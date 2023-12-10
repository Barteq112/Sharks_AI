import ast
import os

class FunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.functions_list = []

    def visit_FunctionDef(self, node):
        function_name = node.name
        function_code = ast.unparse(node)
        self.functions_list.append((function_name, function_code))

def process_python_file(filepath, visitor):
    with open(filepath, 'r', encoding='UTF-8', errors='ignore') as file:
        source_code = file.read()
    try:
        parsed_code = ast.parse(source_code)
    except SyntaxError as e:
        print(f"Syntax error in file: {filepath}")
        print(e)
        return
    visitor.visit(parsed_code)

def scan_django_project(path):
    visitor = FunctionVisitor()
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                process_python_file(os.path.join(root, file), visitor)
    return visitor.functions_list

def find_functions_in_django_project(django_project_path):
    return scan_django_project(django_project_path)

#
