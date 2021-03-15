def validateUserInput() -> object:
    userNumberList = []
    i = 1
    while i <= 5:
        userNumberList.append(int(input()))
        i += 1
    return userNumberList
