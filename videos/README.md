# 🎬 Vídeos do canal IA para Pessoas

Série do canal [IA para Pessoas](https://www.youtube.com/@iaparapessoas): um vídeo de 3 a 5 minutos para cada repositório do foco de IA do radar, **do mais estrelado para o menos**, em linguagem simples para devs e para quem usa Claude ou outras IAs no dia a dia.

## Como funciona (um vídeo por dia, sem custo)

1. **04:17, todos os dias — roteiro (tarefa agendada do Claude):** pega o próximo repositório da fila, lê o README oficial, os dados do radar e vídeos do YouTube sobre o projeto (só como pesquisa), escreve o roteiro em `roteiros/NNN-nome.json` e dispara a renderização.
2. **~04:40 — vídeo (GitHub Actions, `video-render.yml`):** gera a narração com voz sintética grátis (edge-tts), desenha as telas, monta o vídeo 1920×1080 com legenda na tela e a capa.
3. **Postagem:** cada episódio vira um release `video-NNN` (vídeo, capa, legendas, descrição), uma issue **🎬 Vídeo #N pronto** e, com a postagem automática configurada, sobe sozinho para o YouTube agendado para as 06:00 do mesmo dia.

Para um episódio ir ao ar na hora, sem esperar as 06:00: `python3 scripts/video.py disparar --agora`, ou rode o workflow **Vídeos — renderizar** em Actions marcando *Publicar no YouTube assim que renderizar*.

`produzidos.json` guarda o que já saiu: episódio, status (`roteiro` → `pronto`), release e issue.

## Postagem automática

Depois de renderizar, o workflow envia o vídeo pela API oficial do YouTube **agendado para o horário de `postagem.horario`** (06:00) nos dias de `postagem.dias` (todos os dias): até lá ele fica privado, e você pode segurar pelo Studio se não gostar. A issue do episódio recebe o link e fecha sozinha.

Configuração única (custo zero), com a conta Google dona do canal:

1. **Google Cloud:** crie um projeto e ative a **YouTube Data API v3**.
2. **Tela de consentimento OAuth:** tipo *Externo*, adicione o seu e-mail e **publique o app ("Em produção")**. Em modo *Teste* o token expira em 7 dias.
3. **Credenciais:** crie um *ID do cliente OAuth* do tipo **Aplicativo da Web**, com o URI de redirecionamento `https://developers.google.com/oauthplayground`.
4. **Token:** em <https://developers.google.com/oauthplayground>, na engrenagem marque *Use your own OAuth credentials* e cole o ID e a chave secreta. Autorize o escopo `https://www.googleapis.com/auth/youtube.upload` com a conta do canal (no aviso de app não verificado: *Avançado → continuar*) e clique em *Exchange authorization code for tokens*. Copie o **Refresh token**.
5. **GitHub:** em *Settings → Secrets and variables → Actions*, crie `YT_CLIENT_ID`, `YT_CLIENT_SECRET` e `YT_REFRESH_TOKEN`.
6. Rode o workflow **Vídeos — renderizar** em *Actions* para postar o que já estiver pronto.

Capa personalizada exige o canal verificado por telefone (youtube.com/verify). Sem isso o vídeo sobe com a capa automática do YouTube.

## Ajustes (`config-videos.yml`)

- `canal.nome` e `canal.chamada_final`: o que aparece na abertura, no encerramento e na capa.
- `voz.nome` / `voz.velocidade`: outra voz pt-BR do edge-tts, mais rápida ou mais lenta.
- `fila`: `foco` (só IA) ou `todos`.
- `roteiro.palavras_min` / `palavras_max`: duração do vídeo.

Para refazer um episódio, mude o status dele em `produzidos.json` para `roteiro` e rode o workflow **Vídeos — renderizar** em Actions.
