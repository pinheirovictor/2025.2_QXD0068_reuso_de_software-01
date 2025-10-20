from __future__ import annotations
from abc import ABC, abstractmethod

# ============================================================
# OBJETIVO DO EXEMPLO
# ============================================================
# Imagine que sua aplicação precisa criar objetos de tipos diferentes,
# como ProdutoConcreto1 e ProdutoConcreto2.
#
# Um código sem o padrão Factory Method usaria vários "if/else":
#   if tipo == "A": return ProdutoConcreto1()
#   else: return ProdutoConcreto2()
#
# Isso gera alto acoplamento — o código cliente conhece todas as
# classes concretas e precisa ser modificado sempre que um novo
# produto for adicionado.
#
# O padrão Factory Method resolve isso ao delegar a criação dos
# objetos para subclasses, mantendo o código cliente independente
# das classes concretas.
# ============================================================


class Criador(ABC):
    """
    A classe Criador define a interface do método fábrica.
    Ela não cria o produto diretamente — quem faz isso são
    as subclasses concretas.
    """

    @abstractmethod
    def metodo_fabrica(self):
        """
        Este método é uma 'assinatura' (contrato) que as subclasses
        devem implementar para retornar um objeto do tipo Produto.
        """
        pass

    def alguma_operacao(self) -> str:
        """
        Apesar do nome, a principal função do Criador não é apenas
        fabricar objetos — ele também define uma lógica de negócio
        que depende do produto criado.
        
        A ideia é: o Criador executa um processo geral, mas o tipo
        exato do produto (a classe concreta) é decidido por quem
        o herda.
        """

        # Cria um produto chamando o método fábrica.
        produto = self.metodo_fabrica()

        # Usa o produto criado sem saber sua classe concreta.
        resultado = f"Criador: O mesmo código do criador acabou de funcionar com {produto.operacao()}"

        return resultado


# ============================================================
# CRIADORES CONCRETOS
# ============================================================
# As subclasses de Criador implementam o método fábrica,
# decidindo qual tipo concreto de Produto será criado.
# ============================================================

class CriadorConcreto1(Criador):
    """
    Este criador retorna instâncias de ProdutoConcreto1.
    Note que o tipo de retorno ainda é o tipo abstrato Produto —
    isso mantém o Criador desacoplado de implementações concretas.
    """

    def metodo_fabrica(self) -> Produto:
        return ProdutoConcreto1()


class CriadorConcreto2(Criador):
    """
    Este criador retorna instâncias de ProdutoConcreto2.
    """
    def metodo_fabrica(self) -> Produto:
        return ProdutoConcreto2()


# ============================================================
# PRODUTO ABSTRATO
# ============================================================
# Define a interface comum a todos os produtos.
# Assim, o cliente pode usar qualquer produto sem conhecer sua classe.
# ============================================================

class Produto(ABC):
    """
    Interface base que declara a operação que todos os produtos devem implementar.
    """

    @abstractmethod
    def operacao(self) -> str:
        pass


# ============================================================
# PRODUTOS CONCRETOS
# ============================================================
# Implementam a interface Produto de formas diferentes.
# São as classes efetivamente instanciadas pelos Criadores.
# ============================================================

class ProdutoConcreto1(Produto):
    def operacao(self) -> str:
        """
        Implementação específica do ProdutoConcreto1.
        """
        return "{Resultado do ProdutoConcreto1}"


class ProdutoConcreto2(Produto):
    def operacao(self) -> str:
        """
        Implementação específica do ProdutoConcreto2.
        """
        return "{Resultado do ProdutoConcreto2}"


# ============================================================
# CÓDIGO CLIENTE
# ============================================================
# O cliente trabalha com o tipo abstrato Criador.
# Ele não sabe (nem precisa saber) qual classe concreta está sendo usada.
# ============================================================

def codigo_cliente(criador: Criador) -> None:
    """
    O cliente pode usar qualquer criador concreto,
    desde que ele siga a interface Criador.
    """
    print(f"Cliente: Não sei a classe exata do criador, mas ainda assim funciona.\n"
          f"{criador.alguma_operacao()}", end="")


# ============================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================
# O código cliente alterna entre criadores diferentes.
# Cada criador fabrica um produto diferente, sem alterar o código do cliente.
# ============================================================

if __name__ == "__main__":
    print("Aplicação: Iniciada com o CriadorConcreto1.")
    codigo_cliente(CriadorConcreto1())
    print("\n")

    print("Aplicação: Iniciada com o CriadorConcreto2.")
    codigo_cliente(CriadorConcreto2())


# ============================================================
# RESUMO DIDÁTICO
# ============================================================
# Problema:
#   - O cliente precisa criar objetos diferentes (produtos),
#     mas não queremos usar if/else nem depender de classes concretas.
#
# Solução:
#   - O padrão Factory Method delega a criação dos objetos para subclasses.
#   - Cada subclasse define qual produto concreto será criado.
#   - O cliente usa apenas a interface genérica (Criador e Produto).
#
# Benefícios:
#   - Reduz acoplamento entre o cliente e as classes concretas.
#   - Facilita a extensão (novos produtos → novas subclasses).
#   - Mantém o código cliente inalterado.
#
# Princípios demonstrados:
#   - Aberto/Fechado (OCP): novas fábricas e produtos sem mudar o cliente.
#   - Inversão de Dependência: o código depende de abstrações, não de implementações.
#
# Demonstração:
#   - Tente trocar "CriadorConcreto1()" por "CriadorConcreto2()".
#   - Veja que o resultado muda, mas o código do cliente permanece o mesmo.
# ============================================================


