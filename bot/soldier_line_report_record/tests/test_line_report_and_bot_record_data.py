
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
