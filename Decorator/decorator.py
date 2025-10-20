# ============================================
# Padrão de Projeto: DECORATOR (Decorador)
# ============================================
# Tipo: Estrutural
#
# Objetivo:
# Permitir adicionar comportamentos adicionais a objetos dinamicamente,
# encapsulando-os dentro de outros objetos (decoradores) que implementam
# a mesma interface. Isso evita a necessidade de criar subclasses
# para cada variação de comportamento.

# =====================================================
# Interface base do Componente
# =====================================================
class Componente:
    """
    A interface base define operações que podem ser alteradas
    ou estendidas por decoradores.
    """

    def operacao(self) -> str:
        pass


# =====================================================
# Componente Concreto
# =====================================================
class ComponenteConcreto(Componente):
    """
    Fornece uma implementação padrão da operação.
    Pode haver várias variações dessa classe.
    """

    def operacao(self) -> str:
        return "ComponenteConcreto"


# =====================================================
# Classe base Decorador
# =====================================================
class Decorador(Componente):
    """
    O Decorador segue a mesma interface que os outros componentes.
    Seu principal propósito é armazenar uma referência para um
    componente encapsulado e delegar a ele as chamadas de método.
    """

    _componente: Componente = None

    def __init__(self, componente: Componente) -> None:
        self._componente = componente

    @property
    def componente(self) -> Componente:
        """
        Retorna o componente encapsulado.
        """
        return self._componente

    def operacao(self) -> str:
        """
        O comportamento padrão é delegar a chamada ao componente interno.
        """
        return self._componente.operacao()


# =====================================================
# Decoradores Concretos
# =====================================================
class DecoradorConcretoA(Decorador):
    """
    O DecoradorConcretoA chama o objeto encapsulado
    e modifica seu resultado de alguma forma.
    """

    def operacao(self) -> str:
        """
        Decoradores podem chamar a implementação da superclasse
        para reutilizar o comportamento padrão.
        """
        return f"DecoradorConcretoA({self.componente.operacao()})"


class DecoradorConcretoB(Decorador):
    """
    O DecoradorConcretoB pode adicionar comportamento antes ou
    depois da chamada ao componente encapsulado.
    """

    def operacao(self) -> str:
        return f"DecoradorConcretoB({self.componente.operacao()})"


# =====================================================
# Código do Cliente
# =====================================================
def codigo_cliente(componente: Componente) -> None:
    """
    O código cliente trabalha com todos os objetos usando a interface
    Componente, permitindo independência das classes concretas.
    """
    print(f"RESULTADO: {componente.operacao()}", end="")


# =====================================================
# Execução Principal
# =====================================================
if __name__ == "__main__":
    # O cliente pode usar um componente simples...
    simples = ComponenteConcreto()
    print("Cliente: Tenho um componente simples:")
    codigo_cliente(simples)
    print("\n")

    # ...ou um componente decorado.
    # Observe que os decoradores podem encapsular outros decoradores também.
    decorador1 = DecoradorConcretoA(simples)
    decorador2 = DecoradorConcretoB(decorador1)
    print("Cliente: Agora tenho um componente decorado:")
    codigo_cliente(decorador2)



# Componente (Component): define a interface comum que tanto os objetos reais quanto os decoradores seguem.

# ComponenteConcreto: fornece o comportamento básico que pode ser “decorado”.

# Decorador (Decorator): mantém uma referência para um componente e segue a mesma interface.

# DecoradoresConcretos: adicionam comportamento extra ao encapsular o componente.

# Cliente: interage apenas com a interface Componente, sem saber se está usando um objeto simples ou decorado.