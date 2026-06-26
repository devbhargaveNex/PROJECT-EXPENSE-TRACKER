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

---

## Log 3

**Elapsed Time:** ~42h 24m

**Focused Work:**
Session 1: ~2.5–3h
* Session 2: ~2–3h
* Session 3: ~10min
* **Total:** ~4:45–6:45h

### Completed

* Implemented the View Expenses feature.
* Verified that the feature works with the current OOP structure.
* Committed the completed feature.
* Pushed changes to the remote repository.

### Problems

* No major implementation issues encountered.
* Feature integrated cleanly with the existing object-oriented design.

### Decisions

* Continue building one feature at a time.
* Maintain the workflow of:

  * Implement
  * Test
  * Commit
  * Push

### Git

* Merged `feature-view` into `main`.
* Pushed latest changes to GitHub.

### Next Session

* Implement Save functionality.
* Design the load mechanism for `Expense` objects.
* Begin planning the Delete Expense feature.

---

## Log 4

**Elapsed Time:** ~47h 20m

**Focused Work:** 
Session 1: ~2.5–3h
* Session 2: ~2–3h
* Session 3: ~10min
* Session 4: ~10min
* **Total:** ~4:55–6:55h

### Completed

* Implemented the Save feature.
* Application can now write all in-memory `Expense` objects to `expenses.txt`.
* Verified that multiple expenses can be saved successfully.
* Committed and pushed the completed feature.

### Problems Encountered

* Loading data from `expenses.txt` at application startup is not yet implemented.
* Save is currently one-way (memory → file).

### Key Realizations

* Keeping all data in memory and writing it to the file only when saving greatly simplifies the program.
* Separating in-memory data management from file persistence made the save logic much easier to implement.

### Decisions

* Finish the save/load system before implementing additional features.
* Continue treating file handling as a separate layer from the application's core logic.

### Git

* Merged `feature-save` into `main`.
* Pushed the latest changes to GitHub.

### Next Session

* Implement loading expenses from `expenses.txt` when the application starts.
* Recreate `Expense` objects from the saved file.
* Test the full save → close → reopen → load workflow.

---

## Log 5

**Elapsed Time:** ~48h 20m

**Focused Work:** 
Session 1: ~2.5–3h
* Session 2: ~2–3h
* Session 3: ~10min
* Session 4: ~10min
* Session 5: ~1hr
* **Total:** ~5:55–7:55h

### Completed

* Implemented loading of saved expenses from `expenses.txt` at application startup.
* Successfully reconstructed local `Expense` objects from the saved file.
* Reused the existing `add()` logic for both user input and file loading, eliminating duplicate code.
* Verified that previously saved expenses are available in memory after restarting the application.

### Problems Encountered

* Worked through the logic of reading a file line by line.
* Learned how `readline()` behaves at the end of a file and how to detect end-of-file correctly.

### Key Realizations

* Loading data is essentially the reverse of saving data.
* One function can be reused for multiple data sources (user input and file input).
* Reusing existing logic makes future maintenance easier and reduces duplicate code.

### Decisions

* Continue following the DRY (Don't Repeat Yourself) principle.
* Keep file reading responsible only for supplying data, while object creation remains the responsibility of `add()`.

### Git

* Committed the file loading feature.
* Pushed latest changes to GitHub.

### Next Session

* Implement Delete Expense.
* Implement Search Expense.
* Add input validation and exception handling.
* Begin testing the complete application workflow.