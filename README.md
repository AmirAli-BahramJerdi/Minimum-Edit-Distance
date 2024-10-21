
# Minimum Edit Distance Calculator 

This project calculates the minimum edit distance between two strings using dynamic programming. It generates a matrix that shows the possible operations (insertion, deletion, substitution, match) for converting the source string into the target string. The project also exports the operation matrix to an Excel file for better visualization. 📊

## Project Structure 🗂

- `main3.py`: Main Python script that implements the minimum edit distance algorithm and generates the operation matrix.
- `edit_distance_operations.xlsx`: Excel file containing the operation matrix with all possible edit operations.
- `requirements.txt`: List of dependencies required to run the project.

## Features 🌟

- Calculates the **minimum edit distance** between two strings using dynamic programming.
- **Backtracking** functionality to display the optimal sequence of operations (insert, delete, substitute, match).
- Exports the **operation matrix** to an Excel file, including all possible operations for each cell.
- Displays the source and target strings in the matrix to clarify the operations visually. 🎯

## Getting Started 🚀

### Prerequisites 🛠

To run this project, make sure you have Python 3 installed on your system. You also need to install the required Python libraries listed in `requirements.txt`.

### Installing Dependencies 📦

1. Clone or download the project repository to your local machine.
2. Navigate to the project directory and run the following command to install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

This will install the necessary libraries, including **pandas** and **openpyxl**.

### Running the Project 🏃‍♂️

1. Open a terminal in the project directory.
2. Run the following command to execute the script and calculate the edit distance between two strings (defined in the code):

   ```bash
   python main3.py
   ```

3. After running the script:
   - The minimum edit distance will be printed on the console.
   - The optimal sequence of operations will be shown.
   - An Excel file named `edit_distance_operations.xlsx` will be generated, containing the operation matrix.

### Example 💡

#### Input:

```plaintext
Source: intention
Target: execution
```

#### Output:

- **Minimum Edit Distance**: `8`
- **Optimal Path**:

  ```
  Insert: e
  Insert: x
  Delete: i
  Delete: n
  Delete: t
  Match: e
  Insert: c
  Insert: u
  Delete: n
  Match: t
  Match: i
  Match: o
  Match: n
  ```

- **Operation Matrix**: An Excel file with all possible operations (`Insert`, `Delete`, `Substitute`, `Match`) in each cell, along with the source and target characters.

## Requirements 📋

The project uses the following libraries:

- `pandas`: For handling data and exporting the operation matrix to Excel.
- `openpyxl`: For creating and writing to Excel files.

You can install the required libraries using:

```bash
pip install -r requirements.txt
```

## Project Files 📁

- **`main3.py`**: Python script that calculates the minimum edit distance and handles file exports.
- **`edit_distance_operations.xlsx`**: Generated Excel file showing the operation matrix for the given source and target strings.
- **`requirements.txt`**: List of required Python libraries for the project.

## Future Improvements 🚀

- Add support for custom input strings from the user via the command line or a GUI.
- Enhance the visualization of the operation matrix with conditional formatting in Excel.
- Add support for more advanced edit distance algorithms.


Happy coding! 😊
