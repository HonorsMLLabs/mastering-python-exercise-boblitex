vowel = ["a", "e", "i", "o", "u"]


def search(q=input("enter query: ")):
    s = set(vowel)
    if q in s:
        print("vowel found")
    else:
        print("consonant all day")







