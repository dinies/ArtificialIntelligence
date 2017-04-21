#!/bin/bash
java -cp bin TicTacToe Random &
java -cp bin TicTacToe Sequential &
java -cp bin TicTacToe RL &

