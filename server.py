import socket, json, sqlite3 as sql

class Server:
    """ 
    Класс создает сервер и подключается к БД
    """
    def __init__(self, port: int, database: str) -> socket:
        self.__IP = socket.gethostbyname(socket.gethostname())
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.__IP, port))
        self.server.listen(5)
        self.db = database
        print(f'[Server is run - {self.__IP}:{port}]\n')  
    
    # Запуск   
    def run(self) -> None:
        """ 
        Запуск сервера 
        """
        while True:
            user, addres = self.server.accept()
            print(f'Client connected:\n\tIP: {addres[0]} PORT: {addres[1]}')
            self.__listen(user)

    # Обработка        
    def __listen(self, user) -> None:
        """ 
        Метод обработки пользователей 
        """
        try:
            data = user.recv(1024).decode('utf-8')
        except Exception as e:
            data = None 
            
        connect = sql.connect(self.db)
        cursor = connect.cursor()
        
        try:
            answer = [x for x in cursor.execute(data)]
        except Exception as e:
            answer = e
            
        connect.commit()
        cursor.close()
        connect.close()  
        
        data = json.dumps(answer)
        self.__send(user, data)
    
    # Отправка сообщения
    def __send(self, user, text):
        """ 
        Метод для отправки сообщений 
        """
        user.send(text.encode('utf-8'))       
        
