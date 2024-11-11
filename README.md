# Student_Performance_Tracker
This is a Python-based project that allows teachers to input student names and scores for various subjects, track their academic performance, and calculate the average scores of individual students and the entire class.

## Features:
- **Add Students**: Enter student names and scores for subjects (Math, Science, English).
- **Update Scores**: Modify the scores of existing students.
- **Calculate Averages**: Calculate the average score of each student and the overall class average.
- **Pass/Fail Check**: Automatically checks if each student is passing based on their scores.
- **Display Student Performance**: Lists all students, their average score, and their pass/fail status.

## Usage:

### Main Functionality:
1. **Add a New Student**:
   - Enter the student’s name and scores for the subjects: Math, Science, and English.
   
2. **Update an Existing Student’s Scores**:
   - Enter the name of the student you want to update and provide new scores for the subjects.

3. **Display Performance**:
   - After entering or updating student data, the system will display each student's performance, including their average score and pass/fail status. It will also show the overall class average.

### Commands:
- `stop`: Stops the input process and displays all results.
- `update`: Allows you to modify scores for an existing student.

## Example Output:

```plaintext
Enter student's name (or type 'stop' to finish, 'update' to modify scores): John
Enter Math score for John: 85
Enter Science score for John: 90
Enter English score for John: 80

Enter student's name (or type 'stop' to finish, 'update' to modify scores): Jane
Enter Math score for Jane: 45
Enter Science score for Jane: 55
Enter English score for Jane: 40

Enter student's name (or type 'stop' to finish, 'update' to modify scores): update
Enter the name of the student to update: John
Enter new Math score for John: 90
Enter new Science score for John: 92
Enter new English score for John: 88

Enter student's name (or type 'stop' to finish, 'update' to modify scores): stop

Student Performance:
Student: John, Average Score: 90.00, Status: Pass
Student: Jane, Average Score: 46.67, Status: Needs Improvement

Overall Class Average: 68.33
```

---

### How the Code Works:
1. **Student Class**: 
   - The `Student` class stores the student’s name and scores. It provides methods to retrieve and update student information (`get_name`, `set_name`, `get_scores`, `set_scores`).
   - It also calculates the student's average score and checks if the student has passed.

2. **PerformanceTracker Class**: 
   - The `PerformanceTracker` class manages all students and their scores.
   - It allows you to add students, update their scores, calculate the class average, and display individual student performance.

3. **User Interaction**: 
   - The `main` function interacts with the user, allowing them to add or update student information and view the performance data.



