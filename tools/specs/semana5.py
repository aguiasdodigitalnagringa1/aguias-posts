"""Semana 5 (19/11 a 25/11/2026) — primeira semana na grade de séries (modelos A–H).
Gera os JSON em specs/. Carrosséis: python3 render.py specs/<id>.json <saida> · Reels: python3 reel.py specs/<id>.json <saida>"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from modelos import *  # noqa

D = pathlib.Path(__file__).parent


def painel(nome, nivel, pct, dicas):
    """Ilustração genérica de 'força do anúncio' dentro do celular."""
    li = "".join(f"<div style='margin-top:14px'>• {d}</div>" for d in dicas)
    return ("<div class='card' style='padding:34px 36px'>"
            "<div style='font-size:24px;color:#5f6368'>Força do anúncio · ilustração</div>"
            f"<div style='font-size:44px;font-weight:600;margin:12px 0 18px'>{nivel}</div>"
            f"<div style='height:18px;border-radius:9px;background:#eee'><div style='width:{pct}%;height:100%;border-radius:9px;background:#FF7A1A'></div></div>"
            f"<div style='font-size:26px;color:#3c4043;margin-top:18px'>{nome}{li}</div></div>")


def titulos_rsa(fixado=None):
    linhas = [["Título 1", "[Produto] Review", "Fixado na posição 1" if fixado == 0 else "—"],
              ["Título 2", "See How It Works", "—"],
              ["Título 3", "Official Website", "—"],
              ["Título 4", "Read Before You Buy", "—"]]
    return tela_tabela(["Campo", "Texto", "Fixação"], linhas, destaque_linha=fixado, titulo="Ilustração · textos de exemplo")


CARROSSEIS = {
 # Qui 19/11 · A · Tutorial — colunas do painel
 "2026-11-19_carrossel": [
  a_capa("Monte as <span class='o'>colunas</span> do seu painel", "Passo a passo para deixar à vista o que importa na campanha de Pesquisa.",
         tela_tabela(["Campanha", "Cliques", "CTR", "Custo/conv."], [["Pesquisa · Teste 1", "—", "—", "—"]], destaque_linha=0)),
  a_passo(1, "Abra o menu de <span class='o'>colunas</span>",
          tela_tabela(["Opção", ""], [["Modificar colunas", "✎"], ["Salvar conjunto", "—"]], destaque_linha=0, titulo="Ilustração genérica do painel"),
          "Na tabela de campanhas, procure o ícone de <b>colunas</b> e entre em modificar."),
  a_passo(2, "Escolha as <span class='o'>métricas</span> da rotina",
          tela_tabela(["Métrica", "Mostrar"], [["Cliques", "✓"], ["CTR", "✓"], ["CPC médio", "✓"], ["Conversões", "✓"], ["Custo/conv.", "✓"]], destaque_linha=3),
          "Comece pelo básico: <b>clique, custo e conversão</b>. Menos colunas, leitura mais rápida."),
  a_passo(3, "Coloque na <span class='o'>ordem</span> da leitura",
          tela_tabela(["Ordem", "Coluna"], [["1", "Custo"], ["2", "Cliques e CTR"], ["3", "Conversões"], ["4", "Custo/conv."]], destaque_linha=0),
          "Arraste as colunas para ler da esquerda para a direita: <b>gastei, cliquei, converti</b>."),
  a_passo(4, "<span class='o'>Salve</span> o conjunto",
          tela_tabela(["Conjuntos salvos", ""], [["Rotina diária", "✓"], ["Revisão semanal", "—"]], destaque_linha=0, titulo="Ilustração · nomes de exemplo"),
          "Dê um nome ao conjunto e use o <b>mesmo</b> sempre: fica fácil comparar um dia com o outro."),
  cta("TUTORIAL")],

 # Sex 20/11 · E · Mito x Verdade — primeira campanha
 "2026-11-20_carrossel": [
  e_capa("<span class='o'>Mitos</span> da primeira campanha", "O que costuma travar quem está começando no Google Ads."),
  e_par("Quanto mais palavras-chave, melhor.", "Poucas palavras com intenção clara são mais fáceis de acompanhar e ajustar."),
  e_par("Campanha nova tem que vender no primeiro dia.", "No começo você está juntando dados. Julgue por um período, não por um dia."),
  e_par("CPC baixo é sinal de campanha boa.", "Clique barato que não converte continua sendo caro. Olhe o custo por conversão."),
  e_par("Se não vendeu, o problema é a oferta.", "Antes, confira rastreamento, termos de pesquisa e a página de destino.", swipe=True),
  cta("MITO X VERDADE")],

 # Sáb 21/11 · C · Métrica — taxa de conversão
 "2026-11-21_carrossel": [
  c_capa("TX. CONV.", "Taxa de conversão", ["conversões", "÷", "cliques", "×", "100"], "Mostra quantos dos <b>cliques</b> viraram a ação que você mede."),
  c_texto("Como ler", "Ela fala da <span class='o'>página</span> e da <span class='o'>busca</span>",
          "<p>Se as pessoas clicam e não convertem, o problema pode estar na <b>intenção</b> do termo ou no que a <b>página</b> entrega.</p>"
          "<div class='box'><div class='lbl'>Exemplo · valores fictícios</div>4 conversões ÷ 200 cliques × 100 = <b>2%</b></div>"),
  c_texto("Cuidado", "Poucos cliques, <span class='o'>conclusão</span> fraca",
          "<p>Com poucos cliques, uma venda a mais ou a menos muda tudo. Junte dados suficientes <b>antes</b> de tirar conclusões.</p>"),
  c_texto("Na prática", "Compare por <span class='o'>palavra-chave</span>",
          "<p>A taxa geral esconde diferenças. Veja quais termos convertem melhor e onde a verba está indo <b>sem retorno</b>.</p>"
          "<div class='box'><div class='lbl'>Lembre</div>Só confie no número se o <b>rastreamento</b> estiver testado.</div>"),
  cta("MÉTRICA DA SEMANA")],

 # Dom 22/11 · F · Frase
 "2026-11-22_imagem": [f_frase("Não é sobre acertar de primeira. <i>É sobre errar barato e aprender rápido.</i>")],

 # Seg 23/11 · D · Checklist — revisão semanal
 "2026-11-23_carrossel": [
  d_capa("Toda semana", "A revisão <i>semanal</i> da campanha", ["Termos de pesquisa", "Negativas novas", "Conversões conferidas", "… e mais 3"]),
  d_itens([("Termos de pesquisa", "Veja por quais buscas o anúncio apareceu na semana."),
           ("Negativas novas", "Adicione os termos que gastaram sem intenção de compra.")]),
  d_itens([("Conversões conferidas", "Compare o que o Google registrou com o painel da plataforma."),
           ("Status dos anúncios", "Procure anúncios reprovados ou limitados.")], inicio=3),
  d_itens([("Gasto x limite de teste", "Confira se a verba está dentro do que você definiu."),
           ("Anotações", "Registre o que mudou e o que vai observar na próxima semana.")], inicio=5),
  cta("CHECKLIST", lt=True)],

 # Ter 24/11 · B · Errado x Certo — configuração
 "2026-11-24_carrossel": [
  b_capa("Configuração: <span class='o'>errado x certo</span>", "Escolhas de início que mudam o resto da campanha."),
  b_par("<span class='o'>Verba</span> de teste", "Sem limite definido", "Você só percebe o quanto gastou <b>depois</b>.",
        "Valor total decidido antes", "Você sabe até onde vai e quando <b>reavaliar</b>."),
  b_par("<span class='o'>Lance</span> e conversão", "Lance automático sem conversão", "O sistema não sabe o que é <b>resultado</b> para você.",
        "Conversão testada primeiro", "Só depois escolha a estratégia de <b>lance</b>."),
  b_par("<span class='o'>Rede</span> da campanha", "Aceitar o padrão sem ler", "Opções marcadas podem levar o anúncio para <b>fora</b> da busca.",
        "Revisar cada opção", "Mantenha o foco na <b>Rede de Pesquisa</b> do Google.",
        "Cada configuração muda <b>onde</b> e <b>para quem</b> o anúncio aparece."),
  cta("ERRADO X CERTO")],

 # Qua 25/11 · A · Tutorial — fixar títulos
 "2026-11-25_carrossel": [
  a_capa("Como <span class='o'>fixar</span> títulos no anúncio", "Quando usar e quando evitar no anúncio responsivo de Pesquisa.", titulos_rsa(0)),
  a_passo(1, "Entenda o <span class='o'>padrão</span>", titulos_rsa(),
          "Sem fixar, o Google <b>combina</b> seus títulos e testa a ordem sozinho."),
  a_passo(2, "Fixe só o <span class='o'>essencial</span>", titulos_rsa(0),
          "Ex.: um título que <b>precisa</b> aparecer sempre, como uma informação exigida pela oferta."),
  a_passo(3, "Fixe mais de <span class='o'>um texto</span>",
          tela_tabela(["Posição 1", "Opções"], [["[Produto] Review", "✓"], ["[Produto] Official Info", "✓"]], destaque_linha=1, titulo="Ilustração · textos de exemplo"),
          "Colocar 2 ou 3 títulos na mesma posição <b>mantém a variação</b> e ainda controla a mensagem."),
  a_passo(4, "Acompanhe a <span class='o'>força</span>", tela_anuncio(titulo="[Produto] Review | See How It Works", destaque="titulo"),
          "Fixar demais reduz as combinações. Use com moderação e <b>compare</b> o desempenho."),
  cta("TUTORIAL")],
}

ITENS_FRI = [("Defina o valor total", "Antes de começar, não durante."),
             ("Revise o gasto diário", "Um minuto por dia evita surpresa."),
             ("Tenha uma regra de parada", "Decida antes o que te faz pausar ou ajustar.")]
ITENS_SUN = [("Seu link funciona?", "Clique e veja se cai na página certa."),
             ("Regras de tráfego", "Leia o que a oferta permite em anúncios de busca."),
             ("Os números batem?", "Compare cliques e vendas com o Google Ads.")]
ITENS_TUE = [("Dias 1 e 2", "Confira se está rodando e se a conversão registra."),
             ("Dias 3 e 4", "Leia os termos de pesquisa e negative o que não serve."),
             ("Dias 5 a 7", "Junte dados antes de qualquer mudança grande.")]

REELS = {
 # Qui 19/11 · G — força do anúncio
 "2026-11-19_reel": [
  g_titulo("Anúncio", "O que a <span class='o'>força do anúncio</span> mede?"),
  g_tela("Ela olha o <span class='o'>texto</span>", painel("Sugestões:", "Média", 50, ["Mais títulos únicos", "Use palavras-chave nos títulos"]),
         "Variedade e relação com as palavras-chave."),
  g_tela("Não é o <span class='o'>resultado</span>", g_kpis([("Força", "Boa"), ("Conversões", "?")], ativo=1),
         "Força alta não garante venda."),
  g_tela("Use como <span class='o'>guia</span>", painel("Sugestões:", "Boa", 80, ["Títulos diferentes entre si"]),
         "E decida pelos números da campanha."),
  r_cta()],

 # Sex 20/11 · H — verba de teste
 "2026-11-20_reel": [h_titulo("3 hábitos para não <i>estourar</i> a verba de teste")]
  + [h_lista("Verba de <i>teste</i>", ITENS_FRI, k) for k in range(3)] + [r_cta(lt=True)],

 # Sáb 21/11 · R (fallback G) — copiar campanha
 "2026-11-21_reel": [
  g_titulo("Estratégia", "Por que copiar a campanha de alguém <span class='o'>não basta</span>"),
  g_tela("Outra <span class='o'>conta</span>", g_kpis([("Histórico", "≠"), ("Verba", "≠")], ativo=0), "Cada conta tem histórico e verba diferentes."),
  g_tela("Outro <span class='o'>momento</span>", g_kpis([("Concorrência", "↑"), ("CPC", "?")], ativo=0) + g_grafico(True), "O leilão muda com o tempo."),
  g_tela("Copie o <span class='o'>método</span>", tela_tabela(["Etapa", ""], [["Pesquisar termos", "✓"], ["Testar", "✓"], ["Ajustar", "✓"]], destaque_linha=1),
         "Não a campanha pronta."),
  r_cta()],

 # Dom 22/11 · H — painel da plataforma
 "2026-11-22_reel": [h_titulo("Painel da plataforma: <i>3 coisas</i> para checar")]
  + [h_lista("No painel da <i>plataforma</i>", ITENS_SUN, k) for k in range(3)] + [r_cta(lt=True)],

 # Seg 23/11 · G — CPA subiu
 "2026-11-23_reel": [
  g_titulo("Diagnóstico", "O custo por conversão <span class='o'>subiu</span>. E agora?"),
  g_tela("1. O <span class='o'>CPC</span>", g_kpis([("CPC médio", "↑"), ("Custo/conv.", "↑")], ativo=0) + g_grafico(True), "O clique ficou mais caro?"),
  g_tela("2. A <span class='o'>conversão</span>", g_kpis([("Cliques", "="), ("Tx. conv.", "↓")], ativo=1) + g_grafico(False), "Menos cliques viraram venda?"),
  g_tela("3. Os <span class='o'>termos</span>", tela_tabela(["Termo", "Conv."], [["[produto] review", "—"], ["[produto] free trial", "—"]], destaque_linha=1),
         "Entraram buscas novas sem intenção?"),
  r_cta()],

 # Ter 24/11 · R (fallback H) — primeiros 7 dias
 "2026-11-24_reel": [h_titulo("Os primeiros <i>7 dias</i> de uma campanha nova")]
  + [h_lista("Primeira <i>semana</i>", ITENS_TUE, k) for k in range(3)] + [r_cta(lt=True)],

 # Qua 25/11 · G — informações do leilão
 "2026-11-25_reel": [
  g_titulo("Concorrência", "Quem disputa o <span class='o'>mesmo leilão</span> que você?"),
  g_tela("Informações do <span class='o'>leilão</span>",
         tela_tabela(["Domínio", "Sobrep."], [["Você", "—"], ["site-a.com", "—"], ["site-b.com", "—"]], destaque_linha=1, titulo="Ilustração · domínios fictícios"),
         "O relatório mostra quem aparece junto com você."),
  g_tela("Leia com <span class='o'>calma</span>", g_kpis([("Sobreposição", "↑"), ("Acima de você", "↑")], ativo=0),
         "Concorrência maior pode explicar CPC mais alto."),
  g_tela("Use para <span class='o'>entender</span>", g_kpis([("Seu anúncio", "?"), ("Sua página", "?")], ativo=0),
         "E não para copiar: melhore o que é seu."),
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
