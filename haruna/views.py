from django.shortcuts import render
import os
from haruna.settings import BASE_DIR
import random
import datetime

SHARES = []
LAST_TIME = None


def get_new_share():
    global SHARES
    global LAST_TIME
    pic_base = '/pics/Wallpaper_All_cp'
    share_base = BASE_DIR + '/haruna/static' + pic_base
    pics = [s for s in os.listdir(share_base)]
    SHARES = []
    for i in range(5):
        SHARES.append(os.path.join(pic_base, random.choice(pics)))
    LAST_TIME = datetime.datetime.now()


def get_shares():
    global SHARES
    global LAST_TIME
    if not LAST_TIME:
        LAST_TIME = datetime.datetime.now()
    delta_time = (datetime.datetime.now() - LAST_TIME).seconds / 60
    if len(SHARES) < 5 or delta_time > 60:
        get_new_share()
    refresh_time = datetime.timedelta(hours=1) - (datetime.datetime.now() - LAST_TIME)
    refresh_minute = refresh_time.seconds / 60
    refresh_second = refresh_time.seconds % 60
    return {'shares': SHARES, 'refresh_time': '%d:%d' % (refresh_minute, refresh_second)}


def index(request):
    content = get_shares()
    return render(request, 'index.html', content)
