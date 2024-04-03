#imports 

import requests
from bs4 import BeautifulSoup

URL = 'https://dolarbipolar.com'
class_list = set() 
page = requests.get( URL ) 
soup = BeautifulSoup( page.content , 'html.parser') 
tags = {tag.name for tag in soup.find_all()} 
for tag in tags: 
  
    
    for i in soup.find_all( tag ): 
        if i.has_attr( "class" ): 
    if len( i['class'] ) != 0: 
                class_list.add(" ".join( i['class'])) 
  
print( class_list ) 