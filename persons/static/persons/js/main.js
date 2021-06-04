var buttons=document.getElementById("buttons");
var username=document.getElementById("username");
var passwords=document.getElementById("passwords");
buttons.addEventListener("click",function(){
	
var x=username.value;
	var y="admin";
	if(x==y){
		window.location = '{% url 'persons:output' %}'
		alert("hey");
	}
	else{
		alert("ley");
	}
	
});