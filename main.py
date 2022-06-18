print('Let us create you a report card in a text file.')
name = input('How would you like to call it? ')
Report_name = name + '.txt'
print('Provide the subject names, coefficients and the marks obtained below: ')
Subject = []
Coef = []
Scores = []
Marks = []
n = 'y'
i = 0
Sum = 0
Coeff = 0
while n == 'y':
    Subject.append(input('Subject: '))
    Coef.append(int(input('Coefficient: ')))
    Scores.append(float(input('Score: ')))
    Marks.append(Coef[i]*Scores[i])
    Sum += Marks[i]
    Coeff += Coef[i]
    i += 1
    n = input('Do you want to type in data for another subject? (y/n) ')
Aver = Sum / Coeff
print(f'Average: {Aver}')
f = open(Report_name, 'w')
f.write('This is your generated report card\n')
f.write('\nSubject\tCoefficient\tScore\tMark\n')
for k in range(i):
    f.write(f'\n{Subject[k]}\t{Coef[k]}\t{Scores[k]}\t{Marks[k]}\n')
f.write(f'\nAverage: {Aver}')
f.close()