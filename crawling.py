import requests
from bs4 import BeautifulSoup

def daum() :

    req = requests.get('https://www.daum.net/')


    soup = BeautifulSoup(req.text, 'html.parser')

    myList = []
    myList_href = []

    for i in soup.select("#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li"):
        myList.append(i.find("a").text)
        myList_href.append(i.find("a")["href"])

    return myList, myList_href


def today_humor() :

    req = requests.get('http://www.todayhumor.co.kr/board/list.php?table=bestofbest')


    soup = BeautifulSoup(req.text, 'html.parser')

    myList = []
    myList_href = []

    for i in soup.find_all("td", class_="subject") :
        myList.append(i.text)
        myList_href.append("http://www.todayhumor.co.kr/" + i.find("a")["href"])

    return myList,myList_href




def clien():

    req = requests.get('https://www.clien.net/service/recommend')


    soup = BeautifulSoup(req.text, 'html.parser')

    myList = []
    myList_href = []

    for i in soup.find_all("span", class_="subject_fixed") :
        myList.append(i.text)

    for i in soup.find_all("a", class_="list_subject") :
        myList_href.append("https://www.clien.net/" + i["href"])

    return myList, myList_href

