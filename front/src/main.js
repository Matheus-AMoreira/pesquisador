import "./style.css";

const ws = "ws://localhost:8000/chat";

let socket = new WebSocket(ws);

socket.onopen = (event) => {
  console.log("Conectado ao servidor FastAPI!");
};

socket.onmessage = (event) => {
  console.log("Mensagem do servidor:", event.data);
  const chat = document.getElementById("chat");
  const message = document.createElement("li");
  const content = document.createTextNode(event.data);
  message.appendChild(content);
  chat.appendChild(message);
};

socket.onerror = (error) => {
  console.error("Erro no WebSocket:", error);
  socket = new WebSocket(ws);
};

socket.onclose = (event) => {
  console.log("Conexão encerrada.");
};

function sendMessage() {
  const text = document.getElementById("text-box");
  console.log("tipo: " + text.type);
  console.log("enviando " + text.value);
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(text.value);
    text.value = "";
  } else {
    console.warn("O socket não está aberto.");
  }
}

window.sendMessage = sendMessage;
