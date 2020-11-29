"""
Replace the contents of this module docstring with your own details
Name: Ung Ta Hoang Tuan
Date started: 29/11/2020
GitHub URL: https://github.com/peshin-ai
"""
import csv
#def Quit():

# def Process(char):
#     if char == "L":
#         # TODO: changing it
#         for i in range():

def Option():
    char = input()
    while char.upper() not in ["L","A","W","Q"]:
        char = input()
    #Process(char)

def Menu():
    print("L - List movies")
    print("A - Add new movie")
    print("W - Watch a movie")
    print("Q- Quit")
    Option()

def main():
    """..."""
    print("Movies To Watch 1.0 - by Ung Ta Hoang Tuan")
    # TODO changing it
    RawFile = open('movies.csv', 'r')
    Csv_File = csv.reader(RawFile, delimiter=',')

    Line = len(list(Csv_File))
    print("{} movies loaded".format(Line))
    Menu()

    RawFile.close()
if __name__ == '__main__':
    main()

