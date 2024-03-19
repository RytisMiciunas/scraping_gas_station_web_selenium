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
And after that you will receive emails from 3 different browsers (chrome, firefox and edge).

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)