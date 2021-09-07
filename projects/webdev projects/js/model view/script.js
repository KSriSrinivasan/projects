/*'use strict';
//hh
const modelsBtn = document.querySelectorAll("show-modal");
const model = document.querySelector("modal");
const overlay = document.querySelector("overlay");

for (let i = 0; i < openModel.length; i++) {
	modelsBtn[i].addEventListener("click", function () {

		model.classList.remove("hidden");
		overlay.classList.remove("hidden");
	});

}
*/

'use strict';

var modal = document.querySelector('.modal');
var overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
const btnsOpenModal = document.querySelectorAll('.show-modal');

const modalOpen=function(){
	modal.classList.remove('hidden');
	overlay.classList.remove('hidden');						  
};
const modalClose=function(){
	modal.classList.add('hidden');
	overlay.classList.add('hidden');						  
};
for (let i = 0; i < btnsOpenModal.length; i++) {
	btnsOpenModal[i].addEventListener("click", modalOpen) ;

}
btnCloseModal.addEventListener("click", modalClose) ;
overlay.addEventListener("click", modalClose) ;


document.addEventListener("keydown",function(e){
	console.log(e.key);
	if(e.key==="Escape"&&!modal.classList.contains("hidden"))
				modalClose();
		}
	
});