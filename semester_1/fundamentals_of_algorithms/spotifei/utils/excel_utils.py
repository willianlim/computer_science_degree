import pandas as pd
import os

CAMINHO_DB = "data/database.xlsx"

def ler_planilha(nome_planilha):
    """
    Lê uma planilha específica do arquivo Excel.
    """
    try:
        return pd.read_excel(CAMINHO_DB, sheet_name=nome_planilha)
    except FileNotFoundError:
        print(f"❌ Arquivo {CAMINHO_DB} não encontrado.")
        return pd.DataFrame()
    except ValueError:
        print(f"❌ Planilha '{nome_planilha}' não encontrada no arquivo.")
        return pd.DataFrame()


def salvar_planilha(nome_planilha, df, coluna_unica=None):
    """
    Adiciona apenas novos dados a uma planilha específica do arquivo Excel,
    preservando as abas existentes e evitando duplicatas com base em uma coluna ou conjunto de colunas.

    :param nome_planilha: Nome da aba no Excel.
    :param df: DataFrame com os dados a serem salvos.
    :param coluna_unica: Nome da coluna ou lista de colunas usadas para verificar duplicatas.
    """
    if df.empty:
        print(f"⚠️ Nenhum dado para salvar na planilha '{nome_planilha}'.")
        return

    try:
        # Lê os dados existentes da aba, se houver
        if os.path.exists(CAMINHO_DB):
            try:
                df_existente = pd.read_excel(CAMINHO_DB, sheet_name=nome_planilha)

                # Verifica se há duplicatas com base na coluna ou colunas especificadas
                if coluna_unica:
                    if isinstance(coluna_unica, str):
                        # Remove registros antigos com base na coluna única
                        df_existente = df_existente[~df_existente[coluna_unica].isin(df[coluna_unica])]
                    elif isinstance(coluna_unica, list):
                        # Remove registros antigos com base em múltiplas colunas
                        df_existente = df_existente[
                            ~df_existente[coluna_unica].apply(tuple, axis=1).isin(df[coluna_unica].apply(tuple, axis=1))
                        ]

                # Combina os DataFrames, preservando os registros existentes
                df = pd.concat([df_existente, df], ignore_index=True)

            except ValueError:
                # Caso a aba não exista, cria uma nova
                pass

        # Salva o DataFrame atualizado na aba especificada
        with pd.ExcelWriter(CAMINHO_DB, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
            df.to_excel(writer, index=False, sheet_name=nome_planilha)

        print(f"✅ Dados salvos com sucesso na planilha '{nome_planilha}'.")
    except Exception as e:
        print(f"❌ Erro ao salvar a planilha '{nome_planilha}': {e}")


def atualizar_planilha(nome_planilha, identificador_coluna, identificador_valor, novos_dados):
    """
    Atualiza um registro existente em uma planilha específica do arquivo Excel.
    
    :param nome_planilha: Nome da aba no Excel.
    :param identificador_coluna: Nome da coluna que identifica o registro único (ex.: 'id_musica').
    :param identificador_valor: Valor único que identifica o registro a ser atualizado.
    :param novos_dados: Dicionário com os novos valores para atualizar no registro.
    """
    try:
        # Lê os dados existentes da aba
        if os.path.exists(CAMINHO_DB):
            df = pd.read_excel(CAMINHO_DB, sheet_name=nome_planilha)

            # Verifica se o registro existe
            if identificador_valor in df[identificador_coluna].values:
                # Localiza o índice do registro a ser atualizado
                index = df[df[identificador_coluna] == identificador_valor].index[0]

                # Atualiza os valores do registro
                for coluna, valor in novos_dados.items():
                    if coluna in df.columns:
                        df.at[index, coluna] = valor

                # Salva o DataFrame atualizado no Excel
                with pd.ExcelWriter(CAMINHO_DB, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                    df.to_excel(writer, index=False, sheet_name=nome_planilha)
                print(f"✅ Registro atualizado com sucesso na planilha '{nome_planilha}'.")
            else:
                print(f"❌ Registro com {identificador_coluna} = {identificador_valor} não encontrado na planilha '{nome_planilha}'.")
        else:
            print(f"❌ Arquivo {CAMINHO_DB} não encontrado.")
    except Exception as e:
        print(f"❌ Erro ao atualizar o registro na planilha '{nome_planilha}': {e}")


def remover_registro(nome_planilha, condicoes):
    """
    Remove registros de uma planilha específica do arquivo Excel com base em múltiplas condições.

    :param nome_planilha: Nome da aba no Excel.
    :param condicoes: Dicionário onde as chaves são os nomes das colunas e os valores são os valores a serem removidos.
    """
    try:
        # Verifica se o arquivo existe
        if os.path.exists(CAMINHO_DB):
            # Lê os dados existentes da aba
            df = pd.read_excel(CAMINHO_DB, sheet_name=nome_planilha)

            # Verifica se as colunas existem
            for coluna in condicoes.keys():
                if coluna not in df.columns:
                    print(f"❌ Coluna '{coluna}' não encontrada na planilha '{nome_planilha}'.")
                    return

            # Filtrar o DataFrame para remover apenas os registros que atendem a todas as condições
            condicao_combinada = pd.Series(True, index=df.index)
            for coluna, valor in condicoes.items():
                condicao_combinada &= (df[coluna] == valor)
            df = df[~condicao_combinada]

            # Salva o DataFrame atualizado no Excel
            with pd.ExcelWriter(CAMINHO_DB, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                df.to_excel(writer, index=False, sheet_name=nome_planilha)
            print(f"✅ Registro removido da planilha '{nome_planilha}' com sucesso!")
        else:
            print(f"❌ Arquivo {CAMINHO_DB} não encontrado.")
    except Exception as e:
        print(f"❌ Erro ao remover o registro na planilha '{nome_planilha}': {e}")