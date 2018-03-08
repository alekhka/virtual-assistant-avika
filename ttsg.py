from gtts import gTTS
from omxplayer import OMXPlayer as omx

import os
import time
import sys
import subprocess

fo = open("reco.txt","r+")
string = fo.read();
print string

string = string.lower()
#tts = gTTS(text=string,lang='en-US')
#tts.save("gm.mp3")
#os.system("mpg321 gm.mp3")
#player = omx('gm.mp3')
#player.play()
print string



if string[:16] == 'avika play music':
    paar = omx('p.mp4')
    paar.play()
    #time.sleep(10)
    #paar.quit()

elif string[:31] == 'avika play hymn for the weekend':
    hymn = omx('hymn.mp3')
    hymn.play()
    #time.sleep(10)
    #hymn.quit()

elif string[:24] == 'avika play cheap thrills':
    cheap = omx('cheap.mp3')
    cheap.play()
    #time.sleep(10)
    #cheap.quit()

elif string == 'avika navigate' or string == 'avika navigator' or string == 'navigate':
    os.system("lxterminal -e 'python navi.py'")
    #proc = subprocess.Popen([sys.executable, 'navi.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    #pid = proc.pid
    #time.sleep(10)
    #proc.terminate()

elif string == 'avika read the book' or string == 'avika read book' or string == 'avika read a book' or string == 'avika read' or string == 'read the book' or string == 'read book' or string == 'read a book' or string == 'read':
    os.system("lxterminal -e 'python ocr.py'")
    
elif string == 'avika switch off bedroom light' or string == 'avika switch on bedroom light' or string == 'avika turn off bedroom light' or string == 'avika turn on bedroom light' or string == 'switch off bedroom light' or string == 'switch on bedroom light' or string == 'turn off bedroom light' or string == 'turn on bedroom light':
    os.system("python sewrite.py 3")

elif string == 'avika switch off kitchen light' or string == 'avika switch on kitchen light' or string == 'avika turn off kitchen light' or string == 'turn on kitchen light' or string == 'switch off kitchen light' or string == 'switch on kitchen light' or string == 'turn off kitchen light' or string == 'turn on kitchen light':
    os.system("python sewrite.py 2")

elif string == 'avika close the door' or string == 'avika open the door' or string == 'close the door' or string == 'open the door':
    os.system("python sewrite.py 1")

else:
    print "NOTA"
    
#player.quit()
fo.close()
