vars_data = {'current_dial': 50, 'max_dial': 99, 'min_dial': 0, 'zero_count': 0}
for line in open('input.txt', 'r', encoding='utf-8'):
    data = {'right': True if line.startswith('R') else False, 'number': int(line.removeprefix('R' if line.startswith('R') else 'L'))}
    for x in range(data['number']):
        vars_data['current_dial'] = vars_data['current_dial'] + 1 if data['right'] else vars_data['current_dial'] - 1
        vars_data['current_dial'] = vars_data['max_dial'] if not data['right'] and vars_data['current_dial'] < vars_data['min_dial'] else (vars_data['min_dial'] if data['right'] and vars_data['current_dial'] > vars_data['max_dial'] else vars_data['current_dial'])
    vars_data['zero_count'] = vars_data['zero_count'] + 1 if vars_data['current_dial'] == 0 else vars_data['zero_count']
print(vars_data['zero_count'])










