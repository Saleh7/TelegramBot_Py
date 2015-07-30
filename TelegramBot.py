#author Saleh Bin Homoud
#copyright 2015
#Twitter (iPain7)

import requests
import json
from time import sleep

# Here, insert the token Bot Father gave you for your bot.
# https://telegram.me/botfather
token_api = 'your token here'
url = 'https://api.telegram.org/bot%s/' % token_api

"""
:param integer|None offset
:param integer|None limit | Defaults to 100
:param integer|None timeout
:tutorial https://core.telegram.org/bots/api#getupdates
"""
def getUpdates(offset=None, limit=None, timeout=None):
    Params = {
        'offset': offset,
        'limit': limit,
        'timeout': timeout
    }
    return json.loads(requests.get(url + 'getUpdates', params=Params).content.decode('utf8'))

"""
:param integer  chat_id
:param string   text
:param boolean  disable_web | true,false
:param integer|None  reply_t
:param ReplyKeyboard  reply_markup
:tutorial https://core.telegram.org/bots/api#sendmessage
"""
def SendMessage(chat_id, text, disable_web=None, reply_t=None, reply_markup=None):
    Params = {
        'chat_id': chat_id,
        'text': text,
        'disable_web_page_preview': disable_web,
        'reply_to_message_id': reply_t,
        'reply_markup': reply_markup
    }
    return requests.get(url + 'sendMessage', params=Params)

## commands Send user
def commands(Text):
    if(Text):
        if '/start' in Text or '/help' in Text:
            message = 'Welcome My Bot \n Click here test - /test \n list bot - /list'
            return message

        if '/test' in Text:
            message = 'Yes, it is working properly \n goodbye :)'
            return message

        if '/list' in Text:
            message = '/start - start \n /help - help \n /test - test \n-'
            return message
"""
## never ending loop ##
"""
def run ():
    last_update = 0
    while True:
        get_updates = getUpdates()
        for update in get_updates['result']:
            if last_update < update['update_id']:
                last_update = update['update_id']
                if 'message' in update:
                    chat_id = update['message']['chat']['id']
                    text = update['message']['text']
                    command = commands(text)
                    if(command):
                        getUpdates(last_update+1)
                        SendMessage(chat_id,command)
        # New updates every 1 second
        sleep(1)

#Run loop function
run()
