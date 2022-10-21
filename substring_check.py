# Check if a string contains a specific substring
string = input("Tell me about yourself ")
contain_words = ["myself","old","completed","job","graduation"]
for i in contain_words:
    if i in string:
        print("string contain word name")
    else:
        print("string does not contain word name") 