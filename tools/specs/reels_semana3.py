"""Specs dos 7 Reels animados de 05/11 a 11/11 (semana 3)."""
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
 "2026-11-05_reel": [
  hook("Orçamento", "Como o Google <span class='o'>gasta</span> seu orçamento diário"),
  sc("O que é", "Uma <span class='o'>média</span> por dia", "Não um limite exato a cada 24 horas."),
  sc("Na prática", "Alguns dias gasta <span class='o'>mais</span>, outros menos", "O Google aproveita os dias com mais oportunidades."),
  sc("No mês", "O total segue um <span class='o'>limite</span>", "Confira as regras atuais na central de ajuda do Google Ads."),
  sc("A regra", "Defina um valor que você pode <span class='o'>testar com calma</span>"),
  cta()],

 "2026-11-06_reel": [
  hook("Conta no Google Ads", "Já ouviu falar em <span class='o'>verificação de anunciante</span>?"),
  sc("O que é", "O Google confirma <span class='o'>quem anuncia</span>"),
  sc("Por quê", "Mais <span class='o'>transparência</span> para os usuários", "Quem vê o anúncio pode saber quem está por trás."),
  sc("O que fazer", "Responda com <span class='o'>dados reais</span>", "E dentro do prazo que o Google indicar."),
  sc("Lembre", "Conta em dia é conta que <span class='o'>continua rodando</span>"),
  cta()],

 "2026-11-07_reel": [
  hook("Erro comum", "Mexer na campanha <span class='o'>todo dia</span>"),
  sc("O problema", "A campanha precisa de tempo para <span class='o'>aprender</span>"),
  sc("O que acontece", "Cada mudança grande <span class='o'>reinicia</span> a leitura", "E você nunca sabe o que realmente funcionou."),
  sc("O caminho", "Observe <span class='o'>todo dia</span>, ajuste com critério", "Acompanhar é diferente de mexer."),
  sc("A regra", "Paciência também é <span class='o'>estratégia</span>"),
  cta()],

 "2026-11-08_reel": [
  hook("Entenda o modelo", "Afiliado x produtor: <span class='o'>quem faz o quê</span>?"),
  sc("O produtor", "Cria e <span class='o'>entrega</span> o produto", "Cuida da página de vendas, do checkout e do suporte."),
  sc("O afiliado", "Leva o <span class='o'>público certo</span>", "Com anúncios que aparecem para quem já está buscando."),
  sc("A plataforma", "Conecta os <span class='o'>dois</span>", "Registra as vendas e repassa as comissões."),
  sc("Resumo", "Seu trabalho é o <span class='o'>tráfego</span> qualificado"),
  cta()],

 "2026-11-09_reel": [
  hook("Do clique à comissão", "O <span class='o'>caminho</span> de uma venda como afiliado"),
  sc("Passo 1", "A pessoa <span class='o'>pesquisa</span> no Google"),
  sc("Passo 2", "Vê seu <span class='o'>anúncio</span> e clica"),
  sc("Passo 3", "Chega à página pelo seu <span class='o'>link</span>", "É o link de afiliado que identifica você."),
  sc("Passo 4", "Se comprar, a venda é <span class='o'>registrada</span>", "Por isso o link e o rastreamento precisam estar certos."),
  cta()],

 "2026-11-10_reel": [
  hook("Leilão do Google", "Por que o <span class='o'>CPC</span> muda tanto?"),
  sc("O leilão", "Acontece a cada <span class='o'>busca</span>"),
  sc("Concorrência", "Mais anunciantes, mais <span class='o'>disputa</span>", "Em alguns dias e horários, o clique fica mais caro."),
  sc("Qualidade", "Anúncio relevante <span class='o'>ajuda</span>", "Não é só quem paga mais que aparece."),
  sc("A regra", "Olhe a <span class='o'>tendência</span>, não um dia isolado"),
  cta()],

 "2026-11-11_reel": [
  hook("Antes de desistir", "3 perguntas antes de <span class='o'>pausar</span> uma campanha"),
  sc("Pergunta 1", "Teve <span class='o'>dados</span> suficientes?", "Poucos cliques não contam a história toda."),
  sc("Pergunta 2", "A conversão está <span class='o'>rastreando</span>?", "Às vezes a venda aconteceu e não foi registrada."),
  sc("Pergunta 3", "Os termos de pesquisa são <span class='o'>relevantes</span>?", "Talvez falte negativar, não pausar."),
  sc("A regra", "Decida com <span class='o'>diagnóstico</span>, não com emoção"),
  cta()],
}

for sid, scenes in SPECS.items():
    (D / f"{sid}.json").write_text(json.dumps({"id": sid, "scenes": scenes}, ensure_ascii=False, indent=1))
    print(sid, len(scenes), round(sum(s["dur"] for s in scenes), 1), "s")
