"""Specs dos carrosséis/imagens de 12/11 a 18/11 (semana 4)."""
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
 "2026-11-12_carrossel": [
  cover("Anúncio de Pesquisa", "<span class='o'>Recursos</span> que deixam seu anúncio mais completo", "Informações extras além de títulos e descrições."),
  text("01 · O que são", "Mais <span class='o'>informação</span> no mesmo anúncio",
       "<p>São complementos que podem aparecer junto do anúncio: links, destaques e detalhes da oferta.</p>"
       + box("Importante", "O Google decide <b>quando</b> exibir. Adicionar não garante que eles sempre apareçam.")),
  text("02 · Os mais usados", "Três para <span class='o'>começar</span>",
       items("<b>Sitelinks</b>: links para outras partes da página",
             "<b>Frases de destaque</b>: pontos fortes em poucas palavras",
             "<b>Snippets estruturados</b>: listas de itens ou tipos")),
  text("03 · Como usar", "Complementar, <span class='o'>não repetir</span>",
       "<p>Use o recurso para dizer o que <b>não coube</b> no anúncio. Repetir o título só ocupa espaço.</p>"),
  text("04 · Cuidado", "Só o que está <span class='o'>na página</span>",
       "<p>Cada destaque precisa bater com o que a pessoa encontra depois do clique. <b>Coerência</b> vale aqui também.</p>"),
  CTA],

 "2026-11-13_carrossel": [
  cover("Pesquisa de mercado", "Como ver os anúncios da <span class='o'>concorrência</span>", "Uma ferramenta pública do próprio Google."),
  text("01 · A ferramenta", "Central de <span class='o'>Transparência de Anúncios</span>",
       "<p>O Google permite consultar anúncios de anunciantes verificados. Você busca pelo <b>nome do anunciante</b> ou pelo <b>site</b>.</p>"),
  text("02 · O que observar", "Repare nos <span class='o'>padrões</span>",
       items("Quais <b>ângulos</b> se repetem nos títulos",
             "Quais <b>benefícios</b> ganham destaque",
             "Em quais <b>países</b> os anúncios aparecem")),
  text("03 · Como usar", "Inspiração, <span class='o'>não cópia</span>",
       "<p>Entenda a ideia e escreva com as suas palavras, sempre dentro das <b>regras da oferta</b>.</p>"),
  text("04 · O limite", "Ver não é <span class='o'>saber</span>",
       "<p>A ferramenta mostra o anúncio, não o resultado. Estar no ar não prova que funciona. Quem responde são os <b>seus dados</b>.</p>"),
  CTA],

 "2026-11-14_carrossel": [
  cover("Números", "Quanto você pode pagar por uma <span class='o'>venda</span>?", "Calcule seu CPA máximo antes de anunciar."),
  text("01 · O conceito", "O <span class='o'>limite</span> da conta",
       "<p>O CPA máximo é quanto uma venda pode custar em anúncios <b>sem dar prejuízo</b>. A base do cálculo é a comissão.</p>"),
  text("02 · Exemplo fictício", "Faça a <span class='o'>conta</span>",
       items("Comissão de <b>US$ 40</b>",
             "CPA acima de <b>US$ 40</b>: prejuízo",
             "CPA abaixo disso: sobra margem")
       + box("Não esqueça", "<b>Câmbio e taxas</b> também entram na conta.")),
  text("03 · Do CPA ao CPC", "Quanto cabe em <span class='o'>cada clique</span>",
       "<p>Se <b>1 em cada 50 cliques</b> vira venda, com aquela comissão o CPC precisa ficar abaixo de <b>US$ 0,80</b> para empatar.</p>"
       + box("Atenção", "Números ilustrativos. Use os <b>da sua oferta</b>.")),
  text("04 · Na prática", "Um critério para <span class='o'>decidir</span>",
       "<p>Com o limite definido, você deixa de analisar no achismo e sabe <b>quando ajustar</b> a campanha.</p>"),
  CTA],

 "2026-11-15_imagem": [
  "<div class='s'><div class='mid'><div class='kick'>Lembrete de domingo</div>"
  "<h1 style='font-size:92px'>Resultado ruim também é informação.</h1>"
  "<h2 style='margin-top:40px'><span class='o'>O erro é não anotar o que ele ensinou.</span></h2></div></div>"],

 "2026-11-16_carrossel": [
  cover("Organização", "Diário de campanha: o que <span class='o'>anotar</span>", "Sua memória não é um bom relatório."),
  text("01 · Por quê", "Para saber <span class='o'>o que mudou</span>",
       "<p>Sem registro, você vê o resultado mudar e não descobre o <b>motivo</b>.</p>"),
  text("02 · O que anotar", "Uma linha por <span class='o'>mudança</span>",
       items("A <b>data</b>",
             "<b>O que</b> foi alterado",
             "<b>Por que</b> você alterou",
             "<b>O que aconteceu</b> depois")),
  text("03 · No Google Ads", "Use o <span class='o'>histórico de alterações</span>",
       "<p>A própria conta registra as edições. Ele mostra o que mudou, mas o <b>motivo</b> quem anota é você.</p>"),
  text("04 · Rotina", "O simples <span class='o'>dura mais</span>",
       "<p>Planilha ou caderno, tanto faz. O que importa é manter o hábito e <b>consultar</b> antes da próxima mudança.</p>"),
  CTA],

 "2026-11-17_carrossel": [
  cover("Mercado gringo", "Anúncio em inglês: <span class='o'>4 cuidados</span>", "Escrever para fora é mais que traduzir."),
  text("01 · Tradução", "Fuja do <span class='o'>literal</span>",
       "<p>Frase traduzida palavra por palavra soa estranha. Prefira o jeito que o público escreve em <b>buscas e reviews</b>.</p>"),
  text("02 · Detalhes locais", "Ajuste ao <span class='o'>país</span>",
       items("<b>Moeda</b> do público da campanha",
             "<b>Medidas</b>: pounds, feet, inches",
             "<b>Grafia</b>: color (EUA) x colour (Reino Unido)")),
  text("03 · Tom", "Direto e <span class='o'>sem exagero</span>",
       "<p>Frases curtas e claras. Exagero afasta o público e pode esbarrar nas <b>políticas</b>.</p>"
       + box("Em vez de", "“Best miracle solution!!!”, teste <b>“See how it works”</b>.")),
  text("04 · Revisão", "Confira <span class='o'>antes de publicar</span>",
       "<p>Erro de ortografia passa desconfiança. Use um corretor e, se puder, peça para <b>alguém fluente</b> ler.</p>"),
  CTA],

 "2026-11-18_carrossel": [
  cover("Análise", "Não olhe só o <span class='o'>total</span> da campanha", "Os detalhes aparecem quando você segmenta."),
  text("01 · O problema", "A média <span class='o'>esconde</span>",
       "<p>No total, tudo parece igual. Separando os dados, você vê o que vai bem e o que <b>puxa para baixo</b>.</p>"),
  text("02 · Onde olhar", "Quatro <span class='o'>recortes</span>",
       items("<b>Dispositivo</b>: celular, computador, tablet",
             "<b>Horário</b> e dia da semana",
             "<b>Local</b>: país ou região",
             "<b>Palavra-chave</b>: quais trazem resultado")),
  text("03 · Como decidir", "Com dados <span class='o'>suficientes</span>",
       "<p>Poucos cliques em um recorte não provam nada. Espere ter <b>volume</b> antes de ajustar.</p>"),
  text("04 · Exemplo", "Uma pergunta <span class='o'>por vez</span>",
       "<p>O celular converte diferente? Antes de mexer no lance, <b>abra a página no celular</b> e veja como ela aparece.</p>"),
  CTA],
}

for sid, slides in SPECS.items():
    (D / f"{sid}.json").write_text(json.dumps({"id": sid, "slides": slides}, ensure_ascii=False, indent=1))
    print(sid, len(slides))
