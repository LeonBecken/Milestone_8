from dataclasses import dataclass, field
from typing import List, Set, Dict, Optional
from faker import Faker
import random

@dataclass(frozen=True)
class Book:

    title: str
    author: str
    category: str

@dataclass
class Shelf:

    name: str
    categories: Set[str] = field(default_factory=set)
    books: List[Book] = field(default_factory=list)

    def assign_category(self, category: str) -> None:
        """Mark this shelf as responsible for a given category."""
        self.categories.add(category)

    def add_book(self, book: Book) -> None:
        """Put a book on this shelf."""
        self.books.append(book)

    def __str__(self) -> str:
        cats = ", ".join(sorted(self.categories)) or "—"
        titles = ", ".join(b.title for b in self.books) or "—"
        return f"Shelf({self.name}) | categories: [{cats}] | books: [{titles}]"

@dataclass
class Room:

    name: str
    shelves: List[Shelf] = field(default_factory=list)

    def ensure_category_assignment(self, category: str) -> Shelf:

        for sh in self.shelves:
            if category in sh.categories:
                return sh
        if not self.shelves:
            raise ValueError("Room has no shelves to place books on.")
        target = min(self.shelves, key=lambda s: (len(s.categories), len(s.books), s.name))
        target.assign_category(category)
        return target

# ---------------------- Use-cases / utilities ----------------------

def organize_by_category(books: set[Book], room: Room) -> Dict[str, Shelf]:

    category_to_shelf: Dict[str, Shelf] = {}
    for book in books:
        shelf = category_to_shelf.get(book.category)
        if shelf is None:
            shelf = room.ensure_category_assignment(book.category)
            category_to_shelf[book.category] = shelf
        shelf.add_book(book)
    return category_to_shelf

def sort_books_in_shelves(room: Room) -> None:

    for shelf in room.shelves:
        shelf.books.sort(key=lambda b: b.title)

def print_room_structure(room: Room) -> None:

    print(f"\n📚 Room: {room.name}")
    for shelf in room.shelves:
        print(f"  🗂 Shelf: {shelf.name} | Categories: {', '.join(sorted(shelf.categories)) or '—'}")
        if shelf.books:
            for book in shelf.books:
                print(f"     - {book.title} (by {book.author}, category: {book.category})")
        else:
            print("     [empty shelf]")

def generate_books(n: int,
                   categories: List[str],
                   seed: Optional[int] = None) -> set[Book]:

    if seed is not None:
        random.seed(seed)
        fake = Faker()
        fake.random.seed(seed)
    else:
        fake = Faker()

    books = {
        Book(
            title=fake.sentence(nb_words=2),
            author=fake.name(),
            category=random.choice(categories)
        )
        for _ in range(n)
    }
    return books
