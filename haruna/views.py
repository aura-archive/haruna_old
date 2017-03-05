from django.shortcuts import render
import os
from haruna.settings import BASE_DIR
import random


def index(request):
    pic_base = '/pics/Wallpaper'
    share_base = BASE_DIR + '/haruna/static' + pic_base
    pics = [s for s in os.listdir(share_base)]
    shares = []
    for i in range(5):
        shares.append(os.path.join(pic_base, random.choice(pics)))
    return render(request, 'index.html', {'shares': shares})
