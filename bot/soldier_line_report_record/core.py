
"""
1. Specify report format, discard unwanted format message
    0. Get home (Morning)
    1. Body Temp (Morning, Afternoon, Night)
    2. Bus Statistic
    3. Get home (Night)
2. Parse
3. Save (just in mem)

TODO Forgetting policy

"""

from enum import Enum

from linebot.models import TextSendMessage

from bot.setting import line_bot_api
from bot.helper import make_reply_content, random_chat


class ReportType(Enum):
    ArrivalHomeMorning = 'ArrivalHomeMorning'
    BodyTemp = 'BodyTemp'
    BusStatistic = 'BusStatistic'
    GetHomeNight = 'GetHomeNight'

    @staticmethod
    def translate_to_chinese(enum_type):
        translation_map = {
            ReportType.ArrivalHomeMorning: '放假回家',
            ReportType.BodyTemp: '體溫',
            ReportType.BusStatistic: '專車統計',
            ReportType.GetHomeNight: '晚上回報(可能和晚上體溫一起)',
        }

        return translation_map.get(enum_type, 'N/A')


class ReportTypeKeyWords(Enum):
    # Keywords in text will trigger saving related infomation
    ArrivalHomeMorning = ('到家的回報', '到家回報')
    BodyTemp = ('三餐體溫量測回報',)
    BusStatistic = ('專車統計',)
    GetHomeNight = ('三餐體溫量測回報', '到家回報', '到家的回報')


def handle_soldier_line_report(message_event):
    # TODO add test for this function
    report_types = get_types_form_text(message_event.message.text)

    # Currently bot should reply the type and remind user it have the function
    if report_types:
        reply_types = ' 或 '.join(map(lambda enum: ReportType.translate_to_chinese(enum),
                                     report_types))
        reply_text = f"我覺得回報類型是 {reply_types}"
    else:
        reply_text = make_reply_content([random_chat(),
                                         "\n",
                                         "是說，你可以把班群的回報貼給我",
                                         "我會告訴你是哪種回報喔"])

    line_bot_api.reply_message(message_event.reply_token,
                               TextSendMessage(text=reply_text))


def get_types_form_text(text):

    def _check_and_get_report_type(type_name):
        keywords_to_check = getattr(ReportTypeKeyWords, type_name)
        report_type = getattr(ReportType, type_name)

        for keywords in keywords_to_check.value:
            if keywords in text:
                return report_type

        return None

    report_type_names = (
        'ArrivalHomeMorning', 'BodyTemp',
        'BusStatistic', 'GetHomeNight'
    )
    possible_report_types = []

    for type_name in report_type_names:
        report_type = _check_and_get_report_type(type_name)
        if report_type:
            possible_report_types.append(report_type)

    return possible_report_types
