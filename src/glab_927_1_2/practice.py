from nltk.tokenize import word_tokenize

email = "Hello team, please review the report!"
tokens = word_tokenize(email.lower())
print(tokens)
print("Number of tokens:", len(tokens))
