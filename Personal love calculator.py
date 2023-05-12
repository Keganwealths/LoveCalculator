print(' WELCOME TO THE LOVE CALCULATOR PROGRAM\n================================================')
print('\n NB: This is just a game')
your_name=input('Enter your name: ')
your_age=int(input('Enter your age: '))
partner_name=input('Enter your partners name: ')
partner_age=int(input('Enter partners age: '))

love_sentense=input('Please enter a romantic name you call your Bird\'s 😂:  ')

#love calculation
name_length = len(your_name)
pname_length = len(partner_name)
common_chars = 0

# Iterate over each character in the love sentence
for char in love_sentense:
    # Check if the character is in the concatenation of the two names
    if char in your_name + partner_name:
        common_chars += 1

love_calculation = (((name_length + pname_length) + common_chars) / (your_age + partner_age)) * 100

print('Your love percentage is',int(love_calculation),'%')
if int(love_calculation)>=90:
    print('Wow your Love is perfect, you should talk of marriage with your partner, Infact get married tomorrow and invite Me Python ❤️ doctor')
elif int(love_calculation)>=70 and int(love_calculation)<90:
    print('Love is good but show your patner some care, try changing your Bird\'s name😂 ')
elif int(love_calculation)>=50 and int(love_calculation)<70:
    print('Let\'s get to work! 💼 to make your love great again ')
elif int(love_calculation)>=30 and int(love_calculation)<50:
    print('I\'m sorry, but you need to break up. 💔')
else:
    print('it seems you have failed in love try looking for💸 or find a pet! 🐶🐱🐰')

