# Todux

The user-centred and community-driven to-do app.


This project has been created to learn and polish skills with django and python. 

Thanks to [Dennis Ivy](https://dennisivy.com/) for the incredible [django tutorial](https://youtu.be/PtQiiknWUcI?feature=shared) where i learn the basics to do my project  

Strongly inspired by [todoist](https://todoist.com/).


## Model 

- User
    - Tasks
    - Projects 
    - Tags

![model diagram](./misc/assets/todux-model-diagram.png "entity diagram like diagram")



Each task can only be assigned to one project. Each task can have as many tags as you want. 


## Usage and tested

```sh
git clone https://github.com/zft9xgy/todux.git
cd todux
touch db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



## Next steps

Next step will be implementing a front-end with React.js