import mutagen

# загружаем сам файл
mfile = mutagen.File(input('Введите имя файла >>> '))

# выводим общую информацию
print(mfile.info.pprint())
print("Длина аудио (сек):", mfile.info.length)
print("Частота дискретизации:", mfile.info.sample_rate)
print("Битрейт:", mfile.info.bitrate)
print("Каналов:", mfile.info.channels)
