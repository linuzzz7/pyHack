import subprocess
a = '17.1.1.1'
result = subprocess.run(['ping', a, '-c', '3'], stderr=subprocess.PIPE, encoding='utf-8')
# Теперь в result.stdout пустая строка, а в result.stderr находится стандартный поток вывода:
print(result.stdout)
print(result.stderr)
print(result.returncode)
