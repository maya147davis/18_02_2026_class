# ============================================================================
# EXAMPLE 1: MOVIES - Oscar Winners
# ============================================================================
print("=" * 80)
print("EXAMPLE 1: MOVIES - Oscar Winners")
print("=" * 80)

# Movies that won Best Actor Oscar (2010s-2020s)
movies_best_actor = {
    "The King's Speech",  # Colin Firth (2011)
    "The Artist",  # Jean Dujardin (2012)
    "Lincoln",  # Daniel Day-Lewis (2013)
    "Dallas Buyers Club",  # Matthew McConaughey (2014)
    "The Theory of Everything",  # Eddie Redmayne (2015)
    "The Revenant",  # Leonardo DiCaprio (2016)
    "Manchester by the Sea",  # Casey Affleck (2017)
    "Darkest Hour",  # Gary Oldman (2018)
    "Bohemian Rhapsody",  # Rami Malek (2019)
    "Joker",  # Joaquin Phoenix (2020)
    "The Father"  # Anthony Hopkins (2021)
}

# Movies that won Best Original Screenplay Oscar (2010s-2020s)
movies_best_screenplay = {
    "The King's Speech",  # (2011)
    "Midnight in Paris",  # (2012)
    "Django Unchained",  # (2013)
    "Her",  # (2014)
    "Birdman",  # (2015)
    "Spotlight",  # (2016)
    "Manchester by the Sea",  # (2017)
    "Get Out",  # (2018)
    "Green Book",  # (2019)
    "Parasite",  # (2020)
    "Promising Young Woman"  # (2021)
}

print("📽️  Movies that won Best Actor:")
print(movies_best_actor)

print()
print("✍️  Movies that won Best Screenplay:")
print(movies_best_screenplay)

print("\n❓ How to find which movies won BOTH Best Actor AND Best Screenplay?")
# best_both = set()
# for movie in movies_best_actor:
#     if movie in movies_best_screenplay:
#         best_both.add(movie)
best_both = movies_best_actor & movies_best_screenplay
print(best_both)

print("\n❓ How to find ALL movies that won either award?")
# print(set(list(movies_best_actor) + list(movies_best_screenplay)))
both = movies_best_actor | movies_best_screenplay
print(both)

print("\n❓ Movies that won Best Actor but NOT Best Screenplay?")
# best_actor_not_screenplay = set()
# for movie in movies_best_actor:
#     if movie not in movies_best_screenplay:
#         best_actor_not_screenplay.add(movie)
print(movies_best_actor - movies_best_screenplay)

print("\n❓ Movies that won exactly ONE of the two awards (not both)?")
# one_set_only = set()
# for movie in movies_best_actor:
#     if movie not in movies_best_screenplay:
#         one_set_only.add(movie)
# for movie in movies_best_screenplay:
#     if movie not in movies_best_actor:
#         one_set_only.add(movie)
print(movies_best_actor ^ movies_best_screenplay)

print("\n❓ Are Best Actor winners a subset of movies_best_screenplay?")
print("Python command: movies_best_actor <= movies_best_screenplay")
print(f"Result: {movies_best_actor <= movies_best_screenplay}")
print(f"Result: {(   {1,2} <= {1,2,3}  )}")
print(f"Result: {(   {1,2} <= {1,2}  )}")
print(f"Result: {(   {1,2} <= {1,4,5}  )}")
print(f"Result: {(   {1,2} < {1,2}  )}")

print("\n❓ Are Best Actor winners a superset of movies_best_screenplay?")
print(f"Result: {movies_best_actor >= movies_best_screenplay}")
print(f"Result: {(   {1,2} >= {1,2,3}  )}")
print(f"Result: {(   {1,2} >= {1,2}  )}")
print(f"Result: {(   {1,2} >= {1,4,5}  )}")
print(f"Result: {(   {1,2} > {1,2}  )}")  # FALSE

# Example 1: Disjoint Sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2)) # Output: True

set3 = {3, 4, 5}
print(set1.isdisjoint(set3)) # Output: False