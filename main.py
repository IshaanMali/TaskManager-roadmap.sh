import json
import datetime

with open("tasks.json","r") as f:
    data = json.load(f)

def taskManager():
    task = input("\nWhat task would you like to do today? ")
    if task[:3] == "add":
        if data == {}:
            data["tasks"].append({"id":"1","description":f"{task.split('"')[1]}","status":"todo","createdAt":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            print("Task added successfully (ID: 1)")
        else:
            no_of_tasks = len(data["tasks"])
            data["tasks"].append({"id":f"{no_of_tasks+1}","description":f"{task.split('"')[1]}","status":"todo","createdAt":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            print(f"Task added successfully (ID: {no_of_tasks+1})")
        with open("tasks.json","w") as f:
            json.dump(data,f)
    elif task[:6] == "update":
        task_dupe = task
        id_no = task.split(" ")[1]
        task_to_upd_desc = task_dupe.split('"')[1]
        print(int(id_no))
        data["tasks"][int(id_no)-1]["description"] = task_to_upd_desc
        data["tasks"][int(id_no)-1]["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("tasks.json","w") as f:
            json.dump(data,f)
    elif task[:6] == "delete":
        id_no = task.split(" ")[1]
        del data["tasks"][int(id_no)-1]
        with open("tasks.json","w") as f:
            json.dump(data,f)
    elif task[:16] == "mark-in-progress":
        id_no = task.split(" ")[1]
        data["tasks"][int(id_no)-1]["status"] = "in_progress"
        with open("tasks.json","w") as f:
            json.dump(data,f)
    elif task[:9] == "mark-done":
        id_no = task.split(" ")[1]
        data["tasks"][int(id_no)-1]["status"] = "done"
        with open("tasks.json", "w") as f:
            json.dump(data, f)
    elif task[:4] == "list":
        if task[:4] == "list" and len(task) == 4:
            for i in data["tasks"]:
                print(f"Task Name: {i["description"]}, Status: {i["status"]}")
        else:
            if task.split(" ")[1] == "done":
                for i in data["tasks"]:
                    if i["status"] == "done":
                        print(f"Task Name: {i["description"]}, Status: {i["status"]}")
            elif task.split(" ")[1] == "todo":
                for i in data["tasks"]:
                    if i["status"] == "todo":
                        print(f"Task Name: {i["description"]}, Status: {i["status"]}")
            elif task.split(" ")[1] == "in-progress":
                for i in data["tasks"]:
                    if i["status"] == "in_progress":
                        print(f"Task Name: {i["description"]}, Status: {i["status"]}")
    else:
        print("The function you are asking for doesn't exist, Please try again.")
        taskManager()
    taskManager()

taskManager()