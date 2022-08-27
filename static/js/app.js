document.addEventListener('DOMContentLoaded', function () {

    const createButton = document.getElementById('submit-feedback');
    const createForm = document.getElementById('create-form');
    const categoryId = document.getElementById('id_category');

    createButton.addEventListener('click', (event) => {
        event.preventDefault();
        createButton.setAttribute('disabled', 'disabled');
        createButton.innerText = 'Encrypting...';
        const jsEncrypt = new JSEncrypt();
        getOrganisationId(categoryId.value).then(organisationId => {
            getPublicKey(organisationId).then((publicKey) => {
                jsEncrypt.setPublicKey(publicKey);

                const title = document.getElementById('id_title').value;
                const description = document.getElementById('id_description').value;

                const encryptedTitle = jsEncrypt.encrypt(title);
                const encryptedDescription = jsEncrypt.encrypt(description);

                document.getElementById('id_title').value = encryptedTitle;
                document.getElementById('id_description').value = encryptedDescription;

                setTimeout(() => {
                    createButton.innerText = 'Submitting...';
                    createForm.submit();
                }, 1000);
            })
        });
    });
});

function getOrganisationId(categoryId) {
    return new Promise((resolve) => {
        fetch(`/api/categories/${categoryId}`).then(response => {
            response.json().then(json => resolve(json.associated_organisation));
        })
    });
}

function getPublicKey(organisationId) {
    return new Promise((resolve) => {
        fetch(`/api/organisations/${organisationId}/publicKey`).then(response => {
            response.json().then(json => resolve(json.publicKey));
        })
    });
}