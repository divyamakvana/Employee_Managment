from database import connect_db, initialize_db

def add_employee(name, age, department, position, salary):
    with connect_db() as conn:
        conn.execute("""
            INSERT INTO employees (name, age, department, position, salary)
            VALUES (?, ?, ?, ?, ?)
        """, (name, age, department, position, salary))
        conn.commit()

def view_employees():
    with connect_db() as conn:
        result = conn.execute("SELECT * FROM employees")
        for row in result:
            print(row)

def update_employee(emp_id, name, age, department, position, salary):
    with connect_db() as conn:
        conn.execute("""
            UPDATE employees
            SET name = ?, age = ?, department = ?, position = ?, salary = ?
            WHERE id = ?
        """, (name, age, department, position, salary, emp_id))
        conn.commit()

def delete_employee(emp_id):
    with connect_db() as conn:
        conn.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
        conn.commit()

def main():
    initialize_db()
    while True:
        print("\n1. Add Empolyee\n2. View Employee\n3. Update Employee\n4. Delete Employee\n5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            n = input(" Enter Name: ")
            a = int(input(" Enter Age: "))
            d = input("Enterr Deptartment: ")
            p = input("Enter Position: ")
            s = float(input("Enter Salary: "))
            add_employee(n, a, d, p, s)
        elif choice == "2":
            view_employees()
        elif choice == "3":
            eid = int(input("ID: "))
            n = input("Name: ")
            a = int(input("Age: "))
            d = input("Dept: ")
            p = input("Position: ")
            s = float(input("Salary: "))
            update_employee(eid, n, a, d, p, s)
        elif choice == "4":
            eid = int(input("ID to delete: "))
            delete_employee(eid)
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
