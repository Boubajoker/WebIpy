let base_url = `${document.location.origin}${document.location.pathname}`;

if (document.URL == base_url + "#QLID=Home") {
    window.location = './index.html';
}

if (document.URL == base_url + "#QLID=Downlaods") {
    window.location = './downlaods.html';
}