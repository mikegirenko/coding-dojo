import pytest
from leap_years.leap_years import determine_if_year_is_leap_year


@pytest.mark.parametrize("year", [2017, 2018, 2019])
def test_year_is_not_leap_year(year):
    assert not determine_if_year_is_leap_year(year)


@pytest.mark.parametrize("year", [2008, 2012, 2016])
def test_year_is_leap_year(year):
    assert determine_if_year_is_leap_year(year)
