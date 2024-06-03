## 메시지 자동 발송

원하는 채팅창에 원하는 본문을 전송합니다.

### 사전준비
1. 채팅방 목록 이름은 `chat_name_list.txt`에 입력해주세요. 한 줄에 1개의 이름을 입력하고 줄바꿈을 하면 됩니다.
2. 보내고 싶은 메시지 내용들은 `send_message_list` 폴더 안에 넣어주세요. 파일명은 무관합니다. 파일 1개 당 하나입니다.

### 실행안내
1. [Python](https://www.python.org/)을 설치해주세요.
2. "명령 프롬프트 창"에서 다음 명령어를 실행해주세요
    ```
    pip install pygetwindow
    pip install pyautogui
    pip install pyperclip
    ```
3. 파이썬 파일을 실행합니다.
    - Visual Studio Code같은 툴이 있으시다면 바로 run 하셔도 가능합니다.
    - 툴이 없을 경우 "명령 프롬프트 창"에서 다음을 실행해주세요.
        ```
        python main.py
        ```
    - 만약에 main.py을 찾을 수 없다는 안내문구가 나온다면, main.py의 경로와 동일한지 확인해주세요.
4. 실행한 이후에 프로그램의 안내대로 입력해주시면 자동 발송을 하실 수 있습니다.

### 미적용 기능
- GUI (버튼, 디자인) 등
- 랜덤 발송 시간
- 이미지 발송