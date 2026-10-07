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

## Item MedMentions:test:1572
Example input:
Sentence: Ten - year other cause mortality -free survival rates were 90 % and 88 % after nephron sparing surgery and radical nephrectomy , respectively .

Example answer:
{"entities": [{"text": "other cause mortality", "type": "Finding"}, {"text": "nephron sparing surgery", "type": "HealthCareActivity"}, {"text": "radical nephrectomy", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , there was a statistically significant increase in overall disease -associated amputation rates from 5 .

Example answer:
{"entities": [{"text": "disease", "type": "BiologicFunction"}, {"text": "amputation", "type": "HealthCareActivity"}]}

Example input:
Sentence: This study aimed to resolve the association of all four non - invasive haemodynamic parameters in clinically symptomatic patients with PAD with cardiovascular mortality , overall mortality , and amputation free survival ( AFS ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "haemodynamic", "type": "BiologicFunction"}, {"text": "parameters", "type": "Finding"}, {"text": "PAD", "type": "BiologicFunction"}, {"text": "cardiovascular", "type": "SpatialConcept"}]}

Example input:
Sentence: 48 - 9 . 19 [ p = . 050 ] , respectively ; all - cause mortality ( HR 2 . 05 , 95 % CI 1 . 44 - 2 . 92 [ p < . 001 ] ; HR 2 . 53 , 95 % CI 1 . 35 - 4 . 74 [ p = . 040 ] , respectively ) ; and amputation or death ( HR 2 . 13 , 95 % CI 1 .

Example answer:
{"entities": [{"text": "amputation", "type": "HealthCareActivity"}, {"text": "death", "type": "BiologicFunction"}]}

Example input:
Sentence: Potentially preventable amputations associated with high - risk diseases are increasing among patients who require inpatient hospital admission , present to the ED , or require outpatient interventional treatment .

Example answer:
{"entities": [{"text": "amputations", "type": "HealthCareActivity"}, {"text": "risk", "type": "HealthCareActivity"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "hospital admission", "type": "HealthCareActivity"}, {"text": "ED", "type": "Organization"}]}

Example input:
Sentence: Within all age groups , men had worse amputation - free survival than women did .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "amputation", "type": "HealthCareActivity"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: We also attempted to create a measure of a patient 's ability to manage chronic diseases or to access appropriate outpatient care for ulcer management by accounting for hospital and emergency department ( ED ) visits in the preceding 60 days to determine how this also affects amputation - free survival .

Example answer:
{"entities": [{"text": "chronic diseases", "type": "BiologicFunction"}, {"text": "outpatient care", "type": "HealthCareActivity"}, {"text": "ulcer management", "type": "HealthCareActivity"}, {"text": "hospital", "type": "Organization"}, {"text": "emergency department", "type": "Organization"}, {"text": "ED", "type": "Organization"}, {"text": "amputation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Amputation - free survival for the PAD , DM , and PAD / DM groups was determined .

Example answer:
{"entities": [{"text": "Amputation", "type": "HealthCareActivity"}, {"text": "PAD", "type": "BiologicFunction"}, {"text": "DM", "type": "BiologicFunction"}]}

Example input:
Sentence: Demographic factors , cardiovascular mortality , all - cause mortality , and above foot level amputations were obtained and assessed in relation to AP , ABI , TP , and TBI by means of Kaplan - Meier life tables and a multivariate Cox regression model .

Example answer:
{"entities": [{"text": "cardiovascular", "type": "SpatialConcept"}, {"text": "amputations", "type": "HealthCareActivity"}, {"text": "AP", "type": "ClinicalAttribute"}, {"text": "ABI", "type": "HealthCareActivity"}, {"text": "TP", "type": "ClinicalAttribute"}, {"text": "TBI", "type": "HealthCareActivity"}, {"text": "Kaplan - Meier life tables", "type": "ResearchActivity"}, {"text": "Cox regression model", "type": "IntellectualProduct"}]}

Example input:
Sentence: Race did not predict amputation - free survival , but having multiple prior ED or hospital admissions was a significant predictor of worse amputation - free survival .

Example answer:
{"entities": [{"text": "amputation", "type": "HealthCareActivity"}, {"text": "ED", "type": "Organization"}, {"text": "hospital admissions", "type": "HealthCareActivity"}]}

Input:
Sentence: In addition , we characterize patient factors that affect amputation - free survival .

## Item MedMentions:test:1566
Example input:
Sentence: stuartii strain carrying acquired resistance genes conferring panresistance to cephalosporins ( blaSHV - 5 and blaVEB - 1 ) , carbapenems ( blaVIM - 1 ) , and aminoglycosides ( rmtB ) involved in an outbreak in Greek hospitals .

Example answer:
{"entities": [{"text": "stuartii strain", "type": "Bacterium"}, {"text": "cephalosporins", "type": "Chemical"}, {"text": "blaSHV - 5", "type": "AnatomicalStructure"}, {"text": "blaVEB - 1", "type": "AnatomicalStructure"}, {"text": "carbapenems", "type": "Chemical"}, {"text": "blaVIM - 1", "type": "AnatomicalStructure"}, {"text": "aminoglycosides", "type": "Chemical"}, {"text": "rmtB", "type": "AnatomicalStructure"}, {"text": "Greek", "type": "SpatialConcept"}, {"text": "hospitals", "type": "Organization"}]}

Example input:
Sentence: Mey . ) Schischk An orange - coloured , aerobic , motile and short - rods bacterial strain , designated EGI 6500337 T , was isolated from the surface - sterilized root of a halophyte Anabasis elatior ( C .

Example answer:
{"entities": [{"text": "Mey . ) Schischk", "type": "Eukaryote"}, {"text": "short - rods bacterial strain", "type": "Bacterium"}, {"text": "EGI 6500337 T", "type": "Bacterium"}, {"text": "root", "type": "Eukaryote"}, {"text": "halophyte", "type": "Eukaryote"}, {"text": "Anabasis elatior ( C .", "type": "Eukaryote"}]}

Example input:
Sentence: Morpho - Molecular Characterization of Soil Inhabitant Dermatophytes from Ahvaz , Southwest of Iran , a High Occurrence of Microsporum fulvum Occurrence and diversity of dermatophyte mycoflora in 298 soil samples from Ahvaz , Southwest of Iran was investigated by using the hair - baiting technique .

Example answer:
{"entities": [{"text": "Molecular", "type": "SpatialConcept"}, {"text": "Dermatophytes", "type": "Eukaryote"}, {"text": "Ahvaz", "type": "SpatialConcept"}, {"text": "Southwest", "type": "SpatialConcept"}, {"text": "Iran", "type": "SpatialConcept"}, {"text": "Microsporum fulvum", "type": "Eukaryote"}, {"text": "dermatophyte mycoflora", "type": "Eukaryote"}]}

Example input:
Sentence: Systemic Collyriclum faba ( Trematoda : Collyriclidae ) Infection in a Wild Common Raven ( Corvus corax ) A hatch - year Common Raven ( Corvus corax ) with subcutaneous and internal pseudocysts , filled with fluid , containing a pair of adult trematodes and numerous eggs consistent with Collyriclum faba , died near a riverbank in California , US .

Example answer:
{"entities": [{"text": "Collyriclum faba", "type": "Eukaryote"}, {"text": "Trematoda", "type": "Eukaryote"}, {"text": "Collyriclidae", "type": "Eukaryote"}, {"text": "Infection", "type": "BiologicFunction"}, {"text": "Raven", "type": "Eukaryote"}, {"text": "Corvus corax", "type": "Eukaryote"}, {"text": "subcutaneous", "type": "SpatialConcept"}, {"text": "internal", "type": "SpatialConcept"}, {"text": "pseudocysts", "type": "AnatomicalStructure"}, {"text": "adult", "type": "Eukaryote"}, {"text": "trematodes", "type": "Eukaryote"}, {"text": "eggs", "type": "Eukaryote"}, {"text": "died", "type": "Finding"}, {"text": "California", "type": "SpatialConcept"}, {"text": "US", "type": "SpatialConcept"}]}

Example input:
Sentence: equigenitalis field isolates ( n = 40 ) obtained from Austrian Lipizzaner horses were differentiated into three REP ( rep - E1 , rep - E3a , and rep - E4 ) and three PFGE genotypes ( TE - A2 , TE - A5 , and TE - D ) ; those isolated from four Austrian Trotters belonged to the REP / PFGE genotype rep - E2 / TE - A1 .

Example answer:
{"entities": [{"text": "equigenitalis", "type": "Bacterium"}, {"text": "isolates", "type": "Chemical"}, {"text": "Austrian Lipizzaner horses", "type": "Eukaryote"}, {"text": "REP", "type": "SpatialConcept"}, {"text": "PFGE", "type": "HealthCareActivity"}, {"text": "Austrian Trotters", "type": "Eukaryote"}]}

Example input:
Sentence: Rhizothera was originally described in the genus Perdix ( true partridges ) , although a partial cytochrome b ( CYB ) sequence suggests it is sister to Pucrasia ( koklass pheasant ) .

Example answer:
{"entities": [{"text": "Rhizothera", "type": "Eukaryote"}, {"text": "Perdix", "type": "Eukaryote"}, {"text": "true partridges", "type": "Eukaryote"}, {"text": "cytochrome b", "type": "Chemical"}, {"text": "CYB", "type": "Chemical"}, {"text": "Pucrasia", "type": "Eukaryote"}, {"text": "koklass pheasant", "type": "Eukaryote"}]}

Example input:
Sentence: Species distribution modeling and molecular markers suggest longitudinal range shifts and cryptic northern refugia of the typical calcareous grassland species Hippocrepis comosa ( horseshoe vetch ) Calcareous grasslands belong to the most diverse , endangered habitats in Europe , but there is still insufficient information about the origin of the plant species related to these grasslands .

Example answer:
{"entities": [{"text": "Species", "type": "IntellectualProduct"}, {"text": "modeling", "type": "ResearchActivity"}, {"text": "molecular markers", "type": "ClinicalAttribute"}, {"text": "calcareous grassland", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Hippocrepis comosa", "type": "Eukaryote"}, {"text": "horseshoe vetch", "type": "Eukaryote"}, {"text": "Calcareous grasslands", "type": "SpatialConcept"}, {"text": "endangered habitats", "type": "SpatialConcept"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "plant", "type": "Eukaryote"}, {"text": "grasslands", "type": "SpatialConcept"}]}

Example input:
Sentence: Aeromonas salmonicida subsp .

Example answer:
{"entities": [{"text": "Aeromonas salmonicida subsp .", "type": "Bacterium"}]}

Example input:
Sentence: jejuni 81116 ( Penner serotype HS : 6 ) lipoglycan contains two dideoxyhexosamine residues , and enzymological assay data show that this bacterial strain can synthesize both dTDP - 3 - acetamido - 3 , 6 - dideoxy - d - glucose and dTDP - 3 - acetamido - 3 , 6 - dideoxy - d - galactose .

Example answer:
{"entities": [{"text": "jejuni 81116", "type": "IntellectualProduct"}, {"text": "Penner serotype HS : 6", "type": "IntellectualProduct"}, {"text": "lipoglycan", "type": "Chemical"}, {"text": "dideoxyhexosamine", "type": "Chemical"}, {"text": "enzymological assay", "type": "HealthCareActivity"}, {"text": "bacterial strain", "type": "Bacterium"}, {"text": "dTDP - 3 - acetamido - 3 , 6 - dideoxy - d - glucose", "type": "Chemical"}, {"text": "dTDP - 3 - acetamido - 3 , 6 - dideoxy - d - galactose", "type": "Chemical"}]}

Example input:
Sentence: Inducible Expression of both ermB and ermT Conferred High Macrolide Resistance in Streptococcus gallolyticus subsp .

Example answer:
{"entities": [{"text": "Expression", "type": "BiologicFunction"}, {"text": "ermB", "type": "AnatomicalStructure"}, {"text": "ermT", "type": "AnatomicalStructure"}, {"text": "Macrolide Resistance", "type": "Finding"}, {"text": "Streptococcus gallolyticus subsp .", "type": "Bacterium"}]}

Input:
Sentence: gallolyticus subsp .

## Item MedMentions:test:1334
Example input:
Sentence: Both mono - spectrum images of Group A and polychromatic images of Group B were used to reconstruct maximum intensity projection ( MIP ) and volume rendering ( VR ) images of the perforating artery , respectively .

Example answer:
{"entities": [{"text": "mono - spectrum images", "type": "IntellectualProduct"}, {"text": "polychromatic images", "type": "IntellectualProduct"}, {"text": "images", "type": "IntellectualProduct"}, {"text": "perforating artery", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The feasibility of the electrospray deposition device was investigated by combination with MALDI FTICR MSI to analyze the distributions of lipids in mouse brain and liver cancer tissue section .

Example answer:
{"entities": [{"text": "electrospray deposition device", "type": "MedicalDevice"}, {"text": "MALDI FTICR MSI", "type": "HealthCareActivity"}, {"text": "distributions", "type": "BiologicFunction"}, {"text": "lipids", "type": "Chemical"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "brain", "type": "BiologicFunction"}, {"text": "liver cancer", "type": "BiologicFunction"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: By univariate analysis , blood pressure ( BP ) , heart rate , National Institutes of Health Stroke Scale ( NIHSS ) score , number of diffusion - positive lesion , count of red blood cell , high - density lipoprotein , and degree of stenosis differed significantly between the 2 groups .

Example answer:
{"entities": [{"text": "blood pressure", "type": "BiologicFunction"}, {"text": "BP", "type": "BiologicFunction"}, {"text": "heart rate", "type": "ClinicalAttribute"}, {"text": "National Institutes of Health Stroke Scale ( NIHSS ) score", "type": "Finding"}, {"text": "positive", "type": "Finding"}, {"text": "lesion", "type": "Finding"}, {"text": "count of red blood cell", "type": "HealthCareActivity"}, {"text": "high - density lipoprotein", "type": "Chemical"}]}

Example input:
Sentence: This chapter presents a protocol for an optimized and high - throughput IgG N - glycan release , fluorescent labeling and cleanup , and analysis of fluorescently labeled IgG N - glycans by hydrophilic interaction liquid chromatography ( HILIC ) on an ultra performance liquid chromatography ( UPLC ) system with fluorescence ( FLR ) detection .

Example answer:
{"entities": [{"text": "protocol", "type": "IntellectualProduct"}, {"text": "IgG N - glycan", "type": "Chemical"}, {"text": "fluorescent labeling", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "IgG N - glycans", "type": "Chemical"}, {"text": "hydrophilic interaction liquid chromatography", "type": "HealthCareActivity"}, {"text": "HILIC", "type": "HealthCareActivity"}, {"text": "ultra performance liquid chromatography", "type": "HealthCareActivity"}, {"text": "UPLC", "type": "HealthCareActivity"}, {"text": "detection", "type": "HealthCareActivity"}]}

Example input:
Sentence: NIR upconversion fluorescence glucose sensing and glucose - responsive insulin release of carbon dot - immobilized hybrid microgels at physiological pH This work reports the preparation of multifunctional hybrid microgels based on the one - pot free radical dispersion polymerization of hydrogen - bonding complexes in water , formed from hydroxyl / carboxyl bearing carbon dots with 4 - vinylphenylboronic acid and acrylamide comonomers , which can realize the simultaneous optical detection of glucose using near infrared light and glucose - responsive insulin delivery .

Example answer:
{"entities": [{"text": "NIR", "type": "HealthCareActivity"}, {"text": "glucose sensing", "type": "BiologicFunction"}, {"text": "glucose", "type": "Chemical"}, {"text": "insulin", "type": "Chemical"}, {"text": "carbon", "type": "Chemical"}, {"text": "immobilized", "type": "HealthCareActivity"}, {"text": "hybrid microgels", "type": "Chemical"}, {"text": "work", "type": "ResearchActivity"}, {"text": "reports", "type": "HealthCareActivity"}, {"text": "free radical", "type": "Chemical"}, {"text": "dispersion", "type": "SpatialConcept"}, {"text": "complexes", "type": "Chemical"}, {"text": "water", "type": "Chemical"}, {"text": "hydroxyl", "type": "Chemical"}, {"text": "carboxyl", "type": "Chemical"}, {"text": "4 - vinylphenylboronic acid", "type": "Chemical"}, {"text": "acrylamide", "type": "Chemical"}, {"text": "comonomers", "type": "Chemical"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "near infrared light", "type": "HealthCareActivity"}]}

Example input:
Sentence: 7 cells using ( 1 ) H NMR and U - HPLC / Q - TOF - MS Non - destructive proton nuclear magnetic resonance ( ( 1 ) H NMR ) spectroscopy and highly sensitive ultra - performance liquid chromatography quadrupole time - of - flight mass spectrometry ( U - HPLC / Q - TOF - MS ) coupled to data processing methods were applied to analyze the metabolic profiling changes of glycerophospholipids ( GPLs ) in RAW264 .

Example answer:
{"entities": [{"text": "7 cells", "type": "AnatomicalStructure"}, {"text": "( 1 ) H NMR", "type": "HealthCareActivity"}, {"text": "U - HPLC", "type": "HealthCareActivity"}, {"text": "Non - destructive proton nuclear magnetic resonance ( ( 1 ) H NMR ) spectroscopy", "type": "HealthCareActivity"}, {"text": "ultra - performance liquid chromatography", "type": "HealthCareActivity"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "metabolic profiling", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "glycerophospholipids", "type": "Chemical"}, {"text": "GPLs", "type": "Chemical"}, {"text": "RAW264 .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Using Lxrα knockout ( nr1h3 ( - / - ) ) and intestine - limited Lxrα over - expressing [ Tg ( fabp2a : EGFP - nr1h3 ) ] zebrafish strains , we measured post - prandial lipid excursion with live imaging in larvae and physiological methods in adults .

Example answer:
{"entities": [{"text": "Lxrα", "type": "AnatomicalStructure"}, {"text": "knockout", "type": "BiologicFunction"}, {"text": "nr1h3 ( - / - )", "type": "AnatomicalStructure"}, {"text": "intestine", "type": "AnatomicalStructure"}, {"text": "over - expressing", "type": "BiologicFunction"}, {"text": "fabp2a", "type": "AnatomicalStructure"}, {"text": "EGFP", "type": "AnatomicalStructure"}, {"text": "nr1h3", "type": "AnatomicalStructure"}, {"text": "zebrafish", "type": "Eukaryote"}, {"text": "lipid", "type": "Chemical"}, {"text": "live imaging", "type": "HealthCareActivity"}, {"text": "larvae", "type": "Eukaryote"}, {"text": "methods", "type": "IntellectualProduct"}]}

Example input:
Sentence: Such lipid core -containing plaque is still not identifiable by everyday angiography , thus triggering the need to develop a new tool where NIRS - IVUS can visualize plaque characterization in terms of its chemical and morphologic characteristic .

Example answer:
{"entities": [{"text": "lipid", "type": "Chemical"}, {"text": "core", "type": "SpatialConcept"}, {"text": "plaque", "type": "Finding"}, {"text": "angiography", "type": "HealthCareActivity"}, {"text": "NIRS", "type": "HealthCareActivity"}, {"text": "IVUS", "type": "HealthCareActivity"}, {"text": "chemical", "type": "IntellectualProduct"}, {"text": "morphologic", "type": "SpatialConcept"}]}

Example input:
Sentence: Fully Automated Lipid Pool Detection Using Near Infrared Spectroscopy Background .

Example answer:
{"entities": [{"text": "Lipid", "type": "Chemical"}, {"text": "Detection", "type": "HealthCareActivity"}, {"text": "Near Infrared Spectroscopy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Proposed algorithm is fully automated lipid pool detection on near infrared spectroscopy images .

Example answer:
{"entities": [{"text": "algorithm", "type": "IntellectualProduct"}, {"text": "lipid", "type": "Chemical"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "near infrared spectroscopy", "type": "HealthCareActivity"}, {"text": "images", "type": "IntellectualProduct"}]}

Input:
Sentence: In this study , the algorithm to fully automated lipid pool detection on NIRS images is proposed .

## Item MedMentions:test:1493
Example input:
Sentence: Men and women ≥ 65 years old were considered for this research , selected from first consultation records by the institution 's statistical unit for 2011 , who accepted to participate after being contacted by telephone .

Example answer:
{"entities": [{"text": "Men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "research", "type": "ResearchActivity"}, {"text": "consultation records", "type": "IntellectualProduct"}, {"text": "institution 's", "type": "Organization"}]}

Example input:
Sentence: Results The mean age of patients was 11 . 2 ± 5 . 4 years ( range , 1 - 27 years ) , and approximately one - half were female .

Example answer:
{"entities": [{"text": "female", "type": "PopulationGroup"}]}

Example input:
Sentence: After excluding participants with CVD , the study population included 3439 individuals , mean age 43 years , 56 % women , and 52 % black .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "CVD", "type": "BiologicFunction"}, {"text": "study population", "type": "PopulationGroup"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "black", "type": "PopulationGroup"}]}

Example input:
Sentence: Furthermore , 72 . 1 % of attenders were female with the median age 55 years and poor self - reported baseline health .

Example answer:
{"entities": []}

Example input:
Sentence: One hundred ( 100 ) patients were consecutively recruited : 60 women ( mean age 41 ± 14 years ) and 40 men ( mean age 46 ± 13 years ) .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: There were 27 male and 17 female patients with a mean age of 41 ± 12 . 7 years ( range , 15 to 67 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Enrolled in the study were N = 49 patients ( 32 women ) aged M = 60 .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Fifty - one patients were enrolled ; 84 % were African American and 80 % were female ( mean age : 54 years ) .

Example answer:
{"entities": [{"text": "African American", "type": "PopulationGroup"}]}

Example input:
Sentence: 41 455 patients ( mean age 72 . 4 years , 47 . 4 % female ) were identified .

Example answer:
{"entities": []}

Example input:
Sentence: A total of 32 women ( 64 % ) and 18 men ( 36 % ) participated in the study with a mean age at baseline of 82 ( range = 65 - 98 ) years .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}, {"text": "study", "type": "ResearchActivity"}]}

Input:
Sentence: Sixty - three participants were enrolled : mean age 70 . 8 years , female 66 . 7 % , past CPR training 60 .

## Item MedMentions:test:1426
Example input:
Sentence: Lowering the overall charge on TMPyP4 improves its selectivity for G - quadruplex DNA Ligands that stabilize non - canonical DNA structures called G - quadruplexes ( GQs ) might have applications in medicine as anti - cancer agents , due to the involvement of GQ DNA in a variety of cancer - related biological processes .

Example answer:
{"entities": [{"text": "TMPyP4", "type": "Chemical"}, {"text": "G - quadruplex DNA", "type": "SpatialConcept"}, {"text": "Ligands", "type": "Chemical"}, {"text": "DNA structures", "type": "Chemical"}, {"text": "G - quadruplexes", "type": "SpatialConcept"}, {"text": "GQs", "type": "SpatialConcept"}, {"text": "medicine", "type": "Chemical"}, {"text": "anti - cancer agents", "type": "Chemical"}, {"text": "GQ DNA", "type": "SpatialConcept"}, {"text": "cancer - related", "type": "Finding"}, {"text": "biological processes", "type": "BiologicFunction"}]}

Example input:
Sentence: A ring - stabilized analog of PhAH , in which the hydroxamic nitrogen is linked to Cα by an ethylene bridge , was predicted to increase binding affinity by stabilizing the inhibitor in a bound conformation .

Example answer:
{"entities": [{"text": "ring - stabilized analog", "type": "Chemical"}, {"text": "PhAH", "type": "Chemical"}, {"text": "stabilizing", "type": "Finding"}, {"text": "bound conformation", "type": "SpatialConcept"}]}

Example input:
Sentence: Performance of ANTI - HCV testing in dried blood spots and saliva according to HIV status The use of saliva and dried blood spots ( DBS ) could increase access to HCV diagnosis for high - risk populations , such as HIV - infected individuals , but the performance of these assays has not been well established in this group .

Example answer:
{"entities": [{"text": "ANTI - HCV testing", "type": "HealthCareActivity"}, {"text": "dried blood spots", "type": "BodySubstance"}, {"text": "saliva", "type": "BodySubstance"}, {"text": "HIV status", "type": "Finding"}, {"text": "DBS", "type": "BodySubstance"}, {"text": "HCV", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "high - risk populations", "type": "PopulationGroup"}, {"text": "HIV - infected", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "assays", "type": "HealthCareActivity"}]}

Example input:
Sentence: The results showed that tQ [ 14 ] displays clear binding affinity for AAs with a positively charged side chain or containing an aromatic ring , but weaker binding affinity for AAs with hydrophobic or polar side chains , with the binding mode depending on the type of side chain present in the AAs .

Example answer:
{"entities": [{"text": "tQ [ 14 ]", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "AAs", "type": "Chemical"}, {"text": "aromatic ring", "type": "Chemical"}]}

Example input:
Sentence: We have discovered electrophilic quinazolines that covalently modify a soluble catalytic subunit of V - ATPase with high potency and exquisite proteomic selectivity as revealed by fluorescence imaging and chemical proteomic activity - based profiling .

Example answer:
{"entities": [{"text": "quinazolines", "type": "Chemical"}, {"text": "covalently modify", "type": "BiologicFunction"}, {"text": "catalytic subunit", "type": "SpatialConcept"}, {"text": "V - ATPase", "type": "Chemical"}, {"text": "fluorescence imaging", "type": "HealthCareActivity"}, {"text": "chemical proteomic activity - based profiling", "type": "HealthCareActivity"}]}

Example input:
Sentence: Neutralizing antibody assay revealed that sera from mice immunized with the VLPs inhibited KSHV infection of HEK - 293 cells in a dose - dependent manner .

Example answer:
{"entities": [{"text": "Neutralizing antibody", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "immunized", "type": "HealthCareActivity"}, {"text": "VLPs", "type": "AnatomicalStructure"}, {"text": "KSHV", "type": "Virus"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "HEK - 293 cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: However , camelid VHH single - domain Abs ( sdAbs or VHHs ) are not bound by SpG and only sporadically bound by SpA .

Example answer:
{"entities": [{"text": "camelid", "type": "Eukaryote"}, {"text": "VHH single - domain Abs", "type": "Chemical"}, {"text": "sdAbs", "type": "Chemical"}, {"text": "VHHs", "type": "Chemical"}, {"text": "SpG", "type": "Chemical"}, {"text": "SpA", "type": "Chemical"}]}

Example input:
Sentence: Here we describe a simple and rapid mutagenesis -based approach designed to confer SpA binding upon a priori non - SpA - binding VHHs .

Example answer:
{"entities": [{"text": "mutagenesis", "type": "HealthCareActivity"}, {"text": "SpA", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "non - SpA - binding VHHs", "type": "Chemical"}]}

Example input:
Sentence: The recombinant hexahistidyl -tagged SGEH was purified ( 16 . 6 - fold ) by immobilized metal - affinity chromatography , with 90 % yield as a homodimer of 100 kDa .

Example answer:
{"entities": [{"text": "recombinant hexahistidyl", "type": "Chemical"}, {"text": "SGEH", "type": "Chemical"}, {"text": "immobilized metal - affinity chromatography", "type": "HealthCareActivity"}]}

Example input:
Sentence: Thus , the SpA binding phenotype of camelid VHHs can be easily modulated to take advantage of tag - less purification techniques , although the frequency with which this is required may depend on the source species .

Example answer:
{"entities": [{"text": "SpA", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "camelid", "type": "Eukaryote"}, {"text": "VHHs", "type": "Chemical"}, {"text": "modulated", "type": "SpatialConcept"}, {"text": "tag - less purification", "type": "HealthCareActivity"}, {"text": "source species", "type": "Finding"}]}

Input:
Sentence: Currently , VHHs require affinity tag - based purification , which limits their therapeutic potential and adds considerable complexity and cost to their production .

## Item MedMentions:test:1602
Example input:
Sentence: 62 ( 95 % CI , 0 . 52 - 0 . 73 ) and 0 . 70 ( 95 % CI , 0 . 50 - 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % ) participants ; the prevalence of unilateral and bilateral MGD was 26 . 3 % ( 95 % CI : 24 . 5 - 28 . 1 ) and 26 .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "MGD", "type": "BiologicFunction"}]}

Example input:
Sentence: Of the 282 responders , 7 . 8 % had a GMFCS level of I , 14 . 2 % II , 17 . 7 % III , 29 . 1 % IV and 31 .

Example answer:
{"entities": [{"text": "responders", "type": "Finding"}, {"text": "GMFCS level", "type": "IntellectualProduct"}]}

Example input:
Sentence: 1 % ) had PMCI , 98 ( 30 . 1 % ) TCI , and 182 ( 55 . 8 % ) NCI .

Example answer:
{"entities": [{"text": "PMCI", "type": "BiologicFunction"}, {"text": "TCI", "type": "BiologicFunction"}, {"text": "NCI", "type": "Finding"}]}

Example input:
Sentence: Similarly , patients carrying the rs2227282 CC genotype demonstrated higher serum IL - 4 levels than those with the GC and GG genotypes ( both P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "rs2227282", "type": "AnatomicalStructure"}, {"text": "serum", "type": "BodySubstance"}, {"text": "IL - 4", "type": "Chemical"}]}

Example input:
Sentence: 50 % ( 95 % CI , 48 . 70 % to 88 . 30 % ) , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 0003 ) , dominant ( OR : 2 . 23 , 95 % CI : 1 . 49 - 3 . 35 , P = 0 . 0001 ) , homozygous ( OR : 3 . 41 , 95 % CI : 1 .

Example answer:
{"entities": []}

Example input:
Sentence: 48 ; 95 % CI 1 . 31 - 4 . 70 ) , and cystic fibrosis ( OR 2 . 17 ; 95 % CI 1 . 16 - 4 . 06 ) .

Example answer:
{"entities": [{"text": "cystic fibrosis", "type": "BiologicFunction"}]}

Example input:
Sentence: 24 , 95 % CI ; 2 . 21 - 4 . 75 ) , diabetes type 2 ( OR 1 . 52 , 95 % CI ; 1 . 01 - 2 , 28 ) , and ischaemic heart disease ( OR 2 .

Example answer:
{"entities": [{"text": "diabetes type 2", "type": "BiologicFunction"}, {"text": "ischaemic heart disease", "type": "BiologicFunction"}]}

Example input:
Sentence: 37 ; 95 % CI , 1 . 12 - 1 . 69 ) in the UK cohort , and with autoimmune polyglandular syndrome type 2 in the Norwegian cohort ( OR , 1 . 58 ; 95 % CI , 1 . 22 - 2 . 06 ) .

Example answer:
{"entities": [{"text": "UK cohort", "type": "PopulationGroup"}, {"text": "autoimmune polyglandular syndrome type 2", "type": "BiologicFunction"}, {"text": "Norwegian cohort", "type": "PopulationGroup"}]}

Input:
Sentence: 53 ; 95 % CI , 1 . 22 - 1 . 92 ) and autoimmune polyglandular syndrome type 2 ( OR , 1 .

## Item MedMentions:test:1407
Example input:
Sentence: Metabolomics , Nutrition , and Potential Biomarkers of Food Quality , Intake , and Health Status Diet , dietary patterns , and other environmental factors such as exposure to toxins are playing an important role in the prevention / development of many diseases , like obesity , type 2 diabetes , and consequently on the health status of individuals .

Example answer:
{"entities": [{"text": "Metabolomics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Nutrition", "type": "Finding"}, {"text": "Biomarkers", "type": "ClinicalAttribute"}, {"text": "Diet", "type": "Food"}, {"text": "dietary patterns", "type": "ResearchActivity"}, {"text": "toxins", "type": "Chemical"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: The goal of this preliminary study was to assess the predictive significance of a panel of molecular biomarkers , related with the response to treatment or drug resistance to NCT , as determined on the diagnostic tumor .

Example answer:
{"entities": [{"text": "molecular biomarkers", "type": "Chemical"}, {"text": "response to treatment", "type": "ClinicalAttribute"}, {"text": "drug resistance", "type": "BiologicFunction"}, {"text": "tumor", "type": "BiologicFunction"}]}

Example input:
Sentence: Future biomonitoring studies will need to consider the high variability of individual exposure profiles in relation to multiple exposure sources but also physiological and metabolic differences .

Example answer:
{"entities": [{"text": "biomonitoring studies", "type": "ResearchActivity"}, {"text": "individual", "type": "PopulationGroup"}, {"text": "profiles", "type": "HealthCareActivity"}, {"text": "sources", "type": "Finding"}]}

Example input:
Sentence: It might thus be of particular interest to monitor children with high levels of these biomarkers , as part of a longitudinal study in order to determine if the excretion profile at a young age is predictive of the outcomes of disease severity in adulthood .

Example answer:
{"entities": [{"text": "interest", "type": "BiologicFunction"}, {"text": "monitor", "type": "HealthCareActivity"}, {"text": "biomarkers", "type": "ClinicalAttribute"}, {"text": "longitudinal study", "type": "ResearchActivity"}, {"text": "excretion", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: While advances in the understanding of the role of microbiota in other areas of human health have yielded intriguing results ( e . g . , Clostridium difficile , irritable bowel syndrome , autism , etc . ) , to date , no systematic programs of research have examined the role of microbiota in drug addiction .

Example answer:
{"entities": [{"text": "understanding", "type": "BiologicFunction"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "human", "type": "Eukaryote"}, {"text": "Clostridium difficile", "type": "BiologicFunction"}, {"text": "irritable bowel syndrome", "type": "BiologicFunction"}, {"text": "autism", "type": "BiologicFunction"}, {"text": "research", "type": "ResearchActivity"}, {"text": "examined", "type": "Finding"}, {"text": "drug addiction", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , metabolomic investigations have been carried out to discover new early biomarkers of metabolic dysfunction and predictive biomarkers of developing pathologies ( obesity , metabolic syndrome , type - 2 diabetes , etc . ) .

Example answer:
{"entities": [{"text": "metabolomic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "biomarkers", "type": "ClinicalAttribute"}, {"text": "pathologies", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "metabolic syndrome", "type": "BiologicFunction"}, {"text": "type - 2 diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: The faecal microbiome may provide non - invasive biomarkers of CRC and indicate transition in the adenoma - carcinoma sequence .

Example answer:
{"entities": [{"text": "faecal", "type": "BodySubstance"}, {"text": "biomarkers", "type": "ClinicalAttribute"}, {"text": "CRC", "type": "BiologicFunction"}, {"text": "transition", "type": "BiologicFunction"}, {"text": "adenoma - carcinoma", "type": "BiologicFunction"}, {"text": "sequence", "type": "SpatialConcept"}]}

Example input:
Sentence: A fast small - sample kernel independence test for microbiome community - level association analysis To fully understand the role of microbiome in human health and diseases , researchers are increasingly interested in assessing the relationship between microbiome composition and host genomic data .

Example answer:
{"entities": [{"text": "fast small - sample kernel independence test", "type": "IntellectualProduct"}, {"text": "level association analysis", "type": "ResearchActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "researchers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "genomic", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Forthcoming studies that integrate metabolomics with genomic , microbiome and physiological parameters may facilitate a broader systems - level understanding and mechanistic insights into these integrative practices that are employed to promote health and well - being .

Example answer:
{"entities": [{"text": "metabolomics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "genomic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "parameters", "type": "Finding"}]}

Example input:
Sentence: In conclusion , finding biomarkers of chemoresitance ( ypTNM II - III ) and metastases can become a stepping stone for future studies that will need to be assessed in a bigger scale .

Example answer:
{"entities": [{"text": "finding", "type": "Finding"}, {"text": "biomarkers", "type": "Chemical"}, {"text": "ypTNM II - III", "type": "IntellectualProduct"}, {"text": "metastases", "type": "BiologicFunction"}]}

Input:
Sentence: Future studies will investigate the microbiome composition and functional capabilities in more patients while tracing some potential biomarker taxa

## Item MedMentions:test:1644
Example input:
Sentence: nigrinus was 7 wk beginning 22 October 2010 , and the longest emergence was 15 wk beginning 17 October 2012 .

Example answer:
{"entities": [{"text": "nigrinus", "type": "Eukaryote"}]}

Example input:
Sentence: The cohort consisted of 15 857 dabigatran ( age 80 . 7±6 .

Example answer:
{"entities": [{"text": "cohort", "type": "PopulationGroup"}, {"text": "dabigatran", "type": "Chemical"}]}

Example input:
Sentence: 6 years ( range , 38 - 97 years ) .

Example answer:
{"entities": []}

Example input:
Sentence: 2139 . 5 person - years , with a maximum of 6 . 66 years follow - up time .

Example answer:
{"entities": [{"text": "person", "type": "PopulationGroup"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Overall survival and disease - free survival at 60 months are 48 . 8 % and 45 . 8 % , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 5 % , respectively , the median progression - free and overall survival ( OS ) were 19 and 45 months , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 8±6 . 1 years ( 0 . 1 - 25 .

Example answer:
{"entities": []}

Example input:
Sentence: 31 ± 23 . 86 years , ranging from 22 to 102 years .

Example answer:
{"entities": []}

Example input:
Sentence: C . elegans , a worm model popularly used in molecular and developmental biology , was used in the present study .

Example answer:
{"entities": [{"text": "C . elegans", "type": "Eukaryote"}, {"text": "worm", "type": "Eukaryote"}, {"text": "molecular", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "present study", "type": "ResearchActivity"}]}

Example input:
Sentence: elegans postembryonic intestinal development .

Example answer:
{"entities": [{"text": "elegans", "type": "Eukaryote"}, {"text": "postembryonic intestinal development", "type": "BiologicFunction"}]}

Input:
Sentence: elegans life by 26 .

## Item MedMentions:test:839
Example input:
Sentence: Cortical - ventral striatum ( VS ) circuitry is a common target of psychobehavioral interventions in drug addiction , and cortical - VS dysfunction has been reported in IGD ; hence , the primary aim of the study was to investigate how the VS circuitry responds to psychobehavioral interventions in IGD .

Example answer:
{"entities": [{"text": "Cortical", "type": "SpatialConcept"}, {"text": "ventral striatum", "type": "AnatomicalStructure"}, {"text": "VS", "type": "AnatomicalStructure"}, {"text": "psychobehavioral interventions", "type": "HealthCareActivity"}, {"text": "drug addiction", "type": "BiologicFunction"}, {"text": "cortical", "type": "SpatialConcept"}, {"text": "IGD", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: The anxiety group had lower activation of the ventromedial prefrontal cortex ( vmPFC ) during extinction recall ( ηp2 = 0 . 178 , P = .02 ) .

Example answer:
{"entities": [{"text": "anxiety", "type": "Finding"}, {"text": "group", "type": "PopulationGroup"}, {"text": "ventromedial prefrontal cortex", "type": "AnatomicalStructure"}, {"text": "vmPFC", "type": "AnatomicalStructure"}, {"text": "extinction", "type": "BiologicFunction"}, {"text": "recall", "type": "BiologicFunction"}]}

Example input:
Sentence: Emotional arousal state influences the ability of amygdalar endocannabinoid signaling to modulate anxiety Systemic activation of cannabinoid receptors often induces biphasic effects on emotional memory and anxiety depending on the levels of emotional arousal associated to the experimental context .

Example answer:
{"entities": [{"text": "Emotional", "type": "BiologicFunction"}, {"text": "arousal state", "type": "BiologicFunction"}, {"text": "amygdalar", "type": "AnatomicalStructure"}, {"text": "endocannabinoid signaling", "type": "BiologicFunction"}, {"text": "anxiety", "type": "Finding"}, {"text": "Systemic activation", "type": "BiologicFunction"}, {"text": "cannabinoid receptors", "type": "Chemical"}, {"text": "emotional", "type": "BiologicFunction"}, {"text": "memory", "type": "BiologicFunction"}, {"text": "arousal", "type": "BiologicFunction"}]}

Example input:
Sentence: This effect could be related to inhibited cocaine - and amphetamine - regulated transcript ( CART ) gene expression and serotonin ( 5 - hydroxytryptamine , 5 - HT ) synthesis and release , and increased orexin A gene expression in the hypothalamus .

Example answer:
{"entities": [{"text": "cocaine - and amphetamine - regulated transcript", "type": "AnatomicalStructure"}, {"text": "CART", "type": "AnatomicalStructure"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "serotonin", "type": "Chemical"}, {"text": "5 - hydroxytryptamine", "type": "Chemical"}, {"text": "5 - HT", "type": "Chemical"}, {"text": "synthesis", "type": "BiologicFunction"}, {"text": "orexin A", "type": "Chemical"}, {"text": "hypothalamus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Male rats received amphetamine or saline for two weeks followed by 24 hours or two weeks of withdrawal , with transporter expression measured using Western immunoblot .

Example answer:
{"entities": [{"text": "rats", "type": "Eukaryote"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "withdrawal", "type": "BiologicFunction"}, {"text": "transporter", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Western immunoblot", "type": "HealthCareActivity"}]}

Example input:
Sentence: It is the default , unlearned response to prolonged aversive events and it is mediated by the serotonergic activity of the dorsal raphe nucleus , which in turn inhibits escape .

Example answer:
{"entities": [{"text": "serotonergic activity", "type": "BiologicFunction"}, {"text": "dorsal raphe nucleus", "type": "AnatomicalStructure"}, {"text": "escape", "type": "BiologicFunction"}]}

Example input:
Sentence: Somatosensory regulation of serotonin release in the central nucleus of the amygdala is mediated via corticotropin releasing factor and gamma - aminobutyric acid in the dorsal raphe nucleus Noxious cutaneous stimulation increases , whereas innocuous cutaneous stimulation decreases serotonin ( 5 - HT ) release in the central nucleus of the amygdala ( CeA ) in anesthetized rats .

Example answer:
{"entities": [{"text": "Somatosensory", "type": "AnatomicalStructure"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "serotonin release", "type": "BiologicFunction"}, {"text": "central nucleus of the amygdala", "type": "AnatomicalStructure"}, {"text": "corticotropin releasing factor", "type": "Chemical"}, {"text": "gamma - aminobutyric acid", "type": "Chemical"}, {"text": "dorsal raphe nucleus", "type": "AnatomicalStructure"}, {"text": "Noxious cutaneous stimulation", "type": "HealthCareActivity"}, {"text": "innocuous cutaneous stimulation", "type": "HealthCareActivity"}, {"text": "serotonin ( 5 - HT ) release", "type": "BiologicFunction"}, {"text": "CeA", "type": "AnatomicalStructure"}, {"text": "anesthetized", "type": "Finding"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: In the vHipp , OCT3 expression increased only at 24 hours of withdrawal , with an equivalent pattern seen in the dorsomedial hypothalamus .

Example answer:
{"entities": [{"text": "vHipp", "type": "AnatomicalStructure"}, {"text": "OCT3", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "withdrawal", "type": "BiologicFunction"}, {"text": "dorsomedial hypothalamus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: These regionally specific changes in limbic OCT3 and SERT expression may partially contribute to the serotonergic imbalance and negative affect during amphetamine withdrawal .

Example answer:
{"entities": [{"text": "limbic", "type": "BodySystem"}, {"text": "OCT3", "type": "Chemical"}, {"text": "SERT", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "serotonergic", "type": "Chemical"}, {"text": "imbalance", "type": "Finding"}, {"text": "negative affect", "type": "Finding"}, {"text": "amphetamine withdrawal", "type": "BiologicFunction"}]}

Example input:
Sentence: Extracellular serotonin levels are regulated by the serotonin transporter ( SERT ) and organic cation transporter 3 ( OCT3 ) , and vHipp OCT3 expression is enhanced during 24 hours of amphetamine withdrawal , while SERT expression is unaltered .

Example answer:
{"entities": [{"text": "Extracellular", "type": "AnatomicalStructure"}, {"text": "serotonin", "type": "Chemical"}, {"text": "serotonin transporter", "type": "Chemical"}, {"text": "SERT", "type": "Chemical"}, {"text": "organic cation transporter 3", "type": "Chemical"}, {"text": "OCT3", "type": "Chemical"}, {"text": "vHipp", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "amphetamine withdrawal", "type": "BiologicFunction"}]}

Input:
Sentence: Amphetamine Withdrawal Differentially Increases the Expression of Organic Cation Transporter 3 and Serotonin Transporter in Limbic Brain Regions Amphetamine withdrawal increases anxiety and stress sensitivity related to blunted ventral hippocampus ( vHipp ) and enhances the central nucleus of the amygdala ( CeA ) serotonin responses .

## Item MedMentions:test:1459
Example input:
Sentence: In the absence of a clear history of type - I allergic reaction ( e . g . urticaria , anaphylaxis , or bronchospasm ) , we suggest the use of a third - generation cephalosporin instead of clindamycin as perioperative prophylaxis when undergoing a TKR .

Example answer:
{"entities": [{"text": "type - I allergic reaction", "type": "BiologicFunction"}, {"text": "urticaria", "type": "BiologicFunction"}, {"text": "anaphylaxis", "type": "BiologicFunction"}, {"text": "bronchospasm", "type": "BiologicFunction"}, {"text": "third - generation cephalosporin", "type": "Chemical"}, {"text": "clindamycin", "type": "Chemical"}, {"text": "prophylaxis", "type": "HealthCareActivity"}, {"text": "TKR", "type": "HealthCareActivity"}]}

Example input:
Sentence: Although life " on the list " could be stressful , and immunosuppressant side effects were severe , interviewees reported " no regrets . " Posttransplant , interviewees experienced increased confidence , through freedom from hypoglycemia and regained glycemic control , which tempered any disappointment about continued reliance on insulin .

Example answer:
{"entities": [{"text": "immunosuppressant", "type": "Chemical"}, {"text": "side effects", "type": "BiologicFunction"}, {"text": "interviewees", "type": "PopulationGroup"}, {"text": "no", "type": "Finding"}, {"text": "regrets", "type": "BiologicFunction"}, {"text": "confidence", "type": "BiologicFunction"}, {"text": "freedom from hypoglycemia", "type": "Finding"}, {"text": "glycemic control", "type": "HealthCareActivity"}, {"text": "insulin", "type": "Chemical"}]}

Example input:
Sentence: We performed temporary test clamping of the SRS before direct ligation and applied PV pressure monitoring in patients who showed signs of portal hypertension , such as bowel edema .

Example answer:
{"entities": [{"text": "temporary test", "type": "HealthCareActivity"}, {"text": "clamping", "type": "HealthCareActivity"}, {"text": "SRS", "type": "MedicalDevice"}, {"text": "direct ligation", "type": "HealthCareActivity"}, {"text": "PV", "type": "AnatomicalStructure"}, {"text": "pressure", "type": "BiologicFunction"}, {"text": "monitoring", "type": "ResearchActivity"}, {"text": "portal hypertension", "type": "BiologicFunction"}, {"text": "bowel edema", "type": "Finding"}]}

Example input:
Sentence: Our results suggest comparable patient and allograft outcomes in KTRs after SOT and primary KTRs .

Example answer:
{"entities": [{"text": "allograft", "type": "HealthCareActivity"}, {"text": "KTRs", "type": "Finding"}, {"text": "SOT", "type": "HealthCareActivity"}]}

Example input:
Sentence: We studied 40 KTRs after nonrenal SOT .

Example answer:
{"entities": [{"text": "studied", "type": "ResearchActivity"}, {"text": "KTRs", "type": "Finding"}, {"text": "nonrenal SOT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Kidney transplant recipients after nonrenal solid organ transplantation show low alloreactivity but an increased risk of infection The number of kidney transplant recipients ( KTRs ) after nonrenal solid organ transplantation ( SOT ) has increased to almost 5 % .

Example answer:
{"entities": [{"text": "Kidney transplant recipients", "type": "Finding"}, {"text": "nonrenal solid organ transplantation", "type": "HealthCareActivity"}, {"text": "alloreactivity", "type": "BiologicFunction"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "kidney transplant recipients", "type": "Finding"}, {"text": "KTRs", "type": "Finding"}, {"text": "SOT", "type": "HealthCareActivity"}]}

Example input:
Sentence: While death -censored allograft survival was comparable between KTRs after SOT and primary KTRs , KTRs after SOT showed superior 5 - year death -censored allograft survival of 92 .

Example answer:
{"entities": [{"text": "death", "type": "BiologicFunction"}, {"text": "allograft", "type": "HealthCareActivity"}, {"text": "KTRs", "type": "Finding"}, {"text": "SOT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patient survival in KTRs after SOT , primary and repeat KTRs was comparable .

Example answer:
{"entities": [{"text": "KTRs", "type": "Finding"}, {"text": "SOT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Interestingly , KTRs after SOT show less preformed panel - reactive antibodies , frequencies of alloreactive T cells , and acute rejections compared to repeat KTRs .

Example answer:
{"entities": [{"text": "KTRs", "type": "Finding"}, {"text": "SOT", "type": "HealthCareActivity"}, {"text": "panel - reactive antibodies", "type": "HealthCareActivity"}, {"text": "alloreactive", "type": "BiologicFunction"}, {"text": "T cells", "type": "AnatomicalStructure"}, {"text": "acute rejections", "type": "Finding"}]}

Example input:
Sentence: KTRs after SOT , however , show higher incidences of EBV viremia and PTLD , sepsis , and death from sepsis .

Example answer:
{"entities": [{"text": "KTRs", "type": "Finding"}, {"text": "SOT", "type": "HealthCareActivity"}, {"text": "EBV viremia", "type": "BiologicFunction"}, {"text": "PTLD", "type": "BiologicFunction"}, {"text": "sepsis", "type": "BiologicFunction"}, {"text": "death", "type": "BiologicFunction"}]}

Input:
Sentence: Caution should be taken in KTRs after SOT regarding infectious complications due to overimmunosuppression .

## Item MedMentions:test:1410
Example input:
Sentence: Statistically significant associations were found between HERG1 expression and tobacco consumption , disease stage , tumor differentiation , tumor recurrence , and reduced survival .

Example answer:
{"entities": [{"text": "HERG1", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "differentiation", "type": "BiologicFunction"}, {"text": "tumor recurrence", "type": "BiologicFunction"}]}

Example input:
Sentence: EGFR protein expression in lung cancer tissue was measured by immunohistochemistry with a specific antibody that recognizes the intracellular domain ( ID ) of EGFR .

Example answer:
{"entities": [{"text": "EGFR protein", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "immunohistochemistry", "type": "HealthCareActivity"}, {"text": "antibody", "type": "Chemical"}, {"text": "recognizes", "type": "BiologicFunction"}, {"text": "intracellular", "type": "SpatialConcept"}, {"text": "domain", "type": "SpatialConcept"}, {"text": "ID", "type": "SpatialConcept"}, {"text": "EGFR", "type": "Chemical"}]}

Example input:
Sentence: Spearman correlation analysis showed that the expression of TCRP1 has a positive correlation with p - PDK1 , as well as p - AKT1 in lung cancer and gliomas tissues .

Example answer:
{"entities": [{"text": "Spearman correlation analysis", "type": "ResearchActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "TCRP1", "type": "Chemical"}, {"text": "p - PDK1", "type": "Chemical"}, {"text": "p - AKT1", "type": "Chemical"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "gliomas", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Additionally , decreased expression of Drp1 via siRNA knockdown during LG conditions also improved vascular relaxation .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "Drp1", "type": "Chemical"}, {"text": "siRNA", "type": "Chemical"}, {"text": "knockdown", "type": "ResearchActivity"}, {"text": "LG", "type": "Chemical"}, {"text": "improved", "type": "Finding"}, {"text": "vascular relaxation", "type": "BiologicFunction"}]}

Example input:
Sentence: The mean serum DR - 70 levels in lung cancer patients ( 2 . 43 ± 1 . 82 µg / mL ) was significantly higher compared to the 86 non - cancerous subjects ( 1 . 15 ± 0 . 70 µg / mL ) ( p < 0 .

Example answer:
{"entities": [{"text": "mean serum DR - 70", "type": "Chemical"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "significantly higher", "type": "Finding"}, {"text": "non - cancerous", "type": "Finding"}, {"text": "subjects", "type": "PopulationGroup"}]}

Example input:
Sentence: Mechanistic analyses confirm that DRG1 localizes at mitotic spindles in dividing cells and binds to spindle checkpoint signaling proteins in vivo .

Example answer:
{"entities": [{"text": "analyses", "type": "ResearchActivity"}, {"text": "DRG1", "type": "Chemical"}, {"text": "localizes", "type": "SpatialConcept"}, {"text": "mitotic spindles", "type": "AnatomicalStructure"}, {"text": "dividing cells", "type": "AnatomicalStructure"}, {"text": "binds", "type": "BiologicFunction"}, {"text": "spindle checkpoint signaling", "type": "BiologicFunction"}, {"text": "proteins", "type": "Chemical"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: However , the molecular basis of DRG1 in cell proliferation regulation and the relationship between DRG1 and tumor progression remain poorly understood .

Example answer:
{"entities": [{"text": "DRG1", "type": "Chemical"}, {"text": "cell proliferation regulation", "type": "BiologicFunction"}, {"text": "tumor progression", "type": "BiologicFunction"}]}

Example input:
Sentence: Overexpression of DRG1 leads to chromosome missegregation which is an important index for tumorigenesis .

Example answer:
{"entities": [{"text": "Overexpression", "type": "BiologicFunction"}, {"text": "DRG1", "type": "Chemical"}, {"text": "chromosome", "type": "AnatomicalStructure"}, {"text": "missegregation", "type": "BiologicFunction"}, {"text": "tumorigenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: These studies highlight the expanding role of DRG1 in tumorigenesis and reveal a mechanism of DRG1 in taxol resistance .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "DRG1", "type": "AnatomicalStructure"}, {"text": "tumorigenesis", "type": "BiologicFunction"}, {"text": "taxol", "type": "Chemical"}]}

Example input:
Sentence: DRG1 is a potential oncogene in lung adenocarcinoma and promotes tumor progression via spindle checkpoint signaling regulation Developmentally regulated GTP binding protein 1 ( DRG1 ) , a member of the DRG family , plays important roles in regulating cell growth .

Example answer:
{"entities": [{"text": "DRG1", "type": "AnatomicalStructure"}, {"text": "oncogene", "type": "AnatomicalStructure"}, {"text": "lung adenocarcinoma", "type": "BiologicFunction"}, {"text": "tumor progression", "type": "BiologicFunction"}, {"text": "spindle checkpoint signaling", "type": "BiologicFunction"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "GTP binding protein 1", "type": "Chemical"}, {"text": "DRG1", "type": "Chemical"}, {"text": "DRG family", "type": "Chemical"}, {"text": "regulating cell growth", "type": "BiologicFunction"}]}

Input:
Sentence: Here , we demonstrate that DRG1 is elevated in lung adenocarcinomas while weakly expressed in adjacent lung tissues .

## Item MedMentions:test:1600
Example input:
Sentence: The use of structural allograft was most popular among the experts for anterior reconstruction , followed by cage reconstruction , and PMMA bone cement .

Example answer:
{"entities": [{"text": "experts", "type": "ProfessionalOrOccupationalGroup"}, {"text": "anterior", "type": "SpatialConcept"}, {"text": "reconstruction", "type": "HealthCareActivity"}, {"text": "cage", "type": "MedicalDevice"}, {"text": "PMMA", "type": "Chemical"}, {"text": "bone cement", "type": "Chemical"}]}

Example input:
Sentence: After a first reconstruction attempt with an iliac crest graft failed , definitive reconstruction of his mandible with a microvascular anastomosed fibula graft was achieved .

Example answer:
{"entities": [{"text": "reconstruction", "type": "HealthCareActivity"}, {"text": "iliac crest", "type": "AnatomicalStructure"}, {"text": "graft", "type": "AnatomicalStructure"}, {"text": "definitive reconstruction of his mandible", "type": "HealthCareActivity"}, {"text": "microvascular anastomosed fibula graft", "type": "HealthCareActivity"}]}

Example input:
Sentence: New bone forms along outer surfaces of β - TCMP scaffolds after implantation in rabbit femoral defects for one month and grows into the majority of the inner open - cell spaces postoperation in three month s , showing tight interface between the scaffold and regenerative bone tissue .

Example answer:
{"entities": [{"text": "bone", "type": "AnatomicalStructure"}, {"text": "surfaces", "type": "SpatialConcept"}, {"text": "β - TCMP scaffolds", "type": "Chemical"}, {"text": "implantation", "type": "HealthCareActivity"}, {"text": "rabbit", "type": "Eukaryote"}, {"text": "femoral defects", "type": "InjuryOrPoisoning"}, {"text": "grows", "type": "BiologicFunction"}, {"text": "open - cell spaces", "type": "SpatialConcept"}, {"text": "scaffold", "type": "Chemical"}, {"text": "regenerative bone tissue", "type": "BiologicFunction"}]}

Example input:
Sentence: There were 17 studies that described the use of a prefabricated prosthetic , 10 studies describing the use of polymethyl methacrylate ( PMMA ) bone cement , and only three studies describing the use of bone graft for anterior column reconstruction .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "prefabricated prosthetic", "type": "MedicalDevice"}, {"text": "polymethyl methacrylate", "type": "Chemical"}, {"text": "PMMA", "type": "Chemical"}, {"text": "bone cement", "type": "Chemical"}, {"text": "bone graft", "type": "HealthCareActivity"}, {"text": "anterior", "type": "SpatialConcept"}, {"text": "column", "type": "AnatomicalStructure"}, {"text": "reconstruction", "type": "HealthCareActivity"}]}

Example input:
Sentence: The main outcome was a bone healing complication as evidenced by nonunion , delayed union , or re - displacement on follow - up radiographs .

Example answer:
{"entities": [{"text": "bone healing", "type": "Finding"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "nonunion", "type": "Finding"}, {"text": "delayed union", "type": "BiologicFunction"}, {"text": "re - displacement", "type": "HealthCareActivity"}, {"text": "radiographs", "type": "HealthCareActivity"}]}

Example input:
Sentence: An absorbable mesh plate made into a clip was used for fixation after open reduction via the endonasal approach .

Example answer:
{"entities": [{"text": "mesh plate", "type": "MedicalDevice"}, {"text": "clip", "type": "MedicalDevice"}, {"text": "fixation", "type": "HealthCareActivity"}, {"text": "open reduction", "type": "HealthCareActivity"}, {"text": "endonasal", "type": "SpatialConcept"}, {"text": "approach", "type": "SpatialConcept"}]}

Example input:
Sentence: Revision surgery was required for periprosthetic femoral fracture in one patient .

Example answer:
{"entities": [{"text": "Revision surgery", "type": "HealthCareActivity"}, {"text": "periprosthetic", "type": "InjuryOrPoisoning"}, {"text": "femoral fracture", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Surgical Excision of Heterotopic Ossification Leads to Re - Emergence of Mesenchymal Stem Cell Populations Responsible for Recurrence Trauma - induced heterotopic ossification ( HO ) occurs after severe musculoskeletal injuries and burns , and presents a significant barrier to patient rehabilitation .

Example answer:
{"entities": [{"text": "Surgical Excision", "type": "HealthCareActivity"}, {"text": "Heterotopic Ossification", "type": "BiologicFunction"}, {"text": "Mesenchymal Stem Cell Populations", "type": "AnatomicalStructure"}, {"text": "heterotopic ossification", "type": "BiologicFunction"}, {"text": "HO", "type": "BiologicFunction"}, {"text": "musculoskeletal injuries", "type": "InjuryOrPoisoning"}, {"text": "burns", "type": "InjuryOrPoisoning"}, {"text": "rehabilitation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Specifically two aspects of surgical reconstruction are addressed in this study : ( i ) choice of bone graft used during surgery for metastatic spine tumors and ( ii ) the design of reconstruction or construct to stabilize .

Example answer:
{"entities": [{"text": "surgical reconstruction", "type": "HealthCareActivity"}, {"text": "bone graft", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "metastatic spine tumors", "type": "BiologicFunction"}, {"text": "reconstruction", "type": "HealthCareActivity"}, {"text": "construct", "type": "Chemical"}, {"text": "stabilize", "type": "Finding"}]}

Example input:
Sentence: When we first saw him , his reconstruction plate was partially exposed with intraoral and extraoral fistulation .

Example answer:
{"entities": [{"text": "reconstruction", "type": "HealthCareActivity"}, {"text": "plate", "type": "MedicalDevice"}, {"text": "intraoral", "type": "SpatialConcept"}, {"text": "extraoral", "type": "SpatialConcept"}, {"text": "fistulation", "type": "AnatomicalStructure"}]}

Input:
Sentence: Subsequent osteosynthesis was performed with a reconstruction plate .

## Item MedMentions:test:1590
Example input:
Sentence: The NEUROD2 exonic polymorphism rs11078918 showed significant associations with verbal memory and executive functions , whereas the NEUROD2 polymorphism rs12453682 was significantly associated with working and verbal memory , executive functions and with a cognitive index .

Example answer:
{"entities": [{"text": "NEUROD2", "type": "AnatomicalStructure"}, {"text": "verbal memory", "type": "BiologicFunction"}, {"text": "executive functions", "type": "BiologicFunction"}, {"text": "index", "type": "IntellectualProduct"}]}

Example input:
Sentence: The assessment included the Motor Severity Stereotypy Scale ( MSSS ) , the Repetitive Behavior Scale - Revised ( RBS - R ) , the Raven 's Colored Progressive Matrices , the Child Behavior CheckList for ages 1½ - 5 or 4 - 18 ( CBCL ) , the Social Responsiveness Scale ( SRS ) , and the Autism Diagnostic Observation Schedule - second edition ( ADOS 2 ) .

Example answer:
{"entities": [{"text": "assessment", "type": "HealthCareActivity"}, {"text": "Motor Severity Stereotypy Scale", "type": "IntellectualProduct"}, {"text": "MSSS", "type": "IntellectualProduct"}, {"text": "Repetitive Behavior Scale - Revised", "type": "IntellectualProduct"}, {"text": "RBS - R", "type": "IntellectualProduct"}, {"text": "Raven 's Colored Progressive Matrices", "type": "Finding"}, {"text": "Social Responsiveness Scale", "type": "IntellectualProduct"}, {"text": "( SRS )", "type": "IntellectualProduct"}, {"text": "Autism Diagnostic Observation Schedule - second edition", "type": "IntellectualProduct"}, {"text": "ADOS 2", "type": "IntellectualProduct"}]}

Example input:
Sentence: The Edinburgh Postnatal Depression Scale ( EPDS ) , State - Trait Anxiety Inventory ( STAI ) , and Parenting Stress Index - Short Form ( PSI - SF ) were administered to the mothers to assess depression , anxiety , and parenting stress , respectively .

Example answer:
{"entities": [{"text": "Edinburgh Postnatal Depression Scale", "type": "IntellectualProduct"}, {"text": "EPDS", "type": "IntellectualProduct"}, {"text": "State - Trait Anxiety Inventory", "type": "HealthCareActivity"}, {"text": "STAI", "type": "HealthCareActivity"}, {"text": "Parenting Stress Index - Short Form", "type": "IntellectualProduct"}, {"text": "PSI - SF", "type": "IntellectualProduct"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "parenting stress", "type": "BiologicFunction"}]}

Example input:
Sentence: Low birth weight and features of neuroticism and mood disorder in 83 545 participants of the UK Biobank cohort Low birth weight has been inconsistently associated with risk of developing affective disorders , including major depressive disorder ( MDD ) .

Example answer:
{"entities": [{"text": "Low birth weight", "type": "Finding"}, {"text": "neuroticism", "type": "BiologicFunction"}, {"text": "mood disorder", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "UK", "type": "SpatialConcept"}, {"text": "Biobank", "type": "Organization"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "affective disorders", "type": "BiologicFunction"}, {"text": "major depressive disorder", "type": "BiologicFunction"}, {"text": "MDD", "type": "BiologicFunction"}]}

Example input:
Sentence: Fatigue severity 3 months after stroke positively correlated with Geriatric Depression Scale and NEO Five - Factor Inventory neuroticism scores and negatively correlated with the Barthel Index score .

Example answer:
{"entities": [{"text": "Fatigue severity", "type": "IntellectualProduct"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "Geriatric Depression Scale", "type": "IntellectualProduct"}, {"text": "NEO Five - Factor Inventory", "type": "HealthCareActivity"}, {"text": "neuroticism", "type": "BiologicFunction"}, {"text": "negatively", "type": "Finding"}]}

Example input:
Sentence: Neuroticism , independent of depressive symptoms , is a predictor of fatigue severity 3 months after stroke .

Example answer:
{"entities": [{"text": "Neuroticism", "type": "BiologicFunction"}, {"text": "independent", "type": "Finding"}, {"text": "depressive symptoms", "type": "Finding"}, {"text": "fatigue severity", "type": "IntellectualProduct"}, {"text": "stroke", "type": "BiologicFunction"}]}

Example input:
Sentence: Current symptoms were assessed using the Positive and Negative Symptom Scale and neurocognitive functions using Cognitrax , which yields a composite neurocognitive index ( NCI ) and 11 domain scores .

Example answer:
{"entities": [{"text": "symptoms", "type": "Finding"}, {"text": "Positive", "type": "Finding"}, {"text": "Negative", "type": "Finding"}, {"text": "Symptom Scale", "type": "IntellectualProduct"}, {"text": "neurocognitive functions", "type": "BiologicFunction"}]}

Example input:
Sentence: To assess whether very low birth weight ( < 1500 g ) and low birth weight ( 1500 - 2490 g ) were associated with higher neuroticism scores assessed in middle age , and lifetime history of either MDD or BD .

Example answer:
{"entities": [{"text": "very low birth weight", "type": "Finding"}, {"text": "low birth weight", "type": "Finding"}, {"text": "higher neuroticism", "type": "Finding"}, {"text": "MDD", "type": "BiologicFunction"}, {"text": "BD", "type": "BiologicFunction"}]}

Example input:
Sentence: As well as several key demographics , trait negative affect , mindfulness , self - efficacy , coping , resilience , and burnout were measured .

Example answer:
{"entities": [{"text": "trait negative affect", "type": "Finding"}, {"text": "mindfulness", "type": "BiologicFunction"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "burnout", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , as predicted , Neuroticism moderated the relationship between coping and burnout .

Example answer:
{"entities": [{"text": "Neuroticism", "type": "BiologicFunction"}, {"text": "burnout", "type": "BiologicFunction"}]}

Input:
Sentence: The personality trait of neuroticism was measured with the neuroticism subscale of the Chinese version of the NEO Five - Factor Inventory .

## Item MedMentions:test:1596
Example input:
Sentence: Animals were killed in equal numbers at 72 hours , two weeks , eight weeks , and 24 weeks .

Example answer:
{"entities": [{"text": "Animals", "type": "Eukaryote"}]}

Example input:
Sentence: Animals underwent necropsy with blinded histomorphologic evaluation on days 0 , 3 , and 10 postprocedure to assess for presence of bowel perforation , depth of thermal injury , and extent of inflammatory response .

Example answer:
{"entities": [{"text": "Animals", "type": "Eukaryote"}, {"text": "necropsy", "type": "HealthCareActivity"}, {"text": "blinded", "type": "ResearchActivity"}, {"text": "histomorphologic evaluation", "type": "HealthCareActivity"}, {"text": "postprocedure to assess", "type": "Finding"}, {"text": "bowel perforation", "type": "BiologicFunction"}, {"text": "thermal injury", "type": "InjuryOrPoisoning"}, {"text": "inflammatory response", "type": "BiologicFunction"}]}

Example input:
Sentence: The purpose of this study was to establish level of LD 70 / 30 ( a lethal dose for 70 % of mice within 30 days ) by total - body γ irradiation ( TBI ) in a mouse model .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "mice", "type": "Eukaryote"}, {"text": "total - body γ irradiation", "type": "HealthCareActivity"}, {"text": "TBI", "type": "HealthCareActivity"}, {"text": "mouse model", "type": "BiologicFunction"}]}

Example input:
Sentence: Sheep were humanely euthanized and necropsized at 8 weeks post - infection ( the early stage of cyst established ) .

Example answer:
{"entities": [{"text": "Sheep", "type": "Eukaryote"}, {"text": "humanely euthanized", "type": "HealthCareActivity"}, {"text": "necropsized", "type": "HealthCareActivity"}, {"text": "infection", "type": "BiologicFunction"}]}

Example input:
Sentence: At the end of 4 weeks , rats were sacrificed under high - dose ketamine anesthesia .

Example answer:
{"entities": [{"text": "rats", "type": "Eukaryote"}, {"text": "ketamine", "type": "Chemical"}, {"text": "anesthesia", "type": "Chemical"}]}

Example input:
Sentence: Five weeks after insertion of tube , the mice were sacrificed .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Animals were euthanized on PN90 and lungs were harvested for histological and molecular characterization .

Example answer:
{"entities": [{"text": "Animals", "type": "Eukaryote"}, {"text": "euthanized", "type": "HealthCareActivity"}, {"text": "lungs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: At 4 weeks and 8 weeks after implantation , animals were euthanized , respectively .

Example answer:
{"entities": [{"text": "implantation", "type": "HealthCareActivity"}, {"text": "animals", "type": "Eukaryote"}]}

Example input:
Sentence: The rats were sacrificed on gestational day 15 and postnatal day 7 .

Example answer:
{"entities": [{"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: They were sacrificed at week 20 to evaluate their colorectum histopathologically .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "colorectum", "type": "AnatomicalStructure"}]}

Input:
Sentence: The animals were sacrificed at 32 weeks following thoracic irradiation .

## Item MedMentions:test:1613
Example input:
Sentence: 44 95 % CI 1 . 8 to 10 . 92 , P = 0 . 0004 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 001 ; 95 % CI 0 . 18 ; 0 . 38 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 48 , 95 % CI 1 . 24 - 1 . 75 , P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 00 , 95 % CI 1 . 55 - 2 . 57 and OR = 1 . 33 , 95 % CI 1 .

Example answer:
{"entities": []}

Example input:
Sentence: 00001 ; OR = 35 . 57 , 95 % CI = 19 . 61 - 64 . 51 , and p < 0 . 00001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 38 % ( 95 % CI : 7 . 36 - 7 . 40 ) , in the eastern provinces 8 . 59 % ( 95 % CI : 8 . 57 - 8 . 62 ) and in coastal areas 6 . 70 % ( 95 % CI : 6 . 68 - 6 . 72 ) compared to the mountainous ones , which is 8 . 91 % ( 95 % CI : 8 . 88 - 8 . 94 ) .

Example answer:
{"entities": [{"text": "eastern provinces", "type": "SpatialConcept"}, {"text": "coastal areas", "type": "SpatialConcept"}, {"text": "mountainous ones", "type": "PopulationGroup"}]}

Example input:
Sentence: 71 , 95 % CI 1 . 08 , 2 . 70 , p = 0 . 02 ; OR > 10 km vs . 0 - 1 km = 2 . 80 , 95 % CI 1 . 26 , 6 . 21 , p = 0 . 01 ) , adjusting for age and district of residence .

Example answer:
{"entities": [{"text": "residence", "type": "SpatialConcept"}]}

Example input:
Sentence: 18 % lived in rural areas .

Example answer:
{"entities": [{"text": "lived", "type": "SpatialConcept"}]}

Example input:
Sentence: 37 % ( 95 % CI 13 . 67 % - 17 . 24 % ) in rural areas .

Example answer:
{"entities": []}

Example input:
Sentence: 02 - 1 . 04 , p < 0 . 001 ) , and rural residence ( OR 1 .

Example answer:
{"entities": [{"text": "rural", "type": "Finding"}, {"text": "residence", "type": "SpatialConcept"}]}

Input:
Sentence: 00 - 1 . 04 , p = 0 . 001 ) , and rural residence ( OR 2 . 43 , 95 % CI 1 .

## Item MedMentions:test:1543
Example input:
Sentence: Patients were assessed using Numeric Rating Scale ( NRS ) , Pain Disability Index ( PDI ) , and Short Form Health Survey ( SF - 12 ) .

Example answer:
{"entities": [{"text": "Numeric Rating Scale", "type": "IntellectualProduct"}, {"text": "NRS", "type": "IntellectualProduct"}, {"text": "Pain Disability Index", "type": "IntellectualProduct"}, {"text": "PDI", "type": "IntellectualProduct"}, {"text": "Short Form Health Survey", "type": "IntellectualProduct"}, {"text": "SF - 12", "type": "IntellectualProduct"}]}

Example input:
Sentence: The patient 's personal assessment is the primary influence on psychosocial morbidity .

Example answer:
{"entities": [{"text": "psychosocial morbidity", "type": "BiologicFunction"}]}

Example input:
Sentence: A semi - structured diagnostic interview ( conducted with primary caregivers ) was used to assess for child suicidal thoughts and behaviors and psychiatric disorders .

Example answer:
{"entities": [{"text": "caregivers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "suicidal thoughts", "type": "Finding"}, {"text": "behaviors", "type": "Finding"}, {"text": "psychiatric disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: All patients were evaluated by anamnesis , physical examination , and self - report quality - of - life questionnaires .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "anamnesis", "type": "BiologicFunction"}, {"text": "physical examination", "type": "HealthCareActivity"}, {"text": "self - report", "type": "ResearchActivity"}, {"text": "quality - of - life questionnaires", "type": "IntellectualProduct"}]}

Example input:
Sentence: All patients had MR assessment of the brain .

Example answer:
{"entities": [{"text": "MR", "type": "HealthCareActivity"}, {"text": "assessment", "type": "HealthCareActivity"}, {"text": "brain", "type": "AnatomicalStructure"}]}

Example input:
Sentence: One stage - structured assessment of psychopathology was carried out by using a structured and valid Bangla version of the Development and Well - Being Assessment ( DAWBA ) .

Example answer:
{"entities": [{"text": "psychopathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "version", "type": "IntellectualProduct"}]}

Example input:
Sentence: Urgent referrals for psychological and psychiatric evaluations were initiated .

Example answer:
{"entities": [{"text": "referrals", "type": "HealthCareActivity"}, {"text": "psychiatric evaluations", "type": "HealthCareActivity"}]}

Example input:
Sentence: Development and Well - Being Assessment generated psychiatric diagnosis was assigned based on ICD - 10 diagnostic criteria for research .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "ICD - 10", "type": "IntellectualProduct"}, {"text": "diagnostic criteria", "type": "IntellectualProduct"}, {"text": "research", "type": "ResearchActivity"}]}

Example input:
Sentence: Psychiatric disorders were assessed using the Mini International Neuropsychiatric Interview , conducted by trained psychologists .

Example answer:
{"entities": [{"text": "Psychiatric disorders", "type": "BiologicFunction"}, {"text": "Mini International Neuropsychiatric Interview", "type": "HealthCareActivity"}, {"text": "trained psychologists", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Comprehensive clinical and psychiatric evaluations were done .

Example answer:
{"entities": [{"text": "clinical", "type": "HealthCareActivity"}, {"text": "psychiatric evaluations", "type": "HealthCareActivity"}]}

Input:
Sentence: Psychiatric and medical assessments .

## Item MedMentions:test:1555
Example input:
Sentence: Baseline score - adjusted comparison between groups showed that the postoperative median ASES scores ( atraumatic , 95 . 8 ; traumatic , 99 . 9 ) and SANE scores ( atraumatic , 86 . 5 ; traumatic , 98 . 0 ) were significantly more improved in patients with traumatic PSI ( P = .01 and P = .012 , respectively ) .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}, {"text": "median ASES scores", "type": "IntellectualProduct"}, {"text": "atraumatic", "type": "InjuryOrPoisoning"}, {"text": "traumatic", "type": "InjuryOrPoisoning"}, {"text": "SANE scores", "type": "IntellectualProduct"}]}

Example input:
Sentence: Adverse Events Profile total scores improved for 21 / 21 ( 100 . 0 % ) patients , QOLIE - 10 total scores improved for 17 / 21 ( 81 . 0 % ) patients , and alertness scores improved for 16 / 21 ( 76 . 2 % ) patients .

Example answer:
{"entities": [{"text": "Adverse Events Profile", "type": "IntellectualProduct"}, {"text": "improved", "type": "Finding"}, {"text": "QOLIE - 10", "type": "IntellectualProduct"}, {"text": "alertness", "type": "BiologicFunction"}]}

Example input:
Sentence: One hundred fourteen college freshmen completed the detailed questionnaire for estimating ANE ( aim 1 ) and answered the potential screening questions ( aim 2 ) .

Example answer:
{"entities": [{"text": "college freshmen", "type": "PopulationGroup"}, {"text": "questionnaire", "type": "IntellectualProduct"}, {"text": "ANE", "type": "Finding"}, {"text": "answered", "type": "IntellectualProduct"}, {"text": "screening questions", "type": "IntellectualProduct"}]}

Example input:
Sentence: The institution of a formal , faculty - led monthly CE preparation educational program at the University of Wisconsin has significantly improved the first - time pass rate for the ABS CE .

Example answer:
{"entities": [{"text": "institution", "type": "Organization"}, {"text": "University of Wisconsin", "type": "Organization"}, {"text": "improved", "type": "Finding"}, {"text": "pass", "type": "Finding"}, {"text": "ABS", "type": "Organization"}]}

Example input:
Sentence: Overall , applicants felt extremely prepared for the CE ( 4 . 70 ± 0 . 5 , Likert scale 1 - 5 ) .

Example answer:
{"entities": [{"text": "applicants", "type": "PopulationGroup"}, {"text": "prepared", "type": "Finding"}, {"text": "Likert scale", "type": "IntellectualProduct"}]}

Example input:
Sentence: Survey results showed that residents perceived the CE to be easier than the annual mock oral after the institution of the CE prep course ( P = 0 . 036 ) , however , there was no difference in their perception of preparedness .

Example answer:
{"entities": [{"text": "perceived", "type": "BiologicFunction"}, {"text": "mock oral", "type": "SpatialConcept"}, {"text": "institution", "type": "Organization"}, {"text": "perception", "type": "BiologicFunction"}, {"text": "preparedness", "type": "Finding"}]}

Example input:
Sentence: Mock oral annual examination scores were also significantly improved .

Example answer:
{"entities": [{"text": "Mock oral", "type": "SpatialConcept"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: In 2015 , the pass rates for the QE and CE were 80 % and 77 % , respectively .

Example answer:
{"entities": [{"text": "pass", "type": "Finding"}]}

Example input:
Sentence: De - identified data for the ABSITE and first - time pass rates for the QE and CE examination were retrospectively collected and analyzed along with survey results .

Example answer:
{"entities": [{"text": "ABSITE", "type": "IntellectualProduct"}, {"text": "pass", "type": "Finding"}, {"text": "retrospectively", "type": "ResearchActivity"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: Furthermore , ABSITE scores correlate with QE pass rates , and mock oral annual examination scores correlate with pass rates for both QE and CE .

Example answer:
{"entities": [{"text": "ABSITE", "type": "IntellectualProduct"}, {"text": "pass", "type": "Finding"}, {"text": "mock oral", "type": "SpatialConcept"}]}

Input:
Sentence: ABSITE raw score and percentile , as well as mock oral annual examination scores were significantly associated with passing the QE ( 0 . 032 , 0 . 027 , and 0 . 020 , respectively ) , whereas mock oral annual examination scores alone were associated with passing the CE ( P = 0 . 001 ) .

## Item MedMentions:test:1351
Example input:
Sentence: Tolvaptan treatment for severe neonatal autosomal - dominant polycystic kidney disease Severe neonatal autosomal - dominant polycystic kidney disease ( ADPKD ) is rare and easily confused with recessive PKD .

Example answer:
{"entities": [{"text": "Tolvaptan", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "autosomal - dominant polycystic kidney disease", "type": "AnatomicalStructure"}, {"text": "ADPKD", "type": "AnatomicalStructure"}, {"text": "recessive PKD", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Tolvaptan may be a useful treatment for severe neonatal PKD .

Example answer:
{"entities": [{"text": "Tolvaptan", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "PKD", "type": "BiologicFunction"}]}

Example input:
Sentence: A female infant with massive renal enlargement , respiratory compromise and hyponatraemia was treated with the arginine vasopressin receptor 2 antagonist tolvaptan .

Example answer:
{"entities": [{"text": "massive renal enlargement", "type": "Finding"}, {"text": "respiratory compromise", "type": "Finding"}, {"text": "hyponatraemia", "type": "BiologicFunction"}, {"text": "arginine vasopressin receptor 2", "type": "Chemical"}, {"text": "antagonist", "type": "Chemical"}, {"text": "tolvaptan", "type": "Chemical"}]}

Example input:
Sentence: Midodrine and tolvaptan have been used separately in these patients .

Example answer:
{"entities": [{"text": "Midodrine", "type": "Chemical"}, {"text": "tolvaptan", "type": "Chemical"}]}

Example input:
Sentence: Fifty cirrhotic patients with refractory or recurrent ascites were randomised to receive midodrine ( n = 13 ) , tolvaptan ( n = 12 ) or both ( n = 13 ) plus standard medical therapy ( SMT ) or SMT alone ( n = 12 ) .

Example answer:
{"entities": [{"text": "refractory", "type": "Finding"}, {"text": "randomised", "type": "ResearchActivity"}, {"text": "midodrine", "type": "Chemical"}, {"text": "tolvaptan", "type": "Chemical"}, {"text": "medical therapy", "type": "HealthCareActivity"}, {"text": "SMT", "type": "HealthCareActivity"}]}

Example input:
Sentence: The combination therapy was also superior to midodrine in the control of ascites at 1 month .

Example answer:
{"entities": [{"text": "combination therapy", "type": "HealthCareActivity"}, {"text": "midodrine", "type": "Chemical"}, {"text": "ascites", "type": "BiologicFunction"}]}

Example input:
Sentence: Midodrine and tolvaptan in patients with cirrhosis and refractory or recurrent ascites : a randomised pilot study Splanchnic arterial vasodilatation and subsequent sodium and water retention play an important role in cirrhotic ascites .

Example answer:
{"entities": [{"text": "Midodrine", "type": "Chemical"}, {"text": "tolvaptan", "type": "Chemical"}, {"text": "cirrhosis", "type": "BiologicFunction"}, {"text": "refractory", "type": "Finding"}, {"text": "randomised", "type": "ResearchActivity"}, {"text": "pilot study", "type": "ResearchActivity"}, {"text": "Splanchnic arterial vasodilatation", "type": "BiologicFunction"}, {"text": "sodium", "type": "BiologicFunction"}, {"text": "water retention", "type": "Finding"}, {"text": "cirrhotic ascites", "type": "BiologicFunction"}]}

Example input:
Sentence: The aim of this study was to evaluate the safety and efficacy of midodrine , tolvaptan and their combination in control of refractory or recurrent ascites in cirrhotics .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "midodrine", "type": "Chemical"}, {"text": "tolvaptan", "type": "Chemical"}, {"text": "combination", "type": "HealthCareActivity"}, {"text": "refractory", "type": "Finding"}, {"text": "cirrhotics", "type": "BiologicFunction"}]}

Example input:
Sentence: Midodrine as well as combination of midodrine and tolvaptan but not tolvaptan alone was superior to SMT in control of ascites at 3 months ( P < . 05 ) .

Example answer:
{"entities": [{"text": "Midodrine", "type": "Chemical"}, {"text": "combination", "type": "HealthCareActivity"}, {"text": "midodrine", "type": "Chemical"}, {"text": "tolvaptan", "type": "Chemical"}, {"text": "SMT", "type": "HealthCareActivity"}, {"text": "ascites", "type": "BiologicFunction"}]}

Example input:
Sentence: However , there are no reports on the use of combination of midodrine and tolvaptan in the control of ascites .

Example answer:
{"entities": [{"text": "combination", "type": "HealthCareActivity"}, {"text": "midodrine", "type": "Chemical"}, {"text": "tolvaptan", "type": "Chemical"}, {"text": "ascites", "type": "BiologicFunction"}]}

Input:
Sentence: The results of this pilot study suggest that midodrine and combination with tolvaptan better controls ascites without any renal or hepatic dysfunction .

## Item MedMentions:test:1443
Example input:
Sentence: Serum was collected into five types of vacuum blood collection tubes from three manufacturers , and 25OHD was analyzed using the Siemens ADVIA Centaur XP system and liquid chromatography tandem mass spectrometry ( LC - MS / MS ) immediately or after storage at 4°C or -80°C for 48 h .

Example answer:
{"entities": [{"text": "Serum", "type": "BodySubstance"}, {"text": "vacuum blood collection tubes", "type": "MedicalDevice"}, {"text": "25OHD was analyzed", "type": "HealthCareActivity"}, {"text": "liquid chromatography tandem mass spectrometry", "type": "HealthCareActivity"}, {"text": "LC - MS / MS", "type": "HealthCareActivity"}]}

Example input:
Sentence: Univariate analysis showed that PG volumes receiving more than 5 , 10 , 15 , and 20 Gy RBE ( V5 , V10 , V15 and V20 , respectively ) , mean dose , and maximum dose were significantly associated with PG atrophy .

Example answer:
{"entities": [{"text": "PG", "type": "AnatomicalStructure"}, {"text": "PG atrophy", "type": "BiologicFunction"}]}

Example input:
Sentence: 9 cm ( 2 ) ) , PG ( between 55 and 75 mm Hg or over 75 mm Hg ) , and end - diastolic LV dimension ( of more or less than 56 mm ) .

Example answer:
{"entities": [{"text": "PG", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Using both inferential and non - supervised multivariate statistics , we show sets of spots features that lead to a clear discrimination between controls and EU exposed groups on the one hand ( 21 spots ) , and between 4 % EU and 12 % EU on the other hand ( 7 spots ) , showing that investigation of the serum proteome may possibly be of relevance to address both uranium contamination and radiological effect .

Example answer:
{"entities": [{"text": "non - supervised multivariate statistics", "type": "ResearchActivity"}, {"text": "spots", "type": "Chemical"}, {"text": "EU", "type": "Chemical"}, {"text": "serum", "type": "BodySubstance"}, {"text": "proteome", "type": "Chemical"}, {"text": "uranium", "type": "Chemical"}]}

Example input:
Sentence: The strain contained five contigs corresponding to presumptive plasmids of sizes : 19 , 036 ; 24 , 250 ; 26 , 581 ; 65 , 272 ; and 65 , 904 bp .

Example answer:
{"entities": [{"text": "contigs", "type": "SpatialConcept"}, {"text": "plasmids", "type": "Chemical"}, {"text": "sizes", "type": "SpatialConcept"}, {"text": "bp", "type": "Chemical"}]}

Example input:
Sentence: 22 for EUT ( P < 0 .

Example answer:
{"entities": [{"text": "EUT", "type": "HealthCareActivity"}]}

Example input:
Sentence: We have provided objective evidence for the futility of reprocessing attempts , and practice of EUS needle reuse should be discontinued .

Example answer:
{"entities": [{"text": "discontinued", "type": "Finding"}]}

Example input:
Sentence: Residual contamination and bioburden after reprocessing of single - use endoscopic ultrasound needles : An ex vivo study Endoscopic ultrasound ( EUS ) aspiration needles are single - use devices .

Example answer:
{"entities": [{"text": "single - use", "type": "MedicalDevice"}, {"text": "study", "type": "ResearchActivity"}, {"text": "single - use devices", "type": "MedicalDevice"}]}

Example input:
Sentence: There is significant bioburden in reprocessed EUS needles ; standard microbiological cultures have low sensitivity for detection of needle contamination .

Example answer:
{"entities": [{"text": "microbiological cultures", "type": "HealthCareActivity"}, {"text": "sensitivity", "type": "HealthCareActivity"}, {"text": "detection", "type": "Finding"}]}

Example input:
Sentence: Larger ( 19 G ) needles had higher surface contamination ( P = 0 . 016 ) , but there was no relation of luminal contamination with needle diameter ( P = 0 . 138 ) .

Example answer:
{"entities": [{"text": "needles", "type": "MedicalDevice"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "no relation", "type": "Finding"}, {"text": "luminal", "type": "SpatialConcept"}, {"text": "needle", "type": "MedicalDevice"}]}

Input:
Sentence: We studied 10 EUS needles each of 19 G , 22 G , and 25 G in size , and five 22 - G ProCore needles .

## Item MedMentions:test:1646
Example input:
Sentence: A total of 7 , 761 patients from ten clinical trials were included in the meta - analysis .

Example answer:
{"entities": [{"text": "clinical trials", "type": "ResearchActivity"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Eight randomized , controlled trials with a total of 476 subjects were included in the meta - analysis .

Example answer:
{"entities": [{"text": "randomized , controlled trials", "type": "ResearchActivity"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: The reviewers selected a total of 51 studies for qualitative synthesis and 43 studies for meta - analysis .

Example answer:
{"entities": [{"text": "reviewers", "type": "PopulationGroup"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Fifty papers met eligibility criteria for review , and meta - analysis of overall results was possible in thirty - two ( 2050 participants ) .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "meta - analysis", "type": "IntellectualProduct"}, {"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: Nine cross - sectional studies were included in the meta - analyses , providing data on 1547 participants .

Example answer:
{"entities": [{"text": "cross - sectional studies", "type": "ResearchActivity"}, {"text": "meta - analyses", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: Twenty - six studies published from 2008 to 2014 , with a total of 52 , 683 cases and 64 , 672 controls , were included in this meta - analysis .

Example answer:
{"entities": [{"text": "studies published", "type": "IntellectualProduct"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: We identified 433 studies ; 28 were eligible for analysis .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Out of seventeen identified studies , sixteen were included in the meta - analysis .

Example answer:
{"entities": [{"text": "identified studies", "type": "ResearchActivity"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Four studies were included in the meta - analysis .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: A total of 13 studies with 1301 subjects were included for meta - analysis .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "subjects", "type": "PopulationGroup"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Input:
Sentence: A total of 22 studies were eligible for the meta - analysis .

## Item MedMentions:test:1618
Example input:
Sentence: A larger proportion of patients entered through the drop - out side door died or was lost to follow - up ( 37 . 3 % ) , as compared to patients in the front door group ( 24 . 9 % ) and transferred - in side door group ( 17 . 7 % ) .

Example answer:
{"entities": [{"text": "died", "type": "Finding"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: For mental health and substance use services , three classes emerged ( stable - low , 69 % and 61 % , respectively ; low - baseline - increase , 10 % and 12 % , respectively ; high - baseline decline , 21 % and 28 % , respectively ) .

Example answer:
{"entities": [{"text": "mental health", "type": "BiologicFunction"}, {"text": "services", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients were categorized into three groups ( 1 ) Front door : started on ART without interruption during follow - up ; ( 2 ) drop - out side door : restarted on ART after having an interruption > 6 months and ( 3 ) transfer - in side door : transferred - in after being started on ART somewhere else .

Example answer:
{"entities": [{"text": "ART", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: The patients in the chlamydia group were younger and had a higher rate of TOA , a longer mean hospital stay , and had undergone more surgeries than the patients in the non - chlamydia group .

Example answer:
{"entities": [{"text": "chlamydia group", "type": "PopulationGroup"}, {"text": "TOA", "type": "BiologicFunction"}, {"text": "surgeries", "type": "HealthCareActivity"}, {"text": "non - chlamydia group", "type": "PopulationGroup"}]}

Example input:
Sentence: The three groups were generally comparable , although patients transferred in were sicker .

Example answer:
{"entities": [{"text": "patients transferred", "type": "HealthCareActivity"}, {"text": "sicker", "type": "Finding"}]}

Example input:
Sentence: More patients in the front door group ( 32 . 1 % ) were transferred out during the follow - up .

Example answer:
{"entities": [{"text": "transferred", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: There were no differences in the baseline characteristics of patients enrolled in the extension phase versus those who were not .

Example answer:
{"entities": []}

Example input:
Sentence: There was no statistical difference in mean hospital stay between these two groups ( 95 % CI , - 3 . 49 - 5 . 78 ; p = 0 .

Example answer:
{"entities": [{"text": "no", "type": "Finding"}]}

Example input:
Sentence: Only 34 % of the patients in the historical cohort received a second - line chemotherapy in comparison to 69 % in the 2011 + cohort .

Example answer:
{"entities": [{"text": "historical cohort", "type": "PopulationGroup"}, {"text": "second - line chemotherapy", "type": "HealthCareActivity"}, {"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: The highest probability of switching to second line was found in the transferred - in group .

Example answer:
{"entities": [{"text": "second line", "type": "HealthCareActivity"}, {"text": "found", "type": "Finding"}]}

Input:
Sentence: We compared characteristics at enrollment in the three groups and investigated the following outcomes : ( 1 ) retention in care ( 2 ) switch to second line .

## Item MedMentions:test:1593
Example input:
Sentence: Females are twice more likely to develop fibroma than males .

Example answer:
{"entities": [{"text": "fibroma", "type": "BiologicFunction"}]}

Example input:
Sentence: SD at baseline was more common in females ( placebo , 46 . 4 % ; vilazodone , 49 % ) than in males ( placebo , 35 . 1 % ; vilazodone , 40 . 9 % ) .

Example answer:
{"entities": [{"text": "SD", "type": "BiologicFunction"}, {"text": "females", "type": "PopulationGroup"}, {"text": "placebo", "type": "Chemical"}, {"text": "vilazodone", "type": "Chemical"}, {"text": "males", "type": "PopulationGroup"}]}

Example input:
Sentence: In contrast , a strong negative correlation between TSH and T2DM was observed in males , but not in females .

Example answer:
{"entities": [{"text": "TSH", "type": "Chemical"}, {"text": "T2DM", "type": "BiologicFunction"}]}

Example input:
Sentence: This study showed that iNPH occurs most frequently in the 70s , gait impairment and cognitive decline are the most frequent initial symptoms in men and women , respectively , and hypertension and diabetes are the most frequent comorbidities in men and women , respectively .

Example answer:
{"entities": [{"text": "iNPH", "type": "BiologicFunction"}, {"text": "gait impairment", "type": "Finding"}, {"text": "cognitive decline", "type": "Finding"}, {"text": "symptoms", "type": "Finding"}, {"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "hypertension", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: A large Japanese multicenter registry of consecutive patients with severe AS included a much higher proportion of women than men , with the female : male sex ratio increasing with age .

Example answer:
{"entities": [{"text": "Japanese", "type": "SpatialConcept"}, {"text": "AS", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: Women who remained uninfected displayed a greater frequency of positive CD4 ( + ) T - cell responses ( 29 % vs 18 % ; P < .0001 ) , compared with women who had incident infection , while the frequencies of CD8 ( + ) T - cell responses did not differ .

Example answer:
{"entities": [{"text": "Women", "type": "PopulationGroup"}, {"text": "CD4 ( + ) T - cell", "type": "AnatomicalStructure"}, {"text": "responses", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "CD8 ( + ) T - cell", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Hypertension was observed more frequently in men , but diabetes was observed more frequently in women ( p < .05 ) .

Example answer:
{"entities": [{"text": "Hypertension", "type": "BiologicFunction"}, {"text": "men", "type": "PopulationGroup"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Women showed significantly more often persistent lesions than men ( 94 % vs .

Example answer:
{"entities": [{"text": "Women", "type": "PopulationGroup"}, {"text": "lesions", "type": "Finding"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: In addition , female patients taking TH treatment exhibited a lower risk than their male counterparts .

Example answer:
{"entities": [{"text": "TH treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: In males , trends in TC were stable .

Example answer:
{"entities": [{"text": "TC", "type": "BiologicFunction"}]}

Input:
Sentence: TC occurred more frequently in females than in males .

## Item MedMentions:test:1419
Example input:
Sentence: The results of limited proteolysis indicated that Glu138Pro mutant was more resistant against trypsinolysis and this variant was less quenched in both acrylamide and KI quenching experiments .

Example answer:
{"entities": [{"text": "limited proteolysis", "type": "BiologicFunction"}, {"text": "Glu138Pro mutant", "type": "Chemical"}, {"text": "trypsinolysis", "type": "BiologicFunction"}, {"text": "variant", "type": "Chemical"}, {"text": "acrylamide", "type": "Chemical"}, {"text": "KI", "type": "Chemical"}, {"text": "quenching experiments", "type": "HealthCareActivity"}]}

Example input:
Sentence: We show that despite promising results from our cell culture model , our in vivo data failed to demonstrate similarly reproducible enhancement of dystrophin translation , suggesting that miR31 - modulation may not be practical under current oligonucleotide approaches .

Example answer:
{"entities": [{"text": "cell culture", "type": "HealthCareActivity"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "dystrophin", "type": "Chemical"}, {"text": "translation", "type": "BiologicFunction"}, {"text": "miR31", "type": "Chemical"}, {"text": "oligonucleotide", "type": "Chemical"}]}

Example input:
Sentence: This work demonstrates that glycolytic metabolism regulates the translation of HIF1A to determine T cell responses to hypoxia and implicates GAPDH as a potential mechanism for controlling T cell function in peripheral tissue .

Example answer:
{"entities": [{"text": "glycolytic", "type": "BiologicFunction"}, {"text": "metabolism", "type": "BiologicFunction"}, {"text": "translation", "type": "BiologicFunction"}, {"text": "HIF1A", "type": "AnatomicalStructure"}, {"text": "T cell", "type": "AnatomicalStructure"}, {"text": "responses", "type": "BiologicFunction"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "GAPDH", "type": "Chemical"}, {"text": "function", "type": "BiologicFunction"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Mechanistically , ubiquitin - dependent degradation of the cyclin - dependent kinase ( CDK ) inhibitor , p21 protein , is reduced by CHIP knockdown , leading to enhanced senescence of cells in response to exposure to IR .

Example answer:
{"entities": [{"text": "ubiquitin - dependent degradation", "type": "BiologicFunction"}, {"text": "cyclin - dependent kinase ( CDK ) inhibitor , p21 protein", "type": "Chemical"}, {"text": "CHIP", "type": "AnatomicalStructure"}, {"text": "knockdown", "type": "ResearchActivity"}, {"text": "senescence of cells", "type": "BiologicFunction"}, {"text": "exposure to IR", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: We also showed that nutrient deprivation ( serine starvation ) regulated by stringent and general stress response , contribute to the increased tolerance of P .

Example answer:
{"entities": [{"text": "nutrient", "type": "Food"}, {"text": "serine", "type": "Chemical"}, {"text": "starvation", "type": "Finding"}, {"text": "stringent and general stress response", "type": "BiologicFunction"}, {"text": "increased tolerance", "type": "Finding"}, {"text": "P .", "type": "Bacterium"}]}

Example input:
Sentence: Thus , we propose a model where inhibition of protein translation , together with the degradation systems , limit autophagy during starvation .

Example answer:
{"entities": [{"text": "protein translation", "type": "BiologicFunction"}, {"text": "degradation", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "starvation", "type": "Finding"}]}

Example input:
Sentence: Although both autophagic and proteasomal systems contribute to the degradation of ULK1 , under prolonged nitrogen deprivation , its level was still reduced in ATG7 knockout cells , and only initially stabilized in cells treated with the lysosomal or proteasomal inhibitors .

Example answer:
{"entities": [{"text": "autophagic", "type": "BiologicFunction"}, {"text": "proteasomal systems", "type": "Chemical"}, {"text": "degradation", "type": "BiologicFunction"}, {"text": "ULK1", "type": "Chemical"}, {"text": "nitrogen", "type": "Chemical"}, {"text": "ATG7", "type": "AnatomicalStructure"}, {"text": "knockout cells", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "lysosomal", "type": "AnatomicalStructure"}, {"text": "proteasomal inhibitors", "type": "Chemical"}]}

Example input:
Sentence: Here we report that despite the significant upregulation of mRNA of the essential autophagy initiation gene ULK1 , its protein level is rapidly reduced under starvation .

Example answer:
{"entities": [{"text": "upregulation", "type": "BiologicFunction"}, {"text": "mRNA", "type": "Chemical"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "initiation gene", "type": "AnatomicalStructure"}, {"text": "ULK1", "type": "AnatomicalStructure"}, {"text": "protein", "type": "Chemical"}, {"text": "starvation", "type": "Finding"}]}

Example input:
Sentence: Suppressed translation and ULK1 degradation as potential mechanisms of autophagy limitation under prolonged starvation Macroautophagy / autophagy is a well - organized process of intracellular degradation , which is rapidly activated under starvation conditions .

Example answer:
{"entities": [{"text": "translation", "type": "BiologicFunction"}, {"text": "ULK1", "type": "Chemical"}, {"text": "degradation", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "starvation", "type": "Finding"}, {"text": "Macroautophagy", "type": "BiologicFunction"}, {"text": "intracellular degradation", "type": "BiologicFunction"}]}

Example input:
Sentence: However , such upregulation of ULK1 protein is negligible under starvation conditions , further signifying the contribution of translation and suggesting that transcriptional upregulation of ULK1 protein will be diminished under such conditions .

Example answer:
{"entities": [{"text": "upregulation", "type": "BiologicFunction"}, {"text": "ULK1 protein", "type": "Chemical"}, {"text": "starvation", "type": "Finding"}, {"text": "translation", "type": "BiologicFunction"}, {"text": "transcriptional", "type": "BiologicFunction"}]}

Input:
Sentence: We demonstrate that under starvation , protein translation is rapidly diminished and , similar to treatments with the proteosynthesis inhibitors cycloheximide or anisomycin , is associated with a significant reduction of ULK1 .

## Item MedMentions:test:1742
Example input:
Sentence: Haptic feedback helps bipedal coordination The present study investigated whether special haptic or visual feedback would facilitate the coordination of in - phase , cyclical feet movements of different amplitudes .

Example answer:
{"entities": [{"text": "feedback", "type": "BiologicFunction"}, {"text": "bipedal", "type": "AnatomicalStructure"}, {"text": "coordination", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "visual feedback", "type": "BiologicFunction"}, {"text": "feet", "type": "AnatomicalStructure"}, {"text": "movements", "type": "BiologicFunction"}, {"text": "amplitudes", "type": "SpatialConcept"}]}

Example input:
Sentence: Neglecting the need to endorse linkages between human health , animal health and husbandry , agriculture , and environmental sectors , has led to duplicative and weak response systems .

Example answer:
{"entities": [{"text": "linkages", "type": "IntellectualProduct"}, {"text": "human", "type": "Eukaryote"}, {"text": "animal", "type": "Eukaryote"}, {"text": "environmental", "type": "SpatialConcept"}, {"text": "sectors", "type": "SpatialConcept"}, {"text": "weak response systems", "type": "Finding"}]}

Example input:
Sentence: Spatiotemporal Control of Intracellular Phase Transitions Using Light - Activated optoDroplets Phase transitions driven by intrinsically disordered protein regions ( IDRs ) have emerged as a ubiquitous mechanism for assembling liquid - like RNA / protein ( RNP ) bodies and other membrane - less organelles .

Example answer:
{"entities": [{"text": "Spatiotemporal", "type": "ResearchActivity"}, {"text": "Intracellular", "type": "SpatialConcept"}, {"text": "Light - Activated optoDroplets", "type": "ResearchActivity"}, {"text": "intrinsically disordered protein regions", "type": "Chemical"}, {"text": "IDRs", "type": "Chemical"}, {"text": "RNA / protein", "type": "Chemical"}, {"text": "RNP", "type": "Chemical"}, {"text": "bodies", "type": "AnatomicalStructure"}, {"text": "membrane - less organelles", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In general , regardless of the context , Behavioural Avoidance and Passivity are the least prevalent strategies , whereas Active Solution is the most prevalent one , followed by Emotion .

Example answer:
{"entities": [{"text": "general", "type": "SpatialConcept"}, {"text": "Behavioural Avoidance", "type": "BiologicFunction"}, {"text": "Emotion", "type": "BiologicFunction"}]}

Example input:
Sentence: Moderation analysis indicated that all EFs moderated the relationship between physical punishment and aggression , and only inhibition and problem - solving ability , but not cognitive flexibility and nonverbal fluency , moderated the relations between symbolic punishment and aggression .

Example answer:
{"entities": [{"text": "Moderation analysis", "type": "ResearchActivity"}, {"text": "EFs", "type": "BiologicFunction"}, {"text": "problem - solving ability", "type": "Finding"}, {"text": "cognitive flexibility", "type": "BiologicFunction"}, {"text": "nonverbal", "type": "Finding"}]}

Example input:
Sentence: It is the default , unlearned response to prolonged aversive events and it is mediated by the serotonergic activity of the dorsal raphe nucleus , which in turn inhibits escape .

Example answer:
{"entities": [{"text": "serotonergic activity", "type": "BiologicFunction"}, {"text": "dorsal raphe nucleus", "type": "AnatomicalStructure"}, {"text": "escape", "type": "BiologicFunction"}]}

Example input:
Sentence: A tacit division of labour is enacted via multimodal communication strategies , whereby perturbations are dealt with using both linguistic and bodily signals .

Example answer:
{"entities": []}

Example input:
Sentence: This increase in responding , however , was less goal - directed as ID rats also responded more quickly to the non - rewarded manipulandum than did control rats .

Example answer:
{"entities": [{"text": "ID", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: Flexible Coordination of Stationary and Mobile Conversations with Gaze : Resource Allocation among Multiple Joint Activities Gaze is instrumental in coordinating face - to - face social interactions .

Example answer:
{"entities": [{"text": "Gaze", "type": "Finding"}, {"text": "social interactions", "type": "Finding"}]}

Example input:
Sentence: Emergence of diseases such as avian influenza and Ebola virus disease , which threatened social disruption , have established the need for intersectoral coordination / collaboration .

Example answer:
{"entities": [{"text": "Emergence of diseases", "type": "BiologicFunction"}, {"text": "avian influenza", "type": "BiologicFunction"}, {"text": "Ebola virus disease", "type": "BiologicFunction"}, {"text": "intersectoral coordination / collaboration", "type": "HealthCareActivity"}]}

Input:
Sentence: Intersectoral coordination was briefly carried out , more as a reactive response to threats .

## Item MedMentions:test:1749
Example input:
Sentence: 88 , 95 % CI : 1 . 51 - 2 . 33 , P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 44 95 % CI 1 . 8 to 10 . 92 , P = 0 . 0004 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 30 ; 95 % CI 0 . 08 - 0 . 89 ; p = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 85 ( CI 95 % : 0 . 84 to 0 . 92 ) , respectively ( P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 00001 ; OR = 35 . 57 , 95 % CI = 19 . 61 - 64 . 51 , and p < 0 . 00001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 68 ; 95 % CI , -10 . 74 to -2 . 62 ; P = 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 44 ; 95 % CI 0 . 22 - 0 . 87 ; p = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 23 [ 95 % CI , -0 . 44 to -0 . 02 ] ; P = .05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 22 95 % CI 0 . 44 to 3 . 4 , P = 0 . 51 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 4 ; 95 % CI , -7 . 2 to -1 . 6 ; P = .002 ) .

Example answer:
{"entities": []}

Input:
Sentence: 3 to 2 . 4 ; P = 0 . 002 ) as well as in never - smokers ( OR : 2 . 0 , 95 % CI : 1 . 2 to 3 . 5 ; P = 0 . 01 ) .

## Item MedMentions:test:1299
Example input:
Sentence: Ten microRNAs associated with prognosis were identified ( let - 7 g , miR - 29a - 5p , - 34a - 5p , - 125a - 3p , - 146a - 5p , - 187 , - 205 - 5p , - 212 - 3p , - 222 - 5p , and miR - 450b - 5p ) .

Example answer:
{"entities": [{"text": "microRNAs", "type": "Chemical"}, {"text": "prognosis", "type": "HealthCareActivity"}, {"text": "let - 7 g", "type": "Chemical"}, {"text": "miR - 29a - 5p", "type": "AnatomicalStructure"}, {"text": "34a - 5p", "type": "AnatomicalStructure"}, {"text": "125a - 3p", "type": "AnatomicalStructure"}, {"text": "146a - 5p", "type": "AnatomicalStructure"}, {"text": "187", "type": "AnatomicalStructure"}, {"text": "205 - 5p", "type": "Chemical"}, {"text": "212 - 3p", "type": "AnatomicalStructure"}, {"text": "222 - 5p", "type": "AnatomicalStructure"}, {"text": "miR - 450b - 5p", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Previous studies have suggested that long non‑coding RNAs ( lncRNAs ) may be key regulators of tumor development and progression in HCC .

Example answer:
{"entities": [{"text": "long non‑coding RNAs", "type": "Chemical"}, {"text": "lncRNAs", "type": "Chemical"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "HCC", "type": "BiologicFunction"}]}

Example input:
Sentence: The Novel miR - 9600 Suppresses Tumor Progression and Promotes Paclitaxel Sensitivity in Non - small - cell Lung Cancer Through Altering STAT3 Expression MicroRNAs have been identified to be involved in center stage of cancer biology .

Example answer:
{"entities": [{"text": "miR - 9600", "type": "Chemical"}, {"text": "Tumor Progression", "type": "BiologicFunction"}, {"text": "Paclitaxel", "type": "Chemical"}, {"text": "Non - small - cell Lung Cancer", "type": "BiologicFunction"}, {"text": "STAT3", "type": "AnatomicalStructure"}, {"text": "Expression", "type": "BiologicFunction"}, {"text": "MicroRNAs", "type": "Chemical"}, {"text": "center stage", "type": "ClinicalAttribute"}, {"text": "cancer biology", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Twenty - two microRNAs were significantly differently expressed in patients with pancreatic cancer when compared to healthy controls and chronic pancreatitis patients ; 17 miRNAs were upregulated ( miR - 21 - 5p , - 23a - 3p , - 31 - 5p , - 34c - 5p , - 93 - 3p , - 135b - 3p , - 155 - 5p , - 186 - 5p , - 196b - 5p , - 203 , - 205 - 5p , - 210 , - 222 - 3p , - 451 , - 492 , - 614 , and miR - 622 ) and 5 were downregulated ( miR - 122 - 5p , - 130b - 3p , - 216b , - 217 , and miR - 375 ) .

Example answer:
{"entities": [{"text": "microRNAs", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "pancreatic cancer", "type": "BiologicFunction"}, {"text": "chronic pancreatitis", "type": "BiologicFunction"}, {"text": "miRNAs", "type": "Chemical"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "miR - 21 - 5p", "type": "AnatomicalStructure"}, {"text": "23a - 3p", "type": "AnatomicalStructure"}, {"text": "31 - 5p", "type": "AnatomicalStructure"}, {"text": "34c - 5p", "type": "AnatomicalStructure"}, {"text": "93 - 3p", "type": "AnatomicalStructure"}, {"text": "135b - 3p", "type": "AnatomicalStructure"}, {"text": "155 - 5p", "type": "AnatomicalStructure"}, {"text": "186 - 5p", "type": "AnatomicalStructure"}, {"text": "196b - 5p ,", "type": "AnatomicalStructure"}, {"text": "203", "type": "AnatomicalStructure"}, {"text": "205 - 5p", "type": "Chemical"}, {"text": "210", "type": "AnatomicalStructure"}, {"text": "222 - 3p", "type": "AnatomicalStructure"}, {"text": "451", "type": "AnatomicalStructure"}, {"text": "492", "type": "AnatomicalStructure"}, {"text": "614", "type": "AnatomicalStructure"}, {"text": "miR - 622", "type": "AnatomicalStructure"}, {"text": "downregulated", "type": "BiologicFunction"}, {"text": "miR - 122 - 5p", "type": "AnatomicalStructure"}, {"text": "130b - 3p", "type": "AnatomicalStructure"}, {"text": "216b", "type": "AnatomicalStructure"}, {"text": "217", "type": "AnatomicalStructure"}, {"text": "miR - 375", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Different microRNA alterations contribute to diverse outcomes following EV71 and CA16 infections : Insights from high - throughput sequencing in rhesus monkey peripheral blood mononuclear cells Enterovirus 71 ( EV71 ) and Coxsackievirus A16 ( CA16 ) are the predominant pathogens of hand , foot , and mouth disease ( HFMD ) .

Example answer:
{"entities": [{"text": "microRNA", "type": "AnatomicalStructure"}, {"text": "EV71", "type": "BiologicFunction"}, {"text": "infections", "type": "BiologicFunction"}, {"text": "high - throughput sequencing", "type": "ResearchActivity"}, {"text": "rhesus monkey", "type": "Eukaryote"}, {"text": "peripheral blood mononuclear cells", "type": "AnatomicalStructure"}, {"text": "Enterovirus 71", "type": "Virus"}, {"text": "EV71", "type": "Virus"}, {"text": "hand , foot , and mouth disease", "type": "BiologicFunction"}, {"text": "HFMD", "type": "BiologicFunction"}]}

Example input:
Sentence: The comparison with published findings in adults demonstrated a unique miRNA signature in young patients with aggressive disease .

Example answer:
{"entities": [{"text": "published", "type": "IntellectualProduct"}, {"text": "findings", "type": "Finding"}, {"text": "miRNA", "type": "Chemical"}]}

Example input:
Sentence: MiR - 424 - 5p participates in esophageal squamous cell carcinoma invasion and metastasis via SMAD7 pathway mediated EMT ESCC is a life - threatening disease due to invasion and metastasis in the early stage .

Example answer:
{"entities": [{"text": "MiR - 424 - 5p", "type": "AnatomicalStructure"}, {"text": "esophageal squamous cell carcinoma", "type": "BiologicFunction"}, {"text": "invasion", "type": "BiologicFunction"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "SMAD7", "type": "AnatomicalStructure"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "EMT", "type": "BiologicFunction"}, {"text": "ESCC", "type": "BiologicFunction"}, {"text": "life - threatening", "type": "Finding"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: The expression of let - 7f - 5p was upregulated in non - aggressive tumors , while the expression of let - 7e - 5p was upregulated in aggressive tumors , compared with the corresponding normal tissue .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "let - 7f - 5p", "type": "Chemical"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "non - aggressive", "type": "Finding"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "let - 7e - 5p", "type": "Chemical"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The levels of let - 7f - 5p , miR - 30b - 5p and let - 7e - 5p were upregulated in tumors ( P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "let - 7f - 5p", "type": "Chemical"}, {"text": "miR - 30b - 5p", "type": "Chemical"}, {"text": "let - 7e - 5p", "type": "Chemical"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: miRNA expression profiles were evaluated in formalin - fixed , paraffin - embedded samples of tumor and normal mucosa from 12 patients aged < 30 years old with squamous cell carcinoma of the tongue .

Example answer:
{"entities": [{"text": "miRNA", "type": "Chemical"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "formalin - fixed , paraffin - embedded samples", "type": "AnatomicalStructure"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "mucosa", "type": "AnatomicalStructure"}, {"text": "squamous cell carcinoma of the tongue", "type": "BiologicFunction"}]}

Input:
Sentence: Distinctive pattern of let - 7 family microRNAs in aggressive carcinoma of the oral tongue in young patients Oral cavity squamous cell carcinoma may be more aggressive at presentation and recurrence in young patients compared with older patients .

## Item MedMentions:test:1331
Example input:
Sentence: The use of SC79 , an Akt1 / 2 inhibitor , was found to block the PFOS - induced Sertoli cell injury by rescuing the PFOS - induced F - actin dis - organization .

Example answer:
{"entities": [{"text": "SC79", "type": "Chemical"}, {"text": "Akt1", "type": "Chemical"}, {"text": "2", "type": "Chemical"}, {"text": "block", "type": "BiologicFunction"}, {"text": "PFOS", "type": "Chemical"}, {"text": "Sertoli cell", "type": "AnatomicalStructure"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "F - actin", "type": "Chemical"}]}

Example input:
Sentence: In the present study we report on the effect of leonurine on ICR mice with adenomyosis induced by neonatal tamoxifen .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "leonurine", "type": "Chemical"}, {"text": "ICR mice", "type": "Eukaryote"}, {"text": "adenomyosis", "type": "BiologicFunction"}, {"text": "tamoxifen", "type": "Chemical"}]}

Example input:
Sentence: Using the activatory Gq - coupled human M3 muscarinic receptor ( hM3Dq ) , we found that chemogenetic stimulation of dSPNs mimicked , while stimulation of iSPNs abolished the therapeutic action of L - DOPA in PD mice .

Example answer:
{"entities": [{"text": "activatory Gq - coupled human M3 muscarinic receptor", "type": "Chemical"}, {"text": "hM3Dq", "type": "Chemical"}, {"text": "chemogenetic stimulation", "type": "BiologicFunction"}, {"text": "dSPNs", "type": "AnatomicalStructure"}, {"text": "stimulation", "type": "BiologicFunction"}, {"text": "iSPNs", "type": "AnatomicalStructure"}, {"text": "therapeutic action", "type": "BiologicFunction"}, {"text": "L - DOPA", "type": "Chemical"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: In LID mice , hM3Dq stimulation of dSPNs exacerbated dyskinetic responses to L - DOPA , while stimulation of iSPNs inhibited these responses .

Example answer:
{"entities": [{"text": "LID", "type": "Finding"}, {"text": "mice", "type": "Eukaryote"}, {"text": "hM3Dq", "type": "Chemical"}, {"text": "stimulation", "type": "BiologicFunction"}, {"text": "dSPNs", "type": "AnatomicalStructure"}, {"text": "L - DOPA", "type": "Chemical"}, {"text": "iSPNs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In this study , we showed that TEA and 4 - AP insensitive non - inactivating outward K ( + ) current ( NIOK ) may be responsible for the quiescence of murine pregnant longitudinal myometrium .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "TEA", "type": "Chemical"}, {"text": "4 - AP", "type": "Chemical"}, {"text": "insensitive", "type": "Finding"}, {"text": "non - inactivating outward K ( + ) current", "type": "BiologicFunction"}, {"text": "NIOK", "type": "BiologicFunction"}, {"text": "quiescence", "type": "BiologicFunction"}, {"text": "murine", "type": "Eukaryote"}, {"text": "pregnant", "type": "AnatomicalStructure"}, {"text": "longitudinal", "type": "SpatialConcept"}, {"text": "myometrium", "type": "AnatomicalStructure"}]}

Example input:
Sentence: CONCLUSIONS Our results indicate that leonurine attenuates hyperalgesia in mice with induced adenomyosis via down - regulating expressions of p - P65 , COX - 2 , and OTR , and could be beneficial for treating adenomyosis .

Example answer:
{"entities": [{"text": "leonurine", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Finding"}, {"text": "mice", "type": "Eukaryote"}, {"text": "adenomyosis", "type": "BiologicFunction"}, {"text": "down - regulating", "type": "BiologicFunction"}, {"text": "expressions", "type": "BiologicFunction"}, {"text": "p - P65", "type": "Chemical"}, {"text": "COX - 2", "type": "Chemical"}, {"text": "OTR", "type": "Chemical"}]}

Example input:
Sentence: Leonurine Attenuates Hyperalgesia in Mice with Induced Adenomyosis BACKGROUND Adenomyosis , defined as the invasion of endometrial glands and stroma into the myometrium , is a common gynecological disorder .

Example answer:
{"entities": [{"text": "Leonurine", "type": "Chemical"}, {"text": "Hyperalgesia", "type": "Finding"}, {"text": "Mice", "type": "Eukaryote"}, {"text": "Adenomyosis", "type": "BiologicFunction"}, {"text": "invasion", "type": "BiologicFunction"}, {"text": "endometrial glands", "type": "AnatomicalStructure"}, {"text": "stroma", "type": "AnatomicalStructure"}, {"text": "myometrium", "type": "AnatomicalStructure"}, {"text": "gynecological disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: When compared to non - pregnant myometrium , pregnant myometrium showed stronger inhibition of NIOK by quinidine and increased immunohistochemical expression of TASK - 2 .

Example answer:
{"entities": [{"text": "non - pregnant", "type": "Finding"}, {"text": "myometrium", "type": "AnatomicalStructure"}, {"text": "pregnant", "type": "AnatomicalStructure"}, {"text": "NIOK", "type": "BiologicFunction"}, {"text": "quinidine", "type": "Chemical"}, {"text": "TASK - 2", "type": "Chemical"}]}

Example input:
Sentence: In this study , we tried to show the mechanisms of relaxation via TASK - 2 channels in marine myometrium .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "TASK - 2 channels", "type": "Chemical"}, {"text": "myometrium", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Myometrial relaxation of mice via expression of two pore domain acid sensitive K ( + ) ( TASK - 2 ) channels Myometrial relaxation of mouse via expression of two - pore domain acid sensitive ( TASK ) channels was studied .

Example answer:
{"entities": [{"text": "Myometrial", "type": "SpatialConcept"}, {"text": "mice", "type": "Eukaryote"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "two pore domain acid sensitive K ( + ) ( TASK - 2 ) channels", "type": "Chemical"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "two - pore domain acid sensitive ( TASK ) channels", "type": "Chemical"}, {"text": "studied", "type": "ResearchActivity"}]}

Input:
Sentence: Finally , TASK - 2 inhibitors induced strong myometrial contraction even in the presence of L - methionine , a known inhibitor of stretch - activated channels in the longitudinal myometrium of mouse .

## Item MedMentions:test:1672
Example input:
Sentence: Thirteen age - and sex - matched healthy controls were chosen .

Example answer:
{"entities": []}

Example input:
Sentence: Levels of the soluble LDL receptor - relative LR11 decrease in overweight individuals with type 2 diabetes upon diet - induced weight loss Cardiovascular disease ( CVD ) is a major complication in patients with type 2 diabetes ( T2D ) , especially in those with obesity .

Example answer:
{"entities": [{"text": "LDL receptor - relative LR11", "type": "Chemical"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "Cardiovascular disease", "type": "BiologicFunction"}, {"text": "CVD", "type": "BiologicFunction"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "T2D", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}]}

Example input:
Sentence: Plasma soluble low density lipoprotein receptor - relative with 11 ligand - binding repeats ( sLR11 ) plays a role in the development of atherosclerosis and has been linked to the metabolism of triglyceride - rich lipoproteins , adiposity , and vascular complications in T2D .

Example answer:
{"entities": [{"text": "Plasma", "type": "BodySubstance"}, {"text": "low density lipoprotein receptor - relative with 11 ligand - binding repeats", "type": "Chemical"}, {"text": "sLR11", "type": "Chemical"}, {"text": "atherosclerosis", "type": "BiologicFunction"}, {"text": "metabolism", "type": "BiologicFunction"}, {"text": "triglyceride - rich lipoproteins", "type": "Chemical"}, {"text": "T2D", "type": "BiologicFunction"}]}

Example input:
Sentence: Weight loss dieting in overweight and obese individuals with T2D resulted in a reduction in plasma sLR11 levels that was associated with improvements in lipid - profile and glycemic state .

Example answer:
{"entities": [{"text": "Weight loss dieting", "type": "HealthCareActivity"}, {"text": "obese", "type": "BiologicFunction"}, {"text": "T2D", "type": "BiologicFunction"}, {"text": "plasma", "type": "BodySubstance"}, {"text": "sLR11", "type": "Chemical"}, {"text": "lipid - profile", "type": "HealthCareActivity"}]}

Example input:
Sentence: Median plasma sLR11 levels of the T2D study - group at baseline ( 15 . 4 ng / mL ( IQR 12 . 9 - 19 . 5 ) ) were higher than in controls ( 10 . 2 ( IQR : 8 . 7 - 12 . 2 ) ng / mL ; p = 0 .

Example answer:
{"entities": [{"text": "plasma", "type": "BodySubstance"}, {"text": "sLR11", "type": "Chemical"}, {"text": "T2D", "type": "BiologicFunction"}, {"text": "study - group", "type": "PopulationGroup"}]}

Example input:
Sentence: We aimed to determine the effect of diet - induced weight loss on plasma sLR11 levels in overweight and obese individuals with T2D .

Example answer:
{"entities": [{"text": "plasma", "type": "BodySubstance"}, {"text": "sLR11", "type": "Chemical"}, {"text": "obese", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "T2D", "type": "BiologicFunction"}]}

Example input:
Sentence: The changes in non - HDL cholesterol and HbA1c together explained 24 % of the variance of sLR11 reduction ( p = 0 . 001 ) .

Example answer:
{"entities": [{"text": "non - HDL cholesterol", "type": "Chemical"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "sLR11", "type": "Chemical"}]}

Example input:
Sentence: sLR11 levels were reduced to 13 . 3 ng / mL ( IQR 11 .

Example answer:
{"entities": [{"text": "sLR11", "type": "Chemical"}]}

Example input:
Sentence: Changes in sLR11 levels positively associated with changes in non - HDL cholesterol ( B = 1 . 54 , R ( 2 ) = 0 . 17 , p = 0 . 001 ) and HbA1c ( B = 0 . 07 , R ( 2 ) = 0 .

Example answer:
{"entities": [{"text": "sLR11", "type": "Chemical"}, {"text": "non - HDL cholesterol", "type": "Chemical"}, {"text": "HbA1c", "type": "Chemical"}]}

Example input:
Sentence: Plasma sLR11 levels were determined in 64 individuals with T2D and BMI > 27 kg / m ( 2 ) before and after a 20 - week weight loss diet .

Example answer:
{"entities": [{"text": "Plasma", "type": "BodySubstance"}, {"text": "sLR11", "type": "Chemical"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "T2D", "type": "BiologicFunction"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "weight loss diet", "type": "HealthCareActivity"}]}

Input:
Sentence: As a reference , sLR11 levels were also determined in 64 healthy , non - obese controls , matched as a group for age and sex .

## Item MedMentions:test:1481
Example input:
Sentence: In this study , 188 F8 recombinant inbred lines ( RILs ) , derived from a intraspecific cross between HS46 and MARCABUCAG8US - 1 - 88 were genotyped by the cotton 63 K single nucleotide polymorphism ( SNP ) assay .

Example answer:
{"entities": [{"text": "188 F8", "type": "Eukaryote"}, {"text": "recombinant inbred lines", "type": "Eukaryote"}, {"text": "RILs", "type": "Eukaryote"}, {"text": "cross", "type": "BiologicFunction"}, {"text": "HS46", "type": "Eukaryote"}, {"text": "MARCABUCAG8US - 1 - 88", "type": "Eukaryote"}, {"text": "cotton", "type": "Eukaryote"}, {"text": "single nucleotide polymorphism ( SNP ) assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: In this study , we combine multiplex PCR , custom designed dual indexing and Miseq sequencing for high throughput SNP - profiling of 457 malaria infections from Guinea - Bissau , at the cost of 10 USD per sample .

Example answer:
{"entities": [{"text": "multiplex PCR", "type": "HealthCareActivity"}, {"text": "custom designed dual indexing", "type": "ResearchActivity"}, {"text": "Miseq", "type": "IntellectualProduct"}, {"text": "sequencing", "type": "HealthCareActivity"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "malaria", "type": "BiologicFunction"}, {"text": "infections", "type": "BiologicFunction"}, {"text": "Guinea - Bissau", "type": "SpatialConcept"}]}

Example input:
Sentence: A 1784 . 28 cM ( centimorgans ) linkage map , harboring 2618 polymorphic SNP markers , was constructed , which had 0 . 68 cM per marker density .

Example answer:
{"entities": [{"text": "linkage map", "type": "HealthCareActivity"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "markers", "type": "BiologicFunction"}, {"text": "marker", "type": "BiologicFunction"}]}

Example input:
Sentence: In this case - control genetic study , 300 cases of psoriasis and 300 age and gender matched controls were genotyped for CRP SNP rs1205 using Taq Man 5 ' allele discrimination assay at Jawaharlal Institute of Postgraduate Medical Education and Research , Puducherry , India from February 2014 to January 2016 .

Example answer:
{"entities": [{"text": "case - control", "type": "ResearchActivity"}, {"text": "genetic study", "type": "ResearchActivity"}, {"text": "psoriasis", "type": "BiologicFunction"}, {"text": "CRP SNP rs1205", "type": "AnatomicalStructure"}, {"text": "Taq Man 5 ' allele discrimination assay", "type": "HealthCareActivity"}, {"text": "Jawaharlal Institute of Postgraduate Medical Education and Research", "type": "Organization"}, {"text": "India", "type": "SpatialConcept"}]}

Example input:
Sentence: With this aim , we selected 11 variants of 5 genes ( GJB2 , SLC26A4 , MTRNR1 , TMPRSS3 , and CDH23 ) showing high prevalence with varying degrees in Koreans and developed the U - TOP ™ HL Genotyping Kit , a real - time PCR -based method using the MeltingArray technique and peptide nucleic acid probes .

Example answer:
{"entities": [{"text": "variants", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "GJB2", "type": "AnatomicalStructure"}, {"text": "SLC26A4", "type": "AnatomicalStructure"}, {"text": "MTRNR1", "type": "AnatomicalStructure"}, {"text": "TMPRSS3", "type": "AnatomicalStructure"}, {"text": "CDH23", "type": "AnatomicalStructure"}, {"text": "Koreans", "type": "PopulationGroup"}, {"text": "U - TOP ™ HL Genotyping Kit", "type": "MedicalDevice"}, {"text": "real - time PCR", "type": "ResearchActivity"}, {"text": "MeltingArray technique", "type": "ResearchActivity"}, {"text": "peptide nucleic acid", "type": "Chemical"}, {"text": "probes", "type": "MedicalDevice"}]}

Example input:
Sentence: Here , we describe all relevant aspects when developing an assay for a new SNP or STR using either TaqMan or allele - specific genotyping , respectively , such as primer and probe design , optimization of reaction conditions , the experimental procedure for typing hundreds of samples , and finally the data evaluation .

Example answer:
{"entities": [{"text": "assay", "type": "HealthCareActivity"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "STR", "type": "Chemical"}, {"text": "TaqMan", "type": "HealthCareActivity"}, {"text": "allele - specific genotyping", "type": "HealthCareActivity"}, {"text": "primer", "type": "Chemical"}, {"text": "probe", "type": "Chemical"}, {"text": "experimental procedure for typing", "type": "HealthCareActivity"}, {"text": "evaluation", "type": "HealthCareActivity"}]}

Example input:
Sentence: The following single nucleotide polymorphisms ( SNPs ) were genotyped ; C1236 T , C3435 T , G2677 T / A in MDR1 gene and A6986 G in CYP3A5 gene , using PCR - RFLP method and validated by direct gene sequencing .

Example answer:
{"entities": [{"text": "single nucleotide polymorphisms", "type": "SpatialConcept"}, {"text": "SNPs", "type": "SpatialConcept"}, {"text": "genotyped", "type": "HealthCareActivity"}, {"text": "C1236 T", "type": "SpatialConcept"}, {"text": "C3435 T", "type": "SpatialConcept"}, {"text": "G2677 T", "type": "SpatialConcept"}, {"text": "A", "type": "SpatialConcept"}, {"text": "MDR1 gene", "type": "AnatomicalStructure"}, {"text": "A6986 G", "type": "SpatialConcept"}, {"text": "CYP3A5 gene", "type": "AnatomicalStructure"}, {"text": "PCR - RFLP method", "type": "HealthCareActivity"}, {"text": "gene sequencing", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the first phase , the rs3757247 SNP was genotyped in 358 UK AAD subjects and 166 local control subjects .

Example answer:
{"entities": [{"text": "rs3757247 SNP", "type": "SpatialConcept"}, {"text": "AAD", "type": "BiologicFunction"}, {"text": "subjects", "type": "PopulationGroup"}]}

Example input:
Sentence: A total of 4 , 976 SNPs from the 9 K iSelect array were used in the study for the analysis of population structure , linkage disequilibrium ( LD ) and genome - wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "SNPs", "type": "SpatialConcept"}, {"text": "study", "type": "ResearchActivity"}, {"text": "genome - wide association study", "type": "ResearchActivity"}, {"text": "GWAS", "type": "ResearchActivity"}]}

Example input:
Sentence: SNPs were analyzed in 340 healthy unrelated Mestizos from western Mexico by polymerase chain reaction - restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "SNPs", "type": "SpatialConcept"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "unrelated", "type": "Finding"}, {"text": "western Mexico", "type": "SpatialConcept"}, {"text": "polymerase chain reaction", "type": "ResearchActivity"}, {"text": "restriction fragment length polymorphism", "type": "HealthCareActivity"}]}

Input:
Sentence: Eight SNPs were selected and genotyped using MassARRAY technology ( Sequenom , San Diego , CA , USA ) .

## Item MedMentions:test:1244
Example input:
Sentence: In 2015 we treated two patients for very large symptomatic GCH ( 15 . 7 and 25 . 0 cm ) with bipolar RFA during open laparotomy .

Example answer:
{"entities": [{"text": "GCH", "type": "BiologicFunction"}, {"text": "bipolar RFA", "type": "HealthCareActivity"}, {"text": "open laparotomy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Twelve patients with hemiparesis ( 10 - 20 years ) and 8 typically developing subjects ( 8 - 17 years ) participated .

Example answer:
{"entities": [{"text": "hemiparesis", "type": "Finding"}, {"text": "subjects", "type": "PopulationGroup"}]}

Example input:
Sentence: From November 2012 to January 2015 , 50 - to 80 - year - old patients with moderate to severe WMLs or more than four lacunar infarctions and cognitive complaints , excluding those with large vascular diseases diagnosed by transcranial cerebral Doppler , were recruited .

Example answer:
{"entities": [{"text": "WMLs", "type": "Finding"}, {"text": "lacunar infarctions", "type": "BiologicFunction"}, {"text": "cognitive complaints", "type": "BiologicFunction"}, {"text": "vascular diseases", "type": "BiologicFunction"}, {"text": "transcranial cerebral Doppler", "type": "HealthCareActivity"}]}

Example input:
Sentence: Conservatively treated patients with supratentorial ICH , admitted to our hospital over a 5 - year period ( 2008 - 2012 ) , were retrospectively analyzed .

Example answer:
{"entities": [{"text": "Conservatively treated", "type": "HealthCareActivity"}, {"text": "supratentorial", "type": "SpatialConcept"}, {"text": "ICH", "type": "Finding"}, {"text": "hospital", "type": "Organization"}, {"text": "retrospectively analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: She was subsequently diagnosed with an intracranial hemorrhage in the distribution of the right basal ganglia .

Example answer:
{"entities": [{"text": "diagnosed", "type": "Finding"}, {"text": "intracranial hemorrhage", "type": "BiologicFunction"}, {"text": "right basal ganglia", "type": "AnatomicalStructure"}]}

Example input:
Sentence: RESULTS Between May 2014 and September 2015 , the authors used this technique in 17 cases : 16 cases of middle cerebral artery occlusion ( including 5 cases of internal carotid artery occlusion ) and 1 case of basilar artery occlusion ( age range 36 - 88 years , mean age 74 . 7 years , 13 men ) .

Example answer:
{"entities": [{"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "middle cerebral artery occlusion", "type": "AnatomicalStructure"}, {"text": "internal carotid artery occlusion", "type": "BiologicFunction"}, {"text": "basilar artery occlusion", "type": "AnatomicalStructure"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: GCS score on admission together with the baseline volume and localization of the hemorrhage are strong predictors for 30 - day mortality in patients with spontaneous primary intracerebral hemorrhage , and by relying on them it is possible to identify high - risk patients with poor short - term outcome .

Example answer:
{"entities": [{"text": "GCS", "type": "IntellectualProduct"}, {"text": "admission", "type": "HealthCareActivity"}, {"text": "hemorrhage", "type": "BiologicFunction"}, {"text": "intracerebral hemorrhage", "type": "Finding"}, {"text": "high - risk", "type": "Finding"}]}

Example input:
Sentence: In total , 210 patients with stage II - III chronic limb ischemia ( according to the Fontaine classification modified by AV Pokrovsky ) in 33 healthcare facilities in Russia and the Ukraine were enrolled in the study .

Example answer:
{"entities": [{"text": "limb", "type": "AnatomicalStructure"}, {"text": "ischemia", "type": "BiologicFunction"}, {"text": "Fontaine classification", "type": "IntellectualProduct"}, {"text": "healthcare facilities", "type": "Organization"}, {"text": "Russia", "type": "SpatialConcept"}, {"text": "Ukraine", "type": "SpatialConcept"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Upon completion of the literature review , eight GS cases were found to have been treated surgically with the minimum patient age being 9 years .

Example answer:
{"entities": [{"text": "literature review", "type": "IntellectualProduct"}, {"text": "GS", "type": "BiologicFunction"}, {"text": "surgically", "type": "HealthCareActivity"}]}

Example input:
Sentence: In isolated lobar ICH , median hematoma - volume decreased from rostral ( frontal , 22 . 4 mL [ 7 . 3 - 55 . 5 mL ] ) to caudal ( occipital , 7 . 1 mL [ 5 . 2 - 16 . 4 mL ] ; P = 0 . 045 ) , whereas the proportion of patients with favorable outcome increased ( frontal : 23 / 63 [ 36 . 5 % ] versus occipital : 10 / 12 [ 83 . 3 % ] ; P = 0 .

Example answer:
{"entities": [{"text": "hematoma", "type": "BiologicFunction"}, {"text": "rostral", "type": "SpatialConcept"}, {"text": "frontal", "type": "AnatomicalStructure"}, {"text": "caudal", "type": "SpatialConcept"}, {"text": "occipital", "type": "AnatomicalStructure"}, {"text": "favorable outcome", "type": "Finding"}]}

Input:
Sentence: From 342 patients ( mean age : 67 years , mean Glasgow Coma Scale [ GCS ] on admission : 9 , mean ICH volume : 62 . 19 ml , most common hematoma location : basal ganglia [ 43 . 9 % ] ) , 102 received surgical and 240 conservative treatment .

## Item MedMentions:test:1381
Example input:
Sentence: All adult patients scheduled for elective foot or ankle surgery by 1 of 6 orthopaedic foot and ankle surgeons were screened for inclusion over 8 months .

Example answer:
{"entities": [{"text": "foot", "type": "HealthCareActivity"}, {"text": "ankle surgery", "type": "HealthCareActivity"}, {"text": "orthopaedic foot and ankle surgeons", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: 9 points , respectively , at 12 and 24 months after surgery ( p < 0 . 05 ) .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Following revision surgery , all patients reported resolution of the preoperative pain , as well as satisfactory outcome measures ( mean scores : The Western Ontario and McMaster Universities Arthritis Index [ WOMAC ] 84 . 6 , oxford hip score 84 . 7 , Short Form Health Survey ( SF - 16 ) 51 , University of California , Los Angeles ( UCLA ) 7 . 3 ) .

Example answer:
{"entities": [{"text": "revision surgery", "type": "HealthCareActivity"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "pain", "type": "Finding"}, {"text": "Western Ontario and McMaster Universities Arthritis Index", "type": "IntellectualProduct"}, {"text": "WOMAC", "type": "IntellectualProduct"}, {"text": "oxford hip score", "type": "ClinicalAttribute"}, {"text": "Short Form Health Survey", "type": "ResearchActivity"}, {"text": "SF - 16", "type": "ResearchActivity"}, {"text": "University of California", "type": "Organization"}, {"text": "Los Angeles", "type": "SpatialConcept"}, {"text": "UCLA", "type": "Organization"}]}

Example input:
Sentence: Baseline score - adjusted comparison between groups showed that the postoperative median ASES scores ( atraumatic , 95 . 8 ; traumatic , 99 . 9 ) and SANE scores ( atraumatic , 86 . 5 ; traumatic , 98 . 0 ) were significantly more improved in patients with traumatic PSI ( P = .01 and P = .012 , respectively ) .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}, {"text": "median ASES scores", "type": "IntellectualProduct"}, {"text": "atraumatic", "type": "InjuryOrPoisoning"}, {"text": "traumatic", "type": "InjuryOrPoisoning"}, {"text": "SANE scores", "type": "IntellectualProduct"}]}

Example input:
Sentence: Subjective evaluations were obtained with the American Shoulder and Elbow Surgeons ( ASES ) ; Quick Disabilities of the Arm , Shoulder and Hand ; Single Assessment Numeric Evaluation ( SANE ) ; and Short Form 12 Physical Component Summary scores preoperatively and after a minimum 2 - year follow - up postoperatively .

Example answer:
{"entities": [{"text": "American Shoulder and Elbow Surgeons", "type": "IntellectualProduct"}, {"text": "ASES", "type": "IntellectualProduct"}, {"text": "Quick Disabilities of the Arm , Shoulder and Hand", "type": "ClinicalAttribute"}, {"text": "Single Assessment Numeric Evaluation ( SANE )", "type": "IntellectualProduct"}, {"text": "Short Form 12 Physical Component Summary scores", "type": "IntellectualProduct"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Preoperative mean visual analog scale was 6 .

Example answer:
{"entities": [{"text": "Preoperative mean visual analog scale", "type": "HealthCareActivity"}]}

Example input:
Sentence: The differences between the two groups were also significant regarding wrist functional scores at 6 weeks , but not significant at 3 and 12 month after operation .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}, {"text": "operation", "type": "HealthCareActivity"}]}

Example input:
Sentence: All patients were evaluated clinically with American Knee Society Score ( AKSS ) and visual analogue scale ( VAS ) for the pain before the treatment and after 3 months .

Example answer:
{"entities": [{"text": "visual analogue scale", "type": "HealthCareActivity"}, {"text": "VAS", "type": "HealthCareActivity"}, {"text": "pain", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Further improvements were detected at 24 months ( AOFAS , from 57 . 1 ± 14 . 9 before surgery to 86 . 6 ± 10 .

Example answer:
{"entities": [{"text": "AOFAS", "type": "IntellectualProduct"}]}

Example input:
Sentence: Preoperatively , all patients completed the Hospital for Special Surgery Foot & Ankle Surgery Expectations Survey in addition to the Foot & Ankle Outcome Score ( FAOS ) , Short Form ( SF ) - 12 , Patient Health Questionnaire ( PHQ ) - 8 , Generalized Anxiety Disorder 7 - item scale ( GAD - 7 ) , and pain visual analog scale ( VAS ) .

Example answer:
{"entities": [{"text": "Hospital for Special Surgery Foot & Ankle Surgery Expectations Survey", "type": "IntellectualProduct"}, {"text": "Short Form ( SF ) - 12", "type": "IntellectualProduct"}, {"text": "Patient Health Questionnaire", "type": "IntellectualProduct"}, {"text": "PHQ", "type": "IntellectualProduct"}, {"text": "Generalized Anxiety Disorder 7 - item scale", "type": "IntellectualProduct"}, {"text": "GAD - 7", "type": "IntellectualProduct"}, {"text": "pain visual analog scale", "type": "HealthCareActivity"}, {"text": "VAS", "type": "HealthCareActivity"}]}

Input:
Sentence: Patients were evaluated pre - operatively and at 6 , 12 , and 24 months post - operatively using the American Orthopedic Foot and Ankle Society ( AOFAS ) score , the visual analog scale , and the SF - 12 ( Short Form - 12 ) .

## Item MedMentions:test:1278
Example input:
Sentence: A potent inhibitor , JQ1 , which effectively disrupts the interaction of BET proteins with acetylated histones , preferentially suppresses transcription of the MYC gene .

Example answer:
{"entities": [{"text": "potent inhibitor", "type": "Chemical"}, {"text": "JQ1", "type": "Chemical"}, {"text": "BET proteins", "type": "Chemical"}, {"text": "acetylated histones", "type": "BiologicFunction"}, {"text": "transcription", "type": "BiologicFunction"}, {"text": "MYC gene", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Nicotine Suppressed Fetal Adrenal StAR Expression via YY1 Mediated - Histone Deacetylation Modification Mechanism Steroidogenic acute regulatory ( StAR ) protein plays a pivotal role in steroidogenesis .

Example answer:
{"entities": [{"text": "Nicotine", "type": "Chemical"}, {"text": "Fetal Adrenal", "type": "AnatomicalStructure"}, {"text": "StAR", "type": "Chemical"}, {"text": "Expression", "type": "BiologicFunction"}, {"text": "YY1", "type": "Chemical"}, {"text": "Histone Deacetylation", "type": "BiologicFunction"}, {"text": "Steroidogenic acute regulatory ( StAR ) protein", "type": "Chemical"}, {"text": "steroidogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Co - ChIP enables genome - wide mapping of histone mark co - occurrence at single - molecule resolution Histone modifications play an important role in chromatin organization and transcriptional regulation , but despite the large amount of genome - wide histone modification data collected in different cells and tissues , little is known about co - occurrence of modifications on the same nucleosome .

Example answer:
{"entities": [{"text": "Co - ChIP", "type": "HealthCareActivity"}, {"text": "genome - wide mapping", "type": "ResearchActivity"}, {"text": "histone mark", "type": "SpatialConcept"}, {"text": "Histone modifications", "type": "BiologicFunction"}, {"text": "chromatin organization", "type": "BiologicFunction"}, {"text": "transcriptional regulation", "type": "BiologicFunction"}, {"text": "genome - wide", "type": "AnatomicalStructure"}, {"text": "histone modification", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "modifications", "type": "BiologicFunction"}, {"text": "nucleosome", "type": "Chemical"}]}

Example input:
Sentence: StAR and YY1 expression were analyzed by real - time PCR , immunohistochemistry , and Western blotting .

Example answer:
{"entities": [{"text": "StAR", "type": "Chemical"}, {"text": "YY1", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "real - time PCR", "type": "ResearchActivity"}, {"text": "immunohistochemistry", "type": "HealthCareActivity"}, {"text": "Western blotting", "type": "HealthCareActivity"}]}

Example input:
Sentence: Chromatin immunoprecipitation ( ChIP ) showed approximately 3 - fold enrichment of RANKL - specific DNA in anti - SOX5 immunoprecipitate in IL - 6 treated MH7A cells as compared to untreated cells .

Example answer:
{"entities": [{"text": "Chromatin immunoprecipitation", "type": "HealthCareActivity"}, {"text": "ChIP", "type": "HealthCareActivity"}, {"text": "RANKL - specific DNA", "type": "Chemical"}, {"text": "anti - SOX5 immunoprecipitate", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "MH7A cells", "type": "AnatomicalStructure"}, {"text": "untreated cells", "type": "Finding"}]}

Example input:
Sentence: Chromatin immunoprecipitation ( ChIP ) showed that MS188 directly bound to the promoter of CYP703A2 and luciferase - inducible assay showed that MS188 activated the expression of CYP703A2 .

Example answer:
{"entities": [{"text": "Chromatin immunoprecipitation", "type": "HealthCareActivity"}, {"text": "ChIP", "type": "HealthCareActivity"}, {"text": "MS188", "type": "Chemical"}, {"text": "promoter", "type": "Chemical"}, {"text": "CYP703A2", "type": "AnatomicalStructure"}, {"text": "luciferase - inducible", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "CYP703A2", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , in nicotine - treated NCI - H295A cells , nicotine enhanced YY1 expression and inhibited StAR expression .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "NCI - H295A cells", "type": "AnatomicalStructure"}, {"text": "YY1", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "StAR", "type": "Chemical"}]}

Example input:
Sentence: These data indicated that YY1 -medicated histone deacetylation modification in StAR promoters might play an important role in the inhibitory effect of nicotine on StAR expression .

Example answer:
{"entities": [{"text": "YY1", "type": "Chemical"}, {"text": "histone deacetylation", "type": "BiologicFunction"}, {"text": "StAR promoters", "type": "AnatomicalStructure"}, {"text": "nicotine", "type": "Chemical"}, {"text": "StAR", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}]}

Example input:
Sentence: ChIP assay showed that there was a decreasing trend for histone acetylation at the StAR promoter in fetal adrenal glands , whereas H3 acetyl - K14 at the YY1 promoter presented an increasing trend following nicotine exposure .

Example answer:
{"entities": [{"text": "ChIP", "type": "HealthCareActivity"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "decreasing", "type": "Finding"}, {"text": "histone acetylation", "type": "BiologicFunction"}, {"text": "StAR promoter", "type": "AnatomicalStructure"}, {"text": "fetal adrenal glands", "type": "AnatomicalStructure"}, {"text": "H3 acetyl - K14", "type": "BiologicFunction"}, {"text": "YY1 promoter", "type": "AnatomicalStructure"}, {"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: Histone modifications and the interactions between the YY1 and StAR promoter were assessed using chromatin immunoprecipitation ( ChIP ) .

Example answer:
{"entities": [{"text": "Histone modifications", "type": "BiologicFunction"}, {"text": "YY1", "type": "Chemical"}, {"text": "StAR promoter", "type": "AnatomicalStructure"}, {"text": "chromatin immunoprecipitation", "type": "HealthCareActivity"}, {"text": "ChIP", "type": "HealthCareActivity"}]}

Input:
Sentence: ChIP assay showed that histone acetylation decreased at the StAR promoter in NCI - H295A cells and that the interaction between the YY1 and StAR promoter increased .

## Item MedMentions:test:1532
Example input:
Sentence: Protective effect of epigallocatechin - 3 - gallate ( EGCG ) via Nrf2 pathway against oxalate -induced epithelial mesenchymal transition ( EMT ) of renal tubular cells This study evaluated effect of oxalate on epithelial mesenchymal transition ( EMT ) and potential anti - fibrotic property of epigallocatechin - 3 - gallate ( EGCG ) .

Example answer:
{"entities": [{"text": "epigallocatechin - 3 - gallate", "type": "Chemical"}, {"text": "EGCG", "type": "Chemical"}, {"text": "Nrf2", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "oxalate", "type": "Chemical"}, {"text": "epithelial mesenchymal transition", "type": "BiologicFunction"}, {"text": "EMT", "type": "BiologicFunction"}, {"text": "renal", "type": "AnatomicalStructure"}, {"text": "study", "type": "ResearchActivity"}, {"text": "anti - fibrotic property", "type": "Finding"}]}

Example input:
Sentence: Anti - bacterial and Anti - biofilm Evaluation of Thiazolopyrimidinone Derivatives Targeting the Histidine Kinase YycG Protein of Staphylococcus epidermidis Staphylococcus epidermidis is one of the most important opportunistic pathogens in nosocomial infections .

Example answer:
{"entities": [{"text": "Anti - bacterial and Anti - biofilm Evaluation", "type": "BiologicFunction"}, {"text": "Thiazolopyrimidinone Derivatives", "type": "Chemical"}, {"text": "Histidine Kinase", "type": "Chemical"}, {"text": "YycG Protein of Staphylococcus epidermidis", "type": "Chemical"}, {"text": "Staphylococcus epidermidis", "type": "Bacterium"}, {"text": "nosocomial infections", "type": "BiologicFunction"}]}

Example input:
Sentence: mutans through interaction with lipoteichoic acid ( LTA ) , but without antibacterial or biofilm dispersal abilities . ( - ) - Epigallocatechin gallate ( EGCG ) is the most abundant constituent of tea catechins that has the greatest anti - infective potential to inhibit the growth of various microorganisms and biofilm formation .

Example answer:
{"entities": [{"text": "mutans", "type": "Bacterium"}, {"text": "lipoteichoic acid", "type": "Chemical"}, {"text": "LTA", "type": "Chemical"}, {"text": "antibacterial", "type": "Finding"}, {"text": "biofilm", "type": "Bacterium"}, {"text": "dispersal abilities", "type": "SpatialConcept"}, {"text": "( - ) - Epigallocatechin gallate", "type": "Chemical"}, {"text": "EGCG", "type": "Chemical"}, {"text": "tea", "type": "Food"}, {"text": "catechins", "type": "Chemical"}, {"text": "anti - infective potential", "type": "Finding"}, {"text": "inhibit the growth", "type": "BiologicFunction"}, {"text": "biofilm formation", "type": "BiologicFunction"}]}

Example input:
Sentence: In addition , the interaction among EGCG , LL - 37 , and LTA of S .

Example answer:
{"entities": [{"text": "EGCG", "type": "Chemical"}, {"text": "LL - 37", "type": "Chemical"}, {"text": "LTA", "type": "Chemical"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: We recently showed that human cathelicidin LL - 37 exhibits inhibitory effects on biofilm formation of S .

Example answer:
{"entities": [{"text": "human cathelicidin LL - 37", "type": "Chemical"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: In addition , quartz crystal microbalance analysis revealed that LL - 37 interacted with EGCG and promoted binding between EGCG and LTA of S .

Example answer:
{"entities": [{"text": "quartz crystal microbalance analysis", "type": "ResearchActivity"}, {"text": "LL - 37", "type": "Chemical"}, {"text": "EGCG", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "LTA", "type": "Chemical"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: Human cathelicidin LL - 37 enhance the antibiofilm effect of EGCG on Streptococcus mutans Streptococcus mutans forms biofilms as a resistance mechanism against antimicrobial agents in the human oral cavity .

Example answer:
{"entities": [{"text": "Human cathelicidin LL - 37", "type": "Chemical"}, {"text": "antibiofilm effect", "type": "Finding"}, {"text": "EGCG", "type": "Chemical"}, {"text": "Streptococcus mutans", "type": "Bacterium"}, {"text": "biofilms", "type": "Bacterium"}, {"text": "antimicrobial agents", "type": "Chemical"}, {"text": "human", "type": "Eukaryote"}, {"text": "oral cavity", "type": "SpatialConcept"}]}

Example input:
Sentence: The antibiofilm effect of EGCG with and without LL - 37 was analyzed by the minimum biofilm eradication concentration assay and confirmed using field emission - scanning electron microscopy .

Example answer:
{"entities": [{"text": "antibiofilm effect", "type": "Finding"}, {"text": "EGCG", "type": "Chemical"}, {"text": "LL - 37", "type": "Chemical"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "biofilm", "type": "Bacterium"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "emission - scanning electron microscopy", "type": "HealthCareActivity"}]}

Example input:
Sentence: LL - 37 effectively enhanced the bactericidal activity of EGCG against biofilm formation and preformed biofilms as determined by quantitative crystal violet staining and field emission - scanning electron microscopy .

Example answer:
{"entities": [{"text": "LL - 37", "type": "Chemical"}, {"text": "bactericidal activity", "type": "BiologicFunction"}, {"text": "EGCG", "type": "Chemical"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "biofilms", "type": "Bacterium"}, {"text": "crystal violet", "type": "Chemical"}, {"text": "staining", "type": "HealthCareActivity"}, {"text": "emission - scanning electron microscopy", "type": "HealthCareActivity"}]}

Example input:
Sentence: We show that LL - 37 enhances the antibiofilm effect of EGCG on S .

Example answer:
{"entities": [{"text": "LL - 37", "type": "Chemical"}, {"text": "antibiofilm effect", "type": "Finding"}, {"text": "EGCG", "type": "Chemical"}, {"text": "S .", "type": "Bacterium"}]}

Input:
Sentence: Therefore , in this study , we evaluated whether LL - 37 interacts with EGCG to enhance the antibiofilm effect of EGCG on S .

## Item MedMentions:test:1701
Example input:
Sentence: On phenotyping all training animals for both C - LA and CFS , accuracy for CFS increased to 0 . 18 ; however , when validation animals were also phenotyped for C - LA , there was no substantial increase in accuracy .

Example answer:
{"entities": [{"text": "training animals", "type": "Eukaryote"}, {"text": "validation", "type": "ResearchActivity"}, {"text": "animals", "type": "Eukaryote"}, {"text": "no", "type": "Finding"}]}

Example input:
Sentence: In the validation stage , successful linearity ( R ( 2 ) > 0 . 999 ) , recoveries ( between 71 and 117 % for most analytes ) , precision ( RSD lower than 21 % ) and limits of detection and quantification ( LOD and LOQ , lower than 0 . 4 and 1 .

Example answer:
{"entities": [{"text": "validation", "type": "ResearchActivity"}, {"text": "LOQ", "type": "ResearchActivity"}]}

Example input:
Sentence: Methods Participants were randomized in a 2 : 1 ratio for each active arm relative to control , with a targeted 188 participants in total .

Example answer:
{"entities": [{"text": "Methods", "type": "IntellectualProduct"}, {"text": "Participants", "type": "PopulationGroup"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: There is a positive correlation ( r = 0 . 80 ) and moderate agreement ( κ = 0 . 509 ) of grading with PC - MRI and 3D - CISS sequences .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "grading", "type": "IntellectualProduct"}, {"text": "PC - MRI", "type": "HealthCareActivity"}]}

Example input:
Sentence: On a Bland - Altman plot , the bias and precision between these two methods was 19 .

Example answer:
{"entities": [{"text": "Bland - Altman plot", "type": "IntellectualProduct"}, {"text": "methods", "type": "IntellectualProduct"}]}

Example input:
Sentence: The experiments were carried on 21 real patient subjects , and the proposed method achieves an averaged section - based evaluation ( SBE ) of 89 . 90 % , an averaged sensitivity of 91 . 51 % , and an averaged specificity of 88 . 47 % .

Example answer:
{"entities": [{"text": "experiments", "type": "ResearchActivity"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "section - based evaluation", "type": "HealthCareActivity"}, {"text": "SBE", "type": "HealthCareActivity"}]}

Example input:
Sentence: An additional 59 adults participated in data collection where the accuracy of the screening tool was evaluated ( aim 2 ) .

Example answer:
{"entities": [{"text": "data collection", "type": "ResearchActivity"}, {"text": "screening tool", "type": "IntellectualProduct"}]}

Example input:
Sentence: Participants who crossed over ( n = 11 ) showed no statistically significant improvements in a second round of treatment , regardless of condition .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "crossed over", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The positive and negative predictive values were 100 % , and this method showed perfect agreement with Sanger sequencing , with a Kappa value of 1 . 00 .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "negative", "type": "Finding"}, {"text": "Sanger sequencing", "type": "ResearchActivity"}, {"text": "Kappa", "type": "IntellectualProduct"}]}

Example input:
Sentence: The accuracy of the proposed segmentation framework is quantitatively assessed using two public databases ( ISBI VESSEL12 challenge and MICCAI LOLA11 challenge ) and our own database with , respectively , 20 , 55 , and 30 CT images of various lung pathologies acquired with different scanners and protocols .

Example answer:
{"entities": [{"text": "segmentation", "type": "HealthCareActivity"}, {"text": "databases", "type": "IntellectualProduct"}, {"text": "ISBI VESSEL12 challenge", "type": "IntellectualProduct"}, {"text": "MICCAI LOLA11 challenge", "type": "IntellectualProduct"}, {"text": "database", "type": "IntellectualProduct"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "images", "type": "IntellectualProduct"}, {"text": "lung", "type": "AnatomicalStructure"}, {"text": "scanners", "type": "MedicalDevice"}, {"text": "protocols", "type": "HealthCareActivity"}]}

Input:
Sentence: Similarly , the accuracy of our approach is further verified via a blind evaluation by the organizers of the LOLA11 competition , where an average overlap of 98 .

## Item MedMentions:test:1783
Example input:
Sentence: Data analysis included the use of descriptive statistics to examine the frequency and magnitude of reported issues .

Example answer:
{"entities": [{"text": "descriptive statistics", "type": "ResearchActivity"}, {"text": "issues", "type": "Finding"}]}

Example input:
Sentence: Bivariate case - control analysis was performed , using patients who died as cases ; later , analysis using a logistic regression model with variables that were associated with mortality was conducted .

Example answer:
{"entities": [{"text": "died", "type": "BiologicFunction"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "logistic regression model", "type": "IntellectualProduct"}]}

Example input:
Sentence: Descriptive statistics compared clinical and pathological variables between groups .

Example answer:
{"entities": [{"text": "Descriptive statistics", "type": "ResearchActivity"}]}

Example input:
Sentence: Due to the small study size , analyses comprised of descriptive statistics .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "statistics", "type": "ResearchActivity"}]}

Example input:
Sentence: Descriptive analysis and factor analysis were performed .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Descriptive statistics , multivariable logistic regression and multivariable cox regression analysis were utilized to assess the data .

Example answer:
{"entities": [{"text": "Descriptive statistics", "type": "ResearchActivity"}, {"text": "multivariable logistic regression", "type": "ResearchActivity"}, {"text": "multivariable cox regression analysis", "type": "IntellectualProduct"}]}

Example input:
Sentence: Descriptive statistics characterized these features and chi - square analyses were conducted to determine the relationship between select features and habits .

Example answer:
{"entities": [{"text": "chi - square analyses", "type": "IntellectualProduct"}]}

Example input:
Sentence: Descriptive statistics were used to analyse the data .

Example answer:
{"entities": [{"text": "analyse", "type": "ResearchActivity"}]}

Example input:
Sentence: The two groups were compared using standard bivariate methods .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: Descriptive statistics , bivariate analysis and logistic regression were used to analyze the data .

Example answer:
{"entities": [{"text": "Descriptive statistics", "type": "ResearchActivity"}, {"text": "logistic regression", "type": "ResearchActivity"}]}

Input:
Sentence: Descriptive and bivariate analyses were conducted to determine statistically significant differences .

## Item MedMentions:test:1837
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

## Item MedMentions:test:1706
Example input:
Sentence: We intercrossed Ret and Sema3d double  heterozygotes to generate mice with the nine possible genotypes and assessed survival by counting various genotypes , myenteric plexus presence by acetylcholinesterase staining and embryonic day 12 .

Example answer:
{"entities": [{"text": "Ret", "type": "AnatomicalStructure"}, {"text": "Sema3d", "type": "AnatomicalStructure"}, {"text": "counting various genotypes", "type": "HealthCareActivity"}, {"text": "myenteric plexus", "type": "AnatomicalStructure"}, {"text": "acetylcholinesterase staining", "type": "HealthCareActivity"}]}

Example input:
Sentence: Aged APN -KO mice developed hippocampal insulin resistance with reduced pAkt induction upon intracerebral insulin injection .

Example answer:
{"entities": [{"text": "APN", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "pAkt", "type": "Chemical"}, {"text": "insulin injection", "type": "HealthCareActivity"}]}

Example input:
Sentence: High - fidelity Glucagon - CreER mouse line generated by CRISPR - Cas9 assisted gene targeting α - cells are the second most prominent cell type in pancreatic islets and are responsible for producing glucagon to increase plasma glucose levels in times of fasting .

Example answer:
{"entities": [{"text": "Glucagon - CreER mouse line", "type": "AnatomicalStructure"}, {"text": "gene targeting", "type": "ResearchActivity"}, {"text": "α - cells", "type": "AnatomicalStructure"}, {"text": "cell type", "type": "IntellectualProduct"}, {"text": "pancreatic islets", "type": "AnatomicalStructure"}, {"text": "glucagon", "type": "Chemical"}, {"text": "plasma glucose levels", "type": "Finding"}, {"text": "fasting", "type": "Finding"}]}

Example input:
Sentence: Mice were examined for cardiac remodeling processes and the diabetic state was assessed .

Example answer:
{"entities": [{"text": "Mice", "type": "Eukaryote"}, {"text": "examined", "type": "Finding"}, {"text": "cardiac remodeling processes", "type": "BiologicFunction"}, {"text": "diabetic state", "type": "BiologicFunction"}, {"text": "assessed", "type": "HealthCareActivity"}]}

Example input:
Sentence: Despite similar fat mass and energy balance , M ( IL10 ) mice were protected from aging - associated insulin resistance with significant increases in glucose infusion rates , whole - body glucose turnover , and skeletal muscle glucose uptake ( ∼60 % ; P < 0 . 05 ) , as compared to age -matched WT mice .

Example answer:
{"entities": [{"text": "energy balance", "type": "BiologicFunction"}, {"text": "M ( IL10 )", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "aging", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "glucose", "type": "Chemical"}, {"text": "whole - body", "type": "AnatomicalStructure"}, {"text": "skeletal muscle", "type": "AnatomicalStructure"}, {"text": "glucose uptake", "type": "BiologicFunction"}, {"text": "WT mice", "type": "Eukaryote"}]}

Example input:
Sentence: To investigate , we examined glucose metabolism in 18 - mo - old transgenic mice with muscle - specific overexpression of IL - 10 ( M ( IL10 ) ) and in wild - type mice during hyperinsulinemic - euglycemic clamping .

Example answer:
{"entities": [{"text": "glucose metabolism", "type": "BiologicFunction"}, {"text": "transgenic mice", "type": "Eukaryote"}, {"text": "muscle", "type": "AnatomicalStructure"}, {"text": "overexpression", "type": "BiologicFunction"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "M ( IL10 )", "type": "Chemical"}, {"text": "wild - type mice", "type": "Eukaryote"}, {"text": "hyperinsulinemic - euglycemic clamping", "type": "HealthCareActivity"}]}

Example input:
Sentence: Mice were separated into 4 groups : IA ( intermittent air nondiabetic ) , IH ( intermittent hypoxia nondiabetic ) , IADB ( intermittent air diabetic ) , and IHDB ( intermittent hypoxia diabetic ) groups .

Example answer:
{"entities": [{"text": "Mice", "type": "Eukaryote"}]}

Example input:
Sentence: However , in contrast to that in akt2 -  mice , insulin level is lower in akt2 -  zebrafish , implicating the symptoms of type I diabetes exhibited in akt2 -  zebrafish .

Example answer:
{"entities": [{"text": "akt2", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "insulin level", "type": "HealthCareActivity"}, {"text": "zebrafish", "type": "Eukaryote"}, {"text": "symptoms", "type": "Finding"}, {"text": "type I diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: In contrast , Ins2Akita / + mice with highly - expressed Lias gene display lower oxidative stress and less DN pathologic changes .

Example answer:
{"entities": [{"text": "Ins2Akita / + mice", "type": "Eukaryote"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "Lias gene", "type": "AnatomicalStructure"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "DN", "type": "BiologicFunction"}, {"text": "pathologic changes", "type": "Finding"}]}

Example input:
Sentence: Our results show that Ins2Akita / + mice with under - expressed Lias gene , exhibit higher oxidative stress and more severe DN features ( albuminuria , glomerular basement membrane thickening and mesangial matrix expansion ) .

Example answer:
{"entities": [{"text": "Ins2Akita / + mice", "type": "Eukaryote"}, {"text": "under - expressed", "type": "BiologicFunction"}, {"text": "Lias gene", "type": "AnatomicalStructure"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "DN", "type": "BiologicFunction"}, {"text": "albuminuria", "type": "Finding"}, {"text": "glomerular basement membrane thickening", "type": "Finding"}, {"text": "mesangial matrix expansion", "type": "Finding"}]}

Input:
Sentence: These models have been mated with Ins2Akita / + mice , a type I diabetic mouse model .

## Item MedMentions:test:1764
Example input:
Sentence: Among the 47 , 430 women , there were 152 , 091 MMGs or approximately 3 .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "MMGs", "type": "HealthCareActivity"}]}

Example input:
Sentence: For both meta - analyses , the gender difference peaked in adolescence ( OR = 3 .

Example answer:
{"entities": [{"text": "meta - analyses", "type": "ResearchActivity"}]}

Example input:
Sentence: It increases in the population of women older than 45 years , 10 .

Example answer:
{"entities": [{"text": "population", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: 9±6 . 2 years and 2768 ( 58 . 9 % ) were women .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: In this study , 1516 women of 50 years or older were involved .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "women", "type": "PopulationGroup"}, {"text": "older", "type": "PopulationGroup"}]}

Example input:
Sentence: 15 % , P = 0 . 99 ) , whereas it was significantly higher in men than in women at age ≥65 years ( 65 - 74 years , 38 % vs . 19 % , P < 0 .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Children of mothers with higher educational attainment were more likely to be in the ' normative ' and ' eczema / unfavourable weight ' classes .

Example answer:
{"entities": [{"text": "educational attainment", "type": "Finding"}, {"text": "eczema", "type": "BiologicFunction"}, {"text": "classes", "type": "IntellectualProduct"}]}

Example input:
Sentence: Women were much older than men ( 79±10 vs .

Example answer:
{"entities": [{"text": "Women", "type": "PopulationGroup"}, {"text": "older than", "type": "Finding"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: The sample were 370 participants ( 53 % girls , 47 % boys ) enrolled at secondary and higher secondary levels and ranged in age between 13 - 19 years ( M = 15 . 5 , SD = 1 . 3 ) .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "girls", "type": "PopulationGroup"}, {"text": "higher secondary levels", "type": "IntellectualProduct"}]}

Example input:
Sentence: 96 , P≤ . 001 ) , lower education ( OR = 6 .

Example answer:
{"entities": []}

Input:
Sentence: Women having secondary education and higher were 6 .

## Item MedMentions:test:1721
Example input:
Sentence: Involvement of apoptotic pathways in docosahexaenoic acid -induced benefit in prostate cancer : Pathway - focused gene expression analysis using RT ( 2 ) Profile PCR Array System Present study aimed to better understand the potential apoptotic pathways that involved in docosahexaenoic acid ( DHA ) - induced apoptosis of prostate cancer cells .

Example answer:
{"entities": [{"text": "apoptotic pathways", "type": "BiologicFunction"}, {"text": "docosahexaenoic acid", "type": "Chemical"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "gene expression analysis", "type": "ResearchActivity"}, {"text": "RT ( 2 ) Profile PCR Array System", "type": "ResearchActivity"}, {"text": "DHA", "type": "Chemical"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Furthermore , we found that miR - 4638 - 5p , through regulating Kidins220 and the downstream activity of VEGF and PI3K / AKT pathway , influences prostate cancer progression via angiogenesis .

Example answer:
{"entities": [{"text": "miR - 4638 - 5p", "type": "AnatomicalStructure"}, {"text": "Kidins220", "type": "AnatomicalStructure"}, {"text": "downstream", "type": "SpatialConcept"}, {"text": "VEGF", "type": "Chemical"}, {"text": "prostate cancer progression", "type": "BiologicFunction"}, {"text": "angiogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Men with localized prostate cancer were enrolled in a phase 2 single - arm trial ( NCT02958787 ) at a single academic center .

Example answer:
{"entities": [{"text": "Men", "type": "PopulationGroup"}, {"text": "localized", "type": "SpatialConcept"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "phase 2 single - arm trial", "type": "ResearchActivity"}, {"text": "single academic center", "type": "Organization"}]}

Example input:
Sentence: To identify the TIC niche in human prostate tissue , differential keratin ( KRT ) expression was evaluated .

Example answer:
{"entities": [{"text": "TIC", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "prostate tissue", "type": "AnatomicalStructure"}, {"text": "keratin", "type": "Chemical"}, {"text": "KRT", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "evaluated", "type": "HealthCareActivity"}]}

Example input:
Sentence: Keratin 13 Is Enriched in Prostate Tubule - Initiating Cells and May Identify Primary Prostate Tumors that Metastasize to the Bone Benign human prostate tubule - initiating cells ( TIC ) and aggressive prostate cancer display common traits , including tolerance of low androgen levels , resistance to apoptosis , and microenvironment interactions that drive epithelial budding and outgrowth .

Example answer:
{"entities": [{"text": "Keratin 13", "type": "Chemical"}, {"text": "Prostate", "type": "AnatomicalStructure"}, {"text": "Tubule - Initiating Cells", "type": "AnatomicalStructure"}, {"text": "Primary Prostate Tumors", "type": "BiologicFunction"}, {"text": "Metastasize", "type": "BiologicFunction"}, {"text": "Bone", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "prostate", "type": "AnatomicalStructure"}, {"text": "tubule - initiating cells", "type": "AnatomicalStructure"}, {"text": "TIC", "type": "AnatomicalStructure"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "low androgen levels", "type": "Finding"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "microenvironment interactions", "type": "BiologicFunction"}, {"text": "epithelial budding", "type": "BiologicFunction"}, {"text": "outgrowth", "type": "BiologicFunction"}]}

Example input:
Sentence: In addition , restored TIPE2 obviously inhibits proliferation in prostate cancer cells .

Example answer:
{"entities": [{"text": "TIPE2", "type": "Chemical"}, {"text": "inhibits", "type": "BiologicFunction"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In the present study , we explored the role of TIPE2 in prostate cancer and cancer progression including the molecular mechanism that drives TIPE2 -mediated oncogenesis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "TIPE2", "type": "Chemical"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "cancer progression", "type": "BiologicFunction"}, {"text": "molecular mechanism", "type": "BiologicFunction"}, {"text": "oncogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: TIPE2 Overexpression Suppresses the Proliferation , Migration , and Invasion in Prostate Cancer Cells by Inhibiting PI3K / Akt Signaling Pathway Tumor necrosis factor - α ( TNF - α ) - induced protein 8 - like 2 ( TNFAIP8L2 , TIPE2 ) is involved in the invasion and metastasis of human tumors .

Example answer:
{"entities": [{"text": "TIPE2", "type": "Chemical"}, {"text": "Overexpression", "type": "BiologicFunction"}, {"text": "Migration", "type": "BiologicFunction"}, {"text": "Invasion", "type": "Finding"}, {"text": "Prostate Cancer", "type": "BiologicFunction"}, {"text": "Cells", "type": "AnatomicalStructure"}, {"text": "Inhibiting", "type": "BiologicFunction"}, {"text": "Tumor necrosis factor - α ( TNF - α ) - induced protein 8 - like 2", "type": "Chemical"}, {"text": "TNFAIP8L2", "type": "Chemical"}, {"text": "invasion", "type": "Finding"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: In conclusion , for the first time we demonstrated that TIPE2 overexpression may suppress proliferation , migration , and invasion in prostate cancer cells by inhibiting the PI3K / Akt signaling pathway .

Example answer:
{"entities": [{"text": "TIPE2", "type": "Chemical"}, {"text": "overexpression", "type": "BiologicFunction"}, {"text": "migration", "type": "BiologicFunction"}, {"text": "invasion", "type": "Finding"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "inhibiting", "type": "BiologicFunction"}]}

Example input:
Sentence: However , the functional role of TIPE2 in prostate cancer remains unclear .

Example answer:
{"entities": [{"text": "TIPE2", "type": "Chemical"}, {"text": "prostate cancer", "type": "BiologicFunction"}]}

Input:
Sentence: Therefore , TIPE2 might serve as a potential therapeutic target for human prostate cancer .

## Item MedMentions:test:1362
Example input:
Sentence: Ninety - four percent of individuals assigned to the TECH - N intervention completed the nursing visits .

Example answer:
{"entities": [{"text": "individuals", "type": "PopulationGroup"}, {"text": "TECH - N intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the context of a five - wave longitudinal research design , participants included 928 mother - child dyads in Belfast ( 453 boys , 475 girls ) drawn from socially deprived , ethnically homogenous areas that had experienced political violence .

Example answer:
{"entities": [{"text": "five - wave longitudinal research design", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "Belfast", "type": "SpatialConcept"}, {"text": "ethnically", "type": "Finding"}, {"text": "homogenous", "type": "SpatialConcept"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "violence", "type": "BiologicFunction"}]}

Example input:
Sentence: Few randomized controlled trials ( RCTs ) have focused on strategies to improve outpatient adherence or to reduce reproductive morbidity in this population .

Example answer:
{"entities": [{"text": "randomized controlled trials", "type": "ResearchActivity"}, {"text": "RCTs", "type": "ResearchActivity"}, {"text": "improve", "type": "Finding"}, {"text": "reproductive", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: The percentage of patients who shifted from SD at baseline to normal sexual functioning at EOT was higher in males ( placebo , 40 . 6 % ; vilazodone , 35 . 7 % ) than in females ( placebo , 24 . 9 % ; vilazodone , 34 . 9 % ) ; no statistical testing was performed .

Example answer:
{"entities": [{"text": "SD", "type": "BiologicFunction"}, {"text": "sexual functioning", "type": "BiologicFunction"}, {"text": "males", "type": "PopulationGroup"}, {"text": "placebo", "type": "Chemical"}, {"text": "vilazodone", "type": "Chemical"}, {"text": "females", "type": "PopulationGroup"}]}

Example input:
Sentence: Our objective was to define the AYA patient population referred to an on - site fertility consultation service within a comprehensive cancer center and determine factors associated with patients proceeding with FP treatment .

Example answer:
{"entities": [{"text": "objective", "type": "IntellectualProduct"}, {"text": "population", "type": "PopulationGroup"}, {"text": "on - site fertility consultation service", "type": "HealthCareActivity"}, {"text": "comprehensive cancer center", "type": "Organization"}, {"text": "FP treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Records of 154 referred AYA patients were reviewed for age , ethnicity , cancer type gravidity and parity , survivorship status , and decision to pursue FP treatment .

Example answer:
{"entities": [{"text": "Records", "type": "IntellectualProduct"}, {"text": "ethnicity", "type": "PopulationGroup"}, {"text": "gravidity", "type": "Finding"}, {"text": "parity", "type": "Finding"}, {"text": "FP treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: We conducted a retrospective chart review of AYA women who completed a consultation at the MD Anderson Fertility Preservation and Family Building Service during the first year of service .

Example answer:
{"entities": [{"text": "retrospective chart review", "type": "ResearchActivity"}, {"text": "women", "type": "PopulationGroup"}, {"text": "consultation", "type": "HealthCareActivity"}, {"text": "MD Anderson Fertility Preservation and Family Building Service", "type": "HealthCareActivity"}]}

Example input:
Sentence: AYA women aged 13 - 25 years were recruited during acute PID visits in outpatient clinics and emergency departments ( ED ) to participate in this IRB - approved trial .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "acute PID", "type": "BiologicFunction"}, {"text": "visits", "type": "HealthCareActivity"}, {"text": "outpatient clinics", "type": "Organization"}, {"text": "emergency departments", "type": "Organization"}, {"text": "ED", "type": "Organization"}, {"text": "participate", "type": "HealthCareActivity"}, {"text": "IRB - approved", "type": "IntellectualProduct"}]}

Example input:
Sentence: Recruitment of Minority Adolescents and Young Adults into Randomised Clinical Trials : Testing the Design of the Technology Enhanced Community Health Nursing ( TECH - N ) Pelvic Inflammatory Disease Trial Pelvic inflammatory disease ( PID ) disproportionately affects adolescent and young adult ( AYA ) women and can negatively influence reproductive health trajectories .

Example answer:
{"entities": [{"text": "Minority", "type": "PopulationGroup"}, {"text": "Randomised Clinical Trials", "type": "ResearchActivity"}, {"text": "Technology Enhanced Community Health Nursing", "type": "HealthCareActivity"}, {"text": "TECH - N", "type": "HealthCareActivity"}, {"text": "Pelvic Inflammatory Disease", "type": "BiologicFunction"}, {"text": "Pelvic inflammatory disease", "type": "BiologicFunction"}, {"text": "PID", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "reproductive health", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: This paper describes the research methods and preliminary effectiveness of recruitment , retention , and intervention strategies employed in a novel RCT designed to test a technology - enhanced community - health nursing ( TECH - N ) intervention among urban AYA with PID .

Example answer:
{"entities": [{"text": "research methods", "type": "ResearchActivity"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "RCT", "type": "ResearchActivity"}, {"text": "technology - enhanced community - health nursing", "type": "HealthCareActivity"}, {"text": "TECH - N", "type": "HealthCareActivity"}, {"text": "PID", "type": "BiologicFunction"}]}

Input:
Sentence: Preliminary data from the TECH - N study demonstrated that urban , low - income , minority AYA with PID can effectively be recruited and retained to participate in sexual and reproductive health RCTs with sufficient investment in the design and infrastructure of the study .
