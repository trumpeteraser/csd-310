import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'pysports_user',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'pysports',
    'raise_on_warnings': True
}
try:
    db = mysql.connector.connect(**config)
    if db.is_connected():
        #print('\n Database user {} connected to MySQL on host {} with database {}'.format(config['user'], config['host'], config['database']))
        cursor = db.cursor()
        cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
        players = cursor.fetchall()
        print("-- DISPLAYING PLAYER RECORDS --")
        for player in players:
#            print(player)
            print("Player ID: {}".format(player[0]))
            print("First Name: {}".format(player[1]))
            print("Last Name: {}".format(player[2]))
            print("Team ID: {}".format(player[3]),"\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('  The supplied username or password are invalid.')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('  The specified database does not exist.')
    
    else:
        print(err)