#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import time
from random import randrange
import random

textlist = 'jugadoresUY.txt'
while 1 == 1:
        time.sleep(randrange(12,16))
        with open('actual.txt', 'w') as d:
                with open(textlist) as f:
                        lines = f.readlines()
                        jugador = random.choice(lines)
                        d.write(jugador)
                        f.close
                        d.close

