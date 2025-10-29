from __future__ import annotations
from abc import ABC, abstractmethod

# ------------------------
# Interface base Command
# ------------------------
class Command(ABC):
    """A interface Command declara um método para executar um comando."""

    @abstractmethod
    def execute(self) -> None:
        pass


# ------------------------
# Comando simples
# ------------------------
class SimpleCommand(Command):
    """Alguns comandos podem executar operações simples por conta própria."""

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: Veja, posso fazer coisas simples como imprimir ({self._payload})")


# ------------------------
# Comando complexo
# ------------------------
class ComplexCommand(Command):
    """
    Outros comandos podem delegar operações mais complexas para outros objetos,
    chamados de 'receivers' (receptores).
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """Aceita um ou mais receptores e dados de contexto."""
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """Os comandos podem delegar para qualquer método do receptor."""
        print("ComplexCommand: As tarefas complexas devem ser realizadas por um receptor.", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


# ------------------------
# Receptor
# ------------------------
class Receiver:
    """
    A classe Receiver contém a lógica de negócio. Ela sabe como executar as
    operações associadas à solicitação. Qualquer classe pode atuar como receptor.
    """

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Trabalhando em ({a}).", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Também trabalhando em ({b}).", end="")


# ------------------------
# Invocador
# ------------------------
class Invoker:
    """
    O Invoker está associado a um ou mais comandos.
    Ele envia as solicitações aos comandos.
    """

    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        """Configura um comando a ser executado antes da ação principal."""
        self._on_start = command

    def set_on_finish(self, command: Command):
        """Configura um comando a ser executado após a ação principal."""
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        O Invoker não depende de classes concretas de comando ou receptor.
        Ele apenas executa os comandos atribuídos.
        """
        print("Invoker: Alguém quer que eu faça algo antes de começar?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...fazendo algo realmente importante...")

        print("Invoker: Alguém quer que eu faça algo depois de terminar?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


# ------------------------
# Código do cliente
# ------------------------
if __name__ == "__main__":
    """O cliente pode parametrizar o invocador com quaisquer comandos."""
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Dizer Oi!"))

    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Enviar e-mail", "Salvar relatório"))

    invoker.do_something_important()
