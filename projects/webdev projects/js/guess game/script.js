'use strict';
/*
console.log(document.querySelector(".message").textContent);
console.log(document.querySelector(".guess").value)
*/

var gNumber=Math.trunc(Math.random()*20)+1;
var score= Number(document.querySelector('.score').textContent);
var highscore=0;
document.querySelector(".check").addEventListener("click",function()
    {
            var guess=Number(document.querySelector(".guess").value);
        if(score>1)
         {
			if(!guess)
            {
              document.querySelector(".message").textContent="No Number";
            }
            else if(guess===gNumber)
            {
             document.querySelector(".number").textContent=gNumber;
             document.querySelector(".message").textContent="Congratulations You Won!!";
			 document.querySelector('body').style.backgroundColor='green';
			 document.querySelector('.number').style.width="30rem";
			 if(score>highscore)
					 highscore=score;
            }
	        else
			{
               if(guess>gNumber)
                document.querySelector(".message").textContent="Too high";
               
               else
                 document.querySelector(".message").textContent="Too low";
               score-=1;
            }
		 }
	     else
	     {
		  document.querySelector(".message").textContent="Game Over";
	      score=0;
		 }
         document.querySelector(".score").textContent=score;
         document.querySelector(".highscore").textContent=highscore;

        });
  document.querySelector(".again").addEventListener("click",function()
{
	  gNumber=Math.trunc(Math.random()*20)+1;
	  score=20;
      document.querySelector('.score').textContent=20;
	  
	  
	  document.querySelector('.number').textContent="?";	  
	  document.querySelector(".message").textContent="Start guessing...";
	  document.querySelector('body').style.backgroundColor='#222';
	  document.querySelector('.number').style.width="15rem";
  
 });
    
    