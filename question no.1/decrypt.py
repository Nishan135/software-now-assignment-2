from encrypt import shift_lower, shift_upper

def decrypt_text(text, shift1, shift2):
    result = ""
    for c in text:
        if 'a' <= c <= 'z':
            result += shift_lower(c, -shift1) 
        elif 'A' <= c <= 'Z':
            result += shift_upper(c, -shift2) 
        else:
            result += c
    return result
