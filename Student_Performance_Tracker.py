class Student:

    def __init__(self, name, scores):
        self._name = name
        self._scores = scores

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_scores(self):
        return self._scores

    def set_scores(self, scores):
        self._scores = scores

    def calculate_average(self):
        return sum(self._scores) / len(self._scores) if self._scores else 0

    def is_passing(self, passing_score=50):
        return all(score >= passing_score for score in self._scores)

    def update_scores(self, new_scores):
        self._scores = new_scores


class PerformanceTracker:
    def __init__(self):
        self._students = {}

    def add_student(self, name, scores):
        self._students[name] = Student(name, scores)

    def update_student_scores(self, name, new_scores):
        if name in self._students:
            self._students[name].set_scores(new_scores)
            print(f"Updated scores for {name}.")
        else:
            print(f"Student {name} not found. Cannot update scores.")

    def calculate_class_average(self):
        if not self._students:
            return 0
        total_scores = sum(student.calculate_average()
                           for student in self._students.values())
        return total_scores / len(self._students)

    def display_student_performance(self):
        print("\nStudent Performance:")
        if not self._students:
            print("No students have been added yet.")
            return

        for name, student in self._students.items():
            avg_score = student.calculate_average()
            status = "Pass" if student.is_passing() else "Needs Improvement"
            print(f"Student: {name}, Average Score: {
                  avg_score:.2f}, Status: {status}")

        print(f"\nOverall Class Average: {self.calculate_class_average():.2f}")


def main():
    tracker = PerformanceTracker()

    while True:
        name = input(
            "Enter student's name (or type 'stop' to finish, 'update' to modify scores): ")

        if name.lower() == 'stop':
            break

        elif name.lower() == 'update':
            name_to_update = input("Enter the name of the student to update: ")
            new_scores = []

            for subject in ["math", "science", "English"]:
                while True:
                    try:
                        score = int(
                            input(f"Enter new {subject} score for {name_to_update}: "))
                        if score < 0 or score > 100:
                            print(
                                "Score must be between 0 and 100. Please try again.")
                            continue
                        new_scores.append(score)
                        break
                    except ValueError:
                        print("Invalid input. Please enter an integer for the score.")

            tracker.update_student_scores(name_to_update, new_scores)
            continue

        if name == "":
            print("Student name cannot be empty. Please enter a valid name.")
            continue

        scores = []

        for subject in ["Math", "Science", "English"]:
            while True:
                try:
                    score = int(input(f"Enter {subject} score for {name}: "))
                    if score < 0 or score > 100:
                        print("Score must be between 0 and 100. Please try again.")
                        continue
                    scores.append(score)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for the score.")

        tracker.add_student(name, scores)

    tracker.display_student_performance()


main()
