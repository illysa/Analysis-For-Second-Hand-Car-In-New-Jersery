import requests
from bs4 import BeautifulSoup
import unicodedata
import csv
from time import sleep
count_page=1
with open('suv_csv.csv', "a") as out_f:
    writer = csv.writer(out_f)
    writer.writerow(["title", "price","engine","transmission","drivetrain","mileage","location"])
page_url="http://autos.nj.com/search/location-07030/body-SUV/range-12500/page-"+str(count_page)+"/vcond-Used"
def parse(string):
    string=unicodedata.normalize('NFKD', string).encode('ascii','ignore')
    return string.replace("\n", "")
while page_url!=None:
    #use circulation to get all pages
    page_url="http://autos.nj.com/search/location-07030/body-SUV/range-12500/page-"+str(count_page)+"/vcond-Used"
    print(count_page)
    sleep(0.8)
    page = requests.get(page_url)    
    count_page+=1
    if page.status_code!=200:
        page_url=None
    else:       
        soup = BeautifulSoup(page.content, 'html.parser')  
        
        rows=[]
        #the content I need
        print("*******")
        p=soup.select("#results")
        for count in range(len(p)):
            print("**************************")
            div=p[count]
            p_title=div.select(".title")
            #print p_title
            p_price=div.select(".main-price-title")
            p_info=div.select(".properties-list-inner .hidden-mobile")
            p_info2=div.select(".properties-list-inner .r-card-visible-item")
            print("**************************")
            j=0
            k=0
            #get contents and format them
            for i in range(len(p_title)):
                    title = parse(p_title[i].get_text())
                    price = parse(p_price[i].get_text()).strip()
                    engine = parse(p_info[j].get_text())
                    transmission = parse(p_info[j+1].get_text())
                    drivetrain = parse(p_info[j+2].get_text())
                    mileage = parse(p_info2[k].get_text().replace("Mileage","")).strip()
                    location = parse(p_info2[k+1].get_text().replace("Location","").replace(" ",""))
                    #CSV
                    rows.append([title,price,engine,transmission,drivetrain,mileage,location])
                    j=j+3
                    k=k+2
        with open('suv_csv.csv', "a") as out_f:
            writer = csv.writer(out_f)
            writer.writerows(rows)  