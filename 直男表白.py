confession = 'I LOVE YOU!'

message = "" #用于保存加密的结果
for char in confession:
    number = ord(char)
    message += hex(number)[2:]
print(message)

translate=""#用于保存翻译后的结果
i=2
for char in message :
    number=message[i-2:i]
    i+=2
    number=int(number,base=16)
    translate+=chr(number)
    if i>len(message):
        break
print(translate)
