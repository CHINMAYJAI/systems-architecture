# processId, AT (Arrival Time), BT (Burst Time), CT (Completion Time), TAT (Turnaround Time), WT (Waiting Time)

# The number of processes to be entered by the user
number_of_process = int(input("How many processes do you want to enter?\n"))

# List to store the arrival times of the processes
arrival_time_list = []
# List to store the burst times (execution times) of the processes
burst_time_list = []

# NOTE: Both arrival time and burst time must be provided by the user

# Taking arrival times as input
for i in range(number_of_process):
    # Getting the arrival time for each process from the user
    arrival_time = float(input(f"Enter arrival time for process {i + 1}: "))
    arrival_time_list.append(arrival_time)  # Appending each arrival time to the arrival_time_list

# Taking burst times as input
for i in range(number_of_process):
    # Getting the burst time (execution time) for each process from the user
    burst_time = float(input(f"Enter burst/execution time for process {i + 1}: "))
    burst_time_list.append(burst_time)  # Appending each burst time to the burst_time_list

# Initializing variables for process management
copy_arrival_time_list = arrival_time_list.copy()  # A copy of the arrival times
copy_burst_time_list = burst_time_list.copy()  # A copy of the burst times

gantt_chart = []  # List to store the Gantt chart
completion_time_chart = [0] * number_of_process  # Completion time chart for each process
processed = [False] * number_of_process  # A flag list to check if a process is processed

# Logic for the first process
first_arrival_time = min(copy_arrival_time_list)  # Find the first process based on arrival time
index = copy_arrival_time_list.index(first_arrival_time)  # Get the index of the first process
first_burst_time = copy_burst_time_list[index]  # Get the burst time of the first process

if first_arrival_time == 0:
    # If the first arrival time is 0, add burst time directly to Gantt chart
    gantt_chart.append(first_burst_time)
    completion_time_chart[index] = first_burst_time
else:
    # If the first arrival time is not 0, add idle time to Gantt chart
    gantt_chart.append(first_arrival_time)  # Idle time
    gantt_chart.append(first_burst_time + first_arrival_time)  # End time after processing the first process
    completion_time_chart[index] = first_burst_time + first_arrival_time

processed[index] = True  # Mark the first process as processed

# Logic for processing the remaining processes
for _ in range(number_of_process - 1):
    # Fetch unprocessed processes
    remaining_indices = [i for i, p in enumerate(processed) if not p]  # Get indices of unprocessed processes
    # Select the next process based on the earliest arrival time (AT), breaking ties with process ID (index)
    next_index = min(
        remaining_indices, key=lambda x: (arrival_time_list[x], x)
    )
    next_arrival_time = arrival_time_list[next_index]  # Arrival time of the next process
    next_burst_time = burst_time_list[next_index]  # Burst time of the next process

    # If there is idle time between the last process and the next one, add idle time
    if gantt_chart[-1] < next_arrival_time:
        gantt_chart.append(next_arrival_time)

    # Add the burst time of the next process to the Gantt chart
    burst_time_to_add = gantt_chart[-1] + next_burst_time
    gantt_chart.append(burst_time_to_add)  # Add the new end time to Gantt chart
    completion_time_chart[next_index] = burst_time_to_add  # Update completion time for the next process
    processed[next_index] = True  # Mark the process as processed

# Calculate the turnaround time (TAT) and waiting time (WT) for each process
turn_around_time_list = [
    completion_time_chart[i] - arrival_time_list[i] for i in range(number_of_process)
]  # TAT = CT - AT for each process
waiting_time_list = [
    turn_around_time_list[i] - burst_time_list[i] for i in range(number_of_process)
]  # WT = TAT - BT for each process

# Display the results
print(f"Gantt Chart: {gantt_chart}")  # Print the Gantt chart of process execution times
print(f"Completion Chart: {completion_time_chart}")  # Print the completion times of each process
print(f"Turnaround Time Chart: {turn_around_time_list}")  # Print the turnaround time for each process
print(f"Waiting Time Chart: {waiting_time_list}")  # Print the waiting time for each process

# Calculate and print the average turnaround time and average waiting time
average_turn_around_time = sum(turn_around_time_list) / number_of_process
average_waiting_time = sum(waiting_time_list) / number_of_process
print(f"Average Turnaround Time: {average_turn_around_time}")  # Average TAT
print(f"Average Waiting Time: {average_waiting_time}")  # Average WT
average_response_time = average_turn_around_time - average_waiting_time
print(f"Average Response Time: {average_response_time}") # Average RT