"""Specs dos 7 Reels animados de 12/11 a 18/11 (semana 4)."""
import json, pathlib

D = pathlib.Path(__file__).parent


def hook(kick, t):
    return {"kick": kick, "html": f"<div class='t'>{t}</div>", "dur": 3.0}


def sc(kick, t, sub=""):
    s = f"<div class='sub'>{sub}</div>" if sub else ""
    return {"kick": kick, "html": f"<div class='t m'>{t}</div>{s}", "dur": 3.6 if sub else 3.0}


def cta(t="Quer aprender o <span class='o'>passo a passo</span>?",
        sub="Comunidade <b>Águias do Digital</b>"):
    return {"cta": True, "dur": 3.6,
            "html": f"<img class='rlogo' src='{{{{LOGO}}}}'><div class='t m'>{t}</div><div class='sub'>{sub}</div><div><span class='rcta'>Link na bio</span></div>"}


SPECS = {
 "2026-11-12_reel": [
  hook("Regras da oferta", "Posso anunciar com o <span class='o'>nome do produto</span>?"),
  sc("Depende", "Cada produtor tem suas <span class='o'>regras</span>", "Alguns permitem, outros limitam ou proíbem."),
  sc("Onde ver", "Leia as <span class='o'>regras da oferta</span>", "Normalmente estão na página de afiliados."),
  sc("No Google", "Marcas têm <span class='o'>políticas</span> próprias", "O uso no texto do anúncio pode ser restrito."),
  sc("A regra", "Na dúvida, <span class='o'>pergunte</span> antes de anunciar"),
  cta()],

 "2026-11-13_reel": [
  hook("Diagnóstico", "Muitas <span class='o'>impressões</span> e poucos cliques?"),
  sc("O que indica", "O anúncio aparece, mas <span class='o'>não chama</span>"),
  sc("Olhe primeiro", "Os <span class='o'>termos de pesquisa</span>", "Talvez ele esteja aparecendo nas buscas erradas."),
  sc("Depois", "O <span class='o'>texto</span> do anúncio", "Ele responde ao que a pessoa buscou?"),
  sc("A regra", "Ajuste <span class='o'>uma coisa</span> por vez e compare"),
  cta()],

 "2026-11-14_reel": [
  hook("Diagnóstico", "Muitos <span class='o'>cliques</span> e nenhuma venda?"),
  sc("Passo 1", "Confira o <span class='o'>rastreamento</span>", "A venda pode ter acontecido sem ser registrada."),
  sc("Passo 2", "Olhe os <span class='o'>termos</span> de pesquisa", "Quem só está curioso clica, mas nem sempre compra."),
  sc("Passo 3", "Compare <span class='o'>anúncio e página</span>", "O que chamou o clique precisa estar lá."),
  sc("A regra", "Investigue antes de <span class='o'>aumentar</span> a verba"),
  cta()],

 "2026-11-15_reel": [
  hook("Comissão", "Reembolso: o que acontece com a <span class='o'>comissão</span>?"),
  sc("Em geral", "Ela é <span class='o'>estornada</span>", "Se o cliente pede o dinheiro de volta, a comissão costuma sair."),
  sc("Por isso", "Venda nova ainda não é <span class='o'>definitiva</span>", "Produtos costumam ter período de garantia."),
  sc("Na conta", "Olhe as vendas <span class='o'>líquidas</span>", "Já descontando os reembolsos."),
  sc("A regra", "Confira as regras de <span class='o'>cada plataforma</span>"),
  cta()],

 "2026-11-16_reel": [
  hook("Mercado gringo", "Black Friday lá fora: <span class='o'>o que muda</span>?"),
  sc("O leilão", "Mais anunciantes na <span class='o'>disputa</span>", "Os cliques podem ficar mais caros."),
  sc("A busca", "O público procura <span class='o'>promoção</span>", "Os termos e a intenção mudam nessa época."),
  sc("Confira", "A oferta tem <span class='o'>desconto</span> mesmo?", "Só anuncie o que está na página."),
  sc("A regra", "Mantenha a verba <span class='o'>sob controle</span>", "E não tire conclusões só desse período."),
  cta()],

 "2026-11-17_reel": [
  hook("Métrica", "Quantas buscas você está <span class='o'>perdendo</span>?"),
  sc("Parcela de impressões", "Quanto seu anúncio <span class='o'>apareceu</span>", "Entre as vezes em que ele poderia aparecer."),
  sc("Perda por orçamento", "A verba <span class='o'>não deu</span> para tudo"),
  sc("Perda por classificação", "Faltou <span class='o'>qualidade ou lance</span>", "O anúncio não ficou bem posicionado."),
  sc("A regra", "Entenda o <span class='o'>motivo</span> antes de aumentar a verba"),
  cta()],

 "2026-11-18_reel": [
  hook("Conversões", "A venda de hoje pode vir de um <span class='o'>clique antigo</span>"),
  sc("Por quê", "Nem todo mundo <span class='o'>compra na hora</span>", "Muita gente pesquisa antes de decidir."),
  sc("No relatório", "A conversão pode <span class='o'>demorar</span> a aparecer", "Os dias mais recentes ainda podem mudar."),
  sc("O risco", "Julgar tudo pelo <span class='o'>dia de ontem</span>", "E pausar cedo demais."),
  sc("A regra", "Olhe um <span class='o'>período</span>, não um dia"),
  cta()],
}

for sid, scenes in SPECS.items():
    (D / f"{sid}.json").write_text(json.dumps({"id": sid, "scenes": scenes}, ensure_ascii=False, indent=1))
    print(sid, len(scenes), round(sum(s["dur"] for s in scenes), 1), "s")
