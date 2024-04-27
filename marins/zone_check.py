#!/usr/bin/env python3
# import os
#
# list_servers = ['if-dc1.moscow.corp.local',
#                 'if-dc2.moscow.corp.local']
#                 # 'dc1.corp.local',
#                 # 'dc2.corp.local',
#                 # 'dc3.corp.local']
#
#
# def zone_check(server_list):
#     for server in server_list:
#         result = os.popen(f'nslookup corp.local {server}').read()
#         print(result)
#         # if 'nslookup' in result:
#         #     print(server, "Some Errors")
#         # if "can't" in result or "couldn't" in result:
#         #     print(server, "Some Errors")
#         # else:
#         #     print(server, "OK")
#
#
# zone_check(list_servers)

import subprocess


def check_dns_zone(domain_name):
    try:
        # Выполняем команду nslookup для получения информации о доменном имени
        result = subprocess.run(['nslookup', domain_name], capture_output=True, text=True, timeout=10)

        # Проверяем результат выполнения команды nslookup
        if result.returncode == 0:
            # Выводим информацию о DNS-зоне
            print("DNS zone is accessible for:", domain_name)
            print(result.stdout)
        else:
            # Если команда завершилась с ошибкой, выводим сообщение об ошибке
            print("Failed to access DNS zone for:", domain_name)
            print("Error:", result.stderr)
    except subprocess.TimeoutExpired:
        # Если произошел таймаут выполнения команды, выводим сообщение о таймауте
        print("Timeout expired while checking DNS zone for:", domain_name)


# Пример использования функции
check_dns_zone("moscow.corp.local")
