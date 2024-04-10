#!/usr/bin/env python
from pytube import YouTube
from pydub import AudioSegment

# Введите ссылку на YouTube видео
url = input("Введите ссылку на YouTube видео: ")

# Создание объекта YouTube
yt = YouTube(url)

type_file = int(input('Выбор:\n1. Если надо загрузить Аудио - mp3.\n2. Если надо загрузить Видео - mp4.\n>>> '))

if type_file == 1:
    print("Загрузка аудио...")
    audio = yt.streams.filter(only_audio=True).first()
    audio_file = audio.download()
    print("Аудио загружено!")
    # Конвертация в MP3
    print("Конвертация в MP3...")
    song = AudioSegment.from_file(audio_file, format="mp4")
    song.export(f"{yt.title}.mp3", format="mp3")
    print("Конвертация завершена!")
elif type_file == 2:
    # Загрузите видео
    print("Загрузка видео...")
    yt.streams.first().download()
    print("Видео загружено!")
else:
    print('Неверный выбор!')
