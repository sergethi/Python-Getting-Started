contacts = {
    "number": 4,
    "students": [
        {"name":"Sarah holderness", "email": "sarah@example.com"},
        {"name":"Harry Potter", "email": "harry@example.com"},
        {"name":"Hermione Granger", "email": "hermione@example.com"},
        {"name":"Ron Weasley", "email": "ron@example.com"},
    ]
}

print("Here is the students's eamil list:")
for student in contacts["students"]:
    print(student["email"])