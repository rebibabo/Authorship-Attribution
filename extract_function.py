import os
from tree_sitter import Language, Parser
import json
text = lambda node: node.text.decode('utf-8')

def extract_py_file(source_path):
    file_code_list = []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    file_code = f.read()
                    file_code_list.append(file_code)

    return file_code_list

def get_parser(language):
    if not os.path.exists(f'./build/{language}-languages.so'):
        if not os.path.exists(f'./tree-sitter-{language}'):
            os.system(f'git clone https://github.com/tree-sitter/tree-sitter-{language}')
        Language.build_library(
            f'./build/{language}-languages.so',
            [
                f'./tree-sitter-{language}',
            ]
        )
    LANGUAGE = Language(f'./build/{language}-languages.so', language)
    parser = Parser()
    parser.set_language(LANGUAGE)
    os.system(f'rm -rf ./tree-sitter-{language}')
    return parser

def process_intent(file_code, function_code, line):
    space = 0
    for c in file_code.split('\n')[line]:
        if c.isspace():
            space += 1
        else:
            break
    function_code_split = function_code.split('\n')
    new_function_code = function_code_split[0]
    for line in function_code_split[1:]:
        new_function_code += '\n' + line[space:]
    return new_function_code

def extract_function(file_code, parser):
    root_node = parser.parse(bytes(file_code, 'utf8')).root_node
    function_codes = []
    def traverse(node, function_codes):
        if node.type == 'function_definition':
            function_codes.append(process_intent(file_code, text(node), node.start_point[0]))
            return
        for child in node.children:
            traverse(child, function_codes)
    traverse(root_node, function_codes)
    return function_codes

if __name__ == '__main__':
    parser = get_parser('python')
    file_code_list = extract_py_file('unsloth')
    with open('train.jsonl', 'w', encoding='utf-8') as f:
        for file_code in file_code_list:
            function_codes = extract_function(file_code, parser)
            for code in function_codes:
                if 1000 < len(code) < 2000:
                    json.dump({'code': code}, f, ensure_ascii=False)
                    f.write('\n')
