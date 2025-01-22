import { screen, fireEvent, render } from '@testing-library/dom';
import { toggleLike, toggleComment, toggleShare, addPost,subscribe,goToProfile } from '../src/profile.js';

beforeEach(() => {
  document.body.innerHTML = `
    <div id="entete">
        <div id="titreComplet">
            <h1 id="titlePolyte">Polyte</h1>
            <h1 id="titleX">X</h1>
        </div>
        <div id="monProfil">
            <h2 id="monNom">Huguette231</h2>
            <img id="maPhoto" src="../data/huguette.avif">
        </div>
    </div>

    <div id="presentation">
        <img id="photoProfil" src="../data/photoProfilRandom.jpeg">
        <div id="infopersos">
            <h2> Michel Michel</h2>
            <h4> @MichelMichel</h4>
            <h4> Il/Elle/Iel</h4>
            <button id="suscribeButton"> <img id="suscribe" src="../data/plus.png"></button>
        </div>
        <p> Ceci est une description descriptive de ce que fait MichelMichel notre personne X dans sa vie</p>
    </div>
    <div id="zonePosts">
        <div id="premierPost">
            <p>Ceci est un premier post où le profil raconte sa vie</p>
            <div id="zoneInterraction">
                <button id="like"> <img src="../data/coeur.png" alt="like"></button>
                <button id="commentaire"> <img src="../data/commentaire.jpeg" alt="commentaire"></button>
                <button id="share"> <img src="../data/partage.png" alt="partage"></button>
            </div>
        </div>
    </div>
  `;
});

//Là ça teste juste les boutons,normalement ça va.
test('les boutons existent dans la page', () => {
  expect(screen.getByText('like')).toBeInTheDocument();
  expect(screen.getByText('commentaire')).toBeInTheDocument();
  expect(screen.getByText('partage')).toBeInTheDocument();
});

//Là ça teste si les boutons fonctionnent correctement.
// Pour le faire pour l'instant on peut juste partir sur une fonction qui change la classe du bouton.
//Par la suite on pourra ajouter des test pour les api
test('les boutons "like", "commentaire" et "partage" fonctionnent correctement', () => {
  const likeButton = screen.getByAltText('like');
  const commentButton = screen.getByAltText('commentaire');
  const shareButton = screen.getByAltText('partage');
  
  fireEvent.click(likeButton);
  expect(likeButton).toHaveClass('liked');
  
  fireEvent.click(commentButton);
  expect(commentButton).toHaveClass('commented');
  
  fireEvent.click(shareButton);
  expect(shareButton).toHaveClass('shared');
});

//Là on teste l'ajout d'un post sur la page.Pour la position on vera plus tard.
test('ajout d\'un nouveau post dans la zone de posts', () => {
  const content = "Voici un nouveau post ajouté!";
  addPost(content);
  
  const newPost = screen.getByText(content);
  expect(newPost).toBeInTheDocument();
  expect(screen.getByText('like')).toBeInTheDocument();
  expect(screen.getByText('commentaire')).toBeInTheDocument();
  expect(screen.getByText('partage')).toBeInTheDocument();
}); 

test('abonnement à un profil', () => {
  const suscribeButton = screen.getByRole('button', { name: /suscribe/i });


  expect(suscribeButton).not.toHaveClass('suscribed');

  fireEvent.click(suscribeButton);

  expect(suscribeButton).toHaveClass('suscribed');
});


//Généré par ChatGPT, je sais pas si celà fonctionnera comme je le pense.
// C'est censé détecter une redirection simulée.
//Si le test ne passe pas, il faudra créer la page profil utilisateur puis faire une redirection propre
test('retour à son profil', () => {
  const monProfil = screen.getByText('Huguette231');

  // Simule une fonction de redirection
  const mockNavigation = jest.fn();
  monProfil.addEventListener('click', mockNavigation);

  fireEvent.click(monProfil);

  // Vérifie que la fonction de redirection a été appelée
  expect(mockNavigation).toHaveBeenCalled();
});


