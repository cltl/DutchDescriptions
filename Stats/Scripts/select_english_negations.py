import csv
from collections import defaultdict

with open('./splits/val_images.txt') as f:
    images = {line.strip('.jpg\n') for line in f}

index = dict()
with open('./Flask-website/static/negations/flickr30K_negations.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    # This is an issue with duplicate keys, but there are no duplicates in the
    # descriptions with negations, so we can ignore this.
    for key, description in reader:
        index[description] = key

with open('./Flask-website/static/negations/final_annotations.tsv') as f:
    reader = csv.DictReader(f, delimiter='\t')
    entries = list(reader)

selection = []
for entry in entries:
    description = entry['Sentence']
    key = index[description]
    if key in images:
        entry['Key'] = key
        selection.append(entry)

with open('english_selection.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=selection[0].keys())
    writer.writeheader()
    writer.writerows(selection)
    
