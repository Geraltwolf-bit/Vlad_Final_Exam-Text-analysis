from collections import Counter
import string
translator = str.maketrans('', '', string.punctuation)

reviews = [
    "I liked the movie very much! High quality work.",
    "The plot is predictable and boring. Dislike.",
    "Cool movie with fantastic performance. Recommend it very much!",
    "Don't waste your time. Bad actor play, the story is bland.",
    "Beautiful story. Very emotional. A must watch movie!",
]

#find positive and negative reviews:
pos_words = ['liked', 'good', 'beautiful', 'cool', 'emotional']
neg_words = ['dislike', 'bad', 'predictable', 'boring']

positive_reviews = []
negative_reviews = []

for pos_line in reviews:
  for w in pos_line.lower().split():
    if w in pos_words:
      positive_reviews.append(pos_line)

for neg_line in reviews:
  for w1 in neg_line.lower().split():
    if w1 in neg_words:
      negative_reviews.append(neg_line)

#find unique words:
unique_words = []
for line in reviews:
  for word in line.translate(translator).lower().split():
    if word not in unique_words:
      unique_words.append(word)

#sort reviews:
reviews_sorted = sorted(reviews, key = len)

#the number of occurences of each word:
words_list = []
for line in reviews:
  for w in line.translate(translator).lower().split():
    words_list.append(w)

word_occurence = Counter(words_list)
word_occurence_dict = dict(word_occurence)

print("Number of reviews:", len(reviews))
print("\nPositive reviews:")
print(positive_reviews)
print("\nNegative reviews:")
print(negative_reviews)
print("\nUnique words:")
print(unique_words)
print("\nReviews sorted:")
print(reviews_sorted)
print("\nWord occurences:")
print(word_occurence_dict)