from bs4 import BeautifulSoup
import requests
import codecs

import tweet  #other python file.

def imdbWebScrapping():
    nameofCelebrities = []  #defines an empty list
    celebrityKeyValue = {}  #defines an empty dict
    counter = 0

    BASE_URL = "http://m.imdb.com/feature/bornondate"

    r = requests.get(BASE_URL)  #getting url in r
    soup = BeautifulSoup(r.text, 'lxml')    #getting text content in soup

    boccat = soup.find("section", "posters list")   #finding posterlist data
    bornDate = boccat.findChild("h1").text

    celebrityNameList = []

    for i in boccat.findAll("a", "poster "):    #main loop for getting all name,img,profession...
        celebrityKeyValue[counter] = {}
        celebrityName = i.find("span", "title").text
        celebrityNameList.append(celebrityName)
        celebrityKeyValue[counter]["celebrityName"] = celebrityName

        # Celebrity's image link: "*.jpg"
        celebrityKeyValue[counter]["celebrityImg"] = i.img["src"]

        # Parsing Profession and the Best Movie
        profession, bestMovie = i.find("div", "detail").text.split(",")

        # Profession
        celebrityKeyValue[counter]["profession"] = profession

        # Best Movie
        celebrityKeyValue[counter]["bestMovie"] = bestMovie

        counter += 1

    return nameofCelebrities, celebrityKeyValue

if __name__ == '__main__':
    nameofCelebrities, celebrityKeyValue = imdbWebScrapping()   #calling the imdbWebscrapping() function

    celebrity = tweet.tweet()
    outputFile = codecs.open("finalOutput.txt", 'w', "utf-8")

    for i in range(10):
        celebrityName = celebrityKeyValue[i]["celebrityName"]
        celebrity.tweetSearch(celebrityName)    #searching for celebrity name on twitter

        celebrityKeyValue[i]["tSentiment"] = celebrity.tweetSentimentAnalysis()

        outputFile.write("Name of the celebrity: " + celebrityKeyValue[i]["celebrityName"] + "\n")
        outputFile.write("Celebrity Image: " + celebrityKeyValue[i]["celebrityImg"] + "\n")
        outputFile.write("Profession: " + celebrityKeyValue[i]["profession"] + "\n")
        outputFile.write("Best Work: " + celebrityKeyValue[i]["bestMovie"] + "\n")
        outputFile.write("Overall Sentiment on Twitter: " + celebrityKeyValue[i]["tSentiment"] + "\n")
        outputFile.write("\n\n")

    outputFile.close()