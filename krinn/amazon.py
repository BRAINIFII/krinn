"""A simple amazon module.

This module helps in getting the price or title of a product by 
simply using a URL or a Product ID.A product ID is available in
the link itself.

Example:
        https://www.amazon.in/Zebronics-100HB-High-Speed-Port/dp/B07GLNJC25/ref=sr_1_1_sspa?spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbG
        Here in the above link the id is B07GLNJC25.

More information on:
   https://github.com/BRAINIFII/krinn/

"""
import requests
from bs4 import BeautifulSoup
from user_agents import parse
import os.path
import os
import sys
from urllib.parse import urlparse

global i
price = 0
product_title=""
product_price=""

i = 0

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

global prog_location,lenrange

lenrange = 40      #title notification range

tmout = 5          # Value in hours
prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
notifytimeout = tmout * 60 * 60

def short(url):
    """Function to get short url
    
    Arguments:
        url {string} -- URL of the product.

    Returns: string -- A string value which contains a short url.
    """
    shorturl=getid(url)
    shorturl = "https://www.amazon.in/dp/"+shorturl+"/"
    return shorturl

def crawlbyid(id):
    """Function to get product data using id.
    
    Arguments:
        url {string} -- ID of the product.

    Returns: string -- A list value which contains a title and price of the product.
    """
    url = "https://www.amazon.in/dp/"+id+"/"
    # print("byid: ",url)
    values = crawlbyurl(url)
    return values

def getid(url):
    """Function to get product ID.
    
    Arguments:
        getid {string} -- URL of the product.

    Returns: string -- A string value which contains ID of the product.
    """
    if("/dp/" in url):
        linkid = urlparse(url).path
        linkid = linkid[linkid.index("dp"):linkid.index("ref")]
        linkid = linkid[3:-1]
        return linkid
    elif("/product/" in url):
        # print("product")
        linkid = urlparse(url).path
        linkid = linkid[linkid.index("product"):linkid.index("ref")]
        linkid = linkid[8:-1]
        return linkid

def crawlbyurl(URL):
    """Function to get product data using URL.
    
    Arguments:
        url {string} -- URL of the product.

    Returns: string -- A list value which contains a title and price of the product.
    """
    
    global price,product_title,product_price
    # print("Given URL : ",URL + "\n")
    shurl = URL
    page = requests.get(shurl, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice")
    try :
        price = soup.find(id="priceblock_ourprice").get_text()

        if type(price) is str:
            price = price[1:]
            product_price = float(price.replace(",", ""))
            price_notif = str(product_price)
            prd_title = title.strip()
            product_title = prd_title.replace("'","")
            list = []
            list.append(product_title)
            list.append(product_price)
            return list
            

        else:
            print("Product Not Found")

    except AttributeError:
        try :
            price = soup.find(id="priceblock_dealprice").get_text()
            if type(price) is str:
                price = price[1:]
                product_price = float(price.replace(",", ""))
                prd_title = title.strip()
                product_title = prd_title.replace("'","")
                list = []
                list.append(product_title)
                list.append(product_price)
                return list
                
            else:
                print("Product Not Found")
        except AttributeError:
            try:
                price = soup.find(id="priceblock_saleprice").get_text()
                if type(price) is str:
                    price = price[1:]
                    product_price = float(price.replace(",", ""))
                    price_notif = str(product_price)
                    prd_title = title.strip()
                    product_title = prd_title.replace("'","")
                    list = []
                    list.append(product_title)
                    list.append(product_price)
                    return list
                    
                else:
                    print("Product Not Found")
            except AttributeError:
                print("Product unavailable")






def producttitle(url):
    """Function to get title of the given url.
    
    Arguments:
        url {string} -- URL of the product. 
    
    Returns:
        string -- A string value which contains product title.
    """
    productlist = crawlbyurl(url)
    title = productlist[0]
    return title


def productprice(url):
    """Function to get price of the given url.
    
    Arguments:
        url {string} -- URL of the product. 
    
    Returns:
        string -- A string value which contains product price.
    """                
    productlist = crawlbyurl(url)
    price = productlist[1]
    return price