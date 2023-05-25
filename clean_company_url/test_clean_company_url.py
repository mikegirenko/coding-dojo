from clean_company_url.clean_company_url import *

obj = CleanCompanyUrl()


def test_url_has_https():
    this_url = "https://www.example.com"
    assert obj.clean_company_url(this_url) == "example.com"


def test_url_has_http():
    this_url = "http://www.some.com"
    assert obj.clean_company_url(this_url) == "some.com"


def test_url_has_www_only():
    this_url = "www.eggs.com"
    assert obj.clean_company_url(this_url) == "eggs.com"


def test_invalid_url():
    this_url = "spam"
    assert obj.clean_company_url(this_url) == "Invalid URL"
