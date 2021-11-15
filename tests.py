from dealer_review_scraper import analyze_sentiment

BAD_REVIEW = 'Worst Dealership ever. I am never coming back here!'
NEUTRAL_REVIEW = 'they did the work, it was okay but not great'
GOOD_REVIEW = 'Great dealership. I will be back here soon!'
GREAT_REVIEW = 'I love this dealership, they are my favorite! I cannot imagine my life without them! Roberto was so ' \
                   'helpful and kind'

def bad_review_vs_good_review():

    bad_score = analyze_sentiment(BAD_REVIEW)
    good_score = analyze_sentiment(GOOD_REVIEW)
    assert(bad_score < good_score)

def bad_review_vs_neutral_review():
    bad_score = analyze_sentiment(BAD_REVIEW)
    neutral_score = analyze_sentiment(NEUTRAL_REVIEW)
    assert (bad_score < neutral_score)

def good_review_vs_neutral_review():
    good_score = analyze_sentiment(GOOD_REVIEW)
    neutral_score = analyze_sentiment(NEUTRAL_REVIEW)
    assert (good_score > neutral_score)

def great_review_vs_good_review():
    great_score = analyze_sentiment(GREAT_REVIEW)
    good_score = analyze_sentiment(GOOD_REVIEW)
    assert(great_score > good_score)

def empty_review():
    empty_review = ''
    empty_score = analyze_sentiment(empty_review)
    assert (empty_score == 0)

def run_tests():
    bad_review_vs_good_review()
    bad_review_vs_neutral_review()
    good_review_vs_neutral_review()
    great_review_vs_good_review()
    empty_review()


if __name__ == "__main__":
    run_tests()