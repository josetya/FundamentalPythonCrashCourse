anak = []

anak.append('eka')
anak.append('dwi')
anak.append('tri')
anak.append('panca')

print(anak)

anak = ['eka','dwi','tri']
anak.append('lima')
print(anak)


for a in anak:
    print (f'{a}')

for a in range (0, len(anak)+1):
    print(f'{a+1} {anak[a]}')
