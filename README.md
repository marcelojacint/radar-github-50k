# Radar de IA do GitHub — repositórios com 20 mil+ estrelas

Todo dia, às 06:17 (horário de Brasília), uma **tarefa agendada do Claude**:

1. busca **todos os repositórios open source com 20 mil estrelas ou mais** (hoje são ~2.290, sem contar os arquivados);
2. separa o **foco**: IA para construir e entregar software, como agentes, skills, agentes de código, MCP, LLMs e RAG, além de IA aplicada a design, segurança e dados (hoje são ~365). Os demais ficam no catálogo geral, por categoria técnica;
3. compara com o dia anterior e marca os **novos**, os que **saíram** e os que **mais cresceram**;
4. explica cada repositório do foco: **o que é**, **por que importa** e **em quais áreas de entrega** ajuda (arquitetura, engenharia, design, frontend, backend, banco de dados, segurança, testes e DevOps), com relevância e um uso concreto;
5. salva tudo neste próprio repositório e abre uma **issue** quando aparece novidade no foco (o GitHub te avisa por e-mail ou no app).

O repositório serve só para guardar e versionar os resultados. Quem faz o trabalho é o Claude, sem chave de API e sem custo extra além do seu plano.

## Onde fica salvo

| Arquivo | O que guarda | Por que existe |
|---|---|---|
| `data/repos.json` | Base completa: estrelas, linguagem, licença, tópicos, data em que entrou | É a "memória" entre execuções; sem ela não dá para saber o que é novo |
| `data/explicacoes.json` | Cache das explicações da IA | Cada repositório é explicado uma vez só; economiza cota da IA |
| `CATALOGO.md` | Todos os repositórios ativos, por categoria técnica | Consulta geral |
| `geral/*.md` | Os repositórios fora do foco de IA, uma página por categoria técnica (Frontend, Backend, DevOps…), em tabela com resumo em português | Visão completa de tudo com 20 mil+ estrelas |
| `areas/*.md` | Um arquivo por área de entrega (Arquitetura, Backend, Segurança, Testes…) com os repositórios relevantes | Para escolher ferramentas de IA para uma parte específica do projeto |
| `relatorios/AAAA-MM-DD.md` | O que mudou no dia | Histórico diário; também vira o texto da issue |

Como tudo é commitado, o próprio histórico do Git mostra a evolução de cada repositório.

## 🎬 Série de vídeos ([videos/](videos/README.md))

Um vídeo de 3 a 5 minutos por repositório do foco de IA, do mais estrelado para o menos, em linguagem simples. Todo dia a tarefa do Claude escreve o roteiro do próximo da fila e o GitHub Actions gera a narração e o vídeo. Cada episódio chega numa issue **🎬 Vídeo #N pronto**, com o vídeo, a capa, o título e a descrição para postar.

## 📺 Pesquisa no YouTube ([youtube/](youtube/README.md))

Serve de pesquisa para os roteiros: todo dia o GitHub Actions (`youtube-coleta.yml`, 04:47) coleta vídeos novos dos canais seguidos, das buscas fixas e das buscas sobre os repositórios do radar. Às 07:13 a tarefa do Claude escolhe os melhores e os explica em `youtube/`. Canais, buscas e limites ficam em [`config-youtube.yml`](config-youtube.yml).

## Como a tarefa agendada roda

```bash
python scripts/radar.py --sem-ia --exportar-pendentes 80 --exportar-traducoes 500   # busca, compara com ontem e lista o que falta explicar e traduzir
# o Claude lê .radar/pendentes.json e escreve .radar/explicacoes_novas.json
python scripts/radar.py --importar .radar/explicacoes_novas.json   # grava as explicações e regenera tudo
python scripts/radar.py --importar-traducoes .radar/traducoes_novas.json   # resumos em português dos repositórios fora do foco
python scripts/radar.py --abrir-issue marcelojacint/radar-github-50k   # issue só se houver novos
git commit + push
```

Os novos do dia são sempre avaliados: o Claude decide se entram no foco e, se entrarem, escreve a explicação completa. Todos os repositórios atuais do foco já estão explicados.

O workflow do GitHub Actions continua no repositório, mas só para execução manual (**Actions → Run workflow**). Ele faz a busca e o catálogo, sem as explicações. O agendamento dele está comentado para não conflitar com a tarefa do Claude.

## Alternativas para as explicações (se não quiser usar a tarefa do Claude)

- **Groq, plano gratuito:** mude `ia.provedor` para `openai-compativel`. Crie uma conta em console.groq.com (não pede cartão), gere uma API key e salve como secret `LLM_API_KEY` em *Settings → Secrets and variables → Actions*. Quando o limite gratuito do dia acaba, a API só recusa as chamadas, e o radar continua no dia seguinte, sem cobrança.
- **Outro provedor no formato da OpenAI** (Gemini, OpenRouter, OpenAI etc.): troque `url` e `modelo` em `ia.openai_compativel` no `config.yml`. O secret continua sendo `LLM_API_KEY`.
- **Claude (Anthropic, pago por uso):** `ia.provedor: anthropic` e secret `ANTHROPIC_API_KEY`.
- **Sem IA:** `ia.provedor: nenhum`. O catálogo sai só com a descrição original do GitHub e uma categoria definida por regras.

Sem o secret configurado, o radar continua rodando todo dia (busca, novidades, catálogo) e o relatório avisa que a IA está pausada. Em repositório público, o GitHub Actions também não tem custo.

> O GitHub Models (IA gratuita via `GITHUB_TOKEN`) foi descontinuado em 30/07/2026 e não é mais usado.

## Personalizar (`config.yml`)

- **`busca.foco.palavras_chave`**: primeiro filtro do foco (nome, descrição e tópicos). Inclua termos para ampliar, ou remova para restringir. Cada repositório que passa pelo filtro é avaliado pelo Claude, que decide se ele entra no catálogo (campo `foco`).
- **`busca.foco.descricao`**: o foco em uma frase. Aparece no topo do catálogo e orienta o Claude.
- **`areas`**: áreas de entrega usadas para dizer onde cada repositório ajuda. O Claude só usa nomes desta lista.
- **`busca.filtro_extra`**: restringe a busca com a sintaxe do GitHub. Exemplos: `topic:agent-skills` (só skills para agentes de IA), `language:csharp`, `topic:llm`.
- **`busca.min_estrelas`**: o corte (20000 hoje). A busca usa "maior ou igual".
- **`relatorio.abrir_issue`**: `sempre`, `quando_houver_novos` ou `nunca`.

Se você mudar o filtro, a próxima execução cria uma nova base de referência e não marca tudo como "novo".

## Rodar no seu computador

```bash
pip install -r requirements.txt
export GITHUB_TOKEN=ghp_seu_token   # opcional, mas deixa a busca 3x mais rápida
python scripts/radar.py --sem-ia    # só busca e catálogo
export LLM_API_KEY=gsk_...          # chave do Groq, para a IA
python scripts/radar.py             # com IA
```

## Detalhes que evitam alarme falso

- **Oscilação no corte:** um repositório que sai da busca é consultado direto na API antes de ser marcado como "saiu". Assim, quem ficou fora só por um problema de paginação continua ativo. Quem cai abaixo do corte e volta depois aparece em "Voltaram", não em "Novos".
- **Limite de 1000 resultados da busca do GitHub:** se o total passar disso, o script divide a faixa de estrelas automaticamente.
- **Projeto parado:** repositórios sem commit há 2 anos ou mais recebem um ⚠️ no catálogo.

> Estrelas medem popularidade, não qualidade nem adequação. Use o radar para descobrir opções e confira licença, manutenção e documentação antes de adotar algo num projeto de cliente.
