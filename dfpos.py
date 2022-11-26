# DF Portable Operation System
# Портативная Операционная Система от DF

# Import Libs

import json
import time as t
from colorama import Fore
from colorama import Back
import os
import sys
try:
    import psutil
    psutilStatus = 1
except:
    psutilStatus = 0
import platform
import dfpos_tools

from colorama import init
init(convert=True)

import getpass

# Variables

version = "0.1.8"

if psutilStatus == 1:
    memory = psutil.virtual_memory()
    memory = int(memory.total / 1000000000)
    if platform.system() == "Windows":
        total_space = int(psutil.disk_usage("C: ").total/(1024 * 1024 * 1024))
    else:
        total_space = "Error 101 : Не удалось загрузить информацию о диске"

else:
    total_space = "Error 101 : Не удалось загрузить информацию о диске"

global_system = platform.system()

# Import Files

with open("config.json", "r", encoding='utf-8') as config_read_file:
    config_read_data = json.load(config_read_file)

with open("user.json", "r", encoding='utf-8') as user_read_file:
    user_data= json.load(user_read_file)

# Functions

def clear():
    print("\n" * 30)

# Code
# First Launch
if config_read_data['first_launch'] == True:
    print("Добро пожаловать в DFPOS!")
    install_acsess = input(Fore.YELLOW + "Согласны установить операционную систему(Y/N)? " + Fore.RESET)
    if install_acsess == "y" or install_acsess == "Y":
        print("Загрузка начнется через 3 секунды...")
        t.sleep(3)
        print(Back.GREEN + "Установка" + Back.RESET + " [##########]")
        t.sleep(10)
        print(Back.GREEN + "Установка" + Back.RESET + " [" + Fore.YELLOW + "#" + Fore.RESET + "#########]")
        t.sleep(10)
        print(Back.GREEN + "Установка" + Back.RESET + " [" + Fore.YELLOW + "##" + Fore.RESET + "########]")
        t.sleep(10)
        print(Back.GREEN + "Установка" + Back.RESET + " [" + Fore.YELLOW + "###" + Fore.RESET + "#######]")
        t.sleep(10)
        print(Back.GREEN + "Установка" + Back.RESET + " [" + Fore.YELLOW + "####" + Fore.RESET + "######]")
        t.sleep(10)
        print(Back.GREEN + "Установка" + Back.RESET + " [" + Fore.YELLOW + "#####" + Fore.RESET + "#####]")
        t.sleep(10)
        print(Back.GREEN + "Установка" + Back.RESET + " [" + Fore.YELLOW + "######" + Fore.RESET + "####]")
        t.sleep(10)
        print(Back.GREEN + "Установка" + Back.RESET + " [" + Fore.YELLOW + "#######" + Fore.RESET + "###]")
        t.sleep(10)
        print(Back.GREEN + "Установка" + Back.RESET + " [" + Fore.YELLOW + "########" + Fore.RESET + "##]")
        t.sleep(10)
        print(Back.GREEN + "Установка" + Back.RESET + " [" + Fore.YELLOW + "#########" + Fore.RESET + "#]")
        t.sleep(10)
        print(Back.GREEN + "Установка" + Back.RESET + " [" + Fore.YELLOW + "##########" + Fore.RESET + "]")
        config_read_data['first_launch'] = False
        with open("config.json", "w", encoding='utf-8') as config_write_file:
            json.dump(config_read_data, config_write_file, indent=2)
        print(Fore.GREEN + "Установка завершена!")
        print("Перезапустите программу для запуска Операционной Системы.")
        input("Нажмите на Enter для выхода...")
    elif install_acsess == "n" or install_acsess == "N":
        print(Fore.RED + "Установка DFPOS отменена! Программа закроется через 10 секунд.")
        t.sleep(10)
        sys.exit(30351)
    else:
        print(Fore.RED + "Вы ввели неправильный вариант! Программа закроется через 10 секунд.")
        t.sleep(10)
        sys.exit(30351)
elif config_read_data['first_launch'] == False:
    print("Добро пожаловать в DFPOS! ")
    if user_data['registred'] == False:
        print("Похоже у вас нет активных пользователей. Давайте создадим нового! ")
        user_reg = input("\nПридумайте Имя-Пользователя : ")
        while True:
            pswd_reg = input("Придумайте Пароль : ")
            pswd_reg2 = input("Подтвердите Пароль : ")
            if pswd_reg != pswd_reg2:
                print(Fore.RED + "Пароли не совпадают! \n")
            elif pswd_reg == pswd_reg2:
                print(Fore.GREEN + "Вы успешно создали нового пользователя : " + user_reg)
                print("Перезайдите для запуска Операционной Системы")
                input("Нажмите на Enter для выхода...")
                with open("user.json", "w", encoding='utf-8') as user_write_file:
                    user_data['username'] = user_reg
                    user_data['password'] = pswd_reg
                    user_data['registred'] = True
                    json.dump(user_data, user_write_file)
                break
    elif user_data['registred'] == True:
        while True:
            if (input("\nВведите имя пользователя : ") == user_data['username']):
                if config_read_data['show_password'] == False:
                    w_pass = getpass.getpass("Введите пароль : ")
                else:
                    w_pass = input("Введите пароль : ")

                if (w_pass == user_data['password']):
                    print("Вы успешно вошли! \n")
                    break
                else:
                    print(Fore.RED + "Вы ввели неправильный пароль! " + Fore.RESET)
            else:
                print(Fore.RED + "Неизвестный пользователь!" + Fore.RESET)

        # System

        while True:
            if config_read_data['show_username'] == True:
                cmd = input(user_data['username'] + " " + config_read_data['cmd_symbol'] + " ")
            elif config_read_data['show_username'] == False:
                cmd = input(" " + config_read_data['cmd_symbol'] + " ")

            if cmd == "settings":
                while True:
                    if config_read_data['show_username'] == True:
                        cmd_settings = input(user_data['username'] + "/settings " + config_read_data['cmd_symbol'] + " ")
                    elif config_read_data['show_username'] == False:
                        cmd_settings = input("settings " + config_read_data['cmd_symbol'] + " ")

                    if cmd_settings == "exit":
                        print("Выход из настроек...")
                        break
                    elif cmd_settings == "help":
                        print("\nДоступные команды настроек: \n")
                        print("exit - Выход")
                        print("change password - Смена пароля")
                        print("change username - Смена имени пользователя")
                        print("change symbol - Смена символа ввода")
                        print("show username - Вкл/выкл отображения имени пользователя")
                        print("show password - Вкл/выкл отображения пароля при вводе")
                        print("\n")
                    elif cmd_settings == "change password":
                        if input("Введите текущий пароль: ") == user_data['password']:
                            pswd_new = input("Введите новый пароль: ")
                            if pswd_new == input("Подтвердите новый пароль: "):
                                print(Fore.GREEN + "Ваш пароль успешно изменен!" + Fore.RESET)
                                user_data['password'] = pswd_new
                                with open("user.json", "w", encoding='utf-8') as user_write_file:
                                    json.dump(user_data, user_write_file)
                            else:
                                print(Fore.RED + "Пароли не совпадают! " + Fore.RESET)
                        else:
                            print(Fore.RED + "Вы ввели неверный пароль!" + Fore.RESET)
                    elif cmd_settings == "change symbol":
                        symbol_new = input("Введите новый символ для ввода(Без пробелов!): ")
                        config_read_data['cmd_symbol'] = symbol_new
                        with open("config.json", "w", encoding='utf-8') as config_write_file:
                            json.dump(config_read_data, config_write_file)
                        print(Fore.GREEN + "Символ ввода успешно изменён на " + Fore.YELLOW + symbol_new + Fore.GREEN + "!" + Fore.RESET)
                    elif cmd_settings == "change username":
                        if input("Введите текущий пароль: ") == user_data['password']:
                            username_new = input("Введите новое имя пользователя: ")
                            user_data['username'] = username_new
                            with open("user.json", "w", encoding='utf-8') as user_write_file:
                                json.dump(user_data, user_write_file)
                                print(Fore.GREEN + "Ваше имя пользователя успешно изменено на " + Fore.YELLOW + username_new + Fore.GREEN + "!" + Fore.RESET)
                        else:
                            print(Fore.RED + "Вы ввели неверный пароль!" + Fore.RESET)
                    elif cmd_settings == "show username":
                        if config_read_data['show_username'] == True:
                            config_read_data['show_username'] = False
                            with open("config.json", "w", encoding='utf-8') as config_write_file:
                                json.dump(config_read_data, config_write_file)
                            print(Fore.GREEN + "Режим показа имени пользователя успешно" + Fore.YELLOW + " выключен" + Fore.GREEN + "!" + Fore.RESET)
                        elif config_read_data['show_username'] == False:
                            config_read_data['show_username'] = True
                            with open("config.json", "w", encoding='utf-8') as config_write_file:
                                json.dump(config_read_data, config_write_file)
                            print(
                                Fore.GREEN + "Режим показа имени пользователя успешно" + Fore.YELLOW + " включен" + Fore.GREEN + "!" + Fore.RESET)
                        else:
                            print(Fore.RED + "Такой команды не существует! Используй help для получения списка доступных команд." + Fore.RESET)
                    elif cmd_settings == "show password":
                        if config_read_data['show_password'] == True:
                            config_read_data['show_password'] = False
                            with open("config.json", "w", encoding='utf-8') as config_write_file:
                                json.dump(config_read_data, config_write_file)
                            print(Fore.GREEN + "Режим показа пароля успешно " + Fore.YELLOW + "выключен" + Fore.GREEN + "!" + Fore.RESET)
                        elif config_read_data['show_password'] == False:
                            config_read_data['show_password'] = True
                            with open("config.json", "w", encoding='utf-8') as config_write_file:
                                json.dump(config_read_data, config_write_file)
                            print(Fore.GREEN + "Режим показа пароля успешно " + Fore.YELLOW + "включен" + Fore.GREEN + "!" + Fore.RESET)
            elif cmd == "help":
                print("\nСписок доступных команд: \n")
                print("settings - Настройки")
                print("system - Система")
                print("pswdgen - Генератор паролей")
                print("\n")
            elif cmd == "system" or cmd == "sys":
                while True:
                    if config_read_data['show_username'] == True:
                        cmd_system = input(user_data['username'] + "/system " + config_read_data['cmd_symbol'] + " ")
                    elif config_read_data['show_username'] == False:
                        cmd_system = input("system " + config_read_data['cmd_symbol'] + " ")
                    if cmd_system == "help":
                        print("\nДоступные команды системы: \n")
                        print("info - Информация о системе")
                        print("exit - Выход")
                        print("\n")
                    elif cmd_system == "info":
                        print("\n\nDF Portable Operation System\n")
                        print(f"Версия : {version}")
                        print(f"ОЗУ : {memory}гб")
                        if global_system == "Windows":
                            print(f"Память : {total_space}гб")
                        print(f"Основная система : {global_system}")
                        print("\n")
                    elif cmd_system == "exit":
                        break
                    else:
                        print(Fore.RED + "Неизвестная команда! Используй help для получения списка доступных команд." + Fore.RESET)
            elif cmd == "password_generator" or cmd == "pswdgen" or cmd == "password_renerator" or cmd == "password_gen":
                print("\nВыберете генератор паролей :")
                print("1. DFPOS_Password_Generator\n")
                if config_read_data['show_username'] == True:
                    cmd_pswdgen = input(user_data['username'] + "/pswdgen " + config_read_data['cmd_symbol'] + " ")
                elif config_read_data['show_username'] == False:
                    cmd_pswdgen = input("pswdgen " + config_read_data['cmd_symbol'] + " ")
                if cmd_pswdgen == "1":
                    print("\nГенерирую случайный пароль.")
                    t.sleep(0.7)
                    print("Генерирую случайный пароль..")
                    t.sleep(0.7)
                    print("Генерирую случайный пароль...", end="\n")
                    t.sleep(0.5)
                    print(f"\nВаш рандомный пароль : {dfpos_tools.pswdgen(1)}\n")
            else:
                print(Fore.RED + "Неизвестная команда! Используй help для получения списка доступных команд." + Fore.RESET)



