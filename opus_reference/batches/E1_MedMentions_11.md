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

## Item MedMentions:test:2313
Example input:
Sentence: Statistically significant correlations were found only in MB between parameters HPV - p53 , p53 - pRb and p53 - p16 .

Example answer:
{"entities": [{"text": "parameters", "type": "Finding"}, {"text": "HPV", "type": "Virus"}, {"text": "p53", "type": "Chemical"}, {"text": "pRb", "type": "Chemical"}, {"text": "p16", "type": "Chemical"}]}

Example input:
Sentence: Adenosine , but not guanosine , protects vaginal epithelial cells from Trichomonas vaginalis cytotoxicity Trichomonas vaginalis causes the most common non - viral sexually transmitted disease worldwide .

Example answer:
{"entities": [{"text": "Adenosine", "type": "Chemical"}, {"text": "guanosine", "type": "Chemical"}, {"text": "Trichomonas vaginalis", "type": "Eukaryote"}, {"text": "cytotoxicity", "type": "BiologicFunction"}, {"text": "non - viral sexually transmitted disease", "type": "BiologicFunction"}]}

Example input:
Sentence: The percentage of patients who shifted from SD at baseline to normal sexual functioning at EOT was higher in males ( placebo , 40 . 6 % ; vilazodone , 35 . 7 % ) than in females ( placebo , 24 . 9 % ; vilazodone , 34 . 9 % ) ; no statistical testing was performed .

Example answer:
{"entities": [{"text": "SD", "type": "BiologicFunction"}, {"text": "sexual functioning", "type": "BiologicFunction"}, {"text": "males", "type": "PopulationGroup"}, {"text": "placebo", "type": "Chemical"}, {"text": "vilazodone", "type": "Chemical"}, {"text": "females", "type": "PopulationGroup"}]}

Example input:
Sentence: In univariate analysis , we found a relationship statistically significant between the average dose received by the vestibules and vestibular disorder videonystagmography ( P = 0 . 001 , odds ratio [ OR ] : 1 . 08 [ 1 . 025 - . 138 ] ) , but there was no relationship between vestibular disorder videonystagmography and nausea ( P = 0 . 701 ) .

Example answer:
{"entities": [{"text": "vestibules", "type": "SpatialConcept"}, {"text": "vestibular disorder", "type": "BiologicFunction"}, {"text": "videonystagmography", "type": "HealthCareActivity"}, {"text": "no", "type": "Finding"}, {"text": "nausea", "type": "Finding"}]}

Example input:
Sentence: Finally , the sensation -related barriers subscale was significantly associated with testing positive for Chlamydia and / or gonorrhea ( P = 0 . 049 ) .

Example answer:
{"entities": [{"text": "sensation", "type": "BiologicFunction"}, {"text": "barriers", "type": "HealthCareActivity"}, {"text": "subscale", "type": "IntellectualProduct"}, {"text": "positive", "type": "Finding"}, {"text": "Chlamydia", "type": "Bacterium"}, {"text": "gonorrhea", "type": "BiologicFunction"}]}

Example input:
Sentence: To estimate the frequency of human papillomavirus ( HPV ) positivity in a group of Albanian women , the prevalence of vaginal coinfections , and the relationship of coinfections with HPV , as well as their role in metaplasia or cervical intraepithelial lesions ( CIN ) .

Example answer:
{"entities": [{"text": "human papillomavirus ( HPV ) positivity", "type": "Finding"}, {"text": "Albanian", "type": "SpatialConcept"}, {"text": "women", "type": "PopulationGroup"}, {"text": "vaginal coinfections", "type": "BiologicFunction"}, {"text": "coinfections", "type": "BiologicFunction"}, {"text": "HPV", "type": "Virus"}, {"text": "metaplasia", "type": "BiologicFunction"}, {"text": "cervical intraepithelial lesions", "type": "BiologicFunction"}, {"text": "CIN", "type": "BiologicFunction"}]}

Example input:
Sentence: Candida coinfection resulted in 57 . 8 % of HPV positive women with a significant relationship between them .

Example answer:
{"entities": [{"text": "Candida coinfection", "type": "BiologicFunction"}, {"text": "HPV positive", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Gardnerella coinfection resulted in 36 ( 23 % ) , mixed flora in 34 ( 8 % ) , and Trichomonas vaginalis in 50 % of HPV positive woman .

Example answer:
{"entities": [{"text": "Gardnerella coinfection", "type": "BiologicFunction"}, {"text": "Trichomonas vaginalis", "type": "BiologicFunction"}, {"text": "HPV positive", "type": "Finding"}, {"text": "woman", "type": "PopulationGroup"}]}

Example input:
Sentence: The occurrence of gram - negative SSI ( 28 % vs 7 % ) and culture negative fluid collection ( 16 % vs 5 % ) was higher in the vancomycin cohort .

Example answer:
{"entities": [{"text": "gram - negative", "type": "BiologicFunction"}, {"text": "SSI", "type": "BiologicFunction"}, {"text": "culture negative fluid collection", "type": "Finding"}, {"text": "vancomycin", "type": "Chemical"}, {"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: vaginalis isolates were able to hydrolyze nucleotides , showing higher NTPDase than ecto - 5 ' - nucleotidase activity .

Example answer:
{"entities": [{"text": "vaginalis", "type": "Eukaryote"}, {"text": "nucleotides", "type": "Chemical"}, {"text": "NTPDase", "type": "BiologicFunction"}, {"text": "ecto - 5 ' - nucleotidase activity", "type": "BiologicFunction"}]}

Input:
Sentence: vaginalis isolates presented positive Pearson correlation .

## Item MedMentions:test:2226
Example input:
Sentence: Recurrence and reoperation rates are high and progression of aortic insufficiency following subaortic resection is common .

Example answer:
{"entities": [{"text": "Recurrence", "type": "BiologicFunction"}, {"text": "reoperation", "type": "HealthCareActivity"}, {"text": "progression of aortic insufficiency", "type": "BiologicFunction"}, {"text": "subaortic", "type": "AnatomicalStructure"}, {"text": "resection", "type": "HealthCareActivity"}]}

Example input:
Sentence: The most common diagnosis was single ventricle physiology ( 52 % ) , 9 palliated by Fontan operation and 2 by aortopulmonary shunts : d - transposition of the great arteries after Mustard / Senning ( n = 2 ) , tetralogy of Fallot ( n = 2 ) , aortic valve disease ( n = 2 ) , and other biventricular surgery ( n = 4 ) .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "single ventricle", "type": "AnatomicalStructure"}, {"text": "physiology", "type": "BiologicFunction"}, {"text": "palliated", "type": "HealthCareActivity"}, {"text": "Fontan operation", "type": "HealthCareActivity"}, {"text": "aortopulmonary shunts", "type": "HealthCareActivity"}, {"text": "d - transposition of the great arteries", "type": "AnatomicalStructure"}, {"text": "Mustard", "type": "HealthCareActivity"}, {"text": "Senning", "type": "HealthCareActivity"}, {"text": "tetralogy of Fallot", "type": "AnatomicalStructure"}, {"text": "aortic valve disease", "type": "BiologicFunction"}, {"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Transcatheter tricuspid valve - in - valve replacement : one - year results : Alternative to surgery in high - risk patients Although rheumatic heart disease is becoming uncommon in industrialized countries , its global burden is still significant .

Example answer:
{"entities": [{"text": "Transcatheter", "type": "SpatialConcept"}, {"text": "tricuspid valve - in - valve replacement", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "high - risk", "type": "Finding"}, {"text": "rheumatic heart disease", "type": "BiologicFunction"}, {"text": "global burden", "type": "IntellectualProduct"}]}

Example input:
Sentence: Medical records of all patients were also retrospectively reviewed for demographic information , cardiovascular risk factors , preoperative right heart catheterization reports , operation reports , and follow - up data .

Example answer:
{"entities": [{"text": "Medical records", "type": "IntellectualProduct"}, {"text": "retrospectively", "type": "ResearchActivity"}, {"text": "demographic information", "type": "Finding"}, {"text": "right heart catheterization reports", "type": "IntellectualProduct"}, {"text": "operation reports", "type": "IntellectualProduct"}, {"text": "follow - up data", "type": "IntellectualProduct"}]}

Example input:
Sentence: Hospitalization with diagnosis of heart failure / arrhythmia , implantable cardioverter - defibrillator implantation , and cardiac mortality were accepted as adverse cardiac events .

Example answer:
{"entities": [{"text": "Hospitalization", "type": "HealthCareActivity"}, {"text": "diagnosis", "type": "ResearchActivity"}, {"text": "heart failure", "type": "BiologicFunction"}, {"text": "arrhythmia", "type": "Finding"}, {"text": "implantable cardioverter - defibrillator", "type": "MedicalDevice"}, {"text": "implantation", "type": "HealthCareActivity"}, {"text": "adverse cardiac events", "type": "BiologicFunction"}]}

Example input:
Sentence: We report the case of a 70 - year - old male with rheumatic heart disease , who underwent 4 previous heart valve replacement surgeries , and presented to our hospital with refractory heart failure ( NYHA functional class IV ) due to severe stenosis of a previously implanted tricuspid bioprosthesis .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "rheumatic heart disease", "type": "BiologicFunction"}, {"text": "heart valve replacement surgeries", "type": "HealthCareActivity"}, {"text": "hospital", "type": "Organization"}, {"text": "refractory heart failure", "type": "BiologicFunction"}, {"text": "NYHA functional class IV", "type": "BiologicFunction"}, {"text": "severe stenosis", "type": "Finding"}, {"text": "implanted", "type": "HealthCareActivity"}, {"text": "tricuspid bioprosthesis", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients were excluded if they had single - vessel CAD , emergency , no stent , prior bypass graft or myocardial infarction < 24h .

Example answer:
{"entities": [{"text": "single - vessel CAD", "type": "BiologicFunction"}, {"text": "no", "type": "Finding"}, {"text": "stent", "type": "MedicalDevice"}, {"text": "bypass graft", "type": "HealthCareActivity"}, {"text": "myocardial infarction", "type": "BiologicFunction"}]}

Example input:
Sentence: Out of 100 patients , indications for stenting were locally advanced disease not amenable to surgery ( 52 % ) , metastatic disease ( 35 % ) , CVA ( 1 % ) , cardiac and respiratory problem ( 8 % ) , un - willing for surgery in 5 % of patients .

Example answer:
{"entities": [{"text": "stenting", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "metastatic disease", "type": "BiologicFunction"}, {"text": "CVA", "type": "BiologicFunction"}, {"text": "respiratory problem", "type": "Finding"}]}

Example input:
Sentence: A multidisciplinary approach , particularly close involvement of the advanced heart failure , mechanical heart and pancreas surgery teams was key to the success of this case .

Example answer:
{"entities": [{"text": "heart failure", "type": "BiologicFunction"}, {"text": "mechanical heart", "type": "MedicalDevice"}, {"text": "pancreas surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: The majority ( 80 % ) of patients were deemed to be medically inoperable due to underlying pulmonary dysfunction .

Example answer:
{"entities": [{"text": "pulmonary", "type": "AnatomicalStructure"}, {"text": "dysfunction", "type": "BiologicFunction"}]}

Input:
Sentence: The Heart Team deemed the patient as inoperable / high - risk for surgery .

## Item MedMentions:test:2339
Example input:
Sentence: Comprehensive clinical and psychiatric evaluations were done .

Example answer:
{"entities": [{"text": "clinical", "type": "HealthCareActivity"}, {"text": "psychiatric evaluations", "type": "HealthCareActivity"}]}

Example input:
Sentence: They were subjected to detailed clinical evaluation along with hematological , biochemical , microbiological , and electrophysiological studies and followed - up for outcome at 1 and 3 months .

Example answer:
{"entities": [{"text": "clinical evaluation", "type": "HealthCareActivity"}, {"text": "microbiological", "type": "IntellectualProduct"}, {"text": "followed - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Clinical examination included assessment of bony enlargement , crepitus , quadriceps wasting , knee effusion , joint - line and anserine tenderness , and knee range of movement ( ROM ) .

Example answer:
{"entities": [{"text": "assessment", "type": "HealthCareActivity"}, {"text": "crepitus", "type": "BiologicFunction"}, {"text": "quadriceps wasting", "type": "Finding"}, {"text": "knee effusion", "type": "Finding"}, {"text": "joint - line", "type": "SpatialConcept"}, {"text": "anserine", "type": "AnatomicalStructure"}, {"text": "tenderness", "type": "Finding"}, {"text": "knee range of movement", "type": "Finding"}, {"text": "ROM", "type": "Finding"}]}

Example input:
Sentence: Neurological examination revealed prominent gaze - evoked nystagmus , heel to shin ataxia , gait ataxia , reduced reflexes and loss of vibration sensation in the legs .

Example answer:
{"entities": [{"text": "Neurological examination", "type": "HealthCareActivity"}, {"text": "gaze - evoked nystagmus", "type": "BiologicFunction"}, {"text": "heel to shin ataxia", "type": "Finding"}, {"text": "gait ataxia", "type": "Finding"}, {"text": "reduced reflexes", "type": "Finding"}, {"text": "loss of vibration sensation", "type": "Finding"}, {"text": "legs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Evaluations before randomization and 4 weeks after intervention included motor scoring index , real - time PCR and Western blot .

Example answer:
{"entities": [{"text": "Evaluations", "type": "HealthCareActivity"}, {"text": "randomization", "type": "ResearchActivity"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "real - time PCR", "type": "ResearchActivity"}, {"text": "Western blot", "type": "HealthCareActivity"}]}

Example input:
Sentence: Evaluation of patients included a clinical examination , Barthel Index , Time Up and Go test , measurement of the ankle range of motion , and a manual muscle test .

Example answer:
{"entities": [{"text": "Barthel Index", "type": "IntellectualProduct"}, {"text": "Time Up and Go test", "type": "HealthCareActivity"}, {"text": "ankle range of motion", "type": "Finding"}, {"text": "manual muscle test", "type": "HealthCareActivity"}]}

Example input:
Sentence: At different time points after injection , we assessed locomotor function with a 24 - point neurologic deficit scoring system and the rotarod test ; assessed recognition memory with the novel object recognition test ; and assessed emotional abnormality ( anhedonia and behavioral despair ) with the tail suspension test , forced swim test , and sucrose preference test .

Example answer:
{"entities": [{"text": "injection", "type": "HealthCareActivity"}, {"text": "locomotor function", "type": "BiologicFunction"}, {"text": "24 - point neurologic deficit scoring system", "type": "IntellectualProduct"}, {"text": "rotarod test", "type": "ResearchActivity"}, {"text": "recognition", "type": "BiologicFunction"}, {"text": "memory", "type": "BiologicFunction"}, {"text": "recognition test", "type": "IntellectualProduct"}, {"text": "emotional abnormality", "type": "BiologicFunction"}, {"text": "anhedonia", "type": "BiologicFunction"}, {"text": "behavioral despair", "type": "BiologicFunction"}, {"text": "tail suspension test", "type": "HealthCareActivity"}, {"text": "forced swim test", "type": "HealthCareActivity"}, {"text": "sucrose preference test", "type": "HealthCareActivity"}]}

Example input:
Sentence: Motor and neurocognitive functions were assessed at days 1 to 7 and 23 to 28 , respectively .

Example answer:
{"entities": [{"text": "Motor", "type": "BiologicFunction"}, {"text": "neurocognitive functions", "type": "BiologicFunction"}]}

Example input:
Sentence: With advancing disease , both motor and non - motor symptoms represent a considerable burden and symptom relief and quality of life improvement become the main goal of treatment .

Example answer:
{"entities": [{"text": "disease", "type": "BiologicFunction"}, {"text": "motor", "type": "Finding"}, {"text": "non - motor symptoms", "type": "Finding"}, {"text": "symptom", "type": "Finding"}, {"text": "relief", "type": "Finding"}, {"text": "goal", "type": "IntellectualProduct"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Accurate clinical evaluation is the important first step for the proper diagnosis and treatment of patients with abnormal movements .

Example answer:
{"entities": [{"text": "clinical evaluation", "type": "HealthCareActivity"}, {"text": "diagnosis", "type": "ResearchActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "abnormal movements", "type": "BiologicFunction"}]}

Input:
Sentence: Clinical evaluation of motor symptoms was performed .

## Item MedMentions:test:1399
Example input:
Sentence: In contrast , male s . circumfila are highly elongated compared to those of females , perhaps for pheromone detection .

Example answer:
{"entities": [{"text": "s . circumfila", "type": "Eukaryote"}, {"text": "pheromone", "type": "Chemical"}, {"text": "detection", "type": "HealthCareActivity"}]}

Example input:
Sentence: The transcription factors MS188 and AMS form a complex to activate the expression of CYP703A2 for sporopollenin biosynthesis in Arabidopsis thaliana The sexine layer of pollen grain is mainly composed of sporopollenins .

Example answer:
{"entities": [{"text": "transcription factors", "type": "Chemical"}, {"text": "MS188", "type": "Chemical"}, {"text": "AMS", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "CYP703A2", "type": "Chemical"}, {"text": "sporopollenin biosynthesis", "type": "BiologicFunction"}, {"text": "Arabidopsis thaliana", "type": "Eukaryote"}, {"text": "sexine layer", "type": "AnatomicalStructure"}, {"text": "pollen grain", "type": "Eukaryote"}, {"text": "sporopollenins", "type": "Chemical"}]}

Example input:
Sentence: Can Sergentomyia ( Diptera , Psychodidae ) play a role in the transmission of mammal - infecting Leishmania ?

Example answer:
{"entities": [{"text": "Sergentomyia", "type": "Eukaryote"}, {"text": "Diptera", "type": "Eukaryote"}, {"text": "Psychodidae", "type": "Eukaryote"}, {"text": "mammal", "type": "Eukaryote"}, {"text": "infecting", "type": "BiologicFunction"}, {"text": "Leishmania", "type": "Eukaryote"}]}

Example input:
Sentence: While performing an ultrastructural analysis of viral particles present in uterine glands of gestating opossum females , we serendipitously noticed the presence of numerous structures similar to paraspeckles , nuclear bodies which in human and mouse cells are assembled around an architectural NEAT1 / MENϵ / β lncRNA .

Example answer:
{"entities": [{"text": "ultrastructural", "type": "AnatomicalStructure"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "viral particles", "type": "AnatomicalStructure"}, {"text": "uterine glands", "type": "AnatomicalStructure"}, {"text": "opossum", "type": "Eukaryote"}, {"text": "presence", "type": "Finding"}, {"text": "structures", "type": "AnatomicalStructure"}, {"text": "paraspeckles", "type": "AnatomicalStructure"}, {"text": "nuclear bodies", "type": "AnatomicalStructure"}, {"text": "human", "type": "Finding"}, {"text": "mouse cells", "type": "AnatomicalStructure"}, {"text": "NEAT1 / MENϵ / β", "type": "AnatomicalStructure"}, {"text": "lncRNA", "type": "Chemical"}]}

Example input:
Sentence: The optomotor response of the praying mantis is driven predominantly by the central visual field The optomotor response has been widely used to investigate insect sensitivity to contrast and motion .

Example answer:
{"entities": [{"text": "praying mantis", "type": "Eukaryote"}, {"text": "central", "type": "SpatialConcept"}, {"text": "visual field", "type": "SpatialConcept"}, {"text": "insect", "type": "Eukaryote"}]}

Example input:
Sentence: Synchronous vitellogenin expression and sexual maturation during migration are negatively correlated with juvenile hormone levels in Mythimna separata Annual migration of pests between different seasonal habitats can lead to serious crop damage .

Example answer:
{"entities": [{"text": "vitellogenin", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "sexual maturation", "type": "BiologicFunction"}, {"text": "migration", "type": "BiologicFunction"}, {"text": "negatively", "type": "Finding"}, {"text": "juvenile hormone", "type": "Chemical"}, {"text": "Mythimna separata", "type": "Eukaryote"}, {"text": "habitats", "type": "SpatialConcept"}, {"text": "crop", "type": "Eukaryote"}]}

Example input:
Sentence: In this work , we investigated the contribution of Aspergillus nidulans sphingolipid Δ8 - desaturase ( SdeA ) , sphingolipid C9 - methyltransferases ( SmtA / SmtB ) and glucosylceramide synthase ( GcsA ) to fungal phenotypes , sensitivity to Psd1 defensin and Galleria mellonella virulence .

Example answer:
{"entities": [{"text": "Aspergillus nidulans", "type": "Eukaryote"}, {"text": "sphingolipid Δ8 - desaturase", "type": "Chemical"}, {"text": "SdeA", "type": "Chemical"}, {"text": "sphingolipid C9 - methyltransferases", "type": "Chemical"}, {"text": "SmtA", "type": "Chemical"}, {"text": "SmtB", "type": "Chemical"}, {"text": "glucosylceramide synthase", "type": "Chemical"}, {"text": "GcsA", "type": "Chemical"}, {"text": "fungal", "type": "Eukaryote"}, {"text": "Psd1 defensin", "type": "Chemical"}, {"text": "Galleria mellonella", "type": "Eukaryote"}, {"text": "virulence", "type": "BiologicFunction"}]}

Example input:
Sentence: Scanning electron microscopy ( SEM ) was used to show cells adherence to the surface of okara .

Example answer:
{"entities": [{"text": "Scanning electron microscopy", "type": "HealthCareActivity"}, {"text": "SEM", "type": "HealthCareActivity"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "okara", "type": "Chemical"}]}

Example input:
Sentence: In this study , we showed that the monogenean parasite Heterobothrium okamotoi utilizes IgM to recognize its host , fugu Takifugu rubripes Oncomiracidia are infective larvae of H . okamotoi that shed their cilia and metamorphose into juveniles when exposed to purified d - mannose - binding fractions from fugu mucus .

Example answer:
{"entities": [{"text": "monogenean", "type": "Eukaryote"}, {"text": "parasite", "type": "Eukaryote"}, {"text": "Heterobothrium okamotoi", "type": "Eukaryote"}, {"text": "IgM", "type": "Chemical"}, {"text": "fugu Takifugu rubripes Oncomiracidia", "type": "Eukaryote"}, {"text": "infective larvae", "type": "Eukaryote"}, {"text": "H . okamotoi", "type": "Eukaryote"}, {"text": "cilia", "type": "AnatomicalStructure"}, {"text": "metamorphose", "type": "BiologicFunction"}, {"text": "d - mannose", "type": "Chemical"}, {"text": "fugu", "type": "Eukaryote"}, {"text": "mucus", "type": "BodySubstance"}]}

Example input:
Sentence: Mucosal IgM Antibody with d - Mannose Affinity in Fugu Takifugu rubripes Is Utilized by a Monogenean Parasite Heterobothrium okamotoi for Host Recognition How parasites recognize their definitive hosts is a mystery ; however , parasitism is reportedly initiated by recognition of certain molecules on host surfaces .

Example answer:
{"entities": [{"text": "Mucosal", "type": "AnatomicalStructure"}, {"text": "IgM Antibody", "type": "Chemical"}, {"text": "d - Mannose", "type": "Chemical"}, {"text": "Fugu Takifugu rubripes", "type": "Eukaryote"}, {"text": "Monogenean", "type": "Eukaryote"}, {"text": "Parasite", "type": "Eukaryote"}, {"text": "Heterobothrium okamotoi", "type": "Eukaryote"}, {"text": "Host Recognition", "type": "BiologicFunction"}, {"text": "parasites", "type": "Eukaryote"}, {"text": "recognize", "type": "BiologicFunction"}, {"text": "recognition", "type": "BiologicFunction"}, {"text": "host surfaces", "type": "AnatomicalStructure"}]}

Input:
Sentence: Morphology , Ultrastructure and Possible Functions of Antennal Sensilla of Sitodiplosis mosellana Géhin ( Diptera : Cecidomyiidae ) To better understand the olfactory receptive mechanisms involved in host selection and courtship behavior of Sitodiplosis mosellana ( Diptera : Cecidomyiidae ) , one of the most important pests of wheat , scanning and transmission electron microscopy were used to examine the external morphology and ultrastructure of the antennal sensilla .

## Item MedMentions:test:2504
Example input:
Sentence: 5 m .

Example answer:
{"entities": []}

Example input:
Sentence: 5ng / mL and 200ng / mL , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 5 ± 11 . 1 kg / m ( 2 ) )

Example answer:
{"entities": []}

Example input:
Sentence: In Kanas river valley , the estimated encounter rate over a total of 137 km transects was 0 . 15 ± 0 .

Example answer:
{"entities": [{"text": "Kanas river valley", "type": "SpatialConcept"}, {"text": "transects", "type": "ResearchActivity"}]}

Example input:
Sentence: 6 mL / kg / min V̇O2pk , 11 . 1 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 5 mN·m ( - 1 ) vs +5 .

Example answer:
{"entities": []}

Example input:
Sentence: 0 - 1 km = 1 .

Example answer:
{"entities": []}

Example input:
Sentence: The apparent Km was 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 1km·hr ( - 1 ) at a 1 % grade ) in a hot environment ( ambient temperature , 39 .

Example answer:
{"entities": []}

Example input:
Sentence: We found 5 km marked the threshold distance beyond which follow - up attendance significantly dropped .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Input:
Sentence: 5millionkm ( 2 ) .

## Item MedMentions:test:2284
Example input:
Sentence: After 30 days of prednisolone therapy , all symptoms disappeared .

Example answer:
{"entities": [{"text": "prednisolone", "type": "Chemical"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: The percentage of prescriptions requiring adrenal corticosteroid declined from 14 % to 4 % .

Example answer:
{"entities": [{"text": "prescriptions", "type": "IntellectualProduct"}, {"text": "adrenal corticosteroid", "type": "Chemical"}]}

Example input:
Sentence: 4 % versus prednisone 2 .

Example answer:
{"entities": [{"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: Thirty - day all - cause readmission occurred in 17 % and 19 % of matched patients receiving and not receiving spironolactone , respectively ( hazard ratio [ HR ] , 0 .

Example answer:
{"entities": [{"text": "readmission", "type": "HealthCareActivity"}, {"text": "spironolactone", "type": "Chemical"}]}

Example input:
Sentence: Adult emergency department patients ( aged 18 to 55 years ) were randomized to receive either a single dose of 12 mg of oral dexamethasone with 4 days of placebo or a 5 - day course of oral prednisone 60 mg a day .

Example answer:
{"entities": [{"text": "randomized", "type": "ResearchActivity"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: He was transferred to critical care and only improved after starting hydrocortisone and stopping rifampicin .

Example answer:
{"entities": [{"text": "improved", "type": "Finding"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "rifampicin", "type": "Chemical"}]}

Example input:
Sentence: One hundred seventy - three dexamethasone and 203 prednisone subjects completed the study regimen and telephone follow - up .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "telephone follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Prednisolone is associated with a worse lipid profile than hydrocortisone in patients with adrenal insufficiency Prednisolone is used as glucocorticoid replacement therapy for adrenal insufficiency ( AI ) .

Example answer:
{"entities": [{"text": "Prednisolone", "type": "Chemical"}, {"text": "worse lipid profile", "type": "Finding"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "adrenal insufficiency", "type": "BiologicFunction"}, {"text": "glucocorticoid", "type": "Chemical"}, {"text": "replacement therapy", "type": "HealthCareActivity"}, {"text": "AI", "type": "BiologicFunction"}]}

Example input:
Sentence: Significantly higher LDL levels in patients receiving prednisolone relative to hydrocortisone could predict a higher relative risk of cardiovascular disease in the former group .

Example answer:
{"entities": [{"text": "LDL levels", "type": "Finding"}, {"text": "prednisolone", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "cardiovascular disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients receiving prednisolone ( 3 - 6 mg / day , n = 50 ) or hydrocortisone ( 15 - 30 mg / day , n = 909 ) were identified and grouped at a ratio of 1 : 3 ( prednisolone : hydrocortisone ) by matching for gender , age , duration and type of disease .

Example answer:
{"entities": [{"text": "prednisolone", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "grouped", "type": "SpatialConcept"}, {"text": "type of disease", "type": "IntellectualProduct"}]}

Input:
Sentence: were identified in 47 patients on prednisolone vs 141 receiving hydrocortisone at baseline and at follow - up ( P = 0 . 005 and P = 0 .

## Item MedMentions:test:2351
Example input:
Sentence: Two cases suffered from recurred BI and instrument failure but eventually achieved solid fusion between the occiput and C2 was after revision .

Example answer:
{"entities": [{"text": "BI", "type": "AnatomicalStructure"}, {"text": "instrument", "type": "MedicalDevice"}, {"text": "failure", "type": "Finding"}, {"text": "occiput", "type": "SpatialConcept"}, {"text": "C2", "type": "AnatomicalStructure"}, {"text": "revision", "type": "HealthCareActivity"}]}

Example input:
Sentence: One hundred and thirty - one patients undergoing decompression surgery alone ( n = 85 ) or decompression plus fusion surgery ( n = 46 ) were included in this study .

Example answer:
{"entities": [{"text": "decompression surgery", "type": "HealthCareActivity"}, {"text": "decompression", "type": "HealthCareActivity"}, {"text": "fusion surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: The first 89 patients received standard radiation doses ; their data were reconstructed using AIDR 3D , whereas the last 95 patients received in average 20 % reduction in tube current ; their data were reconstructed using FIRST .

Example answer:
{"entities": [{"text": "AIDR 3D", "type": "IntellectualProduct"}, {"text": "FIRST", "type": "HealthCareActivity"}]}

Example input:
Sentence: Of these patients , 100 , 072 ( 69 . 5 % ) were under surveillance for disease progression and / or received compression therapy ; 14 , 007 ( 9 . 7 % ) received laser ablation ; 9125 ( 6 .

Example answer:
{"entities": [{"text": "surveillance", "type": "HealthCareActivity"}, {"text": "disease progression", "type": "BiologicFunction"}, {"text": "compression therapy", "type": "HealthCareActivity"}, {"text": "laser ablation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Previous studies used retrospective single - institution level data to quantify outcomes for CSM patients fusion .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "institution", "type": "Organization"}, {"text": "CSM", "type": "BiologicFunction"}, {"text": "fusion", "type": "HealthCareActivity"}]}

Example input:
Sentence: At the 36 - month follow - up examination , there was continual evidence of satisfactory reduction and fusion .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "examination", "type": "HealthCareActivity"}, {"text": "satisfactory", "type": "Finding"}, {"text": "reduction", "type": "HealthCareActivity"}, {"text": "fusion", "type": "HealthCareActivity"}]}

Example input:
Sentence: Retrospective review was performed of records of 83 patients with HCC who underwent ( 90 ) Y glass microsphere radioembolization with ( 99m ) Tc - MAA single photon emission computed tomography ( SPECT ) and ( 90 ) Y positron emission tomography ( PET ) / CT between January 2013 and December 2014 .

Example answer:
{"entities": [{"text": "Retrospective review", "type": "ResearchActivity"}, {"text": "records", "type": "IntellectualProduct"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "( 90 ) Y", "type": "Chemical"}, {"text": "glass microsphere", "type": "MedicalDevice"}, {"text": "radioembolization", "type": "HealthCareActivity"}, {"text": "( 99m ) Tc - MAA", "type": "Chemical"}, {"text": "single photon emission computed tomography", "type": "HealthCareActivity"}, {"text": "SPECT", "type": "HealthCareActivity"}, {"text": "positron emission tomography", "type": "HealthCareActivity"}, {"text": "( PET ) / CT", "type": "HealthCareActivity"}]}

Example input:
Sentence: At the end of induction ( day +50 ) , 96 % of evaluable patients ( n = 49 ) achieved a complete hematologic remission ; after consolidation , all were in complete hematologic remission .

Example answer:
{"entities": [{"text": "induction", "type": "HealthCareActivity"}, {"text": "hematologic remission", "type": "Finding"}, {"text": "consolidation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Complete necrosis on CT scan was achieved in 26 / 35 patients ( 75 % ) .

Example answer:
{"entities": [{"text": "necrosis", "type": "BiologicFunction"}, {"text": "CT scan", "type": "HealthCareActivity"}]}

Example input:
Sentence: The cancer detection rate of fusion biopsy per lesion was 45 . 6 % ( 206 / 452 ) .

Example answer:
{"entities": [{"text": "cancer", "type": "BiologicFunction"}, {"text": "fusion biopsy", "type": "HealthCareActivity"}, {"text": "lesion", "type": "Finding"}]}

Input:
Sentence: Solid fusion was achieved in 23 patients ( 92 % ) as detected radiologically .

## Item MedMentions:test:2453
Example input:
Sentence: There was no significant difference in the acute physiology and chronic health evaluation ( APACHE ) II and sequential organ failure assessment ( SOFA ) scores between the two groups at day 0 , 2 and 7 .

Example answer:
{"entities": [{"text": "acute physiology and chronic health evaluation ( APACHE ) II", "type": "HealthCareActivity"}, {"text": "sequential organ failure assessment ( SOFA ) scores", "type": "Finding"}, {"text": "day 0", "type": "Finding"}]}

Example input:
Sentence: Extensive as well as uncritical application of this method even in children inevitably causes substantial radiation exposure , a sequel to either pure ignorance or unqualified / inadequate performance of US in this particular situation , which in turn can be considered sequel to either egocentric or economic preponderance .Recent data shed new light on the role of US ( and CT ) in acute appendicitis .

Example answer:
{"entities": [{"text": "uncritical application", "type": "HealthCareActivity"}, {"text": "radiation exposure", "type": "InjuryOrPoisoning"}, {"text": "US", "type": "HealthCareActivity"}, {"text": "egocentric", "type": "Finding"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "acute appendicitis", "type": "BiologicFunction"}]}

Example input:
Sentence: A total of 100 cases ( 38 males , 62 females ; age range - 17 - 76 years ; mean age - 43 . 6 years ) of acute SAH were studied .

Example answer:
{"entities": [{"text": "SAH", "type": "BiologicFunction"}, {"text": "studied", "type": "ResearchActivity"}]}

Example input:
Sentence: We suggest improved patient and physician education on prodromal symptoms , extended femur scans using dual - energy X - ray absorptiometry ( DXA ) to monitor patients on antiresorptive treatment , better identification of high - risk patients perhaps using geometrical parameters from DXA and other risk factors , and more research on pharmacogenomics to identify risk markers .

Example answer:
{"entities": [{"text": "improved", "type": "Finding"}, {"text": "physician", "type": "ProfessionalOrOccupationalGroup"}, {"text": "education", "type": "IntellectualProduct"}, {"text": "prodromal symptoms", "type": "Finding"}, {"text": "femur", "type": "AnatomicalStructure"}, {"text": "scans", "type": "HealthCareActivity"}, {"text": "dual - energy X - ray absorptiometry", "type": "HealthCareActivity"}, {"text": "DXA", "type": "HealthCareActivity"}, {"text": "monitor patients", "type": "HealthCareActivity"}, {"text": "antiresorptive", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "risk factors", "type": "Finding"}, {"text": "pharmacogenomics", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Acute generalized exanthematous pustulosis secondary to levetiracetam and valproic acid use Acute generalized exanthematous pustulosis ( AGEP ) is a rare cutaneous eruption characterized by the appearance of diffuse , sterile pustules on an erythematous and edematous base .

Example answer:
{"entities": [{"text": "Acute generalized exanthematous pustulosis", "type": "BiologicFunction"}, {"text": "levetiracetam", "type": "Chemical"}, {"text": "valproic acid", "type": "Chemical"}, {"text": "( AGEP )", "type": "BiologicFunction"}, {"text": "cutaneous eruption", "type": "Finding"}, {"text": "diffuse", "type": "SpatialConcept"}, {"text": "sterile pustules", "type": "Finding"}, {"text": "erythematous", "type": "BiologicFunction"}, {"text": "edematous base", "type": "Finding"}]}

Example input:
Sentence: In the exploratory analysis , patients with DOR ≥12 months ( n = 287 ) or ≥24 months ( n = 133 ) were more likely to experience grade 3 / 4 AEs than the overall population .

Example answer:
{"entities": [{"text": "exploratory analysis", "type": "ResearchActivity"}, {"text": "AEs", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: Methods and Results : A total of 3 , 815 consecutive patients with severe AS were enrolled in the multicenter CURRENT AS registry between January 2003 and December 2011 .

Example answer:
{"entities": [{"text": "AS", "type": "BiologicFunction"}]}

Example input:
Sentence: Permanent AREs remain very rare .

Example answer:
{"entities": [{"text": "AREs", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: While most studies focus on the long - term morbidity and adverse radiation effects ( AREs ) , none describe the acute clinical AREs that might appear on a short - term basis .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "adverse radiation effects", "type": "InjuryOrPoisoning"}, {"text": "AREs", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: RESULTS Thirty - five ( 22 % ) of 159 patients who fulfilled the inclusion criteria had acute clinical AREs .

Example answer:
{"entities": [{"text": "AREs", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: The clinical acute AREs disappeared in 32 ( 91 .

## Item MedMentions:test:1790
Example input:
Sentence: Mycelia began to grow from one day after incubation ( DAI ) and continued to be in full growth ( control - growth , Con - G ) on PDA without fungicide , while on PDA with iprodione , no fungal growth ( iprodione - no growth , Ipr - N ) occurred for the first 3 DAI , but once the initial growth ( iprodione - initial growth , Ipr - I ) began at 4 - 5 DAI , the colonies grew and expanded continuously to be in full growth ( iprodione - growth , Ipr - G ) , suggesting Ipr - I may be a turning moment of the morphogenetic changes resisting fungicidal toxicity .

Example answer:
{"entities": [{"text": "Mycelia", "type": "Eukaryote"}, {"text": "grow", "type": "BiologicFunction"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "control - growth", "type": "BiologicFunction"}, {"text": "Con - G", "type": "BiologicFunction"}, {"text": "fungicide", "type": "Chemical"}, {"text": "iprodione", "type": "Chemical"}, {"text": "iprodione - initial growth", "type": "BiologicFunction"}, {"text": "Ipr - I", "type": "BiologicFunction"}, {"text": "colonies", "type": "AnatomicalStructure"}, {"text": "expanded", "type": "SpatialConcept"}, {"text": "iprodione - growth", "type": "BiologicFunction"}, {"text": "Ipr - G", "type": "BiologicFunction"}, {"text": "morphogenetic", "type": "BiologicFunction"}, {"text": "resisting", "type": "BiologicFunction"}, {"text": "fungicidal", "type": "BiologicFunction"}]}

Example input:
Sentence: roseus leaf idioblasts are characterized , and a methodology for the isolation of idioblast protoplasts by fluorescence - activated cell sorting is established , taking advantage of the distinctive autofluorescence of these cells .

Example answer:
{"entities": [{"text": "roseus", "type": "Eukaryote"}, {"text": "leaf", "type": "Eukaryote"}, {"text": "idioblasts", "type": "AnatomicalStructure"}, {"text": "isolation", "type": "HealthCareActivity"}, {"text": "idioblast", "type": "AnatomicalStructure"}, {"text": "protoplasts", "type": "AnatomicalStructure"}, {"text": "fluorescence - activated cell sorting", "type": "HealthCareActivity"}, {"text": "autofluorescence", "type": "HealthCareActivity"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The ygdl - 1 mutant also exhibited severe defects in chloroplast development , including disorganized grana stacks .

Example answer:
{"entities": [{"text": "ygdl - 1 mutant", "type": "BiologicFunction"}, {"text": "chloroplast", "type": "AnatomicalStructure"}, {"text": "development", "type": "BiologicFunction"}, {"text": "grana stacks", "type": "AnatomicalStructure"}]}

Example input:
Sentence: CCL2 predominated in osteoblastogenesis of the HPD - treated bony defect in the early stage of healing .

Example answer:
{"entities": [{"text": "CCL2", "type": "AnatomicalStructure"}, {"text": "osteoblastogenesis", "type": "BiologicFunction"}, {"text": "HPD", "type": "BodySubstance"}, {"text": "healing", "type": "BiologicFunction"}]}

Example input:
Sentence: Consequently , proanthocyanidins and chlorogenic acids are induced or de novo synthetised in floral limbs , tubes and stamens .

Example answer:
{"entities": [{"text": "proanthocyanidins", "type": "Chemical"}, {"text": "chlorogenic acids", "type": "Chemical"}, {"text": "floral limbs , tubes", "type": "Eukaryote"}, {"text": "stamens", "type": "Eukaryote"}]}

Example input:
Sentence: Although the plants were grown under natural light - dark cycles , this hypocotyl segment was under full coverage of the soil in 5 - 7 cm depth , thus it was never exposed to light .

Example answer:
{"entities": [{"text": "plants", "type": "Eukaryote"}, {"text": "hypocotyl segment", "type": "Eukaryote"}, {"text": "depth", "type": "SpatialConcept"}]}

Example input:
Sentence: Also the general heterogeneity of plastid forms can be concluded : in tissues not exposed to light , Pchl accumulating plastids develop and are maintained even for a long period .

Example answer:
{"entities": [{"text": "plastid forms", "type": "AnatomicalStructure"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "Pchl", "type": "Chemical"}, {"text": "plastids", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Real - time PCR analysis showed that the expression levels of genes associated with chlorophyll biosynthesis and chloroplast development were concurrently altered in the ygdl - 1 mutant .

Example answer:
{"entities": [{"text": "Real - time PCR analysis", "type": "HealthCareActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "chlorophyll", "type": "Chemical"}, {"text": "chloroplast", "type": "AnatomicalStructure"}, {"text": "development", "type": "BiologicFunction"}, {"text": "ygdl - 1 mutant", "type": "BiologicFunction"}]}

Example input:
Sentence: The maintenance but substantial transformation of plastids was found in lowermost hypocotyl segments of soil -grown bean plants ( Phaseolus vulgaris cv . Magnum ) during a 60 - day cultivation period .

Example answer:
{"entities": [{"text": "transformation", "type": "BiologicFunction"}, {"text": "plastids", "type": "AnatomicalStructure"}, {"text": "hypocotyl segments", "type": "Eukaryote"}, {"text": "bean plants", "type": "Eukaryote"}, {"text": "Phaseolus vulgaris cv . Magnum", "type": "Eukaryote"}]}

Example input:
Sentence: In this study , we identified a rice Chl -deficient mutant , ygdl - 1 ( yellow green and droopy leaf - 1 ) , which showed yellow - green leaves throughout plant development with decreased content of Chls and carotene and an increased Chl a / b ratio .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "rice", "type": "Food"}, {"text": "Chl", "type": "Chemical"}, {"text": "mutant", "type": "BiologicFunction"}, {"text": "ygdl - 1", "type": "BiologicFunction"}, {"text": "yellow green and droopy leaf - 1", "type": "BiologicFunction"}, {"text": "yellow - green leaves", "type": "Eukaryote"}, {"text": "plant development", "type": "BiologicFunction"}, {"text": "Chls", "type": "Chemical"}, {"text": "carotene", "type": "Chemical"}]}

Input:
Sentence: The 4 - day -old plants were fully etiolated : amyloplasts , occasionally prolamellar bodies , protochlorophyllide ( Pchlide ) and protochlorophyll ( Pchl ) were found in the hypocotyls of these young seedlings .

## Item MedMentions:test:2075
Example input:
Sentence: Transcranial magnetic stimulation modifies astrocytosis , cell density and lipopolysaccharide levels in experimental autoimmune encephalomyelitis Experimental autoimmune encephalomyelitis ( EAE ) is considered a valid experimental model for multiple sclerosis , a chronic neuroinflammatory condition of the central nervous system .

Example answer:
{"entities": [{"text": "Transcranial magnetic stimulation", "type": "HealthCareActivity"}, {"text": "astrocytosis", "type": "BiologicFunction"}, {"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "experimental autoimmune encephalomyelitis", "type": "BiologicFunction"}, {"text": "Experimental autoimmune encephalomyelitis", "type": "BiologicFunction"}, {"text": "EAE", "type": "BiologicFunction"}, {"text": "valid experimental model", "type": "IntellectualProduct"}, {"text": "multiple sclerosis", "type": "BiologicFunction"}, {"text": "chronic neuroinflammatory condition", "type": "BiologicFunction"}, {"text": "central nervous system", "type": "BodySystem"}]}

Example input:
Sentence: Using mouse optic nerve crush as a model for CNS traumatic injury , we performed a detailed analysis of AIS and node disruption after nerve crush .

Example answer:
{"entities": [{"text": "mouse", "type": "Eukaryote"}, {"text": "optic nerve", "type": "AnatomicalStructure"}, {"text": "crush", "type": "InjuryOrPoisoning"}, {"text": "model", "type": "BiologicFunction"}, {"text": "CNS", "type": "BodySystem"}, {"text": "traumatic injury", "type": "InjuryOrPoisoning"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "AIS", "type": "AnatomicalStructure"}, {"text": "node", "type": "SpatialConcept"}, {"text": "nerve crush", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Although axons grew rapidly , remyelination and nodal ion channel clustering was much slower .

Example answer:
{"entities": [{"text": "axons", "type": "AnatomicalStructure"}, {"text": "grew", "type": "BiologicFunction"}, {"text": "remyelination", "type": "BiologicFunction"}, {"text": "nodal ion channel clustering", "type": "BiologicFunction"}]}

Example input:
Sentence: Increased cerebral blood volume pulsatility during head - down tilt with elevated carbon dioxide : The SPACECOT Study Astronauts aboard the International Space Station ( ISS ) have exhibited hyperopic shifts , posterior eye globe flattening , dilated optic nerve sheaths , and even optic disc swelling from spaceflight .

Example answer:
{"entities": [{"text": "head - down tilt", "type": "SpatialConcept"}, {"text": "elevated carbon dioxide", "type": "Finding"}, {"text": "SPACECOT Study", "type": "ResearchActivity"}, {"text": "Astronauts", "type": "ProfessionalOrOccupationalGroup"}, {"text": "hyperopic shifts", "type": "BiologicFunction"}, {"text": "posterior", "type": "SpatialConcept"}, {"text": "eye globe", "type": "AnatomicalStructure"}, {"text": "dilated", "type": "Finding"}, {"text": "optic nerve sheaths", "type": "AnatomicalStructure"}, {"text": "optic disc swelling", "type": "BiologicFunction"}]}

Example input:
Sentence: Studies included in this review have investigated abnormal structure and function of pain processing regions in people with MOH , functional patterns that might predispose individuals to development of MOH , similarity of brain functional patterns in patients with MOH to those found in people with addiction , brain structure that could predict headache improvement following discontinuation of the overused medication , and changes in brain structure and function after discontinuation of medication overuse .

Example answer:
{"entities": [{"text": "Studies", "type": "ResearchActivity"}, {"text": "abnormal", "type": "Finding"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "pain", "type": "Finding"}, {"text": "people", "type": "PopulationGroup"}, {"text": "MOH", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "addiction", "type": "BiologicFunction"}, {"text": "brain structure", "type": "AnatomicalStructure"}, {"text": "headache", "type": "Finding"}, {"text": "discontinuation", "type": "HealthCareActivity"}, {"text": "medication", "type": "HealthCareActivity"}]}

Example input:
Sentence: 11778 G > A mutations exhibited significantly higher penetrance of optic neuropathy than those carrying only m .

Example answer:
{"entities": [{"text": "11778 G > A mutations", "type": "BiologicFunction"}, {"text": "optic neuropathy", "type": "BiologicFunction"}, {"text": "m .", "type": "BiologicFunction"}]}

Example input:
Sentence: The Optical Coherence Tomographic Profile of Leber Hereditary Optic Neuropathy The objective of this study was to describe the changes in the retinal ganglion cell complex ( GCC ) relative to the retinal nerve fibre layer ( RNFL ) over time in Leber hereditary optic neuropathy ( LHON ) patients .

Example answer:
{"entities": [{"text": "Optical Coherence Tomographic", "type": "HealthCareActivity"}, {"text": "Leber Hereditary Optic Neuropathy", "type": "BiologicFunction"}, {"text": "retinal", "type": "AnatomicalStructure"}, {"text": "ganglion cell complex", "type": "AnatomicalStructure"}, {"text": "GCC", "type": "AnatomicalStructure"}, {"text": "retinal nerve fibre layer", "type": "AnatomicalStructure"}, {"text": "RNFL", "type": "AnatomicalStructure"}, {"text": "Leber hereditary optic neuropathy", "type": "BiologicFunction"}, {"text": "LHON", "type": "BiologicFunction"}]}

Example input:
Sentence: Gaze - induced LC strains in the PPA group were on average larger than those in the non - PPA group ; however , the relationship was not statistically significant .

Example answer:
{"entities": [{"text": "Gaze", "type": "MedicalDevice"}, {"text": "LC", "type": "AnatomicalStructure"}, {"text": "strains", "type": "AnatomicalStructure"}, {"text": "PPA", "type": "Finding"}]}

Example input:
Sentence: Mobile zinc increases rapidly in the retina after optic nerve injury and regulates ganglion cell survival and optic nerve regeneration Retinal ganglion cells ( RGCs ) , the projection neurons of the eye , cannot regenerate their axons once the optic nerve has been injured and soon begin to die .

Example answer:
{"entities": [{"text": "zinc", "type": "Chemical"}, {"text": "retina", "type": "AnatomicalStructure"}, {"text": "optic nerve injury", "type": "InjuryOrPoisoning"}, {"text": "ganglion cell", "type": "AnatomicalStructure"}, {"text": "survival", "type": "BiologicFunction"}, {"text": "Retinal ganglion cells", "type": "AnatomicalStructure"}, {"text": "RGCs", "type": "AnatomicalStructure"}, {"text": "projection neurons", "type": "AnatomicalStructure"}, {"text": "eye", "type": "AnatomicalStructure"}, {"text": "axons", "type": "AnatomicalStructure"}, {"text": "optic nerve", "type": "AnatomicalStructure"}, {"text": "injured", "type": "InjuryOrPoisoning"}, {"text": "die", "type": "BiologicFunction"}]}

Example input:
Sentence: Within an hour after the optic nerve is injured , Zn ( 2 + ) increases several - fold in retinal amacrine cell processes and continues to rise over the first day , then transfers slowly to RGCs via vesicular release .

Example answer:
{"entities": [{"text": "optic nerve", "type": "AnatomicalStructure"}, {"text": "injured", "type": "InjuryOrPoisoning"}, {"text": "Zn ( 2 + )", "type": "Chemical"}, {"text": "retinal", "type": "AnatomicalStructure"}, {"text": "amacrine cell", "type": "AnatomicalStructure"}, {"text": "RGCs", "type": "AnatomicalStructure"}]}

Input:
Sentence: Further studies are needed to explore a possible link between ONH strains induced by eye movements and axonal loss in optic neuropathies .

## Item MedMentions:test:2252
Example input:
Sentence: In addition , the placebo exhibited a greater TIF , glomerulosclerosis , and urinary HSP72 compared with the eplerenone group .

Example answer:
{"entities": [{"text": "placebo", "type": "HealthCareActivity"}, {"text": "TIF", "type": "HealthCareActivity"}, {"text": "glomerulosclerosis", "type": "BiologicFunction"}, {"text": "urinary", "type": "BodySubstance"}, {"text": "HSP72", "type": "Chemical"}]}

Example input:
Sentence: Compared to CTRL , power output during FENT was 10 ± 4 % higher in the first half of the time trial , but 11 ± 5 % lower in the second half ( both P < 0 . 01 ) .

Example answer:
{"entities": [{"text": "CTRL", "type": "Finding"}, {"text": "FENT", "type": "BiologicFunction"}, {"text": "trial", "type": "ResearchActivity"}]}

Example input:
Sentence: Training improved both absolute ( IHRT : 13 . 1 ± 3 .

Example answer:
{"entities": [{"text": "Training", "type": "HealthCareActivity"}, {"text": "improved", "type": "Finding"}, {"text": "IHRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Heavy Resistance Training in Hypoxia Enhances 1RM Squat Performance Purpose : To determine if heavy resistance training in hypoxia ( IHRT ) is more effective at improving strength , power , and increasing lean mass than the same training in normoxia .

Example answer:
{"entities": [{"text": "Heavy Resistance Training", "type": "HealthCareActivity"}, {"text": "Hypoxia", "type": "BiologicFunction"}, {"text": "Squat", "type": "Finding"}, {"text": "heavy resistance training", "type": "HealthCareActivity"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "IHRT", "type": "HealthCareActivity"}, {"text": "power", "type": "Finding"}, {"text": "lean mass", "type": "ClinicalAttribute"}]}

Example input:
Sentence: A greater proportion of patients who received vernakalant ( 52 . 7 % ) than placebo ( 12 . 5 % ) met the primary end point ( P < 0 . 001 ) , and cardioversion was faster in the vernakalant group than in the placebo group ( P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "vernakalant", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}, {"text": "cardioversion", "type": "HealthCareActivity"}]}

Example input:
Sentence: Conclusion : Heavy resistance training in hypoxia is more effective than placebo for improving absolute and relative strength .

Example answer:
{"entities": [{"text": "Heavy resistance training", "type": "HealthCareActivity"}, {"text": "hypoxia", "type": "BiologicFunction"}]}

Example input:
Sentence: Methods : A pair - matched , placebo - controlled study design included 20 resistance - trained participants assigned to IHRT ( FIO2 0 . 143 ) or placebo ( FIO2 0 . 20 ) , ( n = 10 per group ) .

Example answer:
{"entities": [{"text": "resistance - trained", "type": "HealthCareActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "IHRT", "type": "HealthCareActivity"}, {"text": "FIO2", "type": "HealthCareActivity"}]}

Example input:
Sentence: Both groups performed 20 sessions over 7 weeks either with IHRT or placebo .

Example answer:
{"entities": [{"text": "IHRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: There was also a greater change for IHRT at post for both absolute ( 7 . 0 % greater change , 90 % CI 1 .

Example answer:
{"entities": [{"text": "IHRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Importantly , the change in IHRT was greater than placebo at mid for both absolute [ 4 . 4 % greater change , 90 % Confidence Interval ( CI ) 1 . 0 : 8 . 0 % , ES 0 . 21 , and relative strength ( 5 .

Example answer:
{"entities": [{"text": "IHRT", "type": "HealthCareActivity"}]}

Input:
Sentence: Only IHRT increased countermovement jump peak power at Post ( 4 . 9 % , ES 0 . 35 ) , however the difference between IHRT and placebo was unclear ( 2 . 7 , 90 % CI -2 .

## Item MedMentions:test:2006
Example input:
Sentence: plantarum C88 showed the strongest AFB1 binding capacity in vitro , and was orally administered to mice with liver oxidative damage induced by AFB1 .

Example answer:
{"entities": [{"text": "plantarum C88", "type": "Bacterium"}, {"text": "AFB1", "type": "Chemical"}, {"text": "orally administered", "type": "HealthCareActivity"}, {"text": "mice", "type": "Eukaryote"}, {"text": "liver oxidative damage", "type": "BiologicFunction"}]}

Example input:
Sentence: aeruginosa ( PAO01 strain ) for 1 week and inserted into the trachea of CCSP - deficient mice .

Example answer:
{"entities": [{"text": "aeruginosa", "type": "Bacterium"}, {"text": "trachea", "type": "AnatomicalStructure"}, {"text": "CCSP", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Here we generated a murine monoclonal antibody ( 3c10 - 3 ) directed against the  of A ( H7N9 ) and show that prophylactic systemic administration of 3c10 - 3 fully protected mice from lethal challenge with wild - type A / Anhui / 1 / 2013 ( H7N9 ) .

Example answer:
{"entities": [{"text": "murine", "type": "Eukaryote"}, {"text": "monoclonal antibody", "type": "Chemical"}, {"text": "3c10 - 3", "type": "Chemical"}, {"text": "A ( H7N9 )", "type": "Virus"}, {"text": "wild - type", "type": "AnatomicalStructure"}, {"text": "A / Anhui / 1 / 2013", "type": "Virus"}, {"text": "H7N9", "type": "Virus"}]}

Example input:
Sentence: F901318 , the leading representative of a novel class of drug , the orotomides , is an antifungal drug in clinical development that demonstrates excellent potency against a broad range of dimorphic and filamentous fungi .

Example answer:
{"entities": [{"text": "F901318", "type": "Chemical"}, {"text": "class", "type": "IntellectualProduct"}, {"text": "drug", "type": "Chemical"}, {"text": "orotomides", "type": "Chemical"}, {"text": "antifungal drug", "type": "Chemical"}, {"text": "clinical development", "type": "ResearchActivity"}, {"text": "dimorphic", "type": "Eukaryote"}, {"text": "filamentous fungi", "type": "Eukaryote"}]}

Example input:
Sentence: dolosa strain , AU0158 , and responses compared to the well - studied CF pathogen , Pseudomonas aeruginosa In parallel , mice were also infected with a polar flagellin mutant of B .

Example answer:
{"entities": [{"text": "dolosa strain", "type": "Bacterium"}, {"text": "AU0158", "type": "Bacterium"}, {"text": "CF", "type": "BiologicFunction"}, {"text": "Pseudomonas aeruginosa", "type": "Bacterium"}, {"text": "mice", "type": "Eukaryote"}, {"text": "infected", "type": "Finding"}, {"text": "flagellin", "type": "AnatomicalStructure"}, {"text": "mutant", "type": "BiologicFunction"}, {"text": "B .", "type": "Bacterium"}]}

Example input:
Sentence: Finally , a mouse model of bleomycin ( BLM ) ‑induced pulmonary fibrosis was used to confirm the effect of miR‑221 on EMT .

Example answer:
{"entities": [{"text": "mouse model", "type": "BiologicFunction"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "BLM", "type": "Chemical"}, {"text": "pulmonary fibrosis", "type": "BiologicFunction"}, {"text": "miR‑221", "type": "Chemical"}, {"text": "EMT", "type": "BiologicFunction"}]}

Example input:
Sentence: An investigation into the mechanism of action of F901318 found that it acts via inhibition of the pyrimidine biosynthesis enzyme dihydroorotate dehydrogenase ( DHODH ) in a fungal - specific manner .

Example answer:
{"entities": [{"text": "investigation", "type": "HealthCareActivity"}, {"text": "F901318", "type": "Chemical"}, {"text": "pyrimidine", "type": "Chemical"}, {"text": "enzyme dihydroorotate dehydrogenase", "type": "Chemical"}, {"text": "DHODH", "type": "Chemical"}, {"text": "fungal", "type": "Eukaryote"}]}

Example input:
Sentence: F901318 represents a novel class of antifungal drug that inhibits dihydroorotate dehydrogenase There is an important medical need for new antifungal agents with novel mechanisms of action to treat the increasing number of patients with life - threatening systemic fungal disease and to overcome the growing problem of resistance to current therapies .

Example answer:
{"entities": [{"text": "F901318", "type": "Chemical"}, {"text": "class", "type": "IntellectualProduct"}, {"text": "antifungal drug", "type": "Chemical"}, {"text": "dihydroorotate dehydrogenase", "type": "Chemical"}, {"text": "antifungal agents", "type": "Chemical"}, {"text": "treat", "type": "HealthCareActivity"}, {"text": "number of patients", "type": "Finding"}, {"text": "life - threatening", "type": "Finding"}, {"text": "systemic fungal disease", "type": "BiologicFunction"}, {"text": "problem", "type": "Finding"}, {"text": "resistance", "type": "BiologicFunction"}, {"text": "current therapies", "type": "HealthCareActivity"}]}

Example input:
Sentence: F901318 is currently in late Phase 1 clinical trials , offering hope that the antifungal armamentarium can be expanded to include a class of agent with a mechanism of action distinct from currently marketed antifungals .

Example answer:
{"entities": [{"text": "F901318", "type": "Chemical"}, {"text": "clinical trials", "type": "ResearchActivity"}, {"text": "antifungal", "type": "Chemical"}, {"text": "expanded", "type": "SpatialConcept"}, {"text": "class", "type": "IntellectualProduct"}, {"text": "agent", "type": "Chemical"}, {"text": "antifungals", "type": "Chemical"}]}

Example input:
Sentence: In vitro susceptibility testing of F901318 against more than 100 strains from the four main pathogenic Aspergillus spp .

Example answer:
{"entities": [{"text": "susceptibility testing", "type": "HealthCareActivity"}, {"text": "F901318", "type": "Chemical"}, {"text": "Aspergillus spp", "type": "Eukaryote"}]}

Input:
Sentence: In a murine pulmonary model of aspergillosis , F901318 displays in vivo efficacy against a strain of A .

## Item MedMentions:test:2275
Example input:
Sentence: Furthermore , improved spatial performance was observed in simvastatin - treated animals .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "animals", "type": "Eukaryote"}]}

Example input:
Sentence: The results suggest that treatment with high dose of atorvastatin , independent of glycemia , improves endothelial function in aortas from diabetic rats by reducing the constrictor prostanoids derived from COX - 2 and by reducing the oxidative stress by NADPH oxidase , as well as a possible increasing of nitric oxide participation .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "atorvastatin", "type": "Chemical"}, {"text": "glycemia", "type": "Chemical"}, {"text": "endothelial", "type": "AnatomicalStructure"}, {"text": "aortas", "type": "AnatomicalStructure"}, {"text": "diabetic", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}, {"text": "constrictor prostanoids", "type": "Chemical"}, {"text": "COX - 2", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "NADPH oxidase", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}]}

Example input:
Sentence: Statin treatment had no effect on any of these measures .

Example answer:
{"entities": []}

Example input:
Sentence: MS and AK lowered low - density lipoprotein cholesterol ( LDL - C ) and preserved high - density lipoprotein cholesterol contents .

Example answer:
{"entities": [{"text": "MS", "type": "Chemical"}, {"text": "AK", "type": "Chemical"}, {"text": "low - density lipoprotein cholesterol", "type": "Chemical"}, {"text": "LDL - C", "type": "Chemical"}, {"text": "high - density lipoprotein cholesterol", "type": "Chemical"}]}

Example input:
Sentence: HDACIs treatment also increased the protein and mRNA expression of STAT3 , but not PXR , CAR , Foxo3a or β - catenin , which are known to be involved in ABCB transcription regulation .

Example answer:
{"entities": [{"text": "HDACIs", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "protein", "type": "Chemical"}, {"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "STAT3", "type": "Chemical"}, {"text": "PXR", "type": "Chemical"}, {"text": "CAR", "type": "Chemical"}, {"text": "Foxo3a", "type": "Chemical"}, {"text": "β - catenin", "type": "Chemical"}, {"text": "ABCB transcription regulation", "type": "BiologicFunction"}]}

Example input:
Sentence: Drug - related side effects including an increased propensity for development of type 2 diabetes occur during statin treatment , whilst further evaluation of more potent LDL - lowering treatments such as PCSK9 inhibitors is needed .

Example answer:
{"entities": [{"text": "Drug - related side effects", "type": "BiologicFunction"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "evaluation", "type": "HealthCareActivity"}, {"text": "LDL", "type": "Chemical"}, {"text": "PCSK9 inhibitors", "type": "BiologicFunction"}]}

Example input:
Sentence: Atorvastatin could significantly decrease HG - induced NOXs , ROS and MDA elevation and improve impaired cell viability .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "Chemical"}, {"text": "HG", "type": "Finding"}, {"text": "NOXs", "type": "Chemical"}, {"text": "ROS", "type": "Chemical"}, {"text": "MDA", "type": "Chemical"}, {"text": "elevation", "type": "SpatialConcept"}, {"text": "improve", "type": "Finding"}, {"text": "cell viability", "type": "BiologicFunction"}]}

Example input:
Sentence: Our meta - analysis demonstrates that genistein significantly reduces homocysteine levels and increases HDL cholesterol levels in postmenopausal women .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}, {"text": "genistein", "type": "Chemical"}, {"text": "homocysteine levels", "type": "HealthCareActivity"}, {"text": "HDL cholesterol levels", "type": "HealthCareActivity"}, {"text": "postmenopausal", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: In a case - control study , HDL was isolated from 12 FH patients with and without statin treatment and from 12 healthy controls .

Example answer:
{"entities": [{"text": "case - control study", "type": "ResearchActivity"}, {"text": "HDL", "type": "Chemical"}, {"text": "FH", "type": "BiologicFunction"}]}

Example input:
Sentence: We examined its potential effects on high - density lipoprotein ( HDL ) - associated sphingosine - 1 - phosphate ( S1P ) content ( HDL - S1P ) and HDL -mediated protection against oxidative stress , both with and without statin treatment .

Example answer:
{"entities": [{"text": "high - density lipoprotein", "type": "Chemical"}, {"text": "HDL", "type": "Chemical"}, {"text": "sphingosine - 1 - phosphate", "type": "Chemical"}, {"text": "S1P", "type": "Chemical"}, {"text": "protection against oxidative stress", "type": "BiologicFunction"}]}

Input:
Sentence: Statin treatment does not modulate HDL function in this regard .

## Item MedMentions:test:2273
Example input:
Sentence: This study investigated whether SPostC could regulate the expression of myocardial HIF - 1α and to improve mitochondrial respiratory function , thereby relieving myocardial ischemia - reperfusion injury in rats .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "SPostC", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "myocardial", "type": "AnatomicalStructure"}, {"text": "HIF - 1α", "type": "Chemical"}, {"text": "improve", "type": "Finding"}, {"text": "mitochondrial", "type": "AnatomicalStructure"}, {"text": "respiratory function", "type": "BiologicFunction"}, {"text": "myocardial ischemia", "type": "BiologicFunction"}, {"text": "reperfusion injury", "type": "InjuryOrPoisoning"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: MS and AK also significantly increase apo A1 expression , which facilitates high - density lipoprotein cholesterol formation .

Example answer:
{"entities": [{"text": "MS", "type": "Chemical"}, {"text": "AK", "type": "Chemical"}, {"text": "apo A1", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "high - density lipoprotein cholesterol", "type": "Chemical"}]}

Example input:
Sentence: 05 ) of apoptosis and increased expression ( P < 0 . 05 ) of apoptosis protease - activating factor - 1 ( Apaf - 1 ) in HL - 1 cardiomyocytes .

Example answer:
{"entities": [{"text": "apoptosis", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "apoptosis protease - activating factor - 1", "type": "Chemical"}, {"text": "Apaf - 1", "type": "Chemical"}, {"text": "HL - 1 cardiomyocytes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We reported previously that recombinant protein transduction domain ( PTD ) - Cu / Zn SOD effectively scavenged excessive ROS and prevented cardiomyocytes from hypoxia - reoxygenation damage .

Example answer:
{"entities": [{"text": "reported", "type": "IntellectualProduct"}, {"text": "recombinant", "type": "Chemical"}, {"text": "protein transduction domain", "type": "SpatialConcept"}, {"text": "PTD", "type": "SpatialConcept"}, {"text": "Cu / Zn SOD", "type": "Chemical"}, {"text": "scavenged", "type": "BiologicFunction"}, {"text": "ROS", "type": "Chemical"}, {"text": "cardiomyocytes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A significant increment of malondialdehyde and reduction in heart total thiol , superoxide dismutase and catalase concentrations were observed in LPS group ( p < 0 .

Example answer:
{"entities": [{"text": "malondialdehyde", "type": "Chemical"}, {"text": "heart", "type": "AnatomicalStructure"}, {"text": "thiol", "type": "Chemical"}, {"text": "superoxide dismutase", "type": "Chemical"}, {"text": "catalase", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}]}

Example input:
Sentence: SSM , which are particularly sensitive to reperfusion damage , take advantage of their location in cardiomyocyte boundary and benefit from the cardioprotective signaling driven by caveolae , avoiding injury propagation .

Example answer:
{"entities": [{"text": "SSM", "type": "AnatomicalStructure"}, {"text": "reperfusion damage", "type": "InjuryOrPoisoning"}, {"text": "location", "type": "SpatialConcept"}, {"text": "cardiomyocyte", "type": "AnatomicalStructure"}, {"text": "cardioprotective signaling", "type": "BiologicFunction"}, {"text": "caveolae", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Notably , we found that 1 , 25 ( OH ) 2D3 prevents the reduction of S1P1 expression promoted by Aβ ( 1 - 42 ) and thereby it modulates the downstream signaling leading to ER stress damage ( p38MAPK / ATF4 ) .

Example answer:
{"entities": [{"text": "1 , 25 ( OH ) 2D3", "type": "Chemical"}, {"text": "S1P1", "type": "Chemical"}, {"text": "Aβ ( 1 - 42 )", "type": "Chemical"}, {"text": "downstream signaling", "type": "BiologicFunction"}, {"text": "ER stress damage", "type": "BiologicFunction"}, {"text": "p38MAPK", "type": "Chemical"}, {"text": "ATF4", "type": "Chemical"}]}

Example input:
Sentence: Neither the HDL - S1P content nor HDL protective capacity differed between nontreated FH patients and controls .

Example answer:
{"entities": [{"text": "HDL", "type": "Chemical"}, {"text": "S1P", "type": "Chemical"}, {"text": "FH", "type": "BiologicFunction"}]}

Example input:
Sentence: HDL -associated S1P was significantly correlated with cell protection , but not with HDL - cholesterol or apolipoprotein AI .

Example answer:
{"entities": [{"text": "HDL", "type": "Chemical"}, {"text": "S1P", "type": "Chemical"}, {"text": "cell protection", "type": "BiologicFunction"}, {"text": "HDL - cholesterol", "type": "Chemical"}, {"text": "apolipoprotein AI", "type": "Chemical"}]}

Example input:
Sentence: We examined its potential effects on high - density lipoprotein ( HDL ) - associated sphingosine - 1 - phosphate ( S1P ) content ( HDL - S1P ) and HDL -mediated protection against oxidative stress , both with and without statin treatment .

Example answer:
{"entities": [{"text": "high - density lipoprotein", "type": "Chemical"}, {"text": "HDL", "type": "Chemical"}, {"text": "sphingosine - 1 - phosphate", "type": "Chemical"}, {"text": "S1P", "type": "Chemical"}, {"text": "protection against oxidative stress", "type": "BiologicFunction"}]}

Input:
Sentence: The HDL - S1P content and the capacity of HDL to protect cardiomyocytes against oxidative stress in vitro were measured .

## Item MedMentions:test:2495
Example input:
Sentence: Here , TuLIP ( Two - Level Iterative clustering Process ) is introduced as an iterative , divisive clustering process that utilizes active site profiling to separate structurally characterized superfamily members into functionally relevant clusters .

Example answer:
{"entities": [{"text": "TuLIP", "type": "IntellectualProduct"}, {"text": "Two - Level Iterative clustering Process", "type": "IntellectualProduct"}, {"text": "active site profiling", "type": "ResearchActivity"}]}

Example input:
Sentence: Analyses were stratified by center volume ( low - volume centers [ LVCs ] or high - volume centers [ HVCs ] ) , and transfer status .

Example answer:
{"entities": [{"text": "low - volume centers", "type": "Organization"}, {"text": "LVCs", "type": "Organization"}, {"text": "high - volume centers", "type": "Organization"}, {"text": "HVCs", "type": "Organization"}, {"text": "transfer status", "type": "Finding"}]}

Example input:
Sentence: 8 . 1 . Between - country dispersion rates were tested with Bayesian stochastic search variable selection method and were considered significant where Bayes factor values were greater than three .

Example answer:
{"entities": [{"text": "8 . 1", "type": "IntellectualProduct"}, {"text": "Bayesian stochastic search variable selection method", "type": "IntellectualProduct"}]}

Example input:
Sentence: Methods Analysis was conducted on 4 , 727 participants of Thailand 's 2013 National Mental Health Survey , a multistage stratified cluster survey , using the Composite International Diagnostic Interview .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "Thailand 's", "type": "SpatialConcept"}, {"text": "multistage stratified cluster survey", "type": "IntellectualProduct"}, {"text": "Composite International Diagnostic Interview", "type": "IntellectualProduct"}]}

Example input:
Sentence: Hierarchical clustering revealed three response patterns : ( i ) TIL ( high ) tumors showed increases in multiple immune markers after chemotherapy ; ( ii ) TIL ( low ) tumors underwent similar increases , achieving patterns indistinguishable from the first group ; and ( iii ) TIL ( negative ) cases generally remained negative .

Example answer:
{"entities": [{"text": "Hierarchical clustering", "type": "ResearchActivity"}, {"text": "TIL", "type": "AnatomicalStructure"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "negative", "type": "Finding"}]}

Example input:
Sentence: Subgroup analyses showed that retrospective and low quality studies were statistically significant sources of heterogeneity .

Example answer:
{"entities": [{"text": "Subgroup", "type": "IntellectualProduct"}, {"text": "analyses", "type": "ResearchActivity"}, {"text": "retrospective", "type": "ResearchActivity"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: The blue channel of the first stage output is given as input to k - means algorithm , which provides separate cluster for Ki - 67 positive and negative cells .

Example answer:
{"entities": [{"text": "first stage", "type": "IntellectualProduct"}, {"text": "k - means algorithm", "type": "ResearchActivity"}, {"text": "Ki - 67", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Sampling was performed in two stages : simple random sampling for selecting Hospital Units HU and Health Centers HC throughout the hospital network in the city , followed by random quota sampling in proportion to the number of elderly population assigned to each HU and HC .

Example answer:
{"entities": [{"text": "simple random sampling", "type": "ResearchActivity"}, {"text": "Hospital Units", "type": "Organization"}, {"text": "HU", "type": "Organization"}, {"text": "Health Centers", "type": "Organization"}, {"text": "HC", "type": "Organization"}, {"text": "hospital", "type": "Organization"}, {"text": "city", "type": "SpatialConcept"}, {"text": "random quota sampling", "type": "ResearchActivity"}, {"text": "elderly population", "type": "PopulationGroup"}]}

Example input:
Sentence: We used a cross - sectional study design with stratified random sampling .

Example answer:
{"entities": [{"text": "cross - sectional study design", "type": "ResearchActivity"}, {"text": "stratified random sampling", "type": "ResearchActivity"}]}

Example input:
Sentence: Methods : A multi - stage stratified random cluster sampling method was adopted to identify 29 township hospitals from six counties in three provinces .

Example answer:
{"entities": [{"text": "stratified random cluster sampling method", "type": "ResearchActivity"}, {"text": "hospitals", "type": "Organization"}, {"text": "counties", "type": "SpatialConcept"}, {"text": "provinces", "type": "SpatialConcept"}]}

Input:
Sentence: Two - stage stratified cluster sampling was employed .

## Item MedMentions:test:2513
Example input:
Sentence: The increase in TP / ET was due to an increase in IVCT / ET .

Example answer:
{"entities": [{"text": "ET", "type": "ClinicalAttribute"}]}

Example input:
Sentence: A higher median frequency of CD8 ( + ) T - cell responses was detected in women with lower genital tract chlamydial infection , compared with those with upper genital tract chlamydial infection ( 13 . 8 % vs 9 . 5 % ; P = 04 ) , but the CD4 ( + ) T - cell response frequencies were not different .

Example answer:
{"entities": [{"text": "CD8 ( + ) T - cell", "type": "AnatomicalStructure"}, {"text": "responses", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "lower", "type": "SpatialConcept"}, {"text": "genital tract", "type": "BodySystem"}, {"text": "chlamydial infection", "type": "BiologicFunction"}, {"text": "upper", "type": "SpatialConcept"}, {"text": "CD4 ( + ) T - cell", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In CD and UC patients , V was 49 % and 52 % higher than in AS , respectively , and CL was 47 % and 60 % higher than in AS , respectively .

Example answer:
{"entities": [{"text": "CD", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}, {"text": "AS", "type": "BiologicFunction"}]}

Example input:
Sentence: Increased left ventricular fibrosis mass was associated with increased prevalence of ventricular tachyarrhythmias ( p < 0 .

Example answer:
{"entities": [{"text": "left ventricular", "type": "AnatomicalStructure"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "mass", "type": "Finding"}, {"text": "ventricular tachyarrhythmias", "type": "BiologicFunction"}]}

Example input:
Sentence: Increased VWF levels are observed in hypertension ( HTN ) and disorders of endothelial dysfunction , for example , atherosclerotic heart disease ( ASHD ) and diabetes .

Example answer:
{"entities": [{"text": "VWF", "type": "Chemical"}, {"text": "hypertension", "type": "BiologicFunction"}, {"text": "HTN", "type": "BiologicFunction"}, {"text": "endothelial dysfunction", "type": "BiologicFunction"}, {"text": "atherosclerotic heart disease", "type": "BiologicFunction"}, {"text": "ASHD", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: 1 mmol / L ) had an increased risk of supraventricular arrhythmia and ventricular ectopy .

Example answer:
{"entities": [{"text": "supraventricular arrhythmia", "type": "BiologicFunction"}, {"text": "ventricular ectopy", "type": "BiologicFunction"}]}

Example input:
Sentence: PaO2 / FiO2 increased significantly at H24 .

Example answer:
{"entities": [{"text": "PaO2 / FiO2", "type": "HealthCareActivity"}]}

Example input:
Sentence: Results indicated no significant relationship between overall frequency of VLs and change in client emotion .

Example answer:
{"entities": [{"text": "emotion", "type": "BiologicFunction"}]}

Example input:
Sentence: However , an increase in frequency of high VLs was associated with an increase in positive affect ( PA ) and a decrease in negative affect (  ) while an increase in frequency of low VLs was associated with a decrease in PA and no change in  .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "affect", "type": "BiologicFunction"}, {"text": "PA", "type": "BiologicFunction"}, {"text": "negative", "type": "Finding"}, {"text": "", "type": "BiologicFunction"}]}

Example input:
Sentence: VL 6 was associated with an increase in PA and a decrease in  .

Example answer:
{"entities": [{"text": "PA", "type": "BiologicFunction"}, {"text": "", "type": "BiologicFunction"}]}

Input:
Sentence: An increase in frequency of VL 4 was associated with an increase in  .

## Item MedMentions:test:2512
Example input:
Sentence: From the data obtained , the correlation between the two physicians was found to be statistically significant ( p = 0 . 000 ) in terms of the means of both subtitles and total scores .

Example answer:
{"entities": [{"text": "physicians", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Here , we investigated whether individual differences in the magnitude of these distortions are shared between tactile distance perception and position sense , as would be predicted by the hypothesis that a single distorted body model underlies both tasks .

Example answer:
{"entities": [{"text": "distortions", "type": "AnatomicalStructure"}, {"text": "distance perception", "type": "BiologicFunction"}, {"text": "position sense", "type": "BiologicFunction"}]}

Example input:
Sentence: The correction was uneventful with good functional outcome .

Example answer:
{"entities": []}

Example input:
Sentence: However , the task is far from straightforward due to data issues such as class imbalance or correlated features .

Example answer:
{"entities": [{"text": "class imbalance", "type": "IntellectualProduct"}]}

Example input:
Sentence: There is a positive correlation ( r = 0 . 80 ) and moderate agreement ( κ = 0 . 509 ) of grading with PC - MRI and 3D - CISS sequences .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "grading", "type": "IntellectualProduct"}, {"text": "PC - MRI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using correlation analysis , the main findings indicated that agreement varied as a result of the child 's difficulties for reports of conduct problems , and this seemed to be related to the presence or absence of externalising difficulties in the child 's presentation .

Example answer:
{"entities": [{"text": "correlation analysis", "type": "ResearchActivity"}, {"text": "indicated", "type": "Finding"}, {"text": "reports", "type": "IntellectualProduct"}, {"text": "conduct problems", "type": "Finding"}, {"text": "presence", "type": "Finding"}, {"text": "externalising difficulties", "type": "Finding"}]}

Example input:
Sentence: In four experiments , participants studied a map either while performing a simultaneous interference task ( high cognitive load ) or without interference ( low cognitive load ) .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "interference task", "type": "BiologicFunction"}, {"text": "without interference", "type": "BiologicFunction"}]}

Example input:
Sentence: Importantly , we also find positive correlations between the severity of the face recognition impairment and the degree of impaired performance with degraded objects .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "degraded", "type": "Finding"}]}

Example input:
Sentence: Confirmatory factor analysis revealed the loadings of a single ( broad ability ) factor model were equal across both measurement occasions , but the lack of intercept invariance suggested that mean -level comparisons are more appropriately carried out at a subtest level .

Example answer:
{"entities": []}

Example input:
Sentence: Moreover , within each task there were clear split - half correlations , demonstrating that both tasks show consistent individual differences .

Example answer:
{"entities": [{"text": "split - half correlations", "type": "IntellectualProduct"}]}

Input:
Sentence: Critically , however , there was no correlation between the magnitudes of distortion in the two tasks .

## Item MedMentions:test:2386
Example input:
Sentence: After 4 weeks , self - efficacy , health and well - being scores significantly improved : 63 % of lifestyle goals and 89 % of health management goals were fully achieved ; 58 % of referrals to community lifestyle behaviour change services and 79 % of referrals to other services ( e . g .

Example answer:
{"entities": [{"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "significantly improved", "type": "Finding"}, {"text": "goals", "type": "IntellectualProduct"}, {"text": "achieved", "type": "Finding"}, {"text": "referrals to", "type": "HealthCareActivity"}, {"text": "community", "type": "Organization"}, {"text": "services", "type": "HealthCareActivity"}]}

Example input:
Sentence: Methods Individual and small group semistructured interviews were undertaken with 29 leaders across Australia , reflecting a diverse cross - section of senior public health managers and program implementation staff from state and territory health departments , as well as academics , thought leaders and public health advocates .

Example answer:
{"entities": [{"text": "small group semistructured interviews", "type": "ResearchActivity"}, {"text": "Australia", "type": "SpatialConcept"}, {"text": "senior public health managers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "state and territory health departments", "type": "Organization"}, {"text": "academics", "type": "Organization"}, {"text": "public health advocates", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: What will it take to improve prevention of chronic diseases in Australia ? A case study of two national approaches Objective Despite being a healthy country by international standards , Australia has a growing and serious burden from chronic diseases .

Example answer:
{"entities": [{"text": "Australia", "type": "SpatialConcept"}, {"text": "A case study", "type": "IntellectualProduct"}, {"text": "chronic diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Three months after treatment , > 30 % improvement was seen in 10 / 33 ( 30 % ) of VRET participants and 12 / 33 ( 36 % ) in CET .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "VRET", "type": "HealthCareActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "CET", "type": "HealthCareActivity"}]}

Example input:
Sentence: Since the 1970s , clinicians and researchers have all been working towards improving the health of Indigenous Australians .

Example answer:
{"entities": [{"text": "clinicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "researchers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Australians", "type": "PopulationGroup"}]}

Example input:
Sentence: 422 students from across Australia and Canada completed the survey between July 2014 and July 2015 .

Example answer:
{"entities": [{"text": "students", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Australia", "type": "SpatialConcept"}, {"text": "Canada", "type": "SpatialConcept"}, {"text": "survey", "type": "IntellectualProduct"}]}

Example input:
Sentence: Participants ' self - reported level of knowledge , skill and capacity in identifying priorities , engaging men and influencing practice beyond their own organisation increased immediately following training ( P < 0 . 001 ) and , with the exception of improving capacity to engage men and influencing practice beyond their organisation , these improvements were sustained at 5 - month post training ( P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "Participants '", "type": "PopulationGroup"}, {"text": "self - reported level of knowledge", "type": "Finding"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: Between 2012 and 2015 , ENGAGE Trainers ( n = 57 ) delivered 62 1 - day training programmes to 810 participants .

Example answer:
{"entities": [{"text": "ENGAGE", "type": "Organization"}, {"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: The IMPROVE programme has been well received in Australia and in three different international settings and is now being made available through ISA .

Example answer:
{"entities": [{"text": "Australia", "type": "SpatialConcept"}, {"text": "settings", "type": "SpatialConcept"}, {"text": "ISA", "type": "Organization"}]}

Example input:
Sentence: The IMPROVE programme was delivered to health professionals in maternity hospitals in all seven Australian states and territories and modified for use internationally with piloting in Vietnam , Fiji , and the Netherlands ( with the assistance of the International Stillbirth Alliance , ISA ) .

Example answer:
{"entities": [{"text": "health professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "maternity hospitals", "type": "Organization"}, {"text": "Australian", "type": "SpatialConcept"}, {"text": "states", "type": "SpatialConcept"}, {"text": "Vietnam", "type": "SpatialConcept"}, {"text": "Fiji", "type": "SpatialConcept"}, {"text": "Netherlands", "type": "SpatialConcept"}, {"text": "assistance", "type": "HealthCareActivity"}, {"text": "International Stillbirth Alliance", "type": "Organization"}, {"text": "ISA", "type": "Organization"}]}

Input:
Sentence: Over the period May 2012 to May 2015 , 30 IMPROVE workshops were conducted , including 26 with 758 participants in Australia and four with 136 participants internationally .

## Item MedMentions:test:2009
Example input:
Sentence: In the present study we assessed in non - human primates ( NHPs ) the effects of a novel PDE10A inhibitor ( FRM - 6308 ) that has demonstrated high potency and selectivity for human recombinant PDE10A in vitro .

Example answer:
{"entities": [{"text": "non - human primates", "type": "Eukaryote"}, {"text": "NHPs", "type": "Eukaryote"}, {"text": "PDE10A inhibitor", "type": "Chemical"}, {"text": "FRM - 6308", "type": "Chemical"}, {"text": "human recombinant PDE10A", "type": "Chemical"}]}

Example input:
Sentence: Polycythemia is an independent risk factor for all - cause in - hospital mortality in COPD patients with PE at low risk .

Example answer:
{"entities": [{"text": "Polycythemia", "type": "BiologicFunction"}, {"text": "risk factor", "type": "Finding"}, {"text": "COPD", "type": "BiologicFunction"}, {"text": "PE", "type": "BiologicFunction"}]}

Example input:
Sentence: Plasma plasminogen activator inhibitor - 1 ( PAI - 1 ) as an inflammatory mediator and urinary necoutrophil gelatinase - associated lipocalin ( NGAL ) as a marker of kidney injury were investigated .

Example answer:
{"entities": [{"text": "Plasma", "type": "BodySubstance"}, {"text": "plasminogen activator inhibitor - 1", "type": "Chemical"}, {"text": "PAI - 1", "type": "Chemical"}, {"text": "inflammatory mediator", "type": "Chemical"}, {"text": "necoutrophil gelatinase - associated lipocalin", "type": "Chemical"}, {"text": "NGAL", "type": "Chemical"}, {"text": "marker", "type": "ClinicalAttribute"}, {"text": "kidney injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: CS - PEG decorated PLGA nano - prototype for delivery of bioactive compounds : A novel approach for induction of apoptosis in HepG2 cell line Polymer - based nanoparticles are used as vectors for cancer drug delivery .

Example answer:
{"entities": [{"text": "CS", "type": "Chemical"}, {"text": "PEG", "type": "Chemical"}, {"text": "PLGA nano - prototype", "type": "Chemical"}, {"text": "bioactive compounds", "type": "Chemical"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "HepG2 cell line", "type": "AnatomicalStructure"}, {"text": "Polymer", "type": "Chemical"}, {"text": "vectors", "type": "SpatialConcept"}, {"text": "cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Mice were subcutaneously injected with nPbHsp60 or rPbHsp60 emulsified in complete 's Freund Adjuvant ( CFA ) at three weeks after intravenous injection of P .

Example answer:
{"entities": [{"text": "Mice", "type": "Eukaryote"}, {"text": "nPbHsp60", "type": "Chemical"}, {"text": "rPbHsp60", "type": "Chemical"}, {"text": "emulsified", "type": "BiologicFunction"}, {"text": "complete 's Freund Adjuvant", "type": "Chemical"}, {"text": "CFA", "type": "Chemical"}, {"text": "P .", "type": "Eukaryote"}]}

Example input:
Sentence: CS - PEG -blended PLGA nano - delivery system of quercetin , ellagic acid and gallic acid can potentiate apoptosis - mediated cell death in HepG2 cell line .

Example answer:
{"entities": [{"text": "CS", "type": "Chemical"}, {"text": "PEG", "type": "Chemical"}, {"text": "PLGA", "type": "Chemical"}, {"text": "quercetin", "type": "Chemical"}, {"text": "ellagic acid", "type": "Chemical"}, {"text": "gallic acid", "type": "Chemical"}, {"text": "apoptosis - mediated", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "HepG2 cell line", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Adult Sprague - Dawley rats received a CCI injury followed by an intraperitoneal injection of PYC ( 50 or 100mg / kg ) .

Example answer:
{"entities": [{"text": "Sprague - Dawley rats", "type": "Eukaryote"}, {"text": "CCI injury", "type": "InjuryOrPoisoning"}, {"text": "intraperitoneal injection", "type": "HealthCareActivity"}, {"text": "PYC", "type": "Chemical"}]}

Example input:
Sentence: These results suggest that PEG - PLA - coated CWO NPs are promising materials for use in CT contrast .

Example answer:
{"entities": [{"text": "PEG - PLA", "type": "Chemical"}, {"text": "CT", "type": "HealthCareActivity"}]}

Example input:
Sentence: PEG - PLA - coated CWO NPs are chemically stable and completely nontoxic .

Example answer:
{"entities": [{"text": "PEG - PLA", "type": "Chemical"}]}

Example input:
Sentence: When intratumorally administered , PEG - PLA - coated CWO NPs showed complete retention in a tumor - bearing mouse model ( measurements were made up to 1 week ) .

Example answer:
{"entities": [{"text": "PEG - PLA", "type": "Chemical"}, {"text": "tumor - bearing mouse model", "type": "BiologicFunction"}]}

Input:
Sentence: IV - injected PEG - PLA / CWO NPs caused no histopathologic damage in major excretory organs ( heart , liver , lungs , spleen , and kidney ) .

## Item MedMentions:test:2484
Example input:
Sentence: Compared to cognitively preserved ( CP ) , CI patients had higher T2 WM lesion volume ( LV ) , lower NBV and GMV , and more severe diffusivity abnormalities in WM lesions , cortex , and NAWM .

Example answer:
{"entities": [{"text": "CI", "type": "BiologicFunction"}, {"text": "abnormalities", "type": "AnatomicalStructure"}, {"text": "WM lesions", "type": "Finding"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "NAWM", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The first 89 patients received standard radiation doses ; their data were reconstructed using AIDR 3D , whereas the last 95 patients received in average 20 % reduction in tube current ; their data were reconstructed using FIRST .

Example answer:
{"entities": [{"text": "AIDR 3D", "type": "IntellectualProduct"}, {"text": "FIRST", "type": "HealthCareActivity"}]}

Example input:
Sentence: PFTs averaged over all patients and parameters demonstrated small absolute declines , 5 . 7 % averaged PFT decline , at approximately 1 year of follow - up , but only the diffusing capacity of lung for carbon monoxide ( DLCO ) demonstrated a statistically significant decline ( 10 . 29 vs .

Example answer:
{"entities": [{"text": "PFTs", "type": "HealthCareActivity"}, {"text": "PFT", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Staffing levels can be higher for linacs and more staff training is required for linacs .

Example answer:
{"entities": [{"text": "linacs", "type": "MedicalDevice"}]}

Example input:
Sentence: In shielding , the requirements for a concrete bunker are similar for cobalt - 60 machines and linacs but extra shielding and protection from neutrons are required for linacs .

Example answer:
{"entities": [{"text": "shielding", "type": "Finding"}, {"text": "cobalt - 60 machines", "type": "MedicalDevice"}, {"text": "linacs", "type": "MedicalDevice"}]}

Example input:
Sentence: Infrastructure and maintenance are more demanding for linacs due to the complex electric componentry .

Example answer:
{"entities": [{"text": "Infrastructure", "type": "IntellectualProduct"}, {"text": "linacs", "type": "MedicalDevice"}]}

Example input:
Sentence: Radiation therapy was delivered on a Cobalt - 60 unit using a single fraction of 16 Gy .

Example answer:
{"entities": [{"text": "Radiation therapy", "type": "HealthCareActivity"}, {"text": "Cobalt - 60", "type": "Chemical"}]}

Example input:
Sentence: Security is more complex for cobalt - 60 machines because of the high activity radioactive source .

Example answer:
{"entities": [{"text": "cobalt - 60 machines", "type": "MedicalDevice"}, {"text": "radioactive source", "type": "Chemical"}]}

Example input:
Sentence: In summary , there is no simple answer to the question of the choice of either cobalt - 60 machines or linacs for radiotherapy in low - and middle - income countries .

Example answer:
{"entities": [{"text": "cobalt - 60 machines", "type": "MedicalDevice"}, {"text": "linacs", "type": "MedicalDevice"}, {"text": "radiotherapy", "type": "HealthCareActivity"}, {"text": "low -", "type": "Finding"}, {"text": "countries", "type": "SpatialConcept"}]}

Example input:
Sentence: Cobalt - 60 Machines and Medical Linear Accelerators : Competing Technologies for External Beam Radiotherapy Medical linear accelerators ( linacs ) and cobalt - 60 machines are both mature technologies for external beam radiotherapy .

Example answer:
{"entities": [{"text": "Cobalt - 60 Machines", "type": "MedicalDevice"}, {"text": "Medical Linear Accelerators", "type": "MedicalDevice"}, {"text": "External Beam Radiotherapy", "type": "HealthCareActivity"}, {"text": "Medical linear accelerators", "type": "MedicalDevice"}, {"text": "linacs", "type": "MedicalDevice"}, {"text": "cobalt - 60 machines", "type": "MedicalDevice"}, {"text": "external beam radiotherapy", "type": "HealthCareActivity"}]}

Input:
Sentence: Patient throughput can be affected by source decay for cobalt - 60 machines but poor maintenance and breakdowns can severely affect patient throughput for linacs .

## Item MedMentions:test:2592
Example input:
Sentence: Copyright © 2016 John Wiley & Sons , Ltd .

Example answer:
{"entities": []}

Example input:
Sentence: Copyright © 2016 John Wiley & Sons , Ltd .

Example answer:
{"entities": []}

Example input:
Sentence: Copyright © 2016 John Wiley & Sons , Ltd .

Example answer:
{"entities": []}

Example input:
Sentence: Copyright © 2016 John Wiley & Sons , Ltd .

Example answer:
{"entities": []}

Example input:
Sentence: Copyright © 2016 John Wiley & Sons , Ltd .

Example answer:
{"entities": []}

Example input:
Sentence: © 2016 American Cancer Society .

Example answer:
{"entities": []}

Example input:
Sentence: © 2016 American Cancer Society .

Example answer:
{"entities": []}

Example input:
Sentence: © 2016 by John Wiley & Sons , Inc . Journal Article 2016 - 08 - 18 00 : 00 : 00

Example answer:
{"entities": []}

Example input:
Sentence: © 2016 AACRSee related commentary by Qiao and Lovly , p .

Example answer:
{"entities": []}

Example input:
Sentence: © 2017 AACR .

Example answer:
{"entities": []}

Input:
Sentence: © 2016 AACR .

## Item MedMentions:test:2183
Example input:
Sentence: Glycogen metabolism and respiration were higher in Synechocystis and Anabaena than in S .

Example answer:
{"entities": [{"text": "Glycogen metabolism", "type": "BiologicFunction"}, {"text": "respiration", "type": "BiologicFunction"}, {"text": "Synechocystis", "type": "Bacterium"}, {"text": "Anabaena", "type": "Bacterium"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: Detachment of the fucoxanthin chlorophyll a / c binding protein ( FCP ) antenna is not involved in the acclimative regulation of photoprotection in the pennate diatom Phaeodactylum tricornutum When grown under intermittent light ( IL ) , the pennate diatom Phaeodactylum tricornutum forms ' super ' non - photochemical fluorescence quenching ( NPQ ) in response to excess light .

Example answer:
{"entities": [{"text": "fucoxanthin chlorophyll a / c binding protein", "type": "Chemical"}, {"text": "FCP", "type": "Chemical"}, {"text": "antenna", "type": "AnatomicalStructure"}, {"text": "acclimative", "type": "BiologicFunction"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "photoprotection", "type": "BiologicFunction"}, {"text": "pennate diatom", "type": "Eukaryote"}, {"text": "Phaeodactylum tricornutum", "type": "Eukaryote"}, {"text": "' super ' non - photochemical fluorescence quenching", "type": "BiologicFunction"}, {"text": "NPQ", "type": "BiologicFunction"}]}

Example input:
Sentence: We then used a cAMP - dependent luciferase reporter assay to investigate light - dependent cAMP responses in cultured cells expressing zebrafish , pufferfish , anole and chicken Opn3 .

Example answer:
{"entities": [{"text": "cAMP", "type": "Chemical"}, {"text": "luciferase", "type": "Chemical"}, {"text": "reporter", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "responses", "type": "BiologicFunction"}, {"text": "cultured cells", "type": "AnatomicalStructure"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "zebrafish", "type": "Eukaryote"}, {"text": "pufferfish", "type": "Eukaryote"}, {"text": "anole", "type": "Eukaryote"}, {"text": "chicken", "type": "Eukaryote"}, {"text": "Opn3", "type": "Chemical"}]}

Example input:
Sentence: Real - time PCR analysis showed that the expression levels of genes associated with chlorophyll biosynthesis and chloroplast development were concurrently altered in the ygdl - 1 mutant .

Example answer:
{"entities": [{"text": "Real - time PCR analysis", "type": "HealthCareActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "chlorophyll", "type": "Chemical"}, {"text": "chloroplast", "type": "AnatomicalStructure"}, {"text": "development", "type": "BiologicFunction"}, {"text": "ygdl - 1 mutant", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , using fluorescence microscopy and chromosome conformation capture in conjunction with deep sequencing ( Hi - C ) , we show that in Caulobacter crescentus , both transcription rate and transcript length , independent of concurrent translation , drive the formation of domain boundaries .

Example answer:
{"entities": [{"text": "fluorescence microscopy", "type": "HealthCareActivity"}, {"text": "deep sequencing", "type": "ResearchActivity"}, {"text": "Caulobacter crescentus", "type": "Bacterium"}, {"text": "transcription", "type": "BiologicFunction"}, {"text": "transcript", "type": "Chemical"}, {"text": "translation", "type": "BiologicFunction"}, {"text": "domain boundaries", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Cyanobacterial Surface Display System Mediates Engineered Interspecies and Abiotic Binding Cyanobacteria are uniquely suited for the development of sustainable bioproduction platforms but are currently underutilized in scaled applications in part due to a lack of genetic tools .

Example answer:
{"entities": [{"text": "Cyanobacterial", "type": "Bacterium"}, {"text": "Surface Display System", "type": "ResearchActivity"}, {"text": "Engineered Interspecies", "type": "BiologicFunction"}, {"text": "Cyanobacteria", "type": "Bacterium"}, {"text": "genetic tools", "type": "ResearchActivity"}]}

Example input:
Sentence: Moreover , DNA replication activity in Synechocystis and Anabaena was reduced to the same level as that in S .

Example answer:
{"entities": [{"text": "DNA replication activity", "type": "BiologicFunction"}, {"text": "Synechocystis", "type": "Bacterium"}, {"text": "Anabaena", "type": "Bacterium"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: Interestingly , DNA replication activity in Synechocystis and Anabaena was retained when cells were transferred to the dark , although it was drastically decreased in S .

Example answer:
{"entities": [{"text": "DNA replication activity", "type": "BiologicFunction"}, {"text": "Synechocystis", "type": "Bacterium"}, {"text": "Anabaena", "type": "Bacterium"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "transferred to", "type": "Finding"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: In Synechococcus elongatus PCC 7942 , one of the model cyanobacteria , DNA replication depends on photosynthetic electron transport .

Example answer:
{"entities": [{"text": "Synechococcus elongatus PCC 7942", "type": "Bacterium"}, {"text": "cyanobacteria", "type": "Bacterium"}, {"text": "DNA replication", "type": "BiologicFunction"}, {"text": "photosynthetic electron transport", "type": "BiologicFunction"}]}

Example input:
Sentence: These results demonstrate that there is disparity in DNA replication occurring in the dark among cyanobacteria , which is caused by the difference in activity of respiratory electron transport .

Example answer:
{"entities": [{"text": "disparity", "type": "Finding"}, {"text": "DNA replication", "type": "BiologicFunction"}, {"text": "cyanobacteria", "type": "Bacterium"}, {"text": "electron transport", "type": "BiologicFunction"}]}

Input:
Sentence: Variety of DNA Replication Activity Among Cyanobacteria Correlates with Distinct Respiration Activity in the Dark Cyanobacteria exhibit light -dependent cell growth since most of their cellular energy is obtained by photosynthesis .

## Item MedMentions:test:2353
Example input:
Sentence: 3 % ) participants ; the prevalence of unilateral and bilateral MGD was 26 . 3 % ( 95 % CI : 24 . 5 - 28 . 1 ) and 26 .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "MGD", "type": "BiologicFunction"}]}

Example input:
Sentence: We selected seven targets of NCD risk factors : tobacco use , alcohol use , diet ( salt / sugar intake , vegetable / fruit consumption ) , raised blood pressure , raised blood glucose , physical inactivity and weight measures .

Example answer:
{"entities": [{"text": "NCD", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "diet", "type": "Food"}, {"text": "sugar intake", "type": "Finding"}, {"text": "vegetable", "type": "Food"}, {"text": "fruit", "type": "Food"}, {"text": "raised blood pressure", "type": "Finding"}, {"text": "raised blood glucose", "type": "Finding"}]}

Example input:
Sentence: The 2009 World Health Organisation ( WHO ) Global Health Risks Report was used as a framework to determine the prevalence and number of eight key risk factors for cardiovascular disease ( CVD ) in men and women with psychosis .

Example answer:
{"entities": [{"text": "World Health Organisation", "type": "Organization"}, {"text": "WHO", "type": "Organization"}, {"text": "Report", "type": "IntellectualProduct"}, {"text": "framework", "type": "IntellectualProduct"}, {"text": "cardiovascular disease", "type": "BiologicFunction"}, {"text": "CVD", "type": "BiologicFunction"}, {"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "psychosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Change from nomadic to settled life might be accompanied by higher prevalence of NCDs .

Example answer:
{"entities": [{"text": "settled", "type": "Finding"}, {"text": "NCDs", "type": "BiologicFunction"}]}

Example input:
Sentence: 411 ; 95 % CI : 0 . 169 - 0 . 999 ) ; and being from the North central were significant risk factors ( OR = 3 . 731 ; 95 % CI : 1 . 450 - 9 . 599 ) .

Example answer:
{"entities": [{"text": "North central", "type": "SpatialConcept"}, {"text": "risk factors", "type": "Finding"}]}

Example input:
Sentence: Interobserver agreement on the reclassification of ND cases was moderate ( k = 0 . 57 ) , and consensus yielded 48 ND cases ( 33 % ) , 72 benign cases ( 49 % ) , 24 cases of atypia of undetermined significance ( 16 % ) , and 2 cases suspicious for malignancy ( 1 % ) .

Example answer:
{"entities": [{"text": "reclassification", "type": "IntellectualProduct"}, {"text": "ND", "type": "Finding"}, {"text": "atypia", "type": "Finding"}, {"text": "undetermined significance", "type": "Finding"}, {"text": "suspicious for malignancy", "type": "Finding"}]}

Example input:
Sentence: One hundred forty - six of the 151 cases initially classified as ND were available for review , and they had a mean cell count of 60 . 5 ( standard deviation , 71 . 4 ) .

Example answer:
{"entities": [{"text": "classified", "type": "IntellectualProduct"}, {"text": "ND", "type": "Finding"}, {"text": "cell count", "type": "HealthCareActivity"}]}

Example input:
Sentence: Distribution and patterning of non - communicable disease risk factors in indigenous Mbororo and non - autochthonous populations in Cameroon : cross sectional study Data on Non - Communicable Diseases ( NCDs ) among indigenous populations are needed for interventions to improve health care .

Example answer:
{"entities": [{"text": "patterning", "type": "SpatialConcept"}, {"text": "non - communicable disease", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "Mbororo", "type": "PopulationGroup"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "Cameroon", "type": "SpatialConcept"}, {"text": "cross sectional study", "type": "ResearchActivity"}, {"text": "Non - Communicable Diseases", "type": "BiologicFunction"}, {"text": "NCDs", "type": "BiologicFunction"}, {"text": "interventions", "type": "HealthCareActivity"}, {"text": "improve", "type": "Finding"}, {"text": "health care", "type": "HealthCareActivity"}]}

Example input:
Sentence: Distribution of NCD risk factors was high among settled Fulani ( Fulbe ) when compared to indigenous nomadic Fulani ( Mbororo ) .

Example answer:
{"entities": [{"text": "NCD", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "Fulani", "type": "PopulationGroup"}, {"text": "Fulbe", "type": "PopulationGroup"}, {"text": "Mbororo", "type": "PopulationGroup"}]}

Example input:
Sentence: The prevalence of MGD was summarized as percentage and 95 % confidence intervals ( CI ) , and related factors were studied through simple and multiple logistic regressions .

Example answer:
{"entities": [{"text": "MGD", "type": "BiologicFunction"}, {"text": "logistic regressions", "type": "ResearchActivity"}]}

Input:
Sentence: Prevalence of NCD risk factors was summarised by descriptive statistics .

## Item MedMentions:test:1996
Example input:
Sentence: In contrast , the cladofulvin over - producers caused strong necrosis and desiccation of tomato leaves , which , in turn , arrested conidiation .

Example answer:
{"entities": [{"text": "cladofulvin", "type": "Chemical"}, {"text": "over - producers", "type": "Finding"}, {"text": "necrosis", "type": "BiologicFunction"}, {"text": "tomato", "type": "Eukaryote"}, {"text": "leaves", "type": "Eukaryote"}, {"text": "conidiation", "type": "BiologicFunction"}]}

Example input:
Sentence: AR37 - infected ryegrass grown at high temperature contained high in plant a concentrations of epoxy - janthitrem ( 30 . 6 μg / g in leaves and 83 . 9 μg / g in pseudostems ) that had a strong anti - feedant effect on porina larvae when incorporated into their diets , reducing their survival by 25 - 42 % on pseudostems .

Example answer:
{"entities": [{"text": "AR37", "type": "Eukaryote"}, {"text": "infected", "type": "BiologicFunction"}, {"text": "ryegrass", "type": "Eukaryote"}, {"text": "plant", "type": "Eukaryote"}, {"text": "epoxy - janthitrem", "type": "Chemical"}, {"text": "leaves", "type": "Eukaryote"}, {"text": "pseudostems", "type": "Finding"}, {"text": "anti - feedant", "type": "Finding"}, {"text": "porina larvae", "type": "Eukaryote"}, {"text": "diets", "type": "Food"}]}

Example input:
Sentence: Combining solar heating with organic matter amendment resulted in accelerated weed seed inactivation compared with either approach alone .

Example answer:
{"entities": [{"text": "organic matter amendment", "type": "Eukaryote"}, {"text": "weed", "type": "Eukaryote"}, {"text": "seed", "type": "Eukaryote"}]}

Example input:
Sentence: In comparison , in planta epoxy - janthitrem concentrations in AR37 - infected ryegrass grown at low temperature were very low ( 0 . 67 μg / g in leaves and 7 . 4 μg / g in pseudostems ) resulting in a small anti - feedant effect in perennial but not in Italian ryegrass .

Example answer:
{"entities": [{"text": "planta", "type": "Eukaryote"}, {"text": "epoxy - janthitrem", "type": "Chemical"}, {"text": "AR37", "type": "Eukaryote"}, {"text": "infected", "type": "BiologicFunction"}, {"text": "ryegrass", "type": "Eukaryote"}, {"text": "leaves", "type": "Eukaryote"}, {"text": "pseudostems", "type": "Finding"}, {"text": "anti - feedant", "type": "Finding"}, {"text": "perennial", "type": "Eukaryote"}, {"text": "Italian", "type": "SpatialConcept"}]}

Example input:
Sentence: Ultimately , changes in CO2 and endophyte status will likely alter multiple physiological responses in toxic plants such as locoweed , but it is difficult to predict how these changes will impact plant herbivore interactions .

Example answer:
{"entities": [{"text": "CO2", "type": "Chemical"}, {"text": "endophyte", "type": "Eukaryote"}, {"text": "physiological responses", "type": "BiologicFunction"}, {"text": "toxic plants", "type": "Eukaryote"}, {"text": "locoweed", "type": "Eukaryote"}, {"text": "plant", "type": "Eukaryote"}, {"text": "herbivore", "type": "Eukaryote"}]}

Example input:
Sentence: Metabolic Interference of sod gene mutations on catalase activity in Escherichia coli exposed to Gramoxone ® ( paraquat ) herbicide Herbicides are continuously used to minimize the loss of crop productivity in agricultural environments .

Example answer:
{"entities": [{"text": "sod", "type": "Chemical"}, {"text": "gene mutations", "type": "BiologicFunction"}, {"text": "catalase activity", "type": "BiologicFunction"}, {"text": "Escherichia coli", "type": "Bacterium"}, {"text": "Gramoxone", "type": "Chemical"}, {"text": "paraquat", "type": "Chemical"}, {"text": "herbicide", "type": "Chemical"}, {"text": "Herbicides", "type": "Chemical"}, {"text": "crop", "type": "Eukaryote"}, {"text": "agricultural environments", "type": "SpatialConcept"}]}

Example input:
Sentence: The results showed that soil fumigation significantly ( P < 0 . 05 ) extended the degradation period of these herbicides in the field and in laboratory studies .

Example answer:
{"entities": [{"text": "results", "type": "Finding"}, {"text": "extended", "type": "SpatialConcept"}, {"text": "herbicides", "type": "Chemical"}, {"text": "field", "type": "SpatialConcept"}, {"text": "laboratory studies", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , phytotoxicity has been observed in ginger seedlings following the application of herbicides in fumigated fields .

Example answer:
{"entities": [{"text": "phytotoxicity", "type": "InjuryOrPoisoning"}, {"text": "ginger", "type": "Food"}, {"text": "seedlings", "type": "Eukaryote"}, {"text": "herbicides", "type": "Chemical"}, {"text": "fields", "type": "SpatialConcept"}]}

Example input:
Sentence: The study concluded that applying a dose below the recommended rate of these herbicides in chloropicrin ( CP ) or CP + 1 , 3 - dichloropropene fumigated ginger fields is appropriate , as application of the recommended herbicide dose in fumigated soil may be phytotoxic to ginger .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "herbicides", "type": "Chemical"}, {"text": "chloropicrin", "type": "Chemical"}, {"text": "CP", "type": "Chemical"}, {"text": "1 , 3 - dichloropropene", "type": "Chemical"}, {"text": "ginger", "type": "Food"}, {"text": "fields", "type": "SpatialConcept"}, {"text": "herbicide", "type": "Chemical"}]}

Example input:
Sentence: This study tested a mixture of herbicides ( pendimethalin and oxyfluorfen ) and several fumigant treatments in laboratory and field studies to determine their effect on the growth of ginger .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "herbicides", "type": "Chemical"}, {"text": "pendimethalin", "type": "Chemical"}, {"text": "oxyfluorfen", "type": "Chemical"}, {"text": "fumigant", "type": "Chemical"}, {"text": "laboratory", "type": "HealthCareActivity"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "ginger", "type": "Food"}]}

Input:
Sentence: Moreover , the extended period of herbicide degradation in the fumigant and nonfumigant treatments significantly reduced ginger plant height , leaf number , stem diameter , and the chlorophyll content .

## Item MedMentions:test:2559
Example input:
Sentence: Near and distance stereopsis in treatment group were better than controls at 3 - and 6 - months ( p < 0 . 05 ) .

Example answer:
{"entities": [{"text": "stereopsis", "type": "BiologicFunction"}, {"text": "treatment group", "type": "PopulationGroup"}]}

Example input:
Sentence: Before the LC , 15 % of 18 - and 24 - month visits had documented ASD screening , compared with 91 % during the last month of the LC ( P < .001 ) .

Example answer:
{"entities": [{"text": "LC", "type": "Organization"}, {"text": "visits", "type": "HealthCareActivity"}, {"text": "documented", "type": "HealthCareActivity"}, {"text": "ASD", "type": "Finding"}, {"text": "screening", "type": "HealthCareActivity"}]}

Example input:
Sentence: Furthermore , it is hard to consider motor stereotypies , even the primary ones , exclusively as a movement disorder .

Example answer:
{"entities": [{"text": "motor stereotypies", "type": "Finding"}, {"text": "movement disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: Twelve patients with hemiparesis ( 10 - 20 years ) and 8 typically developing subjects ( 8 - 17 years ) participated .

Example answer:
{"entities": [{"text": "hemiparesis", "type": "Finding"}, {"text": "subjects", "type": "PopulationGroup"}]}

Example input:
Sentence: From November 2012 to January 2015 , 50 - to 80 - year - old patients with moderate to severe WMLs or more than four lacunar infarctions and cognitive complaints , excluding those with large vascular diseases diagnosed by transcranial cerebral Doppler , were recruited .

Example answer:
{"entities": [{"text": "WMLs", "type": "Finding"}, {"text": "lacunar infarctions", "type": "BiologicFunction"}, {"text": "cognitive complaints", "type": "BiologicFunction"}, {"text": "vascular diseases", "type": "BiologicFunction"}, {"text": "transcranial cerebral Doppler", "type": "HealthCareActivity"}]}

Example input:
Sentence: Numbness was present in 13 , 18 , and 29 patients treated with MVD , RF , and SRS respectively ( p = 0 . 008 ) .

Example answer:
{"entities": [{"text": "Numbness", "type": "Finding"}, {"text": "MVD", "type": "HealthCareActivity"}, {"text": "RF", "type": "HealthCareActivity"}, {"text": "SRS", "type": "HealthCareActivity"}]}

Example input:
Sentence: Developmental Profile and Diagnoses in Children Presenting with Motor Stereotypies Motor stereotypies represent a typical example of the difficulty in distinguishing non - clinical behaviors ( physiological and transient ) from symptoms or among different disorders [ " primary stereotypies , " associated with autistic spectrum disorder ( ASD ) , intellectual disabilities , genetic syndromes , and sensory impairment ] .

Example answer:
{"entities": [{"text": "Profile", "type": "HealthCareActivity"}, {"text": "Diagnoses", "type": "ResearchActivity"}, {"text": "Motor Stereotypies", "type": "Finding"}, {"text": "Motor stereotypies", "type": "Finding"}, {"text": "physiological", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "disorders", "type": "BiologicFunction"}, {"text": "primary stereotypies", "type": "BiologicFunction"}, {"text": "autistic spectrum disorder", "type": "BiologicFunction"}, {"text": "ASD", "type": "BiologicFunction"}, {"text": "intellectual disabilities", "type": "BiologicFunction"}, {"text": "genetic syndromes", "type": "BiologicFunction"}]}

Example input:
Sentence: A 65 - year - old Caucasian lady was referred to our Ataxia Clinic because of a 6 - year history of progressive unsteadiness and a 2 - year history of slurred speech .

Example answer:
{"entities": [{"text": "Caucasian", "type": "PopulationGroup"}, {"text": "lady", "type": "PopulationGroup"}, {"text": "Ataxia", "type": "Finding"}, {"text": "Clinic", "type": "Organization"}, {"text": "history", "type": "Finding"}, {"text": "unsteadiness", "type": "Finding"}, {"text": "slurred speech", "type": "Finding"}]}

Example input:
Sentence: Motor stereotypies in children with normal cognitive level represent a challenging diagnostic issue for which a finely tailored assessment is mandatory in order to define a precise developmental profile .

Example answer:
{"entities": [{"text": "Motor stereotypies", "type": "Finding"}, {"text": "normal cognitive level", "type": "Finding"}, {"text": "issue", "type": "Finding"}, {"text": "assessment", "type": "HealthCareActivity"}]}

Example input:
Sentence: We studied 23 children ( 3 girls ) , aged 36 - 95 months , who requested a consultation due to the persistence or increased severity of motor stereotypies .

Example answer:
{"entities": [{"text": "studied", "type": "ResearchActivity"}, {"text": "consultation", "type": "HealthCareActivity"}, {"text": "motor stereotypies", "type": "Finding"}]}

Input:
Sentence: All patients were showing motor stereotypies for periods of time varying from 6 to 77 months .

## Item MedMentions:test:2078
Example input:
Sentence: Normally , superoxide dismutase ( SOD ) converts superoxide anions to hydrogen peroxide ( H2O2 ) and H2O2 is then naturalized to be water by peroxiredoxin 4 .

Example answer:
{"entities": [{"text": "superoxide dismutase", "type": "Chemical"}, {"text": "SOD", "type": "Chemical"}, {"text": "superoxide anions", "type": "Chemical"}, {"text": "hydrogen peroxide", "type": "Chemical"}, {"text": "H2O2", "type": "Chemical"}, {"text": "water", "type": "Chemical"}, {"text": "peroxiredoxin 4", "type": "Chemical"}]}

Example input:
Sentence: Only MDPV increased reactive oxygen species production at all concentrations tested whereas all 3 drugs increased nitric oxide production .

Example answer:
{"entities": [{"text": "MDPV", "type": "Chemical"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "drugs", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}]}

Example input:
Sentence: Additionally , enhanced total ROS and cytoplasmic superoxide production were observed after exposing cells to MF at 0 .

Example answer:
{"entities": [{"text": "ROS", "type": "Chemical"}, {"text": "cytoplasmic", "type": "AnatomicalStructure"}, {"text": "superoxide", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The strain 's growth patterns under various concentrations of H2 O2 and its scavenging properties towards hydroxyl radical ( 64 . 85 % ) and DPPH ( 84 . 97 % ) were also interesting properties .

Example answer:
{"entities": [{"text": "strain 's", "type": "Bacterium"}, {"text": "growth patterns", "type": "Finding"}, {"text": "H2 O2", "type": "Chemical"}, {"text": "scavenging properties", "type": "BiologicFunction"}, {"text": "hydroxyl radical", "type": "Chemical"}, {"text": "DPPH", "type": "Chemical"}]}

Example input:
Sentence: Malondialdehyde content was significantly higher than that of controls at the higher PFOS concentrations .

Example answer:
{"entities": [{"text": "Malondialdehyde", "type": "Chemical"}, {"text": "PFOS", "type": "Chemical"}]}

Example input:
Sentence: There were significant time and treatment - time interaction effects on methane dicarboxylic aldehyde ( P = 0 . 000 and P = 0 . 050 , respectively ) and myeloperoxidase ( P = 0 . 000 and P = 0 . 001 in xenon and control groups , respectively ) .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "methane dicarboxylic aldehyde", "type": "Chemical"}, {"text": "myeloperoxidase", "type": "Chemical"}]}

Example input:
Sentence: Moreover , the up - regulation of malondialdehyde ( MDA ) and the activity of glutathione peroxidase ( GPx ) were reversed by fucoxanthin treatment .

Example answer:
{"entities": [{"text": "up - regulation", "type": "BiologicFunction"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "MDA", "type": "Chemical"}, {"text": "glutathione peroxidase", "type": "Chemical"}, {"text": "GPx", "type": "Chemical"}, {"text": "fucoxanthin", "type": "Chemical"}]}

Example input:
Sentence: A significant increment of malondialdehyde and reduction in heart total thiol , superoxide dismutase and catalase concentrations were observed in LPS group ( p < 0 .

Example answer:
{"entities": [{"text": "malondialdehyde", "type": "Chemical"}, {"text": "heart", "type": "AnatomicalStructure"}, {"text": "thiol", "type": "Chemical"}, {"text": "superoxide dismutase", "type": "Chemical"}, {"text": "catalase", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}]}

Example input:
Sentence: Levels of ROS and malondialdehyde ( MDA ) were also evaluated .

Example answer:
{"entities": [{"text": "ROS", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "MDA", "type": "Chemical"}]}

Example input:
Sentence: A significant increase in malondialdehyde ( MDA ) was shown , suggesting cell membrane damage and oxidative stress .

Example answer:
{"entities": [{"text": "malondialdehyde", "type": "Chemical"}, {"text": "MDA", "type": "Chemical"}, {"text": "cell membrane", "type": "AnatomicalStructure"}, {"text": "oxidative stress", "type": "BiologicFunction"}]}

Input:
Sentence: Similarly , MDA ( malondialdehyde ) , H2 O2 ( hydrogen peroxide ) , and ( • ) O2 ( - ) ( superoxide anion ) production were effectively decreased in the range of 27 .

## Item MedMentions:test:2110
Example input:
Sentence: Longitudinal traction and lateral pushing angles were more correlated with correction ratios .

Example answer:
{"entities": [{"text": "Longitudinal", "type": "SpatialConcept"}, {"text": "traction", "type": "HealthCareActivity"}, {"text": "lateral pushing angles", "type": "Finding"}]}

Example input:
Sentence: THA in patients with severe hip OA could help correct abnormal sagittal spinal - pelvic - leg alignment and relieve comorbid LBP .

Example answer:
{"entities": [{"text": "THA", "type": "HealthCareActivity"}, {"text": "hip OA", "type": "BiologicFunction"}, {"text": "sagittal", "type": "SpatialConcept"}, {"text": "spinal", "type": "SpatialConcept"}, {"text": "pelvic - leg", "type": "AnatomicalStructure"}, {"text": "comorbid", "type": "Finding"}, {"text": "LBP", "type": "Finding"}]}

Example input:
Sentence: The GCL - MPK showed indicators of increased safety and more natural walking patterns in older and low - active transfemoral amputees in comparison to the standard NMPK already after a short acclimatisation time and no structured physical therapy .

Example answer:
{"entities": [{"text": "GCL - MPK", "type": "HealthCareActivity"}, {"text": "low - active", "type": "Finding"}, {"text": "transfemoral amputees", "type": "HealthCareActivity"}, {"text": "NMPK", "type": "HealthCareActivity"}, {"text": "acclimatisation", "type": "BiologicFunction"}, {"text": "no", "type": "Finding"}, {"text": "structured", "type": "SpatialConcept"}, {"text": "physical therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Furthermore , hip joint inflammation caused an increase in CGRP -positive neurons , but not in IB4 - binding neurons .

Example answer:
{"entities": [{"text": "hip joint", "type": "SpatialConcept"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "CGRP", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "IB4", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}]}

Example input:
Sentence: Asymmetry of lumbopelvic movement patterns during active hip abduction is a risk factor for low back pain development during standing An induced - pain paradigm has been used in back - healthy people to understand risk factors for developing low back pain ( LBP ) during prolonged standing .

Example answer:
{"entities": [{"text": "Asymmetry", "type": "SpatialConcept"}, {"text": "lumbopelvic", "type": "SpatialConcept"}, {"text": "movement patterns", "type": "Finding"}, {"text": "hip", "type": "AnatomicalStructure"}, {"text": "abduction", "type": "HealthCareActivity"}, {"text": "risk factor", "type": "Finding"}, {"text": "low back pain", "type": "Finding"}, {"text": "standing", "type": "SpatialConcept"}, {"text": "back", "type": "SpatialConcept"}, {"text": "people", "type": "PopulationGroup"}, {"text": "understand", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "LBP", "type": "Finding"}]}

Example input:
Sentence: Fluoro - Gold ( FG ) was applied to the hip joint after 7 days , and T12 - L6 DRGs were double - stained for calcitonin gene - related peptide ( CGRP ) and isolection - IB4 1 week later .

Example answer:
{"entities": [{"text": "Fluoro - Gold", "type": "Chemical"}, {"text": "FG", "type": "Chemical"}, {"text": "hip joint", "type": "SpatialConcept"}, {"text": "T12", "type": "AnatomicalStructure"}, {"text": "L6", "type": "AnatomicalStructure"}, {"text": "DRGs", "type": "AnatomicalStructure"}, {"text": "double - stained", "type": "HealthCareActivity"}, {"text": "calcitonin gene - related peptide", "type": "Chemical"}, {"text": "CGRP", "type": "Chemical"}, {"text": "isolection - IB4", "type": "Chemical"}]}

Example input:
Sentence: We examined asymmetry of lumbopelvic movement timing during a clinical test of active hip abduction in back - healthy people who developed LBP symptoms during standing ( Pain Developers ; PDs ) compared to back - healthy people who did not develop LBP symptoms during standing ( Non Pain Developers , NPDs ) .

Example answer:
{"entities": [{"text": "asymmetry", "type": "SpatialConcept"}, {"text": "lumbopelvic", "type": "SpatialConcept"}, {"text": "movement", "type": "BiologicFunction"}, {"text": "hip abduction", "type": "Finding"}, {"text": "people", "type": "PopulationGroup"}, {"text": "developed", "type": "Finding"}, {"text": "LBP", "type": "Finding"}, {"text": "symptoms", "type": "Finding"}, {"text": "standing", "type": "SpatialConcept"}]}

Example input:
Sentence: The recruited 69 patients showed significantly reduced hip flexion and improved global spinal balance at follow - up compared with baseline .

Example answer:
{"entities": [{"text": "global spinal balance", "type": "Finding"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Three subgroups based on hip adduction moment characteristics were identified .

Example answer:
{"entities": [{"text": "subgroups", "type": "IntellectualProduct"}]}

Example input:
Sentence: Individuals with GT exhibit greater hip adduction moment impulse and alterations in trunk and pelvic kinematics during stair ascent .

Example answer:
{"entities": [{"text": "Individuals", "type": "PopulationGroup"}, {"text": "GT", "type": "BiologicFunction"}, {"text": "trunk", "type": "SpatialConcept"}, {"text": "pelvic", "type": "AnatomicalStructure"}, {"text": "kinematics", "type": "BiomedicalOccupationOrDiscipline"}]}

Input:
Sentence: Individuals with GT were 4 . 5 times more likely to have a hip adduction moment characteristic of a large impulse and greater lateral pelvic translation at heel strike than the subgroup most likely to contain controls .

## Item MedMentions:test:2436
Example input:
Sentence: 84 patients were identified for study inclusion , 45 in the pre - intervention and 39 in the intervention group .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: Methods : We compared the case notification rates ( CNRs ) in the intervention year with those of the previous year in the FIDELIS areas , then compared the difference between the CNRs of the intervention year and the previous year in the FIDELIS areas with those in the non - FI - DELIS areas within the province .

Example answer:
{"entities": [{"text": "FIDELIS", "type": "IntellectualProduct"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "non - FI - DELIS", "type": "Finding"}, {"text": "province", "type": "SpatialConcept"}]}

Example input:
Sentence: Full economic evaluations investigating family / family - based interventions for adolescents between 10 and 20 years treated for substance use disorders , delinquency or externalizing disorders were included .

Example answer:
{"entities": [{"text": "family - based interventions", "type": "HealthCareActivity"}, {"text": "substance use disorders", "type": "BiologicFunction"}, {"text": "delinquency", "type": "BiologicFunction"}, {"text": "externalizing disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: Trends in preferred first point of contact ( primary vs secondary , public vs . private ) , reason for choice and health services issues , were described and stratified by patient characteristics , provider type , and rural / urban settings .Between 2002 and 2013 , the average number of PHC consultations increased from 1 .

Example answer:
{"entities": [{"text": "primary", "type": "HealthCareActivity"}, {"text": "secondary", "type": "HealthCareActivity"}, {"text": "public", "type": "Organization"}, {"text": "private", "type": "Organization"}, {"text": "health services", "type": "HealthCareActivity"}, {"text": "rural / urban settings", "type": "SpatialConcept"}, {"text": "PHC", "type": "HealthCareActivity"}, {"text": "consultations", "type": "HealthCareActivity"}]}

Example input:
Sentence: A prospective surveillance study from January 2011 to January 2013 was conducted at the medical wards of a district hospital in southern Taiwan .

Example answer:
{"entities": [{"text": "medical wards", "type": "Organization"}, {"text": "district hospital", "type": "Organization"}, {"text": "southern", "type": "SpatialConcept"}, {"text": "Taiwan", "type": "SpatialConcept"}]}

Example input:
Sentence: Intervention participants received text - messaging support for 30 days and a community health nurse ( CHN ) interventionist performed a home visit with clinical assessment within 5 days after enrollment .

Example answer:
{"entities": [{"text": "Intervention", "type": "HealthCareActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "community health nurse ( CHN ) interventionist", "type": "ProfessionalOrOccupationalGroup"}, {"text": "enrollment", "type": "HealthCareActivity"}]}

Example input:
Sentence: One such intervention involved expanding contact investigation to the community using the Xpert MTB / RIF test .

Example answer:
{"entities": [{"text": "intervention", "type": "HealthCareActivity"}, {"text": "investigation", "type": "HealthCareActivity"}, {"text": "Xpert MTB / RIF test", "type": "HealthCareActivity"}]}

Example input:
Sentence: Community contact investigation beyond household not only detected additional TB patients but also increased TB case detection .

Example answer:
{"entities": [{"text": "investigation", "type": "HealthCareActivity"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "detection", "type": "HealthCareActivity"}]}

Example input:
Sentence: Passive case detection of malaria in Ratanakiri Province ( Cambodia ) to detect villages at higher risk for malaria Cambodia reduced malaria incidence by more than 75 % between 2000 and 2015 , a target of the Millennium Development Goal 6 .

Example answer:
{"entities": [{"text": "Passive case detection", "type": "ResearchActivity"}, {"text": "malaria", "type": "BiologicFunction"}, {"text": "detect", "type": "Finding"}, {"text": "villages", "type": "SpatialConcept"}, {"text": "Millennium Development Goal 6", "type": "IntellectualProduct"}]}

Example input:
Sentence: Here , in the intervention period , July 2013 - June 2015 , contact investigation beyond household was conducted : all people staying within a radius of 50 metres ( using Geographical Information System ) from the household of smear positive TB patients were screened for tuberculosis .

Example answer:
{"entities": [{"text": "intervention", "type": "HealthCareActivity"}, {"text": "investigation", "type": "HealthCareActivity"}, {"text": "people", "type": "PopulationGroup"}, {"text": "Geographical Information System", "type": "IntellectualProduct"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "screened", "type": "HealthCareActivity"}, {"text": "tuberculosis", "type": "BiologicFunction"}]}

Input:
Sentence: Passive case finding and household contact investigation was routinely done in the pre - intervention period July 2011 - June 2013 .

## Item MedMentions:test:1832
Example input:
Sentence: Moreover , decrease or loss of CD82 expression is closely associated with malignancy and poor prognosis in many human cancers including prostate cancer .

Example answer:
{"entities": [{"text": "CD82", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "malignancy", "type": "BiologicFunction"}, {"text": "poor prognosis", "type": "Finding"}, {"text": "human", "type": "Eukaryote"}, {"text": "cancers", "type": "BiologicFunction"}, {"text": "prostate cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: We also observed that SNAI1 expression was correlated with distal metastasis , incomplete tumor capsule formation , and histological differentiation in hepatocellular carcinoma ( HCC ) .

Example answer:
{"entities": [{"text": "SNAI1", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "distal metastasis", "type": "BiologicFunction"}, {"text": "tumor capsule formation", "type": "BiologicFunction"}, {"text": "histological differentiation", "type": "ClinicalAttribute"}, {"text": "hepatocellular carcinoma", "type": "BiologicFunction"}, {"text": "HCC", "type": "BiologicFunction"}]}

Example input:
Sentence: SNAI1 promotes the development of HCC through the enhancement of proliferation and inhibition of apoptosis SNAI1 , a zinc - finger transcription factor , plays an important role in the induction of epithelial - mesenchymal transition ( EMT ) in various cancers .

Example answer:
{"entities": [{"text": "SNAI1", "type": "Chemical"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "inhibition of apoptosis", "type": "BiologicFunction"}, {"text": "zinc - finger transcription factor", "type": "Chemical"}, {"text": "epithelial - mesenchymal transition", "type": "BiologicFunction"}, {"text": "EMT", "type": "BiologicFunction"}, {"text": "cancers", "type": "BiologicFunction"}]}

Example input:
Sentence: Variant 2 of KIAA0101 , antagonizing its oncogenic variant 1 , might be a potential therapeutic strategy in hepatocellular carcinoma Hepatocellular carcinoma ( HCC ) is one of the most lethal malignant tumors worldwide and effective therapies , including molecular therapy , remain elusive .

Example answer:
{"entities": [{"text": "Variant 2", "type": "AnatomicalStructure"}, {"text": "KIAA0101", "type": "AnatomicalStructure"}, {"text": "oncogenic", "type": "AnatomicalStructure"}, {"text": "variant 1", "type": "AnatomicalStructure"}, {"text": "therapeutic strategy", "type": "HealthCareActivity"}, {"text": "hepatocellular carcinoma", "type": "BiologicFunction"}, {"text": "Hepatocellular carcinoma", "type": "BiologicFunction"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "lethal", "type": "Finding"}, {"text": "malignant tumors", "type": "BiologicFunction"}, {"text": "worldwide", "type": "PopulationGroup"}, {"text": "therapies", "type": "HealthCareActivity"}, {"text": "molecular therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: In conclusion , lncRNA ZEB2‑AS1 may be used as a valuable biomarker in patients with HCC .

Example answer:
{"entities": [{"text": "lncRNA", "type": "Chemical"}, {"text": "ZEB2‑AS1", "type": "AnatomicalStructure"}, {"text": "biomarker", "type": "ClinicalAttribute"}, {"text": "HCC", "type": "BiologicFunction"}]}

Example input:
Sentence: The Kaplan‑Meier survival curves suggested that patients with high ZEB2‑AS1 expression levels experienced the lowest overall and recurrence‑free survival rates compared with those that had low expression levels .

Example answer:
{"entities": [{"text": "ZEB2‑AS1", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Additionally , the expression levels of ZEB2‑AS1 were downregulated by transfection of small interfering RNAs ( siRNAs ) to determine whether ZEB2‑AS1 is capable of affecting cell proliferation , invasion and metastasis by regulating ZEB2 , vimentin , fibronectin , E‑cadherin and N‑cadherin expression levels .

Example answer:
{"entities": [{"text": "ZEB2‑AS1", "type": "AnatomicalStructure"}, {"text": "downregulated", "type": "BiologicFunction"}, {"text": "transfection", "type": "BiologicFunction"}, {"text": "small interfering RNAs", "type": "Chemical"}, {"text": "siRNAs", "type": "Chemical"}, {"text": "cell proliferation", "type": "BiologicFunction"}, {"text": "invasion", "type": "BiologicFunction"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "ZEB2", "type": "Chemical"}, {"text": "vimentin", "type": "Chemical"}, {"text": "fibronectin", "type": "Chemical"}, {"text": "E‑cadherin", "type": "Chemical"}, {"text": "N‑cadherin", "type": "Chemical"}]}

Example input:
Sentence: The results of the present study demonstrated that the expression levels of ZEB2‑AS1 were greater in HCC tissues when compared with the adjacent normal tissues .

Example answer:
{"entities": [{"text": "ZEB2‑AS1", "type": "AnatomicalStructure"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "normal tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Furthermore , ZEB2‑AS1 expression was significantly associated with the size of the primary tumor , intrahepatic metastasis and tumor - node - metastasis stage .

Example answer:
{"entities": [{"text": "ZEB2‑AS1", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "size of the primary tumor", "type": "SpatialConcept"}, {"text": "intrahepatic", "type": "SpatialConcept"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "tumor - node - metastasis stage", "type": "IntellectualProduct"}]}

Example input:
Sentence: In addition , the current study demonstrated that the downregulation of ZEB2‑AS1 was associated with decreased tumor growth and metastasis in HCC by the regulation of the expression levels of epithelial mesenchymal transition - induced markers .

Example answer:
{"entities": [{"text": "downregulation", "type": "BiologicFunction"}, {"text": "ZEB2‑AS1", "type": "AnatomicalStructure"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "epithelial mesenchymal transition", "type": "BiologicFunction"}, {"text": "markers", "type": "ClinicalAttribute"}]}

Input:
Sentence: Downregulation of ZEB2 - AS1 decreased tumor growth and metastasis in hepatocellular carcinoma Hepatocellular carcinoma ( HCC ) remains one of the most common types of cancer worldwide and prognosis remains poor .

## Item MedMentions:test:1846
Example input:
Sentence: Antipsychotic Drugs and Risk of Hip Fracture in People Aged 60 and Older in Norway To examine associations between exposure to various subgroups of antipsychotic drugs and risk of hip fracture in older adults .

Example answer:
{"entities": [{"text": "Antipsychotic Drugs", "type": "Chemical"}, {"text": "Hip Fracture", "type": "InjuryOrPoisoning"}, {"text": "People", "type": "PopulationGroup"}, {"text": "Older", "type": "PopulationGroup"}, {"text": "Norway", "type": "SpatialConcept"}, {"text": "antipsychotic drugs", "type": "Chemical"}, {"text": "hip fracture", "type": "InjuryOrPoisoning"}, {"text": "older", "type": "PopulationGroup"}]}

Example input:
Sentence: We evaluated this association after adjusting for pre - fracture levels of frailty .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "pre - fracture", "type": "InjuryOrPoisoning"}, {"text": "frailty", "type": "Finding"}]}

Example input:
Sentence: Higher Prevalence of Frailty Among a Sample of HIV - Infected Middle - aged and Older Chinese Adults Is Associated With Neurocognitive Impairment and Depressive Symptoms We investigated the prevalence and correlates of prefrailty / frailty , determined on the basis of the Fried criteria , in Chinese patients with and those without human immunodeficiency virus ( HIV ) infection .

Example answer:
{"entities": [{"text": "Frailty", "type": "Finding"}, {"text": "HIV", "type": "Virus"}, {"text": "Infected", "type": "Finding"}, {"text": "Older Chinese", "type": "PopulationGroup"}, {"text": "Neurocognitive Impairment", "type": "BiologicFunction"}, {"text": "Depressive Symptoms", "type": "Finding"}, {"text": "prefrailty", "type": "Finding"}, {"text": "frailty", "type": "Finding"}, {"text": "Chinese", "type": "PopulationGroup"}, {"text": "human immunodeficiency virus ( HIV ) infection", "type": "BiologicFunction"}]}

Example input:
Sentence: Low calcium and vitamin D intake in Korean women over 50 years of age Inadequate calcium and vitamin D intake is a possible risk factor of osteoporosis .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "Korean", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "risk factor", "type": "Finding"}, {"text": "osteoporosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Spine fracture prevalence is similar in women and men and increases with age and lower BMD , although most subjects with spine fracture do not meet BMD criteria for osteoporosis .

Example answer:
{"entities": [{"text": "Spine fracture", "type": "InjuryOrPoisoning"}, {"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}, {"text": "BMD", "type": "ClinicalAttribute"}, {"text": "subjects", "type": "ResearchActivity"}, {"text": "spine fracture", "type": "InjuryOrPoisoning"}, {"text": "osteoporosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Age - adjusted hazard ratio ( HR ) of death for incident fracture was 3 .

Example answer:
{"entities": [{"text": "death", "type": "Finding"}, {"text": "fracture", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: While fractures reportedly increase the risk of mortality , frailty may complicate this association , generating a false - positive result .

Example answer:
{"entities": [{"text": "fractures", "type": "InjuryOrPoisoning"}, {"text": "frailty", "type": "Finding"}, {"text": "false - positive result", "type": "Finding"}]}

Example input:
Sentence: Incident clinical fracture was associated with an elevated risk of death independently of pre - fracture levels of frailty in community - dwelling elderly men .

Example answer:
{"entities": [{"text": "fracture", "type": "InjuryOrPoisoning"}, {"text": "death", "type": "Finding"}, {"text": "independently", "type": "Finding"}, {"text": "pre - fracture", "type": "InjuryOrPoisoning"}, {"text": "frailty", "type": "Finding"}, {"text": "elderly", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: We examined 1998 community - dwelling ambulatory men aged ≥65 years at baseline in the Fujiwara - kyo Osteoporosis Risk in Men Study for frailty status as represented by activities of daily living ( ADL ) , physical performance tests ( grip strength , one - foot standing balance with eyes open , timed 10 - m walk ) , and laboratory sera tests .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "men", "type": "PopulationGroup"}, {"text": "frailty", "type": "Finding"}, {"text": "physical performance tests", "type": "HealthCareActivity"}, {"text": "timed 10 - m walk", "type": "HealthCareActivity"}, {"text": "laboratory sera tests", "type": "HealthCareActivity"}]}

Example input:
Sentence: We found that incident fractures were associated with an increased risk of death even after adjusting for pre - fracture frailty status as represented by physical performance tests and laboratory tests for common geriatric diseases in community - dwelling elderly Japanese men .

Example answer:
{"entities": [{"text": "fractures", "type": "InjuryOrPoisoning"}, {"text": "death", "type": "Finding"}, {"text": "pre - fracture", "type": "InjuryOrPoisoning"}, {"text": "frailty", "type": "Finding"}, {"text": "physical performance tests", "type": "HealthCareActivity"}, {"text": "laboratory tests", "type": "HealthCareActivity"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "elderly", "type": "PopulationGroup"}, {"text": "Japanese", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}]}

Input:
Sentence: Incident fracture associated with increased risk of mortality even after adjusting for frailty status in elderly Japanese men : the Fujiwara - kyo Osteoporosis Risk in Men ( FORMEN ) Cohort Study Frail elderly individuals have elevated risks of both fracture and mortality .

## Item MedMentions:test:2180
Example input:
Sentence: Our findings show for the first time assembly of SGs and sequestration of COX - 2 mRNAs in human OA chondrocytes under pathological conditions .

Example answer:
{"entities": [{"text": "assembly of SGs", "type": "BiologicFunction"}, {"text": "COX - 2", "type": "AnatomicalStructure"}, {"text": "mRNAs", "type": "Chemical"}, {"text": "human", "type": "Eukaryote"}, {"text": "OA", "type": "BiologicFunction"}, {"text": "chondrocytes", "type": "AnatomicalStructure"}, {"text": "pathological conditions", "type": "Finding"}]}

Example input:
Sentence: The cofactors dependent properties of OcRhS1 were thus characterized in this research .

Example answer:
{"entities": [{"text": "cofactors", "type": "BiologicFunction"}, {"text": "OcRhS1", "type": "Chemical"}, {"text": "research", "type": "ResearchActivity"}]}

Example input:
Sentence: Biochemical evidences indicated that the recombinant OcRhS1 was active in the pH range of 5 - 11 and over the temperature range of 0 - 60 ° C .

Example answer:
{"entities": [{"text": "recombinant OcRhS1", "type": "Chemical"}]}

Example input:
Sentence: Moreover , the N - terminal portion of OcRhS1 ( OcRhS1 - N ) was observed to metabolize UDP - Glc to form intermediate UDP - 4K6DG .

Example answer:
{"entities": [{"text": "N - terminal portion of OcRhS1", "type": "Chemical"}, {"text": "OcRhS1 - N", "type": "Chemical"}, {"text": "UDP - Glc", "type": "Chemical"}]}

Example input:
Sentence: The OcRhS1 gene has an ORF ( open reading frame ) of 2019 bp encoding a tri - functional RhS enzyme .

Example answer:
{"entities": [{"text": "OcRhS1 gene", "type": "AnatomicalStructure"}, {"text": "ORF", "type": "AnatomicalStructure"}, {"text": "open reading frame", "type": "AnatomicalStructure"}, {"text": "tri - functional RhS enzyme", "type": "AnatomicalStructure"}]}

Example input:
Sentence: OcRhS1 is a multi - domain protein with two sets of cofactor - binding motifs .

Example answer:
{"entities": [{"text": "OcRhS1", "type": "Chemical"}, {"text": "multi - domain protein", "type": "Chemical"}, {"text": "cofactor - binding motifs", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , two genes encoding rhamnose synthase ( RhS ) and bi - functional UDP - 4 - keto - 6 - deoxy - D - glucose ( UDP - 4K6DG ) 3 , 5 - epimerase / UDP - 4 - keto - L - rhamnose ( UDP - 4KR ) 4 - keto - reductase ( UER ) were isolated from Ornithogalum caudatum based on the RNA - Seq data .

Example answer:
{"entities": [{"text": "genes", "type": "AnatomicalStructure"}, {"text": "rhamnose synthase", "type": "Chemical"}, {"text": "RhS", "type": "Chemical"}, {"text": "bi - functional", "type": "Chemical"}, {"text": "UDP - 4 - keto - 6 - deoxy - D - glucose", "type": "Chemical"}, {"text": "UDP - 4K6DG", "type": "Chemical"}, {"text": "3 , 5 - epimerase / UDP - 4 - keto - L - rhamnose", "type": "Chemical"}, {"text": "UDP - 4KR", "type": "Chemical"}, {"text": "4 - keto - reductase", "type": "Chemical"}, {"text": "UER", "type": "Chemical"}, {"text": "Ornithogalum caudatum", "type": "Eukaryote"}, {"text": "RNA", "type": "Chemical"}, {"text": "Seq data", "type": "IntellectualProduct"}]}

Example input:
Sentence: In vitro enzymatic assays revealed OcRhS1 can really convert UDP - D - glucose ( UDP - Glc ) into UDP - Rha via three consecutive reactions .

Example answer:
{"entities": [{"text": "enzymatic assays", "type": "HealthCareActivity"}, {"text": "OcRhS1", "type": "Chemical"}, {"text": "UDP - D - glucose", "type": "Chemical"}, {"text": "UDP - Glc", "type": "Chemical"}, {"text": "UDP - Rha", "type": "Chemical"}]}

Example input:
Sentence: OcUER1 shared high similarity with the carboxy - terminal domain of OcRhS1 ( OcRhS1 - C ) , suggesting its intrinsic ability of converting UDP - 4K6DG into UDP - Rha .

Example answer:
{"entities": [{"text": "OcUER1", "type": "Chemical"}, {"text": "carboxy - terminal domain of OcRhS1", "type": "Chemical"}, {"text": "OcRhS1 - C", "type": "Chemical"}, {"text": "UDP - Rha", "type": "Chemical"}]}

Example input:
Sentence: Functional analyses of OcRhS1 and OcUER1 involved in UDP - L - rhamnose biosynthesis in Ornithogalum caudatum UDP - L - rhamnose ( UDP - Rha ) is an important sugar donor for the synthesis of rhamnose -containing compounds in plants .

Example answer:
{"entities": [{"text": "Functional analyses", "type": "ResearchActivity"}, {"text": "OcRhS1", "type": "Chemical"}, {"text": "OcUER1", "type": "Chemical"}, {"text": "UDP - L - rhamnose", "type": "Chemical"}, {"text": "Ornithogalum caudatum", "type": "Eukaryote"}, {"text": "UDP - Rha", "type": "Chemical"}, {"text": "sugar donor", "type": "Chemical"}, {"text": "rhamnose", "type": "Chemical"}, {"text": "compounds", "type": "Chemical"}, {"text": "plants", "type": "Eukaryote"}]}

Input:
Sentence: Importantly , expression profiles of OcRhS1 and OcUER1 revealed their possible involvement in the biosynthesis of rhamnose -containing polysaccharides in O .

## Item MedMentions:test:2338
Example input:
Sentence: Microglia cells , as part of the brain 's innate immune system , are triggered by an inflammatory reaction in the microvasculature after eSAH , thus contributing to neuronal cell death .

Example answer:
{"entities": [{"text": "Microglia", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "brain 's", "type": "AnatomicalStructure"}, {"text": "inflammatory reaction", "type": "BiologicFunction"}, {"text": "microvasculature", "type": "BiologicFunction"}, {"text": "eSAH", "type": "BiologicFunction"}, {"text": "neuronal cell death", "type": "BiologicFunction"}]}

Example input:
Sentence: The present study examines the effects of peripherally administered β - FNA on lipopolysaccharide ( LPS ) - induced neuroinflammation and sickness behavior in vivo .

Example answer:
{"entities": [{"text": "peripherally", "type": "SpatialConcept"}, {"text": "administered", "type": "HealthCareActivity"}, {"text": "β - FNA", "type": "Chemical"}, {"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}]}

Example input:
Sentence: Cultures of primary mouse microglia or BV - 2 microglia cell line exposed to lipopolysaccharide ( LPS ) or interferon gamma ( IFNγ ) for different periods of time , in order to study the role of cPLA2α in the events leading to CD40 protein induction .

Example answer:
{"entities": [{"text": "Cultures", "type": "HealthCareActivity"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "microglia", "type": "AnatomicalStructure"}, {"text": "BV - 2 microglia cell line", "type": "AnatomicalStructure"}, {"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "interferon gamma", "type": "Chemical"}, {"text": "IFNγ", "type": "Chemical"}, {"text": "cPLA2α", "type": "Chemical"}, {"text": "CD40", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}]}

Example input:
Sentence: Microglia , the resident innate immune cells and sentinels in the brain , are a common source of neuroinflammation and are implicated in air pollution - induced CNS effects .

Example answer:
{"entities": [{"text": "Microglia", "type": "AnatomicalStructure"}, {"text": "immune cells", "type": "AnatomicalStructure"}, {"text": "sentinels", "type": "Chemical"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "source", "type": "Finding"}, {"text": "CNS effects", "type": "BiologicFunction"}]}

Example input:
Sentence: LPS also increased IL - 6 , TNF - α , malondialdehyde ( MDA ) and nitric oxide ( NO ) metabolites in the hippocampal tissues ( P < 0 .

Example answer:
{"entities": [{"text": "LPS", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "MDA", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "metabolites", "type": "Chemical"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Our findings indicate that CD169 ( + ) cells promote neuroinflammation .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "CD169 ( + )", "type": "Chemical"}, {"text": "neuroinflammation", "type": "BiologicFunction"}]}

Example input:
Sentence: Addition of LPS to microglia caused an immediate activation of cPLA2α detected by its phosphorylated form , while addition of IFNγ induced cPLA2α activation at a later time scale ( 4 h ) .

Example answer:
{"entities": [{"text": "LPS", "type": "Chemical"}, {"text": "microglia", "type": "AnatomicalStructure"}, {"text": "cPLA2α", "type": "Chemical"}, {"text": "phosphorylated", "type": "BiologicFunction"}, {"text": "IFNγ", "type": "Chemical"}]}

Example input:
Sentence: The bacterial lipopolysaccharide ( LPS ) was injected intravenously ( iv ) on TGFβ reporter mice ( Smad - binding element ( SBE ) / Tk - Luc ) to study in their brains the real - time activation profile of the TGFβ pathway in a non - invasive way .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "injected intravenously", "type": "HealthCareActivity"}, {"text": "TGFβ", "type": "Chemical"}, {"text": "reporter mice", "type": "Eukaryote"}, {"text": "Smad - binding element", "type": "Chemical"}, {"text": "SBE", "type": "Chemical"}, {"text": "study", "type": "ResearchActivity"}, {"text": "brains", "type": "AnatomicalStructure"}, {"text": "real - time activation profile", "type": "HealthCareActivity"}, {"text": "TGFβ pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: The results demonstrate proof of concept that NLRP3 inflammasome activation contributes to long - term behavioral alterations in LPS - exposed mice , probably through enhanced inflammation , and that NLRP3 inflammasome inhibition might alleviate peripheral and brain inflammation and thereby ameliorate long - term behavioral alterations in LPS - exposed mice .

Example answer:
{"entities": [{"text": "NLRP3 inflammasome activation", "type": "BiologicFunction"}, {"text": "LPS", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "NLRP3 inflammasome", "type": "AnatomicalStructure"}, {"text": "inhibition", "type": "BiologicFunction"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "brain", "type": "AnatomicalStructure"}]}

Example input:
Sentence: NLRP3 inflammasome activation contributes to long - term behavioral alterations in mice injected with lipopolysaccharide Lipopolysaccharide ( LPS ) might affect the central nervous system by causing neuroinflammation , which subsequently leads to brain damage and dysfunction .

Example answer:
{"entities": [{"text": "NLRP3 inflammasome activation", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "injected", "type": "HealthCareActivity"}, {"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "Lipopolysaccharide", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "central nervous system", "type": "BodySystem"}, {"text": "neuroinflammation", "type": "BiologicFunction"}, {"text": "brain damage", "type": "InjuryOrPoisoning"}, {"text": "dysfunction", "type": "BiologicFunction"}]}

Input:
Sentence: Additionally , some evidence has shown that some microbial products such as the bacterial lipopolysaccharide could lead to the activation of reactive immune cells , triggering neuroinflammation .

## Item MedMentions:test:2514
Example input:
Sentence: Neural progenitors in dentate gyrus of the hippocampus are known to undergo apoptosis after irradiation .

Example answer:
{"entities": [{"text": "Neural progenitors", "type": "AnatomicalStructure"}, {"text": "dentate gyrus", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Consequently , after radiation , tumor cells expressed less eNOS and Sp1 than controls .

Example answer:
{"entities": [{"text": "tumor cells", "type": "AnatomicalStructure"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "eNOS", "type": "Chemical"}, {"text": "Sp1", "type": "Chemical"}]}

Example input:
Sentence: At 6 months , post - irradiation progressive impairment in gait coordination ( including changes in the regularity index and phase dispersion ) was also evident .

Example answer:
{"entities": [{"text": "gait", "type": "Finding"}, {"text": "coordination", "type": "BiologicFunction"}, {"text": "index", "type": "IntellectualProduct"}, {"text": "dispersion", "type": "SpatialConcept"}]}

Example input:
Sentence: We found that mice with WBI exhibited impaired cerebromicrovascular function at 3 months post - irradiation , which was associated with impaired performance in the radial arm water maze .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: These results could have clinical implications as IR - induced DNA damage and the ensuing CAs and genomic instability can have significant cellular consequences that could potentially have profound implications for long - term human health after IR exposure , such as the emergence of secondary cancers and other pathobiological conditions after radiotherapy .

Example answer:
{"entities": [{"text": "IR - induced DNA damage", "type": "BiologicFunction"}, {"text": "CAs", "type": "BiologicFunction"}, {"text": "genomic instability", "type": "BiologicFunction"}, {"text": "cellular", "type": "AnatomicalStructure"}, {"text": "IR exposure", "type": "InjuryOrPoisoning"}, {"text": "secondary cancers", "type": "BiologicFunction"}, {"text": "radiotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: This review summarizes the epidemiological and biological data on radiation - induced brain damage and describes prevention and therapy methods to avoid and ameliorate these adverse effects , respectively .

Example answer:
{"entities": [{"text": "brain damage", "type": "InjuryOrPoisoning"}, {"text": "adverse effects", "type": "BiologicFunction"}]}

Example input:
Sentence: The primary outcome was the prospectively collected 2 - year cumulative incidence of severe late toxic effects ( Common Terminology Criteria for Adverse Events grade 3 or higher ) occurring 3 months or more after radiotherapy .

Example answer:
{"entities": [{"text": "late toxic effects", "type": "BiologicFunction"}, {"text": "Common Terminology Criteria for Adverse Events", "type": "IntellectualProduct"}, {"text": "grade 3", "type": "Finding"}, {"text": "radiotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Although the molecular mechanisms involved in radiation - induced brain injury remain elusive , first strategies for prevention and amelioration are being developed .

Example answer:
{"entities": [{"text": "brain injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Cerebromicrovascular dysfunction predicts cognitive decline and gait abnormalities in a mouse model of whole brain irradiation -induced accelerated brain senescence Whole brain irradiation ( WBI ) is a mainstream therapy for patients with both identifiable brain metastases and prophylaxis for microscopic malignancies .

Example answer:
{"entities": [{"text": "dysfunction", "type": "BiologicFunction"}, {"text": "cognitive decline", "type": "BiologicFunction"}, {"text": "gait abnormalities", "type": "Finding"}, {"text": "mouse model", "type": "BiologicFunction"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "senescence", "type": "BiologicFunction"}, {"text": "brain metastases", "type": "BiologicFunction"}, {"text": "prophylaxis", "type": "HealthCareActivity"}, {"text": "malignancies", "type": "BiologicFunction"}]}

Example input:
Sentence: However , it also promotes accelerated senescence in healthy tissues and leads to progressive cognitive dysfunction in up to 50 % of tumor patients surviving long term after treatment , due to γ - irradiation -induced cerebromicrovascular injury .

Example answer:
{"entities": [{"text": "senescence", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "cognitive dysfunction", "type": "BiologicFunction"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: Radiation - induced late effects may manifest as brain tumors or cognitive impairment .

## Item MedMentions:test:1950
Example input:
Sentence: Main exclusion criteria were established kidney disease , cardiovascular diseases , diabetes mellitus and a body mass index > 35 kg / m2 .

Example answer:
{"entities": [{"text": "kidney disease", "type": "BiologicFunction"}, {"text": "cardiovascular diseases", "type": "BiologicFunction"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "body mass index", "type": "ClinicalAttribute"}]}

Example input:
Sentence: By univariate analysis , blood pressure ( BP ) , heart rate , National Institutes of Health Stroke Scale ( NIHSS ) score , number of diffusion - positive lesion , count of red blood cell , high - density lipoprotein , and degree of stenosis differed significantly between the 2 groups .

Example answer:
{"entities": [{"text": "blood pressure", "type": "BiologicFunction"}, {"text": "BP", "type": "BiologicFunction"}, {"text": "heart rate", "type": "ClinicalAttribute"}, {"text": "National Institutes of Health Stroke Scale ( NIHSS ) score", "type": "Finding"}, {"text": "positive", "type": "Finding"}, {"text": "lesion", "type": "Finding"}, {"text": "count of red blood cell", "type": "HealthCareActivity"}, {"text": "high - density lipoprotein", "type": "Chemical"}]}

Example input:
Sentence: Associations between sex and 30 distinct biomarkers representative of 6 pathophysiological categories were evaluated using multivariable linear regression adjusting for age , race , traditional CVD risk factors , kidney function , insulin resistance , MRI and dual - energy x - ray absorptiometry measures of body composition and fat distribution , and left ventricular mass .

Example answer:
{"entities": [{"text": "biomarkers", "type": "ClinicalAttribute"}, {"text": "categories", "type": "IntellectualProduct"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "race", "type": "PopulationGroup"}, {"text": "CVD", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "kidney function", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "dual - energy x - ray absorptiometry", "type": "HealthCareActivity"}, {"text": "fat distribution", "type": "Finding"}, {"text": "left ventricular mass", "type": "Finding"}]}

Example input:
Sentence: Promoting daily physical activity may improve the HRQOL in patients on chronic hemodialysis , especially in women .

Example answer:
{"entities": [{"text": "chronic hemodialysis", "type": "HealthCareActivity"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Predictors were age , sex , blood type , calculated panel - reactive antibodies , donation service area , dialysis duration , comorbid conditions , and body mass index .

Example answer:
{"entities": [{"text": "Predictors", "type": "Finding"}, {"text": "blood type", "type": "ClinicalAttribute"}, {"text": "calculated", "type": "HealthCareActivity"}, {"text": "panel - reactive antibodies", "type": "HealthCareActivity"}, {"text": "donation", "type": "HealthCareActivity"}, {"text": "service area", "type": "SpatialConcept"}, {"text": "dialysis", "type": "HealthCareActivity"}, {"text": "comorbid conditions", "type": "Finding"}, {"text": "body mass index", "type": "ClinicalAttribute"}]}

Example input:
Sentence: A low plasma ghrelin level is associated with increased mortality in patients treated with hemodialysis ( HD ) .

Example answer:
{"entities": [{"text": "plasma", "type": "BodySubstance"}, {"text": "ghrelin", "type": "Chemical"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "hemodialysis", "type": "HealthCareActivity"}, {"text": "HD", "type": "HealthCareActivity"}]}

Example input:
Sentence: On investigating , patient 's renal parameters were high and he was started with haemodialysis .

Example answer:
{"entities": [{"text": "renal", "type": "AnatomicalStructure"}, {"text": "haemodialysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: In all patients , changes in EQ - 5D were weakly and negatively correlated with changes in physical activity ( 1 - 3 METs : min per day ) on hemodialysis days .

Example answer:
{"entities": [{"text": "EQ - 5D", "type": "IntellectualProduct"}, {"text": "negatively", "type": "Finding"}, {"text": "hemodialysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: Relationship between Changes in Physical Activity and Changes in Health - related Quality of Life in Patients on Chronic Hemodialysis with 1 - Year Follow - up In a longitudinal study , we examined the link between changes in physical activity and changes in health - related quality of life ( HRQOL ) in patients on chronic hemodialysis .

Example answer:
{"entities": [{"text": "Chronic Hemodialysis", "type": "HealthCareActivity"}, {"text": "1 - Year Follow - up", "type": "Finding"}, {"text": "longitudinal study", "type": "ResearchActivity"}, {"text": "examined", "type": "Finding"}, {"text": "chronic hemodialysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: The multivariable linear regression analysis showed no difference in serum HDL level between the two groups adjusted for sex , age , and time of dialysis , while the level of serum HDL - C could be adversely predicted by duration time .

Example answer:
{"entities": [{"text": "multivariable linear regression analysis", "type": "IntellectualProduct"}, {"text": "serum HDL level", "type": "HealthCareActivity"}, {"text": "dialysis", "type": "HealthCareActivity"}, {"text": "level of serum HDL - C", "type": "HealthCareActivity"}]}

Input:
Sentence: Clinical parameters including age , height , dry weight , duration of hemodialysis , blood pressure ( BP ) , blood triglyceride and HDL cholesterol levels , physical activity , and HRQOL were evaluated .

## Item MedMentions:test:2565
Example input:
Sentence: Despite catch - up growth , VP - / VLBW + infants remained the shortest and lightest at age 19 .

Example answer:
{"entities": [{"text": "catch - up growth", "type": "BiologicFunction"}, {"text": "lightest", "type": "Finding"}]}

Example input:
Sentence: Gore - Tex ® or a Marlex ™ mesh and methyl methacrylate sandwich was used in 22 patients , and 9 children did not require reconstruction .

Example answer:
{"entities": [{"text": "Gore - Tex", "type": "Chemical"}, {"text": "Marlex ™ mesh", "type": "Chemical"}, {"text": "methyl methacrylate sandwich", "type": "Chemical"}]}

Example input:
Sentence: Western blotting analysis demonstrated that the inhibitory effect of STX - 0119 on S6 and 4E - BP1 activation through regulation of YKL - 40 expression occurred in addition to the inhibitory effect of rapamycin against the mTOR pathway .

Example answer:
{"entities": [{"text": "Western blotting analysis", "type": "HealthCareActivity"}, {"text": "inhibitory effect", "type": "BiologicFunction"}, {"text": "STX - 0119", "type": "Chemical"}, {"text": "S6", "type": "Chemical"}, {"text": "4E - BP1", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "YKL - 40", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "rapamycin", "type": "Chemical"}, {"text": "mTOR pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study we optimized the selection of radiolabel - chelator complex to improve tumor uptake and tumor -to - background contrast of radiolabeled analogues of B9958 ( Lys - Lys - Arg - Pro - Hyp - Gly - Cpg - Ser - d - Tic - Cpg ) , a potent B1R antagonist .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "chelator", "type": "Chemical"}, {"text": "complex", "type": "Chemical"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "uptake", "type": "BiologicFunction"}, {"text": "B9958", "type": "Chemical"}, {"text": "B1R antagonist", "type": "Chemical"}]}

Example input:
Sentence: A bleomycin , etoposide , and cisplatin treatment protocol targeting germ cell neoplasia lead to disease remission and prolonged survival of 34 months .

Example answer:
{"entities": [{"text": "bleomycin", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "treatment protocol", "type": "HealthCareActivity"}, {"text": "germ cell neoplasia", "type": "BiologicFunction"}, {"text": "disease remission", "type": "Finding"}]}

Example input:
Sentence: In this prospective study , 40 patients with a BMI < 28 . 0 kg / m ( 2 ) underwent CTA examination for breast reconstruction and were randomly assigned into two groups ( n = 20 for each group ) as follows : Group A was submitted to dual - energy spectral CT and iodixanol ( 270 mg I / mL ) and Group B was submitted to conventional high iodine contrast agent iohexol ( 350 mg I / mL ) .

Example answer:
{"entities": [{"text": "prospective study", "type": "ResearchActivity"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "CTA", "type": "HealthCareActivity"}, {"text": "breast reconstruction", "type": "Finding"}, {"text": "dual - energy spectral CT", "type": "HealthCareActivity"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "iodine contrast agent", "type": "Chemical"}, {"text": "iohexol", "type": "Chemical"}]}

Example input:
Sentence: Patients with T - shaped LAD - LCX BA was shown to have significantly longer LMCA , larger LAD ostial area , larger LCX ostial area and higher diastolic - to - systolic range ( DSR ) of LAD - LCX BA compared to patients with Y - shaped LAD - LCX BA .

Example answer:
{"entities": [{"text": "LAD", "type": "AnatomicalStructure"}, {"text": "LCX", "type": "AnatomicalStructure"}, {"text": "LMCA", "type": "AnatomicalStructure"}, {"text": "LAD ostial", "type": "AnatomicalStructure"}, {"text": "area", "type": "SpatialConcept"}, {"text": "ostial", "type": "SpatialConcept"}]}

Example input:
Sentence: coli BL21 .

Example answer:
{"entities": [{"text": "coli BL21", "type": "Bacterium"}]}

Example input:
Sentence: The isolates were subjected to molecular techniques to detect blaOXA , blaTEM , blaCTX - M , and blaSHV genes in strains of the A .

Example answer:
{"entities": [{"text": "isolates", "type": "Chemical"}, {"text": "molecular techniques", "type": "ResearchActivity"}, {"text": "blaOXA , blaTEM , blaCTX - M , and blaSHV genes", "type": "AnatomicalStructure"}, {"text": "strains", "type": "Bacterium"}, {"text": "A .", "type": "Bacterium"}]}

Example input:
Sentence: PCR results showed that blaOXA , blaTEM , and blaCTX - M genes were positive in some isolates , while blaSHV was not detected in any of the isolates .

Example answer:
{"entities": [{"text": "PCR", "type": "ResearchActivity"}, {"text": "results", "type": "Finding"}, {"text": "blaOXA , blaTEM , and blaCTX - M genes", "type": "AnatomicalStructure"}, {"text": "positive", "type": "Finding"}, {"text": "isolates", "type": "Chemical"}, {"text": "blaSHV", "type": "AnatomicalStructure"}, {"text": "not detected", "type": "Finding"}]}

Input:
Sentence: BlaCTX - M ( 21 .

## Item MedMentions:test:2271
Example input:
Sentence: coli isolates ( 53 from diarrheic herds and 17 from healthy herds ) were examined by PCR for detection of the virulence genes associated with pathogenic E .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "diarrheic", "type": "Finding"}, {"text": "PCR", "type": "ResearchActivity"}, {"text": "virulence", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "E .", "type": "Bacterium"}]}

Example input:
Sentence: Use of single molecule sequencing for comparative genomics of an environmental and a clinical isolate of Clostridium difficile ribotype 078 How the pathogen Clostridium difficile might survive , evolve and be transferred between reservoirs within the natural environment is poorly understood .

Example answer:
{"entities": [{"text": "genomics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "environmental", "type": "SpatialConcept"}, {"text": "isolate", "type": "Chemical"}, {"text": "Clostridium difficile", "type": "Bacterium"}, {"text": "ribotype 078", "type": "Finding"}, {"text": "reservoirs", "type": "SpatialConcept"}, {"text": "natural environment", "type": "SpatialConcept"}]}

Example input:
Sentence: A significant reduction ( p < 0 , 001 - 0 , 02 ) in susceptibility for the strains after 2009 was noted towards piperacillin ( 100 % vs 50 % ) , ceftazidime ( 100 % / 77 . 3 % ) , cefepime ( 97 . 9 % / 68 . 2 % ) , amikacin ( 100 % / 63 .

Example answer:
{"entities": [{"text": "piperacillin", "type": "Chemical"}, {"text": "ceftazidime", "type": "Chemical"}, {"text": "cefepime", "type": "Chemical"}, {"text": "amikacin", "type": "Chemical"}]}

Example input:
Sentence: A significantly greater frequency of the f17 gene was observed in individual camels and in herds with diarrhea , this gene being found in 44 . 7 % and 41 . 5 % of isolates from camels and herds with diarrhea versus 22 . 5 % and 11 .

Example answer:
{"entities": [{"text": "f17 gene", "type": "AnatomicalStructure"}, {"text": "camels", "type": "Eukaryote"}, {"text": "diarrhea", "type": "Finding"}, {"text": "gene", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The susceptibility rates of the VGS strains for levofloxacin , cefepime , piperacillin / tazobactam , meropenem , and vancomycin were 0 % , 95 % , 100 % , 100 % , and 100 % , respectively .

Example answer:
{"entities": [{"text": "susceptibility", "type": "BiologicFunction"}, {"text": "VGS", "type": "Bacterium"}, {"text": "levofloxacin", "type": "Chemical"}, {"text": "cefepime", "type": "Chemical"}, {"text": "piperacillin / tazobactam", "type": "Chemical"}, {"text": "meropenem", "type": "Chemical"}, {"text": "vancomycin", "type": "Chemical"}]}

Example input:
Sentence: Prevalence of afa8 , cdtB , eae , east1 , iroN , iss , kpsMTII , paa , sfa , tsh and papC genes did not differ significantly between herds with or without diarrhea .

Example answer:
{"entities": [{"text": "afa8", "type": "AnatomicalStructure"}, {"text": "cdtB", "type": "AnatomicalStructure"}, {"text": "east1", "type": "AnatomicalStructure"}, {"text": "iroN", "type": "AnatomicalStructure"}, {"text": "iss", "type": "AnatomicalStructure"}, {"text": "kpsMTII", "type": "AnatomicalStructure"}, {"text": "paa", "type": "AnatomicalStructure"}, {"text": "sfa", "type": "AnatomicalStructure"}, {"text": "tsh", "type": "AnatomicalStructure"}, {"text": "papC", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "diarrhea", "type": "Finding"}]}

Example input:
Sentence: In the Spanish cohort , dysbiosis was found significantly greater in patients with CD than with UC , as shown by a more reduced diversity , a less stable microbial community and eight microbial groups were proposed as a specific microbial signature for CD .

Example answer:
{"entities": [{"text": "Spanish", "type": "PopulationGroup"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "dysbiosis", "type": "BiologicFunction"}, {"text": "CD", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}]}

Example input:
Sentence: Predominance of Clostridium difficile Ribotypes 017 and 078 among Toxigenic Clinical Isolates in Southern Taiwan Ribotypes and toxin genotypes of clinical C .

Example answer:
{"entities": [{"text": "Clostridium difficile", "type": "Bacterium"}, {"text": "Ribotypes 017", "type": "Finding"}, {"text": "078", "type": "Finding"}, {"text": "Toxigenic", "type": "Chemical"}, {"text": "Clinical Isolates", "type": "Chemical"}, {"text": "Southern", "type": "SpatialConcept"}, {"text": "Taiwan", "type": "SpatialConcept"}, {"text": "Ribotypes", "type": "Finding"}, {"text": "toxin", "type": "Chemical"}, {"text": "C .", "type": "Bacterium"}]}

Example input:
Sentence: difficile isolates with binary toxin , the ribotype 078 family was predominant .

Example answer:
{"entities": [{"text": "difficile", "type": "Bacterium"}, {"text": "isolates", "type": "Chemical"}, {"text": "binary toxin", "type": "Chemical"}, {"text": "ribotype 078", "type": "Finding"}]}

Example input:
Sentence: difficile isolates in Taiwan are rarely reported .

Example answer:
{"entities": [{"text": "difficile", "type": "Bacterium"}, {"text": "isolates", "type": "Chemical"}, {"text": "Taiwan", "type": "SpatialConcept"}]}

Input:
Sentence: difficile isolates , these isolates from 6 ( 75 % ) patients were identical , irrespective of the presence or absence of diarrhea , suggestive of persistent fecal carriage or colonization .

## Item MedMentions:test:2361
Example input:
Sentence: Genotypes in all the analyzed polymorphisms preserved the Hardy - Weinberg equilibrium in pregnant women , both infected and uninfected with HCMV ( P > 0 . 050 ) .

Example answer:
{"entities": [{"text": "analyzed polymorphisms", "type": "BiologicFunction"}, {"text": "pregnant women", "type": "PopulationGroup"}, {"text": "infected", "type": "Finding"}, {"text": "HCMV", "type": "Virus"}]}

Example input:
Sentence: G G homozygotic and G A heterozygotic status in TLR9 2848 G > A SNP decreased significantly the occurrence of HCMV infection ( OR 0 .

Example answer:
{"entities": [{"text": "G", "type": "Chemical"}, {"text": "A", "type": "Chemical"}, {"text": "TLR9", "type": "AnatomicalStructure"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "HCMV infection", "type": "BiologicFunction"}]}

Example input:
Sentence: To this end , we analyzed stool samples from six stage 4 - HCV patients and eight healthy individuals by high - throughput 16S rRNA gene sequencing using Illumina MiSeq .

Example answer:
{"entities": [{"text": "stool samples", "type": "BodySubstance"}, {"text": "HCV", "type": "Virus"}, {"text": "healthy individuals", "type": "PopulationGroup"}, {"text": "16S rRNA gene sequencing", "type": "HealthCareActivity"}, {"text": "Illumina MiSeq", "type": "MedicalDevice"}]}

Example input:
Sentence: The results also showed that HCV has a GC ( guanine - cytosine ) abundant genome structure and prefers codons with GC for translation .

Example answer:
{"entities": [{"text": "HCV", "type": "Virus"}, {"text": "GC", "type": "Chemical"}, {"text": "guanine - cytosine", "type": "Chemical"}, {"text": "genome structure", "type": "AnatomicalStructure"}, {"text": "codons", "type": "SpatialConcept"}]}

Example input:
Sentence: The purpose of this study was to phylogenetically investigate the differences between the genotypes of HCV , and to determine the types of amino acid codon usage in the structure of the virus in order to discover new methods for treatment regimes .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "phylogenetically investigate", "type": "ResearchActivity"}, {"text": "HCV", "type": "Virus"}, {"text": "amino acid", "type": "Chemical"}, {"text": "codon", "type": "SpatialConcept"}, {"text": "structure of the virus", "type": "AnatomicalStructure"}, {"text": "treatment regimes", "type": "HealthCareActivity"}]}

Example input:
Sentence: A relationship between the genotypes , alleles , haplotypes and multiple variants in the studied polymorphisms , and the occurrence of HCMV infection in pregnant women and their offsprings , was determined , using a logistic regression model .

Example answer:
{"entities": [{"text": "alleles", "type": "AnatomicalStructure"}, {"text": "multiple variants", "type": "AnatomicalStructure"}, {"text": "HCMV infection", "type": "BiologicFunction"}, {"text": "pregnant women", "type": "PopulationGroup"}]}

Example input:
Sentence: The codon usage of the six genotypes of the HCV nucleotide sequence was investigated through the online application available on the website Gene Infinity .

Example answer:
{"entities": [{"text": "codon", "type": "SpatialConcept"}, {"text": "HCV", "type": "Virus"}, {"text": "nucleotide sequence", "type": "SpatialConcept"}, {"text": "website Gene Infinity", "type": "IntellectualProduct"}]}

Example input:
Sentence: Genus -level analysis showed differential abundance of Prevotella and Faecalibacterium ( higher in HCV patients ) vs .

Example answer:
{"entities": [{"text": "Genus", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "Prevotella", "type": "Bacterium"}, {"text": "Faecalibacterium", "type": "Bacterium"}, {"text": "HCV", "type": "Virus"}]}

Example input:
Sentence: The six genotypes of HCV were divided into two groups based on their codon usage properties .

Example answer:
{"entities": [{"text": "HCV", "type": "Virus"}, {"text": "codon", "type": "SpatialConcept"}]}

Example input:
Sentence: Bioinformatic Analysis of Codon Usage and Phylogenetic Relationships in Different Genotypes of the Hepatitis C Virus The hepatitis C virus ( HCV ) has six major genotypes .

Example answer:
{"entities": [{"text": "Bioinformatic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Analysis", "type": "ResearchActivity"}, {"text": "Codon", "type": "SpatialConcept"}, {"text": "Hepatitis C Virus", "type": "Virus"}, {"text": "hepatitis C virus", "type": "Virus"}, {"text": "HCV", "type": "Virus"}]}

Input:
Sentence: Also , phylogenetic analysis and the evolutionary relationship of HCV genotypes were analyzed with MEGA 7 software .

## Item MedMentions:test:2333
Example input:
Sentence: The submodel of the hematoma is fully coupled with the aortic submodel as well as with the submodel of the pulsatile blood flow .

Example answer:
{"entities": [{"text": "hematoma", "type": "BiologicFunction"}]}

Example input:
Sentence: The tumor had rapidly grown to 50 cm and caused abnormalities in the hematological and coagulative systems .

Example answer:
{"entities": [{"text": "tumor", "type": "BiologicFunction"}, {"text": "abnormalities", "type": "Finding"}, {"text": "hematological", "type": "BodySystem"}, {"text": "coagulative", "type": "BiologicFunction"}]}

Example input:
Sentence: Recently , some investigations imply that simvastatin has the ability of accelerating hematoma absorption .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "hematoma", "type": "BiologicFunction"}]}

Example input:
Sentence: Multi - component model of intramural hematoma A novel multi - component model is introduced for studying interaction between blood flow and deforming aortic wall with intramural hematoma ( IMH ) .

Example answer:
{"entities": [{"text": "intramural hematoma", "type": "BiologicFunction"}, {"text": "studying", "type": "ResearchActivity"}, {"text": "blood flow", "type": "BiologicFunction"}, {"text": "deforming", "type": "Finding"}, {"text": "aortic wall", "type": "AnatomicalStructure"}, {"text": "IMH", "type": "BiologicFunction"}]}

Example input:
Sentence: All hematological and coagulative abnormalities had returned to normal after the procedure .

Example answer:
{"entities": [{"text": "hematological", "type": "BodySystem"}, {"text": "coagulative", "type": "BiologicFunction"}, {"text": "abnormalities", "type": "Finding"}, {"text": "procedure", "type": "HealthCareActivity"}]}

Example input:
Sentence: Heme was able of inducing ex vivo coagulation activation in whole blood , affecting predominantly parameters associated with the initial phases of clot formation .

Example answer:
{"entities": [{"text": "Heme", "type": "Chemical"}, {"text": "coagulation", "type": "BiologicFunction"}, {"text": "whole blood", "type": "BodySubstance"}, {"text": "clot formation", "type": "BiologicFunction"}]}

Example input:
Sentence: In altered hemodynamic conditions of critically ill patients , hemorheological variables may play a significant role in appropriate tissue perfusion .

Example answer:
{"entities": [{"text": "hemodynamic", "type": "BiologicFunction"}, {"text": "critically ill", "type": "BiologicFunction"}, {"text": "hemorheological", "type": "BiologicFunction"}, {"text": "variables", "type": "HealthCareActivity"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "perfusion", "type": "HealthCareActivity"}]}

Example input:
Sentence: Whole blood viscosity ( WBV ) and red blood cell ( RBC ) deformability were lower , red blood cell aggregation was higher in septic than in nonseptic patients ( p < 0 .

Example answer:
{"entities": [{"text": "Whole blood viscosity", "type": "Finding"}, {"text": "WBV", "type": "Finding"}, {"text": "red blood cell ( RBC ) deformability", "type": "BiologicFunction"}, {"text": "red blood cell", "type": "AnatomicalStructure"}, {"text": "aggregation", "type": "BiologicFunction"}]}

Example input:
Sentence: Model simulations are used to investigate the relation between the peak wall stress , hematoma thickness and permeability in patients of different age .

Example answer:
{"entities": [{"text": "Model simulations", "type": "ResearchActivity"}, {"text": "hematoma", "type": "BiologicFunction"}]}

Example input:
Sentence: The results indicate that an increase in hematoma thickness leads to larger wall stress , which is in agreement with clinical data .

Example answer:
{"entities": [{"text": "hematoma", "type": "BiologicFunction"}, {"text": "wall stress", "type": "Finding"}, {"text": "clinical data", "type": "IntellectualProduct"}]}

Input:
Sentence: Further simulations demonstrate that a hematoma with smaller permeability results in larger wall stress , suggesting that blood coagulation in hematoma might increase its mechanical stability .

## Item MedMentions:test:2424
Example input:
Sentence: Is there evidence for a close connection between side of intravesical tumor location and ipsilateral lymphatic spread in lymph node - positive bladder cancer patients at radical cystectomy ?

Example answer:
{"entities": [{"text": "intravesical tumor", "type": "BiologicFunction"}, {"text": "location", "type": "SpatialConcept"}, {"text": "ipsilateral", "type": "SpatialConcept"}, {"text": "lymphatic", "type": "BodySystem"}, {"text": "spread", "type": "Finding"}, {"text": "lymph node - positive", "type": "Finding"}, {"text": "bladder cancer", "type": "BiologicFunction"}, {"text": "radical cystectomy", "type": "HealthCareActivity"}]}

Example input:
Sentence: 29 . 2 % ( 40 / 137 ) patients were identified as ITC / LNMM positive and most of them ( 32 / 40 cases , 80 % ) showed high TBL1XR1 expression in primary CRC tissues .

Example answer:
{"entities": [{"text": "ITC", "type": "Finding"}, {"text": "LNMM", "type": "BiologicFunction"}, {"text": "positive", "type": "Finding"}, {"text": "TBL1XR1", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "CRC", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Our prospective cohort showed a concordance of tumor location and laterality of LN metastasis in BC at RC without any predictive criteria and without any influence on CSM .

Example answer:
{"entities": [{"text": "prospective cohort", "type": "ResearchActivity"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "location", "type": "SpatialConcept"}, {"text": "LN", "type": "AnatomicalStructure"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "BC", "type": "BiologicFunction"}, {"text": "RC", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients with PTC , with the primary tumor located in the upper part of the lobe and positive central compartment lymph node metastasis with a tumor size > 1 . 5 cm diameter are more likely to have LLNM .

Example answer:
{"entities": [{"text": "PTC", "type": "BiologicFunction"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "located", "type": "SpatialConcept"}, {"text": "lobe", "type": "AnatomicalStructure"}, {"text": "positive", "type": "Finding"}, {"text": "lymph node metastasis", "type": "BiologicFunction"}, {"text": "tumor size", "type": "SpatialConcept"}, {"text": "LLNM", "type": "BiologicFunction"}]}

Example input:
Sentence: 6 % were luminal B , 5 % were HER2 positive and 5 % were triple negative tumors .

Example answer:
{"entities": [{"text": "luminal B", "type": "BiologicFunction"}, {"text": "HER2 positive", "type": "BiologicFunction"}, {"text": "triple negative", "type": "Finding"}, {"text": "tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: Using multivariate Cox regression analyses ( median follow - up : 25 months ) , the effect of the laterality of positive LN on cancer - specific mortality ( CSM ) was estimated .

Example answer:
{"entities": [{"text": "multivariate Cox regression analyses", "type": "IntellectualProduct"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "positive LN", "type": "Finding"}]}

Example input:
Sentence: Of the 36 patients who had positive LNs at the final pathology , 22 were in the EPLND group and 14 in the SPLND group ( p < 0 . 01 ) .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "LNs", "type": "AnatomicalStructure"}, {"text": "pathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "EPLND", "type": "HealthCareActivity"}, {"text": "SPLND", "type": "HealthCareActivity"}]}

Example input:
Sentence: CSM after 3 years in patients with ipsilateral , contralateral , and bilateral LN metastasis was 41 , 67 , and 100 % , respectively ( p = 0 . 042 ) .

Example answer:
{"entities": [{"text": "ipsilateral", "type": "SpatialConcept"}, {"text": "bilateral", "type": "SpatialConcept"}, {"text": "LN", "type": "AnatomicalStructure"}, {"text": "metastasis", "type": "BiologicFunction"}]}

Example input:
Sentence: There was concordance of tumor location and laterality of positive LN in 82 % [ 95 % confidence interval ( CI ) , 76 - 89 ] .

Example answer:
{"entities": [{"text": "tumor", "type": "BiologicFunction"}, {"text": "location", "type": "SpatialConcept"}, {"text": "positive LN", "type": "Finding"}]}

Example input:
Sentence: No criteria were found to predict ipsilateral positive LN in patients with unilateral tumors .

Example answer:
{"entities": [{"text": "ipsilateral", "type": "SpatialConcept"}, {"text": "positive LN", "type": "Finding"}, {"text": "unilateral", "type": "SpatialConcept"}, {"text": "tumors", "type": "BiologicFunction"}]}

Input:
Sentence: Patients with unilateral tumors ( n = 78 ) harbored exclusively ipsilateral positive LN in 67 % ( 95 % CI 56 - 77 ) .

## Item MedMentions:test:2540
Example input:
Sentence: Forty - two recorded continuing care counseling sessions of 33 people who discussed HIV sex - risk behavior were transcribed and analyzed using thematic analysis .

Example answer:
{"entities": [{"text": "counseling sessions", "type": "HealthCareActivity"}, {"text": "people", "type": "PopulationGroup"}, {"text": "HIV", "type": "BiologicFunction"}, {"text": "thematic analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: In multivariate linear regression models , HIV risk status was significantly associated with increased blood cadmium , lead , and total mercury after adjusting for age , sex , race , education , and poverty income ratio .

Example answer:
{"entities": [{"text": "blood cadmium", "type": "HealthCareActivity"}, {"text": "lead", "type": "HealthCareActivity"}, {"text": "total mercury", "type": "HealthCareActivity"}, {"text": "race", "type": "PopulationGroup"}]}

Example input:
Sentence: Rates and predictors of injury in a population - based cohort of people living with HIV Injuries are responsible for 10 % of the global burden of disease ; however , the epidemiology of injury among people living with HIV ( PLHIV ) has not been well elucidated .

Example answer:
{"entities": [{"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "people", "type": "PopulationGroup"}, {"text": "HIV", "type": "BiologicFunction"}, {"text": "Injuries", "type": "InjuryOrPoisoning"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "people living with HIV", "type": "BiologicFunction"}, {"text": "PLHIV", "type": "BiologicFunction"}]}

Example input:
Sentence: Bivariate and multivariate analyses were done to identify independent predictors of provider -initiated HIV testing and counseling refusal by OPD clients .

Example answer:
{"entities": [{"text": "HIV testing", "type": "HealthCareActivity"}, {"text": "counseling", "type": "HealthCareActivity"}, {"text": "OPD", "type": "Organization"}]}

Example input:
Sentence: There were also higher infection rates among patients undergoing relatively high - complexity arthroscopies , men , obese patients , diabetic patients , and younger patients ( in order of decreasing relative risk ) .

Example answer:
{"entities": [{"text": "infection rates", "type": "BiologicFunction"}, {"text": "high - complexity arthroscopies", "type": "HealthCareActivity"}, {"text": "men", "type": "PopulationGroup"}, {"text": "obese", "type": "BiologicFunction"}, {"text": "diabetic", "type": "BiologicFunction"}]}

Example input:
Sentence: Incidence density rate ratios ( IDRR ) of testing were calculated , and generalized estimating equations were used to analyze the association between HIV testing and behavioral factors .

Example answer:
{"entities": [{"text": "generalized", "type": "SpatialConcept"}, {"text": "HIV testing", "type": "HealthCareActivity"}]}

Example input:
Sentence: HIV - infected patients were more likely to be frail or prefrail than controls , and this association remained significant after adjustment for potential confounders ( odds ratio , 3 . 79 ) .

Example answer:
{"entities": [{"text": "HIV", "type": "Virus"}, {"text": "infected", "type": "Finding"}, {"text": "frail", "type": "Finding"}, {"text": "prefrail", "type": "Finding"}]}

Example input:
Sentence: Study participants who had stigmatizing attitude [ AOR = 6 . 09 , ( 95 % CI : 1 . 70 , 21 . 76 ) ] , who had perceived risk for HIV infection [ AOR = 5 . 23 , ( 95 % CI : 2 . 22 , 12 . 32 ) ] , who did not perceive the benefits of provider -initiated HIV testing and counseling [ AOR = 4 . 64 , ( 95 % CI : 1 . 79 , 12 . 01 ) ] , who did not get minimum recommended pretest information from their providers [ AOR = 2 . 98 , ( 95 % CI : 1 . 06 , 8 . 35 ) ] , who ever not heard of provider -initiated HIV testing and counseling service [ AOR = 2 . 41 , ( 95 % CI : 1 . 14 , 5 . 09 ) ] , and who were from urban area [ AOR = 2 . 40 , ( 95 % CI = 1 . 26 , 4 . 57 ) ] were more likely to refuse provider -initiated HIV testing and counseling service than their counterparts .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "attitude", "type": "BiologicFunction"}, {"text": "HIV infection", "type": "BiologicFunction"}, {"text": "HIV testing", "type": "HealthCareActivity"}, {"text": "counseling", "type": "HealthCareActivity"}, {"text": "counseling service", "type": "HealthCareActivity"}]}

Example input:
Sentence: " Predictors of provider - initiated HIV testing and counseling refusal by outpatient department clients in Wolaita zone , Southern Ethiopia : a case control study " " Despite different strategies designed to rapidly identify HIV infected individuals , majority of HIV -infected people are unaware of their sero - status in developing countries .

Example answer:
{"entities": [{"text": "HIV testing", "type": "HealthCareActivity"}, {"text": "counseling", "type": "HealthCareActivity"}, {"text": "outpatient department", "type": "Organization"}, {"text": "case control study", "type": "ResearchActivity"}, {"text": "HIV infected", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "HIV -infected", "type": "BiologicFunction"}, {"text": "people", "type": "PopulationGroup"}, {"text": "sero - status", "type": "IntellectualProduct"}]}

Example input:
Sentence: Increasing availability of HIV testing outside traditional health care settings , including at - home testing kits , in conjunction with targeted behavioral interventions and biomedical treatment preventions is needed .

Example answer:
{"entities": [{"text": "HIV testing", "type": "HealthCareActivity"}, {"text": "outside", "type": "SpatialConcept"}, {"text": "health care settings", "type": "HealthCareActivity"}, {"text": "biomedical", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "treatment preventions", "type": "HealthCareActivity"}]}

Input:
Sentence: Few studies have identified risk factors associated with HIV testing frequency both within and outside of traditional health care settings .
