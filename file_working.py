from datetime import datetime, date
from pathlib import Path

def read_from_file(filename):
  """Reads content from a file and returns it."""
  with open(filename, 'r', encoding='utf-8') as file:
    return file.read()

def read_lines_from_file(filename):
  """Reads lines from a file and returns them as a list."""
  with open(filename, 'r', encoding='utf-8') as file:
    return [line.strip() for line in file]

def write_to_file(filename, content):
  """Writes content to a file. replacing any existing content."""
  with open(filename, 'a', encoding='utf-8') as file:
    file.write(content)

def read_binary_file(filename):
  """Reads content from a binary file and returns it."""
  with open(filename, 'r+b') as file:
    return file.read() # Read the entire binary file


def copy_file(source_filename, destination_filename):
  """Copies content from source file to destination file."""
  with open(source_filename, 'r', encoding='utf-8') as source_file:
    content = source_file.read()
  with open(destination_filename, 'w', encoding='utf-8') as dest_file:
    dest_file.write(content)
  print(f"Copied content from '{source_filename}' to '{destination_filename}'.")

def path_components(path_str):
  """Returns the components of a file path as a list."""
  path = Path(path_str)
  return list(path.parts)

dict_sum = {
  "description": "Totals for the file",
  "sum_of_amounts": 0.0,
  "sum_of_fee": 0.0,
}

def to_number(value:str, default: int | float = 0) -> int | float:
  """Converts a string to a number (int or float). Returns default if conversion fails."""
  try:
    return int(value)
  except ValueError:
    try:
      return float(value)
    except ValueError:
      return default


def main():

  while True:
  
    MENU = """\
    \nChoose an action:
      r - read the whole file
      w - write to the file
      l - read lines from the file
      b - read a binary file
      c - copy a file
      p - show path components
      q - exit \n
    > """
    action = input(MENU).strip().lower()

    if action == 'q':
      print("Exiting the program.")
      return
    
    elif action == 'r':

      try:
        filename = input("Enter the filename: ")
        print("\n", read_from_file.__doc__)
        content = read_from_file(filename)
        print("File content:")
        print(content)
      except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    
    elif action == 'l':

      try:
        filename = input("Enter the filename: ")
        print("\n", read_lines_from_file.__doc__)
        lines = read_lines_from_file(filename)
        print(f"Lines in '{filename}':" )
        print(f"Total lines: {len(lines)}")
        print(f"First line: {lines[0] if lines else 'No lines in file'}")
        print("\n File lines:")
        amount = 0.0
        fees = 0.0
        for line in lines:
          amount = amount + to_number(line.split(",")[3], 0.0)  # Assuming the amount is in the third column (index 2) of a CSV line
          fees = fees + to_number(line.split(",")[4], 0.0)  # Assuming the fee is in the fourth column (index 3) of a CSV line
          print(line.strip(), "\n")

        print("\nCalculating totals..." )
        dict_sum["sum_of_amounts"] = amount 
        dict_sum["sum_of_fee"] = fees
        print("Totales!", dict_sum)
        print(f"Total Amount: {dict_sum['sum_of_amounts']}")
        print(f"Total Fee: {dict_sum['sum_of_fee']}")

      except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

    elif action == 'w':

      try:
        filename = input("Enter the filename: ")
        print("\n",write_to_file.__doc__)
        content = input("Enter the content to write to the file: ")
        write_to_file(filename, content + "\n")  # Adding a newline at the end of the content
        print(f"Content written to '{filename}'.")
      except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

    elif action == 'b':
      
      try:
        filename = input("Enter the filename: ")
        print("\n",read_binary_file.__doc__)
        binary_content = read_binary_file(filename)
        print(f"Binary content of '{filename}':")
        print(binary_content)
        print(f"Type: {type(binary_content)}" )

      except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
      except Exception as e:
        print(f"An error occurred while reading the binary file: {e}")

    elif action == 'c':
      try:
        source_filename = input("Enter the source filename: ")
        destination_filename = input("Enter the destination filename: ")
        print("\n",copy_file.__doc__)
        copy_file(source_filename, destination_filename)
      except FileNotFoundError:
        print(f"The file '{source_filename}' does not exist.")
      except Exception as e:
        print(f"An error occurred while copying the file: {e}")

    elif action == 'p':
      try:
        path_str = input("Enter the file path: ")

        base_dir = Path(__file__).resolve().parent 
        path = base_dir / path_str
        if not path.is_file():
          print(f"'{path_str}' does not exist.")
          return
        else:
          print(path.read_text(encoding="utf-8"))

        print("\n",path_components.__doc__)
        components = path_components(path_str)
        print(f"Path components of '{path_str}':")
        for component in components:
          print(component)

        #base_dir = Path.cwd()
        # Join paths using the / operator
        # This works on Windows, Mac, and Linux automatically
        logs_dir = base_dir / "app_data" / "logs"
        error_log = logs_dir / "errors.txt"

        print(f"Base Directory: {base_dir}")
        print(f"Full Log Path:  {error_log}")

        # Define a path (it doesn't need to exist to be inspected)
        print(f"Full Name: {path.name}")
        print(f"Stem:      {path.stem}")
        print(f"Suffix:    {path.suffix}")
        print(f"Parent:    {path.parent}")


      except Exception as e:
        print(f"An error occurred while processing the path: {e}")

if __name__ == "__main__":
  main()