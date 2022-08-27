document.addEventListener('DOMContentLoaded', function () {

    const id_title_view = document.getElementById('id_title_view');
    const id_description_view = document.getElementById('id_description_view');

    const jsEncrypt = new JSEncrypt();
    jsEncrypt.setPrivateKey(getPrivateKey(1));

    id_title_view.innerText = jsEncrypt.decrypt(id_title_view.innerText);
    id_description_view.innerText = jsEncrypt.decrypt(id_description_view.innerText);
});

function getPrivateKey(organisationId) {
    const key = localStorage.getItem('privateKey');

    if (!key || key.length < 1) {
        window.location.href = '/encryption/setKey';
    }

    return key;
}