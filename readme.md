# World Currencies 

## Web Programming with Python, JavaScript, ajax, html, Fixer.io API
## Data format: json

## access_key for the api is removed from the code file. When downloading from git, use your own access key. 

Following files are part of this project and their purpose:

##templates/index.html : This files is the homepage and displays the form with 3 sections:
- Get Exchange rate
- Get amount converted to the target currency
- Get historical rate

** All the rates are corresponding to base currency EUR ** 

## application.py
The flask application file having following routes:

/index: Displays the blank form index.html 

/convert: 
This route returns the exchange rate for the target currency by connecting to Fixer.io latest api.  It will return an error if the call to the api fails (status code not 200) or the json response doesn't contain the target currency rate or if there are any other access related issues. 

/getamount:
This route returns the converted amount in the target currency by providing the base amount in EUR. It retrieves the data from fixer.io convert api. It will return an error if the call to the api fails (status code not 200) or the json response doesn't contain the target currency amount or if there are any other access related issues. 

/historydata:
This route returns the historical rate of the target currency by providing the date for which the rate is needed. 
It retrieves data from fixer.io historical rate api. It will return an error if the call to the api fails (status code not 200) or the json response doesn't contain the target currency rate or if there are any other access related issues. 


## static/index.js
The javascript function that runs on DOM load. Three onsubmit events are handled for three different functions we disucssed above. All the three functions use the AJAX call (XMLHttpRequest) to connect to the server and javascript to modify the content of the DOM by displaying the result or the error. The result / error are returned in the json object from where they are extracted. 
