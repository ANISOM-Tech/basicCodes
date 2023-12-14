import pyttsx3 as pts
# initiating the narrator
engine = pts.init('sapi5')

# selecting the voice of the narrator
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # this gives a male voice
# engine.setProperty('voice', voices[1].id)  # this gives a female voice

# setting the speaking rate of the narrator
rate = engine.getProperty('rate')
# print(rate)
engine.setProperty('rate', 200)
"""
# setting the volume of the narrator
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', 1)
"""
"""
Here we will open text file in a variable named 'f'.
"""
f = open('Where the mind is without fear.txt')
txt = f.read()
f.close()


def speaker(topic):
    engine.say(topic)
    # engine.save_to_file(topic, 'Where the mind is without fear.mp3')  # saving the narration as an audio file
    engine.runAndWait()


speaker(txt)