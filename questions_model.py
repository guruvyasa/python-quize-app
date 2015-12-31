import csv
import random

def get_questions(filename):
	questions = None
	try:
		with open(filename,'r') as f:
			reader = csv.reader(f)
			questions = list(reader)
			random.shuffle(questions)
	except:
		print("unable to process request")

	return questions



if __name__ == '__main__':
	print(get_questions('questions.csv'))


