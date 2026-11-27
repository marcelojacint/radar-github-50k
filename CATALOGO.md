# Radar de IA para entregar software — repositórios com 50 mil+ estrelas

Atualizado em 27/11/2026 · **137** repositórios no foco (de 532 com 50 mil+ estrelas) · com explicação completa: 137/137

**Foco:** IA para construir e entregar software melhor: agentes, skills, agentes de código, MCP, LLMs, RAG e ferramentas de IA para arquitetura, engenharia, design, frontend, backend, banco de dados, segurança, testes e DevOps.

**Por área:** [Arquitetura de software](areas/arquitetura-de-software.md) · [Engenharia e produtividade](areas/engenharia-e-produtividade.md) · [Design e UI/UX](areas/design-e-ui-ux.md) · [Frontend](areas/frontend.md) · [Backend e APIs](areas/backend-e-apis.md) · [Banco de dados e dados](areas/banco-de-dados-e-dados.md) · [Segurança e cibersegurança](areas/seguranca-e-ciberseguranca.md) · [Testes e QA](areas/testes-e-qa.md) · [DevOps e infraestrutura](areas/devops-e-infraestrutura.md)

## Categorias

- [Agentes de código](#agentes-de-código) (10)
- [Skills e configurações para agentes](#skills-e-configurações-para-agentes) (18)
- [Frameworks de agentes e orquestração](#frameworks-de-agentes-e-orquestração) (13)
- [Plataformas de IA e automação](#plataformas-de-ia-e-automação) (7)
- [MCP, ferramentas e integrações](#mcp-ferramentas-e-integrações) (8)
- [Memória, contexto e economia de tokens](#memória-contexto-e-economia-de-tokens) (7)
- [Conhecimento do código e diagramas](#conhecimento-do-código-e-diagramas) (5)
- [RAG e processamento de documentos](#rag-e-processamento-de-documentos) (12)
- [Modelos, inferência e gateways](#modelos-inferência-e-gateways) (12)
- [Treino e frameworks de ML](#treino-e-frameworks-de-ml) (9)
- [Design e interfaces com IA](#design-e-interfaces-com-ia) (7)
- [Segurança com IA](#segurança-com-ia) (4)
- [Gestão de agentes e produtividade](#gestão-de-agentes-e-produtividade) (6)
- [Aprendizado de IA](#aprendizado-de-ia) (19)

## Agentes de código

**[anomalyco/opencode](https://github.com/anomalyco/opencode)** · ⭐ 229,5 mil · TypeScript · MIT

- **O que é:** Agente de programação open source.
- **Por que importa:** Agente de código open source que funciona com vários provedores de modelo; evita ficar preso a um fornecedor.
- **Áreas:** **Engenharia e produtividade** (alta) — Usar o mesmo fluxo de agente de código trocando entre modelos pagos e locais

**[anthropics/claude-code](https://github.com/anthropics/claude-code)** · ⭐ 157,3 mil · TypeScript

- **O que é:** Claude Code: ferramenta de programação com agente que roda no terminal, entende seu código e executa tarefas, explica código e cuida do Git em linguagem natural.
- **Por que importa:** Agente de código no terminal que lê o projeto inteiro, edita arquivos, roda testes e cuida do Git; acelera features, refatorações e correções com supervisão humana.
- **Áreas:** **Engenharia e produtividade** (alta) — Implementar features e refatorações em vários arquivos de uma vez, com plano e revisão; **Backend e APIs** (alta) — Criar endpoints, migrations e testes a partir de uma descrição da regra de negócio; **Testes e QA** (média) — Gerar e rodar testes automatizados e corrigir os que falham

**[openai/codex](https://github.com/openai/codex)** · ⭐ 136,6 mil · Rust · Apache-2.0

- **O que é:** Agente de programação leve que roda no terminal (OpenAI Codex).
- **Por que importa:** Agente de código leve da OpenAI para o terminal; boa alternativa ou complemento ao Claude Code para tarefas de implementação e revisão.
- **Áreas:** **Engenharia e produtividade** (alta) — Delegar tarefas de código pelo terminal e revisar as mudanças propostas; **Backend e APIs** (média) — Gerar código de serviços e scripts com base no repositório existente

**[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · ⭐ 109,2 mil · TypeScript · Apache-2.0

- **O que é:** Agente de IA open source que leva o Gemini para o seu terminal.
- **Por que importa:** Agente open source do Gemini no terminal, com contexto grande; útil para analisar bases de código extensas e automatizar tarefas de desenvolvimento.
- **Áreas:** **Engenharia e produtividade** (alta) — Analisar um repositório grande e propor mudanças pelo terminal; **Arquitetura de software** (média) — Ler a base inteira para mapear módulos e dependências antes de uma refatoração

**[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · ⭐ 94,4 mil · TypeScript · MIT

- **O que é:** OpenHands: desenvolvimento de software com agentes de IA.
- **Por que importa:** Plataforma open source de desenvolvimento com agentes que executam tarefas completas em sandbox; referência para automatizar issues e PRs.
- **Áreas:** **Engenharia e produtividade** (alta) — Atribuir issues simples a um agente que abre o PR em ambiente isolado; **DevOps e infraestrutura** (média) — Rodar agentes de manutenção em sandbox dentro da sua infraestrutura

**[cline/cline](https://github.com/cline/cline)** · ⭐ 71,9 mil · TypeScript · Apache-2.0

- **O que é:** Agente de código autônomo, disponível como SDK, extensão de IDE ou CLI.
- **Por que importa:** Agente autônomo dentro do VS Code (também SDK e CLI) que planeja, edita e executa comandos com aprovação passo a passo.
- **Áreas:** **Engenharia e produtividade** (alta) — Programar com um agente dentro da IDE aprovando cada edição e comando; **Frontend** (média) — Criar e ajustar componentes de interface direto no editor

**[openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter)** · ⭐ 69 mil · Rust · Apache-2.0

- **O que é:** Agente de código para modelos abertos.
- **Por que importa:** Agente de código para modelos abertos que executa código localmente; útil para automações e análises sem depender de API paga.
- **Áreas:** **Engenharia e produtividade** (média) — Automatizar tarefas locais e scripts com modelos abertos; **Banco de dados e dados** (média) — Explorar e transformar arquivos de dados localmente conversando com o agente

**[warpdotdev/warp](https://github.com/warpdotdev/warp)** · ⭐ 66,2 mil · Rust · AGPL-3.0

- **O que é:** Warp: ambiente de desenvolvimento com agentes, nascido do terminal.
- **Por que importa:** Terminal moderno com agentes integrados; reúne comandos, IA e fluxos de trabalho do time num só lugar.
- **Áreas:** **Engenharia e produtividade** (média) — Executar e explicar comandos com ajuda de IA no dia a dia; **DevOps e infraestrutura** (média) — Padronizar fluxos de comandos de deploy e diagnóstico para o time

**[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** · ⭐ 56,8 mil · Go · Apache-2.0

- **O que é:** Ferramenta de revisão de código do Alibaba que combina regras determinísticas e agente LLM, com comentários por linha.
- **Por que importa:** Revisão de código do Alibaba que combina regras determinísticas e agente LLM, com comentários por linha (NPE, XSS, SQL injection, concorrência).
- **Áreas:** **Engenharia e produtividade** (alta) — Automatizar revisão de PRs com comentários por linha; **Segurança e cibersegurança** (alta) — Detectar XSS, SQL injection e falhas comuns antes do merge; **Testes e QA** (média) — Reduzir bugs que chegam ao QA

**[Aider-AI/aider](https://github.com/Aider-AI/aider)** · ⭐ 50,3 mil · Python · Apache-2.0

- **O que é:** aider: programação em par com IA no terminal.
- **Por que importa:** Programação em par com IA no terminal, integrada ao Git (cada mudança vira commit); muito bom para mudanças incrementais e rastreáveis.
- **Áreas:** **Engenharia e produtividade** (alta) — Fazer mudanças pequenas e rastreáveis com commits automáticos por alteração


## Skills e configurações para agentes

**[mattpocock/skills](https://github.com/mattpocock/skills)** · ⭐ 333,9 mil · Shell · MIT

- **O que é:** Coleção de skills para agentes de IA voltadas a engenheiros, tiradas do diretório .agents do autor.
- **Por que importa:** Skills práticas de um engenheiro experiente para agentes de código; bons exemplos de como ensinar o agente a seguir boas práticas.
- **Áreas:** **Engenharia e produtividade** (alta) — Adotar skills prontas de engenharia e adaptá-las ao padrão do projeto; **Frontend** (média) — Melhorar o código TypeScript gerado pelo agente

**[obra/superpowers](https://github.com/obra/superpowers)** · ⭐ 327,8 mil · Shell · MIT

- **O que é:** Framework de skills para agentes de IA e metodologia de desenvolvimento de software.
- **Por que importa:** Conjunto de skills e metodologia que faz o agente trabalhar com brainstorming, plano, TDD e revisão; melhora a qualidade das entregas com IA.
- **Áreas:** **Engenharia e produtividade** (alta) — Dar ao agente um processo disciplinado: planejar, testar primeiro e revisar; **Testes e QA** (alta) — Forçar o agente a escrever testes antes do código (TDD)

**[affaan-m/ECC](https://github.com/affaan-m/ECC)** · ⭐ 311,5 mil · JavaScript · MIT

- **O que é:** Sistema para otimizar o desempenho de agentes de código (Claude Code, Codex, Cursor etc.) com skills, memória, segurança e desenvolvimento guiado por pesquisa.
- **Por que importa:** Sistema completo de skills, memória, segurança e regras para agentes de código; acelera a configuração de um ambiente de agente robusto.
- **Áreas:** **Engenharia e produtividade** (alta) — Montar rapidamente uma configuração madura de agente para o time; **Segurança e cibersegurança** (média) — Reaproveitar regras de segurança para limitar o que o agente pode fazer
- ⚠️ Projeto recente e grande; adote por partes.

**[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · ⭐ 236 mil

- **O que é:** Arquivo CLAUDE.md único para melhorar o comportamento do Claude Code, baseado nas observações de Andrej Karpathy sobre erros comuns de LLMs ao programar.
- **Por que importa:** Um único CLAUDE.md com regras contra os erros mais comuns de LLMs ao programar; ganho rápido de qualidade com custo zero.
- **Áreas:** **Engenharia e produtividade** (alta) — Copiar e adaptar o CLAUDE.md para reduzir erros do agente no projeto

**[anthropics/skills](https://github.com/anthropics/skills)** · ⭐ 201,2 mil · Python

- **O que é:** Repositório público de Agent Skills da Anthropic.
- **Por que importa:** Repositório oficial de Agent Skills da Anthropic: exemplos e padrão de como empacotar instruções e scripts para agentes; base para criar as suas.
- **Áreas:** **Engenharia e produtividade** (alta) — Usar como modelo para criar skills próprias do time (padrões de código, revisão, deploy); **Arquitetura de software** (média) — Documentar decisões e padrões de arquitetura como skills reutilizáveis pelo agente

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · ⭐ 199,6 mil · JavaScript · MIT

- **O que é:** Faz o agente de IA pensar como o dev sênior mais preguiçoso da sala: o melhor código é o que você não escreveu.
- **Por que importa:** Skill que empurra o agente a escrever menos código e preferir soluções simples; combate excesso de complexidade gerada por IA.
- **Áreas:** **Engenharia e produtividade** (alta) — Evitar que o agente crie abstrações e código desnecessários; **Arquitetura de software** (média) — Manter a arquitetura enxuta em projetos feitos com IA

**[f/prompts.chat](https://github.com/f/prompts.chat)** · ⭐ 178,6 mil · MDX · outra

- **O que é:** Antigo Awesome ChatGPT Prompts: compartilhe, descubra e organize prompts da comunidade; pode ser auto-hospedado.
- **Por que importa:** Coleção comunitária de prompts (antigo Awesome ChatGPT Prompts), auto-hospedável para o time.
- **Áreas:** **Engenharia e produtividade** (média) — Montar uma biblioteca interna de prompts reutilizáveis

**[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · ⭐ 170,5 mil · Shell · MIT

- **O que é:** Agência de IA completa: agentes especializados (frontend, comunidade, revisão etc.) com personalidade, processos e entregas definidos.
- **Por que importa:** Coleção de agentes especializados (frontend, backend, QA, produto etc.) com personalidade e processos definidos; pronto para montar um 'time' de IA.
- **Áreas:** **Engenharia e produtividade** (média) — Usar papéis prontos (revisor, QA, arquiteto) como subagentes; **Testes e QA** (média) — Ter um agente revisor/testador dedicado para cada entrega

**[github/spec-kit](https://github.com/github/spec-kit)** · ⭐ 151,9 mil · Python · MIT

- **O que é:** Kit para começar com desenvolvimento guiado por especificação (SDD) ou outro processo.
- **Por que importa:** Kit do GitHub para desenvolvimento guiado por especificação: você escreve a spec, o agente planeja e implementa; reduz ambiguidade nas entregas com IA.
- **Áreas:** **Arquitetura de software** (alta) — Transformar requisitos em especificação e plano técnico antes do código; **Engenharia e produtividade** (alta) — Padronizar como o time pede features aos agentes

**[garrytan/gstack](https://github.com/garrytan/gstack)** · ⭐ 142,8 mil · TypeScript · MIT

- **O que é:** Configuração do Claude Code usada por Garry Tan: 23 ferramentas que atuam como CEO, designer, gerente de engenharia, release, documentação e QA.
- **Por que importa:** Configuração opinativa do Claude Code com ferramentas que fazem papel de designer, gerente de engenharia, QA e release; mostra como cobrir o ciclo todo com agentes.
- **Áreas:** **Engenharia e produtividade** (média) — Inspirar um fluxo completo de entrega com papéis definidos para o agente; **Testes e QA** (média) — Adicionar uma etapa automática de QA antes do release

**[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)** · ⭐ 120,7 mil · JavaScript · MIT

- **O que é:** Skills de engenharia de nível produção para agentes de programação com IA.
- **Por que importa:** Skills de engenharia em nível de produção para agentes de código (performance, acessibilidade, qualidade).
- **Áreas:** **Engenharia e produtividade** (alta) — Aplicar boas práticas de produção no código gerado por agentes; **Frontend** (média) — Revisar performance e acessibilidade de páginas com ajuda do agente

**[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)** · ⭐ 75,9 mil · TypeScript · MIT

- **O que é:** Desenvolvimento guiado por especificação (SDD) para assistentes de código com IA.
- **Por que importa:** Desenvolvimento guiado por especificação para assistentes de código; mantém specs e mudanças versionadas junto do código.
- **Áreas:** **Arquitetura de software** (alta) — Registrar e evoluir especificações do sistema junto com o código; **Engenharia e produtividade** (média) — Revisar mudanças de comportamento antes de o agente implementar

**[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · ⭐ 71,2 mil · TypeScript · outra

- **O que é:** Extensão para agentes de código que ativa fluxos avançados com uma palavra-chave no prompt.
- **Por que importa:** Extensão para agentes de código com fluxos avançados acionados por palavra-chave; útil para quem quer orquestrar subagentes sem montar tudo do zero.
- **Áreas:** **Engenharia e produtividade** (média) — Ativar fluxos de orquestração prontos no agente de código
- ⚠️ Projeto recente; teste antes de padronizar no time.

**[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · ⭐ 69,5 mil · HTML · MIT

- **O que é:** Boas práticas para usar o Claude Code, do "vibe coding" à engenharia com agentes.
- **Por que importa:** Boas práticas para sair do 'vibe coding' e usar o Claude Code de forma profissional e previsível.
- **Áreas:** **Engenharia e produtividade** (alta) — Treinar o time em um uso disciplinado de agentes de código

**[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · ⭐ 62,7 mil · Python · MIT

- **O que é:** Skill que impede o agente de código de esconder a resposta: saídas diretas e fáceis de ler.
- **Por que importa:** Skill que obriga o agente a responder de forma direta, com a resposta primeiro; reduz tempo de leitura e retrabalho.
- **Áreas:** **Engenharia e produtividade** (média) — Deixar as respostas do agente mais objetivas no dia a dia

**[emilkowalski/skills](https://github.com/emilkowalski/skills)** · ⭐ 60,2 mil · Markdown · MIT

- **O que é:** Skills para designers e engenheiros.
- **Por que importa:** Skills para designers e engenheiros, de um autor conhecido por componentes de UI bem acabados; melhora a qualidade visual do que o agente gera.
- **Áreas:** **Design e UI/UX** (alta) — Ensinar o agente a seguir detalhes de interação e acabamento visual; **Frontend** (alta) — Gerar componentes com animações e microinterações de qualidade

**[bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)** · ⭐ 55,8 mil · Python · outra

- **O que é:** Método BMAD: desenvolvimento ágil guiado por agentes de IA.
- **Por que importa:** Método ágil guiado por agentes de IA, com papéis (analista, PM, arquiteto, dev, QA) e artefatos definidos; estrutura projetos inteiros feitos com IA.
- **Áreas:** **Arquitetura de software** (alta) — Gerar PRD e documento de arquitetura antes de o agente codar; **Engenharia e produtividade** (alta) — Organizar o desenvolvimento com IA em fases e papéis claros; **Testes e QA** (média) — Incluir o papel de QA no fluxo dos agentes

**[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** · ⭐ 50,4 mil · Python · MIT

- **O que é:** Mais de 3.000 skills reutilizáveis para agentes de IA, com catálogo local, CLI, MCP e plugins.
- **Por que importa:** Milhares de skills reutilizáveis com catálogo local, CLI e MCP; útil para encontrar e instalar skills por tarefa.
- **Áreas:** **Engenharia e produtividade** (média) — Buscar e instalar skills prontas por tipo de tarefa
- ⚠️ Qualidade varia entre as skills; revise antes de usar.


## Frameworks de agentes e orquestração

**[openclaw/openclaw](https://github.com/openclaw/openclaw)** · ⭐ 395,3 mil · TypeScript · MIT

- **O que é:** Assistente pessoal de IA que roda na sua própria máquina e executa tarefas de verdade (mensagens, arquivos, automações), conversando por apps como WhatsApp e Telegram.
- **Por que importa:** Plataforma de agente pessoal auto-hospedado que executa tarefas reais e conversa por WhatsApp/Telegram; referência para automações com agentes.
- **Áreas:** **Backend e APIs** (média) — Base para um assistente que integra mensagens e sistemas internos; **Segurança e cibersegurança** (média) — Exige revisão de permissões: o agente tem acesso amplo à máquina
- ⚠️ Projeto recente e de evolução rápida; revise a segurança antes de usar com dados de clientes.

**[deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)** · ⭐ 287,8 mil · TypeScript · MIT

- **O que é:** DeepSeek Harness: ambiente para agentes de IA em que tudo é plugin.
- **Por que importa:** Ambiente de agente da DeepSeek baseado em plugins; alternativa aberta para rodar agentes com modelos DeepSeek.
- **Áreas:** **Engenharia e produtividade** (média) — Rodar agentes de código com modelos DeepSeek e plugins próprios
- ⚠️ Projeto muito recente.

**[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · ⭐ 266,5 mil · Python · MIT

- **O que é:** Agente de IA que aprende e evolui com o uso.
- **Por que importa:** Agente open source que aprende e acumula habilidades com o uso; interessante para assistentes de longo prazo.
- **Áreas:** **Engenharia e produtividade** (média) — Experimentar agentes que evoluem com o uso em tarefas recorrentes
- ⚠️ Projeto recente.

**[Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)** · ⭐ 188,2 mil · Python · outra

- **O que é:** AutoGPT: plataforma para criar e usar agentes de IA de forma acessível.
- **Por que importa:** Plataforma pioneira de agentes autônomos, hoje com construtor visual de agentes e fluxos.
- **Áreas:** **Backend e APIs** (média) — Prototipar agentes que executam fluxos de negócio de ponta a ponta

**[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** · ⭐ 150,1 mil · Python · MIT

- **O que é:** Plataforma de engenharia de agentes de IA.
- **Por que importa:** Plataforma de engenharia de agentes: integrações com modelos, ferramentas, memória e RAG; base de muitos produtos de IA.
- **Áreas:** **Backend e APIs** (alta) — Construir funcionalidades com LLM (chat, RAG, agentes) no backend; **Arquitetura de software** (média) — Padronizar integrações com vários provedores de modelo

**[earendil-works/pi](https://github.com/earendil-works/pi)** · ⭐ 124,2 mil · TypeScript · MIT

- **O que é:** Kit para agentes de IA: API unificada de LLMs, loop de agente, interface de terminal e agente de código.
- **Por que importa:** Kit para construir agentes: API unificada de LLMs, loop de agente e CLI de código; base enxuta para criar seu próprio agente.
- **Áreas:** **Backend e APIs** (média) — Criar um agente próprio com loop e ferramentas sob controle; **Engenharia e produtividade** (média) — Montar um agente de código customizado para o time

**[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · ⭐ 85,9 mil · Python · MIT

- **O que é:** Ambiente open source de superagente para tarefas longas de pesquisa, código e criação, com sandboxes, memória, ferramentas e subagentes.
- **Por que importa:** Superagente para tarefas longas de pesquisa e código com sandbox, memória e subagentes; referência de arquitetura de agentes complexos.
- **Áreas:** **Arquitetura de software** (média) — Estudar arquitetura de agentes com sandbox, memória e subagentes; **Backend e APIs** (média) — Montar fluxos de pesquisa e geração de relatórios automatizados

**[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · ⭐ 82,5 mil · TypeScript · MIT

- **O que é:** Ambiente para agentes: enxames multiagente, fluxos autônomos e IA conversacional, com memória adaptativa e RAG.
- **Por que importa:** Ambiente para enxames de agentes e fluxos autônomos com memória e RAG, integrado a Claude Code e Codex.
- **Áreas:** **Engenharia e produtividade** (média) — Coordenar vários agentes de código em tarefas paralelas
- ⚠️ Projeto com muitas promessas; valide em casos pequenos antes.

**[FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)** · ⭐ 71,5 mil · Python · MIT

- **O que é:** MetaGPT: framework multiagente que simula uma empresa de software feita de IAs.
- **Por que importa:** Framework multiagente que simula uma empresa de software (PM, arquiteto, dev, QA); mostra como dividir uma entrega entre agentes.
- **Áreas:** **Arquitetura de software** (média) — Gerar requisitos e desenho técnico com agentes em papéis definidos; **Engenharia e produtividade** (média) — Estudar orquestração de vários agentes em um fluxo de desenvolvimento

**[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · ⭐ 61,3 mil · Python · MIT

- **O que é:** CrewAI: framework para orquestrar agentes de IA autônomos que colaboram em tarefas complexas.
- **Por que importa:** Framework Python para orquestrar agentes com papéis e tarefas; um dos mais usados para fluxos multiagente em produção.
- **Áreas:** **Backend e APIs** (alta) — Implementar fluxos multiagente (pesquisa, análise, redação) dentro de um backend; **Arquitetura de software** (média) — Desenhar a divisão de responsabilidades entre agentes

**[FoundationAgents/OpenManus](https://github.com/FoundationAgents/OpenManus)** · ⭐ 59 mil · Python · MIT

- **O que é:** OpenManus: alternativa aberta ao agente Manus.
- **Por que importa:** Alternativa aberta ao agente Manus para tarefas gerais com ferramentas; bom para estudar e montar agentes próprios.
- **Áreas:** **Backend e APIs** (média) — Criar um agente próprio que usa ferramentas e APIs do sistema

**[aaif-goose/goose](https://github.com/aaif-goose/goose)** · ⭐ 57,1 mil · Rust · Apache-2.0

- **O que é:** Agente de IA open source e extensível que instala, executa, edita e testa com qualquer LLM.
- **Por que importa:** Agente open source extensível que vai além de sugerir código: instala, executa, edita e testa com qualquer LLM.
- **Áreas:** **Engenharia e produtividade** (alta) — Automatizar tarefas de desenvolvimento ponta a ponta com qualquer modelo; **DevOps e infraestrutura** (média) — Automatizar rotinas de ambiente e configuração

**[HKUDS/nanobot](https://github.com/HKUDS/nanobot)** · ⭐ 50,4 mil · Python · MIT

- **O que é:** Agente pessoal open source e leve.
- **Por que importa:** Agente pessoal leve e open source; bom ponto de partida para entender e montar agentes simples.
- **Áreas:** **Backend e APIs** (média) — Prototipar um agente leve com ferramentas próprias


## Plataformas de IA e automação

**[n8n-io/n8n](https://github.com/n8n-io/n8n)** · ⭐ 212,4 mil · TypeScript · outra

- **O que é:** Plataforma de automação de fluxos de trabalho com IA nativa: combina construção visual e código, roda na nuvem ou auto-hospedada, com mais de 400 integrações.
- **Por que importa:** Automação de fluxos com IA nativa, mais de 400 integrações e opção auto-hospedada; resolve integrações e automações sem escrever um backend inteiro.
- **Áreas:** **Backend e APIs** (alta) — Orquestrar integrações entre sistemas (CRM, WhatsApp, e-mail, ERP) com etapas de IA; **DevOps e infraestrutura** (média) — Automatizar rotinas operacionais e alertas; **Banco de dados e dados** (média) — Sincronizar e transformar dados entre bancos e planilhas

**[langgenius/dify](https://github.com/langgenius/dify)** · ⭐ 162 mil · Python · outra

- **O que é:** Plataforma para criar fluxos com agentes, pipelines de RAG e ferramentas de IA, na nuvem ou auto-hospedada.
- **Por que importa:** Plataforma para criar apps de IA, agentes e pipelines de RAG com interface visual e deploy auto-hospedado.
- **Áreas:** **Backend e APIs** (alta) — Publicar rapidamente um chatbot ou agente com RAG sobre documentos da empresa; **Arquitetura de software** (média) — Separar a camada de IA do sistema principal via APIs da plataforma

**[open-webui/open-webui](https://github.com/open-webui/open-webui)** · ⭐ 159,7 mil · Svelte · outra

- **O que é:** Interface amigável para IA, compatível com Ollama, API da OpenAI e outros.
- **Por que importa:** Interface web auto-hospedada para usar modelos locais ou via API, com RAG e controle de usuários; 'ChatGPT interno' da empresa.
- **Áreas:** **Backend e APIs** (média) — Oferecer chat com IA interno, com modelos locais e documentos da empresa; **Segurança e cibersegurança** (média) — Manter dados sensíveis dentro da infraestrutura própria

**[langflow-ai/langflow](https://github.com/langflow-ai/langflow)** · ⭐ 157 mil · Python · MIT

- **O que é:** Langflow: ferramenta para criar e publicar agentes e fluxos com IA.
- **Por que importa:** Construtor visual de agentes e fluxos de IA, com exportação para API; acelera protótipos de funcionalidades com LLM.
- **Áreas:** **Backend e APIs** (alta) — Prototipar e expor fluxos de IA como API para o sistema

**[supabase/supabase](https://github.com/supabase/supabase)** · ⭐ 115,6 mil · TypeScript · Apache-2.0

- **O que é:** Supabase: plataforma de desenvolvimento sobre Postgres para apps web, mobile e de IA.
- **Por que importa:** Plataforma sobre Postgres com autenticação, storage, APIs automáticas e vetores (pgvector); backend completo pronto para apps com IA.
- **Áreas:** **Banco de dados e dados** (alta) — Usar Postgres gerenciado com pgvector para busca semântica; **Backend e APIs** (alta) — Ganhar autenticação, storage e APIs sem escrever um backend do zero; **Segurança e cibersegurança** (média) — Controlar acesso aos dados com políticas por linha (RLS)

**[Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)** · ⭐ 68,7 mil · JavaScript · MIT

- **O que é:** AnythingLLM: plataforma local para agentes e chat com seus documentos.
- **Por que importa:** App local para conversar com documentos e rodar agentes, com controle total dos dados.
- **Áreas:** **Backend e APIs** (média) — Montar uma base de conhecimento interna consultável por IA; **Banco de dados e dados** (média) — Indexar documentos e manuais para busca em linguagem natural

**[appwrite/appwrite](https://github.com/appwrite/appwrite)** · ⭐ 58,7 mil · TypeScript · BSD-3-Clause

- **O que é:** Appwrite: nuvem open source com autenticação, bancos de dados, storage, funções, mensagens e hospedagem.
- **Por que importa:** Nuvem open source com autenticação, bancos, storage, funções e mensagens, voltada também a agentes.
- **Áreas:** **Backend e APIs** (alta) — Ter backend pronto (auth, banco, storage, funções) auto-hospedado; **Banco de dados e dados** (média) — Gerenciar coleções de dados com permissões prontas


## MCP, ferramentas e integrações

**[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** · ⭐ 211,2 mil · TypeScript · AGPL-3.0

- **O que é:** Infraestrutura de dados para agentes de IA: busca, raspagem e acesso a mais de 550 fontes de dados por uma única API.
- **Por que importa:** Transforma sites em dados limpos (Markdown/JSON) para agentes e RAG, com busca e raspagem por uma API.
- **Áreas:** **Backend e APIs** (alta) — Alimentar um sistema de IA com conteúdo de sites de forma estruturada; **Banco de dados e dados** (média) — Coletar e normalizar dados da web para análises

**[browser-use/browser-use](https://github.com/browser-use/browser-use)** · ⭐ 122,2 mil · Python · MIT

- **O que é:** Biblioteca Python open source para agentes de IA que navegam na web, com serviço de nuvem opcional.
- **Por que importa:** Biblioteca Python para agentes que navegam e interagem com sites; base para automações e testes guiados por IA.
- **Áreas:** **Testes e QA** (alta) — Criar testes exploratórios em que o agente percorre a aplicação; **Backend e APIs** (média) — Automatizar tarefas em sistemas web sem API

**[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · ⭐ 92,3 mil · TypeScript · outra

- **O que é:** Servidores de referência do Model Context Protocol (MCP).
- **Por que importa:** Servidores de referência do MCP (Git, sistema de arquivos, busca, bancos etc.); ponto de partida para conectar agentes às suas ferramentas.
- **Áreas:** **Backend e APIs** (alta) — Usar como modelo para criar um servidor MCP que expõe a API do seu sistema ao agente; **Banco de dados e dados** (média) — Dar ao agente acesso controlado a um banco de dados via MCP; **DevOps e infraestrutura** (média) — Integrar agentes a ferramentas internas de forma padronizada

**[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** · ⭐ 88 mil · Python · Apache-2.0

- **O que é:** Crawler open source para coletar, extrair e buscar dados na web para agentes de IA, com versão em nuvem opcional.
- **Por que importa:** Crawler open source pensado para LLMs; extrai conteúdo pronto para RAG e pode ser auto-hospedado sem custo.
- **Áreas:** **Backend e APIs** (alta) — Montar coleta de conteúdo para bases de conhecimento de IA; **Banco de dados e dados** (média) — Extrair dados estruturados de páginas para alimentar o banco

**[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)** · ⭐ 66,6 mil · Python · Apache-2.0

- **O que é:** Torna qualquer software "nativo para agentes" por meio de interfaces de linha de comando.
- **Por que importa:** Cria interfaces de linha de comando para softwares existentes, para que agentes consigam operá-los.
- **Áreas:** **Backend e APIs** (média) — Expor operações de um sistema interno como CLI utilizável por agentes
- ⚠️ Projeto recente.

**[upstash/context7](https://github.com/upstash/context7)** · ⭐ 65,5 mil · TypeScript · MIT

- **O que é:** Context7: documentação sempre atualizada para agentes de IA.
- **Por que importa:** Entrega ao agente a documentação atualizada das bibliotecas; evita código baseado em APIs antigas.
- **Áreas:** **Engenharia e produtividade** (alta) — Reduzir erros do agente com versões novas de frameworks; **Frontend** (média) — Gerar código com a API atual de bibliotecas de frontend; **Backend e APIs** (média) — Usar a documentação correta de frameworks de backend

**[ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** · ⭐ 59,6 mil · TypeScript · Apache-2.0

- **O que é:** Chrome DevTools para agentes de código (servidor MCP).
- **Por que importa:** Dá ao agente de código acesso ao Chrome DevTools (console, rede, performance); o agente passa a enxergar e depurar a página de verdade.
- **Áreas:** **Frontend** (alta) — Deixar o agente depurar erros de console e rede da aplicação web; **Testes e QA** (alta) — Verificar no navegador se a tela funciona depois da mudança

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)** · ⭐ 54,2 mil · Rust · Apache-2.0

- **O que é:** CLI de automação de navegador para agentes de IA.
- **Por que importa:** CLI de automação de navegador feita para agentes de IA; leve e fácil de integrar a fluxos de teste e verificação.
- **Áreas:** **Testes e QA** (alta) — Deixar o agente navegar e validar fluxos da aplicação; **Frontend** (média) — Conferir telas no navegador durante o desenvolvimento


## Memória, contexto e economia de tokens

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · ⭐ 123,2 mil · Go · Apache-2.0

- **O que é:** Skill e proxy local para agentes de código que encurtam respostas e saídas de ferramentas, economizando tokens.
- **Por que importa:** Skill e proxy que encurtam respostas e saídas de ferramentas dos agentes, economizando tokens sem perder informação.
- **Áreas:** **Engenharia e produtividade** (média) — Deixar o agente mais econômico e direto

**[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · ⭐ 120,1 mil · TypeScript · Apache-2.0

- **O que é:** Memória persistente entre sessões para agentes de IA: registra, comprime e reaproveita o contexto em sessões futuras.
- **Por que importa:** Memória persistente entre sessões para agentes de código: o agente lembra do que já fez no projeto.
- **Áreas:** **Engenharia e produtividade** (alta) — Evitar que o agente esqueça decisões e contexto entre sessões

**[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · ⭐ 88 mil · Rust · Apache-2.0

- **O que é:** Proxy de linha de comando que reduz em 60–90% o consumo de tokens de LLMs em comandos comuns de desenvolvimento.
- **Por que importa:** Proxy de linha de comando que reduz de 60% a 90% os tokens em comandos comuns de desenvolvimento.
- **Áreas:** **Engenharia e produtividade** (alta) — Economizar tokens e limite de uso dos agentes de código

**[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · ⭐ 81 mil · Python · Apache-2.0

- **O que é:** Comprime saídas de ferramentas, logs e trechos de RAG antes de enviar ao LLM, reduzindo tokens sem mudar as respostas.
- **Por que importa:** Comprime saídas de ferramentas, logs e trechos de RAG antes do LLM; reduz custo e mantém as respostas.
- **Áreas:** **Engenharia e produtividade** (alta) — Reduzir tokens gastos por agentes de código; **Backend e APIs** (média) — Baixar o custo de chamadas de IA no produto

**[mem0ai/mem0](https://github.com/mem0ai/mem0)** · ⭐ 69,5 mil · Python · Apache-2.0

- **O que é:** Camada de memória para agentes e apps de IA: contexto persistente, pronto para produção.
- **Por que importa:** Camada de memória para agentes e apps de IA: guarda preferências e contexto entre conversas, pronta para produção.
- **Áreas:** **Backend e APIs** (alta) — Dar memória de longo prazo a um assistente do produto; **Banco de dados e dados** (média) — Persistir contexto de usuários de forma organizada

**[vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)** · ⭐ 63,8 mil · Python · MIT

- **O que é:** Memória para agentes de IA que aprende com o uso.
- **Por que importa:** Memória para agentes que aprende com as interações; alternativa a soluções de memória mais simples.
- **Áreas:** **Backend e APIs** (média) — Adicionar memória que evolui a agentes do produto
- ⚠️ Projeto recente.

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · ⭐ 60,7 mil · Python · MIT

- **O que é:** Sistema de memória para IA open source e gratuito, com bons resultados em benchmarks.
- **Por que importa:** Sistema de memória para IA open source e gratuito, com bons resultados em benchmarks.
- **Áreas:** **Backend e APIs** (média) — Testar memória de longo prazo para agentes sem custo de licença
- ⚠️ Projeto recente.


## Conhecimento do código e diagramas

**[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · ⭐ 154 mil · Python · Apache-2.0

- **O que é:** Transforma qualquer base de código (com docs, esquemas SQL, configs e PDFs) em um grafo de conhecimento consultável; skill para Claude Code, Cursor, Codex e Gemini CLI.
- **Por que importa:** Transforma o código, docs, esquemas SQL e configs em um grafo de conhecimento consultável pelo agente; melhora respostas sobre sistemas grandes.
- **Áreas:** **Arquitetura de software** (alta) — Mapear dependências e responsabilidades de um sistema legado; **Banco de dados e dados** (média) — Relacionar esquemas SQL com o código que os usa; **Engenharia e produtividade** (média) — Reduzir o tempo do agente procurando contexto em bases grandes

**[tt-a1i/archify](https://github.com/tt-a1i/archify)** · ⭐ 100,7 mil · JavaScript · Apache-2.0

- **O que é:** Transforma ideias, planos ou código em diagramas interativos ou respostas de uma página; skill para Claude Code, Codex, Cursor e outros.
- **Por que importa:** Skill que transforma ideias, planos ou código em diagramas interativos e diagnóstico de arquitetura; ajuda a explicar e revisar sistemas.
- **Áreas:** **Arquitetura de software** (alta) — Gerar diagnóstico e diagramas da arquitetura atual de um sistema; **Engenharia e produtividade** (média) — Explicar PRs e mudanças com diagramas para revisão

**[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · ⭐ 94,7 mil · TypeScript · MIT

- **O que é:** Transforma qualquer código em um grafo de conhecimento interativo para explorar, buscar e fazer perguntas.
- **Por que importa:** Grafo de conhecimento interativo do código para explorar, buscar e perguntar; ótimo para onboarding em projetos desconhecidos.
- **Áreas:** **Arquitetura de software** (alta) — Entender a estrutura de um projeto novo antes de mexer nele; **Engenharia e produtividade** (média) — Acelerar o onboarding de devs em sistemas grandes

**[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · ⭐ 78,8 mil · TypeScript · MIT

- **O que é:** Grafo de conhecimento do código pré-indexado e sincronizado, para agentes gastarem menos tokens; roda 100% local.
- **Por que importa:** Grafo do código pré-indexado e sincronizado para agentes; menos tokens e menos chamadas de ferramenta, tudo local.
- **Áreas:** **Engenharia e produtividade** (alta) — Deixar o agente mais rápido e barato em repositórios grandes; **Arquitetura de software** (média) — Consultar dependências entre módulos durante refatorações

**[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** · ⭐ 74,1 mil · HTML · MIT

- **O que é:** Skill de design de diagramas editoriais para agentes de código: 52 tipos, em HTML + SVG autocontido.
- **Por que importa:** Skill que ensina o agente a gerar diagramas editoriais limpos (52 tipos) em HTML + SVG; melhor que diagramas genéricos em Mermaid.
- **Áreas:** **Arquitetura de software** (alta) — Gerar diagramas de arquitetura e fluxos com visual profissional; **Design e UI/UX** (média) — Produzir diagramas para documentação e apresentações


## RAG e processamento de documentos

**[microsoft/markitdown](https://github.com/microsoft/markitdown)** · ⭐ 198,7 mil · Python · MIT

- **O que é:** Ferramenta em Python para converter arquivos e documentos do Office em Markdown.
- **Por que importa:** Converte PDF, Word, Excel, PowerPoint e outros em Markdown, o formato que LLMs entendem melhor; peça simples e muito útil em pipelines de IA.
- **Áreas:** **Backend e APIs** (alta) — Converter documentos enviados por usuários antes de mandar para a IA; **Banco de dados e dados** (média) — Padronizar documentos para indexação em RAG

**[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · ⭐ 94,8 mil · Go · Apache-2.0

- **O que é:** Motor de RAG (geração aumentada por recuperação) que virou infraestrutura de contexto para agentes.
- **Por que importa:** Motor de RAG focado em entendimento profundo de documentos (tabelas, layouts); bom para bases de conhecimento complexas.
- **Áreas:** **Backend e APIs** (alta) — Responder perguntas sobre contratos, manuais e PDFs com citações; **Banco de dados e dados** (média) — Estruturar documentos complexos para consulta

**[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** · ⭐ 93,4 mil · Python · Apache-2.0

- **O que é:** Kit de OCR que transforma PDFs e imagens em dados estruturados para IA, com suporte a mais de 100 idiomas.
- **Por que importa:** Kit de OCR leve e preciso que transforma imagens e PDFs escaneados em dados estruturados, com mais de 100 idiomas.
- **Áreas:** **Backend e APIs** (alta) — Ler documentos escaneados (notas, formulários) e extrair campos; **Banco de dados e dados** (média) — Digitalizar documentos em papel para o banco de dados

**[opendatalab/MinerU](https://github.com/opendatalab/MinerU)** · ⭐ 84,4 mil · Python · outra

- **O que é:** Converte documentos complexos (PDF, Office) em Markdown/JSON prontos para LLMs.
- **Por que importa:** Converte PDFs e documentos complexos em Markdown/JSON prontos para LLMs, preservando fórmulas e tabelas.
- **Áreas:** **Backend e APIs** (alta) — Processar PDFs de fornecedores ou contratos antes da análise por IA; **Banco de dados e dados** (média) — Extrair tabelas de documentos para o banco

**[redis/redis](https://github.com/redis/redis)** · ⭐ 77,8 mil · C · outra

- **O que é:** Redis: cache e banco em memória para aplicações em tempo real, com estruturas de dados, documentos e busca vetorial.
- **Por que importa:** Cache e banco em memória com estruturas de dados e busca vetorial; peça comum em sistemas com IA para cache, filas e memória semântica.
- **Áreas:** **Banco de dados e dados** (alta) — Usar busca vetorial e cache de respostas de LLM; **Backend e APIs** (alta) — Cache, filas e sessões para APIs de alto desempenho; **Arquitetura de software** (média) — Reduzir latência com uma camada de cache bem desenhada

**[tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)** · ⭐ 77,7 mil · C++ · Apache-2.0

- **O que é:** Tesseract: motor de OCR open source.
- **Por que importa:** Motor de OCR open source clássico e estável; base de muitas soluções de leitura de documentos.
- **Áreas:** **Backend e APIs** (média) — Adicionar OCR simples a um fluxo de documentos

**[docling-project/docling](https://github.com/docling-project/docling)** · ⭐ 71,1 mil · Python · MIT

- **O que é:** Prepara seus documentos para IA generativa (conversão e extração estruturada).
- **Por que importa:** Extrai a estrutura de documentos (tabelas, títulos, layout) e prepara para IA generativa.
- **Áreas:** **Backend e APIs** (alta) — Extrair tabelas e textos de PDFs com precisão para processamento por IA; **Banco de dados e dados** (média) — Transformar documentos em dados estruturados

**[pathwaycom/pathway](https://github.com/pathwaycom/pathway)** · ⭐ 62 mil · Python · outra

- **O que é:** Framework Python de ETL para processamento em streaming, analytics em tempo real, pipelines de LLM e RAG.
- **Por que importa:** Framework Python de ETL em streaming com pipelines de LLM e RAG que se atualizam em tempo real.
- **Áreas:** **Banco de dados e dados** (alta) — Manter índices de RAG sincronizados com dados que mudam o tempo todo; **Backend e APIs** (média) — Processar eventos em tempo real com etapas de IA

**[meilisearch/meilisearch](https://github.com/meilisearch/meilisearch)** · ⭐ 60 mil · Rust · outra

- **O que é:** Meilisearch: API de busca muito rápida, com busca híbrida por IA, para sites e aplicações.
- **Por que importa:** Motor de busca muito rápido com busca híbrida (texto + vetores); simples de operar comparado a soluções maiores.
- **Áreas:** **Backend e APIs** (alta) — Adicionar busca instantânea e semântica ao produto; **Banco de dados e dados** (média) — Indexar catálogos e documentos para busca com relevância

**[pathwaycom/serviette](https://github.com/pathwaycom/serviette)** · ⭐ 58,7 mil · Python · MIT

- **O que é:** Servidor de RAG sem código que mantém as respostas sincronizadas com seus documentos.
- **Por que importa:** Servidor de RAG sem código que mantém as respostas sincronizadas com seus documentos e funciona com vários bancos vetoriais.
- **Áreas:** **Backend e APIs** (média) — Subir um serviço de perguntas e respostas sobre documentos rapidamente; **Banco de dados e dados** (média) — Testar diferentes bancos vetoriais sem reescrever código
- ⚠️ Projeto recente.

**[zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)** · ⭐ 57,7 mil · Python · Apache-2.0

- **O que é:** Camada de API completa para aplicações de IA privadas com modelos locais: RAG, ferramentas, MCP e texto para SQL.
- **Por que importa:** Camada de API completa para IA privada com modelos locais: RAG, ferramentas, MCP e texto para SQL.
- **Áreas:** **Backend e APIs** (alta) — Expor IA privada para o sistema sem enviar dados a terceiros; **Banco de dados e dados** (média) — Consultar o banco em linguagem natural (texto para SQL); **Segurança e cibersegurança** (média) — Atender requisitos de privacidade mantendo modelos e dados locais

**[run-llama/llama_index](https://github.com/run-llama/llama_index)** · ⭐ 53 mil · Python · MIT

- **O que é:** LlamaIndex: plataforma de processamento de documentos para IA.
- **Por que importa:** Framework para conectar dados próprios a LLMs: ingestão, indexação e consulta de documentos.
- **Áreas:** **Backend e APIs** (alta) — Implementar RAG sobre documentos e bancos da empresa; **Banco de dados e dados** (média) — Indexar fontes de dados variadas para consulta por IA


## Modelos, inferência e gateways

**[ollama/ollama](https://github.com/ollama/ollama)** · ⭐ 188,3 mil · Go · MIT

- **O que é:** Roda modelos de IA localmente (Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma e outros).
- **Por que importa:** Forma mais simples de rodar LLMs abertos localmente com uma API; ideal para desenvolvimento, privacidade e reduzir custo.
- **Áreas:** **Backend e APIs** (alta) — Integrar o sistema a um LLM local via API compatível; **Segurança e cibersegurança** (média) — Processar dados sensíveis sem enviá-los a provedores externos; **DevOps e infraestrutura** (média) — Servir modelos internos em servidores próprios

**[Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)** · ⭐ 148,8 mil · Python · GPL-3.0

- **O que é:** Interface, API e backend modulares para modelos de difusão (imagens com IA) em formato de grafo de nós.
- **Por que importa:** Interface e backend em nós para modelos de difusão (imagem e vídeo); permite montar pipelines de geração reproduzíveis e expor como API.
- **Áreas:** **Design e UI/UX** (média) — Gerar imagens e variações de assets com pipelines controlados; **Backend e APIs** (média) — Expor geração de imagens como serviço para o produto

**[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · ⭐ 136,5 mil · C++ · MIT

- **O que é:** Inferência de LLMs em C/C++.
- **Por que importa:** Motor de inferência de LLMs em C/C++ que roda até em CPU; base do Ollama e de muitas ferramentas locais.
- **Áreas:** **Backend e APIs** (média) — Embutir inferência local eficiente em aplicações; **DevOps e infraestrutura** (média) — Rodar modelos em hardware modesto ou na borda

**[openai/whisper](https://github.com/openai/whisper)** · ⭐ 113,6 mil · Python · MIT

- **O que é:** Whisper: reconhecimento de fala robusto da OpenAI.
- **Por que importa:** Modelo de reconhecimento de fala robusto e multilíngue (inclui português); base para transcrição em produtos.
- **Áreas:** **Backend e APIs** (alta) — Transcrever áudios e reuniões dentro do sistema

**[deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3)** · ⭐ 104,9 mil · Python · MIT

- **O que é:** Modelo de linguagem DeepSeek-V3.
- **Por que importa:** Modelo de linguagem aberto de alto desempenho; opção para rodar ou contratar IA com custo menor.
- **Áreas:** **Backend e APIs** (média) — Usar um modelo aberto forte em funcionalidades de texto e código

**[vllm-project/vllm](https://github.com/vllm-project/vllm)** · ⭐ 97,7 mil · Python · Apache-2.0

- **O que é:** Motor de inferência e serving de LLMs com alta vazão e uso eficiente de memória.
- **Por que importa:** Servidor de inferência de LLMs com alta vazão e uso eficiente de GPU; padrão para servir modelos abertos em produção.
- **Áreas:** **DevOps e infraestrutura** (alta) — Servir modelos abertos em produção com bom desempenho por GPU; **Backend e APIs** (média) — Oferecer API compatível com OpenAI para os serviços internos

**[deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)** · ⭐ 92,1 mil · MIT

- **O que é:** Modelo de raciocínio DeepSeek-R1.
- **Por que importa:** Modelo aberto de raciocínio; útil para tarefas que exigem passo a passo, como análise e planejamento.
- **Áreas:** **Backend e APIs** (média) — Aplicar raciocínio em tarefas complexas com modelo aberto

**[nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all)** · ⭐ 77,3 mil · C++ · MIT

- **O que é:** GPT4All: roda LLMs localmente em qualquer dispositivo; open source e liberado para uso comercial.
- **Por que importa:** Roda LLMs localmente em qualquer computador, com app desktop e SDK; liberado para uso comercial.
- **Áreas:** **Backend e APIs** (média) — Adicionar IA local a aplicações desktop ou internas

**[BerriAI/litellm](https://github.com/BerriAI/litellm)** · ⭐ 64 mil · Python · outra

- **O que é:** Gateway de IA: chame mais de 100 APIs de LLM no formato da OpenAI, com controle de custo, guardrails, balanceamento e logs.
- **Por que importa:** Gateway que chama mais de 100 APIs de LLM no mesmo formato, com controle de custos, limites, fallback e logs.
- **Áreas:** **Backend e APIs** (alta) — Centralizar chamadas de IA do sistema com troca fácil de provedor; **Arquitetura de software** (alta) — Desacoplar o produto de um fornecedor de modelo específico; **DevOps e infraestrutura** (média) — Monitorar custo e uso de IA por time ou cliente

**[ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)** · ⭐ 55,6 mil · C++ · MIT

- **O que é:** Versão em C/C++ do modelo Whisper da OpenAI (transcrição de fala).
- **Por que importa:** Versão eficiente do Whisper em C/C++ que roda localmente até em CPU e dispositivos menores.
- **Áreas:** **Backend e APIs** (média) — Transcrição local e rápida sem depender de API

**[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** · ⭐ 52,6 mil · Go · AGPL-3.0

- **O que é:** Gateway de IA auto-hospedado com APIs compatíveis com OpenAI, Claude e Gemini, controle de acesso e contabilidade de custos.
- **Por que importa:** Gateway de IA auto-hospedado com APIs compatíveis com OpenAI, Claude e Gemini, controle de acesso e contabilidade de custos.
- **Áreas:** **Backend e APIs** (média) — Distribuir acesso a modelos para vários sistemas com cotas e chaves próprias; **DevOps e infraestrutura** (média) — Controlar gastos com IA por projeto

**[mudler/LocalAI](https://github.com/mudler/LocalAI)** · ⭐ 50,6 mil · Go · MIT

- **O que é:** LocalAI: motor de IA open source para rodar LLMs, visão, voz, imagem e vídeo em qualquer hardware, sem GPU.
- **Por que importa:** Motor de IA open source compatível com a API da OpenAI para texto, imagem, voz e vídeo, sem exigir GPU.
- **Áreas:** **Backend e APIs** (alta) — Trocar a API da OpenAI por uma local sem mudar o código; **DevOps e infraestrutura** (média) — Rodar IA em servidores próprios sem GPU


## Treino e frameworks de ML

**[tensorflow/tensorflow](https://github.com/tensorflow/tensorflow)** · ⭐ 201,9 mil · C++ · Apache-2.0

- **O que é:** Framework open source de Machine Learning.
- **Por que importa:** Framework de machine learning do Google, forte em produção e em dispositivos (TensorFlow Lite).
- **Áreas:** **Backend e APIs** (média) — Servir modelos de ML em produção ou em dispositivos móveis

**[huggingface/transformers](https://github.com/huggingface/transformers)** · ⭐ 169,4 mil · Python · Apache-2.0

- **O que é:** Transformers: framework de definição de modelos de ML de ponta para texto, visão, áudio e multimodal, em inferência e treino.
- **Por que importa:** Biblioteca padrão para usar e ajustar modelos de texto, visão e áudio do Hugging Face.
- **Áreas:** **Backend e APIs** (alta) — Usar modelos prontos de classificação, extração e embeddings no backend; **Banco de dados e dados** (média) — Gerar embeddings para busca semântica

**[pytorch/pytorch](https://github.com/pytorch/pytorch)** · ⭐ 105,8 mil · Python · outra

- **O que é:** PyTorch: tensores e redes neurais dinâmicas em Python com aceleração por GPU.
- **Por que importa:** Framework de deep learning mais usado em pesquisa e produção; base de boa parte dos modelos atuais.
- **Áreas:** **Backend e APIs** (média) — Treinar ou servir modelos próprios quando APIs prontas não atendem

**[opencv/opencv](https://github.com/opencv/opencv)** · ⭐ 91,7 mil · C++ · Apache-2.0

- **O que é:** OpenCV: biblioteca open source de visão computacional.
- **Por que importa:** Biblioteca de visão computacional mais usada; base para processamento de imagens e vídeo.
- **Áreas:** **Backend e APIs** (média) — Processar imagens (recorte, detecção, leitura) no backend

**[unslothai/unsloth](https://github.com/unslothai/unsloth)** · ⭐ 80,3 mil · Python · Apache-2.0

- **O que é:** Interface local para rodar e treinar LLMs e modelos de difusão, com suporte a vários formatos e modelos.
- **Por que importa:** Ajuste fino (fine-tuning) de LLMs mais rápido e com menos memória, com interface local.
- **Áreas:** **Backend e APIs** (média) — Especializar um modelo aberto no vocabulário e nas tarefas do cliente

**[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** · ⭐ 76,3 mil · Python · Apache-2.0

- **O que é:** Fine-tuning eficiente e unificado de mais de 100 LLMs e modelos de visão e linguagem.
- **Por que importa:** Ajuste fino unificado de mais de 100 LLMs e modelos de visão, com interface web.
- **Áreas:** **Backend e APIs** (média) — Fazer fine-tuning de modelos abertos sem montar o pipeline do zero

**[scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)** · ⭐ 68,4 mil · Python · BSD-3-Clause

- **O que é:** scikit-learn: Machine Learning em Python.
- **Por que importa:** Biblioteca clássica de ML em Python (classificação, regressão, clustering); resolve muitos problemas sem LLM.
- **Áreas:** **Banco de dados e dados** (alta) — Criar modelos de previsão e segmentação com os dados do negócio; **Backend e APIs** (média) — Embutir modelos simples e baratos em APIs

**[keras-team/keras](https://github.com/keras-team/keras)** · ⭐ 64,5 mil · Python · Apache-2.0

- **O que é:** Keras: deep learning para humanos.
- **Por que importa:** API de alto nível para deep learning, simples de aprender; boa porta de entrada para treinar modelos.
- **Áreas:** **Backend e APIs** (média) — Prototipar modelos de ML com pouco código

**[ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)** · ⭐ 63,8 mil · Python · AGPL-3.0

- **O que é:** Ultralytics YOLO: detecção de objetos, segmentação, classificação, pose e rastreamento.
- **Por que importa:** YOLO moderno para detecção, segmentação e rastreamento de objetos, fácil de treinar e exportar.
- **Áreas:** **Backend e APIs** (média) — Detectar objetos em imagens ou câmeras dentro do produto
- ⚠️ Licença AGPL: verifique antes de uso comercial fechado.


## Design e interfaces com IA

**[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · ⭐ 154,8 mil · Python · MIT

- **O que é:** Skill de IA com conhecimento de design para criar UI/UX profissional em várias plataformas.
- **Por que importa:** Skill com conhecimento de design (estilos, paletas, tipografia, padrões de UX) para o agente criar interfaces profissionais.
- **Áreas:** **Design e UI/UX** (alta) — Dar ao agente referências de estilo e UX ao criar telas; **Frontend** (alta) — Gerar páginas e componentes com visual consistente

**[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · ⭐ 129,3 mil · MIT

- **O que é:** Coleção de arquivos DESIGN.md com análises de design systems de marcas famosas, para agentes de código gerarem interfaces no mesmo estilo.
- **Por que importa:** Arquivos DESIGN.md baseados em design systems de marcas conhecidas; você coloca um no projeto e o agente gera UI coerente com aquele estilo.
- **Áreas:** **Design e UI/UX** (alta) — Dar ao agente um design system de referência em um único arquivo; **Frontend** (alta) — Gerar interfaces consistentes com o estilo escolhido

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** · ⭐ 122,1 mil · JavaScript · MIT

- **O que é:** Skills que dão "bom gosto" visual a agentes de código: direção de arte, imagens de referência e checagem no navegador.
- **Por que importa:** Skills que dão direção de arte ao agente e conferem o resultado no navegador; evita páginas com cara de 'gerado por IA'.
- **Áreas:** **Design e UI/UX** (alta) — Definir direção de arte e referências antes de o agente criar a interface; **Frontend** (média) — Checar visualmente no navegador o que foi gerado

**[pbakaus/impeccable](https://github.com/pbakaus/impeccable)** · ⭐ 117,7 mil · Rust · Apache-2.0

- **O que é:** Vocabulário de design para agentes de código: refinar, revisar, auditar e barrar interfaces genéricas de IA.
- **Por que importa:** Vocabulário de design para agentes de código: comandos para refinar, revisar e auditar interfaces.
- **Áreas:** **Design e UI/UX** (alta) — Revisar e polir interfaces geradas com comandos de crítica e auditoria; **Frontend** (média) — Ajustar hierarquia visual e espaçamentos com o agente

**[nexu-io/open-design](https://github.com/nexu-io/open-design)** · ⭐ 109,7 mil · TypeScript · Apache-2.0

- **O que é:** Workspace colaborativo de design com agentes de IA, local e open source: protótipos, sites, apps, dashboards, apresentações, imagens e vídeos.
- **Por que importa:** Workspace colaborativo de design com agentes de IA para protótipos, sites, apps e dashboards; local e open source.
- **Áreas:** **Design e UI/UX** (alta) — Prototipar telas e fluxos com IA junto com o time; **Frontend** (média) — Transformar protótipos em páginas e componentes
- ⚠️ Projeto recente; avalie estabilidade.

**[abi/screenshot-to-code](https://github.com/abi/screenshot-to-code)** · ⭐ 81,5 mil · Python · MIT

- **O que é:** Converte uma captura de tela em código limpo (HTML/Tailwind/React/Vue).
- **Por que importa:** Transforma uma captura de tela ou mockup em código HTML/Tailwind/React/Vue; acelera a passagem do design para o front.
- **Áreas:** **Frontend** (alta) — Gerar a primeira versão de uma tela a partir de um print ou layout; **Design e UI/UX** (média) — Validar rapidamente um layout transformando-o em protótipo navegável

**[Nutlope/hallmark](https://github.com/Nutlope/hallmark)** · ⭐ 61,8 mil · CSS · MIT

- **O que é:** Skill de design contra interfaces genéricas geradas por IA, para Claude Code, Cursor e Codex.
- **Por que importa:** Skill de design contra interfaces genéricas de IA para Claude Code, Cursor e Codex.
- **Áreas:** **Design e UI/UX** (alta) — Evitar layouts genéricos em landing pages e telas geradas por IA; **Frontend** (média) — Melhorar o acabamento de páginas feitas com agentes


## Segurança com IA

**[morluto/rea](https://github.com/morluto/rea)** · ⭐ 480,3 mil · TypeScript · MIT

- **O que é:** Ferramenta com agentes de IA para engenharia reversa, do comportamento de aplicativos até binários nativos, com integração a assistentes de código como o Claude Code.
- **Por que importa:** Agentes de IA para engenharia reversa de apps e binários; pode acelerar auditorias de segurança e análise de integrações sem documentação.
- **Áreas:** **Segurança e cibersegurança** (média) — Analisar binários e comportamento de apps em auditorias
- ⚠️ Projeto muito recente com crescimento de estrelas fora do comum; avalie maturidade e implicações legais.

**[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** · ⭐ 79 mil · JavaScript · MIT

- **O que é:** Skill para agentes de código fazerem auditorias de segurança em várias fases, com achados verificados.
- **Por que importa:** Skill da Cloudflare para auditorias de segurança em várias fases com achados verificados; leva revisão de segurança para dentro do agente de código.
- **Áreas:** **Segurança e cibersegurança** (alta) — Fazer auditoria de segurança do código com o próprio agente; **Testes e QA** (média) — Gerar relatório de achados verificados para correção

**[usestrix/strix](https://github.com/usestrix/strix)** · ⭐ 77,9 mil · Python · Apache-2.0

- **O que é:** Ferramenta open source de pentest com IA para encontrar e corrigir vulnerabilidades da sua aplicação.
- **Por que importa:** Pentest com IA open source: agentes que encontram e ajudam a corrigir vulnerabilidades da aplicação.
- **Áreas:** **Segurança e cibersegurança** (alta) — Rodar testes de invasão automatizados antes de publicar; **Testes e QA** (média) — Incluir verificação de segurança no ciclo de testes

**[KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)** · ⭐ 52,4 mil · TypeScript · AGPL-3.0

- **O que é:** Pentester com IA para aplicações web e APIs: analisa o código e executa ataques reais para provar vulnerabilidades.
- **Por que importa:** Pentester com IA para aplicações web e APIs: lê o código, identifica vetores de ataque e executa explorações reais para provar falhas.
- **Áreas:** **Segurança e cibersegurança** (alta) — Validar vulnerabilidades reais em APIs antes da produção; **Backend e APIs** (média) — Auditar endpoints e autenticação do backend
- ⚠️ Use só em sistemas próprios ou com autorização.


## Gestão de agentes e produtividade

**[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · ⭐ 157,6 mil · Rust · MIT

- **O que é:** Assistente de desktop multiplataforma para gerenciar Claude Code, Codex, OpenCode, DeepSeek Harness e outros.
- **Por que importa:** Assistente desktop para alternar e configurar Claude Code, Codex, OpenCode e outros num só lugar.
- **Áreas:** **Engenharia e produtividade** (média) — Gerenciar configurações e provedores de vários agentes de código

**[stablyai/orca](https://github.com/stablyai/orca)** · ⭐ 141,4 mil · TypeScript · MIT

- **O que é:** Roda uma frota de bots usando sua própria assinatura (Claude Code, Grok, Codex etc.), no desktop, no celular ou remoto.
- **Por que importa:** Roda uma frota de agentes de código usando suas assinaturas, no desktop, celular ou remoto.
- **Áreas:** **Engenharia e produtividade** (média) — Paralelizar tarefas entre vários agentes de código
- ⚠️ Projeto recente.

**[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · ⭐ 117,5 mil · TypeScript · MIT

- **O que é:** App open source para gerenciar agentes de IA no trabalho.
- **Por que importa:** App open source para gerenciar agentes de IA no trabalho: tarefas, papéis e acompanhamento.
- **Áreas:** **Engenharia e produtividade** (média) — Organizar o trabalho de vários agentes como se fossem membros do time
- ⚠️ Projeto recente.

**[pingdotgg/t3code](https://github.com/pingdotgg/t3code)** · ⭐ 81,5 mil · TypeScript · MIT

- **O que é:** Controle o Claude Code, o Codex e outros a partir de qualquer computador ou celular.
- **Por que importa:** Controla Claude Code, Codex e outros a partir de qualquer computador ou celular.
- **Áreas:** **Engenharia e produtividade** (média) — Acompanhar e comandar agentes de código remotamente

**[multica-ai/multica](https://github.com/multica-ai/multica)** · ⭐ 58,1 mil · Go · outra

- **O que é:** Quadro de tarefas compartilhado em que pessoas e agentes de código trabalham como colegas de time; auto-hospedável.
- **Por que importa:** Quadro de tarefas compartilhado em que pessoas e agentes de código trabalham juntos; auto-hospedável.
- **Áreas:** **Engenharia e produtividade** (média) — Distribuir tarefas entre devs e agentes no mesmo quadro
- ⚠️ Licença source-available; confira os termos.

**[herdrdev/herdr](https://github.com/herdrdev/herdr)** · ⭐ 53,1 mil · Rust · Apache-2.0

- **O que é:** Runtime onde seus agentes de código rodam.
- **Por que importa:** Runtime para hospedar e gerenciar agentes de código em execução.
- **Áreas:** **Engenharia e produtividade** (média) — Manter agentes de código rodando e organizados em sessões; **DevOps e infraestrutura** (média) — Padronizar onde e como os agentes rodam
- ⚠️ Projeto recente.


## Aprendizado de IA

**[Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)** · ⭐ 145,9 mil · Python · Apache-2.0

- **O que é:** Mais de 100 agentes de IA, skills e apps de RAG gratuitos e open source.
- **Por que importa:** Mais de 100 exemplos de agentes, skills e apps de RAG com código; ótimo catálogo de ideias e referências de implementação.
- **Áreas:** **Backend e APIs** (média) — Copiar padrões de implementação de agentes e RAG; **Arquitetura de software** (média) — Comparar arquiteturas de apps com LLM antes de escolher a sua

**[microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)** · ⭐ 124,4 mil · Jupyter Notebook · MIT

- **O que é:** 21 aulas para começar a construir com IA generativa (Microsoft).
- **Por que importa:** Curso gratuito da Microsoft em 21 aulas para construir aplicações com IA generativa.
- **Áreas:** **Backend e APIs** (média) — Aprender a integrar LLMs em aplicações reais

**[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)** · ⭐ 109,1 mil · Jupyter Notebook · outra

- **O que é:** Implemente um LLM no estilo ChatGPT em PyTorch do zero, passo a passo.
- **Por que importa:** Livro e código para implementar um LLM do zero em PyTorch; entendimento profundo de como os modelos funcionam.
- **Áreas:** **Backend e APIs** (média) — Entender o funcionamento interno de LLMs para usá-los melhor

**[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · ⭐ 98,6 mil · MIT

- **O que é:** Coleção de servidores MCP.
- **Por que importa:** Coleção de servidores MCP prontos; atalho para conectar agentes a bancos, APIs e serviços sem programar a integração.
- **Áreas:** **Backend e APIs** (média) — Encontrar servidores MCP prontos para os serviços que o projeto usa; **Banco de dados e dados** (média) — Achar MCPs de bancos de dados para consultas assistidas
- ⚠️ Lista de links; verifique segurança de cada servidor.

**[microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners)** · ⭐ 92,5 mil · Jupyter Notebook · MIT

- **O que é:** Curso de Machine Learning clássico em 12 semanas e 26 aulas (Microsoft).
- **Por que importa:** Curso de 12 semanas da Microsoft sobre machine learning clássico.
- **Áreas:** **Banco de dados e dados** (média) — Aprender a criar modelos simples com dados do negócio

**[mlabonne/llm-course](https://github.com/mlabonne/llm-course)** · ⭐ 85,3 mil · Apache-2.0

- **O que é:** Curso para aprender LLMs, com roteiros e notebooks no Colab.
- **Por que importa:** Curso com roteiros e notebooks sobre LLMs: fundamentos, ajuste fino e engenharia de aplicações.
- **Áreas:** **Backend e APIs** (média) — Estudar desde fundamentos até deploy de aplicações com LLM

**[microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)** · ⭐ 81,1 mil · Jupyter Notebook · MIT

- **O que é:** 18 aulas para começar a construir agentes de IA (Microsoft).
- **Por que importa:** Curso gratuito da Microsoft em 18 aulas sobre como construir agentes de IA.
- **Áreas:** **Backend e APIs** (média) — Aprender padrões de agentes (ferramentas, planejamento, memória); **Arquitetura de software** (média) — Conhecer padrões de design de sistemas com agentes

**[shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)** · ⭐ 81 mil · Python · MIT

- **O que é:** Constrói do zero um "agente de código" mínimo parecido com o Claude Code, usando basicamente Bash.
- **Por que importa:** Constrói do zero um agente de código mínimo para entender como ferramentas como o Claude Code funcionam por dentro.
- **Áreas:** **Engenharia e produtividade** (média) — Entender o funcionamento de agentes para usá-los e customizá-los melhor; **Arquitetura de software** (média) — Estudar a arquitetura de um agente de código

**[rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)** · ⭐ 80,7 mil · Python · MIT

- **O que é:** Aprenda engenharia de IA do zero: estude, construa e publique.
- **Por que importa:** Trilha prática de engenharia de IA: aprender, construir e publicar aplicações.
- **Áreas:** **Backend e APIs** (média) — Aprender a levar funcionalidades de IA até produção
- ⚠️ Projeto recente.

**[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** · ⭐ 80,4 mil · Python

- **O que é:** Lista curada de Skills do Claude, recursos e ferramentas para personalizar fluxos de trabalho.
- **Por que importa:** Lista curada de Skills do Claude e ferramentas; atalho para encontrar skills prontas antes de criar as suas.
- **Áreas:** **Engenharia e produtividade** (média) — Procurar skills prontas para tarefas recorrentes do time
- ⚠️ É uma lista de links, não um software.

**[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** · ⭐ 80,4 mil · MDX · MIT

- **O que é:** Guias, artigos, aulas e notebooks sobre engenharia de prompt, engenharia de contexto, RAG e agentes de IA.
- **Por que importa:** Guia completo de engenharia de prompt, contexto, RAG e agentes; referência para escrever prompts e skills melhores.
- **Áreas:** **Engenharia e produtividade** (alta) — Melhorar prompts, skills e instruções para agentes; **Backend e APIs** (média) — Projetar prompts robustos para funcionalidades de IA

**[openai/openai-cookbook](https://github.com/openai/openai-cookbook)** · ⭐ 77,5 mil · Jupyter Notebook · MIT

- **O que é:** Exemplos e guias de uso da API da OpenAI.
- **Por que importa:** Exemplos e guias oficiais de uso da API da OpenAI (RAG, embeddings, ferramentas, avaliação).
- **Áreas:** **Backend e APIs** (alta) — Copiar padrões testados de integração com LLMs

**[josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning)** · ⭐ 74,9 mil · Python · outra

- **O que é:** Lista curada de frameworks, bibliotecas e softwares de Machine Learning.
- **Por que importa:** Lista curada de frameworks e bibliotecas de ML por linguagem; ajuda a achar a ferramenta certa.
- **Áreas:** **Backend e APIs** (média) — Encontrar bibliotecas de ML para a linguagem do projeto
- ⚠️ É uma lista de links, não um software.

**[microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)** · ⭐ 71,3 mil · Jupyter Notebook · MIT

- **O que é:** Curso de IA em 12 semanas e 24 aulas (Microsoft).
- **Por que importa:** Curso de 12 semanas da Microsoft com os fundamentos de IA.
- **Áreas:** **Engenharia e produtividade** (média) — Formar base em IA para o time

**[karpathy/nanochat](https://github.com/karpathy/nanochat)** · ⭐ 60,9 mil · Python · MIT

- **O que é:** O melhor ChatGPT que 100 dólares conseguem treinar: LLM completo de ponta a ponta.
- **Por que importa:** Implementação completa e enxuta de um ChatGPT (treino, ajuste e interface) para estudo.
- **Áreas:** **Backend e APIs** (média) — Entender o ciclo completo de um LLM de ponta a ponta

**[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · ⭐ 58,9 mil · Python · outra

- **O que é:** Coleção selecionada de recursos para o Claude Code: skills, agentes, status lines, ferramentas e plugins.
- **Por que importa:** Coleção selecionada de skills, agentes, hooks e plugins para o Claude Code; boa vitrine do que a comunidade usa.
- **Áreas:** **Engenharia e produtividade** (média) — Descobrir hooks, comandos e plugins para melhorar o fluxo com o Claude Code
- ⚠️ É uma lista de links, não um software.

**[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)** · ⭐ 55,3 mil · Jupyter Notebook · MIT

- **O que é:** Coleção de notebooks e receitas com formas eficazes de usar o Claude.
- **Por que importa:** Notebooks oficiais com receitas de uso do Claude: ferramentas, RAG, agentes e boas práticas.
- **Áreas:** **Backend e APIs** (alta) — Implementar integrações com o Claude seguindo exemplos oficiais; **Engenharia e produtividade** (média) — Aprender técnicas de uso de ferramentas e contexto

**[VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)** · ⭐ 54 mil · MIT

- **O que é:** Coleção de mais de 5.400 skills do OpenClaw filtradas e organizadas por categoria.
- **Por que importa:** Coleção organizada de skills do OpenClaw; referência de ideias de automação com agentes.
- **Áreas:** **Engenharia e produtividade** (média) — Encontrar exemplos de skills para automações com agentes
- ⚠️ Lista de links; qualidade varia.

**[GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML)** · ⭐ 50,2 mil · Jupyter Notebook · MIT

- **O que é:** Aprenda a desenvolver, publicar e iterar aplicações de ML em produção.
- **Por que importa:** Ensina a desenvolver, publicar e iterar aplicações de ML em produção (MLOps).
- **Áreas:** **DevOps e infraestrutura** (média) — Aprender práticas de MLOps: versionamento, deploy e monitoramento de modelos; **Testes e QA** (média) — Testar dados e modelos de ML
