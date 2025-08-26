import csv
import sys
import cs50

def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Please enter suitable command")
        return 1

    # TODO: Read database file into a variable
    filename = sys.argv[1]
    rows = []
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            str_headers = reader.fieldnames[1:]
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print(f"Could not open {filename}")
        return 1

    # TODO: Read DNA sequence file into a variable
    filename2 = sys.argv[2]
    try:
        with open(filename2) as file:
            seq = file.read().strip()
    except FileNotFoundError:
        print(f"Could not open {filename2}. ")
        return 1
    
    # TODO: Find longest match of each STR in DNA sequence
    str_count = {}
    for str in str_headers:
        str_count[str] = longest_match(seq, str)

    # TODO: Check database for matching profiles
    for row in rows:
        if all(str_count[str] == int(row[str]) for str in str_headers):
            print(row['name'])
            return 0
    print("No match")
    return 0


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

main()
