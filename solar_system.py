import os
import requests

os.system('clear')
def getData(): 
    print(":::SOLAR SYSTEM DATA:::")
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"

    try:
        #Request to API
        response = requests.get(url)
        response.raise_for_status()
        #Object to JSON (JS Object Notation)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")

def showPlanets():
    data = getData()
    print("\n::: PLANETS :::")
    planets= [b for b in data["bodies"] if b["isPlanet"] and b["sideralOrbit"] is not None]
    sortedPlanets = sorted(planets, key=lambda p: p["sideralOrbit"])
    for b in sortedPlanets:
        print("-", b["englishName"])

def showMoons():
    data = getData()
    moonsByPlanet = {}
    print("\n::: MOONS :::")
    for b in data["bodies"]:
        if b.get("aroundPlanet"):
            planetName = b["aroundPlanet"]["planet"]
            moonName = b["englishName"]
            if planetName not in moonsByPlanet:
                moonsByPlanet[planetName] = []
            moonsByPlanet[planetName].append(moonName)
    for planet, moons in moonsByPlanet.items():
        print(f"{planet}:")
        for moon in moons:
            print(f"- {moon}")

def showStars():
    data = getData()
    print("\n::: STARS :::")
    for b in data.get("bodies", []):
        if b.get("bodyType") == "Star":
            print("-", b["englishName"])

def showAsteroids():
    data = getData()
    print("\n::: ASTEROIDS :::")
    for b in data.get("bodies", []):
        if b.get("bodyType") == "Asteroid":
            print("-", b["englishName"])

def showComets():
    data = getData()
    print("\n::: COMETS :::")
    for b in data.get("bodies", []):
        if b.get("bodyType") == "Comet":
            print("-", b["englishName"])

def mainMenu():
    while True:
        screen = '''
:::: SOLAR SYSTEM MENU ::::
    [1]. Planets
    [2]. Moons
    [3]. Stars
    [4]. Asteroids
    [5]. Comets
    [6]. Salir'''
        print(screen)

        option = input("Choose an option: ")
        if option == "1":
            showPlanets()
        elif option == "2":
            showMoons()
        elif option == "3":
            showStars()
        elif option == "4":
            showAsteroids()
        elif option == "5":
            showComets()
        elif option == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")



mainMenu()