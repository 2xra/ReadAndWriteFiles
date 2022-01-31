def main():
    # read a file named philosophers.txt
    infile = open("philosophers.txt", "r")
    # read the names of the three philosophers to the file

    # file_contents = infile.read()
    line1 = infile.readline().rstrip("\n")
    line2 = infile.readline().rstrip("\n")
    line3 = infile.readline().rstrip("\n")

    # print the file contents to console.
    # print(file_contents)
    print(line1)
    print(line2)
    print(line3)

    # close the file contents.
    infile.close()


main()
