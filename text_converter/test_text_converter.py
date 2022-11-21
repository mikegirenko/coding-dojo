import unittest

from text_converter.text_converter import UnicodeFileToHtmlTextConverter


class UnicodeFileToHtmlTextConverterTest(unittest.TestCase):

    def test_filename_with_path_returned(self):
        converter = UnicodeFileToHtmlTextConverter("foo")
        self.assertEqual("foo", converter.full_filename_with_path)

    def test_convert_to_html(self):
        converter = UnicodeFileToHtmlTextConverter("text_to_convert.txt")
        assert converter.convert_to_html() is not None

    def test_convert_to_html_when_blank(self):
        converter = UnicodeFileToHtmlTextConverter("blank_to_convert.txt")
        assert converter.convert_to_html() is ""


if __name__ == "__main__":
    unittest.main()
