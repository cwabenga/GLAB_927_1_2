 # GLAB 927.1.2: Hands-On Text Processing for Email Management with Python

An official Per Scholas assignment demonstrating text preprocessing pipelines using the Natural Language Toolkit (NLTK) and the `uv` virtual environment package ecosystem.

## Core Linguistic Concepts

* **NLTK:** The Natural Language Toolkit suite providing streamlined interfaces to lexical databases and text transformation workflows.
* **Tokenization:** The process of parsing a raw text string and slicing it into discrete units like individual words or punctuation marks.
* **Stemming:** A crude, algorithmic heuristic that chops off character suffixes to resolve a word back to a base linguistic trunk.
* **Lemmatization:** A morphology-based database engine that checks structured lookup charts to resolve terms back to their valid dictionary bases.

## Setup & Execution Instructions

To mirror this project container and execute the text analysis pipeline, run the following blocks in your Mac terminal from the project root:

```bash
uv sync
uv run python src/glab_927_1_2/email_processing.py
```

## Task 4 Reflection Questions

### 1. What is the difference between stemming and lemmatization?

Stemming uses blind, rule-based character slicing to chop suffixes off words without checking for vocabulary validity or sentence context. Lemmatization uses complex morphological rules and dictionary lookup catalogs to map words back to their actual base forms based on the sentence structure.

### 2. Which technique is more likely to return dictionary forms? Give a concrete example.

Lemmatization is significantly more likely to return a real dictionary word. For example, when processing the word **"studies"**, the Porter Stemmer may chop characters to return `studi`, whereas the lemmatizer can match it against its database to return the dictionary noun base `study`.

### 3. How could stemming support search or matching in business emails?

Stemming groups together different variations of a word (like "deliverables", "delivered", and "delivering") by reducing them to a common base string (`deliver`). This allows an email search engine to surface related threads even if the user searches for only one variation.

### 4. What benefit might lemmatization offer in a text-analysis pipeline?

Lemmatization reduces structural noise and text variation while producing valid dictionary forms. This can make tokens easier to interpret in downstream tasks such as sentiment analysis or text categorization.

### 5. How did the `pos` argument change a result?

The `pos` (part-of-speech) tag changes which dictionary form the lemmatizer considers. By default, the lemmatizer treats terms as nouns, which may leave verbs like **"working"** unchanged. Passing `pos="v"` selects the verb form and can resolve **"working"** and **"running"** to **"work"** and **"run"**, respectively.

## Summary Findings

Through this lab, I learned how to build isolated runtime workspaces with `uv` project patterns. The output tables demonstrated the tradeoffs between rule-based stemming and dictionary-backed lemmatization when building text-processing pipelines.
