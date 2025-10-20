# Final grade calculator
grade = 0
gpa = 0
passed_enough_labs = True

print("Welcome to the final grade calculator!")

passed_labs = int(input("How many labs did you pass(non-zero grade)? (out of 11):"))

if passed_labs >= 9:
    print("You met all the labs requirements!")
else:
    passed_enough_labs = False

chapter_exercises = float(input("How many of the chapter exercise points did you get? (out of 50):"))

projects = float(input("How many of the project points did you get? (out of 300):"))

coding_challenge_1 = float(input("How much did you score on coding challenge 1(out of 25):"))
coding_challenge_2 = float(input("How much did you score on coding challenge 2(out of 25):"))
coding_challenge_3 = float(input("How much did you score on coding challenge 3(out of 25):"))
print("Lowest of the three coding challenges will be dropped.")
# Find the two highest scores
coding_challenge_scores = [coding_challenge_1, coding_challenge_2, coding_challenge_3]
highest_scores = sorted(coding_challenge_scores, reverse=True)[:2]
coding_challenge_points = highest_scores[0] + highest_scores[1]

extra_credit_1 = float(input("How much did you score on extra credit 1(out of 30):"))

extra_credit_2 = float(input("How much did you score on extra credit 2(out of 30):"))

exam1 = float(input("How much did you score on exam 1 highest try (out of 150):"))
exam2 = float(input("How much did you score on exam 2 highest try (out of 200):"))
exam3 = float(input("How much did you score on the final exam highest try (out of 250):"))

print("Calculating your final grade...")

grade= chapter_exercises + projects + coding_challenge_points + extra_credit_1 + extra_credit_2 + exam1 + exam2 + exam3

grade = grade / 10

if grade >= 90:
    gpa = 4.0
elif grade >= 85:
    gpa = 3.5
elif grade >= 80:
    gpa = 3.0
elif grade >= 75:
    gpa = 2.5
elif grade >= 70:
    gpa = 2.0
elif grade >= 65:
    gpa = 1.5
elif grade >= 60:
    gpa = 1.0
else:
    gpa = 0.0

if not passed_enough_labs:
    gpa -= 0.5 * (9 - passed_labs)

if gpa < 0.0:
    gpa = 0.0

print("Your final grade is:", round(grade,2))
print("Your final GPA is:", gpa)
print("Thank you for using the final grade calculator!")