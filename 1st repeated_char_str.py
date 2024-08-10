def first_repeated_char(s):
    seen_chars = set()
    for char in s:
        if char in seen_chars:
            return char
        seen_chars.add(char)
input_string = "kamalamaharaja"
result = first_repeated_char(input_string)
if result:
    print(f"The first repeated character is: {result}")
