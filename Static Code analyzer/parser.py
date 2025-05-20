import ast
import graphviz

def createAst(code: str):
    parsed_ast = ast.parse(code)
    return ast.dump(parsed_ast, indent=4)

def createAstTree(code: str):
    parsed_ast = ast.parse(code)
    dot = graphviz.Digraph(comment="AST", format="png")

    def add_node(parent_name, node):
        node_name = str(id(node))
        label = str(type(node).__name__)
        if hasattr(node, 'name'):
            label += '\n' + str(node.name)
        elif hasattr(node, 'id'):
            label += '\n' + str(node.id)
        dot.node(node_name, label)
        dot.edge(parent_name, node_name)

        for field, value in ast.iter_fields(node):
            if isinstance(value, ast.AST):
                add_node(node_name, value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        add_node(node_name, item)

    root_node = str(id(parsed_ast))
    dot.node(root_node, "Module")
    add_node(root_node, parsed_ast)

    return dot
