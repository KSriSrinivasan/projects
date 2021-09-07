'use strict';
//element selectors

const playerCur=document.querySelectorAll(".player--active");
const totalScore0=document.getElementById('score--0');
const totalScore1=document.getElementById('score--1');
const currentScore0=document.getElementById('current--0');
const currentScore1=document.getElementById('current--1');

const player0=document.querySelector(".player--0");
const player1=document.querySelector(".player--1");
const dice=document.querySelector(".dice");
const roll= document.querySelector(".btn--roll");
const hold=document.querySelector(".btn--hold");
const reset=document.querySelector(".btn--new");
//intialization
let playing,playerActive,currentScore,score;
var init=function(){

totalScore0.textContent=0;
totalScore1.textContent=0;
currentScore1.textContent=0;
currentScore0.textContent=0;
dice.classList.add('hidden');
playing=true;
playerActive=0;
currentScore=0;
score=[0,0];
}
init();
//player switch
var playerSwitch=function(){
    
        document.getElementById(`current--${playerActive}`).textContent=0;
        currentScore=0;
        playerActive=playerActive===0?1:0;
        player0.classList.toggle('player--active');
        player1.classList.toggle('player--active');
}

//roll event
roll.addEventListener("click",function(){
    //dice random
if(playing===true)
{
    var diceNum=Math.trunc(Math.random()*6+1);
    console.log(diceNum);
    //dice appear
    dice.src=`dice-${diceNum}.png`;
    dice.classList.remove('hidden');
    //if 1
    if(diceNum!=1)
        {    console.log(diceNum+'okokok');

            currentScore+=diceNum;
         
            console.log(currentScore);
            document.getElementById(`current--${playerActive}`).textContent=currentScore;
         
        }
    else
    {
         score[playerActive]+=currentScore;
         document.getElementById(`score--${playerActive}`).textContent= score[playerActive];
        playerSwitch();
    }
 }


});
hold.addEventListener("click",function(){
if(playing===true)
{
  score[playerActive]+=currentScore;
 document.getElementById(`score--${playerActive}`).textContent= score[playerActive];
 if(score[playerActive]>=30)
     {
        
         document.getElementById(`current--${playerActive}`).textContent=0;
         document.querySelector(`.player--${playerActive}`).classList.remove("player--active");
         document.querySelector(`.player--${playerActive}`).classList.add("player--winner");
         playing=false;
         console.log(playing);
     }
       
 else
             playerSwitch();

}
});
reset.addEventListener("click",function()
{
     document.querySelector(`.player--0`).classList.add("player--active");
    document.querySelector(`.player--${playerActive}`).classList.remove("player--winner");
    init();
   
    
});
