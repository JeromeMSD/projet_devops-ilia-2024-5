export class LoginService {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }

    /**
     * Authentifie l'utilisateur et récupère le token.
     * @param {string} userName - Le nom d'utilisateur.
     * @param {string} password - Le mot de passe.
     * @returns {Promise<string>} - Le token de connexion.
     * @throws {Error} - Si l'authentification échoue.
     */
    async login(userName, password) {
        const url = `${this.baseUrl}/auth/login`;
        const params = new URLSearchParams({ userName, password });

        const response = await fetch(`${url}?${params.toString()}`, {
            method: 'POST',
        });

        if (response.ok) {
            const data = await response.json();
            return data.token;
        } else if (response.status === 401) {
            throw new Error('Identifiants incorrects.');
        } else {
            throw new Error('Erreur lors de la connexion.');
        }
    }
}
