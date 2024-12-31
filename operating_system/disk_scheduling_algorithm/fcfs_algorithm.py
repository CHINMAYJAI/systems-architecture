class FifoPageReplacement:
    def __init__(self):
        # Initialize an empty list to store the input disk positions
        self.array_strings = []

    def stringsInput(self):
        try:
            # Prompt user for the number of disk positions to enter
            no_of_strings = int(input("How many disk positions do you want to enter?\n"))
        except Exception as e:
            # Handle invalid input for number of disk positions
            print("Number of disk positions must be positive")
            self.stringsInput()
        if no_of_strings <= 0:
            # Handle non-positive number of disk positions
            print("Number of disk positions cannot be less than or equals to zero")
            self.stringsInput()
        else:
            number = 0
            while number < no_of_strings:
                # Prompt user to enter each disk position
                try:
                    disk_position = float(input(f"Disk Position {number+1}: "))
                except Exception as e:
                    # Handle invalid disk position input
                    print("Disk position must be in integer or in decimal")
                    continue
                if disk_position in self.array_strings:
                    # Ensure disk positions are unique
                    print("Disk position must be different!")
                    continue
                self.array_strings.append(disk_position)
                number += 1
            while True:
                # Prompt user to enter the head pointer
                try:
                    head_pointer = float(input("Head Pointer: "))
                except Exception as e:
                    # Handle invalid head pointer input
                    print("Head pointer must be in integer or in decimal")
                    continue
                if head_pointer < 0 or head_pointer in self.array_strings:
                    # Validate head pointer input
                    print(
                        "Head Pointer cannot be negative and should not be in head pointer"
                    )
                    continue
                else:
                    break
            summation_of_disk_position = 0
            for pointer in range(len(self.array_strings)):
                difference = 0
                if pointer == 0:
                    # Calculate difference for the first disk position
                    difference = abs(head_pointer - self.array_strings[pointer])
                    summation_of_disk_position += difference
                else:
                    # Calculate difference for subsequent disk positions
                    difference = abs(
                            self.array_strings[pointer - 1]
                            - self.array_strings[pointer]
                        )
                    summation_of_disk_position += difference
        # Output the total head movement
        print(f"Total Head Movement: {summation_of_disk_position}")

    def main(self):
        # Call the stringsInput method
        self.stringsInput()


if __name__ == "__main__":
    # Create an instance of FifoPageReplacement and call the main method
    fifo = FifoPageReplacement()
    fifo.main()
