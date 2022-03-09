from AnotarPedido import AnotarPedido
from PrepararPedido import PrepararPedido
from EntregarPedido import EntregarPedido
from Facade import Facade
from client_code import client_code
    
if __name__ == "__main__":
    anotar_pedido = AnotarPedido()
    preparar_pedido = PrepararPedido()
    entregar_pedido = EntregarPedido()
    facade = Facade(anotar_pedido, preparar_pedido, entregar_pedido)
    client_code(facade)

