import { LoginService } from '../services/login-service.js';
import { LoginView } from '../view/login-view.js';

export class LoginController {
    constructor() {
        this.service = new LoginService('https://authentification.polytex.com');
        this.view = new LoginView();
    }

    
    init() {
        const passwordField = this.view.passwordField;

        passwordField.addEventListener('keypress', async (event) => {
            if (event.key === 'Enter') {
                await this.handleLogin();
            }
        });
    }

    
    async handleLogin() {
        const { email, pseudo, password } = this.view.getCredentials();

        
        if (!pseudo || !password) {
            this.view.showError('Veuillez remplir tous les champs obligatoires.');
            return;
        }

        try {
            this.view.hideError();
            const token = await this.service.login(pseudo, password);
            console.log('Connexion réussie. Token :', token);

            
            localStorage.setItem('authToken', token);
            window.location.href = 'mainfeed.html'; 
        } catch (error) {
            this.view.showError(error.message);
        }
    }
}
