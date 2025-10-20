from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# ============================================================
# OBJETIVO DO EXEMPLO
# ============================================================
# Imagine que temos uma aplicação que precisa ordenar dados.
# Em alguns casos, queremos ordenar em ordem crescente,
# em outros, em ordem decrescente.
# 
# Sem o padrão Strategy, precisaríamos:
#   - colocar if/else dentro do método de ordenação;
#   - duplicar código;
#   - ou alterar a classe principal toda vez que quisermos
#     mudar a forma de ordenar.
#
# O Padrão Strategy resolve esse problema ao permitir
# trocar o "comportamento" (a estratégia) dinamicamente,
# sem modificar o contexto que usa esse comportamento.
# ============================================================


class Contexto:
    """
    A classe Contexto é quem usa o algoritmo, mas não o implementa.
    Ela delega a execução para uma Estratégia.
    """

    def __init__(self, estrategia: Estrategia) -> None:
        """
        O Contexto recebe uma estratégia inicial (por exemplo, ordenação normal).
        Essa estratégia pode ser trocada depois, sem alterar o código do Contexto.
        """
        self._estrategia = estrategia

    @property
    def estrategia(self) -> Estrategia:
        """
        Retorna a estratégia atualmente em uso.
        Isso permite que o cliente saiba qual comportamento está ativo.
        """
        return self._estrategia

    @estrategia.setter
    def estrategia(self, estrategia: Estrategia) -> None:
        """
        Permite trocar a estratégia em tempo de execução.
        Por exemplo: passar de ordenação crescente para decrescente.
        """
        self._estrategia = estrategia

    def executar_logica_de_negocio(self) -> None:
        """
        Aqui está o ponto principal: o Contexto delega o trabalho
        para o objeto Estratégia.
        
        O Contexto não precisa saber COMO a estratégia faz o trabalho —
        apenas que ela tem o método 'executar_algoritmo'.
        """
        print("Contexto: Ordenando dados usando a estratégia (sem saber como ela faz isso)")
        resultado = self._estrategia.executar_algoritmo(["a", "b", "c", "d", "e"])
        print(",".join(resultado))
        print()  # Apenas para deixar a saída visualmente separada


# ============================================================
# INTERFACE ESTRATÉGIA
# ============================================================
# Define a estrutura comum para todas as estratégias possíveis.
# Assim, o Contexto pode chamar o mesmo método, independente
# da estratégia concreta utilizada.
# ============================================================

class Estrategia(ABC):
    """
    A interface base define o contrato que todas as estratégias devem seguir.
    Isso garante que o Contexto possa trabalhar com qualquer uma delas.
    """

    @abstractmethod
    def executar_algoritmo(self, dados: List):
        """
        Método que será implementado de formas diferentes nas subclasses.
        """
        pass


# ============================================================
# ESTRATÉGIAS CONCRETAS
# ============================================================
# Cada classe representa uma forma diferente de executar o algoritmo.
# Ambas implementam a interface 'Estrategia', o que as torna intercambiáveis.
# ============================================================

class EstrategiaConcretaA(Estrategia):
    def executar_algoritmo(self, dados: List) -> List:
        """
        Estratégia A: Ordenação normal (crescente).
        """
        return sorted(dados)

class EstrategiaConcretaB(Estrategia):
    def executar_algoritmo(self, dados: List) -> List:
        """
        Estratégia B: Ordenação invertida (decrescente).
        """
        return reversed(sorted(dados))


# ============================================================
# CÓDIGO CLIENTE
# ============================================================
# Aqui demonstramos o uso do padrão.
# O cliente cria o Contexto e escolhe qual Estratégia usar.
# ============================================================

if __name__ == "__main__":
    # Inicialmente usamos a Estratégia A (ordenação normal)
    contexto = Contexto(EstrategiaConcretaA())
    print("Cliente: Estratégia definida para ordenação normal.")
    contexto.executar_logica_de_negocio()

    # Depois, trocamos a estratégia para ordenação reversa
    print("Cliente: Estratégia alterada para ordenação reversa.")
    contexto.estrategia = EstrategiaConcretaB()
    contexto.executar_logica_de_negocio()



# ============================================================
# RESUMO DIDÁTICO
# ============================================================
# Problema:
#   - Precisamos de múltiplas variações de um algoritmo (ordenar de jeitos diferentes).
#   - Não queremos usar vários "if/else" nem duplicar código no Contexto.
#
# Solução:
#   - Criar uma interface comum (Estrategia) e várias classes concretas com comportamentos diferentes.
#   - O Contexto delega o trabalho à Estratégia sem saber detalhes de implementação.
#   - Podemos trocar a estratégia em tempo de execução.
#
# Benefícios:
#   - Reduz acoplamento entre Contexto e as variações do algoritmo.
#   - Facilita a extensão (novas estratégias sem alterar o código existente).
#   - Demonstra o Princípio Aberto/Fechado (OCP) e composição sobre herança.
#
# Conclusão:
#   - O padrão Strategy é ideal quando você quer definir uma família de algoritmos,
#     encapsulá-los e torná-los intercambiáveis.
# ============================================================


