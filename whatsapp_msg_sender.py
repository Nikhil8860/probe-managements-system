import pyautogui as pg
import webbrowser as web
import time
import requests
import schedule


def setup():
    width, height = pg.size()
    pg.click(width / 2, height / 2)
    time.sleep(8)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')


def automatic_msg_send():
    first = True
    combo = get_number_msg_details()
    for lead, message in combo:
        time.sleep(4)
        web.open("https://web.whatsapp.com/send?phone=" + lead + "&text=" + message)
        if first:
            time.sleep(6)
            first = False
        setup()


def get_number_msg_details():
    number = []
    msg = []
    url = "https://flexsmart.pro/cron/messagesend.php"
    details = requests.get(url).json()
    for i in details:
        msg.append(details[i]['Message'])
        number.append(details[i]['Mobile'])
    test_number = ['91_9654362985'] * len(number)
    combo = zip(test_number, msg)
    return combo


if __name__ == '__main__':
    schedule.every().day.at("12:00").do(automatic_msg_send)
    schedule.every().day.at("04:00").do(automatic_msg_send)
    schedule.every().day.at("08:00").do(automatic_msg_send)
    while True:
        schedule.run_pending()
        time.sleep(1)
