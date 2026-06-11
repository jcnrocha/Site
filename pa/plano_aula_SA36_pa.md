# UC: Programação de Aplicativos
## SA 36 — 3º Trimestre

---

## Tema

Projeto Final — Desenvolvimento Parte 3

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Integrar todos os módulos do sistema em um fluxo funcional completo e coeso
- Refatorar o código aplicando DRY, otimização e boas práticas de nomenclatura
- Garantir rastreabilidade do sistema com logs nos pontos críticos da aplicação
- Realizar ajustes finais de interface e experiência de uso do sistema
- Entregar o sistema completo no repositório com histórico de commits rastreável e README atualizado

**Capacidades da matriz:** Integração de todas as capacidades da UC · Aplicar métodos e técnicas de programação · Utilizar a IDE para rastreabilidade do código · Gestão da Qualidade

---

## Conteúdo

- Contextualização: *"Nas duas últimas SAs construímos a estrutura e o CRUD — hoje integramos tudo, refinamos a qualidade e entregamos o sistema funcionando de ponta a ponta. Esta é a última SA de desenvolvimento antes das apresentações"*

- **O que deve ser entregue ao final desta SA:**

  | Entregável | Descrição |
  |------------|-----------|
  | Sistema integrado | Todos os módulos funcionando juntos sem erros críticos |
  | Refatoração aplicada | DRY · nomes descritivos · sem código morto · sem atributos públicos |
  | Logs implementados | Ao menos INFO e ERROR nos pontos críticos do sistema |
  | Testes passando | Todos os testes da SA 35 continuam passando após as alterações |
  | README completo | Descrição do sistema · como instalar · como rodar · integrantes |
  | Repositório final | Histórico de commits limpo e descritivo · todos os membros com commits |

- **Integração dos módulos — checklist:**
  - [ ] Fluxo principal do sistema funciona do início ao fim sem travar
  - [ ] Todas as operações CRUD acessíveis pelo usuário
  - [ ] Mensagens de feedback ao usuário para cada operação (sucesso e erro)
  - [ ] Nenhum `NullPointerException` não tratado em nenhum fluxo testado
  - [ ] Sistema se conecta ao banco e opera normalmente ao ser iniciado do zero

- **Refatoração final — checklist de qualidade:**
  - [ ] Nenhum método com mais de 30 linhas — dividir se necessário
  - [ ] Nenhuma lógica duplicada — extraída para método ou classe utilitária
  - [ ] Todos os atributos `private` — nenhum acesso direto fora da classe
  - [ ] Nomes de variáveis, métodos e classes descritivos — sem `x`, `tmp`, `obj`
  - [ ] Nenhum código comentado desnecessariamente no repositório
  - [ ] Formatação aplicada em todos os arquivos

- **Rastreabilidade com logs — implementação mínima:**

  ```java
  // Pontos onde logs devem estar presentes no sistema final
  import java.util.logging.Logger;
  Logger logger = Logger.getLogger(NomeDaClasse.class.getName());

  // Ao iniciar a aplicação
  logger.info("Sistema iniciado com sucesso");

  // Ao realizar operação bem-sucedida
  logger.info("Cliente inserido: " + cliente.getNome());

  // Ao detectar situação inesperada mas não crítica
  logger.warning("Tentativa de busca com ID inválido: " + id);

  // Ao capturar exceção grave
  logger.severe("Erro ao conectar ao banco: " + e.getMessage());
  ```

- **README final — estrutura mínima esperada:**

  ```markdown
  # Nome do Sistema

  ## Descrição
  Breve descrição do que o sistema faz e qual problema resolve.

  ## Integrantes
  - Nome 1
  - Nome 2
  - Nome 3

  ## Tecnologias utilizadas
  - Linguagem: Java / Python
  - Banco de dados: MySQL / SQLite
  - IDE: VS Code

  ## Como instalar e rodar
  1. Clonar o repositório: `git clone <url>`
  2. Importar o script SQL: `sql/schema.sql`
  3. Configurar as credenciais em `ConexaoDB.java`
  4. Executar o arquivo principal: `Main.java`

  ## Funcionalidades
  - Cadastro de [entidade principal]
  - Consulta e filtro por [campo]
  - Atualização e remoção de registros
  ```

- **Testes de regressão antes da entrega:**
  - Reexecutar todos os testes unitários após as refatorações
  - Se algum teste falhou com a refatoração: corrigir o código, não o teste
  - Verificar a cobertura — não deve ter diminuído em relação à SA 35

- **Orientações finais de qualidade do repositório:**
  - Verificar que todos os membros têm commits — contribuição individual rastreável
  - Último commit deve ser: `"versão final — sistema completo e funcional"`
  - Não commitar arquivos de configuração local (`.env`, senhas, caminhos absolutos)
  - Verificar o `.gitignore` — pasta `target/`, `__pycache__/`, arquivos de IDE

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · feedback rápido do professor sobre o progresso da SA 35 · orientações e prioridades para esta SA de entrega |
| Revisão por grupo | Professor passa com cada grupo verificando o que falta para o sistema estar completo · define prioridades claras para o tempo da SA |
| Desenvolvimento e refatoração | Grupos trabalham na integração, refatoração e logs · professor circula auxiliando nos pontos críticos |
| Checkpoint de qualidade | A 25 minutos do fim: cada grupo executa o fluxo completo do sistema ao vivo para o professor · professor verifica e registra o status final |
| Commit final e fechamento | Commit final com tag de versão · README revisado · professor registra a entrega de cada grupo |

---

## Acompanhamento do Projeto — Ficha de Status Final de Desenvolvimento

| Grupo | Sistema integrado | Refatorado | Logs | Testes passando | README | Todos com commits | Status final |
|-------|------------------|------------|------|----------------|--------|-------------------|-------------|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |

---

## Avaliação

- Avaliação formativa — entrega técnica verificada ao final desta SA
- Critérios verificados:
  - Sistema funcionando de ponta a ponta sem erros críticos
  - Refatoração aplicada (DRY, nomenclatura, sem código morto)
  - Logs nos pontos críticos
  - Todos os testes passando após refatoração
  - README completo e repositório com histórico rastreável
- Avaliação somativa aplicada na SA 38 (apresentação) e SA 39 (avaliação do 3º Trimestre)

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 35 — 28/10/2026 · Projeto Final — Desenvolvimento Parte 2 |
| Próxima SA → | SA 37 — 11/11/2026 · Projeto Final — Canvas e Preparação da Apresentação |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Computadores com VS Code, SGBD e acesso ao GitHub
- Ficha de acompanhamento atualizada das SAs 34 e 35
- Quadro branco e marcador

---

## Observações do Professor
