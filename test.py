import requests
from bs4 import BeautifulSoup
import random

url = "https://movie.naver.com/movie/running/current.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req,'html.parser')

title_tag = doc.select('dt.tit > a')
star_tag = doc.select('div.star_t1 > a > span.num')
reserve_tag = doc.select('div.star_t1.b_star > span.num')

#순위 형태와 함께 dic형태로 만들기
movie_dic = {}
for i in range(0,10):
    movie_dic[i] = {
        "title":title_tag[i].text,
        "star":star_tag[i].text,
        "reserve": reserve_tag[i].text
        
    }

pick_movie = movie_dic[random.randrange(0,10)]

https://movie-phinf.pstatic.net/20180730_82/15329286640280Wu1t_JPEG/movie_image.jpg?type=m99_141_2

# return_doc_movies = doc.select('dt.tit > a')
#list_movies = []
#for i in return_doc_movies :
 # list_movies.append(i.text) 

#return_doc_stars = doc.select('div.star_t1 > a > span.num')
#list_stars = []
#for j in return_doc_stars :
 #   list_stars.append(j.text)
    
#return_doc_reserve = doc.select('div.star_t1 > span.num')
#list_reserve = []
#for k in return_doc_reserve :
 #   list_reserve.append(k.text)
    
#print(list_movies, list_stars, list_reserve) 