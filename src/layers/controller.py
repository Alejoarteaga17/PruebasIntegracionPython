
from .service import UserService

class UserController:
    def __init__(self, service: UserService):
        self.service = service

    # Simula un controlador sin servidor web
    def get_user_full_name(self, user_id: int) -> str:
        full = self.service.get_full_name(user_id)
        return "404 NOT_FOUND" if full is None else full

'''
4) Si cambias el formato de salida del controlador, ¿qué otras capas tendrías que adaptar?
si se cambia el formato de salida del controlador lo primero que hay que adaptar es todo lo que consume
ese controlador, en este caso el test, pero también cualquier otro componente que dependa de ese formato de salida. 
Por ejemplo, si el controlador ahora devuelve un diccionario con más información en lugar de solo el nombre completo, 
entonces el test y cualquier otro código que utilice ese controlador tendría que ser actualizado para manejar el nuevo formato de salida.
'''
