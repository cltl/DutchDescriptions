# DutchDescriptions
Dutch descriptions for the Flickr30K validation data, plus a cross-lingual comparison tool.
This repository is part of [this paper](https://arxiv.org/abs/1707.01736), which
will be presented at [INLG 2017](https://eventos.citius.usc.es/inlg2017/index).

Here is a temporary BibTeX entry, which will be updated when the paper has been
included in the ACL anthology.

```
@unpublished{miltenburg2017cross,
	Author = {Emiel van Miltenburg and Desmond Elliott and Piek Vossen},
	Note = {Paper accepted at INLG 2017, \url{https://arxiv.org/abs/1707.01736}},
	Title = {Cross-linguistic differences and similarities in image descriptions},
	Year = {2017}}
```

## Folder structure

* `Crowdsourcing` Contains the data used as *input* for the crowdsourcing task.
* `Data` Contains all the image description data, including the newly collected Dutch data.
* `InspectionTool` Contains code and data for the inspection tool.
* `Stats` Contains scripts to generate statistics about the data, and the output of these scripts.
* `Utils` Contains a script to anonymize the data, and a script to generate Dutch validation files.


## Requirements

We used Python 3.6.1 with the following external libraries:

* Flask 0.1.2
* NLTK 3.2.2
* Numpy 1.12.0
* Matplotlib 2.0.0
* Matplotlib-venn 0.11.5

## Notes

This repository does NOT contain the Flickr30K images. Please visit the
[Flickr30K website](http://shannon.cs.illinois.edu/DenotationGraph/) and fill in
the form to obtain the images.
