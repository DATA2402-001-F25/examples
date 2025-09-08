
last_3 = []

while True:

    user_input = input('enter some text (q to quit)')
    if user_input == 'q':
        break
    
    last_3.append(float(user_input))

    if len(last_3) == 4:
        del last_3[0]
    
    print(sum(last_3)/len(last_3))
