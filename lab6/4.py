from datetime import datetime
date_str1 = input()
date_str2 = input()

try:
    
    date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

    time_difference = (date2 - date1).total_seconds()

    print("The time difference in seconds is:", time_difference)

except ValueError:
    print("Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS' format.")
