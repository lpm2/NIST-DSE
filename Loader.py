import csv

rpath = '\\57_hypothyroid\\TRAIN\\dataset_TRAIN\\tables\\0'


# Divides dataset into partitions allows us to test
# a configurable section of dataset to avoid overfitting
NumberPartitions = 10
partitions = [1,1,1,1,1,1,1,1,1,1]
testPart = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
Data = []
with open("C:/Users\mraul/Documents/MachineLearning/NIST-DSE/57_hypothyroid/TRAIN/dataset_TRAIN/tables/learningData.csv") as csv_file:
    csv_parser = csv.reader(csv_file, delimiter=',')
    linenum = 0
    for row in csv_parser:
        if linenum == 0:
            print(f'Column names are {", ".join(row)}')
            linenum+=1

        print(tuple(row))
        Data+=tuple(row)


# partitions get removed based on partitions mask
NewData= []
#Data = testPart
offset = int(len(Data)/NumberPartitions)


for i in range(0,NumberPartitions):
        if partitions[i] > 0:
            NewData += Data[(i*offset):((i+1)*offset)]

#print(len(Data), len(NewData))
#print(Data,offset)

Data = NewData
