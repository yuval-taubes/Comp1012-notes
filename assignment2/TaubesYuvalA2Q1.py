file_path = r"C:\School\uni\Comp 1012\assignment2\table1.csv"

def read_table(file_path):
    table = []
    with open(file_path, 'r') as file:
        for line in file:
            #just turning the line into a list
            row = list(map(int, line.strip().split(',')))
            table.append(row)
    print(table)

    return table

def check_horizontal_seatable_cell_greater(row, index):
    if (row[index] > row[index - 1] and row[index] > row[index + 1]):
        return True
    return False

def check_horizontal_seatable_cell_smaller(row, index):
    if (row[index] < row[index - 1] and row[index] < row[index + 1]):
        #for debugging
        # print(f"row[index] {row[index]}")
        # print(f"row[index - 1] {row[index - 1]}")
        # print(f"row[index + 1] {row[index + 1]}")
        return True
    return False

#check at a specific index
def check_vertical_seatable_cell(table, table_index, row_index):
    is_valid = False
    if (table_index == 0):
        return is_valid
    if (table_index == len(table) - 1):
        return is_valid
    is_vertical_greater = table[table_index][row_index] > table[table_index - 1][row_index] and table[table_index][row_index] > table[table_index + 1][row_index]
    is_vertical_smaller = table[table_index][row_index] < table[table_index - 1][row_index] and table[table_index][row_index] < table[table_index + 1][row_index]
    #for debugging
    # print(f"is vertical greater {is_vertical_greater}")
    # print(f"is vertical smaller {is_vertical_smaller}")

    # print(f"table[table_index][row_index] {table[table_index][row_index]}")
    # print(f"table[table_index - 1][row_index] {table[table_index - 1][row_index]}")
    # print(f"table[table_index + 1][row_index] {table[table_index + 1][row_index]}")
    
    if (is_vertical_smaller):
        is_valid = check_horizontal_seatable_cell_greater(table[table_index], row_index)
    if (is_vertical_greater):
        is_valid = check_horizontal_seatable_cell_smaller(table[table_index], row_index)
    return is_valid

def main(file_path):
    table = read_table(file_path)
    total_seatable_cells = 0
    max_seatable_cells_row = -1
    max_seatable_cells_count = -1

    for i, row in enumerate(table):
        seatable_cells_count = 0
        for j in range(len(row)):
            if check_vertical_seatable_cell(table, i, j):
                seatable_cells_count += 1

        total_seatable_cells += seatable_cells_count

        print(f"Row {i + 1} : {seatable_cells_count} Seatable Cells")

        if seatable_cells_count > max_seatable_cells_count:
            max_seatable_cells_count = seatable_cells_count
            max_seatable_cells_row = i

    print(f"\nTotal number of Seatable cells: {total_seatable_cells}")
    print(f"Row with the most Seatable cells: Row {max_seatable_cells_row + 1} with {max_seatable_cells_count} Seatable cells.")


main(file_path)