import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

print(f"NLTK Version: {nltk.__version__}")

# Download the required setup data files
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

print("Environment configured! Ready for text processing.")
# =========================================================================
# Task 2 | Implement stemming
# =========================================================================
email_content = (
    "Our team will be working on the upcoming "
    "project deadlines. Please ensure that all "
    "deliverables are submitted before the end "
    "of the week."
)

# 1. Instantiate the PorterStemmer tool
stemmer = PorterStemmer()

# 2. Normalize the text to lowercase and tokenize it (slice into words)
tokens_stem = word_tokenize(email_content.lower())

# 3. Stem each word in a loop
stems = [stemmer.stem(token) for token in tokens_stem]

# 4. Reconstruct the stemmed words back into a sentence string
reconstructed_stem = " ".join(stems)

# 5. Print the output exactly as required by the assignment structure
print("\nTASK 2: STEMMING")
print(f"Original Email: {email_content}")
print(f"Stemmed Email: {reconstructed_stem}\n")
# =========================================================================
# Task 3 | Apply lemmatization
# =========================================================================
email_content_lemma = (
    "The team members are working on their "
    "tasks diligently. Please ensure that "
    "every report is submitted promptly."
)

# 1. Instantiate the WordNetLemmatizer tool
lemmatizer = WordNetLemmatizer()

# 2. Normalize the text to lowercase and tokenize it (slice into words)
tokens_lemma = word_tokenize(email_content_lemma.lower())

# 3. Lemmatize each word (using default noun behavior)
lemmas = [lemmatizer.lemmatize(token) for token in tokens_lemma]

# 4. Reconstruct the lemmatized words back into a sentence string
reconstructed_lemma = " ".join(lemmas)

# 5. Print the output exactly as required by the assignment structure
print("TASK 3: LEMMATIZATION")
print(f"Original Email: {email_content_lemma}")
print(f"Lemmatized Email: {reconstructed_lemma}\n")
