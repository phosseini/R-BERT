import statistics

result_path = 'results.txt'

results = {'accuracy': list(), 'macro': list(), 'weighted': list()}

with open(result_path, 'r') as in_file:
    lines = in_file.readlines()

for line in lines:
    line = line.replace('macro avg', 'macro')
    line = line.replace('weighted avg', 'weighted')
    line = [l.strip() for l in line.split(' ') if l.strip() != '']
    if len(line) > 0:
        if line[0] == 'accuracy':
            results[line[0]].append(float(line[1]))
        elif line[0] == 'macro':
            results[line[0]].append(float(line[3]))
        elif line[0] == 'weighted':
            results[line[0]].append(float(line[3]))

for metric, values in results.items():
    print('avg. [{}]: {}'.format(metric, round(statistics.mean(values), 3)))
    print('std. [{}]: {}'.format(metric, round(statistics.stdev(values), 2)))
    print('max. [{}]: {}'.format(metric, round(max(values), 3)))
    print('=====================')

print(results)
