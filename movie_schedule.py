current_movies = {
    'The Grinch': '11:00am',
    'Rudolph': '1:00pm',
    'Frosty the Snowman': '3:00pm',
    'Christina Vaccation': '5:00pm'
}

print("We're showing the following movies:")

for key in current_movies:
    print(key)

movie = input('What movie would you like the showtime for?\n')
showtime = current_movies.get(movie)

if showtime:
    print(movie, "is playing at", showtime)
else:
    print("Requested showtime isn't playing")