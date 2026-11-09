> Versão pública sanitizada: números de negócio, nomes de pessoas, citações de fontes privadas e parceiros foram substituídos por marcadores ([valor], [n], [x%], papéis).

Evidence tags used throughout: **[E]** documented (platform docs, methodology-bearing survey, official/regulatory source) · **[C]** operator consensus, no hard data behind it · **[I]** my inference. Untagged claims should be treated as errors — flag them. Where sources disagree, both readings are shown rather than one being picked.

Scope locked for this run: offer-agnostic (branches by category where it matters), ticket **≤ R$ [valor]**, Brazil, classes C/D, 10 videos/day sustained 90 days.

---

## A. SÍNTESE

1. **[E]** Revenue-per-video is not what any platform ranks on. TikTok's, Instagram's and YouTube's own documentation describe ranking by completion, watch time, and send/share behavior — never by downstream purchase. Optimizing for their signals and optimizing for your revenue are related but not identical goals, and the gap between them is exactly Block 4 of this research.
2. **[E]** Kwai is not an optional fourth platform for this audience — it's arguably the primary one. [x%] of classes D/E have it installed vs. [x%] of A/B (Mobile Time/Opinion Box, n=2,068, Nov 2023, via Aos Fatos), yet it has the thinnest official algorithm documentation of the four.
3. **[E]** Instagram's strongest reach signal to non-followers is DM sends, weighted roughly 3–5x a like (head do Instagram, reported consistently across creator-facing channels since Jan 2025). A hook built to be *forwarded to one specific person* — "manda isso pra sua mãe" — is structurally different from one built to be liked.
4. **[E]** The median Pix transaction in Brazil is R$ [valor], not the R$ [valor] average (Banco Central, 2025 data). The mean is dragged up by a small number of large transfers. A ≤R$ [valor] offer sits comfortably inside what this population already pays via Pix routinely — you are not asking for an unusual amount of trust.
5. **[E]** Pix passed credit cards as Brazil's leading e-commerce payment method in H1 2025 ([x%] of paid orders). Checkout should default to Pix-first copy and Pix-first CTA, not "parcelamos em 12x" — that framing fits a higher ticket than this offer.
6. **[E]** Six in ten Brazilians who start a WhatsApp purchase have abandoned one at some point (Opinion Box, n=1,126, Jun 2025). WhatsApp is a qualification and trust layer, not a reliable closing surface by itself — plan for leakage between video click and paid conversation, and don't blame the video for a WhatsApp-side drop.
7. **[E]** When two offers look equivalent, shipping cost — not price — is the top tie-breaker ([x%], Opinion Box). At this ticket size, "frete grátis" or shipping bundled into the price likely outperforms shaving the price further.
8. **[E]** 13º salário and Bolsa Família both run on known, dated calendars (NIS-digit payout schedule; 13º split roughly late-Nov/mid-Dec, ~R$ [valor] injected in 2025, retail up [x%] in December in São Paulo). This gives a real annual and monthly rhythm to test scale-up against, not a flat run rate.
9. **[I]** "Viral ≠ conversion" is repeated constantly by operators but is barely documented publicly at the organic-short-form, low-ticket level. Meta/Kantar's own lift studies (56,984 creatives, 1,295 campaigns, 13.1bn impressions) measure brand and sales lift for large tracked advertising campaigns — not what you're running. Any specific "X views ≠ Y sales" ratio circulating online is operator folklore, not measured fact, and this document treats it as such.
10. **[E]** Regulatory risk in your likely categories (health, income, food) is actively tightening in Brazil right now, not settled. ANVISA opened a formal review of RDC 96/2018 and RDC 24/2010 in August 2026 specifically citing influencer marketing; Meta only loosened its before/after imagery rule in July 2026 while keeping outcome-promise claims banned. This is live ground — re-check policy pages monthly, not once.

---

## B. O SISTEMA

Nine layers, chained. Each layer has one decision rule. Do not skip a layer to save time — most production failures in volume operations trace back to layer 4 (gancho) being written before layer 2 (subgrupo/tensão) actually exists.

**Oferta → Subgrupo/Tensão → Ângulo → Gancho → Estrutura de roteiro → Prova → CTA → Métrica de leitura → Regra de iteração**

### 1. Oferta
Classify before anything else — CTA design and platform-risk profile both depend on it.

| Categoria | Checkout | Implicação principal |
|---|---|---|
| Produto físico | Pix/cartão direto | Risco de política mais baixo; demonstração > depoimento |
| Infoproduto | Pix/cartão digital | Na faixa ≤R$ [valor] provavelmente uma isca (tripwire), não o produto principal — trate como tal |
| Lead via WhatsApp | Sem checkout público | Métrica de leitura muda inteiramente: não é CTR, é taxa de resposta na conversa |

**Regra:** se você ainda não sabe em qual das três está, não passe para a camada 2. A oferta define qual das ramificações abaixo você segue no resto do documento.

### 2. Subgrupo/Tensão
O output do procedimento da Seção C — nunca uma suposição. **Regra de decisão:** nenhum gancho é escrito antes de existir um subgrupo nomeado com evidência (comentários reais, buscas reais, objeções reais). Um gancho sem subgrupo é um palpite fantasiado de estratégia.

### 3. Ângulo
A tensão do subgrupo transformada em uma afirmação testável: "[Subgrupo] acredita que [crença], mas [contradição/prova]." **Regra:** um ângulo por peça. Misturar duas tensões na mesma peça contamina a leitura de qual delas funcionou.

### 4. Gancho
Puxado do banco da Seção D, casado ao driver psicológico do ângulo. **Regra de decisão por posição no funil:**
- Público frio / testando ângulo novo → curiosidade, contradição (baixo risco de queimar audiência, alto poder de filtrar quem presta atenção)
- Ângulo já validado, escalando → prova social, demonstração (reforça o que já converteu, não reintroduz variável)
- Fechamento em sequência (retargeting, ou vídeo 2-3 de uma série sobre o mesmo ângulo) → preço, perda (funciona melhor com quem já viu a demonstração e a prova)

### 5. Estrutura de roteiro
Modular, ≤30s para tráfego frio (finalização = sinal de ranking #1 nas três plataformas com documentação pública — TikTok Newsroom [E], Instagram/head do Instagram [E], YouTube Ajuda [E]):

`Gancho (0–3s) → Agitação da tensão (3–8s) → Prova (8–15s) → Oferta + preço (15–20s) → CTA (20–25s)`

**Regra:** peças em sequência para público já aquecido podem passar de 30s; peças de teste em público frio, nunca.

### 6. Prova
Regra por categoria:

| Categoria | Prova que ranqueia mais alto | Por quê |
|---|---|---|
| Produto físico | Demonstração ao vivo, sem corte | Watch-time e completion recompensam continuidade; "mostrar funcionando" retém melhor que depoimento |
| Infoproduto | Prova social de pares (não celebridade) | Este público confia em prova social de pares, não de autoridade distante — ver Bloco 3 |
| Lead via WhatsApp | Prova de resposta real/rápida | Reduz o atrito que já causa 6-em-10 abandonos (Opinion Box) antes mesmo de começar |

### 7. CTA
| Categoria | CTA primário | CTA de teste |
|---|---|---|
| Produto físico / infoproduto | Compra direta (link na bio, Pix) | Comentário com palavra-chave ("EU QUERO") |
| Lead via WhatsApp | WhatsApp, mas com preço/condição já dito no vídeo | Sem pré-qualificação no vídeo → maior abandono na conversa |

**Regra:** nunca mande para WhatsApp sem ter dito o preço antes — pedir para "chamar no zap para saber o valor" é o padrão que mais alimenta o abandono de 6-em-10.

### 8. Métrica de leitura
Não é views. Ver Seção F para o painel completo — a regra aqui é: **toda métrica lida antes da conversão em si precisa ser uma métrica que precede estatisticamente a compra**, não uma métrica de alcance.

### 9. Regra de iteração
Matar/manter/escalar por percentil dentro do próprio lote do dia (Seção F), com variação controlada — um elemento trocado por vez (Seção E).

---

## C. PROCEDIMENTO DE DESCOBERTA DE ÂNGULO

Uma semana, executável, sem depender de uma tese pronta. Fontes nomeadas em cada dia. **[C]** — este é um procedimento operacional (método reconhecido de pesquisa qualitativa aplicada a marketing), não um dado publicado; a estrutura é minha síntese, as fontes de dados são reais e nomeadas.

**Dia 1 — Varredura de comentários**
Fontes: avaliações de produto no Mercado Livre e Shopee de itens iguais/adjacentes ao seu (1–3 estrelas = mina de objeções; 4–5 estrelas = a linguagem de valor que o próprio cliente usa), seções de comentários de concorrentes no Instagram/TikTok (ordenar por "mais relevantes" *e* "mais recentes" — pegam reações diferentes), comentários em vídeos de unboxing/review no YouTube da categoria.
Ação: cole os comentários crus numa planilha, marque cada um com (a) tipo de objeção, (b) resultado desejado, (c) registro emocional (frustração / aspiração / medo / orgulho).

**Dia 2 — Varredura de intenção de busca**
Fontes: "Pesquisas relacionadas" e "As pessoas também perguntam" do Google para os termos da categoria; autocomplete da barra de busca do TikTok e do Kwai (digite devagar, print da sugestão); autocomplete do YouTube para "[categoria] não funciona", "[categoria] vale a pena", "[categoria] reclame aqui".
Ação: agrupe as variações de busca em afirmações de crença ("as pessoas acham que X não funciona porque Y").

**Dia 3 — Captura de objeção em venda ao vivo**
Fontes: lives de venda de concorrentes/vendedores adjacentes (Instagram, TikTok, Kwai), status/canais de WhatsApp de vendedores do nicho, grupos de Facebook de bairro/cidade ou de nicho, ReclameAqui de marcas concorrentes (dado estruturado de objeção com resposta da empresa visível — raro e valioso).
Ação: registre a frase textual, como foi dita/digitada — vira material de gancho porque já está na língua do público.

**Dia 4 — Segmentar e pontuar**
Junte tudo dos Dias 1–3. Agrupe em 3–5 subgrupos candidatos por crença/tensão compartilhada (não por rótulo demográfico). Para cada subgrupo, pontue: (a) frequência — quantas vezes a tensão aparece nas três fontes, (b) intensidade — força da linguagem emocional usada, (c) acionabilidade — sua oferta resolve isso de forma crível em ≤30s?

**Dia 5 — Rascunhar ângulos**
Para cada subgrupo que passou no corte do Dia 4, escreva uma frase: "[Subgrupo] acredita que [crença], mas [contradição/prova]." Máximo 2 ângulos concorrentes por subgrupo.

**Dia 6 — Casar gancho e roteirizar**
Puxe 2–3 tipos de gancho por ângulo (Seção D), rascunhe os roteiros na estrutura modular da Seção B, camada 5.

**Dia 7 — Produção-piloto e go/no-go**
Grave o menor lote viável (mínimo 2 variantes de gancho por par subgrupo×ângulo), revise contra a varredura de risco (Seção G) antes de publicar. **Critério de saída:** você precisa sair da semana com ≥3 pares subgrupo/ângulo com roteiros distintos prontos para entrar na matriz de segunda-feira (Seção E). Se não tiver 3, repita os Dias 1–3 com uma rede mais estreita (um concorrente só, um marketplace só) em vez de avançar com achismo.

---

## D. BANCO DE 30 GANCHOS

Originais, escritos para este documento — não coletados de peças existentes. Classificados por tipo psicológico. Os "subgrupos prováveis" abaixo são **arquétipos ilustrativos derivados da evidência do Bloco 3** (desconfiança de checkout, prova social de pares, sensibilidade a parcela, sazonalidade de renda) — **não são o resultado real da Seção C**. Substitua-os pelos subgrupos que sua própria semana de descoberta encontrar; usá-los como se fossem definitivos seria exatamente a "invenção de tese" que este documento foi pedido para evitar.

### Por tipo — quando funciona, quando queima

| Tipo | Quando funciona | Quando queima audiência |
|---|---|---|
| Contradição | Público já ouviu a versão "oficial" da categoria e está cansado dela | Usado toda semana, vira previsível e perde o efeito de surpresa |
| Perda | Perto de datas de pagamento/urgência real de estoque | Usado sem prazo real — mentira de escassez é detectada e destrói confiança |
| Demonstração | Produto físico com resultado visível em segundos | Produto sem resultado visualmente imediato — a demonstração falha em entregar o que o gancho prometeu |
| Prova social | Subgrupo desconfiado de propaganda tradicional | Prova social genérica ("todo mundo ama") sem rosto/contexto real soa fabricada |
| Curiosidade | Abre um vídeo de teste em público frio | CTA fraco depois — abre a curiosidade e não entrega, público não volta |
| Acusação | Subgrupo que já se sente enganado por concorrentes/mercado | Acusação sem prova em seguida vira reclamação genérica, perde credibilidade |
| Preço | Momento de decisão, público já viu prova | Usado como primeiro gancho de um público totalmente frio, sem tensão construída antes |

### Os 30 ganchos

**Contradição**
1. "Todo mundo fala que isso é caro. Deixa eu te mostrar quanto custa por dia." — *cético de preço*
2. "Você jura que sabe usar isso certo? A maioria tá fazendo errado." — *cansado de ser enganado*
3. "Isso aqui não é pra quem tem dinheiro sobrando. É justamente pra quem não tem." — *decisor por parcela*
4. "Pararam de vender isso na loja física. Adivinha por quê." — *cético de preço*

**Perda**
5. "Enquanto você pensa se compra, o preço já subiu duas vezes esse mês." — *impulsivo por urgência*
6. "Isso aqui só tem estoque até [dia]. Depois volta pro preço normal." — *impulsivo por urgência*
7. "Se você não resolver isso agora, mês que vem vai te custar o dobro do seu tempo." — *decisor por parcela*
8. "Quantas vezes você já perdeu uma promoção por 'depois eu vejo'?" — *impulsivo por urgência*

**Demonstração**
9. "Olha o que acontece quando eu faço isso na frente de vocês, sem cortar." — *cansado de ser enganado*
10. "Coloquei R$X aqui e o resultado foi esse — sem trocar de cenário." — *cético de preço*
11. "Deixa eu testar isso ao vivo, do jeito que você vai usar em casa." — *cansado de ser enganado*
12. "Um copo de água, isso aqui, e olha o que sobra depois de 10 segundos." — *cético de preço*

**Prova social**
13. "Minha vizinha me mandou isso ontem, juro que não é publi." — *aspiracional por pares*
14. "Fui perguntar no grupo do bairro se vale a pena — foi isso que responderam." — *aspiracional por pares*
15. "Não sou eu que tô falando, é o comentário de quem já comprou." — *cansado de ser enganado*
16. "Toda mãe do meu prédio já tem um desses. Fui a última a saber." — *aspiracional por pares*

**Curiosidade**
17. "Ninguém me contou isso antes de eu comprar o meu." — *cético de preço*
18. "Tem um detalhe nisso aqui que muda tudo — e quase ninguém repara." — *aspiracional por pares*
19. "Por que será que esse vídeo é apagado toda vez que eu posto?" — *cansado de ser enganado*
20. "Isso não devia funcionar. Mas funciona. Deixa eu te mostrar." — *cético de preço*

**Acusação**
21. "Vocês tão pagando caro por isso e nem sabem." — *cético de preço*
22. "Se o seu [concorrente] faz assim, alguém te enganou." — *cansado de ser enganado*
23. "Loja grande não vai te contar isso, porque perde venda." — *cansado de ser enganado*
24. "Você já deve ter caído nessa pelo menos uma vez. Dessa vez eu vou te mostrar como não cair de novo." — *cansado de ser enganado*

**Preço**
25. "Menos que um lanche por dia — é literalmente isso que custa." — *decisor por parcela*
26. "R$X à vista no Pix, sem enrolação, sem letra miúda." — *decisor por parcela*
27. "Cabe no seu bolso? Vou fazer a conta na sua frente." — *decisor por parcela*
28. "Preço de hoje. Amanhã eu não garanto." — *impulsivo por urgência*
29. "Custa menos do que você imagina — o problema é que ninguém mostra o preço antes de te prender no vídeo." — *cético de preço*
30. "Comparei com o que tá vendendo do lado, o preço fala por si." — *decisor por parcela*

---

## E. MATRIZ DE PRODUÇÃO SEMANAL

70 peças/semana (10/dia) distribuídas para gerar **aprendizado**, não só volume. **[C]** — proporções abaixo são ponto de partida razoável de teste direto-resposta; ajuste com os dados reais depois de 2–3 semanas (ver Seção F).

Três baldes por dia:
- **Teste** — ≤1 variável nova por peça (gancho novo em ângulo validado, ou ângulo novo com gancho já comprovado — nunca os dois ao mesmo tempo)
- **Confirmação** — repete peças com sinal fraco-mas-promissor da semana anterior, público maior, para tirar a dúvida sobre ruído de aquecimento de algoritmo
- **Escala** — variação controlada (um elemento trocado: apresentador, cenário, prova visual) do vencedor confirmado

| Dia | Teste | Confirmação | Escala | Total |
|---|---|---|---|---|
| Segunda | 4 | 2 | 4 | 10 |
| Terça | 4 | 2 | 4 | 10 |
| Quarta | 3 | 3 | 4 | 10 |
| Quinta | 3 | 3 | 4 | 10 |
| Sexta | 2 | 3 | 5 | 10 |
| Sábado | 2 | 2 | 6 | 10 |
| Domingo | 2 | 2 | 6 | 10 |
| **Total** | **20** | **17** | **33** | **70** |

**Regra de distribuição:** dentro do balde Teste, nenhum ângulo recebe mais de 1 gancho novo por dia (isola a variável, Seção F). Dentro de Escala, a oferta em si varia no máximo por *enquadramento de preço* (à vista vs. "menos que X por dia") — não por produto, já que a operação tem ticket único ≤R$ [valor].

**[I]** Segunda e terça concentram mais Teste porque a semana está "fresca" — ainda não se sabe o que vai funcionar naquela leva; sexta a domingo concentram Escala porque, empiricamente em operações de resposta direta, o fim de semana costuma ter maior tempo de tela disponível para C/D (sem dado de plataforma específico para confirmar isso nesta pesquisa — tratar como hipótese a testar, não como fato).

---

## F. PAINEL DE DECISÃO

Nenhuma plataforma publica limiares absolutos de matar/manter/escalar — isso não existe como dado público **[E — ausência confirmada]**. O painel abaixo usa **limiares relativos (percentil dentro do próprio lote do dia)** em vez de números absolutos inventados, porque é a única forma honesta de comparar antes de você ter sua própria linha de base. **[C]** — prática padrão de teste em resposta direta, adaptada aqui.

| Etapa | O que mede | Quando já dá pra ler | Matar | Manter | Escalar |
|---|---|---|---|---|---|
| Retenção do gancho (retenção aos 3s) | Força do gancho | ~500 impressões (plataformas testam com audiência pequena primeiro — documentado para YouTube [E], generalizado como prática comum para TikTok/Reels/Kwai [C]) | Terço inferior do lote do dia | Dentro de ±[x%] da mediana do dia | Terço superior do lote do dia |
| Completion rate | Força do roteiro + prova | ~1.000–2.000 impressões | Terço inferior | ±[x%] da mediana | Terço superior |
| Salvar + Compartilhar (DM) | Sinal de empurrão algorítmico (Instagram pesa isso 3–5x mais que curtida [E]) | Mesma janela que completion | Abaixo da mediana do dia | Na mediana | Acima da mediana |
| Comentário com palavra-chave / clique no link/bio | Intenção de compra pré-conversão | Só é legível depois que a peça já passou pelos 3 filtros acima — ler isso cedo demais mistura ruído de alcance com intenção real | Sem comentários/cliques qualificados após atingir volume do funil acima | Alguns, abaixo do esperado pelo histórico | Acima do esperado pelo histórico da conta |
| Conversão (checkout ou fechamento no WhatsApp) | Receita real | **Por ângulo acumulado na semana, nunca por vídeo isolado no dia 1** — matar um ângulo pelo resultado de uma peça só confunde aquecimento de algoritmo com fracasso real | Ângulo sem nenhuma conversão após a semana inteira de exposição acumulada | 1 conversão isolada — não é sinal, é acaso; observar mais uma semana | Múltiplas conversões repetidas em peças diferentes do mesmo ângulo |

**Regra de honestidade estatística [I]:** com uma taxa de conversão de baixo ticket por impulso tipicamente pequena (evento raro), leia comentário/clique-qualificado como proxy antes de esperar volume suficiente de conversão real — mas nunca mate um ângulo só pelo proxy; o proxy orienta o que **escalar mais rápido**, a conversão real decide o que **matar**.

**Regra de conversão para migrar de limiar relativo para absoluto:** depois de ~2–3 semanas (≥1.400 peças cumulativas), você já tem linha de base própria — troque "terço inferior/superior do lote do dia" por números fixos calculados sobre a sua própria mediana histórica.

---

## G. OS 5 MODOS DE FALHA MAIS PROVÁVEIS

1. **Otimizar para views em vez de proxy de receita** — a armadilha que abre este documento. Sinal antecipado: número de views subindo enquanto taxa de comentário-com-palavra-chave e clique-qualificado ficam estáveis ou caem — o alcance está crescendo com o público errado.
2. **Queimar a conta em política de plataforma antes de achar o ângulo** — promessa de resultado/saúde/renda, mesmo sutil, sob risco regulatório ativo em 2026 (Bloco 8). Sinal antecipado: queda de alcance em peças que "parecem" dentro das regras — é sinal de que algo recente (mesmo peça diferente) já disparou um filtro silencioso.
3. **Confundir ruído de aquecimento de algoritmo com sinal real** — matar um ângulo no dia 1 com dado insuficiente (Seção F). Sinal antecipado: o mesmo ângulo varia muito de uma peça pra outra sem diferença estrutural entre elas — ainda está calibrando, não morto.
4. **Gargalo no WhatsApp comendo a conversão que o vídeo já gerou** — com abandono de base de 6-em-10 (Bloco 3), o vazamento pode estar depois do vídeo, não nele. Sinal antecipado: clique-para-bio/comentário-qualificado saudável, mas abertura/resposta no WhatsApp muito atrás disso — não culpe o gancho por um problema de atendimento.
5. **Fadiga de produção colapsando variação controlada em copiar-e-colar** — o sistema inteiro existe para gerar aprendizado, não só volume (Bloco 6). Sinal antecipado: nas vagas de Teste da matriz semanal, a mesma linha de gancho volta a se repetir semana após semana só trocando a oferta — quando isso acontece, o sistema parou de aprender e virou produção pura, exatamente o que ele foi desenhado para evitar.

---

## Fontes citadas [E]

- TikTok Newsroom — "How TikTok recommends videos #ForYou": https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you
- TikTok — Introduction to the recommendation system (Transparency Center): https://www.tiktok.com/transparency/en/recommendation-system
- YouTube Ajuda — "How YouTube recommendations work": https://support.google.com/youtube/answer/16089387?hl=en
- Head do Instagram, sinais de ranking do Instagram (jan/2025), agregado por múltiplas fontes de criadores — ver por ex. https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers
- Aos Fatos — "Perfis demográficos de apps mais populares no Brasil" (pesquisa Mobile Time/Opinion Box, n=2.068, nov/2023): https://www.aosfatos.org/noticias/apps-mais-populares-brasil/
- Instituto Locomotiva / Data Favela — poder de compra de favelas e periferias, n=16.500: via https://miriangasparin.com.br/2025/07/consumo-nas-favelas-e-maior-que-o-de-22-estados-brasileiros/ e https://samais.com.br/detalhe/reportagens/moradores-de-favelas-somam-quase-r-120-bilhoes-em-poder-de-compra
- Banco Central — estatísticas Pix 2025 (valor médio R$ [valor], mediana R$ [valor], [x%] das transações ≤R$ [valor]): via https://monitordomercado.com.br/noticias/416181-pix-movimenta-r-35-trilhoes-e-bate-recorde-em-2025-diz-bc/
- Pix ultrapassa cartão de crédito no e-commerce, H1 2025 ([x%] dos pedidos pagos): via https://babitonhela.com/blog/meios-de-pagamento-ecommerce/
- Opinion Box — Pesquisa WhatsApp no Brasil 2025 (n=1.126, jun/2025, margem 2,9pp): https://blog.opinionbox.com/pesquisa-whatsapp-no-brasil/ e materiais completos em https://materiais.opinionbox.com/pesquisa-whatsapp-no-brasil
- 13º salário 2025 — injeção de ~R$ [valor], calendário e impacto no varejo: https://www.mixvale.com.br/2025/04/03/antecipacao-do-decimo-terceiro-injeta-r-320-bilhoes-e-fortalece-varejo-e-turismo-antes-do-natal/
- CONAR — Código Brasileiro de Autorregulamentação Publicitária (edição vigente): http://conar.org.br/pdf/Codigo-CONAR-2025.pdf
- ANVISA — revisão da RDC 96/2018 e RDC 24/2010, publicidade de alimentos/medicamentos e marketing de influenciadores (ago/2026): https://sincofarmasp.com.br/2026/08/06/anvisa-aprova-abertura-de-processo-para-revisar-normas-da-propaganda-de-alimentos-e-de-medicamentos/
- Meta — Transparency Center, Health and Wellness ad standards (atualização jul/2026 sobre imagens antes/depois): https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/
- Meta + Kantar + CreativeX — "The New Era of Storytelling" (56.984 criativos, 1.295 campanhas, 13,1bi impressões): https://www.kantar.com/north-america/company-news/the-new-era-of-storytelling

**Nota de auditoria:** as citações acima foram obtidas via busca e extração automatizada (WebSearch/WebFetch) em 11/08/2026, com paráfrase de conteúdo agregado por fontes secundárias em vários casos (marcado no texto). Antes de basear decisões de investimento relevante nelas, recomenda-se confirmar manualmente os números do Banco Central e do CONAR/ANVISA diretamente nas fontes primárias — os agregadores de mercado (blogs de growth, SaaS de social media) que citam o head do Instagram e o algoritmo do TikTok não são a fonte primária, são reportagem sobre ela.
