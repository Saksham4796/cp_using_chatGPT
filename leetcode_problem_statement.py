import requests
import json
from bs4 import BeautifulSoup

def get_leetcode_problem_statement(slug):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.3",
    }

    query = '''
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            title
            content
            difficulty
        }
    }
    '''
    variables = {
        "titleSlug": slug
    }

    payload = {
        "operationName": "getQuestionDetail",
        "query": query,
        "variables": variables
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = json.loads(response.text)
        problem = data['data']['question']
        if problem:
            soup = BeautifulSoup(problem['content'], 'html.parser')
            content = "\n".join(soup.stripped_strings)

            problem_statement = f"{problem['title']} (ID: {problem['questionId']}, Difficulty: {problem['difficulty']})\n\n{content}"
            return problem_statement
        else:
            return "Problem not found."
    else:
        return f"Error: Unable to fetch problem (HTTP {response.status_code})."

'''
slug = "two-sum"
problem_statement = get_leetcode_problem_statement(slug)
print(problem_statement)
'''
