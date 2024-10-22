# TaskStack

A GTD (Get Things Done) task management system integrated with GitHub Issues and Pomodoro technique.

## Features

* GitHub Issues integration for task management
* Pomodoro technique support via KDE Plasma Widget (Fokus)
* Task stacking and scheduling
* GitHub Pages integration for "Now Page"
* Session history tracking
* Command-line interface for all operations

## Installation

```bash
pip install taskstack
```

## Configuration

Create a config file at `~/.config/taskstack/config.yml` with:

```yaml
github:
  token: <your-github-token>
repository: <your-repository>
```

## Usage

TaskStack provides the following commands:

```bash
# List all tasks
taskstack list
taskstack list --label bug  # Filter by label

# Add a new task
taskstack add "Task title" --body "Description" --labels bug feature

# Stack management
taskstack stack 123    # Stack task #123 for later
taskstack unstack 123  # Remove task from stack
taskstack next        # Load next stacked task

# Task switching
taskstack switch 123  # Switch to task #123

# Pomodoro integration
taskstack start      # Start focus session
taskstack stop       # End focus session
```

## Task States

* **Active**: Currently selected task
* **WIP**: Task in progress (during Pomodoro session)
* **Stacked**: Task scheduled for later

## Integration

* **GitHub Pages**: Used for the 'Now Page'
* **Fokus**: KDE Plasma Widget for Pomodoro
* **GitHub Issues**: Core task management
* **gh CLI**: Alternative command-line interface

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

BIPCOT NoGov License:
This software is released under BIPCOT NoGov License Version 3.
Created by [@DiosDelRayo](https://github.com/DiosDelRayo)
This license requires the following conditions be met:
1. This software cannot be used by any government agency or government funded organization.
2. All redistribution must retain this condition.
3. Modified versions must also carry this license.
4. Private commercial use is allowed.
5. Creative works and media made using this software can be under any license.
