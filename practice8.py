from collections import deque

queue = deque()
queue.append('Rizwan Defriansyah')
queue.append('Rizwan')
queue.append('Dfriansyah')
queue.append('Defri')
deque(['Rizwan Defriansyah', 'Rizwan', 'Defriansyah', 'Defri'])

print('antrian awal :', list(queue))
print('___Mulai melayani___')

nomor = 1
while queue:
    pelanggan = queue.popleft()
    print(f'[{nomor}] Melayani {pelanggan}')
    if queue:
        print(f' Antrian : {list(queue)}')
    nomor += 1

print('___Semua pelanggan telah dilayani___')