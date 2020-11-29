from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import docx
from csv import writer


html = urlopen('https://joyorganicsaffiliates.com/blog/')
bs = BeautifulSoup(html, 'html.parser')
# print(bs.prettify)

with open("image.csv",'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['id','source']
    csv_writer.writerow(headers )
    images = bs.find_all('img', {'src': re.compile('.jpg')})
    count = 1
    for image in images:
        # print(image['src']+'\n').
        csv_writer.writerow([count, image['src']]) 
        count += 1
        



with open("link.csv",'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['id','term']
    csv_writer.writerow(headers )
    anchors = bs.find_all('a')
    count = 1
    for link in anchors:
        if(link.get('href') != '#'): 
            linkText = "https://joyorganicsaffiliates.com/blog" +link.get('href')
            csv_writer.writerow([count, linkText]) 
            count += 1
        




mydoc = docx.Document()
mydoc.add_paragraph(bs.get_text())
mydoc.save("C:/Users/Buddha/Desktop/newf folder/textFile.docx")


