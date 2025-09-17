from dataclasses import dataclass, field
from typing import List, Set

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
        self.categories.add(category)

    def add_book(self, book: Book) -> None:
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

def organize_by_category(books: set[Book], room: Room):
    category_to_shelf = {}
    for book in books:
        shelf = category_to_shelf.get(book.category)
        if shelf is None:
            shelf = room.ensure_category_assignment(book.category)
            category_to_shelf[book.category] = shelf
        shelf.add_book(book)
    return category_to_shelf
