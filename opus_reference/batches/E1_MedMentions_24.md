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

## Item MedMentions:test:4424
Example input:
Sentence: To investigate this question , we recorded EEG and fMRI separately , while human participants used the spatial method of loci or the pegword method , a similarly associative but nonspatial mnemonic .

Example answer:
{"entities": [{"text": "EEG", "type": "HealthCareActivity"}, {"text": "fMRI", "type": "HealthCareActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "spatial", "type": "BiologicFunction"}, {"text": "method of loci", "type": "HealthCareActivity"}, {"text": "pegword method", "type": "HealthCareActivity"}]}

Example input:
Sentence: The current results challenge the notion that massed practice alone promotes recovery from chronic post - stroke aphasia .

Example answer:
{"entities": [{"text": "aphasia", "type": "BiologicFunction"}]}

Example input:
Sentence: Encoding and retrieval are supported by the engagement of both distinct neural pathways across the cortex and common structures within the medial temporal lobes .

Example answer:
{"entities": [{"text": "Encoding", "type": "BiologicFunction"}, {"text": "neural pathways", "type": "AnatomicalStructure"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "structures", "type": "SpatialConcept"}, {"text": "medial temporal lobes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Examining the relationship between home literacy environment and neural correlates of phonological processing in beginning readers with and without a familial risk for dyslexia : an fMRI study Developmental dyslexia is a language - based learning disability characterized by persistent difficulty in learning to read .

Example answer:
{"entities": [{"text": "between", "type": "SpatialConcept"}, {"text": "environment", "type": "SpatialConcept"}, {"text": "dyslexia", "type": "BiologicFunction"}, {"text": "fMRI study", "type": "HealthCareActivity"}, {"text": "Developmental dyslexia", "type": "BiologicFunction"}, {"text": "learning disability", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , these neural changes were found to be selective to orthographic processing , as they were observed for reading and spelling , but not for visual object naming within the left mid - FG .

Example answer:
{"entities": [{"text": "processing", "type": "BiologicFunction"}, {"text": "reading", "type": "BiologicFunction"}, {"text": "visual object naming", "type": "IntellectualProduct"}, {"text": "left mid - FG", "type": "SpatialConcept"}]}

Example input:
Sentence: i . e . , if there is neural recovery for reading and spelling , but not naming , then these neural changes are selective to the recovery of orthographic processing .

Example answer:
{"entities": [{"text": "processing", "type": "BiologicFunction"}]}

Example input:
Sentence: We tested the hypothesis that this acute impairment to reading and spelling would be associated with a selective loss of neural activation in the left fusiform gyrus ( FG ) , and that subsequent recovery would be associated with a gain of neural activation in this region .

Example answer:
{"entities": [{"text": "left fusiform gyrus", "type": "AnatomicalStructure"}, {"text": "FG", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Here we investigate the neural changes associated with impairment and subsequent recovery of the orthographic lexical processing system in an individual with an ischemic left posterior cerebral artery ( PCA ) stroke .

Example answer:
{"entities": [{"text": "ischemic", "type": "BiologicFunction"}]}

Example input:
Sentence: This work describes a longitudinal case study of a patient , whose initials are MMY , with impairments in orthographic lexical processing for reading and spelling at stroke onset , and who recovered these skills within 1 year post stroke .

Example answer:
{"entities": [{"text": "longitudinal case study", "type": "ResearchActivity"}, {"text": "MMY", "type": "Eukaryote"}, {"text": "stroke", "type": "BiologicFunction"}]}

Example input:
Sentence: To test our hypothesis , we examined longitudinal behavioral and functional magnetic resonance imaging ( fMRI ) data of reading , spelling , and visual object naming acquired acutely , 3 weeks , 5 months , and one year post stroke .

Example answer:
{"entities": [{"text": "longitudinal behavioral", "type": "ResearchActivity"}, {"text": "functional magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "fMRI", "type": "HealthCareActivity"}, {"text": "reading", "type": "BiologicFunction"}, {"text": "visual object naming", "type": "IntellectualProduct"}, {"text": "stroke", "type": "BiologicFunction"}]}

Input:
Sentence: Recovery of orthographic processing after stroke : A longitudinal fMRI study An intact orthographic processing system is critical for normal reading and spelling .

## Item MedMentions:test:4768
Example input:
Sentence: Computed tomography showed significantly smaller bone defects and higher bone density in the Bone - Albumin group .

Example answer:
{"entities": [{"text": "Computed tomography", "type": "HealthCareActivity"}, {"text": "bone", "type": "AnatomicalStructure"}, {"text": "bone density", "type": "ClinicalAttribute"}, {"text": "Bone", "type": "AnatomicalStructure"}, {"text": "Albumin", "type": "Chemical"}]}

Example input:
Sentence: The effect of varying bone strontium content on determined quality indices was evaluated based on determined speed of sound ( SOS ) , broadband ultrasound attenuation ( BUA ) and determined quantitative ultrasound index ( QUI ) for phantoms with varying BMD values and varying strontium concentration using two QUS systems : a clinical Sahara ® system and an in - house research system with two identical transducers with center frequency of 1 MHz .

Example answer:
{"entities": [{"text": "bone", "type": "AnatomicalStructure"}, {"text": "strontium", "type": "Chemical"}, {"text": "indices", "type": "IntellectualProduct"}, {"text": "BMD", "type": "ClinicalAttribute"}, {"text": "strontium concentration", "type": "HealthCareActivity"}, {"text": "clinical Sahara ® system", "type": "HealthCareActivity"}, {"text": "research", "type": "ResearchActivity"}]}

Example input:
Sentence: In particular US imaging has been shown to be reliable in foot and ankle assessment and offers a real - time effective imaging technique that is able to reliably confirm structural changes , such as thickening , and identify changes in the internal echo structure associated with diseased or damaged tissue .

Example answer:
{"entities": [{"text": "US imaging", "type": "HealthCareActivity"}, {"text": "assessment", "type": "HealthCareActivity"}, {"text": "imaging technique", "type": "HealthCareActivity"}, {"text": "structural", "type": "SpatialConcept"}, {"text": "thickening", "type": "Finding"}, {"text": "internal", "type": "SpatialConcept"}, {"text": "echo structure", "type": "ClinicalAttribute"}, {"text": "diseased", "type": "BiologicFunction"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Deep periodontal defects in the ( pre ) molar region were most underrated by intra - oral radiography .

Example answer:
{"entities": [{"text": "Deep", "type": "SpatialConcept"}, {"text": "( pre ) molar region", "type": "SpatialConcept"}, {"text": "intra - oral radiography", "type": "HealthCareActivity"}]}

Example input:
Sentence: Assessment of periodontal bone level revisited : a controlled study on the diagnostic accuracy of clinical evaluation methods and intra - oral radiography The accuracy of analogue and especially digital intra - oral radiography in assessing interdental bone level needs further documentation .

Example answer:
{"entities": [{"text": "controlled study", "type": "ResearchActivity"}, {"text": "clinical evaluation", "type": "HealthCareActivity"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "intra - oral radiography", "type": "HealthCareActivity"}, {"text": "analogue", "type": "HealthCareActivity"}, {"text": "digital intra - oral radiography", "type": "HealthCareActivity"}, {"text": "interdental", "type": "SpatialConcept"}, {"text": "documentation", "type": "IntellectualProduct"}]}

Example input:
Sentence: 6 mm for bone sounding without flap elevation ( p < 0 . 001 ) .

Example answer:
{"entities": [{"text": "bone sounding", "type": "HealthCareActivity"}, {"text": "flap", "type": "AnatomicalStructure"}, {"text": "elevation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Significant underestimation of the true bone level was observed for all evaluation methods pointing to 2 . 7 mm on average for analogue radiography , 2 . 5 mm for digital radiography , 1 . 8 mm for RAL - V and 0 .

Example answer:
{"entities": [{"text": "underestimation", "type": "Finding"}, {"text": "evaluation methods", "type": "ResearchActivity"}, {"text": "analogue radiography", "type": "HealthCareActivity"}, {"text": "digital radiography", "type": "HealthCareActivity"}]}

Example input:
Sentence: Radiographic underestimation of the true bone level was higher in the ( pre ) molar region ( p ≤ 0 . 047 ) and increased with defect depth ( p < 0 .

Example answer:
{"entities": [{"text": "Radiographic", "type": "HealthCareActivity"}, {"text": "underestimation", "type": "Finding"}, {"text": "pre ) molar region", "type": "SpatialConcept"}, {"text": "depth", "type": "SpatialConcept"}]}

Example input:
Sentence: The aim of this study was to compare clinical and radiographic bone level assessment to intra - surgical bone level registration ( 1 ) and to identify the clinical variables rendering interdental bone level assessment inaccurate ( 2 ) .

Example answer:
{"entities": [{"text": "radiographic", "type": "HealthCareActivity"}, {"text": "assessment", "type": "HealthCareActivity"}, {"text": "registration", "type": "HealthCareActivity"}, {"text": "interdental", "type": "SpatialConcept"}]}

Example input:
Sentence: Bone sounding had the highest accuracy in assessing interdental bone level .

Example answer:
{"entities": [{"text": "Bone sounding", "type": "HealthCareActivity"}, {"text": "interdental", "type": "SpatialConcept"}]}

Input:
Sentence: Bone sounding was most accurate , whereas intra - oral radiographs were least accurate .

## Item MedMentions:test:4376
Example input:
Sentence: Reliability of 30 - Day Readmission Measures Used in the Hospital Readmission Reduction Program To assess the reliability of risk - standardized readmission rates ( RSRRs ) for medical conditions and surgical procedures used in the Hospital Readmission Reduction Program ( HRRP ) .

Example answer:
{"entities": [{"text": "Readmission Measures", "type": "HealthCareActivity"}, {"text": "surgical procedures", "type": "HealthCareActivity"}]}

Example input:
Sentence: 6 . 8 % , p = 0 . 006 ) , and 30 - day readmission ( 7 . 5 vs .

Example answer:
{"entities": [{"text": "readmission", "type": "HealthCareActivity"}]}

Example input:
Sentence: In order to reduce unplanned ICU admissions , improving the monitoring of patients is therefore warranted .

Example answer:
{"entities": [{"text": "ICU admissions", "type": "HealthCareActivity"}, {"text": "monitoring", "type": "HealthCareActivity"}]}

Example input:
Sentence: The results of this review will aid the development of future models which predict the risk of unplanned ICU admission .

Example answer:
{"entities": [{"text": "models", "type": "IntellectualProduct"}, {"text": "ICU admission", "type": "HealthCareActivity"}]}

Example input:
Sentence: Readmissions rates remain an important outcome to target for intervention , adverse events associated with care transitions continue to be an issue , and patients are often dissatisfied with the quality of their care .

Example answer:
{"entities": [{"text": "intervention", "type": "HealthCareActivity"}, {"text": "adverse events", "type": "BiologicFunction"}, {"text": "care transitions", "type": "HealthCareActivity"}, {"text": "issue", "type": "Finding"}, {"text": "dissatisfied", "type": "BiologicFunction"}]}

Example input:
Sentence: We compared two groups of patients : patients coded as ' RA30 ' ( readmitted within 30 days after the previous discharge ) and patients coded as ' NRA30 ' ( either admitted only once or readmitted after 30 days since the latest discharge ) .

Example answer:
{"entities": [{"text": "two groups", "type": "PopulationGroup"}, {"text": "readmitted", "type": "HealthCareActivity"}, {"text": "discharge", "type": "HealthCareActivity"}, {"text": "admitted", "type": "HealthCareActivity"}]}

Example input:
Sentence: The primary outcome is a composite of hospital readmissions and visits to emergency departments and urgent care centers for 90 days following hospital discharge .

Example answer:
{"entities": [{"text": "hospital readmissions", "type": "HealthCareActivity"}, {"text": "emergency departments", "type": "Organization"}, {"text": "urgent care centers", "type": "Organization"}, {"text": "hospital discharge", "type": "HealthCareActivity"}]}

Example input:
Sentence: No complications or hospital readmissions occurred within thirty days of discharge .

Example answer:
{"entities": [{"text": "hospital readmissions", "type": "HealthCareActivity"}, {"text": "discharge", "type": "HealthCareActivity"}]}

Example input:
Sentence: The effect of age , sex , length of stay , number of diagnoses , normalized number of admissions and presence of diseases on the probability of rehospitalization within 30 days after discharge was evaluated .

Example answer:
{"entities": [{"text": "diagnoses", "type": "ResearchActivity"}, {"text": "number of admissions", "type": "Finding"}, {"text": "presence", "type": "Finding"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "rehospitalization", "type": "HealthCareActivity"}, {"text": "discharge", "type": "HealthCareActivity"}, {"text": "evaluated", "type": "HealthCareActivity"}]}

Example input:
Sentence: The model can be easily applied when discharging patients who have been hospitalized after an access to the Emergency Department to predict the risk of rehospitalization within 30 days .

Example answer:
{"entities": [{"text": "model", "type": "IntellectualProduct"}, {"text": "discharging patients", "type": "HealthCareActivity"}, {"text": "hospitalized", "type": "HealthCareActivity"}, {"text": "Emergency Department", "type": "Organization"}]}

Input:
Sentence: Unplanned readmissions within 30 days after discharge : improving quality through easy prediction To propose an easy predictive model for the risk of rehospitalization , built from hospital administrative data , in order to prevent repeated admissions and to improve transitional care .

## Item MedMentions:test:4585
Example input:
Sentence: BRAF V600E mutation - specific immunohistochemistry and BRAF sequencing were performed in 24 consecutive GISTs , including 14 cases of KIT or PDGFRA mutations and 10 cases of KIT / PDGFRA wild GISTs .

Example answer:
{"entities": [{"text": "mutation", "type": "BiologicFunction"}, {"text": "immunohistochemistry", "type": "HealthCareActivity"}, {"text": "BRAF", "type": "AnatomicalStructure"}, {"text": "GISTs", "type": "BiologicFunction"}, {"text": "KIT", "type": "BiologicFunction"}, {"text": "PDGFRA mutations", "type": "BiologicFunction"}, {"text": "KIT", "type": "AnatomicalStructure"}, {"text": "PDGFRA wild", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Patients with localized disease showed a 3 - year event - free survival ( EFS ) of 68 % , compared to 3 - year EFS of 20 % in patients with metastases ( P = 0 . 042 ) .

Example answer:
{"entities": [{"text": "localized disease", "type": "BiologicFunction"}, {"text": "metastases", "type": "BiologicFunction"}]}

Example input:
Sentence: In the group of patients with PTC , we found a high frequency of TERTp mutations and a low frequency of BRAF mutations in distant metastases , in comparison to the paired primary tumors .

Example answer:
{"entities": [{"text": "PTC", "type": "BiologicFunction"}, {"text": "TERTp", "type": "AnatomicalStructure"}, {"text": "mutations", "type": "BiologicFunction"}, {"text": "BRAF", "type": "AnatomicalStructure"}, {"text": "distant metastases", "type": "IntellectualProduct"}, {"text": "primary tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: A total of 51 patients achieved 5 - year PRS ; however , 32 ( 63 % ) were cancer -bearing patients in their fifth post - recurrent year who were mainly treated by epidermal growth factor receptor - tyrosine kinase inhibitor ( EGFR - TKI ) .

Example answer:
{"entities": [{"text": "cancer", "type": "BiologicFunction"}, {"text": "epidermal growth factor receptor - tyrosine kinase inhibitor", "type": "Chemical"}, {"text": "EGFR - TKI", "type": "Chemical"}]}

Example input:
Sentence: In 33 patients treated with BRAFi , there was no difference in overall or progression - free survival when the patients were categorized into high or low AF groups .

Example answer:
{"entities": [{"text": "treated", "type": "HealthCareActivity"}, {"text": "BRAFi", "type": "Chemical"}]}

Example input:
Sentence: Quantitative data on BRAF allele frequency ( AF ) are sparse , and the potential relationship with response to BRAF inhibitors ( BRAFi ) in patients with metastatic melanoma is unknown .

Example answer:
{"entities": [{"text": "BRAF", "type": "AnatomicalStructure"}, {"text": "BRAF inhibitors", "type": "Chemical"}, {"text": "BRAFi", "type": "Chemical"}, {"text": "metastatic melanoma", "type": "BiologicFunction"}]}

Example input:
Sentence: We found the following mutation frequency in primary PTC , LNM and distant metastases , respectively : TERTp - 12 . 9 % , 10 . 5 % , and 52 . 4 % ; BRAF - 44 . 6 % , 41 . 7 % , and 23 . 8 % ; NRAS - 1 . 2 % , 1 . 3 % , and 14 . 3 % .

Example answer:
{"entities": [{"text": "primary", "type": "BiologicFunction"}, {"text": "PTC", "type": "BiologicFunction"}, {"text": "LNM", "type": "BiologicFunction"}, {"text": "distant metastases", "type": "IntellectualProduct"}, {"text": "TERTp", "type": "AnatomicalStructure"}, {"text": "BRAF", "type": "AnatomicalStructure"}, {"text": "NRAS", "type": "AnatomicalStructure"}]}

Example input:
Sentence: BRAF V600E mutations were detected in 71 .

Example answer:
{"entities": [{"text": "BRAF V600E mutations were detected", "type": "Finding"}]}

Example input:
Sentence: Clinical and therapeutic implications of BRAF mutation heterogeneity in metastatic melanoma Heterogeneity of BRAF mutation in melanoma has been a controversial subject .

Example answer:
{"entities": [{"text": "BRAF mutation", "type": "BiologicFunction"}, {"text": "metastatic melanoma", "type": "BiologicFunction"}, {"text": "melanoma", "type": "BiologicFunction"}]}

Example input:
Sentence: This was an open - label , multicentre study of vemurafenib ( 960 mg bid ) in patients with previously treated or untreated BRAF mutation - positive metastatic melanoma ( cobas ( ® ) 4800 BRAF V600 Mutation Test ) .

Example answer:
{"entities": [{"text": "open - label , multicentre study", "type": "ResearchActivity"}, {"text": "vemurafenib", "type": "Chemical"}, {"text": "untreated", "type": "Finding"}, {"text": "BRAF mutation", "type": "BiologicFunction"}, {"text": "positive", "type": "Finding"}, {"text": "metastatic melanoma", "type": "BiologicFunction"}, {"text": "cobas ( ® ) 4800", "type": "MedicalDevice"}, {"text": "BRAF V600 Mutation Test", "type": "HealthCareActivity"}]}

Input:
Sentence: After 2 years ' follow - up , safety was maintained in this large group of patients with BRAF ( V600 ) mutation - positive metastatic melanoma who are more representative of routine clinical practice than typical clinical trial populations .

## Item MedMentions:test:4627
Example input:
Sentence: Monolithic and ceramic veneered ( n = 10 ) three - unit restorations ( retainers : first premolar and first molar ; pontic : second premolar ) were subject to endodontic access cavity preparation in both retainers using a diamond rotary instrument under continuous water cooling .

Example answer:
{"entities": [{"text": "ceramic", "type": "Chemical"}, {"text": "veneered", "type": "Chemical"}, {"text": "restorations", "type": "HealthCareActivity"}, {"text": "retainers", "type": "MedicalDevice"}, {"text": "first premolar", "type": "AnatomicalStructure"}, {"text": "first molar", "type": "AnatomicalStructure"}, {"text": "pontic", "type": "MedicalDevice"}, {"text": "second premolar", "type": "AnatomicalStructure"}, {"text": "endodontic access cavity preparation", "type": "HealthCareActivity"}, {"text": "water", "type": "Chemical"}]}

Example input:
Sentence: Our results showed that although the Genium with Cenior - Leg ruleset - MPK ( GCL - MPK ) might help to improve several safety -related outcomes as well as gait biomechanics the functional potential of the GCL - MPK may have been limited without specific training and a sufficient acclimation period .

Example answer:
{"entities": [{"text": "Genium with Cenior - Leg ruleset - MPK", "type": "HealthCareActivity"}, {"text": "GCL - MPK", "type": "HealthCareActivity"}, {"text": "biomechanics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "acclimation", "type": "BiologicFunction"}]}

Example input:
Sentence: In 1964 , Mathisen described an alternative method of ureteral reimplantation with lateralization of the neohiatus , creating an orthotopic course of the submucosal ureter .

Example answer:
{"entities": [{"text": "ureteral reimplantation", "type": "HealthCareActivity"}, {"text": "orthotopic", "type": "SpatialConcept"}, {"text": "submucosal ureter", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The proposed learnable MGRF integrates two visual appearance sub - models with an adaptive lung shape submodel .

Example answer:
{"entities": [{"text": "lung", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Subsequently , an effective optimization algorithm based on the split - Bregman approach was adopted to minimize the associative objective function .

Example answer:
{"entities": [{"text": "optimization algorithm", "type": "IntellectualProduct"}]}

Example input:
Sentence: Finally , the class imbalance problem is minimised with the SMOTE approach for both scales ( MSE < 0 . 006 ) .

Example answer:
{"entities": [{"text": "class imbalance problem", "type": "IntellectualProduct"}, {"text": "SMOTE approach", "type": "IntellectualProduct"}]}

Example input:
Sentence: Starting from a homology template and set of known actives , the method introduces receptor flexibility via Normal Mode Analysis and Monte Carlo sampling , to generate a subset of pockets that display enriched discrimination of actives from inactives in retrospective docking .

Example answer:
{"entities": [{"text": "receptor", "type": "Chemical"}, {"text": "Normal Mode Analysis", "type": "ResearchActivity"}, {"text": "pockets", "type": "Chemical"}, {"text": "docking", "type": "BiologicFunction"}]}

Example input:
Sentence: The SFCR algorithm is composed of two consecutive steps corresponding to complementary reconstruction models , each with a structural feature based l1 norm constraint and a voxel fidelity based l2 norm constraint , which allows both the structure edges and tiny features to be recovered , whereas the noise and artifacts could be reduced .

Example answer:
{"entities": [{"text": "algorithm", "type": "IntellectualProduct"}, {"text": "reconstruction models", "type": "IntellectualProduct"}, {"text": "structural feature", "type": "SpatialConcept"}, {"text": "structure", "type": "SpatialConcept"}]}

Example input:
Sentence: Ensemble Linear Neighborhood Propagation for Predicting Subchloroplast Localization of Multi - Location Proteins In the postgenomic era , the number of unreviewed protein sequences is remarkably larger and grows tremendously faster than that of reviewed ones .

Example answer:
{"entities": [{"text": "Linear Neighborhood Propagation", "type": "IntellectualProduct"}, {"text": "Predicting", "type": "Finding"}, {"text": "Subchloroplast Localization", "type": "BiologicFunction"}, {"text": "Multi - Location Proteins", "type": "Chemical"}, {"text": "protein sequences", "type": "SpatialConcept"}]}

Example input:
Sentence: Robust DLPP With Nongreedy ℓ₁ $ - Norm Minimization and Maximization Recently , discriminant locality preserving projection based on L1 - norm ( DLPP - L1 ) was developed for robust subspace learning and image classification .

Example answer:
{"entities": [{"text": "subspace learning", "type": "BiologicFunction"}, {"text": "image", "type": "IntellectualProduct"}, {"text": "classification", "type": "IntellectualProduct"}]}

Input:
Sentence: A modified subgradient extragradient method for solving monotone variational inequalities In the setting of Hilbert space , a modified subgradient extragradient method is proposed for solving Lipschitz - continuous and monotone variational inequalities defined on a level set of a convex function .

## Item MedMentions:test:4636
Example input:
Sentence: Here , we report a novel real - time ultrasound time - of - flight instrument that is capable of monitoring and imaging the critical step in formalin fixation , diffusion of the fixative into tissue , which provides a quantifiable quality metric for tissue fixation in the clinical laboratory ensuring consistent downstream molecular assay results .

Example answer:
{"entities": [{"text": "real - time ultrasound time - of - flight instrument", "type": "MedicalDevice"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "imaging", "type": "HealthCareActivity"}, {"text": "formalin fixation", "type": "HealthCareActivity"}, {"text": "fixative", "type": "Chemical"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "metric", "type": "Chemical"}, {"text": "tissue fixation", "type": "HealthCareActivity"}, {"text": "clinical laboratory", "type": "Organization"}, {"text": "molecular assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using resting state functional magnetic resonance imaging 3 T data obtained over several years of scanning patients for diagnostic and research purposes , we employed a seed - based approach to examine resting state connectivity in higher - order ( default mode , bilateral external control , and salience ) and lower - order ( auditory , sensorimotor , and visual ) resting state networks and connectivity with the thalamus , in 20 healthy unsedated controls , 8 unsedated patients with DOC , and 8 patients with DOC sedated with propofol .

Example answer:
{"entities": [{"text": "resting state functional magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "scanning", "type": "HealthCareActivity"}, {"text": "research", "type": "ResearchActivity"}, {"text": "bilateral", "type": "SpatialConcept"}, {"text": "thalamus", "type": "AnatomicalStructure"}, {"text": "unsedated", "type": "Finding"}, {"text": "DOC", "type": "BiologicFunction"}, {"text": "sedated", "type": "HealthCareActivity"}, {"text": "propofol", "type": "Chemical"}]}

Example input:
Sentence: Possible spatial misalignments between consecutive IR - ufSSFP parameter maps were corrected using elastic image registration .

Example answer:
{"entities": [{"text": "IR - ufSSFP", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here we used serial block - face scanning electron microscopy to obtain 3D volume measurements of synapses and surrounding astrocytic processes in mouse frontal cortex after 6 - 8 h of sleep , spontaneous wake , or sleep deprivation ( SD ) and after chronic ( ∼5 d ) sleep restriction ( CSR ) .

Example answer:
{"entities": [{"text": "serial block - face scanning electron microscopy", "type": "HealthCareActivity"}, {"text": "synapses", "type": "SpatialConcept"}, {"text": "surrounding", "type": "SpatialConcept"}, {"text": "processes", "type": "BiologicFunction"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "frontal cortex", "type": "AnatomicalStructure"}, {"text": "sleep", "type": "BiologicFunction"}, {"text": "wake", "type": "BiologicFunction"}, {"text": "sleep deprivation", "type": "Finding"}, {"text": "SD", "type": "Finding"}]}

Example input:
Sentence: During a T - tube spontaneous breathing trial ( SBT ) we simultaneously evaluated right hemidiaphragm displacement ( i . e . , DD ) by using M - mode ultrasonography as well as the RSBI .

Example answer:
{"entities": [{"text": "T - tube", "type": "MedicalDevice"}, {"text": "spontaneous breathing trial", "type": "HealthCareActivity"}, {"text": "SBT", "type": "HealthCareActivity"}, {"text": "M - mode ultrasonography", "type": "HealthCareActivity"}]}

Example input:
Sentence: 22 participants underwent single - session ( 82 ) Rb dynamic PET imaging during rest and dipyridamole stress using one of 2 test - retest infusion protocols : CA - CA ( n = 12 ) or CA - CF ( n = 10 ) .

Example answer:
{"entities": [{"text": "( 82 ) Rb", "type": "Chemical"}, {"text": "dynamic PET", "type": "HealthCareActivity"}, {"text": "imaging", "type": "HealthCareActivity"}, {"text": "test - retest", "type": "ResearchActivity"}, {"text": "infusion protocols", "type": "HealthCareActivity"}]}

Example input:
Sentence: This method can estimate localized T2 relaxation times from multiple voxels using conventional hyperpolarized ( 13 ) C CSI and can potentially be used with time resolved fast CSI .

Example answer:
{"entities": [{"text": "method", "type": "IntellectualProduct"}, {"text": "localized", "type": "SpatialConcept"}, {"text": "hyperpolarized ( 13 ) C CSI", "type": "HealthCareActivity"}, {"text": "time resolved fast CSI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Dynamic and steady - state oxygen - dependent lung relaxometry using inversion recovery ultra - fast steady - state free precession imaging at 1 .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "lung relaxometry", "type": "HealthCareActivity"}, {"text": "inversion recovery ultra - fast steady - state free precession imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: Electrocardiogram - triggered pulmonary relaxometry with IR - ufSSFP was performed in 7 healthy human subjects at 1 . 5 T .

Example answer:
{"entities": [{"text": "Electrocardiogram - triggered pulmonary relaxometry", "type": "HealthCareActivity"}, {"text": "IR - ufSSFP", "type": "HealthCareActivity"}, {"text": "healthy human", "type": "PopulationGroup"}]}

Example input:
Sentence: 5 T To demonstrate the feasibility of oxygen - dependent relaxometry in human lung using an inversion recovery ultra - fast steady - state free precession ( IR - ufSSFP ) technique .

Example answer:
{"entities": [{"text": "feasibility", "type": "ResearchActivity"}, {"text": "oxygen", "type": "Chemical"}, {"text": "relaxometry", "type": "HealthCareActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "lung", "type": "AnatomicalStructure"}, {"text": "inversion recovery ultra - fast steady - state free precession ( IR - ufSSFP ) technique", "type": "HealthCareActivity"}]}

Input:
Sentence: In a single breath - hold of less than 9 seconds , 30 transient state IR - ufSSFP images were acquired , yielding longitudinal ( T1 ) and transversal ( T2 ) relaxometry parameter maps using voxel -wise nonlinear fitting .

## Item MedMentions:test:4522
Example input:
Sentence: Determining putative vectors of the Bogia Coconut Syndrome phytoplasma using loop - mediated isothermal amplification of single - insect feeding media Phytoplasmas are insect vectored mollicutes responsible for disease in many economically important crops .

Example answer:
{"entities": [{"text": "putative vectors", "type": "Eukaryote"}, {"text": "Bogia Coconut Syndrome", "type": "BiologicFunction"}, {"text": "phytoplasma", "type": "Bacterium"}, {"text": "loop - mediated isothermal amplification", "type": "HealthCareActivity"}, {"text": "single - insect feeding media", "type": "Food"}, {"text": "Phytoplasmas", "type": "Bacterium"}, {"text": "insect vectored mollicutes", "type": "Bacterium"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "crops", "type": "Eukaryote"}]}

Example input:
Sentence: Impact of Soil Salinity on the Structure of the Bacterial Endophytic Community Identified from the Roots of Caliph Medic ( Medicago truncatula ) In addition to being a forage crop , Caliph medic ( Medicago truncatula ) is also a model legume plant and is used for research focusing on the molecular characterization of the interaction between rhizobia and plants .

Example answer:
{"entities": [{"text": "Structure", "type": "SpatialConcept"}, {"text": "Bacterial", "type": "Bacterium"}, {"text": "Endophytic", "type": "Eukaryote"}, {"text": "Roots", "type": "Eukaryote"}, {"text": "Caliph Medic", "type": "Eukaryote"}, {"text": "Medicago truncatula", "type": "Eukaryote"}, {"text": "forage crop", "type": "Eukaryote"}, {"text": "Caliph medic", "type": "Eukaryote"}, {"text": "model legume plant", "type": "ResearchActivity"}, {"text": "rhizobia", "type": "Bacterium"}, {"text": "plants", "type": "Eukaryote"}]}

Example input:
Sentence: All transgenic lines derived from Badila had significantly greater tons of cane per hectare ( TCH ) and tons of sucrose per hectare ( TSH ) as well as lower SCMV disease incidence than those from Badila in the PC and 1R crops .

Example answer:
{"entities": [{"text": "transgenic lines", "type": "Eukaryote"}, {"text": "Badila", "type": "Eukaryote"}, {"text": "SCMV", "type": "Virus"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "PC", "type": "Eukaryote"}, {"text": "1R crops", "type": "Eukaryote"}]}

Example input:
Sentence: Synchronous vitellogenin expression and sexual maturation during migration are negatively correlated with juvenile hormone levels in Mythimna separata Annual migration of pests between different seasonal habitats can lead to serious crop damage .

Example answer:
{"entities": [{"text": "vitellogenin", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "sexual maturation", "type": "BiologicFunction"}, {"text": "migration", "type": "BiologicFunction"}, {"text": "negatively", "type": "Finding"}, {"text": "juvenile hormone", "type": "Chemical"}, {"text": "Mythimna separata", "type": "Eukaryote"}, {"text": "habitats", "type": "SpatialConcept"}, {"text": "crop", "type": "Eukaryote"}]}

Example input:
Sentence: AR37 - infected ryegrass grown at high temperature contained high in plant a concentrations of epoxy - janthitrem ( 30 . 6 μg / g in leaves and 83 . 9 μg / g in pseudostems ) that had a strong anti - feedant effect on porina larvae when incorporated into their diets , reducing their survival by 25 - 42 % on pseudostems .

Example answer:
{"entities": [{"text": "AR37", "type": "Eukaryote"}, {"text": "infected", "type": "BiologicFunction"}, {"text": "ryegrass", "type": "Eukaryote"}, {"text": "plant", "type": "Eukaryote"}, {"text": "epoxy - janthitrem", "type": "Chemical"}, {"text": "leaves", "type": "Eukaryote"}, {"text": "pseudostems", "type": "Finding"}, {"text": "anti - feedant", "type": "Finding"}, {"text": "porina larvae", "type": "Eukaryote"}, {"text": "diets", "type": "Food"}]}

Example input:
Sentence: In this study we combined this feeding medium method with a loop - mediated isothermal amplification ( LAMP ) assay to study 627 insect specimens of 11 Hemiptera taxa sampled from sites in Papua New Guinea affected by Bogia coconut syndrome ( BCS ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "feeding medium method", "type": "HealthCareActivity"}, {"text": "loop - mediated isothermal amplification ( LAMP ) assay", "type": "HealthCareActivity"}, {"text": "insect", "type": "Eukaryote"}, {"text": "Hemiptera taxa", "type": "Eukaryote"}, {"text": "Papua New Guinea", "type": "SpatialConcept"}, {"text": "Bogia coconut syndrome", "type": "BiologicFunction"}, {"text": "BCS", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study , we showed that the monogenean parasite Heterobothrium okamotoi utilizes IgM to recognize its host , fugu Takifugu rubripes Oncomiracidia are infective larvae of H . okamotoi that shed their cilia and metamorphose into juveniles when exposed to purified d - mannose - binding fractions from fugu mucus .

Example answer:
{"entities": [{"text": "monogenean", "type": "Eukaryote"}, {"text": "parasite", "type": "Eukaryote"}, {"text": "Heterobothrium okamotoi", "type": "Eukaryote"}, {"text": "IgM", "type": "Chemical"}, {"text": "fugu Takifugu rubripes Oncomiracidia", "type": "Eukaryote"}, {"text": "infective larvae", "type": "Eukaryote"}, {"text": "H . okamotoi", "type": "Eukaryote"}, {"text": "cilia", "type": "AnatomicalStructure"}, {"text": "metamorphose", "type": "BiologicFunction"}, {"text": "d - mannose", "type": "Chemical"}, {"text": "fugu", "type": "Eukaryote"}, {"text": "mucus", "type": "BodySubstance"}]}

Example input:
Sentence: Biochemical studies of amylase , lipase and protease in Callosobruchus maculatus ( Coleoptera : Chrysomelidae ) populations fed with Vigna unguiculata grain cultivated with diazotrophic bacteria strains The objective of this study was to evaluate the enzymatic activity of homogenates of insects fed on grain of cowpea , Vigna unguiculata ( L . ) , cultivars grown with different nitrogen sources .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "amylase", "type": "Chemical"}, {"text": "lipase", "type": "Chemical"}, {"text": "protease", "type": "Chemical"}, {"text": "Callosobruchus maculatus", "type": "Eukaryote"}, {"text": "Coleoptera", "type": "Eukaryote"}, {"text": "Chrysomelidae", "type": "Eukaryote"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "Vigna unguiculata", "type": "Eukaryote"}, {"text": "grain", "type": "Food"}, {"text": "cultivated", "type": "ResearchActivity"}, {"text": "diazotrophic bacteria strains", "type": "Bacterium"}, {"text": "study", "type": "ResearchActivity"}, {"text": "enzymatic activity", "type": "BiologicFunction"}, {"text": "insects", "type": "Eukaryote"}, {"text": "cowpea", "type": "Eukaryote"}, {"text": "Vigna unguiculata ( L . )", "type": "Eukaryote"}, {"text": "cultivars", "type": "Eukaryote"}, {"text": "nitrogen", "type": "Chemical"}]}

Example input:
Sentence: For the experiment we used aliquots of the homogenate of 100 unsexed adult insects , emerged from 10 g of grain obtained from four cowpea cultivars : ' BRS Acauã ' , ' BRS Carijó ' , ' BRS Pujante ' , and ' BRS Tapaihum ' grown under different regimes of nitrogen sources : mineral fertilizer , inoculation with strains of diazotrophs ( BR 3267 , BR 3262 , BR 3299 ; INPA 03 - 11B , 03 - 84 UFLA , as well as the control ( with soil nitrogen ) .

Example answer:
{"entities": [{"text": "insects", "type": "Eukaryote"}, {"text": "grain", "type": "Food"}, {"text": "cowpea", "type": "Eukaryote"}, {"text": "cultivars", "type": "Eukaryote"}, {"text": "BRS Acauã", "type": "Eukaryote"}, {"text": "BRS Carijó", "type": "Eukaryote"}, {"text": "BRS Pujante", "type": "Eukaryote"}, {"text": "BRS Tapaihum", "type": "Eukaryote"}, {"text": "nitrogen", "type": "Chemical"}, {"text": "mineral", "type": "Chemical"}, {"text": "fertilizer", "type": "Chemical"}, {"text": "inoculation", "type": "HealthCareActivity"}, {"text": "strains of diazotrophs", "type": "Bacterium"}, {"text": "BR 3267", "type": "Bacterium"}, {"text": "BR 3262", "type": "Bacterium"}, {"text": "BR 3299", "type": "Bacterium"}, {"text": "INPA 03 - 11B", "type": "Bacterium"}, {"text": "03 - 84 UFLA", "type": "Bacterium"}]}

Example input:
Sentence: A lower activity of the enzyme amylase from C . maculatus homogenate was observed when insects were fed grain of the cultivar BRS Carijó .

Example answer:
{"entities": [{"text": "activity of the enzyme", "type": "BiologicFunction"}, {"text": "amylase", "type": "Chemical"}, {"text": "C . maculatus", "type": "Eukaryote"}, {"text": "insects", "type": "Eukaryote"}, {"text": "grain", "type": "Food"}, {"text": "cultivar BRS Carijó", "type": "Eukaryote"}]}

Input:
Sentence: maculatus homogenate was observed when the insects fed on grain from the interaction of the cultivar Tapaihum inoculated with BR 3262 diazotrophs .

## Item MedMentions:test:4730
Example input:
Sentence: A significantly improved health - related quality of life was found 1 year after surgery , with improvements in all eight aspects of SF - 36 ( p < 0 . 001 ) .

Example answer:
{"entities": [{"text": "improved", "type": "Finding"}, {"text": "SF - 36", "type": "IntellectualProduct"}]}

Example input:
Sentence: When the European , AECG and ACR Sjogren 's criteria were applied , 666 patients ( 79 . 9 % ) satisfied at least one of them .

Example answer:
{"entities": [{"text": "European", "type": "IntellectualProduct"}, {"text": "AECG", "type": "IntellectualProduct"}, {"text": "ACR Sjogren 's criteria", "type": "IntellectualProduct"}]}

Example input:
Sentence: A multicentre , cross - sectional study of 298 SSc subjects followed in the Canadian Scleroderma Research Group cohort was performed using validated questionnaires : Jorge - Wexner score ( an FI severity scale ) , Bristol stool scale ( a visual scale of stool consistency ) and FI Quality - of - Life scale .

Example answer:
{"entities": [{"text": "cross - sectional study", "type": "ResearchActivity"}, {"text": "SSc", "type": "BiologicFunction"}, {"text": "Canadian Scleroderma Research Group", "type": "Organization"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "questionnaires", "type": "IntellectualProduct"}, {"text": "Jorge - Wexner score", "type": "IntellectualProduct"}, {"text": "FI", "type": "BiologicFunction"}, {"text": "severity scale", "type": "IntellectualProduct"}, {"text": "Bristol stool scale", "type": "IntellectualProduct"}, {"text": "stool consistency", "type": "Finding"}, {"text": "Quality - of - Life scale", "type": "IntellectualProduct"}]}

Example input:
Sentence: Patients with PAD / DM had the greatest increase in amputation rates from 10 per 100 patients with LE ulcer s in 2005 to 28 per 100 patients in 2013 ( P < .001 ) .

Example answer:
{"entities": [{"text": "PAD", "type": "BiologicFunction"}, {"text": "DM", "type": "BiologicFunction"}, {"text": "amputation", "type": "HealthCareActivity"}]}

Example input:
Sentence: HRQoL was evaluated at baseline and every 6 weeks while on treatment using the European Organisation for Research and Treatment of Care ( EORTC ) Core Quality of Life Questionnaire ( QLQ - C30 ) and the EuroQoL Five Dimensions Questionnaire ( EQ - 5D ) .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "European Organisation for Research and Treatment of Care ( EORTC ) Core Quality of Life Questionnaire ( QLQ - C30 )", "type": "IntellectualProduct"}, {"text": "EuroQoL Five Dimensions Questionnaire", "type": "IntellectualProduct"}, {"text": "EQ - 5D", "type": "IntellectualProduct"}]}

Example input:
Sentence: Methods Quality of life was assessed using the Short - Form 36 item Health Survey ( SF - 36 ) in patients visiting the Leiden NPSLE clinic at baseline and at follow - up .

Example answer:
{"entities": [{"text": "Methods", "type": "IntellectualProduct"}, {"text": "Short - Form 36 item Health Survey", "type": "IntellectualProduct"}, {"text": "SF - 36", "type": "IntellectualProduct"}, {"text": "visiting", "type": "HealthCareActivity"}, {"text": "Leiden", "type": "SpatialConcept"}, {"text": "NPSLE", "type": "BiologicFunction"}, {"text": "clinic", "type": "Organization"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: 40 diagnosis were reviewed to determine whether they met the Kidney Disease Outcomes Quality Initiative ( KDOQI ) 2007 criteria for DN .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "Kidney Disease Outcomes Quality Initiative", "type": "Organization"}, {"text": "KDOQI", "type": "Organization"}, {"text": "criteria", "type": "IntellectualProduct"}, {"text": "DN", "type": "BiologicFunction"}]}

Example input:
Sentence: Results At baseline , quality of life was assessed in 248 SLE patients , of whom 98 had NPSLE ( 39 . 7 % ) .

Example answer:
{"entities": [{"text": "SLE", "type": "BiologicFunction"}, {"text": "NPSLE", "type": "BiologicFunction"}]}

Example input:
Sentence: Assessments were conducted through dermatologist evaluations and subjects ' self - assessment at baseline and then at Weeks 12 , 24 , 36 , and 52 .

Example answer:
{"entities": [{"text": "Assessments", "type": "HealthCareActivity"}, {"text": "dermatologist", "type": "ProfessionalOrOccupationalGroup"}, {"text": "evaluations", "type": "HealthCareActivity"}, {"text": "subjects", "type": "PopulationGroup"}, {"text": "self - assessment", "type": "BiologicFunction"}]}

Example input:
Sentence: Two thousand seven hundred three consecutive patients with dermatitis in 8 dermatology clinics representing 8 countries were patch tested with MCI / MI 0 . 01 % aq . and , in parallel with MCI / MI 0 .

Example answer:
{"entities": [{"text": "dermatitis", "type": "BiologicFunction"}, {"text": "dermatology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "clinics", "type": "Organization"}, {"text": "countries", "type": "SpatialConcept"}, {"text": "patch tested", "type": "HealthCareActivity"}, {"text": "MCI / MI", "type": "Chemical"}, {"text": "parallel", "type": "ResearchActivity"}]}

Input:
Sentence: In 77 patients the mean Dermatology Life Quality Index ( DLQI ) was 12 .

## Item MedMentions:test:4134
Example input:
Sentence: Delicaflavone induced autophagic cell death via Akt / mTOR / p70S6 K signaling pathway .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "autophagic cell death", "type": "BiologicFunction"}, {"text": "Akt", "type": "BiologicFunction"}, {"text": "mTOR", "type": "BiologicFunction"}, {"text": "p70S6 K", "type": "Chemical"}, {"text": "signaling pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: In particular , C9orf72 depletion leads to reduced activity of MTOR , a negative regulator of macroautophagy / autophagy , and concomitantly increased TFEB levels and nuclear translocation .

Example answer:
{"entities": [{"text": "C9orf72", "type": "AnatomicalStructure"}, {"text": "MTOR", "type": "Chemical"}, {"text": "macroautophagy", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "TFEB", "type": "Chemical"}, {"text": "nuclear translocation", "type": "BiologicFunction"}]}

Example input:
Sentence: Icaritin activated AMP - activated protein kinase ( AMPK ) signaling in CRC cells , functioning as the upstream signaling for autophagy activation .

Example answer:
{"entities": [{"text": "Icaritin", "type": "Chemical"}, {"text": "AMP - activated protein kinase", "type": "Chemical"}, {"text": "AMPK", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "CRC", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "autophagy", "type": "BiologicFunction"}]}

Example input:
Sentence: shRNA / siRNA -mediated knockdown of AMPKα1 inhibited icaritin - induced autophagy activation , but exacerbated CRC cell death .

Example answer:
{"entities": [{"text": "shRNA", "type": "Chemical"}, {"text": "siRNA", "type": "Chemical"}, {"text": "knockdown", "type": "ResearchActivity"}, {"text": "AMPKα1", "type": "AnatomicalStructure"}, {"text": "icaritin", "type": "Chemical"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "CRC", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}]}

Example input:
Sentence: Delicaflavone downregulated the expression of phospho - Akt , phospho - mTOR , and phospho - p70S6 K in a time - and dose - dependent manner , suggesting that it induced autophagy by inhibiting the Akt / mTOR / p70S6 K pathway in A549 and PC - 9 cells .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "downregulated", "type": "BiologicFunction"}, {"text": "expression of phospho - Akt", "type": "Finding"}, {"text": "phospho - mTOR", "type": "Chemical"}, {"text": "phospho - p70S6 K", "type": "Chemical"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "Akt", "type": "BiologicFunction"}, {"text": "mTOR", "type": "BiologicFunction"}, {"text": "p70S6 K", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "A549", "type": "AnatomicalStructure"}, {"text": "PC - 9 cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Suppression of S6K1 activity led to the phosphorylation and activation of AMPK , which then phosphorylated ULK1 at S555 .

Example answer:
{"entities": [{"text": "S6K1", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "AMPK", "type": "Chemical"}, {"text": "phosphorylated", "type": "BiologicFunction"}, {"text": "ULK1", "type": "Chemical"}]}

Example input:
Sentence: In addition , inhibition of S6K1 activity led to JNK activation , which also contributed to autophagy .

Example answer:
{"entities": [{"text": "inhibition", "type": "BiologicFunction"}, {"text": "S6K1", "type": "Chemical"}, {"text": "activity", "type": "BiologicFunction"}, {"text": "JNK", "type": "Chemical"}, {"text": "autophagy", "type": "BiologicFunction"}]}

Example input:
Sentence: Although both autophagic and proteasomal systems contribute to the degradation of ULK1 , under prolonged nitrogen deprivation , its level was still reduced in ATG7 knockout cells , and only initially stabilized in cells treated with the lysosomal or proteasomal inhibitors .

Example answer:
{"entities": [{"text": "autophagic", "type": "BiologicFunction"}, {"text": "proteasomal systems", "type": "Chemical"}, {"text": "degradation", "type": "BiologicFunction"}, {"text": "ULK1", "type": "Chemical"}, {"text": "nitrogen", "type": "Chemical"}, {"text": "ATG7", "type": "AnatomicalStructure"}, {"text": "knockout cells", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "lysosomal", "type": "AnatomicalStructure"}, {"text": "proteasomal inhibitors", "type": "Chemical"}]}

Example input:
Sentence: While mTOR feedback activation led to increased phosphorylation of ULK1 at S757 , this modification did not the disrupt ULK1 - AMPK interaction nor dampen ULK1 S555 phosphorylation and the induction of autophagy .

Example answer:
{"entities": [{"text": "mTOR", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "ULK1", "type": "Chemical"}, {"text": "AMPK", "type": "Chemical"}, {"text": "interaction", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}]}

Example input:
Sentence: Taken together , our study establishes S6K1 as a key player in the PI - 3 kinase pathway to suppress autophagy through inhibiting AMPK and JNK in a TAK1 -dependent manner .

Example answer:
{"entities": [{"text": "S6K1", "type": "Chemical"}, {"text": "PI - 3 kinase", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "AMPK", "type": "Chemical"}, {"text": "JNK", "type": "Chemical"}, {"text": "TAK1", "type": "Chemical"}]}

Input:
Sentence: Inhibition of p70 S6 kinase ( S6K1 ) activity by A77 1726 , the active metabolite of leflunomide , induces autophagy through TAK1 -mediated AMPK and JNK activation mTOR activation suppresses autophagy by phosphorylating ULK1 at S757 and suppressing its enzymatic activity .

## Item MedMentions:test:4612
Example input:
Sentence: Targeted next generation sequencing and Sanger sequencing identified a heterozygous T to C transition at position 695 ( c .

Example answer:
{"entities": [{"text": "Targeted next generation sequencing", "type": "ResearchActivity"}, {"text": "Sanger sequencing", "type": "ResearchActivity"}, {"text": "T to C transition at position 695", "type": "BiologicFunction"}, {"text": "c .", "type": "BiologicFunction"}]}

Example input:
Sentence: For 300 SNPs , EBFST had the highest precision in all cases , but the bias was negative and greater than those for GST _ NC and θWC _ F in all cases .

Example answer:
{"entities": [{"text": "EBFST", "type": "IntellectualProduct"}, {"text": "negative", "type": "Finding"}]}

Example input:
Sentence: The introduction of C - rich sequences may promote the folding of amplification products into a G - quadruplex structure , which is specifically recognized by the commercially available fluorescent probe thioflavin T .

Example answer:
{"entities": [{"text": "C - rich sequences", "type": "SpatialConcept"}, {"text": "folding", "type": "BiologicFunction"}, {"text": "amplification products", "type": "SpatialConcept"}, {"text": "G - quadruplex", "type": "SpatialConcept"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "fluorescent probe", "type": "Chemical"}, {"text": "thioflavin T", "type": "Chemical"}]}

Example input:
Sentence: The size polymorphism in the mt genomes of these closely related Chrysoporthe species was attributed to the varying number and length of introns , coding sequences and to a lesser extent , intergenic sequences .

Example answer:
{"entities": [{"text": "size", "type": "SpatialConcept"}, {"text": "polymorphism", "type": "BiologicFunction"}, {"text": "mt genomes", "type": "AnatomicalStructure"}, {"text": "Chrysoporthe species", "type": "Eukaryote"}, {"text": "introns", "type": "Chemical"}, {"text": "coding sequences", "type": "AnatomicalStructure"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "intergenic sequences", "type": "Chemical"}]}

Example input:
Sentence: Mononucleotide repeats had a total number of 8073 ( 46 . 74 % ) and an average length of 15 . 45 bp , and were the most abundant SSRs class , while the percentages of di - , tetra - , tri - , penta - , and hexa - nucleotide repeats were 22 . 86 % , 11 .

Example answer:
{"entities": [{"text": "Mononucleotide repeats", "type": "Chemical"}, {"text": "length", "type": "SpatialConcept"}, {"text": "bp", "type": "BiologicFunction"}, {"text": "SSRs", "type": "Chemical"}, {"text": "di -", "type": "Chemical"}, {"text": "tetra -", "type": "Chemical"}, {"text": "tri -", "type": "Chemical"}, {"text": "penta -", "type": "Chemical"}, {"text": "hexa - nucleotide repeats", "type": "Chemical"}]}

Example input:
Sentence: Our results also showed that across all phylogenies , Afghan and Iranian CRF35 _ AD sequences formed a monophyletic cluster ( posterior clade credibility > 0 . 7 ) .

Example answer:
{"entities": [{"text": "Afghan", "type": "SpatialConcept"}, {"text": "Iranian", "type": "SpatialConcept"}, {"text": "sequences", "type": "SpatialConcept"}]}

Example input:
Sentence: The introduction of 5 ' - CCGG - 3 ' sequences allows the dumbbell template to be destroyed by the restriction endonuclease , HpaII , but is not destroyed in the presence of the target MTase - M .

Example answer:
{"entities": [{"text": "5 ' - CCGG - 3 ' sequences", "type": "SpatialConcept"}, {"text": "restriction endonuclease", "type": "Chemical"}, {"text": "HpaII", "type": "Chemical"}, {"text": "MTase", "type": "Chemical"}, {"text": "M .", "type": "Chemical"}]}

Example input:
Sentence: Bleomycin cleaves DNA at specific DNA sequences and recent genome - wide DNA sequencing specificity data indicated that the sequence 5 ' - RTGT * AY ( where T * is the site of bleomycin cleavage , R is G / A and Y is T / C ) is preferentially cleaved by bleomycin in human cells .

Example answer:
{"entities": [{"text": "Bleomycin", "type": "Chemical"}, {"text": "DNA", "type": "Chemical"}, {"text": "specific DNA sequences", "type": "SpatialConcept"}, {"text": "genome - wide", "type": "ResearchActivity"}, {"text": "indicated", "type": "Finding"}, {"text": "sequence", "type": "SpatialConcept"}, {"text": "5 ' - RTGT * AY", "type": "SpatialConcept"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "G", "type": "Chemical"}, {"text": "A", "type": "Chemical"}, {"text": "T", "type": "Chemical"}, {"text": "C", "type": "Chemical"}, {"text": "cleaved", "type": "SpatialConcept"}, {"text": "human", "type": "Eukaryote"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We observed that the preferred consensus DNA sequence for bleomycin cleavage in the plasmid clone was 5 ' - YYGT * AW ( where W is A / T ) .

Example answer:
{"entities": [{"text": "consensus DNA sequence", "type": "SpatialConcept"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "plasmid", "type": "Chemical"}, {"text": "clone", "type": "AnatomicalStructure"}, {"text": "5 ' - YYGT * AW", "type": "SpatialConcept"}, {"text": "A", "type": "Chemical"}, {"text": "T", "type": "Chemical"}]}

Example input:
Sentence: The consensus motif sequence RRm6ACH was observed in 78 . 90 % of m6A peaks .

Example answer:
{"entities": [{"text": "consensus motif sequence", "type": "SpatialConcept"}, {"text": "RRm6ACH", "type": "SpatialConcept"}, {"text": "m6A", "type": "Chemical"}]}

Input:
Sentence: The most highly cleaved sequence was 5 ' - TCGT * AT and , in fact , the seven most highly cleaved sequences conformed to the consensus sequence 5 ' - YYGT * AW .

## Item MedMentions:test:3948
Example input:
Sentence: Human retinal endothelial cells ( HRECs ) isolated from control and diabetic donor tissue and human CD34 ( + ) CACs from control and diabetic patients were used in this study .

Example answer:
{"entities": [{"text": "Human", "type": "Eukaryote"}, {"text": "retinal", "type": "AnatomicalStructure"}, {"text": "endothelial cells", "type": "AnatomicalStructure"}, {"text": "HRECs", "type": "AnatomicalStructure"}, {"text": "diabetic", "type": "BiologicFunction"}, {"text": "donor", "type": "PopulationGroup"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "CD34 ( + ) CACs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We generated a human embryonic stem cell ( hESC ) line carrying a naturally occurring mutation of MYPBC3 ( c . 2905 +1 G > A ) to study HCM pathogenesis during cardiac differentiation .

Example answer:
{"entities": [{"text": "mutation", "type": "BiologicFunction"}, {"text": "MYPBC3", "type": "AnatomicalStructure"}, {"text": "c . 2905 +1 G > A", "type": "BiologicFunction"}, {"text": "HCM", "type": "BiologicFunction"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "cardiac differentiation", "type": "BiologicFunction"}]}

Example input:
Sentence: Preclinical studies strongly suggest that deregulation of HIF , and particularly HIF2 , drives pVHL -defective renal carcinogenesis .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "deregulation", "type": "BiologicFunction"}, {"text": "HIF", "type": "Chemical"}, {"text": "HIF2", "type": "Chemical"}, {"text": "pVHL", "type": "Chemical"}, {"text": "renal carcinogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: We previously demonstrated that H2S is proangiogenic for tumoral but not for normal endothelium and this may represent a target for antiangiogenic therapeutical strategies .

Example answer:
{"entities": [{"text": "H2S", "type": "Chemical"}, {"text": "proangiogenic", "type": "Chemical"}, {"text": "tumoral", "type": "BiologicFunction"}, {"text": "endothelium", "type": "AnatomicalStructure"}, {"text": "antiangiogenic therapeutical strategies", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here , we report a better approach to target cancer -associated endothelial cells ( ECs ) , reverse permeability and leakiness of tumor blood vessels , and improve delivery of chemotherapeutic agents to the tumor .

Example answer:
{"entities": [{"text": "cancer", "type": "BiologicFunction"}, {"text": "endothelial cells", "type": "AnatomicalStructure"}, {"text": "ECs", "type": "AnatomicalStructure"}, {"text": "tumor blood vessels", "type": "BiologicFunction"}, {"text": "chemotherapeutic agents", "type": "Chemical"}, {"text": "tumor", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , we show that angiogenesis also can be promoted by a direct interaction between brain tumor cells , including tumor cells with cancer stem -like properties ( CSCs ) , and endothelial cells ( ECs ) .

Example answer:
{"entities": [{"text": "angiogenesis", "type": "BiologicFunction"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "tumor cells", "type": "AnatomicalStructure"}, {"text": "cancer stem", "type": "AnatomicalStructure"}, {"text": "CSCs", "type": "AnatomicalStructure"}, {"text": "endothelial cells", "type": "AnatomicalStructure"}, {"text": "ECs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: all EC types are similarly sensitive to oxidative stress induced by hydrogen peroxide ; chemical hypoxia differentially affects endothelial viability , that results unaltered by real hypoxia .

Example answer:
{"entities": [{"text": "EC", "type": "AnatomicalStructure"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "hydrogen peroxide", "type": "Chemical"}, {"text": "chemical hypoxia", "type": "BiologicFunction"}, {"text": "endothelial viability", "type": "BiologicFunction"}, {"text": "hypoxia", "type": "BiologicFunction"}]}

Example input:
Sentence: H2S acts differentially on EC migration and tubulogenesis .

Example answer:
{"entities": [{"text": "H2S", "type": "Chemical"}, {"text": "EC", "type": "AnatomicalStructure"}, {"text": "migration", "type": "BiologicFunction"}, {"text": "tubulogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Hypoxia and hydrogen sulfide differentially affect normal and tumor - derived vascular endothelium endothelial cells play a key role in vessels formation both under physiological and pathological conditions .

Example answer:
{"entities": [{"text": "Hypoxia", "type": "BiologicFunction"}, {"text": "hydrogen sulfide", "type": "Chemical"}, {"text": "vascular endothelium", "type": "AnatomicalStructure"}, {"text": "endothelial cells", "type": "AnatomicalStructure"}, {"text": "vessels formation", "type": "BiologicFunction"}, {"text": "physiological", "type": "BiologicFunction"}, {"text": "pathological conditions", "type": "BiologicFunction"}]}

Example input:
Sentence: Endothelial migration is enhanced by hypoxia , while tubulogenesis is inhibited for all EC types .

Example answer:
{"entities": [{"text": "Endothelial migration", "type": "BiologicFunction"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "tubulogenesis", "type": "BiologicFunction"}, {"text": "EC", "type": "AnatomicalStructure"}]}

Input:
Sentence: in this work , we investigate cell viability , migration and tubulogenesis on human EC derived from two different tumors , breast and renal carcinoma ( BTEC and RTEC ) , compared to normal microvascular endothelium ( HMEC ) under oxidative stress , hypoxia and treatment with exogenous H2S .

## Item MedMentions:test:4172
Example input:
Sentence: The highest variance ratio % PD SDR in all oral diseases DALYs occurred between 1990 and 2013 in ages 20 to 24 ( 50 . 7 % ) and 25 to 29 years ( 50 . 5 % ) .

Example answer:
{"entities": [{"text": "% PD SDR", "type": "Finding"}, {"text": "oral diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Moreover , stratification analyses indicated that the R1628P polymorphism was significantly associated with an increased risk of PD among Chinese as well as non - Chinese Asian populations and an increased risk of PD in Chinese patients from China , Taiwan , and Singapore .

Example answer:
{"entities": [{"text": "stratification analyses", "type": "ResearchActivity"}, {"text": "R1628P polymorphism", "type": "SpatialConcept"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "Chinese", "type": "PopulationGroup"}, {"text": "non - Chinese Asian populations", "type": "PopulationGroup"}, {"text": "China", "type": "SpatialConcept"}, {"text": "Taiwan", "type": "SpatialConcept"}, {"text": "Singapore", "type": "SpatialConcept"}]}

Example input:
Sentence: The WHO Study on global AGEing and adult health ( SAGE ) Wave 1 ( 2007 - 2010 ) in China , Ghana , India , Mexico , Russia and South Africa is the data source .

Example answer:
{"entities": [{"text": "WHO", "type": "Organization"}, {"text": "Study", "type": "ResearchActivity"}, {"text": "AGEing", "type": "BiologicFunction"}, {"text": "SAGE", "type": "ResearchActivity"}, {"text": "China", "type": "SpatialConcept"}, {"text": "Ghana", "type": "SpatialConcept"}, {"text": "India", "type": "SpatialConcept"}, {"text": "Mexico", "type": "SpatialConcept"}, {"text": "Russia", "type": "SpatialConcept"}, {"text": "South Africa", "type": "SpatialConcept"}]}

Example input:
Sentence: We used data from the Global Burden of Disease study ( GBD ) 2013 .

Example answer:
{"entities": [{"text": "Global Burden of Disease study", "type": "IntellectualProduct"}, {"text": "GBD", "type": "IntellectualProduct"}]}

Example input:
Sentence: PD standardized DALYs rate ( SDR ) per 100 , 000 persons , the percentage of PD standardized DALYs rate ( % PD SDR ) in all diseases DALYs , and variance ratio of these two indexes between the years of 1990 and 2013 were compared by province , gender and age groups .

Example answer:
{"entities": [{"text": "PD", "type": "BiologicFunction"}, {"text": "standardized DALYs rate", "type": "Finding"}, {"text": "SDR", "type": "Finding"}, {"text": "persons", "type": "PopulationGroup"}, {"text": "percentage of PD standardized DALYs rate", "type": "Finding"}, {"text": "% PD SDR", "type": "Finding"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "province", "type": "SpatialConcept"}]}

Example input:
Sentence: The estimation of burden of PD between 1990 and 2013 will provide a unique perspective for planning interventions and developing public health policies for PD even chronic diseases in China .

Example answer:
{"entities": [{"text": "burden", "type": "IntellectualProduct"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "chronic diseases", "type": "BiologicFunction"}, {"text": "China", "type": "SpatialConcept"}]}

Example input:
Sentence: DALYs are computed by adding YLLs and YLDs for each age - sex - country group .

Example answer:
{"entities": []}

Example input:
Sentence: The four highest variance ratios % PD SDR in all diseases DALYs between 1990 and 2013 occurred in the west of China ( 97 , 98 . 6 , 108 . 4 and 112 . 8 % ) .

Example answer:
{"entities": [{"text": "% PD SDR", "type": "Finding"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "west of China", "type": "SpatialConcept"}]}

Example input:
Sentence: A comparison of DALYs for periodontal disease in China between 1990 and 2013 : insights from the 2013 global burden of disease study China has undergone a rapid demographic and epidemiological transition with fast ecomonic development since the 1980s .

Example answer:
{"entities": [{"text": "periodontal disease", "type": "BiologicFunction"}, {"text": "China", "type": "SpatialConcept"}, {"text": "global burden of disease study", "type": "IntellectualProduct"}]}

Example input:
Sentence: The PD standardized DALYs rate and % PD SDR in all diseases DALYs in China in 2013 has increased from 1990 .

Example answer:
{"entities": [{"text": "PD", "type": "BiologicFunction"}, {"text": "standardized DALYs rate", "type": "Finding"}, {"text": "% PD SDR", "type": "Finding"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "China", "type": "SpatialConcept"}]}

Input:
Sentence: We used the GBD 2013 results for Years of Life Lost ( YLLs ) and Years Lived with Disability ( YLDs ) to calculate Disability Adjusted Life Years ( DALYs ) for PD in China .

## Item MedMentions:test:4766
Example input:
Sentence: Plants were exposed to high temperatures ( 30 or 35 ° C ) in a controlled environment room for 20 - h periods during meiosis and the premeiotic interphase just prior to meiosis .

Example answer:
{"entities": [{"text": "Plants", "type": "Eukaryote"}, {"text": "meiosis", "type": "BiologicFunction"}, {"text": "premeiotic interphase", "type": "BiologicFunction"}]}

Example input:
Sentence: The CT and CC genotypes were associated with a 50 % and a 2 - fold increased risk , respectively , of a suboptimal plasma 25 ( OH ) D concentration ( < 75 nmol / L ) .

Example answer:
{"entities": [{"text": "plasma", "type": "BodySubstance"}, {"text": "25 ( OH ) D", "type": "Chemical"}]}

Example input:
Sentence: Under high temperature , a rapid elevation in the level of the intermediate metabolite ( M4 ) was found only in pinoxaden - resistant plants .

Example answer:
{"entities": [{"text": "elevation", "type": "SpatialConcept"}, {"text": "intermediate", "type": "SpatialConcept"}, {"text": "metabolite", "type": "Chemical"}, {"text": "M4", "type": "Chemical"}, {"text": "pinoxaden", "type": "Chemical"}, {"text": "plants", "type": "Eukaryote"}]}

Example input:
Sentence: Although alkaloid concentrations were greatly reduced by low temperature this reduction did not occur until after 4 weeks of exposure .

Example answer:
{"entities": [{"text": "alkaloid", "type": "Chemical"}]}

Example input:
Sentence: When maintained at high temperature , they grew significantly faster , became shorter , with genes involved in sugar metabolism and mitochondrial stress protection significantly upregulated .

Example answer:
{"entities": [{"text": "grew", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "mitochondrial", "type": "AnatomicalStructure"}, {"text": "upregulated", "type": "BiologicFunction"}]}

Example input:
Sentence: After exposure to a constant temperature of 25 ° C for 7 , 14 , 21 or 28 d ( n = 6 ) or to 42 ° C for 3 h per d for 7 , 14 , 21 or 28 d ( n = 6 ) , the mice were euthanized and their ovaries were analyzed for follicular atresia , granulosa cell apoptosis , changes in the abundance of HSP70 protein and serum concentrations of estradiol .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}, {"text": "ovaries", "type": "AnatomicalStructure"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "follicular atresia", "type": "BiologicFunction"}, {"text": "granulosa cell", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "HSP70 protein", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: Exposure of wheat to high temperatures during male meiosis prevents normal meiotic progression and reduces grain number .

Example answer:
{"entities": [{"text": "wheat", "type": "Eukaryote"}, {"text": "male meiosis", "type": "BiologicFunction"}, {"text": "meiotic progression", "type": "BiologicFunction"}, {"text": "grain", "type": "Eukaryote"}]}

Example input:
Sentence: PMCs exposed to 35 ° C were less likely to progress than those exposed to 30 ° C .

Example answer:
{"entities": [{"text": "PMCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Grain number per spike was reduced at 30 ° C , and reduced even further at 35 ° C .

Example answer:
{"entities": [{"text": "Grain", "type": "Eukaryote"}]}

Example input:
Sentence: However , following exposure to 30 ° C , in euploid plants grain number was reduced ( though not significantly ) , whereas in N5DT5B plants the reduction was highly significant .

Example answer:
{"entities": [{"text": "euploid plants", "type": "Eukaryote"}, {"text": "grain", "type": "Eukaryote"}, {"text": "not significantly", "type": "Finding"}, {"text": "N5DT5B plants", "type": "Eukaryote"}]}

Input:
Sentence: After exposure to 35 ° C , the reduction in grain number was highly significant for both genotypes .

## Item MedMentions:test:4279
Example input:
Sentence: Additionally , our analysis showed that the Grpr - Cre population expresses Vglut2 mRNA , and mice ablated of Vglut2 in Grpr - Cre cells ( Vglut2 - lox ; Grpr - Cre mice ) displayed less spontaneous itch and attenuated responses to both histaminergic and nonhistaminergic agents .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "Grpr - Cre", "type": "AnatomicalStructure"}, {"text": "expresses", "type": "BiologicFunction"}, {"text": "Vglut2", "type": "Chemical"}, {"text": "mRNA", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "Grpr - Cre cells", "type": "AnatomicalStructure"}, {"text": "lox", "type": "Chemical"}, {"text": "Grpr - Cre mice", "type": "AnatomicalStructure"}, {"text": "itch", "type": "Finding"}, {"text": "histaminergic", "type": "Chemical"}, {"text": "nonhistaminergic agents", "type": "Chemical"}]}

Example input:
Sentence: Cloning and sequence analysis of Wild Argali short palate , lung and nasal epithelium clone 1 cDNA Experiments were conducted to clone the sequence of Wild Argali short palate , lung and nasal epithelium clone 1 ( SPLUNC1 ) cDNA , and to lay the foundation for further study the biological function of Wild Argali SPLUNC1 .

Example answer:
{"entities": [{"text": "Cloning", "type": "HealthCareActivity"}, {"text": "sequence analysis", "type": "HealthCareActivity"}, {"text": "Wild Argali", "type": "Eukaryote"}, {"text": "short palate , lung and nasal epithelium clone 1", "type": "AnatomicalStructure"}, {"text": "cDNA", "type": "Chemical"}, {"text": "clone", "type": "HealthCareActivity"}, {"text": "sequence", "type": "SpatialConcept"}, {"text": "SPLUNC1", "type": "AnatomicalStructure"}, {"text": "biological function", "type": "BiologicFunction"}]}

Example input:
Sentence: In parallel , a fragment of caspase 3 was cloned for the first time in this species , sequenced and used for in situ hybridization to localize messengers and analysed by a phylogenetic survey to shed light on its homology with reptilian caspases .

Example answer:
{"entities": [{"text": "caspase 3", "type": "AnatomicalStructure"}, {"text": "cloned", "type": "HealthCareActivity"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "in situ hybridization", "type": "ResearchActivity"}, {"text": "localize", "type": "SpatialConcept"}, {"text": "phylogenetic survey", "type": "ResearchActivity"}, {"text": "reptilian", "type": "Eukaryote"}, {"text": "caspases", "type": "Chemical"}]}

Example input:
Sentence: The full - length kiss1 cDNA was 682bp , containing an ORF of 405bp , encoding 134 amino acids with a conserved kisspeptin - 10 region .

Example answer:
{"entities": [{"text": "kiss1", "type": "AnatomicalStructure"}, {"text": "cDNA", "type": "Chemical"}, {"text": "ORF", "type": "AnatomicalStructure"}, {"text": "amino acids", "type": "Chemical"}, {"text": "kisspeptin - 10", "type": "Chemical"}]}

Example input:
Sentence: Kiss1 transcripts significantly increased in both sexes 8 weeks after birth , and then were maintained at high levels in adults , indicating its possible role in the onset of puberty and maintaining of reproductive activity .

Example answer:
{"entities": [{"text": "Kiss1", "type": "AnatomicalStructure"}, {"text": "transcripts", "type": "Chemical"}, {"text": "birth", "type": "BiologicFunction"}, {"text": "puberty", "type": "BiologicFunction"}]}

Example input:
Sentence: Brandt 's vole is one of the main pest species on the Inner Mongolian steppes for its striking reproductive capacity and kiss1 is a key candidate gene related to reproductive regulatory cascades .

Example answer:
{"entities": [{"text": "Brandt 's vole", "type": "Eukaryote"}, {"text": "pest species", "type": "IntellectualProduct"}, {"text": "Inner Mongolian steppes", "type": "SpatialConcept"}, {"text": "reproductive", "type": "BiologicFunction"}, {"text": "kiss1", "type": "AnatomicalStructure"}, {"text": "gene", "type": "AnatomicalStructure"}, {"text": "reproductive regulatory cascades", "type": "BiologicFunction"}]}

Example input:
Sentence: These results are helpful to further the study of kiss1 function in reproductive regulation of Brandt 's voles .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "kiss1", "type": "AnatomicalStructure"}, {"text": "reproductive regulation", "type": "BiologicFunction"}, {"text": "Brandt 's voles", "type": "Eukaryote"}]}

Example input:
Sentence: Kiss1 mRNA levels in the hypothalamus did not show a significant difference between week 2 and week 4 , indicating kiss1 mRNA levels may not be related to the rapid growth of the sexual organs in early developmental stages .

Example answer:
{"entities": [{"text": "Kiss1", "type": "AnatomicalStructure"}, {"text": "mRNA", "type": "Chemical"}, {"text": "hypothalamus", "type": "AnatomicalStructure"}, {"text": "kiss1", "type": "AnatomicalStructure"}, {"text": "sexual organs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Kiss1 mRNA was specifically expressed in ovary , testicle , small intestine , kidney , liver and hypothalamus tissues , and was undetectable in other tissues , including pituitary , heart , adrenal gland , bladder and uterus .

Example answer:
{"entities": [{"text": "Kiss1", "type": "AnatomicalStructure"}, {"text": "mRNA", "type": "Chemical"}, {"text": "ovary", "type": "AnatomicalStructure"}, {"text": "testicle", "type": "AnatomicalStructure"}, {"text": "small intestine", "type": "AnatomicalStructure"}, {"text": "kidney", "type": "AnatomicalStructure"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "hypothalamus", "type": "AnatomicalStructure"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "pituitary", "type": "AnatomicalStructure"}, {"text": "heart", "type": "AnatomicalStructure"}, {"text": "adrenal gland", "type": "AnatomicalStructure"}, {"text": "bladder", "type": "AnatomicalStructure"}, {"text": "uterus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Molecular cloning and characterization of kiss1 in Brandt 's voles ( Lasiopodomys brandtii ) Kisspeptin , encoded by kiss1 , has been regarded as a major modulator of mammalian puberty and fertility due to its stimulation on GnRH .

Example answer:
{"entities": [{"text": "Molecular cloning", "type": "HealthCareActivity"}, {"text": "kiss1", "type": "AnatomicalStructure"}, {"text": "Brandt 's voles", "type": "Eukaryote"}, {"text": "Lasiopodomys brandtii", "type": "Eukaryote"}, {"text": "Kisspeptin", "type": "Chemical"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "puberty", "type": "BiologicFunction"}, {"text": "fertility", "type": "BiologicFunction"}, {"text": "stimulation", "type": "BiologicFunction"}, {"text": "GnRH", "type": "Chemical"}]}

Input:
Sentence: In this study , kiss1 cDNA was cloned from the hypothalamus of Brandt 's voles and kiss1 mRNA levels were investigated in different tissues , and at different developmental stages , using high - throughput real - time PCR .

## Item MedMentions:test:4579
Example input:
Sentence: In contrast , a southern Amazon forest ( Jarú RJA ) exhibited dry - season declines in GPP and Re consistent with most DGVMs simulations .

Example answer:
{"entities": [{"text": "southern Amazon", "type": "SpatialConcept"}, {"text": "Re", "type": "BiologicFunction"}, {"text": "DGVMs", "type": "IntellectualProduct"}, {"text": "simulations", "type": "ResearchActivity"}]}

Example input:
Sentence: Within habitat quality , the following subcriteria proved to be most relevant : orographic diversity , elevation range and important plant species located 1 . 5 km from the apiary .

Example answer:
{"entities": [{"text": "habitat", "type": "SpatialConcept"}, {"text": "elevation", "type": "SpatialConcept"}, {"text": "plant", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "located", "type": "SpatialConcept"}]}

Example input:
Sentence: The information contained on this dataset can be applied in the study of macroecological patterns of biodiversity , communities and populations , but also to evaluate the ecological consequences of fragmentation and defaunation , and predict disease outbreaks , trophic interactions and community dynamics in this biodiversity hotspot .

Example answer:
{"entities": [{"text": "dataset", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "populations", "type": "Eukaryote"}, {"text": "fragmentation", "type": "Finding"}, {"text": "defaunation", "type": "Finding"}, {"text": "biodiversity hotspot", "type": "SpatialConcept"}]}

Example input:
Sentence: The dataset also revealed a hyper - dominance of 22 species that comprised 78 . 29 % of all individuals captured , with only seven species representing 44 % of all captures .

Example answer:
{"entities": [{"text": "dataset", "type": "IntellectualProduct"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "individuals", "type": "Eukaryote"}]}

Example input:
Sentence: Here , we used an integrated dataset from four forests in the Brasil flux network , spanning a range of dry - season intensities and lengths , to determine how well four state - of - the - art models ( IBIS , ED2 , JULES , and CLM3 . 5 ) simulated the seasonality of carbon exchanges in Amazonian tropical forests .

Example answer:
{"entities": [{"text": "dataset", "type": "IntellectualProduct"}, {"text": "Brasil flux network", "type": "IntellectualProduct"}, {"text": "models", "type": "IntellectualProduct"}, {"text": "IBIS", "type": "IntellectualProduct"}, {"text": "ED2", "type": "IntellectualProduct"}, {"text": "JULES", "type": "IntellectualProduct"}, {"text": "CLM3 . 5", "type": "IntellectualProduct"}, {"text": "Amazonian", "type": "SpatialConcept"}]}

Example input:
Sentence: Species distribution modeling and molecular markers suggest longitudinal range shifts and cryptic northern refugia of the typical calcareous grassland species Hippocrepis comosa ( horseshoe vetch ) Calcareous grasslands belong to the most diverse , endangered habitats in Europe , but there is still insufficient information about the origin of the plant species related to these grasslands .

Example answer:
{"entities": [{"text": "Species", "type": "IntellectualProduct"}, {"text": "modeling", "type": "ResearchActivity"}, {"text": "molecular markers", "type": "ClinicalAttribute"}, {"text": "calcareous grassland", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Hippocrepis comosa", "type": "Eukaryote"}, {"text": "horseshoe vetch", "type": "Eukaryote"}, {"text": "Calcareous grasslands", "type": "SpatialConcept"}, {"text": "endangered habitats", "type": "SpatialConcept"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "plant", "type": "Eukaryote"}, {"text": "grasslands", "type": "SpatialConcept"}]}

Example input:
Sentence: However , little information is available about microbial diversity in the semi - arid Caatinga , which represents a unique biome that extends to about 11 % of the Brazilian territory and is home to extraordinary diversity and high endemism level of species .

Example answer:
{"entities": [{"text": "extends", "type": "SpatialConcept"}, {"text": "Brazilian territory", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: The dataset comprises 53 , 518 individuals of 124 species of small mammals , including 30 species of marsupials and 94 species of rodents .

Example answer:
{"entities": [{"text": "dataset", "type": "IntellectualProduct"}, {"text": "individuals", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "mammals", "type": "Eukaryote"}, {"text": "marsupials", "type": "Eukaryote"}, {"text": "rodents", "type": "Eukaryote"}]}

Example input:
Sentence: The dataset comprises 136 references from 300 locations covering seven vegetation types of tropical and subtropical Atlantic forests of South America , and presents data on species composition , richness , and relative abundance ( captures / trap - nights ) .

Example answer:
{"entities": [{"text": "dataset", "type": "IntellectualProduct"}, {"text": "locations", "type": "SpatialConcept"}, {"text": "vegetation types", "type": "Eukaryote"}, {"text": "South America", "type": "SpatialConcept"}]}

Example input:
Sentence: ATLANTIC SMALL - MAMMAL : a dataset of communities of rodents and marsupials of the Atlantic Forests of South America The contribution of small mammal ecology to the understanding of macroecological patterns of biodiversity , population dynamics and community assembly has been hindered by the absence of large datasets of small mammal communities from tropical regions .

Example answer:
{"entities": [{"text": "MAMMAL", "type": "Eukaryote"}, {"text": "dataset", "type": "IntellectualProduct"}, {"text": "rodents", "type": "Eukaryote"}, {"text": "marsupials", "type": "Eukaryote"}, {"text": "South America", "type": "SpatialConcept"}, {"text": "mammal", "type": "Eukaryote"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "datasets", "type": "IntellectualProduct"}, {"text": "tropical regions", "type": "SpatialConcept"}]}

Input:
Sentence: The dataset reviews small mammal communities from the Atlantic forest of South America , one of the regions with the highest diversity of small mammals and a global biodiversity hotspot , though currently covering less than 12 % of its original area due to anthropogenic pressures .

## Item MedMentions:test:4308
Example input:
Sentence: The Effect of Oxygen Inhalation Plus Oxytocin Compared with Oxytocin Only on Postpartum Haemorrhage : A Randomized Clinical Trial Post Partum Haemorrhage ( PPH ) is the leading cause of maternal mortality across the world , mainly in the developing countries .

Example answer:
{"entities": [{"text": "Oxygen Inhalation", "type": "HealthCareActivity"}, {"text": "Oxytocin", "type": "Chemical"}, {"text": "Postpartum Haemorrhage", "type": "BiologicFunction"}, {"text": "Randomized Clinical Trial", "type": "ResearchActivity"}, {"text": "Post Partum Haemorrhage", "type": "BiologicFunction"}, {"text": "PPH", "type": "BiologicFunction"}, {"text": "world", "type": "PopulationGroup"}]}

Example input:
Sentence: Our hypothesis is that in sepsis - associated coagulopathies ( SACs ) , interleukins may be upregulated , leading to hemostatic imbalance by generating thrombogenic mediators .

Example answer:
{"entities": [{"text": "sepsis - associated coagulopathies", "type": "BiologicFunction"}, {"text": "SACs", "type": "BiologicFunction"}, {"text": "interleukins", "type": "Chemical"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "hemostatic imbalance", "type": "BiologicFunction"}, {"text": "thrombogenic mediators", "type": "Chemical"}]}

Example input:
Sentence: Mesenchymal stromal cells exposed to carbon monoxide , with docosahexaenoic acid substrate , produced specialized proresolving lipid mediators , particularly D - series resolvins , which promoted survival .

Example answer:
{"entities": [{"text": "Mesenchymal stromal cells", "type": "AnatomicalStructure"}, {"text": "carbon monoxide", "type": "Chemical"}, {"text": "docosahexaenoic acid", "type": "Chemical"}, {"text": "proresolving", "type": "Finding"}, {"text": "resolvins", "type": "Chemical"}]}

Example input:
Sentence: Taken together , these data suggest that production of specialized proresolving lipid mediators contribute to improved mesenchymal stromal cell efficacy when exposed to carbon monoxide , resulting in an improved therapeutic response during sepsis .

Example answer:
{"entities": [{"text": "proresolving", "type": "Finding"}, {"text": "improved", "type": "Finding"}, {"text": "mesenchymal stromal cell", "type": "AnatomicalStructure"}, {"text": "carbon monoxide", "type": "Chemical"}, {"text": "therapeutic response", "type": "ClinicalAttribute"}, {"text": "sepsis", "type": "BiologicFunction"}]}

Example input:
Sentence: Necropsy of moribund individuals revealed hemorrhagic ascites and petechial hemorrhages in the coelomic peritoneum and serosa of internal organs .

Example answer:
{"entities": [{"text": "Necropsy", "type": "HealthCareActivity"}, {"text": "moribund", "type": "Finding"}, {"text": "individuals", "type": "Eukaryote"}, {"text": "hemorrhagic ascites", "type": "Finding"}, {"text": "petechial hemorrhages", "type": "BiologicFunction"}, {"text": "coelomic", "type": "SpatialConcept"}, {"text": "peritoneum", "type": "AnatomicalStructure"}, {"text": "serosa", "type": "AnatomicalStructure"}, {"text": "organs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: When ischemia occurs , the oxygen supply is interrupted , hence the necrosis of the enteral mucosa occurs within 3h , whilst the necrosis of the full thickness of the bowel wall occurs within 6h .

Example answer:
{"entities": [{"text": "ischemia", "type": "BiologicFunction"}, {"text": "oxygen supply", "type": "ClinicalAttribute"}, {"text": "necrosis", "type": "BiologicFunction"}, {"text": "mucosa", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In the bleeding group during the last step of hemorrhage , and compared to the sham group , there were decreases in oxygen consumption ( 3 . 7 [ 2 . 8 - 4 . 6 ] vs .

Example answer:
{"entities": [{"text": "bleeding", "type": "BiologicFunction"}, {"text": "hemorrhage", "type": "BiologicFunction"}, {"text": "sham", "type": "HealthCareActivity"}, {"text": "oxygen consumption", "type": "ClinicalAttribute"}]}

Example input:
Sentence: During HOV , tissue hypoxia was aggravated in the myocardium , brain , and kidneys , whereas tissue oxygenation of the liver and intestine was not influenced by volume status .

Example answer:
{"entities": [{"text": "HOV", "type": "Finding"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "myocardium", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "kidneys", "type": "AnatomicalStructure"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "intestine", "type": "AnatomicalStructure"}, {"text": "volume status", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Systemic and microcirculatory effects of blood transfusion in experimental hemorrhagic shock The microvascular reperfusion injury after retransfusion has not been completely characterized .

Example answer:
{"entities": [{"text": "microcirculatory", "type": "BiologicFunction"}, {"text": "blood transfusion", "type": "HealthCareActivity"}, {"text": "hemorrhagic shock", "type": "BiologicFunction"}, {"text": "reperfusion injury", "type": "InjuryOrPoisoning"}, {"text": "retransfusion", "type": "HealthCareActivity"}]}

Example input:
Sentence: The recovery was only complete for intestinal red blood cell velocity and sublingual total and perfused vascular densities .

Example answer:
{"entities": [{"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "red blood cell", "type": "AnatomicalStructure"}, {"text": "velocity", "type": "ClinicalAttribute"}, {"text": "sublingual", "type": "SpatialConcept"}, {"text": "perfused", "type": "HealthCareActivity"}]}

Input:
Sentence: Therefore , our goal was to characterize sublingual and intestinal ( mucosal and serosal ) microvascular injury after blood resuscitation in hemorrhagic shock and its relation with O2 and CO2 metabolism .

## Item MedMentions:test:4680
Example input:
Sentence: Through screening of 640 different Food and Drug Administration ( FDA ) - approved drugs , we found that disulfiram and diphenhydramine hydrochloride were effective candidates for inhibiting Th17 differentiation and ameliorating EAE development through upregulating miR - 30a .

Example answer:
{"entities": [{"text": "screening", "type": "HealthCareActivity"}, {"text": "Food and Drug Administration ( FDA ) - approved drugs", "type": "Chemical"}, {"text": "disulfiram", "type": "Chemical"}, {"text": "diphenhydramine hydrochloride", "type": "Chemical"}, {"text": "Th17", "type": "AnatomicalStructure"}, {"text": "differentiation", "type": "BiologicFunction"}, {"text": "EAE", "type": "BiologicFunction"}, {"text": "upregulating", "type": "BiologicFunction"}, {"text": "miR - 30a", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Skin biopsies from all the patients were evaluated before and after therapy for the expression of Ki - 67 , various skin barrier genes and thymic stromal lymphopoietin ( TSLP ) by real - time quantitative polymerase chain reaction and immunohistochemistry .

Example answer:
{"entities": [{"text": "Skin biopsies", "type": "HealthCareActivity"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "therapy", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Ki - 67", "type": "Chemical"}, {"text": "skin barrier", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "thymic stromal lymphopoietin", "type": "Chemical"}, {"text": "TSLP", "type": "Chemical"}, {"text": "real - time quantitative polymerase chain reaction", "type": "ResearchActivity"}, {"text": "immunohistochemistry", "type": "HealthCareActivity"}]}

Example input:
Sentence: We show that RA190 reduces the expression of Stat3 and the levels of key immunosuppressive enzymes and cytokines arginase , iNOS , and IL - 10 in MDSCs , while boosting expression of the immunostimulatory cytokine IL - 12 .

Example answer:
{"entities": [{"text": "RA190", "type": "Chemical"}, {"text": "Stat3", "type": "Chemical"}, {"text": "immunosuppressive", "type": "BiologicFunction"}, {"text": "enzymes", "type": "Chemical"}, {"text": "cytokines", "type": "Chemical"}, {"text": "arginase", "type": "Chemical"}, {"text": "iNOS", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "MDSCs", "type": "AnatomicalStructure"}, {"text": "immunostimulatory", "type": "HealthCareActivity"}, {"text": "cytokine", "type": "Chemical"}, {"text": "IL - 12", "type": "Chemical"}]}

Example input:
Sentence: Interestingly , no significant alterations were reported for PON2 and PON3 expression in ex vivo full - thickness healthy skin organ cultures stimulated with IL - 17 .

Example answer:
{"entities": [{"text": "PON2", "type": "AnatomicalStructure"}, {"text": "PON3", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "skin", "type": "BodySystem"}, {"text": "organ cultures", "type": "HealthCareActivity"}, {"text": "IL - 17", "type": "Chemical"}]}

Example input:
Sentence: The Treg cells isolated from the peritoneal lavage and splenocytes of the mice were treated with adenosine or the specific adenosine A2A receptor agonist , CGS21680 , and were transfected with specific siRNA targeting E2F transcription factor 1 ( E2F - 1 ) or cyclic adenosine monophosphate ( cAMP ) response element - binding protein ( CREB ) , which are predicted transcription regulatory factors of CD39 or CD73 .

Example answer:
{"entities": [{"text": "Treg cells", "type": "AnatomicalStructure"}, {"text": "peritoneal lavage", "type": "HealthCareActivity"}, {"text": "splenocytes", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "adenosine", "type": "Chemical"}, {"text": "adenosine A2A receptor agonist", "type": "Chemical"}, {"text": "CGS21680", "type": "Chemical"}, {"text": "transfected", "type": "ResearchActivity"}, {"text": "siRNA", "type": "Chemical"}, {"text": "E2F transcription factor 1", "type": "Chemical"}, {"text": "E2F - 1", "type": "Chemical"}, {"text": "cyclic adenosine monophosphate ( cAMP ) response element - binding protein", "type": "Chemical"}, {"text": "CREB", "type": "Chemical"}, {"text": "transcription regulatory factors", "type": "Chemical"}, {"text": "CD39", "type": "Chemical"}, {"text": "CD73", "type": "Chemical"}]}

Example input:
Sentence: GRIM - 19 siRNA promoted MCF - 7 cell proliferation and migration ; inhibited cell apoptosis ; and promoted the expression of STAT3 , survivin , Bcl - 2 and MMP - 9 .

Example answer:
{"entities": [{"text": "GRIM - 19", "type": "AnatomicalStructure"}, {"text": "siRNA", "type": "Chemical"}, {"text": "MCF - 7 cell", "type": "AnatomicalStructure"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "migration", "type": "BiologicFunction"}, {"text": "cell apoptosis", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "STAT3", "type": "Chemical"}, {"text": "survivin", "type": "Chemical"}, {"text": "Bcl - 2", "type": "Chemical"}, {"text": "MMP - 9", "type": "Chemical"}]}

Example input:
Sentence: Ts19 Frag - II is included is this group , which function is still uncertain .

Example answer:
{"entities": [{"text": "Ts19 Frag - II", "type": "Chemical"}]}

Example input:
Sentence: Expanding biological activities of Ts19 Frag - II toxin : Insights into IL - 17 production Tityus serrulatus ( Ts ) venom is composed of a mixture of toxins presenting diverse biological functions .

Example answer:
{"entities": [{"text": "biological activities", "type": "BiologicFunction"}, {"text": "Ts19 Frag - II toxin", "type": "Chemical"}, {"text": "IL - 17", "type": "Chemical"}, {"text": "production", "type": "BiologicFunction"}, {"text": "Tityus serrulatus", "type": "Eukaryote"}, {"text": "Ts", "type": "Eukaryote"}, {"text": "venom", "type": "Chemical"}, {"text": "toxins", "type": "Chemical"}, {"text": "biological functions", "type": "BiologicFunction"}]}

Example input:
Sentence: Our results demonstrates that mice challenged with Ts19 Frag - II presented biochemical alterations , increasing serum levels of urea , ALT and β - globulin , besides decreasing γ - globulins .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}, {"text": "Ts19 Frag - II", "type": "Chemical"}, {"text": "biochemical", "type": "BiologicFunction"}, {"text": "serum levels of urea", "type": "Finding"}, {"text": "ALT", "type": "Chemical"}, {"text": "β - globulin", "type": "Chemical"}, {"text": "γ - globulins", "type": "Chemical"}]}

Example input:
Sentence: This study expanded the biological activities of Ts19 Frag - II , suggesting that this toxin could be contributing to the Ts envenoming through alterations of biochemical parameters as well as triggering the inflammatory response .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "biological activities", "type": "BiologicFunction"}, {"text": "Ts19 Frag - II", "type": "Chemical"}, {"text": "toxin", "type": "Chemical"}, {"text": "Ts", "type": "Eukaryote"}, {"text": "envenoming", "type": "InjuryOrPoisoning"}, {"text": "inflammatory response", "type": "BiologicFunction"}]}

Input:
Sentence: This study aimed to expand the biological activities of Ts19 Frag - II through in vivo investigation .

## Item MedMentions:test:4650
Example input:
Sentence: Best RECIST responses were : 6 responses ( M - SFT = 2 of 7 , D - SFT = 4 of 5 ) , 1 stable disease , 5 progressions , with a 6 - month median progression - free survival ( M - SFT = 6 , D - SFT = 10 months ) .

Example answer:
{"entities": [{"text": "RECIST", "type": "IntellectualProduct"}, {"text": "M - SFT", "type": "BiologicFunction"}, {"text": "D - SFT", "type": "BiologicFunction"}, {"text": "stable disease", "type": "Finding"}, {"text": "progressions", "type": "BiologicFunction"}]}

Example input:
Sentence: Also , plasma lipid profiles , HbA1C , fasting plasma glucose , and insulin levels , will be measured and insulin resistance ( HOMA - IR ) and beta - cell function ( HOMA - B ) will be calculated at baseline and will be repeated at months 3 , 6 , 12 , and 18 .

Example answer:
{"entities": [{"text": "HbA1C", "type": "Chemical"}, {"text": "fasting plasma glucose", "type": "HealthCareActivity"}, {"text": "insulin", "type": "Chemical"}, {"text": "insulin resistance", "type": "HealthCareActivity"}, {"text": "HOMA - IR", "type": "HealthCareActivity"}, {"text": "beta - cell function", "type": "HealthCareActivity"}, {"text": "HOMA - B", "type": "HealthCareActivity"}]}

Example input:
Sentence: Body weight and composition , RMR , ExEff ( 10 , 25 and 50 W ) , appetite feelings and appetite - regulating hormones ( active ghrelin , cholecystokinin , total peptide YY ( PYY ) , active glucagon - like peptide - 1 and insulin ) , in fasting and every 30 min up to 2 . 5 h , were measured at baseline and after each phase .

Example answer:
{"entities": [{"text": "RMR", "type": "BiologicFunction"}, {"text": "appetite", "type": "BiologicFunction"}, {"text": "feelings", "type": "BiologicFunction"}, {"text": "appetite - regulating hormones", "type": "Chemical"}, {"text": "active ghrelin", "type": "Chemical"}, {"text": "cholecystokinin", "type": "Chemical"}, {"text": "total peptide YY", "type": "Chemical"}, {"text": "PYY", "type": "Chemical"}, {"text": "active glucagon - like peptide - 1", "type": "Chemical"}, {"text": "insulin", "type": "Chemical"}, {"text": "fasting", "type": "Finding"}]}

Example input:
Sentence: After 4 weeks , self - efficacy , health and well - being scores significantly improved : 63 % of lifestyle goals and 89 % of health management goals were fully achieved ; 58 % of referrals to community lifestyle behaviour change services and 79 % of referrals to other services ( e . g .

Example answer:
{"entities": [{"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "significantly improved", "type": "Finding"}, {"text": "goals", "type": "IntellectualProduct"}, {"text": "achieved", "type": "Finding"}, {"text": "referrals to", "type": "HealthCareActivity"}, {"text": "community", "type": "Organization"}, {"text": "services", "type": "HealthCareActivity"}]}

Example input:
Sentence: Assessment completion rates were 100 % at baseline , 59 % at 1 month , 30 % at 2 months , and 65 % at 3 months .

Example answer:
{"entities": []}

Example input:
Sentence: At 1 month , 24 ( 80 . 0 % ) and 23 ( 76 . 7 % ) patients had achieved normal MBI and MRS scores with 28 ( 93 . 3 ) and 27 ( 90 % ) patients , respectively , at 3 months .

Example answer:
{"entities": [{"text": "MBI", "type": "IntellectualProduct"}, {"text": "MRS scores", "type": "IntellectualProduct"}]}

Example input:
Sentence: Intakes of dairy were assessed by using a 196 - item food frequency questionnaire .

Example answer:
{"entities": [{"text": "Intakes of dairy", "type": "Finding"}, {"text": "196 - item food frequency questionnaire", "type": "IntellectualProduct"}]}

Example input:
Sentence: Physical activity ( questionnaire ) and food intake ( food frequency questionnaire ) were assessed .

Example answer:
{"entities": [{"text": "food", "type": "Food"}, {"text": "food frequency questionnaire", "type": "IntellectualProduct"}]}

Example input:
Sentence: NEAC was assessed by a validated food frequency questionnaire collected at baseline .

Example answer:
{"entities": [{"text": "NEAC", "type": "HealthCareActivity"}, {"text": "food frequency questionnaire", "type": "IntellectualProduct"}]}

Example input:
Sentence: Data derived from FFQ was compared to MEDAS in order to evaluate agreement or concordance between the two questionnaires .

Example answer:
{"entities": [{"text": "FFQ", "type": "IntellectualProduct"}, {"text": "MEDAS", "type": "IntellectualProduct"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "questionnaires", "type": "IntellectualProduct"}]}

Input:
Sentence: As part of the assessment , all were given a full - length Food Frequency Questionnaire ( FFQ ) and MEDAS at baseline and after 3 months .

## Item MedMentions:test:4367
Example input:
Sentence: DRibbles triggered innate receptor signaling via Toll - like Receptors ( TLR ) - 2 , TLR4 , TLR7 , TLR8 , and nucleotide - binding oligomerization domain - containing protein 2 ( NOD2 ) , but not TLR3 , TLR5 , or TLR9 .

Example answer:
{"entities": [{"text": "DRibbles", "type": "AnatomicalStructure"}, {"text": "innate receptor signaling", "type": "BiologicFunction"}, {"text": "Toll - like Receptors ( TLR ) - 2", "type": "Chemical"}, {"text": "TLR4", "type": "Chemical"}, {"text": "TLR7", "type": "Chemical"}, {"text": "TLR8", "type": "Chemical"}, {"text": "nucleotide - binding oligomerization domain - containing protein 2", "type": "Chemical"}, {"text": "NOD2", "type": "Chemical"}, {"text": "TLR3", "type": "Chemical"}, {"text": "TLR5", "type": "Chemical"}, {"text": "TLR9", "type": "Chemical"}]}

Example input:
Sentence: Starting from a homology template and set of known actives , the method introduces receptor flexibility via Normal Mode Analysis and Monte Carlo sampling , to generate a subset of pockets that display enriched discrimination of actives from inactives in retrospective docking .

Example answer:
{"entities": [{"text": "receptor", "type": "Chemical"}, {"text": "Normal Mode Analysis", "type": "ResearchActivity"}, {"text": "pockets", "type": "Chemical"}, {"text": "docking", "type": "BiologicFunction"}]}

Example input:
Sentence: G Protein - Coupled Receptor Kinase 3 and Protein Kinase C Phosphorylate the Distal C - Terminal Tail of the Chemokine Receptor CXCR4 and Mediate Recruitment of β - Arrestin Phosphorylation of G protein - coupled receptors ( GPCRs ) is a key event for cell signaling and regulation of receptor function .

Example answer:
{"entities": [{"text": "G Protein - Coupled Receptor Kinase 3", "type": "Chemical"}, {"text": "Protein Kinase C", "type": "Chemical"}, {"text": "Phosphorylate", "type": "BiologicFunction"}, {"text": "Distal", "type": "SpatialConcept"}, {"text": "C - Terminal Tail", "type": "SpatialConcept"}, {"text": "Chemokine Receptor", "type": "Chemical"}, {"text": "CXCR4", "type": "Chemical"}, {"text": "Recruitment", "type": "BiologicFunction"}, {"text": "β - Arrestin", "type": "Chemical"}, {"text": "Phosphorylation", "type": "BiologicFunction"}, {"text": "G protein - coupled receptors", "type": "Chemical"}, {"text": "GPCRs", "type": "Chemical"}, {"text": "cell signaling", "type": "BiologicFunction"}, {"text": "regulation", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , sgRNA targeting GPI anchor protein pathway genes induced loss of function mutations in human and mouse cell lines measured by FLAER labelling .

Example answer:
{"entities": [{"text": "sgRNA", "type": "Chemical"}, {"text": "GPI anchor protein pathway", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "loss of function mutations", "type": "Finding"}, {"text": "human", "type": "Eukaryote"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "cell lines", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Activation of GPR55 by its proposed endogenous ligand lysophosphatidylinositol confers pro - invasive features on breast cancer cells both in vitro and in vivo .

Example answer:
{"entities": [{"text": "GPR55", "type": "Chemical"}, {"text": "ligand", "type": "Chemical"}, {"text": "lysophosphatidylinositol", "type": "Chemical"}, {"text": "breast cancer cells", "type": "AnatomicalStructure"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: Using the activatory Gq - coupled human M3 muscarinic receptor ( hM3Dq ) , we found that chemogenetic stimulation of dSPNs mimicked , while stimulation of iSPNs abolished the therapeutic action of L - DOPA in PD mice .

Example answer:
{"entities": [{"text": "activatory Gq - coupled human M3 muscarinic receptor", "type": "Chemical"}, {"text": "hM3Dq", "type": "Chemical"}, {"text": "chemogenetic stimulation", "type": "BiologicFunction"}, {"text": "dSPNs", "type": "AnatomicalStructure"}, {"text": "stimulation", "type": "BiologicFunction"}, {"text": "iSPNs", "type": "AnatomicalStructure"}, {"text": "therapeutic action", "type": "BiologicFunction"}, {"text": "L - DOPA", "type": "Chemical"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Using melanopsin to study G protein signaling in cortical neurons Our understanding of G protein - coupled receptors ( GPCRs ) in the central nervous system ( CNS ) has been hampered by the limited availability of tools allowing for the study of their signaling with precise temporal control .

Example answer:
{"entities": [{"text": "melanopsin", "type": "Chemical"}, {"text": "study", "type": "ResearchActivity"}, {"text": "G protein signaling", "type": "BiologicFunction"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "understanding", "type": "BiologicFunction"}, {"text": "G protein - coupled receptors", "type": "Chemical"}, {"text": "GPCRs", "type": "Chemical"}, {"text": "central nervous system", "type": "BodySystem"}, {"text": "CNS", "type": "BodySystem"}, {"text": "signaling", "type": "BiologicFunction"}]}

Example input:
Sentence: We also replaced the intracellular loops of melanopsin with those of the 5 - HT2A receptor to create a light - activated GPCR capable of interacting with the 5 - HT2A receptor interacting proteins .

Example answer:
{"entities": [{"text": "intracellular", "type": "SpatialConcept"}, {"text": "loops", "type": "SpatialConcept"}, {"text": "melanopsin", "type": "Chemical"}, {"text": "5 - HT2A receptor", "type": "Chemical"}, {"text": "GPCR", "type": "Chemical"}, {"text": "proteins", "type": "Chemical"}]}

Example input:
Sentence: To gain insight into the active conformation of GPCRs , the X - ray crystal structures of Nanobody ( Nb ) -stabilized β2 - adrenergic receptor ( β2AR ) have been reported .

Example answer:
{"entities": [{"text": "conformation", "type": "SpatialConcept"}, {"text": "GPCRs", "type": "Chemical"}, {"text": "crystal structures", "type": "AnatomicalStructure"}, {"text": "Nanobody ( Nb )", "type": "Chemical"}, {"text": "β2 - adrenergic receptor", "type": "Chemical"}, {"text": "β2AR", "type": "Chemical"}]}

Example input:
Sentence: We demonstrate that peptidomimetics can structurally mimic the CDR3 loop of a Nanobody and its function by inhibiting G protein coupling as measured by partial inhibition of cAMP production .

Example answer:
{"entities": [{"text": "peptidomimetics", "type": "Chemical"}, {"text": "structurally", "type": "SpatialConcept"}, {"text": "CDR3", "type": "Chemical"}, {"text": "loop", "type": "SpatialConcept"}, {"text": "Nanobody", "type": "Chemical"}, {"text": "function", "type": "BiologicFunction"}, {"text": "inhibiting", "type": "BiologicFunction"}, {"text": "G protein coupling", "type": "BiologicFunction"}, {"text": "cAMP production", "type": "BiologicFunction"}]}

Input:
Sentence: RATIONAL DESIGN OF NANOBODY80 LOOP PEPTIDOMIMETICS : TOWARDS BIASED β2 ADRENERGIC RECEPTOR LIGANDS G protein - coupled receptors ( GPCRs ) play an important role for many cellular responses , and as such their mechanism of action is of utmost interest .

## Item MedMentions:test:4396
Example input:
Sentence: However , the combined effects of these fermentation inhibitors on the expression of ADH7 and BDH2 remain unclear .

Example answer:
{"entities": [{"text": "fermentation", "type": "BiologicFunction"}, {"text": "inhibitors", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "ADH7", "type": "AnatomicalStructure"}, {"text": "BDH2", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We determined that the glycolytic enzyme GAPDH negatively regulates HIF1A expression by binding to adenylate - uridylate - rich elements in the 3 ' - UTR region of HIF1A mRNA in glycolytically inactive TN and TCM .

Example answer:
{"entities": [{"text": "glycolytic", "type": "BiologicFunction"}, {"text": "enzyme GAPDH", "type": "Chemical"}, {"text": "HIF1A", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "binding to adenylate - uridylate - rich elements", "type": "BiologicFunction"}, {"text": "3 ' - UTR region", "type": "SpatialConcept"}, {"text": "HIF1A mRNA", "type": "AnatomicalStructure"}, {"text": "glycolytically", "type": "BiologicFunction"}, {"text": "TN", "type": "AnatomicalStructure"}, {"text": "TCM", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Loss of Dhh1 affected local translation of ASH1 mRNA and resulted in delocalization of ASH1 transcript in the bud .

Example answer:
{"entities": [{"text": "Dhh1", "type": "Chemical"}, {"text": "local translation", "type": "BiologicFunction"}, {"text": "ASH1", "type": "AnatomicalStructure"}, {"text": "mRNA", "type": "Chemical"}, {"text": "transcript", "type": "Chemical"}, {"text": "bud", "type": "Eukaryote"}]}

Example input:
Sentence: Forcibly shifting the non - polysomal ASH1 mRNA into polysomes was associated with Dhh1 dissociation .

Example answer:
{"entities": [{"text": "non - polysomal", "type": "Finding"}, {"text": "ASH1", "type": "AnatomicalStructure"}, {"text": "mRNA", "type": "Chemical"}, {"text": "polysomes", "type": "AnatomicalStructure"}, {"text": "Dhh1", "type": "Chemical"}, {"text": "dissociation", "type": "BiologicFunction"}]}

Example input:
Sentence: Additionally , adh7Δ cells were more sensitive to the combined stress than wild - type and bdh2Δ cells .

Example answer:
{"entities": [{"text": "combined stress", "type": "Finding"}, {"text": "wild - type", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Furthermore , we succeeded in improving yeast tolerance to the combined stress by controlling the expression of ALD6 with the ADH7 promoter .

Example answer:
{"entities": [{"text": "yeast", "type": "Eukaryote"}, {"text": "combined stress", "type": "Finding"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "ALD6", "type": "Chemical"}, {"text": "ADH7", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}]}

Example input:
Sentence: These results suggest that induction of the ADH7 expression plays a role in the tolerance to the combined stress of vanillin , furfural , and HMF .

Example answer:
{"entities": [{"text": "results", "type": "Finding"}, {"text": "induction", "type": "BiologicFunction"}, {"text": "ADH7", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "combined stress", "type": "Finding"}, {"text": "vanillin", "type": "Chemical"}, {"text": "furfural", "type": "Chemical"}, {"text": "HMF", "type": "Chemical"}]}

Example input:
Sentence: The protein synthesis of Adh7 , but not Bdh2 was significantly induced under combined stress conditions , even though the mRNA levels of ADH7 and BDH2 were up - regulated .

Example answer:
{"entities": [{"text": "protein synthesis", "type": "BiologicFunction"}, {"text": "Adh7", "type": "Chemical"}, {"text": "Bdh2", "type": "Chemical"}, {"text": "combined stress", "type": "Finding"}, {"text": "mRNA", "type": "Chemical"}, {"text": "ADH7", "type": "AnatomicalStructure"}, {"text": "BDH2", "type": "AnatomicalStructure"}, {"text": "up - regulated .", "type": "BiologicFunction"}]}

Example input:
Sentence: The yeast ADH7 promoter enables gene expression under pronounced translation repression caused by the combined stress of vanillin , furfural , and 5 - hydroxymethylfurfural Lignocellulosic biomass conversion inhibitors such as vanillin , furfural , and 5 - hydroxymethylfurfural ( HMF ) inhibit the growth of and fermentation by Saccharomyces cerevisiae .

Example answer:
{"entities": [{"text": "yeast", "type": "Eukaryote"}, {"text": "ADH7", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "translation repression", "type": "BiologicFunction"}, {"text": "combined stress", "type": "Finding"}, {"text": "vanillin", "type": "Chemical"}, {"text": "furfural", "type": "Chemical"}, {"text": "5 - hydroxymethylfurfural", "type": "Chemical"}, {"text": "Lignocellulosic", "type": "Chemical"}, {"text": "inhibitors", "type": "Chemical"}, {"text": "HMF", "type": "Chemical"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "fermentation", "type": "BiologicFunction"}, {"text": "Saccharomyces cerevisiae", "type": "Eukaryote"}]}

Example input:
Sentence: Our results demonstrate that the ADH7 promoter can overcome the pronounced translation repression caused by the combined stress of vanillin , furfural , and HMF , and also suggest a new gene engineering strategy to breed robust and optimized yeasts for bioethanol production from a lignocellulosic biomass .

Example answer:
{"entities": [{"text": "results", "type": "Finding"}, {"text": "ADH7", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "translation repression", "type": "BiologicFunction"}, {"text": "combined stress", "type": "Finding"}, {"text": "vanillin", "type": "Chemical"}, {"text": "furfural", "type": "Chemical"}, {"text": "HMF", "type": "Chemical"}, {"text": "gene engineering", "type": "ResearchActivity"}, {"text": "yeasts", "type": "Eukaryote"}, {"text": "bioethanol production", "type": "BiologicFunction"}, {"text": "lignocellulosic", "type": "Chemical"}]}

Input:
Sentence: We previously reported that the mRNAs of ADH7 and BDH2 , which encode putative NADPH - and NADH - dependent alcohol dehydrogenases , respectively , were efficiently translated even with translation repression in response to severe vanillin stress .

## Item MedMentions:test:4763
Example input:
Sentence: The ICC and r were highest ( ≥0 . 80 ) for 25 ( OH ) D , free 25 ( OH ) D , bioavailable 25 ( OH ) D and PTH , but somewhat lower ( approximately 0 . 60 - 0 . 75 ) for the other biomarkers .

Example answer:
{"entities": [{"text": "25 ( OH ) D", "type": "Chemical"}, {"text": "PTH", "type": "Chemical"}, {"text": "biomarkers", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The significant analytical performance of the developed nanoprobe , together with good biocompatibility and high cell - permeability , enables the present SERS probe imaging and real - time detection of ClO ( - ) and GSH in live cells upon oxidative stress .

Example answer:
{"entities": [{"text": "cell - permeability", "type": "BiologicFunction"}, {"text": "SERS probe imaging", "type": "HealthCareActivity"}, {"text": "real - time detection", "type": "HealthCareActivity"}, {"text": "ClO ( - )", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "live cells", "type": "AnatomicalStructure"}, {"text": "oxidative stress", "type": "BiologicFunction"}]}

Example input:
Sentence: The single SERS probe also shows high selectivity for ClO ( - ) and GSH detection against other reactive oxygen species and amino acids which may exist in biological systems , as well as remarkable sensitivity ascribed to a larger amount of hot spots on AuFs .

Example answer:
{"entities": [{"text": "ClO ( - )", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "amino acids", "type": "Chemical"}, {"text": "hot spots", "type": "SpatialConcept"}, {"text": "AuFs", "type": "Chemical"}]}

Example input:
Sentence: A Single Nanoprobe for Ratiometric Imaging and Biosensing of Hypochlorite and Glutathione in Live Cells Using Surface - Enhanced Raman Scattering Hypochlorite ( ClO ( - ) ) and glutathione ( GSH ) have been reported to closely correlate with oxidative stress and related diseases ; however , a clear mechanism is still unknown , mainly owing to a lack of accurate analytical methods for live cells .

Example answer:
{"entities": [{"text": "Ratiometric Imaging", "type": "HealthCareActivity"}, {"text": "Biosensing", "type": "HealthCareActivity"}, {"text": "Hypochlorite", "type": "Chemical"}, {"text": "Glutathione", "type": "Chemical"}, {"text": "Live Cells", "type": "AnatomicalStructure"}, {"text": "Surface - Enhanced Raman Scattering", "type": "HealthCareActivity"}, {"text": "ClO ( - )", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "live cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The analytical recoveries of added H2O2 in serum ( 0 . 5μM and1 . 0μM ) were 97 . 77 % and 98 . 01 % respectively and within and between batch coefficients of variation ( CV ) were 3 . 16 % and 3 .

Example answer:
{"entities": [{"text": "analytical", "type": "ResearchActivity"}, {"text": "H2O2", "type": "Chemical"}, {"text": "serum", "type": "BodySubstance"}]}

Example input:
Sentence: Two biosensor strains , Chromobacterium violaceum CV026 and Agrobacterium tumefaciens KYC55 , were used to detect the quorum sensing ( QS ) activity of H .

Example answer:
{"entities": [{"text": "biosensor strains", "type": "Bacterium"}, {"text": "Chromobacterium violaceum CV026", "type": "Bacterium"}, {"text": "Agrobacterium tumefaciens KYC55", "type": "Bacterium"}, {"text": "quorum sensing", "type": "BiologicFunction"}, {"text": "QS", "type": "BiologicFunction"}, {"text": "H .", "type": "Bacterium"}]}

Example input:
Sentence: An amperometric H2O2 biosensor was constructed by immobilizing Hb NPs covalently onto a polycrystalline Au electrode ( Au E ) .

Example answer:
{"entities": [{"text": "H2O2", "type": "Chemical"}, {"text": "immobilizing", "type": "HealthCareActivity"}, {"text": "Hb", "type": "Chemical"}, {"text": "covalently", "type": "BiologicFunction"}, {"text": "polycrystalline", "type": "Chemical"}, {"text": "Au", "type": "Chemical"}, {"text": "electrode", "type": "MedicalDevice"}, {"text": "E", "type": "MedicalDevice"}]}

Example input:
Sentence: An amperometric H2O2 biosensor based on hemoglobin nanoparticles immobilized onto a gold electrode The nanoparticles ( NPs ) of hemoglobin ( Hb ) were prepared by desolvation method and characterized by transmission electron microscopy ( TEM ) , ultraviolet ( UV ) spectroscopy and Fourier - transform infrared spectroscopy ( FTIR ) .

Example answer:
{"entities": [{"text": "H2O2", "type": "Chemical"}, {"text": "hemoglobin", "type": "Chemical"}, {"text": "immobilized", "type": "HealthCareActivity"}, {"text": "gold", "type": "Chemical"}, {"text": "electrode", "type": "MedicalDevice"}, {"text": "Hb", "type": "Chemical"}, {"text": "transmission electron microscopy", "type": "HealthCareActivity"}, {"text": "TEM", "type": "HealthCareActivity"}, {"text": "Fourier - transform infrared spectroscopy", "type": "ResearchActivity"}, {"text": "FTIR", "type": "ResearchActivity"}]}

Example input:
Sentence: The biosensor showed lower detection limit ( 1 . 0μM ) , high sensitivity ( 129±0 . 25μA cm ( - 2 ) mM ( - 1 ) ) and wider linear range ( 1 . 0 - 1200μM ) for H2O2 as compared to earlier biosensors .

Example answer:
{"entities": [{"text": "wider", "type": "SpatialConcept"}, {"text": "linear", "type": "SpatialConcept"}, {"text": "H2O2", "type": "Chemical"}]}

Example input:
Sentence: The biosensor measured H2O2 level in sera of apparently healthy subjects and persons suffering from diabetes type II .

Example answer:
{"entities": [{"text": "H2O2", "type": "Chemical"}, {"text": "sera", "type": "BodySubstance"}, {"text": "healthy subjects", "type": "PopulationGroup"}, {"text": "persons", "type": "PopulationGroup"}, {"text": "suffering", "type": "Finding"}, {"text": "diabetes type II", "type": "BiologicFunction"}]}

Input:
Sentence: There was a good correlation between sera H2O2 values obtained by standard enzymic colourimetric method and the present biosensor ( R ( 2 ) = 0 . 99 ) .

## Item MedMentions:test:4224
Example input:
Sentence: Using a short hairpin RNA strategy , we demonstrate here that the 2 mammalian RBPs , PUMILIO ( PUM ) 1 and PUM2 , members of the PUF family of posttranscriptional regulators , are essential for hematopoietic stem / progenitor cell ( HSPC ) proliferation and survival in vitro and in vivo upon reconstitution assays .

Example answer:
{"entities": [{"text": "short hairpin RNA", "type": "Chemical"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "RBPs", "type": "Chemical"}, {"text": "PUMILIO", "type": "Chemical"}, {"text": "PUM ) 1", "type": "Chemical"}, {"text": "PUM2", "type": "Chemical"}, {"text": "PUF family", "type": "Chemical"}, {"text": "posttranscriptional regulators", "type": "BiologicFunction"}, {"text": "hematopoietic stem / progenitor cell ( HSPC ) proliferation", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "reconstitution assays", "type": "HealthCareActivity"}]}

Example input:
Sentence: Exogenous HOP treatment increases proliferation and self - renewal of GSCs in a PrP ( C ) -dependent manner while HOP knockdown disturbs the proliferation process .

Example answer:
{"entities": [{"text": "HOP", "type": "Chemical"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "self - renewal", "type": "BiologicFunction"}, {"text": "GSCs", "type": "AnatomicalStructure"}, {"text": "PrP ( C )", "type": "Chemical"}, {"text": "proliferation process", "type": "BiologicFunction"}]}

Example input:
Sentence: We observed that , when GBM cells are cultured as neurospheres , they express specific stemness markers such as CD133 , CD15 , Oct4 , and SOX2 ; PrP ( C ) is upregulated compared to monolayer culture and co - localizes with CD133 .

Example answer:
{"entities": [{"text": "GBM", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "cultured", "type": "HealthCareActivity"}, {"text": "neurospheres", "type": "AnatomicalStructure"}, {"text": "stemness markers", "type": "SpatialConcept"}, {"text": "CD133", "type": "Chemical"}, {"text": "CD15", "type": "Chemical"}, {"text": "Oct4", "type": "Chemical"}, {"text": "SOX2", "type": "Chemical"}, {"text": "PrP ( C )", "type": "Chemical"}, {"text": "monolayer culture", "type": "HealthCareActivity"}]}

Example input:
Sentence: PrP ( C ) silencing downregulates the expression of molecules associated with cancer stem cells , upregulates markers of cell differentiation and affects GSC self - renewal , pointing to a pivotal role for PrP ( C ) in the maintenance of GSCs .

Example answer:
{"entities": [{"text": "PrP ( C )", "type": "Chemical"}, {"text": "silencing", "type": "BiologicFunction"}, {"text": "expression of molecules", "type": "BiologicFunction"}, {"text": "cancer stem cells", "type": "AnatomicalStructure"}, {"text": "markers", "type": "SpatialConcept"}, {"text": "cell differentiation", "type": "BiologicFunction"}, {"text": "GSC", "type": "AnatomicalStructure"}, {"text": "self - renewal", "type": "BiologicFunction"}, {"text": "GSCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We than evaluated GSC self - renewal and proliferation by clonal density assays and BrdU incorporation , respectively , in front of recombinant HOP treatment , combined or not with a HOP peptide which mimics the PrP ( C ) binding site .

Example answer:
{"entities": [{"text": "GSC", "type": "AnatomicalStructure"}, {"text": "self - renewal", "type": "BiologicFunction"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "clonal density assays", "type": "HealthCareActivity"}, {"text": "BrdU incorporation", "type": "HealthCareActivity"}, {"text": "HOP", "type": "Chemical"}, {"text": "peptide", "type": "Chemical"}, {"text": "PrP ( C )", "type": "Chemical"}, {"text": "binding site", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , PrP ( C ) -depleted GSCs downregulate cell adhesion - related proteins and impair cell migration indicating a putative role for PrP ( C ) in the cell surface stability of cell adhesion molecules and GBM cell invasiveness , respectively .

Example answer:
{"entities": [{"text": "PrP ( C )", "type": "Chemical"}, {"text": "GSCs", "type": "AnatomicalStructure"}, {"text": "cell", "type": "AnatomicalStructure"}, {"text": "adhesion - related proteins", "type": "Chemical"}, {"text": "cell migration", "type": "BiologicFunction"}, {"text": "cell surface stability", "type": "Finding"}, {"text": "cell adhesion molecules", "type": "Chemical"}, {"text": "GBM", "type": "BiologicFunction"}, {"text": "invasiveness", "type": "BiologicFunction"}]}

Example input:
Sentence: In vivo , PrP ( C ) and / or HOP knockdown potently inhibits the growth of subcutaneously implanted glioblastoma cells .

Example answer:
{"entities": [{"text": "In vivo", "type": "SpatialConcept"}, {"text": "PrP ( C )", "type": "Chemical"}, {"text": "HOP", "type": "Chemical"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "glioblastoma", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In addition , disruption of the PrP ( C ) - HOP complex by a HOP peptide , which mimics the PrP ( C ) binding site , affects GSC self - renewal and proliferation indicating that the HOP - PrP ( C ) complex is required for GSC stemness .

Example answer:
{"entities": [{"text": "PrP ( C ) - HOP complex", "type": "Chemical"}, {"text": "HOP", "type": "Chemical"}, {"text": "peptide", "type": "Chemical"}, {"text": "PrP ( C )", "type": "Chemical"}, {"text": "binding site", "type": "Chemical"}, {"text": "GSC", "type": "AnatomicalStructure"}, {"text": "self - renewal", "type": "BiologicFunction"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "HOP - PrP ( C ) complex", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , our results show that the modulation of HOP - PrP ( C ) engagement or the decrease of PrP ( C ) and HOP expression may represent a potential therapeutic intervention in GBM , regulating glioblastoma stem - like cell self - renewal , proliferation , and migration .

Example answer:
{"entities": [{"text": "HOP", "type": "Chemical"}, {"text": "PrP ( C )", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "therapeutic intervention", "type": "HealthCareActivity"}, {"text": "GBM", "type": "BiologicFunction"}, {"text": "glioblastoma stem - like cell", "type": "AnatomicalStructure"}, {"text": "self - renewal", "type": "BiologicFunction"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "migration", "type": "BiologicFunction"}]}

Example input:
Sentence: Engagement of cellular prion protein with the co - chaperone Hsp70 / 90 organizing protein regulates the proliferation of glioblastoma stem - like cells Glioblastoma ( GBM ) , a highly aggressive brain tumor , contains a subpopulation of glioblastoma stem - like cells ( GSCs ) that play roles in tumor maintenance , invasion , and therapeutic resistance .

Example answer:
{"entities": [{"text": "cellular prion protein", "type": "Chemical"}, {"text": "co - chaperone", "type": "Chemical"}, {"text": "Hsp70 / 90 organizing protein", "type": "Chemical"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "glioblastoma stem - like cells", "type": "AnatomicalStructure"}, {"text": "Glioblastoma", "type": "BiologicFunction"}, {"text": "GBM", "type": "BiologicFunction"}, {"text": "brain tumor", "type": "BiologicFunction"}, {"text": "GSCs", "type": "AnatomicalStructure"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "invasion", "type": "BiologicFunction"}, {"text": "therapeutic resistance", "type": "BiologicFunction"}]}

Input:
Sentence: Our group identified the cellular prion protein ( PrP ( C ) ) and its partner , the co - chaperone Hsp70 / 90 organizing protein ( HOP ) , as potential target candidates due to their role in GBM tumorigenesis and in neural stem cell maintenance .

## Item MedMentions:test:4765
Example input:
Sentence: In this study , we showed that TEA and 4 - AP insensitive non - inactivating outward K ( + ) current ( NIOK ) may be responsible for the quiescence of murine pregnant longitudinal myometrium .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "TEA", "type": "Chemical"}, {"text": "4 - AP", "type": "Chemical"}, {"text": "insensitive", "type": "Finding"}, {"text": "non - inactivating outward K ( + ) current", "type": "BiologicFunction"}, {"text": "NIOK", "type": "BiologicFunction"}, {"text": "quiescence", "type": "BiologicFunction"}, {"text": "murine", "type": "Eukaryote"}, {"text": "pregnant", "type": "AnatomicalStructure"}, {"text": "longitudinal", "type": "SpatialConcept"}, {"text": "myometrium", "type": "AnatomicalStructure"}]}

Example input:
Sentence: PMCs exposed to 35 ° C were less likely to progress than those exposed to 30 ° C .

Example answer:
{"entities": [{"text": "PMCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Chinese Spring ) , defines a heat - sensitive stage and evaluates the role of chromosome 5D in heat tolerance .

Example answer:
{"entities": [{"text": "Chinese Spring", "type": "Eukaryote"}, {"text": "chromosome 5D", "type": "AnatomicalStructure"}, {"text": "heat tolerance", "type": "BiologicFunction"}]}

Example input:
Sentence: Exposure of wheat to high temperatures during male meiosis prevents normal meiotic progression and reduces grain number .

Example answer:
{"entities": [{"text": "wheat", "type": "Eukaryote"}, {"text": "male meiosis", "type": "BiologicFunction"}, {"text": "meiotic progression", "type": "BiologicFunction"}, {"text": "grain", "type": "Eukaryote"}]}

Example input:
Sentence: Chinese Spring nullisomic 5D - tetrasomic 5B ( N5DT5B ) plants , which lack chromosome 5D , were more susceptible to heat during premeiosis - leptotene than Chinese Spring plants with the normal ( euploid ) chromosome complement .

Example answer:
{"entities": [{"text": "Chinese", "type": "SpatialConcept"}, {"text": "Spring nullisomic 5D - tetrasomic 5B ( N5DT5B ) plants", "type": "Eukaryote"}, {"text": "chromosome 5D", "type": "AnatomicalStructure"}, {"text": "premeiosis", "type": "BiologicFunction"}, {"text": "leptotene", "type": "BiologicFunction"}, {"text": "Spring plants", "type": "Eukaryote"}]}

Example input:
Sentence: Short periods of high temperature during meiosis prevent normal meiotic progression and reduce grain number in hexaploid wheat ( Triticum aestivum L . )

Example answer:
{"entities": [{"text": "meiosis", "type": "BiologicFunction"}, {"text": "meiotic progression", "type": "BiologicFunction"}, {"text": "grain", "type": "Eukaryote"}, {"text": "hexaploid wheat", "type": "Eukaryote"}, {"text": "Triticum aestivum L .", "type": "Eukaryote"}]}

Example input:
Sentence: We define a temperature - sensitive period and link heat tolerance to chromosome 5D .

Example answer:
{"entities": [{"text": "heat tolerance", "type": "BiologicFunction"}, {"text": "chromosome 5D", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Examination of pollen mother cells ( PMCs ) from immature anthers immediately before and after heat treatment enabled precise identification of the developmental phases being exposed to heat .

Example answer:
{"entities": [{"text": "pollen mother cells", "type": "AnatomicalStructure"}, {"text": "PMCs", "type": "AnatomicalStructure"}, {"text": "anthers", "type": "Eukaryote"}]}

Example input:
Sentence: Plants were exposed to high temperatures ( 30 or 35 ° C ) in a controlled environment room for 20 - h periods during meiosis and the premeiotic interphase just prior to meiosis .

Example answer:
{"entities": [{"text": "Plants", "type": "Eukaryote"}, {"text": "meiosis", "type": "BiologicFunction"}, {"text": "premeiotic interphase", "type": "BiologicFunction"}]}

Example input:
Sentence: The proportion of plants with PMCs progressing through meiosis after heat treatment was lower for N5DT5B plants than for euploids , but the difference was not significant .

Example answer:
{"entities": [{"text": "plants", "type": "Eukaryote"}, {"text": "PMCs", "type": "AnatomicalStructure"}, {"text": "meiosis", "type": "BiologicFunction"}, {"text": "N5DT5B plants", "type": "Eukaryote"}, {"text": "not significant", "type": "Finding"}]}

Input:
Sentence: A temperature - sensitive period was defined , lasting from premeiotic interphase to late leptotene , during which heat can prevent PMCs from progressing through meiosis .

## Item MedMentions:test:4486
Example input:
Sentence: Porphyromonus gingivalis ( P . gingivalis ) , a major periodontal pathogen , has already been shown to have a significant role in the inflammatory response of CAD in vivo .

Example answer:
{"entities": [{"text": "Porphyromonus gingivalis", "type": "Bacterium"}, {"text": "P . gingivalis", "type": "Bacterium"}, {"text": "inflammatory response", "type": "BiologicFunction"}, {"text": "CAD", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: After initial therapy ( scaling and root planning and oral hygiene instructions ) , periodontal indices including bleeding on probing ( BOP ) , periodontal pocket depth ( PPD ) and modified gingival index ( MGI ) were recorded .

Example answer:
{"entities": [{"text": "therapy", "type": "HealthCareActivity"}, {"text": "scaling", "type": "HealthCareActivity"}, {"text": "root planning", "type": "HealthCareActivity"}, {"text": "oral hygiene instructions", "type": "HealthCareActivity"}, {"text": "periodontal indices", "type": "Finding"}, {"text": "bleeding on probing", "type": "Finding"}, {"text": "BOP", "type": "Finding"}, {"text": "periodontal pocket depth", "type": "Finding"}, {"text": "PPD", "type": "Finding"}, {"text": "modified gingival index", "type": "Finding"}, {"text": "MGI", "type": "Finding"}]}

Example input:
Sentence: Salivary Colony Stimulating Factor - 1 , Interleukin - 34 , and Matrix Metalloproteinase - 8 as Markers of Periodontal Disease Colony - stimulating factor ( CSF ) - 1 and interleukin ( IL ) - 34 are macrophage growth factors and regulators of osteoclastogenesis .

Example answer:
{"entities": [{"text": "Salivary", "type": "SpatialConcept"}, {"text": "Colony Stimulating Factor - 1", "type": "Chemical"}, {"text": "Interleukin - 34", "type": "Chemical"}, {"text": "Matrix Metalloproteinase - 8", "type": "Chemical"}, {"text": "Markers", "type": "ClinicalAttribute"}, {"text": "Periodontal Disease", "type": "BiologicFunction"}, {"text": "Colony - stimulating factor ( CSF ) - 1", "type": "Chemical"}, {"text": "interleukin ( IL ) - 34", "type": "Chemical"}, {"text": "macrophage", "type": "AnatomicalStructure"}, {"text": "growth factors", "type": "Chemical"}, {"text": "osteoclastogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Higher CSF - 1 / IL - 34 ratio was observed in periodontitis patients compared to healthy .

Example answer:
{"entities": [{"text": "CSF - 1", "type": "Chemical"}, {"text": "IL - 34", "type": "Chemical"}, {"text": "periodontitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Clinical periodontal parameters correlated positively to CSF - 1 , MMP - 8 , and to the CSF - 1 / IL - 34 ratio and negatively to IL - 34 in periodontitis patients .

Example answer:
{"entities": [{"text": "CSF - 1", "type": "Chemical"}, {"text": "MMP - 8", "type": "Chemical"}, {"text": "IL - 34", "type": "Chemical"}, {"text": "periodontitis", "type": "BiologicFunction"}]}

Example input:
Sentence: The aim of this study was to explore the presence of CSF - 1 and IL - 34 in whole saliva in relation to periodontal disease .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "CSF - 1", "type": "Chemical"}, {"text": "IL - 34", "type": "Chemical"}, {"text": "saliva", "type": "BodySubstance"}, {"text": "periodontal disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Following treatment CSF - 1 and MMP - 8 levels decreased along with clinical improvement in gingivitis patients .

Example answer:
{"entities": [{"text": "CSF - 1", "type": "Chemical"}, {"text": "MMP - 8", "type": "Chemical"}, {"text": "gingivitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Salivary CSF - 1 , IL - 34 , and matrix metalloproteinase ( MMP ) - 8 , a biomarker candidate of periodontitis , were determined in 48 patients ( 29 periodontitis , 12 gingivitis , 7 healthy ) and related to the clinical periodontal parameters bleeding on probing ( BOP ) , probing depth ( PD ) , clinical attachment loss ( AL ) , and plaque index ( PI ) .

Example answer:
{"entities": [{"text": "Salivary", "type": "SpatialConcept"}, {"text": "CSF - 1", "type": "Chemical"}, {"text": "IL - 34", "type": "Chemical"}, {"text": "matrix metalloproteinase ( MMP ) - 8", "type": "Chemical"}, {"text": "biomarker", "type": "ClinicalAttribute"}, {"text": "periodontitis", "type": "BiologicFunction"}, {"text": "gingivitis", "type": "BiologicFunction"}, {"text": "bleeding on probing", "type": "Finding"}, {"text": "BOP", "type": "Finding"}, {"text": "attachment loss", "type": "BiologicFunction"}, {"text": "AL", "type": "BiologicFunction"}, {"text": "plaque index", "type": "IntellectualProduct"}, {"text": "PI", "type": "IntellectualProduct"}]}

Example input:
Sentence: There was a positive correlation between CSF - 1 and MMP - 8 which both correlated negatively to IL - 34 , in gingivitis and periodontitis .

Example answer:
{"entities": [{"text": "CSF - 1", "type": "Chemical"}, {"text": "MMP - 8", "type": "Chemical"}, {"text": "IL - 34", "type": "Chemical"}, {"text": "gingivitis", "type": "BiologicFunction"}, {"text": "periodontitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Periodontitis patients displayed higher CSF - 1 and MMP - 8 levels in saliva compared to healthy , while IL - 34 levels were lower .

Example answer:
{"entities": [{"text": "Periodontitis", "type": "BiologicFunction"}, {"text": "CSF - 1", "type": "Chemical"}, {"text": "MMP - 8", "type": "Chemical"}, {"text": "saliva", "type": "BodySubstance"}, {"text": "IL - 34", "type": "Chemical"}]}

Input:
Sentence: An additional separate group of gingivitis ( n = 21 ) and part of periodontitis patients ( n = 11 ) were subjected to non - surgical periodontal treatment whereupon changes in salivary CSF - 1 , IL - 34 , and MMP - 8 levels were determined and related to periodontal outcome .

## Item MedMentions:test:4692
Example input:
Sentence: Spinal versus general anaesthesia in surgery for inguinodynia ( SPINASIA trial ) : study protocol for a randomised controlled trial Chronic inguinodynia ( groin pain ) is a common complication following open inguinal hernia repair or a Pfannenstiel incision but may also be experienced after other types of ( groin ) surgery .

Example answer:
{"entities": [{"text": "Spinal", "type": "HealthCareActivity"}, {"text": "general anaesthesia", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "inguinodynia", "type": "Finding"}, {"text": "SPINASIA trial", "type": "ResearchActivity"}, {"text": "study protocol", "type": "IntellectualProduct"}, {"text": "randomised controlled trial", "type": "ResearchActivity"}, {"text": "Chronic inguinodynia", "type": "Finding"}, {"text": "groin pain", "type": "Finding"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "open inguinal hernia repair", "type": "HealthCareActivity"}, {"text": "Pfannenstiel incision", "type": "HealthCareActivity"}, {"text": "groin", "type": "SpatialConcept"}]}

Example input:
Sentence: Validated model -based comparisons were performed to compare vessel - sparing results to nerve - sparing RP and conventional radiotherapy .

Example answer:
{"entities": [{"text": "Validated model", "type": "IntellectualProduct"}, {"text": "vessel - sparing", "type": "HealthCareActivity"}, {"text": "nerve - sparing RP", "type": "HealthCareActivity"}, {"text": "conventional radiotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: This randomised controlled trial is designed to study the effect of type of anaesthesia ( spinal or general ) on pain relief following remedial surgery for inguinodynia .

Example answer:
{"entities": [{"text": "randomised controlled trial", "type": "ResearchActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "type of anaesthesia", "type": "IntellectualProduct"}, {"text": "spinal", "type": "HealthCareActivity"}, {"text": "general", "type": "HealthCareActivity"}, {"text": "pain relief", "type": "HealthCareActivity"}, {"text": "remedial surgery", "type": "HealthCareActivity"}, {"text": "inguinodynia", "type": "Finding"}]}

Example input:
Sentence: Vessel - sparing radiotherapy appears to more effectively preserve erectile function when compared to historical series and model -predicted outcomes following nerve - sparing RP or conventional radiotherapy , with maintenance of tumor control .

Example answer:
{"entities": [{"text": "Vessel - sparing radiotherapy", "type": "HealthCareActivity"}, {"text": "erectile function", "type": "BiologicFunction"}, {"text": "model", "type": "IntellectualProduct"}, {"text": "nerve - sparing RP", "type": "HealthCareActivity"}, {"text": "conventional radiotherapy", "type": "HealthCareActivity"}, {"text": "tumor control", "type": "Finding"}]}

Example input:
Sentence: However , it also promotes accelerated senescence in healthy tissues and leads to progressive cognitive dysfunction in up to 50 % of tumor patients surviving long term after treatment , due to γ - irradiation -induced cerebromicrovascular injury .

Example answer:
{"entities": [{"text": "senescence", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "cognitive dysfunction", "type": "BiologicFunction"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: CyberKnife stereotactic radiosurgery for the treatment of symptomatic vertebral hemangiomas : a single - institution experience OBJECTIVE Symptomatic vertebral hemangiomas ( SVHs ) are a very rare pathology that can present with persistent pain or neurological deficits that warrant surgical intervention .

Example answer:
{"entities": [{"text": "CyberKnife stereotactic radiosurgery", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "vertebral hemangiomas", "type": "BiologicFunction"}, {"text": "SVHs", "type": "BiologicFunction"}, {"text": "very rare", "type": "Finding"}, {"text": "pathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "persistent pain", "type": "Finding"}, {"text": "neurological deficits", "type": "Finding"}, {"text": "surgical intervention", "type": "Finding"}]}

Example input:
Sentence: Following radiosurgery , 4 of 5 patients exhibited improvement in their primary symptoms ( 3 for pain and 1 for weakness ) , achieving a clinical response after a mean period of 1 year .

Example answer:
{"entities": [{"text": "radiosurgery", "type": "HealthCareActivity"}, {"text": "pain", "type": "Finding"}, {"text": "weakness", "type": "Finding"}, {"text": "clinical response", "type": "Finding"}]}

Example input:
Sentence: Patients received vessel - sparing radiotherapy utilizing a planning MRI and MRI - angiogram to delineate and avoid the erectile vasculature .

Example answer:
{"entities": [{"text": "vessel - sparing radiotherapy", "type": "HealthCareActivity"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "angiogram", "type": "HealthCareActivity"}, {"text": "erectile", "type": "BiologicFunction"}, {"text": "vasculature", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Acute clinical adverse radiation effects after Gamma Knife surgery for vestibular schwannomas OBJECTIVE Vestibular schwannomas ( VSs ) represent a common indication of Gamma Knife surgery ( GKS ) .

Example answer:
{"entities": [{"text": "adverse radiation effects", "type": "InjuryOrPoisoning"}, {"text": "Gamma Knife surgery", "type": "HealthCareActivity"}, {"text": "vestibular schwannomas", "type": "BiologicFunction"}, {"text": "Vestibular schwannomas", "type": "BiologicFunction"}, {"text": "VSs", "type": "BiologicFunction"}, {"text": "GKS", "type": "HealthCareActivity"}]}

Example input:
Sentence: To determine pain control and side effects after gamma knife radiosurgery ( GKRS ) for classical idiopathic trigeminal neuralgia ( TN ) with or without neurovascular compression ( NVC ) .

Example answer:
{"entities": [{"text": "pain control", "type": "HealthCareActivity"}, {"text": "side effects", "type": "BiologicFunction"}, {"text": "gamma knife radiosurgery", "type": "HealthCareActivity"}, {"text": "GKRS", "type": "HealthCareActivity"}, {"text": "idiopathic trigeminal neuralgia", "type": "BiologicFunction"}, {"text": "TN", "type": "BiologicFunction"}, {"text": "neurovascular compression", "type": "BiologicFunction"}, {"text": "NVC", "type": "BiologicFunction"}]}

Input:
Sentence: Gamma Knife Radiosurgery for Idiopathic Trigeminal Neuralgia ; does the status of offending vessels influence on pain control or side effects ?

## Item MedMentions:test:4758
Example input:
Sentence: The performance of a 32R method can be estimated by comparing it to an accurate reference or gold standard method ( usually based on fiducial markers ) on the same set of images ( gold standard dataset ) .

Example answer:
{"entities": [{"text": "gold standard method", "type": "HealthCareActivity"}, {"text": "fiducial markers", "type": "MedicalDevice"}, {"text": "images", "type": "IntellectualProduct"}, {"text": "gold", "type": "Chemical"}, {"text": "dataset", "type": "IntellectualProduct"}]}

Example input:
Sentence: The study showed that modelled NH3 concentrations provide more accurate estimations of true exposure than distances - based surrogates , and that distance - based surrogates ( especially those based on distance to the closest point source ) are imprecise methods to identify exposed populations , although they may be useful for initial studies .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "NH3", "type": "Chemical"}, {"text": "exposure", "type": "InjuryOrPoisoning"}, {"text": "source", "type": "Finding"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: Using nPCR as the gold standard technique , the sensitivity of microscopy and RDT was 90 and 70 % , and the specificity was 98 .

Example answer:
{"entities": [{"text": "nPCR", "type": "ResearchActivity"}, {"text": "microscopy", "type": "HealthCareActivity"}, {"text": "RDT", "type": "HealthCareActivity"}]}

Example input:
Sentence: nonspecific sources of contrast through ratiometric imaging of targeted and untargeted ( control ) NP pairs .

Example answer:
{"entities": [{"text": "ratiometric imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: The analytical method was validated by measuring several parameters including limit of detection ( LOD ) , limit of quantification ( LOQ ) , linearity , relative bias , and repeatability .

Example answer:
{"entities": [{"text": "validated", "type": "ResearchActivity"}, {"text": "parameters", "type": "Finding"}]}

Example input:
Sentence: The differences were also significant when the MTB / RIF method was compared with the smear method ( χ ( 2 ) = 88 . 60 , P < 0 . 01 ) or compared with culture plus smear methods ( χ ( 2 ) = 4 . 26 , P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "MTB / RIF method", "type": "HealthCareActivity"}, {"text": "smear method", "type": "HealthCareActivity"}, {"text": "culture plus smear methods", "type": "HealthCareActivity"}]}

Example input:
Sentence: Recently , ' paired - agent ' methods -which employ co - administration of a control ( untargeted ) imaging agent -have been applied to thick - sample staining applications to account for background staining .

Example answer:
{"entities": [{"text": "paired - agent ' methods", "type": "HealthCareActivity"}, {"text": "control ( untargeted ) imaging agent", "type": "Chemical"}, {"text": "sample staining", "type": "HealthCareActivity"}]}

Example input:
Sentence: Rinsing paired - agent model ( RPAM ) to quantify cell - surface receptor concentrations in topical staining applications of thick tissues Conventional molecular assessment of tissue through histology , if adapted to fresh thicker samples , has the potential to enhance cancer detection in surgical margins and monitoring of 3D cell culture molecular environments .

Example answer:
{"entities": [{"text": "Rinsing paired - agent model", "type": "IntellectualProduct"}, {"text": "RPAM", "type": "IntellectualProduct"}, {"text": "cell - surface receptor", "type": "Chemical"}, {"text": "topical", "type": "SpatialConcept"}, {"text": "staining", "type": "HealthCareActivity"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "molecular assessment", "type": "HealthCareActivity"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "histology", "type": "HealthCareActivity"}, {"text": "fresh thicker samples", "type": "BodySubstance"}, {"text": "cancer detection", "type": "HealthCareActivity"}, {"text": "surgical margins", "type": "AnatomicalStructure"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "3D cell culture", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here , a new simplified mathematical model - the rinsing paired - agent model ( RPAM ) - is derived and tested that offers a good balance between the previous models , is adaptable to arbitrary rinsing - imaging protocols , and does not require calibration of the imaging system .

Example answer:
{"entities": [{"text": "mathematical model - the rinsing paired - agent model", "type": "IntellectualProduct"}, {"text": "RPAM", "type": "IntellectualProduct"}, {"text": "models", "type": "IntellectualProduct"}]}

Example input:
Sentence: This work supports the use of RPAM as a preferable model to quantitatively analyze targeted biomarker concentrations in topically stained thick tissues , as it was found to match the accuracy of the complex paired - agent kinetic model while retaining the low noise - sensitivity characteristics of the ratiometric method .

Example answer:
{"entities": [{"text": "RPAM", "type": "IntellectualProduct"}, {"text": "model", "type": "IntellectualProduct"}, {"text": "biomarker", "type": "ClinicalAttribute"}, {"text": "topically", "type": "SpatialConcept"}, {"text": "stained", "type": "HealthCareActivity"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "paired - agent kinetic model", "type": "IntellectualProduct"}]}

Input:
Sentence: To date , these methods have included ( 1 ) a simple ratiometric method that is relatively insensitive to noise in the data but has accuracy that is dependent on the staining protocol and the characteristics of the sample ; and ( 2 ) a complex paired - agent kinetic modeling method that is more accurate but is more noise - sensitive and requires a precise serial rinsing protocol .

## Item MedMentions:test:4757
Example input:
Sentence: Tenofovir alafenamide versus tenofovir disoproxil fumarate for the treatment of HBeAg - positive chronic hepatitis B virus infection : a randomised , double - blind , phase 3 , non - inferiority trial Tenofovir alafenamide is a novel prodrug formulated to deliver the active metabolite to target cells more efficiently than tenofovir disoproxil fumarate at a lower dose , thereby reducing systemic exposure .

Example answer:
{"entities": [{"text": "Tenofovir alafenamide", "type": "Chemical"}, {"text": "tenofovir disoproxil fumarate", "type": "Chemical"}, {"text": "HBeAg - positive", "type": "Finding"}, {"text": "chronic hepatitis B virus infection", "type": "BiologicFunction"}, {"text": "randomised", "type": "ResearchActivity"}, {"text": "double - blind", "type": "ResearchActivity"}, {"text": "phase 3", "type": "ResearchActivity"}, {"text": "non - inferiority trial", "type": "ResearchActivity"}, {"text": "prodrug", "type": "Chemical"}, {"text": "formulated", "type": "ResearchActivity"}, {"text": "metabolite", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: However , DBP and MBP showed significant increases in patients when prophylactic atropine was administrated .

Example answer:
{"entities": [{"text": "DBP", "type": "ClinicalAttribute"}, {"text": "MBP", "type": "Finding"}, {"text": "patients", "type": "Chemical"}, {"text": "prophylactic", "type": "HealthCareActivity"}, {"text": "atropine", "type": "Chemical"}, {"text": "administrated", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of this multicenter phase II study was to assess effectiveness , safety , and tolerability of protracted dual NK1 - receptor and 5 - HT3 antagonist prophylaxis against UA - RINV .

Example answer:
{"entities": [{"text": "multicenter phase II study", "type": "ResearchActivity"}, {"text": "tolerability", "type": "ResearchActivity"}, {"text": "protracted dual NK1 - receptor", "type": "Chemical"}, {"text": "5 - HT3 antagonist", "type": "Chemical"}, {"text": "prophylaxis", "type": "HealthCareActivity"}, {"text": "UA - RINV", "type": "HealthCareActivity"}]}

Example input:
Sentence: Among transcriptional repressors , triptolide , a covalent inhibitor of ERCC3 , was most consistently effective in vitro and in vivo causing prolonged complete regression in multiple PDX models resistant to standard PDAC therapies .

Example answer:
{"entities": [{"text": "transcriptional repressors", "type": "Chemical"}, {"text": "triptolide", "type": "Chemical"}, {"text": "covalent inhibitor", "type": "Chemical"}, {"text": "ERCC3", "type": "Chemical"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "prolonged complete regression", "type": "Finding"}, {"text": "PDX", "type": "HealthCareActivity"}, {"text": "models", "type": "IntellectualProduct"}, {"text": "PDAC", "type": "BiologicFunction"}, {"text": "therapies", "type": "HealthCareActivity"}]}

Example input:
Sentence: β - Blockers may be useful in HTN patients having a hyperkinetic circulation ( palpitations , tachycardia , HTN , and anxiety ) , migraine headache , and essential tremor .

Example answer:
{"entities": [{"text": "β - Blockers", "type": "Chemical"}, {"text": "HTN", "type": "BiologicFunction"}, {"text": "circulation", "type": "BiologicFunction"}, {"text": "palpitations", "type": "Finding"}, {"text": "tachycardia", "type": "BiologicFunction"}, {"text": "anxiety", "type": "Finding"}, {"text": "migraine headache", "type": "BiologicFunction"}, {"text": "essential tremor", "type": "BiologicFunction"}]}

Example input:
Sentence: According to the MTC analysis , TDR may be the most effective treatment and PT the least effective treatment for chronic LBP .

Example answer:
{"entities": [{"text": "MTC analysis", "type": "ResearchActivity"}, {"text": "TDR", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "PT", "type": "HealthCareActivity"}, {"text": "chronic LBP", "type": "BiologicFunction"}]}

Example input:
Sentence: The side effect profile for divalproex sodium was associated with the smallest willingness to take , with gabapentin , propranolol , and topiramate perceived to be much more agreeable .

Example answer:
{"entities": [{"text": "side effect", "type": "BiologicFunction"}, {"text": "profile", "type": "HealthCareActivity"}, {"text": "divalproex sodium", "type": "Chemical"}, {"text": "smallest willingness to take", "type": "Finding"}, {"text": "gabapentin", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "topiramate", "type": "Chemical"}]}

Example input:
Sentence: Acute therapy of chronic migraine is similar to episodic migraine , except that medication overuse is a much greater risk in chronic migraine and must be addressed .

Example answer:
{"entities": [{"text": "therapy", "type": "HealthCareActivity"}, {"text": "chronic migraine", "type": "BiologicFunction"}, {"text": "migraine", "type": "BiologicFunction"}]}

Example input:
Sentence: The Food and Drug Administration has approved several different medications for migraine prophylaxis , but it is not clear whether sufferers perceive these treatments to provide clinically significant benefits given their side effect profiles .

Example answer:
{"entities": [{"text": "Food and Drug Administration", "type": "Organization"}, {"text": "medications", "type": "Chemical"}, {"text": "migraine", "type": "BiologicFunction"}, {"text": "prophylaxis", "type": "HealthCareActivity"}, {"text": "treatments", "type": "HealthCareActivity"}, {"text": "side effect", "type": "BiologicFunction"}, {"text": "profiles", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using a graphical risk tool to examine willingness to take migraine prophylactic medications Many migraine sufferers use daily prophylactic therapy to reduce the frequency of their headache attacks .

Example answer:
{"entities": [{"text": "willingness to take", "type": "Finding"}, {"text": "migraine", "type": "BiologicFunction"}, {"text": "prophylactic", "type": "HealthCareActivity"}, {"text": "medications", "type": "Chemical"}, {"text": "prophylactic therapy", "type": "HealthCareActivity"}, {"text": "headache", "type": "Finding"}]}

Input:
Sentence: The two prophylactic drugs with the best evidence for efficacy in chronic migraine are topiramate and onabotulinumtoxinA .

## Item MedMentions:test:4559
Example input:
Sentence: This study provides preliminary evidence that web - based computer - tailored interventions can be used to increase physical activity among breast cancer survivors .

Example answer:
{"entities": [{"text": "interventions", "type": "HealthCareActivity"}, {"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: A comparative effectiveness study was conducted to determine if virtual reality technology itself improved outcomes , or if similar results could be achieved with a control exposure therapy ( CET ) condition .

Example answer:
{"entities": [{"text": "comparative effectiveness study", "type": "ResearchActivity"}, {"text": "improved", "type": "Finding"}, {"text": "control exposure therapy", "type": "HealthCareActivity"}, {"text": "CET", "type": "HealthCareActivity"}]}

Example input:
Sentence: Integrating Evidence From Systematic Reviews , Qualitative Research , and Expert Knowledge Using Co - Design Techniques to Develop a Web -Based Intervention for People in the Retirement Transition Integrating stakeholder involvement in complex health intervention design maximizes acceptability and potential effectiveness .

Example answer:
{"entities": [{"text": "Systematic Reviews", "type": "IntellectualProduct"}, {"text": "Qualitative Research", "type": "ResearchActivity"}, {"text": "Expert", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Knowledge", "type": "IntellectualProduct"}, {"text": "Intervention", "type": "HealthCareActivity"}, {"text": "People", "type": "PopulationGroup"}, {"text": "Retirement", "type": "Finding"}, {"text": "stakeholder", "type": "PopulationGroup"}, {"text": "intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: The purpose of the study is to investigate the impact of differing delivery schedules of computer - tailored physical activity modules on engagement and physical activity behaviour change in a web - based intervention targeting breast cancer survivors .

Example answer:
{"entities": [{"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: This can be partly attributed to poor clinician awareness and knowledge of CFS and related CBT and GET interventions .

Example answer:
{"entities": [{"text": "knowledge", "type": "IntellectualProduct"}, {"text": "CFS", "type": "BiologicFunction"}, {"text": "CBT", "type": "HealthCareActivity"}, {"text": "GET", "type": "HealthCareActivity"}, {"text": "interventions", "type": "HealthCareActivity"}]}

Example input:
Sentence: We randomized four primary care sites to training or wait - list conditions ; PCPs at wait - list sites were trained after reassessment .

Example answer:
{"entities": [{"text": "primary care sites", "type": "Organization"}, {"text": "PCPs", "type": "ProfessionalOrOccupationalGroup"}, {"text": "reassessment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The primary outcomes will be : 1 ) knowledge and clinical reasoning skills regarding CFS and its management , measured at baseline , postintervention and follow - up , and 2 ) self - reported confidence in knowledge and clinical reasoning skills related to CFS .

Example answer:
{"entities": [{"text": "knowledge", "type": "IntellectualProduct"}, {"text": "CFS", "type": "BiologicFunction"}, {"text": "management", "type": "HealthCareActivity"}, {"text": "postintervention", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "self - reported", "type": "ResearchActivity"}, {"text": "confidence", "type": "BiologicFunction"}]}

Example input:
Sentence: The key benefit of the pdf article intervention was raising doctors ' reflection on limitations in their communication skills , whereas e - learning was more effective in changing their perception of older patients ' proactive attitude , especially among GPs working in privately owned facilities and having a greater number of assigned patients .

Example answer:
{"entities": [{"text": "pdf article", "type": "IntellectualProduct"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "doctors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "older", "type": "PopulationGroup"}, {"text": "GPs", "type": "ProfessionalOrOccupationalGroup"}, {"text": "privately owned facilities", "type": "Organization"}]}

Example input:
Sentence: Although there is level 1 evidence of the benefit of cognitive behaviour therapy ( CBT ) and graded exercise therapy ( GET ) for some people with CFS , uptake of these interventions is low or at best untimely .

Example answer:
{"entities": [{"text": "level 1", "type": "IntellectualProduct"}, {"text": "cognitive behaviour therapy", "type": "HealthCareActivity"}, {"text": "CBT", "type": "HealthCareActivity"}, {"text": "graded exercise therapy", "type": "HealthCareActivity"}, {"text": "GET", "type": "HealthCareActivity"}, {"text": "people", "type": "PopulationGroup"}, {"text": "CFS", "type": "BiologicFunction"}, {"text": "interventions", "type": "HealthCareActivity"}]}

Example input:
Sentence: The influence of the education programme on clinical practice behaviour , and self - reported success in the management of people with CFS , will also be assessed in a cohort study design with participants from the intervention and control groups combined .

Example answer:
{"entities": [{"text": "self - reported", "type": "ResearchActivity"}, {"text": "management", "type": "HealthCareActivity"}, {"text": "people", "type": "PopulationGroup"}, {"text": "CFS", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "intervention", "type": "HealthCareActivity"}]}

Input:
Sentence: This trial aims to evaluate the effect of participation in an online education programme , compared with a wait - list control group , on allied health professionals ' knowledge about evidence - based CFS interventions and their levels of confidence to engage in the dissemination of these interventions .

## Item MedMentions:test:4237
Example input:
Sentence: The medical records of 15 consecutive patients with degenerative lumbar kyphoscoliosis ( DLKS ) who had undergone posterior spinal corrective surgery using a multileve l TLIF with an RR technique and who had a minimum follow - up of 2 years were retrospectively reviewed .

Example answer:
{"entities": [{"text": "medical records", "type": "IntellectualProduct"}, {"text": "degenerative lumbar kyphoscoliosis", "type": "Finding"}, {"text": "DLKS", "type": "Finding"}, {"text": "posterior", "type": "SpatialConcept"}, {"text": "spinal", "type": "SpatialConcept"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Posterior corrective surgery with a multilevel transforaminal lumbar interbody fusion and a rod rotation maneuver for patients with degenerative lumbar kyphoscoliosis The purpose of this study was to assess the clinical results of posterior corrective surgery using a multilevel transforaminal lumbar interbody fusion ( TLIF ) with a rod rotation ( RR ) and to evaluate the segmental corrective effect of a TLIF using CT imaging .

Example answer:
{"entities": [{"text": "Posterior", "type": "SpatialConcept"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "degenerative lumbar kyphoscoliosis", "type": "Finding"}, {"text": "clinical results", "type": "Finding"}, {"text": "posterior", "type": "SpatialConcept"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "segmental", "type": "SpatialConcept"}]}

Example input:
Sentence: The BDUA + TLIF group had significantly less blood loss , shorter length of postoperative hospital stay , and lower complication rate compared with the laminectomy + PLIF group .

Example answer:
{"entities": [{"text": "BDUA", "type": "HealthCareActivity"}, {"text": "TLIF", "type": "HealthCareActivity"}, {"text": "blood loss", "type": "Finding"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "laminectomy", "type": "HealthCareActivity"}, {"text": "PLIF", "type": "HealthCareActivity"}]}

Example input:
Sentence: Decompression Surgery Alone Versus Decompression Plus Fusion in Symptomatic Lumbar Spinal Stenosis : A Swiss Prospective Multi - center Cohort Study with 3 Years of Follow - up Retrospective analysis of a prospective , multicenter cohort study .

Example answer:
{"entities": [{"text": "Decompression Surgery", "type": "HealthCareActivity"}, {"text": "Decompression", "type": "HealthCareActivity"}, {"text": "Fusion", "type": "HealthCareActivity"}, {"text": "Lumbar Spinal Stenosis", "type": "BiologicFunction"}, {"text": "Swiss", "type": "PopulationGroup"}, {"text": "Prospective Multi - center Cohort Study", "type": "ResearchActivity"}, {"text": "Follow - up", "type": "ResearchActivity"}, {"text": "Retrospective analysis", "type": "ResearchActivity"}, {"text": "prospective , multicenter cohort study", "type": "ResearchActivity"}]}

Example input:
Sentence: Among the patients with degenerative lumbar spinal stenosis and spondylolisthesis our study confirms that in the two groups , decompression alone and decompression plus fusion , patients distinctively benefited from surgical treatment .

Example answer:
{"entities": [{"text": "degenerative lumbar spinal stenosis", "type": "BiologicFunction"}, {"text": "spondylolisthesis", "type": "BiologicFunction"}, {"text": "decompression", "type": "HealthCareActivity"}, {"text": "fusion", "type": "HealthCareActivity"}, {"text": "surgical treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The BDUA + TLIF procedure appears to be associated with less postoperative low back discomfort and quicker recovery .

Example answer:
{"entities": [{"text": "BDUA", "type": "HealthCareActivity"}, {"text": "TLIF", "type": "HealthCareActivity"}, {"text": "back discomfort", "type": "Finding"}, {"text": "recovery", "type": "BiologicFunction"}]}

Example input:
Sentence: The mean improvements in low back pain VAS and ODI scores were significantly greater in the BDUA + TLIF group than in the laminectomy + PLIF group .

Example answer:
{"entities": [{"text": "low back pain", "type": "Finding"}, {"text": "VAS", "type": "HealthCareActivity"}, {"text": "ODI scores", "type": "Finding"}, {"text": "BDUA", "type": "HealthCareActivity"}, {"text": "TLIF", "type": "HealthCareActivity"}, {"text": "laminectomy", "type": "HealthCareActivity"}, {"text": "PLIF", "type": "HealthCareActivity"}]}

Example input:
Sentence: This study compared 43 patients undergoing BDUA + TLIF and 40 patients undergoing laminectomy + PLIF .

Example answer:
{"entities": [{"text": "BDUA", "type": "HealthCareActivity"}, {"text": "TLIF", "type": "HealthCareActivity"}, {"text": "laminectomy", "type": "HealthCareActivity"}, {"text": "PLIF", "type": "HealthCareActivity"}]}

Example input:
Sentence: When compared with the conventional laminectomy + PLIF procedure , the BDUA + TLIF procedure achieves similar and satisfactory effects of decompression and fusion for DLS with stenosis .

Example answer:
{"entities": [{"text": "laminectomy", "type": "HealthCareActivity"}, {"text": "PLIF", "type": "HealthCareActivity"}, {"text": "BDUA", "type": "HealthCareActivity"}, {"text": "TLIF", "type": "HealthCareActivity"}, {"text": "decompression", "type": "HealthCareActivity"}, {"text": "fusion", "type": "HealthCareActivity"}, {"text": "DLS", "type": "AnatomicalStructure"}, {"text": "stenosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Clinical and radiographic outcomes of bilateral decompression via a unilateral approach with transforaminal lumbar interbody fusion for degenerative lumbar spondylolisthesis with stenosis Laminectomy with posterior lumbar interbody fusion ( PLIF ) has been shown to achieve satisfactory clinical outcomes , but it leads to potential adverse consequences associated with extensive disruption of posterior bony and soft tissue structures .

Example answer:
{"entities": [{"text": "bilateral", "type": "SpatialConcept"}, {"text": "decompression", "type": "HealthCareActivity"}, {"text": "unilateral", "type": "SpatialConcept"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "transforaminal lumbar interbody fusion", "type": "HealthCareActivity"}, {"text": "degenerative", "type": "BiologicFunction"}, {"text": "lumbar spondylolisthesis", "type": "AnatomicalStructure"}, {"text": "stenosis", "type": "BiologicFunction"}, {"text": "Laminectomy", "type": "HealthCareActivity"}, {"text": "posterior lumbar interbody fusion", "type": "HealthCareActivity"}, {"text": "PLIF", "type": "HealthCareActivity"}, {"text": "adverse consequences", "type": "BiologicFunction"}, {"text": "posterior", "type": "SpatialConcept"}, {"text": "soft tissue", "type": "AnatomicalStructure"}, {"text": "structures", "type": "SpatialConcept"}]}

Input:
Sentence: This study aimed to compare the clinical and radiographic outcomes of bilateral decompression via a unilateral approach ( BDUA ) with transforaminal lumbar interbody fusion ( TLIF ) and laminectomy with PLIF in the treatment of degenerative lumbar spondylolisthesis ( DLS ) with stenosis .

## Item MedMentions:test:4516
Example input:
Sentence:  of the samples contained Citrinin ( < 1 μg / kg ) .

Example answer:
{"entities": [{"text": "Citrinin", "type": "Chemical"}]}

Example input:
Sentence: For the purpose of identification and quantification of citrinin , high performance liquid chromatograph ( HPLC ) with fluorescence was used ( Calibration curve k > 0 . 999 ; Intra assay CV = 2 .

Example answer:
{"entities": [{"text": "citrinin", "type": "Chemical"}, {"text": "high performance liquid chromatograph ( HPLC ) with fluorescence", "type": "HealthCareActivity"}, {"text": "used", "type": "Finding"}]}

Example input:
Sentence: Citrinin is generally formed after harvest and occurs mainly in stored grains , it also occurs in other plant products .

Example answer:
{"entities": [{"text": "Citrinin", "type": "Chemical"}, {"text": "stored grains", "type": "Food"}]}

Example input:
Sentence: From the area of Osijek - Baranja and Vukovar - Srijem County , 15 samples from each County were analyzed .

Example answer:
{"entities": [{"text": "area", "type": "SpatialConcept"}, {"text": "Osijek - Baranja", "type": "SpatialConcept"}, {"text": "Vukovar - Srijem County", "type": "SpatialConcept"}, {"text": "County", "type": "SpatialConcept"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: From the area of Međimurje County , 10 samples of corn and 10 samples of wheat were analyzed .

Example answer:
{"entities": [{"text": "area", "type": "SpatialConcept"}, {"text": "Međimurje County", "type": "SpatialConcept"}, {"text": "corn", "type": "Food"}, {"text": "wheat", "type": "Food"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: It must be stated that grains and grain - based products are the basis of everyday diet of all age groups , especially small children , where higher intake of citrinin can occur .

Example answer:
{"entities": [{"text": "grains", "type": "Food"}, {"text": "grain - based products", "type": "Food"}, {"text": "diet", "type": "Food"}, {"text": "citrinin", "type": "Chemical"}]}

Example input:
Sentence: PRESENCE OF CITRININ IN GRAINS AND ITS POSSIBLE HEALTH EFFECTS Citrinin is a mycotoxin produced by several species of the genera Aspergillus , Penicillium and Monascus and it occurs mainly in stored grain .

Example answer:
{"entities": [{"text": "PRESENCE OF", "type": "Finding"}, {"text": "CITRININ", "type": "Chemical"}, {"text": "GRAINS", "type": "Food"}, {"text": "POSSIBLE", "type": "Finding"}, {"text": "Citrinin", "type": "Chemical"}, {"text": "mycotoxin", "type": "Chemical"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "genera Aspergillus", "type": "Eukaryote"}, {"text": "Penicillium", "type": "Eukaryote"}, {"text": "Monascus", "type": "Eukaryote"}, {"text": "stored grain", "type": "Food"}]}

Example input:
Sentence: At the European Union level , systematic monitoring of Citrinin in grains began with the aim of determining its highest permissible amount in food .

Example answer:
{"entities": [{"text": "European Union", "type": "Organization"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "Citrinin", "type": "Chemical"}, {"text": "grains", "type": "Food"}, {"text": "food", "type": "Food"}]}

Example input:
Sentence: The main goal of this study was to determine the presence of Citrinin in grains sampled in the area of Međimurje , Osijek - Baranja , Vukovar - Srijem and Brod - Posavina County .

Example answer:
{"entities": [{"text": "main goal", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "presence of", "type": "Finding"}, {"text": "Citrinin", "type": "Chemical"}, {"text": "grains", "type": "Food"}, {"text": "area", "type": "SpatialConcept"}, {"text": "Međimurje", "type": "SpatialConcept"}, {"text": "Osijek - Baranja", "type": "SpatialConcept"}, {"text": "Vukovar - Srijem", "type": "SpatialConcept"}, {"text": "Brod - Posavina County", "type": "SpatialConcept"}]}

Example input:
Sentence: From 5 analyzed samples from Brod - Posavina County , one of the samples contained citrinin in the amount of 23 .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "Brod - Posavina County", "type": "SpatialConcept"}, {"text": "citrinin", "type": "Chemical"}]}

Input:
Sentence: Consequently , we emphasize the need for systematic analysis of larger amount of samples , from both large grains and small grains , especially in the area of Brod - Posavina County , in order to obtain more realistic notion of citrinin contamination of grains and to asses the health risk in humans .

## Item MedMentions:test:4700
Example input:
Sentence: SH - SY5Y neuroblastoma cell line was used to study the molecular mechanism upon APN and insulin treatment .

Example answer:
{"entities": [{"text": "SH - SY5Y neuroblastoma cell line", "type": "AnatomicalStructure"}, {"text": "study", "type": "ResearchActivity"}, {"text": "molecular mechanism", "type": "BiologicFunction"}, {"text": "APN", "type": "Chemical"}]}

Example input:
Sentence: Combining comprehensive sgRNA design and an efficient reporter assay to nominate efficient and selective sgRNAs , we establish a pipeline to dissect roles of cancer mutations with potential applicability to personalized medicine and future therapeutic use .

Example answer:
{"entities": [{"text": "sgRNA", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "sgRNAs", "type": "Chemical"}, {"text": "cancer mutations", "type": "BiologicFunction"}, {"text": "personalized medicine", "type": "HealthCareActivity"}]}

Example input:
Sentence: HepG2 cells were transfected with plasmid vectors overexpressing Hint1 or small interfering RNA ( siRNA ) targeting Hint1 , girdin , Hint1 plus girdin , or the scrambled RNA .

Example answer:
{"entities": [{"text": "HepG2 cells", "type": "AnatomicalStructure"}, {"text": "transfected", "type": "ResearchActivity"}, {"text": "plasmid vectors", "type": "Chemical"}, {"text": "overexpressing", "type": "BiologicFunction"}, {"text": "Hint1", "type": "Chemical"}, {"text": "small interfering RNA", "type": "Chemical"}, {"text": "siRNA", "type": "Chemical"}, {"text": "targeting", "type": "BiologicFunction"}, {"text": "girdin", "type": "Chemical"}, {"text": "RNA", "type": "Chemical"}]}

Example input:
Sentence: Through this mechanism , scCRISPR enables gene editing within 2 hr once sgRNA oligos are available , with high efficiency equivalent to conventional sgRNA targeting : > 90 % gene knockout in both mouse and human embryonic stem cells and cancer cell lines .

Example answer:
{"entities": [{"text": "scCRISPR", "type": "AnatomicalStructure"}, {"text": "gene editing", "type": "ResearchActivity"}, {"text": "sgRNA", "type": "Chemical"}, {"text": "oligos", "type": "Chemical"}, {"text": "gene", "type": "AnatomicalStructure"}, {"text": "knockout", "type": "BiologicFunction"}, {"text": "mouse", "type": "AnatomicalStructure"}, {"text": "human embryonic stem cells", "type": "AnatomicalStructure"}, {"text": "cancer cell lines", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Using a combination of short hairpin RNA ( shRNA ) lentivirus -mediated knockdown and pharmacologic isoform - specific inhibition we investigated the role of the PI3 K p110γ ( PI3Kγ ) subunit in regulating MM proliferation and bone marrow microenvironment - induced MM interactions .

Example answer:
{"entities": [{"text": "short hairpin RNA", "type": "Chemical"}, {"text": "( shRNA )", "type": "Chemical"}, {"text": "lentivirus", "type": "Virus"}, {"text": "knockdown", "type": "ResearchActivity"}, {"text": "pharmacologic isoform - specific", "type": "Chemical"}, {"text": "PI3 K p110γ", "type": "Chemical"}, {"text": "( PI3Kγ )", "type": "Chemical"}, {"text": "subunit", "type": "Chemical"}, {"text": "MM", "type": "BiologicFunction"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "bone marrow", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In this chapter , we describe the generation of stable clone Sf9 ( Spodoptera frugiperda ) cells expressing secreted , soluble , and native recombinant CHIKV E2 glycoprotein .

Example answer:
{"entities": [{"text": "clone", "type": "AnatomicalStructure"}, {"text": "Sf9", "type": "AnatomicalStructure"}, {"text": "Spodoptera frugiperda", "type": "Eukaryote"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "soluble", "type": "AnatomicalStructure"}, {"text": "CHIKV", "type": "Virus"}, {"text": "E2 glycoprotein", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , sgRNA targeting GPI anchor protein pathway genes induced loss of function mutations in human and mouse cell lines measured by FLAER labelling .

Example answer:
{"entities": [{"text": "sgRNA", "type": "Chemical"}, {"text": "GPI anchor protein pathway", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "loss of function mutations", "type": "Finding"}, {"text": "human", "type": "Eukaryote"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "cell lines", "type": "AnatomicalStructure"}]}

Example input:
Sentence: To illuminate such mechanisms further , we have recently performed CRISPR / Cas9 -mediated genome - wide knockout screening during reprogramming with a lentiviral gRNA library containing 90 , 000 gRNAs .

Example answer:
{"entities": [{"text": "CRISPR / Cas9", "type": "BiologicFunction"}, {"text": "genome - wide knockout screening", "type": "ResearchActivity"}, {"text": "reprogramming", "type": "BiologicFunction"}, {"text": "gRNAs", "type": "Chemical"}]}

Example input:
Sentence: Lentiviral vector containing small interfering RNA targeting Siglec - 1 ( Lv - shSiglec - 1 ) or control vector ( Lv - shNC ) were injected intravenously into 6 - week old Apoe ( - / - ) mice .

Example answer:
{"entities": [{"text": "Lentiviral vector", "type": "Chemical"}, {"text": "small interfering RNA", "type": "Chemical"}, {"text": "Siglec - 1", "type": "AnatomicalStructure"}, {"text": "Lv - shSiglec - 1", "type": "Chemical"}, {"text": "control vector", "type": "Chemical"}, {"text": "Lv - shNC", "type": "Chemical"}, {"text": "intravenously", "type": "SpatialConcept"}, {"text": "Apoe ( - / - )", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: shRNA lentiviral -mediated targeting of either PI3Kδ or PI3Kγ alone , or both in combination , increased survival of NSG mice xeno - transplanted with MM cells .

Example answer:
{"entities": [{"text": "shRNA", "type": "Chemical"}, {"text": "lentiviral", "type": "Virus"}, {"text": "PI3Kδ", "type": "Chemical"}, {"text": "PI3Kγ", "type": "Chemical"}, {"text": "NSG mice", "type": "Eukaryote"}, {"text": "xeno - transplanted", "type": "Chemical"}, {"text": "MM", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Input:
Sentence: For flexibility in generating stable cell lines the sgRNAs have been cloned in a lentivirus backbone containing PiggyBac transposase recognition elements together with fluorescent and drug selection markers .

## Item MedMentions:test:4409
Example input:
Sentence: Forty - two consecutive patients undergoing CRT had serial clinical and echocardiographic evaluations performed in addition to a post - procedural cardiac -gated CT with blinded measurement of direct and circumferential ( via the myocardium ) ILD measures .

Example answer:
{"entities": [{"text": "CRT", "type": "HealthCareActivity"}, {"text": "clinical", "type": "HealthCareActivity"}, {"text": "echocardiographic", "type": "HealthCareActivity"}, {"text": "evaluations", "type": "HealthCareActivity"}, {"text": "cardiac", "type": "SpatialConcept"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "blinded", "type": "ResearchActivity"}, {"text": "circumferential", "type": "SpatialConcept"}, {"text": "myocardium", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Preclinical fibrinolysis in patients with ST - segment elevation myocardial infarction in a rural region In the current guidelines for the treatment of patients with ST - segment elevation myocardial infarction ( STEMI ) , the European Society of Cardiology ( ESC ) recommends preclinical fibrinolysis as a reperfusion therapy if , due to long transportation times , no cardiac catheterisation is available within 90 - 120 min .

Example answer:
{"entities": [{"text": "fibrinolysis", "type": "BiologicFunction"}, {"text": "ST - segment elevation myocardial infarction", "type": "BiologicFunction"}, {"text": "current guidelines", "type": "IntellectualProduct"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "STEMI", "type": "BiologicFunction"}, {"text": "reperfusion therapy", "type": "HealthCareActivity"}, {"text": "cardiac catheterisation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients hospitalized with advanced HF symptoms and reduced left ventricular ejection function ( LVEF ) were enrolled and prescribed a WCD prior to discharge for a total of 3 months .

Example answer:
{"entities": [{"text": "HF", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "left ventricular ejection function", "type": "ClinicalAttribute"}, {"text": "LVEF", "type": "ClinicalAttribute"}, {"text": "discharge", "type": "HealthCareActivity"}]}

Example input:
Sentence: Study of the wearable cardioverter defibrillator in advanced heart - failure patients ( SWIFT ) The wearable cardioverter defibrillator ( WCD ) may allow stabilization until reassessment for an implantable cardioverter defibrillator ( ICD ) among high - risk HF patients .

Example answer:
{"entities": [{"text": "Study", "type": "ResearchActivity"}, {"text": "advanced heart - failure", "type": "BiologicFunction"}, {"text": "implantable cardioverter defibrillator", "type": "MedicalDevice"}, {"text": "ICD", "type": "MedicalDevice"}, {"text": "high - risk HF", "type": "BiologicFunction"}]}

Example input:
Sentence: WCD interrogations showed a total of 8 arrhythmic events in 5 patients , including 3 non - sustained or self - terminating ventricular tachycardia ( VT ) events , and one polymorphic VT successfully terminated by the WCD .

Example answer:
{"entities": [{"text": "self - terminating ventricular tachycardia ( VT ) events", "type": "Finding"}, {"text": "polymorphic VT", "type": "BiologicFunction"}]}

Example input:
Sentence: Conversely , S - ICD shocks were less cardiotoxic than T - ICD shocks .

Example answer:
{"entities": [{"text": "shocks", "type": "Finding"}, {"text": "cardiotoxic", "type": "InjuryOrPoisoning"}, {"text": "T - ICD", "type": "MedicalDevice"}]}

Example input:
Sentence: For each VF episode , up to two shocks could be delivered by the T - ICD or the S - ICD to terminate the arrhythmia .

Example answer:
{"entities": [{"text": "VF", "type": "BiologicFunction"}, {"text": "shocks", "type": "Finding"}, {"text": "T - ICD", "type": "MedicalDevice"}, {"text": "arrhythmia", "type": "Finding"}]}

Example input:
Sentence: During the 36 - month follow - up , 1 appropriate ICD shock ( 0 . 97 % event per year ) , 1 self - terminating ventricular fibrillation , and 1 inappropriate ICD shock occurred under placebo therapy .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "ICD", "type": "MedicalDevice"}, {"text": "shock", "type": "BiologicFunction"}, {"text": "ventricular fibrillation", "type": "BiologicFunction"}, {"text": "placebo therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Time to therapy in S - ICD was twice as long as for T - ICD , but didn ' t induce relevant brain injury .

Example answer:
{"entities": [{"text": "therapy", "type": "HealthCareActivity"}, {"text": "T - ICD", "type": "MedicalDevice"}, {"text": "brain injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Study carried out in a preclinical porcine model Totally subcutaneous implantable cardioverter defibrillator ( S - ICD ) delivers higher shock energy and can have longer time to therapy compared to transvenous implantable cardioverter defibrillator ( T - ICD ) .

Example answer:
{"entities": [{"text": "Study", "type": "ResearchActivity"}, {"text": "higher shock energy", "type": "Finding"}, {"text": "therapy", "type": "HealthCareActivity"}, {"text": "transvenous implantable cardioverter defibrillator", "type": "MedicalDevice"}, {"text": "T - ICD", "type": "MedicalDevice"}]}

Input:
Sentence: Aim of the study was to compare time to therapy and to investigate cardiac , cerebral and systemic injuries of S - ICD and T - ICD shocks delivered after ventricular fibrillation ( VF ) induction .

## Item MedMentions:test:4449
Example input:
Sentence: The LIF genotype frequencies amongst the 73 controls were C / C = 45 . 20 % , C / T = 50 . 70 % and T / T = 4 .

Example answer:
{"entities": [{"text": "LIF", "type": "Chemical"}, {"text": "C / C", "type": "SpatialConcept"}, {"text": "C / T", "type": "SpatialConcept"}, {"text": "T / T", "type": "SpatialConcept"}]}

Example input:
Sentence: Tamoxifen injection of Gcg - CreER ( T2 ) ; Rosa26 - LSL - YFP mice induced high recombination efficiency of the Rosa26 - LSL - YFP locus in perinatal and adult α - cells ( 88 % and 95 % , respectively ) , as well as in first - wave fetal α - cells ( 36 % ) and adult enteroendocrine L - cells ( 33 % ) .

Example answer:
{"entities": [{"text": "Tamoxifen", "type": "Chemical"}, {"text": "injection", "type": "HealthCareActivity"}, {"text": "Gcg - CreER ( T2 )", "type": "Eukaryote"}, {"text": "Rosa26 - LSL - YFP mice", "type": "Eukaryote"}, {"text": "recombination", "type": "BiologicFunction"}, {"text": "Rosa26 - LSL - YFP locus", "type": "AnatomicalStructure"}, {"text": "α - cells", "type": "AnatomicalStructure"}, {"text": "enteroendocrine L - cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The LIF genotype frequencies amongst the 70 cases were C / C = 40 % , C / T = 52 . 8 % and T / T = 7 . 2 % ; the C and T allele frequencies were 66 % and 34 % , respectively .

Example answer:
{"entities": [{"text": "LIF", "type": "Chemical"}, {"text": "C / C", "type": "SpatialConcept"}, {"text": "C / T", "type": "SpatialConcept"}, {"text": "T / T", "type": "SpatialConcept"}, {"text": "allele", "type": "AnatomicalStructure"}]}

Example input:
Sentence: LIF is a secreted glycoprotein with a variety of biological functions including stimulation of cell proliferation , differentiation and survival that are all essential for blastocyete development and implantation .

Example answer:
{"entities": [{"text": "LIF", "type": "Chemical"}, {"text": "glycoprotein", "type": "Chemical"}, {"text": "biological functions", "type": "BiologicFunction"}, {"text": "cell proliferation", "type": "BiologicFunction"}, {"text": "differentiation", "type": "BiologicFunction"}, {"text": "survival", "type": "BiologicFunction"}, {"text": "blastocyete", "type": "AnatomicalStructure"}, {"text": "implantation", "type": "BiologicFunction"}]}

Example input:
Sentence: The coexistence of CAD risk factors with LDLR A ( + ) A ( + ) genotype , ApoB X ( + ) allele and ApoE E4 allele may increase the risk of the development of PCAD in Egyptian patients .

Example answer:
{"entities": [{"text": "CAD", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "LDLR A ( + ) A ( + )", "type": "AnatomicalStructure"}, {"text": "ApoB X ( + )", "type": "AnatomicalStructure"}, {"text": "allele", "type": "AnatomicalStructure"}, {"text": "ApoE E4", "type": "AnatomicalStructure"}, {"text": "PCAD", "type": "BiologicFunction"}, {"text": "Egyptian", "type": "PopulationGroup"}]}

Example input:
Sentence: Promyelocytic leukemia zinc finger protein ( PLZF ) is a transcription factor that can be activated by low - temperature far - infrared ( FIR ) irradiation to exert beneficial effects on the vascular endothelium .

Example answer:
{"entities": [{"text": "Promyelocytic leukemia zinc finger protein", "type": "Chemical"}, {"text": "PLZF", "type": "Chemical"}, {"text": "transcription factor", "type": "Chemical"}, {"text": "activated", "type": "BiologicFunction"}, {"text": "exert beneficial effects", "type": "BiologicFunction"}, {"text": "vascular endothelium", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The LIF receptor activates several signaling pathways in diverse cell types , including Jak / STAT , MAPK and PI3 - kinase pathways in the endometrium of fertile woman .

Example answer:
{"entities": [{"text": "LIF receptor", "type": "Chemical"}, {"text": "signaling pathways", "type": "BiologicFunction"}, {"text": "diverse cell types", "type": "IntellectualProduct"}, {"text": "MAPK", "type": "Chemical"}, {"text": "PI3 - kinase", "type": "Chemical"}, {"text": "pathways", "type": "BiologicFunction"}, {"text": "endometrium", "type": "AnatomicalStructure"}, {"text": "fertile", "type": "BiologicFunction"}, {"text": "woman", "type": "PopulationGroup"}]}

Example input:
Sentence: In conclusion , the results of this study indicate that SNP 3951C / T of LIF may not be associated with IVF - ET outcome in this population .

Example answer:
{"entities": [{"text": "SNP 3951C / T", "type": "SpatialConcept"}, {"text": "LIF", "type": "Chemical"}, {"text": "IVF", "type": "HealthCareActivity"}, {"text": "ET", "type": "HealthCareActivity"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: It has been suggested that the initial lower expression of LIF in proliferative phase may be one of the causes for multiple failure of implantation .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "LIF", "type": "Chemical"}, {"text": "proliferative", "type": "BiologicFunction"}, {"text": "implantation", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of this study was to evaluate the association between maternal genotype of SNP 3951C / T LIF and in vitro fertilization and embryo transfer ( IVF - ET ) outcome in infertile women .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "maternal", "type": "Finding"}, {"text": "SNP 3951C / T", "type": "SpatialConcept"}, {"text": "LIF", "type": "Chemical"}, {"text": "in vitro fertilization", "type": "HealthCareActivity"}, {"text": "embryo transfer", "type": "HealthCareActivity"}, {"text": "IVF", "type": "HealthCareActivity"}, {"text": "ET", "type": "HealthCareActivity"}, {"text": "infertile", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}]}

Input:
Sentence: Association of leukemia inhibitory factor gene polymorphism and in vitro fertilization outcome in a population in northern Iran Several studies have been demonstrated that endometrial leukemia inhibitory factor ( LIF ) is important in embryo implantation .

## Item MedMentions:test:4618
Example input:
Sentence: Our results are broadly consistent with findings in rodents that acute alcohol and stress exposure suppress neurogenesis in the adult hippocampus , which in turn impairs performance in high interference memory tasks , while adolescent onset binge drinking causes more extensive brain damage and cognitive deficits .

Example answer:
{"entities": [{"text": "rodents", "type": "Eukaryote"}, {"text": "stress", "type": "BiologicFunction"}, {"text": "neurogenesis", "type": "BiologicFunction"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "memory", "type": "BiologicFunction"}, {"text": "brain damage", "type": "InjuryOrPoisoning"}, {"text": "cognitive deficits", "type": "BiologicFunction"}]}

Example input:
Sentence: High - end energy drink consumers reported more risk - taking behaviors ( increased drug and alcohol use and less frequent seat belt use ) , sleep disturbances ( later bedtimes , harder time falling asleep , and more all - nighters ) , and higher frequency of mental illness diagnoses than those who consumed fewer energy drinks .

Example answer:
{"entities": [{"text": "energy drink", "type": "Food"}, {"text": "consumers", "type": "PopulationGroup"}, {"text": "seat belt use", "type": "Finding"}, {"text": "sleep disturbances", "type": "Finding"}, {"text": "harder time falling asleep", "type": "BiologicFunction"}, {"text": "mental illness", "type": "BiologicFunction"}, {"text": "diagnoses", "type": "Finding"}, {"text": "energy drinks", "type": "Food"}]}

Example input:
Sentence: Temporal Stability of Heavy Drinking Days and Drinking Reductions Among Heavy Drinkers in the COMBINE Study Recently , the Food and Drug Administration ( FDA ) proposed to expand the options for primary end points in the development of medications for alcohol use disorder to include either abstinence from alcohol or a nonabstinent outcome : no heavy drinking days ( with a heavy drinking day defined as more than 3 drinks per day for women and more than 4 drinks per day for men [ > 3 / > 4 cutoff ] ) .

Example answer:
{"entities": [{"text": "Heavy Drinking", "type": "Finding"}, {"text": "Reductions", "type": "HealthCareActivity"}, {"text": "COMBINE Study", "type": "ResearchActivity"}, {"text": "Food and Drug Administration", "type": "Organization"}, {"text": "FDA", "type": "Organization"}, {"text": "expand", "type": "SpatialConcept"}, {"text": "medications", "type": "HealthCareActivity"}, {"text": "alcohol", "type": "Food"}, {"text": "nonabstinent", "type": "Finding"}, {"text": "heavy drinking", "type": "Finding"}, {"text": "defined", "type": "IntellectualProduct"}, {"text": "drinks", "type": "Food"}, {"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: On the other hand , adolescent onset of binge drinking predicted poorer performance on broader range of memory tests , including a more systematic test of spatial recognition memory , and an associative learning task .

Example answer:
{"entities": [{"text": "memory", "type": "BiologicFunction"}, {"text": "tests", "type": "IntellectualProduct"}, {"text": "systematic test of spatial recognition memory", "type": "IntellectualProduct"}, {"text": "associative learning", "type": "BiologicFunction"}]}

Example input:
Sentence: Stress and binge drinking : A toxic combination for the teenage brain Young adult university students frequently binge on alcohol and have high stress levels .

Example answer:
{"entities": [{"text": "Stress", "type": "BiologicFunction"}, {"text": "toxic", "type": "InjuryOrPoisoning"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "stress levels", "type": "Finding"}]}

Example input:
Sentence: Prevalence and correlates of binge eating disorder related features in the community Binge eating disorder ( BED ) is associated with high levels of obesity and psychological suffering , but little is known about 1 ) the distribution of features of BED in the general population and 2 ) their consequences for weight development and psychological distress in young adulthood .

Example answer:
{"entities": [{"text": "binge eating disorder", "type": "BiologicFunction"}, {"text": "Binge eating disorder", "type": "BiologicFunction"}, {"text": "BED", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "general population", "type": "PopulationGroup"}]}

Example input:
Sentence: Mostly occurring among young people at weekends , binge drinking increases the risk of both acute ( e . g .

Example answer:
{"entities": [{"text": "people", "type": "PopulationGroup"}]}

Example input:
Sentence: Other major risk factors for binge drinking are frequently spending time with friends who drink , and the drinking norms observed in the wider social environment ( e . g .

Example answer:
{"entities": [{"text": "risk factors", "type": "Finding"}, {"text": "friends", "type": "PopulationGroup"}]}

Example input:
Sentence: Stress , anxiety , traumatic events and depression are also related to binge drinking .

Example answer:
{"entities": [{"text": "Stress", "type": "BiologicFunction"}, {"text": "anxiety", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}]}

Example input:
Sentence: This paper provides an overview of recently published evidence concerning the definition and measuremen t , prevalence rates , health impact , demographic and psychosocial correlates of , and interventions for , binge drinking .

Example answer:
{"entities": [{"text": "published evidence", "type": "IntellectualProduct"}, {"text": "definition", "type": "IntellectualProduct"}, {"text": "health impact", "type": "HealthCareActivity"}, {"text": "demographic", "type": "ResearchActivity"}, {"text": "interventions", "type": "HealthCareActivity"}]}

Input:
Sentence: Binge drinking : Health impact , prevalence , correlates and interventions Binge drinking ( also called heavy episodic drinking , risky single - occasion drinking etc . ) is a major public health problem .

## Item MedMentions:test:4615
Example input:
Sentence: Targeted next generation sequencing and Sanger sequencing identified a heterozygous T to C transition at position 695 ( c .

Example answer:
{"entities": [{"text": "Targeted next generation sequencing", "type": "ResearchActivity"}, {"text": "Sanger sequencing", "type": "ResearchActivity"}, {"text": "T to C transition at position 695", "type": "BiologicFunction"}, {"text": "c .", "type": "BiologicFunction"}]}

Example input:
Sentence: Functional conservation of the lncRNA NEAT1 in the ancestrally diverged marsupial lineage : Evidence for NEAT1 expression and associated paraspeckle assembly during late gestation in the opossum Monodelphis domestica Long non - coding RNAs ( lncRNAs ) are widely expressed and play various roles in cell homeostasis .

Example answer:
{"entities": [{"text": "lncRNA", "type": "Chemical"}, {"text": "NEAT1", "type": "AnatomicalStructure"}, {"text": "marsupial", "type": "Eukaryote"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "paraspeckle", "type": "AnatomicalStructure"}, {"text": "gestation", "type": "BiologicFunction"}, {"text": "opossum", "type": "Eukaryote"}, {"text": "Monodelphis domestica", "type": "Eukaryote"}, {"text": "Long non - coding RNAs", "type": "Chemical"}, {"text": "lncRNAs", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "cell homeostasis", "type": "BiologicFunction"}]}

Example input:
Sentence: Sequence - based genome analysis revealed that LA2007 carries a plasmid highly similar to Bacillus anthracis pXO1 , including the genes responsible for the production and regulation of anthrax toxin .

Example answer:
{"entities": [{"text": "Sequence - based genome analysis", "type": "HealthCareActivity"}, {"text": "LA2007", "type": "Bacterium"}, {"text": "carries", "type": "Finding"}, {"text": "plasmid", "type": "Chemical"}, {"text": "Bacillus anthracis pXO1", "type": "Bacterium"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "production", "type": "Chemical"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "anthrax toxin", "type": "Chemical"}]}

Example input:
Sentence: In this study , we performed a Bayesian phylogeographic analysis to reconstruct the spatio - temporal dispersion pattern of this clade using eligible CRF35 _ AD gag and pol sequences available in the Los Alamos HIV database ( 432 sequences available from Iran , 16 sequences available from Afghanistan , and a single CRF35 _ AD -like pol sequence available from USA ) .

Example answer:
{"entities": [{"text": "gag and pol sequences", "type": "SpatialConcept"}, {"text": "Los Alamos", "type": "SpatialConcept"}, {"text": "HIV database", "type": "IntellectualProduct"}, {"text": "sequences", "type": "SpatialConcept"}, {"text": "Iran", "type": "SpatialConcept"}, {"text": "Afghanistan", "type": "SpatialConcept"}, {"text": "pol sequence", "type": "SpatialConcept"}, {"text": "USA", "type": "SpatialConcept"}]}

Example input:
Sentence: Conservation patterns analysis revealed that 57 % of pig lncRNAs showed homology to humans and mice based on genome alignment .

Example answer:
{"entities": [{"text": "patterns analysis", "type": "HealthCareActivity"}, {"text": "pig", "type": "Eukaryote"}, {"text": "lncRNAs", "type": "Chemical"}, {"text": "humans", "type": "Eukaryote"}, {"text": "mice", "type": "Eukaryote"}, {"text": "genome alignment", "type": "ResearchActivity"}]}

Example input:
Sentence: latos individuals exhibited only 0 .

Example answer:
{"entities": [{"text": "latos", "type": "Eukaryote"}]}

Example input:
Sentence: Complete mitogenomes of 16 , 546bp nucleotides were obtained from two E . l .

Example answer:
{"entities": [{"text": "mitogenomes", "type": "AnatomicalStructure"}, {"text": "16 , 546bp nucleotides", "type": "Chemical"}, {"text": "E . l .", "type": "Eukaryote"}]}

Example input:
Sentence: l . latos and the moapae subspecies of C .

Example answer:
{"entities": [{"text": "l . latos", "type": "Eukaryote"}, {"text": "moapae", "type": "Eukaryote"}, {"text": "subspecies", "type": "IntellectualProduct"}, {"text": "C .", "type": "Eukaryote"}]}

Example input:
Sentence: Characterization and phylogenetic analysis of complete mitochondrial genomes for two desert cyprinodontoid fishes , Empetrichthys latos and Crenichthys baileyi The Pahrump poolfish ( Empetrichthys latos ) and White River springfish ( Crenichthys baileyi ) are small - bodied teleost fishes ( order Cyprinodontiformes ) endemic to the arid Great Basin and Mojave Desert regions of western North America .

Example answer:
{"entities": [{"text": "phylogenetic analysis", "type": "ResearchActivity"}, {"text": "mitochondrial genomes", "type": "AnatomicalStructure"}, {"text": "desert", "type": "SpatialConcept"}, {"text": "cyprinodontoid fishes", "type": "Eukaryote"}, {"text": "Empetrichthys latos", "type": "Eukaryote"}, {"text": "Crenichthys baileyi", "type": "Eukaryote"}, {"text": "Pahrump poolfish", "type": "Eukaryote"}, {"text": "White River springfish", "type": "Eukaryote"}, {"text": "teleost fishes", "type": "Eukaryote"}, {"text": "Cyprinodontiformes", "type": "Eukaryote"}, {"text": "Great Basin", "type": "SpatialConcept"}, {"text": "Mojave Desert", "type": "SpatialConcept"}, {"text": "western", "type": "SpatialConcept"}, {"text": "North America", "type": "SpatialConcept"}]}

Example input:
Sentence: latos and 842bp for C .

Example answer:
{"entities": [{"text": "latos", "type": "Eukaryote"}, {"text": "C .", "type": "Eukaryote"}]}

Input:
Sentence: latos individuals collected from introduced populations at Spring Mountain Ranch State Park and Shoshone Ponds Natural Area , Nevada , USA , while a single mitogenome of 16 , 537bp was sequenced for C .

## Item MedMentions:test:4327
Example input:
Sentence: The majority of resistant isolates were oxa23 -positive global clone GC2 ; fine - scale phylogenomic analysis revealed five distinct GC2 sublineages within the ICU that had evolved locally via independent chromosomal insertions of oxa23 transposons .

Example answer:
{"entities": [{"text": "resistant", "type": "BiologicFunction"}, {"text": "isolates", "type": "Chemical"}, {"text": "clone", "type": "AnatomicalStructure"}, {"text": "GC2", "type": "Bacterium"}, {"text": "phylogenomic analysis", "type": "ResearchActivity"}, {"text": "ICU", "type": "Organization"}, {"text": "chromosomal insertions", "type": "BiologicFunction"}, {"text": "transposons", "type": "Chemical"}]}

Example input:
Sentence: To provide further evidence , we used two glutathione peroxidase ( GPX ) - defective strains , the gpxi strain , the mercaptosuccinic acid ( MS , a GPX inhibitor ) - treated wide - type ( WT ) strain , and gpx overexpression strains for further research .

Example answer:
{"entities": [{"text": "glutathione peroxidase", "type": "Chemical"}, {"text": "GPX", "type": "Chemical"}, {"text": "defective strains", "type": "AnatomicalStructure"}, {"text": "gpxi strain", "type": "AnatomicalStructure"}, {"text": "mercaptosuccinic acid", "type": "Chemical"}, {"text": "MS", "type": "Chemical"}, {"text": "GPX inhibitor", "type": "Chemical"}, {"text": "wide - type ( WT ) strain", "type": "AnatomicalStructure"}, {"text": "gpx overexpression strains", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The main carcinogenic genotypes were HPV - 16 , HPV - 18 , HPV - 58 , HPV - 52 , and HPV - 31 . HPV - 16 and HPV - 18 combined caused 80 .

Example answer:
{"entities": [{"text": "carcinogenic", "type": "Chemical"}, {"text": "HPV - 16", "type": "Virus"}, {"text": "HPV - 18", "type": "Virus"}, {"text": "HPV - 58", "type": "Virus"}, {"text": "HPV - 52", "type": "Virus"}, {"text": "HPV - 31", "type": "Virus"}]}

Example input:
Sentence: In this study , we performed a Bayesian phylogeographic analysis to reconstruct the spatio - temporal dispersion pattern of this clade using eligible CRF35 _ AD gag and pol sequences available in the Los Alamos HIV database ( 432 sequences available from Iran , 16 sequences available from Afghanistan , and a single CRF35 _ AD -like pol sequence available from USA ) .

Example answer:
{"entities": [{"text": "gag and pol sequences", "type": "SpatialConcept"}, {"text": "Los Alamos", "type": "SpatialConcept"}, {"text": "HIV database", "type": "IntellectualProduct"}, {"text": "sequences", "type": "SpatialConcept"}, {"text": "Iran", "type": "SpatialConcept"}, {"text": "Afghanistan", "type": "SpatialConcept"}, {"text": "pol sequence", "type": "SpatialConcept"}, {"text": "USA", "type": "SpatialConcept"}]}

Example input:
Sentence: 9 % , 36 / 84 ) was the most common capsular serotype among HMKP isolates , followed by K1 ( 23 . 8 % , 20 / 84 ) .

Example answer:
{"entities": [{"text": "capsular", "type": "SpatialConcept"}, {"text": "serotype", "type": "IntellectualProduct"}, {"text": "HMKP", "type": "Bacterium"}, {"text": "isolates", "type": "Chemical"}, {"text": "K1", "type": "IntellectualProduct"}]}

Example input:
Sentence: The type strain is SYP - A7299 T ( = DSM 100491T = KCTC 39 592 T ) .

Example answer:
{"entities": [{"text": "SYP - A7299 T", "type": "Bacterium"}, {"text": "= DSM 100491T = KCTC 39 592 T", "type": "Bacterium"}]}

Example input:
Sentence: ( i . e . , B2 , B36 , B38 , B48 , and B51 ) with the wild - type parental clone Badila ( WT ) .

Example answer:
{"entities": [{"text": "B2", "type": "Eukaryote"}, {"text": "B36", "type": "Eukaryote"}, {"text": "B38", "type": "Eukaryote"}, {"text": "B48", "type": "Eukaryote"}, {"text": "B51", "type": "Eukaryote"}, {"text": "wild - type", "type": "AnatomicalStructure"}, {"text": "parental clone", "type": "AnatomicalStructure"}, {"text": "Badila", "type": "Eukaryote"}, {"text": "WT", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A total of 56 KPC - Kp isolates were recovered from clinical samples in a Chinese hospital , which were assigned to clonal lineages by multilocus sequence typing ( MLST ) .

Example answer:
{"entities": [{"text": "KPC - Kp", "type": "Bacterium"}, {"text": "isolates", "type": "Chemical"}, {"text": "Chinese hospital", "type": "Organization"}, {"text": "multilocus sequence typing", "type": "ResearchActivity"}, {"text": "MLST", "type": "ResearchActivity"}]}

Example input:
Sentence: The strain - types identified were AK3 ( ST - 5 SCCmecIV t045 ; n = 1 ) , USA500 ( ST8 SCCmecIV t064 ; n = 1 ) , WSPP ( ST30 SCCmecIV t019 ; n = 1 ) , Rhine Hesse ( ST5 SCCmecII t002 ; n = 2 ) , and EMRSA - 15 ( ST22 SCCmecIV t032 ; n = 3 ) .

Example answer:
{"entities": [{"text": "AK3 ( ST - 5 SCCmecIV", "type": "Bacterium"}, {"text": "USA500 ( ST8 SCCmecIV", "type": "Bacterium"}, {"text": "WSPP ( ST30 SCCmecIV", "type": "Bacterium"}, {"text": "Rhine Hesse ( ST5 SCCmecII", "type": "Bacterium"}, {"text": "EMRSA - 15 ( ST22 SCCmecIV", "type": "Bacterium"}]}

Example input:
Sentence: Capsule typing ( wzi sequencing and wzc polymerase chain reaction [ PCR ] ) and virulence genes were characterized by molecular approaches .

Example answer:
{"entities": [{"text": "Capsule", "type": "Chemical"}, {"text": "typing", "type": "HealthCareActivity"}, {"text": "wzi sequencing", "type": "HealthCareActivity"}, {"text": "wzc polymerase chain reaction", "type": "ResearchActivity"}, {"text": "PCR", "type": "ResearchActivity"}, {"text": "virulence", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "molecular approaches", "type": "HealthCareActivity"}]}

Input:
Sentence: Based on the wzi gene DNA sequences and wzc PCR , these 56 strains were classified as capsular type wzi47 - K47 ( n = 37 ) , wzi64 - K64 ( n = 8 ) , wzi8 - K8 ( n = 4 ) , wzi37 - K37 ( n = 4 ) , wzi53 - K53 ( n = 1 ) , wzi125 - K2 ( n = 1 ) , and wzi1 - K1 ( n = 1 ) .

## Item MedMentions:test:4759
Example input:
Sentence: Households ( n = 13 , 351 ) that participated in the Brazilian Household Budget Survey and the National Dietary Survey were classified as satisfied or dissatisfied with the food consumed in the home .

Example answer:
{"entities": [{"text": "Budget Survey", "type": "IntellectualProduct"}, {"text": "National Dietary Survey", "type": "IntellectualProduct"}, {"text": "classified", "type": "IntellectualProduct"}, {"text": "satisfied", "type": "IntellectualProduct"}, {"text": "dissatisfied", "type": "IntellectualProduct"}, {"text": "home", "type": "Organization"}]}

Example input:
Sentence: This is the first study that concurrently explores the contribution of genetics , population diversity and cultural aspects in taste perception and food consumption .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "population", "type": "PopulationGroup"}, {"text": "taste perception", "type": "BiologicFunction"}]}

Example input:
Sentence: Socio - cognitive and psychosocial factors were measured among users and non - users of dietary supplements in a longitudinal survey study , with measurements at baseline ( N = 1448 ) and at one - month follow - up ( N = 1161 ) .

Example answer:
{"entities": [{"text": "users", "type": "PopulationGroup"}, {"text": "non - users", "type": "PopulationGroup"}, {"text": "dietary supplements", "type": "Food"}, {"text": "study", "type": "ResearchActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Higher likelihood of low consumption of fruits and vegetables was verified among boys who were exposed to sedentary behavior ( OR = 1 . 63 ; 95 % CI = 1 . 18 - 2 . 24 ) , who consumed soft drinks ( OR = 3 .

Example answer:
{"entities": [{"text": "consumption of fruits and vegetables", "type": "BiologicFunction"}, {"text": "soft drinks", "type": "Food"}]}

Example input:
Sentence: We confirmed previous genetic associations , in particular with stevioside perception , and noted significant differences in food consumption : in particular , broccoli , mustard and beer consumption scores were significantly higher ( Adjusted P = 0 .

Example answer:
{"entities": [{"text": "stevioside", "type": "Chemical"}, {"text": "perception", "type": "BiologicFunction"}, {"text": "broccoli", "type": "Food"}, {"text": "mustard", "type": "Food"}]}

Example input:
Sentence: Satisfied families ( n = 4429 ) reported statistically higher intake ( in grams / 1000 kcal ) of vegetables ( 47 . 3 vs 33 . 7 ) , fruits ( 46 . 9 vs 21 . 4 ) , sugar - sweetened beverages ( 118 vs 71 . 7 ) , milk and dairy ( 57 . 9 vs 34 . 6 ) , and ultra - processed products ( 18 . 6 vs 9 . 8 ) ; and lower intake of rice ( 86 . 2 vs 112 ) , beans ( 91 . 7 vs 136 ) , and meat ( 76 . 5 vs 84 .

Example answer:
{"entities": [{"text": "Satisfied", "type": "IntellectualProduct"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "vegetables", "type": "Food"}, {"text": "fruits", "type": "Food"}, {"text": "sugar - sweetened beverages", "type": "Food"}, {"text": "milk", "type": "Food"}, {"text": "dairy", "type": "Food"}, {"text": "ultra - processed products", "type": "Food"}, {"text": "rice", "type": "Food"}, {"text": "beans", "type": "Food"}, {"text": "meat", "type": "Food"}]}

Example input:
Sentence: Satisfied families in the highest income group also consumed more fruits and less beans than dissatisfied families in the same income group .

Example answer:
{"entities": [{"text": "Satisfied", "type": "IntellectualProduct"}, {"text": "highest income group", "type": "PopulationGroup"}, {"text": "fruits", "type": "Food"}, {"text": "beans", "type": "Food"}, {"text": "dissatisfied", "type": "IntellectualProduct"}, {"text": "same income group", "type": "PopulationGroup"}]}

Example input:
Sentence: Also among satisfied families , those in the highest per capita income group presented higher intake of fruits and lower intake of beans than those in the lowest income group .

Example answer:
{"entities": [{"text": "satisfied", "type": "IntellectualProduct"}, {"text": "fruits", "type": "Food"}, {"text": "beans", "type": "Food"}, {"text": "lowest income group", "type": "PopulationGroup"}]}

Example input:
Sentence: We compared the family dietary intake of the two groups considering their socio - demographic characteristics .

Example answer:
{"entities": [{"text": "dietary intake", "type": "BiologicFunction"}]}

Example input:
Sentence: Among satisfied families , in the youngest group we found lower consumption of fruits and higher intake of sugar - sweetened beverages and ultra - processed products when compared to the oldest group .

Example answer:
{"entities": [{"text": "satisfied", "type": "IntellectualProduct"}, {"text": "fruits", "type": "Food"}, {"text": "sugar - sweetened beverages", "type": "Food"}, {"text": "ultra - processed products", "type": "Food"}]}

Input:
Sentence: Socio - demographic characteristics may influence perception of satisfaction with food consumed and potentially influence the success of public health efforts to offer nutrition guidance for families satisfied with diets that may or may not be comprised of healthy food and beverages .

## Item MedMentions:test:4540
Example input:
Sentence: Our data support the pivotal role of the most characterized fibrolytic bacteria ( Prevotella , Ruminocccus and Fibrobacter ) , and highlight a substantial , although most probably underestimated , contribution of fungi and ciliate protozoa to polysaccharide degradation .

Example answer:
{"entities": [{"text": "fibrolytic bacteria", "type": "Bacterium"}, {"text": "Prevotella", "type": "Bacterium"}, {"text": "Ruminocccus", "type": "Bacterium"}, {"text": "Fibrobacter", "type": "Bacterium"}, {"text": "fungi", "type": "Eukaryote"}, {"text": "ciliate protozoa", "type": "Eukaryote"}, {"text": "polysaccharide", "type": "Chemical"}]}

Example input:
Sentence: The results of 16S rDNA sequencing also revealed that Enterococcus spp . and Pseudomonas aeruginosa are major competing bacteria in the enrichment conditions .

Example answer:
{"entities": [{"text": "16S rDNA", "type": "Chemical"}, {"text": "sequencing", "type": "HealthCareActivity"}, {"text": "Enterococcus spp .", "type": "Bacterium"}, {"text": "Pseudomonas aeruginosa", "type": "Bacterium"}, {"text": "bacteria", "type": "Bacterium"}]}

Example input:
Sentence: The effective combinations were able to withstand up to six multiple microbial challenges without product degradation .

Example answer:
{"entities": [{"text": "able", "type": "Finding"}, {"text": "withstand", "type": "Finding"}, {"text": "challenges", "type": "HealthCareActivity"}]}

Example input:
Sentence: Antibacterial and antifungal activities of the compound were tested against different bacterial and fungal strains , employing the agar well diffusion methods .

Example answer:
{"entities": [{"text": "Antibacterial", "type": "Finding"}, {"text": "antifungal activities", "type": "Finding"}, {"text": "compound", "type": "Chemical"}, {"text": "bacterial", "type": "Bacterium"}, {"text": "fungal strains", "type": "Eukaryote"}, {"text": "agar well diffusion methods", "type": "HealthCareActivity"}]}

Example input:
Sentence: Compounds 2 and 4 - 7 showed mild antibacterial activity against human pathogen Staphylococcus aureus and fish pathogens Streptococcus iniae and Vibrio ichthyoenteri , and compounds 4 and 7 weakly suppressed NO production .

Example answer:
{"entities": [{"text": "Compounds 2 and 4 - 7", "type": "Chemical"}, {"text": "antibacterial activity", "type": "Finding"}, {"text": "human", "type": "Eukaryote"}, {"text": "Staphylococcus aureus", "type": "Bacterium"}, {"text": "fish", "type": "Eukaryote"}, {"text": "Streptococcus iniae", "type": "Bacterium"}, {"text": "Vibrio ichthyoenteri", "type": "Bacterium"}, {"text": "compounds 4 and 7", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}]}

Example input:
Sentence: Prokaryotic pathogens which utilize this mechanism for their infectivity include Streptococcus pneumoniae , Haemophilus influenzae , Neisseria meningitidis and Escherichia coli .

Example answer:
{"entities": [{"text": "pathogens", "type": "BiologicFunction"}, {"text": "infectivity", "type": "BiologicFunction"}, {"text": "Streptococcus pneumoniae", "type": "Bacterium"}, {"text": "Haemophilus influenzae", "type": "Bacterium"}, {"text": "Neisseria meningitidis", "type": "Bacterium"}, {"text": "Escherichia coli", "type": "Bacterium"}]}

Example input:
Sentence: Almost all the compounds showed good activities against both Gram - positive and Gram - negative bacterial strains .

Example answer:
{"entities": [{"text": "compounds", "type": "Chemical"}, {"text": "Gram - positive", "type": "Bacterium"}, {"text": "Gram - negative bacterial strains", "type": "Bacterium"}]}

Example input:
Sentence: In total , 1028 clinical strains ( 291 Escherichia coli , 272 Klebsiella pneumoniae , 176 Staphylococcus aureus and 289 Staphylococcus epidermidis ) were included in this study .

Example answer:
{"entities": [{"text": "Escherichia coli", "type": "Bacterium"}, {"text": "Klebsiella pneumoniae", "type": "Bacterium"}, {"text": "Staphylococcus aureus", "type": "Bacterium"}, {"text": "Staphylococcus epidermidis", "type": "Bacterium"}]}

Example input:
Sentence: 47 microorganisms were screened including bacteria , fungi , and yeasts .

Example answer:
{"entities": [{"text": "bacteria", "type": "Bacterium"}, {"text": "fungi", "type": "Eukaryote"}, {"text": "yeasts", "type": "Eukaryote"}]}

Example input:
Sentence: coli , Pseudomonas aeruginosa , Proteus mirabilis , Streptococcus agalactiae , Staphylococcus saprophyticus and Enterococcus faecalis were undertaken using viable bacterial count and optical density measurements over a 48h culture period .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "Pseudomonas aeruginosa", "type": "Bacterium"}, {"text": "Proteus mirabilis", "type": "Bacterium"}, {"text": "Streptococcus agalactiae", "type": "Bacterium"}, {"text": "Staphylococcus saprophyticus", "type": "Bacterium"}, {"text": "Enterococcus faecalis", "type": "Bacterium"}, {"text": "bacterial count", "type": "HealthCareActivity"}, {"text": "optical density measurements", "type": "HealthCareActivity"}, {"text": "culture", "type": "HealthCareActivity"}]}

Input:
Sentence: By using 17 bacteria and 1 fungi , which include Bacillus , Candida , Enterobacter , Enterococcus , Escherichia , Klebsiella , Listeria , Pseudomonas , Salmonella and Staphylococcus genera , the activity of A .

## Item MedMentions:test:4736
Example input:
Sentence: Conclusions Percutaneous access in redo groins with scar tissue and / or synthetic vascular graft using ultrasound - guided punction , preclosing with ProGlide ® system and predilation with percutaneous transluminal angioplasty balloon to introduce large size sheath as used for endovascular aortic repair showed to be feasible , safe and with few local complications .

Example answer:
{"entities": [{"text": "Percutaneous access", "type": "SpatialConcept"}, {"text": "redo groins", "type": "SpatialConcept"}, {"text": "scar tissue", "type": "Finding"}, {"text": "ultrasound - guided punction", "type": "MedicalDevice"}, {"text": "preclosing", "type": "HealthCareActivity"}, {"text": "ProGlide ® system", "type": "MedicalDevice"}, {"text": "predilation", "type": "HealthCareActivity"}, {"text": "percutaneous transluminal angioplasty balloon", "type": "HealthCareActivity"}, {"text": "large size", "type": "Finding"}, {"text": "sheath", "type": "MedicalDevice"}, {"text": "endovascular aortic repair", "type": "HealthCareActivity"}, {"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: Therefore , a randomized dosage adjustment trial should elucidate whether a tailored ASA treatment after CABG surgery represents a useful concept .

Example answer:
{"entities": [{"text": "randomized dosage adjustment trial", "type": "ResearchActivity"}, {"text": "ASA", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "CABG surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Geographical Difference of the Interaction of Sex With Treatment Strategy in Patients With Multivessel Disease and Left Main Disease : A Meta - Analysis From SYNTAX ( Synergy Between PCI With Taxus and Cardiac Surgery ) , PRECOMBAT ( Bypass Surgery Versus Angioplasty Using Sirolimus - Eluting Stent in Patients With Left Main Coronary Artery Disease ) , and BEST ( Bypass Surgery and Everolimus - Eluting Stent Implantation in the Treatment of Patients With Multivessel Coronary Artery Disease ) Randomized Controlled Trials The impact of sex on clinical outcomes of percutaneous coronary intervention and coronary artery bypass graft for patients with multivessel coronary disease and unprotected left main disease could be dissimilar between Western and Asian populations .

Example answer:
{"entities": [{"text": "Sex", "type": "BiologicFunction"}, {"text": "Treatment Strategy", "type": "HealthCareActivity"}, {"text": "Multivessel Disease", "type": "BiologicFunction"}, {"text": "Left Main Disease", "type": "BiologicFunction"}, {"text": "Meta - Analysis", "type": "ResearchActivity"}, {"text": "SYNTAX", "type": "HealthCareActivity"}, {"text": "PCI", "type": "HealthCareActivity"}, {"text": "Taxus", "type": "MedicalDevice"}, {"text": "Cardiac Surgery", "type": "HealthCareActivity"}, {"text": "PRECOMBAT", "type": "HealthCareActivity"}, {"text": "Bypass Surgery", "type": "HealthCareActivity"}, {"text": "Angioplasty", "type": "HealthCareActivity"}, {"text": "Left Main Coronary Artery Disease", "type": "BiologicFunction"}, {"text": "BEST", "type": "HealthCareActivity"}, {"text": "Everolimus - Eluting Stent", "type": "MedicalDevice"}, {"text": "Implantation", "type": "HealthCareActivity"}, {"text": "Treatment", "type": "HealthCareActivity"}, {"text": "Multivessel Coronary Artery Disease", "type": "BiologicFunction"}, {"text": "Randomized Controlled Trials", "type": "ResearchActivity"}, {"text": "sex", "type": "BiologicFunction"}, {"text": "clinical outcomes", "type": "Finding"}, {"text": "percutaneous coronary intervention", "type": "HealthCareActivity"}, {"text": "coronary artery bypass graft", "type": "HealthCareActivity"}, {"text": "multivessel coronary disease", "type": "BiologicFunction"}, {"text": "left main disease", "type": "BiologicFunction"}, {"text": "Western", "type": "PopulationGroup"}, {"text": "Asian populations", "type": "PopulationGroup"}]}

Example input:
Sentence: To assess clinical outcomes after percutaneous coronary intervention or coronary artery bypass graft in women and men with multivessel coronary disease and unprotected left main disease , a pooled analysis ( n = 3280 ) was performed using the patient - level data from 3 large randomized trials : SYNTAX ( Synergy between PCI with Taxus and Cardiac Surgery ) , PRECOMBAT ( Bypass Surgery Versus Angioplasty Using Sirolimus - Eluting Stent in Patients With Left Main Coronary Artery Disease ) , and BEST ( Bypass Surgery and Everolimus - Eluting Stent Implantation in the Treatment of Patients with Multivessel Coronary Artery Disease ) trials .

Example answer:
{"entities": [{"text": "clinical outcomes", "type": "Finding"}, {"text": "percutaneous coronary intervention", "type": "HealthCareActivity"}, {"text": "coronary artery bypass graft", "type": "HealthCareActivity"}, {"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}, {"text": "multivessel coronary disease", "type": "BiologicFunction"}, {"text": "left main disease", "type": "BiologicFunction"}, {"text": "pooled analysis", "type": "ResearchActivity"}, {"text": "randomized trials", "type": "ResearchActivity"}, {"text": "SYNTAX", "type": "HealthCareActivity"}, {"text": "PCI", "type": "HealthCareActivity"}, {"text": "Taxus", "type": "MedicalDevice"}, {"text": "Cardiac Surgery", "type": "HealthCareActivity"}, {"text": "PRECOMBAT", "type": "HealthCareActivity"}, {"text": "Bypass Surgery", "type": "HealthCareActivity"}, {"text": "Angioplasty", "type": "HealthCareActivity"}, {"text": "Left Main Coronary Artery Disease", "type": "BiologicFunction"}, {"text": "BEST", "type": "HealthCareActivity"}, {"text": "Everolimus - Eluting Stent", "type": "MedicalDevice"}, {"text": "Implantation", "type": "HealthCareActivity"}, {"text": "Treatment", "type": "HealthCareActivity"}, {"text": "Multivessel Coronary Artery Disease", "type": "BiologicFunction"}, {"text": "trials", "type": "ResearchActivity"}]}

Example input:
Sentence: Our study revealed inaccurate agreement ( AAMI ) between the two methods when measuring systolic and mean blood pressures during post - operative care .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "agreement", "type": "ClinicalAttribute"}, {"text": "AAMI", "type": "Organization"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "systolic", "type": "ClinicalAttribute"}, {"text": "mean blood pressures", "type": "Finding"}, {"text": "post - operative care", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the Western trial ( SYNTAX ) , female sex favored coronary artery bypass graft compared with percutaneous coronary intervention ( hazard ratio ( percutaneous coronary intervention ) 2 . 213 ; 95 % confidence interval , 1 . 242 - 3 . 943 ; P = 0 . 007 ) , whereas in the Asian women ( PRECOMBAT and BEST ) , the treatment effect was neutral between both strategies .

Example answer:
{"entities": [{"text": "Western", "type": "PopulationGroup"}, {"text": "trial", "type": "ResearchActivity"}, {"text": "SYNTAX", "type": "HealthCareActivity"}, {"text": "female", "type": "PopulationGroup"}, {"text": "sex", "type": "BiologicFunction"}, {"text": "coronary artery bypass graft", "type": "HealthCareActivity"}, {"text": "percutaneous coronary intervention", "type": "HealthCareActivity"}, {"text": "Asian", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "PRECOMBAT", "type": "HealthCareActivity"}, {"text": "BEST", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "strategies", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the second group , cardiac index and pulse pressure variation values were displayed and kept within target ranges following a pre - defined algorithm ( CI - PPV group ) .

Example answer:
{"entities": [{"text": "cardiac index", "type": "Finding"}, {"text": "pulse pressure", "type": "BiologicFunction"}, {"text": "pre - defined algorithm", "type": "IntellectualProduct"}]}

Example input:
Sentence: All patients had mean arterial pressure , cardiac index and pulse pressure variation measured continuously .

Example answer:
{"entities": [{"text": "mean arterial pressure", "type": "Finding"}, {"text": "cardiac index", "type": "Finding"}, {"text": "pulse pressure", "type": "BiologicFunction"}]}

Example input:
Sentence: In one group , healthcare professionals were blinded to cardiac index and pulse pressure variation values and were asked to guide haemodynamic therapy only based on mean arterial pressure ( control group ) .

Example answer:
{"entities": [{"text": "healthcare professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "blinded", "type": "ResearchActivity"}, {"text": "cardiac index", "type": "Finding"}, {"text": "pulse pressure", "type": "BiologicFunction"}, {"text": "haemodynamic therapy", "type": "HealthCareActivity"}, {"text": "mean arterial pressure", "type": "Finding"}]}

Example input:
Sentence: Therefore , we tested the hypothesis that the addition of non - invasive cardiac index and pulse pressure variation monitoring to mean arterial pressure -based goal - directed therapy would reduce the incidence of postoperative complications in patients having moderate - risk abdominal surgery .

Example answer:
{"entities": [{"text": "tested", "type": "IntellectualProduct"}, {"text": "cardiac index", "type": "Finding"}, {"text": "pulse pressure", "type": "BiologicFunction"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "mean arterial pressure", "type": "Finding"}, {"text": "goal - directed therapy", "type": "HealthCareActivity"}, {"text": "postoperative complications", "type": "BiologicFunction"}]}

Input:
Sentence: The added value of cardiac index and pulse pressure variation monitoring to mean arterial pressure - guided volume therapy in moderate - risk abdominal surgery ( COGUIDE ) : a pragmatic multicentre randomised controlled trial There is disagreement regarding the benefits of goal - directed therapy in moderate - risk abdominal surgery .

## Item MedMentions:test:4739
Example input:
Sentence: In 64 % ( 122 / 191 ) of the clinically healthy Labrador retrievers , hepatic histology revealed inflammatory infiltrates .

Example answer:
{"entities": [{"text": "Labrador retrievers", "type": "Eukaryote"}, {"text": "hepatic histology", "type": "Finding"}, {"text": "inflammatory infiltrates", "type": "Finding"}]}

Example input:
Sentence: Blood biochemistry levels ( Amm , ALT , AST , TBiL , DBiL , ALP , LDH , CK , and Cr ) and prothrombin time ( PT ) were significantly increased ( all P < 0 . 01 ) and albumin ( ALB ) was markedly reduced ( P < 0 . 01 ) compared with baseline values .

Example answer:
{"entities": [{"text": "Blood", "type": "BodySubstance"}, {"text": "biochemistry levels", "type": "Finding"}, {"text": "ALT", "type": "HealthCareActivity"}, {"text": "AST", "type": "HealthCareActivity"}, {"text": "TBiL", "type": "HealthCareActivity"}, {"text": "DBiL", "type": "HealthCareActivity"}, {"text": "ALP", "type": "HealthCareActivity"}, {"text": "LDH", "type": "HealthCareActivity"}, {"text": "CK", "type": "HealthCareActivity"}, {"text": "Cr", "type": "HealthCareActivity"}, {"text": "prothrombin time", "type": "ClinicalAttribute"}, {"text": "PT", "type": "ClinicalAttribute"}, {"text": "albumin", "type": "Chemical"}, {"text": "ALB", "type": "Chemical"}]}

Example input:
Sentence: 191 clinically healthy and 51 clinically ill Labrador retrievers with hepatic histopathology .

Example answer:
{"entities": [{"text": "clinically ill", "type": "Finding"}, {"text": "Labrador retrievers", "type": "Eukaryote"}, {"text": "hepatic", "type": "SpatialConcept"}, {"text": "histopathology", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Alanine transaminase ( ALT ) , aspartate transaminase ( AST ) , blood urea nitrogen ( BUN ) , and creatinine ( CRE ) were detected by an automatic biochemical analyzer .

Example answer:
{"entities": [{"text": "Alanine transaminase", "type": "Chemical"}, {"text": "ALT", "type": "Chemical"}, {"text": "aspartate transaminase", "type": "Chemical"}, {"text": "AST", "type": "Chemical"}, {"text": "blood urea nitrogen", "type": "Chemical"}, {"text": "BUN", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "CRE", "type": "Chemical"}, {"text": "detected", "type": "Finding"}, {"text": "analyzer", "type": "MedicalDevice"}]}

Example input:
Sentence: Medical records were reviewed for ALT , ALP , preprandial BA , liver histopathology , and hepatic copper concentrations .

Example answer:
{"entities": [{"text": "Medical records", "type": "IntellectualProduct"}, {"text": "ALT", "type": "Chemical"}, {"text": "ALP", "type": "Chemical"}, {"text": "BA", "type": "Chemical"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "histopathology", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Histopathologic abnormalities in the liver were present in the majority of apparent clinically healthy Labrador retrievers .

Example answer:
{"entities": [{"text": "Histopathologic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "abnormalities", "type": "Finding"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "present", "type": "Finding"}, {"text": "Labrador retrievers", "type": "Eukaryote"}]}

Example input:
Sentence: More sensitive biomarkers are needed for early detection of liver disease in apparent clinically healthy dogs .

Example answer:
{"entities": [{"text": "biomarkers", "type": "ClinicalAttribute"}, {"text": "early detection", "type": "HealthCareActivity"}, {"text": "liver disease", "type": "BiologicFunction"}, {"text": "dogs", "type": "Eukaryote"}]}

Example input:
Sentence: When increased liver enzymes were present , median ALT was significantly higher in PH cases ( 312 U / L , range 38 - 1 , 369 ) compared to RH cases ( 91 U / L , range 39 - 139 ) ( P < .001 ) .

Example answer:
{"entities": [{"text": "increased liver enzymes", "type": "Finding"}, {"text": "present", "type": "Finding"}, {"text": "ALT", "type": "Chemical"}, {"text": "PH", "type": "BiologicFunction"}]}

Example input:
Sentence: Sensitivity of ALT , ALP , and BA in this population for detecting acute hepatitis was 45 , 15 , and 15 % , respectively .

Example answer:
{"entities": [{"text": "Sensitivity", "type": "ResearchActivity"}, {"text": "ALT", "type": "Chemical"}, {"text": "ALP", "type": "Chemical"}, {"text": "BA", "type": "Chemical"}, {"text": "population", "type": "Eukaryote"}, {"text": "acute hepatitis", "type": "BiologicFunction"}]}

Example input:
Sentence: To determine the sensitivity and specificity of ALT , ALP , and BA for detecting primary hepatitis ( PH ) in clinically healthy Labrador retrievers and investigate whether ALT and ALP can discriminate between dogs with PH and nonspecific reactive hepatitis ( RH ) .

Example answer:
{"entities": [{"text": "ALT", "type": "Chemical"}, {"text": "ALP", "type": "Chemical"}, {"text": "BA", "type": "Chemical"}, {"text": "detecting", "type": "Finding"}, {"text": "primary hepatitis", "type": "BiologicFunction"}, {"text": "PH", "type": "BiologicFunction"}, {"text": "Labrador retrievers", "type": "Eukaryote"}, {"text": "dogs", "type": "Eukaryote"}]}

Input:
Sentence: Sensitivity and Specificity of Plasma ALT , ALP , and Bile Acids for Hepatitis in Labrador Retrievers Biochemical indicators for diagnosing liver disease are plasma alanine aminotransferase activity ( ALT ) , alkaline phosphatase activity ( ALP ) , and bile acid concentration ( BA ) .
