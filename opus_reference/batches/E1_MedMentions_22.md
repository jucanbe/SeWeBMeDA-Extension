# Task
You are a biomedical named entity recognition system for the MedMentions annotation scheme.
Identify every mention of the following entity types in the sentence:
- AnatomicalStructure: Specific parts of the body or anatomical regions (e.g., left ventricle, femoral artery).
- Bacterium: Bacterial organisms mentioned in the text (e.g., Escherichia coli, Staphylococcus aureus).
- BiologicFunction: Biological or physiological processes and functions (e.g., immune response, hemostasis).
- BiomedicalOccupationOrDiscipline: Biomedical roles or disciplines (e.g., cardiologist, oncology, radiology).
- BodySubstance: Substances originating from the body (e.g., blood, plasma, cerebrospinal fluid).
- BodySystem: Functional body systems (e.g., cardiovascular system, respiratory system).
- Chemical: Chemical substances and compounds (e.g., ethanol, sodium chloride).
- ClinicalAttribute: Clinical characteristics or attributes (e.g., severity, stage II, BMI).
- Eukaryote: Eukaryotic organisms such as parasites or fungi (e.g., Plasmodium falciparum, Candida albicans).
- Finding: Clinical findings or observations (e.g., fever, rash, wheezing, elevated creatinine).
- Food: Food items or nutrients (e.g., milk, gluten, high-fat diet).
- HealthCareActivity: Healthcare-related activities not primarily procedures (e.g., nursing care, follow-up visit).
- InjuryOrPoisoning: Injuries, poisonings, and related conditions (e.g., blunt trauma, acetaminophen overdose).
- IntellectualProduct: Guidelines, questionnaires, reports, and other intellectual artifacts (e.g., clinical guideline, survey form).
- MedicalDevice: Medical instruments or devices (e.g., pacemaker, ventilator, stent).
- Organization: Institutions or organizations (e.g., hospital, research institute, WHO).
- PopulationGroup: Groups of people or patient populations (e.g., elderly patients, pediatric population).
- ProfessionalOrOccupationalGroup: Professional groups or categories (e.g., nurses, surgeons, laboratory technicians).
- ResearchActivity: Research-related activities or study types (e.g., randomized controlled trial, cohort study).
- SpatialConcept: Spatial or locational concepts relevant to medicine (e.g., upper quadrant, distal segment).
- Virus: Viral agents (e.g., influenza virus, SARS-CoV-2).

Rules:
- Copy each entity text exactly as it appears in the sentence (same characters and spacing).
- Do not annotate text of any other type.
- If the same entity text occurs several times, listing it once is enough.
- For each entity give "confidence": your probability between 0.0 and 1.0 that the text and type are correct.
- Optionally give "normalized_form": the canonical name of the entity when you know it.
- Answer only with JSON of the form {"entities": [{"text": "...", "type": "...", "confidence": 0.0}]}; use {"entities": []} if there are none.
- Example answers shown in the conversation are reference annotations and therefore carry no confidence.

# Items
Each item below is independent. Answer every item.

## Item MedMentions:test:4001
Example input:
Sentence: The literature reviewed suggests probiotics usage could be beneficial for the maintenance of oral health , due to its ability to decrease the colony forming units ( CFU ) counts of the oral pathogens .

Example answer:
{"entities": [{"text": "literature", "type": "IntellectualProduct"}, {"text": "probiotics", "type": "Bacterium"}, {"text": "oral health", "type": "HealthCareActivity"}, {"text": "oral", "type": "SpatialConcept"}]}

Example input:
Sentence: These findings demonstrate that the composition of the small intestinal microbiome is affected differently in diet - and genetically - induced obesity , but both are associated with elevated intestinal inflammation and alterations of the Wnt pathway towards enhancing tumorigenesis .

Example answer:
{"entities": [{"text": "diet", "type": "Food"}, {"text": "genetically - induced", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "intestinal inflammation", "type": "Finding"}, {"text": "Wnt pathway", "type": "BiologicFunction"}, {"text": "tumorigenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Given the role of the gut microbiota in regulating host metabolism , we explored the effect of Roux - en - Y gastric bypass ( RYGB ) and sleeve gastrectomy ( SG ) on the modifications of gut microbiota with regard to the potential influence of food intake and / or weight loss and examined their links with host metabolism .

Example answer:
{"entities": [{"text": "metabolism", "type": "BiologicFunction"}, {"text": "Roux - en - Y gastric bypass", "type": "HealthCareActivity"}, {"text": "RYGB", "type": "HealthCareActivity"}, {"text": "sleeve gastrectomy", "type": "HealthCareActivity"}, {"text": "SG", "type": "HealthCareActivity"}, {"text": "food", "type": "Food"}]}

Example input:
Sentence: Our study using shotgun metagenomics highlights how single probiotic LGG may exert its beneficial effects and decrease polyp formation in mice by maintaining gut microbial functionality .

Example answer:
{"entities": [{"text": "shotgun metagenomics", "type": "ResearchActivity"}, {"text": "probiotic", "type": "Bacterium"}, {"text": "LGG", "type": "Bacterium"}, {"text": "polyp", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Recently , dysbiosis of the intestinal microbiota has emerged as a new candidate that may be linked to metabolic diseases .

Example answer:
{"entities": [{"text": "dysbiosis", "type": "BiologicFunction"}, {"text": "metabolic diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: This probiotic intervention targeting microbiota may be used in conjugation with other dietary supplements or drugs as part of prevention strategies for early - stage colon cancer , after further clinical validations in human .

Example answer:
{"entities": [{"text": "probiotic", "type": "Bacterium"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "dietary supplements", "type": "Food"}, {"text": "drugs", "type": "Chemical"}, {"text": "colon cancer", "type": "BiologicFunction"}, {"text": "validations", "type": "ResearchActivity"}, {"text": "human", "type": "Eukaryote"}]}

Example input:
Sentence: Many studies support the role of probiotics as a contributor to gastrointestinal health , and nowadays many authors are trying to prove its influence in oral health maintenance .

Example answer:
{"entities": [{"text": "probiotics", "type": "Bacterium"}, {"text": "gastrointestinal", "type": "SpatialConcept"}, {"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "oral health maintenance", "type": "HealthCareActivity"}]}

Example input:
Sentence: In a randomized triple - blind controlled clinical trial , 120 adults with impaired glucose tolerance based on the inclusion criteria will be selected by a simple random sampling method and will be randomly allocated to 6 months of 6 g / d probiotic , synbiotic or placebo .

Example answer:
{"entities": [{"text": "randomized triple - blind controlled clinical trial", "type": "ResearchActivity"}, {"text": "impaired glucose tolerance", "type": "BiologicFunction"}, {"text": "sampling method", "type": "IntellectualProduct"}, {"text": "probiotic", "type": "Bacterium"}, {"text": "synbiotic", "type": "Food"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: These findings stimulate deeper explorations of functions of the discriminate microbiota and the mechanisms linking postsurgical modulation of gut microbiota and improvements in insulin resistance .

Example answer:
{"entities": [{"text": "functions", "type": "BiologicFunction"}, {"text": "modulation", "type": "SpatialConcept"}, {"text": "insulin resistance", "type": "BiologicFunction"}]}

Example input:
Sentence: The effects of probiotic and synbiotic supplementation on metabolic syndrome indices in adults at risk of type 2 diabetes : study protocol for a randomized controlled trial The incidence of type 2 diabetes , cardiovascular diseases , and obesity has been rising dramatically ; however , their pathogenesis is particularly intriguing .

Example answer:
{"entities": [{"text": "probiotic", "type": "Bacterium"}, {"text": "synbiotic", "type": "Food"}, {"text": "supplementation", "type": "HealthCareActivity"}, {"text": "metabolic syndrome", "type": "BiologicFunction"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "study protocol", "type": "IntellectualProduct"}, {"text": "randomized controlled trial", "type": "ResearchActivity"}, {"text": "cardiovascular diseases", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "intriguing", "type": "BiologicFunction"}]}

Input:
Sentence: We hypothesize that selective modulation of the intestinal microbiota by probiotic or synbiotic supplementation may improve metabolic dysfunction and prevent diabetes in prediabetics .

## Item MedMentions:test:4148
Example input:
Sentence: We conducted 42 interviews with senior managers in commissioning organisations and senior managers in NHS and independent provider organisations ( acute and community services ) .

Example answer:
{"entities": [{"text": "senior managers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "commissioning", "type": "ProfessionalOrOccupationalGroup"}, {"text": "organisations", "type": "Organization"}, {"text": "NHS", "type": "HealthCareActivity"}, {"text": "independent provider organisations", "type": "Organization"}, {"text": "acute and community services", "type": "Organization"}]}

Example input:
Sentence: A total of 78 participants ( n = 24 residents , n = 18 relatives and n = 26 care professionals ) from 4 nursing homes in the Netherlands engaged in a qualitative study , in which photography was as a supportive tool for subsequent interviews and focus groups .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "care professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "nursing homes", "type": "Organization"}, {"text": "Netherlands", "type": "SpatialConcept"}, {"text": "qualitative study", "type": "ResearchActivity"}]}

Example input:
Sentence: Semi - structured interviews were conducted with a purposive sample of 15 supervisors from different veterinary subdisciplines , to elicit descriptions of excellent , weak and marginal students .

Example answer:
{"entities": [{"text": "purposive sample", "type": "ResearchActivity"}, {"text": "supervisors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "descriptions", "type": "IntellectualProduct"}, {"text": "marginal", "type": "SpatialConcept"}, {"text": "students", "type": "PopulationGroup"}]}

Example input:
Sentence: Methods Individual and small group semistructured interviews were undertaken with 29 leaders across Australia , reflecting a diverse cross - section of senior public health managers and program implementation staff from state and territory health departments , as well as academics , thought leaders and public health advocates .

Example answer:
{"entities": [{"text": "small group semistructured interviews", "type": "ResearchActivity"}, {"text": "Australia", "type": "SpatialConcept"}, {"text": "senior public health managers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "state and territory health departments", "type": "Organization"}, {"text": "academics", "type": "Organization"}, {"text": "public health advocates", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: qualitative semi - structured interview study , using thematic analysis and constant comparison . twenty - two pregnant women in midwife -led primary care , varying in socio - demographic characteristics , weeks of pregnancy and region of residence in the Netherlands , were interviewed between April and December 2013 .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "thematic analysis", "type": "ResearchActivity"}, {"text": "pregnant women", "type": "PopulationGroup"}, {"text": "midwife", "type": "ProfessionalOrOccupationalGroup"}, {"text": "primary care", "type": "HealthCareActivity"}, {"text": "pregnancy", "type": "BiologicFunction"}, {"text": "region", "type": "SpatialConcept"}, {"text": "residence", "type": "SpatialConcept"}, {"text": "Netherlands", "type": "SpatialConcept"}]}

Example input:
Sentence: Cross - sectional qualitative research design using semistructured interviews with 16 adults ( 8 pretransplant , 8 posttransplant ; from 4 UK centers ( n = 13 ) and 1 Canadian center ( n = 3 ) ) .

Example answer:
{"entities": [{"text": "research design", "type": "ResearchActivity"}, {"text": "UK", "type": "SpatialConcept"}, {"text": "centers", "type": "Organization"}, {"text": "Canadian", "type": "SpatialConcept"}, {"text": "center", "type": "Organization"}]}

Example input:
Sentence: Semi - structured interviews were conducted with 20 participants with ME / CFS and 21 participants with type 1 and 2 diabetes and analysed using thematic analysis .

Example answer:
{"entities": [{"text": "Semi - structured interviews", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "ME", "type": "BiologicFunction"}, {"text": "CFS", "type": "BiologicFunction"}, {"text": "type 1", "type": "BiologicFunction"}, {"text": "2 diabetes", "type": "BiologicFunction"}, {"text": "analysed", "type": "ResearchActivity"}, {"text": "thematic analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: A semi - structured diagnostic interview ( conducted with primary caregivers ) was used to assess for child suicidal thoughts and behaviors and psychiatric disorders .

Example answer:
{"entities": [{"text": "caregivers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "suicidal thoughts", "type": "Finding"}, {"text": "behaviors", "type": "Finding"}, {"text": "psychiatric disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: Method Semi - structured focus groups and individual interviews were held with low - literate participants ( n = 45 ) .

Example answer:
{"entities": [{"text": "individual", "type": "PopulationGroup"}, {"text": "low - literate participants", "type": "PopulationGroup"}]}

Example input:
Sentence: Fifty - two semi - structured interviews were conducted with patients and clinicians in all ten , adult and paediatric , Scottish renal units .

Example answer:
{"entities": [{"text": "clinicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Scottish", "type": "SpatialConcept"}, {"text": "renal units", "type": "Organization"}]}

Input:
Sentence: Semi - structured interviews and focus groups were conducted with practice staff ( n = 11 ) and patients ( n = 15 ) from one primary care practice in North East England , United Kingdom .

## Item MedMentions:test:4140
Example input:
Sentence: Collectively , our findings suggest that cucurbitacin B protects against cardiac hypertrophy through increasing the autophagy level in cardiomyocytes , which is associated with the inhibition of Akt / mTOR / FoxO3a signal axis .

Example answer:
{"entities": [{"text": "cucurbitacin B", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "cardiomyocytes", "type": "AnatomicalStructure"}, {"text": "inhibition", "type": "BiologicFunction"}, {"text": "Akt", "type": "Chemical"}, {"text": "mTOR", "type": "Chemical"}, {"text": "FoxO3a", "type": "Chemical"}, {"text": "signal axis", "type": "BiologicFunction"}]}

Example input:
Sentence: Mice were subcutaneously injected with nPbHsp60 or rPbHsp60 emulsified in complete 's Freund Adjuvant ( CFA ) at three weeks after intravenous injection of P .

Example answer:
{"entities": [{"text": "Mice", "type": "Eukaryote"}, {"text": "nPbHsp60", "type": "Chemical"}, {"text": "rPbHsp60", "type": "Chemical"}, {"text": "emulsified", "type": "BiologicFunction"}, {"text": "complete 's Freund Adjuvant", "type": "Chemical"}, {"text": "CFA", "type": "Chemical"}, {"text": "P .", "type": "Eukaryote"}]}

Example input:
Sentence: Moreover , the levels of T cell receptor excision circles ( TRECs ) were significantly higher in the mice treated with GRL prior to the conditioning regimen than in the control mice at 28 days after BMT .

Example answer:
{"entities": [{"text": "T cell receptor excision circles", "type": "Chemical"}, {"text": "TRECs", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "GRL", "type": "Chemical"}, {"text": "conditioning regimen", "type": "HealthCareActivity"}, {"text": "BMT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Male C57BL / 6J wildtype mice were subjected to 6 - weeks of voluntary wheel running or normal cage activities with or without simvastatin treatment ( 20 mg / kg / d , n = 7 - 8 per group ) .

Example answer:
{"entities": [{"text": "C57BL / 6J wildtype mice", "type": "Eukaryote"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The Cucurbitacin B -mediated mitigated cardiac hypertrophy was attributable to the increasing level of autophagy , which was associated with the blockade of Akt / mTOR / FoxO3a signal pathway , validated by SC79 , MK2206 , and 3 - MA , the Akt agonist , inhibitor and autophagy inhibitor in vitro .

Example answer:
{"entities": [{"text": "Cucurbitacin B", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "Akt", "type": "Chemical"}, {"text": "mTOR", "type": "Chemical"}, {"text": "FoxO3a", "type": "Chemical"}, {"text": "signal pathway", "type": "BiologicFunction"}, {"text": "SC79", "type": "Chemical"}, {"text": "MK2206", "type": "Chemical"}, {"text": "3 - MA", "type": "Chemical"}, {"text": "agonist", "type": "Chemical"}, {"text": "inhibitor", "type": "Chemical"}]}

Example input:
Sentence: Methods : U87MG tumor mice were treated via intragastric injections of sunitinib ( 80 mg / kg ) or vehicle for 7 consecutive days .

Example answer:
{"entities": [{"text": "U87MG tumor", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "intragastric", "type": "SpatialConcept"}, {"text": "injections", "type": "HealthCareActivity"}, {"text": "sunitinib", "type": "Chemical"}, {"text": "vehicle", "type": "Chemical"}]}

Example input:
Sentence: Atorvastatin ( 80mg / kg / day , oral gavage , 4 weeks ) or its vehicle was administered to male control or streptozotocin ( STZ ) - induced diabetic rats .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "Chemical"}, {"text": "vehicle", "type": "Chemical"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "STZ", "type": "Chemical"}, {"text": "diabetic", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: Rats with developing type II collagen - induced arthritis ( CIA ) were treated once daily by oral gavage on study days -14 to 17 with vehicle or NEM ( 52 mg / kg body weight ) .

Example answer:
{"entities": [{"text": "Rats", "type": "Eukaryote"}, {"text": "type II collagen - induced arthritis", "type": "BiologicFunction"}, {"text": "CIA", "type": "BiologicFunction"}, {"text": "vehicle", "type": "Chemical"}, {"text": "NEM", "type": "Chemical"}]}

Example input:
Sentence: In order to gain further insight into early gene and pathway changes leading to cancer , we exposed female Wistar Han rats to TBBPA at 0 , 25 , 250 , or 1000mg / kg ( oral gavage in corn oil , 5× / week ) for 13 weeks .

Example answer:
{"entities": [{"text": "gene", "type": "AnatomicalStructure"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "Wistar Han rats", "type": "Eukaryote"}, {"text": "TBBPA", "type": "Chemical"}, {"text": "corn oil", "type": "Chemical"}]}

Example input:
Sentence: After 4 weeks of AB , cucurbitacin B demonstrated a strong anti - hypertrophy and -fibrosis ability as evidenced by decreased of heart weight , myocardial cell cross - sectional area and interstitial fibrosis , ameliorated of systolic and diastolic abnormalities , normalized in gene expression of hypertrophic and fibrotic markers , reserved microvascular density in pressure overload induced hypertrophic mice .

Example answer:
{"entities": [{"text": "AB", "type": "HealthCareActivity"}, {"text": "cucurbitacin B", "type": "Chemical"}, {"text": "anti - hypertrophy", "type": "Finding"}, {"text": "-fibrosis", "type": "Finding"}, {"text": "heart", "type": "AnatomicalStructure"}, {"text": "myocardial cell", "type": "AnatomicalStructure"}, {"text": "interstitial fibrosis", "type": "BiologicFunction"}, {"text": "diastolic", "type": "ClinicalAttribute"}, {"text": "abnormalities", "type": "Finding"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "hypertrophic", "type": "BiologicFunction"}, {"text": "markers", "type": "ClinicalAttribute"}, {"text": "mice", "type": "Eukaryote"}]}

Input:
Sentence: After 1 week of surgery , mice were receive cucurbitacin B treatment ( Gavage , 0 . 2 mg / kg body weight /2 day ) .

## Item MedMentions:test:4400
Example input:
Sentence: Study Design .

Example answer:
{"entities": []}

Example input:
Sentence: Case presentation .

Example answer:
{"entities": []}

Example input:
Sentence: Treatment Study .

Example answer:
{"entities": [{"text": "Treatment Study", "type": "ResearchActivity"}]}

Example input:
Sentence: Study Design Retrospective case series with chart review .

Example answer:
{"entities": [{"text": "Retrospective", "type": "ResearchActivity"}]}

Example input:
Sentence: This investigation was a cross - sectional , case - control , functional magnetic resonance imaging study at an academic medical center .

Example answer:
{"entities": [{"text": "investigation", "type": "HealthCareActivity"}, {"text": "cross - sectional", "type": "ResearchActivity"}, {"text": "case - control", "type": "HealthCareActivity"}, {"text": "functional magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "academic medical center", "type": "Organization"}]}

Example input:
Sentence: Level III , retrospective case - control study .

Example answer:
{"entities": [{"text": "Level III , retrospective", "type": "ResearchActivity"}, {"text": "case - control study", "type": "ResearchActivity"}]}

Example input:
Sentence: The PHRs that were reviewed were unable to effectively manage the case study information .

Example answer:
{"entities": [{"text": "PHRs", "type": "IntellectualProduct"}, {"text": "case study", "type": "IntellectualProduct"}]}

Example input:
Sentence: Retrospective case reports and experimental study .

Example answer:
{"entities": [{"text": "case reports", "type": "IntellectualProduct"}, {"text": "experimental study", "type": "ResearchActivity"}]}

Example input:
Sentence: A prospective case - control study in a tertiary referral university hospital .

Example answer:
{"entities": [{"text": "prospective case - control study", "type": "ResearchActivity"}, {"text": "tertiary referral university hospital", "type": "Organization"}]}

Example input:
Sentence: This qualitative research used a case study approach , with in - depth interviewing and email exchange providing the data for the study .

Example answer:
{"entities": [{"text": "qualitative research", "type": "ResearchActivity"}, {"text": "case study", "type": "IntellectualProduct"}, {"text": "email", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}]}

Input:
Sentence: Case Study .

## Item MedMentions:test:3702
Example input:
Sentence: Mep1A , but not meprin β , was overexpressed in a series of 242 human HCC ( 2 . 04 fold , p < 0 . 0001 ) , and a high expression correlated with a poor prognosis .

Example answer:
{"entities": [{"text": "Mep1A", "type": "Chemical"}, {"text": "meprin β", "type": "Chemical"}, {"text": "overexpressed", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "poor prognosis", "type": "Finding"}]}

Example input:
Sentence: TRPM2 -mediated Ca ( 2 + ) signaling has been implicated in the aggravation of inflammatory diseases .

Example answer:
{"entities": [{"text": "TRPM2", "type": "Chemical"}, {"text": "Ca ( 2 + ) signaling", "type": "BiologicFunction"}, {"text": "aggravation", "type": "Finding"}, {"text": "inflammatory diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Our data indicate that , in response to various inflammatory stimuli , MSCs secrete high amounts of inactive chemerin , which can then be activated by inflammation - induced tissue proteases .

Example answer:
{"entities": [{"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "secrete", "type": "BiologicFunction"}, {"text": "chemerin", "type": "Chemical"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "proteases", "type": "Chemical"}]}

Example input:
Sentence: NF - κB Links TLR2 and PAR1 to Soluble Immunomodulator Factor Secretion in Human Platelets The primary toll - like receptor ( TLR ) - mediated immune cell response pathway common for all TLRs is MyD88 -dependent activation of NF - κB , a seminal transcription factor for many chemokines and cytokines .

Example answer:
{"entities": [{"text": "NF - κB", "type": "Chemical"}, {"text": "TLR2", "type": "Chemical"}, {"text": "PAR1", "type": "Chemical"}, {"text": "Immunomodulator Factor", "type": "Chemical"}, {"text": "Secretion", "type": "BiologicFunction"}, {"text": "Human", "type": "Eukaryote"}, {"text": "Platelets", "type": "AnatomicalStructure"}, {"text": "toll - like receptor", "type": "Chemical"}, {"text": "TLR", "type": "Chemical"}, {"text": "immune cell response pathway", "type": "BiologicFunction"}, {"text": "TLRs", "type": "Chemical"}, {"text": "MyD88", "type": "Chemical"}, {"text": "seminal", "type": "AnatomicalStructure"}, {"text": "transcription factor", "type": "Chemical"}, {"text": "chemokines", "type": "Chemical"}, {"text": "cytokines", "type": "Chemical"}]}

Example input:
Sentence: MCs also expressed mRNAs for FPRs that were functionally active ; indeed , uPA and a soluble peptide ( uPAR84 - 95 ) , containing the SRSRY chemotactic sequence of uPAR and able to interact with FPRs , were able to induce MCs chemotaxis .

Example answer:
{"entities": [{"text": "MCs", "type": "AnatomicalStructure"}, {"text": "mRNAs", "type": "Chemical"}, {"text": "FPRs", "type": "Chemical"}, {"text": "uPA", "type": "Chemical"}, {"text": "soluble peptide", "type": "Chemical"}, {"text": "uPAR84 - 95", "type": "Chemical"}, {"text": "SRSRY chemotactic sequence", "type": "SpatialConcept"}, {"text": "uPAR", "type": "Chemical"}, {"text": "chemotaxis", "type": "BiologicFunction"}]}

Example input:
Sentence: The sIL - 6R is generated proteolytically from its membrane bound form and A Disintegrin And Metalloprotease ( ADAM ) 10 and 17 were shown to perform ectodomain shedding of the receptor in vitro and in vivo .

Example answer:
{"entities": [{"text": "sIL - 6R", "type": "Chemical"}, {"text": "proteolytically", "type": "BiologicFunction"}, {"text": "A Disintegrin And Metalloprotease ( ADAM ) 10", "type": "Chemical"}, {"text": "17", "type": "Chemical"}, {"text": "ectodomain shedding", "type": "BiologicFunction"}, {"text": "receptor", "type": "Chemical"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: Meprin alpha ( Mep1A ) is a secreted metalloproteinase with many substrates relevant to cancer invasion .

Example answer:
{"entities": [{"text": "Meprin alpha", "type": "Chemical"}, {"text": "Mep1A", "type": "Chemical"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "metalloproteinase", "type": "Chemical"}, {"text": "cancer invasion", "type": "Finding"}]}

Example input:
Sentence: Metalloproteinase meprin α regulates migration and invasion of human hepatocarcinoma cells and is a mediator of the oncoprotein Reptin Hepatocellular carcinoma is associated with a high rate of intra - hepatic invasion that carries a poor prognosis .

Example answer:
{"entities": [{"text": "Metalloproteinase", "type": "Chemical"}, {"text": "meprin α", "type": "Chemical"}, {"text": "migration", "type": "BiologicFunction"}, {"text": "invasion", "type": "Finding"}, {"text": "human", "type": "Eukaryote"}, {"text": "hepatocarcinoma", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "oncoprotein", "type": "Chemical"}, {"text": "Reptin", "type": "Chemical"}, {"text": "Hepatocellular carcinoma", "type": "BiologicFunction"}, {"text": "intra - hepatic", "type": "SpatialConcept"}, {"text": "poor prognosis", "type": "Finding"}]}

Example input:
Sentence: Interestingly , meprin β can be shed from the cell surface by ADAM10 / 17 and the observation that soluble meprin β is not capable of shedding the IL - 6R suggests a regulatory mechanism towards trans - signaling .

Example answer:
{"entities": [{"text": "meprin β", "type": "Chemical"}, {"text": "cell surface", "type": "AnatomicalStructure"}, {"text": "ADAM10", "type": "Chemical"}, {"text": "17", "type": "Chemical"}, {"text": "shedding", "type": "BiologicFunction"}, {"text": "IL - 6R", "type": "Chemical"}, {"text": "trans - signaling", "type": "BiologicFunction"}]}

Example input:
Sentence: Additionally , we observed a significant negative correlation of meprin β expression and IL - 6R levels on human granulocytes , providing evidence for in vivo function of this proteolytic interaction .

Example answer:
{"entities": [{"text": "negative", "type": "Finding"}, {"text": "meprin β", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "IL - 6R", "type": "Chemical"}, {"text": "human granulocytes", "type": "BodySubstance"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "proteolytic", "type": "BiologicFunction"}]}

Input:
Sentence: Meprin Metalloproteases Generate Biologically Active Soluble Interleukin - 6 Receptor to Induce Trans - Signaling Soluble Interleukin - 6 receptor ( sIL - 6R ) mediated trans - signaling is an important pro - inflammatory stimulus associated with pathological conditions , such as arthritis , neurodegeneration and inflammatory bowel disease .

## Item MedMentions:test:4280
Example input:
Sentence: A recent study demonstrated that a high level of N - terminal pro - B - type natriuretic peptide ( NT - proBNP ) may be associated with PEW in those patients .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "N - terminal pro - B - type natriuretic peptide", "type": "Chemical"}, {"text": "NT - proBNP", "type": "Chemical"}, {"text": "PEW", "type": "BiologicFunction"}]}

Example input:
Sentence: Levels of copeptin and plasma N - terminal probrain natriuretic peptide ( NT - proBNP ) were evaluated prospectively in 24 obstructive HCM patients , 36 nonobstructive HCM patients , and 36 age - and sex - matched control subjects .

Example answer:
{"entities": [{"text": "copeptin", "type": "Chemical"}, {"text": "HCM", "type": "BiologicFunction"}]}

Example input:
Sentence: Improvement in Exercise Capacity by Exercise Training Associated With Favorable Clinical Outcomes in Advanced Heart Failure With High B - Type Natriuretic Peptide Level The efficacy of exercise training ( ET ) programs and its relationship with long - term clinical outcomes in advanced heart failure ( HF ) patients with high levels of B - type natriuretic peptide ( BNP ) remain uncertain .

Example answer:
{"entities": [{"text": "Favorable Clinical Outcomes", "type": "Finding"}, {"text": "Advanced Heart Failure", "type": "BiologicFunction"}, {"text": "B - Type Natriuretic Peptide", "type": "Chemical"}, {"text": "advanced heart failure", "type": "BiologicFunction"}, {"text": "HF", "type": "BiologicFunction"}, {"text": "B - type natriuretic peptide", "type": "Chemical"}, {"text": "BNP", "type": "Chemical"}]}

Example input:
Sentence: Copeptin and NT - proBNP levels were significantly higher in patients with obstructive HCM , and higher levels were associated with worse outcome .

Example answer:
{"entities": [{"text": "Copeptin", "type": "Chemical"}, {"text": "HCM", "type": "BiologicFunction"}]}

Example input:
Sentence: High NT - proBNP was associated with cardiac dysfunction , increased levels of hsCRP and IL - 6 , and serially decreased levels of the indexes for muscle mass .

Example answer:
{"entities": [{"text": "NT - proBNP", "type": "Chemical"}, {"text": "cardiac dysfunction", "type": "Finding"}, {"text": "increased levels of hsCRP", "type": "Finding"}, {"text": "IL - 6", "type": "Finding"}, {"text": "indexes", "type": "IntellectualProduct"}, {"text": "muscle mass", "type": "Finding"}]}

Example input:
Sentence: During a median follow - up of 46 months , patients in the upper tertile of changes in peak V̇O2 ( ≥13 . 0 % ) , compared with those in the lower tertile ( < 1 . 0 % ) , had lower rates of the composite of all - cause death or HF hospitalization ( 37 . 9 % vs .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "peak V̇O2", "type": "Finding"}, {"text": "death", "type": "BiologicFunction"}, {"text": "HF", "type": "BiologicFunction"}, {"text": "hospitalization", "type": "HealthCareActivity"}]}

Example input:
Sentence: 3±16 . 2 % during the ET program , and changes in peak V̇O2 inversely correlated with changes in BNP ( R = - 0 . 453 , P < 0 . 0001 ) and changes in ventilatory efficiency ( V̇E / V̇CO2 slope ) ( R = - 0 . 439 , P < 0 . 0001 ) .

Example answer:
{"entities": [{"text": "peak V̇O2", "type": "Finding"}, {"text": "BNP", "type": "Chemical"}, {"text": "V̇CO2", "type": "Finding"}]}

Example input:
Sentence: Patients showed a lower peak oxygen consumption ( VO2 /kg ) than controls ( P < 0 . 001 ) , as well as ventilatory inefficiency ( P = 0 . 024 ) .

Example answer:
{"entities": [{"text": "oxygen consumption", "type": "ClinicalAttribute"}, {"text": "VO2", "type": "ClinicalAttribute"}, {"text": "ventilatory inefficiency", "type": "Finding"}]}

Example input:
Sentence: Patients with BNP ≥200 pg / mL ( High - BNP , n = 170 ) had more advanced HF characteristics , including lower EF ( 25 .

Example answer:
{"entities": [{"text": "BNP", "type": "Chemical"}, {"text": "HF", "type": "BiologicFunction"}, {"text": "lower EF", "type": "Finding"}]}

Example input:
Sentence: Even among advanced HF p atient s with high BNP level , an ET program significantly improved exercise capacity , and a greater improvement in exercise capacity was associated with greater decreases in BNP level and V̇E / V̇CO2 slope and more favorable long - term clinical outcomes .

Example answer:
{"entities": [{"text": "HF", "type": "BiologicFunction"}, {"text": "BNP", "type": "Chemical"}, {"text": "improved", "type": "Finding"}, {"text": "decreases", "type": "Finding"}, {"text": "V̇CO2", "type": "Finding"}, {"text": "favorable long - term clinical outcomes", "type": "Finding"}]}

Input:
Sentence: In the High - BNP patients , peak oxygen uptake ( V̇O2 ) was significantly increased by 8 .

## Item MedMentions:test:3910
Example input:
Sentence: This study introduces the concept of retinal telephotocoagulation for diabetic macular edema , and demonstrates the feasibility and safety of using telemedicine to perform navigated retinal laser treatments regardless of geographical distance .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "retinal telephotocoagulation", "type": "HealthCareActivity"}, {"text": "diabetic macular edema", "type": "BiologicFunction"}, {"text": "safety", "type": "HealthCareActivity"}, {"text": "telemedicine", "type": "HealthCareActivity"}, {"text": "navigated retinal laser treatments", "type": "HealthCareActivity"}, {"text": "geographical", "type": "SpatialConcept"}]}

Example input:
Sentence: We propose that diabetes - induced activation of acid sphingomyelinase ( ASM ) plays essential role in retinal endothelial and CD34 ( + ) circulating angiogenic cell ( CAC ) dysfunction in diabetes .

Example answer:
{"entities": [{"text": "diabetes", "type": "BiologicFunction"}, {"text": "acid sphingomyelinase", "type": "Chemical"}, {"text": "ASM", "type": "Chemical"}, {"text": "retinal", "type": "AnatomicalStructure"}, {"text": "endothelial", "type": "AnatomicalStructure"}, {"text": "CD34 ( + ) circulating angiogenic cell", "type": "AnatomicalStructure"}, {"text": "CAC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Well , I Wouldn ' t be Any Worse Off , Would I , Than I am Now ? A Qualitative Study of Decision - Making , Hopes , and Realities of Adults With Type 1 Diabetes Undergoing Islet Cell Transplantation For selected individuals with type 1 diabetes , pancreatic islet transplantation ( IT ) prevents recurrent severe hypoglycemia and optimizes glycemia , although ongoing systemic immunosuppression is needed .

Example answer:
{"entities": [{"text": "Qualitative Study", "type": "ResearchActivity"}, {"text": "Decision - Making", "type": "BiologicFunction"}, {"text": "Hopes", "type": "BiologicFunction"}, {"text": "Type 1 Diabetes", "type": "BiologicFunction"}, {"text": "Islet Cell Transplantation", "type": "HealthCareActivity"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "type 1 diabetes", "type": "BiologicFunction"}, {"text": "pancreatic islet transplantation", "type": "HealthCareActivity"}, {"text": "IT", "type": "HealthCareActivity"}, {"text": "hypoglycemia", "type": "BiologicFunction"}, {"text": "optimizes glycemia", "type": "HealthCareActivity"}, {"text": "systemic immunosuppression", "type": "HealthCareActivity"}]}

Example input:
Sentence: Sixteen eyes of ten subjects with diabetic macular edema underwent navigated focal laser photocoagulation using a novel teleretinal treatment plan .

Example answer:
{"entities": [{"text": "eyes", "type": "AnatomicalStructure"}, {"text": "subjects", "type": "PopulationGroup"}, {"text": "diabetic macular edema", "type": "BiologicFunction"}, {"text": "navigated focal laser photocoagulation", "type": "HealthCareActivity"}, {"text": "teleretinal treatment plan", "type": "IntellectualProduct"}]}

Example input:
Sentence: A Revised Approach for the Detection of Sight - Threatening Diabetic Macular Edema Diabetic macular edema is one of the leading causes of vision loss among working - age adults in the United States .

Example answer:
{"entities": [{"text": "Diabetic macular edema", "type": "BiologicFunction"}, {"text": "vision loss", "type": "BiologicFunction"}, {"text": "United States", "type": "SpatialConcept"}]}

Example input:
Sentence: Diabetic retinopathy and progression following treatment after pancreas transplantation were measured .

Example answer:
{"entities": [{"text": "Diabetic retinopathy", "type": "BiologicFunction"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "pancreas transplantation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Five cases progressed to proliferative diabetic retinopathy and received panretinal photocoagulation .

Example answer:
{"entities": [{"text": "progressed", "type": "BiologicFunction"}, {"text": "proliferative diabetic retinopathy", "type": "BiologicFunction"}, {"text": "panretinal photocoagulation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Acute macular edema after pancreas transplantation has a favorable treatment outcome despite rapid progression to proliferative diabetic retinopathy .

Example answer:
{"entities": [{"text": "macular edema", "type": "BiologicFunction"}, {"text": "pancreas transplantation", "type": "HealthCareActivity"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "proliferative diabetic retinopathy", "type": "BiologicFunction"}]}

Example input:
Sentence: The patients had no or mild pretransplant diabetic retinopathy and developed acute symptomatic macular edema and peripapillary soft exudate in both eyes after pancreas transplantation .

Example answer:
{"entities": [{"text": "diabetic retinopathy", "type": "BiologicFunction"}, {"text": "macular edema", "type": "BiologicFunction"}, {"text": "peripapillary", "type": "SpatialConcept"}, {"text": "exudate", "type": "BodySubstance"}, {"text": "both eyes", "type": "AnatomicalStructure"}, {"text": "pancreas transplantation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Acute macular edema and peripapillary soft exudate after pancreas transplantation with accelerated progression of diabetic retinopathy The effect of pancreas transplantation on diabetic retinopathy remains inconclusive .

Example answer:
{"entities": [{"text": "macular edema", "type": "BiologicFunction"}, {"text": "peripapillary", "type": "SpatialConcept"}, {"text": "exudate", "type": "BodySubstance"}, {"text": "pancreas transplantation", "type": "HealthCareActivity"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "diabetic retinopathy", "type": "BiologicFunction"}]}

Input:
Sentence: Herein , we report six patients with type 1 diabetes mellitus ( DM ) who underwent pancreas transplantation and developed acute macular edema and peripapillary soft exudate with rapid progression to proliferative diabetic retinopathy .

## Item MedMentions:test:4211
Example input:
Sentence: During such a process , hematogenous metastasis is an indispensable approach for the dissemination of cancer cells .

Example answer:
{"entities": [{"text": "hematogenous metastasis", "type": "BiologicFunction"}, {"text": "cancer cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The latter were metastasis in 70 patients ( 50 % ) and a primary lung cancer in 36 patients ( 25 . 7 % ) .

Example answer:
{"entities": [{"text": "metastasis", "type": "BiologicFunction"}, {"text": "lung cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: The lungs were dissected and blind histopathological evaluation was performed .

Example answer:
{"entities": [{"text": "lungs", "type": "AnatomicalStructure"}, {"text": "evaluation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Liver , lung , and lymph nodes were the most frequent sites of metastases ; one patient had brain metastasis .

Example answer:
{"entities": [{"text": "Liver", "type": "AnatomicalStructure"}, {"text": "lung", "type": "AnatomicalStructure"}, {"text": "lymph nodes", "type": "AnatomicalStructure"}, {"text": "metastases", "type": "BiologicFunction"}, {"text": "brain metastasis", "type": "BiologicFunction"}]}

Example input:
Sentence: All 3 were associated with an aggressive clinical course , including multisite bony metastases in 1 patient , progressive peritoneal disease after chemotherapy in another , and metastases to the lung and skin in the last patient .

Example answer:
{"entities": [{"text": "aggressive clinical course", "type": "Finding"}, {"text": "bony metastases", "type": "BiologicFunction"}, {"text": "peritoneal disease", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "metastases", "type": "BiologicFunction"}, {"text": "lung", "type": "AnatomicalStructure"}, {"text": "skin", "type": "BodySystem"}]}

Example input:
Sentence: An algorithm was used to categorize nodules found in the first screening year of the National Lung Screening Trial as malignant or nonmalignant .

Example answer:
{"entities": [{"text": "algorithm", "type": "IntellectualProduct"}, {"text": "nodules", "type": "Finding"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "malignant", "type": "BiologicFunction"}, {"text": "nonmalignant", "type": "BiologicFunction"}]}

Example input:
Sentence: Respondents were most willing to accept minimally invasive operations for treatment of their hypothetical lung cancer , followed by stereotactic body radiation therapy ( SBRT ) ; they were least willing to accept thoracotomy .

Example answer:
{"entities": [{"text": "Respondents", "type": "PopulationGroup"}, {"text": "invasive operations", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "stereotactic body radiation therapy", "type": "HealthCareActivity"}, {"text": "SBRT", "type": "HealthCareActivity"}, {"text": "thoracotomy", "type": "HealthCareActivity"}]}

Example input:
Sentence: The most commonly described sites of distant metastasis are the bones , lungs , and liver , whereas axillary metastasis is seldom reported .

Example answer:
{"entities": [{"text": "sites", "type": "SpatialConcept"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "bones", "type": "AnatomicalStructure"}, {"text": "lungs", "type": "AnatomicalStructure"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "axillary metastasis", "type": "BiologicFunction"}]}

Example input:
Sentence: Survey respondents preferred minimally invasive operations over SBRT or thoracotomy for treatment of early - stage non - small cell lung cancer .

Example answer:
{"entities": [{"text": "Survey", "type": "IntellectualProduct"}, {"text": "respondents", "type": "PopulationGroup"}, {"text": "invasive operations", "type": "HealthCareActivity"}, {"text": "SBRT", "type": "HealthCareActivity"}, {"text": "thoracotomy", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "non - small cell lung cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: He underwent FDG PET / CT scan for response assessment and the images revealed multiple , intensely FDG avid , peripheral , lung nodules with feeding vessels , which were suspicious for pulmonary metastases .

Example answer:
{"entities": [{"text": "FDG", "type": "Chemical"}, {"text": "PET / CT scan", "type": "HealthCareActivity"}, {"text": "response", "type": "Finding"}, {"text": "images", "type": "IntellectualProduct"}, {"text": "avid", "type": "Chemical"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "lung nodules", "type": "Finding"}, {"text": "feeding vessels", "type": "AnatomicalStructure"}, {"text": "pulmonary metastases", "type": "BiologicFunction"}]}

Input:
Sentence: These lesions are often considered as pulmonary metastases and increasingly treated by non - surgical techniques without histological confirmation .

## Item MedMentions:test:3391
Example input:
Sentence: succinogenes in alginates resulted in higher sugar to succinic acid conversion yield ( 0 . 81g / g ) than the respective yield achieved ( 0 . 65g / g ) when DCM immobilized cultures were used .

Example answer:
{"entities": [{"text": "succinogenes", "type": "Bacterium"}, {"text": "alginates", "type": "Chemical"}, {"text": "sugar", "type": "Chemical"}, {"text": "succinic acid", "type": "Chemical"}, {"text": "immobilized", "type": "AnatomicalStructure"}, {"text": "cultures", "type": "HealthCareActivity"}]}

Example input:
Sentence: Long - chain n - 3 PUFA supplied by the usual diet decrease plasma stearoyl - CoA desaturase index in non - hypertriglyceridemic older adults at high vascular risk The activity of stearoyl - CoA desaturase - 1 ( SCD1 ) , the central enzyme in the synthesis of monounsaturated fatty acids ( MUFA ) , has been associated with de novo lipogenesis .

Example answer:
{"entities": [{"text": "Long - chain n - 3 PUFA", "type": "Chemical"}, {"text": "diet", "type": "Food"}, {"text": "plasma stearoyl - CoA desaturase", "type": "Chemical"}, {"text": "index", "type": "IntellectualProduct"}, {"text": "non - hypertriglyceridemic", "type": "Finding"}, {"text": "older adults", "type": "PopulationGroup"}, {"text": "vascular", "type": "AnatomicalStructure"}, {"text": "activity", "type": "BiologicFunction"}, {"text": "stearoyl - CoA desaturase - 1", "type": "Chemical"}, {"text": "SCD1", "type": "Chemical"}, {"text": "central enzyme", "type": "Chemical"}, {"text": "monounsaturated fatty acids", "type": "Chemical"}, {"text": "MUFA", "type": "Chemical"}, {"text": "lipogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: After the GO - Fe3O4 / SiO2 / AuNWs / L - Cys composites were applied to glycopeptide enrichment , 26 glycopeptides from a human IgG digest could be identified , with a detection limit as low as 10 fmol .

Example answer:
{"entities": [{"text": "GO", "type": "Chemical"}, {"text": "Fe3O4", "type": "Chemical"}, {"text": "SiO2", "type": "Chemical"}, {"text": "L - Cys", "type": "Chemical"}, {"text": "glycopeptide", "type": "Chemical"}, {"text": "glycopeptides", "type": "Chemical"}, {"text": "human IgG", "type": "Chemical"}]}

Example input:
Sentence: Gas chromatography / mass spectrometry ( GC / MS ) and gas chromatography isotope ratio mass spectrometry ( GC / IRMS ) were conducted on purified collagen and lipid extracts to assess isotopic responses to PLE .

Example answer:
{"entities": [{"text": "Gas chromatography / mass spectrometry", "type": "HealthCareActivity"}, {"text": "GC / MS", "type": "HealthCareActivity"}, {"text": "gas chromatography isotope ratio mass spectrometry", "type": "HealthCareActivity"}, {"text": "GC / IRMS", "type": "HealthCareActivity"}, {"text": "collagen", "type": "Chemical"}, {"text": "lipid", "type": "Chemical"}, {"text": "PLE", "type": "HealthCareActivity"}]}

Example input:
Sentence: The purpose of our study is to establish a rapid and reliable method to quantify ASA metabolites in biological matrices , especially for glucuronide metabolites whose standards are not commercially available .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "method", "type": "HealthCareActivity"}, {"text": "ASA", "type": "Chemical"}, {"text": "metabolites", "type": "Chemical"}, {"text": "biological matrices", "type": "BodySubstance"}, {"text": "glucuronide", "type": "Chemical"}]}

Example input:
Sentence: The study on drug loading , using salicylic acid ( SA ) as a model drug , was performed .

Example answer:
{"entities": [{"text": "study on drug loading", "type": "ResearchActivity"}, {"text": "salicylic acid", "type": "Chemical"}, {"text": "SA", "type": "Chemical"}, {"text": "model drug", "type": "Chemical"}]}

Example input:
Sentence: The excretion of other three metabolites ( GA , SA and SAPG ) however showed remarkable increases by 16 % , 6 % and 4 % , respectively .

Example answer:
{"entities": [{"text": "excretion", "type": "BiologicFunction"}, {"text": "metabolites", "type": "Chemical"}, {"text": "GA", "type": "Chemical"}, {"text": "SA", "type": "Chemical"}, {"text": "SAPG", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , we have developed a rapid and sensitive method to determine the five ASA metabolites ( SA , GA , SUA , SAPG and SUAPG ) in rat urine .

Example answer:
{"entities": [{"text": "method", "type": "HealthCareActivity"}, {"text": "ASA", "type": "Chemical"}, {"text": "metabolites", "type": "Chemical"}, {"text": "SA", "type": "Chemical"}, {"text": "GA", "type": "Chemical"}, {"text": "SUA", "type": "Chemical"}, {"text": "SAPG", "type": "Chemical"}, {"text": "SUAPG", "type": "Chemical"}, {"text": "rat", "type": "Eukaryote"}, {"text": "urine", "type": "BodySubstance"}]}

Example input:
Sentence: In addition , SUA and SUAPG were mainly excreted in the time period of 12 - 24 h , while GA was excreted in the earlier time periods ( 0 - 4 h and 4 - 8 h ) .

Example answer:
{"entities": [{"text": "SUA", "type": "Chemical"}, {"text": "SUAPG", "type": "Chemical"}, {"text": "excreted", "type": "BiologicFunction"}, {"text": "GA", "type": "Chemical"}]}

Example input:
Sentence: SUA and SUAPG were the major metabolites of ASA in rat urine 24 h after ASA administration , which accounted for 50 % ( SUA ) and 26 % ( SUAPG ) .

Example answer:
{"entities": [{"text": "SUA", "type": "Chemical"}, {"text": "SUAPG", "type": "Chemical"}, {"text": "metabolites", "type": "Chemical"}, {"text": "ASA", "type": "Chemical"}, {"text": "rat", "type": "Eukaryote"}, {"text": "urine", "type": "BodySubstance"}]}

Input:
Sentence: Salicylic acid ( SA ) , gentisic acid ( GA ) and salicyluric acid ( SUA ) were determined directly by UHPLC - MS / MS , while salicyl phenolic glucuronide ( SAPG ) and salicyluric acid phenolic glucuronide ( SUAPG ) were quantified indirectly by measuring the released SA and SUA from SAPG and SUAPG after β - glucuronidase digestion .

## Item MedMentions:test:4338
Example input:
Sentence: The level of NT - proBNP decreased the day after RFA in participants in AF at the time of RFA , compared to the participants in sinus rhythm who showed a slight increase ( P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "NT - proBNP", "type": "Chemical"}, {"text": "RFA", "type": "HealthCareActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "AF", "type": "BiologicFunction"}, {"text": "sinus rhythm", "type": "Finding"}]}

Example input:
Sentence: The most important significant parameters for RFS were intrinsic subtypes ( p < 0 . 001 ) and tumor size ( p < 0 . 001 ) and for OAS age ( p < 0 . 001 ) and intrinsic subtypes ( p < 0 . 001 ) .

Example answer:
{"entities": [{"text": "intrinsic", "type": "SpatialConcept"}, {"text": "subtypes", "type": "IntellectualProduct"}, {"text": "tumor size", "type": "SpatialConcept"}]}

Example input:
Sentence: NT - proBNP , MR - proANP , copeptin , and MR - proADM levels were measured in peripheral blood , the coronary sinus ( CS ) , and the left atrium before ablation , and in peripheral blood immediately and the day after RFA .

Example answer:
{"entities": [{"text": "NT - proBNP", "type": "Chemical"}, {"text": "MR - proANP", "type": "Chemical"}, {"text": "copeptin", "type": "Chemical"}, {"text": "MR - proADM", "type": "Chemical"}, {"text": "peripheral blood", "type": "BodySubstance"}, {"text": "coronary sinus", "type": "AnatomicalStructure"}, {"text": "CS", "type": "AnatomicalStructure"}, {"text": "left atrium", "type": "AnatomicalStructure"}, {"text": "ablation", "type": "HealthCareActivity"}, {"text": "RFA", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using data from a prospectively maintained database , 1884 lymph node - negative breast cancer patients who underwent partial mastectomy with SLN mapping by a dual - tracer using patent blue dye ( PBD ) and radioisotope were retrospectively studied between January 2000 and July 2013 .

Example answer:
{"entities": [{"text": "database", "type": "IntellectualProduct"}, {"text": "lymph node - negative", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "partial mastectomy", "type": "HealthCareActivity"}, {"text": "SLN mapping", "type": "HealthCareActivity"}, {"text": "patent blue dye", "type": "Chemical"}, {"text": "PBD", "type": "Chemical"}, {"text": "radioisotope", "type": "Chemical"}, {"text": "retrospectively studied", "type": "ResearchActivity"}]}

Example input:
Sentence: PSA , clinical stage and both number of nodes removed and EPLND were significant univariable predictors for LNI .

Example answer:
{"entities": [{"text": "PSA", "type": "Chemical"}, {"text": "nodes", "type": "AnatomicalStructure"}, {"text": "EPLND", "type": "HealthCareActivity"}, {"text": "univariable predictors", "type": "IntellectualProduct"}, {"text": "LNI", "type": "Finding"}]}

Example input:
Sentence: The median number of excised lymph nodes was 17 .

Example answer:
{"entities": [{"text": "excised", "type": "HealthCareActivity"}, {"text": "lymph nodes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Personalized axillary dissection : the number of excised lymph nodes of nodal - positive breast cancer patients has no significant impact on relapse - free and overall survival Sentinel lymph node ( SLN ) biopsy has replaced axillary lymph node dissection ( ALND ) for the staging of clinically node - negative breast cancer patients ( BCP ) , demonstrating equivalent survival to ALND while resulting in reduced morbidity .

Example answer:
{"entities": [{"text": "axillary dissection", "type": "HealthCareActivity"}, {"text": "excised", "type": "HealthCareActivity"}, {"text": "lymph nodes", "type": "AnatomicalStructure"}, {"text": "nodal - positive breast cancer", "type": "BiologicFunction"}, {"text": "Sentinel lymph node", "type": "AnatomicalStructure"}, {"text": "SLN", "type": "AnatomicalStructure"}, {"text": "biopsy", "type": "HealthCareActivity"}, {"text": "axillary lymph node dissection", "type": "HealthCareActivity"}, {"text": "ALND", "type": "HealthCareActivity"}, {"text": "staging", "type": "IntellectualProduct"}, {"text": "node - negative breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: There were no significant differences in RFS and OAS in any subgroup stratified by the number of excised lymph nodes .

Example answer:
{"entities": [{"text": "excised", "type": "HealthCareActivity"}, {"text": "lymph nodes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The number of excised lymph nodes was neither significant for RFS ( p = 0 . 085 ) nor for OAS ( p = 0 . 285 ) .

Example answer:
{"entities": [{"text": "excised", "type": "HealthCareActivity"}, {"text": "lymph nodes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: This analysis of pN + BCP shows the impact of the number of excised lymph nodes on RFS and OAS adjusted by age , tumor size , intrinsic subtypes and adjuvant systemic therapy .

Example answer:
{"entities": [{"text": "excised", "type": "HealthCareActivity"}, {"text": "lymph nodes", "type": "AnatomicalStructure"}, {"text": "tumor size", "type": "SpatialConcept"}, {"text": "intrinsic", "type": "SpatialConcept"}, {"text": "subtypes", "type": "IntellectualProduct"}, {"text": "adjuvant systemic therapy", "type": "HealthCareActivity"}]}

Input:
Sentence: The number of excised lymph nodes of pN + BCP neither correlates with RFS nor with OAS .

## Item MedMentions:test:4263
Example input:
Sentence: The participants ' expectations about counselling with regard to longer - term family , practical , and financial challenges were insufficiently met by the CMHC .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "counselling", "type": "HealthCareActivity"}, {"text": "family", "type": "Finding"}, {"text": "practical", "type": "Finding"}, {"text": "financial challenges", "type": "Finding"}, {"text": "CMHC", "type": "Organization"}]}

Example input:
Sentence: Our findings call for EMR ministries of health to increase provision of mental health services and to address the stigma of mental illness .

Example answer:
{"entities": [{"text": "mental health services", "type": "HealthCareActivity"}]}

Example input:
Sentence: Mental Health Composite Summary scores were low in both parents ( mothers : 40·45 ± 9·07 ; fathers : 40·58 ± 9·69 ) and lowest for the item ' vitality ' ( mothers : 37·0 ± 19·46 ; fathers : 43·12 ± 25·9 ) before and after stage II .

Example answer:
{"entities": [{"text": "Mental Health", "type": "BiologicFunction"}, {"text": "vitality", "type": "Finding"}]}

Example input:
Sentence: The burden of mental disorders in EMR increased from 1726 DALYs /100 , 000 in 1990 to 1912 DALYs /100 , 000 in 2013 ( 10 . 8 % increase ) .

Example answer:
{"entities": [{"text": "mental disorders", "type": "BiologicFunction"}, {"text": "EMR", "type": "SpatialConcept"}]}

Example input:
Sentence: Participants outlined transition procedures and drafted a range of preparation activities , centred around dedicated Transition Peer Support and a transition booklet , which should be offered to all CAMHS leavers , irrespective of discharge or transfer to an adult service .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "booklet", "type": "IntellectualProduct"}, {"text": "CAMHS", "type": "HealthCareActivity"}, {"text": "leavers", "type": "PopulationGroup"}, {"text": "adult service", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of the study was to explore how persons using a Community Mental Health Centre ( CMHC ) experienced that their expectations for treatment , and goals and hopes for recovery were supported by the health professionals during treatment .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "persons", "type": "PopulationGroup"}, {"text": "Community Mental Health Centre", "type": "Organization"}, {"text": "CMHC", "type": "Organization"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "goals", "type": "IntellectualProduct"}, {"text": "hopes", "type": "BiologicFunction"}, {"text": "recovery", "type": "BiologicFunction"}, {"text": "health professionals", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: CAMHS transitions are often poorly managed with negative outcomes for young people .

Example answer:
{"entities": [{"text": "CAMHS", "type": "HealthCareActivity"}, {"text": "negative", "type": "Finding"}, {"text": "people", "type": "PopulationGroup"}]}

Example input:
Sentence: Young people have clear ideas about the preparation they require to leave CAMHS with the confidence to take responsibility for their own health care .

Example answer:
{"entities": [{"text": "people", "type": "PopulationGroup"}, {"text": "CAMHS", "type": "HealthCareActivity"}, {"text": "confidence", "type": "BiologicFunction"}, {"text": "health care", "type": "HealthCareActivity"}]}

Example input:
Sentence: Young people , mental health practitioners and researchers co - produce a Transition Preparation Programme to improve outcomes and experience for young people leaving Child and Adolescent Mental Health Services ( CAMHS ) In the UK young people attending child and adolescent mental health services ( CAMHS ) are required to move on , either through discharge or referral to an adult service , at age 17 / 18 , a period of increased risk for onset of mental health problems and other complex psychosocial and physical changes .

Example answer:
{"entities": [{"text": "people", "type": "PopulationGroup"}, {"text": "mental health", "type": "BiologicFunction"}, {"text": "practitioners", "type": "ProfessionalOrOccupationalGroup"}, {"text": "researchers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Transition Preparation Programme", "type": "IntellectualProduct"}, {"text": "experience", "type": "BiologicFunction"}, {"text": "Child and Adolescent Mental Health Services", "type": "HealthCareActivity"}, {"text": "CAMHS", "type": "HealthCareActivity"}, {"text": "UK", "type": "SpatialConcept"}, {"text": "child and adolescent mental health services", "type": "HealthCareActivity"}, {"text": "referral to", "type": "HealthCareActivity"}, {"text": "adult service", "type": "HealthCareActivity"}, {"text": "mental health problems", "type": "Finding"}]}

Example input:
Sentence: Most young people felt anxious , fearful and uncertain on leaving CAMHS and perceived mental health services as uncaring .

Example answer:
{"entities": [{"text": "people", "type": "PopulationGroup"}, {"text": "anxious", "type": "Finding"}, {"text": "fearful", "type": "BiologicFunction"}, {"text": "CAMHS", "type": "HealthCareActivity"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "mental health services", "type": "HealthCareActivity"}]}

Input:
Sentence: Mental health services underestimate the anxiety of CAMHS leavers .

## Item MedMentions:test:3896
Example input:
Sentence: Pediatric Hypovitaminosis D : Molecular Perspectives and Clinical Implications Vitamin D , a secosteroid , is essential for the development and maintenance of healthy bone in both the adult and pediatric populations .

Example answer:
{"entities": [{"text": "Hypovitaminosis D", "type": "BiologicFunction"}, {"text": "Vitamin D", "type": "Chemical"}, {"text": "secosteroid", "type": "Chemical"}, {"text": "development", "type": "BiologicFunction"}, {"text": "bone", "type": "AnatomicalStructure"}, {"text": "populations", "type": "PopulationGroup"}]}

Example input:
Sentence: Serum levels of vitamins A , 25 ( OH ) D , and E , LL - 37 and allergen - specific IgE as well as nasopharyngeal / intratonsillar respiratory viruses were analyzed .

Example answer:
{"entities": [{"text": "Serum", "type": "BodySubstance"}, {"text": "vitamins A", "type": "Chemical"}, {"text": "25 ( OH ) D", "type": "Chemical"}, {"text": "E", "type": "Chemical"}, {"text": "LL - 37", "type": "Chemical"}, {"text": "allergen - specific IgE", "type": "Chemical"}, {"text": "nasopharyngeal", "type": "AnatomicalStructure"}, {"text": "intratonsillar", "type": "AnatomicalStructure"}, {"text": "respiratory viruses", "type": "Virus"}]}

Example input:
Sentence: The relationship of serum vitamins A , D , E and LL - 37 levels with allergic status , tonsillar virus detection and immune response Tonsils have an active role in immune defence and inducing and maintaining tolerance to allergens .

Example answer:
{"entities": [{"text": "serum", "type": "BodySubstance"}, {"text": "vitamins A", "type": "Chemical"}, {"text": "D", "type": "Chemical"}, {"text": "E", "type": "Chemical"}, {"text": "LL - 37", "type": "Chemical"}, {"text": "allergic status", "type": "BiologicFunction"}, {"text": "tonsillar", "type": "AnatomicalStructure"}, {"text": "virus detection", "type": "HealthCareActivity"}, {"text": "immune response", "type": "BiologicFunction"}, {"text": "Tonsils", "type": "AnatomicalStructure"}, {"text": "immune defence", "type": "BiologicFunction"}, {"text": "tolerance", "type": "BiologicFunction"}, {"text": "allergens", "type": "Chemical"}]}

Example input:
Sentence: Vitamin D binding protein ( VDBP ) and 25 - hydroxyvitamin D [ 25 ( OH ) D ] were measured by LC - MS , fibroblast growth factor ( FGF23 ) and parathyroid hormone ( PTH ) by enzyme - linked immunoassay , and calcium and phosphorus by Roche Cobas 6000 .

Example answer:
{"entities": [{"text": "Vitamin D binding protein", "type": "Chemical"}, {"text": "VDBP", "type": "Chemical"}, {"text": "25 - hydroxyvitamin D", "type": "Chemical"}, {"text": "25 ( OH ) D", "type": "Chemical"}, {"text": "LC - MS", "type": "HealthCareActivity"}, {"text": "fibroblast growth factor", "type": "Chemical"}, {"text": "FGF23", "type": "Chemical"}, {"text": "parathyroid hormone", "type": "Chemical"}, {"text": "PTH", "type": "Chemical"}, {"text": "enzyme - linked immunoassay", "type": "HealthCareActivity"}, {"text": "calcium", "type": "Chemical"}, {"text": "phosphorus", "type": "Chemical"}, {"text": "Roche Cobas 6000", "type": "HealthCareActivity"}]}

Example input:
Sentence: Quantification of individual flavins ( riboflavin and FMN ) from the same food samples showed variation in their values compared to TRF , and were in good agreement with values obtained from HPLC and AOAC methods .

Example answer:
{"entities": [{"text": "flavins", "type": "Chemical"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "FMN", "type": "Chemical"}, {"text": "TRF", "type": "Chemical"}, {"text": "agreement", "type": "IntellectualProduct"}, {"text": "HPLC", "type": "HealthCareActivity"}, {"text": "AOAC", "type": "HealthCareActivity"}, {"text": "methods", "type": "IntellectualProduct"}]}

Example input:
Sentence: Selective and sensitive electrochemical device for direct VB2 determination in real products The developed by us electrochemical device for vitamin B2 ( VB2 ; riboflavin ) determination , without preconcentration step , in real products exhibits high sensitivity , selectivity , stability and low detection limit compared to those described in the literature .

Example answer:
{"entities": [{"text": "VB2", "type": "Chemical"}, {"text": "determination", "type": "HealthCareActivity"}, {"text": "vitamin B2", "type": "Chemical"}, {"text": "riboflavin", "type": "Chemical"}]}

Example input:
Sentence: In this study , we have evaluated these two antibodies for the analysis of riboflavin and FMN by indirect competitive ELISA ( icELISA ) in selected foods and pharmaceuticals .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "antibodies", "type": "Chemical"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "FMN", "type": "Chemical"}, {"text": "competitive", "type": "BiologicFunction"}, {"text": "ELISA", "type": "HealthCareActivity"}, {"text": "icELISA", "type": "HealthCareActivity"}, {"text": "foods", "type": "Food"}, {"text": "pharmaceuticals", "type": "Chemical"}]}

Example input:
Sentence: Though , numerous methods have been reported for the determination of total riboflavin ( TRF ) content in foods and biological samples , very few methods are reported for quantifying riboflavin and its coenzymes [ flavin mononucleotide ( FMN ) ; flavin adenine dinucleotide ( FAD ) ] individually .

Example answer:
{"entities": [{"text": "methods", "type": "IntellectualProduct"}, {"text": "reported", "type": "IntellectualProduct"}, {"text": "determination", "type": "HealthCareActivity"}, {"text": "total riboflavin ( TRF ) content", "type": "HealthCareActivity"}, {"text": "foods", "type": "Food"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "coenzymes", "type": "Chemical"}, {"text": "flavin mononucleotide", "type": "Chemical"}, {"text": "FMN", "type": "Chemical"}, {"text": "flavin adenine dinucleotide", "type": "Chemical"}, {"text": "FAD", "type": "Chemical"}]}

Example input:
Sentence: The proposed VB2 detection method was used for determination of riboflavin content in commercially available dietary supplements and yolk of hen egg samples .

Example answer:
{"entities": [{"text": "VB2", "type": "Chemical"}, {"text": "detection", "type": "Finding"}, {"text": "determination", "type": "HealthCareActivity"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "commercially", "type": "IntellectualProduct"}, {"text": "dietary supplements", "type": "Food"}, {"text": "yolk", "type": "Food"}, {"text": "hen", "type": "Eukaryote"}, {"text": "egg samples", "type": "Food"}]}

Example input:
Sentence: The immunoassays developed in this study are sensitive and appears feasible for screening a large number of samples in the quantification of riboflavin and FMN in various biological samples , pharmaceuticals and natural / processed foods .

Example answer:
{"entities": [{"text": "immunoassays", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "FMN", "type": "Chemical"}, {"text": "pharmaceuticals", "type": "Chemical"}, {"text": "processed foods", "type": "Food"}]}

Input:
Sentence: Immunoassays for riboflavin and flavin mononucleotide using antibodies specific to d - ribitol and d - ribitol - 5 - phosphate Riboflavin ( vitamin B2 ) , a water - soluble vitamin , plays a key role in maintaining human health .

## Item MedMentions:test:4051
Example input:
Sentence: As shown in vitro , this direct interaction is mediated by binding of integrin αvβ3 expressed on ECs to the RGD - peptide in L1CAM expressed on CSCs .

Example answer:
{"entities": [{"text": "binding", "type": "BiologicFunction"}, {"text": "integrin αvβ3", "type": "Chemical"}, {"text": "ECs", "type": "AnatomicalStructure"}, {"text": "RGD - peptide", "type": "Chemical"}, {"text": "L1CAM", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "CSCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Intestinal epithelial ErbB3 knockout caused precocious appearance of PCs as early as postnatal day 7 , and substantially increased the number of mature PCs in adult mouse ileum .

Example answer:
{"entities": [{"text": "Intestinal", "type": "AnatomicalStructure"}, {"text": "ErbB3", "type": "AnatomicalStructure"}, {"text": "knockout", "type": "ResearchActivity"}, {"text": "PCs", "type": "AnatomicalStructure"}, {"text": "adult mouse", "type": "Eukaryote"}, {"text": "ileum", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Expansion of the PC compartment in ErbB3 -null intestines was accompanied with elevated ER stress and inflammation markers , raising the possibility that negative regulation of PCs by ErbB3 is necessary to maintain homeostasis .

Example answer:
{"entities": [{"text": "PC", "type": "AnatomicalStructure"}, {"text": "ErbB3", "type": "Chemical"}, {"text": "intestines", "type": "AnatomicalStructure"}, {"text": "ER stress", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "markers", "type": "ClinicalAttribute"}, {"text": "negative", "type": "Finding"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "PCs", "type": "AnatomicalStructure"}, {"text": "homeostasis", "type": "BiologicFunction"}]}

Example input:
Sentence: Finally , the most interesting candidates to this network were further validated by immunoprecipitation coupled with Western Blotting , which strengthened the confidence in the inferred interactions .

Example answer:
{"entities": [{"text": "candidates", "type": "PopulationGroup"}, {"text": "immunoprecipitation", "type": "HealthCareActivity"}, {"text": "Western Blotting", "type": "HealthCareActivity"}]}

Example input:
Sentence: This provides initial preclinical evidence for an essential role of MYC - ERCC3 interactions in PDAC , and suggests a new mechanistic approach for disruption of critical survival signaling in MYC -dependent cancers .

Example answer:
{"entities": [{"text": "MYC", "type": "Chemical"}, {"text": "ERCC3", "type": "Chemical"}, {"text": "PDAC", "type": "BiologicFunction"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "cancers", "type": "BiologicFunction"}]}

Example input:
Sentence: We further show that this ER interaction network changes in both content and abundance upon treatment with kifunensine ( kif ) and N - butyldeoxynojirimycin ( NB - DNJ ) which suggests that when interfering with the N - glycan processing pathway , the functional complexes involving EDEM3 adapt to maintain the cellular homeostasis .

Example answer:
{"entities": [{"text": "ER", "type": "AnatomicalStructure"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "kifunensine", "type": "Chemical"}, {"text": "kif", "type": "Chemical"}, {"text": "N - butyldeoxynojirimycin", "type": "Chemical"}, {"text": "NB - DNJ", "type": "Chemical"}, {"text": "N - glycan processing", "type": "BiologicFunction"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "EDEM3", "type": "Chemical"}, {"text": "cellular homeostasis", "type": "BiologicFunction"}]}

Example input:
Sentence: Inhibition of N - glycan processing modulates the network of EDEM3 interactors We present here data on EDEM3 network of ER resident interactors and the changes induced upon this network by perturbing the early ER N - glycan processing with mannosidase and glucosidase inhibitors .

Example answer:
{"entities": [{"text": "N - glycan processing", "type": "BiologicFunction"}, {"text": "modulates", "type": "SpatialConcept"}, {"text": "EDEM3", "type": "Chemical"}, {"text": "interactors", "type": "Chemical"}, {"text": "ER", "type": "AnatomicalStructure"}, {"text": "resident interactors", "type": "Chemical"}, {"text": "mannosidase", "type": "Chemical"}, {"text": "glucosidase", "type": "Chemical"}, {"text": "inhibitors", "type": "Chemical"}]}

Example input:
Sentence: In order to increase the scope of EDEM3 network contenders , the set of MS identified species was further supplemented with putative interactors derived from in silico simulations performed with STRING .

Example answer:
{"entities": [{"text": "EDEM3", "type": "Chemical"}, {"text": "contenders", "type": "PopulationGroup"}, {"text": "MS", "type": "HealthCareActivity"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "putative interactors", "type": "Chemical"}, {"text": "simulations", "type": "ResearchActivity"}, {"text": "STRING", "type": "IntellectualProduct"}]}

Example input:
Sentence: In addition , the results indicate that this network of EDEM3 interactors is highly sensitive to interfering with early ER N - glycan processing .

Example answer:
{"entities": [{"text": "EDEM3", "type": "Chemical"}, {"text": "interactors", "type": "Chemical"}, {"text": "ER", "type": "AnatomicalStructure"}, {"text": "N - glycan processing", "type": "BiologicFunction"}]}

Example input:
Sentence: The data corroborated herein suggest that besides ER residents , EDEM3 interacts also with proteins involved in the ERAD cargo recognition and targeting to degradation translocation into the cytosol , including UBA1 and UBA2 ubiquitinating enzymes .

Example answer:
{"entities": [{"text": "ER", "type": "AnatomicalStructure"}, {"text": "residents", "type": "Chemical"}, {"text": "EDEM3", "type": "Chemical"}, {"text": "proteins", "type": "Chemical"}, {"text": "ERAD", "type": "BiologicFunction"}, {"text": "degradation", "type": "BiologicFunction"}, {"text": "translocation", "type": "BiologicFunction"}, {"text": "cytosol", "type": "AnatomicalStructure"}, {"text": "UBA1", "type": "Chemical"}, {"text": "UBA2", "type": "Chemical"}, {"text": "ubiquitinating", "type": "BiologicFunction"}, {"text": "enzymes", "type": "Chemical"}]}

Input:
Sentence: By coupling immunoprecipitation with mass spectrometry we identified EDEM3 interactors and assigned statistical significance to those most abundant ER - residents that might form functional complexes with EDEM3 .

## Item MedMentions:test:3920
Example input:
Sentence: Do dynamic global vegetation models capture the seasonality of carbon fluxes in the Amazon basin ? A data - model intercomparison To predict forest response to long - term climate change with high confidence requires that dynamic global vegetation models ( DGVMs ) be successfully tested against ecosystem response to short - term variations in environmental drivers , including regular seasonal patterns .

Example answer:
{"entities": [{"text": "dynamic global vegetation models", "type": "IntellectualProduct"}, {"text": "Amazon basin", "type": "SpatialConcept"}, {"text": "model", "type": "IntellectualProduct"}, {"text": "DGVMs", "type": "IntellectualProduct"}, {"text": "environmental drivers", "type": "SpatialConcept"}]}

Example input:
Sentence: We performed a basin - wide analysis of pre - Columbian impacts on Amazonian forests by overlaying known archaeological sites in Amazonia with the distributions and abundances of 85 woody species domesticated by pre - Columbian peoples .

Example answer:
{"entities": [{"text": "basin - wide analysis", "type": "ResearchActivity"}, {"text": "archaeological sites", "type": "SpatialConcept"}, {"text": "woody", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "peoples", "type": "PopulationGroup"}]}

Example input:
Sentence: Models simulated consistent dry - season declines in GPP in the equatorial Amazon ( Manaus K34 , Santarem K67 , and Caxiuanã CAX ) ; a contrast to observed GPP increases .

Example answer:
{"entities": [{"text": "Models", "type": "IntellectualProduct"}, {"text": "equatorial Amazon", "type": "SpatialConcept"}, {"text": "Manaus K34", "type": "SpatialConcept"}, {"text": "Santarem K67", "type": "SpatialConcept"}, {"text": "Caxiuanã CAX", "type": "SpatialConcept"}]}

Example input:
Sentence: Our analyses indicate that modern tree communities in Amazonia are structured to an important extent by a long history of plant domestication by Amazonian peoples .

Example answer:
{"entities": [{"text": "analyses", "type": "ResearchActivity"}, {"text": "tree", "type": "Eukaryote"}, {"text": "plant", "type": "Eukaryote"}, {"text": "peoples", "type": "PopulationGroup"}]}

Example input:
Sentence: The dataset comprises 136 references from 300 locations covering seven vegetation types of tropical and subtropical Atlantic forests of South America , and presents data on species composition , richness , and relative abundance ( captures / trap - nights ) .

Example answer:
{"entities": [{"text": "dataset", "type": "IntellectualProduct"}, {"text": "locations", "type": "SpatialConcept"}, {"text": "vegetation types", "type": "Eukaryote"}, {"text": "South America", "type": "SpatialConcept"}]}

Example input:
Sentence: Here we present new gridded ( 8x8 km ) reconstructions of pre - settlement ( 1800s ) forest composition and structure from the upper Midwestern US ( Minnesota , Wisconsin , and most of Michigan ) , using 19th Century Public Land Survey System ( PLSS ) , with estimates of relative composition , above - ground biomass , stem density , and basal area for 28 tree types .

Example answer:
{"entities": [{"text": "upper Midwestern US", "type": "SpatialConcept"}, {"text": "Minnesota", "type": "SpatialConcept"}, {"text": "Wisconsin", "type": "SpatialConcept"}, {"text": "Century Public Land Survey System", "type": "IntellectualProduct"}, {"text": "PLSS", "type": "IntellectualProduct"}, {"text": "above - ground", "type": "SpatialConcept"}, {"text": "stem", "type": "Eukaryote"}, {"text": "basal area", "type": "SpatialConcept"}, {"text": "tree", "type": "Eukaryote"}]}

Example input:
Sentence: In contrast , a southern Amazon forest ( Jarú RJA ) exhibited dry - season declines in GPP and Re consistent with most DGVMs simulations .

Example answer:
{"entities": [{"text": "southern Amazon", "type": "SpatialConcept"}, {"text": "Re", "type": "BiologicFunction"}, {"text": "DGVMs", "type": "IntellectualProduct"}, {"text": "simulations", "type": "ResearchActivity"}]}

Example input:
Sentence: Ecosystem -level adaptations to low soil nutrient availability and long - term low levels of disturbance may help to account for the lower productivity and higher accumulation of biomass in nutrient -poor forests compared to nutrient -richer forests .

Example answer:
{"entities": [{"text": "accumulation", "type": "Finding"}]}

Example input:
Sentence: While water limitation was represented in models and the primary driver of seasonal photosynthesis in southern Amazonia , changes in internal biophysical processes , light - harvesting adaptations ( e . g . , variations in leaf area index ( LAI ) and increasing leaf -level assimilation rate related to leaf demography ) , and allocation lags between leaf and wood , dominated equatorial Amazon carbon flux dynamics and were deficient or absent from current model formulations .

Example answer:
{"entities": [{"text": "models", "type": "IntellectualProduct"}, {"text": "southern Amazonia", "type": "SpatialConcept"}, {"text": "biophysical processes", "type": "BiologicFunction"}, {"text": "light - harvesting", "type": "BiologicFunction"}, {"text": "leaf area index", "type": "IntellectualProduct"}, {"text": "LAI", "type": "IntellectualProduct"}, {"text": "leaf", "type": "Eukaryote"}, {"text": "assimilation", "type": "BiologicFunction"}, {"text": "wood", "type": "Eukaryote"}, {"text": "equatorial Amazon", "type": "SpatialConcept"}, {"text": "model", "type": "IntellectualProduct"}]}

Example input:
Sentence: Here , we used an integrated dataset from four forests in the Brasil flux network , spanning a range of dry - season intensities and lengths , to determine how well four state - of - the - art models ( IBIS , ED2 , JULES , and CLM3 . 5 ) simulated the seasonality of carbon exchanges in Amazonian tropical forests .

Example answer:
{"entities": [{"text": "dataset", "type": "IntellectualProduct"}, {"text": "Brasil flux network", "type": "IntellectualProduct"}, {"text": "models", "type": "IntellectualProduct"}, {"text": "IBIS", "type": "IntellectualProduct"}, {"text": "ED2", "type": "IntellectualProduct"}, {"text": "JULES", "type": "IntellectualProduct"}, {"text": "CLM3 . 5", "type": "IntellectualProduct"}, {"text": "Amazonian", "type": "SpatialConcept"}]}

Input:
Sentence: We used data for > 34 000 trees from several permanent plots in French Guiana to investigate if soil characteristics could predict the structure ( tree diameter , density and aboveground biomass ) , and dynamics ( growth , mortality , aboveground wood productivity ) of nutrient -poor tropical forests .

## Item MedMentions:test:4331
Example input:
Sentence: Elevated Serum Uric Acid Level Predicts Rapid Decline in Kidney Function While elevated serum uric acid level ( SUA ) is a recognized risk factor for chronic kidney disease , it remains unclear whether change in SUA is independently associated with change in estimated glomerular filtration rate ( eGFR ) over time .

Example answer:
{"entities": [{"text": "Elevated Serum Uric Acid Level", "type": "Finding"}, {"text": "Kidney Function", "type": "BiologicFunction"}, {"text": "elevated serum uric acid level", "type": "Finding"}, {"text": "SUA", "type": "Chemical"}, {"text": "risk factor", "type": "Finding"}, {"text": "chronic kidney disease", "type": "BiologicFunction"}, {"text": "estimated glomerular filtration rate", "type": "HealthCareActivity"}, {"text": "eGFR", "type": "HealthCareActivity"}]}

Example input:
Sentence: We assessed the association of UACR with subclinical cardiac measures , adjusting for sociodemographic and cardiometabolic factors .

Example answer:
{"entities": [{"text": "UACR", "type": "Finding"}, {"text": "subclinical cardiac measures", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the first 5 years of follow - up , elevated UA was associated with mortality ( Hazard Ratio , HR = 1 . 7 ; p = 0 . 045 ) .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "UA", "type": "Chemical"}]}

Example input:
Sentence: Elevated left ventricular afterload leads to myocardial hypertrophy , diastolic dysfunction , cellular remodelling and compromised calcium dynamics .

Example answer:
{"entities": [{"text": "Elevated left ventricular afterload", "type": "Finding"}, {"text": "myocardial hypertrophy", "type": "BiologicFunction"}, {"text": "diastolic dysfunction", "type": "BiologicFunction"}, {"text": "cellular", "type": "AnatomicalStructure"}, {"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: UA was not associated with ESRD , but was associated with doubling of creatinine among diabetics ( HR = 2 . 2 [ 1 . 1 , 4 . 3 ] ; p = 0 . 025 ) .

Example answer:
{"entities": [{"text": "UA", "type": "Chemical"}, {"text": "ESRD", "type": "BiologicFunction"}, {"text": "creatinine", "type": "Chemical"}, {"text": "diabetics", "type": "BiologicFunction"}]}

Example input:
Sentence: Among 1 , 815 participants ( median age 54 , women 65 % ) , 42 % had normal UACR , 43 % high - normal UACR , 13 % microalbuminuria , and 2 % macroalbuminuria .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "normal UACR", "type": "Finding"}, {"text": "high - normal UACR", "type": "Finding"}, {"text": "microalbuminuria", "type": "Finding"}, {"text": "macroalbuminuria", "type": "Finding"}]}

Example input:
Sentence: We assessed the association of UACR with cardiac structure and function in the Echocardiographic Study of Latinos ( Echo - SOL ) , an ancillary study of the Hispanic Community Health Study / Study of Latinos across 4 US sites .

Example answer:
{"entities": [{"text": "UACR", "type": "Finding"}, {"text": "cardiac structure", "type": "AnatomicalStructure"}, {"text": "function", "type": "BiologicFunction"}, {"text": "Echocardiographic Study of Latinos", "type": "ResearchActivity"}, {"text": "Echo - SOL", "type": "ResearchActivity"}, {"text": "ancillary study", "type": "ResearchActivity"}, {"text": "Hispanic Community Health Study", "type": "ResearchActivity"}, {"text": "Study of Latinos", "type": "ResearchActivity"}, {"text": "US", "type": "SpatialConcept"}]}

Example input:
Sentence: UACR was categorized as normal and high - normal ( based on the midpoint of values below microalbuminuria ) , microalbuminuria ( ≥17 mg / g for men ; ≥25 mg / g for women ) , and macroalbuminuria ( ≥250 mg / g ; ≥355 mg / g ) .

Example answer:
{"entities": [{"text": "UACR", "type": "Finding"}, {"text": "high - normal", "type": "Finding"}, {"text": "microalbuminuria", "type": "Finding"}, {"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "macroalbuminuria", "type": "Finding"}]}

Example input:
Sentence: Association of Albuminuria With Cardiac Dysfunction in US Hispanics / Latinos Higher urine albumin - to - creatinine ratio ( UACR ) has been associated with cardiac dysfunction in the general population .

Example answer:
{"entities": [{"text": "Albuminuria", "type": "Finding"}, {"text": "Cardiac Dysfunction", "type": "BiologicFunction"}, {"text": "US", "type": "SpatialConcept"}, {"text": "Hispanics", "type": "PopulationGroup"}, {"text": "Latinos", "type": "PopulationGroup"}, {"text": "urine albumin - to - creatinine ratio", "type": "Finding"}, {"text": "UACR", "type": "Finding"}, {"text": "cardiac dysfunction", "type": "BiologicFunction"}, {"text": "general population", "type": "PopulationGroup"}]}

Example input:
Sentence: In conclusion , elevated UACR was associated with LV hypertrophy and diastolic dysfunction in the largest known population sample of US Hispanic / Latinos .

Example answer:
{"entities": [{"text": "elevated UACR", "type": "Finding"}, {"text": "LV hypertrophy", "type": "BiologicFunction"}, {"text": "diastolic dysfunction", "type": "BiologicFunction"}, {"text": "population sample", "type": "PopulationGroup"}, {"text": "US", "type": "SpatialConcept"}, {"text": "Hispanic", "type": "PopulationGroup"}, {"text": "Latinos", "type": "PopulationGroup"}]}

Input:
Sentence: Elevated UACR , even at high - normal levels , was significantly associated with greater diastolic dysfunction .

## Item MedMentions:test:3949
Example input:
Sentence: Biotin surface functionalized micelles showed higher internalization rates due biotin -mediated endocytosis , as demonstrated by competitive cellular uptake studies .

Example answer:
{"entities": [{"text": "Biotin", "type": "Chemical"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "micelles", "type": "Chemical"}, {"text": "biotin", "type": "Chemical"}, {"text": "endocytosis", "type": "BiologicFunction"}, {"text": "competitive cellular uptake", "type": "BiologicFunction"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: Long - range interactions between protein - coated particles and POEGMA brush layers in a serum environment Hydrophilic poly [ oligo ( ethylene glycol ) methyl methacrylate ] ( POEGMA ) brush layers with different thickness and graft densities were prepared by surface - initiated atom transfer radical polymerization ( SI - ATRP ) to construct a model surface to examine protein - surface interactions in a serum environment .

Example answer:
{"entities": [{"text": "protein", "type": "Chemical"}, {"text": "particles", "type": "Chemical"}, {"text": "POEGMA brush", "type": "Chemical"}, {"text": "serum environment", "type": "BodySubstance"}, {"text": "Hydrophilic poly [ oligo ( ethylene glycol ) methyl methacrylate ] ( POEGMA ) brush", "type": "Chemical"}, {"text": "prepared", "type": "Finding"}, {"text": "model", "type": "IntellectualProduct"}, {"text": "surface", "type": "SpatialConcept"}]}

Example input:
Sentence: This chapter presents a protocol for an optimized and high - throughput IgG N - glycan release , fluorescent labeling and cleanup , and analysis of fluorescently labeled IgG N - glycans by hydrophilic interaction liquid chromatography ( HILIC ) on an ultra performance liquid chromatography ( UPLC ) system with fluorescence ( FLR ) detection .

Example answer:
{"entities": [{"text": "protocol", "type": "IntellectualProduct"}, {"text": "IgG N - glycan", "type": "Chemical"}, {"text": "fluorescent labeling", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "IgG N - glycans", "type": "Chemical"}, {"text": "hydrophilic interaction liquid chromatography", "type": "HealthCareActivity"}, {"text": "HILIC", "type": "HealthCareActivity"}, {"text": "ultra performance liquid chromatography", "type": "HealthCareActivity"}, {"text": "UPLC", "type": "HealthCareActivity"}, {"text": "detection", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here we have established , to our knowledge , a new platform for monitoring SNARE -mediated docking and fusion between giant unilamellar vesicles ( GUVs ) and smaller liposomes or purified secretory granules with high temporal and spatial resolution .

Example answer:
{"entities": [{"text": "SNARE", "type": "Chemical"}, {"text": "docking", "type": "BiologicFunction"}, {"text": "fusion", "type": "BiologicFunction"}, {"text": "giant unilamellar vesicles", "type": "Chemical"}, {"text": "GUVs", "type": "Chemical"}, {"text": "liposomes", "type": "Chemical"}, {"text": "secretory granules", "type": "AnatomicalStructure"}, {"text": "temporal", "type": "Finding"}]}

Example input:
Sentence: In addition , we used the heterogeneous silicon mesostructures to design a lipid - bilayer -supported bioelectric interface that is remotely controlled and temporally transient , and that permits non - genetic and subcellular optical modulation of the electrophysiology dynamics in single dorsal root ganglia neurons .

Example answer:
{"entities": [{"text": "silicon", "type": "Chemical"}, {"text": "mesostructures", "type": "Chemical"}, {"text": "lipid - bilayer", "type": "AnatomicalStructure"}, {"text": "remotely", "type": "SpatialConcept"}, {"text": "subcellular", "type": "AnatomicalStructure"}, {"text": "dorsal root ganglia", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In order to design an optimal drug carrier for each disease , various kinds of self - assembled aggregates , such as spherical micelles , lens - like vesicles , and tube - like vesicles , were evaluated by " multiple techniques " including dynamic light scattering , differential scanning calorimetry , nuclear magnetic resonance spectroscopy , and fluorescence measurement using the Laurdan probe .

Example answer:
{"entities": [{"text": "drug carrier", "type": "Chemical"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "spherical micelles", "type": "Chemical"}, {"text": "dynamic light scattering", "type": "HealthCareActivity"}, {"text": "differential scanning calorimetry", "type": "HealthCareActivity"}, {"text": "nuclear magnetic resonance spectroscopy", "type": "HealthCareActivity"}, {"text": "fluorescence measurement", "type": "HealthCareActivity"}, {"text": "Laurdan", "type": "Chemical"}, {"text": "probe", "type": "MedicalDevice"}]}

Example input:
Sentence: Liposomes in a concentration of 5mM of varying composition and fluidity were immobilized on the sensor surface by inserting the hydrophobic residues of the former loaded SSMs .

Example answer:
{"entities": [{"text": "Liposomes", "type": "Chemical"}, {"text": "composition", "type": "ClinicalAttribute"}, {"text": "immobilized", "type": "HealthCareActivity"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "SSMs", "type": "Chemical"}]}

Example input:
Sentence: In this work , a method is described for immobilizing liposomes for interaction studies , based on the biophysical principles of this biosensor platform .

Example answer:
{"entities": [{"text": "immobilizing", "type": "HealthCareActivity"}, {"text": "liposomes", "type": "Chemical"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: A combination of this simple liposome immobilization approach , the possibility of automation on BLI systems with high throughput within an acceptable timescale and excellent reproducibility makes this assay suitable for basic research as well as for industrial and regulatory applications .

Example answer:
{"entities": [{"text": "liposome", "type": "Chemical"}, {"text": "immobilization", "type": "HealthCareActivity"}, {"text": "BLI", "type": "HealthCareActivity"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "research", "type": "ResearchActivity"}, {"text": "regulatory applications", "type": "IntellectualProduct"}]}

Example input:
Sentence: The immobilization approach includes the loading of DSPE - PEG ( 2000 ) - biotin containing sterically stabilized micelles ( SSMs ) which are restructured in a buffer change step , resulting in an accessible substrate for liposome immobilization .

Example answer:
{"entities": [{"text": "immobilization", "type": "HealthCareActivity"}, {"text": "DSPE - PEG ( 2000 )", "type": "Chemical"}, {"text": "biotin", "type": "Chemical"}, {"text": "micelles", "type": "Chemical"}, {"text": "SSMs", "type": "Chemical"}, {"text": "liposome", "type": "Chemical"}]}

Input:
Sentence: An approach for liposome immobilization using sterically stabilized micelles ( SSMs ) as a precursor for bio - layer interferometry - based interaction studies Non - fluidic bio - layer interferometry ( BLI ) has rapidly become a standard tool for monitoring almost all biomolecular interactions in a label - free , real - time and high - throughput manner .

## Item MedMentions:test:4405
Example input:
Sentence: Multivariate logistic regression analyses ( adjusted for age , gender , education level , physical activity , alcohol use , smoking status , depression , arrhythmia , myocardial infarction , heart failure , stroke ) showed that participants with better feelings of affection , behavioral confirmation and stable good social support had a lower risk of incident SMC .

Example answer:
{"entities": [{"text": "education level", "type": "Finding"}, {"text": "smoking status", "type": "ClinicalAttribute"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "arrhythmia", "type": "Finding"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "heart failure", "type": "BiologicFunction"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "feelings", "type": "BiologicFunction"}, {"text": "affection", "type": "BiologicFunction"}, {"text": "confirmation", "type": "Finding"}, {"text": "SMC", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients with psychiatric comorbidities had worse net adverse cardiac events ( HR 1 . 18 , 95 % CI : 1 . 16 - 1 . 21 ) and mortality rates ( HR 1 . 26 , 95 % CI : 1 . 23 - 1 . 30 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Consistent with these results , we proved in our own studies , that subjects with mild elevation of serum levels of unconjugated bilirubin ( benign hyperbilirubinemia , Gilbert syndrome ) have much lower prevalence / incidence of coronary heart as well as peripheral vascular disease .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "hyperbilirubinemia", "type": "BiologicFunction"}, {"text": "Gilbert syndrome", "type": "BiologicFunction"}, {"text": "coronary heart", "type": "BiologicFunction"}, {"text": "peripheral vascular disease", "type": "BiologicFunction"}]}

Example input:
Sentence: When the population was stratified into three groups in function of the normalized peak filling rate , significant differences were observed among groups for age ( p = 0 . 002 ) , mean wall thickness ( p = 0 . 036 ) , and myocardial mass ( p = 0 . 046 ) and atrial dimensions , whereas no significant differences with respect to late enhancement were seen .

Example answer:
{"entities": [{"text": "population", "type": "PopulationGroup"}, {"text": "late enhancement", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the Western trial ( SYNTAX ) , female sex favored coronary artery bypass graft compared with percutaneous coronary intervention ( hazard ratio ( percutaneous coronary intervention ) 2 . 213 ; 95 % confidence interval , 1 . 242 - 3 . 943 ; P = 0 . 007 ) , whereas in the Asian women ( PRECOMBAT and BEST ) , the treatment effect was neutral between both strategies .

Example answer:
{"entities": [{"text": "Western", "type": "PopulationGroup"}, {"text": "trial", "type": "ResearchActivity"}, {"text": "SYNTAX", "type": "HealthCareActivity"}, {"text": "female", "type": "PopulationGroup"}, {"text": "sex", "type": "BiologicFunction"}, {"text": "coronary artery bypass graft", "type": "HealthCareActivity"}, {"text": "percutaneous coronary intervention", "type": "HealthCareActivity"}, {"text": "Asian", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "PRECOMBAT", "type": "HealthCareActivity"}, {"text": "BEST", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "strategies", "type": "HealthCareActivity"}]}

Example input:
Sentence: and had higher mean comorbidity score ( 1 . 47 vs .

Example answer:
{"entities": []}

Example input:
Sentence: In CD and UC patients , V was 49 % and 52 % higher than in AS , respectively , and CL was 47 % and 60 % higher than in AS , respectively .

Example answer:
{"entities": [{"text": "CD", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}, {"text": "AS", "type": "BiologicFunction"}]}

Example input:
Sentence: In addition , AAS users demonstrated higher coronary artery plaque volume than nonusers ( median [ interquartile range ] 3 [ 0 , 174 ] mL ( 3 ) versus 0 [ 0 , 69 ] mL ( 3 ) ; P = 0 .

Example answer:
{"entities": [{"text": "AAS", "type": "Chemical"}, {"text": "coronary artery", "type": "AnatomicalStructure"}, {"text": "plaque", "type": "Finding"}, {"text": "nonusers", "type": "PopulationGroup"}]}

Example input:
Sentence: Increased CVD risk ( ≥10 % 10 - year Framingham risk score ) was present for 13 % of the cohort ; 79 % of the cohort had ≥1 cardiometabolic comorbidity , 48 % had ≥2 , and 13 % had all three .

Example answer:
{"entities": [{"text": "CVD", "type": "BiologicFunction"}, {"text": "risk", "type": "HealthCareActivity"}, {"text": "10 - year Framingham risk score", "type": "Finding"}, {"text": "present", "type": "Finding"}, {"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: The prevalence rates of cardiovascular diseases were lower in the moderate ( odds ratio [ OR ] , 0 . 822 ; 95 % confidence interval [ CI ] , 0 . 737 - 0 . 916 ; p = 0 .

Example answer:
{"entities": [{"text": "cardiovascular diseases", "type": "BiologicFunction"}]}

Input:
Sentence: Bivariate comparison showed increased prevalence of coronary artery disease in the OP group ( 32 % vs .

## Item MedMentions:test:4294
Example input:
Sentence: In the Spanish cohort , dysbiosis was found significantly greater in patients with CD than with UC , as shown by a more reduced diversity , a less stable microbial community and eight microbial groups were proposed as a specific microbial signature for CD .

Example answer:
{"entities": [{"text": "Spanish", "type": "PopulationGroup"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "dysbiosis", "type": "BiologicFunction"}, {"text": "CD", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}]}

Example input:
Sentence: The optimal combination of prostatic and urothelial markers could improve the ability to differentiate PAC from UC pathologically .

Example answer:
{"entities": [{"text": "prostatic", "type": "AnatomicalStructure"}, {"text": "urothelial", "type": "AnatomicalStructure"}, {"text": "markers", "type": "Chemical"}, {"text": "improve", "type": "Finding"}, {"text": "ability", "type": "Finding"}, {"text": "PAC", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}]}

Example input:
Sentence: Our study suggests that PSC - UC represent a different immunological disorder from UC , characterised by increased intestinal Th1 and ILC responses .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "PSC", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}, {"text": "immunological disorder", "type": "BiologicFunction"}, {"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "Th1", "type": "AnatomicalStructure"}, {"text": "ILC", "type": "AnatomicalStructure"}, {"text": "responses", "type": "BiologicFunction"}]}

Example input:
Sentence: In order to ensure that the individuals were not affected by unknown syndromes or diseases , we excluded all individuals with any chronic medical condition , or who had other birth defects than clefts , hydroceles and dislocated hips .

Example answer:
{"entities": [{"text": "individuals", "type": "PopulationGroup"}, {"text": "syndromes", "type": "BiologicFunction"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "birth defects", "type": "AnatomicalStructure"}, {"text": "clefts", "type": "AnatomicalStructure"}, {"text": "hydroceles", "type": "AnatomicalStructure"}, {"text": "dislocated hips", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Although UC and CD share many epidemiologic , immunologic , therapeutic and clinical features , our results showed that they are two distinct subtypes of IBD at the microbiome level .

Example answer:
{"entities": [{"text": "UC", "type": "BiologicFunction"}, {"text": "CD", "type": "BiologicFunction"}, {"text": "subtypes", "type": "IntellectualProduct"}, {"text": "IBD", "type": "BiologicFunction"}]}

Example input:
Sentence: Development and validation of diagnostic criteria for IBD subtypes with an emphasis on IBD - Unclassified in children : a multicenter study from the Pediatric IBD Porto group of ESPGHAN The revised Porto criteria identify subtypes of pediatric inflammatory bowel diseases : ulcerative colitis ( UC ) , atypical UC , Inflammatory Bowel Disease Unclassified ( IBDU ) , and Crohn 's disease ( CD ) .

Example answer:
{"entities": [{"text": "diagnostic criteria", "type": "IntellectualProduct"}, {"text": "IBD", "type": "BiologicFunction"}, {"text": "IBD - Unclassified", "type": "BiologicFunction"}, {"text": "multicenter study", "type": "ResearchActivity"}, {"text": "Porto group", "type": "PopulationGroup"}, {"text": "ESPGHAN", "type": "Organization"}, {"text": "Porto criteria", "type": "IntellectualProduct"}, {"text": "inflammatory bowel diseases", "type": "BiologicFunction"}, {"text": "ulcerative colitis", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}, {"text": "Inflammatory Bowel Disease Unclassified", "type": "BiologicFunction"}, {"text": "IBDU", "type": "BiologicFunction"}, {"text": "Crohn 's disease", "type": "BiologicFunction"}, {"text": "CD", "type": "BiologicFunction"}]}

Example input:
Sentence: The validated algorithm can adequately classify children with IBD into small bowel CD , Colonic CD , IBDU , atypical UC and UC .

Example answer:
{"entities": [{"text": "algorithm", "type": "IntellectualProduct"}, {"text": "IBD", "type": "BiologicFunction"}, {"text": "small bowel", "type": "AnatomicalStructure"}, {"text": "CD", "type": "BiologicFunction"}, {"text": "Colonic", "type": "AnatomicalStructure"}, {"text": "IBDU", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}]}

Example input:
Sentence: The algorithm differentiated UC from CD and IBDU with 80 % sensitivity ( 95 % CI 71 - 88 % ) and 84 % specificity ( 77 - 89 % ) , and CD from IBDU and UC with 78 % sensitivity ( 67 - 87 % ) and 94 % specificity ( 89 - 97 % ) .

Example answer:
{"entities": [{"text": "algorithm", "type": "IntellectualProduct"}, {"text": "UC", "type": "BiologicFunction"}, {"text": "CD", "type": "BiologicFunction"}, {"text": "IBDU", "type": "BiologicFunction"}]}

Example input:
Sentence: A total of 23 features were clustered in 3 classes according to their prevalence in UC : 6 class - 1 ( 0 % prevalence in UC ) , 12 class - 2 ( < 5 % prevalence ) and 5 class - 3 ( 5 - 10 % prevalence ) .

Example answer:
{"entities": [{"text": "classes", "type": "IntellectualProduct"}, {"text": "UC", "type": "BiologicFunction"}, {"text": "class - 1", "type": "IntellectualProduct"}, {"text": "class - 2", "type": "IntellectualProduct"}, {"text": "class - 3", "type": "IntellectualProduct"}]}

Example input:
Sentence: When at least one feature exist , different combinations classify the disease into atypical UC , IBDU and CD .

Example answer:
{"entities": [{"text": "disease", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}, {"text": "IBDU", "type": "BiologicFunction"}, {"text": "CD", "type": "BiologicFunction"}]}

Input:
Sentence: According to the algorithm , the disease should be classified as UC if no features exist in any of the classes .

## Item MedMentions:test:4247
Example input:
Sentence: We show that RA190 reduces the expression of Stat3 and the levels of key immunosuppressive enzymes and cytokines arginase , iNOS , and IL - 10 in MDSCs , while boosting expression of the immunostimulatory cytokine IL - 12 .

Example answer:
{"entities": [{"text": "RA190", "type": "Chemical"}, {"text": "Stat3", "type": "Chemical"}, {"text": "immunosuppressive", "type": "BiologicFunction"}, {"text": "enzymes", "type": "Chemical"}, {"text": "cytokines", "type": "Chemical"}, {"text": "arginase", "type": "Chemical"}, {"text": "iNOS", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "MDSCs", "type": "AnatomicalStructure"}, {"text": "immunostimulatory", "type": "HealthCareActivity"}, {"text": "cytokine", "type": "Chemical"}, {"text": "IL - 12", "type": "Chemical"}]}

Example input:
Sentence: However , whether HNO also serves as a treatment to septic arthritis is currently unknown .

Example answer:
{"entities": [{"text": "HNO", "type": "Chemical"}, {"text": "septic arthritis", "type": "BiologicFunction"}]}

Example input:
Sentence: Here we demonstrate that in arthritic , but also in healthy , mice administration of agents that influence macrophage activity / number and / or addition of empty decoy capsids substantially improve the efficacy of recombinant adeno - associated viral vector 5 transgene expression in the joint .

Example answer:
{"entities": [{"text": "arthritic", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "administration of agents", "type": "HealthCareActivity"}, {"text": "macrophage", "type": "AnatomicalStructure"}, {"text": "decoy capsids", "type": "AnatomicalStructure"}, {"text": "improve", "type": "Finding"}, {"text": "adeno - associated viral", "type": "Virus"}, {"text": "vector", "type": "Chemical"}, {"text": "transgene", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "joint", "type": "SpatialConcept"}]}

Example input:
Sentence: Empty Capsids and Macrophage Inhibition / Depletion Increase rAAV Transgene Expression in Joints of Both Healthy and Arthritic Mice Gene therapy has potential to treat rheumatic diseases ; however , the presence of macrophages in the joint might hamper adeno - associated viral vector -mediated gene delivery .

Example answer:
{"entities": [{"text": "Capsids", "type": "AnatomicalStructure"}, {"text": "Macrophage", "type": "AnatomicalStructure"}, {"text": "rAAV", "type": "Chemical"}, {"text": "Transgene", "type": "AnatomicalStructure"}, {"text": "Expression", "type": "BiologicFunction"}, {"text": "Joints", "type": "SpatialConcept"}, {"text": "Arthritic", "type": "BiologicFunction"}, {"text": "Mice", "type": "Eukaryote"}, {"text": "Gene therapy", "type": "HealthCareActivity"}, {"text": "treat", "type": "HealthCareActivity"}, {"text": "rheumatic diseases", "type": "BiologicFunction"}, {"text": "presence", "type": "Finding"}, {"text": "macrophages", "type": "AnatomicalStructure"}, {"text": "joint", "type": "SpatialConcept"}, {"text": "adeno - associated viral", "type": "Virus"}, {"text": "vector", "type": "Chemical"}]}

Example input:
Sentence: ASG - IV played a positive role in human osteoarthritic chondrocyte apoptosis , possibly through modulation of the Hippo signaling pathway by up - regulating YAP1 and ACTG1 expression , and also by up - regulating VTN and COL1A1 , which are involved in the ECM - receptor interaction pathway .

Example answer:
{"entities": [{"text": "ASG - IV", "type": "Chemical"}, {"text": "positive role", "type": "Finding"}, {"text": "human", "type": "Eukaryote"}, {"text": "osteoarthritic chondrocyte apoptosis", "type": "BiologicFunction"}, {"text": "Hippo signaling pathway", "type": "BiologicFunction"}, {"text": "up - regulating", "type": "BiologicFunction"}, {"text": "YAP1", "type": "Chemical"}, {"text": "ACTG1", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "VTN", "type": "Chemical"}, {"text": "COL1A1", "type": "Chemical"}]}

Example input:
Sentence: Results from quantitative polymerase chain reaction and histological analysis indicated that FACDs possessed effective anti - inflammatory effects in vitro and in vivo compared to aspirin only .

Example answer:
{"entities": [{"text": "quantitative polymerase chain reaction", "type": "HealthCareActivity"}, {"text": "histological analysis", "type": "HealthCareActivity"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: The immunosuppressive nature of parasitic infections may offer potential insight into therapeutic strategies for rheumatoid arthritis , in which the immune system is overactivated .

Example answer:
{"entities": [{"text": "immunosuppressive", "type": "BiologicFunction"}, {"text": "parasitic infections", "type": "BiologicFunction"}, {"text": "insight", "type": "BiologicFunction"}, {"text": "rheumatoid arthritis", "type": "BiologicFunction"}, {"text": "immune system", "type": "BodySystem"}]}

Example input:
Sentence: aureus colony forming unities in synovial tissue , enhanced the bactericidal effect of macrophages and inhibited the worsening of systemic inflammatory response ( leukocyte counts in the lung and systemic proinflammatory cytokine concentration ) .

Example answer:
{"entities": [{"text": "aureus", "type": "Bacterium"}, {"text": "colony forming unities", "type": "Finding"}, {"text": "synovial tissue", "type": "AnatomicalStructure"}, {"text": "bactericidal effect", "type": "BiologicFunction"}, {"text": "macrophages", "type": "AnatomicalStructure"}, {"text": "worsening", "type": "Finding"}, {"text": "systemic inflammatory response", "type": "BiologicFunction"}, {"text": "leukocyte counts", "type": "HealthCareActivity"}, {"text": "lung", "type": "AnatomicalStructure"}, {"text": "proinflammatory cytokine concentration", "type": "Finding"}]}

Example input:
Sentence: The nitroxyl donor Angeli 's salt ameliorates Staphylococcus aureus -induced septic arthritis in mice Septic arthritis is a severe and rapidly debilitating disease associated with severe joint pain , inflammation and oxidative stress .

Example answer:
{"entities": [{"text": "nitroxyl donor", "type": "Chemical"}, {"text": "Angeli 's salt", "type": "Chemical"}, {"text": "Staphylococcus aureus", "type": "Bacterium"}, {"text": "septic arthritis", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "Septic arthritis", "type": "BiologicFunction"}, {"text": "rapidly debilitating disease", "type": "BiologicFunction"}, {"text": "severe joint pain", "type": "Finding"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "oxidative stress", "type": "BiologicFunction"}]}

Example input:
Sentence: Daily treatment with AS inhibited mechanical hyperalgesia and inflammation ( edema , leukocyte migration , cytokines release and NF - κB activation , and oxidative stress ) resulting in reduced disease severity ( clinical course , histopathological changes , proteoglycan levels in the joints , and osteoclastogenesis ) .

Example answer:
{"entities": [{"text": "AS", "type": "Chemical"}, {"text": "mechanical hyperalgesia", "type": "Finding"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "edema", "type": "Finding"}, {"text": "leukocyte migration", "type": "BiologicFunction"}, {"text": "cytokines release", "type": "BiologicFunction"}, {"text": "NF - κB activation", "type": "BiologicFunction"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "proteoglycan", "type": "Chemical"}, {"text": "joints", "type": "SpatialConcept"}, {"text": "osteoclastogenesis", "type": "BiologicFunction"}]}

Input:
Sentence: Our results suggest for the first time the therapeutic potential of AS in a model of septic arthritis by mechanisms involving microbicidal effects , anti - inflammatory actions and reduction of disease severity .

## Item MedMentions:test:4271
Example input:
Sentence: Cofactor - binding loop 2 variants had detrimental effects on specific activity at elevated temperatures , whereas the H192P mutation in cofactor - binding loop 1 resulted in a two - fold improved stability to inactivation at elevated temperatures , and increased the critical onset temperature for aggregation .

Example answer:
{"entities": [{"text": "Cofactor - binding loop 2", "type": "SpatialConcept"}, {"text": "variants", "type": "AnatomicalStructure"}, {"text": "H192P mutation", "type": "BiologicFunction"}, {"text": "cofactor - binding loop 1", "type": "SpatialConcept"}]}

Example input:
Sentence: Role of cysteine residues in regulation of peptidyl - prolyl cis - trans isomerase activity of wheat cyclophilin TaCYPA - 1 Oxidative conditions result in inhibition of peptidyl - prolyl cis - trans isomerase ( PPIase ) activity of several cyclophilins .

Example answer:
{"entities": [{"text": "cysteine", "type": "Chemical"}, {"text": "peptidyl - prolyl cis - trans isomerase activity", "type": "BiologicFunction"}, {"text": "wheat", "type": "Food"}, {"text": "cyclophilin", "type": "Chemical"}, {"text": "TaCYPA - 1", "type": "AnatomicalStructure"}, {"text": "peptidyl - prolyl cis - trans isomerase ( PPIase ) activity", "type": "BiologicFunction"}, {"text": "cyclophilins", "type": "Chemical"}]}

Example input:
Sentence: Yet , tspC - cells showed a defect in coping with hypo - osmotic stress , due to accumulation of contractile vacuoles , but heterologous expression of TspC rescued their phenotype .

Example answer:
{"entities": [{"text": "contractile vacuoles", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "TspC", "type": "Chemical"}]}

Example input:
Sentence: The results of limited proteolysis indicated that Glu138Pro mutant was more resistant against trypsinolysis and this variant was less quenched in both acrylamide and KI quenching experiments .

Example answer:
{"entities": [{"text": "limited proteolysis", "type": "BiologicFunction"}, {"text": "Glu138Pro mutant", "type": "Chemical"}, {"text": "trypsinolysis", "type": "BiologicFunction"}, {"text": "variant", "type": "Chemical"}, {"text": "acrylamide", "type": "Chemical"}, {"text": "KI", "type": "Chemical"}, {"text": "quenching experiments", "type": "HealthCareActivity"}]}

Example input:
Sentence: Neither heating rate nor thermal stress affected plasma sodium and chloride levels , nor the expression of transcripts that included catalase , glucocorticoid receptor , heat shock protein70 ( hsp70 ) , heat shock protein 90α ( hsp90α ) and cytochrome P450 1a ( cyp1a ) .

Example answer:
{"entities": [{"text": "thermal stress", "type": "BiologicFunction"}, {"text": "plasma sodium", "type": "HealthCareActivity"}, {"text": "chloride levels", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "transcripts", "type": "Chemical"}, {"text": "catalase", "type": "Chemical"}, {"text": "glucocorticoid receptor", "type": "Chemical"}, {"text": "heat shock protein70", "type": "Chemical"}, {"text": "hsp70", "type": "Chemical"}, {"text": "heat shock protein 90α", "type": "Chemical"}, {"text": "hsp90α", "type": "Chemical"}, {"text": "cytochrome P450 1a", "type": "Chemical"}, {"text": "cyp1a", "type": "Chemical"}]}

Example input:
Sentence: While for both , the starchless mutant of plastidial phospho - gluco mutase ( pgm ) and a mutant defective in sucrose - phosphate synthase A1 , metabolic constraints , especially at low temperature , could be uncovered based on subcellularly resolved metabolite profiles , only pgm had lowered freezing tolerance .

Example answer:
{"entities": [{"text": "starchless mutant", "type": "BiologicFunction"}, {"text": "plastidial", "type": "AnatomicalStructure"}, {"text": "phospho - gluco mutase", "type": "Chemical"}, {"text": "pgm", "type": "Chemical"}, {"text": "mutant", "type": "BiologicFunction"}, {"text": "sucrose - phosphate synthase A1", "type": "Chemical"}, {"text": "subcellularly", "type": "AnatomicalStructure"}, {"text": "resolved", "type": "Finding"}, {"text": "metabolite profiles", "type": "BiologicFunction"}, {"text": "freezing tolerance", "type": "BiologicFunction"}]}

Example input:
Sentence: Compared to wild - type TaCYPA - 1 , the different mutants also showed differential sensitivity to Cu2 + .

Example answer:
{"entities": [{"text": "wild - type", "type": "AnatomicalStructure"}, {"text": "TaCYPA - 1", "type": "AnatomicalStructure"}, {"text": "mutants", "type": "BiologicFunction"}, {"text": "Cu2 +", "type": "Chemical"}]}

Example input:
Sentence: These observations suggest that the mechanism of TaCYPA - 1 -induced thermotolerance may also involve other activities besides cis to trans isomerisation , which needs to be identified further .

Example answer:
{"entities": [{"text": "observations", "type": "ResearchActivity"}, {"text": "TaCYPA - 1", "type": "AnatomicalStructure"}, {"text": "thermotolerance", "type": "BiologicFunction"}]}

Example input:
Sentence: Comparative analysis of their PPIase activity revealed that catalytic efficiencies ( Kcat / Km ) of TaCYPA - 1C40S ( 0 . 37 X 106 M - 1 s - 1 ) and TaCYPA - 1C122S ( 0 . 31 X 106 M - 1 s - 1 ) were significantly lower as compared to the native TaCYPA - 1 ( 1 . 33 X 106 M - 1 s - 1 ) , whereas Kcat / Km of the double mutant TaCYPA - 1C40S / C122S was significantly higher ( 2 . 36 X 106 M - 1 s - 1 ) .

Example answer:
{"entities": [{"text": "PPIase activity", "type": "BiologicFunction"}, {"text": "TaCYPA - 1C40S", "type": "Chemical"}, {"text": "TaCYPA - 1C122S", "type": "Chemical"}, {"text": "TaCYPA - 1", "type": "Chemical"}, {"text": "mutant", "type": "BiologicFunction"}, {"text": "TaCYPA - 1C40S / C122S", "type": "Chemical"}]}

Example input:
Sentence: To further understand the regulation of PPIase activity of TaCYPA - 1 , we generated mutants of TaCYPA - 1 by substituting cysteine residues at positions -40 and -122 with serine , and at -126 with proline .

Example answer:
{"entities": [{"text": "PPIase activity", "type": "BiologicFunction"}, {"text": "TaCYPA - 1", "type": "AnatomicalStructure"}, {"text": "mutants", "type": "BiologicFunction"}, {"text": "cysteine", "type": "Chemical"}, {"text": "positions", "type": "SpatialConcept"}, {"text": "serine", "type": "Chemical"}, {"text": "proline", "type": "Chemical"}]}

Input:
Sentence: Furthermore , the results of this study also revealed that despite lacking PPIase activity , the mutant TaCYPA - 1C126P was able to confer partial protection against heat stress .

## Item MedMentions:test:4423
Example input:
Sentence: In the present study , we attempted to demonstrate effects and preferred modes of therapeutic intervention in PNES patients with ID being treated at a Japanese municipal center with a short referral chain .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "therapeutic intervention", "type": "HealthCareActivity"}, {"text": "PNES", "type": "BiologicFunction"}, {"text": "ID", "type": "BiologicFunction"}, {"text": "Japanese municipal center", "type": "Organization"}, {"text": "referral chain", "type": "HealthCareActivity"}]}

Example input:
Sentence: We describe a cohort of patients with progressive respiratory failure related to a pathogenic variant in FLNA and present lung transplantation as a viable therapeutic option for this group of patients .

Example answer:
{"entities": [{"text": "cohort", "type": "PopulationGroup"}, {"text": "respiratory failure", "type": "BiologicFunction"}, {"text": "lung transplantation", "type": "HealthCareActivity"}, {"text": "viable therapeutic option", "type": "HealthCareActivity"}]}

Example input:
Sentence: Nowadays , PCLs represent a common and often difficult challenge in clinical practice , because of the increase in their detection in asymptomatic patients and our still immature understanding of some aspects of their biologic behavior .

Example answer:
{"entities": [{"text": "PCLs", "type": "Finding"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "asymptomatic", "type": "Finding"}, {"text": "understanding", "type": "BiologicFunction"}]}

Example input:
Sentence: Despite medical and technological advances in PCI , periprocedural myocardial infarction ( PMI ) remains a common complication .

Example answer:
{"entities": [{"text": "PCI", "type": "HealthCareActivity"}, {"text": "periprocedural myocardial infarction", "type": "BiologicFunction"}, {"text": "PMI", "type": "BiologicFunction"}, {"text": "complication", "type": "BiologicFunction"}]}

Example input:
Sentence: Of the 36 patients who had positive LNs at the final pathology , 22 were in the EPLND group and 14 in the SPLND group ( p < 0 . 01 ) .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "LNs", "type": "AnatomicalStructure"}, {"text": "pathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "EPLND", "type": "HealthCareActivity"}, {"text": "SPLND", "type": "HealthCareActivity"}]}

Example input:
Sentence: A Systematic Review and Meta - Analysis of the Data Behind Current Recommendations for Corticosteroids in Non - HIV - Related PCP : Knowing When You Are on Shaky Foundations Randomized trials show a mortality benefit to adjunctive corticosteroids for human immunodeficiency virus ( HIV ) - related Pneumocystis jiroveci pneumonia ( HIV - PCP ) .

Example answer:
{"entities": [{"text": "Systematic Review", "type": "IntellectualProduct"}, {"text": "Meta - Analysis", "type": "IntellectualProduct"}, {"text": "Corticosteroids", "type": "Chemical"}, {"text": "Non - HIV - Related PCP", "type": "BiologicFunction"}, {"text": "Randomized trials", "type": "ResearchActivity"}, {"text": "adjunctive corticosteroids", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Virus"}, {"text": "HIV", "type": "Virus"}, {"text": "Pneumocystis jiroveci pneumonia", "type": "BiologicFunction"}, {"text": "PCP", "type": "BiologicFunction"}]}

Example input:
Sentence: In parallel , clinical and pathological characteristics of 260 patients who underwent resection of noninvasive IPMN were reviewed to identify risk factors associated with local progression .

Example answer:
{"entities": [{"text": "resection", "type": "HealthCareActivity"}, {"text": "noninvasive IPMN", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "local", "type": "SpatialConcept"}, {"text": "progression", "type": "BiologicFunction"}]}

Example input:
Sentence: Under these circumstances , the accurate classification of PCNs becomes crucial .

Example answer:
{"entities": [{"text": "classification", "type": "IntellectualProduct"}, {"text": "PCNs", "type": "BiologicFunction"}]}

Example input:
Sentence: Using NGS , we identify distinct mechanisms for development of metachronous or synchronous neoplasms in patients with IPMN .

Example answer:
{"entities": [{"text": "metachronous", "type": "BiologicFunction"}, {"text": "synchronous neoplasms", "type": "BiologicFunction"}, {"text": "IPMN", "type": "BiologicFunction"}]}

Example input:
Sentence: Since then , the interest in PCLs increased markedly , especially so with the recognition of the importance and prevalence of intraductal papillary mucinous neoplasms ( IPMNs ) .

Example answer:
{"entities": [{"text": "PCLs", "type": "Finding"}, {"text": "intraductal papillary mucinous neoplasms", "type": "BiologicFunction"}, {"text": "IPMNs", "type": "BiologicFunction"}]}

Input:
Sentence: Management of patients with PCNs can be challenging and varies considerably among the various subtypes of PCNs .

## Item MedMentions:test:4059
Example input:
Sentence: Rare deleterious mutations are associated with disease in bipolar disorder families Bipolar disorder ( BD ) is a common , complex and heritable psychiatric disorder characterized by episodes of severe mood swings .

Example answer:
{"entities": [{"text": "deleterious mutations", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "bipolar disorder", "type": "BiologicFunction"}, {"text": "Bipolar disorder", "type": "BiologicFunction"}, {"text": "BD", "type": "BiologicFunction"}, {"text": "heritable", "type": "BiologicFunction"}, {"text": "psychiatric disorder", "type": "BiologicFunction"}, {"text": "episodes", "type": "BiologicFunction"}, {"text": "mood swings", "type": "BiologicFunction"}]}

Example input:
Sentence: Upstream Pathways Controlling Mitochondrial Function in Major Psychosis : A Focus on Bipolar Disorder Mitochondrial dysfunction is commonly observed in bipolar disorder ( BD ) and schizophrenia ( SCZ ) and may be a central feature of psychosis .

Example answer:
{"entities": [{"text": "Upstream Pathways", "type": "BiologicFunction"}, {"text": "Psychosis", "type": "BiologicFunction"}, {"text": "Bipolar Disorder", "type": "BiologicFunction"}, {"text": "Mitochondrial dysfunction", "type": "Finding"}, {"text": "bipolar disorder", "type": "BiologicFunction"}, {"text": "BD", "type": "BiologicFunction"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "SCZ", "type": "BiologicFunction"}, {"text": "psychosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Recently , special attention has been given to homocysteine ( Hcy ) , as it has been suggested that alterations in 1 - carbon metabolism might be implicated in diverse psychiatric disorders .

Example answer:
{"entities": [{"text": "homocysteine", "type": "Chemical"}, {"text": "Hcy", "type": "Chemical"}, {"text": "1 - carbon metabolism", "type": "BiologicFunction"}, {"text": "psychiatric disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: This pattern of de - and increases was not different between bipolar offspring that developed or did not develop a mood disorder over time , apart from the IGF - BP2 level , which was near significantly higher in offspring later developing a mood disorder .

Example answer:
{"entities": [{"text": "pattern", "type": "SpatialConcept"}, {"text": "bipolar", "type": "BiologicFunction"}, {"text": "mood disorder", "type": "BiologicFunction"}, {"text": "IGF - BP2", "type": "Chemical"}]}

Example input:
Sentence: Independent t - tests were used to compare girls with and without DBD , while path analyses tested for the mediating role of post - trauma symptoms in the relation between stress regulating systems and externalizing behaviour . Females with DBD ( n = 37 ) reported significantly higher rates of post - trauma symptoms and externalizing behaviour problems than girls without DBD ( n = 39 ) .

Example answer:
{"entities": [{"text": "t - tests", "type": "IntellectualProduct"}, {"text": "DBD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "stress regulating systems", "type": "BodySystem"}, {"text": "externalizing behaviour", "type": "Finding"}, {"text": "externalizing behaviour problems", "type": "BiologicFunction"}]}

Example input:
Sentence: The aim of this study was to examine temperament in symptomatic and asymptomatic child offspring of parents with bipolar disorder ( OBD ) and to investigate whether inhibited temperament is associated with aberrant hippocampal volumes compared with healthy control ( HC ) youth .

Example answer:
{"entities": [{"text": "examine", "type": "Finding"}, {"text": "temperament", "type": "BiologicFunction"}, {"text": "asymptomatic", "type": "Finding"}, {"text": "bipolar disorder", "type": "BiologicFunction"}, {"text": "OBD", "type": "BiologicFunction"}, {"text": "hippocampal", "type": "AnatomicalStructure"}]}

Example input:
Sentence: However , there is uncertainty regarding possible alterations in peripheral Hcy levels in BD .

Example answer:
{"entities": [{"text": "uncertainty", "type": "Finding"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "Hcy", "type": "Chemical"}, {"text": "BD", "type": "BiologicFunction"}]}

Example input:
Sentence: Our meta - analysis provides evidence that Hcy levels are elevated in persons with BD during mania and euthymia .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}, {"text": "Hcy levels are elevated", "type": "Finding"}, {"text": "persons", "type": "PopulationGroup"}, {"text": "BD", "type": "BiologicFunction"}, {"text": "mania", "type": "BiologicFunction"}, {"text": "euthymia", "type": "BiologicFunction"}]}

Example input:
Sentence: Random - effects meta - analysis showed that serum and plasma levels of Hcy were increased in subjects with BD in either mania or euthymia when compared to healthy controls , with a large effect size in the mania group ( g = 0 .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}, {"text": "serum", "type": "HealthCareActivity"}, {"text": "plasma levels of Hcy", "type": "HealthCareActivity"}, {"text": "BD", "type": "BiologicFunction"}, {"text": "mania", "type": "BiologicFunction"}, {"text": "euthymia", "type": "BiologicFunction"}, {"text": "group", "type": "PopulationGroup"}]}

Example input:
Sentence: Peripheral Hcy could be considered as a potential biomarker in BD , both of trait ( since it is increased in euthymia ) , and also of state ( since its increase is more accentuated in mania ) .

Example answer:
{"entities": [{"text": "Peripheral", "type": "SpatialConcept"}, {"text": "Hcy", "type": "Chemical"}, {"text": "biomarker", "type": "ClinicalAttribute"}, {"text": "BD", "type": "BiologicFunction"}, {"text": "euthymia", "type": "BiologicFunction"}, {"text": "mania", "type": "BiologicFunction"}]}

Input:
Sentence: Longitudinal studies are needed to clarify the relationship between bipolar disorder and Hcy , as well as the usefulness of peripheral Hcy as both a trait and state biomarker in BD .

## Item MedMentions:test:4282
Example input:
Sentence: In contrast , we found a decrease in glutamate uptake in the cortex , but not the hippocampus , 24 h after injury .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "uptake", "type": "BiologicFunction"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Blood samples were also taken from the control group 24 hours before the injury , and whole brain tissues in the injured groups were harvested at 72 and 168 hours post - injury .

Example answer:
{"entities": [{"text": "Blood samples", "type": "HealthCareActivity"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "brain tissues", "type": "AnatomicalStructure"}, {"text": "harvested", "type": "HealthCareActivity"}]}

Example input:
Sentence: Two cohorts of male Wistar rats underwent the intraluminal filament model of middle cerebral artery occlusion ( 30 min ) and were imaged 24 h later .

Example answer:
{"entities": [{"text": "cohorts", "type": "PopulationGroup"}, {"text": "Wistar rats", "type": "Eukaryote"}, {"text": "intraluminal filament model", "type": "IntellectualProduct"}, {"text": "middle cerebral artery occlusion", "type": "AnatomicalStructure"}, {"text": "imaged", "type": "HealthCareActivity"}]}

Example input:
Sentence: Seven days post trauma , subjects were evaluated in a Morris water maze ( MWM ) and evaluated for changes in lesion volume .

Example answer:
{"entities": [{"text": "post trauma", "type": "Finding"}, {"text": "subjects", "type": "PopulationGroup"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "Morris water maze", "type": "HealthCareActivity"}, {"text": "MWM", "type": "HealthCareActivity"}, {"text": "lesion volume", "type": "Finding"}]}

Example input:
Sentence: Mice were tested for spatial memory performance ( radial arm water maze ) , sensorimotor coordination ( computerized gait analysis , CatWalk ) , and cerebromicrovascular function ( whisker - stimulation -induced increases in CBF , measured by laser Doppler flowmetry ) at 3 to 6 months post - irradiation .

Example answer:
{"entities": [{"text": "Mice", "type": "Eukaryote"}, {"text": "spatial memory", "type": "BiologicFunction"}, {"text": "sensorimotor coordination", "type": "BiologicFunction"}, {"text": "computerized gait analysis", "type": "HealthCareActivity"}, {"text": "CatWalk", "type": "IntellectualProduct"}, {"text": "whisker", "type": "AnatomicalStructure"}, {"text": "CBF", "type": "Finding"}, {"text": "laser Doppler flowmetry", "type": "HealthCareActivity"}]}

Example input:
Sentence: Neurological examinations suggested that the functions of the cerebral cortex , cerebellum , and brain stem showed significant differences pre - and post - injury ( p < 0 . 001 ) .

Example answer:
{"entities": [{"text": "Neurological examinations", "type": "HealthCareActivity"}, {"text": "cerebral cortex", "type": "AnatomicalStructure"}, {"text": "cerebellum", "type": "AnatomicalStructure"}, {"text": "brain stem", "type": "AnatomicalStructure"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Diffuse traumatic brain injury affects chronic corticosterone function in the rat As many as 20 - 55 % of patients with a history of traumatic brain injury ( TBI ) experience chronic endocrine dysfunction , leading to impaired quality of life , impaired rehabilitation efforts and lowered life expectancy .

Example answer:
{"entities": [{"text": "Diffuse traumatic brain injury", "type": "InjuryOrPoisoning"}, {"text": "corticosterone", "type": "Chemical"}, {"text": "rat", "type": "Eukaryote"}, {"text": "history", "type": "Finding"}, {"text": "traumatic brain injury", "type": "InjuryOrPoisoning"}, {"text": "TBI", "type": "InjuryOrPoisoning"}, {"text": "lowered life expectancy", "type": "Finding"}]}

Example input:
Sentence: Systematic and detailed analysis of behavioural tests in the rat middle cerebral artery occlusion model of stroke : Tests for long - term assessment In order to test therapeutics , functional assessments are required .

Example answer:
{"entities": [{"text": "detailed analysis", "type": "ResearchActivity"}, {"text": "behavioural tests", "type": "HealthCareActivity"}, {"text": "rat", "type": "Eukaryote"}, {"text": "middle cerebral artery occlusion", "type": "AnatomicalStructure"}, {"text": "model", "type": "Eukaryote"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "Tests", "type": "IntellectualProduct"}, {"text": "therapeutics", "type": "HealthCareActivity"}, {"text": "functional assessments", "type": "HealthCareActivity"}]}

Example input:
Sentence: After 24 h , the rats were anaesthetized , blood and muscle samples were taken .

Example answer:
{"entities": [{"text": "rats", "type": "Eukaryote"}, {"text": "blood", "type": "BodySubstance"}, {"text": "muscle", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Spatial cognitive deficits and chronic brain tissue loss , as well as endogenous brain repair processes such as neurogenesis , angiogenesis , and oligodendrogenesis , were evaluated up to 35 days after TBI .

Example answer:
{"entities": [{"text": "brain tissue", "type": "AnatomicalStructure"}, {"text": "brain repair processes", "type": "HealthCareActivity"}, {"text": "neurogenesis", "type": "BiologicFunction"}, {"text": "angiogenesis", "type": "BiologicFunction"}, {"text": "oligodendrogenesis", "type": "BiologicFunction"}, {"text": "TBI", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: These rats would be assessed from the neurological perspective based on their grades of performance in a sequence of tests 24 hours before and 12 hours after brain injury .

## Item MedMentions:test:4324
Example input:
Sentence: 0 % of AIS 4 + head injury involves the brainstem .

Example answer:
{"entities": [{"text": "head injury", "type": "InjuryOrPoisoning"}, {"text": "brainstem", "type": "AnatomicalStructure"}]}

Example input:
Sentence: NASS - CDS indicates there are 872 ± 133 cases of brainstem injury per year .

Example answer:
{"entities": [{"text": "NASS - CDS", "type": "IntellectualProduct"}, {"text": "brainstem injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Eighteen NASS - CDS electronic cases showed that brainstem injury occurred in very severe collisions where the occupant experienced multiple injuries from intrusion or impact on vehicle structures stiffened by deformation .

Example answer:
{"entities": [{"text": "NASS - CDS", "type": "IntellectualProduct"}, {"text": "brainstem injury", "type": "InjuryOrPoisoning"}, {"text": "collisions", "type": "InjuryOrPoisoning"}, {"text": "occupant", "type": "PopulationGroup"}, {"text": "multiple injuries", "type": "InjuryOrPoisoning"}, {"text": "structures", "type": "SpatialConcept"}]}

Example input:
Sentence: NASS - CDS electronic cases were reviewed to see if the transition from vehicles without advanced airbags and seatbelts , side airbags and curtains to vehicles with the safety technologies has influenced the risk for brainstem injury .

Example answer:
{"entities": [{"text": "NASS - CDS", "type": "IntellectualProduct"}, {"text": "brainstem injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The risk for brainstem injury increased with crash severity .

Example answer:
{"entities": [{"text": "brainstem injury", "type": "InjuryOrPoisoning"}, {"text": "crash", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The highest risk for brainstem injury was 3 .

Example answer:
{"entities": [{"text": "brainstem injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Brainstem Injury in Motor Vehicle Crashes This is a descriptive study of the frequency and risk for brainstem injury by crash type , belt use and crash severity ( delta V ) .

Example answer:
{"entities": [{"text": "Brainstem Injury", "type": "InjuryOrPoisoning"}, {"text": "study", "type": "ResearchActivity"}, {"text": "brainstem injury", "type": "InjuryOrPoisoning"}, {"text": "crash", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: In contrast , the highest risk for brainstem injury was 0 .

Example answer:
{"entities": [{"text": "brainstem injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The prevention of brainstem injuries must address the extreme speed of collisions and weight mismatches that overwhelm structures , seatbelts , frontal airbags , side airbags and curtains in modern vehicles .

Example answer:
{"entities": [{"text": "prevention", "type": "HealthCareActivity"}, {"text": "brainstem injuries", "type": "InjuryOrPoisoning"}, {"text": "address", "type": "IntellectualProduct"}, {"text": "structures", "type": "SpatialConcept"}]}

Example input:
Sentence: The risk for brainstem injury in belted occupants has remained essentially constant over 20 years , whereas the risk for MAIS 4 + F injury has declined 38 .

Example answer:
{"entities": [{"text": "brainstem injury", "type": "InjuryOrPoisoning"}, {"text": "belted", "type": "Finding"}, {"text": "occupants", "type": "PopulationGroup"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: For belted occupants , the highest risk for brainstem injury was in side impacts at 0 .

## Item MedMentions:test:4026
Example input:
Sentence: Osteogenic differentiation led to significant induction of ALP activity in iliac crest ( sixfold ) and facet joint ( eightfold ) MSC .

Example answer:
{"entities": [{"text": "Osteogenic differentiation", "type": "BiologicFunction"}, {"text": "ALP activity", "type": "BiologicFunction"}, {"text": "iliac crest", "type": "AnatomicalStructure"}, {"text": "facet joint", "type": "SpatialConcept"}, {"text": "MSC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Furthermore , in the ninth month , graft fixation groups had the lowest chondrocyte densities , the highest degree of inflammation , the highest degree of foreign body reaction , and the highest butyl cyanoacrylate density .

Example answer:
{"entities": [{"text": "graft", "type": "HealthCareActivity"}, {"text": "fixation", "type": "HealthCareActivity"}, {"text": "chondrocyte", "type": "AnatomicalStructure"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "foreign body reaction", "type": "BiologicFunction"}, {"text": "butyl cyanoacrylate", "type": "Chemical"}]}

Example input:
Sentence: Peritumoral adipose tissues expressed CYP19A1 approximately threefold higher than tumor itself ( p = 0 . 001 ) .

Example answer:
{"entities": [{"text": "Peritumoral", "type": "SpatialConcept"}, {"text": "adipose tissues", "type": "AnatomicalStructure"}, {"text": "CYP19A1", "type": "AnatomicalStructure"}, {"text": "tumor", "type": "BiologicFunction"}]}

Example input:
Sentence: Alkaline phosphatase expression ( ALP ) was used to quantify osteoblastic differentiation of MC3T3 - E1 cell .

Example answer:
{"entities": [{"text": "Alkaline phosphatase", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "ALP", "type": "Chemical"}, {"text": "osteoblastic differentiation", "type": "BiologicFunction"}, {"text": "MC3T3 - E1 cell", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Altered pH gradient at the plasma membrane of osteosarcoma cells is a key mechanism of drug resistance Current therapy of osteosarcoma ( OS ) , the most common primary bone malignancy , is based on a combination of surgery and chemotherapy .

Example answer:
{"entities": [{"text": "plasma membrane", "type": "AnatomicalStructure"}, {"text": "osteosarcoma", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "drug resistance", "type": "BiologicFunction"}, {"text": "therapy", "type": "HealthCareActivity"}, {"text": "OS", "type": "BiologicFunction"}, {"text": "primary bone malignancy", "type": "BiologicFunction"}]}

Example input:
Sentence: The number of osteocalcin - positive cells within the central area of the augmented sinus was significantly higher in the CaS / SB group than in the control group ( 179 ± 26 . 0 mm ( 2 ) and 123 ± 33 . 2 mm ( 2 ) , respectively , p = 0 . 027 ) .

Example answer:
{"entities": [{"text": "osteocalcin - positive", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "central area", "type": "SpatialConcept"}, {"text": "sinus", "type": "SpatialConcept"}, {"text": "CaS", "type": "Chemical"}, {"text": "SB", "type": "Chemical"}]}

Example input:
Sentence: Supplementation with ω - 3 PUFAs not only suppresses bone resorption but also promotes new bone formation in the periapical area of rats with AP in conjunction with downregulation of inflammatory cell infiltration into the lesion .

Example answer:
{"entities": [{"text": "Supplementation", "type": "HealthCareActivity"}, {"text": "ω - 3 PUFAs", "type": "Chemical"}, {"text": "bone resorption", "type": "BiologicFunction"}, {"text": "promotes new bone formation", "type": "BiologicFunction"}, {"text": "periapical area", "type": "SpatialConcept"}, {"text": "rats", "type": "Eukaryote"}, {"text": "AP", "type": "BiologicFunction"}, {"text": "downregulation", "type": "BiologicFunction"}, {"text": "inflammatory cell infiltration", "type": "BiologicFunction"}, {"text": "lesion", "type": "Finding"}]}

Example input:
Sentence: Perivascular fat monocyte / macrophage infiltration was higher in eET - 1 and smPparγ and increased further in eET - 1 / smPparγ .

Example answer:
{"entities": [{"text": "Perivascular", "type": "SpatialConcept"}, {"text": "fat monocyte", "type": "AnatomicalStructure"}, {"text": "macrophage", "type": "AnatomicalStructure"}, {"text": "infiltration", "type": "BiologicFunction"}, {"text": "eET - 1", "type": "Chemical"}, {"text": "smPparγ", "type": "Chemical"}]}

Example input:
Sentence: The number of osteocalcin - positive osteoblasts was significantly increased in the AP -O group compared with the AP group ( P > .05 ) .

Example answer:
{"entities": [{"text": "osteocalcin", "type": "Chemical"}, {"text": "positive", "type": "Finding"}, {"text": "osteoblasts", "type": "AnatomicalStructure"}, {"text": "AP", "type": "BiologicFunction"}]}

Example input:
Sentence: Immunohistochemical analyses were performed to detect tartrate - resistant acid phosphatase - positive osteoclasts and osteocalcin - positive osteoblasts on the bone surface of periapical area .

Example answer:
{"entities": [{"text": "analyses", "type": "ResearchActivity"}, {"text": "tartrate - resistant acid phosphatase", "type": "Chemical"}, {"text": "positive", "type": "Finding"}, {"text": "osteoclasts", "type": "AnatomicalStructure"}, {"text": "osteocalcin", "type": "Chemical"}, {"text": "osteoblasts", "type": "AnatomicalStructure"}, {"text": "bone surface", "type": "SpatialConcept"}, {"text": "periapical area", "type": "SpatialConcept"}]}

Input:
Sentence: The level of inflammatory cell infiltration was significantly elevated , and the number of tartrate - resistant acid phosphatase - positive osteoclasts was significantly higher in the periapical lesions of the AP group compared with AP -O , C , and C - O groups ( P < .05 ) .

## Item MedMentions:test:4590
Example input:
Sentence: 6 × 10 ( - 7 ) M ) .

Example answer:
{"entities": []}

Example input:
Sentence: 03×10 ( - 9 ) , 7 . 57×10 ( - 9 ) , 9 . 69×10 ( - 9 ) and 8 . 15×10 ( - 9 ) , respectively , which were much lower than the threshold value of CR ( 10 ( - 6 ) ) ,

Example answer:
{"entities": []}

Example input:
Sentence: 20×10 ( 6 ) M ( - 1 ) with higher number of binding sites of 6 .

Example answer:
{"entities": [{"text": "binding sites", "type": "SpatialConcept"}]}

Example input:
Sentence: 95 × 10 ( - 3 ) ; combined p = 2 . 26 × 10 ( - 6 ) , 4 . 86 × 10 ( - 6 ) and 1 . 15 × 10 ( - 5 ) , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 1 × 10 ( - 4 ) ) .

Example answer:
{"entities": []}

Example input:
Sentence: 14 to 5 . 03 .

Example answer:
{"entities": []}

Example input:
Sentence: 0 × 10 ( 2 ) to 5 .

Example answer:
{"entities": []}

Example input:
Sentence: 3593×10 ( 4 ) - 1 . 6795×10 ( 4 ) ) , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 5 x 0 . 5 x 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 0 × 10 ( - 5 ) .

Example answer:
{"entities": []}

Input:
Sentence: 5 x 14 . 0 x 10 .

## Item MedMentions:test:4610
Example input:
Sentence: 5 % of the patients and 38 .

Example answer:
{"entities": []}

Example input:
Sentence: 4 % ( 32 / 239 ) of patients .

Example answer:
{"entities": []}

Example input:
Sentence: 57 . 7 % of patients ( 30 / 52 , 95 % CI 43 . 2 - 71 .

Example answer:
{"entities": []}

Example input:
Sentence: 7 % of patients .

Example answer:
{"entities": []}

Example input:
Sentence: 9 % ) , 40 ( 19 . 9 % ) patients respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 6 % of the patients .

Example answer:
{"entities": []}

Example input:
Sentence: 6 % of the patients .

Example answer:
{"entities": []}

Example input:
Sentence: 6 % of the patients .

Example answer:
{"entities": []}

Example input:
Sentence: 6 % ( 16 / 45 patients ) .

Example answer:
{"entities": []}

Example input:
Sentence: 7 % , respectively of patients .

Example answer:
{"entities": []}

Input:
Sentence: 6 % of the patients , respectively ( P < 0 . 001 ) .

## Item MedMentions:test:4318
Example input:
Sentence: The changes in the average foveal ( 1 mm ) thickness and the foveal areas within 500 μm from the foveal center were measured .

Example answer:
{"entities": [{"text": "foveal", "type": "AnatomicalStructure"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "center", "type": "SpatialConcept"}]}

Example input:
Sentence: Secondary measures were change in best - corrected visual acuity ( BCVA ) and central retinal thickness ( CRT ) by spectral - domain optical coherence tomography at 3 months after treatment .

Example answer:
{"entities": [{"text": "best - corrected visual acuity", "type": "Finding"}, {"text": "BCVA", "type": "Finding"}, {"text": "central retinal thickness", "type": "Finding"}, {"text": "CRT", "type": "Finding"}, {"text": "spectral - domain optical coherence tomography", "type": "MedicalDevice"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The amount of intrinsic blur increased for retinal eccentricities beyond 4 ° ( p < 0 . 001 ) and was lower in binocular than monocular conditions ( p < 0 . 001 ) , but was similar across refractive groups ( p = 0 . 47 ) .

Example answer:
{"entities": [{"text": "intrinsic", "type": "SpatialConcept"}, {"text": "binocular", "type": "BiologicFunction"}, {"text": "monocular", "type": "BiologicFunction"}]}

Example input:
Sentence: Relative to the corresponding centre zone , the outermost zones of the 1200 - mm and flat settings showed a decrease of 8 % - 37 % in legibility , whereas those of the flat setting showed an increase of 26 % - 45 % in perceived visual fatigue .

Example answer:
{"entities": [{"text": "centre", "type": "SpatialConcept"}, {"text": "zone", "type": "SpatialConcept"}, {"text": "zones", "type": "SpatialConcept"}, {"text": "flat", "type": "SpatialConcept"}, {"text": "settings", "type": "SpatialConcept"}, {"text": "setting", "type": "SpatialConcept"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "visual fatigue", "type": "BiologicFunction"}]}

Example input:
Sentence: The remaining reasons were endophthalmitis in 6 cases ( 8 . 7 % ) , posterior capsular opacity in 3 eyes ( 4 . 3 % ) , and impacting retinal surgery operation in 2 cases ( 2 . 9 % ) .

Example answer:
{"entities": [{"text": "endophthalmitis", "type": "BiologicFunction"}, {"text": "posterior capsular opacity", "type": "BiologicFunction"}, {"text": "eyes", "type": "AnatomicalStructure"}, {"text": "retinal surgery operation", "type": "HealthCareActivity"}]}

Example input:
Sentence: At the 4 - week follow - up , 84 . 04 % of the eyes showed increased VA of 1 line or more ( P = .001 ) .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "eyes", "type": "AnatomicalStructure"}, {"text": "VA", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Increase in average foveal thickness after internal limiting membrane peeling To report the findings in three cases in which the average foveal thickness was increased after a thin epiretinal membrane ( ERM ) was removed by vitrectomy with internal limiting membrane ( ILM ) peeling .

Example answer:
{"entities": [{"text": "internal limiting membrane peeling", "type": "HealthCareActivity"}, {"text": "findings", "type": "Finding"}, {"text": "epiretinal membrane", "type": "AnatomicalStructure"}, {"text": "ERM", "type": "AnatomicalStructure"}, {"text": "vitrectomy", "type": "HealthCareActivity"}, {"text": "internal limiting membrane", "type": "AnatomicalStructure"}, {"text": "ILM", "type": "AnatomicalStructure"}, {"text": "peeling", "type": "HealthCareActivity"}]}

Example input:
Sentence: The increase in the average foveal thickness and the inner and outer foveal areas suggests that a centripetal movement of the inner and outer retinal layers toward the foveal center probably occurred due to the ILM peeling .

Example answer:
{"entities": [{"text": "inner", "type": "SpatialConcept"}, {"text": "outer", "type": "SpatialConcept"}, {"text": "foveal", "type": "AnatomicalStructure"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "movement", "type": "BiologicFunction"}, {"text": "retinal", "type": "AnatomicalStructure"}, {"text": "layers", "type": "AnatomicalStructure"}, {"text": "center", "type": "SpatialConcept"}, {"text": "ILM peeling", "type": "HealthCareActivity"}]}

Example input:
Sentence: The average foveal thickness and the inner and outer foveal areas increased significantly after the surgery in each of the three cases .

Example answer:
{"entities": [{"text": "inner", "type": "SpatialConcept"}, {"text": "outer", "type": "SpatialConcept"}, {"text": "foveal", "type": "AnatomicalStructure"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "after the surgery", "type": "Finding"}]}

Example input:
Sentence: The percentage increase in the average foveal thickness relative to the baseline thickness was 26 % in Case 1 , 29 % in Case 2 , and 31 % in Case 3 .

Example answer:
{"entities": []}

Input:
Sentence: The percentage increase in the foveal inner retinal area was 71 % in Case 1 , 113 % in Case 2 , and 110 % in Case 3 , and the percentage increase in foveal outer retinal area was 8 % in Case 1 , 13 % in Case 2 , and 18 % in Case 3 .

## Item MedMentions:test:4144
Example input:
Sentence: SBS rats also demonstrated a significant three - to fourfold decrease in SMO , GIL , and PTCH mRNA , and protein levels ( determined by Real - Time PCR and Western blot ) compared to control animals .

Example answer:
{"entities": [{"text": "SBS", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}, {"text": "SMO", "type": "Chemical"}, {"text": "GIL", "type": "Chemical"}, {"text": "PTCH", "type": "Chemical"}, {"text": "mRNA", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}, {"text": "Real - Time PCR", "type": "ResearchActivity"}, {"text": "Western blot", "type": "HealthCareActivity"}, {"text": "control animals", "type": "Eukaryote"}]}

Example input:
Sentence: Injection of BALB / c mice with 2 , 6 , 10 , 14 - tetramethylpentadecane ( TMPD ) , commonly known as pristane , also results in the development of SLE - like disease .

Example answer:
{"entities": [{"text": "Injection", "type": "HealthCareActivity"}, {"text": "BALB / c mice", "type": "Eukaryote"}, {"text": "2 , 6 , 10 , 14 - tetramethylpentadecane", "type": "Chemical"}, {"text": "TMPD", "type": "Chemical"}, {"text": "pristane", "type": "Chemical"}, {"text": "SLE - like disease", "type": "BiologicFunction"}]}

Example input:
Sentence: In conclusion , our results show that polyacrylate derivative of peroxovanadate efficiently arrests growth of A549 cancerous cells by activating the axis of Rac1 - NADPH oxidase leading to oxidative stress and DNA damage .

Example answer:
{"entities": [{"text": "polyacrylate", "type": "Chemical"}, {"text": "peroxovanadate", "type": "Chemical"}, {"text": "arrests growth", "type": "BiologicFunction"}, {"text": "A549", "type": "AnatomicalStructure"}, {"text": "cancerous cells", "type": "AnatomicalStructure"}, {"text": "axis", "type": "SpatialConcept"}, {"text": "Rac1", "type": "Chemical"}, {"text": "NADPH oxidase", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "DNA damage", "type": "BiologicFunction"}]}

Example input:
Sentence: Intravitreal injection of Zn ( 2 + ) chelators enables many RGCs to survive for months after nerve injury and regenerate axons , and enhances the prosurvival and regenerative effects of deleting the gene for phosphatase and tensin homolog ( pten ) .

Example answer:
{"entities": [{"text": "Zn ( 2 + )", "type": "Chemical"}, {"text": "chelators", "type": "Chemical"}, {"text": "RGCs", "type": "AnatomicalStructure"}, {"text": "survive", "type": "BiologicFunction"}, {"text": "nerve injury", "type": "InjuryOrPoisoning"}, {"text": "axons", "type": "AnatomicalStructure"}, {"text": "prosurvival", "type": "BiologicFunction"}, {"text": "regenerative", "type": "BiologicFunction"}, {"text": "deleting the gene", "type": "BiologicFunction"}, {"text": "phosphatase and tensin homolog", "type": "Chemical"}, {"text": "pten", "type": "Chemical"}]}

Example input:
Sentence: 17β - Estradiol ( E2 ) administration , not Progesterone ( P4 ) , to OVX female stress mice , mitigated despair and enhanced hedonic capacity with an increased expression of BDNF in PFC .

Example answer:
{"entities": [{"text": "17β - Estradiol", "type": "Chemical"}, {"text": "E2", "type": "Chemical"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "Progesterone", "type": "Chemical"}, {"text": "P4", "type": "Chemical"}, {"text": "stress", "type": "Finding"}, {"text": "mice", "type": "Eukaryote"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "BDNF", "type": "Chemical"}, {"text": "PFC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We reported previously that recombinant protein transduction domain ( PTD ) - Cu / Zn SOD effectively scavenged excessive ROS and prevented cardiomyocytes from hypoxia - reoxygenation damage .

Example answer:
{"entities": [{"text": "reported", "type": "IntellectualProduct"}, {"text": "recombinant", "type": "Chemical"}, {"text": "protein transduction domain", "type": "SpatialConcept"}, {"text": "PTD", "type": "SpatialConcept"}, {"text": "Cu / Zn SOD", "type": "Chemical"}, {"text": "scavenged", "type": "BiologicFunction"}, {"text": "ROS", "type": "Chemical"}, {"text": "cardiomyocytes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Recombinant protein transduction domain - Cu / Zn superoxide dismutase alleviates bone cancer pain via peroxiredoxin 4 modulation and antioxidation Bone cancer pain ( BCP ) is a serious chronic clinical condition and reactive oxygen species ( ROS ) were considered to be involved in its development and persistency .

Example answer:
{"entities": [{"text": "Recombinant", "type": "Chemical"}, {"text": "protein transduction domain", "type": "SpatialConcept"}, {"text": "Cu / Zn superoxide dismutase", "type": "Chemical"}, {"text": "bone cancer", "type": "BiologicFunction"}, {"text": "pain", "type": "Finding"}, {"text": "peroxiredoxin 4", "type": "Chemical"}, {"text": "modulation", "type": "BiologicFunction"}, {"text": "antioxidation", "type": "BiologicFunction"}, {"text": "Bone cancer", "type": "BiologicFunction"}, {"text": "BCP", "type": "Finding"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "ROS", "type": "Chemical"}]}

Example input:
Sentence: Our data suggested that reactive oxygen species , at least in part , play a role in cancer metastatic pain development and persistency which can be attenuated by the adminstration of recombinant PTD - Cu / Zn SOD via the peroxiredoxin 4 modulation from oxidative stress .

Example answer:
{"entities": [{"text": "reactive oxygen species", "type": "Chemical"}, {"text": "cancer metastatic", "type": "BiologicFunction"}, {"text": "pain", "type": "Finding"}, {"text": "recombinant PTD", "type": "Chemical"}, {"text": "Cu / Zn SOD", "type": "Chemical"}, {"text": "peroxiredoxin 4", "type": "Chemical"}, {"text": "modulation", "type": "BiologicFunction"}, {"text": "oxidative stress", "type": "BiologicFunction"}]}

Example input:
Sentence: In the current study , we found that an implanted carcinoma in the rat tibia induced remarkable hyperalgesia , increased H2O2 levels and decreased SOD and peroxiredoxin 4 levels .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "found", "type": "Finding"}, {"text": "implanted", "type": "MedicalDevice"}, {"text": "carcinoma", "type": "BiologicFunction"}, {"text": "rat", "type": "Eukaryote"}, {"text": "tibia", "type": "AnatomicalStructure"}, {"text": "hyperalgesia", "type": "Finding"}, {"text": "H2O2", "type": "Chemical"}, {"text": "SOD", "type": "Chemical"}, {"text": "peroxiredoxin 4", "type": "Chemical"}]}

Example input:
Sentence: In addition , an increased expression of N - methyl - d - aspartic acid ( NMDA ) receptors and a decreased expression of γ - aminobutyric acid ( GABA ) receptors in this cancer pain were prevented by PTD - Cu / Zn SOD administration or peroxiredoxin 4 overexpression .

Example answer:
{"entities": [{"text": "N - methyl - d - aspartic acid ( NMDA ) receptors", "type": "Chemical"}, {"text": "γ - aminobutyric acid ( GABA ) receptors", "type": "Chemical"}, {"text": "cancer pain", "type": "Finding"}, {"text": "PTD", "type": "SpatialConcept"}, {"text": "Cu / Zn SOD", "type": "Chemical"}, {"text": "peroxiredoxin 4", "type": "Chemical"}, {"text": "overexpression", "type": "BiologicFunction"}]}

Input:
Sentence: After administration of recombinant PTD - Cu / Zn SOD to these tumor - burden rats , their hyperalgesia was significantly attenuated and peroxiredoxin 4 expression was significantly increased .

## Item MedMentions:test:4260
Example input:
Sentence: Transcriptome profiling by RNA - sequencing determined the genome -wide patterns of expression of virulence factors both in vitro ( potato dextrose agar or medium amended with grape wood as substrate ) and in planta .

Example answer:
{"entities": [{"text": "Transcriptome profiling", "type": "HealthCareActivity"}, {"text": "RNA - sequencing", "type": "HealthCareActivity"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "virulence factors", "type": "Chemical"}, {"text": "potato", "type": "Food"}, {"text": "dextrose agar", "type": "Chemical"}, {"text": "medium", "type": "Chemical"}, {"text": "grape", "type": "Food"}, {"text": "planta", "type": "Eukaryote"}]}

Example input:
Sentence: Inverse PCR of DNA isolated from Sf9 L5814 cellular DNA revealed integration of SfRV sequences in the cellular genome .

Example answer:
{"entities": [{"text": "Inverse PCR", "type": "HealthCareActivity"}, {"text": "DNA", "type": "Chemical"}, {"text": "Sf9 L5814 cellular", "type": "AnatomicalStructure"}, {"text": "integration", "type": "BiologicFunction"}, {"text": "SfRV", "type": "Virus"}, {"text": "sequences", "type": "SpatialConcept"}, {"text": "cellular", "type": "AnatomicalStructure"}, {"text": "genome", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Although delayed SIV acquisition did not predict subsequent viral control , alterations existed in the distribution of plasma cells and plasmablasts between macaques that exhibited high or low viremia .

Example answer:
{"entities": [{"text": "SIV", "type": "Virus"}, {"text": "plasma cells", "type": "AnatomicalStructure"}, {"text": "plasmablasts", "type": "AnatomicalStructure"}, {"text": "macaques", "type": "Eukaryote"}, {"text": "viremia", "type": "BiologicFunction"}]}

Example input:
Sentence: Analysis of C9orf72 KO , SMCR8 KO , and double - KO cell lines revealed phenotypes that are consistent with a function for C9orf72 at lysosomes .

Example answer:
{"entities": [{"text": "Analysis", "type": "ResearchActivity"}, {"text": "C9orf72", "type": "AnatomicalStructure"}, {"text": "KO", "type": "BiologicFunction"}, {"text": "SMCR8", "type": "AnatomicalStructure"}, {"text": "KO ,", "type": "BiologicFunction"}, {"text": "double - KO", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "function", "type": "BiologicFunction"}, {"text": "C9orf72", "type": "Chemical"}, {"text": "lysosomes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We performed an extensive analysis of our Sf9 cell bank ( ATCC CRL - 1711 lot 5814 [ Sf9L5814 ] ) to determine whether this virus was already present in cells obtained from ATCC in 1987 .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "Sf9", "type": "AnatomicalStructure"}, {"text": "cell bank", "type": "IntellectualProduct"}, {"text": "ATCC CRL - 1711 lot 5814", "type": "AnatomicalStructure"}, {"text": "Sf9L5814", "type": "AnatomicalStructure"}, {"text": "virus", "type": "Virus"}, {"text": "present", "type": "Finding"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "ATCC", "type": "Organization"}]}

Example input:
Sentence: In conclusion , the current findings demonstrated that Us3 and Us9 play an important role in the invasion of BHV - 1 through the BM of the respiratory mucosa , which shows the way forward for research -based attenuation of viruses in order to make safer and better - performing vaccines .

Example answer:
{"entities": [{"text": "findings", "type": "ResearchActivity"}, {"text": "Us3", "type": "AnatomicalStructure"}, {"text": "Us9", "type": "AnatomicalStructure"}, {"text": "invasion", "type": "Finding"}, {"text": "BHV - 1", "type": "Virus"}, {"text": "BM", "type": "AnatomicalStructure"}, {"text": "respiratory mucosa", "type": "AnatomicalStructure"}, {"text": "research", "type": "ResearchActivity"}, {"text": "viruses", "type": "Virus"}, {"text": "vaccines", "type": "Chemical"}]}

Example input:
Sentence: We performed RNA - Sequencing ( RNA - Seq ) of 2 EV populations and identified a small fraction of transcripts that were expressed at significantly different levels in large oncosomes and exosomes , suggesting they may mediate specialized functions .

Example answer:
{"entities": [{"text": "EV populations", "type": "AnatomicalStructure"}, {"text": "transcripts", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "oncosomes", "type": "AnatomicalStructure"}, {"text": "exosomes", "type": "AnatomicalStructure"}, {"text": "functions", "type": "BiologicFunction"}]}

Example input:
Sentence: SCC9 cells were plated on Transwell ® membranes that were either coated or not coated with Matrigel and were then co - cultured with SAOS - 2 cells during the peak of OPN expression .

Example answer:
{"entities": [{"text": "SCC9 cells", "type": "AnatomicalStructure"}, {"text": "Matrigel", "type": "Chemical"}, {"text": "co - cultured", "type": "HealthCareActivity"}, {"text": "SAOS - 2 cells", "type": "AnatomicalStructure"}, {"text": "OPN", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}]}

Example input:
Sentence: After treating the cells with the nanovector , we were able to distinguish three different cell populations from different cell lines ( cancer HeLa and PC - 3 , and normal HaCaT lines ) , suitably chosen for their different expressions of folate binding proteins .

Example answer:
{"entities": [{"text": "treating the cells", "type": "AnatomicalStructure"}, {"text": "different cell lines", "type": "AnatomicalStructure"}, {"text": "cancer HeLa", "type": "AnatomicalStructure"}, {"text": "PC - 3", "type": "BiologicFunction"}, {"text": "normal HaCaT lines", "type": "AnatomicalStructure"}, {"text": "folate binding proteins", "type": "Chemical"}]}

Example input:
Sentence: Complete study demonstrating the absence of rhabdovirus in a distinct Sf9 cell line A putative novel rhabdovirus ( SfRV ) was previously identified in a Spodoptera frugiperda cell line ( Sf9 cells [ ATCC CRL - 1711 lot 58078522 ] ) by next generation sequencing and extensive bioinformatic analysis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "rhabdovirus", "type": "Virus"}, {"text": "SfRV", "type": "Virus"}, {"text": "Sf9 cells", "type": "AnatomicalStructure"}, {"text": "ATCC CRL - 1711 lot 58078522", "type": "AnatomicalStructure"}, {"text": "next generation sequencing", "type": "ResearchActivity"}, {"text": "bioinformatic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "analysis", "type": "ResearchActivity"}]}

Input:
Sentence: This study highlights how cell lines with different lineages may present different virosomes and therefore no general conclusions can be drawn across Sf9 cells from different laboratories .

## Item MedMentions:test:4519
Example input:
Sentence: The aim of this study is to identify the prevalence and presentation of TB among Sudanese maintenance HD patients .

Example answer:
{"entities": [{"text": "TB", "type": "BiologicFunction"}, {"text": "Sudanese", "type": "PopulationGroup"}, {"text": "HD", "type": "HealthCareActivity"}]}

Example input:
Sentence: Among children ( N = 455 ) evaluated for presumptive TB , 70 . 3 % ( 320 / 455 ) had Xpert and 62 .

Example answer:
{"entities": [{"text": "Xpert", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here , in the intervention period , July 2013 - June 2015 , contact investigation beyond household was conducted : all people staying within a radius of 50 metres ( using Geographical Information System ) from the household of smear positive TB patients were screened for tuberculosis .

Example answer:
{"entities": [{"text": "intervention", "type": "HealthCareActivity"}, {"text": "investigation", "type": "HealthCareActivity"}, {"text": "people", "type": "PopulationGroup"}, {"text": "Geographical Information System", "type": "IntellectualProduct"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "screened", "type": "HealthCareActivity"}, {"text": "tuberculosis", "type": "BiologicFunction"}]}

Example input:
Sentence: The socio - economic status of households with TB cases was lower .

Example answer:
{"entities": [{"text": "TB", "type": "BiologicFunction"}]}

Example input:
Sentence: A total of 783043 contacts were screened for tuberculosis : 23741 ( 3 . 0 % ) presumptive TB patients were identified of whom , 4710 ( 19 . 8 % ) all forms and 4084 ( 17 . 2 % ) bacteriologically confirmed TB patients were detected .

Example answer:
{"entities": [{"text": "screened", "type": "HealthCareActivity"}, {"text": "tuberculosis", "type": "BiologicFunction"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "bacteriologically", "type": "Finding"}, {"text": "detected", "type": "HealthCareActivity"}]}

Example input:
Sentence: This finding did not support the hypothesis that malnourishment was an important causative factor for the development of active TB among patients in this study .

Example answer:
{"entities": [{"text": "finding", "type": "Finding"}, {"text": "malnourishment", "type": "BiologicFunction"}, {"text": "causative factor", "type": "Finding"}, {"text": "active TB", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: A cross - sectional study comparing nutritional and socio - economic status of all newly diagnosed patients with TB in 2014 with household contacts ( persons residing in the household of TB cases ) and random controls .

Example answer:
{"entities": [{"text": "cross - sectional study", "type": "ResearchActivity"}, {"text": "nutritional", "type": "Finding"}, {"text": "TB", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients with TB had 22 % ( 95 % CI 19 - 25 ) lower body weight , 22 % ( 95 % CI 20 - 25 ) lower body mass index and 22 % ( 95 % CI 19 - 24 ) lower mid - upper arm circumference than healthy controls ( P < 0 . 001 ) ; household contacts and healthy controls were comparable for all measures .

Example answer:
{"entities": [{"text": "TB", "type": "BiologicFunction"}, {"text": "lower body weight", "type": "Finding"}, {"text": "lower body mass index", "type": "Finding"}, {"text": "lower mid - upper arm circumference", "type": "Finding"}]}

Example input:
Sentence: We did not find a higher prevalence of malnourishment in households with TB cases .

Example answer:
{"entities": [{"text": "malnourishment", "type": "BiologicFunction"}, {"text": "TB", "type": "BiologicFunction"}]}

Example input:
Sentence: Low prevalence of malnourishment among household contacts of patients with tuberculosis in Guinea - Bissau An urban demographic surveillance site in Bissau , the capital of Guinea - Bissau , West Africa .BACKGROUND We hypothesised that if previous malnutrition plays a part in acquiring active tuberculosis ( TB ) disease , households of TB cases would have a higher prevalence of malnutrition than those of healthy controls .

Example answer:
{"entities": [{"text": "malnourishment", "type": "BiologicFunction"}, {"text": "tuberculosis", "type": "BiologicFunction"}, {"text": "Guinea - Bissau", "type": "SpatialConcept"}, {"text": "urban", "type": "SpatialConcept"}, {"text": "demographic surveillance", "type": "ResearchActivity"}, {"text": "site", "type": "SpatialConcept"}, {"text": "Bissau", "type": "SpatialConcept"}, {"text": "West Africa", "type": "SpatialConcept"}, {"text": "malnutrition", "type": "BiologicFunction"}, {"text": "active tuberculosis", "type": "BiologicFunction"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}]}

Input:
Sentence: Prevalence of malnutrition was 5 % in household contacts and healthy controls , and 51 % in patients with TB .

## Item MedMentions:test:4342
Example input:
Sentence: Relationship between Occupational Stress , 5 - HT2A Receptor Polymorphisms and Mental Health in Petroleum Workers in the Xinjiang Arid Desert : A Cross - Sectional Study At present , there is growing interest in research examining the relationship between occupational stress and mental health .

Example answer:
{"entities": [{"text": "5 - HT2A Receptor", "type": "Chemical"}, {"text": "Mental Health", "type": "BiologicFunction"}, {"text": "Petroleum Workers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Xinjiang", "type": "SpatialConcept"}, {"text": "Arid Desert", "type": "SpatialConcept"}, {"text": "Cross - Sectional Study", "type": "ResearchActivity"}, {"text": "research", "type": "ResearchActivity"}, {"text": "mental health", "type": "BiologicFunction"}]}

Example input:
Sentence: A 3 - month intervention of high - intensity aerobic training reduces risk factors for type 2 .diabetes and cardiovascular disease to a similar extent in late premenopausal and early postmenopausal women .

Example answer:
{"entities": [{"text": "intervention", "type": "HealthCareActivity"}, {"text": "risk factors", "type": "Finding"}, {"text": "type 2 .diabetes", "type": "BiologicFunction"}, {"text": "cardiovascular disease", "type": "BiologicFunction"}, {"text": "premenopausal", "type": "Finding"}, {"text": "postmenopausal", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: We sought to evaluate risk factors for type 2 diabetes and cardiovascular disease in late premenopausal and early postmenopausal women , matched by age and body composition , and investigate the effect of high - intensity training .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "risk factors", "type": "Finding"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "cardiovascular disease", "type": "BiologicFunction"}, {"text": "premenopausal", "type": "Finding"}, {"text": "postmenopausal", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Individuals with T2DM may be at higher risk of developing periodontal disease .

Example answer:
{"entities": [{"text": "Individuals", "type": "PopulationGroup"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "periodontal disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Multivariate logistic regression models were used to estimate the association between job strain and T2DM .

Example answer:
{"entities": [{"text": "Multivariate logistic regression models", "type": "IntellectualProduct"}, {"text": "job strain", "type": "Finding"}, {"text": "T2DM", "type": "BiologicFunction"}]}

Example input:
Sentence: Results from a cohort of Danish men born in 1953 Exposure to psychosocial stress is associated with increased risk of a number of somatic and mental disorders with relation to immune system functioning .

Example answer:
{"entities": [{"text": "cohort", "type": "PopulationGroup"}, {"text": "Danish men", "type": "PopulationGroup"}, {"text": "born", "type": "BiologicFunction"}, {"text": "stress", "type": "Finding"}, {"text": "mental disorders", "type": "BiologicFunction"}, {"text": "immune system", "type": "BodySystem"}]}

Example input:
Sentence: High job strain was associated with T2DM occurrence amongst the 60 - year - old cohort ( OR = 3 .

Example answer:
{"entities": [{"text": "job strain", "type": "Finding"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "old cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: This study examined whether high work stress increased the risk of T2DM risk in later life , accounting also for other sources of stress outside work , such as burden from household chores .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "examined", "type": "Finding"}, {"text": "work stress", "type": "Finding"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "sources", "type": "Finding"}, {"text": "stress", "type": "Finding"}]}

Example input:
Sentence: Work - related psychosocial stress and the risk of type 2 diabetes in later life Although work - related psychosocial stress and type 2 diabetes mellitus ( T2DM ) have been investigated , the association between lifelong work stress and T2DM in later life remains unclear .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "type 2 diabetes mellitus", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "work stress", "type": "Finding"}]}

Example input:
Sentence: When taking into account household chores load , a more pronounced risk of T2DM was associated with high job strain in combination with heavy household chores load in women aged 60 years at baseline ( OR = 9 . 45 , 95 % CI : 1 . 17 - 76 . 53 ) .

Example answer:
{"entities": [{"text": "T2DM", "type": "BiologicFunction"}, {"text": "job strain", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}]}

Input:
Sentence: Work - related psychosocial stress may increase the risk of T2DM only amongst women in their early 60s .

## Item MedMentions:test:4192
Example input:
Sentence: After the GO - Fe3O4 / SiO2 / AuNWs / L - Cys composites were applied to glycopeptide enrichment , 26 glycopeptides from a human IgG digest could be identified , with a detection limit as low as 10 fmol .

Example answer:
{"entities": [{"text": "GO", "type": "Chemical"}, {"text": "Fe3O4", "type": "Chemical"}, {"text": "SiO2", "type": "Chemical"}, {"text": "L - Cys", "type": "Chemical"}, {"text": "glycopeptide", "type": "Chemical"}, {"text": "glycopeptides", "type": "Chemical"}, {"text": "human IgG", "type": "Chemical"}]}

Example input:
Sentence: Secreted Ectodomain of Sialic Acid - Binding Ig - Like Lectin - 9 and Monocyte Chemoattractant Protein - 1 Synergistically Regenerate Transected Rat Peripheral Nerves by Altering Macrophage Polarity Peripheral nerves ( PNs ) exhibit remarkable self - repairing reparative activity after a simple crush or cut injury .

Example answer:
{"entities": [{"text": "Secreted", "type": "BiologicFunction"}, {"text": "Ectodomain", "type": "SpatialConcept"}, {"text": "Sialic Acid - Binding Ig - Like Lectin - 9", "type": "Chemical"}, {"text": "Monocyte Chemoattractant Protein - 1", "type": "Chemical"}, {"text": "Rat", "type": "Eukaryote"}, {"text": "Peripheral Nerves", "type": "AnatomicalStructure"}, {"text": "Macrophage", "type": "AnatomicalStructure"}, {"text": "Polarity", "type": "SpatialConcept"}, {"text": "Peripheral nerves", "type": "AnatomicalStructure"}, {"text": "PNs", "type": "AnatomicalStructure"}, {"text": "repairing", "type": "BiologicFunction"}, {"text": "reparative activity", "type": "BiologicFunction"}, {"text": "crush", "type": "HealthCareActivity"}, {"text": "cut injury", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using the activatory Gq - coupled human M3 muscarinic receptor ( hM3Dq ) , we found that chemogenetic stimulation of dSPNs mimicked , while stimulation of iSPNs abolished the therapeutic action of L - DOPA in PD mice .

Example answer:
{"entities": [{"text": "activatory Gq - coupled human M3 muscarinic receptor", "type": "Chemical"}, {"text": "hM3Dq", "type": "Chemical"}, {"text": "chemogenetic stimulation", "type": "BiologicFunction"}, {"text": "dSPNs", "type": "AnatomicalStructure"}, {"text": "stimulation", "type": "BiologicFunction"}, {"text": "iSPNs", "type": "AnatomicalStructure"}, {"text": "therapeutic action", "type": "BiologicFunction"}, {"text": "L - DOPA", "type": "Chemical"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: In contrast , SHED - CM specifically depleted of a set of anti - inflammatory M2 macrophage inducers , monocyte chemoattractant protein - 1 ( MCP - 1 ) and the secreted ectodomain of sialic acid - binding Ig - like lectin - 9 ( sSiglec - 9 ) lost the ability to restore neurological function in this model .

Example answer:
{"entities": [{"text": "SHED - CM", "type": "AnatomicalStructure"}, {"text": "M2 macrophage", "type": "AnatomicalStructure"}, {"text": "monocyte chemoattractant protein - 1", "type": "Chemical"}, {"text": "MCP - 1", "type": "Chemical"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "ectodomain", "type": "SpatialConcept"}, {"text": "sialic acid - binding Ig - like lectin - 9", "type": "Chemical"}, {"text": "sSiglec - 9", "type": "Chemical"}, {"text": "restore", "type": "HealthCareActivity"}, {"text": "neurological function", "type": "BiologicFunction"}]}

Example input:
Sentence: We recently found N - linked glycosylation of anti - D to be skewed towards low fucosylation , thereby increasing the affinity to IgG - Fc receptor IIIa and IIIb , which correlated with HDFN disease severity .

Example answer:
{"entities": [{"text": "N - linked glycosylation", "type": "BiologicFunction"}, {"text": "anti - D", "type": "Chemical"}, {"text": "fucosylation", "type": "BiologicFunction"}, {"text": "affinity", "type": "BiologicFunction"}, {"text": "IgG - Fc receptor IIIa", "type": "Chemical"}, {"text": "IIIb", "type": "Chemical"}, {"text": "HDFN", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Mucosal IgM Antibody with d - Mannose Affinity in Fugu Takifugu rubripes Is Utilized by a Monogenean Parasite Heterobothrium okamotoi for Host Recognition How parasites recognize their definitive hosts is a mystery ; however , parasitism is reportedly initiated by recognition of certain molecules on host surfaces .

Example answer:
{"entities": [{"text": "Mucosal", "type": "AnatomicalStructure"}, {"text": "IgM Antibody", "type": "Chemical"}, {"text": "d - Mannose", "type": "Chemical"}, {"text": "Fugu Takifugu rubripes", "type": "Eukaryote"}, {"text": "Monogenean", "type": "Eukaryote"}, {"text": "Parasite", "type": "Eukaryote"}, {"text": "Heterobothrium okamotoi", "type": "Eukaryote"}, {"text": "Host Recognition", "type": "BiologicFunction"}, {"text": "parasites", "type": "Eukaryote"}, {"text": "recognize", "type": "BiologicFunction"}, {"text": "recognition", "type": "BiologicFunction"}, {"text": "host surfaces", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Using liquid chromatography - tandem mass spectrometry analysis , proteins contained in the fraction were identified as d - mannose -specific IgM with two d - mannose -binding lectins .

Example answer:
{"entities": [{"text": "liquid chromatography - tandem mass spectrometry analysis", "type": "HealthCareActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "d - mannose", "type": "Chemical"}, {"text": "IgM", "type": "Chemical"}, {"text": "lectins", "type": "Chemical"}]}

Example input:
Sentence: Subsequent immunofluorescent staining experiments showed that fugu d - mannose -specific IgM binds ciliated epidermal cells of oncomiracidium .

Example answer:
{"entities": [{"text": "immunofluorescent staining experiments", "type": "HealthCareActivity"}, {"text": "fugu", "type": "Eukaryote"}, {"text": "d - mannose", "type": "Chemical"}, {"text": "IgM", "type": "Chemical"}, {"text": "ciliated epidermal cells", "type": "AnatomicalStructure"}, {"text": "oncomiracidium", "type": "Eukaryote"}]}

Example input:
Sentence: These observations suggest that deciliation is triggered by binding of fugu IgM to cell surface Ags via Ag binding sites .

Example answer:
{"entities": [{"text": "deciliation", "type": "BiologicFunction"}, {"text": "fugu", "type": "Eukaryote"}, {"text": "IgM", "type": "Chemical"}, {"text": "cell surface Ags", "type": "Chemical"}, {"text": "Ag binding sites", "type": "Chemical"}]}

Example input:
Sentence: Moreover , concentrations of d - mannose - binding IgM in gill mucus were sufficient to induce deciliation in vitro , indicating that H .

Example answer:
{"entities": [{"text": "d - mannose", "type": "Chemical"}, {"text": "IgM", "type": "Chemical"}, {"text": "gill mucus", "type": "BodySubstance"}, {"text": "deciliation", "type": "BiologicFunction"}, {"text": "H .", "type": "Eukaryote"}]}

Input:
Sentence: However , although deciliation was significantly induced by IgM and was inhibited by d - mannose or a specific Ab against fugu IgM , other lectins had no effect , and IgM without d - mannose affinity induced deciliation to a limited degree .

## Item MedMentions:test:4575
Example input:
Sentence: 007 ) and cortical volumetric BMD ( β = 0 . 125 , R ( 2 ) = 1 . 4 % , P = 0 . 007 ) of the tibia as well as areal BMD of the femoral neck ( β = 0 . 102 , R ( 2 ) = 0 .

Example answer:
{"entities": [{"text": "cortical", "type": "AnatomicalStructure"}, {"text": "volumetric BMD", "type": "ClinicalAttribute"}, {"text": "tibia", "type": "AnatomicalStructure"}, {"text": "areal BMD", "type": "ClinicalAttribute"}, {"text": "femoral neck", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 4 mm ( 2 ) ; P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 4E - 06 ) , which was also supported by suggestive evidence in the gene - level analysis ( P = 4 .

Example answer:
{"entities": [{"text": "gene", "type": "AnatomicalStructure"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: 110 , R ( 2 ) = 1 . 1 % , P = 0 . 024 ) , area ( β = 0 .

Example answer:
{"entities": [{"text": "area", "type": "SpatialConcept"}]}

Example input:
Sentence: 4 V vs SHE could be obtained at pH 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 94 ; P = 0 . 001 ) , whereas Latin American participants had a higher risk of cardiovascular death ( hazard ratio 2 .

Example answer:
{"entities": [{"text": "Latin American", "type": "PopulationGroup"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "cardiovascular", "type": "SpatialConcept"}, {"text": "death", "type": "Finding"}]}

Example input:
Sentence: 9 % ) in group B ( P = 0 . 016 ) and at 1 month it was 0 compared to 4 ( 1 . 0 % ) ( P = 0 . 0483 ) .

Example answer:
{"entities": [{"text": "group B", "type": "IntellectualProduct"}]}

Example input:
Sentence: 346 ) and BMI ( β = - 0 .

Example answer:
{"entities": [{"text": "BMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: 05 ) in FBS + OLA , FBS + LNA , or FBS + PAM , whereas that of C / EBPα , C / EBPβ , and ATGL increased ( P < 0 . 05 ) in FBS + OLA or FBS + LNA cells .

Example answer:
{"entities": [{"text": "FBS", "type": "Chemical"}, {"text": "OLA", "type": "Chemical"}, {"text": "LNA", "type": "Chemical"}, {"text": "PAM", "type": "Chemical"}, {"text": "C / EBPα", "type": "AnatomicalStructure"}, {"text": "C / EBPβ", "type": "AnatomicalStructure"}, {"text": "ATGL", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 117±0 . 048 , P < 0 . 001 ) , SAT ( β = - 0 .

Example answer:
{"entities": [{"text": "SAT", "type": "AnatomicalStructure"}]}

Input:
Sentence: 4 , p < 0 . 05 ) and Latina ( β = 3 .

## Item MedMentions:test:4384
Example input:
Sentence: In the cross - sectional analyses behavioural problems were associated with several self - reported wireless device use measures but not operator -recorded mobile phone use measures , concentration capacity was associated with several self - reported and operator -recorded exposures .

Example answer:
{"entities": [{"text": "cross - sectional analyses", "type": "ResearchActivity"}, {"text": "behavioural problems", "type": "BiologicFunction"}, {"text": "self - reported", "type": "IntellectualProduct"}, {"text": "operator", "type": "ProfessionalOrOccupationalGroup"}, {"text": "concentration", "type": "BiologicFunction"}, {"text": "self - reported", "type": "ResearchActivity"}]}

Example input:
Sentence: Gaze to partners was substantially reduced in mobile conversations , but gaze was still used to coordinate conversation via displays of mutual orientation , and conversational performance and content was not different between stationary and mobile conditions .

Example answer:
{"entities": [{"text": "Gaze", "type": "Finding"}, {"text": "partners", "type": "PopulationGroup"}, {"text": "gaze", "type": "Finding"}, {"text": "orientation", "type": "SpatialConcept"}]}

Example input:
Sentence: We manipulated social contingency : children experienced either real - time FaceTime conversations or pre - recorded Videos as the partner taught novel words , actions and patterns .

Example answer:
{"entities": [{"text": "real - time FaceTime", "type": "IntellectualProduct"}, {"text": "words", "type": "IntellectualProduct"}, {"text": "patterns", "type": "SpatialConcept"}]}

Example input:
Sentence: Collision warnings were not associated with significant increases or decreases in the overall likelihood that teen and adult drivers engaged in secondary behaviors or the likelihood of the behaviors at speeds above 25 mph or below 5 mph .

Example answer:
{"entities": [{"text": "Collision", "type": "InjuryOrPoisoning"}, {"text": "teen", "type": "PopulationGroup"}, {"text": "drivers", "type": "PopulationGroup"}]}

Example input:
Sentence: Patient -to - provider and provider -to - provider communication accounted for 16 / 69 ( 23 % ) of events and was the second most common cause .

Example answer:
{"entities": [{"text": "provider", "type": "ProfessionalOrOccupationalGroup"}, {"text": "events", "type": "BiologicFunction"}]}

Example input:
Sentence: Separate models for each of the five most common secondary behaviors also indicated that warnings had no significant effect on the likelihood that each behavior was present .

Example answer:
{"entities": [{"text": "models", "type": "IntellectualProduct"}, {"text": "indicated", "type": "Finding"}, {"text": "present", "type": "Finding"}]}

Example input:
Sentence: The likelihood that at least one secondary behavior was present was not significantly different during period s when drivers received warnings relative to period s without warnings .

Example answer:
{"entities": [{"text": "present", "type": "Finding"}, {"text": "not significantly", "type": "Finding"}, {"text": "drivers", "type": "PopulationGroup"}]}

Example input:
Sentence: At least one secondary behavior was 21 % more likely to be present at speeds below 5 mph relative to speeds above 25 mph ; however , the effect of vehicle speed was not significantly affected by warning presence .

Example answer:
{"entities": [{"text": "present", "type": "Finding"}, {"text": "not significantly", "type": "Finding"}, {"text": "presence", "type": "Finding"}]}

Example input:
Sentence: In an experimental study , pairs were videotaped in four conditions of mobility ( standing still , talking while walking along a straight - line itinerary , talking while walking along a complex itinerary , or walking along a complex itinerary with no conversational task ) .

Example answer:
{"entities": [{"text": "experimental study", "type": "ResearchActivity"}, {"text": "mobility", "type": "Finding"}, {"text": "standing still", "type": "SpatialConcept"}, {"text": "walking along a straight - line itinerary", "type": "HealthCareActivity"}, {"text": "no conversational", "type": "Finding"}]}

Example input:
Sentence: Ten 5 - second video clips were randomly sampled from driving periods at speeds above 25 mph and below 5 mph each week for each driver and coded for the presence of 11 secondary behaviors .

Example answer:
{"entities": [{"text": "video clips", "type": "IntellectualProduct"}, {"text": "randomly sampled", "type": "ResearchActivity"}, {"text": "driver", "type": "PopulationGroup"}, {"text": "presence", "type": "Finding"}]}

Input:
Sentence: At least one secondary behavior was present in 46 % of video clips ; conversing with a passenger ( 17 % ) , personal grooming ( 9 % ) , and cellphone conversation ( 6 % ) were the most common .

## Item MedMentions:test:4264
Example input:
Sentence: T cell -specific suppression of Gcn5 partially protected mice from myelin oligodendrocyte glycoprotein - induced experimental autoimmune encephalomyelitis , an experimental model for human multiple sclerosis .

Example answer:
{"entities": [{"text": "T cell", "type": "AnatomicalStructure"}, {"text": "Gcn5", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "myelin oligodendrocyte glycoprotein", "type": "Chemical"}, {"text": "experimental autoimmune encephalomyelitis", "type": "BiologicFunction"}, {"text": "experimental model", "type": "IntellectualProduct"}, {"text": "human", "type": "Eukaryote"}, {"text": "multiple sclerosis", "type": "BiologicFunction"}]}

Example input:
Sentence: ChIP assay showed that there was a decreasing trend for histone acetylation at the StAR promoter in fetal adrenal glands , whereas H3 acetyl - K14 at the YY1 promoter presented an increasing trend following nicotine exposure .

Example answer:
{"entities": [{"text": "ChIP", "type": "HealthCareActivity"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "decreasing", "type": "Finding"}, {"text": "histone acetylation", "type": "BiologicFunction"}, {"text": "StAR promoter", "type": "AnatomicalStructure"}, {"text": "fetal adrenal glands", "type": "AnatomicalStructure"}, {"text": "H3 acetyl - K14", "type": "BiologicFunction"}, {"text": "YY1 promoter", "type": "AnatomicalStructure"}, {"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: The GCC and ATA haplotypes have been associated with high and low levels of IL - 10 production , respectively .

Example answer:
{"entities": [{"text": "IL - 10", "type": "Chemical"}]}

Example input:
Sentence: Acetylation Modulates IL - 2 Receptor Signaling in T Cells Ligand binding to the cognate cytokine receptors activates intracellular signaling by recruiting protein tyrosine kinases and other protein modification enzymes .

Example answer:
{"entities": [{"text": "Acetylation", "type": "BiologicFunction"}, {"text": "IL - 2 Receptor", "type": "Chemical"}, {"text": "Signaling", "type": "BiologicFunction"}, {"text": "T Cells", "type": "AnatomicalStructure"}, {"text": "Ligand binding", "type": "BiologicFunction"}, {"text": "cytokine receptors", "type": "Chemical"}, {"text": "intracellular signaling", "type": "BiologicFunction"}, {"text": "protein tyrosine kinases", "type": "Chemical"}, {"text": "protein modification", "type": "BiologicFunction"}, {"text": "enzymes", "type": "Chemical"}]}

Example input:
Sentence: Thus , IL - 2 -mediated acetylation plays an important role in the modulation of cytokine signaling and T cell fate .

Example answer:
{"entities": [{"text": "IL - 2", "type": "Chemical"}, {"text": "acetylation", "type": "BiologicFunction"}, {"text": "cytokine signaling", "type": "BiologicFunction"}, {"text": "T cell", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Loss of Gcn5 functions impaired T cell proliferation , IL - 2 production , and Th1 / Th17 , but not Th2 and regulatory T cell differentiation .

Example answer:
{"entities": [{"text": "Loss of", "type": "Finding"}, {"text": "Gcn5", "type": "Chemical"}, {"text": "impaired T cell proliferation", "type": "BiologicFunction"}, {"text": "IL - 2 production", "type": "BiologicFunction"}, {"text": "Th1", "type": "AnatomicalStructure"}, {"text": "Th17", "type": "AnatomicalStructure"}, {"text": "Th2", "type": "AnatomicalStructure"}, {"text": "regulatory T cell differentiation", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study , we conditionally deleted Gcn5 ( encoded by the Kat2a gene ) specifically in T lymphocytes by crossing floxed Gcn5 and Lck - Cre mice , and demonstrated that Gcn5 plays important roles in multiple stages of T cell functions including development , clonal expansion , and differentiation .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "deleted", "type": "BiologicFunction"}, {"text": "Gcn5", "type": "Chemical"}, {"text": "Kat2a gene", "type": "AnatomicalStructure"}, {"text": "T lymphocytes", "type": "AnatomicalStructure"}, {"text": "crossing", "type": "BiologicFunction"}, {"text": "floxed Gcn5", "type": "AnatomicalStructure"}, {"text": "Lck - Cre", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "T cell functions", "type": "BiologicFunction"}, {"text": "development", "type": "BiologicFunction"}, {"text": "clonal expansion", "type": "BiologicFunction"}, {"text": "differentiation", "type": "BiologicFunction"}]}

Example input:
Sentence: As for phosphorylation , IL - 2 induces the acetylation of signaling molecules , including Stat5 , in the murine T cell line CTLL - 2 .

Example answer:
{"entities": [{"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "IL - 2", "type": "Chemical"}, {"text": "acetylation", "type": "BiologicFunction"}, {"text": "signaling molecules", "type": "Chemical"}, {"text": "Stat5", "type": "Chemical"}, {"text": "murine T cell line", "type": "AnatomicalStructure"}, {"text": "CTLL - 2", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Gcn5 is recruited onto the il - 2 promoter by interacting with the NFAT in T cells upon TCR stimulation .

Example answer:
{"entities": [{"text": "Gcn5", "type": "Chemical"}, {"text": "il - 2", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "NFAT", "type": "Chemical"}, {"text": "T cells", "type": "AnatomicalStructure"}, {"text": "TCR stimulation", "type": "BiologicFunction"}]}

Example input:
Sentence: The Histone Acetyltransferase Gcn5 Positively Regulates T Cell Activation Histone acetyltransferases ( HATs ) regulate inducible transcription in multiple cellular processes and during inflammatory and immune response .

Example answer:
{"entities": [{"text": "Histone Acetyltransferase Gcn5", "type": "Chemical"}, {"text": "Positively Regulates T Cell Activation", "type": "BiologicFunction"}, {"text": "Histone acetyltransferases", "type": "Chemical"}, {"text": "HATs", "type": "Chemical"}, {"text": "regulate inducible transcription", "type": "BiologicFunction"}, {"text": "cellular processes", "type": "BiologicFunction"}, {"text": "inflammatory", "type": "BiologicFunction"}, {"text": "immune response", "type": "BiologicFunction"}]}

Input:
Sentence: Interestingly , instead of directly acetylating NFAT , Gcn5 catalyzes histone H3 lysine H9 acetylation to promote IL - 2 production .

## Item MedMentions:test:4508
Example input:
Sentence: The design and conduct of Keep It Off : An online randomized trial of financial incentives for weight - loss maintenance Background Obesity continues to be a serious public health challenge .

Example answer:
{"entities": [{"text": "Keep It Off", "type": "ResearchActivity"}, {"text": "online", "type": "IntellectualProduct"}, {"text": "randomized trial", "type": "ResearchActivity"}, {"text": "Obesity", "type": "BiologicFunction"}, {"text": "public", "type": "Organization"}]}

Example input:
Sentence: At baseline , 24 ( 18 % ) were obese and 36 ( 27 % ) were overweight , 15 became obese ( 69 / 1000 PYFU ) and 22 became overweight ( 163 / 1000 PYFU ) .

Example answer:
{"entities": [{"text": "obese", "type": "BiologicFunction"}, {"text": "overweight", "type": "Finding"}, {"text": "PYFU", "type": "HealthCareActivity"}]}

Example input:
Sentence: Lessons Learned We demonstrated that our pragmatic design was successful in rapid accrual of participants in a trial of interventions to maintain weight loss .

Example answer:
{"entities": [{"text": "Lessons", "type": "IntellectualProduct"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "weight loss", "type": "Finding"}]}

Example input:
Sentence: The primary endpoint was the difference in the rate of weight change over 16 weeks ( linear mixed - effect model for repeated measures ) between high - dose espindolol and placebo .

Example answer:
{"entities": [{"text": "weight change", "type": "Finding"}, {"text": "espindolol", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: A longitudinal , multicentric prospective study was carried out on 771 patients affected by pathological obesity .

Example answer:
{"entities": [{"text": "multicentric prospective study", "type": "ResearchActivity"}, {"text": "obesity", "type": "BiologicFunction"}]}

Example input:
Sentence: Two scenarios for weight loss programmes were considered : a 10 % permanent loss in body weight and a 10 % loss that decays over time .

Example answer:
{"entities": [{"text": "weight loss programmes", "type": "HealthCareActivity"}, {"text": "loss", "type": "Finding"}]}

Example input:
Sentence: After 4 weeks , self - efficacy , health and well - being scores significantly improved : 63 % of lifestyle goals and 89 % of health management goals were fully achieved ; 58 % of referrals to community lifestyle behaviour change services and 79 % of referrals to other services ( e . g .

Example answer:
{"entities": [{"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "significantly improved", "type": "Finding"}, {"text": "goals", "type": "IntellectualProduct"}, {"text": "achieved", "type": "Finding"}, {"text": "referrals to", "type": "HealthCareActivity"}, {"text": "community", "type": "Organization"}, {"text": "services", "type": "HealthCareActivity"}]}

Example input:
Sentence: Eligible participants were those aged 30 - 80 who lost at least 11 lb ( 5 kg ) during the first 4 months of participation in Weight Watchers , a national weight - loss program , with whom we partnered .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "Weight Watchers", "type": "HealthCareActivity"}, {"text": "national weight - loss program", "type": "HealthCareActivity"}]}

Example input:
Sentence: Nearly half of the participants were obese and around 60 % had been on a LCD for ≥ 6 months .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "obese", "type": "BiologicFunction"}, {"text": "LCD", "type": "HealthCareActivity"}]}

Example input:
Sentence: At the 1 - year observation period , obese subjects who did not receive treatment for their obesity experienced longer durations of hospitalisation ( median length : 5 days vs 3 days ) , used more prescription drugs ( 75 . 0 % vs 57 . 7 % ) , required more specialised outpatient healthcare ( mean number : 5 .

Example answer:
{"entities": [{"text": "observation", "type": "ResearchActivity"}, {"text": "obese", "type": "BiologicFunction"}, {"text": "subjects", "type": "PopulationGroup"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "hospitalisation", "type": "HealthCareActivity"}, {"text": "prescription drugs", "type": "Chemical"}, {"text": "healthcare", "type": "HealthCareActivity"}]}

Input:
Sentence: Thirty - five participants with obesity were randomized to lose a similar weight rapidly ( 4 weeks ) or gradually ( 8 weeks ) , and afterwards to maintain it ( 4 weeks ) .

## Item MedMentions:test:4175
Example input:
Sentence: We performed a nested case - control study of more than 8 . 5 million commercially insured adults ( aged ≥18 years ) in all 50 US states , Puerto Rico , and US Virgin Islands in the Verisk Health claims database .

Example answer:
{"entities": [{"text": "nested case - control study", "type": "ResearchActivity"}, {"text": "US states", "type": "SpatialConcept"}, {"text": "Puerto Rico", "type": "SpatialConcept"}, {"text": "US Virgin Islands", "type": "SpatialConcept"}, {"text": "Verisk Health claims database", "type": "IntellectualProduct"}]}

Example input:
Sentence: A retrospective cohort analysis from a single institution across the duration of the study comparing the clinical and financial outcomes of infants ( aged < 32 weeks ) treated under the 2009 AAP guidelines ( PRE ) and infants ( aged > 29 weeks ) managed after the 2014 AAP guidelines ( POST ) took effect .

Example answer:
{"entities": [{"text": "cohort analysis", "type": "ResearchActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "treated", "type": "Finding"}, {"text": "AAP", "type": "Organization"}, {"text": "guidelines", "type": "IntellectualProduct"}, {"text": "AAP guidelines", "type": "IntellectualProduct"}]}

Example input:
Sentence: Based on a review of over 1000 published HPS and POPH articles identified via a MEDLINE search ( 1985 - 2015 ) , clinical guidelines were based on , selected single care reports , small series , registries , databases , and expert opinion .

Example answer:
{"entities": [{"text": "HPS", "type": "BiologicFunction"}, {"text": "POPH", "type": "BiologicFunction"}, {"text": "MEDLINE search", "type": "IntellectualProduct"}, {"text": "clinical guidelines", "type": "IntellectualProduct"}, {"text": "selected single care reports", "type": "HealthCareActivity"}, {"text": "registries", "type": "IntellectualProduct"}, {"text": "databases", "type": "IntellectualProduct"}]}

Example input:
Sentence: This retrospective , hospital - based study was conducted in patients of ALL , admitted to the Clinical Haematology Department of a tertiary care hospital of Odisha from August 2014 to July 2015 .

Example answer:
{"entities": [{"text": "retrospective , hospital - based study", "type": "ResearchActivity"}, {"text": "ALL", "type": "BiologicFunction"}, {"text": "admitted to the Clinical Haematology Department", "type": "HealthCareActivity"}, {"text": "tertiary care hospital", "type": "Organization"}, {"text": "Odisha", "type": "SpatialConcept"}]}

Example input:
Sentence: A health education intervention study was conducted from November 2012 to January 2014 in a rural area of Kuppam , Andhra Pradesh , South India among the people aged 15 years and above .

Example answer:
{"entities": [{"text": "intervention study", "type": "IntellectualProduct"}, {"text": "South India", "type": "SpatialConcept"}, {"text": "people", "type": "PopulationGroup"}]}

Example input:
Sentence: Electronic searches from inception to July 31 , 2016 , were performed using PubMed , Medline OVID , Cochrane Library , EMBASE , CINAHL plus , and PsycINFO .

Example answer:
{"entities": [{"text": "PubMed", "type": "IntellectualProduct"}, {"text": "Medline OVID", "type": "IntellectualProduct"}, {"text": "Cochrane Library", "type": "IntellectualProduct"}, {"text": "EMBASE", "type": "IntellectualProduct"}, {"text": "CINAHL plus", "type": "IntellectualProduct"}]}

Example input:
Sentence: MEDLINE and Web of Science electronic database were searched from January 1990 to December 2015 , using the keywords such as " cervical cancer " , " screening " , " early detection " , " cervical cytology " and " visual inspection " , and their corresponding MeSH terms in combination with Boolean operators " OR , AND . " Two authors independently selected studies that are published in English and conducted in India .

Example answer:
{"entities": [{"text": "MEDLINE", "type": "IntellectualProduct"}, {"text": "keywords", "type": "IntellectualProduct"}, {"text": "cervical cancer", "type": "BiologicFunction"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "early detection", "type": "HealthCareActivity"}, {"text": "cervical cytology", "type": "HealthCareActivity"}, {"text": "visual inspection", "type": "HealthCareActivity"}, {"text": "MeSH terms", "type": "IntellectualProduct"}, {"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "published", "type": "IntellectualProduct"}, {"text": "India", "type": "SpatialConcept"}]}

Example input:
Sentence: We found two documents addressing pre - hospital ACS care .

Example answer:
{"entities": [{"text": "found", "type": "Finding"}, {"text": "documents", "type": "IntellectualProduct"}, {"text": "ACS", "type": "BiologicFunction"}, {"text": "care", "type": "HealthCareActivity"}]}

Example input:
Sentence: Though India has legislation mandating acute care for emergencies such as trauma , regulations or laws to guide pre - hospital ACS care are largely absent .

Example answer:
{"entities": [{"text": "India", "type": "SpatialConcept"}, {"text": "acute care", "type": "HealthCareActivity"}, {"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "laws", "type": "IntellectualProduct"}, {"text": "ACS", "type": "BiologicFunction"}, {"text": "care", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , it is unknown whether guidelines , policies , regulations , or laws exist to guide pre - hospital ACS care in India .

Example answer:
{"entities": [{"text": "guidelines", "type": "IntellectualProduct"}, {"text": "policies", "type": "IntellectualProduct"}, {"text": "laws", "type": "IntellectualProduct"}, {"text": "ACS", "type": "BiologicFunction"}, {"text": "care", "type": "HealthCareActivity"}, {"text": "India", "type": "SpatialConcept"}]}

Input:
Sentence: From November 2014 to May 2016 , we searched for publicly available emergency care guidelines and legislation addressing pre - hospital ACS care in all 29 Indian states and 7 Union Territories via Internet search and direct correspondence .

## Item MedMentions:test:4325
Example input:
Sentence: Substitution of Tyr ( 217 ) with a phosphomimetic residue eliminated PLK1 activity in vitro and in cells .

Example answer:
{"entities": [{"text": "Substitution", "type": "BiologicFunction"}, {"text": "Tyr ( 217 )", "type": "Chemical"}, {"text": "PLK1", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Mutation of 19 potential MRP1 phosphorylation sites revealed that HEK - Tyr920Phe / Ser921Ala - MRP1 transported As ( GS ) 3 like HeLa - WT - MRP1 , whereas individual HEK - Tyr920Phe - and - Ser921Ala - MRP1 mutants were similar to HEK - WT - MRP1 .

Example answer:
{"entities": [{"text": "Mutation", "type": "BiologicFunction"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "sites", "type": "SpatialConcept"}, {"text": "HEK", "type": "AnatomicalStructure"}, {"text": "Tyr920Phe / Ser921Ala - MRP1", "type": "Chemical"}, {"text": "transported", "type": "BiologicFunction"}, {"text": "HeLa - WT", "type": "AnatomicalStructure"}, {"text": "MRP1", "type": "Chemical"}, {"text": "Tyr920Phe -", "type": "Chemical"}, {"text": "Ser921Ala - MRP1", "type": "Chemical"}, {"text": "mutants", "type": "Chemical"}, {"text": "HEK - WT", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Further analysis showed that Tyr ( 217 ) phosphorylation reduced the phosphorylation of Thr ( 210 ) in the activation loop , a phosphorylation event necessary for PLK1 activity .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "Tyr ( 217 )", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "phosphorylation of Thr ( 210 )", "type": "BiologicFunction"}, {"text": "activation loop", "type": "SpatialConcept"}, {"text": "PLK1", "type": "Chemical"}]}

Example input:
Sentence: We identified Polo - like kinase 1 ( PLK1 ) , a major signaling hub in the spindle subnetwork , as phosphorylated at the conserved Tyr ( 217 ) in the kinase domain .

Example answer:
{"entities": [{"text": "Polo - like kinase 1", "type": "Chemical"}, {"text": "PLK1", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "spindle", "type": "AnatomicalStructure"}, {"text": "phosphorylated", "type": "Chemical"}, {"text": "Tyr ( 217 )", "type": "Chemical"}, {"text": "kinase domain", "type": "SpatialConcept"}]}

Example input:
Sentence: PD - 1 expression was associated with reduced phosphorylation of ribosomal protein S6 ( pS6 ) , whereas Tim - 3 expression was associated with increased pS6 .

Example answer:
{"entities": [{"text": "PD - 1", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "ribosomal protein S6", "type": "Chemical"}, {"text": "pS6", "type": "Chemical"}, {"text": "Tim - 3", "type": "Chemical"}]}

Example input:
Sentence: Moreover , in line with its oncogenic activity , we found that TCRP1 is often overexpressed in human in lung cancer , glioma , ovarian cancer , thyroid cancer , nasopharyngeal carcinoma , pancreatic cancer , stomach cancer and tongue carcinoma tissues .

Example answer:
{"entities": [{"text": "oncogenic", "type": "Chemical"}, {"text": "TCRP1", "type": "Chemical"}, {"text": "overexpressed", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "glioma", "type": "BiologicFunction"}, {"text": "ovarian cancer", "type": "BiologicFunction"}, {"text": "thyroid cancer", "type": "BiologicFunction"}, {"text": "nasopharyngeal carcinoma", "type": "BiologicFunction"}, {"text": "pancreatic cancer", "type": "BiologicFunction"}, {"text": "stomach cancer", "type": "BiologicFunction"}, {"text": "tongue carcinoma", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In this study , we showed that TCRP1 overexpression promotes cell transformation and tumorigenesis through hyperphosphorylation of the oncogenic kinase 3 - phosphoinositide - dependent protein kinase - 1 ( PDK1 ) and AKT1 , whereas inhibition of PDK1 by OSU - 03012 or PDK1 small interfering RNA reversed TCRP1 -mediated cell transformation .

Example answer:
{"entities": [{"text": "TCRP1", "type": "Chemical"}, {"text": "overexpression", "type": "BiologicFunction"}, {"text": "cell transformation", "type": "BiologicFunction"}, {"text": "tumorigenesis", "type": "BiologicFunction"}, {"text": "hyperphosphorylation", "type": "BiologicFunction"}, {"text": "oncogenic kinase", "type": "Chemical"}, {"text": "3 - phosphoinositide - dependent protein kinase - 1", "type": "Chemical"}, {"text": "PDK1", "type": "Chemical"}, {"text": "AKT1", "type": "Chemical"}, {"text": "OSU - 03012", "type": "Chemical"}, {"text": "small interfering RNA", "type": "Chemical"}]}

Example input:
Sentence: Thus , TCRP1 may be a candidate as human oncoprotein that promotes cancer development by activation of PDK1 / AKT1 signaling .

Example answer:
{"entities": [{"text": "TCRP1", "type": "Chemical"}, {"text": "human", "type": "Eukaryote"}, {"text": "oncoprotein", "type": "Chemical"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "PDK1", "type": "Chemical"}, {"text": "AKT1", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}]}

Example input:
Sentence: Spearman correlation analysis showed that the expression of TCRP1 has a positive correlation with p - PDK1 , as well as p - AKT1 in lung cancer and gliomas tissues .

Example answer:
{"entities": [{"text": "Spearman correlation analysis", "type": "ResearchActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "TCRP1", "type": "Chemical"}, {"text": "p - PDK1", "type": "Chemical"}, {"text": "p - AKT1", "type": "Chemical"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "gliomas", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: TCRP1 promotes NIH / 3T3 cell transformation by over - activating PDK1 and AKT1 Tongue cancer resistance - related protein 1 ( TCRP1 ) gene was first cloned from the multidrug resistance tongue cancer cell ( Tca8113 / pingyangmycin ) in our lab .

Example answer:
{"entities": [{"text": "TCRP1", "type": "Chemical"}, {"text": "NIH / 3T3 cell", "type": "AnatomicalStructure"}, {"text": "transformation", "type": "BiologicFunction"}, {"text": "over - activating", "type": "BiologicFunction"}, {"text": "PDK1", "type": "Chemical"}, {"text": "AKT1", "type": "Chemical"}, {"text": "Tongue cancer resistance - related protein 1 ( TCRP1 ) gene", "type": "AnatomicalStructure"}, {"text": "cloned", "type": "HealthCareActivity"}, {"text": "tongue cancer", "type": "BiologicFunction"}, {"text": "cell", "type": "AnatomicalStructure"}, {"text": "Tca8113", "type": "AnatomicalStructure"}, {"text": "pingyangmycin", "type": "Chemical"}, {"text": "lab", "type": "Organization"}]}

Input:
Sentence: Importantly , TCRP1 was able to directly interact with PDK1 , and 93 - 107 amino - acid and 109 - 124 amino - acid sites of TCRP1 were the common binding domain of PDK1 .

## Item MedMentions:test:4340
Example input:
Sentence: Participants who developed incident type 2 diabetes were significantly older and had significantly higher body mass index ( BMI ; p = 0 . 012 ) , total cholesterol ( p = 0 . 007 ) , fasting triglycerides ( p < 0 . 001 ) , and Homeostatic Model Assessment of Insulin Resistance ( HOMA - IR ) ( p < 0 .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "type 2 diabetes", "type": "Finding"}, {"text": "significantly older", "type": "PopulationGroup"}, {"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "fasting", "type": "Finding"}, {"text": "triglycerides", "type": "Chemical"}, {"text": "Homeostatic Model Assessment of Insulin Resistance", "type": "HealthCareActivity"}, {"text": "HOMA - IR", "type": "HealthCareActivity"}]}

Example input:
Sentence: Individuals with T2DM may be at higher risk of developing periodontal disease .

Example answer:
{"entities": [{"text": "Individuals", "type": "PopulationGroup"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "periodontal disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Weight loss dieting in overweight and obese individuals with T2D resulted in a reduction in plasma sLR11 levels that was associated with improvements in lipid - profile and glycemic state .

Example answer:
{"entities": [{"text": "Weight loss dieting", "type": "HealthCareActivity"}, {"text": "obese", "type": "BiologicFunction"}, {"text": "T2D", "type": "BiologicFunction"}, {"text": "plasma", "type": "BodySubstance"}, {"text": "sLR11", "type": "Chemical"}, {"text": "lipid - profile", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of this study was to evaluate whether serum TH levels within the reference range are related to T2DM .

Example answer:
{"entities": [{"text": "serum", "type": "BodySubstance"}, {"text": "TH levels", "type": "HealthCareActivity"}, {"text": "T2DM", "type": "BiologicFunction"}]}

Example input:
Sentence: A total of 240 patients with type 2 diabetes ( T2DM ) attending an out - patient medical clinic were randomized to either PPBS or FBS monitoring .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "out - patient medical clinic", "type": "Organization"}, {"text": "randomized", "type": "Finding"}, {"text": "PPBS", "type": "HealthCareActivity"}, {"text": "FBS", "type": "HealthCareActivity"}, {"text": "monitoring", "type": "HealthCareActivity"}]}

Example input:
Sentence: When taking into account household chores load , a more pronounced risk of T2DM was associated with high job strain in combination with heavy household chores load in women aged 60 years at baseline ( OR = 9 . 45 , 95 % CI : 1 . 17 - 76 . 53 ) .

Example answer:
{"entities": [{"text": "T2DM", "type": "BiologicFunction"}, {"text": "job strain", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: 88 for T2DM .

Example answer:
{"entities": [{"text": "T2DM", "type": "BiologicFunction"}]}

Example input:
Sentence: In a cross - sectional survey , relationship between serum levels of 25 - hydroxy vitamin D ( 25 ( OH ) D ) and glycated haemoglobin ( HbA1C ) was examined in 141 type - 2 diabetic patients including 102 males and 39 females ; age range 22 to 70 years , visiting the Aga Khan University Hospital during July 2013 - April 2014 .

Example answer:
{"entities": [{"text": "cross - sectional survey", "type": "ResearchActivity"}, {"text": "serum", "type": "BodySubstance"}, {"text": "levels of 25 - hydroxy vitamin D", "type": "HealthCareActivity"}, {"text": "25 ( OH ) D", "type": "Chemical"}, {"text": "glycated haemoglobin", "type": "HealthCareActivity"}, {"text": "HbA1C", "type": "Chemical"}, {"text": "type - 2 diabetic", "type": "BiologicFunction"}, {"text": "males", "type": "PopulationGroup"}, {"text": "females", "type": "PopulationGroup"}, {"text": "Aga Khan University Hospital", "type": "Organization"}]}

Example input:
Sentence: The prevalence of T2DM was 16 .

Example answer:
{"entities": [{"text": "T2DM", "type": "BiologicFunction"}]}

Example input:
Sentence: Serum free triiodothyronine ( FT3 ) , free thyroxine ( FT4 ) , and thyroid - stimulating hormone ( TSH ) levels were measured by chemiluminescence immunoassay , and T2DM was defined according to the American Diabetes Association criteria .

Example answer:
{"entities": [{"text": "Serum", "type": "BodySubstance"}, {"text": "free triiodothyronine", "type": "Chemical"}, {"text": "FT3", "type": "Chemical"}, {"text": "free thyroxine", "type": "Chemical"}, {"text": "FT4", "type": "Chemical"}, {"text": "thyroid - stimulating hormone ( TSH ) levels", "type": "Finding"}, {"text": "T2DM", "type": "BiologicFunction"}]}

Input:
Sentence: T2DM was ascertained by glycated haemoglobin level , self - report , hypoglycaemic medication use and clinical records .
