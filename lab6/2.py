from datetime import datetime,timedelta
cdate=datetime.now()
yest=cdate-timedelta(days=1)
tw=cdate+timedelta(days=1)
print("yesterday:",yest)
print("today:",cdate)
print("tomorrow:",tw)