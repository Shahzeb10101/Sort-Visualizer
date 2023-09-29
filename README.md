# Sorting Visualizer
### Video Demo: https://youtu.be/xBLq89zQMe0

### Introduction:
This is a sorting Visualizer I made for my Cs50 Final project.
Pygame is used for the display.
It visualizes multiple sorting algorithims for anyone to learn from and enjoy. Additional features include Sliders for changing the speed; changing the number of bars; a rainbow mode;

### References:
Slider code: https://www.youtube.com/watch?v=n_ijgqYmXS0 <br>
Rgb code: https://stackoverflow.com/questions/57400584/how-to-map-a-range-of-numbers-to-rgb-in-python <br>

### Inspiration from:
- Tech with Tim
- Clement Mihailescu

### Details:
#### Files in src/ :
- Classes.py contains the display class, button class and label class
- main.py contains the main app loop
- sorts.py contains all the functions for swapping and all the sorting algorithims:
  - Bubble sort
  - Selection sort
  - Insertion sort
  - Merge sort
  - Quick sort
- helper.py contains the draw_sort_state() function that draw everything on screen; it also contains a num_to_rgb() function that generates the colours for rainbow mode
- slider.py has the Slider class from: https://www.youtube.com/watch?v=n_ijgqYmXS0
- test.py is just for my testing

## Components of each file:
### main.py: 
In this file i only have the main function. It runs the app's main loop. <br> 
One design choice made for displaying sorting alogrithim's (except merge and quick sort) was to use generators. This allowed me to minimise the amount of draw_sort_state() calls. If sorting is currently being done, the generator is called with next() to continue sorting. <br> 
When it ends we call draw_sort_state(...animate=True) to cause a swoosh green animation effect after each sort.

### Classes.py: 
This file is one of the largest. <br> 
I decided to make my display class contain alot of the functionality. Upon initializing: <br>
It creates the main display, holds all the required values like min, max val, etc. It also generates the starting list and buttons that will show on the screen. This is done by the generate_buttons() method: <br>
This method creates various buttons and sliders for each sort and creating a random and set list. Each button is assigned a function it runs when clicked on.
Additionally, 2 sliders are also made, one for Speed(FPS) and the second for list size. <br>
Then initialize_values() initiates alot of values i need. <br>
Generate_list() is responsible for creating all 3 lists i need: one that with completely random size and numbers; one with random numbers but set size (slider list) and one that has set values and set size but it is shuffled (default_list). This lets the user test the sorts with multiple kinds of data.
<br>
I also generate block_width, block_height_scale and startx here. These formulas are half my one and half inspired from tech with tim's formulas. The especially tricky one was block_width and startx since my program dynamically changes padding and width so it took some time to figure out.
<br>
rand_list() set_list() just generate the lists.<br>
event_loop() is responsible for handling all key press events, sliders and buttons. Again the slider code is heavily inspired and partyle taken from the source i gave. <br>
The rest of the functions in this class are used for the sorting algorithims start and end; and also for the button functionality.
<br>
The button class is a pygame sprite. It's intialized with some text to display, its position and the function it will run when clicked. It can also be passed in some arguments. The clicking functionality is handled by pressed().

### helper.py: 
This file is responsible for all the drawing on the screen.
The draw_sort_state() function takes alot of optional parameters which helped me reduce redundancy:
- green, blue, and red are all lists that should contain the indexes that should be coloured.
- done is used to colour the bars green when the algorithim is compelte.
- animate slowly fills in the bars with green to create a kind of swoosh effect.
- update lets me update the screen if needed.<br>
The function itself starts from window.startx. It runs n times where n is the length of the list we are sorting. It creates a surface and rect for the surface and fill's it with the needed colour. One thing to note is line 33: (if done and not window.rainbow), this allows me to fill the bars with a colour based on their value calculated by num_to_rgb() to create a rainbow like pattern. The rest of the function updates the x_position for the next bar, draws the buttons, sliders and bars.
<br>
num_to_rgb() is taken from the source i gave above. It calcutes rgb values based on the value given.

### sorts.py
This file contains all of the sorting algorithims used. <br>
First is bubble sort, which is normal except that i yield after swapping to draw the updated bars.
<br>
Then is selection sort which is also normal except yield to draw
<br> Insertion sort is also normal except yield to draw
<br>
Quick sort had to be changed a bit. 
The partition function draws everytime we check an element. Also after all elements are done being checked, we draw once more. In this function we use update=True since we can't use yield as it will go to quick_sort functon not main().
<br>
The most challenging function to make was merge_sort. Since merge_sort uses multiple lists to work i had to figure out how to track the index in the main list. I decided on calculating the relation of the current list to the main list in terms of the start index and end index. This is done differently for both sorting the left half and the right half.
<br>
The merge function has alot of draw_sort_state()'s due to the amount of swaps merge sort makes.



