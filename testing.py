import csv

def display():
    for i in range(LineCount):
        print(rows[i])

def main():
    """..."""
    print("Movies To Watch 1.0 - by Ung Ta Hoang Tuan")

    global rows, LineCount
    rows = []
    RawFile = open('movies.csv', 'r')
    Csv_File = csv.reader(RawFile, delimiter=',')
    LineCount = 0

    for row in Csv_File:
        rows.append(row)
        LineCount += 1

    print("{} movies loaded".format(LineCount))
    display()
    RawFile.close()


if __name__ == '__main__':
    main()
