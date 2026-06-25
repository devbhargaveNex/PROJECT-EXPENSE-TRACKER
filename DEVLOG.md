# DEVLOG

## Log 1

**Elapsed Time:** 14h 13m
**Focused Work:** ~2–3h

### Completed

* Set up Git repository.
* Created a virtual environment.
* Created the project structure.
* Implemented the application loop.
* Implemented the Add Expense feature.
* Added temporary in-memory storage.

### Problems

* Current storage structure is inefficient (multiple lists).
* User input has no validation.
* OOP design not implemented yet.

### Decisions

* Keep the current implementation temporarily.
* Refactor to OOP before adding more features.
* Leave exception handling until the core functionality is complete.

### Git

* Merged `feature-add` into `main`.
* Keeping the feature branch until the architecture stabilizes.

### Next Session

* Refactor storage using the `Expense` class.
* Implement `view_expenses()`.
* Test the Add and View features together.

---

## Log 2

**Elapsed Time:** 24h 16m

**Focused Work**

* Session 1: ~2.5–3h
* Session 2: ~2–3h
* **Total:** ~4.5–6h

### Completed

* Refactored the project to use OOP.
* Designed the `Expense` class.
* Understood object creation using `__init__()`.
* Successfully create a new `Expense` object for each new expense.
* Store `Expense` objects in a list.
* Application loop remains functional.
* Add Expense feature works using the new OOP design.
* Continued using Git workflow with feature branches and merges.

### Problems Encountered

* Didn't understand how objects should be stored.
* Tried converting objects back into lists.
* Confused about saving objects directly to text files.
* Unsure how constructors (`__init__()`) receive arguments.

### Key Realizations

* Every expense should be its own object.
* A Python list can directly store objects.
* Objects are accessed by iterating through the list.
* `__init__()` receives arguments automatically when an object is created.
* Constructors eliminate the need to create an empty object and populate it later.
* File storage should serialize object data, not store the object itself.

### Decisions

* Prioritize OOP implementation before persistent file handling.
* Finish the in-memory architecture first.
* Implement save/load after the object model is stable.

### Git

* Continued development using feature branches.
* Merged completed work into `main`.

### Next Session

* Implement View Expenses using `Expense` objects.
* Implement Save functionality.
* Implement loading `Expense` objects from `expenses.txt`.
* Add exception handling where necessary.
