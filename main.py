
from chatGPT import chat_gpt

snippets = '''
'''

prompt = """
now write a function that 
"""

print(chat_gpt(prompt
               , model="gpt-3.5-turbo"
               , temperature=0.2
               # , max_tokens=1000
               # , top_p=1
               # , frequency_penalty=0
               # , presence_penalty=0
               , role='Python Engineer'
               , expertise='20 years of experience'
               # , learner=False
               # , level='16 year old child'
               # , step_by_step=False
               , explain_logic=True
               , explain_assumptions=True
               , code=True
               , program_language='Python==3.9'
               , docstring=True
               , doctest=True
               , comments=True
               , include_function=True
               , step_by_step_code=True
               , imports=True
               , elegant_code=True
               # , just_code=True
               , exceptions=True
               # , snippet=False
               ))

