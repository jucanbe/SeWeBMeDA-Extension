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

## Item MedMentions:test:4412
Example input:
Sentence: The erythrocyte sedimentation rate ( ESR ) , C - reactive protein ( CRP ) , and CA - 125 level were higher in the chlamydia group than in the non - chlamydia group , but there was no significant difference in the white blood cell count between the two groups .

Example answer:
{"entities": [{"text": "erythrocyte sedimentation rate", "type": "Finding"}, {"text": "ESR", "type": "Finding"}, {"text": "C - reactive protein", "type": "Chemical"}, {"text": "CRP", "type": "Chemical"}, {"text": "CA - 125", "type": "Chemical"}, {"text": "chlamydia group", "type": "PopulationGroup"}, {"text": "non - chlamydia group", "type": "PopulationGroup"}, {"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: The levels of CRP were higher in the Stoppa group ( P < 0 . 05 ) but the number of leucocytes , haematocrit , and haemoglobin were similar between the groups ( P > 0 . 05 ) .

Example answer:
{"entities": [{"text": "CRP", "type": "Chemical"}, {"text": "Stoppa", "type": "HealthCareActivity"}, {"text": "leucocytes", "type": "AnatomicalStructure"}, {"text": "haematocrit", "type": "Finding"}, {"text": "haemoglobin", "type": "Chemical"}]}

Example input:
Sentence: Also , postoperatively , NGAL , creatinine , aspartate aminotransferase and AOPP levels were higher in group I than group II ( p < 0 .

Example answer:
{"entities": [{"text": "NGAL", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "aspartate aminotransferase", "type": "Chemical"}, {"text": "AOPP", "type": "Chemical"}]}

Example input:
Sentence:  of the formulations had a log10 reduction after 3 h that was significantly better compared with the reference procedure [ mean 1 . 72 ( standard deviation 1 . 15 ) ] .

Example answer:
{"entities": []}

Example input:
Sentence: Within group comparison : The percentage of CD4 + in the two groups was significantly reduced at 24 hours post - operation ( T2 ) compared with the percentage before surgery , whereas the percentage of CD8 + was higher at T2 .

Example answer:
{"entities": [{"text": "percentage of CD4 +", "type": "HealthCareActivity"}, {"text": "percentage", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "percentage of CD8 + was higher", "type": "Finding"}]}

Example input:
Sentence: We tested the function of an upregulated LDP , S100a10 , in vivo with adenovirus -mediated gene silencing and found , unexpectedly , that knockdown of S100a10 accelerated progression of HFD - induced liver steatosis .

Example answer:
{"entities": [{"text": "upregulated", "type": "BiologicFunction"}, {"text": "LDP", "type": "Chemical"}, {"text": "S100a10", "type": "AnatomicalStructure"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "adenovirus", "type": "Virus"}, {"text": "gene silencing", "type": "BiologicFunction"}, {"text": "knockdown", "type": "BiologicFunction"}, {"text": "HFD", "type": "Food"}, {"text": "liver steatosis", "type": "BiologicFunction"}]}

Example input:
Sentence: In group I , T - SH , NGAL and urea levels were found to be significantly increased postoperatively compared to preoperative measurements ( p < 0 .

Example answer:
{"entities": [{"text": "T - SH", "type": "Chemical"}, {"text": "NGAL", "type": "Chemical"}, {"text": "urea levels", "type": "Finding"}]}

Example input:
Sentence: The levels of post - operative serum troponin - T at 12 and 18 h , CK - MB at 24 h , as well as the serum h - FABP levels at 6 h , after CPB were significantly lower , which was coincident with significantly higher protein expression of cardiac Hif - 1α , p - Akt , p - STAT3 , p - STAT5 , and p - eNOS and less vacuolization of mitochondria in the RIPC group compared to the control group .

Example answer:
{"entities": [{"text": "serum troponin - T", "type": "Finding"}, {"text": "CK - MB", "type": "HealthCareActivity"}, {"text": "CPB", "type": "HealthCareActivity"}, {"text": "protein expression", "type": "BiologicFunction"}, {"text": "Hif - 1α", "type": "Chemical"}, {"text": "p - STAT3", "type": "Chemical"}, {"text": "p - STAT5", "type": "Chemical"}, {"text": "p - eNOS", "type": "Chemical"}, {"text": "vacuolization", "type": "Finding"}, {"text": "mitochondria", "type": "AnatomicalStructure"}, {"text": "RIPC", "type": "HealthCareActivity"}]}

Example input:
Sentence: High - sensitivity troponin T levels were significantly higher in the T - ICD group from 1 to 24 h after the procedure ( P ≤ 0 . 02 ) .

Example answer:
{"entities": [{"text": "High - sensitivity troponin T", "type": "HealthCareActivity"}, {"text": "T - ICD", "type": "MedicalDevice"}, {"text": "procedure", "type": "HealthCareActivity"}]}

Example input:
Sentence: Creatine phosphokinase activity levels were significantly higher in the S - ICD group , at 3 , 6 , and 24 h after the procedure ( P ≤ 0 . 05 ) .

Example answer:
{"entities": [{"text": "Creatine phosphokinase activity", "type": "BiologicFunction"}, {"text": "procedure", "type": "HealthCareActivity"}]}

Input:
Sentence: S100 protein level was similar in both groups at 1 h after the procedure and then decreased in the T - ICD group compared to the S - ICD group ( P = 0 . 04 ) .

## Item MedMentions:test:4665
Example input:
Sentence: We demonstrated differential uptake and toxicity of iron after 12 h exposure to 10 μM ferrous ammonium sulphate , ferric citrate or ferrocene .

Example answer:
{"entities": [{"text": "uptake", "type": "BiologicFunction"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "iron", "type": "Chemical"}, {"text": "ferrous ammonium sulphate", "type": "Chemical"}, {"text": "ferric citrate", "type": "Chemical"}, {"text": "ferrocene", "type": "Chemical"}]}

Example input:
Sentence: 38 for Ce ) were significantly elevated compared to 1 - 5 years group ( 2 . 58 ± 1 . 51 for La , 6 . 87 ± 3 .

Example answer:
{"entities": [{"text": "Ce", "type": "Chemical"}, {"text": "La", "type": "Chemical"}]}

Example input:
Sentence: In multi - pollutant models an interquartile range increase in 24 h PMcoarse was associated with increases in FENO by between 6 .

Example answer:
{"entities": [{"text": "multi - pollutant", "type": "Chemical"}, {"text": "models", "type": "IntellectualProduct"}]}

Example input:
Sentence: Likewise , the duration of elevated high - [ Formula : see text ] activity increased with movement duration .

Example answer:
{"entities": [{"text": "movement", "type": "BiologicFunction"}]}

Example input:
Sentence: An increase in transcript abundance of TR - ACO1 and TR - ACO3 , but not TR - ACO2 , was observed after 1 h of exposure to low Pi , with a second increase in TR - ACO1 transcripts occurring after 2 - 5 days .

Example answer:
{"entities": [{"text": "transcript", "type": "Chemical"}, {"text": "TR - ACO1", "type": "AnatomicalStructure"}, {"text": "TR - ACO3", "type": "AnatomicalStructure"}, {"text": "TR - ACO2", "type": "AnatomicalStructure"}, {"text": "Pi", "type": "Chemical"}, {"text": "transcripts", "type": "Chemical"}]}

Example input:
Sentence: CG induced a dose -related oedema more rapidly from 0 to 2 h which lasted for at least 72 h , showing a biphasic profile ( peak at 2 and 24 h ) , compared with the monophasic oedema induced in rat paws ( maximal duration of 24 h ) .

Example answer:
{"entities": [{"text": "CG", "type": "Chemical"}, {"text": "oedema", "type": "Finding"}, {"text": "rat", "type": "Eukaryote"}, {"text": "paws", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Superoxide dismutase and catalase activity was elevated after exposure to the lower concentrations and then decreased with higher concentrations .

Example answer:
{"entities": [{"text": "Superoxide dismutase", "type": "Chemical"}, {"text": "catalase", "type": "Chemical"}, {"text": "activity", "type": "BiologicFunction"}]}

Example input:
Sentence: The results showed that the production of reactive oxygen species increased in a concentration -dependent manner after exposure to PFOS for 96 h .

Example answer:
{"entities": [{"text": "reactive oxygen species", "type": "Chemical"}, {"text": "PFOS", "type": "Chemical"}]}

Example input:
Sentence: Although alkaloid concentrations were greatly reduced by low temperature this reduction did not occur until after 4 weeks of exposure .

Example answer:
{"entities": [{"text": "alkaloid", "type": "Chemical"}]}

Example input:
Sentence: These effects persisted even at 24 h after removal of the compound and culminated in increased levels of p53 and p21 together with growth arrest .

Example answer:
{"entities": [{"text": "p53", "type": "Chemical"}, {"text": "p21", "type": "Chemical"}, {"text": "growth arrest", "type": "BiologicFunction"}]}

Input:
Sentence: Both remained elevated for nearly 48 h after exposure with the effect gradually decreasing .

## Item MedMentions:test:4432
Example input:
Sentence: We discovered a gene co - occurrence network in mesiodens patients with functionally enriched gene groups in the sonic hedgehog ( SHH ) , bone morphogenetic proteins ( BMP ) , and wingless integrated ( WNT ) signaling pathways .

Example answer:
{"entities": [{"text": "gene", "type": "AnatomicalStructure"}, {"text": "mesiodens", "type": "BiologicFunction"}, {"text": "sonic hedgehog", "type": "Chemical"}, {"text": "SHH", "type": "Chemical"}, {"text": "bone morphogenetic proteins", "type": "Chemical"}, {"text": "BMP", "type": "Chemical"}, {"text": "wingless integrated", "type": "Chemical"}, {"text": "WNT", "type": "Chemical"}, {"text": "signaling pathways", "type": "BiologicFunction"}]}

Example input:
Sentence: We postulate that variants in CHH genes , in particular PROKR2 , PROK2 , WDR11 and FGFR1 with CHD7 , may contribute to under - virilisation phenotypes including hypospadias in Indonesia .

Example answer:
{"entities": [{"text": "CHH", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "PROKR2", "type": "AnatomicalStructure"}, {"text": "PROK2", "type": "AnatomicalStructure"}, {"text": "WDR11", "type": "AnatomicalStructure"}, {"text": "FGFR1", "type": "AnatomicalStructure"}, {"text": "CHD7", "type": "AnatomicalStructure"}, {"text": "under - virilisation", "type": "BiologicFunction"}, {"text": "hypospadias", "type": "BiologicFunction"}, {"text": "Indonesia", "type": "SpatialConcept"}]}

Example input:
Sentence: With this aim , we selected 11 variants of 5 genes ( GJB2 , SLC26A4 , MTRNR1 , TMPRSS3 , and CDH23 ) showing high prevalence with varying degrees in Koreans and developed the U - TOP ™ HL Genotyping Kit , a real - time PCR -based method using the MeltingArray technique and peptide nucleic acid probes .

Example answer:
{"entities": [{"text": "variants", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "GJB2", "type": "AnatomicalStructure"}, {"text": "SLC26A4", "type": "AnatomicalStructure"}, {"text": "MTRNR1", "type": "AnatomicalStructure"}, {"text": "TMPRSS3", "type": "AnatomicalStructure"}, {"text": "CDH23", "type": "AnatomicalStructure"}, {"text": "Koreans", "type": "PopulationGroup"}, {"text": "U - TOP ™ HL Genotyping Kit", "type": "MedicalDevice"}, {"text": "real - time PCR", "type": "ResearchActivity"}, {"text": "MeltingArray technique", "type": "ResearchActivity"}, {"text": "peptide nucleic acid", "type": "Chemical"}, {"text": "probes", "type": "MedicalDevice"}]}

Example input:
Sentence: Taken together , these data suggest that genes other than ERG and PTEN may drive carcinogenesis / progression in the majority of men with germline HOXB13 mutations .

Example answer:
{"entities": [{"text": "genes", "type": "AnatomicalStructure"}, {"text": "ERG", "type": "AnatomicalStructure"}, {"text": "PTEN", "type": "AnatomicalStructure"}, {"text": "carcinogenesis", "type": "BiologicFunction"}, {"text": "men", "type": "PopulationGroup"}, {"text": "germline HOXB13 mutations", "type": "BiologicFunction"}]}

Example input:
Sentence: However , there was no association between the mutant genotype of IGF2 rs3741211 and the methylation levels of IGF2 and H19 , and ART might not affect the distribution of the abovementioned genotypes .

Example answer:
{"entities": [{"text": "no", "type": "Finding"}, {"text": "mutant", "type": "AnatomicalStructure"}, {"text": "IGF2 rs3741211", "type": "AnatomicalStructure"}, {"text": "methylation", "type": "BiologicFunction"}, {"text": "IGF2", "type": "AnatomicalStructure"}, {"text": "H19", "type": "AnatomicalStructure"}, {"text": "ART", "type": "HealthCareActivity"}]}

Example input:
Sentence: qRT - PCR analysis showed that Twist1 , periostin , and CTGF mRNA levels were decreased in the H group and increased in the HL group .

Example answer:
{"entities": [{"text": "qRT - PCR", "type": "ResearchActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "Twist1", "type": "AnatomicalStructure"}, {"text": "periostin", "type": "AnatomicalStructure"}, {"text": "CTGF", "type": "AnatomicalStructure"}, {"text": "mRNA", "type": "Chemical"}, {"text": "H group", "type": "PopulationGroup"}, {"text": "HL group", "type": "PopulationGroup"}]}

Example input:
Sentence: We further specified expression of a XTH gene Medtr4g128580 ( MtXTH3 ) under different environmental stresses , and showed that MtXTH3 was induced by Hg exposure .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "XTH gene", "type": "AnatomicalStructure"}, {"text": "Medtr4g128580", "type": "AnatomicalStructure"}, {"text": "MtXTH3", "type": "AnatomicalStructure"}, {"text": "Hg", "type": "Chemical"}]}

Example input:
Sentence: The HHEX gene did not show either allelic or genotypic association with T2DM .

Example answer:
{"entities": [{"text": "HHEX gene", "type": "AnatomicalStructure"}, {"text": "allelic", "type": "AnatomicalStructure"}, {"text": "T2DM", "type": "BiologicFunction"}]}

Example input:
Sentence: A significant association was seen of all the three SNPs of CDKAL1 and CDKN2A / B genes with T2DM but none of the two SNPs of HHEX .

Example answer:
{"entities": [{"text": "SNPs", "type": "SpatialConcept"}, {"text": "CDKAL1", "type": "AnatomicalStructure"}, {"text": "CDKN2A", "type": "AnatomicalStructure"}, {"text": "B genes", "type": "AnatomicalStructure"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "HHEX", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In the ' omics ' era , genomics , transcriptomics , proteomics and metabolomics have been already used to detect genes affecting HT .

Example answer:
{"entities": [{"text": "genomics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "proteomics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "metabolomics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "detect", "type": "Finding"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "HT", "type": "Finding"}]}

Input:
Sentence: Except for the slick hair gene , there are no other genes for which variants have been clearly associated with HT .

## Item MedMentions:test:3917
Example input:
Sentence: Participants with overt heart failure benefit most from CABG combined with intramyocardial injection of CD133 + bone marrow mononuclear cell within the group .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "overt heart failure", "type": "BiologicFunction"}, {"text": "CABG", "type": "HealthCareActivity"}, {"text": "intramyocardial", "type": "AnatomicalStructure"}, {"text": "injection", "type": "HealthCareActivity"}, {"text": "CD133 + bone marrow mononuclear cell", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Circulating progenitor cells and coronary microvascular dysfunction : Results from the NHLBI -sponsored Women 's Ischemia Syndrome Evaluation - Coronary Vascular Dysfunction Study ( WISE - CVD ) Ischemia stimulates a reparative response resulting in mobilization of circulating progenitor cells ( CPCs ) .

Example answer:
{"entities": [{"text": "Circulating progenitor cells", "type": "AnatomicalStructure"}, {"text": "coronary microvascular dysfunction", "type": "BiologicFunction"}, {"text": "NHLBI", "type": "Organization"}, {"text": "Women 's", "type": "PopulationGroup"}, {"text": "Ischemia Syndrome", "type": "BiologicFunction"}, {"text": "Evaluation", "type": "HealthCareActivity"}, {"text": "Coronary Vascular Dysfunction", "type": "BiologicFunction"}, {"text": "Study", "type": "ResearchActivity"}, {"text": "WISE - CVD", "type": "Finding"}, {"text": "Ischemia", "type": "BiologicFunction"}, {"text": "stimulates", "type": "Finding"}, {"text": "circulating progenitor cells", "type": "AnatomicalStructure"}, {"text": "CPCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Perioperative Transfusion of Leukocyte - depleted Blood Products in Contemporary Radical Cystectomy Cohort Does Not Adversely Impact Short - term Survival To evaluate the effect of leukoreduced -only perioperative blood transfusion ( PBT ) and corresponding survival outcomes in a radical cystectomy cohort of patients .

Example answer:
{"entities": [{"text": "Transfusion", "type": "HealthCareActivity"}, {"text": "Leukocyte", "type": "AnatomicalStructure"}, {"text": "Blood Products", "type": "Chemical"}, {"text": "Radical Cystectomy", "type": "HealthCareActivity"}, {"text": "Cohort", "type": "PopulationGroup"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "blood transfusion", "type": "HealthCareActivity"}, {"text": "PBT", "type": "HealthCareActivity"}, {"text": "radical cystectomy", "type": "HealthCareActivity"}, {"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: We hypothesized that streamlined cardiopulmonary bypass circuit and rotational thromboelastometry ( ROTEM ) would reduce blood product usage and improve outcomes .

Example answer:
{"entities": [{"text": "rotational thromboelastometry", "type": "HealthCareActivity"}, {"text": "ROTEM", "type": "HealthCareActivity"}, {"text": "blood product usage", "type": "HealthCareActivity"}]}

Example input:
Sentence: We analysed 150 patients with ischemic cardiomyopathy , who received intramyocardial CD133 + bone marrow mononuclear stem cell treatment combined with coronary artery bypass grafting ( CABG ) or CABG alone .

Example answer:
{"entities": [{"text": "ischemic cardiomyopathy", "type": "BiologicFunction"}, {"text": "intramyocardial", "type": "AnatomicalStructure"}, {"text": "CD133 + bone marrow mononuclear stem cell", "type": "AnatomicalStructure"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "coronary artery bypass grafting", "type": "HealthCareActivity"}, {"text": "CABG", "type": "HealthCareActivity"}]}

Example input:
Sentence: A New Intraoperative Protocol for Reducing Perioperative Transfusions in Cardiac Surgery Perioperative anemia and blood product transfusion increases short - term and long - term morbidity and mortality during cardiac surgery .

Example answer:
{"entities": [{"text": "Reducing Perioperative Transfusions", "type": "HealthCareActivity"}, {"text": "Cardiac Surgery", "type": "HealthCareActivity"}, {"text": "anemia", "type": "BiologicFunction"}, {"text": "blood product transfusion", "type": "HealthCareActivity"}, {"text": "cardiac surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Use of streamlined bypass circuit correlated with significantly reduced intraoperative transfusion of packed red blood cells ( pRBCs ) ( 23 . 8 % versus 17 . 9 % ; p = 0 .

Example answer:
{"entities": [{"text": "transfusion", "type": "HealthCareActivity"}, {"text": "packed red blood cells", "type": "Chemical"}, {"text": "pRBCs", "type": "Chemical"}]}

Example input:
Sentence: 70 diabetic patients who underwent elective CABG and whose hematocrit values had been between 24 - 28 % at any time during CBP were prospectively randomized and equally allocated to two groups : patients who received RBC during CPB ( group I , n = 35 ) vs . did not receive RBC during CPB ( group II , n = 35 ) .

Example answer:
{"entities": [{"text": "diabetic", "type": "BiologicFunction"}, {"text": "CABG", "type": "HealthCareActivity"}, {"text": "hematocrit values", "type": "Finding"}, {"text": "CBP", "type": "HealthCareActivity"}, {"text": "RBC", "type": "AnatomicalStructure"}, {"text": "CPB", "type": "HealthCareActivity"}]}

Example input:
Sentence: The correction of anemia with RBC transfusion in diabetic patients undergoing CABG could increase the risk of renal injury .

Example answer:
{"entities": [{"text": "anemia", "type": "BiologicFunction"}, {"text": "RBC transfusion", "type": "HealthCareActivity"}, {"text": "diabetic", "type": "BiologicFunction"}, {"text": "CABG", "type": "HealthCareActivity"}, {"text": "renal injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Correction of dilutional anemia induces renal dysfunction in diabetic patients undergoing coronary artery bypass grafting : a consequence of microcirculatory alterations ?

Example answer:
{"entities": [{"text": "dilutional anemia", "type": "BiologicFunction"}, {"text": "renal dysfunction", "type": "Finding"}, {"text": "diabetic", "type": "BiologicFunction"}, {"text": "coronary artery bypass grafting", "type": "HealthCareActivity"}, {"text": "microcirculatory", "type": "BiologicFunction"}]}

Input:
Sentence: In this study we aimed to evaluate the effects of dilutional anemia resulting from cardiopulmonary bypass ( CPB ) and its correction with red blood cell ( RBC ) transfusion on tissue oxygenation and renal function in diabetic patients undergoing coronary artery bypass grafting ( CABG ) .

## Item MedMentions:test:4270
Example input:
Sentence: Intensive social cognitive treatment ( can do treatment ) with participation of support partners in persons with relapsing remitting multiple sclerosis : observation of improved self - efficacy , quality of life , anxiety and depression 1 year later In persons with multiple sclerosis ( MS ) self - efficacy positively affects health - related quality of life ( HRQoL ) and physical activity .

Example answer:
{"entities": [{"text": "cognitive treatment", "type": "HealthCareActivity"}, {"text": "partners", "type": "PopulationGroup"}, {"text": "persons", "type": "PopulationGroup"}, {"text": "relapsing remitting multiple sclerosis", "type": "BiologicFunction"}, {"text": "observation", "type": "HealthCareActivity"}, {"text": "improved", "type": "Finding"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "anxiety", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "multiple sclerosis", "type": "BiologicFunction"}, {"text": "MS", "type": "BiologicFunction"}, {"text": "positively", "type": "Finding"}]}

Example input:
Sentence: This study investigates whether parent - child agreement on the conduct and emotional scales of the Strengths and Difficulties Questionnaire ( SDQ ) varied as a result of certain child characteristics , including the child 's presenting problems to clinical services , age and gender .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "conduct", "type": "IntellectualProduct"}, {"text": "emotional scales", "type": "IntellectualProduct"}, {"text": "Strengths and Difficulties Questionnaire", "type": "IntellectualProduct"}, {"text": "SDQ", "type": "IntellectualProduct"}, {"text": "presenting problems", "type": "Finding"}, {"text": "clinical services", "type": "HealthCareActivity"}]}

Example input:
Sentence: A practical , customized video intervention may help improve patient self - efficacy , reduce problems with medication use , and improve medication adherence in diabetes patients .

Example answer:
{"entities": [{"text": "practical", "type": "IntellectualProduct"}, {"text": "video", "type": "IntellectualProduct"}, {"text": "improve", "type": "Finding"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "medication", "type": "HealthCareActivity"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: A short , self - administered diabetes specific screening tool for disordered eating behavior can be used routinely in the clinical care of adolescents with type 1 diabetes .

Example answer:
{"entities": [{"text": "diabetes", "type": "BiologicFunction"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "care", "type": "HealthCareActivity"}, {"text": "type 1 diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Full economic evaluations investigating family / family - based interventions for adolescents between 10 and 20 years treated for substance use disorders , delinquency or externalizing disorders were included .

Example answer:
{"entities": [{"text": "family - based interventions", "type": "HealthCareActivity"}, {"text": "substance use disorders", "type": "BiologicFunction"}, {"text": "delinquency", "type": "BiologicFunction"}, {"text": "externalizing disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: Patient adoption of an internet based diabetes medication tool to improve adherence : A pilot study To investigate the effect of a video intervention , Managing Your Diabetes Medicines , on patient self - efficacy , problems with using medication , and medication adherence in a rural , mostly African American population .

Example answer:
{"entities": [{"text": "diabetes", "type": "BiologicFunction"}, {"text": "medication", "type": "HealthCareActivity"}, {"text": "improve", "type": "Finding"}, {"text": "pilot study", "type": "ResearchActivity"}, {"text": "video", "type": "IntellectualProduct"}, {"text": "Diabetes", "type": "BiologicFunction"}, {"text": "Medicines", "type": "Chemical"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "rural", "type": "Finding"}, {"text": "African American population", "type": "PopulationGroup"}]}

Example input:
Sentence: Adults ( N = 80 ) with type 2 diabetes completed self - report measures identifying barriers to adherence at baseline and monthly for 3 months .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Parent - youth interview and chart review provided demographics and diabetes management data .

Example answer:
{"entities": [{"text": "chart review", "type": "HealthCareActivity"}, {"text": "demographics", "type": "ResearchActivity"}, {"text": "diabetes management", "type": "HealthCareActivity"}]}

Example input:
Sentence: Associations between major life events and adherence , glycemic control , and psychosocial characteristics in teens with type 1 diabetes This cross - sectional study assessed the type of major life events occurring in a contemporary sample of teens with type 1 diabetes and the association between event frequency and demographic , diabetes management , and psychosocial characteristics .

Example answer:
{"entities": [{"text": "glycemic control ,", "type": "HealthCareActivity"}, {"text": "teens", "type": "PopulationGroup"}, {"text": "type 1 diabetes", "type": "BiologicFunction"}, {"text": "cross - sectional study", "type": "ResearchActivity"}, {"text": "diabetes management", "type": "HealthCareActivity"}]}

Example input:
Sentence: Teen s with 4 + events had significantly poorer adherence ( P = .002 teen , P = .02 parent ) , lower self - efficacy ( P = .03 teen , P < .0001 parent ) , poorer quality of life ( P < .0001 teen , P < .0001 parent ) , and more conflict ( P = .006 teen , P = .02 parent ) than teens with fewer events .

Example answer:
{"entities": [{"text": "Teen", "type": "PopulationGroup"}, {"text": "teen", "type": "PopulationGroup"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "conflict", "type": "Finding"}, {"text": "teens", "type": "PopulationGroup"}]}

Input:
Sentence: Teens and parents completed validated measures of treatment adherence , diabetes -specific self - efficacy , quality of life , and diabetes -specific family conflict .

## Item MedMentions:test:4373
Example input:
Sentence: On the basis of this meta - analysis , clinical outcomes of multiple - level CDR are similar to those of single - level CDR for cervical spondylosis , which suggests the multiple - level CDR is as effective and safe as the single - level CDR .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "IntellectualProduct"}, {"text": "multiple - level CDR", "type": "HealthCareActivity"}, {"text": "single - level CDR", "type": "HealthCareActivity"}, {"text": "cervical spondylosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Some authors advocate for the multiple - level CDR instead of anterior decompression and fusion in cervical multiple - level spondylosis .

Example answer:
{"entities": [{"text": "multiple - level CDR", "type": "HealthCareActivity"}, {"text": "anterior", "type": "SpatialConcept"}, {"text": "decompression", "type": "HealthCareActivity"}, {"text": "fusion", "type": "HealthCareActivity"}, {"text": "cervical multiple - level spondylosis", "type": "BiologicFunction"}]}

Example input:
Sentence: MR images of the cervical spine were obtained from 37 subjects ( 13 males and 24 females ) aged 18 - 36 years using an axial T1 - weighted spin echo sequence acquired from a 3 - Tesla MR scanner .

Example answer:
{"entities": [{"text": "MR", "type": "HealthCareActivity"}, {"text": "images", "type": "IntellectualProduct"}, {"text": "cervical spine", "type": "AnatomicalStructure"}, {"text": "3 - Tesla MR scanner", "type": "HealthCareActivity"}]}

Example input:
Sentence: Locating the Seventh Cervical Spinous Process : Development and Validation of a Multivariate Model Using Palpation and Personal Information The aim of this study was to develop and validate a multivariate prediction model , guided by palpation and personal information , for locating the seventh cervical spinous process ( C7SP ) .

Example answer:
{"entities": [{"text": "Seventh Cervical Spinous Process", "type": "AnatomicalStructure"}, {"text": "Multivariate Model", "type": "IntellectualProduct"}, {"text": "Palpation", "type": "HealthCareActivity"}, {"text": "multivariate prediction model", "type": "IntellectualProduct"}, {"text": "palpation", "type": "HealthCareActivity"}, {"text": "seventh cervical spinous process", "type": "AnatomicalStructure"}, {"text": "C7SP", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The aim of this study was to evaluate the efficacy and safety of multiple - level cervical disk replacement ( CDR ) over single - level CDR for the treatment of cervical spondylosis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "multiple - level cervical disk replacement", "type": "HealthCareActivity"}, {"text": "CDR", "type": "HealthCareActivity"}, {"text": "single - level CDR", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "cervical spondylosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Comparisons of Safety and Clinical Outcomes Between Multiple - level and Single - level Cervical Disk Replacement for Cervical Spondylosis : A Systematic Review and Meta - analysis This is a systematic review and meta - analysis .

Example answer:
{"entities": [{"text": "Multiple - level", "type": "HealthCareActivity"}, {"text": "Single - level Cervical Disk Replacement", "type": "HealthCareActivity"}, {"text": "Cervical Spondylosis", "type": "BiologicFunction"}, {"text": "Systematic Review", "type": "IntellectualProduct"}, {"text": "Meta - analysis", "type": "IntellectualProduct"}, {"text": "systematic review", "type": "IntellectualProduct"}, {"text": "meta - analysis", "type": "IntellectualProduct"}]}

Example input:
Sentence: Uterine cervical cancer and CIN III accounted for 40 % of hospitalizations ( hr : 15 . 6 / 100 000 and 17 . 6 / 100 000 , respectively ) .

Example answer:
{"entities": [{"text": "Uterine cervical cancer", "type": "BiologicFunction"}, {"text": "CIN III", "type": "BiologicFunction"}, {"text": "hospitalizations", "type": "HealthCareActivity"}]}

Example input:
Sentence: MEDLINE , EMBASE , and Cochrane library databases were searched up to November 2015 for controlled studies that compared the clinical outcomes of single - level and multiple - level CDR for the treatment of cervical spondylosis .

Example answer:
{"entities": [{"text": "MEDLINE", "type": "IntellectualProduct"}, {"text": "EMBASE", "type": "IntellectualProduct"}, {"text": "Cochrane library databases", "type": "IntellectualProduct"}, {"text": "controlled studies", "type": "ResearchActivity"}, {"text": "single - level", "type": "HealthCareActivity"}, {"text": "multiple - level CDR", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "cervical spondylosis", "type": "BiologicFunction"}]}

Example input:
Sentence: The goal of this study was to review the incidence , patient characteristics , and outcome of C5 palsy in patients undergoing cervical spine surgery .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "C5 palsy", "type": "BiologicFunction"}]}

Example input:
Sentence: C5 Palsy After Cervical Spine Surgery : A Multicenter Retrospective Review of 59 Cases A multicenter , retrospective review of C5 palsy after cervical spine surgery .

Example answer:
{"entities": [{"text": "C5 Palsy", "type": "BiologicFunction"}, {"text": "Multicenter", "type": "ResearchActivity"}, {"text": "Retrospective Review", "type": "ResearchActivity"}, {"text": "multicenter", "type": "ResearchActivity"}, {"text": "retrospective review", "type": "ResearchActivity"}, {"text": "C5 palsy", "type": "BiologicFunction"}]}

Input:
Sentence: We conducted a multicenter , retrospective review of 13 946 patients across 21 centers who received cervical spine surgery ( levels C2 to C7 ) between January 1 , 2005 , and December 31 , 2011 , inclusive .

## Item MedMentions:test:4514
Example input:
Sentence: In DEXCHNP , the IC50 was 20 . 12 μg / ml for HEK and 7 . 37 μg / ml for RAW264 .

Example answer:
{"entities": [{"text": "HEK", "type": "AnatomicalStructure"}, {"text": "RAW264 .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Under the optimized conditions , tilianin and acacetin displayed good linearity in the ranges of 0 . 0595 - 4 . 76 and 0 . 0585 - 4 . 68 μg / mL , respectively , with the average recoveries being 96 .

Example answer:
{"entities": [{"text": "tilianin", "type": "Chemical"}, {"text": "acacetin", "type": "Chemical"}]}

Example input:
Sentence: It must be stated that grains and grain - based products are the basis of everyday diet of all age groups , especially small children , where higher intake of citrinin can occur .

Example answer:
{"entities": [{"text": "grains", "type": "Food"}, {"text": "grain - based products", "type": "Food"}, {"text": "diet", "type": "Food"}, {"text": "citrinin", "type": "Chemical"}]}

Example input:
Sentence: From the area of Međimurje County , 10 samples of corn and 10 samples of wheat were analyzed .

Example answer:
{"entities": [{"text": "area", "type": "SpatialConcept"}, {"text": "Međimurje County", "type": "SpatialConcept"}, {"text": "corn", "type": "Food"}, {"text": "wheat", "type": "Food"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: At the European Union level , systematic monitoring of Citrinin in grains began with the aim of determining its highest permissible amount in food .

Example answer:
{"entities": [{"text": "European Union", "type": "Organization"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "Citrinin", "type": "Chemical"}, {"text": "grains", "type": "Food"}, {"text": "food", "type": "Food"}]}

Example input:
Sentence: For the purpose of identification and quantification of citrinin , high performance liquid chromatograph ( HPLC ) with fluorescence was used ( Calibration curve k > 0 . 999 ; Intra assay CV = 2 .

Example answer:
{"entities": [{"text": "citrinin", "type": "Chemical"}, {"text": "high performance liquid chromatograph ( HPLC ) with fluorescence", "type": "HealthCareActivity"}, {"text": "used", "type": "Finding"}]}

Example input:
Sentence:  of the samples contained Citrinin ( < 1 μg / kg ) .

Example answer:
{"entities": [{"text": "Citrinin", "type": "Chemical"}]}

Example input:
Sentence: From the area of Osijek - Baranja and Vukovar - Srijem County , 15 samples from each County were analyzed .

Example answer:
{"entities": [{"text": "area", "type": "SpatialConcept"}, {"text": "Osijek - Baranja", "type": "SpatialConcept"}, {"text": "Vukovar - Srijem County", "type": "SpatialConcept"}, {"text": "County", "type": "SpatialConcept"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: From 5 analyzed samples from Brod - Posavina County , one of the samples contained citrinin in the amount of 23 .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "Brod - Posavina County", "type": "SpatialConcept"}, {"text": "citrinin", "type": "Chemical"}]}

Example input:
Sentence: The main goal of this study was to determine the presence of Citrinin in grains sampled in the area of Međimurje , Osijek - Baranja , Vukovar - Srijem and Brod - Posavina County .

Example answer:
{"entities": [{"text": "main goal", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "presence of", "type": "Finding"}, {"text": "Citrinin", "type": "Chemical"}, {"text": "grains", "type": "Food"}, {"text": "area", "type": "SpatialConcept"}, {"text": "Međimurje", "type": "SpatialConcept"}, {"text": "Osijek - Baranja", "type": "SpatialConcept"}, {"text": "Vukovar - Srijem", "type": "SpatialConcept"}, {"text": "Brod - Posavina County", "type": "SpatialConcept"}]}

Input:
Sentence: The mean value for the samples of Osijek - Baranja County was 19 . 63 μg / kg ( median = 15 . 8 μg / kg ) , while for Vukovar - Srijem County the mean value of citrinin was 14 , 6 μg / kg ( median = 1 . 23 μg / kg ) .

## Item MedMentions:test:4272
Example input:
Sentence: P - glycoprotein traffics from the nucleus to the plasma membrane in rat brain endothelium during inflammatory pain P - glycoprotein ( PgP ) , a drug efflux pump in blood - brain barrier endothelial cells , is a major clinical obstacle for effective central nervous system drug delivery .

Example answer:
{"entities": [{"text": "P - glycoprotein", "type": "Chemical"}, {"text": "nucleus", "type": "AnatomicalStructure"}, {"text": "plasma membrane", "type": "AnatomicalStructure"}, {"text": "rat brain", "type": "AnatomicalStructure"}, {"text": "endothelium", "type": "AnatomicalStructure"}, {"text": "inflammatory pain", "type": "Finding"}, {"text": "PgP", "type": "Chemical"}, {"text": "drug", "type": "Chemical"}, {"text": "efflux pump", "type": "AnatomicalStructure"}, {"text": "blood - brain barrier", "type": "AnatomicalStructure"}, {"text": "endothelial cells", "type": "AnatomicalStructure"}, {"text": "central nervous system", "type": "BodySystem"}, {"text": "drug delivery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Strikingly , AAV9 - mediated NPC1 delivery significantly promoted Purkinje cell survival , restored locomotor activity and coordination , and increased the lifespan of NPC1 ( - / - ) mice .

Example answer:
{"entities": [{"text": "Purkinje cell", "type": "AnatomicalStructure"}, {"text": "locomotor activity", "type": "BiologicFunction"}, {"text": "coordination", "type": "BiologicFunction"}, {"text": "NPC1 ( - / - )", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: STEP61 protein is also increased in cortical lysates from the central nervous system - specific ErbB2 / 4 mouse model of SZ , as well as in human induced pluripotent stem cell ( hiPSC ) - derived forebrain neurons and Ngn2 - induced excitatory neurons , from two independent SZ patient cohorts .

Example answer:
{"entities": [{"text": "STEP61 protein", "type": "Chemical"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "central nervous system", "type": "BodySystem"}, {"text": "ErbB2", "type": "Chemical"}, {"text": "4", "type": "Chemical"}, {"text": "mouse model", "type": "BiologicFunction"}, {"text": "SZ", "type": "BiologicFunction"}, {"text": "human induced pluripotent stem cell", "type": "AnatomicalStructure"}, {"text": "hiPSC", "type": "AnatomicalStructure"}, {"text": "forebrain", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "Ngn2", "type": "AnatomicalStructure"}, {"text": "excitatory neurons", "type": "AnatomicalStructure"}, {"text": "cohorts", "type": "PopulationGroup"}]}

Example input:
Sentence: We previously found that PgP activity increases in rat brain microvessels concomitant with decreased central nervous system drug delivery in response to acute peripheral inflammatory pain .

Example answer:
{"entities": [{"text": "PgP activity", "type": "BiologicFunction"}, {"text": "rat brain", "type": "AnatomicalStructure"}, {"text": "microvessels", "type": "AnatomicalStructure"}, {"text": "central nervous system", "type": "BodySystem"}, {"text": "drug delivery", "type": "HealthCareActivity"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "inflammatory pain", "type": "Finding"}]}

Example input:
Sentence: By targeting Pten in cerebellar granule cells and activating the AKT1 - mTOR pathway , we increased the caliber of normally unmyelinated axons and the expression of numerous genes encoding regulatory proteins .

Example answer:
{"entities": [{"text": "Pten", "type": "Chemical"}, {"text": "cerebellar granule cells", "type": "AnatomicalStructure"}, {"text": "AKT1", "type": "Chemical"}, {"text": "mTOR", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "unmyelinated axons", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "regulatory proteins", "type": "Chemical"}]}

Example input:
Sentence: Comparative gene expression profiling of motor neurons innervating the extensor digitorum longus ( disease - resistant ) , gastrocnemius ( intermediate vulnerability ) , and tibialis anterior ( vulnerable ) muscles in mice revealed that disease susceptibility correlates strongly with a modified bioenergetic profile .

Example answer:
{"entities": [{"text": "gene expression profiling", "type": "HealthCareActivity"}, {"text": "motor neurons", "type": "AnatomicalStructure"}, {"text": "extensor digitorum longus", "type": "AnatomicalStructure"}, {"text": "disease - resistant", "type": "BiologicFunction"}, {"text": "gastrocnemius", "type": "AnatomicalStructure"}, {"text": "tibialis anterior", "type": "AnatomicalStructure"}, {"text": "muscles", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "disease susceptibility", "type": "ClinicalAttribute"}, {"text": "bioenergetic", "type": "BiologicFunction"}, {"text": "profile", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here , we demonstrate that selective vulnerability of distinct motor neuron pools arises from fundamental modifications to their basal molecular profiles .

Example answer:
{"entities": [{"text": "motor neuron", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We conclude that global bioenergetics pathways can be therapeutically manipulated to ameliorate SMA motor neuron phenotypes in vivo .

Example answer:
{"entities": [{"text": "bioenergetics", "type": "BiologicFunction"}, {"text": "SMA", "type": "BiologicFunction"}, {"text": "motor neuron", "type": "AnatomicalStructure"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: Bioenergetic status modulates motor neuron vulnerability and pathogenesis in a zebrafish model of spinal muscular atrophy Degeneration and loss of lower motor neurons is the major pathological hallmark of spinal muscular atrophy ( SMA ) , resulting from low levels of ubiquitously - expressed survival motor neuron ( SMN ) protein .

Example answer:
{"entities": [{"text": "Bioenergetic", "type": "BiologicFunction"}, {"text": "modulates", "type": "SpatialConcept"}, {"text": "motor neuron", "type": "AnatomicalStructure"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "zebrafish", "type": "Eukaryote"}, {"text": "model", "type": "BiologicFunction"}, {"text": "spinal muscular atrophy", "type": "BiologicFunction"}, {"text": "Degeneration and loss of lower motor neurons", "type": "Finding"}, {"text": "SMA", "type": "BiologicFunction"}, {"text": "survival motor neuron ( SMN ) protein", "type": "Chemical"}]}

Example input:
Sentence: Conversely , Pgk1 overexpression , or treatment with terazosin ( an FDA -approved small molecule that binds and activates Pgk1 ) , rescued motor axon phenotypes in SMA zebrafish .

Example answer:
{"entities": [{"text": "Pgk1", "type": "AnatomicalStructure"}, {"text": "overexpression", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "terazosin", "type": "Chemical"}, {"text": "FDA", "type": "IntellectualProduct"}, {"text": "small molecule", "type": "Chemical"}, {"text": "Pgk1", "type": "Chemical"}, {"text": "motor axon", "type": "AnatomicalStructure"}, {"text": "SMA", "type": "BiologicFunction"}, {"text": "zebrafish", "type": "Eukaryote"}]}

Input:
Sentence: Moreover , targeting of a single bioenergetic protein , phosphoglycerate kinase 1 ( Pgk1 ) , was found to modulate motor neuron vulnerability in vivo .

## Item MedMentions:test:4524
Example input:
Sentence: Biochemical studies of amylase , lipase and protease in Callosobruchus maculatus ( Coleoptera : Chrysomelidae ) populations fed with Vigna unguiculata grain cultivated with diazotrophic bacteria strains The objective of this study was to evaluate the enzymatic activity of homogenates of insects fed on grain of cowpea , Vigna unguiculata ( L . ) , cultivars grown with different nitrogen sources .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "amylase", "type": "Chemical"}, {"text": "lipase", "type": "Chemical"}, {"text": "protease", "type": "Chemical"}, {"text": "Callosobruchus maculatus", "type": "Eukaryote"}, {"text": "Coleoptera", "type": "Eukaryote"}, {"text": "Chrysomelidae", "type": "Eukaryote"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "Vigna unguiculata", "type": "Eukaryote"}, {"text": "grain", "type": "Food"}, {"text": "cultivated", "type": "ResearchActivity"}, {"text": "diazotrophic bacteria strains", "type": "Bacterium"}, {"text": "study", "type": "ResearchActivity"}, {"text": "enzymatic activity", "type": "BiologicFunction"}, {"text": "insects", "type": "Eukaryote"}, {"text": "cowpea", "type": "Eukaryote"}, {"text": "Vigna unguiculata ( L . )", "type": "Eukaryote"}, {"text": "cultivars", "type": "Eukaryote"}, {"text": "nitrogen", "type": "Chemical"}]}

Example input:
Sentence: The CAZyme profile was dominated by families GH94 ( cellobiose - phosphorylase ) , GH13 ( amylase ) , GH43 and GH10 ( hemicellulases ) , GH9 and GH48 ( cellulases ) , PL11 ( pectinase ) as well as GH2 and GH3 ( oligosaccharidases ) .

Example answer:
{"entities": [{"text": "CAZyme", "type": "Chemical"}, {"text": "GH94", "type": "Chemical"}, {"text": "cellobiose - phosphorylase", "type": "Chemical"}, {"text": "GH13", "type": "Chemical"}, {"text": "amylase", "type": "Chemical"}, {"text": "GH43", "type": "Chemical"}, {"text": "GH10", "type": "Chemical"}, {"text": "hemicellulases", "type": "Chemical"}, {"text": "GH9", "type": "Chemical"}, {"text": "GH48", "type": "Chemical"}, {"text": "cellulases", "type": "Chemical"}, {"text": "PL11", "type": "Chemical"}, {"text": "pectinase", "type": "Chemical"}, {"text": "GH2", "type": "Chemical"}, {"text": "GH3", "type": "Chemical"}, {"text": "oligosaccharidases", "type": "Chemical"}]}

Example input:
Sentence: Multiple regression analysis showed significant positive correlations between acyl ghrelin and PG I levels ( β = 0 . 738 , p < 0 . 001 ) and significant negative correlations between ghrelin and age , albumin , and creatinine levels .

Example answer:
{"entities": [{"text": "Multiple regression analysis", "type": "IntellectualProduct"}, {"text": "acyl ghrelin", "type": "Chemical"}, {"text": "PG I", "type": "Chemical"}, {"text": "ghrelin", "type": "Chemical"}, {"text": "albumin", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: A predominance of glycoside hydrolases was observed in soil , and a higher contribution of enzymes involved in carbohydrate biosynthesis was observed in freshwater .

Example answer:
{"entities": [{"text": "glycoside hydrolases", "type": "Chemical"}, {"text": "enzymes", "type": "Chemical"}, {"text": "carbohydrate biosynthesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Fermentable carbohydrates ( sugars and starches ) were the most relevant common dietary risk factor for both diseases , but associated mechanisms differed .

Example answer:
{"entities": [{"text": "Fermentable carbohydrates", "type": "Chemical"}]}

Example input:
Sentence: The transgenic lines also showed a significant increase in starch content , whereas total protein content decreased significantly .

Example answer:
{"entities": [{"text": "transgenic lines", "type": "Eukaryote"}, {"text": "starch", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}]}

Example input:
Sentence: We investigated the association of low SA with diabetes and sex - specific associations of serum amylase with abdominal fat in older adults .

Example answer:
{"entities": [{"text": "SA", "type": "Finding"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "serum", "type": "BodySubstance"}, {"text": "amylase", "type": "Chemical"}, {"text": "abdominal fat", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The parameters evaluated were enzymatic activities of insect protease , amylase and lipase and the starch content of the grains .

Example answer:
{"entities": [{"text": "enzymatic activities", "type": "BiologicFunction"}, {"text": "insect", "type": "Eukaryote"}, {"text": "protease", "type": "Chemical"}, {"text": "amylase", "type": "Chemical"}, {"text": "lipase", "type": "Chemical"}, {"text": "starch", "type": "Chemical"}, {"text": "grains", "type": "Food"}]}

Example input:
Sentence: A lower activity of the enzyme amylase from C . maculatus homogenate was observed when insects were fed grain of the cultivar BRS Carijó .

Example answer:
{"entities": [{"text": "activity of the enzyme", "type": "BiologicFunction"}, {"text": "amylase", "type": "Chemical"}, {"text": "C . maculatus", "type": "Eukaryote"}, {"text": "insects", "type": "Eukaryote"}, {"text": "grain", "type": "Food"}, {"text": "cultivar BRS Carijó", "type": "Eukaryote"}]}

Example input:
Sentence: RESULTS There were statistically significant differences between the C group and the Control group in the values of pancreatic amylase , lipase , blood leukocyte , hematocrit , pH , pO2 , pCO2 , HCO3 , and pancreatic water content , and also in each of the values of edema , inflammation , vacuolization , necrosis , and total histopathological score ( P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "C", "type": "Chemical"}, {"text": "group", "type": "PopulationGroup"}, {"text": "pancreatic amylase", "type": "Chemical"}, {"text": "lipase", "type": "Chemical"}, {"text": "blood leukocyte", "type": "AnatomicalStructure"}, {"text": "hematocrit", "type": "Finding"}, {"text": "pO2", "type": "BiologicFunction"}, {"text": "pCO2", "type": "Finding"}, {"text": "HCO3", "type": "Chemical"}, {"text": "pancreatic", "type": "AnatomicalStructure"}, {"text": "edema", "type": "Finding"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "vacuolization", "type": "Finding"}, {"text": "necrosis", "type": "BiologicFunction"}]}

Input:
Sentence: Starch content correlated positively with the amylase activity of C .

## Item MedMentions:test:4619
Example input:
Sentence: Additionally , this increase may predispose individuals to numerous negative health outcomes if left untreated .

Example answer:
{"entities": [{"text": "individuals", "type": "PopulationGroup"}, {"text": "negative", "type": "Finding"}, {"text": "untreated", "type": "Finding"}]}

Example input:
Sentence: Overview of findings from a 2 - year study of claimants who had sustained a mild or moderate injury in a road traffic crash : prospective study Studies have shown that in people injured in a road traffic crash , persistent symptoms are common and can lead to significant ongoing personal impact .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "traffic crash", "type": "InjuryOrPoisoning"}, {"text": "prospective study", "type": "ResearchActivity"}, {"text": "people", "type": "PopulationGroup"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: As a result , the aftermath is chewing disability and damage to self - esteem due to an altered self - image .

Example answer:
{"entities": [{"text": "chewing", "type": "BiologicFunction"}, {"text": "disability", "type": "Finding"}, {"text": "self - esteem", "type": "BiologicFunction"}, {"text": "self - image", "type": "BiologicFunction"}]}

Example input:
Sentence: 6 % , and the long - term complications , from zero to 7 . 86 % .

Example answer:
{"entities": [{"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: No differences in long - term complications were found .

Example answer:
{"entities": [{"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: Along with its many outcome benefits come the potential for adverse effects .

Example answer:
{"entities": [{"text": "adverse effects", "type": "BiologicFunction"}]}

Example input:
Sentence: It may result in major physical disabilities and significant loss of school years .

Example answer:
{"entities": [{"text": "physical disabilities", "type": "BiologicFunction"}, {"text": "school", "type": "Organization"}]}

Example input:
Sentence: Adverse post - traumatic sequelae are common , morbid and costly public health problems in the USA and other industrialised countries .

Example answer:
{"entities": [{"text": "Adverse post - traumatic sequelae", "type": "BiologicFunction"}, {"text": "morbid", "type": "Finding"}, {"text": "USA", "type": "SpatialConcept"}]}

Example input:
Sentence: This inequality is in turn related to negative health consequences , specifically violence against women , children , and other men , as well as sexual risk .

Example answer:
{"entities": [{"text": "violence", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}, {"text": "sexual risk", "type": "Finding"}]}

Example input:
Sentence: We found that minor injuries had major impacts on pain ratings , physical and mental well - being , health -related quality of life and return to work and pre - injury participation during the 24 months post - injury phase .

Example answer:
{"entities": [{"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "pain", "type": "Finding"}, {"text": "ratings", "type": "IntellectualProduct"}, {"text": "physical", "type": "Finding"}, {"text": "mental well - being", "type": "BiologicFunction"}, {"text": "pre - injury", "type": "InjuryOrPoisoning"}, {"text": "post - injury", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: injuries ) and long - term negative consequences ( e . g .

## Item MedMentions:test:4348
Example input:
Sentence: Our study showed that the recombinant protein rIBPv exhibited a thermal hysteresis of 2 ° C at concentrations of > 50 μM , effectively inhibited ice recrystallization , and enhanced bacterial viability during freeze - thaw cycling .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "recombinant protein", "type": "Chemical"}, {"text": "rIBPv", "type": "Chemical"}, {"text": "hysteresis", "type": "Finding"}, {"text": "ice", "type": "Chemical"}]}

Example input:
Sentence: The BEACH - containing protein WDR81 coordinates p62 and LC3C to promote aggrephagy Autophagy -dependent clearance of ubiquitinated and aggregated proteins is critical to protein quality control , but the underlying mechanisms are not well understood .

Example answer:
{"entities": [{"text": "BEACH - containing protein", "type": "Chemical"}, {"text": "WDR81", "type": "Chemical"}, {"text": "p62", "type": "Chemical"}, {"text": "LC3C", "type": "Chemical"}, {"text": "aggrephagy", "type": "BiologicFunction"}, {"text": "Autophagy", "type": "BiologicFunction"}, {"text": "ubiquitinated and aggregated proteins", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}]}

Example input:
Sentence: Functional Analysis of a Bacterial Antifreeze Protein Indicates a Cooperative Effect between Its Two Ice - Binding Domains Antifreeze proteins make up a class of ice - binding proteins ( IBPs ) that are possessed and expressed by certain cold - adapted organisms to enhance their freezing tolerance .

Example answer:
{"entities": [{"text": "Analysis", "type": "ResearchActivity"}, {"text": "Bacterial", "type": "Bacterium"}, {"text": "Antifreeze Protein", "type": "Chemical"}, {"text": "Cooperative", "type": "Finding"}, {"text": "Ice - Binding", "type": "BiologicFunction"}, {"text": "Domains", "type": "SpatialConcept"}, {"text": "Antifreeze proteins", "type": "Chemical"}, {"text": "ice - binding proteins", "type": "Chemical"}, {"text": "IBPs", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "adapted", "type": "BiologicFunction"}, {"text": "freezing tolerance", "type": "BiologicFunction"}]}

Example input:
Sentence: Uncoupling protein 2 downregulation by hypoxia through repression of peroxisome proliferator - activated receptor γ promotes chemoresistance of non - small cell lung cancer Hypoxic microenvironment is critically involved in the response of non - small cell lung cancer ( NSCLC ) to chemotherapy , the mechanisms of which remain largely unknown .

Example answer:
{"entities": [{"text": "Uncoupling protein 2", "type": "Chemical"}, {"text": "downregulation", "type": "BiologicFunction"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "repression", "type": "BiologicFunction"}, {"text": "peroxisome proliferator - activated receptor γ", "type": "Chemical"}, {"text": "chemoresistance", "type": "BiologicFunction"}, {"text": "non - small cell lung cancer", "type": "BiologicFunction"}, {"text": "Hypoxic", "type": "BiologicFunction"}, {"text": "microenvironment", "type": "SpatialConcept"}, {"text": "NSCLC", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Incubation at temperatures just below the thermal melting transition , above which the protein aggregates , was also found to anneal the enzyme to give an increased specific activity .

Example answer:
{"entities": [{"text": "Incubation", "type": "HealthCareActivity"}, {"text": "protein", "type": "Chemical"}, {"text": "enzyme", "type": "Chemical"}, {"text": "activity", "type": "BiologicFunction"}]}

Example input:
Sentence: We used the expressed pig UCP1 protein as antigen for antibody production in a rabbit .

Example answer:
{"entities": [{"text": "expressed", "type": "BiologicFunction"}, {"text": "pig", "type": "Eukaryote"}, {"text": "UCP1 protein", "type": "Chemical"}, {"text": "antigen", "type": "Chemical"}, {"text": "antibody production", "type": "BiologicFunction"}, {"text": "rabbit", "type": "Eukaryote"}]}

Example input:
Sentence: The downregulation of uncoupling protein 2 ( UCP2 ) , which is attributed to hypoxia - inducible factor 1 ( HIF - 1 ) - mediated suppression of the transcriptional factor peroxisome proliferator - activated receptor γ ( PPARγ ) , was involved in NSCLC chemoresistance , and predicted a poor survival rate of patients receiving routine chemotherapy .

Example answer:
{"entities": [{"text": "downregulation", "type": "BiologicFunction"}, {"text": "uncoupling protein 2", "type": "Chemical"}, {"text": "UCP2", "type": "Chemical"}, {"text": "hypoxia - inducible factor 1", "type": "Chemical"}, {"text": "HIF - 1", "type": "Chemical"}, {"text": "suppression", "type": "BiologicFunction"}, {"text": "transcriptional factor", "type": "Chemical"}, {"text": "peroxisome proliferator - activated receptor γ", "type": "Chemical"}, {"text": "PPARγ", "type": "Chemical"}, {"text": "NSCLC", "type": "BiologicFunction"}, {"text": "chemoresistance", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Specifically , we will provide a step - by - step description of the following procedures : quantification of BAT in vivo using positron emission tomography - computed tomography ( PET / CT ) with 2 - deoxy - 2 - [ ( 18 ) F ] fluoroglucose ( ( 18 ) F - FDG ) as a tracer , mitochondrial respiration , and uncoupling protein 1 ( UCP1 ) gene and protein expression .

Example answer:
{"entities": [{"text": "description", "type": "IntellectualProduct"}, {"text": "BAT", "type": "AnatomicalStructure"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "positron emission tomography - computed tomography", "type": "HealthCareActivity"}, {"text": "PET / CT", "type": "HealthCareActivity"}, {"text": "2 - deoxy - 2 - [ ( 18 ) F ] fluoroglucose", "type": "Chemical"}, {"text": "( 18 ) F - FDG", "type": "Chemical"}, {"text": "tracer", "type": "Chemical"}, {"text": "mitochondrial", "type": "AnatomicalStructure"}, {"text": "respiration", "type": "BiologicFunction"}, {"text": "uncoupling protein 1 ( UCP1 ) gene", "type": "AnatomicalStructure"}, {"text": "protein expression", "type": "BiologicFunction"}]}

Example input:
Sentence: However , whether BAT or more precisely UCP1 protein exists in pig remains a controversy .

Example answer:
{"entities": [{"text": "BAT", "type": "AnatomicalStructure"}, {"text": "UCP1 protein", "type": "Chemical"}, {"text": "pig", "type": "Eukaryote"}]}

Example input:
Sentence: Pig has no uncoupling protein 1 Brown adipose tissue ( BAT ) is critical for mammal 's survival in the cold environment .

Example answer:
{"entities": [{"text": "Pig", "type": "Eukaryote"}, {"text": "no", "type": "Finding"}, {"text": "uncoupling protein 1", "type": "Chemical"}, {"text": "Brown adipose tissue", "type": "AnatomicalStructure"}, {"text": "BAT", "type": "AnatomicalStructure"}, {"text": "mammal 's", "type": "Eukaryote"}]}

Input:
Sentence: Uncoupling protein 1 ( UCP1 ) is responsible for the non - shivering thermogenesis in the BAT .

## Item MedMentions:test:4646
Example input:
Sentence: During 12 months , the mean speech recognition score increased from 30 to 41 % for monosyllabic words in adults , and from 58 to 89 % for multisyllabic numbers .

Example answer:
{"entities": [{"text": "monosyllabic words", "type": "IntellectualProduct"}, {"text": "multisyllabic", "type": "IntellectualProduct"}]}

Example input:
Sentence: Among all participants , 205 ( 30 % ) experienced cognitive decline during the study period .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "cognitive decline", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Overall , 676 participants with intact baseline cognitive function ( measured by the Short Portable Mental Status Questionnaire ) were enrolled and followed for six years .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "cognitive function", "type": "BiologicFunction"}, {"text": "Short Portable Mental Status Questionnaire", "type": "IntellectualProduct"}]}

Example input:
Sentence: The mean score for satisfaction across the six dimensions was 4 . 56 in the collaborative care group and 4 . 30 in the traditional physician group ( p = 0 . 02 ) .

Example answer:
{"entities": [{"text": "mean score for satisfaction", "type": "IntellectualProduct"}, {"text": "six dimensions", "type": "SpatialConcept"}, {"text": "collaborative care group", "type": "Organization"}, {"text": "traditional physician group", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Mean CORE - index score in the total sample was 3 . 06 ( sd 1 . 92 ) units ( range 0 - 11 units ) .

Example answer:
{"entities": [{"text": "Mean CORE - index score", "type": "IntellectualProduct"}]}

Example input:
Sentence: The Clinical Dementia Rating scale - Sum of Boxes ( CDR - SB ) score exhibited significant negative relationships with the average GCIPL thickness ( β = -0 .

Example answer:
{"entities": [{"text": "Clinical Dementia Rating scale - Sum of Boxes", "type": "IntellectualProduct"}, {"text": "CDR - SB", "type": "IntellectualProduct"}, {"text": "negative", "type": "Finding"}, {"text": "average GCIPL", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Any increasing score of the Short Portable Mental Status Questionnaire in the observational period was referred to as cognitive function decline .

Example answer:
{"entities": [{"text": "Short Portable Mental Status Questionnaire", "type": "IntellectualProduct"}, {"text": "observational", "type": "HealthCareActivity"}, {"text": "cognitive function decline", "type": "BiologicFunction"}]}

Example input:
Sentence: Cognitive function was assessed at baseline and week 8 .

Example answer:
{"entities": [{"text": "Cognitive function", "type": "BiologicFunction"}]}

Example input:
Sentence: Neuropsychological tests were carried out using the AD Assessment Scale - cognitive subscale ( ADAS - cog ) , Mini - Mental State Examination ( MMSE ) , Montreal Cognitive Assessment ( MoCA ) , and World Health Organization University of California - Los Angeles , Auditory Verbal Learning Test ( WHO - UCLA AVLT ) before , immediately after , and 6 weeks after the intervention .

Example answer:
{"entities": [{"text": "Neuropsychological tests", "type": "HealthCareActivity"}, {"text": "AD Assessment Scale", "type": "IntellectualProduct"}, {"text": "cognitive subscale", "type": "IntellectualProduct"}, {"text": "ADAS", "type": "IntellectualProduct"}, {"text": "cog", "type": "IntellectualProduct"}, {"text": "Mini - Mental State Examination", "type": "HealthCareActivity"}, {"text": "MMSE", "type": "HealthCareActivity"}, {"text": "Montreal Cognitive Assessment", "type": "IntellectualProduct"}, {"text": "MoCA", "type": "IntellectualProduct"}, {"text": "World Health Organization University of California - Los Angeles , Auditory Verbal Learning Test", "type": "IntellectualProduct"}, {"text": "WHO - UCLA AVLT", "type": "IntellectualProduct"}, {"text": "intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: Cognitive impairment was defined as a total Montreal Cognitive Assessment tool score ≤24 / 30 .

Example answer:
{"entities": [{"text": "Cognitive impairment", "type": "BiologicFunction"}, {"text": "Montreal Cognitive Assessment tool", "type": "IntellectualProduct"}]}

Input:
Sentence: Mean Cognitive Performance Scale score was 4 .

## Item MedMentions:test:4742
Example input:
Sentence: 23 ± 0 . 27 ng / mL [ P = .01 ] ; group 3 : 0 . 19 ± 0 . 34 ng / mL [ P = .01 ] ) .

Example answer:
{"entities": [{"text": "group 3", "type": "IntellectualProduct"}]}

Example input:
Sentence: 26 . 0 mm / mm ( 2 ) ; P ≤ 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 66 ± 0 . 41 mm .

Example answer:
{"entities": []}

Example input:
Sentence: 1 mm ( 2 ) ( p < 0 . 05 ) at final follow - up as assessed by CT , and from 154 . 1 ± 93 .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}]}

Example input:
Sentence: The mean areas were 8 . 64 ± 2 . 59 mm3 in non - deviated cases ( n = 27 ) and 2 . 59 ± 1 . 68 mm3 in deviated ( n = 10 ) .

Example answer:
{"entities": []}

Example input:
Sentence: At random , patients received an implant with a 1 . 5 mm smooth neck ( " smooth group " ) , a rough neck with grooves ( " rough group " ) or a scalloped rough neck with grooves ( " scalloped group " ) .

Example answer:
{"entities": [{"text": "implant", "type": "MedicalDevice"}]}

Example input:
Sentence: 88 ± 1 . 75 mm .

Example answer:
{"entities": []}

Example input:
Sentence: 97 mm in the scalloped group ( P < .05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 85 ± 0 . 27 mm and 0 . 87 ± 0 . 28 mm , was lower than the values obtained by manual and automated probing .

Example answer:
{"entities": [{"text": "probing", "type": "HealthCareActivity"}]}

Example input:
Sentence: 2 % for the smooth and scalloped group and 100 % for the rough group .

Example answer:
{"entities": []}

Input:
Sentence: 1 mm in the rough group and 2 . 28 ± 0 .

## Item MedMentions:test:4536
Example input:
Sentence: Seventeen subjects completed the trial .

Example answer:
{"entities": [{"text": "subjects", "type": "PopulationGroup"}, {"text": "trial", "type": "ResearchActivity"}]}

Example input:
Sentence: 1 . Eight randomized controlled trials ( RCTs ) that involved 511 patients met the criteria .

Example answer:
{"entities": [{"text": "1", "type": "IntellectualProduct"}, {"text": "randomized controlled trials", "type": "ResearchActivity"}, {"text": "RCTs", "type": "ResearchActivity"}]}

Example input:
Sentence: Most trials concluded non - inferiority ( 132 ; 79 % ) .

Example answer:
{"entities": [{"text": "trials", "type": "ResearchActivity"}, {"text": "non - inferiority", "type": "Finding"}]}

Example input:
Sentence: Time , scores and patterns of puncture - site selection were compared with respect to three different methods : [ 1 ] attempt 1 ( tourniquet only ) , [ 2 ] attempt 2 ( Vein Display only ) and [ 3 ] attempt 3 ( both ) .

Example answer:
{"entities": [{"text": "puncture", "type": "HealthCareActivity"}, {"text": "site", "type": "SpatialConcept"}, {"text": "tourniquet", "type": "MedicalDevice"}, {"text": "Vein Display", "type": "MedicalDevice"}]}

Example input:
Sentence: The experiment was repeated ten times in different sessions .

Example answer:
{"entities": [{"text": "experiment", "type": "ResearchActivity"}, {"text": "sessions", "type": "HealthCareActivity"}]}

Example input:
Sentence: All subjects performed a pre - test , a training of ten practice trials on a single day , and a post - test balance test .

Example answer:
{"entities": [{"text": "practice", "type": "BiologicFunction"}]}

Example input:
Sentence: Best - of - rule and mean - of - rule scorings were significantly different except for the best - of - two vs .

Example answer:
{"entities": []}

Example input:
Sentence: When Is a Test Score Fair for the Individual Who Is Being Tested ? Effects of Different Scoring Procedures across Multiple Attempts When Testing a Motor Skill Task Tests or test batteries used for assessing motor skills , either in research studies or in clinical settings , apply a variety of procedures for scoring performances , including everything from one to ten attempts , of which the best is scored or an average is computed .

Example answer:
{"entities": [{"text": "Individual", "type": "PopulationGroup"}, {"text": "Tested", "type": "IntellectualProduct"}, {"text": "Scoring Procedures", "type": "ResearchActivity"}, {"text": "Motor Skill", "type": "BiologicFunction"}, {"text": "Tests", "type": "IntellectualProduct"}, {"text": "test batteries", "type": "IntellectualProduct"}, {"text": "motor skills", "type": "BiologicFunction"}, {"text": "research studies", "type": "ResearchActivity"}, {"text": "clinical settings", "type": "ResearchActivity"}, {"text": "scoring", "type": "ResearchActivity"}, {"text": "computed", "type": "HealthCareActivity"}]}

Example input:
Sentence: The first trial was significantly different from the remaining both as a raw score and as scoring procedure .

Example answer:
{"entities": [{"text": "scoring", "type": "ResearchActivity"}]}

Example input:
Sentence: The rationale behind scoring procedures is rarely stated , and it seems that the number of attempts allowed is decided without much qualification from research .

Example answer:
{"entities": [{"text": "scoring", "type": "ResearchActivity"}, {"text": "research", "type": "ResearchActivity"}]}

Input:
Sentence: They were given 10 attempts , and trials were scored according to nine different procedures including the ' best of ' or ' mean of ' either one , two , three , five , or ten attempts .

## Item MedMentions:test:4753
Example input:
Sentence: 5 % and 55 . 3 % , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 5 % , P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 5 % , 19 . 6 % to 5 .

Example answer:
{"entities": []}

Example input:
Sentence: 9 % and 99 . 2 % , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % on d5 ( P = .0049 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 05 for both groups .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: 05 - P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 1 % of samples followed by V600 K ( 25 % ) and V600R ( 3 .

Example answer:
{"entities": [{"text": "V600 K", "type": "Finding"}, {"text": "V600R", "type": "Finding"}]}

Example input:
Sentence: 05 , 99 . 0 / 0 . 8 / 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 % to 7 . 88±0 . 04 % .

Example answer:
{"entities": []}

Input:
Sentence: 05 , for 89 . 8 - 100 % of samples .

## Item MedMentions:test:4043
Example input:
Sentence: During this process , PEO block chains selectively interact with CTA by strong interpolymer hydrogen - bonding while PPO block microseparated .

Example answer:
{"entities": [{"text": "PEO block chains", "type": "Chemical"}, {"text": "CTA", "type": "Chemical"}, {"text": "interpolymer", "type": "Chemical"}, {"text": "PPO block", "type": "Chemical"}]}

Example input:
Sentence: PVA - TiO2 nanocomposite films with desirable mechanical , thermal and biocompatible properties are fabricated through solution casting method followed by de - hydrothermal cross - linking treatment .

Example answer:
{"entities": [{"text": "PVA", "type": "Chemical"}, {"text": "TiO2", "type": "Chemical"}]}

Example input:
Sentence: In this study , we fabricated three - dimensional composite nanofibre macrostructures of polycaprolactone ( PCL ) with different concentrations of polyaniline ( PANi ) by employing an improved electrospinning technology with a specially designed collector .

Example answer:
{"entities": [{"text": "three - dimensional", "type": "SpatialConcept"}, {"text": "composite", "type": "Chemical"}, {"text": "macrostructures", "type": "SpatialConcept"}, {"text": "polycaprolactone", "type": "Chemical"}, {"text": "PCL", "type": "Chemical"}, {"text": "polyaniline", "type": "Chemical"}, {"text": "PANi", "type": "Chemical"}]}

Example input:
Sentence: Here , we report on a random copolymer brush surface - poly ( CBMAA - ran - HPMAA ) - providing high BRE immobilization capacity while simultaneously exhibiting ultralow - fouling behavior in complex food media .

Example answer:
{"entities": [{"text": "random copolymer brush", "type": "Chemical"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "poly ( CBMAA - ran - HPMAA )", "type": "Chemical"}, {"text": "BRE", "type": "Chemical"}, {"text": "complex food media", "type": "Food"}]}

Example input:
Sentence: SEM studies illustrate improved surface morphology of PVA - TiO2 nanocomposite film with homogenously distributed TiO2 nanoparticles , which help to enhance thermo - mechanical behavior .

Example answer:
{"entities": [{"text": "SEM studies", "type": "HealthCareActivity"}, {"text": "PVA", "type": "Chemical"}, {"text": "TiO2", "type": "Chemical"}, {"text": "homogenously", "type": "SpatialConcept"}]}

Example input:
Sentence: The triblock EPE was chosen since PEO blocks interact favorably with CTA , whereas , PPO blocks remain immiscible which provokes a microphase separation .

Example answer:
{"entities": [{"text": "triblock EPE", "type": "Chemical"}, {"text": "PEO blocks", "type": "Chemical"}, {"text": "CTA", "type": "Chemical"}, {"text": "PPO blocks", "type": "Chemical"}]}

Example input:
Sentence: The addition even 40wt % of EPE leads to nanostructured EPE / CTA composite .

Example answer:
{"entities": [{"text": "EPE", "type": "Chemical"}, {"text": "CTA", "type": "Chemical"}]}

Example input:
Sentence: This allows to obtain EPE / CTA composite films with ordered microphase - separated structures where PPO spherical microdomains are well - dispersed in PEO / CTA matrix by simple solvent - evaporation process .

Example answer:
{"entities": [{"text": "EPE", "type": "Chemical"}, {"text": "CTA", "type": "Chemical"}, {"text": "films", "type": "Chemical"}, {"text": "structures", "type": "SpatialConcept"}, {"text": "PPO", "type": "Chemical"}, {"text": "spherical", "type": "SpatialConcept"}, {"text": "PEO", "type": "Chemical"}, {"text": "matrix", "type": "Chemical"}, {"text": "solvent", "type": "Chemical"}]}

Example input:
Sentence: The cytotoxicity assay of CTA and EPE / CTA composite films confirm non - toxic character of designed transparent nanostructured composites based on sustainable matrices .

Example answer:
{"entities": [{"text": "cytotoxicity assay", "type": "HealthCareActivity"}, {"text": "CTA", "type": "Chemical"}, {"text": "EPE", "type": "Chemical"}, {"text": "films", "type": "Chemical"}, {"text": "matrices", "type": "Chemical"}]}

Example input:
Sentence: The effect of the addition of EPE triblock copolymer on the thermal stability , morphology , and mechanical properties of cellulose triacetate films was investigated .

Example answer:
{"entities": [{"text": "EPE triblock copolymer", "type": "Chemical"}, {"text": "cellulose triacetate", "type": "Chemical"}, {"text": "films", "type": "Chemical"}]}

Input:
Sentence: Transparent nanostructured cellulose acetate films based on the self assembly of PEO - b - PPO - b - PEO block copolymer In this study fabrication and characterization of transparent nanostructured composite films based on cellulose triacetate ( CTA ) and poly ( ethylene oxide ) - b - poly ( propylene oxide ) - b - poly ( ethylene oxide ) ( EPE ) triblock copolymer were presented .

## Item MedMentions:test:4500
Example input:
Sentence: This paper aims to review the current state of knowledge on the frequency of MPAs and dermatoglyphic abnormalities in mood disorders .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "MPAs", "type": "AnatomicalStructure"}, {"text": "dermatoglyphic abnormalities", "type": "AnatomicalStructure"}, {"text": "mood disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: For both production strategies proposed to design Gd -loaded cHANPs , a boosting of the relaxation rate T1 is observed since a T1 of 1562 is achieved with a 10 μM of Gd -loaded cHANPs while a similar value is reached with 100 μM of the relevant clinical Gd - DTPA in solution .

Example answer:
{"entities": [{"text": "Gd", "type": "Chemical"}, {"text": "Gd - DTPA", "type": "Chemical"}]}

Example input:
Sentence: There was also a significant difference in the means of vocal tract severity symptoms , namely for burning and aching between patients with vitamin D deficiency compared to patients with no vitamin D deficiency ( p value < 0 . 05 ) .

Example answer:
{"entities": [{"text": "tract", "type": "AnatomicalStructure"}, {"text": "symptoms", "type": "Finding"}, {"text": "burning", "type": "Finding"}, {"text": "aching", "type": "Finding"}, {"text": "vitamin D deficiency", "type": "BiologicFunction"}, {"text": "no", "type": "Finding"}]}

Example input:
Sentence: The voice / speech of 12 MG patients ( 7 with anti - AchR and 5 with anti - MuSK antibodies ) and 24 age - matched healthy controls was recorded and analyzed using electroglottography ( EGG ) and speech acoustics .

Example answer:
{"entities": [{"text": "voice", "type": "BiologicFunction"}, {"text": "speech", "type": "BiologicFunction"}, {"text": "MG", "type": "BiologicFunction"}, {"text": "anti - AchR", "type": "Chemical"}, {"text": "anti - MuSK antibodies", "type": "HealthCareActivity"}, {"text": "electroglottography", "type": "HealthCareActivity"}, {"text": "EGG", "type": "HealthCareActivity"}]}

Example input:
Sentence: MEP amplitudes were significantly increased during the mirror condition ( P = .005 ) in typically developing subjects and in patients with contralateral reorganization .

Example answer:
{"entities": [{"text": "MEP", "type": "BiologicFunction"}, {"text": "subjects", "type": "PopulationGroup"}, {"text": "contralateral reorganization", "type": "BiologicFunction"}]}

Example input:
Sentence: Voice disorder severity based on the Cepstral Spectral Index of Dysphonia ( KayPentax , Montvale , NJ ) for sustained vowels decreased ( improved ) from 41 ( SD = 41 ) to 25 ( SD = 21 ) points ; no change was observed for connected speech .

Example answer:
{"entities": [{"text": "Voice disorder", "type": "BiologicFunction"}, {"text": "Cepstral Spectral Index", "type": "IntellectualProduct"}, {"text": "Dysphonia", "type": "BiologicFunction"}, {"text": "KayPentax", "type": "Organization"}, {"text": "NJ", "type": "SpatialConcept"}, {"text": "improved", "type": "Finding"}, {"text": "no change", "type": "Finding"}, {"text": "connected speech", "type": "Finding"}]}

Example input:
Sentence: Quantitative methods for the assessment of dysarthrοphonia could facilitate the evaluation of these common MG symptoms .

Example answer:
{"entities": [{"text": "methods", "type": "IntellectualProduct"}, {"text": "assessment", "type": "HealthCareActivity"}, {"text": "dysarthrοphonia", "type": "Finding"}, {"text": "evaluation", "type": "HealthCareActivity"}, {"text": "MG", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: This study demonstrates that non - invasive physiological methods ( EGG and speech acoustics ) offer essential tools for the assessment of dysarthrophonia in MG patients .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "EGG", "type": "HealthCareActivity"}, {"text": "assessment", "type": "HealthCareActivity"}, {"text": "dysarthrophonia", "type": "Finding"}, {"text": "MG", "type": "BiologicFunction"}]}

Example input:
Sentence: For the analysis of voice , the variables that were found to distinguish MG patients compared to healthy controls were a higher average fundamental frequency ( P < 0 . 05 ) , a higher standard deviation of the average fundamental frequency ( P < 0 . 001 ) , a higher mean fundamental frequency of the vibrating vocal folds ( P < 0 .

Example answer:
{"entities": [{"text": "voice", "type": "BiologicFunction"}, {"text": "MG", "type": "BiologicFunction"}, {"text": "vibrating vocal folds", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The goal of this study was to investigate the phonatory ( sustained phonation and reading ) and speech ( diadochokinesis ) function in MG patients using quantitative measures .

Example answer:
{"entities": [{"text": "goal", "type": "IntellectualProduct"}, {"text": "phonatory", "type": "BiologicFunction"}, {"text": "phonation", "type": "BiologicFunction"}, {"text": "speech", "type": "BiologicFunction"}, {"text": "diadochokinesis", "type": "Finding"}, {"text": "function", "type": "BiologicFunction"}, {"text": "MG", "type": "BiologicFunction"}]}

Input:
Sentence: The analysis of diadochokinesis showed that MG patients had a higher mean duration of the silent interval between a series of repetitive /pa / syllables ( P < 0 . 05 ) , of the sound /t / ( P = 0 .

## Item MedMentions:test:4240
Example input:
Sentence: Subjects with at least one plaque ( height ≥2·5 mm ) on ultrasound were imaged using MRI .

Example answer:
{"entities": [{"text": "plaque", "type": "Finding"}, {"text": "ultrasound", "type": "HealthCareActivity"}, {"text": "imaged", "type": "IntellectualProduct"}, {"text": "MRI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Despite the advantages of US imaging , images are difficult to interpret during medical assessment .

Example answer:
{"entities": [{"text": "US imaging", "type": "HealthCareActivity"}, {"text": "medical assessment", "type": "HealthCareActivity"}]}

Example input:
Sentence: In particular US imaging has been shown to be reliable in foot and ankle assessment and offers a real - time effective imaging technique that is able to reliably confirm structural changes , such as thickening , and identify changes in the internal echo structure associated with diseased or damaged tissue .

Example answer:
{"entities": [{"text": "US imaging", "type": "HealthCareActivity"}, {"text": "assessment", "type": "HealthCareActivity"}, {"text": "imaging technique", "type": "HealthCareActivity"}, {"text": "structural", "type": "SpatialConcept"}, {"text": "thickening", "type": "Finding"}, {"text": "internal", "type": "SpatialConcept"}, {"text": "echo structure", "type": "ClinicalAttribute"}, {"text": "diseased", "type": "BiologicFunction"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Critical care ultrasonography requires that all image acquisition , image interpretation , and clinical applications of ultrasonography are personally performed by the critical care clinician at the point of care and that the information obtained is combined with the history , physical , and laboratory information .

Example answer:
{"entities": [{"text": "Critical care", "type": "HealthCareActivity"}, {"text": "ultrasonography", "type": "HealthCareActivity"}, {"text": "image interpretation", "type": "HealthCareActivity"}, {"text": "critical care", "type": "HealthCareActivity"}, {"text": "clinician", "type": "ProfessionalOrOccupationalGroup"}, {"text": "history", "type": "Finding"}]}

Example input:
Sentence: Point - of - care ultrasonography , when performed in ED for the diagnosis of AA , has high sensitivity and specificity and had a positive impact on the clinical decision making of EPs .

Example answer:
{"entities": [{"text": "Point - of - care", "type": "HealthCareActivity"}, {"text": "ultrasonography", "type": "HealthCareActivity"}, {"text": "ED", "type": "HealthCareActivity"}, {"text": "diagnosis", "type": "Finding"}, {"text": "AA", "type": "BiologicFunction"}, {"text": "clinical decision making", "type": "HealthCareActivity"}, {"text": "EPs", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Intravascular ultrasound ( n = 34 ) or optical coherence tomography ( n = 31 ) was performed in all cases .

Example answer:
{"entities": [{"text": "Intravascular ultrasound", "type": "HealthCareActivity"}, {"text": "optical coherence tomography", "type": "HealthCareActivity"}]}

Example input:
Sentence: The standard whole - body ultrasonography examination includes thoracic , cardiac , limited abdominal , and an evaluation for DVT .

Example answer:
{"entities": [{"text": "whole - body", "type": "AnatomicalStructure"}, {"text": "ultrasonography", "type": "HealthCareActivity"}, {"text": "examination", "type": "HealthCareActivity"}, {"text": "thoracic", "type": "SpatialConcept"}, {"text": "cardiac", "type": "AnatomicalStructure"}, {"text": "abdominal", "type": "SpatialConcept"}, {"text": "evaluation", "type": "HealthCareActivity"}, {"text": "DVT", "type": "BiologicFunction"}]}

Example input:
Sentence: Point - of - care ultrasonography is often compartmentalized such that the clinician will focus on one body system while performing the critical care ultrasonography examination .

Example answer:
{"entities": [{"text": "ultrasonography", "type": "HealthCareActivity"}, {"text": "compartmentalized", "type": "Finding"}, {"text": "clinician", "type": "ProfessionalOrOccupationalGroup"}, {"text": "body system", "type": "BodySystem"}, {"text": "critical care", "type": "HealthCareActivity"}, {"text": "examination", "type": "HealthCareActivity"}]}

Example input:
Sentence: A Whole - Body Approach to Point of Care Ultrasound Ultrasonography is an essential imaging modality in the ICU used to diagnose and guide the treatment of cardiopulmonary failure .

Example answer:
{"entities": [{"text": "Whole - Body", "type": "AnatomicalStructure"}, {"text": "Ultrasound", "type": "HealthCareActivity"}, {"text": "Ultrasonography", "type": "HealthCareActivity"}, {"text": "ICU", "type": "Organization"}, {"text": "diagnose", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "cardiopulmonary failure", "type": "BiologicFunction"}]}

Example input:
Sentence: As a remarkable clue and as early as 1986 , ultrasonography ( US ) has been proven a reliable diagnostic method that is also explicitly helpful in difficult cases with atypical presentation and enables to rule out many differential diagnoses .Recent publications emphasized the role of multidetector computed tomography ( CT ) resulting in a significant reduction of false negative findings at operation .

Example answer:
{"entities": [{"text": "ultrasonography", "type": "HealthCareActivity"}, {"text": "US", "type": "HealthCareActivity"}, {"text": "diagnostic method", "type": "HealthCareActivity"}, {"text": "differential diagnoses", "type": "HealthCareActivity"}, {"text": "publications", "type": "IntellectualProduct"}, {"text": "multidetector computed tomography", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "false negative findings", "type": "Finding"}, {"text": "operation", "type": "HealthCareActivity"}]}

Input:
Sentence: Ultrasonography ( US ) is a highly portable , noninvasive , low cost , and fast imaging method , especially when compared to magnetic resonance imaging ( MRI ) , computed tomography ( CT ) , and radiography .

## Item MedMentions:test:4445
Example input:
Sentence: Linear regression analyses assessed the cross - sectional associations between abdominal fat and SA , and logistic regression assessed the odds of diabetes , given low SA .

Example answer:
{"entities": [{"text": "abdominal fat", "type": "AnatomicalStructure"}, {"text": "SA", "type": "Finding"}, {"text": "logistic regression", "type": "ResearchActivity"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Based on the collected data , we did not identify associations with HbA1c ( 0·03 % , -0·01 to 0·08 ) , fasting insulin ( 0·00 % , -0·06 to 0·07 ) , and BMI ( 0·11 kg / m ( 2 ) , -0·09 to 0·30 ) .

Example answer:
{"entities": [{"text": "HbA1c", "type": "Chemical"}, {"text": "fasting", "type": "Finding"}, {"text": "insulin", "type": "Chemical"}, {"text": "BMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The magnitude of this correlation was higher for important nocturia , lower MSaO2 , or higher BMI .

Example answer:
{"entities": [{"text": "nocturia", "type": "BiologicFunction"}, {"text": "MSaO2", "type": "HealthCareActivity"}, {"text": "BMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The pattern of metabolic deviations associated with lower birthweight resembled the metabolic signature of higher adult BMI ( R ( 2 ) = 0 . 77 ) assessed at the same time as the metabolic profiling .

Example answer:
{"entities": [{"text": "deviations", "type": "SpatialConcept"}, {"text": "lower birthweight", "type": "Finding"}, {"text": "metabolic signature", "type": "BiologicFunction"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "metabolic profiling", "type": "BiologicFunction"}]}

Example input:
Sentence: Mean BMI was 50 . 7 kg / m2 [ Class III obese ( BMI ≥40 kg / m2 ) , 92 % ( n = 835 ; CI = 91 - 94 ) ] .

Example answer:
{"entities": [{"text": "BMI", "type": "ClinicalAttribute"}, {"text": "obese", "type": "BiologicFunction"}]}

Example input:
Sentence: 6 ± 9 . 6 kg / m ( 2 ) , P = .02 ) , but there was no difference between groups in percent body fat , metabolic profile , adipocyte size , resting energy expenditure , hyperphagia score , or ghrelin levels .

Example answer:
{"entities": [{"text": "percent body fat", "type": "Finding"}, {"text": "metabolic profile", "type": "BiologicFunction"}, {"text": "adipocyte", "type": "AnatomicalStructure"}, {"text": "resting energy expenditure", "type": "Finding"}, {"text": "hyperphagia", "type": "Finding"}, {"text": "ghrelin levels", "type": "HealthCareActivity"}]}

Example input:
Sentence: Notably , neither waist circumference nor BMI were significant predictors of incident diabetes independent of age , sex and triglycerides .

Example answer:
{"entities": [{"text": "waist circumference", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "triglycerides", "type": "Chemical"}]}

Example input:
Sentence: The resemblance indicated that 1 kg lower birthweight is associated with similar metabolic aberrations as caused by 0 . 92 units higher BMI in adulthood .

Example answer:
{"entities": [{"text": "lower birthweight", "type": "Finding"}, {"text": "BMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Participants who developed incident type 2 diabetes were significantly older and had significantly higher body mass index ( BMI ; p = 0 . 012 ) , total cholesterol ( p = 0 . 007 ) , fasting triglycerides ( p < 0 . 001 ) , and Homeostatic Model Assessment of Insulin Resistance ( HOMA - IR ) ( p < 0 .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "type 2 diabetes", "type": "Finding"}, {"text": "significantly older", "type": "PopulationGroup"}, {"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "fasting", "type": "Finding"}, {"text": "triglycerides", "type": "Chemical"}, {"text": "Homeostatic Model Assessment of Insulin Resistance", "type": "HealthCareActivity"}, {"text": "HOMA - IR", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , in our study , surgery did not achieve the expected outcome in patients with specific metabolic , anthropometric and surgical characteristics ( BMI > 50 Kg / m2 , presence of metabolic syndrome , presence of T2DM with high preoperative HbA1c % level and gastric pouch volume greater than 60 ml ) .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "expected", "type": "IntellectualProduct"}, {"text": "surgical", "type": "HealthCareActivity"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "metabolic syndrome", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "gastric pouch", "type": "AnatomicalStructure"}]}

Input:
Sentence: Statistical analysis showed a correlation between BMI > 50 Kg / m2 , presence of metabolic syndrome , presence of diabetes , gastric pouch volume greater than 60 ml and failure of weight loss outcome .

## Item MedMentions:test:4669
Example input:
Sentence: Lagged models tested directions of effect by examining whether parent - youth differences in familism values predicted parent - youth conflict or vice versa .

Example answer:
{"entities": [{"text": "Lagged models", "type": "IntellectualProduct"}, {"text": "directions", "type": "SpatialConcept"}, {"text": "examining", "type": "Finding"}]}

Example input:
Sentence: Parental warmth at Time 1 was significantly correlated with child agency at Time 2 , which was significantly correlated with child externalizing and internalizing behaviors and academic achievement at Time 3 .

Example answer:
{"entities": [{"text": "child agency", "type": "Organization"}]}

Example input:
Sentence: Compared with teens experiencing 0 to 1 event , teens experiencing 4 + events were less likely to have married parents ( P = .01 ) and a parent with a college degree ( P = .006 ) .

Example answer:
{"entities": [{"text": "teens", "type": "PopulationGroup"}, {"text": "college degree", "type": "IntellectualProduct"}]}

Example input:
Sentence: Teen s with 4 + events had significantly poorer adherence ( P = .002 teen , P = .02 parent ) , lower self - efficacy ( P = .03 teen , P < .0001 parent ) , poorer quality of life ( P < .0001 teen , P < .0001 parent ) , and more conflict ( P = .006 teen , P = .02 parent ) than teens with fewer events .

Example answer:
{"entities": [{"text": "Teen", "type": "PopulationGroup"}, {"text": "teen", "type": "PopulationGroup"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "conflict", "type": "Finding"}, {"text": "teens", "type": "PopulationGroup"}]}

Example input:
Sentence: Major findings indicated that negative peer norms , exposure to community violence , and poor mental health were negatively correlated with school bonding , while parental monitoring , positive self - regard , and future orientation were correlated with higher school motivation .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "negative peer norms", "type": "Finding"}, {"text": "mental health", "type": "BiologicFunction"}, {"text": "negatively", "type": "Finding"}, {"text": "school", "type": "Organization"}, {"text": "bonding", "type": "BiologicFunction"}, {"text": "orientation", "type": "BiologicFunction"}, {"text": "motivation", "type": "BiologicFunction"}]}

Example input:
Sentence: Recent research shows positive associations between positive parent - child and teacher - student interactions and working memory performance and development .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "positive", "type": "Finding"}, {"text": "working memory", "type": "BiologicFunction"}, {"text": "performance", "type": "BiologicFunction"}]}

Example input:
Sentence: The findings revealed that parent - youth conflict predicted greater differences in parent - youth familism values , but differences in familism values did not predict conflict .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}]}

Example input:
Sentence: The FLASHE Study : Survey Development , Dyadic Perspectives , and Participant Characteristics The National Cancer Institute developed the Family Life , Activity , Sun , Health , and Eating ( FLASHE ) Study to examine multiple cancer preventive behaviors within parent - adolescent dyads .

Example answer:
{"entities": [{"text": "FLASHE Study", "type": "IntellectualProduct"}, {"text": "Survey", "type": "IntellectualProduct"}, {"text": "Participant", "type": "PopulationGroup"}, {"text": "National Cancer Institute", "type": "Organization"}, {"text": "Eating", "type": "BiologicFunction"}, {"text": "FLASHE", "type": "IntellectualProduct"}, {"text": "Study", "type": "IntellectualProduct"}, {"text": "cancer preventive", "type": "HealthCareActivity"}]}

Example input:
Sentence: The nationwide sample consisted of 1 , 573 parent - adolescent dyads ( 1 , 699 parents and 1 , 581 adolescents ) who returned all FLASHE surveys .

Example answer:
{"entities": [{"text": "FLASHE surveys", "type": "IntellectualProduct"}]}

Example input:
Sentence: FLASHE assessed parent and adolescent reports of several intrapersonal and interpersonal domains ( including psychosocial variables , parenting , and the community and home environments ) .

Example answer:
{"entities": [{"text": "FLASHE", "type": "IntellectualProduct"}, {"text": "home environments", "type": "SpatialConcept"}]}

Input:
Sentence: On a subset of example FLASHE items across these domains , responses of parents and adolescents within the same dyads were positively and significantly correlated ( r = 0 .

## Item MedMentions:test:4149
Example input:
Sentence: Subjective improvement was reported by 18 ( 90 % ) of the 20 included patients .

Example answer:
{"entities": []}

Example input:
Sentence: A 3 - month intervention of high - intensity aerobic training reduces risk factors for type 2 .diabetes and cardiovascular disease to a similar extent in late premenopausal and early postmenopausal women .

Example answer:
{"entities": [{"text": "intervention", "type": "HealthCareActivity"}, {"text": "risk factors", "type": "Finding"}, {"text": "type 2 .diabetes", "type": "BiologicFunction"}, {"text": "cardiovascular disease", "type": "BiologicFunction"}, {"text": "premenopausal", "type": "Finding"}, {"text": "postmenopausal", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Also , growth performance and food intake were notably improved in P .

Example answer:
{"entities": [{"text": "growth performance", "type": "BiologicFunction"}, {"text": "food intake", "type": "BiologicFunction"}, {"text": "P .", "type": "Eukaryote"}]}

Example input:
Sentence: Quantitative data were analysed to determine changes in motivation between intervention and comparison facilities pre - and post - intervention using STATA ™ version 13 .

Example answer:
{"entities": [{"text": "analysed", "type": "ResearchActivity"}, {"text": "motivation", "type": "BiologicFunction"}, {"text": "STATA ™ version 13", "type": "IntellectualProduct"}]}

Example input:
Sentence: Improve d self - efficacy was associated with a decrease in concerns about medications ( r = - 0 . 64 ) .

Example answer:
{"entities": [{"text": "Improve", "type": "Finding"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "medications", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , no appreciable improvement was observed with regard to smoking status , obesity or HbA1c control .

Example answer:
{"entities": [{"text": "smoking status", "type": "ClinicalAttribute"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "HbA1c", "type": "Chemical"}]}

Example input:
Sentence: After 4 weeks , self - efficacy , health and well - being scores significantly improved : 63 % of lifestyle goals and 89 % of health management goals were fully achieved ; 58 % of referrals to community lifestyle behaviour change services and 79 % of referrals to other services ( e . g .

Example answer:
{"entities": [{"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "significantly improved", "type": "Finding"}, {"text": "goals", "type": "IntellectualProduct"}, {"text": "achieved", "type": "Finding"}, {"text": "referrals to", "type": "HealthCareActivity"}, {"text": "community", "type": "Organization"}, {"text": "services", "type": "HealthCareActivity"}]}

Example input:
Sentence: A 3 - month high - intensity aerobic training intervention , involving healthy , nonobese , late premenopausal ( n = 40 ) and early postmenopausal ( n = 39 ) women was conducted and anthropometrics , body composition , blood pressure , lipid profile , glucose tolerance , and maximal oxygen consumption were determined at baseline and after the intervention .

Example answer:
{"entities": [{"text": "intervention", "type": "HealthCareActivity"}, {"text": "nonobese", "type": "Finding"}, {"text": "premenopausal", "type": "Finding"}, {"text": "postmenopausal", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "anthropometrics", "type": "ClinicalAttribute"}, {"text": "blood pressure", "type": "BiologicFunction"}, {"text": "maximal oxygen consumption", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The evidence statements ( stage 1 ) highlighted the effectiveness of physical activity , dietary and social role interventions in retirement ; the idiosyncratic nature of retirement and well - being ; the value of using specific behavior change techniques including those derived from the Health Action Process Approach ; and the need for signposting to local resources .

Example answer:
{"entities": [{"text": "dietary", "type": "Food"}, {"text": "interventions", "type": "HealthCareActivity"}, {"text": "retirement", "type": "Finding"}, {"text": "idiosyncratic nature", "type": "Finding"}, {"text": "local", "type": "SpatialConcept"}]}

Example input:
Sentence: The training intervention reduced body weight ( P < .01 ) , waist circumference ( P < .01 ) , and improved body composition by increasing lean body mass ( P < .001 ) and decreasing fat mass ( P < .001 ) similarly in both groups .

Example answer:
{"entities": [{"text": "intervention", "type": "HealthCareActivity"}, {"text": "waist circumference", "type": "ClinicalAttribute"}, {"text": "improved", "type": "Finding"}, {"text": "lean body mass", "type": "ClinicalAttribute"}, {"text": "decreasing", "type": "Finding"}, {"text": "groups", "type": "PopulationGroup"}]}

Input:
Sentence: Anecdotal evidence of health improvement was supported by the quantitative analyses , which revealed statistically significant improvements in body mass index , blood pressure , dietary habits , exercise levels , alcohol intake , self - rated health and self - efficacy amongst those who completed the intervention .

## Item MedMentions:test:4715
Example input:
Sentence: A Comparison Between Measured Concentration of 3H in Kalpakkam Environment with Predicted Atmospheric Dispersion Model The field measurements of 3H in the form of HTO present in air moisture carried out around Madras Atomic Power Station were compared with predicted values using atmospheric dispersion modeling .

Example answer:
{"entities": [{"text": "3H", "type": "Chemical"}, {"text": "field", "type": "SpatialConcept"}, {"text": "HTO", "type": "Chemical"}]}

Example input:
Sentence: That of NO₂ was 17 . 0 μg / m³ ( range : 4 . 7 - 31 . 3 ) , NOx was 82 .

Example answer:
{"entities": [{"text": "NO₂", "type": "Chemical"}, {"text": "NOx", "type": "Chemical"}]}

Example input:
Sentence: 1 μg / m³ ( range 4 . 1 - 42 . 3 ) , and that of O₃ was 75 . 0 μg / m³ ( range : 51 . 3 - 106 . 3 ) .

Example answer:
{"entities": [{"text": "O₃", "type": "Chemical"}]}

Example input:
Sentence: However , GDIs had , on average , a factor of 2 higher particulate matter ( PM ) mass emissions than PFIs due to higher elemental carbon ( EC ) emissions .

Example answer:
{"entities": [{"text": "emissions", "type": "Chemical"}, {"text": "elemental carbon", "type": "Chemical"}, {"text": "EC", "type": "Chemical"}]}

Example input:
Sentence: Concentrations of particulate matter ( PM ) - associated ClPAHs and BrPAHs were higher in heating period than in non - heating period , while for gas - associated ClPAHs and BrPAHs , this distinction was not significant .

Example answer:
{"entities": [{"text": "ClPAHs", "type": "Chemical"}, {"text": "BrPAHs", "type": "Chemical"}]}

Example input:
Sentence: PCB concentrations in the air ( pg / m ( 3 ) ) ranged from ~1 - 10 ( TEM ) , ~1 - 40 ( STG ) and 4 - 30 ( CON ) .

Example answer:
{"entities": [{"text": "PCB", "type": "Chemical"}, {"text": "TEM", "type": "SpatialConcept"}, {"text": "STG", "type": "SpatialConcept"}, {"text": "CON", "type": "SpatialConcept"}]}

Example input:
Sentence: w . ) , whereas the concentrations of PBDEs were similar for Danish and Finnish women ( sum of 7 i - PBDE = 4 . 9 and 5 . 2 ng / g l .

Example answer:
{"entities": [{"text": "PBDEs", "type": "Chemical"}, {"text": "Danish", "type": "PopulationGroup"}, {"text": "Finnish", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "i - PBDE", "type": "Chemical"}]}

Example input:
Sentence: For example , a 10 μg / m³ increase of 7 - day ( lag 06 ) average concentrations of PM10 ( particulate matter no greater than 10 microns ) , SO₂ , NO₂ was associated with 0 .

Example answer:
{"entities": []}

Example input:
Sentence: In high temperature days , a 10μg / m ( 3 ) increment in PM10 concentration corresponded to pooled estimates of 0 . 78 % ( 95 % CI : 0 . 44 % , 1 .

Example answer:
{"entities": []}

Example input:
Sentence: PBDE concentrations in air ( pg / m ( 3 ) ) ranged from 1 to 55 ( STG ) , 0 . 5 to 20 ( CON ) and from 0 .

Example answer:
{"entities": [{"text": "PBDE", "type": "Chemical"}, {"text": "STG", "type": "SpatialConcept"}, {"text": "CON", "type": "SpatialConcept"}]}

Input:
Sentence: The sum of gaseous and particle concentrations ( ∑OPE ) ranged from 35 to 343 pg / m3 .

## Item MedMentions:test:4647
Example input:
Sentence: There was no mortality .

Example answer:
{"entities": [{"text": "no mortality", "type": "Finding"}]}

Example input:
Sentence: On average , executive functioning and processing speed improved significantly , while memory test scores decreased significantly , over time .

Example answer:
{"entities": [{"text": "executive functioning", "type": "BiologicFunction"}]}

Example input:
Sentence: Seligman and Maier ( 1967 ) theorized that animals learned that outcomes were independent of their responses -that nothing they did mattered - and that this learning undermined trying to escape .

Example answer:
{"entities": [{"text": "Seligman and Maier", "type": "Eukaryote"}, {"text": "animals", "type": "Eukaryote"}, {"text": "learned", "type": "BiologicFunction"}, {"text": "learning", "type": "BiologicFunction"}, {"text": "escape", "type": "BiologicFunction"}]}

Example input:
Sentence: Crude logistic regression showed that women ( odds ratio [ OR ] 1 . 9 , 95 % confidence interval [ CI ] 1 . 3 - 2 . 6 ) , low educational level ( OR 2 . 0 , 95 % CI 1 . 4 - 3 . 0 ) and low mastery ( OR 1 . 4 , 95 % CI 1 . 0 - 1 . 9 ) were associated with cognitive decline , but no daily consumption of vegetables and fruits had only a marginal association ( OR 1 .

Example answer:
{"entities": [{"text": "logistic regression", "type": "ResearchActivity"}, {"text": "low mastery", "type": "Finding"}, {"text": "cognitive decline", "type": "BiologicFunction"}, {"text": "no", "type": "Finding"}, {"text": "vegetables", "type": "Food"}, {"text": "fruits", "type": "Food"}]}

Example input:
Sentence: Indeed , Frederick Griffith discovered natural competence for transformation in 1928 while he was investigating the exchange of pathogenic traits in pneumococci .

Example answer:
{"entities": [{"text": "transformation", "type": "BiologicFunction"}, {"text": "exchange", "type": "BiologicFunction"}, {"text": "pathogenic", "type": "Finding"}, {"text": "pneumococci", "type": "Bacterium"}]}

Example input:
Sentence: The complexity of the human brain , including normal functioning and potential for dysfunctions , has developed over evolutionary time and has been shaped by natural selection .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "dysfunctions", "type": "BiologicFunction"}]}

Example input:
Sentence: 9 % , respectively ( all P < 0 . 05 ) ; the changes in mental HRQoL ( +17 % ) and fatigue ( -20 % ) failed to be statistically significant

Example answer:
{"entities": [{"text": "mental", "type": "BiologicFunction"}, {"text": "fatigue", "type": "Finding"}]}

Example input:
Sentence: Neuropsychological testing did not suggest true regression in cognitive , language , and academic skills , although decreases in motivation and performance were noted with a reaction to stress and multiple environmental changes as a potential causative factor .

Example answer:
{"entities": [{"text": "Neuropsychological testing", "type": "HealthCareActivity"}, {"text": "regression", "type": "BiologicFunction"}, {"text": "academic skills", "type": "BiologicFunction"}, {"text": "motivation", "type": "BiologicFunction"}, {"text": "stress", "type": "Finding"}, {"text": "environmental", "type": "SpatialConcept"}]}

Example input:
Sentence: Enhanced levels of daily functioning , positive affect , spiritual resilience , and tranquility were also reported .

Example answer:
{"entities": [{"text": "positive affect", "type": "BiologicFunction"}, {"text": "tranquility", "type": "BiologicFunction"}]}

Example input:
Sentence: No significant improvements are observed in the reduction of muscle tone or daily living activities .

Example answer:
{"entities": [{"text": "muscle tone", "type": "BiologicFunction"}]}

Input:
Sentence: There were no significant changes in cognition or ability to perform activities of daily living .

## Item MedMentions:test:4164
Example input:
Sentence: Subsequently , immunoprecipitation , Western blot and tube formation assay results showed that the phosphorylation of both IQGAP1 and N - WASP was required for the angiogenesis induced by C .

Example answer:
{"entities": [{"text": "immunoprecipitation", "type": "HealthCareActivity"}, {"text": "Western blot", "type": "HealthCareActivity"}, {"text": "tube formation assay", "type": "HealthCareActivity"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "IQGAP1", "type": "Chemical"}, {"text": "N - WASP", "type": "Chemical"}, {"text": "angiogenesis", "type": "BiologicFunction"}, {"text": "C .", "type": "Bacterium"}]}

Example input:
Sentence: Our co - immunoprecipitation study revealed that IQGAP1 physically associated with N - WASP after C .

Example answer:
{"entities": [{"text": "co - immunoprecipitation", "type": "HealthCareActivity"}, {"text": "study", "type": "HealthCareActivity"}, {"text": "IQGAP1", "type": "Chemical"}, {"text": "N - WASP", "type": "Chemical"}, {"text": "C .", "type": "Bacterium"}]}

Example input:
Sentence: Firstly , we verify experimentally that dissociation of Raf kinase inhibitor protein ( RKIP ) from Mitogen - activated protein kinase kinase ( MEK ) is required for cerebellar LTD and add this interaction to an earlier published model , along with the known requirement of dissociation of RKIP from Raf kinase .

Example answer:
{"entities": [{"text": "Raf kinase inhibitor protein", "type": "Chemical"}, {"text": "RKIP", "type": "Chemical"}, {"text": "Mitogen - activated protein kinase kinase", "type": "Chemical"}, {"text": "MEK", "type": "Chemical"}, {"text": "cerebellar", "type": "AnatomicalStructure"}, {"text": "LTD", "type": "BiologicFunction"}, {"text": "Raf kinase", "type": "Chemical"}]}

Example input:
Sentence: pneumoniae - infected VECs , both IQGAP1 and N - WASP were recruited to filamentous actin , and shared some common compartments localized at the leading edge of lamellipodia , which was impaired after the depletion of IQGAP1 by using the small interference RNA .

Example answer:
{"entities": [{"text": "pneumoniae", "type": "Bacterium"}, {"text": "infected", "type": "Finding"}, {"text": "VECs", "type": "AnatomicalStructure"}, {"text": "IQGAP1", "type": "Chemical"}, {"text": "N - WASP", "type": "Chemical"}, {"text": "filamentous actin", "type": "Chemical"}, {"text": "localized", "type": "SpatialConcept"}, {"text": "leading edge", "type": "AnatomicalStructure"}, {"text": "lamellipodia", "type": "AnatomicalStructure"}, {"text": "small interference RNA", "type": "Chemical"}]}

Example input:
Sentence: pneumoniae infection on angiogenesis , and then explored the roles of IQGAP1 -related signaling in C .

Example answer:
{"entities": [{"text": "pneumoniae", "type": "Bacterium"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "angiogenesis", "type": "BiologicFunction"}, {"text": "IQGAP1", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "C .", "type": "Bacterium"}]}

Example input:
Sentence: Moreover , the knockdown of IQGAP1 also significantly decreased N - WASP phosphorylation at Tyr256 induced by C .

Example answer:
{"entities": [{"text": "knockdown", "type": "ResearchActivity"}, {"text": "IQGAP1", "type": "AnatomicalStructure"}, {"text": "N - WASP", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "Tyr256", "type": "Chemical"}, {"text": "C .", "type": "Bacterium"}]}

Example input:
Sentence: Furthermore , we show that the WW domain is not required for ERK - IQGAP1 binding , and contributes little or no binding energy to this interaction , challenging previous models of how WW - based peptides might inhibit tumorigenesis .

Example answer:
{"entities": [{"text": "WW domain", "type": "SpatialConcept"}, {"text": "ERK", "type": "Chemical"}, {"text": "IQGAP1", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "no", "type": "Finding"}, {"text": "interaction", "type": "BiologicFunction"}, {"text": "models", "type": "IntellectualProduct"}, {"text": "WW - based peptides", "type": "Chemical"}, {"text": "tumorigenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Finally , we show that the ERK2 - IQGAP1 interaction does not require ERK2 phosphorylation or catalytic activity and does not involve known docking recruitment sites on ERK2 , and we obtain an estimate of the dissociation constant ( Kd ) for this interaction of 8 μm These results prompt a re - evaluation of published findings and a refined model of IQGAP scaffolding .

Example answer:
{"entities": [{"text": "ERK2", "type": "Chemical"}, {"text": "IQGAP1", "type": "Chemical"}, {"text": "interaction", "type": "BiologicFunction"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "docking", "type": "BiologicFunction"}, {"text": "sites", "type": "SpatialConcept"}, {"text": "findings", "type": "Finding"}, {"text": "refined model", "type": "IntellectualProduct"}, {"text": "IQGAP scaffolding", "type": "Chemical"}]}

Example input:
Sentence: Results from previous studies have suggested that the WW domain of IQGAP1 binds to the cancer -associated MAPKs ERK1 and ERK2 , and that this domain might thus offer a new tool to selectively inhibit MAPK activation in cancer cells .

Example answer:
{"entities": [{"text": "WW domain", "type": "SpatialConcept"}, {"text": "IQGAP1", "type": "Chemical"}, {"text": "binds", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "MAPKs", "type": "Chemical"}, {"text": "ERK1", "type": "Chemical"}, {"text": "ERK2", "type": "Chemical"}, {"text": "domain", "type": "SpatialConcept"}, {"text": "MAPK", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "cancer cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The WW domain of the scaffolding protein IQGAP1 is neither necessary nor sufficient for binding to the MAPKs ERK1 and ERK2 Mitogen - activated protein kinase ( MAPK ) scaffold proteins , such as IQ motif containing GTPase activating protein 1 ( IQGAP1 ) , are promising targets for novel therapies against cancer and other diseases .

Example answer:
{"entities": [{"text": "WW domain", "type": "SpatialConcept"}, {"text": "scaffolding protein", "type": "Chemical"}, {"text": "IQGAP1", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "MAPKs", "type": "Chemical"}, {"text": "ERK1", "type": "Chemical"}, {"text": "ERK2", "type": "Chemical"}, {"text": "Mitogen - activated protein kinase", "type": "Chemical"}, {"text": "MAPK", "type": "Chemical"}, {"text": "scaffold proteins", "type": "Chemical"}, {"text": "IQ motif containing GTPase activating protein 1", "type": "Chemical"}, {"text": "therapies", "type": "HealthCareActivity"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "diseases", "type": "BiologicFunction"}]}

Input:
Sentence: Here , using quantitative in vitro binding assays , we show that the IQ domain of IQGAP1 is both necessary and sufficient for binding to ERK1 and ERK2 , as well as to the MAPK kinases MEK1 and MEK2 .

## Item MedMentions:test:4429
Example input:
Sentence: SSM yielded significantly lower radiation doses as compared to HSM ( 2 . 1 ± 2 .

Example answer:
{"entities": [{"text": "SSM", "type": "HealthCareActivity"}, {"text": "HSM", "type": "HealthCareActivity"}]}

Example input:
Sentence: The predicted average SUA level in adults from the high DBMI group was 5 . 32 mg / dl after adjustment for related factors in a combined sex analysis .

Example answer:
{"entities": [{"text": "SUA level", "type": "HealthCareActivity"}, {"text": "DBMI", "type": "ClinicalAttribute"}, {"text": "sex analysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: SBP was higher in eET - 1 and unaffected by smPparγ inactivation .

Example answer:
{"entities": [{"text": "SBP", "type": "ClinicalAttribute"}, {"text": "eET - 1", "type": "Chemical"}, {"text": "smPparγ", "type": "Chemical"}, {"text": "inactivation", "type": "BiologicFunction"}]}

Example input:
Sentence: Diagnostic image quality significantly decreased in SSM in patients with AS ≥2 , 000 ( p = 0 . 03 ) .

Example answer:
{"entities": [{"text": "SSM", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , SBM from India contained more ( < 0 . 05 ) trypsin inhibitors than SBM from the other countries .

Example answer:
{"entities": [{"text": "SBM", "type": "Food"}, {"text": "India", "type": "SpatialConcept"}, {"text": "trypsin inhibitors", "type": "Chemical"}, {"text": "countries", "type": "SpatialConcept"}]}

Example input:
Sentence: However , because of the lower concentration of AA in SBM from China , the concentration of standardized ileal digestible AA in SBM from China was less ( < 0 . 05 ) than in SBM from the U .

Example answer:
{"entities": [{"text": "AA", "type": "Chemical"}, {"text": "SBM", "type": "Food"}, {"text": "China", "type": "SpatialConcept"}, {"text": "U .", "type": "SpatialConcept"}]}

Example input:
Sentence: S . , or India and the apparent ileal digestibility ( AID ) and the standardized ileal digestibility ( SID ) of CP and AA in these SBM when fed to growing pigs .

Example answer:
{"entities": [{"text": "S", "type": "SpatialConcept"}, {"text": "India", "type": "SpatialConcept"}, {"text": "CP", "type": "Chemical"}, {"text": "AA", "type": "Chemical"}, {"text": "SBM", "type": "Food"}, {"text": "pigs", "type": "Eukaryote"}]}

Example input:
Sentence: S . or Brazil had less ( < 0 . 05 ) variability in SID values than SBM from Argentina , China , or India .

Example answer:
{"entities": [{"text": "S", "type": "SpatialConcept"}, {"text": "Brazil", "type": "SpatialConcept"}, {"text": "SBM", "type": "Food"}, {"text": "Argentina", "type": "SpatialConcept"}, {"text": "China", "type": "SpatialConcept"}, {"text": "India", "type": "SpatialConcept"}]}

Example input:
Sentence: Results indicate that the concentration of CP was greater ( < 0 . 05 ) in SBM from Brazil and India ( 49 . 3 and 49 .

Example answer:
{"entities": [{"text": "CP", "type": "Chemical"}, {"text": "SBM", "type": "Food"}, {"text": "Brazil", "type": "SpatialConcept"}, {"text": "India", "type": "SpatialConcept"}]}

Example input:
Sentence: The concentration of most indispensable AA followed the same pattern as CP with the exception that SBM from the U . S . contained more ( < 0 . 05 ) indispensable AA than SBM from China or Argentina .

Example answer:
{"entities": [{"text": "AA", "type": "Chemical"}, {"text": "CP", "type": "Chemical"}, {"text": "SBM", "type": "Food"}, {"text": "U . S", "type": "SpatialConcept"}, {"text": "China", "type": "SpatialConcept"}, {"text": "Argentina", "type": "SpatialConcept"}]}

Input:
Sentence: A greater ( < 0 . 05 ) AID and SID of CP and most AA was observed in SBM from the U .

## Item MedMentions:test:4616
Example input:
Sentence: Phylogenomic analyses of 869 mega base pairs divided into 18 , 621 genome fragments yielded a well - resolved coalescent species tree despite signals for extensive gene flow across species .

Example answer:
{"entities": [{"text": "Phylogenomic analyses", "type": "ResearchActivity"}, {"text": "mega base pairs", "type": "BiologicFunction"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "fragments", "type": "BodySubstance"}, {"text": "species tree", "type": "IntellectualProduct"}, {"text": "gene flow", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: The phylogeographic patterns observed in the studied collection demonstrate that large - scale ( but not middle / small - scale ) distance remains one of the decisive factors of the genetic divergence of M .

Example answer:
{"entities": [{"text": "studied", "type": "HealthCareActivity"}, {"text": "collection", "type": "HealthCareActivity"}, {"text": "genetic divergence", "type": "BiologicFunction"}, {"text": "M .", "type": "Bacterium"}]}

Example input:
Sentence: The size polymorphism in the mt genomes of these closely related Chrysoporthe species was attributed to the varying number and length of introns , coding sequences and to a lesser extent , intergenic sequences .

Example answer:
{"entities": [{"text": "size", "type": "SpatialConcept"}, {"text": "polymorphism", "type": "BiologicFunction"}, {"text": "mt genomes", "type": "AnatomicalStructure"}, {"text": "Chrysoporthe species", "type": "Eukaryote"}, {"text": "introns", "type": "Chemical"}, {"text": "coding sequences", "type": "AnatomicalStructure"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "intergenic sequences", "type": "Chemical"}]}

Example input:
Sentence: DNA variation in one mitochondrial marker and nine nuclear microsatellite loci revealed a strong phylogeographic pattern across 28 populations of G .

Example answer:
{"entities": [{"text": "DNA", "type": "Chemical"}, {"text": "mitochondrial", "type": "AnatomicalStructure"}, {"text": "marker", "type": "SpatialConcept"}, {"text": "nuclear", "type": "AnatomicalStructure"}, {"text": "microsatellite loci", "type": "AnatomicalStructure"}, {"text": "phylogeographic pattern", "type": "Finding"}, {"text": "G .", "type": "Eukaryote"}]}

Example input:
Sentence: Notable nucleotide differences exist between genomes in the right half , including the presence of mycobacteriophage mobile element 1 ( MPME1 ) in Jane .

Example answer:
{"entities": [{"text": "nucleotide", "type": "Chemical"}, {"text": "genomes", "type": "AnatomicalStructure"}, {"text": "mycobacteriophage", "type": "Virus"}, {"text": "mobile element 1", "type": "Chemical"}]}

Example input:
Sentence: Comparative analyses revealed signatures of duplication events , intron number and length variation , and varying intronic ORFs which highlighted the genetic diversity of mt genomes among the Cryphonectriaceae .

Example answer:
{"entities": [{"text": "duplication", "type": "BiologicFunction"}, {"text": "intron", "type": "Chemical"}, {"text": "intronic", "type": "Chemical"}, {"text": "ORFs", "type": "AnatomicalStructure"}, {"text": "mt genomes", "type": "AnatomicalStructure"}, {"text": "Cryphonectriaceae", "type": "Eukaryote"}]}

Example input:
Sentence: Genetic sequence variations at 101 loci were associated with the levels of 246 ( 38 % ) metabolites ( P ≤ 1 . 9 × 10 ( - 11 ) ) .

Example answer:
{"entities": [{"text": "Genetic sequence", "type": "Chemical"}, {"text": "loci", "type": "AnatomicalStructure"}, {"text": "metabolites", "type": "Chemical"}]}

Example input:
Sentence: DNA sequence diversity and the efficiency of natural selection in animal mitochondrial DNA Selection is expected to be more efficient in species that are more diverse because both the efficiency of natural selection and DNA sequence diversity are expected to depend upon the effective population size .

Example answer:
{"entities": [{"text": "DNA sequence", "type": "SpatialConcept"}, {"text": "animal", "type": "Eukaryote"}, {"text": "mitochondrial DNA", "type": "Chemical"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: This is corroborated in mice ( mtDNA deletions 1 , 163 vs 379 pg / mL , p < 0 . 0001 ) .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}, {"text": "mtDNA deletions", "type": "Finding"}]}

Example input:
Sentence: Intron Derived Size Polymorphism in the Mitochondrial Genomes of Closely Related Chrysoporthe Species In this study , the complete mitochondrial ( mt ) genomes of Chrysoporthe austroafricana ( 190 , 834 bp ) , C .

Example answer:
{"entities": [{"text": "Intron", "type": "Chemical"}, {"text": "Size", "type": "SpatialConcept"}, {"text": "Polymorphism", "type": "BiologicFunction"}, {"text": "Mitochondrial Genomes", "type": "AnatomicalStructure"}, {"text": "Chrysoporthe Species", "type": "Eukaryote"}, {"text": "mitochondrial ( mt ) genomes", "type": "AnatomicalStructure"}, {"text": "Chrysoporthe austroafricana", "type": "Eukaryote"}, {"text": "C .", "type": "Eukaryote"}]}

Input:
Sentence: 0181 % nucleotide sequence divergence across the entire mitogenome , implying little intraspecific mtDNA genetic variation .

## Item MedMentions:test:4372
Example input:
Sentence: Using the X - ray crystal structure as a starting point , we have modeled the motions of a DNA duplex built from a self - complementary oligonucleotide ( 5΄ - CTTATPPPZZZATAAG - 3΄ ) in water over a period of 50 μs and calculated DNA local parameters , step parameters , helix parameters , and major / minor groove widths to examine how the presence of multiple , consecutive nucleobase pairs might impact helical structure .

Example answer:
{"entities": [{"text": "X - ray crystal structure", "type": "HealthCareActivity"}, {"text": "DNA", "type": "Chemical"}, {"text": "duplex", "type": "SpatialConcept"}, {"text": "self - complementary oligonucleotide", "type": "Chemical"}, {"text": "5΄ - CTTATPPPZZZATAAG - 3΄", "type": "Chemical"}, {"text": "water", "type": "Chemical"}, {"text": "calculated", "type": "HealthCareActivity"}, {"text": "local", "type": "SpatialConcept"}, {"text": "major", "type": "Chemical"}, {"text": "minor groove", "type": "Chemical"}, {"text": "presence", "type": "Finding"}, {"text": "helical structure", "type": "SpatialConcept"}]}

Example input:
Sentence: The introduction of C - rich sequences may promote the folding of amplification products into a G - quadruplex structure , which is specifically recognized by the commercially available fluorescent probe thioflavin T .

Example answer:
{"entities": [{"text": "C - rich sequences", "type": "SpatialConcept"}, {"text": "folding", "type": "BiologicFunction"}, {"text": "amplification products", "type": "SpatialConcept"}, {"text": "G - quadruplex", "type": "SpatialConcept"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "fluorescent probe", "type": "Chemical"}, {"text": "thioflavin T", "type": "Chemical"}]}

Example input:
Sentence: Here we present the Split - Broccoli system , in which self - assembly is nucleated by a thermostable , three - way junction RNA architecture and fluorescence activation requires both strands .

Example answer:
{"entities": [{"text": "Split - Broccoli system", "type": "Chemical"}, {"text": "RNA", "type": "Chemical"}, {"text": "strands", "type": "Chemical"}]}

Example input:
Sentence: Here , using fluorescence microscopy and chromosome conformation capture in conjunction with deep sequencing ( Hi - C ) , we show that in Caulobacter crescentus , both transcription rate and transcript length , independent of concurrent translation , drive the formation of domain boundaries .

Example answer:
{"entities": [{"text": "fluorescence microscopy", "type": "HealthCareActivity"}, {"text": "deep sequencing", "type": "ResearchActivity"}, {"text": "Caulobacter crescentus", "type": "Bacterium"}, {"text": "transcription", "type": "BiologicFunction"}, {"text": "transcript", "type": "Chemical"}, {"text": "translation", "type": "BiologicFunction"}, {"text": "domain boundaries", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A novel class of pH ( low ) insertion peptides ( pHLIPs ) with pH -dependent transmembrane activity can fold and rapidly insert into the lipid bilayer of tumor cells triggered by acidity , facilitating the cellular internalization of nanomaterials synchronously .

Example answer:
{"entities": [{"text": "pH ( low ) insertion peptides", "type": "Chemical"}, {"text": "pHLIPs", "type": "Chemical"}, {"text": "transmembrane activity", "type": "BiologicFunction"}, {"text": "fold", "type": "SpatialConcept"}, {"text": "lipid bilayer", "type": "AnatomicalStructure"}, {"text": "tumor cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Here , we constructed a distinctive multilayered functional architecture : plasmid DNA ( pDNA ) was electrostatically complexed with cationic poly ( lysine ) ( polyplex ) as the interior pDNA reservoir , which was further cross - linked by redox - responsive disulfide cross - linking to minimize the occurrence of polyplex disassembly through exchange reaction with the biological charged components .

Example answer:
{"entities": [{"text": "plasmid DNA", "type": "Chemical"}, {"text": "pDNA", "type": "Chemical"}, {"text": "cationic", "type": "Chemical"}, {"text": "poly ( lysine )", "type": "Chemical"}, {"text": "polyplex", "type": "Chemical"}, {"text": "interior", "type": "SpatialConcept"}, {"text": "redox", "type": "BiologicFunction"}, {"text": "disulfide", "type": "Chemical"}, {"text": "exchange reaction", "type": "BiologicFunction"}, {"text": "charged components", "type": "Chemical"}]}

Example input:
Sentence: We demonstrate that this motif rapidly assembles into monolayer pits that coalesce during progressive membrane exfoliation , leading to bacterial cell death within minutes .

Example answer:
{"entities": [{"text": "motif", "type": "SpatialConcept"}, {"text": "pits", "type": "AnatomicalStructure"}, {"text": "membrane", "type": "AnatomicalStructure"}, {"text": "bacterial cell", "type": "Bacterium"}, {"text": "death", "type": "Finding"}]}

Example input:
Sentence: Co - Folding of a FliF - FliG Split Domain Forms the Basis of the MS : C Ring Interface within the Bacterial Flagellar Motor The interface between the membrane ( MS ) and cytoplasmic ( C ) rings of the bacterial flagellar motor couples torque generation to rotation within the membrane .

Example answer:
{"entities": [{"text": "Co - Folding", "type": "BiologicFunction"}, {"text": "FliF", "type": "Chemical"}, {"text": "FliG", "type": "Chemical"}, {"text": "Split Domain", "type": "SpatialConcept"}, {"text": "MS : C Ring Interface", "type": "AnatomicalStructure"}, {"text": "Bacterial Flagellar Motor", "type": "BiologicFunction"}, {"text": "membrane", "type": "AnatomicalStructure"}, {"text": "MS", "type": "AnatomicalStructure"}, {"text": "cytoplasmic", "type": "AnatomicalStructure"}, {"text": "C", "type": "AnatomicalStructure"}, {"text": "rings of the bacterial flagellar motor", "type": "BiologicFunction"}]}

Example input:
Sentence: The membranes were characterized with attenuated total reflectance - Fourier transform infrared spectroscopy , scanning electron microscopy coupled with energy - dispersive X - ray spectroscopy ( SEM - EDS ) and ultraviolet - visible spectroscopy and correlative light and electron microscopy ( CLEM ) .

Example answer:
{"entities": [{"text": "reflectance - Fourier transform infrared spectroscopy", "type": "ResearchActivity"}, {"text": "scanning electron microscopy", "type": "HealthCareActivity"}, {"text": "energy - dispersive X - ray spectroscopy", "type": "HealthCareActivity"}, {"text": "SEM - EDS", "type": "HealthCareActivity"}, {"text": "correlative light and electron microscopy", "type": "HealthCareActivity"}, {"text": "CLEM", "type": "HealthCareActivity"}]}

Example input:
Sentence: Live imaging of the genetically intractable obligate intracellular bacteria Orientia tsutsugamushi using a panel of fluorescent dyes Our understanding of the molecular mechanisms of bacterial infection and pathogenesis are disproportionally derived from a small number of well - characterised species and strains .

Example answer:
{"entities": [{"text": "Live imaging", "type": "HealthCareActivity"}, {"text": "genetically", "type": "ResearchActivity"}, {"text": "obligate intracellular bacteria", "type": "Bacterium"}, {"text": "Orientia tsutsugamushi", "type": "Bacterium"}, {"text": "fluorescent dyes", "type": "Chemical"}, {"text": "bacterial infection", "type": "BiologicFunction"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}]}

Input:
Sentence: Using a combination of molecular - scale and real - time imaging , spectroscopy and spectrometry approaches , we introduce a structural motif with a universal insertion mode in reconstituted membranes and live bacteria .

## Item MedMentions:test:4209
Example input:
Sentence: Polystyrene discs coated with chitosan reduced both early biofilm formation ( 6 h ) and late biofilm formation ( 18 h ) , as confirmed by scanning electron microscopy .

Example answer:
{"entities": [{"text": "Polystyrene discs", "type": "Chemical"}, {"text": "chitosan", "type": "Chemical"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "scanning electron microscopy", "type": "HealthCareActivity"}]}

Example input:
Sentence: The activity of the fragment in inhibiting biofilm formation , could be due to the conformations highlighted by the MD simulations , suggesting its interaction with the bacterial membrane .

Example answer:
{"entities": [{"text": "fragment", "type": "Chemical"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "conformations", "type": "SpatialConcept"}]}

Example input:
Sentence: We recently showed that human cathelicidin LL - 37 exhibits inhibitory effects on biofilm formation of S .

Example answer:
{"entities": [{"text": "human cathelicidin LL - 37", "type": "Chemical"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: 5 to 6 . 2 mg / ml and inhibited biofilm formation at sub - inhibitory concentrations ( 3 . 1 - 0 . 75 mg / ml ) .

Example answer:
{"entities": [{"text": "biofilm formation", "type": "BiologicFunction"}]}

Example input:
Sentence: All the derivatives reduced the proportion of viable cells in mature biofilms .

Example answer:
{"entities": [{"text": "derivatives", "type": "Chemical"}, {"text": "biofilms", "type": "Bacterium"}]}

Example input:
Sentence: Based on the findings that compound 5 , targeting the histidine kinase domain of S . epidermidis YycG , possessed bactericidal activity against staphylococci , 39 derivatives of compound 5 with intact thiazolopyrimidinone core structures were newly designed , 7 derivatives were further screened to explore their anti - bacterial and anti - biofilm activities .

Example answer:
{"entities": [{"text": "compound 5", "type": "Chemical"}, {"text": "histidine kinase domain", "type": "Chemical"}, {"text": "S . epidermidis YycG", "type": "Chemical"}, {"text": "bactericidal activity", "type": "BiologicFunction"}, {"text": "staphylococci", "type": "Bacterium"}, {"text": "derivatives of compound 5 with intact thiazolopyrimidinone core structures", "type": "Chemical"}, {"text": "7 derivatives", "type": "Chemical"}, {"text": "screened", "type": "HealthCareActivity"}, {"text": "anti - bacterial and anti - biofilm activities", "type": "BiologicFunction"}]}

Example input:
Sentence: The seven derivatives strongly inhibited the growth of S .

Example answer:
{"entities": [{"text": "seven derivatives", "type": "Chemical"}, {"text": "inhibited the growth", "type": "BiologicFunction"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: mutans within 5 h , inhibited biofilm formation within 24 h , and reduced bacteria cells in preformed biofilms within 3 h at a concentration of 0 . 2 mg / mL .

Example answer:
{"entities": [{"text": "mutans", "type": "Bacterium"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "bacteria cells", "type": "Bacterium"}, {"text": "biofilms", "type": "Bacterium"}]}

Example input:
Sentence: These results were suggestive that the seven derivatives of compound 5 have the potential to be developed into agents for eradicating biofilm -associated infections .

Example answer:
{"entities": [{"text": "seven derivatives of compound 5", "type": "Chemical"}, {"text": "biofilm", "type": "Bacterium"}, {"text": "infections", "type": "BiologicFunction"}]}

Example input:
Sentence: Biofilm formation was significantly promoted ( p < 0 . 05 ) by 5 and 10 µM C6 - HSL , inhibited ( p < 0 . 05 ) by C4 - HSL ( 5 and 10 µM ) and 5 µM 3 - oxo - C8 - HSL , suggesting that QS may have a regulatory role in the biofilm formation of H .

Example answer:
{"entities": [{"text": "Biofilm formation", "type": "BiologicFunction"}, {"text": "C6 - HSL", "type": "Chemical"}, {"text": "C4 - HSL", "type": "Chemical"}, {"text": "3 - oxo - C8 - HSL", "type": "Chemical"}, {"text": "QS", "type": "BiologicFunction"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "H .", "type": "Bacterium"}]}

Input:
Sentence: The biofilm inhibition activities of four derivatives ( H5 - 32 , H5 - 33 , H5 - 34 , and H5 - 35 ) were further investigated under shearing forces , they all led to significant decreases in the biofilm formation of S .

## Item MedMentions:test:4529
Example input:
Sentence: We suggest that modulation of TRPV1 channels by noradrenaline in nociceptive neurons is a mechanism whereby noradrenaline may suppress incoming noxious stimuli at the primary synaptic afferents in the dorsal horn of the spinal cord .

Example answer:
{"entities": [{"text": "TRPV1 channels", "type": "Chemical"}, {"text": "noradrenaline", "type": "Chemical"}, {"text": "nociceptive neurons", "type": "AnatomicalStructure"}, {"text": "synaptic", "type": "SpatialConcept"}, {"text": "afferents", "type": "AnatomicalStructure"}, {"text": "dorsal horn of the spinal cord", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Inflammatory pain -related traits of sensory DRG neurons innervating the hip joints Hip pain is transmitted to the dorsal horn of the spinal cord via the dorsal root ganglion ( DRG ) , which contains two types of neurons with differential sensitivity to neurotrophic factors .

Example answer:
{"entities": [{"text": "Inflammatory pain", "type": "Finding"}, {"text": "DRG", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "hip joints", "type": "SpatialConcept"}, {"text": "Hip pain", "type": "Finding"}, {"text": "dorsal horn of the spinal cord", "type": "AnatomicalStructure"}, {"text": "dorsal root ganglion", "type": "AnatomicalStructure"}, {"text": "neurotrophic factors", "type": "Chemical"}]}

Example input:
Sentence: Spinal blocking EphB1 receptor activation in the late phase after STZ injection significantly suppressed the established mechanical allodynia as well as activation of the astrocytes and microglial cells and activity of TNF - α and IL - 1β .

Example answer:
{"entities": [{"text": "Spinal", "type": "SpatialConcept"}, {"text": "EphB1 receptor", "type": "Chemical"}, {"text": "STZ", "type": "Chemical"}, {"text": "injection", "type": "HealthCareActivity"}, {"text": "mechanical allodynia", "type": "Finding"}, {"text": "astrocytes", "type": "AnatomicalStructure"}, {"text": "microglial cells", "type": "AnatomicalStructure"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "IL - 1β", "type": "Chemical"}]}

Example input:
Sentence: Activation of ephrinB - EphB receptor signalling in rat spinal cord contributes to maintenance of diabetic neuropathic pain Diabetic neuropathic pain ( DNP ) is severe and intractable in clinic .

Example answer:
{"entities": [{"text": "rat spinal cord", "type": "AnatomicalStructure"}, {"text": "diabetic", "type": "Finding"}, {"text": "neuropathic pain", "type": "Finding"}, {"text": "Diabetic", "type": "Finding"}, {"text": "DNP", "type": "Finding"}, {"text": "clinic", "type": "Organization"}]}

Example input:
Sentence: EphB1 receptor activation in the spinal cord is critical to the maintenance , but not induction of diabetic pain .

Example answer:
{"entities": [{"text": "EphB1 receptor", "type": "Chemical"}, {"text": "spinal cord", "type": "AnatomicalStructure"}, {"text": "diabetic", "type": "Finding"}, {"text": "pain", "type": "Finding"}]}

Example input:
Sentence: To explore the mechanisms involved , the expression of glial glutamate transporter 1 ( GLT - 1 ) and the activation of mitogen - activated protein kinases in the spinal dorsal horn were analyzed .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "glial", "type": "AnatomicalStructure"}, {"text": "glutamate transporter 1", "type": "Chemical"}, {"text": "GLT - 1", "type": "Chemical"}, {"text": "mitogen - activated protein kinases", "type": "Chemical"}, {"text": "spinal dorsal horn", "type": "AnatomicalStructure"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: We suggest that modulation of presynaptic TRPV1 channels in nociceptive neurons by descending noradrenergic inputs may constitute a mechanism for noradrenaline to modulate incoming noxious stimuli in the dorsal horn of the spinal cord .

Example answer:
{"entities": [{"text": "presynaptic", "type": "AnatomicalStructure"}, {"text": "TRPV1 channels", "type": "Chemical"}, {"text": "nociceptive neurons", "type": "AnatomicalStructure"}, {"text": "noradrenaline", "type": "Chemical"}, {"text": "dorsal horn of the spinal cord", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Activation of EphB1 receptor in the spinal cord is critical to maintaining the established diabetic neuropathic pain , but not to diabetic pain induction .

Example answer:
{"entities": [{"text": "EphB1 receptor", "type": "Chemical"}, {"text": "spinal cord", "type": "AnatomicalStructure"}, {"text": "diabetic", "type": "Finding"}, {"text": "neuropathic pain", "type": "Finding"}, {"text": "pain", "type": "Finding"}]}

Example input:
Sentence: Spinal blocking EphB1 receptor activation suppresses ongoing diabetic neuropathic pain .

Example answer:
{"entities": [{"text": "Spinal", "type": "SpatialConcept"}, {"text": "EphB1 receptor", "type": "Chemical"}, {"text": "diabetic", "type": "Finding"}, {"text": "neuropathic pain", "type": "Finding"}]}

Example input:
Sentence: Phosphorylated ERK and total ERK protein in the lumbar spinal dorsal horn was detected by using the Western blot technique .

Example answer:
{"entities": [{"text": "Phosphorylated ERK", "type": "Chemical"}, {"text": "ERK", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}, {"text": "lumbar", "type": "SpatialConcept"}, {"text": "spinal dorsal horn", "type": "AnatomicalStructure"}, {"text": "detected", "type": "Finding"}, {"text": "Western blot technique", "type": "HealthCareActivity"}]}

Input:
Sentence: Our results suggest that ERK activation in the spinal dorsal horn plays a vital role in NP - evoked hyperalgesia .

## Item MedMentions:test:4520
Example input:
Sentence: We analyzed 67 patients with suspected MCpEF who underwent endomyocardial biopsy ( EMB ) .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "suspected MCpEF", "type": "BiologicFunction"}, {"text": "endomyocardial biopsy", "type": "HealthCareActivity"}, {"text": "EMB", "type": "HealthCareActivity"}]}

Example input:
Sentence: The Early Treatment Diabetic Retinopathy Study criteria were used to confirm the presence of CSME by the following 2 methods : stereoscopic fundus photography ( method 1 ) and dilated biomicroscopy in combination with optical coherence tomography ( method 2 ) .

Example answer:
{"entities": [{"text": "Diabetic Retinopathy", "type": "BiologicFunction"}, {"text": "Study", "type": "ResearchActivity"}, {"text": "presence", "type": "Finding"}, {"text": "CSME", "type": "BiologicFunction"}, {"text": "methods", "type": "HealthCareActivity"}, {"text": "stereoscopic fundus photography", "type": "HealthCareActivity"}, {"text": "method 1", "type": "HealthCareActivity"}, {"text": "biomicroscopy", "type": "HealthCareActivity"}, {"text": "optical coherence tomography", "type": "HealthCareActivity"}, {"text": "method 2", "type": "HealthCareActivity"}]}

Example input:
Sentence: Under the strict observation of endophthalmitis prophylaxis , SBCS is an option to reduce the cataract blindness backlog in rural areas of developing countries .

Example answer:
{"entities": [{"text": "endophthalmitis", "type": "BiologicFunction"}, {"text": "prophylaxis", "type": "HealthCareActivity"}, {"text": "SBCS", "type": "HealthCareActivity"}, {"text": "cataract", "type": "AnatomicalStructure"}, {"text": "blindness", "type": "Finding"}]}

Example input:
Sentence: A modified ESBL Nordmann / Dortet / Poirel - based protocol to optimize early sepsis management We evaluated a modification of a colorimetric test recently described by Dortet et al . ( 2015 ) for the rapid detection of ESBL -producing Enterobacteriaceae directly from positive blood cultures that requires less manipulation , materials and hands - on time .

Example answer:
{"entities": [{"text": "ESBL Nordmann / Dortet / Poirel - based protocol", "type": "HealthCareActivity"}, {"text": "sepsis", "type": "BiologicFunction"}, {"text": "management", "type": "HealthCareActivity"}, {"text": "colorimetric test", "type": "HealthCareActivity"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "ESBL", "type": "Chemical"}, {"text": "Enterobacteriaceae", "type": "Bacterium"}, {"text": "positive", "type": "Finding"}, {"text": "blood cultures", "type": "HealthCareActivity"}, {"text": "manipulation", "type": "HealthCareActivity"}]}

Example input:
Sentence: MALDI - TOF MS identification allowed identification of three genera belonging to LAB including Lactobacillus , Enterococcus and Leuconostoc .

Example answer:
{"entities": [{"text": "MALDI - TOF MS", "type": "ResearchActivity"}, {"text": "genera", "type": "IntellectualProduct"}, {"text": "LAB", "type": "Bacterium"}, {"text": "Lactobacillus", "type": "Bacterium"}, {"text": "Enterococcus", "type": "Bacterium"}, {"text": "Leuconostoc", "type": "Bacterium"}]}

Example input:
Sentence: Seven out of eight cases of endophthalmitis were confirmed by positive culture .

Example answer:
{"entities": [{"text": "endophthalmitis", "type": "BiologicFunction"}, {"text": "positive culture", "type": "Finding"}]}

Example input:
Sentence: Telemedicine screening programs and epidemiological studies rely on monoscopic fundus photography for the detection of clinically significant macular edema ( CSME ) .

Example answer:
{"entities": [{"text": "Telemedicine", "type": "HealthCareActivity"}, {"text": "screening programs", "type": "HealthCareActivity"}, {"text": "epidemiological studies", "type": "ResearchActivity"}, {"text": "monoscopic fundus photography", "type": "HealthCareActivity"}, {"text": "clinically significant macular edema", "type": "BiologicFunction"}, {"text": "CSME", "type": "BiologicFunction"}]}

Example input:
Sentence: With the development and adoption of matrix - assisted laser desorption ionization - time of flight mass spectrometry ( MALDI - TOF MS ) , suspicious isolates are now routinely identified to the species level .

Example answer:
{"entities": [{"text": "matrix - assisted laser desorption ionization - time of flight mass spectrometry", "type": "HealthCareActivity"}, {"text": "MALDI - TOF MS", "type": "HealthCareActivity"}, {"text": "isolates", "type": "Chemical"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: With the use of a newer diagnostic tool , matrix - assisted laser desorption ionization - time of flight ( MALDI - TOF ) MS , we were able to rapidly identify the organism and initiate appropriate treatment .

Example answer:
{"entities": [{"text": "matrix - assisted laser desorption ionization - time of flight ( MALDI - TOF ) MS", "type": "ResearchActivity"}]}

Example input:
Sentence: Bactec ™ blood culture bottles allied to MALDI - TOF mass spectrometry : rapid etiologic diagnosis of bacterial endophthalmitis Matrix - assisted laser desorption ionization - time of flight ( MALDI - TOF ) mass spectrometry ( MS ) has been used for direct identification of pathogens from blood - inoculated blood culture bottles ( BCBs ) .

Example answer:
{"entities": [{"text": "MALDI - TOF mass spectrometry", "type": "ResearchActivity"}, {"text": "diagnosis", "type": "ResearchActivity"}, {"text": "bacterial endophthalmitis", "type": "BiologicFunction"}, {"text": "Matrix - assisted laser desorption ionization - time of flight ( MALDI - TOF ) mass spectrometry ( MS )", "type": "ResearchActivity"}]}

Input:
Sentence: We showed that MALDI - TOF MS is an useful technique for rapid identification of the causative agents of endophthalmitis from vitreous humor - inoculated BCBs with a simple protocol .

## Item MedMentions:test:4762
Example input:
Sentence: 3 to 52 . 5 μg / m ( 3 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 2 % , respectively , with 0 , 1 , 2 . 5 , and 5 μM ; P < 0 . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 26 . 0 mm / mm ( 2 ) ; P ≤ 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: pastoris was compared in continuous cultures growing at the same µ at either 22 or 30 ° C .

Example answer:
{"entities": [{"text": "pastoris", "type": "Eukaryote"}, {"text": "cultures", "type": "HealthCareActivity"}]}

Example input:
Sentence: 6 μm at baseline to 270 . 8 ± 27 .

Example answer:
{"entities": []}

Example input:
Sentence: 03 ± 0 . 35 μM ( GSK369796 ) .

Example answer:
{"entities": [{"text": "GSK369796", "type": "Chemical"}]}

Example input:
Sentence: 6 μm ( 2 ) and 27 . 5 - 48 . 9 μm , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 37 μM ( MQ ) , and 5 . 06 ± 0 . 86 μM ( GSK369796 ) .

Example answer:
{"entities": [{"text": "MQ", "type": "Chemical"}, {"text": "GSK369796", "type": "Chemical"}]}

Example input:
Sentence: 95 ± 0 . 21 μM ( MQ ) , and 2 . 57 ± 0 .

Example answer:
{"entities": [{"text": "MQ", "type": "Chemical"}]}

Example input:
Sentence: 31 μM ( QC ) , 3 . 22 ± 0 .

Example answer:
{"entities": [{"text": "QC", "type": "Chemical"}]}

Input:
Sentence: 1 μA cm ( - 2 ) with Michaelis - Menten constant ( Km ) of 0 .

## Item MedMentions:test:4633
Example input:
Sentence: yakuba as an outgroup , we found clear evidence for selection on 4 - fold sites along both lineages over a substantial period , with the intensity of selection increasing with GC content .

Example answer:
{"entities": [{"text": "yakuba", "type": "Eukaryote"}, {"text": "selection", "type": "BiologicFunction"}, {"text": "sites", "type": "AnatomicalStructure"}]}

Example input:
Sentence: This study is the first to show adverse effects of imidacloprid on queen bee fecundity and behavior and improves our understanding of how neonicotinoids may impair short - term colony functioning .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "adverse effects", "type": "BiologicFunction"}, {"text": "imidacloprid", "type": "Chemical"}, {"text": "queen bee", "type": "Eukaryote"}, {"text": "fecundity", "type": "BiologicFunction"}, {"text": "understanding", "type": "BiologicFunction"}, {"text": "neonicotinoids", "type": "Chemical"}, {"text": "colony", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The Fungal Kingdom stands alone in the range , extent , and complexity of their manipulation of arthropod behavior .

Example answer:
{"entities": [{"text": "Fungal Kingdom", "type": "Eukaryote"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "arthropod", "type": "Eukaryote"}]}

Example input:
Sentence: Aggregated over trials , participants spent more money for punishing the defection of likable - looking and smiling partners compared to punishing the defection of unlikable - looking and nonsmiling partners , but only because participants were more likely to cooperate with likable - looking and smiling partners , which provided the participants with more opportunities for moralistic punishment .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "likable", "type": "BiologicFunction"}, {"text": "partners", "type": "PopulationGroup"}, {"text": "unlikable", "type": "BiologicFunction"}, {"text": "opportunities", "type": "Finding"}]}

Example input:
Sentence: Therefore , the increased activity during less favorable weather conditions and the fast recruitment of nestmates following the discovery of a food source , as observed for P . orizabaensis , may be adaptations that evolved to coexist even with more aggressive and dominant species of stingless bees , with which P .

Example answer:
{"entities": [{"text": "nestmates", "type": "PopulationGroup"}, {"text": "food", "type": "Food"}, {"text": "source", "type": "Finding"}, {"text": "P . orizabaensis", "type": "Eukaryote"}, {"text": "adaptations", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "stingless bees", "type": "Eukaryote"}, {"text": "P .", "type": "Eukaryote"}]}

Example input:
Sentence: We showed that the outcome of aggression experiments between the non - aggressive species P . orizabaensis and its aggressive competitor Trigona fuscipennis is influenced by the number of bees that arrive early after food source discovery .

Example answer:
{"entities": [{"text": "experiments", "type": "ResearchActivity"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "P . orizabaensis", "type": "Eukaryote"}, {"text": "competitor", "type": "PopulationGroup"}, {"text": "Trigona fuscipennis", "type": "Eukaryote"}, {"text": "bees", "type": "Eukaryote"}, {"text": "food", "type": "Food"}, {"text": "source", "type": "Finding"}]}

Example input:
Sentence: Here , we test whether the removal of queens in colonies of the acorn ant Temnothorax curvispinosus alters their ability to execute important collective behaviors and survive outbreaks of a generalist entomopathogen .

Example answer:
{"entities": [{"text": "queens", "type": "ProfessionalOrOccupationalGroup"}, {"text": "colonies", "type": "AnatomicalStructure"}, {"text": "acorn ant", "type": "Eukaryote"}, {"text": "Temnothorax curvispinosus", "type": "Eukaryote"}]}

Example input:
Sentence: We then tested these subcolonies ' performance in a series of collective behavior assays and finally exposed colonies to the entomopathogenic fungus Metarhizium robertsii by exposing two individuals from the colony and then sealing them back into the nest .

Example answer:
{"entities": [{"text": "subcolonies '", "type": "AnatomicalStructure"}, {"text": "colonies", "type": "AnatomicalStructure"}, {"text": "Metarhizium robertsii", "type": "Eukaryote"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "colony", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Queen presence mediates the relationship between collective behavior and disease susceptibility in ant colonies The success of social living can be explained , in part , by a group 's ability to execute collective behaviors unachievable by solitary individuals .

Example answer:
{"entities": [{"text": "Queen", "type": "ProfessionalOrOccupationalGroup"}, {"text": "presence", "type": "Finding"}, {"text": "disease susceptibility", "type": "ClinicalAttribute"}, {"text": "ant", "type": "Eukaryote"}, {"text": "colonies", "type": "AnatomicalStructure"}, {"text": "group 's", "type": "PopulationGroup"}, {"text": "individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: However , queenless groups that displayed more interactions with brood experienced greater survivorship , a trend not present in queenright subcolonies .

Example answer:
{"entities": [{"text": "queenless groups", "type": "PopulationGroup"}, {"text": "brood", "type": "PopulationGroup"}, {"text": "queenright subcolonies", "type": "AnatomicalStructure"}]}

Input:
Sentence: We found that queenright subcolonies outperformed their queenless counterparts in nearly all collective behaviors .

## Item MedMentions:test:4643
Example input:
Sentence: Healthcare professionals must be aware of parents ' needs during this vulnerable interstage period and to provide psychosocial and nursing support .

Example answer:
{"entities": [{"text": "Healthcare professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "nursing support", "type": "HealthCareActivity"}]}

Example input:
Sentence: Relatives and care professionals emphasized the role the organization of facilitation of care played , as well as making residents feel like they still matter .

Example answer:
{"entities": [{"text": "care professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "organization", "type": "Organization"}]}

Example input:
Sentence: The data collected in our study indicate that a restrictive specimen acceptance policy , computer - generated positive identification systems , and interdisciplinary cooperation can significantly reduce patient identification errors .

Example answer:
{"entities": [{"text": "data collected", "type": "Finding"}, {"text": "study", "type": "ResearchActivity"}, {"text": "computer - generated", "type": "HealthCareActivity"}, {"text": "positive identification systems", "type": "IntellectualProduct"}, {"text": "patient identification", "type": "HealthCareActivity"}]}

Example input:
Sentence: A critical feature in working with this client group is to recognize their ambiguity and the fragility and temporality of their decisions about their destiny .

Example answer:
{"entities": [{"text": "fragility", "type": "Finding"}, {"text": "temporality", "type": "BiologicFunction"}, {"text": "decisions", "type": "BiologicFunction"}]}

Example input:
Sentence: Screening of these factors in tertiary care and long - term follow - up settings may improve identification of those at greatest need for support services .

Example answer:
{"entities": [{"text": "Screening", "type": "HealthCareActivity"}, {"text": "tertiary care", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "improve", "type": "Finding"}]}

Example input:
Sentence: PBIs were associated with slightly improved maternal health worker motivation .

Example answer:
{"entities": [{"text": "maternal", "type": "Finding"}, {"text": "health worker", "type": "ProfessionalOrOccupationalGroup"}, {"text": "motivation", "type": "BiologicFunction"}]}

Example input:
Sentence: Beneficial Effects of Two Types of Personal Health Record Services Connected With Electronic Medical Records Within the Hospital Setting Healthcare consumers must be able to make decisions based on accurate health information .

Example answer:
{"entities": [{"text": "Personal Health Record", "type": "IntellectualProduct"}, {"text": "Services", "type": "HealthCareActivity"}, {"text": "Electronic Medical Records", "type": "IntellectualProduct"}, {"text": "Hospital Setting", "type": "Organization"}, {"text": "Healthcare consumers", "type": "PopulationGroup"}, {"text": "decisions", "type": "BiologicFunction"}]}

Example input:
Sentence: They valued the opportunity to participate in point of service safety partnerships , such as identity and medication double checks , that might afford an immediate risk reduction .

Example answer:
{"entities": []}

Example input:
Sentence: A pilot project involving fingerprint -based criminal history background checks for personal care workers in Michigan has supplied an opportunity to examine one such mechanism .

Example answer:
{"entities": [{"text": "pilot project", "type": "ResearchActivity"}, {"text": "criminal", "type": "PopulationGroup"}, {"text": "background checks", "type": "Finding"}, {"text": "personal care workers", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Fingerprint -based background checks for personal care workers : Stakeholder views of policy criteria Decision makers face difficult choices when tasked with identifying and implementing appropriate mechanisms for protecting the elderly and other vulnerable adults from abuse .

Example answer:
{"entities": [{"text": "background checks", "type": "Finding"}, {"text": "personal care workers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Stakeholder", "type": "PopulationGroup"}, {"text": "policy", "type": "IntellectualProduct"}, {"text": "Decision makers", "type": "PopulationGroup"}, {"text": "protecting", "type": "Finding"}, {"text": "elderly", "type": "PopulationGroup"}, {"text": "vulnerable adults", "type": "Finding"}]}

Input:
Sentence: While stakeholders generally see fingerprint -based background checks for personal care workers as potentially effective and as a net benefit , they also point to a variety of contingencies .

## Item MedMentions:test:4716
Example input:
Sentence: Cyanogen chloride ( CNCl ) was detected when the Cl2 / Asp molar ratio was lower than 5 . N - DBPs formation was influenced by pH .

Example answer:
{"entities": [{"text": "Cyanogen chloride", "type": "Chemical"}, {"text": "CNCl", "type": "Chemical"}, {"text": "Cl2", "type": "Chemical"}, {"text": "Asp", "type": "Chemical"}, {"text": "N - DBPs", "type": "Chemical"}]}

Example input:
Sentence: Pentachlorophenol ( PCP ) was detected at highest concentrations ( 1 . 8 ng / g ) in fish from Prince Edward Bay , the Bay of Quinte Lake reference site , and Hillman Marsh ( the Wheatley Harbour reference site ) , suggesting local sources of contamination .

Example answer:
{"entities": [{"text": "Pentachlorophenol", "type": "Chemical"}, {"text": "PCP", "type": "Chemical"}, {"text": "fish", "type": "Eukaryote"}, {"text": "Prince Edward Bay", "type": "SpatialConcept"}, {"text": "Bay of Quinte Lake reference site", "type": "SpatialConcept"}]}

Example input:
Sentence: DDTs were detected with a prevalence of p , p ' - DDE accounting for ~50 % of the total DDTs .

Example answer:
{"entities": [{"text": "DDTs", "type": "Chemical"}, {"text": "detected", "type": "Finding"}, {"text": "p , p ' - DDE", "type": "Chemical"}]}

Example input:
Sentence: Eighteen ( 15 % ) toxigenic isolates harbored binary toxins ( cdtA and cdtB ) and all had tcdC deletion , including Δ39 ( C184 T ) deletion ( 14 isolates ) , Δ18 in - frame deletion ( 3 isolates ) , and Δ18 ( Δ117A ) deletion ( 1 isolate ) .

Example answer:
{"entities": [{"text": "toxigenic", "type": "Chemical"}, {"text": "isolates", "type": "Chemical"}, {"text": "binary toxins", "type": "Chemical"}, {"text": "deletion", "type": "BiologicFunction"}, {"text": "Δ39 ( C184 T ) deletion", "type": "BiologicFunction"}, {"text": "Δ18 in - frame deletion", "type": "BiologicFunction"}, {"text": "Δ18 ( Δ117A ) deletion", "type": "BiologicFunction"}, {"text": "isolate", "type": "Chemical"}]}

Example input:
Sentence: ( 5 ) The 95th percentile carcinogenic risk ( CR ) of PCDD / Fs in ambient air from s urrounding sites , background site , upwind site and downwind site were 8 .

Example answer:
{"entities": [{"text": "PCDD", "type": "Chemical"}, {"text": "Fs", "type": "Chemical"}, {"text": "urrounding sites", "type": "SpatialConcept"}, {"text": "background site", "type": "SpatialConcept"}, {"text": "upwind site", "type": "SpatialConcept"}, {"text": "downwind site", "type": "SpatialConcept"}]}

Example input:
Sentence: 007 % w / w and 0 . 123 % w / w , respectively , while chloroform was not detected .

Example answer:
{"entities": [{"text": "chloroform", "type": "Chemical"}, {"text": "not detected", "type": "Finding"}]}

Example input:
Sentence: Organophosphate Esters in Air , Snow and Seawater in the North Atlantic and the Arctic The concentrations of eight organophosphate esters ( OPEs ) have been investigated in air , snow and seawater samples collected during the cruise of ARK - XXVIII / 2 from 6th June to 3rd July 2014 across the North Atlantic and the Arctic .

Example answer:
{"entities": [{"text": "Organophosphate Esters", "type": "Chemical"}, {"text": "North Atlantic", "type": "SpatialConcept"}, {"text": "Arctic", "type": "SpatialConcept"}, {"text": "organophosphate esters", "type": "Chemical"}, {"text": "OPEs", "type": "Chemical"}]}

Example input:
Sentence: Polychlorinated biphenyls ( PCBs ) ( 7 indicator congeners ) , chlorinated pesticides hexachlorocyclohexanes ( HCHs ) , dichlorodiphenyl trichloroethanes ( DDTs ) and flame retardants such as polybrominated diphenyl ethers ( PBDEs ) were determined by gas chromatography coupled mass spectrometry ( GC / MS ) .

Example answer:
{"entities": [{"text": "Polychlorinated biphenyls", "type": "Chemical"}, {"text": "PCBs", "type": "Chemical"}, {"text": "chlorinated pesticides", "type": "Chemical"}, {"text": "hexachlorocyclohexanes", "type": "Chemical"}, {"text": "HCHs", "type": "Chemical"}, {"text": "dichlorodiphenyl trichloroethanes", "type": "Chemical"}, {"text": "DDTs", "type": "Chemical"}, {"text": "flame retardants", "type": "Chemical"}, {"text": "polybrominated diphenyl ethers", "type": "Chemical"}, {"text": "PBDEs", "type": "Chemical"}, {"text": "gas chromatography coupled mass spectrometry", "type": "HealthCareActivity"}, {"text": "GC / MS", "type": "HealthCareActivity"}]}

Example input:
Sentence: The organochlorine ( OC ) pesticide contamination profile , determined in a subset of French samples , was dominated by p , p ' - DDE ( 56 . 6 % ) , followed by β - HCH ( 14 . 2 % ) , HCB ( 9 . 7 % ) and dieldrin ( 5 . 2 % ) , while other compounds were only minor contributors ( < 5 % ) .

Example answer:
{"entities": [{"text": "organochlorine ( OC ) pesticide", "type": "Chemical"}, {"text": "profile", "type": "HealthCareActivity"}, {"text": "subset", "type": "IntellectualProduct"}, {"text": "French", "type": "PopulationGroup"}, {"text": "p , p ' - DDE", "type": "Chemical"}, {"text": "β - HCH", "type": "Chemical"}, {"text": "HCB", "type": "Chemical"}, {"text": "dieldrin", "type": "Chemical"}]}

Example input:
Sentence: The most abundant OPE was tris - ( 2 - chloroethyl ) phosphate ( TCEP ) , with concentrations ranging from 30 to 227 pg / m3 , followed by three major OPEs , such as tris - ( 1 - chloro - 2 - propyl ) phosphate ( TCPP , 0 . 8 to 82 pg / m3 ) , tri - n - butyl phosphate ( TnBP , 2 to 19 pg / m3 ) and tri - iso - butyl phosphate ( TiBP , 0 . 3 to 14 pg / m3 ) .

Example answer:
{"entities": [{"text": "OPE", "type": "Chemical"}, {"text": "tris - ( 2 - chloroethyl ) phosphate", "type": "Chemical"}, {"text": "TCEP", "type": "Chemical"}, {"text": "OPEs", "type": "Chemical"}, {"text": "tris - ( 1 - chloro - 2 - propyl ) phosphate", "type": "Chemical"}, {"text": "TCPP", "type": "Chemical"}, {"text": "tri - n - butyl phosphate", "type": "Chemical"}, {"text": "TnBP", "type": "Chemical"}, {"text": "tri - iso - butyl phosphate", "type": "Chemical"}, {"text": "TiBP", "type": "Chemical"}]}

Input:
Sentence: The three chlorinated OPEs accounted for 88 ± 5 % of the ∑OPE .

## Item MedMentions:test:4608
Example input:
Sentence: After vaginal mesh removal , 29 patients ( 35 % ) required 1 or more reoperations , with 3 being the highest number of reoperations per patient .

Example answer:
{"entities": [{"text": "vaginal", "type": "AnatomicalStructure"}, {"text": "removal", "type": "HealthCareActivity"}, {"text": "reoperations", "type": "HealthCareActivity"}]}

Example input:
Sentence: 9 % ) , and 16 ( 22 . 5 % ) patients underwent PG , DG , segmental gastrectomy , local resection , and endoscopic submucosal dissection , respectively , in the SND group .

Example answer:
{"entities": [{"text": "PG", "type": "HealthCareActivity"}, {"text": "DG", "type": "HealthCareActivity"}, {"text": "segmental", "type": "SpatialConcept"}, {"text": "gastrectomy", "type": "HealthCareActivity"}, {"text": "local resection", "type": "HealthCareActivity"}, {"text": "endoscopic submucosal dissection", "type": "HealthCareActivity"}, {"text": "SND", "type": "HealthCareActivity"}]}

Example input:
Sentence: Gastrojejunostomy tube complications - A single center experience and systematic review Gastrojejunostomy tubes ( GJTs ) enable enteral nutrition in infants / children with feeding intolerance .

Example answer:
{"entities": [{"text": "Gastrojejunostomy tube", "type": "MedicalDevice"}, {"text": "systematic review", "type": "IntellectualProduct"}, {"text": "Gastrojejunostomy tubes", "type": "MedicalDevice"}, {"text": "GJTs", "type": "MedicalDevice"}, {"text": "enteral nutrition", "type": "HealthCareActivity"}, {"text": "feeding intolerance", "type": "Finding"}]}

Example input:
Sentence: When considering the 17 patients that failed the weaning attempt , 11 ( 64 % ) had to be reconnected to the ventilator during the SBT , three ( 18 % ) had to be re - intubated within 48 h of extubation , and three ( 18 % ) required non - invasive ventilation support within 48 h of extubation .

Example answer:
{"entities": [{"text": "weaning attempt", "type": "HealthCareActivity"}, {"text": "reconnected", "type": "HealthCareActivity"}, {"text": "ventilator", "type": "MedicalDevice"}, {"text": "SBT", "type": "HealthCareActivity"}, {"text": "re - intubated", "type": "HealthCareActivity"}, {"text": "extubation", "type": "HealthCareActivity"}, {"text": "non - invasive ventilation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Catheter traction and gastric outlet obstruction : a repeated complication of using a Foley catheter for gastrostomy tube replacement Percutaneous endoscopic gastrostomy ( PEG ) is a safe procedure and major morbidity is unusual .

Example answer:
{"entities": [{"text": "Catheter traction", "type": "MedicalDevice"}, {"text": "gastric outlet obstruction", "type": "BiologicFunction"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "Foley catheter", "type": "MedicalDevice"}, {"text": "gastrostomy tube replacement", "type": "HealthCareActivity"}, {"text": "Percutaneous endoscopic gastrostomy", "type": "HealthCareActivity"}, {"text": "PEG", "type": "HealthCareActivity"}, {"text": "procedure", "type": "HealthCareActivity"}]}

Example input:
Sentence: Obstructive Acute Pancreatitis Secondary to PEG Tube Migration Percutaneous gastrostomy is a well - established method of providing enteral nutrition to patients incapable of oral intake , or for whom oral intake is insufficient to meet metabolic needs .

Example answer:
{"entities": [{"text": "Acute Pancreatitis", "type": "BiologicFunction"}, {"text": "PEG Tube", "type": "MedicalDevice"}, {"text": "Migration", "type": "Finding"}, {"text": "Percutaneous gastrostomy", "type": "HealthCareActivity"}, {"text": "enteral nutrition", "type": "HealthCareActivity"}]}

Example input:
Sentence: To study symptom support in these cases , we performed gastrostomies on 3 patients with V180I genetic Creutzfeldt - Jakob disease ( CJD ) who had become akinetic and mute , and compared them to 14 other similar patients being fed by tube .

Example answer:
{"entities": [{"text": "symptom", "type": "Finding"}, {"text": "gastrostomies", "type": "HealthCareActivity"}, {"text": "V180I genetic Creutzfeldt - Jakob disease", "type": "BiologicFunction"}, {"text": "CJD", "type": "BiologicFunction"}, {"text": "mute", "type": "Finding"}, {"text": "fed by tube", "type": "HealthCareActivity"}]}

Example input:
Sentence: 8 % of the total time after gastrostomy being used for intravenous or transluminal administration , respectively .

Example answer:
{"entities": [{"text": "gastrostomy", "type": "HealthCareActivity"}, {"text": "intravenous", "type": "SpatialConcept"}]}

Example input:
Sentence: Thirty - eight patients ( 23 % ) required a feeding tube during treatment .

Example answer:
{"entities": [{"text": "feeding tube", "type": "MedicalDevice"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the 3 gastrostomy cases , there were no direct complications due to the gastrostomy or tube feeding , nor were there episodes of discontinuation of tube feeding or initiation of continuous drip infusion due to severe complications .

Example answer:
{"entities": [{"text": "gastrostomy", "type": "HealthCareActivity"}, {"text": "no direct complications", "type": "Finding"}, {"text": "tube feeding", "type": "HealthCareActivity"}, {"text": "discontinuation", "type": "HealthCareActivity"}, {"text": "initiation of continuous drip infusion", "type": "HealthCareActivity"}, {"text": "severe complications", "type": "Finding"}]}

Input:
Sentence: We compared the present patient series with that of our previous report statistically , and found that patients undergoing gastrostomy required significantly fewer discontinuations of tube feeding than those who did not .

## Item MedMentions:test:4614
Example input:
Sentence: To the best of our knowledge , this is the first experimental evidence for temperature -dependent herbicide sensitivity based on metabolic detoxification .

Example answer:
{"entities": [{"text": "herbicide", "type": "Chemical"}, {"text": "detoxification", "type": "HealthCareActivity"}]}

Example input:
Sentence: We show that the slope of this relationship differs between the two phylogenetic groups for which we have the most data , rodents and bats , and that it also differs between species with high and low body mass , and between those with high and low mass -specific metabolic rate .

Example answer:
{"entities": [{"text": "rodents", "type": "Eukaryote"}, {"text": "bats", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: melanogaster are much higher than the short - term ones , indicating a continuing decline in selection intensity , to such an extent that the short - term estimates suggest that selection is only active in the most GC -rich parts of the genome .

Example answer:
{"entities": [{"text": "melanogaster", "type": "Eukaryote"}, {"text": "selection", "type": "BiologicFunction"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "genome", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Obese animals presented higher GSSG levels ( P = 0 . 003 ) , GSSG / GSH ratio ( P = 0 . 013 ) , lipid peroxidation ( P = 0 . 004 ) , XO activity ( P = 0 . 015 ) and lymphocyte chemotaxis ( P < 0 .

Example answer:
{"entities": [{"text": "animals", "type": "Eukaryote"}, {"text": "GSSG", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "lipid peroxidation", "type": "BiologicFunction"}, {"text": "XO activity", "type": "BiologicFunction"}, {"text": "lymphocyte chemotaxis", "type": "BiologicFunction"}]}

Example input:
Sentence: Metabolic Interference of sod gene mutations on catalase activity in Escherichia coli exposed to Gramoxone ® ( paraquat ) herbicide Herbicides are continuously used to minimize the loss of crop productivity in agricultural environments .

Example answer:
{"entities": [{"text": "sod", "type": "Chemical"}, {"text": "gene mutations", "type": "BiologicFunction"}, {"text": "catalase activity", "type": "BiologicFunction"}, {"text": "Escherichia coli", "type": "Bacterium"}, {"text": "Gramoxone", "type": "Chemical"}, {"text": "paraquat", "type": "Chemical"}, {"text": "herbicide", "type": "Chemical"}, {"text": "Herbicides", "type": "Chemical"}, {"text": "crop", "type": "Eukaryote"}, {"text": "agricultural environments", "type": "SpatialConcept"}]}

Example input:
Sentence: GOX activities were higher in H .

Example answer:
{"entities": [{"text": "GOX", "type": "Chemical"}, {"text": "H .", "type": "Eukaryote"}]}

Example input:
Sentence: The three tested host plants upregulated GOX transcripts , and to a lesser extent , GOX activity in both species .

Example answer:
{"entities": [{"text": "upregulated", "type": "BiologicFunction"}, {"text": "GOX", "type": "AnatomicalStructure"}, {"text": "transcripts", "type": "Chemical"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: In contrast , edge specialists groups mainly included terrestrial insectivores and were positively correlated with open area and shrub cover , and percentage of shrub cover between 1 and 2 m in height .

Example answer:
{"entities": [{"text": "insectivores", "type": "Eukaryote"}, {"text": "positively", "type": "Finding"}, {"text": "open", "type": "SpatialConcept"}, {"text": "area", "type": "SpatialConcept"}]}

Example input:
Sentence: There were significant differences in both GOX transcripts and activity elicited by allelochemicals , but only in GOX transcripts by P : C ratios in both species .

Example answer:
{"entities": [{"text": "GOX", "type": "AnatomicalStructure"}, {"text": "transcripts", "type": "Chemical"}, {"text": "allelochemicals", "type": "Chemical"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: GOX activity and transcripts are upregulated concurrently with food ingestion and body growth , downregulated with stopping ingestion and wandering for pupation in both species .

Example answer:
{"entities": [{"text": "GOX", "type": "AnatomicalStructure"}, {"text": "transcripts", "type": "Chemical"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "food", "type": "Food"}, {"text": "ingestion", "type": "BiologicFunction"}, {"text": "body growth", "type": "BiologicFunction"}, {"text": "downregulated", "type": "BiologicFunction"}, {"text": "pupation", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}]}

Input:
Sentence: Whether generalist herbivores always have significantly higher GOX activities than their specialist counterparts at any comparable stage or conditions and how this is realized remain unknown .

## Item MedMentions:test:4118
Example input:
Sentence: Rubinstein - Taybi Syndrome Associated with Pituitary Macroadenoma : A Case Report Rubinstein - Taybi Syndrome ( RSTS ) is an autosomal dominant disorder that is classically characterized by prenatal and postnatal growth restriction , microcephaly , dysmorphic craniofacial features , broad thumbs and toes , and intellectual disability .

Example answer:
{"entities": [{"text": "Rubinstein - Taybi Syndrome", "type": "BiologicFunction"}, {"text": "Pituitary Macroadenoma", "type": "BiologicFunction"}, {"text": "Case Report", "type": "IntellectualProduct"}, {"text": "RSTS", "type": "BiologicFunction"}, {"text": "autosomal dominant disorder", "type": "BiologicFunction"}, {"text": "growth restriction", "type": "BiologicFunction"}, {"text": "microcephaly", "type": "AnatomicalStructure"}, {"text": "dysmorphic craniofacial features", "type": "AnatomicalStructure"}, {"text": "broad thumbs", "type": "Finding"}, {"text": "toes", "type": "Finding"}, {"text": "intellectual disability", "type": "BiologicFunction"}]}

Example input:
Sentence: These include Cowden syndrome , MUTYH - associated polyposis , hereditary pancreatic cancer , Lynch syndrome , Peutz - Jeghers syndrome , familial adenomatous polyposis ( FAP ) , attenuated FAP , serrated polyposis syndrome , and hereditary gastric cancer .

Example answer:
{"entities": [{"text": "Cowden syndrome", "type": "BiologicFunction"}, {"text": "MUTYH - associated polyposis", "type": "BiologicFunction"}, {"text": "hereditary pancreatic cancer", "type": "BiologicFunction"}, {"text": "Lynch syndrome", "type": "BiologicFunction"}, {"text": "Peutz - Jeghers syndrome", "type": "BiologicFunction"}, {"text": "familial adenomatous polyposis", "type": "BiologicFunction"}, {"text": "FAP", "type": "BiologicFunction"}, {"text": "serrated polyposis syndrome", "type": "BiologicFunction"}, {"text": "hereditary gastric cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Newborn with Gastroschisis associated with Limb Anomalies Gastroschisis is often found together with other extra intestinal conditions such as limb , spine , cardiac , central nervous system and genitourinary abnormalities .

Example answer:
{"entities": [{"text": "Gastroschisis", "type": "BiologicFunction"}, {"text": "Limb Anomalies", "type": "AnatomicalStructure"}, {"text": "found", "type": "Finding"}, {"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "conditions", "type": "BiologicFunction"}, {"text": "limb", "type": "AnatomicalStructure"}, {"text": "spine", "type": "AnatomicalStructure"}, {"text": "cardiac", "type": "AnatomicalStructure"}, {"text": "central nervous system", "type": "AnatomicalStructure"}, {"text": "genitourinary abnormalities", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Combined ultrasound and exome sequencing approach recognizes Opitz G / BBB syndrome in two malformed fetuses Orofacial clefts are the most common congenital craniofacial anomalies and can occur as an isolated defect or be associated with other anomalies such as posterior fossa anomalies as a part of several genetic syndromes .

Example answer:
{"entities": [{"text": "ultrasound", "type": "HealthCareActivity"}, {"text": "exome sequencing", "type": "ResearchActivity"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "Opitz G / BBB syndrome", "type": "BiologicFunction"}, {"text": "fetuses", "type": "AnatomicalStructure"}, {"text": "Orofacial clefts", "type": "AnatomicalStructure"}, {"text": "craniofacial anomalies", "type": "AnatomicalStructure"}, {"text": "anomalies", "type": "AnatomicalStructure"}, {"text": "posterior fossa anomalies", "type": "Finding"}, {"text": "genetic syndromes", "type": "BiologicFunction"}]}

Example input:
Sentence: Variants in congenital hypogonadotrophic hypogonadism genes identified in an Indonesian cohort of 46 , XY under - virilised boys Congenital hypogonadotrophic hypogonadism ( CHH ) and Kallmann syndrome ( KS ) are caused by disruption to the hypothalamic - pituitary - gonadal ( H - P - G ) axis .

Example answer:
{"entities": [{"text": "hypogonadotrophic hypogonadism", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "Indonesian", "type": "PopulationGroup"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "46 , XY", "type": "Finding"}, {"text": "under - virilised", "type": "BiologicFunction"}, {"text": "CHH", "type": "BiologicFunction"}, {"text": "Kallmann syndrome", "type": "BiologicFunction"}, {"text": "KS", "type": "BiologicFunction"}, {"text": "hypothalamic - pituitary - gonadal ( H - P - G ) axis", "type": "BodySystem"}]}

Example input:
Sentence: We describe a female patient harboring an intrachromosomal triplication who presented to the Genetics clinic with dysmorphic features , including telecanthus , flat facial profile , and prognathism , short stature , widely spaced nipples , multiple allergy complaints , loose bowel movements , and mild speech delay .

Example answer:
{"entities": [{"text": "female", "type": "PopulationGroup"}, {"text": "intrachromosomal triplication", "type": "BiologicFunction"}, {"text": "Genetics clinic", "type": "Organization"}, {"text": "dysmorphic features", "type": "AnatomicalStructure"}, {"text": "telecanthus", "type": "Finding"}, {"text": "flat facial profile", "type": "Finding"}, {"text": "prognathism", "type": "AnatomicalStructure"}, {"text": "short stature", "type": "Finding"}, {"text": "widely spaced nipples", "type": "Finding"}, {"text": "multiple allergy complaints", "type": "BiologicFunction"}, {"text": "loose bowel movements", "type": "Finding"}, {"text": "mild speech delay", "type": "Finding"}]}

Example input:
Sentence: To study symptom support in these cases , we performed gastrostomies on 3 patients with V180I genetic Creutzfeldt - Jakob disease ( CJD ) who had become akinetic and mute , and compared them to 14 other similar patients being fed by tube .

Example answer:
{"entities": [{"text": "symptom", "type": "Finding"}, {"text": "gastrostomies", "type": "HealthCareActivity"}, {"text": "V180I genetic Creutzfeldt - Jakob disease", "type": "BiologicFunction"}, {"text": "CJD", "type": "BiologicFunction"}, {"text": "mute", "type": "Finding"}, {"text": "fed by tube", "type": "HealthCareActivity"}]}

Example input:
Sentence: A 41 - week , 4 , 165 g , female presented with craniosynostosis , pre - axial polysyndactyly , and cutaneous findings consistent with a clinical diagnosis of CJS .

Example answer:
{"entities": [{"text": "craniosynostosis", "type": "BiologicFunction"}, {"text": "pre - axial polysyndactyly", "type": "Finding"}, {"text": "cutaneous findings", "type": "Finding"}, {"text": "clinical diagnosis", "type": "HealthCareActivity"}, {"text": "CJS", "type": "BiologicFunction"}]}

Example input:
Sentence: This report describes the gastrointestinal and surgical findings in a baby with CJS who presented with abdominal obstruction and reviews the spectrum of gastrointestinal malformations in this rare disorder .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "gastrointestinal", "type": "SpatialConcept"}, {"text": "surgical findings", "type": "Finding"}, {"text": "CJS", "type": "BiologicFunction"}, {"text": "spectrum of gastrointestinal malformations", "type": "Finding"}, {"text": "rare disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: Gastrointestinal features including structural malformations , motility disorders , and upper GI bleeding are major causes of morbidity in CJS .

Example answer:
{"entities": [{"text": "Gastrointestinal", "type": "SpatialConcept"}, {"text": "features", "type": "Finding"}, {"text": "structural malformations", "type": "Finding"}, {"text": "motility disorders", "type": "BiologicFunction"}, {"text": "upper GI bleeding", "type": "BiologicFunction"}, {"text": "CJS", "type": "BiologicFunction"}]}

Input:
Sentence: Gastrointestinal disorders in Curry - Jones syndrome : Clinical and molecular insights from an affected newborn Curry - Jones syndrome ( CJS ) is a pattern of malformation that includes craniosynostosis , pre - axial polysyndactyly , agenesis of the corpus callosum , cutaneous and gastrointestinal abnormalities .

## Item MedMentions:test:4525
Example input:
Sentence: In multivariate analysis , a smear - positive sputum sample ( OR : 3 . 68 ; 95 % CI : 1 . 63 - 8 . 30 ) and a diagnosis at the university hospital ( OR : 2 . 61 ; 95 % CI : 1 . 14 - 5 . 96 ) were significantly associated with a system delay ≤1 month .

Example answer:
{"entities": [{"text": "smear - positive sputum sample", "type": "BodySubstance"}, {"text": "diagnosis", "type": "Finding"}, {"text": "university hospital", "type": "Organization"}]}

Example input:
Sentence: There was also a significant correlation between BODE - index and ∆VO2 / ∆WR ( r = - 0 . 64 , P < 0 . 001 ) and breathing - reserve ( r = - 0 . 38 , P = 0 . 018 ) .

Example answer:
{"entities": [{"text": "BODE - index", "type": "IntellectualProduct"}, {"text": "∆VO2", "type": "Finding"}, {"text": "∆WR", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The indications of surgery were , on one hand , difficult nasal breathing and altered nasal function ( tendency for chronic rhinosinusitis ) and on the other hand the aesthetic look of the nose .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "nasal breathing", "type": "Finding"}, {"text": "altered nasal function", "type": "BiologicFunction"}, {"text": "tendency", "type": "Finding"}, {"text": "chronic rhinosinusitis", "type": "BiologicFunction"}, {"text": "nose", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 6 , 95 % CI : 1 . 1 - 6 . 2 , and respiratory related arousal index : ≥7 . 6 / h OR = 2 . 3 , 95 % CI : 1 . 1 - 4 . 7 , but not measures of hypoxemia after adjustment for age , hypertension , diabetes , smoking , obesity , and NSAID use .

Example answer:
{"entities": [{"text": "arousal", "type": "BiologicFunction"}, {"text": "index", "type": "IntellectualProduct"}, {"text": "hypoxemia", "type": "Finding"}, {"text": "hypertension", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "NSAID", "type": "Chemical"}]}

Example input:
Sentence: Finally , the sensation -related barriers subscale was significantly associated with testing positive for Chlamydia and / or gonorrhea ( P = 0 . 049 ) .

Example answer:
{"entities": [{"text": "sensation", "type": "BiologicFunction"}, {"text": "barriers", "type": "HealthCareActivity"}, {"text": "subscale", "type": "IntellectualProduct"}, {"text": "positive", "type": "Finding"}, {"text": "Chlamydia", "type": "Bacterium"}, {"text": "gonorrhea", "type": "BiologicFunction"}]}

Example input:
Sentence: Regarding criterion validity , the Horn index showed a correlation of 0 . 722 ( 95 % CI : 0 . 677 - 0 .

Example answer:
{"entities": []}

Example input:
Sentence: Based on the questionnaire , all patients experienced improvement of nasal breathing function , improved appearance of the nose and less stigmatization from the society .

Example answer:
{"entities": [{"text": "questionnaire", "type": "IntellectualProduct"}, {"text": "experienced", "type": "BiologicFunction"}, {"text": "nasal breathing function", "type": "BiologicFunction"}, {"text": "improved", "type": "Finding"}, {"text": "nose", "type": "AnatomicalStructure"}, {"text": "society", "type": "Organization"}]}

Example input:
Sentence: Survey SNOT - 20 ( Sino - Nasal Outcome Test - 20 ) in Polish was completed by patients before surgery and during the postoperative control visits .

Example answer:
{"entities": [{"text": "Survey SNOT - 20", "type": "IntellectualProduct"}, {"text": "Sino - Nasal Outcome Test - 20", "type": "IntellectualProduct"}]}

Example input:
Sentence: The feeling of nasal obstruction is the most reproducible and reliable complaint reported by the patient with rhinological problems .

Example answer:
{"entities": [{"text": "nasal obstruction", "type": "Finding"}, {"text": "rhinological problems", "type": "BiologicFunction"}]}

Example input:
Sentence: The correlation of the results of the survey SNOT - 20 of objective studies of nasal obstruction and the geometry of the nasal cavities In this paper were verified the correlation between the results of the survey SNOT - 20 and the results of the objective tests of nasal obstruction which are rhinomanometry and acoustic rhinometry before and after surgical treatment , such as septoplasty , septoconchoplasty , ethmoidectomy and septoethmoidectomy .

Example answer:
{"entities": [{"text": "survey SNOT - 20", "type": "IntellectualProduct"}, {"text": "nasal obstruction", "type": "Finding"}, {"text": "nasal cavities", "type": "SpatialConcept"}, {"text": "results of the objective tests", "type": "Finding"}, {"text": "rhinomanometry", "type": "HealthCareActivity"}, {"text": "acoustic rhinometry", "type": "HealthCareActivity"}, {"text": "surgical treatment", "type": "HealthCareActivity"}, {"text": "septoplasty", "type": "HealthCareActivity"}, {"text": "septoconchoplasty", "type": "HealthCareActivity"}, {"text": "ethmoidectomy", "type": "HealthCareActivity"}, {"text": "septoethmoidectomy", "type": "HealthCareActivity"}]}

Input:
Sentence: The calculated correlations between the objective parameter , which was the resistance to the flow of air through the nasal cavity , and the subjective feelings of respondents expressed in the survey SNOT - 20 were generally weak , and statistical significance was achieved with respect to the first question survey ( the severity of the nose obstruction ) for all components of resistance flow .

## Item MedMentions:test:4554
Example input:
Sentence: Biobank and Genomic Research in Uganda : Are Extant Privacy and Confidentiality Regimes Adequate ? Not many African countries have been able to develop a robust system for regulating health research within their respective jurisdictions , particularly in the realm of biobanking and genomics .

Example answer:
{"entities": [{"text": "Genomic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Research", "type": "ResearchActivity"}, {"text": "Uganda", "type": "SpatialConcept"}, {"text": "African countries", "type": "SpatialConcept"}, {"text": "health research", "type": "ResearchActivity"}, {"text": "jurisdictions", "type": "IntellectualProduct"}, {"text": "genomics", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Promotion of sanitation and hygiene in a rural area of South India : A community - based study Globally , billions of people do not have access to improved sanitation and many defecate in the open air .

Example answer:
{"entities": [{"text": "Promotion", "type": "HealthCareActivity"}, {"text": "sanitation", "type": "Finding"}, {"text": "hygiene", "type": "Finding"}, {"text": "South India", "type": "SpatialConcept"}, {"text": "community - based study", "type": "ResearchActivity"}, {"text": "people", "type": "PopulationGroup"}]}

Example input:
Sentence: Natural vegetation patches inside the plantation mosaic supported high mean acoustic diversity ( indigenous forests 7 . 6 , grasslands 8 . 0 , wetlands 9 . 1 ) , which increased as plant heterogeneity and patch size increased .

Example answer:
{"entities": [{"text": "grasslands", "type": "SpatialConcept"}, {"text": "plant", "type": "Eukaryote"}, {"text": "patch size", "type": "SpatialConcept"}]}

Example input:
Sentence: Regulation , legitimation , force and markets constituted the mixture of the power elements that FPA governing authorities used to exclude local communities .

Example answer:
{"entities": [{"text": "FPA", "type": "SpatialConcept"}, {"text": "local", "type": "SpatialConcept"}]}

Example input:
Sentence: Indigenous forest patches within the plantation mosaic contained a highly characteristic acoustic species assemblage , emphasizing their complementary contribution to local biodiversity .

Example answer:
{"entities": [{"text": "acoustic species", "type": "IntellectualProduct"}, {"text": "local", "type": "SpatialConcept"}]}

Example input:
Sentence: The seed network furnishing the wild apple reintroduction agroforestry programmes was found to suffer from poor genetic diversity , introgressions and species misidentification .

Example answer:
{"entities": [{"text": "seed", "type": "Eukaryote"}, {"text": "wild apple", "type": "Eukaryote"}, {"text": "introgressions", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: Field research was carried out in four neighbouring villages in a mountain valley of the Diebu ( Tewo ) county , surrounded by spruce forests .

Example answer:
{"entities": [{"text": "villages", "type": "SpatialConcept"}, {"text": "mountain", "type": "SpatialConcept"}, {"text": "valley", "type": "SpatialConcept"}, {"text": "Diebu ( Tewo ) county", "type": "SpatialConcept"}]}

Example input:
Sentence: Local communities ' access to low value FPA resources improved during the post - colonial period but access to high value resources like commercial timber as well as sharing income benefits derived from FPA commercial activities remained a pipe dream .

Example answer:
{"entities": [{"text": "Local", "type": "SpatialConcept"}, {"text": "FPA", "type": "SpatialConcept"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: During the colonial period , it was total exclusion whereby people were evicted from forest land as well as being denied access to basic resources for their livelihoods .

Example answer:
{"entities": [{"text": "people", "type": "PopulationGroup"}]}

Example input:
Sentence: However , from the year 2000 , local communities expressed their dissatisfaction with the centralised exclusionary governance system by invading the FPAs rendering them ungovernable .

Example answer:
{"entities": [{"text": "local", "type": "SpatialConcept"}, {"text": "dissatisfaction", "type": "BiologicFunction"}, {"text": "FPAs", "type": "SpatialConcept"}, {"text": "ungovernable", "type": "Finding"}]}

Input:
Sentence: Forest protected areas governance in Zimbabwe : Shift needed away from a long history of local community exclusion In this literature review based paper we explored the concept of exclusion of local communities from accessing resources in forest protected areas ( FPAs ) in Zimbabwe .

## Item MedMentions:test:4474
Example input:
Sentence: In this study , consistent with a developmental psychopathology perspective emphasizing the value of process - oriented longitudinal study of child adjustment in developmental and social - ecological contexts , we tested emotional insecurity about the community as a dynamic , within - person mediating process for relations between sectarian community violence and child adjustment .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "psychopathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "longitudinal study", "type": "ResearchActivity"}, {"text": "adjustment", "type": "BiologicFunction"}, {"text": "emotional insecurity", "type": "BiologicFunction"}, {"text": "sectarian", "type": "PopulationGroup"}]}

Example input:
Sentence: Independent t - tests were used to compare girls with and without DBD , while path analyses tested for the mediating role of post - trauma symptoms in the relation between stress regulating systems and externalizing behaviour . Females with DBD ( n = 37 ) reported significantly higher rates of post - trauma symptoms and externalizing behaviour problems than girls without DBD ( n = 39 ) .

Example answer:
{"entities": [{"text": "t - tests", "type": "IntellectualProduct"}, {"text": "DBD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "stress regulating systems", "type": "BodySystem"}, {"text": "externalizing behaviour", "type": "Finding"}, {"text": "externalizing behaviour problems", "type": "BiologicFunction"}]}

Example input:
Sentence: This study investigated how alcohol intoxication and time of interview affected reports of intimate partner violence ( IPV ) .

Example answer:
{"entities": [{"text": "alcohol intoxication", "type": "BiologicFunction"}]}

Example input:
Sentence: We examined variables thought to be associated with unproductive and constructive processing of traumatic experiences in a sample of 81 youth with elevated PTSD symptoms , who received Trauma - Focused Cognitive Behavioral Therapy ( TF - CBT ) for abuse or traumatic interpersonal loss .

Example answer:
{"entities": [{"text": "unproductive and constructive processing", "type": "Finding"}, {"text": "traumatic experiences", "type": "BiologicFunction"}, {"text": "PTSD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "Trauma - Focused Cognitive Behavioral Therapy", "type": "HealthCareActivity"}, {"text": "TF - CBT", "type": "HealthCareActivity"}, {"text": "abuse", "type": "Finding"}, {"text": "traumatic", "type": "BiologicFunction"}]}

Example input:
Sentence: Therefore , the aim of the present study is to investigate post - trauma symptoms as a potential mediator in the relation between stress - regulation systems functioning and conduct problems in female adolescents .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "symptoms", "type": "Finding"}, {"text": "stress - regulation systems", "type": "BodySystem"}, {"text": "conduct problems", "type": "BiologicFunction"}]}

Example input:
Sentence: Regression and associated mediation analyses indicated that , while there was a direct effect of trauma exposure on mental health outcomes ( PTSD symptoms ) , daily environmental stressors partially mediated this relationship .

Example answer:
{"entities": [{"text": "Regression", "type": "IntellectualProduct"}, {"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "mental health", "type": "BiologicFunction"}, {"text": "PTSD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: Longitudinal studies typically assessed trauma exposure retrospectively , often after addictive behavior onset , thus precluding robust inferences about whether traumatization affects initial onset of addictive behaviors .

Example answer:
{"entities": [{"text": "Longitudinal studies", "type": "ResearchActivity"}, {"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "addictive behavior", "type": "BiologicFunction"}, {"text": "traumatization", "type": "InjuryOrPoisoning"}, {"text": "addictive behaviors", "type": "BiologicFunction"}]}

Example input:
Sentence: Instead , the proportions of associations tested in this literature that revealed positive , negative , or  relationships between trauma exposure and subsequent addictive behaviors were recorded , along with other methodological features .

Example answer:
{"entities": [{"text": "literature", "type": "IntellectualProduct"}, {"text": "positive", "type": "Finding"}, {"text": "negative", "type": "Finding"}, {"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "addictive behaviors", "type": "BiologicFunction"}]}

Example input:
Sentence: In the 181 prospective observational studies ( 407 , 041 participants , 98 . 8 % recruited from developed countries ) , 35 . 1 % of the tested associations between trauma exposure and later addictive behaviors was positive , 1 . 3 % was negative , and 63 .

Example answer:
{"entities": [{"text": "observational studies", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "addictive behaviors", "type": "BiologicFunction"}, {"text": "positive", "type": "Finding"}, {"text": "negative", "type": "Finding"}]}

Example input:
Sentence: A subset of observational studies ( N = 181 ) prospectively investigating the relationship between exposure to interpersonal traumata and subsequent behavioral or substance - related addiction problems were characterized .

Example answer:
{"entities": [{"text": "observational studies", "type": "ResearchActivity"}, {"text": "traumata", "type": "InjuryOrPoisoning"}, {"text": "behavioral", "type": "BiologicFunction"}, {"text": "addiction", "type": "BiologicFunction"}, {"text": "problems", "type": "Finding"}]}

Input:
Sentence: Relationship between interpersonal trauma exposure and addictive behaviors : a systematic review The aim of this study was to systematically summarize knowledge on the association between exposure to interpersonal trauma and addictive behaviors .
