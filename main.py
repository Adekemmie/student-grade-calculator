def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


def get_course_data(number_of_courses):
    courses = []
    scores = []

    for i in range(number_of_courses):
        course_name = input(f"\nEnter course {i + 1} name: ")

        while True:
            try:
                score = int(input("Enter score (0-100): "))

                if 0 <= score <= 100:
                    break

                print("Invalid score. Please enter a score between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        scores.append(score)

        grade = calculate_grade(score)

        courses.append((course_name, score, grade))

    return courses, scores


def main():
    while True:
        print("\n========================================")
        print("       STUDENT GRADE CALCULATOR")
        print("========================================")

        name = input("Enter your name: ")

        print("Hello,", name)

        while True:
            try:
                number_of_courses = int(
                    input("How many courses do you have? ")
                )

                if number_of_courses > 0:
                    break

                print("Please enter at least one course.")

            except ValueError:
                print("Please enter a valid number.")

        courses, scores = get_course_data(number_of_courses)

        total_score = sum(scores)
        average_score = total_score / number_of_courses
        overall_grade = calculate_grade(average_score)

        print("\n========================================")
        print("                RESULTS")
        print("========================================")

        print("Student:", name)
        print()

        print(f"{'Course':<20}{'Score':<10}{'Grade'}")
        print("-" * 40)

        for course_name, score, grade in courses:
            print(f"{course_name:<20}{score:<10}{grade}")

        print("-" * 40)
        print(f"Total Score: {total_score}")
        print(f"Average Score: {average_score:.2f}")
        print(f"Overall Grade: {overall_grade}")

        choice = input(
            "\nWould you like to calculate another student? (yes/no): "
        )

        if choice.lower() != "yes":
            print("\nThank you for using Student Grade Calculator!")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

