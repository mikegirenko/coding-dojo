from leap_years.leap_years import determine_if_year_is_leap_year


def test_year_is_not_leap_year():
    year = 2017
    assert not determine_if_year_is_leap_year(year)


def test_year_is_leap_year():
    year = 2000
    assert determine_if_year_is_leap_year(year)
