# Task 8: Check whether a skill is in ["python", "SQL", "Git", "HTML"]
# and report whether it is available.

REQUIRED_SKILLS = ["python", "SQL", "Git", "HTML"]


def check_skill(skill_name):
    if skill_name in REQUIRED_SKILLS:
        return "Skill available"
    return "Skill not available"


def main():
    skill_name = input("Enter a skill name: ").strip()
    print(check_skill(skill_name))


if __name__ == "__main__":
    main()