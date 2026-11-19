"""Semana 6 (26/11 a 02/12/2026) — grade de séries (modelos A–H).
Gera os JSON em specs/. Carrosséis: python3 render.py specs/<id>.json <saida> · Reels: python3 reel.py specs/<id>.json <saida>"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from modelos import *  # noqa

D = pathlib.Path(__file__).parent


def otimizacao(pct, recs):
    """Ilustração genérica de 'pontuação de otimização' com recomendações."""
    li = "".join(f"<div style='margin-top:14px'>• {r}</div>" for r in recs)
    return ("<div class='card' style='padding:34px 36px'>"
            "<div style='font-size:24px;color:#5f6368'>Pontuação de otimização · ilustração</div>"
            f"<div style='font-size:44px;font-weight:600;margin:12px 0 18px'>{pct}%</div>"
            f"<div style='height:18px;border-radius:9px;background:#eee'><div style='width:{pct}%;height:100%;border-radius:9px;background:#FF7A1A'></div></div>"
            f"<div style='font-size:26px;color:#3c4043;margin-top:18px'>Recomendações:{li}</div></div>")


def tendencia(sobe=True):
    return g_kpis([("Interesse na busca", "↑" if sobe else "↓"), ("Período", "12 meses")], ativo=0,
                  cab="Tendência de busca · ilustração") + g_grafico(sobe)


CARROSSEIS = {
 # Qui 26/11 · A · Tutorial — visualização e diagnóstico de anúncios
 "2026-11-26_carrossel": [
  a_capa("Veja seu anúncio <span class='o'>sem gerar clique</span>",
         "Como usar a ferramenta de visualização e diagnóstico de anúncios.",
         tela_anuncio(titulo="[Produto] Review | See How It Works", site="www.exemplo-produto.com", destaque="titulo")),
  a_passo(1, "Abra a <span class='o'>ferramenta</span>",
          tela_tabela(["Menu", ""], [["Ferramentas", "›"], ["Visualização e diagnóstico de anúncios", "✓"]], destaque_linha=1, titulo="Ilustração genérica do painel"),
          "Fica no menu de <b>ferramentas</b> da conta. Pesquisar no próprio Google gera impressão sem intenção de compra."),
  a_passo(2, "Digite a <span class='o'>busca</span>",
          tela_tabela(["Campo", "Exemplo"], [["Termo", "[produto] review"], ["Local", "Estados Unidos"], ["Idioma", "Inglês"], ["Dispositivo", "Celular"]], destaque_linha=0, titulo="Ilustração · valores de exemplo"),
          "Escolha o termo, o <b>local</b> e o <b>idioma</b> do público que você quer alcançar."),
  a_passo(3, "Leia o <span class='o'>diagnóstico</span>",
          tela_tabela(["Resultado", ""], [["Seu anúncio está aparecendo", "✓"], ["Não aparece: motivo indicado", "—"]], destaque_linha=1, titulo="Ilustração · mensagens de exemplo"),
          "Se o anúncio não aparece, a ferramenta costuma indicar um <b>motivo</b> para você investigar."),
  a_passo(4, "Confira o <span class='o'>texto</span>",
          tela_anuncio(titulo="[Produto] Review | See How It Works", desc="Read this before you buy. Official information and details.", destaque="desc"),
          "Veja como o anúncio fica na tela e se a mensagem está <b>clara</b> para quem busca."),
  cta("TUTORIAL")],

 # Sex 27/11 · E · Mito x Verdade — lances e orçamento
 "2026-11-27_carrossel": [
  e_capa("<span class='o'>Mitos</span> sobre lance e orçamento", "O que muita gente acredita e acaba custando caro."),
  e_par("Mais orçamento traz mais vendas.", "Orçamento maior em campanha sem ajuste só acelera o gasto. Primeiro o método, depois a escala."),
  e_par("Lance alto garante o primeiro lugar.", "A posição depende também da qualidade do anúncio e da página, não só do lance."),
  e_par("Lance automático dispensa acompanhamento.", "A estratégia automática ainda precisa de conversão bem medida e de revisão frequente."),
  e_par("Baixar o lance resolve custo alto.", "Às vezes o problema está nos termos, no anúncio ou na página. Investigue antes.", swipe=True),
  cta("MITO X VERDADE")],

 # Sáb 28/11 · C · Métrica — impressões no topo
 "2026-11-28_carrossel": [
  c_capa("TOPO %", "Impressões no topo", ["impr. no topo", "÷", "impressões", "×", "100"],
         "Mostra em quantas vezes o anúncio apareceu <b>acima</b> dos resultados orgânicos."),
  c_texto("Como ler", "Ela fala de <span class='o'>posição</span>, não de venda",
          "<p>Aparecer no topo costuma trazer mais atenção, mas também pode deixar o <b>clique</b> mais caro.</p>"
          "<div class='box'><div class='lbl'>Exemplo · valores fictícios</div>600 no topo ÷ 1.000 impressões × 100 = <b>60%</b></div>"),
  c_texto("Primeira posição", "Topo absoluto é <span class='o'>outra</span> métrica",
          "<p>O <b>topo absoluto</b> conta só quando o anúncio foi o primeiro de todos. Não confunda as duas na hora de analisar.</p>"),
  c_texto("Na prática", "Cruze com o <span class='o'>custo por conversão</span>",
          "<p>Subir no topo só vale a pena se a conta continuar fechando. Compare posição, CPC e conversões <b>juntos</b>.</p>"
          "<div class='box'><div class='lbl'>Lembre</div>Estar no topo não é objetivo. <b>Resultado</b> é.</div>"),
  cta("MÉTRICA DA SEMANA")],

 # Dom 29/11 · F · Frase
 "2026-11-29_imagem": [f_frase("Paciência não é ficar parado. <i>É saber exatamente o que você está esperando.</i>")],

 # Seg 30/11 · D · Checklist — segurança da conta
 "2026-11-30_carrossel": [
  d_capa("Conta protegida", "Checklist de <i>segurança</i> da conta", ["Verificação em 2 etapas", "Acessos revisados", "Pagamento conferido", "… e mais 3"]),
  d_itens([("Verificação em 2 etapas", "Ative no e-mail que acessa a conta de anúncios."),
           ("Acessos revisados", "Remova quem não precisa mais entrar na conta.")]),
  d_itens([("Pagamento conferido", "Veja se a forma de pagamento está ativa e é sua."),
           ("E-mail de recuperação", "Mantenha um contato atualizado para emergências.")], inicio=3),
  d_itens([("Notificações ligadas", "Receba avisos de políticas e de faturamento."),
           ("Senha só sua", "Nunca compartilhe login. Dê acesso pelo próprio painel.")], inicio=5),
  cta("CHECKLIST", lt=True)],

 # Ter 01/12 · B · Errado x Certo — ajustes na campanha
 "2026-12-01_carrossel": [
  b_capa("Ajustes na campanha: <span class='o'>errado x certo</span>", "Como mexer sem perder a leitura do que funcionou."),
  b_par("<span class='o'>Quantas</span> mudanças", "Mudar várias coisas juntas", "Depois você não sabe <b>qual</b> delas fez diferença.",
        "Uma mudança por vez", "Fica claro o que melhorou ou piorou o <b>resultado</b>."),
  b_par("<span class='o'>Quando</span> mudar", "Ajustar a cada clique", "Poucos dados levam a decisões no <b>impulso</b>.",
        "Esperar dados suficientes", "Decida com base em um <b>período</b>, não em um momento."),
  b_par("<span class='o'>O que</span> negativar", "Negativar tudo que não vendeu", "Você pode cortar termos que só precisavam de <b>tempo</b>.",
        "Negativar o que não tem intenção", "Corte buscas que nunca levariam à <b>compra</b>.",
        "Ajuste bom é aquele que você consegue <b>medir</b> depois."),
  cta("ERRADO X CERTO")],

 # Qua 02/12 · A · Tutorial — rótulos
 "2026-12-02_carrossel": [
  a_capa("Organize a conta com <span class='o'>rótulos</span>", "Passo a passo para encontrar campanhas, anúncios e testes em segundos.",
         tela_tabela(["Campanha", "Rótulo"], [["Pesquisa · Oferta 1", "Teste"], ["Pesquisa · Oferta 2", "Validada"]], destaque_linha=0, titulo="Ilustração · nomes de exemplo")),
  a_passo(1, "Selecione os <span class='o'>itens</span>",
          tela_tabela(["", "Campanha"], [["☑", "Pesquisa · Oferta 1"], ["☐", "Pesquisa · Oferta 2"]], destaque_linha=0, titulo="Ilustração genérica do painel"),
          "Marque as campanhas, grupos, anúncios ou palavras-chave que quer <b>agrupar</b>."),
  a_passo(2, "Crie o <span class='o'>rótulo</span>",
          tela_tabela(["Rótulo", "Uso"], [["Teste", "Em validação"], ["Validada", "Manter e acompanhar"], ["Pausar?", "Revisar na semana"]], destaque_linha=0, titulo="Ilustração · nomes de exemplo"),
          "Use nomes <b>curtos</b> e que indiquem o que fazer com aquele item."),
  a_passo(3, "<span class='o'>Filtre</span> pelo rótulo",
          tela_tabela(["Filtro", ""], [["Rótulo = Teste", "✓"]], destaque_linha=0, titulo="Ilustração genérica do painel"),
          "Na tabela, filtre por rótulo e veja só o que <b>importa</b> naquele momento."),
  a_passo(4, "<span class='o'>Atualize</span> na revisão",
          tela_tabela(["Campanha", "Antes", "Depois"], [["Pesquisa · Oferta 1", "Teste", "Validada"]], destaque_linha=0, titulo="Ilustração · nomes de exemplo"),
          "Na revisão semanal, troque o rótulo conforme a <b>decisão</b> que você tomou."),
  cta("TUTORIAL")],
}

ITENS_FRI = [("Qual é a intenção?", "A pessoa quer saber, comparar ou comprar?"),
             ("Tem relação com a oferta?", "O termo leva direto ao que a página entrega?"),
             ("Dá para acompanhar?", "Poucos termos claros são mais fáceis de ajustar.")]
ITENS_SUN = [("O CPC pode mudar", "Mais anunciantes disputam o mesmo leilão."),
             ("Compare períodos parecidos", "Não compare uma semana de pico com uma comum."),
             ("Cuidado com conclusões", "Uma semana atípica não define a campanha.")]
ITENS_TUE = [("Idioma", "Anúncio e página no idioma de quem busca."),
             ("Fuso horário", "O público está acordado em outro horário."),
             ("Moeda", "A comissão costuma vir em moeda estrangeira.")]

REELS = {
 # Qui 26/11 · G — pontuação de otimização
 "2026-11-26_reel": [
  g_titulo("Recomendações", "Pontuação de otimização: <span class='o'>aplicar tudo</span>?"),
  g_tela("É uma <span class='o'>sugestão</span>", otimizacao(62, ["Aumentar o orçamento", "Adicionar palavras-chave"]),
         "A pontuação mostra o que o Google sugere."),
  g_tela("Leia <span class='o'>cada uma</span>", otimizacao(62, ["Ampliar a correspondência", "Mudar a estratégia de lance"]),
         "Algumas aumentam o gasto ou ampliam o alcance."),
  g_tela("Decida pelos <span class='o'>seus dados</span>", g_kpis([("Pontuação", "100%"), ("Resultado", "?")], ativo=1),
         "Pontuação alta não é sinônimo de venda."),
  r_cta()],

 # Sex 27/11 · H — escolher palavra-chave
 "2026-11-27_reel": [h_titulo("3 perguntas antes de escolher uma <i>palavra-chave</i>")]
  + [h_lista("Antes de <i>escolher</i>", ITENS_FRI, k) for k in range(3)] + [r_cta(lt=True)],

 # Sáb 28/11 · R (fallback G) — por onde começar a estudar
 "2026-11-28_reel": [
  g_titulo("Começo", "Por onde começar a estudar <span class='o'>Google Ads</span>?"),
  g_tela("1. A <span class='o'>busca</span>", tela_tabela(["Busca", "Intenção"], [["what is [produto]", "Saber"], ["[produto] review", "Comparar"], ["buy [produto]", "Comprar"]], destaque_linha=2, titulo="Ilustração · termos de exemplo"),
         "Entenda o que a pessoa quer quando pesquisa."),
  g_tela("2. A <span class='o'>estrutura</span>", tela_tabela(["Nível", ""], [["Campanha", "›"], ["Grupo de anúncios", "›"], ["Palavras e anúncios", "✓"]], destaque_linha=1, titulo="Ilustração · campanha de Pesquisa"),
         "Campanha, grupo, palavras e anúncios."),
  g_tela("3. Os <span class='o'>números</span>", g_kpis([("CTR", "?"), ("Custo/conv.", "?")], ativo=1),
         "Aprenda a ler antes de mexer."),
  r_cta()],

 # Dom 29/11 · H — sazonalidade
 "2026-11-29_reel": [h_titulo("Fim de ano: <i>3 cuidados</i> com os números")]
  + [h_lista("Época de <i>pico</i>", ITENS_SUN, k) for k in range(3)] + [r_cta(lt=True)],

 # Seg 30/11 · G — tendência de busca
 "2026-11-30_reel": [
  g_titulo("Pesquisa", "Olhe a <span class='o'>tendência</span> antes de anunciar"),
  g_tela("O interesse <span class='o'>muda</span>", tendencia(True), "Algumas buscas sobem em certas épocas."),
  g_tela("Busca em <span class='o'>queda</span>", tendencia(False), "Menos buscas podem significar menos dados."),
  g_tela("Use como <span class='o'>contexto</span>", tela_tabela(["Termo", "Tendência"], [["[produto] review", "estável"], ["[produto] discount", "sazonal"]], destaque_linha=1, titulo="Ilustração · termos de exemplo"),
         "E confirme com os dados da sua campanha."),
  r_cta()],

 # Ter 01/12 · R (fallback H) — mercado gringo
 "2026-12-01_reel": [h_titulo("Mercado gringo: <i>3 diferenças</i> para quem vem do Brasil")]
  + [h_lista("Vender para <i>fora</i>", ITENS_TUE, k) for k in range(3)] + [r_cta(lt=True)],

 # Qua 02/12 · G — pouco volume de pesquisa
 "2026-12-02_reel": [
  g_titulo("Palavras-chave", "Status <span class='o'>pouco volume</span> de pesquisa"),
  g_tela("O que <span class='o'>significa</span>",
         tela_tabela(["Palavra-chave", "Status"], [["[produto] review", "Qualificada"], ["[produto] review 2026 official", "Pouco volume"]], destaque_linha=1, titulo="Ilustração · termos de exemplo"),
         "Quase ninguém pesquisa esse termo."),
  g_tela("Por que <span class='o'>importa</span>", g_kpis([("Impressões", "0"), ("Cliques", "0")], ativo=0),
         "Enquanto isso, ela não mostra o anúncio."),
  g_tela("O que <span class='o'>fazer</span>", tela_tabela(["Ação", ""], [["Testar variações mais comuns", "✓"], ["Não depender de um termo só", "✓"]], destaque_linha=0, titulo="Ilustração"),
         "Prefira termos que as pessoas realmente buscam."),
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
