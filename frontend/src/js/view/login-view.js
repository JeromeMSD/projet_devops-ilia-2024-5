export class LoginView {
    constructor() {
        this.emailField = document.getElementById('email-field');
        this.pseudoField = document.getElementById('pseudo-field');
        this.passwordField = document.getElementById('password-field');
        this.errorBox = this.createErrorBox();
    }

    /**
     * Récupère les données de connexion de l'utilisateur.
     * @returns {Object} - Les informations de connexion.
     */
    getCredentials() {
        return {
            email: this.emailField.value.trim(),
            pseudo: this.pseudoField.value.trim(),
            password: this.passwordField.value.trim(),
        };
    }

    /**
     * Affiche un message d'erreur à l'utilisateur.
     * @param {string} message - Le message d'erreur.
     */
    showError(message) {
        this.errorBox.textContent = message;
        this.errorBox.style.display = 'block';
    }

    /**
     * Cache le message d'erreur.
     */
    hideError() {
        this.errorBox.style.display = 'none';
    }

    /**
     * Crée un élément de boîte d'erreur.
     * @returns {HTMLElement} - L'élément de boîte d'erreur.
     */
    createErrorBox() {
        const errorBox = document.createElement('div');
        errorBox.id = 'error-box';
        errorBox.style.display = 'none';
        errorBox.style.color = 'red';
        errorBox.style.marginTop = '10px';
        document.getElementById('login-box').appendChild(errorBox);
        return errorBox;
    }
}
