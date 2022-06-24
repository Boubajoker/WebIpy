let downlaod_btn_01 = document.querySelector('#downlaod_btn_01');
let downlaod_btn_02 = document.querySelector('#downlaod_btn_02');

class FileDownlaoder {
    constructor(file) {
        this.file = file;
        this.file_found_confirm = null;

        fetch(this.file)
        .then(
            console.log('[INFO]: file:', this.file, 'exists.'),
            window.location = this.file,
            this.file_found_confirm = true,
            console.log(this.file_found_confirm)
        )
        .catch((err)=>{
            console.error('[ERROR]: An error as occured:', err + "."),
            this.file_found_confirm = false
            console.log(this.file_found_confirm)
        });
    };
};

downlaod_btn_01.addEventListener('click', ()=>{
    new FileDownlaoder(`./assets/others${downlaod_btn_01.ariaValueText}.zip`);
});

downlaod_btn_02.addEventListener('click', ()=>{
    new FileDownlaoder(`./assets/others${downlaod_btn_02.ariaValueText}.zip`);
});