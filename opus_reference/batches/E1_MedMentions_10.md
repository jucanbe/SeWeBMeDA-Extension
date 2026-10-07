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

## Item MedMentions:test:2054
Example input:
Sentence: Evaluations before randomization and 4 weeks after intervention included motor scoring index , real - time PCR and Western blot .

Example answer:
{"entities": [{"text": "Evaluations", "type": "HealthCareActivity"}, {"text": "randomization", "type": "ResearchActivity"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "real - time PCR", "type": "ResearchActivity"}, {"text": "Western blot", "type": "HealthCareActivity"}]}

Example input:
Sentence: The greatest therapeutic effect was observed for stage III disease : PWD increased by 683 % ( p = 0 . 0001 ) .

Example answer:
{"entities": [{"text": "therapeutic effect", "type": "ClinicalAttribute"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "PWD", "type": "Finding"}]}

Example input:
Sentence: Thirty - nine TSH measurements were obtained 1 - 28 days post L - T3 withdrawal .

Example answer:
{"entities": [{"text": "TSH measurements", "type": "HealthCareActivity"}, {"text": "L - T3", "type": "Chemical"}, {"text": "withdrawal", "type": "HealthCareActivity"}]}

Example input:
Sentence: T3 was administered to male F344 rats on postnatal days 1 , 3 , and 5 ( week 0 ) .

Example answer:
{"entities": [{"text": "T3", "type": "Chemical"}, {"text": "administered", "type": "HealthCareActivity"}, {"text": "male F344 rats", "type": "Eukaryote"}]}

Example input:
Sentence: The mice were divided into 5 groups : a low - dose leonurine treatment group , a high - dose leonurine treatment group , a valproic acid ( VPA ) treatment group , a vehicle only treatment group , and a blank control group .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}, {"text": "leonurine", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "valproic acid", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "vehicle", "type": "Chemical"}]}

Example input:
Sentence: Further , post - infection treatment with a single systemic dose of 3c10 - 3 at either 24 , 48 or 72 h post A ( H7N9 ) challenge resulted in both dose - and time - dependent protection of up to 100 % of mice , demonstrating therapeutic potential for 3c10 - 3 .

Example answer:
{"entities": [{"text": "infection", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "3c10 - 3", "type": "Chemical"}, {"text": "A ( H7N9 )", "type": "Virus"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: At the end of intervention , 88 . 5 % of the MG and 48 . 1 % of the PG ( P = 0 . 002 ) had a normal level of magnesium .

Example answer:
{"entities": [{"text": "MG", "type": "Chemical"}, {"text": "PG", "type": "Chemical"}, {"text": "normal level of magnesium", "type": "Finding"}]}

Example input:
Sentence: After 6 weeks , mice were split in three groups ( n = 8 / group ) : no supplementation , 2 - OHOA supplementation ( 1500 mg kg ( - 1 ) ) and n - 3 PUFA supplementation ( EPA + DHA , 3000 mg kg ( - 1 ) diet ) .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}, {"text": "EPA", "type": "Chemical"}, {"text": "DHA", "type": "Chemical"}]}

Example input:
Sentence: ATV trough levels at week 9 were higher in controls ( median 438 ng / mL ) than in the switch arm ( median 124 ng / mL ) ( p = 0 . 003 ) , as was total bilirubin at week 48 ( median 38 μmol / L and 28 μmol / L , respectively ; p = 0 .

Example answer:
{"entities": [{"text": "ATV", "type": "Chemical"}, {"text": "median", "type": "SpatialConcept"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: T3 -15 mg / kg group showed reduced VCAM - 1 , ICAM - 1 , E - selectin , IL - 6 , MMP - 12 and MMP - 9 ( 20 . 5±3 .

Example answer:
{"entities": [{"text": "T3", "type": "Chemical"}, {"text": "VCAM - 1", "type": "Chemical"}, {"text": "ICAM - 1", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "MMP - 12", "type": "Chemical"}, {"text": "MMP - 9", "type": "Chemical"}]}

Input:
Sentence: Each group was subdivided into three intervention arms : 1 ) T3 -4 mg / kg , 2 ) T3 -15 mg / kg and 3 ) vehicle without T3 ( T3 negative ) for 8 weeks .

## Item MedMentions:test:1736
Example input:
Sentence: This disulfide linkage causes CA - 4 to become effective only when released by glutathione ( GSH ) reducing the toxicity of the drug while simultaneously releasing the NIR fluorophore .

Example answer:
{"entities": [{"text": "CA - 4", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "drug", "type": "Chemical"}]}

Example input:
Sentence: A nano - delivery system for bioactive ingredients using supercritical carbon dioxide and its release behaviors For the purpose of ensuring the bioavailability of bioactive ingredients , a nano - delivery system with low toxicity was developed using supercritical carbon dioxide ( SC - CO2 ) .

Example answer:
{"entities": [{"text": "carbon dioxide", "type": "Chemical"}, {"text": "CO2", "type": "Chemical"}]}

Example input:
Sentence: We hypothesized that preconditioning of mesenchymal stromal cells with carbon monoxide ex vivo would promote further therapeutic benefit when cells are administered in vivo after the onset of polymicrobial sepsis in mice .

Example answer:
{"entities": [{"text": "mesenchymal stromal cells", "type": "AnatomicalStructure"}, {"text": "carbon monoxide", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "polymicrobial", "type": "BiologicFunction"}, {"text": "sepsis", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Carbonic anhydrase converts COS into H2S , allowing NTAs to serve as either COS or H2S donors , depending on the availability of the enzyme .

Example answer:
{"entities": [{"text": "Carbonic anhydrase", "type": "Chemical"}, {"text": "COS", "type": "Chemical"}, {"text": "H2S", "type": "Chemical"}, {"text": "NTAs", "type": "Chemical"}, {"text": "enzyme", "type": "Chemical"}]}

Example input:
Sentence: The IscS protein of this system was additionally revealed to be the primary sulfur donor for several sulfur - containing molecules with important biological functions , among which are the molybdenum cofactor ( Moco ) and thiolated nucleosides in tRNA .

Example answer:
{"entities": [{"text": "IscS protein", "type": "Chemical"}, {"text": "biological functions", "type": "BiologicFunction"}, {"text": "molybdenum cofactor", "type": "Chemical"}, {"text": "Moco", "type": "Chemical"}, {"text": "thiolated nucleosides in tRNA", "type": "BiologicFunction"}]}

Example input:
Sentence: Taken together , these data suggest that production of specialized proresolving lipid mediators contribute to improved mesenchymal stromal cell efficacy when exposed to carbon monoxide , resulting in an improved therapeutic response during sepsis .

Example answer:
{"entities": [{"text": "proresolving", "type": "Finding"}, {"text": "improved", "type": "Finding"}, {"text": "mesenchymal stromal cell", "type": "AnatomicalStructure"}, {"text": "carbon monoxide", "type": "Chemical"}, {"text": "therapeutic response", "type": "ClinicalAttribute"}, {"text": "sepsis", "type": "BiologicFunction"}]}

Example input:
Sentence: Carbon Monoxide Improves Efficacy of Mesenchymal Stromal Cells During Sepsis by Production of Specialized Proresolving Lipid Mediators Mesenchymal stromal cells are being investigated as a cell - based therapy for a number of disease processes , with promising results in animal models of systemic inflammation and sepsis .

Example answer:
{"entities": [{"text": "Carbon Monoxide", "type": "Chemical"}, {"text": "Improves", "type": "Finding"}, {"text": "Mesenchymal Stromal Cells", "type": "AnatomicalStructure"}, {"text": "Sepsis", "type": "BiologicFunction"}, {"text": "Proresolving", "type": "Finding"}, {"text": "Mesenchymal stromal cells", "type": "AnatomicalStructure"}, {"text": "cell - based therapy", "type": "HealthCareActivity"}, {"text": "disease processes", "type": "BiologicFunction"}, {"text": "results", "type": "Finding"}, {"text": "animal models", "type": "Eukaryote"}, {"text": "sepsis", "type": "BiologicFunction"}]}

Example input:
Sentence: A chemical free nano - delivery system using SC - CO2 has been revealed for storage and controlled release of bioactive ingredients .

Example answer:
{"entities": [{"text": "CO2", "type": "Chemical"}]}

Example input:
Sentence: The volcanic gas carbonyl sulfide ( COS ) is known to catalyze the condensation of amino acids under aqueous conditions , but the reported di - , tri - , and tetra - peptides are too short to support a regular tertiary structure .

Example answer:
{"entities": [{"text": "volcanic gas", "type": "Chemical"}, {"text": "carbonyl sulfide", "type": "Chemical"}, {"text": "( COS )", "type": "Chemical"}, {"text": "amino acids", "type": "Chemical"}, {"text": "reported", "type": "IntellectualProduct"}, {"text": "di -", "type": "Chemical"}, {"text": "tri -", "type": "Chemical"}, {"text": "tetra - peptides", "type": "Chemical"}, {"text": "tertiary structure", "type": "SpatialConcept"}]}

Example input:
Sentence: We report here the use of N - thiocarboxyanhydrides ( NTAs ) as COS donors that release the gas in a sustained manner under biologically relevant conditions with innocuous peptide byproducts .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "N - thiocarboxyanhydrides", "type": "Chemical"}, {"text": "NTAs", "type": "Chemical"}, {"text": "COS", "type": "Chemical"}, {"text": "gas", "type": "Chemical"}, {"text": "peptide", "type": "Chemical"}]}

Input:
Sentence: Therapeutic Delivery of H2S via COS : Small Molecule and Polymeric Donors with Benign Byproducts Carbonyl sulfide ( COS ) is a gas that may play important roles in mammalian and bacterial biology , but its study is limited by a lack of suitable donor molecules .

## Item MedMentions:test:1887
Example input:
Sentence: In the outpatient group , higher physical activity was associated with faster Motor and Psychomotor Speeds in outpatients .

Example answer:
{"entities": [{"text": "Psychomotor", "type": "BiologicFunction"}]}

Example input:
Sentence: Motor and neurocognitive functions were assessed at days 1 to 7 and 23 to 28 , respectively .

Example answer:
{"entities": [{"text": "Motor", "type": "BiologicFunction"}, {"text": "neurocognitive functions", "type": "BiologicFunction"}]}

Example input:
Sentence: Cognitive processing while walking may not increase energy demands of walking in healthy young adults .

Example answer:
{"entities": [{"text": "Cognitive processing", "type": "BiologicFunction"}]}

Example input:
Sentence: Kinematic and EMG Responses to Pelvis and Leg Assistance Force during Treadmill Walking in Children with Cerebral Palsy Treadmill training has been used for improving locomotor function in children with cerebral palsy ( CP ) , but the functional gains are relatively small , suggesting a need to improve current paradigms .

Example answer:
{"entities": [{"text": "Kinematic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "EMG", "type": "HealthCareActivity"}, {"text": "Pelvis", "type": "AnatomicalStructure"}, {"text": "Leg", "type": "AnatomicalStructure"}, {"text": "Cerebral Palsy", "type": "BiologicFunction"}, {"text": "Treadmill training", "type": "HealthCareActivity"}, {"text": "locomotor function", "type": "BiologicFunction"}, {"text": "cerebral palsy", "type": "BiologicFunction"}, {"text": "CP", "type": "BiologicFunction"}]}

Example input:
Sentence: At 60 months , median corrected distance VA ) in the fresh group had improved to 20 / 150 from a baseline of counting fingers , whereas the frozen group improved to 20 / 400 from a baseline of hand motions .

Example answer:
{"entities": [{"text": "VA", "type": "ClinicalAttribute"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: Twenty healthy , young adults completed five conditions : ( 1 ) walking at a self - selected speed ( spontaneous single - task ) , ( 2 ) seated resting ( baseline ) , ( 3 ) performing cognitive task while seated ( cognitive single - task ) , ( 4 ) walking while simultaneously performing the cognitive task ( dual - task ) , and ( 5 ) single - task walking at a speed that matched the participant 's dual - task gait speed ( matched single - task ) .

Example answer:
{"entities": [{"text": "seated", "type": "Finding"}, {"text": "cognitive", "type": "BiologicFunction"}, {"text": "participant 's", "type": "PopulationGroup"}]}

Example input:
Sentence: At any speed of fast walking , older children generated more peakA2 ( p = 0 . 001 ) and less peakH3 ( p = 0 . 001 ) than younger children .

Example answer:
{"entities": []}

Example input:
Sentence: These findings support the concept that running is a skill that matures early for TD children .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "matures", "type": "BiologicFunction"}]}

Example input:
Sentence: Propulsion strategy in the gait of primary school children ; the effect of age and speed The strategy used to generate power for forward propulsion in walking and running has recently been highlighted as a marker of gait maturation and elastic energy recycling .

Example answer:
{"entities": [{"text": "gait", "type": "Finding"}, {"text": "primary school", "type": "Organization"}, {"text": "propulsion", "type": "BiologicFunction"}, {"text": "marker", "type": "ClinicalAttribute"}, {"text": "maturation", "type": "BiologicFunction"}]}

Example input:
Sentence: This study investigated ankle and hip power generation as a propulsion strategy ( PS ) during the late stance / early swing phases of walking and running in typically developing ( TD ) children ( 15 : six to nine years ; 17 : nine to 13 years ) using three - dimensional gait analysis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "investigated", "type": "HealthCareActivity"}, {"text": "ankle", "type": "SpatialConcept"}, {"text": "hip", "type": "AnatomicalStructure"}, {"text": "three - dimensional", "type": "SpatialConcept"}, {"text": "gait analysis", "type": "HealthCareActivity"}]}

Input:
Sentence: While the kinetics of running propulsion appear to be developed by age six years , the skills of fast walking appeared to require additional neuromuscular maturity .

## Item MedMentions:test:2263
Example input:
Sentence: If statistical heterogeneity was significant , random - effects models were used for meta - analysis , otherwise , fixed - effects models were applied .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "IntellectualProduct"}]}

Example input:
Sentence: Overall satisfaction did not change statistically between the iterations but the qualitative analysis revealed greater trust in the second prototype .

Example answer:
{"entities": [{"text": "satisfaction", "type": "BiologicFunction"}, {"text": "iterations", "type": "Finding"}, {"text": "qualitative analysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: Statistical significance was set at p < 0 . 05 .

Example answer:
{"entities": []}

Example input:
Sentence: Univariate and multivariate analysis was performed with a priori significance at p ≤ 0 .

Example answer:
{"entities": []}

Example input:
Sentence:  of the gene - environment interaction results were significant after genome - wide correction for multiple testing ( α = 1 .

Example answer:
{"entities": [{"text": "gene - environment interaction", "type": "BiologicFunction"}, {"text": "genome - wide", "type": "AnatomicalStructure"}]}

Example input:
Sentence: All analyses were performed with a significance level of five percent .

Example answer:
{"entities": [{"text": "analyses", "type": "ResearchActivity"}, {"text": "significance level", "type": "ResearchActivity"}]}

Example input:
Sentence: Post - KAP was assessed twice , and the significance of difference was found by using McNemar 's test .

Example answer:
{"entities": [{"text": "Post - KAP", "type": "IntellectualProduct"}, {"text": "McNemar 's test", "type": "IntellectualProduct"}]}

Example input:
Sentence: One - way analysis of variance , Student 's t - test and Chi - square tests were used as appropriate with statistical significance attributed to P < 0 .

Example answer:
{"entities": [{"text": "Chi - square tests", "type": "IntellectualProduct"}]}

Example input:
Sentence: However , all of these differences lost significance after correction of the p value for multiple comparisons .

Example answer:
{"entities": []}

Example input:
Sentence: Statistical analysis was based on Wilcoxon rank sum tests with Bonferroni correction ( level of significance α = .05 ) .

Example answer:
{"entities": [{"text": "level of significance", "type": "ResearchActivity"}]}

Input:
Sentence: Statistical significance was assessed using correction for multiple testing .

## Item MedMentions:test:2151
Example input:
Sentence: Replacement is more likely to occur in tropical regions than temperate regions .

Example answer:
{"entities": [{"text": "tropical regions", "type": "SpatialConcept"}, {"text": "temperate regions", "type": "SpatialConcept"}]}

Example input:
Sentence: Modelling the influence of temperature and rainfall on malaria incidence in four endemic provinces of Zambia using semiparametric Poisson regression Although malaria morbidity and mortality are greatly reduced globally owing to great control efforts , the disease remains the main contributor .

Example answer:
{"entities": [{"text": "Modelling", "type": "ResearchActivity"}, {"text": "malaria", "type": "BiologicFunction"}, {"text": "endemic", "type": "BiologicFunction"}, {"text": "provinces", "type": "SpatialConcept"}, {"text": "Zambia", "type": "SpatialConcept"}, {"text": "control", "type": "HealthCareActivity"}, {"text": "efforts", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: 31 , 95 % CI = 0 . 25 - 0 . 41 ) compared to Luapula Province . North - western Province did not vary from Luapula Province .

Example answer:
{"entities": [{"text": "Luapula Province", "type": "SpatialConcept"}, {"text": "North - western Province", "type": "SpatialConcept"}]}

Example input:
Sentence: Temperature was the most important subcriterion under climate , while pathogen and Varroa loads were the most significant under health .

Example answer:
{"entities": [{"text": "Varroa", "type": "Eukaryote"}, {"text": "loads", "type": "Finding"}]}

Example input:
Sentence: Using a geoadditive or structured additive semiparametric Poisson regression model , we determined the influence of climatic factors on malaria incidence in four endemic provinces of Zambia .

Example answer:
{"entities": [{"text": "malaria", "type": "BiologicFunction"}, {"text": "endemic", "type": "BiologicFunction"}, {"text": "provinces", "type": "SpatialConcept"}, {"text": "Zambia", "type": "SpatialConcept"}]}

Example input:
Sentence: There was a big variation of regional cumulative mercury emission during 1980 - 2012 in China , with higher emissions occurred in eastern areas and lower values in the western and far northern regions .

Example answer:
{"entities": [{"text": "regional", "type": "SpatialConcept"}, {"text": "mercury", "type": "Chemical"}, {"text": "China", "type": "SpatialConcept"}, {"text": "eastern", "type": "SpatialConcept"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "western", "type": "SpatialConcept"}, {"text": "northern", "type": "SpatialConcept"}, {"text": "regions", "type": "SpatialConcept"}]}

Example input:
Sentence: 7 , while the variance ratio of SDR for provinces in the middle , west and south of China showed a greater variation ( 4 . 8 - 6 . 2 % ) .

Example answer:
{"entities": [{"text": "SDR", "type": "Finding"}, {"text": "provinces", "type": "SpatialConcept"}, {"text": "middle , west and south of China", "type": "SpatialConcept"}]}

Example input:
Sentence: Data from the 9306 participants were categorized by 5 regions : Asia ( n = 552 ) ; Europe ( n = 4909 ) ; Latin America ( n = 1406 ) ; North America ( n = 2146 ) ; and Australia , New Zealand , and South Africa ( n = 293 ) .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "regions", "type": "SpatialConcept"}, {"text": "Asia", "type": "SpatialConcept"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "Latin America", "type": "SpatialConcept"}, {"text": "North America", "type": "SpatialConcept"}, {"text": "Australia", "type": "SpatialConcept"}, {"text": "New Zealand", "type": "SpatialConcept"}, {"text": "South Africa", "type": "SpatialConcept"}]}

Example input:
Sentence: 38 % ( 95 % CI : 7 . 36 - 7 . 40 ) , in the eastern provinces 8 . 59 % ( 95 % CI : 8 . 57 - 8 . 62 ) and in coastal areas 6 . 70 % ( 95 % CI : 6 . 68 - 6 . 72 ) compared to the mountainous ones , which is 8 . 91 % ( 95 % CI : 8 . 88 - 8 . 94 ) .

Example answer:
{"entities": [{"text": "eastern provinces", "type": "SpatialConcept"}, {"text": "coastal areas", "type": "SpatialConcept"}, {"text": "mountainous ones", "type": "PopulationGroup"}]}

Example input:
Sentence: Results indicate that more stations exhibit cooling and warming than predicted by random chance and that spatial variations in these changes can account for spatial variations in the percentage of the population that believes that " global warming is happening . " This effect is diminished in areas that have experienced more record low temperatures than record highs since 2005 .

Example answer:
{"entities": [{"text": "population", "type": "PopulationGroup"}, {"text": "areas", "type": "SpatialConcept"}]}

Input:
Sentence: The effects of geographical region are clearly demonstrated by the unique behaviour and effects of minimum and maximum temperatures in the four provinces .

## Item MedMentions:test:1822
Example input:
Sentence: Gender was a significant moderator of some domains of cognitive performance , and decline tended to be somewhat more pronounced for women .

Example answer:
{"entities": [{"text": "cognitive performance", "type": "BiologicFunction"}, {"text": "decline tended", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: This study aims to analyze the impact of an individual reminiscence program in a group of older persons with cognitive decline living in nursing homes on the dimensions of cognition , autobiographical memory , mood , behavior and anxiety .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "individual", "type": "PopulationGroup"}, {"text": "reminiscence program", "type": "HealthCareActivity"}, {"text": "cognitive decline", "type": "BiologicFunction"}, {"text": "nursing homes", "type": "Organization"}, {"text": "cognition", "type": "BiologicFunction"}, {"text": "autobiographical memory", "type": "BiologicFunction"}, {"text": "mood", "type": "BiologicFunction"}, {"text": "anxiety", "type": "BiologicFunction"}]}

Example input:
Sentence: The data of the 43 patients whose complete measurements were taken again in September 2014 were used for the longitudinal analysis .

Example answer:
{"entities": []}

Example input:
Sentence: For disease - modifying treatments , point differences on cognitive and functional scales should be qualified with duration of treatment .

Example answer:
{"entities": [{"text": "disease", "type": "BiologicFunction"}, {"text": "treatments", "type": "HealthCareActivity"}, {"text": "cognitive", "type": "BiologicFunction"}, {"text": "functional", "type": "BiologicFunction"}, {"text": "scales", "type": "IntellectualProduct"}]}

Example input:
Sentence: In the second longitudinal analysis , in the women , changes in EQ - 5D scores were positively correlated with changes in daily step counts on all days .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "EQ - 5D", "type": "IntellectualProduct"}, {"text": "positively", "type": "Finding"}]}

Example input:
Sentence: Neuropsychological testing did not suggest true regression in cognitive , language , and academic skills , although decreases in motivation and performance were noted with a reaction to stress and multiple environmental changes as a potential causative factor .

Example answer:
{"entities": [{"text": "Neuropsychological testing", "type": "HealthCareActivity"}, {"text": "regression", "type": "BiologicFunction"}, {"text": "academic skills", "type": "BiologicFunction"}, {"text": "motivation", "type": "BiologicFunction"}, {"text": "stress", "type": "Finding"}, {"text": "environmental", "type": "SpatialConcept"}]}

Example input:
Sentence: In the fully adjusted logistic regression analysis , old age , women , low educational level and low sense of mastery were independent predictors for cognitive decline .

Example answer:
{"entities": [{"text": "low sense of mastery", "type": "Finding"}, {"text": "cognitive decline", "type": "BiologicFunction"}]}

Example input:
Sentence: We apply the method to two longitudinal datasets , one containing subjects with mild cognitive impairment along with healthy controls , the other with early dementia subjects and healthy controls .

Example answer:
{"entities": [{"text": "subjects", "type": "PopulationGroup"}, {"text": "mild cognitive impairment", "type": "BiologicFunction"}, {"text": "dementia", "type": "BiologicFunction"}]}

Example input:
Sentence: The intervention group showed significant negative absolute change on depression , anxiety , and perceived burden measures , while on the dementia -related knowledge measure , a significant positive absolute change was found at post - 1 , and post - 2 ( P < 0 . 001 ) , in comparison to controls .

Example answer:
{"entities": [{"text": "intervention group", "type": "PopulationGroup"}, {"text": "negative", "type": "Finding"}, {"text": "depression", "type": "Finding"}, {"text": "anxiety", "type": "Finding"}, {"text": "dementia", "type": "BiologicFunction"}, {"text": "knowledge", "type": "Finding"}, {"text": "positive", "type": "Finding"}]}

Example input:
Sentence: Changes in the outcome measures were examined for cognition ( Montreal Cognitive Assessment ; Autobiographical Memory Test ) , behavior ( Alzheimer Disease Assessment Subscale Non - Cog ) and emotional status ( Cornell Scale for Depression in Dementia ; Geriatric Depression Scale , and Geriatric Anxiety Inventory ) .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "cognition", "type": "BiologicFunction"}, {"text": "Montreal Cognitive Assessment", "type": "IntellectualProduct"}, {"text": "Autobiographical Memory Test", "type": "IntellectualProduct"}, {"text": "Alzheimer Disease Assessment Subscale Non - Cog", "type": "IntellectualProduct"}, {"text": "emotional status", "type": "Finding"}, {"text": "Cornell Scale for Depression", "type": "IntellectualProduct"}, {"text": "Dementia", "type": "BiologicFunction"}, {"text": "Geriatric Depression Scale", "type": "IntellectualProduct"}, {"text": "Geriatric Anxiety Inventory", "type": "IntellectualProduct"}]}

Input:
Sentence: We also aimed to examine longitudinal measurement invariance and identify factors - such as age , gender , educational level , treatment and psychopathological change scores -potentially linked to cognitive change among patients .

## Item MedMentions:test:2280
Example input:
Sentence: Further , 18 of these 20 cases also had stem cells in the metastatic nodule .

Example answer:
{"entities": [{"text": "stem cells", "type": "AnatomicalStructure"}, {"text": "metastatic nodule", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We have developed a simple method for identification and characterization of circulating cancer stem cells among circulating epithelial tumor cells ( CETCs ) .

Example answer:
{"entities": [{"text": "cancer stem cells", "type": "AnatomicalStructure"}, {"text": "circulating epithelial tumor cells", "type": "AnatomicalStructure"}, {"text": "CETCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Here , we describe the derivation and characterization , including single - cell RNA - seq , of neocortical and spinal cord neuroepithelial stem ( NES ) cells to model early human neurodevelopment and ZIKV -related neuropathogenesis .

Example answer:
{"entities": [{"text": "single - cell RNA - seq", "type": "SpatialConcept"}, {"text": "neocortical", "type": "AnatomicalStructure"}, {"text": "spinal cord", "type": "AnatomicalStructure"}, {"text": "stem ( NES ) cells", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "ZIKV", "type": "Virus"}, {"text": "neuropathogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Visualization and targeting of LGR5 ( + ) human colon cancer stem cells The cancer stem cell ( CSC ) theory highlights a self - renewing subpopulation of cancer cells that fuels tumour growth .

Example answer:
{"entities": [{"text": "Visualization", "type": "Finding"}, {"text": "LGR5 ( + )", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "colon", "type": "AnatomicalStructure"}, {"text": "cancer stem cells", "type": "AnatomicalStructure"}, {"text": "cancer stem cell", "type": "AnatomicalStructure"}, {"text": "CSC", "type": "AnatomicalStructure"}, {"text": "self - renewing", "type": "BiologicFunction"}, {"text": "subpopulation", "type": "IntellectualProduct"}, {"text": "cancer cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: There was no statistical significance between the level of CD184 in stem cell harvest and the prediction of successful engraftment ( p > 0 .

Example answer:
{"entities": [{"text": "no", "type": "Finding"}, {"text": "level", "type": "Finding"}, {"text": "CD184", "type": "Chemical"}, {"text": "stem cell harvest", "type": "HealthCareActivity"}, {"text": "engraftment", "type": "BiologicFunction"}]}

Example input:
Sentence: This population is termed cancer stem cells ( CSCs ) .

Example answer:
{"entities": [{"text": "cancer stem cells", "type": "AnatomicalStructure"}, {"text": "CSCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We generated a human embryonic stem cell ( hESC ) line carrying a naturally occurring mutation of MYPBC3 ( c . 2905 +1 G > A ) to study HCM pathogenesis during cardiac differentiation .

Example answer:
{"entities": [{"text": "mutation", "type": "BiologicFunction"}, {"text": "MYPBC3", "type": "AnatomicalStructure"}, {"text": "c . 2905 +1 G > A", "type": "BiologicFunction"}, {"text": "HCM", "type": "BiologicFunction"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "cardiac differentiation", "type": "BiologicFunction"}]}

Example input:
Sentence: ADSCs retained stem cell phenotype after 30 days and satisfied the International Society for Cellular Therapy 's ( ISCT ) minimal criteria for MSCs .

Example answer:
{"entities": [{"text": "ADSCs", "type": "AnatomicalStructure"}, {"text": "stem cell", "type": "AnatomicalStructure"}, {"text": "International Society for Cellular Therapy 's", "type": "Organization"}, {"text": "ISCT", "type": "Organization"}, {"text": "MSCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Stem Cells Translational Medicine 2017 ; 6 : 799 - 806 .

Example answer:
{"entities": []}

Example input:
Sentence: Stem Cells Translational Medicine 2017 ; 6 : 1273 - 1285 .

Example answer:
{"entities": []}

Input:
Sentence: Stem Cells 2017 ; 35 : 641 - 653 .

## Item MedMentions:test:2035
Example input:
Sentence: First complete genome sequence of parainfluenza virus 5 isolated from lesser panda Parainfluenza virus 5 ( PIV5 ) is widespread in mammals and humans .

Example answer:
{"entities": [{"text": "genome sequence", "type": "AnatomicalStructure"}, {"text": "parainfluenza virus 5", "type": "Virus"}, {"text": "lesser panda", "type": "Eukaryote"}, {"text": "Parainfluenza virus 5", "type": "Virus"}, {"text": "PIV5", "type": "Virus"}, {"text": "mammals", "type": "Eukaryote"}, {"text": "humans", "type": "Eukaryote"}]}

Example input:
Sentence: Infectivity , effects on helper viruses and whitefly transmission of the deltasatellites associated with sweepoviruses ( genus Begomovirus , family Geminiviridae ) Begomoviruses ( family Geminiviridae ) are whitefly - transmitted viruses with single - stranded DNA genomes that are frequently associated with DNA satellites .

Example answer:
{"entities": [{"text": "helper viruses", "type": "Virus"}, {"text": "whitefly", "type": "Eukaryote"}, {"text": "transmission", "type": "BiologicFunction"}, {"text": "deltasatellites", "type": "Virus"}, {"text": "sweepoviruses", "type": "Virus"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Begomovirus", "type": "Virus"}, {"text": "family Geminiviridae", "type": "Virus"}, {"text": "Begomoviruses", "type": "Virus"}, {"text": "Geminiviridae", "type": "Virus"}, {"text": "transmitted", "type": "BiologicFunction"}, {"text": "viruses", "type": "Virus"}, {"text": "single - stranded DNA genomes", "type": "AnatomicalStructure"}, {"text": "DNA satellites", "type": "Chemical"}]}

Example input:
Sentence: In this work , we have used deep metagenomic sequencing to assemble eight complete genomes of the first tailed phages that infect freshwater Actinobacteria .

Example answer:
{"entities": [{"text": "metagenomic sequencing", "type": "ResearchActivity"}, {"text": "genomes", "type": "AnatomicalStructure"}, {"text": "infect", "type": "Finding"}, {"text": "Actinobacteria", "type": "Bacterium"}]}

Example input:
Sentence: We report here the complete nucleotide sequence and genome organization of DcFLV , the largest flavi - like virus identified to date .

Example answer:
{"entities": [{"text": "nucleotide sequence", "type": "SpatialConcept"}, {"text": "genome organization", "type": "AnatomicalStructure"}, {"text": "DcFLV", "type": "Virus"}, {"text": "flavi - like virus", "type": "Virus"}]}

Example input:
Sentence: First complete genome sequence of a virulent bacteriophage infecting the opportunistic pathogen Serratia rubidaea A Serratia rubidaea phage , vB _ Sru IME250 , was isolated from hospital sewage .

Example answer:
{"entities": [{"text": "genome sequence", "type": "SpatialConcept"}, {"text": "bacteriophage", "type": "Virus"}, {"text": "infecting", "type": "Finding"}, {"text": "Serratia rubidaea", "type": "Bacterium"}, {"text": "Serratia rubidaea phage , vB _ Sru IME250", "type": "Virus"}, {"text": "hospital", "type": "Organization"}]}

Example input:
Sentence: Complete study demonstrating the absence of rhabdovirus in a distinct Sf9 cell line A putative novel rhabdovirus ( SfRV ) was previously identified in a Spodoptera frugiperda cell line ( Sf9 cells [ ATCC CRL - 1711 lot 58078522 ] ) by next generation sequencing and extensive bioinformatic analysis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "rhabdovirus", "type": "Virus"}, {"text": "SfRV", "type": "Virus"}, {"text": "Sf9 cells", "type": "AnatomicalStructure"}, {"text": "ATCC CRL - 1711 lot 58078522", "type": "AnatomicalStructure"}, {"text": "next generation sequencing", "type": "ResearchActivity"}, {"text": "bioinformatic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Complete Genome Sequence of the Largest Known Flavi - Like Virus , Diaphorina citri flavi - like virus , a Novel Virus of the Asian Citrus Psyllid , Diaphorina citri A novel flavi - like virus tentatively named Diaphorina citri flavi - like virus ( DcFLV ) was identified in field populations of Diaphorina citri through small RNA and transcriptome sequencing followed by reverse transcription ( RT ) - PCR .

Example answer:
{"entities": [{"text": "Complete Genome Sequence", "type": "SpatialConcept"}, {"text": "Flavi - Like Virus", "type": "Virus"}, {"text": "Diaphorina citri flavi - like virus", "type": "Virus"}, {"text": "Virus", "type": "Virus"}, {"text": "Asian Citrus", "type": "Eukaryote"}, {"text": "Psyllid", "type": "Eukaryote"}, {"text": "Diaphorina citri", "type": "Eukaryote"}, {"text": "flavi - like virus", "type": "Virus"}, {"text": "DcFLV", "type": "Virus"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "small RNA", "type": "Chemical"}, {"text": "transcriptome sequencing", "type": "HealthCareActivity"}, {"text": "reverse transcription ( RT ) - PCR", "type": "ResearchActivity"}]}

Example input:
Sentence: Complete Genome Sequence Analysis of a Naturally Reassorted Infectious Bursal Disease Virus from India The novel infectious bursal disease virus ( IBDV ) isolate BGE14 / ABT1 / MVC / India is a very virulent IBDV that was isolated from broiler flocks in southern parts of India during 2014 .

Example answer:
{"entities": [{"text": "Genome Sequence Analysis", "type": "HealthCareActivity"}, {"text": "Infectious Bursal Disease Virus", "type": "Virus"}, {"text": "India", "type": "SpatialConcept"}, {"text": "infectious bursal disease virus", "type": "Virus"}, {"text": "IBDV", "type": "Virus"}, {"text": "isolate", "type": "Chemical"}, {"text": "BGE14 / ABT1 / MVC / India", "type": "Virus"}, {"text": "isolated", "type": "Chemical"}, {"text": "broiler flocks", "type": "Eukaryote"}]}

Example input:
Sentence: Here , we report , for the first time in India , the complete genome sequence of BGE14 / ABT1 / MVC / India , a reassortment strain with segments A and B derived from a very virulent IBDV strain and an attenuated IBDV , respectively .

Example answer:
{"entities": [{"text": "India", "type": "SpatialConcept"}, {"text": "genome sequence", "type": "AnatomicalStructure"}, {"text": "BGE14 / ABT1 / MVC / India", "type": "Virus"}, {"text": "segments A and B", "type": "AnatomicalStructure"}, {"text": "IBDV", "type": "Virus"}]}

Example input:
Sentence: Characterization of Beak and Feather Disease Virus Genomes from Wild Musk Lorikeets ( Glossopsitta concinna ) Three complete genomes of beak and feather disease virus ( BFDV ) were recovered from wild musk lorikeets ( Glossopsitta concinna ) .

Example answer:
{"entities": [{"text": "Beak and Feather Disease Virus", "type": "Virus"}, {"text": "Genomes", "type": "AnatomicalStructure"}, {"text": "Wild", "type": "IntellectualProduct"}, {"text": "Musk Lorikeets", "type": "Eukaryote"}, {"text": "Glossopsitta concinna", "type": "Eukaryote"}, {"text": "genomes", "type": "AnatomicalStructure"}, {"text": "beak and feather disease virus", "type": "Virus"}, {"text": "BFDV", "type": "Virus"}, {"text": "wild", "type": "IntellectualProduct"}, {"text": "musk lorikeets", "type": "Eukaryote"}]}

Input:
Sentence: This is the first report of BFDV complete genome sequences obtained from this host species .

## Item MedMentions:test:1998
Example input:
Sentence: Specifically , relative to controls , children with ASD showed decreased fixations to KIC centers , indicating reduced global perception .

Example answer:
{"entities": [{"text": "ASD", "type": "BiologicFunction"}, {"text": "fixations", "type": "BiologicFunction"}, {"text": "KIC centers", "type": "Organization"}, {"text": "perception", "type": "BiologicFunction"}]}

Example input:
Sentence: Two main effects were found : higher parental psychopathology and ASD severity were both related to lower expectations .

Example answer:
{"entities": [{"text": "psychopathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "ASD", "type": "BiologicFunction"}]}

Example input:
Sentence: Besides the measure of child ASD symptoms , parents completed a survey of their child 's interest in and familiarity with the play session toys .

Example answer:
{"entities": [{"text": "ASD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "survey", "type": "IntellectualProduct"}, {"text": "interest", "type": "BiologicFunction"}, {"text": "familiarity", "type": "BiologicFunction"}]}

Example input:
Sentence: School - aged children with ASD ( n = 28 ) and age - matched typically developing controls ( n = 22 ; 7 - 13 years ) performed a sequential match - to - sample between a solid shape ( sample ) and two illusory alternatives .

Example answer:
{"entities": [{"text": "ASD", "type": "BiologicFunction"}, {"text": "solid shape", "type": "SpatialConcept"}, {"text": "illusory alternatives", "type": "Finding"}]}

Example input:
Sentence: Forty children ( Mage = 6 ; 5 , SDage = 1 . 45 ; 29 males ) , six of whom met the threshold for ASD diagnosis via parent -reported ASD symptoms , participated in play sessions and completed measures of verbal IQ and ToM .

Example answer:
{"entities": [{"text": "ASD", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: Implications for assessment and subsequent treatment for pretend ability among children with varying degrees of ASD symptoms , as well as for future research , are discussed .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "ASD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: Since ASD traits exist along a continuum in the general population , investigating how pretend play varies across the range of ASD symptoms by indexing variations in ASD traits in both typically developing and ASD populations may provide insight into how ASD symptoms may influence the relation between pretend play and associated processes in cognitive development .

Example answer:
{"entities": [{"text": "ASD", "type": "BiologicFunction"}, {"text": "continuum", "type": "SpatialConcept"}, {"text": "general population", "type": "PopulationGroup"}, {"text": "symptoms", "type": "Finding"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "cognitive development", "type": "BiologicFunction"}]}

Example input:
Sentence: Predictors and Moderators of Spontaneous Pretend Play in Children with and without Autism Spectrum Disorder Although pretend play has long been linked to children 's normative cognitive development , inconsistent findings call for greater rigor in examining this relation ( Lillard et al . , 2013 ) .

Example answer:
{"entities": [{"text": "Autism Spectrum Disorder", "type": "BiologicFunction"}, {"text": "cognitive development", "type": "BiologicFunction"}, {"text": "findings", "type": "Finding"}]}

Example input:
Sentence: First , among children with more ASD symptoms , verbal ability marginally negatively predicted pretend play production .

Example answer:
{"entities": [{"text": "ASD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "production", "type": "BiologicFunction"}]}

Example input:
Sentence: Further probing revealed that the negative effect of ASD symptoms on pretend play was simultaneously moderated by both variables : low ToM and high verbal ability both related to less pretend play production among children with more ASD symptoms .

Example answer:
{"entities": [{"text": "ASD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}]}

Input:
Sentence: Second , among children with fewer ASD symptoms , ToM negatively predicted pretend play production .

## Item MedMentions:test:2084
Example input:
Sentence: MR - EFW was calculated using a semi - automated method at 38 . 6 weeks of gestation in 36 patients and compared to the picture archiving and communication system ( PACS ) .

Example answer:
{"entities": [{"text": "method", "type": "IntellectualProduct"}, {"text": "gestation", "type": "BiologicFunction"}, {"text": "picture archiving and communication system", "type": "MedicalDevice"}, {"text": "PACS", "type": "MedicalDevice"}]}

Example input:
Sentence: Pregnancies conceived with ovum donation and women older than 45 years were excluded .

Example answer:
{"entities": [{"text": "Pregnancies", "type": "BiologicFunction"}, {"text": "ovum donation", "type": "HealthCareActivity"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Even after controlling for significant variables , there remained a 73 % reduction in delivery at less than 24 weeks of gestation in the cerclage plus 17α - hydroxyprogesterone caproate cohort ( adjusted OR 0 . 26 , P = . 02 ) .

Example answer:
{"entities": [{"text": "delivery", "type": "BiologicFunction"}, {"text": "24 weeks of gestation", "type": "Finding"}, {"text": "17α - hydroxyprogesterone caproate", "type": "Chemical"}, {"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: There was no difference in gestation ( 40 . 0 [ 39 . 1 - 40 . 3 ] vs 39 .

Example answer:
{"entities": [{"text": "gestation", "type": "BiologicFunction"}]}

Example input:
Sentence: In July 2014 , the American Academy of Pediatrics ( AAP ) Committee on Infectious Diseases concluded that the " limited clinical benefit " for infants born at more than 29 weeks ' gestation , together with the associated high cost of the immunoprophylaxis , no longer supported the routine use of palivizumab ( Synagis ) .

Example answer:
{"entities": [{"text": "American Academy of Pediatrics ( AAP ) Committee", "type": "Organization"}, {"text": "Infectious Diseases", "type": "BiologicFunction"}, {"text": "weeks ' gestation ,", "type": "Finding"}, {"text": "immunoprophylaxis", "type": "HealthCareActivity"}, {"text": "palivizumab", "type": "Chemical"}, {"text": "Synagis", "type": "Chemical"}]}

Example input:
Sentence: Forty aborted human fetuses ( 25 male and 15 female ) of 12 - 40 weeks gestational age with no obvious congenital abnormality were obtained .

Example answer:
{"entities": [{"text": "aborted human fetuses", "type": "AnatomicalStructure"}, {"text": "weeks", "type": "Finding"}, {"text": "no", "type": "Finding"}, {"text": "congenital abnormality", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Women delivered at a mean gestational age of 38 .

Example answer:
{"entities": [{"text": "Women", "type": "PopulationGroup"}]}

Example input:
Sentence: Delivery at less than 24 weeks of gestation occurred in 6 % of women receiving both 17α - hydroxyprogesterone caproate and cerclage compared with 16 % in the cerclage only group ( odds ratio [ OR ] 0 . 31 , 95 % confidence interval 0 .

Example answer:
{"entities": [{"text": "Delivery", "type": "BiologicFunction"}, {"text": "24 weeks of gestation", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "17α - hydroxyprogesterone caproate", "type": "Chemical"}, {"text": "group", "type": "PopulationGroup"}]}

Example input:
Sentence: In total , four women ( 9 . 3 % ) delivered the second pregnancy < 37 weeks : three had a prior term VD and one had a prior 34 weeks VD .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "delivered", "type": "Finding"}, {"text": "pregnancy", "type": "BiologicFunction"}, {"text": "term", "type": "BiologicFunction"}, {"text": "VD", "type": "HealthCareActivity"}]}

Example input:
Sentence: The association patterns were similar , when we restricted to participants who delivered by emergency cesarean ( 1 . 4 , 1 . 1 , 1 . 9 ) , or who delivered after 35 weeks of gestation ( 1 . 4 , 1 .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "delivered", "type": "HealthCareActivity"}, {"text": "emergency cesarean", "type": "HealthCareActivity"}]}

Input:
Sentence: All but two subjects were delivered beyond 39 weeks ' gestation .

## Item MedMentions:test:1852
Example input:
Sentence: In contrast , compared with eIF4G1 , NAT1 preferentially interacted with eIF2 , fragile X mental retardation proteins ( FMR ) , and related proteins and especially with members of the proline - rich and coiled - coil - containing protein 2 ( PRRC2 ) family .

Example answer:
{"entities": [{"text": "eIF4G1", "type": "Chemical"}, {"text": "NAT1", "type": "Chemical"}, {"text": "eIF2", "type": "Chemical"}, {"text": "fragile X mental retardation proteins", "type": "Chemical"}, {"text": "FMR", "type": "Chemical"}, {"text": "proteins", "type": "Chemical"}, {"text": "proline - rich and coiled - coil - containing protein 2", "type": "Chemical"}, {"text": "PRRC2", "type": "Chemical"}, {"text": "family", "type": "Chemical"}]}

Example input:
Sentence: During TSA -mediated acetylation in culture , a time - dependent increase in secreted APE1 / Ref - 1 was confirmed .

Example answer:
{"entities": [{"text": "TSA", "type": "Chemical"}, {"text": "acetylation", "type": "BiologicFunction"}, {"text": "culture", "type": "HealthCareActivity"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "APE1", "type": "Chemical"}, {"text": "Ref - 1", "type": "Chemical"}, {"text": "confirmed", "type": "Finding"}]}

Example input:
Sentence: APE1 / Ref - 1 is essential for cellular survival and embryonic lethal in knockout mouse models .

Example answer:
{"entities": [{"text": "APE1", "type": "Chemical"}, {"text": "Ref - 1", "type": "Chemical"}, {"text": "cellular survival", "type": "BiologicFunction"}, {"text": "embryonic lethal", "type": "BiologicFunction"}, {"text": "knockout mouse", "type": "Eukaryote"}, {"text": "models", "type": "Eukaryote"}]}

Example input:
Sentence: Heterozygous APE1 / Ref - 1 mice showed impaired endothelium -dependent vasorelaxation , reduced vascular NO levels , and are hypertensive .

Example answer:
{"entities": [{"text": "APE1", "type": "Chemical"}, {"text": "Ref - 1 mice", "type": "Chemical"}, {"text": "impaired", "type": "InjuryOrPoisoning"}, {"text": "endothelium", "type": "AnatomicalStructure"}, {"text": "vasorelaxation", "type": "BiologicFunction"}, {"text": "vascular", "type": "AnatomicalStructure"}, {"text": "NO levels", "type": "HealthCareActivity"}, {"text": "hypertensive", "type": "Finding"}]}

Example input:
Sentence: These results strongly indicate that anti - inflammatory effects of secreted APE1 / Ref - 1 and its property of secreted APE1 / Ref - 1 may be useful as a therapeutic biomolecule in cardiovascular disease .

Example answer:
{"entities": [{"text": "secreted", "type": "BiologicFunction"}, {"text": "APE1", "type": "Chemical"}, {"text": "Ref - 1", "type": "Chemical"}, {"text": "cardiovascular disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , rh APE1 / Ref - 1 inhibited IL - 1β - induced VCAM - 1 expression in endothelial cells , and it inhibited iNOS or COX - 2 expression in lipopolysaccharide -stimulated RAW 264 .

Example answer:
{"entities": [{"text": "rh", "type": "Chemical"}, {"text": "APE1", "type": "Chemical"}, {"text": "Ref - 1", "type": "Chemical"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "VCAM - 1", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "endothelial cells", "type": "AnatomicalStructure"}, {"text": "iNOS", "type": "Chemical"}, {"text": "COX - 2", "type": "Chemical"}, {"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "RAW 264 .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We investigated the functions of extracellular APE1 / Ref - 1 with respect to leading anti - inflammatory signaling in TNF - α -stimulated endothelial cells in response to acetylation .

Example answer:
{"entities": [{"text": "functions", "type": "BiologicFunction"}, {"text": "extracellular", "type": "AnatomicalStructure"}, {"text": "APE1", "type": "Chemical"}, {"text": "Ref - 1", "type": "Chemical"}, {"text": "anti - inflammatory signaling", "type": "BiologicFunction"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "endothelial cells", "type": "AnatomicalStructure"}, {"text": "response", "type": "BiologicFunction"}, {"text": "acetylation", "type": "BiologicFunction"}]}

Example input:
Sentence: Recently , it was shown that APE1 / Ref - 1 is secreted in response to hyperacetylation at specific lysine residues .

Example answer:
{"entities": [{"text": "APE1", "type": "Chemical"}, {"text": "Ref - 1", "type": "Chemical"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "response to hyperacetylation", "type": "BiologicFunction"}, {"text": "lysine residues", "type": "Chemical"}]}

Example input:
Sentence: Following treatment with the neutralizing anti - APE1 / Ref - 1 antibody , inflammatory signals via the binding of TNF - α to TNFR1 were remarkably recovered .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "neutralizing", "type": "Chemical"}, {"text": "APE1", "type": "Chemical"}, {"text": "Ref - 1", "type": "Chemical"}, {"text": "antibody", "type": "Chemical"}, {"text": "inflammatory signals", "type": "BiologicFunction"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "TNFR1", "type": "Chemical"}]}

Example input:
Sentence: APE1 / Ref - 1 reduces intracellular reactive oxygen species production by negatively regulating the activity of the NADPH oxidase .

Example answer:
{"entities": [{"text": "APE1", "type": "Chemical"}, {"text": "Ref - 1", "type": "Chemical"}, {"text": "intracellular", "type": "SpatialConcept"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "negatively regulating the activity of the NADPH oxidase", "type": "BiologicFunction"}]}

Input:
Sentence: Recombinant human APE1 / Ref - 1 with reducing activity induced a conformational change in TNFR1 by thiol - disulfide exchange .

## Item MedMentions:test:1939
Example input:
Sentence: L1 retrotransposon expression in circulating tumor cells Long interspersed nuclear element 1 ( LINE - 1 or L1 ) belongs to the non - long terminal repeat ( non - LTR ) retrotransposon family , which has been implicated in carcinogenesis and disease progression .

Example answer:
{"entities": [{"text": "L1 retrotransposon", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "circulating tumor cells", "type": "AnatomicalStructure"}, {"text": "Long interspersed nuclear element 1", "type": "Chemical"}, {"text": "LINE - 1", "type": "Chemical"}, {"text": "L1", "type": "Chemical"}, {"text": "non - long terminal repeat ( non - LTR ) retrotransposon family", "type": "Chemical"}, {"text": "carcinogenesis", "type": "BiologicFunction"}, {"text": "disease progression", "type": "BiologicFunction"}]}

Example input:
Sentence: But serum PVT1 level is not changed in breast cancer and ovarian cancer patients .

Example answer:
{"entities": [{"text": "serum", "type": "BodySubstance"}, {"text": "PVT1", "type": "Chemical"}]}

Example input:
Sentence: Cervical fibronectin was the biomarkers which showed the highest strength of association with the occurrence of SPTB ( delivery within 24 h OR 7 , 95 % CI 3 - 17 ; delivery < 7 days ( OR 12 , 95 % CI 8 - 16 ) .

Example answer:
{"entities": [{"text": "Cervical fibronectin", "type": "Chemical"}, {"text": "biomarkers", "type": "ClinicalAttribute"}, {"text": "SPTB", "type": "Finding"}, {"text": "delivery", "type": "BiologicFunction"}]}

Example input:
Sentence: Long noncoding RNA XIST acts as an oncogene in non - small cell lung cancer by epigenetically repressing KLF2 expression Recently , long noncoding RNAs ( lncRNAs ) have been identified as critical regulators in numerous types of cancers , including non - small cell lung cancer ( NSCLC ) .

Example answer:
{"entities": [{"text": "Long noncoding RNA", "type": "Chemical"}, {"text": "XIST", "type": "Chemical"}, {"text": "oncogene", "type": "AnatomicalStructure"}, {"text": "non - small cell lung cancer", "type": "BiologicFunction"}, {"text": "epigenetically repressing", "type": "BiologicFunction"}, {"text": "KLF2", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "long noncoding RNAs", "type": "Chemical"}, {"text": "lncRNAs", "type": "Chemical"}, {"text": "regulators", "type": "AnatomicalStructure"}, {"text": "cancers", "type": "BiologicFunction"}, {"text": "NSCLC", "type": "BiologicFunction"}]}

Example input:
Sentence: Quantitative RT - PCR was used to measure miR - 376c expression in cervical cancer tissues and cell lines .

Example answer:
{"entities": [{"text": "Quantitative RT - PCR", "type": "ResearchActivity"}, {"text": "miR - 376c", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "cervical cancer", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "cell lines", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Previous studies have suggested that long non‑coding RNAs ( lncRNAs ) may be key regulators of tumor development and progression in HCC .

Example answer:
{"entities": [{"text": "long non‑coding RNAs", "type": "Chemical"}, {"text": "lncRNAs", "type": "Chemical"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "HCC", "type": "BiologicFunction"}]}

Example input:
Sentence: Long Non - Coding RNA SNHG6 as a Potential Biomarker for Hepatocellular Carcinoma Long Non - coding RNAs ( lncRNAs ) refer to all non - protein coding transcripts longer than 200 nucleotides .

Example answer:
{"entities": [{"text": "Long Non - Coding RNA", "type": "Chemical"}, {"text": "SNHG6", "type": "AnatomicalStructure"}, {"text": "Biomarker", "type": "Chemical"}, {"text": "Hepatocellular Carcinoma", "type": "BiologicFunction"}, {"text": "Long Non - coding RNAs", "type": "Chemical"}, {"text": "lncRNAs", "type": "Chemical"}, {"text": "non - protein coding", "type": "Chemical"}, {"text": "transcripts", "type": "Chemical"}, {"text": "nucleotides", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , serum PVT1 level is positively correlated with tissue PVT1 expression , and could indicate cervical cancer dynamics .

Example answer:
{"entities": [{"text": "serum", "type": "BodySubstance"}, {"text": "PVT1", "type": "Chemical"}, {"text": "PVT1", "type": "AnatomicalStructure"}, {"text": "cervical cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: PVT1 serum level in these participants and PVT1 expression in 20 pairs of cervical cancer tissues and adjacent paired normal tissues was measured by quantitative reverse transcription - polymerase chain reaction .

Example answer:
{"entities": [{"text": "PVT1", "type": "Chemical"}, {"text": "serum", "type": "BodySubstance"}, {"text": "PVT1", "type": "AnatomicalStructure"}, {"text": "cervical cancer", "type": "BiologicFunction"}, {"text": "reverse transcription - polymerase chain reaction", "type": "ResearchActivity"}]}

Example input:
Sentence: Serum PVT1 could accurately discriminate cervical cancer patients from cervical intraepithelial neoplasia patients and healthy control subjects , and also discriminate early stage cervical cancer patients from healthy control subjects .

Example answer:
{"entities": [{"text": "Serum", "type": "BodySubstance"}, {"text": "PVT1", "type": "Chemical"}, {"text": "cervical cancer", "type": "BiologicFunction"}, {"text": "cervical intraepithelial neoplasia", "type": "BiologicFunction"}]}

Input:
Sentence: Long noncoding RNA PVT1 may be a novel noninvasive biomarker for early diagnosis of cervical cancer .

## Item MedMentions:test:2197
Example input:
Sentence: C1q + Ab and LABScreen SAB DSA - MFI were significantly associated with FXM .

Example answer:
{"entities": [{"text": "C1q + Ab", "type": "Chemical"}, {"text": "LABScreen SAB", "type": "Chemical"}, {"text": "DSA", "type": "Chemical"}, {"text": "FXM", "type": "HealthCareActivity"}]}

Example input:
Sentence: We included in the study 32 healthy subjects and 32 MS patients : 10 naive , 10 early treated and 12 late treated with INF - β1a .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "healthy subjects", "type": "PopulationGroup"}, {"text": "MS", "type": "BiologicFunction"}, {"text": "INF - β1a", "type": "Chemical"}]}

Example input:
Sentence: 64 ( 95 % CI -0 . 23 - 3 . 50 ) , and Borg 0 . 46 ( 95 % CI 0 . 07 - 0 . 84 ) .

Example answer:
{"entities": [{"text": "Borg 0 . 46", "type": "Finding"}]}

Example input:
Sentence: Cortex FA , age , disease duration , T2 WM LV , and GMV best predicted MS -related cognitive impairment ( C - statistic = 0 . 88 ) . " Diffuse " GM and NAWM damage and WM lesions , rather than intrinsic CL damage , contribute to cognitive impairment in MS .

Example answer:
{"entities": [{"text": "Cortex", "type": "AnatomicalStructure"}, {"text": "MS", "type": "BiologicFunction"}, {"text": "cognitive impairment", "type": "BiologicFunction"}, {"text": "Diffuse", "type": "SpatialConcept"}, {"text": "GM", "type": "AnatomicalStructure"}, {"text": "NAWM", "type": "AnatomicalStructure"}, {"text": "WM lesions", "type": "Finding"}, {"text": "intrinsic", "type": "SpatialConcept"}, {"text": "CL", "type": "BiologicFunction"}]}

Example input:
Sentence: 108 and MSE = 0 . 061 respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 6 ms , p < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 64 , 1 . 04 and 1 . 44V , and good linear current responses were obtained with the detection limits of 18ngmL ( - 1 ) ( 1 . 2×10 ( - 9 ) M ) , 11 .

Example answer:
{"entities": []}

Example input:
Sentence: MS188 complexed with AMS .

Example answer:
{"entities": [{"text": "MS188", "type": "Chemical"}, {"text": "AMS", "type": "Chemical"}]}

Example input:
Sentence: The following criteria were assigned one point : initial dominant R wave in V1 ; initial r > 40 ms in V1 or V2 ; notched S in V1 ; initial R wave in a VR ; lead II RWPT ≥50 ms ; and absence of an RS in leads V1 - V6 .

Example answer:
{"entities": [{"text": "dominant R wave", "type": "Finding"}, {"text": "R wave", "type": "Finding"}, {"text": "VR", "type": "BiologicFunction"}]}

Example input:
Sentence: The parameters for T2DM group were : Cmax 23 . 52 ng ml ( - 1 ) , tmax 1 .

Example answer:
{"entities": [{"text": "T2DM", "type": "BiologicFunction"}, {"text": "group", "type": "PopulationGroup"}]}

Input:
Sentence: Active drivers ( N = 102 ) with various types of MS .

## Item MedMentions:test:2124
Example input:
Sentence: The assembled 37 . 1 Mb genome encodes 12 , 155 putative coding genes , of which , 1 . 01 % are predicted transposable elements .

Example answer:
{"entities": [{"text": "genome", "type": "AnatomicalStructure"}, {"text": "coding genes", "type": "AnatomicalStructure"}, {"text": "transposable elements", "type": "Chemical"}]}

Example input:
Sentence: We have set up an NGS protocol based on a specific selection of DNA regions belonging to about 900 genes of the autophagy - lysosomal ( ALP ) pathway .

Example answer:
{"entities": [{"text": "NGS", "type": "ResearchActivity"}, {"text": "protocol", "type": "IntellectualProduct"}, {"text": "DNA regions", "type": "Chemical"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "autophagy - lysosomal ( ALP ) pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: A total of 4 , 976 SNPs from the 9 K iSelect array were used in the study for the analysis of population structure , linkage disequilibrium ( LD ) and genome - wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "SNPs", "type": "SpatialConcept"}, {"text": "study", "type": "ResearchActivity"}, {"text": "genome - wide association study", "type": "ResearchActivity"}, {"text": "GWAS", "type": "ResearchActivity"}]}

Example input:
Sentence: 1 . This region contains 95 genes and seven microRNAs , none of which have been implicated in a disease resulting from increased gene dosage .

Example answer:
{"entities": [{"text": "1", "type": "AnatomicalStructure"}, {"text": "region", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "microRNAs", "type": "Chemical"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: A 1784 . 28 cM ( centimorgans ) linkage map , harboring 2618 polymorphic SNP markers , was constructed , which had 0 . 68 cM per marker density .

Example answer:
{"entities": [{"text": "linkage map", "type": "HealthCareActivity"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "markers", "type": "BiologicFunction"}, {"text": "marker", "type": "BiologicFunction"}]}

Example input:
Sentence: A comparative analysis of the full genome showed only 73 .

Example answer:
{"entities": [{"text": "comparative analysis", "type": "ResearchActivity"}, {"text": "genome", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The genome assembly comprised 2 , 616 , 174 bp with 34 .

Example answer:
{"entities": [{"text": "genome assembly", "type": "SpatialConcept"}, {"text": "bp", "type": "BiologicFunction"}]}

Example input:
Sentence: The long - read data represented only ~5 - 10 % of an average MinION ( TM ) run ( ~7x genomic coverage ) , but , using standard tools , this was sufficient to complete the circular chromosome of S .

Example answer:
{"entities": [{"text": "long - read data", "type": "IntellectualProduct"}, {"text": "MinION ( TM )", "type": "MedicalDevice"}, {"text": "genomic", "type": "AnatomicalStructure"}, {"text": "tools", "type": "IntellectualProduct"}, {"text": "circular chromosome", "type": "AnatomicalStructure"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: The genome comprised 2 , 748 , 608 bp with a G + C content of 34 .

Example answer:
{"entities": [{"text": "genome", "type": "AnatomicalStructure"}, {"text": "bp", "type": "Chemical"}]}

Example input:
Sentence: Here we present the first individually cloned CRISPR - Cas9 genome wide arrayed sgRNA libraries covering 17 , 166 human and 20 , 430 mouse genes at a complexity of 34 , 332 sgRNAs for human and 40 , 860 sgRNAs for the mouse genome .

Example answer:
{"entities": [{"text": "cloned", "type": "ResearchActivity"}, {"text": "CRISPR - Cas9 genome", "type": "AnatomicalStructure"}, {"text": "sgRNA", "type": "Chemical"}, {"text": "libraries", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "sgRNAs", "type": "Chemical"}, {"text": "genome", "type": "AnatomicalStructure"}]}

Input:
Sentence: Results indicated that a total of 49 , 151 core regions with an average length of 9 . 79 Kb were identified , which occupied approximately 52 . 15 % of genome across all autosomes , and 806 significant core regions attracted us mostly .

## Item MedMentions:test:1784
Example input:
Sentence: Well , I Wouldn ' t be Any Worse Off , Would I , Than I am Now ? A Qualitative Study of Decision - Making , Hopes , and Realities of Adults With Type 1 Diabetes Undergoing Islet Cell Transplantation For selected individuals with type 1 diabetes , pancreatic islet transplantation ( IT ) prevents recurrent severe hypoglycemia and optimizes glycemia , although ongoing systemic immunosuppression is needed .

Example answer:
{"entities": [{"text": "Qualitative Study", "type": "ResearchActivity"}, {"text": "Decision - Making", "type": "BiologicFunction"}, {"text": "Hopes", "type": "BiologicFunction"}, {"text": "Type 1 Diabetes", "type": "BiologicFunction"}, {"text": "Islet Cell Transplantation", "type": "HealthCareActivity"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "type 1 diabetes", "type": "BiologicFunction"}, {"text": "pancreatic islet transplantation", "type": "HealthCareActivity"}, {"text": "IT", "type": "HealthCareActivity"}, {"text": "hypoglycemia", "type": "BiologicFunction"}, {"text": "optimizes glycemia", "type": "HealthCareActivity"}, {"text": "systemic immunosuppression", "type": "HealthCareActivity"}]}

Example input:
Sentence: Eighty female volunteers were recruited , blood pressure and body measurements were recorded and a fasting blood sample was obtained for the quantitation of glucose , lipid profile , insulin , leptin and identification of ACE I / D polymorphs .

Example answer:
{"entities": [{"text": "female", "type": "PopulationGroup"}, {"text": "volunteers", "type": "PopulationGroup"}, {"text": "blood pressure", "type": "HealthCareActivity"}, {"text": "body measurements", "type": "HealthCareActivity"}, {"text": "fasting", "type": "Finding"}, {"text": "blood sample", "type": "BodySubstance"}, {"text": "glucose", "type": "Chemical"}, {"text": "lipid profile", "type": "HealthCareActivity"}, {"text": "insulin ,", "type": "Chemical"}, {"text": "leptin", "type": "Chemical"}, {"text": "ACE I / D polymorphs", "type": "Finding"}]}

Example input:
Sentence: Dried blood spot ( DBS ) sampling and blood collection with heparinized capillaries are the standard techniques .

Example answer:
{"entities": [{"text": "Dried blood spot ( DBS ) sampling", "type": "HealthCareActivity"}, {"text": "blood collection", "type": "HealthCareActivity"}, {"text": "techniques", "type": "HealthCareActivity"}]}

Example input:
Sentence: Rotation - Driven Microfluidic Disc for White Blood Cell Enumeration Using Magnetic Bead Aggregation We recently defined a magnetic bead - based assay that exploited an agglutination -like response for DNA and applied it to DNA - containing cell enumeration using inexpensive benchtop hardware [ J . Am .

Example answer:
{"entities": [{"text": "Rotation - Driven Microfluidic Disc", "type": "MedicalDevice"}, {"text": "White Blood Cell Enumeration", "type": "HealthCareActivity"}, {"text": "magnetic bead - based assay", "type": "HealthCareActivity"}, {"text": "agglutination", "type": "Finding"}, {"text": "DNA", "type": "Chemical"}, {"text": "cell", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The overall proportion of patients seeking RYGB with type 2 diabetes was higher than with SG ( 36 versus 25 % ) , but SG has now overtaken RYGB as the most common procedure among diabetics .

Example answer:
{"entities": [{"text": "RYGB", "type": "HealthCareActivity"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "SG", "type": "HealthCareActivity"}, {"text": "procedure", "type": "HealthCareActivity"}, {"text": "diabetics", "type": "Finding"}]}

Example input:
Sentence: Herein , we evaluated whether 1 - hour post - load plasma glucose ≥155 mg / dl combined with HbA1c may identify pre - diabetic individuals with a higher cardio - metabolic risk .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: 33 patients ( 51 eyes ) with a history of diabetes underwent imaging with a 68 kHz Cirrus - 5000 spectral domain OMAG prototype .

Example answer:
{"entities": [{"text": "eyes", "type": "AnatomicalStructure"}, {"text": "history of diabetes", "type": "Finding"}, {"text": "imaging", "type": "HealthCareActivity"}, {"text": "spectral domain OMAG", "type": "MedicalDevice"}]}

Example input:
Sentence: However , perfect agreement between HbA1c measured on wet VAMS and capillary microsamples was obtained .

Example answer:
{"entities": [{"text": "HbA1c", "type": "Chemical"}, {"text": "wet VAMS", "type": "HealthCareActivity"}, {"text": "capillary microsamples", "type": "BodySubstance"}]}

Example input:
Sentence: In the present study we explored the feasibility of HbA1c monitoring with VAMS sampling at home and analysis in the laboratory .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "VAMS sampling", "type": "HealthCareActivity"}, {"text": "home", "type": "SpatialConcept"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "laboratory", "type": "Organization"}]}

Example input:
Sentence: Utilizing equipment standard available in the clinical laboratory , the use of home -sampled dried VAMS and DBS is not a reliable tool for the monitoring of HbA1c .

Example answer:
{"entities": [{"text": "laboratory", "type": "Organization"}, {"text": "home", "type": "SpatialConcept"}, {"text": "dried VAMS", "type": "HealthCareActivity"}, {"text": "DBS", "type": "HealthCareActivity"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "HbA1c", "type": "Chemical"}]}

Input:
Sentence: Volumetric absorptive microsampling at home as an alternative tool for the monitoring of HbA1c in diabetes patients Microsampling techniques have several advantages over traditional blood collection .

## Item MedMentions:test:2074
Example input:
Sentence: Multivariate logistic regression models were used to estimate the association between job strain and T2DM .

Example answer:
{"entities": [{"text": "Multivariate logistic regression models", "type": "IntellectualProduct"}, {"text": "job strain", "type": "Finding"}, {"text": "T2DM", "type": "BiologicFunction"}]}

Example input:
Sentence: Strains of LC induced by IOP elevations ( on average 21 . 13 ± 7 . 61 mm Hg ) were 6 .

Example answer:
{"entities": [{"text": "Strains", "type": "AnatomicalStructure"}, {"text": "LC", "type": "AnatomicalStructure"}, {"text": "IOP", "type": "BiologicFunction"}, {"text": "elevations", "type": "SpatialConcept"}, {"text": "Hg", "type": "Chemical"}]}

Example input:
Sentence: In infants with bronchopulmonary dysplasia and / or pulmonary hypertension ( n = 119 [ 51 % ] ) , RV free wall longitudinal strain and IVS GLS were significantly lower ( P < .01 ) , LV GLS and GLSRs were similar ( P = .56 ) , and IVS segmental longitudinal strain persisted as an RV - dominant base - to - apex gradient from 32 weeks postmenstrual age to 1 year CA .

Example answer:
{"entities": [{"text": "bronchopulmonary dysplasia", "type": "BiologicFunction"}, {"text": "pulmonary hypertension", "type": "BiologicFunction"}, {"text": "RV free wall", "type": "AnatomicalStructure"}, {"text": "IVS", "type": "AnatomicalStructure"}, {"text": "LV", "type": "AnatomicalStructure"}, {"text": "segmental", "type": "SpatialConcept"}, {"text": "RV", "type": "AnatomicalStructure"}]}

Example input:
Sentence: This paper describes a new low back exposure assessment tool ( the Lifting Fatigue Failure Tool [ LiFFT ] ) , which estimates a " daily dose " of cumulative loading on the low back using fatigue failure principles .

Example answer:
{"entities": [{"text": "assessment tool", "type": "Chemical"}, {"text": "Lifting Fatigue Failure Tool", "type": "Chemical"}, {"text": "LiFFT", "type": "Chemical"}, {"text": "low back", "type": "AnatomicalStructure"}, {"text": "fatigue", "type": "Finding"}]}

Example input:
Sentence: To address these problems , we have developed a biomechanical modeling guided CBCT estimation technique ( Bio - CBCT - est ) by combining 2D - 3D deformation with finite element analysis ( FEA ) - based biomechanical modeling of anatomical structures .

Example answer:
{"entities": [{"text": "modeling", "type": "ResearchActivity"}, {"text": "CBCT", "type": "HealthCareActivity"}, {"text": "estimation technique", "type": "IntellectualProduct"}, {"text": "Bio - CBCT - est", "type": "IntellectualProduct"}, {"text": "2D", "type": "SpatialConcept"}, {"text": "3D", "type": "SpatialConcept"}, {"text": "finite element analysis", "type": "IntellectualProduct"}, {"text": "FEA", "type": "IntellectualProduct"}, {"text": "anatomical structures", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Strains of LC in adduction were on average higher than those in abduction , but the difference was not statistically significant ( P = 0 . 07 ) .

Example answer:
{"entities": [{"text": "Strains", "type": "AnatomicalStructure"}, {"text": "LC", "type": "AnatomicalStructure"}, {"text": "abduction", "type": "BiologicFunction"}]}

Example input:
Sentence: Knowledge of the three - dimensional stress and strain distribution within the SCB tissue helps to understand the mechanism of SCB failure , and may lead to an improved understanding of mechanisms of PTOA initiation , prevention and treatment .

Example answer:
{"entities": [{"text": "three - dimensional", "type": "SpatialConcept"}, {"text": "stress", "type": "Finding"}, {"text": "strain", "type": "Finding"}, {"text": "SCB tissue", "type": "AnatomicalStructure"}, {"text": "SCB", "type": "AnatomicalStructure"}, {"text": "improved", "type": "Finding"}, {"text": "PTOA", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study , we used high - resolution micro - computed tomography ( µCT ) - based finite element ( FE ) modelling of cartilage - bone to evaluate the failure mechanism and the locations of SCB tissue at high - risk of initial failure under compression .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "high - resolution micro - computed tomography", "type": "HealthCareActivity"}, {"text": "µCT", "type": "HealthCareActivity"}, {"text": "finite element ( FE ) modelling", "type": "IntellectualProduct"}, {"text": "cartilage - bone", "type": "AnatomicalStructure"}, {"text": "locations", "type": "SpatialConcept"}, {"text": "SCB tissue", "type": "AnatomicalStructure"}, {"text": "high - risk of", "type": "Finding"}]}

Example input:
Sentence: Development and validation of an easy - to - use risk assessment tool for cumulative low back loading : The Lifting Fatigue Failure Tool ( LiFFT ) Recent evidence suggests that musculoskeletal disorders ( MSDs ) may be the result of a fatigue failure process in affected tissues .

Example answer:
{"entities": [{"text": "validation", "type": "ResearchActivity"}, {"text": "risk assessment tool", "type": "HealthCareActivity"}, {"text": "low back", "type": "AnatomicalStructure"}, {"text": "Lifting Fatigue Failure Tool", "type": "Chemical"}, {"text": "LiFFT", "type": "Chemical"}, {"text": "musculoskeletal disorders", "type": "BiologicFunction"}, {"text": "MSDs", "type": "BiologicFunction"}, {"text": "fatigue", "type": "Finding"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The resulting FEA -corrected deformation fields are then fed back into 2D - 3D deformation to form an iterative loop , combining the benefits of intensity - based deformation and biomechanical modeling for CBCT estimation .

Example answer:
{"entities": [{"text": "FEA", "type": "IntellectualProduct"}, {"text": "2D", "type": "SpatialConcept"}, {"text": "3D", "type": "SpatialConcept"}, {"text": "loop", "type": "SpatialConcept"}, {"text": "modeling", "type": "ResearchActivity"}, {"text": "CBCT", "type": "HealthCareActivity"}, {"text": "estimation", "type": "IntellectualProduct"}]}

Input:
Sentence: Strains of LC for all loading scenarios were mapped using a three - dimensional tracking algorithm .

## Item MedMentions:test:2107
Example input:
Sentence: Multiple linear regression showed that genotypes and TC were independent factors affecting the levels of IL - 2 and IL - 10 ( P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "TC", "type": "Chemical"}, {"text": "levels of IL - 2", "type": "HealthCareActivity"}, {"text": "IL - 10", "type": "HealthCareActivity"}]}

Example input:
Sentence: No significant difference was found in the distribution of IFN - γ +2109 G / A genotypes between children with HLH and controls .

Example answer:
{"entities": [{"text": "No significant", "type": "Finding"}, {"text": "IFN - γ", "type": "AnatomicalStructure"}, {"text": "HLH", "type": "BiologicFunction"}]}

Example input:
Sentence: Our study provides evidence that IL - 4 polymorphisms associated with diminished serum IL - 4 levels may be partially responsible for AS development in the Chinese population .

Example answer:
{"entities": [{"text": "IL - 4", "type": "AnatomicalStructure"}, {"text": "serum", "type": "BodySubstance"}, {"text": "IL - 4", "type": "Chemical"}, {"text": "partially responsible", "type": "Finding"}, {"text": "AS", "type": "BiologicFunction"}, {"text": "Chinese population", "type": "PopulationGroup"}]}

Example input:
Sentence: All 19 X - chromosomal short tandem repeat ( STR ) loci in females were consistent with the Hardy - Weinberg equilibrium test .

Example answer:
{"entities": [{"text": "X - chromosomal", "type": "AnatomicalStructure"}, {"text": "short tandem repeat", "type": "SpatialConcept"}, {"text": "STR", "type": "SpatialConcept"}, {"text": "loci", "type": "AnatomicalStructure"}, {"text": "females", "type": "PopulationGroup"}]}

Example input:
Sentence: The frequencies of IFN - γ +874 T / A and T / T genotypes , as well as T allele , were significantly higher in the HLH group compared with those in the control group .

Example answer:
{"entities": [{"text": "IFN - γ", "type": "AnatomicalStructure"}, {"text": "T allele", "type": "AnatomicalStructure"}, {"text": "HLH", "type": "BiologicFunction"}]}

Example input:
Sentence: The genotype distribution of IL - 28B rs12979860CC , - CT , and - TT was 29 , 41 , and 30 % , respectively , and the distribution for rs8099917TT , - TG , and - GG was 63 , 31 , and 5 % , respectively .

Example answer:
{"entities": [{"text": "IL - 28B rs12979860CC", "type": "AnatomicalStructure"}, {"text": "CT", "type": "AnatomicalStructure"}, {"text": "TT", "type": "AnatomicalStructure"}, {"text": "rs8099917TT", "type": "AnatomicalStructure"}, {"text": "TG", "type": "AnatomicalStructure"}, {"text": "GG", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Similarly , patients carrying the rs2227282 CC genotype demonstrated higher serum IL - 4 levels than those with the GC and GG genotypes ( both P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "rs2227282", "type": "AnatomicalStructure"}, {"text": "serum", "type": "BodySubstance"}, {"text": "IL - 4", "type": "Chemical"}]}

Example input:
Sentence: In addition , serum IL - 4 concentrations were significantly lower in AS patients carrying the rs2243250 TT genotype compared to those with the CC and TC genotypes ( both P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "serum", "type": "BodySubstance"}, {"text": "IL - 4", "type": "Chemical"}, {"text": "AS", "type": "BiologicFunction"}, {"text": "rs2243250", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Genotypes in all the analyzed polymorphisms preserved the Hardy - Weinberg equilibrium in pregnant women , both infected and uninfected with HCMV ( P > 0 . 050 ) .

Example answer:
{"entities": [{"text": "analyzed polymorphisms", "type": "BiologicFunction"}, {"text": "pregnant women", "type": "PopulationGroup"}, {"text": "infected", "type": "Finding"}, {"text": "HCMV", "type": "Virus"}]}

Example input:
Sentence: Genotype frequencies were in Hardy - Weinberg equilibrium for all groups .

Example answer:
{"entities": []}

Input:
Sentence: IL - 4 rs2243250 and rs2227282 genotype frequencies in the latter were consistent with Hardy - Weinberg equilibrium ( both P > 0 . 05 ) .

## Item MedMentions:test:2268
Example input:
Sentence: Conventional PAT was significantly inferior in tracking these changes , with correlation coefficien t of -0 .

Example answer:
{"entities": [{"text": "tracking", "type": "SpatialConcept"}]}

Example input:
Sentence: There were no statistically significant differences .

Example answer:
{"entities": []}

Example input:
Sentence: There was no significant difference in the revision rate for other causes ( p = 0 . 2 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The mean difference was three days ( 95 % CI , 0 . 193 - 6 . 595 ; p = 0 . 039 ) .

Example answer:
{"entities": []}

Example input:
Sentence: There were significant differences between two groups ( P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: This study aimed to elucidate the effect of initiating PI - only ART on SAT function in ART - naive subjects .

Example answer:
{"entities": [{"text": "PI", "type": "Chemical"}, {"text": "ART", "type": "HealthCareActivity"}, {"text": "SAT", "type": "AnatomicalStructure"}, {"text": "naive", "type": "ClinicalAttribute"}]}

Example input:
Sentence: However , the difference was not statistically significant ( P = 0 . 149 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Overall , we found no significant difference with respect to venipuncture quality , as determined by our scale .

Example answer:
{"entities": [{"text": "venipuncture", "type": "HealthCareActivity"}, {"text": "scale", "type": "IntellectualProduct"}]}

Example input:
Sentence: The difference was not statistically significant ( p = 0 . 15 , 95 % CI for median difference -0 .

Example answer:
{"entities": []}

Example input:
Sentence: There were significant differences ( P < 0 . 001 ; < 0 . 001 ; < 0 . 001 ; < 0 . 001 ) .

Example answer:
{"entities": []}

Input:
Sentence: No differences were observed after the introduction of the PI .

## Item MedMentions:test:1928
Example input:
Sentence: Similarly , significant differences in OS were noted in advanced EOC at the following time points : 24 .

Example answer:
{"entities": [{"text": "EOC", "type": "BiologicFunction"}]}

Example input:
Sentence: Even among advanced HF p atient s with high BNP level , an ET program significantly improved exercise capacity , and a greater improvement in exercise capacity was associated with greater decreases in BNP level and V̇E / V̇CO2 slope and more favorable long - term clinical outcomes .

Example answer:
{"entities": [{"text": "HF", "type": "BiologicFunction"}, {"text": "BNP", "type": "Chemical"}, {"text": "improved", "type": "Finding"}, {"text": "decreases", "type": "Finding"}, {"text": "V̇CO2", "type": "Finding"}, {"text": "favorable long - term clinical outcomes", "type": "Finding"}]}

Example input:
Sentence: 9 months , P = 0 . 030 ) , whereas no significant correlation was detected for pts , where only metastatic tissue was available ( PFS : 5 . 8 vs 6 .

Example answer:
{"entities": [{"text": "metastatic tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Patients with localized disease showed a 3 - year event - free survival ( EFS ) of 68 % , compared to 3 - year EFS of 20 % in patients with metastases ( P = 0 . 042 ) .

Example answer:
{"entities": [{"text": "localized disease", "type": "BiologicFunction"}, {"text": "metastases", "type": "BiologicFunction"}]}

Example input:
Sentence: PFTs averaged over all patients and parameters demonstrated small absolute declines , 5 . 7 % averaged PFT decline , at approximately 1 year of follow - up , but only the diffusing capacity of lung for carbon monoxide ( DLCO ) demonstrated a statistically significant decline ( 10 . 29 vs .

Example answer:
{"entities": [{"text": "PFTs", "type": "HealthCareActivity"}, {"text": "PFT", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients ' weight , BMI and skinfold thickness decreased during the IMF period , and this decrease was statistically significant ( P < 0 . 01 ) .

Example answer:
{"entities": [{"text": "BMI", "type": "ClinicalAttribute"}, {"text": "skinfold thickness", "type": "HealthCareActivity"}, {"text": "IMF", "type": "HealthCareActivity"}]}

Example input:
Sentence: EFs were decreased in 48 % of patients ; however , there were thick and coiled EFs in all patients .

Example answer:
{"entities": [{"text": "EFs", "type": "AnatomicalStructure"}, {"text": "coiled", "type": "SpatialConcept"}]}

Example input:
Sentence: The multivariate Cox analysis showed significant body weight changes from the first to the sixth chemotherapy cycle for PFS ( HR = 0 .

Example answer:
{"entities": [{"text": "multivariate Cox analysis", "type": "IntellectualProduct"}, {"text": "body weight changes", "type": "Finding"}, {"text": "chemotherapy cycle", "type": "HealthCareActivity"}]}

Example input:
Sentence: Significant reduction in body weight in advanced EOC was observed with no changes in early EOC .

Example answer:
{"entities": [{"text": "reduction in body weight", "type": "Finding"}, {"text": "EOC", "type": "BiologicFunction"}]}

Example input:
Sentence: Body weight changes can be recognized as a prognostic factor for PFS and OS in advanced EOC patients undergoing chemotherapy .

Example answer:
{"entities": [{"text": "Body weight changes", "type": "Finding"}, {"text": "prognostic factor", "type": "ClinicalAttribute"}, {"text": "EOC", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Input:
Sentence: Significant differences in PFS were observed in advanced EOC patients that lost more than 5 % of their body weight ( 6 months ) , maintained weight ( 13 months ) , or gained more than 5 % of their body weight ( 15 months ) .

## Item MedMentions:test:1937
Example input:
Sentence: This work led to the discovery of 35 , a highly selective inhibitor of PI3K - delta which displays an excellent pharmacokinetic profile and is efficacious in a rodent model of rheumatoid arthritis .

Example answer:
{"entities": [{"text": "35", "type": "Chemical"}, {"text": "inhibitor", "type": "Chemical"}, {"text": "PI3K - delta", "type": "Chemical"}, {"text": "rodent model", "type": "BiologicFunction"}, {"text": "rheumatoid arthritis", "type": "BiologicFunction"}]}

Example input:
Sentence: A self - developed particle deposition model was adapted and validated to simulate the deposition of budesonide ( inhaled corticosteroid ; ICS ) and formoterol ( long acting β2 agonist ; LABA ) in the upper airways and lungs of the healthy volunteers .

Example answer:
{"entities": [{"text": "particle", "type": "Chemical"}, {"text": "model", "type": "IntellectualProduct"}, {"text": "simulate", "type": "ResearchActivity"}, {"text": "budesonide", "type": "Chemical"}, {"text": "inhaled corticosteroid", "type": "Chemical"}, {"text": "ICS", "type": "Chemical"}, {"text": "formoterol", "type": "Chemical"}, {"text": "long acting β2 agonist", "type": "Chemical"}, {"text": "LABA", "type": "Chemical"}, {"text": "upper airways", "type": "SpatialConcept"}, {"text": "lungs", "type": "AnatomicalStructure"}, {"text": "healthy volunteers", "type": "PopulationGroup"}]}

Example input:
Sentence: Our results demonstrated that the histogram method ( Mode , Skewness and Kurtosis ) was not superior to the conventional Mean value method in reproducibility evaluation on DCE - MRI pharmacokinetic parameters ( K ( trans ) & Ve ) in renal cell carcinoma , especially for Skewness and Kurtosis which showed lower intra - , inter - observer and scan - rescan reproducibility than Mean value .

Example answer:
{"entities": [{"text": "DCE - MRI", "type": "HealthCareActivity"}, {"text": "renal cell carcinoma", "type": "BiologicFunction"}]}

Example input:
Sentence: There were no risk of exposure exceeding the ARfD of methamidophos in the optimistic model and of chlorpyrifos ( 100 µg kg ( - ) ( 1 ) bw day ( - ) ( 1 ) ) in both optimistic and pessimistic models in all three populations .

Example answer:
{"entities": [{"text": "methamidophos", "type": "Chemical"}, {"text": "optimistic model", "type": "IntellectualProduct"}, {"text": "chlorpyrifos", "type": "Chemical"}, {"text": "optimistic", "type": "Finding"}, {"text": "pessimistic models", "type": "IntellectualProduct"}, {"text": "populations", "type": "PopulationGroup"}]}

Example input:
Sentence: Pharmacokinetic analyses of DCE - MRI data were performed using the Shutter - Speed model .

Example answer:
{"entities": [{"text": "Pharmacokinetic analyses", "type": "ResearchActivity"}, {"text": "DCE - MRI", "type": "HealthCareActivity"}, {"text": "Shutter - Speed model", "type": "IntellectualProduct"}]}

Example input:
Sentence: Phase I Dose - Escalation Study of Pilaralisib ( SAR245408 , XL147 ) in Combination with Paclitaxel and Carboplatin in Patients with Solid Tumors Despite involvement of PI3 K pathway activation in tumorigenesis of solid tumors , single - agent PI3 K inhibitors have shown modest clinical activity .

Example answer:
{"entities": [{"text": "Phase I", "type": "ResearchActivity"}, {"text": "Study", "type": "ResearchActivity"}, {"text": "Pilaralisib", "type": "Chemical"}, {"text": "SAR245408", "type": "Chemical"}, {"text": "XL147", "type": "Chemical"}, {"text": "Combination with Paclitaxel and Carboplatin", "type": "HealthCareActivity"}, {"text": "Solid Tumors", "type": "BiologicFunction"}, {"text": "tumorigenesis", "type": "BiologicFunction"}, {"text": "solid tumors", "type": "BiologicFunction"}, {"text": "PI3 K inhibitors", "type": "Chemical"}, {"text": "clinical activity", "type": "IntellectualProduct"}]}

Example input:
Sentence: A Markov model was developed to simulate the disease process of aGC ( PFS , progressive disease , and death ) and estimate the incremental cost - effectiveness ratio ( ICER ) of apatinib to placebo .

Example answer:
{"entities": [{"text": "simulate", "type": "ResearchActivity"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "aGC", "type": "BiologicFunction"}, {"text": "progressive disease", "type": "BiologicFunction"}, {"text": "death", "type": "BiologicFunction"}, {"text": "apatinib", "type": "Chemical"}, {"text": "placebo", "type": "HealthCareActivity"}]}

Example input:
Sentence: This phase I dose - escalation study evaluated the maximum tolerated dose ( MTD ) , safety , pharmacokinetics ( PK ) , and pharmacodynamics of pilaralisib in capsule and tablet formulations , administered in combination with paclitaxel and carboplatin in patients with advanced solid tumors .

Example answer:
{"entities": [{"text": "phase I", "type": "ResearchActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "safety", "type": "ResearchActivity"}, {"text": "pharmacokinetics", "type": "BiologicFunction"}, {"text": "PK", "type": "BiologicFunction"}, {"text": "pharmacodynamics", "type": "BiologicFunction"}, {"text": "pilaralisib", "type": "Chemical"}, {"text": "capsule", "type": "Chemical"}, {"text": "tablet", "type": "Chemical"}, {"text": "formulations", "type": "Chemical"}, {"text": "combination with paclitaxel and carboplatin", "type": "HealthCareActivity"}, {"text": "solid tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: The aim of this study was to predict pharmacokinetic and toxicity ( ADME / Tox ) properties of a coumarin isolated from geopropolis using in silico and in vitro approaches .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "ADME", "type": "ResearchActivity"}, {"text": "coumarin", "type": "Chemical"}, {"text": "geopropolis", "type": "Chemical"}]}

Example input:
Sentence: Prediction of pharmacokinetic and toxicological parameters of a 4 - phenylcoumarin isolated from geopropolis : In silico and in vitro approaches In silico and in vitro methodologies have been used as important tools in the drug discovery process , including from natural sources .

Example answer:
{"entities": [{"text": "4 - phenylcoumarin", "type": "Chemical"}, {"text": "geopropolis", "type": "Chemical"}, {"text": "drug discovery", "type": "ResearchActivity"}, {"text": "natural sources", "type": "Finding"}]}

Input:
Sentence: scutellaris geopropolis was evaluated for its pharmacokinetic parameters by in silico models ( ACD / Percepta ™ and MetaDrug ™ software ) .

## Item MedMentions:test:2206
Example input:
Sentence: An evaluation of the buffering of hydrophilic matrix tablets containing a pH - dependent solubility weak acid drug ( flurbiprofen ) , identified as possessing a deleterious effect on hydroxypropyl methylcellulose ( HPMC ) solubility , swelling and gelation , with respect to drug dissolution and the characteristics of the hydrophilic matrix gel layer in the presence of tromethamine as a buffer was undertaken .

Example answer:
{"entities": [{"text": "evaluation", "type": "HealthCareActivity"}, {"text": "buffering", "type": "Chemical"}, {"text": "matrix tablets", "type": "Chemical"}, {"text": "weak acid drug", "type": "Chemical"}, {"text": "flurbiprofen", "type": "Chemical"}, {"text": "hydroxypropyl methylcellulose", "type": "Chemical"}, {"text": "HPMC", "type": "Chemical"}, {"text": "matrix gel layer", "type": "Chemical"}, {"text": "tromethamine", "type": "Chemical"}, {"text": "buffer", "type": "Chemical"}]}

Example input:
Sentence: Long - range interactions between protein - coated particles and POEGMA brush layers in a serum environment Hydrophilic poly [ oligo ( ethylene glycol ) methyl methacrylate ] ( POEGMA ) brush layers with different thickness and graft densities were prepared by surface - initiated atom transfer radical polymerization ( SI - ATRP ) to construct a model surface to examine protein - surface interactions in a serum environment .

Example answer:
{"entities": [{"text": "protein", "type": "Chemical"}, {"text": "particles", "type": "Chemical"}, {"text": "POEGMA brush", "type": "Chemical"}, {"text": "serum environment", "type": "BodySubstance"}, {"text": "Hydrophilic poly [ oligo ( ethylene glycol ) methyl methacrylate ] ( POEGMA ) brush", "type": "Chemical"}, {"text": "prepared", "type": "Finding"}, {"text": "model", "type": "IntellectualProduct"}, {"text": "surface", "type": "SpatialConcept"}]}

Example input:
Sentence: These encouraging results support the use of 1 % phenytoin mucoadhesive paste as an adjunctive in periodontal treatment .

Example answer:
{"entities": [{"text": "phenytoin", "type": "Chemical"}, {"text": "adjunctive in periodontal treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Switching between pills of different appearances was associated with lower patient adherence to pharmacological treatment and a higher uncontrolled BP than no change in pharmacological treatment or change only in package but not in pill appearance .

Example answer:
{"entities": [{"text": "pills", "type": "Chemical"}, {"text": "pharmacological treatment", "type": "HealthCareActivity"}, {"text": "BP", "type": "BiologicFunction"}, {"text": "pill", "type": "Chemical"}]}

Example input:
Sentence: Controlled release patterns coupled with diffusion of drug were observed in two different buffers ( PBS ) at pH 7 .

Example answer:
{"entities": [{"text": "drug", "type": "Chemical"}, {"text": "buffers", "type": "Chemical"}, {"text": "PBS", "type": "Chemical"}]}

Example input:
Sentence: However , when thermolysis of persulfate occurred under circumneutral pH conditions in the presence of PAC , a new removal pathway for PFOA was observed .

Example answer:
{"entities": [{"text": "persulfate", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "PFOA", "type": "Chemical"}]}

Example input:
Sentence: It was observed that periodontal pocket depth was significantly more decreased in phenytoin side in comparison with placebo one ( p < 0 .

Example answer:
{"entities": [{"text": "periodontal pocket depth", "type": "Finding"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "side", "type": "SpatialConcept"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: Drug release profiles were unaffected by matrix pH - changes resulting from loss of tromethamine over time , suggesting that HPMC inhibited precipitation of drug from supersaturated solution in the hydrated matrix .

Example answer:
{"entities": [{"text": "pH - changes", "type": "Finding"}, {"text": "tromethamine", "type": "Chemical"}, {"text": "HPMC", "type": "Chemical"}, {"text": "drug", "type": "Chemical"}]}

Example input:
Sentence: Effect of 1 % Phenytoin Muco - Adhesive Paste on Improvement of Periodontal Status in Patients with Chronic Periodontitis : A Randomized Blinded Controlled Clinical Study Phenytoin ( PHT ) has been known to promote wound healing in some medical conditions owing to its proliferative as well as anti - inflammatory effects .

Example answer:
{"entities": [{"text": "Phenytoin", "type": "Chemical"}, {"text": "Periodontal Status", "type": "Finding"}, {"text": "Chronic Periodontitis", "type": "BiologicFunction"}, {"text": "Randomized Blinded Controlled Clinical Study", "type": "ResearchActivity"}, {"text": "PHT", "type": "Chemical"}, {"text": "wound healing", "type": "BiologicFunction"}, {"text": "medical conditions", "type": "BiologicFunction"}, {"text": "proliferative", "type": "BiologicFunction"}]}

Example input:
Sentence: However , in terms of complete elimination of microbiota , CH paste alone exhibited greater efficacy ( P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "CH paste", "type": "Chemical"}]}

Input:
Sentence: Then one surface received PHT paste whereas the other side had placebo as control .

## Item MedMentions:test:2247
Example input:
Sentence: HQ lengthened the QTc interval ( 409 ± 32 ms vs 433 ± 37 ms ; P = .027 ) and increased repolarization dispersion as evaluated by Tpe max in precordial leads ( 89 ± 15 ms vs 108 ± 27 ms ; P < .0001 ) with no significant changes in J - point elevation .

Example answer:
{"entities": [{"text": "HQ", "type": "Chemical"}, {"text": "repolarization", "type": "BiologicFunction"}, {"text": "dispersion", "type": "SpatialConcept"}, {"text": "Tpe max", "type": "Finding"}, {"text": "elevation", "type": "SpatialConcept"}]}

Example input:
Sentence: 0001 for all in both group s ) , higher HOMA - IR ( p < 0 . 0001 in both groups ) , and carotid IMT ( p = 0 .

Example answer:
{"entities": [{"text": "group", "type": "PopulationGroup"}, {"text": "HOMA - IR", "type": "HealthCareActivity"}, {"text": "groups", "type": "PopulationGroup"}, {"text": "carotid IMT", "type": "ClinicalAttribute"}]}

Example input:
Sentence: When increased liver enzymes were present , median ALT was significantly higher in PH cases ( 312 U / L , range 38 - 1 , 369 ) compared to RH cases ( 91 U / L , range 39 - 139 ) ( P < .001 ) .

Example answer:
{"entities": [{"text": "increased liver enzymes", "type": "Finding"}, {"text": "present", "type": "Finding"}, {"text": "ALT", "type": "Chemical"}, {"text": "PH", "type": "BiologicFunction"}]}

Example input:
Sentence: Between group comparison : The CD4 + percentage of group E was higher than that of group P ( P < 0 .

Example answer:
{"entities": [{"text": "CD4 + percentage", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , group A showed significant increases in DBP and MBP , and group C did not ( P = . 014 and .008 , respectively ) .

Example answer:
{"entities": [{"text": "DBP", "type": "ClinicalAttribute"}, {"text": "MBP", "type": "Finding"}]}

Example input:
Sentence: TP / ET increased after anthracyclines ( 1 . 26 ± 0 .

Example answer:
{"entities": [{"text": "ET", "type": "ClinicalAttribute"}, {"text": "anthracyclines", "type": "Chemical"}]}

Example input:
Sentence: In Kaplan - Meier analyses , the high AST / ALT group showed worse progression - free survival ( PFS ) , cancer - specific survival ( CSS ) , and overall survival ( all P < .001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Importantly , the change in IHRT was greater than placebo at mid for both absolute [ 4 . 4 % greater change , 90 % Confidence Interval ( CI ) 1 . 0 : 8 . 0 % , ES 0 . 21 , and relative strength ( 5 .

Example answer:
{"entities": [{"text": "IHRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Training improved both absolute ( IHRT : 13 . 1 ± 3 .

Example answer:
{"entities": [{"text": "Training", "type": "HealthCareActivity"}, {"text": "improved", "type": "Finding"}, {"text": "IHRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: There was also a greater change for IHRT at post for both absolute ( 7 . 0 % greater change , 90 % CI 1 .

Example answer:
{"entities": [{"text": "IHRT", "type": "HealthCareActivity"}]}

Input:
Sentence: Similarly , at post both groups increased absolute ( IHRT : 20 . 7 ± 7 .

## Item MedMentions:test:2221
Example input:
Sentence: Continuous support by professionals with a positive attitude was described as being of decisive importance for meaningful involvement .

Example answer:
{"entities": [{"text": "support", "type": "HealthCareActivity"}, {"text": "professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "positive attitude", "type": "BiologicFunction"}]}

Example input:
Sentence: Although psychosocial burden before and after stage II remains high , becoming a family is an essential experience for parents and confirms their parenthood .

Example answer:
{"entities": []}

Example input:
Sentence: Despite these challenges , some participants reported having primary intimate partners that supported their recovery through open communication .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: When children had a positive relationship with their parent , support of parents and teachers had little effect on working memory performance .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "support", "type": "HealthCareActivity"}, {"text": "teachers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "working memory", "type": "BiologicFunction"}, {"text": "performance", "type": "BiologicFunction"}]}

Example input:
Sentence: Friend support was perceived as most helpful when it derived from those in similar circumstances .

Example answer:
{"entities": [{"text": "Friend", "type": "PopulationGroup"}, {"text": "perceived", "type": "BiologicFunction"}]}

Example input:
Sentence: This relationship was partially mediated by emotional overeating .

Example answer:
{"entities": [{"text": "emotional overeating", "type": "BiologicFunction"}]}

Example input:
Sentence: Major findings indicated that negative peer norms , exposure to community violence , and poor mental health were negatively correlated with school bonding , while parental monitoring , positive self - regard , and future orientation were correlated with higher school motivation .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "negative peer norms", "type": "Finding"}, {"text": "mental health", "type": "BiologicFunction"}, {"text": "negatively", "type": "Finding"}, {"text": "school", "type": "Organization"}, {"text": "bonding", "type": "BiologicFunction"}, {"text": "orientation", "type": "BiologicFunction"}, {"text": "motivation", "type": "BiologicFunction"}]}

Example input:
Sentence: Relatives and care professionals emphasized the role the organization of facilitation of care played , as well as making residents feel like they still matter .

Example answer:
{"entities": [{"text": "care professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "organization", "type": "Organization"}]}

Example input:
Sentence: Family and friends served a wide range of functions but were equally available to resilient and non - resilient participants .

Example answer:
{"entities": [{"text": "friends", "type": "PopulationGroup"}, {"text": "resilient", "type": "PopulationGroup"}, {"text": "non - resilient participants", "type": "PopulationGroup"}]}

Example input:
Sentence: Becoming a family ' was the most important task as coping strategy to equilibrate the fragile emotional balance .

Example answer:
{"entities": [{"text": "coping strategy", "type": "HealthCareActivity"}, {"text": "fragile emotional balance", "type": "BiologicFunction"}]}

Input:
Sentence: Relationships such as peer , family and friends were the most important facilitators .

## Item MedMentions:test:2012
Example input:
Sentence: Our finding s suggest that GRL may be a novel potential therapeutic approach to protecting the thymic epithelium from conditioning - regimen - induced damage and promoting rapid and durable thymic and peripheral CD4 T cell recovery after HSCT .

Example answer:
{"entities": [{"text": "finding", "type": "Finding"}, {"text": "GRL", "type": "Chemical"}, {"text": "thymic", "type": "AnatomicalStructure"}, {"text": "epithelium", "type": "AnatomicalStructure"}, {"text": "conditioning - regimen", "type": "HealthCareActivity"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "CD4 T cell", "type": "AnatomicalStructure"}, {"text": "recovery", "type": "BiologicFunction"}, {"text": "HSCT", "type": "HealthCareActivity"}]}

Example input:
Sentence: All the GRL - treated mice , especially those administered GRL prior to the conditioning regimen , exhibited more intact thymic architecture and a more rapid restoration of CD4 T lymphocytes after BMT than those of the corresponding control mice .

Example answer:
{"entities": [{"text": "GRL", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "conditioning regimen", "type": "HealthCareActivity"}, {"text": "thymic", "type": "AnatomicalStructure"}, {"text": "restoration", "type": "HealthCareActivity"}, {"text": "CD4 T lymphocytes", "type": "AnatomicalStructure"}, {"text": "BMT", "type": "HealthCareActivity"}]}

Example input:
Sentence: With doped Gd species and strong tunable NIR absorbance , Gd : CuS @ BSA NPs demonstrate prominent tumor - contrasted imaging performance both on the photoacoustic and magnetic resonance imaging modalities .

Example answer:
{"entities": [{"text": "doped Gd species", "type": "Chemical"}, {"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "BSA", "type": "Chemical"}, {"text": "tumor - contrasted imaging", "type": "HealthCareActivity"}, {"text": "photoacoustic", "type": "HealthCareActivity"}, {"text": "magnetic resonance imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: Ghrelin Protects the Thymic Epithelium From Conditioning - Regimen - Induced Damage and Promotes the Restoration of CD4 + T Cells in Mice After Bone Marrow Transplantation The delay in immune reconstitution after hematopoietic stem cell transplantation ( HSCT ) , especially a delay in central immune reconstitution , leads to opportunistic infections and disease relapse after transplantation and affects the long - term outcome of HSCT .

Example answer:
{"entities": [{"text": "Ghrelin", "type": "Chemical"}, {"text": "Thymic Epithelium", "type": "AnatomicalStructure"}, {"text": "Conditioning - Regimen", "type": "HealthCareActivity"}, {"text": "Restoration", "type": "HealthCareActivity"}, {"text": "CD4 + T Cells", "type": "AnatomicalStructure"}, {"text": "Mice", "type": "Eukaryote"}, {"text": "Bone Marrow Transplantation", "type": "HealthCareActivity"}, {"text": "immune reconstitution", "type": "Finding"}, {"text": "hematopoietic stem cell transplantation", "type": "HealthCareActivity"}, {"text": "HSCT", "type": "HealthCareActivity"}, {"text": "immune reconstitution", "type": "BiologicFunction"}, {"text": "opportunistic infections", "type": "BiologicFunction"}, {"text": "disease relapse", "type": "BiologicFunction"}, {"text": "transplantation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Albumin -Bioinspired Gd : CuS Nanotheranostic Agent for In Vivo Photoacoustic / Magnetic Resonance Imaging -Guided Tumor -Targeted Photothermal Therapy Photothermal therapy ( PTT ) is attracting increasing interest and becoming more widely used for skin cancer therapy in the clinic , as a result of its noninvasiveness and low systemic adverse effects .

Example answer:
{"entities": [{"text": "Albumin", "type": "Chemical"}, {"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "In Vivo", "type": "SpatialConcept"}, {"text": "Photoacoustic / Magnetic Resonance Imaging -Guided Tumor -Targeted Photothermal Therapy", "type": "HealthCareActivity"}, {"text": "Photothermal therapy", "type": "HealthCareActivity"}, {"text": "PTT", "type": "HealthCareActivity"}, {"text": "skin cancer therapy", "type": "HealthCareActivity"}, {"text": "clinic", "type": "Organization"}, {"text": "low systemic adverse effects", "type": "BiologicFunction"}]}

Example input:
Sentence: This study highlights the practicality and versatility of albumin -mediated biomimetic mineralization of a nanotheranostic agent and also suggests that bioinspired Gd : CuS @ BSA NPs possess promising imaging guidance and effective tumor ablation properties , with high spatial resolution and deep tissue penetration .

Example answer:
{"entities": [{"text": "albumin", "type": "Chemical"}, {"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "BSA", "type": "Chemical"}, {"text": "imaging guidance", "type": "HealthCareActivity"}, {"text": "tumor ablation properties", "type": "HealthCareActivity"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: There was no significant difference in the CHS response between mice that received Treg cells from UVB - irradiated XPA - deficient donors fed GSPs or the control diet .

Example answer:
{"entities": [{"text": "CHS", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "Treg cells", "type": "AnatomicalStructure"}, {"text": "XPA", "type": "AnatomicalStructure"}, {"text": "deficient", "type": "BiologicFunction"}, {"text": "donors", "type": "PopulationGroup"}, {"text": "control diet", "type": "Finding"}]}

Example input:
Sentence: Herein , a biocompatible Gd -integrated CuS nanotheranostic agent ( Gd : CuS @ BSA ) was synthesized via a facile and environmentally friendly biomimetic strategy , using bovine serum albumin ( BSA ) as a biotemplate at physiological temperature .

Example answer:
{"entities": [{"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "BSA", "type": "Chemical"}, {"text": "bovine serum albumin", "type": "Chemical"}]}

Example input:
Sentence: Adoptive transfer experiments revealed that naïve recipients that received Treg cells from GSPs - fed UVB - irradiated wild - type donors that had been sensitized to DNFB exhibited a significantly higher contact hypersensitivity ( CHS ) response to DNFB than mice that received Treg cells from UVB - exposed mice fed the control diet .

Example answer:
{"entities": [{"text": "Adoptive transfer experiments", "type": "HealthCareActivity"}, {"text": "recipients", "type": "PopulationGroup"}, {"text": "Treg cells", "type": "AnatomicalStructure"}, {"text": "wild - type", "type": "AnatomicalStructure"}, {"text": "donors", "type": "PopulationGroup"}, {"text": "DNFB", "type": "Chemical"}, {"text": "contact hypersensitivity", "type": "BiologicFunction"}, {"text": "CHS", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "control diet", "type": "Finding"}]}

Example input:
Sentence: In addition , toxicity studies in vitro and in vivo verify that Gd : CuS @ BSA NPs qualify as biocompatible agents .

Example answer:
{"entities": [{"text": "toxicity studies", "type": "HealthCareActivity"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "BSA", "type": "Chemical"}]}

Input:
Sentence: The immune response triggered by Gd : CuS @ BSA -mediated PTT is preliminarily explored .

## Item MedMentions:test:2156
Example input:
Sentence: Country - specific chemical signatures of persistent organic pollutants ( POPs ) in breast milk of French , Danish and Finnish women The present study compares concentrations and chemical profiles of an extended range of persistent organic pollutants ( dioxins , polychlorobiphenyls , brominated flame retardants and organochlorine pesticides ) in breast milk samples from French ( n = 96 ) , Danish ( n = 438 ) and Finnish ( n = 22 ) women .

Example answer:
{"entities": [{"text": "Country", "type": "SpatialConcept"}, {"text": "organic pollutants", "type": "Chemical"}, {"text": "POPs", "type": "Chemical"}, {"text": "breast milk", "type": "BodySubstance"}, {"text": "French", "type": "PopulationGroup"}, {"text": "Danish", "type": "PopulationGroup"}, {"text": "Finnish", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "study", "type": "ResearchActivity"}, {"text": "dioxins", "type": "Chemical"}, {"text": "polychlorobiphenyls", "type": "Chemical"}, {"text": "brominated flame retardants", "type": "Chemical"}, {"text": "organochlorine pesticides", "type": "Chemical"}, {"text": "breast milk samples", "type": "BodySubstance"}]}

Example input:
Sentence: Critical assessment of pendimethalin in terms of persistence , bioaccumulation , toxicity , and potential for long - range transport Pendimethalin ( PND , CAS registry number 40487 - 42 - 1 ) is a dinitroaniline herbicide that selectively controls broad - leaf and grassy weeds in a variety of crops and in noncrop areas .

Example answer:
{"entities": [{"text": "pendimethalin", "type": "Chemical"}, {"text": "bioaccumulation", "type": "BiologicFunction"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "Pendimethalin", "type": "Chemical"}, {"text": "PND", "type": "Chemical"}, {"text": "CAS registry number", "type": "IntellectualProduct"}, {"text": "dinitroaniline", "type": "Chemical"}, {"text": "herbicide", "type": "Chemical"}, {"text": "weeds", "type": "Eukaryote"}, {"text": "crops", "type": "Eukaryote"}, {"text": "noncrop areas", "type": "SpatialConcept"}]}

Example input:
Sentence: Analysis of the 260 patients with noninvasive IPMNs showed that family history of pancreatic cancer ( P = 0 . 027 ) and high - grade dysplasia ( HGD ) ( P = 0 . 003 ) were independent risk factors for the development of an IPMN with HGD or an invasive carcinoma in the remnant pancreas .

Example answer:
{"entities": [{"text": "Analysis", "type": "ResearchActivity"}, {"text": "noninvasive IPMNs", "type": "BiologicFunction"}, {"text": "family history", "type": "Finding"}, {"text": "pancreatic cancer", "type": "BiologicFunction"}, {"text": "high - grade dysplasia", "type": "BiologicFunction"}, {"text": "HGD", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "IPMN", "type": "BiologicFunction"}, {"text": "invasive carcinoma", "type": "BiologicFunction"}, {"text": "remnant", "type": "AnatomicalStructure"}, {"text": "pancreas", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Methods : A single - center , retrospective cohort study to determine incidence and diagnostic accuracy for Type 2 DN as the primary cause of ESRD ( Code 250 . 40 ) on the Center for Medicare & Medicaid ( CMS ) Medical Evidence Report form ( CMS2728 ) submitted at renal replacement therapy initiation .

Example answer:
{"entities": [{"text": "center", "type": "Organization"}, {"text": "retrospective cohort study", "type": "ResearchActivity"}, {"text": "Type 2", "type": "IntellectualProduct"}, {"text": "DN", "type": "BiologicFunction"}, {"text": "ESRD", "type": "BiologicFunction"}, {"text": "Center for Medicare & Medicaid", "type": "Organization"}, {"text": "CMS", "type": "Organization"}, {"text": "Medical Evidence Report form", "type": "IntellectualProduct"}, {"text": "CMS2728", "type": "IntellectualProduct"}, {"text": "renal replacement therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Because of its volatility , PND may be transported over short distances in air and was found in samples in local and semiremote regions ; however , these concentrations are not of toxicological concern .

Example answer:
{"entities": [{"text": "PND", "type": "Chemical"}, {"text": "local", "type": "SpatialConcept"}, {"text": "semiremote regions", "type": "SpatialConcept"}]}

Example input:
Sentence: Unlike other current - use pesticides , PND has not been found in samples from remote regions since 2000 and there is no apparent evidence that this herbicide accumulates in food chains in the Arctic .

Example answer:
{"entities": [{"text": "pesticides", "type": "Chemical"}, {"text": "PND", "type": "Chemical"}, {"text": "remote regions", "type": "SpatialConcept"}, {"text": "herbicide", "type": "Chemical"}, {"text": "Arctic", "type": "SpatialConcept"}]}

Example input:
Sentence: Animal permanent environment also affected PBTTC ( 0 . 14±0 . 07 ) .

Example answer:
{"entities": [{"text": "Animal permanent environment", "type": "SpatialConcept"}, {"text": "PBTTC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: ( i . e . , current reduction ) may allow the elimination of the reversible malfunctioning short term effects ( HPNS ) , or even deleterious long term effects induced by increased NMDAR function during HP exposure .

Example answer:
{"entities": [{"text": "HPNS", "type": "BiologicFunction"}, {"text": "NMDAR", "type": "Chemical"}]}

Example input:
Sentence: In air , the DT50 of PND was estimated to be 0 . 35 d , which is well below the criterion of 2 d for LRT under the United Nations Economic Commission for Europe ( UNECE ) Aarhus protocol .

Example answer:
{"entities": [{"text": "PND", "type": "Chemical"}, {"text": "United Nations Economic Commission for Europe", "type": "Organization"}, {"text": "UNECE", "type": "Organization"}, {"text": "Aarhus protocol", "type": "IntellectualProduct"}]}

Example input:
Sentence: 37 to 11 . 58 ) ; p < 0 . 0001 ) than those persistent .

Example answer:
{"entities": []}

Input:
Sentence: From these data PND is not persistent as defined in the Annex II of EC regulation 1107 / 2009 .

## Item MedMentions:test:2100
Example input:
Sentence: Its presence suggests a common and widespread strategy of modulation of host transcriptional machinery upon infection via this transcriptional switch .

Example answer:
{"entities": [{"text": "widespread", "type": "SpatialConcept"}, {"text": "modulation of host", "type": "BiologicFunction"}, {"text": "transcriptional machinery", "type": "BiologicFunction"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "transcriptional", "type": "BiologicFunction"}]}

Example input:
Sentence: Our studies reveal a new paradigm of host - pathogen interactions , in which pathogens exploit conserved host post - translational modifications , thereby achieving highly specific receptor binding while also tolerating genetic changes across multiple isoforms of receptors .

Example answer:
{"entities": [{"text": "host - pathogen interactions", "type": "BiologicFunction"}, {"text": "post - translational modifications", "type": "BiologicFunction"}, {"text": "receptor binding", "type": "BiologicFunction"}, {"text": "genetic changes", "type": "BiologicFunction"}, {"text": "isoforms", "type": "Chemical"}, {"text": "receptors", "type": "Chemical"}]}

Example input:
Sentence: Temporal upregulation of host surface receptors provides a window of opportunity for bacterial adhesion and disease Host surface receptors provide bacteria with a foothold from which to attach , colonize and , in some cases , invade tissue and elicit human disease .

Example answer:
{"entities": [{"text": "upregulation", "type": "BiologicFunction"}, {"text": "host surface receptors", "type": "Chemical"}, {"text": "bacterial adhesion", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "Host surface receptors", "type": "Chemical"}, {"text": "bacteria", "type": "Bacterium"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}]}

Example input:
Sentence: All forms of life , from bacteria to humans , are postulated to rely on a fundamental host defense mechanism , which exploits the formation of open pores in microbial phospholipid bilayers .

Example answer:
{"entities": [{"text": "bacteria", "type": "Bacterium"}, {"text": "humans", "type": "Eukaryote"}, {"text": "host defense mechanism", "type": "BiologicFunction"}, {"text": "open", "type": "SpatialConcept"}, {"text": "pores", "type": "AnatomicalStructure"}, {"text": "phospholipid bilayers", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The virulence of these strains was determined by biofilm formation , serum killing resistance , phagocytosis , and infection models .

Example answer:
{"entities": [{"text": "virulence", "type": "BiologicFunction"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "serum", "type": "BodySubstance"}, {"text": "killing", "type": "BiologicFunction"}, {"text": "phagocytosis", "type": "BiologicFunction"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "models", "type": "IntellectualProduct"}]}

Example input:
Sentence: HGT plays a major role in bacterial evolution , and past research has demonstrated that HGT , including natural competence for transformation , contributes to the emergence of pathogens and the spread of virulence factors .

Example answer:
{"entities": [{"text": "HGT", "type": "BiologicFunction"}, {"text": "evolution", "type": "BiologicFunction"}, {"text": "research", "type": "ResearchActivity"}, {"text": "transformation", "type": "BiologicFunction"}, {"text": "virulence factors", "type": "Chemical"}]}

Example input:
Sentence: The bacterium expresses four major proteases emerging as virulence factors ; aureolysin ( Aur ) , V8 protease ( SspA ) , staphopain A ( ScpA ) , and staphopain B ( SspB ) .

Example answer:
{"entities": [{"text": "bacterium", "type": "Bacterium"}, {"text": "expresses", "type": "BiologicFunction"}, {"text": "proteases", "type": "Chemical"}, {"text": "virulence factors", "type": "Chemical"}, {"text": "aureolysin", "type": "Chemical"}, {"text": "Aur", "type": "Chemical"}, {"text": "V8 protease", "type": "Chemical"}, {"text": "SspA", "type": "Chemical"}, {"text": "staphopain A", "type": "Chemical"}, {"text": "ScpA", "type": "Chemical"}, {"text": "staphopain B", "type": "Chemical"}, {"text": "SspB", "type": "Chemical"}]}

Example input:
Sentence: Deregulation of many signaling pathways involved in growth , survival , migration and resistance to treatment has been implicated in pathogenesis of GBM .

Example answer:
{"entities": [{"text": "signaling pathways", "type": "BiologicFunction"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "migration", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "GBM", "type": "BiologicFunction"}]}

Example input:
Sentence: Uncontrolled inflammatory pathways , pathogenic bacterial burden and impaired antiviral immunity are thought to be important factors in disease severity and duration .

Example answer:
{"entities": [{"text": "inflammatory pathways", "type": "BiologicFunction"}, {"text": "antiviral immunity", "type": "BiologicFunction"}]}

Example input:
Sentence: This effect may be associated with its capacity to inhibit the TLR4 / NF - κB signaling pathways .

Example answer:
{"entities": [{"text": "inhibit", "type": "BiologicFunction"}, {"text": "TLR4", "type": "Chemical"}, {"text": "NF - κB signaling pathways", "type": "BiologicFunction"}]}

Input:
Sentence: However , the implications of bacterial virulence or replicative capacity and the signaling pathways remained unknown .

## Item MedMentions:test:2193
Example input:
Sentence: In this study , data supporting the in vitro and in vivo anticancer effects of delicaflavone , a rarely occurring biflavonoid from Selaginella doederleinii , were reported .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "anticancer effects", "type": "Finding"}, {"text": "delicaflavone", "type": "Chemical"}, {"text": "biflavonoid", "type": "Chemical"}, {"text": "Selaginella doederleinii", "type": "Eukaryote"}]}

Example input:
Sentence: Delicaflavone induced autophagic cell death via Akt / mTOR / p70S6 K signaling pathway .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "autophagic cell death", "type": "BiologicFunction"}, {"text": "Akt", "type": "BiologicFunction"}, {"text": "mTOR", "type": "BiologicFunction"}, {"text": "p70S6 K", "type": "Chemical"}, {"text": "signaling pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Delicaflavone induced autophagic cell death via Akt / mTOR / p70S6 K signaling pathway .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "autophagic cell death", "type": "BiologicFunction"}, {"text": "Akt", "type": "BiologicFunction"}, {"text": "mTOR", "type": "BiologicFunction"}, {"text": "p70S6 K", "type": "Chemical"}, {"text": "signaling pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Delicaflavone induces autophagic cell death in lung cancer via Akt / mTOR / p70S6 K signaling pathway Searching for potential anticancer agents from natural sources is an effective strategy for developing novel chemotherapeutic agents .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "autophagic cell death", "type": "BiologicFunction"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "Akt", "type": "BiologicFunction"}, {"text": "mTOR", "type": "BiologicFunction"}, {"text": "p70S6 K", "type": "Chemical"}, {"text": "signaling pathway", "type": "BiologicFunction"}, {"text": "anticancer agents", "type": "Chemical"}, {"text": "natural sources", "type": "Finding"}, {"text": "chemotherapeutic agents", "type": "Chemical"}]}

Example input:
Sentence: Delicaflavone may represent a potential therapeutic agent for lung cancer .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "lung cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Delicaflavone may represent a potential therapeutic agent for lung cancer .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "lung cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Delicaflavone downregulated the expression of phospho - Akt , phospho - mTOR , and phospho - p70S6 K in a time - and dose - dependent manner , suggesting that it induced autophagy by inhibiting the Akt / mTOR / p70S6 K pathway in A549 and PC - 9 cells .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "downregulated", "type": "BiologicFunction"}, {"text": "expression of phospho - Akt", "type": "Finding"}, {"text": "phospho - mTOR", "type": "Chemical"}, {"text": "phospho - p70S6 K", "type": "Chemical"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "Akt", "type": "BiologicFunction"}, {"text": "mTOR", "type": "BiologicFunction"}, {"text": "p70S6 K", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "A549", "type": "AnatomicalStructure"}, {"text": "PC - 9 cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Delicaflavone showed anti - lung cancer effects in vitro and in vivo .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "anti - lung cancer effects", "type": "Finding"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: Delicaflavone is a potential anticancer agent that can induce autophagic cell death in human non - small cell lung cancer via the Akt / mTOR / p70S6 K signaling pathway .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "anticancer agent", "type": "Chemical"}, {"text": "autophagic cell death", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "non - small cell lung cancer", "type": "BiologicFunction"}, {"text": "Akt", "type": "BiologicFunction"}, {"text": "mTOR", "type": "BiologicFunction"}, {"text": "p70S6 K", "type": "Chemical"}, {"text": "signaling pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Delicaflavone exhibited favorable anticancer properties , as shown by the MTT assay and xenograft model of human non - small cell lung cancer in male BALB / c nude mice without observable adverse effect .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "anticancer", "type": "Finding"}, {"text": "MTT assay", "type": "ResearchActivity"}, {"text": "xenograft model", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "non - small cell lung cancer", "type": "BiologicFunction"}, {"text": "BALB / c nude mice", "type": "Eukaryote"}, {"text": "adverse effect", "type": "BiologicFunction"}]}

Input:
Sentence: Delicaflavone did not show observable side effects in a xenograft mouse model .

## Item MedMentions:test:2315
Example input:
Sentence: In other words , they spontaneously inferred the presence of social norms even when an adult had done nothing to indicate such a norm in either language or behavior . And children of this age even went so far as to enforce these self - inferred norms when third parties " broke " them .

Example answer:
{"entities": [{"text": "inferred", "type": "BiologicFunction"}, {"text": "self - inferred", "type": "BiologicFunction"}]}

Example input:
Sentence: We found that higher levels of spontaneous activity were associated with both higher levels of activation relative to suppression across a variety of wide - band stimuli and higher driven rates in response to WGN .

Example answer:
{"entities": [{"text": "spontaneous activity", "type": "BiologicFunction"}, {"text": "WGN", "type": "IntellectualProduct"}]}

Example input:
Sentence: Faking behavior also introduced a uniform bias , implying that the classically observed mean raw score differences may not be readily interpreted .

Example answer:
{"entities": []}

Example input:
Sentence: Crude logistic regression showed that women ( odds ratio [ OR ] 1 . 9 , 95 % confidence interval [ CI ] 1 . 3 - 2 . 6 ) , low educational level ( OR 2 . 0 , 95 % CI 1 . 4 - 3 . 0 ) and low mastery ( OR 1 . 4 , 95 % CI 1 . 0 - 1 . 9 ) were associated with cognitive decline , but no daily consumption of vegetables and fruits had only a marginal association ( OR 1 .

Example answer:
{"entities": [{"text": "logistic regression", "type": "ResearchActivity"}, {"text": "low mastery", "type": "Finding"}, {"text": "cognitive decline", "type": "BiologicFunction"}, {"text": "no", "type": "Finding"}, {"text": "vegetables", "type": "Food"}, {"text": "fruits", "type": "Food"}]}

Example input:
Sentence: Various types of regression were obtained in 27 ( 69 . 2 % ) eyes .

Example answer:
{"entities": [{"text": "regression", "type": "BiologicFunction"}, {"text": "eyes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: All regression coefficients were negative , implying that the more the surrogate overestimated quality of life compared to the older adult , the more he or she overestimated the older adult ' s desire to be treated .

Example answer:
{"entities": [{"text": "negative", "type": "Finding"}, {"text": "older adult", "type": "PopulationGroup"}]}

Example input:
Sentence: Overall satisfaction did not change statistically between the iterations but the qualitative analysis revealed greater trust in the second prototype .

Example answer:
{"entities": [{"text": "satisfaction", "type": "BiologicFunction"}, {"text": "iterations", "type": "Finding"}, {"text": "qualitative analysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: These broad - based declines in failure rates reverse a long - term pattern of minimal change .

Example answer:
{"entities": []}

Example input:
Sentence: Half a year later , they retook the same personality scales in 1 of 3 randomly assigned experimental response conditions : honest , faking - good , or reproduce .

Example answer:
{"entities": [{"text": "personality scales", "type": "IntellectualProduct"}, {"text": "response conditions", "type": "BiologicFunction"}]}

Example input:
Sentence: To our knowledge , this is the first report of spontaneous regression of meningioma in a patient receiving interferon beta - 1a therapy and just the second report of spontaneous regression in general .

Example answer:
{"entities": [{"text": "report", "type": "HealthCareActivity"}, {"text": "spontaneous regression", "type": "BiologicFunction"}, {"text": "meningioma", "type": "BiologicFunction"}, {"text": "interferon beta - 1a", "type": "Chemical"}, {"text": "therapy", "type": "HealthCareActivity"}]}

Input:
Sentence: However , spontaneous regression is very rarely observed .

## Item MedMentions:test:2200
Example input:
Sentence: OS was estimated by the Kaplan - Meier method , and multivariate analysis was performed by Cox proportional hazards regression modeling .

Example answer:
{"entities": [{"text": "Kaplan - Meier method", "type": "ResearchActivity"}, {"text": "Cox proportional hazards regression modeling", "type": "IntellectualProduct"}]}

Example input:
Sentence: In contrast , in the multivariate analysis , it was significantly associated with primary tumor location , central lymph node metastasis ( p < 0 .

Example answer:
{"entities": [{"text": "tumor", "type": "BiologicFunction"}, {"text": "location", "type": "SpatialConcept"}, {"text": "central lymph node metastasis", "type": "BiologicFunction"}]}

Example input:
Sentence: Multivariate analysis revealed that venous invasion ( hazard ratio , 9 . 22 ; 95 % confidence interval , 3 . 90 - 23 . 66 ; P < 0 . 001 ) and KIF18A expression ( hazard ratio , 3 . 20 ; 95 % confidence interval , 1 . 34 - 6 . 09 ; P = 0 . 010 ) were independent predictive factors for lymph node metastasis .

Example answer:
{"entities": [{"text": "venous invasion", "type": "Finding"}, {"text": "KIF18A", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "predictive factors", "type": "IntellectualProduct"}, {"text": "lymph node metastasis", "type": "BiologicFunction"}]}

Example input:
Sentence: The predictors of OS were analyzed using Cox regression analysis .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "Cox regression analysis", "type": "IntellectualProduct"}]}

Example input:
Sentence: Overall survival ( OS ) , locoregional control ( LRC ) , and freedom from distant metastasis ( FFDM ) were calculated using log - rank and Cox regression analysis .

Example answer:
{"entities": [{"text": "locoregional", "type": "BiologicFunction"}, {"text": "freedom from distant metastasis", "type": "BiologicFunction"}, {"text": "FFDM", "type": "BiologicFunction"}, {"text": "log - rank", "type": "IntellectualProduct"}, {"text": "Cox regression analysis", "type": "IntellectualProduct"}]}

Example input:
Sentence: In the univariate analysis , it was significantly associated with age , tumor size , tumor spread , extrathyroidal extension , primary tumor location and central lymph node metastasis ( p < 0 .

Example answer:
{"entities": [{"text": "tumor size", "type": "SpatialConcept"}, {"text": "tumor spread", "type": "Finding"}, {"text": "extrathyroidal extension", "type": "BiologicFunction"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "location", "type": "SpatialConcept"}, {"text": "central lymph node metastasis", "type": "BiologicFunction"}]}

Example input:
Sentence: Univariable and multivariable Cox regression analyses identified predictors of OS .

Example answer:
{"entities": [{"text": "Univariable and multivariable Cox regression analyses", "type": "IntellectualProduct"}]}

Example input:
Sentence: The predictors of shorter OS were a higher Memorial Sloan Kettering Cancer Center score ; liver , lung , and brain metastases ; and multiple sites of BMs ( hazard ratio , 1 . 38 ; 95 % CI , 1 . 02 - 1 . 91 ; P = .04 ) .

Example answer:
{"entities": [{"text": "liver", "type": "BiologicFunction"}, {"text": "lung", "type": "BiologicFunction"}, {"text": "brain metastases", "type": "BiologicFunction"}, {"text": "multiple sites", "type": "SpatialConcept"}, {"text": "BMs", "type": "BiologicFunction"}]}

Example input:
Sentence: Multivariate Cox model was performed to identify the impact of molecular subtype and other prognostic factors on OS .

Example answer:
{"entities": [{"text": "subtype", "type": "IntellectualProduct"}, {"text": "prognostic factors", "type": "ClinicalAttribute"}]}

Example input:
Sentence: BMI was also an independent prognostic factor for OS in multivariate analysis ( HR 0 . 541 ; 95 % CI 0 .

Example answer:
{"entities": [{"text": "BMI", "type": "ClinicalAttribute"}, {"text": "prognostic factor", "type": "ClinicalAttribute"}]}

Input:
Sentence: In the multivariate analysis , the independent predictors of OS were a CY + status , lymph node metastasis , and adjuvant chemotherapy .

## Item MedMentions:test:1895
Example input:
Sentence: However , randomized clinical trials with long - term follow - up periods are needed to confirm their efficacy in reducing the prevalence / incidence of oral infectious diseases .

Example answer:
{"entities": [{"text": "randomized clinical trials", "type": "ResearchActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "oral infectious diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Early readings of antibiotic susceptibility test ( AST ) results could be of critical importance to ensure adequate treatment .

Example answer:
{"entities": [{"text": "antibiotic susceptibility test", "type": "HealthCareActivity"}, {"text": "AST", "type": "HealthCareActivity"}, {"text": "results", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The most common indications for antimicrobial use were antimicrobial prophylaxis ( 28 .

Example answer:
{"entities": [{"text": "antimicrobial", "type": "Chemical"}, {"text": "prophylaxis", "type": "HealthCareActivity"}]}

Example input:
Sentence: Both of these factors are key to monitoring development and spread of antimalarial drug resistance .

Example answer:
{"entities": [{"text": "monitoring", "type": "HealthCareActivity"}, {"text": "antimalarial drug resistance", "type": "BiologicFunction"}]}

Example input:
Sentence: Fully automated disc diffusion for rapid antibiotic susceptibility test results : a proof - of - principle study Antibiotic resistance poses a significant threat to patients suffering from infectious diseases .

Example answer:
{"entities": [{"text": "disc diffusion", "type": "HealthCareActivity"}, {"text": "antibiotic susceptibility test", "type": "HealthCareActivity"}, {"text": "results", "type": "Finding"}, {"text": "suffering", "type": "Finding"}, {"text": "infectious diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Accurate diagnosis may prevent unnecessary antibiotic use .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "antibiotic", "type": "Chemical"}]}

Example input:
Sentence: Inappropriately used antibiotic s should be subject to rigorous control and management , and public policy initiatives are required to promote the judicious use of antibiotic s .

Example answer:
{"entities": [{"text": "antibiotic", "type": "Chemical"}]}

Example input:
Sentence: This may prove to be a useful tool for multidrug - resistant staphylococci monitoring in clinical laboratories , particularly in the wake of increased chlorhexidine and mupirocin treatments .

Example answer:
{"entities": [{"text": "staphylococci", "type": "Bacterium"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "clinical laboratories", "type": "Organization"}, {"text": "chlorhexidine", "type": "Chemical"}, {"text": "mupirocin", "type": "Chemical"}, {"text": "treatments", "type": "HealthCareActivity"}]}

Example input:
Sentence: Thus , a simple , rapid , and reliable approach will be paramount in monitoring the resistance prevalence to these agents .

Example answer:
{"entities": [{"text": "monitoring", "type": "HealthCareActivity"}, {"text": "agents", "type": "Chemical"}]}

Example input:
Sentence: The dramatically reduced discovery of new antibiotics , as well as the persistent emergence of resistant bacteria , represents a major health problem in both hospital and community settings .

Example answer:
{"entities": [{"text": "antibiotics", "type": "Chemical"}, {"text": "resistant bacteria", "type": "Bacterium"}, {"text": "problem", "type": "Finding"}, {"text": "hospital", "type": "Organization"}, {"text": "community settings", "type": "Organization"}]}

Input:
Sentence: Regular monitoring , judicious prescription , and early detection of resistance to these antibiotics are , therefore , necessary to check further dissemination of the organism .

## Item MedMentions:test:1990
Example input:
Sentence: Use of single molecule sequencing for comparative genomics of an environmental and a clinical isolate of Clostridium difficile ribotype 078 How the pathogen Clostridium difficile might survive , evolve and be transferred between reservoirs within the natural environment is poorly understood .

Example answer:
{"entities": [{"text": "genomics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "environmental", "type": "SpatialConcept"}, {"text": "isolate", "type": "Chemical"}, {"text": "Clostridium difficile", "type": "Bacterium"}, {"text": "ribotype 078", "type": "Finding"}, {"text": "reservoirs", "type": "SpatialConcept"}, {"text": "natural environment", "type": "SpatialConcept"}]}

Example input:
Sentence: coli K - 12 , a classical non - environmental strain , constitutes a model of phenotypic plasticity for adaptation to a redox - cycling herbicide through redundancy of different isoforms of SOD and CAT enzymes .

Example answer:
{"entities": [{"text": "coli K - 12", "type": "Bacterium"}, {"text": "strain", "type": "Bacterium"}, {"text": "adaptation", "type": "BiologicFunction"}, {"text": "redox - cycling", "type": "BiologicFunction"}, {"text": "herbicide", "type": "Chemical"}, {"text": "isoforms", "type": "Chemical"}, {"text": "SOD", "type": "Chemical"}, {"text": "CAT enzymes", "type": "Chemical"}]}

Example input:
Sentence: coli isolates ( 53 from diarrheic herds and 17 from healthy herds ) were examined by PCR for detection of the virulence genes associated with pathogenic E .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "diarrheic", "type": "Finding"}, {"text": "PCR", "type": "ResearchActivity"}, {"text": "virulence", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "E .", "type": "Bacterium"}]}

Example input:
Sentence: These two genes were acquired independently in one highly virulent isolate AL101002 , and clustered with Tn916 and IS1216 , respectively .

Example answer:
{"entities": [{"text": "genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: cholerae is not only critical for survival in various environments and but also is implicated in pathogenicity .

Example answer:
{"entities": [{"text": "cholerae", "type": "Bacterium"}, {"text": "environments", "type": "SpatialConcept"}]}

Example input:
Sentence: cholerae strains within these aquatic environmental reservoirs .

Example answer:
{"entities": [{"text": "cholerae", "type": "Bacterium"}, {"text": "reservoirs", "type": "SpatialConcept"}]}

Example input:
Sentence: These isolates cluster in the evolutionary tree with strains responsible for clinical cholera , possessing genomic components of 6 ( th ) and 7 ( th ) pandemic lineages , and diverge from " modern " cholera strains around 1548 C .

Example answer:
{"entities": [{"text": "isolates", "type": "Chemical"}, {"text": "tree", "type": "Eukaryote"}, {"text": "cholera", "type": "BiologicFunction"}, {"text": "genomic components", "type": "AnatomicalStructure"}]}

Example input:
Sentence: cholerae O1 strains serving as a source for recurrent cholera epidemics and pandemic disease .

Example answer:
{"entities": [{"text": "cholerae O1", "type": "Bacterium"}, {"text": "source", "type": "Finding"}, {"text": "cholera epidemics", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Non - toxigenic environmental Vibrio cholerae O1 strain from Haiti provides evidence of pre - pandemic cholera in Hispaniola Vibrio cholerae is ubiquitous in aquatic environments , with environmental toxigenic V .

Example answer:
{"entities": [{"text": "environmental", "type": "SpatialConcept"}, {"text": "Vibrio cholerae O1", "type": "Bacterium"}, {"text": "Haiti", "type": "SpatialConcept"}, {"text": "cholera", "type": "BiologicFunction"}, {"text": "Hispaniola", "type": "SpatialConcept"}, {"text": "Vibrio cholerae", "type": "Bacterium"}, {"text": "toxigenic", "type": "IntellectualProduct"}, {"text": "V .", "type": "Bacterium"}]}

Example input:
Sentence: Through monitoring of the Haitian aquatic environment following the 2010 cholera epidemic , we isolated two novel non - toxigenic ( ctxA / B - negative ) Vibrio cholerae O1 .

Example answer:
{"entities": [{"text": "Haitian", "type": "SpatialConcept"}, {"text": "cholera epidemic", "type": "BiologicFunction"}, {"text": "ctxA / B", "type": "AnatomicalStructure"}, {"text": "negative", "type": "Finding"}, {"text": "Vibrio cholerae O1", "type": "Bacterium"}]}

Input:
Sentence: It also raises the possibility that these and similar environmental strains could acquire virulence genes from the 2010 Haitian epidemic clone , including the cholera toxin producing CTXϕ .

## Item MedMentions:test:2060
Example input:
Sentence: Under each maintenance dose , six experimental sample and choice sessions were completed involving oral oxycodone administration ( 0 , 15 , and 30 mg / 70 kg , p . o . ) .

Example answer:
{"entities": [{"text": "experimental", "type": "ResearchActivity"}, {"text": "oral", "type": "SpatialConcept"}, {"text": "oxycodone", "type": "Chemical"}, {"text": "administration", "type": "HealthCareActivity"}]}

Example input:
Sentence: Mean opioid consumption for the 3 fracture - type groups ( AO / OTA [ Arbeitsgemeinschaft für Osteosynthesefragen / Orthopaedic Trauma Association ] classification ) was 57 . 7 mg ( class A ) , 60 . 3 mg ( class B ) , and 62 . 0 mg ( class C ) .

Example answer:
{"entities": [{"text": "AO / OTA [ Arbeitsgemeinschaft für Osteosynthesefragen / Orthopaedic Trauma Association ] classification", "type": "IntellectualProduct"}, {"text": "class A", "type": "IntellectualProduct"}, {"text": "class B", "type": "IntellectualProduct"}, {"text": "class C", "type": "IntellectualProduct"}]}

Example input:
Sentence: Clinicians are in need of additional and well - designed randomized control trials that focus on the indications for opioid therapy , appropriate opioid doses and dosing intervals , outcomes with adequacy of symptom control , and reporting on the incidence of adverse side effects .

Example answer:
{"entities": [{"text": "Clinicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "randomized control trials", "type": "ResearchActivity"}, {"text": "opioid", "type": "Chemical"}, {"text": "therapy", "type": "HealthCareActivity"}, {"text": "symptom control", "type": "HealthCareActivity"}, {"text": "adverse side effects", "type": "BiologicFunction"}]}

Example input:
Sentence: The effectiveness of different categories of opioids , dose , duration , and commonly prescribed opioids varied across studies .

Example answer:
{"entities": [{"text": "opioids", "type": "Chemical"}, {"text": "studies", "type": "IntellectualProduct"}]}

Example input:
Sentence: Non - treatment - seeking opioid - dependent male volunteers ( n = 11 ) underwent an in - patient detoxification with morphine , followed by maintenance on placebo ( 0 mg b .

Example answer:
{"entities": [{"text": "opioid - dependent", "type": "BiologicFunction"}, {"text": "male", "type": "PopulationGroup"}, {"text": "detoxification", "type": "HealthCareActivity"}, {"text": "morphine", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: We aimed to study the period prevalence and indications of opioids actually prescribed in people with end - stage COPD .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "opioids", "type": "Chemical"}, {"text": "people", "type": "PopulationGroup"}, {"text": "COPD", "type": "BiologicFunction"}]}

Example input:
Sentence: Mean opioid consumption ( morphine equivalence ) over a mean of 4 . 8 postoperative days ( range , 0 - 16 days ) was 58 . 5 mg ( range , 0 - 280 mg ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Mean overall opioid consumption ( morphine equivalence ) was 58 . 5 mg , or 14 .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: 1 ( interquartile range 0 . 6 - 2 . 0 ) years , 1 , 034 patients ( 46 % ) were dispensed ≥1 opioid prescription ( N = 13 , 722 prescriptions ) .

Example answer:
{"entities": [{"text": "dispensed", "type": "HealthCareActivity"}, {"text": "opioid", "type": "Chemical"}, {"text": "prescription", "type": "HealthCareActivity"}, {"text": "prescriptions", "type": "HealthCareActivity"}]}

Example input:
Sentence: Among those with a prescription , taking more than prescribed was most common for narcotics ( 6 . 8 % ) , followed by sedatives ( 4 . 8 % ) , stimulants ( 3 . 8 % ) , and antidepressants ( 1 . 5 % ) .

Example answer:
{"entities": [{"text": "prescription", "type": "IntellectualProduct"}, {"text": "narcotics", "type": "Chemical"}, {"text": "sedatives", "type": "Chemical"}, {"text": "stimulants", "type": "Chemical"}, {"text": "antidepressants", "type": "Chemical"}]}

Input:
Sentence: The most frequently prescribed opioids were tramadol ( 23 % ) , oxycodone ( 23 % ) , morphine ( 16 % ) , and codeine ( 16 % ) .

## Item MedMentions:test:1864
Example input:
Sentence: Previously , we discovered that beta - funaltrexamine ( β - FNA ) inhibits inflammatory signaling in human astrocytes in vitro , resulting in reduced expression of proinflammatory cytokines / chemokines .

Example answer:
{"entities": [{"text": "beta - funaltrexamine", "type": "Chemical"}, {"text": "β - FNA", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "astrocytes", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "cytokines", "type": "BiologicFunction"}, {"text": "chemokines", "type": "Chemical"}]}

Example input:
Sentence: Effects of etomidate and propofol on immune function in patients with lung adenocarcinoma To investigate the effects of etomidate and propofol on immune function in patients with lung adenocarcinoma .

Example answer:
{"entities": [{"text": "etomidate", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "immune function", "type": "BiologicFunction"}, {"text": "lung adenocarcinoma", "type": "BiologicFunction"}]}

Example input:
Sentence: These results indicate that aging and AD -like brain pathology increase the vulnerability to cognitive impairment after anesthesia and that intranasal treatment with insulin can prevent anesthesia - induced cognitive impairment .

Example answer:
{"entities": [{"text": "aging", "type": "BiologicFunction"}, {"text": "AD", "type": "BiologicFunction"}, {"text": "brain pathology", "type": "BiologicFunction"}, {"text": "cognitive impairment", "type": "BiologicFunction"}, {"text": "anesthesia", "type": "HealthCareActivity"}, {"text": "intranasal treatment", "type": "HealthCareActivity"}, {"text": "insulin", "type": "Chemical"}]}

Example input:
Sentence: The results of present study showed that captopril improved the LPS - induced learning and memory impairments in rats which were accompanied with attenuating hippocampal cytokine levels and improving the brain tissues oxidative damage criteria .

Example answer:
{"entities": [{"text": "captopril", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "learning", "type": "BiologicFunction"}, {"text": "memory impairments", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "cytokine", "type": "Chemical"}, {"text": "brain tissues", "type": "AnatomicalStructure"}, {"text": "damage", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The results showed that paclitaxel decreased the mechanical nociceptive thresholds and increased GFAP expression , leading to spinal astrocyte activation .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "mechanical nociceptive", "type": "BiologicFunction"}, {"text": "GFAP", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "spinal", "type": "AnatomicalStructure"}, {"text": "astrocyte activation", "type": "BiologicFunction"}]}

Example input:
Sentence: Anti - nociceptive roles of the glia -specific metabolic inhibitor fluorocitrate in paclitaxel - evoked neuropathic pain Paclitaxel ( Taxol ) is a powerful chemotherapy drug used in breast cancers , but it often causes neuropathic pain , leading to the early cessation of therapy and poor treatment outcomes .

Example answer:
{"entities": [{"text": "Anti - nociceptive roles", "type": "Finding"}, {"text": "glia", "type": "AnatomicalStructure"}, {"text": "metabolic inhibitor", "type": "BiologicFunction"}, {"text": "fluorocitrate", "type": "Chemical"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "neuropathic pain", "type": "Finding"}, {"text": "Paclitaxel", "type": "Chemical"}, {"text": "Taxol", "type": "Chemical"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "drug", "type": "Chemical"}, {"text": "breast cancers", "type": "BiologicFunction"}, {"text": "therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Propofol administration to patients was associated with minor further decreases in thalamic and insular connectivity .

Example answer:
{"entities": [{"text": "Propofol", "type": "Chemical"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "thalamic", "type": "AnatomicalStructure"}, {"text": "insular", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Anti - TNF therapy with etanercept shows promise as a potential treatment for AD .

Example answer:
{"entities": [{"text": "Anti - TNF therapy", "type": "HealthCareActivity"}, {"text": "etanercept", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "AD", "type": "BiologicFunction"}]}

Example input:
Sentence: The present study shows that propofol exposure in neonatal rats induces an increase of TNF - α in the cerebral spinal fluid , hippocampus and prefrontal cortex ( PFC ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "propofol", "type": "Chemical"}, {"text": "rats", "type": "Eukaryote"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "cerebral spinal fluid", "type": "BodySubstance"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "prefrontal cortex", "type": "AnatomicalStructure"}, {"text": "PFC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Furthermore , mTNF - α ( precursor of TNF - α ) expression in microglia cells is increased after propofol anaesthesia in either the hippocampus or PFC , but mTNF - α expression in neurons is only increased in the PFC .

Example answer:
{"entities": [{"text": "mTNF - α", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "microglia cells", "type": "AnatomicalStructure"}, {"text": "propofol", "type": "Chemical"}, {"text": "anaesthesia", "type": "HealthCareActivity"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "PFC", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}]}

Input:
Sentence: Etanercept , a TNF - α inhibitor , prevents propofol -induced short - or long - term neuronal apoptosis , neuronal loss , synaptic loss and long - term cognitive impairment .

## Item MedMentions:test:1680
Example input:
Sentence: Western blot and immunehistochemical study under confocal microscopy were used to investigate molecular identity of TASK channel .

Example answer:
{"entities": [{"text": "Western blot", "type": "HealthCareActivity"}, {"text": "immunehistochemical study", "type": "HealthCareActivity"}, {"text": "confocal microscopy", "type": "HealthCareActivity"}, {"text": "TASK channel", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , western blotting was used to analyze levels of proteins related to PI3K / Akt - 1 signaling pathway , and results indicated that ost can increase p - Akt and PI3K .

Example answer:
{"entities": [{"text": "western blotting", "type": "HealthCareActivity"}, {"text": "analyze", "type": "HealthCareActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "PI3K / Akt - 1 signaling pathway", "type": "BiologicFunction"}, {"text": "ost", "type": "Chemical"}, {"text": "p - Akt", "type": "Chemical"}, {"text": "PI3K", "type": "Chemical"}]}

Example input:
Sentence: Further analysis of the identified candidate protein included cell rescue experiments by gene transfer followed by subsequent screening of cells for induction of apoptosis and autophagy by immunoblotting , caspase activity as well as LC3 and MDC / PI staining .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "protein", "type": "Chemical"}, {"text": "cell", "type": "AnatomicalStructure"}, {"text": "experiments", "type": "ResearchActivity"}, {"text": "gene transfer", "type": "ResearchActivity"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "immunoblotting", "type": "HealthCareActivity"}, {"text": "caspase activity", "type": "BiologicFunction"}, {"text": "LC3", "type": "Chemical"}, {"text": "MDC", "type": "Chemical"}, {"text": "PI", "type": "Chemical"}, {"text": "staining", "type": "HealthCareActivity"}]}

Example input:
Sentence: Compared with FH2D - group , FH2D + group had a significantly higher oral glucose tolerance test ( OGTT ) 2 - hour insulin , RBP4 and baPWV levels , a lower adiponectin and glucose infusing rate ( GIR ) ( P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "FH2D -", "type": "Finding"}, {"text": "group", "type": "PopulationGroup"}, {"text": "FH2D +", "type": "Finding"}, {"text": "RBP4", "type": "Chemical"}, {"text": "adiponectin", "type": "HealthCareActivity"}]}

Example input:
Sentence: Skin biopsies from all the patients were evaluated before and after therapy for the expression of Ki - 67 , various skin barrier genes and thymic stromal lymphopoietin ( TSLP ) by real - time quantitative polymerase chain reaction and immunohistochemistry .

Example answer:
{"entities": [{"text": "Skin biopsies", "type": "HealthCareActivity"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "therapy", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Ki - 67", "type": "Chemical"}, {"text": "skin barrier", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "thymic stromal lymphopoietin", "type": "Chemical"}, {"text": "TSLP", "type": "Chemical"}, {"text": "real - time quantitative polymerase chain reaction", "type": "ResearchActivity"}, {"text": "immunohistochemistry", "type": "HealthCareActivity"}]}

Example input:
Sentence: In vivo testing indicates that a single patch can regulate glucose levels effectively with reduced risk of hypoglycemia .

Example answer:
{"entities": [{"text": "In vivo", "type": "SpatialConcept"}, {"text": "patch", "type": "Chemical"}, {"text": "glucose levels", "type": "Finding"}, {"text": "hypoglycemia", "type": "BiologicFunction"}]}

Example input:
Sentence: Blood samples were obtained at baseline to measure high - sensitive C - reactive protein ( hsCRP ) , interleukin - 6 ( IL - 6 ) , adiponectin and NT - proBNP .

Example answer:
{"entities": [{"text": "Blood samples", "type": "BodySubstance"}, {"text": "high - sensitive C - reactive protein", "type": "Chemical"}, {"text": "hsCRP", "type": "Chemical"}, {"text": "interleukin - 6", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "adiponectin", "type": "Chemical"}, {"text": "NT - proBNP", "type": "Chemical"}]}

Example input:
Sentence: Cell apoptosis and differentially expressed proteins was detected by flow cytometry ( FCM ) , quantitative real - time polymerase chain reaction ( qRT - PCR ) , and western blotting , respectively .

Example answer:
{"entities": [{"text": "Cell apoptosis", "type": "BiologicFunction"}, {"text": "differentially expressed proteins", "type": "Chemical"}, {"text": "detected", "type": "Finding"}, {"text": "flow cytometry", "type": "HealthCareActivity"}, {"text": "FCM", "type": "HealthCareActivity"}, {"text": "quantitative real - time polymerase chain reaction", "type": "ResearchActivity"}, {"text": "qRT - PCR", "type": "ResearchActivity"}, {"text": "western blotting", "type": "HealthCareActivity"}]}

Example input:
Sentence: 29 , 95 % CI : 1 . 46 - 3 . 58 ) and studies using the strictest diagnosis criteria , the National Diabetes Data Group criteria for 3 - h oral glucose tolerance test ( risk ratio 3 . 81 , 95 % CI : 2 . 18 - 6 . 67 ) .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "diagnosis criteria", "type": "IntellectualProduct"}, {"text": "National Diabetes Data Group criteria", "type": "IntellectualProduct"}, {"text": "oral glucose tolerance test", "type": "HealthCareActivity"}]}

Example input:
Sentence: Western blot and RT - PCR were employed to exam the expression of receptor for advanced glycation end products ( RAGE ) , low - density lipoprotein receptor - related protein - 1 ( LRP - 1 ) and amyloid precursor protein ( APP ) .

Example answer:
{"entities": [{"text": "Western blot", "type": "HealthCareActivity"}, {"text": "RT - PCR", "type": "ResearchActivity"}, {"text": "receptor for advanced glycation end products", "type": "Chemical"}, {"text": "RAGE", "type": "Chemical"}, {"text": "low - density lipoprotein receptor - related protein - 1", "type": "Chemical"}, {"text": "LRP - 1", "type": "Chemical"}, {"text": "amyloid precursor protein", "type": "Chemical"}, {"text": "APP", "type": "Chemical"}]}

Input:
Sentence: Investigations include oral glucose tolerance test , insulin tolerance test , histopathology by H & E and Masson 's trichrome staining , mRNA expression by real - time PCR , protein expression by Western blot , and caspase - 3 activity by colorimetry .

## Item MedMentions:test:2178
Example input:
Sentence: Moreover , the ability for mucin secretion and the expression of membrane water channel ( aquaporine 8 , AQP8 ) were increased significantly in the Lop + Urd treated group compared with Lop + Vehicle treated group .

Example answer:
{"entities": [{"text": "mucin", "type": "Chemical"}, {"text": "secretion", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "membrane water channel", "type": "Chemical"}, {"text": "aquaporine 8", "type": "Chemical"}, {"text": "AQP8", "type": "Chemical"}, {"text": "Lop", "type": "Chemical"}, {"text": "Urd", "type": "Chemical"}, {"text": "treated", "type": "Finding"}, {"text": "Vehicle", "type": "Chemical"}]}

Example input:
Sentence: Using a short hairpin RNA strategy , we demonstrate here that the 2 mammalian RBPs , PUMILIO ( PUM ) 1 and PUM2 , members of the PUF family of posttranscriptional regulators , are essential for hematopoietic stem / progenitor cell ( HSPC ) proliferation and survival in vitro and in vivo upon reconstitution assays .

Example answer:
{"entities": [{"text": "short hairpin RNA", "type": "Chemical"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "RBPs", "type": "Chemical"}, {"text": "PUMILIO", "type": "Chemical"}, {"text": "PUM ) 1", "type": "Chemical"}, {"text": "PUM2", "type": "Chemical"}, {"text": "PUF family", "type": "Chemical"}, {"text": "posttranscriptional regulators", "type": "BiologicFunction"}, {"text": "hematopoietic stem / progenitor cell ( HSPC ) proliferation", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "reconstitution assays", "type": "HealthCareActivity"}]}

Example input:
Sentence: The downregulation of uncoupling protein 2 ( UCP2 ) , which is attributed to hypoxia - inducible factor 1 ( HIF - 1 ) - mediated suppression of the transcriptional factor peroxisome proliferator - activated receptor γ ( PPARγ ) , was involved in NSCLC chemoresistance , and predicted a poor survival rate of patients receiving routine chemotherapy .

Example answer:
{"entities": [{"text": "downregulation", "type": "BiologicFunction"}, {"text": "uncoupling protein 2", "type": "Chemical"}, {"text": "UCP2", "type": "Chemical"}, {"text": "hypoxia - inducible factor 1", "type": "Chemical"}, {"text": "HIF - 1", "type": "Chemical"}, {"text": "suppression", "type": "BiologicFunction"}, {"text": "transcriptional factor", "type": "Chemical"}, {"text": "peroxisome proliferator - activated receptor γ", "type": "Chemical"}, {"text": "PPARγ", "type": "Chemical"}, {"text": "NSCLC", "type": "BiologicFunction"}, {"text": "chemoresistance", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Biochemical evidences indicated that the recombinant OcRhS1 was active in the pH range of 5 - 11 and over the temperature range of 0 - 60 ° C .

Example answer:
{"entities": [{"text": "recombinant OcRhS1", "type": "Chemical"}]}

Example input:
Sentence: OcRhS1 is a multi - domain protein with two sets of cofactor - binding motifs .

Example answer:
{"entities": [{"text": "OcRhS1", "type": "Chemical"}, {"text": "multi - domain protein", "type": "Chemical"}, {"text": "cofactor - binding motifs", "type": "BiologicFunction"}]}

Example input:
Sentence: The Km value of OcRhS1 for UDP - Glc was determined to be 1 . 52 × 10 ( - 4 ) M .

Example answer:
{"entities": [{"text": "OcRhS1", "type": "Chemical"}, {"text": "UDP - Glc", "type": "Chemical"}]}

Example input:
Sentence: Functional analyses of OcRhS1 and OcUER1 involved in UDP - L - rhamnose biosynthesis in Ornithogalum caudatum UDP - L - rhamnose ( UDP - Rha ) is an important sugar donor for the synthesis of rhamnose -containing compounds in plants .

Example answer:
{"entities": [{"text": "Functional analyses", "type": "ResearchActivity"}, {"text": "OcRhS1", "type": "Chemical"}, {"text": "OcUER1", "type": "Chemical"}, {"text": "UDP - L - rhamnose", "type": "Chemical"}, {"text": "Ornithogalum caudatum", "type": "Eukaryote"}, {"text": "UDP - Rha", "type": "Chemical"}, {"text": "sugar donor", "type": "Chemical"}, {"text": "rhamnose", "type": "Chemical"}, {"text": "compounds", "type": "Chemical"}, {"text": "plants", "type": "Eukaryote"}]}

Example input:
Sentence: Moreover , the N - terminal portion of OcRhS1 ( OcRhS1 - N ) was observed to metabolize UDP - Glc to form intermediate UDP - 4K6DG .

Example answer:
{"entities": [{"text": "N - terminal portion of OcRhS1", "type": "Chemical"}, {"text": "OcRhS1 - N", "type": "Chemical"}, {"text": "UDP - Glc", "type": "Chemical"}]}

Example input:
Sentence: OcUER1 shared high similarity with the carboxy - terminal domain of OcRhS1 ( OcRhS1 - C ) , suggesting its intrinsic ability of converting UDP - 4K6DG into UDP - Rha .

Example answer:
{"entities": [{"text": "OcUER1", "type": "Chemical"}, {"text": "carboxy - terminal domain of OcRhS1", "type": "Chemical"}, {"text": "OcRhS1 - C", "type": "Chemical"}, {"text": "UDP - Rha", "type": "Chemical"}]}

Example input:
Sentence: In vitro enzymatic assays revealed OcRhS1 can really convert UDP - D - glucose ( UDP - Glc ) into UDP - Rha via three consecutive reactions .

Example answer:
{"entities": [{"text": "enzymatic assays", "type": "HealthCareActivity"}, {"text": "OcRhS1", "type": "Chemical"}, {"text": "UDP - D - glucose", "type": "Chemical"}, {"text": "UDP - Glc", "type": "Chemical"}, {"text": "UDP - Rha", "type": "Chemical"}]}

Input:
Sentence: It was thus reasonably inferred that UDP - Glc could be bio - transformed into UDP - Rha under the collaborating action of OcRhS1 - N and OcUER1 .

## Item MedMentions:test:2298
Example input:
Sentence: In group I , T - SH , NGAL and urea levels were found to be significantly increased postoperatively compared to preoperative measurements ( p < 0 .

Example answer:
{"entities": [{"text": "T - SH", "type": "Chemical"}, {"text": "NGAL", "type": "Chemical"}, {"text": "urea levels", "type": "Finding"}]}

Example input:
Sentence: 0 % , which was significantly higher than that after liver resection and other types of HBPS ( 8 . 8 and 15 .

Example answer:
{"entities": [{"text": "liver resection", "type": "HealthCareActivity"}, {"text": "HBPS", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: However , in our study , surgery did not achieve the expected outcome in patients with specific metabolic , anthropometric and surgical characteristics ( BMI > 50 Kg / m2 , presence of metabolic syndrome , presence of T2DM with high preoperative HbA1c % level and gastric pouch volume greater than 60 ml ) .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "expected", "type": "IntellectualProduct"}, {"text": "surgical", "type": "HealthCareActivity"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "metabolic syndrome", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "gastric pouch", "type": "AnatomicalStructure"}]}

Example input:
Sentence: After surgery , the levels of interleukin - 6 ( IL - 6 ) , tumor necrosis factor alpha , and thromboxane B2 decreased by 23 . 5 % , 9 . 1 % , and 30 . 2 % , respectively , in the xenon group , but increased by 10 . 8 % , 26 . 2 % , and 26 . 4 % , respectively , in the control group .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "interleukin - 6", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "tumor necrosis factor alpha", "type": "Chemical"}, {"text": "thromboxane B2", "type": "Chemical"}]}

Example input:
Sentence: Following surgery , mean maximal OI values decreased by 18 . 8 % and 33 . 8 % , respectively , in the xenon and control groups .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "OI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Placebo - corrected HbA1c reduction was similar between Caucasian ( -0 .

Example answer:
{"entities": [{"text": "HbA1c", "type": "Chemical"}, {"text": "reduction", "type": "HealthCareActivity"}, {"text": "Caucasian", "type": "PopulationGroup"}]}

Example input:
Sentence: The HbA1c reduction from baseline with vildagliptin was similar across the racial / ethnic subgroups ( -0 . 83 % ± 0 . 02 % to -1 . 01 % ± 0 . 05 % ) .

Example answer:
{"entities": [{"text": "HbA1c", "type": "Chemical"}, {"text": "reduction", "type": "HealthCareActivity"}, {"text": "vildagliptin", "type": "Chemical"}, {"text": "racial", "type": "PopulationGroup"}, {"text": "ethnic subgroups", "type": "PopulationGroup"}]}

Example input:
Sentence: Within group comparison : The percentage of CD4 + in the two groups was significantly reduced at 24 hours post - operation ( T2 ) compared with the percentage before surgery , whereas the percentage of CD8 + was higher at T2 .

Example answer:
{"entities": [{"text": "percentage of CD4 +", "type": "HealthCareActivity"}, {"text": "percentage", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "percentage of CD8 + was higher", "type": "Finding"}]}

Example input:
Sentence: We observed significant reduction of body mass index ( BMI ) after surgery .

Example answer:
{"entities": [{"text": "body mass index", "type": "IntellectualProduct"}, {"text": "BMI", "type": "IntellectualProduct"}]}

Example input:
Sentence: The level of postoperative HbA1c % was related to BMI loss after surgery .

Example answer:
{"entities": [{"text": "HbA1c", "type": "Chemical"}, {"text": "BMI", "type": "IntellectualProduct"}]}

Input:
Sentence: We observed significant reduction of HbA1c % after surgery in both groups .

## Item MedMentions:test:2258
Example input:
Sentence: Hematologic response was observed in 68 % of patients ( very good partial response or complete response in 29 % ) , as well as improved survival .

Example answer:
{"entities": [{"text": "Hematologic response", "type": "Finding"}, {"text": "partial response", "type": "Finding"}, {"text": "complete response", "type": "Finding"}]}

Example input:
Sentence: MRI studies were performed to measure the volumes of intracranial hematoma and lateral ventricle at days 1 , 3 , 7 , 14 , and 28 after IVH .

Example answer:
{"entities": [{"text": "MRI studies", "type": "HealthCareActivity"}, {"text": "volumes", "type": "HealthCareActivity"}, {"text": "intracranial", "type": "SpatialConcept"}, {"text": "hematoma", "type": "BiologicFunction"}, {"text": "lateral ventricle", "type": "SpatialConcept"}, {"text": "IVH", "type": "BiologicFunction"}]}

Example input:
Sentence: 33 , 95 % CI , 1 . 80 - 22 . 23 ) , SDH ( OR 3 . 46 , 95 % CI , 1 . 39 - 8 . 63 ) , and skull fracture ( OR 2 . 67 , 95 % CI , 1 . 28 - 5 . 58 ) were associated with HPC .

Example answer:
{"entities": [{"text": "SDH", "type": "BiologicFunction"}, {"text": "skull fracture", "type": "InjuryOrPoisoning"}, {"text": "HPC", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Iron deposition , iron -related protein expression , ependymal damage , and histology were detected at day 28 .

Example answer:
{"entities": [{"text": "Iron deposition", "type": "BiologicFunction"}, {"text": "iron", "type": "Chemical"}, {"text": "protein expression", "type": "BiologicFunction"}, {"text": "detected", "type": "Finding"}]}

Example input:
Sentence: Intracranial lesions are of particular significance with respect to the timing of organizing hemorrhage given the acute , and often life - threatening nature of the hemorrhages , and the medicolegal investigation into potential crimes .

Example answer:
{"entities": [{"text": "Intracranial lesions", "type": "Finding"}, {"text": "hemorrhage", "type": "BiologicFunction"}, {"text": "life - threatening", "type": "Finding"}, {"text": "hemorrhages", "type": "BiologicFunction"}, {"text": "medicolegal investigation", "type": "HealthCareActivity"}]}

Example input:
Sentence: She was subsequently diagnosed with an intracranial hemorrhage in the distribution of the right basal ganglia .

Example answer:
{"entities": [{"text": "diagnosed", "type": "Finding"}, {"text": "intracranial hemorrhage", "type": "BiologicFunction"}, {"text": "right basal ganglia", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In conclusion , the Prussian Blue reaction was unreliable as an indicator of timing in intracranial hemorrhage .

Example answer:
{"entities": [{"text": "Prussian Blue reaction", "type": "HealthCareActivity"}, {"text": "indicator", "type": "Chemical"}, {"text": "intracranial hemorrhage", "type": "BiologicFunction"}]}

Example input:
Sentence: Moreover , iron loading led to a 15 % loss of olig2 - positive cells and a 16 % increase in number and greater activation of microglia compared with vehicle .

Example answer:
{"entities": [{"text": "iron", "type": "Chemical"}, {"text": "olig2", "type": "Chemical"}, {"text": "positive cells", "type": "AnatomicalStructure"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "microglia", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The Role of the Iron Stain in Assessing Intracranial Hemorrhage The timing of the breakdown of red blood cells and organization of hemorrhage has significance in the catabolism of heme and the processing of iron , but also has a practical application in terms of assigning , or attempting to assign , a time course with respect to traumatic events ( e . g .

Example answer:
{"entities": [{"text": "Iron Stain", "type": "HealthCareActivity"}, {"text": "Intracranial Hemorrhage", "type": "BiologicFunction"}, {"text": "red blood cells", "type": "AnatomicalStructure"}, {"text": "hemorrhage", "type": "BiologicFunction"}, {"text": "catabolism", "type": "BiologicFunction"}, {"text": "heme", "type": "Chemical"}, {"text": "iron", "type": "Chemical"}, {"text": "traumatic", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Therefore , this study examined the utility of the Prussian Blue iron stain in living patients with intracranial hemorrhages and well - defined symptom onset , to test whether the presence of Prussian Blue reactivity could be correlated with chronicity .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "examined", "type": "Finding"}, {"text": "Prussian Blue iron stain", "type": "Chemical"}, {"text": "intracranial hemorrhages", "type": "BiologicFunction"}, {"text": "presence", "type": "Finding"}, {"text": "Prussian Blue", "type": "Chemical"}]}

Input:
Sentence: It was found that out of 12 cases with intracranial hemorrhage , eight cases showed at least focal iron reactivity .

## Item MedMentions:test:2385
Example input:
Sentence: For cholesterol sensing , the microparticles embedded with γ - Fe2O3 nanoparticles were used as catalyst for the oxidation of 3 , 3 ' , 5 , 5 ' - Tetramethylbenzidine by H2O2 , an enzymatic hydrolysis product of cholesterol .

Example answer:
{"entities": [{"text": "cholesterol sensing", "type": "HealthCareActivity"}, {"text": "microparticles", "type": "Chemical"}, {"text": "oxidation", "type": "BiologicFunction"}, {"text": "3 , 3 ' , 5 , 5 ' - Tetramethylbenzidine", "type": "Chemical"}, {"text": "H2O2", "type": "Chemical"}, {"text": "enzymatic", "type": "Chemical"}, {"text": "cholesterol", "type": "Chemical"}]}

Example input:
Sentence: Among the various thermochemical and biochemical routes , fast pyrolysis followed by catalytic hydrotreating is considered to be a promising near - term opportunity .

Example answer:
{"entities": []}

Example input:
Sentence: Chaetomium thermophilum formate dehydrogenase has high activity in the reduction of hydrogen carbonate ( HCO3 - ) to formate While formate dehydrogenases ( FDHs ) have been used for cofactor recycling in chemoenzymatic synthesis , the ability of FDH to reduce CO2 could also be utilized in the conversion of CO2 to useful products via formate ( HCOO ( - ) ) .

Example answer:
{"entities": [{"text": "Chaetomium thermophilum", "type": "Eukaryote"}, {"text": "formate dehydrogenase", "type": "Chemical"}, {"text": "hydrogen carbonate", "type": "Chemical"}, {"text": "HCO3 -", "type": "Chemical"}, {"text": "formate", "type": "Chemical"}, {"text": "formate dehydrogenases", "type": "Chemical"}, {"text": "FDHs", "type": "Chemical"}, {"text": "cofactor", "type": "Chemical"}, {"text": "chemoenzymatic synthesis", "type": "BiologicFunction"}, {"text": "FDH", "type": "Chemical"}, {"text": "CO2", "type": "Chemical"}, {"text": "HCOO ( - )", "type": "Chemical"}]}

Example input:
Sentence: The immobilized enzyme was finally used as enantioselective catalyst in kinetic resolution of racemic 1 - ph enylethanol ( 1 - PEOH ) , and its performance compared with the free PFL .

Example answer:
{"entities": [{"text": "immobilized", "type": "Finding"}, {"text": "enzyme", "type": "Chemical"}, {"text": "1 - ph enylethanol", "type": "Chemical"}, {"text": "1 - PEOH", "type": "Chemical"}, {"text": "PFL", "type": "Chemical"}]}

Example input:
Sentence: CtFDH was modeled in the presence of HCO3 ( - ) showing that it fits to the active site .

Example answer:
{"entities": [{"text": "CtFDH", "type": "Chemical"}, {"text": "HCO3 ( - )", "type": "Chemical"}]}

Example input:
Sentence: High Performance Reduction of H2O2 with an Electron Transport Decaheme Cytochrome on a Porous ITO Electrode The decaheme cytochrome MtrC from Shewanella oneidensis MR - 1 immobilized on an ITO electrode displays unprecedented H2O2 reduction activity .

Example answer:
{"entities": [{"text": "H2O2", "type": "Chemical"}, {"text": "Electron Transport", "type": "BiologicFunction"}, {"text": "Decaheme Cytochrome", "type": "Chemical"}, {"text": "ITO", "type": "Chemical"}, {"text": "decaheme cytochrome MtrC", "type": "Chemical"}, {"text": "Shewanella oneidensis MR - 1", "type": "Bacterium"}, {"text": "immobilized", "type": "Chemical"}]}

Example input:
Sentence: Our findings demonstrate the potential of multiheme cytochromes to catalyze technologically relevant reactions and establish MtrC as a new benchmark in biotechnological H2O2 reduction with scope for applications in fuel cells and biosensors .

Example answer:
{"entities": [{"text": "multiheme cytochromes", "type": "Chemical"}, {"text": "MtrC", "type": "Chemical"}, {"text": "biotechnological", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "H2O2", "type": "Chemical"}]}

Example input:
Sentence: The catalytic efficiency with NADPH was 27 times higher compared to NADH .

Example answer:
{"entities": [{"text": "NADPH", "type": "Chemical"}, {"text": "NADH", "type": "Chemical"}]}

Example input:
Sentence: Enzyme kinetic studies were carried out with Hoechst 33342 as fluorescent dye and substrate of ABCG2 to elucidate the compounds binding modes .

Example answer:
{"entities": [{"text": "Hoechst 33342", "type": "Chemical"}, {"text": "fluorescent dye", "type": "Chemical"}, {"text": "ABCG2", "type": "Chemical"}, {"text": "compounds", "type": "Chemical"}]}

Example input:
Sentence: However , the high concentrations of HCO3 ( - ) reduced the reaction rate .

Example answer:
{"entities": [{"text": "HCO3 ( - )", "type": "Chemical"}]}

Input:
Sentence: The catalytic performance with HCO3 ( - ) as a substrate was evaluated by measuring the kinetic rates and conducting productivity assays .

## Item MedMentions:test:2406
Example input:
Sentence: 1 . 6 ; t = 1 . 99 , p = 0 . 058 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Walker , T .

Example answer:
{"entities": []}

Example input:
Sentence: Interestingly , a T .

Example answer:
{"entities": [{"text": "T .", "type": "Bacterium"}]}

Example input:
Sentence: mansoni and T .

Example answer:
{"entities": [{"text": "mansoni", "type": "Eukaryote"}, {"text": "T .", "type": "Eukaryote"}]}

Example input:
Sentence: surinamensis and T .

Example answer:
{"entities": [{"text": "surinamensis", "type": "Eukaryote"}, {"text": "T .", "type": "Eukaryote"}]}

Example input:
Sentence: coli and T .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "T .", "type": "Bacterium"}]}

Example input:
Sentence: coli and T .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "T .", "type": "Bacterium"}]}

Example input:
Sentence: equigenitalis and T .

Example answer:
{"entities": [{"text": "equigenitalis", "type": "Bacterium"}, {"text": "T .", "type": "Bacterium"}]}

Example input:
Sentence: All T .

Example answer:
{"entities": [{"text": "T .", "type": "Eukaryote"}]}

Example input:
Sentence: The T .

Example answer:
{"entities": [{"text": "T .", "type": "Eukaryote"}]}

Input:
Sentence: T .

## Item MedMentions:test:2236
Example input:
Sentence: The aim of this position paper authored by Austrian experts is to outline the current evidence and provide an overview of recent studies .

Example answer:
{"entities": [{"text": "position paper", "type": "IntellectualProduct"}, {"text": "Austrian", "type": "PopulationGroup"}, {"text": "experts", "type": "ProfessionalOrOccupationalGroup"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: This journal requires that authors assign a level of evidence to each article .

Example answer:
{"entities": [{"text": "journal", "type": "IntellectualProduct"}, {"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "level of evidence", "type": "Finding"}, {"text": "article", "type": "IntellectualProduct"}]}

Example input:
Sentence: The quality of the included primary studies was assessed using the National Health and Medical Research Council evidence hierarchy and the McMaster Critical Appraisal Tool for Quantitative Studies .

Example answer:
{"entities": [{"text": "primary studies", "type": "ResearchActivity"}, {"text": "National Health and Medical Research Council", "type": "Organization"}, {"text": "McMaster Critical Appraisal Tool", "type": "IntellectualProduct"}]}

Example input:
Sentence: This process tightly manages conflicts of interest and strives for evidence - based , as opposed to opinion - based , guidelines , with a clear citation of the supporting evidence .

Example answer:
{"entities": [{"text": "guidelines", "type": "IntellectualProduct"}]}

Example input:
Sentence: A secondary descriptive design with a deductive content analysis was used .

Example answer:
{"entities": []}

Example input:
Sentence: A Universal Design perspective with a holistic understanding remains critical to the foundation of this research study .

Example answer:
{"entities": [{"text": "Universal Design perspective", "type": "IntellectualProduct"}, {"text": "research study", "type": "ResearchActivity"}]}

Example input:
Sentence: Data extraction and quality assessment was performed independently by two authors , and resolved by consensus with a third reviewer .

Example answer:
{"entities": [{"text": "Data extraction", "type": "ResearchActivity"}, {"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "reviewer", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: This may reflect the greater importance of other features , including subvisible pathology , or methodological limitations of the primary literature .

Example answer:
{"entities": [{"text": "pathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "literature", "type": "IntellectualProduct"}]}

Example input:
Sentence: The authors have no conflicts of interest to declare .

Example answer:
{"entities": [{"text": "authors", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: The authors present direct evidence on quality standard implementation , identify implementation shortcomings and make recommendations for future research and practice .

Example answer:
{"entities": [{"text": "quality standard", "type": "IntellectualProduct"}, {"text": "research", "type": "ResearchActivity"}]}

Input:
Sentence: Authors should clearly describe the methods used and provide clear descriptions of and justifications for their design and primary analysis .
