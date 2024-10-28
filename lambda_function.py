import json
from src.predict import Lamb

filename1 = '00280532F4625A5B21B74B29A47C010D9629F875'
filename2 = '0014D73E9987A3FC3DA1055D912286B95929DC6D'
filename3 = 'soft.zip'

"""
tmp1 = Lamb()
#tmp2 = tmp1.predict(filename1)
#tmp3 = tmp1.predict(filename2)
tmp4 = tmp1.predict(filename3)
"""



def handler(event, context):
    pred = Lamb()
    result = pred.predict(filename3)

    print(result)
    #return result


handler(1, 1)
