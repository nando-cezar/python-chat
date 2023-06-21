import requests
import json

from PIL import Image
from ia.get_env import print_env

env = print_env(['midJourney_key'])

api_key = env['midJourney_key']

url = "https://api.midjourneyapi.io/v2/"

buffer_size = 1024


def midJourney_imagine(prompt):
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    payload = json.dumps({
        "prompt": prompt
    })

    return requests.request("POST", url + "imagine", headers=headers, data=payload).json().get('taskId')


def midJourney_result(taskId):
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }

    payload = json.dumps({
        "taskId": taskId
    })

    return requests.request("POST", url + "result", headers=headers, data=payload).json().get('imageURL')


# "taskId": "42539724384585875399397193481003"
# https://cdn.midjourney.com/df1a1195-4d0d-47a1-8740-ca9ce0af8042/0_0.png
# https://cdn.discordapp.com/attachments/1115091943374991360/1115092547413487636/yodan___42539724384585875399397193481003___a_boy_laughing_on_th_df1a1195-4d0d-47a1-8740-ca9ce0af8042.png
def midJourney_call(prompt):
    # keep disabled
    # taskId = midJourney_imagine(prompt)
    taskId = '42539724384585875399397193481003'
    return taskId, midJourney_result(taskId)


if __name__ == '__main__':
    print(midJourney_call('Test connection'))
