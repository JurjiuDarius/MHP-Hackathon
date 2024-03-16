import datetime


def mdy_to_dmy(date):
    """Converts date from MM/DD/YYYY to DD/MM/YYYY format."""
    return date[3:5] + "/" + date[0:2] + "/" + date[6:10]


def is_date(string):
    if len(string) != 10:
        return False
    if string[2] != "/" or string[5] != "/":
        return False
    return True
