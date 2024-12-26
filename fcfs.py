# Function to calculate waiting time for each process
def calculate_waiting_time(processes, n, burst_time, waiting_time):
    waiting_time[0] = 0  # First process has no waiting time

    # Calculating waiting time for each subsequent process
    for i in range(1, n):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]

# Function to calculate turnaround time for each process
def calculate_turnaround_time(processes, n, burst_time, waiting_time, turnaround_time):
    # Turnaround time is the sum of burst time and waiting time
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

# Function to calculate average waiting and turnaround times
def find_avg_times(processes, n, burst_time):
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time and turnaround time
    calculate_waiting_time(processes, n, burst_time, waiting_time)
    calculate_turnaround_time(processes, n, burst_time, waiting_time, turnaround_time)

    print("\nProcesses    Burst Time    Waiting Time    Turnaround Time")

    total_waiting_time = 0
    total_turnaround_time = 0

    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
        print(f"   {processes[i]} \t\t {burst_time[i]} \t\t {waiting_time[i]} \t\t {turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {total_waiting_time / n:.2f}")
    print(f"Average Turnaround Time: {total_turnaround_time / n:.2f}")

# Driver code to take user input
if __name__ == "__main__":
    # Input: Number of processes
    n = int(input("Enter the number of processes: "))

    # Input: Process IDs and Burst times
    processes = []
    burst_time = []

    for i in range(n):
        process_id = str(input(f"Enter Process ID for process {i+1}: "))
        processes.append(process_id)
        bt = int(input(f"Enter Burst Time for process {process_id}: "))
        burst_time.append(bt)

    # Call function to calculate average times
    find_avg_times(processes, n, burst_time)
