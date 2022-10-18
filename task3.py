def season(month):
    season = "spring"
    if 2 >= month >= 1 or month == 12:
        season = "winter"
    elif 8 >= month >= 6:
        season = "summer"
    elif 11 >= month >= 9:
        season = "autumn"
    return season



