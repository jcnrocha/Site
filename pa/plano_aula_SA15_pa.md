# UC: Programação de Aplicativos
## SA 15 — 2º Trimestre

---

## Tema

Conexão com Banco de Dados — CRUD Parte 2

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Implementar operações de UPDATE para atualizar registros existentes no banco de dados via código
- Implementar operações de DELETE para remover registros do banco de dados via código
- Compreender o conceito de transação e aplicar commit e rollback para garantir a integridade dos dados
- Identificar situações onde o rollback é necessário para desfazer operações em caso de erro
- Consolidar o CRUD completo integrando as quatro operações em um fluxo único de sistema

**Capacidades da matriz:** 5. Conexão com banco de dados · Integrar banco de dados por meio da linguagem de programação · Aplicar métodos e técnicas de programação

---

## Conteúdo

- Retomada da SA 14: *"Na SA passada implementamos o INSERT e o SELECT com Prepared Statements — hoje completamos o CRUD com UPDATE e DELETE e aprendemos a garantir que as operações sejam seguras com transações"*

- **UPDATE — atualizando registros via código:**
  - Modifica um ou mais registros já existentes na tabela
  - Sintaxe básica: `UPDATE tabela SET coluna = valor WHERE condição`
  - **Atenção crítica:** UPDATE sem cláusula WHERE atualiza **todos** os registros da tabela — erro gravíssimo em produção

  ```java
  // Java — UPDATE com Prepared Statement
  String sql = "UPDATE alunos SET nota = ? WHERE id = ?";
  PreparedStatement ps = conexao.prepareStatement(sql);
  ps.setDouble(1, novaNota);
  ps.setInt(2, idAluno);
  int linhasAfetadas = ps.executeUpdate();
  exibir("Registros atualizados: " + linhasAfetadas);
  ```

  ```python
  # Python — UPDATE com Prepared Statement
  sql = "UPDATE alunos SET nota = %s WHERE id = %s"
  cursor.execute(sql, (novaNota, idAluno))
  conexao.commit()
  print(f"Registros atualizados: {cursor.rowcount}")
  ```

- **DELETE — removendo registros via código:**
  - Remove um ou mais registros da tabela
  - Sintaxe básica: `DELETE FROM tabela WHERE condição`
  - **Atenção crítica:** DELETE sem cláusula WHERE remove **todos** os registros da tabela — operação irreversível

  ```java
  // Java — DELETE com Prepared Statement
  String sql = "DELETE FROM alunos WHERE id = ?";
  PreparedStatement ps = conexao.prepareStatement(sql);
  ps.setInt(1, idAluno);
  int linhasAfetadas = ps.executeUpdate();
  exibir("Registros removidos: " + linhasAfetadas);
  ```

  ```python
  # Python — DELETE com Prepared Statement
  sql = "DELETE FROM alunos WHERE id = %s"
  cursor.execute(sql, (idAluno,))
  conexao.commit()
  print(f"Registros removidos: {cursor.rowcount}")
  ```

- **Verificando linhas afetadas:**
  - `executeUpdate()` em Java e `cursor.rowcount` em Python retornam o número de linhas afetadas
  - Valor 0: nenhum registro foi afetado — a condição WHERE não encontrou correspondência
  - Útil para confirmar se a operação realmente alterou algum dado antes de exibir mensagem de sucesso

- **Transações — commit e rollback:**
  - **Transação:** conjunto de operações que deve ser executado completamente ou não executado nenhuma — tudo ou nada
  - **Commit:** confirma todas as operações da transação · torna as alterações permanentes no banco
  - **Rollback:** desfaz todas as operações da transação desde o último commit · usado quando ocorre um erro no meio de uma sequência de operações

  - Exemplo do problema sem transação:
    - Sistema de transferência bancária: debita da conta A → **erro** → não credita na conta B → dinheiro some
    - Com transação: debita da conta A → **erro** → rollback → débito é desfeito → nenhuma conta é afetada

  ```java
  // Java — transação com commit e rollback
  try {
      conexao.setAutoCommit(false);   // desativa o commit automático

      // Operação 1
      ps1.executeUpdate();
      // Operação 2
      ps2.executeUpdate();

      conexao.commit();               // confirma as duas operações juntas
      exibir("Transação concluída com sucesso!");

  } catch (SQLException e) {
      conexao.rollback();             // desfaz tudo se qualquer operação falhar
      exibir("Erro — transação revertida: " + e.getMessage());
  } finally {
      conexao.setAutoCommit(true);    // restaura o comportamento padrão
      conexao.close();
  }
  ```

  ```python
  # Python — transação com commit e rollback
  try:
      cursor.execute(sql1, params1)
      cursor.execute(sql2, params2)
      conexao.commit()
      print("Transação concluída com sucesso!")
  except Exception as e:
      conexao.rollback()
      print(f"Erro — transação revertida: {e}")
  ```

- **CRUD completo — visão consolidada:**

  | Operação | SQL | Método | Requer commit? | Risco sem WHERE |
  |----------|-----|--------|---------------|-----------------|
  | INSERT | `INSERT INTO` | `executeUpdate()` | Sim | Não se aplica |
  | SELECT | `SELECT` | `executeQuery()` | Não | Retorna todos os registros |
  | UPDATE | `UPDATE SET` | `executeUpdate()` | Sim | Atualiza todos os registros |
  | DELETE | `DELETE FROM` | `executeUpdate()` | Sim | Remove todos os registros |

- **Boas práticas finais de CRUD:**
  - Sempre usar WHERE em UPDATE e DELETE — conferir duas vezes antes de executar
  - Usar transações quando duas ou mais operações dependem uma da outra para fazer sentido
  - Registrar (log) operações de DELETE — dados removidos são difíceis de recuperar
  - Considerar exclusão lógica em vez de física: campo `ativo = false` em vez de DELETE real

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 14: *"INSERT e SELECT prontos — hoje fechamos o CRUD com UPDATE e DELETE e aprendemos a proteger as operações com transações"* |
| Retomada | Professor pergunta: *"Imaginem um sistema bancário que debita da sua conta mas cai antes de creditar na conta destino. O que deveria acontecer com o débito?"* — alunos respondem · professor conecta com o conceito de transação e rollback |
| Explicação | Slides — UPDATE com WHERE obrigatório, DELETE com WHERE obrigatório, linhas afetadas, transação (commit e rollback), tabela consolidada do CRUD completo · demonstração ao vivo na IDE com cenário de erro para mostrar o rollback em ação |
| Dinâmica | "Operação Segura?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: UPDATE e DELETE sempre precisam de WHERE · commit confirma · rollback desfaz · transação garante tudo ou nada · CRUD completo é a base de qualquer sistema real · Próxima SA: formatação e documentação de código |

---

## Dinâmica — "Operação Segura?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar as operações de UPDATE, DELETE e o uso de transações por meio da análise crítica de cenários de uso — desenvolvendo o raciocínio de segurança e integridade de dados que todo desenvolvedor precisa ter ao manipular informações em banco de dados.

**Materiais:** slide com os cenários projetados · ficha de análise impressa (1 por grupo).

**Passo a passo:**

1. **Apresentação do cenário** *(1 min por rodada)*
O professor projeta um cenário ou trecho de código. O grupo deve classificar: operação segura · operação com risco · operação incorreta — e justificar.

2. **Análise em grupo** *(8 min)*
Os grupos analisam cada cenário, classificam e descrevem o que pode dar errado e como corrigir.

3. **Correção coletiva** *(6 min)*
O professor revela a classificação e discute os riscos reais de cada cenário.

**Cenários para analisar:**

| Cenário | Classificação | Risco / Correção |
|---------|--------------|-----------------|
| `DELETE FROM alunos` sem WHERE | Incorreta — crítico | Remove todos os alunos da tabela · sempre usar WHERE com condição específica |
| `UPDATE alunos SET nota = 10.0 WHERE id = ?` com Prepared Statement | Segura | Atualiza apenas o aluno com o ID informado · uso correto |
| Dois INSERTs em tabelas relacionadas sem transação — o segundo falha | Risco | Banco fica com dados inconsistentes · usar transação com rollback |
| DELETE com `rowcount == 0` sem tratamento | Risco | Nenhum registro foi removido mas o sistema exibe "removido com sucesso" · verificar rowcount antes de exibir mensagem |
| `UPDATE produtos SET preco = preco * 0.9` sem WHERE para aplicar desconto em todos | Segura (se intencional) | Correto se o objetivo é atualizar todos · documentar e confirmar a intenção antes de executar |
| Rollback chamado após commit bem-sucedido | Incorreta | Rollback não desfaz um commit já confirmado · o rollback só age sobre operações ainda não commitadas |

> **Nota:** reforçar que erros de UPDATE e DELETE sem WHERE são responsáveis por alguns dos maiores incidentes de perda de dados em empresas. No mercado, operações de DELETE e UPDATE em produção exigem aprovação, backup prévio e execução cuidadosa — cultivar esse hábito desde o início da formação é o que diferencia um profissional responsável.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 14 — 20/05/2026 · Conexão com Banco de Dados — CRUD Parte 1 |
| Próxima SA → | SA 16 — 03/06/2026 · Técnicas de Programação — Formatação e Documentação de Código |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code e SGBD configurados
- Projeto de demonstração com banco e tabelas prontos para UPDATE e DELETE ao vivo
- Ficha de análise da dinâmica impressa (1 por grupo) ou slide projetado
- Quadro branco e marcador

---

## Observações do Professor
