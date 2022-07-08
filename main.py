import random

data = []
firstDie = 0
secondDie = 0
bucket = []


def rollDie():
    global firstDie, secondDie
    firstDie = random.randint(1, 6)
    secondDie = random.randint(1, 6)


def initArray(data, firstDie, secondDie):
    data.append(firstDie + secondDie)


def sortArray(data):
    for index in range(1, len(data)):
        if data[index] > data[index-1]:
            data.insert(index - 1, data[index])
            data.pop(index + 1)
            for i in range(1, index):
                if index - i == 0:
                    break
                if data[index-i] > data[index - 1 - i]:
                    data.insert(index - 1 - i, data[index-i])
                    data.pop(index + 1 - i)
                else:
                    break


def bucketize(data, bucket):
    for i in range(2, 13):
        a = data.count(i)
        bucket.append(a)


def displayHistogram(bucket):
    for i in range(2, 13):
        print(f"{i:2} : {bucket[i - 2] * '*'}")


def main():
    rollNumber = input("Enter the number of rolls: ")
    for i in range(0, int(rollNumber) + 1):
        rollDie()
        initArray(data, firstDie, secondDie)
    sortArray(data)
    bucketize(data, bucket)
    displayHistogram(bucket)


main()
