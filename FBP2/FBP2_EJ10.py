bandas = {
    "Queen": ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"],
    "The Doors": ["Jim Morrison", "Robby Krieger", "Ray Manzarek", "John Densmore"],
    "Green Day": ["Billie Joe Armstrong", "Mike Dirnt", "Tré Cool"],
    "Rolling Stones": ["Mick Jagger", "Keith Richards", "Charlie Watts", "Ron Wood"],
    "Led Zeppelin": ["Robert Plant", "Jimmy Page", "John Paul Jones", "John Bonham"],
    "Black Sabbath": ["Ozzy Osbourne", "Tony Iommi", "Bill Ward", "Geezer Butler"],
    "Soundgarden": ["Chris Cornell", "Kim Thayil", "Matt Cameron", "Ben Shepherd"],
    "Alice in Chains": ["Layne Staley", "Jerry Cantrell", "Sean Kinney", "Mike Starr"]
}


bandas_ordenadas = sorted(bandas.keys())

for banda in bandas_ordenadas:
    vocalista = bandas[banda][0]
    print(f"{banda}: {vocalista}")