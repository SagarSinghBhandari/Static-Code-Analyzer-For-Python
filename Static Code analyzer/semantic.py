import ast
import builtins

class SemanticAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.defined_vars = set()
        # Include Python built-in functions and constants as predefined
        self.predefined = set(dir(builtins))
        self.errors = []

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            if node.id not in self.defined_vars and node.id not in self.predefined:
                self.errors.append(f"Use of undefined variable '{node.id}' at line {node.lineno}")
        elif isinstance(node.ctx, ast.Store):
            self.defined_vars.add(node.id)
        self.generic_visit(node)

def semantic_analysis(code):
    try:
        tree = ast.parse(code)
        analyzer = SemanticAnalyzer()
        analyzer.visit(tree)
        if analyzer.errors:
            return "\n".join(analyzer.errors)
        else:
            return "No semantic errors found."
    except Exception as e:
        return f"Semantic analysis failed: {e}"
