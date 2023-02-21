from django.shortcuts import render
from MainApp.models import File, Candles
import pandas as pd
from django.http import JsonResponse,HttpResponse
from django.core import serializers
import json
from datetime import datetime
# Create your views here.

#Creating a new candle object and parsing it in json 
def create_candle(file_path, timeframe):
    df = pd.read_csv(file_path, delimiter=',', nrows=timeframe)
    list_of_csv = [list(row) for row in df.values]
    open, close = list_of_csv[0][3], list_of_csv[timeframe-1][6]
    high, low = 0, float('inf')
    date = str(list_of_csv[0][1])
    print(date)
    datetime_obj = datetime.strptime(date,'%y%m%d')
    # date_obj = datetime_obj.date()

    for i in list_of_csv:
        if high < i[4]:
            high = i[4]
        if i[5] < low:
            low = i[5]

    data = Candles.objects.create(open=open, high=high, low=low, close=close,date=date_obj) # To create the candle object
    candle = Candles.objects.values().first() # to get the data in dict type
    print(candle,type(candle))
    candle_json = json.dumps(candle)
    print(candle_json,type(candle_json)) 

    # for i in candle:
        # candle[i] = str(candle[i])

        # candle_json[i] = str(candle_json[i])
        # candle_json = serializers.serialize(json, candle)

    # with open('candle.json','w') as f:
    #     f.write(candle_json)

    # with open('cand.txt','w') as f:
    #     f.write(candle_json)
        # json.dump(candle, 'candle.json')

        
# Saves the csv file and timeframe in the django server and passes the file path and timeframe to create_candle
def index(request):

    if request.method == 'POST':
        file = request.FILES['file']
        timeframe = int(request.POST.get('timeframe'))
        obj = File.objects.create(file=file, timeframe=timeframe)
        res = create_candle(obj.file, timeframe)

    return render(request, 'MainApp/index.html')

