from bs4 import BeautifulSoup as bs
from lib.static import KincirAPI,IMDBAPI,errorMessage,headers,VersionScrap,DocumentationUrl
import requests
from flask import request as req
import urllib.parse
import time

def getRootData():
        return {
            'documentation': DocumentationUrl,
            'version': VersionScrap,
            'status':'1'
        }
def getReviews(page):
    newUrl = KincirAPI['url'] + 'apis/v1/posts/postByTypeAndPostsgroup/movie-reviews?limit=30&page='+str(page)
    ret = requests.get(newUrl , headers={'User-Agent':headers['User-Agent'],'Authorization':getKincirAuth()})
    jsondata = ret.json()
    datas = []
    for item in jsondata['data']['posts']:
        datas.append({
            'id':item['url']+"-"+item['uniqueUrl'],
            'title':item['title'],
            'image':KincirAPI['cdn']+item['image'][1:] if len(item['image']) >0 and item['image'][0] == "/" else item['image'],
            'rating':item['rating'],
            'views':item['views'],
            'excerpt':item['excerpt'],
            'date':item['createdAt'],
            'type':item['type'], 
        })
    jsondata['status']=1
    jsondata['data']=datas
    jsondata['version']=VersionScrap
    return jsondata
def getReview(id):
    newUrl = KincirAPI['url'] + 'movie/cinema/' +str(id)
    ret = requests.get(newUrl , headers={'User-Agent':headers['User-Agent']})
    soup = bs(ret.text , 'html.parser')
    if ret.status_code == 200:
        judul = soup.find('h1',attrs={'class' : 'category'}).get_text().strip()
        author = soup.find('span',attrs={'class' : 'author'}).find('a').get_text().strip()
        tgl = soup.find('span',attrs={'class' : 'author'}).get_text().strip().split('/')[1].strip()
        des = soup.find('div',attrs={'class':'content-detail'}).get_text().strip()
        img = soup.find('div',attrs={'class':'head-img'}).find('img').get('src').split('/production/')[1]
        return {
            'data' : {
                'title':judul,
                'author':author,
                'date':tgl,
                'article':des,
                'image':'https://cdn.kincir.com/2/production/'+img
            },
            'version': VersionScrap,
            'status':'1'
        }
    else:
        return errorMessage
def getRatings(page):
    newUrl = IMDBAPI['url'] + 'en/API/MostPopularMovies/' + IMDBAPI['key']
    ret = requests.get(newUrl , headers=headers)
    jsondata = ret.json()
    jsondata['data']=jsondata['items']
    jsondata.pop('items', None)
    jsondata.pop('errorMessage',None)
    jsondata['status']=1
    jsondata['version']=VersionScrap
    return jsondata
def getSearch(a,keyword,page):
    if(a=="review"):
        newUrl = KincirAPI['url'] + 'apis/v1/posts/search'
        ret = requests.get(newUrl , headers={'User-Agent':headers['User-Agent'],'Authorization':KincirAPI['key']} ,params=[('search',keyword), ('limit','30'), ('page',page)])
        jsondata = ret.json()
        datas = []
        for item in jsondata['data']['posts']:
            datas.append({
                'id':item['url']+"-"+item['uniqueUrl'],
                'title':item['title'],
                'image':KincirAPI['cdn']+item['image'][1:] if len(item['image']) >0 and item['image'][0] == "/" else item['image'],
                'rating':0,
                'views':item['views'],
                'excerpt':item['excerpt'],
                'date':item['createdAt'],
                'type':item['type'], 
            })
        jsondata['data']=datas
    elif(a=="rating"):
        newUrl = IMDBAPI['url'] + 'en/API/SearchMovie/'+ IMDBAPI['key']+"/"+keyword
        ret = requests.get(newUrl , headers={'User-Agent':headers['User-Agent']})
        jsondata = ret.json()
        datas = []
        for item in jsondata['results']:
            if(len(datas)>2): break
            newUrl_ex = IMDBAPI['url'] + 'en/API/Ratings/'+ IMDBAPI['key']+"/"+item['id']
            ret_ex = requests.get(newUrl_ex , headers={'User-Agent':headers['User-Agent']})
            jsondata_ex = ret_ex.json()
            datas.append({
                'id':item['id'],
                'title':item['title'],
                'image':item['image'],
                'rating':jsondata_ex['imDb'],
                'fullTitle':jsondata_ex['fullTitle'],
                'type':jsondata_ex['type'],
                'year':jsondata_ex['year'],
                'imDbRating':jsondata_ex['imDb'],
            })
            jsondata.pop('results', None)
            jsondata.pop('errorMessage',None)
            jsondata.pop('expression',None)
            jsondata['data']=datas
    else:
        return errorMessage
    jsondata['status']=1
    jsondata['version']=VersionScrap
    return jsondata 
def getKincirAuth():
    current_time = time.time()
    if(KincirAPI['expired']<current_time):
        newUrl_ex = KincirAPI['url'] + 'apis/v1/auth'
        ret_ex = requests.post(newUrl_ex , headers={'User-Agent':headers['User-Agent']},data=KincirAPI['auth'])
        KincirAPI['expired'] = ret_ex.json()['data']['auth']['expiredAt']
        KincirAPI['key'] = 'Bearer '+ret_ex.json()['data']['auth']['accessToken']
    return KincirAPI['key']