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

## Item MedMentions:test:2370
Example input:
Sentence: Other outcomes were similar between the LTHome and EUT arms : alternate composite outcome achievement ( last five FPG mean within the range of 5 - 7 . 2 mmol / L + no hypoglycemia , 47 % and 51 % , P = 0 . 73 ) ; A1c reduction ( -1 . 0 % and -1 . 1 % , P = 0 . 66 ) ; proportion achieving A1c ≤7 % ( 14 % and 20 % , P = 0 .

Example answer:
{"entities": [{"text": "LTHome", "type": "IntellectualProduct"}, {"text": "EUT", "type": "HealthCareActivity"}, {"text": "FPG", "type": "Finding"}, {"text": "no", "type": "Finding"}, {"text": "hypoglycemia", "type": "BiologicFunction"}, {"text": "A1c", "type": "Chemical"}]}

Example input:
Sentence: 06 for PBTTC , 0 . 44±0 .

Example answer:
{"entities": [{"text": "PBTTC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Patient satisfaction score improvements were greater in LTHome versus EUT ( change in fear of hypoglycemia score P = 0 . 04 and change in diabetes distress score P = 0 .

Example answer:
{"entities": [{"text": "LTHome", "type": "IntellectualProduct"}, {"text": "EUT", "type": "HealthCareActivity"}, {"text": "fear", "type": "BiologicFunction"}, {"text": "hypoglycemia", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "distress", "type": "Finding"}]}

Example input:
Sentence: The ICC and r were highest ( ≥0 . 80 ) for 25 ( OH ) D , free 25 ( OH ) D , bioavailable 25 ( OH ) D and PTH , but somewhat lower ( approximately 0 . 60 - 0 . 75 ) for the other biomarkers .

Example answer:
{"entities": [{"text": "25 ( OH ) D", "type": "Chemical"}, {"text": "PTH", "type": "Chemical"}, {"text": "biomarkers", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Heavier ewes had higher UPLTC

Example answer:
{"entities": [{"text": "UPLTC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In men , after adjustments for BMI , SBP , DBP , fasting glucose , total cholesterol , triglycerides , low density lipoprotein cholesterol and creatinine , the men with the TT genotype of rs2941484 were found to have significantly higher probability of suffering from hyperuricemia than the ones with CT and CC genotypes ( OR = 2 . 170 , P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "SBP", "type": "ClinicalAttribute"}, {"text": "DBP", "type": "ClinicalAttribute"}, {"text": "fasting glucose", "type": "Finding"}, {"text": "total cholesterol", "type": "Chemical"}, {"text": "triglycerides", "type": "Chemical"}, {"text": "low density lipoprotein cholesterol", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "rs2941484", "type": "AnatomicalStructure"}, {"text": "suffering", "type": "Finding"}, {"text": "hyperuricemia", "type": "BiologicFunction"}]}

Example input:
Sentence: Udder health score s and tick counts at all sites were not related to reproduction traits .

Example answer:
{"entities": [{"text": "Udder", "type": "AnatomicalStructure"}, {"text": "reproduction", "type": "BiologicFunction"}]}

Example input:
Sentence: From January 2003 to December 2012 , TACE was conducted on 81 patients with Child - Pugh score ≤7 who had HCC with sPVTT .

Example answer:
{"entities": [{"text": "TACE", "type": "HealthCareActivity"}, {"text": "Child - Pugh score", "type": "IntellectualProduct"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "sPVTT", "type": "BiologicFunction"}]}

Example input:
Sentence: 03 for udder health score .

Example answer:
{"entities": [{"text": "udder", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 53±0 . 04 for UPLTC , 0 .

Example answer:
{"entities": [{"text": "UPLTC", "type": "AnatomicalStructure"}]}

Input:
Sentence: ( 0 . 47±0 . 10 ) , UPLTC and udder health score ( 0 . 52±0 . 07 ) , HTLTC and UPLTC ( 0 . 24±0 . 11 ) as well as UPLTC and PBTTC

## Item MedMentions:test:2337
Example input:
Sentence: Multivariate analysis using age , gender , and comorbidities as covariates did not reveal any significant differences in survival .

Example answer:
{"entities": []}

Example input:
Sentence: On MVA , older age ( hazard ratio [ HR ] , 1 . 317 ; 95 % confidence interval [ CI ] , 1 . 137 - 1 . 526 ) , € ‰ ‰   € ‰1 comorbidity ( HR , 1 . 587 ; 95 % CI , 1 . 379 - 1 . 827 ) , distant metastasis ( HR , 1 . 385 ; 95 % CI , 1 . 216 - 1 . 578 ) , receipt of systemic therapy ( HR , 0 . 637 ; 95 % CI , 0 . 547 - 0 . 742 ) , and receipt of RT compared with no RT ( < 45 grays [ Gy ] : HR , 0 . 843 ; 95 % CI , 0 . 718 - 0 .

Example answer:
{"entities": [{"text": "older age", "type": "PopulationGroup"}, {"text": "distant metastasis", "type": "ClinicalAttribute"}, {"text": "systemic therapy", "type": "HealthCareActivity"}, {"text": "RT", "type": "IntellectualProduct"}]}

Example input:
Sentence: Overall survival and disease - free survival at 60 months are 48 . 8 % and 45 . 8 % , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: In this paper , we introduce a publicly available multi - spectral template with corresponding tissue probability atlases and regional atlases , optimised to use in studies of ageing cohorts ( mean age 75 ± 5 years ) .

Example answer:
{"entities": [{"text": "publicly", "type": "Organization"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "atlases", "type": "IntellectualProduct"}, {"text": "regional", "type": "SpatialConcept"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "ageing", "type": "BiologicFunction"}, {"text": "cohorts", "type": "PopulationGroup"}]}

Example input:
Sentence: Sixty - one patients with a median age of 75 years were available for analysis .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Ten - year other cause mortality -free survival rates were 90 % and 88 % after nephron sparing surgery and radical nephrectomy , respectively .

Example answer:
{"entities": [{"text": "other cause mortality", "type": "Finding"}, {"text": "nephron sparing surgery", "type": "HealthCareActivity"}, {"text": "radical nephrectomy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Multivariate analysis demonstrated that older age ( > 40 years ) and lower baseline RPR titer ( ≤ 1 : 8 ) were associated with serofast status .

Example answer:
{"entities": [{"text": "older age", "type": "PopulationGroup"}]}

Example input:
Sentence: For the post - matching cohort , there was a statistically significant difference in cancer - specific and overall survival favoring the radical surgery group compared with radiation therapy or no treatment group ( P < .0001 for both endpoints ) .

Example answer:
{"entities": [{"text": "cancer", "type": "BiologicFunction"}, {"text": "radical surgery", "type": "HealthCareActivity"}, {"text": "radiation therapy", "type": "HealthCareActivity"}, {"text": "no treatment", "type": "Finding"}]}

Example input:
Sentence: In this sub - group median survival was significantly longer ( 46 versus 11 months ) for patients undergoing resection ( P < 0 .

Example answer:
{"entities": [{"text": "sub - group", "type": "IntellectualProduct"}, {"text": "resection", "type": "HealthCareActivity"}]}

Example input:
Sentence: After stratification by age , comorbidity and cancer stage , the decrease in one - year mortality was most substantial in the 65 - 74 year old age group 41 .

Example answer:
{"entities": [{"text": "stratification by age", "type": "ResearchActivity"}, {"text": "cancer stage", "type": "HealthCareActivity"}, {"text": "old age group", "type": "PopulationGroup"}]}

Input:
Sentence: In multivariate analysis of the matched population , radical surgery , less advanced SEER summary stage , and age less than 70 years were associated with a better overall survival .

## Item MedMentions:test:2677
Example input:
Sentence: 3 percentage points ; 95 % confidence interval [ CI ] , -3 . 33 to 5 . 93 ) .

Example answer:
{"entities": []}

Example input:
Sentence: C / C , HR = 12 . 96 , 95 % confidence interval ( CI ) = 3 . 08 - 54 . 61 , P < 0 . 001 ; T T vs . C / T + C / C , HR = 11 . 71 , 95 % CI = 3 .

Example answer:
{"entities": [{"text": "C", "type": "Chemical"}, {"text": "T", "type": "Chemical"}]}

Example input:
Sentence: 5 % , 95 % confidence interval [ CI ] : 31 . 7 - 33 . 2 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 81 % ( 95 % confidence intervals ( CI ) 0 . 39 % , 1 . 22 % ) , 2 . 22 % ( 95 % CI : 1 . 27 % , 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % ( 95 % confidence interval [ CI ] = 87 . 2 % - 95 . 8 % ) , 95 . 8 % ( 89 .

Example answer:
{"entities": []}

Example input:
Sentence: 340 , 95 % confidence interval ( CI ) : 0 . 162 - 0 . 716 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 69 ; 95 % confidence interval , CI = 0 . 50 - 0 . 96 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 92 ; 95 % confidence interval [ CI ] , 0 . 64 - 1 . 32 ; p = 0 . 650 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 95 , 95 % confidence interval ( CI ) [ 1 . 88 , 2 . 03 ] , and d = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 937 ( 95 % confidence interval ( CI ) : 0 . 922 - 0 . 950 ) and 0 .

Example answer:
{"entities": []}

Input:
Sentence: 80 ( 95 % confidence interval ( CI ) 0 . 70 - 0 . 87 ) , 0 . 82 ( 95 % CI 0 . 74 - 0 . 88 ) and 0 . 87 ( 95 % CI 0 . 75 - 0 . 94 ) , respectively , with a pooled specificity of 0 .

## Item MedMentions:test:2340
Example input:
Sentence: Besides , ACR treatment resulted in a significant reduction in brain ATP level , mitochondrial metabolic function , OXPHOS and TCA enzymes .

Example answer:
{"entities": [{"text": "ACR", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "ATP", "type": "Chemical"}, {"text": "mitochondrial", "type": "AnatomicalStructure"}, {"text": "metabolic function", "type": "BiologicFunction"}, {"text": "OXPHOS", "type": "BiologicFunction"}, {"text": "TCA", "type": "BiologicFunction"}, {"text": "enzymes", "type": "Chemical"}]}

Example input:
Sentence: The suppression of microglial cells using natural bioactive compounds has become increasingly important for brain therapy owing to the expected beneficial effect of lower toxicity .

Example answer:
{"entities": [{"text": "microglial cells", "type": "AnatomicalStructure"}, {"text": "bioactive compounds", "type": "Chemical"}]}

Example input:
Sentence: Intraperitoneal administration increased the amount of mouse natural killer cells and effector memory T cells , as well as T cell reactivity in vivo .

Example answer:
{"entities": [{"text": "mouse natural killer cells", "type": "AnatomicalStructure"}, {"text": "effector memory T cells", "type": "AnatomicalStructure"}, {"text": "T cell", "type": "AnatomicalStructure"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: Cognitive assessment of pycnogenol therapy following traumatic brain injury We have previously shown that pycnogenol ( PYC ) increases antioxidants , decreases oxidative stress , suppresses neuroinflammation and enhances synaptic plasticity following traumatic brain injury ( TBI ) .

Example answer:
{"entities": [{"text": "Cognitive assessment", "type": "HealthCareActivity"}, {"text": "pycnogenol", "type": "Chemical"}, {"text": "therapy", "type": "HealthCareActivity"}, {"text": "traumatic brain injury", "type": "InjuryOrPoisoning"}, {"text": "PYC", "type": "Chemical"}, {"text": "antioxidants", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "enhances synaptic plasticity", "type": "BiologicFunction"}, {"text": "TBI", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: In addition , Isx - 9 treatment was able to completely reverse the marked reduction in these initial stages of the neurogenic process observed in vehicle - treated animals ( which were submitted to repeated handling and exposure to daily intraperitoneal injections ) .

Example answer:
{"entities": [{"text": "Isx - 9", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "neurogenic process", "type": "BiologicFunction"}, {"text": "vehicle", "type": "Chemical"}, {"text": "animals", "type": "Eukaryote"}, {"text": "handling", "type": "HealthCareActivity"}, {"text": "intraperitoneal injections", "type": "HealthCareActivity"}]}

Example input:
Sentence: Treatment improved locomotor function in these severely compromised animals after it had declined to the point at which animals normally die .

Example answer:
{"entities": [{"text": "locomotor function", "type": "BiologicFunction"}, {"text": "animals", "type": "Eukaryote"}, {"text": "die", "type": "BiologicFunction"}]}

Example input:
Sentence: Cell replacement therapy holds great promise as first animal studies using transplantation of neural stem cells to irradiated brain have been successful in restoring memory and cognition deficits .

Example answer:
{"entities": [{"text": "Cell replacement therapy", "type": "HealthCareActivity"}, {"text": "animal", "type": "Eukaryote"}, {"text": "transplantation", "type": "HealthCareActivity"}, {"text": "neural stem cells", "type": "AnatomicalStructure"}, {"text": "irradiated brain", "type": "AnatomicalStructure"}, {"text": "restoring", "type": "HealthCareActivity"}, {"text": "memory", "type": "BiologicFunction"}, {"text": "cognition deficits", "type": "BiologicFunction"}]}

Example input:
Sentence: Mechanistically , the combined treatment promoted post - TBI restorative processes in the brain , including generation of immature neurons , microvessels , and oligodendrocytes , each of which was significantly correlated with the improved cognitive recovery .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "post - TBI", "type": "InjuryOrPoisoning"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "immature neurons", "type": "AnatomicalStructure"}, {"text": "microvessels", "type": "AnatomicalStructure"}, {"text": "oligodendrocytes", "type": "AnatomicalStructure"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: Brains and tissue lysates were collected to study the pathophysiological and molecular changes in the brain of APN - KO mice .

Example answer:
{"entities": [{"text": "Brains", "type": "AnatomicalStructure"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "study", "type": "ResearchActivity"}, {"text": "molecular changes", "type": "BiologicFunction"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "APN - KO mice", "type": "Eukaryote"}]}

Example input:
Sentence: At P14 , relative to controls , LPS and hyperoxia pups had reduced body weight , increased density of apoptotic cells ( TUNEL ) in the cortex , striatum and white matter , astrocytes ( GFAP ) in the white matter and activated microglia ( CD68 ) in the cortex and striatum , but no change in total microglia density ( Iba1 ) .

Example answer:
{"entities": [{"text": "LPS", "type": "Chemical"}, {"text": "hyperoxia", "type": "Finding"}, {"text": "pups", "type": "Eukaryote"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "TUNEL", "type": "ResearchActivity"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "striatum", "type": "AnatomicalStructure"}, {"text": "white matter", "type": "AnatomicalStructure"}, {"text": "astrocytes", "type": "AnatomicalStructure"}, {"text": "GFAP", "type": "Chemical"}, {"text": "microglia", "type": "AnatomicalStructure"}, {"text": "CD68", "type": "Chemical"}, {"text": "Iba1", "type": "Chemical"}]}

Input:
Sentence: Moreover , in treated animals , brain cell density was improved and the number of pyknotic nuclei was decreased .

## Item MedMentions:test:2120
Example input:
Sentence: Further studies indicated that SL4 induced G2 / M arrest in these cell lines .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "indicated", "type": "Finding"}, {"text": "SL4", "type": "Chemical"}, {"text": "G2 / M arrest", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Western blotting analysis demonstrated that the inhibitory effect of STX - 0119 on S6 and 4E - BP1 activation through regulation of YKL - 40 expression occurred in addition to the inhibitory effect of rapamycin against the mTOR pathway .

Example answer:
{"entities": [{"text": "Western blotting analysis", "type": "HealthCareActivity"}, {"text": "inhibitory effect", "type": "BiologicFunction"}, {"text": "STX - 0119", "type": "Chemical"}, {"text": "S6", "type": "Chemical"}, {"text": "4E - BP1", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "YKL - 40", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "rapamycin", "type": "Chemical"}, {"text": "mTOR pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: These cell - based studies were further confirmed in xenograft studies in that the size and rate of tumor growth was inhibited by JQ1 via inhibition of p21 - Cyclin / CDK - Rb - E2F signaling .

Example answer:
{"entities": [{"text": "cell - based studies", "type": "ResearchActivity"}, {"text": "confirmed", "type": "Finding"}, {"text": "xenograft", "type": "HealthCareActivity"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "size", "type": "SpatialConcept"}, {"text": "p21 - Cyclin / CDK - Rb - E2F signaling", "type": "BiologicFunction"}]}

Example input:
Sentence: After paclitaxel treatment , GLT - 1 was significantly down - regulated , and the phosphorylation of ERK1 / 2 and JNK were obviously up - regulated .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "GLT - 1", "type": "Chemical"}, {"text": "down - regulated", "type": "BiologicFunction"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "ERK1", "type": "Chemical"}, {"text": "2", "type": "Chemical"}, {"text": "JNK", "type": "Chemical"}, {"text": "up - regulated", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , we report that SL4 is able to inhibit the proliferation of different types of breast cancer cell in vitro and in vivo by inducing G2 / M cell cycle arrest .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "SL4", "type": "Chemical"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "breast cancer cell", "type": "AnatomicalStructure"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "G2 / M cell cycle arrest", "type": "BiologicFunction"}]}

Example input:
Sentence: JQ1 markedly inhibited proliferation of 4 ATC cell lines by suppression of MYC and elevation of p21and p27 to decrease phosphorylated Rb to delay cell cycle progression from the G0 / G1 phase to the S phase .

Example answer:
{"entities": [{"text": "ATC", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "MYC", "type": "Chemical"}, {"text": "elevation", "type": "SpatialConcept"}, {"text": "p21and p27", "type": "Chemical"}, {"text": "phosphorylated", "type": "BiologicFunction"}, {"text": "Rb", "type": "Chemical"}, {"text": "delay cell cycle", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , SL4 suppressed the growth of established breast tumors in nude mice through upregulation of p21 and downregulation of cdc25C , and displayed a good safety profile .

Example answer:
{"entities": [{"text": "SL4", "type": "Chemical"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "breast tumors", "type": "BiologicFunction"}, {"text": "nude mice", "type": "Eukaryote"}, {"text": "upregulation", "type": "BiologicFunction"}, {"text": "p21", "type": "Chemical"}, {"text": "downregulation", "type": "BiologicFunction"}, {"text": "cdc25C", "type": "Chemical"}]}

Example input:
Sentence: Notably , the attenuation of JNK activation by a specific inhibitor ( SP600125 ) reduced ApxI -induced NF - κB activation , whereas a p38 blocker ( SB203580 ) had no effect on the NF - κB pathway .

Example answer:
{"entities": [{"text": "JNK", "type": "Chemical"}, {"text": "SP600125", "type": "Chemical"}, {"text": "ApxI", "type": "Chemical"}, {"text": "NF - κB activation", "type": "BiologicFunction"}, {"text": "p38 blocker", "type": "Chemical"}, {"text": "SB203580", "type": "Chemical"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Pep5 induced permanent extracellular signal - regulated kinase ( ERK1 / 2 ) phosphorylation in MDA - MB - 231 cells synchronized in G1 / S or S phase .

Example answer:
{"entities": [{"text": "Pep5", "type": "Chemical"}, {"text": "extracellular signal - regulated kinase", "type": "Chemical"}, {"text": "ERK1 / 2", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "G1 / S", "type": "BiologicFunction"}]}

Example input:
Sentence: Notably , SL4 treatment resulted in an obvious increase in p21 mRNA and protein levels through activation of MAPK signaling pathways , but not the TGF - β pathway .

Example answer:
{"entities": [{"text": "SL4", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "p21", "type": "AnatomicalStructure"}, {"text": "mRNA", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "MAPK signaling pathways", "type": "BiologicFunction"}, {"text": "TGF - β pathway", "type": "BiologicFunction"}]}

Input:
Sentence: SP600125 and PD98059 , specific inhibitors of JNK kinase and ERK kinase , significantly blocked the SL4 - induced G2 / M phase arrest and upregulation of p21 .

## Item MedMentions:test:2139
Example input:
Sentence: fMRI data were analyzing focusing on a priori regions of interest ( ROIs ) of the core neural systems of mental state attribution : the medial prefrontal cortex ( mPFC ) , temporoparietal junction ( TPJ ) and precuneus .

Example answer:
{"entities": [{"text": "fMRI", "type": "HealthCareActivity"}, {"text": "analyzing", "type": "ResearchActivity"}, {"text": "regions of interest", "type": "SpatialConcept"}, {"text": "ROIs", "type": "SpatialConcept"}, {"text": "core", "type": "SpatialConcept"}, {"text": "mental state", "type": "Finding"}, {"text": "attribution", "type": "BiologicFunction"}, {"text": "medial prefrontal cortex", "type": "AnatomicalStructure"}, {"text": "mPFC", "type": "AnatomicalStructure"}, {"text": "temporoparietal junction", "type": "SpatialConcept"}, {"text": "TPJ", "type": "SpatialConcept"}, {"text": "precuneus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Significant brain , cortical GM , hippocampal , deep GM nuclei , and WM atrophy was found in patients with MS with cognitive impairment versus those who were cognitively preserved .

Example answer:
{"entities": [{"text": "brain", "type": "AnatomicalStructure"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "GM", "type": "AnatomicalStructure"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "deep GM", "type": "AnatomicalStructure"}, {"text": "nuclei", "type": "AnatomicalStructure"}, {"text": "WM", "type": "AnatomicalStructure"}, {"text": "atrophy", "type": "BiologicFunction"}, {"text": "MS", "type": "BiologicFunction"}, {"text": "cognitive impairment", "type": "BiologicFunction"}, {"text": "cognitively preserved", "type": "Finding"}]}

Example input:
Sentence: Focal WM and cortical lesions were identified , and volumetric measures from WM , cortical GM , the hippocampus , and deep GM nuclei were obtained .

Example answer:
{"entities": [{"text": "WM", "type": "AnatomicalStructure"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "lesions", "type": "Finding"}, {"text": "volumetric", "type": "SpatialConcept"}, {"text": "GM", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "deep GM", "type": "AnatomicalStructure"}, {"text": "nuclei", "type": "AnatomicalStructure"}]}

Example input:
Sentence: WMH volumes in individual tracts explained more variance in cognition than total WMH burden , emphasizing the importance of lesion location when addressing the functional consequences of WMHs .

Example answer:
{"entities": [{"text": "WMH", "type": "BiologicFunction"}, {"text": "tracts", "type": "AnatomicalStructure"}, {"text": "cognition", "type": "BiologicFunction"}, {"text": "WMHs", "type": "BiologicFunction"}]}

Example input:
Sentence: Region of interest - based analyses showed that WMH volume within the anterior thalamic radiation explained 6 .

Example answer:
{"entities": [{"text": "Region of interest - based analyses", "type": "ResearchActivity"}, {"text": "WMH", "type": "BiologicFunction"}, {"text": "within", "type": "SpatialConcept"}, {"text": "anterior thalamic radiation", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Our findings identify the anterior thalamic radiation and forceps minor as strategic white matter tracts in which WMHs are most strongly associated with cognitive impairment in memory clinic patients with SVD .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "anterior thalamic radiation", "type": "AnatomicalStructure"}, {"text": "forceps minor", "type": "AnatomicalStructure"}, {"text": "white matter", "type": "AnatomicalStructure"}, {"text": "tracts", "type": "AnatomicalStructure"}, {"text": "WMHs", "type": "BiologicFunction"}, {"text": "cognitive impairment", "type": "BiologicFunction"}, {"text": "memory clinic", "type": "Organization"}, {"text": "SVD", "type": "BiologicFunction"}]}

Example input:
Sentence: Impact of Strategically Located White Matter Hyperintensities on Cognition in Memory Clinic Patients with Small Vessel Disease Studies on the impact of small vessel disease ( SVD ) on cognition generally focus on white matter hyperintensity ( WMH ) volume .

Example answer:
{"entities": [{"text": "White Matter Hyperintensities", "type": "BiologicFunction"}, {"text": "Cognition", "type": "BiologicFunction"}, {"text": "Memory Clinic", "type": "Organization"}, {"text": "Small Vessel Disease", "type": "BiologicFunction"}, {"text": "small vessel disease", "type": "BiologicFunction"}, {"text": "SVD", "type": "BiologicFunction"}, {"text": "cognition", "type": "BiologicFunction"}, {"text": "focus", "type": "SpatialConcept"}, {"text": "white matter hyperintensity", "type": "BiologicFunction"}, {"text": "WMH", "type": "BiologicFunction"}]}

Example input:
Sentence: We examined the relation between WMH location and cognition in a memory clinic cohort of patients with sporadic SVD .

Example answer:
{"entities": [{"text": "WMH", "type": "BiologicFunction"}, {"text": "location", "type": "SpatialConcept"}, {"text": "cognition", "type": "BiologicFunction"}, {"text": "memory clinic", "type": "Organization"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "SVD", "type": "BiologicFunction"}]}

Example input:
Sentence: The extent to which WMH location relates to cognitive performance has received less attention , but is likely to be functionally important .

Example answer:
{"entities": [{"text": "extent", "type": "SpatialConcept"}, {"text": "WMH", "type": "BiologicFunction"}, {"text": "location", "type": "SpatialConcept"}, {"text": "cognitive performance", "type": "BiologicFunction"}, {"text": "attention", "type": "BiologicFunction"}]}

Example input:
Sentence: Region of interest - based analyses showed that WMHs located particularly within the anterior thalamic radiation and forceps minor were inversely associated with both executive functioning and visuomotor speed , independent of total WMH volume .

Example answer:
{"entities": [{"text": "Region of interest - based analyses", "type": "ResearchActivity"}, {"text": "WMHs", "type": "BiologicFunction"}, {"text": "located", "type": "SpatialConcept"}, {"text": "within", "type": "SpatialConcept"}, {"text": "anterior thalamic radiation", "type": "AnatomicalStructure"}, {"text": "forceps minor", "type": "AnatomicalStructure"}, {"text": "executive functioning", "type": "BiologicFunction"}, {"text": "visuomotor speed", "type": "BiologicFunction"}, {"text": "WMH", "type": "BiologicFunction"}]}

Input:
Sentence: Assumption - free region of interest - based analyses based on major white matter tracts and voxel - wise analyses were used to determine the association between WMH location and executive functioning , visuomotor speed and memory .

## Item MedMentions:test:2634
Example input:
Sentence: ICU length of stay was shorter ( 3 days [ 1 - 5 ] vs .

Example answer:
{"entities": [{"text": "ICU", "type": "Organization"}]}

Example input:
Sentence: EGDT seems to increase the resource demand in terms of ICU admissions and cardiocirculatory support necessity without reducing mortality , renal and respiratory organ support necessity , respiratory and cardiocirculatory support duration , and length of hospital stay .

Example answer:
{"entities": [{"text": "EGDT", "type": "HealthCareActivity"}, {"text": "ICU admissions", "type": "HealthCareActivity"}, {"text": "renal", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The primary results showed that the length of stay in the intensive care unit ( ICU ) was longer in the control group than in the RIPC group ( 52 . 30 ± 13 .

Example answer:
{"entities": [{"text": "intensive care unit", "type": "Organization"}, {"text": "ICU", "type": "Organization"}, {"text": "RIPC", "type": "HealthCareActivity"}]}

Example input:
Sentence: Individual studies reported shorter intensive care unit stay and duration of mechanical ventilation of patients given adjunctive corticosteroids .

Example answer:
{"entities": [{"text": "Individual", "type": "PopulationGroup"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "intensive care unit", "type": "Organization"}, {"text": "mechanical ventilation", "type": "HealthCareActivity"}, {"text": "adjunctive corticosteroids", "type": "Chemical"}]}

Example input:
Sentence: Patient - controlled analgesia IV morphine consumption 0 to 24 hours postoperatively was significantly reduced in the ketamine group compared with the placebo group : 79 ( 47 ) vs 121 ( 53 ) mg IV , mean difference 42 mg ( 95 % confidence interval -59 to -25 ) , P < 0 . 001 .

Example answer:
{"entities": [{"text": "Patient - controlled analgesia", "type": "HealthCareActivity"}, {"text": "morphine", "type": "Chemical"}, {"text": "ketamine", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: Our study suggested that coil embolization of small UIAs can achieve a high rate of progressive occlusion and low rate of recanalization during follow - up .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "coil embolization", "type": "HealthCareActivity"}, {"text": "UIAs", "type": "BiologicFunction"}, {"text": "recanalization", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: In order to reduce unplanned ICU admissions , improving the monitoring of patients is therefore warranted .

Example answer:
{"entities": [{"text": "ICU admissions", "type": "HealthCareActivity"}, {"text": "monitoring", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , patients receiving aprotinin had a significantly shorter adjusted ICU length of stay .

Example answer:
{"entities": [{"text": "aprotinin", "type": "Chemical"}]}

Example input:
Sentence: Our findings suggest that efforts to reduce AKI in the perioperative period may have a significant long - term impact on patients and payers in reducing mortality and health care utilization .

Example answer:
{"entities": [{"text": "AKI", "type": "InjuryOrPoisoning"}, {"text": "health care utilization", "type": "HealthCareActivity"}]}

Example input:
Sentence: The main advantage is a low postoperative pain level , but with an insufficient HVA correction .

Example answer:
{"entities": [{"text": "postoperative pain", "type": "Finding"}, {"text": "HVA correction", "type": "HealthCareActivity"}]}

Input:
Sentence: Because of a small size effect , and despite significant analgesic effects , this strategy failed to reduce the time spent in ICU .

## Item MedMentions:test:1583
Example input:
Sentence: We show that RA190 reduces the expression of Stat3 and the levels of key immunosuppressive enzymes and cytokines arginase , iNOS , and IL - 10 in MDSCs , while boosting expression of the immunostimulatory cytokine IL - 12 .

Example answer:
{"entities": [{"text": "RA190", "type": "Chemical"}, {"text": "Stat3", "type": "Chemical"}, {"text": "immunosuppressive", "type": "BiologicFunction"}, {"text": "enzymes", "type": "Chemical"}, {"text": "cytokines", "type": "Chemical"}, {"text": "arginase", "type": "Chemical"}, {"text": "iNOS", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "MDSCs", "type": "AnatomicalStructure"}, {"text": "immunostimulatory", "type": "HealthCareActivity"}, {"text": "cytokine", "type": "Chemical"}, {"text": "IL - 12", "type": "Chemical"}]}

Example input:
Sentence: Curcumin is a natural antioxidant and antihypertrophic agent , but it has poor biostability .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}, {"text": "antioxidant", "type": "Chemical"}, {"text": "antihypertrophic agent", "type": "Chemical"}]}

Example input:
Sentence: The following groups were used for the in vitro experiment : control siRNA , GRIM - 19 siRNA , IFN - β / RA and IFN - β / RA + curcumin .

Example answer:
{"entities": [{"text": "experiment", "type": "ResearchActivity"}, {"text": "siRNA", "type": "Chemical"}, {"text": "GRIM - 19", "type": "AnatomicalStructure"}, {"text": "IFN - β", "type": "Chemical"}, {"text": "RA", "type": "Chemical"}, {"text": "curcumin", "type": "Chemical"}]}

Example input:
Sentence: Design , synthesis , and evaluation of curcumin derivatives as Nrf2 activators and cytoprotectors against oxidative death Activation of nuclear factor erythroid - 2 - related factor 2 ( Nrf2 ) has been proven to be an effective means to prevent the development of cancer , and natural curcumin stands out as a potent Nrf2 activator and cancer chemopreventive agent .

Example answer:
{"entities": [{"text": "evaluation", "type": "HealthCareActivity"}, {"text": "curcumin", "type": "Chemical"}, {"text": "derivatives", "type": "Chemical"}, {"text": "Nrf2", "type": "Chemical"}, {"text": "cytoprotectors", "type": "BiologicFunction"}, {"text": "oxidative death", "type": "BiologicFunction"}, {"text": "nuclear factor erythroid - 2 - related factor 2", "type": "Chemical"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "chemopreventive agent", "type": "Chemical"}]}

Example input:
Sentence: Nanocurcumin supplementation decreased HH -induced RVH and apoptosis while modulating cardiac cGMP / cGK - 1 signaling , and maintaining CaMkinase II , intracellular calcium levels and redox status better than curcumin .

Example answer:
{"entities": [{"text": "Nanocurcumin", "type": "Chemical"}, {"text": "supplementation", "type": "HealthCareActivity"}, {"text": "HH", "type": "BiologicFunction"}, {"text": "RVH", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "cardiac", "type": "AnatomicalStructure"}, {"text": "cGMP", "type": "Chemical"}, {"text": "cGK - 1", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "CaMkinase II", "type": "Chemical"}, {"text": "intracellular", "type": "SpatialConcept"}, {"text": "calcium levels", "type": "Finding"}, {"text": "redox status", "type": "BiologicFunction"}, {"text": "curcumin", "type": "Chemical"}]}

Example input:
Sentence: GRIM - 19 siRNA promoted MCF - 7 cell proliferation and migration ; inhibited cell apoptosis ; and promoted the expression of STAT3 , survivin , Bcl - 2 and MMP - 9 .

Example answer:
{"entities": [{"text": "GRIM - 19", "type": "AnatomicalStructure"}, {"text": "siRNA", "type": "Chemical"}, {"text": "MCF - 7 cell", "type": "AnatomicalStructure"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "migration", "type": "BiologicFunction"}, {"text": "cell apoptosis", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "STAT3", "type": "Chemical"}, {"text": "survivin", "type": "Chemical"}, {"text": "Bcl - 2", "type": "Chemical"}, {"text": "MMP - 9", "type": "Chemical"}]}

Example input:
Sentence: IFN - β / RA inhibited cell proliferation and migration ; promoted cell apoptosis ; up - regulated GRIM - 19 ; and inhibited the expression of STAT3 , survivin , Bcl - 2 and MMP - 9 .

Example answer:
{"entities": [{"text": "IFN - β", "type": "Chemical"}, {"text": "RA", "type": "Chemical"}, {"text": "cell proliferation", "type": "BiologicFunction"}, {"text": "migration", "type": "BiologicFunction"}, {"text": "cell apoptosis", "type": "BiologicFunction"}, {"text": "up - regulated", "type": "BiologicFunction"}, {"text": "GRIM - 19", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "STAT3", "type": "Chemical"}, {"text": "survivin", "type": "Chemical"}, {"text": "Bcl - 2", "type": "Chemical"}, {"text": "MMP - 9", "type": "Chemical"}]}

Example input:
Sentence: Combination treatment of curcumin and IFN - β / RA had a stronger effect than that of the IFN - β / RA group .

Example answer:
{"entities": [{"text": "Combination treatment", "type": "HealthCareActivity"}, {"text": "curcumin", "type": "Chemical"}, {"text": "IFN - β", "type": "Chemical"}, {"text": "RA", "type": "Chemical"}]}

Example input:
Sentence: In addition , curcumin and IFN - β / RA combination inhibited the expression of COX - 2 and up - regulated GADD153 .

Example answer:
{"entities": [{"text": "curcumin", "type": "Chemical"}, {"text": "IFN - β", "type": "Chemical"}, {"text": "RA", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "COX - 2", "type": "Chemical"}, {"text": "up - regulated", "type": "BiologicFunction"}, {"text": "GADD153", "type": "Chemical"}]}

Example input:
Sentence: Curcumin synergistically increases the effects of IFN - β / RA on breast cancer cells .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}, {"text": "IFN - β", "type": "Chemical"}, {"text": "RA", "type": "Chemical"}, {"text": "breast cancer cells", "type": "AnatomicalStructure"}]}

Input:
Sentence: Curcumin synergistically increases effects of β - interferon and retinoic acid on breast cancer cells in vitro and in vivo by up - regulation of GRIM - 19 through STAT3 - dependent and STAT3 - independent pathways The study aimed to investigate the effects of combination treatment of curcumin and β - interferon ( IFN - β ) / retinoic acid ( RA ) on breast cancer cells , including cell viability , apoptosis and migration , and to determine the mechanisms related to GRIM - 19 through STAT3 - dependent and STAT3 - independent pathways .

## Item MedMentions:test:2391
Example input:
Sentence: These results demonstrate that salinity - adapted , ACD -producing bacteria isolated from halophytes could promote sugar beet growth under saline stress conditions .

Example answer:
{"entities": [{"text": "salinity", "type": "Finding"}, {"text": "adapted", "type": "BiologicFunction"}, {"text": "ACD", "type": "Chemical"}, {"text": "bacteria", "type": "Bacterium"}, {"text": "halophytes", "type": "Eukaryote"}, {"text": "sugar beet", "type": "Eukaryote"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "saline stress conditions", "type": "BiologicFunction"}]}

Example input:
Sentence: Results show that micro - algae are neither competitive yet with traditional oil crops nor with fossil fuel .

Example answer:
{"entities": [{"text": "micro - algae", "type": "Eukaryote"}, {"text": "oil", "type": "Chemical"}, {"text": "crops", "type": "Eukaryote"}]}

Example input:
Sentence: The results demonstrated that microbial metabolic activities were greatly restrained in saline water irrigated soils , as average well color development ( AWCD ) reduced under all saline water irrigation treatments .

Example answer:
{"entities": [{"text": "greatly restrained", "type": "Finding"}]}

Example input:
Sentence: This experiment was to investigate the biological effect of Ca ( 2 + ) , Mg ( 2 + ) , Cu ( 2 + ) , Fe ( 2 + ) , Zn ( 2 + ) , and K ( + ) which are the most common ions present in biological wastewater treatment systems , on the microbial attachment of AGAS and flocculent activated sludge ( FAS ) , from which AGAS is always derived , in order to provide a new strategy for the rapid cultivation and stability control of AGAS .

Example answer:
{"entities": [{"text": "Ca ( 2 + ) ,", "type": "Chemical"}, {"text": "Mg ( 2 + )", "type": "Chemical"}, {"text": "Cu ( 2 + )", "type": "Chemical"}, {"text": "Fe ( 2 + )", "type": "Chemical"}, {"text": "Zn ( 2 + )", "type": "Chemical"}, {"text": "K ( + )", "type": "Chemical"}, {"text": "ions", "type": "Chemical"}, {"text": "flocculent", "type": "BiologicFunction"}]}

Example input:
Sentence: An in vitro attempt has been taken to overcome the endophytic contamination by using broad spectrum antibiotics as surface sterilant as well as a media component .

Example answer:
{"entities": [{"text": "in vitro attempt", "type": "HealthCareActivity"}, {"text": "broad spectrum antibiotics", "type": "Chemical"}]}

Example input:
Sentence: how nutrient enrichment ( i . e . , nitrogen availability ) affected the growth of Fucus vesiculosus , a foundational macroalgal species in the North Atlantic rocky intertidal zone , and found that nutrient -enriched algal blades showed a significant increase in tissue growth compared to individuals grown under ambient conditions .

Example answer:
{"entities": [{"text": "nutrient", "type": "Food"}, {"text": "nitrogen", "type": "Chemical"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "Fucus vesiculosus", "type": "Eukaryote"}, {"text": "macroalgal", "type": "Eukaryote"}, {"text": "species", "type": "Eukaryote"}, {"text": "North Atlantic rocky intertidal zone", "type": "SpatialConcept"}, {"text": "algal blades", "type": "IntellectualProduct"}, {"text": "tissue growth", "type": "BiologicFunction"}]}

Example input:
Sentence: Ammonia tolerant inocula provide a good base for anaerobic digestion of microalgae in third generation biogas process This study investigated the ability of an ammonia - acclimatized inoculum to digest efficiently protein -rich microalgae for continuous 3rd generation biogas production .

Example answer:
{"entities": [{"text": "Ammonia", "type": "Chemical"}, {"text": "digestion", "type": "BiologicFunction"}, {"text": "microalgae", "type": "Eukaryote"}, {"text": "biogas", "type": "Chemical"}, {"text": "ammonia", "type": "Chemical"}, {"text": "acclimatized", "type": "BiologicFunction"}, {"text": "protein", "type": "Chemical"}]}

Example input:
Sentence: The use of renewable technologies as photovoltaics and biogas self production might increase the competitiveness of micro - algae oil .

Example answer:
{"entities": [{"text": "biogas", "type": "Chemical"}, {"text": "micro - algae", "type": "Eukaryote"}, {"text": "oil", "type": "Chemical"}]}

Example input:
Sentence: Cultivation of four microalgae species in the effluent of anaerobic digester for biodiesel production This study investigated if an effluent from anaerobic digestion ( AD ) system can be used as a nutrients source for the microalgae cultivation , and in so doing , if the effluent can be properly treated .

Example answer:
{"entities": [{"text": "Cultivation", "type": "HealthCareActivity"}, {"text": "microalgae", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "biodiesel", "type": "Chemical"}, {"text": "study", "type": "ResearchActivity"}, {"text": "nutrients", "type": "Food"}, {"text": "source", "type": "Finding"}, {"text": "cultivation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Nitrogen and phosphorus in the AD effluent well supported microalgal growth , and their removal efficiency reached > 97 .

Example answer:
{"entities": [{"text": "Nitrogen", "type": "Chemical"}, {"text": "phosphorus", "type": "Chemical"}, {"text": "microalgal", "type": "Eukaryote"}, {"text": "growth", "type": "BiologicFunction"}]}

Input:
Sentence: This study supports that the AD effluent can indeed serve as a cheap and nutrient - rich medium for microalgae cultivation , and equally importantly , microalgae can be a workable treatment option for it .

## Item MedMentions:test:2330
Example input:
Sentence: Initial attempts of fluid resuscitation failed to improve patient 's clinical condition .

Example answer:
{"entities": [{"text": "fluid resuscitation", "type": "HealthCareActivity"}, {"text": "improve", "type": "Finding"}]}

Example input:
Sentence: The primary outcome was a composite administration of intravenous fluid resuscitation in the first 24 h , insulin bolus and initial insulin infusion rate .

Example answer:
{"entities": [{"text": "administration", "type": "HealthCareActivity"}, {"text": "intravenous fluid resuscitation", "type": "HealthCareActivity"}, {"text": "insulin", "type": "Chemical"}, {"text": "bolus", "type": "HealthCareActivity"}]}

Example input:
Sentence: 9 % for fluid resuscitation ( P = 0 . 0001 ) , 55 % versus 49 . 1 % for insulin bolus ( P = 0 . 58 ) and 60 % versus 81 .

Example answer:
{"entities": [{"text": "fluid resuscitation", "type": "HealthCareActivity"}, {"text": "insulin", "type": "Chemical"}, {"text": "bolus", "type": "HealthCareActivity"}]}

Example input:
Sentence: As a surrogate for perfusion , early and aggressive fluid resuscitation therapy ( guided by lactic acid levels ) was instituted ; 2 . also early in the treatment , broad spectrum antibiotics were administered ; 3 . to guide antibiotic therapy , microbiological cultures were obtained .

Example answer:
{"entities": [{"text": "perfusion", "type": "HealthCareActivity"}, {"text": "fluid resuscitation therapy", "type": "HealthCareActivity"}, {"text": "lactic acid levels", "type": "HealthCareActivity"}, {"text": "antibiotics", "type": "Chemical"}, {"text": "antibiotic therapy", "type": "HealthCareActivity"}, {"text": "microbiological cultures", "type": "HealthCareActivity"}]}

Example input:
Sentence: Measurement of lactate levels is associated with improved outcomes in adult septic shock , but pediatric guidelines do not endorse its use , in part because the association between early lactate levels and mortality is unknown in pediatric sepsis .

Example answer:
{"entities": [{"text": "lactate levels", "type": "Finding"}, {"text": "outcomes", "type": "ResearchActivity"}, {"text": "septic shock", "type": "BiologicFunction"}, {"text": "pediatric guidelines", "type": "IntellectualProduct"}, {"text": "early lactate levels", "type": "Finding"}, {"text": "sepsis", "type": "BiologicFunction"}]}

Example input:
Sentence: Early goal - directed treatment versus standard care in management of early septic shock : Meta - analysis of randomized trials Since the incorporation of the early hemodynamic resuscitation in septic shock according to the early goal - directed therapy ( EGDT ) protocol among the 6 - hour resuscitation bundle of the Surviving Sepsis Campaign guidelines , a great debate has been raised about the issue .

Example answer:
{"entities": [{"text": "Early goal - directed treatment", "type": "HealthCareActivity"}, {"text": "standard care", "type": "HealthCareActivity"}, {"text": "septic shock", "type": "BiologicFunction"}, {"text": "Meta - analysis", "type": "ResearchActivity"}, {"text": "randomized trials", "type": "ResearchActivity"}, {"text": "hemodynamic", "type": "BiologicFunction"}, {"text": "resuscitation", "type": "HealthCareActivity"}, {"text": "early goal - directed therapy", "type": "HealthCareActivity"}, {"text": "EGDT", "type": "HealthCareActivity"}, {"text": "protocol", "type": "HealthCareActivity"}, {"text": "Surviving Sepsis Campaign guidelines", "type": "IntellectualProduct"}]}

Example input:
Sentence: Participants are children aged 29 days to under 18 years with suspected or confirmed septic shock and a need for ongoing resuscitation .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "confirmed", "type": "Finding"}, {"text": "septic shock", "type": "BiologicFunction"}, {"text": "resuscitation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Coming full circle : thirty years of paediatric fluid resuscitation Fluid bolus therapy ( FBT ) is a cornerstone of the management of the septic child , but clinical research in this field is challenging to perform , and hard to interpret .

Example answer:
{"entities": [{"text": "paediatric", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "fluid resuscitation", "type": "HealthCareActivity"}, {"text": "Fluid bolus therapy", "type": "HealthCareActivity"}, {"text": "FBT", "type": "HealthCareActivity"}, {"text": "cornerstone of the management", "type": "HealthCareActivity"}, {"text": "clinical research", "type": "ResearchActivity"}]}

Example input:
Sentence: A trial to determine whether septic shock - reversal is quicker in pediatric patients randomized to an early goal - directed fluid - sparing strategy versus usual care ( SQUEEZE ) : study protocol for a pilot randomized controlled trial Current pediatric septic shock resuscitation guidelines from the American College of Critical Care Medicine focus on the early and goal - directed administration of intravascular fluid followed by vasoactive medication infusions for persistent and fluid - refractory shock .

Example answer:
{"entities": [{"text": "trial", "type": "ResearchActivity"}, {"text": "septic shock", "type": "BiologicFunction"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "goal - directed fluid - sparing strategy", "type": "HealthCareActivity"}, {"text": "SQUEEZE", "type": "ResearchActivity"}, {"text": "study protocol", "type": "IntellectualProduct"}, {"text": "pilot randomized controlled trial", "type": "ResearchActivity"}, {"text": "resuscitation", "type": "HealthCareActivity"}, {"text": "guidelines", "type": "IntellectualProduct"}, {"text": "American College of Critical Care Medicine", "type": "Organization"}, {"text": "goal - directed administration", "type": "HealthCareActivity"}, {"text": "intravascular", "type": "SpatialConcept"}, {"text": "fluid", "type": "BodySubstance"}, {"text": "medication", "type": "Chemical"}, {"text": "infusions", "type": "HealthCareActivity"}, {"text": "fluid - refractory shock", "type": "BiologicFunction"}]}

Example input:
Sentence: The optimal amount of intravascular fluid required in early pediatric septic shock resuscitation prior to the initiation of vasoactive support remains unanswered .

Example answer:
{"entities": [{"text": "intravascular", "type": "SpatialConcept"}, {"text": "fluid", "type": "BodySubstance"}, {"text": "septic shock", "type": "BiologicFunction"}, {"text": "resuscitation", "type": "HealthCareActivity"}]}

Input:
Sentence: The optimal degree of fluid resuscitation and the timing of initiation of vasoactive support in order to achieve recommended therapeutic targets in children with septic shock remains unanswered .

## Item MedMentions:test:2472
Example input:
Sentence: Serial mixed - mode assessments 6 weeks , 6 months and 1 year after MVC include an assessment of adverse sequelae , general health status and health service utilisation .

Example answer:
{"entities": [{"text": "assessments", "type": "HealthCareActivity"}, {"text": "MVC", "type": "InjuryOrPoisoning"}, {"text": "assessment", "type": "HealthCareActivity"}, {"text": "adverse sequelae", "type": "BiologicFunction"}]}

Example input:
Sentence: One of these pathways is phosphatidylinositol - 3 kinases ( PI3K ) / protein kinase B ( AKT ) / rapamycin - sensitive mTOR - complex ( mTOR ) pathway , intensively studied and widely described so far .

Example answer:
{"entities": [{"text": "pathways", "type": "BiologicFunction"}, {"text": "rapamycin - sensitive mTOR - complex ( mTOR ) pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: The Electrophoretic mobility shift assays ( EMSA ) and chromatin immunoprecipitation ( ChIP ) assays determined the MyoD binding site in Mef2c promoter .

Example answer:
{"entities": [{"text": "Electrophoretic mobility shift assays", "type": "HealthCareActivity"}, {"text": "EMSA", "type": "HealthCareActivity"}, {"text": "chromatin immunoprecipitation ( ChIP ) assays", "type": "HealthCareActivity"}, {"text": "MyoD", "type": "Chemical"}, {"text": "binding site", "type": "SpatialConcept"}, {"text": "Mef2c", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}]}

Example input:
Sentence: MVD was significantly higher in SACs , but the serrated morphology was the only significant predictor of MVD in CRC in multivariate analyses .

Example answer:
{"entities": [{"text": "SACs", "type": "BiologicFunction"}, {"text": "serrated", "type": "AnatomicalStructure"}, {"text": "CRC", "type": "BiologicFunction"}]}

Example input:
Sentence: Moreover , four specific pathways were unveiled in the network analysis of the overlaps , i .

Example answer:
{"entities": [{"text": "pathways", "type": "BiologicFunction"}, {"text": "network analysis", "type": "IntellectualProduct"}, {"text": "overlaps", "type": "SpatialConcept"}]}

Example input:
Sentence: 1 , OLIG2 , and COUP - TFII expression occupied distinct ( although overlapping ) neurogenic domains which extended into the cortex and revealed three CGE compartments : lateral , medial , and ventral .

Example answer:
{"entities": [{"text": "1", "type": "Chemical"}, {"text": "OLIG2", "type": "Chemical"}, {"text": "COUP - TFII", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "neurogenic domains", "type": "AnatomicalStructure"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "CGE compartments", "type": "AnatomicalStructure"}, {"text": "lateral", "type": "SpatialConcept"}, {"text": "medial", "type": "SpatialConcept"}, {"text": "ventral", "type": "SpatialConcept"}]}

Example input:
Sentence: Our study provides a novel strategy for improving production of a target compound through integration and modulation of heterologous pathways in both transcription and translation level .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "compound", "type": "Chemical"}, {"text": "integration", "type": "BiologicFunction"}, {"text": "pathways", "type": "BiologicFunction"}, {"text": "transcription", "type": "BiologicFunction"}, {"text": "translation", "type": "BiologicFunction"}]}

Example input:
Sentence: A pathway based analysis revealed a network of Pa14 and Ma549 - resistance genes that are functionally connected through processes that encompass phagocytosis and engulfment , cell mobility , intermediary metabolism , protein phosphorylation , axon guidance , response to DNA damage , and drug metabolism .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "Pa14", "type": "Bacterium"}, {"text": "Ma549", "type": "Eukaryote"}, {"text": "resistance", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "phagocytosis", "type": "BiologicFunction"}, {"text": "engulfment", "type": "BiologicFunction"}, {"text": "cell mobility", "type": "BiologicFunction"}, {"text": "intermediary metabolism", "type": "BiologicFunction"}, {"text": "protein phosphorylation", "type": "BiologicFunction"}, {"text": "axon guidance", "type": "BiologicFunction"}, {"text": "response to DNA damage", "type": "BiologicFunction"}, {"text": "drug metabolism", "type": "BiologicFunction"}]}

Example input:
Sentence: These modules were individually modulated with regulatory parts to optimize efficiency of the pathway in terms of downstream isoprenoid production .

Example answer:
{"entities": [{"text": "modules", "type": "BiologicFunction"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "isoprenoid", "type": "Chemical"}]}

Example input:
Sentence: In addition , a genetically hard - coded chassis with both efficient MEP and MVA pathways for isoprenoid precursor supply was constructed in this work .

Example answer:
{"entities": [{"text": "MEP", "type": "BiologicFunction"}, {"text": "MVA pathways", "type": "BiologicFunction"}, {"text": "isoprenoid", "type": "Chemical"}]}

Input:
Sentence: In this study , MVA pathway was divided into three modules , and two heterologous modules were integrated into the E .

## Item MedMentions:test:2716
Example input:
Sentence: 05 for both groups .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: 05 vs .

Example answer:
{"entities": []}

Example input:
Sentence: 05 vs .

Example answer:
{"entities": []}

Example input:
Sentence: 05 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 ( .

Example answer:
{"entities": []}

Input:
Sentence: 05 ) .

## Item MedMentions:test:2550
Example input:
Sentence: A sectors approach shows good screening test characteristics for the detection of CSME .

Example answer:
{"entities": [{"text": "sectors", "type": "SpatialConcept"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "screening test", "type": "HealthCareActivity"}, {"text": "CSME", "type": "BiologicFunction"}]}

Example input:
Sentence: 8 ± 6 % ) and HSM ( 97 . 5 ± 8 % ) provided no significant differences in the overall diagnostic image quality .

Example answer:
{"entities": [{"text": "HSM", "type": "HealthCareActivity"}]}

Example input:
Sentence: This investigation was a cross - sectional study of CSME grading in monoscopic images using a sectors approach .

Example answer:
{"entities": [{"text": "cross - sectional study", "type": "ResearchActivity"}, {"text": "CSME", "type": "BiologicFunction"}, {"text": "monoscopic images", "type": "IntellectualProduct"}, {"text": "sectors", "type": "SpatialConcept"}, {"text": "approach", "type": "SpatialConcept"}]}

Example input:
Sentence: In this observational cross - sectional study , two masked operators measured CCT thickness twice in 28 healthy eyes .

Example answer:
{"entities": [{"text": "cross - sectional study", "type": "ResearchActivity"}, {"text": "CCT", "type": "ClinicalAttribute"}, {"text": "eyes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A total of 30 , 428 eyes ( 7 , 332 in Group 1 and 23 , 096 in Group 2 ) were studied .

Example answer:
{"entities": [{"text": "eyes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: CSM after 3 years in patients with ipsilateral , contralateral , and bilateral LN metastasis was 41 , 67 , and 100 % , respectively ( p = 0 . 042 ) .

Example answer:
{"entities": [{"text": "ipsilateral", "type": "SpatialConcept"}, {"text": "bilateral", "type": "SpatialConcept"}, {"text": "LN", "type": "AnatomicalStructure"}, {"text": "metastasis", "type": "BiologicFunction"}]}

Example input:
Sentence: From 1998 to 2011 , we identified 109 , 728 hospitalizations with a CSM diagnosis .

Example answer:
{"entities": [{"text": "hospitalizations", "type": "HealthCareActivity"}, {"text": "CSM", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "HealthCareActivity"}]}

Example input:
Sentence: The intermethod and intergrader agreement for CSME diagnosis and sector count was substantial ( κ range , 0 . 66 [ 95 % CI , 0 . 47 - 0 . 85 ] to 0 . 75 [ 95 % CI , 0 . 53 - 0 . 97 ] ; P < .001 for all ) .

Example answer:
{"entities": [{"text": "CSME", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "HealthCareActivity"}, {"text": "sector", "type": "SpatialConcept"}]}

Example input:
Sentence: The Early Treatment Diabetic Retinopathy Study criteria were used to confirm the presence of CSME by the following 2 methods : stereoscopic fundus photography ( method 1 ) and dilated biomicroscopy in combination with optical coherence tomography ( method 2 ) .

Example answer:
{"entities": [{"text": "Diabetic Retinopathy", "type": "BiologicFunction"}, {"text": "Study", "type": "ResearchActivity"}, {"text": "presence", "type": "Finding"}, {"text": "CSME", "type": "BiologicFunction"}, {"text": "methods", "type": "HealthCareActivity"}, {"text": "stereoscopic fundus photography", "type": "HealthCareActivity"}, {"text": "method 1", "type": "HealthCareActivity"}, {"text": "biomicroscopy", "type": "HealthCareActivity"}, {"text": "optical coherence tomography", "type": "HealthCareActivity"}, {"text": "method 2", "type": "HealthCareActivity"}]}

Example input:
Sentence: Telemedicine screening programs and epidemiological studies rely on monoscopic fundus photography for the detection of clinically significant macular edema ( CSME ) .

Example answer:
{"entities": [{"text": "Telemedicine", "type": "HealthCareActivity"}, {"text": "screening programs", "type": "HealthCareActivity"}, {"text": "epidemiological studies", "type": "ResearchActivity"}, {"text": "monoscopic fundus photography", "type": "HealthCareActivity"}, {"text": "clinically significant macular edema", "type": "BiologicFunction"}, {"text": "CSME", "type": "BiologicFunction"}]}

Input:
Sentence: Twelve eyes ( 5 . 8 % ) were diagnosed as having CSME based on method 1 .

## Item MedMentions:test:1920
Example input:
Sentence: These findings suggest that Apoe - deficient mice showed increased susceptibility to inflammation - associated colorectal carcinogenesis due to their high reactivity to inflammatory stimuli .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "Apoe", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "susceptibility", "type": "ClinicalAttribute"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "colorectal carcinogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study , we evaluated the role of nod - like receptor pyrin domain - containing protein 3 ( NLRP3 ) inflammasome activation in long - term behavioral alterations of 8 - week -old male C57BL / 6 mice injected intraperitoneally with LPS ( 5mg / kg ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "nod - like receptor pyrin domain - containing protein 3 ( NLRP3 ) inflammasome activation", "type": "BiologicFunction"}, {"text": "C57BL / 6 mice", "type": "Eukaryote"}, {"text": "injected", "type": "HealthCareActivity"}, {"text": "intraperitoneally", "type": "SpatialConcept"}, {"text": "LPS", "type": "Chemical"}]}

Example input:
Sentence: Juglone also activated MAPKs signaling by activation of ERK , JNK , and p38 proteins .

Example answer:
{"entities": [{"text": "Juglone", "type": "Chemical"}, {"text": "MAPKs signaling", "type": "BiologicFunction"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "ERK", "type": "Chemical"}, {"text": "JNK", "type": "Chemical"}, {"text": "p38", "type": "Chemical"}, {"text": "proteins", "type": "Chemical"}]}

Example input:
Sentence: pleuropneumoniae exotoxins ( ApxI to IV ) are the major virulence factors contributing to A .

Example answer:
{"entities": [{"text": "pleuropneumoniae", "type": "Bacterium"}, {"text": "exotoxins", "type": "Chemical"}, {"text": "ApxI to IV", "type": "Chemical"}, {"text": "virulence factors", "type": "Chemical"}, {"text": "A .", "type": "Bacterium"}]}

Example input:
Sentence: In contrast to the well - established inhibitory effect of autophagy on the inflammasome activation of APCs , our study demonstrates that isolated autophagosomes ( DRibbles ) from antigen donor cells activate inflammasomes by providing first and second signals required for IL - 1β production by PMBC .

Example answer:
{"entities": [{"text": "inhibitory effect", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "inflammasome activation", "type": "BiologicFunction"}, {"text": "APCs", "type": "AnatomicalStructure"}, {"text": "study", "type": "ResearchActivity"}, {"text": "autophagosomes", "type": "AnatomicalStructure"}, {"text": "DRibbles", "type": "AnatomicalStructure"}, {"text": "antigen", "type": "Chemical"}, {"text": "donor cells", "type": "AnatomicalStructure"}, {"text": "activate inflammasomes", "type": "BiologicFunction"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "PMBC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Notably , the attenuation of JNK activation by a specific inhibitor ( SP600125 ) reduced ApxI -induced NF - κB activation , whereas a p38 blocker ( SB203580 ) had no effect on the NF - κB pathway .

Example answer:
{"entities": [{"text": "JNK", "type": "Chemical"}, {"text": "SP600125", "type": "Chemical"}, {"text": "ApxI", "type": "Chemical"}, {"text": "NF - κB activation", "type": "BiologicFunction"}, {"text": "p38 blocker", "type": "Chemical"}, {"text": "SB203580", "type": "Chemical"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Nonetheless , the role of nuclear factor ( NF ) - κB -a transcription factor widely implicated in immune and inflammatory responses -in ApxI -elicited cytokine production has yet to be defined .

Example answer:
{"entities": [{"text": "nuclear factor ( NF ) - κB", "type": "Chemical"}, {"text": "transcription factor", "type": "Chemical"}, {"text": "immune", "type": "BiologicFunction"}, {"text": "inflammatory responses", "type": "BiologicFunction"}, {"text": "ApxI", "type": "Chemical"}, {"text": "cytokine production", "type": "BiologicFunction"}]}

Example input:
Sentence: The results of Western blot analysis , confocal microscopy , and a DNA binding activity assay revealed that the classical NF - κB pathway was activated by ApxI , as evidenced by the decreased levels of IκB and subsequent NF - κB translocation and activation in ApxI -stimulated PAMs .

Example answer:
{"entities": [{"text": "Western blot analysis", "type": "HealthCareActivity"}, {"text": "confocal microscopy", "type": "HealthCareActivity"}, {"text": "DNA binding", "type": "BiologicFunction"}, {"text": "activity assay", "type": "HealthCareActivity"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "ApxI", "type": "Chemical"}, {"text": "IκB", "type": "Chemical"}, {"text": "translocation", "type": "BiologicFunction"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "PAMs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Collectively , this study , for the first time , demonstrates a pivotal role of NF - κB in ApxI -induced IL - 1β , IL - 8 , and TNF - α production ; JNK , but not p38 , may positively affect the activation of the classical NF - κB pathway .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "ApxI", "type": "Chemical"}, {"text": "IL - 1β", "type": "BiologicFunction"}, {"text": "IL - 8", "type": "BiologicFunction"}, {"text": "TNF - α production", "type": "BiologicFunction"}, {"text": "JNK", "type": "Chemical"}, {"text": "p38", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Moreover , the blocking of ApxI -induced NF - κB activation significantly attenuated the levels of mRNA and protein secretion of IL - 1β , IL - 8 , and TNF - α in PAMs .

Example answer:
{"entities": [{"text": "ApxI", "type": "Chemical"}, {"text": "NF - κB activation", "type": "BiologicFunction"}, {"text": "mRNA", "type": "Chemical"}, {"text": "protein secretion", "type": "BiologicFunction"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "IL - 8", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "PAMs", "type": "AnatomicalStructure"}]}

Input:
Sentence: Previously , we demonstrated that ApxI induces the expression of proinflammatory cytokines in porcine alveolar macrophages ( PAMs ) via the mitogen - activated protein kinases ( MAPKs ) p38 and cJun NH2 - terminal kinase ( JNK ) .

## Item MedMentions:test:2681
Example input:
Sentence: Due to limited statistical power , the dose - risk relationship is undetermined below 0 . 5 Gy ; however , if this relationship proves to be without a threshold , it may have considerable impact on current low ‑ dose health risk estimates .

Example answer:
{"entities": [{"text": "statistical power", "type": "ResearchActivity"}]}

Example input:
Sentence: Patient studies also showed that photon contribution towards the total dose can be relatively high and voxel -level dose calculations can be valuable in cases where the target organ is in close proximity to high - uptake organs .

Example answer:
{"entities": [{"text": "organ", "type": "AnatomicalStructure"}, {"text": "close proximity", "type": "SpatialConcept"}, {"text": "uptake", "type": "BiologicFunction"}, {"text": "organs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Dose interpolation accuracy was high .

Example answer:
{"entities": [{"text": "interpolation", "type": "ResearchActivity"}]}

Example input:
Sentence: Dose - guided positioning is compared to replanning for all cases .

Example answer:
{"entities": [{"text": "Dose - guided positioning", "type": "HealthCareActivity"}]}

Example input:
Sentence: The first 89 patients received standard radiation doses ; their data were reconstructed using AIDR 3D , whereas the last 95 patients received in average 20 % reduction in tube current ; their data were reconstructed using FIRST .

Example answer:
{"entities": [{"text": "AIDR 3D", "type": "IntellectualProduct"}, {"text": "FIRST", "type": "HealthCareActivity"}]}

Example input:
Sentence: The suboptimality of approved dosing regimens supports the development of dosing optimization based on concentration measurements .

Example answer:
{"entities": [{"text": "regimens", "type": "HealthCareActivity"}]}

Example input:
Sentence: Thus , dose -guided patient alignment is an interesting approach to use available in - room imaging data for up - to - date dose calculation , aimed at finding the position that yields the optimal dose distribution .

Example answer:
{"entities": [{"text": "imaging", "type": "HealthCareActivity"}, {"text": "finding", "type": "Finding"}]}

Example input:
Sentence: This contribution presents the first implementation of dose -guided patient alignment as multi - criteria optimization problem .

Example answer:
{"entities": []}

Example input:
Sentence: For all patients , dose - guided positioning allowed to find a clinically preferable dose distribution compared to bony anatomy based alignment .

Example answer:
{"entities": [{"text": "dose - guided positioning", "type": "HealthCareActivity"}]}

Example input:
Sentence: Dose interpolation accuracy is validated and the potential of multi - objective dose - guided positioning demonstrated for three head and neck ( H & N ) and three prostate cancer patients .

Example answer:
{"entities": [{"text": "interpolation", "type": "ResearchActivity"}, {"text": "dose - guided positioning", "type": "HealthCareActivity"}, {"text": "head and neck", "type": "BiologicFunction"}, {"text": "H & N", "type": "BiologicFunction"}, {"text": "prostate cancer", "type": "BiologicFunction"}]}

Input:
Sentence: Using pre - calculated dose distributions at a limited number of patient shifts and dose interpolation , a continuous space of Pareto - efficient patient shifts becomes accessible .

## Item MedMentions:test:2597
Example input:
Sentence: A total of 144 , 098 patients met the study criteria .

Example answer:
{"entities": []}

Example input:
Sentence: A total of 13 studies with 1301 subjects were included for meta - analysis .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "subjects", "type": "PopulationGroup"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: A total of 346 patients were included in the study .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: The study included 275 patients .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Ten studies involving 1402 patients were included : including 3 randomized controlled trials , 5 prospective studies , and 3 retrospective studies .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "randomized controlled trials", "type": "ResearchActivity"}, {"text": "prospective studies", "type": "ResearchActivity"}, {"text": "retrospective studies", "type": "ResearchActivity"}]}

Example input:
Sentence: The analysis included 289 109 patients from 13 observational studies .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "observational studies", "type": "ResearchActivity"}]}

Example input:
Sentence: Eight randomized , controlled trials with a total of 476 subjects were included in the meta - analysis .

Example answer:
{"entities": [{"text": "randomized , controlled trials", "type": "ResearchActivity"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: This retrospective study included a study cohort ( 1 , 219 patients ) and a comparison cohort .

Example answer:
{"entities": [{"text": "retrospective study", "type": "ResearchActivity"}, {"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: A total of 7 , 761 patients from ten clinical trials were included in the meta - analysis .

Example answer:
{"entities": [{"text": "clinical trials", "type": "ResearchActivity"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Twenty - six studies published from 2008 to 2014 , with a total of 52 , 683 cases and 64 , 672 controls , were included in this meta - analysis .

Example answer:
{"entities": [{"text": "studies published", "type": "IntellectualProduct"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Input:
Sentence: To rectify this question , we conducted a systematic meta - analysis based on 7 prospective cohort studies published between 2013 and 2015 , comprising 7349 patients .

## Item MedMentions:test:2521
Example input:
Sentence: 2 % nucleotide sequence identity to G6 genotype ( NCDV strain ) , and for the VP4 gene , strains from the vaccinated herd were 96 .

Example answer:
{"entities": [{"text": "nucleotide sequence", "type": "SpatialConcept"}, {"text": "VP4 gene", "type": "AnatomicalStructure"}, {"text": "vaccinated", "type": "Finding"}]}

Example input:
Sentence: In situ detection of draining LNs revealed preferential localization of CD169 ( + ) CD8 ( + ) T cells to subcapsular sinus and interfollicular regions , closely associated with CD169 ( + ) Mϕ .

Example answer:
{"entities": [{"text": "In situ", "type": "SpatialConcept"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "draining LNs", "type": "AnatomicalStructure"}, {"text": "CD169 ( + ) CD8 ( + ) T cells", "type": "AnatomicalStructure"}, {"text": "subcapsular sinus", "type": "AnatomicalStructure"}, {"text": "interfollicular regions", "type": "SpatialConcept"}, {"text": "CD169 ( + ) Mϕ", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Compared to baseline and control ( SCM ) stimulation , nVNS significantly activated primary vagal projections including : nucleus of the solitary tract ( primary central relay of vagal afferents ) , parabrachial area , primary sensory cortex , and insula .

Example answer:
{"entities": [{"text": "( SCM ) stimulation", "type": "Finding"}, {"text": "nVNS", "type": "HealthCareActivity"}, {"text": "primary vagal", "type": "AnatomicalStructure"}, {"text": "projections", "type": "SpatialConcept"}, {"text": "nucleus of the solitary tract", "type": "AnatomicalStructure"}, {"text": "vagal afferents", "type": "AnatomicalStructure"}, {"text": "parabrachial area", "type": "AnatomicalStructure"}, {"text": "primary sensory cortex", "type": "AnatomicalStructure"}, {"text": "insula", "type": "AnatomicalStructure"}]}

Example input:
Sentence: cIAI , NCT01445665 and NCT01445678 ( both trials registered prospectively on September 26 , 2011 ) ; cUTI , NCT01345929 and NCT01345955 ( both trials registered prospectively on April 28 , 2011 ) .

Example answer:
{"entities": [{"text": "cIAI", "type": "BiologicFunction"}, {"text": "cUTI", "type": "BiologicFunction"}]}

Example input:
Sentence: To this end , we analyzed stool samples from six stage 4 - HCV patients and eight healthy individuals by high - throughput 16S rRNA gene sequencing using Illumina MiSeq .

Example answer:
{"entities": [{"text": "stool samples", "type": "BodySubstance"}, {"text": "HCV", "type": "Virus"}, {"text": "healthy individuals", "type": "PopulationGroup"}, {"text": "16S rRNA gene sequencing", "type": "HealthCareActivity"}, {"text": "Illumina MiSeq", "type": "MedicalDevice"}]}

Example input:
Sentence: Comparing trisomic placentas to normal placentas we identified 217 and 219 differentially methylated CpGs for CVS T18 and CVS T13 , respectively ( delta β > 0 .

Example answer:
{"entities": [{"text": "trisomic placentas", "type": "AnatomicalStructure"}, {"text": "placentas", "type": "AnatomicalStructure"}, {"text": "methylated", "type": "BiologicFunction"}, {"text": "CpGs", "type": "Chemical"}, {"text": "CVS", "type": "HealthCareActivity"}, {"text": "T18", "type": "BiologicFunction"}, {"text": "T13", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study , we aimed to determine whether copy number variations ( CNVs ) in FCGR3A and FCGR3B were associated with systemic lupus nephritis ( SLE ) and ANCA - associated systemic vasculitis ( AASV ) in Chinese individuals .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "copy number variations", "type": "BiologicFunction"}, {"text": "CNVs", "type": "BiologicFunction"}, {"text": "FCGR3A", "type": "AnatomicalStructure"}, {"text": "FCGR3B", "type": "AnatomicalStructure"}, {"text": "systemic lupus nephritis", "type": "BiologicFunction"}, {"text": "SLE", "type": "BiologicFunction"}, {"text": "ANCA - associated systemic vasculitis", "type": "BiologicFunction"}, {"text": "AASV", "type": "BiologicFunction"}, {"text": "Chinese individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: FCGR3A and FCGR3B copy numbers ( CNs ) were determined by both a paralogue ratio test and TaqMan quantitative PCR assay .

Example answer:
{"entities": [{"text": "FCGR3A", "type": "AnatomicalStructure"}, {"text": "FCGR3B", "type": "AnatomicalStructure"}, {"text": "paralogue ratio test", "type": "HealthCareActivity"}, {"text": "TaqMan quantitative PCR assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: Subsequently , the MLPA P343 was used to identify alterations in the 15q11q13 , 16p11 .

Example answer:
{"entities": [{"text": "MLPA P343", "type": "ResearchActivity"}, {"text": "15q11q13", "type": "AnatomicalStructure"}, {"text": "16p11 .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Screening with MLPA P343 allowed a 10 - 15 . 7 % increase in the detection rate of CNVs reinforcing the importance of investigating changes in 15q11q13 and 16p11 .

Example answer:
{"entities": [{"text": "Screening", "type": "HealthCareActivity"}, {"text": "MLPA P343", "type": "ResearchActivity"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "CNVs", "type": "BiologicFunction"}, {"text": "15q11q13", "type": "AnatomicalStructure"}, {"text": "16p11 .", "type": "AnatomicalStructure"}]}

Input:
Sentence: Identifying CNVs in 15q11q13 and 16p11 .

## Item MedMentions:test:2486
Example input:
Sentence: Indomethacin ( 10μM ) and NS398 ( 1μM ) decreased the contractile response in diabetic rats and atorvastatin reversed these effects , without changing COX - 2 expression .

Example answer:
{"entities": [{"text": "Indomethacin", "type": "Chemical"}, {"text": "NS398", "type": "Chemical"}, {"text": "contractile", "type": "AnatomicalStructure"}, {"text": "diabetic", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}, {"text": "atorvastatin", "type": "Chemical"}, {"text": "COX - 2", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}]}

Example input:
Sentence: Design , synthesis , molecular docking , anti - Proteus mirabilis and urease inhibition of new fluoroquinolone carboxylic acid derivatives New hydroxamic acid , hydrazide and amide derivatives of ciprofloxacin in addition to their analogues of levofloxacin were prepared and identified by different spectroscopic techniques .

Example answer:
{"entities": [{"text": "molecular docking", "type": "IntellectualProduct"}, {"text": "anti - Proteus mirabilis", "type": "Chemical"}, {"text": "urease", "type": "Chemical"}, {"text": "inhibition", "type": "BiologicFunction"}, {"text": "fluoroquinolone carboxylic acid derivatives", "type": "Chemical"}, {"text": "hydroxamic acid", "type": "Chemical"}, {"text": "hydrazide", "type": "Chemical"}, {"text": "amide derivatives", "type": "Chemical"}, {"text": "ciprofloxacin", "type": "Chemical"}, {"text": "analogues", "type": "Chemical"}, {"text": "levofloxacin", "type": "Chemical"}]}

Example input:
Sentence: Antioxidant activities were determined by total phenolic contents , 1 , 1 - diphenyl - 2 - picrylhydrazyl ( DPPH ) free radical scavenging and inhibition of lipid peroxidation .

Example answer:
{"entities": [{"text": "Antioxidant activities", "type": "BiologicFunction"}, {"text": "phenolic", "type": "Chemical"}, {"text": "1 , 1 - diphenyl - 2 - picrylhydrazyl ( DPPH ) free radical", "type": "Chemical"}, {"text": "lipid", "type": "Chemical"}]}

Example input:
Sentence: In the present study we assessed in non - human primates ( NHPs ) the effects of a novel PDE10A inhibitor ( FRM - 6308 ) that has demonstrated high potency and selectivity for human recombinant PDE10A in vitro .

Example answer:
{"entities": [{"text": "non - human primates", "type": "Eukaryote"}, {"text": "NHPs", "type": "Eukaryote"}, {"text": "PDE10A inhibitor", "type": "Chemical"}, {"text": "FRM - 6308", "type": "Chemical"}, {"text": "human recombinant PDE10A", "type": "Chemical"}]}

Example input:
Sentence: The transgenic plants showed up to 80 % inhibition in both hot plate analgesic assay and carrageenan - induced hind paw edema test , while untransformed plants showed only 45 % inhibition .

Example answer:
{"entities": [{"text": "transgenic plants", "type": "Eukaryote"}, {"text": "hot plate analgesic assay", "type": "HealthCareActivity"}, {"text": "carrageenan", "type": "Chemical"}, {"text": "hind paw edema test", "type": "HealthCareActivity"}, {"text": "untransformed plants", "type": "Eukaryote"}]}

Example input:
Sentence: Total phenols , flavonoids , tannins and antioxidant activity were evaluated using the Folin ciocalteux , Aluminum trichloride , vanillin and scavenging activity on 22 - diphenyl - 1 - picrylhydrazyl ( DPPH ) radical methods , respectively .

Example answer:
{"entities": [{"text": "phenols", "type": "Chemical"}, {"text": "flavonoids", "type": "Chemical"}, {"text": "tannins", "type": "Chemical"}, {"text": "antioxidant activity", "type": "BiologicFunction"}, {"text": "Folin ciocalteux", "type": "Chemical"}, {"text": "Aluminum trichloride", "type": "Chemical"}, {"text": "vanillin", "type": "Chemical"}, {"text": "scavenging activity", "type": "BiologicFunction"}, {"text": "22 - diphenyl - 1 - picrylhydrazyl", "type": "Chemical"}, {"text": "DPPH", "type": "Chemical"}, {"text": "radical", "type": "Chemical"}]}

Example input:
Sentence: The inhibitor of prostaglandin biosynthesis , indomethacin , and antagonists of histamine , serotonin and NK1 receptors were injected s .

Example answer:
{"entities": [{"text": "inhibitor", "type": "Chemical"}, {"text": "prostaglandin biosynthesis", "type": "BiologicFunction"}, {"text": "indomethacin", "type": "Chemical"}, {"text": "antagonists of histamine", "type": "Chemical"}, {"text": "serotonin", "type": "Chemical"}, {"text": "NK1 receptors", "type": "BiologicFunction"}]}

Example input:
Sentence: The removal of cyanide , a strong inhibitor of tyrosinase , enabled an effective degradation of phenols by this enzyme in the second step .

Example answer:
{"entities": [{"text": "cyanide", "type": "Chemical"}, {"text": "tyrosinase", "type": "Chemical"}, {"text": "phenols", "type": "Chemical"}, {"text": "enzyme", "type": "Chemical"}]}

Example input:
Sentence: Histamine and serotonin antagonists and indomethacin , but not the NK1 antagonist , decreased cheek oedema in the first 4 h following carrageenan .

Example answer:
{"entities": [{"text": "Histamine", "type": "Chemical"}, {"text": "serotonin antagonists", "type": "Chemical"}, {"text": "indomethacin", "type": "Chemical"}, {"text": "NK1 antagonist", "type": "BiologicFunction"}, {"text": "cheek", "type": "SpatialConcept"}, {"text": "oedema", "type": "Finding"}, {"text": "carrageenan", "type": "Chemical"}]}

Example input:
Sentence: 2 , 7 , 8 , 11 , 14 , and 22 , in order to rationalize the binding interaction of compounds with the active site of urease enzyme .

Example answer:
{"entities": [{"text": "2", "type": "Chemical"}, {"text": "7", "type": "Chemical"}, {"text": "8", "type": "Chemical"}, {"text": "11", "type": "Chemical"}, {"text": "14", "type": "Chemical"}, {"text": "22", "type": "Chemical"}, {"text": "binding interaction", "type": "BiologicFunction"}, {"text": "compounds", "type": "Chemical"}, {"text": "urease enzyme", "type": "Chemical"}]}

Input:
Sentence: The urease inhibitory activity was investigated using indophenol method .

## Item MedMentions:test:2296
Example input:
Sentence: 70 diabetic patients who underwent elective CABG and whose hematocrit values had been between 24 - 28 % at any time during CBP were prospectively randomized and equally allocated to two groups : patients who received RBC during CPB ( group I , n = 35 ) vs . did not receive RBC during CPB ( group II , n = 35 ) .

Example answer:
{"entities": [{"text": "diabetic", "type": "BiologicFunction"}, {"text": "CABG", "type": "HealthCareActivity"}, {"text": "hematocrit values", "type": "Finding"}, {"text": "CBP", "type": "HealthCareActivity"}, {"text": "RBC", "type": "AnatomicalStructure"}, {"text": "CPB", "type": "HealthCareActivity"}]}

Example input:
Sentence: Statistical analysis of metabolic failure has recognized a high preoperative HbA1c % value as a statistically significant negative predictive factor .

Example answer:
{"entities": [{"text": "HbA1c", "type": "Chemical"}, {"text": "negative", "type": "Finding"}, {"text": "predictive factor", "type": "IntellectualProduct"}]}

Example input:
Sentence: As compared with subjects with 1 - hour post - load glucose < 155 mg / dl , individuals with 1 - hour post - load glucose ≥155 mg / dl exhibited a significantly worse cardio metabolic profile , both in the group with HbA1c < 5 . 7 % , and in the group with prediabetes ( HbA1c 5 . 7 - 6 . 4 % ) .

Example answer:
{"entities": [{"text": "individuals", "type": "PopulationGroup"}, {"text": "cardio metabolic profile", "type": "BiologicFunction"}, {"text": "group", "type": "PopulationGroup"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "prediabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Participants who developed incident type 2 diabetes were significantly older and had significantly higher body mass index ( BMI ; p = 0 . 012 ) , total cholesterol ( p = 0 . 007 ) , fasting triglycerides ( p < 0 . 001 ) , and Homeostatic Model Assessment of Insulin Resistance ( HOMA - IR ) ( p < 0 .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "type 2 diabetes", "type": "Finding"}, {"text": "significantly older", "type": "PopulationGroup"}, {"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "fasting", "type": "Finding"}, {"text": "triglycerides", "type": "Chemical"}, {"text": "Homeostatic Model Assessment of Insulin Resistance", "type": "HealthCareActivity"}, {"text": "HOMA - IR", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , in our study , surgery did not achieve the expected outcome in patients with specific metabolic , anthropometric and surgical characteristics ( BMI > 50 Kg / m2 , presence of metabolic syndrome , presence of T2DM with high preoperative HbA1c % level and gastric pouch volume greater than 60 ml ) .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "expected", "type": "IntellectualProduct"}, {"text": "surgical", "type": "HealthCareActivity"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "metabolic syndrome", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "gastric pouch", "type": "AnatomicalStructure"}]}

Example input:
Sentence: There were no full remissions after surgery in patients with preoperative diabetes .

Example answer:
{"entities": [{"text": "remissions", "type": "Finding"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: In group I , T - SH , NGAL and urea levels were found to be significantly increased postoperatively compared to preoperative measurements ( p < 0 .

Example answer:
{"entities": [{"text": "T - SH", "type": "Chemical"}, {"text": "NGAL", "type": "Chemical"}, {"text": "urea levels", "type": "Finding"}]}

Example input:
Sentence: Herein , we evaluated whether 1 - hour post - load plasma glucose ≥155 mg / dl combined with HbA1c may identify pre - diabetic individuals with a higher cardio - metabolic risk .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: Of the 6323 subjects scheduled for assessment of diabetes state 617 were diabetics and 712 were pre - diabetic .

Example answer:
{"entities": [{"text": "assessment", "type": "HealthCareActivity"}, {"text": "diabetes state", "type": "BiologicFunction"}, {"text": "diabetics", "type": "Finding"}, {"text": "pre - diabetic", "type": "Finding"}]}

Example input:
Sentence: Preoperative abnormalities in glucose homeostasis were confirmed in 64 ( 47 % ) patients .

Example answer:
{"entities": [{"text": "abnormalities", "type": "Finding"}, {"text": "glucose homeostasis", "type": "BiologicFunction"}]}

Input:
Sentence: Patients were assessed preoperatively and allocated to two groups : group 1 -with any preoperative abnormalities in glucose homeostasis ( prediabetes , diabetes ) and group 2 -with non - elevated fasting glucose level .

## Item MedMentions:test:2633
Example input:
Sentence: 60 h , respectively , P = 0 . 016 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 2 % in the RM and control group , respectively ( p = 0 . 01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 2 m ( p = 0 . 0001 ) , in the treatment group , whereas the mean value was unchanged in the control group ( p = 0 . 218 ) .

Example answer:
{"entities": [{"text": "treatment group", "type": "PopulationGroup"}]}

Example input:
Sentence: 2 % ropivacaine ( 3 ml h through each catheter ; ' intervention ' group ) , or standardised care only ( ' control ' group ) .

Example answer:
{"entities": [{"text": "ropivacaine", "type": "Chemical"}, {"text": "catheter", "type": "MedicalDevice"}, {"text": "' intervention ' group", "type": "PopulationGroup"}]}

Example input:
Sentence: There was a significant difference in N / L and P / L between idiopathic AAU and control groups ( P = 0 . 006 , P = 0 . 022 ) .

Example answer:
{"entities": [{"text": "N", "type": "AnatomicalStructure"}, {"text": "L", "type": "AnatomicalStructure"}, {"text": "P", "type": "AnatomicalStructure"}, {"text": "AAU", "type": "BiologicFunction"}]}

Example input:
Sentence: 47 . 55 ± 10 . 34 h , respectively , P = 0 . 039 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 12 . 5 % , p - value 1 . 00 ) between the treatment group and control group , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: Patients were defined as either control group ( 533 patients , 12 months ) or intervention group ( 804 patients , 18 months ) .

Example answer:
{"entities": [{"text": "intervention group", "type": "PopulationGroup"}]}

Example input:
Sentence: 2 h in the healthy controls and STC patients , respectively ( P < . 05 ) .

Example answer:
{"entities": [{"text": "STC", "type": "Finding"}]}

Example input:
Sentence: 3±6 . 5 h in the healthy controls and STC patients , respectively ( P < . 05 ) .

Example answer:
{"entities": [{"text": "STC", "type": "Finding"}]}

Input:
Sentence: 7 h , respectively for the control and intervention groups ( P = 0 . 873 ) .

## Item MedMentions:test:2455
Example input:
Sentence: Plasma sLR11 levels were determined in 64 individuals with T2D and BMI > 27 kg / m ( 2 ) before and after a 20 - week weight loss diet .

Example answer:
{"entities": [{"text": "Plasma", "type": "BodySubstance"}, {"text": "sLR11", "type": "Chemical"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "T2D", "type": "BiologicFunction"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "weight loss diet", "type": "HealthCareActivity"}]}

Example input:
Sentence: The purpose of this study was to test for an association between fasting serum triglycerides and incident diabetes , changes in insulin resistance and changes in β - cell function in a Manitoba First Nation cohort .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "fasting", "type": "Finding"}, {"text": "serum", "type": "BodySubstance"}, {"text": "triglycerides", "type": "Chemical"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "β - cell function", "type": "BiologicFunction"}, {"text": "Manitoba", "type": "SpatialConcept"}, {"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: At week 48 , eGFR was higher in the switch arm ( median 96 mL / min ) than in the control arm ( median 85 mL / min ) ( p = 0 . 035 ) , but the arms were similar with respect to fasting glucose , C - reactive protein , and lipid parameters .

Example answer:
{"entities": [{"text": "eGFR", "type": "HealthCareActivity"}, {"text": "median", "type": "SpatialConcept"}, {"text": "fasting glucose", "type": "HealthCareActivity"}, {"text": "C - reactive protein", "type": "Chemical"}, {"text": "lipid", "type": "Chemical"}]}

Example input:
Sentence: Long - chain n - 3 PUFA supplied by the usual diet decrease plasma stearoyl - CoA desaturase index in non - hypertriglyceridemic older adults at high vascular risk The activity of stearoyl - CoA desaturase - 1 ( SCD1 ) , the central enzyme in the synthesis of monounsaturated fatty acids ( MUFA ) , has been associated with de novo lipogenesis .

Example answer:
{"entities": [{"text": "Long - chain n - 3 PUFA", "type": "Chemical"}, {"text": "diet", "type": "Food"}, {"text": "plasma stearoyl - CoA desaturase", "type": "Chemical"}, {"text": "index", "type": "IntellectualProduct"}, {"text": "non - hypertriglyceridemic", "type": "Finding"}, {"text": "older adults", "type": "PopulationGroup"}, {"text": "vascular", "type": "AnatomicalStructure"}, {"text": "activity", "type": "BiologicFunction"}, {"text": "stearoyl - CoA desaturase - 1", "type": "Chemical"}, {"text": "SCD1", "type": "Chemical"}, {"text": "central enzyme", "type": "Chemical"}, {"text": "monounsaturated fatty acids", "type": "Chemical"}, {"text": "MUFA", "type": "Chemical"}, {"text": "lipogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Confounders were adjusted with fixed effects for age , gender , BMI , diabetes , CIRS musculoskeletal disorders and duration of symptoms .

Example answer:
{"entities": [{"text": "BMI", "type": "ClinicalAttribute"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "musculoskeletal disorders", "type": "BiologicFunction"}, {"text": "duration", "type": "Chemical"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: After multivariable adjustments including baseline eGFR , 1 mg / dL increase in baseline SUA was associated with greater odds of developing rapid eGFR decline ( OR 1 . 27 , 95 % CI 1 . 17 - 1 . 38 ) , and 1 mg / dL increase in SUA over 5 years was associated with 3 . 77 - fold greater odds of rapid eGFR decline ( OR 3 . 77 , 95 % CI 3 . 35 - 4 . 26 ) .

Example answer:
{"entities": [{"text": "eGFR", "type": "HealthCareActivity"}, {"text": "SUA", "type": "Chemical"}]}

Example input:
Sentence: Participants who developed incident type 2 diabetes were significantly older and had significantly higher body mass index ( BMI ; p = 0 . 012 ) , total cholesterol ( p = 0 . 007 ) , fasting triglycerides ( p < 0 . 001 ) , and Homeostatic Model Assessment of Insulin Resistance ( HOMA - IR ) ( p < 0 .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "type 2 diabetes", "type": "Finding"}, {"text": "significantly older", "type": "PopulationGroup"}, {"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "fasting", "type": "Finding"}, {"text": "triglycerides", "type": "Chemical"}, {"text": "Homeostatic Model Assessment of Insulin Resistance", "type": "HealthCareActivity"}, {"text": "HOMA - IR", "type": "HealthCareActivity"}]}

Example input:
Sentence: Additionally , dietary LCn - 3PUFA ( but not MUFA or plant - derived PUFA ) were associated with decreased plasma SCD1 index ( -0 . 544 [ -1 . 044 to -0 . 043 ] , P = 0 .

Example answer:
{"entities": [{"text": "dietary", "type": "Food"}, {"text": "LCn - 3PUFA", "type": "Chemical"}, {"text": "MUFA", "type": "Chemical"}, {"text": "plant - derived PUFA", "type": "Chemical"}, {"text": "plasma SCD1", "type": "Chemical"}, {"text": "index", "type": "IntellectualProduct"}]}

Example input:
Sentence: Our data add clinical evidence on the down - regulation of plasma SCD1 index by LCn - 3PUFA in the context of realistic changes in fish consumption in the customary , non - supplemented diet .

Example answer:
{"entities": [{"text": "down - regulation", "type": "BiologicFunction"}, {"text": "plasma SCD1", "type": "Chemical"}, {"text": "index", "type": "IntellectualProduct"}, {"text": "LCn - 3PUFA", "type": "Chemical"}, {"text": "fish", "type": "Eukaryote"}, {"text": "non - supplemented", "type": "Finding"}, {"text": "diet", "type": "Food"}]}

Example input:
Sentence: We related 1 - y changes in plasma SCD1 index , as assessed by the C16 : 1n - 7 / C16 : 0 ratio , to both adiposity traits and nutrient intake changes in a sub - cohort ( n = 243 ) of non - hypertriglyceridemic subjects of the PREDIMED ( PREvención con DIeta MEDiterranea ) trial .

Example answer:
{"entities": [{"text": "plasma SCD1", "type": "Chemical"}, {"text": "index", "type": "IntellectualProduct"}, {"text": "C16 : 1n - 7", "type": "Chemical"}, {"text": "C16 : 0", "type": "Chemical"}, {"text": "nutrient intake", "type": "Finding"}, {"text": "sub - cohort", "type": "PopulationGroup"}, {"text": "non - hypertriglyceridemic", "type": "Finding"}, {"text": "subjects", "type": "PopulationGroup"}, {"text": "PREDIMED ( PREvención con DIeta MEDiterranea ) trial", "type": "ResearchActivity"}]}

Input:
Sentence: After adjustment for confounders , including changes in fasting triglycerides , plasma SCD1 index increased in parallel with body weight ( 0 . 221 [ 95 % confidence interval , 0 . 021 to 0 . 422 ] , P = 0 .

## Item MedMentions:test:2427
Example input:
Sentence: The utilization of calcium channel blockers and angiotensin - converting enzyme inhibitors across the study period increased in all age categories .

Example answer:
{"entities": [{"text": "calcium channel blockers", "type": "Chemical"}, {"text": "angiotensin - converting enzyme inhibitors", "type": "Chemical"}]}

Example input:
Sentence: Antihypertensive medicines utilization : A decade - long nationwide study of octogenarians , nonagenarians and centenarians Gaining an insight into the utilization of antihypertensive medicines against a background of evolving hypertension treatment guidelines that might not be relevant to the oldest old is important .

Example answer:
{"entities": [{"text": "Antihypertensive medicines", "type": "Chemical"}, {"text": "antihypertensive medicines", "type": "Chemical"}, {"text": "hypertension treatment", "type": "HealthCareActivity"}, {"text": "guidelines", "type": "IntellectualProduct"}]}

Example input:
Sentence: In this prospective , double - blind study , patients in Japan , Korea , and Taiwan were randomized ( 1 : 1 : 1 ) to asenapine 5 mg twice daily ( bid ) , 10 mg bid or placebo for 6 weeks after a 3 - to 7 - day washout / screening period .

Example answer:
{"entities": [{"text": "double - blind study", "type": "ResearchActivity"}, {"text": "Japan", "type": "SpatialConcept"}, {"text": "Korea", "type": "SpatialConcept"}, {"text": "Taiwan", "type": "SpatialConcept"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "asenapine", "type": "Chemical"}, {"text": "placebo", "type": "ResearchActivity"}]}

Example input:
Sentence: A Segal report projects an 11 . 6 % rise in prescription drug spending for employees and early retirees in 2017 , up slightly from 11 . 3 % in 2016 , but that 's probably the result of drug companies highballing estimates .

Example answer:
{"entities": [{"text": "Segal", "type": "Organization"}, {"text": "report", "type": "IntellectualProduct"}, {"text": "prescription drug", "type": "Chemical"}, {"text": "employees", "type": "ProfessionalOrOccupationalGroup"}, {"text": "early retirees", "type": "Finding"}, {"text": "drug companies", "type": "Organization"}]}

Example input:
Sentence: The slightly better efficacy observed in Japanese patients was driven by the absence of placebo effect and might be explained by their earlier stage of diabetes compared to other subgroups .

Example answer:
{"entities": [{"text": "Japanese", "type": "PopulationGroup"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "subgroups", "type": "PopulationGroup"}]}

Example input:
Sentence: The aim of the present study was to characterize the overall trends in the utilization of antihypertensive medicines in the oldest old by therapeutic class and chemical type , stratified by age and sex over a decade .

Example answer:
{"entities": [{"text": "antihypertensive medicines", "type": "Chemical"}]}

Example input:
Sentence: They were grouped on the basis of the year of their initial medications for AD administration into the 2010 - 2011 and 2012 - 2014 groups ( 1 and 2 , respectively ) and their characteristics and AD treatments were summarized by group .

Example answer:
{"entities": [{"text": "grouped", "type": "SpatialConcept"}, {"text": "medications", "type": "HealthCareActivity"}, {"text": "AD", "type": "BiologicFunction"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "treatments", "type": "HealthCareActivity"}]}

Example input:
Sentence: Japanese patients were drug - naïve and treated with a single oral anti - diabetes drug only ; they showed no response to placebo .

Example answer:
{"entities": [{"text": "Japanese", "type": "PopulationGroup"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "oral", "type": "SpatialConcept"}, {"text": "anti - diabetes drug", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: This descriptive study of pharmacy claims databases analyzed outpatient prescription data from community pharmacies across Japan .

Example answer:
{"entities": [{"text": "descriptive", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "pharmacy", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "databases", "type": "IntellectualProduct"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "prescription data", "type": "IntellectualProduct"}, {"text": "community pharmacies", "type": "Organization"}, {"text": "Japan", "type": "SpatialConcept"}]}

Example input:
Sentence: Although the prescription proportions of the various medications for AD have changed since 2011 , no apparent changes occurred in the patient characteristics of those who initiated AD treatment between 2010 - 2011 and 2012 - 2014 .

Example answer:
{"entities": [{"text": "prescription", "type": "IntellectualProduct"}, {"text": "medications", "type": "HealthCareActivity"}, {"text": "AD", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Input:
Sentence: This study aimed to elucidate prescription trends of these medications for AD in Japanese outpatients before and after the new drug releases in 2011 .

## Item MedMentions:test:2230
Example input:
Sentence: These findings reinforce the need for strict morphological and clinical criteria , other than EBV - positivity , when diagnosing PTLD in the paediatric population .

Example answer:
{"entities": [{"text": "morphological", "type": "SpatialConcept"}, {"text": "EBV", "type": "Virus"}, {"text": "positivity", "type": "Finding"}, {"text": "diagnosing", "type": "Finding"}, {"text": "PTLD", "type": "BiologicFunction"}, {"text": "paediatric population", "type": "PopulationGroup"}]}

Example input:
Sentence: Sections of formalin fixed paraffin - embedded tumor tissue from 54 cases of Morbus Bowen ( preinvasive cutaneous carcinoma ) and 41 cases of invasive squamous cell carcinoma of the skin were subjected to HPV genotyping using Lipa ( Line imuno probe assay ) , immunohistochemical staining for p16 ( INK4A ) , p53 , pRb and prepared for flow cytometry DNA content analysis .

Example answer:
{"entities": [{"text": "formalin fixed paraffin - embedded tumor tissue", "type": "AnatomicalStructure"}, {"text": "Morbus Bowen", "type": "BiologicFunction"}, {"text": "preinvasive cutaneous carcinoma", "type": "BiologicFunction"}, {"text": "squamous cell carcinoma", "type": "BiologicFunction"}, {"text": "skin", "type": "BodySystem"}, {"text": "Lipa", "type": "HealthCareActivity"}, {"text": "Line imuno probe assay", "type": "HealthCareActivity"}, {"text": "staining", "type": "HealthCareActivity"}, {"text": "p16 ( INK4A )", "type": "Chemical"}, {"text": "p53", "type": "Chemical"}, {"text": "pRb", "type": "Chemical"}, {"text": "prepared", "type": "Finding"}, {"text": "flow cytometry DNA content analysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: He subsequently underwent endobronchial ultrasound with transbronchial needle aspiration ( EBUS - TBNA ) .

Example answer:
{"entities": [{"text": "endobronchial ultrasound with transbronchial needle aspiration", "type": "HealthCareActivity"}, {"text": "EBUS - TBNA", "type": "HealthCareActivity"}]}

Example input:
Sentence: B - cell markers CD20 and PAX5 were not expressed ; c - Myc IHC and EBER by in situ hybridization ( ISH ) were negative in the tumor .

Example answer:
{"entities": [{"text": "B - cell markers", "type": "Chemical"}, {"text": "CD20", "type": "Chemical"}, {"text": "PAX5", "type": "Chemical"}, {"text": "c - Myc", "type": "AnatomicalStructure"}, {"text": "IHC", "type": "HealthCareActivity"}, {"text": "EBER", "type": "Chemical"}, {"text": "in situ hybridization", "type": "ResearchActivity"}, {"text": "ISH", "type": "ResearchActivity"}, {"text": "negative", "type": "Finding"}, {"text": "tumor", "type": "BiologicFunction"}]}

Example input:
Sentence: Array comparative genomic hybridization and metaphase fluorescence in situ hybridization analyses were performed on the peripheral blood to determine the origin and mosaicism of the sSMC , and quantitative fluorescent polymerase chain reaction was used to exclude uniparental disomy .

Example answer:
{"entities": [{"text": "Array comparative genomic hybridization", "type": "ResearchActivity"}, {"text": "metaphase fluorescence in situ hybridization analyses", "type": "ResearchActivity"}, {"text": "peripheral blood", "type": "BodySubstance"}, {"text": "sSMC", "type": "AnatomicalStructure"}, {"text": "quantitative fluorescent polymerase chain reaction", "type": "HealthCareActivity"}, {"text": "uniparental disomy", "type": "BiologicFunction"}]}

Example input:
Sentence: Thirty - two out of 72 ELBW infants underwent conventional MR imaging and DTI at term - equivalent age .

Example answer:
{"entities": [{"text": "ELBW infants", "type": "Finding"}, {"text": "MR imaging", "type": "HealthCareActivity"}, {"text": "DTI", "type": "HealthCareActivity"}]}

Example input:
Sentence: EBV was positive in 26 / 102 tonsils ( 25 % ) .

Example answer:
{"entities": [{"text": "EBV", "type": "Virus"}, {"text": "positive", "type": "Finding"}, {"text": "tonsils", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Immunostaining for HOXB13 , PTEN , ERG , p53 and SPINK1 as well as RNA in situ hybridization for ETV1 / 4 / 5 were performed using genetically validated assays .

Example answer:
{"entities": [{"text": "Immunostaining", "type": "HealthCareActivity"}, {"text": "HOXB13", "type": "Chemical"}, {"text": "PTEN", "type": "Chemical"}, {"text": "ERG", "type": "Chemical"}, {"text": "p53", "type": "Chemical"}, {"text": "SPINK1", "type": "Chemical"}, {"text": "RNA", "type": "Chemical"}, {"text": "in situ hybridization", "type": "ResearchActivity"}, {"text": "ETV1", "type": "AnatomicalStructure"}, {"text": "4", "type": "AnatomicalStructure"}, {"text": "5", "type": "AnatomicalStructure"}, {"text": "genetically validated assays", "type": "HealthCareActivity"}]}

Example input:
Sentence: Among tonsils from OTR , 4 / 6 ( 67 % ) were EBV - positive .

Example answer:
{"entities": [{"text": "tonsils", "type": "AnatomicalStructure"}, {"text": "EBV", "type": "Virus"}, {"text": "positive", "type": "Finding"}]}

Example input:
Sentence: Incidental EBV - positivity in paediatric post - transplant specimens demonstrates the need for stringent criteria for diagnosing post - transplant lymphoproliferative disorders To examine the need for minimal diagnostic criteria for post - transplant lymphoproliferative disorders ( PTLD ) in children , we sought to determine the rate of incidental Epstein - Barr virus ( EBV ) - positivity in tissues from organ transplant recipients ( OTR ) .

Example answer:
{"entities": [{"text": "EBV", "type": "Virus"}, {"text": "positivity", "type": "Finding"}, {"text": "diagnosing", "type": "Finding"}, {"text": "post - transplant lymphoproliferative disorders", "type": "BiologicFunction"}, {"text": "PTLD", "type": "BiologicFunction"}, {"text": "Epstein - Barr virus", "type": "Virus"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "organ", "type": "AnatomicalStructure"}]}

Input:
Sentence: EBV in situ hybridisation ( ISH ) was done retrospectively on tissue from 34 paediatric autopsies of OTR and paediatric tonsillectomy specimens from non - OTR ( 96 ) and OTR ( 6 ) .

## Item MedMentions:test:2224
Example input:
Sentence: The most common intraoperative complication was hemorrhage , with a frequency of 3 % .

Example answer:
{"entities": [{"text": "intraoperative complication", "type": "BiologicFunction"}, {"text": "hemorrhage", "type": "BiologicFunction"}]}

Example input:
Sentence: There were seven ( 8 . 75 % ) grade 2 complications and one ( 1 . 25 % ) grade 3 complication ( aspiration pneumonia ) .

Example answer:
{"entities": [{"text": "grade 2 complications", "type": "BiologicFunction"}, {"text": "grade 3 complication", "type": "BiologicFunction"}, {"text": "aspiration pneumonia", "type": "BiologicFunction"}]}

Example input:
Sentence: Complications included misdirected infusion that facilitated the transport of retained nuclear fragments to the vitreous , inconsistent lens followability during phacoemulsification , and exaggerated movements of the iris particularly consistent with intraoperative floppy - iris syndrome and pseudoexfoliation .

Example answer:
{"entities": [{"text": "Complications", "type": "BiologicFunction"}, {"text": "infusion", "type": "HealthCareActivity"}, {"text": "vitreous", "type": "Finding"}, {"text": "lens", "type": "AnatomicalStructure"}, {"text": "phacoemulsification", "type": "HealthCareActivity"}, {"text": "iris", "type": "AnatomicalStructure"}, {"text": "intraoperative floppy - iris syndrome", "type": "BiologicFunction"}, {"text": "pseudoexfoliation", "type": "BiologicFunction"}]}

Example input:
Sentence: intraoperative complications including anterior and posterior capsule tears .

Example answer:
{"entities": [{"text": "intraoperative complications", "type": "BiologicFunction"}, {"text": "anterior", "type": "InjuryOrPoisoning"}, {"text": "posterior capsule tears", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: In the 3 gastrostomy cases , there were no direct complications due to the gastrostomy or tube feeding , nor were there episodes of discontinuation of tube feeding or initiation of continuous drip infusion due to severe complications .

Example answer:
{"entities": [{"text": "gastrostomy", "type": "HealthCareActivity"}, {"text": "no direct complications", "type": "Finding"}, {"text": "tube feeding", "type": "HealthCareActivity"}, {"text": "discontinuation", "type": "HealthCareActivity"}, {"text": "initiation of continuous drip infusion", "type": "HealthCareActivity"}, {"text": "severe complications", "type": "Finding"}]}

Example input:
Sentence: The most serious intraoperative complication was a posterior capsule rupture and vitreous loss ( 2 patients , 2 eyes ) .

Example answer:
{"entities": [{"text": "intraoperative complication", "type": "BiologicFunction"}, {"text": "posterior capsule rupture", "type": "InjuryOrPoisoning"}, {"text": "vitreous loss", "type": "BiologicFunction"}, {"text": "eyes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Among all 25 patients , 4 suffered from complications including instrument s failure , cerebrospinal fluid leakage , and intracranial infection .

Example answer:
{"entities": [{"text": "complications", "type": "BiologicFunction"}, {"text": "instrument", "type": "MedicalDevice"}, {"text": "failure", "type": "Finding"}, {"text": "cerebrospinal fluid leakage", "type": "BiologicFunction"}, {"text": "intracranial", "type": "SpatialConcept"}, {"text": "infection", "type": "BiologicFunction"}]}

Example input:
Sentence: Hemorrhagic complications developed in 15 , renal complications in 13 , pulmonary complications in 12 , infectious complications in 11 , neurologic complications in three and mechanical complications in two of the patients .

Example answer:
{"entities": [{"text": "complications", "type": "BiologicFunction"}, {"text": "pulmonary complications", "type": "BiologicFunction"}, {"text": "infectious", "type": "BiologicFunction"}, {"text": "neurologic complications", "type": "BiologicFunction"}, {"text": "mechanical complications", "type": "BiologicFunction"}]}

Example input:
Sentence: Complications included wound infection requiring surgical management , compartment syndrome requiring fasciotomies , nonunion , early fixation failure , and implant removal for discomfort .

Example answer:
{"entities": [{"text": "Complications", "type": "BiologicFunction"}, {"text": "wound infection", "type": "BiologicFunction"}, {"text": "surgical management", "type": "HealthCareActivity"}, {"text": "compartment syndrome", "type": "BiologicFunction"}, {"text": "fasciotomies", "type": "HealthCareActivity"}, {"text": "nonunion", "type": "Finding"}, {"text": "fixation", "type": "HealthCareActivity"}, {"text": "failure", "type": "Finding"}, {"text": "implant removal", "type": "HealthCareActivity"}, {"text": "discomfort", "type": "Finding"}]}

Example input:
Sentence: Most common complications were pneumonia ( 12 % ) , UTI ( 9 % ) , and wound infection ( 7 % ) .

Example answer:
{"entities": [{"text": "complications", "type": "BiologicFunction"}, {"text": "pneumonia", "type": "BiologicFunction"}, {"text": "UTI", "type": "BiologicFunction"}, {"text": "wound infection", "type": "BiologicFunction"}]}

Input:
Sentence: Complications include bleeding , aspiration , internal organ injury , perforation , periostomal leaks , tube dislodgement , and occlusion .

## Item MedMentions:test:2760
Example input:
Sentence: The measures of disease outcome were overall survival ( OS ) and disease - free survival ( DFS ) which estimated using the Kaplan - Meier method .

Example answer:
{"entities": [{"text": "disease outcome", "type": "Finding"}, {"text": "Kaplan - Meier method", "type": "ResearchActivity"}]}

Example input:
Sentence: Among all , median OS and PFS were 35 .

Example answer:
{"entities": []}

Example input:
Sentence: Their Kaplan - Meier survival curves were digitized and pooled for generation of median overall ( OS ) and progression free ( PFS ) survivals and log - rank hazard ratios ( HRs ) .

Example answer:
{"entities": [{"text": "log - rank", "type": "IntellectualProduct"}]}

Example input:
Sentence: Overall survival ( OS ) , locoregional control ( LRC ) , and freedom from distant metastasis ( FFDM ) were calculated using log - rank and Cox regression analysis .

Example answer:
{"entities": [{"text": "locoregional", "type": "BiologicFunction"}, {"text": "freedom from distant metastasis", "type": "BiologicFunction"}, {"text": "FFDM", "type": "BiologicFunction"}, {"text": "log - rank", "type": "IntellectualProduct"}, {"text": "Cox regression analysis", "type": "IntellectualProduct"}]}

Example input:
Sentence: Secondary outcomes were 1 - year progression - free survival ( PFS ) , 1 - year overall survival ( OS ) , and health - related quality of life ( HRQL ) that was assessed using the European Organization for the Research and Treatment of Cancer Quality of Life Questionnaire C30 ( EORTC QLQ - C30 ) and its brain module ( BN - 20 ) , at baseline , after WBRT , and 4 weeks after WBRT .

Example answer:
{"entities": [{"text": "European Organization for the Research and Treatment of Cancer Quality of Life Questionnaire C30", "type": "IntellectualProduct"}, {"text": "EORTC QLQ - C30", "type": "IntellectualProduct"}, {"text": "brain module", "type": "IntellectualProduct"}, {"text": "BN - 20", "type": "IntellectualProduct"}, {"text": "WBRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: The following data were analyzed : disease control rate ( DCR ) , progression free survival ( PFS ) of first and second - line of chemotherapy , and overall survival ( OS ) .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "disease control", "type": "HealthCareActivity"}, {"text": "first", "type": "HealthCareActivity"}, {"text": "second - line", "type": "HealthCareActivity"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: 5 % , respectively , the median progression - free and overall survival ( OS ) were 19 and 45 months , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: Secondary endpoints included response rate ( RR ) , overall survival ( OS ) and median survival time ( MST ) .

Example answer:
{"entities": []}

Example input:
Sentence: The primary end point was the 2 - year progression - free survival ( PFS ) after the protocol treatment .

Example answer:
{"entities": [{"text": "protocol treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Overall survival ( OS ) and progression - free survival ( PFS ) were analyzed .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}]}

Input:
Sentence: Primary endpoints were PFS1 , progression - free survival 2 ( PFS2 ) , overall survival ( OS ) .

## Item MedMentions:test:2517
Example input:
Sentence: However , it also promotes accelerated senescence in healthy tissues and leads to progressive cognitive dysfunction in up to 50 % of tumor patients surviving long term after treatment , due to γ - irradiation -induced cerebromicrovascular injury .

Example answer:
{"entities": [{"text": "senescence", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "cognitive dysfunction", "type": "BiologicFunction"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The putative radial glia - like neural stem cells or type - 1 cells , regardless of proliferation status , were apoptosis resistant after irradiation .

Example answer:
{"entities": [{"text": "radial glia - like neural stem cells", "type": "AnatomicalStructure"}, {"text": "type - 1 cells", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: In this review , we describe the CVD risk related to low doses of ionizing radiation , the clinical manifestation and the pathology of radiation - induced CVD , as well as the importance of the endothelium models in CVD research as a way forward to complement the epidemiological data with the underlying biological and molecular mechanisms .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "CVD", "type": "BiologicFunction"}, {"text": "pathology", "type": "BiologicFunction"}, {"text": "radiation - induced CVD", "type": "BiologicFunction"}, {"text": "endothelium", "type": "AnatomicalStructure"}, {"text": "models", "type": "BiologicFunction"}, {"text": "research", "type": "ResearchActivity"}]}

Example input:
Sentence: Our data suggest for the first time that ROS generation , as mediated by NADPH oxidase activation , could be an important contributor to heavy ion irradiation - induced cell death .

Example answer:
{"entities": [{"text": "ROS generation", "type": "BiologicFunction"}, {"text": "NADPH oxidase", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}]}

Example input:
Sentence: Using a mouse model of hippocampal neuronal development , we characterized the apoptosis sensitivity of the different neural progenitor subpopulations in adult mouse dentate gyrus after irradiation .

Example answer:
{"entities": [{"text": "mouse model", "type": "BiologicFunction"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "neuronal development", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "neural progenitor", "type": "AnatomicalStructure"}, {"text": "subpopulations", "type": "PopulationGroup"}, {"text": "adult mouse", "type": "Eukaryote"}, {"text": "dentate gyrus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Far - infrared protects vascular endothelial cells from advanced glycation end products - induced injury via PLZF -mediated autophagy in diabetic mice The accumulation of advanced glycation end products ( AGEs ) in diabetic patients induces vascular endothelial injury .

Example answer:
{"entities": [{"text": "vascular endothelial cells", "type": "AnatomicalStructure"}, {"text": "advanced glycation end products", "type": "Chemical"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "PLZF", "type": "Chemical"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "diabetic mice", "type": "Eukaryote"}, {"text": "AGEs", "type": "Chemical"}, {"text": "diabetic", "type": "BiologicFunction"}, {"text": "vascular endothelial", "type": "AnatomicalStructure"}]}

Example input:
Sentence: NADPH Oxidase Activation Contributes to Heavy Ion Irradiation - Induced Cell Death Increased oxidative stress plays an important role in heavy ion radiation - induced cell death .

Example answer:
{"entities": [{"text": "NADPH Oxidase", "type": "Chemical"}, {"text": "Activation", "type": "BiologicFunction"}, {"text": "Cell Death", "type": "BiologicFunction"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}]}

Example input:
Sentence: Differential Apoptosis Radiosensitivity of Neural Progenitors in Adult Mouse Hippocampus Mammalian tissue - specific stem cells and progenitors demonstrate differential DNA damage response .

Example answer:
{"entities": [{"text": "Apoptosis", "type": "BiologicFunction"}, {"text": "Neural Progenitors", "type": "AnatomicalStructure"}, {"text": "Adult Mouse", "type": "Eukaryote"}, {"text": "Hippocampus", "type": "AnatomicalStructure"}, {"text": "Mammalian", "type": "Eukaryote"}, {"text": "stem cells", "type": "AnatomicalStructure"}, {"text": "progenitors", "type": "AnatomicalStructure"}, {"text": "DNA damage response", "type": "BiologicFunction"}]}

Example input:
Sentence: Here we show that NADPH oxidase activation is closely related to heavy ion radiation - induced cell death via excessive ROS generation .

Example answer:
{"entities": [{"text": "NADPH oxidase", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "ROS generation", "type": "BiologicFunction"}]}

Example input:
Sentence: Neural progenitors in dentate gyrus of the hippocampus are known to undergo apoptosis after irradiation .

Example answer:
{"entities": [{"text": "Neural progenitors", "type": "AnatomicalStructure"}, {"text": "dentate gyrus", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Input:
Sentence: Radiation - induced enhancement of endothelial cell apoptosis results in disruption of the vascular system and the blood brain barrier .

## Item MedMentions:test:2657
Example input:
Sentence: These findings suggest that clinical assessment of speech recognition is likely to reflect underlying cognitive and linguistic abilities , in addition to a child 's auditory skills , consistent with the Ease of Language Understanding model .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "clinical assessment", "type": "HealthCareActivity"}, {"text": "Ease of Language Understanding model", "type": "IntellectualProduct"}]}

Example input:
Sentence: Recent research shows positive associations between positive parent - child and teacher - student interactions and working memory performance and development .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "positive", "type": "Finding"}, {"text": "working memory", "type": "BiologicFunction"}, {"text": "performance", "type": "BiologicFunction"}]}

Example input:
Sentence: Keeping the Spirits Up : The Effect of Teachers ' and Parents ' Emotional Support on Children 's Working Memory Performance Working memory , used to temporarily store and mentally manipulate information , is important for children 's learning .

Example answer:
{"entities": [{"text": "Teachers '", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Emotional Support", "type": "HealthCareActivity"}, {"text": "Working Memory", "type": "BiologicFunction"}, {"text": "Performance", "type": "BiologicFunction"}, {"text": "Working memory", "type": "BiologicFunction"}, {"text": "temporarily store", "type": "BiologicFunction"}, {"text": "learning", "type": "BiologicFunction"}]}

Example input:
Sentence: When children had a positive relationship with their parent , support of parents and teachers had little effect on working memory performance .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "support", "type": "HealthCareActivity"}, {"text": "teachers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "working memory", "type": "BiologicFunction"}, {"text": "performance", "type": "BiologicFunction"}]}

Example input:
Sentence: As part of a prospective , cross - sectional study , children with normal hearing completed speech recognition in noise for three types of stimuli : ( 1 ) monosyllabic words , ( 2 ) syntactically correct but semantically anomalous sentences and ( 3 ) semantically and syntactically anomalous word sequences .

Example answer:
{"entities": [{"text": "prospective", "type": "ResearchActivity"}, {"text": "cross - sectional study", "type": "ResearchActivity"}, {"text": "normal hearing", "type": "Finding"}, {"text": "types of stimuli", "type": "IntellectualProduct"}, {"text": "monosyllabic words", "type": "IntellectualProduct"}, {"text": "anomalous", "type": "Finding"}, {"text": "sentences", "type": "IntellectualProduct"}, {"text": "word sequences", "type": "IntellectualProduct"}]}

Example input:
Sentence: Learning in Complex Environments : The Effects of Background Speech on Early Word Learning Although most studies of language learning take place in quiet laboratory settings , everyday language learning occurs under noisy conditions .

Example answer:
{"entities": [{"text": "Learning", "type": "BiologicFunction"}, {"text": "Environments", "type": "SpatialConcept"}, {"text": "Speech", "type": "BiologicFunction"}, {"text": "Word Learning", "type": "BiologicFunction"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "learning", "type": "BiologicFunction"}, {"text": "laboratory", "type": "Organization"}]}

Example input:
Sentence: Measures of vocabulary , syntax and working memory were used to predict individual differences in speech recognition in noise .

Example answer:
{"entities": [{"text": "vocabulary", "type": "IntellectualProduct"}, {"text": "working memory", "type": "BiologicFunction"}]}

Example input:
Sentence: Higher working memory was associated with better speech recognition in noise for all three stimulus types .

Example answer:
{"entities": [{"text": "working memory", "type": "BiologicFunction"}, {"text": "stimulus types", "type": "IntellectualProduct"}]}

Example input:
Sentence: Individual differences in language and working memory affect children 's speech recognition in noise We examined how cognitive and linguistic skills affect speech recognition in noise for children with normal hearing .

Example answer:
{"entities": [{"text": "working memory", "type": "BiologicFunction"}, {"text": "affect", "type": "BiologicFunction"}, {"text": "normal hearing", "type": "Finding"}]}

Example input:
Sentence: Children with better working memory and language abilities were expected to have better speech recognition in noise than peers with poorer skills in these domains .

Example answer:
{"entities": [{"text": "working memory", "type": "BiologicFunction"}, {"text": "peers", "type": "PopulationGroup"}, {"text": "domains", "type": "SpatialConcept"}]}

Input:
Sentence: Working memory and language both influence children 's speech recognition in noise , but the relationships vary across types of stimuli .

## Item MedMentions:test:2493
Example input:
Sentence: Patients with GCA had increased risks for all types of incident vascular disease compared with non - vasculitis patients : adjusted hazard ratios were 1 . 57 ( 95 % CI : 1 . 36 , 1 . 82 ) for myocardial infarction , 1 . 41 ( 95 % CI : 1 . 29 , 1 . 55 ) for stroke , 1 . 75 ( 95 % CI : 1 . 49 , 2 . 06 ) for peripheral vascular disease , 1 . 98 ( 95 % CI : 1 . 50 , 2 . 62 ) for aortic aneurysm and 2 . 03 ( 95 % CI : 1 . 77 , 2 . 33 ) for venous thromboembolism .

Example answer:
{"entities": [{"text": "GCA", "type": "BiologicFunction"}, {"text": "risks for all types of incident", "type": "Finding"}, {"text": "vascular disease", "type": "BiologicFunction"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "peripheral vascular disease", "type": "BiologicFunction"}, {"text": "aortic aneurysm", "type": "BiologicFunction"}, {"text": "venous thromboembolism", "type": "BiologicFunction"}]}

Example input:
Sentence: Symptoms included axial back pain in 100 % of patients without concomitant radiculopathy .

Example answer:
{"entities": [{"text": "Symptoms", "type": "Finding"}, {"text": "axial", "type": "SpatialConcept"}, {"text": "back pain", "type": "Finding"}, {"text": "radiculopathy", "type": "BiologicFunction"}]}

Example input:
Sentence: Only 1 subgroup , transapical TAVI , was not significantly associated with stroke - related mortality ( OR 1 . 97 , 95 % confidence interval , 0 . 43 to 7 . 43 , p = 0 .

Example answer:
{"entities": [{"text": "subgroup", "type": "IntellectualProduct"}, {"text": "transapical TAVI", "type": "HealthCareActivity"}, {"text": "stroke", "type": "BiologicFunction"}]}

Example input:
Sentence: The study identified severe malnutrition ( 33 . 9 % ) , intestinal infectious diseases ( 13 . 8 % ) and acute lower respiratory infections ( 9 . 2 % ) to be the three most leading causes of death .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "malnutrition", "type": "BiologicFunction"}, {"text": "intestinal infectious diseases", "type": "BiologicFunction"}, {"text": "acute lower respiratory infections", "type": "BiologicFunction"}, {"text": "causes of death", "type": "Finding"}]}

Example input:
Sentence: 48 - 9 . 19 [ p = . 050 ] , respectively ; all - cause mortality ( HR 2 . 05 , 95 % CI 1 . 44 - 2 . 92 [ p < . 001 ] ; HR 2 . 53 , 95 % CI 1 . 35 - 4 . 74 [ p = . 040 ] , respectively ) ; and amputation or death ( HR 2 . 13 , 95 % CI 1 .

Example answer:
{"entities": [{"text": "amputation", "type": "HealthCareActivity"}, {"text": "death", "type": "BiologicFunction"}]}

Example input:
Sentence: Chronic conditions such as coronary artery disease ( odds ratio [ OR ] 1 . 48 ; 95 % confidence interval [ CI ] 1 . 04 - 2 . 05 ; p = 0 . 03 ) , diabetes ( OR 1 . 86 ; 95 % CI 1 . 32 - 2 . 62 ; p = 0 . 0004 ) , and peripheral vascular disease ( OR 1 . 61 ; 95 % CI 1 .

Example answer:
{"entities": [{"text": "Chronic conditions", "type": "Finding"}, {"text": "coronary artery disease", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "peripheral vascular disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Pooled estimates for cause - specific mortality were strongest in myocardial infarction ( 4 . 30 % , 95 % CI [ 1 . 18 , 7 . 51 ] ) , followed by respiratory diseases ( 3 . 17 % , 95 % CI [ 0 . 26 , 6 . 17 ] ) and ischemic heart diseases ( 2 . 54 % , 95 % CI [ 1 . 08 , 4 . 02 ] ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "respiratory diseases", "type": "BiologicFunction"}, {"text": "ischemic heart diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: An increased hazard of nonneurologic death was seen with increasing age ( P = .03 ) , nonmelanoma histology ( P < . 001 ) , presence of extracranial disease ( P < . 001 ) , and progressive systemic disease ( P = .004 ) .

Example answer:
{"entities": [{"text": "nonneurologic death", "type": "Finding"}, {"text": "nonmelanoma histology", "type": "HealthCareActivity"}, {"text": "extracranial disease", "type": "BiologicFunction"}, {"text": "systemic disease", "type": "BiologicFunction"}]}

Example input:
Sentence: The presence of apical pathosis was significantly correlated ( odds ratio ( OR ) 2 . 556 [ confidence interval ( CI ) 2 . 076 - 3 . 146 ] ; P < 0 .

Example answer:
{"entities": [{"text": "presence", "type": "Finding"}, {"text": "apical", "type": "AnatomicalStructure"}, {"text": "pathosis", "type": "BiologicFunction"}]}

Example input:
Sentence: 41 - 2 . 80 ) when adjusted for age and sex ( p < 0 . 001 ) , and remained significant after stratifying patients into the 2 major causes of death : diseases of the circulatory system and malignant neoplasms .

Example answer:
{"entities": [{"text": "causes of death", "type": "Finding"}, {"text": "diseases of the circulatory system", "type": "BiologicFunction"}, {"text": "malignant neoplasms", "type": "BiologicFunction"}]}

Input:
Sentence: Peripheral and axial disease was associated with death ( OR 4 . 02 , 95 % CI 1 . 84 - 8 . 84 , p < 0 . 001 ) compared with peripheral disease only .

## Item MedMentions:test:2384
Example input:
Sentence: Furthermore , the cells at pH 6 . 6 were resistant to apoptosis by doxorubicin ( P ≤ 0 .

Example answer:
{"entities": [{"text": "cells", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: A bleomycin , etoposide , and cisplatin treatment protocol targeting germ cell neoplasia lead to disease remission and prolonged survival of 34 months .

Example answer:
{"entities": [{"text": "bleomycin", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "treatment protocol", "type": "HealthCareActivity"}, {"text": "germ cell neoplasia", "type": "BiologicFunction"}, {"text": "disease remission", "type": "Finding"}]}

Example input:
Sentence: The cell viability , prolactin level , and G0 - G1 cells are similar in MMQ cells treated with RAPA and a low concentration of BRC and MMQ cells treated with a high concentration of BRC .

Example answer:
{"entities": [{"text": "cell viability", "type": "BiologicFunction"}, {"text": "prolactin level", "type": "Finding"}, {"text": "MMQ cells", "type": "AnatomicalStructure"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "RAPA", "type": "Chemical"}, {"text": "BRC", "type": "Chemical"}]}

Example input:
Sentence: In particular , SP cells were highly sensitive to fenretinide , and in combination with bortezomib and dexamethasone in colony formation and apoptosis assays .

Example answer:
{"entities": [{"text": "SP", "type": "AnatomicalStructure"}, {"text": "fenretinide", "type": "Chemical"}, {"text": "bortezomib and dexamethasone", "type": "HealthCareActivity"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "assays", "type": "HealthCareActivity"}]}

Example input:
Sentence: In this study , we manipulated RBBP6 expression levels followed by treatment with either camptothecin or γ - aminobutyric acid in cervical cancer cells to induce apoptosis or cell cycle arrest .

Example answer:
{"entities": [{"text": "study", "type": "HealthCareActivity"}, {"text": "manipulated", "type": "HealthCareActivity"}, {"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "camptothecin", "type": "Chemical"}, {"text": "γ - aminobutyric acid", "type": "Chemical"}, {"text": "induce", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "cell cycle arrest", "type": "BiologicFunction"}]}

Example input:
Sentence: Aureocin A70 caused a time - dependent reduction in the listerial viable cell counts ( 5 . 51 - log units ) up to 7days of incubation .

Example answer:
{"entities": [{"text": "Aureocin A70", "type": "Chemical"}, {"text": "listerial", "type": "Bacterium"}, {"text": "viable cell counts", "type": "HealthCareActivity"}, {"text": "incubation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Silencing RBBP6 followed by treatment with γ - aminobutyric acid and camptothecin seems to sensitize cells to apoptosis induction rather than cell cycle arrest .

Example answer:
{"entities": [{"text": "Silencing", "type": "BiologicFunction"}, {"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "γ - aminobutyric acid", "type": "Chemical"}, {"text": "camptothecin", "type": "Chemical"}, {"text": "sensitize cells", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "induction", "type": "BiologicFunction"}, {"text": "cell cycle arrest", "type": "BiologicFunction"}]}

Example input:
Sentence: Very high polymyxin B concentration completely eradicated exponential cells and regrowth was seen in a stationary population .

Example answer:
{"entities": [{"text": "polymyxin B", "type": "Chemical"}, {"text": "exponential cells", "type": "Bacterium"}, {"text": "stationary population", "type": "PopulationGroup"}]}

Example input:
Sentence: Stationary cells appear to be somewhat more tolerant than exponential cells in all of these assays .

Example answer:
{"entities": [{"text": "Stationary cells", "type": "Bacterium"}, {"text": "tolerant", "type": "Finding"}, {"text": "exponential cells", "type": "Bacterium"}, {"text": "assays", "type": "HealthCareActivity"}]}

Example input:
Sentence: Stationary - phase cells were more tolerant to imipenem ( Carbapenem ) than exponential cells , leaving a small fraction of persisters at high imipenem concentration in both populations .

Example answer:
{"entities": [{"text": "Stationary - phase cells", "type": "Bacterium"}, {"text": "tolerant", "type": "Finding"}, {"text": "imipenem", "type": "Chemical"}, {"text": "Carbapenem", "type": "Chemical"}, {"text": "exponential cells", "type": "Bacterium"}, {"text": "persisters", "type": "Bacterium"}, {"text": "populations", "type": "PopulationGroup"}]}

Input:
Sentence: Stationary cells were more tolerant to tobramycin ( Aminoglycoside ) than exponential cells but a higher concentration of tobramycin completely eliminated survivors .

## Item MedMentions:test:2212
Example input:
Sentence: Morphologic changes along the trabecular outflow pathway were investigated by confocal , light , and electron microscopy .

Example answer:
{"entities": [{"text": "Morphologic changes", "type": "AnatomicalStructure"}, {"text": "trabecular", "type": "AnatomicalStructure"}, {"text": "confocal", "type": "HealthCareActivity"}, {"text": "light", "type": "HealthCareActivity"}, {"text": "electron microscopy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Additionally , 2 , 3 , 5 , 4 ' - tetrahydroxystilbene - 2 - O - β - D - glucoside significantly increased the microvessel density in the brain and upregulated CD31 expression in ischemic penumbra , relative to that in the control .

Example answer:
{"entities": [{"text": "2 , 3 , 5 , 4 ' - tetrahydroxystilbene - 2 - O - β - D - glucoside", "type": "Chemical"}, {"text": "microvessel", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "CD31", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "ischemic", "type": "BiologicFunction"}]}

Example input:
Sentence: Mechanism studies indicate that its cytoprotective effects are mediated by activating the Nrf2 signaling pathway in the Michael acceptor - and catechol -dependent manners .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "cytoprotective", "type": "BiologicFunction"}, {"text": "Nrf2", "type": "Chemical"}, {"text": "signaling pathway", "type": "BiologicFunction"}, {"text": "Michael acceptor", "type": "Chemical"}, {"text": "catechol", "type": "Chemical"}]}

Example input:
Sentence: Studying neuroprotective effect of Atorvastatin as a small molecule drug on high glucose - induced neurotoxicity in undifferentiated PC12 cells : role of NADPH oxidase Overproduction of reactive oxygen species ( ROS ) by NADPH oxidase ( NOX ) activation has been considered the essential mechanism induced by hyperglycemia in various tissues .

Example answer:
{"entities": [{"text": "Studying", "type": "ResearchActivity"}, {"text": "Atorvastatin", "type": "Chemical"}, {"text": "small molecule", "type": "Chemical"}, {"text": "drug", "type": "Chemical"}, {"text": "high glucose", "type": "Finding"}, {"text": "neurotoxicity", "type": "InjuryOrPoisoning"}, {"text": "PC12 cells", "type": "AnatomicalStructure"}, {"text": "NADPH oxidase", "type": "Chemical"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "ROS", "type": "Chemical"}, {"text": "NOX", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "hyperglycemia", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The 2 - hour infusion of AUY922 at 100mg / kg caused disorganization of the outer segment photoreceptor morphology in male Brown Norway rats ; the severity of the disorganization increased with the number of administrations , but was reversible during a 4 - week posttreatment period .

Example answer:
{"entities": [{"text": "infusion", "type": "HealthCareActivity"}, {"text": "AUY922", "type": "Chemical"}, {"text": "outer segment photoreceptor", "type": "AnatomicalStructure"}, {"text": "Brown Norway rats", "type": "Eukaryote"}, {"text": "administrations", "type": "HealthCareActivity"}]}

Example input:
Sentence: We therefore induced eSAH in knockout mice for ICAM - 1 ( ICAM - 1 ( - / - ) ) and P - selectin glycoprotein ligand - 1 ( PSGL - 1 ( - / - ) ) to find a significant decrease in neutrophil - endothelial interaction within the first 7 days after the bleeding in a chronic cranial window model .

Example answer:
{"entities": [{"text": "eSAH", "type": "BiologicFunction"}, {"text": "knockout mice", "type": "Eukaryote"}, {"text": "ICAM - 1", "type": "AnatomicalStructure"}, {"text": "ICAM - 1 ( - / - )", "type": "AnatomicalStructure"}, {"text": "P - selectin glycoprotein ligand - 1", "type": "AnatomicalStructure"}, {"text": "PSGL - 1 ( - / - )", "type": "AnatomicalStructure"}, {"text": "neutrophil", "type": "AnatomicalStructure"}, {"text": "endothelial", "type": "AnatomicalStructure"}, {"text": "interaction", "type": "BiologicFunction"}, {"text": "bleeding", "type": "BiologicFunction"}, {"text": "cranial", "type": "SpatialConcept"}]}

Example input:
Sentence: Perfusion with netarsudil - M1 significantly increased C when compared to baseline ( 51 % , P < 0 .

Example answer:
{"entities": [{"text": "Perfusion", "type": "HealthCareActivity"}, {"text": "netarsudil - M1", "type": "Chemical"}, {"text": "C", "type": "HealthCareActivity"}]}

Example input:
Sentence: Paired human eyes ( n = 5 ) were perfused with either 0 . 3 μM netarsudil - M1 or vehicle solution at constant pressure ( 15 mm Hg ) .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "eyes", "type": "AnatomicalStructure"}, {"text": "perfused", "type": "HealthCareActivity"}, {"text": "netarsudil - M1", "type": "Chemical"}, {"text": "vehicle solution", "type": "Chemical"}]}

Example input:
Sentence: Netarsudil acutely increased C by expansion of the JCT and dilating the ESVs , which led to redistribution of aqueous outflow through a larger area of the IW and ESVs .

Example answer:
{"entities": [{"text": "Netarsudil", "type": "Chemical"}, {"text": "C", "type": "HealthCareActivity"}, {"text": "JCT", "type": "AnatomicalStructure"}, {"text": "ESVs", "type": "AnatomicalStructure"}, {"text": "larger area", "type": "SpatialConcept"}]}

Example input:
Sentence: Netarsudil Increases Outflow Facility in Human Eyes Through Multiple Mechanisms Netarsudil is a Rho kinase / norepinephrine transporter inhibitor currently in phase 3 clinical development for glaucoma treatment .

Example answer:
{"entities": [{"text": "Netarsudil", "type": "Chemical"}, {"text": "Outflow Facility", "type": "HealthCareActivity"}, {"text": "Human", "type": "Eukaryote"}, {"text": "Eyes", "type": "AnatomicalStructure"}, {"text": "Rho kinase / norepinephrine transporter inhibitor", "type": "Chemical"}, {"text": "phase 3 clinical development", "type": "ResearchActivity"}, {"text": "glaucoma", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Input:
Sentence: We investigated the effects of its active metabolite , netarsudil - M1 , on outflow facility ( C ) , outflow hydrodynamics , and morphology of the conventional outflow pathway in enucleated human eyes .

## Item MedMentions:test:2123
Example input:
Sentence: Many candidate genes have homologs identified in studies of human disease , suggesting that genes affecting variation in susceptibility are conserved across species .

Example answer:
{"entities": [{"text": "candidate genes", "type": "AnatomicalStructure"}, {"text": "homologs", "type": "SpatialConcept"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: We have used an assay targeting approximately 6700 heterozygous SNPs around the CAH gene ( CYP21A2 ) to construct the high - risk parental haplotypes and tested this approach in five cases , showing that inheritance of the parental alleles can be correctly identified using NIPD .

Example answer:
{"entities": [{"text": "assay", "type": "HealthCareActivity"}, {"text": "SNPs", "type": "SpatialConcept"}, {"text": "CAH gene", "type": "AnatomicalStructure"}, {"text": "CYP21A2", "type": "AnatomicalStructure"}, {"text": "high - risk", "type": "Finding"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "alleles", "type": "AnatomicalStructure"}, {"text": "NIPD", "type": "HealthCareActivity"}]}

Example input:
Sentence: A total of 4 , 976 SNPs from the 9 K iSelect array were used in the study for the analysis of population structure , linkage disequilibrium ( LD ) and genome - wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "SNPs", "type": "SpatialConcept"}, {"text": "study", "type": "ResearchActivity"}, {"text": "genome - wide association study", "type": "ResearchActivity"}, {"text": "GWAS", "type": "ResearchActivity"}]}

Example input:
Sentence: Integrating molecular QTL data into genome - wide genetic association analysis : Probabilistic assessment of enrichment and colocalization We propose a novel statistical framework for integrating the result from molecular quantitative trait loci ( QTL ) mapping into genome - wide genetic association analysis of complex traits , with the primary objectives of quantitatively assessing the enrichment of the molecular QTLs in complex trait - associated genetic variants and the colocalizations of the two types of association signals .

Example answer:
{"entities": [{"text": "QTL", "type": "AnatomicalStructure"}, {"text": "genome - wide genetic association analysis", "type": "ResearchActivity"}, {"text": "statistical framework", "type": "IntellectualProduct"}, {"text": "quantitative trait loci", "type": "AnatomicalStructure"}, {"text": "QTLs", "type": "AnatomicalStructure"}, {"text": "genetic variants", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Conservation patterns analysis revealed that 57 % of pig lncRNAs showed homology to humans and mice based on genome alignment .

Example answer:
{"entities": [{"text": "patterns analysis", "type": "HealthCareActivity"}, {"text": "pig", "type": "Eukaryote"}, {"text": "lncRNAs", "type": "Chemical"}, {"text": "humans", "type": "Eukaryote"}, {"text": "mice", "type": "Eukaryote"}, {"text": "genome alignment", "type": "ResearchActivity"}]}

Example input:
Sentence: Genome - Wide SNP Linkage Mapping and QTL Analysis for Fiber Quality and Yield Traits in the Upland Cotton Recombinant Inbred Lines Population It is of significance to discover genes related to fiber quality and yield traits and tightly linked markers for marker - assisted selection ( MAS ) in cotton breeding .

Example answer:
{"entities": [{"text": "Genome - Wide SNP Linkage Mapping", "type": "HealthCareActivity"}, {"text": "QTL", "type": "AnatomicalStructure"}, {"text": "Analysis", "type": "HealthCareActivity"}, {"text": "Fiber", "type": "Eukaryote"}, {"text": "Upland Cotton", "type": "Eukaryote"}, {"text": "Recombinant Inbred Lines", "type": "Eukaryote"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "fiber", "type": "Eukaryote"}, {"text": "markers", "type": "BiologicFunction"}, {"text": "marker - assisted selection", "type": "ResearchActivity"}, {"text": "MAS", "type": "ResearchActivity"}, {"text": "cotton", "type": "Eukaryote"}, {"text": "breeding", "type": "BiologicFunction"}]}

Example input:
Sentence: Evolution of H5 highly pathogenic avian influenza : sequence data indicate stepwise changes in the cleavage site The genetic composition of an H5 subtype hemagglutinin gene quasispecies , obtained from ostrich tissues that had been infected with H5 subtype influenza virus was analysed using a next generation sequencing approach .

Example answer:
{"entities": [{"text": "Evolution", "type": "BiologicFunction"}, {"text": "H5 highly pathogenic avian influenza", "type": "Virus"}, {"text": "sequence", "type": "SpatialConcept"}, {"text": "cleavage site", "type": "SpatialConcept"}, {"text": "H5 subtype hemagglutinin gene", "type": "AnatomicalStructure"}, {"text": "quasispecies", "type": "Virus"}, {"text": "ostrich", "type": "Eukaryote"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "infected", "type": "BiologicFunction"}, {"text": "H5 subtype influenza virus", "type": "Virus"}, {"text": "next generation sequencing approach", "type": "ResearchActivity"}]}

Example input:
Sentence: Further enrichment analyses indicated that these genes were associated with immune function , sensory organ development and neurogenesis , and may have experienced positive selection in chicken .

Example answer:
{"entities": [{"text": "enrichment analyses", "type": "ResearchActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "immune function", "type": "BiologicFunction"}, {"text": "sensory organ development", "type": "BiologicFunction"}, {"text": "neurogenesis", "type": "BiologicFunction"}, {"text": "positive selection", "type": "HealthCareActivity"}, {"text": "chicken", "type": "Eukaryote"}]}

Example input:
Sentence: In the present study , we performed Extended Haplotype Homozygosity ( EHH ) tests to identify significant core regions employing 600 K SNP Chicken chip in an F2 population of 1 , 534 hens , which was derived from reciprocal crosses between White Leghorn and Dongxiang chicken .

Example answer:
{"entities": [{"text": "core regions", "type": "SpatialConcept"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "Chicken", "type": "Eukaryote"}, {"text": "chip", "type": "ResearchActivity"}, {"text": "hens", "type": "Eukaryote"}, {"text": "reciprocal crosses", "type": "HealthCareActivity"}, {"text": "White Leghorn", "type": "Eukaryote"}, {"text": "Dongxiang chicken", "type": "Eukaryote"}]}

Example input:
Sentence: Findings in our study could draw a comparatively integrate genome - wide map of selection signature in the chicken genome , and would be worthy for explicating the genetic mechanisms of phenotypic diversity in poultry breeding .

Example answer:
{"entities": [{"text": "genome - wide map", "type": "ResearchActivity"}, {"text": "selection signature", "type": "BiologicFunction"}, {"text": "chicken", "type": "Eukaryote"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "poultry", "type": "Eukaryote"}, {"text": "breeding", "type": "BiologicFunction"}]}

Input:
Sentence: Genome - Wide Detection of Selective Signatures in Chicken through High Density SNPs Chicken is recognized as an excellent model for studies of genetic mechanism of phenotypic and genomic evolution , with large effective population size and strong human -driven selection .

## Item MedMentions:test:2344
Example input:
Sentence: Accordingly , CYP2C19 pharmacogenetic profiling may be beneficial for coronary heart patients undergoing PCI to predict the efficacy of treatment with clopidogrel .

Example answer:
{"entities": [{"text": "CYP2C19", "type": "AnatomicalStructure"}, {"text": "pharmacogenetic profiling", "type": "BiologicFunction"}, {"text": "PCI", "type": "HealthCareActivity"}, {"text": "clopidogrel", "type": "Chemical"}]}

Example input:
Sentence: Root Cause Analysis of Adverse Events in an Outpatient Anticoagulation Management Consortium A number of factors can lead to adverse events ( AEs ) in patients taking warfarin .

Example answer:
{"entities": [{"text": "Adverse Events", "type": "BiologicFunction"}, {"text": "Anticoagulation", "type": "Finding"}, {"text": "Management", "type": "HealthCareActivity"}, {"text": "Consortium", "type": "ProfessionalOrOccupationalGroup"}, {"text": "adverse events", "type": "BiologicFunction"}, {"text": "AEs", "type": "BiologicFunction"}, {"text": "warfarin", "type": "Chemical"}]}

Example input:
Sentence: The majority of severe AEs for patients taking warfarin were related to nonmodifiable patient -related issues .

Example answer:
{"entities": [{"text": "AEs", "type": "BiologicFunction"}, {"text": "warfarin", "type": "Chemical"}, {"text": "issues", "type": "Finding"}]}

Example input:
Sentence: Various treatment options such as low - intensity warfarin and aspirin plus clopidogrel have been suggested but are inferior to dose - adjusted warfarin .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "inferior", "type": "SpatialConcept"}]}

Example input:
Sentence: This study is an important step toward incorporating pharmacogenomics into CDSS design for clinical testing .

Example answer:
{"entities": [{"text": "pharmacogenomics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "CDSS", "type": "IntellectualProduct"}, {"text": "clinical testing", "type": "ResearchActivity"}]}

Example input:
Sentence: Warfarin treatment was associated with higher risk of bleeding in all eGFR groups and lower risk of stroke in patients with eGFR ≥15 mL / min per 1 .

Example answer:
{"entities": [{"text": "bleeding", "type": "BiologicFunction"}, {"text": "eGFR", "type": "HealthCareActivity"}, {"text": "stroke", "type": "BiologicFunction"}]}

Example input:
Sentence: Of the patients with 1 or no dose - reduction criteria assigned to receive the 5 mg twice daily dose of apixaban or warfarin , 3966 had 1 dose - reduction criterion ; these patients had higher rates of stroke or systemic embolism ( HR , 1 . 47 ; 95 % CI , 1 . 20 - 1 . 81 ) and major bleeding ( HR , 1 . 89 ; 95 % CI , 1 . 62 - 2 . 20 ) compared with those with no dose - reduction criteria ( n = 13 356 ) .

Example answer:
{"entities": [{"text": "apixaban", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "bleeding", "type": "BiologicFunction"}]}

Example input:
Sentence: Twelve physicians and pharmacists completed 6 prescribing tasks using simulated patient scenarios in two iterations ( development and validation phases ) of a newly developed pharmacogenomic -driven CDSS prototype .

Example answer:
{"entities": [{"text": "physicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "pharmacists", "type": "ProfessionalOrOccupationalGroup"}, {"text": "iterations", "type": "Finding"}, {"text": "validation", "type": "ResearchActivity"}, {"text": "pharmacogenomic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "CDSS", "type": "IntellectualProduct"}]}

Example input:
Sentence: A pharmacogenomic -guided CDSS has been developed using warfarin as the test drug .

Example answer:
{"entities": [{"text": "pharmacogenomic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "CDSS", "type": "IntellectualProduct"}, {"text": "warfarin", "type": "Chemical"}, {"text": "drug", "type": "Chemical"}]}

Example input:
Sentence: Iterative Development and Evaluation of a Pharmacogenomic -Guided Clinical Decision Support System for Warfarin Dosing Pharmacogenomic -guided dosing has the potential to improve patient outcomes but its implementation has been met with clinical challenges .

Example answer:
{"entities": [{"text": "Iterative", "type": "Finding"}, {"text": "Evaluation", "type": "HealthCareActivity"}, {"text": "Pharmacogenomic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Clinical Decision Support System", "type": "IntellectualProduct"}, {"text": "challenges", "type": "HealthCareActivity"}]}

Input:
Sentence: Our objective was to develop and evaluate a clinical decision support system ( CDSS ) for pharmacogenomic -guided warfarin dosing designed for physicians and pharmacists .

## Item MedMentions:test:2674
Example input:
Sentence: The nitrogen recovery ( % of nitrogen excreted in housings that is applied to land ) would increase from a mean of 57 % ( in 2010 ) to 61 % by acidification , but would decrease to 48 % by incineration .

Example answer:
{"entities": [{"text": "nitrogen", "type": "Chemical"}, {"text": "land", "type": "SpatialConcept"}]}

Example input:
Sentence: Viable MU N2 were recovered from cultures of the homogenates and aspirates .

Example answer:
{"entities": [{"text": "MU N2", "type": "Bacterium"}, {"text": "cultures", "type": "HealthCareActivity"}, {"text": "aspirates", "type": "BodySubstance"}]}

Example input:
Sentence: Results : Routine cleaning and shaping resulted in twenty four negative ( 80 % ) out of 30 cultures .

Example answer:
{"entities": [{"text": "shaping", "type": "HealthCareActivity"}, {"text": "negative", "type": "Finding"}, {"text": "cultures", "type": "HealthCareActivity"}]}

Example input:
Sentence: The proportion of plants with PMCs progressing through meiosis after heat treatment was lower for N5DT5B plants than for euploids , but the difference was not significant .

Example answer:
{"entities": [{"text": "plants", "type": "Eukaryote"}, {"text": "PMCs", "type": "AnatomicalStructure"}, {"text": "meiosis", "type": "BiologicFunction"}, {"text": "N5DT5B plants", "type": "Eukaryote"}, {"text": "not significant", "type": "Finding"}]}

Example input:
Sentence: As compared to GNS - mPEG , the cellular internalization of GNS - pHLIP was 1 - fold higher after a 2 h incubation with cells in media at pH 6 .

Example answer:
{"entities": [{"text": "GNS", "type": "Chemical"}, {"text": "mPEG", "type": "Chemical"}, {"text": "pHLIP", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Low Efficiency Upconversion Nanoparticles for High - Resolution Coalignment of Near - Infrared and Visible Light Paths on a Light Microscope The combination of near - infrared ( NIR ) and visible wavelengths in light microscopy for biological studies is increasingly common .

Example answer:
{"entities": [{"text": "Light Microscope", "type": "MedicalDevice"}, {"text": "light microscopy", "type": "HealthCareActivity"}, {"text": "biological studies", "type": "HealthCareActivity"}]}

Example input:
Sentence: Detachment of the fucoxanthin chlorophyll a / c binding protein ( FCP ) antenna is not involved in the acclimative regulation of photoprotection in the pennate diatom Phaeodactylum tricornutum When grown under intermittent light ( IL ) , the pennate diatom Phaeodactylum tricornutum forms ' super ' non - photochemical fluorescence quenching ( NPQ ) in response to excess light .

Example answer:
{"entities": [{"text": "fucoxanthin chlorophyll a / c binding protein", "type": "Chemical"}, {"text": "FCP", "type": "Chemical"}, {"text": "antenna", "type": "AnatomicalStructure"}, {"text": "acclimative", "type": "BiologicFunction"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "photoprotection", "type": "BiologicFunction"}, {"text": "pennate diatom", "type": "Eukaryote"}, {"text": "Phaeodactylum tricornutum", "type": "Eukaryote"}, {"text": "' super ' non - photochemical fluorescence quenching", "type": "BiologicFunction"}, {"text": "NPQ", "type": "BiologicFunction"}]}

Example input:
Sentence: The current inactivation was slower and recovery from inactivation was faster in SCN5A - M1851V channels .

Example answer:
{"entities": [{"text": "SCN5A - M1851V channels", "type": "Chemical"}]}

Example input:
Sentence: Here we addressed how antenna reorganisation controls NPQ kinetics in P .

Example answer:
{"entities": [{"text": "antenna", "type": "AnatomicalStructure"}, {"text": "NPQ", "type": "BiologicFunction"}, {"text": "P .", "type": "Eukaryote"}]}

Example input:
Sentence: Although antenna detachment relieved excitation pressure , it provided a minor protective contribution equivalent to NPQ ~1 , while the largest NPQ was 4 . 4±0 .

Example answer:
{"entities": [{"text": "antenna", "type": "AnatomicalStructure"}, {"text": "NPQ", "type": "BiologicFunction"}]}

Input:
Sentence: Regardless of different levels of NPQ formed in both culture conditions , its dark recovery was rapid and similar fractions of their antenna uncoupled ( ~50 % ) .

## Item MedMentions:test:2729
Example input:
Sentence: Negligible ex - vivo hemolysis indicated the higher biocompatibility of the nanoparticles .

Example answer:
{"entities": [{"text": "ex - vivo", "type": "ResearchActivity"}, {"text": "hemolysis", "type": "Finding"}]}

Example input:
Sentence: The prepared nanoparticles were modified by pure AChE and they were used for the measurement anti - Alzheimer 's drug galantamine and carbamate pesticide carbofuran with limit of detection 1 .

Example answer:
{"entities": [{"text": "pure AChE", "type": "Chemical"}, {"text": "anti - Alzheimer 's", "type": "Finding"}, {"text": "drug", "type": "Chemical"}, {"text": "galantamine", "type": "Chemical"}, {"text": "carbamate pesticide", "type": "Chemical"}, {"text": "carbofuran", "type": "Chemical"}, {"text": "detection", "type": "Finding"}]}

Example input:
Sentence: In practice , drug release studies under such close to physiological conditions may be complicated by the small size of lipid nanoparticles , which is in the same range as that of the potential acceptor particles .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "lipid", "type": "Chemical"}, {"text": "acceptor particles", "type": "Chemical"}]}

Example input:
Sentence: neesiana cell ultrastructure was modified and severe alterations were observed in chloroplasts from samples exposed in the most polluted site , and Cd - and Pb - cultured samples .

Example answer:
{"entities": [{"text": "neesiana", "type": "Eukaryote"}, {"text": "cell", "type": "AnatomicalStructure"}, {"text": "ultrastructure", "type": "AnatomicalStructure"}, {"text": "chloroplasts", "type": "AnatomicalStructure"}, {"text": "exposed in the most polluted site", "type": "InjuryOrPoisoning"}, {"text": "Cd", "type": "Chemical"}, {"text": "Pb", "type": "Chemical"}, {"text": "cultured samples", "type": "HealthCareActivity"}]}

Example input:
Sentence: The nanocrystalline biopolymeric nanoparticles were stable , biocompatible and have potential to be administered through i .

Example answer:
{"entities": [{"text": "biopolymeric", "type": "Chemical"}]}

Example input:
Sentence: However , the nanoparticles resistance increases considerably in the presence of the sugars .

Example answer:
{"entities": [{"text": "sugars", "type": "Chemical"}]}

Example input:
Sentence: Nevertheless , given that the molecular changes between the staging groups were subtle , the results need to be interpreted cautiously .

Example answer:
{"entities": [{"text": "staging groups", "type": "IntellectualProduct"}]}

Example input:
Sentence: The colloidal characteristics of the synthesized nanoparticles were revealed by X - ray Diffraction ( XRD ) analysis .

Example answer:
{"entities": [{"text": "nanoparticles", "type": "Chemical"}]}

Example input:
Sentence: Prepared nanoparticles were characterized by Visual inspection , Ultraviolet - visible spectroscopy ( UV ) , Fourier transform infrared Spectroscopy ( FT - IR ) , Transmission Electron Microscopy ( TEM ) techniques .

Example answer:
{"entities": [{"text": "Ultraviolet - visible spectroscopy", "type": "HealthCareActivity"}, {"text": "UV", "type": "HealthCareActivity"}, {"text": "Fourier transform infrared Spectroscopy", "type": "ResearchActivity"}, {"text": "FT - IR", "type": "ResearchActivity"}, {"text": "Transmission Electron Microscopy ( TEM ) techniques", "type": "HealthCareActivity"}]}

Example input:
Sentence: Biopersistence and translocation to extrapulmonary organs of titanium dioxide nanoparticles after subacute inhalation exposure to aerosol in adult and elderly rats The increasing industrial use of nanoparticles ( NPs ) has raised concerns about their impact on human health .

Example answer:
{"entities": [{"text": "translocation", "type": "BiologicFunction"}, {"text": "extrapulmonary", "type": "AnatomicalStructure"}, {"text": "organs", "type": "AnatomicalStructure"}, {"text": "titanium dioxide", "type": "Chemical"}, {"text": "inhalation", "type": "BiologicFunction"}, {"text": "elderly", "type": "PopulationGroup"}, {"text": "rats", "type": "Eukaryote"}, {"text": "human", "type": "Eukaryote"}]}

Input:
Sentence: Nevertheless , some chemical alterations were observed in the nanoparticles .

## Item MedMentions:test:2551
Example input:
Sentence: Electronic databases of PubMed , Embase , and Web of Science were searched for relevant studies .

Example answer:
{"entities": [{"text": "PubMed", "type": "IntellectualProduct"}, {"text": "Embase", "type": "IntellectualProduct"}, {"text": "Web of Science", "type": "IntellectualProduct"}, {"text": "relevant studies", "type": "ResearchActivity"}]}

Example input:
Sentence: Electronic searches from inception to July 31 , 2016 , were performed using PubMed , Medline OVID , Cochrane Library , EMBASE , CINAHL plus , and PsycINFO .

Example answer:
{"entities": [{"text": "PubMed", "type": "IntellectualProduct"}, {"text": "Medline OVID", "type": "IntellectualProduct"}, {"text": "Cochrane Library", "type": "IntellectualProduct"}, {"text": "EMBASE", "type": "IntellectualProduct"}, {"text": "CINAHL plus", "type": "IntellectualProduct"}]}

Example input:
Sentence: A literature search strategy was conducted using various search terms in MEDLINE and Embase .

Example answer:
{"entities": [{"text": "literature", "type": "IntellectualProduct"}, {"text": "MEDLINE", "type": "IntellectualProduct"}, {"text": "Embase", "type": "IntellectualProduct"}]}

Example input:
Sentence: A systematic review ( SR ) was performed by 2 independent reviewers using 3 electronic databases ( PubMed , ScienceDirect , and Scopus ) .

Example answer:
{"entities": [{"text": "systematic review", "type": "IntellectualProduct"}, {"text": "SR", "type": "IntellectualProduct"}, {"text": "reviewers", "type": "PopulationGroup"}, {"text": "PubMed", "type": "IntellectualProduct"}]}

Example input:
Sentence: A systematic search of the literature was conducted to identify related articles published from January 1980 to September 2016 in Pubmed , Embase , the Cochrane Library and SpringerLink .

Example answer:
{"entities": [{"text": "literature", "type": "IntellectualProduct"}, {"text": "articles", "type": "IntellectualProduct"}, {"text": "Pubmed", "type": "IntellectualProduct"}, {"text": "Embase", "type": "IntellectualProduct"}, {"text": "Cochrane Library", "type": "IntellectualProduct"}, {"text": "SpringerLink", "type": "IntellectualProduct"}]}

Example input:
Sentence: Areas covered : We searched Medline , Google Scholar , PubMed , ProQuest Dissertation , and Theses databases for reports published in English .

Example answer:
{"entities": [{"text": "Medline", "type": "IntellectualProduct"}, {"text": "Google Scholar", "type": "IntellectualProduct"}, {"text": "PubMed", "type": "IntellectualProduct"}, {"text": "ProQuest Dissertation", "type": "IntellectualProduct"}, {"text": "databases", "type": "IntellectualProduct"}, {"text": "reports", "type": "IntellectualProduct"}]}

Example input:
Sentence: Five electronic databases were searched , limited to studies published in the English language , during the period 2005 - 2015 : PubMed , Thomson ISI - Web of Science , Scopus , ProQuest , and ScienceDirect .

Example answer:
{"entities": [{"text": "PubMed", "type": "IntellectualProduct"}, {"text": "Thomson ISI - Web of Science", "type": "IntellectualProduct"}, {"text": "Scopus", "type": "IntellectualProduct"}, {"text": "ProQuest", "type": "IntellectualProduct"}, {"text": "ScienceDirect", "type": "IntellectualProduct"}]}

Example input:
Sentence: We conducted a literature review , in consultation with the PubMed , Lilacs , and Scielo databases .

Example answer:
{"entities": [{"text": "literature review", "type": "IntellectualProduct"}, {"text": "PubMed", "type": "IntellectualProduct"}, {"text": "Lilacs", "type": "IntellectualProduct"}, {"text": "Scielo databases", "type": "IntellectualProduct"}]}

Example input:
Sentence: A systematic literature search was performed in PubMed , Education Resource information Centre ( ERIC ) , Psycinfo and Cochrane reviews including studies conducted after 1990 and before the first of August of 2013 .

Example answer:
{"entities": [{"text": "PubMed", "type": "IntellectualProduct"}, {"text": "Cochrane", "type": "IntellectualProduct"}, {"text": "reviews", "type": "IntellectualProduct"}, {"text": "studies", "type": "HealthCareActivity"}]}

Example input:
Sentence: A systematic search of the relevant literature was performed within international databases , including PubMed / Medline , Scopus , ScienceDirect , and ProQuest , as well as Google Scholar using relevant keywords .

Example answer:
{"entities": [{"text": "literature", "type": "IntellectualProduct"}, {"text": "international databases", "type": "IntellectualProduct"}, {"text": "PubMed", "type": "IntellectualProduct"}, {"text": "Medline", "type": "IntellectualProduct"}, {"text": "Scopus", "type": "IntellectualProduct"}, {"text": "ScienceDirect", "type": "IntellectualProduct"}, {"text": "ProQuest", "type": "IntellectualProduct"}, {"text": "Google Scholar", "type": "IntellectualProduct"}, {"text": "keywords", "type": "IntellectualProduct"}]}

Input:
Sentence: Literature survey was carried out by using Google , Scholar Google and Pub - Med .

## Item MedMentions:test:2159
Example input:
Sentence: CBCT has a higher diagnostic accuracy than digital and conventional intraoral radiography for detection of secondary caries around composite restorations .

Example answer:
{"entities": [{"text": "CBCT", "type": "HealthCareActivity"}, {"text": "digital", "type": "HealthCareActivity"}, {"text": "conventional intraoral radiography", "type": "HealthCareActivity"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "secondary caries", "type": "BiologicFunction"}, {"text": "composite", "type": "Chemical"}, {"text": "restorations", "type": "HealthCareActivity"}]}

Example input:
Sentence: Artefacts are reduced and CT -like HUs are recovered in the artefact corrected CBCT images .

Example answer:
{"entities": [{"text": "CT", "type": "HealthCareActivity"}, {"text": "CBCT", "type": "HealthCareActivity"}]}

Example input:
Sentence: The method is demonstrated to reduce artefacts and recover CT -like Hounsfield units ( HU ) in reconstructed CBCT images of five lung cancer patients .

Example answer:
{"entities": [{"text": "method", "type": "IntellectualProduct"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "CBCT", "type": "HealthCareActivity"}, {"text": "lung cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Three - dimensional morphological characterization of malocclusions with mandibular lateral displacement using cone - beam computed tomography The purpose of this study was to evaluate the morphologic characteristics of MLD malocclusions using 3D imaging .

Example answer:
{"entities": [{"text": "Three - dimensional", "type": "SpatialConcept"}, {"text": "morphological", "type": "SpatialConcept"}, {"text": "malocclusions", "type": "BiologicFunction"}, {"text": "mandibular lateral displacement", "type": "AnatomicalStructure"}, {"text": "cone - beam computed tomography", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "MLD", "type": "AnatomicalStructure"}, {"text": "3D imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: Visual inspection confirms that artefacts are indeed suppressed by the proposed method , and the HU root mean square difference between reconstructed CBCTs and the reference CT images are reduced by 31 % when using the artefact corrections compared to the standard clinical CBCT reconstruction .

Example answer:
{"entities": [{"text": "Visual inspection", "type": "HealthCareActivity"}, {"text": "confirms", "type": "Finding"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "CBCTs", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "CBCT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Hounsfield unit recovery in clinical cone beam CT images of the thorax acquired for image guided radiation therapy A comprehensive artefact correction method for clinical cone beam CT ( CBCT ) images acquired for image guided radiation therapy ( IGRT ) on a commercial system is presented .

Example answer:
{"entities": [{"text": "cone beam CT", "type": "HealthCareActivity"}, {"text": "thorax", "type": "SpatialConcept"}, {"text": "image guided radiation therapy", "type": "HealthCareActivity"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "CBCT", "type": "HealthCareActivity"}, {"text": "IGRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using eleven lung cancer patient cases , the accuracy of the Bio - CBCT - est technique has been compared to that of the 2D - 3D deformation technique and the traditional CBCT reconstruction techniques .

Example answer:
{"entities": [{"text": "lung cancer", "type": "BiologicFunction"}, {"text": "Bio - CBCT - est", "type": "IntellectualProduct"}, {"text": "technique", "type": "HealthCareActivity"}, {"text": "2D", "type": "SpatialConcept"}, {"text": "3D", "type": "SpatialConcept"}, {"text": "CBCT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Specifically , Bio - CBCT - est first extracts the 2D - 3D deformation -generated displacement vectors at the high - contrast anatomical structure boundaries .

Example answer:
{"entities": [{"text": "Bio - CBCT - est", "type": "IntellectualProduct"}, {"text": "2D", "type": "SpatialConcept"}, {"text": "3D", "type": "SpatialConcept"}, {"text": "displacement", "type": "SpatialConcept"}, {"text": "vectors", "type": "SpatialConcept"}, {"text": "anatomical structure boundaries", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The resulting FEA -corrected deformation fields are then fed back into 2D - 3D deformation to form an iterative loop , combining the benefits of intensity - based deformation and biomechanical modeling for CBCT estimation .

Example answer:
{"entities": [{"text": "FEA", "type": "IntellectualProduct"}, {"text": "2D", "type": "SpatialConcept"}, {"text": "3D", "type": "SpatialConcept"}, {"text": "loop", "type": "SpatialConcept"}, {"text": "modeling", "type": "ResearchActivity"}, {"text": "CBCT", "type": "HealthCareActivity"}, {"text": "estimation", "type": "IntellectualProduct"}]}

Example input:
Sentence: To address these problems , we have developed a biomechanical modeling guided CBCT estimation technique ( Bio - CBCT - est ) by combining 2D - 3D deformation with finite element analysis ( FEA ) - based biomechanical modeling of anatomical structures .

Example answer:
{"entities": [{"text": "modeling", "type": "ResearchActivity"}, {"text": "CBCT", "type": "HealthCareActivity"}, {"text": "estimation technique", "type": "IntellectualProduct"}, {"text": "Bio - CBCT - est", "type": "IntellectualProduct"}, {"text": "2D", "type": "SpatialConcept"}, {"text": "3D", "type": "SpatialConcept"}, {"text": "finite element analysis", "type": "IntellectualProduct"}, {"text": "FEA", "type": "IntellectualProduct"}, {"text": "anatomical structures", "type": "AnatomicalStructure"}]}

Input:
Sentence: A Biomechanical Modeling Guided CBCT Estimation Technique Two - dimensional -to - three - dimensional ( 2D - 3D ) deformation has emerged as a new technique to estimate cone - beam computed tomography ( CBCT ) images .

## Item MedMentions:test:1967
Example input:
Sentence: Ankaflavin and monascin ( 30 μM ) induced apoptosis and significantly inhibited cell growth ( cell viabilities : 80 . 2 ± 5 .

Example answer:
{"entities": [{"text": "Ankaflavin", "type": "Chemical"}, {"text": "monascin", "type": "Chemical"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "cell growth", "type": "BiologicFunction"}, {"text": "cell viabilities", "type": "BiologicFunction"}]}

Example input:
Sentence: By transmission electron microscopy with acridine orange and Cyto - ID®Autophagy detection dyes , Western blot analysis , and RT - PCR assay , we confirmed that delicaflavone induces autophagic cell death by increasing the ratio of LC3 - II to LC3 - I , which are autophagy - related proteins , and promoting the generation of acidic vesicular organelles and autolysosomes in the cytoplasm of human lung cancer A549 and PC - 9 cells in a time - and dose - dependent manner .

Example answer:
{"entities": [{"text": "transmission electron microscopy", "type": "HealthCareActivity"}, {"text": "acridine orange", "type": "Chemical"}, {"text": "Cyto - ID®Autophagy", "type": "BiologicFunction"}, {"text": "dyes", "type": "Chemical"}, {"text": "Western blot", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "RT - PCR assay", "type": "ResearchActivity"}, {"text": "delicaflavone", "type": "Chemical"}, {"text": "autophagic cell death", "type": "BiologicFunction"}, {"text": "LC3 - II", "type": "Chemical"}, {"text": "LC3 - I", "type": "Chemical"}, {"text": "autophagy - related proteins", "type": "Chemical"}, {"text": "acidic vesicular organelles", "type": "AnatomicalStructure"}, {"text": "autolysosomes", "type": "AnatomicalStructure"}, {"text": "cytoplasm", "type": "AnatomicalStructure"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "A549", "type": "AnatomicalStructure"}, {"text": "PC - 9 cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Pharmacological inhibiting of autophagy dramatically potentiated icaritin - induced CRC cell death and apoptosis .

Example answer:
{"entities": [{"text": "autophagy", "type": "BiologicFunction"}, {"text": "icaritin", "type": "Chemical"}, {"text": "CRC", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: shRNA / siRNA -mediated knockdown of AMPKα1 inhibited icaritin - induced autophagy activation , but exacerbated CRC cell death .

Example answer:
{"entities": [{"text": "shRNA", "type": "Chemical"}, {"text": "siRNA", "type": "Chemical"}, {"text": "knockdown", "type": "ResearchActivity"}, {"text": "AMPKα1", "type": "AnatomicalStructure"}, {"text": "icaritin", "type": "Chemical"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "CRC", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}]}

Example input:
Sentence: Ankaflavin and Monascin Induce Apoptosis in Activated Hepatic Stellate Cells through Suppression of the Akt / NF - κB / p38 Signaling Pathway The increased proliferation of activated hepatic stellate cells ( HSCs ) is associated with hepatic fibrosis and excessive extracellular matrix ( ECM ) - protein production .

Example answer:
{"entities": [{"text": "Ankaflavin", "type": "Chemical"}, {"text": "Monascin", "type": "Chemical"}, {"text": "Apoptosis", "type": "BiologicFunction"}, {"text": "Hepatic Stellate Cells", "type": "AnatomicalStructure"}, {"text": "Akt", "type": "Chemical"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "p38", "type": "Chemical"}, {"text": "Signaling Pathway", "type": "BiologicFunction"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "hepatic stellate cells", "type": "AnatomicalStructure"}, {"text": "HSCs", "type": "AnatomicalStructure"}, {"text": "hepatic fibrosis", "type": "BiologicFunction"}, {"text": "extracellular matrix", "type": "AnatomicalStructure"}, {"text": "ECM", "type": "AnatomicalStructure"}, {"text": "protein", "type": "Chemical"}]}

Example input:
Sentence: Meanwhile , shRNA -mediated knockdown of Beclin - 1 or ATG - 5 also sensitized icaritin - induced CRC cell death and apoptosis .

Example answer:
{"entities": [{"text": "shRNA", "type": "Chemical"}, {"text": "knockdown", "type": "ResearchActivity"}, {"text": "Beclin - 1", "type": "AnatomicalStructure"}, {"text": "ATG - 5", "type": "AnatomicalStructure"}, {"text": "icaritin", "type": "Chemical"}, {"text": "CRC", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Collectively , our findings suggest that cucurbitacin B protects against cardiac hypertrophy through increasing the autophagy level in cardiomyocytes , which is associated with the inhibition of Akt / mTOR / FoxO3a signal axis .

Example answer:
{"entities": [{"text": "cucurbitacin B", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "cardiomyocytes", "type": "AnatomicalStructure"}, {"text": "inhibition", "type": "BiologicFunction"}, {"text": "Akt", "type": "Chemical"}, {"text": "mTOR", "type": "Chemical"}, {"text": "FoxO3a", "type": "Chemical"}, {"text": "signal axis", "type": "BiologicFunction"}]}

Example input:
Sentence: Potentiation of LPS - Induced Apoptotic Cell Death in Human Hepatoma HepG2 Cells by Aspirin via ROS and Mitochondrial Dysfunction : Protection by N - Acetyl Cysteine Cytotoxicity and inflammation - associated toxic responses have been observed to be induced by bacterial lipopolysaccharides ( LPS ) in vitro and in vivo respectively .

Example answer:
{"entities": [{"text": "Potentiation", "type": "HealthCareActivity"}, {"text": "LPS", "type": "Chemical"}, {"text": "Induced", "type": "BiologicFunction"}, {"text": "Apoptotic Cell Death", "type": "BiologicFunction"}, {"text": "Human Hepatoma HepG2 Cells", "type": "AnatomicalStructure"}, {"text": "Aspirin", "type": "Chemical"}, {"text": "ROS", "type": "Chemical"}, {"text": "Mitochondrial Dysfunction", "type": "Finding"}, {"text": "N - Acetyl Cysteine", "type": "Chemical"}, {"text": "Cytotoxicity", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "associated", "type": "BiologicFunction"}, {"text": "lipopolysaccharides", "type": "Chemical"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: Besides , oral administration of acacetin showed a potent in vivo anticancer activity in CLL xenograft mouse models .

Example answer:
{"entities": [{"text": "oral administration", "type": "HealthCareActivity"}, {"text": "acacetin", "type": "Chemical"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "anticancer activity", "type": "Finding"}, {"text": "CLL", "type": "BiologicFunction"}, {"text": "xenograft", "type": "Chemical"}, {"text": "mouse models", "type": "BiologicFunction"}]}

Example input:
Sentence: Our in vivo findings indicate that acacetin accumulates and kills CLL B - lymphocyte in a rather selective way through targeting cancerous mitochondria and ROS formation , which ends in CLL therapy .

Example answer:
{"entities": [{"text": "in vivo", "type": "SpatialConcept"}, {"text": "acacetin", "type": "Chemical"}, {"text": "accumulates", "type": "Finding"}, {"text": "kills", "type": "BiologicFunction"}, {"text": "CLL", "type": "BiologicFunction"}, {"text": "B - lymphocyte", "type": "AnatomicalStructure"}, {"text": "cancerous", "type": "BiologicFunction"}, {"text": "mitochondria", "type": "AnatomicalStructure"}, {"text": "ROS", "type": "Chemical"}, {"text": "therapy", "type": "HealthCareActivity"}]}

Input:
Sentence: We have found that acacetin ( 10 μM ) can selectively induce apoptosis on CLL B - lymphocyte ( 25 % at 24 h ) by directly targeting mitochondria , through increased reactive oxygen species ( ROS ) formation , MMP collapse , MPT , release of cytochrome c , caspase 3 activation , and finally apoptosis , while sparing normal healthy B - lymphocytes unaffected at similar concentrations .

## Item MedMentions:test:2285
Example input:
Sentence: Overweight / obesity , hypertension , high blood glucose / diabetes and high cholesterol were significantly more prevalent in older men and women .

Example answer:
{"entities": [{"text": "hypertension", "type": "BiologicFunction"}, {"text": "high blood glucose", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "high cholesterol", "type": "BiologicFunction"}, {"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: I - carriers were significantly less susceptible to hypertension than DD carriers having normal waist / hip ratio ( p = 0 . 007 , OR = 17 . 29 , CI = 1 .

Example answer:
{"entities": [{"text": "I - carriers", "type": "Finding"}, {"text": "hypertension", "type": "BiologicFunction"}, {"text": "DD carriers", "type": "Finding"}]}

Example input:
Sentence: Women with BMI ≤25 kg / m2 have significant differences in androgens , WBC , neutrophils and HOMA - IR and women with BMI ≥25 kg / m2 in androgens , TSH and cortisol according to the presence or not of hyperandrogenemia .

Example answer:
{"entities": [{"text": "Women", "type": "PopulationGroup"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "androgens", "type": "Chemical"}, {"text": "WBC", "type": "AnatomicalStructure"}, {"text": "neutrophils", "type": "AnatomicalStructure"}, {"text": "HOMA - IR", "type": "HealthCareActivity"}, {"text": "women", "type": "PopulationGroup"}, {"text": "TSH", "type": "Chemical"}, {"text": "cortisol", "type": "Chemical"}, {"text": "presence", "type": "Finding"}, {"text": "hyperandrogenemia", "type": "Finding"}]}

Example input:
Sentence: 6 ± 9 . 6 kg / m ( 2 ) , P = .02 ) , but there was no difference between groups in percent body fat , metabolic profile , adipocyte size , resting energy expenditure , hyperphagia score , or ghrelin levels .

Example answer:
{"entities": [{"text": "percent body fat", "type": "Finding"}, {"text": "metabolic profile", "type": "BiologicFunction"}, {"text": "adipocyte", "type": "AnatomicalStructure"}, {"text": "resting energy expenditure", "type": "Finding"}, {"text": "hyperphagia", "type": "Finding"}, {"text": "ghrelin levels", "type": "HealthCareActivity"}]}

Example input:
Sentence: In fully adjusted models , women had higher levels of high - density lipoprotein cholesterol and high - density lipoprotein particle concentration , leptin , d - dimer , homoarginine , and N - terminal pro B - type natriuretic peptide , and lower levels of low - density lipoprotein cholesterol , adiponectin , lipoprotein - associated phospholipase A2 mass and activity , monocyte chemoattractant protein - 1 , soluble endothelial cell adhesion molecule , symmetrical dimethylarginine , asymmetrical dimethylarginine , high - sensitivity troponin T , and cystatin C .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "high - density lipoprotein cholesterol", "type": "Chemical"}, {"text": "high - density lipoprotein particle", "type": "Chemical"}, {"text": "leptin", "type": "Chemical"}, {"text": "d - dimer", "type": "Chemical"}, {"text": "homoarginine", "type": "Chemical"}, {"text": "N - terminal pro B - type natriuretic peptide", "type": "Chemical"}, {"text": "low - density lipoprotein cholesterol", "type": "Chemical"}, {"text": "adiponectin", "type": "Chemical"}, {"text": "lipoprotein", "type": "Chemical"}, {"text": "phospholipase A2", "type": "Chemical"}, {"text": "activity", "type": "BiologicFunction"}, {"text": "monocyte chemoattractant protein - 1", "type": "Chemical"}, {"text": "endothelial cell adhesion molecule", "type": "Chemical"}, {"text": "symmetrical", "type": "Finding"}, {"text": "dimethylarginine", "type": "Chemical"}, {"text": "asymmetrical", "type": "SpatialConcept"}, {"text": "troponin T", "type": "Chemical"}, {"text": "cystatin C", "type": "Chemical"}]}

Example input:
Sentence: Also , plasma lipid profiles , HbA1C , fasting plasma glucose , and insulin levels , will be measured and insulin resistance ( HOMA - IR ) and beta - cell function ( HOMA - B ) will be calculated at baseline and will be repeated at months 3 , 6 , 12 , and 18 .

Example answer:
{"entities": [{"text": "HbA1C", "type": "Chemical"}, {"text": "fasting plasma glucose", "type": "HealthCareActivity"}, {"text": "insulin", "type": "Chemical"}, {"text": "insulin resistance", "type": "HealthCareActivity"}, {"text": "HOMA - IR", "type": "HealthCareActivity"}, {"text": "beta - cell function", "type": "HealthCareActivity"}, {"text": "HOMA - B", "type": "HealthCareActivity"}]}

Example input:
Sentence: Although DD carriers had apparently higher parameters of blood pressure , lipid profile and insulin resistance , only diastolic blood pressure was almost significant ( p = 0 . 057 ) .

Example answer:
{"entities": [{"text": "DD carriers", "type": "Finding"}, {"text": "parameters", "type": "Finding"}, {"text": "blood pressure", "type": "BiologicFunction"}, {"text": "lipid profile", "type": "HealthCareActivity"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "diastolic blood pressure", "type": "ClinicalAttribute"}]}

Example input:
Sentence: To all participants of the study were carried out biochemical analysis of blood , or the analysis of the lipid profile that included total cholesterol , LDL cholesterol , triglycerides ( TG ) and HDL cholesterol , and was determined the values of BMI and waist circumference ( WC ) .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "study", "type": "ResearchActivity"}, {"text": "biochemical analysis of blood", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "lipid", "type": "Chemical"}, {"text": "profile", "type": "HealthCareActivity"}, {"text": "total cholesterol", "type": "Chemical"}, {"text": "LDL cholesterol", "type": "Chemical"}, {"text": "triglycerides", "type": "Chemical"}, {"text": "TG", "type": "Chemical"}, {"text": "HDL cholesterol", "type": "Chemical"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "waist circumference", "type": "ClinicalAttribute"}, {"text": "WC", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Notably , neither waist circumference nor BMI were significant predictors of incident diabetes independent of age , sex and triglycerides .

Example answer:
{"entities": [{"text": "waist circumference", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "triglycerides", "type": "Chemical"}]}

Example input:
Sentence: Participants who developed incident type 2 diabetes were significantly older and had significantly higher body mass index ( BMI ; p = 0 . 012 ) , total cholesterol ( p = 0 . 007 ) , fasting triglycerides ( p < 0 . 001 ) , and Homeostatic Model Assessment of Insulin Resistance ( HOMA - IR ) ( p < 0 .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "type 2 diabetes", "type": "Finding"}, {"text": "significantly older", "type": "PopulationGroup"}, {"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "fasting", "type": "Finding"}, {"text": "triglycerides", "type": "Chemical"}, {"text": "Homeostatic Model Assessment of Insulin Resistance", "type": "HealthCareActivity"}, {"text": "HOMA - IR", "type": "HealthCareActivity"}]}

Input:
Sentence: HbA1c , high - density lipoprotein and triglyceride levels , body mass index , systolic and diastolic blood pressure and waist circumference were not significantly different .

## Item MedMentions:test:2505
Example input:
Sentence: Using recombinant HLA - A * 02 multimers carrying an immunodominant cytomegalovirus peptide ( NLV ) , we have shown that the majority of healthy donors have pronounced T - cell immunity against this antigen , whereas shortly after the transplantation the patients do not have specific T - lymphocytes .

Example answer:
{"entities": [{"text": "HLA - A * 02", "type": "AnatomicalStructure"}, {"text": "cytomegalovirus peptide", "type": "Chemical"}, {"text": "NLV", "type": "Chemical"}, {"text": "T - cell immunity", "type": "BiologicFunction"}, {"text": "antigen", "type": "Chemical"}, {"text": "transplantation", "type": "HealthCareActivity"}, {"text": "T - lymphocytes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Transfusion of the virus - specific donor T - lymphocytes represents an alternative to a highly toxic and often ineffective antiviral therapy .

Example answer:
{"entities": [{"text": "Transfusion", "type": "HealthCareActivity"}, {"text": "donor T - lymphocytes", "type": "AnatomicalStructure"}, {"text": "antiviral therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Rapid transfusion of virus - specific T - cells to patients has several crucial advantages in comparison with methods based on the in vitro expansion of the cells .

Example answer:
{"entities": [{"text": "transfusion", "type": "HealthCareActivity"}, {"text": "virus", "type": "Virus"}, {"text": "T - cells", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Together , our results suggest tissue T cell reservoirs for CMV control shaped by both viral and tissue - intrinsic factors , with global effects on homeostasis of tissue T cells over the lifespan .

Example answer:
{"entities": [{"text": "tissue", "type": "AnatomicalStructure"}, {"text": "T cell", "type": "AnatomicalStructure"}, {"text": "CMV", "type": "Virus"}, {"text": "control", "type": "HealthCareActivity"}, {"text": "intrinsic factors", "type": "Chemical"}, {"text": "homeostasis", "type": "BiologicFunction"}, {"text": "T cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Here , we investigated human CMV -specific T cells , virus persistence and CMV -associated T cell homeostasis in blood , lymphoid , mucosa l and secretory tissues of 44 CMV seropositive and 28 seronegative donors .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "CMV", "type": "Virus"}, {"text": "T cells", "type": "AnatomicalStructure"}, {"text": "virus", "type": "Virus"}, {"text": "T cell", "type": "AnatomicalStructure"}, {"text": "homeostasis", "type": "BiologicFunction"}, {"text": "blood", "type": "BodySubstance"}, {"text": "lymphoid", "type": "AnatomicalStructure"}, {"text": "mucosa", "type": "AnatomicalStructure"}, {"text": "secretory tissues", "type": "AnatomicalStructure"}, {"text": "seronegative", "type": "Finding"}, {"text": "donors", "type": "PopulationGroup"}]}

Example input:
Sentence: This study demonstrated that strong immune response to CMV of healthy donors and prevalence of HLA - A * 02 allele in the Russian population make it possible to isolate a significant number of virus - specific cells using HLA - A * 02 - NLV multimers .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "immune response", "type": "BiologicFunction"}, {"text": "CMV", "type": "Virus"}, {"text": "HLA - A * 02 allele", "type": "AnatomicalStructure"}, {"text": "Russian population", "type": "PopulationGroup"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "HLA - A * 02 - NLV", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Cytomegalovirus ( CMV ) persists in most humans , requires T cell immunity to control , yet tissue immune responses remain undefined .

Example answer:
{"entities": [{"text": "Cytomegalovirus", "type": "Virus"}, {"text": "CMV", "type": "Virus"}, {"text": "humans", "type": "Eukaryote"}, {"text": "T cell immunity", "type": "BiologicFunction"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "immune responses", "type": "BiologicFunction"}]}

Example input:
Sentence: Tissue reservoirs of antiviral T cell immunity in persistent human CMV infection T cell responses to viruses are initiated and maintained in tissue sites ; however , knowledge of human antiviral T cells is largely derived from blood .

Example answer:
{"entities": [{"text": "Tissue", "type": "AnatomicalStructure"}, {"text": "antiviral", "type": "Finding"}, {"text": "T cell immunity", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "CMV infection", "type": "BiologicFunction"}, {"text": "T cell", "type": "AnatomicalStructure"}, {"text": "responses", "type": "BiologicFunction"}, {"text": "viruses", "type": "Virus"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "T cells", "type": "AnatomicalStructure"}, {"text": "blood", "type": "BodySubstance"}]}

Example input:
Sentence: Potentially promising cell therapy approach comprises transfusion of cytotoxic T - lymphocytes , specific to the viral antigens , immediately after their isolation from the donor 's blood circulation without any in vitro expansion .

Example answer:
{"entities": [{"text": "cell therapy", "type": "HealthCareActivity"}, {"text": "transfusion", "type": "HealthCareActivity"}, {"text": "cytotoxic T - lymphocytes", "type": "AnatomicalStructure"}, {"text": "viral antigens", "type": "Chemical"}, {"text": "isolation", "type": "HealthCareActivity"}, {"text": "donor 's blood circulation", "type": "BiologicFunction"}]}

Example input:
Sentence: Recombinant MHC Tetramers for Isolation of Virus - Specific CD8 ( + ) Cells from Healthy Donors : Potential Approach for Cell Therapy of Posttransplant Cytomegalovirus Infection Patients undergoing allogeneic hematopoietic stem cell transplantation have a high risk of cytomegalovirus reactivation , which in the absence of T - cell immunity can result in the development of an acute inflammatory reaction and damage of internal organs .

Example answer:
{"entities": [{"text": "MHC Tetramers", "type": "AnatomicalStructure"}, {"text": "Isolation", "type": "HealthCareActivity"}, {"text": "Virus", "type": "Virus"}, {"text": "CD8 ( + ) Cells", "type": "AnatomicalStructure"}, {"text": "Cell Therapy", "type": "HealthCareActivity"}, {"text": "Posttransplant Cytomegalovirus Infection", "type": "BiologicFunction"}, {"text": "hematopoietic stem cell transplantation", "type": "HealthCareActivity"}, {"text": "cytomegalovirus reactivation", "type": "BiologicFunction"}, {"text": "T - cell immunity", "type": "BiologicFunction"}, {"text": "acute inflammatory reaction", "type": "Finding"}, {"text": "damage of internal organs", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: After the transfusion , these cells should protect patients from CMV without development of allogeneic immune response .

## Item MedMentions:test:2272
Example input:
Sentence: In vitro and in vivo characterization of anodised zirconium as a potential material for biomedical applications In vitro studies offer the insights for the understanding of the mechanisms at the tissue - implant interface that will provide an effective functioning in vivo .

Example answer:
{"entities": [{"text": "in vivo", "type": "SpatialConcept"}, {"text": "anodised zirconium", "type": "Chemical"}, {"text": "material", "type": "Chemical"}, {"text": "biomedical", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "tissue - implant interface", "type": "SpatialConcept"}]}

Example input:
Sentence: After a healing period of 4 weeks , Ti - Nb - Zr - Ta - Si alloy implants showed significantly higher mineral apposition rate compared to commercially pure titanium implants ( P < 0 . 05 ) , whereas there was no significant difference between Ti - Nb - Zr - Ta - Si alloy implants and commercially pure titanium implants ( P > 0 . 05 ) at 8 weeks .

Example answer:
{"entities": [{"text": "healing", "type": "BiologicFunction"}, {"text": "Ti - Nb - Zr - Ta - Si alloy", "type": "Chemical"}, {"text": "implants", "type": "MedicalDevice"}, {"text": "titanium", "type": "Chemical"}, {"text": "no significant", "type": "Finding"}]}

Example input:
Sentence: This could be achieved using optimized electrochemical anodic oxidation ( anodizing ) and heat treatment processes .

Example answer:
{"entities": []}

Example input:
Sentence: Comparison of alkaline phosphatase activity of MC3T3 - E1 cells cultured on different Ti surfaces : modified sandblasted with large grit and acid - etched ( MSLA ) , laser - treated , and laser and acid - treated Ti surfaces In this study , the aim of this study was to evaluate the effect of implant surface treatment on cell differentiation of osteoblast cells .

Example answer:
{"entities": [{"text": "alkaline phosphatase activity", "type": "BiologicFunction"}, {"text": "MC3T3 - E1 cells", "type": "AnatomicalStructure"}, {"text": "Ti", "type": "Chemical"}, {"text": "surfaces", "type": "SpatialConcept"}, {"text": "grit", "type": "Chemical"}, {"text": "MSLA", "type": "Chemical"}, {"text": "study", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "cell differentiation", "type": "BiologicFunction"}, {"text": "osteoblast cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Second , an anodic oxidation was applied to fabricate zirconia nanotubular arrays .

Example answer:
{"entities": [{"text": "anodic oxidation", "type": "BiologicFunction"}, {"text": "zirconia", "type": "Chemical"}, {"text": "arrays", "type": "SpatialConcept"}]}

Example input:
Sentence: The results demonstrated the formation of amorphous nanostructured titanium oxide after anodizing , which transformed to crystalline anatase and rutile phases upon heat treatment .

Example answer:
{"entities": [{"text": "titanium oxide", "type": "Chemical"}, {"text": "crystalline", "type": "Chemical"}, {"text": "anatase", "type": "Chemical"}, {"text": "rutile", "type": "Chemical"}]}

Example input:
Sentence: It was found that anodisation treatment at 60V enhanced cell spreading and the osteoblastic and osteoclastic cells morphology , showing a strong dependence on the surface characteristics .

Example answer:
{"entities": [{"text": "cell spreading", "type": "BiologicFunction"}, {"text": "surface", "type": "SpatialConcept"}]}

Example input:
Sentence: The results indicate that anodising treatment at 60V could be an effective improvement in the osseointegration of zirconium by stimulating adhesion , proliferation , morphology , new bone thickness and bone mineral apposition , making zirconium an emerging candidate material for biomedical applications .

Example answer:
{"entities": [{"text": "osseointegration", "type": "BiologicFunction"}, {"text": "zirconium", "type": "Chemical"}, {"text": "adhesion", "type": "BiologicFunction"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "bone", "type": "AnatomicalStructure"}, {"text": "mineral apposition", "type": "BiologicFunction"}, {"text": "material", "type": "Chemical"}, {"text": "biomedical", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: The aim of this study was to create a nanostructured surface oxide layer on irregularly shaped titanium granules to improve their bioactivity .

Example answer:
{"entities": [{"text": "surface", "type": "SpatialConcept"}, {"text": "shaped", "type": "SpatialConcept"}, {"text": "titanium granules", "type": "Chemical"}]}

Example input:
Sentence: Surface Modification of Porous Titanium Granules for Improving Bioactivity The highly porous titanium granules are currently being used as bone substitute material and for bone tissue augmentation .

Example answer:
{"entities": [{"text": "Surface", "type": "SpatialConcept"}, {"text": "Modification", "type": "Finding"}, {"text": "Porous Titanium Granules", "type": "Chemical"}, {"text": "porous titanium granules", "type": "Chemical"}, {"text": "bone substitute material", "type": "Chemical"}, {"text": "bone tissue", "type": "AnatomicalStructure"}, {"text": "augmentation", "type": "HealthCareActivity"}]}

Input:
Sentence: It is suggested that anodic oxidation followed by heat treatment could be used as an effective surface treatment procedure to improve bioactivity of titanium granules implemented for bone tissue repair and augmentation .
