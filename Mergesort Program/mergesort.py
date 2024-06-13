import sys
def merge_list(list1,list2):
    merged = []
    i = 0
    j = 0
    running = True
    end = False
    while running is True:
        current1 = list1[i]
        current2 = list2[j]
        if current1 < current2:
            merged.append(list1[i])
            if i < len(list1)-1:
                i += 1
            else:
                for item in range(j, len(list2)):
                    merged.append(list2[item])
                running = False

        elif current1 > current2:
            merged.append(list2[j])
            if j < len(list2)-1:
                j += 1
            else:
                for item in range(i, len(list1) ):
                    merged.append(list1[item])
                running = False

        elif current1 == current2:
            merged.append(list1[i])
            if i < len(list1) - 1:
                i += 1
            else:
                for item in range(j, len(list2)):
                    merged.append(list2[item])
                running = False

    return merged

def sort_list(myList):

    if len(myList) == 1:
        return myList

    half = int(len(myList)/2)

    L = myList[0:half]
    R = myList[half:len(myList)]

    sorted = merge_list(sort_list(L),sort_list(R))

    return sorted

inFile = open(sys.argv[1], "r")
outFile = open(sys.argv[2], "w")
data = inFile.readlines()

data = sort_list(data)

for line in data:
    outFile.write(f"{line}")

inFile.close()
outFile.close()



if __name__ == "__main+__":
    pass