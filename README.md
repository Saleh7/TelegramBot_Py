# TelegramBot_Py
Telegram Bot APi in Python simple :)

## Example usage
```py
# Here, insert the token Bot Father gave you for your bot.
# https://telegram.me/botfather
token_api = 'your token here'
# Example ->
token_api = '113727310:AAFoSJ6TUa0IlvCs2-4y_wB4EYnWYKttqik'

# You may amendment to the comments
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
```

## Function List

* getUpdates(offset, limit, timeout)
* SendMessage(chat_id, text, disable_web, reply_t, reply_markup)
* commands(Text) 
* run() #never ending loop 
