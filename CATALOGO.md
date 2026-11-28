# Radar de IA para entregar software — repositórios com 20 mil+ estrelas

Atualizado em 28/11/2026 · **372** repositórios no foco (de 2289 com 20 mil+ estrelas) · com explicação completa: 224/372

**Foco:** IA para construir e entregar software melhor: agentes, skills, agentes de código, MCP, LLMs, RAG e ferramentas de IA para arquitetura, engenharia, design, frontend, backend, banco de dados, segurança, testes e DevOps.

**Por área:** [Arquitetura de software](areas/arquitetura-de-software.md) · [Engenharia e produtividade](areas/engenharia-e-produtividade.md) · [Design e UI/UX](areas/design-e-ui-ux.md) · [Frontend](areas/frontend.md) · [Backend e APIs](areas/backend-e-apis.md) · [Banco de dados e dados](areas/banco-de-dados-e-dados.md) · [Segurança e cibersegurança](areas/seguranca-e-ciberseguranca.md) · [Testes e QA](areas/testes-e-qa.md) · [DevOps e infraestrutura](areas/devops-e-infraestrutura.md)

## Categorias

- [Agentes de código](#agentes-de-código) (32)
- [Skills e configurações para agentes](#skills-e-configurações-para-agentes) (41)
- [Frameworks de agentes e orquestração](#frameworks-de-agentes-e-orquestração) (60)
- [Plataformas de IA e automação](#plataformas-de-ia-e-automação) (22)
- [MCP, ferramentas e integrações](#mcp-ferramentas-e-integrações) (21)
- [Memória, contexto e economia de tokens](#memória-contexto-e-economia-de-tokens) (12)
- [Conhecimento do código e diagramas](#conhecimento-do-código-e-diagramas) (8)
- [RAG e processamento de documentos](#rag-e-processamento-de-documentos) (34)
- [Modelos, inferência e gateways](#modelos-inferência-e-gateways) (44)
- [Treino e frameworks de ML](#treino-e-frameworks-de-ml) (30)
- [Design e interfaces com IA](#design-e-interfaces-com-ia) (12)
- [Segurança com IA](#segurança-com-ia) (10)
- [Gestão de agentes e produtividade](#gestão-de-agentes-e-produtividade) (8)
- [Aprendizado de IA](#aprendizado-de-ia) (27)
- [Outros](#outros) (11)

## Agentes de código

**[anomalyco/opencode](https://github.com/anomalyco/opencode)** · ⭐ 229,7 mil · TypeScript · MIT

- **O que é:** Agente de programação open source.
- **Por que importa:** Agente de código open source que funciona com vários provedores de modelo; evita ficar preso a um fornecedor.
- **Áreas:** **Engenharia e produtividade** (alta) — Usar o mesmo fluxo de agente de código trocando entre modelos pagos e locais

**[anthropics/claude-code](https://github.com/anthropics/claude-code)** · ⭐ 157,4 mil · TypeScript

- **O que é:** Claude Code: ferramenta de programação com agente que roda no terminal, entende seu código e executa tarefas, explica código e cuida do Git em linguagem natural.
- **Por que importa:** Agente de código no terminal que lê o projeto inteiro, edita arquivos, roda testes e cuida do Git; acelera features, refatorações e correções com supervisão humana.
- **Áreas:** **Engenharia e produtividade** (alta) — Implementar features e refatorações em vários arquivos de uma vez, com plano e revisão; **Backend e APIs** (alta) — Criar endpoints, migrations e testes a partir de uma descrição da regra de negócio; **Testes e QA** (média) — Gerar e rodar testes automatizados e corrigir os que falham

**[openai/codex](https://github.com/openai/codex)** · ⭐ 136,7 mil · Rust · Apache-2.0

- **O que é:** Agente de programação leve que roda no terminal (OpenAI Codex).
- **Por que importa:** Agente de código leve da OpenAI para o terminal; boa alternativa ou complemento ao Claude Code para tarefas de implementação e revisão.
- **Áreas:** **Engenharia e produtividade** (alta) — Delegar tarefas de código pelo terminal e revisar as mudanças propostas; **Backend e APIs** (média) — Gerar código de serviços e scripts com base no repositório existente

**[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · ⭐ 109,3 mil · TypeScript · Apache-2.0

- **O que é:** Agente de IA open source que leva o Gemini para o seu terminal.
- **Por que importa:** Agente open source do Gemini no terminal, com contexto grande; útil para analisar bases de código extensas e automatizar tarefas de desenvolvimento.
- **Áreas:** **Engenharia e produtividade** (alta) — Analisar um repositório grande e propor mudanças pelo terminal; **Arquitetura de software** (média) — Ler a base inteira para mapear módulos e dependências antes de uma refatoração

**[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · ⭐ 94,5 mil · TypeScript · MIT

- **O que é:** OpenHands: desenvolvimento de software com agentes de IA.
- **Por que importa:** Plataforma open source de desenvolvimento com agentes que executam tarefas completas em sandbox; referência para automatizar issues e PRs.
- **Áreas:** **Engenharia e produtividade** (alta) — Atribuir issues simples a um agente que abre o PR em ambiente isolado; **DevOps e infraestrutura** (média) — Rodar agentes de manutenção em sandbox dentro da sua infraestrutura

**[cline/cline](https://github.com/cline/cline)** · ⭐ 72 mil · TypeScript · Apache-2.0

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

**[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** · ⭐ 57 mil · Go · Apache-2.0

- **O que é:** Ferramenta de revisão de código do Alibaba que combina regras determinísticas e agente LLM, com comentários por linha.
- **Por que importa:** Revisão de código do Alibaba que combina regras determinísticas e agente LLM, com comentários por linha (NPE, XSS, SQL injection, concorrência).
- **Áreas:** **Engenharia e produtividade** (alta) — Automatizar revisão de PRs com comentários por linha; **Segurança e cibersegurança** (alta) — Detectar XSS, SQL injection e falhas comuns antes do merge; **Testes e QA** (média) — Reduzir bugs que chegam ao QA

**[Aider-AI/aider](https://github.com/Aider-AI/aider)** · ⭐ 50,3 mil · Python · Apache-2.0

- **O que é:** aider: programação em par com IA no terminal.
- **Por que importa:** Programação em par com IA no terminal, integrada ao Git (cada mudança vira commit); muito bom para mudanças incrementais e rastreáveis.
- **Áreas:** **Engenharia e produtividade** (alta) — Fazer mudanças pequenas e rastreáveis com commits automáticos por alteração

**[codewhale-hq/Codewhale](https://github.com/codewhale-hq/Codewhale)** · ⭐ 41,2 mil · Rust · MIT

- **O que é:** Agente de código open source em Rust para terminal, web e desktop, com qualquer modelo, frotas multiagente, MCP, plugins e sandbox do sistema.
- **Por que importa:** Alternativa aberta e independente de fornecedor aos agentes de código comerciais, com isolamento em sandbox e registro de cada sessão.
- **Áreas:** **Engenharia e produtividade** (alta) — Delegar tarefas de código no terminal usando o modelo que o time já contrata ou um modelo local
- ⚠️ Projeto recente.

**[can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)** · ⭐ 40,1 mil · TypeScript · MIT

- **O que é:** Agente de código de terminal com recursos de IDE integrados, vários provedores de modelos e MCP, da Stencil Labs.
- **Por que importa:** Opção aberta e multiprovedor para quem quer um agente de terminal com mais contexto da IDE ao editar código.
- **Áreas:** **Engenharia e produtividade** (alta) — Usar como agente de código no terminal com o provedor de modelos de preferência
- ⚠️ Projeto recente.

**[continuedev/continue](https://github.com/continuedev/continue)** · ⭐ 36,6 mil · TypeScript · Apache-2.0

- **O que é:** Agente de código open source para IDE (VS Code e JetBrains) e linha de comando, compatível com qualquer modelo.
- **Por que importa:** Opção aberta e configurável para ter assistente e agente de código na IDE com modelos próprios ou locais.
- **Áreas:** **Engenharia e produtividade** (alta) — Usar um agente de código na IDE com o modelo que a empresa já aprovou

**[openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)** · ⭐ 35,5 mil · JavaScript · Apache-2.0

- **O que é:** Plugin oficial da OpenAI que permite usar o Codex de dentro do Claude Code para revisar código ou delegar tarefas.
- **Por que importa:** Facilita ter a segunda opinião de outro modelo sobre o código, sem trocar de ferramenta.
- **Áreas:** **Engenharia e produtividade** (alta) — Pedir ao Codex uma revisão das mudanças feitas no Claude Code antes do commit; **Testes e QA** (média) — Usar a revisão cruzada entre modelos para pegar bugs antes do PR

**[TabbyML/tabby](https://github.com/TabbyML/tabby)** · ⭐ 33,9 mil · Rust · outra

- **O que é:** Assistente de código com IA self-hosted, alternativa ao GitHub Copilot que roda na infraestrutura da empresa.
- **Por que importa:** Permite ter autocompletar e chat de código sem enviar o código para fora, usando modelos próprios.
- **Áreas:** **Engenharia e produtividade** (média) — Oferecer autocompletar de código com IA mantendo o código na infraestrutura interna; **DevOps e infraestrutura** (média) — Hospedar o servidor do assistente em GPU própria
- ⚠️ Sem commits desde junho de 2026 e licença mista; confira a manutenção e os termos.

**[cursor/cursor](https://github.com/cursor/cursor)** · ⭐ 33,4 mil

- **O que é:** Repositório público do Cursor, editor de código com IA (issues e feedback).

**[tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)** · ⭐ 33 mil · Python · MIT

- **O que é:** Grafo local do código para MCP e CLI, para que ferramentas de IA leiam só o que precisam.

**[oraios/serena](https://github.com/oraios/serena)** · ⭐ 31,8 mil · Python · outra

- **O que é:** Serena: kit MCP de programação com busca e edição semântica do código, a "IDE do agente".

**[alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)** · ⭐ 31,2 mil · HTML · MIT

- **O que é:** Skill de design para agentes: gera protótipos de sites e apps, apresentações e infográficos a partir de uma frase.

**[QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)** · ⭐ 31 mil · TypeScript · Apache-2.0

- **O que é:** Qwen Code: agente de código open source no terminal.

**[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** · ⭐ 30,6 mil · TypeScript · Apache-2.0

- **O que é:** Memória persistente para agentes de código.

**[jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)** · ⭐ 29,3 mil · JavaScript · MIT

- **O que é:** Plugin do Claude Code que mostra uso de contexto, ferramentas e agentes ativos.

**[openai/skills](https://github.com/openai/skills)** · ⭐ 29,2 mil · Python

- **O que é:** Catálogo oficial de skills para o Codex (OpenAI).

**[manaflow-ai/cmux](https://github.com/manaflow-ai/cmux)** · ⭐ 29 mil · Swift · outra

- **O que é:** Terminal para macOS com abas verticais e notificações pensado para agentes de código.

**[eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master)** · ⭐ 28,6 mil · JavaScript · outra

- **O que é:** Sistema de gestão de tarefas com IA para usar no Cursor, Windsurf e outros agentes.

**[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** · ⭐ 28,3 mil · Shell · MIT

- **O que é:** Planejamento persistente em arquivos Markdown para agentes de código e tarefas longas.

**[Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode)** · ⭐ 28,1 mil · TypeScript · MIT

- **O que é:** Kilo: plataforma de engenharia com agentes de código open source.

**[EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)** · ⭐ 26,3 mil · TypeScript · MIT

- **O que é:** Plugin de "compound engineering" para Claude Code, Codex e Cursor: cada tarefa deixa a próxima mais fácil.

**[getpaseo/paseo](https://github.com/getpaseo/paseo)** · ⭐ 26,1 mil · TypeScript · outra

- **O que é:** Orquestra vários agentes de código pelo desktop e pelo celular.

**[nocobase/nocobase](https://github.com/nocobase/nocobase)** · ⭐ 25 mil · TypeScript · outra

- **O que é:** NocoBase: plataforma para construir e evoluir sistemas de negócio com IA e agentes.

**[slopus/happy](https://github.com/slopus/happy)** · ⭐ 24,9 mil · Swift · MIT

- **O que é:** Orquestra Claude, Codex e Grok em um app, reaproveitando as assinaturas que você já paga.

**[winfunc/opcode](https://github.com/winfunc/opcode)** · ⭐ 22,5 mil · TypeScript · AGPL-3.0

- **O que é:** Opcode: app gráfico e toolkit para o Claude Code, com agentes personalizados e sessões interativas.


## Skills e configurações para agentes

**[mattpocock/skills](https://github.com/mattpocock/skills)** · ⭐ 334,5 mil · Shell · MIT

- **O que é:** Coleção de skills para agentes de IA voltadas a engenheiros, tiradas do diretório .agents do autor.
- **Por que importa:** Skills práticas de um engenheiro experiente para agentes de código; bons exemplos de como ensinar o agente a seguir boas práticas.
- **Áreas:** **Engenharia e produtividade** (alta) — Adotar skills prontas de engenharia e adaptá-las ao padrão do projeto; **Frontend** (média) — Melhorar o código TypeScript gerado pelo agente

**[obra/superpowers](https://github.com/obra/superpowers)** · ⭐ 328,6 mil · Shell · MIT

- **O que é:** Framework de skills para agentes de IA e metodologia de desenvolvimento de software.
- **Por que importa:** Conjunto de skills e metodologia que faz o agente trabalhar com brainstorming, plano, TDD e revisão; melhora a qualidade das entregas com IA.
- **Áreas:** **Engenharia e produtividade** (alta) — Dar ao agente um processo disciplinado: planejar, testar primeiro e revisar; **Testes e QA** (alta) — Forçar o agente a escrever testes antes do código (TDD)

**[affaan-m/ECC](https://github.com/affaan-m/ECC)** · ⭐ 312,1 mil · JavaScript · MIT

- **O que é:** Sistema para otimizar o desempenho de agentes de código (Claude Code, Codex, Cursor etc.) com skills, memória, segurança e desenvolvimento guiado por pesquisa.
- **Por que importa:** Sistema completo de skills, memória, segurança e regras para agentes de código; acelera a configuração de um ambiente de agente robusto.
- **Áreas:** **Engenharia e produtividade** (alta) — Montar rapidamente uma configuração madura de agente para o time; **Segurança e cibersegurança** (média) — Reaproveitar regras de segurança para limitar o que o agente pode fazer
- ⚠️ Projeto recente e grande; adote por partes.

**[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · ⭐ 236,4 mil

- **O que é:** Arquivo CLAUDE.md único para melhorar o comportamento do Claude Code, baseado nas observações de Andrej Karpathy sobre erros comuns de LLMs ao programar.
- **Por que importa:** Um único CLAUDE.md com regras contra os erros mais comuns de LLMs ao programar; ganho rápido de qualidade com custo zero.
- **Áreas:** **Engenharia e produtividade** (alta) — Copiar e adaptar o CLAUDE.md para reduzir erros do agente no projeto

**[anthropics/skills](https://github.com/anthropics/skills)** · ⭐ 201,7 mil · Python

- **O que é:** Repositório público de Agent Skills da Anthropic.
- **Por que importa:** Repositório oficial de Agent Skills da Anthropic: exemplos e padrão de como empacotar instruções e scripts para agentes; base para criar as suas.
- **Áreas:** **Engenharia e produtividade** (alta) — Usar como modelo para criar skills próprias do time (padrões de código, revisão, deploy); **Arquitetura de software** (média) — Documentar decisões e padrões de arquitetura como skills reutilizáveis pelo agente

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · ⭐ 200,4 mil · JavaScript · MIT

- **O que é:** Faz o agente de IA pensar como o dev sênior mais preguiçoso da sala: o melhor código é o que você não escreveu.
- **Por que importa:** Skill que empurra o agente a escrever menos código e preferir soluções simples; combate excesso de complexidade gerada por IA.
- **Áreas:** **Engenharia e produtividade** (alta) — Evitar que o agente crie abstrações e código desnecessários; **Arquitetura de software** (média) — Manter a arquitetura enxuta em projetos feitos com IA

**[f/prompts.chat](https://github.com/f/prompts.chat)** · ⭐ 178,7 mil · MDX · outra

- **O que é:** Antigo Awesome ChatGPT Prompts: compartilhe, descubra e organize prompts da comunidade; pode ser auto-hospedado.
- **Por que importa:** Coleção comunitária de prompts (antigo Awesome ChatGPT Prompts), auto-hospedável para o time.
- **Áreas:** **Engenharia e produtividade** (média) — Montar uma biblioteca interna de prompts reutilizáveis

**[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · ⭐ 170,7 mil · Shell · MIT

- **O que é:** Agência de IA completa: agentes especializados (frontend, comunidade, revisão etc.) com personalidade, processos e entregas definidos.
- **Por que importa:** Coleção de agentes especializados (frontend, backend, QA, produto etc.) com personalidade e processos definidos; pronto para montar um 'time' de IA.
- **Áreas:** **Engenharia e produtividade** (média) — Usar papéis prontos (revisor, QA, arquiteto) como subagentes; **Testes e QA** (média) — Ter um agente revisor/testador dedicado para cada entrega

**[github/spec-kit](https://github.com/github/spec-kit)** · ⭐ 152,4 mil · Python · MIT

- **O que é:** Kit para começar com desenvolvimento guiado por especificação (SDD) ou outro processo.
- **Por que importa:** Kit do GitHub para desenvolvimento guiado por especificação: você escreve a spec, o agente planeja e implementa; reduz ambiguidade nas entregas com IA.
- **Áreas:** **Arquitetura de software** (alta) — Transformar requisitos em especificação e plano técnico antes do código; **Engenharia e produtividade** (alta) — Padronizar como o time pede features aos agentes

**[garrytan/gstack](https://github.com/garrytan/gstack)** · ⭐ 142,8 mil · TypeScript · MIT

- **O que é:** Configuração do Claude Code usada por Garry Tan: 23 ferramentas que atuam como CEO, designer, gerente de engenharia, release, documentação e QA.
- **Por que importa:** Configuração opinativa do Claude Code com ferramentas que fazem papel de designer, gerente de engenharia, QA e release; mostra como cobrir o ciclo todo com agentes.
- **Áreas:** **Engenharia e produtividade** (média) — Inspirar um fluxo completo de entrega com papéis definidos para o agente; **Testes e QA** (média) — Adicionar uma etapa automática de QA antes do release

**[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)** · ⭐ 120,9 mil · JavaScript · MIT

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

**[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · ⭐ 62,8 mil · Python · MIT

- **O que é:** Skill que impede o agente de código de esconder a resposta: saídas diretas e fáceis de ler.
- **Por que importa:** Skill que obriga o agente a responder de forma direta, com a resposta primeiro; reduz tempo de leitura e retrabalho.
- **Áreas:** **Engenharia e produtividade** (média) — Deixar as respostas do agente mais objetivas no dia a dia

**[emilkowalski/skills](https://github.com/emilkowalski/skills)** · ⭐ 60,7 mil · Markdown · MIT

- **O que é:** Skills para designers e engenheiros.
- **Por que importa:** Skills para designers e engenheiros, de um autor conhecido por componentes de UI bem acabados; melhora a qualidade visual do que o agente gera.
- **Áreas:** **Design e UI/UX** (alta) — Ensinar o agente a seguir detalhes de interação e acabamento visual; **Frontend** (alta) — Gerar componentes com animações e microinterações de qualidade

**[bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)** · ⭐ 55,9 mil · Python · outra

- **O que é:** Método BMAD: desenvolvimento ágil guiado por agentes de IA.
- **Por que importa:** Método ágil guiado por agentes de IA, com papéis (analista, PM, arquiteto, dev, QA) e artefatos definidos; estrutura projetos inteiros feitos com IA.
- **Áreas:** **Arquitetura de software** (alta) — Gerar PRD e documento de arquitetura antes de o agente codar; **Engenharia e produtividade** (alta) — Organizar o desenvolvimento com IA em fases e papéis claros; **Testes e QA** (média) — Incluir o papel de QA no fluxo dos agentes

**[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** · ⭐ 50,5 mil · Python · MIT

- **O que é:** Mais de 3.000 skills reutilizáveis para agentes de IA, com catálogo local, CLI, MCP e plugins.
- **Por que importa:** Milhares de skills reutilizáveis com catálogo local, CLI e MCP; útil para encontrar e instalar skills por tarefa.
- **Áreas:** **Engenharia e produtividade** (média) — Buscar e instalar skills prontas por tipo de tarefa
- ⚠️ Qualidade varia entre as skills; revise antes de usar.

**[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)** · ⭐ 48,5 mil · Python · Apache-2.0

- **O que é:** Diretório oficial, mantido pela Anthropic, de plugins de alta qualidade para o Claude Code.
- **Por que importa:** Fonte confiável de plugins (skills, comandos, agentes e MCP) para estender o Claude Code sem depender de repositórios de terceiros sem curadoria.
- **Áreas:** **Engenharia e produtividade** (alta) — Instalar plugins oficiais para revisão, testes e integrações no Claude Code

**[danielmiessler/Fabric](https://github.com/danielmiessler/Fabric)** · ⭐ 44,8 mil · Go · MIT

- **O que é:** Framework open source com uma coleção colaborativa de prompts prontos (os padrões) para resolver tarefas específicas com IA pela linha de comando.
- **Por que importa:** Reaproveita prompts testados pela comunidade para resumir, extrair e analisar conteúdo, e se encaixa bem em scripts e pipes do terminal.
- **Áreas:** **Engenharia e produtividade** (média) — Encadear padrões prontos em scripts de terminal para resumir documentos, logs ou discussões técnicas

**[wshobson/agents](https://github.com/wshobson/agents)** · ⭐ 43 mil · Python · MIT

- **O que é:** Coleção de plugins, agentes, skills e comandos para Claude Code, Codex CLI, Cursor, OpenCode, Copilot e outros, escritos uma vez em Markdown e adaptados a cada ferramenta.
- **Por que importa:** Dá ao time agentes especialistas prontos (backend, segurança, testes, infraestrutura) e mantém a mesma configuração funcionando em vários agentes de código.
- **Áreas:** **Engenharia e produtividade** (alta) — Instalar agentes especialistas prontos e padronizá-los entre Claude Code, Codex e Cursor; **Arquitetura de software** (média) — Usar os agentes de arquitetura para revisar desenhos e decisões técnicas; **Testes e QA** (média) — Acionar os agentes de testes para gerar e revisar testes automatizados

**[linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer)** · ⭐ 42,7 mil · TypeScript · outra

- **O que é:** Ferramenta para escrever e otimizar prompts de IA, comparando o resultado antes e depois da otimização.
- **Por que importa:** Ajuda a melhorar prompts de sistema e de produto de forma iterativa, testando versões lado a lado antes de colocá-las em produção.
- **Áreas:** **Engenharia e produtividade** (média) — Refinar prompts de sistema de agentes e de funcionalidades com IA antes de publicar
- ⚠️ Licença não padrão; confira os termos antes de uso comercial.

**[github/awesome-copilot](https://github.com/github/awesome-copilot)** · ⭐ 41,6 mil · JavaScript · MIT

- **O que é:** Coleção comunitária de instruções, agentes, skills e configurações para tirar mais proveito do GitHub Copilot.
- **Por que importa:** Atalho para configurar o Copilot com instruções e agentes por linguagem e framework, mantido sob a organização do GitHub.
- **Áreas:** **Engenharia e produtividade** (alta) — Copiar instruções e agentes personalizados para o repositório e padronizar o Copilot no time
- ⚠️ Conteúdo da comunidade; a qualidade varia entre os itens.

**[vercel-labs/skills](https://github.com/vercel-labs/skills)** · ⭐ 41,2 mil · TypeScript · MIT

- **O que é:** Ferramenta de linha de comando da Vercel (npx skills) para instalar e gerenciar skills abertas de agentes.
- **Por que importa:** Simplifica adicionar e atualizar skills em vários agentes de código com um comando, em vez de copiar pastas manualmente.
- **Áreas:** **Engenharia e produtividade** (alta) — Instalar e atualizar as skills do time nos agentes de código com um único comando
- ⚠️ Projeto recente.

**[PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)** · ⭐ 41,2 mil · JavaScript · CC0-1.0

- **O que é:** Coleção de arquivos de regras (.cursorrules) para personalizar o comportamento da IA do editor Cursor por linguagem e framework.
- **Por que importa:** Ponto de partida para escrever regras de projeto que guiam a IA nas convenções da sua stack.
- **Áreas:** **Engenharia e produtividade** (média) — Adaptar uma regra pronta da sua stack como base das instruções do projeto
- ⚠️ Coleção da comunidade com qualidade variável; o formato .cursorrules foi substituído pelas regras em .cursor/rules.

**[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · ⭐ 41,1 mil · TypeScript · MIT

- **O que é:** Camada de orquestração multiagente para o Claude Code, pensada para times, com agentes especializados trabalhando em paralelo.
- **Por que importa:** Divide tarefas grandes entre vários agentes do Claude Code ao mesmo tempo, acelerando entregas que hoje ficam presas numa única sessão.
- **Áreas:** **Engenharia e produtividade** (alta) — Paralelizar implementação, revisão e testes entre agentes especializados no Claude Code
- ⚠️ Projeto recente; teste antes de padronizar no time.

**[virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill)** · ⭐ 39,2 mil · Python · MIT

- **O que é:** Transforma o PDF de um livro técnico em uma skill do Claude Code para estudar, consultar e aplicar o conteúdo durante o trabalho.
- **Por que importa:** Leva o conhecimento dos livros de referência da equipe para dentro do agente, que passa a consultar e aplicar as práticas na hora de programar.
- **Áreas:** **Engenharia e produtividade** (média) — Converter um livro de referência que o time já usa em skill para o agente consultar; **Arquitetura de software** (média) — Transformar livros de arquitetura em skills que o agente usa ao revisar decisões
- ⚠️ Projeto muito recente com crescimento rápido; respeite os direitos autorais dos livros convertidos.

**[vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)** · ⭐ 35,1 mil · JavaScript

- **O que é:** Coleção oficial de skills para agentes da Vercel.
- **Por que importa:** Traz boas práticas da Vercel, como as de React e Next.js, empacotadas para o agente seguir ao escrever código.
- **Áreas:** **Frontend** (alta) — Instalar as skills para o agente seguir boas práticas de React e Next.js
- ⚠️ Sem licença declarada no GitHub.

**[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** · ⭐ 34,3 mil · Python · MIT

- **O que é:** Registro e CLI open source de componentes para o Claude Code: agentes, comandos, skills, hooks, MCPs e configurações.
- **Por que importa:** Instala com um comando componentes prontos para o Claude Code, economizando tempo de configuração.
- **Áreas:** **Engenharia e produtividade** (alta) — Instalar agentes, comandos e hooks prontos no projeto com um comando
- ⚠️ Componentes da comunidade; revise antes de instalar.

**[Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex)** · ⭐ 33,9 mil · TypeScript · MIT

- **O que é:** Complemento para o Codex CLI que adiciona hooks, times de agentes, HUDs e outros recursos.
- **Por que importa:** Estende o Codex com orquestração e automações que ele não traz nativamente.
- **Áreas:** **Engenharia e produtividade** (média) — Adicionar hooks e times de agentes ao fluxo de trabalho com o Codex
- ⚠️ Projeto recente; teste antes de padronizar no time.

**[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)** · ⭐ 30,6 mil · Python · MIT

- **O que é:** Mais de 400 skills, agentes e plugins para o Claude Code.

**[NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)** · ⭐ 28 mil · Python · Apache-2.0

- **O que é:** SkillSpector (NVIDIA): scanner de segurança para skills de agentes, detecta vulnerabilidades, injeção de prompt e vazamento de dados.

**[promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)** · ⭐ 27,8 mil · TypeScript · MIT

- **O que é:** Promptfoo: testa prompts, agentes e RAG, com red teaming e varredura de vulnerabilidades de IA.

**[agentskills/agentskills](https://github.com/agentskills/agentskills)** · ⭐ 27,7 mil · Python · Apache-2.0

- **O que é:** Especificação e documentação do padrão aberto Agent Skills.

**[humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents)** · ⭐ 27,5 mil · TypeScript · outra

- **O que é:** 12-Factor Agents: princípios para construir software com LLM bom o bastante para produção.

**[elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter)** · ⭐ 26,5 mil · Python · MIT

- **O que é:** Pacote de skills do Claude Code para caça a bugs e red team externo.

**[google/skills](https://github.com/google/skills)** · ⭐ 24,9 mil · Python · Apache-2.0

- **O que é:** Skills oficiais para agentes sobre produtos e tecnologias do Google.

**[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** · ⭐ 23,5 mil · Python · Apache-2.0

- **O que é:** Plugin open source do Google para projetar e revisar software com agentes.

**[heydamir/unslop](https://github.com/heydamir/unslop)** · ⭐ 22,8 mil · JavaScript · CC-BY-4.0

- **O que é:** Skill do Claude que transforma interfaces com cara de "vibe coding" em interfaces bem desenhadas.

**[cursor/plugins](https://github.com/cursor/plugins)** · ⭐ 20,1 mil · TypeScript

- **O que é:** Especificação do formato de plugins do Cursor e a coleção de plugins oficiais do editor.
- **Por que importa:** Mostra como empacotar e distribuir extensões de IA para o Cursor; útil para padronizar as configurações do time ou publicar um plugin próprio.
- **Áreas:** **Engenharia e produtividade** (média) — Usar os plugins oficiais como modelo para empacotar as configurações de IA do time no Cursor
- ⚠️ Sem licença declarada no GitHub; confira os termos antes de reutilizar o código.

**[wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)** · ⭐ 20 mil · Python · MIT

- **O que é:** Conjunto de skills em Markdown para pesquisa autônoma em ML: geração de ideias, automação de experimentos e ciclos de revisão entre modelos diferentes.
- **Por que importa:** Mostra como orquestrar Claude Code, Codex e outros agentes só com Markdown, sem framework; o padrão de revisão cruzada entre modelos pode ser reaproveitado em fluxos de engenharia.
- **Áreas:** **Engenharia e produtividade** (média) — Adaptar o ciclo de revisão entre modelos para que um agente revise o trabalho do outro antes do merge
- ⚠️ Projeto recente e voltado a pesquisa em ML; adapte antes de usar em entregas de software.


## Frameworks de agentes e orquestração

**[openclaw/openclaw](https://github.com/openclaw/openclaw)** · ⭐ 395,4 mil · TypeScript · MIT

- **O que é:** Assistente pessoal de IA que roda na sua própria máquina e executa tarefas de verdade (mensagens, arquivos, automações), conversando por apps como WhatsApp e Telegram.
- **Por que importa:** Plataforma de agente pessoal auto-hospedado que executa tarefas reais e conversa por WhatsApp/Telegram; referência para automações com agentes.
- **Áreas:** **Backend e APIs** (média) — Base para um assistente que integra mensagens e sistemas internos; **Segurança e cibersegurança** (média) — Exige revisão de permissões: o agente tem acesso amplo à máquina
- ⚠️ Projeto recente e de evolução rápida; revise a segurança antes de usar com dados de clientes.

**[deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)** · ⭐ 288,2 mil · TypeScript · MIT

- **O que é:** DeepSeek Harness: ambiente para agentes de IA em que tudo é plugin.
- **Por que importa:** Ambiente de agente da DeepSeek baseado em plugins; alternativa aberta para rodar agentes com modelos DeepSeek.
- **Áreas:** **Engenharia e produtividade** (média) — Rodar agentes de código com modelos DeepSeek e plugins próprios
- ⚠️ Projeto muito recente.

**[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · ⭐ 266,6 mil · Python · MIT

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

**[earendil-works/pi](https://github.com/earendil-works/pi)** · ⭐ 124,4 mil · TypeScript · MIT

- **O que é:** Kit para agentes de IA: API unificada de LLMs, loop de agente, interface de terminal e agente de código.
- **Por que importa:** Kit para construir agentes: API unificada de LLMs, loop de agente e CLI de código; base enxuta para criar seu próprio agente.
- **Áreas:** **Backend e APIs** (média) — Criar um agente próprio com loop e ferramentas sob controle; **Engenharia e produtividade** (média) — Montar um agente de código customizado para o time

**[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · ⭐ 85,9 mil · Python · MIT

- **O que é:** Ambiente open source de superagente para tarefas longas de pesquisa, código e criação, com sandboxes, memória, ferramentas e subagentes.
- **Por que importa:** Superagente para tarefas longas de pesquisa e código com sandbox, memória e subagentes; referência de arquitetura de agentes complexos.
- **Áreas:** **Arquitetura de software** (média) — Estudar arquitetura de agentes com sandbox, memória e subagentes; **Backend e APIs** (média) — Montar fluxos de pesquisa e geração de relatórios automatizados

**[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · ⭐ 82,6 mil · TypeScript · MIT

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

**[zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)** · ⭐ 48,1 mil · Python · MIT

- **O que é:** Assistente pessoal de IA e harness de agentes que planeja tarefas, usa ferramentas e skills e evolui com memória, com vários modelos e canais de mensagem.
- **Por que importa:** Base leve para colocar um agente com ferramentas, memória e vários modelos em canais de mensagem, sem montar a infraestrutura do zero.
- **Áreas:** **Backend e APIs** (média) — Integrar um agente com skills e MCP aos canais de mensagem usados pela equipe ou por clientes
- ⚠️ Muito voltado a canais chineses, como WeChat e Feishu.

**[AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot)** · ⭐ 47,7 mil · Python · AGPL-3.0

- **O que é:** Framework de assistente e agente de IA que integra várias plataformas de mensagem (QQ, Telegram, Discord), LLMs, plugins e MCP.
- **Por que importa:** Atalho para criar bots com LLM, ferramentas e plugins em vários canais de chat sem escrever a integração de cada plataforma.
- **Áreas:** **Backend e APIs** (média) — Publicar um agente com ferramentas MCP em canais como Telegram e Discord
- ⚠️ Licença AGPL: verifique antes de uso comercial fechado.

**[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · ⭐ 45,5 mil · Python · MIT

- **O que é:** Framework da LangChain para construir agentes resilientes como grafos de estado, com persistência, retomada e intervenção humana.
- **Por que importa:** Indicado quando o agente precisa de fluxos controlados, checkpoints e aprovação humana, em vez de um loop livre difícil de depurar.
- **Áreas:** **Arquitetura de software** (alta) — Modelar fluxos de agentes como grafos com estado e pontos de aprovação; **Backend e APIs** (alta) — Rodar agentes de longa duração com persistência dentro de serviços Python

**[agno-agi/agno](https://github.com/agno-agi/agno)** · ⭐ 43,3 mil · Python · Apache-2.0

- **O que é:** Plataforma e framework Python para construir, rodar e gerenciar agentes de IA com memória, conhecimento e ferramentas.
- **Por que importa:** Framework enxuto e rápido para colocar agentes e times de agentes em produção, com runtime e interface de gestão inclusos.
- **Áreas:** **Backend e APIs** (alta) — Criar serviços de agentes em Python com ferramentas, memória e base de conhecimento; **Arquitetura de software** (média) — Estruturar times de agentes com papéis definidos

**[tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)** · ⭐ 42,9 mil · Rust · GPL-3.0

- **O que é:** Harness de agentes open source em Rust, local-first, que promete rodar centenas de agentes em um servidor barato, com MCP e app desktop.
- **Por que importa:** Alternativa leve para rodar muitos agentes com pouco recurso e privacidade local, se as promessas de eficiência se confirmarem no seu caso.
- **Áreas:** **DevOps e infraestrutura** (média) — Rodar vários agentes de automação em um VPS pequeno
- ⚠️ Projeto recente; valide as promessas de desempenho. Licença GPL-3.0.

**[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)** · ⭐ 39,3 mil · Python · MIT

- **O que é:** Framework de Stanford para programar, e não apenas escrever prompts, para modelos de linguagem, com módulos declarativos e otimizadores que ajustam prompts e exemplos automaticamente.
- **Por que importa:** Troca prompts frágeis escritos à mão por programas avaliados com métricas, o que torna pipelines de LLM e agentes mais fáceis de melhorar, testar e trocar de modelo.
- **Áreas:** **Backend e APIs** (alta) — Estruturar pipelines de LLM como módulos Python com assinaturas de entrada e saída; **Testes e QA** (média) — Definir métricas e conjuntos de avaliação para otimizar e comparar versões do pipeline

**[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)** · ⭐ 36,8 mil · Python · Apache-2.0

- **O que é:** Framework do Alibaba para construir e rodar agentes e sistemas multiagente observáveis e confiáveis, com MCP, voz e tempo real.
- **Por que importa:** Foca em transparência e controle: dá para acompanhar e depurar o que cada agente faz, o que ajuda a levar sistemas multiagente para produção.
- **Áreas:** **Backend e APIs** (média) — Construir serviços multiagente em Python com ferramentas MCP; **Arquitetura de software** (média) — Desenhar fluxos multiagente com papéis e comunicação explícitos

**[OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev)** · ⭐ 34,9 mil · Python · Apache-2.0

- **O que é:** Plataforma em que vários agentes com LLM colaboram para desenvolver software (ChatDev 2.0).
- **Por que importa:** Mostra como dividir o ciclo de desenvolvimento entre agentes com papéis (produto, código, testes), útil para estudar e prototipar fluxos multiagente.
- **Áreas:** **Arquitetura de software** (média) — Estudar como distribuir papéis de desenvolvimento entre agentes
- ⚠️ Mais indicado para pesquisa e experimentação do que para produção.

**[topoteretes/cognee](https://github.com/topoteretes/cognee)** · ⭐ 33,7 mil · Python · Apache-2.0

- **O que é:** Cognee: plataforma open source de memória de longo prazo para agentes de IA.

**[meta/astryx](https://github.com/meta/astryx)** · ⭐ 33,6 mil · TypeScript · MIT

- **O que é:** Astryx: design system open source da Meta, personalizável e pronto para agentes.

**[trycua/cua](https://github.com/trycua/cua)** · ⭐ 33,2 mil · Rust · MIT

- **O que é:** Infraestrutura open source para agentes que usam o computador: drivers, sandboxes e benchmarks.

**[getzep/graphiti](https://github.com/getzep/graphiti)** · ⭐ 33,2 mil · Python · Apache-2.0

- **O que é:** Graphiti: grafos de conhecimento em tempo real para agentes de IA.

**[langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)** · ⭐ 31,6 mil · Python · MIT

- **O que é:** Deep Agents: harness de agentes "com tudo incluído" da LangChain.

**[ComposioHQ/composio](https://github.com/ComposioHQ/composio)** · ⭐ 31,3 mil · TypeScript · MIT

- **O que é:** Composio: mais de 1.000 integrações, busca de ferramentas, autenticação e sandbox para agentes.

**[e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)** · ⭐ 31,1 mil · outra

- **O que é:** Lista de agentes autônomos de IA.

**[openai/openai-agents-python](https://github.com/openai/openai-agents-python)** · ⭐ 30,9 mil · Python · MIT

- **O que é:** Framework leve da OpenAI para fluxos multiagente.

**[huggingface/smolagents](https://github.com/huggingface/smolagents)** · ⭐ 30,6 mil · Python · Apache-2.0

- **O que é:** smolagents: biblioteca enxuta da Hugging Face para agentes que pensam em código.

**[mastra-ai/mastra](https://github.com/mastra-ai/mastra)** · ⭐ 29,9 mil · TypeScript · outra

- **O que é:** Mastra: framework TypeScript para aplicações e agentes com IA.

**[chroma-core/chroma](https://github.com/chroma-core/chroma)** · ⭐ 29,8 mil · Rust · Apache-2.0

- **O que é:** Chroma: infraestrutura de busca e banco vetorial para IA.

**[alibaba/page-agent](https://github.com/alibaba/page-agent)** · ⭐ 29,8 mil · TypeScript · MIT

- **O que é:** Agente de interface em JavaScript que controla páginas web por linguagem natural.

**[google-labs-code/design.md](https://github.com/google-labs-code/design.md)** · ⭐ 29,2 mil · TypeScript · Apache-2.0

- **O que é:** DESIGN.md: especificação do Google para descrever a identidade visual de um projeto para agentes de código.

**[gastownhall/beads](https://github.com/gastownhall/beads)** · ⭐ 29,2 mil · Go · MIT

- **O que é:** Beads: memória e rastreamento de tarefas para agentes de código.

**[mlflow/mlflow](https://github.com/mlflow/mlflow)** · ⭐ 29 mil · Python · Apache-2.0

- **O que é:** MLflow: plataforma open source de engenharia de IA para agentes, LLMs e modelos de ML (rastreamento, avaliação e deploy).

**[BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)** · ⭐ 28,8 mil · Rust · Apache-2.0

- **O que é:** Quadro kanban para orquestrar Claude Code, Codex e outros agentes de código.

**[openai/symphony](https://github.com/openai/symphony)** · ⭐ 28,2 mil · Elixir · Apache-2.0

- **O que é:** Symphony (OpenAI): transforma trabalho de projeto em execuções autônomas e isoladas de implementação.

**[xai-org/grok-build](https://github.com/xai-org/grok-build)** · ⭐ 27,9 mil · Rust · Apache-2.0

- **O que é:** Harness e interface de terminal do agente de código da xAI.

**[GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance)** · ⭐ 27,2 mil · Apache-2.0

- **O que é:** Mantém o agente de código atualizado com as boas práticas mais recentes da web (Google Chrome).

**[deepset-ai/haystack](https://github.com/deepset-ai/haystack)** · ⭐ 27,1 mil · Python · Apache-2.0

- **O que é:** Haystack: framework de orquestração de IA para apps com LLM prontos para produção.

**[a2aproject/A2A](https://github.com/a2aproject/A2A)** · ⭐ 26,7 mil · Shell · Apache-2.0

- **O que é:** A2A: protocolo aberto para comunicação e interoperabilidade entre agentes.

**[walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering)** · ⭐ 26,2 mil · TypeScript · MIT

- **O que é:** Tutorial de engenharia de harness para agentes, do zero.

**[browserbase/stagehand](https://github.com/browserbase/stagehand)** · ⭐ 26,2 mil · TypeScript · MIT

- **O que é:** Stagehand: SDK para extrair dados e interagir com qualquer site usando IA.

**[agentsmd/agents.md](https://github.com/agentsmd/agents.md)** · ⭐ 25,7 mil · TypeScript · MIT

- **O que é:** AGENTS.md: formato aberto e simples para orientar agentes de código.

**[microsoft/OmniParser](https://github.com/microsoft/OmniParser)** · ⭐ 25,6 mil · Jupyter Notebook · CC-BY-4.0

- **O que é:** OmniParser (Microsoft): analisa telas para agentes de interface baseados em visão.

**[letta-ai/letta](https://github.com/letta-ai/letta)** · ⭐ 25,6 mil · Apache-2.0

- **O que é:** Letta: plataforma de agentes com estado e memória avançada.

**[NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents)** · ⭐ 25,2 mil · Jupyter Notebook · outra

- **O que é:** Mais de 50 tutoriais e implementações de técnicas de agentes de IA generativa.

**[1Panel-dev/MaxKB](https://github.com/1Panel-dev/MaxKB)** · ⭐ 23,2 mil · Python · GPL-3.0

- **O que é:** MaxKB: plataforma open source para construir agentes empresariais.

**[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · ⭐ 23,1 mil · TypeScript · Apache-2.0

- **O que é:** Roda agentes como OpenClaw, Hermes e LangChain Deep Agents com mais segurança dentro do NVIDIA OpenShell.

**[PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent)** · ⭐ 22,9 mil · Rust · outra

- **O que é:** Agente de código que se aprimora sozinho, para fluxos de programação e tarefas longas.

**[google/adk-python](https://github.com/google/adk-python)** · ⭐ 22,4 mil · Python · Apache-2.0

- **O que é:** ADK: kit open source do Google para construir, avaliar e publicar agentes de IA.

**[snarktank/ralph](https://github.com/snarktank/ralph)** · ⭐ 22,4 mil · TypeScript · MIT

- **O que é:** Ralph: loop de agente autônomo que roda até concluir todos os itens do PRD.

**[ai-openshell/openshell](https://github.com/ai-openshell/openshell)** · ⭐ 22 mil · Rust · Apache-2.0

- **O que é:** OpenShell: runtime seguro e privado para agentes de IA autônomos.

**[ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui)** · ⭐ 22 mil · TypeScript · MIT

- **O que é:** AG-UI: protocolo de interação entre agentes e usuários para levar agentes ao frontend.

**[NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production)** · ⭐ 22 mil · Jupyter Notebook · outra

- **O que é:** Tutoriais com código para levar agentes de IA do protótipo à produção.

**[pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)** · ⭐ 21,4 mil · Python · MIT

- **O que é:** Pydantic AI: framework Python tipado para agentes e apps com IA.

**[cube-js/cube](https://github.com/cube-js/cube)** · ⭐ 21,3 mil · Rust · outra

- **O que é:** Cube: camada semântica open source para IA, BI e analytics embarcado.

**[camel-ai/owl](https://github.com/camel-ai/owl)** · ⭐ 20,2 mil · Python

- **O que é:** OWL: agentes colaborativos para automação de tarefas do mundo real.

**[agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)** · ⭐ 20 mil · Python · outra

- **O que é:** Agent Zero: framework de agentes de IA.


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

**[supabase/supabase](https://github.com/supabase/supabase)** · ⭐ 115,5 mil · TypeScript · Apache-2.0

- **O que é:** Supabase: plataforma de desenvolvimento sobre Postgres para apps web, mobile e de IA.
- **Por que importa:** Plataforma sobre Postgres com autenticação, storage, APIs automáticas e vetores (pgvector); backend completo pronto para apps com IA.
- **Áreas:** **Banco de dados e dados** (alta) — Usar Postgres gerenciado com pgvector para busca semântica; **Backend e APIs** (alta) — Ganhar autenticação, storage e APIs sem escrever um backend do zero; **Segurança e cibersegurança** (média) — Controlar acesso aos dados com políticas por linha (RLS)

**[Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)** · ⭐ 68,7 mil · JavaScript · MIT

- **O que é:** AnythingLLM: plataforma local para agentes e chat com seus documentos.
- **Por que importa:** App local para conversar com documentos e rodar agentes, com controle total dos dados.
- **Áreas:** **Backend e APIs** (média) — Montar uma base de conhecimento interna consultável por IA; **Banco de dados e dados** (média) — Indexar documentos e manuais para busca em linguagem natural

**[appwrite/appwrite](https://github.com/appwrite/appwrite)** · ⭐ 58,6 mil · TypeScript · BSD-3-Clause

- **O que é:** Appwrite: nuvem open source com autenticação, bancos de dados, storage, funções, mensagens e hospedagem.
- **Por que importa:** Nuvem open source com autenticação, bancos, storage, funções e mensagens, voltada também a agentes.
- **Áreas:** **Backend e APIs** (alta) — Ter backend pronto (auth, banco, storage, funções) auto-hospedado; **Banco de dados e dados** (média) — Gerenciar coleções de dados com permissões prontas

**[jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** · ⭐ 48,7 mil · Java · Apache-2.0

- **O que é:** Plataforma low-code com IA em Java (Spring Boot e Vue) para sistemas corporativos, com permissões, multi-tenant, fluxos BPM, relatórios e geração de código por IA.
- **Por que importa:** Entrega pronta a base comum de sistemas de gestão e usa IA para gerar tabelas, telas, menus e fluxos, deixando o time focado só na regra de negócio.
- **Áreas:** **Backend e APIs** (alta) — Gerar CRUDs, APIs e telas de um sistema interno a partir de uma descrição; **Frontend** (média) — Aproveitar os formulários, relatórios e painéis gerados como base do frontend
- ⚠️ Documentação e comunidade principalmente em chinês.

**[LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat)** · ⭐ 47,6 mil · TypeScript · MIT

- **O que é:** Interface de chat self-hosted no estilo ChatGPT com agentes, MCP, skills, artefatos, interpretador de código e suporte a muitos provedores de modelos.
- **Por que importa:** Dá à empresa um chat interno com vários modelos, autenticação multiusuário e controle dos dados, sem depender de uma assinatura por pessoa.
- **Áreas:** **DevOps e infraestrutura** (média) — Hospedar um portal de IA interno com login corporativo e vários provedores; **Engenharia e produtividade** (média) — Oferecer ao time agentes com MCP e interpretador de código num só lugar

**[ToolJet/ToolJet](https://github.com/ToolJet/ToolJet)** · ⭐ 41,3 mil · HTML · AGPL-3.0

- **O que é:** Plataforma low-code open source para criar ferramentas internas, dashboards, apps de negócio, fluxos e agentes de IA, visualmente, por prompt ou via MCP a partir do Claude Code, Codex e Cursor.
- **Por que importa:** Acelera a entrega de apps internos conectados a bancos e APIs, sem montar frontend e backend do zero.
- **Áreas:** **Frontend** (média) — Gerar telas de ferramentas internas a partir de um prompt ou montá-las visualmente; **Banco de dados e dados** (média) — Conectar painéis e formulários direto a bancos e APIs existentes
- ⚠️ Licença AGPL; parte dos recursos de IA fica na versão comercial (ToolJet AI).

**[PostHog/posthog](https://github.com/PostHog/posthog)** · ⭐ 41,2 mil · Python · outra

- **O que é:** Plataforma de produto com analytics, replay de sessões, feature flags, experimentos, rastreio de erros, logs e observabilidade de IA, controlável por MCP.
- **Por que importa:** Reúne num lugar o contexto que times e agentes precisam para diagnosticar problemas e validar entregas, incluindo custo e qualidade das chamadas a LLMs.
- **Áreas:** **DevOps e infraestrutura** (média) — Monitorar erros, logs e chamadas a LLMs em produção; **Testes e QA** (média) — Liberar funcionalidades com feature flags e medir o efeito com experimentos A/B
- ⚠️ Licença mista (parte do código é enterprise); confira os termos.

**[langfuse/langfuse](https://github.com/langfuse/langfuse)** · ⭐ 37,9 mil · TypeScript · outra

- **O que é:** Plataforma open source de engenharia de IA com gateway, observabilidade de agentes, avaliações e gestão de prompts e skills, baseada em OpenTelemetry.
- **Por que importa:** Mostra o que cada chamada e cada agente fez, quanto custou e como se saiu nas avaliações, essencial para depurar e melhorar apps com LLM.
- **Áreas:** **DevOps e infraestrutura** (alta) — Rastrear chamadas a LLMs e agentes em produção com custo e latência; **Testes e QA** (alta) — Rodar avaliações e comparar versões de prompts antes de publicar
- ⚠️ Licença mista (parte do código é enterprise); confira os termos.

**[conductor-oss/conductor](https://github.com/conductor-oss/conductor)** · ⭐ 32,5 mil · Java · Apache-2.0

- **O que é:** Conductor: motor de workflows orientado a eventos, com execução durável para aplicações e agentes.

**[simstudioai/sim](https://github.com/simstudioai/sim)** · ⭐ 30,2 mil · TypeScript · Apache-2.0

- **O que é:** Sim: workspace colaborativo para criar, publicar e monitorar agentes e fluxos de IA.

**[Budibase/budibase](https://github.com/Budibase/budibase)** · ⭐ 28,5 mil · TypeScript · outra

- **O que é:** Budibase: agentes, automações e apps internos com IA, independente do modelo.

**[activepieces/activepieces](https://github.com/activepieces/activepieces)** · ⭐ 25,8 mil · TypeScript · outra

- **O que é:** Activepieces: automação de fluxos com IA e agentes, com cerca de 400 servidores MCP.

**[coleam00/Archon](https://github.com/coleam00/Archon)** · ⭐ 24 mil · TypeScript · MIT

- **O que é:** Archon: construtor de harness para programação com IA, deixando o resultado determinístico e repetível.

**[Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern)** · ⭐ 23,6 mil · Python · AGPL-3.0

- **O que é:** Skyvern: automatiza fluxos no navegador com IA.

**[airbytehq/airbyte](https://github.com/airbytehq/airbyte)** · ⭐ 22,5 mil · Python · outra

- **O que é:** Airbyte: movimentação de dados open source (ELT) de APIs, bancos e arquivos para warehouses e aplicações de IA.

**[coze-dev/coze-studio](https://github.com/coze-dev/coze-studio)** · ⭐ 21,8 mil · TypeScript · Apache-2.0

- **O que é:** Coze Studio: plataforma de desenvolvimento de agentes com ferramentas visuais completas.

**[RasaHQ/rasa](https://github.com/RasaHQ/rasa)** · ⭐ 21,4 mil · Python · Apache-2.0

- **O que é:** Rasa: framework open source para automatizar conversas por texto e voz.

**[vercel/chatbot](https://github.com/vercel/chatbot)** · ⭐ 21,1 mil · TypeScript · outra

- **O que é:** Chatbot de IA completo e customizável em Next.js, da Vercel.


## MCP, ferramentas e integrações

**[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** · ⭐ 211,9 mil · TypeScript · AGPL-3.0

- **O que é:** Infraestrutura de dados para agentes de IA: busca, raspagem e acesso a mais de 550 fontes de dados por uma única API.
- **Por que importa:** Transforma sites em dados limpos (Markdown/JSON) para agentes e RAG, com busca e raspagem por uma API.
- **Áreas:** **Backend e APIs** (alta) — Alimentar um sistema de IA com conteúdo de sites de forma estruturada; **Banco de dados e dados** (média) — Coletar e normalizar dados da web para análises

**[browser-use/browser-use](https://github.com/browser-use/browser-use)** · ⭐ 122,3 mil · Python · MIT

- **O que é:** Biblioteca Python open source para agentes de IA que navegam na web, com serviço de nuvem opcional.
- **Por que importa:** Biblioteca Python para agentes que navegam e interagem com sites; base para automações e testes guiados por IA.
- **Áreas:** **Testes e QA** (alta) — Criar testes exploratórios em que o agente percorre a aplicação; **Backend e APIs** (média) — Automatizar tarefas em sistemas web sem API

**[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · ⭐ 92,3 mil · TypeScript · outra

- **O que é:** Servidores de referência do Model Context Protocol (MCP).
- **Por que importa:** Servidores de referência do MCP (Git, sistema de arquivos, busca, bancos etc.); ponto de partida para conectar agentes às suas ferramentas.
- **Áreas:** **Backend e APIs** (alta) — Usar como modelo para criar um servidor MCP que expõe a API do seu sistema ao agente; **Banco de dados e dados** (média) — Dar ao agente acesso controlado a um banco de dados via MCP; **DevOps e infraestrutura** (média) — Integrar agentes a ferramentas internas de forma padronizada

**[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** · ⭐ 88,1 mil · Python · Apache-2.0

- **O que é:** Crawler open source para coletar, extrair e buscar dados na web para agentes de IA, com versão em nuvem opcional.
- **Por que importa:** Crawler open source pensado para LLMs; extrai conteúdo pronto para RAG e pode ser auto-hospedado sem custo.
- **Áreas:** **Backend e APIs** (alta) — Montar coleta de conteúdo para bases de conhecimento de IA; **Banco de dados e dados** (média) — Extrair dados estruturados de páginas para alimentar o banco

**[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)** · ⭐ 67,2 mil · Python · Apache-2.0

- **O que é:** Torna qualquer software "nativo para agentes" por meio de interfaces de linha de comando.
- **Por que importa:** Cria interfaces de linha de comando para softwares existentes, para que agentes consigam operá-los.
- **Áreas:** **Backend e APIs** (média) — Expor operações de um sistema interno como CLI utilizável por agentes
- ⚠️ Projeto recente.

**[upstash/context7](https://github.com/upstash/context7)** · ⭐ 65,6 mil · TypeScript · MIT

- **O que é:** Context7: documentação sempre atualizada para agentes de IA.
- **Por que importa:** Entrega ao agente a documentação atualizada das bibliotecas; evita código baseado em APIs antigas.
- **Áreas:** **Engenharia e produtividade** (alta) — Reduzir erros do agente com versões novas de frameworks; **Frontend** (média) — Gerar código com a API atual de bibliotecas de frontend; **Backend e APIs** (média) — Usar a documentação correta de frameworks de backend

**[ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** · ⭐ 59,7 mil · TypeScript · Apache-2.0

- **O que é:** Chrome DevTools para agentes de código (servidor MCP).
- **Por que importa:** Dá ao agente de código acesso ao Chrome DevTools (console, rede, performance); o agente passa a enxergar e depurar a página de verdade.
- **Áreas:** **Frontend** (alta) — Deixar o agente depurar erros de console e rede da aplicação web; **Testes e QA** (alta) — Verificar no navegador se a tela funciona depois da mudança

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)** · ⭐ 54,4 mil · Rust · Apache-2.0

- **O que é:** CLI de automação de navegador para agentes de IA.
- **Por que importa:** CLI de automação de navegador feita para agentes de IA; leve e fácil de integrar a fluxos de teste e verificação.
- **Áreas:** **Testes e QA** (alta) — Deixar o agente navegar e validar fluxos da aplicação; **Frontend** (média) — Conferir telas no navegador durante o desenvolvimento

**[lightpanda-io/browser](https://github.com/lightpanda-io/browser)** · ⭐ 42,7 mil · Zig · AGPL-3.0

- **O que é:** Navegador headless escrito em Zig e feito para IA e automação, compatível com Playwright e Puppeteer via CDP.
- **Por que importa:** Consome bem menos memória e inicia mais rápido que um Chrome headless, o que barateia agentes que navegam na web e raspagem em escala.
- **Áreas:** **Testes e QA** (média) — Rodar automações de navegador com Playwright ou Puppeteer usando menos recursos; **DevOps e infraestrutura** (média) — Reduzir o custo de infraestrutura de agentes que navegam em muitas páginas
- ⚠️ Ainda não suporta todas as APIs da web; licença AGPL.

**[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · ⭐ 40,2 mil · TypeScript · Apache-2.0

- **O que é:** Servidor MCP oficial da Microsoft que deixa agentes de IA controlarem um navegador via Playwright, usando a árvore de acessibilidade da página.
- **Por que importa:** Dá ao agente de código olhos e mãos no navegador para testar fluxos, reproduzir bugs e conferir o frontend que ele mesmo alterou.
- **Áreas:** **Testes e QA** (alta) — Pedir ao agente que execute e verifique fluxos de ponta a ponta no navegador; **Frontend** (média) — Deixar o agente conferir a página no navegador depois de mudar o código

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)** · ⭐ 37,9 mil · Rust · Apache-2.0

- **O que é:** Navegador headless em Rust para agentes de IA e raspagem web, compatível com Playwright e Puppeteer, com recursos anti-detecção.
- **Por que importa:** Opção leve para agentes que precisam navegar e coletar dados em muitas páginas.
- ⚠️ Projeto muito recente com crescimento de estrelas fora do comum e foco em anti-detecção; avalie os riscos legais antes de usar.

**[github/github-mcp-server](https://github.com/github/github-mcp-server)** · ⭐ 34,8 mil · Go · MIT

- **O que é:** Servidor MCP oficial do GitHub para agentes lerem e operarem repositórios, issues, pull requests e Actions.
- **Por que importa:** Liga o agente ao fluxo real de entrega: abrir e revisar PRs, triar issues e investigar falhas de CI sem sair da conversa.
- **Áreas:** **Engenharia e produtividade** (alta) — Deixar o agente abrir PRs, comentar revisões e triar issues; **DevOps e infraestrutura** (média) — Investigar falhas do GitHub Actions pelo agente

**[ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai)** · ⭐ 33 mil · Python · MIT

- **O que é:** Scraper em Python baseado em IA.

**[jackwener/OpenCLI](https://github.com/jackwener/OpenCLI)** · ⭐ 31,4 mil · JavaScript · Apache-2.0

- **O que é:** Transforma sites em CLI e deixa o agente usar o seu navegador já logado.

**[PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)** · ⭐ 28,8 mil · Python · Apache-2.0

- **O que é:** FastMCP: forma rápida e pythônica de criar servidores e clientes MCP.

**[OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB)** · ⭐ 28,4 mil · Java · outra

- **O que é:** Chat2DB: cliente de banco de dados e workspace SQL com IA, local e multiplataforma.

**[vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop)** · ⭐ 27,2 mil · Rust · Apache-2.0

- **O que é:** CLI de uso do computador para agentes de IA (Vercel).

**[modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)** · ⭐ 25 mil · Python · MIT

- **O que é:** SDK oficial em Python do Model Context Protocol (MCP) para servidores e clientes.

**[czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** · ⭐ 23,3 mil · TypeScript · MIT

- **O que é:** Servidor MCP que permite a assistentes de IA operar o n8n: depurar, editar, validar e criar fluxos.

**[xerj-org/xerj](https://github.com/xerj-org/xerj)** · ⭐ 22,4 mil · Rust · Apache-2.0

- **O que é:** Motor de busca para agentes e servidor MCP que indexa código, documentação, logs e PDFs.

**[1jehuang/jcode](https://github.com/1jehuang/jcode)** · ⭐ 22,1 mil · Rust · MIT

- **O que é:** Harness de agente de código em Rust, feito para fluxos pesados com vários agentes.


## Memória, contexto e economia de tokens

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · ⭐ 123,4 mil · Go · Apache-2.0

- **O que é:** Skill e proxy local para agentes de código que encurtam respostas e saídas de ferramentas, economizando tokens.
- **Por que importa:** Skill e proxy que encurtam respostas e saídas de ferramentas dos agentes, economizando tokens sem perder informação.
- **Áreas:** **Engenharia e produtividade** (média) — Deixar o agente mais econômico e direto

**[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · ⭐ 120,3 mil · TypeScript · Apache-2.0

- **O que é:** Memória persistente entre sessões para agentes de IA: registra, comprime e reaproveita o contexto em sessões futuras.
- **Por que importa:** Memória persistente entre sessões para agentes de código: o agente lembra do que já fez no projeto.
- **Áreas:** **Engenharia e produtividade** (alta) — Evitar que o agente esqueça decisões e contexto entre sessões

**[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · ⭐ 88,1 mil · Rust · Apache-2.0

- **O que é:** Proxy de linha de comando que reduz em 60–90% o consumo de tokens de LLMs em comandos comuns de desenvolvimento.
- **Por que importa:** Proxy de linha de comando que reduz de 60% a 90% os tokens em comandos comuns de desenvolvimento.
- **Áreas:** **Engenharia e produtividade** (alta) — Economizar tokens e limite de uso dos agentes de código

**[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · ⭐ 81 mil · Python · Apache-2.0

- **O que é:** Comprime saídas de ferramentas, logs e trechos de RAG antes de enviar ao LLM, reduzindo tokens sem mudar as respostas.
- **Por que importa:** Comprime saídas de ferramentas, logs e trechos de RAG antes do LLM; reduz custo e mantém as respostas.
- **Áreas:** **Engenharia e produtividade** (alta) — Reduzir tokens gastos por agentes de código; **Backend e APIs** (média) — Baixar o custo de chamadas de IA no produto

**[mem0ai/mem0](https://github.com/mem0ai/mem0)** · ⭐ 69,6 mil · Python · Apache-2.0

- **O que é:** Camada de memória para agentes e apps de IA: contexto persistente, pronto para produção.
- **Por que importa:** Camada de memória para agentes e apps de IA: guarda preferências e contexto entre conversas, pronta para produção.
- **Áreas:** **Backend e APIs** (alta) — Dar memória de longo prazo a um assistente do produto; **Banco de dados e dados** (média) — Persistir contexto de usuários de forma organizada

**[vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)** · ⭐ 63,9 mil · Python · MIT

- **O que é:** Memória para agentes de IA que aprende com o uso.
- **Por que importa:** Memória para agentes que aprende com as interações; alternativa a soluções de memória mais simples.
- **Áreas:** **Backend e APIs** (média) — Adicionar memória que evolui a agentes do produto
- ⚠️ Projeto recente.

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · ⭐ 60,7 mil · Python · MIT

- **O que é:** Sistema de memória para IA open source e gratuito, com bons resultados em benchmarks.
- **Por que importa:** Sistema de memória para IA open source e gratuito, com bons resultados em benchmarks.
- **Áreas:** **Backend e APIs** (média) — Testar memória de longo prazo para agentes sem custo de licença
- ⚠️ Projeto recente.

**[volcengine/OpenViking](https://github.com/volcengine/OpenViking)** · ⭐ 43 mil · Python · AGPL-3.0

- **O que é:** Banco de contexto para agentes de IA, da Volcengine (ByteDance), que unifica memória, base de conhecimento para RAG e skills e evolui com o uso.
- **Por que importa:** Organiza num só lugar o que o agente precisa lembrar e consultar, evitando montar banco vetorial, memória e skills separadamente.
- **Áreas:** **Arquitetura de software** (média) — Centralizar memória e conhecimento dos agentes em uma camada única de contexto; **Banco de dados e dados** (média) — Substituir a combinação de banco vetorial e armazenamento de memória por um serviço só
- ⚠️ Projeto recente; licença AGPL.

**[mksglu/context-mode](https://github.com/mksglu/context-mode)** · ⭐ 34,6 mil · JavaScript · outra

- **O que é:** Plugin local e gratuito que tira a saída das ferramentas da janela de contexto do agente de código, guardando-a em sandbox com busca SQLite FTS5.
- **Por que importa:** Reduz muito os tokens gastos com saídas longas de comandos, deixando as sessões mais longas e baratas no Claude Code, Codex e outros.
- **Áreas:** **Engenharia e produtividade** (alta) — Instalar no agente de código para cortar o consumo de contexto com saídas de testes e logs
- ⚠️ Licença não padrão; confira os termos.

**[supermemoryai/supermemory](https://github.com/supermemoryai/supermemory)** · ⭐ 31,9 mil · TypeScript · MIT

- **O que é:** Supermemory: motor de memória e contexto para apps de IA, rápido e executável localmente.

**[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · ⭐ 31,2 mil · TypeScript · outra

- **O que é:** Central de memória para times de agentes: transforma conversas, documentos e código em memória reutilizável.

**[deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)** · ⭐ 24,2 mil · Python · MIT

- **O que é:** DeepSeek-OCR: modelo de OCR da DeepSeek que comprime o contexto visual.


## Conhecimento do código e diagramas

**[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · ⭐ 154,4 mil · Python · Apache-2.0

- **O que é:** Transforma qualquer base de código (com docs, esquemas SQL, configs e PDFs) em um grafo de conhecimento consultável; skill para Claude Code, Cursor, Codex e Gemini CLI.
- **Por que importa:** Transforma o código, docs, esquemas SQL e configs em um grafo de conhecimento consultável pelo agente; melhora respostas sobre sistemas grandes.
- **Áreas:** **Arquitetura de software** (alta) — Mapear dependências e responsabilidades de um sistema legado; **Banco de dados e dados** (média) — Relacionar esquemas SQL com o código que os usa; **Engenharia e produtividade** (média) — Reduzir o tempo do agente procurando contexto em bases grandes

**[tt-a1i/archify](https://github.com/tt-a1i/archify)** · ⭐ 101,1 mil · JavaScript · Apache-2.0

- **O que é:** Transforma ideias, planos ou código em diagramas interativos ou respostas de uma página; skill para Claude Code, Codex, Cursor e outros.
- **Por que importa:** Skill que transforma ideias, planos ou código em diagramas interativos e diagnóstico de arquitetura; ajuda a explicar e revisar sistemas.
- **Áreas:** **Arquitetura de software** (alta) — Gerar diagnóstico e diagramas da arquitetura atual de um sistema; **Engenharia e produtividade** (média) — Explicar PRs e mudanças com diagramas para revisão

**[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · ⭐ 94,8 mil · TypeScript · MIT

- **O que é:** Transforma qualquer código em um grafo de conhecimento interativo para explorar, buscar e fazer perguntas.
- **Por que importa:** Grafo de conhecimento interativo do código para explorar, buscar e perguntar; ótimo para onboarding em projetos desconhecidos.
- **Áreas:** **Arquitetura de software** (alta) — Entender a estrutura de um projeto novo antes de mexer nele; **Engenharia e produtividade** (média) — Acelerar o onboarding de devs em sistemas grandes

**[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · ⭐ 79 mil · TypeScript · MIT

- **O que é:** Grafo de conhecimento do código pré-indexado e sincronizado, para agentes gastarem menos tokens; roda 100% local.
- **Por que importa:** Grafo do código pré-indexado e sincronizado para agentes; menos tokens e menos chamadas de ferramenta, tudo local.
- **Áreas:** **Engenharia e produtividade** (alta) — Deixar o agente mais rápido e barato em repositórios grandes; **Arquitetura de software** (média) — Consultar dependências entre módulos durante refatorações

**[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** · ⭐ 74,6 mil · HTML · MIT

- **O que é:** Skill de design de diagramas editoriais para agentes de código: 52 tipos, em HTML + SVG autocontido.
- **Por que importa:** Skill que ensina o agente a gerar diagramas editoriais limpos (52 tipos) em HTML + SVG; melhor que diagramas genéricos em Mermaid.
- **Áreas:** **Arquitetura de software** (alta) — Gerar diagramas de arquitetura e fluxos com visual profissional; **Design e UI/UX** (média) — Produzir diagramas para documentação e apresentações

**[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · ⭐ 49,3 mil · C · MIT

- **O que é:** Servidor MCP local que monta um grafo persistente do código, da documentação e da infraestrutura para desenvolvedores e agentes de IA consultarem.
- **Por que importa:** Dá ao agente um mapa estruturado do repositório em vez de ler arquivo por arquivo, o que economiza tokens e ajuda a escolher só os testes afetados por uma mudança.
- **Áreas:** **Arquitetura de software** (alta) — Consultar dependências e o impacto de uma mudança pelo grafo antes de refatorar; **Engenharia e produtividade** (alta) — Conectar o grafo ao Claude Code, Codex ou Cursor para respostas mais precisas sobre o código; **Testes e QA** (média) — Selecionar só os testes afetados por uma alteração
- ⚠️ Projeto recente.

**[abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)** · ⭐ 48,9 mil · TypeScript · outra

- **O que é:** Motor de inteligência de código sem servidor que monta um grafo de conhecimento do repositório no navegador ou na linha de comando, com agente de perguntas e servidor MCP.
- **Por que importa:** Dá a agentes de código e ao time um mapa de dependências e chamadas do projeto, ajudando a entender bases grandes e medir o impacto de mudanças sem montar infraestrutura.
- **Áreas:** **Arquitetura de software** (alta) — Explorar dependências e fluxos de chamadas antes de refatorar ou desenhar uma mudança; **Engenharia e produtividade** (alta) — Conectar o grafo via MCP para o agente de código responder com contexto do repositório inteiro
- ⚠️ Licença não padrão; confira os termos antes de uso comercial.

**[DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io)** · ⭐ 37,2 mil · TypeScript · Apache-2.0

- **O que é:** Cria e edita diagramas do draw.io conversando com uma IA, como app web, app desktop e servidor MCP para Claude Code, Cursor, Codex e VS Code.
- **Por que importa:** Gera diagramas editáveis de arquitetura e de fluxos a partir de texto, e o agente de código pode desenhá-los direto pelo MCP.
- **Áreas:** **Arquitetura de software** (alta) — Gerar e ajustar diagramas de arquitetura no draw.io a partir de uma descrição; **Engenharia e produtividade** (média) — Pedir ao agente de código que documente um fluxo em diagrama pelo MCP


## RAG e processamento de documentos

**[microsoft/markitdown](https://github.com/microsoft/markitdown)** · ⭐ 198,8 mil · Python · MIT

- **O que é:** Ferramenta em Python para converter arquivos e documentos do Office em Markdown.
- **Por que importa:** Converte PDF, Word, Excel, PowerPoint e outros em Markdown, o formato que LLMs entendem melhor; peça simples e muito útil em pipelines de IA.
- **Áreas:** **Backend e APIs** (alta) — Converter documentos enviados por usuários antes de mandar para a IA; **Banco de dados e dados** (média) — Padronizar documentos para indexação em RAG

**[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · ⭐ 94,9 mil · Go · Apache-2.0

- **O que é:** Motor de RAG (geração aumentada por recuperação) que virou infraestrutura de contexto para agentes.
- **Por que importa:** Motor de RAG focado em entendimento profundo de documentos (tabelas, layouts); bom para bases de conhecimento complexas.
- **Áreas:** **Backend e APIs** (alta) — Responder perguntas sobre contratos, manuais e PDFs com citações; **Banco de dados e dados** (média) — Estruturar documentos complexos para consulta

**[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** · ⭐ 93,4 mil · Python · Apache-2.0

- **O que é:** Kit de OCR que transforma PDFs e imagens em dados estruturados para IA, com suporte a mais de 100 idiomas.
- **Por que importa:** Kit de OCR leve e preciso que transforma imagens e PDFs escaneados em dados estruturados, com mais de 100 idiomas.
- **Áreas:** **Backend e APIs** (alta) — Ler documentos escaneados (notas, formulários) e extrair campos; **Banco de dados e dados** (média) — Digitalizar documentos em papel para o banco de dados

**[opendatalab/MinerU](https://github.com/opendatalab/MinerU)** · ⭐ 84,5 mil · Python · outra

- **O que é:** Converte documentos complexos (PDF, Office) em Markdown/JSON prontos para LLMs.
- **Por que importa:** Converte PDFs e documentos complexos em Markdown/JSON prontos para LLMs, preservando fórmulas e tabelas.
- **Áreas:** **Backend e APIs** (alta) — Processar PDFs de fornecedores ou contratos antes da análise por IA; **Banco de dados e dados** (média) — Extrair tabelas de documentos para o banco

**[tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)** · ⭐ 77,7 mil · C++ · Apache-2.0

- **O que é:** Tesseract: motor de OCR open source.
- **Por que importa:** Motor de OCR open source clássico e estável; base de muitas soluções de leitura de documentos.
- **Áreas:** **Backend e APIs** (média) — Adicionar OCR simples a um fluxo de documentos

**[redis/redis](https://github.com/redis/redis)** · ⭐ 77,7 mil · C · outra

- **O que é:** Redis: cache e banco em memória para aplicações em tempo real, com estruturas de dados, documentos e busca vetorial.
- **Por que importa:** Cache e banco em memória com estruturas de dados e busca vetorial; peça comum em sistemas com IA para cache, filas e memória semântica.
- **Áreas:** **Banco de dados e dados** (alta) — Usar busca vetorial e cache de respostas de LLM; **Backend e APIs** (alta) — Cache, filas e sessões para APIs de alto desempenho; **Arquitetura de software** (média) — Reduzir latência com uma camada de cache bem desenhada

**[docling-project/docling](https://github.com/docling-project/docling)** · ⭐ 71,2 mil · Python · MIT

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

**[milvus-io/milvus](https://github.com/milvus-io/milvus)** · ⭐ 46,8 mil · Go · Apache-2.0

- **O que é:** Banco de dados vetorial nativo da nuvem e de alto desempenho para busca por similaridade em larga escala.
- **Por que importa:** Opção madura para guardar embeddings e fazer busca semântica em bilhões de vetores, base de sistemas de RAG e recomendação.
- **Áreas:** **Banco de dados e dados** (alta) — Armazenar embeddings e servir busca vetorial para RAG em produção; **DevOps e infraestrutura** (média) — Implantar no Kubernetes quando o volume de vetores crescer

**[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** · ⭐ 42 mil · C++ · MIT

- **O que é:** Biblioteca da Meta para busca eficiente por similaridade e agrupamento de vetores densos, com suporte a GPU.
- **Por que importa:** É o motor de busca vetorial por trás de muitos bancos e sistemas de RAG; indicado quando se quer busca semântica embutida no próprio serviço, sem um banco vetorial separado.
- **Áreas:** **Banco de dados e dados** (alta) — Indexar embeddings em memória e fazer busca por vizinhos mais próximos dentro do serviço; **Backend e APIs** (média) — Embutir busca semântica em uma API Python ou C++ sem depender de serviço externo

**[datalab-to/marker](https://github.com/datalab-to/marker)** · ⭐ 41,1 mil · Python · Apache-2.0

- **O que é:** Converte PDF (e também DOCX, PPTX e EPUB) para Markdown e JSON com rapidez e alta precisão, incluindo tabelas e equações.
- **Por que importa:** Etapa de ingestão confiável para RAG e agentes: transforma documentos complexos em texto estruturado que o LLM entende bem.
- **Áreas:** **Banco de dados e dados** (média) — Converter acervos de PDFs em Markdown estruturado antes de indexar para RAG
- ⚠️ Verifique a licença dos modelos usados antes de uso comercial.

**[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · ⭐ 40,9 mil · Python · MIT

- **O que é:** Framework de RAG simples e rápido que combina grafo de conhecimento e busca vetorial (artigo no EMNLP 2025).
- **Por que importa:** Melhora respostas sobre relações entre entidades com custo de indexação menor que outras abordagens de GraphRAG.
- **Áreas:** **Banco de dados e dados** (média) — Montar um índice com grafo de conhecimento sobre a documentação interna; **Backend e APIs** (média) — Expor perguntas sobre a base de conhecimento por API com o servidor do LightRAG

**[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · ⭐ 40,8 mil · Python · MIT

- **O que é:** Índice de documentos para RAG sem vetores, baseado em raciocínio: o LLM navega por uma árvore de seções como uma pessoa faria.
- **Por que importa:** Boa opção para documentos longos e estruturados (relatórios, contratos, manuais), em que a busca vetorial por pedaços perde o contexto.
- **Áreas:** **Banco de dados e dados** (média) — Indexar documentos longos pela estrutura de seções em vez de embeddings; **Arquitetura de software** (média) — Avaliar RAG sem banco vetorial quando os documentos têm estrutura clara

**[pingcap/tidb](https://github.com/pingcap/tidb)** · ⭐ 40,8 mil · Go · Apache-2.0

- **O que é:** Banco de dados SQL distribuído compatível com MySQL, com transações ACID, análises e busca vetorial nativa, voltado também a cargas de agentes.
- **Por que importa:** Junta dados transacionais, analíticos e vetores no mesmo banco, evitando manter um banco vetorial separado para RAG e memória de agentes.
- **Áreas:** **Banco de dados e dados** (alta) — Guardar dados da aplicação e embeddings no mesmo banco compatível com MySQL; **Arquitetura de software** (média) — Simplificar a arquitetura eliminando bancos separados para análise e vetores

**[The-Vibe-Company/quivr](https://github.com/The-Vibe-Company/quivr)** · ⭐ 39,7 mil · Go · MIT

- **O que é:** Motor open source que transforma fluxos contínuos de conteúdo em busca e monitoramento, com ingestão durável, busca híbrida, alertas e plugins.
- **Por que importa:** Útil para indexar fontes que mudam o tempo todo e disparar alertas, combinando busca por palavras e busca semântica.
- **Áreas:** **Banco de dados e dados** (média) — Ingerir e indexar fontes de conteúdo contínuas com busca híbrida; **Backend e APIs** (média) — Configurar alertas e regras de negócio sobre o conteúdo indexado
- ⚠️ O projeto mudou de proposta (antes era um assistente de segundo cérebro com RAG); confira a documentação atual.

**[google/langextract](https://github.com/google/langextract)** · ⭐ 39,4 mil · Python · Apache-2.0

- **O que é:** Biblioteca Python do Google para extrair informações estruturadas de textos livres com LLMs, ligando cada dado ao trecho de origem, com visualização interativa.
- **Por que importa:** Facilita extrair campos de documentos sabendo de onde cada informação veio, o que ajuda a auditar e corrigir erros do modelo.
- **Áreas:** **Banco de dados e dados** (alta) — Extrair campos estruturados de textos e documentos para alimentar tabelas; **Backend e APIs** (média) — Criar um serviço de extração de dados de documentos com referência à fonte

**[naptha/tesseract.js](https://github.com/naptha/tesseract.js)** · ⭐ 38,9 mil · JavaScript · Apache-2.0

- **O que é:** OCR em JavaScript puro, via WebAssembly, para mais de 100 idiomas, no navegador ou no Node.
- **Por que importa:** Permite extrair texto de imagens direto no navegador ou no Node, sem um servidor de OCR dedicado.
- **Áreas:** **Frontend** (média) — Ler o texto de imagens enviadas pelo usuário direto no navegador

**[Tencent/WeKnora](https://github.com/Tencent/WeKnora)** · ⭐ 38,4 mil · Go · outra

- **O que é:** Plataforma de conhecimento com LLM da Tencent que transforma documentos em RAG consultável, agente de raciocínio e wiki que se mantém sozinha.
- **Por que importa:** Entrega pronta a parte trabalhosa de um RAG corporativo (ingestão, busca, avaliação e multi-tenant), com suporte a modelos locais via Ollama.
- **Áreas:** **Banco de dados e dados** (média) — Transformar a documentação interna em base consultável por RAG; **Backend e APIs** (média) — Integrar perguntas à base de conhecimento ao produto por API
- ⚠️ Licença não padrão; confira os termos.

**[microsoft/graphrag](https://github.com/microsoft/graphrag)** · ⭐ 36,8 mil · Python · MIT

- **O que é:** Sistema modular de RAG baseado em grafos de conhecimento, da Microsoft.
- **Por que importa:** Responde bem a perguntas amplas sobre um acervo inteiro (temas, relações, resumos), onde o RAG vetorial comum falha.
- **Áreas:** **Banco de dados e dados** (média) — Construir um grafo de conhecimento a partir de documentos para consultas globais; **Arquitetura de software** (média) — Comparar GraphRAG com RAG vetorial ao desenhar a busca de um produto
- ⚠️ A indexação consome muitas chamadas de LLM; teste o custo com um acervo pequeno.

**[qdrant/qdrant](https://github.com/qdrant/qdrant)** · ⭐ 35,8 mil · Rust · Apache-2.0

- **O que é:** Banco de dados vetorial e motor de busca vetorial em Rust, de alto desempenho e grande escala, também disponível na nuvem.
- **Por que importa:** Opção rápida e simples de operar para busca semântica e híbrida com filtros, muito usada como base de RAG.
- **Áreas:** **Banco de dados e dados** (alta) — Guardar embeddings com filtros por metadados e servir a busca de um RAG; **DevOps e infraestrutura** (média) — Rodar em contêiner ou cluster próprio com baixo consumo de recursos

**[ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF)** · ⭐ 35,4 mil · Python · MPL-2.0

- **O que é:** Adiciona uma camada de texto OCR a PDFs escaneados para que possam ser pesquisados e copiados.
- **Por que importa:** Prepara PDFs escaneados para indexação e RAG, usando o Tesseract por baixo, em lote e pela linha de comando.
- **Áreas:** **Banco de dados e dados** (média) — Tornar PDFs escaneados pesquisáveis antes de indexá-los

**[baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)** · ⭐ 32,9 mil · Python · MIT

- **O que é:** Modelo de OCR da Baidu para ler documentos longos de uma vez.

**[NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)** · ⭐ 30,6 mil · Jupyter Notebook · outra

- **O que é:** Técnicas avançadas de RAG com explicações e código.

**[opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf)** · ⭐ 30,4 mil · Java · Apache-2.0

- **O que é:** Parser de PDF que gera dados prontos para IA.

**[typesense/typesense](https://github.com/typesense/typesense)** · ⭐ 27,2 mil · C++ · GPL-3.0

- **O que é:** Typesense: busca rápida e tolerante a erros com busca vetorial, alternativa open source ao Algolia e ao Pinecone.

**[Cinnamon/kotaemon](https://github.com/Cinnamon/kotaemon)** · ⭐ 25,9 mil · Python · Apache-2.0

- **O que é:** Kotaemon: ferramenta open source baseada em RAG para conversar com documentos.

**[HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything)** · ⭐ 24,9 mil · Python · MIT

- **O que é:** RAG-Anything: framework de RAG completo para documentos multimodais.

**[PromtEngineer/localGPT](https://github.com/PromtEngineer/localGPT)** · ⭐ 22,2 mil · Python · MIT

- **O que é:** LocalGPT: converse com seus documentos localmente, sem que os dados saiam do dispositivo.

**[datalab-to/surya](https://github.com/datalab-to/surya)** · ⭐ 21,6 mil · Python · Apache-2.0

- **O que é:** Surya: OCR, análise de layout, ordem de leitura e reconhecimento de tabelas em mais de 90 idiomas.

**[firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector)** · ⭐ 20,1 mil · Rust · MIT

- **O que é:** Biblioteca Rust rápida para inspecionar PDFs e extrair texto, detectando os escaneados.


## Modelos, inferência e gateways

**[ollama/ollama](https://github.com/ollama/ollama)** · ⭐ 188,4 mil · Go · MIT

- **O que é:** Roda modelos de IA localmente (Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma e outros).
- **Por que importa:** Forma mais simples de rodar LLMs abertos localmente com uma API; ideal para desenvolvimento, privacidade e reduzir custo.
- **Áreas:** **Backend e APIs** (alta) — Integrar o sistema a um LLM local via API compatível; **Segurança e cibersegurança** (média) — Processar dados sensíveis sem enviá-los a provedores externos; **DevOps e infraestrutura** (média) — Servir modelos internos em servidores próprios

**[Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)** · ⭐ 149 mil · Python · GPL-3.0

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

**[BerriAI/litellm](https://github.com/BerriAI/litellm)** · ⭐ 64,1 mil · Python · outra

- **O que é:** Gateway de IA: chame mais de 100 APIs de LLM no formato da OpenAI, com controle de custo, guardrails, balanceamento e logs.
- **Por que importa:** Gateway que chama mais de 100 APIs de LLM no mesmo formato, com controle de custos, limites, fallback e logs.
- **Áreas:** **Backend e APIs** (alta) — Centralizar chamadas de IA do sistema com troca fácil de provedor; **Arquitetura de software** (alta) — Desacoplar o produto de um fornecedor de modelo específico; **DevOps e infraestrutura** (média) — Monitorar custo e uso de IA por time ou cliente

**[ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)** · ⭐ 55,6 mil · C++ · MIT

- **O que é:** Versão em C/C++ do modelo Whisper da OpenAI (transcrição de fala).
- **Por que importa:** Versão eficiente do Whisper em C/C++ que roda localmente até em CPU e dispositivos menores.
- **Áreas:** **Backend e APIs** (média) — Transcrição local e rápida sem depender de API

**[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** · ⭐ 52,7 mil · Go · AGPL-3.0

- **O que é:** Gateway de IA auto-hospedado com APIs compatíveis com OpenAI, Claude e Gemini, controle de acesso e contabilidade de custos.
- **Por que importa:** Gateway de IA auto-hospedado com APIs compatíveis com OpenAI, Claude e Gemini, controle de acesso e contabilidade de custos.
- **Áreas:** **Backend e APIs** (média) — Distribuir acesso a modelos para vários sistemas com cotas e chaves próprias; **DevOps e infraestrutura** (média) — Controlar gastos com IA por projeto

**[mudler/LocalAI](https://github.com/mudler/LocalAI)** · ⭐ 50,6 mil · Go · MIT

- **O que é:** LocalAI: motor de IA open source para rodar LLMs, visão, voz, imagem e vídeo em qualquer hardware, sem GPU.
- **Por que importa:** Motor de IA open source compatível com a API da OpenAI para texto, imagem, voz e vídeo, sem exigir GPU.
- **Áreas:** **Backend e APIs** (alta) — Trocar a API da OpenAI por uma local sem mudar o código; **DevOps e infraestrutura** (média) — Rodar IA em servidores próprios sem GPU

**[exo-explore/exo](https://github.com/exo-explore/exo)** · ⭐ 48,6 mil · Python · Apache-2.0

- **O que é:** Roda modelos de IA de ponta localmente, distribuindo a inferência entre vários dispositivos da rede, como Macs e PCs.
- **Por que importa:** Permite somar a memória de várias máquinas para rodar modelos grandes sem nuvem, útil para manter dados privados ou testar modelos abertos.
- **Áreas:** **DevOps e infraestrutura** (média) — Montar um cluster local de inferência com máquinas que o time já tem

**[oobabooga/textgen](https://github.com/oobabooga/textgen)** · ⭐ 47,8 mil · Python · AGPL-3.0

- **O que é:** App desktop open source para rodar LLMs locais, com texto, visão, chamada de ferramentas e API compatível com OpenAI e Anthropic.
- **Por que importa:** Jeito simples de testar modelos abertos na própria máquina e expô-los por uma API compatível, mantendo os dados privados.
- **Áreas:** **Backend e APIs** (média) — Servir um modelo local por API compatível com OpenAI para desenvolvimento e testes
- ⚠️ Licença AGPL: verifique antes de uso comercial fechado.

**[Kong/kong](https://github.com/Kong/kong)** · ⭐ 44,4 mil · Lua · Apache-2.0

- **O que é:** Gateway de APIs e de IA nativo da nuvem, com plugins para autenticação, limite de requisições e roteamento entre provedores de LLM.
- **Por que importa:** Centraliza o tráfego de APIs e de chamadas a LLMs com controle de custo, segurança e observabilidade, sem mudar o código dos serviços.
- **Áreas:** **Backend e APIs** (alta) — Expor e proteger APIs e chamadas a LLMs com autenticação e limite de requisições; **DevOps e infraestrutura** (alta) — Rodar como ingress no Kubernetes com políticas centralizadas; **Segurança e cibersegurança** (média) — Aplicar políticas de acesso e filtragem de prompts nas chamadas a modelos

**[lyogavin/airllm](https://github.com/lyogavin/airllm)** · ⭐ 43,6 mil · Jupyter Notebook · Apache-2.0

- **O que é:** Biblioteca que roda LLMs muito grandes em GPUs com pouca memória, como 4 GB, carregando o modelo camada por camada.
- **Por que importa:** Permite experimentar modelos grandes em hardware modesto, útil para testes e estudos quando não há GPU potente disponível.
- ⚠️ Economiza memória à custa de velocidade: a inferência fica bem mais lenta e pouco indicada para produção.

**[microsoft/BitNet](https://github.com/microsoft/BitNet)** · ⭐ 42,5 mil · C++ · MIT

- **O que é:** Framework oficial da Microsoft para inferência de LLMs de 1 bit (como o BitNet b1.58), otimizado para CPU.
- **Por que importa:** Mostra como rodar modelos quantizados ao extremo em CPU comum, com bem menos memória e energia, útil para IA local ou embarcada.
- ⚠️ Funciona só com modelos treinados no formato de 1 bit, que ainda são poucos.

**[lm-sys/FastChat](https://github.com/lm-sys/FastChat)** · ⭐ 39,6 mil · Python · Apache-2.0

- **O que é:** Plataforma aberta para treinar, servir e avaliar modelos de linguagem grandes; repositório de origem do Vicuna e do Chatbot Arena.
- **Por que importa:** Reúne servidor com API compatível com OpenAI, interface web e ferramentas de avaliação de modelos abertos, útil para estudar e comparar LLMs.
- **Áreas:** **Backend e APIs** (média) — Servir modelos abertos com API compatível com OpenAI em ambiente de testes
- ⚠️ Atividade menor nos últimos meses; para servir em produção, vLLM e SGLang são mais usados hoje.

**[AlexsJones/llmfit](https://github.com/AlexsJones/llmfit)** · ⭐ 39,4 mil · Rust · MIT

- **O que é:** Ferramenta de linha de comando que descobre, com um comando, quais modelos e provedores rodam bem no seu hardware.
- **Por que importa:** Evita tentativa e erro ao escolher um modelo local, indicando o que cabe na memória e no processador disponíveis.
- **Áreas:** **DevOps e infraestrutura** (média) — Verificar quais modelos locais cabem nas máquinas do time ou do servidor antes de instalar
- ⚠️ Projeto recente.

**[sgl-project/sglang](https://github.com/sgl-project/sglang)** · ⭐ 39,1 mil · Python · Apache-2.0

- **O que é:** Framework de alto desempenho para servir LLMs e modelos multimodais.
- **Por que importa:** Uma das opções mais rápidas para servir modelos abertos em produção, com cache de prefixo e boa vazão; alternativa ao vLLM.
- **Áreas:** **DevOps e infraestrutura** (alta) — Servir modelos abertos em GPUs com API compatível com OpenAI; **Backend e APIs** (média) — Reduzir a latência de apps com prompts repetidos usando o cache de prefixo

**[musistudio/claude-code-router](https://github.com/musistudio/claude-code-router)** · ⭐ 38,4 mil · TypeScript · MIT

- **O que é:** Plano de controle local que roteia o Claude Code e outros agentes de IA entre diferentes modelos e provedores.
- **Por que importa:** Permite usar o Claude Code com modelos mais baratos ou locais em tarefas simples e escolher o modelo por tipo de tarefa, reduzindo custo.
- **Áreas:** **Engenharia e produtividade** (média) — Rotear tarefas do agente de código para modelos diferentes conforme custo e complexidade

**[songquanpeng/one-api](https://github.com/songquanpeng/one-api)** · ⭐ 37,5 mil · JavaScript · MIT

- **O que é:** Sistema de gestão e distribuição de APIs de LLM que unifica OpenAI, Azure, Claude, Gemini, DeepSeek e modelos chineses sob uma API única, com controle de chaves.
- **Por que importa:** Centraliza chaves, cotas e provedores atrás de uma API compatível com OpenAI, facilitando trocar de modelo sem mudar a aplicação.
- **Áreas:** **Backend e APIs** (média) — Colocar um gateway único na frente de vários provedores de LLM; **DevOps e infraestrutura** (média) — Controlar chaves e cotas de uso por equipe ou projeto
- ⚠️ Pouca atividade desde janeiro de 2026; o fork new-api é mais ativo.

**[huggingface/diffusers](https://github.com/huggingface/diffusers)** · ⭐ 35 mil · Python · Apache-2.0

- **O que é:** Biblioteca do Hugging Face com modelos de difusão de ponta para gerar imagens, vídeo e áudio em PyTorch.
- **Por que importa:** Base padrão para integrar geração de imagens em produtos e pipelines próprios, com dezenas de modelos abertos prontos.
- **Áreas:** **Backend e APIs** (média) — Integrar geração de imagens com modelos abertos em um serviço próprio

**[onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx)** · ⭐ 33,6 mil · Python · outra

- **O que é:** Onyx: plataforma open source de IA com chat e busca nos documentos da empresa, compatível com qualquer LLM.

**[openai/openai-python](https://github.com/openai/openai-python)** · ⭐ 32,3 mil · Python · Apache-2.0

- **O que é:** Biblioteca Python oficial da API da OpenAI.

**[HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)** · ⭐ 30,4 mil · Jupyter Notebook · Apache-2.0

- **O que é:** Código oficial do livro "Hands-On Large Language Models" (O'Reilly).

**[labring/FastGPT](https://github.com/labring/FastGPT)** · ⭐ 30,1 mil · TypeScript · outra

- **O que é:** FastGPT: plataforma de conhecimento com LLMs, com RAG, fluxos visuais e agentes prontos.

**[yamadashy/repomix](https://github.com/yamadashy/repomix)** · ⭐ 29,5 mil · TypeScript · MIT

- **O que é:** Repomix: empacota o repositório inteiro em um único arquivo pronto para IA.

**[charmbracelet/crush](https://github.com/charmbracelet/crush)** · ⭐ 29,2 mil · Go · outra

- **O que é:** Crush: agente de código no terminal, da Charm.

**[microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)** · ⭐ 28,8 mil · C# · MIT

- **O que é:** Semantic Kernel: SDK da Microsoft para integrar LLMs em aplicações C#, Python e Java.

**[vercel/ai](https://github.com/vercel/ai)** · ⭐ 28,3 mil · TypeScript · outra

- **O que é:** AI SDK: biblioteca TypeScript da Vercel para construir apps e agentes com IA.

**[SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)** · ⭐ 27,1 mil · Python · MIT

- **O que é:** Transcrição com Whisper mais rápida usando CTranslate2.

**[mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile)** · ⭐ 26,7 mil · C++ · outra

- **O que é:** llamafile: distribui e roda LLMs com um único arquivo executável.

**[deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer)** · ⭐ 26,4 mil · Python · Apache-2.0

- **O que é:** DeepInfer: framework de inferência em larga escala para modelos DeepSeek.

**[m-bain/whisperX](https://github.com/m-bain/whisperX)** · ⭐ 26 mil · Python · BSD-2-Clause

- **O que é:** WhisperX: reconhecimento de fala com marcação de tempo por palavra e separação de falantes.

**[toon-format/toon](https://github.com/toon-format/toon)** · ⭐ 25,7 mil · TypeScript · MIT

- **O que é:** TOON: formato compacto para enviar dados JSON em prompts, economizando tokens.

**[antirez/ds4](https://github.com/antirez/ds4)** · ⭐ 24,5 mil · C · MIT

- **O que é:** Motor de inferência local dos modelos DeepSeek 4 para Metal, CUDA e ROCm.

**[sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai)** · ⭐ 24 mil · Python · outra

- **O que é:** PandasAI: converse com seu banco de dados ou data lake (SQL, CSV, parquet) usando LLMs.

**[comet-ml/opik](https://github.com/comet-ml/opik)** · ⭐ 23,5 mil · Java · Apache-2.0

- **O que é:** Opik: depura, avalia e monitora apps com LLM, RAG e agentes.

**[mlc-ai/mlc-llm](https://github.com/mlc-ai/mlc-llm)** · ⭐ 23,4 mil · Python · Apache-2.0

- **O que é:** MLC LLM: motor universal de deploy de LLMs com compilação de ML.

**[dyad-sh/dyad](https://github.com/dyad-sh/dyad)** · ⭐ 22,5 mil · TypeScript · outra

- **O que é:** Dyad: construtor local e open source de apps com IA, alternativa a v0, Lovable e Bolt.

**[guidance-ai/guidance](https://github.com/guidance-ai/guidance)** · ⭐ 21,8 mil · Jupyter Notebook · MIT

- **O que é:** Guidance: linguagem para controlar e estruturar a saída de LLMs.

**[openai/gpt-oss](https://github.com/openai/gpt-oss)** · ⭐ 20,6 mil · Python · Apache-2.0

- **O que é:** gpt-oss: modelos de pesos abertos da OpenAI (120b e 20b).

**[eosphoros-ai/DB-GPT](https://github.com/eosphoros-ai/DB-GPT)** · ⭐ 20,3 mil · Python · MIT

- **O que é:** DB-GPT: agentes de dados controlados para consultas e análises em bancos de dados.


## Treino e frameworks de ML

**[tensorflow/tensorflow](https://github.com/tensorflow/tensorflow)** · ⭐ 201,7 mil · C++ · Apache-2.0

- **O que é:** Framework open source de Machine Learning.
- **Por que importa:** Framework de machine learning do Google, forte em produção e em dispositivos (TensorFlow Lite).
- **Áreas:** **Backend e APIs** (média) — Servir modelos de ML em produção ou em dispositivos móveis

**[huggingface/transformers](https://github.com/huggingface/transformers)** · ⭐ 169,3 mil · Python · Apache-2.0

- **O que é:** Transformers: framework de definição de modelos de ML de ponta para texto, visão, áudio e multimodal, em inferência e treino.
- **Por que importa:** Biblioteca padrão para usar e ajustar modelos de texto, visão e áudio do Hugging Face.
- **Áreas:** **Backend e APIs** (alta) — Usar modelos prontos de classificação, extração e embeddings no backend; **Banco de dados e dados** (média) — Gerar embeddings para busca semântica

**[pytorch/pytorch](https://github.com/pytorch/pytorch)** · ⭐ 105,7 mil · Python · outra

- **O que é:** PyTorch: tensores e redes neurais dinâmicas em Python com aceleração por GPU.
- **Por que importa:** Framework de deep learning mais usado em pesquisa e produção; base de boa parte dos modelos atuais.
- **Áreas:** **Backend e APIs** (média) — Treinar ou servir modelos próprios quando APIs prontas não atendem

**[opencv/opencv](https://github.com/opencv/opencv)** · ⭐ 91,8 mil · C++ · Apache-2.0

- **O que é:** OpenCV: biblioteca open source de visão computacional.
- **Por que importa:** Biblioteca de visão computacional mais usada; base para processamento de imagens e vídeo.
- **Áreas:** **Backend e APIs** (média) — Processar imagens (recorte, detecção, leitura) no backend

**[unslothai/unsloth](https://github.com/unslothai/unsloth)** · ⭐ 80,4 mil · Python · Apache-2.0

- **O que é:** Interface local para rodar e treinar LLMs e modelos de difusão, com suporte a vários formatos e modelos.
- **Por que importa:** Ajuste fino (fine-tuning) de LLMs mais rápido e com menos memória, com interface local.
- **Áreas:** **Backend e APIs** (média) — Especializar um modelo aberto no vocabulário e nas tarefas do cliente

**[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** · ⭐ 76,3 mil · Python · Apache-2.0

- **O que é:** Fine-tuning eficiente e unificado de mais de 100 LLMs e modelos de visão e linguagem.
- **Por que importa:** Ajuste fino unificado de mais de 100 LLMs e modelos de visão, com interface web.
- **Áreas:** **Backend e APIs** (média) — Fazer fine-tuning de modelos abertos sem montar o pipeline do zero

**[scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)** · ⭐ 68,3 mil · Python · BSD-3-Clause

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

**[ray-project/ray](https://github.com/ray-project/ray)** · ⭐ 44,4 mil · Python · Apache-2.0

- **O que é:** Motor de computação distribuída para IA, com runtime de cluster e bibliotecas para dados, treino, ajuste e serving de modelos.
- **Por que importa:** Escala código Python de uma máquina para um cluster sem reescrever, e é base comum para servir LLMs e processar dados em lote.
- **Áreas:** **DevOps e infraestrutura** (média) — Distribuir inferência e jobs de dados em um cluster com Ray Serve e Ray Data; **Banco de dados e dados** (média) — Processar grandes volumes de dados em paralelo antes de treinar ou indexar

**[deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed)** · ⭐ 43,4 mil · Python · Apache-2.0

- **O que é:** Biblioteca de otimização de deep learning (criada na Microsoft) que torna treino e inferência distribuídos mais fáceis, eficientes e baratos.
- **Por que importa:** Reduz memória e custo para treinar ou ajustar modelos grandes em várias GPUs, com técnicas como ZeRO e paralelismo de modelo.
- **Áreas:** **DevOps e infraestrutura** (média) — Configurar treinos e ajustes finos distribuídos em várias GPUs

**[hpcaitech/ColossalAI](https://github.com/hpcaitech/ColossalAI)** · ⭐ 41,4 mil · Python · Apache-2.0

- **O que é:** Sistema para treinar e rodar modelos de IA grandes de forma mais barata e rápida, com várias estratégias de paralelismo.
- **Por que importa:** Útil para times que treinam ou ajustam modelos grandes em várias GPUs e precisam reduzir memória e custo.
- **Áreas:** **DevOps e infraestrutura** (média) — Distribuir o treino de modelos grandes em clusters de GPU

**[google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe)** · ⭐ 37,9 mil · C++ · Apache-2.0

- **O que é:** Soluções de ML multiplataforma do Google para mídia ao vivo e em streaming, como detecção de rosto, mãos, pose e objetos.
- **Por que importa:** Entrega modelos prontos e otimizados para rodar no próprio dispositivo (web, Android, iOS), sem precisar treinar nada.
- **Áreas:** **Frontend** (média) — Adicionar detecção de mãos, rosto ou objetos em apps web e mobile direto no dispositivo

**[huggingface/pytorch-image-models](https://github.com/huggingface/pytorch-image-models)** · ⭐ 37,3 mil · Python · Apache-2.0

- **O que é:** A maior coleção de encoders e backbones de imagem em PyTorch, com pesos pré-treinados e scripts de treino, avaliação, inferência e exportação.
- **Por que importa:** Atalho para usar ou ajustar modelos de visão consolidados (ViT, ConvNeXt, EfficientNet) sem implementar do zero.

**[jax-ml/jax](https://github.com/jax-ml/jax)** · ⭐ 36,7 mil · Python · Apache-2.0

- **O que é:** Biblioteca do Google para transformar programas Python e NumPy: diferenciação automática, vetorização e compilação JIT para GPU e TPU.
- **Por que importa:** Base de pesquisa e treino de modelos de alto desempenho (inclusive no Google), indicada para quem precisa de controle fino e escala em TPU.
- **Áreas:** **DevOps e infraestrutura** (média) — Treinar e escalar modelos em GPUs e TPUs com compilação JIT

**[explosion/spaCy](https://github.com/explosion/spaCy)** · ⭐ 34,1 mil · Python · MIT

- **O que é:** Biblioteca Python de processamento de linguagem natural para uso industrial, com reconhecimento de entidades, análise sintática e mais.
- **Por que importa:** Opção rápida e barata para tarefas de texto previsíveis (entidades, classificação), sem pagar uma chamada de LLM por documento.
- **Áreas:** **Backend e APIs** (média) — Extrair entidades e classificar textos em serviços Python; **Banco de dados e dados** (média) — Pré-processar textos antes de indexar ou analisar

**[lutzroeder/netron](https://github.com/lutzroeder/netron)** · ⭐ 33,7 mil · JavaScript · MIT

- **O que é:** Visualizador de redes neurais e modelos de machine learning (ONNX, PyTorch, TensorFlow, safetensors e outros).
- **Por que importa:** Permite inspecionar a estrutura, as entradas e as saídas de um modelo antes de integrá-lo à aplicação.
- **Áreas:** **Engenharia e produtividade** (média) — Inspecionar entradas, saídas e camadas de um modelo antes de integrá-lo

**[Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)** · ⭐ 31,5 mil · Python · Apache-2.0

- **O que é:** PyTorch Lightning: treine e ajuste modelos de IA de qualquer tamanho, em uma ou milhares de GPUs, sem mudar o código.

**[modular/modular](https://github.com/modular/modular)** · ⭐ 30,2 mil · Mojo · outra

- **O que é:** Plataforma Modular (MAX e Mojo) para inferência de IA de alto desempenho.

**[JaidedAI/EasyOCR](https://github.com/JaidedAI/EasyOCR)** · ⭐ 30,2 mil · Python · Apache-2.0

- **O que é:** EasyOCR: OCR pronto para uso com mais de 80 idiomas.

**[dmlc/xgboost](https://github.com/dmlc/xgboost)** · ⭐ 29 mil · C++ · Apache-2.0

- **O que é:** XGBoost: biblioteca de gradient boosting escalável para modelos de previsão.

**[HumanSignal/label-studio](https://github.com/HumanSignal/label-studio)** · ⭐ 28,8 mil · TypeScript · Apache-2.0

- **O que é:** Label Studio: ferramenta de rotulagem e anotação de dados para treinar modelos.

**[fastai/fastai](https://github.com/fastai/fastai)** · ⭐ 28,3 mil · Jupyter Notebook · Apache-2.0

- **O que é:** fastai: biblioteca de deep learning de alto nível.

**[shap/shap](https://github.com/shap/shap)** · ⭐ 25,9 mil · Jupyter Notebook · MIT

- **O que é:** SHAP: explica as saídas de qualquer modelo de machine learning.

**[lukasmasuch/best-of-ml-python](https://github.com/lukasmasuch/best-of-ml-python)** · ⭐ 23,9 mil · CC-BY-SA-4.0

- **O que é:** Lista ranqueada das melhores bibliotecas Python de machine learning, atualizada toda semana.

**[dipakkr/awesome-ai-engineering](https://github.com/dipakkr/awesome-ai-engineering)** · ⭐ 22,6 mil · MIT

- **O que é:** Coleção de recursos de engenharia de IA: LLMs, RAG, agentes, MCP e mais.

**[huggingface/datasets](https://github.com/huggingface/datasets)** · ⭐ 22,2 mil · Python · Apache-2.0

- **O que é:** Datasets da Hugging Face: maior hub de datasets prontos para IA, com ferramentas de manipulação.

**[recommenders-team/recommenders](https://github.com/recommenders-team/recommenders)** · ⭐ 22 mil · Python · MIT

- **O que é:** Boas práticas e código de sistemas de recomendação (Microsoft).

**[huggingface/peft](https://github.com/huggingface/peft)** · ⭐ 21,9 mil · Python · Apache-2.0

- **O que é:** PEFT: ajuste fino eficiente em parâmetros (LoRA e outros) da Hugging Face.

**[onnx/onnx](https://github.com/onnx/onnx)** · ⭐ 21,8 mil · Python · Apache-2.0

- **O que é:** ONNX: padrão aberto para interoperabilidade de modelos de ML.


## Design e interfaces com IA

**[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · ⭐ 155,3 mil · Python · MIT

- **O que é:** Skill de IA com conhecimento de design para criar UI/UX profissional em várias plataformas.
- **Por que importa:** Skill com conhecimento de design (estilos, paletas, tipografia, padrões de UX) para o agente criar interfaces profissionais.
- **Áreas:** **Design e UI/UX** (alta) — Dar ao agente referências de estilo e UX ao criar telas; **Frontend** (alta) — Gerar páginas e componentes com visual consistente

**[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · ⭐ 129,5 mil · MIT

- **O que é:** Coleção de arquivos DESIGN.md com análises de design systems de marcas famosas, para agentes de código gerarem interfaces no mesmo estilo.
- **Por que importa:** Arquivos DESIGN.md baseados em design systems de marcas conhecidas; você coloca um no projeto e o agente gera UI coerente com aquele estilo.
- **Áreas:** **Design e UI/UX** (alta) — Dar ao agente um design system de referência em um único arquivo; **Frontend** (alta) — Gerar interfaces consistentes com o estilo escolhido

**[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** · ⭐ 122,4 mil · JavaScript · MIT

- **O que é:** Skills que dão "bom gosto" visual a agentes de código: direção de arte, imagens de referência e checagem no navegador.
- **Por que importa:** Skills que dão direção de arte ao agente e conferem o resultado no navegador; evita páginas com cara de 'gerado por IA'.
- **Áreas:** **Design e UI/UX** (alta) — Definir direção de arte e referências antes de o agente criar a interface; **Frontend** (média) — Checar visualmente no navegador o que foi gerado

**[pbakaus/impeccable](https://github.com/pbakaus/impeccable)** · ⭐ 118,2 mil · Rust · Apache-2.0

- **O que é:** Vocabulário de design para agentes de código: refinar, revisar, auditar e barrar interfaces genéricas de IA.
- **Por que importa:** Vocabulário de design para agentes de código: comandos para refinar, revisar e auditar interfaces.
- **Áreas:** **Design e UI/UX** (alta) — Revisar e polir interfaces geradas com comandos de crítica e auditoria; **Frontend** (média) — Ajustar hierarquia visual e espaçamentos com o agente

**[nexu-io/open-design](https://github.com/nexu-io/open-design)** · ⭐ 109,9 mil · TypeScript · Apache-2.0

- **O que é:** Workspace colaborativo de design com agentes de IA, local e open source: protótipos, sites, apps, dashboards, apresentações, imagens e vídeos.
- **Por que importa:** Workspace colaborativo de design com agentes de IA para protótipos, sites, apps e dashboards; local e open source.
- **Áreas:** **Design e UI/UX** (alta) — Prototipar telas e fluxos com IA junto com o time; **Frontend** (média) — Transformar protótipos em páginas e componentes
- ⚠️ Projeto recente; avalie estabilidade.

**[abi/screenshot-to-code](https://github.com/abi/screenshot-to-code)** · ⭐ 81,5 mil · Python · MIT

- **O que é:** Converte uma captura de tela em código limpo (HTML/Tailwind/React/Vue).
- **Por que importa:** Transforma uma captura de tela ou mockup em código HTML/Tailwind/React/Vue; acelera a passagem do design para o front.
- **Áreas:** **Frontend** (alta) — Gerar a primeira versão de uma tela a partir de um print ou layout; **Design e UI/UX** (média) — Validar rapidamente um layout transformando-o em protótipo navegável

**[Nutlope/hallmark](https://github.com/Nutlope/hallmark)** · ⭐ 62,2 mil · CSS · MIT

- **O que é:** Skill de design contra interfaces genéricas geradas por IA, para Claude Code, Cursor e Codex.
- **Por que importa:** Skill de design contra interfaces genéricas de IA para Claude Code, Cursor e Codex.
- **Áreas:** **Design e UI/UX** (alta) — Evitar layouts genéricos em landing pages e telas geradas por IA; **Frontend** (média) — Melhorar o acabamento de páginas feitas com agentes

**[streamlit/streamlit](https://github.com/streamlit/streamlit)** · ⭐ 46,5 mil · Python · Apache-2.0

- **O que é:** Framework Python para criar apps de dados e dashboards rapidamente, agora com foco em apps feitos com e para agentes.
- **Por que importa:** Transforma um script Python em interface web em minutos, ótimo para protótipos de apps com LLM e ferramentas internas de dados.
- **Áreas:** **Frontend** (média) — Montar a interface de um protótipo de app com LLM sem escrever frontend; **Banco de dados e dados** (média) — Criar painéis internos de análise sobre bancos e planilhas

**[gradio-app/gradio](https://github.com/gradio-app/gradio)** · ⭐ 44,2 mil · Python · Apache-2.0

- **O que é:** Biblioteca Python para criar e compartilhar interfaces web de apps de machine learning com poucas linhas de código.
- **Por que importa:** Jeito mais rápido de colocar uma demo de modelo ou agente na frente de usuários, com API automática e hospedagem fácil no Hugging Face Spaces.
- **Áreas:** **Frontend** (média) — Criar a interface de uma demo de modelo ou agente sem escrever frontend

**[CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit)** · ⭐ 39 mil · TypeScript · MIT

- **O que é:** Stack de frontend para agentes e interfaces generativas, com React, Angular, mobile e Slack; dos criadores do protocolo AG-UI.
- **Por que importa:** Economiza o trabalho de construir chat, estado compartilhado e componentes gerados por agentes dentro do app, ligando o frontend a qualquer backend de agentes.
- **Áreas:** **Frontend** (alta) — Embutir um copiloto ou agente no app React com componentes e estado compartilhado; **Design e UI/UX** (média) — Criar interfaces generativas em que o agente monta componentes na tela

**[onlook-dev/onlook](https://github.com/onlook-dev/onlook)** · ⭐ 28 mil · TypeScript · Apache-2.0

- **O que é:** Onlook: ferramenta de design com IA para editar visualmente o código de apps React.

**[wandb/openui](https://github.com/wandb/openui)** · ⭐ 22,8 mil · TypeScript · Apache-2.0

- **O que é:** OpenUI: descreva uma interface e veja ela renderizada ao vivo.


## Segurança com IA

**[morluto/rea](https://github.com/morluto/rea)** · ⭐ 481,5 mil · TypeScript · MIT

- **O que é:** Ferramenta com agentes de IA para engenharia reversa, do comportamento de aplicativos até binários nativos, com integração a assistentes de código como o Claude Code.
- **Por que importa:** Agentes de IA para engenharia reversa de apps e binários; pode acelerar auditorias de segurança e análise de integrações sem documentação.
- **Áreas:** **Segurança e cibersegurança** (média) — Analisar binários e comportamento de apps em auditorias
- ⚠️ Projeto muito recente com crescimento de estrelas fora do comum; avalie maturidade e implicações legais.

**[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** · ⭐ 79,4 mil · JavaScript · MIT

- **O que é:** Skill para agentes de código fazerem auditorias de segurança em várias fases, com achados verificados.
- **Por que importa:** Skill da Cloudflare para auditorias de segurança em várias fases com achados verificados; leva revisão de segurança para dentro do agente de código.
- **Áreas:** **Segurança e cibersegurança** (alta) — Fazer auditoria de segurança do código com o próprio agente; **Testes e QA** (média) — Gerar relatório de achados verificados para correção

**[usestrix/strix](https://github.com/usestrix/strix)** · ⭐ 78,1 mil · Python · Apache-2.0

- **O que é:** Ferramenta open source de pentest com IA para encontrar e corrigir vulnerabilidades da sua aplicação.
- **Por que importa:** Pentest com IA open source: agentes que encontram e ajudam a corrigir vulnerabilidades da aplicação.
- **Áreas:** **Segurança e cibersegurança** (alta) — Rodar testes de invasão automatizados antes de publicar; **Testes e QA** (média) — Incluir verificação de segurança no ciclo de testes

**[KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)** · ⭐ 52,4 mil · TypeScript · AGPL-3.0

- **O que é:** Pentester com IA para aplicações web e APIs: analisa o código e executa ataques reais para provar vulnerabilidades.
- **Por que importa:** Pentester com IA para aplicações web e APIs: lê o código, identifica vetores de ataque e executa explorações reais para provar falhas.
- **Áreas:** **Segurança e cibersegurança** (alta) — Validar vulnerabilidades reais em APIs antes da produção; **Backend e APIs** (média) — Auditar endpoints e autenticação do backend
- ⚠️ Use só em sistemas próprios ou com autorização.

**[ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi)** · ⭐ 47,8 mil · Python · Apache-2.0

- **O que é:** Ferramenta de linha de comando para auditar agentes de IA de forma independente e verificar se fazem o que deveriam, com resultado em cerca de dois minutos.
- **Por que importa:** Ajuda a checar comportamento, alucinações e aderência a normas como EU AI Act e ISO 42001 antes de colocar um agente em produção.
- **Áreas:** **Testes e QA** (média) — Rodar a auditoria como etapa de verificação antes de liberar uma nova versão de um agente; **Segurança e cibersegurança** (média) — Levantar riscos de governança e segurança dos agentes em uso
- ⚠️ Projeto muito recente com crescimento de estrelas fora do comum; valide os resultados antes de confiar neles.

**[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)** · ⭐ 45,4 mil · PowerShell · MIT

- **O que é:** Pacote de skills para engenharia reversa, pentest autorizado e pesquisa de segurança, com roteamento por IA e instalação de ferramentas sob demanda para Claude Code, Cursor e outros.
- **Por que importa:** Reúne o conhecimento de ferramentas de segurança para o agente escolher a certa em cada tarefa, acelerando análises de binários e testes de invasão autorizados.
- **Áreas:** **Segurança e cibersegurança** (média) — Apoiar análises de engenharia reversa e pentest autorizado com um agente de código
- ⚠️ Projeto muito recente com crescimento de estrelas fora do comum; use só com autorização e revise as ferramentas que ele baixa e executa.

**[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)** · ⭐ 36,9 mil · Python · Apache-2.0

- **O que é:** Coleção de 817 skills de cibersegurança para agentes de IA, mapeadas para MITRE ATT&CK, NIST CSF 2.0 e outros frameworks, no padrão agentskills.io.
- **Por que importa:** Dá ao agente procedimentos estruturados de resposta a incidentes, análise de malware, segurança em nuvem e DevSecOps alinhados a frameworks reconhecidos.
- **Áreas:** **Segurança e cibersegurança** (alta) — Instalar skills de resposta a incidentes e análise de ameaças no agente do time de segurança; **DevOps e infraestrutura** (média) — Apoiar revisões de segurança em nuvem e DevSecOps com skills mapeadas ao NIST
- ⚠️ Não é um projeto oficial da Anthropic, apesar do nome; revise as skills antes de usar.

**[vxcontrol/pentagi](https://github.com/vxcontrol/pentagi)** · ⭐ 35,2 mil · Go · MIT

- **O que é:** Sistema de agentes de IA totalmente autônomos para executar tarefas complexas de teste de invasão.
- **Por que importa:** Automatiza etapas de pentest com vários agentes e ferramentas de segurança em ambiente isolado, ajudando a achar falhas antes dos atacantes.
- **Áreas:** **Segurança e cibersegurança** (alta) — Rodar testes de invasão automatizados em ambientes próprios; **Testes e QA** (média) — Incluir varreduras ofensivas automatizadas nos ambientes de homologação
- ⚠️ Use só em sistemas próprios ou com autorização.

**[BaaRai/ARTEX](https://github.com/BaaRai/ARTEX)** · ⭐ 23,9 mil · Go · AGPL-3.0

- **O que é:** Sistema autônomo de pentest com IA, auto-hospedado e independente de modelo.

**[SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent)** · ⭐ 20,9 mil · Python · MIT

- **O que é:** SWE-agent: recebe uma issue do GitHub e tenta corrigi-la automaticamente.


## Gestão de agentes e produtividade

**[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · ⭐ 157,7 mil · Rust · MIT

- **O que é:** Assistente de desktop multiplataforma para gerenciar Claude Code, Codex, OpenCode, DeepSeek Harness e outros.
- **Por que importa:** Assistente desktop para alternar e configurar Claude Code, Codex, OpenCode e outros num só lugar.
- **Áreas:** **Engenharia e produtividade** (média) — Gerenciar configurações e provedores de vários agentes de código

**[stablyai/orca](https://github.com/stablyai/orca)** · ⭐ 143 mil · TypeScript · MIT

- **O que é:** Roda uma frota de bots usando sua própria assinatura (Claude Code, Grok, Codex etc.), no desktop, no celular ou remoto.
- **Por que importa:** Roda uma frota de agentes de código usando suas assinaturas, no desktop, celular ou remoto.
- **Áreas:** **Engenharia e produtividade** (média) — Paralelizar tarefas entre vários agentes de código
- ⚠️ Projeto recente.

**[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · ⭐ 117,7 mil · TypeScript · MIT

- **O que é:** App open source para gerenciar agentes de IA no trabalho.
- **Por que importa:** App open source para gerenciar agentes de IA no trabalho: tarefas, papéis e acompanhamento.
- **Áreas:** **Engenharia e produtividade** (média) — Organizar o trabalho de vários agentes como se fossem membros do time
- ⚠️ Projeto recente.

**[pingdotgg/t3code](https://github.com/pingdotgg/t3code)** · ⭐ 82,5 mil · TypeScript · MIT

- **O que é:** Controle o Claude Code, o Codex e outros a partir de qualquer computador ou celular.
- **Por que importa:** Controla Claude Code, Codex e outros a partir de qualquer computador ou celular.
- **Áreas:** **Engenharia e produtividade** (média) — Acompanhar e comandar agentes de código remotamente

**[multica-ai/multica](https://github.com/multica-ai/multica)** · ⭐ 58,2 mil · Go · outra

- **O que é:** Quadro de tarefas compartilhado em que pessoas e agentes de código trabalham como colegas de time; auto-hospedável.
- **Por que importa:** Quadro de tarefas compartilhado em que pessoas e agentes de código trabalham juntos; auto-hospedável.
- **Áreas:** **Engenharia e produtividade** (média) — Distribuir tarefas entre devs e agentes no mesmo quadro
- ⚠️ Licença source-available; confira os termos.

**[herdrdev/herdr](https://github.com/herdrdev/herdr)** · ⭐ 53,3 mil · Rust · Apache-2.0

- **O que é:** Runtime onde seus agentes de código rodam.
- **Por que importa:** Runtime para hospedar e gerenciar agentes de código em execução.
- **Áreas:** **Engenharia e produtividade** (média) — Manter agentes de código rodando e organizados em sessões; **DevOps e infraestrutura** (média) — Padronizar onde e como os agentes rodam
- ⚠️ Projeto recente.

**[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** · ⭐ 34,6 mil · TypeScript · Apache-2.0

- **O que é:** App open source de cowork para usar Claude Code, Codex, OpenCode, Gemini CLI e mais de 20 agentes de linha de comando numa interface gráfica, com times de assistentes.
- **Por que importa:** Dá uma interface única para gerenciar vários agentes de terminal, útil para quem alterna entre eles ou quer agentes trabalhando em paralelo.
- **Áreas:** **Engenharia e produtividade** (média) — Gerenciar sessões de vários agentes de código numa interface só

**[wavetermdev/waveterm](https://github.com/wavetermdev/waveterm)** · ⭐ 22,8 mil · Go · Apache-2.0

- **O que é:** Terminal open source multiplataforma com IA integrada.


## Aprendizado de IA

**[Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)** · ⭐ 146 mil · Python · Apache-2.0

- **O que é:** Mais de 100 agentes de IA, skills e apps de RAG gratuitos e open source.
- **Por que importa:** Mais de 100 exemplos de agentes, skills e apps de RAG com código; ótimo catálogo de ideias e referências de implementação.
- **Áreas:** **Backend e APIs** (média) — Copiar padrões de implementação de agentes e RAG; **Arquitetura de software** (média) — Comparar arquiteturas de apps com LLM antes de escolher a sua

**[microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)** · ⭐ 124,5 mil · Jupyter Notebook · MIT

- **O que é:** 21 aulas para começar a construir com IA generativa (Microsoft).
- **Por que importa:** Curso gratuito da Microsoft em 21 aulas para construir aplicações com IA generativa.
- **Áreas:** **Backend e APIs** (média) — Aprender a integrar LLMs em aplicações reais

**[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)** · ⭐ 109,2 mil · Jupyter Notebook · outra

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

**[rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)** · ⭐ 80,9 mil · Python · MIT

- **O que é:** Aprenda engenharia de IA do zero: estude, construa e publique.
- **Por que importa:** Trilha prática de engenharia de IA: aprender, construir e publicar aplicações.
- **Áreas:** **Backend e APIs** (média) — Aprender a levar funcionalidades de IA até produção
- ⚠️ Projeto recente.

**[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** · ⭐ 80,5 mil · Python

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

**[karpathy/nanochat](https://github.com/karpathy/nanochat)** · ⭐ 61 mil · Python · MIT

- **O que é:** O melhor ChatGPT que 100 dólares conseguem treinar: LLM completo de ponta a ponta.
- **Por que importa:** Implementação completa e enxuta de um ChatGPT (treino, ajuste e interface) para estudo.
- **Áreas:** **Backend e APIs** (média) — Entender o ciclo completo de um LLM de ponta a ponta

**[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · ⭐ 59 mil · Python · outra

- **O que é:** Coleção selecionada de recursos para o Claude Code: skills, agentes, status lines, ferramentas e plugins.
- **Por que importa:** Coleção selecionada de skills, agentes, hooks e plugins para o Claude Code; boa vitrine do que a comunidade usa.
- **Áreas:** **Engenharia e produtividade** (média) — Descobrir hooks, comandos e plugins para melhorar o fluxo com o Claude Code
- ⚠️ É uma lista de links, não um software.

**[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)** · ⭐ 55,4 mil · Jupyter Notebook · MIT

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

**[luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)** · ⭐ 47,7 mil · Python · MIT

- **O que é:** Guia visual e com exemplos do Claude Code, dos conceitos básicos aos agentes avançados, com templates prontos para copiar.
- **Por que importa:** Encurta a curva de aprendizado do Claude Code com exemplos práticos e templates que o time pode adotar no mesmo dia.
- **Áreas:** **Engenharia e produtividade** (alta) — Usar os templates prontos para padronizar a configuração do Claude Code no time

**[patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** · ⭐ 42,2 mil · Jupyter Notebook · MIT

- **O que é:** Tutoriais aprofundados sobre LLMs, RAG e aplicações reais de agentes de IA, com projetos completos em notebooks.
- **Por que importa:** Bom acervo de exemplos práticos de RAG, agentes e MCP para copiar padrões ao começar um projeto.
- **Áreas:** **Engenharia e produtividade** (média) — Partir de um projeto de exemplo de RAG ou agente ao prototipar uma funcionalidade
- ⚠️ São exemplos didáticos; adapte antes de usar em produção.

**[ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects)** · ⭐ 40,8 mil · Python · MIT

- **O que é:** Lista curada de casos de uso de agentes de IA por setor, com links para projetos open source de implementação.
- **Por que importa:** Serve de inspiração para mapear onde agentes podem ajudar no produto, com ponteiros para código de referência.
- ⚠️ É uma lista de links, não um software.

**[anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)** · ⭐ 39,9 mil · Jupyter Notebook

- **O que é:** Tutorial interativo da Anthropic de engenharia de prompts, em notebooks com exercícios.
- **Por que importa:** Base sólida para o time escrever prompts melhores para o Claude, com técnicas testadas e exercícios práticos.
- **Áreas:** **Engenharia e produtividade** (média) — Treinar o time em técnicas de prompt antes de construir funcionalidades com LLM
- ⚠️ Sem licença declarada no GitHub.

**[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)** · ⭐ 37,6 mil · MIT

- **O que é:** Lista curada de mais de mil skills de agentes, de times oficiais e da comunidade, compatíveis com Claude Code, Codex, Gemini CLI, Cursor e outros.
- **Por que importa:** Ponto de partida para achar skills prontas antes de escrever as suas.
- **Áreas:** **Engenharia e produtividade** (média) — Procurar skills prontas para a stack do time antes de criar uma do zero
- ⚠️ É uma lista de links; revise cada skill antes de instalar.

**[huggingface/agents-course](https://github.com/huggingface/agents-course)** · ⭐ 35,5 mil · MDX · Apache-2.0

- **O que é:** Curso gratuito do Hugging Face sobre agentes de IA, com smolagents, LangGraph e LlamaIndex.
- **Por que importa:** Caminho estruturado para o time aprender conceitos e frameworks de agentes com exercícios práticos.
- **Áreas:** **Engenharia e produtividade** (média) — Formar o time em agentes antes de escolher um framework

**[VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)** · ⭐ 26,8 mil · Shell · MIT

- **O que é:** Mais de 100 subagentes especializados para o Claude Code.

**[EthicalML/awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning)** · ⭐ 21,1 mil · MIT

- **O que é:** Lista de bibliotecas open source para publicar, monitorar e escalar ML em produção.


## Outros

**[Pythagora-io/gpt-pilot](https://github.com/Pythagora-io/gpt-pilot)** · ⭐ 33,6 mil · Python · outra

- **O que é:** GPT Pilot: agente que desenvolve aplicações passo a passo junto com o desenvolvedor.

**[QwenLM/Qwen3](https://github.com/QwenLM/Qwen3)** · ⭐ 27,8 mil · Python

- **O que é:** Qwen3: série de modelos de linguagem da Alibaba.

**[Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM)** · ⭐ 27,5 mil · CC0-1.0

- **O que é:** Lista curada de recursos sobre grandes modelos de linguagem.

**[karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero)** · ⭐ 26,1 mil · Jupyter Notebook · MIT

- **O que é:** Curso "Neural Networks: Zero to Hero", de Andrej Karpathy.
- ⚠️ Sem commits há 2 anos — verifique se ainda é mantido.

**[SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)** · ⭐ 23,9 mil · Python · MIT

- **O que é:** SuperClaude: framework de configuração que amplia o Claude Code com comandos especializados, personas e metodologias de desenvolvimento.

**[pgvector/pgvector](https://github.com/pgvector/pgvector)** · ⭐ 23,9 mil · C · outra

- **O que é:** pgvector: busca vetorial por similaridade dentro do Postgres.

**[livekit/livekit](https://github.com/livekit/livekit)** · ⭐ 22,4 mil · Go · Apache-2.0

- **O que é:** LiveKit: stack de tempo real para conectar pessoas e IA por voz e vídeo.

**[BuilderIO/gpt-crawler](https://github.com/BuilderIO/gpt-crawler)** · ⭐ 22,4 mil · TypeScript · ISC

- **O que é:** Rastreia um site e gera arquivos de conhecimento para alimentar um GPT ou um RAG.

**[anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts)** · ⭐ 21,4 mil · Python · MIT

- **O que é:** Projetos para começar rápido a construir aplicações com a API do Claude.

**[QwenLM/Qwen3-VL](https://github.com/QwenLM/Qwen3-VL)** · ⭐ 20,3 mil · Jupyter Notebook · Apache-2.0

- **O que é:** Qwen3-VL: modelos multimodais (texto e imagem) da Alibaba.

**[keploy/keploy](https://github.com/keploy/keploy)** · ⭐ 20 mil · Go · Apache-2.0

- **O que é:** Keploy: gera testes de API e integração a partir do tráfego real, com ambientes isolados.


## Demais repositórios com 20 mil+ estrelas

Os outros 1917 repositórios, fora do foco de IA, ficam em páginas por categoria técnica:

- [Frontend e UI](geral/frontend-e-ui.md) (243)
- [Backend e APIs](geral/backend-e-apis.md) (173)
- [Mobile e Desktop](geral/mobile-e-desktop.md) (244)
- [DevOps e Cloud](geral/devops-e-cloud.md) (109)
- [Dados e Bancos de dados](geral/dados-e-bancos-de-dados.md) (102)
- [Segurança](geral/seguranca.md) (67)
- [Ferramentas de desenvolvimento](geral/ferramentas-de-desenvolvimento.md) (181)
- [Linguagens e runtimes](geral/linguagens-e-runtimes.md) (44)
- [Sistemas operacionais e infraestrutura](geral/sistemas-operacionais-e-infraestrutura.md) (20)
- [Aprendizado e listas de recursos](geral/aprendizado-e-listas-de-recursos.md) (276)
- [Apps prontos e self-hosted](geral/apps-prontos-e-self-hosted.md) (115)
- [Outros](geral/outros.md) (343)
