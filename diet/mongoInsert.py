import requests # requests 라이브러리 설치 필요
import sys
import io
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

client = MongoClient('45.119.146.59', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.foodKcal

re = requests.get('http://openapi.foodsafetykorea.go.kr/api/ade319c400574705a22d/I0750/json/13001/14000')
rjson = re.json()

for i in range(0, len(rjson['I0750']['row'])):
#    print(rjson['I0750']['row'][i]['DESC_KOR']+rjson['I0750']['row'][i]['NUTR_CONT1']+rjson['I0750']['row'][i]['SERVING_WT'])
    food_list = {
                 'foodname': rjson['I0750']['row'][i]['DESC_KOR'],
                 'foodkcal' : rjson['I0750']['row'][i]['NUTR_CONT1'],
                 'portionsize' : rjson['I0750']['row'][i]['SERVING_WT']
                 }
    db.foodKcal.insert_one(food_list)
