from library import Book, Room, Shelf, organize_by_category
from faker import Faker
import random

def sort_books_in_shelves(room: Room) -> None:
    for shelf in room.shelves:
        shelf.books.sort(key=lambda b: b.title)

if __name__ == "__main__":
    fake = Faker()
    categories = ["Sci-Fi", "Fantasy", "Non-Fiction", "Dystopia", "Romance"]

    room = Room(name="Bob's Room", shelves=[Shelf("A"), Shelf("B"), Shelf("C")])

    pile = {
        Book(
            title=fake.sentence(nb_words=2),
            author=fake.name(),
            category=random.choice(categories)
        )
        for _ in range(10)
    }

    organize_by_category(pile, room)

    print("Not sorted:")
    for sh in room.shelves:
        print(str(sh))

    sort_books_in_shelves(room)

    print("\nSorted:")
    for sh in room.shelves:
        print(str(sh))
