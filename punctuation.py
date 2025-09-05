s = "the has !..,,war"
punc = "!.,"
t = ""
for i in s:
    if i not in punc:
        t+=i


print(t)
