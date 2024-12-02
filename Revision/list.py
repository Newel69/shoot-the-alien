my_favorites=["basketball", "brawl stars", 18, "imagine dragons"]
print(my_favorites)
print(my_favorites[2])
#looping through a list
for i in my_favorites:
    print(i)
#adding an item inside a list
my_favorites.append("lord of the rings")
print(my_favorites)
#updating an item inside a list
my_favorites[2]="peach"
print(my_favorites)
#removing an item from a list
#remove method
my_favorites.remove("peach")
print(my_favorites)
#pop method
poped=my_favorites.pop(1)
print(my_favorites)