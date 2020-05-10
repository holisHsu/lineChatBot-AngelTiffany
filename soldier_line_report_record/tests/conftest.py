
import pytest


@pytest.fixture(scope='module')
def arrival_home_morning_text():
    return """
    5/9到家的回報


    115 已到家 36.4
    116已到家36.3
    117
    118
    119 已到家 36.3
    120 已到家 36.5
    121 已到家 36.2
    122
    123已到家 36.5
    124到家36.5
    125已到家 36.7
    126 已到家 36.5
    127 已到家
    128
    129 已到家 36.7
    130 已到家 36.
    """


@pytest.fixture(scope='module')
def boy_temp_morning_text():
    return """
    5/10三餐體溫量測回報
    例：001早:40
    分三個時段回報
    早：0900 午：1200 晚：1900


    115早36.0
    116早36.1
    117早35.9
    118
    119 早36.6
    120
    121 早36.1
    122
    123早36.5
    124早36.5
    125早36.4
    126 早36.1
    127
    128
    129 早 36.2
    130 早36.5
    """


@pytest.fixture(scope='module')
def boy_temp_night_text():
    return """
    5/9三餐體溫量測回報
    例：001早:40
    分三個時段回報
    早：0900 午：1200 晚：1900


    115晚36.6已在家不出門
    116
    117晚36 已在家 晚上不出門
    118
    119 晚36.2 已在家 2200後不出門
    120
    121
    122
    123
    124
    125
    126
    127
    128 晚 36.6
    129
    130 晚36.6 出門吃飯2200後不出門
    """


@pytest.fixture(scope='module')
def bus_statistic_text():
    return """
    🚌專車統計（5/16-5/17）

    單趟車價
    隆田  80  元 ；台南 120 元
    屏東 250 元 ；潮洲 270 元

    回報［學號：休假車站 / 收假車站
    舉例，001：屏東 / 潮洲
    115 屏東/屏東
    116自行/屏東
    117自行/自行
    118
    119 屏東/自行
    120屏東/自行
    121 屏東/屏東
    122
    123屏東/自行
    124屏東/自行
    125 九如/自行
    126 屏東/自行
    127
    128 潮州 / 潮州
    129 自行/自行
    130 自行/自行
    """
