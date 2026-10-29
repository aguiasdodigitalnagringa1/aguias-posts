"""Specs dos carrosséis/imagens de 05/11 a 11/11 (semana 3)."""
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
 "2026-11-05_carrossel": [
  cover("Estrutura", "Como organizar seus <span class='o'>grupos de anúncios</span>", "Um tema por grupo deixa tudo mais claro."),
  text("01 · O conceito", "Cada grupo, <span class='o'>um assunto</span>",
       "<p>O grupo de anúncios reúne palavras-chave e anúncios que falam da <b>mesma coisa</b>.</p>"
       + box("Por que importa", "Quanto mais fechado o tema, mais fácil o anúncio <b>responder à busca</b>.")),
  text("02 · Exemplo", "Separe pela <span class='o'>intenção</span>",
       items("Grupo <b>review</b>: quem quer opiniões",
             "Grupo <b>buy</b>: quem quer comprar",
             "Grupo <b>vs</b>: quem está comparando")),
  text("03 · O anúncio", "Escreva para <span class='o'>aquele grupo</span>",
       "<p>Um anúncio genérico conversa com todo mundo e convence pouca gente. Use nos títulos a <b>ideia da busca</b> do grupo.</p>"),
  text("04 · Na análise", "Dados <span class='o'>mais limpos</span>",
       "<p>Com grupos organizados, você enxerga rápido o que funciona e o que precisa de <b>ajuste</b>.</p>"),
  CTA],

 "2026-11-06_carrossel": [
  cover("Pesquisa de palavras", "Como usar o <span class='o'>Planejador de palavras-chave</span>", "A ferramenta gratuita dentro do Google Ads."),
  text("01 · O que é", "Ideias a partir de <span class='o'>buscas reais</span>",
       "<p>Você digita um termo e o Google sugere palavras relacionadas, com estimativas de <b>volume</b> e <b>concorrência</b>.</p>"),
  text("02 · Como usar", "Passo a <span class='o'>passo</span>",
       items("Escolha o <b>país</b> e o <b>idioma</b> do seu público",
             "Comece pelo <b>nome do produto</b> e do problema que ele resolve",
             "Filtre as ideias pela <b>intenção</b> da busca")),
  text("03 · Cuidado", "Estimativa não é <span class='o'>garantia</span>",
       "<p>Os números são aproximados. Use como <b>ponto de partida</b> e confirme com os dados da sua campanha.</p>"
       + box("Dica", "Volume alto nem sempre é melhor. Prefira termos <b>próximos da decisão</b>.")),
  CTA],

 "2026-11-07_carrossel": [
  cover("Antes de anunciar", "4 coisas para avaliar em uma <span class='o'>oferta</span>", "Comissão é só uma parte da história."),
  text("01 · Demanda", "As pessoas <span class='o'>procuram</span>?",
       "<p>Campanha de Pesquisa depende de busca. Veja se existe <b>interesse real</b> pelo produto ou pelo problema que ele resolve.</p>"),
  text("02 · Regras do produtor", "O que é <span class='o'>permitido</span>",
       "<p>Cada oferta tem regras próprias: uso da marca, tipos de anúncio, páginas aceitas. Leia <b>antes</b> de começar.</p>"),
  text("03 · Página de vendas", "Ela <span class='o'>convence</span>?",
       "<p>Você leva o clique até lá. Uma página clara, confiável e em bom inglês faz <b>toda a diferença</b>.</p>"),
  text("04 · Suporte e reputação", "Tem <span class='o'>quem responda</span>?",
       "<p>Produtor com suporte ativo e boa reputação dá mais <b>segurança</b> para quem anuncia.</p>"),
  CTA],

 "2026-11-08_imagem": [
  "<div class='s'><div class='mid'><div class='kick'>Lembrete de domingo</div>"
  "<h1 style='font-size:92px'>Constância vence intensidade.</h1>"
  "<h2 style='margin-top:40px'><span class='o'>Um pouco de análise todo dia vale mais que uma maratona por mês.</span></h2></div></div>"],

 "2026-11-09_carrossel": [
  cover("Página de destino", "O que sua página precisa ter para <span class='o'>passar confiança</span>", "Para o usuário e para as políticas do Google."),
  text("01 · Conteúdo útil", "Informação <span class='o'>de verdade</span>",
       "<p>A página precisa ajudar quem chegou: explicar o produto e responder dúvidas, <b>sem exageros</b>.</p>"),
  text("02 · Transparência", "Páginas <span class='o'>institucionais</span>",
       items("<b>Política de privacidade</b>",
             "<b>Termos de uso</b>",
             "<b>Contato</b> visível",
             "Aviso de que é um <b>link de afiliado</b>")),
  text("03 · Experiência", "Rápida e <span class='o'>fácil</span> de usar",
       "<p>Carregamento rápido, leitura boa no <b>celular</b> e sem pop-ups que atrapalham.</p>"),
  text("04 · Coerência", "Fala o mesmo que o <span class='o'>anúncio</span>",
       "<p>Quem clicou procurando algo precisa encontrar <b>exatamente isso</b> na página.</p>"),
  CTA],

 "2026-11-10_carrossel": [
  cover("Mercado gringo", "Configurando <span class='o'>local e idioma</span> da campanha", "Detalhes que decidem quem vê seu anúncio."),
  text("01 · Locais", "Escolha os <span class='o'>países</span>",
       "<p>Comece pelos países que a oferta aceita e onde a página de vendas <b>faz sentido</b>.</p>"),
  text("02 · Presença ou interesse", "Uma opção <span class='o'>escondida</span>",
       "<p>Nas opções de local, dá para mirar quem está <b>no local</b> ou também quem <b>demonstra interesse</b> nele. Confira qual está marcada.</p>"
       + box("Dica", "Para ofertas de um país específico, priorizar <b>presença</b> costuma ser mais seguro.")),
  text("03 · Idioma", "Fale a <span class='o'>língua</span> do público",
       "<p>Defina o idioma de acordo com o público e escreva anúncio e palavras-chave <b>nesse idioma</b>.</p>"),
  text("04 · Revise", "Antes de <span class='o'>publicar</span>",
       "<p>Um país errado ou um idioma esquecido pode levar a verba para quem <b>nunca vai comprar</b>.</p>"),
  CTA],

 "2026-11-11_carrossel": [
  cover("Otimização", "Como fazer <span class='o'>teste A/B</span> de anúncios", "Descubra com dados o que funciona melhor."),
  text("01 · A ideia", "Comparar <span class='o'>versões</span>",
       "<p>Você roda variações do anúncio e deixa os números mostrarem qual <b>performa melhor</b>.</p>"),
  text("02 · A regra", "Mude <span class='o'>uma coisa</span> por vez",
       items("Um <b>título</b> com outro ângulo",
             "Uma <b>chamada para ação</b> diferente",
             "Um <b>benefício</b> em destaque")),
  text("03 · Paciência", "Dê tempo ao <span class='o'>teste</span>",
       "<p>Decidir com poucos cliques é chute. Espere juntar dados suficientes antes de <b>escolher o vencedor</b>.</p>"),
  text("04 · Repita", "Teste é <span class='o'>rotina</span>",
       "<p>O vencedor de hoje vira a base do próximo teste. É assim que o anúncio <b>evolui</b>.</p>"),
  CTA],
}

for sid, slides in SPECS.items():
    (D / f"{sid}.json").write_text(json.dumps({"id": sid, "slides": slides}, ensure_ascii=False, indent=1))
    print(sid, len(slides))
