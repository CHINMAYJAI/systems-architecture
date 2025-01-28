# Virtual Memory

This repository contains implementations of various page replacement algorithms as part of the `operating_system` repository, which is nested under the `system_architecture` parent repository.

## Contents
- `fifo`: First-In-First-Out (FIFO) page replacement algorithm
- `lru`: Least Recently Used (LRU) page replacement algorithm
- `optimal`: Optimal page replacement algorithm

## Page Replacement Algorithms

### First-In-First-Out (FIFO)
The FIFO page replacement algorithm replaces the oldest page in memory that has been there the longest. It operates in a cyclic manner where the first loaded page is the first to be replaced.

### Least Recently Used (LRU)
The LRU page replacement algorithm replaces the page that has not been used for the longest period of time. It operates on the principle of temporal locality, assuming that pages used recently will be used again soon.

### Optimal
The Optimal page replacement algorithm replaces the page that will not be used for the longest period of time in the future. It provides the best performance but requires future knowledge of the reference string.

## How to Use
1. Clone the `system_architecture` repository:

```bash
   git clone https://github.com/CHINMAYJAI/system_architecture.git
```

2. Navigate to the `virtual_memory` directory:
```bash
cd system_architecture/operating_system/virtual_memory
```

3. Run the algorithms as per the instructions provided in their respective directories.

## Contributing
Contributions are welcome! Please fork the repository and open a pull request with your changes.

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to all the contributors and the open-source community for their support.

## Contribution

Feel free to fork the repository and submit a pull request if you'd like to improve this project. Suggestions and feedback are welcome!

## Author

[Chinmay Jain](https://github.com/CHINMAYJAI)









