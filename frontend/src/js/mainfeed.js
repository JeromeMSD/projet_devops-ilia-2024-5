document.addEventListener("DOMContentLoaded", () => {
  const tweets = document.querySelectorAll(".tweet");
  tweets.forEach((tweet) => {
    tweet.addEventListener("click", () => {
      window.location.href = "./conversations.html";
    });
  });
});
