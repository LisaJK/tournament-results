from tournament import *
import random

# you can change the test by changing the number of players (e.g. to an odd number or even number)
the_players = ['Donald', 'Daisy', 'April', 'May', 'June', 'Huey', 'Dewey', 'Louie', 'Scrooge']
# if set to True draws are possible
draw_possible = True


def test():
    # drop and create tables and views in database tournament
    dropAndCreateDB()
    
    # register the players
    for player in the_players:
        registerPlayer(player)

    # count the players
    count = countPlayers()
    print 'Count: ' + str(count)
    if count != len(the_players):
        print 'Players have not been registered correctly!'

    round = 1
    pairs = swissPairings()
    
    while pairs:
        printPlayerStandings(round)
        print '\nRound: ' + str(round)
        round = round + 1
        pairs = swissPairings()
        for pair in pairs:
            print pair
            reportRandomMatchResult(pair[0], pair[2])

def reportRandomMatchResult(player1, player2):
    # check bye (player1 gets free win)
    if player2 is None:
        reportMatch(player1, None, player1)
    else:
        # either one of the players is the winner or it is a draw
        if draw_possible:
            reportMatch(player1, player2, random.choice([player1, player2, None]))
        else: 
            reportMatch(player1, player2, random.choice([player1, player2]))

def printPlayerStandings(round):
    player_standings = playerStandings()
    print '\nPlayer Standings before round ' + str(round)
    print 'Player Id, Player Name, Points, Opponent Match Wins, Matches'
    row_format ="{:>15}" * (len(player_standings) + 1)
    for player in player_standings:
        print player


def dropAndCreateDB():
    # read the file
    fd = open('tournament_lisa.sql', 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')
    
    db = connect()
    c = db.cursor()
    
    # Execute every command from the input file
    for command in sqlCommands:
        # do not execute empty queries
        strippedCommand = command.strip()
        if strippedCommand:
            # skip over drop commands if nothing to drop
            try:
                c.execute(strippedCommand)
            except Exception, msg:
                print 'Command skipped: ', msg
    db.commit()
    db.close()

if __name__ == '__main__':
    test()
    
    

