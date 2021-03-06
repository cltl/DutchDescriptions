"""
This script creates the Dutch validation files in the same format as the English
and German descriptions.
"""

import csv
from collections import defaultdict

# Load file from the first crowdsourcing job.
with open('../Data/Dutch/Raw/crowdflower1-annotated-anonymized.csv') as f:
    reader = csv.DictReader(f)
    entries = list(reader)

# Load file from the second crowdsourcing job.
with open('../Data/Dutch/Raw/crowdflower2-annotated-anonymized.csv') as f:
    reader = csv.DictReader(f)
    entries += list(reader)

# Let's split the set of entries.
tainted = [e for e in entries if not e['sentence_category'] == 'OK']
kept = [e for e in entries if e['sentence_category'] == 'OK']

with open('../Data/splits/test_images.txt') as f:
    keys = [line.split('.')[0] for line in f]

key_set = set(keys)

validation_set = [e for e in kept if e['key'] in key_set]

val_descriptions = defaultdict(list)
for e in validation_set:
    description = e['beschrijf_de_afbeelding_in_n_volledige_maar_eenvoudige_zin'] + '\n'
    flickr_id = e['key']
    val_descriptions[flickr_id].append(description)

sorted_descriptions = [val_descriptions[key] for key in keys]
d1,d2,d3,d4,d5 = zip(*sorted_descriptions)

for i, descriptions in enumerate([d1,d2,d3,d4,d5]):
    with open('../Data/Dutch/Test/test.' + str(i), 'w') as f:
        f.writelines(descriptions)
