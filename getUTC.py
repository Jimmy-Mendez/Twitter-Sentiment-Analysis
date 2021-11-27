import datetime as dt

now = dt.datetime.utcnow()
#print("Time now: " + str(now))
fiveAgo = dt.datetime.utcnow() - dt.timedelta(minutes=5)
#print("Time 5 min ago: " + str(fiveAgo))