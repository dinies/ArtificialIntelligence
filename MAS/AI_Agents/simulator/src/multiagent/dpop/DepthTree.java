package multiagent.dpop;
import java.util.*;

import multiagent.Agent;
import multiagent.Task;
import multiagent.World;
import multiagent.dpop.Edge;

/**
 * This class offers all the function that you need to manage a DFTree for the DPOP problem.
 * The nodes in the tree are stored into and array with a fixed order, since dealing
 * with a DFTree the numbering of the nodes represents also the position of the
 * nodes in the array.
 *
 * Node numbering starts from 0 and ends at N-1.
 *
 * For instance, you can use this package to generate a tree as in the last slides of the practical lecture:
 * DCOPTree.addNewEdge(0, 1, false);
 * DCOPTree.addNewEdge(1, 2, false);
 * DCOPTree.addNewEdge(1, 3, false);
 *
 * @author Albani Dario
 *
 */
public class DepthTree {
	private LinkedList<Node> nodes;
	private World world;

	/** list of the nodes of the DFS tree in preorder: first root, last the only leaf (since fully connected graph) */
	private LinkedList<Integer> treeIndexList;

	/**
	 * Constructor
	 *
	 * @param world, the instance of the world
	 * @param numOfNodes, number of nodes for the current tree
	 */
	public DepthTree(World world, int numOfNodes) {
		this.nodes = new LinkedList<Node>();
		this.world = world;
		for(int n = 0; n < numOfNodes; n++){
			this.nodes.add(new Node(n, this.world.getWeedCellSubset().size()));
		}
		HashMap<Integer, ArrayList<Integer>> graph= this.buildConstraintGraph();
		this.buildTree(graph);
	}

	/**
	 * Define a new edge for the tree.
	 *
	 * @param parent. the parent node
	 * @param child. the child node
	 * @param isPseudo, define if the edge represent an edge for a pseudo parent
	 */
	public void addNewEdge(int parent, int child, boolean isPseudo){
		Edge e = new Edge(this.nodes.get(parent), this.nodes.get(child), isPseudo);
		this.nodes.get(parent).addEdge(e);
		this.nodes.get(child).addEdge(e);
	}

	/**
	 * Add the logic to solve you DPOP problem from here
	 */

	 /** add arcs that will link constrained nodes one with another ( in this case all the nodes are constrained with all the others then is called a fully connected graph*/
	 public HashMap<Integer, ArrayList<Integer>> buildConstraintGraph(){
		HashMap<Integer, ArrayList<Integer>>constraintGraph = new HashMap<>() ;

		for(Node a : nodes){
			ArrayList<Integer>neighboors = new ArrayList<>();

			for(Node b : nodes){

				if ( a.getId() != b.getId() ){
					neighboors.add(b.getId());
				}
			}
			constraintGraph.put( a.getId(), neighboors );

		}
		return constraintGraph;
	 }

	 /** build the DFS tree visiting the constraint graph. Most constrained node heuristic has been adopted
	  * @param graph constrain graph
	 since we are dealing with a fully connected graph we can assume that at every iteration all the posiible children are included in the neighboors of the current node. This simplify the implementation of a deep first selection, otherwise recursion would have been necessary.
	  */

	 public void buildTree( Map<Integer  , ArrayList<Integer>>graph){
		int node_num= graph.keySet().size();
		int previous_node_index= -1;
		int current_node_index= -1;


		LinkedList<Integer>nodes_visited = new LinkedList<>();

		  while (nodes_visited.size() < node_num){
				current_node_index= nextNode(graph, nodes_visited);

				if (previous_node_index != -1){
					addNewEdge(current_node_index, previous_node_index, false);

					for ( int i : graph.get(current_node_index)){
						if (nodes_visited.contains(i)){
							addNewEdge(i, current_node_index, true);
						}
					}
				}
				nodes_visited.add(current_node_index);
				previous_node_index=current_node_index;
				}


		this.treeIndexList= nodes_visited;
	 }



	 /** choose the next node to be visited accordingly to the most constrained node heuristic
	  * @param graph constrain graph
	  * @param visited list of indexs of visited nodes
	  * @return index of the note that has to be visited
	  */
	  protected int nextNode( Map<Integer, ArrayList<Integer>>graph, LinkedList<Integer> visited){
		Map<Integer, List<Integer>>unvisited = new HashMap<>();
		for (int k : graph.keySet()){
			if ( ! visited.contains(k)){
				unvisited.put( k, graph.get(k));
			}
		}
		// choose the first unvisited node as starting point
		Iterator<Integer> iter = unvisited.keySet().iterator();

		int most_constrained_node= iter.next();

		  for ( int key : unvisited.keySet()){
			if ( unvisited.get(key).size() > graph.get(most_constrained_node).size()){
				most_constrained_node= key;
			}
		  }
		return most_constrained_node;
	}

/** it will manage to propagate the values of the constraint optimization
 *  problem with bottom-up approach at first and then it will make the
 *  most promising decision top-down in the DFStree
 * @param valueStruct data structure with node_ids as keys and lists
 *  of DCOP values as values of the dictionary
 * @return a map with node index as key and relative task assigned index as value
 */
	public HashMap<Integer,Integer> executeDCOP(HashMap<Integer, LinkedList<Integer>> valueStruct){

		for( Node n : nodes){
			n.fillValueRelation(valueStruct.get(n.getId()));
		}
		//bottom-up
		// if ( !treeIndexList.getFirst().isRoot()){
		// 	System.out.println("Root node is not recognised");
		// }
		// if ( !treeIndexList.getLast().isLeaf()){
		// 	System.out.println("Leaf node is not recognised");
		// }
		Iterator<Integer> iter_bottom_up= treeIndexList.descendingIterator();

		while (iter_bottom_up.hasNext()){
			Node n = nodes.get(iter_bottom_up.next());
			n.harvestValues();
		}


		//top-down
		Iterator<Integer> iter_top_down = treeIndexList.iterator();
		HashMap<Integer,Integer> task_assigment= new HashMap<>();
		HashSet<Integer> already_assigned= new HashSet<>();
		while ( iter_top_down.hasNext()){
			Node n = nodes.get(iter_top_down.next());
			int node_id= n.getId();
			int task_index= n.chooseMaxUtilityTask( already_assigned);
			task_assigment.put(node_id, task_index);
			already_assigned.add(task_index);

		}
		if ( already_assigned.size() != treeIndexList.size()){
			System.out.println("there is some problem with task assigment");
		}
		return task_assigment;
	}
}
