class DeadlockDetection:
    def __init__(self):
        """all the basic things that are necessary are written over here like conditions initialisation and resource, process intake"""
        # initializing all the conditions as false
        self.mutual_exclusion = True  # as it cannot be avoided
        self.circular_wait = False
        self.non_preemption = False
        self.hold_and_wait = False
        self.resources_list = []
        self.processes_list = []
        self.resource_request_list = []

    def initialize(self):
        # input the total number of processes and resources
        number_of_resources = int(input("Number of resources: "))
        number_of_processes = int(input("Number of processes: "))
        # making the list of all the resources and processes
        for resources in range(number_of_resources):
            self.resources_list.append(f"R{resources+1}")
        for processes in range(number_of_processes):
            self.processes_list.append(f"P{processes+1}")

        # displaying the list of processes and list of resources
        print("Processes", end="  ")
        for processes in self.processes_list:
            print(processes, end=" ")
        print("\nResources", end="  ")
        for resources in self.resources_list:
            print(resources, end=" ")

        print("\n")
        """
        concept:
        conditions of deadlock occurrence:
        1. mutual exclusion
        2. circular wait
        3. non-preemption
        4. hold and wait

        if any of the condition is failed then deadlock will not occur
        """

    def circular_wait_condition(self):
        # NOTE: condition2 (circular_wait)

        # copying the original list so that original data will remain secure
        copy_resources_list_for_allocation = self.resources_list.copy()
        # appending "" as if any resource is not requested by any other process then in that case it can be left void
        copy_resources_list_for_allocation.append("")
        set_of_resource_allocated = set()
        set_of_resource_request = set()

        # if the below condition satisfies then in that case circular wait will not be there and there will be no deadlock
        if len(self.resources_list) > len(self.processes_list):
            self.circular_wait = False
        # if the condition is false then in that case below code is executed
        else:
            # use to break the infinite loop
            encounter_variable = 0
            while encounter_variable != len(self.processes_list):
                # asking for resources that are allocated by the corresponding processes and the resources are waiting to be allocated by the processes
                resource_allocated = str(
                    input(f"{self.processes_list[encounter_variable]} allocates: ")
                )
                resource_request = str(
                    input(f"{self.processes_list[encounter_variable]} requests:  ")
                )

                # if the resource_allocated is already been allocated then another process cannot allocate that resource
                if resource_allocated.title() not in copy_resources_list_for_allocation:
                    print(
                        f"Cannot allocate {resource_allocated.title()} as it is already allocated"
                    )
                    continue
                else:
                    copy_resources_list_for_allocation.remove(resource_allocated.title())

                # this is used to append all the resources that are requested by the processes so that we can easily check hold_and_wait condition
                self.resource_request_list.append(resource_request)
                # if "" is encountered then in that case it will not add into the set as if it added inside the set then in that case number of resources allocated will not match so for that it just increment the encounter_variable and continue the loop

                # if below condition is satisfied but request is there so for that case below code is executed
                if resource_allocated == "":
                    encounter_variable += 1
                    set_of_resource_request.add(resource_request)
                    continue

                # if below condition is satisfied but resource allocation is there so for that case below code is executed
                elif resource_request == "":
                    set_of_resource_allocated.add(resource_allocated)
                    encounter_variable += 1
                    continue

                # if any resource is allocated and request then the below conditional code is executed
                else:
                    set_of_resource_allocated.add(resource_allocated)
                    set_of_resource_request.add(resource_request)
                # incrementing encounter_variable
                encounter_variable += 1
            print("-" * 50)
            if len(self.resources_list) != len(set_of_resource_allocated):
                self.circular_wait = False
            elif len(self.resources_list) != len(set_of_resource_request):
                self.circular_wait = False
            else:
                self.circular_wait = True

    # NOTE: condition3 (non-preemption)
    def non_preemption_condition(self):
        # 1 for non_preemption and 0 for preemption
        while True:
            priority_check = int(
                input(
                    "Enter 0 if all the processes are preemptive\nEnter 1 if all the processes are non-preemptive\n"
                )
            )
            print("-" * 50)
            if priority_check == 0:
                self.non_preemption = False
                break
            elif priority_check == 1:
                self.non_preemption = True
                break
            else:
                print("Invalid Input")

    # NOTE: condition4 (hold and wait)
    def hold_and_wait_condition(self):
        # if two or more number of processes is requesting the same resource then hold and wait condition is satisfied
        # if circular wait is true than hold and wait condition is automatically becomes true
        if self.circular_wait:
            self.hold_and_wait = True
            return

        # removing all the null resources so that we can match that the number of requested resources are occurring more than one or not
        if "" in self.resource_request_list:
            null_resource = self.resource_request_list.count("")
            for _ in range(null_resource):
                self.resource_request_list.remove("")
        # now checking if the resources is occurring more than one or not if yes then the loop will break and it will return hold and wait as true value
        for resource in self.resource_request_list:
            resource_occurance = self.resource_request_list.count(resource)
            if resource_occurance >= 2:
                self.hold_and_wait = True

    def display_deadlock_occurrence(self):
        # displaying the message whether the deadlock is occurred or not
        if not self.circular_wait:
            print("Deadlock Not occur")
        elif not self.non_preemption:
            print("Deadlock Not occur")
        elif not self.hold_and_wait:
            print("Deadlock Not occur")
        else:
            print("Deadlock Occur")

    def main(self):
        self.initialize()
        self.circular_wait_condition()
        self.non_preemption_condition()
        self.hold_and_wait_condition()
        self.display_deadlock_occurrence()


# calling the main function
if __name__ == "__main__":
    deadlock_detection = DeadlockDetection()
    deadlock_detection.main()