from library import Book, Shelf, Room
from library import organize_by_category, sort_books_in_shelves, print_room_structure, generate_books

if __name__ == "__main__":
    categories = ["Sci-Fi", "Fantasy", "Non-Fiction", "Dystopia", "Romance"]

    room = Room(name="Bob's Room", shelves=[Shelf("A"), Shelf("B"), Shelf("C")])

    # Generation is a separate function (per curator requirement)
    pile = generate_books(n=10, categories=categories, seed=42)

    organize_by_category(pile, room)

    print("\n=== Before sorting ===")
    print_room_structure(room)

    sort_books_in_shelves(room)

    print("\n=== After sorting ===")
    print_room_structure(room)

