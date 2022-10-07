def to_camel_case(text):
    word = ''
    for i in text:
        if i == '-' or i == '_':
            word += ' '
    else:
        word += i
    
    new_text = word.split(' ')
    new_word = new_text[0]
    for i in range(1, len(new_text)):
        new_word += new_text[i].capitalize()
    return new_word

