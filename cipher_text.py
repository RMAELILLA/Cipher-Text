# Assignment 2 Problem 3 - Cipher Text

# Get the message
user_message = input('\033[1;32m Please enter your "message" in UPPERCASE LETTERS: \n')
# Get the key
user_key = input('\033[1;33m Please enter your "key" also in UPPERCASE LETTERS: \n')
# Translate letter to correspond values
def translate(string, key): 
  cipher_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])) % 26
    x += ord('A') 
    cipher_text.append(chr(x))
  return("" . join(cipher_text))
# Repeat translation if not equal to length, message key
def rpt_translate(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
# Add each column, excess minus 26
# convert
if __name__ == "__main__":
   message = user_message
   keyword = user_key
   key = translate(message, keyword) 
   cipher_text = (message,key)
# display generated cipher text
print("The cipher text of your input is : ", cipher_text )