def average_score(*scores):
	if scores:
		return sum(scores) / len(scores)
	return 0

print("Average:", average_score(70, 80, 90))
