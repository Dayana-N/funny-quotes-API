# Funny API
A basic api application using FastApi. It returns fun phrases based on the day of the week. Some phrases may include grown up language and introvert vibes. Enjoy!
![img](./meme.jpg)

### Categories
The phrases are categorised by day of the week. Please see example below

### Response:

````
[
  {
    "id": 30,
    "phrase": "Wednesday: one step closer to freedom, one more fuck lost.",
    "category": "Wednesday"
  }
]
````

### Endpoints

Please note: `{}` represent variables.

#### Available Methods:

- **GET**

#### Paths:

- `/`  
  - Returns a random phrase.
  
- `/{category}/random`  
  - Returns a random phrase from the specified category.

- `/{category}/all`  
  - Returns all phrases from the specified category.

- `/category={category}/{number}`  
  - Returns the specified number of phrases for the given category.

- `/id/{id}`  
  - Returns a phrase with the specified ID.

### To run the project
Activate new virtual environment
Install the dependencies from requirements.txt
To run the projecttype in the terminal ``fastapi dev main.py``

#### Future features
The project stores the phrases locally in a .py file. As the project expands in the future, database should be implemented.