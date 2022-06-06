let home_btn = document.querySelector('#home_btn');
let downlaods_btn = document.querySelector('#downlaods_btn');
let credits_btn = document.querySelector('#credits_btn');

home_btn.addEventListener('click', ()=>{
    fetch('./index.html')
    .then(
        window.location = "./index.html"
    )
    .catch((err)=>{
        console.error(`[ERROR]:${err}`)
    });
});

downlaods_btn.addEventListener('click', ()=>{
    fetch('./downlaods.html')
    .then(
        window.location = "./downlaods.html"
    )
    .catch((err)=>{
        console.error(`[ERROR]:${err}`)
    });
});

credits_btn.addEventListener('click', ()=>{
    window.location = "./credits.html"
});