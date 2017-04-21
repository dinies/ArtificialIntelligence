/**
 * Implementation of Tic Tac Toe players.
 * 
 * Luca Iocchi, 2014
 */

import java.util.Random;
import java.util.Map;
import java.util.HashMap;

/**
 * Class for Tic Tac Toe abstract player
 * 
 *
 */
abstract class Player {
	
	TicTacToeGame game;
	String name;
	Random rnd;
	int wins,ties,losts;
	
	/**
	 * Starts a player for the game g
	 * 
	 * @param g The current gameto be played by this player
	 */
	public Player (TicTacToeGame g) {
		game=g;
		name="Unknown";
		rnd = new Random();
	}
	
	/**
	 * Returns the next move.
	 * 
	 * @return Next move to be executed.
	 */
	abstract public Move nextMove();
	
	/**
	 * Result of last move notified
	 * 
	 * @param result = 0 (game not finished), 2 (win), 1 (tie), -1 (lost)
	 */
	public void notifyResult(int result) 
	{	
		if (result==2) { // win
			wins++;
		}
		else if (result==1) { // tie
			ties++;
		}
		else if (result==-1) { // lost
			losts++;
		}		
	}
	
	/**
	 * A global score for his player
	 * 
	 * @return Global score for this player
	 */
	public double getScore() {
		return (double)wins/losts;
	}

	/**
	 * Total number of games played by this player
	 * 
	 * @return Total number of games played by this player
	 */
	public int totalGames() {
		return wins+ties+losts;
	}
	
	/**
	 * Returns a player status
	 * 
	 * @return Player status
	 */
	public String getStatus() {
		return "";
	}

}


class RandomPlayer extends Player {

	public RandomPlayer(TicTacToeGame g) {
		super(g);
		name="Random";
	}
	
	public Move nextMove() {
		Move m = new Move();
		m.random();
		while (!game.isValid(m)) {
			m.random();
		}
		return m; 
	}
}


class SequentialPlayer extends Player {

	public SequentialPlayer(TicTacToeGame g) {
		super(g);
		name="Sequential";
	}
	
	public Move nextMove() {
		Move m = new Move();
		for (m.i=0; m.i<3; m.i++) {
			for (m.j=0; m.j<3; m.j++) {
				if (game.isValid(m))
					return m;
			}
		}
		return m;
	}
}

class RLPlayer extends Player {

	double gamma;
	Q q;
	int lastState, lastMove;
	double eps;
	boolean exploit;
	
	
	class Q {
		Map<Integer,Double> v;
		
		public Q() {
			v = new HashMap<Integer,Double>();
		}

		public double get(Move m) {
			int e = encodeGameStatus();
			int a = encodeMove(m);
			int k = a + e*9;
			//System.out.println(k);
			Double x = v.get(k);
			if (x==null)
				return 0;
			else
				return x;
		}
		
		public double get(int s, int a) {
			int k = a + s*9;
			//System.out.println(k);
			Double x = v.get(k);
			if (x==null)
				return 0;
			else
				return x;
		}
		
		public void set(int state, int move, double value) {
			int k = move + state*9;
			v.put(k,value);
		}
		
	} // Q
	
	public RLPlayer(TicTacToeGame g) {
		super(g);
		name="RL";
		gamma=0.9; eps=0.1;
		q = new Q();
		wins=0; losts=0;
	}
	
	private int encodeGameStatus()
	{
		int r=0; int k=1;
		for (int i=0; i<3; i++) {
			for (int j=0; j<3; j++) {
				// System.out.println("     "+game.gameGrid[i][j]+" * "+k);
				r = r + game.gameGrid[i][j] * k;
				k *= 4;
			}
		}
		return r;
	}
	
	private int encodeMove(Move m)
	{
		return m.i+3*m.j;
	}

	public Move nextMove() {
		if (exploit) {
			//Uti.sleep(5000);
		}
		Move m = chooseMove();
		if (exploit) {
			//System.out.println("EXPLOIT "+m+" "+q.get(m));
			//Uti.sleep(3000);
		}
		lastState = encodeGameStatus();
		lastMove = encodeMove(m);
		return m;
	}
	
	private Move chooseMove() {
		Move m = new Move();
		
		if (rnd.nextDouble()<eps) {
			// exploit
			exploit = true;
			double maxq=Double.NEGATIVE_INFINITY;
			Move best = new Move();
			for (int i=0; i<3; i++) {
				for (int j=0; j<3; j++) {
					if (game.isValid(i,j)) {
						double qm = q.get(new Move(i,j));
						if (qm>maxq) {
							maxq=qm;
							best.i=i; best.j=j;
						}	
					}
				}
			}
			m = best;			
		}
		else {
			// explore
			exploit = false;
			m.random();
			while (!game.isValid(m)) {
				m.random();
			}
		}
		
		//System.out.println(" a = "+m);
		//System.out.println(" Q = "+q.get(m));
		return m;
	}
	

	
	public void notifyResult(int result) 
	{
		super.notifyResult(result);
		double r=0;
		if (result==2) {
			r=100;
			eps=Math.min(1.0, eps+0.005);
		}
		else if (result==1) {
			r=10;
		}
		else if (result==-1) {
			q.set(lastState, lastMove, -1);
			r=-100;
		}		
		
		if (result!=0)
			exploit=false;
		
		//System.out.println("Setting reward...");
		int s1=encodeGameStatus();
		int nm = game.movesAvailable();
		int a1=0;
		if (nm>0)
			a1=encodeMove(chooseMove());

		// SARSA
		double alpha=0.2;
		double q0 = q.get(lastState,lastMove);
		double q1 = q.get(s1,a1);
		double val = q0 + alpha * (r+gamma*q1-q0);
		q.set(lastState,lastMove,val);
		//System.out.println("...  done!");
		
	}
	
	public String getStatus() {
		return "RL player win/lost = "+wins+"/"+losts;
	}
}
