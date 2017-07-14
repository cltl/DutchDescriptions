from nltk import word_tokenize
import glob
import csv

def verb_missing(bag_of_words):
    "Check if there's a verb communicating that something is missing."
    return {w for w in bag_of_words if w.startswith('mis') or   # missen
                                    w.startswith('ontbre') or   # ontbreken
                                    w.startswith('verzuim') or  # verzuimen
                                    w.startswith('manke')       # mankeren
                                    }


# Here's a set of Dutch words that are used to express negation.
dutch_negations = {"geen", "geenszins, ""niet", "nooit",
                   "nimmer", "nergens", "noch",
                   "niemand", "niets", "zonder",
                   "afwezig", "afwezige",
                   'generlei', 'nul',
                   'uitgezonderd', 'afgezien', 'behalve'}


def get_descriptions(filename):
    with open(filename) as f:
        return [line.strip() for line in f]


dutch_filenames = glob.glob('../../Data/Dutch/Val/val*')
dutch_descriptions = map(get_descriptions, dutch_filenames)


with open('../../Data/splits/val_images.txt') as f:
    images = [line.strip('.jpg\n') for line in f]

header = ['flickr_id', 'description', 'negations']
rows = []
for descriptions in dutch_descriptions:
    for flickr_id, description in zip(images, descriptions):
        bag_of_words = set(word_tokenize(description, language='dutch'))
        intersection = bag_of_words & dutch_negations
        neg_verbs = verb_missing(bag_of_words)
        if intersection or neg_verbs:
            row = [flickr_id, description, ' '.join(intersection|neg_verbs)]
            rows.append(row)

with open('../Output/dutch_negations.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
