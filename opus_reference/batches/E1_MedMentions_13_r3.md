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

## Item MedMentions:test:2627
Example input:
Sentence: Gut microbiota after Roux - en - Y gastric bypass and sleeve gastrectomy in a diabetic rat model : Increased diversity and associations of discriminant genera with metabolic changes Recent work with gut microbiota after bariatric surgery is limited , and the results have not been in agreement .

Example answer:
{"entities": [{"text": "Roux - en - Y gastric bypass", "type": "HealthCareActivity"}, {"text": "sleeve gastrectomy", "type": "HealthCareActivity"}, {"text": "diabetic", "type": "BiologicFunction"}, {"text": "rat", "type": "Eukaryote"}, {"text": "model", "type": "BiologicFunction"}, {"text": "genera", "type": "IntellectualProduct"}, {"text": "metabolic", "type": "BiologicFunction"}, {"text": "bariatric surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , in our study , surgery did not achieve the expected outcome in patients with specific metabolic , anthropometric and surgical characteristics ( BMI > 50 Kg / m2 , presence of metabolic syndrome , presence of T2DM with high preoperative HbA1c % level and gastric pouch volume greater than 60 ml ) .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "expected", "type": "IntellectualProduct"}, {"text": "surgical", "type": "HealthCareActivity"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "metabolic syndrome", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "gastric pouch", "type": "AnatomicalStructure"}]}

Example input:
Sentence: HMGB1 inhibition by ethyl pyruvate or blockade by neutralizing antibodies significantly decreased the phosphorylation of STAT3 , p38 and IκBα , the production of IL - 1β and TNF - α , and the islet injury in wild - type islets after exposure to H / R and significantly improved early islet graft failure .

Example answer:
{"entities": [{"text": "HMGB1", "type": "Chemical"}, {"text": "ethyl pyruvate", "type": "Chemical"}, {"text": "antibodies", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "STAT3", "type": "Chemical"}, {"text": "p38", "type": "Chemical"}, {"text": "IκBα", "type": "Chemical"}, {"text": "production", "type": "BiologicFunction"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "islet", "type": "AnatomicalStructure"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "islets", "type": "AnatomicalStructure"}, {"text": "H", "type": "BiologicFunction"}, {"text": "R", "type": "HealthCareActivity"}, {"text": "graft failure", "type": "BiologicFunction"}]}

Example input:
Sentence: Thus , our results suggest that HMGB1 released from H / R induced islets works in an autocrine manner to up - regulate STAT or p38 and augment IL - 1β production via TLR2 , and up - regulate NF - κB and augment TNF - α production via TLR4 in intra - islet , which are associated with H / R -induced islet injury and early graft failure .

Example answer:
{"entities": [{"text": "HMGB1", "type": "Chemical"}, {"text": "H", "type": "BiologicFunction"}, {"text": "R", "type": "HealthCareActivity"}, {"text": "islets", "type": "AnatomicalStructure"}, {"text": "up - regulate", "type": "BiologicFunction"}, {"text": "STAT", "type": "Chemical"}, {"text": "p38", "type": "Chemical"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "production", "type": "BiologicFunction"}, {"text": "TLR2", "type": "Chemical"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "TLR4", "type": "Chemical"}, {"text": "intra - islet", "type": "AnatomicalStructure"}, {"text": "islet", "type": "AnatomicalStructure"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "graft failure", "type": "BiologicFunction"}]}

Example input:
Sentence: However , patients in the POST implementation group were more likely to exhibit hypoglycaemia .

Example answer:
{"entities": [{"text": "hypoglycaemia", "type": "BiologicFunction"}]}

Example input:
Sentence: Targeting postprandial blood sugar over fasting blood sugar : A clinic based comparative study Recent studies indicate that modulation of post prandial blood sugar ( PPBS ) plays an important role in the long term glycemic control .

Example answer:
{"entities": [{"text": "postprandial blood sugar", "type": "HealthCareActivity"}, {"text": "fasting blood sugar", "type": "HealthCareActivity"}, {"text": "clinic based comparative study", "type": "ResearchActivity"}, {"text": "post prandial blood sugar", "type": "BiologicFunction"}, {"text": "PPBS", "type": "BiologicFunction"}, {"text": "glycemic control", "type": "HealthCareActivity"}]}

Example input:
Sentence: We conducted a double - blinded crossover study wherein eight participants with confirmed PBH were assigned in random order to intravenous infusion of the GLP - 1 receptor ( GLP - 1r ) antagonist .

Example answer:
{"entities": [{"text": "double - blinded", "type": "ResearchActivity"}, {"text": "crossover study", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "PBH", "type": "BiologicFunction"}, {"text": "intravenous infusion", "type": "HealthCareActivity"}, {"text": "GLP - 1 receptor", "type": "Chemical"}, {"text": "GLP - 1r", "type": "Chemical"}, {"text": "antagonist", "type": "Chemical"}]}

Example input:
Sentence: The level of postoperative HbA1c % was related to BMI loss after surgery .

Example answer:
{"entities": [{"text": "HbA1c", "type": "Chemical"}, {"text": "BMI", "type": "IntellectualProduct"}]}

Example input:
Sentence: Infusion of Ex - 9 decreased the time to peak glucose and rate of glucose decline during OGTT , and raised the postprandial nadir by over 70 % , normalising it relative to NSCs and preventing hypoglycaemia in all PBH participants .

Example answer:
{"entities": [{"text": "Infusion", "type": "HealthCareActivity"}, {"text": "Ex - 9", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "OGTT", "type": "HealthCareActivity"}, {"text": "hypoglycaemia", "type": "BiologicFunction"}, {"text": "PBH", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: GLP - 1r blockade prevented hypoglycaemia in 100 % of individuals , normalised beta cell function and reversed neuroglycopenic symptoms , supporting the conclusion that GLP - 1 plays a primary role in mediating hyperinsulinaemic hypoglycaemia in PBH .

Example answer:
{"entities": [{"text": "GLP - 1r", "type": "Chemical"}, {"text": "hypoglycaemia", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "beta cell function", "type": "BiologicFunction"}, {"text": "reversed neuroglycopenic symptoms", "type": "Finding"}, {"text": "GLP - 1", "type": "Chemical"}, {"text": "hyperinsulinaemic hypoglycaemia", "type": "BiologicFunction"}, {"text": "PBH", "type": "BiologicFunction"}]}

Input:
Sentence: Critical role for GLP - 1 in symptomatic post - bariatric hypoglycaemia Post - bariatric hypoglycaemia ( PBH ) is a rare , but severe , metabolic disorder arising months to years after bariatric surgery .

## Item MedMentions:test:2776
Example input:
Sentence: We found a possible association between inflammatory markers and exclusive breastfeeding duration in adolescents , regardless of their BMI .

Example answer:
{"entities": [{"text": "found", "type": "Finding"}, {"text": "possible", "type": "Finding"}, {"text": "markers", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: On the other hand , in elderly patients , lesions were characterized by a single , large , well - demarcated amorphous calcified deposit surrounded by fibrous tissue , without chronic inflammation or foreign body reaction .

Example answer:
{"entities": [{"text": "elderly", "type": "PopulationGroup"}, {"text": "lesions", "type": "Finding"}, {"text": "well - demarcated amorphous calcified deposit", "type": "BiologicFunction"}, {"text": "surrounded", "type": "SpatialConcept"}, {"text": "fibrous tissue", "type": "AnatomicalStructure"}, {"text": "chronic inflammation", "type": "BiologicFunction"}, {"text": "foreign body reaction", "type": "BiologicFunction"}]}

Example input:
Sentence: Hypertension was the most frequent comorbidity ( 40 . 0 % ) , followed by diabetes mellitus ( 17 . 8 % ) and Alzheimer 's disease ( 14 . 8 % ) .

Example answer:
{"entities": [{"text": "Hypertension", "type": "BiologicFunction"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "Alzheimer 's disease", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study , youth with chronic pain associated with juvenile fibromyalgia ( JFM ) , juvenile idiopathic arthritis ( JIA ) , or sickle cell disease ( SCD ) ( ages 8 to 18 years ) from three pediatric centers completed all 47 candidate items for development of the pain behavior item bank along with established measures of pain interference , depressive symptoms , fatigue , average pain intensity , and pain catastrophizing .

Example answer:
{"entities": [{"text": "chronic pain", "type": "Finding"}, {"text": "juvenile fibromyalgia", "type": "BiologicFunction"}, {"text": "JFM", "type": "BiologicFunction"}, {"text": "juvenile idiopathic arthritis", "type": "BiologicFunction"}, {"text": "JIA", "type": "BiologicFunction"}, {"text": "sickle cell disease", "type": "BiologicFunction"}, {"text": "SCD", "type": "BiologicFunction"}, {"text": "pediatric centers", "type": "Organization"}, {"text": "items", "type": "IntellectualProduct"}, {"text": "item bank", "type": "IntellectualProduct"}, {"text": "pain interference", "type": "IntellectualProduct"}, {"text": "depressive symptoms", "type": "Finding"}, {"text": "fatigue", "type": "Finding"}, {"text": "average pain intensity", "type": "IntellectualProduct"}, {"text": "pain catastrophizing", "type": "BiologicFunction"}]}

Example input:
Sentence: 48 ; 95 % CI 1 . 31 - 4 . 70 ) , and cystic fibrosis ( OR 2 . 17 ; 95 % CI 1 . 16 - 4 . 06 ) .

Example answer:
{"entities": [{"text": "cystic fibrosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , we found an association between inflammatory and degenerative biomarkers .

Example answer:
{"entities": [{"text": "biomarkers", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Histological signs of chronic inflammation affecting ventricular myocardium are strongly associated with AF and demonstrate significant correlation with fibrosis extent that cannot be explained by cardiovascular comorbidities otherwise .

Example answer:
{"entities": [{"text": "signs", "type": "Finding"}, {"text": "chronic inflammation", "type": "BiologicFunction"}, {"text": "ventricular myocardium", "type": "AnatomicalStructure"}, {"text": "AF", "type": "BiologicFunction"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "cardiovascular", "type": "SpatialConcept"}]}

Example input:
Sentence: Histological evidence of inflammatory reaction associated with fibrosis in the atrial and ventricular walls in a case - control study of patients with history of atrial fibrillation Chronic inflammation in the atrial myocardium was shown to play an important role in the development of atrial fibrosis in patients with atrial fibrillation ( AF ) .

Example answer:
{"entities": [{"text": "inflammatory reaction", "type": "BiologicFunction"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "atrial", "type": "AnatomicalStructure"}, {"text": "ventricular walls", "type": "AnatomicalStructure"}, {"text": "case - control study", "type": "ResearchActivity"}, {"text": "history", "type": "Finding"}, {"text": "atrial fibrillation", "type": "BiologicFunction"}, {"text": "Chronic inflammation", "type": "BiologicFunction"}, {"text": "atrial myocardium", "type": "AnatomicalStructure"}, {"text": "role", "type": "IntellectualProduct"}, {"text": "development", "type": "BiologicFunction"}, {"text": "AF", "type": "BiologicFunction"}]}

Example input:
Sentence: Histopathological studies showed higher inflammatory cell infiltrates , cardiac fibrosis , and collagen deposition in LPS group , which were reduced by the administration of NS .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "inflammatory cell infiltrates", "type": "BodySubstance"}, {"text": "cardiac fibrosis", "type": "BiologicFunction"}, {"text": "collagen", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "NS", "type": "Eukaryote"}]}

Example input:
Sentence: Fibrosis extent demonstrated correlation with both CD3 + and CD45 + cell counts in the right ( r = 0 . 781 , P < 0 . 001 for CD45 + and r = 0 .

Example answer:
{"entities": [{"text": "Fibrosis", "type": "BiologicFunction"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "CD3 +", "type": "Chemical"}, {"text": "CD45 +", "type": "Chemical"}, {"text": "cell counts", "type": "HealthCareActivity"}]}

Input:
Sentence: Neither fibrosis nor inflammatory cell count showed association with either age or comorbidities .

## Item MedMentions:test:2737
Example input:
Sentence: We have previously clarified that exposure to cigarette smoke extract ( CSE ) of a mouse melanoma cell culture medium causes rapid reduction of intracellular GSH levels , and that the GSH - MVK adduct can be detected by LC / MS analysis while the GSH - CA adduct is hardly detected .

Example answer:
{"entities": [{"text": "cigarette smoke extract", "type": "Chemical"}, {"text": "CSE", "type": "Chemical"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "melanoma cell", "type": "AnatomicalStructure"}, {"text": "culture medium", "type": "Chemical"}, {"text": "intracellular", "type": "SpatialConcept"}, {"text": "GSH", "type": "Chemical"}, {"text": "MVK", "type": "Chemical"}, {"text": "detected", "type": "Finding"}, {"text": "LC / MS analysis", "type": "HealthCareActivity"}, {"text": "CA", "type": "Chemical"}]}

Example input:
Sentence: On the contrary , heavy smoking decreased the risk for men , HR 0 .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: Comparing current smokers and nonsmokers , some significant associations from adjusted analyses included the following : having a Mental Component Summary score ( a measure of overall mental health ) above the mean of the US population relative to below the mean ( adjusted odds ratio [ aOR ] = 0 . 81 , 95 % CI : 0 . 73 - 0 . 90 ) ; having physician - diagnosed depression

Example answer:
{"entities": [{"text": "current smokers", "type": "Finding"}, {"text": "nonsmokers", "type": "Finding"}, {"text": "adjusted analyses", "type": "ResearchActivity"}, {"text": "mental health", "type": "BiologicFunction"}, {"text": "US", "type": "SpatialConcept"}, {"text": "population", "type": "PopulationGroup"}, {"text": "physician", "type": "ProfessionalOrOccupationalGroup"}, {"text": "diagnosed", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , PHAs have high rates of depression ( 40 - 60 % ) , a risk factor for smoking cessation relapse .

Example answer:
{"entities": [{"text": "depression", "type": "BiologicFunction"}, {"text": "risk factor", "type": "Finding"}]}

Example input:
Sentence: Rates of cigarette smoking , a leading contributor to CVD among PHAs , are 40 - 70 % ( 2 - 3 times higher than the general population ) .

Example answer:
{"entities": [{"text": "CVD", "type": "BiologicFunction"}, {"text": "general population", "type": "PopulationGroup"}]}

Example input:
Sentence: A significant proportion of smokers with emphysema according to low - dose chest CT scanning but without airway limitation had alterations in their quality of life , number of exacerbations , Dlco values , and oxygen saturation during the 6MWT test .

Example answer:
{"entities": [{"text": "smokers", "type": "Finding"}, {"text": "emphysema", "type": "BiologicFunction"}, {"text": "chest CT scanning", "type": "HealthCareActivity"}, {"text": "airway", "type": "AnatomicalStructure"}, {"text": "exacerbations", "type": "Finding"}, {"text": "Dlco", "type": "HealthCareActivity"}, {"text": "oxygen saturation", "type": "BiologicFunction"}, {"text": "6MWT test", "type": "HealthCareActivity"}]}

Example input:
Sentence: Compared to the control group , a higher proportion of patients with mesenteric embolization were current smokers ( 89 % vs .

Example answer:
{"entities": [{"text": "mesenteric embolization", "type": "BiologicFunction"}, {"text": "smokers", "type": "Finding"}]}

Example input:
Sentence: To better understand the risk - benefit ratio of ECs , more information is needed about net nicotine consumption and toxicant exposure of cigarette smokers switching to ECs .

Example answer:
{"entities": [{"text": "ECs", "type": "MedicalDevice"}, {"text": "nicotine", "type": "Chemical"}, {"text": "smokers", "type": "Finding"}]}

Example input:
Sentence: Those who switched exclusively to ECs for at least half of the study period significantly reduced two additional VOCs .

Example answer:
{"entities": [{"text": "ECs", "type": "MedicalDevice"}, {"text": "study", "type": "ResearchActivity"}, {"text": "VOCs", "type": "Chemical"}]}

Example input:
Sentence: Smokers using ECs over 4 - weeks maintained cotinine levels and experienced significant reductions in carbon monoxide , NNAL , and two out of eight measured VOC metabolites .

Example answer:
{"entities": [{"text": "Smokers", "type": "Finding"}, {"text": "ECs", "type": "MedicalDevice"}, {"text": "cotinine levels", "type": "HealthCareActivity"}, {"text": "carbon monoxide", "type": "Chemical"}, {"text": "NNAL", "type": "Chemical"}, {"text": "VOC", "type": "Chemical"}, {"text": "metabolites", "type": "Chemical"}]}

Input:
Sentence: Smokers switching exclusively to ECs for at least half of the study period demonstrated significant reductions in HEMA ( p > = 0 . 03 ) and AAMA ( p < 0 . 01 ) .

## Item MedMentions:test:2809
Example input:
Sentence: It is judged that below an absorbed dose of 100 mGy , no clinically relevant tissue damage occurs , forming the basis for the current radiation protection system concerning non - cancer effects .

Example answer:
{"entities": [{"text": "tissue damage", "type": "InjuryOrPoisoning"}, {"text": "radiation protection system", "type": "HealthCareActivity"}]}

Example input:
Sentence: The radiation dose imparted to members of public due to the levels observed is well within station technical specification limit for 3H .

Example answer:
{"entities": [{"text": "members of public", "type": "Organization"}, {"text": "3H", "type": "Chemical"}]}

Example input:
Sentence: Establishment of a mouse model of 70 % lethal dose by total - body irradiation Whereas increasing concerns about radiation exposure to nuclear disasters or side effects of anticancer radiotherapy , relatively little research for radiation damages or remedy has been done .

Example answer:
{"entities": [{"text": "mouse model", "type": "BiologicFunction"}, {"text": "total - body irradiation", "type": "HealthCareActivity"}, {"text": "radiation exposure", "type": "InjuryOrPoisoning"}, {"text": "side effects", "type": "BiologicFunction"}, {"text": "anticancer", "type": "HealthCareActivity"}, {"text": "radiotherapy", "type": "HealthCareActivity"}, {"text": "research", "type": "ResearchActivity"}, {"text": "radiation damages", "type": "BiologicFunction"}]}

Example input:
Sentence: Recent epidemiological findings point , however , to an excess risk of non - cancer diseases following exposure to lower doses of ionizing radiation than was previously thought .

Example answer:
{"entities": [{"text": "non - cancer", "type": "Finding"}, {"text": "diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Radiation therapy was delivered on a Cobalt - 60 unit using a single fraction of 16 Gy .

Example answer:
{"entities": [{"text": "Radiation therapy", "type": "HealthCareActivity"}, {"text": "Cobalt - 60", "type": "Chemical"}]}

Example input:
Sentence: We examine radiosensitivity at the dose of 2 Gy , a routinely administered dose during fractionated radiotherapy , and we determined that a wide range of DSBs were induced by the given dose among healthy individuals , with highly radiosensitive individuals harboring more IR - induced breaks in the genome than radioresistant individuals following exposure to the same dose .

Example answer:
{"entities": [{"text": "fractionated radiotherapy", "type": "HealthCareActivity"}, {"text": "DSBs", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "exposure to", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Biological basis of radiation protection needs rejuvenation Human beings encounter radiation in many different situations - from proximity to radioactive waste sites to participation in medical procedures using X - rays etc .

Example answer:
{"entities": [{"text": "basis", "type": "Chemical"}, {"text": "radiation protection", "type": "HealthCareActivity"}, {"text": "rejuvenation", "type": "HealthCareActivity"}, {"text": "Human beings", "type": "Eukaryote"}, {"text": "proximity", "type": "SpatialConcept"}, {"text": "radioactive waste", "type": "Chemical"}, {"text": "sites", "type": "SpatialConcept"}, {"text": "medical procedures", "type": "HealthCareActivity"}]}

Example input:
Sentence: The potential for radiation from wireless technology to cause serious biological effects has important implications and necessitates a reevaluation of its near - ubiquitous presence , especially in hospitals and medical facilities .

Example answer:
{"entities": [{"text": "hospitals", "type": "Organization"}, {"text": "medical facilities", "type": "Organization"}]}

Example input:
Sentence: Ironically , the same health physics community that has been successful in demonstrating that exposures to radiation and to radioactive materials can be effectively managed is shrinking at an increasingly rapid rate .

Example answer:
{"entities": [{"text": "health physics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "exposures to radiation", "type": "InjuryOrPoisoning"}, {"text": "radioactive materials", "type": "Chemical"}, {"text": "effectively managed", "type": "HealthCareActivity"}]}

Example input:
Sentence: The use of radioactive materials and radiation - generating devices is prevalent today .

Example answer:
{"entities": [{"text": "prevalent today", "type": "SpatialConcept"}]}

Input:
Sentence: Radiation doses occur continuously including during airline flights , in our homes , during medical procedures , and in energy production .

## Item MedMentions:test:2599
Example input:
Sentence: Here , we identified putative target genes of PHY signaling in the moss Physcomitrella patens and found light - regulated genes that are putative orthologs of PIF - controlled genes in Arabidopsis .

Example answer:
{"entities": [{"text": "genes", "type": "AnatomicalStructure"}, {"text": "PHY", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "moss", "type": "Eukaryote"}, {"text": "Physcomitrella patens", "type": "Eukaryote"}, {"text": "light - regulated genes", "type": "AnatomicalStructure"}, {"text": "orthologs", "type": "AnatomicalStructure"}, {"text": "PIF - controlled genes", "type": "AnatomicalStructure"}, {"text": "Arabidopsis", "type": "Eukaryote"}]}

Example input:
Sentence: Our studies reveal a new paradigm of host - pathogen interactions , in which pathogens exploit conserved host post - translational modifications , thereby achieving highly specific receptor binding while also tolerating genetic changes across multiple isoforms of receptors .

Example answer:
{"entities": [{"text": "host - pathogen interactions", "type": "BiologicFunction"}, {"text": "post - translational modifications", "type": "BiologicFunction"}, {"text": "receptor binding", "type": "BiologicFunction"}, {"text": "genetic changes", "type": "BiologicFunction"}, {"text": "isoforms", "type": "Chemical"}, {"text": "receptors", "type": "Chemical"}]}

Example input:
Sentence: Although plant hormone synthesis and signal transduction were both significantly affected by DADS , the expression trends of the genes in these two pathways were conflicting .

Example answer:
{"entities": [{"text": "plant", "type": "Eukaryote"}, {"text": "hormone synthesis", "type": "BiologicFunction"}, {"text": "signal transduction", "type": "BiologicFunction"}, {"text": "DADS", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "pathways", "type": "BiologicFunction"}]}

Example input:
Sentence: Silencing PLA2 influenced the expression of immune - related genes , including MyD88 and defensin in the Toll pathway and relish and diptericin in the Imd pathway .

Example answer:
{"entities": [{"text": "Silencing", "type": "BiologicFunction"}, {"text": "PLA2", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "immune - related genes", "type": "AnatomicalStructure"}, {"text": "MyD88", "type": "AnatomicalStructure"}, {"text": "defensin", "type": "Chemical"}, {"text": "Toll pathway", "type": "BiologicFunction"}, {"text": "relish", "type": "Chemical"}, {"text": "diptericin", "type": "Chemical"}]}

Example input:
Sentence: TRPM2 -mediated Ca ( 2 + ) signaling has been implicated in the aggravation of inflammatory diseases .

Example answer:
{"entities": [{"text": "TRPM2", "type": "Chemical"}, {"text": "Ca ( 2 + ) signaling", "type": "BiologicFunction"}, {"text": "aggravation", "type": "Finding"}, {"text": "inflammatory diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Interplant Aboveground Signaling Prompts Upregulation of Auxin Promoter and Malate Transporter as Part of Defensive Response in the Neighboring Plants When disrupted by stimuli such as herbivory , pathogenic infection , or mechanical wounding , plants secrete signals such as root exudates and volatile organic compounds ( VOCs ) .

Example answer:
{"entities": [{"text": "Upregulation", "type": "BiologicFunction"}, {"text": "Auxin", "type": "Chemical"}, {"text": "Promoter", "type": "Chemical"}, {"text": "Malate", "type": "Chemical"}, {"text": "Transporter", "type": "BiologicFunction"}, {"text": "Defensive Response", "type": "BiologicFunction"}, {"text": "Neighboring", "type": "SpatialConcept"}, {"text": "Plants", "type": "Eukaryote"}, {"text": "herbivory", "type": "Eukaryote"}, {"text": "pathogenic infection", "type": "BiologicFunction"}, {"text": "mechanical wounding", "type": "InjuryOrPoisoning"}, {"text": "plants", "type": "Eukaryote"}, {"text": "secrete", "type": "BiologicFunction"}, {"text": "root", "type": "Eukaryote"}, {"text": "volatile organic compounds", "type": "Chemical"}, {"text": "VOCs", "type": "Chemical"}]}

Example input:
Sentence: Pairwise statistical testing of differential expression followed by co - expression network analysis revealed that physically clustered genes coding for putative virulence functions were induced depending on substrate or stage of plant infection .

Example answer:
{"entities": [{"text": "Pairwise statistical testing", "type": "IntellectualProduct"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "co - expression network analysis", "type": "ResearchActivity"}, {"text": "clustered genes", "type": "AnatomicalStructure"}, {"text": "coding", "type": "SpatialConcept"}, {"text": "virulence", "type": "BiologicFunction"}, {"text": "plant", "type": "Eukaryote"}, {"text": "infection", "type": "BiologicFunction"}]}

Example input:
Sentence: Brassinosteroid / Abscisic Acid Antagonism in Balancing Growth and Stress In this issue of Developmental Cell , Gui et al . ( 2016 ) show that an abscisic acid - inducible remorin protein in rice directly interacts with critical brassinosteroid signaling components to attenuate the brassinosteroid response , thus illuminating one aspect of the brassinosteroid / abscisic acid antagonism .

Example answer:
{"entities": [{"text": "Brassinosteroid", "type": "Chemical"}, {"text": "Abscisic Acid", "type": "Chemical"}, {"text": "Growth", "type": "BiologicFunction"}, {"text": "Stress", "type": "Finding"}, {"text": "issue", "type": "IntellectualProduct"}, {"text": "Developmental Cell", "type": "BiologicFunction"}, {"text": "abscisic acid", "type": "Chemical"}, {"text": "remorin protein", "type": "Chemical"}, {"text": "rice", "type": "Eukaryote"}, {"text": "brassinosteroid", "type": "Chemical"}, {"text": "signaling components", "type": "Chemical"}]}

Example input:
Sentence: Silencing of the genes RDR1 , NPR1 and DCL2 / DCL4 , associated with these defence pathways , enhanced virus spread and accumulation in SO plants in comparison with non - silenced controls , whereas silencing of the genes NPR3 / NPR4 , associated with the hypersensitive response , produced a slight decrease in CTV accumulation and reduced stunting of SO grafted on CTV - infected rough lemon plants .

Example answer:
{"entities": [{"text": "Silencing of the genes", "type": "BiologicFunction"}, {"text": "RDR1", "type": "AnatomicalStructure"}, {"text": "NPR1", "type": "AnatomicalStructure"}, {"text": "DCL2", "type": "AnatomicalStructure"}, {"text": "DCL4", "type": "AnatomicalStructure"}, {"text": "defence pathways", "type": "BiologicFunction"}, {"text": "virus spread", "type": "BiologicFunction"}, {"text": "accumulation", "type": "Finding"}, {"text": "SO plants", "type": "Eukaryote"}, {"text": "silencing of the genes", "type": "BiologicFunction"}, {"text": "NPR3", "type": "AnatomicalStructure"}, {"text": "NPR4", "type": "AnatomicalStructure"}, {"text": "hypersensitive response", "type": "BiologicFunction"}, {"text": "CTV", "type": "Virus"}, {"text": "stunting", "type": "BiologicFunction"}, {"text": "SO", "type": "Eukaryote"}, {"text": "infected", "type": "Finding"}, {"text": "lemon plants", "type": "Eukaryote"}]}

Example input:
Sentence: We speculate that plant -derived signal - induced upregulation of root -specific ALMT1 in the undamaged neighboring plants sharing the environment with stressed plants may associate more with the benign microbes belowground .

Example answer:
{"entities": [{"text": "plant", "type": "Eukaryote"}, {"text": "upregulation", "type": "BiologicFunction"}, {"text": "root -specific ALMT1", "type": "Chemical"}, {"text": "neighboring", "type": "SpatialConcept"}, {"text": "plants", "type": "Eukaryote"}, {"text": "environment", "type": "SpatialConcept"}, {"text": "stressed", "type": "Finding"}]}

Input:
Sentence: In plant - pathogen interactions , DEGs related to calcium signaling were primarily inhibited , while those encoding pathogenesis - related proteins were primarily up - regulated .

## Item MedMentions:test:2891
Example input:
Sentence: Multinomial logistic regressions ( crude and adjusted for sex and country ) tested associations between recent pain and alcohol use in the pooled multicountry sample .

Example answer:
{"entities": [{"text": "logistic regressions", "type": "ResearchActivity"}, {"text": "crude", "type": "Chemical"}, {"text": "country", "type": "SpatialConcept"}, {"text": "pain", "type": "Finding"}, {"text": "multicountry", "type": "SpatialConcept"}]}

Example input:
Sentence: Multivariate logistic regression analyses ( adjusted for age , gender , education level , physical activity , alcohol use , smoking status , depression , arrhythmia , myocardial infarction , heart failure , stroke ) showed that participants with better feelings of affection , behavioral confirmation and stable good social support had a lower risk of incident SMC .

Example answer:
{"entities": [{"text": "education level", "type": "Finding"}, {"text": "smoking status", "type": "ClinicalAttribute"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "arrhythmia", "type": "Finding"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "heart failure", "type": "BiologicFunction"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "feelings", "type": "BiologicFunction"}, {"text": "affection", "type": "BiologicFunction"}, {"text": "confirmation", "type": "Finding"}, {"text": "SMC", "type": "BiologicFunction"}]}

Example input:
Sentence: The Copenhagen Psychosocial Questionnaire II was used to measure violence and nurse job outcomes .

Example answer:
{"entities": [{"text": "Copenhagen Psychosocial Questionnaire II", "type": "IntellectualProduct"}, {"text": "violence", "type": "BiologicFunction"}, {"text": "nurse", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Multiple logistic regression was used to estimate the adjusted association of background characteristics , depressed mood , and perceived heroin refusal self - efficacy with preference for MAT .

Example answer:
{"entities": [{"text": "Multiple logistic regression", "type": "ResearchActivity"}, {"text": "depressed mood", "type": "Finding"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "heroin", "type": "Chemical"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "MAT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Correlation coefficients indicated that all four executive functioning measures and the two punishment measures were significantly correlated with aggression .

Example answer:
{"entities": [{"text": "executive functioning", "type": "BiologicFunction"}]}

Example input:
Sentence: Multiple linear regressions were conducted to identify predictive factors for elevated specific PTSD symptoms and elevated nonspecific PTSD symptoms .

Example answer:
{"entities": [{"text": "predictive factors", "type": "IntellectualProduct"}, {"text": "PTSD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: Predicting violence and recidivism in a large sample of males on probation or parole This study evaluated the utility of items and scales from the Iowa Violence and Victimization Instrument in a sample of 1961 males from the state of Iowa who were on probation or released from prison to parole supervision .

Example answer:
{"entities": [{"text": "violence", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "Iowa", "type": "SpatialConcept"}, {"text": "Violence", "type": "BiologicFunction"}, {"text": "Instrument", "type": "IntellectualProduct"}, {"text": "released from prison", "type": "Finding"}]}

Example input:
Sentence: Workplace Violence and Job Outcomes of Newly Licensed Nurses The purpose of this study was to examine the prevalence of workplace violence toward newly licensed nurses and the relationship between workplace violence and job outcomes .

Example answer:
{"entities": [{"text": "Licensed Nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "examine", "type": "Finding"}, {"text": "licensed nurses", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Multivariate logistic regression models were used to estimate the association between job strain and T2DM .

Example answer:
{"entities": [{"text": "Multivariate logistic regression models", "type": "IntellectualProduct"}, {"text": "job strain", "type": "Finding"}, {"text": "T2DM", "type": "BiologicFunction"}]}

Example input:
Sentence: Violence perpetrated by nurse colleagues had a significant relationship with all four job outcomes , while violence by physicians had a significant inverse relationship with job satisfaction .

Example answer:
{"entities": [{"text": "Violence", "type": "BiologicFunction"}, {"text": "nurse", "type": "ProfessionalOrOccupationalGroup"}, {"text": "violence", "type": "BiologicFunction"}, {"text": "physicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "job satisfaction", "type": "BiologicFunction"}]}

Input:
Sentence: Multiple linear and logistic regression analyses were conducted to examine the relationship between violence and job outcomes .

## Item MedMentions:test:2725
Example input:
Sentence: Rates and predictors of injury in a population - based cohort of people living with HIV Injuries are responsible for 10 % of the global burden of disease ; however , the epidemiology of injury among people living with HIV ( PLHIV ) has not been well elucidated .

Example answer:
{"entities": [{"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "people", "type": "PopulationGroup"}, {"text": "HIV", "type": "BiologicFunction"}, {"text": "Injuries", "type": "InjuryOrPoisoning"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "people living with HIV", "type": "BiologicFunction"}, {"text": "PLHIV", "type": "BiologicFunction"}]}

Example input:
Sentence: Population -based community study ( Canberra and Queanbeyan , Australia ) .

Example answer:
{"entities": [{"text": "Population", "type": "PopulationGroup"}, {"text": "study", "type": "ResearchActivity"}, {"text": "Canberra", "type": "SpatialConcept"}, {"text": "Australia", "type": "SpatialConcept"}]}

Example input:
Sentence: Spatio - Temporal History of HIV - 1 CRF35 _ AD in Afghanistan and Iran HIV - 1 Circulating Recombinant Form 35 _ AD ( CRF35 _ AD ) has an important position in the epidemiological profile of Afghanistan and Iran .

Example answer:
{"entities": [{"text": "Spatio - Temporal History", "type": "ResearchActivity"}, {"text": "Afghanistan", "type": "SpatialConcept"}, {"text": "Iran", "type": "SpatialConcept"}, {"text": "HIV - 1 Circulating Recombinant Form 35 _ AD", "type": "Virus"}, {"text": "epidemiological", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: In all , 181 , 814 BC patients ( 1 , 516 male and 180 , 298 female ) were eligible for this study .

Example answer:
{"entities": [{"text": "BC", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Genotype data were also available from 5154 healthy UK controls from the Wellcome Trust ( WTCCC2 ) for comparison .

Example answer:
{"entities": [{"text": "Wellcome Trust ( WTCCC2 )", "type": "ResearchActivity"}]}

Example input:
Sentence: Cost - Effectiveness of the ' One4All ' HIV Linkage Intervention in Guangxi Zhuang Autonomous Region , China In Guangxi Zhuang Autonomous Region , China , an estimated 80 % of newly - identified antiretroviral therapy ( ART ) - eligible patients are not engaged in ART .

Example answer:
{"entities": [{"text": "One4All", "type": "HealthCareActivity"}, {"text": "HIV", "type": "BiologicFunction"}, {"text": "Intervention", "type": "HealthCareActivity"}, {"text": "Guangxi Zhuang Autonomous Region", "type": "SpatialConcept"}, {"text": "China", "type": "SpatialConcept"}, {"text": "antiretroviral therapy", "type": "HealthCareActivity"}, {"text": "ART", "type": "HealthCareActivity"}]}

Example input:
Sentence: Birth records with covariates were obtained from the BC Perinatal Database Registry ( N = 232 , 291 ) .

Example answer:
{"entities": [{"text": "BC Perinatal Database Registry", "type": "IntellectualProduct"}]}

Example input:
Sentence: Using Canadian census data , published literature and expert opinions , two population - based , top - down mathematical models were developed to estimate the supply and demand for donor sperm and the feasibility of an ASD program .

Example answer:
{"entities": [{"text": "published literature", "type": "IntellectualProduct"}, {"text": "two population - based , top - down mathematical models", "type": "IntellectualProduct"}, {"text": "donor", "type": "PopulationGroup"}, {"text": "sperm", "type": "AnatomicalStructure"}, {"text": "feasibility", "type": "ResearchActivity"}]}

Example input:
Sentence: The dataset was provided by the Child Outcomes Research Consortium , which collects outcome measures from child services across the UK .

Example answer:
{"entities": [{"text": "dataset", "type": "IntellectualProduct"}, {"text": "Child Outcomes Research Consortium", "type": "ProfessionalOrOccupationalGroup"}, {"text": "child services", "type": "HealthCareActivity"}, {"text": "UK", "type": "SpatialConcept"}]}

Example input:
Sentence: We populated the model with data from the One4All trial ( CTN - 0056 ) , China CDC HIV registry and published reports .

Example answer:
{"entities": [{"text": "One4All trial", "type": "HealthCareActivity"}, {"text": "CTN - 0056", "type": "HealthCareActivity"}, {"text": "China", "type": "SpatialConcept"}, {"text": "CDC", "type": "Organization"}, {"text": "HIV", "type": "BiologicFunction"}, {"text": "published reports", "type": "IntellectualProduct"}]}

Input:
Sentence: A population - based dataset was created via linkage between the BC Centre for Excellence in HIV / AIDS and PopulationDataBC .

## Item MedMentions:test:2773
Example input:
Sentence: A positive correlation between physical activity level and neurocognitive function has been reported in healthy individuals , but it is unclear whether such a correlation exists in patients with schizophrenia and whether the relationship is different according to inpatients or outpatients .

Example answer:
{"entities": [{"text": "neurocognitive function", "type": "BiologicFunction"}, {"text": "healthy individuals", "type": "PopulationGroup"}, {"text": "schizophrenia", "type": "BiologicFunction"}]}

Example input:
Sentence: Physical Activity and Abnormal Blood Glucose Among Healthy Weight Adults Physical activity has been linked to prevention and treatment of prediabetes and diabetes in overweight and obese adults .

Example answer:
{"entities": [{"text": "Abnormal Blood Glucose", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "prediabetes", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "overweight and obese", "type": "BiologicFunction"}]}

Example input:
Sentence: 001 ) and high activity groups ( OR , 0 . 663 ; 95 % CI , 0 . 589 - 0 . 748 ; p = 0 . 001 ) than in the low activity group , even after adjusting for age , sex , smoking , underlying disease , and general or abdominal obesity and muscle mass .

Example answer:
{"entities": [{"text": "underlying disease", "type": "BiologicFunction"}, {"text": "general", "type": "BiologicFunction"}, {"text": "abdominal obesity", "type": "Finding"}, {"text": "muscle mass", "type": "Finding"}]}

Example input:
Sentence: Higher physical activity was associated with a lower likelihood of abnormal blood glucose in an adjusted Poisson regression .

Example answer:
{"entities": [{"text": "abnormal blood glucose", "type": "Finding"}, {"text": "Poisson regression", "type": "IntellectualProduct"}]}

Example input:
Sentence: Among healthy weight adults , low physical activity levels are significantly associated with abnormal blood glucose ( prediabetes and undiagnosed diabetes ) .

Example answer:
{"entities": [{"text": "abnormal blood glucose", "type": "Finding"}, {"text": "prediabetes", "type": "BiologicFunction"}, {"text": "undiagnosed", "type": "Finding"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Association of physical activity on body composition , cardiometabolic risk factors , and prevalence of cardiovascular disease in the Korean population ( from the fifth Korea national health and nutrition examination survey , 2008 - 2011 ) Data regarding associations among physical activity ( PA ) level , body composition , and prevalence of cardiovascular diseases in Asian populations are rare .

Example answer:
{"entities": [{"text": "cardiometabolic risk factors", "type": "Finding"}, {"text": "cardiovascular disease", "type": "BiologicFunction"}, {"text": "Korean population", "type": "PopulationGroup"}, {"text": "Korea", "type": "SpatialConcept"}, {"text": "national health and nutrition examination survey", "type": "ResearchActivity"}, {"text": "cardiovascular diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Although higher physical activity was associated with better neurocognitive functions of outpatients , in inpatients with non - remitted schizophrenia , higher physical activity was associated with worsening of several cognitive domains .

Example answer:
{"entities": [{"text": "neurocognitive functions", "type": "BiologicFunction"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "cognitive domains", "type": "BiologicFunction"}]}

Example input:
Sentence: In the outpatient group , higher physical activity was associated with faster Motor and Psychomotor Speeds in outpatients .

Example answer:
{"entities": [{"text": "Psychomotor", "type": "BiologicFunction"}]}

Example input:
Sentence: Degree of physical activity was positively correlated with eating disorder psychopathology in the sample with AN , and a trend towards a positive association between physical activity and levels of depression and anxiety was also found in this sample .

Example answer:
{"entities": [{"text": "positively correlated", "type": "Finding"}, {"text": "eating disorder", "type": "BiologicFunction"}, {"text": "psychopathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "AN", "type": "BiologicFunction"}, {"text": "positive association", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "anxiety", "type": "Finding"}]}

Example input:
Sentence: Regular physical activity was associated with a low prevalence of cardiovascular diseases ( stroke , myocardial infarction , stable angina , and chronic renal disease ) , which was independent of body composition and conventional risk factors in the Korean population , with a positive dose - response relationship .

Example answer:
{"entities": [{"text": "cardiovascular diseases", "type": "BiologicFunction"}, {"text": "stroke", "type": "InjuryOrPoisoning"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "stable angina", "type": "BiologicFunction"}, {"text": "chronic renal disease", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "Korean population", "type": "PopulationGroup"}, {"text": "positive", "type": "Finding"}]}

Input:
Sentence: Among individuals with AN , physical activity was not significantly correlated with BMI , duration of illness , or number of days since hospital admission .

## Item MedMentions:test:2993
Example input:
Sentence: 4 . 86 ( 95 % CI , 1 . 9 - 11 .

Example answer:
{"entities": []}

Example input:
Sentence: 1 % ( 95 % CI : 24 . 3 - 27 . 9 ) , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 1 % ( 95 % CI : 54 . 6 , 82 . 3 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 50 % ( 95 % CI , 48 . 70 % to 88 . 30 % ) , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 1 % ( 95 % CI 27 . 1 - 51 . 0 % ) in 2015 .

Example answer:
{"entities": []}

Example input:
Sentence: 81 ( 95 % CI 0 . 65 , 1 . 01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 9 % ( 95 % CI : 79 . 6 , 97 . 7 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 37 % ( 95 % CI : 11 . 35 - 11 . 40 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 4 , 95 % CI = -15 .

Example answer:
{"entities": []}

Example input:
Sentence: 15 ( 95 % CI : 5 . 37 - 9 . 51 ) ] .

Example answer:
{"entities": []}

Input:
Sentence: 81 % ( 95 % CI 20 . 21 % - 30 . 07 % ) and 15 .

## Item MedMentions:test:2842
Example input:
Sentence: suzukii larvae and the fact that fruits used in bioassays often start to rot and dissolve before larvae have reached the adult stage .

Example answer:
{"entities": [{"text": "suzukii", "type": "Eukaryote"}, {"text": "larvae", "type": "Eukaryote"}, {"text": "fruits", "type": "Food"}, {"text": "bioassays", "type": "HealthCareActivity"}]}

Example input:
Sentence: Effects of deltamethrin were initially tested using a colonised strain of Culicoides nubeculosus Meigen and a modified World Health Organisation exposure assay .

Example answer:
{"entities": [{"text": "deltamethrin", "type": "Chemical"}, {"text": "Culicoides nubeculosus Meigen", "type": "Eukaryote"}, {"text": "World Health Organisation", "type": "Organization"}, {"text": "exposure assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: cholerae : these methods include swarm assay , temporal stimulation assay , capillary assay , and receptor methylation assay .

Example answer:
{"entities": [{"text": "cholerae", "type": "Bacterium"}, {"text": "swarm assay", "type": "HealthCareActivity"}, {"text": "temporal stimulation assay", "type": "HealthCareActivity"}, {"text": "capillary assay", "type": "HealthCareActivity"}, {"text": "receptor methylation assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using a fragment based approach , over 1000 compounds were screened by a combination of differential scanning fluorimetry , NMR spectroscopy and enzymatic assay with pure recombinant HsaD to identify potential inhibitors .

Example answer:
{"entities": [{"text": "approach", "type": "SpatialConcept"}, {"text": "compounds", "type": "Chemical"}, {"text": "screened", "type": "HealthCareActivity"}, {"text": "differential scanning fluorimetry", "type": "HealthCareActivity"}, {"text": "NMR spectroscopy", "type": "HealthCareActivity"}, {"text": "enzymatic assay", "type": "HealthCareActivity"}, {"text": "HsaD", "type": "Chemical"}, {"text": "inhibitors", "type": "Chemical"}]}

Example input:
Sentence: Use of grape berries in bioassays made it possible to assess effects of an insecticide present on a fruit 's surface on oviposition and larval hatch from eggs .

Example answer:
{"entities": [{"text": "grape berries", "type": "Food"}, {"text": "bioassays", "type": "HealthCareActivity"}, {"text": "insecticide", "type": "Chemical"}, {"text": "fruit 's", "type": "Food"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "oviposition", "type": "BiologicFunction"}, {"text": "larval", "type": "Eukaryote"}, {"text": "hatch", "type": "BiologicFunction"}, {"text": "eggs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Insecticidal effects of deltamethrin in laboratory and field populations of Culicoides species : how effective are host - contact reduction methods in India ? Bluetongue virus ( BTV ) is transmitted by Culicoides biting midges and causes bluetongue ( BT ) , a clinical disease observed primarily in sheep .

Example answer:
{"entities": [{"text": "deltamethrin", "type": "Chemical"}, {"text": "laboratory", "type": "Organization"}, {"text": "Culicoides species", "type": "Eukaryote"}, {"text": "methods", "type": "ResearchActivity"}, {"text": "India", "type": "SpatialConcept"}, {"text": "Bluetongue virus", "type": "Virus"}, {"text": "BTV", "type": "Virus"}, {"text": "transmitted", "type": "BiologicFunction"}, {"text": "Culicoides", "type": "Eukaryote"}, {"text": "biting midges", "type": "Eukaryote"}, {"text": "bluetongue", "type": "BiologicFunction"}, {"text": "BT", "type": "BiologicFunction"}, {"text": "clinical disease", "type": "BiologicFunction"}, {"text": "sheep", "type": "Eukaryote"}]}

Example input:
Sentence: The results demonstrate mainly the biotechnological potential of D .

Example answer:
{"entities": [{"text": "D .", "type": "Bacterium"}]}

Example input:
Sentence: Number of adult flies was significantly reduced if the bioassay medium was treated with an azadirachtin A containing insecticide both before or after egg deposition .

Example answer:
{"entities": [{"text": "flies", "type": "Eukaryote"}, {"text": "bioassay", "type": "HealthCareActivity"}, {"text": "azadirachtin A", "type": "Chemical"}, {"text": "insecticide", "type": "Chemical"}]}

Example input:
Sentence: Suitability of our bioassays was validated in an assessment of the efficacy of four bioinsecticides and one synthetic insecticide against various developmental stages of D .

Example answer:
{"entities": [{"text": "bioassays", "type": "HealthCareActivity"}, {"text": "validated", "type": "ResearchActivity"}, {"text": "bioinsecticides", "type": "Chemical"}, {"text": "insecticide", "type": "Chemical"}, {"text": "developmental", "type": "BiologicFunction"}, {"text": "D .", "type": "Eukaryote"}]}

Example input:
Sentence: Insecticides tested in these three different bioassays with acetamiprid , spinosad or natural pyrethrins as active ingredients achieved a significant D .

Example answer:
{"entities": [{"text": "Insecticides", "type": "Chemical"}, {"text": "bioassays", "type": "HealthCareActivity"}, {"text": "acetamiprid", "type": "Chemical"}, {"text": "spinosad", "type": "Chemical"}, {"text": "pyrethrins", "type": "Chemical"}, {"text": "achieved", "type": "Finding"}, {"text": "D .", "type": "Eukaryote"}]}

Input:
Sentence: Efficacy of insecticides is usually assessed first in laboratory bioassays , which are compounded by the cryptic nature of D .

