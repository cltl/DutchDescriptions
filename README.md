# DutchDescriptions
Dutch descriptions for the Flickr30K validation data, plus a cross-lingual comparison tool.
This repository is part of the following paper, which will be presented at
[INLG 2017](https://eventos.citius.usc.es/inlg2017/index):

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

## Notes

This repository does NOT contain the Flickr30K images. Please visit the
[Flickr30K website](http://shannon.cs.illinois.edu/DenotationGraph/) and fill in
the form to obtain the images.
