from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import sqlite3
from datetime import datetime
start_time = datetime.now()


conn = sqlite3.connect('seconddz.db')
cur = conn.cursor()

#создаем таблицу с ноутбуками
cur.execute("""CREATE TABLE IF NOT EXISTS laptops (  
   laptopid INTEGER PRIMARY KEY AUTOINCREMENT,
   laptopname VARCHAR(255),
   url VARCHAR(255),
   ddrtype VARCHAR(255),
   ddrvalue INTEGER,
   corefreq INTEGER,
   display VARCHAR(255),
   core INTEGER,
   price INTEGER,
   rank INTEGER,
   date DATETIME );
""")

 #cur.execute("""CREATE TABLE IF NOT EXISTS laptops (
  # laptopid INTEGER PRIMARY KEY AUTOINCREMENT,
 # laptopname VARCHAR(255),
 #  url VARCHAR(255),
 #  ddrtype VARCHAR(255),
#   ddrvalue INTEGER,
  # corefreq INTEGER,
#   display VARCHAR(255),
 #  core INTEGER,
#   price INTEGER,
 #  rank INTEGER,
 #  date DATETIME );
#""")











HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'
}
url = "https://www.regard.ru/catalog/1127/noutbuki"


def gethtml(URL, params=''):
    r = requests.get(URL, headers=HEADERS, params='').text
    return r


def getlinks(url):
    html=gethtml(url)

    soup=BeautifulSoup(html,'html.parser')
    items=soup.find('body').find('div', id='__next').find('div', 'regard-container').find('div', 'LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa').find('div', 'Grid_col__1pxvm Grid_col-10__29lE2 Grid_col-laptop-8-10__22VB0 Grid_col-tablet-12-12__2aj_r Listing_sticky-boundary').find('div', 'rendererWrapper').find('div', 'ListingRenderer_row__jqZol').find_all('div', 'Card_wrap__2fsLE Card_listing__LaohM Card_wrap_borderBottomHidden__3Yybd ListingRenderer_listingCard__XhvNd')

    items2=soup.find('body').find('div', id='__next').find('div', 'regard-container').find('div', 'LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa').find('div', 'Grid_col__1pxvm Grid_col-10__29lE2 Grid_col-laptop-8-10__22VB0 Grid_col-tablet-12-12__2aj_r Listing_sticky-boundary').find('div', 'rendererWrapper').find('div', 'ListingRenderer_row__jqZol').find_all('div', 'Card_wrap__2fsLE Card_listing__LaohM Card_wrap_borderBottomHidden__3Yybd ListingRenderer_listingCard__XhvNd')



    for item in items:
        linktype1=item.find('div','Card_row__3FoSA').find('a')['href']
        hh=item.find('div','Card_row__3FoSA').find('h6').get_text()
        hh = hh.replace('Ноутбук', '')
        linktype1='https://www.regard.ru'+str(linktype1)


        print(linktype1)
        time.sleep(2)
        propshtml=gethtml(linktype1)

        soup2 = BeautifulSoup(propshtml, 'html.parser')
        try:
            corefreq = soup2.find('body').find('div', id='__next').find('div', 'regard-container').find('div','LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa ProductCharacteristics_wrap__XqxyD').find('div', 'Grid_col__1pxvm Grid_col-12__3cRIY').find('div', 'ProductCharacteristics_masonry__2ybUN').find_all('section', 'CharacteristicsSection_section__2Vu5s CharacteristicsSection_open__3YYlm')[2].find('div', 'rah-static rah-static--height-auto').find('div', 'CharacteristicsSection_content__dsggI').find_all('div', 'CharacteristicsItem_item__mn1cf')[3].find('div','CharacteristicsItem_value__3-EWJ').find('span', 'CharacteristicsItem_valueData__3RL19').get_text()
            ddrvalue = soup2.find('body').find('div', id='__next').find('div', 'regard-container').find('div','LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa ProductCharacteristics_wrap__XqxyD').find('div', 'Grid_col__1pxvm Grid_col-12__3cRIY').find('div', 'ProductCharacteristics_masonry__2ybUN').find_all('section', 'CharacteristicsSection_section__2Vu5s CharacteristicsSection_open__3YYlm')[3].find('div', 'rah-static rah-static--height-auto').find('div', 'CharacteristicsSection_content__dsggI').find('div', 'CharacteristicsItem_item__mn1cf').find('div','CharacteristicsItem_value__3-EWJ').find('span').get_text()
            display = soup2.find('body').find('div', id='__next').find('div', 'regard-container').find('div','LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa ProductCharacteristics_wrap__XqxyD').find('div', 'Grid_col__1pxvm Grid_col-12__3cRIY').find('div', 'ProductCharacteristics_masonry__2ybUN').find_all('section', 'CharacteristicsSection_section__2Vu5s CharacteristicsSection_open__3YYlm')[1].find('div', 'rah-static rah-static--height-auto').find('div', 'CharacteristicsSection_content__dsggI').find_all('div', 'CharacteristicsItem_item__mn1cf')[0].find('div','CharacteristicsItem_value__3-EWJ').find('span').get_text()

            ddrtype = soup2.find('body').find('div', id='__next').find('div', 'regard-container').find('div','LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa ProductCharacteristics_wrap__XqxyD').find('div', 'Grid_col__1pxvm Grid_col-12__3cRIY').find('div', 'ProductCharacteristics_masonry__2ybUN').find_all('section', 'CharacteristicsSection_section__2Vu5s CharacteristicsSection_open__3YYlm')[3].find('div', 'rah-static rah-static--height-auto').find('div', 'CharacteristicsSection_content__dsggI').find_all('div', 'CharacteristicsItem_item__mn1cf')[1].find('div','CharacteristicsItem_value__3-EWJ').find('span').get_text()

            core = soup2.find('body').find('div', id='__next').find('div', 'regard-container').find('div','LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa ProductCharacteristics_wrap__XqxyD').find('div', 'Grid_col__1pxvm Grid_col-12__3cRIY').find('div', 'ProductCharacteristics_masonry__2ybUN').find_all('section', 'CharacteristicsSection_section__2Vu5s CharacteristicsSection_open__3YYlm')[2].find('div', 'rah-static rah-static--height-auto').find('div', 'CharacteristicsSection_content__dsggI').find_all('div', 'CharacteristicsItem_item__mn1cf')[0].find('div','CharacteristicsItem_value__3-EWJ').find('span').get_text()
            price = soup2.find('body').find('div', id='__next').find('div', 'regard-container').find('div','LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa').find_all('div','Grid_col__1pxvm Grid_col-6__2cB2p Grid_col-laptop-6-12__8YlXQ Grid_col-mobile-12-12__21fi-')[1].find('div', 'Grid_row__ZvFHa').find_all('div','Grid_col__1pxvm Grid_col-6__2cB2p Grid_col-tablet-12-12__2aj_r')[1].find('div', 'PriceBlock_wrap__2cHBa').find('div','PriceBlock_bottom__3Dpzh').find('div', 'PriceBlock_priceBlock__VzjwV').find('span').string
            price = str(price)
            price = price.replace('\xa0', '')
            price = price.replace('₽', '')
            price = price.replace(' ', '')
            rank = round(float(corefreq) * 0.001 + float(ddrvalue) * 1.2 + float(price) * (-0.0001), 2)
            #print(rank)

            SQL = "INSERT INTO laptops ('laptopname','url','core', 'corefreq','ddrvalue' , 'price', 'rank', 'ddrtype','display','date') VALUES('" + str(hh) + "','" + str(linktype1) + "','" + str(core) + "','" + str(corefreq) + "','" + str(ddrvalue) + "','" + str(price) + "','" + str(rank) + "','" + str(ddrtype) + "','" + str(display) + "', datetime('now'))"

            db = sqlite3.connect('seconddz.db')
            cursor = db.execute(SQL)
            db.commit()
        except:
            print('кривые данные')




    for item in items2:
        linktype2 = item.find('div', 'Card_row__3FoSA').find('a')['href']
        linktype2 = 'https://www.regard.ru' + str(linktype2)
        print(linktype2)
        hh = item.find('div', 'Card_row__3FoSA').find('h6').get_text()
        propshtml = gethtml(linktype2)
        time.sleep(5)
        soup2 = BeautifulSoup(propshtml, 'html.parser')
        try:
            corefreq = soup2.find('body').find('div', id='__next').find('div', 'regard-container').find('div','LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa ProductCharacteristics_wrap__XqxyD').find('div','Grid_col__1pxvm Grid_col-12__3cRIY').find('div', 'ProductCharacteristics_masonry__2ybUN').find_all('section','CharacteristicsSection_section__2Vu5s CharacteristicsSection_open__3YYlm')[2].find('div', 'rah-static rah-static--height-auto').find('div','CharacteristicsSection_content__dsggI').find_all('div', 'CharacteristicsItem_item__mn1cf')[3].find('div', 'CharacteristicsItem_value__3-EWJ').find('span','CharacteristicsItem_valueData__3RL19').get_text()
            ddrvalue = soup2.find('body').find('div', id='__next').find('div', 'regard-container').find('div','LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa ProductCharacteristics_wrap__XqxyD').find('div','Grid_col__1pxvm Grid_col-12__3cRIY').find('div', 'ProductCharacteristics_masonry__2ybUN').find_all('section','CharacteristicsSection_section__2Vu5s CharacteristicsSection_open__3YYlm')[3].find('div', 'rah-static rah-static--height-auto').find('div','CharacteristicsSection_content__dsggI').find('div', 'CharacteristicsItem_item__mn1cf').find('div', 'CharacteristicsItem_value__3-EWJ').find('span').get_text()
            display = soup2.find('body').find('div', id='__next').find('div', 'regard-container').find('div','LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa ProductCharacteristics_wrap__XqxyD').find('div','Grid_col__1pxvm Grid_col-12__3cRIY').find('div', 'ProductCharacteristics_masonry__2ybUN').find_all('section','CharacteristicsSection_section__2Vu5s CharacteristicsSection_open__3YYlm')[1].find('div', 'rah-static rah-static--height-auto').find('div','CharacteristicsSection_content__dsggI').find_all('div', 'CharacteristicsItem_item__mn1cf')[0].find('div', 'CharacteristicsItem_value__3-EWJ').find('span').get_text()

            ddrtype = soup2.find('body').find('div', id='__next').find('div', 'regard-container').find('div','LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa ProductCharacteristics_wrap__XqxyD').find('div','Grid_col__1pxvm Grid_col-12__3cRIY').find('div', 'ProductCharacteristics_masonry__2ybUN').find_all('section','CharacteristicsSection_section__2Vu5s CharacteristicsSection_open__3YYlm')[1].find('div', 'rah-static rah-static--height-auto').find('div','CharacteristicsSection_content__dsggI').find_all('div', 'CharacteristicsItem_item__mn1cf')[0].find('div', 'CharacteristicsItem_value__3-EWJ').find('span').get_text()


            core = soup2.find('body').find('div', id='__next').find('div', 'regard-container').find('div','LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa ProductCharacteristics_wrap__XqxyD').find('div','Grid_col__1pxvm Grid_col-12__3cRIY').find('div', 'ProductCharacteristics_masonry__2ybUN').find_all('section','CharacteristicsSection_section__2Vu5s CharacteristicsSection_open__3YYlm')[2].find('div', 'rah-static rah-static--height-auto').find('div','CharacteristicsSection_content__dsggI').find_all('div', 'CharacteristicsItem_item__mn1cf')[0].find('div', 'CharacteristicsItem_value__3-EWJ').find('span').get_text()
            price = soup2.find('body').find('div', id='__next').find('div', 'regard-container').find('div','LayoutWrapper_wrap__Onh8G').find('main').find('div', 'Grid_row__ZvFHa').find_all('div','Grid_col__1pxvm Grid_col-6__2cB2p Grid_col-laptop-6-12__8YlXQ Grid_col-mobile-12-12__21fi-')[1].find('div', 'Grid_row__ZvFHa').find_all('div','Grid_col__1pxvm Grid_col-6__2cB2p Grid_col-tablet-12-12__2aj_r')[1].find('div', 'PriceBlock_wrap__2cHBa').find('div', 'PriceBlock_bottom__3Dpzh').find('div','PriceBlock_priceBlock__VzjwV').find( 'span').get_text()
            price = str(price)
            price = price.replace('\xa0', '')
            price = price.replace('₽', '')
            price = price.replace(' ', '')
            rank = round(float(corefreq) * 0.001 + float(ddrvalue) * 0.2 + float(price) * (-0.0001),2)
            print(rank)
            SQL = "INSERT INTO laptops ('laptopname','url','core', 'corefreq','ddrvalue' , 'price', 'rank', 'ddrtype','display','date') VALUES('" + str(hh) + "','" + str(linktype2) + "','" + str(core) + "','" + str(corefreq) + "','" + str(ddrvalue) + "','" + str(price) + "','" + str(rank) + "','" + str(ddrtype) + "','" + str(display) + "', datetime('now'))"
            db = sqlite3.connect('seconddz.db')
            cursor = db.execute(SQL)
            db.commit()
        except:
            print('кривые данные')


def getlinksoldi(url):
    html = gethtml(url)
    soup = BeautifulSoup(html, 'html.parser')

    items=soup.find('body').find('div', 'site-wrapper').find('div', 'site-content').find('div', 'layout catalog-page catalog').find('div', 'container').find('div', 'catalog-view view-row view-filter-on').find('div','row').find_all('div', 'col')[1].find('form').find('div',id='view-row').find_all('div','col-12')#.find_all('span')#[2]#.find_all('span')#.find_all('div','col-12')#.find_all('div', 'col product-specification')
    i = 0
    while i < len(items):
        try:
            item=items[i].find_all('span','d-flex jsg-replace-link')[0]['data-href']#.find('div', 'goods-tile preview-product').find('div').find('span')
            name = items[i].find_all('span', 'd-flex jsg-replace-link')[0].find('img')['alt'] # .find('div', 'goods-tile preview-product').find('div').find('span')
            name=name.title()
            name=name.replace('Ноутбук', '')
            item=item.replace('//', 'https://')
            specificationhtml=gethtml(str(item))
            time.sleep(7)
            soup4 = BeautifulSoup(specificationhtml, 'html.parser')
            price=soup4.find('body').find('div','site-wrapper').find('div','site-content').find('div','layout card-product-page catalog').find('div','container').find('div', 'card-product').find('div','row').find_all('div', 'col')[1].find('div', 'about_product_box credit about_product_box--new-style w100 product-new-price-dc-view').find('div','region_block product-new-price-dc-view').find('div','product-price-block').find('div','product-price').find('div', 'product-price__current').get_text()
            price=price.replace(' ', '')
            price = price.replace('₽', '')
            core=soup4.find('body').find('div','site-wrapper').find('div','site-content').find('div','layout card-product-page catalog').find('div','tabs-container accordion tabs-card-product').find('div', 'tab-content').find('div', 'tab-pane fade active show').find('div', 'card').find('div', id='collapseDescription').find('div','container').find('div', 'row').find('div', 'col').find('div', 'det-content clearfix').find('div', id='opisAndTTH').find('div', 'det-content-block').find('div', 'det-content-inner').find('div', 'params-list params-list--in-product').find_all('div', 'params-list__item')[6].find('span').get_text()
            corefreq=soup4.find('body').find('div','site-wrapper').find('div','site-content').find('div','layout card-product-page catalog').find('div','tabs-container accordion tabs-card-product').find('div', 'tab-content').find('div', 'tab-pane fade active show').find('div', 'card').find('div', id='collapseDescription').find('div','container').find('div', 'row').find('div', 'col').find('div', 'det-content clearfix').find('div', id='opisAndTTH').find('div', 'det-content-block').find('div', 'det-content-inner').find('div', 'params-list params-list--in-product').find_all('div', 'params-list__item')[10].find('span').get_text()
            ddrvalue=soup4.find('body').find('div','site-wrapper').find('div','site-content').find('div','layout card-product-page catalog').find('div','tabs-container accordion tabs-card-product').find('div', 'tab-content').find('div', 'tab-pane fade active show').find('div', 'card').find('div', id='collapseDescription').find('div','container').find('div', 'row').find('div', 'col').find('div', 'det-content clearfix').find('div', id='opisAndTTH').find('div', 'det-content-block').find('div', 'det-content-inner').find('div', 'params-list params-list--in-product').find_all('div', 'params-list__item')[11].find('span').get_text()
            ddrtype=soup4.find('body').find('div','site-wrapper').find('div','site-content').find('div','layout card-product-page catalog').find('div','tabs-container accordion tabs-card-product').find('div', 'tab-content').find('div', 'tab-pane fade active show').find('div', 'card').find('div', id='collapseDescription').find('div','container').find('div', 'row').find('div', 'col').find('div', 'det-content clearfix').find('div', id='opisAndTTH').find('div', 'det-content-block').find('div', 'det-content-inner').find('div', 'params-list params-list--in-product').find_all('div', 'params-list__item')[12].find('span').get_text()
            display=soup4.find('body').find('div','site-wrapper').find('div','site-content').find('div','layout card-product-page catalog').find('div','tabs-container accordion tabs-card-product').find('div', 'tab-content').find('div', 'tab-pane fade active show').find('div', 'card').find('div', id='collapseDescription').find('div','container').find('div', 'row').find('div', 'col').find('div', 'det-content clearfix').find('div', id='opisAndTTH').find('div', 'det-content-block').find('div', 'det-content-inner').find('div', 'params-list params-list--in-product').find_all('div', 'params-list__item')[2].find('span').get_text()
            if str(ddrtype)!='SSD M.2' and str(ddrtype)!='SSD':

                try:
                    rank = round(float(corefreq) * 0.001 + float(ddrvalue) * 0.2 + float(price) * (-0.0001), 2)

                    SQL = "INSERT INTO laptops ('laptopname','url','core', 'corefreq','ddrvalue' , 'price', 'rank', 'date', 'ddrtype','display') VALUES('" + str(name) + "','" + str(item) + "','" + str(core) + "','" + str(corefreq) + "','" + str(ddrvalue) + "','" + str(price) + "','" + str(rank) + "',datetime('now'),'" + str(ddrtype) + "','" + str(display)+"')"

                    db = sqlite3.connect('seconddz.db')
                    cursor = db.execute(SQL)
                    db.commit()
                except:
                    print('кривые данные')
            else:
                print('кривые данные')









        except:
            print('кривые данные')

        i += 2



def circle():
    for i in range(1,20):
        url="https://www.holodilnik.ru/digital_tech/notebook/?page="+str(i)
        print(url)
        getlinksoldi(url)
        time.sleep(8)


    for i in range(1,40):
        url="https://www.regard.ru/catalog/1127/noutbuki?page="+str(i)

        getlinks(url)
        time.sleep(8)


circle()

db = sqlite3.connect('seconddz.db')

df=pd.read_sql('SELECT * FROM laptops ORDER by rank DESC',db,)
top5=df.drop_duplicates(subset=['url']).head()
print(top5[["laptopname", "rank"]])
print(datetime.now() - start_time)
