number_of_electrons = int(input())
shells = []
for current_shell in range(1, number_of_electrons + 1):
    max_electrons_in_current_shell = 2 * current_shell ** 2
    if number_of_electrons >= max_electrons_in_current_shell:
        shells.append(max_electrons_in_current_shell)
        number_of_electrons -= max_electrons_in_current_shell
        if number_of_electrons == 0:
            break
    else:
        shells.append(number_of_electrons)
        break

print(shells)