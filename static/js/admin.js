document.addEventListener('DOMContentLoaded', function () {

    const id_title_view = document.getElementById('id_title_view');
    const id_description_view = document.getElementById('id_description_view');

    const jsEncrypt = new JSEncrypt();
    jsEncrypt.setPrivateKey(getPrivateKey());

    console.log(getPrivateKey());

    const title = jsEncrypt.decrypt(id_title_view.innerText);

    if (title === null) {
        window.location.href = '/encryption/setKey';
    }

    id_title_view.innerText = title;
    id_description_view.innerText = jsEncrypt.decrypt(id_description_view.innerText);
});

function getPrivateKey() {
    const key = localStorage.getItem('privateKey');

    if (!key || key.length < 1) {
        window.location.href = '/encryption/setKey';
    }

    return key;
}