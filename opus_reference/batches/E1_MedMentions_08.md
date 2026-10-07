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

## Item MedMentions:test:1569
Example input:
Sentence: LSS values found on cheeks ( ≈0 . 5 N / mm ) were about four times lower than those of the scalp ( ≈2 N / mm ) and about half those of forearms ( ≈1 N / mm ) .

Example answer:
{"entities": [{"text": "LSS", "type": "Finding"}, {"text": "cheeks", "type": "AnatomicalStructure"}, {"text": "scalp", "type": "AnatomicalStructure"}, {"text": "forearms", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The effect of a 7 % glycerol based formula was recorded 20 min post application onto the forearm , leading to a slight drop in LSS ( approx . 15 % ) as compared to a vehicle - applied skin site .

Example answer:
{"entities": [{"text": "glycerol", "type": "Chemical"}, {"text": "formula", "type": "IntellectualProduct"}, {"text": "application", "type": "HealthCareActivity"}, {"text": "forearm", "type": "AnatomicalStructure"}, {"text": "LSS", "type": "Finding"}, {"text": "skin site", "type": "SpatialConcept"}]}

Example input:
Sentence: Measuring and Modeling Contractile Drying in Human Stratum Corneum Stratum corneum ( SC ) is the most superficial skin layer .

Example answer:
{"entities": [{"text": "Modeling", "type": "ResearchActivity"}, {"text": "Human", "type": "Eukaryote"}, {"text": "Stratum Corneum", "type": "AnatomicalStructure"}, {"text": "Stratum corneum", "type": "AnatomicalStructure"}, {"text": "SC", "type": "AnatomicalStructure"}, {"text": "superficial", "type": "SpatialConcept"}, {"text": "skin layer", "type": "AnatomicalStructure"}]}

Example input:
Sentence: ROC curve analyses were used to evaluate the optimal cut - off point of skinfold thickness for overweight and obesity , based on the International Obesity Task Force definitions .

Example answer:
{"entities": [{"text": "analyses", "type": "ResearchActivity"}, {"text": "skinfold thickness", "type": "HealthCareActivity"}, {"text": "overweight", "type": "Finding"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "International Obesity Task Force definitions", "type": "IntellectualProduct"}]}

Example input:
Sentence: Skinfold thickness and BMI of these patients were measured and compared before and after the treatment .

Example answer:
{"entities": [{"text": "Skinfold thickness", "type": "HealthCareActivity"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aims of this study were to establish Colombian smoothed centile charts and LMS L ( Box - Cox transformation ) , M ( median ) , and S ( coefficient of variation ) tables for triceps , subscapular , and triceps + subscapular skinfolds ; appropriate cut - offs were selected using receiver operating characteristic ( ROC ) analysis based on a population - based sample of children and adolescents in Bogotá , Colombia .

Example answer:
{"entities": [{"text": "smoothed centile charts", "type": "IntellectualProduct"}, {"text": "tables", "type": "IntellectualProduct"}, {"text": "triceps", "type": "AnatomicalStructure"}, {"text": "subscapular", "type": "AnatomicalStructure"}, {"text": "triceps", "type": "ClinicalAttribute"}, {"text": "subscapular skinfolds", "type": "Finding"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "Bogotá", "type": "SpatialConcept"}, {"text": "Colombia", "type": "SpatialConcept"}]}

Example input:
Sentence: Smoothed percentile curves for triceps and subscapular skinfold thickness were derived using the LMS method .

Example answer:
{"entities": [{"text": "Smoothed percentile curves", "type": "SpatialConcept"}, {"text": "triceps", "type": "AnatomicalStructure"}, {"text": "subscapular skinfold thickness", "type": "Finding"}, {"text": "LMS method", "type": "IntellectualProduct"}]}

Example input:
Sentence: Triceps and Subscapular Skinfold Thickness Percentiles and Cut - Offs for Overweight and Obesity in a Population - Based Sample of Schoolchildren and Adolescents in Bogota , Colombia The assessment of skinfold thickness is an objective measure of adiposity .

Example answer:
{"entities": [{"text": "Triceps", "type": "AnatomicalStructure"}, {"text": "Subscapular Skinfold Thickness", "type": "Finding"}, {"text": "Overweight", "type": "Finding"}, {"text": "Obesity", "type": "BiologicFunction"}, {"text": "Bogota", "type": "SpatialConcept"}, {"text": "Colombia", "type": "SpatialConcept"}, {"text": "skinfold thickness", "type": "HealthCareActivity"}]}

Example input:
Sentence: Triceps and subscapular skinfold measurements were obtained using standardized methods .

Example answer:
{"entities": [{"text": "Triceps", "type": "AnatomicalStructure"}, {"text": "subscapular", "type": "AnatomicalStructure"}, {"text": "skinfold measurements", "type": "HealthCareActivity"}, {"text": "methods", "type": "IntellectualProduct"}]}

Example input:
Sentence: Subscapular and triceps skinfolds and T + SS were significantly higher in girls than in boys ( p < 0 . 001 ) .

Example answer:
{"entities": [{"text": "Subscapular", "type": "Finding"}, {"text": "triceps skinfolds", "type": "ClinicalAttribute"}, {"text": "T", "type": "ClinicalAttribute"}, {"text": "SS", "type": "Finding"}]}

Input:
Sentence: We calculated the triceps + subscapular skinfold ( T + SS ) sum .

## Item MedMentions:test:1772
Example input:
Sentence: Encoding and retrieval are supported by the engagement of both distinct neural pathways across the cortex and common structures within the medial temporal lobes .

Example answer:
{"entities": [{"text": "Encoding", "type": "BiologicFunction"}, {"text": "neural pathways", "type": "AnatomicalStructure"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "structures", "type": "SpatialConcept"}, {"text": "medial temporal lobes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: These systems often consist of interacting subsystems , whose characterization is of importance for a complete understanding of the brain interaction processes .

Example answer:
{"entities": []}

Example input:
Sentence: Structure - function relations in physiology education : Where 's the mechanism ? Physiology demands systems thinking : reasoning within and between levels of biological organization and across different organ systems .

Example answer:
{"entities": [{"text": "Structure - function", "type": "BiologicFunction"}, {"text": "physiology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Physiology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "systems thinking", "type": "Finding"}, {"text": "biological organization", "type": "AnatomicalStructure"}, {"text": "organ systems", "type": "BodySystem"}]}

Example input:
Sentence: In humans , this network has expanded in multiple ways , including the development of a dorsal object vision system mirroring the complexity of the ventral stream , the integration of object information with parietal working memory systems , and the emergence of tool - specific object representations in the anterior intraparietal sulcus and regions of the inferior parietal lobe .

Example answer:
{"entities": [{"text": "humans", "type": "Eukaryote"}, {"text": "network", "type": "BodySystem"}, {"text": "development", "type": "BiologicFunction"}, {"text": "dorsal object vision system", "type": "BodySystem"}, {"text": "complexity", "type": "BiologicFunction"}, {"text": "ventral stream", "type": "AnatomicalStructure"}, {"text": "parietal", "type": "SpatialConcept"}, {"text": "memory systems", "type": "BodySystem"}, {"text": "tool - specific object representations", "type": "BiologicFunction"}, {"text": "anterior", "type": "SpatialConcept"}, {"text": "intraparietal sulcus", "type": "SpatialConcept"}, {"text": "inferior parietal lobe", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Singularities of Three - Layered Complex - Valued Neural Networks With Split Activation Function There are three important concepts related to learning processes in neural networks : reducibility , nonminimality , and singularity .

Example answer:
{"entities": [{"text": "Neural Networks", "type": "BiologicFunction"}, {"text": "learning", "type": "BiologicFunction"}, {"text": "neural networks", "type": "BiologicFunction"}]}

Example input:
Sentence: An emerging theme from this comparative analysis is that non - spatial information is represented to a greater degree , and with increased complexity , in the human dorsal visual system .

Example answer:
{"entities": [{"text": "complexity", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "dorsal visual system", "type": "BodySystem"}]}

Example input:
Sentence: Recently , it has been suggested that conscious perception might arise from the dynamic interplay of functionally specialized but widely distributed cortical areas .

Example answer:
{"entities": [{"text": "conscious", "type": "BiologicFunction"}, {"text": "perception", "type": "BiologicFunction"}, {"text": "cortical areas", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Many physiological mechanisms explain how structures and their properties interact at one level of organization to produce emergent functions at a higher level of organization .

Example answer:
{"entities": [{"text": "physiological", "type": "BiologicFunction"}, {"text": "structures", "type": "AnatomicalStructure"}, {"text": "organization", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The complexity of the human brain , including normal functioning and potential for dysfunctions , has developed over evolutionary time and has been shaped by natural selection .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "dysfunctions", "type": "BiologicFunction"}]}

Example input:
Sentence: We interpret these results as evidence that students see mechanisms as holding a more narrow definition than used in the biological sciences , and that students struggle to coordinate and distinguish mechanisms from functions due to cognitive processes germane to learning in many domains .

Example answer:
{"entities": [{"text": "students", "type": "PopulationGroup"}, {"text": "definition", "type": "IntellectualProduct"}, {"text": "learning", "type": "BiologicFunction"}]}

Input:
Sentence: We argue that these concepts are complex and cannot be reduced to neural mechanisms , but involve embodied and situated processes that include the physical and social environments .

## Item MedMentions:test:1463
Example input:
Sentence: To investigate the impact of prolonged alcohol exposure , conditioned suppression of alcohol seeking was assessed after 2 and 4 months of intermittent alcohol access ( IAA ) in a subgroup of rats drinking moderate amounts of alcohol .

Example answer:
{"entities": [{"text": "subgroup", "type": "IntellectualProduct"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: One hundred four - week - old female Wistar rats were randomly divided into MMID ( low iodine intake [ L ] ) and normal ( normal iodine intake [ N ] ) groups .

Example answer:
{"entities": [{"text": "female Wistar rats", "type": "Eukaryote"}, {"text": "MMID", "type": "BiologicFunction"}, {"text": "low iodine intake", "type": "Finding"}, {"text": "normal", "type": "Finding"}, {"text": "normal iodine intake", "type": "Finding"}]}

Example input:
Sentence: However , there has been relatively little investigation into the behavioral effects of ID on drug addiction .

Example answer:
{"entities": [{"text": "investigation", "type": "HealthCareActivity"}, {"text": "ID", "type": "BiologicFunction"}, {"text": "drug addiction", "type": "BiologicFunction"}]}

Example input:
Sentence: Notably , the morphine - withdrawn rats displayed persistent motivated behaviors for high - value rewards ( 60 % sucrose and sexual stimulus ) in the conflict tests suggesting impairments in inhibitory control in morphine - treated rats .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "withdrawn", "type": "HealthCareActivity"}, {"text": "rats", "type": "Eukaryote"}, {"text": "motivated", "type": "BiologicFunction"}, {"text": "rewards", "type": "BiologicFunction"}, {"text": "sucrose", "type": "Chemical"}]}

Example input:
Sentence: There is evidence that ID early in development ( preweaning in rat ) causes irreversible neurologic , behavioral , and motor development deficits .

Example answer:
{"entities": [{"text": "ID", "type": "BiologicFunction"}, {"text": "early in development", "type": "Finding"}, {"text": "preweaning", "type": "Finding"}, {"text": "rat", "type": "Eukaryote"}, {"text": "irreversible", "type": "Finding"}, {"text": "neurologic", "type": "Finding"}, {"text": "behavioral", "type": "BiologicFunction"}]}

Example input:
Sentence: Rats were assessed for cocaine - seeking behaviors after either intra - accumbal injections of the BRG1 inhibitor PFI3 or viral - mediated overexpression of BRG1 .

Example answer:
{"entities": [{"text": "Rats", "type": "Eukaryote"}, {"text": "cocaine - seeking behaviors", "type": "BiologicFunction"}, {"text": "intra - accumbal injections", "type": "HealthCareActivity"}, {"text": "BRG1", "type": "Chemical"}, {"text": "inhibitor PFI3", "type": "Chemical"}, {"text": "viral - mediated overexpression", "type": "BiologicFunction"}]}

Example input:
Sentence: This increase in responding , however , was less goal - directed as ID rats also responded more quickly to the non - rewarded manipulandum than did control rats .

Example answer:
{"entities": [{"text": "ID", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: In the present study , we assessed addiction for self - administered cocaine in rats with a history of preweaning ID only during postnatal days 4 through 21 , and iron replete thereafter .

Example answer:
{"entities": [{"text": "present", "type": "Finding"}, {"text": "study", "type": "ResearchActivity"}, {"text": "addiction", "type": "BiologicFunction"}, {"text": "cocaine", "type": "Chemical"}, {"text": "rats", "type": "Eukaryote"}, {"text": "history", "type": "Finding"}, {"text": "preweaning", "type": "Finding"}, {"text": "ID", "type": "BiologicFunction"}, {"text": "iron replete", "type": "HealthCareActivity"}]}

Example input:
Sentence: Preweaning iron deficiency increases non - contingent responding during cocaine self - administration in rats Iron deficiency ( ID ) is the most prevalent single - nutrient deficiency worldwide .

Example answer:
{"entities": [{"text": "Preweaning", "type": "Finding"}, {"text": "iron deficiency", "type": "BiologicFunction"}, {"text": "cocaine", "type": "Chemical"}, {"text": "self - administration", "type": "HealthCareActivity"}, {"text": "rats", "type": "Eukaryote"}, {"text": "Iron deficiency", "type": "BiologicFunction"}, {"text": "ID", "type": "BiologicFunction"}]}

Example input:
Sentence: In 2002 , we found that rats made ID from weaning ( postnatal day 21 ) and throughout the experiment acquired cocaine self - administration significantly more slowly than controls and failed to increase responding when the dose of the drug was decreased .

Example answer:
{"entities": [{"text": "found", "type": "Finding"}, {"text": "rats", "type": "Eukaryote"}, {"text": "ID", "type": "BiologicFunction"}, {"text": "weaning", "type": "Finding"}, {"text": "experiment", "type": "ResearchActivity"}, {"text": "cocaine", "type": "Chemical"}, {"text": "self - administration", "type": "HealthCareActivity"}, {"text": "drug", "type": "Chemical"}]}

Input:
Sentence: The results showed that while ID did not affect the number of cocaine infusions or the overall addiction -like behavior score , ID rats scored higher on a measure of continued responding for drug than did iron replete controls .

## Item MedMentions:test:1520
Example input:
Sentence: High hepatic tumor load ( > 50 % ) and high plasma chromogranin A ( > 600 ng / mL ) were negative baseline predictors for PFS and OS on univariate analysis , CgA remained significant on multivariate analysis ( PFS , P = 0 . 011 ; OS , P = 0 . 026 ) .

Example answer:
{"entities": [{"text": "hepatic tumor", "type": "BiologicFunction"}, {"text": "plasma chromogranin A", "type": "Chemical"}, {"text": "CgA", "type": "Chemical"}]}

Example input:
Sentence: Further analysis results indicated that SHMT2 had better prognostic value for estrogen receptor ( ER ) - negative breast cancer patients , compared to ER - positive patients .

Example answer:
{"entities": [{"text": "SHMT2", "type": "Chemical"}, {"text": "prognostic", "type": "IntellectualProduct"}, {"text": "estrogen receptor ( ER ) - negative", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "ER - positive", "type": "Finding"}]}

Example input:
Sentence: 8 % of the patients were classified as triple - negative breast cancer ( estrogen - recetor / progesteron - receptor - negative ) .

Example answer:
{"entities": [{"text": "triple - negative breast cancer", "type": "BiologicFunction"}, {"text": "estrogen - recetor / progesteron - receptor - negative", "type": "BiologicFunction"}]}

Example input:
Sentence: This correlation was stronger for triple negative and HER2 / neu positive subtypes ( r = 0 . 92 and 0 . 62 , respectively ) .

Example answer:
{"entities": [{"text": "triple negative", "type": "BiologicFunction"}, {"text": "HER2 / neu positive", "type": "ClinicalAttribute"}, {"text": "subtypes", "type": "IntellectualProduct"}]}

Example input:
Sentence: Notably , the low - risk group ( n = 51 ) of 205 estrogen receptor - positive and node negative ( ER + / node - ) patients from three different datasets who had not had any systemic adjuvant therapy had 100 % 15 - year disease - specific survival rate .

Example answer:
{"entities": [{"text": "group", "type": "PopulationGroup"}, {"text": "estrogen receptor - positive", "type": "BiologicFunction"}, {"text": "node negative", "type": "BiologicFunction"}, {"text": "ER +", "type": "BiologicFunction"}, {"text": "node -", "type": "BiologicFunction"}, {"text": "datasets", "type": "IntellectualProduct"}, {"text": "adjuvant therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Triple - negative and HR + / HER2 - subtypes are independent predictors for suboptimal OS in IBC .

Example answer:
{"entities": [{"text": "Triple - negative", "type": "BiologicFunction"}, {"text": "HR + / HER2 -", "type": "Finding"}, {"text": "subtypes", "type": "IntellectualProduct"}, {"text": "predictors", "type": "Finding"}, {"text": "IBC", "type": "BiologicFunction"}]}

Example input:
Sentence: For triple negative or HER2 / neu positive disease the sensitivity and specificity were 88 % ( 95 % CI , 62 - 98 ) and 75 % ( 95 % CI , 43 - 93 ) , respectively .

Example answer:
{"entities": [{"text": "triple negative", "type": "BiologicFunction"}, {"text": "HER2 / neu positive", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The multivariate analysis revealed that TN MBC patients had poorer OS and BCSM ( p < 0 .

Example answer:
{"entities": [{"text": "TN", "type": "Finding"}, {"text": "MBC", "type": "BiologicFunction"}]}

Example input:
Sentence: With adjustments for age , a hormone receptor - positive ( HoR + ) status was no longer related to increased non - BCSD s .

Example answer:
{"entities": [{"text": "hormone receptor - positive ( HoR + ) status", "type": "BiologicFunction"}, {"text": "non - BCSD", "type": "Finding"}]}

Example input:
Sentence: Simultaneously , the results showed that male patients in the HoR - positive / HER2 - negative subgroup were less likely to die of BC when adjusting for other factors ( p < 0 .

Example answer:
{"entities": [{"text": "HoR - positive / HER2 - negative subgroup", "type": "IntellectualProduct"}, {"text": "to die", "type": "Finding"}, {"text": "BC", "type": "BiologicFunction"}]}

Input:
Sentence: The univariate analysis showed that male triple - negative ( TN ) , hormone receptor ( HoR ) - positive / HER2 - positive and HoR - positive / HER2 - negative patients had poorer OS ( p < 0 . 01 ) .

## Item MedMentions:test:771
Example input:
Sentence: AAC ( 6 ' ) - Ib - cr significantly reduced the ciprofloxacin efficacy in vivo .

Example answer:
{"entities": [{"text": "AAC ( 6 ' ) - Ib - cr", "type": "Chemical"}, {"text": "ciprofloxacin", "type": "Chemical"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: Weight -based enoxaparin dosing ( 0 . 5 mg / kg / dose BID ) is an option in trauma patients considered to be at a lower risk of bleeding complications .

Example answer:
{"entities": [{"text": "enoxaparin", "type": "Chemical"}, {"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "bleeding", "type": "BiologicFunction"}, {"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients were centrally randomised ( 1 : 1 ) to receive either oral masitinib ( 6 mg / kg per day over 24 weeks with possible extension ) or matched placebo with minimisation according to severe symptoms .

Example answer:
{"entities": [{"text": "randomised", "type": "ResearchActivity"}, {"text": "masitinib", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}, {"text": "severe symptoms", "type": "Finding"}]}

Example input:
Sentence: In the 24 - month , phase III , randomised , controlled , ORAL Start trial ( NCT01039688 ) , patients were randomised 2 : 2 : 1 to receive tofacitinib 5 mg two times per day ( n = 373 ) , tofacitinib 10 mg two times per day ( n = 397 ) or MTX ( n = 186 ) .

Example answer:
{"entities": [{"text": "phase III", "type": "ResearchActivity"}, {"text": "randomised , controlled , ORAL Start trial", "type": "ResearchActivity"}, {"text": "NCT01039688", "type": "ResearchActivity"}, {"text": "randomised", "type": "Finding"}, {"text": "tofacitinib", "type": "Chemical"}, {"text": "MTX", "type": "Chemical"}]}

Example input:
Sentence: Similarly , the benefit of 5 mg twice daily dose of apixaban compared with warfarin on major bleeding in patients with 1 dose - reduction criterion ( HR , 0 .

Example answer:
{"entities": [{"text": "apixaban", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "bleeding", "type": "BiologicFunction"}]}

Example input:
Sentence: Little is known about patients with 1 dose - reduction criterion who received the 5 mg twice daily dose of apixaban .

Example answer:
{"entities": [{"text": "apixaban", "type": "Chemical"}]}

Example input:
Sentence: To determine the frequency of 1 dose - reduction criterion and whether the effects of the 5 mg twice daily dose of apixaban on stroke or systemic embolism and bleeding varied among patients with 1 or no dose - reduction criteria .

Example answer:
{"entities": [{"text": "apixaban", "type": "Chemical"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "bleeding", "type": "BiologicFunction"}]}

Example input:
Sentence: Of the patients with 1 or no dose - reduction criteria assigned to receive the 5 mg twice daily dose of apixaban or warfarin , 3966 had 1 dose - reduction criterion ; these patients had higher rates of stroke or systemic embolism ( HR , 1 . 47 ; 95 % CI , 1 . 20 - 1 . 81 ) and major bleeding ( HR , 1 . 89 ; 95 % CI , 1 . 62 - 2 . 20 ) compared with those with no dose - reduction criteria ( n = 13 356 ) .

Example answer:
{"entities": [{"text": "apixaban", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "bleeding", "type": "BiologicFunction"}]}

Example input:
Sentence: The benefit of the 5 mg twice daily dose of apixaban ( n = 8665 ) compared with warfarin ( n = 8657 ) on stroke or systemic embolism in patients with 1 dose - reduction criterion ( HR , 0 . 94 ; 95 % CI , 0 . 66 - 1 . 32 ) and no dose - reduction criterion ( HR , 0 . 77 ; 95 % CI , 0 . 62 - 0 . 97 ) were similar ( P for interaction = .36 ) .

Example answer:
{"entities": [{"text": "apixaban", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients with atrial fibrillation and isolated advanced age , low body weight , or renal dysfunction have a higher risk of stroke or systemic embolism and major bleeding but show consistent benefits with the 5 mg twice daily dose of apixaban vs warfarin compared with patients without these characteristics .

Example answer:
{"entities": [{"text": "atrial fibrillation", "type": "BiologicFunction"}, {"text": "renal dysfunction", "type": "Finding"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "bleeding", "type": "BiologicFunction"}, {"text": "apixaban", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}]}

Input:
Sentence: Apixaban 5 mg Twice Daily and Clinical Outcomes in Patients With Atrial Fibrillation and Advanced Age , Low Body Weight , or High Creatinine : A Secondary Analysis of a Randomized Clinical Trial In the Apixaban for Reduction of Stroke and Other Thromboembolic Complications in Atrial Fibrillation ( ARISTOTLE ) trial , the standard dose of apixaban was 5 mg twice daily ; patients with at least 2 dose - reduction criteria - 80 years or older , weight 60 kg or less , and creatinine level 1 . 5 mg / dL or higher - received a reduced dose of apixaban of 2 . 5 mg twice daily .

## Item MedMentions:test:1886
Example input:
Sentence: 7 ( 3 - 12 ) years , p < 0 . 001 ] were significant higher in those that used substances .

Example answer:
{"entities": []}

Example input:
Sentence: Age at the first visit as well as PNES onset was younger in the ID than in the non - ID group ( t = 2 . 651 , p = 0 . 009 ; t = 3 . 528 , p = 0 . 001 , respectively ) .

Example answer:
{"entities": [{"text": "visit", "type": "HealthCareActivity"}, {"text": "PNES", "type": "BiologicFunction"}, {"text": "ID", "type": "BiologicFunction"}, {"text": "non - ID", "type": "Finding"}]}

Example input:
Sentence: At any speed of fast walking , older children generated more peakA2 ( p = 0 . 001 ) and less peakH3 ( p = 0 . 001 ) than younger children .

Example answer:
{"entities": []}

Example input:
Sentence: There were significant differences ( P < 0 . 001 ; < 0 . 001 ; < 0 . 001 ; < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: No significant age difference was noted in terms of any HPV strain positivity .

Example answer:
{"entities": [{"text": "HPV", "type": "Virus"}, {"text": "positivity", "type": "Finding"}]}

Example input:
Sentence: Age was not statistically significant covariate for CAL ( F = 2 . 205 ; p > 0 . 05 ) , only for REC ( F = 4 . 601 ; p < 0 . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Mean PS values decreased as speed increased for comfortable walking ( p < 0 . 001 ) , fast walking ( p < 0 . 001 ) and fast running ( p < 0 . 001 ) , and less consistently during jogging ( p = 0 . 054 ) .

Example answer:
{"entities": []}

Example input:
Sentence: However , significant association was found with respect to younger age of presentation ( p value = 0 . 044 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 15 % , P = 0 . 99 ) , whereas it was significantly higher in men than in women at age ≥65 years ( 65 - 74 years , 38 % vs . 19 % , P < 0 .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: 67 ; p < 0 . 001 ) , among younger subjects ( OR = 1 .

Example answer:
{"entities": [{"text": "younger subjects", "type": "PopulationGroup"}]}

Input:
Sentence: PS varied with age ( p < 0 .

## Item MedMentions:test:1524
Example input:
Sentence: The risk to IAN injury increases many fold , when the third molar root overlaps the nerve canal as identified by the radiographic imaging .

Example answer:
{"entities": [{"text": "IAN", "type": "AnatomicalStructure"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "third molar root", "type": "AnatomicalStructure"}, {"text": "nerve canal", "type": "AnatomicalStructure"}, {"text": "radiographic imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: The following outcomes were extracted and analyzed : prevalence of heterotopic ossification and reoperation , preoperative and postoperative Neck Disability Index scores , preoperative and postoperative Visual Analog Scale scores , and success rate using the Odom grading system .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "heterotopic ossification", "type": "BiologicFunction"}, {"text": "reoperation", "type": "HealthCareActivity"}, {"text": "Neck Disability Index scores", "type": "Finding"}, {"text": "Visual Analog Scale scores", "type": "ClinicalAttribute"}, {"text": "Odom grading system", "type": "IntellectualProduct"}]}

Example input:
Sentence: Clinical parameters ( e . g . , bleeding on probing - BOP , probing depth - PD , mucosal recession - MR ) were assessed immediately after the cementation of the crown and at the final visit .

Example answer:
{"entities": [{"text": "Clinical parameters", "type": "ResearchActivity"}, {"text": "bleeding on probing", "type": "Finding"}, {"text": "BOP", "type": "Finding"}, {"text": "mucosal recession", "type": "AnatomicalStructure"}, {"text": "MR", "type": "AnatomicalStructure"}, {"text": "cementation of the crown", "type": "HealthCareActivity"}, {"text": "final visit", "type": "HealthCareActivity"}]}

Example input:
Sentence: Reassessment has revealed varying levels of completeness for our available AM dental records , the need to thoroughly review our computerized comparisons , adjust our comparisons to include molar pattern variations / third molars , and updating our database comparison program .

Example answer:
{"entities": [{"text": "dental records", "type": "IntellectualProduct"}, {"text": "review", "type": "IntellectualProduct"}, {"text": "molar", "type": "AnatomicalStructure"}, {"text": "pattern", "type": "SpatialConcept"}, {"text": "molars", "type": "AnatomicalStructure"}, {"text": "database", "type": "IntellectualProduct"}]}

Example input:
Sentence: Deep periodontal defects in the ( pre ) molar region were most underrated by intra - oral radiography .

Example answer:
{"entities": [{"text": "Deep", "type": "SpatialConcept"}, {"text": "( pre ) molar region", "type": "SpatialConcept"}, {"text": "intra - oral radiography", "type": "HealthCareActivity"}]}

Example input:
Sentence: 15 , 16 , and 17 were developmentally delayed and were displaying the characteristic " ghost appearance . " Comprehensive dental care was done under local anaesthesia and it included extraction of the primary molars affected by ROD , stainless steel crown on 64 , and caries prevention program .

Example answer:
{"entities": [{"text": "Comprehensive dental care", "type": "HealthCareActivity"}, {"text": "local anaesthesia", "type": "HealthCareActivity"}, {"text": "extraction", "type": "HealthCareActivity"}, {"text": "primary molars", "type": "Finding"}, {"text": "ROD", "type": "AnatomicalStructure"}, {"text": "stainless steel crown", "type": "MedicalDevice"}, {"text": "caries", "type": "BiologicFunction"}]}

Example input:
Sentence: Lateral cephalometric radiographs from 78 patients with impacted canines , 68 with dental agenesis and 17 with hyperdontia were collected .

Example answer:
{"entities": [{"text": "Lateral", "type": "SpatialConcept"}, {"text": "cephalometric", "type": "HealthCareActivity"}, {"text": "radiographs", "type": "HealthCareActivity"}, {"text": "impacted", "type": "AnatomicalStructure"}, {"text": "canines", "type": "Finding"}, {"text": "dental agenesis", "type": "AnatomicalStructure"}, {"text": "hyperdontia", "type": "Finding"}]}

Example input:
Sentence: Evaluation of Outcome Following Coronectomy for the Management of Mandibular Third Molars in Close Proximity to Inferior Alveolar Nerve Iatrogenic damage to Inferior Alveolar Nerve ( IAN ) is a significant risk factor following prophylactic or therapeutic removal of impacted mandibular third molar .

Example answer:
{"entities": [{"text": "Evaluation", "type": "HealthCareActivity"}, {"text": "Mandibular", "type": "AnatomicalStructure"}, {"text": "Third Molars", "type": "AnatomicalStructure"}, {"text": "Proximity", "type": "SpatialConcept"}, {"text": "Inferior Alveolar Nerve", "type": "AnatomicalStructure"}, {"text": "IAN", "type": "AnatomicalStructure"}, {"text": "risk factor", "type": "Finding"}, {"text": "prophylactic", "type": "HealthCareActivity"}, {"text": "therapeutic removal of impacted mandibular third molar", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of present study was to evaluate the fate of the root ( resorbed , exfoliated , covered by bone ) after coronectomy or intentional root retention of impacted mandibular 3 ( rd ) molars in patients with high risk for inferior alveolar nerve damage as evaluated by the intra oral periapical radiograph .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "root", "type": "AnatomicalStructure"}, {"text": "resorbed", "type": "BiologicFunction"}, {"text": "exfoliated", "type": "BiologicFunction"}, {"text": "bone", "type": "AnatomicalStructure"}, {"text": "root retention", "type": "BiologicFunction"}, {"text": "impacted mandibular 3 ( rd ) molars", "type": "BiologicFunction"}, {"text": "high risk", "type": "Finding"}, {"text": "inferior alveolar nerve", "type": "AnatomicalStructure"}, {"text": "damage", "type": "InjuryOrPoisoning"}, {"text": "evaluated", "type": "HealthCareActivity"}]}

Example input:
Sentence: Twenty impacted mandibular third molar teeth , in 18 patients with high risk of injury to IAN based on Rood 's Criteria in an intra oral periapical radiographic examination , between the age group of 18 to 40 years , were included in the study .

Example answer:
{"entities": [{"text": "impacted mandibular third molar teeth", "type": "BiologicFunction"}, {"text": "high risk", "type": "Finding"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "IAN", "type": "AnatomicalStructure"}, {"text": "Rood 's Criteria", "type": "IntellectualProduct"}]}

Input:
Sentence: Preoperatively the impacted third molars were evaluated clinically as well as radiographically . Pederson Difficulty Index and Winter 's Classification of impacted tooth was recorded .

## Item MedMentions:test:1825
Example input:
Sentence: In total , 519 patients completed 1 year of follow - up , among which 69 ( 13 .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients were evaluated periodically for two years at six months interval .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}]}

Example input:
Sentence: All surviving patients were prospectively followed for a mean of 14 . 7 years ( 9 . 8 to 28 . 3 ) with no loss to follow - up .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Both groups were followed up at 1 month , 6 months , 12 months , and yearly thereafter .

Example answer:
{"entities": [{"text": "followed up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients were then followed for three years .

Example answer:
{"entities": []}

Example input:
Sentence: Patients were followed up for six months with scheduled monthly remote monitoring transmissions in addition to routine in - office checks .

Example answer:
{"entities": [{"text": "followed up", "type": "HealthCareActivity"}, {"text": "remote", "type": "SpatialConcept"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "in - office checks", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients were followed up for 13 months to assess outcomes .

Example answer:
{"entities": []}

Example input:
Sentence: Twenty - eight patients were eligible for three - month follow - up .

Example answer:
{"entities": [{"text": "patients were eligible for three - month follow - up", "type": "Finding"}]}

Example input:
Sentence: Forty - one patients had a minimum of 6 - month of follow - up ( mean , 24 months ; range , 6 - 68 months ) .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients were followed for 24 months .

Example answer:
{"entities": []}

Input:
Sentence: All patients were followed up monthly for six months .

## Item MedMentions:test:1745
Example input:
Sentence: Moreover , bicuculline or D - serine treatments rescue the motor and cognitive deficits in MK - 801 -treated mice and reduce STEP61 in mouse frontal cortex .

Example answer:
{"entities": [{"text": "bicuculline", "type": "Chemical"}, {"text": "D - serine", "type": "Chemical"}, {"text": "treatments", "type": "HealthCareActivity"}, {"text": "motor", "type": "Finding"}, {"text": "cognitive deficits", "type": "BiologicFunction"}, {"text": "MK - 801", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "STEP61", "type": "Chemical"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "frontal cortex", "type": "AnatomicalStructure"}]}

Example input:
Sentence: RhoA / Rock Inhibition Improves the Beneficial Effects of Glucocorticoid Treatment in Dystrophic Muscle : Implications for Stem Cell Depletion Glucocorticoid treatment represents a standard palliative treatment for Duchenne muscular dystrophy ( DMD ) patients , but various adverse effects have limited this treatment .

Example answer:
{"entities": [{"text": "RhoA", "type": "Chemical"}, {"text": "Rock", "type": "Chemical"}, {"text": "Inhibition", "type": "BiologicFunction"}, {"text": "Dystrophic Muscle", "type": "BiologicFunction"}, {"text": "Stem Cell", "type": "AnatomicalStructure"}, {"text": "palliative treatment", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Duchenne muscular dystrophy", "type": "BiologicFunction"}, {"text": "DMD", "type": "BiologicFunction"}, {"text": "adverse effects", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The results showed that the efficacy of reducing TC , LDL , ALT , 2hPG , and HbA1c in NAFLD patients of the berberine group were significantly higher than that of control group .

Example answer:
{"entities": [{"text": "TC", "type": "Chemical"}, {"text": "LDL", "type": "Chemical"}, {"text": "ALT", "type": "Chemical"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "NAFLD", "type": "BiologicFunction"}, {"text": "berberine", "type": "Chemical"}, {"text": "group", "type": "PopulationGroup"}]}

Example input:
Sentence: Dietary management and arginine supplementation , if initiated early , may ameliorate symptoms .Because of the nonspecific nature of the symptoms and the possibility for therapeutic management , ASL deficiency is part of the recommended uniform screening panel for newborn screening in the USA .

Example answer:
{"entities": [{"text": "Dietary management", "type": "HealthCareActivity"}, {"text": "arginine", "type": "Chemical"}, {"text": "supplementation", "type": "HealthCareActivity"}, {"text": "symptoms", "type": "Finding"}, {"text": "ASL deficiency", "type": "BiologicFunction"}, {"text": "newborn screening", "type": "HealthCareActivity"}, {"text": "USA", "type": "SpatialConcept"}]}

Example input:
Sentence: N - Nitro - L - arginine methyl ester abrogated relaxation responses , and the Ednra / Ednrb mRNA ratio was decreased in eET - 1 / smPparγ , which could indicate that nitric oxide production was enhanced by ET - 1 stimulation of endothelin type B receptors .

Example answer:
{"entities": [{"text": "N - Nitro - L - arginine methyl ester", "type": "Chemical"}, {"text": "Ednra", "type": "AnatomicalStructure"}, {"text": "Ednrb", "type": "AnatomicalStructure"}, {"text": "mRNA", "type": "Chemical"}, {"text": "eET - 1", "type": "Chemical"}, {"text": "smPparγ", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "ET - 1", "type": "Chemical"}, {"text": "endothelin type B receptors", "type": "Chemical"}]}

Example input:
Sentence: Additionally , decreased expression of Drp1 via siRNA knockdown during LG conditions also improved vascular relaxation .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "Drp1", "type": "Chemical"}, {"text": "siRNA", "type": "Chemical"}, {"text": "knockdown", "type": "ResearchActivity"}, {"text": "LG", "type": "Chemical"}, {"text": "improved", "type": "Finding"}, {"text": "vascular relaxation", "type": "BiologicFunction"}]}

Example input:
Sentence: In conclusion , our study showed that an ONS with arginine loading could decrease oxidative stress and increase antioxidant capacity in healthy volunteers .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "ONS", "type": "Food"}, {"text": "arginine", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "healthy volunteers", "type": "PopulationGroup"}]}

Example input:
Sentence: l - Arginine Enhances Resistance against Oxidative Stress and Heat Stress in Caenorhabditis elegans The antioxidant properties of l - arginine ( l - Arg ) in vivo , and its effect on enhancing resistance to oxidative stress and heat stress in Caenorhabditis elegans were investigated .

Example answer:
{"entities": [{"text": "l - Arginine", "type": "Chemical"}, {"text": "Oxidative Stress", "type": "BiologicFunction"}, {"text": "Heat Stress", "type": "BiologicFunction"}, {"text": "Caenorhabditis elegans", "type": "Eukaryote"}, {"text": "antioxidant", "type": "Chemical"}, {"text": "l - arginine", "type": "Chemical"}, {"text": "l - Arg", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "heat stress", "type": "BiologicFunction"}]}

Example input:
Sentence: The Effect of l - Arginine on Dural Healing After Experimentally Induced Dural Defect in a Rat Model Incomplete repair of the dura mater may result in numerous complications such as cerebrospinal fluid leakage and meningitis .

Example answer:
{"entities": [{"text": "l - Arginine", "type": "Chemical"}, {"text": "Dural Healing", "type": "BiologicFunction"}, {"text": "Dural", "type": "AnatomicalStructure"}, {"text": "Rat", "type": "Eukaryote"}, {"text": "repair", "type": "BiologicFunction"}, {"text": "dura mater", "type": "AnatomicalStructure"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "cerebrospinal fluid leakage", "type": "BiologicFunction"}, {"text": "meningitis", "type": "BiologicFunction"}]}

Example input:
Sentence: The systemic supplementation of l - arginine may accelerate dural healing by increasing the level of granulation tissue formation , collagen deposition , and vascularization .

Example answer:
{"entities": [{"text": "l - arginine", "type": "Chemical"}, {"text": "dural healing", "type": "BiologicFunction"}, {"text": "granulation tissue", "type": "AnatomicalStructure"}, {"text": "collagen", "type": "Chemical"}]}

Input:
Sentence: The systematic supplementation of l - arginine showed a significant effect in dural healing compared with the control group .

## Item MedMentions:test:1777
Example input:
Sentence: We developed a simple multiplex PCR assay capable of screening Staphylococcus isolates for the presence of antiseptic resistance genes for chlorhexidine and quaternary ammonium compounds , as well as mupirocin - and methicillin - resistance genes , while simultaneously discriminating S .

Example answer:
{"entities": [{"text": "PCR", "type": "ResearchActivity"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "Staphylococcus", "type": "Bacterium"}, {"text": "isolates", "type": "Chemical"}, {"text": "presence", "type": "Finding"}, {"text": "antiseptic", "type": "Chemical"}, {"text": "chlorhexidine", "type": "Chemical"}, {"text": "quaternary ammonium compounds", "type": "Chemical"}, {"text": "mupirocin", "type": "Chemical"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: Total Fluorescence Fingerprinting of Pesticides : A Reliable Approach for Continuous Monitoring of Soils and Waters The present work relates to the creation / extension of a database of Total Excitation - Emission and Total Synchronous Fluorescence Matrices ( TEEMs and TSFMs ) along with optimal Synchronous Fluorescence Spectra ( SFS ) to fingerprint pesticides widely used in Morocco .

Example answer:
{"entities": [{"text": "Pesticides", "type": "Chemical"}, {"text": "database", "type": "IntellectualProduct"}, {"text": "Total Excitation - Emission and Total Synchronous Fluorescence Matrices", "type": "HealthCareActivity"}, {"text": "TEEMs and TSFMs", "type": "HealthCareActivity"}, {"text": "optimal Synchronous Fluorescence Spectra", "type": "HealthCareActivity"}, {"text": "SFS", "type": "HealthCareActivity"}, {"text": "pesticides", "type": "Chemical"}, {"text": "Morocco", "type": "SpatialConcept"}]}

Example input:
Sentence: In this work , we report an entropy - driven reaction for amplification assay miRNA with a detection limit of 0 . 27 pM .

Example answer:
{"entities": [{"text": "amplification", "type": "ResearchActivity"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "miRNA", "type": "Chemical"}]}

Example input:
Sentence: Detection assays for toxin genes tpeL and netB were also performed .

Example answer:
{"entities": [{"text": "Detection", "type": "HealthCareActivity"}, {"text": "assays", "type": "HealthCareActivity"}, {"text": "tpeL", "type": "AnatomicalStructure"}, {"text": "netB", "type": "AnatomicalStructure"}]}

Example input:
Sentence: typhi , 27 .

Example answer:
{"entities": [{"text": "typhi", "type": "Bacterium"}]}

Example input:
Sentence: Typhi and GBC .

Example answer:
{"entities": [{"text": "Typhi", "type": "Bacterium"}, {"text": "GBC", "type": "BiologicFunction"}]}

Example input:
Sentence: The pooled estimates of sensitivity and specificity of visual inspection with acetic acid ( VIA ) , magnified VIA , visual inspection with Lugol 's iodine ( VILI ) , cytology ( Pap smear ) , and human papillomavirus DNA were found to be 67 . 65 % and 84 .

Example answer:
{"entities": [{"text": "visual inspection with acetic acid", "type": "HealthCareActivity"}, {"text": "VIA", "type": "HealthCareActivity"}, {"text": "magnified VIA", "type": "HealthCareActivity"}, {"text": "visual inspection with Lugol 's iodine", "type": "HealthCareActivity"}, {"text": "VILI", "type": "HealthCareActivity"}, {"text": "cytology", "type": "HealthCareActivity"}, {"text": "Pap smear", "type": "HealthCareActivity"}, {"text": "human papillomavirus DNA", "type": "HealthCareActivity"}]}

Example input:
Sentence: cholerae : these methods include swarm assay , temporal stimulation assay , capillary assay , and receptor methylation assay .

Example answer:
{"entities": [{"text": "cholerae", "type": "Bacterium"}, {"text": "swarm assay", "type": "HealthCareActivity"}, {"text": "temporal stimulation assay", "type": "HealthCareActivity"}, {"text": "capillary assay", "type": "HealthCareActivity"}, {"text": "receptor methylation assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: The assay is based on Taylor dispersion analysis ( TDA ) and is fully automated with the use of standard capillary electrophoresis ( CE ) based equipment employing fluorescence detection .

Example answer:
{"entities": [{"text": "assay", "type": "HealthCareActivity"}, {"text": "Taylor dispersion analysis", "type": "HealthCareActivity"}, {"text": "TDA", "type": "ResearchActivity"}, {"text": "capillary electrophoresis", "type": "HealthCareActivity"}, {"text": "CE", "type": "HealthCareActivity"}, {"text": "detection", "type": "HealthCareActivity"}]}

Example input:
Sentence: Typhi Vi antibodies and performed culture and quantitative polymerase chain reaction for the subset with bile , gallstone , tissue , and stool samples available .

Example answer:
{"entities": [{"text": "Typhi Vi antibodies", "type": "Chemical"}, {"text": "quantitative polymerase chain reaction", "type": "ResearchActivity"}, {"text": "bile", "type": "BodySubstance"}, {"text": "gallstone", "type": "BodySubstance"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "stool samples", "type": "BodySubstance"}]}

Input:
Sentence: Typhi detection assay )

## Item MedMentions:test:1709
Example input:
Sentence: Here , the authors show that in layer 2 / 3 ( L2 / 3 ) of the somatosensory cortex ( S1 ) , acute RA induces increases in spontaneous but not action - potential evoked transmission , and that this requires retinoic acid receptor ( RARα ) both in presynaptic PV -positive interneurons and postsynaptic pyramidal ( PN ) neurons .

Example answer:
{"entities": [{"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "layer 2 / 3", "type": "AnatomicalStructure"}, {"text": "L2 / 3", "type": "AnatomicalStructure"}, {"text": "somatosensory cortex", "type": "AnatomicalStructure"}, {"text": "S1", "type": "AnatomicalStructure"}, {"text": "RA", "type": "Chemical"}, {"text": "action - potential", "type": "BiologicFunction"}, {"text": "transmission", "type": "BiologicFunction"}, {"text": "retinoic acid receptor", "type": "Chemical"}, {"text": "RARα", "type": "Chemical"}, {"text": "presynaptic", "type": "AnatomicalStructure"}, {"text": "PV", "type": "Chemical"}, {"text": "interneurons", "type": "AnatomicalStructure"}, {"text": "pyramidal ( PN ) neurons", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A lack of Ick in the developing inner ear resulted in PCP defects in the cochlea , including misorientation or misshaping of stereocilia and aberrant localization of the kinocilium and basal body in the apical and middle turns , leading to auditory dysfunction .

Example answer:
{"entities": [{"text": "Ick", "type": "Chemical"}, {"text": "inner ear", "type": "AnatomicalStructure"}, {"text": "PCP", "type": "SpatialConcept"}, {"text": "cochlea", "type": "AnatomicalStructure"}, {"text": "stereocilia", "type": "AnatomicalStructure"}, {"text": "kinocilium", "type": "AnatomicalStructure"}, {"text": "basal body", "type": "AnatomicalStructure"}, {"text": "apical", "type": "SpatialConcept"}, {"text": "middle", "type": "SpatialConcept"}]}

Example input:
Sentence: Compared to baseline and control ( SCM ) stimulation , nVNS significantly activated primary vagal projections including : nucleus of the solitary tract ( primary central relay of vagal afferents ) , parabrachial area , primary sensory cortex , and insula .

Example answer:
{"entities": [{"text": "( SCM ) stimulation", "type": "Finding"}, {"text": "nVNS", "type": "HealthCareActivity"}, {"text": "primary vagal", "type": "AnatomicalStructure"}, {"text": "projections", "type": "SpatialConcept"}, {"text": "nucleus of the solitary tract", "type": "AnatomicalStructure"}, {"text": "vagal afferents", "type": "AnatomicalStructure"}, {"text": "parabrachial area", "type": "AnatomicalStructure"}, {"text": "primary sensory cortex", "type": "AnatomicalStructure"}, {"text": "insula", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In this study , we recorded single - unit activity from primary auditory cortex of awake marmoset monkeys while delivering wide - band random - spectrum stimuli and white Gaussian noise ( WGN ) to examine any divergences in stimulus encoding properties across SFR classes .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "primary auditory cortex", "type": "SpatialConcept"}, {"text": "marmoset", "type": "Eukaryote"}, {"text": "monkeys", "type": "Eukaryote"}, {"text": "white Gaussian noise", "type": "IntellectualProduct"}, {"text": "WGN", "type": "IntellectualProduct"}, {"text": "divergences", "type": "SpatialConcept"}]}

Example input:
Sentence: Testing across a range of conditions and pulse durations , we found that mesoaccumbal and nigrostriatal neurons differ substantially in rebound properties with mesoaccumbal neurons displaying significantly longer delays to spiking following hyperpolarization .

Example answer:
{"entities": [{"text": "pulse", "type": "ClinicalAttribute"}, {"text": "mesoaccumbal", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "mesoaccumbal neurons", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Brain activation following tendon vibration at 100Hz ( ' illusion ' ) and 30Hz ( ' no illusion ' ) were analysed using the two - stage random effects model , with or without white and grey matter covariates .

Example answer:
{"entities": [{"text": "Brain", "type": "AnatomicalStructure"}, {"text": "tendon", "type": "AnatomicalStructure"}, {"text": "vibration", "type": "HealthCareActivity"}, {"text": "' illusion '", "type": "BiologicFunction"}, {"text": "no", "type": "Finding"}, {"text": "illusion", "type": "BiologicFunction"}, {"text": "analysed", "type": "ResearchActivity"}, {"text": "white", "type": "AnatomicalStructure"}, {"text": "grey matter", "type": "AnatomicalStructure"}]}

Example input:
Sentence: These results suggest that communication problems in these listeners cannot be explained by compromised sensory representations in the auditory periphery , but rather point to lingering blast - induced damage to cortical networks implicated in the control of attention .

Example answer:
{"entities": [{"text": "communication problems", "type": "Finding"}, {"text": "listeners", "type": "PopulationGroup"}, {"text": "sensory representations", "type": "BiologicFunction"}, {"text": "auditory periphery", "type": "BodySystem"}, {"text": "blast - induced damage", "type": "InjuryOrPoisoning"}, {"text": "cortical networks", "type": "AnatomicalStructure"}, {"text": "attention", "type": "BiologicFunction"}]}

Example input:
Sentence: Additionally , altered SFRs are a correlate of tinnitus , arising in several auditory areas after exposure to ototoxic substances and noise trauma .

Example answer:
{"entities": [{"text": "tinnitus", "type": "Finding"}, {"text": "auditory areas", "type": "AnatomicalStructure"}, {"text": "trauma", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Previous studies in the auditory system have demonstrated that different levels of spontaneous activity are correlated with a variety of physiological and anatomic properties , suggesting that neurons with differing SFRs make unique contributions to the encoding of auditory stimuli .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "auditory system", "type": "BodySystem"}, {"text": "spontaneous activity", "type": "BiologicFunction"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "auditory stimuli", "type": "BiologicFunction"}]}

Example input:
Sentence: Spontaneous activity is correlated with coding density in primary auditory cortex Sensory neurons across sensory modalities and specific processing areas have diverse levels of spontaneous firing rates ( SFRs ) in the absence of sensory stimuli .

Example answer:
{"entities": [{"text": "Spontaneous activity", "type": "BiologicFunction"}, {"text": "primary auditory cortex", "type": "SpatialConcept"}, {"text": "Sensory neurons", "type": "AnatomicalStructure"}]}

Input:
Sentence: These findings are consistent with a novel view of the role spontaneous spiking may play during normal stimulus processing in primary auditory cortex and how it may malfunction in cases of tinnitus .

## Item MedMentions:test:1616
Example input:
Sentence: The plaque area and serum pro - inflammatory cytokine ( IL - 1β , IL - 6 , TNF - α and IL - 17A ) levels in Lv - shSiglec - 1 mice were significantly lower than Lv - shNC mice , whereas IL - 10 was higher .

Example answer:
{"entities": [{"text": "plaque", "type": "Finding"}, {"text": "area", "type": "SpatialConcept"}, {"text": "serum", "type": "BodySubstance"}, {"text": "pro - inflammatory cytokine", "type": "Chemical"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "IL - 17A", "type": "Chemical"}, {"text": "Lv - shSiglec - 1", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "Lv - shNC", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , these data suggested that ( i ) patients from Group I had recent lesions ( in the beginning of chronic phase ) compared to those from Group II and ( ii ) the modulation of inflammatory response in patients with recent American cutaneous leishmaniasis was correlated with IL - 10 expression in skin lesions preventing the development of mucosal forms .

Example answer:
{"entities": [{"text": "Group I", "type": "PopulationGroup"}, {"text": "recent lesions", "type": "InjuryOrPoisoning"}, {"text": "Group II", "type": "PopulationGroup"}, {"text": "inflammatory response", "type": "BiologicFunction"}, {"text": "American cutaneous leishmaniasis", "type": "BiologicFunction"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "skin lesions", "type": "BiologicFunction"}, {"text": "development", "type": "BiologicFunction"}, {"text": "mucosal forms", "type": "Finding"}]}

Example input:
Sentence: On the contrary , IL - 10 expression was significantly down - regulated in all immunized groups of progressor chickens at 14 dpc .

Example answer:
{"entities": [{"text": "IL - 10", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "down - regulated", "type": "BiologicFunction"}, {"text": "immunized groups of progressor chickens", "type": "Eukaryote"}]}

Example input:
Sentence: Multiple linear regression showed that genotypes and TC were independent factors affecting the levels of IL - 2 and IL - 10 ( P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "TC", "type": "Chemical"}, {"text": "levels of IL - 2", "type": "HealthCareActivity"}, {"text": "IL - 10", "type": "HealthCareActivity"}]}

Example input:
Sentence: ELISA analysis of cultured sorted Treg cells indicated that secretion of immunosuppressive cytokines ( interleukin - 10 , TGF - β ) was significantly lower in Treg cells from GSPs - fed mice .

Example answer:
{"entities": [{"text": "ELISA", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "Treg cells", "type": "AnatomicalStructure"}, {"text": "indicated", "type": "Finding"}, {"text": "secretion", "type": "BiologicFunction"}, {"text": "immunosuppressive", "type": "BiologicFunction"}, {"text": "cytokines", "type": "Chemical"}, {"text": "interleukin - 10", "type": "Chemical"}, {"text": "TGF - β", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: The comparison of cytokine expression / group showed that IL - 10 was significantly higher than IL - 17 and IFN - γ ( similar data were shown in IL - 17 compared with TNF - α ) , suggesting an immunological balance between inflammatory - anti - inflammatory agents .

Example answer:
{"entities": [{"text": "cytokine", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "IL - 17", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "balance", "type": "BiologicFunction"}, {"text": "anti - inflammatory agents", "type": "Chemical"}]}

Example input:
Sentence: DNG , NETA , and MPA suppressed the secretion of interleukin ( IL ) - 6 , IL - 8 , and monocyte chemotactic protein ( MCP ) - 1 from ESC .

Example answer:
{"entities": [{"text": "DNG", "type": "Chemical"}, {"text": "NETA", "type": "Chemical"}, {"text": "MPA", "type": "Chemical"}, {"text": "secretion of interleukin", "type": "BiologicFunction"}, {"text": "( IL ) - 6", "type": "Chemical"}, {"text": "IL - 8", "type": "Chemical"}, {"text": "monocyte chemotactic protein ( MCP ) - 1", "type": "Chemical"}, {"text": "ESC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Compared with the healthy controls , level of IL - 2 increased significantly , while IL - 10 decreased significantly ( P < 0 .

Example answer:
{"entities": [{"text": "IL - 2", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}]}

Example input:
Sentence: The findings showed a decrease in the expression level of IL - 10 in the TLP group ( p = 0 . 004 ) .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "IL - 10", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Moreover , the IL - 10 gene expression level weeas upregulated in the group of the ESP from cell culture medium ( p = 0 . 04 ) and the active tachyzoite group ( p = 0 . 04 ) .

Example answer:
{"entities": [{"text": "IL - 10", "type": "AnatomicalStructure"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "ESP", "type": "Chemical"}, {"text": "tachyzoite", "type": "Eukaryote"}]}

Input:
Sentence: The expression of IL - 10 gene in the group of ESP from cell - free medium was not significant compared to the control one ( p = 0 . 45 ) .

## Item MedMentions:test:1725
Example input:
Sentence: The biphasic character of these BJPNFs , which was controlled via the rotational speed of fabrication , was confirmed at the individual nanofiber scale using energy dispersive X - ray spectroscopy , and at the bulk , macro - scale using attenuated total reflectance - Fourier transform infrared spectroscopy .

Example answer:
{"entities": [{"text": "BJPNFs", "type": "Chemical"}, {"text": "energy dispersive X - ray spectroscopy", "type": "HealthCareActivity"}, {"text": "macro - scale", "type": "IntellectualProduct"}, {"text": "reflectance", "type": "HealthCareActivity"}, {"text": "Fourier transform infrared spectroscopy", "type": "ResearchActivity"}]}

Example input:
Sentence: Here , using dual - color direct stochastic optical reconstruction microscopy , we report that Fcγ receptor I ( FcγRI ) , FcγRII , and SIRPα are not homogeneously distributed at macrophage surfaces but are organized in discrete nanoclusters , with a mean radius of 71 ± 11 nm , 60 ± 6 nm , and 48 ± 3 nm , respectively .

Example answer:
{"entities": [{"text": "dual - color direct stochastic optical reconstruction microscopy", "type": "HealthCareActivity"}, {"text": "Fcγ receptor I", "type": "Chemical"}, {"text": "FcγRI", "type": "Chemical"}, {"text": "FcγRII", "type": "Chemical"}, {"text": "SIRPα", "type": "Chemical"}, {"text": "macrophage", "type": "AnatomicalStructure"}, {"text": "surfaces", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Specimens were subjected to a compressive load until fracture at a crosshead speed of 0 . 5 mm / min .

Example answer:
{"entities": [{"text": "fracture", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Nanomechanical experiments on cylindrical samples , with diameters between 250 nm and 3 , 000 nm , of the bone 's ordered and disordered phases revealed a transition from plastic deformation to brittle failure and at least a factor - of - 2 higher strength in the smaller samples .

Example answer:
{"entities": [{"text": "Nanomechanical experiments", "type": "ResearchActivity"}, {"text": "cylindrical", "type": "SpatialConcept"}, {"text": "bone 's", "type": "AnatomicalStructure"}, {"text": "deformation", "type": "Finding"}, {"text": "brittle", "type": "Finding"}, {"text": "failure", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Here , we report a novel real - time ultrasound time - of - flight instrument that is capable of monitoring and imaging the critical step in formalin fixation , diffusion of the fixative into tissue , which provides a quantifiable quality metric for tissue fixation in the clinical laboratory ensuring consistent downstream molecular assay results .

Example answer:
{"entities": [{"text": "real - time ultrasound time - of - flight instrument", "type": "MedicalDevice"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "imaging", "type": "HealthCareActivity"}, {"text": "formalin fixation", "type": "HealthCareActivity"}, {"text": "fixative", "type": "Chemical"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "metric", "type": "Chemical"}, {"text": "tissue fixation", "type": "HealthCareActivity"}, {"text": "clinical laboratory", "type": "Organization"}, {"text": "molecular assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: This method can estimate localized T2 relaxation times from multiple voxels using conventional hyperpolarized ( 13 ) C CSI and can potentially be used with time resolved fast CSI .

Example answer:
{"entities": [{"text": "method", "type": "IntellectualProduct"}, {"text": "localized", "type": "SpatialConcept"}, {"text": "hyperpolarized ( 13 ) C CSI", "type": "HealthCareActivity"}, {"text": "time resolved fast CSI", "type": "HealthCareActivity"}]}

Example input:
Sentence: We report single - shot ultrafast video recording of a light - induced photonic Mach cone propagating in an engineered scattering plate assembly .

Example answer:
{"entities": []}

Example input:
Sentence: Single - shot real - time video recording of a photonic Mach cone induced by a scattered light pulse Ultrafast video recording of spatiotemporal light distribution in a scattering medium has a significant impact in biomedicine .

Example answer:
{"entities": [{"text": "scattered", "type": "SpatialConcept"}, {"text": "spatiotemporal", "type": "ResearchActivity"}, {"text": "biomedicine", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: This dynamic light - scattering event was captured in a single camera exposure by lossless - encoding compressed ultrafast photography at 100 billion frames per second .

Example answer:
{"entities": [{"text": "dynamic light - scattering", "type": "HealthCareActivity"}, {"text": "single camera", "type": "MedicalDevice"}]}

Example input:
Sentence: The radial acceleration of the interface at the antinodes can be up to 10 ( 5 ) - 10 ( 6 ) ms ( - 2 ) , hence there is a contribution from the inertia of the particles localised at the antinodes .

Example answer:
{"entities": [{"text": "inertia", "type": "Finding"}, {"text": "particles", "type": "Chemical"}]}

Input:
Sentence: We perform high - speed visualisation of the interface shape and of the particle distribution during ultrafast deformation at a rate of up to 10 ( 4 ) s ( - 1 ) .

## Item MedMentions:test:1862
Example input:
Sentence: The key benefit of the pdf article intervention was raising doctors ' reflection on limitations in their communication skills , whereas e - learning was more effective in changing their perception of older patients ' proactive attitude , especially among GPs working in privately owned facilities and having a greater number of assigned patients .

Example answer:
{"entities": [{"text": "pdf article", "type": "IntellectualProduct"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "doctors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "older", "type": "PopulationGroup"}, {"text": "GPs", "type": "ProfessionalOrOccupationalGroup"}, {"text": "privately owned facilities", "type": "Organization"}]}

Example input:
Sentence: ( This article is a translation of J Jpn Coll Angiol 2015 ; 55 : 105 - 110 ) .

Example answer:
{"entities": []}

Example input:
Sentence: © 2016 by John Wiley & Sons , Inc . Journal Article 2016 - 08 - 18 00 : 00 : 00

Example answer:
{"entities": []}

Example input:
Sentence: Four articles meeting the inclusion criteria were included in the review .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}]}

Example input:
Sentence: 1084This article is highlighted in the In This Issue feature , p .

Example answer:
{"entities": []}

Example input:
Sentence: Yet , making this determination - the main objective of this article - is critical in determining the adequacy of protection available to human research subjects in the country .

Example answer:
{"entities": [{"text": "objective", "type": "IntellectualProduct"}, {"text": "article", "type": "IntellectualProduct"}, {"text": "human", "type": "Eukaryote"}, {"text": "research subjects", "type": "PopulationGroup"}, {"text": "country", "type": "SpatialConcept"}]}

Example input:
Sentence: The work cannot be changed in any way or used commercially without permission from the journal .

Example answer:
{"entities": []}

Example input:
Sentence: This article is a US government work and , as such , is in the public domain in the United States of America .

Example answer:
{"entities": []}

Example input:
Sentence: This is an open access article distributed under the terms of the Creative Commons Non - Commercial , No Derivatives ( CC BY - NC - ND ) licence .

Example answer:
{"entities": []}

Example input:
Sentence: This is an open access article distributed under the terms of the Creative Commons Non - Commercial , No Derivatives ( CC BY - NC - ND ) licence .

Example answer:
{"entities": []}

Input:
Sentence: This article is protected by copyright .

## Item MedMentions:test:1057
Example input:
Sentence: However , the expression of RBBP6 in cancer and its interaction with p53 are yet to be understood in order to determine whether or not RBBP6 is cancer promoting and therefore a potential biomarker .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "p53", "type": "AnatomicalStructure"}, {"text": "cancer promoting", "type": "AnatomicalStructure"}, {"text": "biomarker", "type": "ClinicalAttribute"}]}

Example input:
Sentence: We followed on with silencing the overexpression of RBBP6 and treatment with anticancer agents to evaluate how the specimens respond to combinational therapy .

Example answer:
{"entities": [{"text": "silencing", "type": "BiologicFunction"}, {"text": "overexpression", "type": "BiologicFunction"}, {"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "anticancer agents", "type": "Chemical"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Overexpression of RBBP6 seems to promote S - phase in cell cycle and cell proliferation .

Example answer:
{"entities": [{"text": "Overexpression", "type": "BiologicFunction"}, {"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "cell cycle", "type": "BiologicFunction"}, {"text": "cell proliferation", "type": "BiologicFunction"}]}

Example input:
Sentence: This is especially important because RBBP6 associates with the tumor suppressor gene p53 , the inactivation of which has been linked to over 50 % of all cancer types .

Example answer:
{"entities": [{"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "tumor suppressor gene p53", "type": "AnatomicalStructure"}, {"text": "cancer types", "type": "BiologicFunction"}]}

Example input:
Sentence: Silencing RBBP6 followed by treatment with γ - aminobutyric acid and camptothecin seems to sensitize cells to apoptosis induction rather than cell cycle arrest .

Example answer:
{"entities": [{"text": "Silencing", "type": "BiologicFunction"}, {"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "γ - aminobutyric acid", "type": "Chemical"}, {"text": "camptothecin", "type": "Chemical"}, {"text": "sensitize cells", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "induction", "type": "BiologicFunction"}, {"text": "cell cycle arrest", "type": "BiologicFunction"}]}

Example input:
Sentence: These results predict a proliferative role of RBBP6 in cancer progression rather than as a cancer - causing gene .

Example answer:
{"entities": [{"text": "results", "type": "Finding"}, {"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "cancer progression", "type": "BiologicFunction"}, {"text": "cancer - causing gene", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We began by staining human cervical cancer tissue sections with anti - RBBP6 monoclonal antibody to evaluate the extent of expression of RBBP6 in patients ' specimens .

Example answer:
{"entities": [{"text": "staining", "type": "HealthCareActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "monoclonal antibody", "type": "Chemical"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "RBBP6", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Furthermore , sensitization of cells to camptothecin - induced apoptosis by RBBP6 targeting suggests a promising tool for halting cervical cancer progression .

Example answer:
{"entities": [{"text": "sensitization", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "camptothecin", "type": "Chemical"}, {"text": "induced", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "targeting", "type": "ResearchActivity"}, {"text": "cervical cancer progression", "type": "BiologicFunction"}]}

Example input:
Sentence: RBBP6 was highly expressed in cervical cancer tissue sections that were in stage II or III of development .

Example answer:
{"entities": [{"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "stage II", "type": "IntellectualProduct"}, {"text": "III of development", "type": "IntellectualProduct"}]}

Example input:
Sentence: In this study , we manipulated RBBP6 expression levels followed by treatment with either camptothecin or γ - aminobutyric acid in cervical cancer cells to induce apoptosis or cell cycle arrest .

Example answer:
{"entities": [{"text": "study", "type": "HealthCareActivity"}, {"text": "manipulated", "type": "HealthCareActivity"}, {"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "camptothecin", "type": "Chemical"}, {"text": "γ - aminobutyric acid", "type": "Chemical"}, {"text": "induce", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "cell cycle arrest", "type": "BiologicFunction"}]}

Input:
Sentence: RBBP6 : a potential biomarker of apoptosis induction in human cervical cancer cell lines Overexpression of RBBP6 in cancers of the colon , lung , and esophagus makes it a potential target in anticancer therapy .

## Item MedMentions:test:1630
Example input:
Sentence: salmonicida based on phylogenetic analysis of vapA and 16S rRNA gene sequences .

Example answer:
{"entities": [{"text": "salmonicida", "type": "Bacterium"}, {"text": "phylogenetic analysis", "type": "ResearchActivity"}, {"text": "vapA", "type": "AnatomicalStructure"}, {"text": "16S rRNA", "type": "Chemical"}, {"text": "gene sequences", "type": "SpatialConcept"}]}

Example input:
Sentence: Metagenomic recovery of phage genomes of uncultured freshwater actinobacteria Low - GC Actinobacteria are among the most abundant and widespread microbes in freshwaters and have largely resisted all cultivation efforts .

Example answer:
{"entities": [{"text": "phage", "type": "Virus"}, {"text": "genomes", "type": "AnatomicalStructure"}, {"text": "actinobacteria", "type": "Bacterium"}, {"text": "Actinobacteria", "type": "Bacterium"}, {"text": "widespread", "type": "SpatialConcept"}, {"text": "cultivation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here , we report , for the first time in India , the complete genome sequence of BGE14 / ABT1 / MVC / India , a reassortment strain with segments A and B derived from a very virulent IBDV strain and an attenuated IBDV , respectively .

Example answer:
{"entities": [{"text": "India", "type": "SpatialConcept"}, {"text": "genome sequence", "type": "AnatomicalStructure"}, {"text": "BGE14 / ABT1 / MVC / India", "type": "Virus"}, {"text": "segments A and B", "type": "AnatomicalStructure"}, {"text": "IBDV", "type": "Virus"}]}

Example input:
Sentence: Phylogenetic analyses based on 16S rRNA gene sequences indicated that strain SYP - A7299 T belongs to the genus Arthrobacter and is most closely related to Arthrobacter halodurans JSM 078085 T ( 97 . 4 % 16S rRNA gene sequence similarity ) .

Example answer:
{"entities": [{"text": "Phylogenetic analyses", "type": "ResearchActivity"}, {"text": "16S rRNA gene sequences", "type": "AnatomicalStructure"}, {"text": "strain SYP - A7299 T", "type": "Bacterium"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Arthrobacter", "type": "Bacterium"}, {"text": "Arthrobacter halodurans JSM 078085 T", "type": "Bacterium"}, {"text": "16S rRNA gene sequence", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Draft Genome Sequence of MPKL 26 , the Type Strain of the Novel Species Sinomonas mesophila Sinomonas mesophila MPKL 26 ( T ) can produce silver nanoparticles .

Example answer:
{"entities": [{"text": "Draft Genome Sequence", "type": "SpatialConcept"}, {"text": "Novel Species", "type": "IntellectualProduct"}, {"text": "Sinomonas mesophila", "type": "Bacterium"}]}

Example input:
Sentence: Draft Genome Sequence of Bacillus cereus LA2007 , a Human - Pathogenic Isolate Harboring Anthrax -Like Plasmids We present the genome sequence of Bacillus cereus LA2007 , a strain isolated in 2007 from a fatal pneumonia case in Louisiana .

Example answer:
{"entities": [{"text": "Draft Genome Sequence", "type": "SpatialConcept"}, {"text": "Bacillus cereus LA2007", "type": "Bacterium"}, {"text": "Human - Pathogenic Isolate", "type": "Chemical"}, {"text": "Anthrax -Like Plasmids", "type": "Chemical"}, {"text": "genome sequence", "type": "SpatialConcept"}, {"text": "fatal pneumonia", "type": "BiologicFunction"}, {"text": "case", "type": "IntellectualProduct"}, {"text": "Louisiana", "type": "SpatialConcept"}]}

Example input:
Sentence: First complete genome sequence of a virulent bacteriophage infecting the opportunistic pathogen Serratia rubidaea A Serratia rubidaea phage , vB _ Sru IME250 , was isolated from hospital sewage .

Example answer:
{"entities": [{"text": "genome sequence", "type": "SpatialConcept"}, {"text": "bacteriophage", "type": "Virus"}, {"text": "infecting", "type": "Finding"}, {"text": "Serratia rubidaea", "type": "Bacterium"}, {"text": "Serratia rubidaea phage , vB _ Sru IME250", "type": "Virus"}, {"text": "hospital", "type": "Organization"}]}

Example input:
Sentence: The Crystal Structure of the C - Terminal Domain of the Salmonella enterica PduO Protein : An Old Fold with a New Heme - Binding Mode The two - domain protein PduO , involved in 1 , 2 - propanediol utilization in the pathogenic Gram - negative bacterium Salmonella enterica is an ATP : Cob ( I ) alamin adenosyltransferase , but this is a function of the N - terminal domain alone .

Example answer:
{"entities": [{"text": "Crystal Structure", "type": "Chemical"}, {"text": "C - Terminal Domain", "type": "SpatialConcept"}, {"text": "Salmonella enterica", "type": "Bacterium"}, {"text": "PduO Protein", "type": "Chemical"}, {"text": "Heme - Binding", "type": "BiologicFunction"}, {"text": "two - domain protein PduO", "type": "Chemical"}, {"text": "1 , 2 - propanediol", "type": "Chemical"}, {"text": "Gram - negative bacterium", "type": "Bacterium"}, {"text": "ATP", "type": "Chemical"}, {"text": "Cob ( I ) alamin adenosyltransferase", "type": "Chemical"}, {"text": "function", "type": "BiologicFunction"}, {"text": "N - terminal domain", "type": "SpatialConcept"}]}

Example input:
Sentence: enterica serovar Orion strain CRJJGF _ 00093 , isolated from a dog in 2005 .

Example answer:
{"entities": [{"text": "enterica serovar Orion strain CRJJGF _ 00093", "type": "Bacterium"}, {"text": "dog", "type": "Eukaryote"}]}

Example input:
Sentence: Draft Genome Sequence of Salmonella enterica subsp .

Example answer:
{"entities": [{"text": "Draft Genome Sequence", "type": "SpatialConcept"}, {"text": "Salmonella enterica subsp .", "type": "Bacterium"}]}

Input:
Sentence: enterica Serovar Orion Strain CRJJGF _ 00093 ( Phylum Gammaproteobacteria ) Here , we report a 4 . 70 - Mbp draft genome sequence of Salmonella enterica subsp .

## Item MedMentions:test:1726
Example input:
Sentence: A prospective observational study was performed at the University Medical Center Groningen .

Example answer:
{"entities": [{"text": "prospective observational study", "type": "ResearchActivity"}, {"text": "University Medical Center", "type": "Organization"}, {"text": "Groningen", "type": "SpatialConcept"}]}

Example input:
Sentence: This study aimed to identify current practices and processes used in the RTW of injured nurses , and determine if these are consistent with the seven principles for successful RTW as described by the Canadian Institute for Work & Health .

Example answer:
{"entities": [{"text": "RTW", "type": "Finding"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Contrary to popular practice which favors a staged protocol in many high - energy fracture patterns , we have used early single - stage open reduction and internal fixation ( ORIF ) to treat these injuries whenever possible .

Example answer:
{"entities": [{"text": "high - energy fracture", "type": "InjuryOrPoisoning"}, {"text": "open reduction and internal fixation", "type": "HealthCareActivity"}, {"text": "ORIF", "type": "HealthCareActivity"}, {"text": "injuries", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Following approval by our institutional review board , our study design consisted of a retrospective cohort analysis of 413 patients at Staten Island University Hospital , a 700 - bed tertiary referral center between 2008 and 2013 who underwent an initial great toe ( hallux ) amputation .

Example answer:
{"entities": [{"text": "institutional review board", "type": "ProfessionalOrOccupationalGroup"}, {"text": "study design", "type": "ResearchActivity"}, {"text": "retrospective cohort analysis", "type": "ResearchActivity"}, {"text": "Staten Island University Hospital", "type": "Organization"}, {"text": "700 - bed tertiary referral center", "type": "Organization"}, {"text": "great toe ( hallux ) amputation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Large , academic , tertiary care hospital .

Example answer:
{"entities": [{"text": "academic", "type": "Organization"}, {"text": "tertiary care hospital", "type": "Organization"}]}

Example input:
Sentence: The objective of this study was to investigate the epidemiology and outcomes of injuries at 4 referral hospitals in Kenya using hospital -based trauma registries .

Example answer:
{"entities": [{"text": "objective", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "epidemiology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "referral hospitals", "type": "Organization"}, {"text": "Kenya", "type": "SpatialConcept"}, {"text": "hospital", "type": "Organization"}, {"text": "trauma", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: We examined extensive burn wounds in 14 patients by using a combination of autograft and cultured epithelial autografts developed in Japan ( JACE ) .

Example answer:
{"entities": [{"text": "burn wounds", "type": "InjuryOrPoisoning"}, {"text": "autograft", "type": "AnatomicalStructure"}, {"text": "cultured epithelial", "type": "AnatomicalStructure"}, {"text": "autografts", "type": "Chemical"}, {"text": "Japan", "type": "SpatialConcept"}, {"text": "JACE", "type": "Chemical"}]}

Example input:
Sentence: This prospective study was undertaken in a Dutch hospital pharmacy , at Onze Lieve Vrouwe Gasthuis ( OLVG ) , Amsterdam .

Example answer:
{"entities": [{"text": "prospective study", "type": "ResearchActivity"}, {"text": "Dutch hospital pharmacy", "type": "HealthCareActivity"}, {"text": "Onze Lieve Vrouwe Gasthuis", "type": "SpatialConcept"}, {"text": "OLVG", "type": "SpatialConcept"}, {"text": "Amsterdam", "type": "SpatialConcept"}]}

Example input:
Sentence: WHAT THIS PAPER ADDS TO EXISTING KNOWLEDGE ? : This explorative study is unique in offering an insight into current palliative care practice for psychiatric patients and showed that one in three nurses working in Dutch mental health facilities is involved in palliative care provision .

Example answer:
{"entities": [{"text": "explorative study", "type": "ResearchActivity"}, {"text": "palliative care", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Dutch mental health facilities", "type": "Organization"}, {"text": "provision", "type": "HealthCareActivity"}]}

Example input:
Sentence: Aim The aim of this study was to explore nurses ' experiences with and identify barriers to providing palliative care to psychiatric patients in Dutch mental health facilities .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "experiences", "type": "BiologicFunction"}, {"text": "palliative care", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Dutch mental health facilities", "type": "Organization"}]}

Input:
Sentence: The aim of this article is to provide an overview of the type of injuries and applied reconstructive techniques in a large academic hospital in The Netherlands .

## Item MedMentions:test:1766
Example input:
Sentence: In this study , we repurposed Pirfenidone , a clinically approved anti - fibrotic drug for the treatment of idiopathic pulmonary fibrosis , to investigate its possible role on tumor microenvironment normalization .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "Pirfenidone", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "idiopathic pulmonary fibrosis", "type": "BiologicFunction"}, {"text": "normalization", "type": "HealthCareActivity"}]}

Example input:
Sentence: Median OS of CG , CF , and FOLFIRINOX groups was 28 , 21 , and 23 . 5 weeks , respectively ( p = 0 . 497 ) .

Example answer:
{"entities": [{"text": "CG", "type": "Chemical"}, {"text": "CF", "type": "Chemical"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: The side effect profile for divalproex sodium was associated with the smallest willingness to take , with gabapentin , propranolol , and topiramate perceived to be much more agreeable .

Example answer:
{"entities": [{"text": "side effect", "type": "BiologicFunction"}, {"text": "profile", "type": "HealthCareActivity"}, {"text": "divalproex sodium", "type": "Chemical"}, {"text": "smallest willingness to take", "type": "Finding"}, {"text": "gabapentin", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "topiramate", "type": "Chemical"}]}

Example input:
Sentence: 7 % for FOLFIRINOX group .

Example answer:
{"entities": [{"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "group", "type": "PopulationGroup"}]}

Example input:
Sentence: Second - line PFS of FOLFIRINOX was 20 weeks , whereas it was 14 weeks for other fuoropyrimidine -based chemotherapies ( p = 0 . 190 ) .

Example answer:
{"entities": [{"text": "Second - line", "type": "HealthCareActivity"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "fuoropyrimidine", "type": "Chemical"}, {"text": "chemotherapies", "type": "HealthCareActivity"}]}

Example input:
Sentence: 53 ( 57 . 6 % ) , 27 ( 29 . 3 % ) , and 12 ( 13 % ) patients received CG , CF , and FOLFIRINOX regimen as first - line chemotherapy , respectively .

Example answer:
{"entities": [{"text": "received", "type": "Finding"}, {"text": "CG", "type": "Chemical"}, {"text": "CF", "type": "Chemical"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "regimen", "type": "HealthCareActivity"}, {"text": "first - line", "type": "HealthCareActivity"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Comparison of FOLFIRINOX Chemotherapy with Other Regimens in Patients with Biliary Tract Cancers : a Retrospective Study The aim of this retrospective study was to compare the different treatment options of patients with advanced biliary tract carcinoma ( BTC ) who were treated with platinum - gemcitabine ( CG ) or platinum -5 - fluorouracil ( CF ) or 5 - Fluorouracil - oxaliplatin - irinotecan ( FOLFIRINOX ) chemotherapy .

Example answer:
{"entities": [{"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "Chemotherapy", "type": "HealthCareActivity"}, {"text": "Regimens", "type": "HealthCareActivity"}, {"text": "Biliary Tract Cancers", "type": "BiologicFunction"}, {"text": "Retrospective Study", "type": "ResearchActivity"}, {"text": "retrospective study", "type": "ResearchActivity"}, {"text": "treatment options", "type": "HealthCareActivity"}, {"text": "biliary tract carcinoma", "type": "BiologicFunction"}, {"text": "BTC", "type": "BiologicFunction"}, {"text": "platinum", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "CG", "type": "Chemical"}, {"text": "fluorouracil", "type": "Chemical"}, {"text": "CF", "type": "Chemical"}, {"text": "5 - Fluorouracil - oxaliplatin - irinotecan", "type": "HealthCareActivity"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: This was the first study evaluating the FOLFIRINOX regimen in BTC .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "evaluating", "type": "HealthCareActivity"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "regimen", "type": "HealthCareActivity"}, {"text": "BTC", "type": "BiologicFunction"}]}

Example input:
Sentence: Of the 54 patients diagnosed between 2011 and June 2014 , 28 patients received FOLFIRINOX and 22 Gemcitabine as the first - line chemotherapy .

Example answer:
{"entities": [{"text": "diagnosed", "type": "HealthCareActivity"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "Gemcitabine", "type": "Chemical"}, {"text": "first - line chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: This retrospective study analyzes the overall survival of these patients under " real life conditions " before and after the introduction of FOLFIRINOX in 2011 .

Example answer:
{"entities": [{"text": "retrospective study", "type": "ResearchActivity"}, {"text": "analyzes", "type": "ResearchActivity"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}]}

Input:
Sentence: Patients with FOLFIRINOX were further analyzed regarding drug administration and side effects .

## Item MedMentions:test:1236
Example input:
Sentence: We also show that if enhancement of neural activity is combined with elevation of the cell - growth -promoting pathway involving mammalian target of rapamycin ( mTOR ) , RGC axons regenerate long distances and re - innervate the brain .

Example answer:
{"entities": [{"text": "elevation", "type": "SpatialConcept"}, {"text": "cell - growth", "type": "BiologicFunction"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "mammalian target of rapamycin", "type": "Chemical"}, {"text": "mTOR", "type": "Chemical"}, {"text": "RGC", "type": "AnatomicalStructure"}, {"text": "axons", "type": "AnatomicalStructure"}, {"text": "regenerate", "type": "BiologicFunction"}, {"text": "brain", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The axons of graft -derived neurons formed a plexus in the circular muscle layer .

Example answer:
{"entities": [{"text": "axons", "type": "AnatomicalStructure"}, {"text": "graft", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "plexus", "type": "AnatomicalStructure"}, {"text": "circular muscle layer", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 1 channels and calcium ions in nerve terminals following end - to - side neurorrhaphy : ionic imaging analysis by TOF - SIMS The P / Q - type voltage - dependent calcium channel ( Cav2 . 1 ) in the presynaptic membranes of motor nerve terminals plays an important role in regulating Ca ( 2 + ) transport , resulting in transmitter release within the nervous system .

Example answer:
{"entities": [{"text": "1 channels", "type": "Chemical"}, {"text": "calcium ions", "type": "Chemical"}, {"text": "nerve terminals", "type": "AnatomicalStructure"}, {"text": "end - to - side neurorrhaphy", "type": "HealthCareActivity"}, {"text": "ionic imaging analysis", "type": "HealthCareActivity"}, {"text": "P / Q - type voltage - dependent calcium channel", "type": "Chemical"}, {"text": "Cav2 . 1", "type": "Chemical"}, {"text": "presynaptic membranes", "type": "AnatomicalStructure"}, {"text": "motor nerve", "type": "AnatomicalStructure"}, {"text": "terminals", "type": "AnatomicalStructure"}, {"text": "regulating Ca ( 2 + ) transport", "type": "BiologicFunction"}, {"text": "transmitter", "type": "Chemical"}, {"text": "nervous system", "type": "BodySystem"}]}

Example input:
Sentence: We present an improved electrospinning method for fabrication of scaffolds that promote neuronal differentiation into highly 3D integrated networks , formation of inhibitory and excitatory synapses and extensive neurite growth .

Example answer:
{"entities": [{"text": "improved", "type": "Finding"}, {"text": "electrospinning method", "type": "IntellectualProduct"}, {"text": "neuronal", "type": "AnatomicalStructure"}, {"text": "differentiation", "type": "BiologicFunction"}, {"text": "3D", "type": "SpatialConcept"}, {"text": "integrated networks", "type": "SpatialConcept"}, {"text": "inhibitory", "type": "AnatomicalStructure"}, {"text": "excitatory synapses", "type": "AnatomicalStructure"}, {"text": "neurite growth", "type": "BiologicFunction"}]}

Example input:
Sentence: In particular , after axonal damage or pruning the clearance of axonal debris by glial cells is key for a healthy nervous system .

Example answer:
{"entities": [{"text": "axonal damage", "type": "InjuryOrPoisoning"}, {"text": "axonal", "type": "AnatomicalStructure"}, {"text": "debris", "type": "Finding"}, {"text": "glial cells", "type": "AnatomicalStructure"}, {"text": "nervous system", "type": "BodySystem"}]}

Example input:
Sentence: Neural activity promotes long - distance , target - specific regeneration of adult retinal axons Axons in the mammalian CNS fail to regenerate after injury .

Example answer:
{"entities": [{"text": "regeneration", "type": "BiologicFunction"}, {"text": "retinal", "type": "AnatomicalStructure"}, {"text": "axons", "type": "AnatomicalStructure"}, {"text": "Axons", "type": "AnatomicalStructure"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "CNS", "type": "BodySystem"}, {"text": "regenerate", "type": "BiologicFunction"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: However , whether these approaches allow remyelination and promote the reestablishment of AIS and nodes of Ranvier is unknown .

Example answer:
{"entities": [{"text": "remyelination", "type": "BiologicFunction"}, {"text": "AIS", "type": "AnatomicalStructure"}, {"text": "nodes of Ranvier", "type": "SpatialConcept"}]}

Example input:
Sentence: Although axons grew rapidly , remyelination and nodal ion channel clustering was much slower .

Example answer:
{"entities": [{"text": "axons", "type": "AnatomicalStructure"}, {"text": "grew", "type": "BiologicFunction"}, {"text": "remyelination", "type": "BiologicFunction"}, {"text": "nodal ion channel clustering", "type": "BiologicFunction"}]}

Example input:
Sentence: Finally , genetic deletion of ankyrinG from RGCs to block AIS reassembly did not affect axon regeneration , indicating that preservation of neuronal polarity is not required for axon regeneration .

Example answer:
{"entities": [{"text": "genetic deletion", "type": "BiologicFunction"}, {"text": "ankyrinG", "type": "Chemical"}, {"text": "RGCs", "type": "AnatomicalStructure"}, {"text": "AIS", "type": "AnatomicalStructure"}, {"text": "axon regeneration", "type": "BiologicFunction"}, {"text": "neuronal polarity", "type": "SpatialConcept"}, {"text": "not required", "type": "Finding"}]}

Example input:
Sentence: Together , our results demonstrate , for the first time , that regenerating CNS axons can be remyelinated and reassemble new AIS and nodes of Ranvier .

Example answer:
{"entities": [{"text": "regenerating", "type": "BiologicFunction"}, {"text": "CNS", "type": "BodySystem"}, {"text": "axons", "type": "AnatomicalStructure"}, {"text": "remyelinated", "type": "BiologicFunction"}, {"text": "AIS", "type": "AnatomicalStructure"}, {"text": "nodes of Ranvier", "type": "SpatialConcept"}]}

Input:
Sentence: Reassembly of Excitable Domains after CNS Axon Regeneration Action potential initiation and propagation in myelinated axons require ion channel clustering at axon initial segments ( AIS ) and nodes of Ranvier .

## Item MedMentions:test:1505
Example input:
Sentence:  had spinal cord or vertebral artery injury .

Example answer:
{"entities": [{"text": "spinal cord", "type": "InjuryOrPoisoning"}, {"text": "vertebral artery injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Spinal versus general anaesthesia in surgery for inguinodynia ( SPINASIA trial ) : study protocol for a randomised controlled trial Chronic inguinodynia ( groin pain ) is a common complication following open inguinal hernia repair or a Pfannenstiel incision but may also be experienced after other types of ( groin ) surgery .

Example answer:
{"entities": [{"text": "Spinal", "type": "HealthCareActivity"}, {"text": "general anaesthesia", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "inguinodynia", "type": "Finding"}, {"text": "SPINASIA trial", "type": "ResearchActivity"}, {"text": "study protocol", "type": "IntellectualProduct"}, {"text": "randomised controlled trial", "type": "ResearchActivity"}, {"text": "Chronic inguinodynia", "type": "Finding"}, {"text": "groin pain", "type": "Finding"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "open inguinal hernia repair", "type": "HealthCareActivity"}, {"text": "Pfannenstiel incision", "type": "HealthCareActivity"}, {"text": "groin", "type": "SpatialConcept"}]}

Example input:
Sentence: Spine fractures have substantial medical significance but are seldom recognized .

Example answer:
{"entities": [{"text": "Spine fractures", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: This finding opens a new , minimal invasive route for therapy after spinal cord injury .

Example answer:
{"entities": [{"text": "finding", "type": "Finding"}, {"text": "minimal invasive route for therapy", "type": "HealthCareActivity"}, {"text": "spinal cord injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Identifying spine fractures as part of comprehensive risk assessment may improve clinical decision making .

Example answer:
{"entities": [{"text": "spine fractures", "type": "InjuryOrPoisoning"}, {"text": "risk assessment", "type": "HealthCareActivity"}, {"text": "improve", "type": "Finding"}, {"text": "clinical decision making", "type": "HealthCareActivity"}]}

Example input:
Sentence: The surgical treatment of spinal metastases is controversial .

Example answer:
{"entities": [{"text": "surgical treatment", "type": "HealthCareActivity"}, {"text": "spinal metastases", "type": "BiologicFunction"}]}

Example input:
Sentence: Does Intrawound Vancomycin Application During Spine Surgery Create Vancomycin - Resistant Organism ? Surgical site infection ( SSI ) following spine surgery is a morbid and expensive complication .

Example answer:
{"entities": [{"text": "Intrawound Vancomycin", "type": "Chemical"}, {"text": "Spine Surgery", "type": "HealthCareActivity"}, {"text": "Surgical site infection", "type": "BiologicFunction"}, {"text": "SSI", "type": "BiologicFunction"}, {"text": "spine surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: The Effectiveness of a Systematic Algorithm for the Management of Vascular Injuries during the Laparoscopic Surgery Currently , there is no standardized training protocol to teach surgeons how to deal with vascular injuries during laparoscopic procedures .

Example answer:
{"entities": [{"text": "Systematic Algorithm", "type": "IntellectualProduct"}, {"text": "Management", "type": "HealthCareActivity"}, {"text": "Vascular Injuries", "type": "InjuryOrPoisoning"}, {"text": "Laparoscopic Surgery", "type": "HealthCareActivity"}, {"text": "training protocol", "type": "IntellectualProduct"}, {"text": "surgeons", "type": "ProfessionalOrOccupationalGroup"}, {"text": "vascular injuries", "type": "InjuryOrPoisoning"}, {"text": "laparoscopic procedures", "type": "HealthCareActivity"}]}

Example input:
Sentence: We recommended that great attention be paid to drill and screw insertion around the mid - shaft level for prevention of iatrogenic vascular injury .

Example answer:
{"entities": [{"text": "recommended", "type": "HealthCareActivity"}, {"text": "drill", "type": "HealthCareActivity"}, {"text": "screw", "type": "MedicalDevice"}, {"text": "insertion", "type": "HealthCareActivity"}, {"text": "mid - shaft", "type": "AnatomicalStructure"}, {"text": "vascular injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The arterial injury may be iatrogenic , occurring during intramedullary internal fixation , or less frequently , the injury may be due to the fracture itself , caused by a sharp bone fragment that damages the profunda femoris artery or one of its perforating branches .

Example answer:
{"entities": [{"text": "arterial injury", "type": "InjuryOrPoisoning"}, {"text": "intramedullary", "type": "SpatialConcept"}, {"text": "internal fixation", "type": "HealthCareActivity"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "fracture", "type": "InjuryOrPoisoning"}, {"text": "sharp", "type": "Finding"}, {"text": "bone fragment", "type": "InjuryOrPoisoning"}, {"text": "profunda femoris artery", "type": "AnatomicalStructure"}, {"text": "perforating", "type": "Finding"}, {"text": "branches", "type": "SpatialConcept"}]}

Input:
Sentence: However , the traditional approach to spinal surgery carries the risk of catastrophic bleeding from injury to major vessels , as well as iatrogenic injury to the viscera and associated structures .

## Item MedMentions:test:1522
Example input:
Sentence: 90 % , and had more HTN risk factors and HTN outcomes than those without HTN , all P < .0001 , including male and female subgroups , each P < .0001 .

Example answer:
{"entities": [{"text": "HTN", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "subgroups", "type": "IntellectualProduct"}]}

Example input:
Sentence: Patients with GCA had increased risks for all types of incident vascular disease compared with non - vasculitis patients : adjusted hazard ratios were 1 . 57 ( 95 % CI : 1 . 36 , 1 . 82 ) for myocardial infarction , 1 . 41 ( 95 % CI : 1 . 29 , 1 . 55 ) for stroke , 1 . 75 ( 95 % CI : 1 . 49 , 2 . 06 ) for peripheral vascular disease , 1 . 98 ( 95 % CI : 1 . 50 , 2 . 62 ) for aortic aneurysm and 2 . 03 ( 95 % CI : 1 . 77 , 2 . 33 ) for venous thromboembolism .

Example answer:
{"entities": [{"text": "GCA", "type": "BiologicFunction"}, {"text": "risks for all types of incident", "type": "Finding"}, {"text": "vascular disease", "type": "BiologicFunction"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "peripheral vascular disease", "type": "BiologicFunction"}, {"text": "aortic aneurysm", "type": "BiologicFunction"}, {"text": "venous thromboembolism", "type": "BiologicFunction"}]}

Example input:
Sentence: During a median follow - up of 46 months , patients in the upper tertile of changes in peak V̇O2 ( ≥13 . 0 % ) , compared with those in the lower tertile ( < 1 . 0 % ) , had lower rates of the composite of all - cause death or HF hospitalization ( 37 . 9 % vs .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "peak V̇O2", "type": "Finding"}, {"text": "death", "type": "BiologicFunction"}, {"text": "HF", "type": "BiologicFunction"}, {"text": "hospitalization", "type": "HealthCareActivity"}]}

Example input:
Sentence: Increased VWF levels are observed in hypertension ( HTN ) and disorders of endothelial dysfunction , for example , atherosclerotic heart disease ( ASHD ) and diabetes .

Example answer:
{"entities": [{"text": "VWF", "type": "Chemical"}, {"text": "hypertension", "type": "BiologicFunction"}, {"text": "HTN", "type": "BiologicFunction"}, {"text": "endothelial dysfunction", "type": "BiologicFunction"}, {"text": "atherosclerotic heart disease", "type": "BiologicFunction"}, {"text": "ASHD", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Since 2001 , 195 patients with previously untreated TN were managed : with MVD in 79 , RF in 36 , and SRS in 80 .

Example answer:
{"entities": [{"text": "TN", "type": "BiologicFunction"}, {"text": "MVD", "type": "HealthCareActivity"}, {"text": "RF", "type": "HealthCareActivity"}, {"text": "SRS", "type": "HealthCareActivity"}]}

Example input:
Sentence: Factors associated with mortality were univentricular repair ( hazard ratio [ HR ] , 2 . 12 ; 95 % CI , 1 . 21 - 3 . 70 ; P = .008 ) and acute renal failure ( HR , 3 . 01 ; 95 % CI , 1 . 77 - 5 . 12 ; P < .001 ) , but era did not influence mortality ( 1997 - 2005 vs 2006 - 2012 ; log - rank P = .66 ) .

Example answer:
{"entities": [{"text": "univentricular repair", "type": "HealthCareActivity"}, {"text": "acute renal failure", "type": "BiologicFunction"}]}

Example input:
Sentence: The prevalence of hypertension in patients with VWD ( N = 7556 ) , 37 . 35 % , was significantly lower than that in non - VWD patients ( N = 19 918 970 ) , 49 . 40 % , P < .0001 .

Example answer:
{"entities": [{"text": "hypertension", "type": "BiologicFunction"}, {"text": "VWD", "type": "BiologicFunction"}, {"text": "non - VWD", "type": "Finding"}]}

Example input:
Sentence: To determine prevalence and risk factors for HTN in patients with von Willebrand disease ( VWD ) , we conducted a cross - sectional analysis of discharge data from the National Inpatient Sample , 2009 to 2011 .

Example answer:
{"entities": [{"text": "risk factors", "type": "Finding"}, {"text": "HTN", "type": "BiologicFunction"}, {"text": "von Willebrand disease", "type": "BiologicFunction"}, {"text": "VWD", "type": "BiologicFunction"}, {"text": "cross - sectional analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Odds of HTN and HTN outcomes in VWD were estimated by weighted multivariable logistic regression .

Example answer:
{"entities": [{"text": "HTN", "type": "BiologicFunction"}, {"text": "VWD", "type": "BiologicFunction"}, {"text": "multivariable logistic regression", "type": "ResearchActivity"}]}

Example input:
Sentence: The risk of HTN is reduced in patients with VWD , but not after adjustment for HTN risk factors plus demographics , as patients with VWD not having HTN are also typically young , Caucasian , and female .

Example answer:
{"entities": [{"text": "HTN", "type": "BiologicFunction"}, {"text": "VWD", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "Caucasian", "type": "PopulationGroup"}]}

Input:
Sentence: The unadjusted odds of HTN in patients with VWD ( odds ratio [ OR ] = 0 . 611 , P < .0001 ) and of HTN outcomes in patients with VWD ( ASHD , OR = 0 . 509 ; MI , OR = 0 . 422 ; ischemic stroke , OR = 0 . 521 ; renal failure , OR = 0 . 420 , all P < .0001 ) became insignificant after adjustment for HTN risk factors plus demographics ( age / race / gender ) , OR = 1 .

## Item MedMentions:test:1738
Example input:
Sentence: Repeated - measures analysis demonstrated that the experience of pain differed significantly over time by location ( F5 , 70 = 3 . 864 , P = .004 ) , with a notable decrease in pain scores more than 1 hour after sheath removal at the location that used the progressive head elevation protocol .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "pain", "type": "Finding"}, {"text": "location", "type": "SpatialConcept"}, {"text": "pain scores", "type": "Finding"}, {"text": "sheath", "type": "AnatomicalStructure"}, {"text": "removal", "type": "HealthCareActivity"}, {"text": "head", "type": "SpatialConcept"}, {"text": "elevation protocol", "type": "HealthCareActivity"}]}

Example input:
Sentence: The ASES score improved significantly in both groups ( P < .03 ) , whereas the SANE ; Quick Disabilities of the Arm , Shoulder and Hand ; and Short Form 12 Physical Component Summary scores only significantly improved for patients with traumatic PSI ( P < .02 ) .

Example answer:
{"entities": [{"text": "ASES score", "type": "IntellectualProduct"}, {"text": "groups", "type": "PopulationGroup"}, {"text": "SANE", "type": "IntellectualProduct"}, {"text": "Quick Disabilities of the Arm , Shoulder and Hand", "type": "ClinicalAttribute"}, {"text": "Short Form 12 Physical Component Summary scores", "type": "IntellectualProduct"}, {"text": "traumatic", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Outcomes included pain severity , functional disability , and quality of life .

Example answer:
{"entities": []}

Example input:
Sentence: We found that minor injuries had major impacts on pain ratings , physical and mental well - being , health -related quality of life and return to work and pre - injury participation during the 24 months post - injury phase .

Example answer:
{"entities": [{"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "pain", "type": "Finding"}, {"text": "ratings", "type": "IntellectualProduct"}, {"text": "physical", "type": "Finding"}, {"text": "mental well - being", "type": "BiologicFunction"}, {"text": "pre - injury", "type": "InjuryOrPoisoning"}, {"text": "post - injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: In addition , patient satisfaction , pain , stiffness , and impairment of activities of daily living were assessed on a Visual Analogue Scale ( VAS ) followed by a question stating whether they would undergo the same procedure again .

Example answer:
{"entities": [{"text": "pain", "type": "Finding"}, {"text": "stiffness", "type": "Finding"}, {"text": "Visual Analogue Scale", "type": "HealthCareActivity"}, {"text": "VAS", "type": "HealthCareActivity"}]}

Example input:
Sentence: PROs assessed included Patient Global Assessment of disease ( PtGA ) , pain , Health Assessment Questionnaire - Disability Index ( HAQ - DI ) , Functional Assessment of Chronic Illness Therapy - Fatigue ( FACIT - F ) and health - related quality of life ( Short Form - 36 [ SF - 36 ] ) .

Example answer:
{"entities": [{"text": "PROs", "type": "IntellectualProduct"}, {"text": "Patient Global Assessment of disease", "type": "IntellectualProduct"}, {"text": "PtGA", "type": "IntellectualProduct"}, {"text": "pain", "type": "Finding"}, {"text": "Health Assessment Questionnaire - Disability Index", "type": "IntellectualProduct"}, {"text": "HAQ - DI", "type": "IntellectualProduct"}, {"text": "Functional Assessment of Chronic Illness Therapy - Fatigue", "type": "IntellectualProduct"}, {"text": "FACIT - F", "type": "IntellectualProduct"}, {"text": "Short Form - 36", "type": "IntellectualProduct"}, {"text": "SF - 36", "type": "IntellectualProduct"}]}

Example input:
Sentence: A significantly improved health - related quality of life was found 1 year after surgery , with improvements in all eight aspects of SF - 36 ( p < 0 . 001 ) .

Example answer:
{"entities": [{"text": "improved", "type": "Finding"}, {"text": "SF - 36", "type": "IntellectualProduct"}]}

Example input:
Sentence: There was no difference in pain during the 1 st and 7 th post - operative , physical functioning , physical limitation , the impact of pain on daily activities , and the Carolinas Comfort Scale during the 7 th and 15 th post - operative ( P > 0 . 05 ) .

Example answer:
{"entities": [{"text": "pain", "type": "Finding"}, {"text": "post - operative", "type": "Finding"}, {"text": "physical functioning", "type": "Finding"}, {"text": "Carolinas Comfort Scale", "type": "IntellectualProduct"}]}

Example input:
Sentence: At all follow - up time points , the operative groups had a lower percentage of patients reporting pain with their sex life compared to the nonoperative group ( P < 0 .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "pain", "type": "Finding"}]}

Example input:
Sentence: Worse function and quality of life ( as assessed by all FAOS subscales and the SF - 12 physical and mental components ) , more depressive and anxiety symptoms , and higher pain VAS scores were associated with higher expectations scores and more expectations ( P < .01 for all ) .

Example answer:
{"entities": [{"text": "Worse", "type": "Finding"}, {"text": "function", "type": "BiologicFunction"}, {"text": "SF - 12", "type": "IntellectualProduct"}, {"text": "depressive", "type": "Finding"}, {"text": "anxiety symptoms", "type": "Finding"}]}

Input:
Sentence: The bodily pain , vitality , and mental health subcategories were significantly improved at the latest follow - up ( p < 0 . 05 ) .

## Item MedMentions:test:1779
Example input:
Sentence: Retrospective cohort of women with their first two consecutive singleton pregnancies carried to ≥ 20 ( 0 / 7 ) weeks ' gestation within a tertiary health care system from 2002 to 2012 .

Example answer:
{"entities": [{"text": "cohort", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "singleton pregnancies", "type": "BiologicFunction"}, {"text": "gestation", "type": "BiologicFunction"}, {"text": "tertiary health care system", "type": "Organization"}]}

Example input:
Sentence: We suggest that this might be partially due to a closer monitoring of twin pregnancies , which indirectly suggests a need for closer surveillance of singleton pregnancies .

Example answer:
{"entities": [{"text": "closer", "type": "Finding"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "twin pregnancies", "type": "Finding"}, {"text": "surveillance", "type": "HealthCareActivity"}, {"text": "singleton pregnancies", "type": "BiologicFunction"}]}

Example input:
Sentence: The purpose of this study was to compare perinatal mortality rates in relation to gestational age at birth between singleton and twin pregnancies , taking into account socioeconomic status , fetal sex , and parity .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "perinatal mortality", "type": "Finding"}, {"text": "birth", "type": "BiologicFunction"}, {"text": "singleton", "type": "BiologicFunction"}, {"text": "twin pregnancies", "type": "Finding"}, {"text": "account", "type": "Finding"}, {"text": "parity", "type": "Finding"}]}

Example input:
Sentence: After 39 weeks of gestation , the perinatal mortality rate was high er in twin pregnancies .

Example answer:
{"entities": [{"text": "gestation", "type": "BiologicFunction"}, {"text": "perinatal mortality", "type": "Finding"}, {"text": "twin pregnancies", "type": "Finding"}]}

Example input:
Sentence: We studied perinatal mortality rates according to gestational age at birth in 1 , 502 , 120 singletons pregnancies and 51 , 658 twin pregnancies without congenital malformations who were delivered between 2002 and 2010 after 28 weeks of gestation .

Example answer:
{"entities": [{"text": "studied", "type": "ResearchActivity"}, {"text": "perinatal mortality", "type": "Finding"}, {"text": "birth", "type": "BiologicFunction"}, {"text": "singletons pregnancies", "type": "BiologicFunction"}, {"text": "twin pregnancies", "type": "Finding"}, {"text": "congenital malformations", "type": "AnatomicalStructure"}, {"text": "delivered", "type": "BiologicFunction"}, {"text": "gestation", "type": "BiologicFunction"}]}

Example input:
Sentence: Lower perinatal mortality in preterm born twins than in singletons : a nationwide study from The Netherlands Twin pregnancies are at increased risk for perinatal morbidity and death because of many factors that include a high incidence of preterm delivery .

Example answer:
{"entities": [{"text": "perinatal mortality", "type": "Finding"}, {"text": "singletons", "type": "Finding"}, {"text": "study", "type": "ResearchActivity"}, {"text": "Netherlands", "type": "SpatialConcept"}, {"text": "Twin pregnancies", "type": "Finding"}, {"text": "increased risk", "type": "Finding"}, {"text": "death", "type": "BiologicFunction"}, {"text": "preterm delivery", "type": "Finding"}]}

Example input:
Sentence: During the preterm period , the antepartum mortality rate was much lower in twin pregnancies than in singleton pregnancies .

Example answer:
{"entities": [{"text": "twin pregnancies", "type": "Finding"}, {"text": "singleton pregnancies", "type": "BiologicFunction"}]}

Example input:
Sentence: Overall the perinatal mortality rate was higher in twin pregnancies than in singleton pregnancies , which is most likely caused by the high preterm birth rate in twins and not by a higher mortality rate for gestation , apart from term pregnancies .

Example answer:
{"entities": [{"text": "perinatal mortality", "type": "Finding"}, {"text": "twin pregnancies", "type": "Finding"}, {"text": "singleton pregnancies", "type": "BiologicFunction"}, {"text": "twins", "type": "Finding"}, {"text": "gestation", "type": "BiologicFunction"}, {"text": "term pregnancies", "type": "BiologicFunction"}]}

Example input:
Sentence: Compared with singleton pregnancies , overall perinatal risk of death is higher in twin pregnancies ; however , for the preterm period , the perinatal mortality rate has been reported to be lower in twins .

Example answer:
{"entities": [{"text": "singleton pregnancies", "type": "BiologicFunction"}, {"text": "perinatal risk", "type": "Finding"}, {"text": "death", "type": "BiologicFunction"}, {"text": "twin pregnancies", "type": "Finding"}, {"text": "perinatal mortality", "type": "Finding"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "twins", "type": "Finding"}]}

Example input:
Sentence: Overall the perinatal mortality rate in twin pregnancies ( 6 . 6 / 1000 infants ) was higher than in singleton pregnancies ( 4 . 1 / 1000 infants ) .

Example answer:
{"entities": [{"text": "perinatal mortality", "type": "Finding"}, {"text": "twin pregnancies", "type": "Finding"}, {"text": "singleton pregnancies", "type": "BiologicFunction"}]}

Input:
Sentence: However , in the preterm period , the perinatal mortality rate in twin pregnancies was substantially lower than in singleton pregnancies ( 10 . 4 per 1000 infants as compared with 34 .

## Item MedMentions:test:1468
Example input:
Sentence: The prepared nanoparticles were modified by pure AChE and they were used for the measurement anti - Alzheimer 's drug galantamine and carbamate pesticide carbofuran with limit of detection 1 .

Example answer:
{"entities": [{"text": "pure AChE", "type": "Chemical"}, {"text": "anti - Alzheimer 's", "type": "Finding"}, {"text": "drug", "type": "Chemical"}, {"text": "galantamine", "type": "Chemical"}, {"text": "carbamate pesticide", "type": "Chemical"}, {"text": "carbofuran", "type": "Chemical"}, {"text": "detection", "type": "Finding"}]}

Example input:
Sentence: Metabolic responses of the growing Daphnia similis to chronic AgNPs exposure as revealed by GC - Q - TOF / MS and LC - Q - TOF / MS Silver nanoparticles ( AgNPs ) are one of the most widely used nanomaterials .

Example answer:
{"entities": [{"text": "Metabolic responses", "type": "Finding"}, {"text": "Daphnia similis", "type": "Eukaryote"}, {"text": "Silver", "type": "Chemical"}]}

Example input:
Sentence: Antibacterial effect of PEO coating with silver on AA7075 In this work , plasma electrolytic oxidation ( PEO ) coatings were produced on AA7075 using alkaline solution containing silicates compounds and silver micrometric particles in order to give to the coating an antimicrobial effect .

Example answer:
{"entities": [{"text": "Antibacterial effect", "type": "BiologicFunction"}, {"text": "silver", "type": "Chemical"}, {"text": "AA7075", "type": "Chemical"}, {"text": "silicates compounds", "type": "Chemical"}, {"text": "micrometric particles", "type": "Chemical"}, {"text": "antimicrobial effect", "type": "BiologicFunction"}]}

Example input:
Sentence: The silver particles , found both inside and outside of the pores that characterize the PEO layer , produced an efficacious antimicrobial effect both against E .

Example answer:
{"entities": [{"text": "silver", "type": "Chemical"}, {"text": "particles", "type": "Chemical"}, {"text": "inside", "type": "SpatialConcept"}, {"text": "outside", "type": "SpatialConcept"}, {"text": "antimicrobial effect", "type": "BiologicFunction"}, {"text": "E .", "type": "Bacterium"}]}

Example input:
Sentence: The biosynthesized AgNPs demonstrated potentials as anticancer and antibacterial agents .

Example answer:
{"entities": [{"text": "AgNPs", "type": "Chemical"}, {"text": "anticancer", "type": "Chemical"}, {"text": "antibacterial agents", "type": "Chemical"}]}

Example input:
Sentence: The coatings demonstrate the bactericidal effect against the gram - positive Staphylococcus aureus ATCC 209P and gram - negative Escherichia coli ATCC 25922 bacteria both under the natural light and in the darkness .

Example answer:
{"entities": [{"text": "bactericidal effect", "type": "Finding"}, {"text": "gram - positive", "type": "Bacterium"}, {"text": "Staphylococcus aureus ATCC 209P", "type": "Bacterium"}, {"text": "gram - negative", "type": "Bacterium"}, {"text": "Escherichia coli ATCC 25922", "type": "Bacterium"}, {"text": "bacteria", "type": "Bacterium"}]}

Example input:
Sentence: Silver nanoparticles ( Ag NPs ) were added to increase the flexibility of the polymer and the conductivity of the electrode .

Example answer:
{"entities": [{"text": "Silver", "type": "Chemical"}, {"text": "polymer", "type": "Chemical"}]}

Example input:
Sentence: Silver nanoparticles were prepared from the reduction of silver nitrate and NaBH4 was used as reducing agent .

Example answer:
{"entities": [{"text": "Silver", "type": "Chemical"}, {"text": "silver nitrate", "type": "Chemical"}, {"text": "NaBH4", "type": "Chemical"}, {"text": "reducing agent", "type": "Chemical"}]}

Example input:
Sentence: Green and rapid synthesis of silver nanoparticles using Borago officinalis leaf extract : anticancer and antibacterial activities This study highlights the facile , reliable , cost effective , and ecofriendly synthesis of silver nanoparticles ( AgNPs ) using Borago officinalis leaves extract efficiently .

Example answer:
{"entities": [{"text": "silver", "type": "Chemical"}, {"text": "Borago officinalis", "type": "Eukaryote"}, {"text": "leaf", "type": "Eukaryote"}, {"text": "extract", "type": "Chemical"}, {"text": "anticancer", "type": "Finding"}, {"text": "antibacterial activities", "type": "Finding"}, {"text": "leaves", "type": "Eukaryote"}]}

Example input:
Sentence: The results indicates that TiO2 and ZnO nanoparticle inhibits Salmonella , Klebsiella and Shigella .

Example answer:
{"entities": [{"text": "TiO2", "type": "Chemical"}, {"text": "ZnO", "type": "Chemical"}, {"text": "Salmonella", "type": "Bacterium"}, {"text": "Klebsiella", "type": "Bacterium"}, {"text": "Shigella", "type": "Bacterium"}]}

Input:
Sentence: Antibacterial activities of the synthesized silver nanoparticles were tested against Staphylococcus aureus ATCC 25923 , Salmonella typhi ATCC 14028 , Escherichia coli ATCC 25922 and Pseudomonas aeruginosa ATCC 27853 .

## Item MedMentions:test:1577
Example input:
Sentence: As a remarkable clue and as early as 1986 , ultrasonography ( US ) has been proven a reliable diagnostic method that is also explicitly helpful in difficult cases with atypical presentation and enables to rule out many differential diagnoses .Recent publications emphasized the role of multidetector computed tomography ( CT ) resulting in a significant reduction of false negative findings at operation .

Example answer:
{"entities": [{"text": "ultrasonography", "type": "HealthCareActivity"}, {"text": "US", "type": "HealthCareActivity"}, {"text": "diagnostic method", "type": "HealthCareActivity"}, {"text": "differential diagnoses", "type": "HealthCareActivity"}, {"text": "publications", "type": "IntellectualProduct"}, {"text": "multidetector computed tomography", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "false negative findings", "type": "Finding"}, {"text": "operation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Eighteen FNA cases of cervical vertebral and paravertebral lesions performed by a trans - oral route without any image - guidance between 1995 and 2014 were retrieved from the archives of the cytology department at PGIMER , Chandigarh and reviewed .

Example answer:
{"entities": [{"text": "cervical vertebral", "type": "AnatomicalStructure"}, {"text": "paravertebral", "type": "SpatialConcept"}, {"text": "lesions", "type": "Finding"}, {"text": "trans - oral route", "type": "SpatialConcept"}, {"text": "cytology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "department", "type": "Organization"}, {"text": "PGIMER", "type": "Organization"}]}

Example input:
Sentence: Our data suggests that any woman whose fetus has a posterior fossa abnormality as the only intracranial finding on USS should have iuMR imaging for further evaluation .

Example answer:
{"entities": [{"text": "woman", "type": "PopulationGroup"}, {"text": "fetus", "type": "AnatomicalStructure"}, {"text": "posterior fossa abnormality", "type": "Finding"}, {"text": "intracranial finding", "type": "Finding"}, {"text": "USS", "type": "HealthCareActivity"}, {"text": "iuMR imaging", "type": "HealthCareActivity"}, {"text": "evaluation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Thirty - two out of 72 ELBW infants underwent conventional MR imaging and DTI at term - equivalent age .

Example answer:
{"entities": [{"text": "ELBW infants", "type": "Finding"}, {"text": "MR imaging", "type": "HealthCareActivity"}, {"text": "DTI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Successful Fetal Tele - Echo at a Small Regional Hospital Prenatal diagnosis of complex congenital heart disease ( CHD ) has been shown to improve newborn outcomes .

Example answer:
{"entities": [{"text": "Fetal Tele - Echo", "type": "HealthCareActivity"}, {"text": "Small Regional Hospital", "type": "Organization"}, {"text": "Prenatal diagnosis", "type": "HealthCareActivity"}, {"text": "congenital heart disease", "type": "AnatomicalStructure"}, {"text": "CHD", "type": "AnatomicalStructure"}, {"text": "improve", "type": "Finding"}, {"text": "newborn", "type": "Finding"}]}

Example input:
Sentence: A clinical fetal tele - echo service was established at King 's Daughters Medical Center ( KDMC ) in Ashland , KY , a region in eastern Kentucky that is 3 h from the nearest congenital heart surgeon .

Example answer:
{"entities": [{"text": "clinical fetal tele - echo", "type": "HealthCareActivity"}, {"text": "King 's Daughters Medical Center", "type": "Organization"}, {"text": "KDMC", "type": "Organization"}, {"text": "Ashland", "type": "SpatialConcept"}, {"text": "KY", "type": "SpatialConcept"}, {"text": "eastern Kentucky", "type": "SpatialConcept"}, {"text": "congenital heart surgeon", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Anatomical subgroup analysis of the MERIDIAN cohort : Posterior fossa abnormalities To assess the diagnostic and clinical contribution of in utero magnetic resonance ( iuMR ) imaging in fetuses diagnosed with abnormalities of the posterior fossa as the only intracranial abnormality recognised on antenatal ultrasonography ( USS ) .

Example answer:
{"entities": [{"text": "subgroup", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "Posterior fossa abnormalities", "type": "Finding"}, {"text": "in utero magnetic resonance ( iuMR ) imaging", "type": "HealthCareActivity"}, {"text": "fetuses", "type": "AnatomicalStructure"}, {"text": "diagnosed", "type": "Finding"}, {"text": "abnormalities of the posterior fossa", "type": "Finding"}, {"text": "intracranial abnormality", "type": "Finding"}, {"text": "antenatal ultrasonography", "type": "HealthCareActivity"}, {"text": "USS", "type": "HealthCareActivity"}]}

Example input:
Sentence: Medical records were reviewed for all mother - infant pairs who had fetal tele - echoes performed at KDMC and interpreted by University of Louisville pediatric cardiology between March 2011 and December 2013 .

Example answer:
{"entities": [{"text": "Medical records", "type": "IntellectualProduct"}, {"text": "fetal tele - echoes", "type": "HealthCareActivity"}, {"text": "KDMC", "type": "Organization"}, {"text": "University of Louisville pediatric cardiology", "type": "Organization"}]}

Example input:
Sentence: We report two consecutive voluntary pregnancy interruptions in a nonconsanguineous couple following the fetal ultrasound finding of cleft lip and palate and posterior fossa anomalies confirmed by means of post - termination examination on the second fetus .

Example answer:
{"entities": [{"text": "report", "type": "HealthCareActivity"}, {"text": "pregnancy", "type": "BiologicFunction"}, {"text": "fetal ultrasound", "type": "HealthCareActivity"}, {"text": "finding", "type": "Finding"}, {"text": "cleft lip", "type": "AnatomicalStructure"}, {"text": "palate", "type": "AnatomicalStructure"}, {"text": "posterior fossa anomalies", "type": "Finding"}, {"text": "post - termination examination", "type": "HealthCareActivity"}, {"text": "second fetus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We report a sub - group analysis of fetuses with abnormalities of the posterior fossa diagnosed on antenatal USS ( with or without ventriculomegaly ) from the MERIDIAN cohort who had iuMR imaging within 2 weeks of USS and outcome reference data were available .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "sub - group", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "fetuses", "type": "AnatomicalStructure"}, {"text": "abnormalities of the posterior fossa", "type": "Finding"}, {"text": "diagnosed", "type": "Finding"}, {"text": "antenatal USS", "type": "HealthCareActivity"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "iuMR imaging", "type": "HealthCareActivity"}, {"text": "USS", "type": "HealthCareActivity"}]}

Input:
Sentence: Antenatal consultation following limb malformation discovery using ultrasound scan Our unit has been providing antenatal consultations for 30 years following the discovery of limb malformation with the fetus .

## Item MedMentions:test:1981
Example input:
Sentence: Benchmark study on fine - mode aerosol in a big urban area and relevant doses deposited in the human respiratory tract It is well - known that the health effects of PM increase as particle size decreases : particularly , great concern has risen on the role of UltraFine Particles ( UFPs ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "respiratory tract", "type": "AnatomicalStructure"}, {"text": "PM", "type": "Chemical"}, {"text": "UltraFine Particles", "type": "Chemical"}, {"text": "UFPs", "type": "Chemical"}]}

Example input:
Sentence: PMcoarse was associated with an increase in FENO , indicating sub - clinical airway inflammation in healthy children .

Example answer:
{"entities": [{"text": "airway", "type": "AnatomicalStructure"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "healthy children", "type": "Finding"}]}

Example input:
Sentence: We conclude that the impact of PM2 .

Example answer:
{"entities": []}

Example input:
Sentence: In multi - pollutant models an interquartile range increase in 24 h PMcoarse was associated with increases in FENO by between 6 .

Example answer:
{"entities": [{"text": "multi - pollutant", "type": "Chemical"}, {"text": "models", "type": "IntellectualProduct"}]}

Example input:
Sentence: Daily exposure to PMcoarse , PM2 .

Example answer:
{"entities": []}

Example input:
Sentence: The soil dust is the largest contributor to HMCR , being driven by the high impact of soil dust on PM2 .

Example answer:
{"entities": []}

Example input:
Sentence: PaO2 / FiO2 increased significantly at H24 .

Example answer:
{"entities": [{"text": "PaO2 / FiO2", "type": "HealthCareActivity"}]}

Example input:
Sentence: For example , a 10 μg / m³ increase of 7 - day ( lag 06 ) average concentrations of PM10 ( particulate matter no greater than 10 microns ) , SO₂ , NO₂ was associated with 0 .

Example answer:
{"entities": []}

Example input:
Sentence: On average , a 1μg / m ( 3 ) increase in PM10 was associated with cumulative increases of 0 . 26893 , 0 . 30437 , and 0 . 21924 YLL for non - accidental , respiratory , and cardiovascular mortality , respectively , referring to 20μg / m ( 3 ) .

Example answer:
{"entities": []}

Example input:
Sentence: This study focused on the proportion of mortality due to lung cancer and cardiopulmonary diseases attributable to PM2 .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "cardiopulmonary diseases", "type": "BiologicFunction"}]}

Input:
Sentence: Increased levels of PM2 .

## Item MedMentions:test:1710
Example input:
Sentence: Population -wide prevention , especially the promotion of lifestyle improvements , is critical to reducing the morbidity of new - onset hypertension .

Example answer:
{"entities": [{"text": "Population", "type": "PopulationGroup"}, {"text": "promotion", "type": "HealthCareActivity"}]}

Example input:
Sentence: The establishment of a prominent pro - inflammatory immune response after " LbSapSal " immunization supported the increased levels of nitric oxide production , favoring a reduction in spleen parasitism ( 78 . 9 % ) and indicating long - lasting protection against L .

Example answer:
{"entities": [{"text": "immune response", "type": "BiologicFunction"}, {"text": "LbSapSal", "type": "Chemical"}, {"text": "immunization", "type": "HealthCareActivity"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "spleen", "type": "AnatomicalStructure"}]}

Example input:
Sentence: However , helminth infection can also be detrimental in reducing vaccine responses , increasing susceptibility to co - infection , and potentially reducing tumor immunosurveillance .

Example answer:
{"entities": [{"text": "helminth infection", "type": "BiologicFunction"}, {"text": "susceptibility", "type": "ClinicalAttribute"}, {"text": "co - infection", "type": "BiologicFunction"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "immunosurveillance", "type": "BiologicFunction"}]}

Example input:
Sentence: Vaccination plays an important role in protecting Atlantic salmon against the bacterial pathogen Yersinia ruckeri , but , in recent years , there has been an increasing incidence of vaccine breakdown in salmon .

Example answer:
{"entities": [{"text": "Vaccination", "type": "HealthCareActivity"}, {"text": "Atlantic salmon", "type": "Eukaryote"}, {"text": "bacterial", "type": "Bacterium"}, {"text": "Yersinia ruckeri", "type": "Bacterium"}, {"text": "vaccine", "type": "Chemical"}, {"text": "salmon", "type": "Eukaryote"}]}

Example input:
Sentence: In Portugal , there is a lack of knowledge of the current epidemiological situation , as the unique toxoplasmosis National Serological Survey was performed in 1979 / 1980 .

Example answer:
{"entities": [{"text": "Portugal", "type": "SpatialConcept"}, {"text": "toxoplasmosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Toxoplasma gondii seroprevalence in the Portuguese population : comparison of three cross - sectional studies spanning three decades Toxoplasma gondii is an obligate intracellular protozoan infecting up to one - third of the world 's population , constituting a life threat if transmitted from mother to child during pregnancy .

Example answer:
{"entities": [{"text": "Toxoplasma gondii", "type": "Eukaryote"}, {"text": "seroprevalence", "type": "ResearchActivity"}, {"text": "Portuguese population", "type": "PopulationGroup"}, {"text": "cross - sectional studies", "type": "ResearchActivity"}, {"text": "intracellular", "type": "SpatialConcept"}, {"text": "protozoan", "type": "Eukaryote"}, {"text": "world 's population", "type": "PopulationGroup"}, {"text": "life threat", "type": "Finding"}, {"text": "pregnancy", "type": "BiologicFunction"}]}

Example input:
Sentence: Cerebral toxoplasmosis is still a very relevant neurological disease in individuals with AIDS admitted to neurology emergency departments .

Example answer:
{"entities": [{"text": "Cerebral toxoplasmosis", "type": "BiologicFunction"}, {"text": "neurological disease", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "AIDS", "type": "BiologicFunction"}, {"text": "admitted", "type": "HealthCareActivity"}, {"text": "neurology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "emergency departments", "type": "Organization"}]}

Example input:
Sentence: Cerebral toxoplasmosis led to the diagnosis of infection by the human immunodeficiency virus ( HIV ) in 27 ( 48 . 2 % ) of the patients , while 29 ( 51 .

Example answer:
{"entities": [{"text": "Cerebral toxoplasmosis", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "human immunodeficiency virus", "type": "Virus"}, {"text": "HIV", "type": "Virus"}]}

Example input:
Sentence: Fifty ( 89 . 3 % ) patients underwent first - line treatment for toxoplasmosis .

Example answer:
{"entities": [{"text": "first - line treatment", "type": "HealthCareActivity"}, {"text": "toxoplasmosis", "type": "BiologicFunction"}]}

Example input:
Sentence: The scenario observed for the latter indicates that more than 80 % of childbearing women are susceptible to primary infection yielding a risk of congenital toxoplasmosis and respective sequelae .

Example answer:
{"entities": [{"text": "childbearing", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "congenital toxoplasmosis", "type": "BiologicFunction"}, {"text": "sequelae", "type": "BiologicFunction"}]}

Input:
Sentence: Since there is no vaccine to prevent human toxoplasmosis , the improvement of primary prevention constitutes a major tool to avoid infection in such susceptible groups .

## Item MedMentions:test:1857
Example input:
Sentence: The autohydrolyzed chips absorbed more NaOH in impregnation that resulted in a low NaOH concentration in the bulk impregnation liquor

Example answer:
{"entities": [{"text": "NaOH", "type": "Chemical"}]}

Example input:
Sentence: Satisfactory results were obtained overall , with a classification rate of 100 % in the discrimination of the type of barrel used during wine maturing , a normalized NRMSE of 0 .

Example answer:
{"entities": [{"text": "classification", "type": "IntellectualProduct"}, {"text": "wine", "type": "Food"}]}

Example input:
Sentence: Further research should deepen into the metabolisms mostly altered due to wine conditions to elucidate the role of each mechanism in the O .

Example answer:
{"entities": [{"text": "metabolisms", "type": "BiologicFunction"}, {"text": "wine", "type": "Food"}, {"text": "O .", "type": "Bacterium"}]}

Example input:
Sentence: ( i . e . , the impregnation liquor outside wood chips ) , while the concentration in the entrapped liquor ( i . e . , the impregnation liquor inside wood chips ) was increased .

Example answer:
{"entities": [{"text": "entrapped", "type": "Finding"}]}

Example input:
Sentence: Essential oils ( EOs ) treatment lowered the total viable counts , yeast , and mold to 1 . 54 , 2 . 36 , and 2 .

Example answer:
{"entities": [{"text": "Essential oils", "type": "Chemical"}, {"text": "EOs", "type": "Chemical"}, {"text": "yeast", "type": "Eukaryote"}, {"text": "mold", "type": "Eukaryote"}]}

Example input:
Sentence: It also resulted in an increase on a ( * ) and C ( * ) but a decrease on L ( * ) , b ( * ) , and H ( * ) of the wine .

Example answer:
{"entities": [{"text": "wine", "type": "Food"}]}

Example input:
Sentence: Quercetin - 3 - O - glucuronide , myricetin - 3 - O - galactoside , chlorogenic acid , and quercetin exerted a more important effect on the color alteration in wine .

Example answer:
{"entities": [{"text": "Quercetin - 3 - O - glucuronide", "type": "Chemical"}, {"text": "myricetin - 3 - O - galactoside", "type": "Chemical"}, {"text": "chlorogenic acid", "type": "Chemical"}, {"text": "quercetin", "type": "Chemical"}, {"text": "wine", "type": "Food"}]}

Example input:
Sentence: The wine was macerated with oak chips ( 2 or 5 g / L under light or medium toasting level ) for 20 d and then bottle - aged for 6 mo .

Example answer:
{"entities": [{"text": "wine", "type": "Food"}, {"text": "oak chips", "type": "Eukaryote"}]}

Example input:
Sentence: Effect of Oak Chips on Evolution of Phenolic Compounds and Color Attributes of Bog Bilberry Syrup Wine During Bottle - Aging This study investigated the evolution of phenolic compounds of bog bilberry syrup wine during a bottle - aging process , and further estimated the oak chip treatment on the wine color alteration .

Example answer:
{"entities": [{"text": "Oak Chips", "type": "Eukaryote"}, {"text": "Phenolic Compounds", "type": "Chemical"}, {"text": "Bog Bilberry", "type": "Eukaryote"}, {"text": "Syrup", "type": "Food"}, {"text": "Wine", "type": "Food"}, {"text": "phenolic compounds", "type": "Chemical"}, {"text": "bog bilberry", "type": "Eukaryote"}, {"text": "syrup", "type": "Food"}, {"text": "wine", "type": "Food"}, {"text": "oak chip", "type": "Eukaryote"}]}

Example input:
Sentence: Results showed that the oak chip treatment significantly increased the content of phenolic compounds and enhanced the copigmented anthocyanin level before aging .

Example answer:
{"entities": [{"text": "oak chip", "type": "Eukaryote"}, {"text": "phenolic compounds", "type": "Chemical"}, {"text": "anthocyanin", "type": "Chemical"}]}

Input:
Sentence: The oak chip treatment delayed the wine color change and its effect was mainly depended on the addition amount .

## Item MedMentions:test:1983
Example input:
Sentence: Results consistently showed that the survival processing effect persisted under low load but vanished when the number of items held in working memory increased beyond one , irrespective of processing demands .

Example answer:
{"entities": [{"text": "survival processing", "type": "BiologicFunction"}, {"text": "working memory", "type": "BiologicFunction"}]}

Example input:
Sentence: 1 for other physical conditions , and 0 . 30 ± 0 .

Example answer:
{"entities": []}

Example input:
Sentence: In every subtitle , the functional status was evaluated as 0 for the worst functional status and 4 for the best functional status .

Example answer:
{"entities": [{"text": "functional status", "type": "Finding"}, {"text": "evaluated", "type": "HealthCareActivity"}]}

Example input:
Sentence: on low ( i . e . , single - item ) load under time - sharing processing conditions .

Example answer:
{"entities": []}

Example input:
Sentence: Strength - duration curves were performed to identify the optimal output , starting at 25 mA with a pulse width of 10 milliseconds .

Example answer:
{"entities": [{"text": "Strength - duration curves", "type": "HealthCareActivity"}, {"text": "output", "type": "HealthCareActivity"}]}

Example input:
Sentence: 37 to 11 . 58 ) ; p < 0 . 0001 ) than those persistent .

Example answer:
{"entities": []}

Example input:
Sentence: 01 ( 4 . 89 ; 5 . 13 ) with 98 . 8 % ( 97 . 3 % ; 100 % ) assigning none = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: We derive the basic reproduction ratio [ Formula : see text ] and establish a threshold type result on the global dynamics in terms of [ Formula : see text ] , that is , the unique disease - free periodic solution is globally asymptotically stable if [ Formula : see text ] ; and the model system admits a unique positive periodic solution which is globally asymptotically stable if [ Formula : see text ] .

Example answer:
{"entities": [{"text": "Formula", "type": "IntellectualProduct"}, {"text": "model system", "type": "IntellectualProduct"}]}

Example input:
Sentence: In fact , based on the coefficient of determination ( R ( 2 ) ) value , the best model demonstrated the power of the pollinization on the tree productivity ( R ( 2 ) = 0 . 846 ) .

Example answer:
{"entities": [{"text": "model", "type": "IntellectualProduct"}, {"text": "pollinization", "type": "BiologicFunction"}]}

Example input:
Sentence: All formulas exhibited an area under the receiver operating characteristic curve below 0 .

Example answer:
{"entities": [{"text": "formulas", "type": "IntellectualProduct"}]}

Input:
Sentence: Under all conditions , output could be maintained within 0 .

## Item MedMentions:test:1377
Example input:
Sentence: Respiratory failure secondary to progressive obstructive lung disease during infancy may be the presenting phenotype of FLNA - associated periventricular nodular heterotopia .

Example answer:
{"entities": [{"text": "Respiratory failure", "type": "BiologicFunction"}, {"text": "obstructive lung disease", "type": "BiologicFunction"}, {"text": "FLNA - associated periventricular nodular heterotopia", "type": "BiologicFunction"}]}

Example input:
Sentence: The preferential sparing achievable with intensity - modulated radiotherapy ( IMRT ) of key swallowing structures implicated in post - radiation dysfunction , such as the pharyngeal constrictor muscles ( PCM ) , has generated significant research into toxicity - mitigating strategies .

Example answer:
{"entities": [{"text": "intensity - modulated radiotherapy", "type": "HealthCareActivity"}, {"text": "IMRT", "type": "HealthCareActivity"}, {"text": "swallowing structures", "type": "BiologicFunction"}, {"text": "pharyngeal constrictor muscles", "type": "AnatomicalStructure"}, {"text": "PCM", "type": "AnatomicalStructure"}, {"text": "research", "type": "ResearchActivity"}]}

Example input:
Sentence: Central PNETs show a spectrum of morphologic features that overlaps with CNS tumors but lack EWSR1 rearrangement s .

Example answer:
{"entities": [{"text": "Central PNETs", "type": "BiologicFunction"}, {"text": "CNS", "type": "BodySystem"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "EWSR1", "type": "AnatomicalStructure"}, {"text": "rearrangement", "type": "BiologicFunction"}]}

Example input:
Sentence: Surgery of the parapharyngeal space can cause injury to the sympathetic trunk , responsible for Horner 's syndrome , as in our patient .

Example answer:
{"entities": [{"text": "Surgery", "type": "HealthCareActivity"}, {"text": "parapharyngeal space", "type": "SpatialConcept"}, {"text": "cause injury", "type": "Finding"}, {"text": "sympathetic trunk", "type": "AnatomicalStructure"}, {"text": "Horner 's syndrome", "type": "BiologicFunction"}]}

Example input:
Sentence: Using NGS , we identify distinct mechanisms for development of metachronous or synchronous neoplasms in patients with IPMN .

Example answer:
{"entities": [{"text": "metachronous", "type": "BiologicFunction"}, {"text": "synchronous neoplasms", "type": "BiologicFunction"}, {"text": "IPMN", "type": "BiologicFunction"}]}

Example input:
Sentence: To characterize the effect of MDO on key components of sleep architecture in infants with PRS .

Example answer:
{"entities": [{"text": "MDO", "type": "HealthCareActivity"}, {"text": "sleep", "type": "BiologicFunction"}, {"text": "PRS", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Paradoxical physiological responses to propranolol in a Rett syndrome patient : a case report Rett Syndrome ( RTT ) , caused by a loss - of - function in the epigenetic modulator : X - linked methyl - CpG binding protein 2 ( MeCP2 ) , is a pervasive neurological disorder characterized by compromised brain functions , anxiety , severe mental retardation , language and learning disabilities , repetitive stereotyped hand movements and developmental regression .

Example answer:
{"entities": [{"text": "propranolol", "type": "Chemical"}, {"text": "Rett syndrome", "type": "BiologicFunction"}, {"text": "Rett Syndrome", "type": "BiologicFunction"}, {"text": "RTT", "type": "BiologicFunction"}, {"text": "loss - of - function in the epigenetic modulator", "type": "BiologicFunction"}, {"text": "X - linked methyl - CpG binding protein 2", "type": "Chemical"}, {"text": "MeCP2", "type": "Chemical"}, {"text": "neurological disorder", "type": "BiologicFunction"}, {"text": "anxiety", "type": "Finding"}, {"text": "mental retardation", "type": "BiologicFunction"}, {"text": "language", "type": "BiologicFunction"}, {"text": "learning disabilities", "type": "BiologicFunction"}, {"text": "repetitive stereotyped hand movements", "type": "BiologicFunction"}, {"text": "developmental regression", "type": "BiologicFunction"}]}

Example input:
Sentence: Making extra teeth : Lessons from a TRPS1 mutation A Thai mother and her two daughters were affected with tricho - rhino - phalangeal syndrome type I .

Example answer:
{"entities": [{"text": "extra teeth", "type": "Finding"}, {"text": "TRPS1", "type": "AnatomicalStructure"}, {"text": "mutation", "type": "BiologicFunction"}, {"text": "Thai", "type": "PopulationGroup"}, {"text": "tricho - rhino - phalangeal syndrome type I", "type": "BiologicFunction"}]}

Example input:
Sentence: Rubinstein - Taybi Syndrome Associated with Pituitary Macroadenoma : A Case Report Rubinstein - Taybi Syndrome ( RSTS ) is an autosomal dominant disorder that is classically characterized by prenatal and postnatal growth restriction , microcephaly , dysmorphic craniofacial features , broad thumbs and toes , and intellectual disability .

Example answer:
{"entities": [{"text": "Rubinstein - Taybi Syndrome", "type": "BiologicFunction"}, {"text": "Pituitary Macroadenoma", "type": "BiologicFunction"}, {"text": "Case Report", "type": "IntellectualProduct"}, {"text": "RSTS", "type": "BiologicFunction"}, {"text": "autosomal dominant disorder", "type": "BiologicFunction"}, {"text": "growth restriction", "type": "BiologicFunction"}, {"text": "microcephaly", "type": "AnatomicalStructure"}, {"text": "dysmorphic craniofacial features", "type": "AnatomicalStructure"}, {"text": "broad thumbs", "type": "Finding"}, {"text": "toes", "type": "Finding"}, {"text": "intellectual disability", "type": "BiologicFunction"}]}

Example input:
Sentence: MDO improve s several sleep architecture parameters in this sample of infants with PRS .

Example answer:
{"entities": [{"text": "MDO", "type": "HealthCareActivity"}, {"text": "improve", "type": "Finding"}, {"text": "sleep", "type": "BiologicFunction"}, {"text": "PRS", "type": "AnatomicalStructure"}]}

Input:
Sentence: Sleep architecture in Pierre - Robin sequence : The effect of mandibular distraction osteogenesis Pierre - Robin Sequence ( PRS ) , a triad of micro / retrognathia , glossoptosis , and upper airway obstruction , usually in conjunction with a cleft palate is frequently associated with significant morbidity .

## Item MedMentions:test:1545
Example input:
Sentence: Two ( 3 . 5 % ) , 15 ( 25 . 9 % ) , and 41 ( 70 . 7 % ) patients having sentinel nodes underwent total gastrectomy , proximal gastrectomy ( PG ) , and distal gastrectomy ( DG ) , respectively , in the SNM group .

Example answer:
{"entities": [{"text": "sentinel nodes", "type": "AnatomicalStructure"}, {"text": "gastrectomy", "type": "HealthCareActivity"}, {"text": "proximal gastrectomy", "type": "HealthCareActivity"}, {"text": "PG", "type": "HealthCareActivity"}, {"text": "distal gastrectomy", "type": "HealthCareActivity"}, {"text": "DG", "type": "HealthCareActivity"}, {"text": "SNM", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients with a lower Osserman stage and those with / without thymomas had favourable outcomes .

Example answer:
{"entities": [{"text": "Osserman stage", "type": "BiologicFunction"}, {"text": "thymomas", "type": "BiologicFunction"}]}

Example input:
Sentence: 52 cases , all females who underwent modified radical mastectomy at a tertiary care hospital over a period of 3 years , were evaluated .

Example answer:
{"entities": [{"text": "radical mastectomy", "type": "HealthCareActivity"}, {"text": "tertiary care hospital", "type": "Organization"}]}

Example input:
Sentence: Upon completion of the literature review , eight GS cases were found to have been treated surgically with the minimum patient age being 9 years .

Example answer:
{"entities": [{"text": "literature review", "type": "IntellectualProduct"}, {"text": "GS", "type": "BiologicFunction"}, {"text": "surgically", "type": "HealthCareActivity"}]}

Example input:
Sentence: Non - intubated subxiphoid uniportal video - assisted thoracoscopic thymectomy using glasses - free 3D vision Trans - sternal thymectomy has long been accepted as the standard surgical procedure for thymic masses .

Example answer:
{"entities": [{"text": "Non - intubated", "type": "HealthCareActivity"}, {"text": "subxiphoid", "type": "SpatialConcept"}, {"text": "uniportal video - assisted thoracoscopic thymectomy", "type": "HealthCareActivity"}, {"text": "glasses - free", "type": "Finding"}, {"text": "3D", "type": "SpatialConcept"}, {"text": "vision", "type": "BiologicFunction"}, {"text": "Trans - sternal thymectomy", "type": "HealthCareActivity"}, {"text": "surgical procedure", "type": "HealthCareActivity"}, {"text": "thymic masses", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Severe Preeclampsia in the Setting of Myasthenia Gravis Myasthenia gravis ( MG ) is a rare autoimmune disease that leads to progressive muscle weakness and is common during female reproductive years .

Example answer:
{"entities": [{"text": "Severe Preeclampsia", "type": "BiologicFunction"}, {"text": "Myasthenia Gravis", "type": "BiologicFunction"}, {"text": "Myasthenia gravis", "type": "BiologicFunction"}, {"text": "MG", "type": "BiologicFunction"}, {"text": "autoimmune disease", "type": "BiologicFunction"}, {"text": "muscle weakness", "type": "Finding"}, {"text": "reproductive", "type": "BiologicFunction"}]}

Example input:
Sentence: We aimed to describe the clinical outcomes of MG patients who underwent a thymectomy and the factors affecting these outcomes .

Example answer:
{"entities": [{"text": "clinical outcomes", "type": "Finding"}, {"text": "MG", "type": "BiologicFunction"}, {"text": "thymectomy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Although a few studies have described the role of a thymectomy in the treatment of MG in Asians countries , there are no published data on the application of this surgical approach for MG in Malaysia .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "thymectomy", "type": "HealthCareActivity"}, {"text": "MG", "type": "BiologicFunction"}, {"text": "Asians countries", "type": "SpatialConcept"}, {"text": "application", "type": "HealthCareActivity"}, {"text": "Malaysia", "type": "SpatialConcept"}]}

Example input:
Sentence: A thymectomy seems to be an effective treatment for MG , with low surgical morbidity .

Example answer:
{"entities": [{"text": "thymectomy", "type": "HealthCareActivity"}, {"text": "MG", "type": "BiologicFunction"}, {"text": "surgical", "type": "HealthCareActivity"}]}

Example input:
Sentence: This was a retrospective study involving 16 patients with MG who underwent a thymectomy at the Hospital Universiti Sains Malaysia ( HUSM ) from January 2002 until December 2012 , with a follow - up period ranging from 3 - 120 months .

Example answer:
{"entities": [{"text": "retrospective study", "type": "ResearchActivity"}, {"text": "MG", "type": "BiologicFunction"}, {"text": "thymectomy", "type": "HealthCareActivity"}, {"text": "Hospital Universiti Sains Malaysia", "type": "Organization"}, {"text": "HUSM", "type": "Organization"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Input:
Sentence: Thymectomy for Myasthenia Gravis : A 10 - year Review of Cases at the Hospital Universiti Sains Malaysia A thymectomy is considered effective for patients with myasthenia gravis ( MG ) .

## Item MedMentions:test:1751
Example input:
Sentence: The combined results of univariate and multivariate Cox regression analysis showed that the SNP in ERCC1 - 118 was closely associated with survival time .

Example answer:
{"entities": [{"text": "multivariate Cox regression analysis", "type": "IntellectualProduct"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "ERCC1 - 118", "type": "AnatomicalStructure"}, {"text": "survival time", "type": "ClinicalAttribute"}]}

Example input:
Sentence: A parsimonious mortality prediction model using data from multiple cohorts in developed and developing countries can be used to predict mortality in older adults in both settings .

Example answer:
{"entities": [{"text": "mortality prediction model", "type": "IntellectualProduct"}, {"text": "cohorts", "type": "PopulationGroup"}]}

Example input:
Sentence: Five - year survival outcomes were evaluated using Kaplan - Meier and Cox models .

Example answer:
{"entities": [{"text": "Kaplan - Meier", "type": "ResearchActivity"}, {"text": "Cox models", "type": "IntellectualProduct"}]}

Example input:
Sentence: A multivariable Cox proportional hazards model was used to estimate the primary composite outcome of stroke , transient ischaemic attack ( TIA ) and mortality associated with non - persistence .

Example answer:
{"entities": [{"text": "multivariable Cox proportional hazards model", "type": "IntellectualProduct"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "transient ischaemic attack", "type": "BiologicFunction"}, {"text": "TIA", "type": "BiologicFunction"}, {"text": "non - persistence", "type": "Finding"}]}

Example input:
Sentence: Univariate and multivariate survival analyses were conducted using the Cox proportional hazards regression methodology .

Example answer:
{"entities": [{"text": "multivariate survival analyses", "type": "ResearchActivity"}, {"text": "Cox proportional hazards regression methodology", "type": "IntellectualProduct"}]}

Example input:
Sentence: Univariable and multivariable Cox regression analyses tested the effect of different histopathological variant on recurrence , cancer - specific mortality ( CSM ) , and overall mortality ( OM ) after accounting for all available confounders .

Example answer:
{"entities": [{"text": "Univariable and multivariable Cox regression analyses", "type": "IntellectualProduct"}]}

Example input:
Sentence: Multivariate Cox model was performed to identify the impact of molecular subtype and other prognostic factors on OS .

Example answer:
{"entities": [{"text": "subtype", "type": "IntellectualProduct"}, {"text": "prognostic factors", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Four variables were consistently associated with mortality in the logistic regression model and had adequate prediction value ( Hosmer and Lemeshow statistic = 0 . 760 ; Nagelkerke R - squared = 0 . 494 ) .

Example answer:
{"entities": [{"text": "logistic regression model", "type": "IntellectualProduct"}]}

Example input:
Sentence: We performed an individual participant data meta - analysis using a sex - stratified Cox proportional hazards model , with time to death as the time scale .

Example answer:
{"entities": [{"text": "individual", "type": "PopulationGroup"}, {"text": "participant", "type": "PopulationGroup"}, {"text": "meta - analysis", "type": "ResearchActivity"}, {"text": "sex - stratified Cox proportional hazards model", "type": "IntellectualProduct"}]}

Example input:
Sentence: Kaplan - Meier and multivariate Cox proportional hazards modeling was conducted for time to readmission and death over 5 years .

Example answer:
{"entities": [{"text": "multivariate Cox proportional hazards modeling", "type": "IntellectualProduct"}, {"text": "readmission", "type": "HealthCareActivity"}, {"text": "death", "type": "Finding"}]}

Input:
Sentence: Multivariate models for death at 3 months and death over time were developed using logistic regression and Cox modeling , respectively .

## Item MedMentions:test:1754
Example input:
Sentence: Twenty - one percent of patients showed abnormal plasma glucose level .

Example answer:
{"entities": [{"text": "abnormal", "type": "Finding"}, {"text": "plasma glucose level", "type": "Finding"}]}

Example input:
Sentence: Glycemic control was assessed with glycosylated hemoglobin ( HbA1c ) at baseline and six months later .

Example answer:
{"entities": [{"text": "Glycemic control", "type": "HealthCareActivity"}, {"text": "glycosylated hemoglobin", "type": "Chemical"}, {"text": "HbA1c", "type": "Chemical"}]}

Example input:
Sentence: In vivo testing indicates that a single patch can regulate glucose levels effectively with reduced risk of hypoglycemia .

Example answer:
{"entities": [{"text": "In vivo", "type": "SpatialConcept"}, {"text": "patch", "type": "Chemical"}, {"text": "glucose levels", "type": "Finding"}, {"text": "hypoglycemia", "type": "BiologicFunction"}]}

Example input:
Sentence: The achievement of primary composite outcome ( four out of seven fasting plasma glucose [ FPG ] within 5 - 7 . 2 mmol / L + mean for three consecutive FPG within 5 - 7 . 2 mmol / L + no severe hypoglycemia ) was 15 % in LTHome versus 41 % in EUT ( noninferiority not met , P - value = 0 . 92 ) .

Example answer:
{"entities": [{"text": "fasting plasma glucose [ FPG ]", "type": "Finding"}, {"text": "FPG", "type": "Finding"}, {"text": "no", "type": "Finding"}, {"text": "hypoglycemia", "type": "BiologicFunction"}, {"text": "LTHome", "type": "IntellectualProduct"}, {"text": "EUT", "type": "HealthCareActivity"}]}

Example input:
Sentence: As compared with subjects with 1 - hour post - load glucose < 155 mg / dl , individuals with 1 - hour post - load glucose ≥155 mg / dl exhibited a significantly worse cardio metabolic profile , both in the group with HbA1c < 5 . 7 % , and in the group with prediabetes ( HbA1c 5 . 7 - 6 . 4 % ) .

Example answer:
{"entities": [{"text": "individuals", "type": "PopulationGroup"}, {"text": "cardio metabolic profile", "type": "BiologicFunction"}, {"text": "group", "type": "PopulationGroup"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "prediabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Preoperative abnormalities in glucose homeostasis were confirmed in 64 ( 47 % ) patients .

Example answer:
{"entities": [{"text": "abnormalities", "type": "Finding"}, {"text": "glucose homeostasis", "type": "BiologicFunction"}]}

Example input:
Sentence: In a randomized triple - blind controlled clinical trial , 120 adults with impaired glucose tolerance based on the inclusion criteria will be selected by a simple random sampling method and will be randomly allocated to 6 months of 6 g / d probiotic , synbiotic or placebo .

Example answer:
{"entities": [{"text": "randomized triple - blind controlled clinical trial", "type": "ResearchActivity"}, {"text": "impaired glucose tolerance", "type": "BiologicFunction"}, {"text": "sampling method", "type": "IntellectualProduct"}, {"text": "probiotic", "type": "Bacterium"}, {"text": "synbiotic", "type": "Food"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: Herein , we evaluated whether 1 - hour post - load plasma glucose ≥155 mg / dl combined with HbA1c may identify pre - diabetic individuals with a higher cardio - metabolic risk .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: The incremental AUC ( iAUC ) for 24 h glucose ( primary outcome ) and insulin resistance ( HOMA2 - IR ) were assessed on days 4 and 5 , respectively .

Example answer:
{"entities": [{"text": "glucose", "type": "Chemical"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "HOMA2 - IR", "type": "BiologicFunction"}]}

Example input:
Sentence: Infusion of Ex - 9 decreased the time to peak glucose and rate of glucose decline during OGTT , and raised the postprandial nadir by over 70 % , normalising it relative to NSCs and preventing hypoglycaemia in all PBH participants .

Example answer:
{"entities": [{"text": "Infusion", "type": "HealthCareActivity"}, {"text": "Ex - 9", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "OGTT", "type": "HealthCareActivity"}, {"text": "hypoglycaemia", "type": "BiologicFunction"}, {"text": "PBH", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}]}

Input:
Sentence: Indoor records of 146 patients on multi - centered protocol - 841 were evaluated for any alteration in plasma glucose level , time of onset of hypo / hyperglycemia , and persistence of plasma glucose alteration .

## Item MedMentions:test:1877
Example input:
Sentence: Association of Low Ficolin - Lectin Pathway Parameters with Cardiac Syndrome X In patients with typical angina pectoris , inducible myocardial ischaemia and macroscopically normal coronaries ( cardiac syndrome X ( CSX ) ) , a significantly elevated plasma level of terminal complement complex ( TCC ) , the common end product of complement activation , has been observed without accompanying activation of the classical or the alternative pathways .

Example answer:
{"entities": [{"text": "Ficolin", "type": "Chemical"}, {"text": "Lectin", "type": "Chemical"}, {"text": "Pathway", "type": "BiologicFunction"}, {"text": "Cardiac Syndrome X", "type": "BiologicFunction"}, {"text": "typical angina pectoris", "type": "Finding"}, {"text": "myocardial ischaemia", "type": "BiologicFunction"}, {"text": "coronaries", "type": "AnatomicalStructure"}, {"text": "cardiac syndrome X", "type": "BiologicFunction"}, {"text": "CSX", "type": "BiologicFunction"}, {"text": "plasma", "type": "BodySubstance"}, {"text": "terminal complement complex", "type": "Chemical"}, {"text": "TCC", "type": "Chemical"}, {"text": "complement activation", "type": "BiologicFunction"}, {"text": "classical", "type": "BiologicFunction"}, {"text": "alternative pathways", "type": "BiologicFunction"}]}

Example input:
Sentence: Hemorrhagic sarcoid pleural effusion : A rare entity Involvement of pleura by sarcoidosis remains a rare manifestation and varies from pleural effusion , pneumothorax , pleural thickening , hydropneumothorax , trapped lung , hemothorax , or chylothorax .

Example answer:
{"entities": [{"text": "sarcoid", "type": "BiologicFunction"}, {"text": "pleural effusion", "type": "BiologicFunction"}, {"text": "pleura", "type": "AnatomicalStructure"}, {"text": "sarcoidosis", "type": "BiologicFunction"}, {"text": "pneumothorax", "type": "BiologicFunction"}, {"text": "pleural thickening", "type": "BiologicFunction"}, {"text": "hydropneumothorax", "type": "Finding"}, {"text": "trapped lung", "type": "BiologicFunction"}, {"text": "hemothorax", "type": "BiologicFunction"}, {"text": "chylothorax", "type": "BiologicFunction"}]}

Example input:
Sentence: Utility of Post - Mortem Genetic Testing in Cases of Sudden Arrhythmic Death Syndrome Sudden arrhythmic death syndrome ( SADS ) describes a sudden death with negative autopsy and toxicological analysis .

Example answer:
{"entities": [{"text": "Post - Mortem", "type": "HealthCareActivity"}, {"text": "Genetic Testing", "type": "ResearchActivity"}, {"text": "Sudden Arrhythmic Death Syndrome", "type": "BiologicFunction"}, {"text": "Sudden arrhythmic death syndrome", "type": "BiologicFunction"}, {"text": "SADS", "type": "BiologicFunction"}, {"text": "sudden death", "type": "BiologicFunction"}, {"text": "autopsy", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Pathophysiology , treatment and prevention of ovarian hyperstimulation syndrome Severe ovarian hyperstimulation syndrome ( OHSS ) is an iatrogenic condition that affects 1 % of women that undergo treatment with assisted reproductive technology .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "prevention", "type": "HealthCareActivity"}, {"text": "ovarian hyperstimulation syndrome", "type": "BiologicFunction"}, {"text": "OHSS", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "assisted reproductive technology", "type": "HealthCareActivity"}]}

Example input:
Sentence: In nonsyndromic patients , the aortic root is the slowest growing portion of the thoracic aorta .

Example answer:
{"entities": [{"text": "nonsyndromic", "type": "Finding"}, {"text": "aortic root", "type": "SpatialConcept"}, {"text": "growing", "type": "BiologicFunction"}, {"text": "portion", "type": "SpatialConcept"}, {"text": "thoracic aorta", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Medical records from patients who suffered serious AEs ( major bleed , embolic stroke , venous thromboembolism ) were reviewed , and AMS staff were interviewed to determine the root cause using the " 5 Whys " technique .

Example answer:
{"entities": [{"text": "Medical records", "type": "IntellectualProduct"}, {"text": "AEs", "type": "BiologicFunction"}, {"text": "major bleed", "type": "BiologicFunction"}, {"text": "embolic stroke", "type": "BiologicFunction"}, {"text": "venous thromboembolism", "type": "BiologicFunction"}, {"text": "AMS", "type": "Organization"}, {"text": "staff", "type": "ProfessionalOrOccupationalGroup"}, {"text": "\" 5 Whys \" technique", "type": "IntellectualProduct"}]}

Example input:
Sentence: The effectiveness and mechanism of RIPC with respect to myocardial IRI in children with tetralogy of Fallot ( ToF ) , a severe cyanotic congenital cardiac disease , undergoing open heart surgery are unclear .

Example answer:
{"entities": [{"text": "RIPC", "type": "HealthCareActivity"}, {"text": "myocardial", "type": "AnatomicalStructure"}, {"text": "IRI", "type": "InjuryOrPoisoning"}, {"text": "tetralogy of Fallot", "type": "AnatomicalStructure"}, {"text": "ToF", "type": "AnatomicalStructure"}, {"text": "cardiac disease", "type": "BiologicFunction"}, {"text": "open heart surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients with pulmonary embolus , suboptimal CTPA , arrhythmias or pericardial tamponade were excluded .

Example answer:
{"entities": [{"text": "pulmonary embolus", "type": "BiologicFunction"}, {"text": "CTPA", "type": "HealthCareActivity"}, {"text": "arrhythmias", "type": "Finding"}, {"text": "pericardial tamponade", "type": "BiologicFunction"}]}

Example input:
Sentence: Prevalence of Coronary Artery to Pulmonary Artery Collaterals in Patients with Chronic Thromboembolic Pulmonary Hypertension : Retrospective Analysis from a Single Center Background Our aim was to determine the prevalence of coronary artery - pulmonary artery collaterals in patients with chronic thromboembolic pulmonary hypertension ( CTEPH ) by retrospectively evaluating coronary angiograms of eligible consecutive patients who had undergone pulmonary endarterectomy ( PEA ) .

Example answer:
{"entities": [{"text": "Coronary Artery", "type": "Finding"}, {"text": "Pulmonary Artery Collaterals", "type": "AnatomicalStructure"}, {"text": "Chronic Thromboembolic Pulmonary Hypertension", "type": "BiologicFunction"}, {"text": "Retrospective Analysis", "type": "ResearchActivity"}, {"text": "coronary artery", "type": "Finding"}, {"text": "pulmonary artery collaterals", "type": "AnatomicalStructure"}, {"text": "chronic thromboembolic pulmonary hypertension", "type": "BiologicFunction"}, {"text": "CTEPH", "type": "BiologicFunction"}, {"text": "retrospectively", "type": "ResearchActivity"}, {"text": "coronary angiograms", "type": "HealthCareActivity"}, {"text": "pulmonary endarterectomy", "type": "HealthCareActivity"}, {"text": "PEA", "type": "HealthCareActivity"}]}

Example input:
Sentence: The most common diagnosis was single ventricle physiology ( 52 % ) , 9 palliated by Fontan operation and 2 by aortopulmonary shunts : d - transposition of the great arteries after Mustard / Senning ( n = 2 ) , tetralogy of Fallot ( n = 2 ) , aortic valve disease ( n = 2 ) , and other biventricular surgery ( n = 4 ) .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "single ventricle", "type": "AnatomicalStructure"}, {"text": "physiology", "type": "BiologicFunction"}, {"text": "palliated", "type": "HealthCareActivity"}, {"text": "Fontan operation", "type": "HealthCareActivity"}, {"text": "aortopulmonary shunts", "type": "HealthCareActivity"}, {"text": "d - transposition of the great arteries", "type": "AnatomicalStructure"}, {"text": "Mustard", "type": "HealthCareActivity"}, {"text": "Senning", "type": "HealthCareActivity"}, {"text": "tetralogy of Fallot", "type": "AnatomicalStructure"}, {"text": "aortic valve disease", "type": "BiologicFunction"}, {"text": "surgery", "type": "HealthCareActivity"}]}

Input:
Sentence: Arterial thoracic outlet syndrome : rare and triggering Arterial thoracic outlet syndrome ( TOS ) is the least common type of TOS .

## Item MedMentions:test:1951
Example input:
Sentence: 00001 ; OR = 35 . 57 , 95 % CI = 19 . 61 - 64 . 51 , and p < 0 . 00001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 63 , CI = 2 . 14 - 43 . 36 ) and waist / height ratio ( p = 0 . 034 , OR = 6 . 86 , CI = 1 . 25 - 37 . 61 ) , although the variations in percentages between DD and I - carriers were not high enough to conclude an effect of ACE I / D on such an association .

Example answer:
{"entities": [{"text": "waist / height ratio", "type": "Finding"}, {"text": "DD", "type": "Finding"}, {"text": "I - carriers", "type": "Finding"}, {"text": "ACE I / D", "type": "Finding"}]}

Example input:
Sentence: 44 ; 95 % CI 0 . 22 - 0 . 87 ; p = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 34 - 4 . 43 , p = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 47 . 9 cm ( 2 . 1 ) respectively ; P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 666 for the conicity index , 0 . 653 for the waist to height ratio , and 0 . 660 for the fat percentage .

Example answer:
{"entities": [{"text": "conicity index", "type": "IntellectualProduct"}, {"text": "waist to height ratio", "type": "Finding"}, {"text": "fat percentage", "type": "Finding"}]}

Example input:
Sentence: 95 , P = 0 . 001 and 89 vs .

Example answer:
{"entities": []}

Example input:
Sentence: 94 , 95 % CI : 1 . 68 - 5 . 14 , P < 0 . 001 and HR = 1 . 74 , 95 % CI : 1 . 23 - 2 . 47 , P = 0 . 002 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 94 , p < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 23 ( S = 87 . 8 ; SP = 35 . 9 ) ; for the waist to height ratio , it was 0 . 57 ( S = 79 . 6 ; SP = 45 . 6 ) ; and for the fat percentage , it was 39 . 71 ( S = 89 . 8 ; SP = 42 . 7 ) .

Example answer:
{"entities": [{"text": "waist to height ratio", "type": "Finding"}, {"text": "fat percentage", "type": "Finding"}]}

Input:
Sentence: 94 - 40 . 71 ) , waist circumference ( p = 0 .

## Item MedMentions:test:1573
Example input:
Sentence: This prospective single - center nonrandomized controlled clinical trial included 100 adult patients undergoing surgery for Stanford type A AAD at an academic hospital in China .

Example answer:
{"entities": [{"text": "single - center nonrandomized controlled clinical trial", "type": "ResearchActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "academic hospital", "type": "Organization"}, {"text": "China", "type": "SpatialConcept"}]}

Example input:
Sentence: The German Society of Pediatric Oncology and Hematology ( GPOH ) data center registered and followed patients with other diagnoses than Ewing sarcoma who were treated according to the EE99 protocol in an additional non - Ewing database .

Example answer:
{"entities": [{"text": "German Society of Pediatric Oncology and Hematology ( GPOH ) data center", "type": "Organization"}, {"text": "registered", "type": "HealthCareActivity"}, {"text": "diagnoses", "type": "Finding"}, {"text": "Ewing sarcoma", "type": "BiologicFunction"}, {"text": "treated", "type": "Finding"}, {"text": "EE99 protocol", "type": "IntellectualProduct"}, {"text": "non - Ewing database", "type": "IntellectualProduct"}]}

Example input:
Sentence: All patient specimen identification errors that occurred in the outpatient department ( OPD ) , emergency department ( ED ) , and inpatient department ( IPD ) of a 3 , 800 - bed academic medical center in Taiwan were documented and analyzed retrospectively from 2005 to 2014 .

Example answer:
{"entities": [{"text": "patient specimen", "type": "BodySubstance"}, {"text": "outpatient department", "type": "SpatialConcept"}, {"text": "OPD", "type": "SpatialConcept"}, {"text": "emergency department", "type": "Organization"}, {"text": "ED", "type": "Organization"}, {"text": "inpatient department", "type": "SpatialConcept"}, {"text": "IPD", "type": "SpatialConcept"}, {"text": "academic medical center", "type": "Organization"}, {"text": "Taiwan", "type": "SpatialConcept"}, {"text": "documented", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients with PAD / DM had the greatest increase in amputation rates from 10 per 100 patients with LE ulcer s in 2005 to 28 per 100 patients in 2013 ( P < .001 ) .

Example answer:
{"entities": [{"text": "PAD", "type": "BiologicFunction"}, {"text": "DM", "type": "BiologicFunction"}, {"text": "amputation", "type": "HealthCareActivity"}]}

Example input:
Sentence: The Nationwide Inpatient Sample and ICD - 9 - CM codes were used to identify inpatient admissions for Crohn 's disease and ulcerative colitis .

Example answer:
{"entities": [{"text": "ICD - 9 - CM codes", "type": "IntellectualProduct"}, {"text": "admissions", "type": "HealthCareActivity"}, {"text": "Crohn 's disease", "type": "BiologicFunction"}, {"text": "ulcerative colitis", "type": "BiologicFunction"}]}

Example input:
Sentence: There were 219 , 547 patients identified with an incident LE ulcer throughout the state .

Example answer:
{"entities": [{"text": "state", "type": "SpatialConcept"}]}

Example input:
Sentence: Patients with repeated hospitalizations before admission for the LE ulcer had the highest risk of amputation .

Example answer:
{"entities": [{"text": "hospitalizations", "type": "HealthCareActivity"}, {"text": "admission", "type": "HealthCareActivity"}, {"text": "risk", "type": "HealthCareActivity"}, {"text": "amputation", "type": "HealthCareActivity"}]}

Example input:
Sentence: We also attempted to create a measure of a patient 's ability to manage chronic diseases or to access appropriate outpatient care for ulcer management by accounting for hospital and emergency department ( ED ) visits in the preceding 60 days to determine how this also affects amputation - free survival .

Example answer:
{"entities": [{"text": "chronic diseases", "type": "BiologicFunction"}, {"text": "outpatient care", "type": "HealthCareActivity"}, {"text": "ulcer management", "type": "HealthCareActivity"}, {"text": "hospital", "type": "Organization"}, {"text": "emergency department", "type": "Organization"}, {"text": "ED", "type": "Organization"}, {"text": "amputation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Amputation trends for patients with lower extremity ulcers due to diabetes and peripheral artery disease using statewide data This study reports all - payer amputation rates using state -based administrative claims data for high - risk patients with lower extremity ( LE ) ulcers and concomitant peripheral artery disease ( PAD ) , diabetes mellitus ( DM ) , or combination PAD / DM .

Example answer:
{"entities": [{"text": "Amputation", "type": "HealthCareActivity"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "peripheral artery disease", "type": "BiologicFunction"}, {"text": "statewide", "type": "SpatialConcept"}, {"text": "study", "type": "ResearchActivity"}, {"text": "amputation", "type": "HealthCareActivity"}, {"text": "state", "type": "SpatialConcept"}, {"text": "risk", "type": "HealthCareActivity"}, {"text": "PAD", "type": "BiologicFunction"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "DM", "type": "BiologicFunction"}]}

Example input:
Sentence: From 2005 to 2013 , the number of patients with LE ulcers who required inpatient admission , presented to the ED , or had outpatient procedures was stable .

Example answer:
{"entities": [{"text": "admission", "type": "HealthCareActivity"}, {"text": "ED", "type": "Organization"}]}

Input:
Sentence: Patients admitted to nonfederal hospitals , seen in an ED , or treated in an eligible ambulatory surgery center within California from 2005 through 2013 with an International Classification of Diseases , Ninth Revision , Clinical Modification diagnosis code for a disease - specific LE ulcer were identified in the California Office of Statewide Health Planning and Development database .

## Item MedMentions:test:1550
Example input:
Sentence: With this practice , data scientists can develop customized analytics pipelines as APPs in Jupyter Notebook and disseminate them to other researchers easily , and researchers can benefit from the shared notebook to perform analysis tasks or reproduce research results much more easily .

Example answer:
{"entities": [{"text": "data scientists", "type": "ProfessionalOrOccupationalGroup"}, {"text": "analytics pipelines", "type": "IntellectualProduct"}, {"text": "APPs", "type": "IntellectualProduct"}, {"text": "Jupyter Notebook", "type": "IntellectualProduct"}, {"text": "disseminate", "type": "SpatialConcept"}, {"text": "researchers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "notebook", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: This cloud -based version further allows researchers to exploit the computing resources available from AWS to detect similarity in multiple large - scale DNA motif data sets resulting from the next - generation sequencing technology .

Example answer:
{"entities": [{"text": "version", "type": "IntellectualProduct"}, {"text": "researchers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "detect", "type": "Finding"}, {"text": "DNA motif", "type": "SpatialConcept"}, {"text": "data sets", "type": "IntellectualProduct"}, {"text": "next - generation sequencing technology", "type": "ResearchActivity"}]}

Example input:
Sentence: The bioinformatic analysis based on the graphical representation of the matrix of Euclidean distances , the principal components analysis , unweighted pair group method with arithmetic mean , and principal coordinate analysis ( PCoA ) revealed three major clusters which were not correlated with the geographic origin .

Example answer:
{"entities": [{"text": "bioinformatic", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "matrix of Euclidean distances", "type": "ResearchActivity"}, {"text": "unweighted pair group method", "type": "ResearchActivity"}, {"text": "principal coordinate analysis", "type": "ResearchActivity"}, {"text": "PCoA", "type": "ResearchActivity"}, {"text": "geographic", "type": "SpatialConcept"}, {"text": "origin", "type": "Finding"}]}

Example input:
Sentence: In this paper , we present a new statistical algorithm , MACHETE ( Mismatched Alignment CHimEra Tracking Engine ) , which achieves highly sensitive and specific detection of gene fusions from RNA - Seq data , including the highest Positive Predictive Value ( PPV ) compared to the current state - of - the - art , as assessed in simulated data .

Example answer:
{"entities": [{"text": "statistical algorithm", "type": "IntellectualProduct"}, {"text": "MACHETE", "type": "IntellectualProduct"}, {"text": "Mismatched Alignment CHimEra Tracking Engine )", "type": "IntellectualProduct"}, {"text": "detection", "type": "Finding"}, {"text": "gene fusions", "type": "ResearchActivity"}, {"text": "RNA - Seq data", "type": "IntellectualProduct"}]}

Example input:
Sentence: Ultra - deep sequencing has been widely used in viral quasispecies research , especially for low - frequency mutation detection .

Example answer:
{"entities": [{"text": "Ultra - deep sequencing", "type": "ResearchActivity"}, {"text": "viral quasispecies", "type": "Virus"}, {"text": "research", "type": "ResearchActivity"}, {"text": "mutation detection", "type": "HealthCareActivity"}]}

Example input:
Sentence: As proof of principle that MACHETE discovers novel gene fusions with high accuracy in vivo , we mined public data to discover and subsequently PCR validate novel gene fusions missed by other algorithms in the ovarian cancer cell line OVCAR3 .

Example answer:
{"entities": [{"text": "MACHETE", "type": "IntellectualProduct"}, {"text": "gene fusions", "type": "ResearchActivity"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "public", "type": "Organization"}, {"text": "PCR", "type": "ResearchActivity"}, {"text": "validate", "type": "ResearchActivity"}, {"text": "algorithms", "type": "IntellectualProduct"}, {"text": "ovarian cancer", "type": "BiologicFunction"}, {"text": "cell line", "type": "AnatomicalStructure"}, {"text": "OVCAR3", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A tool kit , GRADSCOPT ( GRid Accelerated Directly SCoring OPTimizing ) , was designed to allow rapid development and optimization of different knowledge - based scoring potentials for specific objectives in protein - protein docking .

Example answer:
{"entities": [{"text": "GRADSCOPT", "type": "IntellectualProduct"}, {"text": "GRid Accelerated Directly SCoring OPTimizing", "type": "IntellectualProduct"}, {"text": "knowledge - based", "type": "IntellectualProduct"}, {"text": "scoring", "type": "ResearchActivity"}, {"text": "protein - protein docking", "type": "BiologicFunction"}]}

Example input:
Sentence: com / spaces / roberts - lab - public / wiki / Biospark CONTACT : eroberts @ jhu . eduSupplementary information : Supplementary data are available at Bioinformatics online .

Example answer:
{"entities": []}

Example input:
Sentence: Biospark builds upon the open source Hadoop and Spark projects , bringing domain - specific features for biology .

Example answer:
{"entities": [{"text": "Biospark", "type": "IntellectualProduct"}, {"text": "Hadoop and Spark", "type": "IntellectualProduct"}, {"text": "domain - specific features", "type": "IntellectualProduct"}, {"text": "biology", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Here , we introduce Biospark , a new framework for performing data - parallel analysis on large numerical datasets .

Example answer:
{"entities": [{"text": "Biospark", "type": "IntellectualProduct"}, {"text": "framework", "type": "IntellectualProduct"}]}

Input:
Sentence: Biospark : scalable analysis of large numerical datasets from biological simulations and experiments using Hadoop and Spark Data - parallel programming techniques can dramatically decrease the time needed to analyze large datasets .

## Item MedMentions:test:1841
Example input:
Sentence: Unanimously , all reviews admitted to the need for prospective randomized controlled trials to help clarify the effects of NSAIDs on bone - healing .

Example answer:
{"entities": [{"text": "reviews", "type": "IntellectualProduct"}, {"text": "randomized controlled trials", "type": "ResearchActivity"}, {"text": "NSAIDs", "type": "Chemical"}, {"text": "bone - healing", "type": "Finding"}]}

Example input:
Sentence: This systematic literature review highlights the great variability in the interpretation of the literature addressing the impact of NSAIDs on bone - healing .

Example answer:
{"entities": [{"text": "systematic literature review", "type": "IntellectualProduct"}, {"text": "literature", "type": "IntellectualProduct"}, {"text": "NSAIDs", "type": "Chemical"}, {"text": "bone - healing", "type": "Finding"}]}

Example input:
Sentence: Of the 808 patients included in the final analysis , 338 ( 42 % ) were exposed to ibuprofen .

Example answer:
{"entities": [{"text": "ibuprofen", "type": "Chemical"}]}

Example input:
Sentence: Overall , 27 ( 3 % ) patients had a bone healing complication ; 8 ( 1 % ) developed nonunion , 3 ( 0 .

Example answer:
{"entities": [{"text": "bone healing", "type": "Finding"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "nonunion", "type": "Finding"}]}

Example input:
Sentence: This belief stems from multiple studies , in particular animal studies , that show delayed bone - healing or nonunions associated with NSAID exposure .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "animal studies", "type": "Eukaryote"}, {"text": "bone - healing", "type": "Finding"}, {"text": "NSAID", "type": "Chemical"}]}

Example input:
Sentence: Despite being an effective analgesic for children with fractures , some clinicians may avoid prescribing ibuprofen due to its potentially harmful effect on bone healing .

Example answer:
{"entities": [{"text": "analgesic", "type": "Chemical"}, {"text": "fractures", "type": "InjuryOrPoisoning"}, {"text": "clinicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "ibuprofen", "type": "Chemical"}, {"text": "bone healing", "type": "Finding"}]}

Example input:
Sentence: Does the Use of Ibuprofen in Children with Extremity Fractures Increase their Risk for Bone Healing Complications ?

Example answer:
{"entities": [{"text": "Ibuprofen", "type": "Chemical"}, {"text": "Bone Healing", "type": "Finding"}, {"text": "Complications", "type": "BiologicFunction"}]}

Example input:
Sentence: Children with extremity fractures who are exposed to ibuprofen do not seem to be at increased risk for clinically important bone healing complications .

Example answer:
{"entities": [{"text": "ibuprofen", "type": "Chemical"}, {"text": "bone healing", "type": "Finding"}, {"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: To determine if exposure to ibuprofen is associated with an increased risk of bone healing complications in children with fractures .

Example answer:
{"entities": [{"text": "ibuprofen", "type": "Chemical"}, {"text": "bone healing", "type": "Finding"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "fractures", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Ten ( 3 % ) patients who were exposed to ibuprofen , and 17 ( 4 % ) who were not , developed a bone healing complication ( odds ratio 0 . 8 , 95 % confidence interval 0 . 4 - 1 . 8 ; p = 0 . 61 ) .

Example answer:
{"entities": [{"text": "ibuprofen", "type": "Chemical"}, {"text": "bone healing", "type": "Finding"}, {"text": "complication", "type": "BiologicFunction"}]}

Input:
Sentence: There was no significant association between ibuprofen exposure and the development of a bone healing complication despite adjustment for potential confounders .

## Item MedMentions:test:1959
Example input:
Sentence: The data were analysed using deductive and inductive approaches through a coding framework based on the interview data and literature review , with all sections of coded data grouped into themes .

Example answer:
{"entities": [{"text": "approaches", "type": "SpatialConcept"}, {"text": "literature review", "type": "IntellectualProduct"}]}

Example input:
Sentence: First , we simulate the developmental process of acquiring phonological categories from auditory and visual cues , asking whether simple statistical learning approaches are sufficient for learning multi - modal representations .

Example answer:
{"entities": [{"text": "simulate", "type": "ResearchActivity"}, {"text": "categories", "type": "IntellectualProduct"}, {"text": "learning", "type": "BiologicFunction"}]}

Example input:
Sentence: It is suggested that a graded structure approach can greatly benefit future research into sexual definitions , by permitting variable definitions to be predicted and explained , rather than merely identified .

Example answer:
{"entities": [{"text": "graded structure", "type": "IntellectualProduct"}, {"text": "research", "type": "ResearchActivity"}, {"text": "definitions", "type": "IntellectualProduct"}]}

Example input:
Sentence: We developed multivariate classifiers to identify patterns of spectral power across the brain that independently predicted successful episodic encoding and retrieval .

Example answer:
{"entities": [{"text": "multivariate classifiers", "type": "IntellectualProduct"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "episodic encoding", "type": "BiologicFunction"}]}

Example input:
Sentence: We previously described an integrative transformation system using a drug -resistant marker for L .

Example answer:
{"entities": [{"text": "drug", "type": "Chemical"}, {"text": "marker", "type": "BiologicFunction"}, {"text": "L .", "type": "Eukaryote"}]}

Example input:
Sentence: Seven systems met our inclusion criteria , and are included in this review .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}]}

Example input:
Sentence: It attempts to unify apparently separate entities in a complex biological web , network , and system in a realistic and practical manner , i .

Example answer:
{"entities": [{"text": "complex biological", "type": "IntellectualProduct"}, {"text": "practical manner", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: We investigate this idea by implementing a computational MBRL framework that incorporates features inspired by computational properties of the hippocampus : a hierarchical representation of space , " forward sweeps " through future spatial trajectories , and context -driven remapping of place cells .

Example answer:
{"entities": [{"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "space", "type": "SpatialConcept"}, {"text": "place cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Both a hypothesis - driven judgmental approach and mathematical CART modeling were utilized for creating a diagnostic algorithm .

Example answer:
{"entities": [{"text": "mathematical CART modeling", "type": "IntellectualProduct"}]}

Example input:
Sentence: The current research offers a theoretical explanation for this hierarchy , proposing that sexual definitions display graded categorical structure , arising from goodness of membership judgments .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "explanation", "type": "IntellectualProduct"}, {"text": "definitions", "type": "IntellectualProduct"}, {"text": "graded categorical structure", "type": "IntellectualProduct"}, {"text": "judgments", "type": "BiologicFunction"}]}

Input:
Sentence: We propose a logical categorization system .

## Item MedMentions:test:1731
Example input:
Sentence: Using the METABRIC cohort we identified a16 - gene signature capable of stratifying breast cancer patients into four risk levels with intention that low - risk patients would not undergo adjuvant systemic therapy , intermediate - low - risk patients will be treated with hormonal therapy only , and intermediate -high - and high - risk groups will be treated by chemotherapy in addition to the hormonal therapy .

Example answer:
{"entities": [{"text": "METABRIC", "type": "IntellectualProduct"}, {"text": "cohort", "type": "ResearchActivity"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "systemic therapy", "type": "HealthCareActivity"}, {"text": "intermediate", "type": "SpatialConcept"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "hormonal therapy", "type": "HealthCareActivity"}, {"text": "treated", "type": "HealthCareActivity"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: A bleomycin , etoposide , and cisplatin treatment protocol targeting germ cell neoplasia lead to disease remission and prolonged survival of 34 months .

Example answer:
{"entities": [{"text": "bleomycin", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "treatment protocol", "type": "HealthCareActivity"}, {"text": "germ cell neoplasia", "type": "BiologicFunction"}, {"text": "disease remission", "type": "Finding"}]}

Example input:
Sentence: Second - line PFS of fluoropyrimidine -based chemotherapy group and gemcitabine -based chemotherapy group was 12 vs .

Example answer:
{"entities": [{"text": "Second - line", "type": "HealthCareActivity"}, {"text": "fluoropyrimidine", "type": "Chemical"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "group", "type": "PopulationGroup"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: This retrospective study analyzes the overall survival of these patients under " real life conditions " before and after the introduction of FOLFIRINOX in 2011 .

Example answer:
{"entities": [{"text": "retrospective study", "type": "ResearchActivity"}, {"text": "analyzes", "type": "ResearchActivity"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}]}

Example input:
Sentence: Chemotherapy regimens included gemcitabine alone or in association with other agents ( 44 % ) , oxaliplatin , irinotecan , fluorouracil and leucovorin ( FOLFIRINOX 8 % ) , and cisplatin , gemcitabine plus capecitabine and epirubicin ( PEXG ) or capecitabine and docetaxel ( PDXG ) or epirubicin and fluorouracil ( PEFG ) ( 48 % ) .

Example answer:
{"entities": [{"text": "Chemotherapy regimens", "type": "HealthCareActivity"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "agents", "type": "Chemical"}, {"text": "oxaliplatin", "type": "Chemical"}, {"text": "irinotecan", "type": "Chemical"}, {"text": "fluorouracil", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "capecitabine", "type": "Chemical"}, {"text": "epirubicin", "type": "Chemical"}, {"text": "PEXG", "type": "HealthCareActivity"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "PDXG", "type": "HealthCareActivity"}, {"text": "PEFG", "type": "HealthCareActivity"}]}

Example input:
Sentence: Second - line PFS of FOLFIRINOX was 20 weeks , whereas it was 14 weeks for other fuoropyrimidine -based chemotherapies ( p = 0 . 190 ) .

Example answer:
{"entities": [{"text": "Second - line", "type": "HealthCareActivity"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "fuoropyrimidine", "type": "Chemical"}, {"text": "chemotherapies", "type": "HealthCareActivity"}]}

Example input:
Sentence: 53 ( 57 . 6 % ) , 27 ( 29 . 3 % ) , and 12 ( 13 % ) patients received CG , CF , and FOLFIRINOX regimen as first - line chemotherapy , respectively .

Example answer:
{"entities": [{"text": "received", "type": "Finding"}, {"text": "CG", "type": "Chemical"}, {"text": "CF", "type": "Chemical"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "regimen", "type": "HealthCareActivity"}, {"text": "first - line", "type": "HealthCareActivity"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Of the 54 patients diagnosed between 2011 and June 2014 , 28 patients received FOLFIRINOX and 22 Gemcitabine as the first - line chemotherapy .

Example answer:
{"entities": [{"text": "diagnosed", "type": "HealthCareActivity"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "Gemcitabine", "type": "Chemical"}, {"text": "first - line chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: This was the first study evaluating the FOLFIRINOX regimen in BTC .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "evaluating", "type": "HealthCareActivity"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "regimen", "type": "HealthCareActivity"}, {"text": "BTC", "type": "BiologicFunction"}]}

Example input:
Sentence: Comparison of FOLFIRINOX Chemotherapy with Other Regimens in Patients with Biliary Tract Cancers : a Retrospective Study The aim of this retrospective study was to compare the different treatment options of patients with advanced biliary tract carcinoma ( BTC ) who were treated with platinum - gemcitabine ( CG ) or platinum -5 - fluorouracil ( CF ) or 5 - Fluorouracil - oxaliplatin - irinotecan ( FOLFIRINOX ) chemotherapy .

Example answer:
{"entities": [{"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "Chemotherapy", "type": "HealthCareActivity"}, {"text": "Regimens", "type": "HealthCareActivity"}, {"text": "Biliary Tract Cancers", "type": "BiologicFunction"}, {"text": "Retrospective Study", "type": "ResearchActivity"}, {"text": "retrospective study", "type": "ResearchActivity"}, {"text": "treatment options", "type": "HealthCareActivity"}, {"text": "biliary tract carcinoma", "type": "BiologicFunction"}, {"text": "BTC", "type": "BiologicFunction"}, {"text": "platinum", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "CG", "type": "Chemical"}, {"text": "fluorouracil", "type": "Chemical"}, {"text": "CF", "type": "Chemical"}, {"text": "5 - Fluorouracil - oxaliplatin - irinotecan", "type": "HealthCareActivity"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Input:
Sentence: However , FOLFIRINOX can be an option in the second - line treatment of BTC patients who are eligible for chemotherapy .
