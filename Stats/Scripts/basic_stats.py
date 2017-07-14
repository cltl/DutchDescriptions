from nltk import word_tokenize
import glob
from collections import Counter
from string import punctuation
from numpy import mean, std

punctuation_set = set(punctuation)

de_descriptions = glob.glob('../../Data/German/Val/de_val*')
en_descriptions = glob.glob('../../Data/English/Val/val*')
nl_descriptions = glob.glob('../../Data/Dutch/Val/val*')


def get_lines(filename):
    "Get the lines from a file."
    with open(filename) as f:
        for line in f:
            line = line.lower().strip()
            yield line


def generate_stats(filenames):
    "Generate stats for a list of filenames."
    num_tokens = []
    num_words = []
    num_chars = 0
    all_types = set()
    start_count = Counter()
    for fn in filenames:
        for line in get_lines(fn):
            tokens = word_tokenize(line)
            words = [tok for tok in tokens if not tok in punctuation_set]
            start = ' '.join(tokens[:2])
            num_tokens.append(len(tokens))
            num_words.append(len(words))
            num_chars += len(''.join(words))
            all_types.update(words)
            start_count[start] += 1
    print('Number of types:', len(all_types))
    print('Tokens per sentence:', mean(num_tokens), std(num_tokens))
    print('Words per sentence: ', mean(num_words), std(num_words))
    print('Avg word length: ', num_chars/sum(num_words))
    for w,c in start_count.most_common(10):
        print(w,'\t',c)

print("Dutch")
generate_stats(nl_descriptions)
print()

print("English")
generate_stats(en_descriptions)
print()

print("German")
generate_stats(de_descriptions)
print()
