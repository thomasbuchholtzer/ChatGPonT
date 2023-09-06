const fileForm = document.getElementById("file-form");
const submitFileButton = document.getElementById("submit-file-button");
const messagesContainer = document.getElementById("messages-container");
const lightDarkToggle = document.getElementById("light-dark-button");

const appendHumanMessage = (message) => {
    const humanMessageElement = document.createElement("div");
    humanMessageElement.classList.add("message", "message-human");
    humanMessageElement.innerHTML = message;
    messagesContainer.appendChild(humanMessageElement);
  };
  
const appendAIMessage = async (messagePromise) => {
  // Add a loader to the interface
  const loaderElement = document.createElement("div");
  loaderElement.classList.add("message");
  loaderElement.innerHTML =
    "<div class='loader'><div></div><div></div><div></div>";
  messagesContainer.appendChild(loaderElement);

  // Await the answer from the server
  const messageToAppend = await messagePromise();

  // Replace the loader with the answer
  loaderElement.classList.remove("loader");
  loaderElement.innerHTML = messageToAppend;
};

const handleFile = async (event) => {
  event.preventDefault();
  // Parse form data in a structured object
  const data = new FormData(event.target);
  fileForm.reset();

  let url = "/new_course";

  appendHumanMessage(data.get("file"));

  await appendAIMessage(async () => {
    const response = await fetch(url, {
      method: "POST",
      body: data,
    });
    const result = await response.json();
    return result.answer;
  });
};

fileForm.addEventListener("submit", handleFile);

function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
}

lightDarkToggle.addEventListener('click', toggleDarkMode);