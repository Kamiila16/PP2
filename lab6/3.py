from datetime import datetime,timedelta
cdate=datetime.now()
dwm=cdate.replace(microsecond=0)
print(dwm)