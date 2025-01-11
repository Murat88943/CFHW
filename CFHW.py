import subprocess

def read_passwords_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]  # Читаем все строки и убираем лишние пробелы
    except Exception as ex:
        print(f"Ошибка при чтении файла: {ex}")
        return None

def connect_to_wifi(ssid, passwords):
    for password in passwords:
        try:
            # Команда для подключения к Wi-Fi
            command = f'netsh wlan connect name="{ssid}"'
            subprocess.run(command, shell=True)

            # Печатаем пытаемся подключиться с текущим паролем
            print(f"Попытка подключения к Wi-Fi '{ssid}' с паролем '{password}'...")

            # Здесь можно добавить проверку на успешное подключение
        except Exception as ex:
            print(f"Ошибка: {ex}")

if __name__ == "__main__":
    ssid = input("Введите имя сети (SSID): ")
    passwords = read_passwords_from_file("password.txt")  # Чтение паролей из файла
    if passwords is not None:
        connect_to_wifi(ssid, passwords)
    else:
        print("Не удалось получить пароли из файла.")