# Portfólio de Programação Matemática — Parte 2

**Disciplina:** Estruturas Matemáticas para Computação — Matemática Discreta   
**Curso:** Engenharia da Computação   
**Linguagem:** Python   

## Aluno
- Nome: Carlos Eduardo Rodrigues Lins
- Matrícula: 2612082019
- Turno: Matutino


### Atividade 1 — Congruência modular e Teorema Chinês do Resto (0,8 ponto)

Arquivo Python: `P2/atividade_01_congruencia_tcr/congruencia_tcr.py`
Documento explicativo: `P2/atividade_01_congruencia_tcr/documento_atividade_01.pdf`

O programa:
- verifica se dois inteiros são congruentes módulo um inteiro positivo;
- aceita sistemas com três ou quatro congruências;
- verifica se os módulos são coprimos dois a dois usando o algoritmo de Euclides;
- calcula o produto total, os valores auxiliares e os inversos pelo algoritmo de Euclides estendido;
- apresenta a solução geral e confere a solução em todas as congruências.

### Atividade 2 — Criptografia RSA (1,2 ponto)

Arquivo Python: `P2/atividade_02_rsa/rsa.py`  
Documento explicativo: `P2/atividade_02_rsa/documento_atividade_02.pdf`  

O programa:
- verifica se os números p e q são primos, maiores que 1 e distintos;
- calcula n e a função totiente φ(n);
- valida o expoente público e;
- encontra o expoente privado d pelo algoritmo de Euclides estendido;
- cifra e decifra uma mensagem numérica por exponenciação modular rápida;
- demonstra o Pequeno Teorema de Fermat e o Teorema de Euler.

## Como executar no VS Code

No terminal do VS Code, a partir desta pasta, execute:

python congruencia_tcr.py


Para executar a segunda atividade:

python rsa.py


## Testes de exemplo

**Atividade 1 — Parte A**
- `a = 23`, `b = 8`, `n = 5` → congruentes; resto da diferença igual a 0.
- `a = 17`, `b = 6`, `n = 4` → não congruentes; resto da diferença igual a 3.

**Atividade 1 — Parte B**
- `x ≡ 2 (mod 3)`, `x ≡ 3 (mod 5)`, `x ≡ 2 (mod 7)` → `x = 23 + 105t`.
- `x ≡ 1 (mod 2)`, `x ≡ 2 (mod 3)`, `x ≡ 3 (mod 5)`, `x ≡ 2 (mod 7)` → `x = 23 + 210t`.
- Módulos 4 e 6 no mesmo sistema → o programa informa que eles não são coprimos e pede novos dados.

**Atividade 2**
- `p = 5`, `q = 11`, `e = 3`, `M = 7` → `n = 55`, `φ(n) = 40`, `d = 27`, mensagem cifrada `C = 13` e mensagem decifrada `M' = 7`.
- `p = 7`, `q = 13`, `e = 5`, `M = 12` → `n = 91`, `φ(n) = 72`, `d = 29`, `C = 38` e `M' = 12`.
- Para Fermat, `p = 5` e `a = 2` → `2⁴ % 5 = 1`.
- Para Euler, `n = 55`, `φ(n) = 40` e `a = 2` → `2⁴⁰ % 55 = 1`.