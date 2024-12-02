def get_valid_rows(matrix):
    valid_rows = []
    for row in matrix:
        if is_valid_row(row):
            valid_rows.append(row)
    return valid_rows

def is_valid_row(row):
    # Check if the row is strictly increasing or decreasing with valid differences
    increasing = all(1 <= int(row[i + 1]) - int(row[i]) <= 3 for i in range(len(row) - 1))
    decreasing = all(1 <= int(row[i]) - int(row[i + 1]) <= 3 for i in range(len(row) - 1))
    return increasing or decreasing


def day2():

    # Open input file and collect data
    f = open("day02/input.txt", "r")
    lines = f.readlines()
    f.close()

    # Get reports
    reports = []
    for line in lines:
        reports.append(line.split())
    
    # Get number of safe reports
    safe_reports = get_valid_rows(reports)

    print(len(safe_reports))
    return (safe_reports)