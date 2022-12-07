# Tag-based Audio Generation

## Description

Model to generate audio given input genre(s), mood(s), and instrument(s)

## Link to demo app

https://huggingface.co/spaces/SLAYEROFALL3050/Audio_Generator_Using_GAN

## Youtube Video demo

TODO

## System Architecture Diagram

![System Architecture Diagram](./assets/system_architecture.png)

### Explanation

User inputs one genre tag, mood tag, and instrument tag into frontend. Each tag is passed to semantic similarity NLP model to determine nearest tags within training space, and coerces to (outputs) found training space genre, mood, and instrument tag. Those tags are passed to the audio generation model as input, which produces generated audio which is playable on the frontend.

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
