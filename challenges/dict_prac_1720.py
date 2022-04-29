#!/usr/bin/env python3

pokedex={"Bulbasaur":"Grass/Poison",
         "Squirtle":"Water",
         "Charmander":"Fire"}

pokedex["Pikachu"]="Electric"

print(", ".join(pokedex.keys()))

choice= input("Name a Generation 1 starter Pokemon:\n>")

print(pokedex.get(choice, "Sorry, we don't have any record of that Pokemon!"))


