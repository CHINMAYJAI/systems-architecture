class CScanAlgorithm:
    """It is also known as circular elevator/scan algorithm, and it is the part of disk scheduling algorithm"""
    def __init__(self):
        """data variables are initialised which is required over the period of time"""
        self.head_pointer = 0
        self.direction = ""  # left or right
        self.max_cylinder_value = 0
        self.min_cylinder_value = -1  # setting minimum cylinder value as -1 because maximum cylinder value is greater
        self.seek_time = 0  # required answer
        self.request_queue = []  # input provided by user

    def cScanDiskSchedulingAlgorithm(self):
        """Main c-scan scheduling algorithm calculation function"""

        # asking how many address must be there in the request queue excluding minimum and maximum cylindrical value
        number_of_addresses = int(input(
            "Irrespective of minimum cylinder value and maximum cylinder value\nHow many address do you want to enter?\n"))

        # inserting all the requests in the request_queue
        for i in range(number_of_addresses):
            address = int(input(f"Enter value of address {i + 1}: "))
            self.request_queue.append(address)

        # inserting the value of head pointer in request queue
        self.head_pointer = int(input("Enter the value disk arm/head pointer: "))
        self.request_queue.append(self.head_pointer)

        # sorting the array
        self.request_queue.sort()

        # Asking for inserting the minimum and maximum cylindrical value
        self.min_cylinder_value = int(input("Enter minimum cylindrical value: "))
        self.max_cylinder_value = int(input("Enter maximum cylindrical value: "))

        # inserting the minimum and maximum cylindrical value into request_queue
        self.request_queue.insert(0, self.min_cylinder_value)
        self.request_queue.append(self.max_cylinder_value)

        # NOTE: main logic
        while True:
            self.direction = str(input("Enter direction left or right: "))
            # pointer to the head_pointer. Which is used to move from pointer element to the destination element
            pointer = self.head_pointer
            # fetching the index for the pointer element
            pointer_index = self.request_queue.index(pointer)
            # use to store all the numbers which are already been subtracted from its consecutive numbers
            number_array = []
            # use to store only two numbers whose difference is to be found
            local_array = []
            # movement of right side
            if (self.direction.lower())[0] == "r":
                # movement of first half
                for i in range(pointer_index, len(self.request_queue)):
                    number = self.request_queue[i]
                    local_array.append(number)
                    if len(local_array) == 2:
                        difference = abs(local_array[0] - local_array[1])
                        number_array.append(difference)
                        # removing the first element of local array and retaining the second element
                        local_array.pop(0)
                # now calculating the another half
                for i in range(0,pointer_index):
                    number = self.request_queue[i]
                    local_array.append(number)
                    if len(local_array) == 2:
                        difference = abs(local_array[0] - local_array[1])
                        number_array.append(difference)
                        # removing the first element of local array and retaining the second element
                        local_array.pop(0)
                local_array.clear()
                break

            # movement of left side
            elif (self.direction.lower())[0] == "l":
                for i in range(pointer_index, -1, -1):
                    number = self.request_queue[i]
                    local_array.append(number)
                    # movement of first half
                    if len(local_array) == 2:
                        difference = abs(local_array[0] - local_array[1])
                        number_array.append(difference)
                        # removing the first element of local array and retaining the second element
                        local_array.pop(0)
                # now calculating the another half
                for i in range(len(self.request_queue)-1,pointer_index,-1):
                    number = self.request_queue[i]
                    local_array.append(number)
                    if len(local_array) == 2:
                        difference = abs(local_array[0] - local_array[1])
                        number_array.append(difference)
                        # removing the first element of local array and retaining the second element
                        local_array.pop(0)
                local_array.clear()
                break

            else:
                print("Invalid input: Please enter either \"left\" or \"right\"")
                continue
        # performing the summation of all the numbers that are present inside the number_)array
        self.seek_time = sum(number_array)


    def main(self):
        """Calling function"""
        self.cScanDiskSchedulingAlgorithm()
        # returning the value of seek time
        return self.seek_time


if __name__ == "__main__":
    c_scan = CScanAlgorithm()
    print(f"Seek Time: {c_scan.main()}")