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

## Item MedMentions:test:3096
Example input:
Sentence: For FXM prediction , DSA C1q + Ab was the most specific ( 95 . 8 % , 85 - 100 ) and the combination of DSA - MFI > 2 , 300 and C1q + Ab was the most sensitive ( 92 . 0 % , 79 . 3 - 100 ) .

Example answer:
{"entities": [{"text": "FXM", "type": "HealthCareActivity"}, {"text": "DSA", "type": "Chemical"}, {"text": "C1q + Ab", "type": "Chemical"}]}

Example input:
Sentence: Methylchloroisothiazolinone / MI 0 . 02 % aq . ( dose , 6 μg / cm ) diagnoses significantly more contact allergy than 0 . 01 % ( dose , 3 μg / cm ) , without resulting in more adverse reactions .

Example answer:
{"entities": [{"text": "Methylchloroisothiazolinone / MI", "type": "Chemical"}, {"text": "diagnoses", "type": "Finding"}, {"text": "contact allergy", "type": "BiologicFunction"}, {"text": "adverse reactions", "type": "BiologicFunction"}]}

Example input:
Sentence: Site specific probe displacement data implied that site - I , warfarin sodium site , was the high affinity site , while site - II , diazepam site , was the low affinity site for these drugs .

Example answer:
{"entities": [{"text": "site - I", "type": "SpatialConcept"}, {"text": "warfarin sodium", "type": "Chemical"}, {"text": "site", "type": "SpatialConcept"}, {"text": "high affinity site", "type": "SpatialConcept"}, {"text": "site - II", "type": "SpatialConcept"}, {"text": "diazepam", "type": "Chemical"}, {"text": "low affinity site", "type": "SpatialConcept"}, {"text": "drugs", "type": "Chemical"}]}

Example input:
Sentence: 36 was confirmed as the affinity of aza analogues for the mutant D4 receptor S7 .

Example answer:
{"entities": [{"text": "36", "type": "Chemical"}, {"text": "aza", "type": "Chemical"}, {"text": "analogues", "type": "Chemical"}, {"text": "mutant", "type": "BiologicFunction"}, {"text": "D4 receptor S7 .", "type": "Chemical"}]}

Example input:
Sentence: Methods : Equilibrium dialysis method was adopted to study different protein binding aspects of sulfamethoxazole and diclofenac sodium .

Example answer:
{"entities": [{"text": "Equilibrium dialysis method", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "protein binding aspects", "type": "BiologicFunction"}, {"text": "sulfamethoxazole", "type": "Chemical"}, {"text": "diclofenac sodium", "type": "Chemical"}]}

Example input:
Sentence: Conclusion : The study revealed that the concurrent administration of sulfamethoxazole and diclofenac sodium may result drug concentration alteration in blood .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "sulfamethoxazole", "type": "Chemical"}, {"text": "diclofenac sodium", "type": "Chemical"}, {"text": "blood", "type": "BodySubstance"}]}

Example input:
Sentence: Diclofenac sodium also increased the free concentration of sulfamethoxazole from 2 .

Example answer:
{"entities": [{"text": "Diclofenac sodium", "type": "Chemical"}, {"text": "sulfamethoxazole", "type": "Chemical"}]}

Example input:
Sentence: Characterization of the Effect of Drug - Drug Interaction on Protein Binding in Concurrent Administration of Sulfamethoxazol and Diclofenac Sodium Using Bovine Serum Albumin Purpose : This project was aimed to determine the effect of concurrent administration of sulfamethoxazole and diclofenac sodium .

Example answer:
{"entities": [{"text": "Drug - Drug Interaction", "type": "BiologicFunction"}, {"text": "Protein Binding", "type": "BiologicFunction"}, {"text": "Administration", "type": "HealthCareActivity"}, {"text": "Sulfamethoxazol", "type": "Chemical"}, {"text": "Diclofenac Sodium", "type": "Chemical"}, {"text": "Bovine Serum Albumin", "type": "Chemical"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "sulfamethoxazole", "type": "Chemical"}, {"text": "diclofenac sodium", "type": "Chemical"}]}

Example input:
Sentence: During concurrent administration , sulfamethoxazole increased the free concentration of diclofenac sodium from 17 . 5±0 .

Example answer:
{"entities": [{"text": "administration", "type": "HealthCareActivity"}, {"text": "sulfamethoxazole", "type": "Chemical"}, {"text": "diclofenac sodium", "type": "Chemical"}]}

Example input:
Sentence: Diclofenac sodium showed high affinity constant 33 . 66±0 .

Example answer:
{"entities": [{"text": "Diclofenac sodium", "type": "Chemical"}]}

Input:
Sentence: Results : Sulfamethoxazole showed two types of association constants ; high affinity constant 29 .

## Item MedMentions:test:3139
Example input:
Sentence: More than 50 % of the population had either diabetes or prediabetes based on HbA1c .

Example answer:
{"entities": [{"text": "population", "type": "PopulationGroup"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "prediabetes", "type": "BiologicFunction"}, {"text": "HbA1c", "type": "Chemical"}]}

Example input:
Sentence: Total 80 type II DM patients without any associated complications of diabetes were included in this study .

Example answer:
{"entities": [{"text": "type II DM patients without any associated complications", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: 986 - 0 . 999 ) , diabetes mellitus ( OR = 0 . 83 , 95 % CI : 0 . 71 - 0 . 97 ) , and years of education ( OR = 0 . 98 , 95 % CI : 0 . 96 - 0 . 99 ) .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "BiologicFunction"}]}

Example input:
Sentence: In total , 152 patients with DFU were enrolled in the study group , and 52 age and gender matched people with diabetes but no DFU were included as the control group .

Example answer:
{"entities": [{"text": "DFU", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Twenty ( 15 % ) patients in this group had diabetes .

Example answer:
{"entities": [{"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Of the 6323 subjects scheduled for assessment of diabetes state 617 were diabetics and 712 were pre - diabetic .

Example answer:
{"entities": [{"text": "assessment", "type": "HealthCareActivity"}, {"text": "diabetes state", "type": "BiologicFunction"}, {"text": "diabetics", "type": "Finding"}, {"text": "pre - diabetic", "type": "Finding"}]}

Example input:
Sentence: Diabetes was determined by self - report of a physician 's diagnosis ( n = 4885 ) .

Example answer:
{"entities": [{"text": "Diabetes", "type": "BiologicFunction"}, {"text": "self - report", "type": "ResearchActivity"}, {"text": "physician 's", "type": "ProfessionalOrOccupationalGroup"}, {"text": "diagnosis", "type": "Finding"}]}

Example input:
Sentence: 07 ) overall and 2 . 26 ( 95 % CI 1 . 62 - 3 . 15 ) for ≥5 - year duration of diabetes relative to non - diabetics .

Example answer:
{"entities": [{"text": "diabetes", "type": "BiologicFunction"}, {"text": "non - diabetics", "type": "Finding"}]}

Example input:
Sentence: Overall , 196 participants ( 8 . 5 % ) had diabetes , of which 144 ( 73 . 5 % ) had elevated glycaemia ( uncontrolled diabetes ) ; 571 ( 24 . 8 % ) persons had prediabetes .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "glycaemia", "type": "Chemical"}, {"text": "prediabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Significantly more patients with than without diabetes were 65 years of age or older ; patients with diabetes were also more likely to weigh ≥75 kg at baseline ( 57 . 1 % vs 44 .

Example answer:
{"entities": [{"text": "diabetes", "type": "BiologicFunction"}, {"text": "older", "type": "PopulationGroup"}]}

Input:
Sentence: 5 and < 25 who had never been diagnosed with diabetes ( N = 1 , 153 ) .

## Item MedMentions:test:3140
Example input:
Sentence: A total of 144 , 098 patients met the study criteria .

Example answer:
{"entities": []}

Example input:
Sentence: 167 patients were included in the study .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: In the first 48 months , 64 % of 463 patients were eligible for the study and 81 .

Example answer:
{"entities": []}

Example input:
Sentence: Twenty - one patients ( median 33 . 9 years ) were identified .

Example answer:
{"entities": []}

Example input:
Sentence: The study included 275 patients .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: The study included 5102 Medicare beneficiaries diagnosed with cancer who completed CAHPS between 1998 and 2011 within 1 year before their death .

Example answer:
{"entities": [{"text": "Medicare beneficiaries", "type": "PopulationGroup"}, {"text": "diagnosed with cancer", "type": "HealthCareActivity"}, {"text": "CAHPS", "type": "Organization"}, {"text": "1 year before their death", "type": "HealthCareActivity"}]}

Example input:
Sentence: We conducted a population - based case - control study of 5 , 950 , 391 patients using the 2014 Healthcare Cost and Utilization Project ( HCUP ) , Nationwide Inpatient Survey ( NIS ) discharge records of patients 18 years and older .

Example answer:
{"entities": [{"text": "population - based case - control study", "type": "ResearchActivity"}, {"text": "Nationwide Inpatient Survey", "type": "IntellectualProduct"}, {"text": "NIS", "type": "IntellectualProduct"}, {"text": "discharge records", "type": "IntellectualProduct"}]}

Example input:
Sentence: All patients with ovarian cancer diagnosed between 1995 and 2012 were included in the study .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "BiologicFunction"}, {"text": "diagnosed", "type": "HealthCareActivity"}]}

Example input:
Sentence: The data of the 43 patients whose complete measurements were taken again in September 2014 were used for the longitudinal analysis .

Example answer:
{"entities": []}

Example input:
Sentence: At the time of the study ( 2014 ) , all patients from the study group were of working age .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Input:
Sentence: The current study included patients diagnosed through April 2014 .

## Item MedMentions:test:2883
Example input:
Sentence: Furthermore , donor oocyte infants had a lower mean birthweight and length compared to autologous oocyte neonates ( p = 0 . 013 ) ; however no differences were noted among infants born at term .

Example answer:
{"entities": [{"text": "lower mean birthweight", "type": "Finding"}, {"text": "length", "type": "Finding"}, {"text": "oocyte", "type": "AnatomicalStructure"}, {"text": "born at term", "type": "BiologicFunction"}]}

Example input:
Sentence: Upon multivariate analysis with stepwise selection , height and age were significantly correlated with IJV stenosis ( P = 0 . 043 , odds ratio = 0 . 9 ) and CA abnormality ( P = 0 . 012 , odds ratio = 1 . 1 ) , respectively .

Example answer:
{"entities": [{"text": "IJV stenosis", "type": "BiologicFunction"}, {"text": "CA abnormality", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The continuation of breastfeeding for the group of exposed mothers and the unexposed group was ( mean ± standard deviation ) 5 . 57 ± 0 . 098 and 5 .

Example answer:
{"entities": [{"text": "breastfeeding", "type": "BiologicFunction"}, {"text": "group of exposed", "type": "PopulationGroup"}, {"text": "unexposed group", "type": "PopulationGroup"}]}

Example input:
Sentence: A significant interaction between maternal BMI and infant sex on insulin levels ( p = 0 . 0322 ) was observed such that insulin was 229 % higher in obese mothers nursing female infants than in normal weight mothers nursing female infants and 179 % higher than obese mothers nursing male infants .

Example answer:
{"entities": [{"text": "maternal", "type": "Finding"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "insulin levels", "type": "HealthCareActivity"}, {"text": "insulin was 229 % higher", "type": "Finding"}, {"text": "obese", "type": "BiologicFunction"}, {"text": "normal weight", "type": "Finding"}, {"text": "nursing", "type": "BiologicFunction"}]}

Example input:
Sentence: The primary study objective was to determine the outcome of pregnancies in women diagnosed with overt and subclinical hypothyroidism ( SCH ) ( serum TSH > 2 . 5 mIU / L ) and those with elevated circulating thyroid autoantibody levels in the first trimester of pregnancy and after the institution of appropriate thyroxine replacement therapy to maintain the serum TSH ≤ 2 . 5 mIU / L .

Example answer:
{"entities": [{"text": "outcome of pregnancies", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "diagnosed", "type": "Finding"}, {"text": "subclinical hypothyroidism", "type": "BiologicFunction"}, {"text": "SCH", "type": "BiologicFunction"}, {"text": "serum TSH", "type": "HealthCareActivity"}, {"text": "thyroid autoantibody", "type": "Chemical"}, {"text": "thyroxine replacement therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: During childhood , length , weight and head circumference SD - scores increased in the VP - VLBW + group , while SD - scores in the VP + / VLBW + and VP + / VLBW - groups remained stable or decreased .

Example answer:
{"entities": [{"text": "head circumference", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Despite the antibody level 's decline , at 6 months of age , proportions > 0 . 35 μg / ml remained higher in the infants of vaccinated mothers than controls for all three serotypes .

Example answer:
{"entities": [{"text": "antibody", "type": "Chemical"}, {"text": "vaccinated", "type": "Finding"}, {"text": "serotypes", "type": "IntellectualProduct"}]}

Example input:
Sentence: In infants with bronchopulmonary dysplasia and / or pulmonary hypertension ( n = 119 [ 51 % ] ) , RV free wall longitudinal strain and IVS GLS were significantly lower ( P < .01 ) , LV GLS and GLSRs were similar ( P = .56 ) , and IVS segmental longitudinal strain persisted as an RV - dominant base - to - apex gradient from 32 weeks postmenstrual age to 1 year CA .

Example answer:
{"entities": [{"text": "bronchopulmonary dysplasia", "type": "BiologicFunction"}, {"text": "pulmonary hypertension", "type": "BiologicFunction"}, {"text": "RV free wall", "type": "AnatomicalStructure"}, {"text": "IVS", "type": "AnatomicalStructure"}, {"text": "LV", "type": "AnatomicalStructure"}, {"text": "segmental", "type": "SpatialConcept"}, {"text": "RV", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In a study population composed of both STH - infected and uninfected mothers , maternal postpartum deworming was insufficient to impact infant growth and morbidity indicators up to 6 months postpartum .

Example answer:
{"entities": [{"text": "study population", "type": "PopulationGroup"}, {"text": "STH - infected", "type": "BiologicFunction"}, {"text": "maternal postpartum", "type": "BiologicFunction"}, {"text": "deworming", "type": "HealthCareActivity"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "indicators", "type": "IntellectualProduct"}]}

Example input:
Sentence: Among STH - infected mothers , however , important improvements in infant length gain and length - for - age were observed .

Example answer:
{"entities": [{"text": "STH - infected", "type": "BiologicFunction"}]}

Input:
Sentence: However , ad hoc analyses restricted to mothers who tested positive for STHs at baseline suggest that infants of mothers in the experimental group had greater mean length gain in cm

## Item MedMentions:test:2931
Example input:
Sentence: Temperature - and solvent -dependent absorption changes showed that DANP and pyrene chromophores stacked at room temperature in an aqueous buffer solution and quenched fluorescence .

Example answer:
{"entities": [{"text": "solvent", "type": "Chemical"}, {"text": "DANP", "type": "Chemical"}, {"text": "stacked", "type": "SpatialConcept"}, {"text": "room temperature", "type": "Finding"}, {"text": "quenched fluorescence", "type": "HealthCareActivity"}]}

Example input:
Sentence: The TIRM measurements showed that such adsorbed protein layer could mediate the interactions between the two surfaces by generating steric or bridging forces , resulting in different interaction potentials .

Example answer:
{"entities": [{"text": "TIRM", "type": "HealthCareActivity"}, {"text": "adsorbed protein", "type": "Chemical"}, {"text": "surfaces", "type": "SpatialConcept"}]}

Example input:
Sentence: Thus , BCC was proven to be an effective carrier for enhancing oral absorption of peptide drugs , and it is suggested that the carrier morphology is also an important factor that influences the absorption profile .

Example answer:
{"entities": [{"text": "BCC", "type": "Chemical"}, {"text": "carrier", "type": "Chemical"}, {"text": "oral", "type": "SpatialConcept"}, {"text": "peptide", "type": "Chemical"}, {"text": "drugs", "type": "Chemical"}, {"text": "absorption", "type": "BiologicFunction"}]}

Example input:
Sentence: The coating of long - circulation materials , except for chitosan , resulted in negatively charged and stable vesicles at physiological pH .

Example answer:
{"entities": [{"text": "long - circulation materials", "type": "Chemical"}, {"text": "chitosan", "type": "Chemical"}, {"text": "negatively charged", "type": "Chemical"}, {"text": "vesicles", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The Langmuir model was adequately fitted to the adsorption isotherm , thereby obtaining the maximum mercury adsorption capacity of 111 .

Example answer:
{"entities": [{"text": "Langmuir model", "type": "IntellectualProduct"}, {"text": "mercury", "type": "Chemical"}, {"text": "adsorption", "type": "HealthCareActivity"}]}

Example input:
Sentence: Dependence of Intestinal Absorption Profile of Insulin on Carrier Morphology Composed of β - Cyclodextrin - Grafted Chitosan The effect of carrier morphology on the intestinal absorption of insulin was investigated using a morphology - tunable polymeric carrier , β - cyclodextrin - grafted chitosan ( BCC ) .

Example answer:
{"entities": [{"text": "Intestinal Absorption", "type": "BiologicFunction"}, {"text": "Insulin", "type": "Chemical"}, {"text": "Carrier", "type": "Chemical"}, {"text": "β - Cyclodextrin - Grafted Chitosan", "type": "Chemical"}, {"text": "carrier", "type": "Chemical"}, {"text": "intestinal absorption", "type": "BiologicFunction"}, {"text": "insulin", "type": "Chemical"}, {"text": "morphology - tunable polymeric carrier", "type": "Chemical"}, {"text": "β - cyclodextrin - grafted chitosan", "type": "Chemical"}, {"text": "BCC", "type": "Chemical"}]}

Example input:
Sentence: FTIR confirmed the involvement of phosphoric group of sTPP with amine groups of chitosan and also role of hydrogen bonding involved in the preparation of MTXCHNP and DEXCHNP .

Example answer:
{"entities": [{"text": "FTIR", "type": "ResearchActivity"}, {"text": "sTPP", "type": "Chemical"}, {"text": "amine groups", "type": "Chemical"}, {"text": "chitosan", "type": "Chemical"}]}

Example input:
Sentence: A model chitosan - tripolyphosphate ( TPP ) hydrogel nanoparticles ( CS - HNP ) , with a broad spectrum of possible applications was produced and sterilized in the absence and in the presence of protective sugars ( glucose and mannitol ) .

Example answer:
{"entities": [{"text": "chitosan", "type": "Chemical"}, {"text": "tripolyphosphate", "type": "Chemical"}, {"text": "TPP", "type": "Chemical"}, {"text": "CS", "type": "Chemical"}, {"text": "possible", "type": "Finding"}, {"text": "sterilized", "type": "HealthCareActivity"}, {"text": "protective sugars", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "mannitol", "type": "Chemical"}]}

Example input:
Sentence: Chitosan coatings were functionalized with polymer brushes of oligo ( ethylene glycol ) methyl ether methacrylate and 2 - hydroxyethyl methacrylate using photoinduced single electron transfer living radical polymerization and the surfaces were thoroughly characterized by XPS , AFM , water contact angle goniometry , and in situ ellipsometry .

Example answer:
{"entities": [{"text": "Chitosan", "type": "Chemical"}, {"text": "polymer brushes", "type": "Chemical"}, {"text": "oligo ( ethylene glycol ) methyl ether methacrylate", "type": "Chemical"}, {"text": "2 - hydroxyethyl methacrylate", "type": "Chemical"}, {"text": "surfaces", "type": "SpatialConcept"}, {"text": "XPS", "type": "HealthCareActivity"}, {"text": "AFM", "type": "HealthCareActivity"}, {"text": "water contact angle goniometry", "type": "HealthCareActivity"}, {"text": "in situ", "type": "SpatialConcept"}, {"text": "ellipsometry", "type": "HealthCareActivity"}]}

Example input:
Sentence: In this work , we have developed a quantitative structure - property relationship ( QSPR ) model ( R ( 2 ) = 0 . 998 ) , predicting the adsorption energy [ kcal / mol ] for 1 , 701 PXDDs adsorbed on C60 ( PXDD @ C60 ) .

Example answer:
{"entities": [{"text": "model", "type": "IntellectualProduct"}, {"text": "adsorption", "type": "HealthCareActivity"}, {"text": "PXDDs", "type": "Chemical"}, {"text": "C60", "type": "Chemical"}, {"text": "PXDD", "type": "Chemical"}]}

Input:
Sentence: Moreover , the adsorption isotherms of BeP and 2 , 4DCP into chitosan carrier were determined using the Brunauer - Emmett - Teller model .

## Item MedMentions:test:2959
Example input:
Sentence: Results After adjusting for covariates , women were more likely than men to receive home health care and to use emergency department services during the post - acute care period .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}, {"text": "emergency department services", "type": "HealthCareActivity"}, {"text": "acute care", "type": "HealthCareActivity"}]}

Example input:
Sentence: After adjustment for potential confounders , women who experienced child death had higher odds for all types of PLEs ( when unadjusted for depression ) ( OR 1 . 20 - 1 . 71 ; p < 0 . 05 ) and depression ( OR = 1 .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "child death", "type": "Finding"}, {"text": "PLEs", "type": "BiologicFunction"}, {"text": "depression", "type": "BiologicFunction"}]}

Example input:
Sentence: Female responders reported being less often married , having a smaller number of children , a stronger perception of gender significance level and a higher appreciation of personal qualities .

Example answer:
{"entities": [{"text": "Female", "type": "PopulationGroup"}, {"text": "responders", "type": "PopulationGroup"}, {"text": "married", "type": "Finding"}, {"text": "significance level", "type": "ResearchActivity"}]}

Example input:
Sentence: The mean score for satisfaction across the six dimensions was 4 . 56 in the collaborative care group and 4 . 30 in the traditional physician group ( p = 0 . 02 ) .

Example answer:
{"entities": [{"text": "mean score for satisfaction", "type": "IntellectualProduct"}, {"text": "six dimensions", "type": "SpatialConcept"}, {"text": "collaborative care group", "type": "Organization"}, {"text": "traditional physician group", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: We also found that women needed less support regarding housing and obtained a higher level of marital status as compared with men .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: Crude logistic regression showed that women ( odds ratio [ OR ] 1 . 9 , 95 % confidence interval [ CI ] 1 . 3 - 2 . 6 ) , low educational level ( OR 2 . 0 , 95 % CI 1 . 4 - 3 . 0 ) and low mastery ( OR 1 . 4 , 95 % CI 1 . 0 - 1 . 9 ) were associated with cognitive decline , but no daily consumption of vegetables and fruits had only a marginal association ( OR 1 .

Example answer:
{"entities": [{"text": "logistic regression", "type": "ResearchActivity"}, {"text": "low mastery", "type": "Finding"}, {"text": "cognitive decline", "type": "BiologicFunction"}, {"text": "no", "type": "Finding"}, {"text": "vegetables", "type": "Food"}, {"text": "fruits", "type": "Food"}]}

Example input:
Sentence: In multilevel regression , the satisfaction with availability of services correlated with formal employment status ( p < .01 ) , whereas caregivers receiving care in private facilities were less likely satisfied with both availability ( p < .01 ) and attitude of health workers ( p < .05 ) .

Example answer:
{"entities": [{"text": "satisfaction", "type": "BiologicFunction"}, {"text": "employment status", "type": "Finding"}, {"text": "caregivers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "satisfied", "type": "IntellectualProduct"}, {"text": "attitude", "type": "BiologicFunction"}, {"text": "health workers", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Asymptomatic women had a significantly better three - year survival rate compared to symptomatic women ( 80 . 3 % vs . 54 . 3 % , p < 0 . 01 ) .

Example answer:
{"entities": [{"text": "Asymptomatic", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Women who experienced all four stressor categories , including partner related , traumatic , emotional , and financial , had the highest odds ( adjusted odds ratio [ aOR ] : 5 . 43 ; 95 % confidence interval [ CI ] : 5 . 36 - 5 . 51 ) of PPD symptoms .

Example answer:
{"entities": [{"text": "Women", "type": "PopulationGroup"}, {"text": "categories", "type": "IntellectualProduct"}, {"text": "partner", "type": "PopulationGroup"}, {"text": "related", "type": "Finding"}, {"text": "emotional", "type": "Finding"}, {"text": "PPD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: Although most included variables showed associations with satisfaction , after adjustment for all significantly associated variables , only six variables -having children , being in work , having emotional and informational social support , and having good physical and emotional functioning -were positively associated with satisfaction with life as a whole .

Example answer:
{"entities": [{"text": "satisfaction", "type": "BiologicFunction"}, {"text": "emotional", "type": "BiologicFunction"}, {"text": "positively", "type": "Finding"}]}

Input:
Sentence: The odds ratios for satisfaction were higher in most life domains if the woman had social support and good emotional and cognitive functioning .

## Item MedMentions:test:3014
Example input:
Sentence: Combined with simulations , our experiments show that the extended β - strand conformational state of PHF6 ( ( * ) ) is readily populated under aggregating conditions , constituting a defining signature of aggregation - prone tau , and as such , a possible target for therapeutic interventions .

Example answer:
{"entities": [{"text": "simulations", "type": "ResearchActivity"}, {"text": "experiments", "type": "ResearchActivity"}, {"text": "extended", "type": "SpatialConcept"}, {"text": "β - strand conformational", "type": "SpatialConcept"}, {"text": "PHF6 ( ( * ) )", "type": "Chemical"}, {"text": "signature", "type": "SpatialConcept"}, {"text": "prone", "type": "SpatialConcept"}, {"text": "tau", "type": "Chemical"}, {"text": "therapeutic interventions", "type": "HealthCareActivity"}]}

Example input:
Sentence: 0 wt % ) of conductive PANi facilitated cell proliferation , which indicated that PANi has appreciable cell affinity .

Example answer:
{"entities": [{"text": "PANi", "type": "Chemical"}, {"text": "cell proliferation", "type": "BiologicFunction"}, {"text": "cell affinity", "type": "BiologicFunction"}]}

Example input:
Sentence: This resulted in reduced actin polymerization and centripetal retrograde flow of β - actin and PKC - θ from the lamellipodium - like distal ( d ) - SMAC , promoting PKC - θ activation .

Example answer:
{"entities": [{"text": "actin polymerization", "type": "BiologicFunction"}, {"text": "β - actin", "type": "Chemical"}, {"text": "PKC - θ", "type": "Chemical"}, {"text": "lamellipodium - like", "type": "AnatomicalStructure"}, {"text": "distal", "type": "SpatialConcept"}, {"text": "( d ) - SMAC", "type": "AnatomicalStructure"}, {"text": "activation", "type": "BiologicFunction"}]}

Example input:
Sentence: Nanoclusters of FcγRI , but not FcγRII , are constitutively associated with nanoclusters of SIRPα , within 62 ± 5 nm , mediated by the actin cytoskeleton .

Example answer:
{"entities": [{"text": "FcγRI", "type": "Chemical"}, {"text": "FcγRII", "type": "Chemical"}, {"text": "SIRPα", "type": "Chemical"}, {"text": "actin cytoskeleton", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Self - assembled nanocomplex between polymerized phenylboronic acid and doxorubicin for efficient tumor - targeted chemotherapy Since the discovery that nano - scaled particulates can easily be incorporated into tumors via the enhanced permeability and retention ( EPR ) effect , such nanostructures have been exploited as therapeutic small molecule delivery systems .

Example answer:
{"entities": [{"text": "nanocomplex", "type": "Chemical"}, {"text": "phenylboronic acid", "type": "Chemical"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "delivery systems", "type": "MedicalDevice"}]}

Example input:
Sentence: The importance of NO and the formation of PFN1 - actin complexes on the regulation of PKC - θ was corroborated by overexpression of PFN1 - and actin - binding defective mutants of β - actin ( C374S ) and PFN1 ( H119E ) , respectively , which reduced the coalescence of PKC - θ at the c - SMAC .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "PFN1 - actin complexes", "type": "Chemical"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "PKC - θ", "type": "Chemical"}, {"text": "overexpression", "type": "BiologicFunction"}, {"text": "PFN1", "type": "AnatomicalStructure"}, {"text": "actin - binding", "type": "BiologicFunction"}, {"text": "mutants", "type": "BiologicFunction"}, {"text": "β - actin ( C374S )", "type": "AnatomicalStructure"}, {"text": "PFN1 ( H119E )", "type": "AnatomicalStructure"}, {"text": "c - SMAC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Irrespective of the applied techniques , the results consistently displayed that complexation between LF and PPI did occur .

Example answer:
{"entities": [{"text": "results", "type": "Finding"}, {"text": "complexation", "type": "Chemical"}, {"text": "LF", "type": "Chemical"}]}

Example input:
Sentence: Our results indicate that : At neutral pH , the PEI chains are associated and the addition of NaCl initially reduces and then increases the extent of association .The aggregate form is uncollapsed and co - exists with the free chains .

Example answer:
{"entities": [{"text": "PEI chains", "type": "Chemical"}, {"text": "NaCl", "type": "Chemical"}]}

Example input:
Sentence: Heteroprotein Complex Formation of Bovine Lactoferrin and Pea Protein Isolate : A Multiscale Structural Analysis Associative electrostatic interactions between two oppositely charged globular proteins , lactoferrin ( LF ) and pea protein isolate ( PPI ) , the latter being a mixture of vicilin , legumin , and convicilin , was studied with a specific PPI / LF molar ratio at room temperature .

Example answer:
{"entities": [{"text": "Heteroprotein", "type": "Chemical"}, {"text": "Complex", "type": "Chemical"}, {"text": "Bovine Lactoferrin", "type": "Chemical"}, {"text": "Isolate", "type": "Chemical"}, {"text": "lactoferrin", "type": "Chemical"}, {"text": "LF", "type": "Chemical"}, {"text": "isolate", "type": "Chemical"}, {"text": "vicilin", "type": "Chemical"}, {"text": "legumin", "type": "Chemical"}, {"text": "convicilin", "type": "Chemical"}, {"text": "studied", "type": "ResearchActivity"}, {"text": "room temperature", "type": "Finding"}]}

Example input:
Sentence: Although positive deposits of S403 - p p62 and Lys63 -linked ubiquitin were always observed within p62 aggregates , LC3 often showed dissociated distribution from p62 .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "S403", "type": "Chemical"}, {"text": "p", "type": "Chemical"}, {"text": "p62", "type": "Chemical"}, {"text": "Lys63", "type": "Chemical"}, {"text": "ubiquitin", "type": "Chemical"}, {"text": "LC3", "type": "Chemical"}]}

Input:
Sentence: The most frequently observed compact complexes , we identify as mainly leading to LF - PPI coacervation , whereas for the less frequent chain - like aggregates , we hypothesize that additionally PPI - PPI facilitated complexes exist .

## Item MedMentions:test:3056
Example input:
Sentence: Clinical research that investigates fluoride release patterns into saliva and biofilm fluid from different FV products is insufficient .

Example answer:
{"entities": [{"text": "Clinical research", "type": "ResearchActivity"}, {"text": "investigates", "type": "HealthCareActivity"}, {"text": "fluoride", "type": "Chemical"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "saliva", "type": "BodySubstance"}, {"text": "biofilm fluid", "type": "Bacterium"}, {"text": "FV products", "type": "Chemical"}]}

Example input:
Sentence: The present study has shown that FV vary in their ability to deliver fluoride intra - orally potentially related to formulation differences .

Example answer:
{"entities": [{"text": "present", "type": "Finding"}, {"text": "study", "type": "ResearchActivity"}, {"text": "FV", "type": "Chemical"}, {"text": "fluoride", "type": "Chemical"}, {"text": "intra", "type": "SpatialConcept"}, {"text": "orally", "type": "SpatialConcept"}]}

Example input:
Sentence: Reassessing the evidence for and relevance of dietary supplements ' " promoting healthy growth " claims for otherwise healthy children is both needed in a time of global obesity and an opportunity to refine intervention approaches among small children for whom rapid subsequent growth in early life augments risk for chronic disease .

Example answer:
{"entities": [{"text": "dietary supplements '", "type": "Food"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "intervention approaches", "type": "HealthCareActivity"}, {"text": "chronic disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Methodological considerations for designing a community water fluoridation cessation study High - quality , up - to - date research on community water fluoridation ( CWF ) , and especially on the implications of CWF cessation for dental health , is limited .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "research", "type": "ResearchActivity"}, {"text": "dental health", "type": "HealthCareActivity"}]}

Example input:
Sentence: On the basis of the recommendations of the EFSA on the maximum dietary intakes of PFOS and PFOA , human health risks would not be of concern for nonoccupationally exposed populations , at least in the very limited countries for which recent data are available .

Example answer:
{"entities": [{"text": "EFSA", "type": "Organization"}, {"text": "dietary intakes", "type": "BiologicFunction"}, {"text": "PFOS", "type": "Chemical"}, {"text": "PFOA", "type": "Chemical"}, {"text": "human", "type": "Eukaryote"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "countries", "type": "SpatialConcept"}]}

Example input:
Sentence: All respondents thought that helping and controlling a child while brushing their teeth is indispensable , but they did not know the best time to start using the toothpaste with fluoride .

Example answer:
{"entities": [{"text": "respondents", "type": "PopulationGroup"}, {"text": "brushing", "type": "HealthCareActivity"}, {"text": "teeth", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Referenced to Dietary Reference Intakes , survivors consumed inadequate amounts of vitamin D , vitamin E , potassium , fiber , magnesium , and calcium ( 27 % , 54 % , 58 % , 59 % , 84 % , and 90 % of the recommended intakes ) but excessive amounts of sodium and saturated fat ( 155 % and 115 % of the recommended intakes ) from foods .

Example answer:
{"entities": [{"text": "Dietary Reference Intakes", "type": "IntellectualProduct"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "potassium", "type": "Food"}, {"text": "fiber", "type": "Food"}, {"text": "magnesium", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "recommended intakes", "type": "IntellectualProduct"}, {"text": "sodium", "type": "Food"}, {"text": "saturated fat", "type": "Food"}]}

Example input:
Sentence: Trials in the intensive care unit ( ICU ) and emergency department settings post - FEAST have continued to explore liberal FBT strategies as the norm , despite a strong signal associating fluid accumulation with pulmonary pathology in the paediatric population .

Example answer:
{"entities": [{"text": "Trials", "type": "ResearchActivity"}, {"text": "intensive care unit", "type": "Organization"}, {"text": "ICU", "type": "Organization"}, {"text": "emergency department settings", "type": "HealthCareActivity"}, {"text": "post - FEAST", "type": "HealthCareActivity"}, {"text": "FBT strategies", "type": "HealthCareActivity"}, {"text": "pulmonary pathology", "type": "BiologicFunction"}]}

Example input:
Sentence: Although not the only impediment to appropriate treatment of osteoporosis , concern over AFFs remains a major issue and one that needs to be resolved for effective dissemination of existing treatments to reduce fracture risk .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "osteoporosis", "type": "BiologicFunction"}, {"text": "AFFs", "type": "InjuryOrPoisoning"}, {"text": "issue", "type": "Finding"}, {"text": "resolved", "type": "Finding"}, {"text": "dissemination", "type": "SpatialConcept"}, {"text": "treatments", "type": "HealthCareActivity"}, {"text": "fracture", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The evidence base for independent benefit from liberal FBT in the developed world is limited , and the Fluid Expansion as Supportive Therapy ( FEAST ) trial has led to conservative changes in the World Health Organization - recommended approach to FBT in resource - poor settings .

Example answer:
{"entities": [{"text": "FBT", "type": "HealthCareActivity"}, {"text": "Fluid Expansion as Supportive Therapy", "type": "HealthCareActivity"}, {"text": "FEAST", "type": "HealthCareActivity"}, {"text": "trial", "type": "ResearchActivity"}, {"text": "World Health Organization", "type": "Organization"}]}

Input:
Sentence: It is recommended that fluoride supplementation requires a fresh consideration in light of the current study .

## Item MedMentions:test:2893
Example input:
Sentence: Regression analyses revealed that emotional abuse was associated with difficulty describing feelings and externally oriented thinking , but not difficulty identifying feelings .

Example answer:
{"entities": [{"text": "Regression analyses", "type": "IntellectualProduct"}, {"text": "emotional abuse", "type": "BiologicFunction"}, {"text": "feelings", "type": "BiologicFunction"}, {"text": "externally oriented thinking", "type": "BiologicFunction"}]}

Example input:
Sentence: Because all study participants also suffered from post - traumatic disorder ( PTSD ) , follow - up studies are required to tease apart the contributions of PTSD and blast - induced injury on cognitive performance .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "post - traumatic disorder", "type": "BiologicFunction"}, {"text": "PTSD", "type": "BiologicFunction"}, {"text": "follow - up studies", "type": "ResearchActivity"}, {"text": "blast - induced injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Based on attachment theory , the current study investigated the role of parent and teacher emotional support in promoting working memory performance by buffering the negative effect of social stress .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "teacher", "type": "ProfessionalOrOccupationalGroup"}, {"text": "emotional support", "type": "HealthCareActivity"}, {"text": "working memory", "type": "BiologicFunction"}, {"text": "performance", "type": "BiologicFunction"}, {"text": "negative", "type": "Finding"}, {"text": "social stress", "type": "BiologicFunction"}]}

Example input:
Sentence: Low morale and harm to well - being resulted in some trainees feeling dehumanised .

Example answer:
{"entities": [{"text": "morale", "type": "Finding"}, {"text": "harm", "type": "Finding"}, {"text": "feeling", "type": "BiologicFunction"}]}

Example input:
Sentence: Moderation analysis indicated that all EFs moderated the relationship between physical punishment and aggression , and only inhibition and problem - solving ability , but not cognitive flexibility and nonverbal fluency , moderated the relations between symbolic punishment and aggression .

Example answer:
{"entities": [{"text": "Moderation analysis", "type": "ResearchActivity"}, {"text": "EFs", "type": "BiologicFunction"}, {"text": "problem - solving ability", "type": "Finding"}, {"text": "cognitive flexibility", "type": "BiologicFunction"}, {"text": "nonverbal", "type": "Finding"}]}

Example input:
Sentence: Major findings indicated that negative peer norms , exposure to community violence , and poor mental health were negatively correlated with school bonding , while parental monitoring , positive self - regard , and future orientation were correlated with higher school motivation .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "negative peer norms", "type": "Finding"}, {"text": "mental health", "type": "BiologicFunction"}, {"text": "negatively", "type": "Finding"}, {"text": "school", "type": "Organization"}, {"text": "bonding", "type": "BiologicFunction"}, {"text": "orientation", "type": "BiologicFunction"}, {"text": "motivation", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , as predicted , Neuroticism moderated the relationship between coping and burnout .

Example answer:
{"entities": [{"text": "Neuroticism", "type": "BiologicFunction"}, {"text": "burnout", "type": "BiologicFunction"}]}

Example input:
Sentence: Correlation coefficients indicated that all four executive functioning measures and the two punishment measures were significantly correlated with aggression .

Example answer:
{"entities": [{"text": "executive functioning", "type": "BiologicFunction"}]}

Example input:
Sentence: Strong positive correlations were found between all five job stressors and burnout .

Example answer:
{"entities": [{"text": "burnout", "type": "BiologicFunction"}]}

Example input:
Sentence: Violence perpetrated by nurse colleagues had a significant relationship with all four job outcomes , while violence by physicians had a significant inverse relationship with job satisfaction .

Example answer:
{"entities": [{"text": "Violence", "type": "BiologicFunction"}, {"text": "nurse", "type": "ProfessionalOrOccupationalGroup"}, {"text": "violence", "type": "BiologicFunction"}, {"text": "physicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "job satisfaction", "type": "BiologicFunction"}]}

Input:
Sentence: Bullying had a significant relationship with all four job outcomes ( job satisfaction , burnout , commitment to the workplace , and intent to leave ) , while verbal abuse was associated with all job outcomes except for intent to leave .

## Item MedMentions:test:3057
Example input:
Sentence: 01 ) in the presence of any psychiatric diagnosis ( 14 . 72 ) , dementia ( 20 . 87 ) , schizophrenia ( 15 . 67 ) , and mood disorders ( 13 . 41 ) .

Example answer:
{"entities": [{"text": "psychiatric diagnosis", "type": "BiologicFunction"}, {"text": "dementia", "type": "BiologicFunction"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "mood disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: The World Mental Health Survey version of the Composite International Diagnostic Interview ( CIDI ) was used to establish the diagnosis of past 12 - month DSM - IV depression , and assess four positive psychotic symptoms .

Example answer:
{"entities": [{"text": "Composite International Diagnostic Interview", "type": "IntellectualProduct"}, {"text": "CIDI", "type": "IntellectualProduct"}, {"text": "diagnosis", "type": "ResearchActivity"}, {"text": "DSM - IV", "type": "IntellectualProduct"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "positive psychotic symptoms", "type": "Finding"}]}

Example input:
Sentence: Patients with psychiatric comorbidities had worse net adverse cardiac events ( HR 1 . 18 , 95 % CI : 1 . 16 - 1 . 21 ) and mortality rates ( HR 1 . 26 , 95 % CI : 1 . 23 - 1 . 30 ) .

Example answer:
{"entities": []}

Example input:
Sentence: After accounting for adaptive functioning near diagnosis , premorbid behavior problems predicted declines in adaptive functioning 2 years postdiagnosis .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "postdiagnosis", "type": "Finding"}]}

Example input:
Sentence: Specific patterns of psychiatric comorbidity , early age at onset , long duration of illness ( DI ) and untreated illness ( DUI ) have been associated with poor outcome in OCD .

Example answer:
{"entities": [{"text": "patterns", "type": "SpatialConcept"}, {"text": "comorbidity", "type": "Finding"}, {"text": "early age at onset", "type": "Finding"}, {"text": "untreated illness", "type": "Finding"}, {"text": "DUI", "type": "Finding"}, {"text": "poor outcome", "type": "Finding"}, {"text": "OCD", "type": "BiologicFunction"}]}

Example input:
Sentence: Hence , the present study was aimed to assess DUI and related variables in a sample of Italian patients with MDD as well as to investigate potential differences in subjects with onset before and after 2000 .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "Italian", "type": "PopulationGroup"}, {"text": "MDD", "type": "BiologicFunction"}]}

Example input:
Sentence: An overall sample of 188 patients with MDD was assessed through a specific questionnaire investigating DUI and other variables related to the psychopathological onset and latency to first antidepressant treatment , after dividing them in two different subgroups on the basis of their epoch of onset .

Example answer:
{"entities": [{"text": "MDD", "type": "BiologicFunction"}, {"text": "questionnaire", "type": "IntellectualProduct"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "subgroups", "type": "IntellectualProduct"}]}

Example input:
Sentence: Patients had lower information - processing efficiency ( " drift rate " ) and longer nondecision time than controls , and psychosis per se did not influence response caution .

Example answer:
{"entities": [{"text": "psychosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Our findings indicate a significant DUI reduction in MDD patients whose onset occurred after vs before 2000 , along with other relevant differences in terms of onset -related correlates and first pharmacotherapy .

Example answer:
{"entities": [{"text": "reduction", "type": "HealthCareActivity"}, {"text": "MDD", "type": "BiologicFunction"}, {"text": "pharmacotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Italian patients with more recent onset of Major Depressive Disorder have a shorter duration of untreated illness Previous investigation on the duration of untreated illness ( DUI ) in patients with Major Depressive Disorder ( MDD ) revealed a different latency to first antidepressant treatment , with adverse consequences in terms of outcome for individuals with a longer DUI .

Example answer:
{"entities": [{"text": "Italian", "type": "PopulationGroup"}, {"text": "Major Depressive Disorder", "type": "BiologicFunction"}, {"text": "untreated illness", "type": "Finding"}, {"text": "investigation", "type": "HealthCareActivity"}, {"text": "MDD", "type": "BiologicFunction"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "adverse consequences", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}]}

Input:
Sentence: Recent reports , moreover , documented a reduced DUI , as observed with the passage of time , in patients with different psychiatric disorders .

## Item MedMentions:test:2721
Example input:
Sentence: In ASD , deleterious patterns of noise are consistently exacerbated with the presence of secondary ( comorbid ) neuropsychiatric diagnoses , lower verbal and performance intelligence , and autism severity .

Example answer:
{"entities": [{"text": "ASD", "type": "BiologicFunction"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "secondary ( comorbid ) neuropsychiatric diagnoses", "type": "HealthCareActivity"}, {"text": "autism", "type": "BiologicFunction"}]}

Example input:
Sentence: These included individuals with autism spectrum disorders ( ASD ) and healthy - controls in shared data from the Autism Brain Imaging Data Exchange ( ABIDE ) and the Attention - Deficit Hyperactivity Disorder ( ADHD - 200 ) databases .

Example answer:
{"entities": [{"text": "individuals", "type": "PopulationGroup"}, {"text": "autism spectrum disorders", "type": "BiologicFunction"}, {"text": "ASD", "type": "BiologicFunction"}, {"text": "Autism Brain Imaging Data Exchange", "type": "IntellectualProduct"}, {"text": "ABIDE", "type": "IntellectualProduct"}, {"text": "Attention - Deficit Hyperactivity Disorder", "type": "IntellectualProduct"}, {"text": "ADHD - 200", "type": "IntellectualProduct"}, {"text": "databases", "type": "IntellectualProduct"}]}

Example input:
Sentence: Causal and maintaining mechanisms for SA in ASD are underexplored , but it is feasible that there is an ASD specificity to the clinical presentation , with implications for the development of targeted treatments .

Example answer:
{"entities": [{"text": "SA", "type": "BiologicFunction"}, {"text": "ASD", "type": "BiologicFunction"}, {"text": "underexplored", "type": "Finding"}, {"text": "treatments", "type": "HealthCareActivity"}]}

Example input:
Sentence: The assessment included the Motor Severity Stereotypy Scale ( MSSS ) , the Repetitive Behavior Scale - Revised ( RBS - R ) , the Raven 's Colored Progressive Matrices , the Child Behavior CheckList for ages 1½ - 5 or 4 - 18 ( CBCL ) , the Social Responsiveness Scale ( SRS ) , and the Autism Diagnostic Observation Schedule - second edition ( ADOS 2 ) .

Example answer:
{"entities": [{"text": "assessment", "type": "HealthCareActivity"}, {"text": "Motor Severity Stereotypy Scale", "type": "IntellectualProduct"}, {"text": "MSSS", "type": "IntellectualProduct"}, {"text": "Repetitive Behavior Scale - Revised", "type": "IntellectualProduct"}, {"text": "RBS - R", "type": "IntellectualProduct"}, {"text": "Raven 's Colored Progressive Matrices", "type": "Finding"}, {"text": "Social Responsiveness Scale", "type": "IntellectualProduct"}, {"text": "( SRS )", "type": "IntellectualProduct"}, {"text": "Autism Diagnostic Observation Schedule - second edition", "type": "IntellectualProduct"}, {"text": "ADOS 2", "type": "IntellectualProduct"}]}

Example input:
Sentence: Future studies should establish how aspects of the care pathway can be improved for individuals with ASD and SA .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "improved", "type": "Finding"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "ASD", "type": "BiologicFunction"}, {"text": "SA", "type": "BiologicFunction"}]}

Example input:
Sentence: Improving Early Identification and Ongoing Care of Children With Autism Spectrum Disorder Poor adherence to recommended screening for autism spectrum disorder ( ASD ) and pediatricians ' lack of confidence in providing care for children with ASD reflect quality gaps in primary care .

Example answer:
{"entities": [{"text": "Autism Spectrum Disorder", "type": "Finding"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "autism spectrum disorder", "type": "Finding"}, {"text": "ASD", "type": "Finding"}, {"text": "pediatricians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "lack of confidence", "type": "Finding"}, {"text": "primary care", "type": "HealthCareActivity"}]}

Example input:
Sentence: Our objectives were to describe the prevalence and pattern of skin injuries of children with autism spectrum disorder ( ASD ) , to describe how this compared with previously demonstrated skin injury locations in typically developing children , and to identify differences in skin injury frequency and locations between autistic children with and without self - injurious behaviors ( SIBs ) .

Example answer:
{"entities": [{"text": "objectives", "type": "IntellectualProduct"}, {"text": "pattern", "type": "SpatialConcept"}, {"text": "skin injuries", "type": "InjuryOrPoisoning"}, {"text": "autism spectrum disorder", "type": "BiologicFunction"}, {"text": "ASD", "type": "BiologicFunction"}, {"text": "skin injury", "type": "InjuryOrPoisoning"}, {"text": "locations", "type": "Finding"}]}

Example input:
Sentence: Altered Effects of Perspective - Taking on Functional Connectivity during Self - and Other - Referential Processing in Adults with Autism Spectrum Disorder In interactive social situations , it is often crucial to be able to take another person 's perspective when evaluating one 's own or another person 's specific trait ; individuals with ASD critically lack this social skill .

Example answer:
{"entities": [{"text": "Autism Spectrum Disorder", "type": "BiologicFunction"}, {"text": "person 's", "type": "PopulationGroup"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "ASD", "type": "BiologicFunction"}]}

Example input:
Sentence: Data analysis revealed two overarching themes : conceptualizing SA in ASD and service provision .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "SA", "type": "BiologicFunction"}, {"text": "ASD", "type": "BiologicFunction"}, {"text": "service", "type": "HealthCareActivity"}, {"text": "provision", "type": "HealthCareActivity"}]}

Example input:
Sentence: People with ASD commonly report challenges in social interaction and a heightened sensory perception .

Example answer:
{"entities": [{"text": "ASD", "type": "BiologicFunction"}, {"text": "challenges in social interaction", "type": "BiologicFunction"}, {"text": "sensory perception", "type": "BiologicFunction"}]}

Input:
Sentence: Conceptualizing and Treating Social Anxiety in Autism Spectrum Disorder : A Focus Group Study with Multidisciplinary Professionals Individuals who have autism spectrum disorders ( ASD ) commonly experience social anxiety ( SA ) .

## Item MedMentions:test:2904
Example input:
Sentence: The aim of this study was to explore immunopharmacological activities of IM , using the strongly immunogenic 4T1 mouse breast cancer model , and evaluate its effect on the reactivity and the efficiency of PTX cancer therapy .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "IM", "type": "Chemical"}, {"text": "4T1 mouse", "type": "BiologicFunction"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "PTX", "type": "Chemical"}, {"text": "cancer therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Such TME - targeted pathways shed new light on attacking cancer stem cells with fewer side effects than traditional gene - based treatments for cancer , requiring a “ watch - and - wait ” approach .

Example answer:
{"entities": [{"text": "cancer stem cells", "type": "AnatomicalStructure"}, {"text": "gene - based", "type": "AnatomicalStructure"}, {"text": "treatments", "type": "HealthCareActivity"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "watch - and - wait ” approach", "type": "IntellectualProduct"}]}

Example input:
Sentence: Immunohistochemistry showed that mammalian target of rapamycin was expressed in PMH biopsy specimens , which may explain the reduction in PMH tumor size following treatment .

Example answer:
{"entities": [{"text": "Immunohistochemistry", "type": "HealthCareActivity"}, {"text": "mammalian target of rapamycin", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "PMH", "type": "BiologicFunction"}, {"text": "biopsy specimens", "type": "AnatomicalStructure"}, {"text": "tumor size", "type": "SpatialConcept"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: We aimed to optimize the early response monitoring and prediction of AAT efficacy , as indicated by the multi - targeted anti - angiogenic drug sunitinib in U87MG tumors , using noninvasive positron emission computed tomography ( PET ) molecular imaging strategies of multifactorial bioparameters .

Example answer:
{"entities": [{"text": "response monitoring", "type": "HealthCareActivity"}, {"text": "AAT", "type": "HealthCareActivity"}, {"text": "anti - angiogenic drug", "type": "Chemical"}, {"text": "sunitinib", "type": "Chemical"}, {"text": "U87MG tumors", "type": "BiologicFunction"}, {"text": "noninvasive", "type": "IntellectualProduct"}, {"text": "positron emission computed tomography ( PET ) molecular imaging", "type": "HealthCareActivity"}, {"text": "multifactorial", "type": "Finding"}]}

Example input:
Sentence: However , there is little information regarding the role and efficacy of MTT in the relatively rare malignant endocrine tumours mainly involving the adrenal medulla , adrenal cortex , pituitary and parathyroid glands .

Example answer:
{"entities": [{"text": "MTT", "type": "HealthCareActivity"}, {"text": "malignant endocrine tumours", "type": "BiologicFunction"}, {"text": "adrenal medulla", "type": "AnatomicalStructure"}, {"text": "adrenal cortex", "type": "AnatomicalStructure"}, {"text": "pituitary", "type": "AnatomicalStructure"}, {"text": "parathyroid glands", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Molecular targeted therapies in adrenal , pituitary and parathyroid malignancies Tumourigenesis is a relatively common event in endocrine tissues .

Example answer:
{"entities": [{"text": "Molecular targeted therapies", "type": "HealthCareActivity"}, {"text": "adrenal", "type": "BiologicFunction"}, {"text": "pituitary", "type": "BiologicFunction"}, {"text": "parathyroid malignancies", "type": "BiologicFunction"}, {"text": "Tumourigenesis", "type": "BiologicFunction"}, {"text": "endocrine tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Albumin -Bioinspired Gd : CuS Nanotheranostic Agent for In Vivo Photoacoustic / Magnetic Resonance Imaging -Guided Tumor -Targeted Photothermal Therapy Photothermal therapy ( PTT ) is attracting increasing interest and becoming more widely used for skin cancer therapy in the clinic , as a result of its noninvasiveness and low systemic adverse effects .

Example answer:
{"entities": [{"text": "Albumin", "type": "Chemical"}, {"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "In Vivo", "type": "SpatialConcept"}, {"text": "Photoacoustic / Magnetic Resonance Imaging -Guided Tumor -Targeted Photothermal Therapy", "type": "HealthCareActivity"}, {"text": "Photothermal therapy", "type": "HealthCareActivity"}, {"text": "PTT", "type": "HealthCareActivity"}, {"text": "skin cancer therapy", "type": "HealthCareActivity"}, {"text": "clinic", "type": "Organization"}, {"text": "low systemic adverse effects", "type": "BiologicFunction"}]}

Example input:
Sentence: In this review we aim to present currently existing and evolving data using MTT in the treatment of adrenal , pituitary and malignant parathyroid tumours , and explore the current utility and effectiveness of such therapies and their future evolution .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "present", "type": "Finding"}, {"text": "existing", "type": "HealthCareActivity"}, {"text": "MTT", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "adrenal", "type": "BiologicFunction"}, {"text": "pituitary", "type": "BiologicFunction"}, {"text": "malignant parathyroid tumours", "type": "BiologicFunction"}, {"text": "utility", "type": "IntellectualProduct"}, {"text": "therapies", "type": "HealthCareActivity"}, {"text": "evolution", "type": "BiologicFunction"}]}

Example input:
Sentence: This study investigates the potential benefits of planning target volume ( PTV ) margin reduction for whole breast radiotherapy in relation to dose received by organs at risk ( OARs ) , as well as reductions in radiation - induced secondary cancer risk .

Example answer:
{"entities": [{"text": "margin", "type": "AnatomicalStructure"}, {"text": "breast radiotherapy", "type": "HealthCareActivity"}, {"text": "organs at risk", "type": "SpatialConcept"}, {"text": "OARs", "type": "SpatialConcept"}]}

Example input:
Sentence: In vivo blockade of LR signalling combined with iNKT stimulation resulted in superior anti - tumor protection .

Example answer:
{"entities": [{"text": "In vivo", "type": "SpatialConcept"}, {"text": "LR", "type": "Chemical"}, {"text": "signalling", "type": "BiologicFunction"}, {"text": "iNKT", "type": "AnatomicalStructure"}, {"text": "stimulation", "type": "BiologicFunction"}, {"text": "anti - tumor protection", "type": "BiologicFunction"}]}

Input:
Sentence: Simultaneously , the desirable targeting efficiency significantly improved the PTT efficacy to tumors , with low side effects on normal tissues .

## Item MedMentions:test:2886
Example input:
Sentence: Cognitive impairment in first - episode drug - naïve patients with schizophrenia : Relationships with serum concentrations of brain - derived neurotrophic factor and glial cell line - derived neurotrophic factor Evidence suggests that brain - derived neurotrophic factor ( BDNF ) and glial cell line -derived neurotrophic factor ( GDNF ) are important in the regulation of synaptic plasticity , which plays a key role in the cognitive processes in psychiatric disorders .

Example answer:
{"entities": [{"text": "Cognitive impairment", "type": "BiologicFunction"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "brain - derived neurotrophic factor", "type": "Chemical"}, {"text": "glial cell line - derived neurotrophic factor", "type": "Chemical"}, {"text": "BDNF", "type": "Chemical"}, {"text": "glial cell line -derived neurotrophic factor", "type": "Chemical"}, {"text": "GDNF", "type": "Chemical"}, {"text": "regulation of synaptic plasticity", "type": "BiologicFunction"}, {"text": "psychiatric disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: Predicting real - world functional milestones in schizophrenia Schizophrenia is a severe disorder that often causes impairments in major areas of functioning , and most patients do not achieve expected real - world functional milestones .

Example answer:
{"entities": [{"text": "world", "type": "PopulationGroup"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "Schizophrenia", "type": "BiologicFunction"}, {"text": "severe disorder", "type": "Finding"}]}

Example input:
Sentence: In a future study examining the relationship between physical activity and neurocognitive function for facilitating this research field , separation between inpatients and outpatients are needed because the relationship is different between inpatients and outpatients .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "examining", "type": "HealthCareActivity"}, {"text": "neurocognitive function", "type": "BiologicFunction"}]}

Example input:
Sentence: We used an interval timing task to study elementary cognitive processing that requires both frontal and cerebellar networks that are disrupted in patients with schizophrenia .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "cognitive processing", "type": "BiologicFunction"}, {"text": "frontal", "type": "AnatomicalStructure"}, {"text": "cerebellar networks", "type": "AnatomicalStructure"}, {"text": "schizophrenia", "type": "BiologicFunction"}]}

Example input:
Sentence: Our findings suggest that the NEUROD2 gene could play a role in the pathophysiology of neurocognitive dysfunctions as well as in the change of cognitive symptoms under antipsychotic treatment in schizophrenia and schizoaffective disorder .

Example answer:
{"entities": [{"text": "NEUROD2 gene", "type": "AnatomicalStructure"}, {"text": "neurocognitive dysfunctions", "type": "BiologicFunction"}, {"text": "cognitive symptoms", "type": "Finding"}, {"text": "antipsychotic", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "schizoaffective disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: These findings suggest that while schizophrenia patients rely on the same neural network as controls do when attributing beliefs of others , patients did not show reduced activation in the key regions such as the TPJ .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "neural network", "type": "BiologicFunction"}, {"text": "regions", "type": "SpatialConcept"}, {"text": "TPJ", "type": "SpatialConcept"}]}

Example input:
Sentence: We investigated an association of NEUROD2 with neurocognitive dysfunctions in schizophrenia and schizoaffective disorder patients before and during treatment with different second - generation antipsychotics .

Example answer:
{"entities": [{"text": "NEUROD2", "type": "AnatomicalStructure"}, {"text": "neurocognitive dysfunctions", "type": "BiologicFunction"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "schizoaffective disorder", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "second - generation antipsychotics", "type": "Chemical"}]}

Example input:
Sentence: This study aimed to examine the differences in the correlations between physical activity and multiple neurocognitive domains in inpatients and outpatients with schizophrenia and obtain suggestions for further study to facilitate this field .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "examine", "type": "HealthCareActivity"}, {"text": "neurocognitive domains", "type": "BiologicFunction"}, {"text": "schizophrenia", "type": "BiologicFunction"}]}

Example input:
Sentence: Although higher physical activity was associated with better neurocognitive functions of outpatients , in inpatients with non - remitted schizophrenia , higher physical activity was associated with worsening of several cognitive domains .

Example answer:
{"entities": [{"text": "neurocognitive functions", "type": "BiologicFunction"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "cognitive domains", "type": "BiologicFunction"}]}

Example input:
Sentence: A positive correlation between physical activity level and neurocognitive function has been reported in healthy individuals , but it is unclear whether such a correlation exists in patients with schizophrenia and whether the relationship is different according to inpatients or outpatients .

Example answer:
{"entities": [{"text": "neurocognitive function", "type": "BiologicFunction"}, {"text": "healthy individuals", "type": "PopulationGroup"}, {"text": "schizophrenia", "type": "BiologicFunction"}]}

Input:
Sentence: Correlations between physical activity and neurocognitive domain functions in patients with schizophrenia : a cross - sectional study Neurocognitive dysfunction is a critical target symptom of schizophrenia treatment .

## Item MedMentions:test:3148
Example input:
Sentence: 9±6 . 2 years and 2768 ( 58 . 9 % ) were women .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: A total of 16 patients were managed within the period reviewed , consisting of 10 ( 62 . 5 % ) females and six ( 37 . 5 % ) males , giving a male - to - female ratio of 1 : 1 . 7 .

Example answer:
{"entities": []}

Example input:
Sentence: In all , 181 , 814 BC patients ( 1 , 516 male and 180 , 298 female ) were eligible for this study .

Example answer:
{"entities": [{"text": "BC", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: 8±11 . 0 years ; 89 . 2 % were male and 40 .

Example answer:
{"entities": []}

Example input:
Sentence: The registry included 1 , 443 men ( 38 % ) and 2 , 372 women ( 62 % ) .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: There were 711 males ( 46 % ) and 835 females ( 54 % ) ( mean age 4 . 56 ±2 . 26 years ) .

Example answer:
{"entities": []}

Example input:
Sentence: The total sample included 29 , 010 females and 70 , 995 males .

Example answer:
{"entities": []}

Example input:
Sentence: 9 % of cases were males .

Example answer:
{"entities": []}

Example input:
Sentence: The main population affected by rabies virus was male adult farmers .

Example answer:
{"entities": [{"text": "rabies virus", "type": "Virus"}, {"text": "farmers", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: 47 % cases were male and 60 .

Example answer:
{"entities": []}

Input:
Sentence: 1 . 8 . 2 . 269 rabies cases were reported and 70 . 26 % of the cases were male and 61 .

## Item MedMentions:test:2867
Example input:
Sentence: Flavonoids synthesis is regulated by the MBW transcriptional complex , made of R2R3MYB , bHLH and WD40 proteins , with the MYB components liable for channeling the complex towards specific branches of the pathway .

Example answer:
{"entities": [{"text": "Flavonoids", "type": "Chemical"}, {"text": "MBW", "type": "AnatomicalStructure"}, {"text": "transcriptional complex", "type": "AnatomicalStructure"}, {"text": "R2R3MYB", "type": "Chemical"}, {"text": "bHLH", "type": "Chemical"}, {"text": "WD40 proteins", "type": "Chemical"}, {"text": "MYB", "type": "Chemical"}, {"text": "channeling", "type": "SpatialConcept"}, {"text": "complex", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Five strains were used : ( i ) strain overexpressing MexAB - OprM but with no blaNDM - 1 ; ( ii ) strain harbouring blaNDM - 1 but expressing MexAB - OprM at basal level ; ( iii ) strain possessing blaNDM - 1 and overexpressing MexAB - OprM ; ( iv ) P .

Example answer:
{"entities": [{"text": "strain overexpressing", "type": "BiologicFunction"}, {"text": "MexAB - OprM", "type": "AnatomicalStructure"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "overexpressing", "type": "BiologicFunction"}, {"text": "P .", "type": "Bacterium"}]}

Example input:
Sentence: On the basis of the global occurrence data reported during the past 10 years , the incidences and maximum levels in raw cereal grains were 55 % and 1642 μg / kg for aflatoxins , 29 % and 1164 μg / kg for ochratoxin A , 61 % and 71 , 121 μg / kg for fumonisins , 58 % and 41 , 157 μg / kg , for deoxynivalenol , and 46 % and 3049 μg / kg for zearalenone .

Example answer:
{"entities": [{"text": "reported", "type": "HealthCareActivity"}, {"text": "cereal grains", "type": "Food"}, {"text": "aflatoxins", "type": "Chemical"}, {"text": "ochratoxin A", "type": "Chemical"}, {"text": "fumonisins", "type": "Chemical"}, {"text": "deoxynivalenol", "type": "Chemical"}, {"text": "zearalenone", "type": "Chemical"}]}

Example input:
Sentence: Strains were incubated in Luria - Bertani broth with and without 1μg / mL meropenem .

Example answer:
{"entities": [{"text": "Luria - Bertani broth", "type": "Chemical"}, {"text": "meropenem", "type": "Chemical"}]}

Example input:
Sentence: fulvum strains that do not produce or over - produce cladofulvin during the biotrophic growth phase .

Example answer:
{"entities": [{"text": "fulvum", "type": "Eukaryote"}, {"text": "cladofulvin", "type": "Chemical"}, {"text": "biotrophic growth", "type": "BiologicFunction"}]}

Example input:
Sentence: To provide further evidence , we used two glutathione peroxidase ( GPX ) - defective strains , the gpxi strain , the mercaptosuccinic acid ( MS , a GPX inhibitor ) - treated wide - type ( WT ) strain , and gpx overexpression strains for further research .

Example answer:
{"entities": [{"text": "glutathione peroxidase", "type": "Chemical"}, {"text": "GPX", "type": "Chemical"}, {"text": "defective strains", "type": "AnatomicalStructure"}, {"text": "gpxi strain", "type": "AnatomicalStructure"}, {"text": "mercaptosuccinic acid", "type": "Chemical"}, {"text": "MS", "type": "Chemical"}, {"text": "GPX inhibitor", "type": "Chemical"}, {"text": "wide - type ( WT ) strain", "type": "AnatomicalStructure"}, {"text": "gpx overexpression strains", "type": "AnatomicalStructure"}]}

Example input:
Sentence: plantarum 70810 cells ( IL ) on soymilk fermentation , glucosidic isoflavone bioconversion , and cell resistance to simulated gastric and intestinal stresses .

Example answer:
{"entities": [{"text": "plantarum 70810 cells", "type": "AnatomicalStructure"}, {"text": "IL", "type": "AnatomicalStructure"}, {"text": "fermentation", "type": "BiologicFunction"}, {"text": "glucosidic isoflavone", "type": "Chemical"}, {"text": "cell", "type": "AnatomicalStructure"}, {"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "stresses", "type": "BiologicFunction"}]}

Example input:
Sentence: Moreover , the addition of SSGL to AFB₁ - contaminated diet counteracted these negative effects , indicating that SSGL has a protective effect against aflatoxicosis .

Example answer:
{"entities": [{"text": "SSGL", "type": "Eukaryote"}, {"text": "AFB₁", "type": "Chemical"}, {"text": "diet", "type": "Food"}, {"text": "aflatoxicosis", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Reduction of Aflatoxin B1 Toxicity by Lactobacillus plantarum C88 : A Potential Probiotic Strain Isolated from Chinese Traditional Fermented Food " Tofu " In this study , we investigated the potential of Lactobacillus plantarum isolated from Chinese traditional fermented foods to reduce the toxicity of aflatoxin B1 ( AFB1 ) , and its subsequent detoxification mechanism .

Example answer:
{"entities": [{"text": "Reduction", "type": "HealthCareActivity"}, {"text": "Aflatoxin B1", "type": "Chemical"}, {"text": "Toxicity", "type": "InjuryOrPoisoning"}, {"text": "Lactobacillus plantarum C88", "type": "Bacterium"}, {"text": "Probiotic Strain", "type": "Bacterium"}, {"text": "Chinese", "type": "PopulationGroup"}, {"text": "Fermented Food", "type": "Food"}, {"text": "Tofu", "type": "Food"}, {"text": "study", "type": "ResearchActivity"}, {"text": "Lactobacillus plantarum", "type": "Bacterium"}, {"text": "fermented foods", "type": "Food"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "aflatoxin B1", "type": "Chemical"}, {"text": "AFB1", "type": "Chemical"}, {"text": "detoxification", "type": "HealthCareActivity"}]}

Example input:
Sentence: plantarum C88 , and urinary aflatoxin B1 - N7 - guanine ( AFB - N7 - guanine ) , a AFB1 metabolite formed by CYP 1A2 and CYP 3A4 , was significantly reduced by the presence of viable L .

Example answer:
{"entities": [{"text": "plantarum C88", "type": "Bacterium"}, {"text": "aflatoxin B1 - N7 - guanine", "type": "Chemical"}, {"text": "AFB - N7 - guanine", "type": "Chemical"}, {"text": "AFB1", "type": "Chemical"}, {"text": "CYP 1A2", "type": "Chemical"}, {"text": "CYP 3A4", "type": "Chemical"}, {"text": "L .", "type": "Bacterium"}]}

Input:
Sentence: flavus strains produced aflatoxins B1 and B2 without G1 and G2 .

## Item MedMentions:test:2711
Example input:
Sentence: We have used an assay targeting approximately 6700 heterozygous SNPs around the CAH gene ( CYP21A2 ) to construct the high - risk parental haplotypes and tested this approach in five cases , showing that inheritance of the parental alleles can be correctly identified using NIPD .

Example answer:
{"entities": [{"text": "assay", "type": "HealthCareActivity"}, {"text": "SNPs", "type": "SpatialConcept"}, {"text": "CAH gene", "type": "AnatomicalStructure"}, {"text": "CYP21A2", "type": "AnatomicalStructure"}, {"text": "high - risk", "type": "Finding"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "alleles", "type": "AnatomicalStructure"}, {"text": "NIPD", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the present study , 1 , 997 genes only expressed in B73 and 2 , 024 genes only expressed in Mo17 displayed SPE complementation under control and water deficit conditions .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "water", "type": "Chemical"}]}

Example input:
Sentence: Microarray data showed that the ZmNF - Y genes had tissue - specific expression patterns in various maize developmental stages and in response to biotic and abiotic stresses .

Example answer:
{"entities": [{"text": "Microarray", "type": "HealthCareActivity"}, {"text": "ZmNF - Y genes", "type": "AnatomicalStructure"}, {"text": "tissue - specific expression", "type": "BiologicFunction"}, {"text": "maize", "type": "Eukaryote"}, {"text": "response to biotic", "type": "BiologicFunction"}, {"text": "abiotic stresses", "type": "BiologicFunction"}]}

Example input:
Sentence: Isolation , structural analysis , and expression characteristics of the maize nuclear factor Y gene families NUCLEAR FACTOR - Y ( NF - Y ) has been shown to play an important role in growth , development , and response to environmental stress .

Example answer:
{"entities": [{"text": "Isolation", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "maize", "type": "Eukaryote"}, {"text": "nuclear factor Y gene families", "type": "AnatomicalStructure"}, {"text": "NUCLEAR FACTOR - Y", "type": "Chemical"}, {"text": "NF - Y", "type": "Chemical"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "development", "type": "BiologicFunction"}]}

Example input:
Sentence: Agronomic performance , resistance to SCMV infection , and transgene stability were evaluated and compared with the wild - type parental clone Badila ( WT ) at four experimental locations in China across two successive seasons , i .

Example answer:
{"entities": [{"text": "resistance", "type": "BiologicFunction"}, {"text": "SCMV", "type": "Virus"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "transgene", "type": "AnatomicalStructure"}, {"text": "wild - type", "type": "AnatomicalStructure"}, {"text": "parental clone", "type": "AnatomicalStructure"}, {"text": "Badila", "type": "Eukaryote"}, {"text": "WT", "type": "AnatomicalStructure"}, {"text": "experimental locations", "type": "SpatialConcept"}, {"text": "China", "type": "SpatialConcept"}]}

Example input:
Sentence: Single parent expression ( SPE ) of genes is an extreme instance of gene expression complementation , in which genes are active in only one of two parents but are expressed in both reciprocal hybrids .

Example answer:
{"entities": [{"text": "Single parent expression", "type": "BiologicFunction"}, {"text": "SPE", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "parents", "type": "Eukaryote"}, {"text": "expressed", "type": "BiologicFunction"}]}

Example input:
Sentence: However , heterologous gene expression with plasmid is often not stable and might burden growth of host cells , decreases cell mass and product yield .

Example answer:
{"entities": [{"text": "gene expression", "type": "BiologicFunction"}, {"text": "plasmid", "type": "Chemical"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "host cells", "type": "AnatomicalStructure"}, {"text": "cell", "type": "AnatomicalStructure"}]}

Example input:
Sentence: SPE patterns were substantially more stable to expression changes by water deficit treatment than other genotype - specific expression profiles .

Example answer:
{"entities": [{"text": "SPE", "type": "BiologicFunction"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "water", "type": "Chemical"}]}

Example input:
Sentence: Hence , the significant overrepresentation of nonsyntenic genes among SPE patterns and their stability under water limitation suggests a function of these genes during the early developmental manifestation of heterosis under fluctuating environmental conditions .

Example answer:
{"entities": [{"text": "nonsyntenic genes", "type": "AnatomicalStructure"}, {"text": "SPE", "type": "BiologicFunction"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "water", "type": "Chemical"}, {"text": "function", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In this study , we monitored the transcriptomic divergence of the maize inbred lines B73 and Mo17 and their reciprocal F1 - hybrid progeny in primary roots under control and water deficit conditions simulated by PEG treatment .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "transcriptomic", "type": "SpatialConcept"}, {"text": "divergence", "type": "SpatialConcept"}, {"text": "maize", "type": "Eukaryote"}, {"text": "roots", "type": "Eukaryote"}, {"text": "water", "type": "Chemical"}, {"text": "simulated", "type": "ResearchActivity"}, {"text": "PEG", "type": "Chemical"}]}

Input:
Sentence: Stability of single parent gene expression complementation in maize hybrids upon water deficit stress Heterosis is the superior performance of F1 - hybrids compared to their homozygous , genetically distinct parents .

## Item MedMentions:test:3063
Example input:
Sentence: SBS rats also demonstrated a significant three - to fourfold decrease in SMO , GIL , and PTCH mRNA , and protein levels ( determined by Real - Time PCR and Western blot ) compared to control animals .

Example answer:
{"entities": [{"text": "SBS", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}, {"text": "SMO", "type": "Chemical"}, {"text": "GIL", "type": "Chemical"}, {"text": "PTCH", "type": "Chemical"}, {"text": "mRNA", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}, {"text": "Real - Time PCR", "type": "ResearchActivity"}, {"text": "Western blot", "type": "HealthCareActivity"}, {"text": "control animals", "type": "Eukaryote"}]}

Example input:
Sentence: These findings indicate that PAAE is beneficial in improving insulin sensitivity and attenuating metabolic syndrome and hepatic oxidative stress in fructose - fed rats .

Example answer:
{"entities": [{"text": "insulin sensitivity", "type": "BiologicFunction"}, {"text": "metabolic syndrome", "type": "BiologicFunction"}, {"text": "hepatic oxidative stress", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: The aim of this study was to investigate whether the use of glycyrrhizic acid ( GLA ) could improve the development of lung fibrosis in irradiated animals .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "glycyrrhizic acid", "type": "Chemical"}, {"text": "GLA", "type": "Chemical"}, {"text": "lung fibrosis", "type": "BiologicFunction"}, {"text": "irradiated", "type": "HealthCareActivity"}, {"text": "animals", "type": "Eukaryote"}]}

Example input:
Sentence: p . ) treated rats ( group II ) ; diclofenac - induced ( 50mg / kgb . w . , i . p . ) rats treated with Spirulina fusiformis ( 400mg / kgb . w . , p .

Example answer:
{"entities": [{"text": "rats", "type": "Eukaryote"}, {"text": "diclofenac", "type": "Chemical"}, {"text": "Spirulina fusiformis", "type": "Chemical"}]}

Example input:
Sentence: Moreover , the up - regulation of malondialdehyde ( MDA ) and the activity of glutathione peroxidase ( GPx ) were reversed by fucoxanthin treatment .

Example answer:
{"entities": [{"text": "up - regulation", "type": "BiologicFunction"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "MDA", "type": "Chemical"}, {"text": "glutathione peroxidase", "type": "Chemical"}, {"text": "GPx", "type": "Chemical"}, {"text": "fucoxanthin", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , our in vitro studies demonstrated that fucoxanthin increased the neuron survival and reduced the reactive oxygen species ( ROS ) level .

Example answer:
{"entities": [{"text": "fucoxanthin", "type": "Chemical"}, {"text": "neuron survival", "type": "BiologicFunction"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "ROS", "type": "Chemical"}]}

Example input:
Sentence: p . ) rats treated with silymarin ( 25mg / kgb . w . , p . o . ) ( group IV ) ; Spirulina fusiformis ( 400mg / kgb . w . , p . o . ) alone treated rats ( group V ) .

Example answer:
{"entities": [{"text": "rats", "type": "Eukaryote"}, {"text": "silymarin", "type": "Chemical"}, {"text": "Spirulina fusiformis", "type": "Chemical"}]}

Example input:
Sentence: Suppressive effect of Spirulina fusiformis on diclofenac - induced hepato - renal injury and gastrointestinal ulcer in Wistar albino rats : A biochemical and histological approach The non - steroidal anti - inflammatory drug ( NSAID ) , diclofenac causes hepato - renal toxicity and gastric ulcer .

Example answer:
{"entities": [{"text": "Spirulina fusiformis", "type": "Chemical"}, {"text": "diclofenac", "type": "Chemical"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "gastrointestinal ulcer", "type": "BiologicFunction"}, {"text": "Wistar albino rats", "type": "Eukaryote"}, {"text": "histological approach", "type": "HealthCareActivity"}, {"text": "non - steroidal anti - inflammatory drug", "type": "Chemical"}, {"text": "NSAID", "type": "Chemical"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "gastric ulcer", "type": "BiologicFunction"}]}

Example input:
Sentence: The aim of this study was to investigate the protective effect of Spirulina fusiformis on Diclofenac - induced toxicity in Wistar albino rats .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "Spirulina fusiformis", "type": "Chemical"}, {"text": "Diclofenac", "type": "Chemical"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "Wistar albino rats", "type": "Eukaryote"}]}

Example input:
Sentence: Our study proves the hepato - renal and gastroprotective activity of Spirulina fusiformis in diclofenac - treated rats .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "Spirulina fusiformis", "type": "Chemical"}, {"text": "diclofenac", "type": "Chemical"}, {"text": "rats", "type": "Eukaryote"}]}

Input:
Sentence: Spirulina fusiformis showed to reduce such changes and was able to restore normal antioxidant status in the rats .

## Item MedMentions:test:2932
Example input:
Sentence: Peripheral interactions between cannabinoid and opioid receptor agonists in a model of inflammatory mechanical hyperalgesia Activation of opioid and cannabinoid receptors expressed in nociceptors induces effective antihyperalgesia .

Example answer:
{"entities": [{"text": "Peripheral", "type": "SpatialConcept"}, {"text": "cannabinoid", "type": "Chemical"}, {"text": "opioid receptor", "type": "Chemical"}, {"text": "agonists", "type": "Chemical"}, {"text": "model", "type": "BiologicFunction"}, {"text": "inflammatory", "type": "BiologicFunction"}, {"text": "mechanical hyperalgesia", "type": "Finding"}, {"text": "Activation", "type": "BiologicFunction"}, {"text": "opioid", "type": "Chemical"}, {"text": "cannabinoid receptors", "type": "Chemical"}, {"text": "nociceptors", "type": "AnatomicalStructure"}, {"text": "antihyperalgesia", "type": "Finding"}]}

Example input:
Sentence: Also , ACEA reduced the mechanical hyperalgesia induced by bradykinin and by α , β - meATP , a P2X3 receptor non - selective agonist , but not by tumor necrosis factor alpha ( TNF - α ) , interleukin - 1 beta ( IL - 1β ) and chemokine -induced chemoattractant - 1 ( CINC - 1 ) .

Example answer:
{"entities": [{"text": "ACEA", "type": "Chemical"}, {"text": "mechanical hyperalgesia", "type": "Finding"}, {"text": "α , β - meATP", "type": "Chemical"}, {"text": "P2X3 receptor", "type": "Chemical"}, {"text": "agonist", "type": "Chemical"}, {"text": "tumor necrosis factor alpha", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "interleukin - 1 beta", "type": "Chemical"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "chemokine", "type": "Chemical"}, {"text": "chemoattractant - 1", "type": "Chemical"}, {"text": "CINC - 1", "type": "Chemical"}]}

Example input:
Sentence: At the end of 4 weeks , rats were sacrificed under high - dose ketamine anesthesia .

Example answer:
{"entities": [{"text": "rats", "type": "Eukaryote"}, {"text": "ketamine", "type": "Chemical"}, {"text": "anesthesia", "type": "Chemical"}]}

Example input:
Sentence: Patients taking oral ketorolac had longer time of analgesic covering and less postoperative pain when compared with patients receiving intramuscular tramadol .

Example answer:
{"entities": [{"text": "ketorolac", "type": "Chemical"}, {"text": "analgesic covering", "type": "Finding"}, {"text": "postoperative pain", "type": "Finding"}, {"text": "tramadol", "type": "Chemical"}]}

Example input:
Sentence: Recent preclinical studies have suggested that it also inhibits glial cell activation in rodents , and may alter opioid - mediated effects , including analgesia and withdrawal symptoms .

Example answer:
{"entities": [{"text": "preclinical studies", "type": "ResearchActivity"}, {"text": "glial cell", "type": "AnatomicalStructure"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "rodents", "type": "Eukaryote"}, {"text": "opioid", "type": "Chemical"}, {"text": "analgesia", "type": "HealthCareActivity"}, {"text": "withdrawal symptoms", "type": "Finding"}]}

Example input:
Sentence: Sedation was significantly reduced in the ketamine group 6 and 24 hours postoperatively .

Example answer:
{"entities": [{"text": "Sedation", "type": "Finding"}, {"text": "ketamine", "type": "Chemical"}]}

Example input:
Sentence: Patient - controlled analgesia IV morphine consumption 0 to 24 hours postoperatively was significantly reduced in the ketamine group compared with the placebo group : 79 ( 47 ) vs 121 ( 53 ) mg IV , mean difference 42 mg ( 95 % confidence interval -59 to -25 ) , P < 0 . 001 .

Example answer:
{"entities": [{"text": "Patient - controlled analgesia", "type": "HealthCareActivity"}, {"text": "morphine", "type": "Chemical"}, {"text": "ketamine", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , intraoperative ketamine significantly reduced morphine consumption 0 to 24 hours after lumbar fusion surgery in opioid - dependent patients .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "lumbar fusion surgery", "type": "HealthCareActivity"}, {"text": "opioid", "type": "Chemical"}]}

Example input:
Sentence: We hypothesized that intraoperative ketamine would reduce immediate postoperative opioid consumption compared with placebo in chronic pain patients with opioid dependency undergoing lumbar spinal fusion surgery .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "opioid", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}, {"text": "chronic pain", "type": "Finding"}, {"text": "lumbar spinal fusion surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Intraoperative ketamine reduces immediate postoperative opioid consumption after spinal fusion surgery in chronic pain patients with opioid dependency : a randomized , blinded trial Perioperative handling of surgical patients with opioid dependency represents an important clinical problem .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "opioid", "type": "Chemical"}, {"text": "spinal fusion surgery", "type": "HealthCareActivity"}, {"text": "chronic pain", "type": "Finding"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "blinded trial", "type": "ResearchActivity"}, {"text": "handling", "type": "Finding"}, {"text": "problem", "type": "Finding"}]}

Input:
Sentence: Animal studies suggest that ketamine attenuates central sensitization and hyperalgesia and thereby reduces postoperative opioid tolerance .

## Item MedMentions:test:3242
Example input:
Sentence: 5 % ; p = 0 . 02 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 24 . 6 % , P = 0 . 056 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 27 ( 6 . 7 % ) ( P = 0 . 086 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 95 . 1 % ( p = 0 . 803 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 81 . 6 % , p = 0 . 766 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 5 % , P = 0 . 01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 5 % , P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 9 % ) in group B ( P = 0 . 016 ) and at 1 month it was 0 compared to 4 ( 1 . 0 % ) ( P = 0 . 0483 ) .

Example answer:
{"entities": [{"text": "group B", "type": "IntellectualProduct"}]}

Example input:
Sentence: I . 95 % : 7 . 2 - 38 . 6 vs 60 . 0 % , C . I . 95 % : 21 . 6 - 84 . 3 , p = 0 . 01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 12 . 5 % , p - value 1 . 00 ) between the treatment group and control group , respectively .

Example answer:
{"entities": []}

Input:
Sentence: 5 % ) in the standard approach group ( p = .012 ) .

## Item MedMentions:test:3105
Example input:
Sentence: In contrast , activation in the right precentral gyrus showed a significantly stronger correlation with HLE in FHD + compared to FHD - children , suggesting emerging compensatory networks in genetically at - risk children .

Example answer:
{"entities": [{"text": "right precentral gyrus", "type": "AnatomicalStructure"}, {"text": "HLE", "type": "SpatialConcept"}, {"text": "FHD +", "type": "Finding"}, {"text": "FHD -", "type": "Finding"}]}

Example input:
Sentence: Compared to baseline and control ( SCM ) stimulation , nVNS significantly activated primary vagal projections including : nucleus of the solitary tract ( primary central relay of vagal afferents ) , parabrachial area , primary sensory cortex , and insula .

Example answer:
{"entities": [{"text": "( SCM ) stimulation", "type": "Finding"}, {"text": "nVNS", "type": "HealthCareActivity"}, {"text": "primary vagal", "type": "AnatomicalStructure"}, {"text": "projections", "type": "SpatialConcept"}, {"text": "nucleus of the solitary tract", "type": "AnatomicalStructure"}, {"text": "vagal afferents", "type": "AnatomicalStructure"}, {"text": "parabrachial area", "type": "AnatomicalStructure"}, {"text": "primary sensory cortex", "type": "AnatomicalStructure"}, {"text": "insula", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Focal WM and cortical lesions were identified , and volumetric measures from WM , cortical GM , the hippocampus , and deep GM nuclei were obtained .

Example answer:
{"entities": [{"text": "WM", "type": "AnatomicalStructure"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "lesions", "type": "Finding"}, {"text": "volumetric", "type": "SpatialConcept"}, {"text": "GM", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "deep GM", "type": "AnatomicalStructure"}, {"text": "nuclei", "type": "AnatomicalStructure"}]}

Example input:
Sentence: fMRI data were analyzing focusing on a priori regions of interest ( ROIs ) of the core neural systems of mental state attribution : the medial prefrontal cortex ( mPFC ) , temporoparietal junction ( TPJ ) and precuneus .

Example answer:
{"entities": [{"text": "fMRI", "type": "HealthCareActivity"}, {"text": "analyzing", "type": "ResearchActivity"}, {"text": "regions of interest", "type": "SpatialConcept"}, {"text": "ROIs", "type": "SpatialConcept"}, {"text": "core", "type": "SpatialConcept"}, {"text": "mental state", "type": "Finding"}, {"text": "attribution", "type": "BiologicFunction"}, {"text": "medial prefrontal cortex", "type": "AnatomicalStructure"}, {"text": "mPFC", "type": "AnatomicalStructure"}, {"text": "temporoparietal junction", "type": "SpatialConcept"}, {"text": "TPJ", "type": "SpatialConcept"}, {"text": "precuneus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Thus , it appears that the medial PFC and ventral subiculum , brain regions involved in circuitry modulating ventral tegmental dopamine and nucleus accumbens activities , may be regions vulnerable to effects of prenatal LPS on specific subpopulations of interneurons .

Example answer:
{"entities": [{"text": "medial", "type": "SpatialConcept"}, {"text": "PFC", "type": "AnatomicalStructure"}, {"text": "brain regions", "type": "SpatialConcept"}, {"text": "ventral tegmental dopamine", "type": "AnatomicalStructure"}, {"text": "nucleus accumbens", "type": "AnatomicalStructure"}, {"text": "regions", "type": "SpatialConcept"}, {"text": "LPS", "type": "Chemical"}, {"text": "subpopulations", "type": "IntellectualProduct"}, {"text": "interneurons", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Recent work suggests that successful inhibition and cognitive control involve electrophysiological theta - band dynamics , including medial frontal cortex ( MFC ) power enhancement and functional connectivity between the MFC and dorsal prefrontal cortex ( dPFC ) regions , which may be disrupted by alcohol misuse .

Example answer:
{"entities": [{"text": "inhibition", "type": "BiologicFunction"}, {"text": "cognitive control", "type": "BiologicFunction"}, {"text": "medial frontal cortex", "type": "AnatomicalStructure"}, {"text": "MFC", "type": "AnatomicalStructure"}, {"text": "dorsal prefrontal cortex", "type": "AnatomicalStructure"}, {"text": "dPFC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: It is clear that the engrams for individual motor responses held in the basal ganglia are selected by converging cortical and subcortical inputs .

Example answer:
{"entities": [{"text": "motor responses", "type": "ClinicalAttribute"}, {"text": "basal ganglia", "type": "AnatomicalStructure"}, {"text": "cortical", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Deactivations were found in the hippocampus , visual cortex , and spinal trigeminal nucleus .

Example answer:
{"entities": [{"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "visual cortex", "type": "AnatomicalStructure"}, {"text": "spinal trigeminal nucleus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In Study 2 , this device yielded BOLD activation within the insula ( BA 13 ) and anterior cingulate gyrus ( BA 24 ) ; as pressure increased , activation in these areas parametrically increased .

Example answer:
{"entities": [{"text": "device", "type": "MedicalDevice"}, {"text": "BOLD", "type": "BiologicFunction"}, {"text": "insula", "type": "AnatomicalStructure"}, {"text": "BA 13", "type": "AnatomicalStructure"}, {"text": "anterior cingulate gyrus", "type": "AnatomicalStructure"}, {"text": "BA 24", "type": "SpatialConcept"}]}

Example input:
Sentence: In the control group , positive - scene viewing led to increased activity in the left superior parietal gyrus and right middle / superior temporal gyrus .Conclusion Limbic regions and areas from the prefrontal and orbitofrontal cortex are potential ROI for the study of the neurophysiology of BPD in female adolescents .

Example answer:
{"entities": [{"text": "left", "type": "SpatialConcept"}, {"text": "superior parietal gyrus", "type": "AnatomicalStructure"}, {"text": "right middle", "type": "AnatomicalStructure"}, {"text": "superior temporal gyrus", "type": "AnatomicalStructure"}, {"text": "Limbic", "type": "BodySystem"}, {"text": "regions", "type": "SpatialConcept"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "prefrontal", "type": "AnatomicalStructure"}, {"text": "orbitofrontal cortex", "type": "SpatialConcept"}, {"text": "neurophysiology", "type": "BiologicFunction"}]}

Input:
Sentence: Regions of the basal ganglia and frontal cortex were also significantly activated .

## Item MedMentions:test:3121
Example input:
Sentence: This study has two folds of importance : First , it shows that the combination of non - linear transformations and artificial neural networks improves the prediction accuracy of individual predictors .

Example answer:
{"entities": [{"text": "artificial neural networks", "type": "IntellectualProduct"}, {"text": "predictors", "type": "IntellectualProduct"}]}

Example input:
Sentence: High - throughput extraction of imaging and metabolomic quantitative features from magnetic resonance imaging ( MRI ) and magnetic resonance spectroscopic imaging of glioblastoma multiforme ( GBM ) results in tens of variables per patient .

Example answer:
{"entities": [{"text": "imaging", "type": "HealthCareActivity"}, {"text": "metabolomic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "magnetic resonance spectroscopic imaging", "type": "HealthCareActivity"}, {"text": "glioblastoma multiforme", "type": "BiologicFunction"}, {"text": "GBM", "type": "BiologicFunction"}]}

Example input:
Sentence: Substantial promise is , however , shown by a variety of pattern classification approaches to neuroimaging data .

Example answer:
{"entities": [{"text": "pattern", "type": "SpatialConcept"}, {"text": "classification", "type": "IntellectualProduct"}, {"text": "neuroimaging data", "type": "HealthCareActivity"}]}

Example input:
Sentence: Across both datasets , we show improvements in predictive accuracy relative to cross - sectional classifiers for discriminating disease subjects from healthy controls on the basis of whole - brain structural magnetic resonance image -based voxels .

Example answer:
{"entities": [{"text": "cross - sectional", "type": "ResearchActivity"}, {"text": "disease subjects", "type": "PopulationGroup"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "magnetic resonance image", "type": "HealthCareActivity"}]}

Example input:
Sentence: In contrast , magnetic resonance imaging ( MRI ) provides high soft tissue contrast , which makes it ideal for accurate manual contouring .

Example answer:
{"entities": [{"text": "magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "soft tissue", "type": "AnatomicalStructure"}, {"text": "contouring", "type": "HealthCareActivity"}]}

Example input:
Sentence: We developed multivariate classifiers to identify patterns of spectral power across the brain that independently predicted successful episodic encoding and retrieval .

Example answer:
{"entities": [{"text": "multivariate classifiers", "type": "IntellectualProduct"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "episodic encoding", "type": "BiologicFunction"}]}

Example input:
Sentence: Paralleling an increased use of such studies in neuroimaging has been the adoption of pattern recognition algorithms for making individualized predictions of disease .

Example answer:
{"entities": [{"text": "Paralleling", "type": "HealthCareActivity"}, {"text": "neuroimaging", "type": "HealthCareActivity"}, {"text": "pattern recognition algorithms", "type": "IntellectualProduct"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Compared with the annotated diagnostic imaging reports reference standard , the most accurate implementation of machine learning algorithms in our NLP application allowed extracting relevant findings with a sensitivity of .939 and a positive predictive value of .925 .

Example answer:
{"entities": [{"text": "diagnostic imaging", "type": "HealthCareActivity"}, {"text": "reports", "type": "IntellectualProduct"}, {"text": "algorithms", "type": "IntellectualProduct"}, {"text": "positive", "type": "Finding"}]}

Example input:
Sentence: The affinities were modeled using qualitative classification or quantitative regression schemes involving linear , nonlinear , and deep neural network ( DNN ) machine - learning methods used in the scientific literature for quantitative - structure activity relationships ( QSAR ) .

Example answer:
{"entities": [{"text": "classification", "type": "IntellectualProduct"}, {"text": "regression schemes", "type": "IntellectualProduct"}, {"text": "linear", "type": "SpatialConcept"}, {"text": "deep neural network", "type": "IntellectualProduct"}, {"text": "DNN", "type": "IntellectualProduct"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "literature", "type": "IntellectualProduct"}]}

Example input:
Sentence: This article presents a principal component analysis -based feature construction method that uses longitudinal high - dimensional data to improve predictive performance of pattern recognition algorithms .

Example answer:
{"entities": [{"text": "pattern recognition algorithms", "type": "IntellectualProduct"}]}

Input:
Sentence: High - level feature representation is first learned by a deep learning network , where multiparametric MR images are used as the input data .

## Item MedMentions:test:2861
Example input:
Sentence: High - fidelity Glucagon - CreER mouse line generated by CRISPR - Cas9 assisted gene targeting α - cells are the second most prominent cell type in pancreatic islets and are responsible for producing glucagon to increase plasma glucose levels in times of fasting .

Example answer:
{"entities": [{"text": "Glucagon - CreER mouse line", "type": "AnatomicalStructure"}, {"text": "gene targeting", "type": "ResearchActivity"}, {"text": "α - cells", "type": "AnatomicalStructure"}, {"text": "cell type", "type": "IntellectualProduct"}, {"text": "pancreatic islets", "type": "AnatomicalStructure"}, {"text": "glucagon", "type": "Chemical"}, {"text": "plasma glucose levels", "type": "Finding"}, {"text": "fasting", "type": "Finding"}]}

Example input:
Sentence: The NIH , the FDA , the JDRF , Helmsley Trust , Diabetes Technology Society , and other agencies , funders , and organizations have been strongly supportive of advancing artificial pancreas technology and usability , and thus the proceedings from this conference should be of exceptional interest to the diabetes technology community .

Example answer:
{"entities": [{"text": "NIH", "type": "Organization"}, {"text": "FDA", "type": "Organization"}, {"text": "JDRF", "type": "Organization"}, {"text": "Diabetes Technology Society", "type": "Organization"}, {"text": "agencies , funders , and organizations", "type": "Organization"}, {"text": "artificial pancreas", "type": "MedicalDevice"}, {"text": "proceedings from this conference", "type": "IntellectualProduct"}, {"text": "diabetes technology community", "type": "Organization"}]}

Example input:
Sentence: NIR upconversion fluorescence glucose sensing and glucose - responsive insulin release of carbon dot - immobilized hybrid microgels at physiological pH This work reports the preparation of multifunctional hybrid microgels based on the one - pot free radical dispersion polymerization of hydrogen - bonding complexes in water , formed from hydroxyl / carboxyl bearing carbon dots with 4 - vinylphenylboronic acid and acrylamide comonomers , which can realize the simultaneous optical detection of glucose using near infrared light and glucose - responsive insulin delivery .

Example answer:
{"entities": [{"text": "NIR", "type": "HealthCareActivity"}, {"text": "glucose sensing", "type": "BiologicFunction"}, {"text": "glucose", "type": "Chemical"}, {"text": "insulin", "type": "Chemical"}, {"text": "carbon", "type": "Chemical"}, {"text": "immobilized", "type": "HealthCareActivity"}, {"text": "hybrid microgels", "type": "Chemical"}, {"text": "work", "type": "ResearchActivity"}, {"text": "reports", "type": "HealthCareActivity"}, {"text": "free radical", "type": "Chemical"}, {"text": "dispersion", "type": "SpatialConcept"}, {"text": "complexes", "type": "Chemical"}, {"text": "water", "type": "Chemical"}, {"text": "hydroxyl", "type": "Chemical"}, {"text": "carboxyl", "type": "Chemical"}, {"text": "4 - vinylphenylboronic acid", "type": "Chemical"}, {"text": "acrylamide", "type": "Chemical"}, {"text": "comonomers", "type": "Chemical"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "near infrared light", "type": "HealthCareActivity"}]}

Example input:
Sentence: When insulin -loaded micropatches were administered with a permeation enhancer and protease inhibitor , a peak efficacy of 34 % drop in blood glucose levels was observed within 3 h .

Example answer:
{"entities": [{"text": "insulin", "type": "Chemical"}, {"text": "micropatches", "type": "MedicalDevice"}, {"text": "administered", "type": "HealthCareActivity"}, {"text": "permeation enhancer", "type": "Chemical"}, {"text": "protease inhibitor", "type": "Chemical"}, {"text": "drop in blood glucose levels", "type": "Finding"}]}

Example input:
Sentence: Participants using insulin pump therapy were randomized to either 12 weeks of automated closed - loop glucose control , then 12 weeks of sensor augmented insulin pump therapy ( open loop ) , or vice versa .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "insulin pump", "type": "MedicalDevice"}, {"text": "therapy", "type": "HealthCareActivity"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "glucose control", "type": "Chemical"}]}

Example input:
Sentence: The polymeric vesicles function as both moieties of the glucose sensing element ( GOx ) and the insulin release actuator to provide basal insulin release as well as promote insulin release in response to hyperglycemic states .

Example answer:
{"entities": [{"text": "polymeric vesicles", "type": "MedicalDevice"}, {"text": "glucose sensing element", "type": "Chemical"}, {"text": "GOx", "type": "Chemical"}, {"text": "insulin", "type": "Chemical"}, {"text": "basal", "type": "SpatialConcept"}, {"text": "hyperglycemic states", "type": "BiologicFunction"}]}

Example input:
Sentence: A Novel Insulin / Glucose Model after a Mixed - Meal Test in Patients with Type 1 Diabetes on Insulin Pump Therapy Current closed - loop insulin delivery methods stem from sophisticated models of the glucose - insulin ( G / I ) system , mostly based on complex studies employing glucose tracer technology .

Example answer:
{"entities": [{"text": "Model", "type": "IntellectualProduct"}, {"text": "Mixed - Meal Test", "type": "HealthCareActivity"}, {"text": "Type 1 Diabetes", "type": "BiologicFunction"}, {"text": "Insulin Pump", "type": "MedicalDevice"}, {"text": "Therapy", "type": "HealthCareActivity"}, {"text": "closed - loop insulin delivery methods", "type": "MedicalDevice"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "employing", "type": "Finding"}]}

Example input:
Sentence: In the current study , insulin release responds quickly to elevated glucose and its kinetics can be modulated by adjusting the concentration of GOx loaded into the microneedles .

Example answer:
{"entities": [{"text": "insulin", "type": "Chemical"}, {"text": "elevated glucose", "type": "Finding"}, {"text": "modulated", "type": "SpatialConcept"}, {"text": "GOx", "type": "Chemical"}, {"text": "microneedles", "type": "MedicalDevice"}]}

Example input:
Sentence: In vivo testing indicates that a single patch can regulate glucose levels effectively with reduced risk of hypoglycemia .

Example answer:
{"entities": [{"text": "In vivo", "type": "SpatialConcept"}, {"text": "patch", "type": "Chemical"}, {"text": "glucose levels", "type": "Finding"}, {"text": "hypoglycemia", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , a glucose -responsive insulin delivery device , which integrates H2O2 -responsive polymeric vesicles ( PVs ) with a transcutaneous microneedle -array patch was prepared to achieve a fast response , excellent biocompatibility , and painless administration .

Example answer:
{"entities": [{"text": "glucose", "type": "Chemical"}, {"text": "H2O2", "type": "Chemical"}, {"text": "polymeric vesicles", "type": "MedicalDevice"}, {"text": "PVs", "type": "MedicalDevice"}, {"text": "transcutaneous", "type": "HealthCareActivity"}, {"text": "microneedle", "type": "MedicalDevice"}, {"text": "patch", "type": "Chemical"}, {"text": "fast response", "type": "ClinicalAttribute"}, {"text": "administration", "type": "HealthCareActivity"}]}

Input:
Sentence: H2O2 -Responsive Vesicles Integrated with Transcutaneous Patches for Glucose -Mediated Insulin Delivery A self - regulated " smart " insulin administration system would be highly desirable for diabetes management .

## Item MedMentions:test:3087
Example input:
Sentence: Compound 4 was the most active for enhancing the production of antibody forming cells in the mouse spleen .

Example answer:
{"entities": [{"text": "production", "type": "BiologicFunction"}, {"text": "antibody forming cells", "type": "AnatomicalStructure"}, {"text": "mouse spleen", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Screening of two random peptide phage display libraries resulted in the identification of an enargite - selective peptide with the sequence MHKPTVHIKGPT and a chalcopyrite - selective peptide with the sequence RKKKCKGNCCYTPQ .

Example answer:
{"entities": [{"text": "peptide phage display libraries", "type": "Chemical"}, {"text": "enargite", "type": "Chemical"}, {"text": "peptide", "type": "Chemical"}, {"text": "sequence MHKPTVHIKGPT", "type": "SpatialConcept"}, {"text": "chalcopyrite", "type": "Chemical"}, {"text": "sequence RKKKCKGNCCYTPQ", "type": "SpatialConcept"}]}

Example input:
Sentence: Biliary Phospholipids Sustain Enterocyte Proliferation and Intestinal Tumor Progression via Nuclear Receptor Lrh1 in mice The proliferative - crypt compartment of the intestinal epithelium is enriched in phospholipids and accumulation of phospholipids has been described in colorectal tumors .

Example answer:
{"entities": [{"text": "Biliary", "type": "AnatomicalStructure"}, {"text": "Phospholipids", "type": "Chemical"}, {"text": "Enterocyte", "type": "AnatomicalStructure"}, {"text": "Proliferation", "type": "BiologicFunction"}, {"text": "Intestinal Tumor", "type": "BiologicFunction"}, {"text": "Progression", "type": "BiologicFunction"}, {"text": "Nuclear Receptor", "type": "Chemical"}, {"text": "Lrh1", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "intestinal epithelium", "type": "AnatomicalStructure"}, {"text": "phospholipids", "type": "Chemical"}, {"text": "accumulation", "type": "Finding"}, {"text": "colorectal tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: The results showed that all three mdrPRs maintained their abilities to proteolyze HIV viral substrates ( MA ↓ CA and p6 ) and to confer drug resistance .

Example answer:
{"entities": [{"text": "mdrPRs", "type": "Chemical"}, {"text": "proteolyze", "type": "BiologicFunction"}, {"text": "HIV", "type": "Virus"}, {"text": "MA", "type": "Chemical"}, {"text": "CA", "type": "Chemical"}, {"text": "p6", "type": "Chemical"}, {"text": "drug resistance", "type": "BiologicFunction"}]}

Example input:
Sentence: We used Abcb4 ( - / - ) mice which lack biliary phospholipid secretion .

Example answer:
{"entities": [{"text": "Abcb4", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "biliary", "type": "AnatomicalStructure"}, {"text": "phospholipid", "type": "Chemical"}, {"text": "secretion", "type": "BiologicFunction"}]}

Example input:
Sentence: When prepared in the presence of phosphatase inhibitors , both WT - and SF - MRP1 -enriched membrane vesicles had a high Km value for As ( GS ) 3 ( 3 - 6 µM ) , regardless of the cell line .

Example answer:
{"entities": [{"text": "presence", "type": "Finding"}, {"text": "phosphatase inhibitors", "type": "Chemical"}, {"text": "WT -", "type": "Chemical"}, {"text": "SF - MRP1", "type": "Chemical"}, {"text": "membrane", "type": "AnatomicalStructure"}, {"text": "vesicles", "type": "AnatomicalStructure"}, {"text": "cell line", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The peptides were interacted with monolayers spread at the air - water interface and prepared from a 3 : 1 molar mixture of phosphatidylethanolamine and phosphatidylglycerol used to approximate the cell membranes of Gram positive bacteria .

Example answer:
{"entities": [{"text": "peptides", "type": "Chemical"}, {"text": "monolayers", "type": "Chemical"}, {"text": "water", "type": "Chemical"}, {"text": "phosphatidylethanolamine", "type": "Chemical"}, {"text": "phosphatidylglycerol", "type": "Chemical"}, {"text": "cell membranes", "type": "AnatomicalStructure"}, {"text": "Gram positive bacteria", "type": "Bacterium"}]}

Example input:
Sentence: Enhanced performance of proteins separation was achieved on the MCN - C4 - monolith in comparison with the butyl - silica hybrid monolithic column without MCN ( C4 - monolith ) .

Example answer:
{"entities": [{"text": "proteins", "type": "Chemical"}, {"text": "MCN", "type": "Chemical"}]}

Example input:
Sentence: Z02176 ( Ga - DOTA - Pip - B9958 ; Pip : 4 - amino - ( 1 - carboxymethyl ) piperidine ) , Z02137 ( Ga - NODA - Mpaa - Pip - B9958 ; Mpaa : 4 - methylphenylacetic acid ) , and Z04139 ( AlF - NODA - Mpaa - Pip - B9958 ) bound h B1R with high affinity ( Ki = 1 . 4 - 2 . 5 nM ) .

Example answer:
{"entities": [{"text": "Z02176", "type": "Chemical"}, {"text": "Ga - DOTA - Pip - B9958", "type": "Chemical"}, {"text": "Pip", "type": "Chemical"}, {"text": "4 - amino - ( 1 - carboxymethyl ) piperidine )", "type": "Chemical"}, {"text": "Z02137", "type": "Chemical"}, {"text": "Ga - NODA - Mpaa - Pip - B9958", "type": "Chemical"}, {"text": "Mpaa", "type": "Chemical"}, {"text": "4 - methylphenylacetic acid", "type": "Chemical"}, {"text": "Z04139", "type": "Chemical"}, {"text": "AlF - NODA - Mpaa - Pip - B9958", "type": "Chemical"}, {"text": "B1R", "type": "Chemical"}]}

Example input:
Sentence: Immobilization of Zr ( 4 + ) ions on the phosphate groups present at the poly ( EGMP - co - AM - co - BAA ) monolith surface leads to immobilized metal affinity chromatography support .

Example answer:
{"entities": [{"text": "Zr ( 4 + ) ions", "type": "Chemical"}, {"text": "phosphate groups", "type": "Chemical"}, {"text": "poly ( EGMP - co - AM - co - BAA )", "type": "Chemical"}, {"text": "metal", "type": "Chemical"}, {"text": "affinity chromatography", "type": "HealthCareActivity"}]}

Input:
Sentence: This monolith - Zr ( 4 + ) showed a great capacity to capture phosphopeptides .

## Item MedMentions:test:2777
Example input:
Sentence: Furthermore , we investigated a previously unknown neural circuit originating from septal vGAT neurons to a subset of vGAT neurons in the LH , an area involved in homeostatic and hedonic control of energy states .

Example answer:
{"entities": [{"text": "septal", "type": "SpatialConcept"}, {"text": "vGAT", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "subset", "type": "IntellectualProduct"}, {"text": "LH", "type": "SpatialConcept"}, {"text": "area", "type": "SpatialConcept"}, {"text": "homeostatic", "type": "BiologicFunction"}, {"text": "hedonic", "type": "BiologicFunction"}]}

Example input:
Sentence: Plasma corticosterone ( CRT ) level and orexin mRNA expression were built up in the stress and / or seizure groups .

Example answer:
{"entities": [{"text": "Plasma", "type": "BodySubstance"}, {"text": "corticosterone", "type": "Chemical"}, {"text": "( CRT )", "type": "Chemical"}, {"text": "orexin", "type": "AnatomicalStructure"}, {"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "stress", "type": "BiologicFunction"}, {"text": "seizure", "type": "Finding"}]}

Example input:
Sentence: Here , using the cell - type selectivity of genetic methods , circuit mapping , and behavior assays , we sought to decipher neural circuits emanating from the septal nucleus to the lateral hypothalamus ( LH ) that contribute to neural regulation of food intake in mice .

Example answer:
{"entities": [{"text": "cell - type", "type": "IntellectualProduct"}, {"text": "genetic methods", "type": "ResearchActivity"}, {"text": "circuit mapping", "type": "HealthCareActivity"}, {"text": "assays", "type": "HealthCareActivity"}, {"text": "septal nucleus", "type": "AnatomicalStructure"}, {"text": "lateral hypothalamus", "type": "SpatialConcept"}, {"text": "LH", "type": "SpatialConcept"}, {"text": "food intake", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: This effect could be related to inhibited cocaine - and amphetamine - regulated transcript ( CART ) gene expression and serotonin ( 5 - hydroxytryptamine , 5 - HT ) synthesis and release , and increased orexin A gene expression in the hypothalamus .

Example answer:
{"entities": [{"text": "cocaine - and amphetamine - regulated transcript", "type": "AnatomicalStructure"}, {"text": "CART", "type": "AnatomicalStructure"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "serotonin", "type": "Chemical"}, {"text": "5 - hydroxytryptamine", "type": "Chemical"}, {"text": "5 - HT", "type": "Chemical"}, {"text": "synthesis", "type": "BiologicFunction"}, {"text": "orexin A", "type": "Chemical"}, {"text": "hypothalamus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Specifically , the role of leptin signaling on three different hypothalamic nuclei , the dorsomedial hypothalamus , the ventromedial hypothalamus , and the arcuate nucleus , is reviewed .

Example answer:
{"entities": [{"text": "leptin", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "hypothalamic nuclei", "type": "AnatomicalStructure"}, {"text": "dorsomedial hypothalamus", "type": "AnatomicalStructure"}, {"text": "ventromedial hypothalamus", "type": "AnatomicalStructure"}, {"text": "arcuate nucleus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Hypocretins and Arousal How the brain controls vigilance state transitions remains to be fully understood .

Example answer:
{"entities": [{"text": "Hypocretins", "type": "Chemical"}, {"text": "Arousal", "type": "BiologicFunction"}, {"text": "vigilance state", "type": "BiologicFunction"}]}

Example input:
Sentence: Lateral hypothalamus orexinergic system modulates the stress effect on pentylenetetrazol induced seizures through corticotropin releasing hormone receptor type 1 Stress is a trigger factor for seizure initiation which activates hypothalamic pituitary adrenal ( HPA ) axis as well other brain areas .

Example answer:
{"entities": [{"text": "Lateral hypothalamus orexinergic system", "type": "BodySystem"}, {"text": "modulates", "type": "SpatialConcept"}, {"text": "stress", "type": "BiologicFunction"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "seizures", "type": "Finding"}, {"text": "corticotropin releasing hormone receptor type 1", "type": "Chemical"}, {"text": "Stress", "type": "BiologicFunction"}, {"text": "trigger factor for seizure", "type": "ClinicalAttribute"}, {"text": "hypothalamic pituitary adrenal ( HPA ) axis", "type": "BodySystem"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "areas", "type": "SpatialConcept"}]}

Example input:
Sentence: Lack of function of hypocretin neurons ( a relatively simple and non - redundant neuronal system ) results in inappropriate control of sleep states without affecting the total amount of sleep or homeostatic mechanisms .

Example answer:
{"entities": [{"text": "hypocretin", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "neuronal system", "type": "BodySystem"}, {"text": "sleep", "type": "BiologicFunction"}, {"text": "homeostatic mechanisms", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , we review the role of hypocretins / orexins in arousal state transitions , and discuss possible mechanisms by which such a relatively small population of neurons controls fundamental brain state dynamics .

Example answer:
{"entities": [{"text": "hypocretins", "type": "Chemical"}, {"text": "orexins", "type": "Chemical"}, {"text": "arousal state", "type": "BiologicFunction"}, {"text": "possible", "type": "Finding"}, {"text": "relatively small", "type": "Finding"}, {"text": "population", "type": "PopulationGroup"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "brain state dynamics", "type": "BiologicFunction"}]}

Example input:
Sentence: The discovery of hypocretins , also known as orexins , and their link to narcolepsy has undoubtedly allowed us to advance our knowledge on key mechanisms controlling the boundaries and transitions between sleep and wakefulness .

Example answer:
{"entities": [{"text": "hypocretins", "type": "Chemical"}, {"text": "orexins", "type": "Chemical"}, {"text": "narcolepsy", "type": "BiologicFunction"}, {"text": "knowledge", "type": "IntellectualProduct"}, {"text": "sleep", "type": "BiologicFunction"}, {"text": "wakefulness", "type": "BiologicFunction"}]}

Input:
Sentence: Anatomical and functional evidence shows that the hypothalamic neurons that produce hypocretins / orexins project widely throughout the entire brain and interact with major neuromodulator systems in order to regulate physiological processes underlying wakefulness , attention , and emotions .

## Item MedMentions:test:2900
Example input:
Sentence: Foreign - body ingestion in Egyptian children : a 10 - year experience of endoscopic intervention in a tertiary hospital There was a lack of data about foreign body ( FB ) ingestion among Middle - East children .

Example answer:
{"entities": [{"text": "Foreign - body", "type": "InjuryOrPoisoning"}, {"text": "ingestion", "type": "BiologicFunction"}, {"text": "Egyptian", "type": "PopulationGroup"}, {"text": "experience", "type": "BiologicFunction"}, {"text": "endoscopic", "type": "HealthCareActivity"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "tertiary hospital", "type": "Organization"}, {"text": "foreign body", "type": "InjuryOrPoisoning"}, {"text": "FB", "type": "InjuryOrPoisoning"}, {"text": "Middle - East", "type": "SpatialConcept"}]}

Example input:
Sentence: To study symptom support in these cases , we performed gastrostomies on 3 patients with V180I genetic Creutzfeldt - Jakob disease ( CJD ) who had become akinetic and mute , and compared them to 14 other similar patients being fed by tube .

Example answer:
{"entities": [{"text": "symptom", "type": "Finding"}, {"text": "gastrostomies", "type": "HealthCareActivity"}, {"text": "V180I genetic Creutzfeldt - Jakob disease", "type": "BiologicFunction"}, {"text": "CJD", "type": "BiologicFunction"}, {"text": "mute", "type": "Finding"}, {"text": "fed by tube", "type": "HealthCareActivity"}]}

Example input:
Sentence: The highest rate of complications was observed in FB impacted in duodenum and those without symptoms while symptomatic cases and impaction in upper esophagus were associated with higher success rate of removal .

Example answer:
{"entities": [{"text": "complications", "type": "BiologicFunction"}, {"text": "FB", "type": "InjuryOrPoisoning"}, {"text": "duodenum", "type": "AnatomicalStructure"}, {"text": "symptoms", "type": "Finding"}, {"text": "impaction", "type": "BiologicFunction"}, {"text": "upper esophagus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Gastrointestinal features including structural malformations , motility disorders , and upper GI bleeding are major causes of morbidity in CJS .

Example answer:
{"entities": [{"text": "Gastrointestinal", "type": "SpatialConcept"}, {"text": "features", "type": "Finding"}, {"text": "structural malformations", "type": "Finding"}, {"text": "motility disorders", "type": "BiologicFunction"}, {"text": "upper GI bleeding", "type": "BiologicFunction"}, {"text": "CJS", "type": "BiologicFunction"}]}

Example input:
Sentence: This report describes the gastrointestinal and surgical findings in a baby with CJS who presented with abdominal obstruction and reviews the spectrum of gastrointestinal malformations in this rare disorder .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "gastrointestinal", "type": "SpatialConcept"}, {"text": "surgical findings", "type": "Finding"}, {"text": "CJS", "type": "BiologicFunction"}, {"text": "spectrum of gastrointestinal malformations", "type": "Finding"}, {"text": "rare disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: An upper GI endoscopy showed the catheter pulled into the duodenum causing gastric outlet obstruction .

Example answer:
{"entities": [{"text": "upper GI endoscopy", "type": "HealthCareActivity"}, {"text": "catheter", "type": "MedicalDevice"}, {"text": "pulled into", "type": "Finding"}, {"text": "duodenum", "type": "AnatomicalStructure"}, {"text": "gastric outlet obstruction", "type": "BiologicFunction"}]}

Example input:
Sentence: Multiple number of foreign bodies may be swallowed by psychiatric patients which delay diagnosis and increase the complication rate .

Example answer:
{"entities": [{"text": "foreign bodies", "type": "InjuryOrPoisoning"}, {"text": "swallowed", "type": "BiologicFunction"}, {"text": "complication", "type": "BiologicFunction"}]}

Example input:
Sentence: Long and hard objects cannot pass through the pylorus , and may cause obstruction , ulceration , bleeding and perforation .

Example answer:
{"entities": [{"text": "objects", "type": "InjuryOrPoisoning"}, {"text": "pylorus", "type": "AnatomicalStructure"}, {"text": "obstruction", "type": "BiologicFunction"}, {"text": "ulceration", "type": "BiologicFunction"}, {"text": "bleeding", "type": "BiologicFunction"}, {"text": "perforation", "type": "Finding"}]}

Example input:
Sentence: An exploratory laparatomy was performed after unsuccessful endoscopic foreign object removal in a 28 - year - old schizophrenic patient with gastric outlet obstruction due to multiple cigarette lighter swallowing .

Example answer:
{"entities": [{"text": "exploratory laparatomy", "type": "HealthCareActivity"}, {"text": "endoscopic", "type": "SpatialConcept"}, {"text": "foreign object", "type": "InjuryOrPoisoning"}, {"text": "removal", "type": "HealthCareActivity"}, {"text": "schizophrenic", "type": "BiologicFunction"}, {"text": "gastric outlet obstruction", "type": "BiologicFunction"}, {"text": "swallowing", "type": "BiologicFunction"}]}

Example input:
Sentence: Ten lighters were removed from the stomach through gastrotomy and one more lighter was removed from the descending colon by milking through the anus .

Example answer:
{"entities": [{"text": "stomach", "type": "AnatomicalStructure"}, {"text": "gastrotomy", "type": "HealthCareActivity"}, {"text": "descending colon", "type": "AnatomicalStructure"}, {"text": "milking", "type": "HealthCareActivity"}, {"text": "anus", "type": "AnatomicalStructure"}]}

Input:
Sentence: A rare cause of gastric obstruction : Lighters swallowing The majority of swallowed foreign bodies are thrown spontaneously without causing complications in the digestive system .

## Item MedMentions:test:3036
Example input:
Sentence: The activation of the TGFβ pathway in the brain of SBE / Tk - Luc mice increased 24 h after LPS injection , compared to control animals .

Example answer:
{"entities": [{"text": "activation of the TGFβ pathway", "type": "BiologicFunction"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "SBE / Tk - Luc mice", "type": "Eukaryote"}, {"text": "LPS", "type": "Chemical"}, {"text": "injection", "type": "HealthCareActivity"}, {"text": "control animals", "type": "Eukaryote"}]}

Example input:
Sentence: Don extract inhibits the tumor growth through down - regulating of Treg cells and manipulating Th1 / Th17 immune response in hepatoma H22 -bearing mice Previous studies showed Scutellaria barbata D .

Example answer:
{"entities": [{"text": "Don extract", "type": "Chemical"}, {"text": "down - regulating", "type": "BiologicFunction"}, {"text": "Treg cells", "type": "AnatomicalStructure"}, {"text": "manipulating", "type": "BiologicFunction"}, {"text": "Th1", "type": "BiologicFunction"}, {"text": "Th17 immune response", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "Scutellaria barbata D .", "type": "Chemical"}]}

Example input:
Sentence: 01 ) whereas increased IL - 2 and IFN - γ levels ( P < 0 . 01 ) in the serum of hepatoma H22 -bearing mice .

Example answer:
{"entities": [{"text": "IL - 2", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "serum", "type": "BodySubstance"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: No hepatorenal toxicity was observed in H22 tumor - bearing mice .

Example answer:
{"entities": [{"text": "No hepatorenal toxicity", "type": "Finding"}, {"text": "H22 tumor - bearing mice", "type": "BiologicFunction"}]}

Example input:
Sentence: Moreover , administration of recombinant mouse IL - 17A reversed the anti - tumor effects of SBE .

Example answer:
{"entities": [{"text": "recombinant mouse", "type": "Eukaryote"}, {"text": "IL - 17A", "type": "Chemical"}, {"text": "SBE", "type": "Chemical"}]}

Example input:
Sentence: Don extract ( SBE ) is a potent inhibitor in hepatoma and could improve immune function of hepatoma H22 -bearing mice .

Example answer:
{"entities": [{"text": "Don extract", "type": "Chemical"}, {"text": "SBE", "type": "Chemical"}, {"text": "inhibitor", "type": "Chemical"}, {"text": "hepatoma", "type": "BiologicFunction"}, {"text": "immune function", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: However , the immunomodulatory function of SBE on the tumor growth of hepatoma remains unclear .

Example answer:
{"entities": [{"text": "immunomodulatory function", "type": "BiologicFunction"}, {"text": "SBE", "type": "Chemical"}, {"text": "hepatoma", "type": "BiologicFunction"}]}

Example input:
Sentence: The effect of SBE on the proliferation of HepG2 cells in vitro , the growth of transplanted tumor , the cytotoxicity of natural killer ( NK ) cells in spleen , the amount of CD4 ( + ) CD25 ( + ) Foxp3 ( + ) Treg cells and Th17 cells in tumor tissue , and the levels of IL - 10 , TGF - β , IL - 17A , IL - 2 , and IFN - γ in serum of the hepatoma H22 -bearing mice was observered .

Example answer:
{"entities": [{"text": "SBE", "type": "Chemical"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "HepG2 cells", "type": "AnatomicalStructure"}, {"text": "cytotoxicity of natural killer ( NK ) cells", "type": "BiologicFunction"}, {"text": "spleen", "type": "AnatomicalStructure"}, {"text": "CD4 ( + ) CD25 ( + ) Foxp3 ( + ) Treg cells", "type": "Chemical"}, {"text": "Th17 cells", "type": "AnatomicalStructure"}, {"text": "tumor tissue", "type": "AnatomicalStructure"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "TGF - β", "type": "Chemical"}, {"text": "IL - 17A", "type": "Chemical"}, {"text": "IL - 2", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "serum", "type": "BodySubstance"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: SBE treatment inhibited the proliferation of HepG2 cells in vitro with a dose - dependent manner and significantly suppressed the tumor growth of hepatoma H22 -bearing mice .

Example answer:
{"entities": [{"text": "SBE", "type": "Chemical"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "HepG2 cells", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Meanwhile , SBE also could inhibit the growth of H22 implanted tumor in hepatoma H22 -bearing mice , and this function might be associated with immunomodulatory activity through down - regulating of Treg cells and manipulating Th1 / Th17 immune response .

Example answer:
{"entities": [{"text": "SBE", "type": "Chemical"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "implanted tumor", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "immunomodulatory activity", "type": "BiologicFunction"}, {"text": "down - regulating", "type": "BiologicFunction"}, {"text": "Treg cells", "type": "AnatomicalStructure"}, {"text": "manipulating", "type": "BiologicFunction"}, {"text": "Th1", "type": "BiologicFunction"}, {"text": "Th17 immune response", "type": "BiologicFunction"}]}

Input:
Sentence: This study aimed to investigate the anti - tumor effects of SBE on hepatoma H22 -bearing mice and explore the underlying immunomodulatory function .

## Item MedMentions:test:3192
Example input:
Sentence: In CD and UC patients , V was 49 % and 52 % higher than in AS , respectively , and CL was 47 % and 60 % higher than in AS , respectively .

Example answer:
{"entities": [{"text": "CD", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}, {"text": "AS", "type": "BiologicFunction"}]}

Example input:
Sentence: Compared to cognitively preserved ( CP ) , CI patients had higher T2 WM lesion volume ( LV ) , lower NBV and GMV , and more severe diffusivity abnormalities in WM lesions , cortex , and NAWM .

Example answer:
{"entities": [{"text": "CI", "type": "BiologicFunction"}, {"text": "abnormalities", "type": "AnatomicalStructure"}, {"text": "WM lesions", "type": "Finding"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "NAWM", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In addition , the CR rate was significantly increased in patients carrying one or two ERCC1 - 118 C alleles ( C / C or C / T genotype ) compared with patients lacking the C allele ( T / T genotype ) .

Example answer:
{"entities": [{"text": "CR", "type": "Finding"}, {"text": "ERCC1 - 118", "type": "AnatomicalStructure"}, {"text": "alleles", "type": "AnatomicalStructure"}, {"text": "C", "type": "Chemical"}, {"text": "T", "type": "Chemical"}, {"text": "allele", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Patients who achieved cCR had significantly longer OS in comparison with patients achieving clinical partial response ( cPR ) and clinical stable disease ( cSD ) .

Example answer:
{"entities": [{"text": "achieved", "type": "Finding"}, {"text": "cCR", "type": "Finding"}, {"text": "clinical partial response", "type": "Finding"}, {"text": "cPR", "type": "Finding"}, {"text": "clinical stable disease", "type": "Finding"}, {"text": "cSD", "type": "Finding"}]}

Example input:
Sentence: In fact , we found an inverse relationship between the TDI and CRC stage , an example of the " waiting time paradox " .

Example answer:
{"entities": [{"text": "CRC", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients ≥70 years were more often treated with less toxic chemotherapy , yet experienced higher rates of hospitalization during treatment and increased rates of acute mortality following CRT .

Example answer:
{"entities": [{"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "hospitalization", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "CRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: It was found that the short - term therapeutic efficacy ( CR rate ) was higher in the group of patients carrying the homozygous mutation of XRCC1 - 399 ( A / A genotype ) than in the group of patients without the XRCC1 - 399 mutation ( G / G genotype ) .

Example answer:
{"entities": [{"text": "CR", "type": "Finding"}, {"text": "homozygous mutation", "type": "BiologicFunction"}, {"text": "XRCC1 - 399", "type": "AnatomicalStructure"}, {"text": "A", "type": "Chemical"}, {"text": "mutation", "type": "BiologicFunction"}, {"text": "G", "type": "Chemical"}]}

Example input:
Sentence: Patients ≥70 had an increased risk of death at 3 months following CRT ( odds ratio 5 . 19 , 95 % CI 1 . 64 - 16 . 41 ; p = 0 . 005 ) and worse survival over time ( hazard ratio 2 .

Example answer:
{"entities": [{"text": "death", "type": "Finding"}, {"text": "CRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: The TDIs of patients with different stages of CRC were also compared using the Kruskal - Wallis test .

Example answer:
{"entities": [{"text": "CRC", "type": "BiologicFunction"}, {"text": "Kruskal - Wallis test", "type": "IntellectualProduct"}]}

Example input:
Sentence: Univariate analysis indicated that the TDI was greater in those with less advanced CRC for all 3 methods of calculation , but this association was only statistically significant for the HR - TDI ( p = 0 . 021 ) .

Example answer:
{"entities": [{"text": "CRC", "type": "BiologicFunction"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "HR", "type": "IntellectualProduct"}]}

Input:
Sentence: There is no evidence that patients with more advanced CRC have longer TDIs .

## Item MedMentions:test:2875
Example input:
Sentence: At different time points after injection , we assessed locomotor function with a 24 - point neurologic deficit scoring system and the rotarod test ; assessed recognition memory with the novel object recognition test ; and assessed emotional abnormality ( anhedonia and behavioral despair ) with the tail suspension test , forced swim test , and sucrose preference test .

Example answer:
{"entities": [{"text": "injection", "type": "HealthCareActivity"}, {"text": "locomotor function", "type": "BiologicFunction"}, {"text": "24 - point neurologic deficit scoring system", "type": "IntellectualProduct"}, {"text": "rotarod test", "type": "ResearchActivity"}, {"text": "recognition", "type": "BiologicFunction"}, {"text": "memory", "type": "BiologicFunction"}, {"text": "recognition test", "type": "IntellectualProduct"}, {"text": "emotional abnormality", "type": "BiologicFunction"}, {"text": "anhedonia", "type": "BiologicFunction"}, {"text": "behavioral despair", "type": "BiologicFunction"}, {"text": "tail suspension test", "type": "HealthCareActivity"}, {"text": "forced swim test", "type": "HealthCareActivity"}, {"text": "sucrose preference test", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here we traced the dynamics of distinct abstract and effector - selective decision signals in the form of the broad - band centro - parietal positivity ( CPP ) and limb - selective β - band ( 8 - 16 and 18 - 30 Hz ) EEG activity , respectively , during delayed - reported motion direction decisions with and without foreknowledge of direction - response mapping .

Example answer:
{"entities": [{"text": "traced", "type": "Finding"}, {"text": "abstract", "type": "BiologicFunction"}, {"text": "centro - parietal positivity", "type": "Finding"}, {"text": "CPP", "type": "Finding"}, {"text": "limb - selective β - band", "type": "Finding"}, {"text": "EEG", "type": "HealthCareActivity"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "motion direction", "type": "SpatialConcept"}, {"text": "decisions", "type": "BiologicFunction"}, {"text": "direction", "type": "SpatialConcept"}]}

Example input:
Sentence: Evidence was found in favor of an area - shift , rather than a peak - shift effect , which implies that the peak conditioned fear response extended to , but did not shift to a novel stimulus .

Example answer:
{"entities": [{"text": "conditioned fear response", "type": "BiologicFunction"}]}

Example input:
Sentence: There is great variance in the propensity to generalize as well as the speed of extinction learning when these novel movements are not followed by pain .

Example answer:
{"entities": [{"text": "generalize", "type": "BiologicFunction"}, {"text": "extinction learning", "type": "BiologicFunction"}, {"text": "movements", "type": "BiologicFunction"}, {"text": "pain", "type": "Finding"}]}

Example input:
Sentence: Low inhibitory capacity is not associated with slower generalization , but extinction of fear generalization .

Example answer:
{"entities": [{"text": "Low inhibitory capacity", "type": "BiologicFunction"}, {"text": "generalization", "type": "BiologicFunction"}, {"text": "extinction", "type": "BiologicFunction"}, {"text": "fear", "type": "BiologicFunction"}]}

Example input:
Sentence: Anesthesia resulted in long - term neurobehavioral changes in the fear conditioning task carried out 65 days after exposure to anesthesia in 3xTg - AD mice .

Example answer:
{"entities": [{"text": "Anesthesia", "type": "HealthCareActivity"}, {"text": "3xTg - AD mice", "type": "Eukaryote"}]}

Example input:
Sentence: Changes in anticipatory anxiety , agoraphobic fear / avoidance , and somatization were significant predictors of changes in some aspects of QOL .

Example answer:
{"entities": [{"text": "anticipatory anxiety", "type": "Finding"}, {"text": "agoraphobic fear", "type": "BiologicFunction"}, {"text": "avoidance", "type": "BiologicFunction"}, {"text": "somatization", "type": "BiologicFunction"}]}

Example input:
Sentence: It can be argued that this variance may be associated with executive function capacity , as individuals may be unable to intentionally inhibit fear responses .

Example answer:
{"entities": [{"text": "executive function capacity", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "inhibit fear responses", "type": "BiologicFunction"}]}

Example input:
Sentence: Low inhibitory capacity was associated with slower extinction of generalized fear of movement - related pain and pain expectancy .

Example answer:
{"entities": [{"text": "Low inhibitory capacity", "type": "BiologicFunction"}, {"text": "extinction", "type": "BiologicFunction"}, {"text": "generalized fear", "type": "BiologicFunction"}, {"text": "pain", "type": "Finding"}]}

Example input:
Sentence: This study examined whether executive function capacity contributes to generalization and extinction of generalization as well as peak - shift of conditioned fear of movement - related pain and expectancy .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "executive function capacity", "type": "BiologicFunction"}, {"text": "generalization", "type": "BiologicFunction"}, {"text": "extinction", "type": "BiologicFunction"}]}

Input:
Sentence: Executive function tests assessing updating , switching , and inhibition were used to predict changes in ( extinction of ) fear of movement - related pain and pain expectancy generalization .

## Item MedMentions:test:2742
Example input:
Sentence: The majority of hospice staff and volunteers used personally meaningful rituals after the death of their patients to help them cope ( 71 % ) .

Example answer:
{"entities": [{"text": "hospice", "type": "HealthCareActivity"}, {"text": "volunteers", "type": "PopulationGroup"}, {"text": "death", "type": "BiologicFunction"}]}

Example input:
Sentence: Twenty four community nurses implemented the dignity care intervention for people with advanced and life - limiting conditions were recruited from four pilot sites across Ireland .

Example answer:
{"entities": [{"text": "community nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "people", "type": "PopulationGroup"}, {"text": "life - limiting conditions", "type": "Finding"}, {"text": "Ireland", "type": "SpatialConcept"}]}

Example input:
Sentence: An effective continuum of care model may benefit from greater attention to patient 's perceived refusal self - efficacy during detoxification which may impact preference for MAT and long - term recovery .

Example answer:
{"entities": [{"text": "continuum of care model", "type": "HealthCareActivity"}, {"text": "attention", "type": "BiologicFunction"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "detoxification", "type": "HealthCareActivity"}, {"text": "MAT", "type": "HealthCareActivity"}, {"text": "recovery", "type": "BiologicFunction"}]}

Example input:
Sentence: It important to note that the new CEO ( the author ) found LifeShare possessed numerous significant assets upon which to build .

Example answer:
{"entities": [{"text": "CEO", "type": "ProfessionalOrOccupationalGroup"}, {"text": "author", "type": "ProfessionalOrOccupationalGroup"}, {"text": "LifeShare", "type": "HealthCareActivity"}]}

Example input:
Sentence: Melding a High - Risk Patient for Continuous Flow Left Ventricular Assist Device into a Low - Risk Patient The model for end - stage liver disease ( MELD ) has been used as a predictor of mortality after left ventricular assist device ( LVAD ) placement .

Example answer:
{"entities": [{"text": "Continuous Flow Left Ventricular Assist Device", "type": "MedicalDevice"}, {"text": "model for end - stage liver disease", "type": "IntellectualProduct"}, {"text": "MELD", "type": "IntellectualProduct"}, {"text": "predictor", "type": "IntellectualProduct"}, {"text": "left ventricular assist device", "type": "MedicalDevice"}, {"text": "LVAD", "type": "MedicalDevice"}, {"text": "placement", "type": "HealthCareActivity"}]}

Example input:
Sentence: The participants ' expectations about counselling with regard to longer - term family , practical , and financial challenges were insufficiently met by the CMHC .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "counselling", "type": "HealthCareActivity"}, {"text": "family", "type": "Finding"}, {"text": "practical", "type": "Finding"}, {"text": "financial challenges", "type": "Finding"}, {"text": "CMHC", "type": "Organization"}]}

Example input:
Sentence: Permanence can be Defended In donation after the circulatory - respiratory determination of death ( DCDD ) , the dead donor rule requires that the donor be dead before organ procurement can proceed .

Example answer:
{"entities": [{"text": "circulatory - respiratory determination of death", "type": "HealthCareActivity"}, {"text": "DCDD", "type": "HealthCareActivity"}, {"text": "dead", "type": "BiologicFunction"}, {"text": "donor", "type": "PopulationGroup"}, {"text": "rule", "type": "IntellectualProduct"}, {"text": "organ procurement", "type": "HealthCareActivity"}]}

Example input:
Sentence: This OPO , LifeShare Transplant Donor Services of Oklahoma ( LifeShare ) , had just celebrated its 25th anniversary in 2011 .

Example answer:
{"entities": [{"text": "OPO", "type": "Organization"}, {"text": "LifeShare Transplant Donor Services", "type": "HealthCareActivity"}, {"text": "Oklahoma", "type": "SpatialConcept"}, {"text": "LifeShare", "type": "HealthCareActivity"}]}

Example input:
Sentence: From 2008 through 2011 , the four years prior to the organization beginning its change journey , LifeShare recovered 344 organ donors from which 1 , 007 organs were transplanted in 48 months .

Example answer:
{"entities": [{"text": "organization", "type": "Organization"}, {"text": "LifeShare", "type": "HealthCareActivity"}, {"text": "organ donors", "type": "PopulationGroup"}, {"text": "organs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: While LifeShare was well - established chronologically , growth in organ donors and organs transplanted from these donors had occurred at a much slower rate during the collaborative era and afterward ( 2003 - 2011 ) than the donor / transplant growth the United States ( US ) , as a whole , had experienced .

Example answer:
{"entities": [{"text": "LifeShare", "type": "HealthCareActivity"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "organ donors", "type": "PopulationGroup"}, {"text": "organs", "type": "AnatomicalStructure"}, {"text": "donors", "type": "PopulationGroup"}, {"text": "donor", "type": "PopulationGroup"}, {"text": "transplant", "type": "HealthCareActivity"}, {"text": "United States", "type": "SpatialConcept"}, {"text": "US", "type": "SpatialConcept"}]}

Input:
Sentence: As LifeShare ' s team began to identify pockets of unrealized potential donors , recognized best practices were deployed to areas of opportunity , including responding to all vented referrals , implementation of dedicated family requestors , broadening of already - existing in - house coordinator programs , and aggressive expansion of the donors after cardiac death ( DCD ) program .

## Item MedMentions:test:2905
Example input:
Sentence: Targeted - NGS on genes commonly mutated in IPMN and PDAC was performed on tumors from ( 1 ) 13 patients who developed disease progression in the remnant pancreas following resection of IPMN ; and ( 2 ) 10 patients who underwent a resection for PDAC and had a concomitant IPMN .

Example answer:
{"entities": [{"text": "Targeted - NGS", "type": "ResearchActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "mutated", "type": "BiologicFunction"}, {"text": "IPMN", "type": "BiologicFunction"}, {"text": "PDAC", "type": "BiologicFunction"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "disease progression", "type": "BiologicFunction"}, {"text": "remnant", "type": "AnatomicalStructure"}, {"text": "pancreas", "type": "AnatomicalStructure"}, {"text": "resection", "type": "HealthCareActivity"}]}

Example input:
Sentence: This study highlights the practicality and versatility of albumin -mediated biomimetic mineralization of a nanotheranostic agent and also suggests that bioinspired Gd : CuS @ BSA NPs possess promising imaging guidance and effective tumor ablation properties , with high spatial resolution and deep tissue penetration .

Example answer:
{"entities": [{"text": "albumin", "type": "Chemical"}, {"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "BSA", "type": "Chemical"}, {"text": "imaging guidance", "type": "HealthCareActivity"}, {"text": "tumor ablation properties", "type": "HealthCareActivity"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In conclusion , our results show that the modulation of HOP - PrP ( C ) engagement or the decrease of PrP ( C ) and HOP expression may represent a potential therapeutic intervention in GBM , regulating glioblastoma stem - like cell self - renewal , proliferation , and migration .

Example answer:
{"entities": [{"text": "HOP", "type": "Chemical"}, {"text": "PrP ( C )", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "therapeutic intervention", "type": "HealthCareActivity"}, {"text": "GBM", "type": "BiologicFunction"}, {"text": "glioblastoma stem - like cell", "type": "AnatomicalStructure"}, {"text": "self - renewal", "type": "BiologicFunction"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "migration", "type": "BiologicFunction"}]}

Example input:
Sentence: This work also showed the efficacy of AgNPs against lung cancer cell lines ( A549 ) and cervical cancer cell line ( HeLa ) , in vitro .

Example answer:
{"entities": [{"text": "lung", "type": "AnatomicalStructure"}, {"text": "cancer cell lines", "type": "AnatomicalStructure"}, {"text": "A549", "type": "AnatomicalStructure"}, {"text": "cervical", "type": "AnatomicalStructure"}, {"text": "cancer cell line", "type": "AnatomicalStructure"}, {"text": "HeLa", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In this study , lipid - polymer hybrid nanoparticles ( LPNs ) , which contain both pemetrexed and miR - 21 antisense oligonucleotide ( anti - miR - 21 ) , have been developed for treatment of glioblastoma , the most aggressive type of brain tumor .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "lipid", "type": "Chemical"}, {"text": "polymer", "type": "Chemical"}, {"text": "LPNs", "type": "Chemical"}, {"text": "pemetrexed", "type": "Chemical"}, {"text": "miR - 21 antisense oligonucleotide", "type": "Chemical"}, {"text": "anti - miR - 21", "type": "Chemical"}, {"text": "glioblastoma", "type": "BiologicFunction"}, {"text": "brain tumor", "type": "BiologicFunction"}]}

Example input:
Sentence: As compared to GNS - mPEG , the cellular internalization of GNS - pHLIP was 1 - fold higher after a 2 h incubation with cells in media at pH 6 .

Example answer:
{"entities": [{"text": "GNS", "type": "Chemical"}, {"text": "mPEG", "type": "Chemical"}, {"text": "pHLIP", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Furthermore , GNS - pHLIP exhibited stronger signals than the GNS - mPEG through computed tomography ( CT ) and photoacoustic ( PA ) imaging .

Example answer:
{"entities": [{"text": "GNS", "type": "Chemical"}, {"text": "pHLIP", "type": "Chemical"}, {"text": "mPEG", "type": "Chemical"}, {"text": "computed tomography", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "photoacoustic ( PA ) imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here , we innovatively decorated gold nanostars ( GNSs ) with pHLIPs ( GNS - pHLIP ) to improve their targeting ability and photothermal therapeutic ( PTT ) efficiency .

Example answer:
{"entities": [{"text": "gold nanostars", "type": "Chemical"}, {"text": "GNSs", "type": "Chemical"}, {"text": "pHLIPs", "type": "Chemical"}, {"text": "GNS", "type": "Chemical"}, {"text": "pHLIP", "type": "Chemical"}, {"text": "photothermal therapeutic", "type": "HealthCareActivity"}, {"text": "PTT", "type": "HealthCareActivity"}]}

Example input:
Sentence: The obtained GNS - pHLIP exhibited the excellent characteristics of uniform size and good biocompatibility .

Example answer:
{"entities": [{"text": "GNS", "type": "Chemical"}, {"text": "pHLIP", "type": "Chemical"}, {"text": "size", "type": "SpatialConcept"}]}

Example input:
Sentence: Moreover , the tumor accumulation of the GNS - pHLIP was 3 - fold higher than that of GNS - mPEG after intravenous injection into MCF - 7 breast tumor animal models for 24 h .

Example answer:
{"entities": [{"text": "tumor", "type": "BiologicFunction"}, {"text": "accumulation", "type": "Finding"}, {"text": "GNS", "type": "Chemical"}, {"text": "pHLIP", "type": "Chemical"}, {"text": "mPEG", "type": "Chemical"}, {"text": "MCF - 7", "type": "AnatomicalStructure"}, {"text": "breast tumor", "type": "BiologicFunction"}, {"text": "animal models", "type": "BiologicFunction"}]}

Input:
Sentence: The results clearly demonstrate that the GNS - pHLIP successfully took advantage of the tumor - targeting ability of pHLIPs and the good characteristics of GNS s , which may contribute to the study of tumor imaging and therapy .

## Item MedMentions:test:3050
Example input:
Sentence: yakuba as an outgroup , we found clear evidence for selection on 4 - fold sites along both lineages over a substantial period , with the intensity of selection increasing with GC content .

Example answer:
{"entities": [{"text": "yakuba", "type": "Eukaryote"}, {"text": "selection", "type": "BiologicFunction"}, {"text": "sites", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Phylogenetic tree based on 16S rRNA gene sequences indicated that strain EGI 6500337 T formed a distinct lineage in the cluster that comprised the genera Aurantimonas and Aureimonas in the family Aurantimonadaceae .

Example answer:
{"entities": [{"text": "16S rRNA", "type": "Chemical"}, {"text": "gene sequences", "type": "SpatialConcept"}, {"text": "strain EGI 6500337 T", "type": "Bacterium"}, {"text": "genera Aurantimonas", "type": "Bacterium"}, {"text": "Aureimonas", "type": "Bacterium"}, {"text": "family Aurantimonadaceae", "type": "Bacterium"}]}

Example input:
Sentence: Comparative analyses revealed signatures of duplication events , intron number and length variation , and varying intronic ORFs which highlighted the genetic diversity of mt genomes among the Cryphonectriaceae .

Example answer:
{"entities": [{"text": "duplication", "type": "BiologicFunction"}, {"text": "intron", "type": "Chemical"}, {"text": "intronic", "type": "Chemical"}, {"text": "ORFs", "type": "AnatomicalStructure"}, {"text": "mt genomes", "type": "AnatomicalStructure"}, {"text": "Cryphonectriaceae", "type": "Eukaryote"}]}

Example input:
Sentence: Due to the strong support and consistent topology provided by all UCE analyses , we have identified phylogenetic relationships of these three enigmatic , poorly - studied , phasianid taxa .

Example answer:
{"entities": [{"text": "phasianid taxa", "type": "Eukaryote"}]}

Example input:
Sentence: In all mitogenome analyses , Pucrasia was sister to a clade including Perdix and the typical pheasants with high support , in contrast to UCEs and published nuclear intron data .

Example answer:
{"entities": [{"text": "mitogenome analyses", "type": "HealthCareActivity"}, {"text": "Pucrasia", "type": "Eukaryote"}, {"text": "clade", "type": "Eukaryote"}, {"text": "Perdix", "type": "Eukaryote"}, {"text": "pheasants", "type": "Eukaryote"}, {"text": "published nuclear intron data", "type": "IntellectualProduct"}]}

Example input:
Sentence: However , these studies have largely ignored three enigmatic genera because of scarce DNA source material and limited overlapping phylogenetic data : blood pheasants ( Ithaginis ) , snow partridges ( Lerwa ) , and long - billed partridges ( Rhizothera ) .

Example answer:
{"entities": [{"text": "DNA", "type": "Chemical"}, {"text": "source material", "type": "Finding"}, {"text": "phylogenetic data", "type": "IntellectualProduct"}, {"text": "blood pheasants", "type": "Eukaryote"}, {"text": "Ithaginis", "type": "Eukaryote"}, {"text": "snow partridges", "type": "Eukaryote"}, {"text": "Lerwa", "type": "Eukaryote"}, {"text": "long - billed partridges", "type": "Eukaryote"}, {"text": "Rhizothera", "type": "Eukaryote"}]}

Example input:
Sentence: Unpartitioned and codon - based analyses placed Rhizothera sister to a tragopan clade , whereas a partitioned DNA model of the mitogenome was congruent with UCE results .

Example answer:
{"entities": [{"text": "codon - based analyses", "type": "HealthCareActivity"}, {"text": "Rhizothera", "type": "Eukaryote"}, {"text": "tragopan clade", "type": "Eukaryote"}, {"text": "DNA model", "type": "IntellectualProduct"}, {"text": "mitogenome", "type": "AnatomicalStructure"}, {"text": "UCE results", "type": "Finding"}]}

Example input:
Sentence: Maximum likelihood and multispecies coalescent UCE analyses strongly supported Lerwa sister to a large clade which included Ithaginis at its base , and also including turkey , grouse , typical pheasants , tragopans , Pucrasia , and Perdix .

Example answer:
{"entities": [{"text": "Lerwa", "type": "Eukaryote"}, {"text": "large clade", "type": "Eukaryote"}, {"text": "Ithaginis", "type": "Eukaryote"}, {"text": "turkey", "type": "Eukaryote"}, {"text": "grouse", "type": "Eukaryote"}, {"text": "pheasants", "type": "Eukaryote"}, {"text": "tragopans", "type": "Eukaryote"}, {"text": "Pucrasia", "type": "Eukaryote"}, {"text": "Perdix", "type": "Eukaryote"}]}

Example input:
Sentence: Previous studies using different data types place Lerwa and Ithaginis in similar positions , but the absence of overlapping data means the relationship between them could not be inferred .

Example answer:
{"entities": [{"text": "Lerwa", "type": "Eukaryote"}, {"text": "Ithaginis", "type": "Eukaryote"}]}

Example input:
Sentence: To identify robust relationships among Ithaginis , Lerwa , Rhizothera , and their phasianid relatives , we used 3692 ultra - conserved element ( UCE ) loci and complete mitogenomes from 19 species including previously hypothesized relatives of the three focal genera and representatives from all major phasianid clades .

Example answer:
{"entities": [{"text": "Ithaginis", "type": "Eukaryote"}, {"text": "Lerwa", "type": "Eukaryote"}, {"text": "Rhizothera", "type": "Eukaryote"}, {"text": "phasianid relatives", "type": "Eukaryote"}, {"text": "ultra - conserved element ( UCE ) loci", "type": "AnatomicalStructure"}, {"text": "mitogenomes", "type": "AnatomicalStructure"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "phasianid clades", "type": "Eukaryote"}]}

Input:
Sentence: Mitogenomic genealogies differed from UCEs topologies , supporting a sister relationship between Ithaginis and Lerwa rather than a grade .

## Item MedMentions:test:3289
Example input:
Sentence: In this regard , bioinspired polymer hydrogels offer an attractive and abundant source of coating materials .

Example answer:
{"entities": [{"text": "polymer", "type": "Chemical"}, {"text": "hydrogels", "type": "Chemical"}, {"text": "source", "type": "Finding"}, {"text": "coating materials", "type": "Chemical"}]}

Example input:
Sentence: Our findings highlight the key role of surface chemistry in cell - multilayer film interactions , and these engineered nanocoatings represent a tunable model of cell adhesive and non - adhesive multilayered films .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "cell", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Recent coating developments for combination devices in orthopedic and dental applications : A literature review Orthopedic and dental implants have been used successfully for decades to replace or repair missing or damaged bones , joints , and teeth , thereby restoring patient function subsequent to disease or injury .

Example answer:
{"entities": [{"text": "combination devices", "type": "MedicalDevice"}, {"text": "orthopedic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "dental applications", "type": "HealthCareActivity"}, {"text": "literature review", "type": "IntellectualProduct"}, {"text": "Orthopedic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "dental implants", "type": "MedicalDevice"}, {"text": "repair", "type": "HealthCareActivity"}, {"text": "bones", "type": "AnatomicalStructure"}, {"text": "joints", "type": "SpatialConcept"}, {"text": "teeth", "type": "AnatomicalStructure"}, {"text": "restoring", "type": "HealthCareActivity"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: This methodology offers a facile route to functionalizing implantable sensor systems with antifouling coatings that improve hemocompatibility and pave the way for enhanced device integration in tissue .

Example answer:
{"entities": [{"text": "implantable sensor systems", "type": "MedicalDevice"}, {"text": "antifouling", "type": "Finding"}, {"text": "device", "type": "MedicalDevice"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: It appears that advances in instrumentation , materials and technology have finally delivered it .

Example answer:
{"entities": []}

Example input:
Sentence: Many different types of surface coatings have been developed to address these shortcomings , including those that incorporate therapeutic agents to provide localized delivery to the surgical site .

Example answer:
{"entities": [{"text": "surface", "type": "SpatialConcept"}, {"text": "therapeutic agents", "type": "Chemical"}, {"text": "localized", "type": "SpatialConcept"}, {"text": "surgical site", "type": "SpatialConcept"}]}

Example input:
Sentence: e . , those published in the last 2 - 3years , with a particular focus on technologies that have potential for overcoming the most significant challenges facing therapeutically - loaded coatings .

Example answer:
{"entities": [{"text": "particular focus", "type": "BiologicFunction"}, {"text": "challenges", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Some of the primary challenges related to current coatings are non - optimal release kinetics , which most often are too rapid , the potential for inducing antibiotic resistance in target organisms , high susceptibility to mechanical abrasion and delamination , toxicity , difficult and expensive regulatory approval pathways , and high manufacturing costs .

Example answer:
{"entities": [{"text": "challenges", "type": "ClinicalAttribute"}, {"text": "antibiotic resistance", "type": "BiologicFunction"}, {"text": "delamination", "type": "HealthCareActivity"}]}

Example input:
Sentence: The significant amount of research currentl y being conducted in the field provides a level of optimism that many functional combination coating s will ultimately transition into clinical practice , significant ly improving patient outcomes .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "optimism", "type": "BiologicFunction"}]}

Example input:
Sentence: While these coatings hold enormous potential for improving device function , the list of requirements that an ideal combination coating must fulfill is extensive , and no single coating system today simultaneously addresses all of the criteria .

Example answer:
{"entities": [{"text": "device", "type": "MedicalDevice"}]}

Input:
Sentence: It is concluded that the ideal coating remains an unrealized target , but that advances in the field and emerging technologies are bringing it closer to reality .

## Item MedMentions:test:3306
Example input:
Sentence: EudraCT ( N ° : 2012 - 005225 - 69 ) ; ClinicalTrials . gov ( NCT01828788 ) .

Example answer:
{"entities": [{"text": "ClinicalTrials . gov", "type": "IntellectualProduct"}]}

Example input:
Sentence: gov ( Identifier : NCT01921088 ) https : / / clinicaltrials . gov / ct2 / show / NCT01921088 .

Example answer:
{"entities": []}

Example input:
Sentence: ClinicalTrials . gov , registered on March 12 , 2014 , identifier : NCT02087592 . World Health Organization Trial Registration , registered on 3 August 2015 , identifier : NCT02087592 .

Example answer:
{"entities": [{"text": "World Health Organization", "type": "Organization"}]}

Example input:
Sentence: NCT01912742 ( the study was registered in clinicaltrial . gov ) .

Example answer:
{"entities": []}

Example input:
Sentence: ClinicalTrials . gov as # NCT01501149 .

Example answer:
{"entities": [{"text": "ClinicalTrials . gov", "type": "IntellectualProduct"}]}

Example input:
Sentence: ClinicalTrials . gov registration number : NCT00400738 .

Example answer:
{"entities": [{"text": "ClinicalTrials . gov registration number : NCT00400738", "type": "ResearchActivity"}]}

Example input:
Sentence: ClinicalTrials . gov ( NCT01748929 ) .

Example answer:
{"entities": []}

Example input:
Sentence: ClinicalTrials . gov Identifier NCT01973907 , registered on 23 October 2013 .

Example answer:
{"entities": []}

Example input:
Sentence: Clinicaltrials . gov : NCT01335971 .

Example answer:
{"entities": []}

Example input:
Sentence: ClinicalTrials .Gov Identifier : NCT01383954 .

Example answer:
{"entities": [{"text": "ClinicalTrials", "type": "ResearchActivity"}]}

Input:
Sentence: ClinicalTrials . gov Identifier : NCT01470469 .

## Item MedMentions:test:2962
Example input:
Sentence: Biogeochemical Controls of Uranium Bioavailability from the Dissolved Phase in Natural Freshwaters To gain insights into the risks associated with uranium ( U ) mining and processing , we investigated the biogeochemical controls of U bioavailability in the model freshwater species Lymnaea stagnalis ( Gastropoda ) .

Example answer:
{"entities": [{"text": "Uranium", "type": "Chemical"}, {"text": "uranium", "type": "Chemical"}, {"text": "U", "type": "Chemical"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Lymnaea stagnalis", "type": "Eukaryote"}, {"text": "Gastropoda", "type": "Eukaryote"}]}

Example input:
Sentence: Based on a field experiment , the shifts in soil microbial metabolic activities and community structures under five irrigation salinities were studied using Biolog and metagenomic methods in this study .

Example answer:
{"entities": [{"text": "salinities", "type": "Finding"}, {"text": "Biolog and metagenomic methods", "type": "IntellectualProduct"}]}

Example input:
Sentence: Application of FluorMod to surface waters of streams within the Neuse River Basin showed while > 70 % of DON was attributed to natural sources , non - point sources , such as soil and poultry litter leachates and street runoff , accounted for the remaining 30 % .

Example answer:
{"entities": [{"text": "FluorMod", "type": "IntellectualProduct"}, {"text": "waters", "type": "Chemical"}, {"text": "DON", "type": "Chemical"}, {"text": "sources", "type": "Finding"}, {"text": "poultry", "type": "Eukaryote"}, {"text": "leachates", "type": "Chemical"}]}

Example input:
Sentence: Did municipal solid waste landfill have obvious influence on polychlorinated dibenzo - p - dioxins and polychlorinated dibenzofurans ( PCDD / Fs ) in ambient air : A case study in East China Municipal solid waste ( MSW ) landfill was a main way to disposal of MSW and almost 95 % of MSW was disposed by landfills in the world .

Example answer:
{"entities": [{"text": "landfill", "type": "SpatialConcept"}, {"text": "polychlorinated dibenzo - p - dioxins", "type": "Chemical"}, {"text": "polychlorinated dibenzofurans", "type": "Chemical"}, {"text": "PCDD", "type": "Chemical"}, {"text": "Fs", "type": "Chemical"}, {"text": "case study", "type": "IntellectualProduct"}, {"text": "East China", "type": "SpatialConcept"}, {"text": "landfills", "type": "SpatialConcept"}, {"text": "world", "type": "PopulationGroup"}]}

Example input:
Sentence: Results show that dissolved U is bioavailable under all the geochemical conditions tested .

Example answer:
{"entities": [{"text": "Results", "type": "Finding"}, {"text": "dissolved U", "type": "Chemical"}]}

Example input:
Sentence: Bioavailability of dissolved U ( VI ) was characterized in controlled laboratory experiments over a range of water hardness , pH , and in the presence of complexing ligands in the form of dissolved natural organic matter ( DOM ) .

Example answer:
{"entities": [{"text": "dissolved U ( VI )", "type": "Chemical"}, {"text": "laboratory", "type": "Organization"}, {"text": "experiments", "type": "ResearchActivity"}, {"text": "water", "type": "Chemical"}, {"text": "presence", "type": "Finding"}, {"text": "complexing ligands", "type": "Chemical"}]}

Example input:
Sentence: Applicability of drinking water treatment residue for lake restoration in relation to metal / metalloid risk assessment Drinking water treatment residue ( DWTR ) , a byproduct generated during potable water production , exhibits a high potential for recycling to control eutrophication .

Example answer:
{"entities": [{"text": "lake", "type": "SpatialConcept"}, {"text": "metal", "type": "Chemical"}, {"text": "metalloid", "type": "Chemical"}, {"text": "risk assessment", "type": "HealthCareActivity"}, {"text": "potable water", "type": "Chemical"}]}

Example input:
Sentence: The biochemical methane potential ( BMP ) of five different algae ( Chlorella vulgaris ) / manure ( cattle ) mixtures showed that the mixture of 80 / 20 ( on VS basis ) resulted in the highest BMP value ( 431mL CH4 gVS ( - 1 ) ) , while the BMP of microalgae alone ( 100 / 0 ) was 415mL CH4 gVS ( - 1 ) .

Example answer:
{"entities": [{"text": "methane", "type": "Chemical"}, {"text": "algae", "type": "Eukaryote"}, {"text": "Chlorella vulgaris", "type": "Eukaryote"}, {"text": "cattle", "type": "Eukaryote"}, {"text": "CH4", "type": "Chemical"}, {"text": "microalgae", "type": "Eukaryote"}]}

Example input:
Sentence: The risks of DWTR were also evaluated for sediments on the basis of toxicity characteristics leaching procedure and fractionation in relation to risk assessment code .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "risk assessment", "type": "HealthCareActivity"}, {"text": "code", "type": "IntellectualProduct"}]}

Example input:
Sentence: The results show that water , suspended particles , and sediments were significant ly contaminated by various TMs ( As , Cd , Cu , Ni , Pb , and Zn ) .

Example answer:
{"entities": [{"text": "water", "type": "Chemical"}, {"text": "particles", "type": "Chemical"}, {"text": "TMs", "type": "Chemical"}, {"text": "As", "type": "Chemical"}, {"text": "Cd", "type": "Chemical"}, {"text": "Cu", "type": "Chemical"}, {"text": "Ni", "type": "Chemical"}, {"text": "Pb", "type": "Chemical"}, {"text": "Zn", "type": "Chemical"}]}

Input:
Sentence: The objectives of this study were to assess the bioavailability and transfer potential of various TMs present in water and sediments in a reservoir receiving landfill leachates .

## Item MedMentions:test:3067
Example input:
Sentence: We suggest that modulation of TRPV1 channels by noradrenaline in nociceptive neurons is a mechanism whereby noradrenaline may suppress incoming noxious stimuli at the primary synaptic afferents in the dorsal horn of the spinal cord .

Example answer:
{"entities": [{"text": "TRPV1 channels", "type": "Chemical"}, {"text": "noradrenaline", "type": "Chemical"}, {"text": "nociceptive neurons", "type": "AnatomicalStructure"}, {"text": "synaptic", "type": "SpatialConcept"}, {"text": "afferents", "type": "AnatomicalStructure"}, {"text": "dorsal horn of the spinal cord", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Using the activatory Gq - coupled human M3 muscarinic receptor ( hM3Dq ) , we found that chemogenetic stimulation of dSPNs mimicked , while stimulation of iSPNs abolished the therapeutic action of L - DOPA in PD mice .

Example answer:
{"entities": [{"text": "activatory Gq - coupled human M3 muscarinic receptor", "type": "Chemical"}, {"text": "hM3Dq", "type": "Chemical"}, {"text": "chemogenetic stimulation", "type": "BiologicFunction"}, {"text": "dSPNs", "type": "AnatomicalStructure"}, {"text": "stimulation", "type": "BiologicFunction"}, {"text": "iSPNs", "type": "AnatomicalStructure"}, {"text": "therapeutic action", "type": "BiologicFunction"}, {"text": "L - DOPA", "type": "Chemical"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: The inhibitory effect of noradrenaline on the capsaicin - activated current was not affected either by blocking the activity of protein kinase A with H89 , or by blocking the activity of protein kinase C with bisindolylmaleimide II .

Example answer:
{"entities": [{"text": "inhibitory", "type": "BiologicFunction"}, {"text": "noradrenaline", "type": "Chemical"}, {"text": "capsaicin", "type": "Chemical"}, {"text": "current", "type": "BiologicFunction"}, {"text": "protein kinase A", "type": "Chemical"}, {"text": "H89", "type": "Chemical"}, {"text": "protein kinase C", "type": "Chemical"}, {"text": "bisindolylmaleimide II", "type": "Chemical"}]}

Example input:
Sentence: Infusion of a small amount of a D1 or D2 antagonist led to early saccades in the self - timed , but not the triggered MS tasks , while infusion of DA agonists produced no consistent effect .

Example answer:
{"entities": [{"text": "Infusion", "type": "HealthCareActivity"}, {"text": "D1", "type": "Chemical"}, {"text": "D2", "type": "Chemical"}, {"text": "antagonist", "type": "Chemical"}, {"text": "saccades", "type": "BiologicFunction"}, {"text": "MS tasks", "type": "HealthCareActivity"}, {"text": "infusion", "type": "HealthCareActivity"}, {"text": "DA agonists", "type": "Chemical"}]}

Example input:
Sentence: Noradrenaline strongly inhibited the activity of TRPV1 channels in dorsal root ganglia neurons .

Example answer:
{"entities": [{"text": "Noradrenaline", "type": "Chemical"}, {"text": "TRPV1 channels", "type": "Chemical"}, {"text": "dorsal root ganglia", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In contrast , when the calcium / calmodulin - dependent protein kinase II ( CaMKII ) was blocked with KN - 93 , the inhibitory effect of noradrenaline on the capsaicin - activated current was greatly reduced , suggesting that activation of adrenergic receptors in DRG neurons is preferentially linked to CaMKII activity .

Example answer:
{"entities": [{"text": "calcium / calmodulin - dependent protein kinase II", "type": "Chemical"}, {"text": "CaMKII", "type": "Chemical"}, {"text": "KN - 93", "type": "Chemical"}, {"text": "inhibitory", "type": "BiologicFunction"}, {"text": "noradrenaline", "type": "Chemical"}, {"text": "capsaicin", "type": "Chemical"}, {"text": "current", "type": "BiologicFunction"}, {"text": "adrenergic receptors", "type": "Chemical"}, {"text": "DRG", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Likewise , phenylephrine - induced contractions were greater in the sickle mice , whereas α1A - , α1B - and α1D - adrenoceptor mRNA expression remained unchanged .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "contractions", "type": "BiologicFunction"}, {"text": "sickle", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "α1A -", "type": "Chemical"}, {"text": "α1B -", "type": "Chemical"}, {"text": "α1D - adrenoceptor", "type": "Chemical"}, {"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "unchanged", "type": "Finding"}]}

Example input:
Sentence: The inhibitory effect of noradrenaline on TRPV1 channels was dependent on calcium influx and linked to calcium / calmodulin - dependent protein kinase II .

Example answer:
{"entities": [{"text": "inhibitory", "type": "BiologicFunction"}, {"text": "noradrenaline", "type": "Chemical"}, {"text": "TRPV1 channels", "type": "Chemical"}, {"text": "calcium influx", "type": "BiologicFunction"}, {"text": "calcium / calmodulin - dependent protein kinase II", "type": "Chemical"}]}

Example input:
Sentence: To address whether noradrenaline can down - regulate TRPV1 channel activity in nociceptors and reduce their synaptic transmission , the effects of noradrenaline and clonidine were tested on the capsaicin - activated current recorded from acutely dissociated small diameter ( < 27 μm ) dorsal root ganglia ( DRG ) neurons and on miniature ( m ) EPSCs recorded from large lamina I neurons in horizontal spinal cord slices .

Example answer:
{"entities": [{"text": "noradrenaline", "type": "Chemical"}, {"text": "down - regulate", "type": "BiologicFunction"}, {"text": "TRPV1 channel", "type": "Chemical"}, {"text": "nociceptors", "type": "AnatomicalStructure"}, {"text": "synaptic transmission", "type": "BiologicFunction"}, {"text": "clonidine", "type": "Chemical"}, {"text": "capsaicin", "type": "Chemical"}, {"text": "current", "type": "BiologicFunction"}, {"text": "dorsal root ganglia", "type": "AnatomicalStructure"}, {"text": "DRG", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "miniature ( m ) EPSCs", "type": "BiologicFunction"}, {"text": "lamina I", "type": "AnatomicalStructure"}, {"text": "horizontal", "type": "SpatialConcept"}, {"text": "spinal cord", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Noradrenaline or clonidine inhibited the capsaicin - activated current by ∼60 % , and the effect was reversed by yohimbine , confirming that it was mediated by activation of α2 adrenergic receptors .

Example answer:
{"entities": [{"text": "Noradrenaline", "type": "Chemical"}, {"text": "clonidine", "type": "Chemical"}, {"text": "capsaicin", "type": "Chemical"}, {"text": "current", "type": "BiologicFunction"}, {"text": "yohimbine", "type": "Chemical"}, {"text": "α2 adrenergic receptors", "type": "Chemical"}]}

Input:
Sentence: The effect of noradrenaline was reproduced by clonidine and antagonized by yohimbine , consistent with contribution of α2 adrenergic receptors .

## Item MedMentions:test:3342
Example input:
Sentence: 007 , and p = 0 . 04 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 023±0 . 025 , P = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 004 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 007 - 3 . 337 , P < 0 . 001 ] .

Example answer:
{"entities": []}

Example input:
Sentence: 006 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 005 .

Example answer:
{"entities": []}

Example input:
Sentence: 003 ; p = 0 . 0001 ) , but not in HSM .

Example answer:
{"entities": [{"text": "HSM", "type": "HealthCareActivity"}]}

Example input:
Sentence: 0003 )

Example answer:
{"entities": []}

Example input:
Sentence: 003 , OR = 9 .

Example answer:
{"entities": []}

Example input:
Sentence: 003 , p = .

Example answer:
{"entities": []}

Input:
Sentence: 003 ) .

## Item MedMentions:test:3272
Example input:
Sentence: 37 % ( 95 % CI : 11 . 35 - 11 . 40 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 9 % ( 95 % CI : 79 . 6 , 97 . 7 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 94 ( CI 95 % : 0 . 90 to 0 . 96 ) and 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 92 ( 95 % CI : 0 . 65 - 1 . 28 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 94 , 95 % CI : 1 . 68 - 5 . 14 , P < 0 . 001 and HR = 1 . 74 , 95 % CI : 1 . 23 - 2 . 47 , P = 0 . 002 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 98 , 95 % CI : 0 . 8 - 1 . 17 , P < 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 , 95 % CI : 1 . 12 - 1 . 50 ] , hypertension ( OR = 1 . 34 , 95 % CI : 1 .

Example answer:
{"entities": [{"text": "hypertension", "type": "BiologicFunction"}]}

Example input:
Sentence: 48 ; 95 % CI 1 . 31 - 4 . 70 ) , and cystic fibrosis ( OR 2 . 17 ; 95 % CI 1 . 16 - 4 . 06 ) .

Example answer:
{"entities": [{"text": "cystic fibrosis", "type": "BiologicFunction"}]}

Example input:
Sentence: 4 , 95 % CI : 2 . 80 - 38 . 4 ] .

Example answer:
{"entities": []}

Example input:
Sentence: 4 . 86 ( 95 % CI , 1 . 9 - 11 .

Example answer:
{"entities": []}

Input:
Sentence: 93 to 2 . 10 ) , except for hematuria ( OR , 4 . 80 ; 95 % CI , 1 . 45 to 15 . 94 ) .

## Item MedMentions:test:2499
Example input:
Sentence: Phenol red free media is also used during live cell imaging , to avoid absorbance and fluorescence quenching of fluorophores .

Example answer:
{"entities": [{"text": "Phenol red", "type": "Chemical"}, {"text": "media", "type": "Chemical"}, {"text": "fluorescence quenching", "type": "BiologicFunction"}]}

Example input:
Sentence: Metaphase fluorescence in situ hybridization analysis using the probes of RP11 - 754D24 ( 8p11 . 21 ) and RP11 - 769N21 ( 8q11 . 21 ) showed the sSMC ( 8 ) in 12 / 27 of cultured lymphocytes .

Example answer:
{"entities": [{"text": "Metaphase fluorescence in situ hybridization analysis", "type": "ResearchActivity"}, {"text": "probes", "type": "Chemical"}, {"text": "RP11 - 754D24", "type": "AnatomicalStructure"}, {"text": "8p11 . 21", "type": "AnatomicalStructure"}, {"text": "RP11 - 769N21", "type": "AnatomicalStructure"}, {"text": "8q11 . 21", "type": "AnatomicalStructure"}, {"text": "sSMC ( 8 )", "type": "AnatomicalStructure"}, {"text": "cultured lymphocytes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Mesenchymal stromal cells exposed to carbon monoxide , with docosahexaenoic acid substrate , produced specialized proresolving lipid mediators , particularly D - series resolvins , which promoted survival .

Example answer:
{"entities": [{"text": "Mesenchymal stromal cells", "type": "AnatomicalStructure"}, {"text": "carbon monoxide", "type": "Chemical"}, {"text": "docosahexaenoic acid", "type": "Chemical"}, {"text": "proresolving", "type": "Finding"}, {"text": "resolvins", "type": "Chemical"}]}

Example input:
Sentence: Intracellular reactive oxygen species ( ROS ) production was detected by 2’ , 7’ - dichlorodihydrofluorescein diacetate ( DCHF - DA ) incubation and fluorescence microscopy .

Example answer:
{"entities": [{"text": "Intracellular", "type": "SpatialConcept"}, {"text": "detected", "type": "Finding"}, {"text": "2’ , 7’ - dichlorodihydrofluorescein diacetate", "type": "Chemical"}, {"text": "DCHF - DA", "type": "Chemical"}, {"text": "incubation", "type": "HealthCareActivity"}, {"text": "fluorescence microscopy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Epithelia from the anterior eyes of chicken embryos were labeled with the fluorescent , lipophilic dye , 1 , 1 ' - dioctadecyl - 3 , 3 , 3 ' , 3 ' - tetramethylindocarbocyanine perchlorate ( DiI ) .

Example answer:
{"entities": [{"text": "Epithelia", "type": "AnatomicalStructure"}, {"text": "anterior eyes", "type": "AnatomicalStructure"}, {"text": "chicken embryos", "type": "AnatomicalStructure"}, {"text": "labeled", "type": "Chemical"}, {"text": "fluorescent", "type": "Chemical"}, {"text": "lipophilic dye", "type": "Chemical"}, {"text": "1 , 1 ' - dioctadecyl - 3 , 3 , 3 ' , 3 ' - tetramethylindocarbocyanine perchlorate", "type": "Chemical"}, {"text": "DiI", "type": "Chemical"}]}

Example input:
Sentence: Fluorescence recovery after photobleaching ( FRAP ) microscopy is used to probe the diffusion properties of TATS in isolated rat cardiomyocytes : A fluorescent dextran inside TATS lumen is photobleached , and signal recovery by diffusion of unbleached dextran from the extracellular space is monitored .

Example answer:
{"entities": [{"text": "Fluorescence recovery after photobleaching", "type": "HealthCareActivity"}, {"text": "FRAP", "type": "HealthCareActivity"}, {"text": "microscopy", "type": "HealthCareActivity"}, {"text": "probe", "type": "ResearchActivity"}, {"text": "properties", "type": "BiologicFunction"}, {"text": "TATS", "type": "AnatomicalStructure"}, {"text": "rat", "type": "Eukaryote"}, {"text": "cardiomyocytes", "type": "AnatomicalStructure"}, {"text": "fluorescent dextran", "type": "Chemical"}, {"text": "lumen", "type": "SpatialConcept"}, {"text": "dextran", "type": "Chemical"}, {"text": "extracellular space", "type": "SpatialConcept"}, {"text": "monitored", "type": "HealthCareActivity"}]}

Example input:
Sentence: A diffuse reticular localisation was detected for the complex in the nuclear / perinuclear region of cells , by either optical or X - ray fluorescence imaging techniques .

Example answer:
{"entities": [{"text": "complex", "type": "Chemical"}, {"text": "nuclear", "type": "AnatomicalStructure"}, {"text": "perinuclear region", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "optical", "type": "HealthCareActivity"}, {"text": "X - ray fluorescence imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: The results of cell uptake showed that the fluorescent 3P - Ru loaded in the nanocapsule could be delivered into cells with high efficiency , and then significantly inhibited U251 proliferation in a concentration - dependent manner .

Example answer:
{"entities": [{"text": "cell", "type": "AnatomicalStructure"}, {"text": "uptake", "type": "BiologicFunction"}, {"text": "fluorescent 3P - Ru", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "U251", "type": "AnatomicalStructure"}, {"text": "proliferation", "type": "BiologicFunction"}]}

Example input:
Sentence: The rhenium complex showed no signs of ancillary ligand dissociation , a conclusion based on data obtained via X - ray fluorescence imaging aligning iodine and rhenium distributions .

Example answer:
{"entities": [{"text": "rhenium complex", "type": "Chemical"}, {"text": "ligand", "type": "Chemical"}, {"text": "X - ray fluorescence imaging", "type": "HealthCareActivity"}, {"text": "iodine", "type": "Chemical"}, {"text": "rhenium", "type": "Chemical"}]}

Example input:
Sentence: X - ray fluorescence also showed that the rhenium complex disrupted the homeostasis of some biologically relevant elements , such as chlorine , potassium and zinc .

Example answer:
{"entities": [{"text": "X - ray fluorescence", "type": "HealthCareActivity"}, {"text": "rhenium complex", "type": "Chemical"}, {"text": "homeostasis", "type": "BiologicFunction"}, {"text": "biologically relevant elements", "type": "Chemical"}, {"text": "chlorine", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "zinc", "type": "Chemical"}]}

Input:
Sentence: Intracellular distribution and stability of a luminescent rhenium ( i ) tricarbonyl tetrazolato complex using epifluorescence microscopy in conjunction with X - ray fluorescence imaging Optical epifluorescence microscopy was used in conjunction with X - ray fluorescence imaging to monitor the stability and intracellular distribution of the luminescent rhenium ( i ) complex fac - [ Re ( CO ) 3 ( phen ) L ] , where phen = 1 , 10 - phenathroline and L = 5 - ( 4 - iodophenyl ) tetrazolato , in 22Rv1 cells .

## Item MedMentions:test:2976
Example input:
Sentence: Flow cytometric analysis showed that , compared with the control and Ad - GFP groups , cell apoptosis rate of Ad - PLCγ2 group were significantly increased ( P < 0 .

Example answer:
{"entities": [{"text": "Flow cytometric analysis", "type": "HealthCareActivity"}, {"text": "Ad - GFP groups", "type": "Chemical"}, {"text": "cell apoptosis", "type": "BiologicFunction"}, {"text": "Ad - PLCγ2 group", "type": "Chemical"}]}

Example input:
Sentence: Here we report that despite systematically testing different ways of measuring intracellular calcium and different MS protocols , it was not possible to detect any cellular or neuronal responses to MS in MagR - expressing HEK cells or primary neurons from the dorsal root ganglion and the hippocampus .

Example answer:
{"entities": [{"text": "intracellular", "type": "SpatialConcept"}, {"text": "calcium", "type": "Chemical"}, {"text": "MS", "type": "HealthCareActivity"}, {"text": "protocols", "type": "IntellectualProduct"}, {"text": "detect", "type": "Finding"}, {"text": "cellular", "type": "AnatomicalStructure"}, {"text": "neuronal", "type": "AnatomicalStructure"}, {"text": "MagR", "type": "Chemical"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "HEK cells", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "dorsal", "type": "SpatialConcept"}, {"text": "root ganglion", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In vitro , small and large mouse cholangiocytes , H69 ( non - malignant human cholangiocytes ) and LCDE ( human cholangiocytes from the cystic epithelium ) were stimulated with vasopressin in the absence / presence of AVP antagonists such as OPC - 31260 and Tolvaptan , before assessing cellular growth by MTT assay and cAMP levels .

Example answer:
{"entities": [{"text": "mouse", "type": "Eukaryote"}, {"text": "H69", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "LCDE", "type": "AnatomicalStructure"}, {"text": "cystic epithelium", "type": "AnatomicalStructure"}, {"text": "stimulated", "type": "BiologicFunction"}, {"text": "vasopressin", "type": "Chemical"}, {"text": "presence", "type": "Finding"}, {"text": "AVP antagonists", "type": "Chemical"}, {"text": "OPC - 31260", "type": "Chemical"}, {"text": "Tolvaptan", "type": "Chemical"}, {"text": "cellular growth", "type": "BiologicFunction"}, {"text": "MTT assay", "type": "HealthCareActivity"}, {"text": "cAMP", "type": "Chemical"}]}

Example input:
Sentence: In this study , we manipulated RBBP6 expression levels followed by treatment with either camptothecin or γ - aminobutyric acid in cervical cancer cells to induce apoptosis or cell cycle arrest .

Example answer:
{"entities": [{"text": "study", "type": "HealthCareActivity"}, {"text": "manipulated", "type": "HealthCareActivity"}, {"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "camptothecin", "type": "Chemical"}, {"text": "γ - aminobutyric acid", "type": "Chemical"}, {"text": "induce", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "cell cycle arrest", "type": "BiologicFunction"}]}

Example input:
Sentence: Silencing RBBP6 followed by treatment with γ - aminobutyric acid and camptothecin seems to sensitize cells to apoptosis induction rather than cell cycle arrest .

Example answer:
{"entities": [{"text": "Silencing", "type": "BiologicFunction"}, {"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "γ - aminobutyric acid", "type": "Chemical"}, {"text": "camptothecin", "type": "Chemical"}, {"text": "sensitize cells", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "induction", "type": "BiologicFunction"}, {"text": "cell cycle arrest", "type": "BiologicFunction"}]}

Example input:
Sentence: Specific spatio - temporal patterns of cytosolic calcium elevations are critical determinants of cell fate in response to pro - apoptotic cellular stressors .

Example answer:
{"entities": [{"text": "spatio - temporal", "type": "ResearchActivity"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "cytosolic", "type": "AnatomicalStructure"}, {"text": "calcium", "type": "Chemical"}, {"text": "cellular", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Due to the technical limitations of using calcium - sensitive dyes to measure cytosolic calcium little is known about long - term calcium dynamics in living cells after treatment with apoptosis - inducing drugs .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "dyes", "type": "Chemical"}, {"text": "cytosolic", "type": "AnatomicalStructure"}, {"text": "dynamics", "type": "BiologicFunction"}, {"text": "living cells", "type": "AnatomicalStructure"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "drugs", "type": "Chemical"}]}

Example input:
Sentence: Here , we compared the performance of the genetically encoded calcium indicators GCaMP6s and GCaMP6f with the ratiometric dye Fura - 2 .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "indicators", "type": "Chemical"}, {"text": "ratiometric dye", "type": "Chemical"}, {"text": "Fura - 2", "type": "Chemical"}]}

Example input:
Sentence: As the apoptotic program can take hours or days , measurement of long - term calcium dynamics are essential for understanding the mechanistic role of calcium in apoptotic cell death .

Example answer:
{"entities": [{"text": "apoptotic program", "type": "BiologicFunction"}, {"text": "calcium", "type": "Chemical"}, {"text": "dynamics", "type": "BiologicFunction"}, {"text": "understanding", "type": "BiologicFunction"}, {"text": "apoptotic cell death", "type": "BiologicFunction"}]}

Example input:
Sentence: Our results suggest GCaMP6s is an excellent indicator for monitoring long - term changes cytosolic calcium during apoptosis .

Example answer:
{"entities": [{"text": "indicator", "type": "Chemical"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "cytosolic", "type": "AnatomicalStructure"}, {"text": "calcium", "type": "Chemical"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Input:
Sentence: We found that GCaMP6s was suitable for measuring apoptotic calcium release over long time courses and revealed significant heterogeneity in calcium release dynamics in individual cells challenged with staurosporine .

## Item MedMentions:test:3143
Example input:
Sentence: BEAS - 2B cells were treated with NaF at concentrations of 0 , 0 . 25 , 0 . 5 , 1 .

Example answer:
{"entities": [{"text": "BEAS - 2B cells", "type": "AnatomicalStructure"}, {"text": "NaF", "type": "Chemical"}]}

Example input:
Sentence: So far , the pathogenesis of NAFLD and its more severe variant nonalcoholic steatohepatitis ( NASH ) is yet unclear , with many mechanisms being proposed as possible causes .

Example answer:
{"entities": [{"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "NAFLD", "type": "BiologicFunction"}, {"text": "nonalcoholic steatohepatitis", "type": "BiologicFunction"}, {"text": "NASH", "type": "BiologicFunction"}]}

Example input:
Sentence: By transmission electron microscopy with acridine orange and Cyto - ID®Autophagy detection dyes , Western blot analysis , and RT - PCR assay , we confirmed that delicaflavone induces autophagic cell death by increasing the ratio of LC3 - II to LC3 - I , which are autophagy - related proteins , and promoting the generation of acidic vesicular organelles and autolysosomes in the cytoplasm of human lung cancer A549 and PC - 9 cells in a time - and dose - dependent manner .

Example answer:
{"entities": [{"text": "transmission electron microscopy", "type": "HealthCareActivity"}, {"text": "acridine orange", "type": "Chemical"}, {"text": "Cyto - ID®Autophagy", "type": "BiologicFunction"}, {"text": "dyes", "type": "Chemical"}, {"text": "Western blot", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "RT - PCR assay", "type": "ResearchActivity"}, {"text": "delicaflavone", "type": "Chemical"}, {"text": "autophagic cell death", "type": "BiologicFunction"}, {"text": "LC3 - II", "type": "Chemical"}, {"text": "LC3 - I", "type": "Chemical"}, {"text": "autophagy - related proteins", "type": "Chemical"}, {"text": "acidic vesicular organelles", "type": "AnatomicalStructure"}, {"text": "autolysosomes", "type": "AnatomicalStructure"}, {"text": "cytoplasm", "type": "AnatomicalStructure"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "A549", "type": "AnatomicalStructure"}, {"text": "PC - 9 cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Compound 2c induced apoptosis of MCF - 7 cells through cell membrane alteration .

Example answer:
{"entities": [{"text": "Compound 2c", "type": "Chemical"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "MCF - 7 cells", "type": "AnatomicalStructure"}, {"text": "cell membrane alteration", "type": "BiologicFunction"}]}

Example input:
Sentence: Delicaflavone induced autophagic cell death via Akt / mTOR / p70S6 K signaling pathway .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "autophagic cell death", "type": "BiologicFunction"}, {"text": "Akt", "type": "BiologicFunction"}, {"text": "mTOR", "type": "BiologicFunction"}, {"text": "p70S6 K", "type": "Chemical"}, {"text": "signaling pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Delicaflavone induced autophagic cell death via Akt / mTOR / p70S6 K signaling pathway .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "autophagic cell death", "type": "BiologicFunction"}, {"text": "Akt", "type": "BiologicFunction"}, {"text": "mTOR", "type": "BiologicFunction"}, {"text": "p70S6 K", "type": "Chemical"}, {"text": "signaling pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: However , N - acetyl cysteine ( NAC ) and downregulation of p53 expression could partially reverse the apoptosis caused by the loss of NFBD1 .

Example answer:
{"entities": [{"text": "N - acetyl cysteine", "type": "Chemical"}, {"text": "NAC", "type": "Chemical"}, {"text": "downregulation", "type": "BiologicFunction"}, {"text": "p53 expression", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "NFBD1", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Cell viability decreased and apoptotic cells significantly increased as concentrations of NaF increased over specific periods of time .

Example answer:
{"entities": [{"text": "Cell viability", "type": "BiologicFunction"}, {"text": "apoptotic", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "NaF", "type": "Chemical"}]}

Example input:
Sentence: The Effect of Sodium Fluoride on Cell Apoptosis and the Mechanism of Human Lung BEAS - 2B Cells In Vitro Sodium fluoride ( NaF ) is a source of fluoride ions used in many applications .

Example answer:
{"entities": [{"text": "Sodium Fluoride", "type": "Chemical"}, {"text": "Cell", "type": "AnatomicalStructure"}, {"text": "Apoptosis", "type": "BiologicFunction"}, {"text": "Mechanism", "type": "BiologicFunction"}, {"text": "Human", "type": "Eukaryote"}, {"text": "Lung", "type": "AnatomicalStructure"}, {"text": "BEAS - 2B Cells", "type": "AnatomicalStructure"}, {"text": "Sodium fluoride", "type": "Chemical"}, {"text": "NaF", "type": "Chemical"}, {"text": "fluoride ions", "type": "Chemical"}]}

Example input:
Sentence: These findings suggested that NaF induced apoptosis in the BEAS - 2B cells through mitochondria -mediated signal pathways .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "NaF", "type": "Chemical"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "BEAS - 2B cells", "type": "AnatomicalStructure"}, {"text": "mitochondria", "type": "AnatomicalStructure"}, {"text": "signal pathways", "type": "BiologicFunction"}]}

Input:
Sentence: Therefore , we investigated the mode of cell death induced by NaF and its underlying molecular mechanisms .
