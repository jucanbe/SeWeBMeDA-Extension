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

## Item MedMentions:test:2055
Example input:
Sentence: 95±1 .

Example answer:
{"entities": []}

Example input:
Sentence: 14 ± 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 1 ± 15 . 8 , and 13 . 9 ± 2 .

Example answer:
{"entities": []}

Example input:
Sentence: 4 ± 14 .

Example answer:
{"entities": []}

Example input:
Sentence: 13±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 1±13 .

Example answer:
{"entities": []}

Example input:
Sentence: 14 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 15±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 15±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 77±2 . 59 to 14 .

Example answer:
{"entities": []}

Input:
Sentence: 14 . 0±1 .

## Item MedMentions:test:1909
Example input:
Sentence: The most cytotoxic isolate , TV - LACM6 , hydrolyzes ATP , GTP with more efficiency than AMP and GMP .

Example answer:
{"entities": [{"text": "TV - LACM6", "type": "Eukaryote"}, {"text": "hydrolyzes ATP", "type": "BiologicFunction"}, {"text": "GTP", "type": "Chemical"}, {"text": "AMP", "type": "Chemical"}, {"text": "GMP", "type": "Chemical"}]}

Example input:
Sentence: 97 Å resolution crystal structure of homotrimeric KlacPNP with an intrinsically bound hypoxanthine in the active site .

Example answer:
{"entities": [{"text": "crystal structure", "type": "Chemical"}, {"text": "homotrimeric", "type": "BiologicFunction"}, {"text": "KlacPNP", "type": "Chemical"}, {"text": "intrinsically", "type": "SpatialConcept"}, {"text": "bound", "type": "BiologicFunction"}, {"text": "hypoxanthine", "type": "Chemical"}]}

Example input:
Sentence: We recently reported that Pneumocystis carinii , Pneumocystis murina , and most significantly , Pneumocystis jirovecii lack both enzymes necessary for myo - inositol biosynthesis but contain genes with homologies to fungal myo - inositol transporters .

Example answer:
{"entities": [{"text": "Pneumocystis carinii", "type": "Eukaryote"}, {"text": "Pneumocystis murina", "type": "Eukaryote"}, {"text": "Pneumocystis jirovecii", "type": "Eukaryote"}, {"text": "enzymes", "type": "Chemical"}, {"text": "myo - inositol biosynthesis", "type": "BiologicFunction"}, {"text": "genes with homologies", "type": "AnatomicalStructure"}, {"text": "fungal", "type": "Eukaryote"}, {"text": "myo - inositol", "type": "Chemical"}, {"text": "transporters", "type": "Chemical"}]}

Example input:
Sentence: The results of limited proteolysis indicated that Glu138Pro mutant was more resistant against trypsinolysis and this variant was less quenched in both acrylamide and KI quenching experiments .

Example answer:
{"entities": [{"text": "limited proteolysis", "type": "BiologicFunction"}, {"text": "Glu138Pro mutant", "type": "Chemical"}, {"text": "trypsinolysis", "type": "BiologicFunction"}, {"text": "variant", "type": "Chemical"}, {"text": "acrylamide", "type": "Chemical"}, {"text": "KI", "type": "Chemical"}, {"text": "quenching experiments", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here , we report structurally and functionally characterized purine nucleoside phosphorylase ( PNP ) from Kluyveromyces lactis ( KlacPNP ) , a key enzyme involved in the purine degradation pathway .

Example answer:
{"entities": [{"text": "structurally", "type": "SpatialConcept"}, {"text": "purine nucleoside phosphorylase", "type": "Chemical"}, {"text": "PNP", "type": "Chemical"}, {"text": "Kluyveromyces lactis", "type": "Eukaryote"}, {"text": "KlacPNP", "type": "Chemical"}, {"text": "enzyme", "type": "Chemical"}]}

Example input:
Sentence: Here , we demonstrate that KlacPNP and KlacPNPN256D could be used to catalyze a key reaction involved in lowering beer purine content .

Example answer:
{"entities": [{"text": "KlacPNP", "type": "Chemical"}, {"text": "KlacPNPN256D", "type": "Chemical"}, {"text": "reaction", "type": "BiologicFunction"}, {"text": "beer", "type": "Food"}, {"text": "purine", "type": "Chemical"}]}

Example input:
Sentence: To engineer enzymes with broad substrate specificity , we created two point variants , KlacPNPN256D and KlacPNPN256E , by replacing the catalytically active Asn256 with Asp and Glu , respectively , based on structural and comparative sequence analysis .

Example answer:
{"entities": [{"text": "engineer enzymes", "type": "Chemical"}, {"text": "KlacPNPN256D", "type": "Chemical"}, {"text": "KlacPNPN256E", "type": "Chemical"}, {"text": "Asn256", "type": "Chemical"}, {"text": "Asp", "type": "Chemical"}, {"text": "Glu", "type": "Chemical"}, {"text": "structural", "type": "SpatialConcept"}, {"text": "sequence analysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: KlacPNP belongs to the nucleoside phosphorylase - I ( NP - I ) family , and it specifically utilizes 6 - oxopurine substrates in the following order : inosine > guanosine > xanthosine , but is inactive towards adenosine .

Example answer:
{"entities": [{"text": "KlacPNP", "type": "Chemical"}, {"text": "nucleoside phosphorylase - I", "type": "Chemical"}, {"text": "NP - I", "type": "Chemical"}, {"text": "6 - oxopurine substrates", "type": "Chemical"}, {"text": "inosine", "type": "Chemical"}, {"text": "guanosine", "type": "Chemical"}, {"text": "xanthosine", "type": "Chemical"}, {"text": "adenosine", "type": "Chemical"}]}

Example input:
Sentence: Since KlacPNPN256D has broad substrate specificity , a combination of engineered KlacPNP and other enzymes involved in purine degradation could effectively lower the purine content in foods and beverages .

Example answer:
{"entities": [{"text": "KlacPNPN256D", "type": "Chemical"}, {"text": "engineered", "type": "Chemical"}, {"text": "KlacPNP", "type": "Chemical"}, {"text": "enzymes", "type": "Chemical"}, {"text": "purine", "type": "Chemical"}, {"text": "foods", "type": "Food"}, {"text": "beverages", "type": "Food"}]}

Example input:
Sentence: KlacPNPN256D not only displayed broad substrate specificity by utilizing both 6 - oxopurines and 6 - aminopurines in the order adenosine > inosine > xanthosine > guanosine , but also displayed reversal of substrate specificity .

Example answer:
{"entities": [{"text": "KlacPNPN256D", "type": "Chemical"}, {"text": "6 - oxopurines", "type": "Chemical"}, {"text": "6 - aminopurines", "type": "Chemical"}, {"text": "adenosine", "type": "Chemical"}, {"text": "inosine", "type": "Chemical"}, {"text": "xanthosine", "type": "Chemical"}, {"text": "guanosine", "type": "Chemical"}]}

Input:
Sentence: In contrast , KlacPNPN256E was highly specific to inosine and could not utilize other tested substrates .

## Item MedMentions:test:1927
Example input:
Sentence: Importantly , the change in IHRT was greater than placebo at mid for both absolute [ 4 . 4 % greater change , 90 % Confidence Interval ( CI ) 1 . 0 : 8 . 0 % , ES 0 . 21 , and relative strength ( 5 .

Example answer:
{"entities": [{"text": "IHRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: In comparison between different groups at the end of the first and sixth weeks , maximum changes in healing indicators were observed in the systemic group and the least variations were related to the control group .

Example answer:
{"entities": [{"text": "healing", "type": "BiologicFunction"}]}

Example input:
Sentence: 95 - 0 . 99 ) and OS ( HR = 0 . 94 ; 95 % CI 0 . 91 - 0 . 97 ) as well as from the first to the third chemotherapy cycle for OS ( HR = 0 .

Example answer:
{"entities": [{"text": "chemotherapy cycle", "type": "HealthCareActivity"}]}

Example input:
Sentence: The primary outcome is weight change from baseline to the end of Phase I , with the change at the end of Phase II a key secondary endpoint .

Example answer:
{"entities": [{"text": "weight change from baseline", "type": "Finding"}, {"text": "change", "type": "Finding"}]}

Example input:
Sentence: Nutritional status and changes in muscle mass were assessed by subjective global assessment , percentage creatinine generation rate ( % CGR ) , creatinine index ( CI ) and lean body mass ( LBM ) estimated by dual - energy X - ray absorptiometry ( DXA ) .

Example answer:
{"entities": [{"text": "Nutritional status", "type": "Finding"}, {"text": "muscle mass", "type": "Finding"}, {"text": "subjective global assessment", "type": "IntellectualProduct"}, {"text": "lean body mass", "type": "ClinicalAttribute"}, {"text": "LBM", "type": "ClinicalAttribute"}, {"text": "dual - energy X - ray absorptiometry", "type": "HealthCareActivity"}, {"text": "DXA", "type": "HealthCareActivity"}]}

Example input:
Sentence: The placebo - subtracted differences in the change in glycated haemoglobin ( HbA1c ) and body weight from baseline to week 12 or week 24 were evaluated by race or ethnicity using repeated measure analysis of unstructured covariance .

Example answer:
{"entities": [{"text": "glycated haemoglobin", "type": "Chemical"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "race", "type": "PopulationGroup"}, {"text": "ethnicity", "type": "PopulationGroup"}]}

Example input:
Sentence: The primary endpoint was the difference in the rate of weight change over 16 weeks ( linear mixed - effect model for repeated measures ) between high - dose espindolol and placebo .

Example answer:
{"entities": [{"text": "weight change", "type": "Finding"}, {"text": "espindolol", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: Body weight changes can be recognized as a prognostic factor for PFS and OS in advanced EOC patients undergoing chemotherapy .

Example answer:
{"entities": [{"text": "Body weight changes", "type": "Finding"}, {"text": "prognostic factor", "type": "ClinicalAttribute"}, {"text": "EOC", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: A slight increase in weight occurred over the course of chemotherapy , but this change was not statistically significant .

Example answer:
{"entities": [{"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "change", "type": "Finding"}]}

Example input:
Sentence: The multivariate Cox analysis showed significant body weight changes from the first to the sixth chemotherapy cycle for PFS ( HR = 0 .

Example answer:
{"entities": [{"text": "multivariate Cox analysis", "type": "IntellectualProduct"}, {"text": "body weight changes", "type": "Finding"}, {"text": "chemotherapy cycle", "type": "HealthCareActivity"}]}

Input:
Sentence: Changes in body weight were assessed by comparing measurements at baseline to those of the third and sixth cycles of chemotherapy .

## Item MedMentions:test:2073
Example input:
Sentence: 007 , and p = 0 . 04 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 6 ( 7 . 0 ) months .

Example answer:
{"entities": []}

Example input:
Sentence: 0 months , P = 0 . 05 ) and overall survival ( 6 . 2 vs 2 .

Example answer:
{"entities": []}

Example input:
Sentence: 1 vs 7 . 6 months , P = 0 . 316 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 1 months , P = 0 . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 8±105 . 2 months , P < . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 21 . 3 months , p = -0 . 01 )

Example answer:
{"entities": []}

Example input:
Sentence: 8 months , P = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 6 months , P = 0 . 004 ) and OS ( 7 . 8 vs 8 . 4 months , P = 0 . 032 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 6 months , P = 0 . 502 ; OS : 7 . 0 vs 7 . 8 months , P = 0 . 452 ) .

Example answer:
{"entities": []}

Input:
Sentence: 2 months , P = 0 . 002 ; OS 7 .

## Item MedMentions:test:1759
Example input:
Sentence: In each group , a 5 - mm experimental incision was made at the lumbar segment of the dura mater and cerebrospinal fluid leakage was induced .

Example answer:
{"entities": [{"text": "experimental incision", "type": "HealthCareActivity"}, {"text": "lumbar segment of the dura mater", "type": "SpatialConcept"}, {"text": "cerebrospinal fluid leakage", "type": "BiologicFunction"}]}

Example input:
Sentence: Incomplete Annular Pancreas with Ectopic Opening of the Pancreatic and Bile Ducts into the Pyloric Ring : First Report of a Rare Anomaly The patient was a 56 - year - old woman who had experienced epigastralgia and dorsal pain several times over the last 20 years .

Example answer:
{"entities": [{"text": "Annular Pancreas", "type": "AnatomicalStructure"}, {"text": "Ectopic", "type": "SpatialConcept"}, {"text": "Opening", "type": "SpatialConcept"}, {"text": "Pancreatic", "type": "AnatomicalStructure"}, {"text": "Bile Ducts", "type": "AnatomicalStructure"}, {"text": "Pyloric Ring", "type": "AnatomicalStructure"}, {"text": "Report", "type": "IntellectualProduct"}, {"text": "Anomaly", "type": "Finding"}, {"text": "epigastralgia", "type": "Finding"}, {"text": "dorsal pain", "type": "Finding"}]}

Example input:
Sentence: During the operation , intraperitoneal examination of the rectovesical pouch revealed calcifications and stones , which were subsequently identified as gallstones .

Example answer:
{"entities": [{"text": "operation", "type": "HealthCareActivity"}, {"text": "intraperitoneal", "type": "SpatialConcept"}, {"text": "rectovesical pouch", "type": "SpatialConcept"}, {"text": "calcifications", "type": "BiologicFunction"}, {"text": "stones", "type": "BodySubstance"}, {"text": "gallstones", "type": "BodySubstance"}]}

Example input:
Sentence: No papilla of Vater was present in the descending duodenum , and 2 small holes were present in the pyloric ring .

Example answer:
{"entities": [{"text": "papilla of Vater", "type": "AnatomicalStructure"}, {"text": "descending duodenum", "type": "AnatomicalStructure"}, {"text": "holes", "type": "SpatialConcept"}, {"text": "pyloric ring", "type": "AnatomicalStructure"}]}

Example input:
Sentence: However , in this patient , ( 1 ) the pancreas encompassed the pyloric ring , ( 2 ) the pancreatic and bile ducts opened separately , and ( 3 ) the openings of the pancreatic and bile duct s were present in the pyloric ring .

Example answer:
{"entities": [{"text": "pancreas", "type": "AnatomicalStructure"}, {"text": "encompassed", "type": "SpatialConcept"}, {"text": "pyloric ring", "type": "AnatomicalStructure"}, {"text": "pancreatic", "type": "AnatomicalStructure"}, {"text": "bile ducts", "type": "AnatomicalStructure"}, {"text": "opened", "type": "SpatialConcept"}, {"text": "bile duct s", "type": "AnatomicalStructure"}, {"text": "present", "type": "Finding"}]}

Example input:
Sentence: An upper GI endoscopy showed the catheter pulled into the duodenum causing gastric outlet obstruction .

Example answer:
{"entities": [{"text": "upper GI endoscopy", "type": "HealthCareActivity"}, {"text": "catheter", "type": "MedicalDevice"}, {"text": "pulled into", "type": "Finding"}, {"text": "duodenum", "type": "AnatomicalStructure"}, {"text": "gastric outlet obstruction", "type": "BiologicFunction"}]}

Example input:
Sentence: The fluorescence system demonstrated an hypoperfused area in the ascending colon , therefore an ileocholic resection was thus performed .

Example answer:
{"entities": [{"text": "fluorescence system", "type": "HealthCareActivity"}, {"text": "ascending colon", "type": "AnatomicalStructure"}, {"text": "ileocholic resection", "type": "HealthCareActivity"}]}

Example input:
Sentence: It was considered that the pancreatic and bile ducts separately opened into the pyloric ring .

Example answer:
{"entities": [{"text": "pancreatic", "type": "AnatomicalStructure"}, {"text": "bile ducts", "type": "AnatomicalStructure"}, {"text": "opened", "type": "SpatialConcept"}, {"text": "pyloric ring", "type": "AnatomicalStructure"}]}

Example input:
Sentence: During routine laparoscopic exploration , right vas deferens and testicular vessels were entering the right internal inguinal ring so right inguinal exploration was done , which revealed blind ending vas deferens and testicular vessels and the left testis was found intra - abdominally near the left internal ring with a mass on its upper pole .

Example answer:
{"entities": [{"text": "laparoscopic", "type": "HealthCareActivity"}, {"text": "exploration", "type": "HealthCareActivity"}, {"text": "right vas deferens", "type": "AnatomicalStructure"}, {"text": "right internal inguinal ring", "type": "AnatomicalStructure"}, {"text": "right inguinal", "type": "SpatialConcept"}, {"text": "blind ending", "type": "Finding"}, {"text": "vas deferens", "type": "AnatomicalStructure"}, {"text": "left testis", "type": "AnatomicalStructure"}, {"text": "intra - abdominally", "type": "SpatialConcept"}, {"text": "internal ring", "type": "SpatialConcept"}, {"text": "mass", "type": "Finding"}, {"text": "upper pole", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The advancement of guidewires and other instruments within transparent mock bile ducts can be viewed in the window of the simulator without the need for fluoroscopy .

Example answer:
{"entities": [{"text": "instruments", "type": "MedicalDevice"}, {"text": "bile ducts", "type": "AnatomicalStructure"}, {"text": "simulator", "type": "MedicalDevice"}, {"text": "fluoroscopy", "type": "HealthCareActivity"}]}

Input:
Sentence: Bile excretion from one of the small holes was observed under forward - viewing endoscope .

## Item MedMentions:test:1684
Example input:
Sentence: The composite endpoint of procedure failure or acute complication was less common in the STSF group ( 2 vs . 8 , P = 0 . 05 ) .

Example answer:
{"entities": [{"text": "complication", "type": "BiologicFunction"}]}

Example input:
Sentence: Of the 85 laparoscopic orchiopexies , 35 underwent SFS and 50 had SSLO .

Example answer:
{"entities": [{"text": "laparoscopic orchiopexies", "type": "HealthCareActivity"}, {"text": "SSLO", "type": "HealthCareActivity"}]}

Example input:
Sentence: A descriptive comparative design was employed on a convenience sample of 260 patients who underwent a percutaneous coronary intervention and 105 patients who underwent open - heart surgery patients .

Example answer:
{"entities": [{"text": "sample", "type": "PopulationGroup"}, {"text": "percutaneous coronary intervention", "type": "HealthCareActivity"}, {"text": "open - heart surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: We performed a retrospective analysis of 244 patients implanted with a continuous flow ( CF ) LVAD .

Example answer:
{"entities": [{"text": "retrospective analysis", "type": "ResearchActivity"}, {"text": "implanted", "type": "HealthCareActivity"}, {"text": "continuous flow ( CF ) LVAD", "type": "MedicalDevice"}]}

Example input:
Sentence: Regression analysis was performed to compare outcomes between patients who underwent SFS and SSLO .

Example answer:
{"entities": [{"text": "Regression analysis", "type": "IntellectualProduct"}, {"text": "SSLO", "type": "HealthCareActivity"}]}

Example input:
Sentence: For a three - year period , TIF procedures were performed on 80 patients .

Example answer:
{"entities": []}

Example input:
Sentence: The STSF catheter is safe and effective in treating a range of arrhythmias .

Example answer:
{"entities": [{"text": "arrhythmias", "type": "Finding"}]}

Example input:
Sentence: In our unit , it superseded the ThermoCool ( ® ) SF catheter from the time of its introduction in May 2015 .

Example answer:
{"entities": []}

Example input:
Sentence: Compared with the SF catheter , it shows a trend towards improved safety - efficacy balance .

Example answer:
{"entities": []}

Example input:
Sentence: Procedure -related data were collected prospectively for the first 100 ablation procedures performed in our department using the STSF catheter .

Example answer:
{"entities": [{"text": "Procedure", "type": "HealthCareActivity"}, {"text": "ablation procedures", "type": "HealthCareActivity"}]}

Input:
Sentence: From a database of 654 procedures performed in our unit using the SF catheter , we selected one to match each STSF procedure , matching for procedure type , operator experience , patient age , and gender .

## Item MedMentions:test:1652
Example input:
Sentence: ESR showed that both FPs increase lipid packing and head group ordering as well as reduce the intramembrane water content for anionic membranes .

Example answer:
{"entities": [{"text": "ESR", "type": "HealthCareActivity"}, {"text": "FPs", "type": "Chemical"}, {"text": "lipid", "type": "Chemical"}, {"text": "intramembrane", "type": "AnatomicalStructure"}, {"text": "anionic membranes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: As for the high concentration model , the minimum of the free energy profile slightly shifts to the bilayer center .

Example answer:
{"entities": [{"text": "model", "type": "IntellectualProduct"}, {"text": "bilayer", "type": "AnatomicalStructure"}, {"text": "center", "type": "SpatialConcept"}]}

Example input:
Sentence: Self - assembled nanocomplex between polymerized phenylboronic acid and doxorubicin for efficient tumor - targeted chemotherapy Since the discovery that nano - scaled particulates can easily be incorporated into tumors via the enhanced permeability and retention ( EPR ) effect , such nanostructures have been exploited as therapeutic small molecule delivery systems .

Example answer:
{"entities": [{"text": "nanocomplex", "type": "Chemical"}, {"text": "phenylboronic acid", "type": "Chemical"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "delivery systems", "type": "MedicalDevice"}]}

Example input:
Sentence: An evaluation of the buffering of hydrophilic matrix tablets containing a pH - dependent solubility weak acid drug ( flurbiprofen ) , identified as possessing a deleterious effect on hydroxypropyl methylcellulose ( HPMC ) solubility , swelling and gelation , with respect to drug dissolution and the characteristics of the hydrophilic matrix gel layer in the presence of tromethamine as a buffer was undertaken .

Example answer:
{"entities": [{"text": "evaluation", "type": "HealthCareActivity"}, {"text": "buffering", "type": "Chemical"}, {"text": "matrix tablets", "type": "Chemical"}, {"text": "weak acid drug", "type": "Chemical"}, {"text": "flurbiprofen", "type": "Chemical"}, {"text": "hydroxypropyl methylcellulose", "type": "Chemical"}, {"text": "HPMC", "type": "Chemical"}, {"text": "matrix gel layer", "type": "Chemical"}, {"text": "tromethamine", "type": "Chemical"}, {"text": "buffer", "type": "Chemical"}]}

Example input:
Sentence: It was found that both PGC and Pluronic micelles could increase the permeation of the fluorescent probe rhodamine B through RCE cells by more than ten - fold .

Example answer:
{"entities": [{"text": "PGC", "type": "Chemical"}, {"text": "Pluronic", "type": "Chemical"}, {"text": "micelles", "type": "Chemical"}, {"text": "fluorescent probe", "type": "Chemical"}, {"text": "rhodamine B", "type": "Chemical"}, {"text": "RCE cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Energy analysis show that the stabilization between the selected rofecoxib and other pre - inserted rofecoxib molecule is mainly due to van der Waals interaction energy .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "rofecoxib", "type": "Chemical"}]}

Example input:
Sentence: The predicted permeability of rofecoxib in high concentration model slightly weakens as compared with low concentration model .

Example answer:
{"entities": [{"text": "rofecoxib", "type": "Chemical"}, {"text": "model", "type": "IntellectualProduct"}]}

Example input:
Sentence: Molecular simulation study on concentration effects of rofecoxib with POPC bilayer The interactions between rofecoxib and POPC ( 1 - palmitoyl - 2 - oleoyl - sn - glycero - 3 - phosphocholine ) bilayer were studied using all - atom molecular dynamics simulation method .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "rofecoxib", "type": "Chemical"}, {"text": "POPC", "type": "Chemical"}, {"text": "bilayer", "type": "AnatomicalStructure"}, {"text": "interactions", "type": "BiologicFunction"}, {"text": "( 1 - palmitoyl - 2 - oleoyl - sn - glycero - 3 - phosphocholine )", "type": "Chemical"}, {"text": "studied", "type": "ResearchActivity"}, {"text": "method", "type": "IntellectualProduct"}]}

Example input:
Sentence: Four POPC bilayer systems with different number of rofecoxib molecules were constructed to simulate different drug concentration .

Example answer:
{"entities": [{"text": "POPC", "type": "Chemical"}, {"text": "bilayer", "type": "AnatomicalStructure"}, {"text": "rofecoxib", "type": "Chemical"}, {"text": "drug", "type": "Chemical"}]}

Example input:
Sentence: The free energy of rofecoxib passing across pure POPC bilayer has two minima ( at z ∼1 .

Example answer:
{"entities": [{"text": "rofecoxib", "type": "Chemical"}, {"text": "POPC", "type": "Chemical"}, {"text": "bilayer", "type": "AnatomicalStructure"}]}

Input:
Sentence: Moreover , the energy change from bulk water to POPC bilayer increases while the central barrier to cross the hydrophobic core of bilayer slightly decreases , suggesting that increasing drug concentration makes it favorable for rofecoxib to partition into the bilayer and easier to pass across bialyer center .

## Item MedMentions:test:1823
Example input:
Sentence: Anthropometric , metabolic and hormonal assessment and determination of habitual PA levels with a digital pedometer were evaluated in 84 women with PCOS and 67 age - and body mass index ( BMI ) - matched controls .

Example answer:
{"entities": [{"text": "hormonal assessment", "type": "HealthCareActivity"}, {"text": "digital pedometer", "type": "MedicalDevice"}, {"text": "women", "type": "PopulationGroup"}, {"text": "PCOS", "type": "BiologicFunction"}, {"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Participants using insulin pump therapy were randomized to either 12 weeks of automated closed - loop glucose control , then 12 weeks of sensor augmented insulin pump therapy ( open loop ) , or vice versa .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "insulin pump", "type": "MedicalDevice"}, {"text": "therapy", "type": "HealthCareActivity"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "glucose control", "type": "Chemical"}]}

Example input:
Sentence: Well , I Wouldn ' t be Any Worse Off , Would I , Than I am Now ? A Qualitative Study of Decision - Making , Hopes , and Realities of Adults With Type 1 Diabetes Undergoing Islet Cell Transplantation For selected individuals with type 1 diabetes , pancreatic islet transplantation ( IT ) prevents recurrent severe hypoglycemia and optimizes glycemia , although ongoing systemic immunosuppression is needed .

Example answer:
{"entities": [{"text": "Qualitative Study", "type": "ResearchActivity"}, {"text": "Decision - Making", "type": "BiologicFunction"}, {"text": "Hopes", "type": "BiologicFunction"}, {"text": "Type 1 Diabetes", "type": "BiologicFunction"}, {"text": "Islet Cell Transplantation", "type": "HealthCareActivity"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "type 1 diabetes", "type": "BiologicFunction"}, {"text": "pancreatic islet transplantation", "type": "HealthCareActivity"}, {"text": "IT", "type": "HealthCareActivity"}, {"text": "hypoglycemia", "type": "BiologicFunction"}, {"text": "optimizes glycemia", "type": "HealthCareActivity"}, {"text": "systemic immunosuppression", "type": "HealthCareActivity"}]}

Example input:
Sentence: We adapted an existing clinical - economic model to include environmental outcomes ( carbon dioxide [ CO2 ] emissions ) to predict the consequences of adding insulin to an oral antidiabetic ( OAD ) regimen for patients with type 2 diabetes mellitus ( T2DM ) over 30 years , from the United Kingdom payer perspective .

Example answer:
{"entities": [{"text": "economic model", "type": "IntellectualProduct"}, {"text": "environmental", "type": "SpatialConcept"}, {"text": "carbon dioxide", "type": "Chemical"}, {"text": "CO2", "type": "Chemical"}, {"text": "insulin", "type": "Chemical"}, {"text": "oral", "type": "SpatialConcept"}, {"text": "antidiabetic", "type": "Chemical"}, {"text": "OAD", "type": "Chemical"}, {"text": "regimen", "type": "HealthCareActivity"}, {"text": "type 2 diabetes mellitus", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "United Kingdom", "type": "SpatialConcept"}, {"text": "payer", "type": "Organization"}]}

Example input:
Sentence: In vivo testing indicates that a single patch can regulate glucose levels effectively with reduced risk of hypoglycemia .

Example answer:
{"entities": [{"text": "In vivo", "type": "SpatialConcept"}, {"text": "patch", "type": "Chemical"}, {"text": "glucose levels", "type": "Finding"}, {"text": "hypoglycemia", "type": "BiologicFunction"}]}

Example input:
Sentence: In a randomized triple - blind controlled clinical trial , 120 adults with impaired glucose tolerance based on the inclusion criteria will be selected by a simple random sampling method and will be randomly allocated to 6 months of 6 g / d probiotic , synbiotic or placebo .

Example answer:
{"entities": [{"text": "randomized triple - blind controlled clinical trial", "type": "ResearchActivity"}, {"text": "impaired glucose tolerance", "type": "BiologicFunction"}, {"text": "sampling method", "type": "IntellectualProduct"}, {"text": "probiotic", "type": "Bacterium"}, {"text": "synbiotic", "type": "Food"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: Glycemic control was assessed with glycosylated hemoglobin ( HbA1c ) at baseline and six months later .

Example answer:
{"entities": [{"text": "Glycemic control", "type": "HealthCareActivity"}, {"text": "glycosylated hemoglobin", "type": "Chemical"}, {"text": "HbA1c", "type": "Chemical"}]}

Example input:
Sentence: A total of 240 patients with type 2 diabetes ( T2DM ) attending an out - patient medical clinic were randomized to either PPBS or FBS monitoring .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "out - patient medical clinic", "type": "Organization"}, {"text": "randomized", "type": "Finding"}, {"text": "PPBS", "type": "HealthCareActivity"}, {"text": "FBS", "type": "HealthCareActivity"}, {"text": "monitoring", "type": "HealthCareActivity"}]}

Example input:
Sentence: Targeting postprandial blood sugar over fasting blood sugar : A clinic based comparative study Recent studies indicate that modulation of post prandial blood sugar ( PPBS ) plays an important role in the long term glycemic control .

Example answer:
{"entities": [{"text": "postprandial blood sugar", "type": "HealthCareActivity"}, {"text": "fasting blood sugar", "type": "HealthCareActivity"}, {"text": "clinic based comparative study", "type": "ResearchActivity"}, {"text": "post prandial blood sugar", "type": "BiologicFunction"}, {"text": "PPBS", "type": "BiologicFunction"}, {"text": "glycemic control", "type": "HealthCareActivity"}]}

Example input:
Sentence: Measurement of PPBS is more convenient for patients attending outpatient clinics than fasting blood sugar ( FBS ) as the former needs only two hours of fasting from the last meal .

Example answer:
{"entities": [{"text": "Measurement of PPBS", "type": "HealthCareActivity"}, {"text": "outpatient clinics", "type": "Organization"}, {"text": "fasting blood sugar", "type": "HealthCareActivity"}, {"text": "FBS", "type": "HealthCareActivity"}, {"text": "fasting", "type": "Finding"}, {"text": "last meal", "type": "Finding"}]}

Input:
Sentence: To assess the value of PPBS monitoring in optimization of long term glycemic control among diabetic patients attending an outpatient clinic .

## Item MedMentions:test:2094
Example input:
Sentence: 6 to 94 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 , 42 . 4 , and 66 .

Example answer:
{"entities": []}

Example input:
Sentence: 6 ( 2 . 3 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 6 - 51 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 ± 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 5 - 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 4 to 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 6 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 7 - 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 7 - 6 .

Example answer:
{"entities": []}

Input:
Sentence: 6 to 3 .

## Item MedMentions:test:1412
Example input:
Sentence: In cidaroid sea urchins , the anciently diverged sister clade to euechinoid sea urchins , a homologous SM cell type ingresses later in development , after gastrulation has commenced , and consequently at a distinct developmental address .

Example answer:
{"entities": [{"text": "cidaroid", "type": "Eukaryote"}, {"text": "sea urchins", "type": "Eukaryote"}, {"text": "sister clade", "type": "Eukaryote"}, {"text": "euechinoid", "type": "Eukaryote"}, {"text": "SM", "type": "AnatomicalStructure"}, {"text": "cell type", "type": "AnatomicalStructure"}, {"text": "ingresses", "type": "BiologicFunction"}, {"text": "development", "type": "BiologicFunction"}, {"text": "gastrulation", "type": "BiologicFunction"}, {"text": "developmental", "type": "BiologicFunction"}, {"text": "address", "type": "SpatialConcept"}]}

Example input:
Sentence: To further explore the phylogenetic relationships of invertebrate metazoan MyD88 , we applied MrBayes and PhyML software to construct phylogenetic trees using Bayesian and maximum likelihood approaches , respectively , which suggested that the MyD88 of Arthropoda was closely related to lower invertebrates , in contrast to morphological taxonomy .

Example answer:
{"entities": [{"text": "phylogenetic relationships", "type": "ResearchActivity"}, {"text": "invertebrate", "type": "Eukaryote"}, {"text": "metazoan", "type": "Eukaryote"}, {"text": "MyD88", "type": "AnatomicalStructure"}, {"text": "MrBayes and PhyML software", "type": "IntellectualProduct"}, {"text": "construct", "type": "IntellectualProduct"}, {"text": "maximum likelihood approaches", "type": "IntellectualProduct"}, {"text": "Arthropoda", "type": "Eukaryote"}, {"text": "invertebrates", "type": "Eukaryote"}, {"text": "morphological", "type": "SpatialConcept"}]}

Example input:
Sentence: To summarize , in this study , we report on the diversification of MyD88 in invertebrate metazoans , the specific evolutionary position of Arthropoda MyD88 , and the positive selection pressures on MyD88 of Arthropoda , Mollusca and Insecta .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "MyD88", "type": "AnatomicalStructure"}, {"text": "invertebrate", "type": "Eukaryote"}, {"text": "metazoans", "type": "Eukaryote"}, {"text": "evolutionary position", "type": "BiologicFunction"}, {"text": "Arthropoda", "type": "Eukaryote"}, {"text": "positive", "type": "Finding"}, {"text": "selection pressures", "type": "BiologicFunction"}, {"text": "Mollusca", "type": "Eukaryote"}, {"text": "Insecta", "type": "Eukaryote"}]}

Example input:
Sentence: Among these , the gelsolin proteins sever actin filaments , cap their fast growing end and nucleate actin assembly in a calcium - dependent manner .

Example answer:
{"entities": [{"text": "gelsolin proteins", "type": "Chemical"}, {"text": "actin filaments", "type": "AnatomicalStructure"}, {"text": "fast growing", "type": "Finding"}, {"text": "nucleate", "type": "BiologicFunction"}, {"text": "actin assembly", "type": "BiologicFunction"}, {"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: The Peripatoides and Hypsibius gelsolin revealed both conserved binding motifs for G - actin , F - actin and phosphatidylinositol 4 , 5 - bisphosphate ( PIP2 ) , along with a full set of type - 1 and type - 2 Ca ( 2 + ) - binding sites which could result in the binding of eight and four calcium ions , respectively .

Example answer:
{"entities": [{"text": "Peripatoides", "type": "Eukaryote"}, {"text": "Hypsibius", "type": "Eukaryote"}, {"text": "gelsolin", "type": "Chemical"}, {"text": "conserved", "type": "SpatialConcept"}, {"text": "binding motifs", "type": "Chemical"}, {"text": "G - actin", "type": "Chemical"}, {"text": "F - actin", "type": "Chemical"}, {"text": "phosphatidylinositol 4 , 5 - bisphosphate", "type": "Chemical"}, {"text": "PIP2", "type": "Chemical"}, {"text": "type - 1", "type": "Chemical"}, {"text": "type - 2", "type": "Chemical"}, {"text": "Ca ( 2 + )", "type": "Chemical"}, {"text": "binding sites", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "calcium ions", "type": "Chemical"}]}

Example input:
Sentence: Both gelsolin proteins lack a C - terminal latch - helix indicating a more rapid activation in the submicromolar Ca ( 2 + ) range .

Example answer:
{"entities": [{"text": "gelsolin proteins", "type": "Chemical"}, {"text": "C - terminal", "type": "SpatialConcept"}, {"text": "latch - helix", "type": "SpatialConcept"}, {"text": "Ca ( 2 + ) range", "type": "HealthCareActivity"}]}

Example input:
Sentence: Mapping of our molecular data onto a well - established phylogeny revealed that the number of gelsolin segments does not correlate with the phylogenetic lineage but rather with particular functional demands to alter the kinetics of actin polymerization .

Example answer:
{"entities": [{"text": "Mapping", "type": "HealthCareActivity"}, {"text": "molecular data", "type": "IntellectualProduct"}, {"text": "gelsolin", "type": "Chemical"}, {"text": "segments", "type": "SpatialConcept"}, {"text": "actin polymerization", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , we focus on the gelsolin of the onychophoran Peripatoides novaezealandiae and the eutardigrade Hypsibius dujardini .

Example answer:
{"entities": [{"text": "gelsolin", "type": "Chemical"}, {"text": "onychophoran", "type": "Eukaryote"}, {"text": "Peripatoides novaezealandiae", "type": "Eukaryote"}, {"text": "eutardigrade", "type": "Eukaryote"}, {"text": "Hypsibius dujardini", "type": "Eukaryote"}]}

Example input:
Sentence: However , analysis of data from TardiBase reveals that the gelsolin of the eutardigrade Hypsibius dujardini has only three segments ( S1 - S3 ) .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "TardiBase", "type": "IntellectualProduct"}, {"text": "gelsolin", "type": "Chemical"}, {"text": "eutardigrade", "type": "Eukaryote"}, {"text": "Hypsibius dujardini", "type": "Eukaryote"}, {"text": "segments", "type": "SpatialConcept"}]}

Example input:
Sentence: Gelsolin in Onychophora and Tardigrada with notes on its variability in the Ecdysozoa Rearrangements of the filamentous actin network involve a broad range of actin binding proteins .

Example answer:
{"entities": [{"text": "Gelsolin", "type": "Chemical"}, {"text": "Onychophora", "type": "Eukaryote"}, {"text": "Tardigrada", "type": "Eukaryote"}, {"text": "Ecdysozoa", "type": "Eukaryote"}, {"text": "filamentous actin network", "type": "Chemical"}, {"text": "actin binding proteins", "type": "Chemical"}]}

Input:
Sentence: We suggest that a gelsolin with three segments was present in the last common ancestor of the ecdysozoan clade Panarthropoda ( Onychophora , Tardigrada , Arthropoda ) , primarily because the gelsolin of all non - Ecdysozoa studied so far ( except Chordata ) reveals this number of segments .

## Item MedMentions:test:1894
Example input:
Sentence: baumannii asymptomatic carriage and VAP isolates from this same ICU collected during 2003 - 2007 .

Example answer:
{"entities": [{"text": "baumannii", "type": "Bacterium"}, {"text": "asymptomatic", "type": "Finding"}, {"text": "carriage", "type": "Finding"}, {"text": "VAP", "type": "BiologicFunction"}, {"text": "isolates", "type": "Chemical"}, {"text": "ICU", "type": "Organization"}]}

Example input:
Sentence: baumannii but only moderately reduced susceptibility in P .

Example answer:
{"entities": [{"text": "baumannii", "type": "Bacterium"}, {"text": "susceptibility", "type": "Finding"}, {"text": "P .", "type": "Bacterium"}]}

Example input:
Sentence: The mean age of patient was 44 . 53±8 . 69 years , 89 . 5 % of them were males .

Example answer:
{"entities": []}

Example input:
Sentence: There were also higher infection rates among patients undergoing relatively high - complexity arthroscopies , men , obese patients , diabetic patients , and younger patients ( in order of decreasing relative risk ) .

Example answer:
{"entities": [{"text": "infection rates", "type": "BiologicFunction"}, {"text": "high - complexity arthroscopies", "type": "HealthCareActivity"}, {"text": "men", "type": "PopulationGroup"}, {"text": "obese", "type": "BiologicFunction"}, {"text": "diabetic", "type": "BiologicFunction"}]}

Example input:
Sentence: 41 455 patients ( mean age 72 . 4 years , 47 . 4 % female ) were identified .

Example answer:
{"entities": []}

Example input:
Sentence: baumannii causing ventilator - associated pneumonia ( VAP ) in the ICU during 2009 - 2012 .

Example answer:
{"entities": [{"text": "baumannii", "type": "Bacterium"}, {"text": "ventilator - associated pneumonia", "type": "BiologicFunction"}, {"text": "VAP", "type": "BiologicFunction"}, {"text": "ICU", "type": "Organization"}]}

Example input:
Sentence: There were 27 male and 17 female patients with a mean age of 41 ± 12 . 7 years ( range , 15 to 67 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Patients were predominantly male ( 76 . 1 % ) and young ( mean age 28 years ) .

Example answer:
{"entities": []}

Example input:
Sentence: baumannii group ( 25 % ) was similar to other species ( 30 . 4 % ) .

Example answer:
{"entities": [{"text": "baumannii", "type": "Bacterium"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: Of 60 patients , 42 ( 70 % ) were male , all were white , with a median ( interquartile range ) age of 71 ( 64 to 82 ) years .

Example answer:
{"entities": [{"text": "white", "type": "PopulationGroup"}]}

Input:
Sentence: baumannii was 8 . 5 % and was most prevalent among patients in the age group 51 - 60 ( 36 % ) ; the male patients ( 63 . 6 % ) were more infected than their female counterparts .

## Item MedMentions:test:1489
Example input:
Sentence: Ethical considerations : No objection to the study was made by an Ethical Review Board .

Example answer:
{"entities": [{"text": "considerations", "type": "Finding"}, {"text": "No objection", "type": "Finding"}, {"text": "Ethical Review Board", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Regarding variants of uncertain clinical significance in actionable genes , we found that different understandings of autonomy lead to different conclusions and that , for some of them , it may be legitimate to refrain from returning uncertain information .

Example answer:
{"entities": [{"text": "variants", "type": "AnatomicalStructure"}, {"text": "clinical significance", "type": "Finding"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Recent improvements in the widespread availability of individual participant data from randomised controlled trials makes it feasible to conduct extensive individual participant data meta - analyses which were previously impossible , thereby reducing the effect of publication or reporting bias on the understanding of the infant immune response .

Example answer:
{"entities": [{"text": "widespread", "type": "SpatialConcept"}, {"text": "individual", "type": "PopulationGroup"}, {"text": "participant", "type": "PopulationGroup"}, {"text": "randomised controlled trials", "type": "ResearchActivity"}, {"text": "meta - analyses", "type": "ResearchActivity"}, {"text": "impossible", "type": "Finding"}, {"text": "publication", "type": "IntellectualProduct"}, {"text": "reporting", "type": "HealthCareActivity"}, {"text": "understanding", "type": "BiologicFunction"}, {"text": "immune response", "type": "BiologicFunction"}]}

Example input:
Sentence: It has been suggested that this unrelenting " genohype " is having a range of adverse social consequences , including misleading the public and hurting the long - term legitimacy of the field .

Example answer:
{"entities": [{"text": "adverse", "type": "Finding"}, {"text": "public", "type": "PopulationGroup"}, {"text": "hurting", "type": "Finding"}, {"text": "legitimacy", "type": "IntellectualProduct"}]}

Example input:
Sentence: The accumulating strong scientific evidence may thus support public health policies aimed at reducing social inequalities in cardiovascular health .

Example answer:
{"entities": [{"text": "cardiovascular", "type": "SpatialConcept"}]}

Example input:
Sentence: Despite advances in the regulation and incorporation of technologies by the SUS , given the lack of market interest and neglect of diseases of poverty , the government has a vital role to play in ensuring access to the best available therapies in order to reduce health inequalities .

Example answer:
{"entities": [{"text": "technologies", "type": "HealthCareActivity"}, {"text": "SUS", "type": "Organization"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "government", "type": "Organization"}, {"text": "therapies", "type": "HealthCareActivity"}]}

Example input:
Sentence: While we need more good data on the nature and magnitude of these possible harms , few would argue with the proposition that sustained science hype is a bad thing .

Example answer:
{"entities": [{"text": "proposition", "type": "IntellectualProduct"}]}

Example input:
Sentence: In contrast , the scientific experts and policymakers see risks and social and ethical issues as manageable and quantifiable with more research and knowledge .

Example answer:
{"entities": [{"text": "experts", "type": "ProfessionalOrOccupationalGroup"}, {"text": "policymakers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "manageable", "type": "Finding"}, {"text": "research", "type": "ResearchActivity"}, {"text": "knowledge", "type": "IntellectualProduct"}]}

Example input:
Sentence: Ethics Hype ? There has been growing concern about the phenomenon of science hype , the tendency to exaggerate the value or near - future application of research results .

Example answer:
{"entities": []}

Example input:
Sentence: We find that while the public is broadly supportive of new scientific developments , they see the risks and social and ethical issues associated with them as unpredictable but inherent parts of the developments .

Example answer:
{"entities": [{"text": "public", "type": "Organization"}, {"text": "broadly", "type": "SpatialConcept"}, {"text": "unpredictable", "type": "Finding"}, {"text": "inherent", "type": "SpatialConcept"}, {"text": "parts", "type": "SpatialConcept"}]}

Input:
Sentence: We all benefit from robust science and accurate public representations of biomedical research . But , to date , there has been very little consideration of the degree to which the scholarship on the related ethical , legal , and social issues has been hyped . Are the conclusions from ELSI scholarship also exaggerated ?

## Item MedMentions:test:1782
Example input:
Sentence: The study population consisted of 276 Brown Swiss and Pirenaica adult animals and 145 calves born and weaned at the farm during the study .

Example answer:
{"entities": [{"text": "study population", "type": "ResearchActivity"}, {"text": "Brown Swiss", "type": "Eukaryote"}, {"text": "Pirenaica", "type": "Eukaryote"}, {"text": "calves", "type": "Eukaryote"}, {"text": "born", "type": "BiologicFunction"}, {"text": "weaned", "type": "Finding"}, {"text": "farm", "type": "SpatialConcept"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Repeated udder health scores , site - specific tick count , mating weight and reproduction records ( N = 879 - 1204 ) were recorded annually from 2010 to 2015 on ewes of the indigenous Namaqua Afrikaner (  ) fat - tailed breed , as well as the commercial Dorper and SA Mutton Merino ( SAMM ) breeds .

Example answer:
{"entities": [{"text": "udder", "type": "AnatomicalStructure"}, {"text": "site - specific", "type": "SpatialConcept"}, {"text": "mating", "type": "BiologicFunction"}, {"text": "reproduction", "type": "BiologicFunction"}, {"text": "records", "type": "IntellectualProduct"}, {"text": "Namaqua Afrikaner", "type": "Eukaryote"}, {"text": "", "type": "Eukaryote"}, {"text": "fat - tailed breed", "type": "IntellectualProduct"}, {"text": "commercial", "type": "IntellectualProduct"}, {"text": "Dorper", "type": "Eukaryote"}, {"text": "SA Mutton Merino ( SAMM ) breeds", "type": "Eukaryote"}]}

Example input:
Sentence: We also highlighted how rs860170 ( TAS2R16 ) strongly differentiated populations and was associated to salicin bitterness perception .

Example answer:
{"entities": [{"text": "rs860170 ( TAS2R16 )", "type": "AnatomicalStructure"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "salicin", "type": "Chemical"}, {"text": "bitterness perception", "type": "BiologicFunction"}]}

Example input:
Sentence: Next - generation sequencing of llama , alpaca and dromedary VHH repertoires suggested that species differences in SpA binding may result from frequency variation in specific deleterious polymorphisms , especially Ile57 .

Example answer:
{"entities": [{"text": "Next - generation sequencing", "type": "ResearchActivity"}, {"text": "llama", "type": "Eukaryote"}, {"text": "alpaca", "type": "Eukaryote"}, {"text": "dromedary", "type": "Eukaryote"}, {"text": "VHH repertoires", "type": "Chemical"}, {"text": "SpA", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "polymorphisms", "type": "BiologicFunction"}]}

Example input:
Sentence: Agronomic performance , resistance to SCMV infection , and transgene stability were evaluated and compared with the wild - type parental clone Badila ( WT ) at four experimental locations in China across two successive seasons , i .

Example answer:
{"entities": [{"text": "resistance", "type": "BiologicFunction"}, {"text": "SCMV", "type": "Virus"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "transgene", "type": "AnatomicalStructure"}, {"text": "wild - type", "type": "AnatomicalStructure"}, {"text": "parental clone", "type": "AnatomicalStructure"}, {"text": "Badila", "type": "Eukaryote"}, {"text": "WT", "type": "AnatomicalStructure"}, {"text": "experimental locations", "type": "SpatialConcept"}, {"text": "China", "type": "SpatialConcept"}]}

Example input:
Sentence: Here , we study the population genetic diversity , structure , and stability of a classic " island giant " ( Xantusia riversiana , the Island Night Lizard ) on San Clemente Island , California following the removal of feral goats .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "population", "type": "PopulationGroup"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "island giant", "type": "Eukaryote"}, {"text": "Xantusia riversiana", "type": "Eukaryote"}, {"text": "Island Night Lizard", "type": "Eukaryote"}, {"text": "San Clemente Island", "type": "SpatialConcept"}, {"text": "California", "type": "SpatialConcept"}, {"text": "feral goats", "type": "Eukaryote"}]}

Example input:
Sentence: An eclectic set of tissues and existing data , including purposely collected samples , spanning 1997 - 2006 , was used in an ad hoc assessment of hybridization and introgression of farmed wild Atlantic salmon Salmo salar in the small Loch na Thull ( LnT ) catchment in north - west Scotland .

Example answer:
{"entities": [{"text": "tissues", "type": "AnatomicalStructure"}, {"text": "ad hoc assessment", "type": "ResearchActivity"}, {"text": "hybridization", "type": "BiologicFunction"}, {"text": "farmed wild Atlantic salmon Salmo salar", "type": "Eukaryote"}, {"text": "north - west Scotland", "type": "SpatialConcept"}]}

Example input:
Sentence: Assessment of interbreeding and introgression of farm genes into a small Scottish Atlantic salmon Salmo salar stock : ad hoc samples - ad hoc results ?

Example answer:
{"entities": [{"text": "Assessment", "type": "ResearchActivity"}, {"text": "interbreeding", "type": "BiologicFunction"}, {"text": "farm", "type": "SpatialConcept"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "Scottish Atlantic salmon Salmo salar", "type": "Eukaryote"}]}

Example input:
Sentence: salar , there was no evidence of physical or genetic mixing .

Example answer:
{"entities": [{"text": "salar", "type": "Eukaryote"}]}

Example input:
Sentence: salar stock was found to be genetically distinctive from stocks in neighbouring rivers and , despite regular reports of feral farm S .

Example answer:
{"entities": [{"text": "salar", "type": "Eukaryote"}, {"text": "neighbouring", "type": "SpatialConcept"}, {"text": "feral farm", "type": "SpatialConcept"}, {"text": "S .", "type": "Eukaryote"}]}

Input:
Sentence: salar population little affected by interbreeding with feral farm escapes .

## Item MedMentions:test:2117
Example input:
Sentence: 01 - 1 . 29 , p = 0 . 04 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 2 ; P = 0 . 03 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 06 - 1 . 49 , P = 0 . 007 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 001 and P = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 001 , and p < 0 . 001 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 05 , p = 0 . 076 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 007 , and p = 0 . 04 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 02 ( SE = - 0 . 02 ) ; P = 0 . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 05 , and p > 0 . 05 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 05 and OR 0 . 46 , P = 0 . 01 , respectively ) .

Example answer:
{"entities": []}

Input:
Sentence: 04 ; P = .02 ) .

## Item MedMentions:test:1943
Example input:
Sentence: We compared clinicopathological features ; preoperative calcium , parathyroid hormone ( PTH ) , phosphorus , vitamin D , 24 - hour urine calcium , and alkaline phosphatase levels ; postoperative calcium and PTH levels ; pathologic diagnosis ; multiplicity ; and results of a localization study between the 2 groups .

Example answer:
{"entities": [{"text": "clinicopathological", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "calcium", "type": "HealthCareActivity"}, {"text": "parathyroid hormone", "type": "HealthCareActivity"}, {"text": "PTH", "type": "HealthCareActivity"}, {"text": "phosphorus", "type": "HealthCareActivity"}, {"text": "vitamin D", "type": "HealthCareActivity"}, {"text": "24 - hour urine calcium", "type": "HealthCareActivity"}, {"text": "alkaline phosphatase levels", "type": "Finding"}, {"text": "PTH levels", "type": "HealthCareActivity"}, {"text": "localization study", "type": "ResearchActivity"}]}

Example input:
Sentence: Patients were further divided into high - risk ( grade 3 , non - endometrioid , myometrial invasion ≥1 / 2 and stage III - IV ) and high - intermediate - risk ( grade 2 - 3 , endometrioid , myometrial invasion < 1 / 2 and stage I - II ) groups according to postoperative pathological results .

Example answer:
{"entities": [{"text": "high - risk", "type": "Finding"}, {"text": "grade 3 , non - endometrioid , myometrial invasion ≥1 / 2", "type": "ClinicalAttribute"}, {"text": "stage III - IV", "type": "ClinicalAttribute"}, {"text": "high - intermediate - risk", "type": "Finding"}, {"text": "( grade 2 - 3 , endometrioid , myometrial invasion < 1 / 2", "type": "ClinicalAttribute"}, {"text": "stage I - II", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The following parameters were analysed during the early post - operative period : ( 1 ) The intensity of surgical trauma , operation time , C - reactive protein ( CRP ) levels , white blood cell count , bleeding and pain intensity ; ( 2 ) quality of life assessment ; and ( 3 ) post - operative complications .

Example answer:
{"entities": [{"text": "analysed", "type": "ResearchActivity"}, {"text": "C - reactive protein", "type": "Chemical"}, {"text": "CRP", "type": "Chemical"}, {"text": "white blood cell count", "type": "HealthCareActivity"}, {"text": "bleeding", "type": "BiologicFunction"}, {"text": "pain intensity", "type": "ClinicalAttribute"}, {"text": "assessment", "type": "HealthCareActivity"}, {"text": "post - operative complications", "type": "BiologicFunction"}]}

Example input:
Sentence: The combination was associated with reduced intraoperative ( 44 . 6 % versus 34 .

Example answer:
{"entities": []}

Example input:
Sentence: No group differences were found for intraoperative blood loss , hospitalization times , positive surgical margins , biochemical recurrence , sexual dysfunction or need for adjuvant therapy .

Example answer:
{"entities": [{"text": "blood loss", "type": "Finding"}, {"text": "hospitalization", "type": "HealthCareActivity"}, {"text": "positive surgical margins", "type": "Finding"}, {"text": "sexual dysfunction", "type": "BiologicFunction"}, {"text": "adjuvant therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Although metal ion levels alone should not be relied on as the sole parameter to determine revision surgery , cobalt level > 2 . 8 μg / L and the Co / Cr ratio > 3 .

Example answer:
{"entities": [{"text": "metal ion", "type": "Chemical"}, {"text": "revision surgery", "type": "HealthCareActivity"}, {"text": "cobalt", "type": "Chemical"}, {"text": "Co", "type": "Chemical"}, {"text": "Cr", "type": "Chemical"}]}

Example input:
Sentence: Also , postoperatively , NGAL , creatinine , aspartate aminotransferase and AOPP levels were higher in group I than group II ( p < 0 .

Example answer:
{"entities": [{"text": "NGAL", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "aspartate aminotransferase", "type": "Chemical"}, {"text": "AOPP", "type": "Chemical"}]}

Example input:
Sentence: In group I , T - SH , NGAL and urea levels were found to be significantly increased postoperatively compared to preoperative measurements ( p < 0 .

Example answer:
{"entities": [{"text": "T - SH", "type": "Chemical"}, {"text": "NGAL", "type": "Chemical"}, {"text": "urea levels", "type": "Finding"}]}

Example input:
Sentence: Sensitivity and Specificity of Metal Ion Levels in Predicting " Pseudotumors " due to Taper Corrosion in Patients With Dual Taper Modular Total Hip Arthroplasty Currently , no serum metal ion threshold exists to identify adverse tissue reactions in total hip arthroplasty ( THA ) patients with taper corrosion .

Example answer:
{"entities": [{"text": "Metal Ion", "type": "Chemical"}, {"text": "Pseudotumors", "type": "AnatomicalStructure"}, {"text": "Taper", "type": "MedicalDevice"}, {"text": "Dual Taper Modular", "type": "MedicalDevice"}, {"text": "Total Hip Arthroplasty", "type": "HealthCareActivity"}, {"text": "serum", "type": "BodySubstance"}, {"text": "metal ion", "type": "Chemical"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "total hip arthroplasty", "type": "HealthCareActivity"}, {"text": "THA", "type": "HealthCareActivity"}, {"text": "taper", "type": "MedicalDevice"}]}

Example input:
Sentence: Higher intraoperative tissue damage grades demonstrated significantly higher Co / Cr ratios ( 8 . 6 vs 3 .

Example answer:
{"entities": [{"text": "tissue damage", "type": "InjuryOrPoisoning"}, {"text": "Co", "type": "Chemical"}, {"text": "Cr", "type": "Chemical"}]}

Input:
Sentence: The severity of intraoperative tissue damage was correlated with preoperative metal ion levels .

## Item MedMentions:test:1912
Example input:
Sentence: During 2015 , we conducted qualitative interviews with 35 participants recruited using snowball sampling based on previous research and social networks .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "snowball sampling", "type": "ResearchActivity"}, {"text": "research", "type": "ResearchActivity"}, {"text": "social networks", "type": "PopulationGroup"}]}

Example input:
Sentence: Twenty able - bodied participants were recruited for the study .

Example answer:
{"entities": [{"text": "able - bodied", "type": "Finding"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: This study was a retrospective cohort study of women delivering at a university hospital in 2009 - 2010 who received prenatal care in the faculty and resident clinics .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "retrospective cohort study", "type": "ResearchActivity"}, {"text": "women", "type": "PopulationGroup"}, {"text": "delivering", "type": "BiologicFunction"}, {"text": "university hospital", "type": "Organization"}, {"text": "prenatal care", "type": "HealthCareActivity"}, {"text": "faculty", "type": "ProfessionalOrOccupationalGroup"}, {"text": "resident clinics", "type": "Organization"}]}

Example input:
Sentence: At 19 years , 590 / 998 ( 59 % ) of the subjects enrolled in 1983 were followed up .

Example answer:
{"entities": [{"text": "subjects", "type": "PopulationGroup"}, {"text": "followed up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Participants were recruited from Magee - Womens Hospital .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "Magee - Womens Hospital", "type": "Organization"}]}

Example input:
Sentence: Twenty six participants ( 13 young aged 18 - 30 ; 13 old aged 70 - 80 ) were recruited .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "old aged", "type": "PopulationGroup"}]}

Example input:
Sentence: The vast majority of service providers ( 93 . 4 % ) reported that ENGAGE had impacted their work practice up to 5 - month post training .

Example answer:
{"entities": [{"text": "reported", "type": "HealthCareActivity"}, {"text": "ENGAGE", "type": "Organization"}]}

Example input:
Sentence: The association patterns were similar , when we restricted to participants who delivered by emergency cesarean ( 1 . 4 , 1 . 1 , 1 . 9 ) , or who delivered after 35 weeks of gestation ( 1 . 4 , 1 .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "delivered", "type": "HealthCareActivity"}, {"text": "emergency cesarean", "type": "HealthCareActivity"}]}

Example input:
Sentence: One hundred ( 100 ) patients were consecutively recruited : 60 women ( mean age 41 ± 14 years ) and 40 men ( mean age 46 ± 13 years ) .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: Participants were recruited at a university - based practice between June 14 , 2014 , and December 28 , 2015 .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "university", "type": "Organization"}, {"text": "practice", "type": "BiomedicalOccupationOrDiscipline"}]}

Input:
Sentence: Participants were recruited during 2005 - 2008 and followed up until delivery .

## Item MedMentions:test:1698
Example input:
Sentence: The combined results of univariate and multivariate Cox regression analysis showed that the SNP in ERCC1 - 118 was closely associated with survival time .

Example answer:
{"entities": [{"text": "multivariate Cox regression analysis", "type": "IntellectualProduct"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "ERCC1 - 118", "type": "AnatomicalStructure"}, {"text": "survival time", "type": "ClinicalAttribute"}]}

Example input:
Sentence: 8 % of the patients were classified as triple - negative breast cancer ( estrogen - recetor / progesteron - receptor - negative ) .

Example answer:
{"entities": [{"text": "triple - negative breast cancer", "type": "BiologicFunction"}, {"text": "estrogen - recetor / progesteron - receptor - negative", "type": "BiologicFunction"}]}

Example input:
Sentence: There were statistically significant differences between different IHC intrinsic subtypes regarding tumor size ( p = 0 . 001 ) , estrogen receptor ( ER ) status ( p = 0 . 001 ) , progesterone receptor ( PR ) status ( p = 0 . 001 ) , HER2 status ( p = 0 . 001 ) and Ki67 proliferation index ( p = 0 . 001 ) .

Example answer:
{"entities": [{"text": "IHC", "type": "HealthCareActivity"}, {"text": "tumor size", "type": "SpatialConcept"}, {"text": "estrogen receptor ( ER ) status", "type": "ClinicalAttribute"}, {"text": "progesterone receptor ( PR ) status", "type": "ClinicalAttribute"}, {"text": "HER2 status", "type": "ClinicalAttribute"}, {"text": "Ki67", "type": "Chemical"}]}

Example input:
Sentence: Multivariable analysis revealed that female [ hazard ratio ( HR ) = 0 . 78 ] , adenocarcinoma ( HR = 0 . 77 ) , locoregional ( only ) recurrence ( HR = 0 . 59 ) and longer recurrence -free survival ( HR = 0 . 99 ) were favourably associated with PRS .

Example answer:
{"entities": [{"text": "adenocarcinoma", "type": "BiologicFunction"}, {"text": "locoregional ( only ) recurrence", "type": "BiologicFunction"}, {"text": "longer recurrence -free survival", "type": "Finding"}]}

Example input:
Sentence: On univariate analysis , variables associated with worse survival included : clinical stage IIIB ( p = 0 . 037 ) , planning target volume ( PTV ) over 450 cc ( p < 0 . 001 ) , heart V30 over 40 % ( p = -0 . 048 ) , and esophageal mean dose over 20 % ( p = 0 . 024 ) , V5 ( p = -0 . 015 ) , and V60 ( p = -0 . 011 ) .

Example answer:
{"entities": [{"text": "worse", "type": "Finding"}, {"text": "stage IIIB", "type": "BiologicFunction"}, {"text": "heart", "type": "AnatomicalStructure"}, {"text": "esophageal", "type": "SpatialConcept"}]}

Example input:
Sentence: For triple negative or HER2 / neu positive disease the sensitivity and specificity were 88 % ( 95 % CI , 62 - 98 ) and 75 % ( 95 % CI , 43 - 93 ) , respectively .

Example answer:
{"entities": [{"text": "triple negative", "type": "BiologicFunction"}, {"text": "HER2 / neu positive", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Chemotherapy response and survival of inflammatory breast cancer by hormone receptor - and HER2 -defined molecular subtypes approximation : an analysis from the National Cancer Database To study the impact of hormone receptor ( HR ) - and human epidermal growth factor receptor 2 ( HER2 ) - defined subtypes on survival of inflammatory breast cancer ( IBC ) , and to determine whether sensitivity to neoadjuvant chemotherapy ( NAC ) varies with subtypes in a large IBC population .

Example answer:
{"entities": [{"text": "Chemotherapy", "type": "HealthCareActivity"}, {"text": "inflammatory breast cancer", "type": "BiologicFunction"}, {"text": "hormone receptor", "type": "Chemical"}, {"text": "HER2", "type": "Chemical"}, {"text": "subtypes", "type": "IntellectualProduct"}, {"text": "approximation", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "National Cancer Database", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "HR", "type": "Chemical"}, {"text": "human epidermal growth factor receptor 2", "type": "Chemical"}, {"text": "IBC", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: Simultaneously , the results showed that male patients in the HoR - positive / HER2 - negative subgroup were less likely to die of BC when adjusting for other factors ( p < 0 .

Example answer:
{"entities": [{"text": "HoR - positive / HER2 - negative subgroup", "type": "IntellectualProduct"}, {"text": "to die", "type": "Finding"}, {"text": "BC", "type": "BiologicFunction"}]}

Example input:
Sentence: This correlation was stronger for triple negative and HER2 / neu positive subtypes ( r = 0 . 92 and 0 . 62 , respectively ) .

Example answer:
{"entities": [{"text": "triple negative", "type": "BiologicFunction"}, {"text": "HER2 / neu positive", "type": "ClinicalAttribute"}, {"text": "subtypes", "type": "IntellectualProduct"}]}

Example input:
Sentence: Triple - negative and HR + / HER2 - subtypes are independent predictors for suboptimal OS in IBC .

Example answer:
{"entities": [{"text": "Triple - negative", "type": "BiologicFunction"}, {"text": "HR + / HER2 -", "type": "Finding"}, {"text": "subtypes", "type": "IntellectualProduct"}, {"text": "predictors", "type": "Finding"}, {"text": "IBC", "type": "BiologicFunction"}]}

Input:
Sentence: Multivariate analysis showed that triple - negative and HR + / HER2 - IBCs had significantly worse survival compared with HR + / HER2 + or HR - / HER2 + subtype ( P < 0 .

## Item MedMentions:test:2155
Example input:
Sentence: The GM for field half - lives was 72 d .

Example answer:
{"entities": []}

Example input:
Sentence: When an IV dose of 100 mg / kg was given to mice , the blood circulation half - life was measured to be about 4 h , and more than 90 % of the NPs were cleared from the mice within 24 h via the renal and hepatobiliary systems .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}, {"text": "blood circulation", "type": "BiologicFunction"}, {"text": "renal", "type": "AnatomicalStructure"}, {"text": "hepatobiliary systems", "type": "BodySystem"}]}

Example input:
Sentence: Thermal inactivation and thermal denaturation analysis revealed that Glu138Pro mutation increased half - life and Tm of enzyme , respectively .

Example answer:
{"entities": [{"text": "denaturation", "type": "BiologicFunction"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "Glu138Pro", "type": "SpatialConcept"}, {"text": "mutation", "type": "BiologicFunction"}, {"text": "enzyme", "type": "Chemical"}]}

Example input:
Sentence: In addition , SUA and SUAPG were mainly excreted in the time period of 12 - 24 h , while GA was excreted in the earlier time periods ( 0 - 4 h and 4 - 8 h ) .

Example answer:
{"entities": [{"text": "SUA", "type": "Chemical"}, {"text": "SUAPG", "type": "Chemical"}, {"text": "excreted", "type": "BiologicFunction"}, {"text": "GA", "type": "Chemical"}]}

Example input:
Sentence: SA was mainly excreted in the time period of 0 - 4 h and 12 - 24 h .

Example answer:
{"entities": [{"text": "SA", "type": "Chemical"}, {"text": "excreted", "type": "BiologicFunction"}]}

Example input:
Sentence: A half - life of 280 min was measured for the polymeric donor .

Example answer:
{"entities": [{"text": "polymeric", "type": "Chemical"}]}

Example input:
Sentence: Pendimethalin has a geometric mean ( GM ) half - life of 76 - 98 d in agriculturally relevant soils under aerobic conditions in the lab .

Example answer:
{"entities": [{"text": "Pendimethalin", "type": "Chemical"}, {"text": "lab", "type": "Organization"}]}

Example input:
Sentence: h ml ( - 1 ) , half - life ( t½ ) 4 .

Example answer:
{"entities": []}

Example input:
Sentence: The GM half - life for sediment - water tests in the lab was 20 d and that in field aquatic cosms ranged from 45 to 90 d .

Example answer:
{"entities": [{"text": "lab", "type": "Organization"}, {"text": "aquatic", "type": "SpatialConcept"}]}

Example input:
Sentence: 3 kPa , but only used within the first hour at 1 . 3 and 0 . 67 kPa , as anaerobic end - products did not accumulate between 1 and 4 h exposure .

Example answer:
{"entities": [{"text": "within", "type": "SpatialConcept"}]}

Input:
Sentence: The anaerobic half - life was 12 d .

## Item MedMentions:test:1460
Example input:
Sentence: AS patients showed an increased ( P < 0 . 001 ) cardiomyocyte apoptotic index ( CMAI ) compared with controls .

Example answer:
{"entities": [{"text": "AS", "type": "BiologicFunction"}]}

Example input:
Sentence: Simultaneous assessments were made of left ventricular ( LV ) mass index and hypertrophy and measures of LV systolic and diastolic dysfunction .

Example answer:
{"entities": [{"text": "assessments", "type": "HealthCareActivity"}, {"text": "hypertrophy", "type": "BiologicFunction"}, {"text": "LV systolic", "type": "BiologicFunction"}, {"text": "diastolic dysfunction", "type": "BiologicFunction"}]}

Example input:
Sentence: The ICC and r were highest ( ≥0 . 80 ) for 25 ( OH ) D , free 25 ( OH ) D , bioavailable 25 ( OH ) D and PTH , but somewhat lower ( approximately 0 . 60 - 0 . 75 ) for the other biomarkers .

Example answer:
{"entities": [{"text": "25 ( OH ) D", "type": "Chemical"}, {"text": "PTH", "type": "Chemical"}, {"text": "biomarkers", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Inflammation was quantified with standardized uptake value and regional myocardial blood flow at rest and during regadenoson - stimulated hyperemia was determined in ml / g / min .

Example answer:
{"entities": [{"text": "Inflammation", "type": "BiologicFunction"}, {"text": "myocardial blood flow", "type": "BiologicFunction"}, {"text": "regadenoson", "type": "Chemical"}, {"text": "hyperemia", "type": "BiologicFunction"}]}

Example input:
Sentence: Histopathological studies showed higher inflammatory cell infiltrates , cardiac fibrosis , and collagen deposition in LPS group , which were reduced by the administration of NS .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "inflammatory cell infiltrates", "type": "BodySubstance"}, {"text": "cardiac fibrosis", "type": "BiologicFunction"}, {"text": "collagen", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "NS", "type": "Eukaryote"}]}

Example input:
Sentence: Results When compared with control subjects , patients had higher ventricular volume , higher myocardial native T1 and T2 , and lower longitudinal strain and ejection fraction ( P < .05 for all ) .

Example answer:
{"entities": [{"text": "myocardial", "type": "SpatialConcept"}, {"text": "longitudinal strain", "type": "Finding"}, {"text": "ejection fraction", "type": "Finding"}]}

Example input:
Sentence: Thirty - two patients with confirmed chronic myocardial inflammation by EMB served as study group ( MCpEF ) and the remaining patients ( n = 35 ) served as control group .

Example answer:
{"entities": [{"text": "chronic myocardial inflammation", "type": "BiologicFunction"}, {"text": "EMB", "type": "HealthCareActivity"}, {"text": "MCpEF", "type": "BiologicFunction"}, {"text": "control group", "type": "PopulationGroup"}]}

Example input:
Sentence: By univariate analysis , blood pressure ( BP ) , heart rate , National Institutes of Health Stroke Scale ( NIHSS ) score , number of diffusion - positive lesion , count of red blood cell , high - density lipoprotein , and degree of stenosis differed significantly between the 2 groups .

Example answer:
{"entities": [{"text": "blood pressure", "type": "BiologicFunction"}, {"text": "BP", "type": "BiologicFunction"}, {"text": "heart rate", "type": "ClinicalAttribute"}, {"text": "National Institutes of Health Stroke Scale ( NIHSS ) score", "type": "Finding"}, {"text": "positive", "type": "Finding"}, {"text": "lesion", "type": "Finding"}, {"text": "count of red blood cell", "type": "HealthCareActivity"}, {"text": "high - density lipoprotein", "type": "Chemical"}]}

Example input:
Sentence: There was an inverse correlation between pronounced alterations in myocardial inflammation ( Δ regional myocardial volume with standardized uptake value > 4 . 1 ) and Δ MFR ( r = -0 . 47 ; p = 0 . 048 ) .

Example answer:
{"entities": [{"text": "myocardial inflammation", "type": "BiologicFunction"}, {"text": "MFR", "type": "ClinicalAttribute"}]}

Example input:
Sentence: These results reinforce the advantages of a multimarker strategy in elucidating the underlying cause of cardiac insult and detecting myocardial tissue damage at 24 - hr posttreatment .

Example answer:
{"entities": [{"text": "cardiac insult", "type": "BiologicFunction"}, {"text": "detecting", "type": "Finding"}, {"text": "myocardial", "type": "AnatomicalStructure"}, {"text": "tissue damage", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: This study reports the evaluation of several commercially available biomarker kits by 3 institutions ( SRI , Eli Lilly , and Pfizer ) for the discrimination between myocardial degeneration / necrosis and cardiac hypertrophy as well as the assessment of the interlaboratory and interplatform variation in results .

## Item MedMentions:test:1804
Example input:
Sentence: No exclusion criteria were stated .

Example answer:
{"entities": []}

Example input:
Sentence: The two groups were not different with respect to maternal demographics and gestational age at cerclage .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: Patients were excluded if they had previously undergone B - KPro implantation .

Example answer:
{"entities": [{"text": "B - KPro", "type": "MedicalDevice"}, {"text": "implantation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Inclusion and exclusion criteria concentrated on patient -specific surgical applications , yielding 141 full - text articles , of which 33 craniomaxillofacial articles were analyzed .

Example answer:
{"entities": [{"text": "surgical", "type": "HealthCareActivity"}, {"text": "articles", "type": "IntellectualProduct"}, {"text": "craniomaxillofacial articles", "type": "IntellectualProduct"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: Maternal demographics , gestational age at cerclage , gestational age at delivery , preterm prelabor rupture of membranes ( PROM ) , and birth weight were compared between women with a cerclage and cerclage plus 17α - hydroxyprogesterone caproate .

Example answer:
{"entities": [{"text": "delivery", "type": "BiologicFunction"}, {"text": "preterm prelabor rupture of membranes", "type": "BiologicFunction"}, {"text": "PROM", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "17α - hydroxyprogesterone caproate", "type": "Chemical"}]}

Example input:
Sentence: Main exclusion criteria were established kidney disease , cardiovascular diseases , diabetes mellitus and a body mass index > 35 kg / m2 .

Example answer:
{"entities": [{"text": "kidney disease", "type": "BiologicFunction"}, {"text": "cardiovascular diseases", "type": "BiologicFunction"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "body mass index", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Patients are excluded if pain is attributable to abdominal causes or if any contraindications for either type of anaesthesia are present .

Example answer:
{"entities": [{"text": "pain", "type": "Finding"}, {"text": "abdominal causes", "type": "Finding"}, {"text": "contraindications", "type": "Finding"}, {"text": "type of anaesthesia", "type": "IntellectualProduct"}, {"text": "present", "type": "Finding"}]}

Example input:
Sentence: Exclusion criteria were extra - pulmonary TB , age < 15 years and pregnancy .

Example answer:
{"entities": [{"text": "extra - pulmonary TB", "type": "BiologicFunction"}, {"text": "pregnancy", "type": "BiologicFunction"}]}

Example input:
Sentence: In order to ensure that the individuals were not affected by unknown syndromes or diseases , we excluded all individuals with any chronic medical condition , or who had other birth defects than clefts , hydroceles and dislocated hips .

Example answer:
{"entities": [{"text": "individuals", "type": "PopulationGroup"}, {"text": "syndromes", "type": "BiologicFunction"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "birth defects", "type": "AnatomicalStructure"}, {"text": "clefts", "type": "AnatomicalStructure"}, {"text": "hydroceles", "type": "AnatomicalStructure"}, {"text": "dislocated hips", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Exclusion criteria were ruptured AVMs that required emergent surgery involving AVM resection , previous treatment at another institution , or subacute AVM treatment .

Example answer:
{"entities": [{"text": "ruptured", "type": "InjuryOrPoisoning"}, {"text": "AVMs", "type": "BiologicFunction"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "AVM", "type": "BiologicFunction"}, {"text": "resection", "type": "HealthCareActivity"}, {"text": "institution", "type": "Organization"}]}

Input:
Sentence: Exclusion criteria were delivery at another institution , abdominal cerclage , multiple gestations , and major fetal anomalies .

## Item MedMentions:test:1922
Example input:
Sentence: Epicardial highest dominant frequency ( HDF ) regions and rotor location were compared with the same inverse - computed measurements after addition of noise to the ECG , size variations of the atria , and linear or angular deviations in the atrial location inside the thorax .

Example answer:
{"entities": [{"text": "Epicardial", "type": "SpatialConcept"}, {"text": "regions", "type": "SpatialConcept"}, {"text": "rotor location", "type": "SpatialConcept"}, {"text": "ECG", "type": "HealthCareActivity"}, {"text": "atria", "type": "AnatomicalStructure"}, {"text": "linear", "type": "SpatialConcept"}, {"text": "angular", "type": "SpatialConcept"}, {"text": "deviations", "type": "SpatialConcept"}, {"text": "atrial location", "type": "AnatomicalStructure"}, {"text": "thorax", "type": "SpatialConcept"}]}

Example input:
Sentence: Peripheral Hcy could be considered as a potential biomarker in BD , both of trait ( since it is increased in euthymia ) , and also of state ( since its increase is more accentuated in mania ) .

Example answer:
{"entities": [{"text": "Peripheral", "type": "SpatialConcept"}, {"text": "Hcy", "type": "Chemical"}, {"text": "biomarker", "type": "ClinicalAttribute"}, {"text": "BD", "type": "BiologicFunction"}, {"text": "euthymia", "type": "BiologicFunction"}, {"text": "mania", "type": "BiologicFunction"}]}

Example input:
Sentence: In contrast , activation in the right precentral gyrus showed a significantly stronger correlation with HLE in FHD + compared to FHD - children , suggesting emerging compensatory networks in genetically at - risk children .

Example answer:
{"entities": [{"text": "right precentral gyrus", "type": "AnatomicalStructure"}, {"text": "HLE", "type": "SpatialConcept"}, {"text": "FHD +", "type": "Finding"}, {"text": "FHD -", "type": "Finding"}]}

Example input:
Sentence: Diffusion - weighted magnetic resonance imaging disclosed multiple cortical hyperintensities , which were preferentially located in the frontal lobes .

Example answer:
{"entities": [{"text": "Diffusion - weighted magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "cortical hyperintensities", "type": "Finding"}, {"text": "frontal lobes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Thus , identification of FLAIR change may be a useful surrogate marker to assess the likelihood of subsequent HT in patients treated with reperfusion therapy .

Example answer:
{"entities": [{"text": "FLAIR", "type": "HealthCareActivity"}, {"text": "HT", "type": "BiologicFunction"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "reperfusion therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: FLAIR change was independently associated with HT ( odds ratio : 4 .

Example answer:
{"entities": [{"text": "FLAIR", "type": "HealthCareActivity"}, {"text": "HT", "type": "BiologicFunction"}]}

Example input:
Sentence: In patients in the acute stage of stroke , an early FLAIR change is associated with the risk of HT following reperfusion therapy with a highly matched geographic relationship and common risk factors .

Example answer:
{"entities": [{"text": "stroke", "type": "BiologicFunction"}, {"text": "FLAIR", "type": "HealthCareActivity"}, {"text": "HT", "type": "BiologicFunction"}, {"text": "reperfusion therapy", "type": "HealthCareActivity"}, {"text": "risk factors", "type": "Finding"}]}

Example input:
Sentence: The location of the FLAIR change and HT was classified as subcortical , cortical , or cortico - subcortical .

Example answer:
{"entities": [{"text": "FLAIR", "type": "HealthCareActivity"}, {"text": "HT", "type": "BiologicFunction"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "cortico - subcortical", "type": "SpatialConcept"}]}

Example input:
Sentence: Fluid - Attenuated Inversion Recovery Hyperintensity Is Associated with Hemorrhagic Transformation following Reperfusion Therapy It is still controversial whether early fluid - attenuated inversion recovery ( FLAIR ) hyperintensity within acute ischemic lesions carries the risk of hemorrhagic transformation ( HT ) after reperfusion therapy .

Example answer:
{"entities": [{"text": "Fluid - Attenuated Inversion Recovery", "type": "HealthCareActivity"}, {"text": "Hyperintensity", "type": "BiologicFunction"}, {"text": "Hemorrhagic Transformation", "type": "BiologicFunction"}, {"text": "Reperfusion Therapy", "type": "HealthCareActivity"}, {"text": "fluid - attenuated inversion recovery", "type": "HealthCareActivity"}, {"text": "FLAIR", "type": "HealthCareActivity"}, {"text": "hyperintensity", "type": "BiologicFunction"}, {"text": "ischemic", "type": "BiologicFunction"}, {"text": "lesions", "type": "Finding"}, {"text": "hemorrhagic transformation", "type": "BiologicFunction"}, {"text": "HT", "type": "BiologicFunction"}, {"text": "reperfusion therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: FLAIR hyperintensity within the diffusion - weighted imaging ( DWI ) lesion was rated qualitatively , and HT was assessed on follow - up gradient echo imaging .

Example answer:
{"entities": [{"text": "FLAIR", "type": "HealthCareActivity"}, {"text": "hyperintensity", "type": "BiologicFunction"}, {"text": "diffusion - weighted imaging", "type": "HealthCareActivity"}, {"text": "DWI", "type": "HealthCareActivity"}, {"text": "lesion", "type": "Finding"}, {"text": "HT", "type": "BiologicFunction"}, {"text": "echo imaging", "type": "HealthCareActivity"}]}

Input:
Sentence: Furthermore , the association between the location of FLAIR hyperintensity and HT has not been investigated .

## Item MedMentions:test:1905
Example input:
Sentence: The present study investigated the effect of exercise , exercise withdrawal , and continued regular exercise on excitability and long - term potentiation in the dentate gyrus ( DG ) of hippocampus .

Example answer:
{"entities": [{"text": "present", "type": "Finding"}, {"text": "study", "type": "ResearchActivity"}, {"text": "excitability", "type": "Finding"}, {"text": "long - term potentiation", "type": "BiologicFunction"}, {"text": "dentate gyrus", "type": "AnatomicalStructure"}, {"text": "DG", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Notably , animals that were behaviorally the worst affected at the end of chronic stress suffered the most pronounced early loss in hippocampal volume .

Example answer:
{"entities": [{"text": "animals", "type": "Eukaryote"}, {"text": "suffered", "type": "BiologicFunction"}, {"text": "early loss in hippocampal volume", "type": "Finding"}]}

Example input:
Sentence: The hippocampus is a structure involved in exercise , which can improve synaptic plasticity and long - term potentiation ( LTP ) .

Example answer:
{"entities": [{"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "improve", "type": "Finding"}, {"text": "synaptic plasticity", "type": "BiologicFunction"}, {"text": "long - term potentiation", "type": "BiologicFunction"}, {"text": "LTP", "type": "BiologicFunction"}]}

Example input:
Sentence: Given the proposed role of this form of structural plasticity in the functioning of the hippocampus ( namely learning and memory and affective behaviors ) , it is believed that alterations in hippocampal neurogenesis might underlie some of the behavioral deficits associated with these psychiatric and neurological conditions .

Example answer:
{"entities": [{"text": "functioning", "type": "BiologicFunction"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "learning", "type": "BiologicFunction"}, {"text": "memory", "type": "BiologicFunction"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "neurogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: For men , the associations were robust for controlling childhood parental socioeconomic status , history of unemployment , and adulthood health behavior , but attenuated circa 35 % when three major temperament traits were taken into account .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "associations", "type": "BiologicFunction"}, {"text": "unemployment", "type": "Finding"}, {"text": "temperament", "type": "BiologicFunction"}]}

Example input:
Sentence: Early hippocampal volume loss as a marker of eventual memory deficits caused by repeated stress Exposure to severe and prolonged stress has detrimental effects on the hippocampus .

Example answer:
{"entities": [{"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "volume loss", "type": "Finding"}, {"text": "marker", "type": "ClinicalAttribute"}, {"text": "memory deficits", "type": "BiologicFunction"}, {"text": "repeated stress", "type": "Finding"}, {"text": "stress", "type": "Finding"}, {"text": "detrimental effects", "type": "Finding"}, {"text": "hippocampus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Together , these findings support the view that not only is smaller hippocampal volume linked to stress - induced memory deficits , but it may also act as an early risk factor for the eventual development of cognitive impairments seen in stress - related psychiatric disorders .

Example answer:
{"entities": [{"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "stress", "type": "Finding"}, {"text": "memory deficits", "type": "BiologicFunction"}, {"text": "risk factor", "type": "Finding"}, {"text": "cognitive impairments", "type": "BiologicFunction"}]}

Example input:
Sentence: The aim of this study was to examine temperament in symptomatic and asymptomatic child offspring of parents with bipolar disorder ( OBD ) and to investigate whether inhibited temperament is associated with aberrant hippocampal volumes compared with healthy control ( HC ) youth .

Example answer:
{"entities": [{"text": "examine", "type": "Finding"}, {"text": "temperament", "type": "BiologicFunction"}, {"text": "asymptomatic", "type": "Finding"}, {"text": "bipolar disorder", "type": "BiologicFunction"}, {"text": "OBD", "type": "BiologicFunction"}, {"text": "hippocampal", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Inhibited Temperament and Hippocampal Volume in Offspring of Parents with Bipolar Disorder Prior studies have suggested that inhibited temperament may be associated with an increased risk for developing anxiety or mood disorder , including bipolar disorder .

Example answer:
{"entities": [{"text": "Temperament", "type": "BiologicFunction"}, {"text": "Hippocampal", "type": "AnatomicalStructure"}, {"text": "Bipolar Disorder", "type": "BiologicFunction"}, {"text": "temperament", "type": "BiologicFunction"}, {"text": "anxiety", "type": "BiologicFunction"}, {"text": "mood disorder", "type": "BiologicFunction"}, {"text": "bipolar disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: Within the OBD ( + ) s group , a more inhibited temperament was associated with smaller right hippocampal volumes .

Example answer:
{"entities": [{"text": "OBD ( + ) s", "type": "BiologicFunction"}, {"text": "temperament", "type": "BiologicFunction"}, {"text": "right", "type": "SpatialConcept"}, {"text": "hippocampal", "type": "AnatomicalStructure"}]}

Input:
Sentence: The association between temperament and hippocampal volumes was tested by using multiple regression analysis .

## Item MedMentions:test:1938
Example input:
Sentence: DCAN and DCAcAm formation decreased , and relatively stable TCNM formation increased , with increasing free chlorine contact time during chloramination .

Example answer:
{"entities": [{"text": "DCAN", "type": "Chemical"}, {"text": "DCAcAm", "type": "Chemical"}, {"text": "TCNM", "type": "Chemical"}, {"text": "chlorine", "type": "Chemical"}]}

Example input:
Sentence: In this study , six FmEG derivatives with deletion of N - terminal fragments or fusion with an extra family 1 carbohydrate - binding module ( CBM1 ) was constructed in order to evaluate the contribution of CBM1 to FmEG processivity and catalytic activity .

Example answer:
{"entities": [{"text": "FmEG", "type": "Chemical"}, {"text": "N - terminal fragments", "type": "Chemical"}, {"text": "fusion", "type": "Chemical"}, {"text": "family 1 carbohydrate - binding module", "type": "Chemical"}, {"text": "CBM1", "type": "Chemical"}, {"text": "catalytic activity", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , the predicted Ames test indicated potential mutagenicity of CNM .

Example answer:
{"entities": [{"text": "CNM", "type": "Chemical"}]}

Example input:
Sentence: NPM1 is directly associated with the DNA binding domain of p65 to enhance its DNA binding activity without being a part of the DNA - NF - κB complex .

Example answer:
{"entities": [{"text": "NPM1", "type": "AnatomicalStructure"}, {"text": "DNA binding domain", "type": "SpatialConcept"}, {"text": "p65", "type": "Chemical"}, {"text": "DNA binding", "type": "BiologicFunction"}, {"text": "DNA", "type": "Chemical"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "complex", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Our results suggest that such improvements in processivity and catalytic activity may arise from CBM1 binding affinity .

Example answer:
{"entities": [{"text": "CBM1", "type": "Chemical"}, {"text": "binding affinity", "type": "BiologicFunction"}]}

Example input:
Sentence: Efficient DNA binding of NF - κB requires the chaperone -like function of NPM1 NPM1 / nucleophosmin is frequently overexpressed in various tumors , although the oncogenic role of NPM1 remains unclear .

Example answer:
{"entities": [{"text": "DNA binding", "type": "BiologicFunction"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "chaperone", "type": "Chemical"}, {"text": "NPM1", "type": "AnatomicalStructure"}, {"text": "NPM1 / nucleophosmin", "type": "AnatomicalStructure"}, {"text": "overexpressed", "type": "BiologicFunction"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "oncogenic", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The PCR array analysis showed that CNM significantly upregulated about 7 % of all DNA damage - related genes .

Example answer:
{"entities": [{"text": "PCR array", "type": "ResearchActivity"}, {"text": "CNM", "type": "Chemical"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "DNA damage - related", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: By exploring the biological function of these genes , it was found that the predicted CNM genotoxicity is likely to be mediated by apoptosis .

Example answer:
{"entities": [{"text": "biological function", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "CNM", "type": "Chemical"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: The predicted ADME / Tox profile suggests that external use of CNM may be preferable to systemic exposure , while its genotoxicity was characterized by the upregulation of apoptosis - related genes after treatment .

Example answer:
{"entities": [{"text": "ADME", "type": "ResearchActivity"}, {"text": "CNM", "type": "Chemical"}, {"text": "upregulation", "type": "BiologicFunction"}, {"text": "apoptosis - related", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: CNM did not pass all parameters of Lipinski 's rule of five , with a predicted low oral bioavailability and high plasma protein binding , but with good predicted blood brain barrier penetration .

Example answer:
{"entities": [{"text": "CNM", "type": "Chemical"}, {"text": "parameters", "type": "IntellectualProduct"}, {"text": "Lipinski 's rule of five", "type": "IntellectualProduct"}, {"text": "oral", "type": "SpatialConcept"}, {"text": "plasma protein binding", "type": "BiologicFunction"}]}

Input:
Sentence: CNM was predicted to show low affinity to cytochrome P450 family members .

## Item MedMentions:test:1585
Example input:
Sentence: rubidus was documented from 10 . 75 % of specimens collected during 2010 and 2011 , indicating periodic interbreeding between the introduced and native species .

Example answer:
{"entities": [{"text": "rubidus", "type": "Eukaryote"}, {"text": "interbreeding", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: We clearly demonstrate that H . comosa followed a latitudinal and due to its oceanity also a longitudinal gradient during the last glacial maximum ( LGM ) , restricting the species to southern refugia situated on the Peninsulas of Iberia , the Balkans , and Italy during the last glaciation .

Example answer:
{"entities": [{"text": "H . comosa", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Peninsulas of Iberia", "type": "SpatialConcept"}, {"text": "Balkans", "type": "SpatialConcept"}, {"text": "Italy", "type": "SpatialConcept"}]}

Example input:
Sentence: Flourishing Sponge -Based Ecosystems after the End - Ordovician Mass Extinction The Late Ordovician ( Hirnantian , approximately 445 million years ago ) extinction event was among the largest known , with 85 % species loss [ 1 ] .

Example answer:
{"entities": [{"text": "Sponge", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: Species distribution modeling and molecular markers suggest longitudinal range shifts and cryptic northern refugia of the typical calcareous grassland species Hippocrepis comosa ( horseshoe vetch ) Calcareous grasslands belong to the most diverse , endangered habitats in Europe , but there is still insufficient information about the origin of the plant species related to these grasslands .

Example answer:
{"entities": [{"text": "Species", "type": "IntellectualProduct"}, {"text": "modeling", "type": "ResearchActivity"}, {"text": "molecular markers", "type": "ClinicalAttribute"}, {"text": "calcareous grassland", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Hippocrepis comosa", "type": "Eukaryote"}, {"text": "horseshoe vetch", "type": "Eukaryote"}, {"text": "Calcareous grasslands", "type": "SpatialConcept"}, {"text": "endangered habitats", "type": "SpatialConcept"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "plant", "type": "Eukaryote"}, {"text": "grasslands", "type": "SpatialConcept"}]}

Example input:
Sentence: Pollination of flowers with long corolla tubes by long - tongued hawkmoths has been invoked as a showcase model of co - evolution .

Example answer:
{"entities": [{"text": "Pollination", "type": "BiologicFunction"}, {"text": "flowers", "type": "Eukaryote"}, {"text": "long corolla tubes", "type": "Eukaryote"}, {"text": "long - tongued hawkmoths", "type": "Eukaryote"}, {"text": "co - evolution", "type": "BiologicFunction"}]}

Example input:
Sentence: Network analysis reveals why Xylella fastidiosa will persist in Europe The insect vector borne bacterium Xylella fastidiosa was first detected in olive trees in Southern Italy in 2013 , and identified as the main culprit behind the ' olive quick decline syndrome ' .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "Xylella fastidiosa", "type": "Bacterium"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "insect vector", "type": "Eukaryote"}, {"text": "bacterium", "type": "Bacterium"}, {"text": "olive trees", "type": "Eukaryote"}, {"text": "Southern Italy", "type": "SpatialConcept"}, {"text": "olive quick decline syndrome", "type": "BiologicFunction"}]}

Example input:
Sentence: Chasing ghosts : allopolyploid origin of Oxyria sinensis ( Polygonaceae ) from its only diploid congener and an unknown ancestor Reconstructing the origin of a polyploid species is particularly challenging when an ancestor has become extinct . Under such circumstances , the extinct donor of a genome found in the polyploid may be treated as a ' ghost ' species in that its prior existence is recognized through the presence of its genome in the polyploid .

Example answer:
{"entities": [{"text": "Oxyria sinensis", "type": "Eukaryote"}, {"text": "Polygonaceae", "type": "Eukaryote"}, {"text": "polyploid", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "genome", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Here , we study the population genetic diversity , structure , and stability of a classic " island giant " ( Xantusia riversiana , the Island Night Lizard ) on San Clemente Island , California following the removal of feral goats .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "population", "type": "PopulationGroup"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "island giant", "type": "Eukaryote"}, {"text": "Xantusia riversiana", "type": "Eukaryote"}, {"text": "Island Night Lizard", "type": "Eukaryote"}, {"text": "San Clemente Island", "type": "SpatialConcept"}, {"text": "California", "type": "SpatialConcept"}, {"text": "feral goats", "type": "Eukaryote"}]}

Example input:
Sentence: In this study , we phylogenomically investigated the inter - relationships of the three surviving Society Island valley Partula species : P .

Example answer:
{"entities": [{"text": "phylogenomically investigated", "type": "ResearchActivity"}, {"text": "Society Island valley", "type": "SpatialConcept"}, {"text": "Partula species", "type": "Eukaryote"}, {"text": "P .", "type": "Eukaryote"}]}

Example input:
Sentence: Sampling will be expanded to include the remaining Society Island partulid taxa to further explore the evolutionary history of this radiation .

Example answer:
{"entities": [{"text": "Society Island", "type": "SpatialConcept"}, {"text": "partulid", "type": "Eukaryote"}, {"text": "evolutionary history", "type": "BiologicFunction"}]}

Input:
Sentence: Deliberate introduction of the predatory rosy wolf snail Euglandina rosea in the late 20th century led to the extinction / extirpation of 55 / 61 Society Island Partulidae species .

## Item MedMentions:test:2162
Example input:
Sentence: 8±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 8±7 .

Example answer:
{"entities": []}

Example input:
Sentence: 7 , p = 8 .

Example answer:
{"entities": []}

Example input:
Sentence: 8U·g ( - 1 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 8 versus 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 8 , P = . 027 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 8 vs .

Example answer:
{"entities": []}

Example input:
Sentence: 8 vs .

Example answer:
{"entities": []}

Example input:
Sentence: 8 .

Example answer:
{"entities": []}

Example input:
Sentence: 8 .

Example answer:
{"entities": []}

Input:
Sentence: 8 ) .

## Item MedMentions:test:2163
Example input:
Sentence: 5 points ( unadjusted 95 % CI : -10 . 1 , -1 .

Example answer:
{"entities": []}

Example input:
Sentence: 9 ( 95 % CI : 0 . 5 - 1 . 6 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 4 ; 95 % CI , -7 . 2 to -1 . 6 ; P = .002 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 4 , 95 % CI = -15 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 percentage points ; 95 % confidence interval [ CI ] , -3 . 33 to 5 . 93 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 4 , 95 % CI : 2 . 80 - 38 . 4 ] .

Example answer:
{"entities": []}

Example input:
Sentence: 94 ( CI 95 % : 0 . 90 to 0 . 96 ) and 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 9 ( 95 % CI 6 . 8 - 9 . 2 ) and 4 . 1 ( 95 % CI 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 9 % ( 95 % CI : 79 . 6 , 97 . 7 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 4 . 86 ( 95 % CI , 1 . 9 - 11 .

Example answer:
{"entities": []}

Input:
Sentence: 4 points ( 95 % CI , 3 . 2 - 9 . 3 ) .

## Item MedMentions:test:1447
Example input:
Sentence: Angiotensin - converting enzyme insertion / deletion polymorphism association with obesity and some related disorders in Egyptian females : a case - control observational study According to the WHO report in 2015 , obesity is the fifth leading cause of death worldwide , and the prevalence of Egyptian female obesity is 37 . 5 % .

Example answer:
{"entities": [{"text": "Angiotensin - converting enzyme insertion / deletion polymorphism", "type": "Finding"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "disorders", "type": "BiologicFunction"}, {"text": "Egyptian", "type": "PopulationGroup"}, {"text": "case - control observational study", "type": "ResearchActivity"}, {"text": "WHO", "type": "Organization"}, {"text": "report", "type": "IntellectualProduct"}, {"text": "cause of death", "type": "Finding"}, {"text": "female", "type": "PopulationGroup"}]}

Example input:
Sentence: Matrix metalloproteinase - 9 Gene - 1562C > T Gene Polymorphism and Coronary Artery Disease in the Chinese Han Population : A Meta - Analysis of 5468 Subjects Multiple studies indicate that the matrix metalloproteinase - 9 ( MMP - 9 ) - 1562C > T gene polymorphism may be associated with an increased risk of coronary artery disease ( CAD ) in the Chinese Han population .

Example answer:
{"entities": [{"text": "Matrix metalloproteinase - 9 Gene - 1562C > T Gene", "type": "AnatomicalStructure"}, {"text": "Coronary Artery Disease", "type": "BiologicFunction"}, {"text": "Meta - Analysis", "type": "ResearchActivity"}, {"text": "Subjects", "type": "PopulationGroup"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "matrix metalloproteinase - 9 ( MMP - 9 ) - 1562C > T gene", "type": "AnatomicalStructure"}, {"text": "increased risk", "type": "Finding"}, {"text": "coronary artery disease", "type": "BiologicFunction"}, {"text": "CAD", "type": "BiologicFunction"}]}

Example input:
Sentence: Our analysis confirms the association between the MMP - 9 - 1562C > T gene polymorphism and an increased risk of CAD within the Chinese Han population under allelic ( OR : 1 . 60 , 95 % CI : 1 . 25 - 2 . 04 , P = 0 . 0002 ) , recessive ( OR : 3 . 05 , 95 % CI : 1 . 67 - 5 . 56 , P = 0 .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "MMP - 9 - 1562C > T gene", "type": "AnatomicalStructure"}, {"text": "increased risk", "type": "Finding"}, {"text": "CAD", "type": "BiologicFunction"}, {"text": "allelic", "type": "AnatomicalStructure"}, {"text": "recessive", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Moreover , stratification analyses indicated that the R1628P polymorphism was significantly associated with an increased risk of PD among Chinese as well as non - Chinese Asian populations and an increased risk of PD in Chinese patients from China , Taiwan , and Singapore .

Example answer:
{"entities": [{"text": "stratification analyses", "type": "ResearchActivity"}, {"text": "R1628P polymorphism", "type": "SpatialConcept"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "Chinese", "type": "PopulationGroup"}, {"text": "non - Chinese Asian populations", "type": "PopulationGroup"}, {"text": "China", "type": "SpatialConcept"}, {"text": "Taiwan", "type": "SpatialConcept"}, {"text": "Singapore", "type": "SpatialConcept"}]}

Example input:
Sentence: We investigated the associations between three XPC gene polymorphisms ( rs2228001 A > C , rs2228000 C > T , and rs2229090 G > C ) and neuroblastoma risk with 256 neuroblastoma patients and 531 healthy controls in a Chinese Han population .

Example answer:
{"entities": [{"text": "XPC gene", "type": "AnatomicalStructure"}, {"text": "rs2228001 A > C", "type": "AnatomicalStructure"}, {"text": "rs2228000 C > T", "type": "AnatomicalStructure"}, {"text": "rs2229090 G > C", "type": "AnatomicalStructure"}, {"text": "neuroblastoma", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: The African variant was identified in 49 . 4 % of samples that were positive for BKV .

Example answer:
{"entities": [{"text": "African", "type": "SpatialConcept"}, {"text": "positive", "type": "Finding"}, {"text": "BKV", "type": "Virus"}]}

Example input:
Sentence: In the Chinese Han population , the MMP - 9 - 1562C > T gene polymorphism is correlated with an increased risk of CAD .

Example answer:
{"entities": [{"text": "MMP - 9 - 1562C > T gene", "type": "AnatomicalStructure"}, {"text": "increased risk", "type": "Finding"}, {"text": "CAD", "type": "BiologicFunction"}]}

Example input:
Sentence: The rs6983267 polymorphism has no association with BC risk in any genetic model .

Example answer:
{"entities": [{"text": "rs6983267 polymorphism", "type": "SpatialConcept"}, {"text": "BC", "type": "BiologicFunction"}, {"text": "genetic model", "type": "IntellectualProduct"}]}

Example input:
Sentence: Association between 8q24 ( rs13281615 and rs6983267 ) polymorphism and breast cancer susceptibility : a meta - analysis involving 117 , 355 subjects Published data on the association between 8q24 polymorphism and breast cancer ( BC ) risk are inconclusive .

Example answer:
{"entities": [{"text": "8q24", "type": "AnatomicalStructure"}, {"text": "rs13281615", "type": "SpatialConcept"}, {"text": "rs6983267", "type": "SpatialConcept"}, {"text": "polymorphism", "type": "BiologicFunction"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "susceptibility", "type": "ClinicalAttribute"}, {"text": "meta - analysis", "type": "ResearchActivity"}, {"text": "Published data", "type": "IntellectualProduct"}, {"text": "BC", "type": "BiologicFunction"}]}

Example input:
Sentence: Thus , we conducted a meta - analysis to evaluate the relationship between 8q24 ( rs13281615 and rs6983267 ) polymorphism and BC risk .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}, {"text": "8q24", "type": "AnatomicalStructure"}, {"text": "rs13281615", "type": "SpatialConcept"}, {"text": "rs6983267", "type": "SpatialConcept"}, {"text": "polymorphism", "type": "BiologicFunction"}, {"text": "BC", "type": "BiologicFunction"}]}

Input:
Sentence: This meta - analysis suggests that 8q24 rs13281615 polymorphism is a risk factor for susceptibility to BC in Asians , Caucasians and in overall population , While , there was no association in Africans .

## Item MedMentions:test:1885
Example input:
Sentence: To address this issue , the pathophysiology of chronic lung inflammation induced by Pseudomonas aeruginosa in CCSP - deficient mice was determined .

Example answer:
{"entities": [{"text": "chronic lung inflammation", "type": "BiologicFunction"}, {"text": "Pseudomonas aeruginosa", "type": "Bacterium"}, {"text": "CCSP", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: aeruginosa inflammation resulted in chronic bronchitis and emphysematous changes in the CCSP - deficient mice .

Example answer:
{"entities": [{"text": "aeruginosa", "type": "Bacterium"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "chronic bronchitis", "type": "BiologicFunction"}, {"text": "CCSP", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Further research is critically necessary in order to fully explain roles for tight junctional components such as Cldn6 and other related molecules in lungs coping with exposure .

Example answer:
{"entities": [{"text": "tight junctional components", "type": "SpatialConcept"}, {"text": "Cldn6", "type": "Chemical"}, {"text": "lungs", "type": "AnatomicalStructure"}, {"text": "exposure", "type": "Finding"}]}

Example input:
Sentence: Claudin - 6 ( Cldn6 ) is a tetraspanin transmembrane protein found within the tight junctional complex and is implicated in maintaining lung epithelial barriers .

Example answer:
{"entities": [{"text": "Claudin - 6", "type": "Chemical"}, {"text": "Cldn6", "type": "Chemical"}, {"text": "tetraspanin transmembrane protein", "type": "Chemical"}, {"text": "tight junctional complex", "type": "SpatialConcept"}, {"text": "lung epithelial barriers", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Immunoblotting and qRT - PCR confirmed the differential expression of Cldn6 and the pro - inflammatory cytokines TNF - α and IL - 1β .

Example answer:
{"entities": [{"text": "Immunoblotting", "type": "HealthCareActivity"}, {"text": "qRT - PCR", "type": "ResearchActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Cldn6", "type": "Chemical"}, {"text": "pro - inflammatory cytokines", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "IL - 1β", "type": "Chemical"}]}

Example input:
Sentence: Up - Regulation of Claudin - 6 in the Distal Lung Impacts Secondhand Smoke -Induced Inflammation It has long been understood that increased epithelial permeability contributes to inflammation observed in many respiratory diseases .

Example answer:
{"entities": [{"text": "Up - Regulation", "type": "BiologicFunction"}, {"text": "Claudin - 6", "type": "Chemical"}, {"text": "Distal", "type": "SpatialConcept"}, {"text": "Lung", "type": "AnatomicalStructure"}, {"text": "Secondhand Smoke", "type": "InjuryOrPoisoning"}, {"text": "Inflammation", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "respiratory diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: A subset of Cldn6 TG and control mice were also subjected to daily secondhand tobacco smoke ( SHS ) via a nose only inhalation system from PN30 - 90 and compared to room air ( RA ) controls .

Example answer:
{"entities": [{"text": "Cldn6 TG", "type": "Eukaryote"}, {"text": "control", "type": "Eukaryote"}, {"text": "mice", "type": "Eukaryote"}, {"text": "secondhand tobacco smoke", "type": "InjuryOrPoisoning"}, {"text": "SHS", "type": "InjuryOrPoisoning"}, {"text": "nose", "type": "AnatomicalStructure"}, {"text": "inhalation system", "type": "BodySystem"}]}

Example input:
Sentence: These data reveal captivating information suggesting a role for Cldn6 in lungs exposed to tobacco smoke .

Example answer:
{"entities": [{"text": "Cldn6", "type": "Chemical"}, {"text": "lungs", "type": "AnatomicalStructure"}, {"text": "exposed", "type": "Finding"}, {"text": "tobacco smoke", "type": "Chemical"}]}

Example input:
Sentence: control animals and SHS decreased Cldn6 expression regardless of genetic up - regulation .

Example answer:
{"entities": [{"text": "control animals", "type": "Eukaryote"}, {"text": "SHS", "type": "InjuryOrPoisoning"}, {"text": "Cldn6", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "up - regulation", "type": "BiologicFunction"}]}

Example input:
Sentence: To test the hypothesis that increased Cldn6 ameliorates inflammation at the respiratory barrier , we utilized the Tet - On inducible transgenic system to conditionally over - express Clnd6 in the distal lung .

Example answer:
{"entities": [{"text": "Cldn6", "type": "Chemical"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "respiratory barrier", "type": "AnatomicalStructure"}, {"text": "transgenic system", "type": "AnatomicalStructure"}, {"text": "over - express", "type": "BiologicFunction"}, {"text": "Clnd6", "type": "Chemical"}, {"text": "distal", "type": "SpatialConcept"}, {"text": "lung", "type": "AnatomicalStructure"}]}

Input:
Sentence: As a general theme , inflammation induced by SHS exposure was influenced by the availability of Cldn6 .

## Item MedMentions:test:1891
Example input:
Sentence: Methods : In this eight - week multicenter study , patients were randomized to either a hydrogen peroxide -based or a benzoyl peroxide -based regimen .The primary outcome measure of clinical response was assessed using the Global Acne Grading System ( GAGS ) at baseline , four weeks , and eight weeks .

Example answer:
{"entities": [{"text": "Methods", "type": "IntellectualProduct"}, {"text": "multicenter study", "type": "ResearchActivity"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "hydrogen peroxide", "type": "Chemical"}, {"text": "benzoyl peroxide", "type": "Chemical"}, {"text": "regimen", "type": "HealthCareActivity"}, {"text": "clinical response", "type": "Finding"}, {"text": "Global Acne Grading System", "type": "HealthCareActivity"}, {"text": "GAGS", "type": "HealthCareActivity"}]}

Example input:
Sentence: The primary outcome was proportion of subjects without treatment failure ( regimen switch or VL > 200 copies / mL twice consecutively ) at 48 weeks .

Example answer:
{"entities": [{"text": "subjects", "type": "PopulationGroup"}, {"text": "treatment failure", "type": "Finding"}, {"text": "regimen", "type": "HealthCareActivity"}]}

Example input:
Sentence: 6 ( range 2 - 7 ) days ; major complications were postablation syndrome in 2 / 35 ( 5 . 7 % ) , peritoneal fluid in 4 / 35 ( 11 . 4 % ) , and transient jaundice in 1 / 35 ( 2 . 8 % ) patients .

Example answer:
{"entities": [{"text": "syndrome", "type": "BiologicFunction"}, {"text": "peritoneal fluid", "type": "BodySubstance"}, {"text": "jaundice", "type": "BiologicFunction"}]}

Example input:
Sentence: Of the 413 patients with a hallux amputation , there were 368 eligible patients who had a history of DM with documented hemoglobin A1c ( HbA1c ) within 3 months of the initial first ray ( hallux and first metatarsal ) amputation and available radiographic data .

Example answer:
{"entities": [{"text": "hallux amputation", "type": "HealthCareActivity"}, {"text": "history", "type": "Finding"}, {"text": "DM", "type": "BiologicFunction"}, {"text": "hemoglobin A1c", "type": "Chemical"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "first ray", "type": "SpatialConcept"}, {"text": "hallux", "type": "AnatomicalStructure"}, {"text": "first metatarsal", "type": "AnatomicalStructure"}, {"text": "amputation", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , in our study , surgery did not achieve the expected outcome in patients with specific metabolic , anthropometric and surgical characteristics ( BMI > 50 Kg / m2 , presence of metabolic syndrome , presence of T2DM with high preoperative HbA1c % level and gastric pouch volume greater than 60 ml ) .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "expected", "type": "IntellectualProduct"}, {"text": "surgical", "type": "HealthCareActivity"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "metabolic syndrome", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "gastric pouch", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Preoperative abnormalities in glucose homeostasis were confirmed in 64 ( 47 % ) patients .

Example answer:
{"entities": [{"text": "abnormalities", "type": "Finding"}, {"text": "glucose homeostasis", "type": "BiologicFunction"}]}

Example input:
Sentence: Evaluation of the cohort noted significantly increased overall morbidity , serious morbidity , and mortality in the hypoalbuminemic group ( P < .01 for all procedures ) .

Example answer:
{"entities": [{"text": "cohort", "type": "PopulationGroup"}, {"text": "hypoalbuminemic", "type": "BiologicFunction"}, {"text": "group", "type": "PopulationGroup"}, {"text": "procedures", "type": "HealthCareActivity"}]}

Example input:
Sentence: Serum albumin is a strong predictor of short - term postoperative complications in the urologic oncology patient .

Example answer:
{"entities": [{"text": "Serum albumin", "type": "Chemical"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "urologic oncology", "type": "HealthCareActivity"}]}

Example input:
Sentence: Preoperative Albumin Is Predictive of Early Postoperative Morbidity and Mortality in Common Urologic Oncologic Surgeries Multiple studies have linked preoperative nutrition status to postoperative outcomes .

Example answer:
{"entities": [{"text": "Albumin", "type": "Chemical"}, {"text": "Urologic Oncologic Surgeries", "type": "HealthCareActivity"}, {"text": "Multiple studies", "type": "ResearchActivity"}, {"text": "nutrition status", "type": "Finding"}]}

Example input:
Sentence: Hypoalbuminemia was associated with a significantly higher 30 - day mortality in major procedures such as cystectomy , and in smaller procedures such as TURBT ( P < .01 ) .

Example answer:
{"entities": [{"text": "Hypoalbuminemia", "type": "BiologicFunction"}, {"text": "procedures", "type": "HealthCareActivity"}, {"text": "cystectomy", "type": "HealthCareActivity"}, {"text": "TURBT", "type": "HealthCareActivity"}]}

Input:
Sentence: Hypoalbuminemic patients were compared with those with normal preoperative albumin , and 30 - day outcomes were evaluated .

## Item MedMentions:test:2043
Example input:
Sentence: 1 in skeletal muscle triads The adaptor protein STAC3 is essential for skeletal muscle excitation - contraction ( EC ) coupling and a mutation in the STAC3 gene has been linked to a severe muscle disease , Native American myopathy ( NAM ) .

Example answer:
{"entities": [{"text": "1", "type": "Chemical"}, {"text": "skeletal muscle triads", "type": "AnatomicalStructure"}, {"text": "adaptor protein", "type": "Chemical"}, {"text": "STAC3", "type": "Chemical"}, {"text": "skeletal muscle", "type": "AnatomicalStructure"}, {"text": "excitation - contraction ( EC ) coupling", "type": "BiologicFunction"}, {"text": "mutation", "type": "BiologicFunction"}, {"text": "STAC3 gene", "type": "AnatomicalStructure"}, {"text": "muscle disease", "type": "BiologicFunction"}, {"text": "Native American myopathy", "type": "BiologicFunction"}, {"text": "NAM", "type": "BiologicFunction"}]}

Example input:
Sentence: Additionally , transforming growth factor‑β1 ( TGF‑β1 ) induced the EMT , characterized by the upregulated expression of the mesenchymal markers , namely N‑cadherin , vimentin , α‑smooth muscle actin , collagen I and collagen III , and the downregulated expression of the epithelial marker E - cadherin in A549 and HBE cells .

Example answer:
{"entities": [{"text": "transforming growth factor‑β1", "type": "Chemical"}, {"text": "TGF‑β1", "type": "Chemical"}, {"text": "EMT", "type": "BiologicFunction"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "expression", "type": "HealthCareActivity"}, {"text": "mesenchymal markers", "type": "BiologicFunction"}, {"text": "N‑cadherin", "type": "Chemical"}, {"text": "vimentin", "type": "Chemical"}, {"text": "α‑smooth muscle actin", "type": "Chemical"}, {"text": "collagen I", "type": "Chemical"}, {"text": "collagen III", "type": "Chemical"}, {"text": "downregulated", "type": "BiologicFunction"}, {"text": "epithelial marker", "type": "BiologicFunction"}, {"text": "E - cadherin", "type": "Chemical"}, {"text": "A549", "type": "AnatomicalStructure"}, {"text": "HBE cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In severe to profound sudden deafness refractory to conventional ST , the daily perfusion of 4mg / ml DEX through an intratympanic catheter is an easy , well accepted procedure that enables patients to receive a drug in the middle ear in a repeatable or sustained form , with minimal discomfort and a partial rescue ( 67 . 86 % ) and a speech recognition gain of 39 % .

Example answer:
{"entities": [{"text": "sudden deafness", "type": "Finding"}, {"text": "ST", "type": "HealthCareActivity"}, {"text": "perfusion", "type": "HealthCareActivity"}, {"text": "DEX", "type": "Chemical"}, {"text": "catheter", "type": "MedicalDevice"}, {"text": "drug", "type": "Chemical"}, {"text": "middle ear", "type": "SpatialConcept"}, {"text": "repeatable", "type": "HealthCareActivity"}, {"text": "sustained form", "type": "Chemical"}, {"text": "discomfort and a partial rescue", "type": "ResearchActivity"}]}

Example input:
Sentence: Are TMCs the Mechanotransduction Channels of Vertebrate Hair Cells ?

Example answer:
{"entities": [{"text": "TMCs", "type": "Chemical"}, {"text": "Mechanotransduction", "type": "BiologicFunction"}, {"text": "Channels", "type": "Chemical"}, {"text": "Vertebrate", "type": "Eukaryote"}, {"text": "Hair Cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We used functional MRI - guided proton magnetic resonance spectroscopy to test the hypothesis that unilateral deafferentation is associated with lower levels of N - acetylaspartate ( NAA , a putative marker of neuronal integrity ) in the sensorimotor hand territory located contralateral to the missing hand in chronic amputees ( n = 19 ) compared with the analogous hand territory of age - and sex - matched healthy controls ( n = 28 ) .

Example answer:
{"entities": [{"text": "MRI - guided proton magnetic resonance spectroscopy", "type": "HealthCareActivity"}, {"text": "unilateral deafferentation", "type": "HealthCareActivity"}, {"text": "lower levels of N - acetylaspartate", "type": "Finding"}, {"text": "NAA", "type": "Chemical"}, {"text": "putative marker", "type": "ClinicalAttribute"}, {"text": "neuronal", "type": "AnatomicalStructure"}, {"text": "contralateral", "type": "SpatialConcept"}, {"text": "missing hand", "type": "Finding"}, {"text": "hand territory", "type": "Finding"}, {"text": "age - and sex - matched", "type": "Finding"}]}

Example input:
Sentence: Planar cell polarity ( PCP ) in hair cells ( HCs ) in the cochlea is essential for mechanotransduction and refers to the asymmetric structure consisting of stereociliary bundles and the kinocilium on the apical surface of the cell body .

Example answer:
{"entities": [{"text": "Planar cell polarity", "type": "SpatialConcept"}, {"text": "PCP", "type": "SpatialConcept"}, {"text": "hair cells", "type": "AnatomicalStructure"}, {"text": "HCs", "type": "AnatomicalStructure"}, {"text": "cochlea", "type": "AnatomicalStructure"}, {"text": "mechanotransduction", "type": "BiologicFunction"}, {"text": "asymmetric", "type": "SpatialConcept"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "stereociliary", "type": "AnatomicalStructure"}, {"text": "kinocilium", "type": "AnatomicalStructure"}, {"text": "apical", "type": "SpatialConcept"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "cell body", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Sensory transduction in vertebrate hair cells and the molecules that mediate it have long been of great interest .

Example answer:
{"entities": [{"text": "transduction", "type": "BiologicFunction"}, {"text": "vertebrate", "type": "Eukaryote"}, {"text": "hair cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Establishment of a Flexible Real - Time Polymerase Chain Reaction -Based Platform for Detecting Prevalent Deafness Mutations Associated with Variable Degree of Sensorineural Hearing Loss in Koreans Many cutting - edge technologies based on next - generation sequencing ( NGS ) have been employed to identify candidate variants responsible for sensorineural hearing loss ( SNHL ) .

Example answer:
{"entities": [{"text": "Real - Time Polymerase Chain Reaction", "type": "ResearchActivity"}, {"text": "Detecting", "type": "Finding"}, {"text": "Deafness", "type": "Finding"}, {"text": "Mutations", "type": "BiologicFunction"}, {"text": "Sensorineural Hearing Loss", "type": "BiologicFunction"}, {"text": "Koreans", "type": "PopulationGroup"}, {"text": "next - generation sequencing", "type": "ResearchActivity"}, {"text": "NGS", "type": "ResearchActivity"}, {"text": "identify", "type": "Finding"}, {"text": "candidate", "type": "PopulationGroup"}, {"text": "variants", "type": "AnatomicalStructure"}, {"text": "sensorineural hearing loss", "type": "BiologicFunction"}, {"text": "SNHL", "type": "BiologicFunction"}]}

Example input:
Sentence: We discovered a gene co - occurrence network in mesiodens patients with functionally enriched gene groups in the sonic hedgehog ( SHH ) , bone morphogenetic proteins ( BMP ) , and wingless integrated ( WNT ) signaling pathways .

Example answer:
{"entities": [{"text": "gene", "type": "AnatomicalStructure"}, {"text": "mesiodens", "type": "BiologicFunction"}, {"text": "sonic hedgehog", "type": "Chemical"}, {"text": "SHH", "type": "Chemical"}, {"text": "bone morphogenetic proteins", "type": "Chemical"}, {"text": "BMP", "type": "Chemical"}, {"text": "wingless integrated", "type": "Chemical"}, {"text": "WNT", "type": "Chemical"}, {"text": "signaling pathways", "type": "BiologicFunction"}]}

Example input:
Sentence: Now , two strong candidates , TMC1 and TMC2 ( transmembrane channel - like ) , have emerged from discovery of deafness genes in humans and mice .

Example answer:
{"entities": [{"text": "TMC1", "type": "Chemical"}, {"text": "TMC2", "type": "Chemical"}, {"text": "deafness genes", "type": "AnatomicalStructure"}, {"text": "humans", "type": "Eukaryote"}, {"text": "mice", "type": "Eukaryote"}]}

Input:
Sentence: Some components of the mechanotransduction apparatus have been identified , most as deafness gene products .

## Item MedMentions:test:1880
Example input:
Sentence: Increase of hydrophobic and π - π stacking interactions led to the decrease of pKa values .

Example answer:
{"entities": [{"text": "hydrophobic", "type": "BiologicFunction"}]}

Example input:
Sentence: ( 2 . 9 wt % ) and the second in the order of decreasing Fe concentration ( 2 . 2 wt % ) , which explains their color and indicates that the excess amount of Fe is distributed through the plant body .

Example answer:
{"entities": [{"text": "decreasing", "type": "Finding"}, {"text": "Fe", "type": "Chemical"}, {"text": "plant body", "type": "Eukaryote"}]}

Example input:
Sentence: To clarify the effects , we measured its metal and pigment concentrations .

Example answer:
{"entities": [{"text": "metal", "type": "Chemical"}, {"text": "pigment", "type": "Chemical"}]}

Example input:
Sentence: Potassium and S were both negatively impacted by MeNPs , while B was only affected by 500 mg nCeO₂ · kg ( - 1 ) .

Example answer:
{"entities": [{"text": "Potassium", "type": "Chemical"}, {"text": "S", "type": "Chemical"}, {"text": "nCeO₂", "type": "Chemical"}]}

Example input:
Sentence: Pv - a CO2 /Ca - v O2 had a weak correlation with respiratory quotient ( Spearman R = 0 . 42 , P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "CO2", "type": "Chemical"}, {"text": "O2", "type": "Chemical"}, {"text": "respiratory quotient", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The scores of pigmentation were higher in the IMF group than those in the axilla group with statistical significance ( P < 0 .

Example answer:
{"entities": [{"text": "IMF", "type": "SpatialConcept"}, {"text": "group", "type": "PopulationGroup"}, {"text": "axilla", "type": "HealthCareActivity"}]}

Example input:
Sentence: Partial least square regression revealed that flavonol glycosides , phenolic acids , and anthocyanins displayed a positive correlation with L ( * ) , b ( * ) , and H ( * ) , but a negative correlation with a ( * ) and C ( * ) .

Example answer:
{"entities": [{"text": "flavonol glycosides", "type": "Chemical"}, {"text": "phenolic acids", "type": "Chemical"}, {"text": "anthocyanins", "type": "Chemical"}, {"text": "positive", "type": "Finding"}, {"text": "negative", "type": "Finding"}]}

Example input:
Sentence: This concentration -dependent dual effect of [ K [ Formula : see text ] ] o was observed using in vivo and in vitro mouse brain preparations as well as in human neocortical tissue resected during epilepsy surgery .

Example answer:
{"entities": [{"text": "K", "type": "Chemical"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "mouse brain preparations", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "neocortical", "type": "AnatomicalStructure"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "epilepsy", "type": "BiologicFunction"}, {"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: This inverse relationship between Ca and K can be explained by the reduced uptake of K in S .

Example answer:
{"entities": [{"text": "Ca", "type": "Chemical"}, {"text": "K", "type": "Chemical"}, {"text": "uptake", "type": "BiologicFunction"}, {"text": "S .", "type": "Eukaryote"}]}

Example input:
Sentence: ligulata in response to Ca stress , which is supported by the fact that the concentration of Ca is negatively correlated with that of K .

Example answer:
{"entities": [{"text": "ligulata", "type": "Eukaryote"}, {"text": "Ca", "type": "Chemical"}, {"text": "stress", "type": "Finding"}, {"text": "negatively", "type": "Finding"}, {"text": "K", "type": "Chemical"}]}

Input:
Sentence: Moreover , we observed that the concentration of Ca is negatively correlated with the concentrations of pigments and , conversely , that the concentration of K is positively correlated with the concentrations of pigments .

## Item MedMentions:test:1940
Example input:
Sentence: We examined factors associated with negative psychological consequences of a breast cancer diagnosis , in a diverse sample of 910 recently diagnosed patients ( 378 African - American , 372 White , and 160 Latina ) .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "negative", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "diagnosed", "type": "Finding"}, {"text": "African - American", "type": "PopulationGroup"}, {"text": "White", "type": "PopulationGroup"}, {"text": "Latina", "type": "PopulationGroup"}]}

Example input:
Sentence: Patients were compared based on age , sex , body mass index , tobacco use , presence of diabetes , and Charlson Comorbidity Index .

Example answer:
{"entities": [{"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients with a history of chronic back pain had consistently higher pain scores , but those pain scores did not differ significantly by location ( or protocol ) .

Example answer:
{"entities": [{"text": "history", "type": "Finding"}, {"text": "back pain", "type": "Finding"}, {"text": "pain scores", "type": "Finding"}, {"text": "location", "type": "SpatialConcept"}, {"text": "protocol", "type": "HealthCareActivity"}]}

Example input:
Sentence: Chronic conditions represent major causes of ill - health , avoidable disability , pain and anxiety , and tend to be more prevalent in less affluent groups .

Example answer:
{"entities": [{"text": "ill - health", "type": "Finding"}, {"text": "avoidable disability", "type": "Finding"}, {"text": "pain", "type": "Finding"}, {"text": "anxiety", "type": "Finding"}, {"text": "less affluent groups", "type": "PopulationGroup"}]}

Example input:
Sentence: Out of 100 patients , indications for stenting were locally advanced disease not amenable to surgery ( 52 % ) , metastatic disease ( 35 % ) , CVA ( 1 % ) , cardiac and respiratory problem ( 8 % ) , un - willing for surgery in 5 % of patients .

Example answer:
{"entities": [{"text": "stenting", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "metastatic disease", "type": "BiologicFunction"}, {"text": "CVA", "type": "BiologicFunction"}, {"text": "respiratory problem", "type": "Finding"}]}

Example input:
Sentence: The 18 case - control studies were rated as weak ; nine comparing people with OPC or OCC to people without cancer , eight comparing HPV - positive to HPV - negative cancer patients and one comparing OPCs to other head and neck cancers .

Example answer:
{"entities": [{"text": "case - control studies", "type": "ResearchActivity"}, {"text": "people", "type": "PopulationGroup"}, {"text": "OPC", "type": "BiologicFunction"}, {"text": "OCC", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "HPV - positive", "type": "Finding"}, {"text": "HPV - negative", "type": "Finding"}, {"text": "OPCs", "type": "BiologicFunction"}, {"text": "head", "type": "BiologicFunction"}, {"text": "neck cancers", "type": "BiologicFunction"}]}

Example input:
Sentence: Using data obtained by the Surveillance , Epidemiology , and End Results ( SEER ) program from 2010 - 2012 , a retrospective , population - based cohort study was conducted to investigate tumor subtype - specific differences in various characteristics , overall survival ( OS ) and breast cancer - specific mortality ( BCSM ) between males and females .

Example answer:
{"entities": [{"text": "Surveillance , Epidemiology , and End Results ( SEER ) program", "type": "Organization"}, {"text": "population - based cohort study", "type": "ResearchActivity"}, {"text": "tumor subtype", "type": "IntellectualProduct"}]}

Example input:
Sentence: Chronic conditions such as coronary artery disease ( odds ratio [ OR ] 1 . 48 ; 95 % confidence interval [ CI ] 1 . 04 - 2 . 05 ; p = 0 . 03 ) , diabetes ( OR 1 . 86 ; 95 % CI 1 . 32 - 2 . 62 ; p = 0 . 0004 ) , and peripheral vascular disease ( OR 1 . 61 ; 95 % CI 1 .

Example answer:
{"entities": [{"text": "Chronic conditions", "type": "Finding"}, {"text": "coronary artery disease", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "peripheral vascular disease", "type": "BiologicFunction"}]}

Example input:
Sentence: The link between self - perceptions of aging , cancer view and physical and mental health of older people with cancer : A cross - sectional study Older people may suffer from stigmas linked to cancer and aging .

Example answer:
{"entities": [{"text": "self - perceptions", "type": "BiologicFunction"}, {"text": "aging", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "mental health", "type": "BiologicFunction"}, {"text": "A cross - sectional study", "type": "ResearchActivity"}, {"text": "stigmas", "type": "BiologicFunction"}]}

Example input:
Sentence: African - American and Latina women reported greater psychological consequences related to their breast cancer diagnosis ; this disparity was mediated by differences in unmet social support .

Example answer:
{"entities": [{"text": "African - American", "type": "PopulationGroup"}, {"text": "Latina", "type": "SpatialConcept"}, {"text": "women", "type": "PopulationGroup"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "disparity", "type": "Finding"}]}

Input:
Sentence: We also wanted to reveal any differences in opinion among various groups ( chronic ischemic heart disease , chronic low back pain , breast cancer ) .

## Item MedMentions:test:1559
Example input:
Sentence: The mitochondrial localization of SHMT2 protein was visualized on IHC staining .

Example answer:
{"entities": [{"text": "mitochondrial localization", "type": "BiologicFunction"}, {"text": "SHMT2 protein", "type": "Chemical"}, {"text": "IHC", "type": "HealthCareActivity"}, {"text": "staining", "type": "HealthCareActivity"}]}

Example input:
Sentence: SHMT2 has been implicated as a critical component for tumor cell survival .

Example answer:
{"entities": [{"text": "SHMT2", "type": "Chemical"}, {"text": "tumor cell", "type": "AnatomicalStructure"}, {"text": "survival", "type": "BiologicFunction"}]}

Example input:
Sentence: Independent and pooled analysis confirmed that SHMT2 expression was associated with breast cancer tumor aggressiveness ( TNM staging and Elson grade ) in a dose - dependent manner ( p < 0 . 05 ) .

Example answer:
{"entities": [{"text": "Independent", "type": "ResearchActivity"}, {"text": "pooled analysis", "type": "ResearchActivity"}, {"text": "SHMT2", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "TNM staging", "type": "IntellectualProduct"}, {"text": "Elson grade", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Furthermore , SHMT2 may be a potential target for breast cancer treatment and drug discovery .

Example answer:
{"entities": [{"text": "SHMT2", "type": "Chemical"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "drug discovery", "type": "ResearchActivity"}]}

Example input:
Sentence: Further analysis results indicated that SHMT2 had better prognostic value for estrogen receptor ( ER ) - negative breast cancer patients , compared to ER - positive patients .

Example answer:
{"entities": [{"text": "SHMT2", "type": "Chemical"}, {"text": "prognostic", "type": "IntellectualProduct"}, {"text": "estrogen receptor ( ER ) - negative", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "ER - positive", "type": "Finding"}]}

Example input:
Sentence: In cases involving stage IIb breast cancer , chemotherapy significantly extended survival time among patients with high SHMT2 expression .

Example answer:
{"entities": [{"text": "stage IIb breast cancer", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "extended", "type": "SpatialConcept"}, {"text": "survival time", "type": "ClinicalAttribute"}, {"text": "SHMT2", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}]}

Example input:
Sentence: Gene set enrichment analysis revealed that SHMT2 was significantly associated with gene signatures of mitochondrial module , cancer invasion , metastasis and poor survival among breast cancer patients ( p < 0 .

Example answer:
{"entities": [{"text": "Gene set enrichment analysis", "type": "ResearchActivity"}, {"text": "SHMT2", "type": "Chemical"}, {"text": "mitochondrial module", "type": "BiologicFunction"}, {"text": "cancer invasion", "type": "Finding"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "poor survival", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: The aim of the present study was to evaluate the prognostic value and efficiency of SHMT2 as a biomarker in patients with breast cancer .

Example answer:
{"entities": [{"text": "prognostic", "type": "IntellectualProduct"}, {"text": "SHMT2", "type": "Chemical"}, {"text": "biomarker", "type": "ClinicalAttribute"}, {"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: SHMT2 protein expression was detected using immunohistochemistry ( IHC ) assay in 128 breast cancer cases .

Example answer:
{"entities": [{"text": "SHMT2", "type": "Chemical"}, {"text": "protein expression", "type": "BiologicFunction"}, {"text": "immunohistochemistry", "type": "HealthCareActivity"}, {"text": "IHC", "type": "HealthCareActivity"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: These results indicate that SHMT2 may be a valuable prognostic biomarker in ER - negative breast cancer cases .

Example answer:
{"entities": [{"text": "SHMT2", "type": "Chemical"}, {"text": "prognostic", "type": "IntellectualProduct"}, {"text": "biomarker", "type": "ClinicalAttribute"}, {"text": "ER - negative", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}]}

Input:
Sentence: Prognostic and therapeutic value of mitochondrial serine hydroxyl - methyltransferase 2 as a breast cancer biomarker Mitochondrial serine hydroxylmethyltransferase 2 ( SHMT2 ) is a key enzyme in the serine / glycine synthesis pathway .

## Item MedMentions:test:1923
Example input:
Sentence: An increase in cortical thickness at the hemisphere contralateral to the lesion ( CLH ) was detected in motor and language areas , which may reflect compensation for the gray matter loss in the lesion area or retention of ipsilateral pathways .

Example answer:
{"entities": [{"text": "cortical", "type": "AnatomicalStructure"}, {"text": "hemisphere", "type": "AnatomicalStructure"}, {"text": "contralateral", "type": "SpatialConcept"}, {"text": "lesion", "type": "Finding"}, {"text": "CLH", "type": "AnatomicalStructure"}, {"text": "detected", "type": "Finding"}, {"text": "motor", "type": "SpatialConcept"}, {"text": "language areas", "type": "SpatialConcept"}, {"text": "gray matter", "type": "AnatomicalStructure"}, {"text": "area", "type": "SpatialConcept"}, {"text": "ipsilateral", "type": "SpatialConcept"}]}

Example input:
Sentence: We mapped to atlas regions coordinates of case - control differences derived from 537 task - fMRI studies in schizophrenia , bipolar disorder , major depressive disorder , anxiety disorders , and obsessive compulsive disorder comprising observations derived from 21 , 427 participants .

Example answer:
{"entities": [{"text": "case - control", "type": "HealthCareActivity"}, {"text": "fMRI studies", "type": "HealthCareActivity"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "bipolar disorder", "type": "BiologicFunction"}, {"text": "major depressive disorder", "type": "BiologicFunction"}, {"text": "anxiety disorders", "type": "BiologicFunction"}, {"text": "obsessive compulsive disorder", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: According to changes in Her2 and ER / PgR status , 23 ( 12 . 2 % ) and 33 ( 17 . 6 % ) systemic prescription were respectively modified .

Example answer:
{"entities": [{"text": "Her2", "type": "Chemical"}, {"text": "ER", "type": "Chemical"}, {"text": "PgR", "type": "Chemical"}, {"text": "prescription", "type": "HealthCareActivity"}]}

Example input:
Sentence: TEE findings changed management ( initiation of anticoagulation therapy , administration of IV antibiotic therapy , and patent foramen ovale closure ) in 10 ( 16 % [ 95 % CI : 9 % - 28 % ] ) patients .

Example answer:
{"entities": [{"text": "TEE", "type": "HealthCareActivity"}, {"text": "findings", "type": "Finding"}, {"text": "anticoagulation therapy", "type": "HealthCareActivity"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "IV antibiotic therapy", "type": "HealthCareActivity"}, {"text": "patent foramen ovale closure", "type": "HealthCareActivity"}]}

Example input:
Sentence: FLAIR hyperintensity within the diffusion - weighted imaging ( DWI ) lesion was rated qualitatively , and HT was assessed on follow - up gradient echo imaging .

Example answer:
{"entities": [{"text": "FLAIR", "type": "HealthCareActivity"}, {"text": "hyperintensity", "type": "BiologicFunction"}, {"text": "diffusion - weighted imaging", "type": "HealthCareActivity"}, {"text": "DWI", "type": "HealthCareActivity"}, {"text": "lesion", "type": "Finding"}, {"text": "HT", "type": "BiologicFunction"}, {"text": "echo imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: Fluid - Attenuated Inversion Recovery Hyperintensity Is Associated with Hemorrhagic Transformation following Reperfusion Therapy It is still controversial whether early fluid - attenuated inversion recovery ( FLAIR ) hyperintensity within acute ischemic lesions carries the risk of hemorrhagic transformation ( HT ) after reperfusion therapy .

Example answer:
{"entities": [{"text": "Fluid - Attenuated Inversion Recovery", "type": "HealthCareActivity"}, {"text": "Hyperintensity", "type": "BiologicFunction"}, {"text": "Hemorrhagic Transformation", "type": "BiologicFunction"}, {"text": "Reperfusion Therapy", "type": "HealthCareActivity"}, {"text": "fluid - attenuated inversion recovery", "type": "HealthCareActivity"}, {"text": "FLAIR", "type": "HealthCareActivity"}, {"text": "hyperintensity", "type": "BiologicFunction"}, {"text": "ischemic", "type": "BiologicFunction"}, {"text": "lesions", "type": "Finding"}, {"text": "hemorrhagic transformation", "type": "BiologicFunction"}, {"text": "HT", "type": "BiologicFunction"}, {"text": "reperfusion therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: FLAIR change was independently associated with HT ( odds ratio : 4 .

Example answer:
{"entities": [{"text": "FLAIR", "type": "HealthCareActivity"}, {"text": "HT", "type": "BiologicFunction"}]}

Example input:
Sentence: Thus , identification of FLAIR change may be a useful surrogate marker to assess the likelihood of subsequent HT in patients treated with reperfusion therapy .

Example answer:
{"entities": [{"text": "FLAIR", "type": "HealthCareActivity"}, {"text": "HT", "type": "BiologicFunction"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "reperfusion therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: In patients in the acute stage of stroke , an early FLAIR change is associated with the risk of HT following reperfusion therapy with a highly matched geographic relationship and common risk factors .

Example answer:
{"entities": [{"text": "stroke", "type": "BiologicFunction"}, {"text": "FLAIR", "type": "HealthCareActivity"}, {"text": "HT", "type": "BiologicFunction"}, {"text": "reperfusion therapy", "type": "HealthCareActivity"}, {"text": "risk factors", "type": "Finding"}]}

Example input:
Sentence: The location of the FLAIR change and HT was classified as subcortical , cortical , or cortico - subcortical .

Example answer:
{"entities": [{"text": "FLAIR", "type": "HealthCareActivity"}, {"text": "HT", "type": "BiologicFunction"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "cortico - subcortical", "type": "SpatialConcept"}]}

Input:
Sentence: Geographically , 48 . 2 % of the patients with a FLAIR change developed a matched HT ( restricted to the region with the FLAIR change ) , and the risk of HT was further increased in patients with a FLAIR change in the cortico - subcortical region ( 68 . 8 % ) .

## Item MedMentions:test:2166
Example input:
Sentence: Sexual abstinence was found in 162 women ( 45 % ) .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Of these , 63 patients reported no sexual activity in the last month and thus were analyzed only in relation to the sexual desire domain of FSFI .

Example answer:
{"entities": [{"text": "sexual desire", "type": "BiologicFunction"}, {"text": "FSFI", "type": "IntellectualProduct"}]}

Example input:
Sentence: A total of 4 , 267 patients were included in the analysis .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: 167 patients were included in the study .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Totally 174 patients were enrolled to the study ( 152 male , 22 female ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "male", "type": "PopulationGroup"}, {"text": "female", "type": "PopulationGroup"}]}

Example input:
Sentence: The study included 275 patients .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: A total of 346 patients were included in the study .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: From those patients reporting sexual activity in the last month , 63 . 3 % ( 97 out of 153 ) were classified with sexual dysfunction .

Example answer:
{"entities": [{"text": "sexual dysfunction", "type": "BiologicFunction"}]}

Example input:
Sentence: A total of 144 , 098 patients met the study criteria .

Example answer:
{"entities": []}

Example input:
Sentence: Sex life is a relevant consideration for the majority of patients with DS and SPS ; operative treatment leads to improved sex life - related pain .

Example answer:
{"entities": [{"text": "DS", "type": "BiologicFunction"}, {"text": "SPS", "type": "AnatomicalStructure"}, {"text": "improved", "type": "Finding"}, {"text": "sex life - related pain", "type": "Finding"}]}

Input:
Sentence: A total of 1235 patients were included to determine relevance of sex life .

## Item MedMentions:test:2246
Example input:
Sentence: 23 , moderate , z = 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 68 ( 0 . 11 ) and 0 . 87 ( 0 . 16 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 47 - 2 . 60 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 53 and 20 .

Example answer:
{"entities": []}

Example input:
Sentence: 48 h , AUC 0 - 12 202 .

Example answer:
{"entities": []}

Example input:
Sentence: 90±6 . 86 µg / ml at 24 and 48 h , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 9 mM after 24 and 48 h , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 47 to 72 .

Example answer:
{"entities": []}

Example input:
Sentence: 28 and 34 .

Example answer:
{"entities": []}

Example input:
Sentence: 48 % after 48 h .

Example answer:
{"entities": []}

Input:
Sentence: 48 ) at mid .

## Item MedMentions:test:1936
Example input:
Sentence: Prognostic significance of blood pressure response during vasodilator stress Rb - 82 positron emission tomography myocardial perfusion imaging A drop in blood pressure ( BP ) or blunted BP response is an established high - risk marker during exercise myocardial perfusion imaging ( MPI ) ; however , data are sparse regarding the prognostic value of BP response in patients undergoing vasodilator stress rubidium - 82 ( Rb - 82 ) Positron Emission Tomography ( PET ) MPI .

Example answer:
{"entities": [{"text": "Prognostic", "type": "IntellectualProduct"}, {"text": "blood pressure response", "type": "ClinicalAttribute"}, {"text": "vasodilator stress Rb - 82 positron emission tomography myocardial perfusion imaging", "type": "HealthCareActivity"}, {"text": "blood pressure", "type": "BiologicFunction"}, {"text": "BP", "type": "BiologicFunction"}, {"text": "myocardial perfusion imaging", "type": "HealthCareActivity"}, {"text": "MPI", "type": "HealthCareActivity"}, {"text": "prognostic", "type": "IntellectualProduct"}, {"text": "vasodilator stress rubidium - 82 ( Rb - 82 ) Positron Emission Tomography ( PET ) MPI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Women who experienced all four stressor categories , including partner related , traumatic , emotional , and financial , had the highest odds ( adjusted odds ratio [ aOR ] : 5 . 43 ; 95 % confidence interval [ CI ] : 5 . 36 - 5 . 51 ) of PPD symptoms .

Example answer:
{"entities": [{"text": "Women", "type": "PopulationGroup"}, {"text": "categories", "type": "IntellectualProduct"}, {"text": "partner", "type": "PopulationGroup"}, {"text": "related", "type": "Finding"}, {"text": "emotional", "type": "Finding"}, {"text": "PPD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: The results suggest that baseline ASR has value as a predictive index of the development of a PTSD -like phenotype .

Example answer:
{"entities": [{"text": "ASR", "type": "BiologicFunction"}, {"text": "index", "type": "IntellectualProduct"}, {"text": "development", "type": "BiologicFunction"}, {"text": "PTSD", "type": "BiologicFunction"}]}

Example input:
Sentence: With HML , peak power output ( P = 0 . 035 ) , maximal heart rate ( P < 0 . 01 ) and gain of force measured in the chest press position ( P < 0 . 02 ) were greater after versus before training .

Example answer:
{"entities": [{"text": "heart rate", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Service members with combat - related PTSD were randomly selected to receive nine weeks of VRET or CET .

Example answer:
{"entities": [{"text": "members", "type": "PopulationGroup"}, {"text": "combat - related PTSD", "type": "BiologicFunction"}, {"text": "VRET", "type": "HealthCareActivity"}, {"text": "CET", "type": "HealthCareActivity"}]}

Example input:
Sentence: Covariates included age , pre - deployment PCL , race / ethnicity , marital status , tobacco use , childhood abuse , pre - deployment traumatic brain injury , and previous combat zone deployment .

Example answer:
{"entities": [{"text": "PCL", "type": "IntellectualProduct"}, {"text": "race", "type": "PopulationGroup"}, {"text": "ethnicity", "type": "PopulationGroup"}, {"text": "childhood abuse", "type": "BiologicFunction"}, {"text": "traumatic brain injury", "type": "InjuryOrPoisoning"}, {"text": "combat zone", "type": "SpatialConcept"}]}

Example input:
Sentence: Pre - deployment SDNN was not a significant predictor of post - deployment PCL .

Example answer:
{"entities": [{"text": "PCL", "type": "IntellectualProduct"}]}

Example input:
Sentence: The primary outcome was PTSD symptom severity using the PTSD Checklist - Military version ( PCL ) measured at baseline , 3 - and 12 - month post - deployment .

Example answer:
{"entities": [{"text": "PTSD", "type": "BiologicFunction"}, {"text": "symptom", "type": "Finding"}, {"text": "Checklist", "type": "IntellectualProduct"}, {"text": "Military", "type": "ProfessionalOrOccupationalGroup"}, {"text": "version", "type": "IntellectualProduct"}, {"text": "PCL", "type": "IntellectualProduct"}]}

Example input:
Sentence: This study hypothesized that lower pre - deployment HRV would be associated with higher post - deployment post - traumatic stress disorder ( PTSD ) symptoms .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "HRV", "type": "BiologicFunction"}, {"text": "post - traumatic stress disorder", "type": "BiologicFunction"}, {"text": "PTSD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: Heart rate variability : Pre - deployment predictor of post - deployment PTSD symptoms Heart rate variability is a physiological measure associated with autonomic nervous system activity .

Example answer:
{"entities": [{"text": "Heart rate", "type": "ClinicalAttribute"}, {"text": "PTSD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "autonomic nervous system", "type": "BodySystem"}]}

Input:
Sentence: Pre - deployment heart rate variability predicts post - deployment PTSD symptoms in the context of higher pre - deployment PCL scores .

## Item MedMentions:test:1454
Example input:
Sentence: Reliability of 30 - Day Readmission Measures Used in the Hospital Readmission Reduction Program To assess the reliability of risk - standardized readmission rates ( RSRRs ) for medical conditions and surgical procedures used in the Hospital Readmission Reduction Program ( HRRP ) .

Example answer:
{"entities": [{"text": "Readmission Measures", "type": "HealthCareActivity"}, {"text": "surgical procedures", "type": "HealthCareActivity"}]}

Example input:
Sentence: The experts reached consensus on the following criteria to support the RTP decision : medical staff clearance , absence of pain on palpation , absence of pain during strength and flexibility testing , absence of pain during / after functional testing , similar hamstring flexibility , performance on field testing , and psychological readiness .

Example answer:
{"entities": [{"text": "experts", "type": "ProfessionalOrOccupationalGroup"}, {"text": "decision", "type": "BiologicFunction"}, {"text": "medical staff", "type": "ProfessionalOrOccupationalGroup"}, {"text": "absence of pain", "type": "Finding"}, {"text": "palpation", "type": "HealthCareActivity"}, {"text": "hamstring", "type": "AnatomicalStructure"}, {"text": "field", "type": "SpatialConcept"}, {"text": "readiness", "type": "Finding"}]}

Example input:
Sentence: Demonstration and validation of a new pressure -based MRI -safe pain tolerance device One of the barriers to studying the behavioral and emotional effects of pain using functional Magnetic Resonance Imaging ( fMRI ) is the absence of a commercially available , MRI - compatible , pressure -based algometer to elicit pain .

Example answer:
{"entities": [{"text": "validation", "type": "ResearchActivity"}, {"text": "MRI", "type": "MedicalDevice"}, {"text": "pain tolerance", "type": "Finding"}, {"text": "device", "type": "MedicalDevice"}, {"text": "emotional", "type": "BiologicFunction"}, {"text": "pain", "type": "Finding"}, {"text": "functional Magnetic Resonance Imaging", "type": "HealthCareActivity"}, {"text": "fMRI", "type": "HealthCareActivity"}, {"text": "algometer", "type": "MedicalDevice"}]}

Example input:
Sentence: A few major findings of this study were : ( a ) leakage , is not a strong function of sub - micron aerosol size ; ( b ) for the same gap size , leakage of aerosols through surgical respirators can often be higher than in SMs and FPUs ; and ( c ) as the gap size increases , the increase in leakage through surgical respirators is higher compared for SMs and FPUs , implying that some SMs and FPUs that possess electret layers may be preferable to N95s that have not been fit - tested .

Example answer:
{"entities": [{"text": "leakage", "type": "Finding"}, {"text": "size", "type": "SpatialConcept"}, {"text": "gap size", "type": "SpatialConcept"}, {"text": "SMs", "type": "MedicalDevice"}, {"text": "FPUs", "type": "MedicalDevice"}]}

Example input:
Sentence: However , with the possibility of new or re - emerging airborne diseases or bio - aerosol weapons lingering , combined with the limited availability of respirators and logistical issues associated with fit - testing millions , the general adult and pediatric populations may elect to wear SMs and FPUs , respectively , in the case of a pandemic or a bio - terrorist attack .

Example answer:
{"entities": [{"text": "diseases", "type": "BiologicFunction"}, {"text": "bio - aerosol weapons lingering", "type": "InjuryOrPoisoning"}, {"text": "respirators", "type": "MedicalDevice"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "elect to wear", "type": "Finding"}, {"text": "SMs", "type": "MedicalDevice"}, {"text": "FPUs", "type": "MedicalDevice"}]}

Example input:
Sentence: While N95s including surgical respirators have been routinely studied , SMs and FPUs have not received as much attention , particularly in the context of aerosolized threats .

Example answer:
{"entities": [{"text": "SMs", "type": "MedicalDevice"}, {"text": "FPUs", "type": "MedicalDevice"}, {"text": "attention", "type": "BiologicFunction"}]}

Example input:
Sentence: The significance of developing such an instrument is that it will help identify respirators that are likely to have better adherence in practice settings .

Example answer:
{"entities": [{"text": "instrument", "type": "MedicalDevice"}, {"text": "practice", "type": "BiologicFunction"}]}

Example input:
Sentence: Until now , to our knowledge no instrument with evidence supporting its reliability and validity to assess discomfort and tolerance of FFRs among health care personnel has been published .

Example answer:
{"entities": [{"text": "knowledge", "type": "BiologicFunction"}, {"text": "instrument", "type": "MedicalDevice"}, {"text": "discomfort", "type": "Finding"}, {"text": "health care personnel", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: The R - COMFI may be used within and beyond the VA healthcare system as a psychometrically sound instrument to evaluate the comfort and tolerability of respirators , including developmental prototypes .

Example answer:
{"entities": [{"text": "R - COMFI", "type": "MedicalDevice"}, {"text": "within", "type": "SpatialConcept"}, {"text": "VA healthcare system", "type": "Organization"}, {"text": "psychometrically sound instrument", "type": "MedicalDevice"}, {"text": "comfort", "type": "BiologicFunction"}]}

Example input:
Sentence: A 21 - item psychometrically sound measure of comfort and tolerability of FFRs , Respirator Comfort , Wearing Experience , and Function Instrument ( R - COMFI ) , was developed .

Example answer:
{"entities": [{"text": "comfort", "type": "BiologicFunction"}, {"text": "Comfort", "type": "BiologicFunction"}, {"text": "Wearing Experience", "type": "BiologicFunction"}, {"text": "Instrument", "type": "MedicalDevice"}, {"text": "R - COMFI", "type": "MedicalDevice"}]}

Input:
Sentence: Development and initial validation of the Respirator Comfort , Wearing Experience , and Function Instrument [ R - COMFI Filtering face - piece respirators ( FFRs ) are worn to protect health care personnel from airborne particles ; however , clinical studies have demonstrated that FFR adherence is relatively low in some settings , in part , due to discomfort and intolerance .

## Item MedMentions:test:2248
Example input:
Sentence: 14 ± 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 1 ± 7 .

Example answer:
{"entities": []}

Example input:
Sentence: 31 . 96 ± 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 2 ± 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 6 ± 7 .

Example answer:
{"entities": []}

Example input:
Sentence: 6 ± 7 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 ± 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 9 ± 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 9 ± 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 6 ± 0 .

Example answer:
{"entities": []}

Input:
Sentence: 1 ± 6 .

## Item MedMentions:test:2031
Example input:
Sentence: Stimulation of cell proliferation by glutathione monoethyl ester in aged bone marrow stromal cells is associated with the assistance of TERT gene expression and telomerase activity The proliferation and differentiation potential of aged bone marrow stromal cells ( BMSCs ) are significantly reduced .

Example answer:
{"entities": [{"text": "cell proliferation", "type": "BiologicFunction"}, {"text": "glutathione monoethyl ester", "type": "Chemical"}, {"text": "aged bone marrow stromal cells", "type": "AnatomicalStructure"}, {"text": "TERT", "type": "AnatomicalStructure"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "telomerase activity", "type": "BiologicFunction"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "differentiation", "type": "BiologicFunction"}, {"text": "BMSCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Ageing results from the time - dependent accumulation of random cellular damage .

Example answer:
{"entities": [{"text": "Ageing", "type": "BiologicFunction"}, {"text": "accumulation", "type": "Finding"}]}

Example input:
Sentence: Neurobiological adaptations , including transcriptional and epigenetic alterations in the nucleus accumbens , are thought to contribute to this life - long disease state .

Example answer:
{"entities": [{"text": "Neurobiological adaptations", "type": "BiologicFunction"}, {"text": "transcriptional", "type": "BiologicFunction"}, {"text": "epigenetic alterations", "type": "BiologicFunction"}, {"text": "nucleus accumbens", "type": "AnatomicalStructure"}, {"text": "life - long disease state", "type": "Finding"}]}

Example input:
Sentence: Epigenetic modifications and mitochondrial DNA haplogroups modulate ageing .

Example answer:
{"entities": [{"text": "Epigenetic modifications", "type": "BiologicFunction"}, {"text": "mitochondrial DNA", "type": "Chemical"}, {"text": "modulate", "type": "SpatialConcept"}, {"text": "ageing", "type": "BiologicFunction"}]}

Example input:
Sentence: However , a synthesis of research shows successful aging can be defined as a late - life process of change characterized by high physical , psychological , cognitive , and social functioning .

Example answer:
{"entities": [{"text": "successful aging", "type": "BiologicFunction"}, {"text": "late - life process of change", "type": "BiologicFunction"}, {"text": "high physical", "type": "Finding"}, {"text": "psychological", "type": "BiologicFunction"}, {"text": "cognitive", "type": "BiologicFunction"}]}

Example input:
Sentence: DNA methylation undergoes a profound remodeling during aging , which includes global hypomethylation of the genome , hypermethylation at specific loci and an increase in inter - individual variation and in stochastic changes of DNA methylation values .

Example answer:
{"entities": [{"text": "DNA methylation", "type": "BiologicFunction"}, {"text": "aging", "type": "BiologicFunction"}, {"text": "global hypomethylation", "type": "BiologicFunction"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "hypermethylation", "type": "BiologicFunction"}, {"text": "loci", "type": "AnatomicalStructure"}]}

Example input:
Sentence: However , cells driven deep within the phase boundary form solid - like gels that undergo aging into irreversible aggregates .

Example answer:
{"entities": [{"text": "cells", "type": "AnatomicalStructure"}, {"text": "solid - like gels", "type": "Chemical"}]}

Example input:
Sentence: Extracellular and whole - cell recordings from acute hippocampal slices of aged Wistar rats ( 34 ± 2 months old ) show that aging is accompanied by a reduction in the interneuron -mediated inhibitory mechanisms of area CA3 .

Example answer:
{"entities": [{"text": "Extracellular", "type": "AnatomicalStructure"}, {"text": "whole - cell recordings", "type": "ResearchActivity"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "Wistar rats", "type": "Eukaryote"}, {"text": "aging", "type": "BiologicFunction"}, {"text": "interneuron", "type": "AnatomicalStructure"}, {"text": "area CA3", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Together , these results demonstrate that aging is accompanied by a decrease in the GABAergic inhibition , reduced expression of short - and long - term forms of synaptic plasticity , and increased intrinsic excitability .

Example answer:
{"entities": [{"text": "aging", "type": "BiologicFunction"}, {"text": "GABAergic inhibition", "type": "BiologicFunction"}, {"text": "synaptic plasticity", "type": "BiologicFunction"}, {"text": "increased intrinsic excitability", "type": "Finding"}]}

Example input:
Sentence: Several MF -mediated forms of short - term plasticity , MF long - term potentiation and at least one of the critical signaling cascades necessary for potentiation are also compromised in the aged brain .

Example answer:
{"entities": [{"text": "MF", "type": "AnatomicalStructure"}, {"text": "plasticity", "type": "BiologicFunction"}, {"text": "long - term potentiation", "type": "BiologicFunction"}, {"text": "critical signaling cascades", "type": "BiologicFunction"}, {"text": "aged brain", "type": "AnatomicalStructure"}]}

Input:
Sentence: At the cellular level , aging is accompanied by a progression of biochemical modifications that ultimately affects its ability to generate and consolidate long - term potentiation .
