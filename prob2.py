def library_analysis(records):
    # Dictionary to store book titles and their total borrowed days
    book_borrow_data = {}

    # Process each record to populate the dictionary
    for record in records:
        title, days = record.split(" - ")
        days = int(days)  # Convert days to an integer (casting)

        if title in book_borrow_data:
            book_borrow_data[title] += days
        else:
            book_borrow_data[title] = days

    # Calculate the most and least borrowed books
    most_borrowed = max(book_borrow_data.items(), key=lambda x: x[1])
    print(f"Most Borrowed Book: {most_borrowed[0]} with {most_borrowed[1]} days")
    least_borrowed = min(book_borrow_data.items(), key=lambda x: x[1])
    print(f"Least Borrowed Book: {least_borrowed[0]} with {least_borrowed[1]} days")

    # Calculate the average borrowing time
    total_days = sum(book_borrow_data.values())
    total_books = len(book_borrow_data)
    average_days = total_days / total_books
    print(f"Average Borrowing Time: {average_days:.2f} days")

    # Find the unique titles of all borrowed books
    unique_titles = set(book_borrow_data.keys())
    print(f"Unique Titles: {', '.join(unique_titles)}")

    # Sort books by the number of days borrowed in descending order
    sorted_books = sorted(book_borrow_data.items(), key=lambda x: x[1], reverse=True)
    print("Books Sorted by Borrowing Duration (Descending):")
    for title, days in sorted_books:
        print(f"{title}: {days} days")

records = [
    "Harry Potter - 12",
    "The Hobbit - 8",
    "Harry Potter - 5",
    "1984 - 15",
    "The Catcher in the Rye - 6",
    "The Hobbit - 7"
]

library_analysis(records)