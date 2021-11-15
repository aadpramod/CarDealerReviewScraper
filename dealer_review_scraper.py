import requests
from bs4 import BeautifulSoup
from bs4.element import Tag, Comment
from textblob import TextBlob
import math
from functools import cmp_to_key

from textblob.sentiments import NaiveBayesAnalyzer

SENTIMENT_ANALYZER = NaiveBayesAnalyzer()

NUM_PAGES = 5

class ReviewInfo():
    def __init__(self):
        self._username = None
        self._review = None
        self._sentiment = 0
        self._star_rating = 0

    # SETTERS
    def set_star_rating(self, star_rating):
        self._star_rating = star_rating

    def set_sentiment(self, sentiment):
        self._sentiment = sentiment

    def set_username(self, username):
        self._username = username

    def set_review(self, review):
        self._review = review

    # GETTERS
    def get_star_rating(self):
        return self._star_rating

    def get_username(self):
        return self._username

    def get_sentiment(self):
        return self._sentiment

    def get_review(self):
        return self._review

    def print_data(self):
        print('USER: {} \n Star Rating:{} Sentiment Rating:{} \n "Mesage:{}'.format(self._username,
                                                                                    self.get_star_rating(),
                                                                                    self.get_sentiment(),
                                                                                    self.get_review()))

#comparator that first sorts by star rating and then by sentiment values since that has more precision
def compare(review1, review2):
    if review1.get_star_rating() > review2.get_star_rating():
        return -1
    elif review1.get_star_rating() < review2.get_star_rating():
        return 1
    else:
        if review1.get_sentiment() > review2.get_sentiment():
            return -1
        else:
            return 1


def analyze_sentiment(text):
    review_sentiment = TextBlob(text, analyzer=SENTIMENT_ANALYZER).sentiment
    return review_sentiment.p_pos - review_sentiment.p_neg


def get_reviews():
    users = []
    count = 0
    review_number = 0
    for page in range(1, NUM_PAGES + 1):
        res = requests.get(
            'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page{}/?filter=#link'.format(
                str(page)))

        soup = BeautifulSoup(res.content, 'html.parser')

        # the first class is to find the star rating, second is for actual review and other details
        for data in soup.findAll('div', {
            'class': ['col-xs-12 col-sm-3 pad-left-none text-center review-date margin-bottom-md',
                      'col-xs-12 col-sm-9 pad-none review-wrapper']}):
            count += 1
            review_number = math.ceil(count / 2)
            # odd values indicate its the star rating div
            if count % 2 == 1:
                star_rating = data.select('div[class*="rating-static hidden-xs"]')
                if star_rating is not None and len(star_rating) > 0:
                    star_rating = str(star_rating[0])
                    star_rating = star_rating.split('hidden-xs')[1]
                    num_star_rating = int(star_rating.split()[0].split('-')[1])
                    num_stars = num_star_rating / 10
                    users.append(ReviewInfo())
                    users[review_number - 1].set_star_rating(num_stars)
            # even values indicate its the review wrapper
            else:
                user_data = data.select('span[class="italic font-18 black notranslate"]')[0].text
                username = user_data.split('-')[1].strip()
                review_str = data.select('p[class*="review-content"]')[0].text
                user = users[review_number - 1]
                user.set_username(username)
                user.set_sentiment(analyze_sentiment(review_str))
                user.set_review(review_str)

    #Sort reviews in appropriate range based on sentiment to determine most extreme reviews
    sorted_users = sorted(users, key=cmp_to_key(compare))
    print("The three most extreme positive reviews are as follows: \n")
    for most_positive in range(3):
        sorted_users[most_positive].print_data()


if __name__ == "__main__":
    get_reviews()
