import sqlite3
import asyncio

conn = sqlite3.connect('heroes.db')
cur = conn.cursor()
cur.execute("SELECT * FROM `heroes` WHERE `name` = name")
heroName = cur.fetchall()

maxHeroCount = heroName[62][0]

heroesNames = []
heroesInfo = []
heroesFraction = []
heroesRole = []
heroesFullInfo = []
for el in range(maxHeroCount):
    heroesNames.append(heroName[el][1])
    heroesInfo.append(heroName[el][2])
    heroesFraction.append(heroName[el][3])
    heroesRole.append(heroName[el][4])

for el in range(maxHeroCount):
    heroesFullInfo.append({
    "Имя" : heroesNames[el],
    "РвК" : heroesInfo[el],
    "Фракция" : heroesFraction[el],
    "Роль" : heroesRole[el],
    })

print("[Log]: "+"Heroes count: " + str(maxHeroCount))
print("[Log]: "+"Images loaded: " + str(maxHeroCount))
#print(heroesFullInfo[3]['Роль'])
#print(heroesNames)
