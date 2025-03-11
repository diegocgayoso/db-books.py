```markdown
# 📚✨ Biblioteca de Usuários e Livros ✨📚

Um projeto para guardar seus leitores e livros favoritos em um banco de dados relacional!  

---

## 🧙♂️ Sobre o Projeto  
Uma base de dados simples mas poderosa, feita com **SQLAlchemy** + **SQLite**, onde:  
- **👤 Usuários** podem ser registrados com nome, e-mail e senha  
- **📖 Livros** ganham vida com título, autor, ano e dono!  

Perfeito para aprender ORM e brincar de bibliotecário(a) digital!  

---

## 🏰 Estrutura da Base de Dados  
### Tabela `users`
| Coluna    | Tipo    | Descrição               |
|-----------|---------|-------------------------|
| id        | Integer | Chave única do usuário  |
| name      | String  | Nome                    |
| email     | String  | E-mail                  |
| password  | String  | Senha  🔒               |
| active    | Boolean | Usuário ativo?          |

### Tabela `books` (📖 Livros)
| Coluna    | Tipo    | Descrição                |
|-----------|---------|--------------------------|
| id        | Integer | Chave única do livro     |
| title     | String  | Título ✨         |
| author    | String  | Autor(a)                 |
| year      | Integer | Ano de lançamento        |
| user_id   | Integer | Dono do livro (usuário)  |

---

## 🔮 Tecnologias Usadas  
- **SQLAlchemy** (Mapeamento objeto-relacional)  
- **SQLite** (Banco de dados portátil)  
- **Python** (Linguagem)  

---

## 🧪 Como Explorar o Projeto  
1. **Instale as dependecias necessárias**:  
```bash
pip install sqlalchemy
```

2. **Execute o código**:  
```bash
python seu_arquivo.py
```

3. **Abra o banco de dados**:  
```bash
sqlite3 database.db
```

4. **Experimente na prática**:  
```python
# Criar novo livro (descomente o código no arquivo!)
livro_mágico = Book("Harry Potter", "J.K. Rowling", 1997, 1)
session.add(livro_mágico)
session.commit()

# Consultar todos os usuários
leitores = session.query(User).all()
print(leitores)  # ✨ Apareça, usuários!
```

---

## 🧙♀️ Observações  
- Os dados ficam guardados no `database.db` (não desaparecem como fumaça!)  
- O código tem funcionalidades básicas - perfeito para estudos de ORM!  
- Achou maneiro? Adicione novos métodos às classes!  

**Divirta-se programando!** 🎩🐍  
```  

*P.S.: O SQLAlchemy já está preparada - basta soltar as queries!* 😉
