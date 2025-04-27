let stompClient;

function connect() {
    const socket = new SockJS('http://localhost:8080/ws'); 
    stompClient = Stomp.over(socket);
    stompClient.connect({}, function (frame) {
        console.log('Conectado: ' + frame);
        stompClient.subscribe('/topic/messages', function (message) {
            showMessage(message.body);  
        });
    });
}


function sendMessage() {
    const contentMessage = document.getElementById('messageInput').value;
    const message = { "content": contentMessage };

    stompClient.send("/app/send", {}, JSON.stringify(message));
}

function showMessage(message) {
    const ul = document.getElementById('messages');
    const li = document.createElement('li');
    li.appendChild(document.createTextNode(message));
    ul.appendChild(li);
}

connect();
