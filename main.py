import pygetwindow as gw
import pyautogui
import pyperclip
import time
import os

def read_txt_file(base_path):
    try:
        with open(base_path + '/chat_name_list.txt', 'r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Not Found Chat name list txt file")
        return []
    
def read_files_in_folder(base_path):
    full_path = base_path + '/send_message_list'
    try:
        files = os.listdir(full_path)
        folder_result = []
        for file_name in files :
            file_path = full_path + "/" + file_name
            try :
                with open(file_path, 'r', encoding='utf-8') as file:
                    folder_result.append(file.read())
            except FileNotFoundError:
                print("Not Found File")
                return []
        return folder_result
    except FileNotFoundError:
        print("Not Found Folder Message")
        return []

def activate_chatroom(chatroom_name):
    windows = gw.getWindowsWithTitle(chatroom_name)
    if not windows:
        print(f"'{chatroom_name}' 창을 찾을 수 없습니다.")
        return None
    chatroom_window = windows[0]
    chatroom_window.activate()
    time.sleep(1)
    return chatroom_window

def send_text_to_chatroom(chatroom_name, text):
    window = activate_chatroom(chatroom_name)
    if window:
        pyperclip.copy(text)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v') 
        time.sleep(0.5)
        pyautogui.press('enter') 

CURRENT_DIRECTORY_PATH = os.getcwd()
CHAT_NAME_LIST = read_txt_file(CURRENT_DIRECTORY_PATH)
SEND_MESSAGE_LIST = read_files_in_folder(CURRENT_DIRECTORY_PATH)

for send_message in SEND_MESSAGE_LIST :
    for chat_name in CHAT_NAME_LIST : 
        send_text_to_chatroom(chat_name, send_message)
