from gtts import gTTS
from omxplayer import OMXPlayer as omx

fo = open("ocr.txt","r+")
string = fo.read();
string = ''.join(i for i in string if ord(i)<128)

tts = gTTS(text=string[:500],lang='en-US')
tts.save("read.mp3")
#os.system("mpg321 gm.mp3")
player = omx('read.mp3')
player.play()
