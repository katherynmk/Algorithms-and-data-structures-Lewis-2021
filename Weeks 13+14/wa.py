def removeDuplicate(array):
#ideas from https://paste.ee/p/8h2fu

    array.sort()
    x = [array[0]]

    y = array[0]
    for i in range(1, len(array)):
        if array[i] != y:
            x.append(array[i])
            y = array[i]

    return x
if __name__ == '__main__':
    print(removeDuplicate([5,5,5,7,8,9,9,9,10,11,12]))
