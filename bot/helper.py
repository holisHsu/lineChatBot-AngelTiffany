
from enum import Enum
import random


def make_reply_content(text_arr):
    return '\n'.join(text_arr)


def random_chat():
    candidates = [
        '嗨，你今天好嗎',
        '我告訴你，我昨天做了一場夢\n我幺八',
        '放假記得準時回報呦',
        '今天放了幾次煙啊?',
        '安，沒錢投飲料了嗎',
        '是不是只有我覺得槍班很辛苦，一天到晚在擦槍?',
        '洞五三洞，三聯訓員起床 !!!',
        '要什麼福利，拿表現來換!'
    ]
    return random.choice(candidates)
