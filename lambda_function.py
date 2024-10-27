import json
from predict import Lamb

filename1 = '00280532F4625A5B21B74B29A47C010D9629F875'
filename2 = '0014D73E9987A3FC3DA1055D912286B95929DC6D'

tmp1 = Lamb()
tmp2 = tmp1.predict(filename1)
tmp3 = tmp1.predict(filename2)




"""
def handler(event, context):
    print(event)

    return {
        'statusCode': 200,
        'body': json.dumps(evnet)
    }
"""
