"""
This script produces the input rows for Crowdflower.
"""

import glob
import csv

with open('../Data/splits/val_images.txt') as f:
    val = set(line.strip() for line in f)

with open('../Data/splits/test_images.txt') as f:
    test = set(line.strip() for line in f)

selection = val | test

url = 'http://kyoto.let.vu.nl/~miltenburg/flickr30K_images/'

with open('rows.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['key','url'])
    writer.writerows([[image[:-4], url + image] for image in selection])
