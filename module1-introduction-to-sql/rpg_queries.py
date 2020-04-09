import sqlite3

DB_FILEPATH = ""



query1 = "SELECT
count(name) as character_count
FROM charactercreator_character"

query2 = "SELECT
count(DISTINCT charactercreator_cleric.character_ptr_id) as cleric,
count(DISTINCT charactercreator_fighter.character_ptr_id) as fighter,
count(DISTINCT charactercreator_mage.character_ptr_id) as mage,
count(DISTINCT charactercreator_necromancer.mage_ptr_id) as necromancer,
count(DISTINCT charactercreator_thief.character_ptr_id) as thief
FROM
charactercreator_cleric,
charactercreator_fighter,
charactercreator_mage,
charactercreator_necromancer,
charactercreator_thief"

query3 = "SELECT
count(DISTINCT armory_item.name) as total_items
FROM armory_item"

query4 = "SELECT
count(b.item_ptr_id) as weapon,
count(*) - count(b.item_ptr_id) as not_weapon
FROM armory_item a
LEFT JOIN armory_weapon b ON a.item_id = b.item_ptr_id"

query5 = "SELECT
a.character_id,
COUNT(b.character_id) as items_per_charcter
FROM charactercreator_character a
JOIN charactercreator_character_inventory b ON a.character_id = b.character_id
GROUP BY 1
LIMIT 20"

query6 = "SELECT
COUNT(c.item_ptr_id) as weapons
FROM charactercreator_character a
JOIN charactercreator_character_inventory b ON a.character_id = b.character_id
LEFT JOIN armory_weapon c ON c.item_ptr_id = b.item_id
"

query7 = ""