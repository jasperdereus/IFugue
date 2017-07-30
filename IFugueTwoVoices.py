# -*- coding: utf-8 -*-
"""
Created on Sat May 20 10:06:40 2017

Code to test transformations of subject

@author: Jasper de Reus
"""

from music21 import *
from random import choice, randint



def s_reverse(origStream):
    """Function to reverse music stream

    Args:
        origStream (music21.stream): Stream to be reversed

    Returns:
        newStream (music21.stream): Reversed stream
    """
    newStream = stream.Stream()
    for thisNote in reversed(origStream):
        newNote = note.Note() #note
        newNote.pitch = thisNote.pitch
        newNote.quarterLength = thisNote.quarterLength #time
        newStream.append(newNote)
    return newStream
    
def s_dilate(origStream, multFactTime):
    """Function to change speed

    Args:
        origStream (music21.stream): Stream to be dilated
        multFact (float): Multiplication factor i.e. *0.5 to shorten time by half

    Returns:
        newStream (music21.stream): Reversed stream
    """
    newStream = stream.Stream()
    for thisNote in origStream:
        newNote = note.Note() #note
        newNote.pitch = thisNote.pitch
        newNote.quarterLength = thisNote.quarterLength*multFactTime #time
        newStream.append(newNote)
    return newStream
    

def s_invert(origStream):
    """Function to invert music stream. will take first note as pivot

    Args:
        origStream (music21.stream): Stream to be inverted

    Returns:
        newStream (music21.stream): Inverted stream, pivoted around first note
    """
    newStream = stream.Stream()
    pivotPS = origStream[0].pitch.ps #starting pitch of original stream
    for thisNote in origStream:
        deltaPS = pivotPS - thisNote.pitch.ps #find deviation from original pitch
        newNote = note.Note()
        newNote.pitch.ps = pivotPS + deltaPS #defining new note
        newNote.quarterLength = thisNote.quarterLength #adding time
        newStream.append(newNote)
    return newStream  


def s_trans_random(myStream, mySDilation, nTrans):
    """Demo function for random transformation of stream

    Args:
        myStream (music21.stream): Stream to be transformed
        mySDilation (intlist): List of integers for time transformation
        nTrans (int): number of transformations to use

    Returns:
        myStream (music21.stream): randomly transformed stream
    """    
    for ii in range(nTrans):
        myTrans = randint(0,3)
        if myTrans == 0: 
            myStream = s_reverse(myStream)
        if myTrans == 1:
            myStream = s_reverse(myStream)
        elif myTrans == 2:
            myStream = s_dilate(myStream, choice(mySDilation))
        elif myTrans == 3: 
            myStream = s_invert(myStream)
    return myStream  


mySDilation = [1.0, 1.0, 0.5, 2.0] #options to vary speed of subject
myCompLength = [6,8,12] #length of composition (number of transformed subject repetitions)

mySubject = stream.Stream() #creating subject stream
mySubLetters = ['A3', 'B3', 'A3', 'B3', 'C', 'D', 'E', 'E'] #notes in stream

for ii in range(len(mySubLetters)): #fill mySubject with notes
    myNote = note.Note(mySubLetters[ii])
    if ii <4:
        myNote.quarterLength = 0.5
    mySubject.append(myNote)

#myComposition = stream.Stream() #creating composition based on subject
#for ii in range(choice(myCompLength)):
#    myComposition.append(s_trans_random(mySubject, mySDilation, randint(0,4)))


#myComposition.show('midi')

myFirstPart =  stream.Part() #creating subject stream
mySecondPart = stream.Part()
mySubLetters = ['A3', 'B3', 'A3', 'B3', 'C', 'D', 'E', 'E'] #notes in stream

for ii in range(len(mySubLetters)): #fill mySubject with notes
    myNote = note.Note(mySubLetters[ii])
    myOtherNote = note.Note(mySubLetters[ii])

    if ii <4:
        myNote.quarterLength = 0.5
    myFirstPart.append(myNote)
    mySecondPart.append(myOtherNote)
    
myFirstPart.insert(0, instrument.Clarinet())
mySecondPart.insert(0, instrument.Flute())

s2 = stream.Stream([myFirstPart, mySecondPart])

s2.show('midi')

#>>> c1 = clef.TrebleClef()
#>>> c1.offset = 0.0
#>>> c1.priority = -1
#>>> n1 = note.Note("E-6", type='eighth')
#>>> n1.offset = 1.0
#>>> p1 = stream.Part()
#>>> p1.offset = 0.0
#>>> p1.id = 'embeddedPart'
#>>> p1.append(note.Rest()) # quarter rest
#>>> s2 = stream.Stream([c1, n1, p1])
#>>> s2.duration.quarterLength
#1.5
#>>> s2.show('text')



    


