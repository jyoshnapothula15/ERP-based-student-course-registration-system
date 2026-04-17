# Simple ERP Course Registration System

# Data
students = {}
courses = {
    "C1": {"name": "Maths", "seats": 2},
    "C2": {"name": "Physics", "seats": 2}
}

# Register
def register():
    name = input("Enter username: ")
    pwd = input("Enter password: ")
    role = input("Enter role (student/admin): ")
    students[name] = {"pwd": pwd, "role": role, "courses": []}
    print("Registered successfully!")

# Login
def login():
    name = input("Enter username: ")
    pwd = input("Enter password: ")
    
    if name in students and students[name]["pwd"] == pwd:
        return name, students[name]["role"]
    else:
        print("Invalid login")
        return None, None

# Student
def student(name):
    while True:
        print("\n1.View Courses  2.Register Course  3.Logout")
        ch = input("Enter choice: ")
        
        if ch == "1":
            for c in courses:
                print(c, courses[c])
        
        elif ch == "2":
            cid = input("Enter course id: ")
            if cid in courses and courses[cid]["seats"] > 0:
                students[name]["courses"].append(cid)
                courses[cid]["seats"] -= 1
                print("Registered!")
            else:
                print("Not available")
        
        elif ch == "3":
            break

# Admin
def admin():
    while True:
        print("\n1.Add Course  2.View Courses  3.Logout")
        ch = input("Enter choice: ")
        
        if ch == "1":
            cid = input("Course ID: ")
            cname = input("Course Name: ")
            seats = int(input("Seats: "))
            courses[cid] = {"name": cname, "seats": seats}
        
        elif ch == "2":
            print(courses)
        
        elif ch == "3":
            break

# Main
while True:
    print("\n1.Register  2.Login  3.Exit")
    ch = input("Enter choice: ")
    
    if ch == "1":
        register()
    
    elif ch == "2":
        user, role = login()
        
        if role == "student":
            student(user)
        elif role == "admin":
            admin()
    
    elif ch == "3":
        break
