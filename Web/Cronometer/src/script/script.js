let seg = document.getElementById("seg");
let min = document.getElementById("min");
let hrs = document.getElementById("hrs");

let buttonStart = document.getElementById("start");

let mili = 99;
let timer = null;
let miniLoopClicked = false;
seg.innerHTML="10";

function format(n) {
    return n < 10 ? "0" + n : n;
}

function miliLoop() {
    clearInterval(timer);
    timer = setInterval(() => {
        if (mili <= 0) {
            mili = 99;
            segLoop();
        }
        else {
            mili--;
        }
    }, 10);
}

function segLoop() {
    let s = parseInt(seg.innerHTML);
    if (s <= 0) {
        seg.innerHTML = "00";
        minLoop();
    }
    else {
        s--;
        seg.innerHTML = format(s);
    }
}

function minLoop() {
    let m = parseInt(min.innerHTML);
    if (m <= 0) {
        min.innerHTML = "00";
        hrsLoop();
    }
    else {
        m--;
        min.innerHTML = format(m);
        seg.innerHTML = "59";
    }
}

function hrsLoop() {
    let h = parseInt(hrs.innerHTML);
    if (h <= 0) {
        hrs.innerHTML = "00";
        stopCronometer();
    }
    else {
        h--;
        hrs.innerHTML = format(h);
        min.innerHTML = "59";
        seg.innerHTML = "59";
    }
}

function pauseCronometer() {
    clearInterval(timer);
    timer = null;
}

function startCronometer() {
    miniLoopClicked = !miniLoopClicked;
    if (miniLoopClicked) {
        miliLoop();
        buttonStart.style.backgroundImage = "url(https://icons.veryicon.com/png/o/miscellaneous/round-thick-linear-icon/pause-96.png)";
    }
    else {
        pauseCronometer();
        buttonStart.style.backgroundImage = "url(https://w7.pngwing.com/pngs/261/757/png-transparent-computer-icons-google-play-music-button-play-angle-rectangle-triangle-thumbnail.png)";
    }
}


function stopCronometer() {
    seg.innerHTML="00";
    min.innerHTML="00";
    hrs.innerHTML="00";
    miniLoopClicked=false;
    buttonStart.style.backgroundImage = "url(https://w7.pngwing.com/pngs/261/757/png-transparent-computer-icons-google-play-music-button-play-angle-rectangle-triangle-thumbnail.png)";
}

function resetCronometer() {
    stopCronometer();
    hrs.innerHTML = "00";
    min.innerHTML = "00";
    seg.innerHTML = "10";
    mili = 99;
}
function editCronometer(){
    let command = prompt("digite o timer [hrs/min/seg]: ");
    command = command.trim().split('/');
    hrs.innerHTML=format(command[0])%60;
    min.innerHTML=format(command[1])%60;
    seg.innerHTML=format(command[2])%60;
}
