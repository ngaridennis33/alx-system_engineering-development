#!/usr/bin/python3
# Accepts integers(employee ID) as input
# Displays:
# Firstline: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
# EMPLOYEE_NAME: name of the employee
# NUMBER_OF_DONE_TASKS: number of completed tasks
# TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
# Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests as r
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    usr_id = r.get(url + 'users/{}'.format(sys.argv[1])).json()
    to_do = r.get(url + 'todos', params={'userId': sys.argv[1]}).json()
#    print(to_do)
    completed = [title.get("title") for title in to_do if
                 title.get('completed') is True]
    # print(completed)
    print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"),
                                                          len(completed),
                                                          len(to_do)))
    [print("\t {}".format(title)) for title in completed]
