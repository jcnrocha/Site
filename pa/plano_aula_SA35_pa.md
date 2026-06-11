# UC: Programação de Aplicativos
## SA 35 — 3º Trimestre

---

## Tema

Projeto Final — Desenvolvimento Parte 2

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Completar o CRUD completo do sistema com UPDATE e DELETE usando Prepared Statement
- Implementar tratamento de erros robusto em todas as operações com banco de dados
- Documentar o código-fonte com Javadoc/docstring em todos os métodos públicos
- Escrever testes unitários para os módulos principais do sistema
- Manter o repositório atualizado com commits descritivos a cada avanço

**Capacidades da matriz:** Integração de todas as capacidades da UC · Integrar banco de dados por meio da linguagem de programação · Empregar comentários para documentação · Utilizar a IDE para aplicação de teste unitário

---

## Conteúdo

- Contextualização: *"Na SA passada a estrutura e os primeiros módulos foram criados — hoje completamos o CRUD, tratamos os erros, documentamos e escrevemos os primeiros testes. O sistema começa a tomar forma profissional"*

- **O que deve ser entregue ao final desta SA:**

  | Entregável | Descrição |
  |------------|-----------|
  | CRUD completo | INSERT · SELECT (com e sem filtro) · UPDATE · DELETE — todos com Prepared Statement |
  | Tratamento de erros | try/catch em todas as operações de banco · mensagens de erro informativas |
  | Documentação | Javadoc/docstring em todos os métodos públicos das classes model e DAO |
  | Testes unitários | Ao menos 5 testes cobrindo métodos das classes de modelo e regras de negócio |
  | Repositório | Ao menos 4 commits descritivos com o progresso da SA |

- **Checklist de CRUD completo:**
  - [ ] INSERT com Prepared Statement e commit
  - [ ] SELECT sem filtro — retorna todos os registros
  - [ ] SELECT com WHERE — filtra por ID ou outro campo relevante
  - [ ] UPDATE com WHERE obrigatório e verificação de `rowcount`
  - [ ] DELETE com WHERE obrigatório e confirmação de exclusão
  - [ ] Transação aplicada onde duas operações dependem uma da outra

- **Tratamento de erros — padrão mínimo esperado:**

  ```java
  // Padrão mínimo para cada método DAO
  public void atualizar(Cliente cliente) {
      String sql = "UPDATE clientes SET nome = ?, email = ? WHERE id = ?";
      try (PreparedStatement ps = ConexaoDB.getConexao().prepareStatement(sql)) {
          ps.setString(1, cliente.getNome());
          ps.setString(2, cliente.getEmail());
          ps.setInt(3, cliente.getId());

          int linhasAfetadas = ps.executeUpdate();
          if (linhasAfetadas == 0) {
              System.out.println("Nenhum registro atualizado — ID não encontrado");
          }
      } catch (SQLException e) {
          System.err.println("Erro ao atualizar cliente: " + e.getMessage());
      }
  }
  ```

- **Documentação — padrão mínimo esperado:**

  ```java
  /**
   * Atualiza os dados de um cliente existente no banco.
   *
   * @param cliente objeto Cliente com os dados atualizados e o ID preenchido
   */
  public void atualizar(Cliente cliente) { ... }

  /**
   * Remove um cliente pelo ID.
   *
   * @param id identificador único do cliente a ser removido
   * @return true se o cliente foi removido · false se o ID não foi encontrado
   */
  public boolean remover(int id) { ... }
  ```

- **Testes unitários — o que testar nesta SA:**
  - Métodos das classes de modelo: getters, setters com validação, construtores
  - Regras de negócio: cálculos, validações, classificações
  - **Não** testar métodos DAO diretamente — usam banco de dados real · devem ser testados com mock (avançado)

  ```java
  // Exemplos de testes para o modelo — sem dependência de banco
  @Test
  void deveCalcularTotalComDescontoCorretamente() { ... }

  @Test
  void naoDeveAceitarEmailSemArroba() { ... }

  @Test
  void deveLancarExcecaoQuandoNomeForVazio() { ... }

  @Test
  void deveRetornarSituacaoCorretaParaCadaNivel() { ... }

  @Test
  void deveAplicarDescontoZeroQuandoPercentualForZero() { ... }
  ```

- **Erros frequentes nesta fase — orientações preventivas:**

  | Erro frequente | Como evitar |
  |---------------|-------------|
  | UPDATE sem WHERE atualiza tudo | Sempre verificar que o WHERE está presente antes de executar |
  | DELETE sem WHERE remove tudo | Mesma orientação — WHERE é obrigatório |
  | Testes testando apenas o cenário feliz | Incluir ao menos um cenário de borda ou erro em cada método |
  | Documentação copiada e colada sem ajustar | Cada método tem sua própria descrição — não copiar de outro método |
  | Commits com código com erros de compilação | Commitar apenas código que compila — nunca subir código quebrado |

- **Orientações de qualidade para esta SA:**
  - Revisar o código da SA 34 antes de continuar — corrigir problemas identificados pelo professor
  - Aplicar DRY: se dois métodos DAO têm código de abertura de conexão duplicado, extrair para `ConexaoDB`
  - Verificar se todos os atributos estão `private` — nenhum atributo público em nenhuma classe
  - Commitar ao terminar cada método que funciona — não acumular para o final

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · feedback rápido do professor sobre o progresso da SA 34 de cada grupo · orientações específicas para esta SA |
| Revisão por grupo | Professor passa rapidamente com cada grupo revisando o que foi entregue na SA 34 e orientando o foco desta SA |
| Desenvolvimento orientado | Grupos desenvolvem com suporte do professor · prioridade: completar CRUD → tratar erros → documentar → testar |
| Checkpoint intermediário | A 20 minutos do fim o professor verifica o progresso de cada grupo e orienta quem está travado |
| Fechamento | Commit final com o progresso da SA · professor atualiza a ficha de acompanhamento de cada grupo |

---

## Acompanhamento do Projeto — Ficha de Progresso SA 35

| Grupo | CRUD completo | Tratamento de erros | Documentação | Testes (qtd) | Commits | Observações |
|-------|--------------|--------------------|--------------|--------------|---------|----|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

---

## Avaliação

- Avaliação formativa contínua ao longo do desenvolvimento
- Critérios verificados ao final desta SA:
  - CRUD completo funcionando com Prepared Statement
  - Tratamento de erros em todos os métodos DAO
  - Javadoc/docstring nos métodos públicos
  - Ao menos 5 testes unitários passando
  - Repositório com ao menos 4 commits descritivos
- Avaliação somativa será aplicada na SA 38 (apresentação) e SA 39 (avaliação do 3º Trimestre)

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 34 — 21/10/2026 · Projeto Final — Desenvolvimento Parte 1 |
| Próxima SA → | SA 36 — 04/11/2026 · Projeto Final — Desenvolvimento Parte 3 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Computadores com VS Code, SGBD e acesso ao GitHub
- Ficha de acompanhamento atualizada da SA 34
- Quadro branco e marcador

---

## Observações do Professor
