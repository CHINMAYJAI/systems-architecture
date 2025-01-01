class FifoPageReplacementAlgorithm:
    def __init__(self):
        self.linear_queue = []
        self.page_secondary_storage = []
    
    def pageReplacementAlgo(self):
        # Get the number of pages from the user
        try:
            no_of_pages = int(input("Number of pages: "))
            if no_of_pages <= 0:
                print("Number of pages must be positive and non-zero")
                self.pageReplacementAlgo()
        except Exception as e:
            print("Enter Positive Integer Value")
            self.pageReplacementAlgo()
        
        # Get the page numbers from the user
        for page in range(no_of_pages):
            page_number = float(input(f"Page {page+1}: "))
            self.page_secondary_storage.append(page_number)
        
        page_fault = 0
        page_hit = 0
        
        # Get the number of frames from the user
        while True:
            try:
                no_of_frames = int(input("Number of Frames: "))
                if no_of_frames <= 0:
                    print("Number of frames must be positive and non-zero")
                else:
                    break
            except Exception as e:
                print("Number of frames must be positive integer and non-zero")
        
        pointer = 1
        self.linear_queue.append("#")
        
        # Process each page in the secondary storage
        for page in range(len(self.page_secondary_storage)):
            if self.page_secondary_storage[page] in self.linear_queue:
                page_hit += 1
            else:
                page_fault += 1
                if len(self.linear_queue) != no_of_frames + 1:
                    self.linear_queue.append(self.page_secondary_storage[page])
                else:
                    self.linear_queue[pointer] = self.page_secondary_storage[page]
                    if pointer == no_of_frames:
                        pointer = 1
                    else:
                        pointer += 1
            self.linear_queue.remove("#")
            print(self.linear_queue)
            self.linear_queue.insert(0, "#")
        
        # Print the results
        print(f"Page Fault: {page_fault}")
        print(f"Page Hit: {page_hit}")
    
    def main(self):
        self.pageReplacementAlgo()

if __name__ == "__main__":
    fifo_pagereplacement_algo = FifoPageReplacementAlgorithm()
    fifo_pagereplacement_algo.main()