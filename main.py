import telebot
import requests

bot = telebot.TeleBot('8362782279:AAFlv6vFx7enQY2fSX7CdEyJbjWy1wgYU_8')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello world!")


@bot.message_handler(commands=['stat'])
def send_welcome(message):
    bot.send_message(message.chat.id, "statistics is: none")

response = requests.get('https://api.opendota.com/api/heroes').json()

def info(i):
    answer = ''
    answer += 'localized_name '
    answer += i['localized_name']
    answer += '\n'
    answer += 'primary_attr '
    answer += i['primary_attr']
    answer += '\n'
    answer += 'attack_type '
    answer += i['attack_type']
    answer += '\n'
    return answer

@bot.message_handler(commands=['sf'])
def send_welcome(message):
    i = response[10]
    print(i)
    answer = info(i)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['all'])
def send_welcome(message):
    answer = ""
    for i in range(10):
        answer += info(response[i])
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)