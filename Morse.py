def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "Aa":
            translation = translation + "._/"
        elif letter in "Bb":
            translation = translation + "_.../"
        elif letter in "Cc":
            translation = translation + "_._./"
        elif letter in "Dd":
            translation = translation + "_../"
        elif letter in "Ee":
            translation = translation + "./"
        elif letter in "Ff":
            translation = translation + ".._./"
        elif letter in "Gg":
            translation = translation + "_../"
        elif letter in "Hh":
            translation = translation + "..../"
        elif letter in "Ii":
            translation = translation + "../"
        elif letter in "Jj":
            translation = translation + "._ _ _/"
        elif letter in "Kk":
            translation = translation + "_._/"
        elif letter in "Ll":
            translation = translation + "._../"
        elif letter in "Mm":
            translation = translation + "_ _/"
        elif letter in "Nn":
            translation = translation + "_./"
        elif letter in "Oo":
            translation = translation + "- - -/"
        elif letter in "Pp":
            translation = translation + "._ _./"
        elif letter in "Qq":
            translation = translation + "_ _._/"
        elif letter in "Rr":
            translation = translation + "._./"
        elif letter in "Ss":
            translation = translation + ".../"
        elif letter in "Tt":
            translation = translation + "_/"
        elif letter in "Uu":
            translation = translation + ".._/"
        elif letter in "Vv":
            translation = translation + "..._/"
        elif letter in "Ww":
            translation = translation + "._ _/"
        elif letter in "Xx":
            translation = translation + "_.._/"
        elif letter in "Yy":
            translation = translation + "_._ _/"
        elif letter in "Zz":
            translation = translation + "_ _../"
        elif letter in " ":
            translation = translation + "/"
        else:
            print("This Translator can only translate alfabet")
    return translation
        
            
    

    
    
print(translate(input("Enter a Text: ")))
    
    


