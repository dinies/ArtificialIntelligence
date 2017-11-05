Python modelling of a chess endgame situation played on a reduced board.

Running Instructions

the dependencies are only a MySql server Database instelled on the machine

after the installation of MySql two databases should be created togheter with two users accordingly to the names in Database.txt

then each user has to be given the rights to use its database.


After that, tests can be executed with the following command in  project_dir/RLproject/tests

$  python  -m unittest discover -p  '*Test.py"

then the main code can be executed in project_dir/RLproject/src through

$  python  ChessPanel.py

