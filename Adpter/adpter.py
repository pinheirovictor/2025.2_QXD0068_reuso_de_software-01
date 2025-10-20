# ============================================================
# OBJETIVO DO EXEMPLO
# ============================================================
# Imagine que temos um sistema que já espera trabalhar com objetos
# que seguem uma interface específica — o "Alvo" (Target).
# 
# Porém, precisamos usar uma classe já existente (Adaptee)
# que faz o que queremos, mas com uma interface completamente diferente.
#
# Se tentarmos usar o Adaptee diretamente, o código cliente quebra.
# 
# O padrão Adapter resolve isso criando um "tradutor" — o Adaptador —
# que converte a interface do Adaptee para o formato que o Alvo entende.
# ============================================================


# ============================================================
# CLASSE ALVO (TARGET)
# ============================================================
# Representa a interface esperada pelo cliente.
# É o formato "oficial" que o sistema entende.
# ============================================================

class Alvo:
    """
    O Alvo define a interface usada pelo código cliente.
    É a "forma" que o cliente entende — o padrão esperado.
    """

    def requisicao(self) -> str:
        """
        Método que o cliente sabe chamar.  
        Todas as classes compatíveis com o cliente devem implementar isso.
        """
        return "Alvo: comportamento padrão do alvo."


# ============================================================
# CLASSE ADAPTEE
# ============================================================
# Uma classe já existente que faz algo útil,
# mas de um jeito incompatível com o formato do cliente.
# ============================================================

class Adaptee:
    """
    O Adaptee tem um comportamento útil, mas sua interface é incompatível.
    Aqui simulamos isso com uma string "invertida".
    """

    def requisicao_especifica(self) -> str:
        # O texto está invertido para representar um formato diferente.
        return ".eetpadA od odahrovaeb laicepS"


# ============================================================
# CLASSE ADAPTADOR (ADAPTER)
# ============================================================
# É o "tradutor" que converte a interface do Adaptee
# para o formato esperado pelo Alvo.
# ============================================================

class Adaptador(Alvo, Adaptee):
    """
    O Adaptador combina herança (ou composição) para conectar
    o Adaptee e o Alvo.
    Ele traduz a linguagem do Adaptee para o formato que o cliente entende.
    """

    def requisicao(self) -> str:
        """
        Sobrescreve o método esperado pelo cliente (requisicao)
        e internamente usa o método do Adaptee.
        """
        # Chama o método do Adaptee e o "traduz" (inverte a string)
        return f"Adaptador: (TRADUZIDO) {self.requisicao_especifica()[::-1]}"


# ============================================================
# CÓDIGO CLIENTE
# ============================================================
# O cliente trabalha apenas com objetos compatíveis com a interface Alvo.
# Ele não precisa saber que existe um Adaptador por trás.
# ============================================================

def codigo_cliente(alvo: "Alvo") -> None:
    """
    O cliente interage apenas com o tipo Alvo.
    Qualquer classe que implemente 'requisicao()' pode ser usada aqui.
    """
    print(alvo.requisicao(), end="")


# ============================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================
# Demonstra como o padrão Adapter permite usar uma classe incompatível
# (Adaptee) sem alterar o código cliente.
# ============================================================

if __name__ == "__main__":
    # Cliente interagindo com o Alvo normalmente
    print("Cliente: Eu consigo trabalhar normalmente com objetos do tipo Alvo:")
    alvo = Alvo()
    codigo_cliente(alvo)
    print("\n")

    # Tentando usar o Adaptee diretamente
    adaptee = Adaptee()
    print("Cliente: A classe Adaptee tem uma interface estranha. Veja, eu não entendo:")
    print(f"Adaptee: {adaptee.requisicao_especifica()}", end="\n\n")

    # Agora usamos o Adaptador como "ponte" entre o cliente e o Adaptee
    print("Cliente: Mas eu posso trabalhar com ela através do Adaptador:")
    adaptador = Adaptador()
    codigo_cliente(adaptador)


# ============================================================
# RESUMO DIDÁTICO
# ============================================================
# Problema:
#   - Temos uma classe existente (Adaptee) útil, mas com interface incompatível.
#   - O cliente entende apenas o formato do Alvo.
#
# Solução:
#   - Criar um Adaptador que "traduz" as chamadas entre o cliente e o Adaptee.
#   - O Adaptador faz o Adaptee parecer um Alvo aos olhos do cliente.
#
# Benefícios:
#   - Reutiliza código legado ou de terceiros sem precisar modificá-lo.
#   - Mantém o código cliente inalterado (baixo acoplamento).
#   - Segue o princípio Aberto/Fechado (OCP): adiciona compatibilidade sem alterar o código existente.
#
# Analogia:
#   - Pense no Adaptador como um "carregador universal" de tomada:
#     o aparelho (cliente) espera um formato de plugue (Alvo),
#     mas o carregador antigo (Adaptee) tem outro formato.
#     O Adaptador faz a ponte entre os dois.
#
# Demonstração prática:
#   - Alvo → interface esperada pelo cliente.
#   - Adaptee → classe existente (incompatível).
#   - Adaptador → tradutor entre os dois.
# ============================================================














# # Classe Alvo (Target)
# # Define a interface esperada pelo código cliente.
# class Alvo:
#     """
#     O Alvo define a interface usada pelo código cliente.
#     É a "forma" que o cliente entende.
#     """

#     def requisicao(self) -> str:
#         return "Alvo: comportamento padrão do alvo."


# # Classe Adaptee (ou Adaptee)
# # É uma classe existente, mas com interface incompatível com o cliente.
# class Adaptee:
#     """
#     O Adaptee contém comportamentos úteis,
#     mas sua interface é incompatível com o código cliente.
#     Precisa de adaptação antes de ser usada.
#     """

#     def requisicao_especifica(self) -> str:
#         # Observe que o texto está invertido de propósito para simular "incompatibilidade"
#         return ".eetpadA od odahrovaeb laicepS"


# # Classe Adaptadora (Adapter)
# # Converte a interface do Adaptee para a interface do Alvo.
# class Adaptador(Alvo, Adaptee):
#     """
#     O Adaptador faz a interface do Adaptee compatível
#     com a interface esperada pelo Alvo (cliente),
#     usando herança múltipla.
#     """

#     def requisicao(self) -> str:
#         # Traduz o comportamento invertido do Adaptee
#         return f"Adaptador: (TRADUZIDO) {self.requisicao_especifica()[::-1]}"


# # Código do Cliente
# # Trabalha apenas com objetos que seguem a interface do Alvo.
# def codigo_cliente(alvo: "Alvo") -> None:
#     """
#     O código cliente espera objetos compatíveis com a interface do Alvo.
#     """
#     print(alvo.requisicao(), end="")


# # Execução do programa
# if __name__ == "__main__":
#     print("Cliente: Eu consigo trabalhar normalmente com objetos do tipo Alvo:")
#     alvo = Alvo()
#     codigo_cliente(alvo)
#     print("\n")

#     adaptee = Adaptee()
#     print("Cliente: A classe Adaptee tem uma interface estranha. Veja, eu não entendo:")
#     print(f"Adaptee: {adaptee.requisicao_especifica()}", end="\n\n")

#     print("Cliente: Mas eu posso trabalhar com ela através do Adaptador:")
#     adaptador = Adaptador()
#     codigo_cliente(adaptador)


# # Como explicar aos alunos:

# # Alvo (Target) → É a interface padrão que o sistema já entende.

# # Adaptee → É uma classe existente, mas que “fala outra língua” (interface diferente).

# # Adaptador (Adapter) → Traduz a linguagem do Adaptee para o formato que o Alvo entende.

# # codigo_cliente() → Representa o sistema que trabalha apenas com objetos que seguem o formato de Alvo.