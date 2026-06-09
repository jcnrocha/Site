# UC: Fundamentos de Redes de Computadores
## Aula 20 — 2º Trimestre

---

## Tema

Protocolos de Aplicação — HTTP, DNS, DHCP e FTP

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o funcionamento do protocolo HTTP e HTTPS — entendendo o que acontece entre o navegador e o servidor a cada requisição
- Identificar o papel do DNS na resolução de nomes de domínio — entendendo como um endereço como "google.com" vira um endereço IP
- Reconhecer o funcionamento do DHCP — como um dispositivo recebe automaticamente suas configurações de rede ao se conectar
- Diferenciar FTP de SFTP — entendendo quando cada um é indicado e por que a segurança importa na transferência de arquivos
- Relacionar cada protocolo de aplicação com situações reais do desenvolvimento de sistemas e da infraestrutura de redes

**Habilidade da matriz:** H4 — Identificar tipos e tecnologias de conexão a redes de computadores

---

## Conteúdo

- Retomada rápida da Aula 19: camada de Aplicação do modelo TCP/IP — onde os protocolos de hoje vivem
- **HTTP — HyperText Transfer Protocol**
  - O que é: protocolo de comunicação entre navegador (cliente) e servidor web
  - Como funciona: modelo requisição × resposta (Request / Response)
  - Métodos HTTP principais:

| Método | Função | Exemplo de uso |
|--------|--------|---------------|
| GET | Solicita um recurso do servidor | Abrir uma página web |
| POST | Envia dados ao servidor | Enviar um formulário de cadastro |
| PUT | Atualiza um recurso existente | Editar um perfil de usuário |
| DELETE | Remove um recurso | Excluir um registro |

  - Códigos de status HTTP:

| Código | Significado | Exemplo |
|--------|-------------|---------|
| 200 | OK — requisição bem-sucedida | Página carregada com sucesso |
| 301 | Redirecionamento permanente | Site mudou de endereço |
| 404 | Not Found — recurso não encontrado | Página inexistente |
| 500 | Internal Server Error — erro no servidor | Bug na aplicação do servidor |

  - **HTTPS** — HTTP com camada de segurança TLS/SSL
    - Criptografia dos dados em trânsito — ninguém no caminho consegue ler o conteúdo
    - Certificado digital: como o navegador confirma que o site é legítimo
    - Por que todo site moderno deve usar HTTPS — impacto no SEO e na confiança do usuário
    - Porta padrão: HTTP → 80 · HTTPS → 443

- **DNS — Domain Name System**
  - O que é: sistema que traduz nomes de domínio em endereços IP
  - Analogia: agenda telefônica da internet — você digita o nome, ele devolve o número
  - Como funciona a resolução DNS passo a passo:
    1. Usuário digita `www.senai.br` no navegador
    2. O computador consulta o cache local — já sabe o IP?
    3. Se não, consulta o servidor DNS configurado (geralmente do provedor ou 8.8.8.8)
    4. O servidor DNS consulta os servidores raiz → TLD (.br) → autoritativo
    5. Retorna o IP correspondente → navegador conecta ao servidor
  - DNS público: Google (8.8.8.8 / 8.8.4.4), Cloudflare (1.1.1.1)
  - Porta padrão: 53 (UDP para consultas, TCP para transferências de zona)

- **DHCP — Dynamic Host Configuration Protocol**
  - O que é: protocolo que atribui automaticamente configurações de rede a um dispositivo
  - O que o DHCP fornece: endereço IP, máscara de sub-rede, gateway padrão e servidor DNS
  - Como funciona — processo DORA:
    1. **D**iscover — cliente envia broadcast procurando um servidor DHCP
    2. **O**ffer — servidor oferece uma configuração de IP disponível
    3. **R**equest — cliente aceita a oferta e solicita formalmente
    4. **A**cknowledge — servidor confirma e registra a concessão (lease)
  - Tempo de concessão (lease time): por que o IP pode mudar após um período
  - Porta padrão: 67 (servidor) e 68 (cliente) — protocolo UDP

- **FTP — File Transfer Protocol**
  - O que é: protocolo para transferência de arquivos entre cliente e servidor
  - Como funciona: duas conexões — canal de controle (porta 21) e canal de dados (porta 20)
  - Modos: ativo e passivo — diferença e quando cada um é usado
  - Limitação crítica: dados trafegam sem criptografia — usuário, senha e arquivos visíveis na rede
  - **SFTP (SSH File Transfer Protocol)**
    - Transferência de arquivos com criptografia via SSH — porta 22
    - Substituto seguro do FTP — padrão atual para ambientes profissionais
  - **FTPS** — FTP com TLS/SSL · diferença em relação ao SFTP
  - Ferramentas comuns: FileZilla, WinSCP, Cyberduck

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 19: *"Vimos TCP e UDP como protocolos de transporte — hoje subimos uma camada e vemos os protocolos que as aplicações usam diretamente"* |
| Retomada | Professor pergunta: *"Quando você digita 'google.com' no navegador e a página abre, o que você acha que acontece nos bastidores entre o seu computador e o servidor do Google?"* — alunos respondem livremente |
| Explicação | Slides — HTTP/HTTPS (requisição × resposta, métodos, status codes, TLS), DNS (resolução passo a passo, servidores públicos), DHCP (processo DORA), FTP × SFTP |
| Dinâmica | "O Que Está Acontecendo na Rede?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: HTTP/HTTPS para web · DNS traduz nomes em IPs · DHCP configura dispositivos automaticamente · FTP transfere arquivos, SFTP faz isso com segurança · Próxima aula: Segurança Básica em Redes |

---

## Dinâmica — "O Que Está Acontecendo na Rede?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver a capacidade de identificar qual protocolo de aplicação está em uso em cada situação do cotidiano digital, conectando o conteúdo teórico com o que realmente acontece por baixo das aplicações que os alunos usam todos os dias — e que desenvolvedores de sistemas precisam entender para construir e depurar suas aplicações.

**Materiais:** cartões com situações — um conjunto por grupo · ou slide com as situações projetadas.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com situações do cotidiano digital. O desafio é identificar qual protocolo de aplicação está envolvido e o que ele está fazendo naquela situação.

2. **Análise em grupo** *(8 min)*
O grupo discute cada situação: qual protocolo, qual porta, e o que acontece nos bastidores.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça o funcionamento de cada protocolo.

**Situações sugeridas:**

| Situação | Protocolo | O que acontece nos bastidores |
|----------|-----------|-------------------------------|
| Você digita "www.senai.br" e a página abre | DNS + HTTP/HTTPS | DNS resolve o nome · HTTPS busca a página no servidor (porta 443) |
| Seu celular conecta ao Wi-Fi e recebe um IP automaticamente | DHCP | Processo DORA · servidor atribui IP, máscara, gateway e DNS |
| Desenvolvedor faz upload de arquivos para o servidor de produção | SFTP | Transferência segura via SSH (porta 22) |
| Navegador exibe um cadeado verde ao lado da URL | HTTPS + TLS | Certificado digital validado · dados criptografados em trânsito |
| Página retorna erro 404 ao acessar um link quebrado | HTTP | Servidor respondeu: recurso não encontrado |
| Sistema faz login em servidor FTP sem criptografia | FTP | Usuário e senha trafegam em texto puro — vulnerável a interceptação |
| Aplicação consulta qual IP corresponde a "api.github.com" | DNS | Resolução de nome · resposta com o IP do servidor da API |
| Formulário de cadastro envia dados para o servidor | HTTP POST | Método POST envia os dados do formulário ao servidor via HTTPS |

> **Nota:** o objetivo é desenvolver o raciocínio: *"toda ação digital usa um protocolo por baixo — saber qual protocolo está em jogo ajuda a entender, depurar e construir sistemas melhores."* Reforçar que desenvolvedores trabalham diretamente com HTTP ao construir APIs REST, com DNS ao configurar domínios e com SFTP ao fazer deploy de aplicações.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 19 — 24/06/2026 · Protocolos de Rede — TCP/IP e UDP |
| Próxima aula → | Aula 21 — 08/07/2026 · Segurança Básica em Redes |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões com as situações da dinâmica impressos (1 conjunto por grupo) ou slide com as situações
- Se possível: demonstração ao vivo — abrir o DevTools do navegador (F12 → aba Network) e mostrar as requisições HTTP/HTTPS sendo feitas ao carregar uma página

---

## Observações do Professor
