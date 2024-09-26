# Employee Data Processing

This Python project processes employee data from a CSV file and performs the following operations:

1. **Remove duplicates** in the dataset.
2. **Remove decimal places** in the Age column.
3. **Convert salary** from USD to EGP.
4. **Print basic statistics**:
   - Average age of employees.
   - Median salary in EGP.
   - Male-to-female employee ratio.
5. **Save the cleaned and processed data** to a new CSV file.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Files](#files)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/employee-data-processing.git
    ```
2. Navigate to the project directory:
    ```bash
    cd employee-data-processing
    ```
3. Install the required dependencies (if any). This project primarily uses **Pandas**, so make sure you have it installed:
    ```bash
    pip install pandas
    ```

## Usage

1. Place your CSV file (e.g., `Employees.csv`) in the project directory.
2. Modify the `file_path` variable in the script to point to your file.

3. Run the Python script:
    ```bash
    python process_data.py
    ```

4. After execution, the script will output basic statistics to the console, and a new CSV file (`Updated_Employees.csv`) will be generated with the cleaned data.

## Example Output

Console output example: Average age: 34.43 Median salary (in EGP): 58615.00 Male to Female ratio: 2.50


## Files

- **Employees.csv**: Input file containing the raw employee data.
- **Updated_Employees.csv**: Output file with the processed and cleaned data.
- **process_data.py**: The main Python script that performs the data processing.



