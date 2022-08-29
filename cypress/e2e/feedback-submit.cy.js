describe('when visiting the home page', () => {
    it('redirects to the submission form', () => {
        cy.visit('http://127.0.0.1:8000/');
        cy.contains("Submit New Feedback");
    });
});

describe('testing form submit', function () {
    it('it should successfully submit a form', () => {
        cy.visit('http://127.0.0.1:8000/');
        cy.get('#id_title').type("Test Complaint");
        cy.get('#id_description').type("Test Description");
        cy.get('#id_category').select(1);
        cy.get('#submit-feedback').click();
        cy.wait(5000);
        cy.contains("Your Feedback");
    })
});