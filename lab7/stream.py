
# This code doesn't work but offers a head start
def main():
    username = input("Enter your username: ")
    watchlist = Watchlist(username)
    
    # Create some sample content.
    # Read the streamflix.csv rather than hand-code each item in the array.
    content_library = [
        Movie(...),
        Movie(...),
        Series(...),
    ]
    
    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            browse_content(content_library, watchlist)
        elif choice == "2":
            view_watchlist(watchlist)
        # ... etc
        elif choice == "6":
            break