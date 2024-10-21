import pandas as pd

class EditDistanceCalculator:
    def __init__(self, source: str, target: str):
        """
        Initializes the calculator with the source and target strings.
        Also initializes matrices for distances and operations.
        """
        self.source = source
        self.target = target
        self.n = len(source)
        self.m = len(target)
        
        # Initialize distance and operation matrices
        self.D = [[0 for _ in range(self.m + 1)] for _ in range(self.n + 1)]
        self.operation_matrix = [[[] for _ in range(self.m + 1)] for _ in range(self.n + 1)]

    def initialize_matrices(self):
        """Initialize the base cases for the distance and operation matrices."""
        for i in range(1, self.n + 1):
            self.D[i][0] = i
            self.operation_matrix[i][0] = ["D"]  # All deletions from the source
        
        for j in range(1, self.m + 1):
            self.D[0][j] = j
            self.operation_matrix[0][j] = ["I"]  # All insertions into the target

    def fill_matrices(self):
        """Fills the matrices for minimum edit distances and possible operations."""
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                if self.source[i - 1] == self.target[j - 1]:
                    sub_cost = 0
                    operation = "M"  # Match
                else:
                    sub_cost = 2
                    operation = "S"  # Substitution

                deletion = self.D[i - 1][j] + 1
                insertion = self.D[i][j - 1] + 1
                substitution = self.D[i - 1][j - 1] + sub_cost

                # Find the minimum cost and track the operations leading to that cost
                min_cost = min(deletion, insertion, substitution)
                self.D[i][j] = min_cost

                # Collect all operations that lead to the minimum cost
                if min_cost == deletion:
                    self.operation_matrix[i][j].append("D")  # Deletion
                if min_cost == insertion:
                    self.operation_matrix[i][j].append("I")  # Insertion
                if min_cost == substitution:
                    self.operation_matrix[i][j].append(operation)  # Match or Substitution

    def compute_edit_distance(self) -> int:
        """Main method to compute the edit distance between source and target."""
        self.initialize_matrices()
        self.fill_matrices()
        return self.D[self.n][self.m]

    def backtrack_path(self) -> list:
        """
        Backtrack through the distance matrix to find the sequence of operations
        that results in the minimum edit distance.
        """
        i, j = self.n, self.m
        path = []
        
        while i > 0 or j > 0:
            if i > 0 and j > 0 and self.source[i - 1] == self.target[j - 1]:
                path.append(f"Match: {self.source[i - 1]}")
                i, j = i - 1, j - 1
            elif i > 0 and self.D[i][j] == self.D[i - 1][j] + 1:
                path.append(f"Delete: {self.source[i - 1]}")
                i -= 1
            elif j > 0 and self.D[i][j] == self.D[i][j - 1] + 1:
                path.append(f"Insert: {self.target[j - 1]}")
                j -= 1
            else:
                path.append(f"Substitute: {self.source[i - 1]} -> {self.target[j - 1]}")
                i, j = i - 1, j - 1
        
        path.reverse()  # Reverse the path to get the correct order
        return path

    def get_operation_matrix_as_dataframe(self) -> pd.DataFrame:
        """
        Convert the operation matrix to a Pandas DataFrame for better display and analysis,
        adding the source and target strings to the respective rows and columns.
        """
        # Adding target as row labels and source as column labels
        df = pd.DataFrame(self.operation_matrix)
        df.columns = [''] + list(self.source)  # First column empty, then source characters
        df.index = [''] + list(self.target)    # First row empty, then target characters
        return df

    def save_operation_matrix_to_excel(self, filename: str = 'edit_distance_operations.xlsx'):
        """
        Save the operation matrix to an Excel file with source and target characters included.
        """
        df = self.get_operation_matrix_as_dataframe()
        df.to_excel(filename, index=True)
        print(f"Operation matrix with source and target saved to {filename}")

    def print_operation_matrix(self):
        """Prints the operation matrix using Pandas for a cleaner display."""
        df = self.get_operation_matrix_as_dataframe()
        print("\nOperation Matrix (lists of all possible operations in each cell):")
        print(df)


# Main function to demonstrate the class usage
def main():
    source = "intention"
    target = "execution"

    # Create an instance of EditDistanceCalculator
    calculator = EditDistanceCalculator(source, target)

    # Compute the minimum edit distance
    min_distance = calculator.compute_edit_distance()

    # Get the backtracking path
    optimal_path = calculator.backtrack_path()

    # Output the results
    print(f"Source: {source}\nTarget: {target}\nMinimum Edit Distance: {min_distance}")
    print("\nOptimal Path:")
    for step in optimal_path:
        print(step)

    # Print the operation matrix in a clean format
    calculator.print_operation_matrix()

    # Optionally, save the matrix to an Excel file
    calculator.save_operation_matrix_to_excel()


if __name__ == "__main__":
    main()
