import time


delay_text = 0.015
delay_loading = 0.5
delay_question = 0.05
delay_image = 0.0005

def print_with_delay(text, delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

text = '''
                        ______________________________________________________________________________________________

                         8888b.  88   88 88b 88  dP""b8 888888  dP"Yb  88b 88      db    88""Yb 888888 88b 88    db    
                          8I  Yb 88   88 88Yb88 dP   `" 88__   dP   Yb 88Yb88     dPYb   88__dP 88__   88Yb88   dPYb   
                          8I  dY Y8   8P 88 Y88 Yb  "88 88""   Yb   dP 88 Y88    dP__Yb  88"Yb  88""   88 Y88  dP__Yb  
                         8888Y"  `YbodP' 88  Y8  YboodP 888888  YbodP  88  Y8   dP""""Yb 88  Yb 888888 88  Y8 dP""""Yb  
                        ______________________________________________________________________________________________
'''
print_with_delay(text, delay_text)

prompt = "Do you want to start the game? (Y/N): "
print_with_delay(prompt, delay_question)

start_game = input()
if start_game == "Y":
    message = "Loading"
    print_with_delay(message, delay_text)
    
else:
    message = "Maybe next time!"
    print_with_delay(message, delay_text)

line3 = '''
.....................................
'''

print_with_delay(line3, delay_loading)

line = '''

----------------------------------------------------------------------------------------------------------------------------------------------------------
'''
print(line)

delay_text = 0.05

print_with_delay("Welcome Traveller, to the enchanting land of Eldoria. A realm of magic and mystery, Eldoria is known for its lush landscapes,", delay_text)
print_with_delay("towering mountains, and bustling towns. However, darkness looms over this once-peaceful kingdom. The ancient evil that has long been sealed away", delay_text)
print_with_delay("within the depths of the Forbidden Dungeon has awakened, unleashing chaos and despair. To make matters worse, the nefarious creature has captured", delay_text)
print_with_delay("the beloved princess, casting a shadow of sorrow upon the land. Now, a call to heroes echoes through the realm, beckoning courageous souls like", delay_text)
print_with_delay("yourself to rise up and embark on a perilous quest to save the princess and restore hope to Eldoria. The fate of the kingdom rests in your hands.", delay_text)
print_with_delay("Will you answer the call and face the treacherous trials that lie ahead? Prepare to venture into the heart of darkness, where danger lurks at every turn.", delay_text)
print_with_delay("Brace yourself, for the destiny of the princess and the fate of Eldoria await your valiant efforts.", delay_text)

line = '''

----------------------------------------------------------------------------------------------------------------------------------------------------------
'''
print(line)


