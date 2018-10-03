import boto3
import time
import csv
from boto3.dynamodb.conditions import Key, Attr

def datetime_from_utc_to_local(utc_datetime):
	time_difference  = 5.30 # it s in hours
	time_difference_hrs = int(time_difference)
	time_difference_min = (time_difference - time_difference_hrs)*100
	offset = (time_difference_hrs*3600) + (time_difference_min*60)
	return utc_datetime+offset

#LOCAL DATE TIME
date_time0 = '29.09.2018 21:53:29'
date_time1 = '29.09.2018 22:00:14'
pattern = '%d.%m.%Y %H:%M:%S'
epoch0 = int(time.mktime(time.strptime(date_time0, pattern)))
epoch1 = int(time.mktime(time.strptime(date_time1, pattern)))
epoch0 = epoch0*1000
epoch1 = epoch1*1000
#Use if Query time is in EPOCH GMT
#epoch0 = int(datetime_from_utc_to_local(epoch0)*1000)
#epoch1 = int(datetime_from_utc_to_local(epoch1)*1000)
print epoch0, epoch1
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DRIVE_CYCLE_DATA')
response = table.query(
    KeyConditionExpression=Key('deviceId').eq('VIM_2.4_3') & Key('timestamp').between(epoch0, epoch1)
)
line_count = 0
data = response['Items']

while 'LastEvaluatedKey' in response:
    response = table.query(
    	ExclusiveStartKey=response['LastEvaluatedKey'],
   	    KeyConditionExpression=Key('deviceId').eq('VIM_2.4_3') & Key('timestamp').between(epoch0, epoch1)
    	)
    data.extend(response['Items'])
timestr = time.strftime("%Y%m%d-%H%M%S")
with open(timestr + '.csv', 'wb') as csvfile: 
	filewriter = csv.writer(csvfile)#, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(['deviceId', 'timestamp', 'ACC', 'BV', 'CR', 'GYR', 'LAT_LON', 'RPM_KM', 'Sl_No.', 'TEMP', 'TIME'])
	for i in data:
		line_count += 1
		filewriter.writerow([ i['deviceId'], i['timestamp'], i['ACC'], i['BV'], i['CR'], i['GYR'], i['LAT_LON'], i['RPM_KM'], i['Sl_No.'], i['TEMP'], i['TIME']])
		my_time = i['timestamp']/1000
		my_time = my_time + ((5*3600) + (30*60))
		print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(int(my_time))))
print(line_count)
