import datetime


def mdy_to_dmy(date):
    """Converts date from MM/DD/YYYY to DD/MM/YYYY format."""
    return date[3:5] + "/" + date[0:2] + "/" + date[6:10]


def is_date(string, date_format="%d/%m/%Y"):
    try:
        datetime.datetime.strptime(string, date_format)
        return True
    except ValueError:
        return False
