def get_valid_rows(matrix):
    def is_valid_row(row):
        """Check if a row is strictly increasing or decreasing with valid differences."""
        if not row:
            return False
        increasing = all(1 <= int(row[i + 1]) - int(row[i]) <= 3 for i in range(len(row) - 1))
        decreasing = all(1 <= int(row[i]) - int(row[i + 1]) <= 3 for i in range(len(row) - 1))
        return increasing or decreasing

    valid_rows = []
    for row in matrix:
        if is_valid_row(row):
            valid_rows.append(row)
        else:
            # Check all possible sub-rows by removing one element
            for i in range(len(row)):
                sub_row = row[:i] + row[i + 1:]  # Create sub-row by excluding the element at index i
                if is_valid_row(sub_row):
                    valid_rows.append(sub_row)
                    break  # Stop checking once a valid sub-row is found
    return valid_rows


def day2():
    # Open input file and collect data
    with open("day02/input.txt", "r") as f:
        lines = f.readlines()

    # Get reports as a list of rows
    reports = [line.split() for line in lines]

    # Get valid (safe) reports
    safe_reports = get_valid_rows(reports)

    # Output results
    print("Safe reports:", len(safe_reports))
    return safe_reports

day2()