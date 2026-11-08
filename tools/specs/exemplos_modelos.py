"""Exemplo completo de cada série nova (tools/modelos.py). Copie e adapte para a semana.
Gera os JSON em specs/; renderize com:  python3 render.py specs/ex_A.json <saida>  /  python3 reel.py specs/ex_G.json <saida>
Os textos aqui são só exemplo: os temas de verdade seguem o histórico do PROCESSO.md."""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from modelos import *  # noqa

D = pathlib.Path(__file__).parent

CARROSSEIS = {
 # A · Tutorial com tela — capa + 3 a 4 passos com ilustração + CTA
 "ex_A": [
  a_capa("Como usar <span class='o'>sitelinks</span> no anúncio", "Passo a passo para complementar o anúncio de Pesquisa.",
         tela_anuncio(sitelinks=["Como funciona", "Perguntas frequentes", "Garantia", "Contato"], destaque="sitelinks")),
  a_passo(1, "Onde eles <span class='o'>aparecem</span>", tela_anuncio(sitelinks=["Como funciona", "Perguntas frequentes"], destaque="sitelinks"),
          "Abaixo do anúncio, levando para <b>partes diferentes</b> da página."),
  a_passo(2, "Leia os <span class='o'>termos</span> antes", tela_tabela(["Termo de pesquisa", "Cliques"],
          [["[produto] review", "—"], ["[produto] price", "—"], ["free [produto]", "—"]], destaque_linha=2),
          "Termos como <b>free</b> raramente viram venda: candidatos a negativa."),
  cta("TUTORIAL")],
 # B · Errado x Certo — capa + 2 a 3 comparações + CTA
 "ex_B": [
  b_capa("Palavras-chave: <span class='o'>errado x certo</span>", "Pequenas escolhas que mudam quem vê seu anúncio."),
  b_par("Genérica x com <span class='o'>intenção</span>", "“weight loss”", "Muita gente curiosa, pouca perto da <b>decisão</b>.",
        "“[produto] review”", "Quem busca isso já está <b>avaliando</b>.", "Pesquisa funciona melhor quando a palavra mostra <b>o momento</b> de quem busca."),
  cta("ERRADO X CERTO")],
 # C · Métrica da semana — capa com fórmula + 2 a 3 slides de leitura + CTA
 "ex_C": [
  c_capa("CTR", "Taxa de cliques", ["cliques", "÷", "impressões", "×", "100"], "Mostra se o anúncio <b>chama atenção</b> de quem viu."),
  c_texto("Como ler", "CTR baixo <span class='o'>sozinho</span> não diz tudo", "<p>Compare com o histórico da própria campanha e olhe <b>quais termos</b> geram as impressões.</p>"),
  cta("MÉTRICA DA SEMANA")],
 # D · Checklist claro — capa + itens (até 3 por slide) + CTA claro
 "ex_D": [
  d_capa("Antes de publicar", "A revisão de <i>5 minutos</i> da campanha", ["País e idioma", "Palavras negativas", "Conversão testada", "… e mais 2"]),
  d_itens([("País e idioma", "Os que a oferta aceita e o idioma do público."), ("Palavras negativas", "Corte buscas que não têm intenção de compra."),
           ("Conversão testada", "Faça um teste antes de gastar.")]),
  cta("CHECKLIST", lt=True)],
 # E · Mito x Verdade — capa + 2 a 4 pares + CTA
 "ex_E": [
  e_capa("<span class='o'>Mitos</span> sobre o leilão do Google", "O que é verdade e o que é exagero."),
  e_par("Quem paga mais sempre aparece primeiro.", "O lance conta, mas a qualidade do anúncio também pesa no leilão."),
  cta("MITO X VERDADE")],
 # F · Frase de domingo — imagem única
 "ex_F": [f_frase("Campanha boa não nasce pronta. <i>Ela é ajustada.</i>")],
}

ITENS_H = [("Sem palavras negativas", "A verba vai para buscas sem intenção."),
           ("Sem testar a conversão", "Você não sabe o que funcionou."),
           ("Mudar tudo todo dia", "A campanha não tem tempo de aprender.")]

REELS = {
 # G · Reel com tela (escuro): título + 3 a 4 cenas de celular + CTA  (~20 s)
 "ex_G": [
  g_titulo("Diagnóstico", "Onde olhar quando o <span class='o'>CTR cai</span>"),
  g_tela("Impressões <span class='o'>sobem</span>…", g_kpis([("Impressões", "↑"), ("CTR", "↓")], ativo=0) + g_grafico(True), "Mais gente vendo o anúncio…"),
  g_tela("…e o CTR <span class='o'>cai</span>", g_kpis([("Impressões", "↑"), ("CTR", "↓")], ativo=1) + g_grafico(False), "…mas menos gente clicando."),
  g_tela("Olhe os <span class='o'>termos</span>", tela_tabela(["Termo", "Cliques"], [["[produto] review", "—"], ["free [produto]", "—"]], destaque_linha=1),
         "Buscas fora da intenção puxam o CTR para baixo."),
  r_cta()],
 # H · Reel em lista (claro): título + um item por cena + CTA  (~20 s)
 "ex_H": [h_titulo("3 erros na <i>primeira</i> campanha")]
         + [h_lista("3 erros na <i>primeira</i> campanha", ITENS_H, k) for k in range(3)]
         + [r_cta(lt=True)],
}

for sid, slides in CARROSSEIS.items():
    (D / f"{sid}.json").write_text(json.dumps({"id": sid, "raw": True, "slides": slides}, ensure_ascii=False))
    print(sid, len(slides))
for sid, scenes in REELS.items():
    (D / f"{sid}.json").write_text(json.dumps({"id": sid, "raw": True, "scenes": scenes}, ensure_ascii=False))
    print(sid, len(scenes), round(sum(s["dur"] for s in scenes), 1), "s")
