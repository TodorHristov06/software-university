def age_assignment(*names, **ages):
    result = []
    for name in sorted(names):
        first_letter = name[0]
        age = ages.get(first_letter)
        result.append(f"{name} is {age} years old.")
    return '\n'.join(result)