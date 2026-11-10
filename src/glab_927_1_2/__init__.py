from glab_927_1_2.email_processing import run_assignment
from glab_927_1_2.sentiment_analysis import run_sentiment_analysis


def main() -> None:
	print("=================================================================")
	print("RUNNING GLAB 927.1.2: EMAIL PROCESSING")
	print("=================================================================\n")
	run_assignment()

	print("\n=================================================================")
	print("RUNNING GLAB 927.4.1: SENTIMENT ANALYSIS")
	print("=================================================================\n")
	run_sentiment_analysis()
