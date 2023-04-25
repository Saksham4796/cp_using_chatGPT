import os
import re
import subprocess

def parse_test_cases(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    
    inputs = re.findall(r'Input\d+:\n((?:.|\n)*?)(?=Output\d+:)', content)
    inputs = [input_str.strip() for input_str in inputs]
    expected_outputs = re.findall(r'Output\d+:\n((?:.|\n)*?)(?=Input\d+:|\Z)', content)
    expected_outputs = [output_str.strip() for output_str in expected_outputs]

    return list(zip(inputs, expected_outputs))

def run_cpp_code(input_str):
    with open('input.txt', 'w') as input_file:
        input_file.write(input_str)

    os.system('g++ -o output output.cpp')
    process = subprocess.run('./output', stdin=open('input.txt'), stdout=subprocess.PIPE, text=True)

    return process.stdout.strip()

def check_test_cases(test_cases):
    passed_cases = {}
    failed_cases = {}

    for i, (input_str, expected_output_str) in enumerate(test_cases):
        actual_output_str = run_cpp_code(input_str)
        print(actual_output_str)
        if actual_output_str == expected_output_str.strip():
            passed_cases[i] = actual_output_str
        else:
            failed_cases[i] = [actual_output_str,expected_output_str.strip()]

    return passed_cases, failed_cases
'''
if __name__ == "__main__":
    test_cases = parse_test_cases('testCases_313A.txt')
    passed_cases, failed_cases = check_test_cases(test_cases)

    if len(failed_cases) == 0:
        print('All test cases passed.')
    else:
        print(f'Test cases passed: {len(passed_cases)}')
        print(f'Test cases failed: {len(failed_cases)}')
        print('Failed test cases:', failed_cases)
        print(test_cases[1])
'''
