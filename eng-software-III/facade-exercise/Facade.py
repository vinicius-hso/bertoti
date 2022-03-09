from AnotarPedido import AnotarPedido
from PrepararPedido import PrepararPedido
from EntregarPedido import EntregarPedido

class Facade:
    
    def __init__(self, anotar_pedido: AnotarPedido, preparar_pedido: PrepararPedido, entregar_pedido: EntregarPedido) -> None:
        self._anotar_pedido = anotar_pedido or AnotarPedido()
        self._preparar_pedido = preparar_pedido or PrepararPedido()
        self._entregar_pedido = entregar_pedido or EntregarPedido()
        
    def finalizarPedido(self) -> str:
        results = []
        results.append("Facade inicializando os subsistemas:")
        results.append(self._anotar_pedido.pedido())
        results.append(self._preparar_pedido.preparo())
        results.append(self._entregar_pedido.entrega())
        results.append("Pedido entregue!\n")
        return "\n".join(results)
       