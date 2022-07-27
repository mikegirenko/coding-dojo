
# All years divisible by 4 but not by 100 ARE leap years (e.g., 2008, 2012, 2016) DONE

def determine_if_year_is_leap_year(year_to_check):
    is_leap = False
    if year_to_check % 4 == 0:
        if year_to_check % 100 != 0:
            is_leap = True

    return is_leap
