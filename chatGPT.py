import openai
import configparser


def chat_gpt(
        prompt
        , model="gpt-3.5-turbo"
        , temperature=0.8
        , max_tokens=1000
        , top_p=1
        , frequency_penalty=0
        , presence_penalty=0
        , role=''
        , expertise='20 years of experience'
        , learner=False
        , level='12 year old child'
        , step_by_step=False
        , explain_logic=False
        , explain_assumptions=False
        , code=False
        , program_language='Python==3.11'
        , step_by_step_code=False
        , include_function=False
        , docstring=False
        , comments=False
        , doctest=False
        , imports=False
        , elegant_code=False
        , snippet=False
        , just_code=False
        , exceptions=False
):
    """
    Generates a response using the OpenAI ChatGPT model.

    Args:
        :param exceptions: (bool)
        :param just_code: (bool)
        :param elegant_code: (bool)
        :param imports: (bool)
        :param step_by_step_code: (bool)
        :param snippet: (bool)
        :param docstring: (bool)
        :param prompt: (str): The user's input prompt.
        :param model: (str): The model to use for generating the response. Defaults to "gpt-3.5-turbo".
        :param temperature: (float): Controls the randomness of the output. Higher values make the output more random. Defaults to 0.8.
        :param max_tokens: (int): The maximum number of tokens in the response. Defaults to 1000.
        :param top_p: (float): Controls the diversity of the output. Lower values make the output more focused. Defaults to 1.
        :param frequency_penalty: (float): Controls the penalty for using frequent tokens. Higher values make the output more focused. Defaults to 0.
        :param presence_penalty: (float): Controls the penalty for using rare tokens. Higher values make the output more focused. Defaults to 0.
        :param role: (str): The role to act as. Defaults to an empty string.
        :param expertise: (str): The level of expertise to act as. Defaults to "20 years of experience".
        :param learner: (bool): Whether to explain the response as if to a learner. Defaults to False.
        :param level: (str): The level of the learner. Defaults to "12 year old child".
        :param step_by_step: (bool): Whether to provide step-by-step instructions. Defaults to False.
        :param explain_logic: (bool): Whether to explain the logic behind the response. Defaults to False.
        :param explain_assumptions: (bool): Whether to state and explain the assumptions made. Defaults to False.
        :param code: (bool): Whether to include code in the response. Defaults to False.
        :param doctest: (bool): .
        :param comments: (bool): .
        :param include_function: (bool): .
        :param program_language: (str): The programming language to use in the code. Defaults to "Python==3.11".
        :param snippet (bool): Whether to include a code snippet in the response. Defaults to False.

    Returns:
        str: The generated response.

    Raises:
        ValueError: If the API key is not found in the configuration file.

    """
    config = configparser.ConfigParser()
    config.read('../config.ini')

    try:
        api_key = config['chatgpt'].get('api_key')
    except KeyError:
        raise ValueError("API key not found in configuration file.")

    openai.api_key = api_key

    if role != '':
        prompt = f"""Act like an {role} with {expertise}:""" + prompt
    if learner:
        prompt += f"""\nExplain it as if to a {level}:"""
    if step_by_step:
        prompt += "Give step by step instructions:"
    if explain_logic:
        prompt += "\nExplain your logic:"
    if explain_assumptions:
        prompt += "\nState and explain your assumptions:"
    if code:
        prompt += f"\nUse the {program_language} program language:"
        temperature = 0.2
    if step_by_step_code:
        prompt += '\nPerform the following steps:'
        prompt += '\n\tFirst, write the code:'
    if include_function:
        if step_by_step_code:
            prompt += "\n\tThen convert it to a function:"
        else:
            prompt += "\nthe output should be a function:"
    if docstring:
        if step_by_step_code:
            prompt += "\n\tThen add a docstring:"
        else:
            prompt += "\nEnsure to include a docstring:"
    if comments:
        if step_by_step_code:
            prompt += "\n\tThen add comments:"
        else:
            prompt += "\nEnsure to include comments:"
    if doctest:
        if step_by_step_code:
            prompt += "\n\tThen add doctest:"
        else:
            prompt += "\nEnsure to include doctest:"
    if imports:
        if step_by_step_code:
            prompt += "\n\tFinally add any imports used:"
        else:
            prompt += "\nEnsure to add any imports used"
    if exceptions:
        prompt += "\nBe sure to use try/except clauses appropriately"
    if elegant_code:
        prompt += """\nPerform each of the next 10 steps below in order, evaluating and reworking the code:
    1. Code Readability: Look for clear and well-structured code that is easy to understand. The code should be properly indented, have meaningful variable and function names, and follow a consistent coding style.
    2. Modular and Reusable Design: Check if the code follows the principles of modularity and reusability. Well-designed code should be divided into logical modules and functions that can be reused in different contexts without causing side effects.
    3. Performance and Efficiency: Assess if the code is optimized for performance and resource usage. Evaluate algorithms, loops, and data structures to ensure they are efficiently implemented. Avoid unnecessary computations and minimize memory consumption.
    4. Error Handling and Exception Handling: Check if the code handles errors and exceptions effectively. Look for proper error messages, logging of exceptions, and appropriate handling of edge cases to prevent unexpected crashes or incorrect behavior.
    5. Code Maintainability: Evaluate if the code is maintainable in the long term. Look for the presence of inline comments, useful documentation, and version control usage. Consider if the code can be easily updated, extended, or refactored without introducing bugs.
    6. Testability and Test Coverage: Assess if the code has unit tests and if the tests cover a significant portion of the codebase. Good code should have a comprehensive set of tests to ensure reliability and facilitate future modifications.
    7. Security Considerations: Check if the code follows secure coding practices. Look for proper input validation, protection against common vulnerabilities like SQL injection or cross-site scripting, and handling of sensitive data.
    8. Integration and Interoperability: Evaluate if the code interacts seamlessly with external systems or libraries. Check if it adheres to relevant standards, APIs, and protocols.
    9. Documentation: Assess if the code is well-documented, including inline comments, docstrings, and external documentation files. Good documentation helps other developers understand the code and accelerates onboarding.
    10. Code Consistency: Look for consistent coding patterns and adherence to design principles. Consistency in code style, naming conventions, and architectural choices is crucial for maintainability and collaboration.
"""

    if snippet:
        prompt += f"|||{snippet}|||"
    if include_function:
        prompt += '\nThe output should be a function:'
    if just_code:
        prompt += "\nGive the final output code:"
    print(prompt + '\n')

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
