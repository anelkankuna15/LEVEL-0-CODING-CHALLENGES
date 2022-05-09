def common():
    string1 = "I love Umuzi"
    string2 = "I am starting to get the hang of this python is awesome"
    a1 = set(string1)
    a2 = set(string2)
    common_letters = a1 & a2
    print(a1 & a2)

common()