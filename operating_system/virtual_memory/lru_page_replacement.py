class LRUPageReplacementAlgorithm:
    def __init__(self):
        self.linear_queue = []
        self.page_secondary_storage = []

    def pageReplacementAlgo(self):
        no_of_pages = int(input("Number of pages: "))
        for i in range(no_of_pages):
            page = int(input(f"Page Number {i + 1}: "))
            self.page_secondary_storage.append(page)

        page_fault, page_hit = 0, 0
        no_of_frames = int(input("Number of frames: "))
        local_list = []

        for page in range(len(self.page_secondary_storage)):
            current_page = self.page_secondary_storage[page]
            # Page Hit
            if current_page in self.linear_queue:
                page_hit += 1
                continue

            # Page Fault
            page_fault += 1
            if len(self.linear_queue) < no_of_frames:
                self.linear_queue.append(current_page)
                continue

            # backward traversal
            encounter_variable = 0
            for j in range(page - 1, -1, -1):
                if encounter_variable == no_of_frames:
                    break
                element = self.page_secondary_storage[j]
                if element in self.linear_queue and element not in local_list:
                    local_list.append(element)
                    encounter_variable += 1

            print(f"Local list after backward traversal: {local_list}")
            replaceable_element = local_list[-1]
            print(f"Replacing: {replaceable_element} with {current_page}")

            # Replace in linear_queue
            index = self.linear_queue.index(replaceable_element)
            self.linear_queue[index] = current_page
            local_list.clear()

        print(f"Page Fault: {page_fault}")
        print(f"Page Hit: {page_hit}")

    def main(self):
        self.pageReplacementAlgo()


if __name__ == "__main__":
    lru = LRUPageReplacementAlgorithm()
    lru.main()
