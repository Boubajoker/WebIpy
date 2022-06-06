let downlaod_btn_01 = document.querySelector('#downlaod_btn_01');

class FileDownlaoder {
    constructor(file) {
        this.file = file;
        this.file_found_confirm = null;

        fetch(this.file)
        .then(
            console.log('[INFO]: file:', this.file, 'exists.'),
            window.location = this.file,
            this.file_found_confirm = true
        )
        .catch((err)=>{
            console.error('[ERROR]: An error as occured:', err + "."),
            this.file_found_confirm = false
        });
    };
};

downlaod_btn_01.addEventListener('click', ()=>{
    new FileDownlaoder(`./assets/others/webipy_v0.0.1_Alpha_A1.zip`);
});

async function getnews(json_file) {

}

this.getnews('./news.json');