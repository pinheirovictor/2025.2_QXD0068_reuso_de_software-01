from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

# ------------------------
# Interface Builder
# ------------------------
class Builder(ABC):
    """A interface Builder define os métodos para criar as diferentes partes de um produto."""

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


# ------------------------
# Builder concreto
# ------------------------
class ConcreteBuilder1(Builder):
    """
    O Builder concreto implementa a interface Builder e fornece
    a implementação específica das etapas de construção.
    """

    def __init__(self) -> None:
        """Cria uma nova instância de produto limpa para ser montada."""
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Retorna o produto final e reinicia o builder.
        Cada builder pode produzir diferentes tipos de produtos,
        por isso esse método não está na interface base.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("ParteA1")

    def produce_part_b(self) -> None:
        self._product.add("ParteB1")

    def produce_part_c(self) -> None:
        self._product.add("ParteC1")


# ------------------------
# Produto
# ------------------------
class Product1():
    """
    O produto final montado pelo Builder.
    Pode conter partes independentes que precisam ser montadas passo a passo.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes do produto: {', '.join(self.parts)}", end="")


# ------------------------
# Diretor
# ------------------------
class Director:
    """
    O Diretor define a ordem de execução das etapas de construção.
    Ele é útil para criar produtos com diferentes configurações.
    Seu uso é opcional — o cliente pode chamar o builder diretamente.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """Associa um builder ao diretor."""
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        """Constrói um produto básico (mínimo viável)."""
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        """Constrói um produto completo com todos os componentes."""
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


# ------------------------
# Código do cliente
# ------------------------
if __name__ == "__main__":
    """O cliente cria o builder, passa-o ao diretor e inicia o processo de construção."""
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Produto básico padrão:")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Produto completo padrão:")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Também é possível usar o builder sem o diretor.
    print("Produto personalizado:")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
