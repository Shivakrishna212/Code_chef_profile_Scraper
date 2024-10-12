import requests 
from bs4 import BeautifulSoup as bs



def scrapecodechef(username):
    url ="https://www.codechef.com/users/"+username
    html =requests.get(url)
    s=(bs(html.content,"html.parser"))
    del html
    details=dict()
    details["problems_solved"] = int(str(s.find_all("h3")[-1])[26:-5])
    details['latest_contest'] = (s.find_all("div",class_="contest-name")[0]).find("a").contents[0]
    details['latest_rank'] = s.find_all("div",id="global-rank-all")[0].find("strong").contents[0]
    details['current_rating' ] = s.find_all("div",class_="rating-number")[0].contents[0]
    return details
print(scrapecodechef("shivakrishna21"))

