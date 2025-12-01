"""
Constantes do Sistema EKKO 
Faixas ideais e configurações
"""

# Faixas ideais dos parâmetros de solo
SOIL_RANGES = {
    "ph": {"min": 6.0, "max": 7.0, "unit": "", "name": "pH do Solo"},
    "umidade": {"min": 40, "max": 70, "unit": "%", "name": "Umidade"},
    "temperatura": {"min": 20, "max": 30, "unit": "°C", "name": "Temperatura"},
    "salinidade": {"max": 600, "unit": " ppm", "name": "Salinidade"},
    "condutividade": {"max": 1.5, "unit": " dS/m", "name": "Condutividade"},
    "nitrogenio": {"min": 20, "max": 100, "unit": " mg/kg", "name": "Nitrogênio (N)"},
    "fosforo": {"min": 15, "max": 50, "unit": " mg/kg", "name": "Fósforo (P)"},
    "potassio": {"min": 100, "max": 250, "unit": " mg/kg", "name": "Potássio (K)"},
    "drenagem": {"min": 60, "max": 90, "unit": "%", "name": "Drenagem"},
    "aeracao": {"min": 10, "max": 30, "unit": "%", "name": "Aeração"},
    "compactacao": {"max": 2.0, "unit": " g/cm³", "name": "Compactação"},
    "atividadeMicrobiana": {"min": 50, "max": 100, "unit": " mg CO2/kg", "name": "Atividade Microbiana"}
}

# Status de análise
STATUS_IDEAL = "ideal"
STATUS_ATENCAO = "atencao"
STATUS_CRITICO = "critico"

# Mensagens padrão
MESSAGES = {
    "ph": {
        STATUS_IDEAL: "O pH está na faixa ideal (6.0-7.0), proporcionando máxima disponibilidade de nutrientes essenciais. As plantas conseguem absorver eficientemente nitrogênio, fósforo, potássio e micronutrientes. A atividade microbiana está otimizada, favorecendo a decomposição da matéria orgânica. Continue mantendo as práticas atuais de manejo para preservar este equilíbrio químico ideal.",
        STATUS_ATENCAO: "O pH está ligeiramente fora da faixa ideal, reduzindo a eficiência na absorção de nutrientes. Pode haver deficiências graduais que afetam a produtividade das culturas. A disponibilidade de micronutrientes como ferro, manganês e zinco pode estar comprometida. É recomendado monitorar frequentemente e considerar correções preventivas.",
        STATUS_CRITICO: "O pH está em níveis críticos que bloqueiam severamente a absorção de nutrientes pelas plantas. Esta condição causa deficiências graves, reduzindo drasticamente a produtividade e qualidade dos cultivos. A atividade microbiana benéfica está prejudicada, afetando a decomposição da matéria orgânica. Correção urgente através de calagem ou aplicação de enxofre é necessária."
    },
    "umidade": {
        STATUS_IDEAL: "A umidade está na faixa ideal (40-70%), garantindo disponibilidade adequada de água sem encharcamento. Esta condição favorece a absorção de nutrientes dissolvidos e mantém a estrutura física adequada. A respiração das raízes ocorre normalmente, permitindo crescimento vigoroso e saudável. O equilíbrio entre água e ar nos poros está otimizado para máxima produtividade.",
        STATUS_ATENCAO: "A umidade está fora da faixa ideal, podendo causar estresse hídrico moderado nas plantas. Níveis baixos reduzem absorção de nutrientes e causam murchamento, níveis altos prejudicam aeração. O crescimento pode ser afetado e a resistência a doenças reduzida. Ajustes na irrigação são recomendados para manter a saúde das plantas.",
        STATUS_CRITICO: "A umidade está em níveis críticos causando estresse hídrico severo e comprometendo a sobrevivência das plantas. Umidade baixa causa murchamento permanente, excesso causa apodrecimento das raízes e doenças. A absorção de nutrientes está severamente prejudicada. Correção imediata da irrigação é essencial para evitar perdas totais."
    },
    "temperatura": {
        STATUS_IDEAL: "A temperatura está na faixa ideal (20-30°C), proporcionando condições ótimas para crescimento radicular e atividade microbiana. Esta temperatura favorece germinação de sementes, desenvolvimento das raízes e absorção eficiente de nutrientes. Os processos bioquímicos no solo ocorrem em velocidade adequada, incluindo decomposição da matéria orgânica. A atividade enzimática das plantas está otimizada, resultando em crescimento vigoroso.",
        STATUS_ATENCAO: "A temperatura está fora da faixa ideal, podendo afetar o crescimento e desenvolvimento das plantas. Temperaturas baixas reduzem atividade metabólica e retardam germinação, altas causam estresse térmico. A absorção de água e nutrientes pode ser comprometida, afetando a produtividade. Medidas de proteção como cobertura morta ou sombreamento podem ser necessárias.",
        STATUS_CRITICO: "A temperatura está em níveis críticos causando estresse térmico severo e prejudicando drasticamente o desenvolvimento. Temperaturas extremas podem causar danos por congelamento ou desnaturar proteínas e enzimas essenciais. O crescimento radicular é severamente afetado, comprometendo absorção de água e nutrientes. Implementação urgente de medidas de controle térmico é necessária."
    },
    "salinidade": {
        STATUS_IDEAL: "A salinidade está em níveis baixos e seguros (≤600 ppm), não limitando o crescimento das plantas. Esta condição permite absorção normal de água pelas raízes sem competição osmótica prejudicial. A estrutura do solo mantém-se estável e a atividade microbiana não é afetada negativamente. A maioria das culturas pode se desenvolver plenamente, garantindo produtividade máxima.",
        STATUS_ATENCAO: "A salinidade está em níveis moderados que podem afetar plantas mais sensíveis ao sal. Algumas culturas podem apresentar redução no crescimento devido à competição osmótica na absorção de água. A estrutura do solo pode começar a se deteriorar, afetando a infiltração. Monitoramento frequente e práticas de lixiviação são recomendados.",
        STATUS_CRITICO: "A salinidade está em níveis tóxicos causando severo estresse salino e impedindo crescimento normal. A alta concentração de sais impede absorção de água, causando desidratação mesmo com solo úmido. A estrutura do solo está deteriorada, reduzindo infiltração e drenagem drasticamente. Apenas plantas halófitas sobrevivem. Lixiviação intensiva é urgentemente necessária."
    },
    "condutividade": {
        STATUS_IDEAL: "A condutividade elétrica está adequada (≤1.5 dS/m), indicando concentração balanceada de sais dissolvidos no solo. Esta condição permite absorção eficiente de água e nutrientes sem interferência osmótica. A disponibilidade de nutrientes essenciais está otimizada e a estrutura física mantém-se estável. A maioria das culturas agrícolas pode se desenvolver plenamente com alta produtividade.",
        STATUS_ATENCAO: "A condutividade está moderadamente elevada, indicando início de acúmulo salino que afeta culturas sensíveis. Algumas plantas podem apresentar sintomas de estresse osmótico, com redução na absorção de água. A produtividade pode começar a declinar e a qualidade dos produtos ser afetada. Irrigação com água de melhor qualidade e melhoria da drenagem são recomendadas.",
        STATUS_CRITICO: "A condutividade está em níveis críticos indicando solo salino e causando severo estresse osmótico. A alta concentração de sais impede absorção normal de água, causando sintomas similares à seca. A estrutura do solo está comprometida, reduzindo permeabilidade e aeração. Apenas culturas muito tolerantes sobrevivem. Lixiviação intensiva e correção urgente da drenagem são essenciais."
    },
    "drenagem": {
        STATUS_IDEAL: "A drenagem está funcionando adequadamente (60-90%), permitindo remoção eficiente do excesso de água sem encharcamento. Esta condição mantém equilíbrio ideal entre água e ar nos poros, favorecendo respiração das raízes. A infiltração de água da chuva e irrigação ocorre normalmente, evitando erosão superficial. O risco de doenças radiculares está minimizado, proporcionando ambiente saudável.",
        STATUS_ATENCAO: "A drenagem está comprometida, podendo causar acúmulo temporário de água que afeta aeração das raízes. Períodos prolongados de umidade excessiva podem favorecer desenvolvimento de doenças fúngicas e bacterianas. A absorção de nutrientes pode ser prejudicada devido à redução do oxigênio no solo. Melhorias no sistema de drenagem, como sulcos ou drenos, podem ser necessárias.",
        STATUS_CRITICO: "A drenagem está severamente deficiente, causando encharcamento frequente que prejudica drasticamente o sistema radicular. O excesso de água expulsa oxigênio dos poros, causando asfixia das raízes e favorecendo doenças. A absorção de nutrientes está severamente comprometida e pode ocorrer apodrecimento das raízes. Instalação urgente de sistema de drenagem adequado é essencial."
    },
    "aeracao": {
        STATUS_IDEAL: "A aeração está na faixa ideal (10-30%), garantindo suprimento adequado de oxigênio para respiração das raízes. Esta condição permite crescimento radicular vigoroso e absorção eficiente de nutrientes. Os processos de decomposição da matéria orgânica ocorrem adequadamente, liberando nutrientes para as plantas. A estrutura porosa do solo favorece tanto retenção de água quanto movimentação de gases.",
        STATUS_ATENCAO: "A aeração está reduzida, podendo limitar a respiração das raízes e afetar o crescimento das plantas. A atividade microbiana benéfica pode estar comprometida, reduzindo decomposição da matéria orgânica. Sintomas de deficiência de oxigênio podem aparecer, especialmente em períodos úmidos. Práticas como subsolagem leve ou adição de matéria orgânica podem melhorar a estrutura.",
        STATUS_CRITICO: "A aeração está severamente deficiente, causando asfixia das raízes e impedindo crescimento normal das plantas. A falta de oxigênio favorece processos anaeróbicos prejudiciais, produzindo compostos tóxicos como sulfeto de hidrogênio. A absorção de nutrientes está drasticamente reduzida e pode ocorrer morte das raízes. Descompactação urgente do solo através de subsolagem profunda é necessária."
    },
    "compactacao": {
        STATUS_IDEAL: "A compactação está em níveis adequados (≤2.0 g/cm³), mantendo estrutura porosa que favorece crescimento radicular. Esta densidade permite penetração fácil das raízes em todas as direções, maximizando exploração do solo. A porosidade adequada facilita trocas gasosas e atividade da fauna do solo. A estrutura física está otimizada para suportar o tráfego necessário sem prejudicar as plantas.",
        STATUS_ATENCAO: "A compactação está começando a afetar a estrutura do solo, podendo dificultar crescimento radicular em algumas áreas. A infiltração de água pode estar reduzida, aumentando risco de erosão superficial. Algumas raízes podem apresentar deformações ao tentar penetrar camadas mais densas. Práticas preventivas como evitar tráfego em solo úmido e rotação de culturas podem prevenir agravamento.",
        STATUS_CRITICO: "A compactação está em níveis críticos que impedem severamente crescimento radicular e infiltração de água. As raízes ficam confinadas às camadas superficiais, limitando drasticamente absorção de água e nutrientes. A infiltração reduzida aumenta significativamente o risco de erosão e perda de solo. A produtividade está severamente comprometida. Subsolagem profunda urgente é necessária."
    },
    "atividadeMicrobiana": {
        STATUS_IDEAL: "A atividade microbiana está em níveis saudáveis (≥50 mg CO2/kg), indicando solo biologicamente ativo com decomposição eficiente. Esta condição favorece a ciclagem de nutrientes, tornando-os disponíveis para as plantas de forma gradual. A diversidade microbiana contribui para supressão natural de patógenos e melhoria da estrutura do solo. O ecossistema do solo está equilibrado, promovendo crescimento saudável e resistência das plantas.",
        STATUS_ATENCAO: "A atividade microbiana está reduzida, indicando possível desequilíbrio no ecossistema do solo. A decomposição da matéria orgânica pode estar mais lenta, reduzindo disponibilidade gradual de nutrientes. A capacidade natural de supressão de doenças pode estar comprometida. Adição de matéria orgânica, como compostagem ou adubos orgânicos, pode ajudar a estimular a atividade microbiana.",
        STATUS_CRITICO: "A atividade microbiana está severamente reduzida, indicando solo biologicamente inativo ou desequilibrado. A decomposição da matéria orgânica está praticamente paralisada, impedindo ciclagem natural de nutrientes. O solo pode estar dominado por microrganismos patogênicos devido à falta de competição benéfica. Inoculação microbiana urgente e adição massiva de matéria orgânica são necessárias."
    },
    "nitrogenio": {
        STATUS_IDEAL: "O nitrogênio está em níveis adequados (20-100 mg/kg), fornecendo suporte essencial para crescimento vegetativo e síntese de proteínas. Esta concentração permite desenvolvimento vigoroso da parte aérea, folhas verdes e saudáveis. A disponibilidade balanceada evita tanto deficiências quanto excessos prejudiciais. As plantas podem expressar seu potencial genético máximo, resultando em alta produtividade.",
        STATUS_ATENCAO: "Os níveis de nitrogênio estão fora da faixa ideal, podendo afetar crescimento e desenvolvimento das plantas. Deficiência causa amarelecimento das folhas mais velhas e crescimento reduzido, excesso causa crescimento vegetativo excessivo. A eficiência de uso de outros nutrientes pode estar comprometida. Ajustes na adubação nitrogenada são recomendados para otimizar a nutrição das plantas.",
        STATUS_CRITICO: "Os níveis de nitrogênio estão críticos, causando severos problemas nutricionais nas plantas. Deficiência extrema resulta em clorose generalizada, nanismo e pode levar à morte das plantas. Excesso crítico causa crescimento vegetativo descontrolado, atraso na maturação e maior suscetibilidade a doenças. A produtividade está severamente comprometida. Correção urgente através de adubação balanceada é essencial."
    },
    "fosforo": {
        STATUS_IDEAL: "O fósforo está em níveis adequados (15-50 mg/kg), essencial para desenvolvimento radicular, floração e formação de frutos. Esta concentração favorece a transferência de energia celular através do ATP, promovendo crescimento vigoroso. O desenvolvimento do sistema radicular está otimizado, melhorando absorção de água e outros nutrientes. A qualidade dos frutos e sementes está maximizada, com maior teor de óleo e proteínas.",
        STATUS_ATENCAO: "Os níveis de fósforo estão fora da faixa ideal, podendo afetar especialmente desenvolvimento radicular e reprodutivo. Deficiência causa sistema radicular pouco desenvolvido, atraso na floração e redução na formação de frutos. Excesso pode interferir na absorção de micronutrientes como zinco e ferro. Ajustes na adubação fosfatada são necessários para otimizar o desenvolvimento das culturas.",
        STATUS_CRITICO: "Os níveis de fósforo estão críticos, comprometendo severamente o desenvolvimento das plantas. Deficiência extrema causa nanismo, sistema radicular muito pobre, folhas com coloração arroxeada e falha na reprodução. Excesso crítico pode causar deficiências induzidas de micronutrientes e desequilíbrios nutricionais. A produtividade está drasticamente reduzida. Correção urgente da adubação fosfatada é essencial."
    },
    "potassio": {
        STATUS_IDEAL: "O potássio está em níveis adequados (100-250 mg/kg), essencial para regulação hídrica, resistência a doenças e qualidade dos frutos. Esta concentração otimiza a abertura e fechamento dos estômatos, melhorando eficiência no uso da água. A resistência das plantas a estresses abióticos e bióticos está maximizada. A qualidade dos frutos é superior, com melhor sabor, coloração e capacidade de armazenamento.",
        STATUS_ATENCAO: "Os níveis de potássio estão fora da faixa ideal, podendo afetar regulação hídrica e resistência das plantas. Deficiência causa queima das bordas das folhas, maior suscetibilidade a doenças e frutos de qualidade inferior. Excesso pode interferir na absorção de cálcio e magnésio. A eficiência no uso da água pode estar comprometida. Ajustes na adubação potássica são recomendados.",
        STATUS_CRITICO: "Os níveis de potássio estão críticos, comprometendo severamente a regulação hídrica e resistência das plantas. Deficiência extrema causa necrose foliar generalizada, alta suscetibilidade a doenças e frutos de péssima qualidade. Excesso crítico pode causar deficiências induzidas de outros nutrientes essenciais. As plantas ficam extremamente vulneráveis a estresses. Correção urgente da adubação potássica é essencial."
    }
}