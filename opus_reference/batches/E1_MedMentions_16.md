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

## Item MedMentions:test:2997
Example input:
Sentence: Upon Fc receptor activation , Src - family kinase signaling leads to segregation of FcγRI and SIRPα nanoclusters to be 197 ± 3 nm apart .

Example answer:
{"entities": [{"text": "Fc receptor", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "Src - family kinase", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "FcγRI", "type": "Chemical"}, {"text": "SIRPα", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , the expression of the muscarinic acetylcholine receptors M2 and M3 ( mAChR M2 and M3 ) at the transcriptional and translational level was recovered in the Lop + Urd treated group , while some markers such as Gα and inositol triphosphate ( IP3 ) in their downstream signaling pathway were completely recovered by Urd treatment .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "muscarinic acetylcholine receptors M2", "type": "Chemical"}, {"text": "M3", "type": "Chemical"}, {"text": "mAChR M2", "type": "Chemical"}, {"text": "transcriptional", "type": "BiologicFunction"}, {"text": "translational", "type": "BiologicFunction"}, {"text": "Lop", "type": "Chemical"}, {"text": "Urd", "type": "Chemical"}, {"text": "treated", "type": "Finding"}, {"text": "markers", "type": "ClinicalAttribute"}, {"text": "Gα", "type": "Chemical"}, {"text": "downstream", "type": "SpatialConcept"}, {"text": "signaling pathway", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: In addition , chronic treatment with 1 , 25 ( OH ) 2D3 protects from aggregated Aβ ( 1 - 42 ) - induced damage in the CA1 region of the rat hippocampus and promotes cell proliferation in the hippocampal dentate gyrus of adult mice .

Example answer:
{"entities": [{"text": "chronic treatment", "type": "HealthCareActivity"}, {"text": "1 , 25 ( OH ) 2D3", "type": "Chemical"}, {"text": "Aβ ( 1 - 42 )", "type": "Chemical"}, {"text": "damage", "type": "InjuryOrPoisoning"}, {"text": "CA1 region", "type": "SpatialConcept"}, {"text": "rat", "type": "Eukaryote"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "cell proliferation", "type": "BiologicFunction"}, {"text": "hippocampal dentate gyrus", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Finally , CB1 receptor s are co - localized with P2X3 receptors in DRG small - diameter neurons and the treatment with ACEA reduced the number of α , β - meATP - responsive cultured DRG neurons .

Example answer:
{"entities": [{"text": "CB1 receptor", "type": "Chemical"}, {"text": "P2X3 receptors", "type": "Chemical"}, {"text": "DRG", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "ACEA", "type": "Chemical"}, {"text": "α , β - meATP", "type": "Chemical"}]}

Example input:
Sentence: uPAR focuses uPA activity at the cell surface and activates intracellular signaling through lateral interactions with integrins , receptor tyrosine kinases and the G - protein - coupled family of fMLF chemotaxis receptors ( FPRs ) .

Example answer:
{"entities": [{"text": "uPAR", "type": "Chemical"}, {"text": "uPA", "type": "Chemical"}, {"text": "activity", "type": "BiologicFunction"}, {"text": "cell surface", "type": "AnatomicalStructure"}, {"text": "activates intracellular signaling", "type": "BiologicFunction"}, {"text": "integrins", "type": "Chemical"}, {"text": "receptor tyrosine kinases", "type": "Chemical"}, {"text": "G - protein - coupled family", "type": "Chemical"}, {"text": "fMLF chemotaxis receptors", "type": "Chemical"}, {"text": "FPRs", "type": "Chemical"}]}

Example input:
Sentence: These results suggest that intracellular Zn ( 2 + ) signaling , which originates in internal stores / proteins , is involved in LTP at perforant pathway - CA1 pyramidal cell synapses .

Example answer:
{"entities": [{"text": "intracellular", "type": "AnatomicalStructure"}, {"text": "Zn ( 2 + )", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "proteins", "type": "Chemical"}, {"text": "LTP", "type": "BiologicFunction"}, {"text": "perforant pathway", "type": "AnatomicalStructure"}, {"text": "CA1 pyramidal cell synapses", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Computational modeling suggests that D2Rs act by modulating interneuron - to - pyramidal signaling .

Example answer:
{"entities": [{"text": "Computational modeling", "type": "ResearchActivity"}, {"text": "D2Rs", "type": "Chemical"}, {"text": "modulating", "type": "SpatialConcept"}, {"text": "interneuron - to - pyramidal signaling", "type": "BiologicFunction"}]}

Example input:
Sentence: Involvement of intracellular Zn ( 2 + ) signaling in LTP at perforant pathway - CA1 pyramidal cell synapse Physiological significance of synaptic Zn ( 2 + ) signaling was examined at perforant pathway - CA1 pyramidal cell synapses .

Example answer:
{"entities": [{"text": "intracellular", "type": "AnatomicalStructure"}, {"text": "Zn ( 2 + )", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "LTP", "type": "BiologicFunction"}, {"text": "perforant pathway", "type": "AnatomicalStructure"}, {"text": "CA1 pyramidal cell synapse", "type": "AnatomicalStructure"}, {"text": "synaptic Zn ( 2 + ) signaling", "type": "BiologicFunction"}, {"text": "CA1 pyramidal cell synapses", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Using the activatory Gq - coupled human M3 muscarinic receptor ( hM3Dq ) , we found that chemogenetic stimulation of dSPNs mimicked , while stimulation of iSPNs abolished the therapeutic action of L - DOPA in PD mice .

Example answer:
{"entities": [{"text": "activatory Gq - coupled human M3 muscarinic receptor", "type": "Chemical"}, {"text": "hM3Dq", "type": "Chemical"}, {"text": "chemogenetic stimulation", "type": "BiologicFunction"}, {"text": "dSPNs", "type": "AnatomicalStructure"}, {"text": "stimulation", "type": "BiologicFunction"}, {"text": "iSPNs", "type": "AnatomicalStructure"}, {"text": "therapeutic action", "type": "BiologicFunction"}, {"text": "L - DOPA", "type": "Chemical"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Notably , we found that 1 , 25 ( OH ) 2D3 prevents the reduction of S1P1 expression promoted by Aβ ( 1 - 42 ) and thereby it modulates the downstream signaling leading to ER stress damage ( p38MAPK / ATF4 ) .

Example answer:
{"entities": [{"text": "1 , 25 ( OH ) 2D3", "type": "Chemical"}, {"text": "S1P1", "type": "Chemical"}, {"text": "Aβ ( 1 - 42 )", "type": "Chemical"}, {"text": "downstream signaling", "type": "BiologicFunction"}, {"text": "ER stress damage", "type": "BiologicFunction"}, {"text": "p38MAPK", "type": "Chemical"}, {"text": "ATF4", "type": "Chemical"}]}

Input:
Sentence: We have also studied the crosstalk between 1 , 25 ( OH ) 2D3 and S1P signaling pathways downstream to the activation of S1P receptor subtype S1P1 .

## Item MedMentions:test:2934
Example input:
Sentence: However , mean operative time was significantly longer for junior residents ( n = 27 ; 115 ± 24 min ) compared to senior residents ( n = 37 ; 77 ± 35 min ) and attending surgeons ( n = 66 ; 55 ± 17 min ) ( P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "junior residents", "type": "ProfessionalOrOccupationalGroup"}, {"text": "senior residents", "type": "ProfessionalOrOccupationalGroup"}, {"text": "surgeons", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: We prospectively collected geriatric ( age > 65 ) emergency general surgery patients for 1 - year .

Example answer:
{"entities": []}

Example input:
Sentence: The median age at surgery was 12 months ( 5 - 151 months ) , and the average follow - up was 17 . 3 months .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: If these rates remain constant over time , the average surgeon would perform 1 . 8 ( SD = 1 . 7 ) splenectomies and 0 . 6 ( SD = 1 . 1 ) splenorrhaphies for trauma over a 30 - year surgical career .

Example answer:
{"entities": [{"text": "surgeon", "type": "ProfessionalOrOccupationalGroup"}, {"text": "splenectomies", "type": "HealthCareActivity"}, {"text": "splenorrhaphies", "type": "HealthCareActivity"}, {"text": "trauma", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Anesthesia for Ambulatory Pediatric Surgery in Sub - Saharan Africa : A Pilot Study in Burkina Faso Long surgical wait times and limited hospital capacity are common obstacles to surgical care in many countries in Sub - Saharan Africa ( SSA ) .

Example answer:
{"entities": [{"text": "Anesthesia", "type": "Chemical"}, {"text": "Ambulatory Pediatric Surgery", "type": "HealthCareActivity"}, {"text": "Sub - Saharan Africa", "type": "SpatialConcept"}, {"text": "Pilot Study", "type": "ResearchActivity"}, {"text": "Burkina Faso", "type": "SpatialConcept"}, {"text": "surgical care", "type": "HealthCareActivity"}, {"text": "countries", "type": "SpatialConcept"}, {"text": "SSA", "type": "SpatialConcept"}]}

Example input:
Sentence: Further improvements were detected at 24 months ( AOFAS , from 57 . 1 ± 14 . 9 before surgery to 86 . 6 ± 10 .

Example answer:
{"entities": [{"text": "AOFAS", "type": "IntellectualProduct"}]}

Example input:
Sentence: All adult patients scheduled for elective foot or ankle surgery by 1 of 6 orthopaedic foot and ankle surgeons were screened for inclusion over 8 months .

Example answer:
{"entities": [{"text": "foot", "type": "HealthCareActivity"}, {"text": "ankle surgery", "type": "HealthCareActivity"}, {"text": "orthopaedic foot and ankle surgeons", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: The mean follow - up period was 46 . 7 months , and the mean age at the time of surgery was 60 . 7 years .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: One hundred fourteen patients ( age range , 2 - 65 years ; American Society of Anesthesiology class I - II ) participated in this study , willing to be sedated and to undergo spinal anesthesia .

Example answer:
{"entities": [{"text": "patients", "type": "Chemical"}, {"text": "American Society of Anesthesiology class I - II", "type": "Organization"}, {"text": "study", "type": "ResearchActivity"}, {"text": "spinal anesthesia", "type": "HealthCareActivity"}]}

Example input:
Sentence: During the study period , a total of 1250 patients underwent surgery , of whom 515 were elective cases ; 115 of these met the criteria for ambulatory surgery ; 103 patients , with an average age of 59 . 74 ± 41 . 57 months , actually underwent surgery .

Example answer:
{"entities": [{"text": "met the criteria", "type": "Finding"}, {"text": "ambulatory surgery", "type": "HealthCareActivity"}, {"text": "underwent surgery", "type": "BiomedicalOccupationOrDiscipline"}]}

Input:
Sentence: Eligibility criteria for the ambulatory surgery program included > 1 year of age , American Society of Anesthesiologists ( ASA ) 1 status , surgery with a low risk of bleeding , lasting < 90 minutes , and with an expectation of mild to moderate postoperative pain .

## Item MedMentions:test:3095
Example input:
Sentence: In 64 % ( 122 / 191 ) of the clinically healthy Labrador retrievers , hepatic histology revealed inflammatory infiltrates .

Example answer:
{"entities": [{"text": "Labrador retrievers", "type": "Eukaryote"}, {"text": "hepatic histology", "type": "Finding"}, {"text": "inflammatory infiltrates", "type": "Finding"}]}

Example input:
Sentence: The tissue histology showed a chronic inflammatory cell infiltrate associated with the MTA .

Example answer:
{"entities": [{"text": "tissue", "type": "AnatomicalStructure"}, {"text": "histology", "type": "HealthCareActivity"}, {"text": "inflammatory cell infiltrate", "type": "BodySubstance"}, {"text": "MTA", "type": "Chemical"}]}

Example input:
Sentence: We observed a reduction of 84 % in blood eosinophilia and a decrease in the IL - 4 and IL - 10 blood levels after treatment .

Example answer:
{"entities": [{"text": "reduction", "type": "HealthCareActivity"}, {"text": "blood eosinophilia", "type": "BiologicFunction"}, {"text": "IL - 4", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "blood levels", "type": "BodySubstance"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Blood eosinophils from children and adults with EoE , and healthy controls , were analyzed with flow cytometry regarding levels of CD23 , CD44 , CD54 , CRTH2 , FOXP3 , and galectin - 10 .

Example answer:
{"entities": [{"text": "Blood eosinophils", "type": "AnatomicalStructure"}, {"text": "EoE", "type": "BiologicFunction"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "flow cytometry", "type": "HealthCareActivity"}, {"text": "CD23", "type": "Chemical"}, {"text": "CD44", "type": "Chemical"}, {"text": "CD54", "type": "Chemical"}, {"text": "CRTH2", "type": "Chemical"}, {"text": "galectin - 10", "type": "Chemical"}]}

Example input:
Sentence: Perivascular fat monocyte / macrophage infiltration was higher in eET - 1 and smPparγ and increased further in eET - 1 / smPparγ .

Example answer:
{"entities": [{"text": "Perivascular", "type": "SpatialConcept"}, {"text": "fat monocyte", "type": "AnatomicalStructure"}, {"text": "macrophage", "type": "AnatomicalStructure"}, {"text": "infiltration", "type": "BiologicFunction"}, {"text": "eET - 1", "type": "Chemical"}, {"text": "smPparγ", "type": "Chemical"}]}

Example input:
Sentence: Double labeling immunohistochemical staining revealed that IFN - λ1 ( + ) inflammatory cells such as mast cells , eosinophils , B cells , neutrophils , and macrophages were mainly located in dermis , whereas epidermis tissue highly expressed IFN - λ1 .

Example answer:
{"entities": [{"text": "IFN - λ1", "type": "Chemical"}, {"text": "inflammatory cells", "type": "AnatomicalStructure"}, {"text": "mast cells", "type": "AnatomicalStructure"}, {"text": "eosinophils", "type": "AnatomicalStructure"}, {"text": "B cells", "type": "AnatomicalStructure"}, {"text": "neutrophils", "type": "AnatomicalStructure"}, {"text": "macrophages", "type": "AnatomicalStructure"}, {"text": "located", "type": "SpatialConcept"}, {"text": "dermis", "type": "AnatomicalStructure"}, {"text": "epidermis tissue", "type": "AnatomicalStructure"}, {"text": "expressed", "type": "BiologicFunction"}]}

Example input:
Sentence: E / I LF differentiated between the " Low inflammation " and " Eosinophilic type " groups ( p = 0 . 006 ) .

Example answer:
{"entities": [{"text": "inflammation", "type": "BiologicFunction"}, {"text": "Eosinophilic", "type": "Finding"}]}

Example input:
Sentence: FeNO differentiated between the " Low inflammation " and " Eosinophilic type " groups , " Low inflammation " and " Neutrophilic type " groups , and " Neutrophilic type " and " Mixed type " ( p < 0 . 0001 , p = 0 .

Example answer:
{"entities": [{"text": "inflammation", "type": "BiologicFunction"}, {"text": "Eosinophilic", "type": "Finding"}, {"text": "Neutrophilic", "type": "BiologicFunction"}]}

Example input:
Sentence: E / I LF could distinguish the " Mixed type " group from the " Low inflammation " and " Eosinophilic type " groups ( p = 0 . 002 ) .

Example answer:
{"entities": [{"text": "inflammation", "type": "BiologicFunction"}, {"text": "Eosinophilic", "type": "Finding"}]}

Example input:
Sentence: An association was found between the eosinophilic infiltrate and clinical scores of greater severity ( p = 0 . 002 ) .

Example answer:
{"entities": [{"text": "eosinophilic infiltrate", "type": "BodySubstance"}]}

Input:
Sentence: Inflammatory infiltrates were divided in eosinophilic ( 46 . 30 % ) , neutrophilic and mixed .

## Item MedMentions:test:2944
Example input:
Sentence: From 2011 to 2015 , one hundred and three patients were enrolled in a prospective randomized controlled trial evaluating the use of PR in the treatment of patients undergoing damage control surgery compared with conventional resuscitation ( CR ) alone .

Example answer:
{"entities": [{"text": "randomized controlled trial", "type": "ResearchActivity"}, {"text": "evaluating", "type": "HealthCareActivity"}, {"text": "PR", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "damage control surgery", "type": "HealthCareActivity"}, {"text": "conventional", "type": "HealthCareActivity"}, {"text": "resuscitation", "type": "HealthCareActivity"}, {"text": "CR", "type": "HealthCareActivity"}]}

Example input:
Sentence: A standardised strategy of periprocedural anticoagulation was adopted in both groups as well as the use of a single suture - based closure device .

Example answer:
{"entities": [{"text": "periprocedural anticoagulation", "type": "HealthCareActivity"}, {"text": "single suture - based closure device", "type": "MedicalDevice"}]}

Example input:
Sentence: Ultrasound - guided pericardiocentesis : a novel parasternal approach The aim of this study was to evaluate a novel pericardiocentesis technique using an in - plane parasternal medial -to - lateral approach with the use of a high - frequency probe in patients with cardiac tamponade .

Example answer:
{"entities": [{"text": "Ultrasound - guided", "type": "HealthCareActivity"}, {"text": "pericardiocentesis", "type": "HealthCareActivity"}, {"text": "parasternal", "type": "SpatialConcept"}, {"text": "study", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "medial", "type": "SpatialConcept"}, {"text": "lateral", "type": "SpatialConcept"}, {"text": "probe", "type": "MedicalDevice"}, {"text": "cardiac tamponade", "type": "BiologicFunction"}]}

Example input:
Sentence: This is the first large randomised controlled trial comparing the two most frequently used anaesthetic techniques in remedial surgery for groin pain .

Example answer:
{"entities": [{"text": "randomised controlled trial", "type": "ResearchActivity"}, {"text": "anaesthetic techniques", "type": "HealthCareActivity"}, {"text": "remedial surgery", "type": "HealthCareActivity"}, {"text": "groin pain", "type": "Finding"}]}

Example input:
Sentence: In this analysis , we sought to assess the impact of a modified femoral artery puncture technique using digital subtraction angiography ( DSA ) and road mapping during transfemoral TAVI on periprocedural vascular and bleeding events .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "femoral artery", "type": "AnatomicalStructure"}, {"text": "puncture", "type": "HealthCareActivity"}, {"text": "digital subtraction angiography", "type": "HealthCareActivity"}, {"text": "DSA", "type": "HealthCareActivity"}, {"text": "TAVI", "type": "HealthCareActivity"}, {"text": "periprocedural", "type": "BiologicFunction"}, {"text": "vascular", "type": "AnatomicalStructure"}, {"text": "bleeding", "type": "BiologicFunction"}]}

Example input:
Sentence: In all patients , a percutaneous transluminal angioplasty balloon was used to predilate the scar tissue and the femoral artery or the synthetic vascular graft after preclosing ( ProGlide ® ; Abbott Vascular , Santa Clara , CA , USA ) .

Example answer:
{"entities": [{"text": "percutaneous transluminal angioplasty balloon", "type": "HealthCareActivity"}, {"text": "predilate", "type": "HealthCareActivity"}, {"text": "scar tissue", "type": "Finding"}, {"text": "femoral artery", "type": "AnatomicalStructure"}, {"text": "preclosing", "type": "HealthCareActivity"}, {"text": "ProGlide ®", "type": "MedicalDevice"}, {"text": "Santa Clara , CA", "type": "SpatialConcept"}, {"text": "USA", "type": "SpatialConcept"}]}

Example input:
Sentence: For the first time , a pericardiocentesis approach with a medial - to - lateral needle trajectory and real - time , in - plane , needle visualization was performed in a tamponade patient population .This is an open - access article distributed under the terms of the Creative Commons Attribution - Non Commercial - No Derivatives License 4 . 0 ( CCBY - NC - ND ) , where it is permissible to download and share the work provided it is properly cited .

Example answer:
{"entities": [{"text": "pericardiocentesis", "type": "HealthCareActivity"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "medial - to - lateral", "type": "SpatialConcept"}, {"text": "needle", "type": "MedicalDevice"}, {"text": "tamponade", "type": "BiologicFunction"}]}

Example input:
Sentence: Conclusions Percutaneous access in redo groins with scar tissue and / or synthetic vascular graft using ultrasound - guided punction , preclosing with ProGlide ® system and predilation with percutaneous transluminal angioplasty balloon to introduce large size sheath as used for endovascular aortic repair showed to be feasible , safe and with few local complications .

Example answer:
{"entities": [{"text": "Percutaneous access", "type": "SpatialConcept"}, {"text": "redo groins", "type": "SpatialConcept"}, {"text": "scar tissue", "type": "Finding"}, {"text": "ultrasound - guided punction", "type": "MedicalDevice"}, {"text": "preclosing", "type": "HealthCareActivity"}, {"text": "ProGlide ® system", "type": "MedicalDevice"}, {"text": "predilation", "type": "HealthCareActivity"}, {"text": "percutaneous transluminal angioplasty balloon", "type": "HealthCareActivity"}, {"text": "large size", "type": "Finding"}, {"text": "sheath", "type": "MedicalDevice"}, {"text": "endovascular aortic repair", "type": "HealthCareActivity"}, {"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: Predilation technique with balloon angioplasty to facilitate percutaneous groin access of large size sheath through scar tissue Purpose Percutaneous remote access for endovascular aortic repair is an advantageous alternative to open access .

Example answer:
{"entities": [{"text": "Predilation technique", "type": "HealthCareActivity"}, {"text": "balloon angioplasty", "type": "HealthCareActivity"}, {"text": "percutaneous groin", "type": "SpatialConcept"}, {"text": "access", "type": "SpatialConcept"}, {"text": "large size", "type": "Finding"}, {"text": "sheath", "type": "MedicalDevice"}, {"text": "scar tissue", "type": "Finding"}, {"text": "Percutaneous remote access", "type": "SpatialConcept"}, {"text": "endovascular aortic repair", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of this study was to evaluate an original technique used for enabling percutaneous remote access for thoracic or abdominal endovascular aortic repair in patients with scar tissue and / or a vascular graft in the groin .

Example answer:
{"entities": [{"text": "percutaneous remote access", "type": "SpatialConcept"}, {"text": "thoracic", "type": "HealthCareActivity"}, {"text": "abdominal endovascular aortic repair", "type": "HealthCareActivity"}, {"text": "scar tissue", "type": "Finding"}, {"text": "groin", "type": "SpatialConcept"}]}

Input:
Sentence: Methods Twenty - five consecutive patients with a thoracic ( 11 / 25 ; 44 % ) or an aortic aneurysm ( 14 / 25 ; 66 % ) and with a synthetic vascular graft in the groin ( 16 / 25 ; 64 % ) or a redo groin access ( 9 / 25 ; 36 % ) were managed through the percutaneous remote access .

## Item MedMentions:test:3089
Example input:
Sentence: Cognitive impairment was defined as a total Montreal Cognitive Assessment tool score ≤24 / 30 .

Example answer:
{"entities": [{"text": "Cognitive impairment", "type": "BiologicFunction"}, {"text": "Montreal Cognitive Assessment tool", "type": "IntellectualProduct"}]}

Example input:
Sentence: Neuropsychological testing did not suggest true regression in cognitive , language , and academic skills , although decreases in motivation and performance were noted with a reaction to stress and multiple environmental changes as a potential causative factor .

Example answer:
{"entities": [{"text": "Neuropsychological testing", "type": "HealthCareActivity"}, {"text": "regression", "type": "BiologicFunction"}, {"text": "academic skills", "type": "BiologicFunction"}, {"text": "motivation", "type": "BiologicFunction"}, {"text": "stress", "type": "Finding"}, {"text": "environmental", "type": "SpatialConcept"}]}

Example input:
Sentence: We used an interval timing task to study elementary cognitive processing that requires both frontal and cerebellar networks that are disrupted in patients with schizophrenia .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "cognitive processing", "type": "BiologicFunction"}, {"text": "frontal", "type": "AnatomicalStructure"}, {"text": "cerebellar networks", "type": "AnatomicalStructure"}, {"text": "schizophrenia", "type": "BiologicFunction"}]}

Example input:
Sentence: 85 ; 95 % confidence intervals , 1 . 09 - 3 . 12 ) among cognitively impaired individuals .

Example answer:
{"entities": [{"text": "cognitively impaired", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: Hippocampal and deep GM nuclei atrophy were the best predictors of cognitive impairment , while WM atrophy was the best predictor of disability .

Example answer:
{"entities": [{"text": "Hippocampal", "type": "AnatomicalStructure"}, {"text": "deep GM", "type": "AnatomicalStructure"}, {"text": "nuclei", "type": "AnatomicalStructure"}, {"text": "atrophy", "type": "BiologicFunction"}, {"text": "cognitive impairment", "type": "BiologicFunction"}, {"text": "WM", "type": "AnatomicalStructure"}, {"text": "disability", "type": "BiologicFunction"}]}

Example input:
Sentence: Neuropsychological tests were carried out using the AD Assessment Scale - cognitive subscale ( ADAS - cog ) , Mini - Mental State Examination ( MMSE ) , Montreal Cognitive Assessment ( MoCA ) , and World Health Organization University of California - Los Angeles , Auditory Verbal Learning Test ( WHO - UCLA AVLT ) before , immediately after , and 6 weeks after the intervention .

Example answer:
{"entities": [{"text": "Neuropsychological tests", "type": "HealthCareActivity"}, {"text": "AD Assessment Scale", "type": "IntellectualProduct"}, {"text": "cognitive subscale", "type": "IntellectualProduct"}, {"text": "ADAS", "type": "IntellectualProduct"}, {"text": "cog", "type": "IntellectualProduct"}, {"text": "Mini - Mental State Examination", "type": "HealthCareActivity"}, {"text": "MMSE", "type": "HealthCareActivity"}, {"text": "Montreal Cognitive Assessment", "type": "IntellectualProduct"}, {"text": "MoCA", "type": "IntellectualProduct"}, {"text": "World Health Organization University of California - Los Angeles , Auditory Verbal Learning Test", "type": "IntellectualProduct"}, {"text": "WHO - UCLA AVLT", "type": "IntellectualProduct"}, {"text": "intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: The patients with MCI or AD underwent clinical and neuropsychological tests at baseline and once every year thereafter for 2 years .

Example answer:
{"entities": [{"text": "MCI", "type": "BiologicFunction"}, {"text": "AD", "type": "BiologicFunction"}, {"text": "neuropsychological tests", "type": "HealthCareActivity"}]}

Example input:
Sentence: Twenty - three patients ( 38 % ) were cognitively impaired .

Example answer:
{"entities": [{"text": "cognitively impaired", "type": "BiologicFunction"}]}

Example input:
Sentence: Compared to cognitively preserved ( CP ) , CI patients had higher T2 WM lesion volume ( LV ) , lower NBV and GMV , and more severe diffusivity abnormalities in WM lesions , cortex , and NAWM .

Example answer:
{"entities": [{"text": "CI", "type": "BiologicFunction"}, {"text": "abnormalities", "type": "AnatomicalStructure"}, {"text": "WM lesions", "type": "Finding"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "NAWM", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Patients with at least 2 neuropsychological tests with abnormal findings were considered cognitively impaired .

Example answer:
{"entities": [{"text": "neuropsychological tests", "type": "HealthCareActivity"}, {"text": "abnormal findings", "type": "Finding"}, {"text": "cognitively impaired", "type": "BiologicFunction"}]}

Input:
Sentence: Cognitively impaired ( CI ) patients had ⩾2 abnormal neuropsychological tests .

## Item MedMentions:test:2841
Example input:
Sentence: We found substantial individual variation in resistance and tolerance to the fungal pathogen Metarhizium anisopliae Ma549 using the Drosophila melanogaster Genetic Reference Panel ( DGRP ) .

Example answer:
{"entities": [{"text": "individual", "type": "PopulationGroup"}, {"text": "resistance", "type": "BiologicFunction"}, {"text": "fungal pathogen Metarhizium anisopliae Ma549", "type": "Eukaryote"}, {"text": "Drosophila melanogaster Genetic Reference Panel", "type": "Eukaryote"}, {"text": "DGRP", "type": "Eukaryote"}]}

Example input:
Sentence: Insecticidal effects of deltamethrin in laboratory and field populations of Culicoides species : how effective are host - contact reduction methods in India ? Bluetongue virus ( BTV ) is transmitted by Culicoides biting midges and causes bluetongue ( BT ) , a clinical disease observed primarily in sheep .

Example answer:
{"entities": [{"text": "deltamethrin", "type": "Chemical"}, {"text": "laboratory", "type": "Organization"}, {"text": "Culicoides species", "type": "Eukaryote"}, {"text": "methods", "type": "ResearchActivity"}, {"text": "India", "type": "SpatialConcept"}, {"text": "Bluetongue virus", "type": "Virus"}, {"text": "BTV", "type": "Virus"}, {"text": "transmitted", "type": "BiologicFunction"}, {"text": "Culicoides", "type": "Eukaryote"}, {"text": "biting midges", "type": "Eukaryote"}, {"text": "bluetongue", "type": "BiologicFunction"}, {"text": "BT", "type": "BiologicFunction"}, {"text": "clinical disease", "type": "BiologicFunction"}, {"text": "sheep", "type": "Eukaryote"}]}

Example input:
Sentence: Ultra - low activities of a common radioisotope for permission -free tracking of a drosophilid fly in its natural habitat Knowledge of a species ' ecology , including its movement in time and space , is key for many questions in biology and conservation .

Example answer:
{"entities": [{"text": "radioisotope", "type": "Chemical"}, {"text": "tracking", "type": "SpatialConcept"}, {"text": "drosophilid fly", "type": "Eukaryote"}, {"text": "natural habitat", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "movement", "type": "BiologicFunction"}, {"text": "space", "type": "SpatialConcept"}, {"text": "biology", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: A relatively new method to detect likely transmission involves molecular testing for phytoplasma DNA in sucrose solution that insects have fed upon .

Example answer:
{"entities": [{"text": "molecular testing", "type": "HealthCareActivity"}, {"text": "phytoplasma", "type": "Bacterium"}, {"text": "DNA", "type": "Chemical"}, {"text": "sucrose", "type": "Chemical"}, {"text": "insects", "type": "Eukaryote"}]}

Example input:
Sentence: Use of grape berries in bioassays made it possible to assess effects of an insecticide present on a fruit 's surface on oviposition and larval hatch from eggs .

Example answer:
{"entities": [{"text": "grape berries", "type": "Food"}, {"text": "bioassays", "type": "HealthCareActivity"}, {"text": "insecticide", "type": "Chemical"}, {"text": "fruit 's", "type": "Food"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "oviposition", "type": "BiologicFunction"}, {"text": "larval", "type": "Eukaryote"}, {"text": "hatch", "type": "BiologicFunction"}, {"text": "eggs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Suitability of our bioassays was validated in an assessment of the efficacy of four bioinsecticides and one synthetic insecticide against various developmental stages of D .

Example answer:
{"entities": [{"text": "bioassays", "type": "HealthCareActivity"}, {"text": "validated", "type": "ResearchActivity"}, {"text": "bioinsecticides", "type": "Chemical"}, {"text": "insecticide", "type": "Chemical"}, {"text": "developmental", "type": "BiologicFunction"}, {"text": "D .", "type": "Eukaryote"}]}

Example input:
Sentence: suzukii larvae and the fact that fruits used in bioassays often start to rot and dissolve before larvae have reached the adult stage .

Example answer:
{"entities": [{"text": "suzukii", "type": "Eukaryote"}, {"text": "larvae", "type": "Eukaryote"}, {"text": "fruits", "type": "Food"}, {"text": "bioassays", "type": "HealthCareActivity"}]}

Example input:
Sentence: Number of adult flies was significantly reduced if the bioassay medium was treated with an azadirachtin A containing insecticide both before or after egg deposition .

Example answer:
{"entities": [{"text": "flies", "type": "Eukaryote"}, {"text": "bioassay", "type": "HealthCareActivity"}, {"text": "azadirachtin A", "type": "Chemical"}, {"text": "insecticide", "type": "Chemical"}]}

Example input:
Sentence: Insecticides tested in these three different bioassays with acetamiprid , spinosad or natural pyrethrins as active ingredients achieved a significant D .

Example answer:
{"entities": [{"text": "Insecticides", "type": "Chemical"}, {"text": "bioassays", "type": "HealthCareActivity"}, {"text": "acetamiprid", "type": "Chemical"}, {"text": "spinosad", "type": "Chemical"}, {"text": "pyrethrins", "type": "Chemical"}, {"text": "achieved", "type": "Finding"}, {"text": "D .", "type": "Eukaryote"}]}

Example input:
Sentence: suzukii Water - apple juice agar used as a bioassay substrate allowed egg counting and observation of larval development due to its transparency , while apple - nutrition medium allowed complete metamorphosis .

Example answer:
{"entities": [{"text": "suzukii", "type": "Eukaryote"}, {"text": "Water - apple juice agar", "type": "Chemical"}, {"text": "bioassay", "type": "HealthCareActivity"}, {"text": "egg counting", "type": "HealthCareActivity"}, {"text": "larval development", "type": "BiologicFunction"}, {"text": "apple - nutrition medium", "type": "Chemical"}, {"text": "metamorphosis", "type": "BiologicFunction"}]}

Input:
Sentence: Laboratory Bioassays with Three Different Substrates to Test the Efficacy of Insecticides against Various Stages of Drosophila suzukii ( Diptera : Drosophilidae ) Rapid worldwide spread and polyphagous nature of the spotted wing Drosophila Drosophila suzukii Matsumura ( Diptera : Drosophilidae ) calls for efficient and selective control strategies to prevent severe economic losses in various fruit crops .

## Item MedMentions:test:3160
Example input:
Sentence: These include pain after stenting ( 38 % ) , stent obstruction ( 23 % ) and stent migration ( 6 % ) .

Example answer:
{"entities": [{"text": "pain", "type": "Finding"}, {"text": "stenting", "type": "HealthCareActivity"}, {"text": "stent obstruction", "type": "BiologicFunction"}, {"text": "stent migration", "type": "BiologicFunction"}]}

Example input:
Sentence: Plaque with thickness ≥5 mm was present ipsilateral to stroke in 11 % of patients , and contralateral in 1 % ( 9 / 85 vs 1 / 85 ; p = 0 . 008 ) .

Example answer:
{"entities": [{"text": "Plaque", "type": "AnatomicalStructure"}, {"text": "ipsilateral", "type": "SpatialConcept"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "contralateral", "type": "SpatialConcept"}]}

Example input:
Sentence: Plaque with thickness ≥4 mm was present ipsilateral to stroke in 19 % of patients , and contralateral in 5 % ( 16 / 85 vs 4 / 85 ; p = 0 . 002 ) .

Example answer:
{"entities": [{"text": "Plaque", "type": "AnatomicalStructure"}, {"text": "ipsilateral", "type": "SpatialConcept"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "contralateral", "type": "SpatialConcept"}]}

Example input:
Sentence: Plaque with thickness ≥3 mm was present ipsilateral to stroke in 35 % of patients , and contralateral in 15 % ( 30 / 85 vs 13 / 85 ; p = 0 . 001 ) .

Example answer:
{"entities": [{"text": "Plaque", "type": "AnatomicalStructure"}, {"text": "ipsilateral", "type": "SpatialConcept"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "contralateral", "type": "SpatialConcept"}]}

Example input:
Sentence: An increase in cortical thickness at the hemisphere contralateral to the lesion ( CLH ) was detected in motor and language areas , which may reflect compensation for the gray matter loss in the lesion area or retention of ipsilateral pathways .

Example answer:
{"entities": [{"text": "cortical", "type": "AnatomicalStructure"}, {"text": "hemisphere", "type": "AnatomicalStructure"}, {"text": "contralateral", "type": "SpatialConcept"}, {"text": "lesion", "type": "Finding"}, {"text": "CLH", "type": "AnatomicalStructure"}, {"text": "detected", "type": "Finding"}, {"text": "motor", "type": "SpatialConcept"}, {"text": "language areas", "type": "SpatialConcept"}, {"text": "gray matter", "type": "AnatomicalStructure"}, {"text": "area", "type": "SpatialConcept"}, {"text": "ipsilateral", "type": "SpatialConcept"}]}

Example input:
Sentence: Steel stent showed the lowest foreshortening and fully expansion pressure but the difference was much lower than that the one for dogboning .

Example answer:
{"entities": [{"text": "Steel", "type": "Chemical"}, {"text": "stent", "type": "MedicalDevice"}, {"text": "foreshortening", "type": "Finding"}]}

Example input:
Sentence: Assessment of Vascular Stent Heating with Repetitive Transcranial Magnetic Stimulation A high proportion of patients with stroke do not qualify for repetitive transcranial magnetic stimulation ( rTMS ) clinical studies due to the presence of metallic stents .

Example answer:
{"entities": [{"text": "Assessment", "type": "HealthCareActivity"}, {"text": "Vascular Stent", "type": "MedicalDevice"}, {"text": "Repetitive Transcranial Magnetic Stimulation", "type": "HealthCareActivity"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "repetitive transcranial magnetic stimulation", "type": "HealthCareActivity"}, {"text": "rTMS", "type": "HealthCareActivity"}, {"text": "clinical studies", "type": "ResearchActivity"}, {"text": "metallic stents", "type": "MedicalDevice"}]}

Example input:
Sentence: In our method , stents were tested in gelled saline at 2 different locations : at the center and at the lobe of the coil .

Example answer:
{"entities": [{"text": "stents", "type": "MedicalDevice"}, {"text": "tested", "type": "IntellectualProduct"}, {"text": "locations", "type": "SpatialConcept"}, {"text": "at the center", "type": "SpatialConcept"}, {"text": "lobe", "type": "AnatomicalStructure"}, {"text": "coil", "type": "MedicalDevice"}]}

Example input:
Sentence: We have found that heating of stents was well below the Food and Drug Administration standards of 2°C .

Example answer:
{"entities": [{"text": "stents", "type": "MedicalDevice"}, {"text": "Food and Drug Administration", "type": "Organization"}, {"text": "standards", "type": "IntellectualProduct"}]}

Example input:
Sentence: We found that stents did not heat to more than 1°C with either 1 Hz rTMS or 10 Hz rTMS in any configuration or orientation .

Example answer:
{"entities": [{"text": "stents", "type": "MedicalDevice"}, {"text": "rTMS", "type": "HealthCareActivity"}, {"text": "orientation", "type": "SpatialConcept"}]}

Input:
Sentence: Heating in general was greater at the lobe when the stent was oriented perpendicularly .

## Item MedMentions:test:3198
Example input:
Sentence: Quality of nursing intensity data : inter - rater reliability of the patient classification after two decades in clinical use The aim of this study was to measure the inter - rater reliability of the Oulu Patient Classification and to discuss existing methods of reliability testing .

Example answer:
{"entities": [{"text": "nursing intensity data", "type": "IntellectualProduct"}, {"text": "classification", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "Oulu Patient Classification", "type": "IntellectualProduct"}]}

Example input:
Sentence: Despite highlighting good intra - and inter - operator reproducibility , we found that a scale bias between instruments might interfere with thorough CCT monitoring .

Example answer:
{"entities": [{"text": "scale", "type": "IntellectualProduct"}, {"text": "instruments", "type": "MedicalDevice"}, {"text": "CCT", "type": "ClinicalAttribute"}, {"text": "monitoring", "type": "HealthCareActivity"}]}

Example input:
Sentence: Interobserver repeatability was also high in this measure , ranging from r = .74 to r = .96 .

Example answer:
{"entities": []}

Example input:
Sentence: Inter - and intra - observer reproducibility of CT -derived ILD measures was excellent .

Example answer:
{"entities": [{"text": "CT", "type": "HealthCareActivity"}]}

Example input:
Sentence: The inter - rater agreement ( k ) between local and central pathology was calculated for Ki - 67 , grading , hormone receptors ( ER / PgR ) and HER2 / neu .

Example answer:
{"entities": [{"text": "central pathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Ki - 67", "type": "Chemical"}, {"text": "grading", "type": "IntellectualProduct"}, {"text": "hormone receptors", "type": "Chemical"}, {"text": "ER", "type": "Chemical"}, {"text": "PgR", "type": "Chemical"}, {"text": "HER2 / neu", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Intra - and inter - observer reproducibility and scan - rescan reproducibility were evaluated using intra - class correlation coefficients ( ICCs ) and coefficient of variation ( CoV ) .

Example answer:
{"entities": []}

Example input:
Sentence: Internal consistency , inter - rater reliability , and convergent validity were examined for the VSS and patient satisfaction scoring .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "VSS", "type": "IntellectualProduct"}, {"text": "patient satisfaction scoring", "type": "IntellectualProduct"}]}

Example input:
Sentence: 8 ; inter - rater reliability resulted in a reliability coefficient of 0 .

Example answer:
{"entities": []}

Example input:
Sentence: To test inter - rater reliability , a pair of nurses classified the same patients , without knowledge of each other 's ratings , as a part of annually conducted standardization .

Example answer:
{"entities": [{"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "classified", "type": "IntellectualProduct"}, {"text": "standardization", "type": "ResearchActivity"}]}

Example input:
Sentence: Inter - rater reliability coefficients were a reliable or almost perfect means of considering the nursing intensity category and various practices , but there were detectable differences between subareas .

Example answer:
{"entities": [{"text": "nursing", "type": "HealthCareActivity"}, {"text": "category", "type": "IntellectualProduct"}, {"text": "detectable", "type": "Finding"}]}

Input:
Sentence: All assessments were made by two raters ; inter - rater and intra - rater reliability was acceptable .

## Item MedMentions:test:2897
Example input:
Sentence: Frequency distribution of interleukin - 10 haplotypes ( -1082 A > G , -819 C > T , and -592 C > A ) in a Mexican population Interleukin 10 ( IL - 10 ) is an immunoregulatory cytokine with multiple roles in the immune system .

Example answer:
{"entities": [{"text": "interleukin - 10", "type": "AnatomicalStructure"}, {"text": "-1082 A > G", "type": "SpatialConcept"}, {"text": "-819 C > T", "type": "SpatialConcept"}, {"text": "-592 C > A", "type": "SpatialConcept"}, {"text": "Mexican", "type": "PopulationGroup"}, {"text": "population", "type": "PopulationGroup"}, {"text": "Interleukin 10", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "immunoregulatory cytokine", "type": "Chemical"}, {"text": "immune system", "type": "BodySystem"}]}

Example input:
Sentence: Forty patients with chronic HCV ( 80 % with cirrhosis ) were enrolled in the study , 28 received triple therapy ( Group A ) with pegylated - interferon and ribavirin for 4 weeks followed by the addition of a PI ( telaprevir , boceprevir or simeprevir ) , and 12 patients received an interferon -free regimen ( Group B ) with simeprevir and sofosbuvir .

Example answer:
{"entities": [{"text": "chronic HCV", "type": "BiologicFunction"}, {"text": "cirrhosis", "type": "BiologicFunction"}, {"text": "triple therapy", "type": "HealthCareActivity"}, {"text": "Group A", "type": "IntellectualProduct"}, {"text": "pegylated - interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "PI", "type": "Chemical"}, {"text": "telaprevir", "type": "Chemical"}, {"text": "boceprevir", "type": "Chemical"}, {"text": "simeprevir", "type": "Chemical"}, {"text": "interferon -free regimen", "type": "HealthCareActivity"}, {"text": "Group B", "type": "IntellectualProduct"}, {"text": "sofosbuvir", "type": "Chemical"}]}

Example input:
Sentence: G G homozygotic and G A heterozygotic status in TLR9 2848 G > A SNP decreased significantly the occurrence of HCMV infection ( OR 0 .

Example answer:
{"entities": [{"text": "G", "type": "Chemical"}, {"text": "A", "type": "Chemical"}, {"text": "TLR9", "type": "AnatomicalStructure"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "HCMV infection", "type": "BiologicFunction"}]}

Example input:
Sentence: To this end , we analyzed stool samples from six stage 4 - HCV patients and eight healthy individuals by high - throughput 16S rRNA gene sequencing using Illumina MiSeq .

Example answer:
{"entities": [{"text": "stool samples", "type": "BodySubstance"}, {"text": "HCV", "type": "Virus"}, {"text": "healthy individuals", "type": "PopulationGroup"}, {"text": "16S rRNA gene sequencing", "type": "HealthCareActivity"}, {"text": "Illumina MiSeq", "type": "MedicalDevice"}]}

Example input:
Sentence: The simultaneous genotyping of 2 IL - 28B SNPs could improve the prediction of SVR contributing to better therapeutic decisions and treatment management .

Example answer:
{"entities": [{"text": "genotyping", "type": "HealthCareActivity"}, {"text": "IL - 28B", "type": "AnatomicalStructure"}, {"text": "SNPs", "type": "SpatialConcept"}, {"text": "improve", "type": "Finding"}, {"text": "SVR", "type": "Finding"}, {"text": "decisions", "type": "BiologicFunction"}, {"text": "treatment management", "type": "HealthCareActivity"}]}

Example input:
Sentence: The study cohort included 73 chronic HCV patients treated with concomitant administration of CIGB - 230 and nonpegylated IFN - α plus ribavirin ( non - pegIFN - α / R ) antiviral therapy .

Example answer:
{"entities": [{"text": "HCV", "type": "Virus"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "CIGB - 230", "type": "Chemical"}, {"text": "nonpegylated IFN - α", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "non - pegIFN - α", "type": "Chemical"}, {"text": "R", "type": "Chemical"}, {"text": "antiviral therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Risk factors for hepatitis C virus infection in the Colombian Caribbean coast : A case - control study An estimated 6 . 8 - 8 . 9 million people are infected with hepatitis C virus in Latin America , of which less than 1 % receives antiviral treatment .

Example answer:
{"entities": [{"text": "Risk factors", "type": "Finding"}, {"text": "hepatitis C virus infection", "type": "BiologicFunction"}, {"text": "Caribbean coast", "type": "SpatialConcept"}, {"text": "case - control study", "type": "ResearchActivity"}, {"text": "people", "type": "PopulationGroup"}, {"text": "infected", "type": "Finding"}, {"text": "hepatitis C virus", "type": "Virus"}, {"text": "Latin America", "type": "SpatialConcept"}, {"text": "antiviral treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The genotype distribution of IL - 28B rs12979860CC , - CT , and - TT was 29 , 41 , and 30 % , respectively , and the distribution for rs8099917TT , - TG , and - GG was 63 , 31 , and 5 % , respectively .

Example answer:
{"entities": [{"text": "IL - 28B rs12979860CC", "type": "AnatomicalStructure"}, {"text": "CT", "type": "AnatomicalStructure"}, {"text": "TT", "type": "AnatomicalStructure"}, {"text": "rs8099917TT", "type": "AnatomicalStructure"}, {"text": "TG", "type": "AnatomicalStructure"}, {"text": "GG", "type": "AnatomicalStructure"}]}

Example input:
Sentence: It is concluded that in Cuban HCV - infected patients , the responder homogeneous variant rs8099917TT is the most frequent genotype .

Example answer:
{"entities": [{"text": "Cuban", "type": "PopulationGroup"}, {"text": "HCV", "type": "Virus"}, {"text": "infected", "type": "Finding"}, {"text": "responder", "type": "Finding"}, {"text": "variant", "type": "AnatomicalStructure"}, {"text": "rs8099917TT", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Assessment of IL - 28 : rs12979860 and rs8099917 Polymorphisms in a Cohort of Cuban Chronic HCV Genotype 1b Patients Hepatitis C virus ( HCV ) is a significant global public health problem with > 185 million infections worldwide .

Example answer:
{"entities": [{"text": "Assessment", "type": "HealthCareActivity"}, {"text": "IL - 28", "type": "AnatomicalStructure"}, {"text": "rs8099917", "type": "AnatomicalStructure"}, {"text": "Polymorphisms", "type": "BiologicFunction"}, {"text": "Cohort", "type": "PopulationGroup"}, {"text": "Cuban", "type": "PopulationGroup"}, {"text": "Chronic HCV Genotype 1b", "type": "BiologicFunction"}, {"text": "Hepatitis C virus", "type": "Virus"}, {"text": "HCV", "type": "Virus"}, {"text": "infections", "type": "BiologicFunction"}, {"text": "worldwide", "type": "PopulationGroup"}]}

Input:
Sentence: The objective of this work was to evaluate the prevalence of IL - 28B rs12979860 and rs8099917 polymorphisms in Cuban chronic HCV patients .

## Item MedMentions:test:3387
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

## Item MedMentions:test:3218
Example input:
Sentence: Potentially preventable amputations associated with high - risk diseases are increasing among patients who require inpatient hospital admission , present to the ED , or require outpatient interventional treatment .

Example answer:
{"entities": [{"text": "amputations", "type": "HealthCareActivity"}, {"text": "risk", "type": "HealthCareActivity"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "hospital admission", "type": "HealthCareActivity"}, {"text": "ED", "type": "Organization"}]}

Example input:
Sentence: Hyposalivation , rheumatoid arthritis , smoking / tobacco use , undiagnosed or sub - optimally controlled diabetes and obesity are common acquired risk factors for both caries and periodontal diseases .

Example answer:
{"entities": [{"text": "Hyposalivation", "type": "Finding"}, {"text": "rheumatoid arthritis", "type": "BiologicFunction"}, {"text": "smoking / tobacco use", "type": "Finding"}, {"text": "undiagnosed", "type": "Finding"}, {"text": "sub - optimally controlled", "type": "Finding"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "caries", "type": "BiologicFunction"}, {"text": "periodontal diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: The frequency of DDE and MIH might have been masked by extended carious lesions , dental wear and ante - mortem tooth loss .

Example answer:
{"entities": [{"text": "DDE", "type": "Finding"}, {"text": "MIH", "type": "BiologicFunction"}, {"text": "masked", "type": "ResearchActivity"}, {"text": "extended", "type": "SpatialConcept"}, {"text": "carious lesions", "type": "BiologicFunction"}, {"text": "dental wear", "type": "InjuryOrPoisoning"}, {"text": "ante - mortem", "type": "Finding"}, {"text": "tooth loss", "type": "AnatomicalStructure"}]}

Example input:
Sentence: However , some complications , such as microstomia , distortion of oral commissure , lip functional problems , and sensory loss might occur with these techniques .

Example answer:
{"entities": [{"text": "complications", "type": "BiologicFunction"}, {"text": "microstomia", "type": "AnatomicalStructure"}, {"text": "oral commissure", "type": "SpatialConcept"}, {"text": "lip", "type": "AnatomicalStructure"}, {"text": "problems", "type": "Finding"}, {"text": "sensory loss", "type": "Finding"}]}

Example input:
Sentence: No individual suffered from affected molars and incisors in combination .

Example answer:
{"entities": [{"text": "individual", "type": "PopulationGroup"}, {"text": "molars", "type": "AnatomicalStructure"}, {"text": "incisors", "type": "AnatomicalStructure"}]}

Example input:
Sentence: PD accounts for the majority of tooth loss and increases with age . China 's third national epidemiological investigation on oral diseases ( 2005 ) revealed that periodontitis affected > 50 % of the adult population .

Example answer:
{"entities": [{"text": "PD", "type": "BiologicFunction"}, {"text": "tooth loss", "type": "AnatomicalStructure"}, {"text": "China 's", "type": "SpatialConcept"}, {"text": "national epidemiological investigation", "type": "ResearchActivity"}, {"text": "oral diseases", "type": "BiologicFunction"}, {"text": "periodontitis", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: Various methods like orthodontic assisted extraction , staged removal of tooth or coronectomy have been advocated to reduce the incidence of IAN injury in high risk cases with variable outcome .

Example answer:
{"entities": [{"text": "methods", "type": "HealthCareActivity"}, {"text": "orthodontic assisted extraction", "type": "HealthCareActivity"}, {"text": "staged removal of tooth", "type": "HealthCareActivity"}, {"text": "IAN", "type": "AnatomicalStructure"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "high risk", "type": "Finding"}, {"text": "variable outcome", "type": "Finding"}]}

Example input:
Sentence: As a result , the aftermath is chewing disability and damage to self - esteem due to an altered self - image .

Example answer:
{"entities": [{"text": "chewing", "type": "BiologicFunction"}, {"text": "disability", "type": "Finding"}, {"text": "self - esteem", "type": "BiologicFunction"}, {"text": "self - image", "type": "BiologicFunction"}]}

Example input:
Sentence: Interaction of lifestyle , behaviour or systemic diseases with dental caries and periodontal diseases : consensus report of group 2 of the joint EFP / ORCA workshop on the boundaries between caries and periodontal diseases Periodontal diseases and dental caries are the most common diseases of humans and the main cause of tooth loss .

Example answer:
{"entities": [{"text": "systemic diseases", "type": "BiologicFunction"}, {"text": "dental caries", "type": "BiologicFunction"}, {"text": "periodontal diseases", "type": "BiologicFunction"}, {"text": "consensus report of group 2 of the joint EFP / ORCA workshop", "type": "ProfessionalOrOccupationalGroup"}, {"text": "caries", "type": "BiologicFunction"}, {"text": "Periodontal diseases", "type": "BiologicFunction"}, {"text": "common diseases", "type": "BiologicFunction"}, {"text": "tooth loss", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Inadequate resection may lead to many complications such as bone deformity and dysfunction .

Example answer:
{"entities": [{"text": "resection", "type": "HealthCareActivity"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "bone deformity", "type": "AnatomicalStructure"}]}

Input:
Sentence: Unfortunately , the consequence of this disease frequently involves tooth extractions .

## Item MedMentions:test:3214
Example input:
Sentence: Furthermore , acetamiprid induced liver toxicity measured by the increased activities of aspartate aminotransferase ( AST ) , alanine aminotransferase ( ALT ) , alkaline phosphates ( ALPs ) , and lactate dehydrogenase ( LDH ) which may be due to the loss of hepatic membrane architecture and hepatocellular damage .

Example answer:
{"entities": [{"text": "acetamiprid", "type": "Chemical"}, {"text": "induced liver toxicity", "type": "BiologicFunction"}, {"text": "activities", "type": "BiologicFunction"}, {"text": "aspartate aminotransferase", "type": "Chemical"}, {"text": "AST", "type": "Chemical"}, {"text": "alanine aminotransferase", "type": "Chemical"}, {"text": "ALT", "type": "Chemical"}, {"text": "alkaline phosphates", "type": "Chemical"}, {"text": "ALPs", "type": "Chemical"}, {"text": "lactate dehydrogenase", "type": "Chemical"}, {"text": "LDH", "type": "Chemical"}, {"text": "hepatic membrane architecture", "type": "AnatomicalStructure"}, {"text": "hepatocellular damage", "type": "BiologicFunction"}]}

Example input:
Sentence: The upregulation of various enzymes , including CYP2B6 , by CAR activators is a critical problem leading to clinically severe drug - drug interactions ( DDIs ) .

Example answer:
{"entities": [{"text": "upregulation", "type": "BiologicFunction"}, {"text": "enzymes", "type": "Chemical"}, {"text": "CYP2B6", "type": "Chemical"}, {"text": "CAR", "type": "Chemical"}, {"text": "activators", "type": "Chemical"}, {"text": "drug - drug interactions", "type": "BiologicFunction"}, {"text": "DDIs", "type": "BiologicFunction"}]}

Example input:
Sentence: The results of this study demonstrated that PZA decreased the expression levels of liver fatty acid binding protein ( L - FABP ) and its target gene , peroxisome proliferator - activated receptor α ( PPAR - α ) , and provoked more severe oxidative stress and hepatitis via the upregulation of inflammatory cytokines such as tumor necrosis factor alpha ( TNF - α ) and transforming growth factor β ( TGF - β ) .

Example answer:
{"entities": [{"text": "PZA", "type": "Chemical"}, {"text": "liver fatty acid binding protein", "type": "Chemical"}, {"text": "L - FABP", "type": "Chemical"}, {"text": "target gene", "type": "AnatomicalStructure"}, {"text": "peroxisome proliferator - activated receptor α", "type": "Chemical"}, {"text": "PPAR - α", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "hepatitis", "type": "BiologicFunction"}, {"text": "upregulation", "type": "BiologicFunction"}, {"text": "inflammatory cytokines", "type": "BiologicFunction"}, {"text": "tumor necrosis factor alpha", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "transforming growth factor β", "type": "Chemical"}, {"text": "TGF - β", "type": "Chemical"}]}

Example input:
Sentence: Although only 10 % of genes overlapped across the two drugs , network analysis shows that both drugs modulated the CREB pathway , through different molecular mechanisms .

Example answer:
{"entities": [{"text": "genes", "type": "AnatomicalStructure"}, {"text": "drugs", "type": "Chemical"}, {"text": "network analysis", "type": "IntellectualProduct"}, {"text": "CREB pathway", "type": "BiologicFunction"}, {"text": "molecular mechanisms", "type": "BiologicFunction"}]}

Example input:
Sentence: We investigated potential molecular mechanisms of liver injury in pediatric onset IF .

Example answer:
{"entities": [{"text": "liver injury", "type": "InjuryOrPoisoning"}, {"text": "IF", "type": "BiologicFunction"}]}

Example input:
Sentence: 8 ( IQR 1 . 2 to 11 ) ] in relation to biochemical and histologic liver injury , PN , serum plant sterols , fibroblast growth factor 19 , and α - tocopherol .

Example answer:
{"entities": [{"text": "liver injury", "type": "InjuryOrPoisoning"}, {"text": "PN", "type": "HealthCareActivity"}, {"text": "serum", "type": "BodySubstance"}, {"text": "plant sterols", "type": "Chemical"}, {"text": "fibroblast growth factor 19", "type": "Chemical"}, {"text": "α - tocopherol", "type": "Chemical"}]}

Example input:
Sentence: According to statistical analysis , gender as well as the number of drugs prescribed were significant predictors for drug - drug interactions .

Example answer:
{"entities": [{"text": "drugs prescribed", "type": "Chemical"}, {"text": "drug - drug interactions", "type": "BiologicFunction"}]}

Example input:
Sentence: The most frequent interaction was between cytostatics and coumarins while the most relevant one was between cisplatin and furosemide .

Example answer:
{"entities": [{"text": "interaction", "type": "BiologicFunction"}, {"text": "cytostatics", "type": "Chemical"}, {"text": "coumarins", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "furosemide", "type": "Chemical"}]}

Example input:
Sentence: Associations of gender and a proxy of female menopausal status with histological features of drug - induced liver injury Gender and menopause may contribute to type and severity of drug - induced liver injury ( DILI ) by influencing host responses to injury .

Example answer:
{"entities": [{"text": "menopausal status", "type": "ClinicalAttribute"}, {"text": "drug - induced liver injury", "type": "BiologicFunction"}, {"text": "menopause", "type": "BiologicFunction"}, {"text": "DILI", "type": "BiologicFunction"}, {"text": "responses", "type": "Finding"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: While HCV epidemiology , pathophysiology , and therapy are being deeply studied , rare attention is given to reciprocal interactions between HCV infection , HCV -induced chronic liver diseases , and the human gut microbiome .

Example answer:
{"entities": [{"text": "HCV", "type": "Virus"}, {"text": "epidemiology", "type": "ResearchActivity"}, {"text": "pathophysiology", "type": "BiologicFunction"}, {"text": "reciprocal interactions", "type": "BiologicFunction"}, {"text": "HCV infection", "type": "BiologicFunction"}, {"text": "chronic liver diseases", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}]}

Input:
Sentence: We analyzed liver injury and drug - drug interactions .

## Item MedMentions:test:3251
Example input:
Sentence: 051 , WRMR = 1 . 297 ] and reliability was acceptable ( range 0 . 73 - 0 . 84 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 8 for BED , 1 . 5 for LAg and 40 % for BRAI , estimated MDRIs for postpartum mothers , were 192 , 104 and 144 days , 33 % , 32 - 41 % and 52 % lower than published estimates of 287 , 152 - 177 and 298 days , respectively , for clade C samples from general populations .

Example answer:
{"entities": [{"text": "BED", "type": "HealthCareActivity"}, {"text": "LAg", "type": "HealthCareActivity"}, {"text": "BRAI", "type": "HealthCareActivity"}, {"text": "published estimates", "type": "IntellectualProduct"}, {"text": "clade C", "type": "IntellectualProduct"}, {"text": "general populations", "type": "PopulationGroup"}]}

Example input:
Sentence: There were significant reductions in the median monthly number of type and screens not associated with RBC crossmatches ( 10 714 - 10 061 ; p < 0 . 0001 ) and the median number of type and screens associated with RBC crossmatches ( 10 127 - 9 349 ; p = 0 . 0014 ) on surgical patients after dMSBOS implementation .

Example answer:
{"entities": [{"text": "RBC", "type": "AnatomicalStructure"}, {"text": "crossmatches", "type": "HealthCareActivity"}, {"text": "surgical", "type": "HealthCareActivity"}, {"text": "dMSBOS", "type": "IntellectualProduct"}]}

Example input:
Sentence: At 1 month , 24 ( 80 . 0 % ) and 23 ( 76 . 7 % ) patients had achieved normal MBI and MRS scores with 28 ( 93 . 3 ) and 27 ( 90 % ) patients , respectively , at 3 months .

Example answer:
{"entities": [{"text": "MBI", "type": "IntellectualProduct"}, {"text": "MRS scores", "type": "IntellectualProduct"}]}

Example input:
Sentence: 7 μm 3 months after treatment ( p = 0 . 005 ) .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: 1 - 14 . 1 ) , 3 . 7 years ( range 0 . 8 - 15 . 2 ) , and 3 . 6 years ( range 0 . 7 - 13 .

Example answer:
{"entities": []}

Example input:
Sentence: 12 ± 18 . 35 months post - RT .

Example answer:
{"entities": [{"text": "RT", "type": "HealthCareActivity"}]}

Example input:
Sentence: No complications or recurrence were shown during follow - up ( range , 12 - 60 mo ) .

Example answer:
{"entities": [{"text": "complications", "type": "BiologicFunction"}, {"text": "recurrence", "type": "BiologicFunction"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Heterotopic ossification after the use of recombinant human bone morphogenetic protein - 7 To present the incidence of heterotopic ossification after the use of recombinant human bone morphogenetic protein - 7 ( rhBMP - 7 ) for the treatment of nonunions .

Example answer:
{"entities": [{"text": "Heterotopic ossification", "type": "BiologicFunction"}, {"text": "recombinant human bone morphogenetic protein - 7", "type": "Chemical"}, {"text": "heterotopic ossification", "type": "BiologicFunction"}, {"text": "rhBMP - 7", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "nonunions", "type": "Finding"}]}

Example input:
Sentence: Eighty point nine percent of the nonunions treated with rhBMP - 7 , healed with no need for further procedures .

Example answer:
{"entities": [{"text": "nonunions", "type": "Finding"}, {"text": "rhBMP - 7", "type": "Chemical"}]}

Input:
Sentence: 5 mo after the rhBMP - 7 application ( range 3 - 12 ) .

## Item MedMentions:test:3255
Example input:
Sentence: Such a referential choice theory unravels that choice with reference to the family push and social norms sustains the engagement .

Example answer:
{"entities": [{"text": "engagement", "type": "Finding"}]}

Example input:
Sentence: We therefore aimed to apply the social marketing theory and health belief model in promoting cervical cancer screening in Kanthararom District , Sisaket Province .

Example answer:
{"entities": [{"text": "health belief model", "type": "HealthCareActivity"}, {"text": "cervical cancer screening", "type": "HealthCareActivity"}, {"text": "Kanthararom District", "type": "SpatialConcept"}, {"text": "Sisaket Province", "type": "SpatialConcept"}]}

Example input:
Sentence: Extrapolating from focus group data collected from African American church populations as part of a social marketing health promotion project on cancer prevention , we theoretically consider how a similar communication framework and approach may apply to address LBW disparities .

Example answer:
{"entities": [{"text": "data collected", "type": "Finding"}, {"text": "African American", "type": "PopulationGroup"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "health promotion project", "type": "HealthCareActivity"}, {"text": "cancer prevention", "type": "HealthCareActivity"}, {"text": "communication", "type": "HealthCareActivity"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "LBW", "type": "Finding"}, {"text": "disparities", "type": "Finding"}]}

Example input:
Sentence: This pattern documents that social learning through peer -to - peer information exchange can serve as a complementary and reinforcing pathway with technical learning that is stimulated by traditional outreach and extension programs .

Example answer:
{"entities": [{"text": "pattern", "type": "SpatialConcept"}, {"text": "social learning", "type": "BiologicFunction"}, {"text": "peer", "type": "PopulationGroup"}]}

Example input:
Sentence: Effects of Application of Social Marketing Theory and the Health Belief Model in Promoting Cervical Cancer Screening among Targeted Women in Sisaket Province , Thailand Cervical cancer is a major public health problem in Thailand , being ranked second only to breast cancer .

Example answer:
{"entities": [{"text": "Health Belief Model", "type": "HealthCareActivity"}, {"text": "Cervical Cancer Screening", "type": "HealthCareActivity"}, {"text": "Women", "type": "PopulationGroup"}, {"text": "Sisaket Province", "type": "SpatialConcept"}, {"text": "Thailand", "type": "SpatialConcept"}, {"text": "Cervical cancer", "type": "BiologicFunction"}, {"text": "public health problem", "type": "Finding"}, {"text": "ranked", "type": "IntellectualProduct"}, {"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Findings suggest stigma is still prevalent even in organizations that have consumers in leadership positions , and consumers are often perceived as less able to work in mental health organizations than non - consumers .

Example answer:
{"entities": [{"text": "Findings", "type": "Finding"}, {"text": "stigma", "type": "Finding"}, {"text": "consumers", "type": "PopulationGroup"}, {"text": "perceived", "type": "BiologicFunction"}]}

Example input:
Sentence: The experimental group underwent application of social marketing theory and a health belief model program promoting cervical cancer screening while the control group received normal services .

Example answer:
{"entities": [{"text": "experimental group", "type": "PopulationGroup"}, {"text": "health belief model", "type": "HealthCareActivity"}, {"text": "cervical cancer screening", "type": "HealthCareActivity"}]}

Example input:
Sentence: Several discourses challenged such a view - showing how consumers bring value to mental health organizations through their expertise in the mental health system , and their ability to provide safety and support to other consumers .

Example answer:
{"entities": [{"text": "consumers", "type": "PopulationGroup"}, {"text": "safety", "type": "HealthCareActivity"}]}

Example input:
Sentence: Improving exchange with consumers within mental health organizations : Recognizing mental ill health experience as a ' sneaky , special degree ' Stigmatizing views towards consumers may be held even by those working within mental health organizations .

Example answer:
{"entities": [{"text": "consumers", "type": "PopulationGroup"}, {"text": "mental ill health", "type": "BiologicFunction"}, {"text": "Stigmatizing", "type": "Finding"}]}

Example input:
Sentence: Using social exchange theory , which emphasises mutual exchange to maximise benefits in partnership , the current study explores the perspectives of those working within organizations that have some level of consumer leadership .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "consumer", "type": "PopulationGroup"}]}

Input:
Sentence: Through a social exchange theory lens , the authors call for organizations to challenge stigma and promote the value that consumers can bring to maximize mutual benefits .

## Item MedMentions:test:3277
Example input:
Sentence: Impact of AAC ( 6 ' ) - Ib - cr in combination with chromosomal -mediated mechanisms on clinical quinolone resistance in Escherichia coli aac ( 6 ' ) - Ib - cr is the most prevalent plasmid -mediated fluoroquinolone ( FQ ) resistance mechanism in Enterobacteriaceae .

Example answer:
{"entities": [{"text": "AAC ( 6 ' ) - Ib - cr", "type": "Chemical"}, {"text": "chromosomal", "type": "AnatomicalStructure"}, {"text": "quinolone", "type": "Chemical"}, {"text": "resistance", "type": "BiologicFunction"}, {"text": "Escherichia coli", "type": "Bacterium"}, {"text": "aac ( 6 ' ) - Ib - cr", "type": "AnatomicalStructure"}, {"text": "plasmid", "type": "Chemical"}, {"text": "fluoroquinolone", "type": "Chemical"}, {"text": "FQ", "type": "Chemical"}, {"text": "resistance mechanism", "type": "BiologicFunction"}, {"text": "Enterobacteriaceae", "type": "Bacterium"}]}

Example input:
Sentence: We aimed to analyse the interplay between this plasmid -mediated gene and chromosomal -mediated quinolone resistance mechanisms on both FQ resistance and bacterial fitness in Escherichia coli .

Example answer:
{"entities": [{"text": "plasmid", "type": "Chemical"}, {"text": "gene", "type": "AnatomicalStructure"}, {"text": "chromosomal", "type": "AnatomicalStructure"}, {"text": "quinolone", "type": "Chemical"}, {"text": "resistance mechanisms", "type": "BiologicFunction"}, {"text": "FQ", "type": "Chemical"}, {"text": "resistance", "type": "BiologicFunction"}, {"text": "bacterial", "type": "Bacterium"}, {"text": "fitness", "type": "BiologicFunction"}, {"text": "Escherichia coli", "type": "Bacterium"}]}

Example input:
Sentence: Besides potentiating tetracycline antibiotics , TOB - EPI conjugates can also suppress resistance development to the tetracycline antibiotic minocycline , thereby providing a strategy to develop more effective adjuvants to rescue tetracycline antibiotics from resistance in MDR Gram - negative bacteria .

Example answer:
{"entities": [{"text": "potentiating", "type": "BiologicFunction"}, {"text": "tetracycline antibiotics", "type": "Chemical"}, {"text": "TOB", "type": "Chemical"}, {"text": "EPI", "type": "Chemical"}, {"text": "tetracycline antibiotic", "type": "Chemical"}, {"text": "minocycline", "type": "Chemical"}, {"text": "adjuvants", "type": "Chemical"}, {"text": "Gram - negative bacteria", "type": "Bacterium"}]}

Example input:
Sentence: Reportedly , bacterial resistance to rifampicin is associated with polymorphisms in the target gene rpoB or the presence of enzymes that modify and thereby inactivate rifampicin .

Example answer:
{"entities": [{"text": "bacterial resistance", "type": "BiologicFunction"}, {"text": "rifampicin", "type": "Chemical"}, {"text": "polymorphisms", "type": "BiologicFunction"}, {"text": "gene rpoB", "type": "AnatomicalStructure"}, {"text": "enzymes", "type": "Chemical"}]}

Example input:
Sentence: We demonstrate that conjugation of a tobramycin ( TOB ) vector to EPIs like NMP , paroxetine , or DBP enhances synergy and efficacy of EPIs in combination with tetracycline antibiotics against MDR Gram - negative bacteria including Pseudomonas aeruginosa .

Example answer:
{"entities": [{"text": "conjugation", "type": "BiologicFunction"}, {"text": "tobramycin", "type": "Chemical"}, {"text": "TOB", "type": "Chemical"}, {"text": "EPIs", "type": "Chemical"}, {"text": "NMP", "type": "Chemical"}, {"text": "paroxetine", "type": "Chemical"}, {"text": "DBP", "type": "ClinicalAttribute"}, {"text": "synergy", "type": "Finding"}, {"text": "tetracycline antibiotics", "type": "Chemical"}, {"text": "Gram - negative bacteria", "type": "Bacterium"}, {"text": "Pseudomonas aeruginosa", "type": "Bacterium"}]}

Example input:
Sentence: Bacterial resistance is often caused by molecular changes at the bacterial surface , which alter the nature of specific drug - target interactions .

Example answer:
{"entities": [{"text": "Bacterial resistance", "type": "BiologicFunction"}, {"text": "molecular changes", "type": "Finding"}, {"text": "bacterial surface", "type": "Finding"}, {"text": "drug - target interactions", "type": "BiologicFunction"}]}

Example input:
Sentence: Using an exactly solvable model , which takes into account the solvent and membrane effects , we demonstrate that drug - target interactions are strengthened by pronounced polyvalent interactions catalyzed by the surface itself .

Example answer:
{"entities": [{"text": "exactly solvable model", "type": "IntellectualProduct"}, {"text": "solvent", "type": "Chemical"}, {"text": "membrane", "type": "AnatomicalStructure"}, {"text": "drug - target interactions", "type": "BiologicFunction"}, {"text": "pronounced polyvalent interactions", "type": "BiologicFunction"}, {"text": "surface", "type": "SpatialConcept"}]}

Example input:
Sentence: Our studies reveal a new paradigm of host - pathogen interactions , in which pathogens exploit conserved host post - translational modifications , thereby achieving highly specific receptor binding while also tolerating genetic changes across multiple isoforms of receptors .

Example answer:
{"entities": [{"text": "host - pathogen interactions", "type": "BiologicFunction"}, {"text": "post - translational modifications", "type": "BiologicFunction"}, {"text": "receptor binding", "type": "BiologicFunction"}, {"text": "genetic changes", "type": "BiologicFunction"}, {"text": "isoforms", "type": "Chemical"}, {"text": "receptors", "type": "Chemical"}]}

Example input:
Sentence: A Tobramycin Vector Enhances Synergy and Efficacy of Efflux Pump Inhibitors against Multidrug - Resistant Gram - Negative Bacteria Drug efflux mechanisms interact synergistically with the outer membrane permeability barrier of Gram - negative bacteria , leading to intrinsic resistance that presents a major challenge for antibiotic drug development .

Example answer:
{"entities": [{"text": "Tobramycin Vector", "type": "Chemical"}, {"text": "Synergy", "type": "Finding"}, {"text": "Efflux Pump Inhibitors", "type": "Chemical"}, {"text": "Gram - Negative Bacteria", "type": "Bacterium"}, {"text": "Drug efflux", "type": "BiologicFunction"}, {"text": "interact", "type": "BiologicFunction"}, {"text": "outer membrane", "type": "AnatomicalStructure"}, {"text": "permeability", "type": "BiologicFunction"}, {"text": "barrier", "type": "BiologicFunction"}, {"text": "Gram - negative bacteria", "type": "Bacterium"}, {"text": "intrinsic", "type": "SpatialConcept"}, {"text": "challenge", "type": "HealthCareActivity"}, {"text": "antibiotic", "type": "Chemical"}, {"text": "drug development", "type": "ResearchActivity"}]}

Example input:
Sentence: Surface mediated cooperative interactions of drugs enhance mechanical forces for antibiotic action The alarming increase of pathogenic bacteria that are resistant to multiple antibiotics is now recognized as a major health issue fuelling demand for new drugs .

Example answer:
{"entities": [{"text": "Surface", "type": "SpatialConcept"}, {"text": "interactions of drugs", "type": "BiologicFunction"}, {"text": "antibiotic", "type": "Chemical"}, {"text": "resistant to multiple antibiotics", "type": "BiologicFunction"}, {"text": "demand", "type": "HealthCareActivity"}, {"text": "drugs", "type": "Chemical"}]}

Input:
Sentence: Here , we identify a novel mechanism by which drug - target interactions in resistant bacteria can be enhanced .

## Item MedMentions:test:3153
Example input:
Sentence: Optical simulations ( in terms of through - focus Strehl ratio from Hartmann - Shack aberrometry ) accurately predicted the pattern producing the highest perceived quality in 4 out of 5 patients , both for far and near vision .

Example answer:
{"entities": [{"text": "Optical simulations", "type": "Finding"}, {"text": "pattern", "type": "SpatialConcept"}, {"text": "vision", "type": "BiologicFunction"}]}

Example input:
Sentence: Correlations with anatomic aspects provided evidence of a rostrocaudal gradient with increasing gray / white - matter ratio and decreasing hematoma -volume and rate of hematoma enlargement from frontal to occipital ICH location .

Example answer:
{"entities": [{"text": "rostrocaudal", "type": "SpatialConcept"}, {"text": "gray", "type": "AnatomicalStructure"}, {"text": "white - matter", "type": "AnatomicalStructure"}, {"text": "hematoma", "type": "BiologicFunction"}, {"text": "enlargement", "type": "AnatomicalStructure"}, {"text": "frontal", "type": "AnatomicalStructure"}, {"text": "occipital", "type": "AnatomicalStructure"}, {"text": "ICH", "type": "Finding"}, {"text": "location", "type": "SpatialConcept"}]}

Example input:
Sentence: For manual segmentation , linear regression tests consistently identified the voxel intensity ratio derived from the dorsolateral SN and nigrosome - 1 ( IR2 ) as predictive of nBehav ( p = 0 . 0377 ) and nExp ( p = 0 . 03856 ) .

Example answer:
{"entities": [{"text": "segmentation", "type": "HealthCareActivity"}, {"text": "dorsolateral", "type": "SpatialConcept"}, {"text": "SN", "type": "AnatomicalStructure"}, {"text": "nigrosome - 1", "type": "AnatomicalStructure"}, {"text": "nBehav", "type": "HealthCareActivity"}, {"text": "nExp", "type": "Finding"}]}

Example input:
Sentence: 50mm ( 3 ) resolution was obtained , which indeed showed a higher response in the cortex compared to the corpus callosum .

Example answer:
{"entities": [{"text": "cortex", "type": "AnatomicalStructure"}, {"text": "corpus callosum", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The voxel intensity ratio derived from the dorsolateral SN and nigrosome - 1 was consistently predictive of non - motor complex behaviors in all three analyses and predictive of non - motor experiences of daily living , motor experiences of daily living , and motor signs of PD in two of the three analyses .

Example answer:
{"entities": [{"text": "dorsolateral", "type": "SpatialConcept"}, {"text": "SN", "type": "AnatomicalStructure"}, {"text": "nigrosome - 1", "type": "AnatomicalStructure"}, {"text": "complex behaviors", "type": "Finding"}, {"text": "motor signs", "type": "Finding"}, {"text": "PD", "type": "BiologicFunction"}]}

Example input:
Sentence: Visual inspection confirms that artefacts are indeed suppressed by the proposed method , and the HU root mean square difference between reconstructed CBCTs and the reference CT images are reduced by 31 % when using the artefact corrections compared to the standard clinical CBCT reconstruction .

Example answer:
{"entities": [{"text": "Visual inspection", "type": "HealthCareActivity"}, {"text": "confirms", "type": "Finding"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "CBCTs", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "CBCT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Finally , the susceptibility values of deep gray matter are analyzed in multiple head positions , with the supine position most approximate to the gold standard COSMOS result .

Example answer:
{"entities": [{"text": "gray matter", "type": "AnatomicalStructure"}, {"text": "multiple head positions", "type": "SpatialConcept"}, {"text": "supine position", "type": "SpatialConcept"}]}

Example input:
Sentence: Simulations and in vivo human experiments at 7 T MRI show that the SFCR method provides high quality susceptibility maps with improved RMSE and MSSIM .

Example answer:
{"entities": [{"text": "Simulations", "type": "ResearchActivity"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "human", "type": "Eukaryote"}, {"text": "experiments", "type": "ResearchActivity"}, {"text": "MRI", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the S - step , the susceptibility map is fitted in spatial domain using weighted constraints derived from the initial susceptibility map from the M - step .

Example answer:
{"entities": []}

Example input:
Sentence: In the M - step , the initial susceptibility map is reconstructed by employing a k - space based compressed sensing model incorporating magnitude prior .

Example answer:
{"entities": [{"text": "compressed sensing model", "type": "IntellectualProduct"}]}

Input:
Sentence: However , the anatomy observed in magnitude and phase images does not always coincide spatially with that in susceptibility maps , which could give erroneous estimation in the reconstructed susceptibility map .

## Item MedMentions:test:3161
Example input:
Sentence: Albumin -Bioinspired Gd : CuS Nanotheranostic Agent for In Vivo Photoacoustic / Magnetic Resonance Imaging -Guided Tumor -Targeted Photothermal Therapy Photothermal therapy ( PTT ) is attracting increasing interest and becoming more widely used for skin cancer therapy in the clinic , as a result of its noninvasiveness and low systemic adverse effects .

Example answer:
{"entities": [{"text": "Albumin", "type": "Chemical"}, {"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "In Vivo", "type": "SpatialConcept"}, {"text": "Photoacoustic / Magnetic Resonance Imaging -Guided Tumor -Targeted Photothermal Therapy", "type": "HealthCareActivity"}, {"text": "Photothermal therapy", "type": "HealthCareActivity"}, {"text": "PTT", "type": "HealthCareActivity"}, {"text": "skin cancer therapy", "type": "HealthCareActivity"}, {"text": "clinic", "type": "Organization"}, {"text": "low systemic adverse effects", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients were monitored post - operatively for 2 h with standard invasive monitoring and with a study device comprising an arterial tonometry sensor ( BPro ( ® ) ) added with a three - dimensional accelerometer to investigate the potential impact of movement .

Example answer:
{"entities": [{"text": "monitored post - operatively", "type": "HealthCareActivity"}, {"text": "invasive monitoring", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "arterial", "type": "AnatomicalStructure"}, {"text": "tonometry sensor", "type": "MedicalDevice"}, {"text": "BPro ( ® )", "type": "MedicalDevice"}, {"text": "movement", "type": "BiologicFunction"}]}

Example input:
Sentence: We suggest improved patient and physician education on prodromal symptoms , extended femur scans using dual - energy X - ray absorptiometry ( DXA ) to monitor patients on antiresorptive treatment , better identification of high - risk patients perhaps using geometrical parameters from DXA and other risk factors , and more research on pharmacogenomics to identify risk markers .

Example answer:
{"entities": [{"text": "improved", "type": "Finding"}, {"text": "physician", "type": "ProfessionalOrOccupationalGroup"}, {"text": "education", "type": "IntellectualProduct"}, {"text": "prodromal symptoms", "type": "Finding"}, {"text": "femur", "type": "AnatomicalStructure"}, {"text": "scans", "type": "HealthCareActivity"}, {"text": "dual - energy X - ray absorptiometry", "type": "HealthCareActivity"}, {"text": "DXA", "type": "HealthCareActivity"}, {"text": "monitor patients", "type": "HealthCareActivity"}, {"text": "antiresorptive", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "risk factors", "type": "Finding"}, {"text": "pharmacogenomics", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: We observed a marked increase ( P = 0 . 01 ) in stenting after publication of the SAPPHIRE trial ( Stenting and Angioplasty With Protection in Patients at High Risk for Endarterectomy ) in 2004 , whereas stenting remained relatively unchanged after subsequent randomized trials published in 2006 ( P = 0 . 11 ) and 2010 ( P = 0 . 34 ) .

Example answer:
{"entities": [{"text": "stenting", "type": "HealthCareActivity"}, {"text": "publication", "type": "IntellectualProduct"}, {"text": "SAPPHIRE trial", "type": "ResearchActivity"}, {"text": "Stenting and Angioplasty With Protection in Patients at High Risk for Endarterectomy", "type": "ResearchActivity"}, {"text": "unchanged", "type": "Finding"}, {"text": "randomized trials", "type": "ResearchActivity"}]}

Example input:
Sentence: Influence of increased epicardial adipose tissue volume on 1 - year in - stent restenosis in patients who received coronary stent implantation Epicardial adipose tissue ( EAT ) is significantly associated with the formation and composition of coronary atherosclerotic plaque , cardiac events and the clinical prognosis of coronary heart disease .

Example answer:
{"entities": [{"text": "epicardial adipose tissue", "type": "AnatomicalStructure"}, {"text": "in - stent restenosis", "type": "BiologicFunction"}, {"text": "coronary stent", "type": "MedicalDevice"}, {"text": "implantation", "type": "HealthCareActivity"}, {"text": "Epicardial adipose tissue", "type": "AnatomicalStructure"}, {"text": "EAT", "type": "AnatomicalStructure"}, {"text": "composition", "type": "ClinicalAttribute"}, {"text": "coronary atherosclerotic", "type": "BiologicFunction"}, {"text": "plaque", "type": "Finding"}, {"text": "clinical prognosis", "type": "HealthCareActivity"}, {"text": "coronary heart disease", "type": "BiologicFunction"}]}

Example input:
Sentence: In our method , stents were tested in gelled saline at 2 different locations : at the center and at the lobe of the coil .

Example answer:
{"entities": [{"text": "stents", "type": "MedicalDevice"}, {"text": "tested", "type": "IntellectualProduct"}, {"text": "locations", "type": "SpatialConcept"}, {"text": "at the center", "type": "SpatialConcept"}, {"text": "lobe", "type": "AnatomicalStructure"}, {"text": "coil", "type": "MedicalDevice"}]}

Example input:
Sentence: However , to date , no clinical safety data are available regarding the risk of metallic stents heating with rTMS .

Example answer:
{"entities": [{"text": "clinical safety data", "type": "IntellectualProduct"}, {"text": "metallic stents", "type": "MedicalDevice"}, {"text": "rTMS", "type": "HealthCareActivity"}]}

Example input:
Sentence: We have found that heating of stents was well below the Food and Drug Administration standards of 2°C .

Example answer:
{"entities": [{"text": "stents", "type": "MedicalDevice"}, {"text": "Food and Drug Administration", "type": "Organization"}, {"text": "standards", "type": "IntellectualProduct"}]}

Example input:
Sentence: Assessment of Vascular Stent Heating with Repetitive Transcranial Magnetic Stimulation A high proportion of patients with stroke do not qualify for repetitive transcranial magnetic stimulation ( rTMS ) clinical studies due to the presence of metallic stents .

Example answer:
{"entities": [{"text": "Assessment", "type": "HealthCareActivity"}, {"text": "Vascular Stent", "type": "MedicalDevice"}, {"text": "Repetitive Transcranial Magnetic Stimulation", "type": "HealthCareActivity"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "repetitive transcranial magnetic stimulation", "type": "HealthCareActivity"}, {"text": "rTMS", "type": "HealthCareActivity"}, {"text": "clinical studies", "type": "ResearchActivity"}, {"text": "metallic stents", "type": "MedicalDevice"}]}

Example input:
Sentence: We found that stents did not heat to more than 1°C with either 1 Hz rTMS or 10 Hz rTMS in any configuration or orientation .

Example answer:
{"entities": [{"text": "stents", "type": "MedicalDevice"}, {"text": "rTMS", "type": "HealthCareActivity"}, {"text": "orientation", "type": "SpatialConcept"}]}

Input:
Sentence: Our study represents a new method for ex vivo quantification of stent heating .

## Item MedMentions:test:3372
Example input:
Sentence: The silver particles , found both inside and outside of the pores that characterize the PEO layer , produced an efficacious antimicrobial effect both against E .

Example answer:
{"entities": [{"text": "silver", "type": "Chemical"}, {"text": "particles", "type": "Chemical"}, {"text": "inside", "type": "SpatialConcept"}, {"text": "outside", "type": "SpatialConcept"}, {"text": "antimicrobial effect", "type": "BiologicFunction"}, {"text": "E .", "type": "Bacterium"}]}

Example input:
Sentence: Mechanistic investigations in organic as well as aqueous media demonstrate how controlled delivery of protons is fundamental in dictating the selectivity of a multi - electron multi - proton process like the reduction of dioxygen to water .

Example answer:
{"entities": [{"text": "controlled delivery of protons", "type": "BiologicFunction"}, {"text": "dioxygen", "type": "Chemical"}, {"text": "water", "type": "Chemical"}]}

Example input:
Sentence: Particulate matter ( PM ) in atmospheric pollution contains readily - measurable concentrations of magnetic minerals .

Example answer:
{"entities": [{"text": "magnetic minerals", "type": "Chemical"}]}

Example input:
Sentence: MagR Alone Is Insufficient to Confer Cellular Calcium Responses to Magnetic Stimulation Magnetic manipulation of cell activity offers advantages over optical manipulation but an ideal tool remains elusive .

Example answer:
{"entities": [{"text": "MagR", "type": "Chemical"}, {"text": "Cellular Calcium Responses", "type": "BiologicFunction"}, {"text": "Stimulation", "type": "HealthCareActivity"}, {"text": "manipulation", "type": "HealthCareActivity"}, {"text": "cell activity", "type": "BiologicFunction"}, {"text": "optical manipulation", "type": "HealthCareActivity"}]}

Example input:
Sentence: This form of magnetic field was capable of decreasing the proliferation of astrocytes as a response to the autoimmune attack , reducing the content of nitric oxide , bacterial lipopolysaccharide and lipopolysaccharide - binding protein in central nervous system .

Example answer:
{"entities": [{"text": "decreasing", "type": "Finding"}, {"text": "astrocytes", "type": "AnatomicalStructure"}, {"text": "autoimmune attack", "type": "BiologicFunction"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "lipopolysaccharide - binding protein", "type": "Chemical"}, {"text": "central nervous system", "type": "BodySystem"}]}

Example input:
Sentence: The presence of these weak interactions alters the spin ground state , and axial ligand bonding and provides a proton translocation pathway into the active site .

Example answer:
{"entities": [{"text": "presence", "type": "Finding"}, {"text": "axial", "type": "SpatialConcept"}, {"text": "ligand", "type": "Chemical"}, {"text": "proton translocation pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Our results indicate that MagR alone is not sufficient to confer cellular magnetic responses .

Example answer:
{"entities": [{"text": "MagR", "type": "Chemical"}, {"text": "cellular", "type": "AnatomicalStructure"}, {"text": "magnetic responses", "type": "BiologicFunction"}]}

Example input:
Sentence: Interaction - driven distinctive electronic states of artificial atoms at the ZnO interface We have investigated the electronic states of planar quantum dots at the ZnO interface containing a few interacting electrons in an externally applied magnetic field .

Example answer:
{"entities": [{"text": "electronic states", "type": "SpatialConcept"}, {"text": "artificial atoms", "type": "Chemical"}, {"text": "ZnO", "type": "Chemical"}, {"text": "electrons", "type": "Chemical"}]}

Example input:
Sentence: On application of physiologically acceptable external magnetic field , FITC conjugated artemisinin magnetic nanoparticles showed an enhanced accumulation of nanoparticles in the 4T1 breast tumour tissues of BALB / c mice model .

Example answer:
{"entities": [{"text": "external", "type": "SpatialConcept"}, {"text": "FITC", "type": "Chemical"}, {"text": "artemisinin", "type": "Chemical"}, {"text": "4T1 breast tumour tissues", "type": "AnatomicalStructure"}, {"text": "BALB / c mice", "type": "Eukaryote"}, {"text": "model", "type": "BiologicFunction"}]}

Example input:
Sentence: Drug loaded magnetic nanoparticles by using external magnetic field could selectively accumulate the drug at the target site and thereby reduce the doses required to achieve therapeutic concentration which may otherwise produce serious side effects on healthy cells .

Example answer:
{"entities": [{"text": "Drug", "type": "Chemical"}, {"text": "external", "type": "SpatialConcept"}, {"text": "drug", "type": "Chemical"}, {"text": "target site", "type": "SpatialConcept"}, {"text": "side effects", "type": "BiologicFunction"}, {"text": "healthy cells", "type": "AnatomicalStructure"}]}

Input:
Sentence: Besides , the particles could be manipulated by an external magnetic field .

## Item MedMentions:test:3293
Example input:
Sentence: We hypothesized that obesity and leptin deficiency impair opioid pharmacokinetics ( PK ) independently of one another .

Example answer:
{"entities": [{"text": "obesity", "type": "BiologicFunction"}, {"text": "leptin deficiency", "type": "BiologicFunction"}, {"text": "opioid", "type": "Chemical"}, {"text": "pharmacokinetics", "type": "BiologicFunction"}, {"text": "PK", "type": "BiologicFunction"}]}

Example input:
Sentence: Obesity also has been shown to cause resistance to leptin , an adipose -derived hormone that is key in regulating hunger , metabolism , and respiratory stimulation .

Example answer:
{"entities": [{"text": "Obesity", "type": "BiologicFunction"}, {"text": "leptin", "type": "Chemical"}, {"text": "adipose", "type": "AnatomicalStructure"}, {"text": "hormone", "type": "Chemical"}, {"text": "regulating", "type": "BiologicFunction"}, {"text": "hunger", "type": "Finding"}, {"text": "metabolism", "type": "BiologicFunction"}, {"text": "stimulation", "type": "BiologicFunction"}]}

Example input:
Sentence: Based on the collected data , we did not identify associations with HbA1c ( 0·03 % , -0·01 to 0·08 ) , fasting insulin ( 0·00 % , -0·06 to 0·07 ) , and BMI ( 0·11 kg / m ( 2 ) , -0·09 to 0·30 ) .

Example answer:
{"entities": [{"text": "HbA1c", "type": "Chemical"}, {"text": "fasting", "type": "Finding"}, {"text": "insulin", "type": "Chemical"}, {"text": "BMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: ABCA1 and ABCG1 gene expression positively correlated with obesity indicators such as body mass index ( BMI ) ( r = 0 . 522 , p = 0 .

Example answer:
{"entities": [{"text": "ABCA1", "type": "AnatomicalStructure"}, {"text": "ABCG1", "type": "AnatomicalStructure"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "indicators", "type": "Chemical"}, {"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: These data demonstrate that maternal BMI , infant sex and stage of lactation affect the compositional make - up of insulin and leptin .

Example answer:
{"entities": [{"text": "maternal", "type": "Finding"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "stage of lactation", "type": "BiologicFunction"}, {"text": "insulin", "type": "Chemical"}, {"text": "leptin", "type": "Chemical"}]}

Example input:
Sentence: There were statistically significant associations between BMI category and weight control ( ranging from a mean 5 . 18 to 7 . 68 odds of obesity ) and body image ( 3 . 40 to 13 .

Example answer:
{"entities": [{"text": "BMI", "type": "ClinicalAttribute"}, {"text": "category", "type": "IntellectualProduct"}, {"text": "weight control", "type": "HealthCareActivity"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "body image", "type": "BiologicFunction"}]}

Example input:
Sentence: Leptin has been shown to increase energy expenditure in particular through its effects on the cardiovascular system and brown adipose tissue ( BAT ) thermogenesis via the hypothalamus .

Example answer:
{"entities": [{"text": "Leptin", "type": "Chemical"}, {"text": "energy expenditure", "type": "BiologicFunction"}, {"text": "cardiovascular system", "type": "BodySystem"}, {"text": "brown adipose tissue", "type": "AnatomicalStructure"}, {"text": "BAT", "type": "AnatomicalStructure"}, {"text": "thermogenesis", "type": "BiologicFunction"}, {"text": "hypothalamus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: such that overweight and obese mothers had 96 . 5 % and 315 . 1 % higher leptin levels than normal weight mothers , respectively .

Example answer:
{"entities": [{"text": "overweight", "type": "Finding"}, {"text": "obese", "type": "BiologicFunction"}, {"text": "higher leptin levels", "type": "Finding"}, {"text": "normal weight", "type": "Finding"}]}

Example input:
Sentence: A significant inverse relationship between month 1 leptin levels and infant length ( p = 0 . 0257 ) , percent fat ( p = 0 . 0223 ) , total fat mass ( p = 0 . 0226 ) and trunk fat mass ( p = 0 . 0111 ) at month 6 was also found .

Example answer:
{"entities": [{"text": "leptin", "type": "Chemical"}, {"text": "infant length", "type": "Finding"}, {"text": "percent fat", "type": "Finding"}]}

Example input:
Sentence: Leptin was also found to have a significant ( p = 0 . 0004 ) 33 . 7 % decrease from months 1 to 6 , controlling for BMI category and sex .

Example answer:
{"entities": [{"text": "Leptin", "type": "Chemical"}, {"text": "BMI", "type": "ClinicalAttribute"}]}

Input:
Sentence: For leptin , a significant association with BMI category was observed ( p < 0 . 0001 )

## Item MedMentions:test:3314
Example input:
Sentence: Fatigue did not correlate with any CSF parameter but correlated negatively with total and cortical grey matter volume .

Example answer:
{"entities": [{"text": "Fatigue", "type": "Finding"}, {"text": "CSF", "type": "BodySubstance"}, {"text": "negatively", "type": "Finding"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "grey matter", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Still , for the AR patients dorsal of the STN significantly more afferent than efferent connections were associated with coherence in the frequency range from 12 to 16Hz .

Example answer:
{"entities": [{"text": "AR", "type": "BiologicFunction"}, {"text": "dorsal", "type": "SpatialConcept"}, {"text": "STN", "type": "AnatomicalStructure"}, {"text": "afferent", "type": "SpatialConcept"}, {"text": "efferent", "type": "SpatialConcept"}, {"text": "connections", "type": "SpatialConcept"}, {"text": "coherence", "type": "BiologicFunction"}]}

Example input:
Sentence: We determined the association of different clinical , CSF and magnetic resonance imaging ( MRI ) parameters with prevalence and severity of fatigue , as measured by the Fatigue Scale for Motor and Cognitive Functions in 68 early MS patients ( discovery cohort ) .

Example answer:
{"entities": [{"text": "CSF", "type": "BodySubstance"}, {"text": "magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "fatigue", "type": "Finding"}, {"text": "Fatigue Scale for Motor and Cognitive Functions", "type": "IntellectualProduct"}, {"text": "MS", "type": "BiologicFunction"}, {"text": "discovery cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: During the first 2 min of ventricular fibrillation , low - frequency oscillations ( 4 - 7 Hz ) dominated , while on min 3 to 10 after the onset of fibrillation , the dominant frequencies were low and medium ( 4 - 12 Hz ) .

Example answer:
{"entities": [{"text": "ventricular fibrillation", "type": "BiologicFunction"}, {"text": "fibrillation", "type": "BiologicFunction"}, {"text": "dominant frequencies", "type": "Finding"}]}

Example input:
Sentence: Fusional amplitude improved in treatment group but decreased in control group at 3 - and 6 - months visits ( p < 0 .

Example answer:
{"entities": [{"text": "Fusional amplitude", "type": "Finding"}, {"text": "improved", "type": "Finding"}, {"text": "treatment group", "type": "PopulationGroup"}, {"text": "visits", "type": "HealthCareActivity"}]}

Example input:
Sentence: Across curvature s , legibility decreased by 2 % - 8 % , whereas perceived visual fatigue increased by 22 % during the second task set .

Example answer:
{"entities": [{"text": "curvature", "type": "SpatialConcept"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "visual fatigue", "type": "BiologicFunction"}]}

Example input:
Sentence: Brain activation following tendon vibration at 100Hz ( ' illusion ' ) and 30Hz ( ' no illusion ' ) were analysed using the two - stage random effects model , with or without white and grey matter covariates .

Example answer:
{"entities": [{"text": "Brain", "type": "AnatomicalStructure"}, {"text": "tendon", "type": "AnatomicalStructure"}, {"text": "vibration", "type": "HealthCareActivity"}, {"text": "' illusion '", "type": "BiologicFunction"}, {"text": "no", "type": "Finding"}, {"text": "illusion", "type": "BiologicFunction"}, {"text": "analysed", "type": "ResearchActivity"}, {"text": "white", "type": "AnatomicalStructure"}, {"text": "grey matter", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Before the 3Hz - AO training cortical excitability was highest during the observation of the 2Hz video .

Example answer:
{"entities": [{"text": "cortical excitability", "type": "BiologicFunction"}, {"text": "video", "type": "IntellectualProduct"}]}

Example input:
Sentence: Paired samples statistical analyses revealed that mean F0 decreased from 215 Hz ( standard deviation [ SD ] = 40 Hz ) to 201 Hz ( SD = 65 Hz ) following surgery .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Relative to the corresponding centre zone , the outermost zones of the 1200 - mm and flat settings showed a decrease of 8 % - 37 % in legibility , whereas those of the flat setting showed an increase of 26 % - 45 % in perceived visual fatigue .

Example answer:
{"entities": [{"text": "centre", "type": "SpatialConcept"}, {"text": "zone", "type": "SpatialConcept"}, {"text": "zones", "type": "SpatialConcept"}, {"text": "flat", "type": "SpatialConcept"}, {"text": "settings", "type": "SpatialConcept"}, {"text": "setting", "type": "SpatialConcept"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "visual fatigue", "type": "BiologicFunction"}]}

Input:
Sentence: 3 Hz in the critical fusion frequency , both of which indicated an increase in visual fatigue .

## Item MedMentions:test:3053
Example input:
Sentence: Monolithic and ceramic veneered ( n = 10 ) three - unit restorations ( retainers : first premolar and first molar ; pontic : second premolar ) were subject to endodontic access cavity preparation in both retainers using a diamond rotary instrument under continuous water cooling .

Example answer:
{"entities": [{"text": "ceramic", "type": "Chemical"}, {"text": "veneered", "type": "Chemical"}, {"text": "restorations", "type": "HealthCareActivity"}, {"text": "retainers", "type": "MedicalDevice"}, {"text": "first premolar", "type": "AnatomicalStructure"}, {"text": "first molar", "type": "AnatomicalStructure"}, {"text": "pontic", "type": "MedicalDevice"}, {"text": "second premolar", "type": "AnatomicalStructure"}, {"text": "endodontic access cavity preparation", "type": "HealthCareActivity"}, {"text": "water", "type": "Chemical"}]}

Example input:
Sentence: A search of English peer - reviewed dental literature ( 2003 - 2015 ) from PubMed and MEDLINE databases was conducted with the terms " low shrinkage " and " silorane composites . " The list was screened , and 70 articles that were relevant to the objectives of this work were included .

Example answer:
{"entities": [{"text": "peer - reviewed dental literature", "type": "IntellectualProduct"}, {"text": "PubMed", "type": "IntellectualProduct"}, {"text": "MEDLINE", "type": "IntellectualProduct"}, {"text": "databases", "type": "IntellectualProduct"}, {"text": "silorane composites", "type": "Chemical"}, {"text": "articles", "type": "IntellectualProduct"}, {"text": "objectives", "type": "IntellectualProduct"}]}

Example input:
Sentence: 15 , 16 , and 17 were developmentally delayed and were displaying the characteristic " ghost appearance . " Comprehensive dental care was done under local anaesthesia and it included extraction of the primary molars affected by ROD , stainless steel crown on 64 , and caries prevention program .

Example answer:
{"entities": [{"text": "Comprehensive dental care", "type": "HealthCareActivity"}, {"text": "local anaesthesia", "type": "HealthCareActivity"}, {"text": "extraction", "type": "HealthCareActivity"}, {"text": "primary molars", "type": "Finding"}, {"text": "ROD", "type": "AnatomicalStructure"}, {"text": "stainless steel crown", "type": "MedicalDevice"}, {"text": "caries", "type": "BiologicFunction"}]}

Example input:
Sentence: Appearance Differences Between Lots and Brands of Similar Shade Designations of Dental Composite Resins The purposes of this study were to investigate differences in two inherent appearance characteristics between lots of an enamel dental composite resin of the same shade and brand , and to further compare these differences to those of similar shade designation of a different brand of dental composite resins .

Example answer:
{"entities": [{"text": "Lots", "type": "IntellectualProduct"}, {"text": "Brands", "type": "IntellectualProduct"}, {"text": "Designations", "type": "IntellectualProduct"}, {"text": "Dental Composite Resins", "type": "Chemical"}, {"text": "study", "type": "ResearchActivity"}, {"text": "lots", "type": "IntellectualProduct"}, {"text": "enamel dental composite resin", "type": "Chemical"}, {"text": "brand", "type": "IntellectualProduct"}, {"text": "designation", "type": "IntellectualProduct"}, {"text": "dental composite resins", "type": "Chemical"}]}

Example input:
Sentence: Recent coating developments for combination devices in orthopedic and dental applications : A literature review Orthopedic and dental implants have been used successfully for decades to replace or repair missing or damaged bones , joints , and teeth , thereby restoring patient function subsequent to disease or injury .

Example answer:
{"entities": [{"text": "combination devices", "type": "MedicalDevice"}, {"text": "orthopedic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "dental applications", "type": "HealthCareActivity"}, {"text": "literature review", "type": "IntellectualProduct"}, {"text": "Orthopedic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "dental implants", "type": "MedicalDevice"}, {"text": "repair", "type": "HealthCareActivity"}, {"text": "bones", "type": "AnatomicalStructure"}, {"text": "joints", "type": "SpatialConcept"}, {"text": "teeth", "type": "AnatomicalStructure"}, {"text": "restoring", "type": "HealthCareActivity"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Considering the missing of the permanent successor , the tooth was disinfected during endodontic preparation and the root canal system was filled with calcium - enriched mixture ( CEM ) cement in the same session .

Example answer:
{"entities": [{"text": "permanent successor", "type": "AnatomicalStructure"}, {"text": "tooth", "type": "AnatomicalStructure"}, {"text": "endodontic preparation", "type": "HealthCareActivity"}, {"text": "root canal", "type": "SpatialConcept"}, {"text": "filled", "type": "HealthCareActivity"}, {"text": "calcium - enriched mixture ( CEM ) cement", "type": "Chemical"}]}

Example input:
Sentence: The aim of this study was to compare surface roughness of enamel in teeth bleached using Diode and Neodymium - Doped Yttrium Aluminium Garnet ( Nd : YAG ) lasers with those bleached using conventional method .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "surface roughness", "type": "Finding"}, {"text": "enamel", "type": "BodySubstance"}, {"text": "teeth bleached", "type": "HealthCareActivity"}, {"text": "Diode", "type": "MedicalDevice"}, {"text": "Neodymium - Doped Yttrium Aluminium Garnet ( Nd : YAG ) lasers", "type": "MedicalDevice"}, {"text": "bleached", "type": "HealthCareActivity"}]}

Example input:
Sentence: In order to evaluate tooth discoloration , the pulp chamber of 60 human maxillary central and lateral incisors were filled with one of the sealers , naming AH - 26 ( resin - based sealer ) , Pulpdent sealer ( ZOE -based ) and a NZOE experimental sealer .

Example answer:
{"entities": [{"text": "tooth discoloration", "type": "Finding"}, {"text": "pulp chamber", "type": "SpatialConcept"}, {"text": "human", "type": "Eukaryote"}, {"text": "maxillary central", "type": "AnatomicalStructure"}, {"text": "lateral incisors", "type": "AnatomicalStructure"}, {"text": "sealers", "type": "Chemical"}, {"text": "AH - 26", "type": "Chemical"}, {"text": "resin - based sealer", "type": "Chemical"}, {"text": "Pulpdent", "type": "Chemical"}, {"text": "sealer", "type": "Chemical"}, {"text": "ZOE", "type": "Chemical"}, {"text": "NZOE", "type": "Chemical"}]}

Example input:
Sentence: Computerized tomography scan of wax model of socket was converted into three dimensional format using Materialize Interactive Medical Image Control System ( MIMICS ) software and further refined .

Example answer:
{"entities": [{"text": "wax", "type": "Chemical"}, {"text": "three dimensional", "type": "SpatialConcept"}, {"text": "Materialize Interactive Medical Image Control System", "type": "HealthCareActivity"}, {"text": "MIMICS", "type": "HealthCareActivity"}, {"text": "software", "type": "IntellectualProduct"}]}

Example input:
Sentence: Reassessment has revealed varying levels of completeness for our available AM dental records , the need to thoroughly review our computerized comparisons , adjust our comparisons to include molar pattern variations / third molars , and updating our database comparison program .

Example answer:
{"entities": [{"text": "dental records", "type": "IntellectualProduct"}, {"text": "review", "type": "IntellectualProduct"}, {"text": "molar", "type": "AnatomicalStructure"}, {"text": "pattern", "type": "SpatialConcept"}, {"text": "molars", "type": "AnatomicalStructure"}, {"text": "database", "type": "IntellectualProduct"}]}

Input:
Sentence: Computer - aided design and computer - aided manufacturing ( CAD - CAM ) systems can generate and store libraries of teeth with various anatomies in their database , and diagnostic tooth waxing may not be required .

## Item MedMentions:test:3222
Example input:
Sentence: Retrospective review was performed of records of 83 patients with HCC who underwent ( 90 ) Y glass microsphere radioembolization with ( 99m ) Tc - MAA single photon emission computed tomography ( SPECT ) and ( 90 ) Y positron emission tomography ( PET ) / CT between January 2013 and December 2014 .

Example answer:
{"entities": [{"text": "Retrospective review", "type": "ResearchActivity"}, {"text": "records", "type": "IntellectualProduct"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "( 90 ) Y", "type": "Chemical"}, {"text": "glass microsphere", "type": "MedicalDevice"}, {"text": "radioembolization", "type": "HealthCareActivity"}, {"text": "( 99m ) Tc - MAA", "type": "Chemical"}, {"text": "single photon emission computed tomography", "type": "HealthCareActivity"}, {"text": "SPECT", "type": "HealthCareActivity"}, {"text": "positron emission tomography", "type": "HealthCareActivity"}, {"text": "( PET ) / CT", "type": "HealthCareActivity"}]}

Example input:
Sentence: We conducted a retrospective cohort study of cirrhotic patients without prior bleeding who initiated a NSBB ( propranolol , nadolol ) at any Veterans Administration facility between 2008 and 2013 .

Example answer:
{"entities": [{"text": "retrospective cohort study", "type": "ResearchActivity"}, {"text": "cirrhotic", "type": "BiologicFunction"}, {"text": "bleeding", "type": "BiologicFunction"}, {"text": "propranolol", "type": "Chemical"}, {"text": "nadolol", "type": "Chemical"}, {"text": "Veterans Administration facility", "type": "Organization"}]}

Example input:
Sentence: A venous ( adults ) or capillary ( children ) sample was taken for immediate HbA1c analysis .

Example answer:
{"entities": [{"text": "venous", "type": "BodySubstance"}, {"text": "capillary ( children ) sample", "type": "BodySubstance"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Medical records from patients who suffered serious AEs ( major bleed , embolic stroke , venous thromboembolism ) were reviewed , and AMS staff were interviewed to determine the root cause using the " 5 Whys " technique .

Example answer:
{"entities": [{"text": "Medical records", "type": "IntellectualProduct"}, {"text": "AEs", "type": "BiologicFunction"}, {"text": "major bleed", "type": "BiologicFunction"}, {"text": "embolic stroke", "type": "BiologicFunction"}, {"text": "venous thromboembolism", "type": "BiologicFunction"}, {"text": "AMS", "type": "Organization"}, {"text": "staff", "type": "ProfessionalOrOccupationalGroup"}, {"text": "\" 5 Whys \" technique", "type": "IntellectualProduct"}]}

Example input:
Sentence: TEE findings changed management ( initiation of anticoagulation therapy , administration of IV antibiotic therapy , and patent foramen ovale closure ) in 10 ( 16 % [ 95 % CI : 9 % - 28 % ] ) patients .

Example answer:
{"entities": [{"text": "TEE", "type": "HealthCareActivity"}, {"text": "findings", "type": "Finding"}, {"text": "anticoagulation therapy", "type": "HealthCareActivity"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "IV antibiotic therapy", "type": "HealthCareActivity"}, {"text": "patent foramen ovale closure", "type": "HealthCareActivity"}]}

Example input:
Sentence: In subgroup analysis , the rates of initiation of anticoagulation therapy on the basis of TEE investigation did not differ ( p = 0 . 315 ) among patients with cryptogenic stroke ( 6 . 9 % [ 95 % CI : 4 . 9 % - 9 . 6 % ] ) , ESUS ( 8 . 1 % [ 95 % CI : 3 . 4 % - 18 . 1 % ] ) , and IS ( 9 . 4 % [ 95 % CI : 7 .

Example answer:
{"entities": [{"text": "subgroup analysis", "type": "ResearchActivity"}, {"text": "anticoagulation therapy", "type": "HealthCareActivity"}, {"text": "TEE", "type": "HealthCareActivity"}, {"text": "ESUS", "type": "BiologicFunction"}, {"text": "IS", "type": "BiologicFunction"}]}

Example input:
Sentence: The pooled rate of reported anticoagulation therapy attributed to abnormal TEE findings among 3 , 562 acute IS patients included in the meta - analysis ( 12 studies ) was 8 . 7 % ( 95 % CI : 7 . 3 % - 10 . 4 % ) .

Example answer:
{"entities": [{"text": "anticoagulation therapy", "type": "HealthCareActivity"}, {"text": "abnormal", "type": "Finding"}, {"text": "TEE", "type": "HealthCareActivity"}, {"text": "findings", "type": "Finding"}, {"text": "IS", "type": "BiologicFunction"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Lipids were assessed in patients with a first venous thrombosis ( n = 2106 ) followed for 6 .

Example answer:
{"entities": [{"text": "Lipids", "type": "Chemical"}, {"text": "venous thrombosis", "type": "BiologicFunction"}]}

Example input:
Sentence: They stated that venous thromboembolism ( VTE ) had been seen in 21 ( 4 . 6 % ) of their patients .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "BiologicFunction"}, {"text": "VTE", "type": "BiologicFunction"}]}

Example input:
Sentence: We performed a large epidemiologic study on hospital admissions for portal vein thrombosis ( PVT ) and the Budd - Chiari syndrome ( BCS ) between 2002 and 2012 in Northwestern Italy .

Example answer:
{"entities": [{"text": "epidemiologic study", "type": "ResearchActivity"}, {"text": "hospital admissions", "type": "HealthCareActivity"}, {"text": "portal vein thrombosis", "type": "BiologicFunction"}, {"text": "PVT", "type": "BiologicFunction"}, {"text": "Budd - Chiari syndrome", "type": "BiologicFunction"}, {"text": "BCS", "type": "BiologicFunction"}, {"text": "Northwestern Italy", "type": "SpatialConcept"}]}

Input:
Sentence: Patients /Methods Patients with a first venous thrombosis from the MEGA study were included .

## Item MedMentions:test:2885
Example input:
Sentence: Antenatal Stressful Life Events and Postpartum Depressive Symptoms in the United States : The Role of Women 's Socioeconomic Status Indices at the State Level Approximately 10 % - 20 % of women suffer from postpartum depression ( PPD ) , important predictors of which are antenatal stressful life event ( SLE ) experiences .

Example answer:
{"entities": [{"text": "Depressive Symptoms", "type": "Finding"}, {"text": "United States", "type": "SpatialConcept"}, {"text": "Women 's", "type": "PopulationGroup"}, {"text": "Indices", "type": "IntellectualProduct"}, {"text": "women", "type": "PopulationGroup"}, {"text": "suffer", "type": "BiologicFunction"}, {"text": "postpartum depression", "type": "BiologicFunction"}, {"text": "PPD", "type": "BiologicFunction"}]}

Example input:
Sentence: Amongst all the parasites , Toxocara canis ( 44 . 93 % ) infection was highest , followed by Dipylidium caninum ( 17 . 39 % ) and hookworms ( 15 . 94 % ) .

Example answer:
{"entities": [{"text": "parasites", "type": "Eukaryote"}, {"text": "Toxocara canis ( 44 . 93 % ) infection", "type": "BiologicFunction"}, {"text": "Dipylidium caninum", "type": "Eukaryote"}, {"text": "hookworms", "type": "Eukaryote"}]}

Example input:
Sentence: The scenario observed for the latter indicates that more than 80 % of childbearing women are susceptible to primary infection yielding a risk of congenital toxoplasmosis and respective sequelae .

Example answer:
{"entities": [{"text": "childbearing", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "congenital toxoplasmosis", "type": "BiologicFunction"}, {"text": "sequelae", "type": "BiologicFunction"}]}

Example input:
Sentence: Further , deworming had no effect on measured infant morbidity indicators .

Example answer:
{"entities": [{"text": "deworming", "type": "HealthCareActivity"}, {"text": "indicators", "type": "IntellectualProduct"}]}

Example input:
Sentence: The Effect of Oxygen Inhalation Plus Oxytocin Compared with Oxytocin Only on Postpartum Haemorrhage : A Randomized Clinical Trial Post Partum Haemorrhage ( PPH ) is the leading cause of maternal mortality across the world , mainly in the developing countries .

Example answer:
{"entities": [{"text": "Oxygen Inhalation", "type": "HealthCareActivity"}, {"text": "Oxytocin", "type": "Chemical"}, {"text": "Postpartum Haemorrhage", "type": "BiologicFunction"}, {"text": "Randomized Clinical Trial", "type": "ResearchActivity"}, {"text": "Post Partum Haemorrhage", "type": "BiologicFunction"}, {"text": "PPH", "type": "BiologicFunction"}, {"text": "world", "type": "PopulationGroup"}]}

Example input:
Sentence: Request and fulfillment of postpartum tubal ligation in patients after high - risk pregnancy Female sterilization is one of the most prevalent methods of contraception in the United States .

Example answer:
{"entities": [{"text": "tubal ligation", "type": "HealthCareActivity"}, {"text": "high - risk pregnancy", "type": "BiologicFunction"}, {"text": "Female sterilization", "type": "HealthCareActivity"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "contraception", "type": "HealthCareActivity"}, {"text": "United States", "type": "SpatialConcept"}]}

Example input:
Sentence: Among STH - infected mothers , however , important improvements in infant length gain and length - for - age were observed .

Example answer:
{"entities": [{"text": "STH - infected", "type": "BiologicFunction"}]}

Example input:
Sentence: A Double - Blind Randomized Controlled Trial of Maternal Postpartum Deworming to Improve Infant Weight Gain in the Peruvian Amazon Nutritional interventions targeting the critical growth and development period before two years of age can have the greatest impact on health trajectories over the life course .

Example answer:
{"entities": [{"text": "Double - Blind", "type": "ResearchActivity"}, {"text": "Randomized Controlled Trial", "type": "ResearchActivity"}, {"text": "Maternal Postpartum", "type": "BiologicFunction"}, {"text": "Deworming", "type": "HealthCareActivity"}, {"text": "Weight Gain", "type": "Finding"}, {"text": "Nutritional interventions", "type": "HealthCareActivity"}]}

Example input:
Sentence: In a study population composed of both STH - infected and uninfected mothers , maternal postpartum deworming was insufficient to impact infant growth and morbidity indicators up to 6 months postpartum .

Example answer:
{"entities": [{"text": "study population", "type": "PopulationGroup"}, {"text": "STH - infected", "type": "BiologicFunction"}, {"text": "maternal postpartum", "type": "BiologicFunction"}, {"text": "deworming", "type": "HealthCareActivity"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "indicators", "type": "IntellectualProduct"}]}

Example input:
Sentence: One such potential intervention is deworming integrated into maternal postpartum care in areas where soil - transmitted helminth ( STH ) infections are endemic .

Example answer:
{"entities": [{"text": "intervention", "type": "HealthCareActivity"}, {"text": "deworming", "type": "HealthCareActivity"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "helminth", "type": "Eukaryote"}, {"text": "STH", "type": "Eukaryote"}, {"text": "infections", "type": "BiologicFunction"}, {"text": "endemic", "type": "BiologicFunction"}]}

Input:
Sentence: The benefits of maternal postpartum deworming should be further investigated in study populations having higher overall prevalences and intensities of STH infections and , in particular , where whipworm and hookworm infections are of public health concern .

## Item MedMentions:test:3216
Example input:
Sentence: Hyposalivation , rheumatoid arthritis , smoking / tobacco use , undiagnosed or sub - optimally controlled diabetes and obesity are common acquired risk factors for both caries and periodontal diseases .

Example answer:
{"entities": [{"text": "Hyposalivation", "type": "Finding"}, {"text": "rheumatoid arthritis", "type": "BiologicFunction"}, {"text": "smoking / tobacco use", "type": "Finding"}, {"text": "undiagnosed", "type": "Finding"}, {"text": "sub - optimally controlled", "type": "Finding"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "caries", "type": "BiologicFunction"}, {"text": "periodontal diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Our current understanding of this disease is that specific bacteria invade the oral cavity and the host reacts with an inflammatory response leading to mass destruction of the alveolar bone .

Example answer:
{"entities": [{"text": "disease", "type": "BiologicFunction"}, {"text": "specific bacteria", "type": "Bacterium"}, {"text": "oral cavity", "type": "SpatialConcept"}, {"text": "alveolar bone", "type": "HealthCareActivity"}]}

Example input:
Sentence: The objective of this study is to examine the relationship between frequent recreational cannabis ( FRC ) ( marijuana and hashish ) use and periodontitis prevalence among adults in the United States .

Example answer:
{"entities": [{"text": "recreational", "type": "BiologicFunction"}, {"text": "cannabis", "type": "BiologicFunction"}, {"text": "FRC", "type": "BiologicFunction"}, {"text": "marijuana", "type": "BiologicFunction"}, {"text": "hashish ) use", "type": "BiologicFunction"}, {"text": "periodontitis", "type": "BiologicFunction"}, {"text": "United States", "type": "SpatialConcept"}]}

Example input:
Sentence: Porphyromonus gingivalis ( P . gingivalis ) , a major periodontal pathogen , has already been shown to have a significant role in the inflammatory response of CAD in vivo .

Example answer:
{"entities": [{"text": "Porphyromonus gingivalis", "type": "Bacterium"}, {"text": "P . gingivalis", "type": "Bacterium"}, {"text": "inflammatory response", "type": "BiologicFunction"}, {"text": "CAD", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: Interaction of lifestyle , behaviour or systemic diseases with dental caries and periodontal diseases : consensus report of group 2 of the joint EFP / ORCA workshop on the boundaries between caries and periodontal diseases Periodontal diseases and dental caries are the most common diseases of humans and the main cause of tooth loss .

Example answer:
{"entities": [{"text": "systemic diseases", "type": "BiologicFunction"}, {"text": "dental caries", "type": "BiologicFunction"}, {"text": "periodontal diseases", "type": "BiologicFunction"}, {"text": "consensus report of group 2 of the joint EFP / ORCA workshop", "type": "ProfessionalOrOccupationalGroup"}, {"text": "caries", "type": "BiologicFunction"}, {"text": "Periodontal diseases", "type": "BiologicFunction"}, {"text": "common diseases", "type": "BiologicFunction"}, {"text": "tooth loss", "type": "AnatomicalStructure"}]}

Example input:
Sentence: PD accounts for the majority of tooth loss and increases with age . China 's third national epidemiological investigation on oral diseases ( 2005 ) revealed that periodontitis affected > 50 % of the adult population .

Example answer:
{"entities": [{"text": "PD", "type": "BiologicFunction"}, {"text": "tooth loss", "type": "AnatomicalStructure"}, {"text": "China 's", "type": "SpatialConcept"}, {"text": "national epidemiological investigation", "type": "ResearchActivity"}, {"text": "oral diseases", "type": "BiologicFunction"}, {"text": "periodontitis", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: Oral health is becoming a major public health problem as the prevalence of non - communicable diseases has greatly increased .

Example answer:
{"entities": [{"text": "Oral health", "type": "HealthCareActivity"}, {"text": "public", "type": "Organization"}, {"text": "non - communicable diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Periodontal disease ( PD ) and caries are among the most prevalent oral diseases .

Example answer:
{"entities": [{"text": "Periodontal disease", "type": "BiologicFunction"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "caries", "type": "BiologicFunction"}, {"text": "oral diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Aggressive periodontal disease has a tremendous effect on patients ' overall quality of life and needs to be investigated more extensively in order to develop methods for earlier definitive diagnosis and effective treatments .

Example answer:
{"entities": [{"text": "Aggressive periodontal disease", "type": "BiologicFunction"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "definitive diagnosis", "type": "Finding"}, {"text": "treatments", "type": "HealthCareActivity"}]}

Example input:
Sentence: One of the mysteries of aggressive periodontal disease is the relatively nominal amount of plaque present on the tooth surface in relation to the large amount of bone loss .

Example answer:
{"entities": [{"text": "mysteries", "type": "Finding"}, {"text": "aggressive periodontal disease", "type": "BiologicFunction"}, {"text": "plaque", "type": "BiologicFunction"}, {"text": "tooth surface", "type": "SpatialConcept"}, {"text": "bone loss", "type": "BiologicFunction"}]}

Input:
Sentence: Aggressive periodontitis : The unsolved mystery Aggressive periodontal disease is an oral health mystery .

## Item MedMentions:test:3259
Example input:
Sentence: Apart from these handful of studies , the effects of GCs on aquatic biota are largely unknown .

Example answer:
{"entities": [{"text": "GCs", "type": "Chemical"}]}

Example input:
Sentence: Two species , O . franksi and S . michelini , later recovered to net positive growth , which continued until a second thermal stress event in 2010 .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "O . franksi", "type": "Eukaryote"}, {"text": "S . michelini", "type": "Eukaryote"}, {"text": "positive", "type": "Finding"}, {"text": "growth", "type": "BiologicFunction"}]}

Example input:
Sentence: There was some evidence that hypoxia tolerance was lower ( higher DO at LOE ) in hypoxia - raised fish compared with those raised in normoxia , but the magnitude of the effect was small ( 12 . 52 % DO vs .

Example answer:
{"entities": [{"text": "hypoxia", "type": "BiologicFunction"}, {"text": "DO", "type": "Chemical"}, {"text": "LOE", "type": "Finding"}, {"text": "fish", "type": "Eukaryote"}]}

Example input:
Sentence: Increasing evidence suggests that transmembrane water channels ( aquaporins ) evolved to play vital adaptive roles that mitigate the osmotic and oxidative stress problems of the developing oocytes , embryos and spermatozoa .

Example answer:
{"entities": [{"text": "transmembrane water channels", "type": "Chemical"}, {"text": "aquaporins", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "problems", "type": "Finding"}, {"text": "developing", "type": "BiologicFunction"}, {"text": "oocytes", "type": "AnatomicalStructure"}, {"text": "embryos", "type": "AnatomicalStructure"}, {"text": "spermatozoa", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Developmental Hypoxia Has Negligible Effects on Long - Term Hypoxia Tolerance and Aerobic Metabolism of Atlantic Salmon ( Salmo salar ) Exposure to developmental hypoxia can have long - term impacts on the physiological performance of fish because of irreversible plasticity .

Example answer:
{"entities": [{"text": "Hypoxia", "type": "BiologicFunction"}, {"text": "Aerobic Metabolism", "type": "BiologicFunction"}, {"text": "Atlantic Salmon", "type": "Eukaryote"}, {"text": "Salmo salar", "type": "Eukaryote"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "physiological", "type": "BiologicFunction"}, {"text": "fish", "type": "Eukaryote"}]}

Example input:
Sentence: Multigenerational studies have proved to be an advantage in assessing the cumulative damage caused by aquatic toxicants at the population level of the exposed organisms over a period of successive generations using multiple biological endpoints .

Example answer:
{"entities": [{"text": "Multigenerational studies", "type": "ResearchActivity"}, {"text": "aquatic toxicants", "type": "Chemical"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: Their use has been linked to a host of deleterious effects in aquatic ecosystems such as osteoporosis in vertebrates , developmental impairments in molluscs and reduced fecundity and growth in cladocerans .

Example answer:
{"entities": [{"text": "osteoporosis", "type": "BiologicFunction"}, {"text": "vertebrates", "type": "Eukaryote"}, {"text": "developmental", "type": "BiologicFunction"}, {"text": "molluscs", "type": "Eukaryote"}, {"text": "fecundity", "type": "BiologicFunction"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "cladocerans", "type": "Eukaryote"}]}

Example input:
Sentence: What is more , these impacts do not always conform to ecological theory based on differential resource allocation towards reproduction , which would predict females to be more sensitive to OA owing to the higher production cost of eggs compared with sperm .

Example answer:
{"entities": [{"text": "reproduction", "type": "BiologicFunction"}, {"text": "eggs", "type": "AnatomicalStructure"}, {"text": "sperm", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The results from the current work highlighted the importance of multigenerational studies in identifying the evolutionary responses of stressed non - target aquatic organisms , and data obtained can be further used in developing water quality guidelines .

Example answer:
{"entities": [{"text": "multigenerational studies", "type": "ResearchActivity"}, {"text": "evolutionary", "type": "BiologicFunction"}, {"text": "stressed", "type": "Finding"}, {"text": "guidelines", "type": "IntellectualProduct"}]}

Example input:
Sentence: Here we highlight that sex can significantly impact organism responses to OA , differentially affecting physiology , reproduction , biochemistry and ultimately survival .

Example answer:
{"entities": [{"text": "physiology", "type": "BiologicFunction"}, {"text": "reproduction", "type": "BiologicFunction"}]}

Input:
Sentence: The number and complexity of experiments examining the effects of OA has substantially increased over the past decade , in an attempt to address multi - stressor interactions and long - term responses in an increasing range of aquatic organisms .

## Item MedMentions:test:3436
Example input:
Sentence: 64 ; 95 % CI = 1 . 39 - 1 . 93 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 86 , 95 % CI = 0 . 78 - 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 81 ( 95 % CI 0 . 65 , 1 . 01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 98 , 95 % CI : 0 . 8 - 1 . 17 , P < 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 00001 ; OR = 35 . 57 , 95 % CI = 19 . 61 - 64 . 51 , and p < 0 . 00001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 88 , 95 % CI : 1 . 51 - 2 . 33 , P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 83 ; 95 % CI : 0 . 62 - 1 . 11 , P = 0 . 21 ] .

Example answer:
{"entities": []}

Example input:
Sentence: 85 ( CI 95 % : 0 . 84 to 0 . 92 ) , respectively ( P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 62 ( 95 % CI , 0 . 52 - 0 . 73 ) and 0 . 70 ( 95 % CI , 0 . 50 - 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 68 ; 95 % CI , -10 . 74 to -2 . 62 ; P = 0 . 001 ) .

Example answer:
{"entities": []}

Input:
Sentence: 66 ; 95 % CI : 0 . 56 - 0 . 78 , P < 0 . 001 . ) .

## Item MedMentions:test:3024
Example input:
Sentence: Transcription factors of β - cell function ( INSIG1 , SREBP1c and PDX1 ) as well as hepatic gluconeogenesis ( FOXO1 and PEPCK ) were adversely affected in diet - induced insulin - resistant rats .

Example answer:
{"entities": [{"text": "Transcription factors", "type": "Chemical"}, {"text": "β - cell function", "type": "BiologicFunction"}, {"text": "INSIG1", "type": "Chemical"}, {"text": "SREBP1c", "type": "Chemical"}, {"text": "PDX1", "type": "Chemical"}, {"text": "hepatic", "type": "SpatialConcept"}, {"text": "gluconeogenesis", "type": "BiologicFunction"}, {"text": "FOXO1", "type": "Chemical"}, {"text": "PEPCK", "type": "Chemical"}, {"text": "adversely affected", "type": "BiologicFunction"}, {"text": "diet", "type": "Food"}, {"text": "insulin - resistant", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: The strong relationships with NP systems and inflammatory mediators could suggest an involvement for IL - 33 / ST2 in molecular pathways leading to cardiac dysfunction and inflammation associated with obesity .

Example answer:
{"entities": [{"text": "NP", "type": "Chemical"}, {"text": "inflammatory mediators", "type": "BiologicFunction"}, {"text": "IL - 33", "type": "Chemical"}, {"text": "ST2", "type": "Chemical"}, {"text": "molecular pathways", "type": "BiologicFunction"}, {"text": "cardiac dysfunction", "type": "Finding"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}]}

Example input:
Sentence: ATF3 expression in cardiomyocytes preserves homeostasis in the heart and controls peripheral glucose tolerance Obesity and type 2 diabetes ( T2D ) trigger a harmful stress - induced cardiac remodeling process known as cardiomyopathy .

Example answer:
{"entities": [{"text": "ATF3", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "cardiomyocytes", "type": "AnatomicalStructure"}, {"text": "homeostasis", "type": "BiologicFunction"}, {"text": "heart", "type": "AnatomicalStructure"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "Obesity", "type": "BiologicFunction"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "T2D", "type": "BiologicFunction"}, {"text": "stress", "type": "BiologicFunction"}, {"text": "cardiac remodeling process", "type": "BiologicFunction"}, {"text": "cardiomyopathy", "type": "BiologicFunction"}]}

Example input:
Sentence: Because the levels of IFN - β were lower in AH23848 - treated mice but the level of IL - 6 was similar , over - production of pathogenic IFN - β was modulated and the generation of IFN - γ - producing T cell responses was enhanced by the inhibition of PGE2 signaling .

Example answer:
{"entities": [{"text": "IFN - β", "type": "Chemical"}, {"text": "AH23848", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "over - production", "type": "BiologicFunction"}, {"text": "pathogenic", "type": "Finding"}, {"text": "modulated", "type": "SpatialConcept"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "producing", "type": "BiologicFunction"}, {"text": "T cell", "type": "AnatomicalStructure"}, {"text": "PGE2", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}]}

Example input:
Sentence: These results demonstrate the importance of skeletal muscle inflammation in aging -mediated insulin resistance , and our findings further implicate a potential therapeutic role of anti - inflammatory cytokine in the treatment of aging -mediated insulin resistance .

Example answer:
{"entities": [{"text": "skeletal muscle", "type": "AnatomicalStructure"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "aging", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "findings", "type": "Finding"}, {"text": "anti - inflammatory", "type": "Chemical"}, {"text": "cytokine", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: TLR4 deficiency in TLR4 - KO islets resulted in the inhibition of TNF - α production and IκBα phosphorylation after HMGB1 exposure .

Example answer:
{"entities": [{"text": "TLR4", "type": "Chemical"}, {"text": "TLR4", "type": "AnatomicalStructure"}, {"text": "KO", "type": "ResearchActivity"}, {"text": "islets", "type": "AnatomicalStructure"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "production", "type": "BiologicFunction"}, {"text": "IκBα", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "HMGB1", "type": "Chemical"}]}

Example input:
Sentence: Increasing evidence suggests that insulin resistance plays an important role in AD pathogenesis , possibly due to abnormal GSK3β activation , causing intra - and extracellular amyloid - beta ( Aβ ) accumulation .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "GSK3β", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "intra -", "type": "AnatomicalStructure"}, {"text": "extracellular", "type": "AnatomicalStructure"}]}

Example input:
Sentence: No associations or interactions were observed for glucose , TNF - α or IL - 6 .

Example answer:
{"entities": [{"text": "glucose", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}]}

Example input:
Sentence: AT inflammation is a key factor causing insulin resistance and thus type 2 diabetes , both linked to atherosclerotic cardiovascular disease .

Example answer:
{"entities": [{"text": "AT inflammation", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "atherosclerotic cardiovascular disease", "type": "BiologicFunction"}]}

Example input:
Sentence: The increased insulin resistance seen in RA is closely linked to the systemic inflammation induced by certain proinflammatory cytokines such as tumor necrosis factor α ( TNFα ) and interleukin - 6 .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "proinflammatory cytokines", "type": "Chemical"}, {"text": "tumor necrosis factor α", "type": "Chemical"}, {"text": "TNFα", "type": "Chemical"}, {"text": "interleukin - 6", "type": "Chemical"}]}

Input:
Sentence: Elevated levels of the cardiac inflammatory cytokines IL - 6 and TNFα leading to impaired insulin signalling may partially explain the peripheral glucose intolerance .

## Item MedMentions:test:3088
Example input:
Sentence: Twenty - five kinome array peptide substrates were differentially phoshorylated between LFPI and controls in the cortex , whereas 19 peptide substrates were differentially phosphorylated in the hippocampus ( fold change ≥ ± 1 . 15 ) .

Example answer:
{"entities": [{"text": "kinome array", "type": "IntellectualProduct"}, {"text": "peptide substrates", "type": "Chemical"}, {"text": "phoshorylated", "type": "BiologicFunction"}, {"text": "LFPI", "type": "IntellectualProduct"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "phosphorylated", "type": "BiologicFunction"}, {"text": "hippocampus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Finally , when infection was performed in the presence of an extracellular signal - regulated kinase 1 / 2 ( Erk1 / 2 ) inhibitor , MHC - I surface expression was significantly recovered .

Example answer:
{"entities": [{"text": "infection", "type": "BiologicFunction"}, {"text": "extracellular signal - regulated kinase 1 / 2", "type": "Chemical"}, {"text": "Erk1 / 2", "type": "Chemical"}, {"text": "inhibitor", "type": "Chemical"}, {"text": "MHC - I", "type": "Chemical"}, {"text": "surface", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}]}

Example input:
Sentence: The ErbB3 receptor tyrosine kinase negatively regulates Paneth cells by PI3 K - dependent suppression of Atoh1 Paneth cells ( PCs ) , a secretory population located at the base of the intestinal crypt , support the intestinal stem cells ( ISC ) with growth factors and participate in innate immunity by releasing antimicrobial peptides , including lysozyme and defensins .

Example answer:
{"entities": [{"text": "ErbB3 receptor tyrosine kinase", "type": "Chemical"}, {"text": "regulates", "type": "BiologicFunction"}, {"text": "Paneth cells", "type": "AnatomicalStructure"}, {"text": "PI3 K", "type": "Chemical"}, {"text": "suppression", "type": "BiologicFunction"}, {"text": "Atoh1", "type": "AnatomicalStructure"}, {"text": "PCs", "type": "AnatomicalStructure"}, {"text": "secretory population", "type": "AnatomicalStructure"}, {"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "stem cells", "type": "AnatomicalStructure"}, {"text": "ISC", "type": "AnatomicalStructure"}, {"text": "growth factors", "type": "Chemical"}, {"text": "antimicrobial peptides", "type": "Chemical"}, {"text": "lysozyme", "type": "Chemical"}, {"text": "defensins", "type": "Chemical"}]}

Example input:
Sentence: When prepared in the presence of phosphatase inhibitors , both WT - and SF - MRP1 -enriched membrane vesicles had a high Km value for As ( GS ) 3 ( 3 - 6 µM ) , regardless of the cell line .

Example answer:
{"entities": [{"text": "presence", "type": "Finding"}, {"text": "phosphatase inhibitors", "type": "Chemical"}, {"text": "WT -", "type": "Chemical"}, {"text": "SF - MRP1", "type": "Chemical"}, {"text": "membrane", "type": "AnatomicalStructure"}, {"text": "vesicles", "type": "AnatomicalStructure"}, {"text": "cell line", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Although positive deposits of S403 - p p62 and Lys63 -linked ubiquitin were always observed within p62 aggregates , LC3 often showed dissociated distribution from p62 .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "S403", "type": "Chemical"}, {"text": "p", "type": "Chemical"}, {"text": "p62", "type": "Chemical"}, {"text": "Lys63", "type": "Chemical"}, {"text": "ubiquitin", "type": "Chemical"}, {"text": "LC3", "type": "Chemical"}]}

Example input:
Sentence: Finally , we show that the ERK2 - IQGAP1 interaction does not require ERK2 phosphorylation or catalytic activity and does not involve known docking recruitment sites on ERK2 , and we obtain an estimate of the dissociation constant ( Kd ) for this interaction of 8 μm These results prompt a re - evaluation of published findings and a refined model of IQGAP scaffolding .

Example answer:
{"entities": [{"text": "ERK2", "type": "Chemical"}, {"text": "IQGAP1", "type": "Chemical"}, {"text": "interaction", "type": "BiologicFunction"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "docking", "type": "BiologicFunction"}, {"text": "sites", "type": "SpatialConcept"}, {"text": "findings", "type": "Finding"}, {"text": "refined model", "type": "IntellectualProduct"}, {"text": "IQGAP scaffolding", "type": "Chemical"}]}

Example input:
Sentence: These interactions could explain the long - lasting ERK1 / 2 phosphorylation and the cytoskeleton perturbations in the MDA - MB - 231 cells , in which the stress fibers ' integrity is affected by pep5 treatments .

Example answer:
{"entities": [{"text": "ERK1 / 2", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "cytoskeleton", "type": "AnatomicalStructure"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "stress fibers", "type": "AnatomicalStructure"}, {"text": "pep5", "type": "Chemical"}, {"text": "treatments", "type": "HealthCareActivity"}]}

Example input:
Sentence: Indeed , phosphorylation of several signaling proteins , including SLP76 itself , phospholipase Cγ1 and the protein kinases AKT and ERK1 / 2 , was increased .

Example answer:
{"entities": [{"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "signaling proteins", "type": "Chemical"}, {"text": "SLP76", "type": "Chemical"}, {"text": "phospholipase Cγ1", "type": "Chemical"}, {"text": "protein kinases AKT", "type": "Chemical"}, {"text": "ERK1", "type": "Chemical"}, {"text": "2", "type": "Chemical"}]}

Example input:
Sentence: Pep5 induced permanent extracellular signal - regulated kinase ( ERK1 / 2 ) phosphorylation in MDA - MB - 231 cells synchronized in G1 / S or S phase .

Example answer:
{"entities": [{"text": "Pep5", "type": "Chemical"}, {"text": "extracellular signal - regulated kinase", "type": "Chemical"}, {"text": "ERK1 / 2", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "G1 / S", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , phosphorylated - ERK / ERK ratios were significantly decreased in naïve LysMcreTNF ( fl / fl ) mice demonstrating altered ERK signal transduction .

Example answer:
{"entities": [{"text": "phosphorylated - ERK", "type": "Chemical"}, {"text": "ERK", "type": "Chemical"}, {"text": "naïve LysMcreTNF ( fl / fl ) mice", "type": "Eukaryote"}, {"text": "signal transduction", "type": "BiologicFunction"}]}

Input:
Sentence: Successful preconcentration and separation of a mixture of ERK2 derived peptides differing only by their phosphorylation degree and sites could be achieved with signal enhancement factors between 340 and 910 after only 7 min of preconcentration .

## Item MedMentions:test:3284
Example input:
Sentence: Living on the edge : substrate competition explains loss of robustness in mitochondrial fatty - acid oxidation disorders Defects in genes involved in mitochondrial fatty - acid oxidation ( mFAO ) reduce the ability of patients to cope with metabolic challenges .

Example answer:
{"entities": [{"text": "mitochondrial", "type": "AnatomicalStructure"}, {"text": "fatty - acid oxidation disorders", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "fatty - acid oxidation", "type": "BiologicFunction"}, {"text": "mFAO", "type": "BiologicFunction"}]}

Example input:
Sentence: We conclude that substrate competition is at the basis of the physiology seen in patients with mFAO disorders , a finding that may explain why these patients run a risk of a life - threatening metabolic catastrophe .

Example answer:
{"entities": [{"text": "physiology", "type": "BiologicFunction"}, {"text": "mFAO disorders", "type": "BiologicFunction"}, {"text": "finding", "type": "Finding"}, {"text": "life - threatening metabolic catastrophe", "type": "Finding"}]}

Example input:
Sentence: Tailored acquisitions can be designed to detect , for example , the inhibitory neurotransmitter γ - aminobutyric acid ( GABA ) , or the reduction - oxidation ( redox ) compound glutathione ( GSH ) , and single - voxel edited experiments are generally acquired at a rate of one metabolite - per - experiment .

Example answer:
{"entities": [{"text": "detect", "type": "HealthCareActivity"}, {"text": "neurotransmitter", "type": "Chemical"}, {"text": "γ - aminobutyric acid", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}, {"text": "reduction - oxidation", "type": "BiologicFunction"}, {"text": "redox", "type": "BiologicFunction"}, {"text": "glutathione", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "experiments", "type": "ResearchActivity"}, {"text": "metabolite", "type": "Chemical"}, {"text": "per - experiment", "type": "ResearchActivity"}]}

Example input:
Sentence: Here , we combined computational modeling with quantitative mouse and patient data to investigate whether substrate competition affects pathway robustness in mFAO disorders .

Example answer:
{"entities": [{"text": "mouse", "type": "Eukaryote"}, {"text": "mFAO disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: They produced high granzyme B , perforin , TNF - α , and IFNγ levels , and promoted tumor - killing efficiency ex vitro .

Example answer:
{"entities": [{"text": "granzyme B", "type": "Chemical"}, {"text": "perforin", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "IFNγ", "type": "Chemical"}, {"text": "tumor - killing efficiency", "type": "HealthCareActivity"}]}

Example input:
Sentence: Thermal inactivation and thermal denaturation analysis revealed that Glu138Pro mutation increased half - life and Tm of enzyme , respectively .

Example answer:
{"entities": [{"text": "denaturation", "type": "BiologicFunction"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "Glu138Pro", "type": "SpatialConcept"}, {"text": "mutation", "type": "BiologicFunction"}, {"text": "enzyme", "type": "Chemical"}]}

Example input:
Sentence: These results suggest that in vitro enzymatic glycosylation is a powerful approach to structural modification , improving water - solubility .

Example answer:
{"entities": [{"text": "enzymatic", "type": "Chemical"}, {"text": "structural modification", "type": "HealthCareActivity"}]}

Example input:
Sentence: Conversely , active glycolysis with decreased GAPDH availability in TEM resulted in elevated HIF1α expression .

Example answer:
{"entities": [{"text": "glycolysis", "type": "BiologicFunction"}, {"text": "GAPDH", "type": "Chemical"}, {"text": "TEM", "type": "AnatomicalStructure"}, {"text": "HIF1α", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , a single rigidifying mutation within this loop can significantly improve the enzyme specific activity , as well as the stability to thermal denaturation and aggregation , to give an increased temperature optimum for activity .

Example answer:
{"entities": [{"text": "single rigidifying mutation", "type": "BiologicFunction"}, {"text": "loop", "type": "SpatialConcept"}, {"text": "enzyme specific activity", "type": "BiologicFunction"}, {"text": "denaturation", "type": "BiologicFunction"}, {"text": "activity", "type": "BiologicFunction"}]}

Example input:
Sentence: First , we constructed generalized additive models ( GAMs ) that described the association between changes in specific metabolite concentrations with changes in enzymatic activities and substrate concentrations .

Example answer:
{"entities": [{"text": "metabolite", "type": "Chemical"}, {"text": "enzymatic activities", "type": "BiologicFunction"}]}

Input:
Sentence: Addition of information on enzymatic activities almost always improved the fitness of GAMs built solely based on substrate concentrations .

## Item MedMentions:test:2995
Example input:
Sentence: The objective of the study was to test the potential ovarian cancer chemopreventive effect of the p53 stabilizing compound CP - 31398 on hens that spontaneously present the ovarian cancer phenotype .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "BiologicFunction"}, {"text": "p53", "type": "Chemical"}, {"text": "stabilizing compound", "type": "Chemical"}, {"text": "CP - 31398", "type": "Chemical"}, {"text": "hens", "type": "Eukaryote"}]}

Example input:
Sentence: Neurotrophins and specific receptors in the oviduct tracts of Japanese quail ( Coturnix coturnix japonica ) Neurotrophins ( NGF , BDNF and NT - 3 ) and their specific receptors ( TrkA , TrkB and TrkC ) were studied in the oviduct of egg laying quails .

Example answer:
{"entities": [{"text": "Neurotrophins", "type": "Chemical"}, {"text": "specific receptors", "type": "Chemical"}, {"text": "oviduct tracts", "type": "AnatomicalStructure"}, {"text": "Japanese quail", "type": "Eukaryote"}, {"text": "Coturnix coturnix japonica", "type": "Eukaryote"}, {"text": "NGF", "type": "Chemical"}, {"text": "BDNF", "type": "Chemical"}, {"text": "NT - 3", "type": "Chemical"}, {"text": "TrkA", "type": "Chemical"}, {"text": "TrkB", "type": "Chemical"}, {"text": "TrkC", "type": "Chemical"}, {"text": "studied", "type": "ResearchActivity"}, {"text": "oviduct", "type": "AnatomicalStructure"}, {"text": "egg laying", "type": "BiologicFunction"}, {"text": "quails", "type": "Eukaryote"}]}

Example input:
Sentence: Host - induced gene silencing ( HIGS ) strategy was used to generate the transgenic eggplants expressing msp - 18 and msp - 20 , independently .

Example answer:
{"entities": [{"text": "gene silencing", "type": "BiologicFunction"}, {"text": "HIGS", "type": "BiologicFunction"}, {"text": "transgenic eggplants", "type": "Eukaryote"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "msp - 18", "type": "AnatomicalStructure"}, {"text": "msp - 20", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Anxiolytic effects of fluoxetine and nicotine exposure on exploratory behavior in zebrafish Zebrafish ( Danio rerio ) have emerged as a popular model for studying the pharmacology and behavior of anxiety .

Example answer:
{"entities": [{"text": "Anxiolytic effects", "type": "BiologicFunction"}, {"text": "fluoxetine", "type": "Chemical"}, {"text": "nicotine", "type": "Chemical"}, {"text": "zebrafish", "type": "Eukaryote"}, {"text": "Zebrafish", "type": "Eukaryote"}, {"text": "Danio rerio", "type": "Eukaryote"}, {"text": "studying", "type": "ResearchActivity"}, {"text": "anxiety", "type": "Finding"}]}

Example input:
Sentence: MeHg accumulation in the brain causes histopathological alterations , neurobehavioral changes , and impairments to cognitive motor functions in mammalian models .

Example answer:
{"entities": [{"text": "MeHg", "type": "Chemical"}, {"text": "accumulation", "type": "Finding"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "motor functions", "type": "BiologicFunction"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "models", "type": "BiologicFunction"}]}

Example input:
Sentence: Eimeria appeared to be more important than fishmeal in predisposing birds to NE , thus the application of Eimeria in NE challenge provides more consistent success in inducing the disease .

Example answer:
{"entities": [{"text": "Eimeria", "type": "Eukaryote"}, {"text": "birds", "type": "Eukaryote"}, {"text": "NE", "type": "BiologicFunction"}, {"text": "challenge", "type": "HealthCareActivity"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Chemoprevention of spontaneous ovarian cancer in the domestic hen The hen is an attractive animal model for in vivo testing of agents that thwart ovarian carcinogenesis because ovarian cancer in the domestic hen features clinical and molecular alterations that are similar to ovarian cancer in humans , including a high incidence of p53 mutations .

Example answer:
{"entities": [{"text": "Chemoprevention", "type": "HealthCareActivity"}, {"text": "ovarian cancer", "type": "BiologicFunction"}, {"text": "domestic hen", "type": "Eukaryote"}, {"text": "hen", "type": "Eukaryote"}, {"text": "animal model", "type": "Eukaryote"}, {"text": "in vivo testing", "type": "HealthCareActivity"}, {"text": "agents", "type": "Chemical"}, {"text": "ovarian carcinogenesis", "type": "BiologicFunction"}, {"text": "humans", "type": "Eukaryote"}, {"text": "p53", "type": "Chemical"}, {"text": "mutations", "type": "BiologicFunction"}]}

Example input:
Sentence: Moreover , passerine birds are poorly represented in MeHg neurotoxicology studies in comparison to other avian orders .

Example answer:
{"entities": [{"text": "passerine birds", "type": "Eukaryote"}, {"text": "MeHg", "type": "Chemical"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "avian", "type": "Eukaryote"}]}

Example input:
Sentence: No adverse effects of in ovo MeHg treatment were detected on courtship song quality or on mating behavior in experimental males at sexually maturity which would suggest that observable neurobehavioral effects of MeHg exposure may depend on the timing of exposure during offspring development .

Example answer:
{"entities": [{"text": "No adverse effects", "type": "Finding"}, {"text": "MeHg", "type": "Chemical"}, {"text": "detected", "type": "Finding"}, {"text": "mating behavior", "type": "BiologicFunction"}, {"text": "sexually maturity", "type": "Finding"}, {"text": "observable", "type": "ClinicalAttribute"}, {"text": "development", "type": "BiologicFunction"}]}

Example input:
Sentence: Assessment of neuroanatomical and behavioural effects of in ovo methylmercury exposure in zebra finches ( Taeniopygia guttata ) Methylmercury ( MeHg ) readily crosses the blood brain barrier and is a known neuro - toxicant .

Example answer:
{"entities": [{"text": "Assessment", "type": "ResearchActivity"}, {"text": "methylmercury", "type": "Chemical"}, {"text": "zebra finches", "type": "Eukaryote"}, {"text": "Taeniopygia guttata", "type": "Eukaryote"}, {"text": "Methylmercury", "type": "Chemical"}, {"text": "MeHg", "type": "Chemical"}, {"text": "blood brain barrier", "type": "AnatomicalStructure"}]}

Input:
Sentence: Hence in this study , we used the egg injection method to investigate the long term effects of in ovo MeHg exposure on brain histopathology and courtship behavior in a model songbird species , the zebra finch ( Taeniopygia guttata ) .

## Item MedMentions:test:3400
Example input:
Sentence: We also studied how dengue -related acute myopathy differs from other causes and also difference between myopathy due to myositis and hypokalemia in cases of dengue .

Example answer:
{"entities": [{"text": "dengue", "type": "BiologicFunction"}, {"text": "acute myopathy", "type": "BiologicFunction"}, {"text": "myopathy", "type": "BiologicFunction"}, {"text": "myositis", "type": "BiologicFunction"}, {"text": "hypokalemia", "type": "Finding"}]}

Example input:
Sentence: In silico analyses associated these proteins with key molecular events including platelet activation and inflammatory responses , and with events not previously attributed to platelets during dengue infection including antigen processing and presentation , proteasome activity , and expression of histones .

Example answer:
{"entities": [{"text": "analyses", "type": "ResearchActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "platelet activation", "type": "BiologicFunction"}, {"text": "inflammatory responses", "type": "BiologicFunction"}, {"text": "platelets", "type": "AnatomicalStructure"}, {"text": "dengue", "type": "BiologicFunction"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "antigen", "type": "Chemical"}, {"text": "proteasome activity", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "histones", "type": "Chemical"}]}

Example input:
Sentence: our study aimed to show the association of IL - 2 , -4 , and -10 with severity of dengue infection .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "IL - 2", "type": "Chemical"}, {"text": "-4", "type": "Chemical"}, {"text": "-10", "type": "Chemical"}, {"text": "dengue infection", "type": "BiologicFunction"}]}

Example input:
Sentence: Platelet proteome reveals novel pathways of platelet activation and platelet - mediated immunoregulation in dengue Dengue is the most prevalent human arbovirus disease worldwide .

Example answer:
{"entities": [{"text": "Platelet", "type": "AnatomicalStructure"}, {"text": "proteome", "type": "Chemical"}, {"text": "platelet activation", "type": "BiologicFunction"}, {"text": "platelet", "type": "AnatomicalStructure"}, {"text": "immunoregulation", "type": "BiologicFunction"}, {"text": "dengue", "type": "BiologicFunction"}, {"text": "Dengue", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "worldwide", "type": "SpatialConcept"}]}

Example input:
Sentence: Association of interleukin - 2 , -4 and -10 with dengue severity Dengue is an arboviral disease caused by four distinct serotypes of dengue virus .

Example answer:
{"entities": [{"text": "interleukin - 2", "type": "Chemical"}, {"text": "-4", "type": "Chemical"}, {"text": "-10", "type": "Chemical"}, {"text": "dengue", "type": "BiologicFunction"}, {"text": "Dengue", "type": "BiologicFunction"}, {"text": "arboviral disease", "type": "BiologicFunction"}, {"text": "serotypes", "type": "IntellectualProduct"}, {"text": "dengue virus", "type": "Virus"}]}

Example input:
Sentence: The flavivirus dengue induces hypertrophy of white matter astrocytes Flaviviruses , including Zika and dengue ( DENV ) , pose a serious global threat to human health .

Example answer:
{"entities": [{"text": "flavivirus", "type": "Virus"}, {"text": "dengue", "type": "Virus"}, {"text": "hypertrophy", "type": "BiologicFunction"}, {"text": "white matter", "type": "AnatomicalStructure"}, {"text": "astrocytes", "type": "AnatomicalStructure"}, {"text": "Flaviviruses", "type": "Virus"}, {"text": "Zika", "type": "Virus"}, {"text": "DENV", "type": "Virus"}, {"text": "human", "type": "Eukaryote"}]}

Example input:
Sentence: Etiology was dengue viral infection in 14 patients ; hypokalemia due to various causes other than dengue in 8 ; pyomyositis in 3 ; dermatomyositis , polymyositis , thyrotoxicosis , systemic lupus erythematosus , and unknown etiology in one each .

Example answer:
{"entities": [{"text": "dengue", "type": "Virus"}, {"text": "viral infection", "type": "BiologicFunction"}, {"text": "hypokalemia", "type": "Finding"}, {"text": "dengue", "type": "BiologicFunction"}, {"text": "pyomyositis", "type": "BiologicFunction"}, {"text": "dermatomyositis", "type": "BiologicFunction"}, {"text": "polymyositis", "type": "BiologicFunction"}, {"text": "thyrotoxicosis", "type": "BiologicFunction"}, {"text": "systemic lupus erythematosus", "type": "BiologicFunction"}]}

Example input:
Sentence: Dengue virus ( DENV ) infection causes syndromes varying from self - limiting febrile illness to severe dengue .

Example answer:
{"entities": [{"text": "Dengue virus ( DENV ) infection", "type": "BiologicFunction"}, {"text": "syndromes", "type": "BiologicFunction"}, {"text": "febrile illness", "type": "BiologicFunction"}, {"text": "severe dengue", "type": "BiologicFunction"}]}

Example input:
Sentence: Various pro - and anti - inflammatory cytokines are involved in the immune pathogenesis of dengue .

Example answer:
{"entities": [{"text": "pro -", "type": "Chemical"}, {"text": "anti - inflammatory cytokines", "type": "Chemical"}, {"text": "immune pathogenesis", "type": "BiologicFunction"}, {"text": "dengue", "type": "BiologicFunction"}]}

Example input:
Sentence: Although dengue pathophysiology is not completely understood , it is widely accepted that increased inflammation plays important roles in dengue pathogenesis .

Example answer:
{"entities": [{"text": "dengue", "type": "BiologicFunction"}, {"text": "understood", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "pathogenesis", "type": "BiologicFunction"}]}

Input:
Sentence: The pathogenesis of dengue is not very clearly understood .

## Item MedMentions:test:3440
Example input:
Sentence: Among the patients who developed renal failure , HCRU ( days on mechanical ventilation : 13 . 2±10 .

Example answer:
{"entities": [{"text": "renal failure", "type": "BiologicFunction"}, {"text": "mechanical ventilation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Respiratory failure secondary to progressive obstructive lung disease during infancy may be the presenting phenotype of FLNA - associated periventricular nodular heterotopia .

Example answer:
{"entities": [{"text": "Respiratory failure", "type": "BiologicFunction"}, {"text": "obstructive lung disease", "type": "BiologicFunction"}, {"text": "FLNA - associated periventricular nodular heterotopia", "type": "BiologicFunction"}]}

Example input:
Sentence: A common feature of muscular dystrophy is respiratory failure , i . e .

Example answer:
{"entities": [{"text": "muscular dystrophy", "type": "BiologicFunction"}, {"text": "respiratory failure", "type": "BiologicFunction"}]}

Example input:
Sentence: Respiratory load increases in muscular dystrophy because scoliosis makes chest wall compliance decrease , atelectasis and fibrosis make lung compliance decrease , and airway obstruction makes airway resistance increase .The consequences of respiratory pump failure are restrictive pulmonary function , hypoventilation , altered thoracoabdominal pattern , hypercapnia , dyspnoea , impaired regulation of breathing , inefficient cough and sleep disordered breathing .

Example answer:
{"entities": [{"text": "Respiratory load", "type": "Finding"}, {"text": "muscular dystrophy", "type": "BiologicFunction"}, {"text": "scoliosis", "type": "AnatomicalStructure"}, {"text": "chest wall compliance", "type": "Finding"}, {"text": "atelectasis", "type": "BiologicFunction"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "lung compliance", "type": "BiologicFunction"}, {"text": "airway obstruction", "type": "BiologicFunction"}, {"text": "airway resistance", "type": "BiologicFunction"}, {"text": "respiratory pump failure", "type": "BiologicFunction"}, {"text": "restrictive pulmonary function", "type": "Finding"}, {"text": "hypoventilation", "type": "BiologicFunction"}, {"text": "thoracoabdominal", "type": "SpatialConcept"}, {"text": "hypercapnia", "type": "Finding"}, {"text": "dyspnoea", "type": "Finding"}, {"text": "inefficient cough", "type": "Finding"}, {"text": "sleep disordered breathing", "type": "BiologicFunction"}]}

Example input:
Sentence: We describe a cohort of patients with progressive respiratory failure related to a pathogenic variant in FLNA and present lung transplantation as a viable therapeutic option for this group of patients .

Example answer:
{"entities": [{"text": "cohort", "type": "PopulationGroup"}, {"text": "respiratory failure", "type": "BiologicFunction"}, {"text": "lung transplantation", "type": "HealthCareActivity"}, {"text": "viable therapeutic option", "type": "HealthCareActivity"}]}

Example input:
Sentence: The failure rates for mask ventilation ( tidal volume ≤ anatomical dead space ) were 44 % for the C - E technique and 0 % for the V - E technique ( P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "mask ventilation", "type": "HealthCareActivity"}, {"text": "tidal volume", "type": "Finding"}, {"text": "anatomical dead space", "type": "Finding"}, {"text": "C - E technique", "type": "HealthCareActivity"}, {"text": "V - E technique", "type": "HealthCareActivity"}]}

Example input:
Sentence: Ventilatory failure in muscular dystrophy is caused by increased respiratory load and respiratory muscles weakness .

Example answer:
{"entities": [{"text": "Ventilatory failure", "type": "BiologicFunction"}, {"text": "muscular dystrophy", "type": "BiologicFunction"}, {"text": "respiratory load", "type": "Finding"}, {"text": "respiratory muscles weakness", "type": "Finding"}]}

Example input:
Sentence: 01 ) and respiratory failure ( p = 0 . 01 ) compared with LVC patients .

Example answer:
{"entities": [{"text": "respiratory failure", "type": "BiologicFunction"}, {"text": "LVC", "type": "Organization"}]}

Example input:
Sentence: She subsequently deteriorated , developing respiratory failure .

Example answer:
{"entities": [{"text": "deteriorated", "type": "Finding"}, {"text": "respiratory failure", "type": "BiologicFunction"}]}

Example input:
Sentence: the inability of the respiratory system to provide proper oxygenation and carbon dioxide elimination .In the lung , respiratory failure is caused by recurrent aspiration , and leads to hypoxaemia and hypercarbia .

Example answer:
{"entities": [{"text": "respiratory system", "type": "BodySystem"}, {"text": "carbon dioxide elimination", "type": "BiologicFunction"}, {"text": "lung", "type": "AnatomicalStructure"}, {"text": "respiratory failure", "type": "BiologicFunction"}, {"text": "aspiration", "type": "BiologicFunction"}, {"text": "hypoxaemia", "type": "Finding"}, {"text": "hypercarbia", "type": "Finding"}]}

Input:
Sentence: Respiratory failure , i . e .

## Item MedMentions:test:3448
Example input:
Sentence: 4 ± 3 . 5 ml ( D3 ) .

Example answer:
{"entities": []}

Example input:
Sentence: GRV ≥ 25 mL or higher than expected GRV adjusted by weight ( 0 . 4 mL / kg ) were also not different among the study groups ( P = .90 and P = .87 , respectively ) .

Example answer:
{"entities": [{"text": "GRV", "type": "ClinicalAttribute"}, {"text": "expected", "type": "IntellectualProduct"}]}

Example input:
Sentence: 6 . 8 [ 5 . 8 - 8 . 0 ] mL min ( - 1 ) kg ( - 1 ) , P < 0 . 001 ) and increases in respiratory quotient ( 0 . 96 [ 0 . 91 - 1 . 06 ] vs .

Example answer:
{"entities": [{"text": "respiratory quotient", "type": "ClinicalAttribute"}]}

Example input:
Sentence: 0 ± 52 . 2 mL , P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 6 ± 1 . 5 mmHg ( p < 0 . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 1 pmol / L , P < 0 . 01 ; and 717 vs 223 pg / mL , P < 0 . 01 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: In the GDFR group , ( 1 ) fluid maintenance was restricted to 3 ml / kg / h of a crystalloid solution and ( 2 ) colloid boluses were allowed only in case of hypotension associated with a low cardiac index and a high stroke volume variation .

Example answer:
{"entities": [{"text": "GDFR", "type": "HealthCareActivity"}, {"text": "fluid", "type": "BodySubstance"}, {"text": "crystalloid solution", "type": "Chemical"}, {"text": "colloid boluses", "type": "Chemical"}, {"text": "hypotension", "type": "Finding"}, {"text": "cardiac index", "type": "Finding"}, {"text": "high stroke volume", "type": "Finding"}]}

Example input:
Sentence: 3μg / mL versus 42 . 1μg / mL ; the ratio of FDP to fibrinogen , 3 . 39 versus 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 23 ± 0 . 27 ng / mL [ P = .01 ] ; group 3 : 0 . 19 ± 0 . 34 ng / mL [ P = .01 ] ) .

Example answer:
{"entities": [{"text": "group 3", "type": "IntellectualProduct"}]}

Example input:
Sentence: 0 ± 2 . 8 ml / kg / h , p < 0 . 001 )

Example answer:
{"entities": []}

Input:
Sentence: 6 ml / kg / h , p = 0 . 021 ) and less crystalloid ( 3 ± 0 vs .

## Item MedMentions:test:3344
Example input:
Sentence: In this post hoc analysis , patients with diabetes in general were older , heavier , and had a greater number of complicating comorbidities .

Example answer:
{"entities": [{"text": "hoc analysis", "type": "ResearchActivity"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "older", "type": "PopulationGroup"}]}

Example input:
Sentence: Hypertension was the most frequent comorbidity ( 40 . 0 % ) , followed by diabetes mellitus ( 17 . 8 % ) and Alzheimer 's disease ( 14 . 8 % ) .

Example answer:
{"entities": [{"text": "Hypertension", "type": "BiologicFunction"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "Alzheimer 's disease", "type": "BiologicFunction"}]}

Example input:
Sentence: In a cross - sectional survey , relationship between serum levels of 25 - hydroxy vitamin D ( 25 ( OH ) D ) and glycated haemoglobin ( HbA1C ) was examined in 141 type - 2 diabetic patients including 102 males and 39 females ; age range 22 to 70 years , visiting the Aga Khan University Hospital during July 2013 - April 2014 .

Example answer:
{"entities": [{"text": "cross - sectional survey", "type": "ResearchActivity"}, {"text": "serum", "type": "BodySubstance"}, {"text": "levels of 25 - hydroxy vitamin D", "type": "HealthCareActivity"}, {"text": "25 ( OH ) D", "type": "Chemical"}, {"text": "glycated haemoglobin", "type": "HealthCareActivity"}, {"text": "HbA1C", "type": "Chemical"}, {"text": "type - 2 diabetic", "type": "BiologicFunction"}, {"text": "males", "type": "PopulationGroup"}, {"text": "females", "type": "PopulationGroup"}, {"text": "Aga Khan University Hospital", "type": "Organization"}]}

Example input:
Sentence: More patients with diabetes had comorbidities and an increased incidence of complicating factors in both cIAI and cUTI .

Example answer:
{"entities": [{"text": "diabetes", "type": "BiologicFunction"}, {"text": "cIAI", "type": "BiologicFunction"}, {"text": "cUTI", "type": "BiologicFunction"}]}

Example input:
Sentence: The overall proportion of patients seeking RYGB with type 2 diabetes was higher than with SG ( 36 versus 25 % ) , but SG has now overtaken RYGB as the most common procedure among diabetics .

Example answer:
{"entities": [{"text": "RYGB", "type": "HealthCareActivity"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "SG", "type": "HealthCareActivity"}, {"text": "procedure", "type": "HealthCareActivity"}, {"text": "diabetics", "type": "Finding"}]}

Example input:
Sentence: Total 80 type II DM patients without any associated complications of diabetes were included in this study .

Example answer:
{"entities": [{"text": "type II DM patients without any associated complications", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Patients with diabetes had lower cure rates and a significantly higher frequency of adverse events than patients without diabetes , likely because of the higher rates of medical complications in this subgroup .

Example answer:
{"entities": [{"text": "diabetes", "type": "BiologicFunction"}, {"text": "lower", "type": "SpatialConcept"}, {"text": "adverse events", "type": "BiologicFunction"}]}

Example input:
Sentence: Significantly higher rates of adverse events observed in patients with diabetes were likely due to comorbidities because treatment -related adverse events were similar between groups .

Example answer:
{"entities": [{"text": "adverse events", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of this study was to ascertain whether vitamin D levels have any influence on glycaemic control in Pakistani patients with type - 2 DM .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "vitamin D levels", "type": "HealthCareActivity"}, {"text": "Pakistani", "type": "PopulationGroup"}, {"text": "type - 2 DM", "type": "BiologicFunction"}]}

Example input:
Sentence: The association between vitamin D deficiency and abnormal HbA1C in Pakistani diabetic patients is suggestive that patients with hypovitaminosis D could benefit from vitamin D supplementation .

Example answer:
{"entities": [{"text": "vitamin D deficiency", "type": "BiologicFunction"}, {"text": "abnormal", "type": "Finding"}, {"text": "HbA1C", "type": "Chemical"}, {"text": "Pakistani", "type": "PopulationGroup"}, {"text": "diabetic", "type": "BiologicFunction"}, {"text": "hypovitaminosis D", "type": "BiologicFunction"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "supplementation", "type": "Chemical"}]}

Input:
Sentence: However , there are no reports on this relationship in Pakistani diabetic patients .

## Item MedMentions:test:3287
Example input:
Sentence: The PHRs that were reviewed were unable to effectively manage the case study information .

Example answer:
{"entities": [{"text": "PHRs", "type": "IntellectualProduct"}, {"text": "case study", "type": "IntellectualProduct"}]}

Example input:
Sentence: Before such a strategy can be widely implemented , further prospective data are required with standardized definitions , diagnostic criteria , and management protocols , with an emphasis on shared patient - provider decision making and patient - centered outcomes .

Example answer:
{"entities": [{"text": "data", "type": "ResearchActivity"}, {"text": "definitions", "type": "IntellectualProduct"}, {"text": "diagnostic criteria", "type": "IntellectualProduct"}, {"text": "management protocols", "type": "IntellectualProduct"}, {"text": "patient - provider", "type": "ProfessionalOrOccupationalGroup"}, {"text": "decision making", "type": "BiologicFunction"}, {"text": "patient - centered outcomes", "type": "ResearchActivity"}]}

Example input:
Sentence: Criteria identified are broadly consistent with those used in wider public health practice but additionally incorporated criteria which recognizes the political siting of the boards .

Example answer:
{"entities": [{"text": "public health practice", "type": "HealthCareActivity"}]}

Example input:
Sentence: Ethical considerations : No objection to the study was made by an Ethical Review Board .

Example answer:
{"entities": [{"text": "considerations", "type": "Finding"}, {"text": "No objection", "type": "Finding"}, {"text": "Ethical Review Board", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: The Critical Appraisal Checklist for Studies Reporting Prevalence Data from the Joanna Briggs Institute was used to assess the risk of bias of the included studies .

Example answer:
{"entities": [{"text": "Critical Appraisal Checklist for Studies Reporting Prevalence Data", "type": "IntellectualProduct"}, {"text": "Joanna Briggs Institute", "type": "Organization"}]}

Example input:
Sentence: In conjunction with the pilot project , we have conducted a stakeholder analysis with the aim of informing decision makers about stakeholder perceptions of standard policy criteria like effectiveness , efficiency , and equity .

Example answer:
{"entities": [{"text": "pilot project", "type": "ResearchActivity"}, {"text": "stakeholder", "type": "ProfessionalOrOccupationalGroup"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "decision makers", "type": "PopulationGroup"}, {"text": "stakeholder", "type": "PopulationGroup"}, {"text": "perceptions", "type": "BiologicFunction"}, {"text": "policy", "type": "IntellectualProduct"}]}

Example input:
Sentence: Following three rounds of ranking and prioritizing , five priorities were agreed at Divisional level , and from these , the five top organizational priorities were selected .

Example answer:
{"entities": [{"text": "ranking", "type": "IntellectualProduct"}, {"text": "priorities", "type": "ResearchActivity"}, {"text": "Divisional level", "type": "Organization"}, {"text": "organizational priorities", "type": "ResearchActivity"}]}

Example input:
Sentence: This raises the question of how decision making functions of the boards reflects wider public health decision making , if criteria are applied to decision making , and what prioritization processes , if any , are used .

Example answer:
{"entities": [{"text": "question", "type": "IntellectualProduct"}, {"text": "public health", "type": "HealthCareActivity"}]}

Example input:
Sentence: Decision making may benefit from the explicit inclusion of criteria in the prioritization process .

Example answer:
{"entities": []}

Example input:
Sentence: Prioritization was described as an engaged and collaborative process , but criteria were not explicitly referenced in the decision making of the boards which instead made unstructured prioritization of population sub - groups or interventions agreed by consensus .

Example answer:
{"entities": [{"text": "unstructured", "type": "Finding"}, {"text": "population sub - groups", "type": "PopulationGroup"}, {"text": "interventions", "type": "HealthCareActivity"}]}

Input:
Sentence: The study explored the variety in different board 's approaches to prioritization and identified a lack of clarity and rigour in the identification and use of criteria in prioritization processes .

## Item MedMentions:test:3477
Example input:
Sentence: Mean age was 51 ± 11 years and 64 % were female .

Example answer:
{"entities": [{"text": "female", "type": "PopulationGroup"}]}

Example input:
Sentence: The median age was 58 ( range , 31 - 84 ) years ; 21 .

Example answer:
{"entities": []}

Example input:
Sentence: Of 167 participants , the median age was 25 years ( interquartile range , 21 - 29 years ) .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: RESULTS There were 173 males and 227 females ( average age : 63 .

Example answer:
{"entities": []}

Example input:
Sentence: There were 11 men and 3 women with a mean age of 35 , 6 years ( range 19 - 66 years ) .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: The mean age was 48 years ( 95 % CI 45 - 51 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The age range was 53 - 80 years with a mean of 65 .

Example answer:
{"entities": []}

Example input:
Sentence: 4 years of age ) .

Example answer:
{"entities": []}

Example input:
Sentence: Age was 18 - 72 years old , the average age 45 years , male 31 ( 51 , 7 % ) and female 29 ( 48 . 3 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: The average age was 53 years , and most were male ( 93 . 1 % ) .

Example answer:
{"entities": []}

Input:
Sentence: The average age was 4 .

## Item MedMentions:test:3364
Example input:
Sentence: Among a total of 286 eligible patients , 61 ( 21 % ) patients developed HPC .

Example answer:
{"entities": [{"text": "HPC", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: HPV 16 was the commonest strain ( N = 57 , 73 . 08 % ) followed by HPV 18 ( N = 28 , 35 . 90 % ) .

Example answer:
{"entities": [{"text": "HPV 16", "type": "Virus"}, {"text": "HPV 18", "type": "Virus"}]}

Example input:
Sentence: Twenty - four samples ( 28 . 9 % ) harbored mucosal HPVs : 3 oropharyngeal ( 6 . 9 % ) , 15 oral ( 48 . 3 % ) , 4 laryngeal ( 66 . 7 % ) , and 2 nasopharyngeal papillomas ( 66 . 7 % ) .

Example answer:
{"entities": [{"text": "mucosal", "type": "AnatomicalStructure"}, {"text": "HPVs", "type": "Virus"}, {"text": "oropharyngeal", "type": "SpatialConcept"}, {"text": "oral", "type": "SpatialConcept"}, {"text": "laryngeal", "type": "AnatomicalStructure"}, {"text": "nasopharyngeal", "type": "AnatomicalStructure"}, {"text": "papillomas", "type": "BiologicFunction"}]}

Example input:
Sentence: There was a high prevalence of HPV infection both for in situ ( 95 % ) or invasive ( 94 . 83 % ) adenocarcinomas , comprising also cancers of unusual morphology .

Example answer:
{"entities": [{"text": "HPV infection", "type": "BiologicFunction"}, {"text": "in situ", "type": "BiologicFunction"}, {"text": "invasive ( 94 . 83 % ) adenocarcinomas", "type": "BiologicFunction"}, {"text": "cancers", "type": "BiologicFunction"}]}

Example input:
Sentence: Personal and system - related barriers including low confidence in the reasons for changing current cervical screening provision need to be addressed , should HPV self - sampling be incorporated into the cervical screening programme .

Example answer:
{"entities": [{"text": "system - related barriers", "type": "Finding"}, {"text": "low confidence", "type": "Finding"}, {"text": "cervical", "type": "AnatomicalStructure"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "HPV", "type": "Virus"}, {"text": "self - sampling", "type": "HealthCareActivity"}]}

Example input:
Sentence: Insights gained from this research can be used to guide further enquiry into the possibility of HPV self - sampling and to help inform future policy and practice .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "HPV", "type": "Virus"}, {"text": "self - sampling", "type": "HealthCareActivity"}, {"text": "policy", "type": "IntellectualProduct"}, {"text": "practice", "type": "BiologicFunction"}]}

Example input:
Sentence: In anticipation of this development , we sought to inform future policy and practice by identifying potential barriers to HPV self - sampling .

Example answer:
{"entities": [{"text": "policy", "type": "IntellectualProduct"}, {"text": "practice", "type": "BiologicFunction"}, {"text": "HPV", "type": "Virus"}, {"text": "self - sampling", "type": "HealthCareActivity"}]}

Example input:
Sentence: Prevalence of HPV positivity was 43 . 9 % with an average age of 35 .

Example answer:
{"entities": [{"text": "HPV positivity", "type": "Finding"}]}

Example input:
Sentence: Women 's perspectives on human papillomavirus self - sampling in the context of the UK cervical screening programme Testing for human papillomavirus ( HPV ) is being incorporated into the cervical screening programme , with the probable future introduction of HPV as a primary test and a possibility of HPV self - sampling .

Example answer:
{"entities": [{"text": "Women 's", "type": "PopulationGroup"}, {"text": "human papillomavirus", "type": "Virus"}, {"text": "self - sampling", "type": "HealthCareActivity"}, {"text": "UK", "type": "SpatialConcept"}, {"text": "cervical", "type": "AnatomicalStructure"}, {"text": "HPV", "type": "Virus"}]}

Example input:
Sentence: Personal barriers included a lack of knowledge about HPV self - sampling , women 's low confidence in their ability to self - sample correctly and low confidence in the subsequent results .

Example answer:
{"entities": [{"text": "knowledge", "type": "IntellectualProduct"}, {"text": "HPV", "type": "Virus"}, {"text": "self - sampling", "type": "HealthCareActivity"}, {"text": "women 's", "type": "PopulationGroup"}, {"text": "low confidence", "type": "Finding"}]}

Input:
Sentence: Most survey participants ( N = 133 , 69 . 3 % ) intended to HPV self - sample .

## Item MedMentions:test:3423
Example input:
Sentence: In total , 152 patients with DFU were enrolled in the study group , and 52 age and gender matched people with diabetes but no DFU were included as the control group .

Example answer:
{"entities": [{"text": "DFU", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: On MVA , older age ( hazard ratio [ HR ] , 1 . 317 ; 95 % confidence interval [ CI ] , 1 . 137 - 1 . 526 ) , € ‰ ‰   € ‰1 comorbidity ( HR , 1 . 587 ; 95 % CI , 1 . 379 - 1 . 827 ) , distant metastasis ( HR , 1 . 385 ; 95 % CI , 1 . 216 - 1 . 578 ) , receipt of systemic therapy ( HR , 0 . 637 ; 95 % CI , 0 . 547 - 0 . 742 ) , and receipt of RT compared with no RT ( < 45 grays [ Gy ] : HR , 0 . 843 ; 95 % CI , 0 . 718 - 0 .

Example answer:
{"entities": [{"text": "older age", "type": "PopulationGroup"}, {"text": "distant metastasis", "type": "ClinicalAttribute"}, {"text": "systemic therapy", "type": "HealthCareActivity"}, {"text": "RT", "type": "IntellectualProduct"}]}

Example input:
Sentence: A total of 193 cognitively intact participants , 91 younger adults and 102 older adults , were primarily recruited through a Psychology department undergraduate subject pool and a gerontology research registry , respectively .

Example answer:
{"entities": [{"text": "intact participants", "type": "PopulationGroup"}, {"text": "Psychology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "department", "type": "Organization"}, {"text": "research registry", "type": "IntellectualProduct"}]}

Example input:
Sentence: We conducted a population - based case - control study of 5 , 950 , 391 patients using the 2014 Healthcare Cost and Utilization Project ( HCUP ) , Nationwide Inpatient Survey ( NIS ) discharge records of patients 18 years and older .

Example answer:
{"entities": [{"text": "population - based case - control study", "type": "ResearchActivity"}, {"text": "Nationwide Inpatient Survey", "type": "IntellectualProduct"}, {"text": "NIS", "type": "IntellectualProduct"}, {"text": "discharge records", "type": "IntellectualProduct"}]}

Example input:
Sentence: A cross - sectional resting - state functional connectivity magnetic resonance imaging investigation was conducted of LLD ( n = 39 ) and age - and gender -equated healthy comparison ( HC ) ( n = 29 ) participants .

Example answer:
{"entities": [{"text": "cross - sectional resting - state functional connectivity magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "investigation", "type": "HealthCareActivity"}, {"text": "LLD", "type": "PopulationGroup"}, {"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: A total of 923 adult patients with chronic heart failure and 1020 age - and gender -matched healthy controls were recruited .

Example answer:
{"entities": [{"text": "chronic heart failure", "type": "BiologicFunction"}]}

Example input:
Sentence: A cross - sectional analysis of oncologic factors and geriatric variables associated with disability that were collected using a comprehensive geriatric assessment ( CGA ) was conducted .

Example answer:
{"entities": [{"text": "cross - sectional analysis", "type": "ResearchActivity"}, {"text": "disability", "type": "Finding"}, {"text": "geriatric assessment", "type": "HealthCareActivity"}, {"text": "CGA", "type": "HealthCareActivity"}]}

Example input:
Sentence: The Physical Frailty in Elderly Cancer patients ( PF - EC ) study ( France ) is a prospective bicentric observational cohort study .

Example answer:
{"entities": [{"text": "Physical Frailty", "type": "Finding"}, {"text": "Elderly", "type": "PopulationGroup"}, {"text": "PF", "type": "Finding"}, {"text": "France", "type": "SpatialConcept"}, {"text": "prospective bicentric observational cohort study", "type": "ResearchActivity"}]}

Example input:
Sentence: Enhancing the mobility of geriatric patients through suitably tailored kinesitherapeutic methods during their hospital stay may mitigate the burden endured by FCs .

Example answer:
{"entities": [{"text": "kinesitherapeutic methods", "type": "HealthCareActivity"}]}

Example input:
Sentence: The cross - sectional study involved 100 participants who were residents of a nursing home and aged older than 65 years .

Example answer:
{"entities": [{"text": "cross - sectional study", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}]}

Input:
Sentence: A cross - sectional study of 100 FC - geriatric patient dyads was conducted .

## Item MedMentions:test:3386
Example input:
Sentence: Participants ≥18 years , initiating ART < 90 days prior to study enrollment , were examined for incidence of impaired fasting glucose ( IFG ) , diabetes mellitus ( DM ) , overweight , and obesity .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "ART", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "enrollment", "type": "HealthCareActivity"}, {"text": "examined", "type": "Finding"}, {"text": "impaired fasting glucose", "type": "Finding"}, {"text": "IFG", "type": "Finding"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "DM", "type": "BiologicFunction"}, {"text": "overweight , and obesity", "type": "BiologicFunction"}]}

Example input:
Sentence: 3 % ) achieved CR on study , with 73 . 1 % ( 38 / 52 , 95 % CI 59 . 0 - 84 .

Example answer:
{"entities": [{"text": "CR", "type": "Finding"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Eight studies met the eligibility criteria and were selected .

Example answer:
{"entities": []}

Example input:
Sentence: One hundred fourteen college freshmen completed the detailed questionnaire for estimating ANE ( aim 1 ) and answered the potential screening questions ( aim 2 ) .

Example answer:
{"entities": [{"text": "college freshmen", "type": "PopulationGroup"}, {"text": "questionnaire", "type": "IntellectualProduct"}, {"text": "ANE", "type": "Finding"}, {"text": "answered", "type": "IntellectualProduct"}, {"text": "screening questions", "type": "IntellectualProduct"}]}

Example input:
Sentence: Twenty able - bodied participants were recruited for the study .

Example answer:
{"entities": [{"text": "able - bodied", "type": "Finding"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Three hundred nine university students participated in the study ( 201 men , 108 women ; mean age : 19 . 32 years ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Twenty - seven studies met the study entry criteria .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: In the study period 11 , 528 ( 87 . 2 % ) were enrolled through the front door , 1159 ( 8 . 7 % ) resumed ART after dropping out , while 527 ( 4 % ) patients were transferred in on ART .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "enrolled", "type": "HealthCareActivity"}, {"text": "ART", "type": "HealthCareActivity"}, {"text": "out", "type": "SpatialConcept"}, {"text": "transferred", "type": "HealthCareActivity"}]}

Example input:
Sentence: 2 % of 293 eligible patients were recruited for the study ( 63 . 3 % ) ; 238 ( 81 . 2 % ) of eligible patients were enrolled .

Example answer:
{"entities": [{"text": "enrolled", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the first 48 months , 64 % of 463 patients were eligible for the study and 81 .

Example answer:
{"entities": []}

Input:
Sentence: Study uptake was 47 % ( 9 enrolled / 19 eligible ) .

## Item MedMentions:test:3078
Example input:
Sentence: Tips and Pitfalls in Direct Ligation of Large Spontaneous Splenorenal Shunt during Liver Transplantation Patients with large spontaneous splenorenal shunt ( SRS ) prove challenging during liver transplantation ( LT ) , irrespective of organizing portal vein ( PV ) thrombosis .

Example answer:
{"entities": [{"text": "Direct Ligation", "type": "HealthCareActivity"}, {"text": "Spontaneous Splenorenal Shunt", "type": "MedicalDevice"}, {"text": "Liver Transplantation", "type": "HealthCareActivity"}, {"text": "large", "type": "IntellectualProduct"}, {"text": "spontaneous splenorenal shunt", "type": "MedicalDevice"}, {"text": "SRS", "type": "MedicalDevice"}, {"text": "liver transplantation", "type": "HealthCareActivity"}, {"text": "LT", "type": "HealthCareActivity"}, {"text": "portal vein ( PV ) thrombosis", "type": "BiologicFunction"}]}

Example input:
Sentence: The rhesus monkey , however , has numerous advantages to the rodent and marmoset that make it a superior and irreplaceable animal model for studying stroke in the brain .

Example answer:
{"entities": [{"text": "rhesus monkey", "type": "Eukaryote"}, {"text": "rodent", "type": "Eukaryote"}, {"text": "marmoset", "type": "Eukaryote"}, {"text": "animal model", "type": "Eukaryote"}]}

Example input:
Sentence: In 2012 the patient underwent percutaneous transhepatic biliary drainage for bile duct stricture , complicated with acute pancreatitis .

Example answer:
{"entities": [{"text": "percutaneous transhepatic biliary drainage", "type": "HealthCareActivity"}, {"text": "bile duct stricture", "type": "BiologicFunction"}, {"text": "acute pancreatitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Following preparation of the sinus access window on a randomly selected side , SB loaded onto CaS ( CaS / SB ) was grafted in five rabbits , and CaS alone ( control ) was grafted in another five rabbits .

Example answer:
{"entities": [{"text": "sinus", "type": "SpatialConcept"}, {"text": "side", "type": "SpatialConcept"}, {"text": "SB", "type": "Chemical"}, {"text": "CaS", "type": "Chemical"}, {"text": "grafted", "type": "HealthCareActivity"}, {"text": "rabbits", "type": "Eukaryote"}]}

Example input:
Sentence: The middle cerebral artery occlusion ( MCAO ) model was established in rats and then RIPostC was carried out by three cycles of 10 minutes occlusion /10 minutes release of the bilateral femoral artery at the beginning of the reperfusion .

Example answer:
{"entities": [{"text": "middle cerebral artery occlusion", "type": "AnatomicalStructure"}, {"text": "MCAO", "type": "AnatomicalStructure"}, {"text": "rats", "type": "Eukaryote"}, {"text": "RIPostC", "type": "HealthCareActivity"}, {"text": "occlusion", "type": "AnatomicalStructure"}, {"text": "bilateral", "type": "SpatialConcept"}, {"text": "femoral artery", "type": "AnatomicalStructure"}, {"text": "reperfusion", "type": "HealthCareActivity"}]}

Example input:
Sentence: A total of 96 rabbits were randomly and equally assigned to four different groups : arthrotomy alone ; arthrotomy and collagen scaffold placement ; contracture surgery ; and contracture surgery and collagen scaffold placement .

Example answer:
{"entities": [{"text": "rabbits", "type": "Eukaryote"}, {"text": "arthrotomy", "type": "HealthCareActivity"}, {"text": "collagen", "type": "Chemical"}, {"text": "placement", "type": "HealthCareActivity"}, {"text": "contracture", "type": "AnatomicalStructure"}, {"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Evaluation of Mathisen 's technique for ureteral reimplantation in children with primary vesicoureteral reflux Although cross - trigonal ureteral reimplantation ( Cohen ) is a commonly used technique in children , it represents a non - physiological transfer of the ureteral orifices and may prove challenging with regard to endoscopic ureteral operations in later life .

Example answer:
{"entities": [{"text": "ureteral reimplantation", "type": "HealthCareActivity"}, {"text": "vesicoureteral reflux", "type": "BiologicFunction"}, {"text": "cross - trigonal ureteral reimplantation ( Cohen )", "type": "HealthCareActivity"}, {"text": "non - physiological transfer", "type": "BiologicFunction"}, {"text": "ureteral orifices", "type": "SpatialConcept"}, {"text": "endoscopic ureteral operations", "type": "HealthCareActivity"}]}

Example input:
Sentence: Direct ligation of large SRS was applied in poor portal flow during LT .

Example answer:
{"entities": [{"text": "Direct ligation", "type": "HealthCareActivity"}, {"text": "large", "type": "IntellectualProduct"}, {"text": "SRS", "type": "MedicalDevice"}, {"text": "poor portal flow", "type": "Finding"}, {"text": "LT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here we report a novel simplified surgical ALF model using cynomolgus monkeys .

Example answer:
{"entities": [{"text": "surgical", "type": "HealthCareActivity"}, {"text": "ALF", "type": "BiologicFunction"}, {"text": "model", "type": "BiologicFunction"}, {"text": "cynomolgus monkeys", "type": "Eukaryote"}]}

Example input:
Sentence: Establishment of a Novel Simplified Surgical Model of Acute Liver Failure in the Cynomolgus Monkey Models using large animals that are suitable for studying artificial liver support system ( ALSS ) are urgently needed .

Example answer:
{"entities": [{"text": "Surgical", "type": "HealthCareActivity"}, {"text": "Model", "type": "BiologicFunction"}, {"text": "Acute Liver Failure", "type": "BiologicFunction"}, {"text": "Cynomolgus Monkey", "type": "Eukaryote"}, {"text": "Models", "type": "BiologicFunction"}, {"text": "animals", "type": "Eukaryote"}, {"text": "artificial liver support system", "type": "BiologicFunction"}, {"text": "ALSS", "type": "BiologicFunction"}]}

Input:
Sentence: Six monkeys underwent portal - right renal venous shunt combined with common bile duct ligation and transection ( PRRS + CBDLT ) .
