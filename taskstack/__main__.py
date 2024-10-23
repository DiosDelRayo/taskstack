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

def task_priority(task) -> int:
    labels = [label.name for label in task.labels()]
    if 'WIP' in labels or 'Active' in labels:
        return 10
    prio = 0
    if 'Stacked' in labels:
        prio += 5
    if 'Urgent' in labels:
        prio += 2
    if 'Important' in labels:
        prio += 1
    if 'Low Priority' in labels:
        prio -= 10
    return prio

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
        print('Load tasks...', end='', flush=True)
        tasks = taskstack.list_tasks(args.label)
        print('done')
        for task in sorted(tasks, key=task_priority):
            if not task.assignee:
                continue
            labels = [label.name for label in task.labels()]
            status = []
            if 'READ' in labels or 'Idea' in labels:
                continue
            if 'WIP' in labels:
                status.append('[WIP]')
                labels.remove('WIP')
            elif 'Active' in labels:
                status.append('[Active]')
                labels.remove('Active')
            elif 'Stacked' in labels:
                status.append('[Stacked]')
                labels.remove('Stacked')
            l = ' '.join([f'[{label}]' for label in labels])
            print(f"#{task.number:03d} {' '.join(status)}{' ' if len(status) > 0 else ''}{task.title}{' ' if len(labels) > 0 else ''}{l}")
            if task.milestone:
                print(f'     >{task.milestone.title}')
        return
    if args.command == 'add':
        if taskstack.add_task(args.title, args.body or '', args.labels or []):
            print(f"Task '{args.title}' created successfully")
        else:
            print('Failed to create task')
        return
    parser.print_help()

if __name__ == '__main__':
    main()

