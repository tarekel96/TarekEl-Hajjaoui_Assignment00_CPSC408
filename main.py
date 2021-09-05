from random import randrange

class MyMatrix():
        def __init__(self, rows, columns, matrix):
                super().__init__()
                self.rows = rows
                self.columns = columns
                self.matrix = [[randrange(0, 1001) for x in range(columns)] for y in range(rows)]
matrix_columns = ['A', 'B', 'C', 'D', 'E', 'F']

# create 2D int list with the first parameter being number of rows and second being number of columns
def create_matrix(rows = 400, columns = 6):
        matrix = [[randrange(0, 1001) for x in range(columns)] for y in range(rows)]
        return matrix

# prints the given matrix to the console terminal window
def print_matrix(matrix):
        for row in matrix:
                curr_row = ''
                col_counter = 0
                for col in row:
                        curr_row += str(col)
                        if col_counter != len(row) - 1:
                                curr_row += ','
                        col_counter += 1
                print(curr_row)

# writes the appropriate matrix to the file
def write_matrix_in_file(file):
        inFile = open(file, 'wt') # write mode & text values
        # write title row
        for col in matrix_columns:
                inFile.write(col)
        # create 2D int list 
        matrix = create_matrix(400, 6) # create a matrix with 400 rows and 6 columns
        # write elements of 2D list with commas and line spaces between rows
        for row in matrix:
                curr_row = ''
                col_counter = 0
                for col in row:
                        curr_row += str(col)
                        if col_counter != 5:
                                curr_row += ','
                        col_counter += 1
                inFile.write(curr_row)
                inFile.write('\n')
        inFile.close()

matrix = create_matrix(3,2)
print(len(matrix[0]))
print(matrix)
print_matrix(matrix)
write_matrix_in_file('data.csv')
