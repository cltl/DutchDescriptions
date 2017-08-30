# Cross-linguistic differences and similarities in image descriptions
*Emiel van Miltenburg, Desmond Elliott, Piek Vossen*

**Presentation notes**: Emiel van Miltenburg

## Opening slide

This talk covers our paper on cross-linguistic differences and similarities in
image descriptions. So we will look at how people describe images, and we'll make
some generalizations about the things they say.

## Image descriptions

First off: what do we understand by image descriptions? Basically, these are just
one-sentence descriptions of a set of images, elicited from native speakers. You
don't have to read all of these descriptions, but the important thing to note is
that already, with one example, we see a lot of variation between speakers.

## Why describe images?

Why would we want to look at image descriptions? There are several reasons for
us to do so:

- Automatic image description is a key task in the intersection of computer vision
and natural language generation, in order to see whether a system can understand
the contents of an image. This is also the main context in which image description
corpora are used at the moment.
- We can use image description data to better understand human language. Especially
with respect to issues like reference (how do you relate language to the outside world?)
and pragmatics (how do we choose to talk about the world? What do our utterances convey?)
- A key motivation for studying the task of automatic image description is to aid
visually impaired people. We will not go into this motivation here, but it is important
to consider that you can't just have a system produce any description. We'll eventually
have to make choices about how we want the system to talk about the world.
- Image description is more generally relevant to human-computer interaction, because
eventually if we want to interact more naturally with machines, they will need to
understand the world around us. And vision is a very important modality to take into
account here.

We will focus on the cognitive, linguistic side of the story. That is: image understanding.

## Image understanding

Image description is not the only task to measure image understanding. There are
several others, with each task testing different aspects of image understanding.
We don't have time to go into the other tasks here (we can discuss them during the
Q&A), but just ask straight away: what about image description? What is that all about?

I would like to argue that image description is all about variation and perspective.
Let me explain with the next slide.

## A model

Here's a model of the image description task, as it is currently carried out using
crowdsourcing tasks. An image is presented to the speaker, who interprets this image,
and then produces a description for that image. The interpretation aspect is often
ignored, but it is crucial to the process. We will see that differences in perspective
lead to differences in the descriptions, i.e. variation.

## Sources of variation

Now there are several sources of variation. We provide a partial list in our paper,
with at least these six being important: background knowledge, cultural differences,
language differences, task design, audience, and demographic factors. We only study
the first three factors here.

The first three speak for themselves, but the next two require some additional
explanation. Task design is basically the set up of the crowdsourcing task. Basically
these are like psycholinguistic experiments, and you can bias participants to produce
other kinds of descriptions. (See e.g. last year's paper by Adriana Baltaretu and
Thiago Castro-Ferreira.) Audience is who or what the participants believe they are
describing the images for, and demographic factors again speaks for itself.

Since we are doing a corpus study, we cannot study the last three factors, as these
would require manipulating and controlling the crowdsourcing task.

## Data

The data for our study comes from Dutch, English, and German. The English descriptions
come from the Flickr30K data, German from the Multi30K data, and we collect the Dutch
descriptions ourselves. This means that we have parallel data, with the images as pivot.

## Collecting data

We collect data using a simple procedure. We show participants an image, and we
ask them to provide a short-but-complete description of the image. We use the same
procedure as the one used for Flickr30K and Multi30K.

## Dutch Descriptions

We collected Dutch descriptions for the validation and test sets of the Flickr30K data,
with 5 descriptions per image. This took 4 months, due to the size of the crowd. As you
can see, these people come from all over the Netherlands.

I should emphasize that this 4 month period really is an issue, because it means that
we cannot collect large datasets for small-pool crowdsourcing languages.

## Manual checking

Crowdsourcing in Dutch requires manual checking, because the crowdsourcing pool also
contains e.g. expats living in Amsterdam, who don't speak Dutch but use Google translate.

Here are two examples, that we found through visually inspecting these examples.
By looking at these ungrammatical sentences, you can usually guess what the original
descriptions must've been. So we verified this using Google Translate.

## Our study

So in our study, we take descriptions from three languages --Dutch, English, and
German-- and we compare these descriptions on the Flickr30K validation set. We don't
touch the test set.

## Phenomena

We will be looking at three phenomena: the use of negations, stereotypes in the data,
and familiarity effects. We leave aside the use of definite and indefinite articles.

## Methodology

Our methodology is simple: we visually inspect all the images to find examples of
each phenomenon. This is made easier by the search function, which we use to find
occurrences of specific strings. I'd be happy to give you a demo during the conference.

## Negations

Negations are words that are used to signal that something is *not* in an image.
This is interesting from a pragmatic point of view, because that typically means
that there is something unusual going on. Also note that this is a cognitively
complex process, that requires reasoning about an image and goes beyond 'mere'
description. In an earlier study, we present a taxonomy showing how negations
are used in English image descriptions.

In this study, we find that speakers in German as well as in Dutch use negations,
which suggests that, even though this is a rare phenomenon, the use of negations
is robust across languages. The German example shows a negation being used to refer
to something outside the image. The Dutch example shows the negation being used
for a remarkable event.

## Results

Here are the exact numbers, showing that negations are very infrequent (only 11
descriptions in Dutch). But still, they are there.

We also find that there is little overlap in their use. Instead of negations,
people may use all sorts of alternatives to signal, for example, that someone is
not wearing a shirt.

## Take-home message

So the take-home message from this is that the use of negations is a general phenomenon.
Moreover, searching for negations is an efficient way to find image description
examples that are cognitively complex, and that show you that reasoning about scenes
occurs in every language.

## Stereotypes

Here is a slide for some earlier work that I did, on the use of stereotypes in
the Flickr30K data. This is a particularly extreme example, but it gets the message
across: crowd workers really like to speculate about images.

Or perhaps they are just trying to be helpful, by being as informative as possible (c.f. Grice's maxims).
Whatever the reason, they often make what I would call "Unwarranted inferences."
That is, they go beyond the contents of an image, to provide speculative information.
This is immensely hard to detect, so right now all we can do is manually inspect all
the images.

## "Mothers"

Here are example images for a search I did in the Flickr30K data, looking for the
term "Mother". We see these kinds of examples pop up in Dutch, as well as in German.
Our paper contains one such example, and another extreme example from German, which
refers to two stewardesses as 'lesbians'. Of course this is an extreme case, but the
point is that it's almost impossible to detect these (sometimes abusive) cases.

## Stereotyping results

We found that stereotypes occur in all languages. And although some of them are
very hard to detect, social roles like 'mother' are easy. Most of those uses are
speculative.

But again, this is relative. Some descriptions are just highly likely to be true,
and we have to face the question: where to draw the line? For example, if someone
is breastfeeding a child, it is extremely likely that this person is also the mother.

## Take-home message

In sum, human annotations are subjective. And while this makes the descriptions
more specific, it also creates noise in terms of reliability. We cannot be sure
whether a label applies or not, if crowd-workers are speculating about the images.

## Bias

Here's a two line summary of the literature on bias in language:

    "The language we use reflects the way we perceive the world.
    People report things that are stand out to them, that are Other."

We also find bias in image descriptions. We will focus on the use of ethnicity/nationality
markers.

## Ethnicity

Here are some examples from the Flickr30K corpus. I've borrowed these slides from
my earlier work on stereotyping and bias. These descriptions do not just talk about
the people that are in the images, they also mark their ethnicity. Note how in the
last example, the white woman is simply called 'blonde'. No ethnicity or nationality,
except perhaps implicitly.

## Results

We found that speakers of all three languages use markers of nationality/ethnicity.
Some of these cases are fine (e.g. people in traditional clothing, like Scottish kilts).
But it's striking that 'White' is almost exclusively used for contrast. Otherwise,
white people are the unmarked default.

This isn't necessarily a Western thing, though. In Asian-language datasets (Chinese,
Japanese), we see the reverse: Asian is unmarked and Europeans are marked.

The question is: is this kind of behavior necessary? Is it useful? racist?
Should image description systems copy this behavior?

## Familiarity

The last phenomenon that I will cover is Familiarity. This hasn't been highlighted
before in the literature, but it's important to realize:

    "People can only be as specific as their knowledge allows them to.
    This leads to differences between languages/populations!"

We'll look at three examples.

The first example is this image. Can you guess where this was taken?
The Dutch crowd workers could. And incidentally, France is a popular holiday
destination for Dutch people. We got a perfect description of the location in Dutch.
And not just one Dutch person, but three crowd workers knew it was in Paris.
The American response is also interesting: the Washington monument. These locations are
similar enough that they're easily mistaken.

Moving on to the next image. Can you tell what is going on?
The US workers actually outperformed the others on two counts: they identified the
jersey as a Broncos outfit, and they described the activity as tailgating. I.e.
having a barbecue outside a sports stadium. This concept is unfamiliar to most Dutch
and German speakers.

The final example is close to my heart. Can you guess what this is?
This Amsterdam street organ was of course identified by the Dutch speakers, but not
at all by the English speakers, and only by some (2/5) German speakers.

## Take-home message

The take-home message is that NLG systems cannot just be translated, and image
description cannot be done by just anyone. The past three examples require background
knowledge in order to fully capture the image contents.

And so the question is: how can we tailor image descriptions to different audiences,
and integrate world knowledge into NLG systems?

## Limitations of this study

Now of course we have only scratched the surface of cross-linguistic differences
and similarities in image descriptions. We've only looked at Germanic languages!

Here's a nice negation example that I found in the Turkish tasviret corpus. Two dogs
are "unable to share" a toy. From this example speaks the expectation that it is normal
to share things.

I'm sure there are many other interesting differences between Germanic and other languages,
that can inform us about the relation between language and the outside world. And
so I encourage you to look beyond English, or beyond Germanic languages, to see what
we may find.

## Conclusion
In conclusion, I hope to have shown you that image descriptions are inherently
subjective, involve reasoning over the images, and depend on world knowledge.

An important open question that we may now ask is: what should we want NLG systems
to look like? Do we want them to also have these properties, or should we reconsider?
