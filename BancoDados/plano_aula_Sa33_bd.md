# UC: Fundamentos de Banco de Dados
## SA 33 — 3º Trimestre

---

## Tema

SQL DML Avançado — UPDATE e DELETE

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Escrever comandos `UPDATE` para alterar registros existentes com segurança, utilizando a cláusula `WHERE`
- Escrever comandos `DELETE` para remover registros com precisão, utilizando a cláusula `WHERE`
- Compreender os riscos críticos de executar `UPDATE` e `DELETE` sem a cláusula `WHERE`
- Utilizar transações básicas com `BEGIN`, `COMMIT` e `ROLLBACK` para proteger operações de escrita
- Identificar erros comuns no uso de UPDATE e DELETE e adotar boas práticas de segurança

**Habilidades da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais · H07 — Identificar ferramentas de manipulação de banco de dados

---

## Conteúdo

- Revisão rápida da SA 32: o que é uma View e como ela simplifica consultas recorrentes
- O papel do UPDATE e DELETE dentro do DML — completando o ciclo de manipulação de dados junto ao INSERT
- Comando `UPDATE` — alterar valores de registros existentes:
  ```sql
  UPDATE nome_tabela
  SET coluna1 = novo_valor, coluna2 = novo_valor
  WHERE condição;
  ```
- Comando `DELETE` — remover registros de uma tabela:
  ```sql
  DELETE FROM nome_tabela
  WHERE condição;
  ```
- **O risco crítico do UPDATE e DELETE sem WHERE:**
  - `UPDATE produto SET preco = 0;` — zera o preço de TODOS os produtos
  - `DELETE FROM cliente;` — apaga TODOS os clientes do banco
  - Esses erros acontecem em produção e podem ser irreversíveis sem backup
- Boas práticas antes de executar UPDATE ou DELETE:
  - Sempre escrever e testar o `WHERE` com um `SELECT` antes de executar
  - Verificar quantas linhas serão afetadas com `SELECT COUNT(*) WHERE ...`
  - Usar transações para poder desfazer a operação se necessário
- Transações básicas — `BEGIN`, `COMMIT` e `ROLLBACK`:
  ```sql
  BEGIN;
    UPDATE produto SET preco = preco * 1.10 WHERE id_categoria = 3;
  COMMIT; -- confirma as alterações
  ```
  ```sql
  BEGIN;
    DELETE FROM locacao WHERE data_locacao < '2023-01-01';
  ROLLBACK; -- desfaz as alterações antes de confirmar
  ```
- Diferença entre `DELETE` e `TRUNCATE`:
  - `DELETE` remove registros linha a linha, pode usar WHERE, pode ser revertido com ROLLBACK
  - `TRUNCATE` remove todos os registros de uma vez, não aceita WHERE, não pode ser revertido
- UPDATE com subquery no WHERE:
  ```sql
  UPDATE filme SET genero = 'Clássico'
  WHERE ano < (SELECT AVG(ano) FROM filme);
  ```
- Erros comuns: esquecer o WHERE, condição incorreta que afeta mais linhas do que o esperado, violar restrições de FK ao deletar

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 32 — pergunta oral: *"Qual a diferença entre uma View e uma tabela?"* |
| Retomada | Professor projeta o comando `UPDATE produto SET preco = 0;` sem WHERE e pergunta: *"O que acontece quando esse comando é executado?"* — alunos respondem · o silêncio ou hesitação já é suficiente para introduzir o tema |
| Explicação | Slides — UPDATE com WHERE, DELETE com WHERE, o risco do uso sem WHERE, boas práticas, transações BEGIN/COMMIT/ROLLBACK, diferença DELETE x TRUNCATE, UPDATE com subquery |
| Dinâmica | "Certo ou Errado? — Round UPDATE e DELETE" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: sempre SELECT antes de UPDATE ou DELETE · WHERE é obrigatório na prática · BEGIN/ROLLBACK salva vidas · Próxima aula: Documentação de Código SQL |

---

## Dinâmica — "Certo ou Errado? — Round UPDATE e DELETE"

**Duração:** 15 minutos · **Agrupamento:** turma inteira

**Objetivo:** fixar a sintaxe correta do UPDATE e DELETE e os riscos do uso sem WHERE por meio da análise crítica de comandos com erros intencionais — desenvolvendo o hábito de questionar cada comando de escrita antes de executar.

**Materiais:** slides com os blocos de código · quadro branco para registrar os votos.

**Passo a passo:**

1. **Apresentação do comando** *(1 min por rodada)*
O professor exibe o comando no slide — sem marcação de erro.

2. **Votação** *(1 min)*
A turma decide: **CERTO ✅ ou ERRADO ❌** — ou **PERIGOSO ⚠️** (sintaticamente correto mas arriscado). O professor registra os votos.

3. **Justificativa obrigatória** *(2 min)*
Quem votou ❌ ou ⚠️ aponta o problema e explica o risco. Sem justificativa o ponto não conta.

4. **Reveal e consolidação** *(1 min)*
O professor revela a classificação correta e reforça a boa prática correspondente.

**Blocos sugeridos (4 rodadas):**

| Rodada | Comando | Classificação | Problema |
|--------|---------|---------------|----------|
| 1 | `UPDATE cliente SET cidade_cliente = 'Curitiba' WHERE cpf = '12345678901';` | ✅ Certo | Sintaxe correta com WHERE preciso — altera apenas um registro |
| 2 | `DELETE FROM locacao;` | ⚠️ Perigoso | Sintaticamente correto mas sem WHERE — apaga TODAS as locações do banco |
| 3 | `UPDATE filme SET genero = 'Ação' WHERE ano >= 2020 AND genero = 'Aventura';` | ✅ Certo | WHERE com duas condições — altera apenas os registros esperados |
| 4 | `DELETE FROM cliente WHERE cidade_cliente = 'São Paulo'; ` | ⚠️ Perigoso | Sintaticamente correto, mas deleta todos os clientes de São Paulo — sem verificar se têm locações ativas · pode violar FK se houver FOREIGN KEY com restrição |

> **Nota:** introduzir a categoria ⚠️ Perigoso é intencional — desenvolve nos alunos a percepção de que código tecnicamente correto pode causar danos graves em produção. Reforçar que profissionais experientes sempre fazem um SELECT com o mesmo WHERE antes de executar qualquer UPDATE ou DELETE.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 32 — 14/10/2026 · Views — Criando Visões do Banco |
| Próxima aula → | SA 34 — 28/10/2026 · Documentação de Código SQL — Comentários |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Quadro branco e marcador

---

## Observações do Professor
