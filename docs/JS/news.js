let news_section_title = document.querySelector('#news_section_title');
let news_section_desc = document.querySelector('#news_section_desc');
let news_section_img = document.querySelector('#news_section_img');
let news_section_vid = document.querySelector('#news_section_vid');

// async function loadJSONFile(callback) {   
//     var request_handler = new XMLHttpRequest();

//     request_handler.overrideMimeType("application/json");
//     request_handler.open('GET', 'news.json', true);

//     request_handler.onreadystatechange = function () {
//         if (request_handler.readyState == 4 && request_handler.status == "200") {
//           callback(request_handler.responseText);
//         } if (request_handler.status === 400) {
//             throw new Error('400 (Bad Request)')
//         }
//     };
//     request_handler.send(null);  
// }
// loadJSONFile(function(response) {
//    var news_data = JSON.parse(response);
// });
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
    const response = await direct_refresh(`./news.json`);
    const news_data = await response.json();

    news_section_title.innerHTML = `<h1>[INFO]: ${news_data.request_package.title}</h1>`;
    news_section_desc.innerHTML = `<p>${news_data.request_package.desc}</p>`;

    if (news_data.request_package.additional_img === null) {
        news_section_img.innerHTML = '<p>No image with the info</p>';
    } else {
        news_section_img.innerHTML = `<img src="${news_data.request_package.additional_img}">`;
    };

    if (news_data.request_package.additional_video === null) {
      news_section_vid.innerHTML = '<p>No video with the info</p>';
    } else {
        news_section_vid.innerHTML = `<video muted="" loop="" autoplay="" src="${news_data.request_package.additional_video}.mp4">`;
    };

    return news_data;
}

this.getnews();