article_prompt = """
System Prompt:
We would like to request your feedback on the performance of AI assistant in response to the instruction
and the given input displayed following.
Instruction: [Instruction]
Input: [Input]
Response: [Response]
User Prompt:
Please rate according to the [dimension] of the response to the instruction and the input. Each assistant
receives a score on a scale of 0 to 5, where a higher score indicates higher level of the [dimension]. Please
first output a single line containing the value indicating the scores. In the subsequent line, please provide a
comprehensive explanation of your evaluation, avoiding any potential bias.
"""