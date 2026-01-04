'''
Real World Example: Multithreading for I/O bound Tasks
scenario: Web scrapping
Web scrapping often inovlves making numerous network requests to 
fetch web pages. These tasks are I/O bound because they spend a lot of 
time waiting for responses from server. Multithreading can significantly 
impove the performance by allowing multiple web pages to be fetched concurrently.
'''

import threading 
import requests 
from bs4 import BeautifulSoup

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/concpets/',
'https://python.langchain.com/v0.2/docs/modules/',
'https://python.langchain.com/v0.2/docs/tutorials/',
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')
    
thread=[]

for url in urls:
    t=threading.Thread(target=fetch_content,args=(url,))
    thread.append(t)
    t.start()
    
for t in thread:
    t.join()
    
print("All web pages fecthed")