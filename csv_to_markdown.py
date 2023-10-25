# This script is for copy/pasting results from Datagrip (or similar IDE) into a MD table format.
# This is because sometimes a full CSV export is overkill and I don't want to rewrite or run a query.

import csv

def csv_to_markdown(csv_string):

    # read the CSV
    csv_reader = csv.reader(csv_string.splitlines())

    next(csv_reader, None)

    header = next(csv_reader)
    if not header:
        return ""
    
    num_columns = len(header)

    markdown_table = "| " + " | ".join(header) + "|\n"

    markdown_table += "| " + " | ".join([":---: "] * num_columns)+ " |\n"

    for row in csv_reader:
        if any(row):
            markdown_table += "| " + " | ".join(row) + " |\n"

    return markdown_table

csv_string = """
# Add your copy/pasted text starting here with the header.
"""

markdown_table = csv_to_markdown(csv_string)

print(markdown_table)