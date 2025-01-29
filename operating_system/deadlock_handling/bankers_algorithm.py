class BankersAlgorithm:
    def __init__(self):
        """All the prerequisites that are required to perform Banker's Algorithm"""
        self.processes = []
        self.resources = []
        self.allocation = []
        self.max_need = []
        self.total_resources_available = []

        # Total number of processes
        no_of_processes = int(input("Total number of processes: "))
        # Inserting those processes into the list
        for i in range(no_of_processes):
            self.processes.append(f"P{i+1}")

        # Total number of resources
        no_of_resources = int(input("Total number of resources: "))
        # Inserting those resources into the list
        for i in range(no_of_resources):
            self.resources.append(f"R{i+1}")

        # Fetch the total number of resources that are available
        for resource in range(no_of_resources):
            maximum_resource = int(
                input(f"Maximum resources available for {self.resources[resource]}: ")
            )
            self.total_resources_available.append(maximum_resource)

        # Resource allocation for each process
        for process in range(no_of_processes):
            resource_list = []
            for resource in range(no_of_resources):
                resource_allocation = int(
                    input(
                        f"Number of resources allocated for Process {process+1} and resource {resource+1} is:\n"
                    )
                )
                resource_list.append(resource_allocation)
            self.allocation.append(resource_list)

        # Maximum need for each process
        for process in range(no_of_processes):
            max_need_list = []
            for resource in range(no_of_resources):
                max_resource_allocation = int(
                    input(
                        f"Maximum need of resources allocated for Process {process+1} and resource {resource+1} is:\n"
                    )
                )
                max_need_list.append(max_resource_allocation)
            self.max_need.append(max_need_list)

    def calculation(self):
        """This function is used to perform the calculation of Banker's Algorithm"""
        # Calculate total allocated resources
        total_allocated_resources = [0] * len(self.resources)
        for process in range(len(self.processes)):
            for resource in range(len(self.resources)):
                total_allocated_resources[resource] += self.allocation[process][resource]

        # Calculate available resources
        total_available_resources = [
            self.total_resources_available[i] - total_allocated_resources[i]
            for i in range(len(self.resources))
        ]

        # Calculate need matrix
        need_matrix = []
        for process in range(len(self.processes)):
            need_matrix.append([
                self.max_need[process][resource] - self.allocation[process][resource]
                for resource in range(len(self.resources))
            ])

        # Safe sequence calculation
        safe_sequence = []
        work = total_available_resources.copy()
        finish = [False] * len(self.processes)

        while True:
            found = False
            for process in range(len(self.processes)):
                if not finish[process]:
                    can_allocate = True
                    for resource in range(len(self.resources)):
                        if need_matrix[process][resource] > work[resource]:
                            can_allocate = False
                            break
                    if can_allocate:
                        safe_sequence.append(f"P{process+1}")
                        for resource in range(len(self.resources)):
                            work[resource] += self.allocation[process][resource]
                        finish[process] = True
                        found = True

            if not found:
                break

        # Check if all processes are finished
        if all(finish):
            print("Safe sequence exists:")
            print(" -> ".join(safe_sequence))
        else:
            print("Deadlock will occur. No safe sequence exists.")

    def main(self):
        self.calculation()


if __name__ == "__main__":
    bankers_algorithm = BankersAlgorithm()
    bankers_algorithm.main()