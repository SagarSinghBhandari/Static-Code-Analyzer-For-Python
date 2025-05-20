import ast
from parse import jsonify_ast

def syntax_analysis(code: str):
    try:
        tree = ast.parse(code)
        return jsonify_ast(tree)
    except SyntaxError as e:
        return {"SyntaxError": str(e)}
