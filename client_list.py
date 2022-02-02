def main():

    infile = open("clients.txt", "r")

    # line = infile.readline().rstrip("\n")
    count = 1
    # while line != "":
    #    print(count.__str__() + ". " + line)
    #    count += 1
    #    line = infile.readline().rstrip("\n")
    # infile.close

    # another version
    for client in infile:
        print(count, ". ", client.rstrip("\n"), sep="")
        count += 1
    infile.close


main()
