# Modelo de negócio dos players de sorteio/capitalização — BR, ago/2026

> Versão pública sanitizada: números de negócio, nomes de pessoas, citações de fontes privadas e parceiros foram substituídos por marcadores ([valor], [n], [x%], papéis).

**Legenda de evidência:** **[E]** documentado (fonte primária lida, URL citada) · **[C]** consenso entre múltiplas fontes secundárias, sem documento primário · **[I]** inferência do analista, não observada diretamente.

**Escopo:** modelo de negócio, arquitetura regulatória, preço, estrutura de prêmio, escala e canais dos 5 players. **Não** cobre formato de anúncio — isso está em `research/2026-08-11-meta-ad-library-sorteio-br/README.md`, que este documento complementa e não repete.

**Data da pesquisa:** 14/08/2026. Preços e prêmios do setor mudam por edição semanal — tratar valores como snapshot, não como constante.

---

## 0. O achado que reorganiza a leitura: existem TRÊS arquiteturas regulatórias, não uma

Antes de olhar player por player: o PRD do Seu Milhão trata "capitalização SUSEP" como se fosse uma categoria única que separa os regulados dos informais. **A pesquisa mostra que isso é falso.** Nenhum dos cinco players é rifa informal — mas eles se dividem em três desenhos jurídicos materialmente diferentes, com consequências diretas de copy, de fornecedor e de risco.

| Arquitetura | O que o consumidor compra | Quem regula | Players |
|---|---|---|---|
| **A — Filantropia Premiável** | **O próprio título de capitalização**. Cede [x%] do direito de resgate a uma entidade beneficente certificada | **SUSEP** (só) | Viva Sorte (produto clássico), SBT Prêmios |
| **B — Promoção comercial lastreada em título de Incentivo** | **Um produto** (e-book, assinatura de clube). O sorteio é distribuição gratuita de prêmio; o título é comprado *pela empresa*, não pelo cliente | **SPA/MF + SUSEP** (dupla) | Apcap da Sorte, Pix do Milhão |
| **C — Promoção comercial pura, sem capitalização** | **Uma assinatura de clube de benefícios**. Sorteio autorizado como distribuição gratuita de prêmios (Lei 5.768/1971) | **SPA/MF** (só) — sem SUSEP | Familhão |

**[E]** A base legal da arquitetura C é a Lei 5.768/1971: "promoções comerciais como sorteios, concursos, vale-brindes ou operações assemelhadas dependem de autorização prévia da Secretaria de Prêmios e Apostas do Ministério da Fazenda" ([gov.br/fazenda — SPA](https://www.gov.br/fazenda/pt-br/composicao/orgaos/secretaria-de-premios-e-apostas), [gov.br — obter autorização](https://www.gov.br/pt-br/servicos/obter-autorizacao-para-atividades-de-distribuicao-gratuita-de-premios-a-titulo-de-propaganda-ou-de-captacao-de-poupanca-popular)).

**[E]** A base normativa da arquitetura A é a Resolução CNSP 384/20 + Circular SUSEP 656/22 ([Circular SUSEP 656/2022](https://www.legisweb.com.br/legislacao/?id=428900)).

**[I] Por que isso importa para o Seu Milhão:** o PRD assume arquitetura A ("título de capitalização regulado pela SUSEP, prêmio vinculado a transação via Pix"). Mas **o benchmark eleito pelo squad (Viva Sorte) opera A e B simultaneamente**, e os dois players de maior tração digital do setor (Apcap e Pix do Milhão) operam **B**, não A. Escolher A por default, sem ter avaliado B, é uma decisão de arquitetura tomada por omissão.

---

## 1. Viva Sorte — o benchmark do squad

> Este é o player que um parceiro do projeto elegeu como referência [em mensagem interna, apontou o Viva Sorte como o melhor que tinha visto] e que **não aparecia** na pesquisa formal anterior. É o mais bem documentado deste relatório e o único com dois produtos, três negócios e uma marca-guarda-chuva.

### 1.1 Quem é, de verdade

**[E]** Não é uma empresa — é um **grupo com três camadas societárias distintas**:

| Papel | Entidade | CNPJ | Fonte |
|---|---|---|---|
| **Emissora do título** | VIA CAPITALIZAÇÃO S.A. (ViaCap) — Porto Alegre/RS | [CNPJ omitido] | [regulamento oficial via busca](https://regulamento.vivasorteoficial.com.br/) · [Portal de Pinhal](https://portaldepinhal.com.br/2025/09/como-funciona-o-viva-sorte-e-confiavel-analise-sincera/) |
| **Distribuidora / comercializadora** | Viva Sorte Distribuidora e Intermediadora de Negócios Ltda — Londrina/PR | [CNPJ omitido] | Econodata (link omitido: contém CNPJ) · [Reclame Aqui](https://www.reclameaqui.com.br/empresa/viva-sorte/) |
| **Casa de apostas do grupo** | Viva Sorte Bet, operada por **Jogo Principal Ltda** | — | [Correio Braziliense](https://www.correiobraziliense.com.br/apostas/viva-sorte) · [OddsScanner](https://oddsscanner.com/br/apostas/viva-sorte-bet) |

**[E]** Processo SUSEP do título: **15414.633461/2022-92**, produto "VIVA SORTE V.02", pagamento único, **modalidade Filantropia Premiável** ([regulamento oficial](https://regulamento.vivasorteoficial.com.br/)).

**[E]** Autorização da bet: **SPA/MF nº 2.104-39**, Portaria SPA/MF nº 2.104 de 30/12/2024 ([Correio Braziliense](https://www.correiobraziliense.com.br/apostas/viva-sorte)).

**[E]** Fundador e rosto: **o fundador do grupo**, apresentador e empresário, CEO, com [n] seguidores no Instagram, aparece pessoalmente nos anúncios de patrocínio — comportamento que a imprensa esportiva registra como **incomum entre executivos de bet** ([Máquina do Esporte](https://maquinadoesporte.com.br/apostas/quem-e-viva-sorte-grupo-que-mais-avanca-no-mercado-de-patrocinio-do-futebol-brasileiro/)).

**[I]** Esse é quase certamente **"o dono" não nomeado** cuja publicação o parceiro do projeto compartilhou no grupo interno [comentou que a publicação estava tendo grande alcance], citado no PRD §5.4 com assinatura *founder-as-face*. A hipótese fecha: o benchmark eleito e o "dono" cuja publicação bombou são a mesma operação.

### 1.2 Fundação e tempo de mercado

**[E]** Produto **criado em 2022**; primeira exibição na TV Band em **outubro de 2022** (BNLData (link omitido: URL contém valor), [Portal de Pinhal](https://portaldepinhal.com.br/2023/09/%F0%9F%A4%91-viva-sorte-veja-como-comprar-e-participar-do-sorteio-deste-domingo/)).

**[E]** Mas o grupo por trás vem de Londrina/PR com **mais de 15 anos no setor de capitalização**; a operação de título nasceu "há aproximadamente 16 anos" para arrecadar fundos para um hospital de câncer ([Máquina do Esporte](https://maquinadoesporte.com.br/apostas/quem-e-viva-sorte-grupo-que-mais-avanca-no-mercado-de-patrocinio-do-futebol-brasileiro/)).

**[I]** Leitura: **Viva Sorte não é uma startup de 4 anos — é uma operação filantrópica regional de 16 anos que rebrandou para digital e TV em 2022.** A "credibilidade" que o parceiro do projeto percebeu esteticamente tem lastro operacional de década e meia. Isso não é copiável em 6 meses.

### 1.3 Preço e produto

**[E/C]** **R$ [valor] a R$ [valor] por título**, e o valor **varia a cada semana conforme os prêmios da edição** — não é preço fixo ([Portal de Pinhal — análise](https://portaldepinhal.com.br/2025/09/como-funciona-o-viva-sorte-e-confiavel-analise-sincera/); [Portal de Pinhal — carros 0km por R$ [valor]](https://portaldepinhal.com.br/2025/01/viva-sorte-oficial-concorra-a-10-carros-0km-neste-domingo-por-apenas/)).

**[I] Este é o achado de preço mais acionável do relatório.** Viva Sorte trata o ticket como **variável de campanha**, não como âncora de marca. Todos os outros players têm preço fixo publicado. Precificar por edição permite escalar prêmio e ticket juntos sem quebrar a promessa da marca — e é exatamente o oposto do que o Seu Milhão está desenhando ao tratar o preço como constante de copy.

**[E]** **Dois produtos sob a mesma marca:**
- **Viva Sorte (clássico)** — Filantropia Premiável, direito de resgate cedido à **APAE Brasil** e/ou **Hospital do Câncer de Londrina** conforme a edição ([vivasorteoficial](https://vivasorteoficial.com.br/), [regulamento](https://regulamento.vivasorteoficial.com.br/)).
- **Viva Sorte+** — lançado ~set/2025, posicionado como **"o maior clube de pontos e vantagens do Brasil"**; acumula pontos, troca por vantagens e concorre ao Pix de R$ [valor], com **premiações especiais por estado** ("nossos Top estados") ([anúncio oficial no X](https://x.com/viva_sorte/status/1967226835353403680), [site](https://vivasorteoficial.com.br/)). **[E]** A imprensa setorial descreve o produto atual como **título de modalidade Incentivo funcionando como clube de pontos com sorteios** (BNLData (link omitido: URL contém valor)).

**[I]** Ou seja: **Viva Sorte roda arquitetura A e arquitetura B ao mesmo tempo**, com marcas quase idênticas. É hedge regulatório e de posicionamento — e contradiz frontalmente o princípio de "escolher uma via e não hedgear" que a pesquisa de criativo (F4) recomendou para formato de anúncio. **Hedge de formato é ruim; hedge de arquitetura de produto é o que o líder faz.**

### 1.4 Estrutura de prêmio

| Camada | Valor | Cadência | Tag |
|---|---|---|---|
| Prêmio âncora | **R$ [valor]** via Pix | Semanal, sorteio de domingo | [E] |
| Prêmios materiais | Casas, veículos, **[n] carros 0km em edição especial** | Por edição | [E] |
| Prêmios regionais | Premiações por estado ("Top estados") no Viva Sorte+ | Por edição | [E] |
| **Instantâneo** | **"Giropix"** — premiação instantânea | Contínuo | [C] |
| Raspadinha | Existe (confirmada indiretamente via reclamação de não-pagamento) | Contínuo | [E] |

**[E]** Sorteios **aos domingos, 10h30, ao vivo na TV Band** ([Portal de Pinhal](https://portaldepinhal.com.br/2023/09/%F0%9F%A4%91-viva-sorte-veja-como-comprar-e-participar-do-sorteio-deste-domingo/), [Claro grade de programação](https://www.claro.com.br/tv-por-assinatura/programacao/grade/programa/band/1-2247/viva-sorte/1-1016807)).

**[E]** Apuração baseada nos resultados da **Loteria Federal**; entrega do prêmio anunciada em **até 24h via Pix** ([vivasorteoficial](https://vivasorteoficial.com.br/), [Portal de Pinhal](https://portaldepinhal.com.br/2025/09/como-funciona-o-viva-sorte-e-confiavel-analise-sincera/)). **[I]** Isso é marketing sobre a norma: a Circular SUSEP 656/22 exige pagamento em **até 15 dias corridos** após documentação completa — os 24h são promessa comercial voluntária, e é exatamente o mesmo SLA que um membro da equipe registrou no schema do Seu Milhão (§5.3) [SLA dentro do prazo regulatório, idealmente em 1–2 dias]. **O mercado já converteu a folga regulatória em diferencial de marca.**

### 1.5 Escala e tração

| Métrica | Valor | Fonte |
|---|---|---|
| Meta de faturamento | **R$ [valor] em 2025** | [E] BNLData (link omitido: URL contém valor) |
| Pontos de venda físicos | **[n]**, meta de mais que dobrar em 2026 | [E] mesma fonte |
| Clubes de futebol patrocinados | **[n]** — Athletico-PR, Bahia, Vitória, Goiás, Vasco, Corinthians, São Paulo, Ceará, Fortaleza, Novorizontino, Santos. Meta: [n] | [E] [Máquina do Esporte](https://maquinadoesporte.com.br/apostas/quem-e-viva-sorte-grupo-que-mais-avanca-no-mercado-de-patrocinio-do-futebol-brasileiro/) |
| Reclamações Reclame Aqui | **[n]**, nota **[n]/10** (6 meses), [x%] de resposta, nota média do consumidor [n] | [E] [Reclame Aqui](https://www.reclameaqui.com.br/empresa/viva-sorte/) |

**[E]** O grupo **não divulga valores de contrato de patrocínio**. O fundador: *"adotamos essa decisão de não informar valores, para evitar criar um leilão no mercado."* Referência de ordem de grandeza: o Bahia recebia R$ [valor] da Esportes da Sorte antes ([Máquina do Esporte](https://maquinadoesporte.com.br/apostas/quem-e-viva-sorte-grupo-que-mais-avanca-no-mercado-de-patrocinio-do-futebol-brasileiro/)).

**[I]** A meta de faturamento dividida pelo ticket implica ordem de **[n] títulos/ano** se fosse só o produto avulso — o que é implausível. A conta só fecha com PDV físico + recorrência do clube + a bet no mesmo guarda-chuva. **Não é um negócio de ticket baixo digital; é um conglomerado com o ticket baixo como porta de entrada.**

### 1.6 Canais de aquisição — o que o squad ainda não mapeou

| Canal | Detalhe | Tag |
|---|---|---|
| **TV aberta** | Programa próprio semanal na Band, domingos 10h30, apresentado pelo próprio dono | [E] |
| **PDV físico** | [n] bancas, supermercados, padarias — canal que **nenhum concorrente digital tem** | [E] |
| **Patrocínio esportivo** | [n] clubes da Série A/B — mídia de massa contínua, não campanha | [E] |
| **Celebridades/influenciadores** | Jogadores de futebol, um influenciador digital e um colunista de celebridades | [E] BNLData (link omitido: URL contém valor) |
| **Founder-as-face** | Fundador com [n] seguidores, presença pessoal em anúncios | [E] |
| **App próprio** | Android (`com.edjdigital.vivasorte`) e web app | [E] [Google Play](https://play.google.com/store/apps/details?id=com.edjdigital.vivasorte) |
| **Afiliados** | Portais regionais publicam conteúdo "como comprar" com **link de afiliado** | [E] — observado em [Portal de Pinhal](https://portaldepinhal.com.br/2025/09/viva-sorte-oficial-comprar-online-veja-como-adquirir-pelo-site-e-participar-dos-sorteios/) |

**[I] O ponto cego mais caro:** o Viva Sorte não ganhou por criativo de Meta Ads. Ganhou por **TV + PDV + futebol + rosto do dono**. A pesquisa de Meta Ad Library (F4) **não capturou o Viva Sorte** — e agora sabemos por quê: o motor dele não está lá. Se o squad copiar o Viva Sorte via anúncio de performance, estará copiando o único canal em que ele não é referência.

### 1.7 Controvérsias

- **[E]** Reclamação formal de **não-pagamento de prêmio de raspadinha**: usuário relata ter recebido valor menor que o prêmio ganho ([Reclame Aqui](https://www.reclameaqui.com.br/viva-sorte/viva-sorte-nao-paga-premio-da-raspadinha_3cAtAnGMbhKig14H/)).
- **[E]** Reclamações recorrentes de **não recebimento de resgate e prêmio instantâneo** também contra o CNPJ da emissora (VIA Cap) ([Reclame Aqui — VIA Cap](https://www.reclameaqui.com.br/empresa/via-cap/lista-reclamacoes/), [prêmio instantâneo não recebido](https://www.reclameaqui.com.br/via-cap/premio-instantaneo-nao-recebido_QSjFC8tCsU-pLJoJ/)).
- **[E]** **Ecossistema de clones e golpes** usando a marca: sites como `vivaresgatedepremio.shop` e alerta oficial da própria marca ("GOLPE USANDO O NOME DO VIVA SORTE") ([Instagram oficial](https://www.instagram.com/reel/DMGjN0-sGkG/)). A empresa se posiciona publicamente afirmando que ações fraudulentas com o nome não são oficiais ([Reclame Aqui](https://www.reclameaqui.com.br/empresa/viva-sorte/)).
- **[I]** **Não encontrei autuação regulatória da SUSEP ou da SPA contra o Viva Sorte.** Isso é relevante como sinal positivo — mas ausência de notícia não é ausência de processo; verificação definitiva exige consulta ao sistema de processos da SUSEP, fora do escopo desta pesquisa.

> **Nota de higiene:** existe uma notícia antiga do Jusbrasil ("MPF/PI pede o fechamento do seguro Viva Sorte") que aparece nas buscas. **[I]** Pela data e pelo objeto (um "seguro"), avalio como provavelmente **não relacionada** a este Viva Sorte. Não usar essa fonte sem verificação — foi descartada deste relatório.

---

## 2. Pix do Milhão (influenciador A)

### 2.1 Arquitetura regulatória — o player que já trocou de regime uma vez

**[E]** Enquadramento atual: **Clube de Benefícios** que opera em parceria com **Título de Capitalização da Modalidade Incentivo, emitido pela ViaCap**, sociedade autorizada pela SUSEP ([TechTudo](https://www.techtudo.com.br/guia/2025/04/pix-do-milhao-e-confiavel-saiba-como-funciona-site-que-realiza-sorteios-online-edsoftwares.ghtml), [UAI](https://www.uai.com.br/networking-e-negocios/2026/06/26/o-que-e-o-pix-do-milhao-entenda-o-clube-de-beneficios-como-funciona-premios-valor-e-como-participar/)).

**[E] Histórico regulatório — este é o dado mais importante do player:** até 2025 os sorteios eram realizados sob autorização da **Loteria Estadual da Paraíba (Lotep)**. Esse modelo foi **questionado pela Secretaria de Prêmios e Apostas do Ministério da Fazenda quanto à competência legal do estado para autorizar esse tipo de atividade**. A empresa então **migrou em 2025 para o regime federal de capitalização regulado pela SUSEP** ([TechTudo](https://www.techtudo.com.br/guia/2025/04/pix-do-milhao-e-confiavel-saiba-como-funciona-site-que-realiza-sorteios-online-edsoftwares.ghtml)).

**[I]** Traduzindo: **o Pix do Milhão foi empurrado para a capitalização por pressão regulatória, não por escolha de design.** Ele é a prova viva de que loteria estadual não sustenta operação nacional — e de que a SUSEP é o porto seguro para onde o setor converge quando apertado. Isso valida a escolha do Seu Milhão pela via SUSEP, mas por um motivo diferente do que o PRD registra: não é diferenciação de marca, é **o único regime que sobrevive à fiscalização federal**.

**[E]** Razões sociais associadas na base do Reclame Aqui: **PIX DO MILHÃO CLUBE DE BENEFÍCIOS E VANTAGENS LTDA** e **Criative Publicidade, Promoções e Shows** ([Reclame Aqui](https://www.reclameaqui.com.br/empresa/criative-publicidade-promocoes-e-shows/)).

**[E]** Donos: **o influenciador A e sua sócia** (Poder Paraíba (link omitido: URL contém nome de pessoa)).

### 2.2 Preço — modelo híbrido assinatura + avulso

**[E]** Duas portas de entrada ([UAI](https://www.uai.com.br/networking-e-negocios/2026/06/26/o-que-e-o-pix-do-milhao-entenda-o-clube-de-beneficios-como-funciona-premios-valor-e-como-participar/)):
- **Assinatura mensal a partir de R$ [valor]** — pacote recorrente de benefícios
- **Compra avulsa de pontos a partir de R$ [valor]** — sem precisar assinar

Pagamento via Pix.

**[I]** Este é o modelo mais sofisticado do grupo: **R$ [valor] é o gancho de mídia, R$ [valor] é o negócio.** O anúncio da varredura F4 que convidava a entrar com o ticket mínimo estava vendendo o degrau de entrada de uma escada de assinatura — não o produto. Se o Seu Milhão anunciar R$ [valor] sem ter o degrau de recorrência montado atrás, estará pagando CAC de aquisição para um produto sem receita recorrente.

### 2.3 Estrutura de prêmio

| Camada | Valor | Cadência | Tag |
|---|---|---|---|
| Âncora | **R$ [valor]** | Semanal (sexta-feira, conforme uma fonte) | [E] [UAI](https://www.uai.com.br/networking-e-negocios/2026/06/26/o-que-e-o-pix-do-milhao-entenda-o-clube-de-beneficios-como-funciona-premios-valor-e-como-participar/) / [C] dia |
| Intermediário | **R$ [valor]** | Toda **segunda-feira** | [E] |
| Intermediário | **R$ [valor]** | Toda **terça-feira** | [E] |
| **Instantâneo** | **"Raspou, Achou, é Pix"** — prêmios instantâneos até R$ [valor] | Contínuo | [E] [UAI](https://www.uai.com.br/networking-e-negocios/2026/06/26/o-que-e-o-pix-do-milhao-entenda-o-clube-de-beneficios-como-funciona-premios-valor-e-como-participar/) · Poder Paraíba (link omitido: URL contém nome de pessoa) |

**[E]** Sorteios com base nos **resultados da Loteria da CAIXA**, com transmissão ao vivo do estúdio próprio da organização (Poder Paraíba (link omitido: URL contém nome de pessoa)).

**[I]** A **grade semanal nomeada por dia** (segunda R$ [valor], terça R$ [valor], sexta R$ [valor]) é o desenho mais agressivo de retenção do grupo. Cria hábito diário, não evento semanal. Nenhum outro player tem cadência tão fragmentada.

### 2.4 Escala e canais

**[E]** Números auto-reportados de benefícios (não de sorteio): usuários economizaram **mais de R$ [valor] em medicamentos só em maio/2026**, acumulado **superior a R$ [valor] em 2026** ([TechTudo](https://www.techtudo.com.br/guia/2025/04/pix-do-milhao-e-confiavel-saiba-como-funciona-site-que-realiza-sorteios-online-edsoftwares.ghtml)).

**[E]** Claim de mídia observado na pesquisa F4: [claim de [n] ganhadores em [n] anos] — **[I]** não encontrei validação independente; tratar como claim publicitário.

**[E]** Canais: influenciador-fundador (influenciador A como rosto e embaixador — [Instagram oficial](https://www.instagram.com/pixdomilhaooficial/p/C7XB_hMAA6S/)), **patrocínio master do Botafogo-PB desde fev/2026** (Poder Paraíba (link omitido: URL contém nome de pessoa)), app próprio iOS ([App Store](https://apps.apple.com/br/app/pix-do-milh%C3%A3o-oficial/id6756222511)), transmissão ao vivo em estúdio próprio, rede de afiliados com landing pages replicadas.

**[E]** **Sinal de ecossistema descontrolado de afiliados:** o domínio `pixdomilhao.live` retorna hoje um **"Website Takedown Notice — Lovable Trust & Safety"** (verificado 14/08/2026). **[I]** Landing pages de afiliado construídas em no-code e derrubadas por abuso — risco de marca embutido no modelo de afiliados agressivo.

### 2.5 Controvérsias — o player com o maior passivo reputacional

- **[E]** **Denúncia do Ministério Público** contra o influenciador A, um ex-prefeito e mais três pessoas, por envolvimento em **processo irregular de desapropriação de lotes** (Portal do Litoral PB (link omitido: URL contém nome de pessoa), 1001 Notícias (link omitido: URL contém nome de pessoa)). **[I]** Assunto pessoal/imobiliário, não do produto — mas contamina o rosto da marca, que é o próprio ativo de aquisição.
- **[E]** Cobertura de imprensa sobre **"suposta farsa milionária"** por trás dos **e-books premiados** ([Blog do FM](https://blogdofm.com.br/pix-do-milhao-entenda-a-suposta-farsa-milionaria-que-estaria-enganando-o-brasil-por-tras-dos-e-books-premiados/) — página retornou 403 na tentativa de leitura direta; título e enquadramento confirmados via índice de busca, conteúdo **não verificado** [I]).
- **[E]** Denúncia registrada no Reclame Aqui: *"Possível Esquema Irregular Utilizando Ebooks para Contornar Fiscalizações"* ([Reclame Aqui](https://www.reclameaqui.com.br/criative-publicidade-promocoes-e-shows/denuncia-possivel-esquema-irregular-no-sorteio-pix-do-milhao-utilizando_LTAwkybUqzw9cniV/)).
- **[E]** Reclamações de **não pagamento de prêmio e falta de suporte** ([Reclame Aqui](https://www.reclameaqui.com.br/criative-publicidade-promocoes-e-shows/nao-pagamento-de-premio-do-sorteio-pix-do-milhao-e-falta-de-suporte_iCfpOuzehpkAMYjv/)).
- **[E]** Após operação da PF que mirou bets em 2024, o influenciador gravou vídeo público explicando como sorteia R$ [valor] ([Maurílio Júnior](https://mauriliojunior.com/2024/09/06/apos-operacao-que-mira-bets-influenciador-paraibano-grava-video-para-explicar-como-sorteia-r-1-milhao/)).

**[I]** **Pix do Milhão é o caso de estudo de por que a "transparência do mecanismo" (o whitespace sem nenhum anúncio identificado em F4) é valiosa:** ele foi obrigado a fazer transparência **reativamente**, sob pressão de operação policial e de imprensa. Quem faz proativamente compra o mesmo ativo por muito menos.

---

## 3. Apcap ("Apcap da Sorte")

### 3.1 A arquitetura mais complexa do grupo — quatro entidades, dupla autorização

**[E]** Rodapé legal do site oficial ([apcapdasorte.com.br](https://apcapdasorte.com.br/), [/sorteios](https://apcapdasorte.com.br/sorteios), [/home-institucional](https://apcapdasorte.com.br/home-institucional)):

| Papel | Entidade | CNPJ |
|---|---|---|
| **Emissora do título** | **[emissora B]** | [CNPJ omitido] |
| **Promotora da promoção** | **IDEA MAKER MEIOS DE PAGAMENTO E CONSULTORIA** | [CNPJ omitido] |
| **Distribuidora / vendedora do produto** | **SAFE INK DIGITAL EDITORA S/A** | [CNPJ omitido] |
| **Entidade beneficiada** | **Hospital de Amor** (Barretos) — "maior centro oncológico de atendimento gratuito da América Latina" | — |

**[E]** Modalidade: **Incentivo de Contribuição Única**. Processos SUSEP: **15414.670127/2025-62, 15414.659942/2025-71 e 15414.623793/2023-40**. **Autorização SPA/ME nº 05.047999/2026** ([apcapdasorte.com.br/sorteios](https://apcapdasorte.com.br/sorteios)).

**[E] O que o consumidor efetivamente compra é um E-BOOK**, vendido em **pacotes combo**: *"cada compra gera números da sorte automaticamente. Quanto maior a série, mais cupons você acumula"* ([apcapdasorte.com.br](https://apcapdasorte.com.br/)).

**[I]** Note a diferença estrutural de arquitetura A: quem compra o título de capitalização é a **Idea Maker** (a promotora), não o cliente. O cliente compra um e-book de uma **editora** e recebe o sorteio como brinde promocional. Isso significa que **a relação de consumo do cliente não é regida pelas normas de capitalização da SUSEP** — é uma compra de produto digital com promoção acoplada, sob Lei 5.768/1971 e SPA. **É juridicamente sólido e simultaneamente é onde mora a crítica pública de "contornar fiscalização".**

**[I]** A dupla numeração das autorizações SPA é informativa: o prefixo **05.xxx** (usado pela Apcap e pelo Familhão no prêmio instantâneo) corresponde à modalidade **vale-brinde**, e **04.xxx** a **sorteio**. Quem quiser rodar raspadinha/instantâneo no Brasil provavelmente precisa de autorização de vale-brinde separada da de sorteio — **e o PRD §6.10 registra que a "regra de negócio da raspadinha nunca foi especificada" no Seu Milhão.** Isso não é só regra de produto; é uma segunda autorização regulatória.

### 3.2 Preço

**[E/C]** Divergência entre fontes — provável reflexo de múltiplos produtos coexistindo:
- **R$ [valor]** — título de Filantropia Premiável de pagamento único ([Reclame Aqui — conteúdo institucional APCAP](https://www.reclameaqui.com.br/empresa/apcap-sp/conteudos/saiba-tudo-sobre-as-nossas-premiacoes_8aV0YTD6lTpX3TJX/))
- **R$ [valor]** — cupom ([Informa Curitiba](https://informa.curitiba.br/loterias/loterias-gerais/como-funciona-o-apcap-da-sorte/))
- **R$ [valor]** — preço observado em anúncio ativo no Meta Ad Library (*"A sua chance começa com R$ [valor]"*), pesquisa F4, 11/08/2026 [E]

**[I]** **Apcap opera preço em escada, não preço único** — R$ [valor] é o degrau de mídia, R$ [valor] é o produto de prateleira. Mesmo padrão do Pix do Milhão. **Dois dos três players de arquitetura B têm preço-de-anúncio menor que preço-de-produto.** Isso reforça o achado F4 de que o preço no criativo é gancho de CTA, não a economia real.

### 3.3 Estrutura de prêmio — a grade mais densa do mercado

**[E]** **Uma única compra participa de 4 sorteios diferentes** ([Reclame Aqui — institucional](https://www.reclameaqui.com.br/empresa/apcap-sp/conteudos/saiba-tudo-sobre-as-nossas-premiacoes_8aV0YTD6lTpX3TJX/)):

| Sorteio | Prêmio | Cadência | Tag |
|---|---|---|---|
| **Estouro da Sorte / Balão do Milhão** | **Instantâneo até R$ [valor]** via Pix na hora + [n] Pix instantâneos até R$ [valor] | Contínuo | [E] |
| **Domingão da Sorte** | Carro elétrico BYD Dolphin + R$ [valor] = **R$ [valor]** | Domingo | [E] [Informa Curitiba](https://informa.curitiba.br/loterias/loterias-gerais/como-funciona-o-apcap-da-sorte/) |
| **Sabadão da Sorte** | **R$ [valor]** + R$ [valor] "Na Trave" | Sábado | [E] |
| **Dia da Sorte** | — | Diário | [E] |

**[I] O achado estrutural mais forte da Apcap:** o prêmio âncora de R$ [valor] **não é do sorteio semanal — é do instantâneo**. Ela inverteu a economia padrão do setor. Enquanto todos usam o milhão como evento de calendário, a Apcap usa como possibilidade permanente. Isso é o que sustenta o formato de anúncio "prova de pagamento nomeada" que F4 identificou como exclusivo dela: **prova de pagamento só funciona como formato se você tem pagamentos acontecendo o tempo todo.** Formato de anúncio e arquitetura de prêmio são a mesma decisão.

### 3.4 Escala

**[E]** Claim oficial: **[n] ganhadores**, [n] pessoas "com a vida transformada", **R$ [valor] distribuídos** em prêmios (acumulado) ([apcapdasorte.com.br](https://apcapdasorte.com.br/), [Informa Curitiba](https://informa.curitiba.br/loterias/loterias-gerais/como-funciona-o-apcap-da-sorte/)).

**[I]** [n] "ganhadores" com R$ [valor] distribuídos dá **R$ [valor] por ganhador** — o número de ganhadores está contando micro-prêmios instantâneos. É claim de mídia, não de economia. Útil como benchmark de *como se conta a história*, não de tamanho.

**[E]** Autodescrição: *"a maior promoção comercial com sorteios lastreados por títulos de capitalização da modalidade incentivo do Brasil"* ([Informa Curitiba](https://informa.curitiba.br/loterias/loterias-gerais/como-funciona-o-apcap-da-sorte/)).

### 3.5 Origem e tempo de mercado

**[E]** A **Idea Maker** já operava a **"Corrente de Amor"**, criada em **maio de 2020** pelo Hospital de Amor em parceria com a Idea Maker, para arrecadar fundos via doações e sorteios: *"a cada doação a partir de R$ [valor] o cliente recebe um número da sorte por SMS, com instruções para baixar o aplicativo Apcap do Bem"* ([A Tribuna Regional](https://atribunaregional.com.br/corrente-de-amor-destina-mais-de-r%EF%BC%84-53-milhoes-ao-hospital-de-amor/)). O app Apcap da Sorte está na App Store desde ao menos 2018 ([App Store](https://apps.apple.com/br/app/apcap-da-sorte/id1444105915)).

**[I]** Portanto: Apcap ≈ **6 anos** no modelo digital-filantrópico atual, e mais tempo como app. Não é entrante.

### 3.6 Canais

**[E]** App oficial iOS/Android, site de compra, **YouTube**, **RedeTV!**, **Record**, Instagram, Facebook, TikTok ([apcapdasorte.com.br/home-institucional](https://apcapdasorte.com.br/home-institucional)).

**[I]** Apcap é o único player do grupo com **TV aberta em duas emissoras simultâneas** + YouTube como canal primário declarado. Combinado com o achado F4 (anúncio mais persistente da varredura, ~[n] semanas e [n] variantes, e **único anúncio de reativação/CRM de todo o dataset**), o perfil é de operação de mídia madura com funil completo — não de teste.

### 3.7 Controvérsias

- **[E]** Reclame Aqui **APCAP da Sorte**: [n] reclamações, **nota [n]/10** (6 meses), [x%] resolvidas, [x%] respondidas, com selo de verificação ([Reclame Aqui](https://www.reclameaqui.com.br/empresa/apcap-da-sorte/)). **[I]** Melhor reputação relativa entre todos os players deste relatório.
- **[E]** Reclamações concentradas em **dificuldade de saque de prêmio** (erro 0010 após envio de selfie e documento) e **cupons não creditados** ([Reclame Aqui](https://www.reclameaqui.com.br/apcap-da-sorte/lista-reclamacoes/)).
- **[E]** Resposta institucional: *"todos os sorteios passam por auditorias rigorosas seguindo o mesmo modelo dos sorteios da Loteria Federal"*.
- **[I]** Não encontrei autuação regulatória, ação do MP ou notícia negativa de imprensa relevante contra a Apcap. **É o player mais limpo do conjunto.**

---

## 4. Familhão (apresentador de TV A)

### 4.1 Enquadramento — o outlier: NÃO é capitalização

**[E]** Rodapé oficial ([familhao.com](https://www.familhao.com/)):
- Operador: **Familhão Engajamento e Intermediação S.A.**, [CNPJ omitido], Barueri/SP
- **Três certificados de autorização SPA/MF**:
  - Sorteio principal: **nº 04.048228/2026**
  - Prêmios instantâneos: **nº 05.047975/2026**
  - Sorteio semanal de viagem: **nº 04.047756/2026**
- **Nenhuma menção a SUSEP, a sociedade de capitalização ou a título de capitalização no rodapé.**

**[E]** Desenvolvido pela **D+V**, joint venture entre a **Dilus** (desenvolvedora de projetos) e a **Vertem** (ecossistema de engajamento) (Meio & Mensagem (link omitido: URL contém nome de pessoa)).

**[I] Este é o achado regulatório mais importante do relatório para o Seu Milhão.** O Familhão — o player com o maior rosto do Brasil e integração com a Globo — **operou sem precisar ser capitalização**. Ele resolveu tudo com autorização de promoção comercial da SPA sobre uma assinatura de clube de benefícios. Isso significa que **"ser SUSEP" não é pré-requisito para operar sorteio de R$ [valor] em escala nacional com marca premium** — o que enfraquece a premissa central do PRD de que a capitalização é *a* diferenciação. A diferenciação real do Seu Milhão precisa ser outra coisa.

### 4.2 Preço e produto

**[E]** **R$ [valor]/mês**, pagamento via **Pix ou cartão de crédito**. Por esse valor o assinante recebe ([familhao.com](https://www.familhao.com/), TechTudo (link omitido: URL contém nome de pessoa)):
- [n] créditos (≈ R$ [valor]) para trocar no "Lojão do Familhão" — validade de 2 anos
- **1 número da sorte** para o sorteio mensal de R$ [valor]
- 1 cupom de desconto
- [n] figurinhas colecionáveis (álbum completo rende créditos extras)

**[E]** **[n] níveis de plano**, indo de um pacote básico de créditos até experiências exclusivas com celebridades + acesso ao Globoplay ([familhao.com](https://www.familhao.com/)).

**[E]** Prêmio instantâneo **"Achou, Levou!"** por **R$ [valor] adicionais** ([familhao.com](https://www.familhao.com/)).

**[I]** Ticket de **R$ [valor]/mês é [n]× o ticket de entrada dos concorrentes** (R$ [valor]–R$ [valor]). O Familhão não compete por impulso — compete por assinatura. É o único do grupo cuja unidade econômica é claramente recorrente por design, não por upsell.

### 4.3 Estrutura de prêmio

| Camada | Valor | Cadência | Tag |
|---|---|---|---|
| Âncora | **R$ [valor] em barras de ouro** | **Mensal** | [E] |
| Semanal | **Uma "super viagem"** | Semanal | [E] |
| Instantâneo | "Achou, Levou!" (R$ [valor] adicional) | Contínuo | [E] |

**[E]** Apuração com base nos números da **Loteria Federal**. **O apresentador de TV A entrega o prêmio pessoalmente**, e a entrega vai ao ar no **programa dominical dele** (Globo) (TechTudo (link omitido: URL contém nome de pessoa)).

**[I]** É o único player cujo **momento de entrega do prêmio é o próprio produto de mídia**. A pesquisa F4 identificou "documentário/revelação (visita-surpresa)" como a assinatura exclusiva do Familhão — agora está claro que não é uma escolha criativa, é a **consequência direta do desenho do prêmio**: mensal (raro o suficiente para virar evento), com celebridade, em horário nobre. Cadência mensal é o que torna o formato documentário economicamente viável. **Um player com sorteio diário não consegue produzir esse formato.**

### 4.4 Escala e tração

| Métrica | Valor | Fonte |
|---|---|---|
| Lançamento | **06/03/2024**, no programa dominical do apresentador (Globo) | [E] Meio & Mensagem (link omitido: URL contém nome de pessoa) |
| Assinantes ativos | **[n]** (nov/2024) | [E] TechTudo (link omitido: URL contém nome de pessoa) |
| Projeção | **[n] em [n] anos** | [E] mesma fonte |
| Reclamações Reclame Aqui | **[n]** (mai/2026) | [E] FDR (link omitido: URL contém nome de pessoa) |

**[I]** [n] assinantes × R$ [valor]/mês ≈ **R$ [valor]/mês de receita bruta recorrente**, contra R$ [valor]/mês de prêmio âncora. **A economia do prêmio é irrelevante no P&L do Familhão** — o prêmio é custo de aquisição, e a margem vem do clube. Este é o modelo que o PRD §6.3 ("economia do produto em branco") precisa como referência: **não modele o produto a partir do prêmio; modele a partir do que sustenta a recorrência.**

### 4.5 Canais

**[E]** Integração com o **programa dominical do apresentador** (Globo, domingo, horário nobre); o apresentador de TV A como rosto — as fontes o descrevem como **sócio** em alguns registros e como garoto-propaganda/personalidade em outros; **[I]** participação societária **não confirmada** por fonte primária.

**[E]** Rede de parceiros de benefício no lançamento: 99, Burger King/Popeyes, ChilliBeans, Domino's, **Globoplay**, iFood, Natura, Pague Menos, Petrobras Premmia, Petlove, Polishop, Vivo, Zé Delivery (Meio & Mensagem (link omitido: URL contém nome de pessoa)).

**[E]** Agências: Galeria, Tomato e Monumenta (planejamento estratégico), Vetor Zero (produção).

### 4.6 Controvérsias

- **[E]** **[n] reclamações** acumuladas até mai/2026, com relatos de **pagamentos debitados sem contrapartida em créditos** e **ausência de suporte**; recomendação corrente de registro no Procon estadual para forçar reembolso (FDR (link omitido: URL contém nome de pessoa)).
- **[E]** Crise de reputação em **maio/2026**: o apresentador criticou publicamente o Bolsa Família ("ineficiente") em fórum empresarial, gerando reação ampla (Poder360 (link omitido: URL contém nome de pessoa), O Tempo (link omitido: URL contém nome de pessoa)). A imprensa fez o contraste direto entre a crítica ao programa social e as reclamações do próprio clube de assinatura, cujo público-alvo é a mesma faixa de renda.
- **[E]** Reação pública do público ao formato de premiação: *"Pavor de ganhar"* (Terra (link omitido: URL contém nome de pessoa)).

**[I]** **Risco de canal aprendível:** a marca do Familhão é indistinguível do risco reputacional de uma pessoa física. Quando o apresentador teve uma crise pública, o produto foi arrastado junto no mesmo ciclo de notícia. O Seu Milhão herda rede de influenciadores de um parceiro e tem um parceiro do projeto como relacionamento central — **concentrar a marca em um rosto único é o mesmo trade-off, sem o mesmo colchão de escala.**

---

## 5. SBT Prêmios

### 5.1 Enquadramento

**[E]** **Título de capitalização, modalidade Filantropia Premiável**, operado pela **Liderança Capitalização S.A.** (a mesma da Tele Sena), pagamento único de **R$ [valor]**, **vigência de 2 meses** a partir da data de aquisição ([SBT Prêmios — condições gerais](https://demo.sbtpremios.com/condicoes-gerais), via índice de busca; página retornou 403 na leitura direta).

**[E]** Entidade beneficiada: **Instituto Ronald McDonald** (tratamento de câncer infantojuvenil) — o comprador cede o direito de resgate ([Diário Indústria & Comércio](https://www.diarioinduscom.com.br/Noticias/884672/lideranca_capitalizacao_acelera_expansao_alem_da_tele_sena)).

**[I]** Arquitetura **A pura** — a mais próxima do que o PRD do Seu Milhão descreve. Sem e-book, sem clube de pontos, sem SPA. É o modelo de referência mais limpo se o squad seguir a via filantropia premiável.

### 5.2 Preço, prêmio e cadência

| Item | Valor | Tag |
|---|---|---|
| Ticket | **R$ [valor]** (pagamento único) | [E] |
| Vigência do título | **2 meses** | [E] |
| Cadência | **Sorteios semanais, aos domingos**, transmitidos | [E] |
| Prêmio | Prêmios em dinheiro + **experiências exclusivas** | [E] |
| SLA de pagamento | Até **15 dias corridos** após documentação (norma SUSEP) | [E] [Circular SUSEP 656/22](https://www.legisweb.com.br/legislacao/?id=428900) |

**[I]** Não encontrei valor de prêmio âncora publicado para o SBT Prêmios. Dado o ticket de R$ [valor] e o volume de [n] títulos/mês (abaixo), a receita mensal é da ordem de **R$ [valor]** — o que **não comporta** um prêmio âncora de R$ [valor] semanal sem outras fontes. **[I]** Provável que o âncora seja materialmente menor que o de Viva Sorte/Apcap/PDM, ou que o valor circule em prêmios menores e experiências. Gap de pesquisa.

### 5.3 Escala — o dado mais concreto do relatório

**[E]** ([Diário Indústria & Comércio](https://www.diarioinduscom.com.br/Noticias/884672/lideranca_capitalizacao_acelera_expansao_alem_da_tele_sena)):
- **[n] títulos vendidos por mês**
- **Projeção de R$ [valor] de receita em 2026**
- Meta de **dobrar o volume mensal** até o fim do ano
- Segmento de **incentivo B2B** com projeção de crescimento de até **[x%] em 2026**; clientes ativos: Gazin Seguros, BMG Seguros, Akad Seguros

**[E]** CEO da Liderança: *"Por não integrar um conglomerado financeiro, a companhia atua sem conflito direto com seguradoras."*

**[E]** A Tele Sena mantém **[x%] de market share em capitalização popular**; a diversificação do SBT Prêmios existe justamente para reduzir a dependência dela, sobre um legado de **80 anos** de companhia.

**[I] Este é o único número público limpo de conversão de ticket→receita do setor:** [n] títulos/mês × R$ [valor] ≈ **R$ [valor]/mês ≈ R$ [valor]/ano**, contra projeção declarada de R$ [valor] em 2026. A diferença sugere que ou o volume de [n] é recente, ou parte da receita é repassada (entidade filantrópica + emissora). **Use R$ [valor]/[n]-títulos-mês como âncora de sanity-check para qualquer modelo financeiro do Seu Milhão.**

### 5.4 Cronologia e canais

**[E]** Lançado em **dezembro de 2025** pela Liderança em parceria com o SBT, como **plataforma totalmente digital** ([Jornal Tribuna](https://www.jornaltribuna.com.br/2025/12/sbt-lanca-plataforma-100-digital-de-premios-e-inaugura-nova-fase-de-inovacao-na-tv-brasileira) — 403 na leitura direta, título e data confirmados via índice). Em **abril de 2026 a Liderança assumiu a gestão integral da operação** ([Diário Indústria & Comércio](https://www.diarioinduscom.com.br/Noticias/884672/lideranca_capitalizacao_acelera_expansao_alem_da_tele_sena)).

**[E]** Canais: TV aberta (SBT), site/app próprio, expansão geográfica planejada (lançamento em Santa Catarina com oferta localizada), investimento em modernização tecnológica e IA para automação.

**[I]** **8 meses de mercado — é o player mais novo do grupo, e já faz [n] títulos/mês.** Ou seja: com emissora estabelecida + marca de TV, a curva de rampa é de meses, não de anos. Isso é diretamente relevante para o Seu Milhão: **o gargalo não é tempo de mercado, é ter emissora e distribuição.** O PRD §5.1 registra "Emissor SUSEP: nunca nomeado" como gap crítico — este player mostra o custo desse gap.

### 5.5 Controvérsias

**[I]** Não encontrei controvérsia, autuação ou notícia negativa relevante contra o SBT Prêmios. **[E]** Existe, porém, um ecossistema ativo de **golpes usando o nome do SBT e de uma apresentadora da emissora** prometendo prêmios instantâneos via WhatsApp/links, desmentido por checagem (Boatos.org (link omitido: URL contém nome de pessoa)).

**[I]** Padrão transversal: **os cinco players têm clones/golpes usando sua marca.** Não é exceção, é custo fixo da categoria. O Seu Milhão precisa de plano de brand protection **antes** do primeiro anúncio, não depois.

---

## 6. Tabela comparativa

| | **Viva Sorte** | **Pix do Milhão** | **Apcap da Sorte** | **Familhão** | **SBT Prêmios** |
|---|---|---|---|---|---|
| **Preço de entrada** | R$ [valor] (**variável por edição**) [E] | R$ [valor] avulso · **R$ [valor]/mês** assinatura [E] | R$ [valor] (anúncio) · R$ [valor] (produto) [E/C] | **R$ [valor]/mês** (+R$ [valor] instantâneo) [E] | **R$ [valor]** único [E] |
| **Prêmio âncora** | R$ [valor] Pix [E] | R$ [valor] [E] | **R$ [valor] INSTANTÂNEO** (Balão do Milhão) [E] | R$ [valor] em barras de ouro [E] | Não publicado [I] |
| **Cadência** | Semanal (dom 10h30, Band) [E] | Sexta R$ [valor] · **seg R$ [valor] · ter R$ [valor]** [E] | Diário + sáb + dom + instantâneo contínuo [E] | **Mensal** + viagem semanal [E] | Semanal (domingo) [E] |
| **Camada instantânea** | "Giropix" + raspadinha [C/E] | "Raspou, Achou, é Pix" até R$ [valor] [E] | Estouro da Sorte até R$ [valor] · Balão até R$ [valor] [E] | "Achou, Levou!" (R$ [valor]) [E] | Não identificada [I] |
| **Canal principal** | **TV Band + PDVs + clubes de futebol** [E] | **Influenciador-fundador + afiliados** [E] | **YouTube + RedeTV! + Record + app** [E] | **Globo / programa dominical do apresentador** [E] | **SBT (TV aberta) + digital** [E] |
| **Arquitetura regulatória** | **A + B** (Filantropia Premiável **e** clube de pontos Incentivo) [E] | **B** — clube de benefícios + título Incentivo [E] | **B** — e-book + Incentivo + SPA vale-brinde [E] | **C** — promoção comercial pura, **sem SUSEP** [E] | **A** — Filantropia Premiável pura [E] |
| **Emissora** | ViaCap [E] | ViaCap [E] | **[emissora B]** [E] | **Nenhuma** [E] | **Liderança Capitalização** [E] |
| **Entidade beneficiada** | APAE Brasil / Hosp. Câncer de Londrina [E] | n/a (Incentivo) [E] | Hospital de Amor (Barretos) [E] | n/a [E] | Instituto Ronald McDonald [E] |
| **Autorização adicional** | SPA/MF 2.104-39 (a **bet** do grupo) [E] | — | SPA/ME 05.047999/2026 [E] | SPA/MF 04.048228, 05.047975, 04.047756/2026 [E] | — |
| **Ano de entrada** | Produto 2022 · grupo ~16 anos [E] | Lotep até 2025 → SUSEP 2025 [E] | Corrente de Amor 2020 · app desde 2018 [E] | **mar/2024** [E] | **dez/2025** [E] |
| **Escala pública** | Meta R$ [valor]/2025 · [n] PDVs [E] | R$ [valor] economia em benefícios 2026 [E] | [n] "ganhadores" · R$ [valor] distribuídos [E] | **[n] assinantes** (nov/24) [E] | **[n] títulos/mês · R$ [valor] proj. 2026** [E] |
| **Reclame Aqui** | [n] · **[n]**/10 [E] | Reclamações de não-pagamento [E] | [n] · **[n]**/10 [E] | **[n]** reclamações [E] | Não identificado [I] |
| **Passivo público** | Raspadinha não paga · clones [E] | **Denúncia do MP** (pessoal) · "farsa dos e-books" · PF/bets [E] | Nenhum relevante [I] | [n] reclamações · crise Bolsa Família [E] | Nenhum relevante [I] |

---

## 7. Sete leituras que mudam decisões do Seu Milhão

1. **"Capitalização SUSEP" não é diferenciação — é tabela de entrada, e nem isso.** [E] O Familhão faz R$ [valor]/mês com marca premium e [n] assinantes **sem ser capitalização**, só com autorização SPA. [I] A premissa do PRD §2.2 ("por que SUSEP e não rifa") precisa ser reescrita: a escolha real não é SUSEP-vs-rifa, é **entre três arquiteturas legais, todas legítimas**, com custos e velocidades diferentes.

2. **O benchmark eleito (Viva Sorte) não ganha por anúncio.** [E] TV Band semanal, rede de PDVs, clubes de futebol patrocinados, dono com grande audiência própria. [I] Copiar o Viva Sorte via Meta Ads é copiar o único canal em que ele não é referência — e explica por que ele não apareceu na varredura F4.

3. **O prêmio âncora não precisa ser semanal — e a cadência determina o formato de anúncio.** [I] Apcap tornou o milhão **instantâneo e permanente** (e por isso pode viver de prova de pagamento). Familhão tornou **mensal e televisionado** (e por isso pode viver de documentário). **A escolha de cadência é anterior à escolha de formato criativo, e o PRD trata as duas como independentes.**

4. **Preço de anúncio ≠ preço de produto em 3 dos 5 players.** [E] PDM anuncia R$ [valor] e vende assinatura de R$ [valor]; Apcap anuncia R$ [valor] e vende título de R$ [valor]. Viva Sorte **varia o preço a cada semana**. [I] O PRD trata o ticket como constante de copy; o mercado trata como variável de campanha.

5. **A raspadinha é uma segunda autorização regulatória, não uma feature.** [E] Familhão e Apcap têm certificados SPA distintos, com prefixo 05.xxx (vale-brinde), separados do sorteio (04.xxx). [I] O PRD §6.10 trata a raspadinha como "regra de negócio nunca especificada" — o risco é maior: pode ser um processo de autorização inteiro não previsto no cronograma.

6. **ViaCap emite para dois dos cinco players e é o fornecedor default do nicho.** [E] Viva Sorte e Pix do Milhão. Alternativas identificadas: **[emissora B]** (Apcap), **Liderança** (SBT Prêmios), e **ApliCap**, que se posiciona explicitamente como emissora para influenciadores — R$ [valor] destinados a entidades beneficentes em 2025, R$ [valor]+ de faturamento, R$ [valor] em prêmios em cinco meses ([SEGS](https://www.segs.com.br/seguros/432177-aplicap-alcanca-mais-de-r-450-milhoes-em-faturamento-com-crescimento-expressivo-em-2025), [JRS Portal](https://jrsportal.com.br/artigo-jrs/em-apenas-cinco-meses-aplicap-distribui-r-109-milhoes-em-premios/), [ApliCap — Regularize seus Sorteios](https://aplicap.com.br/regularize-seus-sorteios/)). [I] O gap "Emissor SUSEP nunca nomeado" (PRD §5.1) tem **pelo menos 4 candidatos concretos e um deles vende exatamente para o perfil do Seu Milhão.** Isso é resolvível em uma semana de calls, não é bloqueio estrutural.

7. **A regulação está em movimento agora, e a arquitetura B é a exposta.** [E] A **Portaria SPA/MF nº 230, de 28/01/2026**, instituiu **Grupo de Trabalho sobre Promoções Comerciais** para apoiar a revisão de normas de distribuição gratuita de prêmios ([LegisMap](https://legismap.com.br/leis-e-normas/portaria-spa-mf-n-230-de-28-01-2026)). [E] O Pix do Milhão já foi forçado a mudar de regime uma vez (Lotep → SUSEP) por questionamento da SPA. [I] Quem opera arquitetura B (e-book/clube + Incentivo) está no escopo direto dessa revisão. Arquitetura A (filantropia premiável) é a menos exposta — **e é a que o Seu Milhão está desenhando.** É a decisão mais defensável do PRD, por um motivo que o PRD não registra.

---

## 8. Lacunas desta pesquisa (não resolvidas)

| Lacuna | Por que importa | Como fechar |
|---|---|---|
| Prêmio âncora do SBT Prêmios não publicado | Único player sem valor de âncora conhecido | Ler regulamento em `sbtpremios.com` (bloqueou WebFetch — 403; tentar via app ou navegador) |
| Preço exato e tabela de séries do Viva Sorte | Benchmark #1 do squad; só temos faixa de preço | `regulamento.vivasorteoficial.com.br` retornou HTTP 530 nas duas tentativas — repetir; ou comprar um título e ler as Condições Gerais |
| Participação societária do apresentador de TV A no Familhão | Muda a leitura de risco de marca | Consulta de quadro societário do CNPJ do operador |
| Existência de autuação SUSEP/SPA contra qualquer player | Ausência de notícia ≠ ausência de processo | Consulta direta ao sistema de processos SUSEP e ao DOU |
| Volume/faturamento real de Viva Sorte, PDM e Apcap | Todos os números são metas ou claims, não auditados | Não há fonte pública; só via demonstrações financeiras das emissoras (as emissoras publicam na SUSEP) |
| Conteúdo integral do Blog do FM sobre "farsa dos e-books" | Único material investigativo encontrado sobre arquitetura B | Página retorna 403; tentar via arquivo/cache |

---

## Fontes

**Viva Sorte:** [Regulamento oficial](https://regulamento.vivasorteoficial.com.br/) · [Site oficial](https://vivasorteoficial.com.br/) · [BNLData — meta R$ [valor] (link omitido)] · [Máquina do Esporte — grupo e patrocínios](https://maquinadoesporte.com.br/apostas/quem-e-viva-sorte-grupo-que-mais-avanca-no-mercado-de-patrocinio-do-futebol-brasileiro/) · Econodata — CNPJ distribuidora (link omitido: contém CNPJ) · [Reclame Aqui — Viva Sorte](https://www.reclameaqui.com.br/empresa/viva-sorte/) · [Reclame Aqui — VIA Cap](https://www.reclameaqui.com.br/empresa/via-cap/lista-reclamacoes/) · [Reclame Aqui — raspadinha não paga](https://www.reclameaqui.com.br/viva-sorte/viva-sorte-nao-paga-premio-da-raspadinha_3cAtAnGMbhKig14H/) · [Portal de Pinhal — análise](https://portaldepinhal.com.br/2025/09/como-funciona-o-viva-sorte-e-confiavel-analise-sincera/) · [Portal de Pinhal — carros por R$ [valor]](https://portaldepinhal.com.br/2025/01/viva-sorte-oficial-concorra-a-10-carros-0km-neste-domingo-por-apenas/) · [X oficial — lançamento Viva Sorte+](https://x.com/viva_sorte/status/1967226835353403680) · [Google Play — app](https://play.google.com/store/apps/details?id=com.edjdigital.vivasorte) · [Claro — grade Band](https://www.claro.com.br/tv-por-assinatura/programacao/grade/programa/band/1-2247/viva-sorte/1-1016807) · [Correio Braziliense — Viva Sorte Bet](https://www.correiobraziliense.com.br/apostas/viva-sorte) · [OddsScanner — Viva Sorte Bet](https://oddsscanner.com/br/apostas/viva-sorte-bet) · [JRS — sorteios na Band](https://jrs.digital/sorteios-da-nova-operacao-da-viacap-serao-transmitidos-na-band/)

**Pix do Milhão:** [TechTudo](https://www.techtudo.com.br/guia/2025/04/pix-do-milhao-e-confiavel-saiba-como-funciona-site-que-realiza-sorteios-online-edsoftwares.ghtml) · [UAI](https://www.uai.com.br/networking-e-negocios/2026/06/26/o-que-e-o-pix-do-milhao-entenda-o-clube-de-beneficios-como-funciona-premios-valor-e-como-participar/) · Poder Paraíba — Botafogo-PB (link omitido: URL contém nome de pessoa) · Portal do Litoral PB — denúncia do MP (link omitido: URL contém nome de pessoa) · 1001 Notícias (link omitido: URL contém nome de pessoa) · [Maurílio Júnior — vídeo após operação da PF](https://mauriliojunior.com/2024/09/06/apos-operacao-que-mira-bets-influenciador-paraibano-grava-video-para-explicar-como-sorteia-r-1-milhao/) · [Reclame Aqui — denúncia e-books](https://www.reclameaqui.com.br/criative-publicidade-promocoes-e-shows/denuncia-possivel-esquema-irregular-no-sorteio-pix-do-milhao-utilizando_LTAwkybUqzw9cniV/) · [Reclame Aqui — não pagamento](https://www.reclameaqui.com.br/criative-publicidade-promocoes-e-shows/nao-pagamento-de-premio-do-sorteio-pix-do-milhao-e-falta-de-suporte_iCfpOuzehpkAMYjv/) · [App Store](https://apps.apple.com/br/app/pix-do-milh%C3%A3o-oficial/id6756222511) · [Site oficial](https://pixdomilhao.com.br/)

**Apcap:** [Site oficial](https://apcapdasorte.com.br/) · [Sorteios — rodapé legal](https://apcapdasorte.com.br/sorteios) · [Institucional](https://apcapdasorte.com.br/home-institucional) · [Informa Curitiba — prêmios e preços](https://informa.curitiba.br/loterias/loterias-gerais/como-funciona-o-apcap-da-sorte/) · [Reclame Aqui — institucional premiações](https://www.reclameaqui.com.br/empresa/apcap-sp/conteudos/saiba-tudo-sobre-as-nossas-premiacoes_8aV0YTD6lTpX3TJX/) · [Reclame Aqui — APCAP da Sorte](https://www.reclameaqui.com.br/empresa/apcap-da-sorte/) · [A Tribuna Regional — Corrente de Amor](https://atribunaregional.com.br/corrente-de-amor-destina-mais-de-r%EF%BC%84-53-milhoes-ao-hospital-de-amor/) · [App Store](https://apps.apple.com/br/app/apcap-da-sorte/id1444105915)

**Familhão:** [Site oficial](https://www.familhao.com/) · TechTudo (link omitido: URL contém nome de pessoa) · Meio & Mensagem — lançamento (link omitido: URL contém nome de pessoa) · Meio & Mensagem — apresentador explica (link omitido: URL contém nome de pessoa) · FDR — 4.460 reclamações (link omitido: URL contém nome de pessoa) · Poder360 — crise Bolsa Família (link omitido: URL contém nome de pessoa) · O Tempo (link omitido: URL contém nome de pessoa) · Terra — reação do público (link omitido: URL contém nome de pessoa)

**SBT Prêmios:** [Site oficial](https://sbtpremios.com/) · [Condições gerais](https://demo.sbtpremios.com/condicoes-gerais) · [Diário Indústria & Comércio — expansão da Liderança](https://www.diarioinduscom.com.br/Noticias/884672/lideranca_capitalizacao_acelera_expansao_alem_da_tele_sena) · [SEGS — expansão além da Tele Sena](https://www.segs.com.br/seguros/448816-expansao-da-lideranca-capitalizacao-vai-alem-da-marca-tele-sena) · [Jornal Tribuna — lançamento](https://www.jornaltribuna.com.br/2025/12/sbt-lanca-plataforma-100-digital-de-premios-e-inaugura-nova-fase-de-inovacao-na-tv-brasileira) · [InvestNews — LiderCap](https://investnews.com.br/negocios/lidercap-futuro-tele-sena-mercado/) · [Liderança — produtos](https://www.lidercap.com.br/produtos.html) · Boatos.org — golpes com nome do SBT (link omitido: URL contém nome de pessoa)

**Regulatório e mercado:** [SUSEP — Circular 656/2022](https://www.legisweb.com.br/legislacao/?id=428900) · [SUSEP — Manual Técnico de Capitalização](https://www.gov.br/susep/pt-br/arquivos/arquivos-planos-e-produtos/manual-tecnico-de-capitalizacao.pdf/@@display-file/file) · [SUSEP — Perguntas frequentes capitalização](https://www.gov.br/susep/pt-br/copy_of_planos-e-produtos/capitalizacao/perguntas-frequentes-1/capitalizacao) · [Secretaria de Prêmios e Apostas — Ministério da Fazenda](https://www.gov.br/fazenda/pt-br/composicao/orgaos/secretaria-de-premios-e-apostas) · [gov.br — autorização de distribuição gratuita de prêmios](https://www.gov.br/pt-br/servicos/obter-autorizacao-para-atividades-de-distribuicao-gratuita-de-premios-a-titulo-de-propaganda-ou-de-captacao-de-poupanca-popular) · [Portaria SPA/MF nº 230/2026 — GT Promoções Comerciais](https://legismap.com.br/leis-e-normas/portaria-spa-mf-n-230-de-28-01-2026) · [SEGS — influenciadores adotam capitalização](https://www.segs.com.br/seguros/441887-influenciadores-adotam-capitalizacao-para-dar-mais-credibilidade-a-sorteios) · [SEGS — ApliCap R$ [valor]](https://www.segs.com.br/seguros/432177-aplicap-alcanca-mais-de-r-450-milhoes-em-faturamento-com-crescimento-expressivo-em-2025) · [JRS Portal — ApliCap R$ [valor] em prêmios](https://jrsportal.com.br/artigo-jrs/em-apenas-cinco-meses-aplicap-distribui-r-109-milhoes-em-premios/) · [ApliCap — Regularize seus sorteios](https://aplicap.com.br/regularize-seus-sorteios/) · [FenaCap/CNseg — mercado de capitalização](https://fenacap.org.br/noticias/capitalizacao-ultrapassa-26-bilhoes-pagos-a-seus-clientes-em-resgates-e-sorteios) · [Jusbrasil — títulos de capitalização no contexto legal](https://www.jusbrasil.com.br/artigos/titulos-de-capitalizacao-sorteios-e-premios-no-contexto-legal/405685092)
