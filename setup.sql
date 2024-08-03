CREATE TABLE task(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128),
    summary VARCHAR(256),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

--Insert some dummy data to test the tabel

INSERT INTO task(
    name,
    summary,
    description
    
) VALUES(
    "Wash car",
    "The car needs to be washed",
    "Make sure the car gets waxed after it is washed"
    
), (
    "Walk the dog",
    "Rocky needs their exercise",
    "Make sure to do at least 2 laps around the park"
    
), (
    "Buy Groceries",
    "Go to the supermarket and buy groceries",
    "We need: Eggs, Milk, Cereal, and Coffee"
    
);