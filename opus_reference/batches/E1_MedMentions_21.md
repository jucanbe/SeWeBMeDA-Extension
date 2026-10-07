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

## Item MedMentions:test:4221
Example input:
Sentence: 0 , 2 . 0 ) .

Example answer:
{"entities": []}

Example input:
Sentence: s . ) .

Example answer:
{"entities": []}

Example input:
Sentence: A .

Example answer:
{"entities": []}

Example input:
Sentence: A .

Example answer:
{"entities": [{"text": "A .", "type": "Bacterium"}]}

Example input:
Sentence: A .

Example answer:
{"entities": [{"text": "A .", "type": "Eukaryote"}]}

Example input:
Sentence: A .

Example answer:
{"entities": [{"text": "A .", "type": "Bacterium"}]}

Example input:
Sentence: A .

Example answer:
{"entities": [{"text": "A .", "type": "Eukaryote"}]}

Example input:
Sentence: A .

Example answer:
{"entities": [{"text": "A .", "type": "Eukaryote"}]}

Example input:
Sentence: S . and a U .

Example answer:
{"entities": [{"text": "S .", "type": "SpatialConcept"}, {"text": "U .", "type": "SpatialConcept"}]}

Example input:
Sentence: 1 , 2 . 0 , and 1 .

Example answer:
{"entities": []}

Input:
Sentence: .

## Item MedMentions:test:4024
Example input:
Sentence: These patients had significantly higher PSA , PSAd and IGF - 1 values and a tendency towards higher internal organ fat levels and lower % PSA readings ( p = . 001 , p = .

Example answer:
{"entities": [{"text": "PSA", "type": "Chemical"}, {"text": "PSAd", "type": "Chemical"}, {"text": "IGF - 1", "type": "Chemical"}, {"text": "internal organ fat", "type": "ClinicalAttribute"}, {"text": "lower", "type": "SpatialConcept"}]}

Example input:
Sentence: Patients with PsA had a small but significant increase in SMR for death due to diseases of the circulatory system compared with the general population .

Example answer:
{"entities": [{"text": "PsA", "type": "BiologicFunction"}, {"text": "death", "type": "Finding"}, {"text": "diseases of the circulatory system", "type": "BiologicFunction"}, {"text": "general population", "type": "PopulationGroup"}]}

Example input:
Sentence: Main Outcomes and Measures : Body composition ( Dual Energy X - ray Absorptiometry ) and metabolic parameters were compared in PWS adults ( mean age , 25 . 5 ± 8 . 9 y ) with deletion ( n = 47 ) or uniparental disomy ( UPD ) ( n = 26 ) , taking into account GH treatment in childhood and / or adolescence .

Example answer:
{"entities": [{"text": "Dual Energy X - ray Absorptiometry", "type": "HealthCareActivity"}, {"text": "metabolic parameters", "type": "Finding"}, {"text": "PWS", "type": "AnatomicalStructure"}, {"text": "deletion", "type": "BiologicFunction"}, {"text": "uniparental disomy", "type": "BiologicFunction"}, {"text": "UPD", "type": "BiologicFunction"}]}

Example input:
Sentence: On univariate analysis , variables associated with worse survival included : clinical stage IIIB ( p = 0 . 037 ) , planning target volume ( PTV ) over 450 cc ( p < 0 . 001 ) , heart V30 over 40 % ( p = -0 . 048 ) , and esophageal mean dose over 20 % ( p = 0 . 024 ) , V5 ( p = -0 . 015 ) , and V60 ( p = -0 . 011 ) .

Example answer:
{"entities": [{"text": "worse", "type": "Finding"}, {"text": "stage IIIB", "type": "BiologicFunction"}, {"text": "heart", "type": "AnatomicalStructure"}, {"text": "esophageal", "type": "SpatialConcept"}]}

Example input:
Sentence: For THA patients there was no difference in LOS , OHS score was two points lower for each increasing BMI category and postoperative problems increase from 25 % for non - obese to 31 % for obese and 38 % for morbidly obese patients .

Example answer:
{"entities": [{"text": "THA", "type": "HealthCareActivity"}, {"text": "OHS score", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "category", "type": "IntellectualProduct"}, {"text": "postoperative problems", "type": "BiologicFunction"}, {"text": "obese", "type": "BiologicFunction"}, {"text": "morbidly obese", "type": "BiologicFunction"}]}

Example input:
Sentence: BMI was also an independent prognostic factor for OS in multivariate analysis ( HR 0 . 541 ; 95 % CI 0 .

Example answer:
{"entities": [{"text": "BMI", "type": "ClinicalAttribute"}, {"text": "prognostic factor", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Here , we report the clinical impact of the change , from baseline , in nutritional status and volume of abdominal skeletal muscle mass and adipose tissue after radical cystetomy .

Example answer:
{"entities": [{"text": "report", "type": "HealthCareActivity"}, {"text": "nutritional status", "type": "Finding"}, {"text": "abdominal", "type": "SpatialConcept"}, {"text": "skeletal muscle", "type": "AnatomicalStructure"}, {"text": "adipose tissue", "type": "AnatomicalStructure"}, {"text": "radical cystetomy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Body weight changes can be recognized as a prognostic factor for PFS and OS in advanced EOC patients undergoing chemotherapy .

Example answer:
{"entities": [{"text": "Body weight changes", "type": "Finding"}, {"text": "prognostic factor", "type": "ClinicalAttribute"}, {"text": "EOC", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Clinical impact of postoperative loss in psoas major muscle and nutrition index after radical cystectomy for patients with urothelial carcinoma of the bladder Although the significance of preoperative nutritional status has been investigated , there is no report regarding the relationship of their postoperative changes on outcomes in patients who underwent radical cystectomy for bladder cancer .

Example answer:
{"entities": [{"text": "postoperative loss", "type": "BiologicFunction"}, {"text": "psoas major muscle", "type": "AnatomicalStructure"}, {"text": "radical cystectomy", "type": "HealthCareActivity"}, {"text": "urothelial carcinoma", "type": "BiologicFunction"}, {"text": "bladder", "type": "AnatomicalStructure"}, {"text": "nutritional status", "type": "Finding"}, {"text": "report", "type": "IntellectualProduct"}, {"text": "postoperative changes", "type": "BiologicFunction"}, {"text": "bladder cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Multivariate analyzes identified sarcopenia status at baseline ( HR 2 . 2 , P = 0 . 03 ) and a ≤ -10 % loss in the psoas muscle ( HR 2 . 4 , P = 0 .

Example answer:
{"entities": [{"text": "sarcopenia", "type": "BiologicFunction"}, {"text": "psoas muscle", "type": "AnatomicalStructure"}]}

Input:
Sentence: A subanalysis of patients without sarcopenia identified a worse survival outcome for patients with a ≤ -10 % loss in the psoas muscle ( HR 2 . 6 , P = 0 . 03 ) and ≤ - 5 change in the Prognostic Nutritional Index ( HR 3 . 6 , P = 0 .

## Item MedMentions:test:3932
Example input:
Sentence: Furthermore , the potential energy -dependent Pareto fronts were calculated to elucidate dissimilarities between peptide conformations and the native state as observed by x - ray crystallography .

Example answer:
{"entities": [{"text": "potential energy -dependent Pareto fronts", "type": "Finding"}, {"text": "peptide conformations", "type": "SpatialConcept"}, {"text": "x - ray crystallography", "type": "HealthCareActivity"}]}

Example input:
Sentence: In addition , improved mitochondrial function primarily enhancing nicotinamide adenine dinucleotide ( NADH ) generated enzymes activities and ATP level in the mitochondria .

Example answer:
{"entities": [{"text": "improved", "type": "Finding"}, {"text": "mitochondrial function", "type": "BiologicFunction"}, {"text": "nicotinamide adenine dinucleotide", "type": "Chemical"}, {"text": "NADH", "type": "Chemical"}, {"text": "enzymes activities", "type": "BiologicFunction"}, {"text": "ATP", "type": "Chemical"}, {"text": "mitochondria", "type": "AnatomicalStructure"}]}

Example input:
Sentence: As a result , in solution PEI exhibits multiple buffering mechanisms , and polyelectrolyte states that shift between aggregated and free forms .

Example answer:
{"entities": [{"text": "PEI", "type": "Chemical"}, {"text": "buffering", "type": "Chemical"}, {"text": "polyelectrolyte states", "type": "Chemical"}]}

Example input:
Sentence: Increase of hydrophobic and π - π stacking interactions led to the decrease of pKa values .

Example answer:
{"entities": [{"text": "hydrophobic", "type": "BiologicFunction"}]}

Example input:
Sentence: Intriguingly , the two amino acid residues K92 and D228 , interacting with the triphosphate group of ATP , are donated from atypical positions in the primary structure .

Example answer:
{"entities": [{"text": "amino acid residues K92", "type": "SpatialConcept"}, {"text": "D228", "type": "SpatialConcept"}, {"text": "triphosphate group of ATP", "type": "Chemical"}, {"text": "primary structure", "type": "SpatialConcept"}]}

Example input:
Sentence: Using the X - ray crystal structure as a starting point , we have modeled the motions of a DNA duplex built from a self - complementary oligonucleotide ( 5΄ - CTTATPPPZZZATAAG - 3΄ ) in water over a period of 50 μs and calculated DNA local parameters , step parameters , helix parameters , and major / minor groove widths to examine how the presence of multiple , consecutive nucleobase pairs might impact helical structure .

Example answer:
{"entities": [{"text": "X - ray crystal structure", "type": "HealthCareActivity"}, {"text": "DNA", "type": "Chemical"}, {"text": "duplex", "type": "SpatialConcept"}, {"text": "self - complementary oligonucleotide", "type": "Chemical"}, {"text": "5΄ - CTTATPPPZZZATAAG - 3΄", "type": "Chemical"}, {"text": "water", "type": "Chemical"}, {"text": "calculated", "type": "HealthCareActivity"}, {"text": "local", "type": "SpatialConcept"}, {"text": "major", "type": "Chemical"}, {"text": "minor groove", "type": "Chemical"}, {"text": "presence", "type": "Finding"}, {"text": "helical structure", "type": "SpatialConcept"}]}

Example input:
Sentence: KlacPNPN256D not only displayed broad substrate specificity by utilizing both 6 - oxopurines and 6 - aminopurines in the order adenosine > inosine > xanthosine > guanosine , but also displayed reversal of substrate specificity .

Example answer:
{"entities": [{"text": "KlacPNPN256D", "type": "Chemical"}, {"text": "6 - oxopurines", "type": "Chemical"}, {"text": "6 - aminopurines", "type": "Chemical"}, {"text": "adenosine", "type": "Chemical"}, {"text": "inosine", "type": "Chemical"}, {"text": "xanthosine", "type": "Chemical"}, {"text": "guanosine", "type": "Chemical"}]}

Example input:
Sentence: We introduce a method by which we can examine the relationship between our measure of the efficiency of natural selection , the nonsynonymous relative to the synonymous nucleotide site diversity ( πN / πS ) , and synonymous nucleotide diversity ( πS ) , avoiding the statistical non - independence between the two quantities .

Example answer:
{"entities": [{"text": "method", "type": "IntellectualProduct"}, {"text": "nonsynonymous", "type": "SpatialConcept"}, {"text": "synonymous nucleotide site diversity", "type": "SpatialConcept"}, {"text": "πN", "type": "SpatialConcept"}, {"text": "πS", "type": "SpatialConcept"}, {"text": "synonymous nucleotide diversity", "type": "SpatialConcept"}]}

Example input:
Sentence: In these simulations , the - containing DNA duplex exhibits a significantly wider major groove and greater average values of stagger , slide , rise , twist and h - rise than observed for a ' control ' oligonucleotide in which nucleobase pairs are replaced by .

Example answer:
{"entities": [{"text": "DNA", "type": "Chemical"}, {"text": "duplex", "type": "SpatialConcept"}, {"text": "wider", "type": "SpatialConcept"}, {"text": "major groove", "type": "Chemical"}, {"text": "twist", "type": "SpatialConcept"}, {"text": "oligonucleotide", "type": "Chemical"}]}

Example input:
Sentence: Consecutive non - natural PZ nucleobase pairs in DNA impact helical structure as seen in 50 μs molecular dynamics simulations Little is known about the influence of multiple consecutive ' non - standard ' ( , 6 - amino - 5 - nitro - 2 ( 1H ) - pyridone , and , 2 - amino - imidazo [ 1 , 2 - a ] - 1 , 3 , 5 - triazin - 4 ( 8H ) - one ) nucleobase pairs on the structural parameters of duplex DNA .

Example answer:
{"entities": [{"text": "DNA", "type": "Chemical"}, {"text": "helical structure", "type": "SpatialConcept"}, {"text": "structural", "type": "SpatialConcept"}, {"text": "duplex", "type": "SpatialConcept"}]}

Input:
Sentence: Second , differences are seen in the base stacking of pairs in dinucleotide steps , arising from energetically favorable stacking of the nitro group in with π - electrons of the adjacent base .

## Item MedMentions:test:4096
Example input:
Sentence: In the exploratory analysis , patients with DOR ≥12 months ( n = 287 ) or ≥24 months ( n = 133 ) were more likely to experience grade 3 / 4 AEs than the overall population .

Example answer:
{"entities": [{"text": "exploratory analysis", "type": "ResearchActivity"}, {"text": "AEs", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: 95 % confidence interval : 1 . 710 - 6 . 248 ; HR : 2 . 295 , 95 % confidence interval : 1 . 217 - 4 . 331 , respectively ) than those with an AAPR ≥ 0 . 447 .

Example answer:
{"entities": []}

Example input:
Sentence: On MVA , older age ( hazard ratio [ HR ] , 1 . 317 ; 95 % confidence interval [ CI ] , 1 . 137 - 1 . 526 ) , € ‰ ‰   € ‰1 comorbidity ( HR , 1 . 587 ; 95 % CI , 1 . 379 - 1 . 827 ) , distant metastasis ( HR , 1 . 385 ; 95 % CI , 1 . 216 - 1 . 578 ) , receipt of systemic therapy ( HR , 0 . 637 ; 95 % CI , 0 . 547 - 0 . 742 ) , and receipt of RT compared with no RT ( < 45 grays [ Gy ] : HR , 0 . 843 ; 95 % CI , 0 . 718 - 0 .

Example answer:
{"entities": [{"text": "older age", "type": "PopulationGroup"}, {"text": "distant metastasis", "type": "ClinicalAttribute"}, {"text": "systemic therapy", "type": "HealthCareActivity"}, {"text": "RT", "type": "IntellectualProduct"}]}

Example input:
Sentence: Patients in the PR group had a lower 30 - day mortality rate , despite similar Injury Severity Scores ( 13 % vs 28 % ; p = 0 . 06 ) .

Example answer:
{"entities": [{"text": "PR", "type": "HealthCareActivity"}, {"text": "group", "type": "PopulationGroup"}, {"text": "Injury Severity Scores", "type": "IntellectualProduct"}]}

Example input:
Sentence: Patients ' disease - and recurrence - free survival after ISR and APR were similar ( p = 0 . 2872 and p = 0 .

Example answer:
{"entities": [{"text": "disease", "type": "BiologicFunction"}, {"text": "recurrence - free survival", "type": "ClinicalAttribute"}, {"text": "ISR", "type": "HealthCareActivity"}, {"text": "APR", "type": "HealthCareActivity"}]}

Example input:
Sentence: 73 m ( 2 ) ; hazard ratios 0 . 57 ( 95 % CI , 0 . 43 - 0 . 76 ) , 0 . 57 ( 95 % CI , 0 . 51 - 0 . 64 ) , 0 . 48 ( 95 % CI , 0 . 44 - 0 . 54 ) , 0 . 60 ( 95 % CI , 0 . 45 - 0 . 80 ) in patients with eGFR ≥90 , 60 to 89 , 30 to 59 , and 15 to 29 mL / min per 1 .

Example answer:
{"entities": [{"text": "eGFR", "type": "HealthCareActivity"}]}

Example input:
Sentence: Disease progression despite PRRT was associated with shorter survival ( median OS 15 vs 53 mo , P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "Disease progression", "type": "BiologicFunction"}, {"text": "PRRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients ≥70 had an increased risk of death at 3 months following CRT ( odds ratio 5 . 19 , 95 % CI 1 . 64 - 16 . 41 ; p = 0 . 005 ) and worse survival over time ( hazard ratio 2 .

Example answer:
{"entities": [{"text": "death", "type": "Finding"}, {"text": "CRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: An AAPR less than 0 . 447 was significantly associated with a higher lactate dehydrogenase ( LDH ) level ( 273 vs .

Example answer:
{"entities": [{"text": "lactate dehydrogenase ( LDH ) level", "type": "Finding"}]}

Example input:
Sentence: Multivariable analysis revealed that female [ hazard ratio ( HR ) = 0 . 78 ] , adenocarcinoma ( HR = 0 . 77 ) , locoregional ( only ) recurrence ( HR = 0 . 59 ) and longer recurrence -free survival ( HR = 0 . 99 ) were favourably associated with PRS .

Example answer:
{"entities": [{"text": "adenocarcinoma", "type": "BiologicFunction"}, {"text": "locoregional ( only ) recurrence", "type": "BiologicFunction"}, {"text": "longer recurrence -free survival", "type": "Finding"}]}

Input:
Sentence: Additionally , patients with an AAPR < 0 . 447 had a shorter overall survival and progression - free survival ( hazard ratio : 3 .

## Item MedMentions:test:3869
Example input:
Sentence: Real - time PCR and Western blotting experiments further showed that the expression of Hoxd13 was significantly lower when miR - 193 was highly expressed in rat intestinal epithelial cells .

Example answer:
{"entities": [{"text": "Real - time PCR", "type": "ResearchActivity"}, {"text": "Western blotting experiments", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Hoxd13", "type": "Chemical"}, {"text": "miR - 193", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "rat", "type": "Eukaryote"}, {"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "epithelial cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Identification of MiR - 21 - 5p as a Functional Regulator of Mesothelin Expression Using MicroRNA Capture Affinity Coupled with Next Generation Sequencing MicroRNAs ( miRNAs ) are small non - coding RNAs that regulate mRNA expression mainly by silencing target transcripts via binding to miRNA recognition elements ( MREs ) in the 3 ' untranslated region ( 3 ' UTR ) .

Example answer:
{"entities": [{"text": "MiR - 21 - 5p", "type": "Chemical"}, {"text": "Functional Regulator", "type": "AnatomicalStructure"}, {"text": "Mesothelin", "type": "AnatomicalStructure"}, {"text": "Expression", "type": "BiologicFunction"}, {"text": "MicroRNA", "type": "Chemical"}, {"text": "Next Generation Sequencing", "type": "ResearchActivity"}, {"text": "MicroRNAs", "type": "Chemical"}, {"text": "miRNAs", "type": "Chemical"}, {"text": "small non - coding RNAs", "type": "Chemical"}, {"text": "regulate", "type": "BiologicFunction"}, {"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "silencing", "type": "BiologicFunction"}, {"text": "transcripts", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "miRNA recognition elements ( MREs )", "type": "SpatialConcept"}, {"text": "3 ' untranslated region", "type": "SpatialConcept"}, {"text": "3 ' UTR", "type": "SpatialConcept"}]}

Example input:
Sentence: In this study , miR - 708 was identified to be enriched in the neonatal cardiomyocytes of rats , but this has not yet been proven in adult humans .

Example answer:
{"entities": [{"text": "miR - 708", "type": "Chemical"}, {"text": "cardiomyocytes", "type": "AnatomicalStructure"}, {"text": "rats", "type": "Eukaryote"}, {"text": "humans", "type": "Eukaryote"}]}

Example input:
Sentence: Interestingly , one of the identified miRNAs ( miR - 101b ) is highly conserved between rat and human and was recently found to be downregulated in the PFC of depressed suicide subjects .

Example answer:
{"entities": [{"text": "miRNAs", "type": "AnatomicalStructure"}, {"text": "miR - 101b", "type": "AnatomicalStructure"}, {"text": "rat", "type": "Eukaryote"}, {"text": "human", "type": "Eukaryote"}, {"text": "downregulated", "type": "BiologicFunction"}, {"text": "PFC", "type": "AnatomicalStructure"}, {"text": "depressed", "type": "Finding"}, {"text": "suicide", "type": "Finding"}]}

Example input:
Sentence: A miRNA expression assay that can simultaneously detect 423 rat miRNAs ( miRBase v . 17 ) was used to profile the prefrontal cortex ( PFC ) of a genetic rat model of MDD ( the Flinders Sensitive Line [ FSL ] ) and the controls , the Flinders Resistant Line ( FRL ) .

Example answer:
{"entities": [{"text": "miRNA", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "miRNAs", "type": "AnatomicalStructure"}, {"text": "profile", "type": "HealthCareActivity"}, {"text": "prefrontal cortex", "type": "AnatomicalStructure"}, {"text": "PFC", "type": "AnatomicalStructure"}, {"text": "genetic rat model", "type": "IntellectualProduct"}, {"text": "MDD", "type": "BiologicFunction"}, {"text": "Flinders Sensitive Line", "type": "IntellectualProduct"}, {"text": "FSL", "type": "IntellectualProduct"}, {"text": "Flinders Resistant Line", "type": "IntellectualProduct"}, {"text": "FRL", "type": "IntellectualProduct"}]}

Example input:
Sentence: We found that all 11 known miRNAs were involved mainly in pathways of reproduction regulation , such as steroid hormone biosynthesis and dopaminergic synapse .

Example answer:
{"entities": [{"text": "miRNAs", "type": "Chemical"}, {"text": "pathways", "type": "BiologicFunction"}, {"text": "reproduction", "type": "BiologicFunction"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "steroid hormone biosynthesis", "type": "BiologicFunction"}, {"text": "dopaminergic synapse", "type": "SpatialConcept"}]}

Example input:
Sentence: Differences identified in the miRNA expression profiles and the target gene analysis results were further analyzed to identify potential regulators of terminal hindgut development .

Example answer:
{"entities": [{"text": "miRNA", "type": "AnatomicalStructure"}, {"text": "gene analysis", "type": "ResearchActivity"}, {"text": "terminal", "type": "SpatialConcept"}, {"text": "hindgut", "type": "AnatomicalStructure"}, {"text": "development", "type": "BiologicFunction"}]}

Example input:
Sentence: Compared with the control group , 111 miRNAs expressed in the terminal hindgut of the experimental group were up - regulated on gestational day 16 , while 117 miRNAs were down - regulated .

Example answer:
{"entities": [{"text": "miRNAs", "type": "AnatomicalStructure"}, {"text": "terminal", "type": "SpatialConcept"}, {"text": "hindgut", "type": "AnatomicalStructure"}, {"text": "group", "type": "PopulationGroup"}, {"text": "up - regulated", "type": "BiologicFunction"}, {"text": "miRNAs", "type": "Chemical"}, {"text": "down - regulated", "type": "BiologicFunction"}]}

Example input:
Sentence: Differential miRNA expression analysis during late stage terminal hindgut development in fetal rats Terminal hindgut deformity is the leading digestive tract malformation , however , the etiology and pathogenesis remained unknown .

Example answer:
{"entities": [{"text": "miRNA expression analysis", "type": "ResearchActivity"}, {"text": "terminal", "type": "SpatialConcept"}, {"text": "hindgut", "type": "AnatomicalStructure"}, {"text": "development", "type": "BiologicFunction"}, {"text": "fetal", "type": "Finding"}, {"text": "rats", "type": "Eukaryote"}, {"text": "Terminal", "type": "SpatialConcept"}, {"text": "deformity", "type": "AnatomicalStructure"}, {"text": "digestive tract", "type": "BodySystem"}, {"text": "pathogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: These data support an important regulatory role for miRNAs in the expression of target genes during terminal hindgut development in fetal rats .

Example answer:
{"entities": [{"text": "regulatory", "type": "AnatomicalStructure"}, {"text": "miRNAs", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "terminal", "type": "SpatialConcept"}, {"text": "hindgut", "type": "AnatomicalStructure"}, {"text": "development", "type": "BiologicFunction"}, {"text": "fetal", "type": "Finding"}, {"text": "rats", "type": "Eukaryote"}]}

Input:
Sentence: A subset of these miRNAs was found to be closely related to rat fetus terminal hindgut growth and development .

## Item MedMentions:test:3923
Example input:
Sentence: Here , we report a novel real - time ultrasound time - of - flight instrument that is capable of monitoring and imaging the critical step in formalin fixation , diffusion of the fixative into tissue , which provides a quantifiable quality metric for tissue fixation in the clinical laboratory ensuring consistent downstream molecular assay results .

Example answer:
{"entities": [{"text": "real - time ultrasound time - of - flight instrument", "type": "MedicalDevice"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "imaging", "type": "HealthCareActivity"}, {"text": "formalin fixation", "type": "HealthCareActivity"}, {"text": "fixative", "type": "Chemical"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "metric", "type": "Chemical"}, {"text": "tissue fixation", "type": "HealthCareActivity"}, {"text": "clinical laboratory", "type": "Organization"}, {"text": "molecular assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: Both mono - spectrum images of Group A and polychromatic images of Group B were used to reconstruct maximum intensity projection ( MIP ) and volume rendering ( VR ) images of the perforating artery , respectively .

Example answer:
{"entities": [{"text": "mono - spectrum images", "type": "IntellectualProduct"}, {"text": "polychromatic images", "type": "IntellectualProduct"}, {"text": "images", "type": "IntellectualProduct"}, {"text": "perforating artery", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Fluorescence recovery after photobleaching ( FRAP ) microscopy is used to probe the diffusion properties of TATS in isolated rat cardiomyocytes : A fluorescent dextran inside TATS lumen is photobleached , and signal recovery by diffusion of unbleached dextran from the extracellular space is monitored .

Example answer:
{"entities": [{"text": "Fluorescence recovery after photobleaching", "type": "HealthCareActivity"}, {"text": "FRAP", "type": "HealthCareActivity"}, {"text": "microscopy", "type": "HealthCareActivity"}, {"text": "probe", "type": "ResearchActivity"}, {"text": "properties", "type": "BiologicFunction"}, {"text": "TATS", "type": "AnatomicalStructure"}, {"text": "rat", "type": "Eukaryote"}, {"text": "cardiomyocytes", "type": "AnatomicalStructure"}, {"text": "fluorescent dextran", "type": "Chemical"}, {"text": "lumen", "type": "SpatialConcept"}, {"text": "dextran", "type": "Chemical"}, {"text": "extracellular space", "type": "SpatialConcept"}, {"text": "monitored", "type": "HealthCareActivity"}]}

Example input:
Sentence: Evaluations with modified dynamic XCAT phantom and preclinical porcine datasets have demonstrated that the proposed PWLS - ndiSTV approach can achieve promising gains over other existing approaches in terms of noise - induced artifacts mitigation , edge details preservation , and accurate MPHP maps calculation .

Example answer:
{"entities": [{"text": "preclinical porcine datasets", "type": "IntellectualProduct"}, {"text": "PWLS - ndiSTV", "type": "IntellectualProduct"}, {"text": "MPHP maps", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here , we show that several dozen plaque - forming units ( pfu ) of influenza virus ( IFV ) can be detected using a boron - doped diamond ( BDD ) electrode terminated with a sialic acid - mimic peptide .

Example answer:
{"entities": [{"text": "influenza virus", "type": "Virus"}, {"text": "IFV", "type": "Virus"}, {"text": "boron - doped diamond ( BDD ) electrode", "type": "MedicalDevice"}, {"text": "sialic acid - mimic peptide", "type": "Chemical"}]}

Example input:
Sentence: The assay was transformed into an integrated microfluidic system using a multilayered polyester microfluidic disc created through laser print , cut and laminate fabrication , with fluid flow controlled by rotation speed without any mechanical valves .

Example answer:
{"entities": [{"text": "assay", "type": "HealthCareActivity"}, {"text": "integrated microfluidic system", "type": "HealthCareActivity"}, {"text": "polyester", "type": "Chemical"}, {"text": "microfluidic disc", "type": "MedicalDevice"}, {"text": "mechanical valves", "type": "MedicalDevice"}]}

Example input:
Sentence: Diffusion imaging with nCPMG SS - FSE gives similar SNR to an EPI acquisition , though apparent diffusion coefficient values are higher than seen with EPI .

Example answer:
{"entities": [{"text": "Diffusion imaging", "type": "HealthCareActivity"}, {"text": "nCPMG", "type": "Finding"}, {"text": "SS - FSE", "type": "HealthCareActivity"}, {"text": "EPI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Fully automated disc diffusion for rapid antibiotic susceptibility test results : a proof - of - principle study Antibiotic resistance poses a significant threat to patients suffering from infectious diseases .

Example answer:
{"entities": [{"text": "disc diffusion", "type": "HealthCareActivity"}, {"text": "antibiotic susceptibility test", "type": "HealthCareActivity"}, {"text": "results", "type": "Finding"}, {"text": "suffering", "type": "Finding"}, {"text": "infectious diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: At 0 , 24 , 48 , and 72 hours , a 1 - cm disk was cut from the dressing sheet of each study arm , placed on agar plates seeded with Staphylococcus aureus and Pseudomonas aeruginosa , and incubated for 24 hours , and the zone of inhibition was measured .

Example answer:
{"entities": [{"text": "disk", "type": "SpatialConcept"}, {"text": "dressing sheet", "type": "MedicalDevice"}, {"text": "study arm", "type": "PopulationGroup"}, {"text": "agar plates", "type": "Chemical"}, {"text": "seeded", "type": "HealthCareActivity"}, {"text": "Staphylococcus aureus", "type": "Bacterium"}, {"text": "Pseudomonas aeruginosa", "type": "Bacterium"}, {"text": "incubated", "type": "HealthCareActivity"}, {"text": "zone", "type": "SpatialConcept"}]}

Example input:
Sentence: Disc diffusion is a well - standardized , established and cost - efficient AST procedure ; however , its use in the clinical laboratory is hampered by the many manual steps involved , and an incubation time of 16 - 18 h , which is required to achieve reliable test results .

Example answer:
{"entities": [{"text": "Disc diffusion", "type": "HealthCareActivity"}, {"text": "AST procedure", "type": "HealthCareActivity"}, {"text": "laboratory", "type": "Organization"}, {"text": "incubation time", "type": "Finding"}, {"text": "test results", "type": "Finding"}]}

Input:
Sentence: Disc diffusion plates were streaked , incubated and imaged using the WASPLab TM automation system .

## Item MedMentions:test:4034
Example input:
Sentence: The SF - 6D and both EQ - 5D - 5L value sets appeared to be valid but sensitive to different outcomes in Thai patients with chronic diseases .

Example answer:
{"entities": [{"text": "SF - 6D", "type": "IntellectualProduct"}, {"text": "EQ - 5D - 5L value sets", "type": "IntellectualProduct"}, {"text": "Thai", "type": "SpatialConcept"}, {"text": "chronic diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: The ICC and r were highest ( ≥0 . 80 ) for 25 ( OH ) D , free 25 ( OH ) D , bioavailable 25 ( OH ) D and PTH , but somewhat lower ( approximately 0 . 60 - 0 . 75 ) for the other biomarkers .

Example answer:
{"entities": [{"text": "25 ( OH ) D", "type": "Chemical"}, {"text": "PTH", "type": "Chemical"}, {"text": "biomarkers", "type": "ClinicalAttribute"}]}

Example input:
Sentence: 9 months , P = 0 . 030 ) , whereas no significant correlation was detected for pts , where only metastatic tissue was available ( PFS : 5 . 8 vs 6 .

Example answer:
{"entities": [{"text": "metastatic tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The pooled mean difference favoring fusion over PT was 8 . 8 points ( 95 % CI , 4 . 1 - 13 . 6 ) .

Example answer:
{"entities": [{"text": "fusion", "type": "HealthCareActivity"}, {"text": "PT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Ultrasound measurements of diaphragm thickness , excursion ( EXdi ) and thickening fraction ( TFdi ) are putative estimators of diaphragm function , but have never been compared with phrenic nerve stimulation .

Example answer:
{"entities": [{"text": "Ultrasound measurements", "type": "HealthCareActivity"}, {"text": "diaphragm", "type": "AnatomicalStructure"}, {"text": "excursion", "type": "Finding"}, {"text": "EXdi", "type": "Finding"}, {"text": "thickening fraction", "type": "Finding"}, {"text": "TFdi", "type": "Finding"}, {"text": "phrenic nerve stimulation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Our aim was to describe the relationship between these variables and diaphragm function evaluated using the change in endotracheal pressure after phrenic nerve stimulation ( Ptr , stim ) , and to compare their prognostic value .

Example answer:
{"entities": [{"text": "endotracheal pressure", "type": "Finding"}, {"text": "phrenic nerve stimulation", "type": "HealthCareActivity"}, {"text": "Ptr , stim", "type": "HealthCareActivity"}]}

Example input:
Sentence: Moreover , patients in the S + EX group displayed greater increases of different HRV indices ( RR , pNN50 , RMSSD , SDHR , SDNN , HF , and LF ) compared with those in the S group .

Example answer:
{"entities": [{"text": "indices", "type": "IntellectualProduct"}]}

Example input:
Sentence: Between November 2014 and June 2015 , Ptr , stim and ultrasound variables were measured in mechanically ventilated patients < 24 hours after intubation ( ' initiation of mechanical ventilation ( MV ) ' , under assist - control ventilation , ACV ) and at the time of switch to pressure support ventilation ( ' switch to PSV ' ) , and compared using Spearman 's correlation and receiver operating characteristic curve analysis .

Example answer:
{"entities": [{"text": "Ptr , stim", "type": "HealthCareActivity"}, {"text": "ultrasound", "type": "HealthCareActivity"}, {"text": "mechanically ventilated", "type": "HealthCareActivity"}, {"text": "intubation", "type": "HealthCareActivity"}, {"text": "pressure support ventilation", "type": "HealthCareActivity"}, {"text": "PSV", "type": "HealthCareActivity"}, {"text": "Spearman 's correlation", "type": "IntellectualProduct"}]}

Example input:
Sentence: Under PSV , TFdi was strongly correlated to diaphragm strength and both were predictors of remaining length of MV and ICU and hospital death .

Example answer:
{"entities": [{"text": "PSV", "type": "HealthCareActivity"}, {"text": "TFdi", "type": "Finding"}, {"text": "diaphragm", "type": "AnatomicalStructure"}, {"text": "strength", "type": "BiologicFunction"}, {"text": "ICU", "type": "Organization"}, {"text": "hospital death", "type": "Finding"}]}

Example input:
Sentence: Under ACV , diaphragm thickness , EXdi and TFdi were uncorrelated to Ptr , stim .

Example answer:
{"entities": [{"text": "diaphragm", "type": "AnatomicalStructure"}, {"text": "EXdi", "type": "Finding"}, {"text": "TFdi", "type": "Finding"}, {"text": "Ptr , stim", "type": "HealthCareActivity"}]}

Input:
Sentence: At switch to PSV , TFdi and EXdi were respectively very strongly and moderately correlated to Ptr , stim , ( r = 0 . 87 , p < 0 . 001 and 0 . 45 , p = 0 .

## Item MedMentions:test:4012
Example input:
Sentence: TpTe immediately after CRT - D independently predicted VT / VF episodes at 1 - year follow - up ( hazard ratio [ HR ] , 1 . 030 ; P = 0 . 001 ) .

Example answer:
{"entities": [{"text": "VT", "type": "BiologicFunction"}, {"text": "VF", "type": "BiologicFunction"}, {"text": "1 - year follow - up", "type": "Finding"}]}

Example input:
Sentence: Three months after treatment , > 30 % improvement was seen in 10 / 33 ( 30 % ) of VRET participants and 12 / 33 ( 36 % ) in CET .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "VRET", "type": "HealthCareActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "CET", "type": "HealthCareActivity"}]}

Example input:
Sentence: For all patients , TpTe slightly increased immediately after CRT - D implantation , and then decreased at the 1 - year follow - up ( from 107 ± 23 to 110 ± 21 ms within 24 h , to 94 ± 24 ms at 1 - year follow - up , F = 19 . 366 , P < 0 .

Example answer:
{"entities": [{"text": "1 - year follow - up", "type": "Finding"}]}

Example input:
Sentence: Best RECIST responses were : 6 responses ( M - SFT = 2 of 7 , D - SFT = 4 of 5 ) , 1 stable disease , 5 progressions , with a 6 - month median progression - free survival ( M - SFT = 6 , D - SFT = 10 months ) .

Example answer:
{"entities": [{"text": "RECIST", "type": "IntellectualProduct"}, {"text": "M - SFT", "type": "BiologicFunction"}, {"text": "D - SFT", "type": "BiologicFunction"}, {"text": "stable disease", "type": "Finding"}, {"text": "progressions", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients ≥70 had an increased risk of death at 3 months following CRT ( odds ratio 5 . 19 , 95 % CI 1 . 64 - 16 . 41 ; p = 0 . 005 ) and worse survival over time ( hazard ratio 2 .

Example answer:
{"entities": [{"text": "death", "type": "Finding"}, {"text": "CRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Circumferential ILD measures on cardiac CT are predictive of clinical response to CRT .

Example answer:
{"entities": [{"text": "Circumferential", "type": "SpatialConcept"}, {"text": "cardiac CT", "type": "HealthCareActivity"}, {"text": "clinical response", "type": "Finding"}, {"text": "CRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using transthoracic echocardiography and coronary computed tomography angiography , we assessed 3 primary outcome measures : left ventricular ( LV ) systolic function ( left ventricular ejection fraction ) , LV diastolic function ( early relaxation velocity ) , and coronary atherosclerosis ( coronary artery plaque volume ) .

Example answer:
{"entities": [{"text": "transthoracic echocardiography", "type": "HealthCareActivity"}, {"text": "coronary computed tomography angiography", "type": "HealthCareActivity"}, {"text": "left ventricular ( LV ) systolic function", "type": "BiologicFunction"}, {"text": "left ventricular ejection fraction", "type": "ClinicalAttribute"}, {"text": "LV diastolic function", "type": "BiologicFunction"}, {"text": "coronary atherosclerosis", "type": "BiologicFunction"}, {"text": "coronary artery", "type": "AnatomicalStructure"}, {"text": "plaque", "type": "Finding"}]}

Example input:
Sentence: Patients with TpTe shortened at 1 - year after CRT had a higher rate of LV reverse remodeling and less VT / VF episodes .

Example answer:
{"entities": [{"text": "CRT", "type": "HealthCareActivity"}, {"text": "LV reverse remodeling", "type": "BiologicFunction"}, {"text": "VT", "type": "BiologicFunction"}, {"text": "VF", "type": "BiologicFunction"}]}

Example input:
Sentence: Forty - two consecutive patients undergoing CRT had serial clinical and echocardiographic evaluations performed in addition to a post - procedural cardiac -gated CT with blinded measurement of direct and circumferential ( via the myocardium ) ILD measures .

Example answer:
{"entities": [{"text": "CRT", "type": "HealthCareActivity"}, {"text": "clinical", "type": "HealthCareActivity"}, {"text": "echocardiographic", "type": "HealthCareActivity"}, {"text": "evaluations", "type": "HealthCareActivity"}, {"text": "cardiac", "type": "SpatialConcept"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "blinded", "type": "ResearchActivity"}, {"text": "circumferential", "type": "SpatialConcept"}, {"text": "myocardium", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Secondary measures were change in best - corrected visual acuity ( BCVA ) and central retinal thickness ( CRT ) by spectral - domain optical coherence tomography at 3 months after treatment .

Example answer:
{"entities": [{"text": "best - corrected visual acuity", "type": "Finding"}, {"text": "BCVA", "type": "Finding"}, {"text": "central retinal thickness", "type": "Finding"}, {"text": "CRT", "type": "Finding"}, {"text": "spectral - domain optical coherence tomography", "type": "MedicalDevice"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Input:
Sentence: Clinical response to CRT , the primary clinical outcome , was defined as a ≥15 % reduction in LVESV using echocardiography at 6 - months .

## Item MedMentions:test:3921
Example input:
Sentence: Phytolith - occluded organic carbon as a mechanism for long - term carbon sequestration in a typical steppe : The predominant role of belowground productivity Phytolith - occluded organic carbon ( phytOC ) has recently been demonstrated to be an important terrestrial carbon ( C ) fraction resistant to decomposition and thus has potential for long - term C sequestration .

Example answer:
{"entities": [{"text": "carbon", "type": "Chemical"}, {"text": "steppe", "type": "SpatialConcept"}, {"text": "phytOC", "type": "Chemical"}, {"text": "terrestrial", "type": "SpatialConcept"}, {"text": "C", "type": "Chemical"}]}

Example input:
Sentence: Roots growing up - slope were the main contributors to anchorage properties , which included higher strength and higher number of fibers in the xylematic tissues .

Example answer:
{"entities": [{"text": "Roots", "type": "Eukaryote"}, {"text": "fibers", "type": "Eukaryote"}, {"text": "xylematic", "type": "Eukaryote"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: While water limitation was represented in models and the primary driver of seasonal photosynthesis in southern Amazonia , changes in internal biophysical processes , light - harvesting adaptations ( e . g . , variations in leaf area index ( LAI ) and increasing leaf -level assimilation rate related to leaf demography ) , and allocation lags between leaf and wood , dominated equatorial Amazon carbon flux dynamics and were deficient or absent from current model formulations .

Example answer:
{"entities": [{"text": "models", "type": "IntellectualProduct"}, {"text": "southern Amazonia", "type": "SpatialConcept"}, {"text": "biophysical processes", "type": "BiologicFunction"}, {"text": "light - harvesting", "type": "BiologicFunction"}, {"text": "leaf area index", "type": "IntellectualProduct"}, {"text": "LAI", "type": "IntellectualProduct"}, {"text": "leaf", "type": "Eukaryote"}, {"text": "assimilation", "type": "BiologicFunction"}, {"text": "wood", "type": "Eukaryote"}, {"text": "equatorial Amazon", "type": "SpatialConcept"}, {"text": "model", "type": "IntellectualProduct"}]}

Example input:
Sentence: We proved computationally that the predicted overload behavior was due to substrate competition in the pathway .

Example answer:
{"entities": [{"text": "overload behavior", "type": "BiologicFunction"}]}

Example input:
Sentence: In Arabidopsis thaliana , light - activated PHYs accumulate in the nucleus , where they regulate downstream signaling components , such as phytochrome interacting factors ( PIFs ) .

Example answer:
{"entities": [{"text": "Arabidopsis thaliana", "type": "Eukaryote"}, {"text": "PHYs", "type": "Chemical"}, {"text": "nucleus", "type": "AnatomicalStructure"}, {"text": "downstream signaling components", "type": "Chemical"}, {"text": "phytochrome interacting factors", "type": "Chemical"}, {"text": "PIFs", "type": "Chemical"}]}

Example input:
Sentence: The increase of A is largely due to an increase of RuBP regeneration rate via increased leaf nitrogen content , and partially explained by reduced stomatal limitation via increased stomatal conductance relative to A .

Example answer:
{"entities": [{"text": "leaf", "type": "Eukaryote"}, {"text": "nitrogen", "type": "Chemical"}, {"text": "stomatal", "type": "Eukaryote"}]}

Example input:
Sentence: To reach an unbiased synchronization of the IADF position within tree rings and seasonal fluctuations in environmental conditions , it is necessary to know the timing of cambial activity and wood formation , which are species - and site - specific processes .

Example answer:
{"entities": [{"text": "unbiased", "type": "ResearchActivity"}, {"text": "position", "type": "SpatialConcept"}, {"text": "tree", "type": "Eukaryote"}, {"text": "rings", "type": "SpatialConcept"}, {"text": "fluctuations", "type": "Finding"}, {"text": "environmental", "type": "SpatialConcept"}, {"text": "cambial activity", "type": "BiologicFunction"}]}

Example input:
Sentence: how nutrient enrichment ( i . e . , nitrogen availability ) affected the growth of Fucus vesiculosus , a foundational macroalgal species in the North Atlantic rocky intertidal zone , and found that nutrient -enriched algal blades showed a significant increase in tissue growth compared to individuals grown under ambient conditions .

Example answer:
{"entities": [{"text": "nutrient", "type": "Food"}, {"text": "nitrogen", "type": "Chemical"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "Fucus vesiculosus", "type": "Eukaryote"}, {"text": "macroalgal", "type": "Eukaryote"}, {"text": "species", "type": "Eukaryote"}, {"text": "North Atlantic rocky intertidal zone", "type": "SpatialConcept"}, {"text": "algal blades", "type": "IntellectualProduct"}, {"text": "tissue growth", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , we test the hypothesis that the identity and richness of ectomycorrhizal ( ECM ) fungi at the intra - and interspecific levels affect ecosystem multifunctionality by regulating plant and fungal productivity , soil CO2 efflux and nutrient retention .

Example answer:
{"entities": [{"text": "ectomycorrhizal", "type": "Eukaryote"}, {"text": "ECM", "type": "Eukaryote"}, {"text": "fungi", "type": "Eukaryote"}, {"text": "regulating", "type": "BiologicFunction"}, {"text": "plant", "type": "Eukaryote"}, {"text": "fungal", "type": "Eukaryote"}, {"text": "CO2", "type": "Chemical"}, {"text": "nutrient", "type": "Food"}]}

Example input:
Sentence: Ecosystem -level adaptations to low soil nutrient availability and long - term low levels of disturbance may help to account for the lower productivity and higher accumulation of biomass in nutrient -poor forests compared to nutrient -richer forests .

Example answer:
{"entities": [{"text": "accumulation", "type": "Finding"}]}

Input:
Sentence: the nutrient uptake from litter , the resorption , or the storage of nutrients in the biomass ) , may strongly control forest structure and dynamics .

## Item MedMentions:test:4230
Example input:
Sentence: Hypoxia could play an important role in this association .

Example answer:
{"entities": [{"text": "Hypoxia", "type": "BiologicFunction"}]}

Example input:
Sentence: Previous population studies of the association are sparse , conflicting and confined largely to studies of administrative data .

Example answer:
{"entities": [{"text": "population studies", "type": "ResearchActivity"}, {"text": "conflicting", "type": "Finding"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "administrative", "type": "Finding"}]}

Example input:
Sentence: These factors were influenced by participants ' knowledge , resources , and monthly contact with study staff ( perceived as a form of social support ) .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "knowledge", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "staff", "type": "ProfessionalOrOccupationalGroup"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "social support", "type": "HealthCareActivity"}]}

Example input:
Sentence: Significant associations ( p ≤ 0 . 05 ) included age and education with somewhat and income and comorbidities with very severe .

Example answer:
{"entities": [{"text": "education", "type": "Finding"}]}

Example input:
Sentence: However , further research is needed to investigate long - term efficacy of the intervention .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: For men , the associations were robust for controlling childhood parental socioeconomic status , history of unemployment , and adulthood health behavior , but attenuated circa 35 % when three major temperament traits were taken into account .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "associations", "type": "BiologicFunction"}, {"text": "unemployment", "type": "Finding"}, {"text": "temperament", "type": "BiologicFunction"}]}

Example input:
Sentence: Findings indicate that , dependent upon study goals , researchers ' choice of design may influence participant recruitment , participant commitment , and impact on staff , factors that may in turn affect overall study success .

Example answer:
{"entities": [{"text": "study goals", "type": "ResearchActivity"}, {"text": "researchers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "design", "type": "IntellectualProduct"}, {"text": "participant", "type": "PopulationGroup"}, {"text": "staff", "type": "ProfessionalOrOccupationalGroup"}, {"text": "study success", "type": "ResearchActivity"}]}

Example input:
Sentence: Further research is needed to enable targeted effective interventions in this group .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "interventions", "type": "HealthCareActivity"}]}

Example input:
Sentence: Moreover , possible associated factors need to be explored .

Example answer:
{"entities": []}

Example input:
Sentence: However , the mechanism underlying this association requires further investigation .

Example answer:
{"entities": []}

Input:
Sentence: Furthermore , research is needed to identify individual factors that might influence these associations .

## Item MedMentions:test:3539
Example input:
Sentence: Inferior petrosal sinus sampling demonstrated a significant central -to - peripheral and lateralized left - sided ACTH gradient .

Example answer:
{"entities": [{"text": "Inferior petrosal sinus sampling", "type": "HealthCareActivity"}, {"text": "central", "type": "SpatialConcept"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "ACTH", "type": "Chemical"}]}

Example input:
Sentence: It can be diagnosed by the complex shape of the RTA , by the membranous tegular extension , the long coiled embolus , the retrolateral incision on the cymbium , the long convoluted copulatory duct extending anteriorly to the copulatory openings and by the presence of paramedian epigynal pockets and of an anterior ridge on the epigynum .

Example answer:
{"entities": [{"text": "diagnosed", "type": "Finding"}, {"text": "shape", "type": "SpatialConcept"}, {"text": "RTA", "type": "AnatomicalStructure"}, {"text": "membranous tegular extension", "type": "AnatomicalStructure"}, {"text": "long coiled embolus", "type": "AnatomicalStructure"}, {"text": "retrolateral incision on the cymbium", "type": "AnatomicalStructure"}, {"text": "long convoluted copulatory duct", "type": "AnatomicalStructure"}, {"text": "anteriorly", "type": "SpatialConcept"}, {"text": "copulatory openings", "type": "AnatomicalStructure"}, {"text": "presence", "type": "Finding"}, {"text": "paramedian epigynal pockets", "type": "AnatomicalStructure"}, {"text": "anterior", "type": "SpatialConcept"}, {"text": "ridge", "type": "SpatialConcept"}, {"text": "epigynum", "type": "AnatomicalStructure"}]}

Example input:
Sentence: During routine laparoscopic exploration , right vas deferens and testicular vessels were entering the right internal inguinal ring so right inguinal exploration was done , which revealed blind ending vas deferens and testicular vessels and the left testis was found intra - abdominally near the left internal ring with a mass on its upper pole .

Example answer:
{"entities": [{"text": "laparoscopic", "type": "HealthCareActivity"}, {"text": "exploration", "type": "HealthCareActivity"}, {"text": "right vas deferens", "type": "AnatomicalStructure"}, {"text": "right internal inguinal ring", "type": "AnatomicalStructure"}, {"text": "right inguinal", "type": "SpatialConcept"}, {"text": "blind ending", "type": "Finding"}, {"text": "vas deferens", "type": "AnatomicalStructure"}, {"text": "left testis", "type": "AnatomicalStructure"}, {"text": "intra - abdominally", "type": "SpatialConcept"}, {"text": "internal ring", "type": "SpatialConcept"}, {"text": "mass", "type": "Finding"}, {"text": "upper pole", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Combining serial sectioning and three - dimensional reconstruction , we identified a pair of supracrucal plexus vascular bodies at the proximal end of the alligator phallus that extend distally adjacent to ventro - medial sulcus tissues .

Example answer:
{"entities": [{"text": "serial sectioning", "type": "HealthCareActivity"}, {"text": "three - dimensional reconstruction", "type": "HealthCareActivity"}, {"text": "supracrucal plexus vascular", "type": "AnatomicalStructure"}, {"text": "bodies", "type": "AnatomicalStructure"}, {"text": "alligator", "type": "Eukaryote"}, {"text": "phallus", "type": "AnatomicalStructure"}, {"text": "ventro - medial sulcus tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Nerve decompression on the lateral surface of the ischial tuberosity was then performed .

Example answer:
{"entities": [{"text": "Nerve decompression", "type": "HealthCareActivity"}, {"text": "lateral surface", "type": "SpatialConcept"}, {"text": "ischial tuberosity", "type": "AnatomicalStructure"}]}

Example input:
Sentence: It extends transversely across the posterior abdominal wall from the duodenum to the spleen .

Example answer:
{"entities": [{"text": "extends", "type": "SpatialConcept"}, {"text": "transversely", "type": "SpatialConcept"}, {"text": "posterior abdominal wall", "type": "SpatialConcept"}, {"text": "duodenum", "type": "AnatomicalStructure"}, {"text": "spleen", "type": "AnatomicalStructure"}]}

Example input:
Sentence: On the inducing graft ( IG ) side , the tendon canal and semitendinosus tibial attachment site were connected by the fascia lata , which was harvested at the same width as the semitendinosus tendon .

Example answer:
{"entities": [{"text": "side", "type": "SpatialConcept"}, {"text": "tendon canal", "type": "AnatomicalStructure"}, {"text": "semitendinosus", "type": "AnatomicalStructure"}, {"text": "tibial", "type": "AnatomicalStructure"}, {"text": "attachment site", "type": "SpatialConcept"}, {"text": "fascia lata", "type": "AnatomicalStructure"}, {"text": "harvested", "type": "HealthCareActivity"}, {"text": "semitendinosus tendon", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The palmar cutaneous branch of the median nerve ( PCB ) is considered to run in a position adjacent to , but outside , the ulnar FCR sheath .

Example answer:
{"entities": [{"text": "palmar cutaneous branch of the median nerve", "type": "AnatomicalStructure"}, {"text": "PCB", "type": "AnatomicalStructure"}, {"text": "ulnar", "type": "AnatomicalStructure"}, {"text": "FCR", "type": "AnatomicalStructure"}, {"text": "sheath", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Entrapment of the posterior femoral cutaneous nerve and its inferior cluneal branches : anatomical basis of surgery for inferior cluneal neuralgia The apparent failure of pudendal nerve surgery in some patients has led us to suggest the possibility of entrapment of other adjacent nerve structures , leading to the concept of inferior cluneal neuralgia .

Example answer:
{"entities": [{"text": "Entrapment", "type": "BiologicFunction"}, {"text": "posterior femoral cutaneous nerve", "type": "AnatomicalStructure"}, {"text": "inferior cluneal branches", "type": "AnatomicalStructure"}, {"text": "anatomical basis", "type": "SpatialConcept"}, {"text": "surgery", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "inferior cluneal neuralgia", "type": "Finding"}, {"text": "pudendal nerve", "type": "AnatomicalStructure"}, {"text": "entrapment", "type": "BiologicFunction"}, {"text": "adjacent nerve structures", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A constant anatomical finding must be highlighted : the presence of a lateral fibrous expansion from the ischium passing behind the nerves and vessels , especially the posterior femoral cutaneous nerve and its perineal branches .

Example answer:
{"entities": [{"text": "anatomical finding", "type": "SpatialConcept"}, {"text": "lateral fibrous", "type": "AnatomicalStructure"}, {"text": "expansion", "type": "HealthCareActivity"}, {"text": "ischium", "type": "AnatomicalStructure"}, {"text": "nerves", "type": "AnatomicalStructure"}, {"text": "vessels", "type": "AnatomicalStructure"}, {"text": "posterior femoral cutaneous nerve", "type": "AnatomicalStructure"}, {"text": "perineal branches", "type": "AnatomicalStructure"}]}

Input:
Sentence: Via its numerous collateral branches , the posterior femoral cutaneous nerve innervates a very extensive territory including the posterior surface of the thigh , the infragluteal fold , the skin over the ischial tuberosity , but also the lateral anal region , scrotum or labium majus via its perineal branch .

## Item MedMentions:test:3969
Example input:
Sentence: Beyond that , the antioxidant N - acetyl cysteine ( NAC ) could reverse the changes of both cPLA2 and NF - κB caused by MGO .

Example answer:
{"entities": [{"text": "antioxidant", "type": "Chemical"}, {"text": "N - acetyl cysteine", "type": "Chemical"}, {"text": "NAC", "type": "Chemical"}, {"text": "cPLA2", "type": "Chemical"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "MGO", "type": "Chemical"}]}

Example input:
Sentence: The microenvironmental pH ( pHM ) was measured to evaluate the effect of the alkalizer on the pHM of SDs .

Example answer:
{"entities": [{"text": "alkalizer", "type": "Chemical"}, {"text": "SDs", "type": "Chemical"}]}

Example input:
Sentence: SEM data showed a relatively spherical shape of the MgO -loaded SD compared to the less - defined shape of pure drug .

Example answer:
{"entities": [{"text": "SEM", "type": "HealthCareActivity"}, {"text": "spherical shape", "type": "SpatialConcept"}, {"text": "MgO", "type": "Chemical"}, {"text": "SD", "type": "Chemical"}, {"text": "shape", "type": "SpatialConcept"}, {"text": "drug", "type": "Chemical"}]}

Example input:
Sentence: pHM values of the alkalizer -containing SDs were significantly higher than that of the SD without alkalizer .

Example answer:
{"entities": [{"text": "alkalizer", "type": "Chemical"}, {"text": "SDs", "type": "Chemical"}, {"text": "SD", "type": "Chemical"}]}

Example input:
Sentence: FTIR indicated a strong molecular interaction among EPM , alkalizer and polymer ; in particular , MgO showed the strongest interaction with EPM .

Example answer:
{"entities": [{"text": "FTIR", "type": "ResearchActivity"}, {"text": "molecular interaction", "type": "BiologicFunction"}, {"text": "EPM", "type": "Chemical"}, {"text": "alkalizer", "type": "Chemical"}, {"text": "polymer", "type": "Chemical"}, {"text": "MgO", "type": "Chemical"}]}

Example input:
Sentence: The current alkalizer -containing SD could provide a promising approach for aqueous stabilization of acid - labile drugs without using enteric coating method .

Example answer:
{"entities": [{"text": "alkalizer", "type": "Chemical"}, {"text": "SD", "type": "Chemical"}, {"text": "acid", "type": "Chemical"}, {"text": "labile", "type": "Finding"}, {"text": "drugs", "type": "Chemical"}, {"text": "enteric coating", "type": "Chemical"}]}

Example input:
Sentence: In this study , we prepared new gastric fluid resistant solid dispersions ( SDs ) containing alkalizers .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "gastric fluid", "type": "BodySubstance"}, {"text": "solid dispersions", "type": "Chemical"}, {"text": "SDs", "type": "Chemical"}, {"text": "alkalizers", "type": "Chemical"}]}

Example input:
Sentence: Enhanced gastric stability of esomeprazole by molecular interaction and modulation of microenvironmental pH with alkalizers in solid dispersion Due to the instability of esomeprazole magnesium dihydrate ( EPM ) , a proton pump inhibitor , in gastric fluid , enteric - coated dosage form is commonly used for therapeutic application .

Example answer:
{"entities": [{"text": "esomeprazole", "type": "Chemical"}, {"text": "molecular interaction", "type": "BiologicFunction"}, {"text": "alkalizers", "type": "Chemical"}, {"text": "solid dispersion", "type": "Chemical"}, {"text": "instability", "type": "Finding"}, {"text": "esomeprazole magnesium dihydrate", "type": "Chemical"}, {"text": "EPM", "type": "Chemical"}, {"text": "proton pump inhibitor", "type": "Chemical"}, {"text": "gastric fluid", "type": "BodySubstance"}, {"text": "enteric - coated dosage", "type": "Chemical"}, {"text": "therapeutic application", "type": "HealthCareActivity"}]}

Example input:
Sentence: It was evident that alkalizer interacts with benzimidazole ring and / or sulfonyl group of EPM for enhancing EPM stability in gastric fluid .

Example answer:
{"entities": [{"text": "alkalizer", "type": "Chemical"}, {"text": "EPM", "type": "Chemical"}, {"text": "gastric fluid", "type": "BodySubstance"}]}

Example input:
Sentence: Then , new mechanistic evidence regarding the effects of pharmaceutical alkalizers on the aqueous stability of EPM in simulated gastric fluid was investigated .

Example answer:
{"entities": [{"text": "pharmaceutical", "type": "Chemical"}, {"text": "alkalizers", "type": "Chemical"}, {"text": "EPM", "type": "Chemical"}, {"text": "gastric fluid", "type": "BodySubstance"}]}

Input:
Sentence: Among alkalizer s , MgO loaded in SDs proved to be the best alkalizer to stabilize EPM in simulated gastric fluid .

## Item MedMentions:test:3971
Example input:
Sentence: Form and function in gene regulatory networks : the structure of network motifs determines fundamental properties of their dynamical state space Network motifs have been studied extensively over the past decade , and certain motifs , such as the feed - forward loop , play an important role in regulatory networks .

Example answer:
{"entities": [{"text": "gene regulatory networks", "type": "BiologicFunction"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "regulatory networks", "type": "BiologicFunction"}]}

Example input:
Sentence: A pathway based analysis revealed a network of Pa14 and Ma549 - resistance genes that are functionally connected through processes that encompass phagocytosis and engulfment , cell mobility , intermediary metabolism , protein phosphorylation , axon guidance , response to DNA damage , and drug metabolism .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "Pa14", "type": "Bacterium"}, {"text": "Ma549", "type": "Eukaryote"}, {"text": "resistance", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "phagocytosis", "type": "BiologicFunction"}, {"text": "engulfment", "type": "BiologicFunction"}, {"text": "cell mobility", "type": "BiologicFunction"}, {"text": "intermediary metabolism", "type": "BiologicFunction"}, {"text": "protein phosphorylation", "type": "BiologicFunction"}, {"text": "axon guidance", "type": "BiologicFunction"}, {"text": "response to DNA damage", "type": "BiologicFunction"}, {"text": "drug metabolism", "type": "BiologicFunction"}]}

Example input:
Sentence: Gene Ontology enrichment analysis was performed for the DEGs in the gene coexpression network with DAVID online tool .

Example answer:
{"entities": [{"text": "Gene Ontology", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "DEGs", "type": "AnatomicalStructure"}, {"text": "gene coexpression", "type": "BiologicFunction"}, {"text": "DAVID online tool", "type": "IntellectualProduct"}]}

Example input:
Sentence: GO and pathway analysis of the predicted targets showed enrichment in 14 biological processes , 10 molecular functions , 8 cellular components and 104 pathways .

Example answer:
{"entities": [{"text": "GO", "type": "IntellectualProduct"}, {"text": "pathway analysis", "type": "IntellectualProduct"}, {"text": "biological processes", "type": "BiologicFunction"}, {"text": "molecular functions", "type": "BiologicFunction"}, {"text": "cellular components", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Biological networks are usually represented as graphs ; evolutionary events not only include addition and removal of vertices and edges but also duplication of vertices and their associated edges .

Example answer:
{"entities": [{"text": "graphs", "type": "IntellectualProduct"}, {"text": "edges", "type": "SpatialConcept"}]}

Example input:
Sentence: Recent studies have used Boolean network motifs to explore the link between form and function in gene regulatory networks and have found that the structure of a motif does not strongly determine its function , if this is defined in terms of the gene expression patterns the motif can produce .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "Boolean", "type": "IntellectualProduct"}, {"text": "gene regulatory networks", "type": "BiologicFunction"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "patterns", "type": "SpatialConcept"}]}

Example input:
Sentence: Gene ontology enrichment analysis revealed that the gene set connected to the T18 differentially methylated CpGs was highly enriched for GO terms related to " DNA binding " and " transcription factor binding " coupled to the RNA polymerase II transcription .

Example answer:
{"entities": [{"text": "Gene ontology", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "gene set", "type": "AnatomicalStructure"}, {"text": "T18", "type": "BiologicFunction"}, {"text": "methylated", "type": "BiologicFunction"}, {"text": "CpGs", "type": "Chemical"}, {"text": "GO", "type": "IntellectualProduct"}, {"text": "DNA binding", "type": "BiologicFunction"}, {"text": "transcription factor binding", "type": "BiologicFunction"}, {"text": "RNA polymerase II", "type": "Chemical"}, {"text": "transcription", "type": "BiologicFunction"}]}

Example input:
Sentence: Transcripts were annotated using statistically enriched GO terms , pathways and diseases across cells / tissues based on guilt - by - association principle .

Example answer:
{"entities": [{"text": "Transcripts", "type": "Chemical"}, {"text": "GO terms", "type": "IntellectualProduct"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Gene ontology ( GO ) analysis indicated that differentially expressed mRNAs were involved in transport , cell adhesion , ion transport , and metabolic processes , among others .

Example answer:
{"entities": [{"text": "Gene ontology", "type": "IntellectualProduct"}, {"text": "GO", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "differentially expressed", "type": "BiologicFunction"}, {"text": "mRNAs", "type": "Chemical"}, {"text": "transport", "type": "BiologicFunction"}, {"text": "cell adhesion", "type": "BiologicFunction"}, {"text": "ion transport", "type": "BiologicFunction"}, {"text": "metabolic processes", "type": "BiologicFunction"}]}

Example input:
Sentence: Gene Ontology ( GO ) and Kyoto Encyclopedia of Genes and Genomes ( KEGG ) analysis were performed to identify potential pathways and functional annotations associated with AS .

Example answer:
{"entities": [{"text": "Gene Ontology", "type": "IntellectualProduct"}, {"text": "( GO )", "type": "IntellectualProduct"}, {"text": "Kyoto Encyclopedia of Genes and Genomes", "type": "IntellectualProduct"}, {"text": "( KEGG )", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "pathways", "type": "BiologicFunction"}, {"text": "annotations", "type": "ResearchActivity"}, {"text": "AS", "type": "BiologicFunction"}]}

Input:
Sentence: Results are visualized as networks in which Gene Ontology ( GO ) terms and pathways are grouped based on their biological role .

## Item MedMentions:test:4086
Example input:
Sentence: Overall , heritability ( H2 ) was calculated for GYLD , LM6 and JIM and resulted to be 0 . 42 , 0 . 32 and 0 . 20 , respectively .

Example answer:
{"entities": [{"text": "LM6", "type": "Chemical"}, {"text": "JIM", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we performed Extended Haplotype Homozygosity ( EHH ) tests to identify significant core regions employing 600 K SNP Chicken chip in an F2 population of 1 , 534 hens , which was derived from reciprocal crosses between White Leghorn and Dongxiang chicken .

Example answer:
{"entities": [{"text": "core regions", "type": "SpatialConcept"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "Chicken", "type": "Eukaryote"}, {"text": "chip", "type": "ResearchActivity"}, {"text": "hens", "type": "Eukaryote"}, {"text": "reciprocal crosses", "type": "HealthCareActivity"}, {"text": "White Leghorn", "type": "Eukaryote"}, {"text": "Dongxiang chicken", "type": "Eukaryote"}]}

Example input:
Sentence: This process caused an increase on L ( * ) , b ( * ) , and H ( * ) , but a decrease on a ( * ) and C ( * ) .

Example answer:
{"entities": []}

Example input:
Sentence: In faecal batch incubations , LA biohydrogenation and butyrate production were positively correlated and SA did not inhibit butyrate production .

Example answer:
{"entities": [{"text": "faecal", "type": "BodySubstance"}, {"text": "batch incubations", "type": "HealthCareActivity"}, {"text": "LA", "type": "Chemical"}, {"text": "butyrate", "type": "Chemical"}, {"text": "SA", "type": "Chemical"}]}

Example input:
Sentence: However , the antagonistic relationship between level of production and response to heat stress ( HS ) implies that selection for HT animals under this approach must be done with caution so that productivity is not damaged .

Example answer:
{"entities": [{"text": "antagonistic", "type": "Chemical"}, {"text": "response to heat stress", "type": "BiologicFunction"}, {"text": "HS", "type": "BiologicFunction"}, {"text": "HT", "type": "Finding"}, {"text": "animals", "type": "Eukaryote"}]}

Example input:
Sentence: Thin layer chromatography ( TLC ) and high resolution triple quadrupole liquid chromatography / mass spectrometry ( LC / MS ) analysis of the AHLs extracted from the culture supernatant of H .

Example answer:
{"entities": [{"text": "Thin layer chromatography", "type": "HealthCareActivity"}, {"text": "TLC", "type": "HealthCareActivity"}, {"text": "high resolution triple quadrupole liquid chromatography / mass spectrometry", "type": "HealthCareActivity"}, {"text": "LC / MS", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "AHLs", "type": "Chemical"}, {"text": "culture", "type": "HealthCareActivity"}, {"text": "H .", "type": "Bacterium"}]}

Example input:
Sentence: alvei H4 was investigated by adding exogenous AHLs ( C4 - HSL , C6 - HSL and 3 - oxo - C8 - HSL ) to H .

Example answer:
{"entities": [{"text": "alvei H4", "type": "Bacterium"}, {"text": "AHLs", "type": "Chemical"}, {"text": "C4 - HSL", "type": "Chemical"}, {"text": "C6 - HSL", "type": "Chemical"}, {"text": "3 - oxo - C8 - HSL", "type": "Chemical"}, {"text": "H .", "type": "Bacterium"}]}

Example input:
Sentence: The effect of AHLs on biofilm formation of H .

Example answer:
{"entities": [{"text": "AHLs", "type": "Chemical"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "H .", "type": "Bacterium"}]}

Example input:
Sentence: AHLs production reached a maximum level of 134 .

Example answer:
{"entities": [{"text": "AHLs", "type": "Chemical"}, {"text": "production", "type": "BiologicFunction"}]}

Example input:
Sentence: AHL production and bacterial growth displayed a similar trend , suggesting that growth of H .

Example answer:
{"entities": [{"text": "AHL", "type": "Chemical"}, {"text": "production", "type": "BiologicFunction"}, {"text": "bacterial growth", "type": "Finding"}, {"text": "growth", "type": "Finding"}, {"text": "H .", "type": "Bacterium"}]}

Input:
Sentence: In order to determine the relationship between the production of AHL by H .

## Item MedMentions:test:4042
Example input:
Sentence: In contrast , Ae . aegypti ensured high viral dissemination and moderate to very high transmission .

Example answer:
{"entities": [{"text": "Ae . aegypti", "type": "Eukaryote"}, {"text": "viral dissemination", "type": "Finding"}, {"text": "transmission", "type": "BiologicFunction"}]}

Example input:
Sentence: Amongst all the parasites , Toxocara canis ( 44 . 93 % ) infection was highest , followed by Dipylidium caninum ( 17 . 39 % ) and hookworms ( 15 . 94 % ) .

Example answer:
{"entities": [{"text": "parasites", "type": "Eukaryote"}, {"text": "Toxocara canis ( 44 . 93 % ) infection", "type": "BiologicFunction"}, {"text": "Dipylidium caninum", "type": "Eukaryote"}, {"text": "hookworms", "type": "Eukaryote"}]}

Example input:
Sentence: This consistency of prevalence in each population over time suggests remarkable spatiotemporal constancy in parasite delivery vectors in this system , notably gulls that serve as definitive hosts for the parasites .

Example answer:
{"entities": [{"text": "parasite", "type": "Eukaryote"}, {"text": "vectors", "type": "Eukaryote"}, {"text": "gulls", "type": "Eukaryote"}, {"text": "parasites", "type": "Eukaryote"}]}

Example input:
Sentence: The minimum infection rate of ticks was less than 5 % .

Example answer:
{"entities": [{"text": "ticks", "type": "Eukaryote"}]}

Example input:
Sentence: We examined blood samples from 192 patients who visited clinics during the active tick - borne diseases season , using a newly developed qPCR assay that uses the specific molecular beacon probe .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "blood samples", "type": "BodySubstance"}, {"text": "clinics", "type": "Organization"}, {"text": "tick - borne diseases", "type": "BiologicFunction"}, {"text": "qPCR assay", "type": "ResearchActivity"}, {"text": "molecular beacon probe", "type": "Chemical"}]}

Example input:
Sentence: We collected 6 , 407 host - seeking ticks from two regions and 1 , 598 larvae obtained from 32 engorged female ticks and examined them to elucidate transovarial transmission .

Example answer:
{"entities": [{"text": "host - seeking ticks", "type": "Eukaryote"}, {"text": "regions", "type": "SpatialConcept"}, {"text": "larvae", "type": "Eukaryote"}, {"text": "female ticks", "type": "Eukaryote"}, {"text": "transovarial transmission", "type": "BiologicFunction"}]}

Example input:
Sentence: Babesia species infect erythrocytes and can be transmitted through blood transfusion .

Example answer:
{"entities": [{"text": "Babesia species", "type": "Eukaryote"}, {"text": "erythrocytes", "type": "AnatomicalStructure"}, {"text": "transmitted", "type": "BiologicFunction"}, {"text": "blood transfusion", "type": "HealthCareActivity"}]}

Example input:
Sentence: aureus transmission , and will inform strategies to control importation and spread .

Example answer:
{"entities": [{"text": "aureus", "type": "Bacterium"}]}

Example input:
Sentence: Epidemiological study of relapsing fever borreliae detected in Haemaphysalis ticks and wild animals in the western part of Japan The genus Borrelia comprises arthropod - borne bacteria , which are infectious agents in vertebrates .

Example answer:
{"entities": [{"text": "Epidemiological study", "type": "ResearchActivity"}, {"text": "relapsing fever", "type": "BiologicFunction"}, {"text": "borreliae", "type": "Bacterium"}, {"text": "detected", "type": "Finding"}, {"text": "Haemaphysalis", "type": "Eukaryote"}, {"text": "ticks", "type": "Eukaryote"}, {"text": "wild animals", "type": "Eukaryote"}, {"text": "western part of Japan", "type": "SpatialConcept"}, {"text": "genus Borrelia", "type": "Bacterium"}, {"text": "arthropod - borne bacteria", "type": "Bacterium"}, {"text": "vertebrates", "type": "Eukaryote"}]}

Example input:
Sentence: While the ticks collected from the horses were : Dermacentor nitens ( 41 . 5 % ) , A .

Example answer:
{"entities": [{"text": "ticks", "type": "Eukaryote"}, {"text": "horses", "type": "Eukaryote"}, {"text": "Dermacentor nitens", "type": "Eukaryote"}, {"text": "A .", "type": "Eukaryote"}]}

Input:
Sentence: They are mainly transmitted by ixodid or argasid ticks .

## Item MedMentions:test:3850
Example input:
Sentence: We found that Mep1A was a target of Reptin , a protein that is oncogenic in HCC .

Example answer:
{"entities": [{"text": "Mep1A", "type": "Chemical"}, {"text": "Reptin", "type": "Chemical"}, {"text": "protein that is oncogenic", "type": "Chemical"}, {"text": "HCC", "type": "BiologicFunction"}]}

Example input:
Sentence: c - Src Suppresses Dendritic Cell Antitumor Activity via T Cell Ig and Mucin Protein - 3 Receptor The enhanced expression of T cell Ig and mucin protein - 3 ( TIM - 3 ) on tumor - associated dendritic cells ( DCs ) attenuates antitumor effects of DNA vaccines .

Example answer:
{"entities": [{"text": "c - Src", "type": "AnatomicalStructure"}, {"text": "Dendritic Cell", "type": "AnatomicalStructure"}, {"text": "T Cell Ig and Mucin Protein - 3", "type": "Chemical"}, {"text": "Receptor", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "T cell Ig and mucin protein - 3", "type": "Chemical"}, {"text": "TIM - 3", "type": "Chemical"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "dendritic cells", "type": "AnatomicalStructure"}, {"text": "DCs", "type": "AnatomicalStructure"}, {"text": "DNA vaccines", "type": "Chemical"}]}

Example input:
Sentence: Mechanistic investigations show that SNHG12 is a direct transcriptional target of c - MYC .

Example answer:
{"entities": [{"text": "SNHG12", "type": "AnatomicalStructure"}, {"text": "transcriptional", "type": "BiologicFunction"}, {"text": "c - MYC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Importantly , triptolide showed superior activity in MYC - amplified PDX models and elicited rapid and profound depletion of the oncoprotein MYC , a transcriptional regulator .

Example answer:
{"entities": [{"text": "triptolide", "type": "Chemical"}, {"text": "MYC - amplified", "type": "Chemical"}, {"text": "PDX", "type": "Chemical"}, {"text": "models", "type": "IntellectualProduct"}, {"text": "oncoprotein MYC", "type": "Chemical"}, {"text": "transcriptional regulator", "type": "BiologicFunction"}]}

Example input:
Sentence: Taken together , the results of this study establish N - ( 1H - pyrazol - 3 - yl ) quinazolin - 4 - amines especially 3c and 3d as valuable lead molecules with great potential for CK1δ / ε inhibitor development targeting neurodegenerative disorders and cancer .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "N - ( 1H - pyrazol - 3 - yl ) quinazolin - 4 - amines", "type": "Chemical"}, {"text": "3c", "type": "Chemical"}, {"text": "3d", "type": "Chemical"}, {"text": "CK1δ", "type": "Chemical"}, {"text": "ε", "type": "Chemical"}, {"text": "inhibitor", "type": "Chemical"}, {"text": "neurodegenerative disorders", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: We recently reported that JQ1 decreased thyroid tumor growth and improved survival in a mouse model of anaplastic thyroid cancer ( ATC ) by targeting MYC transcription .

Example answer:
{"entities": [{"text": "recently reported", "type": "HealthCareActivity"}, {"text": "JQ1", "type": "Chemical"}, {"text": "thyroid tumor", "type": "BiologicFunction"}, {"text": "improved", "type": "Finding"}, {"text": "mouse model", "type": "BiologicFunction"}, {"text": "anaplastic thyroid cancer", "type": "BiologicFunction"}, {"text": "ATC", "type": "BiologicFunction"}, {"text": "MYC", "type": "AnatomicalStructure"}, {"text": "transcription", "type": "BiologicFunction"}]}

Example input:
Sentence: It remains to be elucidated on the role of MYC in human ATC and whether JQ1 could effectively target MYC as a novel treatment modality .

Example answer:
{"entities": [{"text": "MYC in human", "type": "Chemical"}, {"text": "ATC", "type": "BiologicFunction"}, {"text": "MYC", "type": "Chemical"}, {"text": "novel treatment modality", "type": "HealthCareActivity"}]}

Example input:
Sentence: Transactivation Domain of Human c - Myc Is Essential to Alleviate Poly ( Q ) -Mediated Neurotoxicity in Drosophila Disease Models Polyglutamine ( poly ( Q ) ) disorders , such as Huntington 's disease ( HD ) and spinocerebellar ataxias , represent a group of neurological disorders which arise due to an atypically expanded poly ( Q ) tract in the coding region of the affected gene .

Example answer:
{"entities": [{"text": "Transactivation", "type": "BiologicFunction"}, {"text": "Domain", "type": "SpatialConcept"}, {"text": "Human c - Myc", "type": "Chemical"}, {"text": "Poly ( Q )", "type": "Chemical"}, {"text": "Neurotoxicity", "type": "InjuryOrPoisoning"}, {"text": "Drosophila", "type": "Eukaryote"}, {"text": "Disease Models", "type": "BiologicFunction"}, {"text": "Polyglutamine", "type": "Chemical"}, {"text": "poly ( Q )", "type": "Chemical"}, {"text": "disorders", "type": "BiologicFunction"}, {"text": "Huntington 's disease", "type": "BiologicFunction"}, {"text": "HD", "type": "BiologicFunction"}, {"text": "spinocerebellar ataxias", "type": "BiologicFunction"}, {"text": "neurological disorders", "type": "BiologicFunction"}, {"text": "expanded", "type": "SpatialConcept"}, {"text": "coding region", "type": "AnatomicalStructure"}, {"text": "gene", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Our study suggests that strategies focussing on the transactivation domain of c - Myc could be a very useful approach to design novel drug molecules against poly ( Q ) disorders .

Example answer:
{"entities": [{"text": "transactivation", "type": "BiologicFunction"}, {"text": "domain", "type": "SpatialConcept"}, {"text": "c - Myc", "type": "Chemical"}, {"text": "drug molecules", "type": "Chemical"}, {"text": "poly ( Q )", "type": "Chemical"}, {"text": "disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: We report for the first time that similar to dmyc , tissue - specific induced expression of human c - myc also suppresses poly ( Q ) -mediated neurotoxicity by an analogous mechanism .

Example answer:
{"entities": [{"text": "dmyc", "type": "Chemical"}, {"text": "induced expression", "type": "BiologicFunction"}, {"text": "human c - myc", "type": "Chemical"}, {"text": "poly ( Q )", "type": "Chemical"}, {"text": "neurotoxicity", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: The present study examines the ability of the human c - myc proto - oncogene and also identifies the specific c - Myc isoform which drives the mitigation of poly ( Q ) -mediated neurotoxicity , so that it could be further substantiated as a potential drug target .

## Item MedMentions:test:4041
Example input:
Sentence: Vascular endothelial cells responded to membrane geometry by either forming vascular tubes that extended through the pore or completely filling membrane pores after 4 days in culture .

Example answer:
{"entities": [{"text": "Vascular endothelial cells", "type": "AnatomicalStructure"}, {"text": "vascular tubes", "type": "AnatomicalStructure"}, {"text": "extended", "type": "SpatialConcept"}]}

Example input:
Sentence: Polymer electrodes for long - term ECG measurements were fabricated by loading high content of carbon nanotubes ( CNTs ) in polydimethylsiloxane .

Example answer:
{"entities": [{"text": "Polymer", "type": "Chemical"}, {"text": "carbon nanotubes", "type": "Chemical"}, {"text": "CNTs", "type": "Chemical"}, {"text": "polydimethylsiloxane", "type": "Chemical"}]}

Example input:
Sentence: The papilla is made out of organic material and can be cut by high frequency current .

Example answer:
{"entities": [{"text": "papilla", "type": "AnatomicalStructure"}]}

Example input:
Sentence: With the braided tube , fluid in the gel construct was further removed by vacuum suction aiming to consolidate the concentric layers of the construct .

Example answer:
{"entities": [{"text": "gel", "type": "Chemical"}, {"text": "construct", "type": "MedicalDevice"}, {"text": "vacuum suction", "type": "MedicalDevice"}]}

Example input:
Sentence: Although tube formation began to predominate overgrowth around 75 μm and continued to increase at even larger pore sizes , tubes formed at these large pore sizes were not completely round and had relatively thin walls .

Example answer:
{"entities": [{"text": "overgrowth", "type": "Finding"}, {"text": "round", "type": "SpatialConcept"}, {"text": "walls", "type": "SpatialConcept"}]}

Example input:
Sentence: The resulting gel sheet was then wrapped around a custom - made multi - layered braided tube to form aligned tubular constructs whereas the gel sheet prepared similarly but without uniaxial stretching formed control constructs .

Example answer:
{"entities": [{"text": "gel", "type": "Chemical"}, {"text": "sheet", "type": "Chemical"}, {"text": "tubular constructs", "type": "MedicalDevice"}, {"text": "constructs", "type": "MedicalDevice"}]}

Example input:
Sentence: Evaluation of Drug Sorption to PVC - and Non - PVC -based Tubes in Administration Sets Using a Pump Administration sets are delivery tools for the direct application of drugs into the body and are composed of a spike , a drip chamber , tubes , Luer adapters ( connectors ) , a needle cover for protection , and other accessories .

Example answer:
{"entities": [{"text": "Evaluation", "type": "HealthCareActivity"}, {"text": "PVC", "type": "Chemical"}, {"text": "Tubes", "type": "MedicalDevice"}, {"text": "Administration Sets", "type": "MedicalDevice"}, {"text": "Pump", "type": "MedicalDevice"}, {"text": "Administration sets", "type": "MedicalDevice"}, {"text": "delivery tools", "type": "Chemical"}, {"text": "drugs", "type": "Chemical"}, {"text": "body", "type": "Eukaryote"}, {"text": "spike", "type": "MedicalDevice"}, {"text": "drip chamber", "type": "MedicalDevice"}, {"text": "tubes", "type": "MedicalDevice"}, {"text": "Luer adapters", "type": "MedicalDevice"}, {"text": "needle cover", "type": "MedicalDevice"}]}

Example input:
Sentence: Rapid Fabrication of a Cell - Seeded Collagen Gel -Based Tubular Construct that Withstands Arterial Pressure : Rapid Fabrication of a Gel -Based Media Equivalent Based on plastically compressed cell - seeded collagen gels , we fabricated a small - diameter tubular construct that withstands arterial pressure without prolonged culture in vitro .

Example answer:
{"entities": [{"text": "Cell", "type": "AnatomicalStructure"}, {"text": "Seeded", "type": "HealthCareActivity"}, {"text": "Collagen", "type": "Chemical"}, {"text": "Gel", "type": "Chemical"}, {"text": "Tubular Construct", "type": "MedicalDevice"}, {"text": "Arterial Pressure", "type": "BiologicFunction"}, {"text": "cell", "type": "AnatomicalStructure"}, {"text": "seeded", "type": "HealthCareActivity"}, {"text": "collagen", "type": "Chemical"}, {"text": "gels", "type": "Chemical"}, {"text": "tubular construct", "type": "MedicalDevice"}, {"text": "arterial pressure", "type": "BiologicFunction"}, {"text": "culture", "type": "HealthCareActivity"}]}

Example input:
Sentence: This study demonstrated that by combining stretch - induced fiber alignment , plastic compression , and enzyme -mediated crosslinking , a cell - seeded collagen gel -based tubular construct with potential to be used as vascular media can be made within 3 days .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "fiber", "type": "AnatomicalStructure"}, {"text": "enzyme", "type": "Chemical"}, {"text": "cell", "type": "AnatomicalStructure"}, {"text": "seeded", "type": "HealthCareActivity"}, {"text": "collagen", "type": "Chemical"}, {"text": "gel", "type": "Chemical"}, {"text": "tubular construct", "type": "MedicalDevice"}, {"text": "vascular media", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A tube of 5 mm in length was soaked in a fluid containing P .

Example answer:
{"entities": [{"text": "soaked", "type": "HealthCareActivity"}, {"text": "P .", "type": "Bacterium"}]}

Input:
Sentence: Tubes made of polyvinyl chloride ( PVC ) - and non - PVC -based polymeric materials were cut to 1 m in length .

## Item MedMentions:test:4106
Example input:
Sentence: In conclusion , iron deficiency is common during clinical remission in children with IBD , even in cohorts with low prevalence of anemia .

Example answer:
{"entities": [{"text": "iron deficiency", "type": "BiologicFunction"}, {"text": "remission", "type": "Finding"}, {"text": "IBD", "type": "BiologicFunction"}, {"text": "cohorts", "type": "PopulationGroup"}, {"text": "anemia", "type": "BiologicFunction"}]}

Example input:
Sentence: The findings from this study provide additional insight into the genetic exchange between attenuated and very virulent strains of IBDV circulating in the field .

Example answer:
{"entities": [{"text": "genetic exchange", "type": "BiologicFunction"}, {"text": "IBDV", "type": "Virus"}, {"text": "in the field", "type": "SpatialConcept"}]}

Example input:
Sentence: Testing the Ret and Sema3d genetic interaction in mouse enteric nervous system development For most multigenic disorders , clinical manifestation ( penetrance ) and presentation ( expressivity ) are likely to be an outcome of genetic interaction between multiple susceptibility genes .

Example answer:
{"entities": [{"text": "Ret", "type": "AnatomicalStructure"}, {"text": "Sema3d", "type": "AnatomicalStructure"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "enteric nervous system development", "type": "BiologicFunction"}, {"text": "multigenic disorders", "type": "BiologicFunction"}, {"text": "susceptibility genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The genetics literature for periodontal disease is more substantial than for caries and genes associated with chronic periodontitis are the vitamin D receptor ( VDR ) , Fc gamma receptor IIA ( Fc - γRIIA ) and Interleukin 10 ( IL10 ) genes .

Example answer:
{"entities": [{"text": "periodontal disease", "type": "BiologicFunction"}, {"text": "caries", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "chronic periodontitis", "type": "BiologicFunction"}, {"text": "vitamin D receptor", "type": "AnatomicalStructure"}, {"text": "VDR", "type": "AnatomicalStructure"}, {"text": "Fc gamma receptor IIA", "type": "AnatomicalStructure"}, {"text": "Fc - γRIIA", "type": "AnatomicalStructure"}, {"text": "Interleukin 10 ( IL10 ) genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Colitis was established in CD177 ( - / - ) and wild - type mice in response to dextran sulfate sodium ( DSS ) insults to determine the role of CD177 ( + ) neutrophils in IBD .

Example answer:
{"entities": [{"text": "Colitis", "type": "BiologicFunction"}, {"text": "CD177 ( - / - )", "type": "AnatomicalStructure"}, {"text": "wild - type mice", "type": "Eukaryote"}, {"text": "dextran sulfate sodium", "type": "Chemical"}, {"text": "DSS", "type": "Chemical"}, {"text": "CD177 ( + )", "type": "AnatomicalStructure"}, {"text": "neutrophils", "type": "AnatomicalStructure"}, {"text": "IBD", "type": "BiologicFunction"}]}

Example input:
Sentence: Many candidate genes have homologs identified in studies of human disease , suggesting that genes affecting variation in susceptibility are conserved across species .

Example answer:
{"entities": [{"text": "candidate genes", "type": "AnatomicalStructure"}, {"text": "homologs", "type": "SpatialConcept"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: However , the role of CD177 ( + ) neutrophils in pathogenesis of IBD remains elusive .

Example answer:
{"entities": [{"text": "CD177 ( + )", "type": "AnatomicalStructure"}, {"text": "neutrophils", "type": "AnatomicalStructure"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "IBD", "type": "BiologicFunction"}]}

Example input:
Sentence: Prevalence of afa8 , cdtB , eae , east1 , iroN , iss , kpsMTII , paa , sfa , tsh and papC genes did not differ significantly between herds with or without diarrhea .

Example answer:
{"entities": [{"text": "afa8", "type": "AnatomicalStructure"}, {"text": "cdtB", "type": "AnatomicalStructure"}, {"text": "east1", "type": "AnatomicalStructure"}, {"text": "iroN", "type": "AnatomicalStructure"}, {"text": "iss", "type": "AnatomicalStructure"}, {"text": "kpsMTII", "type": "AnatomicalStructure"}, {"text": "paa", "type": "AnatomicalStructure"}, {"text": "sfa", "type": "AnatomicalStructure"}, {"text": "tsh", "type": "AnatomicalStructure"}, {"text": "papC", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "diarrhea", "type": "Finding"}]}

Example input:
Sentence: A microbial signature for Crohn 's disease A decade of microbiome studies has linked IBD to an alteration in the gut microbial community of genetically predisposed subjects .

Example answer:
{"entities": [{"text": "Crohn 's disease", "type": "BiologicFunction"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "IBD", "type": "BiologicFunction"}, {"text": "gut", "type": "AnatomicalStructure"}, {"text": "subjects", "type": "PopulationGroup"}]}

Example input:
Sentence: RNA sequencing revealed that differential gene expression between CD177 ( + ) and CD177 ( - ) neutrophils from patients with IBD was associated with response to bacterial defence , hydrogen peroxide and reactive oxygen species ( ROS ) .

Example answer:
{"entities": [{"text": "RNA sequencing", "type": "HealthCareActivity"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "CD177 ( + )", "type": "AnatomicalStructure"}, {"text": "CD177 ( - )", "type": "AnatomicalStructure"}, {"text": "neutrophils", "type": "AnatomicalStructure"}, {"text": "IBD", "type": "BiologicFunction"}, {"text": "bacterial defence", "type": "BiologicFunction"}, {"text": "hydrogen peroxide", "type": "Chemical"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "ROS", "type": "Chemical"}]}

Input:
Sentence: Genetic studies have identified immune - related susceptibility genes that only partially overlap with those involved in IBD .

## Item MedMentions:test:3954
Example input:
Sentence: Here we show that Angptl4 - / - mice fed a diet rich in trans fatty acids develop numerous lipid -filled giant cells in their mesenteric lymph nodes , yet do not have elevated serum amyloid and haptoglobin , do not exhibit ascites , and survive , unlike Angptl4 - / - mice fed a saturated fatty acid -rich diet .

Example answer:
{"entities": [{"text": "Angptl4 - / -", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "diet", "type": "Food"}, {"text": "trans fatty acids", "type": "Chemical"}, {"text": "lipid", "type": "Chemical"}, {"text": "giant cells", "type": "AnatomicalStructure"}, {"text": "mesenteric lymph nodes", "type": "AnatomicalStructure"}, {"text": "serum", "type": "BodySubstance"}, {"text": "amyloid", "type": "Chemical"}, {"text": "haptoglobin", "type": "Chemical"}, {"text": "ascites", "type": "Finding"}, {"text": "saturated fatty acid", "type": "Food"}]}

Example input:
Sentence: High - performance liquid chromatography analyses of hamster ear extracts showed that OG treatment increased ACC levels and the ratio of acetyl - CoA to free CoA in these animals , indicating increased fatty acid oxidation .

Example answer:
{"entities": [{"text": "High - performance liquid chromatography analyses", "type": "HealthCareActivity"}, {"text": "hamster", "type": "Eukaryote"}, {"text": "ear", "type": "AnatomicalStructure"}, {"text": "OG", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "ACC", "type": "Chemical"}, {"text": "acetyl - CoA", "type": "Chemical"}, {"text": "free CoA", "type": "Chemical"}, {"text": "animals", "type": "Eukaryote"}, {"text": "fatty acid", "type": "Chemical"}, {"text": "oxidation", "type": "BiologicFunction"}]}

Example input:
Sentence: Further analysis of the fatty acid composition revealed that palmitic acid ( C16 : 0 ) and linolenic acid ( C18 : 3 ) increased significantly in the seeds of the transgenic rice lines , but oleic acid ( C18 : 1 ) levels significantly declined .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "fatty acid", "type": "Chemical"}, {"text": "palmitic acid", "type": "Chemical"}, {"text": "C16 : 0", "type": "Chemical"}, {"text": "linolenic acid", "type": "Chemical"}, {"text": "C18 : 3", "type": "Chemical"}, {"text": "seeds", "type": "Eukaryote"}, {"text": "transgenic", "type": "Eukaryote"}, {"text": "rice lines", "type": "Eukaryote"}, {"text": "oleic acid", "type": "Chemical"}, {"text": "C18 : 1", "type": "Chemical"}]}

Example input:
Sentence: After five days of feeding , weight of larvae and their survival rate was found to decrease with increasing JA concentrations in both broccoli cultivars .

Example answer:
{"entities": [{"text": "larvae", "type": "Eukaryote"}, {"text": "JA", "type": "Chemical"}, {"text": "broccoli cultivars", "type": "Eukaryote"}]}

Example input:
Sentence: As fish progressed through the harvest event , cook loss decreased , tenderness increased , and pH increased , indicating that stress induced textural changes .

Example answer:
{"entities": []}

Example input:
Sentence: Interestingly , the fatty acids profile showed differences between the two rotifer cultures : omega - 3 fatty acids were only observed in the Microalgae / rotifer , whereas , omega - 6 fatty acids presented similar levels in both rotifer cultures .

Example answer:
{"entities": [{"text": "fatty acids profile", "type": "HealthCareActivity"}, {"text": "rotifer", "type": "Eukaryote"}, {"text": "cultures", "type": "HealthCareActivity"}, {"text": "omega - 3 fatty acids", "type": "Chemical"}, {"text": "Microalgae", "type": "Eukaryote"}, {"text": "omega - 6 fatty acids", "type": "Chemical"}]}

Example input:
Sentence: The short - term effects of farmed fish food consumed by wild fish congregating outside the farms We simulated in the laboratory the possible effects on fatty acids and immune status of wild fish arriving for the first time in the vicinity of a sea - cage fish farm , shifting their natural diet to commercial feed consumption , rich in fatty acids of vegetable origin .

Example answer:
{"entities": [{"text": "farmed fish", "type": "Eukaryote"}, {"text": "food consumed", "type": "Food"}, {"text": "wild fish", "type": "Eukaryote"}, {"text": "farms", "type": "Organization"}, {"text": "laboratory", "type": "Organization"}, {"text": "fatty acids", "type": "Food"}, {"text": "immune status", "type": "ClinicalAttribute"}, {"text": "sea - cage fish farm", "type": "Organization"}, {"text": "natural diet", "type": "Food"}, {"text": "commercial", "type": "IntellectualProduct"}, {"text": "rich in fatty acids", "type": "Finding"}, {"text": "vegetable origin", "type": "Food"}]}

Example input:
Sentence: More research is needed in order to elucidate whether the rapid assimilation of the dietary fatty acids could harm the immune status of fish when feeding for longer periods than two months .

Example answer:
{"entities": [{"text": "dietary fatty acids", "type": "Chemical"}, {"text": "could harm", "type": "Finding"}, {"text": "immune status", "type": "ClinicalAttribute"}, {"text": "fish", "type": "Eukaryote"}]}

Example input:
Sentence: After 21 d of feeding , supplementation of oxidized fish oil increased the levels of malondialdehyde ( MDA ) , oxidized glutathione ( GSSG ) , interleukin - 1β ( IL - 1β ) , tumor necrosis factor - α ( TNF - α ) , interleukin - 2 ( IL - 2 ) , nuclear factor κ B ( NF - κB ) , inducible nitric oxide synthase ( iNOS ) , NO , and Caspase - 3 in jejunal mucosa , and decreased the villous height in duodenum and the levels of secretory immunoglobulin A ( sIgA ) and IL - 4 in the jejunal mucosa compared with supplementation with fresh oil .

Example answer:
{"entities": [{"text": "supplementation", "type": "HealthCareActivity"}, {"text": "oxidized", "type": "BiologicFunction"}, {"text": "fish oil", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "MDA", "type": "Chemical"}, {"text": "oxidized glutathione", "type": "Chemical"}, {"text": "GSSG", "type": "Chemical"}, {"text": "interleukin - 1β", "type": "Chemical"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "tumor necrosis factor - α", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "interleukin - 2", "type": "Chemical"}, {"text": "IL - 2", "type": "Chemical"}, {"text": "nuclear factor κ B", "type": "Chemical"}, {"text": "( NF - κB", "type": "Chemical"}, {"text": "inducible nitric oxide synthase", "type": "Chemical"}, {"text": "iNOS", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "Caspase - 3", "type": "Chemical"}, {"text": "jejunal mucosa", "type": "AnatomicalStructure"}, {"text": "villous", "type": "AnatomicalStructure"}, {"text": "duodenum", "type": "AnatomicalStructure"}, {"text": "secretory immunoglobulin A", "type": "Chemical"}, {"text": "( sIgA", "type": "Chemical"}, {"text": "IL - 4", "type": "Chemical"}, {"text": "oil", "type": "Chemical"}]}

Example input:
Sentence: Higher fish consumption ( at least 3 portions ) was associated with lower omega - 6 fatty acid levels ( p = 0 . 026 ) and higher omega - 3 fatty acid levels ( p = 0 . 037 ) , both results being statistically significant .

Example answer:
{"entities": [{"text": "fish consumption", "type": "BiologicFunction"}, {"text": "omega - 6 fatty acid", "type": "Chemical"}, {"text": "omega - 3 fatty acid", "type": "Chemical"}, {"text": "results", "type": "Finding"}]}

Input:
Sentence: The flesh fatty acid profile of golden mullet specimens was altered after 2weeks of commercial feed consumption , showing an increase in fatty acids of vegetable origin .

## Item MedMentions:test:4111
Example input:
Sentence: It often involves young patients sustaining multiple injuries , with a high associated mortality rate .

Example answer:
{"entities": [{"text": "multiple injuries", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The greatest burden appears for the most part in infants ( < 1 year ) in Bulgaria , Hungary , Latvia , Romania , and Serbia , but not in the other participating countries where the burden may have shifted to older children , though surveillance of adults may be inappropriate .

Example answer:
{"entities": [{"text": "Bulgaria", "type": "SpatialConcept"}, {"text": "Hungary", "type": "SpatialConcept"}, {"text": "Latvia", "type": "SpatialConcept"}, {"text": "Romania", "type": "SpatialConcept"}, {"text": "Serbia", "type": "SpatialConcept"}, {"text": "countries", "type": "SpatialConcept"}]}

Example input:
Sentence: Among PLHIV , 13 . 45 % of deaths were due to injury , compared to 5 . 52 % of deaths in the general population .

Example answer:
{"entities": [{"text": "PLHIV", "type": "BiologicFunction"}, {"text": "deaths", "type": "Finding"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "general population", "type": "PopulationGroup"}]}

Example input:
Sentence: Child death and maternal psychosis - like experiences in 44 low - and middle - income countries : The role of depression Studies on the effect of child death on the mental wellbeing of women in low - and middle - income countries ( LMICs ) are scarce despite the high child mortality rates .

Example answer:
{"entities": [{"text": "Child death", "type": "Finding"}, {"text": "maternal", "type": "Finding"}, {"text": "psychosis - like experiences", "type": "BiologicFunction"}, {"text": "low -", "type": "PopulationGroup"}, {"text": "countries", "type": "SpatialConcept"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "child death", "type": "Finding"}, {"text": "mental wellbeing", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "LMICs", "type": "SpatialConcept"}]}

Example input:
Sentence: The most common mechanisms of injury were road traffic injuries ( 36 . 8 % ) , falls ( 26 . 4 % ) , and being struck / hit by a person or object ( 20 .

Example answer:
{"entities": [{"text": "traffic injuries", "type": "InjuryOrPoisoning"}, {"text": "falls", "type": "InjuryOrPoisoning"}, {"text": "person", "type": "PopulationGroup"}]}

Example input:
Sentence: Rates and predictors of injury in a population - based cohort of people living with HIV Injuries are responsible for 10 % of the global burden of disease ; however , the epidemiology of injury among people living with HIV ( PLHIV ) has not been well elucidated .

Example answer:
{"entities": [{"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "people", "type": "PopulationGroup"}, {"text": "HIV", "type": "BiologicFunction"}, {"text": "Injuries", "type": "InjuryOrPoisoning"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "people living with HIV", "type": "BiologicFunction"}, {"text": "PLHIV", "type": "BiologicFunction"}]}

Example input:
Sentence: Hospital -based trauma registries can be important sources of data to study the epidemiology of injuries in low - and middle - income countries .

Example answer:
{"entities": [{"text": "Hospital", "type": "Organization"}, {"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "study the epidemiology", "type": "ResearchActivity"}, {"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "low - and middle - income countries", "type": "SpatialConcept"}]}

Example input:
Sentence: Epidemiology and outcomes of injuries in Kenya : A multisite surveillance study Injury is a leading cause of disability and death worldwide , accounting for over 5 million deaths each year .

Example answer:
{"entities": [{"text": "Epidemiology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "Kenya", "type": "SpatialConcept"}, {"text": "Injury", "type": "InjuryOrPoisoning"}, {"text": "disability", "type": "Finding"}, {"text": "death", "type": "Finding"}, {"text": "deaths", "type": "Finding"}]}

Example input:
Sentence: Kenya lacks robust data to describe injury epidemiology and care .

Example answer:
{"entities": [{"text": "Kenya", "type": "SpatialConcept"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "epidemiology", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Despite this burden , the use of prospective trauma registries to describe injury epidemiology and outcomes is limited in low - and middle - income countries .

Example answer:
{"entities": [{"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "epidemiology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "low - and middle - income countries", "type": "SpatialConcept"}]}

Input:
Sentence: The injury burden is higher in low - and middle - income countries where more than 90 % of injury -related deaths occur .

## Item MedMentions:test:4219
Example input:
Sentence: At time of return to sport , compliant athletes had full restoration of strength while noncompliant athletes had significant hamstring weakness , which was progressively worse at longer muscle lengths ( compliance × side × angle P = .006 ; involved vs noninvolved at 20 ° , compliant 7 % stronger , noncompliant 43 % weaker ) .

Example answer:
{"entities": [{"text": "athletes", "type": "ProfessionalOrOccupationalGroup"}, {"text": "restoration", "type": "HealthCareActivity"}, {"text": "strength", "type": "BiologicFunction"}, {"text": "worse", "type": "Finding"}, {"text": "muscle", "type": "AnatomicalStructure"}, {"text": "compliance", "type": "Finding"}, {"text": "side", "type": "SpatialConcept"}, {"text": "angle", "type": "SpatialConcept"}, {"text": "noncompliant", "type": "Finding"}]}

Example input:
Sentence: These findings suggest that if properly informed of the side effect profiles of these medications , many patients might opt for other treatments .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "side effect", "type": "BiologicFunction"}, {"text": "profiles", "type": "HealthCareActivity"}, {"text": "medications", "type": "Chemical"}, {"text": "treatments", "type": "HealthCareActivity"}]}

Example input:
Sentence: Significant effects favouring the intervention were noted for dynamic pain , patient satisfaction , occurrence of nausea and vomiting , occurrence of delirium or mental confusion and occurrence of pulmonary complications .

Example answer:
{"entities": [{"text": "intervention", "type": "HealthCareActivity"}, {"text": "dynamic pain", "type": "Finding"}, {"text": "vomiting", "type": "Finding"}, {"text": "delirium", "type": "BiologicFunction"}, {"text": "mental confusion", "type": "BiologicFunction"}, {"text": "pulmonary complications", "type": "BiologicFunction"}]}

Example input:
Sentence: In addition , the perception of side effects has changed owing to progress in supportive therapy in recent years .

Example answer:
{"entities": [{"text": "side effects", "type": "BiologicFunction"}, {"text": "supportive therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: The major clinical side effect is cardiotoxicity but the mechanism is largely unknown .

Example answer:
{"entities": [{"text": "side effect", "type": "BiologicFunction"}, {"text": "cardiotoxicity", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: No significant side effects were noted .

Example answer:
{"entities": [{"text": "side effects", "type": "BiologicFunction"}]}

Example input:
Sentence: Although the effects observed were not likely to negatively impact consumer acceptance , a strict management plan should be followed to maintain consistency in the product and avoid changes in stressors that might alter quality more drastically .

Example answer:
{"entities": [{"text": "negatively", "type": "Finding"}, {"text": "consumer", "type": "PopulationGroup"}]}

Example input:
Sentence: The side effect profile for divalproex sodium was associated with the smallest willingness to take , with gabapentin , propranolol , and topiramate perceived to be much more agreeable .

Example answer:
{"entities": [{"text": "side effect", "type": "BiologicFunction"}, {"text": "profile", "type": "HealthCareActivity"}, {"text": "divalproex sodium", "type": "Chemical"}, {"text": "smallest willingness to take", "type": "Finding"}, {"text": "gabapentin", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "topiramate", "type": "Chemical"}]}

Example input:
Sentence: Side effects were significantly more frequent in deviated cases ( 8 / 10 ; 80 % ) than in non - deviated ( 7 / 27 ; 25 . 9 % ) ( p = 0 . 003 ) .

Example answer:
{"entities": [{"text": "Side effects", "type": "BiologicFunction"}]}

Example input:
Sentence: Despite beneficial effects , its administration can lead to severe side effects including hyperparathyroidism , renal and thyroid disorders .

Example answer:
{"entities": [{"text": "administration", "type": "HealthCareActivity"}, {"text": "hyperparathyroidism", "type": "BiologicFunction"}, {"text": "renal", "type": "BiologicFunction"}, {"text": "thyroid disorders", "type": "BiologicFunction"}]}

Input:
Sentence: Its frequent side effects greatly reduce its probable compliance and therefore do not reveal a significant effect .

## Item MedMentions:test:3915
Example input:
Sentence: EU - AIR , comprising of 19 centres across Germany , the Netherlands , Sweden and the UK , commenced enrolling patients with AI in August 2012 .

Example answer:
{"entities": [{"text": "EU - AIR", "type": "IntellectualProduct"}, {"text": "centres", "type": "Organization"}, {"text": "Germany", "type": "SpatialConcept"}, {"text": "Netherlands", "type": "SpatialConcept"}, {"text": "Sweden", "type": "SpatialConcept"}, {"text": "UK", "type": "SpatialConcept"}, {"text": "AI", "type": "BiologicFunction"}]}

Example input:
Sentence: Secondary contacts were inferred between the Southern / Central Iberian populations and Eastern Iberian cluster as well as between the two Pyrenean ones .

Example answer:
{"entities": []}

Example input:
Sentence: Our results imply that Southern Italy is becoming a reservoir for X .

Example answer:
{"entities": [{"text": "Southern Italy", "type": "SpatialConcept"}, {"text": "reservoir", "type": "SpatialConcept"}, {"text": "X .", "type": "Bacterium"}]}

Example input:
Sentence: Based on species distribution modeling and molecular markers , we identified the glacial refugia and the postglacial migration routes of the species to Central Europe .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "modeling", "type": "ResearchActivity"}, {"text": "molecular markers", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Data from the 9306 participants were categorized by 5 regions : Asia ( n = 552 ) ; Europe ( n = 4909 ) ; Latin America ( n = 1406 ) ; North America ( n = 2146 ) ; and Australia , New Zealand , and South Africa ( n = 293 ) .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "regions", "type": "SpatialConcept"}, {"text": "Asia", "type": "SpatialConcept"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "Latin America", "type": "SpatialConcept"}, {"text": "North America", "type": "SpatialConcept"}, {"text": "Australia", "type": "SpatialConcept"}, {"text": "New Zealand", "type": "SpatialConcept"}, {"text": "South Africa", "type": "SpatialConcept"}]}

Example input:
Sentence: In Europe , relicts of other groups can be found in local populations along the Mediterranean Sea .

Example answer:
{"entities": [{"text": "Europe", "type": "SpatialConcept"}, {"text": "relicts", "type": "Eukaryote"}, {"text": "found in", "type": "SpatialConcept"}, {"text": "local", "type": "SpatialConcept"}, {"text": "Mediterranean Sea", "type": "SpatialConcept"}]}

Example input:
Sentence: This study highlighted that OPEs are subject to long - range transport via both air and seawater from the European continent and seas to the North Atlantic and the Arctic .

Example answer:
{"entities": [{"text": "OPEs", "type": "Chemical"}, {"text": "European", "type": "SpatialConcept"}, {"text": "continent", "type": "SpatialConcept"}, {"text": "seas", "type": "SpatialConcept"}, {"text": "North Atlantic", "type": "SpatialConcept"}, {"text": "Arctic", "type": "SpatialConcept"}]}

Example input:
Sentence: Species distribution modeling and molecular markers suggest longitudinal range shifts and cryptic northern refugia of the typical calcareous grassland species Hippocrepis comosa ( horseshoe vetch ) Calcareous grasslands belong to the most diverse , endangered habitats in Europe , but there is still insufficient information about the origin of the plant species related to these grasslands .

Example answer:
{"entities": [{"text": "Species", "type": "IntellectualProduct"}, {"text": "modeling", "type": "ResearchActivity"}, {"text": "molecular markers", "type": "ClinicalAttribute"}, {"text": "calcareous grassland", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Hippocrepis comosa", "type": "Eukaryote"}, {"text": "horseshoe vetch", "type": "Eukaryote"}, {"text": "Calcareous grasslands", "type": "SpatialConcept"}, {"text": "endangered habitats", "type": "SpatialConcept"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "plant", "type": "Eukaryote"}, {"text": "grasslands", "type": "SpatialConcept"}]}

Example input:
Sentence: The analysis showed a distinct separation of the southern refugia into a western cluster embracing Iberia and an eastern group including the Balkans and Italy , which determined the postglacial recolonization of Central Europe .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "Iberia", "type": "SpatialConcept"}, {"text": "eastern", "type": "SpatialConcept"}, {"text": "Balkans", "type": "SpatialConcept"}, {"text": "Italy", "type": "SpatialConcept"}]}

Example input:
Sentence: We clearly demonstrate that H . comosa followed a latitudinal and due to its oceanity also a longitudinal gradient during the last glacial maximum ( LGM ) , restricting the species to southern refugia situated on the Peninsulas of Iberia , the Balkans , and Italy during the last glaciation .

Example answer:
{"entities": [{"text": "H . comosa", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Peninsulas of Iberia", "type": "SpatialConcept"}, {"text": "Balkans", "type": "SpatialConcept"}, {"text": "Italy", "type": "SpatialConcept"}]}

Input:
Sentence: comosa seems to have expanded from the Iberian refugium , to Central and Northern Europe , including the UK , Belgium , and Germany .

## Item MedMentions:test:4171
Example input:
Sentence: A high proportion of patients with recurrent episodes of NTM infection or a history of zoster and dNTM infection had initial nAIGA titers ≥10 dilution ( P < 0 .

Example answer:
{"entities": [{"text": "NTM", "type": "Bacterium"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "zoster", "type": "BiologicFunction"}, {"text": "dNTM", "type": "Bacterium"}, {"text": "nAIGA titers", "type": "HealthCareActivity"}]}

Example input:
Sentence: ClinicalTrials . gov Identifier NCT01973907 , registered on 23 October 2013 .

Example answer:
{"entities": []}

Example input:
Sentence: Trial registration Chinese Clinical Trial Registry ChiCTR - TRC - 13003583 , Registered 20 Aug , 2013 .

Example answer:
{"entities": []}

Example input:
Sentence: cIAI , NCT01445665 and NCT01445678 ( both trials registered prospectively on September 26 , 2011 ) ; cUTI , NCT01345929 and NCT01345955 ( both trials registered prospectively on April 28 , 2011 ) .

Example answer:
{"entities": [{"text": "cIAI", "type": "BiologicFunction"}, {"text": "cUTI", "type": "BiologicFunction"}]}

Example input:
Sentence: The BUMPES Trial is registered with Current Controlled Trials : ISRCTN35706297 , 26 ( th ) August 2009 .

Example answer:
{"entities": [{"text": "BUMPES Trial", "type": "ResearchActivity"}, {"text": "registered", "type": "HealthCareActivity"}, {"text": "Current Controlled Trials", "type": "ResearchActivity"}]}

Example input:
Sentence: This trial was registered under IRCT201212232602N11 .

Example answer:
{"entities": [{"text": "trial", "type": "ResearchActivity"}, {"text": "registered", "type": "HealthCareActivity"}]}

Example input:
Sentence: The trial is registered with IRCT201109267647N1 .

Example answer:
{"entities": [{"text": "trial", "type": "ResearchActivity"}, {"text": "registered", "type": "HealthCareActivity"}]}

Example input:
Sentence: NTR5568 .

Example answer:
{"entities": []}

Example input:
Sentence: ClinicalTrials . gov , registered on March 12 , 2014 , identifier : NCT02087592 . World Health Organization Trial Registration , registered on 3 August 2015 , identifier : NCT02087592 .

Example answer:
{"entities": [{"text": "World Health Organization", "type": "Organization"}]}

Example input:
Sentence: This study was registered at the Netherlands Trial Register [ NTR2153 ] on the 5 ( th ) of January 2010 .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "registered", "type": "IntellectualProduct"}, {"text": "Netherlands Trial Register", "type": "IntellectualProduct"}, {"text": "NTR2153", "type": "IntellectualProduct"}]}

Input:
Sentence: Dutch Trial Register NTR - 5597 .

## Item MedMentions:test:4038
Example input:
Sentence: 3 mins / d sitting . After controlling for age and sex , individuals in higher income groups compared with the lowest income group , living in nonmetro Seoul compared with metro Seoul , and who were overweight compared with nonoverweight were more likely to meet PA guidelines .

Example answer:
{"entities": [{"text": "sitting", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "higher income groups", "type": "PopulationGroup"}, {"text": "lowest income group", "type": "PopulationGroup"}, {"text": "Seoul", "type": "SpatialConcept"}, {"text": "overweight", "type": "Finding"}, {"text": "guidelines", "type": "IntellectualProduct"}]}

Example input:
Sentence: The food consumption data were obtained from the Shanghai Food Consumption Survey ( SHFCS ) of 2012 - 14 including a total of 1973 participants aged 2 - 90 years .

Example answer:
{"entities": [{"text": "Shanghai Food Consumption Survey", "type": "IntellectualProduct"}, {"text": "SHFCS", "type": "IntellectualProduct"}, {"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: Data from the National Health and Nutrition Examination Survey ( NHANES ) 2011 to 2012 were analyzed .

Example answer:
{"entities": [{"text": "National Health and Nutrition Examination Survey", "type": "ResearchActivity"}, {"text": "NHANES", "type": "ResearchActivity"}]}

Example input:
Sentence: Data in adolescents aged 10 - 19 years came from China ( 1997 - 2011 , n = 8025 ) , Korea ( 1998 - 2012 , n = 10 119 ) , Seychelles ( 1998 - 2012 , n = 27 569 ) and the United States of America ( 1999 - 2012 , n = 14 580 ) .

Example answer:
{"entities": [{"text": "China", "type": "SpatialConcept"}, {"text": "Korea", "type": "SpatialConcept"}, {"text": "Seychelles", "type": "SpatialConcept"}, {"text": "United States of America", "type": "SpatialConcept"}]}

Example input:
Sentence: An online survey was conducted of newly licensed registered nurses who had obtained their license in 2012 or 2013 in South Korea and had been working for 5 - 12 months after first being employed .

Example answer:
{"entities": [{"text": "online survey", "type": "IntellectualProduct"}, {"text": "licensed", "type": "IntellectualProduct"}, {"text": "registered nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "license", "type": "IntellectualProduct"}, {"text": "South Korea", "type": "SpatialConcept"}, {"text": "employed", "type": "Finding"}]}

Example input:
Sentence: Prevalence of Physical Activity and Sitting Time Among South Korean Adolescents : Results From the Korean National Health and Nutrition Examination Survey , 2013 This study aimed to describe physical activity ( PA ) and sitting time , and to examine associations between sociodemographic factors , weight status , PA , and sitting time among South Korean adolescents ( 12 - 18 years ) .

Example answer:
{"entities": [{"text": "Sitting", "type": "BiologicFunction"}, {"text": "South Korean", "type": "PopulationGroup"}, {"text": "Korean", "type": "PopulationGroup"}, {"text": "National Health and Nutrition Examination Survey", "type": "ResearchActivity"}, {"text": "sitting", "type": "BiologicFunction"}]}

Example input:
Sentence: Shift Work Is Associated with Metabolic Syndrome in Young Female Korean Workers Shift work is associated with health problems , including metabolic syndrome .

Example answer:
{"entities": [{"text": "Metabolic Syndrome", "type": "BiologicFunction"}, {"text": "Korean", "type": "PopulationGroup"}, {"text": "metabolic syndrome", "type": "BiologicFunction"}]}

Example input:
Sentence: Participants were adults aged ≥20 years from the cross - sectional National Health and Nutrition Examination Surveys , 1988 - 2012 ( N = 49 770 ) .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "cross - sectional National Health and Nutrition Examination Surveys", "type": "ResearchActivity"}]}

Example input:
Sentence: Findings are based on self - report data from 638 participants in the 2013 Korea National Health and Nutrition Examination Survey .

Example answer:
{"entities": [{"text": "self - report data", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "Korea", "type": "SpatialConcept"}, {"text": "National Health and Nutrition Examination Survey", "type": "ResearchActivity"}]}

Example input:
Sentence: This study analysed the data from a one day 24 - hour dietary recall as well as a demographic survey of 1 , 738 Korean adolescents aged 12 to 18 - years -old obtained from the 2010 - 2012 Korea National Health and Nutrition Examination Survey . ' Night eating ' was defined as consuming 25 % or more of one 's daily energy intake between 21 : 00 and 06 : 00 .

Example answer:
{"entities": [{"text": "study", "type": "IntellectualProduct"}, {"text": "dietary recall", "type": "ResearchActivity"}, {"text": "demographic survey", "type": "ResearchActivity"}, {"text": "Korean", "type": "PopulationGroup"}, {"text": "Korea", "type": "SpatialConcept"}, {"text": "National Health and Nutrition Examination Survey", "type": "ResearchActivity"}, {"text": "eating", "type": "BiologicFunction"}]}

Input:
Sentence: A total of 3 , 317 subjects aged 20 - 40 years enrolled in the 2011 - 2012 Korean National Health and Nutrition Examination Survey were divided into shift and day workers .

## Item MedMentions:test:3840
Example input:
Sentence: Systemic Deregulation of Autophagy Upon Loss of ALS - and FTD -linked C9orf72 A genetic mutation in the C9orf72 gene causes the most common forms of neurodegenerative diseases amyotrophic lateral sclerosis ( ALS ) and frontotemporal dementia ( FTD ) .

Example answer:
{"entities": [{"text": "Autophagy", "type": "BiologicFunction"}, {"text": "ALS", "type": "BiologicFunction"}, {"text": "FTD", "type": "BiologicFunction"}, {"text": "C9orf72", "type": "AnatomicalStructure"}, {"text": "genetic mutation", "type": "BiologicFunction"}, {"text": "C9orf72 gene", "type": "AnatomicalStructure"}, {"text": "neurodegenerative diseases", "type": "BiologicFunction"}, {"text": "amyotrophic lateral sclerosis", "type": "BiologicFunction"}, {"text": "frontotemporal dementia", "type": "BiologicFunction"}]}

Example input:
Sentence: The CLASP2 Protein Interaction Network in Adipocytes Links CLIP2 to AGAP3 , CLASP2 to G2L1 , MARK2 , and SOGA1 , and Identifies SOGA1 as a Microtubule - Associated Protein CLASP2 is a microtubule - associated protein that undergoes insulin - stimulated phosphorylation and co - localization with reorganized actin and GLUT4 at the plasma membrane .

Example answer:
{"entities": [{"text": "CLASP2", "type": "Chemical"}, {"text": "Adipocytes", "type": "AnatomicalStructure"}, {"text": "CLIP2", "type": "Chemical"}, {"text": "AGAP3", "type": "Chemical"}, {"text": "G2L1", "type": "Chemical"}, {"text": "MARK2", "type": "Chemical"}, {"text": "SOGA1", "type": "Chemical"}, {"text": "Microtubule - Associated Protein", "type": "Chemical"}, {"text": "microtubule - associated protein", "type": "Chemical"}, {"text": "insulin", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "actin", "type": "Chemical"}, {"text": "GLUT4", "type": "Chemical"}, {"text": "plasma membrane", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Pathogenesis of these disorders inside the cells begins with the assembly of these mutant proteins in the form of insoluble inclusion bodies ( IBs ) , which progressively sequester several vital cellular transcription factors and other essential proteins , and finally leads to neuronal dysfunction and apoptosis .

Example answer:
{"entities": [{"text": "Pathogenesis", "type": "BiologicFunction"}, {"text": "disorders", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "mutant proteins", "type": "Chemical"}, {"text": "inclusion bodies", "type": "AnatomicalStructure"}, {"text": "IBs", "type": "AnatomicalStructure"}, {"text": "cellular", "type": "AnatomicalStructure"}, {"text": "transcription factors", "type": "Chemical"}, {"text": "proteins", "type": "Chemical"}, {"text": "neuronal", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: From a review of the recent literature and our own published work including aggregation kinetics and structural morphology , Aβ clearance , molecular simulations , long - term potentiation measurements with inhibition binding , and the binding of a commercial monoclonal antibody , aducanumab , we hypothesize that the N - terminal domains of neurotoxic Aβ oligomers are implicated in causing the disease .

Example answer:
{"entities": [{"text": "literature", "type": "IntellectualProduct"}, {"text": "published work", "type": "IntellectualProduct"}, {"text": "structural", "type": "SpatialConcept"}, {"text": "Aβ", "type": "Chemical"}, {"text": "simulations", "type": "ResearchActivity"}, {"text": "long - term potentiation", "type": "BiologicFunction"}, {"text": "inhibition binding", "type": "BiologicFunction"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "monoclonal antibody", "type": "Chemical"}, {"text": "aducanumab", "type": "Chemical"}, {"text": "N - terminal domains", "type": "SpatialConcept"}, {"text": "Aβ oligomers", "type": "Chemical"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Therefore , we tested whether a more stable and easier - to - synthesize modified version of NQTrp , containing a Cl ion , namely Cl - NQTrp , is also an effective inhibitor of tau aggregation in vitro and in vivo .

Example answer:
{"entities": [{"text": "NQTrp", "type": "Chemical"}, {"text": "Cl ion", "type": "Chemical"}, {"text": "Cl - NQTrp", "type": "Chemical"}, {"text": "tau", "type": "Chemical"}, {"text": "aggregation", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: We present pulsed double electron - electron resonance measurements of two key fibril - forming regions of tau , PHF6 and PHF6 * , in transient as aggregation happens .

Example answer:
{"entities": [{"text": "pulsed double electron - electron resonance", "type": "HealthCareActivity"}, {"text": "fibril", "type": "AnatomicalStructure"}, {"text": "regions", "type": "SpatialConcept"}, {"text": "tau", "type": "Chemical"}, {"text": "PHF6", "type": "Chemical"}, {"text": "PHF6 *", "type": "Chemical"}]}

Example input:
Sentence: We demonstrate that Cl - NQTrp inhibits the in vitro assembly of PHF6 , the aggregation -prone fragment of tau , and alleviates tauopathy symptoms in a transgenic Drosophila model through the inhibition of tau aggregation -engendered toxicity .

Example answer:
{"entities": [{"text": "Cl - NQTrp", "type": "Chemical"}, {"text": "PHF6", "type": "Chemical"}, {"text": "aggregation", "type": "BiologicFunction"}, {"text": "fragment", "type": "Chemical"}, {"text": "tau", "type": "Chemical"}, {"text": "tauopathy", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "transgenic", "type": "Eukaryote"}, {"text": "Drosophila", "type": "Eukaryote"}, {"text": "model", "type": "BiologicFunction"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Cl - NQTrp Alleviates Tauopathy Symptoms in a Model Organism through the Inhibition of Tau Aggregation -Engendered Toxicity Alzheimer 's disease ( AD ) is the most abundant tauopathy and is characterized by Aβ -derived plaques and tau -derived tangles , resulting from the unfolding of the corresponding monomeric subunits into ordered β - sheet oligomers and fibrils .

Example answer:
{"entities": [{"text": "Cl - NQTrp", "type": "Chemical"}, {"text": "Tauopathy", "type": "BiologicFunction"}, {"text": "Symptoms", "type": "Finding"}, {"text": "Model Organism", "type": "BiologicFunction"}, {"text": "Tau", "type": "Chemical"}, {"text": "Aggregation", "type": "BiologicFunction"}, {"text": "Toxicity", "type": "InjuryOrPoisoning"}, {"text": "Alzheimer 's disease", "type": "BiologicFunction"}, {"text": "AD", "type": "BiologicFunction"}, {"text": "tauopathy", "type": "BiologicFunction"}, {"text": "plaques", "type": "AnatomicalStructure"}, {"text": "tau", "type": "Chemical"}, {"text": "tangles", "type": "BiologicFunction"}, {"text": "unfolding", "type": "BiologicFunction"}, {"text": "monomeric subunits", "type": "Chemical"}, {"text": "β - sheet", "type": "SpatialConcept"}, {"text": "fibrils", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The mechanism by which tau self - assembles into pathological entities is a matter of much debate , largely due to the lack of direct experimental insights into the earliest stages of aggregation .

Example answer:
{"entities": [{"text": "tau", "type": "Chemical"}, {"text": "insights", "type": "BiologicFunction"}]}

Example input:
Sentence: Combined with simulations , our experiments show that the extended β - strand conformational state of PHF6 ( ( * ) ) is readily populated under aggregating conditions , constituting a defining signature of aggregation - prone tau , and as such , a possible target for therapeutic interventions .

Example answer:
{"entities": [{"text": "simulations", "type": "ResearchActivity"}, {"text": "experiments", "type": "ResearchActivity"}, {"text": "extended", "type": "SpatialConcept"}, {"text": "β - strand conformational", "type": "SpatialConcept"}, {"text": "PHF6 ( ( * ) )", "type": "Chemical"}, {"text": "signature", "type": "SpatialConcept"}, {"text": "prone", "type": "SpatialConcept"}, {"text": "tau", "type": "Chemical"}, {"text": "therapeutic interventions", "type": "HealthCareActivity"}]}

Input:
Sentence: Signature of an aggregation - prone conformation of tau The self - assembly of the microtubule associated tau protein into fibrillar cell inclusions is linked to a number of devastating neurodegenerative disorders collectively known as tauopathies .

## Item MedMentions:test:4281
Example input:
Sentence: Parental depressive and posttraumatic stress symptoms were associated with impairments in social emotional adjustment in young children , increased anxiety in early childhood , and adjustment problems in school - age children .

Example answer:
{"entities": [{"text": "depressive", "type": "BiologicFunction"}, {"text": "posttraumatic stress symptoms", "type": "BiologicFunction"}, {"text": "emotional", "type": "Finding"}, {"text": "anxiety", "type": "Finding"}]}

Example input:
Sentence: When children had a negative relationship with their parent , a supportive message of that parent decreased working memory performance , while a supportive message from the teacher increased performance .

Example answer:
{"entities": [{"text": "negative", "type": "Finding"}, {"text": "supportive", "type": "HealthCareActivity"}, {"text": "message", "type": "IntellectualProduct"}, {"text": "working memory", "type": "BiologicFunction"}, {"text": "performance", "type": "BiologicFunction"}, {"text": "teacher", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: The findings suggest four main social processes that influence parents ' talk with their children about parental mental health issues , namely " Protecting and being protected , " " Responding to children 's search for understanding , " " Prioritizing family life , " and " Relating to others . " Implications of the findings for clinical practice and future research are considered .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "mental health issues", "type": "Finding"}, {"text": "Protecting", "type": "BiologicFunction"}, {"text": "being protected", "type": "BiologicFunction"}, {"text": "understanding", "type": "BiologicFunction"}, {"text": "research", "type": "ResearchActivity"}]}

Example input:
Sentence: Lastly , the children 's age and gender did not seem to have an impact on agreement .

Example answer:
{"entities": []}

Example input:
Sentence: Results from a UK clinical sample Discrepancies are often found between child and parent reports of child psychopathology , nevertheless the role of the child 's presenting difficulties in relation to these is underexplored .

Example answer:
{"entities": [{"text": "UK", "type": "SpatialConcept"}, {"text": "Discrepancies", "type": "Finding"}, {"text": "found", "type": "Finding"}, {"text": "reports", "type": "IntellectualProduct"}, {"text": "presenting difficulties", "type": "Finding"}]}

Example input:
Sentence: These findings demonstrate that certain child presenting difficulties , and in particular conduct problems , may be related to informant agreement and need to be considered in clinical practice and research .

Example answer:
{"entities": [{"text": "presenting difficulties", "type": "Finding"}, {"text": "conduct problems", "type": "Finding"}, {"text": "research", "type": "ResearchActivity"}]}

Example input:
Sentence: The findings revealed that parent - youth conflict predicted greater differences in parent - youth familism values , but differences in familism values did not predict conflict .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}]}

Example input:
Sentence: This study investigates whether parent - child agreement on the conduct and emotional scales of the Strengths and Difficulties Questionnaire ( SDQ ) varied as a result of certain child characteristics , including the child 's presenting problems to clinical services , age and gender .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "conduct", "type": "IntellectualProduct"}, {"text": "emotional scales", "type": "IntellectualProduct"}, {"text": "Strengths and Difficulties Questionnaire", "type": "IntellectualProduct"}, {"text": "SDQ", "type": "IntellectualProduct"}, {"text": "presenting problems", "type": "Finding"}, {"text": "clinical services", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using correlation analysis , the main findings indicated that agreement varied as a result of the child 's difficulties for reports of conduct problems , and this seemed to be related to the presence or absence of externalising difficulties in the child 's presentation .

Example answer:
{"entities": [{"text": "correlation analysis", "type": "ResearchActivity"}, {"text": "indicated", "type": "Finding"}, {"text": "reports", "type": "IntellectualProduct"}, {"text": "conduct problems", "type": "Finding"}, {"text": "presence", "type": "Finding"}, {"text": "externalising difficulties", "type": "Finding"}]}

Example input:
Sentence: In addition , agreement was higher when reporting problems not consistent with the child 's presentation ; for instance , agreement on conduct problems was greater for children presenting with internalising problems .

Example answer:
{"entities": [{"text": "reporting", "type": "HealthCareActivity"}, {"text": "problems", "type": "Finding"}, {"text": "conduct problems", "type": "Finding"}, {"text": "internalising problems", "type": "Finding"}]}

Input:
Sentence: Does parent - child agreement vary based on presenting problems ?

## Item MedMentions:test:3760
Example input:
Sentence: Cardiovascular diseases related to ionizing radiation : The risk of low - dose exposure ( Review ) Traditionally , non - cancer diseases are not considered as health risks following exposure to low doses of ionizing radiation .

Example answer:
{"entities": [{"text": "Cardiovascular diseases", "type": "BiologicFunction"}, {"text": "Review", "type": "IntellectualProduct"}, {"text": "non - cancer", "type": "Finding"}, {"text": "diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Due to limited statistical power , the dose - risk relationship is undetermined below 0 . 5 Gy ; however , if this relationship proves to be without a threshold , it may have considerable impact on current low ‑ dose health risk estimates .

Example answer:
{"entities": [{"text": "statistical power", "type": "ResearchActivity"}]}

Example input:
Sentence: We also analyze radiosensitivity at other doses ( 0 . 2 - 15 Gy ) , to represent hypo - and hyperfractionation doses and determined that RDE is dose dependent : high ratios at low doses , and approaching 1 at high doses .

Example answer:
{"entities": [{"text": "hypo", "type": "HealthCareActivity"}, {"text": "low doses", "type": "HealthCareActivity"}]}

Example input:
Sentence: Establishment of a mouse model of 70 % lethal dose by total - body irradiation Whereas increasing concerns about radiation exposure to nuclear disasters or side effects of anticancer radiotherapy , relatively little research for radiation damages or remedy has been done .

Example answer:
{"entities": [{"text": "mouse model", "type": "BiologicFunction"}, {"text": "total - body irradiation", "type": "HealthCareActivity"}, {"text": "radiation exposure", "type": "InjuryOrPoisoning"}, {"text": "side effects", "type": "BiologicFunction"}, {"text": "anticancer", "type": "HealthCareActivity"}, {"text": "radiotherapy", "type": "HealthCareActivity"}, {"text": "research", "type": "ResearchActivity"}, {"text": "radiation damages", "type": "BiologicFunction"}]}

Example input:
Sentence: We examine radiosensitivity at the dose of 2 Gy , a routinely administered dose during fractionated radiotherapy , and we determined that a wide range of DSBs were induced by the given dose among healthy individuals , with highly radiosensitive individuals harboring more IR - induced breaks in the genome than radioresistant individuals following exposure to the same dose .

Example answer:
{"entities": [{"text": "fractionated radiotherapy", "type": "HealthCareActivity"}, {"text": "DSBs", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "exposure to", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Recent epidemiological findings point , however , to an excess risk of non - cancer diseases following exposure to lower doses of ionizing radiation than was previously thought .

Example answer:
{"entities": [{"text": "non - cancer", "type": "Finding"}, {"text": "diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: The radiation dose imparted to members of public due to the levels observed is well within station technical specification limit for 3H .

Example answer:
{"entities": [{"text": "members of public", "type": "Organization"}, {"text": "3H", "type": "Chemical"}]}

Example input:
Sentence: It is judged that below an absorbed dose of 100 mGy , no clinically relevant tissue damage occurs , forming the basis for the current radiation protection system concerning non - cancer effects .

Example answer:
{"entities": [{"text": "tissue damage", "type": "InjuryOrPoisoning"}, {"text": "radiation protection system", "type": "HealthCareActivity"}]}

Example input:
Sentence: Results of the work done so far support the idea that low doses of radiation have effects that differ from those associated with high dose exposures ; this work , however , is far from sufficient for the development of a new theoretical framework needed for the understanding of low dose radiation exposures .

Example answer:
{"entities": [{"text": "exposures", "type": "InjuryOrPoisoning"}, {"text": "theoretical framework", "type": "IntellectualProduct"}, {"text": "radiation exposures", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Mechanistic understanding of radiation effects at low doses is necessary in order to develop better radiation protection policy .

Example answer:
{"entities": [{"text": "radiation protection", "type": "HealthCareActivity"}, {"text": "policy", "type": "IntellectualProduct"}]}

Input:
Sentence: Limits for radiation exposures are legally regulated ; however , current radiation protection policy does not explicitly acknowledge that biological , cellular and molecular effects of low doses and low dose rates of radiation differ from effects induced by medium and high dose radiation exposures .

## Item MedMentions:test:4162
Example input:
Sentence: Time to DKA resolution was decreased ( P = 0 . 04 ) , and hypoglycaemia was increased ( P = 0 . 0022 ) .

Example answer:
{"entities": [{"text": "DKA", "type": "BiologicFunction"}, {"text": "hypoglycaemia", "type": "BiologicFunction"}]}

Example input:
Sentence: Over 4 years ( between Jan 2011 and Jan 2015 ) , all cases of severe hypospadias were included in this study ; except those with prior attempts at repair , circumcised cases , and cases with severe hypogonadism - because of partial androgen insensitivity - not responding to hormonal manipulations .

Example answer:
{"entities": [{"text": "hypospadias", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "attempts at repair", "type": "HealthCareActivity"}, {"text": "circumcised", "type": "Finding"}, {"text": "hypogonadism", "type": "BiologicFunction"}, {"text": "partial androgen insensitivity", "type": "BiologicFunction"}, {"text": "hormonal manipulations", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients with hyperkalemia had a lower risk of developing mild ( odds ratio [ OR ] , 0 .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Finding"}]}

Example input:
Sentence: Other indications were the treatment of functional impairment resulting from dystonia ( 26 . 25 % ) , sialorrhea ( 18 . 75 % ) , freezing of gait , and camptocormia .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "dystonia", "type": "Finding"}, {"text": "sialorrhea", "type": "BiologicFunction"}, {"text": "freezing of gait", "type": "Finding"}, {"text": "camptocormia", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Dengue with hypokalemia had less myalgia , more of hyporeflexia , and lower serum CK compared to those without hypokalemia .

Example answer:
{"entities": [{"text": "Dengue", "type": "BiologicFunction"}, {"text": "hypokalemia", "type": "Finding"}, {"text": "myalgia", "type": "Finding"}, {"text": "hyporeflexia", "type": "Finding"}, {"text": "serum", "type": "BodySubstance"}, {"text": "CK", "type": "Chemical"}]}

Example input:
Sentence: Even though events were rare , patients with severe hypokalemia ( potassium levels ≤ 3 .

Example answer:
{"entities": [{"text": "hypokalemia", "type": "Finding"}, {"text": "potassium levels", "type": "Finding"}]}

Example input:
Sentence: We reviewed a consecutive series of patients who had potassium testing within 48 hours of undergoing DSE for the evaluation of myocardial ischemia over a 10 - year period ( N = 13 , 198 ) .

Example answer:
{"entities": [{"text": "consecutive series of patients", "type": "ResearchActivity"}, {"text": "potassium", "type": "Chemical"}, {"text": "DSE", "type": "HealthCareActivity"}, {"text": "evaluation", "type": "HealthCareActivity"}, {"text": "myocardial ischemia", "type": "BiologicFunction"}]}

Example input:
Sentence: Along with the notion that a timely diagnosis entails a fundamental step for the choice of an appropriate therapy , which can correct the arterial hypertension and the hypokalemia , this justifies efforts to search for PA in the majority of the patients with hypertension .

Example answer:
{"entities": [{"text": "diagnosis", "type": "HealthCareActivity"}, {"text": "therapy", "type": "HealthCareActivity"}, {"text": "arterial hypertension", "type": "BiologicFunction"}, {"text": "hypokalemia", "type": "Finding"}, {"text": "search", "type": "HealthCareActivity"}, {"text": "PA", "type": "BiologicFunction"}, {"text": "hypertension", "type": "BiologicFunction"}]}

Example input:
Sentence: While remaining at relatively low risk , patients with very low potassium levels ( ≤3 . 1 mmol / L ) at the time of DSE have a modestly increased risk of arrhythmia .

Example answer:
{"entities": [{"text": "potassium levels", "type": "Finding"}, {"text": "DSE", "type": "HealthCareActivity"}, {"text": "arrhythmia", "type": "Finding"}]}

Example input:
Sentence: DSE is safe even in the setting of abnormalities in blood potassium concentrations , and hence cancellation of DSE in patients with potassium abnormalities does not appear warranted .

Example answer:
{"entities": [{"text": "DSE", "type": "HealthCareActivity"}, {"text": "abnormalities", "type": "Finding"}, {"text": "blood potassium concentrations", "type": "Finding"}, {"text": "potassium", "type": "Chemical"}]}

Input:
Sentence: Consideration could be given to correcting severe hypokalemia prior to DSE .

## Item MedMentions:test:4103
Example input:
Sentence: We used data from five cohorts , including data from 16 developed and developing countries : ELSA ( English Longitudinal Study of Aging ) , HRS ( Health and Retirement Study ) , MHAS ( Mexican Health and Aging Study ) , SABE - Sao Paulo ( The Health , Well - being and Aging ) , and SHARE ( Survey on Health , Ageing and Retirement in Europe ) .

Example answer:
{"entities": [{"text": "cohorts", "type": "PopulationGroup"}, {"text": "ELSA", "type": "ResearchActivity"}, {"text": "English Longitudinal Study of Aging", "type": "ResearchActivity"}, {"text": "HRS", "type": "ResearchActivity"}, {"text": "Health and Retirement Study", "type": "ResearchActivity"}, {"text": "MHAS", "type": "ResearchActivity"}, {"text": "Mexican Health and Aging Study", "type": "ResearchActivity"}, {"text": "SABE - Sao Paulo", "type": "ResearchActivity"}, {"text": "The Health , Well - being and Aging", "type": "ResearchActivity"}, {"text": "SHARE", "type": "ResearchActivity"}, {"text": "Survey on Health , Ageing and Retirement in Europe", "type": "ResearchActivity"}]}

Example input:
Sentence: This study represents the largest series of North American patients reviewed to date .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "North American", "type": "SpatialConcept"}]}

Example input:
Sentence: Ninety - two patients with severe OSAHS were consecutively enrolled between September 2014 and February 2016 and compared to age - , sex - , and body mass index ( BMI ) - matched controls .

Example answer:
{"entities": [{"text": "OSAHS", "type": "BiologicFunction"}, {"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: This was a large , single - center , retrospective 5 - year cohort study at St . Luke 's International Hospital , Tokyo , Japan , between 2004 and 2009 .

Example answer:
{"entities": [{"text": "single - center", "type": "Organization"}, {"text": "St . Luke 's International Hospital", "type": "Organization"}, {"text": "Tokyo", "type": "SpatialConcept"}, {"text": "Japan", "type": "SpatialConcept"}]}

Example input:
Sentence: The current study used the Surveillance , Epidemiology , and End Results ( SEER ) - Consumer Assessment of Healthcare Providers and Systems ( CAHPS ) data set , a new data resource linking patient - reported information from the CAHPS Medicare Survey with clinical information from the National Cancer Institute 's SEER program .

Example answer:
{"entities": [{"text": "Surveillance , Epidemiology , and End Results", "type": "Organization"}, {"text": "SEER", "type": "Organization"}, {"text": "Consumer Assessment of Healthcare Providers and Systems", "type": "Organization"}, {"text": "CAHPS", "type": "Organization"}, {"text": "data set", "type": "IntellectualProduct"}, {"text": "resource linking patient - reported information", "type": "IntellectualProduct"}, {"text": "Medicare Survey", "type": "ResearchActivity"}, {"text": "clinical information", "type": "IntellectualProduct"}, {"text": "National Cancer Institute 's", "type": "Organization"}, {"text": "SEER program", "type": "Organization"}]}

Example input:
Sentence: We conducted a population - based case - control study of 5 , 950 , 391 patients using the 2014 Healthcare Cost and Utilization Project ( HCUP ) , Nationwide Inpatient Survey ( NIS ) discharge records of patients 18 years and older .

Example answer:
{"entities": [{"text": "population - based case - control study", "type": "ResearchActivity"}, {"text": "Nationwide Inpatient Survey", "type": "IntellectualProduct"}, {"text": "NIS", "type": "IntellectualProduct"}, {"text": "discharge records", "type": "IntellectualProduct"}]}

Example input:
Sentence: Using data obtained by the Surveillance , Epidemiology , and End Results ( SEER ) program from 2010 - 2012 , a retrospective , population - based cohort study was conducted to investigate tumor subtype - specific differences in various characteristics , overall survival ( OS ) and breast cancer - specific mortality ( BCSM ) between males and females .

Example answer:
{"entities": [{"text": "Surveillance , Epidemiology , and End Results ( SEER ) program", "type": "Organization"}, {"text": "population - based cohort study", "type": "ResearchActivity"}, {"text": "tumor subtype", "type": "IntellectualProduct"}]}

Example input:
Sentence: Prospective database and retrospective data collection and clinical outcomes were evaluated for all 44 patients .

Example answer:
{"entities": [{"text": "Prospective database", "type": "IntellectualProduct"}, {"text": "retrospective data collection", "type": "ResearchActivity"}, {"text": "evaluated", "type": "HealthCareActivity"}]}

Example input:
Sentence: Retrospective cohort study using baseline data on the 83 545 UK Biobank participants with detailed mental health and birth weight data .

Example answer:
{"entities": [{"text": "UK", "type": "SpatialConcept"}, {"text": "Biobank", "type": "Organization"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "mental health", "type": "BiologicFunction"}]}

Example input:
Sentence: We conducted a retrospective claims database study using data from the Truven Health MarketScan database .

Example answer:
{"entities": [{"text": "database", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "Truven Health MarketScan database", "type": "IntellectualProduct"}]}

Input:
Sentence: This retrospective study utilized a patient database at a national weight management service ( WMS ) .

## Item MedMentions:test:4254
Example input:
Sentence: This study provides a novel approach to exploit the history of physical illnesses extracted from EMR ( ICD - 10 codes without chapter V - mental and behavioral disorders ) to predict suicide risk , and this model outperforms existing clinical assessments of suicide risk .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "history", "type": "Finding"}, {"text": "physical illnesses", "type": "BiologicFunction"}, {"text": "EMR", "type": "IntellectualProduct"}, {"text": "without chapter V - mental and behavioral disorders", "type": "Finding"}, {"text": "suicide risk", "type": "Finding"}, {"text": "assessments", "type": "HealthCareActivity"}]}

Example input:
Sentence: Subjective improvement was reported by 18 ( 90 % ) of the 20 included patients .

Example answer:
{"entities": []}

Example input:
Sentence: The pooled odds ratios ( ORs ) of relapse rates and Hedges 's g , along with 95 % confidence intervals ( CIs ) , for the mean differences in the levels of depression , mania , and psychosocial functioning were calculated .

Example answer:
{"entities": [{"text": "levels of depression", "type": "Finding"}, {"text": "mania", "type": "BiologicFunction"}]}

Example input:
Sentence: We used history of physical illnesses ( except chapter V : Mental and behavioral disorders ) from EMR data over different time - periods to build a lookup table that contains the probability of suicide risk for each chapter of the International Statistical Classification of Diseases and Related Health Problems , 10th Revision ( ICD - 10 ) codes .

Example answer:
{"entities": [{"text": "history", "type": "Finding"}, {"text": "physical illnesses", "type": "BiologicFunction"}, {"text": "except chapter V : Mental and behavioral disorders", "type": "Finding"}, {"text": "EMR", "type": "IntellectualProduct"}, {"text": "lookup table", "type": "IntellectualProduct"}, {"text": "suicide risk", "type": "Finding"}, {"text": "International Statistical Classification of Diseases and Related Health Problems , 10th Revision ( ICD - 10 )", "type": "IntellectualProduct"}]}

Example input:
Sentence: This strategy involved the development of an evidence - based order set , which included elements of symptom assessment and management , patient and family education , and spiritual and emotional support .

Example answer:
{"entities": [{"text": "evidence - based order set", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "symptom assessment", "type": "HealthCareActivity"}, {"text": "family education", "type": "HealthCareActivity"}, {"text": "spiritual", "type": "HealthCareActivity"}, {"text": "emotional support", "type": "HealthCareActivity"}]}

Example input:
Sentence: For mental health and substance use services , three classes emerged ( stable - low , 69 % and 61 % , respectively ; low - baseline - increase , 10 % and 12 % , respectively ; high - baseline decline , 21 % and 28 % , respectively ) .

Example answer:
{"entities": [{"text": "mental health", "type": "BiologicFunction"}, {"text": "services", "type": "HealthCareActivity"}]}

Example input:
Sentence: We hypothesized that patients with more disability and those with anxiety or depressive symptoms would have greater expectations .

Example answer:
{"entities": [{"text": "disability", "type": "Finding"}, {"text": "anxiety", "type": "Finding"}, {"text": "depressive symptoms", "type": "Finding"}]}

Example input:
Sentence: Other than ' moral reasoning ' ( median ( md ) : 45 % of the spoken time ) , the Moral Case Deliberations consisted of ' reflections on the psychosocial work environment ' to a varying extent ( md : 29 % ) .

Example answer:
{"entities": [{"text": "moral reasoning", "type": "BiologicFunction"}, {"text": "psychosocial work", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Before and after the intervention , an Empathy Scale in Patient Care ( ES - PC ) , a critical thinking disposition assessment ( CTDA - R ) , and a reflective writing test were administered to both groups .

Example answer:
{"entities": [{"text": "intervention", "type": "HealthCareActivity"}, {"text": "Empathy Scale", "type": "IntellectualProduct"}, {"text": "Patient Care", "type": "HealthCareActivity"}, {"text": "ES", "type": "IntellectualProduct"}, {"text": "PC", "type": "HealthCareActivity"}, {"text": "critical thinking disposition assessment", "type": "HealthCareActivity"}, {"text": "CTDA - R", "type": "HealthCareActivity"}]}

Example input:
Sentence: Video -based problem - based learning displayed significantly higher achievement rates for imagining authentic patients ( p = 0 . 001 ) , incorporating a comprehensive approach including psychosocial aspects ( p < 0 . 001 ) , and satisfaction with sessions ( p = 0 . 001 ) .

Example answer:
{"entities": [{"text": "Video", "type": "IntellectualProduct"}, {"text": "achievement rates", "type": "Finding"}]}

Input:
Sentence: Additional content comprised ' assumptions about the patient 's psychosocial situation ' ( md : 6 % ) , ' facts about the patient 's situation ' ( md : 5 % ) , ' concrete problem - solving ' ( md : 6 % ) and ' process ' ( md : 3 % ) .

## Item MedMentions:test:3911
Example input:
Sentence: The primary outcome of the study was feasibility of image transfer and performing navigated laser photocoagulation for subjects with diabetic macular edema between two distant clinics .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "image", "type": "IntellectualProduct"}, {"text": "navigated laser photocoagulation", "type": "HealthCareActivity"}, {"text": "subjects", "type": "PopulationGroup"}, {"text": "diabetic macular edema", "type": "BiologicFunction"}, {"text": "distant", "type": "SpatialConcept"}, {"text": "clinics", "type": "Organization"}]}

Example input:
Sentence: In 2012 the patient underwent percutaneous transhepatic biliary drainage for bile duct stricture , complicated with acute pancreatitis .

Example answer:
{"entities": [{"text": "percutaneous transhepatic biliary drainage", "type": "HealthCareActivity"}, {"text": "bile duct stricture", "type": "BiologicFunction"}, {"text": "acute pancreatitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Treatment after explantation included posterior chamber IOL implantation in 44 eyes ( 63 . 8 % ) and aphakia in 25 eyes ( 36 . 2 % ) .

Example answer:
{"entities": [{"text": "Treatment after explantation", "type": "HealthCareActivity"}, {"text": "posterior chamber IOL implantation", "type": "HealthCareActivity"}, {"text": "eyes", "type": "AnatomicalStructure"}, {"text": "aphakia", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Only 1 of 11 patients ( 9 % ) had recurrence of macular fluid ( 14 months postoperatively ) .

Example answer:
{"entities": [{"text": "macular fluid", "type": "BodySubstance"}]}

Example input:
Sentence: Well , I Wouldn ' t be Any Worse Off , Would I , Than I am Now ? A Qualitative Study of Decision - Making , Hopes , and Realities of Adults With Type 1 Diabetes Undergoing Islet Cell Transplantation For selected individuals with type 1 diabetes , pancreatic islet transplantation ( IT ) prevents recurrent severe hypoglycemia and optimizes glycemia , although ongoing systemic immunosuppression is needed .

Example answer:
{"entities": [{"text": "Qualitative Study", "type": "ResearchActivity"}, {"text": "Decision - Making", "type": "BiologicFunction"}, {"text": "Hopes", "type": "BiologicFunction"}, {"text": "Type 1 Diabetes", "type": "BiologicFunction"}, {"text": "Islet Cell Transplantation", "type": "HealthCareActivity"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "type 1 diabetes", "type": "BiologicFunction"}, {"text": "pancreatic islet transplantation", "type": "HealthCareActivity"}, {"text": "IT", "type": "HealthCareActivity"}, {"text": "hypoglycemia", "type": "BiologicFunction"}, {"text": "optimizes glycemia", "type": "HealthCareActivity"}, {"text": "systemic immunosuppression", "type": "HealthCareActivity"}]}

Example input:
Sentence: A Revised Approach for the Detection of Sight - Threatening Diabetic Macular Edema Diabetic macular edema is one of the leading causes of vision loss among working - age adults in the United States .

Example answer:
{"entities": [{"text": "Diabetic macular edema", "type": "BiologicFunction"}, {"text": "vision loss", "type": "BiologicFunction"}, {"text": "United States", "type": "SpatialConcept"}]}

Example input:
Sentence: Diabetic retinopathy and progression following treatment after pancreas transplantation were measured .

Example answer:
{"entities": [{"text": "Diabetic retinopathy", "type": "BiologicFunction"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "pancreas transplantation", "type": "HealthCareActivity"}]}

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
Sentence: In this retrospective observational study , diabetic patients who underwent pancreas transplantation in a single medical center and developed symptomatic acute macular edema and peripapillary soft exudate within 3 months after the operation were enrolled .

## Item MedMentions:test:4374
Example input:
Sentence: The age range was 53 - 80 years with a mean of 65 .

Example answer:
{"entities": []}

Example input:
Sentence: 2139 . 5 person - years , with a maximum of 6 . 66 years follow - up time .

Example answer:
{"entities": [{"text": "person", "type": "PopulationGroup"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: The patients qualifying for MVD were generally healthier and younger , with a mean age ± SD of 57±14 , compared to those undergoing RF ( 75±15 ) or SRS ( 73±13 , p < 0 . 0001 ) .

Example answer:
{"entities": [{"text": "MVD", "type": "HealthCareActivity"}, {"text": "RF", "type": "HealthCareActivity"}, {"text": "SRS", "type": "HealthCareActivity"}]}

Example input:
Sentence: Retrospective study of patients aged 5 - 19 years who underwent WBS .

Example answer:
{"entities": [{"text": "Retrospective study", "type": "ResearchActivity"}, {"text": "WBS", "type": "HealthCareActivity"}]}

Example input:
Sentence: The mean age was 58 . 8 ( SD 10 . 9 ) years old .

Example answer:
{"entities": []}

Example input:
Sentence: This retrospective study was performed with ( 99m ) Tc - DMSA SPECT images of 316 patients ( age range , 1 - 26 years ) .

Example answer:
{"entities": [{"text": "retrospective study", "type": "ResearchActivity"}, {"text": "( 99m ) Tc - DMSA", "type": "Chemical"}, {"text": "SPECT", "type": "HealthCareActivity"}, {"text": "images", "type": "IntellectualProduct"}]}

Example input:
Sentence: 3 % were male with a mean ± SD age of 28 .

Example answer:
{"entities": []}

Example input:
Sentence: Interviewees were aged ( mean ± SD ) 52 ± 10 years ( range , 30 - 64 ) ; duration of diabetes , 36 ± 9 years ( range , 21 - 56 ) ; 12 ( 75 % ) were women .

Example answer:
{"entities": [{"text": "Interviewees", "type": "PopulationGroup"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: 4 years , 42 [ 84 % ] male ) , 26 ( 52 % ) fully completed both phases .

Example answer:
{"entities": []}

Example input:
Sentence: The mean ( SD ) age was 19 ( 13 . 96 ) years .

Example answer:
{"entities": []}

Input:
Sentence: 32 years , SD = .48 , at Wave 3 ) who participated in Waves 3 - 5

## Item MedMentions:test:4322
Example input:
Sentence: The diagnosis of TB was supported by microbiological evidence of alcohol acid - fast Bacilli present in sputum smear ( 21 % ) , histological diagnosis ( 31 . 6 % ) , polymerase chain reaction ( 21 % ) , and imaging in ( 26 . 3 % ) .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "microbiological", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "alcohol acid - fast Bacilli present in sputum smear", "type": "Finding"}, {"text": "polymerase chain reaction", "type": "ResearchActivity"}, {"text": "imaging in", "type": "HealthCareActivity"}]}

Example input:
Sentence: Among children ( N = 455 ) evaluated for presumptive TB , 70 . 3 % ( 320 / 455 ) had Xpert and 62 .

Example answer:
{"entities": [{"text": "Xpert", "type": "HealthCareActivity"}]}

Example input:
Sentence: This finding did not support the hypothesis that malnourishment was an important causative factor for the development of active TB among patients in this study .

Example answer:
{"entities": [{"text": "finding", "type": "Finding"}, {"text": "malnourishment", "type": "BiologicFunction"}, {"text": "causative factor", "type": "Finding"}, {"text": "active TB", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Patients with TB had 22 % ( 95 % CI 19 - 25 ) lower body weight , 22 % ( 95 % CI 20 - 25 ) lower body mass index and 22 % ( 95 % CI 19 - 24 ) lower mid - upper arm circumference than healthy controls ( P < 0 . 001 ) ; household contacts and healthy controls were comparable for all measures .

Example answer:
{"entities": [{"text": "TB", "type": "BiologicFunction"}, {"text": "lower body weight", "type": "Finding"}, {"text": "lower body mass index", "type": "Finding"}, {"text": "lower mid - upper arm circumference", "type": "Finding"}]}

Example input:
Sentence: TB can be difficult to diagnose based only on the clinical signs ; therefore , it is usually diagnosed in the field with the tuberculin skin test and diagnostic blood tests , including the lymphocyte proliferation assay , the interferon ( IFN ) - γ assay , and enzyme - linked immunosorbent assay .

Example answer:
{"entities": [{"text": "TB", "type": "BiologicFunction"}, {"text": "diagnose", "type": "Finding"}, {"text": "clinical signs", "type": "Finding"}, {"text": "diagnosed", "type": "Finding"}, {"text": "tuberculin skin test", "type": "HealthCareActivity"}, {"text": "diagnostic blood tests", "type": "HealthCareActivity"}, {"text": "lymphocyte proliferation assay", "type": "HealthCareActivity"}, {"text": "interferon ( IFN ) - γ", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "enzyme - linked immunosorbent assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: Spinal TB ( Pott 's disease ) accounts for 50 % of skeletal TB .

Example answer:
{"entities": [{"text": "Spinal TB", "type": "BiologicFunction"}, {"text": "Pott 's disease", "type": "BiologicFunction"}]}

Example input:
Sentence: A 30 - minute visual health education was given on TB in English , followed by general pictorial presentation , and the data were collected as pre - test and post - test .

Example answer:
{"entities": [{"text": "TB", "type": "BiologicFunction"}, {"text": "pictorial presentation", "type": "IntellectualProduct"}]}

Example input:
Sentence: tb DK9897 infected animals .

Example answer:
{"entities": [{"text": "tb DK9897", "type": "Bacterium"}]}

Example input:
Sentence: tuberculosis and M .

Example answer:
{"entities": [{"text": "tuberculosis", "type": "Bacterium"}, {"text": "M .", "type": "Bacterium"}]}

Example input:
Sentence: A study on knowledge and awareness about tuberculosis in senior school children in Bangalore , India Tuberculosis ( TB ) is an infectious disease caused by Mycobacterium tuberculosis ( M . tuberculosis ) , commonly affecting the lungs .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "knowledge", "type": "IntellectualProduct"}, {"text": "awareness", "type": "BiologicFunction"}, {"text": "tuberculosis", "type": "BiologicFunction"}, {"text": "Bangalore", "type": "SpatialConcept"}, {"text": "India", "type": "SpatialConcept"}, {"text": "Tuberculosis", "type": "BiologicFunction"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "infectious disease", "type": "BiologicFunction"}, {"text": "Mycobacterium tuberculosis", "type": "Bacterium"}, {"text": "M . tuberculosis", "type": "Bacterium"}, {"text": "lungs", "type": "AnatomicalStructure"}]}

Input:
Sentence: tb .

## Item MedMentions:test:4133
Example input:
Sentence: Structural Insight into Recognition of Methylated Histone H3K4 by Set3 The plant homeodomain ( PHD ) finger of Set3 binds methylated lysine 4 of histone H3 in vitro and in vivo ; however , precise selectivity of this domain has not been fully characterized .

Example answer:
{"entities": [{"text": "Structural Insight", "type": "Finding"}, {"text": "Methylated Histone H3K4", "type": "BiologicFunction"}, {"text": "Set3", "type": "SpatialConcept"}, {"text": "plant homeodomain ( PHD ) finger", "type": "SpatialConcept"}, {"text": "binds methylated lysine 4 of histone H3", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "domain", "type": "SpatialConcept"}]}

Example input:
Sentence: Design , synthesis and anti - tumor activity study of novel histone deacetylase inhibitors containing isatin -based caps and o - phenylenediamine -based zinc binding groups As a hot topic of epigenetic studies , histone deacetylases ( HDACs ) are related to lots of diseases , especially cancer .

Example answer:
{"entities": [{"text": "anti - tumor activity", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "histone deacetylase inhibitors", "type": "Chemical"}, {"text": "isatin", "type": "Chemical"}, {"text": "o - phenylenediamine", "type": "Chemical"}, {"text": "epigenetic studies", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "histone deacetylases", "type": "Chemical"}, {"text": "HDACs", "type": "Chemical"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Western blot analysis and immunohistochemistry were used to analyse expression of EphB1 receptor as well as the activation of the glial cells and the pro - inflammatory cytokines in the spinal cord .

Example answer:
{"entities": [{"text": "Western blot analysis", "type": "HealthCareActivity"}, {"text": "immunohistochemistry", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "EphB1 receptor", "type": "Chemical"}, {"text": "glial cells", "type": "AnatomicalStructure"}, {"text": "pro - inflammatory cytokines", "type": "Chemical"}, {"text": "spinal cord", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In vitro and cell -based assays demonstrate that p21 is a novel and direct ubiquitylation substrate of CHIP that also requires the CHIP - associated chaperone HSP70 .

Example answer:
{"entities": [{"text": "cell", "type": "AnatomicalStructure"}, {"text": "assays", "type": "HealthCareActivity"}, {"text": "p21", "type": "Chemical"}, {"text": "ubiquitylation", "type": "BiologicFunction"}, {"text": "CHIP", "type": "Chemical"}, {"text": "chaperone", "type": "Chemical"}, {"text": "HSP70", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , western blotting was used to analyze levels of proteins related to PI3K / Akt - 1 signaling pathway , and results indicated that ost can increase p - Akt and PI3K .

Example answer:
{"entities": [{"text": "western blotting", "type": "HealthCareActivity"}, {"text": "analyze", "type": "HealthCareActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "PI3K / Akt - 1 signaling pathway", "type": "BiologicFunction"}, {"text": "ost", "type": "Chemical"}, {"text": "p - Akt", "type": "Chemical"}, {"text": "PI3K", "type": "Chemical"}]}

Example input:
Sentence: The data described here provide a mass spectrometry -based quantitative analysis of hPTMs from formalin - fixed paraffin - embedded ( FFPE ) tissues , from which histones were extracted through the recently developed PAT - H - MS method .

Example answer:
{"entities": [{"text": "mass spectrometry", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "hPTMs", "type": "BiologicFunction"}, {"text": "formalin - fixed paraffin - embedded ( FFPE ) tissues", "type": "AnatomicalStructure"}, {"text": "histones", "type": "Chemical"}, {"text": "extracted", "type": "HealthCareActivity"}, {"text": "PAT - H - MS method", "type": "HealthCareActivity"}]}

Example input:
Sentence: Surprisingly , we found that U7 base - pairing with nascent histone transcripts was not required for localization to HLBs .

Example answer:
{"entities": [{"text": "base - pairing", "type": "BiologicFunction"}, {"text": "nascent histone transcripts", "type": "Chemical"}, {"text": "localization", "type": "BiologicFunction"}, {"text": "HLBs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In addition , we applied this optimized method in in vitro experiment and clinical trial of Chidamide ( the only China FDA approved HDACi ) , the result of which confirmed that the flow cytometry -based method for detecting histone acetylation levels is a reliable , fast and convenient method which can be used in basic and clinical research .

Example answer:
{"entities": [{"text": "method", "type": "IntellectualProduct"}, {"text": "experiment", "type": "ResearchActivity"}, {"text": "clinical trial", "type": "ResearchActivity"}, {"text": "Chidamide", "type": "Chemical"}, {"text": "China", "type": "SpatialConcept"}, {"text": "FDA approved HDACi", "type": "IntellectualProduct"}, {"text": "confirmed", "type": "Finding"}, {"text": "flow cytometry", "type": "HealthCareActivity"}, {"text": "detecting", "type": "Finding"}, {"text": "histone acetylation", "type": "BiologicFunction"}, {"text": "basic", "type": "ResearchActivity"}, {"text": "clinical research", "type": "ResearchActivity"}]}

Example input:
Sentence: Quantitative regulation of histone variant H2A .

Example answer:
{"entities": [{"text": "regulation", "type": "BiologicFunction"}, {"text": "histone variant H2A .", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , we demonstrate that cell - free histone H2A released during dengue infection binds to platelets , increasing platelet activation .

Example answer:
{"entities": [{"text": "cell - free histone H2A", "type": "Chemical"}, {"text": "dengue infection", "type": "BiologicFunction"}, {"text": "binds", "type": "BiologicFunction"}, {"text": "platelets", "type": "AnatomicalStructure"}, {"text": "platelet activation", "type": "BiologicFunction"}]}

Input:
Sentence: Histone H2A ubiquitination levels were analyzed by Western blot after acidic extraction of core histones .

## Item MedMentions:test:4401
Example input:
Sentence: RESULTS There were 173 males and 227 females ( average age : 63 .

Example answer:
{"entities": []}

Example input:
Sentence: A sample of 125 children , ranging in age from 0 - 17 years , among seven group homes ( group A ) was compared with 121 children of the general population we ( group B ) .

Example answer:
{"entities": [{"text": "group homes", "type": "Organization"}, {"text": "general population", "type": "PopulationGroup"}]}

Example input:
Sentence: 9 to 3 . 9 in 55 - 69 year - olds and 1 .

Example answer:
{"entities": []}

Example input:
Sentence: Thirty - one children with a median age of 32 .

Example answer:
{"entities": []}

Example input:
Sentence: A cross - sectional study was conducted in 9618 children and adolescents ( 55 . 7 % girls ; age range of 9 - 17 .

Example answer:
{"entities": [{"text": "cross - sectional study", "type": "ResearchActivity"}]}

Example input:
Sentence: There were 11 men and 3 women with a mean age of 35 , 6 years ( range 19 - 66 years ) .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: The sample is composed of 7 , 058 school children aged between 8 and 13 years old .

Example answer:
{"entities": []}

Example input:
Sentence: There were 711 males ( 46 % ) and 835 females ( 54 % ) ( mean age 4 . 56 ±2 . 26 years ) .

Example answer:
{"entities": []}

Example input:
Sentence: 11 males ( 20 . 3 ± 0 . 8 years , 57 . 2 ± 7 .

Example answer:
{"entities": []}

Example input:
Sentence: The patient group consisted of 50 ( 52 . 6 % ) boys and 45 ( 47 . 4 % ) girls with a mean age of 125 ±38 months old .

Example answer:
{"entities": []}

Input:
Sentence: Fifty - six children ( 26 boys , mean age 10 .

## Item MedMentions:test:3871
Example input:
Sentence: Estimated glomerular filtration rate ( eGFR ) decreased in the control arm ( p = 0 . 007 ) , but did not change in the switch arm .

Example answer:
{"entities": [{"text": "Estimated glomerular filtration rate", "type": "HealthCareActivity"}, {"text": "eGFR", "type": "HealthCareActivity"}, {"text": "not change", "type": "Finding"}]}

Example input:
Sentence: Cox regression analysis revealed that postoperative AKI , preoperative eGFR , and histologic score of non - neoplastic kidney were the independent predictors for CKD .

Example answer:
{"entities": [{"text": "Cox regression analysis", "type": "IntellectualProduct"}, {"text": "AKI", "type": "InjuryOrPoisoning"}, {"text": "eGFR", "type": "HealthCareActivity"}, {"text": "non - neoplastic kidney", "type": "AnatomicalStructure"}, {"text": "CKD", "type": "BiologicFunction"}]}

Example input:
Sentence: The Pre - Eclampsia Ontology : A Disease Ontology Representing the Domain Knowledge Specific to Pre - Eclampsia Pre - eclampsia ( PE ) is a clinical syndrome characterized by new - onset hypertension and proteinuria at ≥20 weeks of gestation , and is a leading cause of maternal and perinatal morbidity and mortality .

Example answer:
{"entities": [{"text": "Pre - Eclampsia", "type": "BiologicFunction"}, {"text": "Pre - eclampsia", "type": "BiologicFunction"}, {"text": "PE", "type": "BiologicFunction"}, {"text": "proteinuria", "type": "Finding"}, {"text": "≥20 weeks of gestation", "type": "Finding"}]}

Example input:
Sentence: Elevated Serum Uric Acid Level Predicts Rapid Decline in Kidney Function While elevated serum uric acid level ( SUA ) is a recognized risk factor for chronic kidney disease , it remains unclear whether change in SUA is independently associated with change in estimated glomerular filtration rate ( eGFR ) over time .

Example answer:
{"entities": [{"text": "Elevated Serum Uric Acid Level", "type": "Finding"}, {"text": "Kidney Function", "type": "BiologicFunction"}, {"text": "elevated serum uric acid level", "type": "Finding"}, {"text": "SUA", "type": "Chemical"}, {"text": "risk factor", "type": "Finding"}, {"text": "chronic kidney disease", "type": "BiologicFunction"}, {"text": "estimated glomerular filtration rate", "type": "HealthCareActivity"}, {"text": "eGFR", "type": "HealthCareActivity"}]}

Example input:
Sentence: Pregnancy and Kidney Outcomes in Patients With IgA Nephropathy : A Cohort Study The outcomes of pregnancy in immunoglobulin A nephropathy ( IgAN ) are controversial .

Example answer:
{"entities": [{"text": "Pregnancy", "type": "Finding"}, {"text": "Kidney", "type": "AnatomicalStructure"}, {"text": "IgA Nephropathy", "type": "BiologicFunction"}, {"text": "outcomes of pregnancy", "type": "Finding"}, {"text": "immunoglobulin A nephropathy", "type": "BiologicFunction"}, {"text": "IgAN", "type": "BiologicFunction"}]}

Example input:
Sentence: The estimated glomerular filtration rate ( eGFR ) was calculated using the creatinine based chronic kidney disease epidemiology collaboration ( CKD - EPI ) formula .

Example answer:
{"entities": [{"text": "estimated glomerular filtration rate", "type": "HealthCareActivity"}, {"text": "eGFR", "type": "HealthCareActivity"}, {"text": "calculated", "type": "HealthCareActivity"}, {"text": "creatinine", "type": "Chemical"}, {"text": "chronic kidney disease", "type": "BiologicFunction"}, {"text": "epidemiology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "CKD", "type": "BiologicFunction"}, {"text": "EPI", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "formula", "type": "IntellectualProduct"}]}

Example input:
Sentence: CKD was defined as an estimated glomerular filtration rate ( eGFR ) < 60 mL / min / 1 .

Example answer:
{"entities": [{"text": "CKD", "type": "BiologicFunction"}, {"text": "estimated glomerular filtration rate", "type": "HealthCareActivity"}, {"text": "eGFR", "type": "HealthCareActivity"}]}

Example input:
Sentence: This cohort study assessed the effects of pregnancy on kidney disease progression and risk factors for adverse pregnancy outcomes in patients with IgAN .

Example answer:
{"entities": [{"text": "pregnancy", "type": "BiologicFunction"}, {"text": "kidney", "type": "AnatomicalStructure"}, {"text": "disease progression", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "adverse", "type": "Finding"}, {"text": "pregnancy outcomes", "type": "Finding"}, {"text": "IgAN", "type": "BiologicFunction"}]}

Example input:
Sentence: Pregnancy , treated as a time - dependent variable ; baseline ( at time of biopsy ) estimated glomerular filtration rate ( eGFR ) , proteinuria , blood pressure , and kidney pathology ( Oxford MEST classification ) .

Example answer:
{"entities": [{"text": "Pregnancy", "type": "BiologicFunction"}, {"text": "biopsy", "type": "HealthCareActivity"}, {"text": "glomerular filtration rate", "type": "HealthCareActivity"}, {"text": "eGFR", "type": "HealthCareActivity"}, {"text": "proteinuria", "type": "Finding"}, {"text": "blood pressure", "type": "BiologicFunction"}, {"text": "kidney", "type": "AnatomicalStructure"}, {"text": "pathology", "type": "BiologicFunction"}, {"text": "Oxford MEST classification", "type": "IntellectualProduct"}]}

Example input:
Sentence: Pregnancy accelerated kidney disease progression in women with IgAN and CKD stage 3 , but not in those at stage 1 or 2 .

Example answer:
{"entities": [{"text": "Pregnancy", "type": "BiologicFunction"}, {"text": "kidney", "type": "AnatomicalStructure"}, {"text": "disease progression", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "IgAN", "type": "BiologicFunction"}, {"text": "CKD stage 3", "type": "BiologicFunction"}, {"text": "stage 1", "type": "BiologicFunction"}, {"text": "2", "type": "BiologicFunction"}]}

Input:
Sentence: Kidney disease progression event , defined as 30 % decline in eGFR or end - stage kidney disease ; rate of eGFR decline ; and adverse pregnancy outcomes , including severe preeclampsia and fetal loss .

## Item MedMentions:test:4244
Example input:
Sentence: Active packaging of chicken meats with modified atmosphere including oxygen scavengers The effects of modified atmosphere packaging ( MAP -70 % CO2 /30 % N2 ) and iron -based oxygen scavengers ( OS ) with various absorption capacities ( Ageless ( ® ) ss100 , ss300 , and ss500 ) as an active packaging system on microbiological and oxidative changes in chicken thigh meats were evaluated during refrigerated storage ( 4°C ) for 19 d at 3 - day intervals .

Example answer:
{"entities": [{"text": "chicken meats", "type": "Food"}, {"text": "oxygen", "type": "Chemical"}, {"text": "CO2", "type": "Chemical"}, {"text": "N2", "type": "Chemical"}, {"text": "iron", "type": "Chemical"}, {"text": "microbiological", "type": "IntellectualProduct"}, {"text": "chicken thigh meats", "type": "Food"}]}

Example input:
Sentence: Its content was significantly higher after the baking at 250 ° C than at 180 ° C .

Example answer:
{"entities": []}

Example input:
Sentence: Frozen storage did not stop oxysterols formation .

Example answer:
{"entities": [{"text": "oxysterols", "type": "Chemical"}]}

Example input:
Sentence: The content of 7 - ketocholesterol increased from the centre ( 87 µg kg ( - 1 ) ) to the surface ( 122 µg kg ( - 1 ) ) of baked meatloaf prepared under the standard conditions .

Example answer:
{"entities": [{"text": "7 - ketocholesterol", "type": "Chemical"}, {"text": "meatloaf", "type": "Food"}]}

Example input:
Sentence: The level of α - tocopherol and its distribution was also affected by the baking regime .

Example answer:
{"entities": [{"text": "α - tocopherol", "type": "Chemical"}]}

Example input:
Sentence: The effect of frozen storage and marjoram addition on the level of oxysterols was studied as well .

Example answer:
{"entities": [{"text": "marjoram", "type": "Food"}, {"text": "oxysterols", "type": "Chemical"}, {"text": "studied", "type": "ResearchActivity"}]}

Example input:
Sentence: Higher level of 7 - ketocholesterol was found in the baked meatloaves after their frozen storage .

Example answer:
{"entities": [{"text": "7 - ketocholesterol", "type": "Chemical"}, {"text": "meatloaves", "type": "Food"}]}

Example input:
Sentence: Formation of oxysterols during thermal processing and frozen storage of cooked minced meat Cholesterol is susceptible to oxidation and formation of oxysterols , which could have a negative health effect .

Example answer:
{"entities": [{"text": "oxysterols", "type": "Chemical"}, {"text": "minced", "type": "Food"}, {"text": "meat", "type": "Food"}, {"text": "Cholesterol", "type": "Chemical"}, {"text": "oxidation", "type": "BiologicFunction"}, {"text": "negative", "type": "Finding"}]}

Example input:
Sentence: The temperature was the most important factor affecting 7 - ketocholesterol formation in baked meatloaf .

Example answer:
{"entities": [{"text": "7 - ketocholesterol", "type": "Chemical"}, {"text": "meatloaf", "type": "Food"}]}

Example input:
Sentence: The effect of baking regime on the content and distribution of oxysterols was found .

Example answer:
{"entities": [{"text": "oxysterols", "type": "Chemical"}]}

Input:
Sentence: The formation and distribution of oxysterols was studied in meatloaves prepared under different baking regimes with increased temperature or prolonged time .

## Item MedMentions:test:4215
Example input:
Sentence: Dental implants in the anterior region proved to be an inadequate treatment modality in patients with severe hypodontia because of pronounced mucosal discoloration .

Example answer:
{"entities": [{"text": "Dental implants", "type": "MedicalDevice"}, {"text": "anterior region", "type": "SpatialConcept"}, {"text": "inadequate treatment modality", "type": "Finding"}, {"text": "hypodontia", "type": "AnatomicalStructure"}, {"text": "mucosal discoloration", "type": "Finding"}]}

Example input:
Sentence: Conclusion : Regarding elimination of intraradicular microbiota , additional PDT may increase the effectiveness of conventional chemomechanical preparation in previously root filled teeth accompanied by AP .

Example answer:
{"entities": [{"text": "PDT", "type": "HealthCareActivity"}, {"text": "chemomechanical preparation", "type": "HealthCareActivity"}, {"text": "root filled", "type": "HealthCareActivity"}, {"text": "teeth", "type": "AnatomicalStructure"}, {"text": "AP", "type": "BiologicFunction"}]}

Example input:
Sentence: Intraosseous pseudocarcinomatous hyperplasia of the mandible is a rare differential diagnosis in maxillofacial surgery .

Example answer:
{"entities": [{"text": "Intraosseous", "type": "HealthCareActivity"}, {"text": "pseudocarcinomatous hyperplasia", "type": "BiologicFunction"}, {"text": "mandible", "type": "AnatomicalStructure"}, {"text": "differential diagnosis", "type": "HealthCareActivity"}, {"text": "maxillofacial surgery", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Here , the miR - CATCH technique was applied to the mesothelin ( MSLN ) gene and coupled with next generation sequencing ( NGS ) , to identify miRNAs that regulate MSLN mRNA and that may be responsible for its increased protein levels found in malignant pleural mesothelioma ( MPM ) .

Example answer:
{"entities": [{"text": "mesothelin ( MSLN ) gene", "type": "AnatomicalStructure"}, {"text": "next generation sequencing", "type": "ResearchActivity"}, {"text": "NGS", "type": "ResearchActivity"}, {"text": "miRNAs", "type": "Chemical"}, {"text": "regulate", "type": "BiologicFunction"}, {"text": "MSLN mRNA", "type": "AnatomicalStructure"}, {"text": "protein levels", "type": "Finding"}, {"text": "malignant pleural mesothelioma", "type": "BiologicFunction"}, {"text": "MPM", "type": "BiologicFunction"}]}

Example input:
Sentence: Fabrication of gelatin methacrylate / nanohydroxyapatite microgel arrays for periodontal tissue regeneration Periodontitis is a chronic infectious disease and is the major cause of tooth loss and other oral health issues around the world .

Example answer:
{"entities": [{"text": "gelatin methacrylate", "type": "Chemical"}, {"text": "nanohydroxyapatite", "type": "Chemical"}, {"text": "microgel", "type": "Chemical"}, {"text": "arrays", "type": "SpatialConcept"}, {"text": "periodontal tissue regeneration", "type": "HealthCareActivity"}, {"text": "Periodontitis", "type": "BiologicFunction"}, {"text": "chronic infectious disease", "type": "BiologicFunction"}, {"text": "major cause", "type": "Finding"}, {"text": "tooth loss", "type": "AnatomicalStructure"}, {"text": "oral health", "type": "HealthCareActivity"}, {"text": "issues", "type": "Finding"}, {"text": "world", "type": "PopulationGroup"}]}

Example input:
Sentence: BAP1 mutations are frequent in malignant pleural mesothelioma ( MPM ) .

Example answer:
{"entities": [{"text": "BAP1", "type": "Chemical"}, {"text": "mutations", "type": "BiologicFunction"}, {"text": "malignant pleural mesothelioma", "type": "BiologicFunction"}, {"text": "MPM", "type": "BiologicFunction"}]}

Example input:
Sentence: Bone marrow mesenchymal stem cells combine with Treated dentin matrix to build biological root Treated dentin matrix ( TDM ) as a kind of scaffolding material has been proved odontogenic induction ability on dental - derived stem cells .

Example answer:
{"entities": [{"text": "Bone marrow", "type": "AnatomicalStructure"}, {"text": "mesenchymal stem cells", "type": "AnatomicalStructure"}, {"text": "Treated dentin matrix", "type": "Chemical"}, {"text": "biological root", "type": "AnatomicalStructure"}, {"text": "TDM", "type": "Chemical"}, {"text": "scaffolding material", "type": "Chemical"}, {"text": "odontogenic induction ability", "type": "BiologicFunction"}, {"text": "stem cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Pleural malignant mesothelioma in dental laboratory technicians : A case series Asbestos was used in dentistry as a binder in periodontal dressings and as lining material for casting rings and crucible .

Example answer:
{"entities": [{"text": "Pleural malignant mesothelioma", "type": "BiologicFunction"}, {"text": "dental laboratory technicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "case series", "type": "ResearchActivity"}, {"text": "Asbestos", "type": "Chemical"}, {"text": "dentistry", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "binder", "type": "Chemical"}, {"text": "periodontal dressings", "type": "MedicalDevice"}, {"text": "lining material", "type": "Chemical"}]}

Example input:
Sentence: Dental technicians suffering from mesothelioma should be questioned about past occupational asbestos exposure .

Example answer:
{"entities": [{"text": "Dental technicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "suffering", "type": "Finding"}, {"text": "mesothelioma", "type": "BiologicFunction"}, {"text": "asbestos exposure", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: However , until now , only one case of malignant mesothelioma with occupational exposure to asbestos in dental practice has been reported .

Example answer:
{"entities": [{"text": "malignant mesothelioma", "type": "BiologicFunction"}, {"text": "exposure to asbestos", "type": "InjuryOrPoisoning"}, {"text": "dental practice", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "reported", "type": "HealthCareActivity"}]}

Input:
Sentence: We confirm the association of malignant mesothelioma with dental technician work .

## Item MedMentions:test:4346
Example input:
Sentence: 95 % confidence interval : 1 . 710 - 6 . 248 ; HR : 2 . 295 , 95 % confidence interval : 1 . 217 - 4 . 331 , respectively ) than those with an AAPR ≥ 0 . 447 .

Example answer:
{"entities": []}

Example input:
Sentence: 85 ( CI 95 % : 0 . 84 to 0 . 92 ) , respectively ( P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 1 - 88 . 7 , p < 0 . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 852 - 0 . 995 ; p values < 0 . 0001 in all cases ) .

Example answer:
{"entities": []}

Example input:
Sentence: In the exploratory analysis , patients with DOR ≥12 months ( n = 287 ) or ≥24 months ( n = 133 ) were more likely to experience grade 3 / 4 AEs than the overall population .

Example answer:
{"entities": [{"text": "exploratory analysis", "type": "ResearchActivity"}, {"text": "AEs", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: I . 95 % : 7 . 2 - 38 . 6 vs 60 . 0 % , C . I . 95 % : 21 . 6 - 84 . 3 , p = 0 . 01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Among cannabis users , dependent patients had 43 % significantly lower prevalence of NAFLD compared to non - dependent patients ( AOR : 0 . 57 [ 0 . 42 - 0 . 77 ] ; p < 0 . 0001 ) .

Example answer:
{"entities": [{"text": "cannabis", "type": "Chemical"}, {"text": "users", "type": "PopulationGroup"}, {"text": "NAFLD", "type": "BiologicFunction"}]}

Example input:
Sentence: I . 95 % : 5 . 8 - 69 . 1 , p = 0 . 02 ) and lower relapse incidence ( 20 . 5 % , C .

Example answer:
{"entities": []}

Example input:
Sentence: 95 % confidence interval : 0 . 70 , 0 . 84 , P = 0 . 00 ) and had fewer withdrawals due to adverse events .

Example answer:
{"entities": [{"text": "adverse events", "type": "BiologicFunction"}]}

Example input:
Sentence: 07 ; model 2 : aOR : 1 . 9 , 95 % CI : 1 . 1 to 3 .

Example answer:
{"entities": []}

Input:
Sentence: 85 [ 0 . 79 - 0 . 92 ] ; p < 0 . 0001 ) and 52 % lower in dependent users ( AOR : 0 . 49 [ 0 . 36 - 0 . 65 ] ; p < 0 . 0001 ) .

## Item MedMentions:test:4083
Example input:
Sentence: Myoglobin , arterial blood lactate , aspartate aminotransferase , alanine aminotransferase and pancreatic amylase levels were elevated in 100 % , 67 % , 89 % , 89 % , 89 % and 56 % of patients with mesenteric embolization , respectively .

Example answer:
{"entities": [{"text": "Myoglobin", "type": "Chemical"}, {"text": "aspartate aminotransferase", "type": "Chemical"}, {"text": "alanine aminotransferase", "type": "Chemical"}, {"text": "pancreatic amylase", "type": "Chemical"}, {"text": "mesenteric embolization", "type": "BiologicFunction"}]}

Example input:
Sentence: The antithrombotic activity of Batroxase was tested in vivo in a model based on two factors of the Virchow 's Triad : blood flow alterations ( partial stenosis of the inferior vena cava ) , and vessel wall injury ( 10 % ferric chloride for 5min ) , in comparison with sodium heparin ( positive control ) and saline ( negative control ) .

Example answer:
{"entities": [{"text": "antithrombotic activity", "type": "Finding"}, {"text": "Batroxase", "type": "Chemical"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "model", "type": "Eukaryote"}, {"text": "Virchow 's Triad", "type": "IntellectualProduct"}, {"text": "blood flow", "type": "BiologicFunction"}, {"text": "partial stenosis", "type": "AnatomicalStructure"}, {"text": "inferior vena cava", "type": "AnatomicalStructure"}, {"text": "vessel wall", "type": "AnatomicalStructure"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "ferric chloride", "type": "Chemical"}, {"text": "sodium heparin", "type": "Chemical"}]}

Example input:
Sentence: We hypothesized that streamlined cardiopulmonary bypass circuit and rotational thromboelastometry ( ROTEM ) would reduce blood product usage and improve outcomes .

Example answer:
{"entities": [{"text": "rotational thromboelastometry", "type": "HealthCareActivity"}, {"text": "ROTEM", "type": "HealthCareActivity"}, {"text": "blood product usage", "type": "HealthCareActivity"}]}

Example input:
Sentence: The evidence suggests that PduOC : heme plays an important role in the set of cobalamin transformations required for effective catabolism of 1 , 2 - propanediol .

Example answer:
{"entities": [{"text": "PduOC", "type": "Chemical"}, {"text": "heme", "type": "Chemical"}, {"text": "cobalamin", "type": "Chemical"}, {"text": "transformations", "type": "BiologicFunction"}, {"text": "catabolism", "type": "BiologicFunction"}, {"text": "1 , 2 - propanediol", "type": "Chemical"}]}

Example input:
Sentence: Albumin and hemoglobin were incubated with busulfan or control compounds , digested with trypsin and analyzed by LC - MS / MS on a Thermo Fisher LTQ Orbitrap Velos Pro .

Example answer:
{"entities": [{"text": "Albumin", "type": "Chemical"}, {"text": "hemoglobin", "type": "Chemical"}, {"text": "incubated", "type": "HealthCareActivity"}, {"text": "busulfan", "type": "Chemical"}, {"text": "control compounds", "type": "Chemical"}, {"text": "trypsin", "type": "Chemical"}, {"text": "LC - MS", "type": "HealthCareActivity"}, {"text": "MS", "type": "HealthCareActivity"}]}

Example input:
Sentence: A Recombinant Human Anti - Platelet scFv Antibody Produced in Pichia pastoris for Atheroma Targeting Cells of the innate and adaptive immune system are key factors in the progression of atherosclerotic plaque , leading to plaque instability and rupture , potentially resulting in acute atherothrombotic events such as coronary artery disease , cerebrovascular disease and peripheral arterial disease .

Example answer:
{"entities": [{"text": "Recombinant", "type": "ResearchActivity"}, {"text": "Human", "type": "Eukaryote"}, {"text": "Anti - Platelet scFv Antibody", "type": "Chemical"}, {"text": "Pichia pastoris", "type": "Eukaryote"}, {"text": "Atheroma", "type": "BiologicFunction"}, {"text": "Cells", "type": "AnatomicalStructure"}, {"text": "immune system", "type": "BodySystem"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "atherosclerotic plaque", "type": "BodySubstance"}, {"text": "plaque", "type": "Finding"}, {"text": "instability", "type": "Finding"}, {"text": "rupture", "type": "InjuryOrPoisoning"}, {"text": "atherothrombotic", "type": "AnatomicalStructure"}, {"text": "coronary artery disease", "type": "BiologicFunction"}, {"text": "cerebrovascular disease", "type": "BiologicFunction"}, {"text": "peripheral arterial disease", "type": "BiologicFunction"}]}

Example input:
Sentence: The animals were then hemodiluted until their individual critical hemoglobin concentrations ( Hbcrit ) were reached by the exchange of whole blood for hydroxyethyl starch ( HES ; 130 : 0 . 4 ) .

Example answer:
{"entities": [{"text": "animals", "type": "Eukaryote"}, {"text": "hemodiluted", "type": "HealthCareActivity"}, {"text": "critical hemoglobin concentrations", "type": "Finding"}, {"text": "Hbcrit", "type": "Finding"}, {"text": "whole blood", "type": "BodySubstance"}, {"text": "hydroxyethyl starch", "type": "Chemical"}, {"text": "HES", "type": "Chemical"}]}

Example input:
Sentence: In addition , very recent data have demonstrated biological pathways modulated by bilirubin , which are responsible for observed strong clinical associations .

Example answer:
{"entities": [{"text": "biological pathways", "type": "BiologicFunction"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Consistent with these results , we proved in our own studies , that subjects with mild elevation of serum levels of unconjugated bilirubin ( benign hyperbilirubinemia , Gilbert syndrome ) have much lower prevalence / incidence of coronary heart as well as peripheral vascular disease .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "hyperbilirubinemia", "type": "BiologicFunction"}, {"text": "Gilbert syndrome", "type": "BiologicFunction"}, {"text": "coronary heart", "type": "BiologicFunction"}, {"text": "peripheral vascular disease", "type": "BiologicFunction"}]}

Example input:
Sentence: However , data from recent years convincingly suggest that mildly elevated bilirubin concentrations are associated with protection against various oxidative stress -mediated diseases , atherosclerotic conditions being the most clinically relevant .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "atherosclerotic", "type": "BiologicFunction"}]}

Input:
Sentence: Bilirubin and atherosclerotic diseases Bilirubin is the final product of heme catabolism in the systemic circulation .
