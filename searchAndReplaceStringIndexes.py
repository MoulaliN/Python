def replace_spaces(input_string):
    indices_to_replace = [3,7,13,42,44,75,79,110,116,147,153,155,157,166,175,179,210,214,222,230,261,264,274,282,291,300,309,318,327,329,331,333,401,403,407,409,413,444]
    
    # Convert the string to a list of characters for easy manipulation
    char_list = list(input_string)
    
    # Replace spaces at specified indices with '|'
    for index in indices_to_replace:
        if index < len(char_list):
            char_list[index] = '|'
    
    # Convert the list back to a string
    modified_string = ''.join(char_list)
    
    return modified_string

def process_file(file_path):
    with open(file_path, 'r') as file:
        # Read each line from the file
        lines = file.readlines()

        # Process each line
        modified_lines = [replace_spaces(line.strip()) for line in lines]

    return modified_lines

# Example usage:
input_file_path = 'C://Users//0025T7744//Downloads//pim_item.FILE'
output_file_path = 'C://Users//0025T7744//Downloads//pim_item_converted.txt'

# Process the file and get modified lines
modified_lines = process_file(input_file_path)

# Write modified lines to a new file
with open(output_file_path, 'w') as output_file:
    output_file.write('\n'.join(modified_lines))

print(f"Lines processed and written to {output_file_path}")
