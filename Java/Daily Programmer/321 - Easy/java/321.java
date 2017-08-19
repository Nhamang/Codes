import java.util.*;
import java.text.*;

class challenge321{
	public static void main(String [] args){
		prog p1 = new prog();
		p1.runCode();
	}
}

class prog{
	
	String time;
	String AMPM = "AM";
	int hour, min;
	
	//Arrays containing the hours and minutes
	String [] strArrayHours = {"Twelve", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven"};
	String [] strArrayMin ={" ", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "thirteen", "fourteen", "fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
	String [] strArrayTens = {"Twenty", "Thirty", "Fouty", "Fifty"};
	
	void runCode(){
		
		/*
		Scanner user_input = new Scanner(System.in);
		System.out.print("What time is it?: ");
		time = user_input.next();
		*/
		while(true){
			//Gets the current time
			DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
			Date date = new Date();
			String time = dateFormat.format(date);
			
			//Splits time to hours and minutes and turns them to Integers
			String [] timeSplit = time.split(":");
			String [] minSplit;
			hour = Integer.parseInt(timeSplit[0]);
			min = Integer.parseInt(timeSplit[1]);
			
			time = "It's ";
			
			//Converts 24h to 12h and sets PM or AM
			if(hour >= 12){
				hour -= 12;
				AMPM = "PM";
			}
			
			time += strArrayHours[hour] + " ";
			
			
			if(min <= 19){
				if(min > 0 && min < 10){
					time += "oh ";
				}
				
				time += strArrayMin[min];
			}else{
				minSplit = timeSplit[1].split("");
				time += strArrayTens[Integer.parseInt(minSplit[0])-2] + " " + strArrayMin[Integer.parseInt(minSplit[1])];
				
			}
			
			time += " " + AMPM;
			System.out.println(time);
			try{
				Thread.sleep(60000);
			}catch(InterruptedException e){
				Thread.currentThread().interrupt();
			}
			//TimeUnit.SECONDS.sleep(1);
		}
	}
}