import sqlite3
import os

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

conn = sqlite3.connect(DB_FILEPATH)
# conn.row_factory = sqlite3.Row

curs = conn.cursor()

query1 = """SELECT
count(name) as character_count
FROM charactercreator_character"""

query2 = """SELECT
count(distinct c.character_ptr_id) as total_clerics,
count(distinct f.character_ptr_id) as total_fighters,
count(distinct m.character_ptr_id) as total_mages,
count(distinct n.mage_ptr_id) as total_necromancers,
count(distinct t.character_ptr_id) as total_thieves
FROM charactercreator_character ccc
LEFT JOIN charactercreator_fighter f ON ccc.character_id = f.character_ptr_id
LEFT JOIN charactercreator_cleric c ON ccc.character_id = c.character_ptr_id
LEFT JOIN charactercreator_mage m ON ccc.character_id =  m.character_ptr_id
LEFT JOIN charactercreator_necromancer n ON ccc.character_id = n.mage_ptr_id
LEFT JOIN charactercreator_thief t ON ccc.character_id = t.character_ptr_id"""

query3 = """SELECT
count(DISTINCT armory_item.name) as total_items
FROM armory_item"""

query4 = """SELECT
count(b.item_ptr_id) as weapon,
count(*) - count(b.item_ptr_id) as not_weapon
FROM armory_item a
LEFT JOIN armory_weapon b ON a.item_id = b.item_ptr_id"""

query5 = """SELECT
a.character_id,
COUNT(b.character_id) as items_per_charcter
FROM charactercreator_character a
JOIN charactercreator_character_inventory b ON a.character_id = b.character_id
GROUP BY 1
LIMIT 20"""

query6 = """SELECT
COUNT(c.item_ptr_id) as weapons
FROM charactercreator_character a
JOIN charactercreator_character_inventory b ON a.character_id = b.character_id
LEFT JOIN armory_weapon c ON c.item_ptr_id = b.item_id"""

query7 = """SELECT AVG(item_count) as avg_items
FROM (SELECT
c.character_id,
c."name" as character_name,
count(DISTINCT inv.item_id) as item_count
from charactercreator_character c
left join charactercreator_character_inventory inv
ON c.character_id = inv.character_id
GROUP BY 1, 2
) subq"""

query8 = """SELECT AVG(weapons) as avg_weapons
FROM(SELECT
a.character_id,
COUNT(c.item_ptr_id) as weapons
FROM charactercreator_character a
JOIN charactercreator_character_inventory b ON a.character_id = b.character_id
LEFT JOIN armory_weapon c ON c.item_ptr_id = b.item_id
GROUP BY 1
) subq"""

results1 = curs.execute(query1).fetchall()
print("--------------")
print("How many total Characters are there?:", results1)

results2 = curs.execute(query2).fetchall()
print("--------------")
print("How many of each specific subclass?:", results2)

results3 = curs.execute(query3).fetchall()
print("--------------")
print("How many total Items?:", results3)

results4 = curs.execute(query4).fetchall()
print("--------------")
print("How many of the Items are weapons? How many are not?:", results3)

results5 = curs.execute(query5).fetchall()
print("--------------")
print("How many Items does each character have? (Return first 20 rows):", results5)

results6 = curs.execute(query6).fetchall()
print("--------------")
print("How many Weapons does each character have? (Return first 20 rows):", results6)

results7 = curs.execute(query7).fetchall()
print("--------------")
print("On average, how many Items does each Character have?:", results7)

results8 = curs.execute(query8).fetchall()
print("--------------")
print("On average, how many Weapons does each character have?:", results8)
