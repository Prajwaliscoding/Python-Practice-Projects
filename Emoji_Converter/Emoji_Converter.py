sentence=input("Enter your sentence\n")
strings=sentence.split(' ')
emoji_dictionary={
    ":)":"😀",
    ':(':'😞'
}
output=""
for i in strings:
    output+=emoji_dictionary.get(i,i)+" "
print(output)
