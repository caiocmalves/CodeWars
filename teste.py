text = 'the-pippi_Is-Savage'
novo_text = ''
for i in text:
    if i == '-' or i == '_':
        novo_text += ' '
    else:
        novo_text += i
    
        
print(novo_text)        
