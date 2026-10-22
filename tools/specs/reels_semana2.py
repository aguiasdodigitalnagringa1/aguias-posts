"""Specs dos 7 Reels animados de 29/10 a 04/11 (semana 2)."""
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
 "2026-10-29_reel": [
  hook("Sem isso, você está no escuro", "Rastreamento de <span class='o'>conversão</span>"),
  sc("O que é", "Saber qual clique virou <span class='o'>venda</span>"),
  sc("Sem rastreamento", "Você só vê <span class='o'>custo</span>", "Cliques e gastos, mas não o que deu resultado."),
  sc("Com rastreamento", "Você vê o que <span class='o'>funciona</span>", "Quais palavras-chave e anúncios trazem conversões."),
  sc("A regra", "Teste a conversão <span class='o'>antes</span> de publicar"),
  cta()],

 "2026-10-30_reel": [
  hook("Fique de olho", "3 sinais de que sua campanha precisa de <span class='o'>ajuste</span>"),
  sc("Sinal 1", "CTR <span class='o'>baixo</span>", "O anúncio aparece, mas quase ninguém clica."),
  sc("Sinal 2", "Cliques sem <span class='o'>conversão</span>", "Revise a página de destino e a intenção das buscas."),
  sc("Sinal 3", "Termos <span class='o'>sem relação</span>", "Buscas que nada têm a ver com o produto. Hora de negativar."),
  sc("Lembre", "Ajuste com <span class='o'>dados</span>, não com pressa"),
  cta()],

 "2026-10-31_reel": [
  hook("Escala", "Campanha deu certo. <span class='o'>Dobro o orçamento?</span>"),
  sc("Calma", "Mudanças bruscas <span class='o'>bagunçam</span> o aprendizado"),
  sc("O caminho", "Aumente <span class='o'>aos poucos</span>", "E observe como os números reagem a cada ajuste."),
  sc("Antes de escalar", "Confirme a <span class='o'>consistência</span>", "Um dia bom não é tendência. Veja um período maior."),
  sc("A regra", "Escalar é um <span class='o'>processo</span>, não um clique"),
  cta()],

 "2026-11-01_reel": [
  hook("Rotina", "O que quem roda campanhas <span class='o'>olha todo dia</span>"),
  sc("Checagem 1", "Gasto x <span class='o'>orçamento</span>", "A campanha está gastando como o planejado?"),
  sc("Checagem 2", "Termos de <span class='o'>pesquisa</span>", "Apareceu alguma busca que precisa virar negativa?"),
  sc("Checagem 3", "<span class='o'>Conversões</span>", "O rastreamento continua registrando normalmente?"),
  sc("Checagem 4", "Anúncios <span class='o'>aprovados</span>", "Nenhum anúncio ou palavra-chave reprovado?"),
  cta()],

 "2026-11-02_reel": [
  hook("Mercado gringo", "Seu anúncio está no ar no <span class='o'>horário certo</span>?"),
  sc("O detalhe", "O público está em outro <span class='o'>fuso horário</span>"),
  sc("Na prática", "Sua madrugada pode ser o <span class='o'>horário de pico</span> deles"),
  sc("O que fazer", "Analise os dados por <span class='o'>horário</span>", "E use a programação de anúncios a partir do que os números mostram."),
  sc("Lembre", "Confira o <span class='o'>fuso da conta</span> ao criar", "Ele é a referência dos seus relatórios."),
  cta()],

 "2026-11-03_reel": [
  hook("Políticas do Google", "Por que seu anúncio pode ser <span class='o'>reprovado</span>"),
  sc("Motivo comum", "Promessas <span class='o'>exageradas</span>", "Resultados garantidos ou milagrosos."),
  sc("Outro motivo", "Página que <span class='o'>não entrega</span>", "O que o anúncio diz precisa estar na página."),
  sc("Também", "Desrespeitar as regras do <span class='o'>produtor</span>", "Cada oferta tem as suas. Leia antes."),
  sc("A regra", "Anúncio <span class='o'>honesto</span> é anúncio que dura"),
  cta()],

 "2026-11-04_reel": [
  hook("Estratégia de lance", "Maximizar <span class='o'>cliques</span> ou <span class='o'>conversões</span>?"),
  sc("Maximizar cliques", "Foco em <span class='o'>tráfego</span>", "O Google busca o máximo de cliques dentro do orçamento."),
  sc("Maximizar conversões", "Foco em <span class='o'>resultado</span>", "O Google usa os dados de conversão para otimizar os lances."),
  sc("O ponto-chave", "Lance automático <span class='o'>precisa de dados</span>", "Sem conversões registradas, ele tem pouco para aprender."),
  sc("Resumo", "A escolha depende da <span class='o'>fase</span> da campanha"),
  cta()],
}

for sid, scenes in SPECS.items():
    (D / f"{sid}.json").write_text(json.dumps({"id": sid, "scenes": scenes}, ensure_ascii=False, indent=1))
    print(sid, len(scenes), round(sum(s["dur"] for s in scenes), 1), "s")
