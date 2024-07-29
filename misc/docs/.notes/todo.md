# Next steps

- make a CRUD for the models
- tasks, create, edit, delete
- project
- tags

- currently on delete project, all tasks associated with that project are deleted. Confirm this behaviour

## Backlog

- add error catchers and data validation before saving to database.
- creating a task within a project or tag, by default the tag must be associated to that project or tag (maybe it is handled by the frontend?).
- when a task is added either from projects or tags, it should redirect to the page where it has been created:
  example, within the personal project, I create a task, it should redirect to the personal project page. (maybe it is handled by the frontend?)
- when a user create a new task, only need to be able to see users projects or tags, not the
- install corsheaders to allow call api from other origins

## Done

291123

- it should not be possible to create 2 tags with the same name
- it should not be possible to create 2 projects with the same name
