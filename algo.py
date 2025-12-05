vars_data = {'current_dial': 50, 'max_dial': 99, 'min_dial': 0, 'zero_count': 0}
[[vars_data.update({'current_dial': (vars_data['current_dial'] + 1 if vars_data['current_dial'] + 1 <= vars_data['max_dial'] else vars_data['min_dial']) if (True if line.startswith('R') else False) else (vars_data['current_dial'] - 1 if vars_data['current_dial'] - 1 >= vars_data['min_dial'] else vars_data['max_dial']),'zero_count': vars_data['zero_count'] + 1 if ((vars_data['current_dial'] + 1 if vars_data['current_dial'] + 1 <= vars_data['max_dial'] else vars_data['min_dial']) if (True if line.startswith('R') else False) else (vars_data['current_dial'] - 1 if vars_data['current_dial'] - 1 >= vars_data['min_dial'] else vars_data['max_dial'])) == 0 else vars_data['zero_count']}) for x in range(int(line.removeprefix('R' if line.startswith('R') else 'L')))] for line in open('input.txt', 'r', encoding='utf-8')]
print(vars_data['zero_count'])









