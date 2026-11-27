# 🎬 Vídeos do canal IA para Pessoas

Série do canal [IA para Pessoas](https://www.youtube.com/@iaparapessoas): um vídeo de 3 a 5 minutos para cada repositório do foco de IA do radar, **do mais estrelado para o menos**, em linguagem simples para devs e para quem usa Claude ou outras IAs no dia a dia.

## Como funciona (todo dia, sem custo)

1. **08:41 — roteiro (tarefa agendada do Claude):** pega o próximo repositório da fila, lê o README oficial, os dados do radar e vídeos do YouTube sobre o projeto (só como pesquisa), escreve o roteiro em `roteiros/NNN-nome.json` e dispara a renderização.
2. **~08:50 — vídeo (GitHub Actions, `video-render.yml`):** gera a narração com voz sintética grátis (edge-tts), desenha as telas, monta o vídeo 1920×1080 com legenda na tela e a capa.
3. **Pronto para postar:** cada episódio vira um release `video-NNN` (vídeo, capa, legendas, descrição) e uma issue **🎬 Vídeo #N pronto** com o passo a passo e o título, a descrição e as tags para copiar.

`produzidos.json` guarda o que já saiu: episódio, status (`roteiro` → `pronto`), release e issue.

## Por que a postagem não é automática

Vídeo enviado pela API do YouTube por um projeto que não passou pela auditoria do Google fica travado como **privado**, sem como tornar público. Por isso o último passo é seu, pelo app YouTube Studio (uns 2 minutos). Se um dia o projeto for auditado, dá para acrescentar o envio automático no mesmo workflow.

## Ajustes (`config-videos.yml`)

- `canal.nome` e `canal.chamada_final`: o que aparece na abertura, no encerramento e na capa.
- `voz.nome` / `voz.velocidade`: outra voz pt-BR do edge-tts, mais rápida ou mais lenta.
- `fila`: `foco` (só IA) ou `todos`.
- `roteiro.palavras_min` / `palavras_max`: duração do vídeo.

Para refazer um episódio, mude o status dele em `produzidos.json` para `roteiro` e rode o workflow **Vídeos — renderizar** em Actions.
