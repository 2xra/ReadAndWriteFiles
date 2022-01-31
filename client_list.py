def main():

    infile = open("clients.txt", "r")

    # line = infile.readline().rstrip("\n")
    linenum = 1
    # while line != "":
    #    print(linenum.__str__() + ". " + line)
    #    linenum += 1
    #    line = infile.readline().rstrip("\n")
    # infile.close

    # another version
    for client in infile:
        print(linenum, ". ", client.rstrip("\n"), sep="")
        linenum += 1
    infile.close


main()
