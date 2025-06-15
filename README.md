---

## 📦 Exercício 01 - Operações Matemáticas em Python com foco de Inteiros (int)

Estas atividades reforçam o uso de **números inteiros em Python**, entrada de dados com `input()` e operadores matemáticos.

## 📦 Alterações no decorrer das atividades

### ♻️ Refatoração com função `titulo()`

Para padronizar e reutilizar a formatação dos cabeçalhos dos exercícios no terminal, foi criada a função:

```python
def titulo(titulo):
    print("\n" + titulo)
    print("*" * len(titulo) + "\n")
```

### Adicionando try e except básicos no codigo

   except ZeroDivisionError:
      print("integer division or modulo by zero")
   except KeyboardInterrupt:
      print("Acredito que você não queira mais digitar nenhum número")

### 🔢 Exercícios:

1. **Soma de inteiros**  
   Solicita dois números inteiros e imprime a soma.

2. **Resto da divisão por 5**  
   Recebe um número e calcula o `módulo` (`%`) por 5.

3. **Multiplicação de inteiros**  
   Recebe dois números e exibe a multiplicação.

4. **Divisão inteira**  
   Solicita dois inteiros e mostra a divisão inteira (`//`).

5. **Quadrado de um número**  
   Lê um número e imprime seu quadrado usando `**`.

---
## Exercício 02 - Operações Matemáticas em Python com foco no Float

Este programa Python realiza diversas operações matemáticas básicas e conversões, interagindo com o usuário via terminal.

### ♻️ Refatoração com função `titulo()`

Para padronizar e reutilizar a formatação dos cabeçalhos dos exercícios no terminal, foi criada a função:

```python
def titulo(titulo):
    print("\n" + titulo)
    print("*" * len(titulo) + "\n")
```

### Criei uma calculadora de media que o usuário pode escolher quantas notas deseja calcular:
Localizado no comentario:
   7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

### Adicionando try e except básicos no codigo

except ValueError:
    print("could not convert string to float: '2,2'")
except ZeroDivisionError:
    print("division by zero")
except KeyboardInterrupt:
    print("Acredito que não queira mais digitar nenhum número")


## 📋 Funcionalidades

O programa contém as seguintes operações:

1. **Soma de dois números flutuantes**
2. **Cálculo de média de notas** (com verificação de aprovação)
3. **Cálculo de potência** (base e expoente)
4. **Conversão de temperatura** (Celsius para Fahrenheit)
5. **Cálculo da área de um círculo**

---

## Exercício 03 - Manipulaçãp de Strings (`str`)
1. **Conversão para maiúsculas
2. **Conversão para minúsculas
3. **Remoção de espaços
4. **Separação de data (dd/mm/aaaa)
5. **Concatenação

---