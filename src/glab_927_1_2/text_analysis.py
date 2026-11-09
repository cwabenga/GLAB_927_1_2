import nltk

# =========================================================================
# Setup Setup: Download Mandatory NLTK Resources
# =========================================================================
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('punkt_tab', quiet=True)  # Essential fallback safety mapping

# Raw Business Context Target Document String
business_document = """
The recent feedback from Acme Corp highlighted issues with the new model of the Omega widget.
Customers from New York and San Francisco have reported delays in shipping.
The CEO of Acme Corp, Jane Doe, mentioned plans to address these concerns by Q3.
"""

# Slicing the continuous character wall down into structured word string fragments
tokens = nltk.word_tokenize(business_document)

# Generating structural grammar parts-of-speech mappings for the tokens array
pos_tags = nltk.pos_tag(tokens)

# Executing the maximum entropy entity chunker tool tree pipeline
ner_result = nltk.ne_chunk(pos_tags)


# =========================================================================
# Task 1: Named Entity Recognition (NER) - Extract Business Entities
# =========================================================================
print("=================================================================")
print("TASK 1: NAMED ENTITY EXTRACTION")
print("=================================================================")
for entity in ner_result:
	# If the token object is wrapped as an NLTK sub-tree, it represents an Entity
	if isinstance(entity, nltk.Tree):
		entity_text = " ".join([word for word, tag in entity.leaves()])
		print(f"Extracted Entity: {entity_text}")


# =========================================================================
# Task 2: Named Entity Recognition (NER) - Print Entity Categories
# =========================================================================
print("\n=================================================================")
print("TASK 2: ENTITY CATEGORIZATION ANALYSIS")
print("=================================================================")
for entity in ner_result:
	if isinstance(entity, nltk.Tree):
		entity_text = " ".join([word for word, tag in entity.leaves()])
		# Pulling the root structural category label string assigned to the sub-tree
		entity_category = entity.label()
		print(f"Entity: {entity_text:<15} | Category Label: {entity_category}")


# =========================================================================
# Task 3: Part-of-Speech (POS) Tagging - Analyze Business Text
# =========================================================================
print("\n=================================================================")
print("TASK 3: COMPLETE GRAMMATICAL POS MAPPING")
print("=================================================================")
print(f"{'Tokenized Word':<18} | {'Grammar POS Tag Symbol':<22}")
print("-" * 45)
for word, tag in pos_tags:
	print(f"{word:<18} | {tag:<22}")
print("=================================================================")
