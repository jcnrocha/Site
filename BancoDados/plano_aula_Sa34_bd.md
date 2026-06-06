# UC: Fundamentos de Banco de Dados
## SA 34 — 3º Trimestre

---

## Tema

Documentação de Código SQL — Comentários

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é documentação de código e por que ela é essencial no trabalho em equipe e na manutenção de sistemas
- Utilizar comentários de linha (`--`) e comentários de bloco (`/* */`) na linguagem SQL
- Aplicar boas práticas de documentação em comandos `CREATE TABLE`, `INSERT`, `SELECT` e `UPDATE`
- Diferenciar código bem documentado de código sem documentação — reconhecendo o impacto na manutenção
- Documentar o banco de dados da locadora utilizado ao longo do trimestre aplicando os padrões aprendidos

**Habilidade da matriz:** H08 — Empregar comentários para documentação do código fonte

---

## Conteúdo

- O que é documentação de código — definição, propósito e impacto na vida real do desenvolvedor
- Por que documentar código SQL: bancos de dados são mantidos por anos · equipes mudam · comentários explicam o "porquê", não apenas o "o quê"
- Tipos de comentário em SQL:
  - **Comentário de linha** — inicia com `--` e vai até o fim da linha:
    ```sql
    -- Seleciona todos os clientes ativos de Curitiba
    SELECT nome, email FROM cliente
    WHERE cidade_cliente = 'Curitiba'; -- filtro por cidade
    ```
  - **Comentário de bloco** — abre com `/*` e fecha com `*/` · pode ocupar múltiplas linhas:
    ```sql
    /*
      Autor: Prof. Julio Cesar
      Data: 28/10/2026
      Descrição: View de histórico completo de locações
      Tabelas: cliente, locacao, filme
    */
    CREATE VIEW vw_historico_locacoes AS
    SELECT c.nome, f.titulo, l.data_locacao
    FROM cliente c
    INNER JOIN locacao l ON c.cpf = l.cpf_cliente
    INNER JOIN filme f   ON l.id_filme = f.id_filme;
    ```
- Boas práticas de documentação em SQL:
  - Documentar o propósito de cada tabela no CREATE TABLE
  - Explicar restrições não óbvias (ex: por que esse campo é UNIQUE)
  - Documentar Views e consultas complexas com cabeçalho de autor, data e descrição
  - Usar comentários em UPDATEs e DELETEs para registrar o motivo da alteração
  - Evitar comentários óbvios que apenas repetem o código — comentar o raciocínio, não a sintaxe
- O que NÃO é boa documentação:
  - `-- seleciona nome` acima de `SELECT nome` — não acrescenta nada
  - Comentários desatualizados que contradizem o código — pior do que não ter comentário
- Documentação de `CREATE TABLE` com comentários por coluna:
  ```sql
  CREATE TABLE produto (
      id_produto INT PRIMARY KEY AUTO_INCREMENT, -- identificador único gerado automaticamente
      nome       VARCHAR(100) NOT NULL,          -- nome do produto, obrigatório
      preco      DECIMAL(8,2) NOT NULL,          -- preço de venda com até 2 casas decimais
      estoque    INT DEFAULT 0,                  -- quantidade em estoque, começa zerado
      ativo      BOOLEAN DEFAULT TRUE            -- FALSE quando o produto é descontinuado
  );
  ```
- Como comentários ajudam em auditorias, revisões de código e onboarding de novos membros da equipe

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 33 — pergunta oral: *"Por que é perigoso executar um DELETE sem WHERE?"* |
| Retomada | Professor projeta um script SQL longo sem nenhum comentário e pergunta: *"Se esse banco fosse entregue para vocês hoje, quanto tempo levariam para entender o que cada parte faz?"* — alunos percebem o problema · introdução natural à documentação |
| Explicação | Slides — o que é documentação de código, comentário de linha e de bloco, boas práticas, exemplos em CREATE TABLE, View e SELECT, o que evitar |
| Dinâmica | "Documenta esse Código" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: `--` para linha · `/* */` para bloco · documentar o porquê, não o óbvio · Próxima aula: Projeto Integrador |

---

## Dinâmica — "Documenta esse Código"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** fixar as boas práticas de documentação SQL por meio da adição de comentários a blocos de código já conhecidos — desenvolvendo o hábito de documentar o raciocínio técnico, e não apenas a sintaxe.

**Materiais:** slide ou folha com os blocos de código sem comentários · folha A4 por grupo para escrever a versão documentada.

**Passo a passo:**

1. **Distribuição do bloco** *(1 min)*
Cada grupo recebe um bloco de código SQL sem comentários — extraído do banco da locadora trabalhado ao longo do trimestre.

2. **Documentação em grupo** *(9 min)*
O grupo adiciona comentários de linha e/ou de bloco ao código, explicando: o que cada parte faz, por que as restrições foram escolhidas e qual o propósito do bloco como um todo.

3. **Apresentação e debate** *(5 min)*
Cada grupo lê seus comentários em voz alta. O professor e a turma avaliam: os comentários explicam o raciocínio ou apenas repetem o código?

**Blocos sugeridos por grupo:**

| Grupo | Bloco para documentar |
|-------|----------------------|
| A | `CREATE TABLE locacao (id_locacao INT PRIMARY KEY AUTO_INCREMENT, cpf_cliente CHAR(11) NOT NULL, id_filme INT NOT NULL, data_locacao DATE NOT NULL DEFAULT (CURRENT_DATE), FOREIGN KEY (cpf_cliente) REFERENCES cliente(cpf), FOREIGN KEY (id_filme) REFERENCES filme(id_filme));` |
| B | `CREATE VIEW vw_filmes_por_genero AS SELECT genero, COUNT(*) AS total FROM filme GROUP BY genero;` |
| C | `SELECT c.nome, COUNT(*) AS total_locacoes FROM cliente c INNER JOIN locacao l ON c.cpf = l.cpf_cliente GROUP BY c.nome ORDER BY total_locacoes DESC;` |
| D | `UPDATE filme SET genero = 'Clássico' WHERE ano < 1990;` |

> **Nota:** reforçar que não existe uma única resposta correta para a documentação — o critério de avaliação é se o comentário agrega informação útil para quem vai ler o código no futuro. Comentários que apenas traduzem a sintaxe para português não são bem-vindos.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 33 — 21/10/2026 · SQL DML Avançado — UPDATE e DELETE |
| Próxima aula → | SA 35 — 04/11/2026 · Projeto Integrador — Banco de Dados Completo |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Folha A4 por grupo (para escrever a versão documentada dos blocos)
- Quadro branco e marcador

---

## Observações do Professor
