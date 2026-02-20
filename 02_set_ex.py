# Actors in Marvel Cinematic Universe (Main Avengers)
actors_mcu = {
    "Robert Downey Jr.",
    "Chris Evans",
    "Chris Hemsworth",
    "Mark Ruffalo",
    "Scarlett Johansson",
    "Jeremy Renner",
    "Tom Hiddleston",
    "Benedict Cumberbatch",
    "Paul Rudd",
    "Brie Larson",
    "Chadwick Boseman"
}

# Actors in DC Extended Universe
actors_dceu = {
    "Henry Cavill",
    "Ben Affleck",
    "Gal Gadot",
    "Jason Momoa",
    "Ezra Miller",
    "Ray Fisher",
    "Margot Robbie",
    "Will Smith",
    "Jared Leto",
    "Zachary Levi"
}

# Actors who have done superhero movies in general (including non-MCU/DCEU)
actors_superhero = {
    "Robert Downey Jr.",
    "Chris Evans",
    "Christian Bale",  # Batman (Dark Knight Trilogy)
    "Tobey Maguire",  # Spider-Man
    "Andrew Garfield",  # Spider-Man
    "Hugh Jackman",  # X-Men
    "Patrick Stewart",  # X-Men
    "Ian McKellen",  # X-Men
    "Ryan Reynolds",  # Deadpool
    "Michael Keaton",  # Batman
    "Ben Affleck",
    "Gal Gadot"
}

print("\n🦸 Actors in Marvel Cinematic Universe:")
print(actors_mcu)

print("\n🦇 Actors in DC Extended Universe:")
print(actors_dceu)

print("\n🎭 Actors in superhero movies (any franchise):")
# {1 2 3} | {3 4 5} = {1 2 3 4 5}
print(actors_mcu | actors_dceu | actors_superhero)  # | = JOIN

print("\n❓ Are there any actors in BOTH MCU and DCEU?")
# {1 2 3} & {3 4 5} = {3}
print(actors_mcu & actors_dceu)  # & = MUST BE IN BOTH GROUPS

print("\n❓ Actors in superhero movies but NOT in MCU?")
# {1 2 3} - {3 4 5} = {1 2}
print(actors_superhero - actors_mcu)  # MUST BE only in left group

# { 1 2 } <= { 1 2 } True
# { 1 2 } <= { 1 2 3} True
# { 1 2 3} <= { 1 2 4 5 6} FALSE
print("\n❓ Is the DCEU set a subset of any superhero actors?")
print(actors_dceu <= actors_superhero) # Boolean

print("\n❓ Actors ONLY in MCU (not in other franchises)?")
print(actors_mcu - actors_dceu - actors_superhero)
print(actors_mcu - (actors_dceu | actors_superhero))

# { 1 2 } >= { 1 2 } True
# { 1 2 } >= { 1 2 3} FALSE
# { 1 2 3} >= { 1 2 4 5 6} FALSE
print("\n❓ Is superhero_actors a superset of DCEU?")
print(actors_superhero >= actors_dceu)