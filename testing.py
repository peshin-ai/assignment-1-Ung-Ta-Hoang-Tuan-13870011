import csv


def Quit():
    pass


def display():
    i = 0

    for row in rows:
        if row[3] == 'u':
            print(str(i) + '.{:^3}'.format('*') + ' {:40}'.format(row[0]) + '{:2}'.format('-') + '{:>4}'.format(
                row[1]) + ' ({})'.format(row[2]))
        else:
            print(str(i) + '.{:^3}'.format(' ') + ' {:40}'.format(row[0]) + '{:2}'.format('-') + '{:>4}'.format(
                row[1]) + ' ({})'.format(row[2]))
        i += 1


def ReadFile():
    global rows, LineCount, RawFile
    # inital varible and array
    rows = []
    LineCount = 0
    # reading the csv file
    with open('movies.csv', 'r') as RawFile:
        Csv_File = csv.reader(RawFile, delimiter=',')

        # changing data in csv file -> array
        # count the line in
        for row in Csv_File:
            rows.append(row)
            LineCount += 1


def main():
    """..."""
    print("Movies To Watch 1.0 - by Ung Ta Hoang Tuan")

    ReadFile()
    print("{} movies loaded".format(LineCount))
    display()


if __name__ == '__main__':
    main()
