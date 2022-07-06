from numpy import array
import requests
from bs4 import BeautifulSoup

try:
    main_site = 'https://en.wikipedia.org/'
    url = 'https://en.wikipedia.org/wiki/Main_Page'
    r = requests.get(url)
    if r.status_code == 200:
        main_site = 'https://en.wikipedia.org/'
        url = 'https://en.wikipedia.org/wiki/Main_Page'

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        titles = soup.find_all("div", {"id": "mp-tfa"})

        # getting title and full post link
        for title in titles:
            b = title.find('b')
            featured = b.text
            print(f'Title: {featured}')
            link = main_site+b.find('a').get('href')

        # following link of the full featured post
        flink = requests.get(link)
        fsoup = BeautifulSoup(flink.content, 'html.parser')

        # getting featured image
        try:
            img = fsoup.find_all('img')[1]
        except:
            img = "No Images to show"
        # paragraph
        try:
            p1 = fsoup.find_all('p')[1]
        except:
            p1 = ' '
        try:
            p2 = fsoup.find_all('p')[2]
        except:
            p2 = ' '
        try:
            p3 = fsoup.find_all('p')[3]
        except:
            p3 = ' '
        try:
            p4 = fsoup.find_all('p')[4]
        except:
            p4 = ' '
        try:
            p5 = fsoup.find_all('p')[4]
        except:
            p5 = ' '

        # writing html
        html_init = '''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Today's Featured Article</title>
            <link rel="stylesheet" href="style.css">
            <link rel="shortcut icon" href="favicon.png" type="image/x-icon">
        </head>
        <body>
            <h1>{heading}</h1>
            {thumbnail}
            {para1}
            {para2}
            {para3}
            {para4}
            {para5}
            
        </body>
        </html>
        '''

        # formatting html string and saving to a file
        html = html_init.format(heading=featured, thumbnail=img,
                                para1=p1, para2=p2, para3=p3, para4=p4, para5=p5)

        with open("index.html", 'wb') as file:
            file.write(html.encode())
            print("Article Updated Successfully")


except:
    print("No internet Connection")
