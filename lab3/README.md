# Lab 3

## Goal
Build a functional programming pipeline to clean and analyze movie data. 

## Setup
* Open the `movies.csv` file to get a feel for the data.
* Open up movies.py.  This is where all your code will live.
* Optionally, take a look at the `CSV` module in Python3 to get a feel for how to use it: https://docs.python.org/3/library/csv.html

## Required Functions

Implement these functions to process the movie data. If possible, try to write **pure** functions
wherever possible.

### 1. `parse_date(movie_dict) -> dict`
Takes a movie dictionary and returns a new dictionary with a parsed `year` field (as an integer).

**Handles:**
- Simple years: `"1999"` → `1999`
- Month + year: `"July 1994"` → `1994`
- Full dates: `"July 24 1998"` → `1998`
- ISO format: `"2001-12-19"` → `2001`

### 2. `normalize_rating(movie_dict) -> dict`
Returns a new dictionary with `rating` normalized to a 0-10 scale (as a float).

**Handles:**
- Already 0-10: `8.7` → `8.7`
- 0-100 scale: `88` → `8.8`
- Percentages: `"89%"` → `8.9`
- Missing values: `""` → `None` or `0.0` (your choice, but also see #5 below)

### 3. `extract_primary_genre(movie_dict) -> dict`
Returns a new dictionary with a `primary_genre` field containing just the first genre.

**Example:** `"Action, Sci-Fi, Thriller"` → `"Action"`

### 4. `group_by_decade(movies_list) -> dict`
Groups movies into decades: `{1990: [...], 2000: [...], 2010: [...], 2020: [...]}`

### 5. `average_rating(movies_list) -> float`
Calculates the mean rating for a list of movies. Skip any movies with missing ratings.

## Build a Pipeline

Create a complete pipeline that:
1. Loads the CSV
2. Parses dates for all movies
3. Normalizes ratings for all movies  
4. Filters to only movies from 2000 or later
5. Extracts primary genres
6. Groups by decade
7. Calculates average rating per decade

**Use:** `map()`, `filter()`, list comprehensions, or dictionary comprehensions as appropriate.

## Output

Your final output should look like:
```
2000s: 8.3 average rating
2010s: 7.8 average rating
2020s: 7.6 average rating
```

## Suggested Pairing Strategy

- **Round 1:** Person A "drives", implements parsing functions. Person B writes tests with sample data to get confidence that the functions will work as expected.
- **Round 2:** Switch! Person B drives filtering and grouping. Person A writes tests and asks questions as needed.

## Discussion Questions

- Are all your functions pure? How can you tell?
- Where did you use `map` vs list comprehensions? Why?
- How did you handle missing data?
- Could you chain the transformations differently?
