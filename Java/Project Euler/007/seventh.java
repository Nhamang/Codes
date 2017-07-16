class seventh{
	public static void main(String[]argv){
		prog p1 = new prog();
		p1.runCode();
	}
}

class prog{
	boolean [] prime;
	void runCode(){
		prime = primeCreator(100000000);
		
		int count = 1;
		int num = 3;
		int ans = 0;
		
		while(count <10001){
			if(isPrime(num)){
				count++;
				ans=num;
			}
			num++;
		}
		
		System.out.println(ans);
		
	}
	
	boolean isPrime(int pos){
		return prime[pos];
	}
	
	boolean [] primeCreator(int max){
		
		boolean[] tmpPrimes = new boolean[max+1];
		for(int i = 2; i<=max; i++){
			tmpPrimes[i] = true;
		}
		
		for(int fact = 2; fact*fact <= max; fact++){
			if(tmpPrimes[fact]){
				for(int rem=fact; rem*fact <= max; rem++){
					tmpPrimes[fact*rem] = false;
				}
			}
		}
		return tmpPrimes;
	}	
}