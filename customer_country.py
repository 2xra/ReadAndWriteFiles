import csv

customers = open("customers.csv", "r")

customer_file = csv.reader(customers, delimiter=",")
output = open("customer_country.csv", "w")


count = 0
for meme in customer_file:
    output.write(
        meme[1].__str__() + "," + meme[2].__str__() + "," + meme[4].__str__() + "\n"
    )
    count += 1

print(count)

customers.close()
output.close()
