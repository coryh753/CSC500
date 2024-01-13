roomNumber = {"CSC101" : 3004, "CSC102" : 4501, "CSC103" : 6755, "NET110" : 1244, "COM241" : 1411}
instructorName = {"CSC101" : "Haynes", "CSC102": "Alvarado", "CSC103" : "Rich", "NET110" : "Burke", "COM241" : "Lee"}
meetingTime = {"CSC101" : "8:00 a.m.", "CSC102" : "9:00 a.m", "CSC103" : "10:00 a.m.", "NET110" : "11:00 a.m.", "COM241" : "1:00 p.m."}

courseNum = input("Enter your course number in all caps (ex. CSC101): ")

try:
    print(f'Course {courseNum} taught by professor {instructorName[courseNum]} in room {roomNumber[courseNum]} at {meetingTime[courseNum]}')
except KeyError:
    print("Please enter a valid course number.")