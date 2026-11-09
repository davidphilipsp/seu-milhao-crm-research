# PRD — Seu Milhão

> Versão pública sanitizada. Foram removidos: números de negócio (preço, prêmio, custos, LTV, conversão, contagens), citações de conversas internas, nomes de pessoas, fornecedores e parceiros, domínios e dados de contas. As seções que dependiam de fontes confidenciais (reunião com um player do mercado; timeline e papéis do time) foram omitidas. O método, a estrutura, as perguntas e as decisões foram mantidos. Pessoas aparecem por papel.

**Versão:** 0.1 (documento vivo) · **Data:** 14/08/2026 · **Status:** Draft — base de conhecimento + backlog de pesquisa

> **Natureza deste documento.** Este não é um PRD de especificação fechada. É o **hub de conhecimento estratégico** do Seu Milhão: consolida o que se sabe, marca o que se supõe, expõe o que está em aberto e transforma cada lacuna em **pergunta de pesquisa acionável ligada a uma decisão pendente**.

**Convenção de evidência (obrigatória neste projeto):**
- **[E]** documentado — fonte primária lida diretamente, citável verbatim
- **[C]** consenso/padrão — repetido entre múltiplas fontes, sem fonte única atribuível
- **[I]** inferência — plausível, não observada diretamente

Afirmações sem tag são estruturais/organizacionais deste PRD. As tags aparecem onde ajudam a calibrar confiança, não em toda frase.

**Fontes deste documento:**

| # | Fonte | Natureza |
|---|---|---|
| F1 | Briefing de reunião com um player do mercado | Relato verbal, **dados auto-reportados, não auditados** (conteúdo omitido nesta versão) |
| F2 | Extração da conversa interna do time (fundadores/dev) | Export de chat, cobertura integral (privado) |
| F3 | Extração da conversa com o fornecedor da plataforma | Export de chat, cobertura integral (privado) |
| F4 | Pesquisa Meta Ad Library — nicho sorteio BR | Leitura de anúncios ativos na biblioteca pública |
| F5 | Pesquisa TikTok Creative Center BR | Sessão assistida (relatório e artefatos não publicados) |
| F6 | Pesquisa short-form direct sales BR | Fontes públicas + síntese metodológica |

---

## 1. Sumário executivo

**O produto.** Seu Milhão é um **título de capitalização regulado pela SUSEP** [E, F2] distribuído digitalmente: o cliente paga via Pix, recebe um título com série e número da sorte, e concorre em sorteio apurado por **extração da Loteria Federal** [E, F2]. Há camadas de premiação modeladas — **âncora, intermediário e instantâneo** [E, F2] — sendo a instantânea materializada como **raspadinha** [E, F2/F3]. Não é rifa informal: o número da sorte está condicionado a uma transação financeira real, que é exatamente o que enquadra o produto sob a SUSEP [E, F1].

**Onde o projeto estava.** Havia um protótipo navegável construído sobre a plataforma de um fornecedor (site builder white-label + checkout + painel de afiliados + tracking backend + produção de criativo). Marca, perfis sociais e contas de mídia estavam prontos [E, F2]. Três pesquisas de mercado formais estavam concluídas [E, F4/F5/F6].

**O diagnóstico central.** O time tinha **execução comercial muito à frente da definição de produto** [I, F2]. Marca, domínios e contas de mídia foram fechados em poucos dias, enquanto **preço, valor de prêmio, stack de banco, gateway de Pix e o emissor do título seguiam indefinidos** [E, ausência confirmada em F2 e F3]. O maior risco identificável não era regulatório nem técnico: era de **sequenciamento** — contas de mídia prontas para comprar tráfego contra um produto cujo checkout ainda não tinha economia definida.

**As cinco tensões que este PRD existe para tornar visíveis:**

1. **Regulatório não resolvido no ponto que mais importa** — a mecânica de "combo" tinha dúvida SUSEP declarada, sem resolução registrada [E, F2].
2. **LGPD ausente da discussão** — pediu-se CPF + dados pessoais completos + eventos de Pix via webhook para um CRM próprio, e **ninguém mencionou base legal, minimização ou contrato controlador/operador** [E, ausência confirmada em F3].
3. **Concentração de risco no fornecedor** — o fornecedor detinha plataforma, checkout, dados transacionais, painel de afiliados, tracking e criativo; o time detinha marca, domínio, design e rede de influenciadores [I, F3].
4. **Desconexão entre pesquisa formal e benchmark real** — os concorrentes das pesquisas **não apareciam** nas conversas do time; o benchmark observado na prática era outro concorrente (Viva Sorte), escolhido por critério estético, não analítico [E + I, F2 × F4].
5. **Economia do produto em branco** — preço, prêmio âncora e emissor nunca foram mencionados [E, ausência em F2 e F3].

**O que já é ativo real.** O **schema de dados** de 7 domínios é bom para o estágio [I, F2]: modela prova social de ganhador, atribuição de creator e réguas de CRM como cidadãos de primeira classe desde o dia 1. Isso casa com a lacuna que a própria pesquisa identificou no setor: anúncios de reativação/CRM são raríssimos na varredura do Meta Ad Library [E, F4].

---

## 2. Contexto e definição do produto

### 2.1 O que é um título de capitalização

Título de capitalização é um produto financeiro em que o consumidor paga um valor e recebe (a) direito de participação em sorteios e (b) eventual devolução de parte do capital ao fim de um prazo, conforme a modalidade contratada. É **produto regulado pela SUSEP** (Superintendência de Seguros Privados) e só pode ser emitido por **sociedade de capitalização autorizada** [C]. Isso implica: produto registrado, condições gerais depositadas, e um emissor autorizado por trás da operação comercial.

> **[I] Ponto de atenção estrutural:** o Seu Milhão, como desenhado, é a **camada de distribuição e marca**. O emissor autorizado não estava nomeado em nenhuma fonte [E, ausência]. Sem identificá-lo, várias decisões de produto (preço, série, estrutura de prêmio, "combo") não são decidíveis pelo time sozinho — são negociáveis com o emissor dentro do que o produto registrado permite.

### 2.2 Por que SUSEP e não rifa

| Elemento | Rifa/sorteio informal | Título de capitalização (Seu Milhão) |
|---|---|---|
| Origem do número da sorte | Compra de bilhete, sem produto financeiro subjacente | **Condicionado a uma transação financeira** que adquire o título [E, F1] |
| Regulador | Nenhum / autorização de sorteio, conforme o caso [C] | **SUSEP** [E, F1/F2] |
| Emissor | Promotor do sorteio | Sociedade de capitalização autorizada [C] |
| Titularidade | Portador do bilhete | **CPF como chave obrigatória de titularidade** [E, F2] |
| Apuração | Livre | **Extração da Loteria Federal** [E, F2] |

> **⚠ Ressalva de proveniência.** As afirmações regulatórias do schema (CPF obrigatório pela SUSEP; idade mínima) entraram no artefato de referência **através de um schema gerado com assistência de LLM** e aprovado sem revisão campo a campo nem validação jurídica independente [E + I, F2]. São plausíveis, mas **estavam sendo tratadas como fato sem fonte primária**. Isso vale como risco (§6.2) e como pergunta de pesquisa (Q-R1).

### 2.3 Mecânica do produto — o que estava definido

| Elemento | Definição | Tag | Fonte |
|---|---|---|---|
| Pagamento | **Pix** (estados: gerado / pago / expirado / estornado) | [E] | F2, F3 |
| Identificação | CPF como chave única; idade mínima | [E] | F2 |
| Bilhete | `série` + `número da sorte` por título | [E] | F2 |
| Apuração | Extração da Loteria Federal vinculada por edição | [E] | F2 |
| Camadas de prêmio | Âncora / intermediário / instantâneo | [E] | F2 |
| Gratificação instantânea | Raspadinha (evento `raspadinha jogada`), em duas versões: co-branded com influenciador e de marca própria | [E] | F2, F3 |
| SLA de pagamento de prêmio | Teto regulatório com meta interna bem mais curta | [E] | F2 |
| Engajamento | Lives (evento `live assistida`) | [E] | F2 |
| Distribuição | Programa de afiliados/creators com código, contrato, comissão, atribuição, postbacks | [E] | F2, F3 |
| Checkout | Pacotes de títulos, com um destacado como "mais vendido" | [E] | F3 |
| **Preço / ticket** | **NUNCA DEFINIDO** | [E] ausência | F2, F3 |
| **Valor do prêmio âncora** | **NUNCA DEFINIDO** (o nome da marca cria expectativa) | [E] ausência / [I] leitura | F2 |
| **"Combo"** | Mecânica com **dúvida regulatória SUSEP declarada e não resolvida** | [E] | F2 |
| **Emissor SUSEP** | **NÃO NOMEADO** | [E] ausência | F2, F3 |

**[I]** O desenho é uma **cópia estrutural do padrão do setor** mapeado em F4: Pix de ticket baixo → título com número da sorte → sorteio pela Loteria Federal → camada instantânea para retenção D+0 → prova social de ganhador → distribuição via creators. **Nada aqui é diferenciação; é paridade competitiva.** A única possível inovação de oferta no corpus é o **"combo"** — justamente o item travado por dúvida regulatória.

### 2.4 Público-alvo

**[I]** O time tinha tese de público classes C/D/E e a testava contra nomes de marca, não contra dado.

**[E, F6]** Contexto de mercado que sustenta o ticket baixo (fontes públicas do Banco Central): a mediana de transação Pix é baixa, bem abaixo da média, e o Pix passou o cartão como principal meio de pagamento no e-commerce brasileiro. Um ticket baixo está dentro do que essa população já paga por Pix rotineiramente.

---

## 3. Inteligência estratégica de terceiro (omitida)

Esta seção registrava dados **auto-reportados verbalmente por um player do mercado** (stack de CRM, custo de disparo, métricas de aquisição, estrutura de oferta, régua de CRM, mídia paga e copy). É conteúdo confidencial de terceiro e não auditado, por isso foi omitido nesta versão. A regra de uso continua valendo: **número auto-reportado por terceiro nunca entra como [E] simples**, só como [E, auto-reportado], com aviso de qualidade de dado.

## 4. Estado do time (omitido)

Timeline, papéis e concentração de decisão do time foram omitidos por envolverem pessoas e conversas privadas. O diagnóstico que sai desta seção está no §1 (execução à frente da definição de produto) e no §6.

---

## 5. Base de conhecimento — referências, tecnologias e ferramentas

### 5.1 Stack e ferramentas catalogadas (por camada)

| Camada | Situação | Tag |
|---|---|---|
| **Plataforma** | Fornecedor white-label: site builder + checkout modular (customização restrita a cores) + afiliados + automação (n8n) + criativo | [E] |
| **Domínio / DNS** | Domínio principal registrado e apontado; transferência de registrador decidida e não confirmada; DNSSEC sem confirmação | [E] / [I] |
| **Ingestão de dados** | **Webhook** ou **n8n direto** (acesso ao banco completo do fornecedor **negado**) | [E] |
| Documentação de API | Citada em call, **nunca entregue** | [E] |
| **Banco próprio** | Conceito definido; **nenhum banco, cloud, linguagem ou framework escolhido** | [E] ausência |
| Event store | Separado do transacional, *porque é o que alimenta as réguas* | [E] |
| **CRM** | **Próprio**, não de mercado | [E] |
| **Tracking** | PostBack/Conversions API (Meta/TikTok/Google) perguntado ao fornecedor, **não confirmado**; sobreposição com um sistema próprio de tracking | [E] + [I] |
| **Afiliados** | Painel pronto na plataforma, não ativado | [E] |
| **Mídia paga** | Contas TikTok, Meta e Google criadas, **bloqueadas pela emissão do CNPJ** | [E] |
| **Gateway de Pix** | **Nunca definido** | [E] ausência |
| **Emissor SUSEP** | **Nunca nomeado** | [E] ausência |
| **IA regulatória** | IA treinada em normas SUSEP, encomendada, **entrega não confirmada** | [E] |

### 5.2 CRM próprio vs. plataforma de mercado

**[I] Tensão a resolver:** a decisão de "CRM próprio" foi tomada antes de conhecer o padrão de operação de disparo de um concorrente que usa plataforma de mercado, e não há registro de reavaliação. Construir régua de disparo WhatsApp própria vs. contratar plataforma estabelecida é uma decisão de build-vs-buy de peso, tomada em uma frase, sem análise comparativa registrada (Q-P9).

### 5.3 Schema de dados — 7 domínios [E, F2]

| Domínio | Campos | Driver declarado |
|---|---|---|
| **Cliente** | CPF (chave única), nome, WhatsApp, e-mail, data de nascimento, CEP/cidade, status KYC, **opt-ins LGPD por canal**, data de cadastro, origem (UTM/afiliado/creator) | CPF para titularidade; idade mínima; CEP para segmentação regional e entrega de prêmio |
| **Título/Pedido** | ID, série, número da sorte, valor, status (carrinho / Pix gerado / pago / expirado / estornado), timestamp por transição, método de pagamento, campanha vinculada | Máquina de estados de checkout com timestamp por transição |
| **Sorteio** | Edição, data, **extração da Loteria Federal vinculada**, prêmios, status, resultados públicos | Vínculo com apuração oficial |
| **Prêmio/Ganho** | Cliente, título, valor, tipo (âncora/intermediário/instantâneo), status de pagamento, **autorização de imagem, conteúdo gerado** | Onde mora o SLA de pagamento |
| **Afiliado/Creator** | Código, contrato, comissão, atribuição de vendas, postbacks | Distribuição via creators |
| **Eventos comportamentais** | Pageview, checkout iniciado, Pix gerado, **raspadinha jogada**, **live assistida** | *Stream de eventos separado do transacional, porque é o que alimenta as réguas* |
| **Interações CRM** | Cada disparo: canal, template, campanha, status de entrega, clique, conversão | *Essencial para atribuição e para não queimar contato com frequência excessiva* |

**[I] Três leituras:**
1. **`opt-ins LGPD por canal` existe no schema** — a LGPD está presente como *campo de banco*, mas nunca como discussão de base legal, minimização ou contrato de operador (ver §6.2).
2. `autorização de imagem` + `conteúdo gerado` no domínio Prêmio mostra que **prova social de ganhador é ativo de primeira classe** — coerente com F4 (prova de pagamento nomeada é um dos formatos dominantes do setor).
3. `tipo (âncora, intermediário, instantâneo)` é a pegada de uma **economia de prêmio deliberada** — prêmio grande para chamada de mídia, médios para credibilidade de frequência, instantâneos para retenção D+0. Sofisticado, e **nunca debatido** — sugere que veio pronto da mesma sessão de LLM que gerou o schema.

### 5.4 Concorrentes: pesquisa formal vs. observação informal

| Concorrente | Pesquisa formal (F4) | Conversas do time (F2/F3) | Assinatura de formato |
|---|---|---|---|
| **Apcap da Sorte** | Sim — dona do formato "prova de pagamento nomeada"; anúncio mais persistente da varredura; **único anúncio de reativação/CRM** | Nunca citado | Prova de pagamento nomeada |
| **Familhão** | Sim — assinatura própria de **documentário/revelação** (visita-surpresa), com apresentador de TV; bundle com streaming | Nunca citado | Documentário/revelação |
| **Pix do Milhão** | Sim — oferta/preço direto, prova social institucional de escala, ligação reencenada | Citado só como semente de brainstorm de domínio | Preço + prova social de escala |
| **SBT Prêmios** | Incluído no escopo da varredura | Nunca citado | — |
| Anunciante com apresentador de TV | Ângulo acusação, alta velocidade de teste de variantes | Nunca citado | Acusação |
| Afiliado de entretenimento | Curiosidade minimalista, longa permanência no ar | Nunca citado | Curiosidade minimalista |
| **Viva Sorte** | **Não aparece na pesquisa formal** | **Eleito o melhor benchmark** por critério estético | **Desconhecida — nunca analisada** |
| Fundador de um concorrente | Não | Publicação compartilhada como referência | **Founder-as-face** |

> **[I] O problema não é que o benchmark escolhido seja ruim — é que ninguém sabe se é bom.** Ele foi escolhido por varredura visual pessoal, **não por análise de formato, persistência de criativo ou economia de oferta**. Ao mesmo tempo existia uma pesquisa rigorosa com taxonomia de 8 formatos e ranking de persistência que **não foi referenciada nas conversas**. Há conhecimento produzido que não circula. Este PRD tenta fechar esse ciclo.

### 5.5 Achados de mídia que já orientam decisão

| Achado | Tag | Fonte | Implicação para o Seu Milhão |
|---|---|---|---|
| **Três formatos dominam o que está no ar**: endereçamento direto emocional, oferta/preço direto, prova de pagamento nomeada | [C] | F4 | Baseline de paridade competitiva |
| **Cada marca líder é dona de exatamente 1 formato** e não divide aposta | [C] | F4 | **Escolher uma via-assinatura, não hedge** |
| Esqueleto dominante **B1**: `Ruptura → Guinada → Prova → CTA+preço`; **preço só no beat de CTA, nunca no gancho** | [C] | F4 | Roteiro padrão recomendado |
| **Descompasso frequência × persistência**: preço vence em frequência bruta, mas anúncios preço-first duram pouco e têm poucas variantes; os mais iterados são **emocionais** | [E]+[I] | F4 | Frequência mede o que é barato de produzir; persistência mede o que continua sendo alimentado |
| **Transparência do mecanismo (Loteria Federal/SUSEP) não aparece em nenhum anúncio** da varredura | [E] | F4 | **Única lacuna real de whitespace** — e a que mais casa com a natureza regulada do produto |
| No TikTok Creative Center BR, **nenhum top-ad nem amostra de vídeo** tem relação com sorteio/rifa/loteria | [E] | F5 | Possível baixo investimento pago do nicho no TikTok vs. Meta — whitespace de canal ou sinal de que não funciona lá |
| Para o Brasil, o Creative Center só oferece **Hashtag trends**; Song foi descontinuado e Video é geo-restrito (BR fora) | [E] | F5 | Limita a pesquisa de tendência de primeira mão no TikTok |
| Cluster de hashtags de "renda extra via TikTok LIVE" | [E] | F5 | **[I]** Fácil de estender para o whitespace de transparência: live mostrando como funciona o sorteio |
| **3 formatos validados fora da taxonomia do Meta**: recap em quadro branco, demonstração silenciosa de produto, POV + legenda única | [C] | F5 | Recap em quadro branco sustenta vídeos longos — **transferível para explicar o mecanismo de sorteio/SUSEP** |
| **Kwai tem penetração muito maior nas classes D/E do que nas A/B** (pesquisa pública Mobile Time/Opinion Box) | [E] | F6 | **Kwai não estava no plano de mídia** |
| Instagram: **envio por DM pesa várias vezes uma curtida** como sinal de alcance para não-seguidores | [E] | F6 | Gancho feito para ser **encaminhado a uma pessoa específica** é diferente de um feito para curtida |
| **Boa parte dos brasileiros que iniciam compra por WhatsApp já abandonou uma** | [E] | F6 | WhatsApp é camada de qualificação e confiança, **não superfície confiável de fechamento sozinha** |
| Regra dura: **nunca mandar para WhatsApp sem ter dito o preço antes** | [C] | F6 | Padrão que mais alimenta o abandono |
| **13º salário e Bolsa Família têm calendários conhecidos e datados** | [E] | F6 | Ritmo anual e mensal real para testar escala |
| Completion/watch-time é o sinal de ranking nº 1 nas plataformas com documentação pública; **vídeos curtos para tráfego frio** | [E] | F6 | Restrição de roteiro |
| Nenhuma plataforma publica limiar absoluto de matar/manter/escalar — usar **percentil dentro do lote do dia** | [E] ausência + [C] | F6 | Painel de decisão operacional |
| **"Viral ≠ conversão" é folclore de operador**, não fato medido nesse nível | [I] | F6 | Não citar ratios de "X views = Y vendas" como dado |
| O risco regulatório de publicidade **está se apertando** no Brasil (revisões abertas citando marketing de influenciador; políticas de plataforma contra promessa de resultado) | [E] | F6 | Re-checar páginas de política **mensalmente** |

---

## 6. Riscos e tensões abertas

Cada item é **endereçável**: tem dono sugerido (por papel), decisão travada e caminho de resolução. Severidade é avaliação deste PRD [I], calibrada por impacto × irreversibilidade.

### 6.1 🔴 CRÍTICO — "Combo" com dúvida regulatória SUSEP não resolvida

| Campo | Conteúdo |
|---|---|
| **O que é** | Foi encomendada uma IA treinada na regulamentação SUSEP, motivada por dúvidas sobre o "combo". **Nenhuma resolução foi registrada** [E] |
| **Por que é crítico** | **[I]** "Combo" é o **único ponto de possível inovação de oferta** — provavelmente venda de múltiplos títulos em pacote. E o checkout já tinha pacotes [E, F3]: a mecânica cuja legalidade está em dúvida **já estava no protótipo** |
| **Risco real** | Vender pacote fora do que o produto registrado do emissor permite; construir mídia sobre uma oferta que precisa ser desmontada depois |
| **Dono sugerido** | Líder de produto, com validação do emissor e de assessoria jurídica. **[I] Uma IA treinada em SUSEP não substitui parecer jurídico nem a validação do emissor** |
| **Decisão travada** | Estrutura de pacotes do checkout, copy de oferta, economia de ticket |
| **Pergunta de pesquisa** | Q-R2, Q-R3 |

### 6.2 🔴 CRÍTICO — Exposição de dados pessoais sem LGPD discutida

| Campo | Conteúdo |
|---|---|
| **O que é** | Pediu-se acesso ao banco completo do fornecedor (negado). Acordou-se integração via **Webhook ou n8n**, com payload de CPF, telefone, e-mail, nome e *todos os campos coletados*, mais transacionais de Pix [E, F3] |
| **A ausência** | **LGPD nunca foi mencionada** [E, ausência]. Ausentes: base legal, minimização (*todos os coletados* é o oposto), contrato de operador/controlador com o fornecedor, política de retenção e definição de quem é controlador |
| **Agravante** | O schema tem `opt-ins LGPD por canal` [E, F2] — o consentimento foi modelado como campo de banco sem discussão do regime jurídico. Isso cria falsa sensação de cobertura |
| **Risco real** | Tratamento de CPF + dados pessoais em massa sem base legal documentada, em produto financeiro regulado, com transferência entre empresas sem instrumento contratual |
| **Dono sugerido** | Líder de produto/dados + responsável técnico da integração + sócio responsável pelo contrato com o fornecedor |
| **Decisão travada** | Escopo do payload; instrumento contratual com o fornecedor; go-live com coleta de dados pessoais |
| **Pergunta de pesquisa** | Q-R4, Q-R5, Q-R6 |

### 6.3 🔴 CRÍTICO — Economia do produto em branco

| Campo | Conteúdo |
|---|---|
| **O que é** | **Preço/ticket, prêmio âncora, estrutura de série, stack de banco, gateway de Pix e emissor nunca foram definidos** [E, ausência] |
| **Contexto de mercado disponível** | Faixa de ticket dos concorrentes observada nos anúncios públicos [E, F4]; mediana do Pix no Brasil [E, F6] |
| **Por que é crítico** | Contas de mídia prontas apontando para um produto cuja unit economics ninguém calculou. **[I] É o risco de sequenciamento que abre este PRD** |
| **Dono sugerido** | Líder de produto + líder de mídia (amarra CAC ao ticket) + sócio responsável pelo investimento em prêmio |
| **Decisão travada** | Praticamente todas: copy, criativo, comissão de afiliado, meta de mídia, viabilidade |
| **Pergunta de pesquisa** | Q-P1, Q-P2, Q-P3, Q-P4 |

### 6.4 🟠 ALTO — Fragilidade dos ativos de marca/domínio

| Campo | Conteúdo |
|---|---|
| **O risco real** | (a) só um TLD da marca estava protegido — o `.com.br`, TLD de confiança para o público brasileiro, não foi verificado [E, ausência]; (b) a custódia do domínio estava com alguém fora do núcleo de decisão [E] — risco de bus factor e de governança; (c) transferência de registrador decidida mas não confirmada; (d) DNSSEC sem confirmação; (e) o produto ainda rodava em URL de preview do fornecedor [E] |
| **A tensão de coordenação** | O time registrou marcas satélite enquanto **o domínio principal seguia com registrador instável, sem `.com.br`, sem DNSSEC e sem go-live** |
| **Custo de checagem** | **Minutos.** Maior risco/menor custo de verificação do projeto |
| **Dono sugerido** | Responsável por infraestrutura + quem detém a custódia + líder de produto |
| **Pergunta de pesquisa** | Q-M1, Q-M2 |

### 6.5 🟠 ALTO — Concentração de risco no fornecedor da plataforma

| Campo | Conteúdo |
|---|---|
| **A assimetria** | **Fornecedor detém:** plataforma, site builder, checkout, dados transacionais, painel de afiliados, tracking server-side, automação e **produção de criativo em vídeo** [E, F3]. **Time detém:** marca, domínio, design e rede de influenciadores [I, F3] |
| **Evidências de dependência** | (a) acesso ao banco completo negado — a fronteira de dados foi ditada pelo fornecedor [E]; (b) customização de arte por pacote vetada pela plataforma, aceita sem avaliar alternativa [E + I]; (c) o criativo com maior reação positiva do time foi produzido pelo fornecedor [E]; (d) documentação de API pedida e **nunca entregue** [E] |
| **Quebra de domínio no checkout** | **[I]** O usuário **sai do domínio da marca** no momento da conversão (checkout em subdomínio do fornecedor) — risco clássico de quebra de confiança e de perda de atribuição/pixel. **Ninguém levantou esse ponto** [E, ausência] |
| **Dono sugerido** | Sócio responsável pela relação comercial + líder de produto (arquitetura e fronteira de dados) |
| **Pergunta de pesquisa** | Q-F1, Q-F2, Q-F3 |

### 6.6 🟠 ALTO — Desconexão entre pesquisa formal e benchmark real

| Campo | Conteúdo |
|---|---|
| **O que é** | Os concorrentes da pesquisa formal **não aparecem** nas conversas do time [E, ausência]. O benchmark real foi escolhido por critério estético e **nunca analisado** [E] |
| **Por que importa** | **[I]** Há conhecimento rigoroso (taxonomia de formatos, ranking de persistência, whitespace de transparência) que **não chega à decisão**, enquanto o benchmark que orienta o time nunca passou por análise |
| **Sinal adicional** | O time observava **founder-as-face** em um concorrente e havia mudança no arranjo com o influenciador parceiro — debate implícito e **não resolvido sobre quem é o rosto da marca** [I] |
| **Dono sugerido** | Sócio que faz o benchmark hoje + líder de mídia |
| **Pergunta de pesquisa** | Q-C1, Q-C2, Q-C3, Q-C4 |

### 6.7 🟠 ALTO — Sobreposição de tracking não resolvida

| Campo | Conteúdo |
|---|---|
| **O que é** | Havia um sistema próprio de tracking/atribuição server-side, e o fornecedor também oferecia conversion API server-side. **Quem é a fonte de verdade de conversão nunca foi decidido** [I] |
| **Agravante** | A disponibilidade de PostBack para Meta/TikTok/Google **nunca foi respondida** pelo fornecedor, e a documentação de API não foi entregue [E] |
| **Risco real** | Dupla contagem de conversão, otimização sobre sinal inconsistente, disputa de atribuição com afiliados comissionados |
| **Dono sugerido** | Responsável técnico da integração, com escalação ao líder de produto |
| **Pergunta de pesquisa** | Q-F2, Q-T1 |

### 6.8 🟠 ALTO — CNPJ trava toda a máquina de mídia

| Campo | Conteúdo |
|---|---|
| **O que é** | Contas TikTok, Meta e Google prontas, bloqueadas exclusivamente pela emissão do CNPJ, sem confirmação de emissão no fim do período analisado [E] |
| **Por que importa** | Todo o plano de aquisição depende disso; é a dependência crítica única e explícita do corpus |
| **Dono sugerido** | Líder de mídia |
| **Pergunta de pesquisa** | Q-T2 |

### 6.9 🟡 MÉDIO — "Plano de jogo oficial" inexistente e refém de terceiro

| Campo | Conteúdo |
|---|---|
| **O que é** | O fornecedor cobrou duas vezes o **"plano de jogo oficial da campanha"**, que dependia do aval do time de um influenciador [E] |
| **Contradição a resolver** | O arranjo com o influenciador mudou depois, e o plano de aquisição foi redesenhado sem ele [E]. **[I] Não está claro se o gate da campanha ainda existe** |
| **Dono sugerido** | Sócio responsável pela relação com o influenciador + líder de mídia |
| **Pergunta de pesquisa** | Q-G1, Q-G2 |

### 6.10 🟡 MÉDIO — Regra de negócio da raspadinha nunca especificada

| Campo | Conteúdo |
|---|---|
| **O que é** | Existiam assets de duas raspadinhas (co-branded e de marca própria, esta com *prêmios melhores*) [E]. **Nenhuma regra de negócio, preço, probabilidade, prêmios ou posição no fluxo** [E, ausência] |
| **Agravante regulatório** | **[I]** Prêmio instantâneo em título de capitalização tem tratamento próprio sob SUSEP — é a segunda mecânica (junto do "combo") que precisa de validação do emissor antes de virar copy |
| **Dono sugerido** | Líder de produto + responsável por design/ativos |
| **Pergunta de pesquisa** | Q-P5 |

### 6.11 🟡 MÉDIO — Cifra ambígua propagando sem desambiguação

Uma cifra grande citada no chat logo após a liberação de crédito de mídia, sem unidade clara (limite de crédito? alcance?). **Regra:** número ambíguo não é propagado como fato sem confirmação. Dono sugerido: líder de mídia. Ver Q-T3.

### 6.12 🟡 MÉDIO — Ponto único de falha

**[I]** Uma única pessoa acumulava dados, arquitetura de CRM, integração com fornecedor, marca, frente regulatória e coordenação. Decisão organizacional, não pergunta de pesquisa.

### 6.13 🟡 MÉDIO — Kwai ausente do plano, apesar de ser possivelmente o canal nº 1 do público-alvo

**[E, F6]** Kwai tem penetração muito maior nas classes D/E do que nas A/B. **[E, ausência]** Kwai **nunca foi mencionado** nas conversas nem nas pesquisas de canal; o plano cobria Meta, TikTok e Google. **[I]** Se a tese de público C/D/E estiver correta (§2.4), há um canal relevante fora do plano. Dono sugerido: líder de mídia. Ver Q-C5.

---

## 7. Backlog de perguntas de pesquisa em aberto

> **Esta é a seção operacional do documento.** Cada pergunta é acionável, está ligada a uma **decisão pendente** e nomeia **qual fonte disparou a dúvida**. Prioridade: **P0** = trava go-live ou expõe a operação · **P1** = trava decisão de produto/mídia · **P2** = melhora qualidade da decisão.
>
> **Regra de uso:** quando uma pergunta for respondida, mover a resposta para a seção correspondente (§2–§5) **com tag de evidência** e registrar a pesquisa no índice da §8. O backlog encolhe porque a base de conhecimento cresce, não por descarte.

### 7.1 Regulatório e jurídico

| ID | Pergunta | Decisão que destrava | Fonte | Prio |
|---|---|---|---|---|
| **Q-R1** | As afirmações regulatórias do schema — **CPF obrigatório pela SUSEP para titularidade** e **idade mínima como obrigação legal** — se confirmam em fonte normativa primária (Circulares SUSEP / Código Civil / ECA)? | KYC, campos obrigatórios, política de idade mínima | F2 — schema gerado com LLM, sem validação jurídica | **P0** |
| **Q-R2** | **O "combo" (múltiplos títulos em pacote) é permitido para título de capitalização na regulamentação SUSEP vigente?** Sob quais condições (limite por transação, apresentação de preço, condições gerais)? | Pacotes já implementados no checkout; copy de oferta; economia de ticket | F2 — dúvida declarada, sem resolução | **P0** |
| **Q-R3** | **Prêmio instantâneo tipo raspadinha** é admitido dentro de título de capitalização, ou exige produto/autorização distinta? Muda algo quando é co-branded com influenciador? | Regra de negócio da raspadinha | F3 — asset entregue sem discussão regulatória; F2 — evento no event store | **P0** |
| **Q-R4** | **Qual a base legal (LGPD art. 7º)** para tratar CPF + dados pessoais recebidos do fornecedor via webhook? Quem é **controlador** e quem é **operador**? | Escopo do payload; política de privacidade; go-live com coleta | F3 — payload amplo especificado, LGPD nunca mencionada | **P0** |
| **Q-R5** | Existe (ou precisa existir) **instrumento contratual de tratamento de dados (DPA)** com o fornecedor, com finalidade, retenção e segurança? | Contrato antes de trafegar dados pessoais em produção | F3 | **P0** |
| **Q-R6** | Aplicando **minimização (LGPD art. 6º, III)**: quais campos do payload são necessários para o CRM? | Reduzir o payload antes da implementação | F3 | P1 |
| **Q-R7** | **Quais os limites de claim publicitário** para título de capitalização sob SUSEP + CONAR? Valor de prêmio como headline? Prova de pagamento nomeada exige autorização formal do ganhador? | Copy de todos os criativos; formato-assinatura | F4, F6 | P1 |
| **Q-R8** | A **IA de SUSEP** foi entregue? Qual base normativa usa, e qual o status: apoio à decisão ou fonte de verdade? | Se o regulatório é resolvível internamente ou exige assessoria externa | F2 | P1 |

### 7.2 Produto, oferta e economia

| ID | Pergunta | Decisão que destrava | Fonte | Prio |
|---|---|---|---|---|
| **Q-P1** | **Qual o ticket de entrada?** Como se posiciona contra a faixa dos concorrentes e contra a mediana do Pix? | Copy, criativo, comissão, meta de CAC, viabilidade | F2/F3 (ausência), F4, F6 | **P0** |
| **Q-P2** | **Qual o prêmio âncora?** O nome da marca cria uma expectativa; se o âncora real for menor, há risco de dissonância e de claim publicitário? | Headline de campanha; economia de prêmio | F2 | **P0** |
| **Q-P3** | **Qual a economia completa das três camadas** (âncora / intermediário / instantâneo): frequência, valores, probabilidade e custo esperado por título? | Margem unitária; sustentabilidade do SLA; quanto de mídia o ticket suporta | F2 | **P0** |
| **Q-P4** | **Quem é a sociedade de capitalização emissora?** Qual produto registrado, e o que suas condições gerais permitem em série, pacote e prêmio instantâneo? | **Destrava Q-R2, Q-R3, Q-P1 e Q-P3 de uma vez** | F2 (ausência) | **P0** |
| **Q-P5** | **Qual a regra de negócio da raspadinha?** Avulsa ou embutida, prêmios, probabilidade, momento no fluxo, diferença entre as duas versões | Feature; briefing de assets; copy de retenção D+0 | F3 | P1 |
| **Q-P6** | Cadência **semanal + mensal com upsell** se traduz para a estrutura de sorteios do Seu Milhão? | Calendário de sorteios; estrutura de campanha | F1 | P1 |
| **Q-P7** | **App ou web?** Sem app, o CRM WhatsApp substitui o push como canal proprietário de retenção? | Roadmap de app; peso do CRM WhatsApp | F1, F3 | P1 |
| **Q-P8** | O **checkout deve ficar em subdomínio do fornecedor**? Qual o impacto na conversão e na atribuição/pixel para este público? | Checkout próprio vs. limitação do fornecedor | F3 | P1 |
| **Q-P9** | **"CRM próprio" se sustenta** frente a plataformas de mercado? Custo real de construir vs. contratar, e custo efetivo de disparo por canal? | Build vs. buy; briefing da V1 | F3, F1 | P1 |
| **Q-P10** | Os números de benchmark de terceiros são de base de contatos ou de custo, de unidades ou de receita? | Calibrar qualquer modelagem baseada em benchmark | F1 | P2 |
| **Q-P11** | Os **pacotes do checkout** com destaque "mais vendido" estão direcionando a escolha como pretendido? | Validar a única decisão de conversão com racional explícito | F3 | P2 |

### 7.3 Concorrência, mídia e criativo

| ID | Pergunta | Decisão que destrava | Fonte | Prio |
|---|---|---|---|---|
| **Q-C1** | **Análise formal do benchmark que o time de fato usa**: formato-assinatura, ticket, estrutura de prêmio, persistência de criativo no Meta Ad Library | Se o benchmark é defensável e o que copiar dele | F2 × F4 | **P0** |
| **Q-C2** | **Qual o formato-assinatura do Seu Milhão?** Cada líder é dono de um formato; vale atacar o whitespace de **transparência do mecanismo**? | Direção criativa inteira | F4 | **P0** |
| **Q-C3** | **Quem é o rosto da marca?** Influenciador, apresentador, fundador (founder-as-face)? | Criativo, contratos de influenciador, plano de Instagram | F2 | **P0** |
| **Q-C4** | **Por que a pesquisa formal não circula?** O que muda no formato/entrega para os achados chegarem à decisão de mídia e de marca? | Eficácia da função de pesquisa — **a meta-pergunta deste PRD** | F2 × F4 | P1 |
| **Q-C5** | **Kwai entra no plano de mídia?** | Alocação de budget; criativo por plataforma | F6 (Mobile Time/Opinion Box) | P1 |
| **Q-C6** | **Há investimento pago do nicho no TikTok Brasil?** A ausência é whitespace ou sinal de que o formato não performa lá? | Split TikTok vs. Meta | F5 | P1 |
| **Q-C7** | **Benchmark realista de conversão de disparo** para uma base nova vs. base quente no nicho | Modelagem de receita do CRM | F1 | P1 |
| **Q-C8** | Aplicar o **procedimento de descoberta de ângulo de 1 semana** (F6 §C): quais subgrupos e tensões reais existem no público C/D/E para sorteio/Pix? | **Regra dura: nenhum gancho antes de subgrupo com evidência** | F6 | P1 |
| **Q-C9** | O **recap em quadro branco** funciona para explicar o mecanismo de sorteio/Loteria Federal/SUSEP? | Veículo concreto para o whitespace de transparência | F5 | P2 |
| **Q-C10** | **Pricing e limites de volume** de plataformas de disparo WhatsApp em escala no Brasil | Insumo de Q-P9 | F1 | P2 |
| **Q-C11** | O calendário de **13º salário e Bolsa Família** deve estruturar sorteios e escalonamento de mídia? | Sazonalidade; quando escalar | F6 | P2 |
| **Q-C12** | Existe **categoria de indústria para sorteio/rifa/loteria** no filtro do TikTok Top Ads? | Refinar Q-C6; checagem manual de um clique | F5 | P2 |

### 7.4 Fornecedor, técnico e ativos

| ID | Pergunta | Decisão que destrava | Fonte | Prio |
|---|---|---|---|---|
| **Q-F1** | **Plano de contingência se a relação com o fornecedor se deteriorar**: dados portáveis? cláusula de saída? tempo para reconstruir checkout + afiliados? | Nível aceitável de dependência; checkout próprio agora ou depois | F3 | **P0** |
| **Q-F2** | **Fonte de verdade de conversão**: tracking do fornecedor ou sistema próprio? PostBack confirmado? | Otimização de campanha; comissão de afiliado; leitura de CAC | F3 | **P0** |
| **Q-F3** | **Onde está a documentação da API do fornecedor?** | Especificação do webhook; prazo do banco próprio | F3 | P1 |
| **Q-T1** | **Qual stack para o banco próprio**, conciliando event store × transacional? | Prazo do CRM V1; receber webhook antes do go-live de mídia | F2 | **P0** |
| **Q-T2** | **O CNPJ foi emitido** e as contas de mídia desbloqueadas? | Destrava toda a máquina de mídia | F2 | **P0** |
| **Q-T3** | **O que exatamente é a cifra ambígua** citada após o crédito de mídia? | Dimensionamento do plano de mídia | F2 | P1 |
| **Q-T4** | **Qual gateway de Pix?** Taxa, tempo de liquidação e efeito no SLA de pagamento de prêmio | Margem unitária; viabilidade do SLA | F2 | P1 |
| **Q-M1** | **O `.com.br` da marca está disponível?** O público C/D/E trata `.com.br` como sinal de confiança? | Portfólio de marca; risco de squatting | F2, F3 | **P0** |
| **Q-M2** | Status real de: transferência de registrador, DNSSEC, go-live no domínio próprio e titularidade formal do domínio | Estabilidade antes de qualquer investimento de mídia | F3 | **P0** |
| **Q-G1** | O gate da campanha ligado ao influenciador ainda existe? | Se o "plano de jogo oficial" ainda depende de terceiro | F2 × F3 | P1 |
| **Q-G2** | **O "plano de jogo oficial da campanha" existe?** | Go-live — gargalo interno, não do fornecedor | F3 | **P0** |
| **Q-G3** | **Quando acontece o onboarding oficial com o fornecedor?** | Ativação de afiliados e tracking | F3 | P1 |
| **Q-A1** | **Anexos de alta prioridade não abertos** (identidade visual, prints de referência que podem ter originado o "combo", criativo aprovado) | Pode resolver metade de Q-R2 | F2, F3 | P1 |

### 7.5 Regras de higiene deste backlog

1. **Nenhuma resposta entra no PRD sem tag de evidência.** Número auto-reportado por terceiro entra como [E, auto-reportado], nunca como [E] simples.
2. **Q-P4 (emissor SUSEP) é a pergunta de maior alavancagem** — destrava Q-R2, Q-R3, Q-P1 e Q-P3 de uma vez. **[I]** Priorizar acima das outras P0 se houver escolha.
3. **Perguntas de custo de checagem em minutos vêm antes das de custo em semanas.** Q-M1, Q-M2, Q-T2 e Q-C12 se resolvem em uma tarde.
4. **Não escrever gancho antes de subgrupo com evidência** (F6, regra dura). Q-C8 precede toda produção de criativo.
5. **Re-checar páginas de política de plataforma mensalmente** [E, F6].

---

## 8. Índice de pesquisas já realizadas

| Pesquisa | Caminho | Resumo |
|---|---|---|
| **Meta Ad Library — nicho sorteio BR** | `research/2026-08-11-meta-ad-library-sorteio-br/README.md` | Leitura de anúncios ativos de marcas do nicho + termos genéricos, com taxonomia de **8 formatos**, 3 esqueletos de roteiro e ranking de persistência (tempo no ar × variantes) como proxy de onde o budget está. **Achado mais acionável: transparência do mecanismo não aparece em nenhum anúncio — único whitespace confirmado**, e cada marca líder é dona de um formato. |
| **TikTok Creative Center — BR** | (não publicada: coleta automatizada) | Sessão assistida no Creative Center BR: Song trends descontinuado, Video trends geo-restrito (BR fora), só Hashtag trends para o Brasil. **Nenhum anúncio do nicho na amostra brasileira** e **3 formatos de vídeo validados [C] fora da taxonomia do Meta**, incluindo o recap em quadro branco. |
| **Short-form direct sales — BR, classes C/D, ticket baixo** | `research/2026-08-11-shortform-direct-sales-br/README.md` | Sistema operacional de 9 camadas (Oferta → Subgrupo/Tensão → Ângulo → Gancho → Roteiro → Prova → CTA → Métrica → Iteração), procedimento de descoberta de ângulo em 1 semana, banco de ganchos, matriz de produção semanal e painel de decisão por percentil. |
| Pesquisas complementares | `research/2026-08-14-*`, `docs/research/` | Modelo de negócio dos players de capitalização, regulatório SUSEP, reclamações públicas no ReclameAqui, cadência/ângulo/canais de promoções, fluxo financeiro de rifas, anúncios em vídeo gerados por IA no Meta. |

**[I] Lacunas de cobertura do índice original:** o benchmark real do time, **regulamentação SUSEP** em fonte primária, **LGPD** aplicada a esta arquitetura, **Kwai** como canal e **pricing de plataformas de disparo WhatsApp**. Todas viraram perguntas na §7.

---

## 9. Próximos passos recomendados

Ordenados por **alavancagem ÷ custo**, não por urgência percebida. Donos por papel.

### Sprint 0 — Verificações de uma tarde

| # | Ação | Dono | Fecha |
|---|---|---|---|
| 1 | Confirmar emissão do **CNPJ** e desbloqueio das contas de mídia | Líder de mídia | Q-T2 |
| 2 | Verificar e registrar o **`.com.br`** da marca; auditar titularidade formal do domínio | Infraestrutura | Q-M1 |
| 3 | Confirmar **transferência de registrador, DNSSEC e go-live** no domínio próprio | Infraestrutura | Q-M2 |
| 4 | Desambiguar a **cifra ambígua** e parar a propagação até lá | Líder de mídia | Q-T3 |
| 5 | Abrir os **anexos de alta prioridade** | Líder de produto | Q-A1 |
| 6 | Cobrar a **documentação da API** do fornecedor | Responsável técnico | Q-F3 |

### Sprint 1 — Destravar o produto

| # | Ação | Dono | Fecha |
|---|---|---|---|
| 7 | **Identificar e formalizar o emissor SUSEP** — a ação de maior alavancagem do plano | Sócios + líder de produto | Q-P4 → Q-R2, Q-R3, Q-P1, Q-P3 |
| 8 | Definir **preço, prêmio âncora e economia das três camadas** | Líder de produto + líder de mídia | Q-P1, Q-P2, Q-P3 |
| 9 | **Congelar a mídia paga até 7 e 8 fecharem.** [I] Comprar tráfego contra economia indefinida é o modo de falha mais caro disponível | Sócios | — |
| 10 | Produzir o **"plano de jogo oficial da campanha"** | Sócios + líder de mídia | Q-G2 |
| 11 | Esclarecer se o gate ligado ao influenciador ainda existe | Sócios | Q-G1 |

### Sprint 2 — Fechar a exposição jurídica

| # | Ação | Dono | Fecha |
|---|---|---|---|
| 12 | **Definir base legal LGPD** e **reduzir o payload por minimização** antes da implementação | Líder de produto + responsável técnico | Q-R4, Q-R6 |
| 13 | Assinar **DPA com o fornecedor** antes de trafegar dados pessoais em produção | Sócios + líder de produto | Q-R5 |
| 14 | **Validar em fonte primária** as afirmações regulatórias do schema | Líder de produto | Q-R1 |
| 15 | Definir o status da **IA de SUSEP** como apoio à decisão, **nunca fonte de verdade**; levar combo/raspadinha ao emissor e/ou assessoria jurídica | Líder de produto | Q-R8, Q-R2, Q-R3 |

### Sprint 3 — Fechar o ciclo de conhecimento

| # | Ação | Dono | Fecha |
|---|---|---|---|
| 16 | **Pesquisa formal do benchmark real** com o mesmo rigor aplicado aos demais | Sócios + analista | Q-C1 |
| 17 | **Escolher o formato-assinatura** e decidir se ataca o whitespace de transparência | Líder de mídia + sócios | Q-C2 |
| 18 | **Decidir o rosto da marca** | Sócios | Q-C3 |
| 19 | Rodar o **procedimento de descoberta de ângulo** antes de qualquer gancho | Líder de mídia | Q-C8 |
| 20 | Decidir sobre **Kwai** no plano de mídia | Líder de mídia | Q-C5 |
| 21 | **Resolver a fonte de verdade de tracking** antes de campanha com afiliado comissionado | Responsável técnico | Q-F2 |
| 22 | Escolher **stack do banco próprio** e **gateway de Pix** | Infraestrutura + responsável técnico | Q-T1, Q-T4 |

### Ritual sugerido para manter este PRD vivo

- **Revisão semanal do backlog** (30 min): quais perguntas foram respondidas, se a resposta subiu para §2–§5 com tag de evidência, e qual pesquisa entra na §8.
- **Toda pesquisa concluída entra na §8** com 1–2 linhas de resumo e atualiza as seções correspondentes. Sem isso, repete-se o padrão do §5.4 (pesquisa que não circula).
- **Toda decisão relevante tomada em chat** vira registro com data e porquê.
- **Nenhum número auto-reportado por terceiro** entra sem aviso de qualidade de dado.

---

*Documento vivo. Para atualizar: responder perguntas da §7, promover a resposta para a seção correspondente com tag de evidência, registrar a pesquisa na §8.*
