describe('when visiting feedback admin', function () {
    it('it requires login', () => {
        cy.visit('http://127.0.0.1:8000/feedbacks');
        cy.contains('Sign In');
    })

    it('fails login with incorrect credentials', () => {
        cy.visit('http://127.0.0.1:8000/feedbacks');
        cy.get('input[name=login]').type('admin');
        cy.get('input[name=password]').type('12345');
        cy.get('button[type=submit]').click();
        cy.contains('password you specified are not correct');
    });

    it('successful login with correct credentials', () => {
        cy.visit('http://127.0.0.1:8000/feedbacks');
        cy.get('input[name=login]').type('admin');
        cy.get('input[name=password]').type('admin');
        cy.get('button[type=submit]').click();
        cy.contains('Successfully signed in');
    });
});