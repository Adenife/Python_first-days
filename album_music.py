'''
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.

'''
def make_album(name, titles, *other):
    music = {"First": name.rstrip(), "Last": titles.rstrip(), "Track": other}
    return music

i = 0
while i < 3:
    input1 = input("Enter Musician Name: ")
    input2 = input("Enter Album Name: ")
    input3 = input("Enter Number of tracks: ")
    message = make_album(input1.title(), input2.title(), int(input3))
    print(message)
    i += 1
