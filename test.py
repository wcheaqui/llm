```python
import openai
import configparser
import pytest

def chat_gpt(prompt, model="gpt-3.5-turbo", temperature=0.8, max_tokens=1000, top_p=1, frequency_penalty=0, presence_penalty=0, role='', expertise='20 years of experience', learner=False, level='12 year old child', step_by_step=False, explain_logic=False, explain_assumptions=False, code=False, program_language='Python==3.11', snippet=False):
    """
    Generates a response using the OpenAI ChatGPT model.

    Args:
        prompt (str): The input prompt for the model.
        model (str): The model to use for generating the response. Defaults to "gpt-3.5-turbo".
        temperature (float): Controls the randomness of the output. Higher values make the output more random. Defaults to 0.8.
        max_tokens (int): The maximum number of tokens in the response. Defaults to 1000.
        top_p (float): Controls the diversity of the output. Lower values make the output more focused. Defaults to 1.
        frequency_penalty (float): Controls the penalty for using frequent tokens. Higher values make the output more focused. Defaults to 0.
        presence_penalty (float): Controls the penalty for using tokens that are present in the input. Higher values make the output more focused. Defaults to 0.
        role (str): The role to act like. Defaults to an empty string.
        expertise (str): The level of expertise to act like. Defaults to "20 years of experience".
        learner (bool): Whether to explain the response as if to a learner. Defaults to False.
        level (str): The level of the learner to explain to. Defaults to "12 year old child".
        step_by_step (bool): Whether to give step-by-step instructions. Defaults to False.
        explain_logic (bool): Whether to explain the logic behind the response. Defaults to False.
        explain_assumptions (bool): Whether to state and explain the assumptions made in the response. Defaults to False.
        code (bool): Whether to include code in the response. Defaults to False.
        program_language (str): The programming language to use in the code. Defaults to "Python==3.11".
        snippet (bool): Whether to include a code snippet in the response. Defaults to False.

    Returns:
        str: The generated response.
    """

    config = configparser.ConfigParser()
    config.read('../config.ini')

    try:
        api_key = config['chatgpt'].get('api_key')
    except KeyError:
        raise ValueError("API key not found in configuration file.")

    openai.api_key = api_key

    if role != '':
        prompt = f"""Act like an {role} {expertise}:
""" + prompt
    if learner:
        prompt += f"""
Explain it as if to a {level}:"""
    if step_by_step:
        prompt += "\nGive step by step instructions:"
    if explain_logic:
        prompt += "\nExplain your logic:"
    if explain_assumptions:
        prompt += "\nState and explain your assumptions:"
    if code:
        prompt += f"\nUse the {program_language} program language"
        temperature = 0.2
    if snippet:
        prompt += f"\n|||{snippet}|||"
    print(prompt)

    response = openai.ChatCompletion.create(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    response_text = response.choices[0].message["content"]

    return response_text

def test_chat_gpt():
    # Test case 1
    prompt = "What is the capital of France?"
    response = chat_gpt(prompt)
    assert isinstance(response, str)

    # Test case 2
    prompt = "How do I create a list in Python?"
    response = chat_gpt(prompt, learner=True)
    assert isinstance(response, str)

    # Test case 3
    prompt = "Explain the concept of inheritance in object-oriented programming."
    response = chat_gpt(prompt, explain_logic=True)
    assert isinstance(response, str)

    # Test case 4
    prompt = "Write a function to calculate the factorial of a number."
    response = chat_gpt(prompt, code=True)
    assert isinstance(response, str)

    # Test case 5
    prompt = "What is the output of the following code?\n\n```python\nx = 5\nprint(x + 3)\n```"
    response = chat_gpt(prompt, snippet=True)