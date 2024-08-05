""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """

    def agregar_usuarios_ingresados(self, entrada: dict):
        query = f"""
            INSERT INTO public.datos_usuarios(nombre, contrasena)
            VALUES ('{entrada.get('username')}', '{entrada.get('password')}');
        """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)