	package multiagent;

	import java.io.*;
	import java.util.*;
	import multiagent.dpop.DepthTree;

	/**
	 * This class implements a full simulator.
	 *
	 * @version 1.1
	 * @author Albani Dario
	 *
	 * @version 1.0 - May 22, 2013
	 * @author Federico Patota
	 * @author Gabriele Buondonno
	 */

	public class AgentSim implements Serializable{
		private static final long serialVersionUID = 1L;

		/**The agents*/
		public List<Agent> agents;
		/**The world*/
		public World world;
		/**The agent currently executing an action (used for simulation purposes)*/
		private int currentAgent;

		/**DCOP logic */
		private DepthTree depthTree;

		/**
		 * Counter used to check if the exploration process has ended.
		 */
		private int inactiveSteps = 0;

		/**Number of a Actions performed (used for statistics).*/
		private int totalNoOps;
		private int totalMoveToLocation;
		private int totalNextTask;

		/**
		 * Constructs a simulator creating a new world with the specified characteristics.
		 * @param height the height of the world
		 * @param width the width of the world
		 */
		public AgentSim(int height, int width){
			world=new World(height,width);
		}

		/**
		 * Constructs a simulator creating a new world with the specified characteristics.
		 * @param height the height of the world
		 * @param width the width of the world
		 * @param weed the number of inaccessible cells
		 * @param ags the number of agents
		 */
		public AgentSim(int height, int width, int weed, int ags){
			world = new World(height,width);
			addWeedCells(weed);
			initTasks();
			initAgentsRandom(ags);
			executionDCOPlogic();

		}

		/** it implements the whole logic of an execution of a DCOP algorithm
		*/
		public void executionDCOPlogic(){

			//DCOP LOGIC HAVE TO BE IMLEMENTED HERE
			// choose 4 random cells with weed to be assigned and store them in wolrd.class as a list
			int n_agents= agents.size();
			world.chooseCellSubset(n_agents);
			// instantiate Depthtree.class --> 4 nodes created [0,1,2,3] and build DFS tree
			depthTree= new DepthTree( this.world, n_agents );
			//DCOP execution (at the end all the tasks that belong to the subset will be assigned)

			HashMap<Integer, LinkedList<Integer>> struct = this.computePathValues();

			System.out.println("Path values :    "  + struct.toString());

			HashMap<Integer, Integer> task_assigment= depthTree.executeDCOP( struct);
			System.out.println( "Task assigment :  "+ task_assigment);

			for( Agent a : agents){
				a.assignTasks(task_assigment);
			}

			//check
			ArrayList<Cell> task_cells = world.getWeedCellSubset();
			for (int i=0; i < agents.size(); i++){
				Cell agent_pos = this.agents.get(i).getPosition();
				int task_assigned_id= task_assigment.get(i);
				Cell agent_assigment= task_cells.get(task_assigned_id);
				int row_task_assigned= agent_assigment.getRow();
				int col_task_assigned= agent_assigment.getCol();
				System.out.print(" Agent n."+ (i+1)+ " in position "+ agent_pos.getRow() + " , "+ agent_pos.getCol() +" has assigned task in position "+row_task_assigned+" , "+ col_task_assigned+ " ;\n");
			}
		}

		/**
		 * Adds weeds in cells.
		 * @param weed the number of weed cells that we want to add
		 */
		public void addWeedCells(int weed){
			world.addWeedCells(weed);
		}

		/**Positions agents in the world in random positions.*/
		public void initAgentsRandom(int numAgents){
			agents=new LinkedList<Agent>();
			for(int i=1;i<=numAgents;i++){
				boolean  valid_flag = false;
				Cell cell = null;
				while (!valid_flag){
					cell = world.getCell((int)(world.getHeight()*Math.random()), (int)(world.getWidth()*Math.random()));
					valid_flag= !cell.isWeed();
				}
				Agent a = new Agent(i,cell, this.world);
				agents.add(a);

				cell.setVisited(true);
				if(cell.isWeed()){
					cell.setSprayed(true);
				}

				if(cell.getTask() != null)
					cell.getTask().markAsComplete(cell.getAgent());
			}
			world.addAgents(agents);
		}

		/**
		 * Task initialization.
		 *
		 * TODO update the task list according to your problem.
		 * Check the setUpForCoverage and setUpForWeed methods in class World
		 */
		public int initTasks(){
	//		this.world.setUpForCoverage();
			this.world.setUpForWeed();
			System.out.print("setting up for weed removal\n");
			return 0;
		}

		/**
		 * Executes one step for one agent and switches agent.
		 * The one step execution change with respect to the exercise.
		 * @return true if there have been two full rounds without any action taken,
		 * indicating that the system will have no further evolution.
		 */
		public boolean doOneStep() {
			// try {
			// 	Thread.sleep(500);
			// } catch (InterruptedException e) {
			// 	// TODO Auto-generated catch block
			// 	e.printStackTrace();
			// }

			System.out.println("STEp");

			//retrieve the action from the current agent
			Agent agent = agents.get(currentAgent);
			Action act = agent.nextAction();

			//managing statistics and inactive steps count
			if(act == Action.noOp){
				inactiveSteps++;
				totalNoOps++;
			}
			else{
				inactiveSteps=0;
				if(act==Action.moveToLocation)
					this.totalMoveToLocation++;
			    else
			    	this.totalNextTask++;
			}

			//executing the action for the agent and return the new task that has to be executed
			//e.g. move to a task already executed and return the new task computed according to the wanted action

			Task previous_task= agent.getCurrentTask();
			Task nextTask = world.executeAction(agent.getId(),agent.getCurrentTask(),act);			

			//updates the state of the agents with the new agent position and the next task to be performed
	        agent.updateState(world.getAgentPosition(agent.getId()),nextTask);

					//check
					Action next_act= agent.nextAction();
					String prev_task;
					if (previous_task==null){
						prev_task= " NONe ";
				}
					else{
						prev_task= previous_task.getStatus().toString();
					}
					String next__Task;

					if (nextTask==null){
						next__Task= " NONe ";
				}
					else{
						next__Task= nextTask.getStatus().toString();
					}


					System.out.print("Current agent: "+ (currentAgent+1)+" previous_task:"+ prev_task +" , ");
					System.out.print("nextTask: "+next__Task+" next action : "+ next_act.toString()+" .." );
					System.out.print("currentPosition: "+ world.getAgentPosition(agent.getId()).getRow() +" , "+world.getAgentPosition(agent.getId()).getCol());
	        //assing and validate the next task
	//        agent.assignTasks(agents);

	        currentAgent=(currentAgent+1)%agents.size();

	        if(inactiveSteps>=2*agents.size()  || this.world.getUncompletedTask().isEmpty())
	            return true;
	        else{
	        	  if (this.world.checkSprayedInSubSet()){
	        		System.out.println("\nDCOP EXEC");
	        		executionDCOPlogic();
	        	}
	        }
	            return false;


		}


		/** compute the value of each task (reaching the cell) wtr to each agent
		 * @return a map in  wich each node has an associated list that contains all the costs
		 */
		public HashMap<Integer, LinkedList<Integer>> computePathValues(){

			HashMap<Integer, LinkedList<Integer>> struct = new HashMap<>();
			for( Agent a : agents){
				LinkedList<Integer> values= a.getTaskValues();
				if (!values.isEmpty()){
				 // since the nodes are [0,1,2,3,4...] and the agent ids are [1,2,3,4,5...]
					Integer node_number= a.getId() -1 ;
					struct.put( node_number, values);
				}

			}
			return struct;
	}

		//************************************************ Methods to retrieve information about the world and about the simulation ******

		/**
		 * Returns the number of cells with the given status.
		 * Visited.
		 * @return the number of cells with the given status.
		 */
		public int countVisitedCells(){
			int count=0;
			for(int row=this.world.getHeight()-1;row>=0;row--)
				for(int col=this.world.getWidth()-1;col>=0;col--)
					if(this.world.getCell(row,col).isVisited())
						count++;
			return count;
		}

		/**
		 * Returns the number of cells with the given status.
		 * Weed.
		 * @return the number of cells with the given status.
		 */
		public int countWeedCells(){
			int count=0;
			for(int row=world.getHeight()-1;row>=0;row--)
				for(int col=world.getWidth()-1;col>=0;col--)
					if(world.getCell(row,col).isWeed())
						count++;
			return count;
		}

		/**
		 * Returns the number of cells with the given status.
		 * Sprayed.
		 * @return the number of cells with the given status.
		 */
		public int countUnsprayedCells(){
			int count=0;
			for(int row=world.getHeight()-1;row>=0;row--)
				for(int col=world.getWidth()-1;col>=0;col--)
					if(world.getCell(row,col).isSprayed())
						count++;
			return count;
		}

		/**
		 * Returns the total number of cells.
		 * @return the total number of cells.
		 */
		public int getTotalCells(){
			return world.getWidth()*world.getHeight();
		}

		/**
		 * Returns the number of times the given Action has been called. If the simulation
		 * is over and act==Action.noOp, noOp is subtracted the last series of noOps.
		 * @param act the action to examine.
		 * @return the number of times the given Action has been called.
		 */
		public int getCalls(Action act){
			if(act==Action.noOp){
				return (inactiveSteps<2*agents.size() ? totalNoOps: totalNoOps-inactiveSteps);
			}
			if(act==Action.moveToLocation){
				return this.totalMoveToLocation;
			}
			if(act==Action.publishNextTask){
				return this.totalNextTask;
			}
			return -1;
		}

		/**
		 * Returns the total number of steps performed. The number of total steps is
		 * equal to getCalls(Action.noOp) + getCalls(Action.nextMoveToTarget) + getCalls(Action.totalNextStepInTask).
		 * @return the number of total steps performed.
		 */
		public int getTotalSteps(){
			return getCalls(Action.noOp)+this.totalMoveToLocation+this.totalNextTask;
		}

		/**
		 * Returns the total number of complete rounds the simulation has performed.
		 * By performing a round, we mean doing one step for each agent.
		 * The result is rounded by defect.
		 * @return the number of total loops performed.
		 */
		public int getTotalRounds(){
			return getTotalSteps()/agents.size();
		}

		/**
		 * Returns the number of cells visited by the given agent.
		 * @param agId the id of the agent
		 */
		public int getVisited(int agId){
			int count=0;
			for(int row=world.getHeight()-1;row>=0;row--)
				for(int col=world.getWidth()-1;col>=0;col--)
					if(world.getCell(row,col).isVisited() && world.getCell(row,col).getAgent() == agId)
						count++;
			return count;
		}

		/**
		 * Convenience method returning a String representation for all the statisics.
		 * @return a String representation for the statisics.
		 */
		public String statsToString(){
			StringBuilder builder=new StringBuilder();

			builder.append("Total cells: "+ getTotalCells()+"\n");
			for(int i = 0; i < this.world.getHeight(); i++){
				for(int j = 0; j < this.world.getWidth(); j++){
					if (this.world.getCell(i, j).getTask() != null){
						builder.append(i + " " + j + " ");
						builder.append(this.world.getCell(i, j).getTask().getStatus());
						builder.append("\n");
					}
				}
			}
			//TODO fill with your information
			//this is the string contained in the pop up that appears at the end of the execution

			return builder.toString();
		}
	}
