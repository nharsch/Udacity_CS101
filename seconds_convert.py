def convert_seconds(secs):
    minutes = (secs // 60) % 60
    hours = (secs // 60) // 60
    seconds = secs % 60 
    return int(hours), int(minutes), seconds
    


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
