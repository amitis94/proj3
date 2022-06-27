from pymongo import MongoClient
import requests
from requests.exceptions import HTTPError
import json
import time

#몽고db연결
URI = 'mongodb+srv://amitis:rksk4137@cluster.etbe6rl.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(URI)
DATABASE = 'MovieDB'
mong0_data = client[DATABASE]

COLLECTION = 'movie_contents'
collection = mong0_data[COLLECTION]

COLLECTION2 = 'movie_company'
collection2 = mong0_data[COLLECTION2]

COLLECTION3 = 'movie_actor'
collection3 = mong0_data[COLLECTION3]

#영화목록 api로 받기
key = '37f1e565bd0eb7cee309289b6378ee66'

def searchcode(key, number):
    
    URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key='+key+'&itemPerPage='+'100'+'&curPage'+number
    try:
        resp = requests.get(URL)
        resp.raise_for_status()
        
    except HTTPError as Err:
        return 'HTTP 에러가 발생했습니다.'
    
    except Exception as Err:
        return '다른 에러가 발생했습니다.'
    
    else:
        return resp.text

def mvcompany(key, number):
    
    URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.json?key='+key+'&itemPerPage='+'100'+'&curPage'+number
    try:
        resp = requests.get(URL)
        resp.raise_for_status()
        
    except HTTPError as Err:
        return 'HTTP 에러가 발생했습니다.'
    
    except Exception as Err:
        return '다른 에러가 발생했습니다.'
    
    else:
        return resp.text

def mvactor(key, number):
    
    URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key='+key+'&itemPerPage='+'100'+'&curPage'+number
    try:
        resp = requests.get(URL)
        resp.raise_for_status()
        
    except HTTPError as Err:
        return 'HTTP 에러가 발생했습니다.'
    
    except Exception as Err:
        return '다른 에러가 발생했습니다.'
    
    else:
        return resp.text

#몽고db에 데이터 넣기
#searchcode는 먼저 테스트 하면서 돌려봄.
#새로 돌려보기 위해선 아래 for문처럼 만들어야 함
#time.sleep(5)

#for num in range(1,129):
    
#   data = mvcompany(key=key, number=str(num))
#  dict_data = json.loads(data)
#  collection2.insert_one(dict_data)

for num in range(1,1626)[:3]:
    
    print(num)
    data = mvactor(key=key, number=str(num))
    dict_data = json.loads(data)
    print(dict_data['peopleListResult'])

    #collection3.insert_one(dict_data)
    #time.sleep(10)