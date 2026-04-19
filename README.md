# LLM Watermark Detector

## What is this project?
This project demonstrates how watermarking works in 
Large Language Models (LLMs). It detects whether a 
given text contains a watermark signal based on the 
KGW research paper by Kirchenbauer et al. (2023).

## How does it work?
The core idea is simple — every word in the vocabulary 
is secretly split into a GREEN list and a RED list using 
a secret key and a threshold called gamma (default 0.5).

Watermarked text will have more green words than expected 
by chance. The detector counts green words and if the 
fraction exceeds gamma, the text is flagged as watermarked.

## How to run it?
```bash
pip install hashlib
python generate.py   # analyze a sentence word by word
python detect.py     # detect watermark in your own text
python evaluate.py   # run evaluation on multiple sentences
```

## What I learned
I learned how watermarking systems work at a fundamental 
level — how green/red lists are created using hashing, 
how gamma controls the detection threshold, and how the 
same secret key must be shared between generator and 
detector. This project is a small scale demonstration 
of concepts used in real LLM watermarking research.

## Reference
Kirchenbauer et al. (2023) — A Watermark for Large 
Language Models. https://arxiv.org/abs/2301.10226