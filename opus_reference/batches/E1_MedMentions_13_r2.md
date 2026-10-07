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

## Item MedMentions:test:2855
Example input:
Sentence: With a 5 - year survival rate of just 8 % , pancreatic cancer ( PC ) is projected to be the second leading cause of cancer deaths by 2030 .

Example answer:
{"entities": [{"text": "pancreatic cancer", "type": "BiologicFunction"}, {"text": "PC", "type": "BiologicFunction"}]}

Example input:
Sentence: Preterm infants at 36 weeks PMA have comparable measurements of twist to term infants .

Example answer:
{"entities": [{"text": "twist", "type": "SpatialConcept"}]}

Example input:
Sentence: We conducted a prospective analysis of risk factors and length of survival among pancreatic cancer patients living in Oklahoma between 1997 and 2012 ( n = 6 , 291 ) .

Example answer:
{"entities": [{"text": "prospective analysis", "type": "ResearchActivity"}, {"text": "risk factors", "type": "Finding"}, {"text": "Oklahoma", "type": "SpatialConcept"}]}

Example input:
Sentence: The ventral pancreas encompassed almost the entire circumference of the pyloric ring , suggesting a subtype of annular pancreas .

Example answer:
{"entities": [{"text": "ventral pancreas", "type": "AnatomicalStructure"}, {"text": "encompassed", "type": "SpatialConcept"}, {"text": "pyloric ring", "type": "AnatomicalStructure"}, {"text": "subtype", "type": "IntellectualProduct"}, {"text": "annular pancreas", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 6 % ID / g at 15min ) , with corresponding high tumor -to - blood ( T / B ) , tumor -to - muscle ( T / M ) , and tumor -to - pancreas ( T / P ) ratios ( T / B = 2 . 55 , T / M = 22 .

Example answer:
{"entities": [{"text": "tumor -to - blood", "type": "Finding"}, {"text": "T / B", "type": "Finding"}, {"text": "tumor -to - muscle", "type": "Finding"}, {"text": "T / M", "type": "Finding"}, {"text": "tumor -to - pancreas ( T / P ) ratios", "type": "Finding"}]}

Example input:
Sentence: 4 weeks and their infants had a mean birthweight of 3138 ± 677 g .

Example answer:
{"entities": []}

Example input:
Sentence: Incomplete Annular Pancreas with Ectopic Opening of the Pancreatic and Bile Ducts into the Pyloric Ring : First Report of a Rare Anomaly The patient was a 56 - year - old woman who had experienced epigastralgia and dorsal pain several times over the last 20 years .

Example answer:
{"entities": [{"text": "Annular Pancreas", "type": "AnatomicalStructure"}, {"text": "Ectopic", "type": "SpatialConcept"}, {"text": "Opening", "type": "SpatialConcept"}, {"text": "Pancreatic", "type": "AnatomicalStructure"}, {"text": "Bile Ducts", "type": "AnatomicalStructure"}, {"text": "Pyloric Ring", "type": "AnatomicalStructure"}, {"text": "Report", "type": "IntellectualProduct"}, {"text": "Anomaly", "type": "Finding"}, {"text": "epigastralgia", "type": "Finding"}, {"text": "dorsal pain", "type": "Finding"}]}

Example input:
Sentence: This study was undertaken to study the morphometry of human pancreas at different gestational age groups of normal , still born fetuses .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "morphometry", "type": "HealthCareActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "pancreas", "type": "AnatomicalStructure"}, {"text": "fetuses", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The length and weight of the pancreas as well as height of its head were noted .

Example answer:
{"entities": [{"text": "pancreas", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The average length of pancreas was 1 . 80 cm in 12 ( th ) week and 4 . 70 cm in 40 ( th ) week of gestation .

Example answer:
{"entities": [{"text": "pancreas", "type": "AnatomicalStructure"}, {"text": "week", "type": "Finding"}, {"text": "week of gestation", "type": "Finding"}]}

Input:
Sentence: The average height of pancreas head was 0 . 80 cm in the 12 ( th ) and 2 . 70 cm in 40 ( th ) week of gestation .

## Item MedMentions:test:2635
Example input:
Sentence: In this study , we determined the cumulative acute exposure to OPs and CPs of Shanghai residents from vegetables and fruits ( VFs ) .

Example answer:
{"entities": [{"text": "OPs", "type": "Chemical"}, {"text": "CPs", "type": "Chemical"}, {"text": "residents", "type": "PopulationGroup"}, {"text": "vegetables", "type": "Food"}, {"text": "fruits", "type": "Food"}, {"text": "VFs", "type": "Food"}]}

Example input:
Sentence: Referenced to Dietary Reference Intakes , survivors consumed inadequate amounts of vitamin D , vitamin E , potassium , fiber , magnesium , and calcium ( 27 % , 54 % , 58 % , 59 % , 84 % , and 90 % of the recommended intakes ) but excessive amounts of sodium and saturated fat ( 155 % and 115 % of the recommended intakes ) from foods .

Example answer:
{"entities": [{"text": "Dietary Reference Intakes", "type": "IntellectualProduct"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "potassium", "type": "Food"}, {"text": "fiber", "type": "Food"}, {"text": "magnesium", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "recommended intakes", "type": "IntellectualProduct"}, {"text": "sodium", "type": "Food"}, {"text": "saturated fat", "type": "Food"}]}

Example input:
Sentence: In conclusion , substitution of saturated fat with omega - 3 fat in a high - caloric diet induced hyperlipidaemia with an FA profile yielding similar rates and quality of blastocysts compared with normolipidaemic controls .

Example answer:
{"entities": [{"text": "saturated fat", "type": "Food"}, {"text": "omega - 3 fat", "type": "Chemical"}, {"text": "high - caloric diet", "type": "HealthCareActivity"}, {"text": "hyperlipidaemia", "type": "BiologicFunction"}, {"text": "FA profile", "type": "HealthCareActivity"}, {"text": "blastocysts", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Corn oil intake favorably impacts lipoprotein cholesterol , apolipoprotein and lipoprotein particle levels compared with extra - virgin olive oil Corn oil ( CO ) and extra - virgin olive oil ( EVOO ) are rich sources of unsaturated fatty acids ( UFA ) , but UFA profiles differ among oils , which may affect lipoprotein levels .

Example answer:
{"entities": [{"text": "Corn oil intake", "type": "Chemical"}, {"text": "lipoprotein cholesterol", "type": "Chemical"}, {"text": "apolipoprotein", "type": "HealthCareActivity"}, {"text": "lipoprotein", "type": "HealthCareActivity"}, {"text": "extra - virgin olive oil", "type": "Chemical"}, {"text": "Corn oil", "type": "Chemical"}, {"text": "CO", "type": "Chemical"}, {"text": "EVOO", "type": "Chemical"}, {"text": "sources of", "type": "Finding"}, {"text": "unsaturated fatty acids", "type": "Chemical"}, {"text": "UFA", "type": "Chemical"}, {"text": "oils", "type": "Chemical"}, {"text": "lipoprotein levels", "type": "HealthCareActivity"}]}

Example input:
Sentence: After 21 d of feeding , supplementation of oxidized fish oil increased the levels of malondialdehyde ( MDA ) , oxidized glutathione ( GSSG ) , interleukin - 1β ( IL - 1β ) , tumor necrosis factor - α ( TNF - α ) , interleukin - 2 ( IL - 2 ) , nuclear factor κ B ( NF - κB ) , inducible nitric oxide synthase ( iNOS ) , NO , and Caspase - 3 in jejunal mucosa , and decreased the villous height in duodenum and the levels of secretory immunoglobulin A ( sIgA ) and IL - 4 in the jejunal mucosa compared with supplementation with fresh oil .

Example answer:
{"entities": [{"text": "supplementation", "type": "HealthCareActivity"}, {"text": "oxidized", "type": "BiologicFunction"}, {"text": "fish oil", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "MDA", "type": "Chemical"}, {"text": "oxidized glutathione", "type": "Chemical"}, {"text": "GSSG", "type": "Chemical"}, {"text": "interleukin - 1β", "type": "Chemical"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "tumor necrosis factor - α", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "interleukin - 2", "type": "Chemical"}, {"text": "IL - 2", "type": "Chemical"}, {"text": "nuclear factor κ B", "type": "Chemical"}, {"text": "( NF - κB", "type": "Chemical"}, {"text": "inducible nitric oxide synthase", "type": "Chemical"}, {"text": "iNOS", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "Caspase - 3", "type": "Chemical"}, {"text": "jejunal mucosa", "type": "AnatomicalStructure"}, {"text": "villous", "type": "AnatomicalStructure"}, {"text": "duodenum", "type": "AnatomicalStructure"}, {"text": "secretory immunoglobulin A", "type": "Chemical"}, {"text": "( sIgA", "type": "Chemical"}, {"text": "IL - 4", "type": "Chemical"}, {"text": "oil", "type": "Chemical"}]}

Example input:
Sentence: Higher fish consumption ( at least 3 portions ) was associated with lower omega - 6 fatty acid levels ( p = 0 . 026 ) and higher omega - 3 fatty acid levels ( p = 0 . 037 ) , both results being statistically significant .

Example answer:
{"entities": [{"text": "fish consumption", "type": "BiologicFunction"}, {"text": "omega - 6 fatty acid", "type": "Chemical"}, {"text": "omega - 3 fatty acid", "type": "Chemical"}, {"text": "results", "type": "Finding"}]}

Example input:
Sentence: The ApoE polymorphism showed different influences on serum lipid parameters with increasing age and body mass index ( BMI ) in our Shandong Han population .

Example answer:
{"entities": [{"text": "ApoE", "type": "AnatomicalStructure"}, {"text": "serum lipid parameters", "type": "HealthCareActivity"}, {"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Serum apolipoprotein E concentration and polymorphism influence serum lipid levels in Chinese Shandong Han population Apolipoprotein E ( ApoE ) , which has been shown to influence serum lipid parameters , can bind to multiple types of lipids and plays an important role in the metabolism and homeostasis of lipids and lipoproteins .

Example answer:
{"entities": [{"text": "serum lipid levels", "type": "HealthCareActivity"}, {"text": "Apolipoprotein E", "type": "Chemical"}, {"text": "ApoE", "type": "Chemical"}, {"text": "serum lipid parameters", "type": "HealthCareActivity"}, {"text": "lipids", "type": "Chemical"}, {"text": "metabolism", "type": "BiologicFunction"}, {"text": "homeostasis", "type": "BiologicFunction"}, {"text": "lipoproteins", "type": "Chemical"}]}

Example input:
Sentence: Shandong province of China .

Example answer:
{"entities": [{"text": "Shandong province of China", "type": "SpatialConcept"}]}

Example input:
Sentence: Therefore , studying the effect of ApoE polymorphism on ApoE concentration and serum lipid levels in Shandong province is very important .A total of 815 subjects including 285 men and 530 women were randomly selected and studied from Jinan , Shandong province .

Example answer:
{"entities": [{"text": "ApoE", "type": "AnatomicalStructure"}, {"text": "ApoE", "type": "Chemical"}, {"text": "serum lipid levels", "type": "HealthCareActivity"}, {"text": "Shandong province", "type": "SpatialConcept"}, {"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Input:
Sentence: The serum lipid levels were also closely correlated with dietary habits , and Shandong cuisine is famous for its high salt and oil contents , which widely differ among the different areas in China .

## Item MedMentions:test:2798
Example input:
Sentence: All cases showed markers positivity to Neuron - specific enolase , Chromogranin , Synaptophysin and Estrogen and Progesterone receptors were found .

Example answer:
{"entities": [{"text": "Neuron - specific enolase", "type": "Chemical"}, {"text": "Chromogranin", "type": "Chemical"}, {"text": "Synaptophysin", "type": "Chemical"}]}

Example input:
Sentence: There were decreased numbers of GFAP immunopositive astrocytes per unit area , although those that remained had increased arbor length and complexity .

Example answer:
{"entities": [{"text": "decreased numbers", "type": "Finding"}, {"text": "immunopositive astrocytes", "type": "AnatomicalStructure"}, {"text": "complexity", "type": "Finding"}]}

Example input:
Sentence: C - Reactive Protein ( CRP ) is a good inflammatory marker .

Example answer:
{"entities": [{"text": "C - Reactive Protein", "type": "Chemical"}, {"text": "CRP", "type": "Chemical"}, {"text": "marker", "type": "ClinicalAttribute"}]}

Example input:
Sentence: CGRP expression , as determined by IHC , cannot be observed in other groups , indicating that the hippocampus may be the specific component of the brain that responds to " big stress " .

Example answer:
{"entities": [{"text": "CGRP", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "IHC", "type": "HealthCareActivity"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "big stress", "type": "BiologicFunction"}]}

Example input:
Sentence: ELISA analysis indicated a great density of CGRP in TBI - fracture group at different time points .

Example answer:
{"entities": [{"text": "ELISA analysis", "type": "HealthCareActivity"}, {"text": "CGRP", "type": "Chemical"}, {"text": "TBI", "type": "InjuryOrPoisoning"}, {"text": "fracture", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: 3 % of the patched Grpr - Cre neurons , where the majority of the cells displayed a tonic firing property .

Example answer:
{"entities": [{"text": "Grpr - Cre", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "tonic firing", "type": "BiologicFunction"}]}

Example input:
Sentence: Our results suggest that CGRP - expressing nerve growth factor -dependent neurons are primarily responsible for hip joint pain and may represent therapeutic targets .

Example answer:
{"entities": [{"text": "CGRP", "type": "Chemical"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "nerve growth factor", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "hip joint pain", "type": "Finding"}]}

Example input:
Sentence: FG -labeled neurons in the control group were distributed throughout the left DRG from T13 to L5 , primarily in L2 to L4 , and CGRP -positive neurons were significantly more frequent than IB4 - binding neurons .

Example answer:
{"entities": [{"text": "FG", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "left DRG", "type": "AnatomicalStructure"}, {"text": "T13", "type": "AnatomicalStructure"}, {"text": "L5", "type": "AnatomicalStructure"}, {"text": "L2", "type": "AnatomicalStructure"}, {"text": "L4", "type": "AnatomicalStructure"}, {"text": "CGRP", "type": "Chemical"}, {"text": "IB4", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , hip joint inflammation caused an increase in CGRP -positive neurons , but not in IB4 - binding neurons .

Example answer:
{"entities": [{"text": "hip joint", "type": "SpatialConcept"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "CGRP", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "IB4", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}]}

Example input:
Sentence: In the inflammatory group , FG -labeled neurons were similarly distributed , primarily at L3 and L4 , and CGRP -positive neurons were significantly more frequent than IB4 - binding neurons .

Example answer:
{"entities": [{"text": "FG", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "L3", "type": "AnatomicalStructure"}, {"text": "L4", "type": "AnatomicalStructure"}, {"text": "CGRP", "type": "Chemical"}, {"text": "IB4", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}]}

Input:
Sentence: The percentage of CGRP -positive neurons was significantly greater in the inflammatory group ( P < 0 . 05 ) .

## Item MedMentions:test:2586
Example input:
Sentence: MSCs derived from bone marrow , adipose and umbilical cord that were infected with NDV delivered the virus to co - cultured glioma cells and GSCs .

Example answer:
{"entities": [{"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "bone marrow", "type": "AnatomicalStructure"}, {"text": "adipose", "type": "AnatomicalStructure"}, {"text": "umbilical cord", "type": "AnatomicalStructure"}, {"text": "infected", "type": "Finding"}, {"text": "NDV", "type": "Virus"}, {"text": "virus", "type": "Virus"}, {"text": "co - cultured", "type": "HealthCareActivity"}, {"text": "glioma", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "GSCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: MSC - EV increased hepatic mRNA expression of NACHT , LRR and PYD domains - containing protein 12 ( Nlrp12 ) , and the chemokine ( C - X - C motif ) ligand 1 ( CXCL1 ) , and reduced mRNA expression of several inflammatory cytokines such as IL - 6 during IRI .

Example answer:
{"entities": [{"text": "MSC", "type": "AnatomicalStructure"}, {"text": "EV", "type": "AnatomicalStructure"}, {"text": "hepatic", "type": "SpatialConcept"}, {"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "NACHT , LRR and PYD domains - containing protein 12", "type": "AnatomicalStructure"}, {"text": "Nlrp12", "type": "AnatomicalStructure"}, {"text": "chemokine ( C - X - C motif ) ligand 1", "type": "AnatomicalStructure"}, {"text": "CXCL1", "type": "AnatomicalStructure"}, {"text": "cytokines", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "IRI", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: CCR2 Positive Exosome Released by Mesenchymal Stem Cells Suppresses Macrophage Functions and Alleviates Ischemia / Reperfusion - Induced Renal Injury Mesenchymal stem cells ( MSCs ) derived exosomes have been shown to have protective effects on the kidney in ischemia / reperfusion - induced renal injury .

Example answer:
{"entities": [{"text": "CCR2", "type": "Chemical"}, {"text": "Exosome", "type": "AnatomicalStructure"}, {"text": "Mesenchymal Stem Cells", "type": "AnatomicalStructure"}, {"text": "Macrophage", "type": "AnatomicalStructure"}, {"text": "Ischemia", "type": "BiologicFunction"}, {"text": "Reperfusion", "type": "BiologicFunction"}, {"text": "Induced Renal Injury", "type": "InjuryOrPoisoning"}, {"text": "Mesenchymal stem cells", "type": "AnatomicalStructure"}, {"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "exosomes", "type": "AnatomicalStructure"}, {"text": "kidney", "type": "AnatomicalStructure"}, {"text": "ischemia", "type": "BiologicFunction"}, {"text": "reperfusion", "type": "BiologicFunction"}, {"text": "induced renal injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: In particular , platelet lysate ( PL ) - MSCs produce higher levels of chemerin compared with fetal bovine serum ( FBS ) - MSCs .

Example answer:
{"entities": [{"text": "platelet lysate", "type": "AnatomicalStructure"}, {"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "chemerin", "type": "Chemical"}, {"text": "fetal bovine serum", "type": "Chemical"}, {"text": "FBS", "type": "Chemical"}]}

Example input:
Sentence: The results indicate that CCR2 expressed on MSC - exo may play a key role in inflammation regulation and renal injury repair by acting as a decoy to suppress CCL2 activity .

Example answer:
{"entities": [{"text": "indicate", "type": "Finding"}, {"text": "CCR2", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "MSC", "type": "AnatomicalStructure"}, {"text": "exo", "type": "AnatomicalStructure"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "renal injury repair", "type": "BiologicFunction"}]}

Example input:
Sentence: After purification , MSC - secreted chemerin was identified using mass spectrometry analysis and the biological activity of secreted isoforms was evaluated using migration assay .

Example answer:
{"entities": [{"text": "MSC", "type": "AnatomicalStructure"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "chemerin", "type": "Chemical"}, {"text": "mass spectrometry", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "isoforms", "type": "Chemical"}, {"text": "migration assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: We also proved that CCR2 high - expressed MSC - exo could reduce the concentration of free CCL2 and suppress its functions to recruit or activate macrophage .

Example answer:
{"entities": [{"text": "CCR2", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "MSC", "type": "AnatomicalStructure"}, {"text": "exo", "type": "AnatomicalStructure"}, {"text": "CCL2", "type": "Chemical"}, {"text": "activate macrophage", "type": "BiologicFunction"}]}

Example input:
Sentence: In our current study , we focused on the abundant proteins in exosomes derived from MSCs ( MSC - exo ) and found that the C - C motif chemokine receptor - 2 ( CCR2 ) was expressed on MSC - exo with a high ability to bind to its ligand CCL2 .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "exosomes", "type": "AnatomicalStructure"}, {"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "MSC", "type": "AnatomicalStructure"}, {"text": "exo", "type": "AnatomicalStructure"}, {"text": "C - C motif chemokine receptor - 2", "type": "Chemical"}, {"text": "CCR2", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "bind to its ligand CCL2", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , chemerin is secreted by MSCs as an inactive precursor , which can be converted into its active form by exogenous chemerin - activating serine and cysteine proteases .

Example answer:
{"entities": [{"text": "chemerin", "type": "Chemical"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "serine", "type": "Chemical"}, {"text": "cysteine proteases", "type": "Chemical"}]}

Example input:
Sentence: Our data indicate that , in response to various inflammatory stimuli , MSCs secrete high amounts of inactive chemerin , which can then be activated by inflammation - induced tissue proteases .

Example answer:
{"entities": [{"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "secrete", "type": "BiologicFunction"}, {"text": "chemerin", "type": "Chemical"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "proteases", "type": "Chemical"}]}

Input:
Sentence: Bone marrow - derived MSCs secrete chemerin and express its receptors ChemR23 and CCRL2 .

## Item MedMentions:test:2734
Example input:
Sentence: A patient with an abnormally high level of the tumor markers , carbohydrate antigen - 724 ( CA724 ) , CA19 - 9 and carcinoembryonic antigen ( CEA ) , although without any detectable tumor , was treated with an immunomodulatory therapy featuring an infusion of cytokine - induced autologous killer cells ( CIKs ) at the request of the patient .

Example answer:
{"entities": [{"text": "tumor markers", "type": "Chemical"}, {"text": "carbohydrate antigen - 724", "type": "Chemical"}, {"text": "CA724", "type": "Chemical"}, {"text": "CA19 - 9", "type": "Chemical"}, {"text": "carcinoembryonic antigen", "type": "Chemical"}, {"text": "CEA", "type": "Chemical"}, {"text": "detectable", "type": "ClinicalAttribute"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "immunomodulatory therapy", "type": "HealthCareActivity"}, {"text": "infusion", "type": "HealthCareActivity"}, {"text": "cytokine - induced autologous killer cells", "type": "AnatomicalStructure"}, {"text": "CIKs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Finally , we discuss the potential role of PSCs in pituitary tumorigenesis in the context of current models of carcinogenesis and present evidence showing that in contrast to pituitary adenoma , which follows a classical cancer stem cell paradigm , a novel mechanism has been revealed for paracrine , non - cell autonomous tumor initiation in adamantinomatous craniopharyngioma , a benign but clinically aggressive pediatric tumor .

Example answer:
{"entities": [{"text": "PSCs", "type": "AnatomicalStructure"}, {"text": "pituitary", "type": "AnatomicalStructure"}, {"text": "tumorigenesis", "type": "BiologicFunction"}, {"text": "carcinogenesis", "type": "BiologicFunction"}, {"text": "present", "type": "Finding"}, {"text": "pituitary adenoma", "type": "BiologicFunction"}, {"text": "cancer stem cell", "type": "AnatomicalStructure"}, {"text": "non - cell", "type": "AnatomicalStructure"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "adamantinomatous craniopharyngioma", "type": "BiologicFunction"}, {"text": "pediatric tumor", "type": "BiologicFunction"}]}

Example input:
Sentence: Carcinoid tumor , as the glomus tumor , can show an organoid pattern , increased vascularity , and uniform , round cells with eosinophilic cytoplasm , but usually are positive for cytokeratin and always stained with chromogranin and synaptophysin showing negative for smooth muscle markers which is presented in our case .

Example answer:
{"entities": [{"text": "Carcinoid tumor", "type": "BiologicFunction"}, {"text": "glomus tumor", "type": "BiologicFunction"}, {"text": "organoid pattern", "type": "Finding"}, {"text": "eosinophilic cytoplasm", "type": "AnatomicalStructure"}, {"text": "positive for cytokeratin", "type": "Finding"}, {"text": "chromogranin", "type": "Chemical"}, {"text": "synaptophysin", "type": "Chemical"}, {"text": "negative", "type": "Finding"}, {"text": "smooth muscle", "type": "AnatomicalStructure"}, {"text": "markers", "type": "Chemical"}]}

Example input:
Sentence: Coronal histological examination of the lateral wall of the CS showed invagination of the dura propria and periosteal dura into the SOF .

Example answer:
{"entities": [{"text": "Coronal histological examination", "type": "HealthCareActivity"}, {"text": "lateral wall", "type": "SpatialConcept"}, {"text": "CS", "type": "SpatialConcept"}, {"text": "invagination", "type": "AnatomicalStructure"}, {"text": "dura propria", "type": "AnatomicalStructure"}, {"text": "periosteal dura", "type": "AnatomicalStructure"}, {"text": "SOF", "type": "SpatialConcept"}]}

Example input:
Sentence: We describe the first reported case of a pituitary macroadenoma associated with RSTS .

Example answer:
{"entities": [{"text": "pituitary macroadenoma", "type": "BiologicFunction"}, {"text": "RSTS", "type": "BiologicFunction"}]}

Example input:
Sentence: Incomplete Annular Pancreas with Ectopic Opening of the Pancreatic and Bile Ducts into the Pyloric Ring : First Report of a Rare Anomaly The patient was a 56 - year - old woman who had experienced epigastralgia and dorsal pain several times over the last 20 years .

Example answer:
{"entities": [{"text": "Annular Pancreas", "type": "AnatomicalStructure"}, {"text": "Ectopic", "type": "SpatialConcept"}, {"text": "Opening", "type": "SpatialConcept"}, {"text": "Pancreatic", "type": "AnatomicalStructure"}, {"text": "Bile Ducts", "type": "AnatomicalStructure"}, {"text": "Pyloric Ring", "type": "AnatomicalStructure"}, {"text": "Report", "type": "IntellectualProduct"}, {"text": "Anomaly", "type": "Finding"}, {"text": "epigastralgia", "type": "Finding"}, {"text": "dorsal pain", "type": "Finding"}]}

Example input:
Sentence: EES is the ideal approach for complete resection of ectopic intracavernous adenomas allowing for a wide exploration of the CS with no surgical complications .

Example answer:
{"entities": [{"text": "EES", "type": "HealthCareActivity"}, {"text": "resection", "type": "HealthCareActivity"}, {"text": "ectopic", "type": "SpatialConcept"}, {"text": "adenomas", "type": "BiologicFunction"}, {"text": "exploration", "type": "HealthCareActivity"}, {"text": "CS", "type": "SpatialConcept"}, {"text": "no", "type": "Finding"}, {"text": "surgical", "type": "HealthCareActivity"}, {"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: Pathology confirmed the diagnosis of an ACTH - secreting adenoma .

Example answer:
{"entities": [{"text": "Pathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "diagnosis", "type": "Finding"}, {"text": "ACTH - secreting adenoma", "type": "BiologicFunction"}]}

Example input:
Sentence: Increased ACTH , serum cortisol and free urine cortisol levels were identified , however the pituitary MRI failed to reveal a pituitary tumor ; instead , a parasellar lesion in the left cavernous sinus ( CS ) was noticed .

Example answer:
{"entities": [{"text": "ACTH", "type": "Chemical"}, {"text": "serum cortisol", "type": "Chemical"}, {"text": "pituitary MRI", "type": "HealthCareActivity"}, {"text": "pituitary tumor", "type": "BiologicFunction"}, {"text": "parasellar lesion", "type": "Finding"}, {"text": "cavernous sinus", "type": "SpatialConcept"}, {"text": "CS", "type": "SpatialConcept"}]}

Example input:
Sentence: Only 12 cases of ectopic intracavernous ACTH - secreting adenomas have been reported to date and all were microadenomas .

Example answer:
{"entities": [{"text": "ectopic", "type": "SpatialConcept"}, {"text": "ACTH - secreting adenomas", "type": "BiologicFunction"}, {"text": "microadenomas", "type": "BiologicFunction"}]}

Input:
Sentence: The presence of an ectopic ACTH - secreting macroadenoma in the CS represents a surgical challenge .

## Item MedMentions:test:2770
Example input:
Sentence: Intravascular ultrasound ( n = 34 ) or optical coherence tomography ( n = 31 ) was performed in all cases .

Example answer:
{"entities": [{"text": "Intravascular ultrasound", "type": "HealthCareActivity"}, {"text": "optical coherence tomography", "type": "HealthCareActivity"}]}

Example input:
Sentence: The present method of optimized HR - FSE imaging with a 3 T system improved visualization of intimal flaps and should thus be considered for assessing patients with suspected ICAD that cannot be definitively diagnosed by conventional imaging modalities .

Example answer:
{"entities": [{"text": "HR - FSE imaging", "type": "HealthCareActivity"}, {"text": "improved", "type": "Finding"}, {"text": "visualization", "type": "HealthCareActivity"}, {"text": "intimal flaps", "type": "AnatomicalStructure"}, {"text": "ICAD", "type": "AnatomicalStructure"}, {"text": "diagnosed", "type": "Finding"}]}

Example input:
Sentence: A combined optical coherence tomography and intravascular ultrasound study Some plaques grow slowly in a linear manner , whereas others undergo a rapid phasic progression .

Example answer:
{"entities": [{"text": "optical coherence tomography", "type": "HealthCareActivity"}, {"text": "intravascular ultrasound", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "plaques", "type": "Finding"}, {"text": "grow slowly", "type": "Finding"}]}

Example input:
Sentence: The aim of the current study was to compare the performance of MRI and ultrasound in detecting carotid artery plaques and measuring extent of atherosclerosis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "ultrasound", "type": "HealthCareActivity"}, {"text": "detecting", "type": "Finding"}, {"text": "carotid artery plaques", "type": "AnatomicalStructure"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "atherosclerosis", "type": "BiologicFunction"}]}

Example input:
Sentence: On the one hand , this technique allows a better and direct visualization of vascular and solid organ lesions .

Example answer:
{"entities": [{"text": "vascular", "type": "BiologicFunction"}, {"text": "solid organ", "type": "AnatomicalStructure"}, {"text": "lesions", "type": "Finding"}]}

Example input:
Sentence: For rapid imaging of the cerebrovasculature , digital subtraction angiography ( DSA ) remains the gold standard as it offers high spatial resolution .

Example answer:
{"entities": [{"text": "imaging", "type": "HealthCareActivity"}, {"text": "cerebrovasculature", "type": "BodySystem"}, {"text": "digital subtraction angiography", "type": "HealthCareActivity"}, {"text": "DSA", "type": "HealthCareActivity"}]}

Example input:
Sentence: Before the introduction of this technique , vascular puncture was acquired based on an integration of angiographic data , the bony iliofemoral landmarks and a radiopaque object .

Example answer:
{"entities": [{"text": "vascular", "type": "AnatomicalStructure"}, {"text": "puncture", "type": "HealthCareActivity"}, {"text": "angiographic", "type": "HealthCareActivity"}, {"text": "iliofemoral", "type": "AnatomicalStructure"}, {"text": "landmarks", "type": "SpatialConcept"}]}

Example input:
Sentence: The results provide further evidence that retinal vascular features are clinically informative about underlying stroke risk factors and demonstrate the utility of handheld retinal photography in the stroke ward .

Example answer:
{"entities": [{"text": "retinal", "type": "AnatomicalStructure"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "retinal photography", "type": "HealthCareActivity"}, {"text": "ward", "type": "Organization"}]}

Example input:
Sentence: Vessels abnormalities were assessed with brain computed tomography ( CT ) angiography , magnetic resonance angiography ( MRA ) and / or digital subtraction angiography ( DSA ) .

Example answer:
{"entities": [{"text": "Vessels abnormalities", "type": "Finding"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "computed tomography", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "angiography", "type": "HealthCareActivity"}, {"text": "magnetic resonance angiography", "type": "HealthCareActivity"}, {"text": "MRA", "type": "HealthCareActivity"}, {"text": "digital subtraction angiography", "type": "HealthCareActivity"}, {"text": "DSA", "type": "HealthCareActivity"}]}

Example input:
Sentence: The quality of the imaging procedure was compared according to four items : global vascular opacification , cerebral venous opacification , and lower limbs opacification ( arterial and venous ) .

Example answer:
{"entities": [{"text": "imaging procedure", "type": "HealthCareActivity"}, {"text": "global vascular", "type": "AnatomicalStructure"}, {"text": "lower limbs", "type": "AnatomicalStructure"}, {"text": "arterial", "type": "SpatialConcept"}, {"text": "venous", "type": "SpatialConcept"}]}

Input:
Sentence: Modern imaging equipment can facilitate precise measurement and monitoring of vascular features .

## Item MedMentions:test:2638
Example input:
Sentence: AKT / GSK3β Signaling in Glioblastoma Glioblastoma ( GBM ) is the most aggressive of primary brain tumors .

Example answer:
{"entities": [{"text": "AKT", "type": "Chemical"}, {"text": "GSK3β", "type": "Chemical"}, {"text": "Signaling", "type": "BiologicFunction"}, {"text": "Glioblastoma", "type": "BiologicFunction"}, {"text": "GBM", "type": "BiologicFunction"}, {"text": "brain tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: PI3 K and its downstream Akt are widely expressed in the spinal cord , particularly in the laminae I - IV of the dorsal horn , where nociceptive C and Aδ fibers of primary afferents principally terminate .

Example answer:
{"entities": [{"text": "PI3 K", "type": "Chemical"}, {"text": "downstream", "type": "SpatialConcept"}, {"text": "Akt", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "spinal cord", "type": "AnatomicalStructure"}, {"text": "laminae I - IV", "type": "AnatomicalStructure"}, {"text": "dorsal horn", "type": "AnatomicalStructure"}, {"text": "nociceptive C", "type": "AnatomicalStructure"}, {"text": "Aδ fibers", "type": "AnatomicalStructure"}, {"text": "afferents", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Much less attention has been paid to the role of glycogen synthase kinase 3 β ( GSK3β ) , a target of AKT .

Example answer:
{"entities": [{"text": "glycogen synthase kinase 3 β", "type": "Chemical"}, {"text": "GSK3β", "type": "Chemical"}, {"text": "AKT", "type": "Chemical"}]}

Example input:
Sentence: Exposure of CreaT and GSK3ß expressing oocytes for 24 hours to Lithium was followed by a significant increase of the creatine induced current .

Example answer:
{"entities": [{"text": "CreaT", "type": "Chemical"}, {"text": "GSK3ß", "type": "Chemical"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "oocytes", "type": "AnatomicalStructure"}, {"text": "Lithium", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "current", "type": "BiologicFunction"}]}

Example input:
Sentence: Down - Regulation of the Na + , Cl - Coupled Creatine Transporter CreaT ( SLC6A8 ) by Glycogen Synthase Kinase GSK3ß The Na + , Cl - coupled creatine transporter CreaT ( SLC6A8 ) is expressed in a variety of tissues including the brain .

Example answer:
{"entities": [{"text": "Down - Regulation", "type": "BiologicFunction"}, {"text": "Na + , Cl -", "type": "Chemical"}, {"text": "Creatine Transporter", "type": "Chemical"}, {"text": "CreaT", "type": "Chemical"}, {"text": "SLC6A8", "type": "Chemical"}, {"text": "Glycogen Synthase Kinase", "type": "Chemical"}, {"text": "GSK3ß", "type": "Chemical"}, {"text": "creatine transporter", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Kinetic analysis revealed that GSK3ß significantly decreased the maximal creatine transport rate .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "GSK3ß", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "transport", "type": "BiologicFunction"}]}

Example input:
Sentence: GSK3ß is phosphorylated and thus inhibited by PKB / Akt .

Example answer:
{"entities": [{"text": "GSK3ß", "type": "Chemical"}, {"text": "phosphorylated", "type": "BiologicFunction"}, {"text": "PKB / Akt", "type": "Chemical"}]}

Example input:
Sentence: In CreaT expressing oocytes , co - expression of GSK3ß but not of K85RGSK3ß , resulted in a significant decrease of creatine induced current .

Example answer:
{"entities": [{"text": "CreaT", "type": "Chemical"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "oocytes", "type": "AnatomicalStructure"}, {"text": "co - expression", "type": "BiologicFunction"}, {"text": "GSK3ß", "type": "Chemical"}, {"text": "K85RGSK3ß", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "current", "type": "BiologicFunction"}]}

Example input:
Sentence: GSK3ß down - regulates the creatine transporter CreaT , an effect reversed by treatment with the antidepressant Lithium and by co - expression of PKB / Akt .

Example answer:
{"entities": [{"text": "GSK3ß", "type": "Chemical"}, {"text": "down - regulates", "type": "BiologicFunction"}, {"text": "creatine transporter", "type": "Chemical"}, {"text": "CreaT", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "Lithium", "type": "Chemical"}, {"text": "co - expression", "type": "BiologicFunction"}, {"text": "PKB / Akt", "type": "Chemical"}]}

Example input:
Sentence: CreaT was expressed in Xenopus laevis oocytes with or without wild - type GSK3ß or inactive K85RGSK3ß .

Example answer:
{"entities": [{"text": "CreaT", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "Xenopus laevis", "type": "Eukaryote"}, {"text": "oocytes", "type": "AnatomicalStructure"}, {"text": "wild - type", "type": "AnatomicalStructure"}, {"text": "GSK3ß", "type": "Chemical"}, {"text": "inactive K85RGSK3ß", "type": "Chemical"}]}

Input:
Sentence: CreaT and GSK3ß were further expressed without and with additional expression of wild type PKB / Akt .

## Item MedMentions:test:2469
Example input:
Sentence: The micelle system of CS - P68 and CS - P127 formed at drug to polymer ratios of 1 : 4 and 1 : 2 , respectively , was found to be the most suitable monodispersed system with a nanosize - range diameter .

Example answer:
{"entities": [{"text": "micelle system", "type": "Chemical"}, {"text": "CS - P68", "type": "Chemical"}, {"text": "CS - P127", "type": "Chemical"}, {"text": "drug", "type": "Chemical"}, {"text": "polymer", "type": "Chemical"}]}

Example input:
Sentence: After the GO - Fe3O4 / SiO2 / AuNWs / L - Cys composites were applied to glycopeptide enrichment , 26 glycopeptides from a human IgG digest could be identified , with a detection limit as low as 10 fmol .

Example answer:
{"entities": [{"text": "GO", "type": "Chemical"}, {"text": "Fe3O4", "type": "Chemical"}, {"text": "SiO2", "type": "Chemical"}, {"text": "L - Cys", "type": "Chemical"}, {"text": "glycopeptide", "type": "Chemical"}, {"text": "glycopeptides", "type": "Chemical"}, {"text": "human IgG", "type": "Chemical"}]}

Example input:
Sentence: Liquid trimyristin nanoparticles loaded with fenofibrate , orlistat , tocopherol acetate and ubidecarenone were studied in three different release media with increasing complexity and comparability to physiological conditions : a rapeseed oil nanoemulsion , porcine serum and porcine blood .

Example answer:
{"entities": [{"text": "trimyristin", "type": "Chemical"}, {"text": "fenofibrate", "type": "Chemical"}, {"text": "orlistat", "type": "Chemical"}, {"text": "tocopherol acetate", "type": "Chemical"}, {"text": "ubidecarenone", "type": "Chemical"}, {"text": "media", "type": "Chemical"}, {"text": "porcine", "type": "Eukaryote"}, {"text": "serum", "type": "BodySubstance"}, {"text": "blood", "type": "BodySubstance"}]}

Example input:
Sentence: In RCE and in pig cornea , the micelles improved the penetration of both rhodamine andr cyclosporine .

Example answer:
{"entities": [{"text": "RCE", "type": "AnatomicalStructure"}, {"text": "pig", "type": "Eukaryote"}, {"text": "cornea", "type": "AnatomicalStructure"}, {"text": "micelles", "type": "Chemical"}, {"text": "improved", "type": "Finding"}, {"text": "rhodamine", "type": "Chemical"}, {"text": "cyclosporine", "type": "Chemical"}]}

Example input:
Sentence: A model chitosan - tripolyphosphate ( TPP ) hydrogel nanoparticles ( CS - HNP ) , with a broad spectrum of possible applications was produced and sterilized in the absence and in the presence of protective sugars ( glucose and mannitol ) .

Example answer:
{"entities": [{"text": "chitosan", "type": "Chemical"}, {"text": "tripolyphosphate", "type": "Chemical"}, {"text": "TPP", "type": "Chemical"}, {"text": "CS", "type": "Chemical"}, {"text": "possible", "type": "Finding"}, {"text": "sterilized", "type": "HealthCareActivity"}, {"text": "protective sugars", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "mannitol", "type": "Chemical"}]}

Example input:
Sentence: PEG - DSPE coating may be related to better absorption , based on the stability and a pharmacokinetic improvement in the blood circulation time .

Example answer:
{"entities": [{"text": "PEG - DSPE", "type": "Chemical"}, {"text": "blood circulation time", "type": "HealthCareActivity"}]}

Example input:
Sentence: CS - PEG -blended PLGA nano - delivery system of quercetin , ellagic acid and gallic acid can potentiate apoptosis - mediated cell death in HepG2 cell line .

Example answer:
{"entities": [{"text": "CS", "type": "Chemical"}, {"text": "PEG", "type": "Chemical"}, {"text": "PLGA", "type": "Chemical"}, {"text": "quercetin", "type": "Chemical"}, {"text": "ellagic acid", "type": "Chemical"}, {"text": "gallic acid", "type": "Chemical"}, {"text": "apoptosis - mediated", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "HepG2 cell line", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The immobilization approach includes the loading of DSPE - PEG ( 2000 ) - biotin containing sterically stabilized micelles ( SSMs ) which are restructured in a buffer change step , resulting in an accessible substrate for liposome immobilization .

Example answer:
{"entities": [{"text": "immobilization", "type": "HealthCareActivity"}, {"text": "DSPE - PEG ( 2000 )", "type": "Chemical"}, {"text": "biotin", "type": "Chemical"}, {"text": "micelles", "type": "Chemical"}, {"text": "SSMs", "type": "Chemical"}, {"text": "liposome", "type": "Chemical"}]}

Example input:
Sentence: On application of physiologically acceptable external magnetic field , FITC conjugated artemisinin magnetic nanoparticles showed an enhanced accumulation of nanoparticles in the 4T1 breast tumour tissues of BALB / c mice model .

Example answer:
{"entities": [{"text": "external", "type": "SpatialConcept"}, {"text": "FITC", "type": "Chemical"}, {"text": "artemisinin", "type": "Chemical"}, {"text": "4T1 breast tumour tissues", "type": "AnatomicalStructure"}, {"text": "BALB / c mice", "type": "Eukaryote"}, {"text": "model", "type": "BiologicFunction"}]}

Example input:
Sentence: CS - PEG decorated PLGA nano - prototype for delivery of bioactive compounds : A novel approach for induction of apoptosis in HepG2 cell line Polymer - based nanoparticles are used as vectors for cancer drug delivery .

Example answer:
{"entities": [{"text": "CS", "type": "Chemical"}, {"text": "PEG", "type": "Chemical"}, {"text": "PLGA nano - prototype", "type": "Chemical"}, {"text": "bioactive compounds", "type": "Chemical"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "HepG2 cell line", "type": "AnatomicalStructure"}, {"text": "Polymer", "type": "Chemical"}, {"text": "vectors", "type": "SpatialConcept"}, {"text": "cancer", "type": "BiologicFunction"}]}

Input:
Sentence: Reaction of Lymphoid Organs to Injection of Iron - Carbon Nanoparticles The distribution of iron - carbon nanoparticles in FeC - DSPE - PEG - 2000 modification ( micellar particles with structure ( Fe ) core - carbon shell ; PEG -based coating ) is studied .

## Item MedMentions:test:1992
Example input:
Sentence: RRMS patients had higher levels of NFL , CXCL13 , CHI3L1 , and CHIT1 than controls ( p < 0 .

Example answer:
{"entities": [{"text": "RRMS", "type": "BiologicFunction"}, {"text": "NFL", "type": "Chemical"}, {"text": "CXCL13", "type": "Chemical"}, {"text": "CHI3L1", "type": "Chemical"}, {"text": "CHIT1", "type": "Chemical"}]}

Example input:
Sentence: Cell wall polymers in culms were quantified by means of the monoclonal antibodies LM6 , LM11 , JIM13 and BS - 400 - 3 and the carbohydrate - binding module CBM3a using the high - throughput CoMPP technique .

Example answer:
{"entities": [{"text": "Cell wall", "type": "AnatomicalStructure"}, {"text": "culms", "type": "Eukaryote"}, {"text": "monoclonal antibodies", "type": "Chemical"}, {"text": "LM6", "type": "Chemical"}, {"text": "LM11", "type": "Chemical"}, {"text": "JIM13", "type": "Chemical"}, {"text": "BS - 400 - 3", "type": "Chemical"}, {"text": "carbohydrate - binding module CBM3a", "type": "Chemical"}, {"text": "CoMPP technique", "type": "HealthCareActivity"}]}

Example input:
Sentence: In contrast , SHED - CM specifically depleted of a set of anti - inflammatory M2 macrophage inducers , monocyte chemoattractant protein - 1 ( MCP - 1 ) and the secreted ectodomain of sialic acid - binding Ig - like lectin - 9 ( sSiglec - 9 ) lost the ability to restore neurological function in this model .

Example answer:
{"entities": [{"text": "SHED - CM", "type": "AnatomicalStructure"}, {"text": "M2 macrophage", "type": "AnatomicalStructure"}, {"text": "monocyte chemoattractant protein - 1", "type": "Chemical"}, {"text": "MCP - 1", "type": "Chemical"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "ectodomain", "type": "SpatialConcept"}, {"text": "sialic acid - binding Ig - like lectin - 9", "type": "Chemical"}, {"text": "sSiglec - 9", "type": "Chemical"}, {"text": "restore", "type": "HealthCareActivity"}, {"text": "neurological function", "type": "BiologicFunction"}]}

Example input:
Sentence: After the GO - Fe3O4 / SiO2 / AuNWs / L - Cys composites were applied to glycopeptide enrichment , 26 glycopeptides from a human IgG digest could be identified , with a detection limit as low as 10 fmol .

Example answer:
{"entities": [{"text": "GO", "type": "Chemical"}, {"text": "Fe3O4", "type": "Chemical"}, {"text": "SiO2", "type": "Chemical"}, {"text": "L - Cys", "type": "Chemical"}, {"text": "glycopeptide", "type": "Chemical"}, {"text": "glycopeptides", "type": "Chemical"}, {"text": "human IgG", "type": "Chemical"}]}

Example input:
Sentence: Serum biomarkers of cartilage function and inflammation [ collagen type II C - telopeptide ( CTXII ) , cartilage oligomeric matrix protein ( COMP ) , and alpha - 2 - macroglobulin ( A2 M ) ] were measured by ELISA .

Example answer:
{"entities": [{"text": "Serum", "type": "BodySubstance"}, {"text": "biomarkers", "type": "ClinicalAttribute"}, {"text": "cartilage function", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "collagen type II C - telopeptide", "type": "HealthCareActivity"}, {"text": "CTXII", "type": "HealthCareActivity"}, {"text": "cartilage oligomeric matrix protein", "type": "HealthCareActivity"}, {"text": "COMP", "type": "HealthCareActivity"}, {"text": "alpha - 2 - macroglobulin", "type": "HealthCareActivity"}, {"text": "A2 M", "type": "HealthCareActivity"}, {"text": "ELISA", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the CSX group , a significant correlation was found between TCC and FCN3 - TCC level ( r = 0 . 507 , P = 0 . 032 ) and between ficolin - 3 / MASP - 2 complex level and FCN3 - TCC deposition ( r = 0 . 651 , P = 0 . 003 ) .

Example answer:
{"entities": [{"text": "CSX", "type": "BiologicFunction"}, {"text": "TCC", "type": "Chemical"}, {"text": "FCN3", "type": "Chemical"}, {"text": "ficolin - 3", "type": "Chemical"}, {"text": "MASP - 2", "type": "Chemical"}, {"text": "complex", "type": "Chemical"}]}

Example input:
Sentence: Serum levels of ficolin - 2 and ficolin - 3 , ficolin - 3 / MASP - 2 complex and ficolin - 3 -mediated TCC deposition ( FCN3 - TCC ) were determined .

Example answer:
{"entities": [{"text": "Serum", "type": "BodySubstance"}, {"text": "ficolin - 2", "type": "Chemical"}, {"text": "ficolin - 3", "type": "Chemical"}, {"text": "MASP - 2", "type": "Chemical"}, {"text": "complex", "type": "Chemical"}, {"text": "TCC", "type": "Chemical"}, {"text": "FCN3", "type": "Chemical"}]}

Example input:
Sentence: Levels of interleukin - 6 ( IL - 6 ) , interferon - γ inducible protein - 10 ( CXCL10 ) , and monocyte chemoattractant protein - 1 ( CCL2 ) were determined by enzyme - linked immunosorbant assay ( ELISA ) .

Example answer:
{"entities": [{"text": "interleukin - 6", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "interferon - γ inducible protein - 10", "type": "Chemical"}, {"text": "CXCL10", "type": "Chemical"}, {"text": "monocyte chemoattractant protein - 1", "type": "Chemical"}, {"text": "CCL2", "type": "Chemical"}, {"text": "enzyme - linked immunosorbant assay", "type": "HealthCareActivity"}, {"text": "ELISA", "type": "HealthCareActivity"}]}

Example input:
Sentence: NFL and CHIT1 levels correlated with relapse status , and NFL and CXCL13 levels correlated with the formation of new magnetic resonance imaging lesions .

Example answer:
{"entities": [{"text": "NFL", "type": "Chemical"}, {"text": "CHIT1", "type": "Chemical"}, {"text": "relapse status", "type": "BiologicFunction"}, {"text": "CXCL13", "type": "Chemical"}, {"text": "magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "lesions", "type": "Finding"}]}

Example input:
Sentence: The results indicate that CSF levels of NFL , CXCL13 , CHI3L1 , and CHIT1 correlate with the clinical and / or radiological disease activity , providing additional dimensions in the assessment of treatment efficacy .

Example answer:
{"entities": [{"text": "CSF", "type": "BodySubstance"}, {"text": "NFL", "type": "Chemical"}, {"text": "CXCL13", "type": "Chemical"}, {"text": "CHI3L1", "type": "Chemical"}, {"text": "CHIT1", "type": "Chemical"}, {"text": "assessment", "type": "HealthCareActivity"}]}

Input:
Sentence: The concentrations of C - X - C motif chemokine 13 ( CXCL13 ) , C - C motif chemokine ligand 2 ( CCL2 ) , chitinase - 3 - like protein 1 ( CHI3L1 ) , glial fibrillary acidic protein , neurofilament light protein ( NFL ) , and neurogranin were determined by ELISA , and chitotriosidase ( CHIT1 ) was analyzed by spectrofluorometry .

## Item MedMentions:test:2902
Example input:
Sentence: Meta - analysis for poor prognostic factors as determined by hazard ratio ( HR ) and 95 % confidential interval ( 95 % CI ) .

Example answer:
{"entities": [{"text": "Meta - analysis", "type": "ResearchActivity"}, {"text": "prognostic factors", "type": "ClinicalAttribute"}]}

Example input:
Sentence: We performed a meta - analysis using weighted mean differences ( WMD ) and 95 % confidence intervals in a random - effects model .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: The present meta - analysis aims to determine whether the resuscitative phase really takes advantages by being performed with EGDT .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}, {"text": "resuscitative", "type": "HealthCareActivity"}, {"text": "EGDT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Meta - analytic methods will be employed wherever appropriate .

Example answer:
{"entities": [{"text": "Meta - analytic methods", "type": "ResearchActivity"}]}

Example input:
Sentence: Meta - analyses of 21 interventions fully or partially recommended their use , with recommendations being positively correlated with the effect sizes of the pooled intervention .

Example answer:
{"entities": [{"text": "Meta - analyses", "type": "ResearchActivity"}, {"text": "positively", "type": "Finding"}]}

Example input:
Sentence: Our results are consistent with the meta - analysis .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: A random effects meta - analysis was then used to estimate pooled effects .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Meta - analysis was performed using HR and 95 % CI as the primary outcomes of interest .

Example answer:
{"entities": [{"text": "Meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: The outcomes subject to meta - analysis were pulmonary function , hospitalization , and further treatment .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "IntellectualProduct"}, {"text": "pulmonary function", "type": "BiologicFunction"}, {"text": "hospitalization", "type": "HealthCareActivity"}, {"text": "further treatment", "type": "Finding"}]}

Example input:
Sentence: Due to the variations in setting , design and outcome it was not feasible to pool results using a meta - analysis .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}]}

Input:
Sentence: Meta - analysis was used to pool results for these outcomes .

