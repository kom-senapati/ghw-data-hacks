from sqlobject import *
import os

db_filename = os.path.abspath("database.db")
connection_string = "sqlite:" + db_filename
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection


class Issue(SQLObject):
    title = StringCol()
    description = StringCol()
    status = StringCol(default="Open")
    assignee = ForeignKey("User")
    created = DateTimeCol(default=DateTimeCol.now)
    updated = DateTimeCol(default=DateTimeCol.now)


class User(SQLObject):
    username = StringCol()
    email = StringCol()
    password = StringCol()
    issues = MultipleJoin("Issue")

Issue.createTable(ifNotExists=True)
User.createTable(ifNotExists=True)


def create_issue(title, description, assignee):
    user = User.selectBy(username=assignee)[0]
    Issue(title=title, description=description, assignee=user)


def read_issue(issue_id):
    return Issue.get(issue_id)


def update_issue(issue_id, title=None, description=None, status=None, assignee=None):
    issue = Issue.get(issue_id)
    if title:
        issue.title = title
    if description:
        issue.description = description
    if status:
        issue.status = status
    if assignee:
        user = User.get(username=assignee)
        issue.assignee = user
    issue.updated = DateTimeCol.now()


def delete_issue(issue_id):
    issue = Issue.get(issue_id)
    issue.destroySelf()


def list_issues():
    return Issue.select()


def create_user(username, email, password):
    User(username=username, email=email, password=password)


def read_user(username):
    return User.get(username=username)


def update_user(username, email=None, password=None):
    user = User.get(username=username)
    if email:
        user.email = email
    if password:
        user.password = password


def delete_user(username):
    user = User.get(username=username)
    user.destroySelf()


def list_users():
    return User.select()
