import pandas as pd

people = pd.read_json("/Users/edouardlacroix/Desktop/star wars/people.json")
print(people.head())

people = people.drop(
    columns=[
        "hair_color", 
        "skin_color", 
        "eye_color", 
        "birth_year", 
        "films", 
        "vehicles", 
        "created", 
        "edited", 
        "url", 
        "starships"
        ]
    )
print("CHARACTERS TABLE")
print(people.head())

species = pd.read_json("/Users/edouardlacroix/Desktop/star wars/species.json")
species = species.drop(
    columns=[
        "classification",
        "designation",
        "average_height",
        "skin_colors",
        "hair_colors",
        "eye_colors",
        "average_lifespan",
        "language",
        "films",
        "created",
        "edited"
        ]
    )
print("SPECIES TABLE")
print(species.head())

people = people.rename(columns={"species" : "species_url"})
people["species"] = None
people["species_url_clean"] = people["species_url"].apply(
    lambda x: x[0] if isinstance(x, list) and len(x) > 0 else None
)
people = people.drop(columns="species_url")
print("CHARACTERS TABLE")
print(people.head())

species_dic = dict(zip(species["url"], species["name"]))
print(species_dic)

people["species"] = people["species_url_clean"].map(species_dic)
people = people.drop(columns="species_url_clean")
people["species"] = people["species"].fillna("Human")
print("CHARACTERS TABLE")
print(people)

planets = pd.read_json("/Users/edouardlacroix/Desktop/star wars/planets.json")
people = people.rename(columns={"homeworld" : "homeworld_url"})
people["homeworld"] = None
print("HOMEWORLDS TABLE")
print(planets.head())

homeworld_dic = dict(zip(planets["url"], planets["name"]))
print(homeworld_dic)

people["homeworld"] = people["homeworld_url"].map(homeworld_dic)
people = people.drop(columns="homeworld_url")
print(people.head())

people["height"] = pd.to_numeric(people["height"], errors="coerce")
people["mass"] = pd.to_numeric(people["mass"], errors="coerce")
people = people.dropna(subset=["height", "mass"])

print(people.head())
print(people["species"].value_counts())
print(people["homeworld"].value_counts())

people.to_csv("people_v2_enriched.csv", index=False)

