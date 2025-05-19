def validar_email(email):
    """
    Verifica se o e-mail fornecido é válido.
    """
    import re
    padrao = r"[^@]+@[^@]+\.[^@]+"
    return re.match(padrao, email) is not None