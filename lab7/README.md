# Lab 7

## Today's Goal: Build a Streaming Platform Backend, Part 1.

Today, you should try to finish the following:

1. Draw a UML class diagram that showing inheritance and composition. See https://en.wikipedia.org/wiki/Class_diagram

2. Implement requirement #1 below: "Browse available content"

3. As time allows, implement requirements 2-7 below


## Turning In Your Lab / Working With Others

Working with others is encouraged! Only one person in the group needs to turn in your combined work.

If you are turning in the work performed by the group, simply list their names below and include this file in your submission:

* [name]
* [name]

## The Requirements

**Command-Line Interface (CLI)**

Build a simple menu-driven program where users can:

1. Browse available content (show all movies and series)
2. View content details (runtime for movies, episode count for series)
3. Add content to their watchlist
4. View their watchlist
5. Filter their watchlist by genre
6. "Watch" content (which records a view)
7. See platform statistics

## Sample Terminal Session

Here's what your program might look like when running:

```
$ python streamflix.py

=== Welcome to StreamFlix ===

Enter your username: alex

Hello, alex!

--- Main Menu ---
1. Browse all content
2. View my watchlist
3. Filter watchlist by genre
4. Watch something
5. Platform statistics
6. Quit

Choose an option: 1

=== All Available Content ===
[1] The Matrix (1999) - 8.7★
[2] Inception (2010) - 8.8★
[3] The Dark Knight (2008) - 9.0★
[4] Stranger Things (2016) - 8.7★ [Series]
[5] Breaking Bad (2008) - 9.5★ [Series]

Enter a number for details, or 'b' to go back: 1

--- The Matrix (1999) - 8.7★ ---
Type: Movie
Genres: Action, Sci-Fi
Runtime: 139 minutes
Director: Wachowski Sisters
Views: 0
Feature length: Yes

Options:
[a] Add to watchlist
[w] Watch now
[b] Back to browse

Choose: a

✓ Added "The Matrix" to your watchlist!

Options:
[a] Add to watchlist (already added)
[w] Watch now
[b] Back to browse

Choose: w

▶ Now watching: The Matrix (1999)
✓ View recorded!

[Press Enter to continue]

--- Main Menu ---
1. Browse all content
2. View my watchlist
3. Filter watchlist by genre
4. Watch something
5. Platform statistics
6. Quit

Choose an option: 2

=== alex's Watchlist ===
Average rating: 8.7

[1] The Matrix (1999) - 8.7★
    Views: 1

Options:
[s] Sort by rating
[f] Filter by genre
[r] Remove item
[b] Back to main menu

Choose: b

--- Main Menu ---
1. Browse all content
2. View my watchlist
3. Filter watchlist by genre
4. Watch something
5. Platform statistics
6. Quit

Choose an option: 3

Enter genre to filter by: Sci-Fi

=== Sci-Fi content in your watchlist ===
[1] The Matrix (1999) - 8.7★

[Press Enter to continue]

--- Main Menu ---
1. Browse all content
2. View my watchlist
3. Filter watchlist by genre
4. Watch something
5. Platform statistics
6. Quit

Choose an option: 5

=== Platform Statistics ===
Total content items: 5
Total platform views: 1
Most viewed: The Matrix (1 views)

[Press Enter to continue]

--- Main Menu ---
1. Browse all content
2. View my watchlist
3. Filter watchlist by genre
4. Watch something
5. Platform statistics
6. Quit

Choose an option: 6

Thanks for using StreamFlix! Goodbye, alex.

$
```


## The Idea

StreamFlix, a new streaming service, needs you to build their content management system. They've provided requirements below. Your job is to:

* Identify the classes needed (which concepts deserve to be classes?)
* Determine relationships (inheritance vs composition - is-a vs has-a)
* Design the interface (what methods does each class need?)
* Implement it using OOP principles

**1. Content Management**

* The platform offers two types of content: movies and series.
* Both types share common attributes: title, release year, rating (0-10), and a list of genres
* Movies have a runtime in minutes and a director
* Series have multiple seasons, and each season has a different number of episodes
* Series can be "ongoing" or "completed"
* The platform needs to track how many times each piece of content has been viewed
* Business analytics wants to know total views across the entire platform

**2. User Features**

Users can create personal watchlists to save content they want to watch later.

Each watchlist belongs to one user (identified by username).

Users should be able to:

* Add content to their watchlist (but not add the same thing twice)
* Remove content from their watchlist
* Find all content in their watchlist matching a specific genre
* See the average rating of everything in their watchlist
* View their watchlist sorted by rating (highest first)

**3. Discovery & Display**

Content should display nicely when printed, showing: title, year, and rating with a star.

Example: "The Matrix (1999) - 8.7★"

* The system needs to identify if a movie qualifies as "feature length" (over 80 minutes)
* Users should be able to check if any content matches a genre they're interested in
* For series, users want to know the total number of episodes across all seasons

**4. Analytics**

* Every time someone watches content, it should increment that content's view count
* The business team needs to track total views platform-wide, not tied to any specific content

