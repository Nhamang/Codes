class fourth{
	public static void main(String[]argv){
		prog p1 = new prog();
		p1.runCode();
	}
}

class prog{
	
	int result = 0;
	String testInt = "";
	boolean found = false;
	int maxPal =-1;
	void runCode(){
		for(int i=999; i>99; i--){
			for(int j = 999; j>99; j--){
				testInt = ""+(i*j);
				if(isPalindrome(testInt) && ((i*j)>maxPal)){
					maxPal= i*j;
				}
			}
		}
		System.out.println("\n" + maxPal);
	}
	
	boolean isPalindrome(String str) {
		return str.equals(new StringBuilder(str).reverse().toString());
	}
}