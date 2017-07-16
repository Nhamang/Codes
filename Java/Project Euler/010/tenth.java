class tenth{
	public static void main(String[]argv){
		prog p1 = new prog();
		p1.runCode();
	}
}

class prog{
	
	boolean [] primes;
	void runCode(){
		primes = primeCreator(2000000);
		long sum = 2;
		int current = 2;
		int tmpNum;
		while(current != -1){
			tmpNum = nextPrime(current);
			if(tmpNum != -1) sum += tmpNum;
			current = tmpNum;
		}
		System.out.println(sum);
	}
	
	int nextPrime(int current){
		for(int i = current+1; i<primes.length; i++){
			if(primes[i]) return i;
		}
		return -1;
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