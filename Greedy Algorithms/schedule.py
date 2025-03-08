#Greedy algorithm for scheduling tasks by earliest deadlines.

#Number of tasks input
num_tasks = int(input("Enter the number of tasks: "))

tasks = []

#take user input for task name and deadline
for i in range(num_tasks):
	task_name = input(f"Enter the name of task {i+1}: ")
	deadline = int(input(f"Enter the deadline (days) for task '{task_name}': "))
	tasks.append((task_name, deadline))

tasks.sort(key=lambda x: x[1])

#Display the ordered schedule.
print("\nTasks should be performed in the following order (earliest deadline first):")
for task, deadline in tasks:
	print(f"Task: '{task}', Deadline: {deadline} days")