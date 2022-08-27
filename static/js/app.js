document.addEventListener('DOMContentLoaded', function () {
    function getPublicKey(organisationId) {
        return `-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9CbJCg1MZA5Z8TvgT/o9Vtd54
XnYmFq4lYwh15Hx9Uhjpty0ih7ZHeho5jJ7KziFgvB0dX5r3+JbwXcrGNbuM7hQg
nTEFCEKHc/HgkBSDPuJJur2QprbM9grXSuN9AZA3zwX6Tgg8P2Y4iev+dImruupG
2BuYcmZsEEf4qAWWSQIDAQAB
-----END PUBLIC KEY-----`;
    }

    const createButton = document.getElementById('submit-feedback');
    const createForm = document.getElementById('create-form');

    createButton.addEventListener('click', (event) => {
        event.preventDefault();
        createButton.setAttribute('disabled', 'disabled');
        createButton.innerText = 'Encrypting...';
        const jsEncrypt = new JSEncrypt();
        jsEncrypt.setPublicKey(getPublicKey(1));

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
    });
});