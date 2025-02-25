student = {
    "name":"Mary",
    "courses":[
        {
            "name":"Programming",
            "grade":56
        },
        {
            "name":"History",
            "grade":99
        }
    ]
}
print(f"Student: {student['name']}")
for course in student['courses']:
    print(f"\t {course['name']:<12}: {course['grade']:>5}")
