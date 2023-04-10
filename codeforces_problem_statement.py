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
            examples = problem_statement.find('div', class_='sample-tests').text.strip()
            note = problem_statement.find('div', class_='note').text.strip() if problem_statement.find('div', class_='note') else ""

            # Combine and format the extracted parts
            formatted_statement = f"{title}\n\n{time_limit}\n{memory_limit}\n\n{problem_description}\n\n{input_spec}\n\n{output_spec}\n\n{examples}\n\n{note}"
            return formatted_statement
        else:
            return "Problem statement not found."
    else:
        return f"Error: Unable to fetch problem (HTTP {response.status_code})."

contest_id = 4
problem_index = 'A'
problem_statement = get_problem_statement(contest_id, problem_index)
print(problem_statement)
