def grade_classifier(score):
    if score >= 90:
        return 'Distinction'
    elif score >= 60:
        return 'Pass'
    else:
        return 'Fail'

for test_score in [100, 90, 75, 60, 45]:
    print(f"Score {test_score}: {grade_classifier(test_score)}")


print("\nTesting with a new set of scores:")
scores = [45, 72, 91, 60, 38, 85]
for score in scores:
    print(f"Score {score}: {grade_classifier(score)}")
