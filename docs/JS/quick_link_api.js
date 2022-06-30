let base_url = `${document.location.origin}${document.location.pathname}`;
let links = {
    'names' : {
        'Home' : 'Home',
        'Downlaods' : 'Downlaods'
    },
    'paths' : {
        'index' : './index.html',
        'downlaods' : './downlaods.html'
    }
}

if (document.URL == base_url + `?Link=${links.names.Home}`) {
    window.location = links.paths.index;
};

if (document.URL == base_url + `?Link=${links.names.Downlaods}`) {
    window.location = links.paths.downlaods;
};