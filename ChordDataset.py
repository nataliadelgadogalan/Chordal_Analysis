from mido import MidiFile, MidiTrack, Message
import os

mididir = 'midifiles/kpcorpus'
outdir = 'output'
metaTypes = ['track_name', 'time_signature', 'key_signature', 'set_tempo']
metadata = []
firstchord = []
msgList = []

def createMidi(filename):
	mid = MidiFile()
	track = MidiTrack()
	mid.tracks.append(track)
	for msg in metadata:
		track.append(msg)
	track.append(Message('program_change', channel=0, program=0, time=0))
	for msg in msgList:
		track.append(msg)
	filepath = os.path.join(outdir, filename)
	mid.save(filepath)

def printmsgs():
	for filename in os.listdir(mididir):
		if not os.path.exists(outdir):
			os.makedirs(outdir)
		if filename.endswith('.mid'):
			chordindex = 0
			filepath = os.path.join(mididir, filename)
			for msg in MidiFile(filepath):
				print msg
		break

for filename in os.listdir(mididir):
	metadata = []
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	if filename.endswith('.mid'):
		chordindex = 0
		filepath = os.path.join(mididir, filename)
		mid = MidiFile(filepath)
		for track in mid.tracks:
			for msg in track:
				#print msg
				msgList.append(msg)
				if msg.type in metaTypes:
					metadata.append(msg)
				if msg.type == 'note_on':
					if msg.velocity != 0:
						firstchord.append(msg)
					else:
						firstchord = []
				if msg.type == 'lyrics':
					if chordindex != 0:
						chordfile = '{}_{}_{}.mid'.format(filename[:-4],chordindex, chordlabel)
						notestoremove = len(firstchord) + 1
						msgList = msgList[:-notestoremove]
						createMidi(chordfile)
						msgList = firstchord
						firstchord = []
						chordlabel = msg.text
						chordindex = chordindex + 1
					else:
						chordlabel = msg.text
						chordindex = 1
				if msg.type == 'end_of_track':					
					chordfile = '{}_{}_{}.mid'.format(filename[:-4],chordindex, chordlabel)
					createMidi(chordfile)
					msgList = []
				#print '\t{}'.format(msg.text)
