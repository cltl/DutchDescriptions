import csv
import matplotlib.pyplot as plt
# pip install matplotlib-venn
from matplotlib_venn import venn3


with open('./ethnicity.csv') as f:
    reader = csv.DictReader(f)
    entries = list(reader)

images_per_language = {'dutch': set(), 'german': set(), 'english': set()}

for entry in entries:
    language = entry['language']
    flickr_id = entry['flickr_id']
    images_per_language[language].add(flickr_id)

diagram = venn3([images_per_language['dutch'],
                 images_per_language['german'],
                 images_per_language['english']],
                 ['Dutch','German','English'])

for patch in diagram.patches:
    patch.set_facecolor('white')
    patch.set_linewidth(1)
    patch.set_edgecolor('black')
    patch.set_alpha(1.0)

for label in diagram.set_labels:
    label.set_size(20)

for label in diagram.subset_labels:
    label.set_size(20)

# Minor tweaks
label_12 = diagram.subset_labels[2]
x,y = label_12.get_position()
label_12.set_y(y+0.03)
label_12.set_x(x+0.02)

label_11 = diagram.subset_labels[4]
x,y = label_11.get_position()
#label_11.set_x(x-0.025)
label_11.set_y(y-0.07)

plt.savefig('ethnicity.pdf')
