const fileForm = document.getElementById("file-form");
const messagesContainer = document.getElementById("messages-container");
const lightDarkToggle = document.getElementById("light-dark-button");

const handleFile = function() {
  document.getElementById("file-form").click()
};

fileForm.addEventListener("submit", handleFile);

function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
}

lightDarkToggle.addEventListener('click', toggleDarkMode);