import argparse
from lib.task_manager import get_or_create_user
from lib.generate_log import generate_log

def main():
    parser = argparse.ArgumentParser(description="Task Management CLI Tool")
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    
    add_parser = subparsers.add_parser('add-task', help='Add a new task')
    add_parser.add_argument('username', help='Username')
    add_parser.add_argument('task', help='Task description')
    
    
    complete_parser = subparsers.add_parser('complete-task', help='Mark task as complete')
    complete_parser.add_argument('username', help='Username')
    complete_parser.add_argument('task_index', type=int, help='Task index to complete')
    
    
    list_parser = subparsers.add_parser('list-tasks', help='List all tasks for user')
    list_parser.add_argument('username', help='Username')
    
    
    log_parser = subparsers.add_parser('generate-log', help='Generate a log file from tasks')
    log_parser.add_argument('username', help='Username')
    
    args = parser.parse_args()
    
    if args.command == 'add-task':
        user = get_or_create_user(args.username)
        result = user.add_task(args.task)
        print(result)
        
    elif args.command == 'complete-task':
        user = get_or_create_user(args.username)
        result = user.complete_task(args.task_index)
        print(result)
        
    elif args.command == 'list-tasks':
        user = get_or_create_user(args.username)
        print(f"Tasks for {args.username}:")
        print(user.list_tasks())
        
    elif args.command == 'generate-log':
        user = get_or_create_user(args.username)
        if user.tasks:
            log_data = [f"{args.username}: {task}" for task in user.list_tasks().split('\n') if task]
            generate_log(log_data)
        else:
            print(f"No tasks for {args.username} to log")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()