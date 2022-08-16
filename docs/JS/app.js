let home_btn = document.querySelector('#home_btn');
let downlaods_btn = document.querySelector('#downlaods_btn');
let credits_btn = document.querySelector('#credits_btn');
let audio_player = new Audio();
let copy_code_btn = document.querySelector('#copy_btn');
let check_box = document.querySelector('#check_box');

async function check_internet() {
    const response = await fetch('"https://github.com/Boubajoker/WebIpy/');

    if (response.status === 400 || response.status === 404) {
        alert('Whoops... Something went wrong !');
    } else {
        window.location = "https://github.com/Boubajoker/WebIpy/blob/master/ThirdPartyNotices.md";
    };
}

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

});

document.body.addEventListener('click', ()=>{
    audio_player.src = "./assets/sounds/click.mp3";
    audio_player.play();
});

if (page_name === 'main_page') {
    copy_code_btn.addEventListener('click', ()=>{
        if ('Clipboard' in window) {
            navigator.clipboard.writeText('import webipy\n\nwebipy.APP_ENGINE.setApplicationName(\'[app name]\')\nwebipy.APP_ENGINE.setApplicationVersion(\'[app version]\')\nwebipy.APP_ENGINE.setWindowIcon(webipy.QIcon(\'[icon]\'))\nroot = webipy.WebIPyAppEngine(width=1080, height=700, main_url="[html file path]")\n\nif __name__ == \'__main__\':\n webipy.APP_ENGINE.exec()');
            check_box.style.display = 'block';
            check_box.style.animation = 'fade 0.5s ease-in';
            setTimeout(()=>{
              check_box.style.display = 'none';
            }, 4500);
        } else {
            console.error('[ERROR]: Browser Not Supported');
        }
    });
};

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