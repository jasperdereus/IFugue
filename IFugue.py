# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:08:27 2017

"""


from music21 import *

#load music
b = corpus.parse('bach/bwv66.6')

#show sheet music and play
b.show('midi')
b.show()

