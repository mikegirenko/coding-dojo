"""
This program will take Company URL, remove protocol and www, and return domain only (example.com)
Possible url: https://www.example.com, http://www.some.com", www.eggs.com
"""
COMPANY_URL = "https://www.example.com"


class CleanCompanyUrl:
    def clean_company_url(self, url_to_clean):
        final_url = ""
        if "https://" in url_to_clean:
            temp_url = url_to_clean[8:]
            final_url = temp_url[4:]
        if "http://" in url_to_clean:
            temp_url = url_to_clean[7:]
            final_url = temp_url[4:]
        if "http" not in url_to_clean:
            if "www" in url_to_clean:
                final_url = url_to_clean[4:]
            else:
                final_url = "Invalid URL"

        return final_url


if __name__ == "__main__":
    obj = CleanCompanyUrl()
    print(f"Clean URL is {obj.clean_company_url(COMPANY_URL)}")
