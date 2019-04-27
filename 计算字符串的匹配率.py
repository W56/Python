def Rate(origin,userInput):

    if not (isinstance(origin,str) and isinstance(userInput,str)):
        print("The two parameters must be strings")
        return

    if len(origin)<len(userInput):
        print("Sorry.I suppose the second parameter string is shorter.")
        return

    right = 0
    for origin_char,userInput_char in zip(origin,userInput):
        if origin_char == userInput_char:
            right += 1

    return right/len(origin)

if __name__ == '__main__':
    origin = "Shandong Institude of Bussiness and Technology"
    userInput = "ShanDong institude of bussiness and technology"
    print(len(origin))
    print(Rate(origin,userInput))
