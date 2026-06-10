# UC: Programação de Aplicativos
## SA 14 — 2º Trimestre

---

## Tema

Conexão com Banco de Dados — CRUD Parte 1

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o conceito de CRUD e sua relação com as operações fundamentais de um sistema de software
- Implementar operações de INSERT para inserir registros no banco de dados via código
- Implementar operações de SELECT com e sem filtro (WHERE) para recuperar dados do banco
- Utilizar Prepared Statements para parametrizar consultas SQL, evitando erros e vulnerabilidades
- Realizar tratamento básico de erros de operação com banco de dados usando try/catch

**Capacidades da matriz:** 5. Conexão com banco de dados · Integrar banco de dados por meio da linguagem de programação · Aplicar métodos e técnicas de programação

---

## Conteúdo

- Retomada da SA 13: *"Na SA passada configuramos a conexão e fizemos o primeiro SELECT — hoje avançamos para o CRUD completo, começando pelo INSERT e aprofundando o SELECT"*

- **O que é CRUD:**
  - Acrônimo para as quatro operações fundamentais de persistência de dados em qualquer sistema
  - Todo sistema que gerencia dados realiza alguma combinação dessas quatro operações

  | Letra | Operação | SQL | Descrição |
  |-------|----------|-----|-----------|
  | **C** | Create | `INSERT` | Inserir novos registros no banco |
  | **R** | Read | `SELECT` | Consultar e recuperar registros |
  | **U** | Update | `UPDATE` | Atualizar registros existentes |
  | **D** | Delete | `DELETE` | Remover registros do banco |

  > Esta SA cobre o **C** (INSERT) e o **R** (SELECT) · a SA 15 cobre o **U** (UPDATE) e o **D** (DELETE)

- **INSERT — inserindo dados via código:**
  - Comando SQL que adiciona um novo registro em uma tabela
  - Sintaxe básica: `INSERT INTO tabela (coluna1, coluna2) VALUES (valor1, valor2)`

  ```java
  // Java — INSERT simples
  Statement stmt = conexao.createStatement();
  stmt.executeUpdate("INSERT INTO alunos (nome, nota) VALUES ('Ana', 8.5)");
  exibir("Aluno inserido com sucesso!");
  ```

  ```python
  # Python — INSERT simples
  cursor = conexao.cursor()
  cursor.execute("INSERT INTO alunos (nome, nota) VALUES ('Ana', 8.5)")
  conexao.commit()
  print("Aluno inserido com sucesso!")
  ```

  > **Atenção:** após um INSERT (e qualquer operação que modifica dados), é necessário chamar `commit()` para confirmar a operação no banco — sem o commit, a alteração é descartada

- **Prepared Statements — parametrizando as operações:**
  - Forma segura e correta de passar valores dinâmicos para um comando SQL
  - Substitui a concatenação de strings — que é perigosa e propensa a erros
  - O valor do parâmetro é enviado separado do SQL — o SGBD trata os dois de forma independente
  - Previne SQL Injection: ataque onde um usuário mal-intencionado insere código SQL dentro de um campo de entrada

  ```java
  // Java — INSERT com Prepared Statement
  String sql = "INSERT INTO alunos (nome, nota) VALUES (?, ?)";
  PreparedStatement ps = conexao.prepareStatement(sql);
  ps.setString(1, nomeAluno);
  ps.setDouble(2, notaAluno);
  ps.executeUpdate();
  ```

  ```python
  # Python — INSERT com Prepared Statement
  sql = "INSERT INTO alunos (nome, nota) VALUES (%s, %s)"
  cursor.execute(sql, (nomeAluno, notaAluno))
  conexao.commit()
  ```

- **SELECT com filtro — WHERE:**
  - Recupera apenas os registros que atendem a uma condição específica
  - Muito mais eficiente que buscar tudo e filtrar no código da aplicação

  ```java
  // Java — SELECT com WHERE e Prepared Statement
  String sql = "SELECT nome, nota FROM alunos WHERE nota >= ?";
  PreparedStatement ps = conexao.prepareStatement(sql);
  ps.setDouble(1, 7.0);
  ResultSet rs = ps.executeQuery();

  while (rs.next()) {
      exibir("Nome: " + rs.getString("nome") + " | Nota: " + rs.getDouble("nota"));
  }
  ```

  ```python
  # Python — SELECT com WHERE
  sql = "SELECT nome, nota FROM alunos WHERE nota >= %s"
  cursor.execute(sql, (7.0,))
  for (nome, nota) in cursor:
      print(f"Nome: {nome} | Nota: {nota}")
  ```

- **Tratamento de erros com try/catch:**
  - Operações com banco de dados podem falhar por diversos motivos: banco indisponível, dados inválidos, violação de constraint
  - O bloco try/catch captura a exceção e permite que o programa trate o erro sem travar

  ```java
  // Java
  try {
      PreparedStatement ps = conexao.prepareStatement(sql);
      ps.executeUpdate();
      exibir("Operação realizada com sucesso!");
  } catch (SQLException e) {
      exibir("Erro ao acessar o banco: " + e.getMessage());
  } finally {
      conexao.close();   // sempre fecha a conexão
  }
  ```

- **Boas práticas de CRUD:**
  - Sempre usar Prepared Statements — nunca concatenar valores diretamente no SQL
  - Sempre chamar `commit()` após INSERT, UPDATE e DELETE
  - Sempre fechar conexão e cursor no bloco `finally` ou usar try-with-resources
  - Validar os dados na aplicação antes de enviar ao banco — nunca confiar apenas nas constraints do banco

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 13: *"Configuramos a conexão e fizemos o primeiro SELECT — hoje o sistema começa a escrever dados no banco de verdade"* |
| Retomada | Professor pergunta: *"Quando vocês se cadastram em um site, o que acontece com o nome e e-mail que vocês digitaram? Onde eles vão parar?"* — alunos respondem · professor conecta com INSERT e persistência de dados |
| Explicação | Slides — o que é CRUD, INSERT simples, por que Prepared Statement (com exemplo de SQL Injection), SELECT com WHERE, tratamento de erros com try/catch · demonstração ao vivo na IDE |
| Dinâmica | "CRUD na Prática" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: CRUD são as quatro operações fundamentais · INSERT insere · SELECT consulta · Prepared Statement é obrigatório · commit confirma a operação · Próxima SA: UPDATE e DELETE |

---

## Dinâmica — "CRUD na Prática"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** fixar as operações de INSERT e SELECT por meio da análise e correção de trechos de código com erros intencionais — desenvolvendo a capacidade de identificar falhas comuns na integração com banco de dados antes de executar o código.

**Materiais:** slide com os trechos de código projetados · ficha de análise impressa (1 por grupo).

**Passo a passo:**

1. **Apresentação do trecho** *(1 min por rodada)*
O professor projeta um trecho de código com um ou mais erros intencionais. O grupo deve identificar o erro, classificá-lo e propor a correção.

2. **Análise em grupo** *(8 min)*
Os grupos analisam cada trecho, registram o erro encontrado e escrevem a versão corrigida.

3. **Correção coletiva** *(6 min)*
O professor revela os erros e discute cada correção com a turma.

**Trechos para analisar:**

| Trecho com erro | Erro | Correção |
|----------------|------|----------|
| `stmt.executeUpdate("INSERT INTO alunos (nome, nota) VALUES (" + nome + "," + nota + ")")` | Concatenação direta — vulnerável a SQL Injection e erros de tipo | Usar Prepared Statement com `?` |
| INSERT executado sem `commit()` em Python | Dados não são persistidos no banco | Chamar `conexao.commit()` após o execute |
| `ps.setString(1, nota)` onde nota é `double` | Tipo incorreto — nota é double, não String | Usar `ps.setDouble(1, nota)` |
| Conexão aberta sem bloco try/catch nem fechamento | Conexão fica aberta indefinidamente — vazamento de recursos | Envolver em try/catch/finally com `conexao.close()` |
| `SELECT * FROM alunos WHERE nome = Ana` | Valor String sem aspas no SQL | Usar Prepared Statement: `WHERE nome = ?` |

> **Nota:** reforçar que SQL Injection é uma das vulnerabilidades mais exploradas no mundo — aparecem constantemente em listas de ataques reais a sistemas. Usar Prepared Statement não é apenas boa prática: é uma obrigação profissional em qualquer sistema que lida com dados de usuários.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 13 — 13/05/2026 · Conexão com Banco de Dados — Introdução |
| Próxima SA → | SA 15 — 27/05/2026 · Conexão com Banco de Dados — CRUD Parte 2 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code e SGBD configurados
- Projeto de demonstração com banco de dados e tabela `alunos` já criados
- Ficha de análise da dinâmica impressa (1 por grupo) ou slide projetado
- Quadro branco e marcador

---

## Observações do Professor
