
import random
from datetime import datetime
import os
import time

t_R="\033[31m"
t_R1="\033[4;31m"
t_G="\033[32m"
t_Y="\033[33m"
t_Pur="\033[35m"

verdefluo="\033[1;32m"
def_col="\033[0m" #- сбросить все до значений по умолчанию

def_player_name = "noName"

def check_line(line_1, line_2):
    result =""
    for i in zip(line_1, line_2):
        if i[0] != i[1]:
            result += f"{t_R1}{i[1]}{def_col}"
        else:
            result += i[1]
    return result

with open("name_player.txt", "r" , encoding="utf-8")as cont_name_player:
    player_name = cont_name_player.readline()

    if player_name != "":
        def_player_name = player_name

with open("text.txt", "r", encoding="utf-8") as content_file:
    list_content = content_file.readlines()

    while True:

        os.system("clear")
        print(f'\n\t\t{def_col}=== {t_Pur}Speed writer{def_col} ===\n')
        print(f"Player's name is {t_G}{def_player_name}{def_col}\n")
        
        print(f"{t_G}1){def_col} Зарегистрироваться")
        print(f"{t_G}2){def_col} Начать новую игру")
        print(f"{t_G}3){def_col} Турнрная таблица")
        print(f"{t_G}4){def_col} О игре")
        print(f"{t_G}0){t_Y} EXIT{def_col}")

        choise = input(f"\nВаш выбор: ")

        match choise:
            case "1":
                os.system("clear")
                def_player_name = input(f"\nВведите имя игрока: {t_G}")
                if def_player_name == "":
                    def_player_name = "noName"
                print({def_col})
                with open("name_player.txt", "w" , encoding="utf-8") as cont_name_player:
                    cont_name_player.write(def_player_name)

            case "2":
                
                os.system("clear")
                position = random.randint(0,(len(list_content)-1))
                res_position = str(list_content[position]).split(";")
                text_original = res_position[0]

                print(f"\n\n\t\t{verdefluo}{text_original}{def_col}  ")

                start_time1 = datetime.now()
                start_time2 = time.time() 

                text_my_tape = input(f"\n{t_G}{def_player_name}{def_col} введите указанный выше текст: ")

                if text_my_tape == str(text_original):
                    result_time = datetime.now() - start_time1
                    count_sec = time.time() - start_time2 
                    speed_in_sec = round((len(text_original)/count_sec), 2)

                    second_part= res_position[1].replace("\n", "")

                    print(f"\n\t\t\t\t\t{t_Y}( {second_part} ){def_col}\n\n{t_G}Вы выполнили задание!{def_col}\n\n\t- время выполнения задания составило: {str(result_time)[0:10]}\n\t- скорость печати ровна {speed_in_sec} символа в секунду\n\t- сложность задания равна {len(text_original[0])} символа\n")
                    res_position = f'{def_player_name};{speed_in_sec};{len(text_original)};{str(start_time1)[0:16]}\n'

                    with open("save_result.txt", "a", encoding="utf-8") as content_save:
                        content_save.write(res_position)

                    input(f"{t_G}{def_player_name}{def_col} для продолжения нажмите ENTER")
                else:
                    text_my_tape = check_line(text_original, text_my_tape)
                    print(f'\n{t_R}Вы проиграли {def_col}- вы не правильно повторили текст.\n')
                    print(f"\tОригинал текста: ",text_original)
                    print(f"\tВаш набор текста:",text_my_tape)
                    input(f"\n{t_G}{def_player_name}{def_col} для продолжения нажмите ENTER")


            case "3":
                os.system("clear")

                print(f'\n\t\t{t_Pur}Турнирная таблица{def_col}\n')

                with open("save_result.txt", "r" , encoding="utf-8") as content_load:
                    list_load = content_load.readlines()

                    sorted_list = []
                    for i in list_load:
                        line = i.split(";")
                        sorted_list.append(line)
                    
                    sorted_list.sort(key=lambda arr: arr[1], reverse=True)

                    count_line = 0
                    for i in range(len(sorted_list)):
                        count_line +=1
                        if i < 3:
                            color = t_Y
                        else:
                            color = def_col
                        
                        fore_part = str(sorted_list[i][3]).replace("\n", "")
                        print(f'{t_G}{i+1}){def_col} {color}{sorted_list[i][0]}{def_col}, {color}Скорость:{def_col}{sorted_list[i][1]}, {color}Сложность:{def_col}{sorted_list[i][2]}, {color}Дата:{def_col}{fore_part}')
                        if i == 2 or i == 9 or i == 100:
                            print(f"{t_G}-------------------------------------------------------------{def_col}")
                        
                        if count_line == 10:
                            break

                input(f"\n{t_G}{def_player_name}{def_col} для продолжения нажмите ENTER")

            case "4":
                os.system("clear")
                print(f'\nЦель игры на время напечатать предложение по заданию.\nРезультат сохроняется в турнирную таблицу.\nВ турнирной таблице позиции игроков сортируются по скорости печати\n')
                
                
                print(f'\nИгра содержит {len(list_content)} фраз:\n')
                count_line = 0
                for i in list_content:
                    count_line += 1
                    i = i.replace("\n", "").replace(";", " = ")
                    print(f"{t_G}{count_line}){def_col} {i}")
                
                input(f"\n{t_G}{def_player_name}{def_col} для продолжения нажмите ENTER")
            case "0":
                os.system("clear")
                exit()



        
