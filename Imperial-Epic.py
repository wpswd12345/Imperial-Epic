import time
import os
import random
import math
import ctypes
import pyautogui
import tkinter as tk
from tkinter import messagebox
import json
import sys


MONEY = 1000  # 钱
ARMY = 20  # 军队
WOOD = 80  # 木材
STONE = 80  # 石头
FOOD = 60  # 食物
LINGTU = 500  # 领土
L_USE = 70  # 使用的领土
POPULATION = 50  # 人口
BUILDING = 2  # 大厦
RANDOM1_5 = 0  # 1到10的随机数，用来做搜刮的次数
HOME = 10  # 民宅
FIELD = 15  # 田地
ROUND_SEARCH = 0  # 搜索次数
SAVE = 0  # 保存次数
AUTO_SAVE = 0
AUTO_READ = 0

screen_width, screen_height = pyautogui.size()
right_bottom_corner = (screen_width - 1, screen_height - 1)
current_position = pyautogui.position()
if current_position != right_bottom_corner:
    pyautogui.moveTo(right_bottom_corner)

def press_f11():
    auto_press_f11 = 0x7A
    ctypes.windll.user32.keybd_event(auto_press_f11, 0, 0, 0)
    ctypes.windll.user32.keybd_event(auto_press_f11, 0, 2, 0)

def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')

def bring_window_to_front():
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(0, 0)
    pyautogui.moveTo(screen_width - 1, screen_height - 1)
    pyautogui.moveTo(screen_width, screen_height)


def read_tui_auto():
    global AUTO_SAVE, AUTO_READ
    user_data_path = os.path.join(os.path.expanduser("~"), "DGSS")
    file_path = os.path.join(user_data_path, "data.json")
    try:
        with open(file_path, "r") as file:
            loaded_data = json.load(file)
            AUTO_SAVE = loaded_data["p12"]
            AUTO_READ = loaded_data["p13"]
    except:
        pass


bring_window_to_front()
press_f11()


def read_tui():
    global MONEY, ARMY, WOOD, STONE, FOOD, LINGTU, L_USE, POPULATION, BUILDING, HOME, FIELD
    user_data_path = os.path.join(os.path.expanduser("~"), "DGSS")
    file_path = os.path.join(user_data_path, "data.json")
    try:
        with open(file_path, "r") as file:
            loaded_data = json.load(file)
            MONEY = loaded_data['p1']
            ARMY = loaded_data['p2']
            WOOD = loaded_data['p3']
            STONE = loaded_data['p4']
            FOOD = loaded_data['p5']
            LINGTU = loaded_data['p6']
            L_USE = loaded_data['p7']
            POPULATION = loaded_data['p8']
            BUILDING = loaded_data['p9']
            HOME = loaded_data['p10']
            FIELD = loaded_data["p11"]
        print('')
        print('读取游戏数据完成。')
        print('')
        time.sleep(1)
    except FileNotFoundError:        
        print('')
        print("找不到游戏记录文件。")
        print('你可以在命令行界面中输入"save"或在图形界面中点击"读取游戏记录"以重试。')
        while True:
            a = input('按Enter以退出。')
            if a == '':
                break
            else:
                continue
        print('')
        time.sleep(1)
    except json.JSONDecodeError:       
        print('')
        print("游戏记录文件损坏或格式错误。")
        print('你可以在命令行界面中输入"save"或在图形界面中点击"读取游戏记录"以重试。')
        while True:
            a = input('按Enter以退出。')
            if a == '':
                break
            else:
                continue
        print('')
        time.sleep(1)
    except Exception as e:
        print('')
        print(f"读取游戏记录失败：{str(e)}。")
        print('你可以在命令行界面中输入"save"或在图形界面中点击"读取游戏记录"以重试。')
        while True:
            a = input('按Enter以退出。')
            if a == '':
                break
            else:
                continue
        print('')
        time.sleep(1)


def save_tui():
    global MONEY, ARMY, WOOD, STONE, FOOD, LINGTU, L_USE, POPULATION, BUILDING, HOME, FIELD, SAVE
    data = {
        "p1": MONEY,
        "p2": ARMY,
        "p3": WOOD,
        "p4": STONE,
        "p5": FOOD,
        "p6": LINGTU,
        "p7": L_USE,
        "p8": POPULATION,
        "p9": BUILDING,
        "p10": HOME,
        "p11": FIELD,
        "p12": AUTO_SAVE,
        "p13": AUTO_READ
    }
    user_data_path = os.path.join(os.path.expanduser("~"), "DGSS")
    os.makedirs(user_data_path, exist_ok=True)
    file_path = os.path.join(user_data_path, "data.json")
    with open(file_path, "w") as file:
        json.dump(data, file)
        SAVE += 1
        time.sleep(0.5)

def auto_save_tui():
    global AUTO_SAVE, AUTO_READ
    data = {
        "p1": 1000,
        "p2": 20,
        "p3": 80,
        "p4": 80,
        "p5": 60,
        "p6": 500,
        "p7": 70,
        "p8": 50,
        "p9": 2,
        "p10": 10,
        "p11": 15,
        "p12": AUTO_SAVE,
        "p13": AUTO_READ
    }
    user_data_path = os.path.join(os.path.expanduser("~"), "DGSS")
    os.makedirs(user_data_path, exist_ok=True)
    file_path = os.path.join(user_data_path, "data.json")
    with open(file_path, "w") as file:
        json.dump(data, file)
    
for i in range(1, 640, 28):
    print("checking memory: " + str(i) + " kb ok")
    time.sleep(0.025)
    clear_screen()
print('checking memory: 640 kb ok')
time.sleep(1.5)
clear_screen()
time.sleep(2.3)
print("starting POINT-DGSS")
time.sleep(5)
print("C:/")
time.sleep(0.1)
print("C:/")
time.sleep(0.1)
print("C:/")
time.sleep(0.1)
print("C:/ cd dgss")
time.sleep(0.1)
print("C:/dgset.com")
time.sleep(0.1)
print("C:/")
time.sleep(0.5)
clear_screen()
time.sleep(1)
read_tui_auto()
if AUTO_READ == 1:
    print('Auto loading...')
    read_tui()
    clear_screen()
time.sleep(2)
print('Welcome to POINT-DGSS V4.2.2.Type \'HELP\' for help.')
time.sleep(0.6)
while True:
    commands = ['dir', 'cls', 'help', 'shutdown', 'building', 'search', 'bdhm', 'opfld', 'field', 'market', 'read', 'save', 'ver', 'gui', 'dgssver', 'sas', 'sar', 'cas', 'car', '']  # 命令
    player_input = input("C:\\>").lower()
    if player_input == "help":  # 玩家帮助
        if AUTO_SAVE == 0 and AUTO_READ == 0:
            time.sleep(1)
            time.sleep(0.03)
            print('')
            print('HELP          显示帮助。')
            time.sleep(0.03)
            print('CLS           清除屏幕。')
            time.sleep(0.03)
            print('DIR           显示玩家当前状态')
            time.sleep(0.03)
            print('VER           显示帝国史诗的版本号。')
            time.sleep(0.03)
            print('BUILDING      建造大厦。')
            time.sleep(0.03)
            print('SEARCH        搜刮物资。')
            time.sleep(0.03)
            print('BDHM          建造民宅。')
            time.sleep(0.03)
            print('OPFLD         开垦土地。')
            time.sleep(0.03)
            print('FIELD         种田。')
            time.sleep(0.03)
            print('MARKET        交易货物。')
            time.sleep(0.03)
            print('SAVE          存档。')
            time.sleep(0.03)
            print('READ          读档。')
            time.sleep(0.03)
            print('SAS           启动自动存档。')
            time.sleep(0.03)
            print('SAR           启动自动读档。')
            time.sleep(0.03)
            print('GUI           启动图形界面。')
            time.sleep(0.03)
            print('SHUTDOWN      退出游戏。')
            time.sleep(0.03)
            print('')
            time.sleep(0.5)
        if AUTO_SAVE == 1 and AUTO_READ == 0:
            time.sleep(1)
            time.sleep(0.03)
            print('')
            print('HELP          显示帮助。')
            time.sleep(0.03)
            print('CLS           清除屏幕。')
            time.sleep(0.03)
            print('DIR           显示玩家当前状态')
            time.sleep(0.03)
            print('VER           显示帝国史诗的版本号。')
            time.sleep(0.03)
            print('BUILDING      建造大厦。')
            time.sleep(0.03)
            print('SEARCH        搜刮物资。')
            time.sleep(0.03)
            print('BDHM          建造民宅。')
            time.sleep(0.03)
            print('OPFLD         开垦土地。')
            time.sleep(0.03)
            print('FIELD         种田。')
            time.sleep(0.03)
            print('MARKET        交易货物。')
            time.sleep(0.03)
            print('SAVE          存档。')
            time.sleep(0.03)
            print('READ          读档。')
            time.sleep(0.03)
            print('CAS           关闭自动存档。')
            time.sleep(0.03)
            print('SAR           启动自动读档。')
            time.sleep(0.03)
            print('GUI           启动图形界面。')
            time.sleep(0.03)
            print('SHUTDOWN      退出游戏。')
            time.sleep(0.03)
            print('')
            time.sleep(0.5)
        if AUTO_SAVE == 1 and AUTO_READ == 1:
            time.sleep(1)
            time.sleep(0.03)
            print('')
            print('HELP          显示帮助。')
            time.sleep(0.03)
            print('CLS           清除屏幕。')
            time.sleep(0.03)
            print('DIR           显示玩家当前状态')
            time.sleep(0.03)
            print('VER           显示帝国史诗的版本号。')
            time.sleep(0.03)
            print('BUILDING      建造大厦。')
            time.sleep(0.03)
            print('SEARCH        搜刮物资。')
            time.sleep(0.03)
            print('BDHM          建造民宅。')
            time.sleep(0.03)
            print('OPFLD         开垦土地。')
            time.sleep(0.03)
            print('FIELD         种田。')
            time.sleep(0.03)
            print('MARKET        交易货物。')
            time.sleep(0.03)
            print('SAVE          存档。')
            time.sleep(0.03)
            print('READ          读档。')
            time.sleep(0.03)
            print('CAS           关闭自动存档。')
            time.sleep(0.03)
            print('CAR           关闭自动读档。')
            time.sleep(0.03)
            print('GUI           启动图形界面。')
            time.sleep(0.03)
            print('SHUTDOWN      退出游戏。')
            time.sleep(0.03)
            print('')
            time.sleep(0.5)
        if AUTO_SAVE == 0 and AUTO_READ == 1:
            time.sleep(1)
            time.sleep(0.03)
            print('')
            print('HELP          显示帮助。')
            time.sleep(0.03)
            print('CLS           清除屏幕。')
            time.sleep(0.03)
            print('DIR           显示玩家当前状态')
            time.sleep(0.03)
            print('VER           显示帝国史诗的版本号。')
            time.sleep(0.03)
            print('BUILDING      建造大厦。')
            time.sleep(0.03)
            print('SEARCH        搜刮物资。')
            time.sleep(0.03)
            print('BDHM          建造民宅。')
            time.sleep(0.03)
            print('OPFLD         开垦土地。')
            time.sleep(0.03)
            print('FIELD         种田。')
            time.sleep(0.03)
            print('MARKET        交易货物。')
            time.sleep(0.03)
            print('SAVE          存档。')
            time.sleep(0.03)
            print('READ          读档。')
            time.sleep(0.03)
            print('SAS           启动自动存档。')
            time.sleep(0.03)
            print('CAR           关闭自动读档。')
            time.sleep(0.03)
            print('GUI           启动图形界面。')
            time.sleep(0.03)
            print('SHUTDOWN      退出游戏。')
            time.sleep(0.03)
            print('')
            time.sleep(0.5)
    if player_input not in commands:  # 错误命令
        time.sleep(1)
        print('')
        print('bad command or files name')
        print('')
        time.sleep(0.5)
    if player_input == 'ver':
        time.sleep(1)
        print('')
        print('POINT-DGSS Version 4.2.2')
        print('')
        time.sleep(0.5)
    if player_input in 'dir':  # 玩家输入dir
        time.sleep(1)
        print('')
        time.sleep(0.03)
        print('金钱:          ' + str(MONEY))
        time.sleep(0.03)
        print('军队:          ' + str(ARMY))
        time.sleep(0.03)
        print('木材:          ' + str(WOOD))
        time.sleep(0.03)
        print('石头:          ' + str(STONE))
        time.sleep(0.03)
        print('食物:          ' + str(FOOD))
        time.sleep(0.03)
        print('领土:          ' + str(LINGTU))
        time.sleep(0.03)
        print('剩余领土:      ' + str(LINGTU-L_USE))
        time.sleep(0.03)
        print('人口:          ' + str(POPULATION))
        time.sleep(0.03)
        print('大厦:          ' + str(BUILDING))
        time.sleep(0.03)
        print('民宅:          ' + str(HOME))
        time.sleep(0.03)
        print('田地:          ' + str(FIELD))
        time.sleep(0.03)
        print('')
        time.sleep(0.5)
    if player_input == 'sas':
        time.sleep(0.3)
        AUTO_SAVE = 1
    if player_input == 'cas':
        time.sleep(0.3)
        AUTO_SAVE = 0
    if player_input == 'sar':
        time.sleep(0.3)
        AUTO_READ = 1
    if player_input == 'car':
        time.sleep(0.3)
        AUTO_READ = 0
    if player_input == 'cls':  # 玩家输入cls
        time.sleep(0.5)
        clear_screen()
    if player_input == 'dgssver':
        def button_exit():
            dgssver.destroy()
            bring_window_to_front()
        dgssver = tk.Tk()
        dgssver.title('关于帝国史诗')
        lable1 = tk.Label(dgssver, text='POINT-DGSS Version 4.2.2')
        lable1.pack()
        lable2 = tk.Label(dgssver, text='POINT(Non-Profit Information Technology Organization) 2022-2024 All Rights Reserved')
        lable2.pack()
        button1 = tk.Button(dgssver, text='确定', command=button_exit)
        button1.pack()
        dgssver.mainloop()
    if player_input == 'shutdown':
        time.sleep(1)
        if SAVE >= 1 or AUTO_SAVE == 1:
            print('游戏正在将数据保存到磁盘.')
            save_tui()
            time.sleep(1.5)
            clear_screen()
            print('游戏正在将数据保存到磁盘.....  done')
            time.sleep(0.5)
            sys.exit()
        if SAVE == 0 and AUTO_SAVE == 0:
            while True:
                key = input('你尚未保存游戏进度，确实要退出吗(Y/N)?').lower()
                if key == 'y':
                    time.sleep(1)
                    print('游戏正在将数据保存到磁盘.')
                    time.sleep(1.5)
                    auto_save_tui()
                    clear_screen()
                    time.sleep(0.2)
                    print('游戏正在将数据保存到磁盘.....  done')
                    time.sleep(0.5)
                    sys.exit()
                elif key == 'n':
                    break
                else:
                    continue


    def build():  # 建造大厦
        global MONEY, WOOD, STONE, LINGTU, L_USE, POPULATION, BUILDING
        if WOOD >= 20 and STONE >= 20 and LINGTU >= 10 and LINGTU - L_USE > 10:
            time.sleep(1)
            print('')
            time.sleep(0.03)
            print('建造中...')
            time.sleep(5)
            print('成功建造了一座大厦，花费100金钱、20木头、20石头，占用20领土，增加了5人口。')
            print('')
            WOOD -= 20
            STONE -= 20
            MONEY -= 100
            POPULATION += 5
            L_USE += 20
            BUILDING += 1
            time.sleep(0.5)
        else:
            time.sleep(1)
            print('你没有足够的材料!')
            time.sleep(0.5)

    def random_int():  # 随机数
        global RANDOM1_5
        RANDOM1_5 = random.randint(1, 5)

    def search():  # 搜寻物资
        global MONEY, WOOD, STONE, FOOD, LINGTU, ROUND_SEARCH, RANDOM1_5, FIELD
        if ROUND_SEARCH <= 2:
            print('')
            print('正在搜寻物资...')
            time.sleep(3)
            random_int()
            w_p = RANDOM1_5
            WOOD += w_p
            random_int()
            m_p = RANDOM1_5
            MONEY += m_p
            random_int()
            s_p = RANDOM1_5
            STONE += s_p
            random_int()
            l_p = RANDOM1_5
            LINGTU += l_p / 2
            print('物资搜寻成功。搜寻到了' + str(w_p) + '的木头，' + str(m_p) + '的金钱，' + str(s_p) + '的石头和' + str(l_p) + '的领土。')
            print('')
            time.sleep(0.5)
            ROUND_SEARCH += 1
        if ROUND_SEARCH >= 3:
            time.sleep(1)
            print('')
            time.sleep(0.03)
            print('你的搜(白)寻(嫖)次数今日已达上限')
            print('')
            time.sleep(0.5)

    def build_home():  # 建造民宅
        global MONEY, WOOD, STONE, FOOD, LINGTU, L_USE, POPULATION, BUILDING, HOME
        if MONEY >= 10 and WOOD >= 10 and STONE >= 10 and LINGTU >= 10 and LINGTU - L_USE > 10:
            time.sleep(1)
            print('')
            time.sleep(0.03)
            print('建造中...')
            time.sleep(5)
            print('成功建造了一座民宅，花费10金钱、10木头、10石头，占用5领土，增加3人口。')
            print('')
            time.sleep(0.03)
            MONEY -= 10
            WOOD -= 10
            STONE -= 10
            POPULATION += 3
            L_USE += 5
            HOME += 1
            time.sleep(0.005)
        else:
            time.sleep(1)
            print('')
            time.sleep(0.03)
            print('你没有足够的材料')
            print('')
            time.sleep(0.5)

    def open_field():  # 开垦土地
        global MONEY, WOOD, STONE, FOOD, LINGTU, L_USE, POPULATION, FIELD
        if WOOD >= 10 and STONE >= 10 and LINGTU >= 10 and LINGTU - L_USE > 10:
            time.sleep(1)
            print('')
            time.sleep(0.03)
            print('开垦中...')
            time.sleep(3)
            print('你开垦了一片土地，花费2食物、10木头、10石头，占用5领土。')
            print('')
            time.sleep(0.03)
            WOOD -= 10
            STONE -= 10
            L_USE += 5
            FOOD -= 2
            time.sleep(0.5)
        else:
            time.sleep(1)
            print('')
            time.sleep(0.03)
            print('你没有足够的材料')
            print('')
            time.sleep(0.5)

    def field():
        global FOOD, POPULATION, FIELD, L_USE
        time.sleep(1)
        food_plus = random.randint(math.ceil(POPULATION / 2), POPULATION * 2)
        FOOD += food_plus
        FIELD -= 5
        L_USE -= 5
        print('')
        time.sleep(0.03)
        print('你种了田，获得了' + str(food_plus) + '的食物,消耗了5田地。')
        print('')
        time.sleep(0.5)

    def wood():
        global WOOD, POPULATION
        time.sleep(1)
        print('')
        wood_need = int(input('请输入你需要的木材：'))
        if POPULATION * 1.5 >= wood_need:
            WOOD += wood_need
            pop_small = random.randint(math.ceil(wood_need / 2), math.ceil(wood_need * 1.5))
            POPULATION -= pop_small
            print('你获得了', wood_need, '的木材，损失了' + str(pop_small) + '的人。')
            time.sleep(0.5)
        if POPULATION * 1.5 < wood_need:
            print('你没有足够的人口!')
            time.sleep(0.5)

    def market():
        global MONEY, WOOD, STONE, FOOD, LINGTU
        time.sleep(1)
        print('欢迎来到市场')
        time.sleep(0.03)
        print('stone(石头)：20元1块')
        time.sleep(0.03)
        print('wood(木材)：20元1条')
        time.sleep(0.03)
        print('territory(领土)：30元1块')
        time.sleep(0.03)
        while True:
            print('')
            time.sleep(0.03)
            thing = input('用英文输入你想要买的东西(输入\'exit\'以退出): ')
            thing_list = ['wood', 'stone', 'territory', 'exit']
            if thing not in thing_list:
                continue
            if thing == 'wood':
                time.sleep(0.5)
                print('好的。请问想要多少木材?')
                wood_need = int(input())
                wood_money_need = wood_need * 20
                if wood_money_need >= MONEY:
                    time.sleep(0.5)
                    print('你没有足够的钱。')
                    print('')
                    time.sleep(0.5)
                if wood_money_need < MONEY:
                    time.sleep(0.5)
                    print('正在运输木材...')
                    print('')
                    time.sleep(3)
                    print('木材运输完成。')
                    WOOD += wood_need
                    MONEY -= wood_money_need
                    time.sleep(0.5)
                    continue
            if thing == 'stone':
                time.sleep(0.5)
                print('好的。请问想要多少石头?')
                stone_need = int(input())
                stone_money_need = stone_need * 20
                if stone_money_need >= MONEY:
                    time.sleep(0.5)
                    print('你没有足够的钱。')
                    print('')
                    time.sleep(0.5)
                if stone_money_need < MONEY:
                    time.sleep(0.5)
                    print('正在运输石头...')
                    print('')
                    print('石头运输完成。')
                    time.sleep(3)
                    STONE += stone_need
                    MONEY -= stone_money_need
                    continue
            if thing == 'territory':
                time.sleep(0.5)
                print('好的。请问想要多少领土?')
                lingtu_need = int(input())
                lingtu_money_need = lingtu_need * 30
                if lingtu_money_need >= MONEY:
                    time.sleep(0.5)
                    print('你没有足够的钱。')
                    print('')
                    time.sleep(0.5)
                if lingtu_money_need < MONEY:
                    time.sleep(0.5)
                    print('正在扩展领土...')
                    print('')
                    time.sleep(3)
                    print('领土扩展完成。')
                    LINGTU += lingtu_need
                    MONEY -= lingtu_money_need
                    continue
            if thing == 'exit':
                time.sleep(0.5)
                print('')
                break

    def gui_mode():

        def build_gui():
            global MONEY, WOOD, STONE, LINGTU, L_USE, POPULATION, BUILDING
            if WOOD >= 20 and STONE >= 20 and LINGTU >= 10 and LINGTU - L_USE > 10:
                messagebox.showinfo("建造大厦", "成功建造了一座大厦，花费100金钱、20木头、20石头，占用20领土，增加了5人口。")
                WOOD -= 20
                STONE -= 20
                MONEY -= 100
                POPULATION += 5
                L_USE += 20
                BUILDING += 1
            else:
                messagebox.showerror("建造大厦", "你没有足够的材料！")

        def search_gui():
            global MONEY, WOOD, STONE, FOOD, LINGTU, ROUND_SEARCH, RANDOM1_5, FIELD
            if ROUND_SEARCH <= 2:
                random_int_gui()
                w_p = RANDOM1_5
                WOOD += w_p
                random_int_gui()
                m_p = RANDOM1_5
                MONEY += m_p
                random_int_gui()
                s_p = RANDOM1_5
                STONE += s_p
                random_int_gui()
                l_p = RANDOM1_5
                LINGTU += l_p / 2
                messagebox.showinfo("搜刮物资",
                                    f"物资搜寻成功。搜寻到了{w_p}的木头，{m_p}的金钱，{s_p}的石头和{l_p}的领土。")
                ROUND_SEARCH += 1
            else:
                messagebox.showerror("搜刮物资", "你的搜寻次数今日已达上限")

        def build_home_gui():
            global MONEY, WOOD, STONE, FOOD, LINGTU, L_USE, POPULATION, BUILDING, HOME
            if MONEY >= 10 and WOOD >= 10 and STONE >= 10 and LINGTU >= 10 and LINGTU - L_USE > 10:
                messagebox.showinfo("建造民宅", "成功建造了一座民宅，花费10金钱、10木头、10石头，占用5领土，增加3人口。")
                MONEY -= 10
                WOOD -= 10
                STONE -= 10
                POPULATION += 3
                L_USE += 5
                HOME += 1
            else:
                messagebox.showerror("建造民宅", "你没有足够的材料！")

        def open_field_gui():
            global MONEY, WOOD, STONE, FOOD, LINGTU, L_USE, POPULATION, FIELD
            if WOOD >= 10 and STONE >= 10 and LINGTU >= 10 and LINGTU - L_USE > 10:
                messagebox.showinfo("开垦土地",
                                    "成功开垦了一片土地，花费2食物、10木头、10石头，占用5领土。每一个循环都会增加几食物。")
                WOOD -= 10
                STONE -= 10
                L_USE += 5
                FOOD -= 2
            else:
                messagebox.showerror("开垦土地", "你没有足够的材料！")

        def field_gui():
            global FOOD, POPULATION, FIELD, L_USE
            food_plus = random.randint(math.ceil(POPULATION / 2), POPULATION * 2)
            FOOD += food_plus
            FIELD -= 5
            L_USE -= 5
            messagebox.showinfo("种田", f"你种了田，获得了{food_plus}的食物，消耗了5田地。")
    
        def market_gui():
            global MONEY, WOOD, STONE, FOOD, LINGTU
            market_window = tk.Toplevel(root)
            market_window.title("市场")
            market_window.geometry("300x300")
            wood_label = tk.Label(market_window, text="木材：15元1条")
            wood_label.pack()
            stone_label = tk.Label(market_window, text="石头：20元1块")
            stone_label.pack()
            lingtu_label = tk.Label(market_window, text="领土：30元1块")
            lingtu_label.pack()

            def buy_wood():
                nonlocal market_window
                global MONEY, WOOD
                wood_need = int(wood_entry.get())
                wood_money_need = wood_need * 20
                if wood_money_need >= MONEY:
                    messagebox.showerror("购买木材", "你没有足够的钱！")
                else:
                    messagebox.showinfo("购买木材", f"已购买{wood_need}的木材。")
                    WOOD += wood_need
                    MONEY -= wood_money_need
                market_window.destroy()

            def buy_stone():
                nonlocal market_window
                global MONEY, STONE
                stone_need = int(stone_entry.get())
                stone_money_need = stone_need * 20
                if stone_money_need >= MONEY:
                    messagebox.showerror("购买石头", "你没有足够的钱！")
                else:
                    messagebox.showinfo("购买石头", f"已购买{stone_need}的石头。")
                    STONE += stone_need
                    MONEY -= stone_money_need
                market_window.destroy()

            def buy_lingtu():
                nonlocal market_window
                global MONEY, LINGTU
                lingtu_need = int(lingtu_entry.get())
                lingtu_money_need = lingtu_need * 30
                if lingtu_money_need >= MONEY:
                    messagebox.showerror("购买领土", "你没有足够的钱！")
                else:
                    messagebox.showinfo("购买领土", f"已购买{lingtu_need}的领土。")
                    LINGTU += lingtu_need
                    MONEY -= lingtu_money_need
                market_window.destroy()

            wood_entry = tk.Entry(market_window)
            wood_entry.pack()
            wood_button = tk.Button(market_window, text="购买木材", command=buy_wood)
            wood_button.pack()
            stone_entry = tk.Entry(market_window)
            stone_entry.pack()
            stone_button = tk.Button(market_window, text="购买石头", command=buy_stone)
            stone_button.pack()
            lingtu_entry = tk.Entry(market_window)
            lingtu_entry.pack()
            lingtu_button = tk.Button(market_window, text="购买领土", command=buy_lingtu)
            lingtu_button.pack()

        def read_gui():
            global MONEY, ARMY, WOOD, STONE, FOOD, LINGTU, L_USE, POPULATION, BUILDING, HOME, FIELD, SAVE, AUTO_SAVE, AUTO_READ
            user_data_path = os.path.join(os.path.expanduser("~"), "DGSS")
            file_path = os.path.join(user_data_path, "data.json")
            try:
                with open(file_path, "r") as file:
                    loaded_data = json.load(file)
                    MONEY = loaded_data['p1']
                    ARMY = loaded_data['p2']
                    WOOD = loaded_data['p3']
                    STONE = loaded_data['p4']
                    FOOD = loaded_data['p5']
                    LINGTU = loaded_data['p6']
                    L_USE = loaded_data['p7']
                    POPULATION = loaded_data['p8']
                    BUILDING = loaded_data['p9']
                    HOME = loaded_data['p10']
                    FIELD = loaded_data["p11"]
                    AUTO_SAVE = loaded_data["p12"]
                    AUTO_READ = loaded_data["p13"]
                messagebox.showinfo("读取游戏记录", "游戏记录读取成功")
            except FileNotFoundError:
                messagebox.showwarning("读取游戏记录", "找不到游戏记录文件")
            except json.JSONDecodeError:
                messagebox.showerror("读取游戏记录", "游戏记录文件损坏或格式错误")
            except Exception as e:
                messagebox.showerror("读取游戏记录", f"读取游戏记录失败：{str(e)}")

        def save_gui():
            global MONEY, ARMY, WOOD, STONE, FOOD, LINGTU, L_USE, POPULATION, BUILDING, HOME, FIELD, SAVE
            data = {
                "p1": MONEY,
                "p2": ARMY,
                "p3": WOOD,
                "p4": STONE,
                "p5": FOOD,
                "p6": LINGTU,
                "p7": L_USE,
                "p8": POPULATION,
                "p9": BUILDING,
                "p10": HOME,
                "p11": FIELD,
                "p12":AUTO_SAVE,
                "p13":AUTO_READ
            }
            user_data_path = os.path.join(os.path.expanduser("~"), "DGSS")
            os.makedirs(user_data_path, exist_ok=True)
            file_path = os.path.join(user_data_path, "data.json")
            with open(file_path, "w") as file:
                json.dump(data, file)
            messagebox.showinfo("保存游戏记录", "游戏记录保存成功")
            SAVE += 1
        def button_exit_gui_func():
            root.destroy()
            bring_window_to_front()

        def random_int_gui():
            global RANDOM1_5
            RANDOM1_5 = random.randint(1, 5)

        root = tk.Tk()
        root.title("POINT-DGSS")
        root.geometry("400x300")

        def on_button_click(command):
            if command == "build":
                build_gui()
            elif command == "search":
                search_gui()
            elif command == "build_home":
                build_home_gui()
            elif command == "open_field":
                open_field_gui()
            elif command == "field":
                field_gui()
            elif command == "market":
                market_gui()
            elif command == "save":
                save_gui()
            elif command == "read":
                read_gui()
            elif command == "exit_gui":
                button_exit_gui_func()

        build_button = tk.Button(root, text="建造大厦", command=lambda: on_button_click("build"))
        build_button.pack()
        search_button = tk.Button(root, text="搜刮物资", command=lambda: on_button_click("search"))
        search_button.pack()
        build_home_button = tk.Button(root, text="建造民宅", command=lambda: on_button_click("build_home"))
        build_home_button.pack()
        open_field_button = tk.Button(root, text="开垦土地", command=lambda: on_button_click("open_field"))
        open_field_button.pack()
        field_button = tk.Button(root, text="种田", command=lambda: on_button_click("field"))
        field_button.pack()
        market_button = tk.Button(root, text="市场", command=lambda: on_button_click("market"))
        market_button.pack()
        save_button = tk.Button(root, text="保存游戏记录", command=lambda: on_button_click("save"))
        save_button.pack()
        read_button = tk.Button(root, text="读取游戏记录", command=lambda: on_button_click("read"))
        read_button.pack()
        button_exit_gui = tk.Button(root, text='退出图形界面', command=lambda: on_button_click("exit_gui"))
        button_exit_gui.pack()
        root.mainloop()

    def decrypt(a):  # 加密模块
        if type(a) is str:
            hex_str = a.encode('utf-8').hex()  # 十六进制的字符
            return hex_str
        else:
            return hex(a)

    def encrypt(a):  # 解密模块
        code_new_output = int(a, 16)
        return code_new_output

    def save():  # 保存游戏记录，这两个读写函数留作纪念
        global MONEY, ARMY, WOOD, STONE, FOOD, LINGTU, L_USE, POPULATION, BUILDING, HOME, FIELD
        time.sleep(1)
        print('')
        print('请把以下数字按顺序记录，避免记录错误，顺序错误。')
        time.sleep(0.1)
        print(decrypt(MONEY))
        time.sleep(0.05)
        print(decrypt(ARMY))
        time.sleep(0.05)
        print(decrypt(WOOD))
        time.sleep(0.05)
        print(decrypt(STONE))
        time.sleep(0.05)
        print(decrypt(FOOD))
        time.sleep(0.05)
        print(decrypt(LINGTU))
        time.sleep(0.05)
        print(decrypt(L_USE))
        time.sleep(0.05)
        print(decrypt(POPULATION))
        time.sleep(0.05)
        print(decrypt(BUILDING))
        time.sleep(0.05)
        print(decrypt(HOME))
        time.sleep(0.05)
        print(decrypt(FIELD))
        time.sleep(0.05)
        print('')
        time.sleep(0.5)

    def read():  # 读取游戏记录
        global MONEY, ARMY, WOOD, STONE, FOOD, LINGTU, L_USE, POPULATION, BUILDING, HOME, FIELD
        time.sleep(1)
        print('请输入上次游戏记录。')
        time.sleep(0.5)
        while True:
            try:
                MONEY = encrypt(input('请输入第一组数字：'))
                time.sleep(0.6)
                ARMY = encrypt(input('很好。现在，请输入第二组数字：'))
                time.sleep(0.6)
                WOOD = encrypt(input('接下来，请输入第三组数字：'))
                time.sleep(0.6)
                STONE = encrypt(input('好的。现在输入第四组数字：'))
                time.sleep(0.6)
                FOOD = encrypt(input('好的。接下来，输入第五组数字：'))
                time.sleep(0.6)
                LINGTU = encrypt(input('很好。现在输入第六组数字：'))
                time.sleep(0.6)
                L_USE = encrypt(input('好的。接下来输入第七组数字：'))
                time.sleep(0.6)
                POPULATION = encrypt(input('好的。现在输入第八组数字：'))
                time.sleep(0.6)
                BUILDING = encrypt(input('很好。接下来，请输入第九组数字：'))
                time.sleep(0.6)
                HOME = encrypt(input('非常好。接下来，请输入第十组数字：'))
                time.sleep(0.6)
                FIELD = encrypt(input('现在，输入最后一组数字：'))
            except:
                print('输入错误')
                continue
            time.sleep(2)
            print('现在你成功的激活了这场游戏！')
            time.sleep(0.5)
            break


    if player_input == 'building':
        build()
    if player_input == 'search':
        search()
    if player_input == 'bdhm':
        build_home()
    if player_input == 'opfld':
        open_field()
    if player_input == 'field':
        field()
    if player_input == 'market':
        market()
    if player_input == 'save':
        save_tui()
    if player_input == 'read':
        read_tui()
    if player_input == 'gui':
        time.sleep(2)
        gui_mode()
