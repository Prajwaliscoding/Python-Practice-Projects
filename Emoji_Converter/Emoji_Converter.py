def emoji():
    strings=sentence.split(' ')
    emoji_dictionary={
        ":)":"😀",
        ':(':'😞'
    }
    output=""
    for i in strings:
        output+=emoji_dictionary.get(i,i)+" "
    return output
sentence=input("Enter your sentence\n")
print(emoji())
