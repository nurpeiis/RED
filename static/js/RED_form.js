var action = 1;

function section_clicked(index) {
    var temp = "subsectionBox" + index;
    var grab = document.getElementById(temp);
    console.log(grab);

    if (action == 1){
        grab.style.display="flex";
        action = 2;
    }
    
    else if (action == 2){
        grab.style.display="none";
        action = 1;
    }
    
}