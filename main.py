import database
print(database.db_obj.fetch("SELECT * FROM sensor LIMIT 5"))

for index, entry in enumerate(database.db_obj.fetch("SELECT * FROM sensor LIMIT 5")):
    print(index, entry)