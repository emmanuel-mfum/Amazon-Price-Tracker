# Amazon-Price-Tracker
Python app that checks if the price of article is below a buying price and alert the user about it.

Given an article on Amazon (in this case a cooking pot), the program will send an email to the user if the price of that article goes below a threshold
set by the user, in our case 100.

To be able to scrape a web page from Amazon, we need provide the correcto information in the header then make a GET request using the Amazon link. 
Then, we need to extract the text from the response of the request and use it to make a BeautifulSoup object. We afterwards find the name of the article we are
eyeing as well as its price and extract the text out of the html tags holding them. We also convert the price froma string into a float.

We make a message using the information we extracted from the Amazon webpage and lastly check if the price we parse from Amazon is lower than the our buying price,
we use the SMTP module to send an email to the user to alert him about that fact.

This project necessiated the use of the BeautifulSoup module for webscraping and the SMTP module in order to send emails.
To run this program simply run the "main.py" and use your own email addresses.
