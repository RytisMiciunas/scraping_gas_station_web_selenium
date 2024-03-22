# Selenium-Powered Gas Price Scrapper: Get the Best Deals Straight to Gmail

This script automates the process of scraping gas prices from gas stations' located in Vilnius. The information is taken from https://gas.didnt.work/ website using Selenium, selecting the cheapest options, and then sending the information via Gmail. It provides a convenient way to stay updated on the best gas deals without manually checking each station's prices.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt

```bash
pip install -r requirements.txt
```

## Usage
Simply go to "Constans" folder, open "where_to_send.py" file and change email where you want to receive mail.
```python
EMAIL_TO_RECIVE_INFO = "expectumpatronum5@gmail.com"
```
Or run pass email through console like this: 
```bash
python ./main.py your@email.com
```


And after that you will receive emails from 3 different browsers (chrome, firefox and edge).

You can see the example of letter here: 


![alt text](https://live.staticflickr.com/65535/53597627604_6bbd0c3484_n.jpg)


