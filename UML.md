classDiagram
class Book {
  +title: str
  +author: str
  +category: str
}

class Shelf {
  +name: str
  +categories: Set[str]
  +books: List[Book]
  +assign_category(category: str): void
  +add_book(book: Book): void
}

class Room {
  +name: str
  +shelves: List[Shelf]
  +ensure_category_assignment(category: str): Shelf
}

Room "1" o-- "*" Shelf : contains
Shelf "1" o-- "*" Book  : stores
