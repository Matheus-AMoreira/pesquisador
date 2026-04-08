import { chatApp } from "./socket";

const chat = document.getElementById("chat");
const textInput = document.getElementById("text-box");

textInput.addEventListener("keypress", (event) => {
  if (event.key === "Enter") {
    event.preventDefault();
    sendUserMessage();
  }
});

window.sendUserMessage = function sendUserMessage() {
  const text = textInput.value;

  if (text !== "") {
    chatApp.send(text);

    if (!text.trim()) return;
    createMessageElement(true, text);

    textInput.value = "";
  }
};

window.receiveBotMessage = function receiveBotMessage(content) {
  createMessageElement(false, content);
  scrollToBottom();
};

function createMessageElement(user = false, content = "") {
  if (!chat) return;

  const message = document.createElement("li");
  message.setAttribute("class", user ? "user" : "bot");
  message.setAttribute("data-role", user ? "user" : "bot");

  // Avatar
  const avatar = document.createElement("div");
  avatar.classList.add("avatar");
  avatar.classList.add(user ? "avatar-user" : "avatar-bot");
  avatar.innerHTML = user ? "👤" : "🤖";

  // Conteúdo da mensagem
  const messageContent = document.createElement("div");
  messageContent.classList.add("message-content");

  // Timestamp
  const timestamp = document.createElement("span");
  timestamp.classList.add("timestamp");
  timestamp.textContent = new Date().toLocaleTimeString("pt-BR", {
    hour: "2-digit",
    minute: "2-digit",
  });

  // Texto do conteúdo
  const contentSpan = document.createElement("span");
  contentSpan.classList.add("content");
  contentSpan.textContent = content;

  messageContent.appendChild(timestamp);
  messageContent.appendChild(contentSpan);
  message.appendChild(avatar);
  message.appendChild(messageContent);
  chat.appendChild(message);

  return message;
}

function scrollToBottom() {
  const chatArea = chat;
  if (chatArea) {
    chatArea.scrollTop = chatArea.scrollHeight;
  }
}
