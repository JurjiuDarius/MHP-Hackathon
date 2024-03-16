def mdy_to_dmy(date):
    """Converts date from MM/DD/YYYY to DD/MM/YYYY format."""
    return date[3:5] + "/" + date[0:2] + "/" + date[6:10]
