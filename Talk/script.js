let stompClient;

async function login() {
    const username = document.getElementById("usernameInput").value;
    const password = document.getElementById("passwordInput").value;

    const response = await fetch('http://localhost:8080/api/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({userName: username, password: password}),
        credentials: 'include'
    });

    if (response.ok) {
        console.log('Login feito com sucesso!');
        const user = await response.json(); // Assume que o backend retorna o usuário logado
        localStorage.setItem('userId', user.id); // Armazena o id do usuário
        connect(); // Só conecta depois do login
    } else {
        console.error('Erro ao fazer login');
    }
}

function connect() {
    const socket = new SockJS('http://localhost:8080/ws');
    stompClient = Stomp.over(socket);
    stompClient.connect({}, function (frame) {
        console.log('Conectado: ' + frame);
        stompClient.subscribe('/user/queue/messages', function (message) {
            console.log(message.body);  
        });
    });
}

function sendMessage() {
    const contentMessage = document.getElementById('messageInput').value;
    const senderId = localStorage.getItem('userId'); // Pega o id do usuário do localStorage
    const recipientId = document.getElementById("recipientId").value;
    stompClient.send("/app/chat.private", {}, JSON.stringify({
        sender: senderId,
        receiver: recipientId,
        content: contentMessage
    }));
}

function showMessage(message) {
    const ul = document.getElementById('messages');
    const li = document.createElement('li');
    li.appendChild(document.createTextNode(message));
    ul.appendChild(li);
}