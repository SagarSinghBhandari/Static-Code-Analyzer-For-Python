import re

# Token specification with proper order (MISMATCH last)
token_specification = [
    ('NUMBER',      r'\b\d+(\.\d*)?\b'),         # Integer or decimal number
    ('ID',          r'\b[A-Za-z_][A-Za-z_0-9]*\b'),  # Identifiers
    ('STRING',      r'(\".*?\"|\'.*?\')'),       # String literals (simple)
    ('OP',          r'[\+\-\*\=/<>%]+'),          # Operators
    ('LPAREN',      r'\('),                       # Left Parenthesis
    ('RPAREN',      r'\)'),                       # Right Parenthesis
    ('COMMA',       r','),                        # Comma
    ('NEWLINE',     r'\n'),                       # Line endings
    ('SKIP',        r'[ \t]+'),                   # Skip spaces and tabs
    ('MISMATCH',    r'.'),                        # Any other character (catch all, must be last)
]

tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

def lexical_analysis(code):
    tokens = []
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            tokens.append(f"NUMBER: {value}")
        elif kind == 'ID':
            tokens.append(f"ID: {value}")
        elif kind == 'STRING':
            tokens.append(f"STRING: {value}")
        elif kind == 'OP':
            tokens.append(f"OP: {value}")
        elif kind == 'LPAREN':
            tokens.append("LPAREN: (")
        elif kind == 'RPAREN':
            tokens.append("RPAREN: )")
        elif kind == 'COMMA':
            tokens.append("COMMA: ,")
        elif kind == 'NEWLINE' or kind == 'SKIP':
            continue  # Ignore whitespace and newlines
        elif kind == 'MISMATCH':
            tokens.append(f"Unexpected character: {value}")
    return tokens
