# --*-- coding : utf-8 --*--
# --*-- author : silly rabbit --*--
import requests
from bs4 import BeautifulSoup
from main.csv_process import write_list, read_csv
from main.dic_process import dic2list

class Baike:
    def __init__(self):
       self.URL = 'https://baike.baidu.com/item/%E8%B6%8A%E5%85%89%E5%AE%9D%E7%9B%92'
       self.selectActorStr = 'body > div.body-wrapper.feature.large-feature.movieLarge > div.content-wrapper > div > div.main-content.J-content > div.main_tab.main_tab-defaultTab.curTab > div.basic-info.J-basic-info.cmn-clearfix > dl.basicInfo-block.basicInfo-right > dd > div > dl > dd > a'
       self.selectMovieStr = 'ul > li> ul > li > div > p > b.title > a'
       self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    def get_actors(self,url,selectStr):
        #根据电影百科界面获取主演，返回值形式为
        #[
        # ['张三','http://...'],
        # ['李四','http://...'],
        # ...
        # ]
        html = requests.get(url, headers = self.header)
        soup = BeautifulSoup(html.text,"html.parser")
        actor_name = soup.select(selectStr)
        actor_list = []

        try:
            for na in actor_name:
                actor_info = []

                actor_info.append(na.get_text())

                actor_info.append('https://baike.baidu.com'+na.get('href'))


                actor_list.append(actor_info)
        except Exception as e:
            print(e)
        return actor_list
    def get_movies(self,actor_name,url,selectStr):
        #根据演员百科获取其作品
        html = requests.get(url, headers = self.header)
        soup = BeautifulSoup(html.text,"html.parser")
        movie_name = soup.select(selectStr)
        #print(len(movie_name))
        movie_info = dict()
        list = []

        for name in movie_name:
            try:
                #movie_info[name.get_text()] = 'https://baike.baidu.com'+name.get('href')
                li = []
                li.append(actor_name)
                li.append(name.get_text())
                li.append('https://baike.baidu.com'+name.get('href'))
                #list.append(movie_info)
                list.append(li)
            except Exception as e:
                  print(e)
        return list



    def getActorByMovie(self):
        actor_dic = dict()
        movie_dic = dict()
        index = 0
        movielist = read_csv('movies.csv')

        for m in movielist:
            try:
                actors = cls.get_actors(m[2], '#marqueeViewport_actor > ul > li > ul > li > dl > dt > a')
                for a in actors:
                    if a[0] not in actor_dic:
                        actor_dic[a[0]] = a[1]
            except Exception as e:
                print(e)
            print('第' + str(index) + '条已完成,共' + str(len(movielist)) + '条')
            index += 1
        ans = []
        for key in actor_dic:
            actor_list = []
            actor_list.append(key)
            actor_list.append(actor_dic[key])
            ans.append(actor_list)
        write_list('actor.csv', ans)
    def get_movies(self):
        actorVisted = []
        index = 0

        actorlist = read_csv('actor.csv')
        for actor in actorlist:
            try:
                movies = cls.get_movies(actor[0], actor[1], 'ul > li> ul > li > div > p > b.title > a')
                write_list('movies.csv', movies)
                print('第' + str(index) + '条已完成,共' + str(len(actorlist)) + '条')
                index += 1
            except Exception as e:
                print(e)


if __name__== "__main__":
    cls = Baike()




