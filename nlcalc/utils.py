# Returns True if String can be converted to Numeric Type
# otherwise return False
def is_numeric(value):
    try:
        int(value)
        return True
    except (ValueError,TypeError):
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False


# Converts String to Numeric Type
# Raises Error if not Possible
# int conversion is tried first so that high precision of
# int in python can be utilized
def convert_to_numeric(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return float(value)



def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    final_text = []
    flag = 0
    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            if flag == 1:
                final_text.append(str(result + current))
                current = result = 0
            final_text.append(word)
            flag = 2
            continue
        flag = 1
        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    if flag == 1:
        final_text.append(str(result + current))
    
    return " ".join(final_text)

