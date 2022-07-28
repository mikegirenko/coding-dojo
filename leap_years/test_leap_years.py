import calendar
import pytest
from leap_years.leap_years import *


@pytest.mark.parametrize("year", [1700, 1800, 1900, 2017, 2018, 2019, 2100])
def test_year_is_not_leap_year(year):
    assert not determine_if_year_is_leap_year(year)


@pytest.mark.parametrize("year", [2000, 2008, 2012, 2016])
def test_year_is_leap_year(year):
    assert determine_if_year_is_leap_year(year)


def test_read_file():
    assert len(read_input()) == 130


def test_which_year_is_leap():
    leap_years = which_year_is_leap()
    for year in leap_years:
        assert calendar.isleap(int(year))
