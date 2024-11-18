import socket, json

class Client:
    """ 
    Класс клиент для подключения к серверу
    """
    def __init__(self) -> socket:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключение
    def connect(self, ip: str, port: int, request: str) -> list:
        """ 
        Mетод подключения, который возврощает список с информацией
        """
        self.client.connect((ip, port))
        self.send(request)
        return (json.loads(self.client.recv(1024).decode("utf-8")))

    # Оотправка
    def send(self, text) -> None:
        """ 
        Метод для отправки сообщения 
        """
        self.client.send(text.encode('utf-8'))       
        
