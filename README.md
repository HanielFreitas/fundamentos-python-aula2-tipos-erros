---

## 📦 Atividades de Inteiros (int)

Estas atividades reforçam o uso de **números inteiros em Python**, entrada de dados com `input()` e operadores matemáticos.

## 📦 Alterações no decorrer das atividades

### ♻️ Refatoração com função `titulo()`

Para padronizar e reutilizar a formatação dos cabeçalhos dos exercícios no terminal, foi criada a função:

```python
def titulo(titulo):
    print("\n" + titulo)
    print("*" * len(titulo) + "\n")```

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
