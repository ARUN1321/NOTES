# sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
# sudo apt-get install ffmpeg libav-tools
# sudo pip install pyaudio
from datetime import datetime
import json

a = sr.Recognizer()
run = True
datas = {}
with open("notes.json","r") as i: datas=json.load(i)

while run:
    with sr.Microphone() as i:
        print("Running")
        audiotext = a.listen(i)
        print("Complete")
        try:
            text = a.recognize_google(audiotext)
            print(json.dumps(datas, indent=4))
            b = datetime.now()
            timestamp = datetime.timestamp(b)
            datas["notes"].append({str(timestamp):text})
            with open("notes.json","w") as j:
                j.write(json.dumps(datas, indent=4))
        except KeyboardInterrupt: print("Stopping")
        except:
            print("Error")
            run = False
