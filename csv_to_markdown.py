import csv

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def csv_to_markdown(csv_string, skip_commas_columns=None):
    # Read the CSV
    csv_reader = csv.reader(csv_string.splitlines())

    next(csv_reader, None)

    header = next(csv_reader)
    if not header:
        return ""

    num_columns = len(header)

    markdown_table = "| " + " | ".join(header) + "|\n"

    markdown_table += "| " + " | ".join([":---:"] * num_columns) + " |\n"

    # List of column names where commas should not be added
    skip_commas_columns = [col.strip().lower() for col in skip_commas_columns] if skip_commas_columns else []

    for row in csv_reader:
        if any(row):
            formatted_row = []
            for i, cell in enumerate(row):
                # Check if the column name is in the skip_commas_columns list
                if header[i].strip().lower() in skip_commas_columns:
                    formatted_row.append(cell)
                elif is_numeric(cell):
                    # Check for a decimal point in the original value
                    if '.' in cell:
                        formatted_row.append(f"{float(cell):,}")
                    else:
                        formatted_row.append(f"{int(cell):,}")
                else:
                    # Replace empty values with "null"
                    formatted_row.append("null" if cell.strip() == "" else cell)
            markdown_table += "| " + " | ".join(formatted_row) + " |\n"

    return markdown_table

csv_string = """
name, item, number, ID, version
jay, bird, 1, , 1234567
crow, bird, , 21213213, 9876543
bluebird, bird, 200000, ,
3423423324, 2342343223, 234232.5, 32432423, 8888888
"""

# List of column names where commas should not be added (as a list)
skip_commas_columns = ["ID", "version"]

markdown_table = csv_to_markdown(csv_string, skip_commas_columns=skip_commas_columns)

# Replace empty values with "null"
markdown_table = markdown_table.replace("|   |", "| null |")

print(markdown_table)
