import java.lang.Math;
public class challenge322{
  public static void main(String[] args){
    code c1 = new code(Integer.parseInt(args[0]));
    c1.runCode();
  }
  

}

class code{
  
  int n;
  code(int n){
    this.n = n;
  }
  
  public void runCode(){
    
    int maxN = (int) Math.pow(10, n);
    
    for (int i = maxN-1; i>0; i--){
      for(int j = maxN-1; i>0; i++){
        if(isPalindrome(""+(i*j))){
          System.out.println("The palindrome "+ (i*j) +" is a product of "+ i + " and "+ j);
        }
      }
    }
    
  }
  
  public boolean isPalindrome(String n){
    return n.equals(new StringBuilder(n).reverse().toString());
  }
}