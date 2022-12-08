# Tag-based Audio Generation

## Description

Model to generate audio given input genre(s), mood(s), and instrument(s)

## Link to demo app

[Google Colab Notebook](https://colab.research.google.com/drive/17G45yw0ZzsD84X-Q3RHPy6ER9Pb-u6hK)

## Youtube Video demo

[YouTube Demo](https://youtu.be/cZIcJ5TRCmA)

## System Architecture Diagram

![System Architecture Diagram](./assets/system_architecture.png)

### Explanation

User inputs a genre tag into frontend. This tag is passed to semantic similarity NLP model to determine nearest tag within training space, and implicitly coerces to (outputs) the found tag This tag is passed to the audio generation model as input, which produces generated audio which is playable on the frontend.

## Model Architecture Diagrams

TODO: NLP model diagram

TODO: Audio generation model diagram

## Directory Guide

TODO

## Training Instructions

TODO

## Testing Instructions

TODO

## Citations and References

TODO
