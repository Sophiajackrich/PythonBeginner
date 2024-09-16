import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):

    print(index, name)

# for name in sr.Microphone.list_microphone_names():

#     print(name)

r = sr.Recognizer() # the object-recognizer

# Create a function for "Try and except" blocks
def speech():

    with sr.Microphone(device_index=1) as source:

        print("Say something")

        try:

            audio = r.listen(source, phrase_time_limit=2, timeout=2)

            query = r.recognize_google(audio, language="en-US")

        except (sr.WaitTimeoutError, sr.UnknownValueError):

            return "Nothing said"

        else:

            return query.lower()
        
text = speech()
print(text)

# with sr.Microphone(device_index = 1) as source: # select and turn on the microphone

#     print('Say something')

#     audio = r.listen(source, phrase_time_limit = 4, timeout = 1) # listen to the sound
#     query = r.recognize_google(audio, language='en-US') # speech recognition
#     print(query.upper()) # displaying the text 


