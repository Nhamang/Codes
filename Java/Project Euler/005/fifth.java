class fifth{
	public static void main(String[]argv){
		prog p1 = new prog();
		p1.runCode();
	}
}

class prog{
	
	void runCode(){
		for(int i = 1; ; i++){
			if(isDevisable(i)){
				System.out.println("\n"+ i);
				break;
			}
		}
	}
	
	boolean isDevisable(int testNr){
		for(int i = 1; i <= 20; i++){
			if((testNr%i) != 0){
				return false;
			}
		}
		return  true;
	}
}