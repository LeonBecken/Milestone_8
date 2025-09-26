# UML: Book Catalog (Bob's Room)

```mermaid
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
  +__str__(): str
}

class Room {
  +name: str
  +shelves: List[Shelf]
  +ensure_category_assignment(category: str): Shelf
}

class LibraryFunctions {
  +organize_by_category(books: set[Book], room: Room) -> Dict[str, Shelf]
  +sort_books_in_shelves(room: Room) -> None
  +print_room_structure(room: Room) -> None
  +generate_books(n: int, categories: List[str], seed: Optional[int]) -> set[Book]
}

Room "1" o-- "*" Shelf : contains
Shelf "1" o-- "*" Book  : stores
