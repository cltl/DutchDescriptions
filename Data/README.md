# Language data

This folder contains image description data for three languages: Dutch, English,
and German.

* The `English` and `German` folders contain Flickr30K training, validation, and
test data, coming from the [WMT 16 Multimodal Translation](http://www.statmt.org/wmt16/multimodal-task.html)
Task 2: Crosslingual Image Description Generation.

* In addition, the `English` folder contains annotations for non-affixal negation,
from Van Miltenburg et al. (2016, [GitHub](https://github.com/evanmiltenburg/annotating-negations/)).

* The `Dutch` folder contains the (anonymized) Dutch crowdsourcing data along with
validation and test files, in the same format as the English and German data.

* The `splits` folder contains files indicating how the Flickr30K images are split
into `train`, `val`, and `test` splits. The descriptions in the Train, Val, and Test
files follow the same order as these splits.
