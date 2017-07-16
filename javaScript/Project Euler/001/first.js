val sum = 0;

for(val i = 3; i < 1000; i++){
	if((i%3==0) || (i%5==0)){
		sum+=i;
	}
}
console.log(sum);