"""Specs dos carrosséis/imagens de 29/10 a 04/11 (semana 2)."""
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
 "2026-10-29_carrossel": [
  cover("Palavras-chave", "Ampla, frase ou <span class='o'>exata</span>?", "Os 3 tipos de correspondência sem complicação."),
  text("01 · Ampla", "O Google <span class='o'>interpreta</span>",
       "<p>Seu anúncio pode aparecer para buscas <b>relacionadas</b> ao termo, mesmo sem as mesmas palavras.</p>"
       + box("Cuidado", "Alcance maior, mas exige atenção redobrada às <b>palavras-chave negativas</b>.")),
  text("02 · Frase", "O <span class='o'>sentido</span> precisa estar lá",
       "<p>Aparece para buscas que incluem o <b>significado</b> do termo, com palavras antes ou depois.</p>"
       + box("Como escrever", "Entre aspas: <b>\"[produto] review\"</b>")),
  text("03 · Exata", "A busca <span class='o'>mais próxima</span>",
       "<p>Aparece para buscas com o mesmo significado do termo. Menos alcance, mais <b>controle</b>.</p>"
       + box("Como escrever", "Entre colchetes: <b>[[produto] review]</b>")),
  text("04 · Na prática", "Qual <span class='o'>usar</span>?",
       "<p>Não existe resposta única. O que decide é o <b>teste</b> e a leitura dos <b>termos de pesquisa</b> que realmente ativaram seus anúncios.</p>"),
  CTA],

 "2026-10-30_carrossel": [
  cover("Economize verba", "Palavras-chave <span class='o'>negativas</span>", "Como bloquear as buscas que não vendem."),
  text("01 · O que são", "Termos que você <span class='o'>exclui</span>",
       "<p>Quando a busca contém uma palavra negativa, o seu anúncio <b>não aparece</b>.</p>"
       + box("Por que importa", "Cada clique de quem não vai comprar é <b>verba gasta à toa</b>.")),
  text("02 · Exemplos comuns", "Buscas que <span class='o'>raramente</span> compram",
       items("<b>free</b>, <b>download</b>, <b>pdf</b>: quem quer de graça",
             "<b>scam</b>, <b>complaints</b>: quem procura problemas",
             "<b>side effects</b>, <b>ingredients</b>: avalie caso a caso",
             "Termos de <b>outros países</b> ou outros produtos")),
  text("03 · Onde achar", "O relatório de <span class='o'>termos de pesquisa</span>",
       "<p>Ele mostra o que as pessoas <b>digitaram de verdade</b> antes de clicar. É de lá que sai a sua lista.</p>"),
  text("04 · A rotina", "Lista <span class='o'>viva</span>",
       "<p>Negativas não se fazem uma vez só. Revise com frequência e vá refinando conforme a campanha junta <b>dados</b>.</p>"),
  CTA],

 "2026-10-31_carrossel": [
  cover("Anúncio de Pesquisa", "A <span class='o'>anatomia</span> de um anúncio que recebe cliques", "O que aparece para quem pesquisa."),
  text("01 · Títulos", "A primeira <span class='o'>impressão</span>",
       "<p>Textos curtos que o Google combina entre si. Repita a ideia da busca e mostre o <b>benefício</b>.</p>"
       + box("Dica", "Escreva variações diferentes: o Google testa as combinações para você.")),
  text("02 · Descrições", "O <span class='o'>complemento</span>",
       "<p>Espaço para explicar melhor, responder dúvidas e chamar para a ação, sem promessas exageradas.</p>"),
  text("03 · URL e recursos", "Mais <span class='o'>espaço</span> na tela",
       items("<b>Caminho de exibição</b> que reforça o tema",
             "<b>Sitelinks</b> para outras seções da página",
             "<b>Frases de destaque</b> com diferenciais")),
  text("04 · A regra de ouro", "Anúncio e página <span class='o'>falam igual</span>",
       "<p>O que o anúncio promete, a página de destino precisa entregar. Coerência ajuda o usuário e a <b>qualidade</b> da campanha.</p>"),
  CTA],

 "2026-11-01_imagem": [
  "<div class='s'><div class='mid'><div class='kick'>Lembrete de domingo</div>"
  "<h1 style='font-size:92px'>Os números não têm ansiedade.</h1>"
  "<h2 style='margin-top:40px'><span class='o'>Antes de mexer na campanha, deixe os dados falarem.</span></h2></div></div>"],

 "2026-11-02_carrossel": [
  cover("Otimização", "Como ler o relatório de <span class='o'>termos de pesquisa</span>", "O relatório mais revelador da sua campanha."),
  text("01 · O que é", "O que a pessoa <span class='o'>digitou</span>",
       "<p>Palavra-chave é o que <b>você escolhe</b>. Termo de pesquisa é o que o usuário <b>realmente buscou</b> antes de ver o anúncio.</p>"),
  text("02 · O que procurar", "Três <span class='o'>perguntas</span>",
       items("Esse termo tem a ver com o <b>produto</b>?",
             "A pessoa parece querer <b>comprar</b> ou só pesquisar?",
             "Esse termo trouxe <b>conversão</b> ou só custo?")),
  text("03 · O que fazer", "Decida <span class='o'>termo a termo</span>",
       items("<b>Bom e convertendo:</b> vire palavra-chave",
             "<b>Irrelevante:</b> vire negativa",
             "<b>Na dúvida:</b> espere mais dados")),
  text("04 · Frequência", "Crie o <span class='o'>hábito</span>",
       "<p>Separar um momento fixo para olhar esse relatório é uma das rotinas mais valiosas de quem roda campanhas de Pesquisa.</p>"),
  CTA],

 "2026-11-03_carrossel": [
  cover("Google Ads", "O que é o <span class='o'>Índice de Qualidade</span>?", "Os 3 pilares que o Google avalia."),
  text("01 · O conceito", "Uma <span class='o'>nota</span> para a palavra-chave",
       "<p>É uma estimativa do Google sobre a qualidade dos seus anúncios em relação aos de outros anunciantes.</p>"
       + box("Por que importa", "Anúncios mais relevantes tendem a ter um <b>desempenho melhor</b> no leilão.")),
  text("02 · Os pilares", "O que <span class='o'>entra</span> na conta",
       items("<b>CTR esperada:</b> a chance de clique no anúncio",
             "<b>Relevância do anúncio:</b> o quanto ele combina com a busca",
             "<b>Experiência na página:</b> se a página é útil e coerente")),
  text("03 · Como melhorar", "Foque no <span class='o'>usuário</span>",
       items("Grupos de anúncios com <b>temas fechados</b>",
             "Títulos que <b>respondem</b> à busca",
             "Página <b>rápida</b>, clara e alinhada ao anúncio")),
  CTA],

 "2026-11-04_carrossel": [
  cover("Mercado gringo", "As buscas em inglês que mostram <span class='o'>intenção</span>", "Nem toda pesquisa está perto da compra."),
  text("01 · Curiosidade", "Ainda está <span class='o'>conhecendo</span>",
       "<p>Buscas como <b>\"what is...\"</b> ou <b>\"how to...\"</b>. A pessoa quer entender, ainda não decidiu.</p>"),
  text("02 · Comparação", "Está <span class='o'>avaliando</span>",
       "<p>Buscas como <b>\"review\"</b>, <b>\"vs\"</b> ou <b>\"does it work\"</b>. Já conhece o produto e quer confirmar.</p>"),
  text("03 · Decisão", "Está perto de <span class='o'>comprar</span>",
       "<p>Buscas como <b>\"buy\"</b>, <b>\"price\"</b> ou <b>\"discount\"</b>. A intenção de compra é mais clara.</p>"
       + box("Atenção", "Alguns produtores <b>proíbem</b> anunciar com o nome da marca. Leia as regras antes.")),
  CTA],
}

for sid, slides in SPECS.items():
    (D / f"{sid}.json").write_text(json.dumps({"id": sid, "slides": slides}, ensure_ascii=False, indent=1))
    print(sid, len(slides))
