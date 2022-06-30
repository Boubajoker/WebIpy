let news_section_title = document.querySelector('#news_section_title');
let news_section_desc = document.querySelector('#news_section_desc');
let news_section_img = document.querySelector('#news_section_img');
let news_section_vid = document.querySelector('#news_section_vid');

async function direct_refresh(file, callback) {
    const response = await fetch(file);

    if (response.readyState === 4 && response.status === 200) {
        callback(response.responseText)
    }
    if (response.status === 400) {
        throw new Error('400 (Bad Request)');
    }
    if (response.status === 404) {
        throw new Error('404 (not found)');
    }
    return response;
}

async function getnews() {
    const response = await direct_refresh('news.json');
    const news_data = await response.json();

    if (news_data.NEWS_ID === "WEBIPY_JSON_NEWS_REQUEST_FILE") {
        news_section_title.innerHTML = `<h1>[INFO]: ${news_data.request_package.title}</h1>`;
        news_section_desc.innerHTML = `<p>${news_data.request_package.desc}</p>`;
    
        if (news_data.request_package.additional_img === null) {
            news_section_img.innerHTML = '<p>No image with the info</p>';
        } else {
            news_section_img.innerHTML = `<img src="${news_data.request_package.additional_img}" title="${news_data.request_package.desc}">`;
        };
    
        if (news_data.request_package.additional_video === null) {
            news_section_vid.innerHTML = '<p>No video with the info</p>';
        } else {
            news_section_vid.innerHTML = `<video muted="" loop="" autoplay="" src="${news_data.request_package.additional_video}.mp4">`;
        };
    } else {
        console.warn('[!WARN!]: The news.json file does not correspond to the normal ID.');
    };

    return news_data;
}

this.getnews();