for i in range(1, int(input("Enter string amount: ")) + 1):
    cmnt = input()
    if not (cmnt == "" or cmnt.isspace()):
        print(f"{i}: {cmnt}")
    else:
        print(f"{i}: COMMENT SHOULD BE DELETED")