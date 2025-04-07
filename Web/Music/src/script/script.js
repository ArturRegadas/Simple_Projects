const musics =[{
        name:"Musica 1",
        src:"https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    },
    {
        name:"Musica 2",
        src:"https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
    }
];

let musicName = document.getElementById("musicName");
let audio = document.getElementById("audio");
let progress = document.getElementById("progress");

let current = 0;
let startClicked = false;

function loadMusic(index){
    const currentMusic = musics[index];
    audio.src = currentMusic.src;
    musicName.innerHTML = currentMusic.name;
    audio.load();
    audio.play();
}
function startPause(){
    startClicked=!startClicked;
    if(startClicked) audio.play();
    else audio.pause();
}

function passMusic(passValue){
    current = (current+passValue)%musics.length;
    loadMusic(current);
}
audio.addEventListener("ended", passMusic(1));

//muda a barra de progresso baseado no tempo
audio.addEventListener("timeupdate", ()=>{
    progress.value = audio.currentTime;
    progress.max = audio.duration;
})
//muda o tempo baseado na barra de progresso
progress.addEventListener("input", ()=>{
    audio.currentTime = progress.value;
})
loadMusic(0);