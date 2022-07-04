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
            img = fsoup.find('div', class_='thumbinner').find('a').find('img')
        except:
            img = "No Images to show"
        # paragraph
        try:
            p1 = fsoup.select(
                'p:nth-child(10) , p:nth-child(9) , p:nth-child(8) , .hlist+ p')[0]
        except:
            p1 = ' '
        try:
            p2 = fsoup.select(
                'p:nth-child(10) , p:nth-child(9) , p:nth-child(8) , .hlist+ p')[1]
        except:
            p2 = ' '
        try:
            p3 = fsoup.select(
                'p:nth-child(10) , p:nth-child(9) , p:nth-child(8) , .hlist+ p')[2]
        except:
            p3 = ' '

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
        </body>
        </html>
        '''

        # formatting html string and saving to a file
        html = html_init.format(heading=featured, thumbnail=img,
                                para1=p1, para2=p2, para3=p3)

        with open("index.html", 'wb') as file:
            file.write(html.encode())
            print("Article Updated Successfully")


except:
    print("No internet Connection")
