# Decisões Travadas — CRM Seu Milhão

> Versão pública sanitizada: fornecedores e parceiros viraram papéis genéricos, links de quadros privados e números de exemplo foram removidos.

**Status:** fase de perguntas/captura encerrada · **Data:** 20/08/2026

> Síntese de tudo que foi decidido, pergunta por pergunta, antes de escrever o blueprint. Nada aqui é definitivo até você revisar — é o checkpoint antes de eu começar a escrever os arquivos do estudo.

---

## 1. Escopo e vendors

- **Build completo** (segmentação, orquestração, disparo, assets) — CRM próprio, não plataforma comprada.
- **WhatsApp/SMS/Voz → provedor de WhatsApp/SMS (BSP)** (integrado ao CRM).
- **Email → provedor de email** (secundário, confirmado por você direto).
- **WhatsApp é o canal principal**, disparado — SMS/Voz e Email são de apoio, não recebem o mesmo investimento de design.
- **Marca única** (Seu Milhão). Sem multi-marca.
- **Sem app** — só website. Isso elimina Push e Inbox (central de notificação in-app) do escopo — não têm onde morar sem app/login persistente.
- **Deliverable final é pra uso pessoal seu**, não spec pro squad implementar às cegas.

---

## 2. Métrica-norte e métricas

- **FTD (First Time Deposit) por ciclo** é a métrica-norte — renomeado de "net-new" a seu pedido, terminologia do mercado de apostas.
- **19 métricas aprovadas** (12 core + 7 cirúrgicas): FTD net-new, conversão Pix, recuperação Pix, CPA, LTV, ticket médio, SLA de prêmio, recompra pós-sorteio, engajamento raspadinha/live, opt-in, atribuição de afiliado, frequência de contato + margem por edição de sorteio, payout ratio/exposição de prêmio pendente, WhatsApp quality/delivery rate, taxa de bloqueio pelo compliance rail, discrepância de tracking entre fontes, taxa de estorno de Pix, taxa de reclamação (ReclameAqui).
- **FTD por safra (cohort):** em escopo — rastrear de qual ciclo de aquisição cada cliente veio, pra medir recompra por cohort ao longo do tempo.
- **Home screen — topo revisado em 24/08 (briefing visual):** header com a edição atual + 5 cards: dias até apuração · cotas vendidas/total (com %) · faturamento atual · ROI atual · compradores do ciclo (únicos, com split novos/recompra — FTD vive aqui, dentro da composição, não como card isolado). Margem projetada saiu do topo (parcialmente coberta por ROI, definição pendente — ver Q em aberto). Saúde de canal WhatsApp segue fora do topo (é alerta, não KPI diário). Busca por CPF saiu da Home (fica só em Segmentos).

---

## 3. Modelo de dados

- **IA cycle-first, dado entity-first:** home organizada em torno da `edição de sorteio` atual, mas Cliente/segmentos/jornadas de longa duração são agnósticas de ciclo — só referenciam via FK, não ficam aninhadas nele (senão quebra LTV/RFM/recompra entre ciclos).
- **Chave única do cliente: CPF.** Leads pré-compra (só telefone) viram registro provisório até o CPF aparecer no primeiro pagamento.
- **Pedido = aggregate root financeiro** (1 Pix = 1 pedido = 1 máquina de estado: carrinho/gerado/pago/expirado/estornado). **Título = entidade filha legal** (série + número da sorte), gerada por pedido pago (1 pedido → N títulos em combo), herda o estado do pedido, ganha estado próprio só pós-apuração. Receita/ticket/CPA/margem contam por Pedido; titularidade/apuração/prêmio contam por Título.
- **Event store append-only, confirmado:** todo evento (Pix, raspadinha, mensagem entregue) é logado pra sempre, nunca sobrescrito. Tabelas de estado atual (perfil, segmento) são derivadas desse log.
- **Atributos derivados (RFM, Value Score, LTV):** recalculados 1x/dia (batch noturno) — aceitável ficar até 1 dia desatualizado.
- **Latência transacional:** recovery de Pix não pago dispara em até **15 min** (webhook, tempo real) — diferente e mais rápido que o batch acima.
- **Política de dado com o fornecedor da plataforma de vendas:** exigimos o que for necessário (raspadinha jogada, live assistida, UTM/atribuição), não desenhamos só em cima do payload limitado de hoje.

---

## 4. Regulação e compliance

- **Rail de compliance é aviso, não bloqueio duro** — envio pra não-opt-in/menor/fora de horário mostra aviso explícito, mas você pode ignorar (você mesmo vai operar). Risco residual de LGPD/SUSEP registrado, decisão mantida.
- **Sem etapa de aprovação dentro do sistema** — combinado por fora.
- ~~LGPD (apagar/exportar dado de cliente) entra na v1 — tela própria~~ → **REVERTIDO em 24/08 (briefing visual):** sem tela própria de LGPD na v1; tratamento fica manual/por fora. Risco residual mantido em registro.
- **Log permanente de quem/o quê/quando/copy** — coberto pelo event store, não é sistema separado.

---

## 5. Economia na interface

- **Painel de custo/margem** ao lado do botão de enviar (não relatório separado): custo projetado, conversão de equilíbrio, margem esperada — com sinal verde/amarelo/vermelho. Avisa se margem negativa, não bloqueia.
- **Sem teto de gasto, sem confirmação extra** antes de enviar.
- **Sem abortar disparo em andamento** — premissa de trabalho não verificada (doc do provedor de WhatsApp não deu pra confirmar); vira pergunta aberta no backlog final.

---

## 6. WhatsApp — regra central

- **Quase tudo é template pré-aprovado**, não mensagem livre — porque nossos disparos são disparados por evento de backend (Pix, apuração), não por conversa em andamento.
- **Mapeamento de categoria:** recovery de Pix e confirmação de título → **Utility** (nunca pode ser limitado por frequência). Resultado do sorteio → Utility ou Marketing (se empurrar recompra junto). Campanha semanal/mensal → **Marketing** (sujeita a cap de frequência, conta pra FTD).
- **CRM tem tela própria de status de template** (rascunho → aprovação → aprovado/rejeitado → nota de qualidade) — não assumimos que o provedor de WhatsApp abstrai isso.
- **Múltiplos números/BSP possíveis** — métrica de qualidade/entrega precisa ser por número, não só agregada.
- **Sem inbox de WhatsApp no CRM** — conversa de ida e volta fica no WhatsApp Business App normal; só o fato de ter respondido vira evento no log.
- **Editor de asset (Popup/Email):** HTML travado com o desenvolvedor, operador só troca campos simples (texto/imagem/link) — confirmado via captura de um CRM SaaS de referência. WhatsApp é exceção: só preenche variável dentro do template já aprovado pela Meta.

---

## 7. Jornadas do dia-1

Três jornadas, confirmadas como as únicas do dia-1:

1. **Pix gerado → não pago** (recovery, SLA 15min)
2. **Confirmação de título** pós-compra (artefato legal/confiança, não é opcional)
3. **Resultado do sorteio** → ganhador/não-ganhador → recompra

Nenhuma das três gera FTD (a métrica-norte) — aquisição vem da **campanha semanal/mensal agendada**, não de jornada automatizada.

**Console "Dia de Sorteio" → rebaixado a ação contextual (24/08, briefing visual):** não é mais área de menu nem tela permanente. No dia do sorteio, o card "Dias até apuração = 0" na Home abre um overlay guiado: confirmar extração da Loteria Federal → apurar ganhadores → disparar pagamento (SLA 24-48h) → publicar prova social. Concluir a apuração dispara a jornada de resultado (Fluxo 3). *(Ajuste anterior no mesmo dia: "lançar recompra" já havia sido removido — recompra roda pela jornada de resultado e pela campanha agendada.)* Cada passo reusa o que já existe (motor de segmento, painel de custo, gate de compliance) — não é sistema paralelo.

**Monitor de Pix → rebaixado a ação contextual (24/08, briefing visual):** sem área de menu. O alerta de Pix na Home detecta o problema; clicar nele abre o detalhe em tempo real (lendo o event store) — gerados/pagos/expirados/travados, ritmo esperado vs atual, e a lista dos travados com ação de reenvio. Continua pegando falhas de "nada está acontecendo" (gateway caiu) que jornada automatizada não detecta. **Menu final: 6 áreas** — Home · Clientes · Segmentos · Campanhas · Jornadas · Templates.

---

## 8. Fora de escopo (descartado)

- Raspadinha — 100% fora, sem placeholder no modelo (regras de negócio e status regulatório indefinidos).
- Tela própria de performance de afiliado — fica no painel do fornecedor da plataforma de vendas; só entra atributo de segmentação.
- Inbox (central de notificação in-app) e Push — sem app pra hospedar.
- RFM Analysis / Value Score / Reports nativos de CRM SaaS de referência — o cálculo fica, só a tela dedicada é descartada (já vive no perfil/segmento/home).
- "Common cases segment" — atalho, não capacidade nova, dispensável.
- Gamificação, pontos, níveis, torneios — sem equivalente no produto.

---

## 9. Segmentação

- **Visual por padrão + toggle "ver como SQL"** — mesma regra, não dois sistemas.
- **User state** e **Behavioral** já cobertos (tabelas batch + event store).
- **CSV import** — gap real, adicionar (lista manual, ex: export do fornecedor da plataforma de vendas ou escalação de suporte; mapeia pra CPF, passa pelo rail de compliance igual a qualquer outro segmento).
- **CSV export** — também adicionar (baixar segmento filtrado com seletor de colunas), visto em dashboard real do seu dev.

---

## 10. Categoria de campanha

- **Marketing vs Operational**, confirmado necessário (mesma distinção do Utility/Marketing do WhatsApp, §6, exposta como 1 campo por campanha). Operational nunca é limitado por frequência e fica fora do KPI global de FTD; Marketing é limitado e conta pra FTD.

---

## 11. Prova de conceito do seu dev

Duas plataformas próprias (um app de grupos e um dashboard de Meta Ads/afiliados) já construídas pelo mesmo dev que fará nosso CRM, em cima de base de CRM SaaS, com layout totalmente diferente — prova que o blueprint não precisa imitar visual do CRM de referência.

Padrões adotados de lá: coluna "Seg. Anterior → Variação → Seg. Atual" (mostrar subida/descida de RFM entre ciclos); export de CSV com seletor de colunas; grid de cards por cliente ordenável.

Métricas validadas por lá: Netcash = nossa "margem por edição"; Vol. Saques = nosso "payout ratio". GGR/Turnover não têm equivalente (conceito de aposta repetida) — descartados.

---

## 12. Perguntas em aberto (viram `Q-U*` no backlog final)

- provedor de WhatsApp permite abortar/pausar um disparo em andamento? — não verificado.
- provedor de WhatsApp já resolve o status de template do WhatsApp, ou o CRM precisa de tela própria mesmo assim? — não verificado.
- **Definição do "ROI atual" da Home (24/08):** (a) retorno sobre gasto de marketing (exige gasto de Meta Ads vindo do fornecedor da plataforma de vendas — dependência de integração) ou (b) margem da edição (faturamento − prêmio − custos)? — David ainda não definiu.

---

## Próximo passo

Se tudo isso bater com o que você tem em mente, sigo pra escrever `02-ENTITY-MODEL.md` e `03-DATA-CONTRACT.md` em cima dessas decisões.
