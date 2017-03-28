import requests
from bs4 import BeautifulSoup


full_url="http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los%20Angeles%2C%20CA&page="
def download_all_info(url,pages=5):
    page=1
    fw=open("sample.txt","w+")
    while(page<=pages):

        full_url=url+str(page)

        r=requests.get(full_url)
        soup=BeautifulSoup(r.content,"html.parser")

        g_data=soup.find_all("div",{"class" : "info"})
        for items in g_data:
            fw.write(items.contents[0].find_all("a",{"class" : "business-name"})[0].text+"\n")
            print items.contents[0].find_all("a",{"class" : "business-name"})[0].text
            try:
                fw.write(items.contents[1].find_all("span",{"itemprop" : "streetAddress"})[0].text)
                print items.contents[1].find_all("span",{"itemprop" : "streetAddress"})[0].text
            except:
                pass
            try:
                fw.write(items.contents[2].find_all("span", {"itemprop" : "addressLocality"})[0].text,"\n")
                print items.contents[2].find_all("span", {"itemprop" : "addressLocality"})[0].text,"\n"

            except:
                pass
        page+=1
    fw.close()
download_all_info(full_url)

