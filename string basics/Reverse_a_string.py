# Most easiest using reversed() keyword

def will_reverse(s):
    return "".join(reversed(s))

example_string = 'Tamaghno'
reversed_string = will_reverse(example_string)

print("Original string : ",example_string)
print("Reversed string : ",reversed_string)