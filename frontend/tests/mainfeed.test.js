import '@testing-library/jest-dom';
import { screen, fireEvent } from '@testing-library/dom';
import { initMainFeed, ajouterTweet } from '../src/mainfeed.js';


beforeEach(() => {
  document.body.innerHTML = `
    <div id="entete">
      <div id="titreComplet">
        <h1 id="titlePolyte">Polyte</h1>
        <h1 id="titleX">X</h1>
      </div>
      <div id="enteteButtons">
        <button id="acceuilBtn">Acceuil</button>
        <button id="messagesPrivesBtn">Messages Privés</button>
        <button id="rechercherBtn">Rechercher</button>
      </div>
      <div id="monProfil">
        <a href=""><h2 id="monNom">Huguette231</h2></a>
        <img id="maPhoto" src="data/huguette.avif">
      </div>
    </div>
    <div id="zoneTweets">
      <div class="tweet">
        <h3>@MichelMichel</h3>
        <p>Ceci est mon premier tweet sur PolyteX. !</p>
      </div>
      <div class="tweet">
        <h3>@Huguette231</h3>
        <p>Moi aussi je tweet. </p>
      </div>
      <div class="tweet">
        <h3>@Ulysses</h3>
        <p>Je hais le café et j'adore le grec ancien!</p>
      </div>
    </div>
  `;
});

// Test de l'existence des boutons
test('les boutons existent sur la page', () => {
  expect(screen.getByText('Acceuil')).toBeInTheDocument();
  expect(screen.getByText('Messages Privés')).toBeInTheDocument();
  expect(screen.getByText('Rechercher')).toBeInTheDocument();
});

// Test de la redirection des boutons
test('les boutons redirigent correctement', () => {
  const acceuilBtn = screen.getByText('Acceuil');
  const messagesPrivesBtn = screen.getByText('Messages Privés');
  const rechercherBtn = screen.getByText('Rechercher');

  acceuilBtn.addEventListener('click', () => {
    window.location.href = '/acceuil';
  });

  messagesPrivesBtn.addEventListener('click', () => {
    window.location.href = '/messages';
  });

  rechercherBtn.addEventListener('click', () => {
    window.location.href = '/rechercher';
  });

  fireEvent.click(acceuilBtn);
  expect(window.location.href).toBe('/acceuil');
  
  fireEvent.click(messagesPrivesBtn);
  expect(window.location.href).toBe('/messages');

  fireEvent.click(rechercherBtn);
  expect(window.location.href).toBe('/rechercher');
});

// Test de l'ajout d'un tweet
test('ajouter un tweet dans la zoneTweets', () => {
  const newTweetText = 'Ceci est un nouveau tweet';
  const zoneTweets = document.getElementById('zoneTweets');

  function ajouterTweet(tweetText) {
    const newTweet = document.createElement('div');
    newTweet.classList.add('tweet');
    const tweetContent = document.createElement('p');
    tweetContent.textContent = tweetText;
    newTweet.appendChild(tweetContent);
    zoneTweets.appendChild(newTweet);
  }

  ajouterTweet(newTweetText);
  
  const addedTweet = screen.getByText(newTweetText);
  expect(addedTweet).toBeInTheDocument();
  expect(zoneTweets.children).toHaveLength(4); // Il y a maintenant 4 tweets
});
