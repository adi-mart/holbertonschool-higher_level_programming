#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

# TODO: 1. Importer MySQLdb
# TODO: 2. Récupérer les arguments (username, password, dbname, state_name)
# TODO: 3. Se connecter à la base de données hbtn_0e_0_usa sur localhost:3306
# TODO: 4. Exécuter la requête SQL (avec format) pour sélectionner les états dont le nom correspond à l'argument, triés par id croissant
# TODO: 5. Afficher chaque état sous la forme (id, 'name')
# TODO: 6. Ne pas exécuter le code si le fichier est importé

import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server on localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name, states=state_name)
    cur = db.cursor()

    # Execute query and fetch results sorted by id (ascending)
    cur.execute("SELECT * FROM states WHERE name = %s")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
