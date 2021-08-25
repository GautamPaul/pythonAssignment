def binary_search(numList, low, high, key):
    mid = (low+high)//2
    if low <= high:
        if(numList[mid] == key):
            return mid
        elif key > numList[mid]:
            return binary_search(numList, mid+1, high, key)
        else:
            return binary_search(numList, low, mid-1, key)
    else:
        return -1


num_list = [1, 22, 333, 4444, 55555, 666666]
print(num_list)
num = int(input("Enter an item to search from the list:"))
low = 0
high = len(num_list)-1
index = binary_search(num_list, low, high, num)
if index == -1:
    print("{} not found in the list.".format(num))
else:
    print("{} found at index {}".format(num, index))
