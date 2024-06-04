'''

You are given a list of dates in the format Dec 11 and a month in the format Dec as arguments.

Each date represents a video that was uploaded on that day.

Return the number of uploads for a given month.
'''

def upload_count(dates, month):
    count = 0
    for date in dates:
        if month in date:
            count += 1
    return count