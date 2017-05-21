from music21 import *
 
mf = midi.MidiFile()
mf.open('ex1a.mid')
mf.read()
mf.close()

s = midi.translate.midiFileToStream(mf)
print s.chordify()
s.show()