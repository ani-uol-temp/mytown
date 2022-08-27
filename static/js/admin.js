document.addEventListener('DOMContentLoaded', function () {

    const id_title_view = document.getElementById('id_title_view');
    const id_description_view = document.getElementById('id_description_view');

    const jsEncrypt = new JSEncrypt();
    jsEncrypt.setPrivateKey(getPrivateKey(1));

    id_title_view.innerText = jsEncrypt.decrypt(id_title_view.innerText);
    id_description_view.innerText = jsEncrypt.decrypt(id_description_view.innerText);
});

function getPrivateKey(organisationId) {
    return `-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQC9CbJCg1MZA5Z8TvgT/o9Vtd54XnYmFq4lYwh15Hx9Uhjpty0i
h7ZHeho5jJ7KziFgvB0dX5r3+JbwXcrGNbuM7hQgnTEFCEKHc/HgkBSDPuJJur2Q
prbM9grXSuN9AZA3zwX6Tgg8P2Y4iev+dImruupG2BuYcmZsEEf4qAWWSQIDAQAB
AoGBALIoYkVHSVioxfnP3wPRBLtNlSayN/17oJKBvCaHuT/O0MXrqfECICtLC04z
ljAihtiJUZMuWHndYjuU2ZdmaqMvoSpTZhuoPY9IsxDrQyaOG8B33hqCri7U8bq2
D8vt7JQ3yhPvnx0AIttiqnlovYiHwptfJP83qqN1CdIu+iTVAkEA4sc0UMWqi+G6
trBuNPCU9WKhKx/obKPt3HCOqw9ObUZgt9P3t4UkFfI951K7RacrJxmYo5AMZwDq
/z4C6bhImwJBANVliwGzRdXWW+sXRXmzAhCS0TOncgkFn22OZeMXfQtl3tkY/Dw8
OZnFoegPnYAVrBAVDkXrGCNg6lk22+fn0OsCQQCgS5ZbEZ0/SssjnwoHOZbQ7Gpn
hSJQyH61Nopht2wEKZ7r0VRj0CR1rsi63eupjEQgWyNdWdCqbietSzPb6HrJAkAS
pdf64w6kPCI2LgdtNh5lEl9jsys87Jfc/AedS60qtNE/iXZpUR37eRDH9a1exwYN
NbnUlFG8rbhs6WVYI6LXAkEA0mKaWOnAP5zwOifgDRz7nxM1XfKpKiS8FBeFlUJh
U01k3kwfvZQYxnH+HxxIckNpFePRpQ6aEAdJV6WIKcQNTQ==
-----END RSA PRIVATE KEY-----`;
}