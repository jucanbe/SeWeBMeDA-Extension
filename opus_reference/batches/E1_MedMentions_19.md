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

## Item MedMentions:test:3676
Example input:
Sentence: Animals underwent necropsy with blinded histomorphologic evaluation on days 0 , 3 , and 10 postprocedure to assess for presence of bowel perforation , depth of thermal injury , and extent of inflammatory response .

Example answer:
{"entities": [{"text": "Animals", "type": "Eukaryote"}, {"text": "necropsy", "type": "HealthCareActivity"}, {"text": "blinded", "type": "ResearchActivity"}, {"text": "histomorphologic evaluation", "type": "HealthCareActivity"}, {"text": "postprocedure to assess", "type": "Finding"}, {"text": "bowel perforation", "type": "BiologicFunction"}, {"text": "thermal injury", "type": "InjuryOrPoisoning"}, {"text": "inflammatory response", "type": "BiologicFunction"}]}

Example input:
Sentence: Hematologic response was observed in 68 % of patients ( very good partial response or complete response in 29 % ) , as well as improved survival .

Example answer:
{"entities": [{"text": "Hematologic response", "type": "Finding"}, {"text": "partial response", "type": "Finding"}, {"text": "complete response", "type": "Finding"}]}

Example input:
Sentence: Patients treated with radical prostatectomy have been shown to suffer declines in urinary and sexual HRQoL as compared to those managed with active surveillance ( AS ) .

Example answer:
{"entities": [{"text": "treated with", "type": "HealthCareActivity"}, {"text": "radical prostatectomy", "type": "HealthCareActivity"}, {"text": "sexual", "type": "BiologicFunction"}, {"text": "active surveillance", "type": "HealthCareActivity"}, {"text": "AS", "type": "HealthCareActivity"}]}

Example input:
Sentence: Tumor response and patient outcome after preoperative radiotherapy in locally advanced non - inflammatory breast cancer patients The purpose of this analysis was to assess the tumor response and long - term outcome in patients treated with preoperative radiotherapy ( PRT ) without systemic therapy .

Example answer:
{"entities": [{"text": "Tumor response", "type": "Finding"}, {"text": "preoperative radiotherapy", "type": "HealthCareActivity"}, {"text": "locally advanced non - inflammatory breast cancer", "type": "BiologicFunction"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "tumor response", "type": "Finding"}, {"text": "PRT", "type": "HealthCareActivity"}, {"text": "systemic therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: No threshold was found between tumor AD and response ( P > .1 ) .

Example answer:
{"entities": [{"text": "tumor", "type": "BiologicFunction"}]}

Example input:
Sentence: After treatment , histologic examination showed no residual tumor in 6 patients ( complete response [ CR ] ) , stable disease in 2 patients , and progressive disease in 2 patients .

Example answer:
{"entities": [{"text": "histologic examination", "type": "HealthCareActivity"}, {"text": "no residual tumor", "type": "Finding"}, {"text": "complete response", "type": "Finding"}, {"text": "CR", "type": "Finding"}, {"text": "stable disease", "type": "Finding"}, {"text": "progressive disease", "type": "BiologicFunction"}]}

Example input:
Sentence: In parallel , clinical and pathological characteristics of 260 patients who underwent resection of noninvasive IPMN were reviewed to identify risk factors associated with local progression .

Example answer:
{"entities": [{"text": "resection", "type": "HealthCareActivity"}, {"text": "noninvasive IPMN", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "local", "type": "SpatialConcept"}, {"text": "progression", "type": "BiologicFunction"}]}

Example input:
Sentence: Sixteen patients ( 31 % ) had complete pathological response .

Example answer:
{"entities": [{"text": "complete pathological response", "type": "Finding"}]}

Example input:
Sentence: The study cohort was comprised of patients who underwent either no surgery or grossly incomplete resection .

Example answer:
{"entities": [{"text": "resection", "type": "HealthCareActivity"}]}

Example input:
Sentence: Twenty - one patients were not evaluated for radiological response because of death ( n = 16 ) , noncompliance to follow - up ( n = 4 ) , and clinical deterioration ( n = 1 ) .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "radiological", "type": "HealthCareActivity"}, {"text": "response", "type": "Finding"}, {"text": "death", "type": "BiologicFunction"}, {"text": "noncompliance", "type": "Finding"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Input:
Sentence: Pathologic responses were not evaluated in two patients who did not undergo radical resection .

## Item MedMentions:test:3845
Example input:
Sentence: The American College of Surgeons National Surgical Quality Improvement Program is a risk - adjusted dataset analyzing preoperative risk factors , demographics , and 30 - day outcomes .

Example answer:
{"entities": [{"text": "American College of Surgeons", "type": "Organization"}, {"text": "National Surgical Quality Improvement Program", "type": "IntellectualProduct"}, {"text": "risk - adjusted dataset", "type": "IntellectualProduct"}, {"text": "risk factors", "type": "Finding"}]}

Example input:
Sentence: The aim of our study was to validate a modified 15 variable emergency general surgery specific frailty index ( EGSFI ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "validate", "type": "ResearchActivity"}, {"text": "emergency general surgery specific frailty index", "type": "HealthCareActivity"}, {"text": "EGSFI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Management of skin and soft - tissue infections at a community teaching hospital using a severity - of - illness tool Skin and soft - tissue infections ( SSTIs ) encompass a diverse range of infections of varying severity .

Example answer:
{"entities": [{"text": "Management", "type": "HealthCareActivity"}, {"text": "skin and soft - tissue infections", "type": "BiologicFunction"}, {"text": "teaching hospital", "type": "Organization"}, {"text": "Skin and soft - tissue infections", "type": "BiologicFunction"}, {"text": "SSTIs", "type": "BiologicFunction"}, {"text": "infections", "type": "BiologicFunction"}]}

Example input:
Sentence: Disease severity was assessed using a clinical score .

Example answer:
{"entities": []}

Example input:
Sentence: A propensity adjusted regression analysis was used to investigate the association of patient satisfaction metrics with neurosurgeon quality , as measured by their individual rate of mortality and average length - of - stay ( LOS ) .

Example answer:
{"entities": [{"text": "regression analysis", "type": "IntellectualProduct"}, {"text": "patient satisfaction metrics", "type": "IntellectualProduct"}, {"text": "neurosurgeon", "type": "ProfessionalOrOccupationalGroup"}, {"text": "individual", "type": "PopulationGroup"}]}

Example input:
Sentence: 87 for the ordinal surgical index of seve rity for surgical services ( IGQ ) .

Example answer:
{"entities": [{"text": "surgical services", "type": "HealthCareActivity"}]}

Example input:
Sentence: Severity of illness index for surgical departments in a Cuban hospital : a revalidation study In the context of the evaluation of hospital services , the incorporation of severity indices allows an essential control variable for performance comparisons in time and space through risk adjustment .

Example answer:
{"entities": [{"text": "surgical departments", "type": "Organization"}, {"text": "Cuban", "type": "SpatialConcept"}, {"text": "hospital", "type": "Organization"}, {"text": "revalidation study", "type": "ResearchActivity"}, {"text": "evaluation", "type": "HealthCareActivity"}, {"text": "risk adjustment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Criterion validity was demonstrated through the correlation s between the severity index for surgical services and other similar indices .

Example answer:
{"entities": [{"text": "surgical services", "type": "HealthCareActivity"}, {"text": "indices", "type": "IntellectualProduct"}]}

Example input:
Sentence: The severity index for surgical services was developed in 1999 and validated as a general index for surgical services .

Example answer:
{"entities": [{"text": "surgical services", "type": "HealthCareActivity"}, {"text": "general index", "type": "IntellectualProduct"}]}

Example input:
Sentence: The surgical services severity index may be used in the original context and is easily adaptable to other contexts as well .

Example answer:
{"entities": [{"text": "surgical services", "type": "HealthCareActivity"}]}

Input:
Sentence: To evaluate the validity and reliability of the surgical services severity index to warrant its reasonable use under current conditions .

## Item MedMentions:test:3696
Example input:
Sentence: Presently , we sought to further advance our understanding of the mechanisms by which obesity promotes CRC by examining associations between microbiome , inflammation and Wnt - signaling in Apc ( + / 1638N ) mice whose obesity was induced by one of two modalities , diet - or genetically - induced obesity .

Example answer:
{"entities": [{"text": "obesity", "type": "BiologicFunction"}, {"text": "CRC", "type": "BiologicFunction"}, {"text": "inflammation", "type": "Finding"}, {"text": "Wnt - signaling", "type": "BiologicFunction"}, {"text": "Apc ( + / 1638N )", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "diet", "type": "Food"}, {"text": "genetically - induced", "type": "BiologicFunction"}]}

Example input:
Sentence: Our findings support a link between obesity and immunosenescence and suggest a potential therapeutic tool for obesity -related immune dysfunction .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "immunosenescence", "type": "BiologicFunction"}, {"text": "immune dysfunction", "type": "BiologicFunction"}]}

Example input:
Sentence: Correlation analysis showed that IL - 2 was positively correlated with total cholesterol ( TC ) , LDL - c , and genotype ( r = 0 . 542 , 0 . 410 , 0 . 598 , P < 0 . 05 ) and negatively correlated with HDL - c ( r = -0 .

Example answer:
{"entities": [{"text": "Correlation analysis", "type": "ResearchActivity"}, {"text": "IL - 2", "type": "Chemical"}, {"text": "total cholesterol", "type": "Chemical"}, {"text": "TC", "type": "Chemical"}, {"text": "LDL - c", "type": "Chemical"}, {"text": "negatively", "type": "Finding"}, {"text": "HDL - c", "type": "Chemical"}]}

Example input:
Sentence: Participants who developed incident type 2 diabetes were significantly older and had significantly higher body mass index ( BMI ; p = 0 . 012 ) , total cholesterol ( p = 0 . 007 ) , fasting triglycerides ( p < 0 . 001 ) , and Homeostatic Model Assessment of Insulin Resistance ( HOMA - IR ) ( p < 0 .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "type 2 diabetes", "type": "Finding"}, {"text": "significantly older", "type": "PopulationGroup"}, {"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "fasting", "type": "Finding"}, {"text": "triglycerides", "type": "Chemical"}, {"text": "Homeostatic Model Assessment of Insulin Resistance", "type": "HealthCareActivity"}, {"text": "HOMA - IR", "type": "HealthCareActivity"}]}

Example input:
Sentence: A strong relationship of IL - 33 / ST2 with NPs and classical inflammatory mediators was observed in cardiac tissue .

Example answer:
{"entities": [{"text": "IL - 33", "type": "Chemical"}, {"text": "ST2", "type": "Chemical"}, {"text": "NPs", "type": "Chemical"}, {"text": "inflammatory mediators", "type": "BiologicFunction"}, {"text": "cardiac tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: mRNA expression of IL - 33 / ST2 system was evaluated in cardiac , adipose and hepatic biopsies from obese Zucker rats ( O ) and controls ( CO ) .

Example answer:
{"entities": [{"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "IL - 33", "type": "AnatomicalStructure"}, {"text": "ST2", "type": "AnatomicalStructure"}, {"text": "cardiac", "type": "HealthCareActivity"}, {"text": "adipose", "type": "AnatomicalStructure"}, {"text": "hepatic biopsies", "type": "HealthCareActivity"}, {"text": "obese Zucker rats", "type": "Eukaryote"}, {"text": "O", "type": "Eukaryote"}]}

Example input:
Sentence: The strong relationships with NP systems and inflammatory mediators could suggest an involvement for IL - 33 / ST2 in molecular pathways leading to cardiac dysfunction and inflammation associated with obesity .

Example answer:
{"entities": [{"text": "NP", "type": "Chemical"}, {"text": "inflammatory mediators", "type": "BiologicFunction"}, {"text": "IL - 33", "type": "Chemical"}, {"text": "ST2", "type": "Chemical"}, {"text": "molecular pathways", "type": "BiologicFunction"}, {"text": "cardiac dysfunction", "type": "Finding"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}]}

Example input:
Sentence: Expression of sST2 in cardiac , adipose and liver tissue decreased in O compared with controls , suggesting an involvement for IL - 33 / ST2 system in molecular mechanisms of obesity .

Example answer:
{"entities": [{"text": "Expression", "type": "BiologicFunction"}, {"text": "sST2", "type": "Chemical"}, {"text": "cardiac", "type": "AnatomicalStructure"}, {"text": "adipose", "type": "AnatomicalStructure"}, {"text": "liver tissue", "type": "AnatomicalStructure"}, {"text": "O", "type": "Eukaryote"}, {"text": "IL - 33", "type": "Chemical"}, {"text": "ST2", "type": "Chemical"}, {"text": "molecular mechanisms", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}]}

Example input:
Sentence: Effects of obesity on IL - 33 / ST2 system in heart , adipose tissue and liver : study in the experimental model of Zucker rats Suppression of tumorigenicity 2 ( ST2 ) mediates the effect of Interleukin - 33 ( IL - 33 ) .

Example answer:
{"entities": [{"text": "obesity", "type": "BiologicFunction"}, {"text": "IL - 33", "type": "Chemical"}, {"text": "ST2", "type": "Chemical"}, {"text": "heart", "type": "AnatomicalStructure"}, {"text": "adipose tissue", "type": "AnatomicalStructure"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "study", "type": "ResearchActivity"}, {"text": "experimental model", "type": "IntellectualProduct"}, {"text": "Zucker rats", "type": "Eukaryote"}, {"text": "Suppression of tumorigenicity 2", "type": "Chemical"}, {"text": "Interleukin - 33", "type": "Chemical"}]}

Example input:
Sentence: We aimed to investigate effects of obesity on IL - 33 / ST2 system in heart , adipose tissue and liver in a rodent model of obesity .

Example answer:
{"entities": [{"text": "obesity", "type": "BiologicFunction"}, {"text": "IL - 33", "type": "Chemical"}, {"text": "ST2", "type": "Chemical"}, {"text": "heart", "type": "AnatomicalStructure"}, {"text": "adipose tissue", "type": "AnatomicalStructure"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "rodent model", "type": "BiologicFunction"}]}

Input:
Sentence: Few data are reported on the relationship between IL - 33 / ST2 and obesity .

## Item MedMentions:test:3175
Example input:
Sentence: As for phosphorylation , IL - 2 induces the acetylation of signaling molecules , including Stat5 , in the murine T cell line CTLL - 2 .

Example answer:
{"entities": [{"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "IL - 2", "type": "Chemical"}, {"text": "acetylation", "type": "BiologicFunction"}, {"text": "signaling molecules", "type": "Chemical"}, {"text": "Stat5", "type": "Chemical"}, {"text": "murine T cell line", "type": "AnatomicalStructure"}, {"text": "CTLL - 2", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Mitochondrial pyruvate dehydrogenase phosphatase 1 regulates the early differentiation of cardiomyocytes from mouse embryonic stem cells Mitochondria are crucial for maintaining the properties of embryonic stem cells ( ESCs ) and for regulating their subsequent differentiation into diverse cell lineages , including cardiomyocytes .

Example answer:
{"entities": [{"text": "Mitochondrial pyruvate dehydrogenase phosphatase 1", "type": "AnatomicalStructure"}, {"text": "differentiation of cardiomyocytes", "type": "BiologicFunction"}, {"text": "mouse embryonic stem cells", "type": "AnatomicalStructure"}, {"text": "Mitochondria", "type": "AnatomicalStructure"}, {"text": "embryonic stem cells", "type": "AnatomicalStructure"}, {"text": "ESCs", "type": "AnatomicalStructure"}, {"text": "differentiation", "type": "BiologicFunction"}, {"text": "cardiomyocytes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The LIF receptor activates several signaling pathways in diverse cell types , including Jak / STAT , MAPK and PI3 - kinase pathways in the endometrium of fertile woman .

Example answer:
{"entities": [{"text": "LIF receptor", "type": "Chemical"}, {"text": "signaling pathways", "type": "BiologicFunction"}, {"text": "diverse cell types", "type": "IntellectualProduct"}, {"text": "MAPK", "type": "Chemical"}, {"text": "PI3 - kinase", "type": "Chemical"}, {"text": "pathways", "type": "BiologicFunction"}, {"text": "endometrium", "type": "AnatomicalStructure"}, {"text": "fertile", "type": "BiologicFunction"}, {"text": "woman", "type": "PopulationGroup"}]}

Example input:
Sentence: LIFR - activated STAT3 restricts differentiation via cytokine induction .

Example answer:
{"entities": [{"text": "LIFR", "type": "Chemical"}, {"text": "STAT3", "type": "Chemical"}, {"text": "cytokine", "type": "Chemical"}]}

Example input:
Sentence: The differentiation domain contains four SPXX repeats that are phosphorylated by MAPK to restrict STAT3 activation ; the self - renewal domain is characterized by a 3 K motif that is acetylated by p300 .

Example answer:
{"entities": [{"text": "SPXX repeats", "type": "Chemical"}, {"text": "phosphorylated", "type": "BiologicFunction"}, {"text": "MAPK", "type": "Chemical"}, {"text": "STAT3 activation", "type": "BiologicFunction"}, {"text": "self - renewal", "type": "BiologicFunction"}, {"text": "3 K motif", "type": "Chemical"}, {"text": "acetylated", "type": "BiologicFunction"}]}

Example input:
Sentence: LIF is a secreted glycoprotein with a variety of biological functions including stimulation of cell proliferation , differentiation and survival that are all essential for blastocyete development and implantation .

Example answer:
{"entities": [{"text": "LIF", "type": "Chemical"}, {"text": "glycoprotein", "type": "Chemical"}, {"text": "biological functions", "type": "BiologicFunction"}, {"text": "cell proliferation", "type": "BiologicFunction"}, {"text": "differentiation", "type": "BiologicFunction"}, {"text": "survival", "type": "BiologicFunction"}, {"text": "blastocyete", "type": "AnatomicalStructure"}, {"text": "implantation", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , we report that the LIFR cytoplasmic domain contains a self - renewal domain within the juxtamembrane region and a differentiation domain within the C - terminal region .

Example answer:
{"entities": [{"text": "LIFR", "type": "Chemical"}, {"text": "cytoplasmic domain", "type": "AnatomicalStructure"}, {"text": "self - renewal", "type": "BiologicFunction"}, {"text": "juxtamembrane region", "type": "AnatomicalStructure"}, {"text": "C - terminal region", "type": "SpatialConcept"}]}

Example input:
Sentence: In mESCs , acetyl - LIFR undergoes homodimerization , leading to STAT3 hypo - or hyper - activation depending on the presence or absence of gp130 .

Example answer:
{"entities": [{"text": "mESCs", "type": "AnatomicalStructure"}, {"text": "LIFR", "type": "Chemical"}, {"text": "homodimerization", "type": "BiologicFunction"}, {"text": "STAT3", "type": "Chemical"}, {"text": "presence", "type": "Finding"}, {"text": "gp130", "type": "Chemical"}]}

Example input:
Sentence: LIF binds to the LIF receptor ( LIFR ) and activates the JAK - STAT3 pathway , but it remains unknown how the receptor complex triggers differentiation or self - renewal .

Example answer:
{"entities": [{"text": "LIF", "type": "Chemical"}, {"text": "LIF receptor", "type": "Chemical"}, {"text": "LIFR", "type": "Chemical"}, {"text": "JAK - STAT3 pathway", "type": "BiologicFunction"}, {"text": "receptor complex", "type": "AnatomicalStructure"}, {"text": "self - renewal", "type": "BiologicFunction"}]}

Example input:
Sentence: Thus , LIFR acetylation and serine phosphorylation differentially promote stem cell self - renewal and differentiation .

Example answer:
{"entities": [{"text": "LIFR", "type": "Chemical"}, {"text": "acetylation", "type": "BiologicFunction"}, {"text": "serine phosphorylation", "type": "BiologicFunction"}, {"text": "stem cell", "type": "AnatomicalStructure"}, {"text": "self - renewal", "type": "BiologicFunction"}]}

Input:
Sentence: Opposing Roles of Acetylation and Phosphorylation in LIFR - Dependent Self - Renewal Growth Signaling in Mouse Embryonic Stem Cells LIF promotes self - renewal of mouse embryonic stem cells ( mESCs ) , and in its absence , the cells differentiate .

## Item MedMentions:test:3895
Example input:
Sentence: 9 % and 5 . 9 % , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 68 % vs .

Example answer:
{"entities": []}

Example input:
Sentence: 91 . 54 % , 79 % vs .

Example answer:
{"entities": []}

Example input:
Sentence: 0±8 . 6 % vs .

Example answer:
{"entities": []}

Example input:
Sentence: 6 % , 89 .

Example answer:
{"entities": []}

Example input:
Sentence: 78 . 87 % and 80 . 48 % vs .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % ) , compared to 6 ( 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 6±2 . 5 % ; 24 . 9±1 .

Example answer:
{"entities": []}

Example input:
Sentence: 6 - 1 . 9 % and 1 . 9 - 2 .

Example answer:
{"entities": []}

Example input:
Sentence: 4 . 9 % vs .

Example answer:
{"entities": []}

Input:
Sentence: 6 . 9 % vs .

## Item MedMentions:test:3891
Example input:
Sentence: 3 % .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % , 10 . 8 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % ( 90 . 7 % - 93 . 7 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % and 89 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % ( median 41 .

Example answer:
{"entities": [{"text": "median", "type": "SpatialConcept"}]}

Example input:
Sentence: 3 % to 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % ; 29 . 9±6 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % , 17 . 6 % , and 15 .

Example answer:
{"entities": []}

Input:
Sentence: 3 % at a mean of 15 .

## Item MedMentions:test:3803
Example input:
Sentence: One hundred nine of 608 patients in the hypofractionated arm versus 117 of 598 in the standard arm experienced BCF .

Example answer:
{"entities": [{"text": "hypofractionated arm", "type": "HealthCareActivity"}, {"text": "standard arm", "type": "HealthCareActivity"}, {"text": "BCF", "type": "Finding"}]}

Example input:
Sentence: Thirty and 24 patients were treated with total doses [ relative biological effectiveness ( RBE ) ] of 57 . 6 Gy and 64 . 0 Gy , respectively , in 16 fractions .

Example answer:
{"entities": [{"text": "treated with", "type": "HealthCareActivity"}]}

Example input:
Sentence: We hypothesized that hypofractionation versus conventional fractionation is similar in efficacy without increased toxicity .

Example answer:
{"entities": [{"text": "hypofractionation", "type": "HealthCareActivity"}, {"text": "conventional fractionation", "type": "HealthCareActivity"}]}

Example input:
Sentence: 42 patients with prostate cancer received 7 - week fractionated radiotherapy treatment ( RT ) with daily dose fractions

Example answer:
{"entities": [{"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "radiotherapy treatment", "type": "HealthCareActivity"}, {"text": "RT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Conclusion The hypofractionated RT regimen used in this trial was not inferior to conventional RT and was not associated with increased late toxicity .

Example answer:
{"entities": [{"text": "hypofractionated RT regimen", "type": "HealthCareActivity"}, {"text": "trial", "type": "ResearchActivity"}, {"text": "conventional RT", "type": "HealthCareActivity"}]}

Example input:
Sentence: One hundred and eighteen patients received EBRT in 23 fractions of 2 Gy and HDR ( TG43 algorithm ) in 3 fractions of 6 .

Example answer:
{"entities": [{"text": "HDR", "type": "HealthCareActivity"}, {"text": "TG43 algorithm", "type": "IntellectualProduct"}]}

Example input:
Sentence: The following fractionation regimens were analyzed [ 8 Gy × 1 , 4 Gy × 5 ( short course radiation therapy ) ] , were compared to 3 Gy × 10 , 2 . 50 Gy × 14 - 15 and 2 Gy × 20 - 30 ( long course radiation therapy ) .

Example answer:
{"entities": [{"text": "fractionation regimens", "type": "HealthCareActivity"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "radiation therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Hypofractionated RT is more convenient for patients and should be considered for intermediate - risk prostate cancer .

Example answer:
{"entities": [{"text": "Hypofractionated RT", "type": "HealthCareActivity"}, {"text": "intermediate - risk", "type": "Finding"}, {"text": "prostate cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Dose fractionations were 27 Gy / 2 fractions for 69 patients ( 13 % ) , 45 . 5 Gy / 7 fractions for 168 ( 32 % ) , 49 Gy / 7 fractions for 149 ( 28 % ) , 54 Gy / 9 fractions for 130 ( 25 % ) , and others for 8 ( 2 % ) .

Example answer:
{"entities": [{"text": "Dose fractionations", "type": "HealthCareActivity"}]}

Example input:
Sentence: Hypofractionated RT is given over a shorter time with larger doses per treatment than standard RT .

Example answer:
{"entities": [{"text": "Hypofractionated RT", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "RT", "type": "HealthCareActivity"}]}

Input:
Sentence: Patients were allocated to conventional RT of 78 Gy in 39 fractions over 8 weeks or to hypofractionated RT of 60 Gy in 20 fractions over 4 weeks .

## Item MedMentions:test:3536
Example input:
Sentence: Family Matters : Promoting the Academic Adaptation of Latino Youth in New and Established Destination As primary agents of socialization , families and schools can powerfully shape the academic adaptation of youth .

Example answer:
{"entities": [{"text": "Academic", "type": "Finding"}, {"text": "Latino", "type": "PopulationGroup"}, {"text": "Destination", "type": "SpatialConcept"}, {"text": "schools", "type": "Organization"}, {"text": "academic", "type": "Finding"}]}

Example input:
Sentence: There are many factors that relate to an increase in clinic utilization ; some of this increase may have been a result of the linkages between schools and clinics .

Example answer:
{"entities": [{"text": "clinic", "type": "Organization"}, {"text": "schools", "type": "Organization"}, {"text": "clinics", "type": "Organization"}]}

Example input:
Sentence: In the future , adolescents should be offered more individually organised programmes according to their preferences and needs in cooperation with parents and health care providers .

Example answer:
{"entities": [{"text": "programmes", "type": "HealthCareActivity"}, {"text": "health care providers", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: A closer look at school bonding among African American adolescents in low - income communities : A latent class analysis Positive school bonding is a significant precursor to students ' school success .

Example answer:
{"entities": [{"text": "school", "type": "Organization"}, {"text": "bonding", "type": "BiologicFunction"}, {"text": "African American", "type": "PopulationGroup"}, {"text": "low - income communities", "type": "PopulationGroup"}, {"text": "latent class analysis", "type": "ResearchActivity"}, {"text": "Positive", "type": "Finding"}, {"text": "students", "type": "PopulationGroup"}]}

Example input:
Sentence: Randomized Trials of the Teen Outreach Program in Louisiana and Rochester , New York To evaluate the Teen Outreach Program , a pregnancy prevention program , in 2 community -based settings .

Example answer:
{"entities": [{"text": "Randomized Trials", "type": "ResearchActivity"}, {"text": "Louisiana", "type": "SpatialConcept"}, {"text": "Rochester", "type": "SpatialConcept"}, {"text": "New York", "type": "SpatialConcept"}, {"text": "evaluate", "type": "HealthCareActivity"}]}

Example input:
Sentence: Early results demonstrated the strength and feasibility of the model over a 4 - year period , with 31 linkages developed and maintained , over 11 , 300 contacts between clinic health educators and teens completed , and increasing adherence to the Centers for Disease Control and Prevention -defined clinical best practices for adolescent reproductive health .

Example answer:
{"entities": [{"text": "model", "type": "IntellectualProduct"}, {"text": "clinic", "type": "Organization"}, {"text": "health educators", "type": "ProfessionalOrOccupationalGroup"}, {"text": "teens", "type": "PopulationGroup"}, {"text": "Centers for Disease Control and Prevention", "type": "Organization"}, {"text": "clinical best practices", "type": "HealthCareActivity"}, {"text": "reproductive health", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: The New York City Department of Health and Mental Hygiene implemented a community - wide , multicomponent intervention to reduce unintended teen pregnancy , the Bronx Teens Connection .

Example answer:
{"entities": [{"text": "New York City", "type": "SpatialConcept"}, {"text": "Department of Health and Mental Hygiene", "type": "Organization"}, {"text": "multicomponent intervention", "type": "HealthCareActivity"}, {"text": "teen pregnancy", "type": "Finding"}]}

Example input:
Sentence: Bronx Teens Connection 's Clinic Linkage Model : Connecting Youth to Quality Sexual and Reproductive Health Care Teen pregnancy and birth rates in the Bronx have been higher than in New York City , representing a longstanding health disparity .

Example answer:
{"entities": [{"text": "Clinic", "type": "Organization"}, {"text": "Linkage Model", "type": "IntellectualProduct"}, {"text": "Sexual and Reproductive Health Care", "type": "HealthCareActivity"}, {"text": "Teen pregnancy", "type": "Finding"}, {"text": "Bronx", "type": "SpatialConcept"}, {"text": "New York City", "type": "SpatialConcept"}, {"text": "health disparity", "type": "Finding"}]}

Example input:
Sentence: The Bronx Teens Connection Clinic Linkage Model used needs assessments , delineated the criteria for linkages , clarified roles and responsibilities of partners and staff , established trainings to support the staff engaged in linkage activities , and developed and used process evaluation methods .

Example answer:
{"entities": [{"text": "Clinic", "type": "Organization"}, {"text": "Linkage Model", "type": "IntellectualProduct"}, {"text": "assessments", "type": "HealthCareActivity"}, {"text": "partners", "type": "PopulationGroup"}, {"text": "staff", "type": "ProfessionalOrOccupationalGroup"}, {"text": "evaluation methods", "type": "ResearchActivity"}]}

Example input:
Sentence: The Bronx Teens Connection Clinic Linkage Model sought to increase teens ' access to and use of sexual and reproductive health care by increasing community partner capacity to link neighborhood clinics to youth - serving organizations , including schools .

Example answer:
{"entities": [{"text": "Clinic", "type": "Organization"}, {"text": "Linkage Model", "type": "IntellectualProduct"}, {"text": "teens", "type": "PopulationGroup"}, {"text": "sexual and reproductive health care", "type": "HealthCareActivity"}, {"text": "partner", "type": "PopulationGroup"}, {"text": "capacity", "type": "Finding"}, {"text": "neighborhood", "type": "SpatialConcept"}, {"text": "clinics", "type": "Organization"}, {"text": "youth - serving organizations", "type": "Organization"}, {"text": "schools", "type": "Organization"}]}

Input:
Sentence: The Bronx Teens Connection Clinic Linkage Model is an explicit framework for clinical and youth - serving organizations seeking to establish formal linkage relationships that may be useful for other municipalities or organizations .

## Item MedMentions:test:3026
Example input:
Sentence: The possible role of Sergentomyia in the circulation of mammalian leishmaniases in the Old World has been considered as Leishmania DNA and / or parasites have been identified in several species .

Example answer:
{"entities": [{"text": "possible", "type": "Finding"}, {"text": "Sergentomyia", "type": "Eukaryote"}, {"text": "circulation", "type": "Finding"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "leishmaniases", "type": "BiologicFunction"}, {"text": "Old World", "type": "SpatialConcept"}, {"text": "Leishmania DNA", "type": "Chemical"}, {"text": "parasites", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: stenygros is compared with other Bruchomyiinae and Psychodidae species , especially with species of Phlebotominae that are superficially similar to Bruchomyiinae .

Example answer:
{"entities": [{"text": "stenygros", "type": "Eukaryote"}, {"text": "Bruchomyiinae", "type": "Eukaryote"}, {"text": "Psychodidae", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Phlebotominae", "type": "Eukaryote"}]}

Example input:
Sentence: supseomense erected by Rho & Min ( 2011 ) are considered as invalid species while Prochaetosoma arcticum , P . lugubre and Epsilonema cygnoides are assumed as species inquirenda .

Example answer:
{"entities": [{"text": "supseomense", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Prochaetosoma arcticum", "type": "Eukaryote"}, {"text": "P . lugubre", "type": "Eukaryote"}, {"text": "Epsilonema cygnoides", "type": "Eukaryote"}, {"text": "species inquirenda", "type": "IntellectualProduct"}]}

Example input:
Sentence: Draconema ophicephalum ( Claparède , 1863 ) ( Draconematidae ) and Epsilonema steineri Chitwood , 1935 ( Epsilonematidae ) , both known from insufficient material and females only , are re - described and problems of their taxonomic identification as well as species compositions of respective genera are discussed .

Example answer:
{"entities": [{"text": "Draconema ophicephalum", "type": "Eukaryote"}, {"text": "Draconematidae", "type": "Eukaryote"}, {"text": "Epsilonema steineri", "type": "Eukaryote"}, {"text": "Epsilonematidae", "type": "Eukaryote"}, {"text": "problems", "type": "Finding"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "compositions", "type": "ClinicalAttribute"}, {"text": "genera", "type": "IntellectualProduct"}]}

Example input:
Sentence: In this paper , we consider the genus Sergentomyia as divided into seven subgenera , mainly based on spermathecal morphology : Sergentomyia , Sintonius , Parrotomyia , Rondanomyia , Capensomyia , Vattieromyia and Trouilletomyia .

Example answer:
{"entities": [{"text": "paper", "type": "IntellectualProduct"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Sergentomyia", "type": "Eukaryote"}, {"text": "spermathecal", "type": "AnatomicalStructure"}, {"text": "Sintonius", "type": "Eukaryote"}, {"text": "Parrotomyia", "type": "Eukaryote"}, {"text": "Rondanomyia", "type": "Eukaryote"}, {"text": "Capensomyia", "type": "Eukaryote"}, {"text": "Vattieromyia", "type": "Eukaryote"}, {"text": "Trouilletomyia", "type": "Eukaryote"}]}

Example input:
Sentence: Results of this study revealed striking morphological differences between the immature stages of Bruchomyiinae and Phlebotominae ; the former are lacking abdominal pseudopods and microtrichia on the cephalic integument , both of which are present in the larvae of Phlebotominae .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "morphological", "type": "SpatialConcept"}, {"text": "Bruchomyiinae", "type": "Eukaryote"}, {"text": "Phlebotominae", "type": "Eukaryote"}, {"text": "abdominal", "type": "SpatialConcept"}, {"text": "pseudopods", "type": "AnatomicalStructure"}, {"text": "microtrichia", "type": "AnatomicalStructure"}, {"text": "cephalic", "type": "SpatialConcept"}, {"text": "integument", "type": "BodySystem"}, {"text": "larvae", "type": "Eukaryote"}]}

Example input:
Sentence: A remarkable new species of Eutrichopoda Townsend , 1908 ( Diptera : Tachinidae : Phasiinae ) A new Tachinidae species , Eutrichopoda flavipenna sp . nov . ( Diptera : Tachinidae : Phasiinae ) , from Brazil and Paraguay is described and illustrated by photographs and line drawings .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "Eutrichopoda Townsend", "type": "Eukaryote"}, {"text": "Diptera", "type": "Eukaryote"}, {"text": "Tachinidae", "type": "Eukaryote"}, {"text": "Phasiinae", "type": "Eukaryote"}, {"text": "Eutrichopoda flavipenna sp . nov .", "type": "Eukaryote"}, {"text": "Brazil", "type": "SpatialConcept"}, {"text": "Paraguay", "type": "SpatialConcept"}, {"text": "line", "type": "SpatialConcept"}, {"text": "drawings", "type": "IntellectualProduct"}]}

Example input:
Sentence: Record of a new species of the genus Viridopromontorius Luna de Carvalho ( Strepsiptera : Corioxenidae ) from India with a revised key to Corioxenidae A new species of the genus Viridopromontorius Luna de Carvalho is described from West Bengal , India .

Example answer:
{"entities": [{"text": "Record", "type": "IntellectualProduct"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Viridopromontorius Luna de Carvalho", "type": "Eukaryote"}, {"text": "Strepsiptera", "type": "Eukaryote"}, {"text": "Corioxenidae", "type": "Eukaryote"}, {"text": "India", "type": "SpatialConcept"}, {"text": "West Bengal , India", "type": "SpatialConcept"}]}

Example input:
Sentence: Immature stages and larval chaetotaxy of Notofairchildia stenygros ( Quate & Alexander ) ( Diptera : Psychodidae : Bruchomyiinae ) Some authors have hypothesized that Bruchomyiinae is " the most plesiomorphic subfamily of Psychodidae " and its members " are among the most primitive living Diptera " . Although Bruchomyiinae is of no medical importance , it is of great evolutionary significance , having long been placed as the sister group of Phlebotominae .

Example answer:
{"entities": [{"text": "larval", "type": "Eukaryote"}, {"text": "Notofairchildia stenygros", "type": "Eukaryote"}, {"text": "Diptera", "type": "Eukaryote"}, {"text": "Psychodidae", "type": "Eukaryote"}, {"text": "Bruchomyiinae", "type": "Eukaryote"}, {"text": "plesiomorphic subfamily", "type": "IntellectualProduct"}, {"text": "no", "type": "Finding"}, {"text": "evolutionary", "type": "BiologicFunction"}, {"text": "Phlebotominae", "type": "Eukaryote"}]}

Example input:
Sentence: Notes on the natural history of Lipoptilocnema species are provided , and their potential importance as PMI indicators is highlighted , including the first record of Lipoptilocnema reared from a dead human body .

Example answer:
{"entities": [{"text": "Notes", "type": "IntellectualProduct"}, {"text": "Lipoptilocnema species", "type": "IntellectualProduct"}, {"text": "PMI indicators", "type": "Chemical"}, {"text": "Lipoptilocnema", "type": "Eukaryote"}, {"text": "dead", "type": "BiologicFunction"}, {"text": "human body", "type": "Eukaryote"}]}

Input:
Sentence: Taxonomic Revision of Lipoptilocnema ( Diptera : Sarcophagidae ) , With Notes on Natural History and Forensic Importance of Its Species Lipoptilocnema Townsend is a small genus of Neotropical Sarcophaginae with a distinctive genitalic morphology .

## Item MedMentions:test:3434
Example input:
Sentence: Long - term follow - up of this cohort for the incident cardiovascular disease will shed light on the true cardiovascular risk in a typical South Indian rural farming population .

Example answer:
{"entities": [{"text": "Long - term follow - up", "type": "HealthCareActivity"}, {"text": "cardiovascular disease", "type": "BiologicFunction"}, {"text": "South Indian", "type": "SpatialConcept"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: With a 5 - year survival rate of just 8 % , pancreatic cancer ( PC ) is projected to be the second leading cause of cancer deaths by 2030 .

Example answer:
{"entities": [{"text": "pancreatic cancer", "type": "BiologicFunction"}, {"text": "PC", "type": "BiologicFunction"}]}

Example input:
Sentence: Out of 100 patients , indications for stenting were locally advanced disease not amenable to surgery ( 52 % ) , metastatic disease ( 35 % ) , CVA ( 1 % ) , cardiac and respiratory problem ( 8 % ) , un - willing for surgery in 5 % of patients .

Example answer:
{"entities": [{"text": "stenting", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "metastatic disease", "type": "BiologicFunction"}, {"text": "CVA", "type": "BiologicFunction"}, {"text": "respiratory problem", "type": "Finding"}]}

Example input:
Sentence: Stenting is the best option to palliate the symptoms of dysphagia , from which patient is suffering the most .

Example answer:
{"entities": [{"text": "Stenting", "type": "HealthCareActivity"}, {"text": "symptoms", "type": "Finding"}, {"text": "dysphagia", "type": "BiologicFunction"}, {"text": "suffering the most", "type": "Finding"}]}

Example input:
Sentence: A bleomycin , etoposide , and cisplatin treatment protocol targeting germ cell neoplasia lead to disease remission and prolonged survival of 34 months .

Example answer:
{"entities": [{"text": "bleomycin", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "treatment protocol", "type": "HealthCareActivity"}, {"text": "germ cell neoplasia", "type": "BiologicFunction"}, {"text": "disease remission", "type": "Finding"}]}

Example input:
Sentence: Between October 2015 and January 2016 , 15 consecutive patients with cancer in the distal third of the esophagus or the gastric cardia underwent this modified surgical procedure .

Example answer:
{"entities": [{"text": "cancer", "type": "BiologicFunction"}, {"text": "distal third of the esophagus", "type": "SpatialConcept"}, {"text": "gastric cardia", "type": "SpatialConcept"}, {"text": "surgical procedure", "type": "HealthCareActivity"}]}

Example input:
Sentence: All 578 patients undergoing esophagectomy for thoracic esophageal squamous cell carcinoma at the Center for Esophageal Diseases located in Padova between January 1992 and December 2010 were retrospectively evaluated .

Example answer:
{"entities": [{"text": "esophagectomy", "type": "HealthCareActivity"}, {"text": "thoracic esophageal squamous cell carcinoma", "type": "BiologicFunction"}, {"text": "Center for Esophageal Diseases", "type": "Organization"}, {"text": "retrospectively evaluated", "type": "ResearchActivity"}]}

Example input:
Sentence: One hundred patients , who had undergone esophageal stenting from January 2012 to January 2015 , were included in the study .

Example answer:
{"entities": [{"text": "esophageal stenting", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Esophageal stenting is relatively safe procedure with short stay of the patient in the hospital .

Example answer:
{"entities": [{"text": "Esophageal stenting", "type": "HealthCareActivity"}, {"text": "procedure", "type": "HealthCareActivity"}, {"text": "hospital", "type": "Organization"}]}

Example input:
Sentence: To know the success rate , early and long term complications and mortality in esophageal stenting , when it was done in malignant esophageal stricture patients .

Example answer:
{"entities": [{"text": "early", "type": "Finding"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "esophageal stenting", "type": "HealthCareActivity"}, {"text": "malignant esophageal stricture", "type": "BiologicFunction"}]}

Input:
Sentence: Long Term Outcome in Patients with Esophageal Stenting for Cancer Esophagus - Our Experience at a Rural Hospital of Punjab , India Cancer of the esophagus is among the leading cause of cancer deaths in Punjab , India .

## Item MedMentions:test:3537
Example input:
Sentence: Andrographolide induced the expression and translocation of Nrf2 from the cytoplasm to the nucleus , thereby activating antioxidant response element ( ARE ) gene transcription and HO - 1 expression in murine hippocampal HT22 cells .

Example answer:
{"entities": [{"text": "Andrographolide", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "translocation", "type": "BiologicFunction"}, {"text": "Nrf2", "type": "Chemical"}, {"text": "cytoplasm", "type": "AnatomicalStructure"}, {"text": "nucleus", "type": "AnatomicalStructure"}, {"text": "antioxidant response element", "type": "Chemical"}, {"text": "ARE", "type": "Chemical"}, {"text": "gene transcription", "type": "BiologicFunction"}, {"text": "HO - 1", "type": "Chemical"}, {"text": "murine", "type": "Eukaryote"}, {"text": "hippocampal", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We discovered that CLASP2 co - immunoprecipitates ( co - IPs ) the novel protein SOGA1 , the microtubule - associated protein kinase MARK2 , and the microtubule / actin - regulating protein G2L1 .

Example answer:
{"entities": [{"text": "CLASP2", "type": "Chemical"}, {"text": "co - immunoprecipitates", "type": "Chemical"}, {"text": "co - IPs", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}, {"text": "SOGA1", "type": "Chemical"}, {"text": "microtubule - associated protein kinase", "type": "Chemical"}, {"text": "MARK2", "type": "Chemical"}, {"text": "microtubule", "type": "AnatomicalStructure"}, {"text": "actin", "type": "Chemical"}, {"text": "regulating", "type": "BiologicFunction"}, {"text": "G2L1", "type": "Chemical"}]}

Example input:
Sentence: Owing to the fact that the peptide bonds between lysine and dopamine can be cleaved under triggering by pepsin , the resulting RhB / DOX @ PLDA - MSNs exibit enzyme - responsive characterization .

Example answer:
{"entities": [{"text": "lysine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "pepsin", "type": "Chemical"}, {"text": "RhB", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "PLDA", "type": "Chemical"}, {"text": "MSNs", "type": "Chemical"}, {"text": "enzyme", "type": "Chemical"}]}

Example input:
Sentence: The other protocol is based on the synthesis of a cyclic depsipeptide library in which a glycolamidic ester group is incorporated by adding glycolic acid .

Example answer:
{"entities": [{"text": "cyclic depsipeptide library", "type": "Chemical"}, {"text": "glycolic acid", "type": "Chemical"}]}

Example input:
Sentence: Tyrphostin AG - related compounds attenuate H2O2 - induced TRPM2 - dependent and - independent cellular responses TRPM2 is a Ca ( 2 + ) - permeable channel that is activated by H2O2 .

Example answer:
{"entities": [{"text": "Tyrphostin AG - related compounds", "type": "Chemical"}, {"text": "H2O2", "type": "Chemical"}, {"text": "TRPM2", "type": "Chemical"}, {"text": "cellular", "type": "AnatomicalStructure"}, {"text": "Ca ( 2 + ) - permeable channel", "type": "Chemical"}]}

Example input:
Sentence: The R2R3MYB VvMYBPA1 from grape reprograms the phenylpropanoid pathway in tobacco flowers This work shows that , in tobacco , the ectopic expression of VvMYBPA1 , a grape regulator of proanthocyanidin biosynthesis , up - or down - regulates different branches of the phenylproanoid pathway , in a structure - specific fashion .

Example answer:
{"entities": [{"text": "R2R3MYB", "type": "Chemical"}, {"text": "VvMYBPA1", "type": "Chemical"}, {"text": "grape", "type": "Eukaryote"}, {"text": "phenylpropanoid pathway", "type": "BiologicFunction"}, {"text": "tobacco", "type": "Eukaryote"}, {"text": "flowers", "type": "Eukaryote"}, {"text": "ectopic expression", "type": "BiologicFunction"}, {"text": "proanthocyanidin", "type": "Chemical"}, {"text": "up - or down - regulates", "type": "BiologicFunction"}, {"text": "phenylproanoid pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Quantification of intact plasma AGT consisting of oxidized and reduced conformations using a modified ELISA The pleiotropic actions of the renin - angiotensin system ( RAS ) depend on the availability of angiotensinogen ( AGT ) which generates angiotensin I ( ANG I ) when cleaved by renin .

Example answer:
{"entities": [{"text": "plasma", "type": "BodySubstance"}, {"text": "AGT", "type": "Chemical"}, {"text": "reduced conformations", "type": "SpatialConcept"}, {"text": "ELISA", "type": "HealthCareActivity"}, {"text": "renin - angiotensin system", "type": "BodySystem"}, {"text": "RAS", "type": "BodySystem"}, {"text": "angiotensinogen", "type": "Chemical"}, {"text": "angiotensin I", "type": "Chemical"}, {"text": "ANG I", "type": "Chemical"}, {"text": "cleaved", "type": "SpatialConcept"}, {"text": "renin", "type": "Chemical"}]}

Example input:
Sentence: These data suggest that WDR81 coordinates p62 and LC3C to facilitate autophagic removal of Ub proteins , and provide important insights into CAMRQ2 syndrome , a WDR81 -related developmental disorder .

Example answer:
{"entities": [{"text": "WDR81", "type": "Chemical"}, {"text": "p62", "type": "Chemical"}, {"text": "LC3C", "type": "Chemical"}, {"text": "autophagic removal", "type": "BiologicFunction"}, {"text": "Ub proteins", "type": "Chemical"}, {"text": "insights", "type": "BiologicFunction"}, {"text": "CAMRQ2 syndrome ,", "type": "BiologicFunction"}, {"text": "developmental disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: Immodin ( IM ) is low molecular dialysate fraction of homogenate made from human leukocytes .

Example answer:
{"entities": [{"text": "Immodin", "type": "Chemical"}, {"text": "IM", "type": "Chemical"}, {"text": "dialysate fraction", "type": "Chemical"}, {"text": "human", "type": "Eukaryote"}, {"text": "leukocytes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Immunoprecipitates of β - Raf from cardiomyocytes phosphorylated the C - terminal 182 amino acids of NHE1 and mass spectrometry analysis showed that amino acid Thr ( 653 ) was phosphorylated .

Example answer:
{"entities": [{"text": "Immunoprecipitates", "type": "Chemical"}, {"text": "β - Raf", "type": "Chemical"}, {"text": "cardiomyocytes", "type": "AnatomicalStructure"}, {"text": "phosphorylated", "type": "BiologicFunction"}, {"text": "C - terminal 182 amino acids", "type": "SpatialConcept"}, {"text": "NHE1", "type": "Chemical"}, {"text": "mass spectrometry analysis", "type": "HealthCareActivity"}, {"text": "amino acid", "type": "Chemical"}, {"text": "Thr ( 653 )", "type": "Chemical"}]}

Input:
Sentence: Imreg 1 and Imreg 2 formed by the dipeptide tyrosine - glycine and the tripeptide tyrosine - glycine - glycine , respectively .

## Item MedMentions:test:3416
Example input:
Sentence: Presence of CD44 positive and CD24 negative tumor cells in breast carcinoma ( cells with ' stem cell ' like property ) as marker of aggressiveness and poor prognosis was checked for association with various markers of disease aggression like age at presentation , size of tumor , histological grade of tumor , triple negative status , level of micro - vessel density , and nodal status .

Example answer:
{"entities": [{"text": "CD44 positive", "type": "AnatomicalStructure"}, {"text": "CD24", "type": "AnatomicalStructure"}, {"text": "negative tumor cells", "type": "Finding"}, {"text": "breast carcinoma", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "stem cell", "type": "AnatomicalStructure"}, {"text": "marker of aggressiveness", "type": "Chemical"}, {"text": "poor prognosis", "type": "Finding"}, {"text": "markers of disease aggression", "type": "Chemical"}, {"text": "size of tumor", "type": "SpatialConcept"}, {"text": "histological grade of tumor", "type": "IntellectualProduct"}, {"text": "triple negative status", "type": "Finding"}]}

Example input:
Sentence: CSCs were then isolated from the tumors and their microRNA ( miRNA ) expression was analyzed by semi - quantitative polymerase chain reaction .

Example answer:
{"entities": [{"text": "CSCs", "type": "AnatomicalStructure"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "microRNA", "type": "Chemical"}, {"text": "miRNA", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "semi - quantitative polymerase chain reaction", "type": "HealthCareActivity"}]}

Example input:
Sentence: While neutrophils and benign human mammary epithelial cells ( HMEC ) form a single leading edge , MDA - MB - 231 breast cancer cells possess multiple leading edges enriched with A3 adenosine receptors .

Example answer:
{"entities": [{"text": "neutrophils", "type": "AnatomicalStructure"}, {"text": "human mammary", "type": "AnatomicalStructure"}, {"text": "epithelial cells", "type": "AnatomicalStructure"}, {"text": "HMEC", "type": "AnatomicalStructure"}, {"text": "leading edge", "type": "AnatomicalStructure"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "breast cancer cells", "type": "AnatomicalStructure"}, {"text": "leading edges", "type": "AnatomicalStructure"}, {"text": "A3 adenosine receptors", "type": "Chemical"}]}

Example input:
Sentence: CD44 positive / CD24 negative ( stem cell like property ) breast carcinoma cells as marker of tumor aggression Cells with stem cell like properties in solid organ malignancies like breast and pancreas have been studied over the last decade and have been found to be associated with poor prognosis .

Example answer:
{"entities": [{"text": "CD44 positive", "type": "AnatomicalStructure"}, {"text": "CD24 negative", "type": "AnatomicalStructure"}, {"text": "stem cell", "type": "AnatomicalStructure"}, {"text": "breast carcinoma cells", "type": "AnatomicalStructure"}, {"text": "marker of tumor aggression", "type": "Chemical"}, {"text": "Cells", "type": "AnatomicalStructure"}, {"text": "solid organ", "type": "AnatomicalStructure"}, {"text": "malignancies", "type": "BiologicFunction"}, {"text": "breast", "type": "AnatomicalStructure"}, {"text": "pancreas", "type": "AnatomicalStructure"}, {"text": "poor prognosis", "type": "Finding"}]}

Example input:
Sentence: In this study , we examined the roles of contractile dynamics of CSCs in cell invasion and delineated the underlying molecular mechanisms of their distinct cell invasion potential .

Example answer:
{"entities": [{"text": "CSCs", "type": "AnatomicalStructure"}, {"text": "cell invasion", "type": "BiologicFunction"}, {"text": "molecular mechanisms", "type": "BiologicFunction"}, {"text": "potential", "type": "Finding"}]}

Example input:
Sentence: The existence of human CSCs is mainly supported by xenotransplantation of prospectively isolated cells , but their clonal dynamics and plasticity remain unclear .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "CSCs", "type": "AnatomicalStructure"}, {"text": "xenotransplantation", "type": "HealthCareActivity"}, {"text": "isolated cells", "type": "Finding"}, {"text": "clonal", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Conditioned medium and direct cell - cell contacts experiments were used to investigate the effect of bone marrow -derived mesenchymal stromal cells ( MSCs ) , osteoprogenitor - like cells ( MG - 63 ) and osteosarcoma cells ( SaOS - 2 ) on luminal - like ( MCF - 7 ) and basal - like ( MDA - MB - 231 ) BCCs flow cytometry was used to assess the purity of isolated BCCs and osteoblasts .

Example answer:
{"entities": [{"text": "Conditioned medium", "type": "Chemical"}, {"text": "cell - cell contacts", "type": "BiologicFunction"}, {"text": "bone marrow", "type": "AnatomicalStructure"}, {"text": "mesenchymal stromal cells", "type": "AnatomicalStructure"}, {"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "osteoprogenitor - like cells", "type": "AnatomicalStructure"}, {"text": "MG - 63", "type": "AnatomicalStructure"}, {"text": "osteosarcoma cells", "type": "AnatomicalStructure"}, {"text": "SaOS - 2", "type": "AnatomicalStructure"}, {"text": "luminal - like", "type": "AnatomicalStructure"}, {"text": "MCF - 7", "type": "AnatomicalStructure"}, {"text": "basal - like", "type": "AnatomicalStructure"}, {"text": "MDA - MB - 231", "type": "AnatomicalStructure"}, {"text": "BCCs", "type": "AnatomicalStructure"}, {"text": "flow cytometry", "type": "HealthCareActivity"}, {"text": "osteoblasts", "type": "AnatomicalStructure"}]}

Example input:
Sentence: However , high CD82 expression rendered prostate cancer cells to have intensified epithelial characteristics upon fibronectin engagement , along with decreased cell motility and invasiveness .

Example answer:
{"entities": [{"text": "CD82", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "prostate", "type": "AnatomicalStructure"}, {"text": "cancer cells", "type": "AnatomicalStructure"}, {"text": "fibronectin", "type": "Chemical"}, {"text": "cell motility", "type": "BiologicFunction"}]}

Example input:
Sentence: Engineering of Anti - CD133 Tri - Specific Molecule Capable of Inducing NK Expansion and Driving Antibody - Dependent Cell - Mediated Cytotoxicity ( ADCC ) The selective elimination of cancer stem cells ( CSCs ) in tumor patients is a crucial goal because CSCs cause drug refractory relapse .

Example answer:
{"entities": [{"text": "Engineering", "type": "ResearchActivity"}, {"text": "Anti - CD133 Tri - Specific Molecule", "type": "Chemical"}, {"text": "NK", "type": "AnatomicalStructure"}, {"text": "Expansion", "type": "BiologicFunction"}, {"text": "Antibody - Dependent Cell - Mediated Cytotoxicity", "type": "BiologicFunction"}, {"text": "ADCC", "type": "BiologicFunction"}, {"text": "cancer stem cells", "type": "AnatomicalStructure"}, {"text": "CSCs", "type": "AnatomicalStructure"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "drug refractory", "type": "BiologicFunction"}]}

Example input:
Sentence: Post expansion , ( 1 ) ADSCs showed in vitro adherence to tissue culture polystyrene ( TCPS ) ; ( 2 ) MSC surface antigen expression [ CD14 ( - ) , CD19 ( - ) , CD34 ( - ) , CD45 ( - ) , CD73 ( + ) , CD90 ( + ) , CD105 ( + ) ] ; and ( 3 ) trilineage differentiation into osteoblasts , adipocytes , and chondrocytes .

Example answer:
{"entities": [{"text": "ADSCs", "type": "AnatomicalStructure"}, {"text": "tissue culture polystyrene", "type": "Chemical"}, {"text": "TCPS", "type": "Chemical"}, {"text": "MSC", "type": "AnatomicalStructure"}, {"text": "surface antigen", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "CD14", "type": "Chemical"}, {"text": "CD19", "type": "Chemical"}, {"text": "CD34", "type": "Chemical"}, {"text": "CD45", "type": "Chemical"}, {"text": "CD73", "type": "Chemical"}, {"text": "CD90", "type": "Chemical"}, {"text": "CD105", "type": "Chemical"}, {"text": "trilineage differentiation", "type": "BiologicFunction"}, {"text": "osteoblasts", "type": "AnatomicalStructure"}, {"text": "adipocytes", "type": "AnatomicalStructure"}, {"text": "chondrocytes", "type": "AnatomicalStructure"}]}

Input:
Sentence: Using de - adhesion assay and atomic force microscopy , we show that CSCs derived from melanoma and breast cancer cell lines exhibit increased contractility compared to non - CSCs across all tumor types .

## Item MedMentions:test:3540
Example input:
Sentence: The mean SUVmax of two common sites ( posterior superior iliac spine [ PSIS ] and greater trochanter ) was higher in patients with involved marrow than those with uninvolved one ( 2 . 36 and 2 . 75 vs .

Example answer:
{"entities": [{"text": "posterior superior iliac spine", "type": "AnatomicalStructure"}, {"text": "PSIS", "type": "AnatomicalStructure"}, {"text": "greater trochanter", "type": "AnatomicalStructure"}, {"text": "marrow", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Moreover , using a conditional anterograde axonal tract - tracing approach , we found that OB A2AR neurons innervate the piriform cortex and olfactory tubercle .

Example answer:
{"entities": [{"text": "anterograde axonal tract - tracing approach", "type": "ResearchActivity"}, {"text": "OB", "type": "AnatomicalStructure"}, {"text": "A2AR", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "piriform cortex", "type": "AnatomicalStructure"}, {"text": "olfactory tubercle", "type": "AnatomicalStructure"}]}

Example input:
Sentence: All clinical cases and cadaveric specimens underwent surgical closure prior to MR imaging including placement of titanium mesh over the craniotomy defect with a dural graft of porcine small intestinal submucosa ( SIS ) sealed with Tisseel ( fibrin sealant ) .

Example answer:
{"entities": [{"text": "cadaveric", "type": "AnatomicalStructure"}, {"text": "surgical closure", "type": "HealthCareActivity"}, {"text": "MR imaging", "type": "HealthCareActivity"}, {"text": "titanium", "type": "Chemical"}, {"text": "mesh", "type": "MedicalDevice"}, {"text": "craniotomy", "type": "HealthCareActivity"}, {"text": "porcine", "type": "Eukaryote"}, {"text": "small intestinal submucosa", "type": "AnatomicalStructure"}, {"text": "SIS", "type": "AnatomicalStructure"}, {"text": "Tisseel", "type": "Chemical"}, {"text": "fibrin sealant", "type": "Chemical"}]}

Example input:
Sentence: The palmar cutaneous branch of the median nerve ( PCB ) is considered to run in a position adjacent to , but outside , the ulnar FCR sheath .

Example answer:
{"entities": [{"text": "palmar cutaneous branch of the median nerve", "type": "AnatomicalStructure"}, {"text": "PCB", "type": "AnatomicalStructure"}, {"text": "ulnar", "type": "AnatomicalStructure"}, {"text": "FCR", "type": "AnatomicalStructure"}, {"text": "sheath", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The aim of present study was to evaluate the fate of the root ( resorbed , exfoliated , covered by bone ) after coronectomy or intentional root retention of impacted mandibular 3 ( rd ) molars in patients with high risk for inferior alveolar nerve damage as evaluated by the intra oral periapical radiograph .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "root", "type": "AnatomicalStructure"}, {"text": "resorbed", "type": "BiologicFunction"}, {"text": "exfoliated", "type": "BiologicFunction"}, {"text": "bone", "type": "AnatomicalStructure"}, {"text": "root retention", "type": "BiologicFunction"}, {"text": "impacted mandibular 3 ( rd ) molars", "type": "BiologicFunction"}, {"text": "high risk", "type": "Finding"}, {"text": "inferior alveolar nerve", "type": "AnatomicalStructure"}, {"text": "damage", "type": "InjuryOrPoisoning"}, {"text": "evaluated", "type": "HealthCareActivity"}]}

Example input:
Sentence: Abnormalities confined to the posterior fossa according to USS were found in 81 fetuses ( 67 with parenchymal and 14 with CSF -containing lesions ) .

Example answer:
{"entities": [{"text": "Abnormalities confined to the posterior fossa", "type": "Finding"}, {"text": "USS", "type": "HealthCareActivity"}, {"text": "fetuses", "type": "AnatomicalStructure"}, {"text": "parenchymal", "type": "AnatomicalStructure"}, {"text": "CSF", "type": "BodySubstance"}, {"text": "lesions", "type": "Finding"}]}

Example input:
Sentence: During routine laparoscopic exploration , right vas deferens and testicular vessels were entering the right internal inguinal ring so right inguinal exploration was done , which revealed blind ending vas deferens and testicular vessels and the left testis was found intra - abdominally near the left internal ring with a mass on its upper pole .

Example answer:
{"entities": [{"text": "laparoscopic", "type": "HealthCareActivity"}, {"text": "exploration", "type": "HealthCareActivity"}, {"text": "right vas deferens", "type": "AnatomicalStructure"}, {"text": "right internal inguinal ring", "type": "AnatomicalStructure"}, {"text": "right inguinal", "type": "SpatialConcept"}, {"text": "blind ending", "type": "Finding"}, {"text": "vas deferens", "type": "AnatomicalStructure"}, {"text": "left testis", "type": "AnatomicalStructure"}, {"text": "intra - abdominally", "type": "SpatialConcept"}, {"text": "internal ring", "type": "SpatialConcept"}, {"text": "mass", "type": "Finding"}, {"text": "upper pole", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A lateral ischial obstacle must be investigated , in the form of a constant fibrous expansion , which , like a retinaculum , can cause nerve entrapment .

Example answer:
{"entities": [{"text": "lateral ischial", "type": "AnatomicalStructure"}, {"text": "fibrous", "type": "AnatomicalStructure"}, {"text": "expansion", "type": "HealthCareActivity"}, {"text": "retinaculum", "type": "AnatomicalStructure"}, {"text": "nerve entrapment", "type": "BiologicFunction"}]}

Example input:
Sentence: A constant anatomical finding must be highlighted : the presence of a lateral fibrous expansion from the ischium passing behind the nerves and vessels , especially the posterior femoral cutaneous nerve and its perineal branches .

Example answer:
{"entities": [{"text": "anatomical finding", "type": "SpatialConcept"}, {"text": "lateral fibrous", "type": "AnatomicalStructure"}, {"text": "expansion", "type": "HealthCareActivity"}, {"text": "ischium", "type": "AnatomicalStructure"}, {"text": "nerves", "type": "AnatomicalStructure"}, {"text": "vessels", "type": "AnatomicalStructure"}, {"text": "posterior femoral cutaneous nerve", "type": "AnatomicalStructure"}, {"text": "perineal branches", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Entrapment of the posterior femoral cutaneous nerve and its inferior cluneal branches : anatomical basis of surgery for inferior cluneal neuralgia The apparent failure of pudendal nerve surgery in some patients has led us to suggest the possibility of entrapment of other adjacent nerve structures , leading to the concept of inferior cluneal neuralgia .

Example answer:
{"entities": [{"text": "Entrapment", "type": "BiologicFunction"}, {"text": "posterior femoral cutaneous nerve", "type": "AnatomicalStructure"}, {"text": "inferior cluneal branches", "type": "AnatomicalStructure"}, {"text": "anatomical basis", "type": "SpatialConcept"}, {"text": "surgery", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "inferior cluneal neuralgia", "type": "Finding"}, {"text": "pudendal nerve", "type": "AnatomicalStructure"}, {"text": "entrapment", "type": "BiologicFunction"}, {"text": "adjacent nerve structures", "type": "AnatomicalStructure"}]}

Input:
Sentence: Exploration was continued cranially underneath the piriformis , looking for potential entrapments affecting the posterior femoral cutaneous nerve and the sciatic nerve .

## Item MedMentions:test:3645
Example input:
Sentence: Candida biofilm was formed on a denture base resin and was then treated with Lactobacillus rhamnosus and Lactobacillus casei .

Example answer:
{"entities": [{"text": "Candida", "type": "Eukaryote"}, {"text": "biofilm", "type": "Bacterium"}, {"text": "Lactobacillus rhamnosus", "type": "Bacterium"}, {"text": "Lactobacillus casei", "type": "Bacterium"}]}

Example input:
Sentence: Consequently , our results suggested a novel finding that lactic acid bacterium affected the production of several constituents such as cyclotene , furfural , furfuryl alcohol and methional in the soy sauce fermentation process .

Example answer:
{"entities": [{"text": "finding", "type": "Finding"}, {"text": "lactic acid bacterium", "type": "Bacterium"}, {"text": "cyclotene", "type": "Chemical"}, {"text": "furfural", "type": "Chemical"}, {"text": "furfuryl alcohol", "type": "Chemical"}, {"text": "methional", "type": "Chemical"}, {"text": "soy sauce", "type": "Food"}, {"text": "fermentation process", "type": "BiologicFunction"}]}

Example input:
Sentence: In faecal batch incubations , LA biohydrogenation and butyrate production were positively correlated and SA did not inhibit butyrate production .

Example answer:
{"entities": [{"text": "faecal", "type": "BodySubstance"}, {"text": "batch incubations", "type": "HealthCareActivity"}, {"text": "LA", "type": "Chemical"}, {"text": "butyrate", "type": "Chemical"}, {"text": "SA", "type": "Chemical"}]}

Example input:
Sentence: CAT - NP containing biocompatible Fe3O4 were developed to catalyze H2O2 to generate free - radicals in situ that simultaneously degrade the biofilm matrix and rapidly kill the embedded bacteria with exceptional efficacy ( > 5 - log reduction of cell - viability ) .

Example answer:
{"entities": [{"text": "biocompatible", "type": "Chemical"}, {"text": "Fe3O4", "type": "Chemical"}, {"text": "H2O2", "type": "Chemical"}, {"text": "free - radicals", "type": "Chemical"}, {"text": "in situ", "type": "SpatialConcept"}, {"text": "biofilm matrix", "type": "AnatomicalStructure"}, {"text": "embedded bacteria", "type": "Bacterium"}, {"text": "cell - viability", "type": "BiologicFunction"}]}

Example input:
Sentence: Biofilm formation was significantly promoted ( p < 0 . 05 ) by 5 and 10 µM C6 - HSL , inhibited ( p < 0 . 05 ) by C4 - HSL ( 5 and 10 µM ) and 5 µM 3 - oxo - C8 - HSL , suggesting that QS may have a regulatory role in the biofilm formation of H .

Example answer:
{"entities": [{"text": "Biofilm formation", "type": "BiologicFunction"}, {"text": "C6 - HSL", "type": "Chemical"}, {"text": "C4 - HSL", "type": "Chemical"}, {"text": "3 - oxo - C8 - HSL", "type": "Chemical"}, {"text": "QS", "type": "BiologicFunction"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "H .", "type": "Bacterium"}]}

Example input:
Sentence: Functional foods or probiotics could be helpful in caries prevention and periodontal disease management , although evidence is limited and biological mechanisms not fully elucidated .

Example answer:
{"entities": [{"text": "Functional foods", "type": "Food"}, {"text": "probiotics", "type": "Bacterium"}, {"text": "caries prevention", "type": "HealthCareActivity"}, {"text": "periodontal disease", "type": "BiologicFunction"}, {"text": "management", "type": "HealthCareActivity"}]}

Example input:
Sentence: It can also create highly acidic microenvironments that cause acid - dissolution of enamel - apatite on teeth , leading to the onset of dental caries .

Example answer:
{"entities": [{"text": "acidic microenvironments", "type": "SpatialConcept"}, {"text": "enamel", "type": "BodySubstance"}, {"text": "apatite", "type": "Chemical"}, {"text": "teeth", "type": "AnatomicalStructure"}, {"text": "dental caries", "type": "BiologicFunction"}]}

Example input:
Sentence: Group 3 specimens were subjected to pH cycling and artificial caries were created on the buccal , lingual and gingival walls .

Example answer:
{"entities": [{"text": "pH cycling", "type": "HealthCareActivity"}, {"text": "caries", "type": "BiologicFunction"}, {"text": "buccal", "type": "SpatialConcept"}, {"text": "lingual", "type": "SpatialConcept"}, {"text": "gingival walls", "type": "SpatialConcept"}]}

Example input:
Sentence: Nanocatalysts promote Streptococcus mutans biofilm matrix degradation and enhance bacterial killing to suppress dental caries in vivo Dental biofilms ( known as plaque ) are notoriously difficult to remove or treat because the bacteria can be enmeshed in a protective extracellular matrix .

Example answer:
{"entities": [{"text": "Streptococcus mutans", "type": "Bacterium"}, {"text": "biofilm matrix", "type": "AnatomicalStructure"}, {"text": "bacterial killing", "type": "Finding"}, {"text": "dental caries", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "biofilms", "type": "Bacterium"}, {"text": "plaque", "type": "BiologicFunction"}, {"text": "bacteria", "type": "Bacterium"}, {"text": "protective extracellular matrix", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Here , we report a novel strategy to control plaque - biofilms using catalytic nanoparticles ( CAT - NP ) with peroxidase -like activity that trigger extracellular matrix degradation and cause bacterial death within acidic niches of caries -causing biofilm .

Example answer:
{"entities": [{"text": "plaque", "type": "BiologicFunction"}, {"text": "biofilms", "type": "Bacterium"}, {"text": "peroxidase", "type": "Chemical"}, {"text": "extracellular matrix", "type": "AnatomicalStructure"}, {"text": "bacterial death", "type": "Finding"}, {"text": "caries", "type": "BiologicFunction"}, {"text": "biofilm", "type": "Bacterium"}]}

Input:
Sentence: In caries , the fermentation process leads to acid production and the generation of biofilm components such as Glucans .

## Item MedMentions:test:3901
Example input:
Sentence: The type strain is SYP - A7299 T ( = DSM 100491T = KCTC 39 592 T ) .

Example answer:
{"entities": [{"text": "SYP - A7299 T", "type": "Bacterium"}, {"text": "= DSM 100491T = KCTC 39 592 T", "type": "Bacterium"}]}

Example input:
Sentence: The strain - types identified were AK3 ( ST - 5 SCCmecIV t045 ; n = 1 ) , USA500 ( ST8 SCCmecIV t064 ; n = 1 ) , WSPP ( ST30 SCCmecIV t019 ; n = 1 ) , Rhine Hesse ( ST5 SCCmecII t002 ; n = 2 ) , and EMRSA - 15 ( ST22 SCCmecIV t032 ; n = 3 ) .

Example answer:
{"entities": [{"text": "AK3 ( ST - 5 SCCmecIV", "type": "Bacterium"}, {"text": "USA500 ( ST8 SCCmecIV", "type": "Bacterium"}, {"text": "WSPP ( ST30 SCCmecIV", "type": "Bacterium"}, {"text": "Rhine Hesse ( ST5 SCCmecII", "type": "Bacterium"}, {"text": "EMRSA - 15 ( ST22 SCCmecIV", "type": "Bacterium"}]}

Example input:
Sentence: The Peptidoglycan Pattern of Staphylococcus carnosus TM300 - Detailed Analysis and Variations Due to Genetic and Metabolic Influences The Gram - positive bacterium Staphylococcus carnosus ( S . carnosus ) TM300 is an apathogenic staphylococcal species commonly used in meat starter cultures .

Example answer:
{"entities": [{"text": "Peptidoglycan", "type": "Chemical"}, {"text": "Pattern", "type": "SpatialConcept"}, {"text": "Staphylococcus carnosus TM300", "type": "Bacterium"}, {"text": "Detailed Analysis", "type": "ResearchActivity"}, {"text": "Genetic", "type": "AnatomicalStructure"}, {"text": "Gram - positive bacterium", "type": "Bacterium"}, {"text": "Staphylococcus carnosus ( S . carnosus ) TM300", "type": "Bacterium"}, {"text": "apathogenic", "type": "Finding"}, {"text": "staphylococcal", "type": "Bacterium"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "meat", "type": "Food"}, {"text": "starter cultures", "type": "HealthCareActivity"}]}

Example input:
Sentence: aureus ATCC 25923 .

Example answer:
{"entities": [{"text": "aureus ATCC 25923", "type": "Bacterium"}]}

Example input:
Sentence: aureus strains of the same capsular phenotype with different biofilm forming strengths were used to non - invasively infect mammary glands of lactating mice .

Example answer:
{"entities": [{"text": "aureus", "type": "Bacterium"}, {"text": "capsular", "type": "SpatialConcept"}, {"text": "biofilm forming", "type": "BiologicFunction"}, {"text": "mammary glands", "type": "AnatomicalStructure"}, {"text": "lactating", "type": "Finding"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: aureus strains .

Example answer:
{"entities": [{"text": "aureus", "type": "Bacterium"}]}

Example input:
Sentence: aureus strain produced marked acute mastitic lesions , showing profuse infiltration predominantly with neutrophils , with evidence of necrosis in the affected mammary glands .

Example answer:
{"entities": [{"text": "aureus", "type": "Bacterium"}, {"text": "acute mastitic", "type": "BiologicFunction"}, {"text": "lesions", "type": "Finding"}, {"text": "infiltration", "type": "BiologicFunction"}, {"text": "neutrophils", "type": "AnatomicalStructure"}, {"text": "necrosis", "type": "BiologicFunction"}, {"text": "mammary glands", "type": "AnatomicalStructure"}]}

Example input:
Sentence: aureus strain .

Example answer:
{"entities": [{"text": "aureus", "type": "Bacterium"}]}

Example input:
Sentence: aureus strain MHO _ 001 ( 2 . 86 Mb ) and two complete plasmids ( 27 Kb and 3 Kb ) .

Example answer:
{"entities": [{"text": "aureus", "type": "Bacterium"}, {"text": "plasmids", "type": "Chemical"}]}

Example input:
Sentence: The strain we used , MHO _ 001 , represents the important community - acquired methicillin resistant Staphylococcus aureus lineage USA300 .

Example answer:
{"entities": [{"text": "Staphylococcus aureus", "type": "Bacterium"}]}

Input:
Sentence: aureus USA300 strain MHO _ 001 .

## Item MedMentions:test:3807
Example input:
Sentence: The German Society of Pediatric Oncology and Hematology ( GPOH ) data center registered and followed patients with other diagnoses than Ewing sarcoma who were treated according to the EE99 protocol in an additional non - Ewing database .

Example answer:
{"entities": [{"text": "German Society of Pediatric Oncology and Hematology ( GPOH ) data center", "type": "Organization"}, {"text": "registered", "type": "HealthCareActivity"}, {"text": "diagnoses", "type": "Finding"}, {"text": "Ewing sarcoma", "type": "BiologicFunction"}, {"text": "treated", "type": "Finding"}, {"text": "EE99 protocol", "type": "IntellectualProduct"}, {"text": "non - Ewing database", "type": "IntellectualProduct"}]}

Example input:
Sentence: Peripheral blood mononuclear cells ( PBMCs ) were obtained from 13 patients with GD without eye manifestations ; 10 patients with active GO ; and 12 patients with nodular goiter ( NG ) .

Example answer:
{"entities": [{"text": "Peripheral blood mononuclear cells", "type": "AnatomicalStructure"}, {"text": "PBMCs", "type": "AnatomicalStructure"}, {"text": "GD", "type": "BiologicFunction"}, {"text": "eye manifestations", "type": "Finding"}, {"text": "GO", "type": "BiologicFunction"}, {"text": "nodular goiter", "type": "BiologicFunction"}, {"text": "NG", "type": "BiologicFunction"}]}

Example input:
Sentence: Pancreatic neuroendocrine cancer with liver metastases and multiple peritoneal metastases : report of one case Pancreatic neuroendocrine tumor ( pNET ) is a rare pancreatic tumor , with its incidence showing a rising trend in recent years .

Example answer:
{"entities": [{"text": "Pancreatic", "type": "AnatomicalStructure"}, {"text": "liver metastases", "type": "BiologicFunction"}, {"text": "multiple peritoneal metastases", "type": "BiologicFunction"}, {"text": "pancreatic tumor", "type": "BiologicFunction"}]}

Example input:
Sentence: Human Ewing sarcoma cells A673 were cultured with vincristine and doxorubicin to determine half maximal inhibitory concentration ( IC50 ) .

Example answer:
{"entities": [{"text": "Human", "type": "Eukaryote"}, {"text": "Ewing sarcoma", "type": "BiologicFunction"}, {"text": "cells A673", "type": "AnatomicalStructure"}, {"text": "cultured", "type": "HealthCareActivity"}, {"text": "vincristine", "type": "Chemical"}, {"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: By immunohistochemistry , 17 PNETs expressed at least 1 marker of neuronal differentiation , including synaptophysin , NSE , CD56 , S100 , and chromogranin in 10 , 8 , 14 , 8 , and 1 tumors , respectively .

Example answer:
{"entities": [{"text": "immunohistochemistry", "type": "HealthCareActivity"}, {"text": "PNETs", "type": "BiologicFunction"}, {"text": "marker", "type": "Chemical"}, {"text": "neuronal differentiation", "type": "Finding"}, {"text": "synaptophysin", "type": "Chemical"}, {"text": "NSE", "type": "Chemical"}, {"text": "CD56", "type": "Chemical"}, {"text": "S100", "type": "Chemical"}, {"text": "chromogranin", "type": "Chemical"}, {"text": "tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: Central PNETs show a spectrum of morphologic features that overlaps with CNS tumors but lack EWSR1 rearrangement s .

Example answer:
{"entities": [{"text": "Central PNETs", "type": "BiologicFunction"}, {"text": "CNS", "type": "BodySystem"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "EWSR1", "type": "AnatomicalStructure"}, {"text": "rearrangement", "type": "BiologicFunction"}]}

Example input:
Sentence: Morphologic features of central nervous system ( CNS ) tumors were seen in 15 PNETs , including 9 medulloblastomas , 3 ependymomas , 2 medulloepitheliomas , and 1 glioblastoma , consistent with central PNET .

Example answer:
{"entities": [{"text": "central nervous system", "type": "BodySystem"}, {"text": "CNS", "type": "BodySystem"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "PNETs", "type": "BiologicFunction"}, {"text": "medulloblastomas", "type": "BiologicFunction"}, {"text": "ependymomas", "type": "BiologicFunction"}, {"text": "medulloepitheliomas", "type": "BiologicFunction"}, {"text": "glioblastoma", "type": "BiologicFunction"}, {"text": "central PNET", "type": "BiologicFunction"}]}

Example input:
Sentence: Membranous CD99 and nuclear Fli - 1 staining was seen in 10 and 16 tumors , respectively , and concurrent expression of both markers was seen in both central and Ewing sarcoma / peripheral PNET s .

Example answer:
{"entities": [{"text": "Membranous", "type": "AnatomicalStructure"}, {"text": "CD99", "type": "Chemical"}, {"text": "nuclear", "type": "SpatialConcept"}, {"text": "Fli - 1", "type": "Chemical"}, {"text": "staining", "type": "HealthCareActivity"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "markers", "type": "Chemical"}, {"text": "central", "type": "BiologicFunction"}, {"text": "Ewing sarcoma / peripheral PNET", "type": "BiologicFunction"}]}

Example input:
Sentence: In conclusion , central and Ewing sarcoma / peripheral PNETs may be encountered in the female genital tract with central PNETs being more common .

Example answer:
{"entities": [{"text": "central", "type": "BiologicFunction"}, {"text": "Ewing sarcoma / peripheral PNETs", "type": "BiologicFunction"}, {"text": "female genital tract", "type": "AnatomicalStructure"}, {"text": "central PNETs", "type": "BiologicFunction"}]}

Example input:
Sentence: Ewing sarcoma / peripheral PNETs lack morphologic features of CNS tumors .

Example answer:
{"entities": [{"text": "Ewing sarcoma / peripheral PNETs", "type": "BiologicFunction"}, {"text": "CNS", "type": "BodySystem"}, {"text": "tumors", "type": "BiologicFunction"}]}

Input:
Sentence: The remaining 4 PNETs were composed entirely of undifferentiated small round blue cells and were classified as Ewing sarcoma / peripheral PNET .

## Item MedMentions:test:3777
Example input:
Sentence: No statistically significant change , however , was observed in T2 , with normoxic and hyperoxic T2 values of 55 ± 16 and 56 ± 17 ms , respectively .

Example answer:
{"entities": [{"text": "No statistically significant change", "type": "Finding"}]}

Example input:
Sentence: 8 / h and post = 4 . 4 / h , P < 0 . 0001 ) , oxygen desaturation ( pre = 13 . 7 / h and post = 3 . 8 / h , P < 0 . 0001 ) and Respiratory Disturbance Indexes ( RDI ) ( 20 . 0 / h vs .

Example answer:
{"entities": []}

Example input:
Sentence: In the bleeding group during the last step of hemorrhage , and compared to the sham group , there were decreases in oxygen consumption ( 3 . 7 [ 2 . 8 - 4 . 6 ] vs .

Example answer:
{"entities": [{"text": "bleeding", "type": "BiologicFunction"}, {"text": "hemorrhage", "type": "BiologicFunction"}, {"text": "sham", "type": "HealthCareActivity"}, {"text": "oxygen consumption", "type": "ClinicalAttribute"}]}

Example input:
Sentence: An electricity consumption of 0 . 6 kWh kg ( - 1 ) of chemical oxygen demand ( COD ) removed was observed .

Example answer:
{"entities": [{"text": "chemical oxygen demand", "type": "BiologicFunction"}, {"text": "COD", "type": "BiologicFunction"}]}

Example input:
Sentence: Saturation of peripheral oxygen was unchanged 1 year postoperatively compared to baseline .

Example answer:
{"entities": [{"text": "Saturation of peripheral oxygen", "type": "BiologicFunction"}, {"text": "unchanged", "type": "Finding"}]}

Example input:
Sentence: Acute hypoxia significantly reduced aerobic scope by reducing [ Formula : see text ] , while [ Formula : see text ] remained unchanged .

Example answer:
{"entities": [{"text": "hypoxia", "type": "BiologicFunction"}, {"text": "unchanged", "type": "Finding"}]}

Example input:
Sentence: Individuals at 8°C were exposed to 50 % ( hypoxia ) or 100 % ( normoxia ) dissolved oxygen ( DO ) saturation ( as percent of air saturation ) from fertilization for ∼100 d ( 800 degree days ) and then raised in normoxic conditions for a further 15 mo .

Example answer:
{"entities": [{"text": "Individuals", "type": "Eukaryote"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "dissolved oxygen ( DO ) saturation", "type": "BiologicFunction"}]}

Example input:
Sentence: Overall , oxygen consumption rates increased with thermal stress , but the response patterns were not affected by heating rate .

Example answer:
{"entities": [{"text": "oxygen consumption rates increased", "type": "Finding"}, {"text": "thermal stress", "type": "BiologicFunction"}, {"text": "response", "type": "BiologicFunction"}, {"text": "patterns", "type": "SpatialConcept"}]}

Example input:
Sentence: At 18 mo after fertilization , aerobic scope was calculated in normoxia ( 100 % DO ) and acute ( 18 h ) hypoxia ( 50 % DO ) from the difference between the minimum and maximum oxygen consumption rates ( [ Formula : see text ] and [ Formula : see text ] , respectively ) at 10°C .

Example answer:
{"entities": [{"text": "DO", "type": "Chemical"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "oxygen consumption", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Patients showed a lower peak oxygen consumption ( VO2 /kg ) than controls ( P < 0 . 001 ) , as well as ventilatory inefficiency ( P = 0 . 024 ) .

Example answer:
{"entities": [{"text": "oxygen consumption", "type": "ClinicalAttribute"}, {"text": "VO2", "type": "ClinicalAttribute"}, {"text": "ventilatory inefficiency", "type": "Finding"}]}

Input:
Sentence: Although oxygen delivery remained unchanged , oxygen consumption was decreased from 4 . 0 ± 0 . 2 to 3 . 2 ± 0 .

## Item MedMentions:test:3699
Example input:
Sentence: 8 ( IQR 1 . 2 to 11 ) ] in relation to biochemical and histologic liver injury , PN , serum plant sterols , fibroblast growth factor 19 , and α - tocopherol .

Example answer:
{"entities": [{"text": "liver injury", "type": "InjuryOrPoisoning"}, {"text": "PN", "type": "HealthCareActivity"}, {"text": "serum", "type": "BodySubstance"}, {"text": "plant sterols", "type": "Chemical"}, {"text": "fibroblast growth factor 19", "type": "Chemical"}, {"text": "α - tocopherol", "type": "Chemical"}]}

Example input:
Sentence: Our results show that relapse -like alcohol drinking during the ADE was abolished by repeated intraperitoneal administration of Ro61 - 8048 and significantly reduced by its oral prodrug JM6 .

Example answer:
{"entities": [{"text": "ADE", "type": "Finding"}, {"text": "intraperitoneal administration", "type": "HealthCareActivity"}, {"text": "Ro61 - 8048", "type": "Chemical"}, {"text": "oral", "type": "SpatialConcept"}, {"text": "prodrug", "type": "Chemical"}, {"text": "JM6", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , acetamiprid induced liver toxicity measured by the increased activities of aspartate aminotransferase ( AST ) , alanine aminotransferase ( ALT ) , alkaline phosphates ( ALPs ) , and lactate dehydrogenase ( LDH ) which may be due to the loss of hepatic membrane architecture and hepatocellular damage .

Example answer:
{"entities": [{"text": "acetamiprid", "type": "Chemical"}, {"text": "induced liver toxicity", "type": "BiologicFunction"}, {"text": "activities", "type": "BiologicFunction"}, {"text": "aspartate aminotransferase", "type": "Chemical"}, {"text": "AST", "type": "Chemical"}, {"text": "alanine aminotransferase", "type": "Chemical"}, {"text": "ALT", "type": "Chemical"}, {"text": "alkaline phosphates", "type": "Chemical"}, {"text": "ALPs", "type": "Chemical"}, {"text": "lactate dehydrogenase", "type": "Chemical"}, {"text": "LDH", "type": "Chemical"}, {"text": "hepatic membrane architecture", "type": "AnatomicalStructure"}, {"text": "hepatocellular damage", "type": "BiologicFunction"}]}

Example input:
Sentence: Antrosterol , a bioactive constitute of sterols in edible Antrodia camphorata submerged whole broth , can protect liver from CCl4 damage via enhancing antioxidant and anti - inflammatory capacities .

Example answer:
{"entities": [{"text": "Antrosterol", "type": "Chemical"}, {"text": "sterols", "type": "Chemical"}, {"text": "edible Antrodia camphorata", "type": "Eukaryote"}, {"text": "submerged whole broth", "type": "Chemical"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "CCl4", "type": "Chemical"}, {"text": "antioxidant", "type": "BiologicFunction"}]}

Example input:
Sentence: In conclusion , the administration of EV derived from bone marrow derived MSCs may ameliorate hepatic IRI by reducing hepatic injury through modulation of the inflammatory response .

Example answer:
{"entities": [{"text": "administration", "type": "HealthCareActivity"}, {"text": "EV", "type": "AnatomicalStructure"}, {"text": "bone marrow", "type": "AnatomicalStructure"}, {"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "ameliorate", "type": "Finding"}, {"text": "hepatic IRI", "type": "InjuryOrPoisoning"}, {"text": "hepatic injury", "type": "InjuryOrPoisoning"}, {"text": "modulation", "type": "SpatialConcept"}, {"text": "inflammatory response", "type": "BiologicFunction"}]}

Example input:
Sentence: This study aimed to evaluate the role of interleukin ( IL ) - 18 and tumor necrosis factor ( TNF ) receptor in liver dysfunction induced by diet .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "interleukin ( IL ) - 18", "type": "Chemical"}, {"text": "tumor necrosis factor ( TNF ) receptor", "type": "Chemical"}, {"text": "liver dysfunction", "type": "BiologicFunction"}, {"text": "diet", "type": "Food"}]}

Example input:
Sentence: In order to avoid such adverse metabolic effects of oral treatment , estradiol ( E2 ) prodrugs ( EP ) were designed which bypass the liver tissue as inactive molecules .

Example answer:
{"entities": [{"text": "oral treatment", "type": "HealthCareActivity"}, {"text": "estradiol", "type": "Chemical"}, {"text": "E2", "type": "Chemical"}, {"text": "prodrugs", "type": "Chemical"}, {"text": "EP", "type": "Chemical"}, {"text": "liver tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Interestingly , treatment with a high - carbohydrate diet did not exacerbate liver damage in IL - 18 ( - / - ) and TNFR1 ( - / - ) mice .

Example answer:
{"entities": [{"text": "high - carbohydrate diet", "type": "HealthCareActivity"}, {"text": "liver damage", "type": "BiologicFunction"}, {"text": "IL - 18 ( - / - )", "type": "Chemical"}, {"text": "TNFR1 ( - / - )", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Alcohol Liver Disease ( ALD ) is a systemic pathology whose beginning and end belong to the intestine .

Example answer:
{"entities": [{"text": "Alcohol Liver Disease", "type": "BiologicFunction"}, {"text": "ALD", "type": "BiologicFunction"}, {"text": "intestine", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Binge - like EtOH exposure did not alter plasma IL - 1β levels but reduced the cerebrospinal fluid levels of this cytokine .

Example answer:
{"entities": [{"text": "plasma", "type": "BodySubstance"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "cerebrospinal fluid", "type": "BodySubstance"}, {"text": "cytokine", "type": "Chemical"}]}

Input:
Sentence: A Lieber - DeCarli regular EtOH diet ( EtOH liquid diet , 5 % ( v / v ) alcohol ) was applied to induce alcoholic liver damage .

## Item MedMentions:test:3832
Example input:
Sentence: Our findings suggest that owners in Alberta are predominantly new to production ; most ( 73 . 1 % ) have kept birds for less than 5 yr and 25 . 6 % for less than 1 yr .

Example answer:
{"entities": [{"text": "owners", "type": "PopulationGroup"}, {"text": "Alberta", "type": "SpatialConcept"}, {"text": "birds", "type": "Eukaryote"}]}

Example input:
Sentence: Psychosocial aspects towards donation were positive from the egg share donor and recipient .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "egg share donor", "type": "PopulationGroup"}, {"text": "recipient", "type": "PopulationGroup"}]}

Example input:
Sentence: Laying hens were the most commonly reported type of bird ( 93 . 4 % ) , followed by ducks and geese ( 35 . 3 % ) , turkeys , ( 33 . 8 % ) , and broiler chickens ( 33 . 1 % ) .

Example answer:
{"entities": [{"text": "Laying hens", "type": "Eukaryote"}, {"text": "bird", "type": "Eukaryote"}, {"text": "ducks", "type": "Eukaryote"}, {"text": "geese", "type": "Eukaryote"}, {"text": "turkeys", "type": "Eukaryote"}, {"text": "broiler chickens", "type": "Eukaryote"}]}

Example input:
Sentence: Beginning at 79 wk of age , 576 egg - laying hens ( Gallus domesticus ) were randomized to diets containing different amounts of CP - 31398 for 94 wk , 5 d , comprising a control group ( C ) ( n = 144 ) , which was fed a diet containing 0 ppm ( mg / kg ) of CP - 31398 ; a low - dose treatment ( LDT ) group ( n = 144 ) , which was fed a diet containing 100 ppm of CP - 31398 ; a moderate - dose treatment ( MDT ) group ( n = 144 ) which was fed a diet containing 200 ppm of CP - 31398 ; and a high - dose treatment ( HDT ) group ( n = 144 ) , which was fed a diet containing 300 ppm of CP - 31398 .

Example answer:
{"entities": [{"text": "egg - laying hens", "type": "Eukaryote"}, {"text": "Gallus domesticus", "type": "Eukaryote"}, {"text": "randomized", "type": "Finding"}, {"text": "diets", "type": "Food"}, {"text": "CP - 31398", "type": "Chemical"}, {"text": "diet", "type": "Food"}, {"text": "low - dose treatment", "type": "ResearchActivity"}, {"text": "LDT", "type": "ResearchActivity"}, {"text": "moderate - dose treatment", "type": "ResearchActivity"}, {"text": "MDT", "type": "ResearchActivity"}, {"text": "high - dose treatment", "type": "ResearchActivity"}, {"text": "HDT", "type": "ResearchActivity"}]}

Example input:
Sentence: These results revealed great diversity of both owners and flocks , characterized by wide variations in flock sizes and composition .

Example answer:
{"entities": [{"text": "owners", "type": "PopulationGroup"}]}

Example input:
Sentence: Flock health parameters revealed inconsistent use of medical interventions , such as vaccinations , treatments , and veterinary consultation .

Example answer:
{"entities": [{"text": "medical interventions", "type": "HealthCareActivity"}, {"text": "vaccinations", "type": "HealthCareActivity"}, {"text": "treatments", "type": "HealthCareActivity"}, {"text": "veterinary consultation", "type": "HealthCareActivity"}]}

Example input:
Sentence: It explores the motives , experiences and attitudes of egg sharers and their views towards donor anonymity and disclosure .

Example answer:
{"entities": [{"text": "experiences", "type": "BiologicFunction"}, {"text": "attitudes", "type": "BiologicFunction"}, {"text": "egg sharers", "type": "PopulationGroup"}, {"text": "donor", "type": "PopulationGroup"}]}

Example input:
Sentence: Information on flock demographics and bird health , as well as production and biosecurity practices , were gathered and analyzed from 206 surveys , representing respondents from 43 counties .

Example answer:
{"entities": [{"text": "demographics", "type": "ResearchActivity"}, {"text": "surveys", "type": "IntellectualProduct"}, {"text": "respondents", "type": "PopulationGroup"}, {"text": "counties", "type": "SpatialConcept"}]}

Example input:
Sentence: A systematic review investigating psychosocial aspects of egg sharing in the United Kingdom and their potential effects on egg donation numbers This review aims to provide an up - to - date knowledge of the psychosocial aspects of egg donation from the perspectives of the egg share donor and their recipient .

Example answer:
{"entities": [{"text": "systematic review", "type": "IntellectualProduct"}, {"text": "United Kingdom", "type": "SpatialConcept"}, {"text": "review", "type": "IntellectualProduct"}, {"text": "knowledge", "type": "IntellectualProduct"}, {"text": "egg share donor", "type": "PopulationGroup"}, {"text": "recipient", "type": "PopulationGroup"}]}

Example input:
Sentence: 1 % of owners reported having more than one type of bird in their flock , with many owners never , or only sometimes , separating flocks based on species or purpose .

Example answer:
{"entities": [{"text": "owners", "type": "PopulationGroup"}, {"text": "bird", "type": "Eukaryote"}]}

Input:
Sentence: Personal consumption ( 81 . 8 % ) and sale of eggs ( 48 . 2 % ) were the most frequently cited purposes for owning a flock .

## Item MedMentions:test:3726
Example input:
Sentence: We tested the function of an upregulated LDP , S100a10 , in vivo with adenovirus -mediated gene silencing and found , unexpectedly , that knockdown of S100a10 accelerated progression of HFD - induced liver steatosis .

Example answer:
{"entities": [{"text": "upregulated", "type": "BiologicFunction"}, {"text": "LDP", "type": "Chemical"}, {"text": "S100a10", "type": "AnatomicalStructure"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "adenovirus", "type": "Virus"}, {"text": "gene silencing", "type": "BiologicFunction"}, {"text": "knockdown", "type": "BiologicFunction"}, {"text": "HFD", "type": "Food"}, {"text": "liver steatosis", "type": "BiologicFunction"}]}

Example input:
Sentence: We found that senecionine administration increased serum alanine aminotransferase levels in mice .

Example answer:
{"entities": [{"text": "senecionine", "type": "Chemical"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "increased serum alanine aminotransferase levels", "type": "Finding"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: However , Drp1 , a marker of mitochondrial fission , was less in simvastatin treated mice , independent of exercise training , and there was a significant interaction between training and statin treatment ( P < 0 . 022 ) for LC3 - II protein content , a marker of autophagy flux .

Example answer:
{"entities": [{"text": "Drp1", "type": "Chemical"}, {"text": "marker", "type": "ClinicalAttribute"}, {"text": "mitochondrial fission", "type": "BiologicFunction"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "LC3 - II protein", "type": "Chemical"}, {"text": "autophagy", "type": "BiologicFunction"}]}

Example input:
Sentence: Pharmacological disruption of the profission protein Drp1 with Mdivi - 1 during LG exposure reduced mitochondrial fragmentation among vascular endothelial cells ( LG : 0 . 469 ; LG + Mdivi - 1 : 0 . 276 ; P = 0 . 003 ) , prevented formation of vascular ROS ( LG : 2 . 036 ; LG + Mdivi - 1 : 1 . 774 ; P = 0 . 005 ) , increased the presence of NO ( LG : 1 . 352 ; LG + Mdivi - 1 : 1 . 502 ; P = 0 . 048 ) , and improved vascular dilation response to acetylcholine ( LG : 31 . 6 % ; LG + Mdivi - 1 ; 78 . 5 % at maximum dose ; P < 0 .

Example answer:
{"entities": [{"text": "profission protein", "type": "Chemical"}, {"text": "Drp1", "type": "Chemical"}, {"text": "Mdivi - 1", "type": "Chemical"}, {"text": "LG", "type": "Chemical"}, {"text": "mitochondrial fragmentation", "type": "BiologicFunction"}, {"text": "vascular endothelial cells", "type": "AnatomicalStructure"}, {"text": "vascular", "type": "AnatomicalStructure"}, {"text": "presence", "type": "Finding"}, {"text": "NO", "type": "Chemical"}, {"text": "improved", "type": "Finding"}, {"text": "vascular dilation", "type": "BiologicFunction"}, {"text": "acetylcholine", "type": "Chemical"}]}

Example input:
Sentence: Disruption of Drp1 and subsequent mitochondrial fragmentation events prevents impaired vascular dilation , restores mitochondrial phenotype , and implicates mitochondrial fission as a primary mediator of LG - induced endothelial dysfunction .NEW & NOTEWORTHY Acute low - glucose exposure induces mitochondrial fragmentation in endothelial cells via Drp1 and is associated with impaired endothelial function in human arterioles .

Example answer:
{"entities": [{"text": "Drp1", "type": "Chemical"}, {"text": "mitochondrial fragmentation", "type": "BiologicFunction"}, {"text": "vascular dilation", "type": "BiologicFunction"}, {"text": "mitochondrial", "type": "AnatomicalStructure"}, {"text": "mitochondrial fission", "type": "BiologicFunction"}, {"text": "LG", "type": "Chemical"}, {"text": "endothelial dysfunction", "type": "BiologicFunction"}, {"text": "low - glucose", "type": "Chemical"}, {"text": "endothelial cells", "type": "AnatomicalStructure"}, {"text": "endothelial", "type": "AnatomicalStructure"}, {"text": "function", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "arterioles", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In the present study , we determined the hepatotoxicity and molecular mechanisms of senecionine , one of the most common toxic PAs , in primary cultured mouse and human hepatocytes as well as in mice .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "InjuryOrPoisoning"}, {"text": "molecular mechanisms", "type": "BiologicFunction"}, {"text": "senecionine", "type": "Chemical"}, {"text": "toxic", "type": "Chemical"}, {"text": "PAs", "type": "Chemical"}, {"text": "cultured", "type": "HealthCareActivity"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "human", "type": "Eukaryote"}, {"text": "hepatocytes", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Inhibition of Drp1 protects against senecionine - induced mitochondria -mediated apoptosis in primary hepatocytes and in mice Pyrrolizidine alkaloids ( PAs ) are a group of compounds found in various plants and some of them are widely consumed in the world as herbal medicines and food supplements .

Example answer:
{"entities": [{"text": "Inhibition", "type": "BiologicFunction"}, {"text": "Drp1", "type": "Chemical"}, {"text": "senecionine", "type": "Chemical"}, {"text": "mitochondria", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "hepatocytes", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "Pyrrolizidine alkaloids", "type": "Chemical"}, {"text": "PAs", "type": "Chemical"}, {"text": "compounds", "type": "Chemical"}, {"text": "plants", "type": "Eukaryote"}, {"text": "herbal medicines", "type": "Chemical"}, {"text": "food supplements", "type": "Food"}]}

Example input:
Sentence: Pharmacological inhibition of dynamin - related protein1 ( Drp1 ) , a protein that is critical to regulate mitochondrial fission , blocked senecionine - induced mitochondrial fragmentation and mitochondrial release of cytochrome c and apoptosis .

Example answer:
{"entities": [{"text": "inhibition", "type": "BiologicFunction"}, {"text": "dynamin - related protein1", "type": "Chemical"}, {"text": "Drp1", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}, {"text": "regulate mitochondrial fission", "type": "BiologicFunction"}, {"text": "senecionine", "type": "Chemical"}, {"text": "mitochondrial fragmentation", "type": "BiologicFunction"}, {"text": "mitochondrial", "type": "AnatomicalStructure"}, {"text": "cytochrome c", "type": "Chemical"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Interestingly , senecionine also caused marked mitochondria fragmentation in hepatocytes .

Example answer:
{"entities": [{"text": "senecionine", "type": "Chemical"}, {"text": "mitochondria fragmentation", "type": "BiologicFunction"}, {"text": "hepatocytes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: More importantly , hepatocyte -specific Drp1 knockout mice were resistant to senecionine - induced liver injury due to decreased mitochondrial damage and apoptosis .

Example answer:
{"entities": [{"text": "hepatocyte", "type": "AnatomicalStructure"}, {"text": "Drp1", "type": "Chemical"}, {"text": "knockout mice", "type": "Eukaryote"}, {"text": "senecionine", "type": "Chemical"}, {"text": "liver injury", "type": "InjuryOrPoisoning"}, {"text": "mitochondrial damage", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Input:
Sentence: In conclusion , our results uncovered a novel mechanism of Drp1 -mediated mitochondrial fragmentation in senecionine - induced liver injury .

## Item MedMentions:test:3553
Example input:
Sentence: Increased CVD risk ( ≥10 % 10 - year Framingham risk score ) was present for 13 % of the cohort ; 79 % of the cohort had ≥1 cardiometabolic comorbidity , 48 % had ≥2 , and 13 % had all three .

Example answer:
{"entities": [{"text": "CVD", "type": "BiologicFunction"}, {"text": "risk", "type": "HealthCareActivity"}, {"text": "10 - year Framingham risk score", "type": "Finding"}, {"text": "present", "type": "Finding"}, {"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: However , there were no consistent results in ischemic cerebrovascular disease and hemorrhagic cerebrovascular disease for men or cardio - cerebrovascular disease for women .

Example answer:
{"entities": [{"text": "cerebrovascular disease", "type": "BiologicFunction"}, {"text": "men", "type": "PopulationGroup"}, {"text": "cardio", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Respective unadjusted 5 - year risks for new - onset diabetes mellitus , cardiovascular death , and the composite cardiovascular outcome were 33 % , 0 . 4 % , and 4 % for Asia ; 34 % , 2 % , and 6 % for Europe ; 37 % , 4 % , and 8 % for Latin America ; 38 % , 2 % , and 6 % for North America ; and 32 % , 4 % , and 8 % for Australia , New Zealand , and South Africa .

Example answer:
{"entities": [{"text": "cardiovascular", "type": "SpatialConcept"}, {"text": "death", "type": "Finding"}, {"text": "outcome", "type": "ResearchActivity"}, {"text": "Asia", "type": "SpatialConcept"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "Latin America", "type": "SpatialConcept"}, {"text": "North America", "type": "SpatialConcept"}, {"text": "Australia", "type": "SpatialConcept"}, {"text": "New Zealand", "type": "SpatialConcept"}, {"text": "South Africa", "type": "SpatialConcept"}]}

Example input:
Sentence: When stratified by age group , subjects aged 20 - 39 years had a higher risk of stroke and many CV risk factors .

Example answer:
{"entities": [{"text": "stroke", "type": "BiologicFunction"}, {"text": "CV", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}]}

Example input:
Sentence: A 1 - year period of Workers ' General Health Examinations in non - office workers had a more significant prevention effect on ischemic heart disease than a 2 - year period in office workers among working age ( 40s - 50s ) men .

Example answer:
{"entities": [{"text": "Workers", "type": "PopulationGroup"}, {"text": "General Health Examinations", "type": "HealthCareActivity"}, {"text": "non - office workers", "type": "PopulationGroup"}, {"text": "prevention", "type": "HealthCareActivity"}, {"text": "ischemic heart disease", "type": "BiologicFunction"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: Age - sex adjusted hazard ratios were highest in the 45 - 64 years group : for major CVD s , HR ( no qualifications vs university degree ) = 1 . 62 ( 95 % CI : 1 . 49 - 1 . 77 ) for primary events , and HR = 1 . 49

Example answer:
{"entities": [{"text": "CVD", "type": "BiologicFunction"}, {"text": "university degree", "type": "IntellectualProduct"}, {"text": "primary", "type": "BiologicFunction"}]}

Example input:
Sentence: It is , however , necessary to consider that prevention of cardio - cerebrovascular disease can be partially explained by their occupational characteristics rather than by health examination period .

Example answer:
{"entities": [{"text": "prevention", "type": "HealthCareActivity"}, {"text": "cardio", "type": "BiologicFunction"}, {"text": "cerebrovascular disease", "type": "BiologicFunction"}]}

Example input:
Sentence: We identified newly occurring cardio - cerebrovascular disease over 7 years ( from 2007 to 2013 ) .

Example answer:
{"entities": [{"text": "cardio", "type": "BiologicFunction"}, {"text": "cerebrovascular disease", "type": "BiologicFunction"}]}

Example input:
Sentence: The compliant group presented a lower cumulative incidence of cardio - cerebrovascular disease than the non - compliant group ; this result was consistent across sex , working age ( 40s and 50s ) , and workplace policyholder .

Example answer:
{"entities": [{"text": "compliant group", "type": "PopulationGroup"}, {"text": "cardio", "type": "BiologicFunction"}, {"text": "cerebrovascular disease", "type": "BiologicFunction"}, {"text": "non - compliant group", "type": "PopulationGroup"}, {"text": "workplace", "type": "SpatialConcept"}]}

Example input:
Sentence: Relative risk of cardio - cerebrovascular disease by health examination period ( 1 and 2 years ) showed statistically significant results in ischemic heart disease for male participants .

Example answer:
{"entities": [{"text": "cardio", "type": "BiologicFunction"}, {"text": "cerebrovascular disease", "type": "BiologicFunction"}, {"text": "ischemic heart disease", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}]}

Input:
Sentence: After stratification by age , sex , and national health insurance type , we identified 7 years ' cumulative incidence of cardio - cerebrovascular disease by health examination compliance and estimated its relative risk by health examination period and compliance .

## Item MedMentions:test:3790
Example input:
Sentence: Of particular interest are milk biomarkers , which together with infrared spectra prediction equations can provide useful tools for genetic selection .

Example answer:
{"entities": [{"text": "milk", "type": "BodySubstance"}, {"text": "biomarkers", "type": "ClinicalAttribute"}, {"text": "infrared spectra", "type": "HealthCareActivity"}, {"text": "genetic selection", "type": "BiologicFunction"}]}

Example input:
Sentence: Genomic EBV for the separate fertility traits were also computed , in univariate models .

Example answer:
{"entities": [{"text": "fertility", "type": "BiologicFunction"}]}

Example input:
Sentence: We show that microbiomes isolated from each sample type are distinct , and specifically , that octocoral species type had the greatest effect on predicting the composition of the Muricea microbiome .

Example answer:
{"entities": [{"text": "octocoral", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "composition", "type": "ClinicalAttribute"}, {"text": "Muricea", "type": "Eukaryote"}]}

Example input:
Sentence: Our coalescent simulations revealed that the finite sample correction of θWC is necessary to assess population structure using pairwise FST values .

Example answer:
{"entities": [{"text": "simulations", "type": "ResearchActivity"}, {"text": "pairwise FST", "type": "IntellectualProduct"}]}

Example input:
Sentence: This study provides a benchmark for metagenomic sequencing application as is required for virus detection in complex food matrices using a culture -independent diagnostic approach .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "metagenomic sequencing application", "type": "ResearchActivity"}, {"text": "virus detection", "type": "HealthCareActivity"}, {"text": "food", "type": "Food"}, {"text": "culture", "type": "HealthCareActivity"}, {"text": "diagnostic approach", "type": "HealthCareActivity"}]}

Example input:
Sentence: The dimensionality of the data as well as complex relationships between microbiota and host genomics pose considerable challenges for analysis .

Example answer:
{"entities": [{"text": "dimensionality", "type": "SpatialConcept"}, {"text": "genomics", "type": "AnatomicalStructure"}, {"text": "challenges", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: The use of informativity in the development of robust viromics -based examinations Metagenomics -based studies have provided insight into many of the complex microbial communities responsible for maintaining life on this planet .

Example answer:
{"entities": [{"text": "robust viromics", "type": "AnatomicalStructure"}, {"text": "examinations", "type": "ResearchActivity"}, {"text": "maintaining life on this planet", "type": "HealthCareActivity"}]}

Example input:
Sentence: A fast small - sample kernel independence test for microbiome community - level association analysis To fully understand the role of microbiome in human health and diseases , researchers are increasingly interested in assessing the relationship between microbiome composition and host genomic data .

Example answer:
{"entities": [{"text": "fast small - sample kernel independence test", "type": "IntellectualProduct"}, {"text": "level association analysis", "type": "ResearchActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "researchers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "genomic", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The KRV statistic can capture nonlinear correlations and complex relationships among the individual data types and between gene expression and microbiome composition through measuring general dependency .

Example answer:
{"entities": [{"text": "KRV statistic", "type": "IntellectualProduct"}, {"text": "gene expression", "type": "BiologicFunction"}]}

Example input:
Sentence: In this article , we apply a kernel RV coefficient ( KRV ) test to evaluate the overall association between host gene expression and microbiome composition .

Example answer:
{"entities": [{"text": "kernel RV coefficient ( KRV ) test", "type": "IntellectualProduct"}, {"text": "gene expression", "type": "BiologicFunction"}]}

Input:
Sentence: Simulation studies show that KRV is useful in testing statistical independence with finite samples given the kernels are appropriately chosen , and can powerfully identify existing associations between microbiome composition and host genomic data while protecting type I error .

## Item MedMentions:test:3769
Example input:
Sentence: Histopathologic and immunohistochemical examination confirmed the diagnosis of an EOS .

Example answer:
{"entities": [{"text": "Histopathologic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "diagnosis", "type": "Finding"}, {"text": "EOS", "type": "BiologicFunction"}]}

Example input:
Sentence: Based on a review of over 1000 published HPS and POPH articles identified via a MEDLINE search ( 1985 - 2015 ) , clinical guidelines were based on , selected single care reports , small series , registries , databases , and expert opinion .

Example answer:
{"entities": [{"text": "HPS", "type": "BiologicFunction"}, {"text": "POPH", "type": "BiologicFunction"}, {"text": "MEDLINE search", "type": "IntellectualProduct"}, {"text": "clinical guidelines", "type": "IntellectualProduct"}, {"text": "selected single care reports", "type": "HealthCareActivity"}, {"text": "registries", "type": "IntellectualProduct"}, {"text": "databases", "type": "IntellectualProduct"}]}

Example input:
Sentence: Physical examination and X - ray films were taken to rule out any spinal disorder .

Example answer:
{"entities": [{"text": "Physical examination", "type": "HealthCareActivity"}, {"text": "X - ray films", "type": "MedicalDevice"}, {"text": "spinal disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: Histopathology remains the gold standard in diagnosing the disease .

Example answer:
{"entities": [{"text": "Histopathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "diagnosing", "type": "Finding"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: The patient sustained a trauma to his left arm , and QSS was successfully diagnosed by physical examination , magnetic resonance image , electromyographic evaluation , and nerve conduction studies .

Example answer:
{"entities": [{"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "left arm", "type": "AnatomicalStructure"}, {"text": "QSS", "type": "BiologicFunction"}, {"text": "diagnosed", "type": "Finding"}, {"text": "physical examination", "type": "HealthCareActivity"}, {"text": "magnetic resonance image", "type": "HealthCareActivity"}, {"text": "nerve conduction studies", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients ' symptomatology was assessed by means of the Positive and Negative Syndrome Scale ( PANSS ) .

Example answer:
{"entities": [{"text": "symptomatology", "type": "Finding"}, {"text": "Positive and Negative Syndrome Scale", "type": "IntellectualProduct"}, {"text": "PANSS", "type": "IntellectualProduct"}]}

Example input:
Sentence: Criteria sets for primary Sjogren 's syndrome are not adequate for those presenting with extraglandular organ involvements as their dominant clinical features Patients with primary Sjogren 's syndrome ( pSS ) may go undiagnosed or be misclassified due to the insidious nature and wide spectrum of the disease .

Example answer:
{"entities": [{"text": "Criteria", "type": "IntellectualProduct"}, {"text": "primary Sjogren 's syndrome", "type": "BiologicFunction"}, {"text": "organ", "type": "AnatomicalStructure"}, {"text": "dominant clinical features", "type": "Finding"}, {"text": "pSS", "type": "BiologicFunction"}, {"text": "undiagnosed", "type": "Finding"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: In all cases , diagnosis was confirmed by histological analysis .

Example answer:
{"entities": [{"text": "diagnosis", "type": "ResearchActivity"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: A diagnosis of PNSC was made in 17 . 6 % of all patients referred during the 15 - month study period .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "PNSC", "type": "BiologicFunction"}]}

Example input:
Sentence: Diagnosis is typically based on clinical history and a strong suspicion of this syndrome .

Example answer:
{"entities": [{"text": "Diagnosis", "type": "Finding"}, {"text": "clinical history", "type": "Finding"}, {"text": "suspicion", "type": "BiologicFunction"}, {"text": "syndrome", "type": "BiologicFunction"}]}

Input:
Sentence: Diagnosis of pSS was made on the clinical basis by the expert opinion .

## Item MedMentions:test:3624
Example input:
Sentence: As fish progressed through the harvest event , cook loss decreased , tenderness increased , and pH increased , indicating that stress induced textural changes .

Example answer:
{"entities": []}

Example input:
Sentence: In this study we combined this feeding medium method with a loop - mediated isothermal amplification ( LAMP ) assay to study 627 insect specimens of 11 Hemiptera taxa sampled from sites in Papua New Guinea affected by Bogia coconut syndrome ( BCS ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "feeding medium method", "type": "HealthCareActivity"}, {"text": "loop - mediated isothermal amplification ( LAMP ) assay", "type": "HealthCareActivity"}, {"text": "insect", "type": "Eukaryote"}, {"text": "Hemiptera taxa", "type": "Eukaryote"}, {"text": "Papua New Guinea", "type": "SpatialConcept"}, {"text": "Bogia coconut syndrome", "type": "BiologicFunction"}, {"text": "BCS", "type": "BiologicFunction"}]}

Example input:
Sentence: Fluorescence recovery after photobleaching ( FRAP ) microscopy is used to probe the diffusion properties of TATS in isolated rat cardiomyocytes : A fluorescent dextran inside TATS lumen is photobleached , and signal recovery by diffusion of unbleached dextran from the extracellular space is monitored .

Example answer:
{"entities": [{"text": "Fluorescence recovery after photobleaching", "type": "HealthCareActivity"}, {"text": "FRAP", "type": "HealthCareActivity"}, {"text": "microscopy", "type": "HealthCareActivity"}, {"text": "probe", "type": "ResearchActivity"}, {"text": "properties", "type": "BiologicFunction"}, {"text": "TATS", "type": "AnatomicalStructure"}, {"text": "rat", "type": "Eukaryote"}, {"text": "cardiomyocytes", "type": "AnatomicalStructure"}, {"text": "fluorescent dextran", "type": "Chemical"}, {"text": "lumen", "type": "SpatialConcept"}, {"text": "dextran", "type": "Chemical"}, {"text": "extracellular space", "type": "SpatialConcept"}, {"text": "monitored", "type": "HealthCareActivity"}]}

Example input:
Sentence: Furthermore , the abundance of sponges in the Hirnantian sequence of South China may have aided post - extinction ecosystem recovery by stabilizing the sediment surface , allowing sessile suspension feeders such as brachiopods , corals , and bryozoans to recover rapidly .

Example answer:
{"entities": [{"text": "sponges", "type": "Eukaryote"}, {"text": "South China", "type": "SpatialConcept"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "brachiopods", "type": "Eukaryote"}, {"text": "corals", "type": "Eukaryote"}, {"text": "bryozoans", "type": "Eukaryote"}]}

Example input:
Sentence: Flourishing Sponge -Based Ecosystems after the End - Ordovician Mass Extinction The Late Ordovician ( Hirnantian , approximately 445 million years ago ) extinction event was among the largest known , with 85 % species loss [ 1 ] .

Example answer:
{"entities": [{"text": "Sponge", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: Caribbean massive corals not recovering from repeated thermal stress events during 2005 - 2013 Massive coral bleaching events associated with high sea surface temperatures are forecast to become more frequent and severe in the future due to climate change .

Example answer:
{"entities": [{"text": "Caribbean", "type": "SpatialConcept"}, {"text": "massive corals", "type": "Eukaryote"}, {"text": "Massive coral", "type": "Eukaryote"}, {"text": "sea", "type": "SpatialConcept"}, {"text": "surface", "type": "SpatialConcept"}]}

Example input:
Sentence: Monitoring colony recovery from bleaching disturbances over multiyear time frames is important for improving predictions of future coral community changes .

Example answer:
{"entities": [{"text": "Monitoring", "type": "ResearchActivity"}, {"text": "coral", "type": "Eukaryote"}]}

Example input:
Sentence: Following this event , all species again lost tissue , with previously unbleached colony species groups experiencing greater declines than conspecific sample groups , which were previously bleached , indicating a possible positive acclimative response .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "acclimative response", "type": "BiologicFunction"}]}

Example input:
Sentence: We recorded colony pigmentation and size for bleached and unbleached groups of co - located conspecifics of three major reef - building scleractinian corals ( Orbicella franksi , Siderastrea siderea , and Stephanocoenia michelini ; n = 198 total ) in Bocas del Toro , Panama , during the major 2005 bleaching event and then monitored pigmentation status and changes live tissue colony size for 8 years ( 2005 - 2013 ) .

Example answer:
{"entities": [{"text": "size", "type": "SpatialConcept"}, {"text": "reef - building scleractinian", "type": "Eukaryote"}, {"text": "corals", "type": "Eukaryote"}, {"text": "Orbicella franksi", "type": "Eukaryote"}, {"text": "Siderastrea siderea", "type": "Eukaryote"}, {"text": "Stephanocoenia michelini", "type": "Eukaryote"}, {"text": "Panama", "type": "SpatialConcept"}, {"text": "monitored", "type": "ResearchActivity"}, {"text": "live tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: However , despite this beneficial effect for previously bleached corals , all groups experienced substantial net tissue loss between 2005 and 2013 , indicating that many important Caribbean reef - building corals will likely suffer continued tissue loss and may be unable to maintain current benthic coverage when faced with future thermal stress forecast for the region , even with potential benefits from bleaching -related acclimation .

Example answer:
{"entities": [{"text": "corals", "type": "Eukaryote"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "Caribbean", "type": "SpatialConcept"}, {"text": "reef - building corals", "type": "Eukaryote"}, {"text": "region", "type": "SpatialConcept"}, {"text": "acclimation", "type": "BiologicFunction"}]}

Input:
Sentence: Corals that were bleached in 2005 demonstrated markedly different response trajectories compared to unbleached colony groups , with extensive live tissue loss for bleached corals of all species following bleaching , with mean live tissue losses per colony 9 months postbleaching of 26 .

## Item MedMentions:test:3791
Example input:
Sentence: A fast small - sample kernel independence test for microbiome community - level association analysis To fully understand the role of microbiome in human health and diseases , researchers are increasingly interested in assessing the relationship between microbiome composition and host genomic data .

Example answer:
{"entities": [{"text": "fast small - sample kernel independence test", "type": "IntellectualProduct"}, {"text": "level association analysis", "type": "ResearchActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "researchers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "genomic", "type": "AnatomicalStructure"}]}

Example input:
Sentence: These findings demonstrate that the composition of the small intestinal microbiome is affected differently in diet - and genetically - induced obesity , but both are associated with elevated intestinal inflammation and alterations of the Wnt pathway towards enhancing tumorigenesis .

Example answer:
{"entities": [{"text": "diet", "type": "Food"}, {"text": "genetically - induced", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "intestinal inflammation", "type": "Finding"}, {"text": "Wnt pathway", "type": "BiologicFunction"}, {"text": "tumorigenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Gut microbiome alterations in patients with stage 4 hepatitis C Hepatitis C virus ( HCV ) causes debilitating liver diseases , which may progress to cirrhosis and cancer , and claims 500 , 000 annual lives worldwide .

Example answer:
{"entities": [{"text": "hepatitis C", "type": "BiologicFunction"}, {"text": "Hepatitis C virus", "type": "Virus"}, {"text": "HCV", "type": "Virus"}, {"text": "liver diseases", "type": "BiologicFunction"}, {"text": "cirrhosis", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: To this end , we analyzed stool samples from six stage 4 - HCV patients and eight healthy individuals by high - throughput 16S rRNA gene sequencing using Illumina MiSeq .

Example answer:
{"entities": [{"text": "stool samples", "type": "BodySubstance"}, {"text": "HCV", "type": "Virus"}, {"text": "healthy individuals", "type": "PopulationGroup"}, {"text": "16S rRNA gene sequencing", "type": "HealthCareActivity"}, {"text": "Illumina MiSeq", "type": "MedicalDevice"}]}

Example input:
Sentence: Overall , the alpha - diversity of the healthy persons ' gut microbiomes was higher than those of the HCV patients .

Example answer:
{"entities": [{"text": "healthy persons '", "type": "PopulationGroup"}, {"text": "HCV", "type": "Virus"}]}

Example input:
Sentence: Analysis of Gene Ontology suggested that transcription from the RNA polymerase II promoter and the RNA biosynthetic process were enriched , and pathway analyses suggested that oxidative phosphorylation , as well as the T cell receptor and Interleukin - 17 ( IL - 17 ) signalling pathways might be activated by IBDV infection .

Example answer:
{"entities": [{"text": "Analysis", "type": "ResearchActivity"}, {"text": "Gene Ontology", "type": "IntellectualProduct"}, {"text": "transcription from the RNA polymerase II promoter", "type": "BiologicFunction"}, {"text": "RNA biosynthetic process", "type": "BiologicFunction"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "analyses", "type": "ResearchActivity"}, {"text": "oxidative phosphorylation", "type": "BiologicFunction"}, {"text": "T cell receptor", "type": "Chemical"}, {"text": "Interleukin - 17", "type": "Chemical"}, {"text": "IL - 17", "type": "Chemical"}, {"text": "signalling pathways", "type": "BiologicFunction"}, {"text": "IBDV", "type": "Virus"}, {"text": "infection", "type": "BiologicFunction"}]}

Example input:
Sentence: In the present study , we performed de novo transcriptome sequencing to produce a comprehensive transcript dataset of visceral mass tissue of K .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "transcriptome sequencing", "type": "HealthCareActivity"}, {"text": "transcript", "type": "Chemical"}, {"text": "dataset", "type": "IntellectualProduct"}, {"text": "visceral mass tissue", "type": "AnatomicalStructure"}, {"text": "K .", "type": "Eukaryote"}]}

Example input:
Sentence: A microbial signature for Crohn 's disease A decade of microbiome studies has linked IBD to an alteration in the gut microbial community of genetically predisposed subjects .

Example answer:
{"entities": [{"text": "Crohn 's disease", "type": "BiologicFunction"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "IBD", "type": "BiologicFunction"}, {"text": "gut", "type": "AnatomicalStructure"}, {"text": "subjects", "type": "PopulationGroup"}]}

Example input:
Sentence: The KRV statistic can capture nonlinear correlations and complex relationships among the individual data types and between gene expression and microbiome composition through measuring general dependency .

Example answer:
{"entities": [{"text": "KRV statistic", "type": "IntellectualProduct"}, {"text": "gene expression", "type": "BiologicFunction"}]}

Example input:
Sentence: In this article , we apply a kernel RV coefficient ( KRV ) test to evaluate the overall association between host gene expression and microbiome composition .

Example answer:
{"entities": [{"text": "kernel RV coefficient ( KRV ) test", "type": "IntellectualProduct"}, {"text": "gene expression", "type": "BiologicFunction"}]}

Input:
Sentence: We apply the KRV to a microbiome study examining the relationship between host transcriptome and microbiome composition within the context of inflammatory bowel disease and are able to derive new biological insights and provide formal inference on prior qualitative observations .

## Item MedMentions:test:3479
Example input:
Sentence: Stretching red blood cells using optical tweezers is a way to characterize the mechanical properties of their membrane by measuring the size of the cell in the direction of the stretching ( axial diameter ) and perpendicularly ( transverse diameter ) .

Example answer:
{"entities": [{"text": "Stretching", "type": "HealthCareActivity"}, {"text": "red blood cells", "type": "AnatomicalStructure"}, {"text": "optical tweezers", "type": "ResearchActivity"}, {"text": "membrane", "type": "AnatomicalStructure"}, {"text": "direction", "type": "SpatialConcept"}, {"text": "stretching", "type": "HealthCareActivity"}]}

Example input:
Sentence: Directing traffic on DNA -How transcription factors relieve or induce transcriptional interference Transcriptional interference ( TI ) is increasingly recognized as a widespread mechanism of gene control , particularly given the pervasive nature of transcription , both sense and antisense , across all kingdoms of life .

Example answer:
{"entities": [{"text": "Directing traffic on DNA", "type": "BiologicFunction"}, {"text": "transcription factors", "type": "Chemical"}, {"text": "transcriptional interference", "type": "BiologicFunction"}, {"text": "Transcriptional interference", "type": "BiologicFunction"}, {"text": "TI", "type": "BiologicFunction"}, {"text": "widespread", "type": "SpatialConcept"}, {"text": "gene control", "type": "BiologicFunction"}, {"text": "transcription", "type": "BiologicFunction"}, {"text": "antisense", "type": "Chemical"}, {"text": "kingdoms", "type": "IntellectualProduct"}]}

Example input:
Sentence: In order to allow flexible and timely control over gene expression without the interference of native gene expression machinery , a large number of studies have focused on developing synthetic biology tools for orthogonal control of transcription .

Example answer:
{"entities": [{"text": "gene expression", "type": "BiologicFunction"}, {"text": "native gene expression machinery", "type": "BiologicFunction"}, {"text": "transcription", "type": "BiologicFunction"}]}

Example input:
Sentence: Phylogenetic trees based on the RNA - dependent RNA polymerase , heat shock protein 70 homolog , and coat protein showed that GLRaV - 13 had the closest , but still distant , relationship to GLRaV - 1 in the subgroup I cluster .

Example answer:
{"entities": [{"text": "RNA - dependent RNA polymerase", "type": "Chemical"}, {"text": "heat shock protein 70", "type": "Chemical"}, {"text": "coat protein", "type": "Chemical"}, {"text": "GLRaV - 13", "type": "Virus"}, {"text": "GLRaV - 1", "type": "Virus"}, {"text": "subgroup I", "type": "IntellectualProduct"}]}

Example input:
Sentence: An evolutionary conserved Hexim1 peptide binds to the Cdk9 catalytic site to inhibit P - TEFb The positive transcription elongation factor ( P - TEFb ) is required for the transcription of most genes by RNA polymerase II .

Example answer:
{"entities": [{"text": "evolutionary conserved Hexim1 peptide", "type": "Chemical"}, {"text": "binds", "type": "BiologicFunction"}, {"text": "Cdk9", "type": "Chemical"}, {"text": "P - TEFb", "type": "Chemical"}, {"text": "positive transcription elongation factor", "type": "Chemical"}, {"text": "transcription", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "RNA polymerase II", "type": "Chemical"}]}

Example input:
Sentence: Transcriptome profiling by RNA - sequencing determined the genome -wide patterns of expression of virulence factors both in vitro ( potato dextrose agar or medium amended with grape wood as substrate ) and in planta .

Example answer:
{"entities": [{"text": "Transcriptome profiling", "type": "HealthCareActivity"}, {"text": "RNA - sequencing", "type": "HealthCareActivity"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "virulence factors", "type": "Chemical"}, {"text": "potato", "type": "Food"}, {"text": "dextrose agar", "type": "Chemical"}, {"text": "medium", "type": "Chemical"}, {"text": "grape", "type": "Food"}, {"text": "planta", "type": "Eukaryote"}]}

Example input:
Sentence: Gene ontology enrichment analysis revealed that the gene set connected to the T18 differentially methylated CpGs was highly enriched for GO terms related to " DNA binding " and " transcription factor binding " coupled to the RNA polymerase II transcription .

Example answer:
{"entities": [{"text": "Gene ontology", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "gene set", "type": "AnatomicalStructure"}, {"text": "T18", "type": "BiologicFunction"}, {"text": "methylated", "type": "BiologicFunction"}, {"text": "CpGs", "type": "Chemical"}, {"text": "GO", "type": "IntellectualProduct"}, {"text": "DNA binding", "type": "BiologicFunction"}, {"text": "transcription factor binding", "type": "BiologicFunction"}, {"text": "RNA polymerase II", "type": "Chemical"}, {"text": "transcription", "type": "BiologicFunction"}]}

Example input:
Sentence: Maf1 -mediated regulation of yeast RNA polymerase III is correlated with CCA addition at the 3 ' end of tRNA precursors In eukaryotic cells tRNA synthesis is negatively regulated by the protein Maf1 , conserved from yeast to humans .

Example answer:
{"entities": [{"text": "Maf1", "type": "AnatomicalStructure"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "yeast", "type": "Eukaryote"}, {"text": "RNA polymerase III", "type": "Chemical"}, {"text": "CCA addition at the 3 ' end of tRNA", "type": "BiologicFunction"}, {"text": "eukaryotic cells", "type": "AnatomicalStructure"}, {"text": "tRNA synthesis", "type": "BiologicFunction"}, {"text": "negatively", "type": "Finding"}, {"text": "regulated", "type": "BiologicFunction"}, {"text": "protein Maf1", "type": "Chemical"}, {"text": "humans", "type": "Eukaryote"}]}

Example input:
Sentence: We give an overview of the latest results in the single - molecule transcription field , focusing on transcription by eukaryotic RNA polymerases .

Example answer:
{"entities": [{"text": "transcription", "type": "BiologicFunction"}, {"text": "eukaryotic", "type": "AnatomicalStructure"}, {"text": "RNA polymerases", "type": "Chemical"}]}

Example input:
Sentence: In this review , we emphasise the advantages of using single - molecule techniques , particularly optical tweezers , to study transcription dynamics .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "optical tweezers", "type": "ResearchActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "transcription", "type": "BiologicFunction"}]}

Input:
Sentence: Optical tweezers studies of transcription by eukaryotic RNA polymerases Transcription is the first step in the expression of genetic information and it is carried out by large macromolecular enzymes called RNA polymerases .

## Item MedMentions:test:3752
Example input:
Sentence: In subgroup analysis , β - blocker therapy was associated with better outcome , in terms of all - cause death , in patients with CTO of the left anterior descending coronary artery and Synergy Between PCI with Taxus and Cardiac Surgery ( SYNTAX ) score ≥23 ( P for interaction = 0 . 01 and 0 . 02 , respectively ) .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "all - cause death", "type": "Finding"}, {"text": "CTO", "type": "BiologicFunction"}, {"text": "left anterior descending coronary artery", "type": "AnatomicalStructure"}, {"text": "PCI", "type": "HealthCareActivity"}, {"text": "Cardiac Surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients with atrial fibrillation and isolated advanced age , low body weight , or renal dysfunction have a higher risk of stroke or systemic embolism and major bleeding but show consistent benefits with the 5 mg twice daily dose of apixaban vs warfarin compared with patients without these characteristics .

Example answer:
{"entities": [{"text": "atrial fibrillation", "type": "BiologicFunction"}, {"text": "renal dysfunction", "type": "Finding"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "bleeding", "type": "BiologicFunction"}, {"text": "apixaban", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}]}

Example input:
Sentence: Non - persistence was defined as a gap in dabigatran or rivaroxaban prescriptions ≥14 days .

Example answer:
{"entities": [{"text": "Non - persistence", "type": "Finding"}, {"text": "dabigatran", "type": "Chemical"}, {"text": "rivaroxaban", "type": "Chemical"}, {"text": "prescriptions", "type": "IntellectualProduct"}]}

Example input:
Sentence: After adjusting for age and sex , prior cardiovascular disease was less common in patients discharged on ticagrelor ( myocardial infarction , ischaemic stroke , and peripheral vascular disease ; P for all < 0 . 001 ) .

Example answer:
{"entities": [{"text": "cardiovascular disease", "type": "BiologicFunction"}, {"text": "less common", "type": "Finding"}, {"text": "discharged", "type": "HealthCareActivity"}, {"text": "ticagrelor", "type": "Chemical"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "ischaemic stroke", "type": "BiologicFunction"}, {"text": "peripheral vascular disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Warfarin treatment was associated with higher risk of bleeding in all eGFR groups and lower risk of stroke in patients with eGFR ≥15 mL / min per 1 .

Example answer:
{"entities": [{"text": "bleeding", "type": "BiologicFunction"}, {"text": "eGFR", "type": "HealthCareActivity"}, {"text": "stroke", "type": "BiologicFunction"}]}

Example input:
Sentence: A systematic review of the literature Dabigatran is a newly commercialized drug that is replacing other anticoagulants in the prevention of venous thromboembolism , stroke and systemic arterial valve embolism .

Example answer:
{"entities": [{"text": "review of the literature", "type": "IntellectualProduct"}, {"text": "Dabigatran", "type": "Chemical"}, {"text": "drug", "type": "Chemical"}, {"text": "anticoagulants", "type": "Chemical"}, {"text": "venous thromboembolism", "type": "BiologicFunction"}, {"text": "stroke", "type": "BiologicFunction"}]}

Example input:
Sentence: NOAC non - persistence rates are high in clinical practice , with approximately one in three patients becoming non - persistent to dabigatran or rivaroxaban within 6 months after drug initiation .

Example answer:
{"entities": [{"text": "NOAC", "type": "Chemical"}, {"text": "non - persistence", "type": "Finding"}, {"text": "clinical practice", "type": "IntellectualProduct"}, {"text": "non - persistent", "type": "Finding"}, {"text": "dabigatran", "type": "Chemical"}, {"text": "rivaroxaban", "type": "Chemical"}, {"text": "drug", "type": "Chemical"}]}

Example input:
Sentence: Early non - persistence with dabigatran and rivaroxaban in patients with atrial fibrillation Dabigatran and rivaroxaban are novel oral anticoagulants ( NOACs ) approved for stroke prevention in atrial fibrillation ( AF ) .

Example answer:
{"entities": [{"text": "non - persistence", "type": "Finding"}, {"text": "dabigatran", "type": "Chemical"}, {"text": "rivaroxaban", "type": "Chemical"}, {"text": "atrial fibrillation", "type": "BiologicFunction"}, {"text": "Dabigatran", "type": "Chemical"}, {"text": "novel oral anticoagulants", "type": "Chemical"}, {"text": "NOACs", "type": "Chemical"}, {"text": "stroke prevention", "type": "HealthCareActivity"}, {"text": "AF", "type": "BiologicFunction"}]}

Example input:
Sentence: At 6 months , 36 . 4 % of patients were non - persistent to dabigatran , while 31 .

Example answer:
{"entities": [{"text": "non - persistent", "type": "Finding"}, {"text": "dabigatran", "type": "Chemical"}]}

Example input:
Sentence: Risk of stroke / TIA was markedly higher in non - persistent patients to dabigatran ( HR 3 .

Example answer:
{"entities": [{"text": "stroke", "type": "BiologicFunction"}, {"text": "TIA", "type": "BiologicFunction"}, {"text": "non - persistent", "type": "Finding"}, {"text": "dabigatran", "type": "Chemical"}]}

Input:
Sentence: Stroke / TIA / death was significantly higher for those non - persistent to dabigatran ( HR 1 . 76 ( 95 % CI 1 .

## Item MedMentions:test:3630
Example input:
Sentence: After performing spinal anesthesia , dexmedetomidine was infused at a loading dose of 0 .

Example answer:
{"entities": [{"text": "spinal anesthesia", "type": "HealthCareActivity"}, {"text": "dexmedetomidine", "type": "Chemical"}, {"text": "infused", "type": "HealthCareActivity"}]}

Example input:
Sentence: Anticholinergic premedication to prevent bradycardia in combined spinal anesthesia and dexmedetomidine sedation : a randomized , double - blind , placebo - controlled study When dexmedetomidine is used in patients undergoing spinal anesthesia , high incidence of bradycardia in response to parasympathetic activation is reported .

Example answer:
{"entities": [{"text": "Anticholinergic", "type": "Chemical"}, {"text": "premedication", "type": "HealthCareActivity"}, {"text": "bradycardia", "type": "BiologicFunction"}, {"text": "spinal anesthesia", "type": "HealthCareActivity"}, {"text": "dexmedetomidine", "type": "Chemical"}, {"text": "sedation", "type": "HealthCareActivity"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "double - blind", "type": "ResearchActivity"}, {"text": "parasympathetic", "type": "BodySystem"}]}

Example input:
Sentence: Although motoneuronal output was 21 ± 12 % higher during FENT compared to CTRL ( P < 0 . 05 ) , time to complete the time trial was similar ( ∼8 . 8 min ) .

Example answer:
{"entities": [{"text": "motoneuronal", "type": "AnatomicalStructure"}, {"text": "FENT", "type": "BiologicFunction"}, {"text": "CTRL", "type": "Finding"}, {"text": "trial", "type": "ResearchActivity"}]}

Example input:
Sentence:  of patients were required to clinically intervene in heart rates reduction and none suffered respiratory depression after administrations of dexmedetomidine in either group .

Example answer:
{"entities": [{"text": "heart rates", "type": "ClinicalAttribute"}, {"text": "respiratory depression", "type": "BiologicFunction"}, {"text": "administrations", "type": "HealthCareActivity"}, {"text": "dexmedetomidine", "type": "Chemical"}]}

Example input:
Sentence: It might be worthwhile for patients to receive dexmedetomidine before the induction of anesthesia in ECT .

Example answer:
{"entities": [{"text": "dexmedetomidine", "type": "Chemical"}, {"text": "induction of anesthesia", "type": "HealthCareActivity"}, {"text": "ECT", "type": "HealthCareActivity"}]}

Example input:
Sentence: There was no significant difference in motor or EEG seizure duration between dexmedetomidine and nondexmedetomidine groups [ motor : 6 studies ; mean difference ( MD ) , 1 . 62 ; 95 % confidence interval ( CI ) , -2 . 24 to 5 . 49 ; P = 0 . 41 ; EEG : 3 studies ; MD , 2 . 34 ; 95 % CI , -6 . 03 to 10 . 71 ; P = 0 . 58 ] .

Example answer:
{"entities": [{"text": "motor", "type": "Finding"}, {"text": "EEG seizure", "type": "Finding"}, {"text": "duration", "type": "Finding"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: Besides , the addition of dexmedetomidine in ECT did not prolong recovery time when reduced - dose propofol was used .

Example answer:
{"entities": [{"text": "dexmedetomidine", "type": "Chemical"}, {"text": "ECT", "type": "HealthCareActivity"}, {"text": "propofol", "type": "Chemical"}]}

Example input:
Sentence: Dexmedetomidine Combined With Intravenous Anesthetics in Electroconvulsive Therapy : A Meta - analysis and Systematic Review The aim of this study was to investigate how the combined use of dexmedetomidine with intravenous anesthetics influences seizure duration and circulatory dynamics in electroconvulsive therapy ( ECT ) .

Example answer:
{"entities": [{"text": "Dexmedetomidine", "type": "Chemical"}, {"text": "Intravenous Anesthetics", "type": "Chemical"}, {"text": "Electroconvulsive Therapy", "type": "HealthCareActivity"}, {"text": "Meta - analysis", "type": "ResearchActivity"}, {"text": "Systematic Review", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "dexmedetomidine", "type": "Chemical"}, {"text": "intravenous anesthetics", "type": "Chemical"}, {"text": "seizure duration", "type": "Finding"}, {"text": "electroconvulsive therapy", "type": "HealthCareActivity"}, {"text": "ECT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Both maximum MAP and HR after ECT were significantly reduced in the dexmedetomidine group ( MAP : 6 studies ; MD , -4 . 83 ; 95 % CI , -8 .

Example answer:
{"entities": [{"text": "MAP", "type": "Finding"}, {"text": "HR", "type": "ClinicalAttribute"}, {"text": "ECT", "type": "HealthCareActivity"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: A literature search was performed to identify studies that evaluated the effect of dexmedetomidine on motor - or electroencephalogram ( EEG ) - based seizure duration s and maximum mean arterial pressure ( MAP ) and heart rate ( HR ) after ECT .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "dexmedetomidine", "type": "Chemical"}, {"text": "motor", "type": "Finding"}, {"text": "electroencephalogram", "type": "Finding"}, {"text": "( EEG ) - based seizure", "type": "Finding"}, {"text": "duration", "type": "Finding"}, {"text": "mean arterial pressure", "type": "Finding"}, {"text": "MAP", "type": "Finding"}, {"text": "heart rate", "type": "ClinicalAttribute"}, {"text": "HR", "type": "ClinicalAttribute"}, {"text": "ECT", "type": "HealthCareActivity"}]}

Input:
Sentence: The use of dexmedetomidine in ECT did not interfere with motor and EEG seizure duration s but could reduce maximum MAP and HR after ECT .

## Item MedMentions:test:3913
Example input:
Sentence: On logistic regression analysis , smaller size ( < 3 mm ) without complete occlusion related to recanalization ( OR , 8 . 0 , 95 % CI , 1 . 3 - 50 . 0 , P = 0 . 026 ) .

Example answer:
{"entities": [{"text": "size", "type": "SpatialConcept"}, {"text": "recanalization", "type": "HealthCareActivity"}]}

Example input:
Sentence: The revised response categories had a better distribution with lower average scores in three domains , compared with the original , and improved item information curves .

Example answer:
{"entities": [{"text": "response categories", "type": "BiologicFunction"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: Treatment recommendations correlated with the effect size ( correlation coefficient , 0 . 22 ; 95 % CI , 0 . 35 - 0 . 10 ; P < .001 ) , yet effect sizes were inversely correlated with study quality ( correlation coefficient , -0 . 06 ; 95 % CI , 0 . 01 to -0 . 12 ; P = .02 ) .

Example answer:
{"entities": [{"text": "Treatment recommendations", "type": "HealthCareActivity"}]}

Example input:
Sentence: In multivariate models , a negative association was found between patient age , psychological burden of family caregivers , and changes in total SoMe score , as well as for the superordinate dimensions .

Example answer:
{"entities": [{"text": "negative association", "type": "Finding"}, {"text": "SoMe", "type": "IntellectualProduct"}]}

Example input:
Sentence: Anxiety demonstrated comparable effect sizes across multiple models .

Example answer:
{"entities": [{"text": "Anxiety", "type": "Finding"}, {"text": "sizes", "type": "SpatialConcept"}, {"text": "multiple models", "type": "IntellectualProduct"}]}

Example input:
Sentence: However , the effect sizes were inversely correlated with meta - analyzed study quality , reducing confidence in these recommendations .

Example answer:
{"entities": [{"text": "meta - analyzed study", "type": "ResearchActivity"}, {"text": "confidence", "type": "BiologicFunction"}]}

Example input:
Sentence: Both qualitative and quantitative validation support key assumptions in the model structure and suggest the model is useful at predicting the populations of cats at geographical scales important for decision - making , although it also indicates where further research may improve model performance .

Example answer:
{"entities": [{"text": "validation", "type": "ResearchActivity"}, {"text": "model", "type": "IntellectualProduct"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "cats", "type": "Eukaryote"}, {"text": "geographical", "type": "SpatialConcept"}, {"text": "scales", "type": "IntellectualProduct"}, {"text": "decision - making", "type": "BiologicFunction"}, {"text": "research", "type": "ResearchActivity"}, {"text": "improve", "type": "Finding"}]}

Example input:
Sentence: If statistical heterogeneity was significant , random - effects models were used for meta - analysis , otherwise , fixed - effects models were applied .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "IntellectualProduct"}]}

Example input:
Sentence: We found that a model which included attentional load and task experience as predictors had the best model fit while adding performance as a predictor to this model reduced the overall model fit .

Example answer:
{"entities": [{"text": "model", "type": "IntellectualProduct"}, {"text": "attentional load", "type": "IntellectualProduct"}, {"text": "experience", "type": "BiologicFunction"}, {"text": "performance", "type": "HealthCareActivity"}]}

Example input:
Sentence: Our results indicate that the choice of variable is more critical than the choice of model .

Example answer:
{"entities": []}

Input:
Sentence: In addition to a ranking of variables from more to less useful , the effect of using models of varying taxonomic and size compositions is examined .

## Item MedMentions:test:3811
Example input:
Sentence: Within a larger global phylogenomic framework , Bayesian modelling suggested that this NZ clade emerged in the late 2000s , with a probable origin in swine from Western Europe .

Example answer:
{"entities": [{"text": "NZ", "type": "SpatialConcept"}, {"text": "clade", "type": "Bacterium"}, {"text": "swine", "type": "Eukaryote"}, {"text": "Western Europe", "type": "SpatialConcept"}]}

Example input:
Sentence: We propose that these evolutionary changes have enabled the emergence of human - specific behaviors , such as the sophisticated use of tools .

Example answer:
{"entities": [{"text": "evolutionary", "type": "BiologicFunction"}]}

Example input:
Sentence: In prehistoric environments , the motor behaviors of individuals with tic disorders may have been appropriate in environmental context , and had ecological relevance in survival and self - promotion .

Example answer:
{"entities": [{"text": "prehistoric environments", "type": "SpatialConcept"}, {"text": "motor behaviors", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "tic disorders", "type": "BiologicFunction"}, {"text": "ecological", "type": "SpatialConcept"}]}

Example input:
Sentence: Lessons learned from an unstable genomic landscape This brief historical perspective will highlight the many accomplishments of the late William ' Bill ' Morgan , and how his laboratory during the mid - 1990s shaped the field of genomic instability .

Example answer:
{"entities": [{"text": "genomic landscape", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "historical", "type": "Finding"}, {"text": "perspective", "type": "SpatialConcept"}, {"text": "William ' Bill ' Morgan", "type": "ProfessionalOrOccupationalGroup"}, {"text": "laboratory", "type": "Organization"}, {"text": "genomic instability", "type": "BiologicFunction"}]}

Example input:
Sentence: Our results showed that women living in villages consuming a mostly agricultural diet exhibited more caries and periodontal disease than those living in the bush consuming a mostly wild - food diet .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "villages", "type": "SpatialConcept"}, {"text": "consuming", "type": "BiologicFunction"}, {"text": "agricultural", "type": "Eukaryote"}, {"text": "diet", "type": "Food"}, {"text": "caries", "type": "BiologicFunction"}, {"text": "periodontal disease", "type": "BiologicFunction"}, {"text": "bush", "type": "Eukaryote"}, {"text": "wild - food diet", "type": "Food"}]}

Example input:
Sentence: On the post - glacial spread of human commensal Arabidopsis thaliana Recent work has shown that Arabidopsis thaliana contains genetic groups originating from different ice age refugia , with one particular group comprising over 95 % of the current worldwide population .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "Arabidopsis thaliana", "type": "Eukaryote"}]}

Example input:
Sentence: This was consistent with lack of biomagnification or accumulation in aquatic and terrestrial food chains .

Example answer:
{"entities": [{"text": "accumulation", "type": "Finding"}, {"text": "aquatic", "type": "SpatialConcept"}, {"text": "terrestrial", "type": "SpatialConcept"}]}

Example input:
Sentence: The world has been told for over two decades -by the media , researchers , politicians , and the biotech industry -that a genome -driven health care revolution is just around the corner . And while the revolution never seems to arrive , the hopeful rhetoric continues .

Example answer:
{"entities": [{"text": "world", "type": "PopulationGroup"}, {"text": "media", "type": "IntellectualProduct"}, {"text": "researchers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "biotech", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "health care", "type": "HealthCareActivity"}]}

Example input:
Sentence: In recent years , we witnessed a revolution regarding the nature , collection , and availability of data in general .

Example answer:
{"entities": []}

Example input:
Sentence: Apropos , a revolution in the area of human health is underway , which is occurring at the nexus between enteric microbiology and neuroscience .

Example answer:
{"entities": [{"text": "area", "type": "SpatialConcept"}, {"text": "human", "type": "Eukaryote"}, {"text": "enteric", "type": "SpatialConcept"}, {"text": "microbiology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "neuroscience", "type": "BiomedicalOccupationOrDiscipline"}]}

Input:
Sentence: This widely touted example of the mismatch between our biology and modern lifestyle has been intuited largely from the bioarchaeological record of the Neolithic Revolution in the New World .

## Item MedMentions:test:3749
Example input:
Sentence: Numbness was present in 13 , 18 , and 29 patients treated with MVD , RF , and SRS respectively ( p = 0 . 008 ) .

Example answer:
{"entities": [{"text": "Numbness", "type": "Finding"}, {"text": "MVD", "type": "HealthCareActivity"}, {"text": "RF", "type": "HealthCareActivity"}, {"text": "SRS", "type": "HealthCareActivity"}]}

Example input:
Sentence: In this study we propose an alternative to evaluate the effects of pirfenidone treatment on CPFES patients via acoustic information .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "pirfenidone", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "CPFES", "type": "BiologicFunction"}]}

Example input:
Sentence: Using the activatory Gq - coupled human M3 muscarinic receptor ( hM3Dq ) , we found that chemogenetic stimulation of dSPNs mimicked , while stimulation of iSPNs abolished the therapeutic action of L - DOPA in PD mice .

Example answer:
{"entities": [{"text": "activatory Gq - coupled human M3 muscarinic receptor", "type": "Chemical"}, {"text": "hM3Dq", "type": "Chemical"}, {"text": "chemogenetic stimulation", "type": "BiologicFunction"}, {"text": "dSPNs", "type": "AnatomicalStructure"}, {"text": "stimulation", "type": "BiologicFunction"}, {"text": "iSPNs", "type": "AnatomicalStructure"}, {"text": "therapeutic action", "type": "BiologicFunction"}, {"text": "L - DOPA", "type": "Chemical"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Secondly , we observed the effects of isradipine , a LTCC antagonist , on MPTP - induced DA neuron degeneration and iron accumulation in the SN .

Example answer:
{"entities": [{"text": "isradipine", "type": "Chemical"}, {"text": "LTCC", "type": "Chemical"}, {"text": "antagonist", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "induced", "type": "BiologicFunction"}, {"text": "DA neuron", "type": "AnatomicalStructure"}, {"text": "degeneration", "type": "BiologicFunction"}, {"text": "iron accumulation in the SN", "type": "Finding"}]}

Example input:
Sentence: We also found that isradipine prevented against MPTP - induced DA neuron depletion in the SN and partly restored the DA content in the striatum .

Example answer:
{"entities": [{"text": "isradipine", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "induced", "type": "BiologicFunction"}, {"text": "DA neuron", "type": "AnatomicalStructure"}, {"text": "SN", "type": "AnatomicalStructure"}, {"text": "restored", "type": "HealthCareActivity"}, {"text": "DA content", "type": "HealthCareActivity"}, {"text": "striatum", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Minocycline treatment ( daily 80 mg / kg per os ) of three - week duration started four weeks after induction of diabetes .

Example answer:
{"entities": [{"text": "Minocycline", "type": "Chemical"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Moreover , a recent study reported that minocycline has an acute antidepressive - like effect in diabetic animals .

Example answer:
{"entities": [{"text": "minocycline", "type": "Chemical"}, {"text": "acute antidepressive - like effect", "type": "Finding"}, {"text": "diabetic animals", "type": "Eukaryote"}]}

Example input:
Sentence: Minocycline treatment significantly attenuated mechanical allodynia and depression - like behaviour , while it failed to produce significant changes in mechanical hyperalgesia , cold allodynia or heat hypoalgesia .

Example answer:
{"entities": [{"text": "Minocycline", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "mechanical allodynia", "type": "Finding"}, {"text": "depression - like behaviour", "type": "BiologicFunction"}, {"text": "mechanical hyperalgesia", "type": "Finding"}, {"text": "cold allodynia", "type": "Finding"}, {"text": "heat hypoalgesia", "type": "Finding"}]}

Example input:
Sentence: Minocycline reduces mechanical allodynia and depressive - like behaviour in type - 1 diabetes mellitus in the rat A common and devastating complication of diabetes mellitus is painful diabetic neuropathy ( PDN ) that can be accompanied by emotional disorders such as depression .

Example answer:
{"entities": [{"text": "Minocycline", "type": "Chemical"}, {"text": "mechanical allodynia", "type": "Finding"}, {"text": "depressive - like behaviour", "type": "BiologicFunction"}, {"text": "type - 1 diabetes mellitus", "type": "BiologicFunction"}, {"text": "rat", "type": "Eukaryote"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "painful diabetic neuropathy", "type": "BiologicFunction"}, {"text": "PDN", "type": "BiologicFunction"}, {"text": "emotional disorders", "type": "BiologicFunction"}, {"text": "depression", "type": "BiologicFunction"}]}

Example input:
Sentence: Here we studied whether ( i ) prolonged minocycline treatment suppresses pain behaviour in PDN , ( ii ) the minocycline effect varies with submodality of pain , and ( iii ) the suppression of pain behaviour by prolonged minocycline treatment is associated with antidepressive - like effect .

Example answer:
{"entities": [{"text": "minocycline", "type": "Chemical"}, {"text": "PDN", "type": "BiologicFunction"}, {"text": "submodality of pain", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "antidepressive - like effect", "type": "Finding"}]}

Input:
Sentence: These results support the proposal that minocycline might provide a treatment option for attenuating sensory and comorbid emotional symptoms in chronic PDN .

## Item MedMentions:test:3854
Example input:
Sentence: Also , plasma lipid profiles , HbA1C , fasting plasma glucose , and insulin levels , will be measured and insulin resistance ( HOMA - IR ) and beta - cell function ( HOMA - B ) will be calculated at baseline and will be repeated at months 3 , 6 , 12 , and 18 .

Example answer:
{"entities": [{"text": "HbA1C", "type": "Chemical"}, {"text": "fasting plasma glucose", "type": "HealthCareActivity"}, {"text": "insulin", "type": "Chemical"}, {"text": "insulin resistance", "type": "HealthCareActivity"}, {"text": "HOMA - IR", "type": "HealthCareActivity"}, {"text": "beta - cell function", "type": "HealthCareActivity"}, {"text": "HOMA - B", "type": "HealthCareActivity"}]}

Example input:
Sentence: Specifically , in both groups , subjects with 1 - hour post - load glucose ≥155 mg / dl had higher fasting and 2 - h post - load glucose ( p < 0 .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}, {"text": "higher fasting", "type": "Finding"}, {"text": "2 - h post - load glucose", "type": "Finding"}]}

Example input:
Sentence: Serial fasting blood samples were obtained for lipid profile , and whole lengths of aorta were used to determine tissue markers of endothelial activation , inflammation and plaque stability .

Example answer:
{"entities": [{"text": "fasting", "type": "Finding"}, {"text": "blood samples", "type": "BodySubstance"}, {"text": "lipid profile", "type": "HealthCareActivity"}, {"text": "aorta", "type": "AnatomicalStructure"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "markers", "type": "ClinicalAttribute"}, {"text": "endothelial activation", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "plaque", "type": "Finding"}]}

Example input:
Sentence: The purpose of this study was to test for an association between fasting serum triglycerides and incident diabetes , changes in insulin resistance and changes in β - cell function in a Manitoba First Nation cohort .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "fasting", "type": "Finding"}, {"text": "serum", "type": "BodySubstance"}, {"text": "triglycerides", "type": "Chemical"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "β - cell function", "type": "BiologicFunction"}, {"text": "Manitoba", "type": "SpatialConcept"}, {"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: Fasting further attenuated its oral absorption and led to ∼70 % drops in average maximal plasma concentration ( Cmax ) and AUC .

Example answer:
{"entities": [{"text": "oral", "type": "SpatialConcept"}]}

Example input:
Sentence: The objective of this study was to assess the effects of CO versus EVOO intake on fasting lipoprotein and subfraction cholesterol levels , apolipoprotein ( apo ) A1 , apo B , and low - density lipoprotein particle concentrations in men and women .

Example answer:
{"entities": [{"text": "objective", "type": "IntellectualProduct"}, {"text": "CO", "type": "Chemical"}, {"text": "EVOO", "type": "Chemical"}, {"text": "fasting", "type": "Finding"}, {"text": "lipoprotein", "type": "HealthCareActivity"}, {"text": "cholesterol levels", "type": "HealthCareActivity"}, {"text": "apolipoprotein ( apo ) A1", "type": "HealthCareActivity"}, {"text": "apo B", "type": "HealthCareActivity"}, {"text": "low - density lipoprotein", "type": "HealthCareActivity"}]}

Example input:
Sentence: Fasting lipoprotein cholesterol and related variables were determined with density gradient ultracentrifugation .

Example answer:
{"entities": [{"text": "Fasting", "type": "Finding"}, {"text": "lipoprotein cholesterol", "type": "Chemical"}, {"text": "density gradient ultracentrifugation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Fasting triglycerides as a predictor of incident diabetes , insulin resistance and β - cell function in a Canadian First Nation Diabetes prevalence is substantially higher among Canadian First Nations populations than the non - First Nation population .

Example answer:
{"entities": [{"text": "Fasting", "type": "Finding"}, {"text": "triglycerides", "type": "Chemical"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "β - cell function", "type": "BiologicFunction"}, {"text": "Diabetes", "type": "BiologicFunction"}, {"text": "non - First Nation population", "type": "PopulationGroup"}]}

Example input:
Sentence: Eighty female volunteers were recruited , blood pressure and body measurements were recorded and a fasting blood sample was obtained for the quantitation of glucose , lipid profile , insulin , leptin and identification of ACE I / D polymorphs .

Example answer:
{"entities": [{"text": "female", "type": "PopulationGroup"}, {"text": "volunteers", "type": "PopulationGroup"}, {"text": "blood pressure", "type": "HealthCareActivity"}, {"text": "body measurements", "type": "HealthCareActivity"}, {"text": "fasting", "type": "Finding"}, {"text": "blood sample", "type": "BodySubstance"}, {"text": "glucose", "type": "Chemical"}, {"text": "lipid profile", "type": "HealthCareActivity"}, {"text": "insulin ,", "type": "Chemical"}, {"text": "leptin", "type": "Chemical"}, {"text": "ACE I / D polymorphs", "type": "Finding"}]}

Example input:
Sentence: From sixty antipsychotic naive patients with schizophrenia and sixty first - degree relatives matched for gender and age , fasting blood lipid profiles were measured at baseline and after twelve weeks .

Example answer:
{"entities": [{"text": "antipsychotic", "type": "Chemical"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "fasting blood lipid profiles", "type": "HealthCareActivity"}]}

Input:
Sentence: Fasting lipid profile changes of both groups were compared .

## Item MedMentions:test:3522
Example input:
Sentence: Chromatin immunoprecipitation ( ChIP ) showed that MS188 directly bound to the promoter of CYP703A2 and luciferase - inducible assay showed that MS188 activated the expression of CYP703A2 .

Example answer:
{"entities": [{"text": "Chromatin immunoprecipitation", "type": "HealthCareActivity"}, {"text": "ChIP", "type": "HealthCareActivity"}, {"text": "MS188", "type": "Chemical"}, {"text": "promoter", "type": "Chemical"}, {"text": "CYP703A2", "type": "AnatomicalStructure"}, {"text": "luciferase - inducible", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "CYP703A2", "type": "Chemical"}]}

Example input:
Sentence: Cellular senescence and sensitivity to IR is prevented by CRISPR / Cas9 -mediated deletion of the p21 gene ( CDKN1A ) in CHIP knockdown cells .

Example answer:
{"entities": [{"text": "Cellular senescence", "type": "BiologicFunction"}, {"text": "CRISPR", "type": "Chemical"}, {"text": "Cas9", "type": "Chemical"}, {"text": "deletion", "type": "BiologicFunction"}, {"text": "p21 gene", "type": "AnatomicalStructure"}, {"text": "CDKN1A", "type": "AnatomicalStructure"}, {"text": "CHIP", "type": "AnatomicalStructure"}, {"text": "knockdown", "type": "ResearchActivity"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: SNAI1 promotes the development of HCC through the enhancement of proliferation and inhibition of apoptosis SNAI1 , a zinc - finger transcription factor , plays an important role in the induction of epithelial - mesenchymal transition ( EMT ) in various cancers .

Example answer:
{"entities": [{"text": "SNAI1", "type": "Chemical"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "inhibition of apoptosis", "type": "BiologicFunction"}, {"text": "zinc - finger transcription factor", "type": "Chemical"}, {"text": "epithelial - mesenchymal transition", "type": "BiologicFunction"}, {"text": "EMT", "type": "BiologicFunction"}, {"text": "cancers", "type": "BiologicFunction"}]}

Example input:
Sentence: TFAP2C promotes lung tumorigenesis and aggressiveness through miR - 183 - and miR - 33a -mediated cell cycle regulation Non - small cell lung cancer ( NSCLC ) remains one of the leading causes of death worldwide , and thus new molecular targets need to be identified to improve treatment efficacy .

Example answer:
{"entities": [{"text": "TFAP2C", "type": "Chemical"}, {"text": "lung", "type": "AnatomicalStructure"}, {"text": "tumorigenesis", "type": "BiologicFunction"}, {"text": "miR - 183", "type": "Chemical"}, {"text": "miR - 33a", "type": "Chemical"}, {"text": "cell cycle regulation", "type": "BiologicFunction"}, {"text": "Non - small cell lung cancer", "type": "BiologicFunction"}, {"text": "NSCLC", "type": "BiologicFunction"}, {"text": "death", "type": "BiologicFunction"}, {"text": "worldwide", "type": "PopulationGroup"}, {"text": "molecular targets", "type": "Chemical"}]}

Example input:
Sentence: The downregulation of uncoupling protein 2 ( UCP2 ) , which is attributed to hypoxia - inducible factor 1 ( HIF - 1 ) - mediated suppression of the transcriptional factor peroxisome proliferator - activated receptor γ ( PPARγ ) , was involved in NSCLC chemoresistance , and predicted a poor survival rate of patients receiving routine chemotherapy .

Example answer:
{"entities": [{"text": "downregulation", "type": "BiologicFunction"}, {"text": "uncoupling protein 2", "type": "Chemical"}, {"text": "UCP2", "type": "Chemical"}, {"text": "hypoxia - inducible factor 1", "type": "Chemical"}, {"text": "HIF - 1", "type": "Chemical"}, {"text": "suppression", "type": "BiologicFunction"}, {"text": "transcriptional factor", "type": "Chemical"}, {"text": "peroxisome proliferator - activated receptor γ", "type": "Chemical"}, {"text": "PPARγ", "type": "Chemical"}, {"text": "NSCLC", "type": "BiologicFunction"}, {"text": "chemoresistance", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Uncoupling protein 2 downregulation by hypoxia through repression of peroxisome proliferator - activated receptor γ promotes chemoresistance of non - small cell lung cancer Hypoxic microenvironment is critically involved in the response of non - small cell lung cancer ( NSCLC ) to chemotherapy , the mechanisms of which remain largely unknown .

Example answer:
{"entities": [{"text": "Uncoupling protein 2", "type": "Chemical"}, {"text": "downregulation", "type": "BiologicFunction"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "repression", "type": "BiologicFunction"}, {"text": "peroxisome proliferator - activated receptor γ", "type": "Chemical"}, {"text": "chemoresistance", "type": "BiologicFunction"}, {"text": "non - small cell lung cancer", "type": "BiologicFunction"}, {"text": "Hypoxic", "type": "BiologicFunction"}, {"text": "microenvironment", "type": "SpatialConcept"}, {"text": "NSCLC", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Mechanistically , ubiquitin - dependent degradation of the cyclin - dependent kinase ( CDK ) inhibitor , p21 protein , is reduced by CHIP knockdown , leading to enhanced senescence of cells in response to exposure to IR .

Example answer:
{"entities": [{"text": "ubiquitin - dependent degradation", "type": "BiologicFunction"}, {"text": "cyclin - dependent kinase ( CDK ) inhibitor , p21 protein", "type": "Chemical"}, {"text": "CHIP", "type": "AnatomicalStructure"}, {"text": "knockdown", "type": "ResearchActivity"}, {"text": "senescence of cells", "type": "BiologicFunction"}, {"text": "exposure to IR", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: In vitro and cell -based assays demonstrate that p21 is a novel and direct ubiquitylation substrate of CHIP that also requires the CHIP - associated chaperone HSP70 .

Example answer:
{"entities": [{"text": "cell", "type": "AnatomicalStructure"}, {"text": "assays", "type": "HealthCareActivity"}, {"text": "p21", "type": "Chemical"}, {"text": "ubiquitylation", "type": "BiologicFunction"}, {"text": "CHIP", "type": "Chemical"}, {"text": "chaperone", "type": "Chemical"}, {"text": "HSP70", "type": "Chemical"}]}

Example input:
Sentence: Here , we show that human lung cancer cell lines can be rendered sensitive to ionizing radiation ( IR ) by RNAi knockdown of C - terminus of Hsc70 - interacting protein ( CHIP / STUB1 ) , a U - box - type E3 ubiquitin ligase that targets a number of stress - induced proteins .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "RNAi", "type": "BiologicFunction"}, {"text": "knockdown", "type": "ResearchActivity"}, {"text": "C - terminus of Hsc70 - interacting protein", "type": "Chemical"}, {"text": "CHIP", "type": "Chemical"}, {"text": "STUB1", "type": "Chemical"}, {"text": "U - box - type E3 ubiquitin ligase", "type": "Chemical"}, {"text": "stress - induced proteins", "type": "Chemical"}]}

Example input:
Sentence: These data reveal that the inhibition of the E3 ubiquitin ligase CHIP promotes radiosensitivity , thus suggesting a novel strategy for the treatment of lung cancer .

Example answer:
{"entities": [{"text": "E3 ubiquitin ligase CHIP", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "lung cancer", "type": "BiologicFunction"}]}

Input:
Sentence: Implications : The CHIP - HSP70 - p21 ubiquitylation / degradation axis identified here could be exploited to enhance the efficacy of radiotherapy in patients with non - small cell lung cancer .

## Item MedMentions:test:3660
Example input:
Sentence: To explore the mechanisms involved , the expression of glial glutamate transporter 1 ( GLT - 1 ) and the activation of mitogen - activated protein kinases in the spinal dorsal horn were analyzed .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "glial", "type": "AnatomicalStructure"}, {"text": "glutamate transporter 1", "type": "Chemical"}, {"text": "GLT - 1", "type": "Chemical"}, {"text": "mitogen - activated protein kinases", "type": "Chemical"}, {"text": "spinal dorsal horn", "type": "AnatomicalStructure"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: Using melanopsin to study G protein signaling in cortical neurons Our understanding of G protein - coupled receptors ( GPCRs ) in the central nervous system ( CNS ) has been hampered by the limited availability of tools allowing for the study of their signaling with precise temporal control .

Example answer:
{"entities": [{"text": "melanopsin", "type": "Chemical"}, {"text": "study", "type": "ResearchActivity"}, {"text": "G protein signaling", "type": "BiologicFunction"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "understanding", "type": "BiologicFunction"}, {"text": "G protein - coupled receptors", "type": "Chemical"}, {"text": "GPCRs", "type": "Chemical"}, {"text": "central nervous system", "type": "BodySystem"}, {"text": "CNS", "type": "BodySystem"}, {"text": "signaling", "type": "BiologicFunction"}]}

Example input:
Sentence: Moreover , we revealed that several novel pathways , including PluriNetWork and Focal Adhesion , were responsible for the delayed progression of female EpiStem cells .

Example answer:
{"entities": [{"text": "Focal Adhesion", "type": "AnatomicalStructure"}, {"text": "responsible for", "type": "Finding"}, {"text": "EpiStem cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We investigated whether guidance signalling through Slit and Netrin pathways plays a role in cell migration during heart development .

Example answer:
{"entities": [{"text": "guidance signalling", "type": "BiologicFunction"}, {"text": "Slit", "type": "Chemical"}, {"text": "Netrin pathways", "type": "BiologicFunction"}, {"text": "cell migration", "type": "BiologicFunction"}, {"text": "heart development", "type": "BiologicFunction"}]}

Example input:
Sentence: Among these targets , calcium signaling mechanisms are critically dependent on the developmental stage and their full expression is a hallmark of the mature , functional neuron .

Example answer:
{"entities": [{"text": "calcium signaling", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "neuron", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Besides , GAS activated MAPK and PI3 K signaling pathways which are often involved in growth of nerve cells were also reported .

Example answer:
{"entities": [{"text": "GAS", "type": "Chemical"}, {"text": "MAPK", "type": "Chemical"}, {"text": "PI3 K", "type": "Chemical"}, {"text": "signaling pathways", "type": "BiologicFunction"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "nerve cells", "type": "AnatomicalStructure"}, {"text": "reported", "type": "HealthCareActivity"}]}

Example input:
Sentence: We identified multiple signaling pathways that trigger distinct downstream transcriptional networks to regulate the diversity of neural cells originating from the SVZ .

Example answer:
{"entities": [{"text": "signaling pathways", "type": "BiologicFunction"}, {"text": "downstream transcriptional networks", "type": "BiologicFunction"}, {"text": "neural cells", "type": "AnatomicalStructure"}, {"text": "SVZ", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Here , using the cell - type selectivity of genetic methods , circuit mapping , and behavior assays , we sought to decipher neural circuits emanating from the septal nucleus to the lateral hypothalamus ( LH ) that contribute to neural regulation of food intake in mice .

Example answer:
{"entities": [{"text": "cell - type", "type": "IntellectualProduct"}, {"text": "genetic methods", "type": "ResearchActivity"}, {"text": "circuit mapping", "type": "HealthCareActivity"}, {"text": "assays", "type": "HealthCareActivity"}, {"text": "septal nucleus", "type": "AnatomicalStructure"}, {"text": "lateral hypothalamus", "type": "SpatialConcept"}, {"text": "LH", "type": "SpatialConcept"}, {"text": "food intake", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Although connections between cilia and PCP signaling in vertebrate development have been reported , their precise nature is not well understood .

Example answer:
{"entities": [{"text": "cilia", "type": "AnatomicalStructure"}, {"text": "PCP", "type": "SpatialConcept"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "vertebrate", "type": "Eukaryote"}, {"text": "development", "type": "BiologicFunction"}]}

Example input:
Sentence: Although animal neurophysiology has largely concentrated on effector - selective decision signals that translate the emerging decision into a specific motor plan , recent research on the human brain has isolated abstract neural signatures of decision formation that are independent of specific sensory and motor requirements .

Example answer:
{"entities": [{"text": "animal", "type": "Eukaryote"}, {"text": "neurophysiology", "type": "BiologicFunction"}, {"text": "decision", "type": "BiologicFunction"}, {"text": "research", "type": "ResearchActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "abstract", "type": "BiologicFunction"}, {"text": "signatures", "type": "ClinicalAttribute"}, {"text": "decision formation", "type": "BiologicFunction"}]}

Input:
Sentence: Thus , bidirectional neuron - glial interactions are crucial in development , but little is known about the cellular sensors and signalling pathways involved .

## Item MedMentions:test:3865
Example input:
Sentence: There were 14 deaths and they occurred significantly in younger age among positive cases as compared to negatives ( Mean ± SD : 34 ± 2 . 8 vs 47 ± 8 . 4 years ) .

Example answer:
{"entities": [{"text": "deaths", "type": "BiologicFunction"}, {"text": "positive cases", "type": "Finding"}, {"text": "negatives", "type": "Finding"}]}

Example input:
Sentence: Joint model imputation to estimate the treatment effect on long - term survival using auxiliary events Clinical trial duration may be a concern in clinical research , especially in cancer trials where the endpoint is overall survival .

Example answer:
{"entities": [{"text": "treatment effect", "type": "Finding"}, {"text": "Clinical trial", "type": "ResearchActivity"}, {"text": "clinical research", "type": "ResearchActivity"}, {"text": "cancer trials", "type": "ResearchActivity"}, {"text": "endpoint", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Greater time before death predicted an increased likelihood of higher ratings for health plan and specialist physician .

Example answer:
{"entities": [{"text": "death", "type": "BiologicFunction"}, {"text": "specialist physician", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: While death -censored allograft survival was comparable between KTRs after SOT and primary KTRs , KTRs after SOT showed superior 5 - year death -censored allograft survival of 92 .

Example answer:
{"entities": [{"text": "death", "type": "BiologicFunction"}, {"text": "allograft", "type": "HealthCareActivity"}, {"text": "KTRs", "type": "Finding"}, {"text": "SOT", "type": "HealthCareActivity"}]}

Example input:
Sentence: The Schedule of Attitudes toward Hastened Death is the most widely used and is the instrument whose psychometric properties have been most often analysed .

Example answer:
{"entities": [{"text": "Schedule", "type": "IntellectualProduct"}, {"text": "Attitudes", "type": "BiologicFunction"}, {"text": "Hastened Death", "type": "HealthCareActivity"}, {"text": "psychometric", "type": "HealthCareActivity"}]}

Example input:
Sentence: At 22 h , the animal was rapidly decompressed and observed for DCS type , onset time , and mortality .

Example answer:
{"entities": [{"text": "animal", "type": "Eukaryote"}, {"text": "DCS", "type": "BiologicFunction"}]}

Example input:
Sentence: Under the relevant limb of the Uniform Determination of Death Act 1981 ( USA ) , a person is dead when the cessation of circulatory - respiratory function is ' irreversible ' .

Example answer:
{"entities": [{"text": "Uniform Determination of Death Act 1981 ( USA )", "type": "IntellectualProduct"}, {"text": "person", "type": "PopulationGroup"}, {"text": "dead", "type": "BiologicFunction"}, {"text": "irreversible", "type": "Finding"}]}

Example input:
Sentence: Two imputation methods were compared : sampling from the estimated parametric distribution of the survival time and sampling using its nonparametric estimation .

Example answer:
{"entities": [{"text": "sampling", "type": "ResearchActivity"}, {"text": "survival time", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Each increment of 1 hour / day in sitting time was linked to a 7 % increase in mortality .

Example answer:
{"entities": [{"text": "sitting", "type": "BiologicFunction"}]}

Example input:
Sentence: Exclusion of deaths within the first 24 months of follow - up did not alter these results .

Example answer:
{"entities": [{"text": "deaths", "type": "Finding"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "not alter", "type": "Finding"}, {"text": "results", "type": "Finding"}]}

Input:
Sentence: At an early time point , the high number of censored observations can be compensated by the imputation of the unobserved deaths times .

## Item MedMentions:test:3936
Example input:
Sentence: The growth of S .

Example answer:
{"entities": [{"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: This indicates that S .

Example answer:
{"entities": [{"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: S . automotive manufacturer .

Example answer:
{"entities": [{"text": "S", "type": "SpatialConcept"}]}

Example input:
Sentence: S . and SBM from China .

Example answer:
{"entities": [{"text": "S", "type": "SpatialConcept"}, {"text": "SBM", "type": "Food"}, {"text": "China", "type": "SpatialConcept"}]}

Example input:
Sentence: acnes and S .

Example answer:
{"entities": [{"text": "acnes", "type": "Bacterium"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: acnes and S .

Example answer:
{"entities": [{"text": "acnes", "type": "Bacterium"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: While in S .

Example answer:
{"entities": [{"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: S . and a U .

Example answer:
{"entities": [{"text": "S .", "type": "SpatialConcept"}, {"text": "U .", "type": "SpatialConcept"}]}

Example input:
Sentence: s . ) .

Example answer:
{"entities": []}

Example input:
Sentence: The S .

Example answer:
{"entities": [{"text": "S .", "type": "Eukaryote"}]}

Input:
Sentence: S .

## Item MedMentions:test:3827
Example input:
Sentence: Specifically , radiographic measurements of grafted bone height at the mesial and distal side of each implant were taken , and the sinus floor configuration was classified into concave , angle , and flat according to the sinus floor profile at the implant site .

Example answer:
{"entities": [{"text": "radiographic", "type": "HealthCareActivity"}, {"text": "mesial", "type": "SpatialConcept"}, {"text": "distal", "type": "SpatialConcept"}, {"text": "implant", "type": "MedicalDevice"}, {"text": "sinus", "type": "SpatialConcept"}, {"text": "angle", "type": "SpatialConcept"}, {"text": "flat", "type": "SpatialConcept"}, {"text": "site", "type": "SpatialConcept"}]}

Example input:
Sentence: Correlations with anatomic aspects provided evidence of a rostrocaudal gradient with increasing gray / white - matter ratio and decreasing hematoma -volume and rate of hematoma enlargement from frontal to occipital ICH location .

Example answer:
{"entities": [{"text": "rostrocaudal", "type": "SpatialConcept"}, {"text": "gray", "type": "AnatomicalStructure"}, {"text": "white - matter", "type": "AnatomicalStructure"}, {"text": "hematoma", "type": "BiologicFunction"}, {"text": "enlargement", "type": "AnatomicalStructure"}, {"text": "frontal", "type": "AnatomicalStructure"}, {"text": "occipital", "type": "AnatomicalStructure"}, {"text": "ICH", "type": "Finding"}, {"text": "location", "type": "SpatialConcept"}]}

Example input:
Sentence: Using a three - dimensional motion analyzer , the difference in volume within the upper and lower hemithoraces was measured .

Example answer:
{"entities": [{"text": "three - dimensional motion analyzer", "type": "MedicalDevice"}, {"text": "upper", "type": "SpatialConcept"}, {"text": "lower", "type": "SpatialConcept"}, {"text": "hemithoraces", "type": "SpatialConcept"}]}

Example input:
Sentence: A unilateral decrease in the vertical height of the dentition and the subsequent steeper occlusal plane inclinations correlated with ( 1 ) mandibular rotational displacement and condylar lateral displacement , ( 2 ) mandibular and condylar morphologic changes ( 3 ) changes in temporal bone position .

Example answer:
{"entities": [{"text": "unilateral", "type": "SpatialConcept"}, {"text": "decrease in the vertical height", "type": "Finding"}, {"text": "dentition", "type": "AnatomicalStructure"}, {"text": "occlusal plane inclinations", "type": "Finding"}, {"text": "mandibular rotational displacement", "type": "AnatomicalStructure"}, {"text": "condylar", "type": "AnatomicalStructure"}, {"text": "mandibular", "type": "AnatomicalStructure"}, {"text": "temporal bone", "type": "AnatomicalStructure"}, {"text": "position", "type": "SpatialConcept"}]}

Example input:
Sentence: Three - dimensional printing technology in craniomaxillofacial surgery can be classified into contour models ( type I ) , guides ( type II ) , splints ( type III ) , and implants ( type IV ) .

Example answer:
{"entities": [{"text": "technology", "type": "HealthCareActivity"}, {"text": "craniomaxillofacial surgery", "type": "HealthCareActivity"}, {"text": "classified", "type": "IntellectualProduct"}, {"text": "guides", "type": "MedicalDevice"}, {"text": "splints", "type": "MedicalDevice"}, {"text": "implants", "type": "MedicalDevice"}]}

Example input:
Sentence: Axial ( through - plane ) , sagittal ( in - plane ) PC - MRI and sagittal 3D - CISS were applied to assess the cerebral aqueduct and the spontaneous third ventriculostomy if present .

Example answer:
{"entities": [{"text": "Axial", "type": "SpatialConcept"}, {"text": "sagittal", "type": "SpatialConcept"}, {"text": "PC - MRI", "type": "HealthCareActivity"}, {"text": "cerebral aqueduct", "type": "SpatialConcept"}]}

Example input:
Sentence: Lateral cephalometric radiographs were used to evaluate the extent of distal movement .

Example answer:
{"entities": [{"text": "extent", "type": "SpatialConcept"}, {"text": "distal", "type": "SpatialConcept"}, {"text": "movement", "type": "HealthCareActivity"}]}

Example input:
Sentence: Three - dimensional motion analysis was conducted using an optoelectronic system .

Example answer:
{"entities": [{"text": "Three - dimensional motion analysis", "type": "HealthCareActivity"}, {"text": "optoelectronic system", "type": "MedicalDevice"}]}

Example input:
Sentence: Three - dimensional facial computed tomography and cephalolateral radiography were performed preoperatively and postoperatively .

Example answer:
{"entities": [{"text": "Three - dimensional", "type": "SpatialConcept"}, {"text": "facial computed tomography", "type": "HealthCareActivity"}, {"text": "cephalolateral radiography", "type": "HealthCareActivity"}]}

Example input:
Sentence: Three - dimensional morphological characterization of malocclusions with mandibular lateral displacement using cone - beam computed tomography The purpose of this study was to evaluate the morphologic characteristics of MLD malocclusions using 3D imaging .

Example answer:
{"entities": [{"text": "Three - dimensional", "type": "SpatialConcept"}, {"text": "morphological", "type": "SpatialConcept"}, {"text": "malocclusions", "type": "BiologicFunction"}, {"text": "mandibular lateral displacement", "type": "AnatomicalStructure"}, {"text": "cone - beam computed tomography", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "MLD", "type": "AnatomicalStructure"}, {"text": "3D imaging", "type": "HealthCareActivity"}]}

Input:
Sentence: A 3D Cephalometric analysis was developed to describe the spatial position of the mandible and temporal bones .

## Item MedMentions:test:4030
Example input:
Sentence: 34 + 11 .

Example answer:
{"entities": []}

Example input:
Sentence: 34 ( t18 = 1 . 50 , p = 0 . 15 , d = 0 . 34 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 5 vs 34 .

Example answer:
{"entities": []}

Example input:
Sentence: 34 ; 1 . 15 - 1 . 57 and 1 .

Example answer:
{"entities": []}

Example input:
Sentence: 34 - 3 . 93 ; p = 0 . 002 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 34 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 33±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 34 , P < 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 33 to 1 .

Example answer:
{"entities": []}

Example input:
Sentence: 28 and 34 .

Example answer:
{"entities": []}

Input:
Sentence: 34 to -33 .

## Item MedMentions:test:3872
Example input:
Sentence: Patients ( N = 327 ) who had completed each of the 4 annual postoperative follow - ups were included in this study .

Example answer:
{"entities": [{"text": "postoperative follow - ups", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: With a median follow - up of 6 . 2 years , 343 recurrence , 365 CSM , and 451 OM were recorded , respectively .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: RESULTS : A total of 306 consecutive eligible patients were included .

Example answer:
{"entities": []}

Example input:
Sentence: Over a 2 - year period , 141 patients were followed .

Example answer:
{"entities": []}

Example input:
Sentence: From 191 total pregnancies occurring before AVM obliteration , there were 175 ( 91 . 6 % ) term deliveries and 16 ( 8 . 4 % ) abortions .

Example answer:
{"entities": [{"text": "pregnancies", "type": "BiologicFunction"}, {"text": "AVM", "type": "AnatomicalStructure"}, {"text": "term deliveries", "type": "BiologicFunction"}, {"text": "abortions", "type": "Finding"}]}

Example input:
Sentence: After median 1 . 7 years follow - up , 270 patients died .

Example answer:
{"entities": [{"text": "median", "type": "SpatialConcept"}, {"text": "died", "type": "Finding"}]}

Example input:
Sentence: After a mean follow - up of 4 . 2 years , 1 , 073 death s and 6 , 306 hospitalizations had occurred .

Example answer:
{"entities": [{"text": "death", "type": "BiologicFunction"}, {"text": "hospitalizations", "type": "HealthCareActivity"}]}

Example input:
Sentence: In total , four women ( 9 . 3 % ) delivered the second pregnancy < 37 weeks : three had a prior term VD and one had a prior 34 weeks VD .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "delivered", "type": "Finding"}, {"text": "pregnancy", "type": "BiologicFunction"}, {"text": "term", "type": "BiologicFunction"}, {"text": "VD", "type": "HealthCareActivity"}]}

Example input:
Sentence: Among 113 women with an unfulfilled PPTL request , there were 17 subsequent pregnancies ( 15 . 0 % ) during the 27 months of follow - up .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "PPTL", "type": "HealthCareActivity"}, {"text": "pregnancies", "type": "BiologicFunction"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: In total , 519 patients completed 1 year of follow - up , among which 69 ( 13 .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Input:
Sentence: During follow - up , 104 had 116 pregnancies , of which 110 continued beyond week 20 ; 309 patients did not become pregnant .

## Item MedMentions:test:3408
Example input:
Sentence: Although the role of β - adrenergic stimulation on viral myocarditis has been investigated in our pervious studies , the direct effect of vagal tone in this setting has not been yet studied .

Example answer:
{"entities": [{"text": "β - adrenergic stimulation", "type": "Finding"}, {"text": "viral myocarditis", "type": "BiologicFunction"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "studied", "type": "ResearchActivity"}]}

Example input:
Sentence: Sarcoid -mediated myocardial inflammation is associated with a regional impairment of coronary circulatory function .

Example answer:
{"entities": [{"text": "Sarcoid", "type": "BiologicFunction"}, {"text": "myocardial inflammation", "type": "BiologicFunction"}, {"text": "coronary circulatory", "type": "BiologicFunction"}]}

Example input:
Sentence: Nicotine Suppressed Fetal Adrenal StAR Expression via YY1 Mediated - Histone Deacetylation Modification Mechanism Steroidogenic acute regulatory ( StAR ) protein plays a pivotal role in steroidogenesis .

Example answer:
{"entities": [{"text": "Nicotine", "type": "Chemical"}, {"text": "Fetal Adrenal", "type": "AnatomicalStructure"}, {"text": "StAR", "type": "Chemical"}, {"text": "Expression", "type": "BiologicFunction"}, {"text": "YY1", "type": "Chemical"}, {"text": "Histone Deacetylation", "type": "BiologicFunction"}, {"text": "Steroidogenic acute regulatory ( StAR ) protein", "type": "Chemical"}, {"text": "steroidogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , in nicotine - treated NCI - H295A cells , nicotine enhanced YY1 expression and inhibited StAR expression .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "NCI - H295A cells", "type": "AnatomicalStructure"}, {"text": "YY1", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "StAR", "type": "Chemical"}]}

Example input:
Sentence: The findings suggest that vagus nerve stimulation mediated inhibition of the inflammatory processes likely provide important benefits in myocarditis treatment .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "vagus nerve", "type": "AnatomicalStructure"}, {"text": "stimulation", "type": "HealthCareActivity"}, {"text": "myocarditis", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The vagus nerve can modulate the immune response and control inflammation through a ' cholinergic anti - inflammatory pathway ' dependent on the α7 - nicotinic acetylcholine receptor ( α7nAChR ) .

Example answer:
{"entities": [{"text": "vagus nerve", "type": "AnatomicalStructure"}, {"text": "modulate", "type": "SpatialConcept"}, {"text": "immune response", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "anti - inflammatory", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "α7 - nicotinic acetylcholine receptor", "type": "Chemical"}, {"text": "α7nAChR", "type": "Chemical"}]}

Example input:
Sentence: Therefore , in the present study , we investigated the effect s of cervical vagotomy in a murine model of viral myocarditis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "cervical", "type": "SpatialConcept"}, {"text": "vagotomy", "type": "HealthCareActivity"}, {"text": "murine", "type": "Eukaryote"}, {"text": "model", "type": "BiologicFunction"}, {"text": "viral myocarditis", "type": "BiologicFunction"}]}

Example input:
Sentence: Right Cervical Vagotomy Aggravates Viral Myocarditis in Mice Via the Cholinergic Anti - inflammatory Pathway The autonomic nervous system dysfunction with increased sympathetic activity and withdrawal of vagal activity may play an important role in the pathogenesis of viral myocarditis .

Example answer:
{"entities": [{"text": "Vagotomy", "type": "HealthCareActivity"}, {"text": "Aggravates", "type": "Finding"}, {"text": "Viral Myocarditis", "type": "BiologicFunction"}, {"text": "Mice", "type": "Eukaryote"}, {"text": "Anti - inflammatory", "type": "Chemical"}, {"text": "Pathway", "type": "BiologicFunction"}, {"text": "autonomic nervous system dysfunction", "type": "Finding"}, {"text": "increased sympathetic activity", "type": "BiologicFunction"}, {"text": "vagal", "type": "AnatomicalStructure"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "viral myocarditis", "type": "BiologicFunction"}]}

Example input:
Sentence: These results indicate that vagal nerve plays an important role in mediating the anti - inflammatory effect in viral myocarditis , and that cholinergic stimulation with nicotine also plays its peripheral anti - inflammatory role relying on α7nAChR , without requirement for the integrity of vagal nerve in the model .

Example answer:
{"entities": [{"text": "vagal nerve", "type": "AnatomicalStructure"}, {"text": "anti - inflammatory", "type": "Chemical"}, {"text": "viral myocarditis", "type": "BiologicFunction"}, {"text": "stimulation", "type": "HealthCareActivity"}, {"text": "nicotine", "type": "Chemical"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "α7nAChR", "type": "Chemical"}, {"text": "model", "type": "BiologicFunction"}]}

Example input:
Sentence: In a coxsackievirus B3 murine myocarditis model ( Balb / c ) , effects of right cervical vagotomy and nAChR agonist nicotine on echocardiography , myocardial histopathology , viral RNA , and proinflammatory cytokine levels were studied .

Example answer:
{"entities": [{"text": "murine", "type": "Eukaryote"}, {"text": "myocarditis", "type": "BiologicFunction"}, {"text": "model", "type": "BiologicFunction"}, {"text": "Balb / c", "type": "Eukaryote"}, {"text": "vagotomy", "type": "HealthCareActivity"}, {"text": "nAChR agonist nicotine", "type": "Chemical"}, {"text": "echocardiography", "type": "HealthCareActivity"}, {"text": "myocardial", "type": "SpatialConcept"}, {"text": "histopathology", "type": "ResearchActivity"}, {"text": "viral RNA", "type": "Chemical"}, {"text": "cytokine", "type": "Chemical"}, {"text": "studied", "type": "ResearchActivity"}]}

Input:
Sentence: We found that right cervical vagotomy inhibited the cholinergic anti - inflammatory pathway , aggravated myocardial lesions , up - regulated the expression of TNF - α , IL - 1β , and IL - 6 , and worsened the impaired left ventricular function in murine viral myocarditis , and these changes were reversed by co - treatment with nicotine by activating the cholinergic anti - inflammatory pathway .
