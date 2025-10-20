# ============================================
# Padrão de Projeto: OBSERVER (Observador)
# ============================================
# Também conhecido como: Assinante (Subscriber), Listener, Event-Subscriber
# Tipo: Comportamental
#
# Objetivo:
# Permitir que um objeto (o Sujeito) notifique automaticamente uma lista de
# outros objetos (Observadores) quando seu estado for alterado,
# sem precisar saber quem são esses objetos ou como eles funcionam.

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


# =====================================================
# Interface do Sujeito (Subject)
# =====================================================
class Sujeito(ABC):
    """
    Define os métodos para gerenciar os observadores (assinantes).
    """

    @abstractmethod
    def adicionar(self, observador: Observador) -> None:
        """Adiciona um observador à lista."""
        pass

    @abstractmethod
    def remover(self, observador: Observador) -> None:
        """Remove um observador da lista."""
        pass

    @abstractmethod
    def notificar(self) -> None:
        """Notifica todos os observadores sobre um evento."""
        pass


# =====================================================
# Sujeito Concreto
# =====================================================
class SujeitoConcreto(Sujeito):
    """
    O Sujeito mantém um estado interno e notifica os observadores
    sempre que esse estado muda.
    """

    _estado: int = None
    _observadores: List[Observador] = []

    def adicionar(self, observador: Observador) -> None:
        print("Sujeito: Observador adicionado.")
        self._observadores.append(observador)

    def remover(self, observador: Observador) -> None:
        self._observadores.remove(observador)
        print("Sujeito: Observador removido.")

    def notificar(self) -> None:
        print("Sujeito: Notificando observadores...")
        for observador in self._observadores:
            observador.atualizar(self)

    def executar_logica_principal(self) -> None:
        """
        Simula alguma operação importante que muda o estado interno.
        Após a mudança, todos os observadores são notificados.
        """
        print("\nSujeito: Executando uma operação importante...")
        self._estado = randrange(0, 10)
        print(f"Sujeito: Meu estado mudou para {self._estado}")
        self.notificar()


# =====================================================
# Interface do Observador
# =====================================================
class Observador(ABC):
    """
    Declara o método de atualização usado pelo sujeito.
    """

    @abstractmethod
    def atualizar(self, sujeito: Sujeito) -> None:
        """Recebe atualizações do sujeito."""
        pass


# =====================================================
# Observadores Concretos
# =====================================================
class ObservadorConcretoA(Observador):
    def atualizar(self, sujeito: Sujeito) -> None:
        if sujeito._estado < 3:
            print("Observador A: Reagiu ao evento (estado menor que 3).")


class ObservadorConcretoB(Observador):
    def atualizar(self, sujeito: Sujeito) -> None:
        if sujeito._estado == 0 or sujeito._estado >= 2:
            print("Observador B: Reagiu ao evento (estado é 0 ou maior/igual a 2).")


# =====================================================
# Código do Cliente
# =====================================================
if __name__ == "__main__":
    sujeito = SujeitoConcreto()

    observador_a = ObservadorConcretoA()
    sujeito.adicionar(observador_a)

    observador_b = ObservadorConcretoB()
    sujeito.adicionar(observador_b)

    sujeito.executar_logica_principal()
    sujeito.executar_logica_principal()

    sujeito.remover(observador_a)

    sujeito.executar_logica_principal()




# Sujeito (Subject): é o objeto que possui um estado e permite que outros se inscrevam para receber atualizações.

# Observador (Observer): define a interface que todos os objetos interessados devem implementar.

# SujeitoConcreto: mantém uma lista de observadores e notifica-os quando o estado muda.

# ObservadoresConcretos: reagem de maneiras diferentes ao mesmo evento.

# Vantagem: baixo acoplamento entre classes — o sujeito não precisa saber o que os observadores fazem.

# Aplicação comum: interfaces gráficas, sistemas de eventos, notificações em tempo real, etc.