import ast
from typing import List, Tuple

def extract_modified_functions(file_path: str) -> List[Tuple[str, str]]:
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            start = node.lineno - 1
            end = node.end_lineno
            func_code = "\n".join(source.splitlines()[start:end])
            functions.append((node.name, func_code))
    
    return functions
