export const chatApp = {
  socket: null,
  url: "ws://localhost:8000/chat",

  init() {
    this.socket = new WebSocket(this.url);

    this.socket.onopen = () => console.log("Conectado!");

    this.socket.onclose = () => {
      console.log("Caiu! Tentando voltar...");
      setTimeout(() => this.init(), 4000);
    };

    this.socket.onmessage = (e) => {
      console.log(e);
      receiveBotMessage(e.data);
    };
  },

  send(msg) {
    console.log(msg);
    if (this.socket && this.socket.readyState === WebSocket.OPEN) {
      const msg_envio = typeof msg === "object" ? JSON.stringify(msg) : msg;
      this.socket.send(msg_envio);
    } else {
      console.error("❌ Erro: O socket não está aberto.");
    }
  },
};

chatApp.init();
