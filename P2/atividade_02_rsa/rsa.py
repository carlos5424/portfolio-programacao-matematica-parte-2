# ============================================================
# PORTFOLIO DE PROGRAMACAO MATEMATICA - PARTE 2
# ATIVIDADE 2: CRIPTOGRAFIA RSA
# ============================================================
# Aluno: Carlos Eduardo Rodrigues Lins
# Matricula: 2612082019
# Curso: Engenharia da Computacao
# Disciplina: Estruturas Matematicas para Computacao - Matematica Discreta
# Turno: Matutino
# Linguagem: Python
# ============================================================


def ler_inteiro(mensagem):
    """Solicita um inteiro e repete a pergunta se a entrada for invalida."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.\n")


def eh_primo(numero, mostrar_passos=False):
    """Verifica se um inteiro e primo por tentativa de divisores."""
    if numero <= 1:
        if mostrar_passos:
            print(f"  {numero} nao e primo, pois numeros primos sao maiores que 1.")
        return False

    divisor = 2
    while divisor * divisor <= numero:
        resto = numero % divisor
        if mostrar_passos:
            print(f"  Teste: {numero} % {divisor} = {resto}")
        if resto == 0:
            if mostrar_passos:
                print(f"  {numero} e divisivel por {divisor}; portanto, nao e primo.")
            return False
        divisor += 1

    if mostrar_passos:
        print(f"  Nenhum divisor inteiro entre 2 e a raiz de {numero} foi encontrado.")
        print(f"  Portanto, {numero} e primo.")
    return True


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
    """Calcula o inverso multiplicativo usando o algoritmo de Euclides estendido."""
    r0, r1 = modulo, numero % modulo
    t0, t1 = 0, 1
    passo = 1

    if mostrar_passos:
        print(f"\nEuclides estendido para o inverso de {numero} modulo {modulo}:")

    while r1 != 0:
        quociente = r0 // r1
        resto = r0 - quociente * r1
        if mostrar_passos:
            print(f"  Passo {passo}: {r0} = {r1} * {quociente} + {resto}")
        r0, r1 = r1, resto
        t0, t1 = t1, t0 - quociente * t1
        passo += 1

    if r0 != 1:
        if mostrar_passos:
            print(f"O MDC e {r0}; o inverso multiplicativo nao existe.\n")
        return None

    inverso = t0 % modulo
    if mostrar_passos:
        print(f"Inverso encontrado: d = {inverso}")
        print(f"Conferencia: ({numero} * {inverso}) % {modulo} = {(numero * inverso) % modulo}\n")
    return inverso


def potencia_modular(base, expoente, modulo, titulo):
    """Calcula base**expoente % modulo por exponenciacao modular rapida."""
    resultado = 1
    base_atual = base % modulo
    expoente_atual = expoente
    passo = 1

    print(f"\n{titulo}")
    print(f"Calcular {base}^{expoente} modulo {modulo} por quadraturas sucessivas:")

    while expoente_atual > 0:
        bit = expoente_atual % 2
        print(f"  Passo {passo}: expoente={expoente_atual}, base reduzida={base_atual}.")
        if bit == 1:
            antes = resultado
            resultado = (resultado * base_atual) % modulo
            print(f"    Expoente impar: ({antes} * {base_atual}) % {modulo} = {resultado}.")
        else:
            print("    Expoente par: nao multiplicamos a base ao resultado nesta etapa.")

        base_atual = (base_atual * base_atual) % modulo
        expoente_atual //= 2
        print(f"    Nova base = {base_atual}; novo expoente = {expoente_atual}.")
        passo += 1

    print(f"  Resultado final: {base}^{expoente} % {modulo} = {resultado}\n")
    return resultado


def ler_primos_distintos():
    """Solicita p e q primos, distintos, e com expoente publico possivel."""
    while True:
        print("\nPARTE A - ESCOLHA DOS NUMEROS PRIMOS")
        p = ler_inteiro("Digite o numero primo p: ")
        q = ler_inteiro("Digite o numero primo q: ")

        print("\nVerificacao de primalidade de p:")
        primo_p = eh_primo(p, mostrar_passos=True)
        print("\nVerificacao de primalidade de q:")
        primo_q = eh_primo(q, mostrar_passos=True)

        if not primo_p or not primo_q or p == q:
            print("\nCondicao nao atendida: p e q devem ser primos distintos. Tente novamente.")
            continue

        n = p * q
        phi = (p - 1) * (q - 1)
        if phi <= 3:
            print("\nEsse par nao permite um e inteiro com 1 < e < phi(n). Escolha outro par.")
            continue

        print(f"\nCalculo de n: n = p * q = {p} * {q} = {n}")
        print(f"Calculo da funcao totiente: phi(n) = (p - 1) * (q - 1)")
        print(f"phi({n}) = ({p} - 1) * ({q} - 1) = {phi}")
        return p, q, n, phi


def escolher_expoente_publico(phi):
    """Solicita e valida e: 1 < e < phi e MDC(e, phi) = 1."""
    print("\nEscolha do expoente publico:")
    while True:
        e = ler_inteiro(f"Digite e (1 < e < {phi}): ")
        if not (1 < e < phi):
            print("O expoente precisa satisfazer 1 < e < phi(n).\n")
            continue

        mdc = calcular_mdc(e, phi, mostrar_passos=True)
        if mdc != 1:
            print("O MDC nao e 1. Escolha outro expoente publico.\n")
            continue
        print(f"Expoente publico aceito: e = {e}, pois MDC({e}, {phi}) = 1.")
        return e


def construir_chave_privada(e, phi, n):
    print("\nPARTE B - CONSTRUCAO DAS CHAVES")
    d = inverso_modular(e, phi, mostrar_passos=True)
    if d is None:
        print("Nao foi possivel construir a chave privada com os parametros escolhidos.")
        return None
    print(f"Verificacao da chave: e * d = {e} * {d} = {e * d}")
    print(f"{e * d} % {phi} = {(e * d) % phi}")
    print(f"Chave publica: (e, n) = ({e}, {n})")
    print(f"Chave privada: (d, n) = ({d}, {n})")
    return d


def cifrar_e_decifrar(n, e, d):
    print("\nPARTE C - CIFRAGEM E DECIFRAGEM")
    mensagem = ler_inteiro(f"Digite a mensagem numerica M (0 <= M < {n}): ")
    while not (0 <= mensagem < n):
        print("A mensagem precisa estar no intervalo informado.")
        mensagem = ler_inteiro(f"Digite novamente M (0 <= M < {n}): ")

    cifrada = potencia_modular(mensagem, e, n, "CIFRAGEM")
    decifrada = potencia_modular(cifrada, d, n, "DECIFRAGEM")

    print("Resumo da cifragem e decifragem:")
    print(f"  Mensagem original: M = {mensagem}")
    print(f"  Mensagem cifrada: C = M^e mod n = {cifrada}")
    print(f"  Mensagem decifrada: M' = C^d mod n = {decifrada}")
    if decifrada == mensagem:
        print("  Conferencia: M' = M. A recuperacao da mensagem foi bem-sucedida.")
    else:
        print("  Conferencia: M' e diferente de M. Revise os parametros.")


def demonstrar_fermat_e_euler(p, n, phi):
    print("\nPARTE D - TEOREMAS DE FERMAT E EULER")

    # Pequeno Teorema de Fermat: p e primo e p nao divide a base.
    print("\nPequeno Teorema de Fermat:")
    base_fermat = ler_inteiro(f"Digite uma base a que nao seja divisivel por p = {p}: ")
    while base_fermat % p == 0:
        print(f"A base nao pode ser multipla de {p}. Tente novamente.")
        base_fermat = ler_inteiro("Digite outra base a: ")

    resultado_fermat = potencia_modular(
        base_fermat, p - 1, p, "Verificacao do Pequeno Teorema de Fermat"
    )
    print(f"Como p = {p} e primo e {base_fermat} nao e divisivel por {p}:")
    print(f"  {base_fermat}^{p - 1} % {p} = {resultado_fermat}")
    if resultado_fermat == 1:
        print(f"  O resultado confirma que o resto de {base_fermat}^{p - 1} por {p} e 1.")
    else:
        print("  O resultado nao confirmou o teorema; confira os valores.")

    # Teorema de Euler: a base deve ser coprima com o modulo n.
    print("\nTeorema de Euler:")
    while True:
        base_euler = ler_inteiro(f"Digite uma base a coprima com n = {n}: ")
        mdc = calcular_mdc(base_euler, n, mostrar_passos=True)
        if mdc == 1:
            break
        print("A base nao e coprima com n. Escolha outro valor.\n")

    resultado_euler = potencia_modular(
        base_euler, phi, n, "Verificacao do Teorema de Euler"
    )
    print(f"Como MDC({base_euler}, {n}) = 1:")
    print(f"  {base_euler}^{phi} % {n} = {resultado_euler}")
    if resultado_euler == 1:
        print(f"  O resultado confirma que o resto de {base_euler}^{phi} por {n} e 1.")
    else:
        print("  O resultado nao confirmou o teorema; confira os valores.")


def main():
    print("=" * 70)
    print("PORTFOLIO DE PROGRAMACAO MATEMATICA - PARTE 2")
    print("ATIVIDADE 2 - CRIPTOGRAFIA RSA")
    print("Aluno: Carlos Eduardo Rodrigues Lins | Matricula: 2612082019")
    print("Curso: Engenharia da Computacao | Turno: Matutino")
    print("=" * 70)
    print("Aviso: este programa usa mensagens numericas para fins didaticos; nao e um sistema seguro de producao.\n")

    p, q, n, phi = ler_primos_distintos()
    e = escolher_expoente_publico(phi)

    d = construir_chave_privada(e, phi, n)
    if d is None:
        return

    cifrar_e_decifrar(n, e, d)
    demonstrar_fermat_e_euler(p, n, phi)

    print("\nFim da Atividade 2. Os calculos essenciais foram exibidos na tela.")


if __name__ == "__main__":
    main()
