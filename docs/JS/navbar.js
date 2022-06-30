let home_btn = document.querySelector('#home_btn');
let downlaods_btn = document.querySelector('#downlaods_btn');
let credits_btn = document.querySelector('#credits_btn');
let audio_player = new Audio();

home_btn.addEventListener('click', ()=>{
    fetch('./index.html')
    .then(
        window.location = "./index.html"
    )
    .catch((err)=>{
        console.error(`[ERROR]:${err}`);
    });
});

downlaods_btn.addEventListener('click', ()=>{
    fetch('./downlaods.html')
    .then(
        window.location = "./downlaods.html",
    )
    .catch((err)=>{
        console.error(`[ERROR]:${err}`);
    });
});

credits_btn.addEventListener('click', ()=>{
    window.location = "https://github.com/Boubajoker/WebIpy/blob/master/ThirdPartyNotices.md";
});

document.body.addEventListener('click', ()=>{
    audio_player.src = "./assets/sounds/click.mp3";
    audio_player.play();
});

document.addEventListener('keydown', (e)=> {
    e.preventDefault();
    // console.log(e)
    console.log(`[INFO]: Pressed key \`${e.key}\`; code: \`${e.code}\``)
    if (
        e.key.toLocaleLowerCase() === 'h'
        && e.ctrlKey
    ) {
       window.location = './index.html';
    };

    if (
        e.key.toLocaleLowerCase() === 'd'
        && e.ctrlKey
    ) {
        window.location = './downlaods.html';
    };
    
    if (
        e.key.toLocaleLowerCase() === 'r'
        && e.altKey
        && e.metaKey
    ) {
        window.location.reload();
    };

    if (
        e.key.toLocaleLowerCase() === 'r'
        && e.ctrlKey
    ) {
        alert('To relaod the page press `Windows`/`Apple` + `Alt` + `R')
    };

    if (
        e.code.toLocaleLowerCase() === 'F5'
    ) {
        alert('To relaod the page press `Windows`/`Apple` + `Alt` + `R')
    };
});