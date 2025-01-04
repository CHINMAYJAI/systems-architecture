class OptimalPageReplacementAlgorithm:
    # Constructor which is used to initialise the arrays
    def __init__(self):
        # List to store pages in secondary storage
        self.page_secondary_storage = []
        # List to act as the main memory frame
        self.linear_queue = []

    def pageReplacementAlgorithm(self):
        """It is used to calculate the page faults and page hit in the main memory"""
        # number of pages to enter
        no_of_pages = int(input("Number of pages: "))
        for page in range(no_of_pages):
            page_number = int(input(f"Page {page+1}: "))
            self.page_secondary_storage.append(page_number)
        # number of frames to enter
        no_of_frames = int(input("Number of frames: "))
        # initializing page fault and page hit as 0
        page_fault = 0
        page_hit = 0
        # algorithm of optimal Page Replacement
        for page in range(len(self.page_secondary_storage)):
            # if page is already present in main frame then page hit occurs
            if self.page_secondary_storage[page] in self.linear_queue:
                page_hit += 1
            # if page is not present then in that case we have to load that page from secondary memory to main frame
            else:
                # incrementing page fault by 1
                page_fault += 1
                # for initial conditions when main frame is not filled
                if len(self.linear_queue) < no_of_frames:
                    self.linear_queue.append(self.page_secondary_storage[page])
                # if main frame is filled but when we have to replace the existing page to the new page
                else:
                    # Find the page in the frame that will not be used for the longest period of time in the future
                    farthest = -1
                    index_to_replace = -1
                    for i in range(len(self.linear_queue)):
                        try:
                            # Find the index of the current page in the future pages
                            index = self.page_secondary_storage[page + 1 :].index(
                                self.linear_queue[i]
                            )
                        except ValueError:
                            # If the page is not found in the future pages, set index to infinity
                            index = float("inf")
                        # Update the farthest page
                        if index > farthest:
                            farthest = index
                            index_to_replace = i
                    # If no page is found in the future pages, replace the page that is not used in the future
                    if farthest == float("inf"):
                        for i in range(len(self.linear_queue)):
                            if (
                                self.linear_queue[i]
                                not in self.page_secondary_storage[page + 1 :]
                            ):
                                index_to_replace = i
                                break
                    # Replace the page in the frame with the new page
                    self.linear_queue[index_to_replace] = self.page_secondary_storage[
                        page
                    ]
        # Print the number of page faults and page hits
        print(f"Page Fault: {page_fault}")
        print(f"Page Hit: {page_hit}")

    def main(self):
        """Function which is used to execute the pageReplacementAlgorithm"""
        self.pageReplacementAlgorithm()


# program file execution starts
if __name__ == "__main__":
    optimal = OptimalPageReplacementAlgorithm()
    optimal.main()
