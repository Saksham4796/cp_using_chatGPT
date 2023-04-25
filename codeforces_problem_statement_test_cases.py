import requests
from bs4 import BeautifulSoup

def get_problem_statement(contest_id, problem_index):
    problem_url = f"https://codeforces.com/problemset/problem/{contest_id}/{problem_index}"
    response = requests.get(problem_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        problem_statement = soup.find('div', class_='problem-statement')

        if problem_statement:
            # Extract specific parts of the problem statement
            title = problem_statement.find('div', class_='title').text
            time_limit = problem_statement.find('div', class_='time-limit').text.strip()
            memory_limit = problem_statement.find('div', class_='memory-limit').text.strip()
            problem_description = ' '.join(problem_statement.find('div', class_=None).stripped_strings)
            input_spec = problem_statement.find('div', class_='input-specification').text.strip()
            output_spec = problem_statement.find('div', class_='output-specification').text.strip()

            # Extract test cases
            input_tests = problem_statement.find_all('div', class_='input')
            output_tests = problem_statement.find_all('div', class_='output')
            #print(input_tests)
            #print(output_tests)
            test_cases = []
            k = 1
            for i, o in zip(input_tests, output_tests):
                pre_tag_i = i.find('pre')
                if pre_tag_i:
                    input_content = 'Input'+str(k)+':\n'
                    for item in pre_tag_i.contents:
                        if item.name == 'br':
                            input_content += '\n'
                        else:
                            input_content += str(item)
                    #print(input_content)
                
                pre_tag_o = o.find('pre')
                if pre_tag_o:
                    output_content = 'Output'+str(k)+':\n'
                    for item in pre_tag_o.contents:
                        if item.name == 'br':
                            output_content += '\n'
                        else:
                            output_content += str(item)
                    #print(output_content)
                    
                test_cases.append(input_content+'\n'+output_content)
                k += 1

            test_cases_str = "\n\n".join(test_cases)

            note = problem_statement.find('div', class_='note').text.strip() if problem_statement.find('div', class_='note') else ""

            # Combine and format the extracted parts
            formatted_statement = f"{title}\n\n{time_limit}\n{memory_limit}\n\n{problem_description}\n\n{input_spec}\n\n{output_spec}\n\n{note}"
            return formatted_statement, test_cases_str
        else:
            return "Problem statement not found."
    else:
        return f"Error: Unable to fetch problem (HTTP {response.status_code})."

'''        
# Example usage
contest_id = 266
problem_index = "B"
problem_statement, test_cases = get_problem_statement(contest_id, problem_index)
print(problem_statement)
print(test_cases)
'''
