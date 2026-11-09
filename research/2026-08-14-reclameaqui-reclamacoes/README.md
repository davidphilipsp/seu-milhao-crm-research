# O que as pessoas realmente reclamam — conteúdo das reclamações no Reclame Aqui dos 5 players

> Versão pública sanitizada: números de negócio, nomes de pessoas, citações de fontes privadas e parceiros foram substituídos por marcadores ([valor], [n], [x%], papéis).

**Legenda de evidência:** **[E]** documentado (fonte primária lida, URL citada) · **[C]** padrão repetido observado em múltiplas reclamações, sem fonte única atribuível · **[I]** inferência do analista.

**Data da coleta:** 14/08/2026. Todos os números são snapshot desse dia.

---

## 0. O que esta pesquisa é, e por que ela existe

A pesquisa anterior (`research/2026-08-14-capitalizacao-players-modelo-negocio/`) mapeou modelo de negócio, arquitetura regulatória e escala dos cinco concorrentes diretos. Naquele documento, a linha "Reclame Aqui" da tabela comparativa (§6) era uma célula de duas informações: **volume e nota**. Uma célula de duas informações não diz *o que quebra* — diz só *quanto*.

Esta pesquisa desce um nível. Cinco agentes de pesquisa independentes abriram e leram **reclamações individuais** de cada player: o texto integral do consumidor, a resposta verbatim da empresa, a réplica quando existia, a data, a cidade, o status e a nota atribuída. **Mais de [n] reclamações lidas na íntegra ou em snippet classificável**, além das facetas oficiais de categorização, que cobrem a base populacional inteira de cada perfil.

| Player | Reclamações lidas | Cobertura |
|---|---|---|
| Viva Sorte + VIA Cap | [n] na íntegra | amostra temática, 2023–2026 |
| Pix do Milhão | [n] na íntegra | [x%] do universo, 09/2024–08/2026 |
| Apcap da Sorte | [n] classificadas · **[n] na íntegra** | [x%] da listagem, cobertura integral de ago/2025→ago/2026 |
| Familhão | [n] na íntegra | [x%] do acumulado, 04/2024–08/2026 |
| SBT Prêmios | [n] snippets · **[n] na íntegra** | ~22/07 a 14/08/2026 + fase Icatu |

### 0.1 Método e sua limitação estrutural

**[E]** `reclameaqui.com.br` e sua API interna (`iosite.reclameaqui.com.br`) retornam **403 / desafio Cloudflare** a WebFetch e a `curl` direto. Todo o acesso foi obtido via proxy de leitura com renderização de DOM (`r.jina.ai`), que expõe o payload `astro-island props` embutido nas páginas — contendo `title`, `description` (corpo integral), `created`, `userCity`/`userState`, `status`, `solved`, `score` e `interactions[].message` (as respostas da empresa, verbatim, com data). O mesmo payload carrega o objeto `companyIndexes`, com a série de reputação por janela (6 meses, [n] meses, ano-calendário, 3 anos) — bem mais rica do que os números que a página exibe visualmente.

**[E] A paginação das listas de reclamação é client-side** e não renderizou de forma confiável pelo proxy em nenhum dos cinco levantamentos. **Consequência declarada por todos os agentes: não foi possível fazer amostragem aleatória.** As amostras foram montadas por busca temática indexada, pelo widget "Reclamações Parecidas" e pelas reclamações recentes exibidas no perfil — o que **enviesa sistematicamente para casos extremos, títulos dramáticos e itens bem indexados**.

**Regra de leitura deste documento, portanto:** onde há **faceta oficial do RA**, o número descreve a **população**. Onde há **percentual de amostra**, o número descreve **a amostra**, e está marcado como tal. Os dois nunca são somados.

**[E] Uma limitação que afeta a pergunta central e precisa ficar registrada:** o Reclame Aqui **censura automaticamente** os termos "golpe", "fraude", "estelionato" e equivalentes, substituindo-os por `[Editado pelo Reclame Aqui]`. Isso aparece em ~[n] das [n] reclamações do Viva Sorte, em dezenas de títulos da Apcap e em 5 das [n] do Familhão. **[I] Consequência: é impossível contar menções literais a "golpe" nesta base — a plataforma apaga exatamente o termo que a pergunta pede.** Qualquer análise de "menções a fraude no RA" subconta por design. O sinal existe, é alto, e está mascarado.

### 0.2 O que mudou em relação à pesquisa anterior

Quatro dos cinco levantamentos produziram **correção material de número**. Isso não é detalhe de rodapé: a pesquisa anterior comparou players usando números de **janelas temporais diferentes** como se fossem o mesmo indicador.

| Player | Registrado antes | Real (14/08/2026) | Natureza do erro |
|---|---|---|---|
| Viva Sorte | [n] · nota [n] | **[n] ativas** · [n] (janela 6m: [n]) | O [n] era a **janela de 6 meses**, não o acumulado |
| Pix do Milhão | "reclamações de não-pagamento" (sem número) | **[n] ativas** · nota **[n] / RA1000** | Ausência de dado → maior volume relativo do grupo, com a melhor nota |
| Apcap da Sorte | [n] · nota [n] · "nenhum passivo relevante" | **[n] + [n] = ~[n]** em dois perfis | Leitura de janela curta **e** perfil irmão não localizado |
| Familhão | [n] (via matéria do FDR) | **[n] ativas** · nota **[n] / RA1000** | O [n] era janela de 6 meses da época; acumulado é ~[n]× maior |
| SBT Prêmios | "não identificado" | **[n] no perfil próprio + ~[n] no perfil da Icatu ≈ [n]+ em 8 meses** | Gap fechado; slug era `sbt-premios` |

**[I] A lição metodológica é maior que as correções.** O Reclame Aqui exibe *simultaneamente*, na mesma página, o total histórico de reclamações ativas e a contagem da janela móvel de 6 meses — e a nota se refere **só** à janela. Comparar players misturando as duas leituras produz rankings invertidos. Toda comparação futura precisa declarar a janela.

---

## 1. Viva Sorte (+ VIA Cap) — o passivo se concentra na marca não-regulada

### 1.1 Escala real

**[E]**

| Métrica | Viva Sorte (distribuidora) | VIA Cap (emissora) |
|---|---|---|
| **Reclamações ativas — total** | **[n]** ([n] páginas) | **[n]** |
| Janela de reputação (01/02–31/07/2026) | [n] | [n] |
| Nota (6 meses) | **[n]/10** — Regular | [n]/10 — Regular |
| % respondidas | [x%] | **[x%]** |
| Aguardando resposta | **[n]** | 0 |
| % resolvidas | [x%] | [x%] |
| **Tempo médio de resposta** | **[n] dias e [n] horas** | **2 dias e [n] horas** |

Fontes: [perfil Viva Sorte](https://www.reclameaqui.com.br/empresa/viva-sorte/) · [lista Viva Sorte](https://www.reclameaqui.com.br/empresa/viva-sorte/lista-reclamacoes/) · [perfil VIA Cap](https://www.reclameaqui.com.br/empresa/via-cap/) · [lista VIA Cap](https://www.reclameaqui.com.br/empresa/via-cap/lista-reclamacoes/).

> **Correção de número.** A pesquisa anterior registrou "[n] reclamações". Esse é o volume da **janela de 6 meses**. O acumulado ativo é **[n]** — [n]× maior. Os dois números coexistem na mesma página.

**[I] O achado estrutural:** a razão distribuidora ÷ emissora é de **[n] para 1**. Todo o passivo reputacional se acumula na **marca voltada ao consumidor**, não na sociedade de capitalização regulada. E a emissora — que tem obrigação regulatória de ouvidoria — responde **[x%] em [n]**, enquanto a distribuidora responde **[x%] em [n]**. A arquitetura de duas empresas não distribuiu o risco de reputação: **concentrou-o inteiramente do lado não-regulado, que é justamente o lado com o pior SLA**.

### 1.2 Taxonomia

**[E] Facetas oficiais (base: [n]):** Propaganda enganosa **[n] ([x%])** · Login-Senha [n] · Estorno do valor pago [n] · Problemas na finalização da compra [n] · Problema no recebimento [n] · Dificuldade de cadastro [n].

**[E]** Nas categorias/produtos aparece uma anomalia: **"Leilão" ([n])** e **"Recuperadora de crédito" ([n] categoria / [n] produto)** — que **não são produtos do Viva Sorte**. Somadas, ~[n] reclamações, mais que a categoria "Títulos de capitalização" ([n]). **[I]** A leitura mais provável é contaminação massiva por golpes de terceiros que usam a marca em contextos de leilão falso e cobrança falsa, categorizados pelo consumidor conforme o golpe que sofreu. **Hipótese forte, não confirmada** — não foi possível abrir essas reclamações em volume.

**[C] Convergência notável:** distribuidora e emissora têm **exatamente a mesma proporção de "propaganda enganosa" ([x%])**, apesar de bases [n]× diferentes e de a emissora nem fazer publicidade ao consumidor. **[I]** Isso indica que "propaganda enganosa" no RA deste setor **não é julgamento sobre a peça publicitária** — é o rótulo genérico para "prometeram e não entregaram". Usar essa faceta como proxy de qualidade de criativo é erro de leitura.

**[E] Amostra lida (n=[n], enviesada para casos extremos):** golpe de terceiro usando a marca **[x%]** · atraso/falha no pagamento de prêmio legítimo [x%] · propaganda enganosa própria [x%] · prêmio instantâneo pago em crédito [x%] · estorno negado / bloqueio de cadastro [x%] · desconfiança de aleatoriedade [x%] · resgate do título [x%].

### 1.3 Verbatim que mais revela

**O sub-padrão mais grave: deepfake do fundador em videochamada ao vivo.** Três reclamações independentes descrevem chamadas de vídeo em que o fundador aparece pessoalmente:

> [relato de consumidor: golpista se passou pelo fundador em videochamada, de forma convincente; a vítima quase caiu no golpe]
> — **14/05/2025**, *Resolvido* **[E]**

> [relato de consumidor: golpista em videochamada tinha CPF e nome completo da vítima e anunciou um prêmio falso apoiado na credibilidade da TV; a vítima suspeita de imagem clonada por IA]
> — **14/05/2025**, *Resolvido* — mas com nota baixa e "voltaria a fazer negócio: Não" **[E]**

**[E]** O padrão persiste em **13/08/2026**, sem resposta na data da coleta: [relato de consumidor sobre golpe aplicado por Pix e videochamada usando o nome e a imagem do fundador].

**O risco regulatório mais concreto do painel inteiro** — um consumidor confronta o prazo praticado com o prazo registrado na SUSEP:

> [relato de consumidor: o atendimento por WhatsApp informou prazo de pagamento do prêmio em dias úteis, enquanto o site da marca e o processo SUSEP (item 10.11) registram dias corridos; o SAC da emissora disse que não era ela quem fazia o pagamento e encaminhou para a distribuidora]
> — **14/05/2024**, *Resolvido* **[E]**

**[E] A resposta da empresa assumiu a divergência sem corrigi-la:** *"Finais de semana não são considerados dias de efetivação de pagamentos. Portanto […] é utilizado o termo dias uteis."* **[I]** A empresa declarou por escrito, em canal público, uma contagem de prazo diferente da do processo SUSEP que ela mesma registrou. **[C]** Circulam simultaneamente quatro prazos: 24h (marketing), 72h úteis, [n] dias úteis e [n] dias corridos (regulamento/SUSEP).

**A raspadinha em crédito vestida de dinheiro:**

> [relato de consumidor: a raspadinha exibiu um prêmio alto e a empresa creditou apenas um valor simbólico] — jun/2025 **[E]**

> [relato de consumidor: a raspadinha indicou prêmio, mas a aba "Contemplações" aparecia vazia, o que o levou a duvidar de que seus títulos entram nos sorteios]
> — **10/06/2025** **[E]**

### 1.4 Padrão de resposta

**[E] Três templates verbatim identificados** — blocos de texto idênticos, reutilizados literalmente e identificáveis por colagem exata: **T1 "golpe de terceiro"** (4 ocorrências), **T2 "deflexão para o WhatsApp"** (4 ocorrências, texto de duas linhas), **T3 "os R$ [valor] são crédito"** (3 ocorrências).

**[C]** Das 4 reclamações que receberam o T2, **3 permaneceram não resolvidas** — e são justamente as de maior teor acusatório (manipulação de roleta, divergência anúncio×app, golpe com dados vazados). A única resolvida foi um atraso simples de pagamento. **[I]** O T2 tira a conversa do canal público exatamente quando o conteúdo é reputacionalmente perigoso: funciona para atrasos operacionais e falha para questionamentos estruturais — e deixa uma acusação detalhada indexada ao lado de uma resposta de duas linhas.

### 1.5 Tendência temporal — degradação por ordem de grandeza

**[E]** Latência complaint→resposta medida na amostra:

| Período | Latência | Casos |
|---|---|---|
| nov/2023 – jun/2025 | **0 a 3 dias** | [n] casos |
| ago/2025 – nov/2025 | **7 a [n] dias** | 6 casos |
| 2026 | **[n] a [n] dias, ou nenhuma** | [n]d (mar/26), [n]d (mai→ago/26), **5 reclamações de 07–14/08/2026 sem resposta** |

**[I]** O atendimento degradou de <3 dias para ~[n] dias em cerca de [n] meses — assinatura de **operação de aquisição escalando mais rápido que a de suporte**. E a nota do RA continuou "Regular" mesmo assim: **neste setor, o mercado não pune atendimento ruim o suficiente para forçar correção.**

**[C] Mudança de composição temática.** A amostra de 2024–2025 é dominada por *atraso de prêmio* e *golpe com taxa de liberação*. A frente de ago/2026 é dominada por **cancelamento/estorno, dificuldade de saque e cobrança repetida via Pix** — vocabulário de plataforma transacional, não de título de capitalização. **[E]** Corrobora: a caixa "quem acessou VIA Cap também acessou" lista **"plataforma de jogos"** com reputação "Não recomendada"; e a base do Viva Sorte tem "Games e Jogos" ([n]) como categoria.

**[E] Achado inesperado:** duas reclamações de ago/2026 **contra o Viva Sorte** mencionam **Liderança Capitalização** (emissora da Tele Sena e do SBT Prêmios), não a VIA Cap — inclusive uma que diz *"fiz dois depositos atraves da liderança capitalização […] **para o sbt premios**"*. **[I]** Ou o Viva Sorte passou a distribuir títulos de outra emissora, ou **o nome que aparece no extrato do Pix não é o nome da marca que o cliente acha que comprou** — e isso sozinho gera estorno, chargeback e reclamação registrada contra a marca errada. Não foi possível distinguir as hipóteses.

### 1.6 Sinais regulatórios levantados pelo consumidor

**[E]** Consulta ao processo SUSEP e citação do item 10.11 (14/05/2024) · ameaça formal de Procon (23/06/2025) · citação do **CDC art. 47** em raspadinha ambígua (14/09/2025) · enumeração dos elementos jurídicos de propaganda enganosa com declaração de posse de provas (25/08/2025) · ameaça de providências judiciais contra a emissora (18/07/2024) · alegação de vazamento de dados/LGPD (≥4 casos).

**[I] Ausência notável:** em [n] reclamações, **nenhuma menção a SUSEP como autoridade a ser acionada** — a única menção foi como *fonte de consulta* para checar prazo. Nenhuma denúncia à SPA/MF. O consumidor deste setor **não sabe a quem recorrer**: recorre ao Procon, ao RA e à ameaça judicial genérica. Isso reduz o risco regulatório de curto prazo do incumbente e explica por que [n] reclamações convivem com nota "Regular".

---

## 2. Pix do Milhão — atendimento industrializado sobre produto não corrigido

### 2.1 Escala real e o paradoxo da nota

**[E]** Os dois slugs `criative-publicidade-promocoes-e-shows` e `pix-do-milhao-ltda11` resolvem para **o mesmo perfil único** (`PIX DO MILHAO CLUBE DE BENEFICIOS E VANTAGENS LTDA`, CNPJ omitido).

| Indicador (01/02–31/07/2026) | Valor |
|---|---|
| Reputação | **RA1000** (nota máxima da plataforma) |
| Nota 6 meses | **[n] / 10** |
| Reclamações na janela | [n] |
| Respondidas | **[x%]** (1 aguardando) |
| Resolvidas | **[x%]** |
| Tempo médio de resposta | **4 dias e 4 horas** |
| Ranking | **1º lugar** em "Clubes de Benefícios e Descontos" |
| **Total ativas (histórico)** | **[n]** |

Fontes: [perfil](https://www.reclameaqui.com.br/empresa/criative-publicidade-promocoes-e-shows/) · [lista + facetas](https://www.reclameaqui.com.br/empresa/pix-do-milhao-ltda11/lista-reclamacoes/).

> **Correção de número.** A pesquisa anterior tinha apenas "reclamações de não-pagamento", sem contagem nem nota. **O player que a leitura anterior sugeria ter o maior passivo reputacional é o que tem a melhor nota do grupo** — pela métrica do RA.

**[I] Leitura crítica:** RA1000 e [n]/10 **não medem a legitimidade do produto — medem a operação de atendimento**. O player com maior volume absoluto de reclamações entre os que têm perfil comparável é também o de melhor nota. **Isso é uma capability comprável, não um acaso.**

### 2.2 Taxonomia

**[E] Facetas oficiais:** Propaganda enganosa **[n]** · Outro problema [n] · Não recebi [n] · Sorteios-Concursos [n] · Dificuldade de cadastro [n] · Login-Senha [n]. O FAQ do perfil declara, para 3 anos: *"Problemas — [x%] Propaganda enganosa"*.

**[E] Amostra lida (n=[n]):** prêmio instantâneo exibido e não pago **[x%]** · golpe de terceiro se passando pela marca [x%] · benefício comprado não entregue [x%] · denúncia de irregularidade regulatória [x%] · operacional de plataforma [x%] · assinatura/recorrência [x%].

**[I]** "Propaganda enganosa" com [n] ocorrências é, na prática, **o rótulo que o RA aplica ao tipo A** (prêmio exibido e não pago). O consumidor não tem a categoria "o sistema mostrou que eu ganhei e depois disse que não".

### 2.3 Verbatim que mais revela

**A falha de design mais explorável do painel inteiro** — a animação exibe um resultado que não é o resultado:

> [relato de consumidor: a raspadinha exibiu claramente um prêmio alto no Pix e o sistema pulou sozinho para a próxima cartela antes do resgate]
> — **29/11/2025**, **Não resolvido** **[E]**

> [relato de consumidor: a roleta parou visivelmente num prêmio alto, a tela piscou e o resultado mudou para "Não Ganhou"; pede inversão do ônus da prova com base nos logs técnicos]
> — **05/10/2025** **[E]**

**[E] A defesa da empresa é sempre a mesma frase, literal:** *"A animação da raspadinha exibida ao usuário possui **caráter meramente ilustrativo e recreativo**, não interferindo na efetiva distribuição dos prêmios."* — idêntica em 11/11/2025, 02/12/2025, 05/02/2026 (×3) e 06/02/2026. Para a roleta: *"o giro da roleta exibido ao usuário tem caráter meramente lúdico"*.

**[C] Três subpadrões:** (1) o prêmio aparece e a tela avança sozinha, impedindo screenshot; (2) giros/raspadinhas "somem" ou são consumidos automaticamente; (3) **o histórico não é auditável pelo próprio usuário** — *"os números da compra vocês passam, mas pq não deixam salvo o nosso registro de raspadinhas?"* (05/02/2026).

**O documento mais relevante do perfil** — denúncia estruturada de 07/02/2025, com 5 pontos e 6 perguntas formais: **[E]** e-books como fachada (*"pode ser uma estratégia para mascarar a venda direta de apostas"*); competência da LOTEP vs. União; compartilhamento de dados com "parceiros" não nomeados; **Pix vinculado ao CPF como barreira de resgate** (*"caso o ganhador não tenha uma chave PIX com seu CPF […] o dinheiro é destinado ao Tesouro Estadual"*); e **cláusula de desclassificação discricionária** (*"sem critérios claros, o que pode ser usado para impedir pagamentos legítimos"*).

**O achado mais estranho — SUSEP lida como aval do governo:**

> [relato de consumidor perguntando se a marca "é da Susep, empresa do governo" e descrevendo-a como "empresa apoiada pelo site do governo Susep", com valor retido na plataforma]
> — **23/05/2026** **[E]**

**[I]** O consumidor de baixa renda **não lê "SUSEP" como órgão fiscalizador — lê como sócio/avalista estatal**. O selo está sendo consumido como garantia de pagamento, não de conformidade. Consequência dupla: o selo tem valor de conversão maior do que o PRD supõe, **e cria expectativa de que o Estado pagará se a empresa não pagar** — e a frustração dessa expectativa é o que produz a linguagem de denúncia formal.

### 2.4 Padrão de resposta — quatro templates acionados por tipo

**[C]**

| Template | Aciona quando | Desfecho típico |
|---|---|---|
| **Jurídico-defensivo** (~[n] palavras: emissora, SUSEP, Decreto-Lei, Resolução CNSP, "animação meramente ilustrativa", **e termina negando o prêmio**) | prêmio não pago | Não resolvido / Em réplica |
| **Antifraude** (site oficial + CNPJ + recebedor + "peça estorno ao seu banco") | golpe de terceiro | Resolvido, às vezes nota 10 |
| **Tutorial** (passo a passo Menu > Meus Títulos > Solicitar Saque) | benefício/saque | Resolvido |
| **Personalizado** (só a partir de ~ago/2026: diagnóstico individual + data do contato) | todos | Resolvido, notas 9–10 |

**[E] Prova de que o template jurídico é literalmente copiado:** as respostas de **05/02/2026 às 17:33, 17:38 e 17:40** — três reclamações diferentes, três consumidores diferentes — são **textualmente idênticas, parágrafo por parágrafo** (links omitidos). E a réplica do consumidor mostra por que falha: *"**a compra mencionada?** se vocês verificaram, como vocês não sabem que foram **diversas compras**?"*

**[E]** A empresa **opera o perfil do RA como canal de marketing**: publica post promocional ativo (*"AÇÕES NOVAS LIBERADAS […] SEGUNDA DA SORTE: PRÊMIO = R$ [valor]"*), vídeo institucional, FAQ próprio e página "Sobre" — dentro do Reclame Aqui.

### 2.5 Tendência temporal — o passivo mudou de natureza junto com o modelo

**[E] Reputação:** Fev/26 Boa → Mar Boa → Abr Ótima → Mai Ótima → Jun **RA1000** → Jul **RA1000**.

**[E] Latência:** [n] dias (fev/2025) → [n] dias (dez/2025) → [n] dias (mai/2026) → 3 dias (ago/2026) → **7 horas** (12/08/2026).

**[C] Mudança na natureza das reclamações:**

| Período | Perfil dominante | Produto vendido |
|---|---|---|
| set–dez/2024 | Golpe de terceiro com taxa antecipada | "bilhetes" |
| fev–ago/2025 | Denúncia regulatória (LOTEP), roleta que "some" | "e-books" |
| **out/2025–fev/2026** | **Pico de gravidade:** prêmios de R$ [valor] exibidos e não pagos; ameaças de Procon/MP | "pontos" |
| mai–ago/2026 | Operacionais de baixa gravidade: cancelar assinatura, login, spam de WhatsApp | "assinatura / plano Premium" |

**[E] A migração de regime, datada pelas próprias respostas da empresa** — e revelando uma etapa que a pesquisa anterior não tinha:

| Data | Enquadramento afirmado pela empresa |
|---|---|
| 28/02/2025 | *"sorteios autorizados, fiscalizados e auditados pela **LOTEP**"* + invoca STF, ADPF 492 e 493 |
| 19/06 e 02/07/2025 | *"em parceria com a **emissora A** […] fiscalizados pela SUSEP"* |
| 31/10/2025 | *"em parceria com a **VIACAP**"* — descrevendo a modalidade como *"Filantropia Previável"* [sic] |
| 11/11/2025 → | VIACAP, modalidade **Incentivo**, *"promoção de vendas de **e-books**"* |
| 02/12/2025 → | VIACAP, modalidade Incentivo, *"promoção de vendas de **Pontos**"* |

**[E]** As instituições de pagamento também rodaram cinco vezes em [n] meses: Mercado Pago → +Efi/Gerencianet → +Credifit/SuitPay → EFI-IP → **Stark Bank S.A.-IP**. E o CNPJ citado alterna entre duas entidades distintas operando a mesma marca.

**[I] Sequência reconstruída:** *Lotep → emissora A → ViaCap*, com o produto de fachada mudando de bilhete → e-book → ponto → assinatura. **Não é um player estável que trocou de regime uma vez — é um player em reengenharia jurídica contínua.** A pesquisa anterior captou 1 de 3 movimentos.

### 2.6 Sinais regulatórios

**[E]** Ministério Público citado espontaneamente 4× · Procon 3× · CDC com artigo nominal 2× (art. 6º, art. 20, "Inversão do Ônus da Prova") · SUSEP 1× (como suposto aval do governo) · LOTEP/competência da União 1× · LGPD 2× · e uma reclamação pedindo *"que todos os representantes sejam indiciados, **inclusive os artistas que fazem a propaganda**"* (14/07/2025). **[E]** Reclamantes citam nominalmente artistas e influenciadores que divulgam a marca (nomes omitidos), incluindo um que diz ter comprado pelo link de um influenciador.

---

## 3. Apcap da Sorte — nota alta comprada com resposta, não com produto

### 3.1 Escala real

> **Correção de número — a mais importante desta pesquisa.** A pesquisa anterior registrou *"[n] reclamações, nota [n], nenhum passivo público relevante — o player mais limpo do conjunto"*. Os dois primeiros números eram leitura de janela curta, e **existia um segundo perfil do mesmo grupo que não havia sido localizado**.

**[E]** Índices oficiais do perfil `apcap-da-sorte` ([lista](https://www.reclameaqui.com.br/empresa/apcap-da-sorte/lista-reclamacoes/)):

| Janela | Reclamações | Nota RA | Nota do consumidor | Resolvidas | Respondidas | Tempo médio |
|---|---|---|---|---|---|---|
| 6 meses (02–07/2026) | [n] | **[n]** | [n] | [x%] | [x%] | **[n] dias** |
| [n] meses | [n] | [n] | [n] | [x%] | [x%] | [n] dias |
| 2025 (ano) | [n] | [n] | [n] | [x%] | [x%] | [n] dias |
| 2024 (ano) | [n] | [n] | [n] | [x%] | [x%] | [n] dias |
| **3 anos** | **[n]** | [n] | [n] | [x%] | **[x%]** | [n] dias |

**[E]** A listagem declara literalmente: *"Exibindo 5 de **[n]** reclamações (todas as reclamações ativas da empresa APCAP da Sorte)"*.

**[E] Segundo perfil do mesmo grupo:** [APCAP (`apcap-sp`), marca "Idea Maker"](https://www.reclameaqui.com.br/empresa/apcap-sp/lista-reclamacoes/) — **[n] reclamações ativas**, nota **[n]**, [x%] resolvidas, tempo médio de resposta **[n] dia**.

**Volume real do grupo: [n] + [n] ≈ [n] reclamações ativas** — comparável ao passivo do Viva Sorte na janela equivalente. **[I] Apcap não é um player de baixo volume de reclamação; é um player de volume comparável, distribuído em dois perfis.** A nota alta não vem de menos reclamação — vem de **mais resposta** ([x%] em 3 anos, [x%] em 2024 e 2025). E a nota **melhora monotonicamente** ([n] → [n] → [n] → [n]) enquanto o volume cresce: **a operação de atendimento melhorou mais rápido do que o produto piorou.**

### 3.2 Taxonomia — e o descompasso que explica tudo

**[E] Rótulos oficiais (população = [n]):** Propaganda enganosa [n] ([x%]) · Estorno do valor pago [n] ([x%]) · Prêmio não recebido [n] ([x%]) · Dificuldade de cadastro [n] ([x%]) · Outro problema [n] · Divergência de valores [n].

**[E] Taxonomia por leitura do texto (amostra = [n], multi-rótulo):** compra paga e não entregue **[x%]** · acesso/cadastro travado **[x%]** · prêmio não pago [x%] · saque bloqueado [x%] · estorno negado [x%] · percepção de manipulação [x%] · marketing abusivo/LGPD [x%] · KYC/biometria falhando [x%] · suporte inexistente [x%] · golpe de terceiro [x%].

**[I] O descompasso é o achado mais informativo do painel inteiro.** O rótulo #1 escolhido pelo consumidor é *"propaganda enganosa"* ([x%]), mas na leitura do texto **apenas [x%]** falam de odds ou manipulação. **Os outros [x%] chamam de "propaganda enganosa" uma falha operacional.** O consumidor não tem vocabulário de "falha de entrega" na taxonomia do RA e converte falha de execução em acusação de má-fé. **Num produto de sorteio, toda falha de UX vira acusação de fraude na percepção pública — e vira o rótulo mais tóxico possível para due diligence, para adquirente de pagamento e para regulador.**

### 3.3 O padrão estrutural: o funil é assimétrico entre comprar e receber

**[C]** O arco se repete em dezenas de reclamações, e a ordem importa:

> **Anúncio/WhatsApp → Pix pago ANTES de existir conta → app exige cadastro → cadastro exige biometria facial → biometria falha → dinheiro pago, produto inacessível.**

E, quando o cadastro passa:

> **Ganha prêmio instantâneo → valor cai na carteira do app → saque exige nova validação de identidade → validação falha → dinheiro fica preso na carteira.**

> [relato de consumidor: ganhou um prêmio pequeno no instantâneo e enfrentou erros de validação e bloqueios temporários ao sacar; contrasta a ausência de barreiras para comprar com as dificuldades para sacar]
> — **10/04/2026** **[E]**

E a réplica do mesmo consumidor [n] dias depois, **o achado mais duro de toda a pesquisa**:

> [réplica do mesmo consumidor: depois de enviar todos os documentos, só conseguiu sacar após registrar a reclamação no Reclame Aqui] — 23/04/2026 **[E]**

**[I] Para uma parcela dos casos, o canal efetivo de saque é a reclamação pública, não o app.** Isso explica simultaneamente por que o volume de reclamação é alto **e** por que a taxa de resolução é alta — são a mesma coisa. **O Reclame Aqui virou etapa do fluxo de pagamento de prêmio.**

**[E]** Há um código de erro citado nominalmente pelos consumidores (**erro 0010 / 0011** no reconhecimento facial), e um consumidor registra: *"Fui por impulso e comprei 3 Apcap sem antes consultar o Reclame Aqui. Vi q tem MTAs reclamações iguais as minhas. Erro 0011..."*.

**[I] O provedor de KYC/liveness é o gargalo único que produz simultaneamente as categorias de acesso, saque e biometria — [x%] da amostra tem esse componente. Não são três problemas; é um problema com três sintomas.**

### 3.4 Custo de UX da arquitetura regulatória B

**[E]** As respostas da empresa revelam o que o consumidor achava que comprava vs. o que comprou: *"identificamos que você adquiriu o **E-book do Milhão**, que garante cupons **exclusivamente para o Estouro da Sorte**"* (15/06/2026) · *"você adquiriu um **Pacote Especial Super Quarta** […] toque na aba Cupons e depois em **Super Quarta**"* (30/04/2026) · *"o prêmio recebido foi um **cupom para participação no Sábadão da Sorte, do dia 19 de novembro de 2022**"* (20/04/2026).

**[I]** Uma fração relevante da categoria "compra não entregue" ([x%]) **não é falha técnica: é falha de modelo mental.** O consumidor compra um e-book/pacote e espera "número da sorte"; recebe cupons segmentados por campanha, guardados em abas separadas do app. **A arquitetura B — vender um produto e dar o sorteio como brinde — gera atrito de comunicação que se converte em reclamação registrada como "propaganda enganosa".** Esse é um custo da arquitetura B que a pesquisa anterior não precificou ao comparar A vs. B. **O Seu Milhão, que desenha arquitetura A, não herda esse atrito — e isso é um argumento a favor de A que ainda não está escrito no PRD.**

### 3.5 Padrão de resposta — resolvido fora da plataforma, "resolvido" por exceção manual

**[C]** Todas as [n] respostas lidas seguem o mesmo esqueleto, sem exceção: saudação nominal → narrativa de contato feito **fora do RA**, com datas explícitas → bloco doutrinário reutilizado (aleatoriedade / LGPD / antifraude / instrução de acesso) → convite a usar "canais oficiais". **[I] Personalizada na forma, template no conteúdo.**

**[E]** *"Aproveitamos para informar que **o Reclame Aqui não é um canal direto de atendimento**"* (25/04/2025). **[C]** Em [x%] das respostas a fórmula é *"Durante o atendimento realizado pelo nosso time **via WhatsApp**, você nos informou que…"*. **[I]** A tratativa é integralmente narrada, nunca demonstrada: **a nota alta se apoia numa narrativa não auditável por terceiro.**

**[C] O eufemismo revelador:** quando o problema é saque, a resposta usa sistematicamente *"apresentamos uma **alternativa** para resolver a situação, que foi aceita por você"* — em ao menos 6 respostas distintas. **[I]** Admissão implícita e repetida de que **o trilho de saque padrão não funciona para uma parcela dos ganhadores e a empresa opera um bypass manual**. Não é incidente; é processo estabelecido, com custo operacional recorrente escondido.

**[C] "Não obtivemos retorno" como mecanismo de encerramento:** a empresa lista 3–4 tentativas de contato com datas e encerra atribuindo a ausência de solução ao consumidor. **[I]** Efeito no índice: a reclamação fica `ANSWERED` + `solved=false` + **sem avaliação do consumidor** — **não entra no denominador de "resolvidas" e não pesa contra a nota**.

**[E] Quem avalia — e por que a nota alta é seletiva:** na janela de 6 meses, [n] reclamações e **apenas [n] avaliadas ([x%])**. Das 9 notas capturadas na amostra aberta: notas **10** foram para opt-out de marketing (×2), bypass manual de saldo e orientação de navegação; notas **0 e 1** foram para insatisfação com odds e **exclusão de cadastro negada**. **[I] As notas 9–10 concentram-se em casos cuja "solução" custa quase nada. Os casos caros terminam sem avaliação. A nota [n] mede a eficiência do opt-out de marketing, não a confiabilidade do pagamento de prêmio.**

### 3.6 Tendência temporal — três ondas, e a direção errada

**[I]** Três ondas distinguíveis na amostra de [n]:

1. **~mai–ago/2025:** onda de **telemarketing por robocall**. Sete reclamações consecutivas exclusivamente sobre ligações — *"mais de [n] ligações em meia hora num sábado à noite"*; uma identifica a locução como a voz gravada de uma celebridade de TV, ligando quase de cinco em cinco minutos.
2. **~set/2025–jan/2026:** pico de **acesso/cadastro ([x%])** e estorno ([x%]).
3. **~abr–ago/2026:** o telemarketing por voz some e **é substituído por WhatsApp em massa**; o eixo migra para o fim do funil — **saque bloqueado ([x%]) e prêmio não pago ([x%]) dominam os últimos 3 meses**.

**[I]** A migração de "não consigo entrar" (2025) para "não consigo sacar" (2026) é o que se espera quando a base amadurece. **É a pior direção possível de deslocamento**, porque falha de saque é o único tipo de reclamação que um regulador ou um adquirente de pagamento lê como risco material.

### 3.7 Sinais regulatórios

**[E] SUSEP invocada pela própria empresa como escudo contra pedido de exclusão de dados sob LGPD:**

> *"após a aquisição de qualquer produto, seja e-book, título de capitalização ou bilhete, algumas informações podem ser mantidas por exigências legais e técnicas. Esse procedimento segue, entre outras normas, a **Circular SUSEP nº 605**, que determina a guarda dos dados das operações […] pelo prazo mínimo de 5 anos."*
> — resposta em 30/03/2026. Réplica: *"Vieram com aquela conversa de resolução da SUSEP e que o cadastro fica 5 anos até ser excluído."* **Status final: NOT_SOLVED, nota 1** **[E]**

**[E] Enquadramento como jogo de azar, por consumidor:**

> [relato de consumidor, motivado pelas perdas de um familiar, que compara o aplicativo a plataformas de cassino ilegais — "única diferença é que essa é regulamentada"]
> — **18/01/2026**, **NOT_SOLVED** **[E]**

**[E]** Procon citado nominalmente em ao menos 2 casos · LGPD como fundamento explícito em ≥5 casos, incluindo descumprimento de compromisso anterior de descadastro · questionamento da base legal do "Globo Virtual" como método de sorteio (16/04/2025).

**[E] Um caso grave por outra razão:** a compensação oferecida por falha foi **em cupons de sorteio, não em dinheiro** — e o consumidor voltou a reclamar porque os cupons também não premiaram. **[I] Compensar falha de sorteio com mais sorteio realimenta o ciclo.**

**[C] Golpe de terceiro** é só [x%] da amostra, mas a empresa mantém bloco de resposta dedicado: *"O Apcap da Sorte **não entra em contato com ganhadores pelas redes sociais**. Todos os contatos oficiais são feitos exclusivamente por telefone ou WhatsApp […] **nunca solicitamos pagamentos para liberar premiações**."* **[I]** Esse bloco é ao mesmo tempo a melhor prática de comunicação da amostra **e** um passivo: o canal legítimo da empresa é telefone e **WhatsApp de números variados** (*"mesmo bloqueando eles me enviam mensagens por outros números"*). **Uma marca que faz outbound massivo por WhatsApp de números rotativos destrói a capacidade do consumidor de distinguir a empresa do golpista.**

**[I] Nota de precisão sobre a correção:** não foi encontrada nenhuma autuação da SUSEP, ação civil pública ou decisão judicial contra Apcap/Idea Maker/emissora. **A avaliação "nenhum passivo público relevante" da pesquisa anterior continua correta quanto a *ato de autoridade*, e passa a estar incorreta quanto a *volume e conteúdo do passivo reputacional*.**

---

## 4. Familhão — a melhor reputação do painel, com o maior volume absoluto

### 4.1 Escala real

**[E]** Perfil localizado: `reclameaqui.com.br/empresa/familhao-programa/`, confirmado pelo CNPJ exibido na própria página. A pesquisa anterior não achou porque o slug não é `familhao` nem `familhao-engajamento`.

| Métrica | Jan–Jun/2026 | **Fev–Jul/2026** |
|---|---|---|
| Reclamações na janela de 6 meses | [n] | **[n]** |
| Nota RA | [n]/10 | **[n]/10** |
| Reputação | RA1000 | **RA1000** |
| Respondidas | [x%] | **[x%]** |
| Resolvidas | [x%] | **[x%]** |
| Nota média do consumidor | [n] | **[n]** |
| Tempo médio de resposta | [n] | **[n]** |

**[E] Reclamações ativas acumuladas: [n]** ([lista](https://www.reclameaqui.com.br/empresa/familhao-programa/lista-reclamacoes/)). Selo **Empresa verificada** + **1º lugar na categoria "Programas de fidelidade"**; RA1000 em todos os 6 meses da série.

> **Correção de número — em duas direções opostas.** O "[n]" da matéria do FDR **não é o acumulado**: é a janela móvel de 6 meses da época. O acumulado é **~[n]× maior**. Mas a pesquisa anterior simultaneamente **superestimou o dano**: com [n] reclamações em 6 meses, o Familhão tem **a melhor reputação de todo o painel**. **[E]** A matéria do FDR (25/05/2026) **não cita nota nem período** (FDR; link omitido) — usou o número absoluto descontextualizado no gancho da crise do Bolsa Família. **[I] É artefato de pauta, não medida de qualidade; citá-lo como evidência de baixa qualidade replica o erro.**

### 4.2 Taxonomia — não é reclamação de sorteio

**[E] Tags oficiais (top-6, somam [n] dos [n] — há cauda longa não exposta):** Cobrança indevida **[n] ([x%])** · Outro problema [n] · Produto não recebido [n] ([x%]) · Propaganda enganosa [n] ([x%]) · Estorno do valor pago [n] · Dificuldade de cadastro [n].

**[E] Categorias:** Não encontrei meu problema [n] · **Financeiras [n]** · Programas de Fidelidade [n] · Sites e portais [n] · **Bancos [n]**. **[I]** [n] consumidores classificaram um clube de assinatura como "Financeiras"/"Bancos": é o **débito recorrente** sendo percebido como relação bancária.

**[E] Amostra lida (n=[n]):** créditos/Lojão (saldo não aparece, resgate travado, mínimo, frete) **[x%]** · raspadinha "Achou, Levou!" [x%] · cobrança recorrente + dificuldade de cancelar [x%] · pagamento feito mas não reconhecido [x%] · sorteio/desconfiança de lisura [x%] · acesso/login [x%] · propaganda enganosa [x%] · entrega física [x%] (**emergente, só em ago/2026**) · golpe de terceiro [x%].

**[I] O achado central:** o Familhão **não é reclamado como produto de sorteio — é reclamado como e-commerce e como assinatura**. Créditos + entrega + cobrança-não-reconhecida ≈ **[x%]** da amostra. A camada de sorteio é [x%], e majoritariamente **dúvida**, não acusação. É exatamente o esperado da arquitetura regulatória C: **quem vende clube de benefícios herda o passivo de varejo, não o de loteria.**

### 4.3 Verbatim que mais revela

**A regra da raspadinha, admitida pela própria empresa** — e por que ela gera reclamação:

> *"para que haja premiação, é necessário encontrar **três valores iguais** na mesma cartela. […] Quando a cartela é totalmente raspada e não apresenta três valores iguais, **ela é automaticamente encerrada pelo sistema e some da tela**. […] o valor pago pela cartela não é perdido. Ele **retorna ao participante em forma de benefícios dentro do próprio Achou Levou**"* — atendente do Familhão, 2026 **[E]**

> [relato de consumidor: encontrou o valor premiado na raspadinha Achou, Levou!, o sistema disse que não ganhou e a cartela sumiu rapidamente]
> — **08/01/2026**, tag *Propaganda enganosa*, **resolvida** **[E]**

> [relato de consumidor: resgate muito limitado, com taxa para cupons pré-determinados de lojas caras; defende o saque dos prêmios para a conta bancária]
> — **23/04/2025**, **não resolvida** **[E]**

**[I] Duas falhas de produto embutidas:** (a) a cartela perdedora **desaparece sem recibo**, então o consumidor não consegue provar nada e conclui má-fé; (b) "seu dinheiro não é perdido, vira benefício" é devolução em moeda fechada com taxa de R$ [valor] e catálogo restrito — economicamente é perda, e o consumidor lê como tal. **A ausência de comprovante é o defeito de maior alavancagem: é barato emitir e desativa a acusação de fraude na origem.**

**A reclamação mais pesada da amostra:**

> [relato de consumidor de baixa renda, em situação de vulnerabilidade, pedindo de volta o saldo retido no programa e criticando os preços do catálogo]
> — **08/04/2026**, **não resolvida** **[E]**

**[I]** Materializa o contraste que a imprensa fez de forma retórica: R$ [valor] acumulados por uma beneficiária, retidos em moeda de catálogo, num produto vendido em horário nobre. Não é problema de reputação — **é problema de desenho de resgate**.

**Objeção de compra registrada como reclamação:**

> *"Ninguém consegue ver as datas dos sorteios, os nomes e cidades dos ganhadores!!!! **Ainda não comprei pq não vejo nada sobre quem já ganhou!!!**"*
> — **30/06/2024**, *em réplica* **[E]**

**[I]** O consumidor diz explicitamente que *não comprou* por falta de prova pública de ganhador. **Confirma, por evidência direta de consumidor, que a falta de prova pública é fricção de conversão mensurável, não só de retenção** — e valida o whitespace de "transparência do mecanismo" apontado na pesquisa de criativo.

**O defeito de UI que sobreviveu [n] meses:** **[E]** uma reclamação de 05/02/2026 (*"ao acessar a página, só aparece a opção 'Assinar o Familião'"*) tem texto **quase idêntico** a uma de 09/09/2024 (links omitidos).

**O CRM disparando contra pagante ativo:** **[E]** *"paguei os R$ [valor] mensal do Familhão ontem, hoje recebi uma mensagem dizendo que perceberam que eu não vou participar do sorteio desse mês, pedindo pra eu pagar. Sendo que paguei ontem. **esse Familhão do verificado azul, é falso!**"* (08/09/2025). **[I]** Uma régua de cobrança que não lê o estado de pagamento converte cliente adimplente em reclamante público. É falha de integração, e a mais barata de corrigir de toda a pesquisa.

### 4.4 Padrão de resposta — o único atendimento genuinamente personalizado do painel

**[E]** Métricas medidas nas [n] respostas datadas: mediana **2 dias** · [x%] em ≤1 dia · [x%] em >7 dias · menciona contato privado em [x%] · emoji/identidade de marca em [x%] · nº de protocolo em [x%] · explicação didática da regra de negócio em [x%].

**[E] Assinatura do padrão:** resposta **nominal em ambos os lados** ("Oi [nome do consumidor]", "Aqui é a [nome da agente], do time Familhão"), agente identificado por nome + função — *"[nome] | Especialista de Reclame Aqui"*, *"[nome], especialista da **Ouvidoria** Familhão"*.

**[C] Não é template genérico.** Cada resposta cita o dado específico do caso. Em vários casos a empresa **resolve e estorna antes de responder publicamente**: *"a assinatura já foi cancelada e **o estorno do valor de R$ [valor] pago no dia 23/11 já foi realizado**. O comprovante foi enviado de maneira privada."*

**[E] Escalada de estrutura:** o Familhão publicou no RA um post institucional **"📢 Quando procurar a OUVIDORIA do Familhão?"** em **13/02/2026** ([link](https://www.reclameaqui.com.br/empresa/familhao-programa/conteudos/quando-procurar-a-ouvidoria-do-familhao_9NKzZCBkaZaKz-ex/)). **[I]** Criar ouvidoria formal é resposta a volume, não a marketing.

**[E] O único ponto fraco do playbook — deflexão para o banco:** *"**O Familhão não tem acesso à sua conta bancária** […] **Toda a cobrança é executada pelo banco** […] basta cancelar a autorização diretamente no aplicativo do seu banco."* **[I]** Tecnicamente correto e estrategicamente frágil: transfere ao consumidor a tarefa de navegar o app do banco — e a amostra mostra que ele não consegue (num caso, **nem o funcionário da agência Bradesco localizou a opção**). É a única parte do playbook que produz réplica em vez de resolução.

**[I] Leitura consolidada:** o Familhão trata o Reclame Aqui como **canal de atendimento operado**, não como crise de PR — equipe dedicada (o nome literal usado pelos agentes é "time Reclame Aqui do Familhão"), SLA agressivo, resolução antes da resposta pública, tom de marca preservado. **É isso, não a ausência de problemas, que produz nota [n] sobre [n] reclamações.**

### 4.5 Tendência temporal

**[E]** Janela móvel: **[n] (Jan–Jun/26) → [n] (Fev–Jul/26)**, com nota subindo e resolução subindo. Volume em queda, qualidade em alta.

**[E] Crise Bolsa Família (mai/2026) — não há evidência de pico correlato no RA.** Nenhuma reclamação da amostra menciona a declaração do apresentador. A única menção ao programa é uma consumidora descrevendo **a própria condição** (08/04/2026), **anterior** à polêmica de 25/05/2026. **[I] A crise foi midiática, não de base de clientes.**

**[E] Deriva do mix em ago/2026:** nas 10 reclamações de 12–14/08/2026 aparecem tipos **ausentes de todo o histórico anterior** da amostra — atraso de entrega física com pedido de rastreio (Kit Havanna), cobrança de múltiplos fretes na mesma loja, suspensão temporária impedindo resgate. **[I] O Familhão está migrando de "clube de sorteio com catálogo" para marketplace de verdade — e importando o passivo de e-commerce (frete, prazo, rastreio, SKU esgotado) junto.** É o risco de médio prazo mais subestimado do modelo: a camada de benefício que sustenta a recorrência é também a que gera reclamação de logística, uma operação inteiramente diferente da de sorteio.

### 4.6 Sinais regulatórios — o resultado negativo é o achado

**[E]** Busca de termos nos [n] textos lidos:

| Termo | Ocorrências |
|---|---|
| **SUSEP** | **0** |
| **capitalização / título de capitalização** | **0** |
| **pirâmide** | **0** |
| **fraude** (a palavra) | **0** |
| **advogado / justiça / judicial** | **0** |
| **loteria federal** (dito pelo consumidor) | **0** |
| Procon | 4 (sempre como ameaça, nunca como processo relatado) |
| "enganação / enganoso / enganado" | [n] |
| CDC com artigo citado | 1 |
| nome do apresentador citado (inclusive com grafia errada) | [n] |

**[E] A única invocação jurídica técnica de toda a amostra** — e a mais perigosa, porque é a única de alto risco **sem resposta da empresa**:

> *"conforme estabelecido pelos **artigos [n] e [n] do Código de Defesa do Consumidor**, que tratam do cumprimento da oferta e propaganda enganosa"*
> — **31/10/2025**, sobre um produto de catálogo prometido ao vivo no programa dominical da Globo e indisponível no dia seguinte; **não resolvida, sem resposta** **[E]**

**[I]** Oferta de resgate anunciada ao vivo em TV cria pico de demanda que o estoque não absorve, e o CDC art. 30/35 tipifica isso diretamente.

**[I] Duas conclusões:**
1. **A percepção de risco do consumidor do Familhão é inteiramente consumerista, nada financeira.** Ninguém pergunta se é regulado, quem é o emissor, se tem SUSEP. Ele compra do **apresentador e da Globo**, não de uma estrutura jurídica. Isso corrobora empiricamente que "ser SUSEP" não é ativo percebido pelo consumidor — e vai além: **o consumidor não sabe que a categoria existe.** A regulação é ativo de defesa jurídica e de mídia, não de conversão.
2. **A palavra que aparece é "enganação" ([n]×), não "golpe" nem "pirâmide".** O sentimento é de **promessa não cumprida**, não de crime. Distinção operacionalmente importante: **"enganação" é curável por UX e SLA; "golpe" é curável só por prova pública.** O Familhão está no lado barato do problema; Viva Sorte e Pix do Milhão, com reclamação de prêmio não pago, não estão.

---

## 5. SBT Prêmios — gap fechado, e o player com a maior taxa de reclamação por mês de vida

### 5.1 Onde as reclamações moram — arquitetura de dois perfis

**[E]** Perfil comercial: [SBT Prêmios](https://www.reclameaqui.com.br/empresa/sbt-premios/) — CNPJ da própria emissora, cadastrado no RA há 8–9 meses (≈dez/2025, coerente com o lançamento).

**[E] Esse CNPJ pertence a TVSBT CANAL 4 DE SÃO PAULO S/A** — a emissora de TV, atividade principal "televisão aberta" (consulta pública de CNPJ; links omitidos).

**[I] Isso é decisão estrutural, não detalhe cadastral.** O SBT colocou o **CNPJ da emissora de TV** como interlocutor de consumo do produto financeiro. Toda reclamação de título de capitalização cola na marca de mídia, não numa subsidiária descartável. **É o oposto exato do desenho de blindagem de Viva Sorte e Pix do Milhão.**

**[E]** Segundo perfil: parte relevante das reclamações sobre SBT Prêmios está registrada contra **[Icatu Seguros](https://www.reclameaqui.com.br/empresa/icatu-seguros-1)** — busca interna por `sbt` naquele perfil retorna **[n] reclamações**. **[E]** Há ainda vazamento para um terceiro perfil: reclamação de 14/08/2026 sobre SBT Prêmios registrada no perfil do **Viva Sorte**.

> **Correção de número.** Volume real ≈ **[n]+ reclamações em ~8 meses** ([n] ativas no perfil próprio + ~[n] no perfil da Icatu), não os [n] do headline de 6 meses. **[I]** Comparação de volume que use só o perfil comercial subestima o SBT Prêmios em [x%] — e o mesmo viés provavelmente afeta os outros players.

### 5.2 Correção de emissora

> **Correção material.** A pesquisa anterior registra **Liderança Capitalização** como emissora. **Isso é verdadeiro apenas para a fase atual.**

**[E]** Cadeia de evidência: as condições gerais do produto declaram *"**Icatu Capitalização S.A.** é a sociedade responsável pela emissão, administração, registro, realização dos sorteios"* ([termos](https://sbtpremios.com/termos-de-uso), [condições gerais](https://demo.sbtpremios.com/condicoes-gerais)) · consumidor descreve o comprovante do Pix em 29/12/2025: *"No valor de [valor] **recebei Icatu capitalização S/A**"* · respostas assinadas *"Núcleo Gestão de Reclamações / Icatu"* em jan–mar/2026 · resposta do SBT em 22/04/2026: *"os processos de análise são realizados pela **Icatu Seguros**, empresa parceira responsável pela operação financeira"* · consumidor em 13/08/2026: *"fiz dois depositos **através da liderança capitalização** […] para o sbt premios"*.

**[I] Registro correto: *emissora: Icatu → Liderança (troca em 2026)*.** Trocar de emissora SUSEP em menos de 6 meses de operação é sinal de que o arranjo inicial não funcionou — e é dado direto para a decisão de fornecedor do Seu Milhão: **a escolha de emissora é reversível, mas o custo aparece na experiência do cliente.**

### 5.3 Reputação e taxonomia

**[E]** 01/02–31/07/2026: nota **[n]/10** ("Ótima") · **[n]** reclamações na janela · **[n] ativas** · **[x%] respondidas** · [x%] resolvidas · [x%] voltariam a fazer negócio · nota do consumidor [n] · **tempo médio 9 dias e [n] horas** · 5º no ranking de Capitalização.

**[I]** O gap entre [x%] respondidas e [n] é o número mais informativo: a empresa **responde quase tudo, mas devagar**. Para um produto de edição semanal, resposta em 9 dias chega depois do sorteio.

**[E] Facetas oficiais ([n] de [n] têm tag — [x%]):** Produto não recebido **[n] ([x%])** · Propaganda enganosa [n] ([x%]) · Sorteios-Concursos [n] ([x%]) · Problemas na finalização da compra [n] · Estorno [n]. **Categorias:** Títulos de capitalização [n] · **Emissoras de rádio-TV [n]** · Não encontrei meu problema [n].

**[I]** "Emissoras de rádio-TV" como 2ª categoria ([n]) e 2º produto ([n]) é a prova quantitativa da §5.1: **uma fatia grande dos consumidores não está reclamando de um produto financeiro — está reclamando do SBT. O selo de confiança virou o para-raios.**

**[C] Amostra recente (n=[n], ~22/07 a 14/08/2026):** pagou via Pix e não recebeu título/giro **[x%]** (subtipos: tela "atualizando seus títulos" [x%], "não tenho giros disponíveis" [x%], números do sorteio não entregues [x%]) · prêmio ganho e não pago [x%] · percepção de manipulação da roleta [x%].

### 5.4 Verbatim que mais revela

**A falha de capacidade sob pico de tráfego televisivo:**

> *"Fiz a compra no site **escaneando o QR code mostrando na tv** e meus títulos não carrega, se for enganação quero reembolso."* **[E]**

> [relato de consumidor: comprou títulos durante programas de auditório do SBT, mas o pião da sorte não aparece e os títulos ficam "atualizando", sem nenhum número]
> — **23/07/2026** **[E]**

**[C] Correlação temporal decisiva:** as reclamações de falha de entrega se agrupam em torno das **transmissões ao vivo de domingo**, com compra por QR code exibido na TV. Programas citados espontaneamente: Domingo Legal (07/12/2025 — domingo; 26/07/2026 — domingo) e outros programas de auditório do SBT.

**[I] O achado mais acionável do relatório para o Seu Milhão.** A falha não é aleatória: chamada na TV aberta → milhares de Pix simultâneos → a conciliação não dá conta → o título não materializa na conta. **O SBT tem o canal de aquisição mais barato do setor (mídia própria) e está queimando a conversão exatamente no pico.**

**A reclamação-âncora, nunca respondida:**

> [relato de consumidor: dezenas de giros seguidos na roleta sem nenhum prêmio; questiona a aleatoriedade e pede esclarecimentos formais sobre o algoritmo e sobre auditoria independente]
> — **08/12/2025** — **Não respondida / Não resolvido** **[E]**

**Denúncia com enquadramento jurídico completo**, referente à mesma transmissão de 07/12/2025:

> *"**Propaganda Enganosa (Art. 37 do CDC)** […] **Jogo de Azar Proibido:** embora o produto possa ser formalmente registrado como Título de Capitalização, a mecânica da roleta virtual […] possui as características de um jogo de azar, o que é estritamente regulamentado e, em muitos casos, proibido no Brasil (**Decreto-Lei nº 9.215/46 e Lei de Contravenções Penais, Art. 50**) […] configurando **vício do serviço (Art. 20 do CDC)** […] solicito que revisem urgentemente as campanhas publicitárias para que reflitam a real (e aparentemente ínfima) chance de ganho."*
> **[E]**

**Um manual de UX ao contrário:**

> *"Esse jogo não é confiável. Dez giros da sorte e só uma opção de perder, e todos os giros só cai na opção de perda […] **qnd a roleta vai perdendo a força ela só perde na casa anterior p justamente cair na perda. nunca cai uma casa depois, pq já seria o prêmio.**"*
> — **06/08/2026** **[E]**

**[I]** A animação da roleta **desacelera e para uma casa antes do prêmio**, e o usuário lê isso como prova de fraude. É erro de *design de animação*, não de RNG — mas produz acusação de crime. **Em mecânica de prêmio instantâneo, a curva de desaceleração da animação é decisão de compliance, não de motion design.**

**A erosão explícita do selo SBT** — o padrão mais estratégico do relatório:

> *"**Logo o SBT, uma empresa tão séria, enganando os outros?** Será que é pq dizem que a **emissora está falindo**, aí estão arrancando dinheiro fácil assim do povo?"* — 18/02/2026 **[E]**

> *"**Confiando na credibilidade da emissora** e na forma como o produto foi apresentado […] adquiri…"* — dez/2025 **[E]**

> *"mais uma **Telesena** da vida que ninguém ganha, mas aparece **os atores da vida** para mostrar o êxito só SBT"* — 31/03/2026 **[E]**

> *"Isso aí é enganação. Gastei mais de [valor] e nunca deu nada. **Pior que casa de apostas — lá vc consegue recuperar o dinheiro.**"* **[E]**

**[I]** O SBT emprestou seu ativo mais caro — [n] anos de credibilidade de TV aberta e os rostos de seus apresentadores — para vender um título de R$ [valor]. O consumidor **declara explicitamente que comprou por causa do selo**. Quando o título não chega, ele não conclui "o site falhou" — conclui "**o SBT me enganou**". **Emprestar credibilidade de terceiro (celebridade, emissora, marca conhecida) não é hedge de risco — é alavancagem de risco.**

### 5.5 Padrão de resposta — bimodal e enviesado contra o consumidor

**[C] Dois regimes, separados pela troca de emissora:**

| | **Regime 1 — Icatu** (dez/25 – ~abr/26) | **Regime 2 — SBT Prêmios** (mai – ago/26) |
|---|---|---|
| Assinatura | *"Núcleo Gestão de Reclamações — Icatu"* | sem assinatura corporativa; 1ª pessoa |
| Tom | Jurídico-defensivo | Cordial-comercial |
| Canal de resolução | **Telefone** (*"realizamos diversas tentativas de contato por telefone, sem sucesso"*) | **WhatsApp** (*"conforme alinhado em nosso atendimento por WhatsApp"*) |
| Reembolso | *"não há possibilidade de devolução do valor"* | encaminha para a Icatu |

**[I]** A migração do canal de resolução de **telefone → WhatsApp** é provavelmente a causa isolada mais importante da recuperação de reputação. No regime 1, a frase recorrente é *"tentativas de contato, sem sucesso"* — **o público do produto (TV aberta, classe C/D) não atende telefone desconhecido**. Mesmo produto, mesmo bug, canal diferente, +[n] pontos de nota.

**[E] Tempos medidos ([n] reclamações respondidas):**

| Tipo | Tempo até resposta |
|---|---|
| Falha de entrega ("PIX perdidos", 14/08/26) | **[n] minutos** |
| Falha de entrega (03/08/26) | [n] minutos |
| Manipulação da roleta (31/03/26) | 6 horas |
| Pedido de reembolso (12/04/26) | 10 dias |
| **Prêmio ganho e não pago (28/07/26)** | **[n] dias** |
| **Roleta / [n] giros (08/12/25)** | **nunca respondida** |

**[I] O ordenamento é claro e consistente: quanto mais o caso implica devolver ou pagar dinheiro, mais lenta a resposta.** Casos de "não recebi o título" (custo marginal ≈ zero, o título já existe) são atendidos em menos de 1 hora. E na amostra de [n] reclamações completas, **todas as 3 não resolvidas são de fairness/reembolso; todas as resolvidas são de falha de entrega**. **Os [x%] de resolução descrevem majoritariamente a empresa consertando um bug de sessão que ela mesma causou.**

**[E] Workaround canonizado:** o mesmo bloco *"saia da conta e atualize a página […] acesse novamente com seu CPF e telefone […] Selecione 'Meus Títulos'"* aparece literalmente em ao menos 4 respostas distintas entre jun e ago/2026. **[I] A empresa conhece o bug há 3+ meses e escolheu operacionalizar o workaround em vez de corrigir a causa.**

### 5.6 Tendência temporal e sinais regulatórios

**[E] Reputação:** Fev/26 sem índice → Mar **Não recomendada** → Abr Regular → Mai Boa → Jun Boa → Jul **Ótima**. **[I]** Recuperação de 4 meses, coincidente com três eventos simultâneos (troca de emissora, mudança de canal de atendimento, mudança de tom) — não isoláveis com dados públicos.

**[I] O sinal precoce que importa:** o SBT Prêmios entrou em dez/2025 e em **8 meses acumulou ~[n] reclamações**. Normalizando por tempo de operação, **é o player com a maior taxa de reclamação por mês de vida do grupo**. O que o salva na nota é a máquina de SAC, não a qualidade da entrega.

**[E] SUSEP aparece exclusivamente como escudo da empresa, nunca como canal do consumidor:** *"O produto é um título de capitalização, amparado por lei e regularizado e fiscalizado pela SUSEP […] através da Circular 656 e Resolução CNSP 384. **Por isso, não é um jogo de azar.**"*

**[E] Divulgação de odds como argumento de defesa:** a empresa cita a probabilidade de contemplação prevista nas condições gerais (tópico X SORTEIO, item 10.6, letra 'd') — [n] números premiados em [n] números da série. **[I]** Isso é uma fração ínfima por título, e a empresa usa o número como prova de que o consumidor foi informado — **peça de compliance transformada em resposta de SAC**.

**[I]** Nenhuma reclamação da amostra menciona ter acionado SUSEP ou Procon. O consumidor cita **CDC e Lei de Contravenções Penais**. **O risco jurídico prático deste modelo, hoje, não vem do regulador setorial — vem do sistema de defesa do consumidor e do enquadramento como jogo de azar. O selo SUSEP é defesa eficaz contra o regulador e inútil contra o Procon/CDC.**

---

## 6. Tabela comparativa final

| | **Viva Sorte** | **Pix do Milhão** | **Apcap da Sorte** | **Familhão** | **SBT Prêmios** |
|---|---|---|---|---|---|
| **Volume real corrigido** (ativas) | **[n]** [E] *(antes: [n] = janela 6m)* | **[n]** [E] *(antes: sem número)* | **~[n]** em 2 perfis ([n] + [n]) [E] *(antes: [n])* | **[n]** [E] *(antes: [n] = janela 6m)* | **~[n]+** em 8 meses ([n] + ~[n] no perfil Icatu) [E] *(antes: não identificado)* |
| Volume na janela de 6m (fev–jul/26) | [n] [E] | [n] [E] | [n] [E] | **[n]** [E] | [n] [E] |
| **Nota (6 meses)** | **[n]** — Regular [E] | **[n] — RA1000** [E] | [n] [E] · perfil irmão [n] [E] | **[n] — RA1000** [E] | [n] — Ótima [E] |
| Nota do consumidor | [n] [E] | [n] [E] | [n] [E] | [n] [E] | [n] [E] |
| **Taxa de resposta** | **[x%]** · [n] aguardando [E] | **[x%]** [E] | **[x%]** ([x%] em 3 anos) [E] | **[x%]** [E] | **[x%]** [E] |
| **Tempo médio de resposta** | **[n]d 19h** [E] *(VIA Cap: [n])* | [n] [E] | [n]d [E] *(perfil irmão: [n]d)* | **[n]** [E] | [n] [E] |
| % resolvidas | [x%] [E] | [x%] [E] | [x%] [E] | [x%] [E] | [x%] [E] |
| **Tipo dominante (faceta oficial)** | Propaganda enganosa [n] ([x%]) [E] | Propaganda enganosa [n] ([x%]) [E] | Propaganda enganosa [n] ([x%]) [E] | **Cobrança indevida** [n] ([x%]) [E] | **Produto não recebido** [n] ([x%]) [E] |
| **Tipo dominante (leitura do texto)** | **Golpe de terceiro usando a marca** [x%] [E, amostra] | **Prêmio instantâneo exibido e não pago** [x%] [E, amostra] | **Compra não entregue [x%] + acesso travado [x%]** [E, amostra] | **Créditos/Lojão [x%] + raspadinha [x%]** [E, amostra] | **Falha de entrega pós-Pix [x%]** [C, amostra recente] |
| **Natureza do passivo** [I] | Falsificação da marca + atraso de prêmio | Defeito de design da camada instantânea | Gargalo único de KYC/liveness | E-commerce e assinatura (não sorteio) | Capacidade sob pico de tráfego de TV |
| **SUSEP citada** | Só como *fonte de consulta de prazo* (1×) [E] | Como **suposto aval do governo** (1×) [E] | Pela **empresa**, contra pedido LGPD (Circular 605) [E] | **0 ocorrências** [E] | Só como **escudo da empresa** [E] |
| **Procon / MP / CDC citados pelo consumidor** | Procon 1 · CDC art. 47 · elementos de propaganda enganosa [E] | **MP 4 · Procon 3 · CDC arts. 6/20** [E] | Procon 2 · **LGPD ≥5** · "cassino ilegal" [E] | Procon 4 · **CDC arts. 30/35 (1×, sem resposta)** [E] | **CDC arts. 37/20 · DL 9.215/46 · LCP art. 50** [E] |
| **"Golpe" / enquadramento criminal** | Alto (censurado pelo RA em ~[n]/[n]) [E] | Alto ([x%] da amostra) [E] | Alto (títulos inteiros censurados) [E] | **Baixo** — "enganação" [n]× · "fraude" 0 [E] | Médio — tese de jogo de azar [E] |
| **Padrão de resposta** | **Templatizado** — 3 blocos verbatim; T2 deflete p/ WhatsApp e correlaciona com não-resolução [E/C] | **Templatizado por tipo** — 4 templates; jurídico copiado literal em 3 respostas no mesmo dia, negando o prêmio [E] | **Personalizado na forma, template no conteúdo** — resolução narrada via WhatsApp, não auditável [C] | **Genuinamente personalizado** — agente nominal, protocolo, estorno antes da resposta pública, ouvidoria formal [E/C] | **Bimodal** — <1h p/ falha de entrega, [n]d p/ prêmio não pago, **nunca** p/ questionamento de lisura [C] |
| **Tendência temporal** | **Piorando** — latência de <3d (2024) → ~[n]d (2026); mix migrando p/ saque/estorno/"roleta Pix" [E/C] | **Melhorando na forma** — Boa→RA1000 em 6 meses; passivo mudou de natureza junto com o modelo de negócio [E/C] | **Melhorando na nota, piorando no eixo** — nota [n]→[n]; gargalo migrou de onboarding (2025) p/ **saque (2026)** [E/I] | **Estável/melhorando** — volume caindo, nota subindo; **novo passivo logístico emergindo** em ago/2026 [E/I] | **Recuperação forte** — Não recomendada (mar/26) → Ótima (jul/26); mas **maior taxa de reclamação por mês de vida** do painel [E/I] |

---

## 7. Lições para o Seu Milhão

A separação abaixo é a parte operacional deste documento. **Padrão estrutural** = falha que aparece em 3+ players com desenhos de negócio diferentes, o que sugere causa no nicho e não na competência de quem executa — logo, **oportunidade de diferenciação defensável**. **Padrão específico** = falha de execução de um player, evitável com processo — **serve como checklist, não como estratégia**.

### 7.1 Padrões ESTRUTURAIS do nicho — todo mundo erra, logo há espaço

#### E1. A camada de prêmio instantâneo é o maior gerador de atrito do setor inteiro

**[E]** Aparece em **todos os cinco players**, com a mesma anatomia:

| Player | Manifestação | Peso |
|---|---|---|
| Pix do Milhão | Animação exibe prêmio, tela avança sozinha; defesa oficial: *"caráter meramente ilustrativo e recreativo"* | **[x%] da amostra**; [n] tags de propaganda enganosa |
| Viva Sorte | [raspadinha exibiu prêmio alto e pagou valor simbólico] — prêmio em **crédito** vestido de dinheiro; regra de "3 iguais" ambígua | [x%] da amostra |
| Familhão | Cartela perdedora **some sem recibo**; devolução em moeda fechada com taxa de R$ [valor] | [x%] da amostra |
| SBT Prêmios | Roleta **desacelera e para uma casa antes do prêmio**; [n] giros sem ganho, nunca respondido | [n] tags + reclamação-âncora nunca respondida |
| Apcap | Prêmio instantâneo cai na carteira e **não sai** | [x%] saque bloqueado |

**[I] O denominador comum tem três componentes, e cada um é uma decisão de produto:**
1. **A animação exibe um resultado que não é o resultado.** O sorteio real acontece no backend; a UI é decorativa. Juridicamente defensável (está no regulamento), experiencialmente indefensável.
2. **Não existe comprovante persistente.** A cartela/roleta some, e o consumidor não consegue provar nada — então conclui má-fé. *"pq não deixam salvo o nosso registro de raspadinhas?"*
3. **O prêmio "instantâneo" frequentemente não é dinheiro** — é crédito, cupom ou saldo em carteira com trilho de saque quebrado.

**A oportunidade:** fazer a raspadinha ser **o próprio evento de premiação** — resultado determinístico exibido = resultado pago — com **histórico persistente e auditável na conta do usuário** e **declaração de natureza (crédito vs. Pix) antes da animação de vitória**. É barato, é verificável e ataca a maior fonte de atrito de quatro concorrentes de uma vez.

→ **PRD §6.10** ("regra de negócio da raspadinha nunca especificada", severidade 🟡 MÉDIO). **[I] Esta pesquisa argumenta pela reclassificação para 🔴 CRÍTICO**: não é lacuna de especificação, é o principal passivo reputacional do setor.
→ **Q-R3** (raspadinha é modalidade admitida sob SUSEP?) e **Q-P5** (regra de negócio) — **evidência nova substancial**. A pergunta que faltava ao backlog: *o prêmio instantâneo é pago em dinheiro ou em crédito, e a tela de resultado declara isso antes da animação?*

#### E2. A marca de sorteio é, por construção, um vetor de fraude de terceiros

**[E]** Presente em 4 dos 5 players, com o mesmo roteiro: contato ativo não solicitado (WhatsApp / videochamada / Kwai) → anúncio de prêmio → **taxa pequena** (R$ [valor] a R$ [valor]) para "liberar", "converter", "frete", "nota fiscal" → segunda taxa → nada entregue.

**[E] O sub-padrão mais grave: deepfake do fundador em videochamada ao vivo.** Três casos independentes no Viva Sorte, com a vítima registrando *"posso informar que era ele mesmo"*. Também presente no Pix do Milhão (*"no número do wats é a foto do Pix do milhão, acreditei que era vdd pois fizeram chamada de vídeo"*) e no Familhão.

**[I] A conclusão desconfortável: o ativo de marketing e o passivo de segurança são o mesmo ativo.** A estratégia *founder-as-face* — identificada na pesquisa anterior como o diferencial de aquisição do Viva Sorte — **é o próprio vetor de ataque**. Quanto mais reconhecível o rosto na TV, mais barato fica para o golpista converter. E o vetor é **exatamente o mesmo mecanismo de aquisição** de quem notifica prêmio por canal pessoal: quem treina o mercado a esperar uma ligação de vídeo anunciando prêmio está escrevendo o roteiro que o golpista vai copiar.

**Três consequências de desenho, todas para o dia 1 e não para depois do primeiro incidente:**
- **Canal oficial único e verificável**, publicado em toda peça de mídia.
- **"Nunca cobramos nada após a compra"** dito em toda peça, não só na página de FAQ.
- **A empresa nunca liga primeiro.** O prêmio aparece na conta; o usuário descobre entrando.

→ **Q-C3** ("Quem é o rosto da marca?", P0) — **evidência nova que muda o cálculo**. A pergunta atual pesa formato criativo; falta pesar que rosto único em mídia de massa **compra um passivo antifraude proporcional ao alcance**.
→ **PRD §6.4** (ativos de marca/domínio): o risco registrado é bus factor e ausência de `.com.br`. **[I] Falta o risco de clone**: um domínio `.com.br` da marca não registrado não é só perda de tráfego — é **domínio disponível para site clone**, e o padrão dos concorrentes mostra que o clone chega antes do volume.

#### E3. Nota de Reclame Aqui mede atendimento, não produto — e é comprável

**[E]** Os três players com **maior volume absoluto** de reclamação do painel têm as **três melhores notas**: Familhão ([n] · [n] · RA1000), Pix do Milhão ([n] · [n] · RA1000), Apcap (~[n] · [n]). O player com **menos** reclamações no eixo comparável tem a **pior** nota (Viva Sorte, [n]), porque responde [x%] em [n] dias.

**[E] E os três mecanismos que produzem nota alta sem produto melhor estão documentados:**
- **Apcap:** as notas 9–10 concentram-se em casos cuja "solução" custa quase nada (remover número de lista de disparo, explicar em qual aba está o cupom). Casos caros terminam `ANSWERED`/`solved=false` **sem avaliação** — e não entram no denominador.
- **Pix do Milhão:** template jurídico literalmente copiado que **termina negando o prêmio**, e mesmo assim conta como "respondida".
- **SBT Prêmios:** <1h para falha de entrega (custo marginal zero), [n] dias para prêmio não pago, nunca para questionamento de lisura.

**[I] Consequências diretas:**
1. **Nota de RA não é moat nem sinal de qualidade — é custo operacional.** Se o Seu Milhão for benchmarkeado por nota RA, estará medindo a coisa errada.
2. Se o produto vai gerar reclamação (e vai — todos geram), **a operação de atendimento precisa existir antes do go-live de mídia, não depois**. O Familhão criou ouvidoria formal como *resposta a volume*.
3. **A melhor prática de atendimento observada no painel é a do Familhão** e é replicável: agente nominal identificado por nome e função, número de protocolo, resolução e estorno **antes** da resposta pública, tom de marca preservado, SLA mediano de 2 dias.

→ **PRD §6.6** (desconexão entre pesquisa formal e benchmark real): o benchmark eleito pelo squad (Viva Sorte) é **o player com a pior nota e o pior SLA do painel**. Isso não o desqualifica como referência de aquisição — mas desqualifica qualquer leitura de que "ele funciona, então copiar funciona".

#### E4. O funil é assimétrico: entrar é fácil, receber é difícil — e essa assimetria é lida como fraude

**[C]** Padrão em 3 dos 5 players, mais nítido na Apcap:

> *"**pra comprar não tem nenhuma segurança, porém pra sacar e mil dificuldades**"*

**[E]** Na Apcap, um único fornecedor de KYC/liveness gera simultaneamente as categorias de acesso travado ([x%]), saque bloqueado ([x%]) e biometria falhando ([x%]) — **[x%] da amostra tem esse componente**. E existe o padrão pior: **Pix pago ANTES de existir conta** → cadastro exigido depois → cadastro falha → dinheiro pago, produto inacessível. O mesmo padrão aparece no Viva Sorte (*"não pedia para que eu me cadastrasse […] comprei três cartelas […] fui bloqueada temporariamente"*).

**[E] E há um dado que muda a leitura do custo de suporte:** *"incrivelmente depois de uma reclamação aqui, no reclame aqui, consegui fazer o saque"*. **[I] O Reclame Aqui virou etapa do fluxo de pagamento de prêmio.** Isso explica simultaneamente volume alto e resolução alta — são a mesma coisa. É um custo operacional recorrente escondido dentro de uma métrica que parece boa.

**Três regras de desenho que caem direto:**
- **Nunca cobrar antes de existir conta.** Inverter a ordem elimina uma parcela relevante do passivo observado na Apcap.
- **A escolha de provedor de KYC e o fallback manual são decisão arquitetural, não de sprint.** Definir SLA e caminho alternativo de validação **antes** do lançamento.
- **Prêmio preso na carteira é pior que prêmio pequeno.** A raiva mais intensa das amostras não vem de não ganhar; vem de ganhar e não conseguir sacar. E é o único tipo de reclamação que um regulador ou um adquirente de pagamento lê como risco material.

→ **PRD §6.3** (economia do produto em branco, 🔴 CRÍTICO) e **Q-P3** (estrutura completa da economia de prêmio): **evidência nova** de que o custo do SLA de saque tem três componentes que ninguém orçou — trilho automático, trilho de exceção manual, e o suporte que o trilho quebrado gera.
→ **Q-T4** (gateway de Pix): **evidência nova**. Ver também E7.

#### E5. "Propaganda enganosa" não é queixa de criativo — é o rótulo genérico de falha de entrega

**[E]** É a faceta #1 em **quatro dos cinco players** (Viva Sorte [x%] · Pix do Milhão [x%] · Apcap [x%] · SBT [x%]) e a #4 no Familhão ([x%]). **[E]** Mas a leitura do texto desmonta o rótulo: na Apcap, o rótulo é [x%] e **apenas [x%] do texto fala de odds ou manipulação** — os outros [x%] descrevem falha operacional. E no Viva Sorte, distribuidora e emissora têm **exatamente a mesma proporção ([x%])**, apesar de a emissora nem fazer publicidade ao consumidor.

**[I] Duas consequências, uma tranquilizadora e uma alarmante:**
- **Tranquilizadora:** usar essa faceta como proxy de "criativo agressivo demais" é erro de leitura. O criativo não é o principal gerador.
- **Alarmante:** **num produto de sorteio, toda falha de UX vira acusação de má-fé no registro público** — e vira o rótulo mais tóxico possível para due diligence, para adquirente de pagamento e para regulador. O consumidor não tem, na taxonomia do RA, a categoria "pagou e não entregou". **O custo reputacional de um bug de entrega neste nicho é desproporcional ao bug.**

→ **Q-R7** (limites de claim publicitário sob SUSEP + CONAR, P1) — **esta pesquisa reformula a pergunta**. O risco de claim não está principalmente na headline; está na **distância entre o que a peça mostra e o que o app entrega**. Casos concretos: a roleta do anúncio do Viva Sorte tem **8 prêmios**, a do app tem **5 e um "tente novamente"** (reclamação de 25/08/2025, não resolvida); o Familhão anunciou ao vivo no Domingão um óculos indisponível no dia seguinte, e levou **CDC arts. 30 e 35** citados nominalmente, sem resposta. **Pergunta a adicionar ao backlog: quem valida que o mock do criativo corresponde à UI de produção antes do ar?**

#### E6. O consumidor não usa a SUSEP — usa o CDC, o Procon e o MP

**[E]** Em nenhum dos cinco players a SUSEP aparece como autoridade acionada pelo consumidor. Ela aparece: como **fonte de consulta de prazo** (Viva Sorte, 1×), como **suposto aval do governo** (Pix do Milhão, 1×), como **escudo da empresa contra pedido de exclusão LGPD** (Apcap) e como **escudo da empresa contra a tese de jogo de azar** (SBT). No Familhão: **zero ocorrências**, junto com zero ocorrências de "capitalização".

**[E]** O que o consumidor efetivamente cita: **CDC** (arts. 6, 20, 30, 35, 37, 47), **Procon**, **Ministério Público**, **LGPD**, e — no SBT — **Decreto-Lei 9.215/46 e Lei de Contravenções Penais art. 50**, com a tese de que a mecânica de roleta descaracteriza o título de capitalização.

**[I] Três leituras que mudam decisão:**
1. **O selo SUSEP é defesa eficaz contra o regulador setorial e inútil contra o Procon/CDC** — que é de onde vem o risco jurídico prático hoje.
2. **A regulação não é ativo de conversão porque o consumidor não sabe que a categoria existe.** O consumidor do Familhão compra do apresentador e da Globo, não de uma estrutura jurídica. Isso corrobora e endurece a leitura #1 da pesquisa anterior.
3. **Mas há um efeito colateral perigoso:** quando o consumidor *entende* SUSEP, ele entende errado — como **avalista estatal do pagamento**. *"Essa empresa apoiada pelo site do governo Susep está me [prejudicando]"*. **Comunicar SUSEP sem explicar o que ela não cobre é acumular passivo**, porque a frustração dessa expectativa é o que produz linguagem de denúncia formal.

→ **PRD §6.1** ("Combo" com dúvida SUSEP) e **Q-R2**: **evidência lateral relevante**. A dúvida regulatória sobre combo é real, mas a evidência mostra que **o vetor de risco imediato do nicho não é a SUSEP — é o CDC**. Se houver escassez de atenção jurídica, ela deve ir primeiro para: coerência entre peça e produto, prazo único de pagamento, e regra de raspadinha por escrito.
→ **Q-R7**: adicionar a pergunta *"como comunicar SUSEP sem induzir à leitura de garantia estatal de pagamento?"*

#### E7. Nenhum player publica prova pública auditável de ganhador — e isso é fricção de conversão medida

**[E]** Em todos os cinco perfis o consumidor questiona a lisura, e a resposta da empresa é sempre **narrativa, nunca demonstrável**:

| Player | Verbatim do consumidor |
|---|---|
| Viva Sorte | *"sempre dois ou três de cada estado ganham, isso indica que não é aleatório"* |
| Pix do Milhão | *"nunca mais ninguém vê esses ganhadores postando […] acho que **paga as pessoas para falar que ganhou**"* |
| Apcap | *"Qual lei ou regulamentação permite o sorteio ser realizado através de um Globo Virtual"* |
| Familhão | *"as pessoas sorteadas **são escolhidas a dedo**"* · *"**Ainda não comprei pq não vejo nada sobre quem já ganhou!!!**"* |
| SBT Prêmios | *"**Os ganhadores pode ser IA**"* · *"Só tem 3 vídeos de ganhadores lendo texto similar"* · *"[n] giros seguidos […] Existe auditoria independente?"* |

**[I]** Este é o whitespace de **transparência do mecanismo** já identificado na pesquisa de criativo (share nulo entre os anúncios analisados) — agora **confirmado do lado da demanda, com um caso em que o consumidor declara explicitamente que não comprou por falta de prova pública**. Não é só diferencial de retenção; **é fricção de conversão mensurável**.

**[E] E há um anti-padrão a evitar, documentado no Viva Sorte:** o vídeo do ganhador **foi ao ar antes do prêmio ser pago**, com a empresa justificando: *"nosso material de marketing também são os vídeos de ganhadores […] assegurando a transparência"*. **[I]** Prova social produzida antes do pagamento é eficiente para aquisição e tóxica quando o pagamento atrasa: o consumidor se vê na TV recebendo um prêmio que ainda não recebeu.

→ **Q-C2** ("qual é o formato-assinatura do Seu Milhão? vale atacar o whitespace de transparência?") — **esta pesquisa responde parcialmente: sim, e com evidência de demanda.** O que falta especificar é *o que* seria auditável: número de série emitido no ato da compra, resultado da Loteria Federal linkado, comprovante de pagamento com data, e histórico persistente na conta.
→ **Q-C9** (formato "recap em quadro branco" para explicar mecanismo) ganha um insumo concreto: as cinco perguntas acima são o roteiro.

### 7.2 Padrões ESPECÍFICOS de execução ruim — checklist, não estratégia

| # | Player | Falha | Custo observado | Prevenção |
|---|---|---|---|---|
| **S1** | Viva Sorte | **Quatro prazos de pagamento circulando** (24h marketing · 72h úteis · [n] dias úteis · [n] dias corridos no regulamento e na SUSEP) — e a empresa **admitiu a divergência por escrito em canal público** | Reclamação com o item 10.11 do processo SUSEP citado; é o risco regulatório mais concreto do painel | **Um único prazo, escrito uma vez, replicado em todo canal**, idêntico ao registrado no produto do emissor |
| **S2** | Viva Sorte | **SLA de suporte degradou de <3 dias para ~[n] dias em [n] meses** — aquisição escalou mais rápido que suporte | [n] reclamações aguardando resposta; nota [n] | Dimensionar suporte como função do volume projetado de mídia, não do volume atual |
| **S3** | Viva Sorte | **Golpistas com nome, CPF e e-mail corretos**, e sabendo que a vítima já era cliente. A resposta da empresa **nunca aborda a origem do dado** — só afirma *"Estamos totalmente alinhados à LGPD"* | Exposição LGPD não tratada; ≥4 casos na amostra | Política de retenção + auditoria de cadeia de afiliados/PDV; **investigar, não afirmar conformidade** |
| **S4** | Pix do Milhão | **Template jurídico literalmente copiado** — 3 respostas idênticas parágrafo por parágrafo no mesmo dia (05/02/2026, 17:33/17:38/17:40), terminando em negação de prêmio | Réplica devastadora: *"se vocês verificaram, como não sabem que foram diversas compras?"* | Se a resposta é template, o **diagnóstico do caso** não pode ser |
| **S5** | Pix do Milhão | **Reengenharia jurídica contínua**: Lotep → emissora A → ViaCap; produto de fachada bilhete → e-book → ponto → assinatura; **5 gateways em [n] meses**; 2 CNPJs alternando | Denúncia estruturada pública com 6 perguntas formais | Estabilidade de emissora/gateway é ativo de confiança, não detalhe de backoffice |
| **S6** | Apcap | **Fornecedor único de KYC/liveness sem fallback** — erros 0010/0011 nomeados pelos próprios consumidores | [x%] da amostra; bypass manual virou processo permanente (*"apresentamos uma alternativa"*) | Fallback de validação desenhado, com SLA, **antes** do go-live |
| **S7** | Apcap | **SUSEP (Circular 605) invocada para negar exclusão de dados sob LGPD** | **NOT_SOLVED, nota 1** — o pior desfecho reputacional de toda a amostra | Separar o que a norma obriga a guardar (registro da operação) do que pode ser excluído (base de marketing) — e comunicar assim |
| **S8** | Apcap | **Outbound massivo por WhatsApp de números rotativos** (antes, robocall: *"mais de [n] ligações em meia hora num sábado à noite"*) | Gera reclamação de perturbação, pedido de exclusão LGPD **e destrói a capacidade de distinguir a marca do golpista** | Canal único e verificável desde o dia 1 — é defesa antifraude de marca, não higiene de CRM |
| **S9** | Apcap | **Compensação de falha oferecida em cupons de sorteio, não em dinheiro** — e os cupons também não premiaram | Consumidor voltou a reclamar | Compensar falha de sorteio com mais sorteio realimenta o ciclo |
| **S10** | Familhão | **Fluxo de cancelamento quebrado por [n] meses** — reclamações de 09/2024 e 02/2026 com texto quase idêntico | Tag #1 do perfil (Cobrança indevida, [n]) | Cancelamento self-service testado como fluxo crítico, com regressão |
| **S11** | Familhão | **CRM de reativação disparando contra pagante ativo** (*"paguei ontem, hoje recebi mensagem dizendo que eu não vou participar"*) | [x%] da amostra; converte cliente adimplente em reclamante público | Régua de cobrança lê estado de pagamento antes de disparar — **a correção mais barata de toda a pesquisa** |
| **S12** | Familhão | **Deflexão para o banco** em cobrança recorrente (*"basta cancelar a autorização no aplicativo do seu banco"*) | Única parte do playbook que produz réplica em vez de resolução; num caso **nem o funcionário da agência localizou a opção** | Se o mecanismo é Pix Automático, a empresa precisa de trilho próprio de cancelamento |
| **S13** | Familhão | **Migração para marketplace importando passivo de e-commerce** — frete, prazo, rastreio, SKU esgotado aparecem só em ago/2026 | Tipos ausentes de todo o histórico anterior | Camada de benefício que sustenta recorrência é operação logística — decidir se isso entra no escopo |
| **S14** | SBT Prêmios | **Conciliação Pix→título falha sob pico de tráfego televisivo** — QR code ao vivo no Domingo Legal | [x%] da amostra recente | **Conciliação em janela de segundos é requisito de infraestrutura de nível arquitetural** para quem usa tráfego concentrado |
| **S15** | SBT Prêmios | **Workaround "logout/login" canonizado como resposta padrão há 3+ meses** | Bug conhecido, não corrigido; cada ocorrência = 1 ticket + 1 reclamação pública | Workaround repetido em ≥3 respostas é sinal de bug com dono, não de FAQ |
| **S16** | SBT Prêmios | **Troca de emissora SUSEP em menos de 6 meses** (Icatu → Liderança), com reembolso sendo empurrado de uma empresa para a outra | Consumidor refaz a reclamação em outro perfil; atrito real amplificado | A escolha de emissora é reversível, mas **o custo aparece na experiência do cliente** |
| **S17** | SBT Prêmios | **Curva de desaceleração da animação da roleta para uma casa antes do prêmio** | Lido como prova de fraude, com pedido de auditoria independente | Em prêmio instantâneo, **a curva de animação é decisão de compliance, não de motion design** |

### 7.3 Perguntas do backlog §7 que esta pesquisa move

| ID | Status | O que esta pesquisa acrescenta |
|---|---|---|
| **Q-R3** (raspadinha é modalidade admitida sob SUSEP?) | **Evidência nova forte** | Não responde a pergunta jurídica, mas mostra que é o **maior gerador de atrito do setor** (E1) e que os players resolvem com a defesa *"animação meramente ilustrativa"*, que é juridicamente eficaz e reputacionalmente cara. Sugere elevar §6.10 de 🟡 para 🔴 |
| **Q-P5** (regra de negócio da raspadinha) | **Evidência nova forte** | Três especificações que faltam ao PRD e que os concorrentes erram: (a) prêmio em dinheiro ou crédito, declarado **antes** da animação; (b) comprovante persistente da cartela perdedora; (c) regra de "3 iguais" escrita de forma não ambígua — no Viva Sorte gerou citação do **CDC art. 47** |
| **Q-R7** (limites de claim publicitário) | **Pergunta reformulada** | O risco não está na headline; está na **distância entre a peça e a UI de produção** (roleta de 8 prêmios no anúncio × 5 no app; oferta anunciada ao vivo e indisponível no dia seguinte → CDC arts. 30/35). Adicionar: *quem valida a paridade peça↔produto antes do ar?* e *como comunicar SUSEP sem induzir à leitura de garantia estatal?* |
| **Q-R4 / Q-R5 / Q-R6** (LGPD) | **Evidência nova** | Dois desfechos concretos observados: golpistas com CPF/nome/e-mail corretos sem investigação de origem (Viva Sorte, S3) e **SUSEP invocada para negar exclusão de dados → NOT_SOLVED, nota 1** (Apcap, S7). A política de retenção precisa separar registro da operação de base de marketing |
| **Q-P4** (quem é o emissor SUSEP?) | **Evidência nova** | (a) A escolha é **reversível** — SBT trocou Icatu→Liderança em <6 meses; (b) mas o custo aparece no cliente (reembolso empurrado entre empresas); (c) **a emissora regulada atende muito melhor que a distribuidora** — VIA Cap responde [x%] em [n] contra [x%] em [n] do Viva Sorte. Se a operação for split, o SLA da distribuidora precisa ser tratado como requisito, mesmo não sendo |
| **Q-P3** (economia de prêmio) | **Evidência nova** | Três custos não orçados: trilho automático de saque, **trilho de exceção manual** (que na Apcap virou processo permanente) e o suporte gerado pelo trilho quebrado |
| **Q-P7** (app ou web) e **Q-P8** (checkout em subdomínio de terceiro) | **Evidência nova** | Duas reclamações contra o Viva Sorte em ago/2026 citam **Liderança Capitalização** no comprovante do Pix — **o nome no extrato não é o nome da marca**, e isso sozinho gera estorno, chargeback e reclamação registrada contra a marca errada. Aplica-se diretamente ao checkout em subdomínio de fornecedor terceiro previsto para o Seu Milhão |
| **Q-T4** (gateway de Pix) | **Evidência nova** | O caso SBT mostra que o requisito não é só taxa e liquidação: é **conciliação Pix→título em janela de segundos sob pico de tráfego concentrado**. Requisito arquitetural, não de sprint |
| **Q-C1** (análise formal do Viva Sorte) | **Evidência nova substancial** | O benchmark do squad tem **[n] reclamações ativas, nota [n], [x%] de resposta em [n] dias e [n] pendências** — a pior operação de atendimento do painel. Funciona em aquisição; não funciona em pós-venda |
| **Q-C2** (formato-assinatura / whitespace de transparência) | **Respondida parcialmente** | Sim, o whitespace é real **e tem demanda documentada**: consumidor do Familhão declara que não comprou por falta de prova pública de ganhador (E7). Anti-padrão a evitar: vídeo de ganhador ao ar **antes** do pagamento |
| **Q-C3** (quem é o rosto da marca) | **Evidência nova que muda o cálculo** | Rosto único em mídia de massa compra um passivo antifraude proporcional ao alcance — **deepfake em videochamada ao vivo**, ainda ativo em ago/2026 (E2) |
| **Q-R2** (combo) | **Evidência lateral** | Não resolve a dúvida regulatória, mas mostra que o vetor de risco imediato do nicho é o **CDC**, não a SUSEP (E6) |

### 7.4 Duas leituras finais que não cabem em nenhuma categoria

**[I] Primeira: "enganação" e "golpe" são problemas de custos diferentes.** O Familhão gera [n] reclamações e **zero** ocorrências de "fraude", "pirâmide" ou "advogado" — a palavra que aparece é "enganação" ([n]×), que é sentimento de **promessa não cumprida**. Viva Sorte, Pix do Milhão e SBT geram reclamação de **prêmio não pago**, que é acusação de crime (e que o RA censura). **"Enganação" é curável por UX e SLA. "Golpe" é curável só por prova pública.** A escolha de mecânica de produto determina em qual dos dois lados a marca vai viver — e o lado barato é o de quem entrega um benefício tangível e trata o sorteio como camada, não como promessa central.

**[I] Segunda: emprestar credibilidade de terceiro é alavancagem de risco, não hedge.** O SBT emprestou [n] anos de credibilidade de TV aberta para vender um título de R$ [valor], e a categoria de reclamação "Emissoras de rádio-TV" ([n] ocorrências, 2ª maior) é a métrica do dano. O consumidor declara que comprou pelo selo; quando o produto falha, ele não conclui "o site falhou" — conclui "**o SBT me enganou**". Para um projeto que herdou rede de influenciadores e discute quem é o rosto da marca, isso inverte a intuição: **a marca emprestada não amortece a falha operacional, amplifica.**

---

## 8. Lacunas e limitações declaradas

### 8.1 Limitações de amostragem (todas declaradas pelos agentes)

| Limitação | Detalhe |
|---|---|
| **Nenhuma amostra é aleatória** | A paginação das listas é client-side e não renderizou de forma confiável pelo proxy em nenhum dos 5 levantamentos. Amostras montadas por busca temática indexada, widget "Reclamações Parecidas" e reclamações recentes do perfil — **enviesa para títulos dramáticos, casos extremos e itens bem indexados** |
| **Cobertura muito desigual** | Apcap [x%] da listagem ([n]/[n]) vs. Familhão [x%] do acumulado ([n]/[n]). **Os percentuais de amostra dos cinco players não são comparáveis entre si** |
| **Facetas oficiais também são parciais** | O RA expõe só os 6 maiores problemas/categorias. No Familhão os 6 somam [n] dos [n] (**cauda longa de [x%] não observável**); no SBT apenas [n] de [n] ([x%]) têm tag; no Pix do Milhão as facetas somam ~[n] de [n] |
| **Censura da plataforma** | "golpe", "fraude", "estelionato" são substituídos por `[Editado pelo Reclame Aqui]`. **Impossível contar menções literais** — qualquer análise de "menções a fraude" subconta por design. Valores e telefones aparecem como `*****`, impedindo quantificar prêmios disputados |
| **Resolução não é auditável** | Em Apcap, Viva Sorte e SBT, as tratativas são **narradas** como ocorridas via WhatsApp, fora do RA. "[x%] resolvidas" não é verificável por terceiro |
| **Reclamações são desativadas ao longo do tempo** | Confirmado em Viva Sorte e Pix do Milhão: páginas indexadas no Google retornam *"Essa reclamação foi desativada"*. Os totais são de **reclamações ativas**, não de reclamações já registradas. Causa não determinável (moderação, acordo ou pedido da empresa) |
| **Série histórica de reputação limitada a 6 meses** | O RA só publica a janela móvel. Nenhum dos 5 levantamentos conseguiu reconstruir curva longa; snapshots de cache de buscadores são ruidosos e não datados |
| **Perfis irmãos parcialmente cobertos** | `apcap-sp` ([n] reclamações) teve só os índices lidos, não o conteúdo — a taxonomia da Apcap cobre [x%] do passivo do grupo. As ~[n] reclamações sobre SBT Prêmios no perfil da Icatu não foram lidas individualmente, o que **subamostra a fase Icatu (dez/25–abr/26)** |

### 8.2 O que não foi possível confirmar

| Questão em aberto | Player | Por quê importa |
|---|---|---|
| As ~[n] reclamações do Viva Sorte classificadas em "Leilão" e "Recuperadora de crédito" são de fato golpes de terceiro? | Viva Sorte | Se sim, o peso real do vetor de fraude é muito maior que os [x%] da amostra. **Hipótese forte, não confirmada** |
| O Viva Sorte passou a distribuir títulos da **Liderança Capitalização** além da VIA Cap, ou é confusão do consumidor no momento do pagamento? | Viva Sorte | Muda o mapa de fornecedores **ou** confirma que o nome no extrato do Pix diverge da marca — as duas hipóteses são relevantes e nenhuma foi confirmada |
| A "Roleta da Sorte" é produto ativo em 2026? | Viva Sorte | A empresa nega em ago/2026 (*"não possuímos a modalidade de roleta mencionada"*), mas reclamações de 2025 a descrevem **dentro do app oficial**, anunciada em TV com o fundador e um jogador de futebol famoso. Não resolvido |
| A frente de ago/2026 ("roleta Pix", "plataforma de jogos", saque) é migração do produto para mecânica de aposta, ou migração do ecossistema de golpes? | Viva Sorte | Duas leituras não distinguíveis com os dados disponíveis |
| O regulamento e as Condições Gerais preveem de fato a defesa da "animação ilustrativa"? | Pix do Milhão | Não foi possível ler o regulamento; a defesa cita "item 3.9 e seguintes" |
| Números de processo SUSEP citados nas respostas | Pix do Milhão | Todos mascarados pelo próprio RA (`Portaria SUSEP nº 3.*******`) — impossível cruzar com o cadastro da SUSEP a partir desta fonte |
| Queda de volume da Apcap nos últimos [n] dias (campo `totalComplains30` muito abaixo da média mensal) | Apcap | Sem série mensal para distinguir sazonalidade de agosto, mudança de mix de mídia ou migração para o perfil irmão. **Não usar como evidência de melhoria** |
| Outras marcas do mesmo operador (HiperCap Brasil, Saúde Cap, mesmo CNPJ/família Idea Maker) | Apcap | O passivo consolidado do grupo pode ser **maior que [n]** |
| Existe perfil RA secundário da razão social Familhão Engajamento e Intermediação S.A.? | Familhão | Busca por CNPJ não retornou perfil adicional; a submarca "Achou Levou do Familhão" existe como *marca* dentro do perfil, sem estatísticas próprias |
| Prêmio âncora do SBT Prêmios | SBT Prêmios | **Gap herdado da pesquisa anterior, não fechado.** `sbtpremios.com` retorna 403 direto |
| Causa isolada da recuperação Mar→Jul/2026 do SBT | SBT Prêmios | Três variáveis mudaram juntas (emissora, canal de atendimento, tom). Hipótese de maior verossimilhança: canal telefone→WhatsApp. **Não resolvível com dados públicos** |
| Autuação de SUSEP, SPA, Procon ou MP contra qualquer player | Todos | **Nenhuma localizada em nenhum dos 5 levantamentos.** Ausência de notícia ≠ ausência de processo. Fechar exige consulta direta ao sistema de processos SUSEP, ao DOU e ao Procon-SP |

### 8.3 Fontes de contraponto não cobertas

**Consumidor.gov.br** e **Procon-SP** — bases públicas que dariam contraponto ao RA e cobririam justamente os consumidores que **efetivamente escalaram** (e não só ameaçaram). Fora do escopo desta camada, e é a lacuna de maior valor a fechar em seguida: os cinco levantamentos convergem em que a ameaça de Procon é frequente, mas **nenhum conseguiu verificar se ela se materializa**.

---

## 9. Fontes

### Páginas de perfil e listagem (índices oficiais, todas verificadas em 14/08/2026)

**Viva Sorte / VIA Cap:** [perfil Viva Sorte](https://www.reclameaqui.com.br/empresa/viva-sorte/) · [lista Viva Sorte](https://www.reclameaqui.com.br/empresa/viva-sorte/lista-reclamacoes/) · [perfil VIA Cap](https://www.reclameaqui.com.br/empresa/via-cap/) · [lista VIA Cap](https://www.reclameaqui.com.br/empresa/via-cap/lista-reclamacoes/)

**Pix do Milhão:** [perfil (slug criative)](https://www.reclameaqui.com.br/empresa/criative-publicidade-promocoes-e-shows/) · [perfil (slug ltda11)](https://www.reclameaqui.com.br/empresa/pix-do-milhao-ltda11/) · [lista + facetas](https://www.reclameaqui.com.br/empresa/pix-do-milhao-ltda11/lista-reclamacoes/) · [FAQ "Alerta de Golpes"](https://www.reclameaqui.com.br/empresa/criative-publicidade-promocoes-e-shows/faq/alerta-de-golpes_lr-rRVUkkt6vjb7M/) · [post institucional "Ações novas liberadas"](https://www.reclameaqui.com.br/empresa/pix-do-milhao-ltda11/conteudos/acoes-novas-liberadas-diversos-premios_I_sTymdVlxPFr9z6/) · [ranking Clubes de Benefícios](https://www.reclameaqui.com.br/segmentos/fidelidade-pontos/clubes-de-beneficios-e-descontos)

**Apcap:** [perfil APCAP da Sorte](https://www.reclameaqui.com.br/empresa/apcap-da-sorte/) · [lista APCAP da Sorte](https://www.reclameaqui.com.br/empresa/apcap-da-sorte/lista-reclamacoes/) · [lista APCAP (`apcap-sp` / Idea Maker)](https://www.reclameaqui.com.br/empresa/apcap-sp/lista-reclamacoes/) · [conteúdo institucional sobre premiações](https://www.reclameaqui.com.br/empresa/apcap-sp/conteudos/saiba-tudo-sobre-as-nossas-premiacoes_8aV0YTD6lTpX3TJX/)

**Familhão:** [perfil](https://www.reclameaqui.com.br/empresa/familhao-programa/) · [lista](https://www.reclameaqui.com.br/empresa/familhao-programa/lista-reclamacoes/) · [post institucional — Ouvidoria (13/02/2026)](https://www.reclameaqui.com.br/empresa/familhao-programa/conteudos/quando-procurar-a-ouvidoria-do-familhao_9NKzZCBkaZaKz-ex/) · [marca "Achou Levou do Familhão"](https://www.reclameaqui.com.br/empresa/familhao-programa/marcas/achou-levou-do-familhao/)

**SBT Prêmios:** [perfil](https://www.reclameaqui.com.br/empresa/sbt-premios/) · [lista + facetas](https://www.reclameaqui.com.br/empresa/sbt-premios/lista-reclamacoes/) · [perfil Icatu Seguros](https://www.reclameaqui.com.br/empresa/icatu-seguros-1) · [busca "sbt" no perfil da Icatu](https://www.reclameaqui.com.br/empresa/icatu-seguros-1/lista-reclamacoes/?busca=sbt)

### Reclamações individuais citadas neste documento

Na versão pública, os links para reclamações individuais foram omitidos: são páginas escritas por consumidores e podem conter dados pessoais. Cada reclamação citada no corpo do documento está identificada pela data e pelo status, o que basta para entender o método e os padrões encontrados.

### Fontes fora do Reclame Aqui

FDR — matéria de 25/05/2026 sobre o volume de reclamações do Familhão (link omitido) · consulta pública de CNPJ da emissora dona do perfil do SBT Prêmios (links omitidos) · [SBT Prêmios — termos de uso](https://sbtpremios.com/termos-de-uso) · [SBT Prêmios — condições gerais](https://demo.sbtpremios.com/condicoes-gerais)

### Pesquisas relacionadas neste repositório

- `research/2026-08-14-capitalizacao-players-modelo-negocio/README.md` — modelo de negócio, arquitetura regulatória, preço e escala dos mesmos 5 players. **Este documento corrige a linha "Reclame Aqui" da tabela comparativa §6 daquele relatório** (ver §0.2)
- `research/2026-08-14-susep-capitalizacao-regulatorio/README.md` — base normativa
- `research/2026-08-11-meta-ad-library-sorteio-br/README.md` — formato de anúncio e whitespace de transparência (confirmado do lado da demanda em §7.1 E7)
- `research/2026-08-14-cadencia-angulo-canais-promocoes/README.md` — cadência e ângulo
