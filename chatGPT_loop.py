import openai
import os

from codeforces_problem_statement_test_cases import get_problem_statement

# Replace 'your_api_key' with your actual API key
os.environ["OPENAI_API_KEY"] = 'enter API Key'

# Set up the OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a function to generate code using OpenAI GPT-3
def generate_code(prompt):

	# Call the ChatGPT API
	response = openai.Completion.create(
		engine="text-davinci-002",
		prompt=prompt,
		max_tokens=1024,
		n=1,
		stop=None,
		temperature=0.5,
	)
	
	return response
	
# Extract the "Code" portion of the response and write to 'output.py' file
def extract_code(response, output_file="output.cpp"):
	print(response)
	with open("output.cpp",'w') as fl:
		for choice in response.choices:
		    text = choice.text.strip()
		    fl.write(text)
	return text
		    
contest_id = 313
problem_index = 'A'
problem_statement, test_cases = get_problem_statement(contest_id, problem_index)
prompt = "Write the complete C++ code for the following problem statement in a way a professional programmer writes it.\n\n"+"Problem Statement:\n"+problem_statement+"\nSample Test Cases:\n"+test_cases+"\nMake sure of writing the code and nothing else as the entire output contained will be directly submitted to Codeforeces and having text in the output would lead to compilaton error. Also, write the code just one time."
generated_code = generate_code(prompt)
#print(prompt)
code_text = extract_code(generated_code,'output.cpp')

from test_case_execution import parse_test_cases, check_test_cases

test_cases = parse_test_cases('testCases_313A.txt')
passed_cases, failed_cases = check_test_cases(test_cases)

while len(failed_cases) != 0:
	#print(failed_cases)
	failed_content = ''
	for key in failed_cases.keys():
		failed_content += 'Input: '+test_cases[key][0]+'\n'
		failed_content += 'Expected Output: '+failed_cases[key][1]+'\n'
		failed_content += 'Actual Output: '+failed_cases[key][0]+'\n'
		failed_content += '\n'
	
	p = "Modify the below code, such that the test cases which failed for the code also pass.\n\nCode:\n"+code_text+"\n\nFailed Test Cases:\n"+failed_content
	print(p)
	
	generated_code = generate_code(p)
	#print(prompt)
	code_text = extract_code(generated_code,'output.cpp')
	
	passed_cases, failed_cases = check_test_cases(test_cases)
	print("********")
