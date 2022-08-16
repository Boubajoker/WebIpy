let downlaod_btn_01 = document.querySelector('#downlaod_btn_01');
let downlaod_btn_02 = document.querySelector('#downlaod_btn_02');
let downlaod_btn_03 = document.querySelector('#downlaod_btn_03');
let downlaod_btn_04 = document.querySelector('#downlaod_btn_04');

async function get_file(file) {
    const response = await fetch(file);

    if (response.readyState === 4 && response.status === 200) {
        console.log(response.text());
    };

    if (response.status === 400) {
        throw new Error('400 (Bad Request)');
    } else if (response.status === 404) {
        throw new Error('404 (not found)');
    };
    
    return response;
};

async function downlaod_file(file) {
    const response = await get_file(file);

    if (response.status === 400 || response.status === 404) {
        window.location.reload();
    } else {
        window.location = file;
    }
};


downlaod_btn_01.addEventListener('click', ()=>{
    this.downlaod_file(`./assets/others${downlaod_btn_01.ariaValueText}.zip`);
});

downlaod_btn_02.addEventListener('click', ()=>{
    this.downlaod_file(`./assets/others${downlaod_btn_02.ariaValueText}.zip`);
});

downlaod_btn_03.addEventListener('click', ()=>{
    this.downlaod_file(`./assets/others${downlaod_btn_03.ariaValueText}.zip`);
});

downlaod_btn_04.addEventListener('click', ()=>{
    this.downlaod_file(`./assets/others${downlaod_btn_04.ariaValueText}.zip`);
});