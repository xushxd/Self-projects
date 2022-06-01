with open(input('Drag and drop the text file you want to check here\n'), 'r', encoding='utf-8') as f: input_string = f.read()

repeads = {}

for string_letter in input_string:
    if string_letter in repeads: repeads[string_letter] += 1
    else: repeads[str(string_letter)] = 1

for i in range(20): # change how much values you want to print
    max_value = max(repeads, key=repeads.get)
    print(f" '{max_value}' {repeads[max_value]}")
    repeads.pop(max_value)
