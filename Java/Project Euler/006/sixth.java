class sixth{
	public static void main(String[]argv){
		prog p1 = new prog();
		p1.runCode();
	}
}

class prog{
	
	
	void runCode(){
		int tot1 = 0;
		int tot2 = 0;
		int sumtot = 0;
		for(int i = 1; i <=100; i++){
			tot1+=(i*i);
			tot2+=i;
		}
		tot2*=tot2;
		sumtot = tot2-tot1;
		
		System.out.println("tot1: "+ tot1 +" tot2: "+ tot2 +" sumtot: "+ sumtot);
	}
}