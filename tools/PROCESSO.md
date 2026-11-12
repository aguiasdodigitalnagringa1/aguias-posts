# Processo semanal — Instagram @aguiasdodigitalads

Conta da **Águias do Digital**: comunidade que ensina pessoas a serem afiliadas no **Google Ads**, com foco no **mercado gringo**.
Público: brasileiros iniciantes/intermediários. Idioma dos posts: português do Brasil.

## Regra principal
**Nada é publicado sem aprovação do dono da conta.** Todo post novo entra no Metricool como **rascunho** (`draft: true`).
Só depois que ele responder aprovando no chat é que os rascunhos viram agendados (`draft: false`).

## Cadência
- 14 posts por semana, de quinta a quarta.
- **12:00** → carrossel (5–6 slides, 1080x1350) ou imagem única.
- **19:00** → Reel (1080x1920, ~20 s).
- Fuso: America/Sao_Paulo.

## Grade de séries (padrão desde a semana de 19/11/2026)
O dono pediu para variar os modelos e profissionalizar o perfil: **cada dia tem uma série fixa**, com layout próprio (ver `tools/modelos.py`).

| Dia | 12:00 (carrossel/imagem) | 19:00 (Reel) |
|---|---|---|
| Qui | A · Tutorial com tela | G · Reel com tela de celular |
| Sex | E · Mito x Verdade | H · Reel em lista (claro) |
| Sáb | C · Métrica da semana | **R · Reel com rosto** (fallback: G) |
| Dom | F · Frase de domingo (imagem única) | H · Reel em lista (claro) |
| Seg | D · Checklist (claro) | G · Reel com tela de celular |
| Ter | B · Errado x Certo | **R · Reel com rosto** (fallback: H) |
| Qua | A · Tutorial com tela | G · Reel com tela de celular |

- Ilustrações de tela (anúncio, tabela, painel) são **genéricas**: sem marca real, sem dados reais, sempre com "ilustração" ou "valores fictícios".
- Temas escolhidos de acordo com a série (ex.: Métrica → CTR, CPA, parcela de impressões; Errado x Certo → escolhas de configuração).

### Reels com rosto (R)
O dono grava 2 vídeos por semana (sáb e ter). Fluxo:
1. Na produção semanal, escreva **2 roteiros** (30–45 s): gancho (até 3 s), 3 pontos curtos, CTA "link na bio". Inclua o texto de tela sugerido.
2. Crie os rascunhos desses horários com o Reel gráfico de fallback (G/H) e mande os roteiros junto com o pedido de aprovação.
3. Quando o dono mandar o vídeo (no chat ou na pasta `entrada/` do repositório), gere a capa no padrão da série, salve em `posts/AAAA-MM-DD/`, dê push e troque a mídia do rascunho (updateScheduledPost, mantendo o resto do post).

## Ferramentas (pasta `tools/`)
- `render.py <spec.json> <saida>` → gera slides JPEG do carrossel. Spec: `{"id": "...", "slides": ["<html>", ...]}`.
- `reel.py <spec.json> <saida>` → gera MP4 + `_capa.png`. Spec: `{"id": "...", "scenes": [{"kick","html","dur"}]}`.
- **`modelos.py` + `specs/exemplos_modelos.py`** → modelos atuais (séries A–H). Cada função gera um slide/cena completo; specs com `"raw": true`. Comece copiando `exemplos_modelos.py`.
- `specs/carrosseis_semana1..4.py` e `specs/reels_semana1..4.py` → modelo antigo (único layout), só como referência de textos.
- `assets/logo.png` → emblema dourado (versão sem o "G" do Google).
- Dependências: Python, Playwright (Chromium), Pillow, ffmpeg. Fontes Poppins/Inter em /usr/share/fonts.
- Rode os scripts de dentro de `tools/` (o `reel.py` importa o `render.py`).

## Identidade visual
Fundo preto (#070707), destaque laranja (#FF7A1A) com brilho, texto claro. Cabeçalho com o emblema + "Águias do Digital" e o nome da série com a numeração (ex.: "TUTORIAL · 02/05"), rodapé "@aguiasdodigitalads", slide/cena final com o emblema grande e botão "Link na bio".
Séries Checklist (D) e Reel em lista (H) usam a variação clara: fundo creme (#F5F0E8), texto preto, laranja escuro (#D9620B) e títulos serifados (Lora).

## Publicação
1. Salvar mídias em `posts/AAAA-MM-DD/` neste repositório e dar push (o repositório é público; o Metricool baixa pelo link `https://raw.githubusercontent.com/aguiasdodigitalnagringa1/aguias-posts/main/posts/...`).
2. Metricool (conector): marca **Aguiasads**, `blogId` **7571936**, rede `instagram`.
   - Carrossel/imagem: `instagramData.type = "POST"`.
   - Reel: `instagramData.type = "REEL"`, `showReelOnFeed: true`, `videoThumbnailUrl` = capa.
   - Sempre `isAiGenerated: true`.
   - Música dos Reels: **instrumental** do catálogo do Instagram, via `audioConfiguration.audioId` (busque por termo; se vier lista de candidatos, escolha IDs numéricos e varie entre os Reels).
3. Criar tudo como **rascunho** e pedir aprovação.

## Regras de conteúdo
- **Nunca** prometer ganhos, renda ou resultado garantido. Tratar como negócio que exige método, verba de teste e disciplina.
- **Não falar de campanhas Display** (a comunidade não usa). Foco em campanhas de **Pesquisa** no Google.
- Não inventar detalhes da comunidade (preço, aulas, bônus, módulos). Descrever só: comunidade para aprender a ser afiliado no Google Ads, foco no mercado gringo, aprender com quem roda campanhas todos os dias.
- Informações sobre plataformas e políticas: em termos gerais, sem números que possam ficar desatualizados.
- Legenda: gancho na 1ª linha, 3–5 linhas de valor, CTA ("Link na bio" / "Salva"), 5 hashtags.
- Não repetir temas já publicados (ver histórico abaixo).

## Histórico de temas
### Semana 22–28/10/2026
- Carrosséis/imagem: O que é ser afiliado no Google Ads · Google Ads x Meta Ads · Glossário CPC/CTR/CPA/ROI · Frase de domingo (campanha boa nasce do teste) · Estrutura da campanha de Pesquisa · Checklist da 1ª campanha · Plataformas gringas (ClickBank, Digistore24, BuyGoods)
- Reels: Por que brasileiros vendem para fora · Precisa falar inglês? · Erro nº 1 (escolher pela comissão) · Prazer, Águias do Digital · Por que focamos em Pesquisa · Mito: precisa de muito dinheiro? · Página de pré-venda

### Semana 29/10–04/11/2026
- Carrosséis/imagem: Tipos de correspondência (ampla, frase, exata) · Palavras-chave negativas · Anatomia do anúncio de Pesquisa · Frase de domingo (os números não têm ansiedade) · Relatório de termos de pesquisa · Índice de Qualidade · Buscas em inglês por intenção (curiosidade, comparação, decisão)
- Reels: Rastreamento de conversão · 3 sinais de que a campanha precisa de ajuste · Escalar orçamento aos poucos · Rotina diária de quem roda campanhas · Fuso horário e programação de anúncios · Por que anúncios são reprovados · Maximizar cliques x Maximizar conversões
- Músicas usadas (audioId): Stardust (Instrumental) 1540755600953104 · Motive (Instrumental) 1579921342191993 · Hypnotized (Instrumental) 1852688158814799 · You Can Do It Too (Instrumental) 973266493758189 · Maya Maya (Instrumental) 823145229909724 · Be Happy (Instrumental) 761736589642441 · Carnaval (Instrumental) 897193789954241
- Specs: `specs/carrosseis_semana2.py` e `specs/reels_semana2.py`. Obs.: renderizar os 7 Reels de uma vez passa de 10 min; rode em 2 lotes.

### Semana 05–11/11/2026
- Carrosséis/imagem: Como organizar grupos de anúncios · Planejador de palavras-chave · 4 coisas para avaliar em uma oferta · Frase de domingo (constância vence intensidade) · O que a página de destino precisa ter para passar confiança · Local e idioma da campanha (presença x interesse) · Teste A/B de anúncios
- Reels: Como o Google gasta o orçamento diário · Verificação de anunciante · Erro: mexer na campanha todo dia · Afiliado x produtor: quem faz o quê · O caminho do clique à comissão · Por que o CPC muda tanto · 3 perguntas antes de pausar uma campanha
- Músicas usadas (audioId): Spontaneous (Instrumental) 235065218897660 · Bulletproof (Instrumental) 844709300522860 · Someday (Instrumental) 976299230340697 · Todo Bien (Instrumental) 998330555713118 · Sheesh (Instrumental) 1969553887185917 · Donde Tu Like It (Instrumental) 592285976921117 · Zara Si Hansi (Instrumental) 619234943566409
- Specs: `specs/carrosseis_semana3.py` e `specs/reels_semana3.py`. Obs.: busca útil de músicas no conector: audioId "(Instrumental) Version" devolve lista de candidatos instrumentais.

### Semana 12–18/11/2026
- Carrosséis/imagem: Recursos de anúncio (sitelinks, frases de destaque, snippets) · Central de Transparência de Anúncios (ver anúncios da concorrência) · Calcular CPA máximo · Frase de domingo (resultado ruim também é informação) · Diário de campanha e histórico de alterações · Anúncio em inglês: 4 cuidados · Segmentar os dados (não olhar só o total)
- Reels: Anunciar com o nome do produto (regras da oferta) · Muitas impressões e poucos cliques · Muitos cliques e nenhuma venda · Reembolso e comissão · Black Friday no mercado gringo · Parcela de impressões · Atraso de conversão (clique antigo)
- Músicas usadas (audioId): In My Life (Instrumental) 843481004054430 · Adore You (Instrumental) 4487975741418395 · Till The End (Instrumental) 595594926697501 · I Wish You Saw That (Instrumental) 263227909387827 · Colors (Instrumental) 667025948686455 · Beautiful, You Are (Instrumental) 526825256283644 · Peaceful Piano 2477944699150252
- Specs: `specs/carrosseis_semana4.py` e `specs/reels_semana4.py`. Obs.: rodar os 7 Reels com `xargs -P 4` em segundo plano termina em poucos minutos. Outras buscas úteis de música: "Instrumental Mix", "Love (Instrumental)", "Sunset Instrumental" (a resposta de erro traz os candidatos e nada é criado).

### Semana 19–25/11/2026 (1ª semana na grade de séries)
- 12:00: Qui A Colunas personalizadas do painel · Sex E Mitos da primeira campanha · Sáb C Taxa de conversão · Dom F Frase (errar barato e aprender rápido) · Seg D Revisão semanal da campanha · Ter B Configuração da campanha (verba, lance, rede) · Qua A Fixar títulos no anúncio responsivo
- 19:00: Qui G Força do anúncio · Sex H 3 hábitos para não estourar a verba de teste · Sáb R Por que copiar a campanha de alguém não basta (fallback G) · Dom H Painel da plataforma: 3 coisas para checar · Seg G Custo por conversão subiu: onde olhar · Ter R Os primeiros 7 dias de uma campanha nova (fallback H) · Qua G Informações do leilão
- Músicas usadas (audioId): Easy Going (Instrumental) 603168641184147 · Me Gusta (Instrumental) 302055452405923 · Piano Sketch #4 223045325575779 · Iro (Lies) (Instrumental) 4035197266698346 · Lofi Return 912937830269606 · Lullaby (Brent Bourgeois) 251099062087011 · Séquoia (Yann Falquet) 510358037368479
- Specs: `specs/semana5.py` (um arquivo para carrosséis e Reels). Obs.: `modelos.py` corrigido — texto secundário dos Reels claros (H) estava quase invisível. Outras buscas úteis de música: "Instrumental Version", "Chill (Instrumental)", "Dream (Instrumental)", "Summer (Instrumental)".
