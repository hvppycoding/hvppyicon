import hvppyicon

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "brown",
    "gray",
]

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for alphabet in alphabets:
    for color in colors:
        filename = f"{alphabet}_{color}.png"
        hvppyicon.run(color=color, text=alphabet, output=f"images/{filename}")
        print(f"![{filename}](doc/images/{filename})")
    