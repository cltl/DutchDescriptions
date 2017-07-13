"""
Flask website to inspect image descriptions in three different languages.

* Use `python compare_languages.py` to run the tool
* Open http://127.0.0.1:5001/ in a web browser.
"""

# Flask-related imports:
from flask import Flask, request, render_template

# Other imports go here:
from collections import Counter, defaultdict
from nltk.tokenize import sent_tokenize, word_tokenize
import csv
import glob
from string import ascii_lowercase
ascii_set = set(ascii_lowercase)

################################################################################
# Load data

with open('../Data/splits/val_images.txt') as f:
    val_keys = [line.strip().split('.')[0] for line in f]
    val_set = set(val_keys)

def val_dict(path):
    "Create a description dictionary for the validation data from the MMT task."
    filenames = glob.glob(path)
    descriptions = []
    for filename in filenames:
        with open(filename) as f:
            descriptions_for_file = [d.strip() for d in f]
            descriptions.append(descriptions_for_file)
    description_tuples = list(zip(*descriptions))
    return dict(zip(val_keys, description_tuples))

english_descriptions = val_dict('../Data/English/Val/val*')
german_descriptions = val_dict('../Data/German/Val/de_val*')
dutch_descriptions = val_dict('../Data/Dutch/Val/val*')

# All images:
image_dict = {key: '/static/images/'+ key +'.jpg' for key in val_keys}

image_list = sorted(val_keys)

max_index = len(image_list) -1

################################################################################
# Negation experiment

# From Van Miltenburg, Morante & Elliott (2016):
with open('../Data/English/Negations/final_annotations.tsv') as f:
    reader = csv.DictReader(f,delimiter='\t')
    ignore = {'False positive', 'Not a description/Meta'}
    descriptions_with_negations = [row['Sentence'] for row in reader
                                                    if not row['Category'] in ignore]

# Different datasets have different preprocessing steps. This function is a workaround
# to combat the effects of preprocessing.
def only_ascii(description):
    "Reduce description to only contain lowercase ascii."
    chars = [char for char in description.lower() if char in ascii_set]
    return ''.join(chars)

# Get neg keys:
neg_hash = {only_ascii(d) for d in descriptions_with_negations}
neg_keys = {key for key, desc_tuple in english_descriptions.items()
                for desc in desc_tuple
                if only_ascii(desc) in neg_hash}

print(len(neg_keys), "keys corresponding to images with negations.")

# image_list = sorted(neg_keys)

################################################################################
# Set up general functions

def index_for_key(key):
    "Function that returns the index of an image in the image list for a given key."
    try:
        return image_list.index(key)
    except ValueError:
        return None

################################################################################
# Set up app:
app = Flask(__name__)

################################################################################
# Webpage-related functions


@app.route('/', methods=['GET'])
def main_page():
    """
    Function to display the main page. This is the first thing you see when you
    load the website.
    """
    index = 0
    return image(index)

@app.route('/image/<n>')
def image(n):
    """
    Function to display the a specific image with its description.
    """
    # If the index is a regular index.
    if int(n) < len(image_list):
        index = int(n)
    # Else redirect to the first one.
    else:
        index = 0
    key = image_list[index]
    # Return the relevant data:
    return render_template("index.html",
                            key=key,
                            img=image_dict[key],
                            dutch=dutch_descriptions[key],
                            english=english_descriptions[key],
                            german=german_descriptions[key],
                            index=index,
                            max_index=max_index)

def search_descriptions(query, d):
    query = query.lower()
    return {key for key, descriptions in d.items()
                for description in descriptions
                if query in description.lower()}

@app.route('/image_by_id/<identifier>')
def image_by_id(identifier):
    """
    Function to display the main page. This is the first thing you see when you
    load the website.
    """
    try:
        index = image_list.index(identifier)
    # If the identifier isn't actually in the list.
    except ValueError:
        index = 0
    return image(index)


search_term = ''
result_list = sorted(val_keys)
max_result_index = len(result_list) - 1

@app.route('/results/<n>', methods=['GET', 'POST'])
def results(n):
    """
    Function to display the a specific image within the search results.
    """
    if request.method == 'POST':
        query = request.form['query']
        print(query)
        global search_term
        global result_list
        global max_result_index
        search_term = query
        result_list = sorted(set.union(search_descriptions(query, dutch_descriptions) & val_set,
                                        search_descriptions(query, english_descriptions),
                                        search_descriptions(query, german_descriptions)))
        max_result_index = len(result_list) - 1
    # If the index is a regular index.
    if int(n) < len(result_list):
        index = int(n)
    # Else redirect to the first one.
    else:
        index = 0
    try:
        key = result_list[index]
    except IndexError:
        key=image_list[0]
    # Return the relevant data:
    return render_template("result_index.html",
                            key=key,
                            img=image_dict[key],
                            dutch=dutch_descriptions[key],
                            english=english_descriptions[key],
                            german=german_descriptions[key],
                            index=index,
                            max_index=max_result_index,
                            query=search_term,
                            num_results=len(result_list))


################################################################################
# Running the website

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
