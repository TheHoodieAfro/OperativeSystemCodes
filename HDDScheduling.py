import numpy as np

#Scheduling algorithm to use
algorithm = input()

# Queue of the cylinders, starting with the initial position
queue = np.array([int(y) for y in input().split()])

sum = 0
if (algorithm.lower() == 'fcfs'):
    for i in range(len(queue)-1):
        sum += abs(queue[i]-queue[i+1])

elif (algorithm.lower() == 'scan'):
    direction = input()

    if (direction.lower() == 'down'):
        up = np.sort(queue[queue > queue[0]])

        down = queue[queue <= queue[0]]
        down[::-1].sort()

        queue = np.concatenate((down, up), axis=None)

    elif (direction.lower() == 'up'):
        up = np.sort(queue[queue >= queue[0]])

        down = queue[queue < queue[0]]
        down[::-1].sort()

        queue = np.concatenate((up, down), axis=None)
        print(queue)

    else:
        print('Select a valid direction')
        exit()
    
    for i in range(len(queue)-1):
            sum += abs(queue[i]-queue[i+1])

elif (algorithm.lower() == 'c-scan'):
    direction = input()

    if (direction.lower() == 'down'):
        up = queue[queue > queue[0]]
        up[::-1].sort()

        down = queue[queue <= queue[0]]
        down[::-1].sort()

        queue = np.concatenate((down, up), axis=None)

    elif (direction.lower() == 'up'):
        up = np.sort(queue[queue >= queue[0]])

        down = np.sort(queue[queue < queue[0]])

        queue = np.concatenate((up, down), axis=None)

    else:
        print('Select a valid direction')
        exit()
    
    for i in range(len(queue)-1):
            sum += abs(queue[i]-queue[i+1])

else:
    print('Select a valid algorithm')
    exit()

print('queue', queue)
print('Se movio', sum, 'cilindros')