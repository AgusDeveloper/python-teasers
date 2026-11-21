#The read .read() method consumes the entire content of the file and returns it as a string.
#It can be dangerous for large files as it can consume a lot of memory.
def read_file_content():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            #Dangerous for large files as it can consume a lot of memory
            content = file.read() #Read the entire content of the file
            print("FileContent: \n", content, " \n ")
        
        #print(f"Is the file closed now? {filename.closed}")
            
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#for reading large files, it is better to read the file line by line using a loop.
#Python translate all-platform newline characters to '\n' when reading files in text mode.
def read_file_by_lines():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            i = 1
            for line in file:
                #line = line.strip()  # Remove leading/trailing whitespace and newline characters
                cleaned_line = line.strip()  # Remove leading/trailing whitespace and newline characters
                print(f"Line {i}: {cleaned_line}")  # Print each line with a line number
                i += 1

        #print(f"Is the file closed now? {filename.closed}")
            
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#Reading staructured data from a file can be done using the csv module in Python. The csv module provides functionality to read and write CSV files, which are commonly used for storing tabular data.
def read_csv_file():
    import csv
    filename = input("Enter the CSV filename: ")
    try:
        with open(filename, mode='r', encoding='utf-8') as csv_file:
            total_amount = 0.0  # Initialize a variable to keep track of the total amount
            #DictReader reads the CSV file and maps the data into a dictionary where the keys are the column headers and the values are the corresponding data for each row.
            reader = csv.DictReader(csv_file)
            #reader reads one line from the file and returns it as a dictionary where the keys are the column headers and the values are the corresponding data for that row.   
            for row in reader:
                print(row)  # Print each row as a list of values
                amount = row["amount"]
                total_amount = total_amount + float(amount)  # Convert the amount to a float for calculations

            print(f"Amount: {total_amount}")  # Print the total amount after each row is processed

    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#read_file_content()
#read_file_by_lines()
read_csv_file()