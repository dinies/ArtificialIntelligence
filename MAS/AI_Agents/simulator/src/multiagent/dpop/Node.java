package multiagent.dpop;

import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import multiagent.dpop.Relation;

/**
 * This class represent a node in the tree.
 * Such node is structured to let you use it for the DPOP solution.
 *
 * @author Albani Dario
 *
 */

class Node {
	private int id;
	// the number of variables to be managed by the node during the DPOP execution
	// e.g following the example on the practical slide this could be [a,b,c], then 3.
	private int numOfVariables;
	private LinkedList<Edge> edges;
	private LinkedList<Relation> relations;

	/** result of the value bottom-up propagation */
	private LinkedList<Integer> joined_value_from_children;

	/**
	 * Constructor for the node (an agent)
	 *
	 * @param id, a unique id assigned to the node. Must be the same as the agentID
	 * @param numOfVariables, the number of variables to be managed by the agent (i.e. Tasks)
	 */
	public Node(int id, int numOfVariables){
		this.id = id;
		this.setNumOfVariables(numOfVariables);
		this.relations = new LinkedList<Relation>();
		this.edges = new LinkedList<Edge>();
		 LinkedList<Integer> zeroes= new LinkedList<>();
		for(int j = 0; j < numOfVariables; j++){
			zeroes.add(0);
		}
		this.joined_value_from_children= zeroes;

	}

	/**
	 * Get current node id
	 * @return int id
	 */
	protected int getId() {
		return id;
	}

	/**
	 * Get current node relations tables as in the DPOP structure
	 *
	 * @return list of relations
	 */
	protected LinkedList<Relation> getRelations() {
		return relations;
	}

	/**
	 * Get the relation table associated with the node in input
	 *
	 * @return relation from this to node or vice versa
	 */
	protected Relation getRelation(Node n) {
		for (Relation r : this.relations){
			if(r.getChild() == n || r.getParent() == n){
				return r;
			}
		}
		return null;
	}

	/**
	 * Add or update a relation to the list of relations of the current node.
	 * Use this method to update the relations between the nodes or to add a new one
	 *
	 * @param relation
	 */
	protected void addRelation(Relation relation) {
		for(Relation r : this.relations){
			if(r.equals(relation)){
				this.relations.remove(r);
				break;
			}
		}
		this.relations.add(relation);
	}

	protected LinkedList<Edge> getEdges() {
		return edges;
	}

	protected void setEdges(LinkedList<Edge> edges) {
		this.edges = edges;
	}

	protected void addEdge(Edge e) {
		if(this.edges.contains(e)){
			return;
		}

		this.edges.add(e);
		Relation rel =  new Relation(e.getNode1(), e.getNode2(),numOfVariables);
		this.relations.add(rel);
	}

	/**
	 *
	 * @return true if this is the root
	 */
	protected boolean isRoot(){
		return this.getParents().isEmpty();
	}

	/**
	 *
	 * @return true if this is a leaf
	 */
	protected boolean isLeaf(){
		return this.getChildren().isEmpty();
	}

	/**
	 * Retrieve all the parents node of this
	 *
	 * NOTE if the list is empty, this is the root
	 * @return a list of parents
	 */
	protected LinkedList<Node> getParents(){
		LinkedList<Node> parents = new LinkedList<Node>();
		for (Edge e : this.edges){
			if(e.getNode2() == this){
				parents.add(e.getNode1());
			}
		}

		return parents;
	}

	/**
	 * Retrieve all the children node of this
	 *
	 * NOTE if the list is empty, this is a leaf
	 * @return a list of children
	 */
	protected LinkedList<Node> getChildren(){
		LinkedList<Node> children = new LinkedList<Node>();
		for (Edge e : this.edges){
			if(e.getNode1() == this){
				children.add(e.getNode2());
			}
		}

		return children;
	}

	/** update the values in each relation with the values in the struct
	* @param valueVec lists of DCOP values
  	*/
  	public 	void  fillValueRelation( LinkedList<Integer> valueVec){

		Iterator<Relation> iter= this.getRelations().iterator();
		while ( iter.hasNext()){
			Relation rel= iter.next();
			if (this.isChildInRelation(rel)){
				rel.updateChildValues(valueVec);
			}
			else{
				rel.updateParentValues(valueVec);
			}
		}
	}

	/** check if the node is a child or a parent in the relation
	 * @param rel relation to check
	 * @return true if it is the child in the relation
	*/
	protected boolean isChildInRelation( Relation rel){
		return rel.getChild().equals(this);
	}

	/**
	 * @return the numOfVariables
	 */
	protected int getNumOfVariables() {
		return numOfVariables;
	}

	/** the node will check if it isn't a leaf node and then it will
	 *  pick up each value message from its children and compute
	 *  the joint values to propagate
	 * */
	public void harvestValues(){
		if (!isLeaf()){
			LinkedList<Relation> is_parent_relations= new LinkedList<>();
			LinkedList<Relation> is_child_relations= new LinkedList<>();
			for (Relation rel : this.getRelations()){
				if (this.isChildInRelation(rel)){
					is_child_relations.add(rel);
				}
				else{
					is_parent_relations.add(rel);
				}
			}
			this.joined_value_from_children= this.joinValuesRec(is_parent_relations);
			if (!isRoot()){
				for(Relation parent : is_child_relations){
					parent.jointMaxSumUtilMessages(joined_value_from_children);
				}
			}
	}

	}

	/** recursive method which compute the jointsum between the given list of relations
 	* @param relations List of the relation in which this node is the parent
	 */
	protected LinkedList<Integer> joinValuesRec( LinkedList<Relation> relations){
		if (relations.isEmpty()){
			 LinkedList<Integer> zeroes = new LinkedList<>();
			 for(int j = 0; j < numOfVariables; j++){
				zeroes.add(0);
			 }
			 return zeroes;
		}
		Relation rel = relations.pop();
		return rel.jointSumUtilMessages(this.joinValuesRec(relations));

	}


	/** choose a task among the unassigned ones that maximizes utility
	 * @param already_assigned  set of tasks that are already assigned to a node
	 * @return the index of the chosen task
	*/
	public int chooseMaxUtilityTask( HashSet<Integer> already_assigned){
		int max = -1;
		int max_index = -1;
		for (int i =0 ; i< this.joined_value_from_children.size();i++){
		 	if ( this.joined_value_from_children.get(i) > max && !already_assigned.contains(i)) {
				max= this.joined_value_from_children.get(i);
				max_index= i;
		 	}
		}
		return max_index;
	}


	/**
	 * @param numOfVariables the numOfVariables to set
	 */
	protected void setNumOfVariables(int numOfVariables) {
		this.numOfVariables = numOfVariables;
	}

	@Override
	public boolean equals(Object o){
		Node e = (Node)o;
		return this.id == e.getId();
	}

}
