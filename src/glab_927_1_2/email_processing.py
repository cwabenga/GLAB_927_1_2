import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def run_assignment():
    # =========================================================================
    # Task 1 | Import libraries and configure the application
    # =========================================================================
    print("=================================================================")
    print(f"NLTK Version: {nltk.__version__}")
    print("=================================================================\n")
    
    # Secure required tokenizers and lexical databases
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)
    nltk.download("wordnet", quiet=True)
    nltk.download("omw-1.4", quiet=True)

    # =========================================================================
    # Task 2 | Implement stemming
    # =========================================================================
    email_content = (
        "Our team will be working on the upcoming "
        "project deadlines. Please ensure that all "
        "deliverables are submitted before the end "
        "of the week."
    )
    
    stemmer = PorterStemmer()
    tokens_stem = word_tokenize(email_content.lower())
    stems = [stemmer.stem(token) for token in tokens_stem]
    reconstructed_stem = " ".join(stems)
    
    print("TASK 2: STEMMING")
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
    
    lemmatizer = WordNetLemmatizer()
    tokens_lemma = word_tokenize(email_content_lemma.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens_lemma]
    reconstructed_lemma = " ".join(lemmas)
    
    print("TASK 3: LEMMATIZATION")
    print(f"Original Email: {email_content_lemma}")
    print(f"Lemmatized Email: {reconstructed_lemma}\n")

    # =========================================================================
    # Task 4 | Compare stemming and lemmatization
    # =========================================================================
    words = ["running", "studies", "working", "children", "connections"]
    
    print("TASK 4: COMPARISON")
    print(f"{'Original Word':<15} | {'Stemmed (Porter)':<18} | {'Lemmatized (Noun)':<20} | {'Lemmatized (Verb)':<20}")
    print("-" * 80)
    for word in words:
        stemmed_w = stemmer.stem(word)
        lemmed_noun = lemmatizer.lemmatize(word, pos="n")
        lemmed_verb = lemmatizer.lemmatize(word, pos="v")
        print(f"{word:<15} | {stemmed_w:<18} | {lemmed_noun:<20} | {lemmed_verb:<20}")
    print("=================================================================")

if __name__ == "__main__":
    run_assignment()
