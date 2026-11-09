# Briefing Visual — CRM Seu Milhão

> Versão pública sanitizada: fornecedores e parceiros viraram papéis genéricos, links de quadros privados e números de exemplo foram removidos.

**Status:** em andamento · **Data:** 24/08/2026 · **Ferramenta:** Whimsical (quadros privados, não publicados)

> Registro dos artefatos visuais do estudo de UX. Cada etapa é aprovada por David antes da seguinte começar. Fonte das decisões: `01-DECISOES-TRAVADAS.md`.

---

## Etapa 1 — Arquitetura de Informação ✅ APROVADA

IA — CRM Seu Milhão

Mapa mental com as 9 áreas do CRM: Home (ciclo atual) · Clientes · Segmentos · Campanhas · Jornadas (dia-1) · Templates · Console Dia de Sorteio · Monitor Pix · Fora de escopo.

**Alterações feitas por David direto no board (24/08, intencionais):**
- Removido **LGPD (exportar/apagar)** de Clientes — sem tela própria na v1 (decisão revertida em `01-DECISOES-TRAVADAS.md` §4)
- Removido **Lançar recompra** do Console Dia de Sorteio — recompra roda via jornada de resultado + campanha agendada (`01-DECISOES-TRAVADAS.md` §7)
- Removido **Reports de CRM SaaS de referência** do ramo Fora de escopo (já registrado no doc, dispensável no mapa)
- Simplificado texto dos atributos de Segmentos (sem "(batch)")

---

## Etapa 2 — Fluxos principais ✅ APROVADA

Rascunho em texto aprovado por David em 24/08. Boards criados:

1. Fluxo 1 — Recovery de Pix — SLA 15min, template Utility, expiração + marca p/ campanha futura
2. Fluxo 2 — Confirmação de Título — 1 pedido → N títulos, WhatsApp Utility, log no event store
3. Fluxo 3 — Resultado do Sorteio — ganhador (SLA pagamento) vs não-ganhador (recompra)
4. Fluxo 4 — Campanha Agendada — fluxo do operador com painel custo/margem e aviso de compliance (não bloqueia)

**Aprovação dos boards visuais:** aprovados por David em 24/08, sem alterações.

---

## Etapa 3 — Wireframes das telas-chave ✅ FASE 1 CONCLUÍDA (24/08)

**Entregue (grade 2×3 no board, alinhada):** Home · Apuração #47 · Detalhe Pix (linha 1) / Clientes · Segmentos · Compose (linha 2). Ajuste fino de alinhamento feito e verificado por render.

**Backlog (decisão de David, 24/08 — "para depois"):** telas de Jornadas (lista/canvas) e Campanhas (lista) · Perfil de cliente individual · Status de template WhatsApp.

Wireframes — CRM Seu Milhão

Decisão de David (24/08): Console Dia de Sorteio fica **sempre igual** no menu, sem destaque sazonal.

Ordem de prioridade:
1. Home — 🔄 v3 criada após 2 rodadas de feedback de David (24/08):
   - Busca de CPF removida (fica só em Segmentos); menu lateral mantido.
   - Topo: 5 cards uniformes com borda, mesma altura, número grande alinhado: dias até apuração · cotas vendidas (% como número principal) · faturamento · ROI (definição pendente, Q registrada) · compradores do ciclo (split novos/recompra).
   - **Cortados da Home:** "Campanha da semana" e "Jornadas (dia-1)" — julgados descartáveis; vivem nas suas áreas próprias.
   - **Mantidos:** Alertas (agora condicional — só renderiza quando houver alerta ativo) e gráfico "Vendas do ciclo, dia a dia".
   - David reorganizou os cards direto no board (layout dele preservado).
   - Gráfico definido (24/08): **barras empilhadas diárias (novos/recompra) + linha de acumulado vs meta de cotas** — mock desenhado no wireframe no lugar do placeholder.
   - ✅ **Home aprovada por David em 24/08** (v3 com rearranjo manual dele + gráfico combo).
2. Compose/envio de campanha — ✅ aprovado por David (24/08). 4 passos à esquerda (básico c/ categoria Marketing·Operational → segmento → template travado c/ preview e teste → quando) + painel direito fixo de custo/margem (semáforo) com aviso de compliance não-bloqueante, seletor de número/BSP e botão de envio.
3. Clientes — 🔄 v1 criada abaixo da Home (24/08), a pedido de David (adiantada na ordem). Dados consistentes com a Edição #47 da Home: tabs Todos ([n]) · Compradores #47 ([n]) · Leads provisórios ([n]); 4 KPIs (base, compradores c/ split, leads pré-CPF, LTV médio); 2 gráficos — compradores por safra/cohort (novos + recompra por edição) e distribuição RFM (batch noturno); lista com colunas "Seg. Anterior → Variação → Seg. Atual" (padrão do dev), export CSV. ✅ Aprovada por David (24/08).
4. Segmentos — 🔄 v1 criada ao lado de Clientes (24/08). Lista lateral de segmentos salvos (incl. um importado de CSV e um em tempo real via eventos); builder editando "Compradores #46 sem #47" (mesmo total dos destinatários do Compose); toggle Visual/SQL; condições com fonte explícita (batch vs event store); contador ao vivo; breakdown de compliance (contagem sem opt-in, consistente com o Compose); import CSV via rail de compliance; export CSV com seletor de colunas. Aguardando aprovação.
5. Apuração + Detalhe Pix — ✅ v1 criadas (24/08), realocadas para a linha 1 da grade ao lado da Home (são ações contextuais dela). **Decisão de David: Console Sorteio e Monitor Pix saem do menu** (8 → 6 áreas) e viram ações contextuais da Home: Apuração = overlay guiado de 4 passos aberto pelo card "Dias até apuração = 0" (concluir dispara o Fluxo 3); Detalhe Pix = overlay aberto pelo alerta (KPIs da última hora, ritmo esperado vs atual, lista dos travados com reenvio). Menus das 4 telas existentes e mapa mental de IA atualizados. Aguardando aprovação.
6. Perfil de cliente (timeline, RFM anterior→variação→atual) — ⏳ backlog
7. Status de template WhatsApp — ⏳ backlog
8. Jornadas (lista/canvas) e Campanhas (lista) — ⏳ backlog (deixadas para depois por decisão de David, 24/08)

## Etapa 4 — Revisão ⏳ PENDENTE

## Etapa 5 (opcional) — Mockups de alta fidelidade ⏳ PENDENTE
