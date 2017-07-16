def pigLatin(strInput):
    #String of all vowels to test if a word should be skipped
    vowels = "aeiouAEIOU"

    #String of all symbols to test if a char should be skipped 
    symbols = "',.-;:_*?!" + '"'

    suffix = "ay"

    #Strings to store the symbols in for them to be re-added
    firstSymbol = ""
    lastSymbol = ""
    
    output = ""
    user_input = strInput.split()

    #Run's through a sentence to alter words starting with a consonant
    for word in user_input:

        #Set's the first and second character, for ease of testing and altering
        firstChar = word[0]
        lastChar = word[len(word)-1]

        #Removes all possible symbols in front of word
        while(firstChar in symbols):
            firstSymbol += firstChar
            word = word[1:]
            firstChar = word[0]

        #Removes all possible symbols at the end of a word
        while(lastChar in symbols):
            lastSymbol += lastChar
            word = word[:len(word)-2]
            lastChar = word[:len(word)-1]

        #Alter all word that starts with a consonant
        if(firstChar not in vowels):
            word = word[1:]

            #Turns all capital letters to lowercase and sets a new captial
            if(firstChar.isupper()):
                firstChar = firstChar.lower()
                newCap = word[0].upper()
                tmpWord = word[1:]
                word = newCap + tmpWord
            
            word += firstChar+suffix
            output += firstSymbol + word + lastSymbol + " "
        else:
            output += firstSymbol + word + lastSymbol + " "

        #Resets the symbols at the start and at the end
        firstSymbol = ""
        lastSymbol = ""

    return output
