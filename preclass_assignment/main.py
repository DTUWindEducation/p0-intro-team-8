import functions as fxn

# Exercise 1
fxn.greet('Thomas')
fxn.greet('Marco')

# Exercise 2
bed_size_list = [-5, 135, 140, 141, 145, 150, 150.0001, 200]
for bed_size in bed_size_list:
    fxn.goldilocks(bed_size)

# Exercise 3
example_lists = [[1, 2, 3, 4], [-1, -2, -3, -4], [0, 2**0.5, 3.4, 100000]]
for ex_list in example_lists:
    print(fxn.square_list(ex_list))

# Exercise 4
stop_points = [0, -10, 55, 100]
for stop in stop_points:
    print(fxn.fibonacci_stop(stop))

# Exercise 5
status_lists = [[1,0,0,0], [1,1,1,1], [0,0,0,0], [1,0,1,0]]
pitch_lists = [[-1, 2, 6, 95],[-1, 2, 6, 95],[-1, 2, 6, 95],[100,100,100,100]]
for pitch, status in zip(pitch_lists,status_lists):
    print(fxn.clean_pitch(pitch,status))


