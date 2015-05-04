A. Project Description

In this project, a Python module that uses the PostgreSQL database can be used to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

B. Implementation Details

The following extra credits are implemented:

1. Draw is possible
   Implementation: Draw counts as 1/2 point, if a match is reported and no winner is given, both players get 1/2 point.

2. Odd number of players is possible
   Implementation: The last player in the player standings not having a "bye" yet gets a free win. A match is reported with only one player, who is also the winner.

3. Opponent Match Win
   Implementation: The player standings are extended and have one extra field containing the total number of wins of all opponents of the player.

The player standings consider:
- points (win points + draw points)
- opponent match wins
- played matches
- player id

C. Files

1. tournament_lisa.sql
This file contains all SQL statements which are necessary to create the tables and views of the database tournament:
- table players
- table matches
- view played_matches
- view won_matches
- view opponent_match_wins
- view player_standings
If the tables and views have been existing before, they are dropped before they are recreated.

2. tournament.py
This file contains the implementation of the Swiss-system tournament. 

3. tournament_test.py
This file contains the (slightly changed, to enable draws) testcases of tournament.py provided by Udacity. To run the testcases, the database tournament and its tables and views must exist before.
To run:
- create a database named tournament (createdb tournament)
- execute the script tournament_lisa.sql (psql tournament -f tournament_lisa.sql)
- run tournament_test.py (python tournament_test.py)

4. tournament_test_lisa.py
This file contains more testcases, especially to test the extra credits (draw matches, odd number of players and the integration of opponent match wins to the player standings). To run the testcases, make sure that a database tournament exists. The tables and views are created by tournament_test_lisa.py.
To run:
- create a database tournament (createdb tournament)
- run tournament_test_lisa.py (python tournament_test_lisa.py)

5. README.txt
This file.