str='ab3cdgk4ejkjk99337hkjlkj'
extract=[]
def string(str):
    for ch in str:
        if ch.isalpha():
            extract.append(ch)
            # print(extract)
    return extract
print(string(str))


