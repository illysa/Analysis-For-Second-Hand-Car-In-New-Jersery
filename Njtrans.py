
import requests
from bs4 import BeautifulSoup
#import libraries
rows=[]
def getReviews(movie_id):
    # variable to hold all reviews
    count=1
    
    page_url="http://autos.nj.com/search/location-07030/body-SUV/range-12500/page-"+str(count)+"/vcond-Used"
    #page_url="https://www.rottentomatoes.com/m/finding_dory/reviews/?page=16&sort="
    while page_url!=None:
        page_url="http://autos.nj.com/search/location-07030/body-SUV/range-12500/page-"+str(count)+"/vcond-Used"
        page = requests.get(page_url)
        count=count+1
        if page.status_code!=200: # a status code !=200 indicates a failure, exit the loop
            page_url=None
        else: # status_code 200 indicates success.
            soup = BeautifulSoup(page.content, 'html.parser')  
            print("*******")
            p=soup.select("#results")
            print len(p)
            
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
                for i in range(len(p_title)):
                    rows.append((p_title[i].get_text().encode('UTF-8'),p_price[i].get_text().encode('UTF-8'),p_info[j].get_text().encode('UTF-8'),p_info[j+1].get_text().encode('UTF-8'),p_info[j+2].get_text().encode('UTF-8'),p_info2[k].get_text().encode('UTF-8'),p_info2[k+1].get_text().encode('UTF-8')))
                    j=j+3
                    k=k+2
#                p_date=section.select("h2.title a")
#                #print len(p_date)
#                #get review
#                p_review=section.select("span.main-price-title large")
#                #get score
#                p_score1=section.select("span.properties-list-inner")
#                p_score=[item for item in p_score1 if item not in p_date]           
#                #print (len(p_score))
#            for i in range(len(p_score)):
#                rows.append((p_date[i].get_text(),p_review[i].get_text(),p_score[i].get_text()[12:]))
#    print len(rows)
    return rows
