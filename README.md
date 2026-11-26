# Radar GitHub 50k

Todo dia, às 06:17 (horário de Brasília), um GitHub Actions:

1. busca **todos os repositórios open source com 50 mil+ estrelas** (hoje são ~530, sem contar os arquivados);
2. compara com o dia anterior e marca os **novos**, os que **saíram** e os que **mais cresceram**;
3. usa IA para explicar cada repositório: **o que é**, **por que importa** num projeto real e **em quais segmentos de negócio** ele faz sentido (relevância alta ou média, com um uso concreto);
4. salva tudo neste próprio repositório e abre uma **issue** quando aparece novidade (o GitHub te avisa por e-mail ou no app).

## Onde fica salvo

| Arquivo | O que guarda | Por que existe |
|---|---|---|
| `data/repos.json` | Base completa: estrelas, linguagem, licença, tópicos, data em que entrou | É a "memória" entre execuções; sem ela não dá para saber o que é novo |
| `data/explicacoes.json` | Cache das explicações da IA | Cada repositório é explicado uma vez só; economiza cota da IA |
| `CATALOGO.md` | Todos os repositórios ativos, por categoria técnica | Consulta geral |
| `segmentos/*.md` | Um arquivo por segmento (Saúde, Indústria/ERP, Varejo…) com os repositórios relevantes | Para quando você vai começar um projeto de um segmento específico |
| `relatorios/AAAA-MM-DD.md` | O que mudou no dia | Histórico diário; também vira o texto da issue |

Como tudo é commitado, o próprio histórico do Git mostra a evolução de cada repositório.

## Instalação (5 minutos)

1. Crie um repositório no GitHub (ex.: `radar-github-50k`), público ou privado.
2. Suba todos os arquivos desta pasta, incluindo `.github/workflows/radar-diario.yml`.
3. Vá em **Actions** → **Radar GitHub 50k (diário)** → **Run workflow** para a primeira execução.
4. Pronto. A partir daí roda sozinho todo dia.

Na primeira execução ele cria a base de referência e começa a gerar explicações (100 por dia, por padrão). A base inteira fica explicada em uns 6 dias. Para acelerar, rode manualmente informando um número maior em `max_explicacoes`.

Se o passo de salvar der erro 403: **Settings → Actions → General → Workflow permissions → Read and write permissions**.

## IA usada para as explicações (sem custo)

- **Padrão: Groq, plano gratuito.** Crie uma conta em console.groq.com (não pede cartão), gere uma API key e salve como secret `LLM_API_KEY` em *Settings → Secrets and variables → Actions*. Quando o limite gratuito do dia acaba, a API só recusa as chamadas, e o radar continua no dia seguinte, sem cobrança.
- **Outro provedor no formato da OpenAI** (Gemini, OpenRouter, OpenAI etc.): troque `url` e `modelo` em `ia.openai_compativel` no `config.yml`. O secret continua sendo `LLM_API_KEY`.
- **Claude (Anthropic, pago por uso):** `ia.provedor: anthropic` e secret `ANTHROPIC_API_KEY`.
- **Sem IA:** `ia.provedor: nenhum`. O catálogo sai só com a descrição original do GitHub e uma categoria definida por regras.

Sem o secret configurado, o radar continua rodando todo dia (busca, novidades, catálogo) e o relatório avisa que a IA está pausada. Em repositório público, o GitHub Actions também não tem custo.

> O GitHub Models (IA gratuita via `GITHUB_TOKEN`) foi descontinuado em 30/07/2026 e não é mais usado.

## Personalizar (`config.yml`)

- **`segmentos`**: troque pelos segmentos dos seus clientes (ex.: "Arquitetura e construção", "Estética e beleza"). A IA só usa nomes dessa lista.
- **`busca.filtro_extra`**: restringe a busca com a sintaxe do GitHub. Exemplos: `topic:agent-skills` (só skills para agentes de IA), `language:csharp`, `topic:llm`.
- **`busca.min_estrelas`**: o corte (50000 por padrão).
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

- **Oscilação no corte:** um repositório que sai da busca é consultado direto na API antes de ser marcado como "saiu". Assim, quem ficou fora só por um problema de paginação continua ativo. Quem cai abaixo de 50 mil e volta depois aparece em "Voltaram", não em "Novos".
- **Limite de 1000 resultados da busca do GitHub:** se o total passar disso, o script divide a faixa de estrelas automaticamente.
- **Projeto parado:** repositórios sem commit há 2 anos ou mais recebem um ⚠️ no catálogo.

> Estrelas medem popularidade, não qualidade nem adequação. Use o radar para descobrir opções e confira licença, manutenção e documentação antes de adotar algo num projeto de cliente.
