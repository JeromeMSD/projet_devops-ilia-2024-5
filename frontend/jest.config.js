module.exports = {
    testEnvironment: 'jsdom',          // Simule un DOM pour Jest
    collectCoverage: true,             // Active la collecte de couverture de code
    coverageDirectory: 'coverage',     // Dossier où stocker les rapports de couverture
    coverageReporters: ['json', 'text', 'lcov'], // Formats des rapports (console, fichier, HTML)
    testMatch: ['**/tests/**/*.test.js'], // Quels fichiers tester (ici, tout fichier .test.js dans le dossier "tests")
  };
  