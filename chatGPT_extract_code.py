import openai
import os

from codeforces_problem_statement import get_problem_statement

# Replace 'your_api_key' with your actual API key
os.environ["OPENAI_API_KEY"] = 'enter the key here'

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
		    
contest_id = 339
problem_index = 'A'
problem_statement = get_problem_statement(contest_id, problem_index)
generated_code = generate_code("Write the complete C++ code for the following problem statement in a way a professional programmer writes it.\n\n"+problem_statement+"\nMake sure of writing the code and nothing else as the entire output contained will be directly submitted to Codeforeces and having text in the output would lead to compilaton error. Also, write the code just one time.")
extract_code(generated_code,'output.cpp')
