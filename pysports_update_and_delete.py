import mysql.connector
from mysql.connector import errorcode
import time

config = {
    'user': 'pysports_user',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'pysports',
    'raise_on_warnings': True
}
#INSERT Smeagol
db = mysql.connector.connect(**config)
cursor = db.cursor()
sql = ("INSERT INTO player (player_id, first_name, last_name, team_id) VALUES (%s, %s, %s, %s)")
val = ("021", "Smeagol", "Shire Folk", "2")
cursor.execute(sql, val)
db.commit()
print("\n",cursor.rowcount, "record(s) affected\n")
print("Smeagol added!\n")

#Shows all players in the database
cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()
print("-- DISPLAYING PLAYERS AFTER INSERT --")
for player in players:
#            print(player)
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}".format(player[3]),"\n")
input("Press the enter key to update Smeagol's record.\n")

#UPDATE Smeagol to Gollum
db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
db.commit()
print(cursor.rowcount, "record(s) affected\n")

#Shows all players in the database after Smeagol is updated
cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()
print("-- DISPLAYING PLAYERS AFTER UPDATE --")
for player in players:
#            print(player)
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}".format(player[3]),"\n")
input("Press the enter key to delete Gollum.\n")

#Delete Gollum
db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")
db.commit()
print(cursor.rowcount, "record(s) affected\n")

#Shows all players in the database after Gollum is deleted
cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()
print("-- DISPLAYING PLAYERS AFTER DELETE --")
for player in players:
#            print(player)
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}".format(player[3]),"\n")

print("Smeagol deleted!\n")
