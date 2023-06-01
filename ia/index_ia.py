import openai
from ia.get_env import print_env

env = print_env(['app_key'])

openai.api_key = env['app_key']

model_engine = 'text-davinci-003'


def openia_write(prompt):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5
    )

    return completion.choices[0].text
