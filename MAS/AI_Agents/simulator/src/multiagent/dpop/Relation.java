package multiagent.dpop;

import java.awt.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;

//import com.sun.org.apache.xml.internal.utils.res.IntArrayWrapper;

/**
 * Class used to simulate a relation table as for the DPOP problem.
 * Use this to store and propagate utility values bottom up in the tree.
 * 
 * @author Albani Dario
 *
 */
class Relation {
	private Node child;
	private Node parent;

	private LinkedList<LinkedList<Integer>> utilValues;
	private LinkedList<Integer> utilMessage;

	public boolean updated = false;

	public Relation(Node child, Node parent, int numOfVariables){
		this.child = child;
		this.parent = parent;
		this.utilMessage = new LinkedList<>();
		this.utilValues = new LinkedList<>();
		for(int i = 0; i < numOfVariables; i++){
			LinkedList<Integer> zeros = new LinkedList<Integer>();
			for(int j = 0; j < numOfVariables; j++){
				zeros.add(0);
			}
			this.utilValues.add(zeros);
		}
	}

	protected Node getChild() {
		return child;
	}

	protected void setChild(Node child) {
		this.child = child;
	}

	protected Node getParent() {
		return parent;
	}

	protected void setParent(Node parent) {
		this.parent = parent;
	}

	protected LinkedList<LinkedList<Integer>> getUtilValues() {
		return utilValues;
	}

	protected void setUtilValues(LinkedList<LinkedList<Integer>> utilValues) {
		this.utilValues = utilValues;
		this.updateUtilMessage();
	}

	/**
	 * Update the value at position row, col with the new given value
	 * 
	 * @param row, the variable related to the children node
	 * @param col, the variable related to the parent node
	 * @param newValue, the new value to update
	 */
	protected void updateValue(int row, int col, int newValue){
		this.utilValues.get(row).add(col, newValue);
		this.utilValues.get(row).remove(col+1);
		this.updateUtilMessage();
	}

	/**
	 * Update the utility message with the new values in input.
	 * This method is call every time an update occur in the utility table of 
	 * the relation.
	 * 
	 */
	private void updateUtilMessage(){
		this.utilMessage.clear();

		for(LinkedList<Integer> column : this.utilValues){
			this.utilMessage.add(Collections.max(column));
		}
	}


	/** update the value table in case that the node is the PARENT in the relation
	 * so all the COLUMNS one by one will be summed with the elems of the vector passed as param
	 * NOTE: the elements on the diagonal won't be considered 
	 * since they represent hard constraints between nodes
	 * example: vec= [3,2,1]
	 * | +0  +2   +1|
	 * | +3  +0	  +1|
	 * | +3	 +2   +0|
	 * @param vec list of all the values for every task variable 
	 */
	public void updateParentValues( LinkedList<Integer> vec){
		//each elem of vec will be added to the entire current column : 1st ele --> added to all the first row ( NO on the diagonal position)
		Iterator<Integer> iter= vec.iterator();
		int current_column= 0;
		while (iter.hasNext()){

			int vec_value= iter.next();
				
			for (int i=0 ; i < vec.size(); i++ ){
				if (i != current_column){
					int old_value= this.utilValues.get(i).get(current_column);
					
					this.utilValues.get(i).add(current_column, vec_value + old_value);
					this.utilValues.get(i).remove(current_column+1);
				}
			}
			current_column ++;
		}
		this.updateUtilMessage();
		
	}


	/** update the value table in case that the node is the CHILD in the relation
	 * so all the ROWS  one by one will be summed with the eelems of the  vector passed as param
	 * NOTE: the elements on the diagonal won't be considered 
	 * example: vec= [3,2,1]
	 * | +0  +3   +3|
	 * | +2  +0	  +2|
	 * | +1	 +1   +0|
	 * since they represent hard constraints between nodes
	 * @param vec list of all the values for every task variable 
	 */
	public void updateChildValues(LinkedList<Integer> vec){
		//each elem of vec will be added to the entire current row : 1st ele --> added to all the first row ( NO on the diagonal position)
		Iterator<Integer> iter= vec.iterator();
		int current_row= 0;
		while (iter.hasNext()){
		
			int vec_value= iter.next();
						
			for (int i=0 ; i < vec.size(); i++ ){
				if (i != current_row){
							int old_value= this.utilValues.get(current_row).get(i);
							
							this.utilValues.get(current_row).add(i, vec_value + old_value);
							this.utilValues.get(current_row).remove(i+1);
				}
			}
			current_row ++;
		}
		this.updateUtilMessage();
				
	}


	public LinkedList<Integer> getUtilMessage(){
		return this.utilMessage;
	}

	public void setUtilMessage( LinkedList<Integer> list){
		this.utilMessage= list;

	}

	/**
	 * Implements the join between two different utility messages.
	 * this and util must be of the same length.
	 * @param msg
	 * @return a single utility message that is the element wise sum of the two in input
	 */
	public LinkedList<Integer> jointSumUtilMessages(LinkedList<Integer> msg){
		LinkedList<Integer> elementWise_sum = new LinkedList<>();
		LinkedList<Integer> value_msg= this.getUtilMessage();
		for (int i =0 ; i < value_msg.size() ; i++){
			Integer sum= msg.get(i) + value_msg.get(i);
			elementWise_sum.add(i, sum);
		}
		return elementWise_sum;
	}


	/** it will compute the joint max value considering all the combinations of variables 
	 * it will use the value, in each column of the value table,
	 * which will give the maximum number after that is being added to
	 *  the corresponding value  ( according to the index in the column ) 
	 * in the utility message vector given as param
	 * fianlly it will overwrite the utility message
	 * @param childrenJointValue List of values for each variable
	 *   value_table = [ 0 2 3			childrenJointValue= [ 2 5 6 ]
	 *					 5 0 1
	 *					 9 1 0 ]
	 *
	 * 	joint_max_utility_table = [ 0+2 2+2 3+2 		[  2  4  5
	 *								5+5 0+5 1+5		==>   10  5  6
	 *								9+6 1+6 0+6]		  15  7  6 ]
	 *
	 *	final_util_message= [ 15  7  6 ]								
	 */
	public void jointMaxSumUtilMessages(  LinkedList<Integer> childrenJointValue){
		LinkedList<Integer> new_utility_message= new LinkedList<>();
		int j=0;
		for(LinkedList<Integer> column : this.utilValues){

			ArrayList<Integer> sum = new ArrayList<>();
			for (int i=0; i< column.size(); i++){
				sum.add(i, (column.get(i) + childrenJointValue.get(i)));
			}

			new_utility_message.add(j, Collections.max(sum));
			j++;

		}
		this.setUtilMessage( new_utility_message);
	}

	/**
	 * Implements the projection of an utility message into the utility table 
	 * of this relation as defined in the DPOP framework.
	 * 
	 * @param util, must have the same number of column as the current util table
	 * 
	 * @return a single utility message
	 */
	public LinkedList<Integer> projectUtilMessages(LinkedList<Integer> util){
		//TODO
		return null;
	}

	@Override
	public boolean equals(Object o){
		Relation r = (Relation) o;
		return (this.child.equals(r.getChild()) && this.parent.equals(r.getParent())) || 
				(this.parent.equals(r.getChild()) && this.child.equals(r.getParent()));
	}

}
