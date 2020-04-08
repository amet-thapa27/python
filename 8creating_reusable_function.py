def emoji_convertor(message):
    words = message.split()
    emojis = {
        ":)": "happy",
        ":(": "sad"
    }
    outputr = " "
    for word in words:
        outputr += emojis.get(word, word) + " "
    return outputr


message=input(">")
output = emoji_convertor(message)
print(output)
