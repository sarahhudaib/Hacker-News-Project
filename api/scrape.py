import requests
from bs4 import BeautifulSoup
import pprint
from http.server import BaseHTTPRequestHandler , HTTPServer

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(all_rapper().encode())
    return
    
res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")
links = soup.select('.titlelink')
subtext = soup.select('.subtext')
links2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def all_rapper():
    def sort_stories_by_votes(hn_list):
        """ This function takes in a list of dictionaries and sorts them by votes """
        return sorted(hn_list, key=lambda key: key['votes'], reverse=True)


    def create_custom_hn(links, subtext):
        """ This function takes in a list of links and subtext and returns a list of dictionaries with the title, votes, and comments """
        hn = []
        for index, item in enumerate(links):
            title = item.getText()
            href = item.get('href', None)
            vote = subtext[index].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                # print (points)
                if points > 99:
                    hn.append({'title': title, 'href': href, 'votes': points})
        return sort_stories_by_votes(hn)
    
    pprint.pprint(create_custom_hn(mega_links, mega_subtext))


# print (create_custom_hn(links, subtext))
# create_custom_hn(links, subtext)

if __name__=='__main__':
    all_rapper()
    
