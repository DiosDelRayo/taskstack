from.taskstack import TaskStack
from argparse import ArgumentParser

def start():
    taskstack = TaskStack()
    taskstack.start()

def stop():
    taskstack = TaskStack()
    taskstack.stop()

def next():
    taskstack = TaskStack()
    taskstack.next()

def main():
    parser = ArgumentParser(description='TaskStack CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Switch command
    switch_parser = subparsers.add_parser('switch', help='Switch to a new task')
    switch_parser.add_argument('task_id', type=int, help='ID of the task to switch to')

    # Start command
    start_parser = subparsers.add_parser('start', help='Start a new focus session')

    # Stop command
    stop_parser = subparsers.add_parser('stop', help='Stop the current focus session')

    # Stack command
    stack_parser = subparsers.add_parser('stack', help='Stack a task for later')
    stack_parser.add_argument('task_id', type=int, help='ID of the task to stack')

    # Unstack command
    unstack_parser = subparsers.add_parser('unstack', help='Unstack a task')
    unstack_parser.add_argument('task_id', type=int, help='ID of the task to unstack')

    # Next command
    next_parser = subparsers.add_parser('next', help='Load the next task into the TaskStack')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('--label', '-l', help='Filter by label')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('--body', '-b', help='Task description')
    add_parser.add_argument('--labels', '-l', nargs='+', help='Labels to add')
    args = parser.parse_args()

    taskstack = TaskStack()

    if args.command == 'switch':
        taskstack.switch(args.task_id)
        return
    if args.command == 'start':
        taskstack.start()
        return
    if args.command == 'stop':
        taskstack.stop()
        return
    if args.command == 'stack':
        taskstack.stack(args.task_id)
        return
    if args.command == 'unstack':
        taskstack.unstack(args.task_id)
        return
    if args.command == 'next':
        taskstack.next()
        return
    if args.command == 'list':
        tasks = taskstack.list_tasks(args.label)
        for task in tasks:
            labels = [label.name for label in task.labels()]
            status = ""
            if "WIP" in labels:
                status = "[WIP]"
            elif "Active" in labels:
                status = "[Active]"
            elif "Stacked" in labels:
                status = "[Stacked]"
            print(f"#{task.number} {status} {task.title}")
        return
    if args.command == 'add':
        if taskstack.add_task(args.title, args.body or "", args.labels or []):
            print(f"Task '{args.title}' created successfully")
        else:
            print("Failed to create task")
        return
    parser.print_help()

if __name__ == '__main__':
    main()

