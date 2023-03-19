# python3


def build_heap(data):
    swaps = []
    for i in range((len(data) // 2) -1, -1, -1):
        swapBot(i, data, swaps)
    return swaps

def swapBot(numb, data, swaps):
    lab = 2*numb + 2
    kr = 2*numb + 1
    
    if lab < len(data):
        maz = kr if (data[kr]<data[lab]) else lab
    elif kr <len(data):
        maz = kr
    
    if 'maz' in locals() and data[maz] < data[numb]:
        data[maz], data[numb] =  data[numb], data[maz]
        swaps.append([numb,maz])

        swapBot(maz,data,swaps)

def main():
    
    input_type = input()
    if "F" in input_type:
        file_name = input()
        try:
            file = open("tests/" + file_name[:2], "r")
        except IOError:
            print("Invalid file")
        else:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
            file.close()
    elif "I" in input_type:
        try:
            n = int(input())
            data = list(map(int, input().split()))
        except IOError:
            print("Wrong keyboard input")
    else:
        print("Wrong input type")
    # checks if lenght of data is the same as the said lenght

    assert len(data) == n, "Incorrect element amount"
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
