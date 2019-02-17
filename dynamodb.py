import boto3
from boto3.dynamodb.conditions import Key, Attr
import datetime as dt
from datetime import date

def login():
	try:
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('iOweTea-login')
		response = table.scan()

		items = response['Items']

		return items
	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def get_data():
	try:
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('iOweTea-iotdata')

		startdate = date.today().isoformat()
		response = table.query(KeyConditionExpression=Key('id').eq('id_smartgarden') & Key('datetimeid').begins_with(startdate),
				ScanIndexForward=False
		)

		items = response['Items']

		n=1 # get latest data
		data = items[:n]
		print(data)
		return data
	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def get_chart_data():
	try:

		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('iOweTea-iotdata')

		startdate = date.today().isoformat()
		response = table.query(KeyConditionExpression=Key('id').eq('id_smartgarden') & Key('datetimeid').begins_with(startdate),
				ScanIndexForward=False
		)

		items = response['Items']

		n=15 # limit to last 15 items
		data = items[:n]
		data_reversed = data[::-1]
		return data_reversed
	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def get_status():
	try:
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('iOweTea-statusData')

		startdate = date.today().isoformat()
		response = table.query(KeyConditionExpression=Key('id').eq('id_status') & Key('datetimeid').begins_with(startdate),
				ScanIndexForward=False
		)

		items = response['Items']

		n=1
		data = items[:n]
		return data
	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def send_status(status):
	try:
		# print("status", status)
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('iOweTea-statusData')

		now = dt.datetime.now()
		new_item = {
			"id": "id_status",
			'datetimeid': now.isoformat(),
			'status': status
		}
		table.put_item(Item = new_item)

	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])


if __name__ == "__main__":
	query_data_from_dynamodb()
