from nltk import word_tokenize
import glob
import csv

def verb_missing(bag_of_words):
    "Check if there's a verb communicating that something is missing."
    return {w for w in bag_of_words if w.startswith('fehl') or
                                       w.startswith('entgeh') or
                                       w.startswith('verfehl') or
                                       w.startswith('versäum') or
                                       w.startswith('vermiss') or
                                       w.startswith('verpass')}


# Here's a set of German words that are used to express negation.
german_negations = {'nicht', 'nichts',
                    'kein', 'keine', 'keinen', 'keines', 'keiner', 'keinem',
                    'sondern', 'noch', 'ohne', 'außer', 'ausser', 'sonder',
                    'niemand', 'niemanden', 'niemandes', 'niemandem', 'niemals',
                    'nie', 'nirgendwo', 'nirgends', 'nirgendswo', 'nirgendwohin',
                    'nirgendhin', 'nirgendshin', 'nirgendwoher', 'nirgendher',
                    'nirgendsher',
                    'vermisst', 'fehlend','verschwunden','verschollen'}


def get_descriptions(filename):
    with open(filename) as f:
        return [line.strip() for line in f]


german_filenames = glob.glob('./Flask-website/static/mmt_task2/de/val/de_val.*')
german_descriptions = map(get_descriptions, german_filenames)


with open('./splits/val_images.txt') as f:
    images = [line.strip('.jpg\n') for line in f]

header = ['flickr_id', 'description', 'negations']
rows = []
for descriptions in german_descriptions:
    for flickr_id, description in zip(images, descriptions):
        bag_of_words = set(word_tokenize(description, language='german'))
        intersection = bag_of_words & german_negations
        neg_verbs = verb_missing(bag_of_words)
        if intersection or neg_verbs:
            row = [flickr_id, description, ' '.join(intersection|neg_verbs)]
            rows.append(row)

with open('german_negations.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
