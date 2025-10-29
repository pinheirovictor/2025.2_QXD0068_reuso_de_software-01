from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    """Classe base que define operações comuns para objetos simples e compostos."""

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """Define ou acessa o componente pai na estrutura de árvore."""
        self._parent = parent

    def add(self, component: Component) -> None:
        """Adiciona um componente filho (implementado apenas em classes compostas)."""
        pass

    def remove(self, component: Component) -> None:
        """Remove um componente filho (implementado apenas em classes compostas)."""
        pass

    def is_composite(self) -> bool:
        """Indica se o componente pode conter outros filhos."""
        return False

    @abstractmethod
    def operation(self) -> str:
        """Define uma operação que pode ser executada de forma uniforme por folhas e compostos."""
        pass


class Leaf(Component):
    """Classe Folha: representa objetos finais da composição que não têm filhos."""

    def operation(self) -> str:
        return "Folha"


class Composite(Component):
    """Classe Composite: representa objetos complexos que podem ter filhos."""

    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """Executa operações recursivas em todos os filhos e agrega os resultados."""
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Galho({'+'.join(results)})"


def client_code(component: Component) -> None:
    """O código cliente trabalha com todos os componentes via a interface base."""
    print(f"RESULTADO: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Graças ao fato de que as operações de gerenciamento de filhos estão declaradas
    na classe base, o código cliente pode trabalhar com qualquer componente
    (simples ou composto) sem depender de suas classes concretas.
    """
    if component1.is_composite():
        component1.add(component2)
    print(f"RESULTADO: {component1.operation()}", end="")


if __name__ == "__main__":
    # O cliente pode trabalhar com componentes simples...
    simples = Leaf()
    print("Cliente: Tenho um componente simples:")
    client_code(simples)
    print("\n")

    # ...assim como com composições complexas.
    arvore = Composite()

    galho1 = Composite()
    galho1.add(Leaf())
    galho1.add(Leaf())

    galho2 = Composite()
    galho2.add(Leaf())

    arvore.add(galho1)
    arvore.add(galho2)

    print("Cliente: Agora tenho uma árvore composta:")
    client_code(arvore)
    print("\n")

    print("Cliente: Não preciso verificar as classes ao manipular a árvore:")
    client_code2(arvore, simples)
