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

## Item MedMentions:test:730
Example input:
Sentence: It was observed that stronger regularization might corrupt the microstructure analysis , because the trabecular structure is a very small detail that might get lost during the regularization process .

Example answer:
{"entities": [{"text": "microstructure", "type": "SpatialConcept"}, {"text": "trabecular", "type": "AnatomicalStructure"}, {"text": "structure", "type": "SpatialConcept"}]}

Example input:
Sentence: Notably , the PET imaging of ( 18 ) F - Alfatide II and ( 18 ) F - FMISO was significantly correlated ( all P < 0 . 05 ) with TGR , whereas the imaging of ( 18 ) F - FDG and ( 18 ) F - ML - 10 was not significantly correlated with TGR .

Example answer:
{"entities": [{"text": "PET imaging", "type": "HealthCareActivity"}, {"text": "( 18 ) F - Alfatide II", "type": "Chemical"}, {"text": "( 18 ) F - FMISO", "type": "Chemical"}, {"text": "( 18 ) F - FDG", "type": "Chemical"}, {"text": "( 18 ) F - ML - 10", "type": "Chemical"}]}

Example input:
Sentence: The IRAB and PDL of M1 were examined by microcomputed tomography ( micro - CT ) analysis .

Example answer:
{"entities": [{"text": "IRAB", "type": "AnatomicalStructure"}, {"text": "PDL", "type": "AnatomicalStructure"}, {"text": "M1", "type": "AnatomicalStructure"}, {"text": "microcomputed tomography", "type": "HealthCareActivity"}, {"text": "micro - CT", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Effect of Low - Dose MDCT and Iterative Reconstruction on Trabecular Bone Microstructure Assessment We investigated the effects of low - dose multi detector computed tomography ( MDCT ) in combination with statistical iterative reconstruction algorithms on trabecular bone microstructure parameters .

Example answer:
{"entities": [{"text": "MDCT", "type": "HealthCareActivity"}, {"text": "Iterative Reconstruction", "type": "HealthCareActivity"}, {"text": "Trabecular Bone", "type": "AnatomicalStructure"}, {"text": "Microstructure", "type": "SpatialConcept"}, {"text": "multi detector computed tomography", "type": "HealthCareActivity"}, {"text": "statistical iterative reconstruction", "type": "HealthCareActivity"}, {"text": "algorithms", "type": "IntellectualProduct"}, {"text": "trabecular bone", "type": "AnatomicalStructure"}, {"text": "microstructure", "type": "SpatialConcept"}]}

Example input:
Sentence: The added - value of PBD to reduce the false - negative rate of SLN mapping is only limited to the rare cases in which no radioactivity is detectable in the axilla ( < 1 % ) .

Example answer:
{"entities": [{"text": "PBD", "type": "Chemical"}, {"text": "false - negative", "type": "Finding"}, {"text": "SLN mapping", "type": "HealthCareActivity"}, {"text": "detectable", "type": "ClinicalAttribute"}, {"text": "axilla", "type": "SpatialConcept"}]}

Example input:
Sentence: The most important significant parameters for RFS were intrinsic subtypes ( p < 0 . 001 ) and tumor size ( p < 0 . 001 ) and for OAS age ( p < 0 . 001 ) and intrinsic subtypes ( p < 0 . 001 ) .

Example answer:
{"entities": [{"text": "intrinsic", "type": "SpatialConcept"}, {"text": "subtypes", "type": "IntellectualProduct"}, {"text": "tumor size", "type": "SpatialConcept"}]}

Example input:
Sentence: While all FGMs had lower dogboning in comparison to the stents made of the uniform materials , the stent with the lowest heterogeneous index displayed the lowest amount of dogboning .

Example answer:
{"entities": [{"text": "stents", "type": "MedicalDevice"}, {"text": "stent", "type": "MedicalDevice"}, {"text": "heterogeneous index", "type": "IntellectualProduct"}]}

Example input:
Sentence: Longitudinal MicroPET / CT scans with ( 18 ) F - FDG , ( 18 ) F - FMISO , ( 18 ) F - ML - 10 and ( 18 ) F - Alfatide II were acquired to quantitatively measure metabolism , hypoxia , apoptosis and angiogenesis on days 0 , 1 , 3 , 7 and 13 following therapy initiation .

Example answer:
{"entities": [{"text": "Longitudinal", "type": "SpatialConcept"}, {"text": "MicroPET / CT scans", "type": "HealthCareActivity"}, {"text": "( 18 ) F - FDG", "type": "Chemical"}, {"text": "( 18 ) F - FMISO ,", "type": "Chemical"}, {"text": "( 18 ) F - ML - 10", "type": "Chemical"}, {"text": "( 18 ) F - Alfatide II", "type": "Chemical"}, {"text": "metabolism", "type": "BiologicFunction"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "angiogenesis", "type": "BiologicFunction"}, {"text": "therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: As a consequence , the introduction of SIR for trabecular bone microstructure analysis requires a specific optimization of the regularization parameters .

Example answer:
{"entities": [{"text": "SIR", "type": "HealthCareActivity"}, {"text": "trabecular bone", "type": "AnatomicalStructure"}, {"text": "microstructure", "type": "SpatialConcept"}]}

Example input:
Sentence: Trabecular bone microstructure parameters based on low - dose MDCT and SIR significantly correlated with vertebral bone strength .

Example answer:
{"entities": [{"text": "Trabecular bone", "type": "AnatomicalStructure"}, {"text": "microstructure", "type": "SpatialConcept"}, {"text": "MDCT", "type": "HealthCareActivity"}, {"text": "SIR", "type": "HealthCareActivity"}, {"text": "vertebral bone", "type": "AnatomicalStructure"}]}

Input:
Sentence: There was no significant difference between microstructure parameters calculated on low - dose SIR and standard - dose FBP images .

## Item MedMentions:test:633
Example input:
Sentence: At enrollment , late - onset SLE patients had a lower total number of American College of Rheumatology ( ACR ) criteria , with less renal and neurologic manifestations .

Example answer:
{"entities": [{"text": "SLE", "type": "BiologicFunction"}, {"text": "American College of Rheumatology ( ACR ) criteria", "type": "IntellectualProduct"}, {"text": "neurologic manifestations", "type": "Finding"}]}

Example input:
Sentence: The second patient was a young woman with fever , anasarca , bicytopenia and reticulin fibrosis in the marrow biopsy .

Example answer:
{"entities": [{"text": "woman", "type": "PopulationGroup"}, {"text": "fever", "type": "Finding"}, {"text": "anasarca", "type": "Finding"}, {"text": "bicytopenia", "type": "Finding"}, {"text": "reticulin fibrosis", "type": "Finding"}, {"text": "marrow biopsy", "type": "HealthCareActivity"}]}

Example input:
Sentence: The results suggest that anxiety and depression are common in patients with SLE in Southwest China .

Example answer:
{"entities": [{"text": "anxiety", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "SLE", "type": "BiologicFunction"}, {"text": "Southwest", "type": "SpatialConcept"}, {"text": "China", "type": "SpatialConcept"}]}

Example input:
Sentence: This study aimed to examine whether the association between antenatal SLE and PPD symptoms was moderated by women 's state - level SES .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "PPD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "women 's", "type": "PopulationGroup"}]}

Example input:
Sentence: Rarely it may occur in patients with autoimmune markers but no definable autoimmune disease ( Primary - AIMF ) .

Example answer:
{"entities": [{"text": "autoimmune markers", "type": "ClinicalAttribute"}, {"text": "autoimmune disease", "type": "BiologicFunction"}, {"text": "Primary - AIMF", "type": "BiologicFunction"}]}

Example input:
Sentence: Results A total of 86 patients with late - onset disease ( 84 . 9 % female , 81 . 4 % Caucasian , mean age at SLE diagnosis ± SD 58 . 05 ± 7 . 30 ) and 169 patients with early - onset disease ( 86 . 4 % female , 71 % Caucasian , mean age at SLE diagnosis ± SD 27 . 80 ± 5 . 90 ) were identified .

Example answer:
{"entities": [{"text": "disease", "type": "BiologicFunction"}, {"text": "Caucasian", "type": "PopulationGroup"}, {"text": "SLE", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}]}

Example input:
Sentence: Autoimmune Myelofibrosis in Systemic Lupus Erythematosus Report of Two Cases and Review of the Literature Autoimmune myelofibrosis ( AIMF ) is a rare entity of steroid - responsive bone marrow fibrosis that accompanies a variety of autoimmune diseases , particularly systemic lupus erythematosus ( SLE ) .

Example answer:
{"entities": [{"text": "Autoimmune Myelofibrosis", "type": "BiologicFunction"}, {"text": "Systemic Lupus Erythematosus", "type": "BiologicFunction"}, {"text": "Literature", "type": "IntellectualProduct"}, {"text": "Autoimmune myelofibrosis", "type": "BiologicFunction"}, {"text": "AIMF", "type": "BiologicFunction"}, {"text": "steroid", "type": "Chemical"}, {"text": "bone marrow fibrosis", "type": "BiologicFunction"}, {"text": "autoimmune diseases", "type": "BiologicFunction"}, {"text": "systemic lupus erythematosus", "type": "BiologicFunction"}, {"text": "SLE", "type": "BiologicFunction"}]}

Example input:
Sentence: Whether AIMF is one of several hematological complications of SLE , or represents a unique and distinct subset of patients with SLE in not clear .

Example answer:
{"entities": [{"text": "AIMF", "type": "BiologicFunction"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "SLE", "type": "BiologicFunction"}]}

Example input:
Sentence: A review of the literature revealed a total of 30 patients with SLE - AIMF reported to - date .

Example answer:
{"entities": [{"text": "literature", "type": "IntellectualProduct"}, {"text": "SLE", "type": "BiologicFunction"}, {"text": "AIMF", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients with SLE - AIMF are young women with SLE and blood cytopenia who are found to have increased bone marrow reticulin on marrow biopsy .

Example answer:
{"entities": [{"text": "SLE", "type": "BiologicFunction"}, {"text": "AIMF", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "blood cytopenia", "type": "BiologicFunction"}, {"text": "bone marrow reticulin", "type": "Finding"}, {"text": "marrow biopsy", "type": "HealthCareActivity"}]}

Input:
Sentence: We report the cases of two young women with SLE - associated AIMF ( SLE - AIMF ) .

## Item MedMentions:test:635
Example input:
Sentence: Autoimmune Myelofibrosis in Systemic Lupus Erythematosus Report of Two Cases and Review of the Literature Autoimmune myelofibrosis ( AIMF ) is a rare entity of steroid - responsive bone marrow fibrosis that accompanies a variety of autoimmune diseases , particularly systemic lupus erythematosus ( SLE ) .

Example answer:
{"entities": [{"text": "Autoimmune Myelofibrosis", "type": "BiologicFunction"}, {"text": "Systemic Lupus Erythematosus", "type": "BiologicFunction"}, {"text": "Literature", "type": "IntellectualProduct"}, {"text": "Autoimmune myelofibrosis", "type": "BiologicFunction"}, {"text": "AIMF", "type": "BiologicFunction"}, {"text": "steroid", "type": "Chemical"}, {"text": "bone marrow fibrosis", "type": "BiologicFunction"}, {"text": "autoimmune diseases", "type": "BiologicFunction"}, {"text": "systemic lupus erythematosus", "type": "BiologicFunction"}, {"text": "SLE", "type": "BiologicFunction"}]}

Example input:
Sentence: This study aimed to examine whether the association between antenatal SLE and PPD symptoms was moderated by women 's state - level SES .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "PPD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "women 's", "type": "PopulationGroup"}]}

Example input:
Sentence: Disease evolution in late - onset and early - onset systemic lupus erythematosus Objective The objective of this study was to compare clinical features , disease activity , and outcome in late - onset versus early - onset systemic lupus erythematosus ( SLE ) over 5 years of follow up Method Patients with SLE since 1970 were followed prospectively according to standard protocol and tracked on a computerized database .

Example answer:
{"entities": [{"text": "early - onset", "type": "Finding"}, {"text": "systemic lupus erythematosus", "type": "BiologicFunction"}, {"text": "objective", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "outcome", "type": "Finding"}, {"text": "SLE", "type": "BiologicFunction"}, {"text": "follow up", "type": "HealthCareActivity"}, {"text": "standard protocol", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , randomized clinical trials with long - term follow - up periods are needed to confirm their efficacy in reducing the prevalence / incidence of oral infectious diseases .

Example answer:
{"entities": [{"text": "randomized clinical trials", "type": "ResearchActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "oral infectious diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Rarely it may occur in patients with autoimmune markers but no definable autoimmune disease ( Primary - AIMF ) .

Example answer:
{"entities": [{"text": "autoimmune markers", "type": "ClinicalAttribute"}, {"text": "autoimmune disease", "type": "BiologicFunction"}, {"text": "Primary - AIMF", "type": "BiologicFunction"}]}

Example input:
Sentence: Results A total of 86 patients with late - onset disease ( 84 . 9 % female , 81 . 4 % Caucasian , mean age at SLE diagnosis ± SD 58 . 05 ± 7 . 30 ) and 169 patients with early - onset disease ( 86 . 4 % female , 71 % Caucasian , mean age at SLE diagnosis ± SD 27 . 80 ± 5 . 90 ) were identified .

Example answer:
{"entities": [{"text": "disease", "type": "BiologicFunction"}, {"text": "Caucasian", "type": "PopulationGroup"}, {"text": "SLE", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}]}

Example input:
Sentence: At enrollment , late - onset SLE patients had a lower total number of American College of Rheumatology ( ACR ) criteria , with less renal and neurologic manifestations .

Example answer:
{"entities": [{"text": "SLE", "type": "BiologicFunction"}, {"text": "American College of Rheumatology ( ACR ) criteria", "type": "IntellectualProduct"}, {"text": "neurologic manifestations", "type": "Finding"}]}

Example input:
Sentence: Patients with SLE - AIMF are young women with SLE and blood cytopenia who are found to have increased bone marrow reticulin on marrow biopsy .

Example answer:
{"entities": [{"text": "SLE", "type": "BiologicFunction"}, {"text": "AIMF", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "blood cytopenia", "type": "BiologicFunction"}, {"text": "bone marrow reticulin", "type": "Finding"}, {"text": "marrow biopsy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Whether AIMF is one of several hematological complications of SLE , or represents a unique and distinct subset of patients with SLE in not clear .

Example answer:
{"entities": [{"text": "AIMF", "type": "BiologicFunction"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "SLE", "type": "BiologicFunction"}]}

Example input:
Sentence: A review of the literature revealed a total of 30 patients with SLE - AIMF reported to - date .

Example answer:
{"entities": [{"text": "literature", "type": "IntellectualProduct"}, {"text": "SLE", "type": "BiologicFunction"}, {"text": "AIMF", "type": "BiologicFunction"}]}

Input:
Sentence: Prospective studies with longer follow - up are needed to better define the prevalence and clinical spectrum of SLE - AIMF .

## Item MedMentions:test:514
Example input:
Sentence: Most sites ( 63 % ) had access to Xpert , either in the clinic ( 13 % ) , in the same facility ( 20 % ) or offsite ( 30 % ) .

Example answer:
{"entities": [{"text": "sites", "type": "SpatialConcept"}, {"text": "access", "type": "SpatialConcept"}, {"text": "Xpert", "type": "HealthCareActivity"}, {"text": "clinic", "type": "Organization"}, {"text": "offsite", "type": "SpatialConcept"}]}

Example input:
Sentence: Our hospital - based intervention was feasible , acceptable and showed preliminary health and well - being gains .

Example answer:
{"entities": [{"text": "hospital - based intervention", "type": "HealthCareActivity"}, {"text": "preliminary health and well - being gains", "type": "Finding"}]}

Example input:
Sentence: Use of Six Sigma Methodology to Reduce Appointment Lead - Time in Obstetrics Outpatient Department This paper focuses on the issue of longer appointment lead - time in the obstetrics outpatient department of a maternal - child hospital in Colombia .

Example answer:
{"entities": [{"text": "Obstetrics Outpatient Department", "type": "Organization"}, {"text": "issue", "type": "Finding"}, {"text": "obstetrics outpatient department", "type": "Organization"}, {"text": "maternal - child hospital", "type": "Organization"}, {"text": "Colombia", "type": "SpatialConcept"}]}

Example input:
Sentence: In addition to conventional methods ( steam autoclave and gamma irradiation ) , a recent ozone - based method of sterilization was also tested .

Example answer:
{"entities": [{"text": "methods", "type": "IntellectualProduct"}, {"text": "steam autoclave", "type": "MedicalDevice"}, {"text": "gamma irradiation", "type": "HealthCareActivity"}, {"text": "ozone - based", "type": "Chemical"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "sterilization", "type": "HealthCareActivity"}]}

Example input:
Sentence: In fact a radiotherapy department with a combination of technologies , including orthovoltage X - ray units , may be an option .

Example answer:
{"entities": [{"text": "radiotherapy department", "type": "Organization"}, {"text": "orthovoltage X - ray units", "type": "Organization"}]}

Example input:
Sentence: The aim of this study was to evaluate an original technique used for enabling percutaneous remote access for thoracic or abdominal endovascular aortic repair in patients with scar tissue and / or a vascular graft in the groin .

Example answer:
{"entities": [{"text": "percutaneous remote access", "type": "SpatialConcept"}, {"text": "thoracic", "type": "HealthCareActivity"}, {"text": "abdominal endovascular aortic repair", "type": "HealthCareActivity"}, {"text": "scar tissue", "type": "Finding"}, {"text": "groin", "type": "SpatialConcept"}]}

Example input:
Sentence: Request and fulfillment of postpartum tubal ligation in patients after high - risk pregnancy Female sterilization is one of the most prevalent methods of contraception in the United States .

Example answer:
{"entities": [{"text": "tubal ligation", "type": "HealthCareActivity"}, {"text": "high - risk pregnancy", "type": "BiologicFunction"}, {"text": "Female sterilization", "type": "HealthCareActivity"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "contraception", "type": "HealthCareActivity"}, {"text": "United States", "type": "SpatialConcept"}]}

Example input:
Sentence: Esophageal stenting is relatively safe procedure with short stay of the patient in the hospital .

Example answer:
{"entities": [{"text": "Esophageal stenting", "type": "HealthCareActivity"}, {"text": "procedure", "type": "HealthCareActivity"}, {"text": "hospital", "type": "Organization"}]}

Example input:
Sentence: This study was conducted with the aim of evaluating the technology of regional sterilization centers .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "evaluating", "type": "HealthCareActivity"}, {"text": "regional", "type": "SpatialConcept"}, {"text": "sterilization", "type": "HealthCareActivity"}, {"text": "centers", "type": "Organization"}]}

Example input:
Sentence: The next step was done to evaluate the economical aspect of off - site sterilization technology using gathered data from systematic review of the texts which were related to the technology and costs of off - site and in - site hospital sterilization .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "off - site", "type": "SpatialConcept"}, {"text": "sterilization", "type": "HealthCareActivity"}, {"text": "review", "type": "IntellectualProduct"}, {"text": "texts", "type": "IntellectualProduct"}, {"text": "in - site", "type": "SpatialConcept"}, {"text": "hospital", "type": "Organization"}]}

Input:
Sentence: According to the revealed evidences and also cost analysis , due to shortage of necessary substructures and economical aspect , installing the off - site sterilization health technology in hospitals is not possible currently . But this method can be used to provide sterilization services for clinics and outpatients centers .

## Item MedMentions:test:663
Example input:
Sentence: Correlations coefficients and associated p values were as follows : invasive contrast left ventriculography versus two - dimensional echocardiography ( r = 0 . 69 , p < 0 . 001 ) , invasive contrast left ventriculography versus gated single - photon emission computed tomography ( r = 0 . 80 , p < 0 . 0001 ) , and gated single - photon emission computed tomography versus two - dimensional echocardiography ( r = 0 . 69 , p < 0 . 001 ) .

Example answer:
{"entities": [{"text": "contrast left ventriculography", "type": "HealthCareActivity"}, {"text": "two - dimensional echocardiography", "type": "HealthCareActivity"}, {"text": "gated", "type": "HealthCareActivity"}, {"text": "single - photon emission computed tomography", "type": "HealthCareActivity"}]}

Example input:
Sentence: cFFR is accurate in predicting the functional significance of coronary stenosis .

Example answer:
{"entities": [{"text": "cFFR", "type": "ClinicalAttribute"}, {"text": "coronary stenosis", "type": "BiologicFunction"}]}

Example input:
Sentence: The clinical diagnosis was FP in 45 . 5 % , nasolacrimal duct stenosis ( NLDS ) in 26 .

Example answer:
{"entities": [{"text": "clinical diagnosis", "type": "HealthCareActivity"}, {"text": "FP", "type": "Finding"}, {"text": "nasolacrimal duct stenosis", "type": "Finding"}, {"text": "NLDS", "type": "Finding"}]}

Example input:
Sentence: The SIR ( 95 % CI ) for a CV event ( myocardial infarction or stroke ) was 0 . 597 ( 0 . 40 - 0 . 86 ) ; this association was only significant in men .

Example answer:
{"entities": [{"text": "CV event", "type": "Finding"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "stroke", "type": "InjuryOrPoisoning"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: 387 to predominating coronary artery disease ( CAD ) .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "BiologicFunction"}, {"text": "CAD", "type": "BiologicFunction"}]}

Example input:
Sentence: Nonstenotic carotid plaque on CT angiography in patients with cryptogenic stroke To determine whether large ( ≥3 mm thick ) but nonstenotic ( < 50 % ) carotid artery atherosclerotic plaque predominantly occurs ipsilateral rather than contralateral to cryptogenic stroke .

Example answer:
{"entities": [{"text": "Nonstenotic", "type": "Finding"}, {"text": "carotid plaque", "type": "AnatomicalStructure"}, {"text": "CT angiography", "type": "HealthCareActivity"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "nonstenotic", "type": "Finding"}, {"text": "carotid artery atherosclerotic plaque", "type": "AnatomicalStructure"}, {"text": "ipsilateral", "type": "SpatialConcept"}, {"text": "contralateral", "type": "SpatialConcept"}]}

Example input:
Sentence: In women with non - obstructive CAD , impaired CFR is associated with higher levels of CPCs , suggesting that chronic myocardial ischemia from CMD stimulates CPC mobilization .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "CAD", "type": "BiologicFunction"}, {"text": "CFR", "type": "HealthCareActivity"}, {"text": "CPCs", "type": "AnatomicalStructure"}, {"text": "chronic myocardial ischemia", "type": "BiologicFunction"}, {"text": "CMD", "type": "BiologicFunction"}, {"text": "stimulates", "type": "Finding"}, {"text": "CPC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Using CT angiography , we measured carotid plaque size ( thickness , mm ) and carotid artery stenosis ( North American Symptomatic Carotid Endarterectomy Trial method ) for each patient .

Example answer:
{"entities": [{"text": "CT angiography", "type": "HealthCareActivity"}, {"text": "carotid plaque", "type": "AnatomicalStructure"}, {"text": "size", "type": "SpatialConcept"}, {"text": "carotid artery stenosis", "type": "BiologicFunction"}, {"text": "North American Symptomatic Carotid Endarterectomy Trial method", "type": "IntellectualProduct"}]}

Example input:
Sentence: Resting Pd / Pa , cFFR and FFR were measured in 1 , 026 coronary stenoses functionally evaluated using commercially available pressure wires .

Example answer:
{"entities": [{"text": "Resting", "type": "Finding"}, {"text": "Pa", "type": "Finding"}, {"text": "cFFR", "type": "ClinicalAttribute"}, {"text": "FFR", "type": "ClinicalAttribute"}, {"text": "coronary stenoses", "type": "BiologicFunction"}, {"text": "pressure wires", "type": "MedicalDevice"}]}

Example input:
Sentence: In 123 women with ischemic symptoms and signs but no obstructive coronary artery disease ( CAD ) enrolled in the Women 's Ischemia Syndrome Evaluation - Coronary Vascular Dysfunction Study ( WISE - CVD ) , we measured coronary flow reserve ( CFR ) in response to intracoronary adenosine .

Example answer:
{"entities": [{"text": "symptoms and signs", "type": "Finding"}, {"text": "coronary artery disease", "type": "BiologicFunction"}, {"text": "CAD", "type": "BiologicFunction"}, {"text": "Women 's", "type": "PopulationGroup"}, {"text": "Ischemia Syndrome", "type": "BiologicFunction"}, {"text": "Evaluation", "type": "HealthCareActivity"}, {"text": "Coronary Vascular Dysfunction", "type": "BiologicFunction"}, {"text": "Study", "type": "ResearchActivity"}, {"text": "WISE - CVD", "type": "Finding"}, {"text": "measured coronary flow reserve", "type": "HealthCareActivity"}, {"text": "CFR", "type": "HealthCareActivity"}, {"text": "adenosine", "type": "Chemical"}]}

Input:
Sentence: FDrecirculation correlated moderately with per cent diameter stenosis in invasive coronary angiography in lesions classified CAD ( r = 0 . 472 , p = 0 .

## Item MedMentions:test:606
Example input:
Sentence: Silencing PLA2 influenced the expression of immune - related genes , including MyD88 and defensin in the Toll pathway and relish and diptericin in the Imd pathway .

Example answer:
{"entities": [{"text": "Silencing", "type": "BiologicFunction"}, {"text": "PLA2", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "immune - related genes", "type": "AnatomicalStructure"}, {"text": "MyD88", "type": "AnatomicalStructure"}, {"text": "defensin", "type": "Chemical"}, {"text": "Toll pathway", "type": "BiologicFunction"}, {"text": "relish", "type": "Chemical"}, {"text": "diptericin", "type": "Chemical"}]}

Example input:
Sentence: Contrary to its canonical repressive activity , PUM1 / 2 rather promote FOXP1 expression by a direct binding to 2 canonical PUM responsive elements present in the FOXP1 - 3 ' untranslated region ( UTR ) .

Example answer:
{"entities": [{"text": "repressive activity", "type": "BiologicFunction"}, {"text": "PUM1", "type": "Chemical"}, {"text": "2", "type": "Chemical"}, {"text": "FOXP1", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "PUM", "type": "Chemical"}, {"text": "responsive elements", "type": "Chemical"}, {"text": "3 ' untranslated region", "type": "SpatialConcept"}, {"text": "UTR", "type": "Chemical"}]}

Example input:
Sentence: An evolutionary conserved Hexim1 peptide binds to the Cdk9 catalytic site to inhibit P - TEFb The positive transcription elongation factor ( P - TEFb ) is required for the transcription of most genes by RNA polymerase II .

Example answer:
{"entities": [{"text": "evolutionary conserved Hexim1 peptide", "type": "Chemical"}, {"text": "binds", "type": "BiologicFunction"}, {"text": "Cdk9", "type": "Chemical"}, {"text": "P - TEFb", "type": "Chemical"}, {"text": "positive transcription elongation factor", "type": "Chemical"}, {"text": "transcription", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "RNA polymerase II", "type": "Chemical"}]}

Example input:
Sentence: Hence , our results reveal that SLP76 - Ser376 phosphorylation does not mediate all HPK1 -dependent regulatory effects in T cells but it fine - tunes helper T cell responses .

Example answer:
{"entities": [{"text": "SLP76 - Ser376", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "HPK1", "type": "Chemical"}, {"text": "T cells", "type": "AnatomicalStructure"}, {"text": "helper T cell", "type": "AnatomicalStructure"}]}

Example input:
Sentence: MIAT siRNA substantially alleviated the Ang II induced upregulation of ANP , BNP and β - MHC in H9c2 cells and markedly attenuated the Ang II induced increase of the cell surface area and the protein synthesis .

Example answer:
{"entities": [{"text": "MIAT", "type": "Chemical"}, {"text": "siRNA", "type": "Chemical"}, {"text": "Ang II", "type": "Chemical"}, {"text": "upregulation", "type": "BiologicFunction"}, {"text": "ANP", "type": "AnatomicalStructure"}, {"text": "BNP", "type": "AnatomicalStructure"}, {"text": "β - MHC", "type": "AnatomicalStructure"}, {"text": "H9c2 cells", "type": "AnatomicalStructure"}, {"text": "cell surface", "type": "AnatomicalStructure"}, {"text": "area", "type": "SpatialConcept"}, {"text": "protein synthesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Compared with the wild type , the serine - threonine mutant polymerases caused a significant decrease of analogue contacts with conserved interrogating residues in motif F and a displacement of metal ion cofactors .

Example answer:
{"entities": [{"text": "wild type", "type": "AnatomicalStructure"}, {"text": "serine - threonine mutant polymerases", "type": "Chemical"}, {"text": "analogue", "type": "Chemical"}, {"text": "conserved interrogating residues", "type": "SpatialConcept"}, {"text": "motif F", "type": "SpatialConcept"}, {"text": "metal ion cofactors", "type": "Chemical"}]}

Example input:
Sentence: Suppression of cPLA2α activity inhibited superoxide production by NOX2 - NADPH oxidase and activation of NF - κB detected by the phosphorylation of p65 on serine 536 at 15 min by LPS and at 4 h by IFNγ .

Example answer:
{"entities": [{"text": "cPLA2α", "type": "Chemical"}, {"text": "superoxide production by NOX2 - NADPH oxidase", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "serine 536", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "IFNγ", "type": "Chemical"}]}

Example input:
Sentence: To address if Prophage 3 affects Pol II activity , we constructed a Prophage 3 negative deletion mutant in E .

Example answer:
{"entities": [{"text": "Prophage 3", "type": "Virus"}, {"text": "Pol II", "type": "Chemical"}, {"text": "activity", "type": "BiologicFunction"}, {"text": "deletion mutant", "type": "BiologicFunction"}, {"text": "E .", "type": "Bacterium"}]}

Example input:
Sentence: coli 83972 modifies host gene expression by inhibition of Pol II phosphorylation , and discusses the ability of ABU strains to actively create an environment that enhances their persistence .

Example answer:
{"entities": [{"text": "coli 83972", "type": "Bacterium"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "Pol II phosphorylation", "type": "BiologicFunction"}, {"text": "ABU", "type": "BiologicFunction"}, {"text": "environment", "type": "SpatialConcept"}, {"text": "persistence", "type": "BiologicFunction"}]}

Example input:
Sentence: coli 83972 and compared the effect on Pol II phosphorylation between the mutant and the E .

Example answer:
{"entities": [{"text": "coli 83972", "type": "Bacterium"}, {"text": "Pol II phosphorylation", "type": "BiologicFunction"}, {"text": "mutant", "type": "AnatomicalStructure"}, {"text": "E .", "type": "Bacterium"}]}

Input:
Sentence: Specific repressors and activators of Pol II - dependent transcription were modified , and Pol II Serine 2 phosphorylation was significantly inhibited , indicating reduced activity of the polymerase .

## Item MedMentions:test:321
Example input:
Sentence: In parallel , a reduction in the percentage of circulating CD4 + T regulatory ( Treg ) cells , starting as early as day 3 post - 6 - OHDA injection , was detected in 6 - OHDA -injected rats .

Example answer:
{"entities": [{"text": "CD4 + T regulatory", "type": "AnatomicalStructure"}, {"text": "Treg", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "6 - OHDA", "type": "Chemical"}, {"text": "injection", "type": "HealthCareActivity"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: In this randomised , double - blind , placebo - controlled , phase 3 study , we enrolled adults ( aged 18 - 75 years ) with indolent or smouldering systemic mastocytosis , according to WHO classification or documented mastocytosis based on histological criteria , at 50 centres in 15 countries .

Example answer:
{"entities": [{"text": "randomised", "type": "ResearchActivity"}, {"text": "double - blind", "type": "ResearchActivity"}, {"text": "placebo - controlled", "type": "ResearchActivity"}, {"text": "phase 3 study", "type": "ResearchActivity"}, {"text": "indolent", "type": "BiologicFunction"}, {"text": "smouldering systemic mastocytosis", "type": "BiologicFunction"}, {"text": "WHO", "type": "Organization"}, {"text": "classification", "type": "IntellectualProduct"}, {"text": "documented", "type": "IntellectualProduct"}, {"text": "mastocytosis", "type": "BiologicFunction"}, {"text": "histological criteria", "type": "ClinicalAttribute"}, {"text": "countries", "type": "SpatialConcept"}]}

Example input:
Sentence: IFN - λ1 induced a dose - dependent increase in number of eosinophils , lymphocytes , mast cells , macrophages , and neutrophils in the peritoneum of mice at 6 h following injection , which was inhibited by pretreatment of the animals with anti - intercellular adhesion molecule - ( ICAM - ) 1 and / or anti - L - selectin antibodies .

Example answer:
{"entities": [{"text": "IFN - λ1", "type": "Chemical"}, {"text": "eosinophils", "type": "AnatomicalStructure"}, {"text": "lymphocytes", "type": "AnatomicalStructure"}, {"text": "mast cells", "type": "AnatomicalStructure"}, {"text": "macrophages", "type": "AnatomicalStructure"}, {"text": "neutrophils", "type": "AnatomicalStructure"}, {"text": "peritoneum", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "injection", "type": "Chemical"}, {"text": "animals", "type": "Eukaryote"}, {"text": "anti - intercellular adhesion molecule - ( ICAM - ) 1", "type": "Chemical"}, {"text": "anti - L - selectin antibodies", "type": "Chemical"}]}

Example input:
Sentence: Early indications include an increased accumulation of TLR7 - expressing Ly6C ( hi ) inflammatory monocytes at the site of injection , upregulation of IFN -regulated gene expression in the peritoneal cavity , and an increased production of myeloid lineage precursors ( common myeloid progenitors and granulocyte myeloid precursors ) in the bone marrow .

Example answer:
{"entities": [{"text": "accumulation", "type": "Finding"}, {"text": "TLR7", "type": "AnatomicalStructure"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "Ly6C ( hi )", "type": "Chemical"}, {"text": "monocytes", "type": "AnatomicalStructure"}, {"text": "site of injection", "type": "SpatialConcept"}, {"text": "upregulation", "type": "BiologicFunction"}, {"text": "IFN", "type": "Chemical"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "peritoneal cavity", "type": "SpatialConcept"}, {"text": "myeloid lineage precursors", "type": "AnatomicalStructure"}, {"text": "common myeloid progenitors", "type": "AnatomicalStructure"}, {"text": "granulocyte", "type": "AnatomicalStructure"}, {"text": "myeloid precursors", "type": "AnatomicalStructure"}, {"text": "bone marrow", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Histamine and serotonin antagonists and indomethacin , but not the NK1 antagonist , decreased cheek oedema in the first 4 h following carrageenan .

Example answer:
{"entities": [{"text": "Histamine", "type": "Chemical"}, {"text": "serotonin antagonists", "type": "Chemical"}, {"text": "indomethacin", "type": "Chemical"}, {"text": "NK1 antagonist", "type": "BiologicFunction"}, {"text": "cheek", "type": "SpatialConcept"}, {"text": "oedema", "type": "Finding"}, {"text": "carrageenan", "type": "Chemical"}]}

Example input:
Sentence: Analysis of skin biopsies before treatment showed a significant increase in Ki - 67 - positive cells in the suprabasal layer and a dysregulated expression of various skin barrier genes , such as claudin 1 , loricrin , filaggrin and cytokeratin 10 , which were normalized after treatment .

Example answer:
{"entities": [{"text": "Analysis", "type": "ResearchActivity"}, {"text": "skin biopsies", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "Ki - 67", "type": "AnatomicalStructure"}, {"text": "positive", "type": "Finding"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "suprabasal layer", "type": "AnatomicalStructure"}, {"text": "dysregulated expression", "type": "BiologicFunction"}, {"text": "skin barrier", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "claudin 1", "type": "AnatomicalStructure"}, {"text": "loricrin", "type": "AnatomicalStructure"}, {"text": "filaggrin", "type": "AnatomicalStructure"}, {"text": "cytokeratin 10", "type": "AnatomicalStructure"}, {"text": "normalized", "type": "ResearchActivity"}]}

Example input:
Sentence: Tissue -selective inflammation in the oral cavity of the rat In the current study , carrageenan ( CG ; 100 - 1000 μg / site ) was injected intraorally in the cheeks of Holtzman or Wistar rats to evaluate the consequences of administration of a non - immunogenic stimulus in the orofacial region .

Example answer:
{"entities": [{"text": "Tissue", "type": "AnatomicalStructure"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "oral cavity", "type": "SpatialConcept"}, {"text": "rat", "type": "Eukaryote"}, {"text": "carrageenan", "type": "Chemical"}, {"text": "CG", "type": "Chemical"}, {"text": "cheeks", "type": "SpatialConcept"}, {"text": "Holtzman", "type": "Eukaryote"}, {"text": "Wistar rats", "type": "Eukaryote"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "non - immunogenic", "type": "Finding"}, {"text": "orofacial region", "type": "IntellectualProduct"}]}

Example input:
Sentence: Subsequent inflammation was measured as oedema ( increased thickness of the cheek wall using digital calipers ) , relative to the other cheek injected with saline .

Example answer:
{"entities": [{"text": "inflammation", "type": "BiologicFunction"}, {"text": "oedema", "type": "Finding"}, {"text": "increased thickness", "type": "Finding"}, {"text": "cheek wall", "type": "SpatialConcept"}, {"text": "digital calipers", "type": "MedicalDevice"}, {"text": "cheek", "type": "SpatialConcept"}]}

Example input:
Sentence: CG induced a dose -related oedema more rapidly from 0 to 2 h which lasted for at least 72 h , showing a biphasic profile ( peak at 2 and 24 h ) , compared with the monophasic oedema induced in rat paws ( maximal duration of 24 h ) .

Example answer:
{"entities": [{"text": "CG", "type": "Chemical"}, {"text": "oedema", "type": "Finding"}, {"text": "rat", "type": "Eukaryote"}, {"text": "paws", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Oedema formation and tissue collection for histopathological studies were assessed at 0 . 5 , 1 , 2 , 3 , 4 , 6 , 24 , 48 , 72 , 96 , 120 and 144 h after injection .

Example answer:
{"entities": [{"text": "Oedema", "type": "Finding"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "histopathological studies", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "injection", "type": "HealthCareActivity"}]}

Input:
Sentence: Histopathological analysis of the CG - injected cheek revealed oedema formation with little leukocyte recruitment at 1 - 3 h , mast cell degranulation at 6 h , and a mixed polymorphonuclear and mononuclear cell infiltrate by 24 h .

## Item MedMentions:test:303
Example input:
Sentence: APC promoter methylation was detected in 30 . 67 % breast cancer tissues and BRCA1 was methylated in 9 .

Example answer:
{"entities": [{"text": "APC", "type": "AnatomicalStructure"}, {"text": "promoter methylation", "type": "BiologicFunction"}, {"text": "detected", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "BRCA1", "type": "AnatomicalStructure"}, {"text": "methylated", "type": "BiologicFunction"}]}

Example input:
Sentence: A differentially methylated region at the Ascl1 promoter , isolated from murine dorsal root ganglion ( hypermethylated ) and striated cells ( hypomethylated ) , was targeted with these optogenetic - epigenetic constructs .

Example answer:
{"entities": [{"text": "Ascl1", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "murine", "type": "Eukaryote"}, {"text": "dorsal root ganglion", "type": "AnatomicalStructure"}, {"text": "hypermethylated", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "hypomethylated", "type": "BiologicFunction"}, {"text": "optogenetic - epigenetic constructs", "type": "Chemical"}]}

Example input:
Sentence: Analysed region for three genes , BCR , IL17RA and RBM38 showed an absolute mean DNA methylation of 25 .

Example answer:
{"entities": [{"text": "Analysed", "type": "ResearchActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "BCR", "type": "AnatomicalStructure"}, {"text": "IL17RA", "type": "AnatomicalStructure"}, {"text": "RBM38", "type": "AnatomicalStructure"}, {"text": "DNA methylation", "type": "BiologicFunction"}]}

Example input:
Sentence: Using genomic DNA of peripheral blood from 14 healthy individuals , DNA methylation in 465 CpG sites from 12 loci of genes ( ADAM22 , ATF2 , BCR , CD83 , CREBBP , IL12B , IL17RA , MAP2K2 , RBM38 , TGFBR2 , TGFBR3 , and WNT5A ) was analysed by targeted next generation bisulfite sequencing .

Example answer:
{"entities": [{"text": "genomic DNA", "type": "Chemical"}, {"text": "peripheral blood", "type": "BodySubstance"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "DNA methylation", "type": "BiologicFunction"}, {"text": "CpG sites", "type": "Chemical"}, {"text": "loci of genes", "type": "AnatomicalStructure"}, {"text": "ADAM22", "type": "AnatomicalStructure"}, {"text": "ATF2", "type": "AnatomicalStructure"}, {"text": "BCR", "type": "AnatomicalStructure"}, {"text": "CD83", "type": "AnatomicalStructure"}, {"text": "CREBBP", "type": "AnatomicalStructure"}, {"text": "IL12B", "type": "AnatomicalStructure"}, {"text": "IL17RA", "type": "AnatomicalStructure"}, {"text": "MAP2K2", "type": "AnatomicalStructure"}, {"text": "RBM38", "type": "AnatomicalStructure"}, {"text": "TGFBR2", "type": "AnatomicalStructure"}, {"text": "TGFBR3", "type": "AnatomicalStructure"}, {"text": "WNT5A", "type": "AnatomicalStructure"}, {"text": "analysed", "type": "ResearchActivity"}, {"text": "next generation bisulfite sequencing", "type": "ResearchActivity"}]}

Example input:
Sentence: The aim of the current investigation was to unveil if methylation circumstances of CpG sites in DNMT1 promoter could affect the mRNA expression level of this gene in peripheral blood mononuclear cells ( PBMCs ) from AS patients .

Example answer:
{"entities": [{"text": "investigation", "type": "HealthCareActivity"}, {"text": "methylation", "type": "BiologicFunction"}, {"text": "CpG", "type": "Chemical"}, {"text": "sites", "type": "SpatialConcept"}, {"text": "DNMT1", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "gene", "type": "AnatomicalStructure"}, {"text": "peripheral blood mononuclear cells", "type": "AnatomicalStructure"}, {"text": "PBMCs", "type": "AnatomicalStructure"}, {"text": "AS", "type": "BiologicFunction"}]}

Example input:
Sentence: The prevalence of methylation in the promoter region of this gene in tumor tissues and autologous controls has not been consistent in previous studies .

Example answer:
{"entities": [{"text": "promoter region", "type": "Chemical"}, {"text": "gene", "type": "AnatomicalStructure"}, {"text": "tumor tissues", "type": "AnatomicalStructure"}, {"text": "autologous controls", "type": "HealthCareActivity"}]}

Example input:
Sentence: The expression of the FZD9 gene was absent in various leukemic cell lines , while it was restored following treatment with DNA demethylating agent 5 - aza - 2 ' - deoxycytidine .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "FZD9 gene", "type": "AnatomicalStructure"}, {"text": "leukemic", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "DNA demethylating agent", "type": "Chemical"}, {"text": "5 - aza - 2 ' - deoxycytidine", "type": "Chemical"}]}

Example input:
Sentence: Bisulfite sequencing analysis of the FZD9 promoter region showed that it was partially methylated in cell lines in which FZD9 gene was not expressed .

Example answer:
{"entities": [{"text": "Bisulfite sequencing analysis", "type": "ResearchActivity"}, {"text": "FZD9", "type": "AnatomicalStructure"}, {"text": "promoter region", "type": "Chemical"}, {"text": "methylated", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "FZD9 gene", "type": "AnatomicalStructure"}, {"text": "expressed", "type": "BiologicFunction"}]}

Example input:
Sentence: In conclusion , the present study indicated that the methylation profile of the FZD9 gene corresponded to that of a candidate tumor - suppressor gene in acute myeloid leukemia .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "methylation", "type": "BiologicFunction"}, {"text": "profile", "type": "HealthCareActivity"}, {"text": "FZD9 gene", "type": "AnatomicalStructure"}, {"text": "tumor - suppressor gene", "type": "AnatomicalStructure"}, {"text": "acute myeloid leukemia", "type": "BiologicFunction"}]}

Example input:
Sentence: The present study examined the involvement of FZD9 promoter methylation in the downregulation of FZD9 expression in leukemia cells .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "examined", "type": "Finding"}, {"text": "FZD9", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "methylation", "type": "BiologicFunction"}, {"text": "downregulation", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "leukemia", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Input:
Sentence: Thus , DNA methylation in the promoter region may lead to inactivation of the FZD9 gene , which may represent and aberration associated with leukemia , since DNA was not methylated in normal peripheral blood mononuclear cells .

## Item MedMentions:test:776
Example input:
Sentence: In the F1 population N345 , 15 % of the population outperformed both parents with the top performing strain having 10 % improvement in ethanol production .

Example answer:
{"entities": [{"text": "population", "type": "Eukaryote"}, {"text": "parents", "type": "Eukaryote"}, {"text": "ethanol production", "type": "BiologicFunction"}]}

Example input:
Sentence: High - end energy drink consumers reported more risk - taking behaviors ( increased drug and alcohol use and less frequent seat belt use ) , sleep disturbances ( later bedtimes , harder time falling asleep , and more all - nighters ) , and higher frequency of mental illness diagnoses than those who consumed fewer energy drinks .

Example answer:
{"entities": [{"text": "energy drink", "type": "Food"}, {"text": "consumers", "type": "PopulationGroup"}, {"text": "seat belt use", "type": "Finding"}, {"text": "sleep disturbances", "type": "Finding"}, {"text": "harder time falling asleep", "type": "BiologicFunction"}, {"text": "mental illness", "type": "BiologicFunction"}, {"text": "diagnoses", "type": "Finding"}, {"text": "energy drinks", "type": "Food"}]}

Example input:
Sentence: Preventing Youth Internalizing Symptoms Through the Familias Unidas Intervention : Examining Variation in Response Prevention programs that strengthen parenting and family functioning have been found to reduce poor behavioral outcomes in adolescents , including substance use , HIV risk , externalizing and internalizing problems .

Example answer:
{"entities": [{"text": "Response", "type": "ClinicalAttribute"}, {"text": "reduce", "type": "HealthCareActivity"}, {"text": "substance use", "type": "BiologicFunction"}]}

Example input:
Sentence: The emergence of drinking behaviors is likely to result from a developmental cascade of interacting variables that make the ontogeny of drinking unlikely to emerge from a single class of variables .

Example answer:
{"entities": [{"text": "ontogeny", "type": "BiologicFunction"}, {"text": "unlikely", "type": "Finding"}, {"text": "single class", "type": "IntellectualProduct"}]}

Example input:
Sentence: On the other hand , adolescent onset of binge drinking predicted poorer performance on broader range of memory tests , including a more systematic test of spatial recognition memory , and an associative learning task .

Example answer:
{"entities": [{"text": "memory", "type": "BiologicFunction"}, {"text": "tests", "type": "IntellectualProduct"}, {"text": "systematic test of spatial recognition memory", "type": "IntellectualProduct"}, {"text": "associative learning", "type": "BiologicFunction"}]}

Example input:
Sentence: The purpose of this study was to examine whether warning feedback from an integrated vehicle - based safety system affected the likelihood that various secondary behaviors were present among drivers ages 16 - 17 , 20 - 30 , 40 - 50 , and 60 - 70 .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "examine", "type": "Finding"}, {"text": "present", "type": "Finding"}, {"text": "drivers", "type": "PopulationGroup"}]}

Example input:
Sentence: The driving performance data and the physiological measurements reported by this paper combined with air - alcohol concentration could be integrated using the support vector regression classification method to establish a better early warning model , thereby improving vehicle safety .

Example answer:
{"entities": [{"text": "reported", "type": "HealthCareActivity"}, {"text": "paper", "type": "IntellectualProduct"}, {"text": "alcohol", "type": "Food"}, {"text": "classification", "type": "IntellectualProduct"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "model", "type": "IntellectualProduct"}]}

Example input:
Sentence: Initiatives should target vulnerable road users , specifically adults > 50 years in urban areas .

Example answer:
{"entities": [{"text": "Initiatives", "type": "BiologicFunction"}, {"text": "users", "type": "PopulationGroup"}]}

Example input:
Sentence: Interventions to improve youths ' well - being should include comprehensive care and education that promotes and supports healthy sexual development .

Example answer:
{"entities": [{"text": "Interventions", "type": "HealthCareActivity"}, {"text": "improve", "type": "Finding"}, {"text": "comprehensive care", "type": "HealthCareActivity"}, {"text": "sexual development", "type": "BiologicFunction"}]}

Example input:
Sentence: Distracting behaviors among teenagers and young , middle - aged , and older adult drivers when driving without and with warnings from an integrated vehicle safety system Negative reinforcement from crash warnings may reduce the likelihood that drivers engage in distracted driving .

Example answer:
{"entities": [{"text": "teenagers", "type": "PopulationGroup"}, {"text": "older adult", "type": "PopulationGroup"}, {"text": "drivers", "type": "PopulationGroup"}, {"text": "Negative reinforcement", "type": "HealthCareActivity"}, {"text": "crash", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: Strengthening of drink driving programs aimed at young drivers / occupants is promising .

## Item MedMentions:test:766
Example input:
Sentence: Most of the hypermethylated genes were involved in the MAPK signaling pathway which is a key regulator for apoptosis while the hypomethylated genes were involved in the PI3K - AKT signaling pathway and proliferation process .

Example answer:
{"entities": [{"text": "hypermethylated genes", "type": "AnatomicalStructure"}, {"text": "MAPK signaling pathway", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "hypomethylated genes", "type": "AnatomicalStructure"}, {"text": "PI3K - AKT signaling pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Comparative gene expression profiling of motor neurons innervating the extensor digitorum longus ( disease - resistant ) , gastrocnemius ( intermediate vulnerability ) , and tibialis anterior ( vulnerable ) muscles in mice revealed that disease susceptibility correlates strongly with a modified bioenergetic profile .

Example answer:
{"entities": [{"text": "gene expression profiling", "type": "HealthCareActivity"}, {"text": "motor neurons", "type": "AnatomicalStructure"}, {"text": "extensor digitorum longus", "type": "AnatomicalStructure"}, {"text": "disease - resistant", "type": "BiologicFunction"}, {"text": "gastrocnemius", "type": "AnatomicalStructure"}, {"text": "tibialis anterior", "type": "AnatomicalStructure"}, {"text": "muscles", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "disease susceptibility", "type": "ClinicalAttribute"}, {"text": "bioenergetic", "type": "BiologicFunction"}, {"text": "profile", "type": "HealthCareActivity"}]}

Example input:
Sentence: Weighted co - expression network analysis revealed a set of conserved lncRNAs that are likely involved in postnatal muscle development .

Example answer:
{"entities": [{"text": "co - expression", "type": "BiologicFunction"}, {"text": "network analysis", "type": "IntellectualProduct"}, {"text": "conserved", "type": "SpatialConcept"}, {"text": "lncRNAs", "type": "Chemical"}, {"text": "muscle development", "type": "BiologicFunction"}]}

Example input:
Sentence: In here , we show that decreased cellular fitness in retinal progenitors caused by reduced Drosophila Myc expression triggers non cell - autonomous activation of retinal glia proliferation and overmigration .

Example answer:
{"entities": [{"text": "cellular", "type": "AnatomicalStructure"}, {"text": "retinal", "type": "AnatomicalStructure"}, {"text": "progenitors", "type": "AnatomicalStructure"}, {"text": "Drosophila", "type": "Eukaryote"}, {"text": "Myc", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "non cell", "type": "AnatomicalStructure"}, {"text": "glia", "type": "AnatomicalStructure"}, {"text": "overmigration", "type": "BiologicFunction"}]}

Example input:
Sentence: In glioma cell lines , we found that decreased miR - 451 expression suppressed tumor cell proliferation but enhanced migration with a concomitant low level of CAB39 / AMPK / mTOR pathway activation and high level of Rac1 / cofilin pathway activation , respectively .

Example answer:
{"entities": [{"text": "glioma", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "miR - 451", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "tumor cell", "type": "AnatomicalStructure"}, {"text": "migration", "type": "BiologicFunction"}, {"text": "CAB39", "type": "Chemical"}, {"text": "AMPK", "type": "Chemical"}, {"text": "mTOR", "type": "Chemical"}, {"text": "Rac1", "type": "Chemical"}]}

Example input:
Sentence: Reduction of extracellular matrix components were mediated via TGFβ signaling pathway inhibition due to downregulation of TGFβ1 , COL1A1 , COL3A1 , HAS2 , HAS3 expression levels .

Example answer:
{"entities": [{"text": "extracellular matrix components", "type": "AnatomicalStructure"}, {"text": "downregulation", "type": "BiologicFunction"}, {"text": "TGFβ1", "type": "AnatomicalStructure"}, {"text": "COL1A1", "type": "AnatomicalStructure"}, {"text": "COL3A1", "type": "AnatomicalStructure"}, {"text": "HAS2", "type": "AnatomicalStructure"}, {"text": "HAS3", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}]}

Example input:
Sentence: Finally , we found that MALAT1 positively regulated FBXW7 expression , which was responsible for glioma progression mediated by MALAT1 - miR - 155 pathway .

Example answer:
{"entities": [{"text": "MALAT1", "type": "Chemical"}, {"text": "positively regulated FBXW7 expression", "type": "BiologicFunction"}, {"text": "glioma progression", "type": "BiologicFunction"}, {"text": "miR - 155 pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Genes were associated with ribosome and focal adhesion functions .

Example answer:
{"entities": [{"text": "Genes", "type": "AnatomicalStructure"}, {"text": "ribosome", "type": "AnatomicalStructure"}, {"text": "focal adhesion", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 1 in skeletal muscle triads The adaptor protein STAC3 is essential for skeletal muscle excitation - contraction ( EC ) coupling and a mutation in the STAC3 gene has been linked to a severe muscle disease , Native American myopathy ( NAM ) .

Example answer:
{"entities": [{"text": "1", "type": "Chemical"}, {"text": "skeletal muscle triads", "type": "AnatomicalStructure"}, {"text": "adaptor protein", "type": "Chemical"}, {"text": "STAC3", "type": "Chemical"}, {"text": "skeletal muscle", "type": "AnatomicalStructure"}, {"text": "excitation - contraction ( EC ) coupling", "type": "BiologicFunction"}, {"text": "mutation", "type": "BiologicFunction"}, {"text": "STAC3 gene", "type": "AnatomicalStructure"}, {"text": "muscle disease", "type": "BiologicFunction"}, {"text": "Native American myopathy", "type": "BiologicFunction"}, {"text": "NAM", "type": "BiologicFunction"}]}

Example input:
Sentence: Kyoto Encyclopedia of Genes and Genomes ( KEGG ) enrichment analysis showed that the neuroactive ligand - receptor interaction , the PI3 K - Akt signaling pathway , and focal adhesions were potentially implicated in SCI pathology .

Example answer:
{"entities": [{"text": "PI3 K", "type": "Chemical"}, {"text": "Akt", "type": "Chemical"}, {"text": "signaling pathway", "type": "BiologicFunction"}, {"text": "focal adhesions", "type": "AnatomicalStructure"}, {"text": "SCI", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: Three modules were identified , in which genes were involved in muscle contraction , negative regulation of glial cell proliferation and extracellular matrix organization functions , respectively .

## Item MedMentions:test:890
Example input:
Sentence: A critical feature in working with this client group is to recognize their ambiguity and the fragility and temporality of their decisions about their destiny .

Example answer:
{"entities": [{"text": "fragility", "type": "Finding"}, {"text": "temporality", "type": "BiologicFunction"}, {"text": "decisions", "type": "BiologicFunction"}]}

Example input:
Sentence: They resulted in uptake of knowledge among participants .

Example answer:
{"entities": [{"text": "uptake of knowledge", "type": "Finding"}, {"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: The outputs from stages 1 - 3 were translated into a design brief and specification ( stage 4 ) , which guided the building of a functioning prototype , Web -based intervention ( stage 5 ) .

Example answer:
{"entities": [{"text": "specification", "type": "IntellectualProduct"}, {"text": "prototype", "type": "IntellectualProduct"}, {"text": "intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: Study concept and design were contributed by Chastek , Nagar , and Dalal .

Example answer:
{"entities": []}

Example input:
Sentence: Domain experts established a reference standard by manually annotating 282 reports to train and then test the NLP application .

Example answer:
{"entities": [{"text": "experts", "type": "ProfessionalOrOccupationalGroup"}, {"text": "reports", "type": "IntellectualProduct"}]}

Example input:
Sentence: A two - level full factorial design was employed .

Example answer:
{"entities": []}

Example input:
Sentence: Items rated very or extremely important by 80 % or more of the experts were reviewed in the final group round to build the final set .

Example answer:
{"entities": [{"text": "experts", "type": "ProfessionalOrOccupationalGroup"}, {"text": "set", "type": "IntellectualProduct"}]}

Example input:
Sentence: A multidisciplinary design charrette was held to test the feasibility of incorporating these tactics into near - highway housing and school developments that were in the planning stages .

Example answer:
{"entities": [{"text": "school", "type": "Organization"}, {"text": "planning", "type": "BiologicFunction"}]}

Example input:
Sentence: Integrating Evidence From Systematic Reviews , Qualitative Research , and Expert Knowledge Using Co - Design Techniques to Develop a Web -Based Intervention for People in the Retirement Transition Integrating stakeholder involvement in complex health intervention design maximizes acceptability and potential effectiveness .

Example answer:
{"entities": [{"text": "Systematic Reviews", "type": "IntellectualProduct"}, {"text": "Qualitative Research", "type": "ResearchActivity"}, {"text": "Expert", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Knowledge", "type": "IntellectualProduct"}, {"text": "Intervention", "type": "HealthCareActivity"}, {"text": "People", "type": "PopulationGroup"}, {"text": "Retirement", "type": "Finding"}, {"text": "stakeholder", "type": "PopulationGroup"}, {"text": "intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: A Universal Design perspective with a holistic understanding remains critical to the foundation of this research study .

Example answer:
{"entities": [{"text": "Universal Design perspective", "type": "IntellectualProduct"}, {"text": "research study", "type": "ResearchActivity"}]}

Input:
Sentence: The design expert made an invaluable contribution throughout the process .

## Item MedMentions:test:846
Example input:
Sentence: In a group of older adult humans at the earliest stages of cognitive decline , we show that alERC volume selectively predicted configural processing ( attention to the spatial arrangement of an object 's parts ) .

Example answer:
{"entities": [{"text": "humans", "type": "Eukaryote"}, {"text": "cognitive decline", "type": "BiologicFunction"}, {"text": "alERC", "type": "AnatomicalStructure"}, {"text": "configural processing", "type": "IntellectualProduct"}, {"text": "attention", "type": "BiologicFunction"}, {"text": "spatial arrangement", "type": "SpatialConcept"}]}

Example input:
Sentence: All outcome measures recorded a large effect size ; the highest was for knowledge ( partial eta2 = 0 . 98 ) , and the least was for perceived burden ( partial eta2 = 0 . 71 ) .

Example answer:
{"entities": [{"text": "knowledge", "type": "Finding"}]}

Example input:
Sentence: Patients had lower information - processing efficiency ( " drift rate " ) and longer nondecision time than controls , and psychosis per se did not influence response caution .

Example answer:
{"entities": [{"text": "psychosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Cognitive load was found to affect spatial recall detrimentally regardless of interference modality .

Example answer:
{"entities": [{"text": "spatial recall", "type": "Finding"}, {"text": "interference", "type": "BiologicFunction"}]}

Example input:
Sentence: Implications of these findings for explanations of the survival - processing advantage are discussed .

Example answer:
{"entities": []}

Example input:
Sentence: In three experiments , we investigated the differences between these studies to achieve a better understanding of dual - task effects on the survival - processing advantage .

Example answer:
{"entities": [{"text": "understanding", "type": "BiologicFunction"}]}

Example input:
Sentence: This phenomenon is known as the survival processing effect .

Example answer:
{"entities": [{"text": "survival processing effect", "type": "BiologicFunction"}]}

Example input:
Sentence: What kind of processing is survival processing ? : Effects of different types of dual - task load on the survival processing effect Words judged for their relevance in a survival context are remembered better than words processed in non - survival contexts .

Example answer:
{"entities": [{"text": "survival processing", "type": "BiologicFunction"}, {"text": "Words judged", "type": "BiologicFunction"}, {"text": "words processed", "type": "BiologicFunction"}]}

Example input:
Sentence: Results consistently showed that the survival processing effect persisted under low load but vanished when the number of items held in working memory increased beyond one , irrespective of processing demands .

Example answer:
{"entities": [{"text": "survival processing", "type": "BiologicFunction"}, {"text": "working memory", "type": "BiologicFunction"}]}

Example input:
Sentence: Whereas Kroneisen , Rummel , and Erdfelder ( Memory 22 : 92 - 102 , 2014 ) observed that the survival processing effect vanishes under dual - task conditions , Stillman , Coane , Profaci , Howard , and Howard ( Memory & Cognition 42 : 175 - 185 , 2014 , Experiment 1 ) found that the size of survival processing effect is essentially unaffected by a cognitively demanding secondary task .

Example answer:
{"entities": [{"text": "Kroneisen", "type": "PopulationGroup"}, {"text": "Rummel", "type": "PopulationGroup"}, {"text": "Erdfelder", "type": "PopulationGroup"}, {"text": "Memory", "type": "BiologicFunction"}, {"text": "survival processing effect", "type": "BiologicFunction"}, {"text": "Stillman", "type": "PopulationGroup"}, {"text": "Coane", "type": "PopulationGroup"}, {"text": "Profaci", "type": "PopulationGroup"}, {"text": "Howard", "type": "PopulationGroup"}, {"text": "size", "type": "SpatialConcept"}, {"text": "survival processing", "type": "BiologicFunction"}, {"text": "cognitively demanding secondary task", "type": "BiologicFunction"}]}

Input:
Sentence: Recently , inconsistent results were reported on whether the size of the survival processing effect is affected by cognitive load .

## Item MedMentions:test:634
Example input:
Sentence: Repeat marrow biopsy showed marked regression of marrow fibrosis .

Example answer:
{"entities": [{"text": "marrow biopsy", "type": "HealthCareActivity"}, {"text": "marked regression", "type": "BiologicFunction"}, {"text": "marrow fibrosis", "type": "BiologicFunction"}]}

Example input:
Sentence: She underwent a transsphenoidal biopsy , which yielded a diagnosis of DLBCL with an activated B - cell immunophenotype with somatotroph hyperplasia .

Example answer:
{"entities": [{"text": "transsphenoidal biopsy", "type": "HealthCareActivity"}, {"text": "diagnosis", "type": "Finding"}, {"text": "DLBCL", "type": "BiologicFunction"}, {"text": "B - cell", "type": "AnatomicalStructure"}, {"text": "immunophenotype", "type": "HealthCareActivity"}, {"text": "somatotroph hyperplasia", "type": "AnatomicalStructure"}]}

Example input:
Sentence: With a clinical suspicion of infection and haemophagocytic lymphohistiocytosis bone marrow aspiration ( BMA ) and biopsy ( BMBx ) was done .

Example answer:
{"entities": [{"text": "suspicion", "type": "BiologicFunction"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "haemophagocytic lymphohistiocytosis", "type": "BiologicFunction"}, {"text": "bone marrow aspiration ( BMA ) and biopsy ( BMBx )", "type": "HealthCareActivity"}]}

Example input:
Sentence: A 30 - year - old female patient with HIV / AIDS and CKD on hemodialysis was admitted to the emergency room for complaints of fever , prostration , and headache in the last six days .

Example answer:
{"entities": [{"text": "CKD", "type": "BiologicFunction"}, {"text": "hemodialysis", "type": "HealthCareActivity"}, {"text": "admitted to the emergency room", "type": "HealthCareActivity"}, {"text": "fever", "type": "Finding"}, {"text": "prostration", "type": "Finding"}, {"text": "headache", "type": "Finding"}]}

Example input:
Sentence: This case was unusual as the diagnosis of a primary aggressive lymphoma with haemophagocytosis was established in a patient who presented with fever and splenic infarct without lymphadenopathy .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "primary aggressive lymphoma", "type": "BiologicFunction"}, {"text": "haemophagocytosis", "type": "BiologicFunction"}, {"text": "fever", "type": "Finding"}, {"text": "splenic infarct", "type": "BiologicFunction"}, {"text": "lymphadenopathy", "type": "BiologicFunction"}]}

Example input:
Sentence: We describe a case of plasmablastic transformation having a pan T - cell phenotype with CD3 and CD4 positivity , in an immunocompetent elderly lady diagnosed with PCM .

Example answer:
{"entities": [{"text": "plasmablastic transformation", "type": "BiologicFunction"}, {"text": "pan T - cell phenotype", "type": "Chemical"}, {"text": "CD3", "type": "Chemical"}, {"text": "CD4", "type": "Chemical"}, {"text": "immunocompetent", "type": "ClinicalAttribute"}, {"text": "diagnosed", "type": "Finding"}, {"text": "PCM", "type": "BiologicFunction"}]}

Example input:
Sentence: Patient was being managed as splenic infarct but continued to have bicytopenia .

Example answer:
{"entities": [{"text": "splenic infarct", "type": "BiologicFunction"}, {"text": "bicytopenia", "type": "Finding"}]}

Example input:
Sentence: The pancytopenia and splenomegaly resolved completely within weeks of treatment with corticosteroids .

Example answer:
{"entities": [{"text": "pancytopenia", "type": "BiologicFunction"}, {"text": "splenomegaly", "type": "Finding"}, {"text": "resolved", "type": "Finding"}, {"text": "corticosteroids", "type": "Chemical"}]}

Example input:
Sentence: Patients with SLE - AIMF are young women with SLE and blood cytopenia who are found to have increased bone marrow reticulin on marrow biopsy .

Example answer:
{"entities": [{"text": "SLE", "type": "BiologicFunction"}, {"text": "AIMF", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "blood cytopenia", "type": "BiologicFunction"}, {"text": "bone marrow reticulin", "type": "Finding"}, {"text": "marrow biopsy", "type": "HealthCareActivity"}]}

Example input:
Sentence: The second patient was a young woman with fever , anasarca , bicytopenia and reticulin fibrosis in the marrow biopsy .

Example answer:
{"entities": [{"text": "woman", "type": "PopulationGroup"}, {"text": "fever", "type": "Finding"}, {"text": "anasarca", "type": "Finding"}, {"text": "bicytopenia", "type": "Finding"}, {"text": "reticulin fibrosis", "type": "Finding"}, {"text": "marrow biopsy", "type": "HealthCareActivity"}]}

Input:
Sentence: The first patient was a young woman who had pancytopenia , massive splenomegaly and reticulin fibrosis in the marrow biopsy .

## Item MedMentions:test:898
Example input:
Sentence: The more time spent on emphasising proper technique to prevent injuries in training , the more important players rated ' own safety ' ( τ - b = 0 .

Example answer:
{"entities": [{"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "players", "type": "PopulationGroup"}]}

Example input:
Sentence: Although a positive perception of their educational environment was found , minor corrective measures need to be implemented .

Example answer:
{"entities": [{"text": "perception", "type": "BiologicFunction"}]}

Example input:
Sentence: Injury prevention should focus on improved safety mechanisms , protective gear , safe areas for off - road vehicle use and strict laws with minimum age requirements LEVEL OF EVIDENCE : : Level IV .

Example answer:
{"entities": [{"text": "Injury prevention", "type": "HealthCareActivity"}, {"text": "safety mechanisms", "type": "HealthCareActivity"}, {"text": "strict laws", "type": "IntellectualProduct"}]}

Example input:
Sentence: 3 % ) comprised outpatients with higher education , who anticipated more benefits to safety partnerships , were more confident in their ability to contribute , and were more intent on participating .

Example answer:
{"entities": []}

Example input:
Sentence: They were more likely to prefer a personal engagement strategy , valued scientific evidence , preferred a more active approach to safety education , and advocated disclosure of errors .

Example answer:
{"entities": [{"text": "engagement", "type": "HealthCareActivity"}, {"text": "approach", "type": "SpatialConcept"}]}

Example input:
Sentence: Unintentional Injuries in Children Up to Six Years of Age and Related Parental Knowledge , Attitudes , and Behaviors in Italy To describe risk factors associated with unintentional injuries among children aged < 6 years and to examine parents ' level of knowledge , attitudes , and behaviors about pediatric injuries and related preventive measures .

Example answer:
{"entities": [{"text": "Unintentional Injuries", "type": "InjuryOrPoisoning"}, {"text": "Knowledge", "type": "IntellectualProduct"}, {"text": "Attitudes", "type": "BiologicFunction"}, {"text": "Italy", "type": "SpatialConcept"}, {"text": "risk factors", "type": "Finding"}, {"text": "unintentional injuries", "type": "InjuryOrPoisoning"}, {"text": "knowledge", "type": "IntellectualProduct"}, {"text": "attitudes", "type": "BiologicFunction"}, {"text": "injuries", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Impact of an Educational Intervention to Improve Antibiotic Prescribing for Nurse Practitioners in a Pediatric Urgent Care Center Up to 21 % of pediatric visits result in an antibiotic prescription , and a large portion of these are unnecessary .

Example answer:
{"entities": [{"text": "Educational Intervention", "type": "HealthCareActivity"}, {"text": "Improve", "type": "Finding"}, {"text": "Antibiotic", "type": "Chemical"}, {"text": "Prescribing", "type": "HealthCareActivity"}, {"text": "Nurse Practitioners", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Urgent Care Center", "type": "Organization"}, {"text": "pediatric visits", "type": "HealthCareActivity"}, {"text": "antibiotic", "type": "Chemical"}, {"text": "prescription", "type": "HealthCareActivity"}]}

Example input:
Sentence: Parents who did not believe that it is possible to prevent unintentional injuries were more likely to have had a child injured .

Example answer:
{"entities": [{"text": "unintentional injuries", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: This study highlights a clear need for public health educational programs for parents regarding prevention of unintentional injuries in children as a valuable tool to increase safety and injury prevention and to reduce risks , because the majority of such injuries occur at home .

Example answer:
{"entities": [{"text": "public health", "type": "HealthCareActivity"}, {"text": "unintentional injuries", "type": "InjuryOrPoisoning"}, {"text": "injury prevention", "type": "HealthCareActivity"}, {"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "home", "type": "SpatialConcept"}]}

Example input:
Sentence: Approximately 70 % of respondents were aware of security measures to prevent pediatric injuries , and this knowledge was more prevalent in older parents and in those with at least a college level of education compared with those with a middle school education .

Example answer:
{"entities": [{"text": "respondents", "type": "PopulationGroup"}, {"text": "aware", "type": "BiologicFunction"}, {"text": "security measures", "type": "IntellectualProduct"}, {"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "knowledge", "type": "IntellectualProduct"}]}

Input:
Sentence: The perceived utility of education about preventive measures of pediatric injuries had a mean value of 8 .

## Item MedMentions:test:920
Example input:
Sentence: The lost art of the splenorrhaphy In the case of the hemodynamically unstable child , splenorrhaphy is preferred to splenectomy to avert postsplenectomy sepsis .

Example answer:
{"entities": [{"text": "splenorrhaphy", "type": "HealthCareActivity"}, {"text": "hemodynamically unstable", "type": "BiologicFunction"}, {"text": "splenectomy", "type": "HealthCareActivity"}, {"text": "postsplenectomy", "type": "BiologicFunction"}, {"text": "sepsis", "type": "BiologicFunction"}]}

Example input:
Sentence: For the comparison proctectomy group , pooled rates of local recurrence , overall survival , and disease - free survival were 8 .

Example answer:
{"entities": [{"text": "proctectomy", "type": "HealthCareActivity"}]}

Example input:
Sentence: 9 before surgery and significantly improved to 4 . 0 at the latest follow - up .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "improved", "type": "Finding"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Two ( 3 . 5 % ) , 15 ( 25 . 9 % ) , and 41 ( 70 . 7 % ) patients having sentinel nodes underwent total gastrectomy , proximal gastrectomy ( PG ) , and distal gastrectomy ( DG ) , respectively , in the SNM group .

Example answer:
{"entities": [{"text": "sentinel nodes", "type": "AnatomicalStructure"}, {"text": "gastrectomy", "type": "HealthCareActivity"}, {"text": "proximal gastrectomy", "type": "HealthCareActivity"}, {"text": "PG", "type": "HealthCareActivity"}, {"text": "distal gastrectomy", "type": "HealthCareActivity"}, {"text": "DG", "type": "HealthCareActivity"}, {"text": "SNM", "type": "HealthCareActivity"}]}

Example input:
Sentence: The total number of reoperations was 43 , with a total of 63 individual procedures performed . Forty - four percent ( n = 28 ) of the procedures were graft removals , 40 % ( n = 25 ) were pelvic organ prolapse surgeries ( only native tissue repairs ) , and 16 % ( n = 10 ) were stress incontinence surgeries .

Example answer:
{"entities": [{"text": "reoperations", "type": "HealthCareActivity"}, {"text": "procedures", "type": "HealthCareActivity"}, {"text": "graft", "type": "AnatomicalStructure"}, {"text": "removals", "type": "HealthCareActivity"}, {"text": "pelvic organ prolapse", "type": "BiologicFunction"}, {"text": "surgeries", "type": "HealthCareActivity"}, {"text": "tissue repairs", "type": "BiologicFunction"}, {"text": "stress", "type": "Finding"}, {"text": "incontinence surgeries", "type": "HealthCareActivity"}]}

Example input:
Sentence: The principal indications for surgery were inguinal ( 62 ) and umbilical ( 47 ) hernias .

Example answer:
{"entities": [{"text": "surgery", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "inguinal", "type": "AnatomicalStructure"}, {"text": "umbilical ( 47 ) hernias", "type": "BiologicFunction"}]}

Example input:
Sentence: 2 . 1 % underwent a splenectomy and 0 . 8 % underwent a splenorrhaphy .

Example answer:
{"entities": [{"text": "splenectomy", "type": "HealthCareActivity"}, {"text": "splenorrhaphy", "type": "HealthCareActivity"}]}

Example input:
Sentence: We sought to determine how many splenectomies or splenorrhaphies for trauma the average pediatric surgeon can be expected to perform during their career .

Example answer:
{"entities": [{"text": "splenectomies", "type": "HealthCareActivity"}, {"text": "splenorrhaphies", "type": "HealthCareActivity"}, {"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "pediatric surgeon", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: 0 % ) patients and maxillectomies in six ( 40 .

Example answer:
{"entities": [{"text": "maxillectomies", "type": "HealthCareActivity"}]}

Example input:
Sentence: If these rates remain constant over time , the average surgeon would perform 1 . 8 ( SD = 1 . 7 ) splenectomies and 0 . 6 ( SD = 1 . 1 ) splenorrhaphies for trauma over a 30 - year surgical career .

Example answer:
{"entities": [{"text": "surgeon", "type": "ProfessionalOrOccupationalGroup"}, {"text": "splenectomies", "type": "HealthCareActivity"}, {"text": "splenorrhaphies", "type": "HealthCareActivity"}, {"text": "trauma", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: 6 ) splenectomies and 0 .

## Item MedMentions:test:665
Example input:
Sentence: The ratio of phospho - Akt to Akt and mRNA expression of vascular endothelial growth factor measured in the ischemic border zone were higher in group 2 .

Example answer:
{"entities": [{"text": "phospho - Akt", "type": "Chemical"}, {"text": "Akt", "type": "Chemical"}, {"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "vascular endothelial growth factor", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Clinical and angiographic correlation of high - sensitivity C - reactive protein with acute ST elevation myocardial infarction Vascular inflammation and associated ongoing inflammatory responses are considered as the critical culprits in the pathogenesis of acute atherothrombotic events such as acute coronary syndrome ( ACS ) and myocardial infarction ( MI ) .

Example answer:
{"entities": [{"text": "angiographic", "type": "HealthCareActivity"}, {"text": "high - sensitivity C - reactive protein", "type": "Chemical"}, {"text": "acute ST elevation myocardial infarction", "type": "BiologicFunction"}, {"text": "Vascular inflammation", "type": "BiologicFunction"}, {"text": "inflammatory responses", "type": "BiologicFunction"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "atherothrombotic", "type": "AnatomicalStructure"}, {"text": "acute coronary syndrome", "type": "BiologicFunction"}, {"text": "ACS", "type": "BiologicFunction"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "MI", "type": "BiologicFunction"}]}

Example input:
Sentence: Intramyocardial Injection of siRNAs Can Efficiently Establish Myocardial Tissue -Specific Renalase Knockdown Mouse Model Ischaemia / reperfusion ( I / R ) injury will cause additional death of cardiomyocytes in ischaemic heart disease .

Example answer:
{"entities": [{"text": "Intramyocardial", "type": "SpatialConcept"}, {"text": "Injection", "type": "HealthCareActivity"}, {"text": "siRNAs", "type": "Chemical"}, {"text": "Myocardial Tissue", "type": "AnatomicalStructure"}, {"text": "Renalase", "type": "AnatomicalStructure"}, {"text": "Knockdown", "type": "ResearchActivity"}, {"text": "Mouse Model", "type": "BiologicFunction"}, {"text": "Ischaemia / reperfusion ( I / R ) injury", "type": "InjuryOrPoisoning"}, {"text": "death", "type": "BiologicFunction"}, {"text": "cardiomyocytes", "type": "AnatomicalStructure"}, {"text": "ischaemic heart disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Other changes included ischemic myopathy , focal intracellular calcium accumulation within myofibers , and calcium deposits in endomysial capillaries associated with marked complement activation and C5b9 formation .

Example answer:
{"entities": [{"text": "ischemic myopathy", "type": "BiologicFunction"}, {"text": "focal intracellular", "type": "SpatialConcept"}, {"text": "myofibers", "type": "AnatomicalStructure"}, {"text": "endomysial capillaries", "type": "AnatomicalStructure"}, {"text": "complement activation", "type": "BiologicFunction"}, {"text": "C5b9", "type": "Chemical"}]}

Example input:
Sentence: Relation of Left Ventricular Mass and Infarct Size in Anterior Wall ST - Segment Elevation Acute Myocardial Infarction ( from the EMBRACE STEMI Clinical Trial ) Biomarker measures of infarct size and myocardial salvage index ( MSI ) are important surrogate measures of clinical outcomes after a myocardial infarction .

Example answer:
{"entities": [{"text": "Left Ventricular Mass", "type": "Finding"}, {"text": "Infarct Size", "type": "BiologicFunction"}, {"text": "Anterior Wall ST - Segment Elevation Acute Myocardial Infarction", "type": "BiologicFunction"}, {"text": "STEMI", "type": "BiologicFunction"}, {"text": "Clinical Trial", "type": "ResearchActivity"}, {"text": "Biomarker", "type": "ClinicalAttribute"}, {"text": "infarct size", "type": "BiologicFunction"}, {"text": "myocardial infarction", "type": "BiologicFunction"}]}

Example input:
Sentence: Circulating progenitor cells and coronary microvascular dysfunction : Results from the NHLBI -sponsored Women 's Ischemia Syndrome Evaluation - Coronary Vascular Dysfunction Study ( WISE - CVD ) Ischemia stimulates a reparative response resulting in mobilization of circulating progenitor cells ( CPCs ) .

Example answer:
{"entities": [{"text": "Circulating progenitor cells", "type": "AnatomicalStructure"}, {"text": "coronary microvascular dysfunction", "type": "BiologicFunction"}, {"text": "NHLBI", "type": "Organization"}, {"text": "Women 's", "type": "PopulationGroup"}, {"text": "Ischemia Syndrome", "type": "BiologicFunction"}, {"text": "Evaluation", "type": "HealthCareActivity"}, {"text": "Coronary Vascular Dysfunction", "type": "BiologicFunction"}, {"text": "Study", "type": "ResearchActivity"}, {"text": "WISE - CVD", "type": "Finding"}, {"text": "Ischemia", "type": "BiologicFunction"}, {"text": "stimulates", "type": "Finding"}, {"text": "circulating progenitor cells", "type": "AnatomicalStructure"}, {"text": "CPCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: • A novel hypothesis and method is introduced to pathophysiologically characterise myocardial ischemia .

Example answer:
{"entities": [{"text": "method", "type": "IntellectualProduct"}, {"text": "myocardial ischemia", "type": "BiologicFunction"}]}

Example input:
Sentence: • Fractal analysis may characterise pathomechanical composition and severity of myocardial ischemia .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "myocardial ischemia", "type": "BiologicFunction"}]}

Example input:
Sentence: • The ischemic transition region appears a meaningful diagnostic target in perfusion imaging .

Example answer:
{"entities": [{"text": "ischemic", "type": "BiologicFunction"}, {"text": "region", "type": "SpatialConcept"}, {"text": "perfusion imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: Fractal analysis of the ischemic transition region in chronic ischemic heart disease using magnetic resonance imaging To introduce a novel hypothesis and method to characterise pathomechanisms underlying myocardial ischemia in chronic ischemic heart disease by local fractal analysis ( FA ) of the ischemic myocardial transition region in perfusion imaging .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "chronic ischemic heart disease", "type": "BiologicFunction"}, {"text": "magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "pathomechanisms", "type": "BiologicFunction"}, {"text": "myocardial ischemia", "type": "BiologicFunction"}, {"text": "FA", "type": "ResearchActivity"}, {"text": "myocardial", "type": "SpatialConcept"}, {"text": "perfusion imaging", "type": "HealthCareActivity"}]}

Input:
Sentence: The ischemic transition region may provide information on pathomechanical composition and severity of myocardial ischemia .

## Item MedMentions:test:964
Example input:
Sentence: 3 ± 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 . 21 ± 1 . 69 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 6 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 2 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 ± 31 .

Example answer:
{"entities": []}

Example input:
Sentence: 0 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 0 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 5 . 1 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 . 9 ± 1 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 ± 3 .

Example answer:
{"entities": []}

Input:
Sentence: 3 ± 1 .

## Item MedMentions:test:877
Example input:
Sentence: Receiver operator characteristic ( ROC ) curves were used to evaluate the diagnostic accuracy of D - RSBI and RSBI .

Example answer:
{"entities": [{"text": "D", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Sample volume was modified for DBS and saliva , and an ROC curve was used for cut - off determination in saliva .

Example answer:
{"entities": [{"text": "Sample volume", "type": "Finding"}, {"text": "DBS", "type": "BodySubstance"}, {"text": "saliva", "type": "BodySubstance"}, {"text": "determination", "type": "HealthCareActivity"}]}

Example input:
Sentence: ROC analysis demonstrated that the ROC area of the Hangzhou criteria & PLR method was 0 .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "Hangzhou criteria", "type": "IntellectualProduct"}, {"text": "PLR", "type": "HealthCareActivity"}]}

Example input:
Sentence: 325 was identified using ROC curve analysis for frail status .Sixty - patients ( frail : 18 , non - frail : 42 ) were enrolled in the validation cohort .

Example answer:
{"entities": [{"text": "frail", "type": "Finding"}, {"text": "non - frail", "type": "Finding"}, {"text": "enrolled", "type": "HealthCareActivity"}, {"text": "validation", "type": "ResearchActivity"}, {"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: The area under the ROC curve was used to assess the discriminatory capacity of formulas between high - intake salt individuals from low - intake individuals , taking the arbitrary values 3000 and 3900 mg / day for , respectively , Na and K intake .

Example answer:
{"entities": [{"text": "formulas", "type": "IntellectualProduct"}, {"text": "salt", "type": "Chemical"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "Na", "type": "Chemical"}, {"text": "K", "type": "Chemical"}]}

Example input:
Sentence: ROC curve analysis showed an excellent accuracy ( 89 % ) of the cFFR cut - off of ≤0 .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "cFFR", "type": "ClinicalAttribute"}]}

Example input:
Sentence: ROC curve analyses were used to evaluate the optimal cut - off point of skinfold thickness for overweight and obesity , based on the International Obesity Task Force definitions .

Example answer:
{"entities": [{"text": "analyses", "type": "ResearchActivity"}, {"text": "skinfold thickness", "type": "HealthCareActivity"}, {"text": "overweight", "type": "Finding"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "International Obesity Task Force definitions", "type": "IntellectualProduct"}]}

Example input:
Sentence: The areas under the ROC curves for D - RSBI and RSBI were 0 . 89 and 0 . 72 , respectively ( P = 0 . 006 ) .

Example answer:
{"entities": [{"text": "areas", "type": "SpatialConcept"}, {"text": "D", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The area under the ROC curve was 0 .

Example answer:
{"entities": []}

Example input:
Sentence: We calculated the receiver operating characteristic ( ROC ) curves for the PSA levels , % PSA , internal organ fat and IGF - 1 and PSA density .

Example answer:
{"entities": [{"text": "PSA levels", "type": "Finding"}, {"text": "PSA", "type": "Chemical"}, {"text": "internal organ fat", "type": "ClinicalAttribute"}, {"text": "IGF - 1", "type": "Chemical"}]}

Input:
Sentence: The ROC curve showed an area under the curve for IGF - 1 and PSA of .82 and .81 , respectively .

## Item MedMentions:test:565
Example input:
Sentence: ISX - 9 can potentiate cell proliferation and neuronal commitment in the rat dentate gyrus Adult hippocampal neurogenesis can be modulated by various physiological and pathological conditions , including stress , affective disorders , and several neurological conditions .

Example answer:
{"entities": [{"text": "ISX - 9", "type": "Chemical"}, {"text": "cell proliferation", "type": "BiologicFunction"}, {"text": "neuronal", "type": "AnatomicalStructure"}, {"text": "commitment", "type": "BiologicFunction"}, {"text": "rat", "type": "Eukaryote"}, {"text": "dentate gyrus", "type": "AnatomicalStructure"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "neurogenesis", "type": "BiologicFunction"}, {"text": "modulated", "type": "SpatialConcept"}, {"text": "pathological conditions", "type": "BiologicFunction"}, {"text": "stress", "type": "Finding"}, {"text": "affective disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: Fyn regulates multipolar - bipolar transition and neurite morphogenesis of migrating neurons in the developing neocortex Fyn is a non - receptor protein tyrosine kinase that belongs to Src family kinases .

Example answer:
{"entities": [{"text": "Fyn", "type": "Chemical"}, {"text": "bipolar", "type": "SpatialConcept"}, {"text": "neurite morphogenesis", "type": "BiologicFunction"}, {"text": "migrating neurons", "type": "BiologicFunction"}, {"text": "developing neocortex", "type": "BiologicFunction"}, {"text": "non - receptor", "type": "Finding"}, {"text": "protein tyrosine kinase", "type": "Chemical"}, {"text": "Src family kinases", "type": "Chemical"}]}

Example input:
Sentence: Yet , no studies have examined NPCs from the early postnatal Fragile X mouse hippocampus despite the importance of this developmental time point , which marks the highest expression level of FMRP , the protein missing in Fragile X , in the rodent hippocampus and is when hippocampal NPCs have migrated to the dentate gyrus ( DG ) to give rise to lifelong neurogenesis .

Example answer:
{"entities": [{"text": "no", "type": "Finding"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "NPCs", "type": "AnatomicalStructure"}, {"text": "Fragile X", "type": "BiologicFunction"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "FMRP", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}, {"text": "rodent", "type": "Eukaryote"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "dentate gyrus", "type": "AnatomicalStructure"}, {"text": "DG", "type": "AnatomicalStructure"}, {"text": "neurogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: We report that Frizzled9 ( FZD9 ) , a Wnt receptor related to Williams ' syndrome , is localized in the postsynaptic region , where it interacts with Wnt - 5a .

Example answer:
{"entities": [{"text": "Frizzled9", "type": "Chemical"}, {"text": "FZD9", "type": "Chemical"}, {"text": "Wnt", "type": "Chemical"}, {"text": "receptor", "type": "Chemical"}, {"text": "Williams ' syndrome", "type": "BiologicFunction"}, {"text": "interacts", "type": "BiologicFunction"}, {"text": "Wnt - 5a", "type": "Chemical"}]}

Example input:
Sentence: In particular , the activation of Gαo appears to be a key factor controlling the Wnt - 5a - induced dendritic spine density .

Example answer:
{"entities": [{"text": "Gαo", "type": "Chemical"}, {"text": "Wnt - 5a", "type": "Chemical"}, {"text": "dendritic spine density", "type": "AnatomicalStructure"}]}

Example input:
Sentence: FZD9 forms a pre - coupled complex with Gαo under basal conditions that dissociates after Wnt - 5a stimulation .

Example answer:
{"entities": [{"text": "FZD9", "type": "Chemical"}, {"text": "pre - coupled complex", "type": "AnatomicalStructure"}, {"text": "Gαo", "type": "Chemical"}, {"text": "dissociates", "type": "BiologicFunction"}, {"text": "Wnt - 5a", "type": "Chemical"}, {"text": "stimulation", "type": "BiologicFunction"}]}

Example input:
Sentence: Accordingly , we found that G - protein inhibition abrogates Wnt - 5a -dependent pathway in hippocampal neurons .

Example answer:
{"entities": [{"text": "G - protein inhibition abrogates", "type": "BiologicFunction"}, {"text": "Wnt - 5a", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Additionally , we studied the role of heterotrimeric G proteins in Wnt - 5a -dependent synaptic development .

Example answer:
{"entities": [{"text": "heterotrimeric G proteins", "type": "Chemical"}, {"text": "Wnt - 5a", "type": "Chemical"}, {"text": "synaptic", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Wnt - 5a / Frizzled9 receptor signaling through the Gαo / Gβγ complex regulates dendritic spine formation Wnt ligands play crucial roles in the development and regulation of synapse structure and function .

Example answer:
{"entities": [{"text": "Wnt - 5a", "type": "Chemical"}, {"text": "Frizzled9", "type": "Chemical"}, {"text": "receptor signaling", "type": "BiologicFunction"}, {"text": "Gαo", "type": "Chemical"}, {"text": "Gβγ complex", "type": "Chemical"}, {"text": "regulates", "type": "BiologicFunction"}, {"text": "dendritic spine", "type": "AnatomicalStructure"}, {"text": "formation", "type": "BiologicFunction"}, {"text": "Wnt ligands", "type": "Chemical"}, {"text": "regulation of synapse structure and function", "type": "BiologicFunction"}]}

Example input:
Sentence: Functionally , FZD9 is required for the Wnt - 5a -mediated increase in dendritic spine density .

Example answer:
{"entities": [{"text": "FZD9", "type": "Chemical"}, {"text": "Wnt - 5a", "type": "Chemical"}, {"text": "dendritic spine density", "type": "AnatomicalStructure"}]}

Input:
Sentence: Our findings reveal that FZD9 and heterotrimeric G proteins regulate Wnt - 5a signaling and dendritic spines in cultured hippocampal neurons .

## Item MedMentions:test:706
Example input:
Sentence: TEE findings changed management ( initiation of anticoagulation therapy , administration of IV antibiotic therapy , and patent foramen ovale closure ) in 10 ( 16 % [ 95 % CI : 9 % - 28 % ] ) patients .

Example answer:
{"entities": [{"text": "TEE", "type": "HealthCareActivity"}, {"text": "findings", "type": "Finding"}, {"text": "anticoagulation therapy", "type": "HealthCareActivity"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "IV antibiotic therapy", "type": "HealthCareActivity"}, {"text": "patent foramen ovale closure", "type": "HealthCareActivity"}]}

Example input:
Sentence: Anticholinergic premedication to prevent bradycardia in combined spinal anesthesia and dexmedetomidine sedation : a randomized , double - blind , placebo - controlled study When dexmedetomidine is used in patients undergoing spinal anesthesia , high incidence of bradycardia in response to parasympathetic activation is reported .

Example answer:
{"entities": [{"text": "Anticholinergic", "type": "Chemical"}, {"text": "premedication", "type": "HealthCareActivity"}, {"text": "bradycardia", "type": "BiologicFunction"}, {"text": "spinal anesthesia", "type": "HealthCareActivity"}, {"text": "dexmedetomidine", "type": "Chemical"}, {"text": "sedation", "type": "HealthCareActivity"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "double - blind", "type": "ResearchActivity"}, {"text": "parasympathetic", "type": "BodySystem"}]}

Example input:
Sentence: showed the importance of playing during hospitalization , of a friendly and caring approach and providing explanations regarding the performed procedures .

Example answer:
{"entities": [{"text": "hospitalization", "type": "HealthCareActivity"}, {"text": "explanations", "type": "IntellectualProduct"}, {"text": "procedures", "type": "HealthCareActivity"}]}

Example input:
Sentence: , the choice and number of antiseizure drugs [ ASDs ] ) in therapeutic hypothermia - treated neonates with HI from 2007 to 2015 in the Johns Hopkins Hospital Neonatal Intensive Care Unit . During this period , 3 different EEG monitoring protocols were utilized : Period 1 ( 2007 - 2009 ) , single , brief conventional EEG ( 1 h duration ) at a variable time during therapeutic hypothermia treatment , i .

Example answer:
{"entities": [{"text": "antiseizure drugs", "type": "Chemical"}, {"text": "ASDs", "type": "Chemical"}, {"text": "hypothermia - treated", "type": "HealthCareActivity"}, {"text": "HI", "type": "BiologicFunction"}, {"text": "Johns Hopkins Hospital Neonatal Intensive Care Unit", "type": "Organization"}, {"text": "EEG", "type": "Finding"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "protocols", "type": "HealthCareActivity"}, {"text": "EEG", "type": "HealthCareActivity"}, {"text": "hypothermia treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the patients treated with MVD , RF , and SRS , the average number of procedures per patient necessary to achieve pain control was 1 .

Example answer:
{"entities": [{"text": "MVD", "type": "HealthCareActivity"}, {"text": "RF", "type": "HealthCareActivity"}, {"text": "SRS", "type": "HealthCareActivity"}, {"text": "procedures", "type": "HealthCareActivity"}, {"text": "pain control", "type": "HealthCareActivity"}]}

Example input:
Sentence: The primary clinical endpoint will be the total number of inpatient hospital days ( including the index admission ) for venous thromboembolic or bleeding - related events during the first 30 days after randomization .

Example answer:
{"entities": [{"text": "clinical endpoint", "type": "ClinicalAttribute"}, {"text": "hospital", "type": "Organization"}, {"text": "admission", "type": "HealthCareActivity"}, {"text": "venous thromboembolic", "type": "BiologicFunction"}, {"text": "bleeding - related events", "type": "BiologicFunction"}, {"text": "randomization", "type": "ResearchActivity"}]}

Example input:
Sentence: The principal indications for surgery were inguinal ( 62 ) and umbilical ( 47 ) hernias .

Example answer:
{"entities": [{"text": "surgery", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "inguinal", "type": "AnatomicalStructure"}, {"text": "umbilical ( 47 ) hernias", "type": "BiologicFunction"}]}

Example input:
Sentence: It appears that using a progressive head - elevation protocol within the first 3 hours after diagnostic angiography is not associated with an increased risk of bleeding complications at the access site and warrants further exploration in the mitigation of back pain associated with prolonged supine bed rest .

Example answer:
{"entities": [{"text": "head", "type": "SpatialConcept"}, {"text": "elevation protocol", "type": "HealthCareActivity"}, {"text": "angiography", "type": "HealthCareActivity"}, {"text": "bleeding", "type": "BiologicFunction"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "access site", "type": "SpatialConcept"}, {"text": "back pain", "type": "Finding"}, {"text": "supine", "type": "SpatialConcept"}, {"text": "bed rest", "type": "HealthCareActivity"}]}

Example input:
Sentence: The most common indications for antimicrobial use were antimicrobial prophylaxis ( 28 .

Example answer:
{"entities": [{"text": "antimicrobial", "type": "Chemical"}, {"text": "prophylaxis", "type": "HealthCareActivity"}]}

Example input:
Sentence: The pediatric hospitalist added pain medication to the original postoperative orders placed by the orthopaedics team in 44 percent of patients ( 14 of the 32 ) either for breakthrough pain or better long - term coverage .

Example answer:
{"entities": [{"text": "hospitalist", "type": "ProfessionalOrOccupationalGroup"}, {"text": "postoperative orders", "type": "HealthCareActivity"}, {"text": "orthopaedics team", "type": "ProfessionalOrOccupationalGroup"}, {"text": "breakthrough pain", "type": "Finding"}]}

Input:
Sentence: Indications for hospitalization included pain control , antibiotic infusion , and need for neurovascular monitoring .

## Item MedMentions:test:755
Example input:
Sentence: However , gastrocnemius and biceps femoris activity increased as the decline angle increased above 15 degrees .

Example answer:
{"entities": [{"text": "gastrocnemius", "type": "AnatomicalStructure"}, {"text": "biceps femoris", "type": "AnatomicalStructure"}, {"text": "angle", "type": "SpatialConcept"}]}

Example input:
Sentence: 3 . Also , ANXA1 was decreased in the bEnd .

Example answer:
{"entities": [{"text": "3 .", "type": "AnatomicalStructure"}, {"text": "ANXA1", "type": "Chemical"}, {"text": "bEnd .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The former and latter spaces were involved in 79 . 2 % ( 137 / 173 ) and 13 .

Example answer:
{"entities": [{"text": "spaces", "type": "SpatialConcept"}]}

Example input:
Sentence: The high - risk group showed decreased fractional anisotropy ( FA ) , a measure of water diffusion directionality , and increased radial diffusivity in the anterior region of corpus callosum compared to the low - risk group .

Example answer:
{"entities": [{"text": "high - risk group", "type": "PopulationGroup"}, {"text": "fractional anisotropy", "type": "HealthCareActivity"}, {"text": "FA", "type": "HealthCareActivity"}, {"text": "water", "type": "Chemical"}, {"text": "anterior region of corpus callosum", "type": "AnatomicalStructure"}, {"text": "low - risk group", "type": "PopulationGroup"}]}

Example input:
Sentence: For the 50 - 60 % peak gas levels , individuals showed statistically significant reductions in responsiveness compared to rest , and across the group CS and CCS increased by 39 and 42 % , respectively , while CCSd was found to decrease by 398 % .

Example answer:
{"entities": [{"text": "individuals", "type": "PopulationGroup"}, {"text": "reductions", "type": "HealthCareActivity"}, {"text": "group", "type": "PopulationGroup"}, {"text": "CS", "type": "IntellectualProduct"}, {"text": "CCS", "type": "IntellectualProduct"}, {"text": "CCSd", "type": "IntellectualProduct"}]}

Example input:
Sentence: Cross - sectional area ( CSA ) , elongation , and force during isometric contractions were used to estimate the morphological , mechanical and material properties of the ATs bilaterally .

Example answer:
{"entities": [{"text": "Cross - sectional area", "type": "SpatialConcept"}, {"text": "CSA", "type": "SpatialConcept"}, {"text": "isometric contractions", "type": "BiologicFunction"}, {"text": "morphological", "type": "SpatialConcept"}, {"text": "ATs", "type": "AnatomicalStructure"}, {"text": "bilaterally", "type": "SpatialConcept"}]}

Example input:
Sentence: Relative to the corresponding centre zone , the outermost zones of the 1200 - mm and flat settings showed a decrease of 8 % - 37 % in legibility , whereas those of the flat setting showed an increase of 26 % - 45 % in perceived visual fatigue .

Example answer:
{"entities": [{"text": "centre", "type": "SpatialConcept"}, {"text": "zone", "type": "SpatialConcept"}, {"text": "zones", "type": "SpatialConcept"}, {"text": "flat", "type": "SpatialConcept"}, {"text": "settings", "type": "SpatialConcept"}, {"text": "setting", "type": "SpatialConcept"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "visual fatigue", "type": "BiologicFunction"}]}

Example input:
Sentence: Mean reduction was seen in up to 39 and 60 % in the cystic cavity size and increase in the mean density up to 59 and 90 .

Example answer:
{"entities": [{"text": "reduction", "type": "HealthCareActivity"}, {"text": "cavity", "type": "AnatomicalStructure"}, {"text": "size", "type": "SpatialConcept"}]}

Example input:
Sentence: Analysis showed a 75 . 4 % prevalence rate of a single anechoic space .

Example answer:
{"entities": [{"text": "Analysis", "type": "ResearchActivity"}, {"text": "anechoic space", "type": "SpatialConcept"}]}

Example input:
Sentence: Cross - sectional area ( CSA ) , perimeter and position of anechoic space relative to median nerve were recorded .

Example answer:
{"entities": [{"text": "Cross - sectional area", "type": "SpatialConcept"}, {"text": "CSA", "type": "SpatialConcept"}, {"text": "position", "type": "SpatialConcept"}, {"text": "anechoic space", "type": "SpatialConcept"}, {"text": "median nerve", "type": "AnatomicalStructure"}]}

Input:
Sentence: 89 . 1 % had a decrease in CSA and perimeter of anechoic space from Position A to B while 10 .

## Item MedMentions:test:259
Example input:
Sentence: We first developed a panel of new physiologic models for study of PDAC , expanding surgical PDAC tumor samples in culture using short - term culture and conditional reprogramming with the Rho kinase inhibitor Y - 27632 , and creating matched patient - derived xenografts ( PDX ) .

Example answer:
{"entities": [{"text": "models", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "PDAC", "type": "BiologicFunction"}, {"text": "tumor samples", "type": "AnatomicalStructure"}, {"text": "culture", "type": "HealthCareActivity"}, {"text": "Rho kinase", "type": "Chemical"}, {"text": "inhibitor", "type": "Chemical"}, {"text": "Y - 27632", "type": "Chemical"}, {"text": "patient - derived xenografts", "type": "Chemical"}, {"text": "PDX", "type": "Chemical"}]}

Example input:
Sentence: Phosphodiesterase type 5 inhibitors : Irrational use in Saudi Arabia To identify the criteria of phosphodiesterase type 5 inhibitor ( PDE5i ) users and to analyse the knowledge , attitude , and practices of PDE5i use amongst Saudi men .

Example answer:
{"entities": [{"text": "Phosphodiesterase type 5 inhibitors", "type": "Chemical"}, {"text": "Irrational", "type": "Finding"}, {"text": "Saudi Arabia", "type": "SpatialConcept"}, {"text": "identify", "type": "BiologicFunction"}, {"text": "phosphodiesterase type 5 inhibitor", "type": "Chemical"}, {"text": "PDE5i", "type": "Chemical"}, {"text": "users", "type": "PopulationGroup"}, {"text": "analyse", "type": "ResearchActivity"}, {"text": "knowledge", "type": "IntellectualProduct"}, {"text": "attitude", "type": "BiologicFunction"}, {"text": "practices", "type": "BiologicFunction"}]}

Example input:
Sentence: Such inhibitors have therapeutic potential for treating malignant melanoma , since high levels of S100B downregulate wild - type p53 tumor suppressor function in this cancer .

Example answer:
{"entities": [{"text": "inhibitors", "type": "Chemical"}, {"text": "malignant melanoma", "type": "BiologicFunction"}, {"text": "S100B", "type": "Chemical"}, {"text": "downregulate", "type": "BiologicFunction"}, {"text": "wild - type p53", "type": "Chemical"}, {"text": "tumor suppressor function", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Inhibition of programmed cell death protein 1 and / or its specific ligand programmed death - ligand 1 ( PD - L1 ) was effective in clinical trials in advanced melanoma , non - small cell lung cancer ( NSCLC ) bladder and kidney cancer .

Example answer:
{"entities": [{"text": "programmed cell death protein 1", "type": "Chemical"}, {"text": "ligand", "type": "Chemical"}, {"text": "clinical trials", "type": "ResearchActivity"}, {"text": "melanoma", "type": "BiologicFunction"}, {"text": "non - small cell lung cancer", "type": "BiologicFunction"}, {"text": "NSCLC", "type": "BiologicFunction"}, {"text": "bladder", "type": "BiologicFunction"}, {"text": "kidney cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: In a post hoc analysis , there was strong evidence that solar keratosis was associated with future PDE5 inhibitor use ( odds ratio = 1 . 28 , 95 % CI 1 .

Example answer:
{"entities": [{"text": "post hoc analysis", "type": "ResearchActivity"}, {"text": "solar keratosis", "type": "BiologicFunction"}, {"text": "PDE5 inhibitor", "type": "Chemical"}]}

Example input:
Sentence: 23 - 1 . 34 , p < 0 . 001 ) , suggesting that men with higher sun exposure were more likely to become PDE5 inhibitor users .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "sun exposure", "type": "Finding"}, {"text": "PDE5 inhibitor", "type": "Chemical"}, {"text": "users", "type": "PopulationGroup"}]}

Example input:
Sentence: Ever use of a PDE5 inhibitor and time - updated cumulative number of PDE5 inhibitor prescriptions were investigated as exposures , and the primary outcome was malignant melanoma .

Example answer:
{"entities": [{"text": "PDE5 inhibitor", "type": "Chemical"}, {"text": "prescriptions", "type": "IntellectualProduct"}, {"text": "malignant melanoma", "type": "BiologicFunction"}]}

Example input:
Sentence: After adjusting for potential confounders , there was weak evidence of a small positive association between PDE5 inhibitor use and melanoma risk ( HR = 1 . 14 , 95 % CI 1 .

Example answer:
{"entities": [{"text": "PDE5 inhibitor", "type": "Chemical"}, {"text": "melanoma", "type": "BiologicFunction"}]}

Example input:
Sentence: Our results were not consistent with PDE5 inhibitors being causally associated with melanoma risk , and strongly suggest that observed risk increases are driven by greater sun exposure among patients exposed to a PDE5 inhibitor .

Example answer:
{"entities": [{"text": "PDE5 inhibitors", "type": "Chemical"}, {"text": "melanoma", "type": "BiologicFunction"}, {"text": "sun exposure", "type": "Finding"}, {"text": "PDE5 inhibitor", "type": "Chemical"}]}

Example input:
Sentence: We therefore aimed to investigate whether PDE5 inhibitor use is associated with an increased risk of malignant melanoma , and whether any increase in risk is likely to represent a causal relationship .

Example answer:
{"entities": [{"text": "PDE5 inhibitor", "type": "Chemical"}, {"text": "malignant melanoma", "type": "BiologicFunction"}]}

Input:
Sentence: Phosphodiesterase Type 5 Inhibitors and Risk of Malignant Melanoma : Matched Cohort Study Using Primary Care Data from the UK Clinical Practice Research Datalink Laboratory evidence suggests that reduced phosphodiesterase type 5 ( PDE5 ) expression increases the invasiveness of melanoma cells ; hence , pharmacological inhibition of PDE5 could affect melanoma risk .

## Item MedMentions:test:921
Example input:
Sentence: The efficacy of remote monitoring was evaluated by recording compliance to transmissions , number of device alerts requiring intervention and time from transmission to review .

Example answer:
{"entities": [{"text": "remote", "type": "SpatialConcept"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "compliance", "type": "Finding"}, {"text": "device", "type": "MedicalDevice"}, {"text": "intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: This study evaluated the impact of ENGAGE on frontline service providers ' self - reported knowledge , skills , capacity and practice up to 5 - months post training .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "ENGAGE", "type": "Organization"}, {"text": "self - reported knowledge", "type": "Finding"}]}

Example input:
Sentence: School engagement is measured as student attitudes to school ( cognitive and emotional ) and suspension rates ( behavioural ) .

Example answer:
{"entities": [{"text": "school", "type": "Organization"}, {"text": "cognitive", "type": "BiologicFunction"}, {"text": "emotional", "type": "BiologicFunction"}]}

Example input:
Sentence: The vast majority of service providers ( 93 . 4 % ) reported that ENGAGE had impacted their work practice up to 5 - month post training .

Example answer:
{"entities": [{"text": "reported", "type": "HealthCareActivity"}, {"text": "ENGAGE", "type": "Organization"}]}

Example input:
Sentence: The primary outcome measure by which success will be determined is participant enrollment rate ( " pass " defined as at least two participants / site / month , recognizing that enrollment may be slower during the run - in phase ) .

Example answer:
{"entities": [{"text": "participant", "type": "PopulationGroup"}, {"text": "enrollment", "type": "HealthCareActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "site", "type": "SpatialConcept"}]}

Example input:
Sentence: For each scenario , usability was measured via efficiency , recorded as time to task completion , and participants ' perceived satisfaction which were compared using Kruskal - Wallis and Mann Whitney U tests , respectively .

Example answer:
{"entities": [{"text": "recorded", "type": "IntellectualProduct"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "satisfaction", "type": "BiologicFunction"}, {"text": "Kruskal - Wallis and Mann Whitney U tests", "type": "IntellectualProduct"}]}

Example input:
Sentence: We used GCO program data , website metrics , and provincial STI clinic records to describe temporal trends , progression through the service pathway , and demographic , risk , and testing outcomes for individuals creating GCO accounts during the first 15 months of implementation .

Example answer:
{"entities": [{"text": "GCO", "type": "IntellectualProduct"}, {"text": "website", "type": "IntellectualProduct"}, {"text": "provincial", "type": "Organization"}, {"text": "STI", "type": "BiologicFunction"}, {"text": "clinic", "type": "Organization"}, {"text": "records", "type": "IntellectualProduct"}, {"text": "individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: Other outcomes ( website acceptability , physical activity behaviour ) were assessed using online surveys .

Example answer:
{"entities": [{"text": "website", "type": "IntellectualProduct"}, {"text": "online surveys", "type": "IntellectualProduct"}]}

Example input:
Sentence: The purpose of the study is to investigate the impact of differing delivery schedules of computer - tailored physical activity modules on engagement and physical activity behaviour change in a web - based intervention targeting breast cancer survivors .

Example answer:
{"entities": [{"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Results Using the study web - based platform , we integrated recruitment , enrollment , and follow - up procedures into a digital platform that required little staff effort to implement and manage .

Example answer:
{"entities": [{"text": "enrollment", "type": "HealthCareActivity"}, {"text": "follow - up procedures", "type": "ResearchActivity"}, {"text": "staff", "type": "ProfessionalOrOccupationalGroup"}, {"text": "implement", "type": "HealthCareActivity"}]}

Input:
Sentence: Engagement with the website ( number of logins , time on site , modules viewed , action plans completed ) was measured using tracking software .

## Item MedMentions:test:741
Example input:
Sentence: salmonicida strains isolated from Chinese freshwater fish contain a novel genomic island and possible regional - specific mobile genetic elements profiles Two strains of Aeromonas salmonicida , YK and BG , were isolated from largemouth bronze gudgeon and northern whitefish in China , and identified as A .

Example answer:
{"entities": [{"text": "salmonicida", "type": "Bacterium"}, {"text": "Chinese freshwater fish", "type": "Eukaryote"}, {"text": "genomic island", "type": "Chemical"}, {"text": "mobile genetic elements", "type": "Chemical"}, {"text": "Aeromonas salmonicida", "type": "Bacterium"}, {"text": "largemouth bronze gudgeon", "type": "Eukaryote"}, {"text": "northern whitefish", "type": "Eukaryote"}, {"text": "China", "type": "SpatialConcept"}, {"text": "A .", "type": "Bacterium"}]}

Example input:
Sentence: ruckeri clones associated with Atlantic salmon but only five associated with rainbow trout ; none of the Atlantic salmon clones occurred in rainbow trout and vice versa These findings suggest that distinct subpopulations of Y .

Example answer:
{"entities": [{"text": "ruckeri", "type": "Bacterium"}, {"text": "clones", "type": "AnatomicalStructure"}, {"text": "Atlantic salmon", "type": "Eukaryote"}, {"text": "rainbow trout", "type": "Eukaryote"}, {"text": "findings", "type": "Finding"}, {"text": "subpopulations", "type": "PopulationGroup"}, {"text": "Y .", "type": "Bacterium"}]}

Example input:
Sentence: This is largely because current vaccines are aimed at rainbow trout and are based on serotypes specific for this species .

Example answer:
{"entities": [{"text": "vaccines", "type": "Chemical"}, {"text": "rainbow trout", "type": "Eukaryote"}, {"text": "serotypes", "type": "IntellectualProduct"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: Yersinia ruckeri Isolates Recovered from Diseased Atlantic Salmon ( Salmo salar ) in Scotland Are More Diverse than Those from Rainbow Trout ( Oncorhynchus mykiss ) and Represent Distinct Subpopulations Yersinia ruckeri is the etiological agent of enteric redmouth ( ERM ) disease of farmed salmonids .

Example answer:
{"entities": [{"text": "Yersinia ruckeri", "type": "Bacterium"}, {"text": "Isolates", "type": "Chemical"}, {"text": "Diseased", "type": "BiologicFunction"}, {"text": "Atlantic Salmon", "type": "Eukaryote"}, {"text": "Salmo salar", "type": "Eukaryote"}, {"text": "Scotland", "type": "SpatialConcept"}, {"text": "Rainbow Trout", "type": "Eukaryote"}, {"text": "Oncorhynchus mykiss", "type": "Eukaryote"}, {"text": "Subpopulations", "type": "PopulationGroup"}, {"text": "enteric redmouth", "type": "BiologicFunction"}, {"text": "ERM", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "salmonids", "type": "Eukaryote"}]}

Example input:
Sentence: ruckeri isolates recovered over a 14 - year period from infected Atlantic salmon in Scotland ; 26 isolates from infected rainbow trout were also characterized .

Example answer:
{"entities": [{"text": "ruckeri", "type": "Bacterium"}, {"text": "isolates", "type": "Chemical"}, {"text": "infected", "type": "Finding"}, {"text": "Atlantic salmon", "type": "Eukaryote"}, {"text": "Scotland", "type": "SpatialConcept"}, {"text": "rainbow trout", "type": "Eukaryote"}]}

Example input:
Sentence: Yersinia ruckeri isolates recovered from diseased Atlantic salmon have been poorly characterized , and very little is known about the relationship of the isolates associated with these two species .

Example answer:
{"entities": [{"text": "Yersinia ruckeri", "type": "Bacterium"}, {"text": "isolates", "type": "Chemical"}, {"text": "diseased", "type": "BiologicFunction"}, {"text": "Atlantic salmon", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: A new O serotype ( designated O8 ) was identified in 56 biotype 1 Atlantic salmon isolates and was the most common serotype identified from 2006 to 2011 and in 2014 , suggesting an increased prevalence during the time period sampled .

Example answer:
{"entities": [{"text": "O serotype", "type": "IntellectualProduct"}, {"text": "56 biotype 1", "type": "IntellectualProduct"}, {"text": "Atlantic salmon", "type": "Eukaryote"}, {"text": "isolates", "type": "Chemical"}, {"text": "serotype", "type": "IntellectualProduct"}]}

Example input:
Sentence: In addition , a new O serotype was identified that is responsible for a significant proportion of the disease in Atlantic salmon .

Example answer:
{"entities": [{"text": "O serotype", "type": "IntellectualProduct"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "Atlantic salmon", "type": "Eukaryote"}]}

Example input:
Sentence: However , the identification of two biotype 2 , serotype O8 isolates in rainbow trout suggests that vaccines containing serotypes O1 and O8 should be evaluated in both rainbow trout and Atlantic salmon for application in Scotland .

Example answer:
{"entities": [{"text": "biotype 2", "type": "IntellectualProduct"}, {"text": "serotype O8", "type": "IntellectualProduct"}, {"text": "isolates", "type": "Chemical"}, {"text": "rainbow trout", "type": "Eukaryote"}, {"text": "vaccines", "type": "Chemical"}, {"text": "serotypes O1 and O8", "type": "IntellectualProduct"}, {"text": "Atlantic salmon", "type": "Eukaryote"}, {"text": "Scotland", "type": "SpatialConcept"}]}

Example input:
Sentence: Rainbow trout isolates were represented almost exclusively by the same biotype 2 , serotype O1 clone that has been responsible for the majority of ERM outbreaks in this species within the United Kingdom since the 1980s .

Example answer:
{"entities": [{"text": "Rainbow trout", "type": "Eukaryote"}, {"text": "isolates", "type": "Chemical"}, {"text": "biotype 2", "type": "IntellectualProduct"}, {"text": "serotype O1", "type": "IntellectualProduct"}, {"text": "ERM", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "United Kingdom", "type": "SpatialConcept"}]}

Input:
Sentence: A wider range of serotypes is responsible for infection in Atlantic salmon , but very little is known about the diversity of these strains and their relationships to those recovered from rainbow trout .

## Item MedMentions:test:918
Example input:
Sentence: Biliary papillotomy / sphincterotomy should be considered especially after difficult cannulation .

Example answer:
{"entities": [{"text": "Biliary papillotomy", "type": "HealthCareActivity"}, {"text": "sphincterotomy", "type": "HealthCareActivity"}, {"text": "cannulation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Laparascopic Splenectomy Due to Splenic Injury after Colonoscopy Colonoscopy , which is routinely performed in diagnosis and treatment of colorectal disorders , is a reliable procedure .

Example answer:
{"entities": [{"text": "Laparascopic Splenectomy", "type": "HealthCareActivity"}, {"text": "Splenic Injury", "type": "InjuryOrPoisoning"}, {"text": "Colonoscopy", "type": "HealthCareActivity"}, {"text": "diagnosis", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "procedure", "type": "HealthCareActivity"}]}

Example input:
Sentence: Although splenogonadal fusion is a rare condition , surgeons should be aware of this rare disease entity to avoid unnecessary aggressive interventions such as orchiectomy .

Example answer:
{"entities": [{"text": "splenogonadal fusion", "type": "AnatomicalStructure"}, {"text": "condition", "type": "BiologicFunction"}, {"text": "surgeons", "type": "ProfessionalOrOccupationalGroup"}, {"text": "rare disease", "type": "BiologicFunction"}, {"text": "unnecessary", "type": "HealthCareActivity"}, {"text": "interventions", "type": "HealthCareActivity"}, {"text": "orchiectomy", "type": "HealthCareActivity"}]}

Example input:
Sentence: During the entirety of this modified approach , neither technically challenging operations such as intrathoracic suturing or knotting , nor special instruments such as an OrVil system or a reverse - puncture head are required .

Example answer:
{"entities": [{"text": "operations", "type": "HealthCareActivity"}, {"text": "intrathoracic suturing", "type": "HealthCareActivity"}, {"text": "knotting", "type": "HealthCareActivity"}, {"text": "instruments", "type": "MedicalDevice"}, {"text": "OrVil system", "type": "MedicalDevice"}, {"text": "reverse - puncture head", "type": "MedicalDevice"}]}

Example input:
Sentence: We sought to determine how many splenectomies or splenorrhaphies for trauma the average pediatric surgeon can be expected to perform during their career .

Example answer:
{"entities": [{"text": "splenectomies", "type": "HealthCareActivity"}, {"text": "splenorrhaphies", "type": "HealthCareActivity"}, {"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "pediatric surgeon", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: 4 ) splenorrhaphies for trauma .

Example answer:
{"entities": [{"text": "splenorrhaphies", "type": "HealthCareActivity"}, {"text": "trauma", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Nonoperative management is associated with a host of benefits , but has resulted in a decrease in the experience level of the pediatric surgeons expected to perform an emergency splenectomy or splenorrhaphy when the unusual occasion arises .

Example answer:
{"entities": [{"text": "Nonoperative management", "type": "HealthCareActivity"}, {"text": "pediatric surgeons", "type": "ProfessionalOrOccupationalGroup"}, {"text": "splenectomy", "type": "HealthCareActivity"}, {"text": "splenorrhaphy", "type": "HealthCareActivity"}]}

Example input:
Sentence: If these rates remain constant over time , the average surgeon would perform 1 . 8 ( SD = 1 . 7 ) splenectomies and 0 . 6 ( SD = 1 . 1 ) splenorrhaphies for trauma over a 30 - year surgical career .

Example answer:
{"entities": [{"text": "surgeon", "type": "ProfessionalOrOccupationalGroup"}, {"text": "splenectomies", "type": "HealthCareActivity"}, {"text": "splenorrhaphies", "type": "HealthCareActivity"}, {"text": "trauma", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: 2 . 1 % underwent a splenectomy and 0 . 8 % underwent a splenorrhaphy .

Example answer:
{"entities": [{"text": "splenectomy", "type": "HealthCareActivity"}, {"text": "splenorrhaphy", "type": "HealthCareActivity"}]}

Example input:
Sentence: The lost art of the splenorrhaphy In the case of the hemodynamically unstable child , splenorrhaphy is preferred to splenectomy to avert postsplenectomy sepsis .

Example answer:
{"entities": [{"text": "splenorrhaphy", "type": "HealthCareActivity"}, {"text": "hemodynamically unstable", "type": "BiologicFunction"}, {"text": "splenectomy", "type": "HealthCareActivity"}, {"text": "postsplenectomy", "type": "BiologicFunction"}, {"text": "sepsis", "type": "BiologicFunction"}]}

Input:
Sentence: However , successful splenorrhaphy requires familiarity with the procedure .

## Item MedMentions:test:932
Example input:
Sentence: PubMed was reviewed to identify papers published between 2010 and 2016 .

Example answer:
{"entities": [{"text": "PubMed", "type": "IntellectualProduct"}, {"text": "papers published", "type": "IntellectualProduct"}]}

Example input:
Sentence: The systematic review assessed 48 articles representing 2726 procedures .

Example answer:
{"entities": [{"text": "systematic review", "type": "IntellectualProduct"}]}

Example input:
Sentence: Review of randomised clinical trials that used a non - inferiority design published between January 2010 and May 2015 in medical journals that had an impact factor > 10 ( JAMA Internal Medicine , Archives Internal Medicine , PLOS Medicine , Annals of Internal Medicine , BMJ , JAMA , Lancet and New England Journal of Medicine ) .

Example answer:
{"entities": [{"text": "randomised", "type": "ResearchActivity"}, {"text": "clinical trials", "type": "ResearchActivity"}, {"text": "non - inferiority", "type": "Finding"}, {"text": "medical journals", "type": "IntellectualProduct"}, {"text": "JAMA Internal Medicine", "type": "IntellectualProduct"}, {"text": "Archives Internal Medicine", "type": "IntellectualProduct"}, {"text": "PLOS Medicine", "type": "IntellectualProduct"}, {"text": "Annals of Internal Medicine", "type": "IntellectualProduct"}, {"text": "BMJ", "type": "IntellectualProduct"}, {"text": "JAMA", "type": "IntellectualProduct"}, {"text": "Lancet and New England Journal of Medicine", "type": "IntellectualProduct"}]}

Example input:
Sentence: Based on a review of over 1000 published HPS and POPH articles identified via a MEDLINE search ( 1985 - 2015 ) , clinical guidelines were based on , selected single care reports , small series , registries , databases , and expert opinion .

Example answer:
{"entities": [{"text": "HPS", "type": "BiologicFunction"}, {"text": "POPH", "type": "BiologicFunction"}, {"text": "MEDLINE search", "type": "IntellectualProduct"}, {"text": "clinical guidelines", "type": "IntellectualProduct"}, {"text": "selected single care reports", "type": "HealthCareActivity"}, {"text": "registries", "type": "IntellectualProduct"}, {"text": "databases", "type": "IntellectualProduct"}]}

Example input:
Sentence: Fifty papers met eligibility criteria for review , and meta - analysis of overall results was possible in thirty - two ( 2050 participants ) .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "meta - analysis", "type": "IntellectualProduct"}, {"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: The mean number ( and standard deviation ) of clinical studies cited was significantly greater ( p = 0 . 008 ) for reviews that concluded that NSAIDs were safe ( 8 . 0 ± 4 . 8 ) compared with those that recommended avoiding them ( 2 . 1 ± 2 .

Example answer:
{"entities": [{"text": "clinical studies", "type": "ResearchActivity"}, {"text": "reviews", "type": "IntellectualProduct"}, {"text": "NSAIDs", "type": "Chemical"}]}

Example input:
Sentence: The initial search retrieved 1240 articles . Twenty - two articles were selected and used in the review .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}, {"text": "review", "type": "IntellectualProduct"}]}

Example input:
Sentence: Seven hundred thirty - one articles met the search criteria and 51 studies were initially selected .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}, {"text": "studies", "type": "HealthCareActivity"}]}

Example input:
Sentence: All human studies , including review articles , were identified for further analysis .

Example answer:
{"entities": [{"text": "human studies", "type": "ResearchActivity"}, {"text": "review articles", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Review articles were analyzed with regard to variability in the cited literature and final conclusions .

Example answer:
{"entities": [{"text": "Review articles", "type": "IntellectualProduct"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "literature", "type": "IntellectualProduct"}]}

Input:
Sentence: Review articles also demonstrated substantial variability in the number of cited clinical studies and overall conclusions .

## Item MedMentions:test:1011
Example input:
Sentence: 3±8 . 8 years .

Example answer:
{"entities": []}

Example input:
Sentence: 8 years ( range 29 - 88 years ) .

Example answer:
{"entities": []}

Example input:
Sentence: 3 years .

Example answer:
{"entities": []}

Example input:
Sentence: 9 years ) .

Example answer:
{"entities": []}

Example input:
Sentence: 9 years ) .

Example answer:
{"entities": []}

Example input:
Sentence: 5 years .

Example answer:
{"entities": []}

Example input:
Sentence: 6 years ( range , 38 - 97 years ) .

Example answer:
{"entities": []}

Example input:
Sentence: 4 years .

Example answer:
{"entities": []}

Example input:
Sentence: 9 years .

Example answer:
{"entities": []}

Example input:
Sentence: 8 years .

Example answer:
{"entities": []}

Input:
Sentence: 6 years ) .

## Item MedMentions:test:674
Example input:
Sentence: In recent years , there have been significant advances centered on in vitro test systems and bioanalytical strategies , yet a frontier challenge concerns linking observed network perturbations to phenotypes , which will require understanding pathways and networks that give rise to adverse responses .

Example answer:
{"entities": [{"text": "bioanalytical strategies", "type": "HealthCareActivity"}]}

Example input:
Sentence: Thus , integrative analysis of multiple molecular measurements , particularly acquired by omics strategies , is a key approach in Systems Toxicology .

Example answer:
{"entities": [{"text": "integrative analysis", "type": "ResearchActivity"}, {"text": "omics strategies", "type": "HealthCareActivity"}, {"text": "Toxicology", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Systems Toxicology : Real World Applications and Opportunities Systems Toxicology aims to change the basis of how adverse biological effects of xenobiotics are characterized from empirical end points to describing modes of action as adverse outcome pathways and perturbed networks .

Example answer:
{"entities": [{"text": "Toxicology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "World", "type": "PopulationGroup"}, {"text": "xenobiotics", "type": "Chemical"}]}

Example input:
Sentence: There are several novel enabling technologies , such as vesicle proteomics and chemical genomics , with great potential for dissecting secretion pathways , providing information about the cargo that travels along them and the conditions that induce them .

Example answer:
{"entities": [{"text": "enabling", "type": "BiologicFunction"}, {"text": "vesicle", "type": "AnatomicalStructure"}, {"text": "proteomics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "chemical", "type": "Chemical"}, {"text": "genomics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "secretion pathways", "type": "BiologicFunction"}]}

Example input:
Sentence: This evolving approach depends critically on data reliability and relevance , which in turn depends on the quality of experimental models and bioanalysis techniques used to generate toxicological data .

Example answer:
{"entities": [{"text": "experimental models", "type": "IntellectualProduct"}, {"text": "bioanalysis techniques", "type": "ResearchActivity"}]}

Example input:
Sentence: Systems Toxicology involves the use of large - scale data streams ( " big data " ) , such as those derived from omics measurements that require computational means for obtaining informative results .

Example answer:
{"entities": [{"text": "Toxicology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "data streams", "type": "IntellectualProduct"}, {"text": "omics measurements", "type": "ResearchActivity"}]}

Example input:
Sentence: Human cells provide a valuable tool for investigating currently unresolved issues on the cellular mechanisms of Se toxicity and metabolism .

Example answer:
{"entities": [{"text": "Human", "type": "Eukaryote"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "issues", "type": "Finding"}, {"text": "cellular", "type": "AnatomicalStructure"}, {"text": "Se", "type": "Chemical"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "metabolism", "type": "BiologicFunction"}]}

Example input:
Sentence: This proposed in silico approach is an inexpensive and rapid strategy for the detection of chemicals with estrogenic metabolites and may reduce potential false negative results from in vitro assays .

Example answer:
{"entities": [{"text": "detection", "type": "Finding"}, {"text": "chemicals", "type": "Chemical"}, {"text": "estrogenic", "type": "Chemical"}, {"text": "metabolites", "type": "Chemical"}, {"text": "false negative", "type": "Finding"}, {"text": "in vitro assays", "type": "HealthCareActivity"}]}

Example input:
Sentence: In conclusion , our data demonstrated that miRNA - mRNA networks provide a better understanding of toxicological mechanism caused by environmental pollutants in vitro using HL - 60 cells and exosomes .

Example answer:
{"entities": [{"text": "miRNA", "type": "Chemical"}, {"text": "mRNA", "type": "Chemical"}, {"text": "toxicological mechanism", "type": "BiologicFunction"}, {"text": "environmental pollutants", "type": "Chemical"}, {"text": "HL - 60 cells", "type": "AnatomicalStructure"}, {"text": "exosomes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Toward this aim , Systems Toxicology entails the integration of in vitro and in vivo toxicity data with computational modeling .

Example answer:
{"entities": [{"text": "Toxicology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: Therefore , it is imperative to build and share a database of safety information on toxicological mechanisms and pathways collected through in vivo , in vitro , and in silico methods .

## Item MedMentions:test:759
Example input:
Sentence: Altogether , our findings show that , in OS cells , short - term acidosis induces resistance to different chemotherapeutic drugs by a reversal of ΔpHcm , suggesting that buffer therapies or regimens including proton pump inhibitors in combination to low concentrations of conventional anticancer agents may offer novel solutions to overcome drug resistance .

Example answer:
{"entities": [{"text": "OS", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "acidosis", "type": "BiologicFunction"}, {"text": "chemotherapeutic drugs", "type": "Chemical"}, {"text": "buffer", "type": "Chemical"}, {"text": "therapies", "type": "HealthCareActivity"}, {"text": "regimens", "type": "IntellectualProduct"}, {"text": "proton pump inhibitors", "type": "Chemical"}, {"text": "anticancer agents", "type": "Chemical"}, {"text": "drug resistance", "type": "BiologicFunction"}]}

Example input:
Sentence: We considered the typical acidic extracellular pH ( pHe ) of sarcomas , and found that doxorubicin ( DXR ) cytotoxicity is reduced in P - gp negative OS cells cultured at pHe 6 .

Example answer:
{"entities": [{"text": "sarcomas", "type": "BiologicFunction"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DXR", "type": "Chemical"}, {"text": "cytotoxicity", "type": "BiologicFunction"}, {"text": "P - gp", "type": "AnatomicalStructure"}, {"text": "OS", "type": "BiologicFunction"}, {"text": "cells cultured", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Final results of the GIMEMA LAL 0904 study In the GIMEMA LAL 0904 protocol , adult Ph + acute lymphoblastic leukemia patients were treated with chemotherapy for induction and consolidation , followed by maintenance with imatinib .

Example answer:
{"entities": [{"text": "results", "type": "Finding"}, {"text": "GIMEMA LAL 0904 study", "type": "HealthCareActivity"}, {"text": "GIMEMA LAL 0904 protocol", "type": "IntellectualProduct"}, {"text": "Ph + acute lymphoblastic leukemia", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "induction", "type": "HealthCareActivity"}, {"text": "consolidation", "type": "HealthCareActivity"}, {"text": "imatinib", "type": "Chemical"}]}

Example input:
Sentence: A sequential approach with imatinib alone in induction , consolidated by chemotherapy plus imatinib followed by a stem cell transplant is a feasible , well - tolerated and effective strategy for adult Ph + acute lymphoblastic leukemia , leading to the best long - term survival rates so far reported .

Example answer:
{"entities": [{"text": "approach", "type": "SpatialConcept"}, {"text": "imatinib", "type": "Chemical"}, {"text": "induction", "type": "HealthCareActivity"}, {"text": "consolidated", "type": "HealthCareActivity"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "stem cell transplant", "type": "HealthCareActivity"}, {"text": "Ph + acute lymphoblastic leukemia", "type": "BiologicFunction"}, {"text": "reported", "type": "HealthCareActivity"}]}

Example input:
Sentence: Acute Ph - negative lymphoblastic leukemias in adults : Risk factors in the use of the ALL - 2009 protocol to analyze well - known risk factors ( RFs ) , such as age , immunophenotype , baseline leukocytosis , enhanced lactate dehydrogenase ( LDH ) activity , time to achieve complete remission , a risk group , and cytogenetic abnormalities ) in patients with acute lymphoblastic leukemia ( ALL ) in the use of the ALL - 2009 protocol .

Example answer:
{"entities": [{"text": "Acute Ph - negative lymphoblastic leukemias", "type": "BiologicFunction"}, {"text": "Risk factors", "type": "Finding"}, {"text": "ALL - 2009 protocol", "type": "IntellectualProduct"}, {"text": "risk factors", "type": "Finding"}, {"text": "RFs", "type": "Finding"}, {"text": "immunophenotype", "type": "HealthCareActivity"}, {"text": "leukocytosis", "type": "BiologicFunction"}, {"text": "lactate dehydrogenase", "type": "Chemical"}, {"text": "LDH", "type": "Chemical"}, {"text": "activity", "type": "BiologicFunction"}, {"text": "remission", "type": "Finding"}, {"text": "cytogenetic abnormalities", "type": "BiologicFunction"}, {"text": "acute lymphoblastic leukemia", "type": "BiologicFunction"}, {"text": "ALL", "type": "BiologicFunction"}]}

Example input:
Sentence: A sequential approach with imatinib , chemotherapy and transplant for adult Ph + acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "approach", "type": "SpatialConcept"}, {"text": "imatinib", "type": "Chemical"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "transplant", "type": "Finding"}, {"text": "Ph + acute lymphoblastic leukemia", "type": "BiologicFunction"}]}

Example input:
Sentence: The results indicated the enhanced growth and invasion of leukemic cells at pH 6 .

Example answer:
{"entities": [{"text": "growth", "type": "BiologicFunction"}, {"text": "invasion", "type": "BiologicFunction"}, {"text": "leukemic", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Extracellular acidity can influence the behavior of leukemic cells and therefore , the manipulation of extracellular liquid can be selected as a therapeutic strategy for leukemia , especially for acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "Extracellular", "type": "SpatialConcept"}, {"text": "leukemic", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "extracellular liquid", "type": "BodySubstance"}, {"text": "therapeutic strategy", "type": "HealthCareActivity"}, {"text": "leukemia", "type": "BiologicFunction"}, {"text": "acute lymphoblastic leukemia", "type": "BiologicFunction"}]}

Example input:
Sentence: The aim of this study was to investigate the effects of extracellular acidic pH on proliferation , invasion , and drug - induced apoptosis in acute lymphoblastic cells .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "extracellular", "type": "SpatialConcept"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "invasion", "type": "BiologicFunction"}, {"text": "drug", "type": "Chemical"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "acute lymphoblastic cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Investigating Effects of Acidic pH on Proliferation , Invasion and Drug - Induced Apoptosis in Lymphoblastic Leukemia Some studies have shown that extracellular pH in tumors , which results in tumor progression , is less than that in normal tissues .

Example answer:
{"entities": [{"text": "Proliferation", "type": "BiologicFunction"}, {"text": "Invasion", "type": "BiologicFunction"}, {"text": "Drug", "type": "Chemical"}, {"text": "Apoptosis", "type": "BiologicFunction"}, {"text": "Lymphoblastic Leukemia", "type": "BiologicFunction"}, {"text": "extracellular", "type": "SpatialConcept"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "tumor progression", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Input:
Sentence: It can be concluded that acidic pH increases the proliferation , invasion and reduces the drug - induced apoptosis in acute lymphoblastic leukemia .

## Item MedMentions:test:968
Example input:
Sentence: 88 % lower than in Group B ( 25 . 60±6 .

Example answer:
{"entities": []}

Example input:
Sentence: Average AL was higher among FRC users than among non - FRC users ( 1 . 8 versus 1 . 6 mm ; P = 0 .

Example answer:
{"entities": [{"text": "AL", "type": "BiologicFunction"}, {"text": "FRC users", "type": "BiologicFunction"}, {"text": "non - FRC users", "type": "Finding"}]}

Example input:
Sentence: Between group comparison : The CD4 + percentage of group E was higher than that of group P ( P < 0 .

Example answer:
{"entities": [{"text": "CD4 + percentage", "type": "HealthCareActivity"}]}

Example input:
Sentence: 79 to 1 . 45 and there was no consistent pattern among the three groups ; the changes were not statistically significantly different from baseline .

Example answer:
{"entities": [{"text": "pattern", "type": "SpatialConcept"}, {"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: 9 % ) in group B ( P = 0 . 016 ) and at 1 month it was 0 compared to 4 ( 1 . 0 % ) ( P = 0 . 0483 ) .

Example answer:
{"entities": [{"text": "group B", "type": "IntellectualProduct"}]}

Example input:
Sentence: However , the difference was not statistically significant ( P = 0 . 149 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 20 ) , with no significant difference ( P > . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: There was no significant difference between groups in terms of genotype distribution ( p > 0 . 05 ) .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: There were significant differences ( P < 0 . 001 ; < 0 . 001 ; < 0 . 001 ; < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: There were significant differences between two groups ( P < 0 . 001 ) .

Example answer:
{"entities": []}

Input:
Sentence: 9 fl , respectively ; there were no significant differences between groups ( p > 0 . 05 ) .

## Item MedMentions:test:181
Example input:
Sentence: Loss of myenteric plexus was observed only in all Ret  homozygotes , irrespective of the genotypes at Sema3d locus , and Sema3d  heterozygote and homozygote mice had normal intestinal innervation .

Example answer:
{"entities": [{"text": "myenteric plexus", "type": "AnatomicalStructure"}, {"text": "Ret", "type": "AnatomicalStructure"}, {"text": "Sema3d", "type": "AnatomicalStructure"}, {"text": "locus", "type": "SpatialConcept"}]}

Example input:
Sentence: We discovered a gene co - occurrence network in mesiodens patients with functionally enriched gene groups in the sonic hedgehog ( SHH ) , bone morphogenetic proteins ( BMP ) , and wingless integrated ( WNT ) signaling pathways .

Example answer:
{"entities": [{"text": "gene", "type": "AnatomicalStructure"}, {"text": "mesiodens", "type": "BiologicFunction"}, {"text": "sonic hedgehog", "type": "Chemical"}, {"text": "SHH", "type": "Chemical"}, {"text": "bone morphogenetic proteins", "type": "Chemical"}, {"text": "BMP", "type": "Chemical"}, {"text": "wingless integrated", "type": "Chemical"}, {"text": "WNT", "type": "Chemical"}, {"text": "signaling pathways", "type": "BiologicFunction"}]}

Example input:
Sentence: Knocking down TCF8 inhibits high glucose - and angiotensin II - induced epithelial to mesenchymal transition in podocytes Epithelial to mesenchymal transition ( EMT ) is a physiological phenomenon in mammalian embryogenesis by which epithelial cells become mesenchymal stem cells .

Example answer:
{"entities": [{"text": "Knocking down", "type": "ResearchActivity"}, {"text": "TCF8", "type": "AnatomicalStructure"}, {"text": "high glucose", "type": "Finding"}, {"text": "angiotensin II", "type": "Chemical"}, {"text": "epithelial to mesenchymal transition", "type": "BiologicFunction"}, {"text": "podocytes", "type": "AnatomicalStructure"}, {"text": "Epithelial to mesenchymal transition", "type": "BiologicFunction"}, {"text": "EMT", "type": "BiologicFunction"}, {"text": "physiological phenomenon", "type": "BiologicFunction"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "embryogenesis", "type": "BiologicFunction"}, {"text": "epithelial cells", "type": "AnatomicalStructure"}, {"text": "mesenchymal stem cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A change in expression of ZnTs and Zips in response to Cd exposure emphasizes the involvement of Zn transporters in Cd cellular metabolism and induced oxidative stress .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "ZnTs", "type": "BiologicFunction"}, {"text": "Zips", "type": "BiologicFunction"}, {"text": "Cd", "type": "Chemical"}, {"text": "Zn transporters", "type": "Chemical"}, {"text": "induced", "type": "BiologicFunction"}, {"text": "oxidative stress", "type": "BiologicFunction"}]}

Example input:
Sentence: We intercrossed Ret and Sema3d double  heterozygotes to generate mice with the nine possible genotypes and assessed survival by counting various genotypes , myenteric plexus presence by acetylcholinesterase staining and embryonic day 12 .

Example answer:
{"entities": [{"text": "Ret", "type": "AnatomicalStructure"}, {"text": "Sema3d", "type": "AnatomicalStructure"}, {"text": "counting various genotypes", "type": "HealthCareActivity"}, {"text": "myenteric plexus", "type": "AnatomicalStructure"}, {"text": "acetylcholinesterase staining", "type": "HealthCareActivity"}]}

Example input:
Sentence: Modeling the ferrochelatase c . 315 - 48C modifier mutation for erythropoietic protoporphyria ( EPP ) in mice Erythropoietic protoporphyria ( EPP ) is caused by deficiency of ferrochelatase ( FECH ) , which incorporates iron into protoporphyrin IX ( PPIX ) to form heme .

Example answer:
{"entities": [{"text": "Modeling", "type": "ResearchActivity"}, {"text": "ferrochelatase c . 315 - 48C", "type": "AnatomicalStructure"}, {"text": "mutation", "type": "BiologicFunction"}, {"text": "erythropoietic protoporphyria", "type": "BiologicFunction"}, {"text": "EPP", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "Erythropoietic protoporphyria", "type": "BiologicFunction"}, {"text": "ferrochelatase", "type": "Chemical"}, {"text": "FECH", "type": "Chemical"}, {"text": "iron", "type": "Chemical"}, {"text": "protoporphyrin IX", "type": "Chemical"}, {"text": "PPIX", "type": "Chemical"}, {"text": "heme", "type": "Chemical"}]}

Example input:
Sentence: Additionally , transforming growth factor‑β1 ( TGF‑β1 ) induced the EMT , characterized by the upregulated expression of the mesenchymal markers , namely N‑cadherin , vimentin , α‑smooth muscle actin , collagen I and collagen III , and the downregulated expression of the epithelial marker E - cadherin in A549 and HBE cells .

Example answer:
{"entities": [{"text": "transforming growth factor‑β1", "type": "Chemical"}, {"text": "TGF‑β1", "type": "Chemical"}, {"text": "EMT", "type": "BiologicFunction"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "expression", "type": "HealthCareActivity"}, {"text": "mesenchymal markers", "type": "BiologicFunction"}, {"text": "N‑cadherin", "type": "Chemical"}, {"text": "vimentin", "type": "Chemical"}, {"text": "α‑smooth muscle actin", "type": "Chemical"}, {"text": "collagen I", "type": "Chemical"}, {"text": "collagen III", "type": "Chemical"}, {"text": "downregulated", "type": "BiologicFunction"}, {"text": "epithelial marker", "type": "BiologicFunction"}, {"text": "E - cadherin", "type": "Chemical"}, {"text": "A549", "type": "AnatomicalStructure"}, {"text": "HBE cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Morpholino -mediated knock - down of zip10 causes delayed epiboly and deformities of the head , eye , heart and tail .

Example answer:
{"entities": [{"text": "Morpholino", "type": "Chemical"}, {"text": "knock - down", "type": "ResearchActivity"}, {"text": "zip10", "type": "AnatomicalStructure"}, {"text": "epiboly", "type": "BiologicFunction"}, {"text": "head", "type": "SpatialConcept"}, {"text": "eye", "type": "AnatomicalStructure"}, {"text": "heart", "type": "AnatomicalStructure"}, {"text": "tail", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We postulate that a subset of ZIPs carrying PrP - like ectodomains , including ZIP6 and ZIP10 , are integral to cellular pathways and plasticity programs , such as EMT .

Example answer:
{"entities": [{"text": "subset", "type": "IntellectualProduct"}, {"text": "ZIPs", "type": "Chemical"}, {"text": "PrP - like ectodomains", "type": "SpatialConcept"}, {"text": "ZIP6", "type": "Chemical"}, {"text": "ZIP10", "type": "Chemical"}, {"text": "cellular", "type": "HealthCareActivity"}, {"text": "pathways", "type": "BiologicFunction"}, {"text": "plasticity", "type": "BiologicFunction"}, {"text": "EMT", "type": "BiologicFunction"}]}

Example input:
Sentence: Zinc transporter ZIP10 forms a heteromer with ZIP6 which regulates embryonic development and cell migration There is growing evidence that zinc and its transporters are involved in cell migration during development and in cancer .

Example answer:
{"entities": [{"text": "Zinc transporter", "type": "Chemical"}, {"text": "ZIP10", "type": "Chemical"}, {"text": "ZIP6", "type": "Chemical"}, {"text": "regulates", "type": "BiologicFunction"}, {"text": "embryonic development", "type": "BiologicFunction"}, {"text": "cell migration", "type": "BiologicFunction"}, {"text": "zinc", "type": "Chemical"}, {"text": "transporters", "type": "Chemical"}, {"text": "development", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}]}

Input:
Sentence: Furthermore , zip10 deficiency results in overexpression of cdh1 , zip6 and stat3 , the latter gene product driving transcription of both zip6 and zip10 The non - reduntant requirement of Zip6 and Zip10 for epithelial to mesenchymal transition ( EMT ) is consistent with our finding that they exist as a heteromer .

## Item MedMentions:test:992
Example input:
Sentence: Concentrations of polybrominated diphenyl ethers were highest in the Toronto and Region AOC , and at 2 of the Bay of Quinte AOC exposed sites near Trenton and Belleville .

Example answer:
{"entities": [{"text": "polybrominated diphenyl ethers", "type": "Chemical"}, {"text": "Toronto and Region AOC", "type": "SpatialConcept"}, {"text": "Bay of Quinte", "type": "SpatialConcept"}, {"text": "AOC", "type": "SpatialConcept"}, {"text": "Trenton and Belleville", "type": "SpatialConcept"}]}

Example input:
Sentence: The findings demonstrate that the mean annual concentration of PM2 .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}]}

Example input:
Sentence: Organophosphate Esters in Air , Snow and Seawater in the North Atlantic and the Arctic The concentrations of eight organophosphate esters ( OPEs ) have been investigated in air , snow and seawater samples collected during the cruise of ARK - XXVIII / 2 from 6th June to 3rd July 2014 across the North Atlantic and the Arctic .

Example answer:
{"entities": [{"text": "Organophosphate Esters", "type": "Chemical"}, {"text": "North Atlantic", "type": "SpatialConcept"}, {"text": "Arctic", "type": "SpatialConcept"}, {"text": "organophosphate esters", "type": "Chemical"}, {"text": "OPEs", "type": "Chemical"}]}

Example input:
Sentence: The greatest burden appears for the most part in infants ( < 1 year ) in Bulgaria , Hungary , Latvia , Romania , and Serbia , but not in the other participating countries where the burden may have shifted to older children , though surveillance of adults may be inappropriate .

Example answer:
{"entities": [{"text": "Bulgaria", "type": "SpatialConcept"}, {"text": "Hungary", "type": "SpatialConcept"}, {"text": "Latvia", "type": "SpatialConcept"}, {"text": "Romania", "type": "SpatialConcept"}, {"text": "Serbia", "type": "SpatialConcept"}, {"text": "countries", "type": "SpatialConcept"}]}

Example input:
Sentence: This study focused on the proportion of mortality due to lung cancer and cardiopulmonary diseases attributable to PM2 .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "cardiopulmonary diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Thanks to intense efforts by the Polish Nurses Association and the International Council of Nurses Accredited Center for ICNP ( ® ) Research & Development at the Medical University of Łódź , the Classification is known in Poland and has been tested at several centres .

Example answer:
{"entities": [{"text": "Polish Nurses Association", "type": "Organization"}, {"text": "International Council of Nurses", "type": "Organization"}, {"text": "ICNP", "type": "IntellectualProduct"}, {"text": "Research & Development", "type": "ResearchActivity"}, {"text": "Medical University of Łódź", "type": "Organization"}, {"text": "Classification", "type": "IntellectualProduct"}, {"text": "Poland", "type": "SpatialConcept"}]}

Example input:
Sentence: The soil dust is the largest contributor to HMCR , being driven by the high impact of soil dust on PM2 .

Example answer:
{"entities": []}

Example input:
Sentence: However , in 2014 , only 11 cases of work - related COPD were recognized in Poland .

Example answer:
{"entities": [{"text": "COPD", "type": "BiologicFunction"}, {"text": "Poland", "type": "SpatialConcept"}]}

Example input:
Sentence: 5 concentration on the incidence of premature deaths is unduly high in Polish cities .

Example answer:
{"entities": [{"text": "premature deaths", "type": "Finding"}, {"text": "Polish", "type": "PopulationGroup"}, {"text": "cities", "type": "SpatialConcept"}]}

Example input:
Sentence: 5 Exposure and Mortality Due to Lung Cancer and Cardiopulmonary Diseases in Polish Cities Air pollution , one of ten most important causes of premature mortality worldwide , remains a major issue also in the EU , with more than 400 , 000 premature deaths due to exposure to PM2 .

Example answer:
{"entities": [{"text": "Lung Cancer", "type": "BiologicFunction"}, {"text": "Cardiopulmonary Diseases", "type": "BiologicFunction"}, {"text": "Polish", "type": "PopulationGroup"}, {"text": "Cities", "type": "SpatialConcept"}, {"text": "premature mortality", "type": "Finding"}, {"text": "issue", "type": "Finding"}, {"text": "EU", "type": "Organization"}, {"text": "premature deaths", "type": "Finding"}]}

Input:
Sentence: The issue is particularly significant in Poland , where there is the highest concentration of PM2 .

## Item MedMentions:test:690
Example input:
Sentence: The consensus motif sequence RRm6ACH was observed in 78 . 90 % of m6A peaks .

Example answer:
{"entities": [{"text": "consensus motif sequence", "type": "SpatialConcept"}, {"text": "RRm6ACH", "type": "SpatialConcept"}, {"text": "m6A", "type": "Chemical"}]}

Example input:
Sentence: Our findings are consistent with the idea that diffuse co - evolution drives the evolution of extremely long proboscises and flower tubes , and highlight the importance of morphological traits , beyond the forbidden links hypothesis , in structuring interactions between mutualistic partners , revealing that the role of niche - based processes can be much more complex than previously known .

Example answer:
{"entities": [{"text": "co - evolution", "type": "BiologicFunction"}, {"text": "evolution", "type": "BiologicFunction"}, {"text": "long proboscises", "type": "Eukaryote"}, {"text": "flower tubes", "type": "Eukaryote"}, {"text": "morphological", "type": "SpatialConcept"}]}

Example input:
Sentence: Our experimental results reveal that different cancer interactomes are characterized by significant enhancement of long - range NTC , which arises from circulation of information flow within robustly organized gene subnetworks .

Example answer:
{"entities": [{"text": "gene subnetworks", "type": "BiologicFunction"}]}

Example input:
Sentence: Interestingly , we show here that a construct that contains all the regulatory regions of the UPF3 gene except this long 3 ' UTR is also feedback - regulated by NMD .

Example answer:
{"entities": [{"text": "regulatory regions", "type": "Chemical"}, {"text": "UPF3 gene", "type": "AnatomicalStructure"}, {"text": "3 ' UTR", "type": "SpatialConcept"}, {"text": "feedback - regulated", "type": "BiologicFunction"}, {"text": "NMD", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , we construct a cellular network of 74538 directional and differential gene expression weighted protein - protein and gene regulatory interactions , and perform graph - theoretical analysis of global human interactome using a novel , degree - independent feature - the normalized total communicability ( NTC ) .

Example answer:
{"entities": [{"text": "cellular network", "type": "BiologicFunction"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "protein - protein", "type": "BiologicFunction"}, {"text": "graph - theoretical analysis", "type": "ResearchActivity"}, {"text": "global human interactome", "type": "BiologicFunction"}]}

Example input:
Sentence: One is the basin entropy , which is a complexity measure of the dynamics of Boolean networks .

Example answer:
{"entities": [{"text": "Boolean", "type": "IntellectualProduct"}]}

Example input:
Sentence: The other is the diversity of cyclic attractor lengths that a given motif can produce .

Example answer:
{"entities": []}

Example input:
Sentence: Using these two measures , we examine all 104 topologically distinct three - node motifs and show that the structural properties of a motif , such as the presence of feedback loops and feed - forward loops , predict fundamental characteristics of its dynamical state space , which in turn determine aspects of its functional versatility .

Example answer:
{"entities": [{"text": "structural", "type": "SpatialConcept"}]}

Example input:
Sentence: Recent studies have used Boolean network motifs to explore the link between form and function in gene regulatory networks and have found that the structure of a motif does not strongly determine its function , if this is defined in terms of the gene expression patterns the motif can produce .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "Boolean", "type": "IntellectualProduct"}, {"text": "gene regulatory networks", "type": "BiologicFunction"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "patterns", "type": "SpatialConcept"}]}

Example input:
Sentence: Form and function in gene regulatory networks : the structure of network motifs determines fundamental properties of their dynamical state space Network motifs have been studied extensively over the past decade , and certain motifs , such as the feed - forward loop , play an important role in regulatory networks .

Example answer:
{"entities": [{"text": "gene regulatory networks", "type": "BiologicFunction"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "regulatory networks", "type": "BiologicFunction"}]}

Input:
Sentence: We also show that these higher - level properties have a direct bearing on real regulatory networks , as both basin entropy and cycle length diversity show a close correspondence with the prevalence , in neural and genetic regulatory networks , of the 13 connected motifs without self - interactions that have been studied extensively in the literature .

## Item MedMentions:test:830
Example input:
Sentence: Repeated - measures analysis demonstrated that the experience of pain differed significantly over time by location ( F5 , 70 = 3 . 864 , P = .004 ) , with a notable decrease in pain scores more than 1 hour after sheath removal at the location that used the progressive head elevation protocol .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "pain", "type": "Finding"}, {"text": "location", "type": "SpatialConcept"}, {"text": "pain scores", "type": "Finding"}, {"text": "sheath", "type": "AnatomicalStructure"}, {"text": "removal", "type": "HealthCareActivity"}, {"text": "head", "type": "SpatialConcept"}, {"text": "elevation protocol", "type": "HealthCareActivity"}]}

Example input:
Sentence: Mean opioid consumption ( morphine equivalence ) over a mean of 4 . 8 postoperative days ( range , 0 - 16 days ) was 58 . 5 mg ( range , 0 - 280 mg ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: All patients were asked to grade their pain experience during induction and maintenance of anesthesia and also during the phacoemulsification surgery , using a visual analogue scale ( VAS ) from 0 ( no pain ) to 10 ( unbearable pain ) administered after the surgery .

Example answer:
{"entities": [{"text": "pain", "type": "Finding"}, {"text": "experience", "type": "BiologicFunction"}, {"text": "induction", "type": "HealthCareActivity"}, {"text": "anesthesia", "type": "HealthCareActivity"}, {"text": "phacoemulsification surgery", "type": "HealthCareActivity"}, {"text": "visual analogue scale", "type": "HealthCareActivity"}, {"text": "VAS", "type": "HealthCareActivity"}, {"text": "no pain", "type": "Finding"}, {"text": "unbearable pain", "type": "Finding"}, {"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: All groups were evaluated at 24 , 48 and 72 h in order to determine the possible negative effects of the drug on the chondrocytes .

Example answer:
{"entities": [{"text": "possible", "type": "Finding"}, {"text": "negative", "type": "Finding"}, {"text": "drug", "type": "Chemical"}, {"text": "chondrocytes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: All patients were evaluated clinically with American Knee Society Score ( AKSS ) and visual analogue scale ( VAS ) for the pain before the treatment and after 3 months .

Example answer:
{"entities": [{"text": "visual analogue scale", "type": "HealthCareActivity"}, {"text": "VAS", "type": "HealthCareActivity"}, {"text": "pain", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: 9 - 82 . 9 % ) who did not use rescue medication during the OP .

Example answer:
{"entities": [{"text": "rescue medication", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients were initially screened by phone 3 months after injury using the validated International Association for the Study of Pain Budapest criteria .

Example answer:
{"entities": [{"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "International Association for the Study of Pain", "type": "Organization"}, {"text": "Budapest criteria", "type": "IntellectualProduct"}]}

Example input:
Sentence: Primary outcome was morphine consumption 0 to 24 hours postoperatively .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Secondary outcomes were acute pain at rest and during mobilization 2 to 24 hours postoperatively ( visual analogue scale ) , adverse events , and persistent pain 6 months postoperatively .

Example answer:
{"entities": [{"text": "acute pain at rest", "type": "Finding"}, {"text": "mobilization", "type": "HealthCareActivity"}, {"text": "visual analogue scale", "type": "HealthCareActivity"}, {"text": "adverse events", "type": "BiologicFunction"}, {"text": "pain", "type": "Finding"}]}

Example input:
Sentence: Patient - controlled analgesia IV morphine consumption 0 to 24 hours postoperatively was significantly reduced in the ketamine group compared with the placebo group : 79 ( 47 ) vs 121 ( 53 ) mg IV , mean difference 42 mg ( 95 % confidence interval -59 to -25 ) , P < 0 . 001 .

Example answer:
{"entities": [{"text": "Patient - controlled analgesia", "type": "HealthCareActivity"}, {"text": "morphine", "type": "Chemical"}, {"text": "ketamine", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}]}

Input:
Sentence: We evaluated the time of first analgesic rescue medication , pain intensity , total analgesic consumption and adverse effects .

## Item MedMentions:test:880
Example input:
Sentence: Purpose Workplace injury and illness rates are high within the nursing profession , and in conjunction with current nursing shortages , low retention rates , and the high cost of workplace injury , the need for effective return to work ( RTW ) for injured nurses is highlighted .

Example answer:
{"entities": [{"text": "Workplace", "type": "SpatialConcept"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "illness", "type": "Finding"}, {"text": "nursing profession", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "nursing", "type": "ProfessionalOrOccupationalGroup"}, {"text": "workplace", "type": "SpatialConcept"}, {"text": "return to work", "type": "Finding"}, {"text": "RTW", "type": "Finding"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: A pilot study exploring the relationship between self - compassion , self - judgement , self - kindness , compassion , professional quality of life and wellbeing among UK community nurses Compassion fatigue and burnout can impact on performance of nurses .

Example answer:
{"entities": [{"text": "pilot study", "type": "ResearchActivity"}, {"text": "judgement", "type": "BiologicFunction"}, {"text": "kindness", "type": "BiologicFunction"}, {"text": "wellbeing", "type": "Finding"}, {"text": "UK", "type": "SpatialConcept"}, {"text": "community nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Compassion fatigue", "type": "BiologicFunction"}, {"text": "burnout", "type": "BiologicFunction"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Interpersonal relationships and management issues most strongly predicted participants ' burnout ( 11·3 % of average variance ) .

Example answer:
{"entities": [{"text": "issues", "type": "Finding"}, {"text": "participants '", "type": "PopulationGroup"}, {"text": "burnout", "type": "BiologicFunction"}]}

Example input:
Sentence: Results are discussed in terms of potential approaches to supporting nursing students who may be at risk of burnout .

Example answer:
{"entities": [{"text": "nursing students", "type": "ProfessionalOrOccupationalGroup"}, {"text": "burnout", "type": "BiologicFunction"}]}

Example input:
Sentence: Predictors of occupational burnout among nurses : a dominance analysis of job stressors To quantitatively compare dimensions of job stressors ' effects on nurses ' burnout .

Example answer:
{"entities": [{"text": "occupational burnout", "type": "BiologicFunction"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "nurses '", "type": "ProfessionalOrOccupationalGroup"}, {"text": "burnout", "type": "BiologicFunction"}]}

Example input:
Sentence: Results show that community nurses who score high on measures of self - compassion and wellbeing , also report less burnout .

Example answer:
{"entities": [{"text": "community nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "wellbeing", "type": "Finding"}, {"text": "burnout", "type": "BiologicFunction"}]}

Example input:
Sentence: We compared five potential stressors ' ability to predict nurses ' burnout using dominance analysis and assuming that each stressor was intercorrelated .

Example answer:
{"entities": [{"text": "nurses '", "type": "ProfessionalOrOccupationalGroup"}, {"text": "burnout", "type": "BiologicFunction"}]}

Example input:
Sentence: Can We Predict Burnout among Student Nurses ? An Exploration of the ICWR - 1 Model of Individual Psychological Resilience The nature of nursing work is demanding and can be stressful .

Example answer:
{"entities": [{"text": "Burnout", "type": "BiologicFunction"}, {"text": "Student Nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "ICWR - 1 Model", "type": "IntellectualProduct"}, {"text": "Individual", "type": "PopulationGroup"}, {"text": "nursing work", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "demanding", "type": "HealthCareActivity"}]}

Example input:
Sentence: Extensive research has examined the relationship between job stressors and burnout ; however , less has specifically compared the effects of job stressor domains on nurses ' burnout .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "burnout", "type": "BiologicFunction"}, {"text": "nurses '", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Job stressors , and particularly interpersonal relationships and management issues , significantly predict nurses ' job burnout .

Example answer:
{"entities": [{"text": "issues", "type": "Finding"}, {"text": "nurses '", "type": "ProfessionalOrOccupationalGroup"}, {"text": "job burnout", "type": "BiologicFunction"}]}

Input:
Sentence: Previous studies have shown a high rate of burnout among employed nurses .

## Item MedMentions:test:216
Example input:
Sentence: This review is aimed at collecting and summarizing available evidence from experimental and mechanistic studies on the action of GLP1 - RA and DPP4i on the cardiovascular system , both deriving from clinical and pre - clinical sources .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "experimental", "type": "ResearchActivity"}, {"text": "mechanistic studies", "type": "ResearchActivity"}, {"text": "GLP1 - RA", "type": "Chemical"}, {"text": "DPP4i", "type": "Chemical"}, {"text": "cardiovascular system", "type": "BodySystem"}]}

Example input:
Sentence: In particular , we discuss the possible contribution to the incretin cardiovascular effects of a direct cardiac action of GLP - 1 metabolites through GLP - 1 receptor -independent pathways , and of DPP4 substrates other than GLP - 1 .

Example answer:
{"entities": [{"text": "incretin", "type": "Chemical"}, {"text": "cardiovascular", "type": "BodySystem"}, {"text": "cardiac", "type": "AnatomicalStructure"}, {"text": "GLP - 1", "type": "Chemical"}, {"text": "metabolites", "type": "Chemical"}, {"text": "GLP - 1 receptor", "type": "Chemical"}, {"text": "pathways", "type": "BiologicFunction"}, {"text": "DPP4", "type": "Chemical"}]}

Example input:
Sentence: Moreover , studies also suggest that ALR2 and PARP - 1 co - occur in retinal cells , making them appropriate targets for the treatment of diabetic retinopathy .

Example answer:
{"entities": [{"text": "ALR2", "type": "Chemical"}, {"text": "PARP - 1", "type": "Chemical"}, {"text": "retinal", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "diabetic retinopathy", "type": "BiologicFunction"}]}

Example input:
Sentence: Angiopoietin - like protein 4 improves glucose tolerance and insulin resistance but induces liver steatosis in high - fat - diet mice Angiopoietin - like protein 4 ( Angptl4 ) is a secreted protein predominantly expressed in liver and adipose tissues , and has been identified as an adipokine .

Example answer:
{"entities": [{"text": "Angiopoietin - like protein 4", "type": "Chemical"}, {"text": "improves", "type": "Finding"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "liver steatosis", "type": "BiologicFunction"}, {"text": "high - fat - diet mice", "type": "Eukaryote"}, {"text": "Angptl4", "type": "Chemical"}, {"text": "secreted protein", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "adipose tissues", "type": "AnatomicalStructure"}, {"text": "adipokine", "type": "Chemical"}]}

Example input:
Sentence: Adv ‑ Angptl4 injection was observed to improve glucose tolerance and insulin resistance .

Example answer:
{"entities": [{"text": "Adv", "type": "Virus"}, {"text": "Angptl4", "type": "AnatomicalStructure"}, {"text": "improve", "type": "Finding"}, {"text": "insulin resistance", "type": "BiologicFunction"}]}

Example input:
Sentence: Administration of RGD peptide , TGFβ , and αvβ6 - neutralizing antibodies attenuated IVD degeneration .

Example answer:
{"entities": [{"text": "Administration", "type": "HealthCareActivity"}, {"text": "RGD peptide", "type": "Chemical"}, {"text": "TGFβ", "type": "Chemical"}, {"text": "αvβ6", "type": "Chemical"}, {"text": "neutralizing antibodies", "type": "Chemical"}, {"text": "IVD degeneration", "type": "BiologicFunction"}]}

Example input:
Sentence: Perspectives on cardiovascular effects of incretin -based drugs : From bedside to bench , return trip Recently , cardiovascular outcome trials with glucose -lowering drugs used in type 2 diabetes mellitus , namely glucagon - like peptide - 1 receptor agonists ( GLP - 1RA ) , liraglutide and semaglutide , showed a reduction in cardiovascular events , which had not been observed in trials with other incretin -based drugs , such as lixisenatide or with dipeptidyl peptidase - 4 inhibitors ( DPP4i ) .

Example answer:
{"entities": [{"text": "cardiovascular", "type": "BodySystem"}, {"text": "incretin", "type": "Chemical"}, {"text": "drugs", "type": "Chemical"}, {"text": "trials", "type": "ResearchActivity"}, {"text": "glucose", "type": "Chemical"}, {"text": "type 2 diabetes mellitus", "type": "BiologicFunction"}, {"text": "glucagon - like peptide - 1 receptor", "type": "Chemical"}, {"text": "agonists", "type": "Chemical"}, {"text": "GLP - 1RA", "type": "Chemical"}, {"text": "liraglutide", "type": "Chemical"}, {"text": "semaglutide", "type": "Chemical"}, {"text": "cardiovascular events", "type": "Finding"}, {"text": "lixisenatide", "type": "Chemical"}, {"text": "dipeptidyl peptidase - 4 inhibitors", "type": "Chemical"}, {"text": "DPP4i", "type": "Chemical"}]}

Example input:
Sentence: This is the first study to show the benefits of DPP4 inhibitors in reducing DR progression , and provides encouraging preliminary data for further evaluation of DPP4 inhibitors in the progression of DR in a randomized , double - blind , placebo - controlled trial .

Example answer:
{"entities": [{"text": "DPP4 inhibitors", "type": "Chemical"}, {"text": "DR", "type": "BiologicFunction"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "evaluation", "type": "HealthCareActivity"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "double - blind", "type": "ResearchActivity"}]}

Example input:
Sentence: Seven of 28 patients treated with DPP4 inhibitors and 26 of 54 treated with other hypoglycemic agents showed progression of retinopathy , defined as one or more steps on the Early Treatment Diabetic Retinopathy Study scale ( P = 0 . 043 ) .

Example answer:
{"entities": [{"text": "DPP4 inhibitors", "type": "Chemical"}, {"text": "hypoglycemic agents", "type": "Chemical"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "retinopathy", "type": "BiologicFunction"}]}

Example input:
Sentence: Treatment with DPP4 inhibitors was the independent protective factor against the progression of DR , aside from improving glycemic control .

Example answer:
{"entities": [{"text": "DPP4 inhibitors", "type": "Chemical"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "DR", "type": "BiologicFunction"}, {"text": "improving glycemic control", "type": "Finding"}]}

Input:
Sentence: PROTECTIVE EFFECTS OF DIPEPTIDYL PEPTIDASE - 4 INHIBITORS ON PROGRESSION OF DIABETIC RETINOPATHY IN PATIENTS WITH TYPE 2 DIABETES To investigate the effects of dipeptidyl peptidase - 4 inhibitors ( DPP4 ) on the progression of diabetic retinopathy ( DR ) in patients with Type 2 diabetes based on the DR severity scale .

## Item MedMentions:test:283
Example input:
Sentence: Simulating the potential role of media coverage and infected bats in the 2014 Ebola outbreak Multiple epidemiological models have been developed to model the transmission dynamics of Ebola virus ( EBOV ) disease in West Africa in 2014 because the severity of the epidemic is commonly overestimated .

Example answer:
{"entities": [{"text": "Simulating", "type": "ResearchActivity"}, {"text": "infected", "type": "Finding"}, {"text": "bats", "type": "Eukaryote"}, {"text": "Ebola", "type": "BiologicFunction"}, {"text": "Ebola virus ( EBOV ) disease", "type": "BiologicFunction"}, {"text": "West Africa", "type": "SpatialConcept"}]}

Example input:
Sentence: A compartmental model that incorporates the media impact and the effect of infected bats was constructed and calibrated using data reported until the end of 2014 .

Example answer:
{"entities": [{"text": "compartmental model", "type": "IntellectualProduct"}, {"text": "infected", "type": "Finding"}, {"text": "bats", "type": "Eukaryote"}]}

Example input:
Sentence: We sought to determine if the same macaques maintained high mucosal plasma cell frequencies postinfection and if this translated to reduced viremia .

Example answer:
{"entities": [{"text": "macaques", "type": "Eukaryote"}, {"text": "mucosal", "type": "AnatomicalStructure"}, {"text": "plasma cell", "type": "AnatomicalStructure"}, {"text": "viremia", "type": "BiologicFunction"}]}

Example input:
Sentence: To gain insights into the pathogenicity of this variant , its viral load and temporal shedding pattern were evaluated in piglets from infected farms .

Example answer:
{"entities": [{"text": "viral load", "type": "HealthCareActivity"}, {"text": "temporal shedding", "type": "BiologicFunction"}, {"text": "pattern", "type": "SpatialConcept"}, {"text": "piglets", "type": "Eukaryote"}, {"text": "infected", "type": "Finding"}, {"text": "farms", "type": "SpatialConcept"}]}

Example input:
Sentence: Accordingly , low - viremic macaques had a higher frequency of both bone marrow IRF4 ( hi ) subsets than did animals with high viremia .

Example answer:
{"entities": [{"text": "macaques", "type": "Eukaryote"}, {"text": "bone marrow", "type": "AnatomicalStructure"}, {"text": "IRF4 ( hi )", "type": "AnatomicalStructure"}, {"text": "animals", "type": "Eukaryote"}, {"text": "viremia", "type": "BiologicFunction"}]}

Example input:
Sentence: Then , we analysed the viral replication and plaque size ( latitude ) in Madin - Darby bovine kidney ( MDBK ) cells and the respiratory mucosa as well as viral penetration depth underneath the BM of the respiratory mucosa when inoculated with these recombinant viruses .

Example answer:
{"entities": [{"text": "analysed", "type": "ResearchActivity"}, {"text": "viral replication", "type": "BiologicFunction"}, {"text": "plaque", "type": "Finding"}, {"text": "size", "type": "SpatialConcept"}, {"text": "Madin - Darby bovine kidney", "type": "AnatomicalStructure"}, {"text": "MDBK", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "respiratory mucosa", "type": "AnatomicalStructure"}, {"text": "viral penetration", "type": "BiologicFunction"}, {"text": "BM", "type": "AnatomicalStructure"}, {"text": "inoculated", "type": "HealthCareActivity"}, {"text": "recombinant viruses", "type": "Virus"}]}

Example input:
Sentence: The evolutionary relationship of Saudi RHDVs strains revealed significant nucleotides and amino acid substitutions in hypervariable region E , suggesting the emergence of new RHDVs circulating in Saudi Arabia rabbitries .

Example answer:
{"entities": [{"text": "Saudi", "type": "SpatialConcept"}, {"text": "RHDVs strains", "type": "Virus"}, {"text": "nucleotides", "type": "Chemical"}, {"text": "amino acid substitutions", "type": "BiologicFunction"}, {"text": "hypervariable region E", "type": "SpatialConcept"}, {"text": "emergence", "type": "BiologicFunction"}, {"text": "RHDVs", "type": "Virus"}, {"text": "Saudi Arabia", "type": "SpatialConcept"}, {"text": "rabbitries", "type": "SpatialConcept"}]}

Example input:
Sentence: However , the uptake and spread of these RABV variants into N2a cells were inversely proportional .

Example answer:
{"entities": [{"text": "uptake", "type": "BiologicFunction"}, {"text": "spread", "type": "BiologicFunction"}, {"text": "RABV", "type": "Virus"}, {"text": "variants", "type": "Finding"}, {"text": "N2a cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Although delayed SIV acquisition did not predict subsequent viral control , alterations existed in the distribution of plasma cells and plasmablasts between macaques that exhibited high or low viremia .

Example answer:
{"entities": [{"text": "SIV", "type": "Virus"}, {"text": "plasma cells", "type": "AnatomicalStructure"}, {"text": "plasmablasts", "type": "AnatomicalStructure"}, {"text": "macaques", "type": "Eukaryote"}, {"text": "viremia", "type": "BiologicFunction"}]}

Example input:
Sentence: Our results provide evidence that the clinical manifestations of infection with bat RABV variant occur at a later time when compared to what was observed with canine and marmoset rabies virus variants .

Example answer:
{"entities": [{"text": "infection", "type": "BiologicFunction"}, {"text": "bat", "type": "Eukaryote"}, {"text": "RABV", "type": "Virus"}, {"text": "variant", "type": "Finding"}, {"text": "canine", "type": "Eukaryote"}, {"text": "marmoset", "type": "Eukaryote"}, {"text": "rabies virus", "type": "Virus"}, {"text": "variants", "type": "Finding"}]}

Input:
Sentence: Delayed progression of rabies transmitted by a vampire bat Here , we compared the growth kinetics , cell - to - cell spread , and virus internalization kinetics in N2a cells of RABV variants isolated from vampire bats ( V - 3 ) , domestic dogs ( V - 2 ) and marmosets ( V - M ) as well as the clinical symptoms and mortality caused by these variants .

## Item MedMentions:test:566
Example input:
Sentence: With regard to the malignant disorders ( including liver , gastric , colon , pancreatic and oesophageal cancer ) , no such large - scale changes were observed in the last 50 years .

Example answer:
{"entities": [{"text": "malignant disorders", "type": "BiologicFunction"}, {"text": "liver", "type": "BiologicFunction"}, {"text": "gastric", "type": "BiologicFunction"}, {"text": "colon", "type": "BiologicFunction"}, {"text": "pancreatic", "type": "BiologicFunction"}, {"text": "oesophageal cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: In disorder condition , what is the first one : metabolic diseases cause inflammation or conversely ? This " chicken or egg " type question was hard to answer .

Example answer:
{"entities": [{"text": "disorder", "type": "BiologicFunction"}, {"text": "metabolic diseases", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "question", "type": "IntellectualProduct"}]}

Example input:
Sentence: Distinct Abnormalities of Small Bowel and Regional Colonic Volumes in Subtypes of Irritable Bowel Syndrome Revealed by MRI Non - invasive biomarkers which identify different mechanisms of disease in subgroups of irritable bowel syndrome ( IBS ) could be valuable .

Example answer:
{"entities": [{"text": "Abnormalities", "type": "Finding"}, {"text": "Small Bowel", "type": "AnatomicalStructure"}, {"text": "Regional", "type": "SpatialConcept"}, {"text": "Colonic", "type": "AnatomicalStructure"}, {"text": "Subtypes", "type": "IntellectualProduct"}, {"text": "Irritable Bowel Syndrome", "type": "BiologicFunction"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "biomarkers", "type": "ClinicalAttribute"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "subgroups", "type": "IntellectualProduct"}, {"text": "irritable bowel syndrome", "type": "BiologicFunction"}, {"text": "IBS", "type": "BiologicFunction"}]}

Example input:
Sentence: Here we report a patient with a delayed diagnosis of chronic mesenteric ischaemia after 6 months of gastrointestinal symptoms strongly mimicking an alternative diagnosis such as inflammatory bowel disease due an atypical predominance of nausea and diarrhoea rather than pain .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "chronic mesenteric ischaemia", "type": "BiologicFunction"}, {"text": "gastrointestinal symptoms", "type": "Finding"}, {"text": "inflammatory bowel disease", "type": "BiologicFunction"}, {"text": "nausea", "type": "Finding"}, {"text": "diarrhoea", "type": "Finding"}, {"text": "pain", "type": "Finding"}]}

Example input:
Sentence: It is usually related to myeloproliferative disorders , malignancy and hypercoagulable states .

Example answer:
{"entities": [{"text": "myeloproliferative disorders", "type": "BiologicFunction"}, {"text": "malignancy", "type": "BiologicFunction"}, {"text": "hypercoagulable states", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients with GCA had more prior vascular diseases and other comorbidities before the diagnosis and they also had increased risks for incident vascular diseases and many other incident comorbidities after the diagnosis compared with non - vasculitis population .

Example answer:
{"entities": [{"text": "GCA", "type": "BiologicFunction"}, {"text": "vascular diseases", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "risks for incident", "type": "Finding"}]}

Example input:
Sentence: Patients with GCA were more likely to have a history of vascular diseases and other comorbidities except myocardial infarction , type 2 diabetes , obesity and cancer , compared with non - vasculitis patients .

Example answer:
{"entities": [{"text": "GCA", "type": "BiologicFunction"}, {"text": "vascular diseases", "type": "BiologicFunction"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: A Delayed Diagnosis of Chronic Mesenteric Ischaemia : The Role of Clinicians ' Cognitive Errors Chronic diarrhoeal illnesses with nausea and weight loss are a common indication for gastroenterology review .

Example answer:
{"entities": [{"text": "Diagnosis", "type": "Finding"}, {"text": "Chronic Mesenteric Ischaemia", "type": "BiologicFunction"}, {"text": "Clinicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "diarrhoeal illnesses", "type": "BiologicFunction"}, {"text": "nausea", "type": "Finding"}, {"text": "weight loss", "type": "Finding"}, {"text": "gastroenterology", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Among the 55 patients , five were diagnosed with diseases other than HIS ( amoebic colitis , three ; ulcerative colitis , one ) .

Example answer:
{"entities": [{"text": "diagnosed", "type": "Finding"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "HIS", "type": "BiologicFunction"}, {"text": "amoebic colitis", "type": "BiologicFunction"}, {"text": "ulcerative colitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Gastrointestinal features including structural malformations , motility disorders , and upper GI bleeding are major causes of morbidity in CJS .

Example answer:
{"entities": [{"text": "Gastrointestinal", "type": "SpatialConcept"}, {"text": "features", "type": "Finding"}, {"text": "structural malformations", "type": "Finding"}, {"text": "motility disorders", "type": "BiologicFunction"}, {"text": "upper GI bleeding", "type": "BiologicFunction"}, {"text": "CJS", "type": "BiologicFunction"}]}

Input:
Sentence: While many such cases have intra - luminal aetiologies , such as inflammatory bowel disease , coeliac disease or other malabsorptive conditions , with many other cases due to functional gut disorders or systemic malignancy , clinicians must also keep vascular disorders in mind .

## Item MedMentions:test:786
Example input:
Sentence: Data suggest that the cells were able to cope with subnanomolar MeHg exposure , but this tolerance resulted in a significant cost to the cell energy and reserve metabolism as well as ample changes in the nutrition and motility of C .

Example answer:
{"entities": [{"text": "cells", "type": "AnatomicalStructure"}, {"text": "able to cope", "type": "Finding"}, {"text": "MeHg", "type": "Chemical"}, {"text": "cell energy and reserve metabolism", "type": "BiologicFunction"}, {"text": "nutrition", "type": "BiologicFunction"}, {"text": "motility", "type": "BiologicFunction"}, {"text": "C .", "type": "Eukaryote"}]}

Example input:
Sentence: This work demonstrates that glycolytic metabolism regulates the translation of HIF1A to determine T cell responses to hypoxia and implicates GAPDH as a potential mechanism for controlling T cell function in peripheral tissue .

Example answer:
{"entities": [{"text": "glycolytic", "type": "BiologicFunction"}, {"text": "metabolism", "type": "BiologicFunction"}, {"text": "translation", "type": "BiologicFunction"}, {"text": "HIF1A", "type": "AnatomicalStructure"}, {"text": "T cell", "type": "AnatomicalStructure"}, {"text": "responses", "type": "BiologicFunction"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "GAPDH", "type": "Chemical"}, {"text": "function", "type": "BiologicFunction"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In gene expression analyses , 25 ( OH ) D was associated with higher IL - 37 , vitamin A with higher IFN - γ and vitamin E with less IL - 28 ( P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "gene expression", "type": "BiologicFunction"}, {"text": "analyses", "type": "ResearchActivity"}, {"text": "25 ( OH ) D", "type": "Chemical"}, {"text": "IL - 37", "type": "Chemical"}, {"text": "vitamin A", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "IL - 28", "type": "Chemical"}]}

Example input:
Sentence: Pathway analysis showed that upregulated genes were mainly enriched in the " B cell receptor signaling pathway " , " Cell cycle " and " NF - kappa B signaling pathway " , whereas downregulated genes were mainly enriched in the " Ribosome " , " FoxO signaling pathway " and " p53 signaling pathway " .

Example answer:
{"entities": [{"text": "Pathway analysis", "type": "IntellectualProduct"}, {"text": "upregulated genes", "type": "AnatomicalStructure"}, {"text": "B cell receptor signaling pathway", "type": "BiologicFunction"}, {"text": "Cell cycle", "type": "BiologicFunction"}, {"text": "downregulated genes", "type": "AnatomicalStructure"}, {"text": "Ribosome", "type": "AnatomicalStructure"}, {"text": "p53 signaling pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: This achievement represents a crucial step for the development of differential omic strategies leading to the identification of candidate genes putatively involved in the biosynthesis , pathway regulation , and transmembrane transport leading to the anticancer alkaloids from C .

Example answer:
{"entities": [{"text": "omic strategies", "type": "ResearchActivity"}, {"text": "candidate genes", "type": "AnatomicalStructure"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "transmembrane transport", "type": "BiologicFunction"}, {"text": "anticancer", "type": "Finding"}, {"text": "alkaloids", "type": "Chemical"}, {"text": "C .", "type": "Eukaryote"}]}

Example input:
Sentence: When maintained at high temperature , they grew significantly faster , became shorter , with genes involved in sugar metabolism and mitochondrial stress protection significantly upregulated .

Example answer:
{"entities": [{"text": "grew", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "mitochondrial", "type": "AnatomicalStructure"}, {"text": "upregulated", "type": "BiologicFunction"}]}

Example input:
Sentence: In the LC - MS ( E ) analysis , proteins involved in the acute phase response and complement activation and coagulation were significantly different between the staging groups in both models .

Example answer:
{"entities": [{"text": "LC - MS ( E ) analysis", "type": "HealthCareActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "acute phase response", "type": "BiologicFunction"}, {"text": "complement activation", "type": "BiologicFunction"}, {"text": "coagulation", "type": "BiologicFunction"}, {"text": "staging groups", "type": "IntellectualProduct"}, {"text": "models", "type": "IntellectualProduct"}]}

Example input:
Sentence: These results demonstrate the important role of these genes in defense against oxidative stress in different periods of growth .

Example answer:
{"entities": [{"text": "genes", "type": "AnatomicalStructure"}, {"text": "defense against oxidative stress", "type": "BiologicFunction"}, {"text": "growth", "type": "BiologicFunction"}]}

Example input:
Sentence: The major groups of differentially expressed proteins were associated with energy metabolism ( 25 % ) , fatty acid metabolism ( 15 . 79 % ) and defense ( 14 .

Example answer:
{"entities": [{"text": "differentially expressed", "type": "BiologicFunction"}, {"text": "proteins", "type": "Chemical"}, {"text": "energy metabolism", "type": "BiologicFunction"}, {"text": "fatty acid metabolism", "type": "BiologicFunction"}]}

Example input:
Sentence: The KEGG annotation revealed that metabolism pathway genes were enriched .

Example answer:
{"entities": [{"text": "KEGG annotation", "type": "IntellectualProduct"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Input:
Sentence: Deeper analysis indicated that complement together with other genes associated with metabolism , played important roles in the defense of E .

## Item MedMentions:test:952
Example input:
Sentence: It can be concluded that HG could elevate NOXs activity , ROS and MDA levels in neural tissues and Atorvastatin as a small molecule NOX inhibitor drug may prevent and delay diabetic complications , particularly neuropathy .

Example answer:
{"entities": [{"text": "HG", "type": "Finding"}, {"text": "NOXs activity", "type": "BiologicFunction"}, {"text": "ROS", "type": "Chemical"}, {"text": "MDA", "type": "Chemical"}, {"text": "neural tissues", "type": "AnatomicalStructure"}, {"text": "Atorvastatin", "type": "Chemical"}, {"text": "small molecule", "type": "Chemical"}, {"text": "NOX inhibitor drug", "type": "Chemical"}, {"text": "diabetic complications", "type": "BiologicFunction"}, {"text": "neuropathy", "type": "BiologicFunction"}]}

Example input:
Sentence: 23 - 1 . 34 , p < 0 . 001 ) , suggesting that men with higher sun exposure were more likely to become PDE5 inhibitor users .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "sun exposure", "type": "Finding"}, {"text": "PDE5 inhibitor", "type": "Chemical"}, {"text": "users", "type": "PopulationGroup"}]}

Example input:
Sentence: Metabolic profiles of pgm point to redox imbalance as a possible reason for reduced cold acclimation capacity .

Example answer:
{"entities": [{"text": "Metabolic profiles", "type": "BiologicFunction"}, {"text": "pgm", "type": "Chemical"}, {"text": "redox", "type": "BiologicFunction"}, {"text": "cold acclimation", "type": "BiologicFunction"}]}

Example input:
Sentence: Although alkaloid concentrations were greatly reduced by low temperature this reduction did not occur until after 4 weeks of exposure .

Example answer:
{"entities": [{"text": "alkaloid", "type": "Chemical"}]}

Example input:
Sentence: Neither heating rate nor thermal stress affected plasma sodium and chloride levels , nor the expression of transcripts that included catalase , glucocorticoid receptor , heat shock protein70 ( hsp70 ) , heat shock protein 90α ( hsp90α ) and cytochrome P450 1a ( cyp1a ) .

Example answer:
{"entities": [{"text": "thermal stress", "type": "BiologicFunction"}, {"text": "plasma sodium", "type": "HealthCareActivity"}, {"text": "chloride levels", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "transcripts", "type": "Chemical"}, {"text": "catalase", "type": "Chemical"}, {"text": "glucocorticoid receptor", "type": "Chemical"}, {"text": "heat shock protein70", "type": "Chemical"}, {"text": "hsp70", "type": "Chemical"}, {"text": "heat shock protein 90α", "type": "Chemical"}, {"text": "hsp90α", "type": "Chemical"}, {"text": "cytochrome P450 1a", "type": "Chemical"}, {"text": "cyp1a", "type": "Chemical"}]}

Example input:
Sentence: Pushing the system toward harsher pH ( > 9 ) and temperature ( > 35°C ) conditions , such as those encountered in thermophilic digestion and alkaline treatments , led to more consistent inactivation kinetics among ssRNA and other viruses .

Example answer:
{"entities": [{"text": "digestion", "type": "BiologicFunction"}, {"text": "ssRNA", "type": "Chemical"}, {"text": "viruses", "type": "Virus"}]}

Example input:
Sentence: To the best of our knowledge , this is the first experimental evidence for temperature -dependent herbicide sensitivity based on metabolic detoxification .

Example answer:
{"entities": [{"text": "herbicide", "type": "Chemical"}, {"text": "detoxification", "type": "HealthCareActivity"}]}

Example input:
Sentence: Cofactor - binding loop 2 variants had detrimental effects on specific activity at elevated temperatures , whereas the H192P mutation in cofactor - binding loop 1 resulted in a two - fold improved stability to inactivation at elevated temperatures , and increased the critical onset temperature for aggregation .

Example answer:
{"entities": [{"text": "Cofactor - binding loop 2", "type": "SpatialConcept"}, {"text": "variants", "type": "AnatomicalStructure"}, {"text": "H192P mutation", "type": "BiologicFunction"}, {"text": "cofactor - binding loop 1", "type": "SpatialConcept"}]}

Example input:
Sentence: Under high temperature , a rapid elevation in the level of the intermediate metabolite ( M4 ) was found only in pinoxaden - resistant plants .

Example answer:
{"entities": [{"text": "elevation", "type": "SpatialConcept"}, {"text": "intermediate", "type": "SpatialConcept"}, {"text": "metabolite", "type": "Chemical"}, {"text": "M4", "type": "Chemical"}, {"text": "pinoxaden", "type": "Chemical"}, {"text": "plants", "type": "Eukaryote"}]}

Example input:
Sentence: Responses of several grass weed populations to herbicides that inhibit acetyl - CoA carboxylase ( ACCase ) were examined under different temperature regimes .

Example answer:
{"entities": [{"text": "grass", "type": "Eukaryote"}, {"text": "weed", "type": "Eukaryote"}, {"text": "herbicides", "type": "Chemical"}, {"text": "acetyl - CoA carboxylase", "type": "Chemical"}, {"text": "ACCase", "type": "Chemical"}]}

Input:
Sentence: Decreased sensitivity to ACCase inhibitors was observed under elevated temperatures .
