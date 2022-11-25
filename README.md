# Scrabb-e-Player-Rating
## Dataset Description
The dataset includes information about ~73,000 Scrabble games played by three bots on Woogles.io: BetterBot (beginner), STEEBot (intermediate), and HastyBot (advanced). The games are between the bots and their opponents who are regular registered users. You are using metadata about the games as well as turns in each game (i.e., players' racks and where and what they played, AKA gameplay) to predict the rating of the human opponents in the test set (test.csv). You will train your model on gameplay data from one set of human opponents to make predictions about a different set of human opponents in the test set.

There is metadata for each game (games.csv), gameplay data about turns played by each player in each game (turns.csv), and final scores and ratings from BEFORE a given game was played for each player in each game (train.csv and test.csv).

Here is an example of a game played on woogles.io: https://woogles.io/game/icNJtmxy. Use the "Examine" button to replay the game turn-by-turn.
 
## Files
> + **games.csv** - metadata about games (e.g., who went first, time controls)<br>
> + **turns.csv** - all turns from start to finish of each game<br>
> + **train.csv** - final scores and ratings for each player in each game; ratings for each player are as of BEFORE the game was played<br>
> + **test.csv** - final scores and ratings for each player in each game; ratings for each player are as of BEFORE the game was played<br>
> + **sample_submission.csv** - a sample submission file in the correct format<br>
### turns.csv - contains full data for every turn for each game
+ game_id Unique id for the game<br>
+ turn_number The turn number in the game<br>
+ nickname Player's username on woogles.io<br>
+ rack Player's current rack<br>
+ location Where the player places their turn on the board (NA for games in the test set or if the player didn't make a play, e.g., if they exchanged)<br>
+ move Tiles the player laid (NA for games in the test set; "--" if the turn_type was "Pass"; "(challenge)" if the turn_type was "Challenge"; "-" plus tiles exchanged if the turn_type was "Exchange"; at the end of the game, remaining tiles in a player's rack are in parentheses)<br>
+ points Points the player earned (or lost) in their turn<br>
+ score Player's total score at the time of the turn<br>
+ turn_type Type of turn played ("Play", "Exchange", "Pass", "Six-Zero Rule" (i.e., a game that ends when players pass 3 turns in a row each), "Challenge")<br>


### games.csv
+ game_id Unique id for the game<br>
+ first Which player went first<br>
+ time_control_name Name of time control used ("regular", "rapid", or "blitz")<br>
+ game_end_reason How the game ended<br>
+ winner Who won the game<br>
+ created_at When the game was created
lexicon English lexicon used in the game ("CSW19", "NWL20", "CSW21")<br>
+ initial_time_seconds Time limit each player has in the game (defines the time control name)<br>
+ increment_seconds Time increment each player gets each time they play a turn<br>
+ rating_mode Whether the game counts towards player ratings or not ("RATED", "CASUAL")<br>
+ max_overtime_minutes How far past the initial time limit players can go before they timeout<br>
+ game_duration_seconds How long the game lasted<br>


### test.csv and train.csv
There's score and rating data about 1031 players in train.csv and 443 players in test.csv. Except for the three bots, no players are in both train.csv and test.csv. Ratings for the players are from BEFORE the game was played. Your task is to predict what the rating of the human player was in test.csv BEFORE the given game was played.

+ game_id Unique id for the game<br>
+ nickname Player's username on woogles.io<br>
+ score Final score for each player for each game.<br>
+ rating Player's rating on woogles.io BEFORE the game was played; ratings are per Lexicon / time control name (AKA game variant). In test.csv, ratings are NA for player games; this is what you are predicting.<br>
