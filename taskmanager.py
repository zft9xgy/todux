import sqlite3


class TaskManager:
    def __init__(self, db_connection):
        self.conn = db_connection
        self.cursor = db_connection.cursor()

    """ 
    Task methods:
    - add_task
    - delete_task
    - complete_task
    - uncomplete_task
    - edit_task_title
    - assign_task_to_project
    - move_task_to_inbox
    - get_inbox_tasks

    """

    def add_task(self, task_title: str, task_done=False, project_id=1):
        self.cursor.execute(
            'INSERT INTO tasks (task_title,task_done,project_id) VALUES (?,?,?)', (str(task_title), bool(task_done), int(project_id)))
        self.conn.commit()

    def delete_task(self, task_id: int):
        self.cursor.execute(
            'DELETE FROM tasks WHERE task_id = (?)', (int(task_id),))
        self.conn.commit()

    def complete_task(self, task_id: int):
        self.cursor.execute(
            "UPDATE tasks SET task_done = ? WHERE task_id = ?", (1, int(task_id)))
        self.conn.commit()

    def uncomplete_task(self, task_id: int):
        self.cursor.execute(
            "UPDATE tasks SET task_done = ? WHERE task_id = ?", (0, int(task_id)))
        self.conn.commit()

    def edit_task_title(self, task_id: int, new_title: str):
        self.cursor.execute(
            "UPDATE tasks SET task_title = ? WHERE task_id = ?", (str(new_title), int(task_id)))
        self.conn.commit()

    def assign_task_to_project(self, task_id: int, project_id: str):
        self.cursor.execute(
            "UPDATE tasks SET project_id = ? WHERE task_id = ?", (int(project_id), int(task_id)))
        self.conn.commit()

    def move_task_to_inbox(self, task_id: int):
        self.assign_task_to_project(task_id, 1)

    def get_task_from_project(self, project_id: int):
        self.cursor.execute(
            "SELECT * FROM tasks WHERE project_id = ?", (int(project_id),))
        return self.cursor.fetchall()

    def get_inbox_tasks(self):
        return self.get_task_from_project(1)

    def get_uncompleted_tasks(self):
        self.cursor.execute('SELECT * FROM tasks WHERE done = false')
        return self.cursor.fetchall()

    def get_completed_tasks(self):
        self.cursor.execute('SELECT * FROM tasks WHERE done = true')
        return self.cursor.fetchall()

    def get_all_tasks(self):
        self.cursor.execute('SELECT * FROM tasks')
        return self.cursor.fetchall()

    #  projects
    # crud
    # add project
    def new_project(self, project_title: str, project_description: str = None):
        self.cursor.execute(
            "INSERT INTO projects (project_title,project_description) VALUES(?,?)", (str(project_title), project_description))
        self.conn.commit()
    # delete project (not for inbox)
    # update project title
    # update project description
    # delete project

    # methods
    # get_task_from_project(project_id,completed,uncompleted, all)
    # -> done, default uncompleted pero puede elegir completed, uncompleted o all

    def close(self):
        self.conn.close()
