# Build a simple student grade evaluation system

from enum import Enum

class Grade(Enum):
    A = "Excellent"
    B = "Good"
    C = "Average"
    FAIL = "Needs Improvement"

student_results = []

name = "Jimmy"
Phy = 70
Chem = 90
Elec = 89

student_data = {
    'name': name,
    'marks': [Phy, Chem, Elec]
}

average_score = sum(student_data["marks"]) / len(student_data['marks'])

if average_score >= 90:
    grade = Grade.A
elif average_score >= 75:
    grade = Grade.B
elif average_score >= 60:
    grade = Grade.C
else: 
    grade = Grade.FAIL

student_results.append({
    'name': student_data['name'],
    'average': average_score,
    'grade': grade.name,
    'remarks': grade.value
})

result = student_results[0]

print("Student summary: ")
print("Name:",result['name'])
print("Average:",result['average'])
print("Grade:",result['grade'])
print("Remarks:",result['remarks'])