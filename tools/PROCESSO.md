# Processo semanal — Instagram @aguiasdodigitalads

Conta da **Águias do Digital**: comunidade que ensina pessoas a serem afiliadas no **Google Ads**, com foco no **mercado gringo**.
Público: brasileiros iniciantes/intermediários. Idioma dos posts: português do Brasil.

## Regra principal
**Nada é publicado sem aprovação do dono da conta.** Todo post novo entra no Metricool como **rascunho** (`draft: true`).
Só depois que ele responder aprovando no chat é que os rascunhos viram agendados (`draft: false`).

## Cadência
- 14 posts por semana, de quinta a quarta.
- **12:00** → carrossel (5–6 slides, 1080x1350) ou imagem única.
- **19:00** → Reel animado (1080x1920, ~20 s, 6 cenas).
- Fuso: America/Sao_Paulo.

## Ferramentas (pasta `tools/`)
- `render.py <spec.json> <saida>` → gera slides JPEG do carrossel. Spec: `{"id": "...", "slides": ["<html>", ...]}`.
- `reel.py <spec.json> <saida>` → gera MP4 + `_capa.png`. Spec: `{"id": "...", "scenes": [{"kick","html","dur"}]}`.
- `specs/carrosseis_semana1.py` e `specs/reels_semana1.py` → modelos de como escrever os specs (helpers `cover`, `text`, `items`, `box`, `cta`, `hook`, `sc`). Copie e adapte.
- `assets/logo.png` → emblema dourado (versão sem o "G" do Google).
- Dependências: Python, Playwright (Chromium), Pillow, ffmpeg. Fontes Poppins/Inter em /usr/share/fonts.
- Rode os scripts de dentro de `tools/` (o `reel.py` importa o `render.py`).

## Identidade visual
Fundo preto (#070707), destaque laranja (#FF7A1A) com brilho, texto claro. Cabeçalho com o emblema + "Águias do Digital", rodapé "@aguiasdodigitalads", slide/cena final com o emblema grande e botão "Link na bio".

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
