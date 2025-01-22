USE polytex;

CREATE TABLE utilisateur (
    nom_utilisateur VARCHAR(50) NOT NULL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    pseudo VARCHAR(50) NOT NULL
);

INSERT INTO utilisateur (Nom, Prenom, Email, Mot_de_passe, Nom_utilisateur, Pseudo)
VALUES
    ('Dupont', 'Jean', 'jean.dupont@example.com', '$2y$10$nrDWDpEgOI0JrMVZs00rrOsnD/dALCYn3T4nKWIX3EyrpNMF81TSe', 'jdupont', 'JeanD'),
    ('Martin', 'Sophie', 'sophie.martin@example.com', '$2y$10$nrDWDpEgOI0JrMVZs00rrOsnD/dALCYn3T4nKWIX3EyrpNMF81TSe', 'smartin', 'SophieM'),
    ('Durand', 'Luc', 'luc.durand@example.com', '$2y$10$nrDWDpEgOI0JrMVZs00rrOsnD/dALCYn3T4nKWIX3EyrpNMF81TSe', 'ldurand', 'LucD'),
    ('Moreau', 'Claire', 'claire.moreau@example.com', '$2y$10$nrDWDpEgOI0JrMVZs00rrOsnD/dALCYn3T4nKWIX3EyrpNMF81TSe', 'cmoreau', 'ClaireM'),
    ('Rousseau', 'Paul', 'paul.rousseau@example.com', '$2y$10$nrDWDpEgOI0JrMVZs00rrOsnD/dALCYn3T4nKWIX3EyrpNMF81TSe', 'prousseau', 'PaulR');
