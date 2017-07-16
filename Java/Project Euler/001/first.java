class first{
	public static void main(String [] argv){
			prog p1 = new prog();
			p1.runCode();
	}
}

class prog{
	static void runCode(){
		int total = 0;
		
		for(int i = 1; i < 1000; i++){
			if((i%3==0)){
				total=total+i;
			}else if(i%5==0){
				total+=i;
			}
		}
		
		System.out.println("\n"+ total);
	}
}