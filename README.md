#Car Dealer Review Sentiment Analyzer
##Prompt:
Coding Challenge: “A Dealer For the People” <br>

The KGB has noticed a resurgence of overly excited reviews for a McKaig Chevrolet Buick, a dealership they have planted 
    in the United States. In order to avoid attracting unwanted attention, you’ve been enlisted to scrape reviews for 
    this dealership from DealerRater.com and uncover the top three worst offenders of these overly positive endorsements. <br>

Your mission, should you choose to accept it, is to write a tool that: <br>

1. scrapes the first five pages of reviews <br>
2. identifies the top three most “overly positive” endorsements (using criteria of your choosing, documented in the README) <br>
3. outputs these three reviews to the console, in order of severity <br>

## How to run
Before running anything, make sure your environment contains these required python packages <br>
* requests
* bs4(Beautiful Soup)
* textblob

After verifying said packages are installed, then run `python -m textblob.download_corpora` to download the NLTK corpora 
    used in the sentiment analysis <br>
Finally you can run the code simply by running `python dealer_review_scraper.py`

## Sentiment Analysis Logic
So I decided to start by utilizing the user star ratings. When people look at a review, they tend to look at the rating 
    score/stars first and as such I decided to sort based on the number of stars as a base. I realized that I was unable 
    to retrieve a value from the webpage, but after some digging ofund I could calculate the score by scraping the 
    corresponding text of the class of the star picture. <br>
After sorting by stars, I then use the textblob to analyze the review sentiment. this library is using an NLTK classifier 
    that is trained on a movie review corpus. I initally tried the default implementation of Textblob but found the NLTK 
    classifier implentation lined up with my expectations more. 

## Test Cases
I added a few test cases that I used to compare different sentiment analyzers.  



