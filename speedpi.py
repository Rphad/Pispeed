import matplotlib.pyplot as plt
import time
from sympy import pi
import os

digits = []
times = []


os.system('nmcli radio wifi off')
print('Wifi turned off')
os.system('date')
print('Computing...')
startall = time.time()
j=1
for i in range(1,6+1):
    while j < 10**i:
        start = time.time()
        pi.evalf(j)
        end = time.time()
        digits.append(j)
        duration = end-start
        times.append(duration)
        j+=10**(i-1)

start = time.time()
pi.evalf(j)
end = time.time()
digits.append(j)
duration = end-start
times.append(duration)



endall = time.time()

os.system('date')

os.system('nmcli radio wifi on')
print('Wifi turned back on')


k=1
while os.path.exists('./results_' + str(k)):
    k+=1

print('Creating path ./results_{}'.format(k))
os.system('mkdir results_' + str(k))
print('Changing directory')
os.chdir('results_' + str(k))

del(k)

print('Writing list elements')

with open('digits_pispeed.txt', 'w') as digits_pispeed:
    for number in digits:
        digits_pispeed.write('%s\n' % number)

print('Digits done')

with open('times_pispeed.txt', 'w') as times_pispeed:
    for time in times:
        times_pispeed.write('%s\n' % time)

print('Times done')
print('Crating log')
with open('log.txt', 'w') as log:
    log.write(str(endall-startall))

print('Creating plot')
plt.plot(digits, times, 'ro')
plt.ylabel('Computation time')
plt.xlabel('Digits')
plt.savefig('pispeed.png')
print('Creating log y plot')
plt.yscale('log')
plt.plot(digits, times, 'ro')
plt.ylabel('Computation time (log)')
plt.xlabel('Digits')
plt.savefig('pispeed_log_y.png')
print('Creating log y plot')
plt.yscale('linear')
plt.xscale('log')
plt.plot(digits, times, 'ro')
plt.ylabel('Computation time')
plt.xlabel('Digits (log)')
plt.savefig('pispeed_log_x.png')

print('Done')
