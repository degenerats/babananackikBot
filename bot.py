# -*- coding:utf-8 -*-
import telepot
import config
import time
import urllib3
import re

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
bot = telepot.Bot(config.key)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(msg['text'])

    if content_type == 'text':
        human = re.findall(ur'челик', msg['text'])
        dotka = re.findall(ur'дотку', msg['text'])
        if human:
            bot.sendMessage(chat_id, u'членик')
        if dotka:
            bot.sendMessage(chat_id, u'ебаться в сракотан собрались чтоле?')

bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
