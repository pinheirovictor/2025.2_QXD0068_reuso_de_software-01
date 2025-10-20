# ============================================
# Padrão de Projeto: FACADE (Fachada)
# ============================================
# Tipo: Estrutural
#
# Objetivo:
# Fornecer uma interface simples e unificada para um sistema complexo
# de classes, bibliotecas ou frameworks. 
# A Fachada oculta a complexidade interna e expõe apenas o necessário
# para o cliente, reduzindo o acoplamento e melhorando a clareza do código.

from __future__ import annotations


# =====================================================
# Classe Fachada
# =====================================================
class Fachada:
    """
    A classe Fachada oferece uma interface simples para a lógica complexa
    de um ou mais subsistemas.
    Ela delega as solicitações do cliente para os objetos apropriados
    dentro desses subsistemas e também pode gerenciar seu ciclo de vida.
    """

    def __init__(self, subsistema1: Subsistema1, subsistema2: Subsistema2) -> None:
        """
        Dependendo das necessidades da aplicação, a Fachada pode receber
        instâncias já existentes dos subsistemas ou criar novas internamente.
        """
        self._subsistema1 = subsistema1 or Subsistema1()
        self._subsistema2 = subsistema2 or Subsistema2()

    def operacao(self) -> str:
        """
        O método da Fachada atua como um atalho conveniente para a funcionalidade
        mais complexa dos subsistemas. O cliente acessa apenas uma parte simplificada
        das capacidades reais do sistema.
        """
        resultados = []
        resultados.append("Fachada inicializa os subsistemas:")
        resultados.append(self._subsistema1.operacao1())
        resultados.append(self._subsistema2.operacao1())
        resultados.append("Fachada solicita aos subsistemas que executem ações:")
        resultados.append(self._subsistema1.operacao_n())
        resultados.append(self._subsistema2.operacao_z())
        return "\n".join(resultados)


# =====================================================
# Subsistema 1
# =====================================================
class Subsistema1:
    """
    O Subsistema pode aceitar requisições tanto da Fachada quanto diretamente
    do cliente. Para o Subsistema, a Fachada é apenas mais um cliente.
    """

    def operacao1(self) -> str:
        return "Subsistema1: Pronto!"

    def operacao_n(self) -> str:
        return "Subsistema1: Executando ação!"


# =====================================================
# Subsistema 2
# =====================================================
class Subsistema2:
    """
    Algumas Fachadas podem coordenar múltiplos subsistemas simultaneamente.
    """

    def operacao1(self) -> str:
        return "Subsistema2: Preparando-se!"

    def operacao_z(self) -> str:
        return "Subsistema2: Ação concluída!"


# =====================================================
# Código do Cliente
# =====================================================
def codigo_cliente(fachada: Fachada) -> None:
    """
    O código cliente interage com o sistema complexo através da interface simples
    fornecida pela Fachada.
    Assim, o cliente pode executar operações sem conhecer os detalhes internos
    dos subsistemas.
    """
    print(fachada.operacao(), end="")


# =====================================================
# Execução Principal
# =====================================================
if __name__ == "__main__":
    # O cliente pode já ter instâncias dos subsistemas criadas.
    # Nesse caso, ele pode passá-las à Fachada, em vez de deixá-la criar novas.
    subsistema1 = Subsistema1()
    subsistema2 = Subsistema2()
    fachada = Fachada(subsistema1, subsistema2)

    # O cliente faz tudo através da interface unificada da Fachada.
    codigo_cliente(fachada)



# Fachada (Facade) — é a classe principal que oferece uma interface única e simples, escondendo a complexidade de vários componentes.

# Subsistemas — são as partes internas complexas do sistema. Cada um tem suas próprias responsabilidades e métodos específicos.

# Cliente — interage apenas com a Fachada, sem saber como os subsistemas realmente funcionam.

# 🏫 Dica pedagógica para aplicar em sala

# Use a analogia de “atendimento bancário”:

# O cliente (usuário) fala com o atendente (Fachada), que internamente lida com o caixa, o gerente e o sistema central (Subsistemas).
# O cliente não precisa conhecer o funcionamento interno do banco.