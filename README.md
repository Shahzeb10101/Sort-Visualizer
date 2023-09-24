# Sorting Visualizer
### Video Demo:  <URL HERE>

#### Introduction:
This is a sorting Visualizer I made for my Cs50 Final project.
Pygame is used for the display.
It visualizes multiple sorting algorithims for anyone to learn from and enjoy. Additional features include Sliders for changing the speed; changing the number of bars; a rainbow mode;

#### References:
Slider code: https://www.youtube.com/watch?v=n_ijgqYmXS0 <br>
Rgb code: https://stackoverflow.com/questions/57400584/how-to-map-a-range-of-numbers-to-rgb-in-python <br>

#### Inspiration from:
- Tech with Tim
- Clement Mihailescu

#### Details:
##### Files in src/ :
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
