import random


class InputGenerator:
    """
    This class generates the test input for Minesweeper based on values
    from its own input file and prints to provided output file
    """
    def __init__(self, input_file, output_file):
        self._input_file = input_file
        self._output_file = output_file
        self.create_test_data()

    def create_test_data(self):
        """This method generates the test input for Minesweeper"""
        # set up i/o files
        input_file = open(self._input_file, "r")
        output_file = open(self._output_file, "w")

        # get dimensions
        dimensions = input_file.readline().strip()

        while dimensions != "END":
            # process row/col values and print to output
            rows, cols = dimensions.split()
            output_file.write(dimensions + "\n")

            # the row/col values are strings that should be ints
            rows = int(rows)
            cols = int(cols)

            # get % of mines to be used
            chance_of_mines = input_file.readline().strip()

            # print minefield to output
            for n in range(rows):
                for m in range(cols):
                    output_file.write(self.generate_mine(int(chance_of_mines)))
                output_file.write("\n")

            # process new row/col values
            dimensions = input_file.readline().strip()

        # close i/o files
        input_file.close()
        output_file.close()

    @staticmethod
    def generate_mine(chance_of_mines):
        """
        This method determines if the current cell should be a bomb
        :param chance_of_mines: int from 1-100
        :return: String representing a bomb or non-bomb cell
        """
        return "*" if random.randint(1, 100) <= chance_of_mines else "."


if __name__ == '__main__':
    generator = InputGenerator("test_data.txt", "mine_data.txt")
