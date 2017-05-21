from music21 import *

mid = converter.parse('ex1a.mid')

sChords = mid.chordify()

sOnlyChords = sChords.getElementsByClass('Chord')

displayPart = stream.Part(id='displayPart')

def appendChordPairs(thisChord, nextChord):
    closePositionThisChord = thisChord.closedPosition(forceOctave=4)
    m = stream.Measure()
    m.append(closePositionThisChord)
    displayPart.append(m)



for i in range(0, len(sOnlyChords) - 1):
    thisChord = sOnlyChords[i]
    nextChord = sOnlyChords[i+1]
    appendChordPairs(thisChord, nextChord)

for c in displayPart.recurse().getElementsByClass('Chord'):
    rn = roman.romanNumeralFromChord(c, key.Key('G'))
    c.addLyric(str(rn.figure))

displayPart.show()

sChords.show()



    
'''

for thisChord in chordified.recurse().getElementsByClass('Chord'):
    print(thisChord.measureNumber, thisChord.beatStr, thisChord)
    if thisChord.isDominantSeventh():
        print 'Dominant seventh'

#chordified.show()
'''
