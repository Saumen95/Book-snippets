import time


def tostring(num):
    return ('0'+str(num))[-2:]


seconds_since_epoch = int(time.time())
seconds_per_day = 24 * 60 * 60
seconds_since_midnight = seconds_since_epoch % seconds_per_day
gmt_sec = seconds_since_midnight % 60
gmt_hr = seconds_since_midnight // (60 * 60)
gmt_min = (seconds_since_midnight - (gmt_hr * 60 * 60)) // 60

print('There have been', seconds_since_epoch // seconds_per_day, 'days since Jan 1, 1970.')
print('It has been', gmt_hr, 'hours,', gmt_min, 'minutes, and', gmt_sec, 'seconds since midnight GMT.')
print('Current GMT is', tostring(gmt_hr) + ':' + tostring(gmt_min) + ':' + tostring(gmt_sec) + '.')