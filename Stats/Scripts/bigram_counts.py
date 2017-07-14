from nltk import word_tokenize
from collections import Counter
import glob


def ngram_counts(path, language, n=2):
    "Count the "
    bigram_counter = Counter()
    for filename in glob.glob(path):
        with open(filename) as f:
            for line in f:
                lowercase = line.lower()
                tokens = word_tokenize(lowercase, language=language)
                bigram = ' '.join(tokens[:2])
                bigram_counter[bigram] += 1
    return bigram_counter


def print_counts(counts, language, n=5):
    "Print the top-n counts."
    print('----------------------')
    print(language)
    print('----------------------')
    for word, count in counts.most_common(n):
        print(word, '\t', count)
    print('----------------------')
    print()

dutch_counts = ngram_counts('../../Data/Dutch/Val/val*', language='dutch')
english_counts = ngram_counts('../../Data/English/Val/val*', language='english')
german_counts = ngram_counts('../../Data/German/Val/de_val*', language='german')


print_counts(dutch_counts, 'Dutch')
print_counts(english_counts, 'English')
print_counts(german_counts, 'German')
