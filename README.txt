Edureka Python Project Documentation

Problem Statement

IMDB provides a list of celebrities born on the current date. Below is the link: http://m.imdb.com/feature/bornondate

Get the list of these celebrities from this webpage using web scraping (the ones that are displayed i.e top 10). You have to extract the below information:

1.Name of the celebrity
2.Celebrity Image
3.Profession
4.Best Work

Once you have this list, run a sentiment analysis on twitter for each celebrity and finally the output should be in the below format

Name of the celebrity:
1.Celebrity Image:
2.Profession:
3.Best Work:
4.Overall Sentiment on Twitter: Positive, Negative or Neutral

Hint: Use IMDB scrapping sample example as reference for scraping the mentioned web page. For sentiment analysis use the Twitter sentiment code as reference.

Please Note That I Am Using Python 2.7

Tools and Packages Used :

•	Version: Python 2.7 •	Tweepy ? Tweepy is an open-sourced, hosted on GitHub, and enables Python to communicate with the Twitter platform and use its API. Here's the documentation.

•	Codecs ? The codecs module provides stream and file interfaces for transcoding data in your program. In this project I use the module for storing the tweets as Unicode text. Here's the documentation.

•	String (punctuation) ? To strip the tweets of all punctuations.

•	BeautifulSoup ? Beautiful Soup provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree using Python parsers like lxml and html5lib. It automatically converts incoming documents to Unicode and outgoing documents to UTF-8. Here's the documentation.

•	requests,OAuthHandler, punctuation.

Challenges Faced during the project :

•	appending the content and searching the content on the imdb website was tough at the beginning, I was unable to get the desired content for a long time and thet's why was quite frustrated at the beginning . 

•	tweet search was an easy part as compared to the imdb web scrapping.

•	Error message: TypeError: Can't convert 'bytes' object to str implicity was also an problem for some time as earlier I was using read_len to ascii then later used chunk_size to ascii.
