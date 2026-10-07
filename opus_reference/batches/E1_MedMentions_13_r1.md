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

## Item MedMentions:test:2791
Example input:
Sentence: Compound 1 exhibited significant inhibition on NO production with an IC50 value of 9 .

Example answer:
{"entities": [{"text": "Compound 1", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}]}

Example input:
Sentence: The change of CDR - SB from baseline to 2 years exhibited significant negative associations with the average ( β = -0 . 150 , p = 0 . 006 ) and minimum GCIPL thicknesses as well as GCIPL thickness in the superotemporal , superior , superonasal , and inferonasal sectors at baseline .

Example answer:
{"entities": [{"text": "CDR - SB", "type": "IntellectualProduct"}, {"text": "negative", "type": "Finding"}, {"text": "minimum GCIPL", "type": "AnatomicalStructure"}, {"text": "GCIPL", "type": "AnatomicalStructure"}, {"text": "superotemporal", "type": "SpatialConcept"}, {"text": "superior", "type": "SpatialConcept"}, {"text": "superonasal", "type": "SpatialConcept"}, {"text": "inferonasal sectors", "type": "SpatialConcept"}]}

Example input:
Sentence: A comparison of γH2AX and 53BP1 quantifications in double - staine d biopsies showed similar HRS dose - response relationships .

Example answer:
{"entities": [{"text": "γH2AX", "type": "AnatomicalStructure"}, {"text": "53BP1", "type": "AnatomicalStructure"}, {"text": "biopsies", "type": "HealthCareActivity"}]}

Example input:
Sentence: 99mg / mL ) and DPPH assay ( 88 . 65 % , EC50 = 212 . 33μg / ml ) .

Example answer:
{"entities": [{"text": "DPPH", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: To determine optimal concentration , B - CSM was firstly added at varying amounts ( 5 , 10 , 20 , 40 , and 60 % ) relative to culture medium .

Example answer:
{"entities": [{"text": "B - CSM", "type": "Chemical"}, {"text": "culture medium", "type": "Chemical"}]}

Example input:
Sentence: Median creatinine and eGFR were 67 μmol / L and 112 mL / min / 1 . 73 m2 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "eGFR", "type": "HealthCareActivity"}]}

Example input:
Sentence: There was no significant effect on PAM - 13 ( estimated mean difference ( emd ) -0 . 41 , 95 % CI ( CI ) : - 7 . 49 - 6 . 67 ) , nor on the RAS ( emd 0 . 02 , CI : - 0 . 27 - 0 . 31 ) or BASIS - 32 ( 0 . 09 , CI : - 0 . 28 - 0 . 45 ) .

Example answer:
{"entities": [{"text": "PAM - 13", "type": "IntellectualProduct"}, {"text": "RAS", "type": "IntellectualProduct"}, {"text": "BASIS - 32", "type": "IntellectualProduct"}]}

Example input:
Sentence: In DEXCHNP , the IC50 was 20 . 12 μg / ml for HEK and 7 . 37 μg / ml for RAW264 .

Example answer:
{"entities": [{"text": "HEK", "type": "AnatomicalStructure"}, {"text": "RAW264 .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Preliminary pharmacokinetic studies with EC508 used intravenous and oral administration in male rats .

Example answer:
{"entities": [{"text": "pharmacokinetic studies", "type": "ResearchActivity"}, {"text": "EC508", "type": "Chemical"}, {"text": "intravenous", "type": "SpatialConcept"}, {"text": "oral administration", "type": "HealthCareActivity"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: Lastly , the authors constructed a nonlinear dose - response numerical model for these synoptic sediment PCB concentrations and biological effects : Y = 100 / 1 + 10 ( ( [ logEC50 - logX ] × [ Hill slope ] ) ) ( EC50 = median effective concentration ) .

Example answer:
{"entities": [{"text": "dose - response numerical model", "type": "IntellectualProduct"}, {"text": "PCB", "type": "Chemical"}]}

Input:
Sentence: Median effect concentrations ( EC50s ) for B .

## Item MedMentions:test:2732
Example input:
Sentence: The functional and aesthetic assessments were performed at least 6 months after surgery , and the results were compared statistically with a control group .

Example answer:
{"entities": [{"text": "assessments", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: 2 years ) , 29 . 0 % ( 20 / 69 ) of patients had recurrence and 18 . 8 % ( 13 / 69 ) required reoperation at median time of 4 . 8 years ( 3 . 1 - 9 . 1 years ) after the initial repair .

Example answer:
{"entities": [{"text": "recurrence", "type": "BiologicFunction"}, {"text": "reoperation", "type": "HealthCareActivity"}, {"text": "initial repair", "type": "HealthCareActivity"}]}

Example input:
Sentence: Clinical evaluations showed that all photoaging parameters improved significantly from baseline as early as Week 12 and the amelioration continued until Week 52 .

Example answer:
{"entities": [{"text": "Clinical evaluations", "type": "HealthCareActivity"}, {"text": "photoaging", "type": "InjuryOrPoisoning"}, {"text": "parameters", "type": "Finding"}]}

Example input:
Sentence: Both patients fully recovered and both showed a complete relief of symptoms at 3 months following the procedure .

Example answer:
{"entities": [{"text": "relief", "type": "Finding"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: 4 ; 95 % CI , -8 . 1 to -2 . 6 ; P < .001 ) , and the treatment effect was maintained for at least 12 months ( -15 . 4 vs -11 .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The median OS for the patients treated in the TKI era was 22 months ( 95 % confidence interval [ CI ] , 17 - 25 months ) compared with 14 months ( 95 % CI , 10 - 19 months ; P < .01 ) for the historical controls .

Example answer:
{"entities": [{"text": "treated", "type": "HealthCareActivity"}, {"text": "TKI", "type": "Chemical"}, {"text": "historical controls", "type": "PopulationGroup"}]}

Example input:
Sentence: Further improvements were detected at 24 months ( AOFAS , from 57 . 1 ± 14 . 9 before surgery to 86 . 6 ± 10 .

Example answer:
{"entities": [{"text": "AOFAS", "type": "IntellectualProduct"}]}

Example input:
Sentence: During the median 21 . 5 months follow - up ( range , 3 - 119 months ) , 36 ( 76 . 6 % ) patients showed good outcomes ( improved to below BNI class IIIa ) .

Example answer:
{"entities": [{"text": "median", "type": "SpatialConcept"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "class IIIa", "type": "IntellectualProduct"}]}

Example input:
Sentence: At the 36 - month follow - up examination , there was continual evidence of satisfactory reduction and fusion .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "examination", "type": "HealthCareActivity"}, {"text": "satisfactory", "type": "Finding"}, {"text": "reduction", "type": "HealthCareActivity"}, {"text": "fusion", "type": "HealthCareActivity"}]}

Example input:
Sentence: Successful Restoration of Severely Mutilated Primary Incisors Using a Novel Method to Retain Zirconia Crowns - Two Year Results This manuscript describes a simple reliable technique for restoring severely mutilated primary anterior teeth .

Example answer:
{"entities": [{"text": "Successful Restoration", "type": "HealthCareActivity"}, {"text": "Primary Incisors", "type": "AnatomicalStructure"}, {"text": "Crowns", "type": "MedicalDevice"}, {"text": "manuscript", "type": "IntellectualProduct"}, {"text": "restoring", "type": "HealthCareActivity"}, {"text": "primary anterior teeth", "type": "AnatomicalStructure"}]}

Input:
Sentence: Restorations were evaluated at baseline and at 6 , 12 , 18 , and 24 months by two blinded independent examiners using modified FDI criteria .

## Item MedMentions:test:2697
Example input:
Sentence: Using data obtained by the Surveillance , Epidemiology , and End Results ( SEER ) program from 2010 - 2012 , a retrospective , population - based cohort study was conducted to investigate tumor subtype - specific differences in various characteristics , overall survival ( OS ) and breast cancer - specific mortality ( BCSM ) between males and females .

Example answer:
{"entities": [{"text": "Surveillance , Epidemiology , and End Results ( SEER ) program", "type": "Organization"}, {"text": "population - based cohort study", "type": "ResearchActivity"}, {"text": "tumor subtype", "type": "IntellectualProduct"}]}

Example input:
Sentence: The breast cancer mortality reduction in the invited population due to screening and the percentage of females diagnosed with symptomatic breast cancer , who die from breast cancer , were collated from the literature .

Example answer:
{"entities": [{"text": "breast cancer", "type": "BiologicFunction"}, {"text": "invited population", "type": "PopulationGroup"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "diagnosed", "type": "Finding"}, {"text": "literature", "type": "IntellectualProduct"}]}

Example input:
Sentence: Given the higher prevalence and earlier onset of type 2 diabetes in Black women , it is likely that diabetes contributes to racial disparities in breast cancer mortality .

Example answer:
{"entities": [{"text": "earlier onset", "type": "Finding"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "Black women", "type": "PopulationGroup"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "racial", "type": "PopulationGroup"}, {"text": "disparities", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Among 228 , 511 women identified , the percentage of blacks with stage IIIC / IV disease at diagnosis was nearly twice that of non - Hispanic whites ( 17 . 8 % vs 9 . 8 % ; P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "blacks", "type": "PopulationGroup"}, {"text": "stage IIIC / IV disease at diagnosis", "type": "IntellectualProduct"}, {"text": "non - Hispanic whites", "type": "PopulationGroup"}]}

Example input:
Sentence: Overall , breast cancer was detected in 543 women , with a detection rate of 10 . 3 per 1 , 000 persons .

Example answer:
{"entities": [{"text": "breast cancer", "type": "BiologicFunction"}, {"text": "detected", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "persons", "type": "PopulationGroup"}]}

Example input:
Sentence: Women with resectable breast cancer from 1990 to 2007 in the Surveillance , Epidemiology , and End Results database ( n = 199 , 963 ) were analyzed .

Example answer:
{"entities": [{"text": "Women", "type": "PopulationGroup"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "Surveillance , Epidemiology , and End Results database", "type": "Organization"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: We examined factors associated with negative psychological consequences of a breast cancer diagnosis , in a diverse sample of 910 recently diagnosed patients ( 378 African - American , 372 White , and 160 Latina ) .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "negative", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "diagnosed", "type": "Finding"}, {"text": "African - American", "type": "PopulationGroup"}, {"text": "White", "type": "PopulationGroup"}, {"text": "Latina", "type": "PopulationGroup"}]}

Example input:
Sentence: There were 368 deaths during follow - up , of which 273 were due to breast cancer .

Example answer:
{"entities": [{"text": "deaths", "type": "Finding"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Diabetes and breast cancer mortality in Black women Breast cancer mortality is higher in Black women than in White women .

Example answer:
{"entities": [{"text": "Diabetes", "type": "BiologicFunction"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "Black women", "type": "PopulationGroup"}, {"text": "Breast cancer", "type": "BiologicFunction"}, {"text": "White women", "type": "PopulationGroup"}]}

Example input:
Sentence: African - American and Latina women reported greater psychological consequences related to their breast cancer diagnosis ; this disparity was mediated by differences in unmet social support .

Example answer:
{"entities": [{"text": "African - American", "type": "PopulationGroup"}, {"text": "Latina", "type": "SpatialConcept"}, {"text": "women", "type": "PopulationGroup"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "disparity", "type": "Finding"}]}

Input:
Sentence: 1 , 621 Black women with invasive breast cancer diagnosed in 1995 - 2013 were followed by mailed questionnaires and searches of the National Death Index .

## Item MedMentions:test:2630
Example input:
Sentence: LAMP - 2 mediates oxidative stress -dependent cell death in Zn ( 2 + ) - treated lung epithelium cells Zinc is an essential element for the biological system .

Example answer:
{"entities": [{"text": "LAMP - 2", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "Zn ( 2 + )", "type": "Chemical"}, {"text": "treated", "type": "HealthCareActivity"}, {"text": "lung", "type": "AnatomicalStructure"}, {"text": "epithelium cells", "type": "AnatomicalStructure"}, {"text": "Zinc", "type": "Chemical"}, {"text": "element", "type": "Chemical"}, {"text": "biological system", "type": "BodySystem"}]}

Example input:
Sentence: To investigate thiamine 's role in symbiosis , we focused on THI1 , a thiamine - biosynthesis gene expressed in roots , nodules , and seeds .

Example answer:
{"entities": [{"text": "thiamine 's", "type": "Chemical"}, {"text": "THI1", "type": "AnatomicalStructure"}, {"text": "thiamine - biosynthesis gene", "type": "AnatomicalStructure"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "roots", "type": "Eukaryote"}, {"text": "nodules", "type": "Eukaryote"}, {"text": "seeds", "type": "Eukaryote"}]}

Example input:
Sentence: Despite robust activation of the intestinal innate immune response , mice lacking acinar Orai1 exhibited intestinal bacterial outgrowth and dysbiosis , ultimately causing systemic translocation , inflammation , and death .

Example answer:
{"entities": [{"text": "activation of the intestinal innate immune response", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "acinar", "type": "SpatialConcept"}, {"text": "Orai1", "type": "AnatomicalStructure"}, {"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "outgrowth", "type": "BiologicFunction"}, {"text": "translocation", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "death", "type": "BiologicFunction"}]}

Example input:
Sentence: irregularis stored more thiamine than the source ( host plants ) , despite lacking thiamine biosynthesis genes .

Example answer:
{"entities": [{"text": "irregularis", "type": "Eukaryote"}, {"text": "thiamine", "type": "Chemical"}, {"text": "thiamine biosynthesis genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In particular , C9orf72 depletion leads to reduced activity of MTOR , a negative regulator of macroautophagy / autophagy , and concomitantly increased TFEB levels and nuclear translocation .

Example answer:
{"entities": [{"text": "C9orf72", "type": "AnatomicalStructure"}, {"text": "MTOR", "type": "Chemical"}, {"text": "macroautophagy", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "TFEB", "type": "Chemical"}, {"text": "nuclear translocation", "type": "BiologicFunction"}]}

Example input:
Sentence: Argininosuccinic Acid Lyase Deficiency Missed by Newborn Screen Argininosuccinic acid lyase ( ASL ) deficiency , caused by mutations in the ASL gene ( OMIM : 608310 ) is a urea cycle disorder that has pleiotropic presentations .

Example answer:
{"entities": [{"text": "Argininosuccinic Acid Lyase Deficiency", "type": "BiologicFunction"}, {"text": "Newborn Screen", "type": "HealthCareActivity"}, {"text": "Argininosuccinic acid lyase ( ASL ) deficiency", "type": "BiologicFunction"}, {"text": "mutations", "type": "BiologicFunction"}, {"text": "ASL gene", "type": "AnatomicalStructure"}, {"text": "OMIM : 608310", "type": "IntellectualProduct"}, {"text": "urea cycle", "type": "BiologicFunction"}, {"text": "disorder", "type": "BiologicFunction"}, {"text": "pleiotropic presentations", "type": "BiologicFunction"}]}

Example input:
Sentence: Cyclic nucleotide signaling is impaired in HD models , and PDE10 loss may represent a homeostatic adaptation to maintain signaling .

Example answer:
{"entities": [{"text": "Cyclic nucleotide signaling", "type": "BiologicFunction"}, {"text": "HD", "type": "BiologicFunction"}, {"text": "models", "type": "BiologicFunction"}, {"text": "PDE10", "type": "Chemical"}, {"text": "homeostatic", "type": "BiologicFunction"}, {"text": "adaptation", "type": "BiologicFunction"}, {"text": "signaling", "type": "BiologicFunction"}]}

Example input:
Sentence: These phenotypes were rescued by THI1 complementation and by exogenous thiamine .

Example answer:
{"entities": [{"text": "THI1", "type": "AnatomicalStructure"}, {"text": "thiamine", "type": "Chemical"}]}

Example input:
Sentence: Therefore , disturbance of the thiamine supply would affect progeny phenotypes such as spore formation and hyphal growth .

Example answer:
{"entities": [{"text": "thiamine", "type": "Chemical"}, {"text": "spore formation", "type": "BiologicFunction"}, {"text": "hyphal growth", "type": "BiologicFunction"}]}

Example input:
Sentence: Binding of Pollutants to Biomolecules : A Simulation Study A number of cases around the world have been reported where animals were found dead or dying with symptoms resembling a thiamine ( vitamin B ) deficiency , and for some of these , a link to pollutants has been suggested .

Example answer:
{"entities": [{"text": "Pollutants", "type": "Chemical"}, {"text": "Biomolecules", "type": "Chemical"}, {"text": "Simulation Study", "type": "ResearchActivity"}, {"text": "world", "type": "PopulationGroup"}, {"text": "animals", "type": "Eukaryote"}, {"text": "found dead", "type": "Finding"}, {"text": "dying", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "thiamine", "type": "BiologicFunction"}, {"text": "( vitamin B ) deficiency", "type": "BiologicFunction"}, {"text": "pollutants", "type": "Chemical"}]}

Input:
Sentence: Loss of function produces chlorosis , a typical thiamine -deficiency phenotype , and mortality .

## Item MedMentions:test:2628
Example input:
Sentence: EphB1 receptor may be a potential target for relieving the established diabetic pain .

Example answer:
{"entities": [{"text": "EphB1 receptor", "type": "Chemical"}, {"text": "relieving", "type": "HealthCareActivity"}, {"text": "diabetic", "type": "Finding"}, {"text": "pain", "type": "Finding"}]}

Example input:
Sentence: Further , rPbHsp60 treatment ( i ) decreased the known protective effect of CFA against PCM and ( ii ) increased the concentrations of IL - 17 , TNF - α , IL - 12 , IFN - γ , IL - 4 , IL - 10 , and TGF - β in the lungs .

Example answer:
{"entities": [{"text": "rPbHsp60", "type": "Chemical"}, {"text": "CFA", "type": "Chemical"}, {"text": "PCM", "type": "BiologicFunction"}, {"text": "IL - 17", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "IL - 12", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "IL - 4", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "TGF - β", "type": "Chemical"}, {"text": "lungs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Finally , we demonstrate that CBG upregulates gene expression of the antimicrobial peptides ( AMPs ) hBD - 2 and hBD - 3 in DCs , and induces secretion of HNP1 - 3 and hCAP - 18 / LL - 37 from neutrophils , potentiating neutrophil antibacterial activity .

Example answer:
{"entities": [{"text": "CBG", "type": "Chemical"}, {"text": "upregulates", "type": "BiologicFunction"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "antimicrobial peptides", "type": "Chemical"}, {"text": "AMPs", "type": "Chemical"}, {"text": "hBD - 2", "type": "Chemical"}, {"text": "hBD - 3", "type": "Chemical"}, {"text": "DCs", "type": "AnatomicalStructure"}, {"text": "secretion", "type": "BiologicFunction"}, {"text": "HNP1", "type": "Chemical"}, {"text": "3", "type": "Chemical"}, {"text": "hCAP - 18 / LL - 37", "type": "Chemical"}, {"text": "neutrophils", "type": "AnatomicalStructure"}, {"text": "neutrophil", "type": "AnatomicalStructure"}, {"text": "antibacterial activity", "type": "BiologicFunction"}]}

Example input:
Sentence: Peptide -based vaccination against OPN integrin binding sites does not improve cardio - metabolic disease in mice Obesity causes insulin resistance via a chronic low - grade inflammation .

Example answer:
{"entities": [{"text": "Peptide", "type": "Chemical"}, {"text": "vaccination", "type": "HealthCareActivity"}, {"text": "OPN", "type": "Chemical"}, {"text": "integrin", "type": "Chemical"}, {"text": "binding sites", "type": "Chemical"}, {"text": "cardio - metabolic disease", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "Obesity", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}]}

Example input:
Sentence: In particular , we discuss the possible contribution to the incretin cardiovascular effects of a direct cardiac action of GLP - 1 metabolites through GLP - 1 receptor -independent pathways , and of DPP4 substrates other than GLP - 1 .

Example answer:
{"entities": [{"text": "incretin", "type": "Chemical"}, {"text": "cardiovascular", "type": "BodySystem"}, {"text": "cardiac", "type": "AnatomicalStructure"}, {"text": "GLP - 1", "type": "Chemical"}, {"text": "metabolites", "type": "Chemical"}, {"text": "GLP - 1 receptor", "type": "Chemical"}, {"text": "pathways", "type": "BiologicFunction"}, {"text": "DPP4", "type": "Chemical"}]}

Example input:
Sentence: All patients who presented with lower urinary tract symptoms due to BPH and who met the inclusion criteria were studied .

Example answer:
{"entities": [{"text": "lower urinary tract symptoms", "type": "Finding"}, {"text": "BPH", "type": "BiologicFunction"}, {"text": "studied", "type": "ResearchActivity"}]}

Example input:
Sentence: BaPWV was positively correlated with age , systolic blood pressure ( SBP ) , diastolic blood pressure ( DBP ) , 2 - hour ( OGTT ) insulin , RBP4 , and VFA , and negatively correlated with GIR in FH2D + group .

Example answer:
{"entities": [{"text": "systolic blood pressure", "type": "ClinicalAttribute"}, {"text": "SBP", "type": "ClinicalAttribute"}, {"text": "diastolic blood pressure", "type": "ClinicalAttribute"}, {"text": "DBP", "type": "ClinicalAttribute"}, {"text": "RBP4", "type": "Chemical"}, {"text": "FH2D +", "type": "Finding"}, {"text": "group", "type": "PopulationGroup"}]}

Example input:
Sentence: Pharmacological Actions of Glucagon - Like Peptide - 1 , Gastric Inhibitory Polypeptide , and Glucagon Glucagon family of peptide hormones is a group of structurally related brain - gut peptides that exert their pleiotropic actions through interactions with unique members of class B1 G protein - coupled receptors ( GPCRs ) .

Example answer:
{"entities": [{"text": "Pharmacological Actions", "type": "BiologicFunction"}, {"text": "Glucagon - Like Peptide - 1", "type": "Chemical"}, {"text": "Gastric Inhibitory Polypeptide", "type": "Chemical"}, {"text": "Glucagon", "type": "Chemical"}, {"text": "Glucagon family", "type": "Chemical"}, {"text": "peptide hormones", "type": "Chemical"}, {"text": "brain - gut peptides", "type": "Chemical"}, {"text": "pleiotropic actions", "type": "BiologicFunction"}, {"text": "unique members of class B1", "type": "IntellectualProduct"}, {"text": "G protein - coupled receptors", "type": "Chemical"}, {"text": "GPCRs", "type": "Chemical"}]}

Example input:
Sentence: GLP - 1r blockade prevented hypoglycaemia in 100 % of individuals , normalised beta cell function and reversed neuroglycopenic symptoms , supporting the conclusion that GLP - 1 plays a primary role in mediating hyperinsulinaemic hypoglycaemia in PBH .

Example answer:
{"entities": [{"text": "GLP - 1r", "type": "Chemical"}, {"text": "hypoglycaemia", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "beta cell function", "type": "BiologicFunction"}, {"text": "reversed neuroglycopenic symptoms", "type": "Finding"}, {"text": "GLP - 1", "type": "Chemical"}, {"text": "hyperinsulinaemic hypoglycaemia", "type": "BiologicFunction"}, {"text": "PBH", "type": "BiologicFunction"}]}

Example input:
Sentence: We conducted a double - blinded crossover study wherein eight participants with confirmed PBH were assigned in random order to intravenous infusion of the GLP - 1 receptor ( GLP - 1r ) antagonist .

Example answer:
{"entities": [{"text": "double - blinded", "type": "ResearchActivity"}, {"text": "crossover study", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "PBH", "type": "BiologicFunction"}, {"text": "intravenous infusion", "type": "HealthCareActivity"}, {"text": "GLP - 1 receptor", "type": "Chemical"}, {"text": "GLP - 1r", "type": "Chemical"}, {"text": "antagonist", "type": "Chemical"}]}

Input:
Sentence: This study was designed to test the hypothesis that PBH and associated symptoms are primarily mediated by glucagon - like peptide - 1 ( GLP - 1 ) .

## Item MedMentions:test:2740
Example input:
Sentence: We hypothesized that it would also be favorable as a laparoscopic application due to unique features .

Example answer:
{"entities": [{"text": "laparoscopic application", "type": "SpatialConcept"}]}

Example input:
Sentence: Further studies will help to refine and determine the benefits of standardized protocols such as that developed in this study for the management of life - threatening laparoscopic complications .

Example answer:
{"entities": [{"text": "standardized protocols", "type": "IntellectualProduct"}, {"text": "management", "type": "HealthCareActivity"}, {"text": "life - threatening", "type": "Finding"}, {"text": "laparoscopic", "type": "HealthCareActivity"}, {"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: The Effectiveness of a Systematic Algorithm for the Management of Vascular Injuries during the Laparoscopic Surgery Currently , there is no standardized training protocol to teach surgeons how to deal with vascular injuries during laparoscopic procedures .

Example answer:
{"entities": [{"text": "Systematic Algorithm", "type": "IntellectualProduct"}, {"text": "Management", "type": "HealthCareActivity"}, {"text": "Vascular Injuries", "type": "InjuryOrPoisoning"}, {"text": "Laparoscopic Surgery", "type": "HealthCareActivity"}, {"text": "training protocol", "type": "IntellectualProduct"}, {"text": "surgeons", "type": "ProfessionalOrOccupationalGroup"}, {"text": "vascular injuries", "type": "InjuryOrPoisoning"}, {"text": "laparoscopic procedures", "type": "HealthCareActivity"}]}

Example input:
Sentence: Future studies should focus on longer - term durability and comparisons with laparoscopic techniques .

Example answer:
{"entities": [{"text": "longer - term durability", "type": "Finding"}, {"text": "laparoscopic techniques", "type": "HealthCareActivity"}]}

Example input:
Sentence: Introducing enhanced haptic feedback in laparoscopic instruments might well improve surgical safety and efficiency .

Example answer:
{"entities": [{"text": "laparoscopic instruments", "type": "MedicalDevice"}, {"text": "improve", "type": "Finding"}]}

Example input:
Sentence: Therefore , haptic feedback is considered an unmet need in laparoscopy .

Example answer:
{"entities": [{"text": "laparoscopy", "type": "HealthCareActivity"}]}

Example input:
Sentence: The questionnaire was distributed to a group of laparoscopic surgeons based in Europe .

Example answer:
{"entities": [{"text": "questionnaire", "type": "IntellectualProduct"}, {"text": "laparoscopic surgeons", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Europe", "type": "SpatialConcept"}]}

Example input:
Sentence: A questionnaire was designed to determine surgeons ' use and preferences for laparoscopic instruments and expectations about enhanced haptic feedback .

Example answer:
{"entities": [{"text": "questionnaire", "type": "IntellectualProduct"}, {"text": "surgeons '", "type": "ProfessionalOrOccupationalGroup"}, {"text": "laparoscopic instruments", "type": "MedicalDevice"}]}

Example input:
Sentence: Surgeons were also asked whether they experience physical complaints related to laparoscopic instruments .

Example answer:
{"entities": [{"text": "Surgeons", "type": "ProfessionalOrOccupationalGroup"}, {"text": "laparoscopic instruments", "type": "MedicalDevice"}]}

Example input:
Sentence: Of all respondents , 77 % reported physical complaints directly attributable to the use of laparoscopic instruments .

Example answer:
{"entities": [{"text": "respondents", "type": "PopulationGroup"}, {"text": "laparoscopic instruments", "type": "MedicalDevice"}]}

Input:
Sentence: This study stresses that the high prevalence of physical complaints directly related to laparoscopic instruments among laparoscopic surgeons is still relevant .

## Item MedMentions:test:2872
Example input:
Sentence: Data from a multiple baseline design indicated that all children acquired the targeted skills and demonstrated high levels of generalization of these skills to untrained context .

Example answer:
{"entities": [{"text": "baseline design", "type": "ResearchActivity"}, {"text": "generalization", "type": "BiologicFunction"}, {"text": "untrained", "type": "Finding"}]}

Example input:
Sentence: Although a positive perception of their educational environment was found , minor corrective measures need to be implemented .

Example answer:
{"entities": [{"text": "perception", "type": "BiologicFunction"}]}

Example input:
Sentence: Other highly prevalent strategies in the school context include Search for Information , Emotion , and Social Support .

Example answer:
{"entities": [{"text": "Emotion", "type": "BiologicFunction"}]}

Example input:
Sentence: The vast majority of service providers ( 93 . 4 % ) reported that ENGAGE had impacted their work practice up to 5 - month post training .

Example answer:
{"entities": [{"text": "reported", "type": "HealthCareActivity"}, {"text": "ENGAGE", "type": "Organization"}]}

Example input:
Sentence: Multivariable regression analyses examined student , family , and school factors affecting engagement .

Example answer:
{"entities": [{"text": "Multivariable regression analyses", "type": "IntellectualProduct"}, {"text": "student", "type": "PopulationGroup"}]}

Example input:
Sentence: They were more likely to prefer a personal engagement strategy , valued scientific evidence , preferred a more active approach to safety education , and advocated disclosure of errors .

Example answer:
{"entities": [{"text": "engagement", "type": "HealthCareActivity"}, {"text": "approach", "type": "SpatialConcept"}]}

Example input:
Sentence: Hence , it is imperative that education interventions are needed to bring or sustain positive change .

Example answer:
{"entities": [{"text": "education interventions", "type": "HealthCareActivity"}, {"text": "positive", "type": "Finding"}]}

Example input:
Sentence: Cross - sectional study assessing school engagement .

Example answer:
{"entities": [{"text": "Cross - sectional study", "type": "ResearchActivity"}]}

Example input:
Sentence: To investigate school engagement for students with ADHD during the crucial high school transition period and to identify factors associated with low school engagement .

Example answer:
{"entities": [{"text": "students", "type": "PopulationGroup"}, {"text": "ADHD", "type": "BiologicFunction"}, {"text": "low school engagement", "type": "Finding"}]}

Example input:
Sentence: School engagement is measured as student attitudes to school ( cognitive and emotional ) and suspension rates ( behavioural ) .

Example answer:
{"entities": [{"text": "school", "type": "Organization"}, {"text": "cognitive", "type": "BiologicFunction"}, {"text": "emotional", "type": "BiologicFunction"}]}

Input:
Sentence: School engagement is potentially modifiable , and targeting engagement may be a means to improve education outcomes .

## Item MedMentions:test:2567
Example input:
Sentence: Prevalence of HPV positivity was 43 . 9 % with an average age of 35 .

Example answer:
{"entities": [{"text": "HPV positivity", "type": "Finding"}]}

Example input:
Sentence: Women older than 50 years were a high - risk group for HR - HPV infection and cervical cancer .

Example answer:
{"entities": [{"text": "HR - HPV infection", "type": "BiologicFunction"}, {"text": "cervical cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Statistically significant correlations were found only in MB between parameters HPV - p53 , p53 - pRb and p53 - p16 .

Example answer:
{"entities": [{"text": "parameters", "type": "Finding"}, {"text": "HPV", "type": "Virus"}, {"text": "p53", "type": "Chemical"}, {"text": "pRb", "type": "Chemical"}, {"text": "p16", "type": "Chemical"}]}

Example input:
Sentence: HPV DNA was amplified using polymerase chain reaction ( PCR ) and HPV genotypes were identified by reverse hybridization .

Example answer:
{"entities": [{"text": "HPV DNA", "type": "Chemical"}, {"text": "amplified", "type": "BiologicFunction"}, {"text": "polymerase chain reaction", "type": "ResearchActivity"}, {"text": "PCR", "type": "ResearchActivity"}, {"text": "HPV", "type": "Virus"}, {"text": "reverse hybridization", "type": "ResearchActivity"}]}

Example input:
Sentence: It is concluded that in Cuban HCV - infected patients , the responder homogeneous variant rs8099917TT is the most frequent genotype .

Example answer:
{"entities": [{"text": "Cuban", "type": "PopulationGroup"}, {"text": "HCV", "type": "Virus"}, {"text": "infected", "type": "Finding"}, {"text": "responder", "type": "Finding"}, {"text": "variant", "type": "AnatomicalStructure"}, {"text": "rs8099917TT", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Tumors positive for any other high - risk HPV genotype were classified as non - HPV16 - positive .

Example answer:
{"entities": [{"text": "Tumors", "type": "BiologicFunction"}, {"text": "positive for", "type": "Finding"}, {"text": "high - risk", "type": "Finding"}, {"text": "HPV genotype", "type": "Chemical"}, {"text": "classified", "type": "IntellectualProduct"}, {"text": "non - HPV16 - positive", "type": "Finding"}]}

Example input:
Sentence: The prevalence of HR - HPV among women older than 50 years was significantly higher than the other groups ( P < 0 .

Example answer:
{"entities": [{"text": "HR - HPV", "type": "Virus"}]}

Example input:
Sentence: As opposed to other studies , HPV 52 was the third most commonly encountered strain after HPV 16 and HPV 18 .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "HPV 52", "type": "Virus"}, {"text": "encountered", "type": "HealthCareActivity"}, {"text": "HPV 16", "type": "Virus"}, {"text": "HPV 18", "type": "Virus"}]}

Example input:
Sentence: The main carcinogenic genotypes were HPV - 16 , HPV - 18 , HPV - 58 , HPV - 52 , and HPV - 31 . HPV - 16 and HPV - 18 combined caused 80 .

Example answer:
{"entities": [{"text": "carcinogenic", "type": "Chemical"}, {"text": "HPV - 16", "type": "Virus"}, {"text": "HPV - 18", "type": "Virus"}, {"text": "HPV - 58", "type": "Virus"}, {"text": "HPV - 52", "type": "Virus"}, {"text": "HPV - 31", "type": "Virus"}]}

Example input:
Sentence: HPV 16 was the commonest strain ( N = 57 , 73 . 08 % ) followed by HPV 18 ( N = 28 , 35 . 90 % ) .

Example answer:
{"entities": [{"text": "HPV 16", "type": "Virus"}, {"text": "HPV 18", "type": "Virus"}]}

Input:
Sentence: The most common HR - HPV genotypes were HPV - 16 , HPV - 58 , HPV - 52 , HPV - 18 , and HPV - 31 .

## Item MedMentions:test:2546
Example input:
Sentence: Lentiviral vector containing small interfering RNA targeting Siglec - 1 ( Lv - shSiglec - 1 ) or control vector ( Lv - shNC ) were injected intravenously into 6 - week old Apoe ( - / - ) mice .

Example answer:
{"entities": [{"text": "Lentiviral vector", "type": "Chemical"}, {"text": "small interfering RNA", "type": "Chemical"}, {"text": "Siglec - 1", "type": "AnatomicalStructure"}, {"text": "Lv - shSiglec - 1", "type": "Chemical"}, {"text": "control vector", "type": "Chemical"}, {"text": "Lv - shNC", "type": "Chemical"}, {"text": "intravenously", "type": "SpatialConcept"}, {"text": "Apoe ( - / - )", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Importantly , even though the immune system of newborns may be characterized as developmentally immature , with a propensity to develop Th2 immunity , significant CD8 + T - cell responses may still be elicited in the context of optimal priming .

Example answer:
{"entities": [{"text": "immune system", "type": "BodySystem"}, {"text": "developmentally", "type": "BiologicFunction"}, {"text": "Th2", "type": "AnatomicalStructure"}, {"text": "immunity", "type": "BiologicFunction"}, {"text": "CD8 + T - cell", "type": "AnatomicalStructure"}, {"text": "responses", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study , we used adeno - associated virus ( AAV ) serotype 9 ( AAV9 ) to deliver a functional NPC1 gene systemically into NPC1 ( - / - ) mice at postnatal day 4 .

Example answer:
{"entities": [{"text": "adeno - associated virus", "type": "Virus"}, {"text": "AAV", "type": "Virus"}, {"text": "serotype 9", "type": "IntellectualProduct"}, {"text": "AAV9", "type": "Virus"}, {"text": "NPC1 gene", "type": "AnatomicalStructure"}, {"text": "NPC1 ( - / - )", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "postnatal day 4", "type": "HealthCareActivity"}]}

Example input:
Sentence: Female BALB / c mice were vaccinated with 100 μg of purified recombinant vector intramuscularly 3 times at two - week intervals and the levels of five cytokines including IFN - γ , IL - 12 , IL - 4 , IL - 10 and TGF - β were measured .

Example answer:
{"entities": [{"text": "BALB / c mice", "type": "Eukaryote"}, {"text": "vaccinated", "type": "HealthCareActivity"}, {"text": "recombinant", "type": "Chemical"}, {"text": "vector", "type": "Chemical"}, {"text": "intramuscularly", "type": "SpatialConcept"}, {"text": "cytokines", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "IL - 12", "type": "Chemical"}, {"text": "IL - 4", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "TGF - β", "type": "Chemical"}]}

Example input:
Sentence: We aimed to improve the efficacy and safety of adoptive T - cell transfer by using adenoviral vectors for direct delivery of immunomodulatory murine cytokines into B16 .

Example answer:
{"entities": [{"text": "adoptive T - cell transfer", "type": "HealthCareActivity"}, {"text": "adenoviral vectors", "type": "Chemical"}, {"text": "immunomodulatory", "type": "HealthCareActivity"}, {"text": "murine", "type": "Eukaryote"}, {"text": "cytokines", "type": "Chemical"}, {"text": "B16 .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We further tested the impact of maternal immunity against our replication - deficient adenoviral vector during early life vaccination .

Example answer:
{"entities": [{"text": "maternal", "type": "Finding"}, {"text": "immunity", "type": "BiologicFunction"}, {"text": "replication - deficient", "type": "BiologicFunction"}, {"text": "adenoviral vector", "type": "Chemical"}, {"text": "vaccination", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of the present study was therefore to assess whether replication - deficient adenovectors could overcome the risk of overwhelming antigen stimulation during the first period of life and provide a pertinent alternative in infant vaccinology .

Example answer:
{"entities": [{"text": "replication - deficient", "type": "BiologicFunction"}, {"text": "adenovectors", "type": "Chemical"}, {"text": "antigen stimulation", "type": "BiologicFunction"}, {"text": "vaccinology", "type": "HealthCareActivity"}]}

Example input:
Sentence: Replication deficient adenoviral vectors have been demonstrated to induce potent CD8 + T - cell response in mice , primates and humans .

Example answer:
{"entities": [{"text": "Replication deficient", "type": "BiologicFunction"}, {"text": "adenoviral vectors", "type": "Chemical"}, {"text": "CD8 + T - cell", "type": "AnatomicalStructure"}, {"text": "response", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "primates", "type": "Eukaryote"}, {"text": "humans", "type": "Eukaryote"}]}

Example input:
Sentence: Overall , our results indicate that memory CD8 + T cells induced by adenoviral vectors in infant mice are of good quality and match those elicited in the adult host .

Example answer:
{"entities": [{"text": "memory", "type": "AnatomicalStructure"}, {"text": "CD8 + T cells", "type": "AnatomicalStructure"}, {"text": "adenoviral vectors", "type": "Chemical"}, {"text": "infant", "type": "Eukaryote"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Early life vaccination : Generation of adult - quality memory CD8 + T cells in infant mice using non - replicating adenoviral vectors Intracellular pathogens represent a serious threat during early life .

Example answer:
{"entities": [{"text": "vaccination", "type": "HealthCareActivity"}, {"text": "memory", "type": "AnatomicalStructure"}, {"text": "CD8 + T cells", "type": "AnatomicalStructure"}, {"text": "infant", "type": "Eukaryote"}, {"text": "mice", "type": "Eukaryote"}, {"text": "non - replicating", "type": "BiologicFunction"}, {"text": "adenoviral vectors", "type": "Chemical"}, {"text": "Intracellular", "type": "SpatialConcept"}]}

Input:
Sentence: To address this , infant mice were vaccinated with three different adenoviral vectors and the CD8 + T - cell response after early life vaccination was explored .

## Item MedMentions:test:2829
Example input:
Sentence: Rapid intervention necessitates the capacity to generate , grow , and genetically manipulate infectious CoVs in order to rapidly evaluate pathogenic mechanisms , host and tissue permissibility , and candidate antiviral therapeutic efficacy .

Example answer:
{"entities": [{"text": "Rapid intervention", "type": "HealthCareActivity"}, {"text": "genetically manipulate", "type": "ResearchActivity"}, {"text": "infectious CoVs", "type": "BiologicFunction"}, {"text": "pathogenic", "type": "Finding"}, {"text": "host and tissue permissibility", "type": "BiologicFunction"}, {"text": "antiviral therapeutic efficacy", "type": "HealthCareActivity"}]}

Example input:
Sentence: In particular , CRISPR - Cas9 shows highly efficient gene editing activity for therapeutic purposes in systems ranging from patient stem cells to animal models .

Example answer:
{"entities": [{"text": "CRISPR - Cas9", "type": "BiologicFunction"}, {"text": "gene editing", "type": "ResearchActivity"}, {"text": "stem cells", "type": "AnatomicalStructure"}, {"text": "animal models", "type": "Eukaryote"}]}

Example input:
Sentence: The central concepts of genomic instability fit nicely with the mutator phenotype hypothesis proposed by Lawrence Loeb , both of which represent functionally similar frameworks for describing how genomic stability can be compromised .

Example answer:
{"entities": [{"text": "genomic instability", "type": "BiologicFunction"}, {"text": "Lawrence Loeb", "type": "ProfessionalOrOccupationalGroup"}, {"text": "genomic stability", "type": "BiologicFunction"}]}

Example input:
Sentence: The results from this study indicate that the molecular signature of AD treatment may include a much broader range of genomic markers than previously hypothesized , suggesting that response to medication may be as complex as the pathology .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "AD", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "genomic markers", "type": "BiologicFunction"}, {"text": "response", "type": "ClinicalAttribute"}, {"text": "medication", "type": "Chemical"}]}

Example input:
Sentence: It was found that the short - term therapeutic efficacy ( CR rate ) was higher in the group of patients carrying the homozygous mutation of XRCC1 - 399 ( A / A genotype ) than in the group of patients without the XRCC1 - 399 mutation ( G / G genotype ) .

Example answer:
{"entities": [{"text": "CR", "type": "Finding"}, {"text": "homozygous mutation", "type": "BiologicFunction"}, {"text": "XRCC1 - 399", "type": "AnatomicalStructure"}, {"text": "A", "type": "Chemical"}, {"text": "mutation", "type": "BiologicFunction"}, {"text": "G", "type": "Chemical"}]}

Example input:
Sentence: The aim of this research is to propose a practical implementation of the notion of actionability , a common criteria justifying the disclosure of secondary findings but whose interpretation varies greatly among professionals .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "findings", "type": "Finding"}, {"text": "interpretation", "type": "IntellectualProduct"}, {"text": "professionals", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: We distinguish three types of actionability corresponding to ( 1 ) well - established medical actions , ( 2 ) patient -initiated health - related actions and ( 3 ) life - plan decisions .

Example answer:
{"entities": [{"text": "life - plan decisions", "type": "BiologicFunction"}]}

Example input:
Sentence: The mutation burden in the involved tissues likely accounts for the variable manifestations .

Example answer:
{"entities": [{"text": "mutation", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "variable manifestations", "type": "Finding"}]}

Example input:
Sentence: A clinically actionable pathogenic or likely pathogenic variant was identified in 40 of 302 cases ( 13 % ) .

Example answer:
{"entities": [{"text": "pathogenic", "type": "Finding"}]}

Example input:
Sentence: Regarding variants of uncertain clinical significance in actionable genes , we found that different understandings of autonomy lead to different conclusions and that , for some of them , it may be legitimate to refrain from returning uncertain information .

Example answer:
{"entities": [{"text": "variants", "type": "AnatomicalStructure"}, {"text": "clinical significance", "type": "Finding"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Input:
Sentence: We argue that actionability depends on the characteristics of the mutation or gene and on the values of patients .

