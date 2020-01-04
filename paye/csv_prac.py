import csv

# with open('data.csv','w',newline="") as fd:
#     csv_writer = csv.writer(fd, delimiter=',')
#     csv_writer.writerow(['Name','Age','Class'])
#     csv_writer.writerow(['Amjad',25,'AI'])
#     csv_writer.writerow(['Asad',20,'AI'])
#     csv_writer.writerow(['Sania',26,'AI'])

# with open('data.csv','r') as fd:
#     csv_reader = csv.reader(fd)
#     for line in csv_reader:
#         print(line)

with open("data.csv") as fd:
        word_reader = csv.reader(fd)
        words = []
        for each_line in word_reader:
            words += each_line

print(words)