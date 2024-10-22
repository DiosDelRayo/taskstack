# TaskStack

## Objectives

* GTD (Get Things Done)
* Pomodoro
* Now Page
* Attributing time to tasks
* History of Sessions worked on

## Uses

* GitHub Pages for the 'Now Page'
* Fokus (KDE Plasma Widget for Pomodoro)
* GitHub Issues for GTD task Managment
* gh CLI
* Own python scripts to:
    * [x] Switch current task
    * [x] Load next task into the "TaskStack"
    * [x] Stack Tasks for today or schedule ahead of time
    * [x] Mark current active task (issue with label 'Active') with 'WIP' on 'focus start'
    * [x] Unmark current active task (issue with label 'WIP') on 'focus end'
* Pelican plugin to:
    * parse tasks and create/update tasks(articles) in projects(folders)
    * create the now page

# Usage

You need to add the config file `~/.config/taskstack/config.yml` into CWD with the content:
```
github:
  token: <token>
repository: <repository>
```
