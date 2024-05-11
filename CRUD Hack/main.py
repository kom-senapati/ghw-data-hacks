from db import *
from tabulate import tabulate


def main():

    print("🚀 Issue Tracking System 🚀")
    print("1. Create new issue")
    print("2. Assign issue to team member")
    print("3. Update issue details")
    print("4. Close issue")
    print("5. List issues")
    print("6. User management")
    print("7. Exit")
    print("\n\n")

    option = input("Enter your choice: ")

    if option == "1":
        title = input("Enter issue title: ")
        description = input("Enter issue description: ")
        assignee = input("Enter assignee username: ")
        create_issue(title, description, assignee)

        print("\n✨ Issue created successfully ✨\n")

    elif option == "2":
        issue_id = input("Enter issue ID: ")
        assignee = input("Enter assignee username: ")
        update_issue(issue_id, assignee=assignee)

        print("\n✨ Issue assigned successfully ✨\n")

    elif option == "3":
        issue_id = input("Enter issue ID: ")
        title = input("Enter issue title: ")
        description = input("Enter issue description: ")
        status = input("Enter issue status: ")
        assignee = input("Enter assignee username: ")
        update_issue(issue_id, title, description, status, assignee)

        print("\n✨ Issue updated successfully ✨\n")

    elif option == "4":
        issue_id = input("Enter issue ID: ")
        delete_issue(issue_id)

        print("\n✨ Issue closed successfully ✨\n")

    elif option == "5":
        issues = list_issues()
        issues_data = [
            [
                issue.id,
                issue.title,
                issue.description,
                issue.status,
                issue.assignee.username,
            ]
            for issue in issues
        ]
        print(
            tabulate(
                issues_data,
                headers=["ID", "Title", "Description", "Status", "Assignee"],
            )
        )

    elif option == "6":

        print("👩‍💼👨‍💼 User Management 👩‍💼👨‍💼")
        print("1. Create new user")
        print("2. Update user details")
        print("3. Delete user")
        print("4. List users")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                username = input("Enter username: ")
                email = input("Enter email: ")
                password = input("Enter password: ")
                create_user(username, email, password)

                print("\n✨ User created successfully ✨\n")

            case "2":
                username = input("Enter username: ")
                email = input("Enter email: ")
                password = input("Enter password: ")
                update_user(username, email, password)

                print("\n✨ User updated successfully ✨\n")

            case "3":
                username = input("Enter username: ")
                delete_user(username)

                print("\n✨ User deleted successfully ✨\n")

            case "4":
                users = list_users()
                users_data = [[user.username, user.email] for user in users]
                print(tabulate(users_data, headers=["Username", "Email"]))

            case "5":
                main()

            case _:
                print("Invalid option 🚫")
        main()

    elif option == "7":
        print("👋 Exiting... 👋")
        exit()

    else:
        print("Invalid option 🚫")


if __name__ == "__main__":
    while 1:
        main()
