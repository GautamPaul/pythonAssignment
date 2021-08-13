def binarySearch(numList, low, high, key):
    mid = (low+high)//2
    if low <= high:
        if(numList[mid] == key):
            return mid
        elif key > numList[mid]:
            return binarySearch(numList, mid+1, high, key)
        else:
            return binarySearch(numList, low, mid-1, key)
    else:
        return -1


numList = [1, 22, 333, 4444, 55555, 666666]
print(numList)
num = int(input("Enter an item to search from the list:"))
low = 0
high = len(numList)-1
index = binarySearch(numList, low, high, num)
if index == -1:
    print("{} not found in the list.".format(num))
else:
    print("{} found at index {}".format(num, index))
