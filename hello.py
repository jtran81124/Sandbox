print("Start Guessing game")
word = "apple"


# while word!= input("Enter the secret word: "):
#     print("try again")
# print("You win!")

print("Practice Dictionaries")

jacky = {
    "birthday": 0o1/27/98,
    "school": "SJSU",
    "gamesPlayed": ["COD","valorant"]
}
    
print(", ".join(jacky["gamesPlayed"]))

print("Working with Lists")
print("")
numbers = [2,3.14, 4,6,10]

print(numbers[:])
print("reversed: ", numbers[::-1])

print("")
print("Loops")
for x in range(3):
    print(x, end=" ")\

print("")
print("Functions")
def exponent(value, power):
    result = 1
    for x in range(power):
        result = result * value
    return result

print (exponent(2,6))

print("")
print("all vowls become g")

def translate(word):
    result = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            result = result + "g"
        else:
            result = result + letter
    return result

# word = input("enter a word to be translated: ")
# print(word, " translates to: ", translate(word))

print("")
print("Error catching")


flag = True

while flag:
    try:
        number = int(input("Enter a number: "))
        flag = False
    except:
        flag = True
        print("Invalid input")
    
    
print("Number is: ", number)