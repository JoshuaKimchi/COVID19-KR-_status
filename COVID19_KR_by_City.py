import requests, bs4
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import unquote, quote_plus, urlencode
from xml.etree import ElementTree as ET
from datetime import datetime, timedelta, date

# Service URL
xmlUrl = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'

My_API_Key = unquote('본인의 키') # 본인의 키를 공공데이터포털에서 받아서 입력(입력필요)
f=open("covid19kr.txt",'w')
f.write("날짜,도시,총확진자,증감량\n")

timestart=date(2020,3,1)    #시작할 날짜 지정(3월부터 데이터가 있음)

while date.today()>timestart:
    dstart=timestart.strftime("%Y%m%d")
    queryParams = '?' + urlencode(
        {
            quote_plus('ServiceKey') : My_API_Key,
            quote_plus('startCreateDt') : dstart,
            quote_plus('endCreateDt') : dstart
        }
    )
    try:
        response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
        root = ET.fromstring(response)
        items = root.findall('.//item')
        for item in items:
            city = item.find('gubun').text      #도시명(한글)
            confirm = item.find('defCnt').text  #확진자 누적수
            incdec = item.find('incDec').text   #확진자 증감량
            dstart2=timestart-timedelta(days=1) #하루전 데이터기 때문에 하루 빼줌
            dstart2=dstart2.strftime("%Y/%m/%d")
            f.write(dstart2+","+city+","+confirm+","+incdec+"\n")
        print(dstart,"자료 기록중")
    except Exception as e:
        print(dstart,e)
    timestart=timestart+timedelta(days=1)
f.close()