from.taskstack import TaskStack
from argparse import ArgumentParser
from typing import Optional

def start() -> None:
    TaskStack().start()

def stop() -> None:
    TaskStack().stop()

def next() -> None:
    TaskStack().next()

def done(task: Optional[int] = None) -> None:
    TaskStack().done(task)

def list(label: str) -> None:
    print('Load tasks...', end='', flush=True)
    tasks = TaskStack().list_tasks(label)
    print('done')
    for task in process_tasks(tasks):
        print(f"#{task.number:03d} {task.status or ''}{' ' if task.status else ''}{task.title}{' ' if len(task.label_list) > 0 else ''}{' '.join(['[' + label + ']' for label in task.label_list])}")
        if task.milestone:
            print(f'     > {task.milestone.title}')
    return

def process_tasks(tasks: list) -> list:
    print('Proccess tasks...', end='', flush=True)
    out = []
    for task in tasks:
        if not task.assignee:
            continue
        task.status = None
        task.label_list = [label.name for label in task.original_labels]
        if 'READ' in task.label_list or 'Idea' in task.label_list:
            continue
        task.priority = 0
        priorities = [10, 10, 5, 2, 1, -10]
        i = 0
        for label in ('WIP', 'Active', 'Stacked'):
            if label in task.label_list:
                if task.status is None:
                    task.status = f'[{label}]'
                task.priority += priorities[i]
                task.label_list.remove(label)
            i += 1
        for label in ('Urgent', 'Important', 'Low Priority'):
            if label in task.label_list:
                task.priority += priorities[i]
            i += 1
        out.append(task)
    out.sort(key=lambda task: task.priority)
    print('done')
    return out

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
    stack_parser.add_argument('task_id', type=int, nargs='?', help='ID of the task to stack, or without id will list tasks in stack')

    # Unstack command
    unstack_parser = subparsers.add_parser('unstack', help='Unstack a task')
    unstack_parser.add_argument('task_id', type=int, help='ID of the task to unstack')

    # Next command
    next_parser = subparsers.add_parser('next', help='Load the next task into the TaskStack')

    # Done command
    done_parser = subparsers.add_parser('done', help='Mark current task as done, if inside a pomodoro it will switch to the next one. You can also provide a task number to mark any task as done.')
    done_parser.add_argument('task_id', type=int, nargs='?', help='ID of the task to mark as done')

    # List command
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('--label', '-l', help='Filter by label')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('--body', '-b', help='Task description')
    add_parser.add_argument('--labels', '-l', nargs='+', help='Labels to add')
    args = parser.parse_args()

    if args.command == 'switch':
        TaskStack().switch(args.task_id)
        return
    if args.command == 'start':
        TaskStack().start()
        return
    if args.command == 'stop':
        TaskStack().stop()
        return
    if args.command == 'stack':
        if not args.task_id:
            list('Stacked')
            return
        TaskStack().stack(args.task_id)
        return
    if args.command == 'unstack':
        TaskStack().unstack(args.task_id)
        return
    if args.command == 'next':
        TaskStack().next()
        return
    if args.command == 'done':
        TaskStack().done(args.task_id)
        return
    if args.command == 'list':
        list(args.label)
        return
    if args.command == 'add':
        if TaskStack().add_task(args.title, args.body or '', args.labels or []):
            print(f"Task '{args.title}' created successfully")
        else:
            print('Failed to create task')
        return
    parser.print_help()

if __name__ == '__main__':
    main()

