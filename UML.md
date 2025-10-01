```mermaid
classDiagram
%% ==== Domain Entities ====
class Author {
  +id: str
  +name: str
  +country: str
}

class Book {
  +id: str
  +title: str
  +author: Author
  +category: str
  +year: int
  +pages: int
}

class Shelf {
  +name: str
  +categories: Set~str~
  +books: List~Book~
  +assign_category(category: str): void
  +add_book(book: Book): void
  +__str__(): str
}

class Room {
  +name: str
  +shelves: List~Shelf~
  +ensure_category_assignment(category: str): Shelf
}

%% ==== Use-case / Utilities (functions) ====
class LibraryFunctions {
  +organize_by_category(books: set~Book~, room: Room) -> Dict~str, Shelf~
  +sort_books_in_shelves(room: Room) -> void
  +print_room_structure(room: Room) -> void
  +generate_books(n: int, categories: List~str~, seed: Optional~int~) -> set~Book~
}

%% ==== Relations ====
Room "1" o-- "*" Shelf : contains
Shelf "1" o-- "*" Book  : stores
Book  "many" *-- "1" Author : written by
