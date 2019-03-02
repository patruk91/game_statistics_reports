# game_statistics_reports

### The story
You are a happy programmer at a big game developer company, named "ID Software". Judy, your statistician colleague,
asks help from you in a competitor evaluation project. She has a data file with a lot of statistical information about
famous games of all time. Judy has some unanswered questions about the games. She needs you to write a program that can
answer these questions.

### Description
Your task is to write reports that answer Judy's questions. Every report needs to be implemented as a function so every
function is related to a question. For every report function you need to write a printer function also. The printer
function has to print the return value(s) of the report function.

The input file
You can find the input file in the repository. Its name is game_stat.txt. Every line in the file contains the following
information about a game:
- title
- total copies sold (million)
- release date
- genre
- publisher
These are the properties of a game. Properties are separated by a tab character and lines are separated by line break
characters.

### General expectations of the report functions
Every report function:
- has to be named properly (as you see in the Questions section)
- must NOT contain printing to console
- returns only the asked information
- should run in any order
- has only the parameters predefined in the questions
- has to be prepared for any other data files (not just the game_stat.txt) within the same structure
- do NOT import other modules

### Expectation of the source code
You need to write your project into 3 source files:
- reports.py: write only the report functions in it.
- printing.py: for printing the output of the report functions in a user friendly way. You can use this to test your
solutions.
- export.py: for exporting the reports into a single export file. By running this program Judy will get a single text
file with all the answers she needs (you should export only the answers line by line, Judy will know the questions).
Judy will run printing.py and export.py to get the answers she want's, ask her for input where needed (e.g. game title).

### Judy's questions
1.  many games are in the file?
Expected name of the function: count_games(file_name)
Expected output of the function: a number
2. Is there a game from a given year?
Expected name of the function: decide(file_name, year)
Expected output of the function: boolean value
3. Which was the latest game?
Expected name of the function: get_latest(file_name)
Expected output of the function: the title of the latest game as a string
Other expectation: if there is more than one, then return the first from the file
4. How many games do we have by genre?
Expected name of the function: count_by_genre(file_name, genre)
Expected output of the function: a number
5. What is the line number of the given game (by title)?
Expected name of the function: get_line_number_by_title(file_name, title)
Expected output of the function: a number (if there is no game found, then raises ValueError exception)

### ...and more bonus questions! (nice to have)
Judy knows that you are a very busy programmer, but she has more questions and she looks like a cute little
dog with big eyes.

1. What is the alphabetical ordered list of the titles?
Expected name of the function: sort_abc(file_name)
Expected output of the function: a list of strings
2. Do not use the builtin sort() or sorted() functions, but implement an easy sort algorithm by your own!
What are the genres?
Expected name of the function: get_genres(file_name)
Expected output of the function: a list of the genres (without duplicates, in alphabetical order)
3. What is the release date of the top sold "First-person shooter" game?
Expected name of the function: when_was_top_sold_fps(file_name)
Expected output of the function: year of the release, as integer (if there is no game with genre "First-person shooter"
then raises ValueError exception

### Judy's questions
1. What is the title of the most played game (i.e. sold the most copies)?
Expected name of the function: get_most_played(file_name)
Expected output of the function: (string)
Other expectation: if there is more than one, then return the first from the file
2. How many copies have been sold total?
Expected name of the function: sum_sold(file_name)
Expected output of the function: (number)
3. What is the average selling?
Expected name of the function: get_selling_avg(file_name)
Expected output of the function: (number)
4. How many characters long is the longest title?
Expected name of the function: count_longest_title(file_name)
Expected output of the function: (number)
5. What is the average of the release dates?
Expected name of the function: get_date_avg(file_name)
Expected output of the function: average year (number)
Other expectation : the return value must be the rounded up average
6. What properties has a game? Expected name of the function: get_game(file_name, title)
Expected output of the function: a list of all the properties of the game (a list of various type).
Details : the function get a parameter named game. This is the title of the game (string). This is an existent game.
The function return a list of the properties of this game including the title.
An example return value: ["Minecraft", 23.0, 2009, "Survival game", "Microsoft"].

### ... and more bonus questions! (nice to have)
Judy knows that you are a very busy programmer, but she has more questions and she looks like a cute little dog
with big eyes.

1. How many games are there grouped by genre?
Expected name of the function: count_grouped_by_genre(file_name)
Expected output of the function: a dictionary with this structure: { [genre] : [count] }
Detailed description: return a dictionary where each genre is associated with the count of the games of its genre
2. What is the date ordered list of the games?
Expected name of the function: get_date_ordered(file_name)
Expected output of the function: the date ordered list of the titles in descending order (list of string)
Other expectation: The secondary ordering rule is the alphabetical ordering of the titles. So if there are titles from the same 
year, you need to order them alphabetically in ascending order.
