"""
=============================================================================
BUSINESS NLP: SENTIMENT ANALYSIS REFERENCE & SCRIPT
=============================================================================
This script tracks and interprets customer opinions for business insights:
- Polarity: Measures the emotional direction (-1 = Negative, 0 = Neutral, 1 = Positive).
- Subjectivity: Measures opinion bias (0 = Fact-based, 1 = Opinion-based).
=============================================================================
"""
from textblob import TextBlob


def run_sentiment_analysis():
	# =========================================================================
	# Task 1: Importing Libraries and Verifying Environment
	# =========================================================================
	print("=================================================================")
	print("TASK 1: ENVIRONMENT SETUP & VERIFICATION")
	print("=================================================================")
	sample_setup_text = "TextBlob is successfully installed and ready to use!"
	print(f"TextBlob library successfully imported. Sample text: {sample_setup_text}\n")

	# =========================================================================
	# Task 2: Implementing Basic Sentiment Analysis
	# =========================================================================
	print("=================================================================")
	print("TASK 2: SINGLE TEXT SENTIMENT ANALYSIS")
	print("=================================================================")
	single_review = "I absolutely love this product! The quality is excellent and it arrived on time."

	blob = TextBlob(single_review)
	sentiment = blob.sentiment

	print(f"Original Text: {single_review}")
	print("Sentiment Analysis Result:")
	print(f"Polarity score    : {sentiment.polarity:.2f} (Ranges -1 to 1)")
	print(f"Subjectivity score: {sentiment.subjectivity:.2f} (Ranges 0 to 1)\n")

	# =========================================================================
	# Task 3: Analyzing Business Communication Data (Multiple Feedbacks)
	# =========================================================================
	print("=================================================================")
	print("TASK 3: MULTIPLE CUSTOMER FEEDBACK SENTIMENT ANALSYS")
	print("=================================================================")

	# Collection of realistic business service improvement comments
	feedback_comments = [
		"The recent updates to the support portal are amazing. Issues get resolved so quickly now!",
		"The new interface is completely confusing. It took me twice as long to file a single report.",
		"The platform received security updates yesterday. It functions exactly as it did before.",
		"Customer service responded within ten minutes, but they completely failed to resolve my issue.",
		"Outstanding training session today! The documentation is incredibly clear and helpful."
	]

	# Print a clean, formatted grid header for our analysis tracking table
	print(f"{'Analyzed Customer Comment':<40} | {'Polarity':<8} | {'Subjectivity':<12} | {'Derived Sentiment Label'}")
	print("-" * 90)

	for comment in feedback_comments:
		fb_blob = TextBlob(comment)
		pol = fb_blob.sentiment.polarity
		sub = fb_blob.sentiment.subjectivity

		# Deriving an actionable, rule-based label based on our polarity thresholds
		if pol > 0.1:
			label = "🟢 Positive Sentiment"
		elif pol < -0.1:
			label = "🔴 Negative Sentiment"
		else:
			label = "🟡 Neutral Sentiment"

		# Truncating long strings to keep our table perfectly square in the console
		short_comment = comment if len(comment) <= 38 else comment[:35] + "..."
		print(f"{short_comment:<40} | {pol:<8.2f} | {sub:<12.2f} | {label}")
	print("=================================================================")


if __name__ == "__main__":
	run_sentiment_analysis()
