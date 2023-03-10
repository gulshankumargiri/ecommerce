
let x =0;
    document.getElementById("totalitem").innerHTML=x;

function add(val){
    x= x+1;
    document.getElementById("c").innerText=x;

    document.getElementById("addeditem").innerHTML += "<LI>"+val+"</LI>";
}