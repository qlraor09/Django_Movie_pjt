# import requests
# from pprint import pprint

# def data():
#     TMD_KEY = '35f4573a150eb6d257d0b497b9cfe878'
#     tmd_id = 'ken5609'
#     cnt =0
#     for n in range(1, 6):
#             num = str(n)
#             # 영화 목록 url
#             LIST_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={TMD_KEY}&language=ko-KR&page={num}"
#             listData = requests.get(LIST_URL)
#             resDatas = listData.json().get('results')
#     return resDatas

# pprint(data)
# import data from data 

import requests
from pprint import pprint
TMD_KEY = '35f4573a150eb6d257d0b497b9cfe878'
tmd_id = 'ken5609'
cnt =0
for n in range(1, 6):
        num = str(n)
        # 영화 목록 url
        LIST_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={TMD_KEY}&language=ko-KR&page={num}"
        listData = requests.get(LIST_URL)
        resDatas = listData.json().get('results')
pprint(resDatas)