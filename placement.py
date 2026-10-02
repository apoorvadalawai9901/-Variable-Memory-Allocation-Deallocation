# Task 10: Accept age, marks, attendance, experience, and backlog status.
# Determine placement eligibility and classify experience as fresher,
# junior, or experienced.

def assess_placement(age, marks, attendance, experience, has_backlog):
    if experience == 0:
        category = "fresher"
    elif 1 <= experience <= 2:
        category = "junior"
    else:
        category = "experienced"

    eligible = marks >= 60 and attendance >= 75 and not has_backlog
    return {"placement_eligible": "Yes" if eligible else "No", "candidate_category": category}


def main():
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))
    attendance = float(input("Enter attendance: "))
    experience = float(input("Enter years of experience: "))
    has_backlog = input("Has backlog? (yes/no): ").lower() == "yes"
    result = assess_placement(age, marks, attendance, experience, has_backlog)
    print(f"Placement eligible: {result['placement_eligible']}")
    print(f"Candidate category: {result['candidate_category']}")


if __name__ == "__main__":
    main()