from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from enum import Enum

class Produto(ABC):
    def __init__(self, nome: str, preco_base: float):
        self.nome = nome
        self.preco_base = preco_base
    
    @abstractmethod
    def preparo(self) -> str:
        pass
    
    def __str__(self):
        return f"{self.nome} - R$ {self.preco_base:.2f}"

class CafeLatte(Produto):
    def __init__(self):
        super().__init__("Café Latte", 8.50)
    
    def preparo(self) -> str:
        return "Preparar café expresso, adicionar leite vaporizado e finalizar com espuma"


class ChaVerde(Produto):
    def __init__(self):
        super().__init__("Chá Verde", 5.00)
    
    def preparo(self) -> str:
        return "Infusionar folhas de chá verde em água a 80°C por 3 minutos"


class CafeExpresso(Produto):
    def __init__(self):
        super().__init__("Café Expresso", 4.50)
    
    def preparo(self) -> str:
        return "Extrair café expresso duplo em xícara pré-aquecida"


class Cappuccino(Produto):
    def __init__(self):
        super().__init__("Cappuccino", 7.50)
    
    def preparo(self) -> str:
        return "Preparar café expresso, adicionar leite vaporizado e cobrir com espuma densa"

class Brownie(Produto):
    def __init__(self):
        super().__init__("Brownie", 6.00)
    
    def preparo(self) -> str:
        return "Aquecer brownie por 30 segundos no micro-ondas e servir com sorvete"

class Croissant(Produto):
    def __init__(self):
        super().__init__("Croissant", 5.50)
    
    def preparo(self) -> str:
        return "Aquecer croissant no forno por 3 minutos até ficar crocante"

class Bolo(Produto):
    def __init__(self):
        super().__init__("Fatia de Bolo", 7.00)
    
    def preparo(self) -> str:
        return "Cortar fatia generosa e servir em prato de sobremesa"

class FabricaProduto:
    _produtos = {
        "cafe_latte": CafeLatte,
        "cha_verde": ChaVerde,
        "cafe_expresso": CafeExpresso,
        "cappuccino": Cappuccino,
        "brownie": Brownie,
        "croissant": Croissant,
        "bolo": Bolo
    }
    
    @classmethod
    def fabrica_produto(cls, tipo: str) -> Produto:
        produto_class = cls._produtos.get(tipo.lower())
        if produto_class:
            return produto_class()
        else:
            raise ValueError(f"Tipo de produto '{tipo}' não encontrado")
    
    @classmethod
    def produtos_disponiveis(cls) -> List[str]:
        """Retorna lista de produtos disponíveis"""
        return list(cls._produtos.keys())

class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular_desconto(self, valor_total: float, produtos: List[Produto]) -> float:
        pass
    
    @abstractmethod
    def descricao(self) -> str:
        pass


class DescontoClienteFrequente(EstrategiaDesconto):
    def __init__(self, valor_fixo: float = 5.00):
        self.valor_fixo = valor_fixo
    
    def calcular_desconto(self, valor_total: float, produtos: List[Produto]) -> float:
        return self.valor_fixo
    
    def descricao(self) -> str:
        return f"Cliente Frequente - R$ {self.valor_fixo:.2f} de desconto"


class PromocaoDoDia(EstrategiaDesconto):
    def __init__(self, tipo_promocao: str = "bebidas", percentual: float = 0.15):
        self.tipo_promocao = tipo_promocao.lower()
        self.percentual = percentual
    
    def calcular_desconto(self, valor_total: float, produtos: List[Produto]) -> float:
        valor_desconto = 0.0
        bebidas = ["CafeLatte", "ChaVerde", "CafeExpresso", "Cappuccino"]
        comidas = ["Brownie", "Croissant", "Bolo"]
        
        produtos_promocao = bebidas if self.tipo_promocao == "bebidas" else comidas
        
        for produto in produtos:
            if produto.__class__.__name__ in produtos_promocao:
                valor_desconto += produto.preco_base * self.percentual
        
        return valor_desconto
    
    def descricao(self) -> str:
        return f"Promoção do Dia - {self.percentual*100:.0f}% em {self.tipo_promocao}"


class CupomPersonalizado(EstrategiaDesconto):
    def __init__(self, percentual: float):
        self.percentual = percentual / 100 if percentual > 1 else percentual
    
    def calcular_desconto(self, valor_total: float, produtos: List[Produto]) -> float:
        return valor_total * self.percentual
    
    def descricao(self) -> str:
        return f"Cupom Personalizado - {self.percentual*100:.0f}% de desconto"

class Observer(ABC):
    @abstractmethod
    def notificar(self, pedido):
        pass


class NotificadorCliente(Observer):
    def notificar(self, pedido):
        print(f"\nNOTIFICAÇÃO CLIENTE:")
        print(f"Pedido #{pedido.numero} confirmado!")
        print(f"Total: R$ {pedido.valor_final:.2f}")
        print(f"Tempo estimado: {len(pedido.produtos) * 5} minutos")
        print("Obrigado pela preferência! ☕")


class NotificadorCozinha(Observer):
    def notificar(self, pedido):
        print(f"\nNOTIFICAÇÃO COZINHA:")
        print(f"Novo pedido #{pedido.numero} - Preparar:")
        for i, produto in enumerate(pedido.produtos, 1):
            print(f"{i}. {produto.nome}")
            print(f"   Preparo: {produto.preparo()}")


class LoggerSistema(Observer):
    def __init__(self):
        self.historico = []
    
    def notificar(self, pedido):
        registro = {
            "numero": pedido.numero,
            "produtos": [p.nome for p in pedido.produtos],
            "valor_total": pedido.valor_total,
            "desconto": pedido.valor_desconto,
            "valor_final": pedido.valor_final,
            "estrategia_desconto": pedido.estrategia_desconto.descricao() if pedido.estrategia_desconto else "Nenhuma"
        }
        self.historico.append(registro)
        
        print(f"\nLOG SISTEMA:")
        print(f"Pedido #{pedido.numero} registrado no histórico")
        print(f"Total de pedidos: {len(self.historico)}")
    
    def exibir_historico(self):
        print(f"\nHISTÓRICO DE PEDIDOS ({len(self.historico)} pedidos):")
        for registro in self.historico:
            print(f"Pedido #{registro['numero']} - R$ {registro['valor_final']:.2f}")


class Pedido:
    _contador_pedidos = 1
    
    def __init__(self):
        self.numero = Pedido._contador_pedidos
        Pedido._contador_pedidos += 1
        
        self.produtos: List[Produto] = []
        self.estrategia_desconto: Optional[EstrategiaDesconto] = None
        self.observadores: List[Observer] = []
        
        self.valor_total = 0.0
        self.valor_desconto = 0.0
        self.valor_final = 0.0
    
    def adicionar_produto(self, tipo_produto: str):
        try:
            produto = FabricaProduto.fabrica_produto(tipo_produto)
            self.produtos.append(produto)
            print(f"{produto.nome} adicionado ao pedido")
        except ValueError as e:
            print(f"Erro: {e}")
    
    def definir_estrategia_desconto(self, estrategia: EstrategiaDesconto):
        self.estrategia_desconto = estrategia
        print(f"Estratégia de desconto aplicada: {estrategia.descricao()}")
    
    def adicionar_observador(self, observador: Observer):
        self.observadores.append(observador)
    
    def remover_observador(self, observador: Observer):
        if observador in self.observadores:
            self.observadores.remove(observador)
    
    def notificar_observadores(self):
        for observador in self.observadores:
            observador.notificar(self)
    
    def calcular_totais(self):
        self.valor_total = sum(produto.preco_base for produto in self.produtos)
        
        if self.estrategia_desconto:
            self.valor_desconto = self.estrategia_desconto.calcular_desconto(
                self.valor_total, self.produtos
            )
        else:
            self.valor_desconto = 0.0
        
        self.valor_final = max(0, self.valor_total - self.valor_desconto)
    
    def finalizar_pedido(self):
        if not self.produtos:
            print("Não é possível finalizar um pedido vazio!")
            return
        
        self.calcular_totais()
        
        print(f"\nPEDIDO #{self.numero} FINALIZADO!")
        print("=" * 40)
        
        print("ITENS DO PEDIDO:")
        for i, produto in enumerate(self.produtos, 1):
            print(f"{i}. {produto}")
        
        print(f"\nSubtotal: R$ {self.valor_total:.2f}")
        if self.valor_desconto > 0:
            print(f"Desconto: -R$ {self.valor_desconto:.2f}")
            if self.estrategia_desconto:
                print(f"({self.estrategia_desconto.descricao()})")
        print(f"TOTAL FINAL: R$ {self.valor_final:.2f}")
        
        self.notificar_observadores()

class SistemaCafeteria:
    def __init__(self):
        self.notificador_cliente = NotificadorCliente()
        self.notificador_cozinha = NotificadorCozinha()
        self.logger_sistema = LoggerSistema()
        
        self.pedido_atual = None
    
    def novo_pedido(self):
        self.pedido_atual = Pedido()
        
        self.pedido_atual.adicionar_observador(self.notificador_cliente)
        self.pedido_atual.adicionar_observador(self.notificador_cozinha)
        self.pedido_atual.adicionar_observador(self.logger_sistema)
        
        print(f"\nNovo pedido iniciado - Pedido #{self.pedido_atual.numero}")
        return self.pedido_atual
    
    def exibir_cardapio(self):
        print("\nCARDÁPIO DA CAFETERIA")
        print("=" * 30)
        
        produtos_exemplo = {}
        for tipo in FabricaProduto.produtos_disponiveis():
            try:
                produto = FabricaProduto.fabrica_produto(tipo)
                produtos_exemplo[tipo] = produto
            except:
                continue
        
        print("BEBIDAS:")
        bebidas = ["cafe_latte", "cha_verde", "cafe_expresso", "cappuccino"]
        for tipo in bebidas:
            if tipo in produtos_exemplo:
                print(f"  • {produtos_exemplo[tipo]}")
        
        print("\nCOMIDAS:")
        comidas = ["brownie", "croissant", "bolo"]
        for tipo in comidas:
            if tipo in produtos_exemplo:
                print(f"  • {produtos_exemplo[tipo]}")
    
    def exibir_promocoes(self):
        print("\nPROMOÇÕES DISPONÍVEIS:")
        print("1. Cliente Frequente - R$ 5,00 de desconto")
        print("2. Promoção Bebidas - 15% em todas as bebidas")
        print("3. Promoção Comidas - 15% em todas as comidas")
        print("4. Cupom Personalizado - Desconto customizado")
    
    def aplicar_promocao(self, opcao: int, cupom_percentual: Optional[float] = None):
        if not self.pedido_atual:
            print("Nenhum pedido ativo!")
            return
        
        estrategias = {
            1: DescontoClienteFrequente(),
            2: PromocaoDoDia("bebidas", 0.15),
            3: PromocaoDoDia("comidas", 0.15),
            4: CupomPersonalizado(cupom_percentual if cupom_percentual is not None else 10.0)
        }
        
        if opcao in estrategias:
            self.pedido_atual.definir_estrategia_desconto(estrategias[opcao])
        else:
            print("Opção de promoção inválida!")
    
    def exibir_historico(self):
        self.logger_sistema.exibir_historico()


def demonstracao_sistema():
    print("SISTEMA DE PEDIDOS - CAFETERIA ARTESANAL")
    print("=" * 50)
    
    sistema = SistemaCafeteria()
    
    sistema.exibir_cardapio()
    
    print("\n" + "="*50)
    print("TESTE 1: Pedido com desconto de cliente frequente")
    print("="*50)
    
    pedido1 = sistema.novo_pedido()
    pedido1.adicionar_produto("cafe_latte")
    pedido1.adicionar_produto("brownie")
    
    sistema.exibir_promocoes()
    sistema.aplicar_promocao(1)  # Cliente frequente
    
    pedido1.finalizar_pedido()
    
    print("\n" + "="*50)
    print("TESTE 2: Pedido com promoção de bebidas")
    print("="*50)
    
    pedido2 = sistema.novo_pedido()
    pedido2.adicionar_produto("cappuccino")
    pedido2.adicionar_produto("cafe_expresso")
    pedido2.adicionar_produto("croissant")
    
    sistema.aplicar_promocao(2)  # Promoção bebidas
    
    pedido2.finalizar_pedido()
    
    print("\n" + "="*50)
    print("TESTE 3: Pedido com cupom personalizado")
    print("="*50)
    
    pedido3 = sistema.novo_pedido()
    pedido3.adicionar_produto("cha_verde")
    pedido3.adicionar_produto("bolo")
    
    sistema.aplicar_promocao(4, 20)  # Cupom 20%
    
    pedido3.finalizar_pedido()
    
    print("\n" + "="*50)
    print("TESTE 4: Pedido sem desconto")
    print("="*50)
    
    pedido4 = sistema.novo_pedido()
    pedido4.adicionar_produto("cafe_latte")
    pedido4.adicionar_produto("cappuccino")
    
    pedido4.finalizar_pedido()
    
    print("\n" + "="*50)
    sistema.exibir_historico()


if __name__ == "__main__":
    demonstracao_sistema() 