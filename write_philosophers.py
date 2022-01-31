# this program writes 3 lines of date
# to a file.
def main():
    # Open a file named philosophers.txt
    outfile = open("philosophers.txt", "w")
    # write the names of the three philosophers to the file

    outfile.write("John Locke" + "\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")

    # close the file.
    outfile.close()


def add_my_name():
    outfile = open("philosophers.txt", "a")

    outfile.write("Reese Alexander\n")

    outfile.close()


main()
add_my_name()
