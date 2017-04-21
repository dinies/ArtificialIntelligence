/**
 * Example of Tic Tac Toe games with different players,
 * including a Reinforcement Learning one.
 * 
 * Luca Iocchi, 2014
 */

import java.awt.BorderLayout;
import java.awt.Canvas;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.Random;
import javax.swing.JFrame;

/**
 * Class with utility functions
 *
 */
class Uti {
	/**
	 * Waits for some time
	 * 
	 * @param ms Time to sleep (ms)
	 */
	public static void sleep(int ms)
	{
		try {
			Thread.sleep(ms);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}


/**
 * Class Move represents a single move 
 * (i,j) are the coordinates of the board (0,0) to (2,2) 
 */
class Move {
	public int i,j;
	Random rand;
	
	public Move() { i=0; j=0; rand=new Random(); }

	public Move(int i, int j) { this.i=i; this.j=j; rand=new Random(); }
	
	public void random() {
		i=rand.nextInt(3); j=rand.nextInt(3);
	}
	
	public String toString() {
		return "("+i+","+j+")";
	}
}


/**
 * Class TicTacToeGame implements a single game 
 * (i,j) are the coordinates of the board (0,0) to (2,2) 
 */
class TicTacToeGame
{
	static final int EMPTY = 0,X_PIECE = 1,O_PIECE = 2;
	int[][] gameGrid = new int[3][3]; // Game grid
	boolean xTurn; // Is it X's turn?

	/**
	 * Starts a new game
	 * 
	 */
	public TicTacToeGame() {
		reset();
	}
	
	/**
	 * Resets the game board
	 * 
	 */
	public void reset() {
		// Wipe grid
		wipeGrid();		
	}
	
	/**
	 * Clears the game board of all pieces.
	 * 
	 */
	private void wipeGrid()
	{
		// Wipes the entire grid
		for(int y = 0;y < 3;y++)
			for(int x = 0;x < 3;x++)
				gameGrid[x][y] = EMPTY;
		// Set starting player
		xTurn = true;
	}
	
	
	/**
	 * Counts the number of valid moves.
	 * 
	 * @return  number of valid moves
	 */
	public int movesAvailable()
	{	
		int c=0;
		for(int y = 0;y < 3;y++)
			for(int x = 0;x < 3;x++)
				if (gameGrid[x][y] == EMPTY) c++;
		return c;
	}
	
	/**
	 * Checks if this move is valid.
	 * 
	 * @return  true if move (i,j) is valid, false otherwise
	 */
	boolean isValid(int i, int j) {
		return (i>=0 && i<3 && j>=0 && j<3 && gameGrid[i][j] == EMPTY);
	}
	
	/**
	 * Checks if this move is valid.
	 * 
	 * @return  true if move m is valid, false otherwise
	 */
	boolean isValid(Move m) {
		return isValid(m.i,m.j);
	}
	
	/**
	 * Executes this move
	 * 
	 * @return  true if move is valid, false otherwise
	 */
	boolean doMove(Move m) {
		return doMove(m.i,m.j);
	}
	
	/**
	 * Executes this move
	 * 
	 * @return  true if move is valid, false otherwise
	 */
	boolean doMove(int i, int j) { 					
		// Check for an empty place
		if(gameGrid[i][j] != EMPTY)
			return false; // Not empty, can't place piece
		gameGrid[i][j] = xTurn?X_PIECE:O_PIECE;
		xTurn = !xTurn;
		return true;
	}

	/**
	 * Checks whether the game is over.
	 * 
	 * @return  0 = Game not over, 1 = X wins, 2 = O wins, 3 = tie
	 */
	int gameOver()
	{
		// Check for a match
		for(int x = 0;x < 3;x++) // Rows
			if(gameGrid[x][0] == gameGrid[x][1] && gameGrid[x][1] == gameGrid[x][2])
				return gameGrid[x][0];
		for(int y = 0;y < 3;y++) // Columns
			if(gameGrid[0][y] == gameGrid[1][y] && gameGrid[1][y] == gameGrid[2][y])
				return gameGrid[0][y];
		// Diagonal 1
		if(gameGrid[0][0] == gameGrid[1][1] && gameGrid[1][1] == gameGrid[2][2])
			return gameGrid[0][0];
		if(gameGrid[2][0] == gameGrid[1][1] && gameGrid[0][2] == gameGrid[1][1])
			return gameGrid[2][0];
		// Check for tie
		for(int y = 0;y < 3;y++)
			for(int x = 0;x < 3;x++)
				if(gameGrid[x][y] == 0)
					return 0; // Not a tie because there is an empty space
		// The game is a tie
		return 3;
	}
}

/**
 * Canvas showing the results of the games
 * 
 */

class Results extends Canvas
{
	private int w,h,last_x,last_v;
	private int value; private double x;
	private Player player;
	
	public Results(Player p) {
		w=510; h=250;
		setPreferredSize(new Dimension(w,h));
		x=5; value=0;
		player=p;
	}
	
	public void refresh() {
		value=(int) (Math.log(player.getScore())*100); x+=0.5;
		this.repaint();
	}
	
	public void paint(Graphics g)
	{
		g.setColor(Color.BLACK);
		g.drawLine((int)x, h/2, w-(int)x, h/2);		
	}
	
	public void update(Graphics g)
	{
		g.setColor(Color.BLACK);
		g.clearRect(0, 0, 400, 40);
		String s = player.name+" - w/t/l: "+player.wins+"/"+player.ties+"/"+player.losts;
		g.drawString(s, 20, 20);
		g.setColor(Color.RED);
		g.drawString("log( win / lost )", 10, 50);
		int v = h/2-value;
		g.drawLine(last_x, last_v, (int)x, v);
		last_x=(int)x; last_v=v; 
	}
	
	
}

/**
 * Canvas for drawing game evolution.
 *
 */
class GameBoard extends Canvas
{
	private TicTacToeGame game;
	Player player1, player2;
	private boolean gameRunning; // Is a game in progress?
	private int gameResult; // Result of game
	private Results results;

	
	/**
	 * Creates a new game board.
	 */
	public GameBoard(TicTacToeGame g, Player p1, Player p2)
	{
		game = g; player1 = p1; player2 = p2;
		// Set the size and background color
		setPreferredSize(new Dimension(256,256));
		setBackground(Color.WHITE);
		
		// Set game status
		gameRunning = true;
	}

	
	/**
	 * Creates a link the results canvas
	 *  
	 * @param r The results canvas
	 */
	public void setResultsLink(Results r) {
		results=r;
	}
	
	/**
	 * Returns the link to the results canvas
	 * 
	 * @return the result canvas
	 */
	public Results getResultsLink() {
		return results;
	}

	/**
	 * Paints the game board.
	 */
	public void paint(Graphics g)
	{	
		g.setColor(Color.BLUE);
		g.drawString(player1.name, 10, 20);
		g.setColor(Color.RED);
		g.drawString(player2.name, 100, 20);
	}
	
	/**
	 * Updates the graphics of the game board
	 */
	public void update(Graphics g)
	{
		// Clear old stuff out
		g.clearRect(0,40,getWidth(),getHeight()-40);
		// Draw lines
		g.setColor(Color.BLACK);
		for(int y = 1;y < 3;y++)
			g.drawLine(50,y*50+50,50+50*3,y*50+50);
		for(int x = 1;x < 3;x++)
			g.drawLine(x*50+50,50,x*50+50,50+50*3);
		// Draw pieces
		for(int y = 0;y < 3;y++)
		{
			for(int x = 0;x < 3;x++)
			{
				if(game.gameGrid[x][y] == TicTacToeGame.X_PIECE)
				{
					g.setColor(Color.BLUE);
					g.drawLine(50+x*50,50+y*50,50+x*50+50,50+y*50+50);
					g.drawLine(50+50+x*50,50+y*50,50+x*50,50+y*50+50);
				}
				if(game.gameGrid[x][y] == TicTacToeGame.O_PIECE)
				{
					g.setColor(Color.RED);
					g.drawOval(50+x*50,50+y*50,50,50);
				}
			}
		}
		// Check for turns
		g.setColor(Color.BLACK);		
	}
	
	/**
	 * Executes one game loop
	 * 
	 * @param ms time sleep (ms) after the game
	 */
	public void oneGameLoop(int ms) {
		Player p = player1;
		Player o = player2;
		game.reset();
		gameRunning = true; boolean firstMove=true;
		gameResult=game.gameOver();
		while (gameResult==0) {
			Move m = p.nextMove();
			while (!game.isValid(m))
				m = p.nextMove();
			game.doMove(m);
			
			
			gameResult=game.gameOver();
			if (gameResult==0) {
				// notify other player
				if (!firstMove)
					o.notifyResult(0);
				// switch player
				Player tmp=p; p=o; o=tmp;
			}
			firstMove=false;
		}
		this.repaint();
		Uti.sleep(ms);
		gameRunning = false;
		// gameResult 0 = Not over, 1 = X wins, 2 = O wins, 3 = tie
		if (gameResult==3) {
			p.notifyResult(1); o.notifyResult(1); results.refresh();
		}
		else {
			p.notifyResult(2); o.notifyResult(-1); results.refresh();
		}
		
		this.repaint();
	}
}


/**
 * GUI Interface showing the evolution of the games.
 *
 */
public class TicTacToe extends JFrame
{
	
	/**
	 * This is the frame where the game is drawn on.
	 * 
	 */
	public TicTacToe(GameBoard gameBoard) {
		this.setLayout(new BorderLayout());
		add(gameBoard,BorderLayout.NORTH);
		add(gameBoard.getResultsLink(),BorderLayout.SOUTH);
		// Pack and show
		setTitle("Tic Tac Toe");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		pack();
		setLocationRelativeTo(null);
		setVisible(true);
	}

	/**
	 * Starts many games of Tic Tac Toe between Random and selected player.
	 * 
	 * @param args [Random|Sequential|RL] (Player type)  
	 */
	public static void main(String[] args)
	{
		// Game
		TicTacToeGame game = new TicTacToeGame();
		// Players
		Player p1 = new RandomPlayer(game);
		Player p2 = new RandomPlayer(game);
		Player p3 = new SequentialPlayer(game);
		Player p4 = new RLPlayer(game);
		// Create the game board and the results window
		Player pl1 = p1; 
		Player pl2 = p4;
		if (args.length>0) {
			if (args[0].equals("RL"))
				pl2=p4;
			else if (args[0].equals("Random"))
				pl2=p2;
			else if (args[0].equals("Sequential"))
				pl2=p3;
		}
		GameBoard gameBoard = new GameBoard(game,pl1,pl2);
		Results results = new Results(gameBoard.player2);
		gameBoard.setResultsLink(results);
		// Create the window for tic tac toe
		TicTacToe ticTacToe = new TicTacToe(gameBoard);

		// Run 1000 games
		for (int k=0; k<1000; k++) {
			// System.out.println("Game "+k);
			gameBoard.oneGameLoop(10);
			Uti.sleep(25);
		}
	}
}
