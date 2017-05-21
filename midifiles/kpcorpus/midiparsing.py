from mido import MidiFile
for msg in MidiFile('ex1a.mid'):
	print msg
	#if msg.type == 'lyrics':
	#	print msg.text
