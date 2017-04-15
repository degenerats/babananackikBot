# -*- coding: utf-8 -*-
import config
import telebot
import time
import re

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            human = re.findall(r'челик', m.text)
            dotka = re.findall(r'дотку', m.text)
            if human:
                bot.send_message(m.chat.id, 'членик')
            if dotka:
                bot.send_message(m.chat.id, 'ебаться в сракотан собрались чтоле?')

if __name__ == '__main__':
     bot = telebot.TeleBot(config.token)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)
