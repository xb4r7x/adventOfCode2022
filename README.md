# adventOfCode2022
![](https://img.shields.io/badge/day%20📅-6-blue)
![](https://img.shields.io/badge/stars%20⭐-12-yellow)	
![](https://img.shields.io/badge/days%20completed-6-red)

https://adventofcode.com/2022

# newDay.sh
This script will create the directory structure, get your input file, and create a basic python skeleton.
It takes the day as an argument. There's currently no validation. Don't fuck it up.
It requires that your adventofcode.com session cookie be stored in an environment variable $ADVENT_SESSION

#### Obtaining session cookie
- Log into adventofcode.com
- Navigate to any day's input page
- Open your browser's dev tools and find your session cookie in the request headers.
- The same session cookie should be valid for the whole month, so you should only have to do this once. 

# Folder Structure
Each day of the advent calendar has its own numbered folder. All files to solve the problems of the day will be placed inside that folder. 
