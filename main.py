import argparse
import json
import os

FILE = "tasks.json"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

def add(task, priority):
    data = load()
    data.append({"task": task, "priority": priority})
    save(data)

def delete(index):
    data = load()
    if 0 <= index < len(data):
        data.pop(index)
    save(data)

def list_tasks():
    data = load()
    data.sort(key=lambda x: x["priority"])
    for i, t in enumerate(data):
        print(i, t)

parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("--task")
parser.add_argument("--priority", type=int)
parser.add_argument("--index", type=int)

args = parser.parse_args()

if args.action == "add":
    add(args.task, args.priority)
elif args.action == "delete":
    delete(args.index)
elif args.action == "list":
    list_tasks()
