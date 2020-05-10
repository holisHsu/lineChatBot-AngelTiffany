
import pytest

from ..core import (
    ReportType,
    get_types_form_text
)


def test_get_report_type_ArrivalHomeMorning(arrival_home_morning_text):
    assert ReportType.ArrivalHomeMorning \
        in get_types_form_text(arrival_home_morning_text)


def test_get_report_type_BodyTemp(boy_temp_morning_text):
    assert ReportType.BodyTemp \
        in get_types_form_text(boy_temp_morning_text)


def test_get_report_type_BusStatistic(bus_statistic_text):
    assert ReportType.BusStatistic \
        in get_types_form_text(bus_statistic_text)


def test_get_report_type_GetHomeNight(arrival_home_morning_text):
    assert ReportType.GetHomeNight \
        in get_types_form_text(arrival_home_morning_text)


def test_get_report_type_None(normal_chat_text):
    assert get_types_form_text(normal_chat_text) == []


def test_report_type_translation():

    def _check_report_type_and_translation_content(report_type, translation):
        assert ReportType.translate_to_chinese(report_type) == translation

    type_and_translation_check_arr = [
        (ReportType.ArrivalHomeMorning, '放假回家'),
        (ReportType.BodyTemp, '體溫'),
        (ReportType.BusStatistic, '專車統計'),
        (ReportType.GetHomeNight, '晚上回報(可能和晚上體溫一起)'),
    ]
    for element in type_and_translation_check_arr:
        _check_report_type_and_translation_content(element[0], element[1])
