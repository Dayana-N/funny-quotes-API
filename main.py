import random

from fastapi import FastAPI, HTTPException

from phrases import phrases

app = FastAPI()


@app.get("/")
def root():
    """Returns random phrase"""
    random_phrase = random.choice(phrases)
    return [random_phrase]

@app.get("/{category}/random")
def random_phrase_category(category:str):
    """
    Returns random phrase based on category, 
    if no category is found returns exception with status 404
    """
    categorised_phrases = []
    for item in phrases:
        if item["category"] == category.capitalize():
            categorised_phrases.append(item)

    if not categorised_phrases:
        raise HTTPException(status_code = 404, detail = f"No such category {category}")
        
    random_phrase = random.choice(categorised_phrases)
    return [random_phrase]


@app.get("/{category}/all")
def all_phrases_category(category: str):
    """Returns all phrases in category"""
    categorised_phrases = []
    for item in phrases:
        if item["category"] == category.capitalize():
            categorised_phrases.append(item)

    if not categorised_phrases:
        raise HTTPException(status_code = 404, detail = f"No such category {category}")
        
    return categorised_phrases


@app.get("/category={category}/{number}")
def get_amount_phrases_category(category: str, number: str):
    """Returns the given amount of phrases per category"""
    try:
        number_phrases = int(number)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = f"{e}")

    categorised_phrases = []
    for item in phrases:
        if item["category"] == category.capitalize():
            categorised_phrases.append(item)

    if not categorised_phrases:
        raise HTTPException(status_code = 404, detail = f"No such category {category}")
    elif number_phrases > len(categorised_phrases):
        return categorised_phrases
    else:
        return categorised_phrases[:abs(number_phrases)]

@app.get("/id/{id}")
def get_phrase_by_id(id:str):
    """Returns phrase with the corresponding id"""
    try:
        phrase_id = int(id)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = f"{e}")
    for item in phrases:
        if item["id"] == phrase_id:
            return [item]
    return []

