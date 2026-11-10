# ============================================================
# PORTFOLIO DE PROGRAMACAO MATEMATICA - PARTE 2
# ATIVIDADE 1: CONGRUENCIA MODULAR E TEOREMA CHINES DO RESTO
# ============================================================
# Aluno: Carlos Eduardo Rodrigues Lins
# Matricula: 2612082019
# Curso: Engenharia da Computacao
# Disciplina: Estruturas Matematicas para Computacao - Matematica Discreta
# Turno: Matutino
# Linguagem: Python
# ============================================================


def ler_inteiro(mensagem):
    """Solicita um numero inteiro e repete a pergunta se a entrada for invalida."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.\n")


def calcular_mdc(a, b, mostrar_passos=False):
    """Calcula o MDC pelo algoritmo de Euclides, sem math.gcd()."""
    a = abs(a)
    b = abs(b)
    passo = 1

    if mostrar_passos:
        print(f"\nAlgoritmo de Euclides para MDC({a}, {b}):")

    while b != 0:
        quociente = a // b
        resto = a % b
        if mostrar_passos:
            print(f"  Passo {passo}: {a} = {b} * {quociente} + {resto}")
        a, b = b, resto
        passo += 1

    if mostrar_passos:
        print(f"  MDC = {a}\n")
    return a


def inverso_modular(numero, modulo, mostrar_passos=False):
    """Encontra o inverso por Euclides estendido. Retorna None se nao existir."""
    if modulo == 1:
        # A congruencia modulo 1 e sempre verdadeira; seu unico resto e zero.
        if mostrar_passos:
            print("  Modulo 1: a congruencia e trivial; usamos o representante 0.\n")
        return 0

    r0 = modulo
    r1 = numero % modulo
    t0 = 0
    t1 = 1
    passo = 1

    if mostrar_passos:
        print(f"  Euclides estendido para encontrar o inverso de {numero} modulo {modulo}:")

    while r1 != 0:
        quociente = r0 // r1
        resto = r0 - quociente * r1
        if mostrar_passos:
            print(f"    Passo {passo}: {r0} = {r1} * {quociente} + {resto}")
        r0, r1 = r1, resto
        t0, t1 = t1, t0 - quociente * t1
        passo += 1

    if r0 != 1:
        if mostrar_passos:
            print(f"  MDC = {r0}; portanto, o inverso nao existe.\n")
        return None

    inverso = t0 % modulo
    if mostrar_passos:
        print(f"  Inverso encontrado: {inverso}")
        print(f"  Conferencia: ({numero} * {inverso}) % {modulo} = {(numero * inverso) % modulo}\n")
    return inverso


def ler_conjunto(nome):
    """Le elementos inteiros separados por espaco ou virgula."""
    while True:
        entrada = input(f"Digite os elementos de {nome} (separe por espacos ou virgulas): ")
        entrada = entrada.replace(",", " ").strip()
        if entrada == "":
            return set()
        try:
            return {int(item) for item in entrada.split()}
        except ValueError:
            print("Ha um elemento que nao e inteiro. Tente novamente.\n")


def conjunto_das_partes(conjunto):
    """Gera manualmente o conjunto das partes, sem funcao pronta."""
    partes = [set()]
    for elemento in sorted(conjunto):
        novas_partes = []
        for parte in partes:
            novas_partes.append(parte | {elemento})
        partes.extend(novas_partes)
    return partes


def formatar_conjunto(conjunto):
    """Formata um conjunto em notacao literal com seus elementos ordenados."""
    if not conjunto:
        return "{}"
    return "{" + ", ".join(str(item) for item in sorted(conjunto)) + "}"


def exibir_partes(conjunto):
    partes = conjunto_das_partes(conjunto)
    representacoes = [formatar_conjunto(parte) for parte in partes]
    return "{" + ", ".join(representacoes) + "}", len(partes)


def demonstrar_congruencia():
    print("\n" + "=" * 65)
    print("PARTE A - VERIFICACAO DE CONGRUENCIA MODULAR")
    print("=" * 65)

    a = ler_inteiro("Digite o inteiro a: ")
    b = ler_inteiro("Digite o inteiro b: ")
    n = ler_inteiro("Digite o modulo n (n > 0): ")
    while n <= 0:
        print("O modulo precisa ser positivo.")
        n = ler_inteiro("Digite novamente o modulo n: ")

    diferenca = a - b
    resto = diferenca % n

    print("\nCalculos realizados:")
    print(f"  a = {a}; b = {b}; n = {n}")
    print(f"  Diferenca: a - b = {a} - ({b}) = {diferenca}")
    print(f"  Divisao inteira: {diferenca} = ({diferenca // n}) * {n} + {resto}")
    print(f"  Resto de (a - b) por n: {diferenca} % {n} = {resto}")
    print(f"  Restos individuais: {a} % {n} = {a % n} e {b} % {n} = {b % n}")

    if resto == 0:
        print(f"\nConclusao: {a} e {b} SAO congruentes modulo {n}.")
        print(f"Portanto, {a} e {b} sao congruentes modulo {n}.")
    else:
        print(f"\nConclusao: {a} e {b} NAO sao congruentes modulo {n}.")


def ler_sistema_congruencias():
    """Le tres ou quatro congruencias e verifica coprimalidade par a par."""
    while True:
        quantidade = ler_inteiro("Quantas congruencias deseja resolver? Digite 3 ou 4: ")
        while quantidade not in (3, 4):
            print("Escolha somente 3 ou 4 congruencias.")
            quantidade = ler_inteiro("Digite 3 ou 4: ")

        restos = []
        modulos = []
        print("\nDigite o resto e o modulo de cada congruencia x = a (mod n).")
        for indice in range(quantidade):
            print(f"\nCongruencia {indice + 1}:")
            resto = ler_inteiro("  Resto a: ")
            modulo = ler_inteiro("  Modulo n (positivo): ")
            while modulo <= 0:
                print("  O modulo deve ser positivo.")
                modulo = ler_inteiro("  Digite novamente o modulo: ")
            restos.append(resto % modulo)
            modulos.append(modulo)

        print("\nVerificacao de coprimalidade dois a dois:")
        todos_coprimos = True
        for i in range(quantidade):
            for j in range(i + 1, quantidade):
                mdc = calcular_mdc(modulos[i], modulos[j], mostrar_passos=True)
                if mdc != 1:
                    print(f"Os modulos {modulos[i]} e {modulos[j]} nao sao coprimos.")
                    todos_coprimos = False

        if todos_coprimos:
            return restos, modulos

        print("O sistema nao atende a condicao do Teorema Chines do Resto nesta atividade.")
        print("Informe novamente todos os restos e modulos.\n")


def resolver_teorema_chines():
    print("\n" + "=" * 65)
    print("PARTE B - TEOREMA CHINES DO RESTO")
    print("=" * 65)
    print("O programa aceita sistemas com tres ou quatro congruencias.\n")

    restos, modulos = ler_sistema_congruencias()

    # Etapa 1: calcular o produto de todos os modulos.
    N = 1
    for modulo in modulos:
        N *= modulo

    print("\nEtapa 1 - Produto dos modulos:")
    print("  N = " + " * ".join(str(modulo) for modulo in modulos) + f" = {N}")

    soma = 0
    print("\nEtapas 2 a 5 - Calculo de N_i, dos inversos e dos termos:")
    for indice in range(len(modulos)):
        modulo = modulos[indice]
        resto = restos[indice]
        Ni = N // modulo
        print(f"\nCongruencia {indice + 1}: x tem resto {resto} na divisao por {modulo}")
        print(f"  N_{indice + 1} = N / n_{indice + 1} = {N} / {modulo} = {Ni}")
        inverso = inverso_modular(Ni, modulo, mostrar_passos=True)

        if inverso is None:
            print("Nao foi possivel encontrar o inverso. Verifique os modulos.")
            return

        if modulo == 1:
            print("  O termo desta congruencia e nulo, pois o modulo 1 e trivial.")
        termo = resto * Ni * inverso
        print(f"  Termo: a_{indice + 1} * N_{indice + 1} * inverso")
        print(f"       = {resto} * {Ni} * {inverso} = {termo}")
        soma += termo

    # Etapa 6: reduzir a soma modulo N.
    x0 = soma % N
    print("\nEtapa 6 - Calculo da solucao particular:")
    print(f"  Soma dos termos = {soma}")
    print(f"  x0 = {soma} % {N} = {x0}")

    # Etapa 7: verificar todas as congruencias.
    print("\nEtapa 7 - Verificacao da solucao:")
    todas_satisfeitas = True
    for indice in range(len(modulos)):
        modulo = modulos[indice]
        resto = restos[indice]
        resultado = x0 % modulo
        satisfaz = resultado == resto % modulo
        print(f"  {x0} % {modulo} = {resultado}; resto esperado = {resto % modulo} -> "
              f"{'OK' if satisfaz else 'FALHOU'}")
        if not satisfaz:
            todas_satisfeitas = False

    if todas_satisfeitas:
        print("\nConclusao: o sistema possui a solucao geral:")
        print(f"  x = {x0} + t * {N}, com t pertencente aos inteiros.")
    else:
        print("\nA verificacao falhou. Confira os dados digitados.")


def main():
    print("=" * 65)
    print("PORTFOLIO DE PROGRAMACAO MATEMATICA - PARTE 2")
    print("ATIVIDADE 1 - CONGRUENCIA MODULAR E TEOREMA CHINES DO RESTO")
    print("Aluno: Carlos Eduardo Rodrigues Lins | Matricula: 2612082019")
    print("Curso: Engenharia da Computacao | Turno: Matutino")
    print("=" * 65)

    demonstrar_congruencia()
    resolver_teorema_chines()

    print("\nFim da Atividade 1. Todos os calculos principais foram exibidos.")


if __name__ == "__main__":
    main()
