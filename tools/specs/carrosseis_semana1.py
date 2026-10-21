"""Specs dos carrosséis/imagens de 23 a 28/10 (semana 1)."""
import json, pathlib

D = pathlib.Path(__file__).parent


def cover(kick, title, sub):
    return f"<div class='s cover'><div class='mid'><div class='kick'>{kick}</div><h1>{title}</h1><p style='margin-top:44px'>{sub}</p></div></div>"


def text(kick, h2, body):
    return f"<div class='s'><div class='mid'><div class='kick'>{kick}</div><h2>{h2}</h2>{body}</div></div>"


def items(*rows):
    inner = "".join(f"<div class='it'><div class='n'>{i}</div><div>{r}</div></div>" for i, r in enumerate(rows, 1))
    return f"<div class='list'>{inner}</div>"


def box(lbl, txt):
    return f"<div class='box'><div class='lbl'>{lbl}</div>{txt}</div>"


def cta(title, body):
    return ("<div class='s center'><div class='mid' style='display:flex;flex-direction:column;align-items:center'>"
            f"<img class='biglogo' src='{{{{LOGO}}}}'><h2 style='margin-bottom:24px'>{title}</h2><p>{body}</p>"
            "<div class='cta'>Link na bio</div>"
            "<p style='margin-top:40px;font-size:32px;color:#9A9A9A'>Salva este post para consultar depois</p></div></div>")


CTA = cta("Quer aprender o <span class='o'>passo a passo</span>?",
          "Na comunidade <b>Águias do Digital</b> você aprende com quem roda campanhas todos os dias.")

SPECS = {
 "2026-10-23_carrossel": [
  cover("Comparativo", "Google Ads <span class='o'>x</span> Meta Ads para afiliados", "Qual a diferença na prática?"),
  text("01 · Google Ads", "A pessoa <span class='o'>vem até você</span>",
       "<p>No Google, o anúncio aparece quando alguém <b>pesquisa</b> pelo assunto. Ela já tem interesse e está procurando uma solução.</p>"
       + box("Ponto forte", "Público com <b>intenção</b>: quem pesquisa já está perto de decidir.")),
  text("02 · Meta Ads", "Você <span class='o'>interrompe</span> a pessoa",
       "<p>No Facebook e no Instagram, o anúncio aparece no meio do feed, para quem estava vendo outra coisa.</p>"
       + box("Ponto forte", "Alcance grande e criativo visual. Mas é preciso <b>despertar</b> o interesse do zero.")),
  text("03 · O que muda", "O <span class='o'>centro</span> de cada campanha",
       items("<b>Google:</b> as palavras-chave que o público digita",
             "<b>Meta:</b> o criativo (vídeo ou imagem) que para o scroll",
             "<b>Google:</b> anúncio em texto, direto ao ponto",
             "<b>Meta:</b> público definido por interesses e comportamento")),
  text("04 · Nossa escolha", "Por que focamos no <span class='o'>Google</span>",
       "<p>Para o afiliado iniciante, anunciar para quem <b>já está procurando</b> o produto costuma ser um caminho mais direto para aprender com os dados.</p>"
       "<p style='margin-top:30px'>Não existe plataforma mágica: existe <b>método</b> bem aplicado.</p>"),
  CTA],

 "2026-10-24_carrossel": [
  cover("Glossário do afiliado", "As <span class='o'>siglas</span> que você precisa dominar", "CPC, CTR, CPA e ROI sem complicação."),
  text("01 · CPC", "Custo por <span class='o'>clique</span>",
       "<p>Quanto você paga, em média, cada vez que alguém clica no seu anúncio.</p>"
       + box("Exemplo", "Gastou <b>R$ 100</b> e teve <b>50 cliques</b>: CPC de <b>R$ 2</b>.")),
  text("02 · CTR", "Taxa de <span class='o'>cliques</span>",
       "<p>De cada 100 pessoas que viram o anúncio, quantas clicaram. Mostra se o anúncio chama atenção.</p>"
       + box("Exemplo", "<b>1.000</b> visualizações e <b>50</b> cliques: CTR de <b>5%</b>.")),
  text("03 · CPA", "Custo por <span class='o'>aquisição</span>",
       "<p>Quanto custou, em anúncios, para gerar <b>uma venda</b>.</p>"
       + box("Exemplo", "Gastou <b>R$ 300</b> e fez <b>3 vendas</b>: CPA de <b>R$ 100</b>.")),
  text("04 · ROI", "Retorno sobre o <span class='o'>investimento</span>",
       "<p>Mostra se a campanha deu lucro ou prejuízo em relação ao que foi investido.</p>"
       + box("A conta", "<b>(Comissões − Investimento) ÷ Investimento</b><br>Se o resultado é negativo, a campanha precisa de ajuste.")),
  CTA],

 "2026-10-25_imagem": [
  "<div class='s'><div class='mid'><div class='kick'>Lembrete de domingo</div>"
  "<h1 style='font-size:92px'>Campanha boa não nasce pronta.</h1>"
  "<h2 style='margin-top:40px'><span class='o'>Ela nasce do teste, do ajuste e de quem não desiste no terceiro dia.</span></h2></div></div>"],

 "2026-10-26_carrossel": [
  cover("Google Ads na prática", "Como funciona uma <span class='o'>campanha de Pesquisa</span>", "A estrutura, camada por camada."),
  text("01 · Campanha", "A <span class='o'>base</span> de tudo",
       "<p>Aqui você define o <b>orçamento diário</b>, o <b>país</b>, o <b>idioma</b> e a <b>estratégia de lance</b>.</p>"
       + box("Dica", "Comece com um orçamento que você aceita usar como <b>custo de teste</b>.")),
  text("02 · Grupo de anúncios", "Um <span class='o'>tema</span> por grupo",
       "<p>Cada grupo reúne palavras-chave parecidas e os anúncios que falam delas.</p>"
       + box("Exemplo", "Um grupo para buscas de <b>“[produto] funciona”</b>, outro para <b>“[produto] onde comprar”</b>.")),
  text("03 · Palavras-chave", "O que a pessoa <span class='o'>digita</span>",
       "<p>São os termos que ativam o seu anúncio. Use também as <b>palavras-chave negativas</b> para bloquear buscas que não trazem venda.</p>"),
  text("04 · Anúncio e página", "O que a pessoa <span class='o'>vê</span>",
       items("<b>Títulos e descrições</b> que respondem à busca",
             "<b>Página de destino</b> alinhada com o que foi prometido no anúncio",
             "<b>Conversão rastreada</b>, para saber o que vende")),
  CTA],

 "2026-10-27_carrossel": [
  cover("Salva antes de começar", "<span class='o'>Checklist</span> da sua 1ª campanha", "6 pontos para conferir antes de clicar em publicar."),
  text("Parte 1", "Antes de <span class='o'>anunciar</span>",
       items("<b>Leia as regras do produtor.</b> Alguns não permitem anunciar no Google ou usar o nome da marca.",
             "<b>Conta do Google Ads</b> configurada: faturamento, fuso horário e moeda.",
             "<b>Rastreamento de conversão</b> funcionando e testado.")),
  text("Parte 2", "Na hora de <span class='o'>montar</span>",
       items("<b>Palavras-chave</b> definidas, com a lista de <b>negativas</b>.",
             "<b>Anúncio</b> dentro das políticas do Google, sem promessas exageradas.",
             "<b>Orçamento diário</b> definido, que você aceita usar como teste.")),
  text("Bônus", "Depois de <span class='o'>publicar</span>",
       "<p>Não mexa na campanha a cada hora. Dê tempo para juntar <b>dados</b> e tome decisões com base nos números, não na ansiedade.</p>"),
  CTA],

 "2026-10-28_carrossel": [
  cover("Mercado gringo", "Plataformas de <span class='o'>afiliados</span> para vender lá fora", "Três nomes que você vai ouvir muito."),
  text("01 · ClickBank", "Uma das <span class='o'>mais antigas</span>",
       "<p>Marketplace com milhares de produtos de vários nichos, muito conhecido por quem começa no mercado internacional.</p>"),
  text("02 · Digistore24", "Forte na <span class='o'>Europa e nos EUA</span>",
       "<p>Plataforma de origem alemã, com produtos digitais e físicos e público em vários países.</p>"),
  text("03 · BuyGoods", "Foco em <span class='o'>produtos físicos</span>",
       "<p>Muito usada para ofertas de produtos físicos, como suplementos.</p>"
       + box("Atenção", "Cada plataforma e cada produtor têm <b>regras próprias</b> de aprovação e de tráfego. Leia antes de anunciar.")),
  CTA],
}

for sid, slides in SPECS.items():
    (D / f"{sid}.json").write_text(json.dumps({"id": sid, "slides": slides}, ensure_ascii=False, indent=1))
    print(sid, len(slides))
