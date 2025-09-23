character_ = [
        ("name", "What is the character's **Name**?"),
        ("class", "What is the character's **Class**"),
        ("level", "What is the character's **Level**"),
        ("race", "What is the character's **Race**"),
        ("alignment", "What is the character's **Alignment**"),
        ("player", "What is the character's **Player**"),
        ("strg", "What is the character's **Strength**"),
        ("dex", "What is the character's **Dexterity**"),
        ("con", "What is the character's **Constitution**"),
        ("intel", "What is the character's **Intelligence**"),
        ("wis", "What is the character's **Wisdom**"),
        ("cha", "What is the character's **Charisma**"),
        ("proficiency", "What is the character's **Proficiency Bonus**"),
        ("ac", "What is the character's **Armor Class**"),
        ("initiative", "What is the character's **Initiative Bonus**"),
        ("speed", "What is the character's **Speed**")]

weapon_ = [
    ("name", "What is the weapon's **Name**?"),
    ("cost", "What is the weapon's **Cost**?"),
    ("damage", "What is the weapon's **Damage**?"),
    ("weight", "What is the weapon's **Weight**?"),
    ("properties", "What are the weapon's **Properties**?"),
    ("type","What **type** is the weapon(Ranged or Melee)")
]

get_weapons =  "Select * FROM Weapons WHERE GuildID = %s"

get_characters = "Select `Character Name` FROM Characters WHERE GuildID = %s"

select_weapon_name = "Select Name FROM Weapons WHERE GuildID = %s"

add_campaign = "INSERT Into `Campaigns` (`GuildID`,`Name`) \
                    VALUES (%s,%s)"

weapon_insert = """INSERT INTO `Weapons` (`Name`, `Cost`, `Damage`, `Weight`, `Properties`, `Type`,`GuildID` ) \
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""

char_insert = """INSERT INTO `Characters` (`Character Name`, `Class`, `Level`, `Race`, `Alignment`, `Player Name`, \
                                               `Strg`, `Dex`, `Con`, `Intel`, `Wis`, `Cha`, \
                                               `Proficiency Bonus`, `AC`, `Initiative`, `Speed`, `GuildID`) \
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

