# Per Scholas NLP Development Portfolio
## Active Labs: GLAB 927.1.2, GLAB 927.2.1, and GLAB 927.4.1

This unified repository tracks advanced text manipulation pipelines, grammatical token tagging arrays, and sentiment opinion modeling engines within a single, isolated `uv` virtual environment framework.

## Core Language & NLP Concepts
* **NLTK:** The Natural Language Toolkit suite providing streamlined interfaces to lexical databases and text transformation workflows.
* **Tokenization:** The process of parsing a raw text string and slicing it into discrete units like individual words or punctuation marks.
* **Stemming:** A crude, algorithmic heuristic that chops off character suffixes to resolve a word back to a base linguistic trunk.
* **Lemmatization:** A morphology-based database engine that checks structured lookup charts to resolve terms back to their valid dictionary bases.
* **Part-of-Speech (POS) Tagging:** Assigning grammatical categories (like nouns, verbs, or adjectives) to individual words based on their context.
* **Named Entity Recognition (NER):** A classification technique that identifies and extracts real-world entities like people, organizations, and geographic locations from text data.
* **Sentiment Analysis:** An NLP technique used to analyze the emotional tone (polarity) and opinion bias (subjectivity) from textual data using Python's TextBlob library.

## Setup & Execution Instructions

To execute any specific text analysis pipeline matrix system, ensure your terminal is anchored in the root repository folder and run the targeted command blocks:

```bash
# Sync package environment dependencies
uv sync

# Run Lab 927.1.2: Stemming and Lemmatization
uv run python src/glab_927_1_2/email_processing.py

# Run Lab 927.2.1: Part-of-Speech (POS) & Named Entity Recognition (NER)
uv run python src/glab_927_1_2/text_analysis.py

# Run Lab 927.4.1: TextBlob Sentiment Analysis Mapping
uv run python src/glab_927_1_2/sentiment_analysis.py
```

---

## 📑 Lab 927.1.2: Task 4 Reflection Questions

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

---

## 📊 Lab 927.2.1: Business NLP Quick Reference Appendix

When processing text data for business analytics, understanding part-of-speech (POS) and entity tags helps automate tracking. Here is a breakdown of the key markers observed in our business document:

### 🧩 Grammatical POS Tags
* **NNP (Proper Noun, Singular):** Identifies specific names, companies, or brands (e.g., *Acme*, *Corp*, *Jane*, *Doe*). Essential for isolating specific business actors.
* **VBD (Verb, Past Tense):** Identifies completed actions or historical metrics (e.g., *highlighted*, *reported*, *mentioned*). Helpful for tracking logged events.
* **VBG (Verb, Gerund/Present Participle):** Identifies ongoing actions or workflows (e.g., *working*, *shipping*). Crucial for monitoring real-time pipelines.
* **NNS (Noun, Plural):** Identifies plural subjects or products (e.g., *issues*, *customers*, *delays*, *plans*, *concerns*).

### 🏷️ Named Entity Recognition (NER) Classifications
* **ORGANIZATION:** Clusters associated corporate identities together (e.g., *Acme Corp*). Used to automate competitive intelligence or client sorting.
* **GPE (Geo-Political Entity):** Identifies physical geographic operational territories, states, or cities (e.g., *New York*, *San Francisco*). Used to map shipping and regional demand.
* **PERSON:** Extracts distinct individual names (e.g., *Jane Doe*). Used to automatically map leadership roles or account executives to specific files.

---

## 📈 Lab 927.4.1: Sentiment Analysis Insights

Using `TextBlob`, customer feedback was parsed across two major scalar metrics to derive actionable business insights:

* **Polarity (-1.0 to 1.0):** Measures the emotional direction of the feedback. Positive reviews (e.g., *"updates to the support portal are amazing"*) scored high polarity, allowing automated sorting of happy customers. Negative remarks (e.g., *"interface is completely confusing"*) dropped below zero, instantly flagging accounts that need customer service intervention.
* **Subjectivity (0.0 to 1.0):** Measures how opinion-biased vs. factual a statement is. Comments tracking pure system actions (e.g., *"The platform received security updates yesterday"*) scored near `0.0` (objective), while highly emotional venting scored near `1.0` (subjective). This allows a business pipeline to separate factual bug logs from emotional user expressions.

---

## 🏁 Summary Findings & Discoveries
Through these consecutive labs, I learned how to build isolated runtime workspaces with `uv` project patterns. Working through these workflows made the trade offs of NLP models immediately clear: rule-based stemming offers computational speed, contextual lemmatization preserves dictionary forms, grammatical POS sequences expose textual syntax structure, and TextBlob's polarity and subjectivity metrics reliably translate qualitative customer feedback data into actionable business strategies.

