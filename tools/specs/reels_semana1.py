"""Specs dos 7 Reels animados de 22 a 28/10 (semana 1)."""
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
 "2026-10-22_reel": [
  hook("Mercado gringo", "Por que tantos brasileiros estão <span class='o'>vendendo para fora</span>?"),
  sc("Motivo 1", "Comissões em <span class='o'>moeda forte</span>", "Os produtos internacionais pagam em <b>dólar</b> ou <b>euro</b>."),
  sc("Motivo 2", "Um mercado <span class='o'>gigante</span>", "Milhões de pessoas pesquisando produtos no Google todos os dias."),
  sc("Motivo 3", "Dá para fazer <span class='o'>daqui</span>", "Produto, pagamento e entrega ficam com o <b>produtor</b>."),
  sc("Papo reto", "Mas exige <span class='o'>método</span>", "Ferramentas certas, verba para testes e disciplina."),
  cta()],

 "2026-10-23_reel": [
  hook("Dúvida comum", "Preciso falar <span class='o'>inglês</span> para vender na gringa?"),
  sc("Resposta curta", "Não precisa ser <span class='o'>fluente</span>"),
  sc("Por quê?", "Você não atende o <span class='o'>cliente</span>", "Suporte, entrega e pagamento ficam com o <b>produtor</b>."),
  sc("O que ajuda", "Ler o <span class='o'>básico</span>", "E usar tradutores para pesquisar palavras-chave e entender a página do produto."),
  sc("Resumo", "Inglês fluente não é pré-requisito. <span class='o'>Método&nbsp;é.</span>"),
  cta()],

 "2026-10-24_reel": [
  hook("Iniciante, atenção", "O erro nº 1 de quem começa como <span class='o'>afiliado</span>"),
  sc("O erro", "Escolher o produto só pela <span class='o'>comissão</span>"),
  sc("O problema", "Comissão alta não adianta se <span class='o'>ninguém pesquisa</span> pelo produto"),
  sc("O que olhar antes", "Busca, regras e <span class='o'>página de vendas</span>", "Volume de pesquisa, regras do produtor para Google Ads e qualidade da oferta."),
  sc("A regra", "Produto certo + campanha certa <span class='o'>&gt; comissão alta</span>"),
  cta()],

 "2026-10-25_reel": [
  hook("Prazer, somos a", "<span class='o'>Águias do Digital</span>"),
  sc("O que é", "Uma comunidade para aprender a ser <span class='o'>afiliado no Google Ads</span>"),
  sc("O foco", "Mercado <span class='o'>gringo</span>", "Produtos e comissões internacionais."),
  sc("Como", "Aprender com quem <span class='o'>roda campanhas</span> todos os dias"),
  sc("Para quem", "Para quem trata o digital como <span class='o'>negócio</span>, não como aposta"),
  cta("Quer fazer parte?", "Conheça a comunidade <b>Águias do Digital</b>")],

 "2026-10-26_reel": [
  hook("Nosso método", "Por que focamos em campanhas de <span class='o'>Pesquisa</span>?"),
  sc("O motivo", "O anúncio aparece para quem <span class='o'>já está procurando</span>"),
  sc("Na prática", "A pessoa digita a dúvida...", "...e a resposta que aparece no topo é o <b>seu anúncio</b>."),
  sc("A diferença", "<span class='o'>Intenção</span> em vez de interrupção", "Quem pesquisa já está mais perto de decidir."),
  sc("O bônus", "Dados mais <span class='o'>claros</span> para otimizar"),
  cta()],

 "2026-10-27_reel": [
  hook("Mito ou verdade?", "Precisa de <span class='o'>muito dinheiro</span> para começar como afiliado?"),
  sc("A verdade", "Não precisa de uma <span class='o'>fortuna</span>", "Mas precisa de <b>verba para anúncios</b>."),
  sc("Por quê?", "Sem verba, <span class='o'>sem dados</span>", "E sem dados não dá para otimizar a campanha."),
  sc("Como começar", "Um orçamento de <span class='o'>teste</span>", "Que você aceita usar para aprender com os números."),
  sc("A regra", "Pouco dinheiro com método vale mais que <span class='o'>muito dinheiro sem estratégia</span>"),
  cta()],

 "2026-10-28_reel": [
  hook("Estratégia", "Página de <span class='o'>pré-venda</span>: o que é e por que usar?"),
  sc("O que é", "Uma página <span class='o'>sua</span>", "Entre o anúncio e a página do produtor."),
  sc("Para que serve", "<span class='o'>Aquece</span> o visitante", "Explica, responde dúvidas e prepara para a compra."),
  sc("Atenção", "Precisa ter <span class='o'>conteúdo útil</span>", "Página vazia só para redirecionar vai contra as políticas do Google."),
  sc("Resultado", "Feita do jeito certo, vira <span class='o'>vantagem</span>"),
  cta()],
}

for sid, scenes in SPECS.items():
    (D / f"{sid}.json").write_text(json.dumps({"id": sid, "scenes": scenes}, ensure_ascii=False, indent=1))
    print(sid, len(scenes), round(sum(s["dur"] for s in scenes), 1), "s")
