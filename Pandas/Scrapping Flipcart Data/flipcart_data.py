import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []

Description = []
Reviews = []


for i in range(1, 5):
    
    url = f"https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
    r = requests.get(url)
    
    if r.status_code == 200: 
        soup = BeautifulSoup(r.text, "lxml")
        box = soup.find("div" , class_ = "DOjaWF gdgoEp")

        names = box.find_all("div", class_="KzDlHZ")
        
        for name_div in names:
            name = name_div.text
            Product_name.append(name)

        

        des = box.find_all( "ul" , class_ = "G4BRas")

        for des_div in des:
            des = des_div.text
            Description.append(des)

        rev = box.find_all("div" , class_ = "XQDdHH")

        for rev_div in rev:
            rev = rev_div.text
            Reviews.append(rev)

    else:
        print(f"Error fetching page {i}: {r.status_code}")

import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []

Description = []
Reviews = []


for i in range(1, 5):
    
    url = f"https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
    r = requests.get(url)
    
    if r.status_code == 200: 
        soup = BeautifulSoup(r.text, "lxml")
        box = soup.find("div" , class_ = "DOjaWF gdgoEp")

        names = box.find_all("div", class_="KzDlHZ")
        
        for name_div in names:
            name = name_div.text
            Product_name.append(name)

        

        des = box.find_all( "ul" , class_ = "G4BRas")

        for des_div in des:
            des = des_div.text
            Description.append(des)

        rev = box.find_all("div" , class_ = "XQDdHH")

        for rev_div in rev:
            rev = rev_div.text
            Reviews.append(rev)

    else:
        print(f"Error fetching page {i}: {r.status_code}")


d= {"Product_name":Product_name, "Description":Description , "Reviews" :Reviews  }
var = pd.DataFrame(d )
var.to_csv("flipcartdata.csv" )

































