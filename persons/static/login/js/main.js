var buttons=document.getElementById("buttons");
var username=document.getElementById("username");
var passwords=document.getElementById("passwords");
buttons.addEventListener("click",function(){
	
var x=username.value;
	var y="admin";
	if(x==y){
       window.open("http://127.0.0.1:8000/persons/output/");
	}
	else{
		alert("Oops!Wrong Username or password ");
	}
	
});
