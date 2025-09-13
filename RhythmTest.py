import time

# Define the function to calculate the accurate time for ratings
def rate_rhythm (target_time, actual_time):
    percentage_diff = abs(actual_time - target_time) / target_time * 100
    
    if percentage_diff <= 8:
        return 'Grate!'
    elif percentage_diff <= 16:
        return 'Okay!'
    else:
        return 'Miss!'

print ('Welcome to the Rhythm Test.')
print ('This program will test your rhythm - How consistent are YOU!')
print ('When the test start press Enter according to the rhythm speed you selected.')

# Get rhythm speed input
while True:
    try:
        speed = int(input('\nChoose rhythm speed(1,2 or 3): '))
        
        if speed in [1,2,3]:
         break
        else:
            print('Invalid choice. Enter 1,2 or 3: ')
    except ValueError:
             print('Invalid choice. Enter 1,2 or 3: ')

# Get rounds input
while True:
    try:
        rounds = int(input('\nChoose number of rounds(5 to 50): '))
        
        if 5<= rounds <=50:
            break
        else:
            print('Invalid choice. Enter a number between 5 to 50')
    except ValueError:
                print('Invalid choice. Enter a number between 5 to 50')

print('\nThis test will last', rounds, 'rounds and you are aiming for a', speed, 'second rhythm.')
input('Press Enter to start!')


# Initialize end time for calculations
end_time = time.time()


# Initialize lists to store results
response_times = []
differences = []


# Calculating the response time
for round_num in range(1, rounds + 1):
    input(f'\nRound {round_num} of {rounds}')
    reaction_time = round(time.time() - end_time, 2)
    

    # Store the response time and time differences
    response_times.append(reaction_time) 
    differences.append(round(abs(reaction_time - speed), 2))

    print(f'Response time: {reaction_time:.2f}s - {rate_rhythm(speed, reaction_time)}')
    end_time = time.time()
    
input('\nTest Complete! Press Enter to see your results.')


# Calculate the fastest, average and slowest time
fastest = min(response_times)
average = round(sum(response_times) / len(response_times), 2)
slowest = max(response_times)

print('\nResults:')
print(f'  Fastest Response: {fastest:.2f}s ({rate_rhythm(speed, fastest)})')
print(f'  Average Response: {average:.2f}s ({rate_rhythm(speed, average)})')
print(f'  Slowest Response: {slowest:.2f}s ({rate_rhythm(speed, slowest)})')

print('\nRound | Response Time | Difference')
print('-' * 5, ' ', '-' * 13, ' ', '-' * 11)


# Display results summary
for r in range(rounds):
    round_num = r + 1
    if differences[r] == 0:
        diff_text = 'Spot on!'
    else:
        if response_times[r] < speed:
            diff_text = 'early'
        else:
            diff_text = 'late'
        diff_text = f'{differences[r]:.2f}s {diff_text}'

    print(f'{round_num:<5} {response_times[r]:>10.2f}s       {diff_text}')
    
print('\nThe End!')
