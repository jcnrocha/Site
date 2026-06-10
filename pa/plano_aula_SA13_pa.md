# UC: Programação de Aplicativos
## SA 13 — 1º Trimestre

---

## Tema

Conexão com Banco de Dados — Introdução

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o papel do banco de dados em um sistema de software e por que a integração com a aplicação é essencial
- Identificar os principais drivers e conectores utilizados para conectar uma aplicação ao banco de dados
- Configurar uma conexão com banco de dados na IDE, informando os parâmetros necessários
- Executar o primeiro comando SELECT via código, recuperando dados do banco e exibindo no console
- Reconhecer o fluxo completo de uma requisição ao banco de dados: aplicação → driver → SGBD → retorno

**Capacidades da matriz:** 5. Conexão com banco de dados · Integrar banco de dados por meio da linguagem de programação · Aplicar linguagem de programação por meio do ambiente integrado de desenvolvimento (IDE)

---

## Conteúdo

- Retomada da SA 12: *"Encerramos o 1º Trimestre com OO consolidada — agora no 2º Trimestre o sistema começa a se conectar com o mundo real: vamos integrar nossa aplicação com um banco de dados"*

- **Por que integrar aplicação com banco de dados:**
  - Aplicações sem banco de dados perdem todos os dados quando o programa é encerrado — os dados vivem apenas na memória RAM durante a execução
  - Com banco de dados: os dados são persistidos em disco · podem ser consultados, atualizados e compartilhados entre múltiplos usuários e sessões
  - Todo sistema profissional real usa banco de dados: e-commerce, sistema de RH, aplicativo de delivery, sistema escolar

- **Componentes da integração aplicação × banco de dados:**

  | Componente | Função |
  |------------|--------|
  | **Aplicação** | Código que solicita operações ao banco (SELECT, INSERT, UPDATE, DELETE) |
  | **Driver / Conector** | Biblioteca que traduz as chamadas da aplicação para o protocolo do SGBD |
  | **SGBD** | Sistema Gerenciador de Banco de Dados — processa as operações e retorna os resultados |
  | **Banco de dados** | Onde os dados estão armazenados em tabelas |

- **Fluxo de uma requisição ao banco de dados:**
  ```
  Aplicação (código Java/Python)
       ↓  chama o driver
  Driver (JDBC / psycopg2 / mysql-connector)
       ↓  envia SQL pelo protocolo do SGBD
  SGBD (MySQL / PostgreSQL / SQLite)
       ↓  processa e retorna resultado
  Aplicação recebe os dados e os utiliza
  ```

- **Principais drivers e conectores:**

  | Linguagem | Banco de Dados | Driver / Conector | Como adicionar |
  |-----------|---------------|-------------------|----------------|
  | Java | MySQL | JDBC MySQL Connector | Dependência Maven / JAR externo |
  | Java | PostgreSQL | JDBC PostgreSQL | Dependência Maven |
  | Python | MySQL | mysql-connector-python | `pip install mysql-connector-python` |
  | Python | PostgreSQL | psycopg2 | `pip install psycopg2` |
  | Python | SQLite | sqlite3 | Nativo — sem instalação |
  | JavaScript | MySQL | mysql2 | `npm install mysql2` |

- **Parâmetros necessários para a conexão:**
  - **Host:** endereço do servidor onde o banco está rodando · `localhost` para banco local
  - **Porta:** porta de comunicação do SGBD · MySQL: `3306` · PostgreSQL: `5432` · SQLite: não usa porta
  - **Nome do banco:** qual banco de dados usar dentro do SGBD
  - **Usuário:** login de acesso ao banco
  - **Senha:** senha do usuário

- **Configurando a conexão no código:**

  ```java
  // Exemplo Java com JDBC + MySQL
  String url = "jdbc:mysql://localhost:3306/escola";
  String usuario = "root";
  String senha = "1234";

  Connection conexao = DriverManager.getConnection(url, usuario, senha);
  exibir("Conexão estabelecida com sucesso!");
  ```

  ```python
  # Exemplo Python com mysql-connector
  import mysql.connector

  conexao = mysql.connector.connect(
      host="localhost",
      port=3306,
      database="escola",
      user="root",
      password="1234"
  )
  print("Conexão estabelecida com sucesso!")
  ```

- **Primeiro SELECT via código:**
  - Após estabelecer a conexão, o próximo passo é consultar dados com um comando SQL
  - O resultado é retornado como um objeto que pode ser percorrido linha por linha

  ```java
  // Java
  Statement stmt = conexao.createStatement();
  ResultSet rs = stmt.executeQuery("SELECT nome, nota FROM alunos");

  while (rs.next()) {
      exibir("Nome: " + rs.getString("nome") + " | Nota: " + rs.getDouble("nota"));
  }
  ```

  ```python
  # Python
  cursor = conexao.cursor()
  cursor.execute("SELECT nome, nota FROM alunos")

  for (nome, nota) in cursor:
      print(f"Nome: {nome} | Nota: {nota}")
  ```

- **Boas práticas desde o início:**
  - Sempre fechar a conexão após o uso — conexões abertas desnecessariamente consomem recursos do servidor
  - Nunca colocar senha diretamente no código que vai para o repositório — usar variáveis de ambiente ou arquivos de configuração separados
  - Tratar erros de conexão com try/catch — banco indisponível não deve derrubar a aplicação inteira

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · contextualização do 2º Trimestre: *"Até agora o programa funcionava na memória — a partir de hoje os dados passam a persistir. Isso muda tudo."* |
| Retomada | Professor pergunta: *"Quando vocês fecham um aplicativo e reabrem, os dados continuam lá. Como isso é possível se o programa estava na memória RAM?"* — alunos respondem livremente · professor conecta com banco de dados como camada de persistência |
| Explicação | Slides — por que integrar com BD, componentes da integração, fluxo da requisição, drivers e conectores, parâmetros de conexão, primeiro SELECT via código · demonstração ao vivo na IDE com banco MySQL ou SQLite |
| Dinâmica | "Liga os Pontos" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: driver é o tradutor entre a aplicação e o SGBD · conexão precisa de host, porta, banco, usuário e senha · SELECT via código retorna dados que podem ser percorridos · Próxima SA: CRUD — INSERT e SELECT |

---

## Dinâmica — "Liga os Pontos"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** fixar o fluxo de integração entre aplicação e banco de dados por meio do mapeamento de componentes e da identificação de erros de configuração de conexão — desenvolvendo o raciocínio de diagnóstico que o desenvolvedor usa quando a conexão falha.

**Materiais:** slide com o diagrama de fluxo e os cenários de erro projetados · ficha de diagnóstico impressa (1 por grupo).

**Passo a passo:**

1. **Mapeamento do fluxo** *(5 min)*
O professor projeta o diagrama de fluxo com os componentes fora de ordem (Aplicação · Driver · SGBD · Banco de Dados). Os grupos organizam o fluxo correto e descrevem o papel de cada componente com suas próprias palavras.

2. **Diagnóstico de erros** *(7 min)*
O professor projeta 4 mensagens de erro reais de conexão. Os grupos identificam qual parâmetro está errado em cada caso e sugerem a correção.

3. **Apresentação** *(3 min)*
Os grupos apresentam os diagnósticos. O professor confirma e complementa com dicas práticas de debugging de conexão.

**Mensagens de erro para diagnosticar:**

| Mensagem de erro | Parâmetro com problema | Correção sugerida |
|-----------------|----------------------|-------------------|
| `Unknown database 'escolas'` | Nome do banco incorreto | Verificar o nome exato do banco criado no SGBD |
| `Access denied for user 'root'@'localhost'` | Usuário ou senha incorretos | Verificar credenciais no SGBD |
| `Communications link failure` | Host ou porta incorretos | Verificar se o SGBD está rodando e se host/porta estão corretos |
| `Loading class 'com.mysql.jdbc.Driver' failed` | Driver não adicionado ao projeto | Adicionar o JAR do driver MySQL ao projeto |

> **Nota:** reforçar que erros de conexão são extremamente comuns no mercado — todo desenvolvedor já ficou travado por horas por causa de um parâmetro errado. Saber diagnosticar esses erros rapidamente é uma habilidade prática valiosa que começa com entender o que cada parâmetro faz.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 12 — 06/05/2026 · Linguagem de Programação Orientada a Objetos — Consolidação |
| Próxima SA → | SA 14 — 20/05/2026 · Conexão com Banco de Dados — CRUD Parte 1 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code e SGBD instalado (MySQL ou SQLite recomendado)
- Driver/conector da linguagem configurado no projeto de demonstração
- Ficha de diagnóstico impressa (1 por grupo) ou slide projetado
- Quadro branco e marcador

---

## Observações do Professor
