# KRINN
This module helps you in getting the price or title of a product by  simply using a URL or a Product ID. A product ID is available in the link itself.

## Installation
Run the following to install:

```python
pip install krinn
```

## Please Note
For now crawling of products like book or multiple product based on size are not supported.

## Usage

### shorten the url
```python
from krinn import amazon

shorturl = amazon.short("https://www.amazon.in/Zebronics-100HB-High-Speed-Port/dp/B07GLNJC25/ref=sr_1_1_sspa?keywords=usb+hub&qid=1583729190&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExRzg4NTU3SFFCNk5JJmVuY3J5cHRlZElkPUEwODY2NTY4MkxDUUpOVlBPUks4QyZlbmNyeXB0ZWRBZElkPUEwNzk1MjU3NEZUNVJJNkdGVzYwJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
print("Short URL:",shorturl)
```
Output:
```
Short URL: https://www.amazon.in/dp/B07GLNJC25/
```
### Get the id using link
The ID of the product is in the url itself. To get the id of the link use this function.

```python
from krinn import amazon

product_id = amazon.getid("https://www.amazon.in/Zebronics-100HB-High-Speed-Port/dp/B07GLNJC25/ref=sr_1_1_sspa?keywords=usb+hub&qid=1583729190&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExRzg4NTU3SFFCNk5JJmVuY3J5cHRlZElkPUEwODY2NTY4MkxDUUpOVlBPUks4QyZlbmNyeXB0ZWRBZElkPUEwNzk1MjU3NEZUNVJJNkdGVzYwJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
print("Product ID:",product_id)
```
Output:
```
Product ID: B07GLNJC25
```
### crawl by id

```python
from krinn import amazon

byid = amazon.crawlbyid("B07GLNJC25")
print("By ID: ",byid)
```
Output:
```
By ID:  ['Zebronics ZEB-100HB USB hubs with 4 Ports', 340.0]
```
### crawl by url
```python
from krinn import amazon

url = "https://www.amazon.in/dp/B07GLNJC25/"

byurl = amazon.crawlbyurl(url)
print("\nBy URL: ",byurl)
```
Output:
```
By URL:  ['Zebronics ZEB-100HB USB hubs with 4 Ports', 340.0]
```
### get title of the product
```python
from krinn import amazon

url = "https://www.amazon.in/dp/B07GLNJC25/"

title = amazon.producttitle(url)
print("\nTitle:",title)
```
Output:
```
Title: Zebronics ZEB-100HB USB hubs with 4 Ports
```
### get price of the product
```python
from krinn import amazon

url = "https://www.amazon.in/dp/B07GLNJC25/"

price = amazon.productprice(url)
print("\nPrice:",price)
```
Output:
```
Price: 340.0
```
## Upcoming Features
- Number of Rating of the current product.
- How many stars out of 5.
- And many more.
