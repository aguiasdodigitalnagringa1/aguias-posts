"""Semana 7 (03/12 a 09/12/2026) — grade de séries (modelos A–H).
Gera os JSON em specs/. Carrosséis: python3 render.py specs/<id>.json <saida> · Reels: python3 reel.py specs/<id>.json <saida>"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from modelos import *  # noqa

D = pathlib.Path(__file__).parent


def status_anuncio(status, motivo):
    """Ilustração genérica de status de anúncio."""
    return ("<div class='card' style='padding:34px 36px'>"
            "<div style='font-size:24px;color:#5f6368'>Status do anúncio · ilustração</div>"
            f"<div style='font-size:40px;font-weight:600;margin:14px 0 10px;color:#202124'>{status}</div>"
            f"<div style='font-size:26px;color:#3c4043;line-height:1.45'>{motivo}</div></div>")


CARROSSEIS = {
 # Qui 03/12 · A · Tutorial — comparar períodos
 "2026-12-03_carrossel": [
  a_capa("Compare <span class='o'>períodos</span> no painel", "Passo a passo para ver se a campanha melhorou ou piorou de verdade.",
         tela_tabela(["Métrica", "Atual", "Anterior"], [["Cliques", "—", "—"], ["Conversões", "—", "—"]], destaque_linha=1, titulo="Ilustração · sem dados reais")),
  a_passo(1, "Abra o <span class='o'>seletor de datas</span>",
          tela_tabela(["Período", ""], [["Últimos 7 dias", "✓"], ["Comparar", "ativar"]], destaque_linha=1, titulo="Ilustração genérica do painel"),
          "No canto da tela de campanhas, escolha o período e ative a opção de <b>comparar</b>."),
  a_passo(2, "Escolha a <span class='o'>comparação</span>",
          tela_tabela(["Comparar com", "Quando usar"], [["Período anterior", "Ver a tendência recente"], ["Mesmo período do ano passado", "Épocas sazonais"]], destaque_linha=0, titulo="Ilustração · opções de exemplo"),
          "Compare períodos do <b>mesmo tamanho</b> e com dias da semana parecidos."),
  a_passo(3, "Leia a <span class='o'>variação</span>",
          tela_tabela(["Métrica", "Variação"], [["Cliques", "↑"], ["Custo", "↑"], ["Conversões", "→"]], destaque_linha=2, titulo="Ilustração · valores fictícios"),
          "Mais cliques com as mesmas conversões pede <b>investigação</b>, não comemoração."),
  a_passo(4, "Anote o <span class='o'>contexto</span>",
          tela_tabela(["Data", "O que mudou"], [["Semana 1", "Novo anúncio"], ["Semana 2", "Negativas novas"]], destaque_linha=1, titulo="Ilustração · anotações de exemplo"),
          "Toda variação tem uma causa provável. Registre o que você <b>alterou</b> em cada período."),
  cta("TUTORIAL")],

 # Sex 04/12 · E · Mito x Verdade — palavras-chave
 "2026-12-04_carrossel": [
  e_capa("<span class='o'>Mitos</span> sobre palavras-chave", "Crenças comuns que atrapalham quem está começando."),
  e_par("Quanto mais palavras-chave, mais vendas.", "Muitas palavras espalham a verba e dificultam saber o que funciona."),
  e_par("Palavra com mais buscas é sempre a melhor.", "Volume alto pode ser curiosidade. A intenção de compra pesa mais."),
  e_par("Correspondência exata mostra só o termo exato.", "Ela também aceita variações com o mesmo sentido. Por isso, leia os termos de pesquisa."),
  e_par("Depois de configurar, é só esperar.", "Palavras-chave pedem revisão: negativar, pausar e testar faz parte do processo.", swipe=True),
  cta("MITO X VERDADE")],

 # Sáb 05/12 · C · Métrica — ROAS
 "2026-12-05_carrossel": [
  c_capa("ROAS", "Retorno sobre o gasto com anúncios", ["valor das conversões", "÷", "custo"],
         "Mostra quanto <b>voltou em valor</b> para cada unidade investida em anúncios."),
  c_texto("Como ler", "Um número, <span class='o'>duas leituras</span>",
          "<p>ROAS acima de 1 significa que o valor das conversões passou o custo. Abaixo de 1, o anúncio custou mais do que trouxe.</p>"
          "<div class='box'><div class='lbl'>Exemplo · valores fictícios</div>500 em comissões ÷ 250 de custo = <b>ROAS 2</b></div>"),
  c_texto("Para o afiliado", "Use o valor da <span class='o'>comissão</span>",
          "<p>No cálculo, o valor que importa é a <b>comissão</b> que você recebe, não o preço do produto.</p>"),
  c_texto("Cuidado", "ROAS bom com <span class='o'>poucos dados</span> engana",
          "<p>Uma venda isolada pode deixar o número bonito. Olhe um <b>período</b> com volume e lembre dos reembolsos.</p>"
          "<div class='box'><div class='lbl'>Lembre</div>Métrica é bússola, <b>não promessa</b>.</div>"),
  cta("MÉTRICA DA SEMANA")],

 # Dom 06/12 · F · Frase
 "2026-12-06_imagem": [f_frase("Disciplina é fazer a revisão <i>mesmo quando a semana foi boa.</i>")],

 # Seg 07/12 · D · Checklist — fechamento do mês
 "2026-12-07_carrossel": [
  d_capa("Fim de mês", "Checklist de <i>fechamento</i> do mês", ["Números do mês salvos", "Comparação com o mês anterior", "Faturamento conferido", "… e mais 3"]),
  d_itens([("Números do mês salvos", "Baixe o relatório das campanhas antes de esquecer."),
           ("Comparação com o mês anterior", "Veja o que subiu, o que caiu e por quê.")]),
  d_itens([("Faturamento conferido", "Confira se o que foi cobrado bate com o painel."),
           ("Comissões x custo", "Compare o que entrou na plataforma com o que saiu em anúncios.")], inicio=3),
  d_itens([("Aprendizados anotados", "Registre o que funcionou e o que não funcionou."),
           ("Teste do próximo mês", "Defina um único teste principal para começar.")], inicio=5),
  cta("CHECKLIST", lt=True)],

 # Ter 08/12 · B · Errado x Certo — texto do anúncio
 "2026-12-08_carrossel": [
  b_capa("Texto do anúncio: <span class='o'>errado x certo</span>", "Escolhas de escrita que mudam quem clica."),
  b_par("O <span class='o'>título</span>", "“Best Product Ever”", "Genérico, não conversa com o que a pessoa <b>buscou</b>.",
        "“[Produto] Review: How It Works”", "Repete a busca e mostra o que a pessoa vai <b>encontrar</b>."),
  b_par("A <span class='o'>promessa</span>", "Prometer resultado garantido", "Exagero tira credibilidade e pode <b>reprovar</b> o anúncio.",
        "Mostrar o que a página entrega", "Informação clara atrai quem tem <b>interesse real</b>."),
  b_par("A <span class='o'>chamada</span>", "“Click here”", "Não diz o que acontece depois do <b>clique</b>.",
        "“See Details on the Official Site”", "A pessoa sabe para onde vai e <b>o que</b> vai ver.",
        "O anúncio certo atrai o clique de quem está <b>perto da decisão</b>."),
  cta("ERRADO X CERTO")],

 # Qua 09/12 · A · Tutorial — regras automatizadas (alerta)
 "2026-12-09_carrossel": [
  a_capa("Crie um <span class='o'>alerta</span> automático", "Passo a passo para receber um aviso quando algo sair do esperado.",
         tela_tabela(["Regra", "Ação"], [["Custo do dia acima do limite", "Enviar e-mail"]], destaque_linha=0, titulo="Ilustração · valores de exemplo")),
  a_passo(1, "Abra as <span class='o'>regras</span>",
          tela_tabela(["Menu", ""], [["Ferramentas", "›"], ["Regras automatizadas", "✓"]], destaque_linha=1, titulo="Ilustração genérica do painel"),
          "Elas ficam no menu de <b>ferramentas</b> da conta, em ações em massa."),
  a_passo(2, "Escolha <span class='o'>enviar e-mail</span>",
          tela_tabela(["Tipo de regra", ""], [["Pausar campanhas", "—"], ["Enviar e-mail", "✓"]], destaque_linha=1, titulo="Ilustração · opções de exemplo"),
          "Comece com um <b>aviso</b>: você decide o que fazer, a regra só te chama."),
  a_passo(3, "Defina a <span class='o'>condição</span>",
          tela_tabela(["Condição", "Exemplo"], [["Custo", "maior que seu limite"], ["Período", "hoje"]], destaque_linha=0, titulo="Ilustração · valores fictícios"),
          "Use um limite que faça sentido para a sua <b>verba de teste</b>."),
  a_passo(4, "Programe a <span class='o'>frequência</span>",
          tela_tabela(["Frequência", ""], [["Uma vez", "—"], ["Diariamente", "✓"]], destaque_linha=1, titulo="Ilustração genérica do painel"),
          "Revise as regras de vez em quando para não receber <b>avisos antigos</b>."),
  cta("TUTORIAL")],
}

ITENS_FRI = [("Fica fácil acompanhar", "Você enxerga o que cada termo está fazendo."),
             ("A verba não se espalha", "Cada palavra recebe dados suficientes."),
             ("Você aprende mais rápido", "Fica claro o que manter e o que cortar.")]
ITENS_SUN = [("Poucos cliques", "Com pouco volume, qualquer número oscila."),
             ("Decisão em um dia", "Um dia ruim não define a campanha."),
             ("Compara com a expectativa", "Compare com o histórico, não com o que você queria.")]
ITENS_TUE = [("Vai ter teste que não dá certo", "Faz parte. O importante é saber por quê."),
             ("Anotar vale ouro", "Seu histórico vira o seu melhor professor."),
             ("Ler números é treino", "Fica mais fácil com prática e com método.")]

REELS = {
 # Qui 03/12 · G — CPA desejado
 "2026-12-03_reel": [
  g_titulo("Lances", "CPA desejado: <span class='o'>quando usar</span>?"),
  g_tela("O que <span class='o'>é</span>", g_kpis([("Estratégia", "CPA desejado"), ("Meta", "custo/conv.")], ativo=0),
         "Você informa quanto quer pagar por conversão."),
  g_tela("Precisa de <span class='o'>histórico</span>", g_kpis([("Conversões", "registradas"), ("Rastreamento", "✓")], ativo=0),
         "Sem conversões medidas, o Google não tem base."),
  g_tela("Meta <span class='o'>realista</span>", tela_tabela(["Meta", "Efeito"], [["Muito baixa", "Pouca entrega"], ["Perto do histórico", "Mais estável"]], destaque_linha=1, titulo="Ilustração · sem dados reais"),
         "Comece perto do custo que a campanha já tem."),
  r_cta()],

 # Sex 04/12 · H — poucas palavras-chave
 "2026-12-04_reel": [h_titulo("3 motivos para começar com <i>poucas</i> palavras-chave")]
  + [h_lista("Começar <i>enxuto</i>", ITENS_FRI, k) for k in range(3)] + [r_cta(lt=True)],

 # Sáb 05/12 · R (fallback G) — é para todo mundo?
 "2026-12-05_reel": [
  g_titulo("Papo reto", "Afiliado no Google Ads é <span class='o'>para todo mundo</span>?"),
  g_tela("Exige <span class='o'>método</span>", tela_tabela(["Rotina", ""], [["Ler os números", "✓"], ["Ajustar com critério", "✓"], ["Anotar o que mudou", "✓"]], destaque_linha=0, titulo="Ilustração"),
         "Não é sorte, é processo."),
  g_tela("Exige <span class='o'>verba de teste</span>", g_kpis([("Verba de teste", "definida"), ("Limite", "respeitado")], ativo=0),
         "Dinheiro que você pode usar para aprender."),
  g_tela("Exige <span class='o'>paciência</span>", g_kpis([("Dados", "acumulando"), ("Decisão", "depois")], ativo=1),
         "Resultado não é garantido nem imediato."),
  r_cta()],

 # Dom 06/12 · H — conclusão cedo demais
 "2026-12-06_reel": [h_titulo("3 sinais de que você está <i>concluindo cedo</i> demais")]
  + [h_lista("Calma com a <i>análise</i>", ITENS_SUN, k) for k in range(3)] + [r_cta(lt=True)],

 # Seg 07/12 · G — aprovado (limitado)
 "2026-12-07_reel": [
  g_titulo("Anúncios", "Status <span class='o'>aprovado (limitado)</span>"),
  g_tela("O que <span class='o'>significa</span>", status_anuncio("Aprovado (limitado)", "O anúncio pode ser exibido, mas com alguma restrição de política."),
         "Ele roda, mas com restrições."),
  g_tela("Veja o <span class='o'>motivo</span>", status_anuncio("Aprovado (limitado)", "Passe o mouse no status para ver a política indicada."),
         "O painel mostra qual política foi aplicada."),
  g_tela("O que <span class='o'>fazer</span>", tela_tabela(["Ação", ""], [["Ler a política indicada", "✓"], ["Ajustar texto ou página", "✓"]], destaque_linha=0, titulo="Ilustração"),
         "Entenda a regra antes de mudar o anúncio."),
  r_cta()],

 # Ter 08/12 · R (fallback H) — primeiros meses
 "2026-12-08_reel": [h_titulo("Primeiros meses como afiliado: <i>3 verdades</i>")]
  + [h_lista("Ninguém <i>conta</i>", ITENS_TUE, k) for k in range(3)] + [r_cta(lt=True)],

 # Qua 09/12 · G — palavra-chave repetida
 "2026-12-09_reel": [
  g_titulo("Palavras-chave", "A mesma palavra em <span class='o'>dois grupos</span>?"),
  g_tela("Elas <span class='o'>disputam</span>", tela_tabela(["Grupo", "Palavra-chave"], [["Grupo 1", "[produto] review"], ["Grupo 2", "[produto] review"]], destaque_linha=1, titulo="Ilustração · termos de exemplo"),
         "Fica difícil saber qual grupo vai aparecer."),
  g_tela("Os dados se <span class='o'>dividem</span>", g_kpis([("Grupo 1", "½"), ("Grupo 2", "½")], ativo=1),
         "E a análise fica confusa."),
  g_tela("Deixe <span class='o'>uma só</span>", tela_tabela(["Grupo", "Palavra-chave"], [["Grupo 1", "[produto] review"], ["Grupo 2", "[produto] price"]], destaque_linha=1, titulo="Ilustração · termos de exemplo"),
         "Cada termo no grupo que faz mais sentido."),
  r_cta()],
}

if __name__ == "__main__":
    for sid, slides in CARROSSEIS.items():
        (D / f"{sid}.json").write_text(json.dumps({"id": sid, "raw": True, "slides": slides}, ensure_ascii=False))
        print(sid, len(slides))
    for sid, scenes in REELS.items():
        k = 20.0 / sum(sc["dur"] for sc in scenes)  # ~20 s por Reel
        for sc in scenes: sc["dur"] = round(sc["dur"] * k, 2)
        (D / f"{sid}.json").write_text(json.dumps({"id": sid, "raw": True, "scenes": scenes}, ensure_ascii=False))
        print(sid, len(scenes), round(sum(s["dur"] for s in scenes), 1), "s")
