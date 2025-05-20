def is_valid_syntax(tokens):
    """
    Accepts only expressions like: ID = NUMBER + ID or ID = NUMBER
    """
    if len(tokens) not in [3, 5]:
        return False

    if tokens[0][0] != 'ID' or tokens[1][0] != 'ASSIGN':
        return False

    if len(tokens) == 3:
        return tokens[2][0] in ['NUMBER', 'ID']

    if tokens[2][0] not in ['NUMBER', 'ID']:
        return False
    if tokens[3][0] not in ['PLUS', 'MINUS', 'MULT', 'DIV']:
        return False
    if tokens[4][0] not in ['NUMBER', 'ID']:
        return False

    return True
