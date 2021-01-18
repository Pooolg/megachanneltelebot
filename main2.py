# -*- coding:utf-8 -*-
import requests
from time import sleep
from bs4 import BeautifulSoup
import random
from functools import reduce

# General
token = 'TOKEN'
channels = [chat_id, 'nameChannel', 'invitecode', chat_id2, 'nameChannel2', 'invitecode2']
#example channels = [-1001358639076, 'Hentai-tai-tai', 'UPsv5P9qj0A8bl0y', -1001419126370, 'Fox Kids 🦊', 'VJYmYmJvK0ktDmqA', -1001209830842, 'Your bitch', 'SByNuhGcaVoreicu']
# t.me/joinchat/UPsv5P9qj0A8bl0y   = > invitecode = "UPsv5P9qj0A8bl0y"
interval = 1800 #sec

# Mega setting
Mega_status = True
body = "&caption=MIKU%20presents%20you%20today%27s%20best%20channels%20(*≧ω≦*)%20Check%20out%20all%20of%20them%20and%20find%20something%20new!"
rand = ["💛", "🌈", "💦", "🍓", "💮", "🍒", "💝", "💕", "🍜"]


while True:
    try:
        def sendomai(channel, tag):
            links = BeautifulSoup(
                requests.get(
                    "https://danbooru.donmai.us/posts?page=" + str(random.randint(1, 1000)) + "&tags=" + tag).content,
                features="html.parser").find_all("article", class_="post-preview")
            try:
                for link in links:
                    if link.attrs['data-file-ext'] == "zip":
                        send = requests.get(
                            "https://api.telegram.org/bot" + token + "/senddocument?chat_id=" + str(channel) + "&document=" +
                            link.attrs['data-file-url'] + "&caption=%23zip").json()
                        print("Отправка...ok = ", send['ok'])
                    elif link.attrs['data-file-ext'] == "mp4":
                        send = requests.get(
                            "https://api.telegram.org/bot" + token + "/sendvideo?chat_id=" + str(channel) + "&video=" +
                            link.attrs[
                                'data-file-url'] + "&caption=%23video").json()
                        print("Отправка...ok = ", send['ok'])
                    else:
                        send = requests.get(
                            "https://api.telegram.org/bot" + token + "/sendphoto?chat_id=" + str(channel) + "&photo=" +
                            link.attrs[
                                'data-file-url'] + "&caption=%23"+tag).json()
                        print("Отправка...ok = ", send['ok'])
            except:
                print("Ошибка отправки пикч danbooru.donmai.us")
        def sendwaifpic(channel, tag):
            try:
                link = requests.get("https://waifu.pics/api/nsfw/"+tag).json()["url"]
            except:
                print("Отправка из waifu.pics...ok = False - ошибка получения пикч")
            try:
                send = requests.get(
                    "https://api.telegram.org/bot" + token + "/sendphoto?chat_id=" + str(channel) + "&photo=" + link+"&caption=%23"+tag).json()
                print("Отправка из waifu.pics...ok = ", send['ok'])
            except:
                print("Отправка из waifu.pics...ok = False - ошибка отправки пикч")

        def sendnekoslife(channel, tag):
            try:
                link = requests.get("https://nekos.life/api/v2/img/"+tag).json()["url"]
            except:
                print("Отправка из nekos.life...ok = False - ошибка получения пикч")
            try:
                send = requests.get(
                    "https://api.telegram.org/bot" + token + "/sendphoto?chat_id=" + str(channel) + "&photo=" + link +"&caption=%23"+tag).json()
                print("Отправка из nekos.life...ok = ", send['ok'])
            except:
                print("Отправка из nekos.life...ok = False - ошибка отправки пикч")

        def sendnekoslifeGIF(channel, tag):
            try:
                link = requests.get("https://nekos.life/api/v2/img/"+tag).json()["url"]
            except:
                print("Отправка из nekos.life...ok = False - ошибка получения пикч")
            try:
                send = requests.get(
                    "https://api.telegram.org/bot" + token + "/senddocument?chat_id=" + str(channel) + "&document=" + link +"&caption=%23"+tag).json()
                print("Отправка из nekos.life...ok = ", send['ok'])
            except:
                print("Отправка из nekos.life...ok = False - ошибка отправки пикч")


        for channel in channels[::3]:
            if channel == -1001473410456 or channel == -1001253280728:
                sendomai(channel, "yuri")
            else:
                sendomai(channel, "sex")
                sleep(1)
        sleep(interval)
        for channel in channels[::3]:
            if channel == -1001473410456 or channel == -1001253280728:
                sendwaifpic(channel, "neko")
            else:
                sendwaifpic(channel, "neko")
                sleep(1)
        sleep(interval)
        for channel in channels[::3]:
            if channel == -1001473410456 or channel == -1001253280728:
                sendnekoslife(channel, "yuri")
            else:
                sendnekoslife(channel, "ero")
                sleep(1)
        sleep(interval)
        for channel in channels[::3]:
            if channel == -1001473410456 or channel == -1001253280728:
                sendnekoslife(channel, "yuri")
            else:
                sendnekoslife(channel, "pussy_jpg")
                sleep(1)
        sleep(interval)
        for channel in channels[::3]:
            if channel == -1001473410456 or channel == -1001253280728:
                sendnekoslife(channel, "yuri")
            else:
                sendnekoslife(channel, "erokemo")
                sleep(1)
        sleep(interval)
        for channel in channels[::3]:
            if channel == -1001473410456 or channel == -1001253280728:
                sendnekoslife(channel, "yuri")
            else:
                sendnekoslife(channel, "blowjob")
                sleep(1)
        sleep(interval)
        for channel in channels[::3]:
            if channel == -1001473410456 or channel == -1001253280728:
                sendnekoslife(channel, "yuri")
            else:
                sendnekoslife(channel, "hentai")
                sleep(1)
        sleep(interval)
        for channel in channels[::3]:
            if channel == -1001473410456 or channel == -1001253280728:
                sendnekoslife(channel, "yuri")
            else:
                sendnekoslife(channel, "eron")
                sleep(1)
        sleep(interval)
        for channel in channels[::3]:
            if channel == -1001473410456 or channel == -1001253280728:
                sendnekoslife(channel, "yuri")
            else:
                sendnekoslifeGIF(channel, "cum")
                sleep(1)
        sleep(interval)
        for channel in channels[::3]:
            if channel == -1001473410456 or channel == -1001253280728:
                sendnekoslife(channel, "yuri")
            else:
                sendnekoslifeGIF(channel, "nsfw_neko_gif")
                sleep(1)
        sleep(interval)
# время для меги:
        """
        for channel in channels[::3]:
            pass #удалене меги
        """
        try:
            if Mega_status == True:
                chname = channels[1::3]
                link_codes = channels[2::3]
                items = []
                body_list = []
                i = 0
                for link_code in link_codes:
                    items.append(
                        "%0A•••%20•••%20•••%20%0A🌼%5B" + rand[random.randint(0, 8)] + chname[i].replace(' ', '%20') +
                        rand[
                            random.randint(0, 8)] + "%5D(https%3A%2F%2Ft.me%2Fjoinchat%2F" + link_code + ")")
                    i += 1
                random.shuffle(items)
                rand_list = reduce(lambda xss, x: xss[:-1] + [xss[-1] + [x]] if len(xss[-1]) < 10 else xss + [[x]],
                                   items,
                                   [[]])
                for i in range(len(rand_list)):
                    body_list_cache = body
                    for n in range(len(rand_list[i])):
                        body_list_cache = body_list_cache + rand_list[i][n]
                    body_list_cache = body_list_cache + "&parse_mode=markdown"
                    body_list.append(body_list_cache)
                for channel in channels[::3]:
                    link = requests.get("https://nekos.life/api/v2/img/ngif").json()["url"]
                    lastID = requests.get(
                        "https://api.telegram.org/bot" + token + "/senddocument?chat_id=" + channel + "&document=" + link +
                        body_list[random.randint(0, 4)]).json()[
                        'result']['message_id']
                print("Мега была отправлена, сплю 5 часов...")
                sleep(18000)
        except:
            print("Ошибка отправки меги...")
    except:
        print("Общая ошибка")
