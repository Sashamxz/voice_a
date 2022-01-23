#!/bin/bash
import os
import random
import speech_recognition


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.6


def listen_command():
    """the function will return recognize command"""
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source= mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='es_ES').lower()
            return query    
    except speech_recognition.UnknownValueError:
        return 'What did you say... ?'



def hello_w():
    return 'Bonjour!'


def play_music():
    """play a ranom song"""
    files = os.listdir('mz')
    random_file = f'mz/{random.choice(files)}'
    os.system(f'vlc {random_file}')
    return f' PLAY- {random_file.split("/")[-1]}' 


def create_task():
    print ('що добавити в список справ?')
    query = listen_command()
    
    with open('toddo.txt', 'a' ) as file:
        file.write(f'{query}\n') 
    
    return f'Завдання- {query} - додано'    



def main():
    query = listen_command()
    if query == 'привіт':
        print(hello_w())

    elif query == 'додати завдання':
        print(create_task())

    elif 'музику' in query:
        print(play_music()) 

    else:
        print(query)



if __name__ == '__main__':
    main()
