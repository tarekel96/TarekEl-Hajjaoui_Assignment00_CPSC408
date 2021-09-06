from random import randrange

class MyMatrix():
        # CLASS CONSTRUCTOR
        def __init__(self, rows, columns, column_titles, output_file):
                super().__init__()
        # CLASS FIELDS
                self.rows = rows
                self.columns = columns
                self.column_titles = column_titles
                # create 2D int list via Python list comprehension filled with random numbers btwn 0 and 1001 (exclusive)
                self.matrix = [[randrange(0, 1001) for x in range(self.columns)] for y in range(self.rows)]
                self.output_file = output_file
        
        # CLASS METHODS

                # writes the appropriate matrix to the file
        def write_matrix_in_file(self):
                inFile = open(self.output_file, 'wt') # write mode & text values
                # write title row
                col_counter = 0
                for col in self.column_titles:
                        if col_counter == len(self.column_titles) - 1:
                                inFile.write(col)
                        else:
                                inFile.write(col + ',')
                        col_counter += 1
                inFile.write('\n')
                # write elements of 2D list with commas and line spaces between rows
                for row in self.matrix:
                        curr_row = ''
                        col_counter = 0
                        for col in row:
                                curr_row += str(col)
                                if col_counter != len(self.column_titles) - 1:
                                        curr_row += ','
                                col_counter += 1
                        inFile.write(curr_row)
                        inFile.write('\n')
                inFile.close()
        # prints the given matrix to the console terminal window
        def print_matrix(self):
                for row in self.matrix:
                        curr_row = ''
                        col_counter = 0
                        for col in row:
                                curr_row += str(col)
                                if col_counter != len(row) - 1:
                                        curr_row += ','
                                col_counter += 1
                        print(curr_row)

def main():
        myMatrix = MyMatrix(400, 6, ['A', 'B', 'C', 'D', 'E', 'F'], 'data.csv')
        myMatrix.write_matrix_in_file()

if __name__ == "__main__":
    main()