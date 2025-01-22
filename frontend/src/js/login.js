import { LoginController } from './controller/login-controller.js';

document.addEventListener('DOMContentLoaded', () => {
    const controller = new LoginController();
    controller.init();
});
