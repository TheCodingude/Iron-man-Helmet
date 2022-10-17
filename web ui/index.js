const batterypercent = document.getElementById("percent");
const bar = document.getElementById("batteryLevel");
const mostRecent = document.getElementById("mostRecent");
const secondRecent = document.getElementById("secondRecent");
const thrdRecent = document.getElementById("thirdRecent");
const all = document.getElementById("all");


function getBatteryPercent(){

    let percent = "4%";

    batterypercent.innerText = percent;
    bar.style.width = percent;

    temp = parseInt(percent)
    if(temp <= 30 && temp > 15){
        bar.style.backgroundColor = "#e0c302";
    }
    else if(temp <= 15){
        bar.style.backgroundColor = "#cc0404";
    }
    else{
        bar.style.backgroundColor = "green";
    }
}


all.addEventListener("click", () => {
    console.log("Clicked")
})

