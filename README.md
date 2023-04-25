# Automating the Code Submission Using chatGPT

This repo performs an experiment where a problem statement is extracted from different competetive coding websites such as `Codesforces` and `Leetcode` and the code for the corresponding problem statement is generated using [chatGPT](https://chat.openai.com/chat). The solution obtained submitted to the competetive coding website using the API.

The python program `codeforces_problem_statement_test_cases.py` is used to extract the problem statement and sample test cases from the [Codeforces](https://codeforces.com/). Similarly, the python program `leetcode_problem_statement.py` is used to extract the problem statement from the [Leetcode](https://leetcode.com/).

Next, `chatGPT_extract_code.py` takes problem statement as input prompt and feeds it to the chatGPT API which generates code coressponding to the input problem statement and stores it in the `output.cpp` file. We have test cases for the problem statement stored in `testCases_XXX.txt` type files. The generated C++ code is executed against all the test case present in the `testCases_XXX.txt` file using `test_case_execution.py` code. If a test case fails then the program is regenerated and until all the test cases pass. This loop for generating the correct program is implemented using `chatGPT_loop.py` file. 
