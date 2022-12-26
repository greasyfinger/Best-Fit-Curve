
# Best Fit curve plot

Uses curve fit function of scipy to fit curve to a scatter plot based on
initial guess.


## Features

- provides a scatter plot of the csv data
- uses numpy to generate linespace of points for line plot of best fit curve
- prints the best fit parameter received from curve fit to the standard out


## Deployment
paste your data to the csv file in the x,y format and change the equation returned by
func() function.

add your best guess of the parameters in line 14.

To add more parameters, add them to the func() function and everywhere m and c are mentioned.

Then just run make to generate plot and print the best parameters
```bash
  make
```


## Acknowledgements
 [Mr P Solver](https://www.youtube.com/watch?v=peBOquJ3fDo&t=18s)


