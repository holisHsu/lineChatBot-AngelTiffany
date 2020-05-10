
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


class ReportType(Enum):
    ArrivalHomeMorning = 'ArrivalHomeMorning'
    BodyTemp = 'BodyTemp'
    BusStatistic = 'BusStatistic'
    GetHomeNight = 'GetHomeNight'


class ReportTypeKeyWords(Enum):
    # Keywords in text will trigger saving related infomation
    ArrivalHomeMorning = ('到家的回報', '到家回報')
    BodyTemp = ('三餐體溫量測回報',)
    BusStatistic = ('專車統計',)
    GetHomeNight = ('三餐體溫量測回報', '到家回報', '到家的回報')



def handle_soldier_line_report(message_event):
    pass


def handle_report_context(text):
    pass


def get_types_form_text(text):

    def _check_and_get_report_type(type_name):
        keywords_to_check = getattr(ReportTypeKeyWords, type_name)
        report_type = getattr(ReportType, type_name)

        for keywords in keywords_to_check.value:
            if keywords in text:
                return report_type

        return None

    report_types = (
        'ArrivalHomeMorning', 'BodyTemp',
        'BusStatistic', 'GetHomeNight'
    )
    possible_report_types = []

    for type_name in report_types:
        report_type = _check_and_get_report_type(type_name)
        if report_type:
            possible_report_types.append(report_type)

    return possible_report_types


def save_report(type, text):
    pass
