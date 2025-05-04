let stompClient = null;

async function login() {
  const username = document.getElementById("usernameInput").value;
  const password = document.getElementById("passwordInput").value;

  const response = await fetch('http://localhost:8080/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ userName: username, password: password }),
    credentials: 'include' // Envia e mantém o cookie JSESSIONID
  });

  if (response.ok) {
    const user = await response.json();
    localStorage.setItem('userId', user.id);
    console.log("Login bem-sucedido. Conectando WebSocket...");
    connect(); // conecta o WebSocket após login
  } else {
    console.error("Erro ao fazer login.");
  }
}

function connect() {
  const socket = new SockJS('http://localhost:8080/ws'); // endpoint websocket
  stompClient = Stomp.over(socket);

  // Opcional: remove logs do console

  stompClient.connect({}, function (frame) {
    console.log("Conectado: " + frame);

    // Subscrição para mensagens públicas

    // Subscrição para mensagens privadas
    const userId = localStorage.getItem('userId');
    stompClient.subscribe(`/user/queue/messages`, function (message) {
      console.log("Mensagem privada:", JSON.parse(message.body));
    });

  }, function (error) {
    console.error("Erro de conexão WebSocket:", error);
  });
}

function sendMessage(){
    messageInput = document.getElementById("messageInput").value;
    senderId = localStorage.getItem('userId');
    recipientId = document.getElementById("recipientId").value;

    stompClient.send("/app/chat.private", {}, JSON.stringify({
        senderId: senderId,
        recipientId: recipientId,
        content: messageInput
    }));

}