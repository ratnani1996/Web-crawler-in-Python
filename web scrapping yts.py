import requests

from bs4 import BeautifulSoup

url="https://yts.ag/browse-movies?page="

def download_all_info(url,maxpages):
    fw=open("yts.txt","w+")
    for i in range(maxpages):
        fw.write("\t\t Page number "+str(i+1)+"\n\n")
        print "\t\t Page number ",i+1,"\n\n"
        full_url=url+str(i+1)
        response=requests.get(full_url)
        from itertools import izip
        soup=BeautifulSoup(response.content,"html.parser")
        data=soup.find_all("div" ,{"class" : "browse-movie-bottom"})

        for items in data:
            fw.write(items.contents[1].text.encode("utf-8")+"--"+items.contents[3].text.encode("utf-8")+"\n")
            print items.contents[1].text,"--",items.contents[3].text
    fw.close()
download_all_info(url,283)


