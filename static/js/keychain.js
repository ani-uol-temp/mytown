document.addEventListener('DOMContentLoaded', function () {
    const setButton = document.getElementById('set_private_key');
    const clearButton = document.getElementById('clear_private_key');

    setButton.addEventListener('click', (ev) => {
        ev.preventDefault();
        const keyText = document.getElementById('text_private_key').value;

        if (!keyText || keyText.length < 10) {
            alert("Invalid Key")
            return;
        }

        localStorage.setItem('privateKey', keyText);
        alert("Your private key has been set.");
        window.location.href = '/feedbacks';
    });

    clearButton.addEventListener('click', (ev) => {
        ev.preventDefault();
        localStorage.removeItem('privateKey');
    });

    if (localStorage.getItem('privateKey')) {
        clearButton.removeAttribute('disabled');
    } else {
        clearButton.setAttribute('disabled', 'disabled');
    }
});