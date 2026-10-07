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

## Item MedMentions:test:3557
Example input:
Sentence: We applied multinomial regression models adjusted for age , sex , year and season of death .

Example answer:
{"entities": [{"text": "regression models", "type": "IntellectualProduct"}, {"text": "death", "type": "Finding"}]}

Example input:
Sentence: We used logistic regression to determine whether differences between the two time periods were significant , adjusting for the demographic characteristics of respondents .

Example answer:
{"entities": [{"text": "logistic regression", "type": "ResearchActivity"}, {"text": "respondents", "type": "PopulationGroup"}]}

Example input:
Sentence: This association was retained in multivariable models adjusted for demographics ( age , sex , race / ethnicity , and income level ) , alcohol and tobacco use , diabetes mellitus , and past periodontal treatment ( model 1 : adjusted OR [ aOR ] : 1 . 4 , 95 % CI : 1 . 1 to 1 . 9 ; P = 0 .

Example answer:
{"entities": [{"text": "race", "type": "PopulationGroup"}, {"text": "ethnicity", "type": "PopulationGroup"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "periodontal treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Multivariate logistic regression analyses ( adjusted for age , gender , education level , physical activity , alcohol use , smoking status , depression , arrhythmia , myocardial infarction , heart failure , stroke ) showed that participants with better feelings of affection , behavioral confirmation and stable good social support had a lower risk of incident SMC .

Example answer:
{"entities": [{"text": "education level", "type": "Finding"}, {"text": "smoking status", "type": "ClinicalAttribute"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "arrhythmia", "type": "Finding"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "heart failure", "type": "BiologicFunction"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "feelings", "type": "BiologicFunction"}, {"text": "affection", "type": "BiologicFunction"}, {"text": "confirmation", "type": "Finding"}, {"text": "SMC", "type": "BiologicFunction"}]}

Example input:
Sentence: Bias varied across quintiles with overestimation of UNa at lower quintiles ( by 29 - 105 % ) and underestimation at higher quintile ( by 7 - 37 % ) regardless of formula .

Example answer:
{"entities": [{"text": "formula", "type": "IntellectualProduct"}]}

Example input:
Sentence: Linear and logistic regressions models were applied to examine the relationships between baseline and change in SUA , change in eGFR , and rapid eGFR decline ( defined as the highest quartile of change in eGFR ) , adjusted for age , gender , body mass index , abdominal circumference , hypertension , dyslipidemia , and diabetes mellitus .

Example answer:
{"entities": [{"text": "SUA", "type": "Chemical"}, {"text": "eGFR", "type": "HealthCareActivity"}, {"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "abdominal circumference", "type": "ClinicalAttribute"}, {"text": "hypertension", "type": "BiologicFunction"}, {"text": "dyslipidemia", "type": "BiologicFunction"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}]}

Example input:
Sentence: Generalized linear modeling with DiD regression estimation showed that the mean number of MS relapses decreased significantly in the post - index period among patients in the Test Cohort compared with patients in the Control Cohort .

Example answer:
{"entities": [{"text": "DiD", "type": "ResearchActivity"}, {"text": "MS", "type": "BiologicFunction"}, {"text": "Test Cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: All regression coefficients were negative , implying that the more the surrogate overestimated quality of life compared to the older adult , the more he or she overestimated the older adult ' s desire to be treated .

Example answer:
{"entities": [{"text": "negative", "type": "Finding"}, {"text": "older adult", "type": "PopulationGroup"}]}

Example input:
Sentence: Linear modeling was used to assess change in the association between perceived overweight and self - reported psychosomatic complaint burden , adjusting for overweight status .

Example answer:
{"entities": [{"text": "perceived", "type": "BiologicFunction"}, {"text": "overweight", "type": "Finding"}]}

Example input:
Sentence: Design - adjusted logistic regressions were used to quantify changes in overweight perceptions over time .

Example answer:
{"entities": [{"text": "Design - adjusted logistic regressions", "type": "ResearchActivity"}, {"text": "overweight", "type": "Finding"}, {"text": "perceptions", "type": "BiologicFunction"}]}

Input:
Sentence: The results demonstrate that simple regression models can be used to statistically adjust for over or underestimation in self - report measures among different segments of the population .

## Item MedMentions:test:3677
Example input:
Sentence: A total of 171 patients were included .

Example answer:
{"entities": []}

Example input:
Sentence: Twenty - eight patients were enrolled .

Example answer:
{"entities": []}

Example input:
Sentence: 167 patients were included in the study .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Totally 174 patients were enrolled to the study ( 152 male , 22 female ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "male", "type": "PopulationGroup"}, {"text": "female", "type": "PopulationGroup"}]}

Example input:
Sentence: A total of 144 , 098 patients met the study criteria .

Example answer:
{"entities": []}

Example input:
Sentence: A total of 14 , 237 patients were enrolled in our study .

Example answer:
{"entities": []}

Example input:
Sentence: A total of 346 patients were included in the study .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: A total of 57 patients were enrolled ; 16 ( 28 .

Example answer:
{"entities": []}

Example input:
Sentence: A total of 400 patients ( 200 in each study center ) undergoing elective CABG surgery were enrolled after written informed consent .

Example answer:
{"entities": [{"text": "elective", "type": "HealthCareActivity"}, {"text": "CABG surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Informed consent was obtained from 45 patients , 39 were randomised and 36 needed support .

Example answer:
{"entities": [{"text": "Informed consent", "type": "IntellectualProduct"}, {"text": "randomised", "type": "ResearchActivity"}]}

Input:
Sentence: In total , 83 patients consented .

## Item MedMentions:test:3555
Example input:
Sentence: Group comparisons were performed by Rao - Scott χ ( 2 ) test .

Example answer:
{"entities": [{"text": "Rao - Scott χ ( 2 ) test", "type": "IntellectualProduct"}]}

Example input:
Sentence: For known - groups validity , the Mann - Whitney U test and Kruskal - Wallis test were used to examine the associations between SF - 6D and EQ - 5D - 5L and patient characteristics .

Example answer:
{"entities": [{"text": "Kruskal - Wallis test", "type": "IntellectualProduct"}, {"text": "SF - 6D", "type": "IntellectualProduct"}, {"text": "EQ - 5D - 5L", "type": "IntellectualProduct"}]}

Example input:
Sentence: Comparisons of continuous parameters were made with independent sample t - test between two groups .

Example answer:
{"entities": [{"text": "parameters", "type": "Finding"}, {"text": "sample t - test", "type": "IntellectualProduct"}]}

Example input:
Sentence: Using the leave - one - out cross - validation method to analyze our sample , we reliably distinguished the participants with PD from the controls with 92 % sensitivity and 87 % specificity .

Example answer:
{"entities": [{"text": "cross - validation method", "type": "ResearchActivity"}, {"text": "analyze", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "PD", "type": "BiologicFunction"}]}

Example input:
Sentence: Independent t - tests were used to evaluate potential sex and grade level differences for age , BMI , VO2 , EE , and METs .

Example answer:
{"entities": [{"text": "Independent t - tests", "type": "IntellectualProduct"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "VO2", "type": "HealthCareActivity"}, {"text": "EE", "type": "BiologicFunction"}, {"text": "METs", "type": "HealthCareActivity"}]}

Example input:
Sentence: The predictions were comparable with the measured value .

Example answer:
{"entities": []}

Example input:
Sentence: For each scenario , usability was measured via efficiency , recorded as time to task completion , and participants ' perceived satisfaction which were compared using Kruskal - Wallis and Mann Whitney U tests , respectively .

Example answer:
{"entities": [{"text": "recorded", "type": "IntellectualProduct"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "satisfaction", "type": "BiologicFunction"}, {"text": "Kruskal - Wallis and Mann Whitney U tests", "type": "IntellectualProduct"}]}

Example input:
Sentence: One - sample test for proportions and T - tests examined equality of proportions ( anchors ) and means scores ( non - anchors ) with the fixed intervals ( 0 . 0 , 2 . 5 , 5 . 0 , 7 . 5 , and 10 . 0 ) .

Example answer:
{"entities": [{"text": "One - sample test", "type": "IntellectualProduct"}, {"text": "T - tests", "type": "IntellectualProduct"}, {"text": "anchors", "type": "PopulationGroup"}, {"text": "non - anchors", "type": "PopulationGroup"}]}

Example input:
Sentence: The models produced group estimates from the PAR that were statistically equivalent to the observed time spent in SB and MVPA obtained from the objective SWA monitor ; however additional work is needed to correct for estimates of individual behavior .

Example answer:
{"entities": [{"text": "models", "type": "IntellectualProduct"}, {"text": "monitor", "type": "MedicalDevice"}]}

Example input:
Sentence: Confirmatory factor analysis revealed the loadings of a single ( broad ability ) factor model were equal across both measurement occasions , but the lack of intercept invariance suggested that mean -level comparisons are more appropriately carried out at a subtest level .

Example answer:
{"entities": []}

Input:
Sentence: Equivalence testing was used to evaluate the equivalence of the model - predicted values with the objective measures in a separate holdout sample .

## Item MedMentions:test:3495
Example input:
Sentence: Abstracts of 4255 papers identified were reviewed by three reviewers to determine whether the entire article was likely to contain relevant information .

Example answer:
{"entities": [{"text": "Abstracts", "type": "IntellectualProduct"}, {"text": "papers", "type": "IntellectualProduct"}, {"text": "reviewers", "type": "PopulationGroup"}, {"text": "article", "type": "IntellectualProduct"}]}

Example input:
Sentence: A systematic literature search was performed in PubMed , Education Resource information Centre ( ERIC ) , Psycinfo and Cochrane reviews including studies conducted after 1990 and before the first of August of 2013 .

Example answer:
{"entities": [{"text": "PubMed", "type": "IntellectualProduct"}, {"text": "Cochrane", "type": "IntellectualProduct"}, {"text": "reviews", "type": "IntellectualProduct"}, {"text": "studies", "type": "HealthCareActivity"}]}

Example input:
Sentence: Review articles were analyzed with regard to variability in the cited literature and final conclusions .

Example answer:
{"entities": [{"text": "Review articles", "type": "IntellectualProduct"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "literature", "type": "IntellectualProduct"}]}

Example input:
Sentence: A review of research evidence , published guidelines and clinical literature was undertaken following an electronic database and relevant literature search .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "published guidelines", "type": "IntellectualProduct"}, {"text": "literature", "type": "IntellectualProduct"}]}

Example input:
Sentence: In total , we identified 791 references , retrieved 20 full text articles , and included nine studies in our review .

Example answer:
{"entities": [{"text": "references", "type": "IntellectualProduct"}, {"text": "full text articles", "type": "IntellectualProduct"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: After deduplication , citations will be screened independently by 2 authors , and selected for inclusion based on prespecified criteria .

Example answer:
{"entities": [{"text": "citations", "type": "IntellectualProduct"}, {"text": "authors", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Five primary studies were included in the review ( all level III - 3 evidence ) ; 7 additional sources of relevant data were also included .

Example answer:
{"entities": [{"text": "primary studies", "type": "ResearchActivity"}, {"text": "review", "type": "IntellectualProduct"}]}

Example input:
Sentence: The literature review identified 51 publications that were included .

Example answer:
{"entities": [{"text": "literature review", "type": "IntellectualProduct"}, {"text": "publications", "type": "IntellectualProduct"}]}

Example input:
Sentence: All human studies , including review articles , were identified for further analysis .

Example answer:
{"entities": [{"text": "human studies", "type": "ResearchActivity"}, {"text": "review articles", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Manual review of references was completed and experts in the field were contacted for unpublished data .

Example answer:
{"entities": [{"text": "experts", "type": "ProfessionalOrOccupationalGroup"}, {"text": "unpublished data", "type": "IntellectualProduct"}]}

Input:
Sentence: Additional references were identified from a review of literature citations .

## Item MedMentions:test:3072
Example input:
Sentence: The median ( range ) follow - up for survivors was 22 ( 4 - 73 ) months from diagnosis .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}]}

Example input:
Sentence: At 1 - month follow - up , 10 - 12 treatment responders who completed the assessment maintained improvement .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "responders", "type": "PopulationGroup"}, {"text": "assessment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Evaluations before randomization and 4 weeks after intervention included motor scoring index , real - time PCR and Western blot .

Example answer:
{"entities": [{"text": "Evaluations", "type": "HealthCareActivity"}, {"text": "randomization", "type": "ResearchActivity"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "real - time PCR", "type": "ResearchActivity"}, {"text": "Western blot", "type": "HealthCareActivity"}]}

Example input:
Sentence: After accounting for adaptive functioning near diagnosis , premorbid behavior problems predicted declines in adaptive functioning 2 years postdiagnosis .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "postdiagnosis", "type": "Finding"}]}

Example input:
Sentence: Adverse Events Profile total scores improved for 21 / 21 ( 100 . 0 % ) patients , QOLIE - 10 total scores improved for 17 / 21 ( 81 . 0 % ) patients , and alertness scores improved for 16 / 21 ( 76 . 2 % ) patients .

Example answer:
{"entities": [{"text": "Adverse Events Profile", "type": "IntellectualProduct"}, {"text": "improved", "type": "Finding"}, {"text": "QOLIE - 10", "type": "IntellectualProduct"}, {"text": "alertness", "type": "BiologicFunction"}]}

Example input:
Sentence: PTSD symptom improvement was assessed one week and 3 months after the conclusion of treatment using the clinician - administered PTSD scale ( CAPS ) .

Example answer:
{"entities": [{"text": "PTSD", "type": "BiologicFunction"}, {"text": "symptom", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "clinician - administered PTSD scale", "type": "IntellectualProduct"}, {"text": "CAPS", "type": "IntellectualProduct"}]}

Example input:
Sentence: An exploratory analysis was performed to assess safety outcomes in patients with long duration of response ( DOR ) ( ≥12 or ≥24 months ) .

Example answer:
{"entities": [{"text": "exploratory analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: At baseline and 12 months after treatment self - efficacy control , self - efficacy function , physical and mental HRQoL , anxiety , depression and fatigue were assessed via self - report questionnaires .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "mental", "type": "BiologicFunction"}, {"text": "anxiety", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "fatigue", "type": "Finding"}, {"text": "self - report", "type": "ResearchActivity"}, {"text": "questionnaires", "type": "IntellectualProduct"}]}

Example input:
Sentence: Twelve months effect of self - referral to inpatient treatment on patient activation , recovery , symptoms and functioning : A randomized controlled study To investigate the effect of having a contract for self - referral to inpatient treatment ( SRIT ) in patients with severe mental disorders .

Example answer:
{"entities": [{"text": "self - referral", "type": "HealthCareActivity"}, {"text": "inpatient treatment", "type": "HealthCareActivity"}, {"text": "patient activation", "type": "HealthCareActivity"}, {"text": "symptoms", "type": "Finding"}, {"text": "functioning", "type": "BiologicFunction"}, {"text": "randomized controlled study", "type": "ResearchActivity"}, {"text": "contract", "type": "IntellectualProduct"}, {"text": "self - referral to inpatient treatment", "type": "HealthCareActivity"}, {"text": "SRIT", "type": "HealthCareActivity"}, {"text": "mental disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: There was no significant effect on PAM - 13 ( estimated mean difference ( emd ) -0 . 41 , 95 % CI ( CI ) : - 7 . 49 - 6 . 67 ) , nor on the RAS ( emd 0 . 02 , CI : - 0 . 27 - 0 . 31 ) or BASIS - 32 ( 0 . 09 , CI : - 0 . 28 - 0 . 45 ) .

Example answer:
{"entities": [{"text": "PAM - 13", "type": "IntellectualProduct"}, {"text": "RAS", "type": "IntellectualProduct"}, {"text": "BASIS - 32", "type": "IntellectualProduct"}]}

Input:
Sentence: Outcomes were assessed after 12 months with the self - report questionnaires Patient Activation Measure ( PAM - 13 ) , Recovery Assessment Scale ( RAS ) , and the Behavior and Symptom Identification Scale ( BASIS - 32 ) and analyzed using linear mixed and regression models .

## Item MedMentions:test:3453
Example input:
Sentence: Plantago major extract at 1200 mg / kg significantly improved malondialdehyde concentration and total thiol content compared to the cisplatin group .

Example answer:
{"entities": [{"text": "Plantago major extract", "type": "Chemical"}, {"text": "improved", "type": "Finding"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Thirty minutes before the procedure , the experimental groups were treated intraperitoneally with hydroalcoholic fruit extracts of E .

Example answer:
{"entities": [{"text": "intraperitoneally", "type": "SpatialConcept"}, {"text": "hydroalcoholic fruit extracts", "type": "Chemical"}, {"text": "E .", "type": "Eukaryote"}]}

Example input:
Sentence: On Day 7 , embryo yields were assessed and the blastocysts were vitrified by Cryotop method in 16 . 5 % ethylene glycol , 16 . 5 % DMSO , and 0 . 5 M sucrose .

Example answer:
{"entities": [{"text": "blastocysts", "type": "AnatomicalStructure"}, {"text": "Cryotop method", "type": "IntellectualProduct"}, {"text": "ethylene glycol", "type": "Chemical"}, {"text": "DMSO", "type": "Chemical"}, {"text": "sucrose", "type": "Chemical"}]}

Example input:
Sentence: 1 % formic acid in water ) ; sample load ( 26 cycles of 250μL ) ; wash ( 100μL of 3 % acetic acid in water followed by 100μL 5 % methanol in water ) ; and elution ( 6 cycles of 100μL of 10 % ammonium hydroxide in methanol ) .

Example answer:
{"entities": [{"text": "formic acid", "type": "Chemical"}, {"text": "water", "type": "Chemical"}, {"text": "acetic acid", "type": "Chemical"}, {"text": "methanol", "type": "Chemical"}, {"text": "ammonium hydroxide", "type": "Chemical"}]}

Example input:
Sentence: Various in vitro evaluation ( antioxidant and anti - inflammatory ) guided purification of ethyl acetate - methanol ( EtOAc - MeOH ) extract of bivalve clam , Paphia malabarica characterised two new sterol derivatives as 23 - gem - dimethylcholesta - 5 - en - 3β - ol ( 1 ) and ( 22E ) - 24 ( 1 ) , 24 ( 2 ) - methyldihomocholest - 5 , 22 - dien - 3β - ol ( 2 ) collected from the south - west coast of Arabian Sea .

Example answer:
{"entities": [{"text": "antioxidant", "type": "BiologicFunction"}, {"text": "ethyl acetate", "type": "Chemical"}, {"text": "methanol", "type": "Chemical"}, {"text": "EtOAc", "type": "Chemical"}, {"text": "MeOH", "type": "Chemical"}, {"text": "bivalve clam", "type": "Eukaryote"}, {"text": "Paphia malabarica", "type": "Eukaryote"}, {"text": "sterol", "type": "Chemical"}, {"text": "derivatives", "type": "Chemical"}, {"text": "23 - gem - dimethylcholesta - 5 - en - 3β - ol", "type": "Chemical"}, {"text": "1", "type": "Chemical"}, {"text": "( 22E ) - 24 ( 1 ) , 24 ( 2 ) - methyldihomocholest - 5 , 22 - dien - 3β - ol", "type": "Chemical"}, {"text": "2", "type": "Chemical"}, {"text": "south - west coast", "type": "SpatialConcept"}, {"text": "Arabian Sea", "type": "SpatialConcept"}]}

Example input:
Sentence: Dietary administration of Pontogammarus maeoticus extract affects immune responses , stress resistance , feed intake and growth performance of caspian roach ( Rutilus caspicus ) fingerlings Dietary administration of immunostimulants showed promising results for elevation of immune responses and disease resistance .

Example answer:
{"entities": [{"text": "Dietary administration", "type": "HealthCareActivity"}, {"text": "Pontogammarus maeoticus", "type": "Eukaryote"}, {"text": "immune responses", "type": "BiologicFunction"}, {"text": "feed intake", "type": "BiologicFunction"}, {"text": "growth performance", "type": "BiologicFunction"}, {"text": "caspian roach", "type": "Eukaryote"}, {"text": "Rutilus caspicus", "type": "Eukaryote"}, {"text": "immunostimulants", "type": "Chemical"}, {"text": "disease resistance", "type": "BiologicFunction"}]}

Example input:
Sentence: A small plasma volume ( 0 . 25mL ) pre - diluted ( 1 : 20 ) , was extracted with MEPS M1 sorbent as follows : conditioning ( 4 cycles of 250μL methanol and 4 cycles of 250μL 0 .

Example answer:
{"entities": [{"text": "small plasma volume", "type": "ClinicalAttribute"}, {"text": "MEPS", "type": "HealthCareActivity"}, {"text": "methanol", "type": "Chemical"}]}

Example input:
Sentence: maeoticus extract on innate immune response , resistance , feed intake as well as growth performance of the Caspian roach .

Example answer:
{"entities": [{"text": "maeoticus", "type": "Eukaryote"}, {"text": "response", "type": "BiologicFunction"}, {"text": "feed intake", "type": "BiologicFunction"}, {"text": "growth performance", "type": "BiologicFunction"}, {"text": "Caspian roach", "type": "Eukaryote"}]}

Example input:
Sentence: maeoticus extracts fed fish ( P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "maeoticus", "type": "Eukaryote"}, {"text": "fed fish", "type": "Eukaryote"}]}

Example input:
Sentence: maeoticus extracts ( P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "maeoticus", "type": "Eukaryote"}]}

Input:
Sentence: maeoticus extract dilution with distilled water 1 : 25 [ T1 ] and 1 : 50 [ T2 ] were prepared .

## Item MedMentions:test:3469
Example input:
Sentence: Our results demonstrate that the ADH7 promoter can overcome the pronounced translation repression caused by the combined stress of vanillin , furfural , and HMF , and also suggest a new gene engineering strategy to breed robust and optimized yeasts for bioethanol production from a lignocellulosic biomass .

Example answer:
{"entities": [{"text": "results", "type": "Finding"}, {"text": "ADH7", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "translation repression", "type": "BiologicFunction"}, {"text": "combined stress", "type": "Finding"}, {"text": "vanillin", "type": "Chemical"}, {"text": "furfural", "type": "Chemical"}, {"text": "HMF", "type": "Chemical"}, {"text": "gene engineering", "type": "ResearchActivity"}, {"text": "yeasts", "type": "Eukaryote"}, {"text": "bioethanol production", "type": "BiologicFunction"}, {"text": "lignocellulosic", "type": "Chemical"}]}

Example input:
Sentence: starkeyi , we constructed a series of mutants by disrupting genes for LsKu70p , LsKu80p , and / or LsLig4p , which share homology with other yeasts Ku70p , Ku80p , and Lig4p , respectively , being involved in non - homologous end - joining pathway .

Example answer:
{"entities": [{"text": "starkeyi", "type": "Eukaryote"}, {"text": "mutants", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "LsKu70p", "type": "Chemical"}, {"text": "LsKu80p", "type": "Chemical"}, {"text": "LsLig4p", "type": "Chemical"}, {"text": "yeasts", "type": "Eukaryote"}, {"text": "Ku70p", "type": "Chemical"}, {"text": "Ku80p", "type": "Chemical"}, {"text": "Lig4p", "type": "Chemical"}]}

Example input:
Sentence: However , improvement of its lipid productivity is essential for the cost - effective production of oleochemicals and fuels .

Example answer:
{"entities": [{"text": "lipid", "type": "Chemical"}, {"text": "oleochemicals", "type": "Chemical"}]}

Example input:
Sentence: In this study we compared two different systems of dCas9 -mediated transcriptional reprogramming , and applied them to genes controlling two biosynthetic pathways for biobased production of isoprenoids and triacylglycerols ( TAGs ) in baker 's yeast Saccharomyces cerevisiae .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "dCas9", "type": "Chemical"}, {"text": "transcriptional reprogramming", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "biosynthetic pathways", "type": "BiologicFunction"}, {"text": "isoprenoids", "type": "Chemical"}, {"text": "triacylglycerols", "type": "Chemical"}, {"text": "TAGs", "type": "Chemical"}, {"text": "baker 's yeast", "type": "Eukaryote"}, {"text": "Saccharomyces cerevisiae", "type": "Eukaryote"}]}

Example input:
Sentence: Thermomyces lanuginosus ( TL ) lipase showed a 1 . 3 - fold enhanced activity after irradiating at 22 kHz and 11 .

Example answer:
{"entities": [{"text": "Thermomyces lanuginosus", "type": "Eukaryote"}, {"text": "TL", "type": "Eukaryote"}, {"text": "lipase", "type": "Chemical"}, {"text": "activity", "type": "BiologicFunction"}]}

Example input:
Sentence: The polar lipid profile of strain EGI 6500337 T contained diphosphatidylglycerol , phosphatidylglycerol , phosphatidylcholine , phosphatidylethanolamine as major components , similarly to the members of the genus Aurantimonas .

Example answer:
{"entities": [{"text": "lipid profile", "type": "Chemical"}, {"text": "strain EGI 6500337 T", "type": "Bacterium"}, {"text": "diphosphatidylglycerol", "type": "Chemical"}, {"text": "phosphatidylglycerol", "type": "Chemical"}, {"text": "phosphatidylcholine", "type": "Chemical"}, {"text": "phosphatidylethanolamine", "type": "Chemical"}, {"text": "genus Aurantimonas", "type": "Bacterium"}]}

Example input:
Sentence: starkeyi ∆lslig4 background strains have promise as efficient recipient strains for genetic and metabolic engineering approaches in this yeast .

Example answer:
{"entities": [{"text": "starkeyi", "type": "Eukaryote"}, {"text": "∆lslig4", "type": "AnatomicalStructure"}, {"text": "genetic", "type": "ResearchActivity"}, {"text": "metabolic engineering", "type": "ResearchActivity"}, {"text": "yeast", "type": "Eukaryote"}]}

Example input:
Sentence: starkeyi via gene manipulation techniques may result in improvements in lipid production and our understanding of the mechanisms behind lipid biosynthesis pathways .

Example answer:
{"entities": [{"text": "starkeyi", "type": "Eukaryote"}, {"text": "lipid", "type": "Chemical"}]}

Example input:
Sentence: Efficient gene targeting in non - homologous end - joining -deficient Lipomyces starkeyi strains Microbial lipids are sustainable feedstock for the production of oleochemicals and biodiesel .

Example answer:
{"entities": [{"text": "gene targeting", "type": "ResearchActivity"}, {"text": "Lipomyces starkeyi", "type": "Eukaryote"}, {"text": "lipids", "type": "Chemical"}, {"text": "oleochemicals", "type": "Chemical"}, {"text": "biodiesel", "type": "Chemical"}]}

Example input:
Sentence: Oleaginous yeasts have recently been proposed as alternative lipid producers to plants and animals to promote sustainability in the chemical and fuel industries .

Example answer:
{"entities": [{"text": "Oleaginous yeasts", "type": "Eukaryote"}, {"text": "lipid", "type": "Chemical"}, {"text": "producers", "type": "Eukaryote"}, {"text": "plants", "type": "Eukaryote"}, {"text": "animals", "type": "Eukaryote"}, {"text": "chemical", "type": "Organization"}]}

Input:
Sentence: The oleaginous yeast Lipomyces starkeyi has great industrial potential as an excellent lipid producer .

## Item MedMentions:test:3549
Example input:
Sentence: It was performed using ten individual samples ( DNA and sera ) selected on the basis of their Gm ( gamma marker ) allotype polymorphism in order to cover the main immunoglobulin heavy gamma ( IGHG ) gene diversity .

Example answer:
{"entities": [{"text": "individual", "type": "PopulationGroup"}, {"text": "samples", "type": "AnatomicalStructure"}, {"text": "DNA", "type": "Chemical"}, {"text": "sera", "type": "Chemical"}, {"text": "Gm", "type": "BiologicFunction"}, {"text": "gamma marker", "type": "BiologicFunction"}, {"text": "allotype", "type": "BiologicFunction"}, {"text": "polymorphism", "type": "BiologicFunction"}, {"text": "immunoglobulin heavy gamma ( IGHG ) gene", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The results indicated a few clonal populations , mainly observed in human strains , with 32 . 5 % of all strains associated with one of three clonal complexes and 30 sequences types .

Example answer:
{"entities": [{"text": "indicated", "type": "Finding"}, {"text": "clonal", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "clonal complexes", "type": "AnatomicalStructure"}, {"text": "sequences", "type": "SpatialConcept"}]}

Example input:
Sentence: With this aim , we selected 11 variants of 5 genes ( GJB2 , SLC26A4 , MTRNR1 , TMPRSS3 , and CDH23 ) showing high prevalence with varying degrees in Koreans and developed the U - TOP ™ HL Genotyping Kit , a real - time PCR -based method using the MeltingArray technique and peptide nucleic acid probes .

Example answer:
{"entities": [{"text": "variants", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "GJB2", "type": "AnatomicalStructure"}, {"text": "SLC26A4", "type": "AnatomicalStructure"}, {"text": "MTRNR1", "type": "AnatomicalStructure"}, {"text": "TMPRSS3", "type": "AnatomicalStructure"}, {"text": "CDH23", "type": "AnatomicalStructure"}, {"text": "Koreans", "type": "PopulationGroup"}, {"text": "U - TOP ™ HL Genotyping Kit", "type": "MedicalDevice"}, {"text": "real - time PCR", "type": "ResearchActivity"}, {"text": "MeltingArray technique", "type": "ResearchActivity"}, {"text": "peptide nucleic acid", "type": "Chemical"}, {"text": "probes", "type": "MedicalDevice"}]}

Example input:
Sentence: Nevertheless , in RBC genotyping ( BioArray HEA BeadChip , Immucor , Warren , NJ ) performed in our transfusion service on all patients with alloantibodies , her Kidd typing was JK * A / JK * B based on the Jka / Jkb single nucleotide polymorphism in exon 9 ( c .

Example answer:
{"entities": [{"text": "RBC", "type": "AnatomicalStructure"}, {"text": "genotyping", "type": "HealthCareActivity"}, {"text": "BioArray HEA BeadChip , Immucor , Warren , NJ", "type": "IntellectualProduct"}, {"text": "transfusion", "type": "HealthCareActivity"}, {"text": "service", "type": "HealthCareActivity"}, {"text": "alloantibodies", "type": "Chemical"}, {"text": "Kidd typing", "type": "HealthCareActivity"}, {"text": "JK * A / JK * B", "type": "Finding"}, {"text": "Jka / Jkb", "type": "AnatomicalStructure"}, {"text": "single nucleotide polymorphism", "type": "SpatialConcept"}, {"text": "exon 9", "type": "Chemical"}, {"text": "c .", "type": "Chemical"}]}

Example input:
Sentence: Subjects were genotyped using polymerase chain reaction - restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "Subjects", "type": "PopulationGroup"}, {"text": "polymerase chain reaction", "type": "ResearchActivity"}, {"text": "restriction fragment length polymorphism", "type": "BiologicFunction"}]}

Example input:
Sentence: Additionally , determining the single - nucleotide polymorphisms of 4 loci , including IGF2 rs3741205 , rs3741206 , rs3741211 , and GRB10 rs2237457 , showed that the TC + CC genotype of IGF2 rs3741211 had a 1 . 91 - fold increased risk of SA after ART .

Example answer:
{"entities": [{"text": "single - nucleotide polymorphisms", "type": "SpatialConcept"}, {"text": "4 loci", "type": "AnatomicalStructure"}, {"text": "IGF2 rs3741205", "type": "AnatomicalStructure"}, {"text": "rs3741206", "type": "AnatomicalStructure"}, {"text": "rs3741211", "type": "AnatomicalStructure"}, {"text": "GRB10 rs2237457", "type": "AnatomicalStructure"}, {"text": "IGF2 rs3741211", "type": "AnatomicalStructure"}, {"text": "SA", "type": "BiologicFunction"}, {"text": "ART", "type": "HealthCareActivity"}]}

Example input:
Sentence: Bioinformatic Analysis of Codon Usage and Phylogenetic Relationships in Different Genotypes of the Hepatitis C Virus The hepatitis C virus ( HCV ) has six major genotypes .

Example answer:
{"entities": [{"text": "Bioinformatic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Analysis", "type": "ResearchActivity"}, {"text": "Codon", "type": "SpatialConcept"}, {"text": "Hepatitis C Virus", "type": "Virus"}, {"text": "hepatitis C virus", "type": "Virus"}, {"text": "HCV", "type": "Virus"}]}

Example input:
Sentence: Genotyping for SNP - 3951C / T was performed by PCR / RFLP .

Example answer:
{"entities": [{"text": "Genotyping", "type": "HealthCareActivity"}, {"text": "SNP - 3951C / T", "type": "SpatialConcept"}, {"text": "PCR / RFLP", "type": "HealthCareActivity"}]}

Example input:
Sentence: We used a case - control study involving 386 IS patients and 386 non - IS controls from a rural population and determined the genotypes of five polymorphisms ( rs12237774 , rs17611 , rs4837805 , rs7026551 , and rs1017119 ) of C5 gene by Snapshot single - nucleotide polymorphism genotyping assays to assess any links with IS .

Example answer:
{"entities": [{"text": "case - control study", "type": "ResearchActivity"}, {"text": "IS", "type": "BiologicFunction"}, {"text": "rural population", "type": "PopulationGroup"}, {"text": "polymorphisms", "type": "BiologicFunction"}, {"text": "rs12237774", "type": "SpatialConcept"}, {"text": "rs17611", "type": "SpatialConcept"}, {"text": "rs4837805", "type": "SpatialConcept"}, {"text": "rs7026551", "type": "SpatialConcept"}, {"text": "rs1017119", "type": "SpatialConcept"}, {"text": "C5 gene", "type": "AnatomicalStructure"}, {"text": "single - nucleotide polymorphism genotyping assays", "type": "HealthCareActivity"}]}

Example input:
Sentence: A total of 56 KPC - Kp isolates were recovered from clinical samples in a Chinese hospital , which were assigned to clonal lineages by multilocus sequence typing ( MLST ) .

Example answer:
{"entities": [{"text": "KPC - Kp", "type": "Bacterium"}, {"text": "isolates", "type": "Chemical"}, {"text": "Chinese hospital", "type": "Organization"}, {"text": "multilocus sequence typing", "type": "ResearchActivity"}, {"text": "MLST", "type": "ResearchActivity"}]}

Input:
Sentence: In this study , multilocus sequence typing protocol was used to investigate genotypic relationships among 40 C .

## Item MedMentions:test:3534
Example input:
Sentence: The success of the effort for improving access to opioid medications was underpinned by a three - pronged strategy of 1 ) persuading the executive arm of the government to take interim enabling measures ; 2 ) leveraging judicial intervention through public interest litigation ; and 3 ) crafting a viable policy document for legislative approval and implementation .

Example answer:
{"entities": [{"text": "opioid", "type": "Chemical"}, {"text": "medications", "type": "HealthCareActivity"}, {"text": "executive arm of the government", "type": "ProfessionalOrOccupationalGroup"}, {"text": "measures", "type": "IntellectualProduct"}, {"text": "public", "type": "PopulationGroup"}, {"text": "interest", "type": "PopulationGroup"}]}

Example input:
Sentence: To optimize postoperative opioid dosage and better understand opioid consumption patterns after DRF - ORIF , we conducted a prospective study with the hypothesis that opioid consumption would increase with worsening fracture classification and various patient demographics .

Example answer:
{"entities": [{"text": "optimize", "type": "HealthCareActivity"}, {"text": "opioid", "type": "Chemical"}, {"text": "DRF", "type": "InjuryOrPoisoning"}, {"text": "prospective study", "type": "ResearchActivity"}, {"text": "fracture", "type": "InjuryOrPoisoning"}, {"text": "classification", "type": "IntellectualProduct"}]}

Example input:
Sentence: However , among individuals completing inpatient heroin detoxification , perceived refusal self - efficacy may also reduce one 's perceived need for medication - assisted treatment ( MAT ) , an effective and recommended treatment for opioid use disorder .

Example answer:
{"entities": [{"text": "individuals", "type": "PopulationGroup"}, {"text": "heroin", "type": "Chemical"}, {"text": "detoxification", "type": "HealthCareActivity"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "medication - assisted", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "MAT", "type": "HealthCareActivity"}, {"text": "recommended treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: 1 ( interquartile range 0 . 6 - 2 . 0 ) years , 1 , 034 patients ( 46 % ) were dispensed ≥1 opioid prescription ( N = 13 , 722 prescriptions ) .

Example answer:
{"entities": [{"text": "dispensed", "type": "HealthCareActivity"}, {"text": "opioid", "type": "Chemical"}, {"text": "prescription", "type": "HealthCareActivity"}, {"text": "prescriptions", "type": "HealthCareActivity"}]}

Example input:
Sentence: Moreover , we find that poor people present a greater tendency to incur catastrophic OOP expenditures for hospital health care in private providers .

Example answer:
{"entities": [{"text": "find", "type": "Finding"}, {"text": "people", "type": "PopulationGroup"}, {"text": "hospital health care", "type": "HealthCareActivity"}, {"text": "private providers", "type": "Organization"}]}

Example input:
Sentence: Mean overall opioid consumption ( morphine equivalence ) was 58 . 5 mg , or 14 .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: There were no significant differences in opioid consumption between the general and regional anesthesia groups .

Example answer:
{"entities": [{"text": "no significant", "type": "Finding"}, {"text": "general", "type": "HealthCareActivity"}]}

Example input:
Sentence: Demographic analysis revealed an inverse relationship between age and opioid use .

Example answer:
{"entities": [{"text": "Demographic analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: A significant relationship was found between increasing age and decreasing opioid consumption .

Example answer:
{"entities": [{"text": "increasing age", "type": "Finding"}, {"text": "decreasing", "type": "Finding"}]}

Example input:
Sentence: Worsening fracture classification and self - payment / Medicaid payment trended toward increasing opioid consumption .

Example answer:
{"entities": [{"text": "fracture classification", "type": "IntellectualProduct"}]}

Input:
Sentence: Similarly , there was a trend toward more opioid consumption among self - pay and Medicaid patients .

## Item MedMentions:test:3576
Example input:
Sentence: TpTe immediately after CRT - D independently predicted VT / VF episodes at 1 - year follow - up ( hazard ratio [ HR ] , 1 . 030 ; P = 0 . 001 ) .

Example answer:
{"entities": [{"text": "VT", "type": "BiologicFunction"}, {"text": "VF", "type": "BiologicFunction"}, {"text": "1 - year follow - up", "type": "Finding"}]}

Example input:
Sentence: The highest and lowest residues were obtained for the 7 and 0 days ' treatment and the 21 and 14 days ' treatment , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: Similar fluoride concentration × time patterns were noted for all investigated FV and studied variables , with the highest fluoride concentrations observed for the first biological sample collected after FV application ( 30min ) .

Example answer:
{"entities": [{"text": "fluoride", "type": "Chemical"}, {"text": "noted", "type": "IntellectualProduct"}, {"text": "FV", "type": "Chemical"}, {"text": "studied", "type": "ResearchActivity"}]}

Example input:
Sentence: At 60 months , median corrected distance VA ) in the fresh group had improved to 20 / 150 from a baseline of counting fingers , whereas the frozen group improved to 20 / 400 from a baseline of hand motions .

Example answer:
{"entities": [{"text": "VA", "type": "ClinicalAttribute"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: Between November 2014 and June 2015 , Ptr , stim and ultrasound variables were measured in mechanically ventilated patients < 24 hours after intubation ( ' initiation of mechanical ventilation ( MV ) ' , under assist - control ventilation , ACV ) and at the time of switch to pressure support ventilation ( ' switch to PSV ' ) , and compared using Spearman 's correlation and receiver operating characteristic curve analysis .

Example answer:
{"entities": [{"text": "Ptr , stim", "type": "HealthCareActivity"}, {"text": "ultrasound", "type": "HealthCareActivity"}, {"text": "mechanically ventilated", "type": "HealthCareActivity"}, {"text": "intubation", "type": "HealthCareActivity"}, {"text": "pressure support ventilation", "type": "HealthCareActivity"}, {"text": "PSV", "type": "HealthCareActivity"}, {"text": "Spearman 's correlation", "type": "IntellectualProduct"}]}

Example input:
Sentence: The mean difference was three days ( 95 % CI , 0 . 193 - 6 . 595 ; p = 0 . 039 ) .

Example answer:
{"entities": []}

Example input:
Sentence:  of the formulations had a log10 reduction after 3 h that was significantly better compared with the reference procedure [ mean 1 . 72 ( standard deviation 1 . 15 ) ] .

Example answer:
{"entities": []}

Example input:
Sentence: A large - volume bowel preparation regimen finished on the day of colonoscopy as close as 3 hours before the procedure result s in no increase in GRV or decrease in gastric pH .

Example answer:
{"entities": [{"text": "bowel preparation", "type": "HealthCareActivity"}, {"text": "regimen", "type": "HealthCareActivity"}, {"text": "colonoscopy", "type": "HealthCareActivity"}, {"text": "GRV", "type": "ClinicalAttribute"}, {"text": "decrease in gastric pH", "type": "Finding"}]}

Example input:
Sentence: GRV ≥ 25 mL or higher than expected GRV adjusted by weight ( 0 . 4 mL / kg ) were also not different among the study groups ( P = .90 and P = .87 , respectively ) .

Example answer:
{"entities": [{"text": "GRV", "type": "ClinicalAttribute"}, {"text": "expected", "type": "IntellectualProduct"}]}

Example input:
Sentence: The aim of this study is to evaluate GRV and gastric pH in patients who received day - before bowel preparation versus those ingesting their laxative on the day of colonoscopy under anesthesiologist - directed propofol deep sedation .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "GRV", "type": "ClinicalAttribute"}, {"text": "bowel preparation", "type": "HealthCareActivity"}, {"text": "ingesting", "type": "BiologicFunction"}, {"text": "laxative", "type": "Chemical"}, {"text": "colonoscopy", "type": "HealthCareActivity"}, {"text": "anesthesiologist", "type": "ProfessionalOrOccupationalGroup"}, {"text": "propofol", "type": "Chemical"}, {"text": "deep sedation", "type": "HealthCareActivity"}]}

Input:
Sentence: Evaluating GRV based on time since last ingestion of preparation ( 3 - 5 , 5 - 7 , > 7 hours ) did not result in any differences ( P = .56 ) .

## Item MedMentions:test:3147
Example input:
Sentence: Passive case detection of malaria in Ratanakiri Province ( Cambodia ) to detect villages at higher risk for malaria Cambodia reduced malaria incidence by more than 75 % between 2000 and 2015 , a target of the Millennium Development Goal 6 .

Example answer:
{"entities": [{"text": "Passive case detection", "type": "ResearchActivity"}, {"text": "malaria", "type": "BiologicFunction"}, {"text": "detect", "type": "Finding"}, {"text": "villages", "type": "SpatialConcept"}, {"text": "Millennium Development Goal 6", "type": "IntellectualProduct"}]}

Example input:
Sentence: The disease was first reported in China in 1984 and later on in Saudi Arabia in 1996 .

Example answer:
{"entities": [{"text": "disease", "type": "BiologicFunction"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "China", "type": "SpatialConcept"}, {"text": "Saudi Arabia", "type": "SpatialConcept"}]}

Example input:
Sentence: tuberculosis Beijing family isolates from different provinces across all China was genotyped by high - resolution ( 24 - MIRU - VNTR ) and low - resolution , high - rank ( modern and ancient sublineages ) markers .

Example answer:
{"entities": [{"text": "tuberculosis", "type": "Bacterium"}, {"text": "Beijing", "type": "SpatialConcept"}, {"text": "isolates", "type": "Chemical"}, {"text": "provinces", "type": "SpatialConcept"}, {"text": "China", "type": "SpatialConcept"}, {"text": "high - resolution", "type": "BiologicFunction"}, {"text": "24 - MIRU - VNTR", "type": "ResearchActivity"}, {"text": "low - resolution", "type": "BiologicFunction"}, {"text": "high - rank", "type": "BiologicFunction"}, {"text": "markers", "type": "BiologicFunction"}]}

Example input:
Sentence: Epidemiological study of relapsing fever borreliae detected in Haemaphysalis ticks and wild animals in the western part of Japan The genus Borrelia comprises arthropod - borne bacteria , which are infectious agents in vertebrates .

Example answer:
{"entities": [{"text": "Epidemiological study", "type": "ResearchActivity"}, {"text": "relapsing fever", "type": "BiologicFunction"}, {"text": "borreliae", "type": "Bacterium"}, {"text": "detected", "type": "Finding"}, {"text": "Haemaphysalis", "type": "Eukaryote"}, {"text": "ticks", "type": "Eukaryote"}, {"text": "wild animals", "type": "Eukaryote"}, {"text": "western part of Japan", "type": "SpatialConcept"}, {"text": "genus Borrelia", "type": "Bacterium"}, {"text": "arthropod - borne bacteria", "type": "Bacterium"}, {"text": "vertebrates", "type": "Eukaryote"}]}

Example input:
Sentence: The main population affected by rabies virus was male adult farmers .

Example answer:
{"entities": [{"text": "rabies virus", "type": "Virus"}, {"text": "farmers", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Survey of Trichinella infection from domestic pigs in the historical endemic areas of Henan province , central China The aim of this work was to investigate the current situation of Trichinella infection from domestic pigs in the historical endemic areas of Henan province , central China .

Example answer:
{"entities": [{"text": "Survey", "type": "IntellectualProduct"}, {"text": "Trichinella infection", "type": "BiologicFunction"}, {"text": "domestic pigs", "type": "Eukaryote"}, {"text": "historical", "type": "Finding"}, {"text": "endemic areas", "type": "SpatialConcept"}, {"text": "Henan province", "type": "SpatialConcept"}, {"text": "central China", "type": "SpatialConcept"}, {"text": "current situation", "type": "Finding"}]}

Example input:
Sentence: In this study , a PIV5 variant ( named ZJQ - 221 ) was isolated from a lesser panda with respiratory disease in Guangzhou zoo in Guangdong province , southern China .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "PIV5 variant", "type": "Virus"}, {"text": "ZJQ - 221", "type": "Virus"}, {"text": "lesser panda", "type": "Eukaryote"}, {"text": "respiratory disease", "type": "BiologicFunction"}, {"text": "Guangdong province", "type": "SpatialConcept"}, {"text": "southern China", "type": "SpatialConcept"}]}

Example input:
Sentence: Prevalence of high - risk human papillomavirus infection among women in Shaanxi province of China : A hospital -based investigation This study aimed to investigate the characteristics of female high - risk human papillomavirus ( HR - HPV ) infection in Shaanxi province of China .

Example answer:
{"entities": [{"text": "high - risk", "type": "Finding"}, {"text": "human papillomavirus infection", "type": "BiologicFunction"}, {"text": "Shaanxi", "type": "SpatialConcept"}, {"text": "province", "type": "SpatialConcept"}, {"text": "China", "type": "SpatialConcept"}, {"text": "hospital", "type": "Organization"}, {"text": "investigation", "type": "HealthCareActivity"}, {"text": "high - risk human papillomavirus ( HR - HPV ) infection", "type": "BiologicFunction"}]}

Example input:
Sentence: In conclusion , HPV infection was common among women in Shaanxi province .

Example answer:
{"entities": [{"text": "HPV infection", "type": "BiologicFunction"}, {"text": "Shaanxi", "type": "SpatialConcept"}, {"text": "province", "type": "SpatialConcept"}]}

Example input:
Sentence: We detected viral migration paths from Sichuan , Guizhou and Hunan to Hanzhong prefecture of Shaanxi and then spreaded to Xi ' an and other prefectures .

Example answer:
{"entities": [{"text": "detected", "type": "Finding"}, {"text": "migration paths", "type": "SpatialConcept"}, {"text": "Sichuan", "type": "SpatialConcept"}, {"text": "Guizhou", "type": "SpatialConcept"}, {"text": "Hunan", "type": "SpatialConcept"}, {"text": "Hanzhong prefecture", "type": "SpatialConcept"}, {"text": "Shaanxi", "type": "SpatialConcept"}, {"text": "Xi ' an", "type": "SpatialConcept"}, {"text": "other prefectures", "type": "SpatialConcept"}]}

Input:
Sentence: Re - emerging of rabies in Shaanxi Province , China , 2009 to 2015 To explore the epidemiological , phylogeographic and migration characteristics of human rabies in Shaanxi Province , China from 2009 to 2015 .

## Item MedMentions:test:3464
Example input:
Sentence: Two patients ( 7 . 7 % ) needed re - operation due to nonunion .

Example answer:
{"entities": [{"text": "re - operation", "type": "HealthCareActivity"}, {"text": "nonunion", "type": "Finding"}]}

Example input:
Sentence: Reperfusion was observed in 41 ( 51 . 89 % ) patients , the proportion of reperfusion was very similar in patients with and without severe LA ( 53 . 33 vs 51 . 02 % , p = 1 . 000 ) .

Example answer:
{"entities": [{"text": "Reperfusion", "type": "BiologicFunction"}, {"text": "reperfusion", "type": "BiologicFunction"}, {"text": "LA", "type": "BiologicFunction"}]}

Example input:
Sentence: 2 years ) , 29 . 0 % ( 20 / 69 ) of patients had recurrence and 18 . 8 % ( 13 / 69 ) required reoperation at median time of 4 . 8 years ( 3 . 1 - 9 . 1 years ) after the initial repair .

Example answer:
{"entities": [{"text": "recurrence", "type": "BiologicFunction"}, {"text": "reoperation", "type": "HealthCareActivity"}, {"text": "initial repair", "type": "HealthCareActivity"}]}

Example input:
Sentence: Among 19 cancer - controlled patients in their fifth post - recurrent year , 17 ( 89 % ) patients initially received radical local therapy for their recurrence .

Example answer:
{"entities": [{"text": "cancer", "type": "BiologicFunction"}, {"text": "controlled", "type": "Finding"}, {"text": "radical local therapy", "type": "HealthCareActivity"}, {"text": "recurrence", "type": "BiologicFunction"}]}

Example input:
Sentence: Eighty - two percent of the patients ( n = 815 ) participated . 97 % of those were ASA physical status 1 or 2 ; 83 % ( n = 676 ) had experience with previous anaesthetics , 86 % ( n = 700 ) reported to use the internet in general .

Example answer:
{"entities": [{"text": "ASA physical status 1", "type": "Finding"}, {"text": "2", "type": "Finding"}, {"text": "experience", "type": "BiologicFunction"}, {"text": "anaesthetics", "type": "Chemical"}, {"text": "general", "type": "SpatialConcept"}]}

Example input:
Sentence: A second surgical procedure was necessary in 2 , 23 , and 18 patients initially treated with MVD , RF , and SRS respectively ( p < 0 . 0001 ) .

Example answer:
{"entities": [{"text": "surgical procedure", "type": "HealthCareActivity"}, {"text": "MVD", "type": "HealthCareActivity"}, {"text": "RF", "type": "HealthCareActivity"}, {"text": "SRS", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the patients treated with MVD , RF , and SRS , the average number of procedures per patient necessary to achieve pain control was 1 .

Example answer:
{"entities": [{"text": "MVD", "type": "HealthCareActivity"}, {"text": "RF", "type": "HealthCareActivity"}, {"text": "SRS", "type": "HealthCareActivity"}, {"text": "procedures", "type": "HealthCareActivity"}, {"text": "pain control", "type": "HealthCareActivity"}]}

Example input:
Sentence: Twenty - four ( 54 . 5 % ) patients had normal activity , 3 ( 6 . 8 % ) had occasional discomfort , 2 ( 4 . 5 % ) had pain impairing function , 7 ( 15 .

Example answer:
{"entities": [{"text": "occasional discomfort", "type": "Finding"}, {"text": "pain impairing function", "type": "BiologicFunction"}]}

Example input:
Sentence: 91 % of the patients reported only very mild postoperative pain .

Example answer:
{"entities": [{"text": "postoperative pain", "type": "Finding"}]}

Example input:
Sentence: Many lived with pain , but all reported that they were willing to undergo the same procedure again .

Example answer:
{"entities": [{"text": "pain", "type": "Finding"}]}

Input:
Sentence: More than 50 % of patients reported mild , moderate or severe pain , but all patients reported that they were willing to undergo the same procedure again .

## Item MedMentions:test:3515
Example input:
Sentence: THL increased the production of IFN - γ , IL - 2 , and TNF - α in mice vaccinated with γ - irradiated CT - 26 - high cells .

Example answer:
{"entities": [{"text": "THL", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "IL - 2", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "vaccinated", "type": "Finding"}, {"text": "γ - irradiated", "type": "HealthCareActivity"}, {"text": "CT - 26 - high cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Collectively , these results indicate that rather than marking the most proinflammatory lymphocytes in diabetes development , IFN - γ production could represent an attempted limitation of pathogenic CD8 ( + ) T - cell activation .

Example answer:
{"entities": [{"text": "lymphocytes", "type": "AnatomicalStructure"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "CD8 ( + ) T - cell", "type": "AnatomicalStructure"}, {"text": "activation", "type": "BiologicFunction"}]}

Example input:
Sentence: 01 ) whereas increased IL - 2 and IFN - γ levels ( P < 0 . 01 ) in the serum of hepatoma H22 -bearing mice .

Example answer:
{"entities": [{"text": "IL - 2", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "serum", "type": "BodySubstance"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: The results showed that level of IFN - λ1 was 2 . 0 - fold higher in plasma of the patients with CSU than the level in healthy control ( HC ) subjects .

Example answer:
{"entities": [{"text": "IFN - λ1", "type": "Chemical"}, {"text": "plasma", "type": "BodySubstance"}, {"text": "CSU", "type": "BiologicFunction"}, {"text": "subjects", "type": "PopulationGroup"}]}

Example input:
Sentence: Serum IFN - γ and IL - 10 levels were measured by enzyme linked - immunosorbent assay .

Example answer:
{"entities": [{"text": "Serum", "type": "BodySubstance"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "enzyme linked - immunosorbent assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: Disease -protective IFN - γ could be derived from any lymphocyte source and suppressed diabetogenic CD8 ( + ) T - cell responses both directly and through an intermediary nonlymphoid cell population .

Example answer:
{"entities": [{"text": "Disease", "type": "BiologicFunction"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "lymphocyte", "type": "AnatomicalStructure"}, {"text": "diabetogenic CD8 ( + ) T - cell", "type": "AnatomicalStructure"}, {"text": "responses", "type": "BiologicFunction"}, {"text": "nonlymphoid", "type": "AnatomicalStructure"}, {"text": "cell population", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Because the levels of IFN - β were lower in AH23848 - treated mice but the level of IL - 6 was similar , over - production of pathogenic IFN - β was modulated and the generation of IFN - γ - producing T cell responses was enhanced by the inhibition of PGE2 signaling .

Example answer:
{"entities": [{"text": "IFN - β", "type": "Chemical"}, {"text": "AH23848", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "over - production", "type": "BiologicFunction"}, {"text": "pathogenic", "type": "Finding"}, {"text": "modulated", "type": "SpatialConcept"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "producing", "type": "BiologicFunction"}, {"text": "T cell", "type": "AnatomicalStructure"}, {"text": "PGE2", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}]}

Example input:
Sentence: Interferon - γ Limits Diabetogenic CD8 ( + ) T - Cell Effector Responses in Type 1 Diabetes Type 1 diabetes development in the NOD mouse model is widely reported to be dependent on high - level production by autoreactive CD4 ( + ) and CD8 ( + ) T cells of interferon - γ ( IFN - γ ) , generally considered a proinflammatory cytokine .

Example answer:
{"entities": [{"text": "Interferon - γ", "type": "Chemical"}, {"text": "Diabetogenic CD8 ( + ) T - Cell Effector", "type": "AnatomicalStructure"}, {"text": "Type 1 Diabetes", "type": "BiologicFunction"}, {"text": "Type 1 diabetes", "type": "BiologicFunction"}, {"text": "NOD mouse model", "type": "BiologicFunction"}, {"text": "CD4 ( + )", "type": "AnatomicalStructure"}, {"text": "CD8 ( + ) T cells", "type": "AnatomicalStructure"}, {"text": "interferon - γ", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "cytokine", "type": "Chemical"}]}

Example input:
Sentence: The NK cell -related cytokine release measured by IFN - γ detection was higher than that of BiKE .

Example answer:
{"entities": [{"text": "NK cell", "type": "AnatomicalStructure"}, {"text": "cytokine release", "type": "BiologicFunction"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "BiKE", "type": "Chemical"}]}

Example input:
Sentence: NK cytokine release studies showed that although the IFN - γ levels were elevated , they did not approach the levels achieved with IL - 12 / IL - 18 , indicating that release was not at the supraphysiologic level .

Example answer:
{"entities": [{"text": "NK", "type": "AnatomicalStructure"}, {"text": "cytokine release", "type": "BiologicFunction"}, {"text": "IFN - γ levels", "type": "HealthCareActivity"}, {"text": "IL - 12", "type": "Chemical"}, {"text": "IL - 18", "type": "Chemical"}]}

Input:
Sentence: The level of interferon ( IFN ) - γ release was measured because of its importance in the anti - cancer response .

## Item MedMentions:test:3365
Example input:
Sentence: The ERG expression was suppressed by miR - 96 which was increased by GM - CSF through the phosphoinositide - 3 kinase ( PI3K ) / Akt pathway .

Example answer:
{"entities": [{"text": "ERG", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "miR - 96", "type": "Chemical"}, {"text": "GM - CSF", "type": "Chemical"}, {"text": "phosphoinositide - 3 kinase", "type": "Chemical"}, {"text": "PI3K", "type": "Chemical"}, {"text": "Akt pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: IGFBP5 expression was higher estrogene receptor ( ER ) ( + ) than ER ( - ) patients ( p = 0 . 0549 ) .

Example answer:
{"entities": [{"text": "IGFBP5", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "estrogene receptor ( ER ) ( + )", "type": "Finding"}, {"text": "ER ( - )", "type": "Finding"}]}

Example input:
Sentence: The group of EGFR - positive or PTEN - positive patients with ECOG PS of 0 or 1 had better clinical outcomes than patients who were EGFR - negative and PTEN - negative or who had poor ECOG PS with longer median progression - free survival ( 2 . 1 vs 1 .

Example answer:
{"entities": [{"text": "EGFR", "type": "Chemical"}, {"text": "positive", "type": "Finding"}, {"text": "PTEN", "type": "Chemical"}, {"text": "ECOG PS", "type": "ClinicalAttribute"}, {"text": "better clinical outcomes", "type": "Finding"}, {"text": "negative", "type": "Finding"}, {"text": "progression", "type": "BiologicFunction"}]}

Example input:
Sentence: Genes commonly coaltered with ERBB2 were tumor protein 53 ( TP53 ) ( 49 % ) ; phosphatidylinositol 3 - kinase catalytic subunit alpha ( PIK3CA ) ( 42 % ) ; cadherin 1 , type 1 ( CDH1 ) ( 37 % ) ; MYC ( 17 % ) ; and cyclin D1 protein ( CCND1 ) ( 16 % ) .

Example answer:
{"entities": [{"text": "Genes", "type": "AnatomicalStructure"}, {"text": "ERBB2", "type": "AnatomicalStructure"}, {"text": "tumor protein 53", "type": "AnatomicalStructure"}, {"text": "TP53", "type": "AnatomicalStructure"}, {"text": "phosphatidylinositol 3 - kinase catalytic subunit alpha", "type": "AnatomicalStructure"}, {"text": "PIK3CA", "type": "AnatomicalStructure"}, {"text": "cadherin 1 , type 1", "type": "AnatomicalStructure"}, {"text": "CDH1", "type": "AnatomicalStructure"}, {"text": "MYC", "type": "AnatomicalStructure"}, {"text": "cyclin D1 protein", "type": "AnatomicalStructure"}, {"text": "CCND1", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Furthermore , several transcripts differentially expressed in EVs from patients versus controls mirrored differential expression between normal and breast cancer tissues .

Example answer:
{"entities": [{"text": "transcripts", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "EVs", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "normal", "type": "AnatomicalStructure"}, {"text": "breast cancer tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: PTEN was lost in 11 % ( 11 / 101 ) of G84E carriers compared to 25 % ( 25 / 99 ) of the controls ( p = 0 . 014 ) .

Example answer:
{"entities": [{"text": "PTEN", "type": "Chemical"}, {"text": "G84E carriers", "type": "BiologicFunction"}]}

Example input:
Sentence: Taken together , these data suggest that genes other than ERG and PTEN may drive carcinogenesis / progression in the majority of men with germline HOXB13 mutations .

Example answer:
{"entities": [{"text": "genes", "type": "AnatomicalStructure"}, {"text": "ERG", "type": "AnatomicalStructure"}, {"text": "PTEN", "type": "AnatomicalStructure"}, {"text": "carcinogenesis", "type": "BiologicFunction"}, {"text": "men", "type": "PopulationGroup"}, {"text": "germline HOXB13 mutations", "type": "BiologicFunction"}]}

Example input:
Sentence: EGFR ID expression ( hazard ratio [ HR ] 0 . 53 , P = 0 . 022 ) and Eastern Cooperative Oncology Group ( ECOG ) performance status ( PS ) ( HR 0 . 43 , P = 0 . 022 ) were significantly related with progression - free survival following EGFR - TKIs treatment .

Example answer:
{"entities": [{"text": "EGFR", "type": "Chemical"}, {"text": "ID", "type": "SpatialConcept"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Eastern Cooperative Oncology Group ( ECOG ) performance status ( PS )", "type": "ClinicalAttribute"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "EGFR - TKIs treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Tumors from G84E carriers generally expressed HOXB13 protein at a level comparable to benign and wild - type glands .

Example answer:
{"entities": [{"text": "Tumors", "type": "BiologicFunction"}, {"text": "G84E carriers", "type": "BiologicFunction"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "HOXB13 protein", "type": "Chemical"}, {"text": "wild - type", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We identified 101 heterozygous carriers of G84E who underwent radical prostatectomy for prostate cancer between 1985 and 2011 and matched these men by race , age and tumor grade to 99 HOXB13 wild - type controls .

Example answer:
{"entities": [{"text": "heterozygous carriers of G84E", "type": "BiologicFunction"}, {"text": "radical prostatectomy", "type": "HealthCareActivity"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "race", "type": "PopulationGroup"}, {"text": "tumor grade", "type": "BiologicFunction"}, {"text": "HOXB13", "type": "AnatomicalStructure"}, {"text": "wild - type", "type": "AnatomicalStructure"}]}

Input:
Sentence: ETS gene expression ( either ERG or ETV1 / 4 / 5 ) was seen in 36 % ( 36 / 101 ) of tumors from G84E carriers compared to 68 % ( 65 / 96 ) of the controls ( p < 0 . 0001 ) .

## Item MedMentions:test:3668
Example input:
Sentence: Between group comparison : The CD4 + percentage of group E was higher than that of group P ( P < 0 .

Example answer:
{"entities": [{"text": "CD4 + percentage", "type": "HealthCareActivity"}]}

Example input:
Sentence: Presentation of Results : Groups were not clearly different for any test at baseline .

Example answer:
{"entities": []}

Example input:
Sentence: There were significant differences between two groups ( P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: We observed additional between - group differences at the level of statistical trend .

Example answer:
{"entities": []}

Example input:
Sentence: The differences in both sets of experiments were statistically significant compared with the negative control group ( P < 0 .

Example answer:
{"entities": [{"text": "negative", "type": "Finding"}]}

Example input:
Sentence: The two groups were compared using standard bivariate methods .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: No differences were found on univariate analysis between groups in demographics or diagnosis category .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "category", "type": "IntellectualProduct"}]}

Example input:
Sentence: It was concluded that there was no significant difference in both groups in the baseline characteristics .

Example answer:
{"entities": []}

Example input:
Sentence: The two groups were homogenous in regard to all the base line variables .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: There were no other significant between group differences observed .

Example answer:
{"entities": []}

Input:
Sentence: Firstly , we investigated whether different groups could present difference in every variable .

## Item MedMentions:test:3661
Example input:
Sentence: We sought to generate a mouse model of one or more of these tumor types by targeting deletion of the Tsc1 gene to fibroblasts using the Fsp - Cre allele .

Example answer:
{"entities": [{"text": "mouse model", "type": "BiologicFunction"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "deletion", "type": "BiologicFunction"}, {"text": "Tsc1 gene", "type": "AnatomicalStructure"}, {"text": "fibroblasts", "type": "AnatomicalStructure"}, {"text": "Fsp - Cre", "type": "AnatomicalStructure"}, {"text": "allele", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Somatic Therapy of a Mouse SMA Model with a U7 snRNA Gene Correcting SMN2 Splicing Spinal Muscular Atrophy is due to the loss of SMN1 gene function .

Example answer:
{"entities": [{"text": "Somatic Therapy", "type": "HealthCareActivity"}, {"text": "Mouse", "type": "Eukaryote"}, {"text": "SMA", "type": "BiologicFunction"}, {"text": "Model", "type": "BiologicFunction"}, {"text": "U7 snRNA Gene", "type": "AnatomicalStructure"}, {"text": "SMN2", "type": "AnatomicalStructure"}, {"text": "Splicing", "type": "BiologicFunction"}, {"text": "Spinal Muscular Atrophy", "type": "BiologicFunction"}, {"text": "SMN1", "type": "AnatomicalStructure"}, {"text": "gene function", "type": "BiologicFunction"}]}

Example input:
Sentence: Mechanism of motor coordination of masseter and temporalis muscles for increased masticatory efficiency in mice The demand for the use of mice as animal models for elucidating the pathophysiologies and pathogeneses of oral motor disorders has been increasing in recent years , as more and more kinds of genetically modified mice that express functional disorders of the stomatognathic system become available .

Example answer:
{"entities": [{"text": "motor coordination", "type": "BiologicFunction"}, {"text": "masseter", "type": "AnatomicalStructure"}, {"text": "temporalis muscles", "type": "AnatomicalStructure"}, {"text": "masticatory", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "animal models", "type": "Eukaryote"}, {"text": "pathogeneses", "type": "BiologicFunction"}, {"text": "oral", "type": "SpatialConcept"}, {"text": "motor disorders", "type": "BiologicFunction"}, {"text": "functional disorders", "type": "BiologicFunction"}, {"text": "stomatognathic system", "type": "BodySystem"}]}

Example input:
Sentence: Two dedifferentiated - SFT ( D - SFT ) models obtained from patients ' biopsies were grown in immunodeficient mice .

Example answer:
{"entities": [{"text": "dedifferentiated - SFT", "type": "BiologicFunction"}, {"text": "D - SFT", "type": "BiologicFunction"}, {"text": "models", "type": "IntellectualProduct"}, {"text": "biopsies", "type": "HealthCareActivity"}, {"text": "immunodeficient mice", "type": "Eukaryote"}]}

Example input:
Sentence: These convergent findings from mouse and hiPSC SZ models provide evidence for STEP61 dysfunction in SZ .Molecular Psychiatry advance online publication , 18 October 2016 ; doi : 10 . 1038 / mp . 2016 .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "hiPSC", "type": "AnatomicalStructure"}, {"text": "SZ", "type": "BiologicFunction"}, {"text": "models", "type": "BiologicFunction"}, {"text": "STEP61", "type": "Chemical"}]}

Example input:
Sentence: For evaluation of novel drugs , the Syrian golden hamster is considered as a clinically relevant laboratory model .

Example answer:
{"entities": [{"text": "evaluation", "type": "HealthCareActivity"}, {"text": "drugs", "type": "Chemical"}, {"text": "Syrian golden hamster", "type": "Eukaryote"}, {"text": "laboratory model", "type": "IntellectualProduct"}]}

Example input:
Sentence: Furthermore , we show that cell culture - validated genetic modifications can be readily applied to mouse embryonic stem cells ( mESCs ) for the generation of corresponding mouse models .

Example answer:
{"entities": [{"text": "cell culture - validated genetic modifications", "type": "ResearchActivity"}, {"text": "mouse embryonic stem cells", "type": "AnatomicalStructure"}, {"text": "mESCs", "type": "AnatomicalStructure"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "models", "type": "Eukaryote"}]}

Example input:
Sentence: aureus in a murine infection model .

Example answer:
{"entities": [{"text": "aureus", "type": "Bacterium"}, {"text": "murine infection model", "type": "BiologicFunction"}]}

Example input:
Sentence: The melanoma mouse model in vivo study further supports the in vitro findings .

Example answer:
{"entities": [{"text": "melanoma", "type": "BiologicFunction"}, {"text": "mouse model", "type": "BiologicFunction"}]}

Example input:
Sentence: A peritoneal sepsis murine model was used to evaluate the in vivo impact .

Example answer:
{"entities": [{"text": "peritoneal sepsis murine model", "type": "Eukaryote"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Input:
Sentence: By using a murine model of S .

## Item MedMentions:test:3476
Example input:
Sentence: In addition , we used the heterogeneous silicon mesostructures to design a lipid - bilayer -supported bioelectric interface that is remotely controlled and temporally transient , and that permits non - genetic and subcellular optical modulation of the electrophysiology dynamics in single dorsal root ganglia neurons .

Example answer:
{"entities": [{"text": "silicon", "type": "Chemical"}, {"text": "mesostructures", "type": "Chemical"}, {"text": "lipid - bilayer", "type": "AnatomicalStructure"}, {"text": "remotely", "type": "SpatialConcept"}, {"text": "subcellular", "type": "AnatomicalStructure"}, {"text": "dorsal root ganglia", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The application of such intermediary layer formed during electroreduction of appropriate diazonium salt at CV peak potential guarantees high efficiency of hybridization process and thus fully available places for VB2 interaction .

Example answer:
{"entities": [{"text": "intermediary", "type": "SpatialConcept"}, {"text": "diazonium salt", "type": "Chemical"}, {"text": "VB2", "type": "Chemical"}]}

Example input:
Sentence: An ion - gating multinanochannel system based on a copper - responsive self - cleaving DNAzyme We developed an ion - gating nanochannel composite system by immobilizing a Cu ( 2 + ) - responsive self - cleaving DNAzyme into PET conical multinanochannels , which could control the ion transport by regulating the surface charge density of the channels .

Example answer:
{"entities": [{"text": "copper", "type": "Chemical"}, {"text": "cleaving", "type": "SpatialConcept"}, {"text": "DNAzyme", "type": "Chemical"}, {"text": "Cu ( 2 + )", "type": "Chemical"}, {"text": "PET", "type": "Chemical"}, {"text": "conical multinanochannels", "type": "Chemical"}, {"text": "ion transport", "type": "BiologicFunction"}, {"text": "regulating", "type": "BiologicFunction"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "channels", "type": "Chemical"}]}

Example input:
Sentence: To improve MWCNT wettability , oxygen plasma etching has been applied to promote MWCNT exfoliation and oxidation and to produce graphene oxide ( GO ) at the end of the tips .

Example answer:
{"entities": [{"text": "MWCNT", "type": "Chemical"}, {"text": "oxidation", "type": "BiologicFunction"}, {"text": "graphene oxide", "type": "Chemical"}, {"text": "GO", "type": "Chemical"}]}

Example input:
Sentence: SssI MTase -protected dumbbell template -mediated RCA proceed in a multiple primers -like exponential mode , thus providing the RCA with high amplification efficiency .

Example answer:
{"entities": [{"text": "SssI MTase", "type": "Chemical"}, {"text": "RCA", "type": "ResearchActivity"}, {"text": "multiple primers", "type": "Chemical"}, {"text": "amplification", "type": "BiologicFunction"}]}

Example input:
Sentence: Carbon nanotube -based self - adhesive polymer electrodes for wireless long - term recording of electrocardiogram signals In this study , the concept of polymer electrodes integrated with a wireless electrocardiogram ( ECG ) system was described .

Example answer:
{"entities": [{"text": "Carbon nanotube", "type": "Chemical"}, {"text": "self - adhesive", "type": "Chemical"}, {"text": "polymer", "type": "Chemical"}, {"text": "electrocardiogram signals", "type": "Finding"}, {"text": "electrocardiogram", "type": "Finding"}, {"text": "ECG", "type": "Finding"}]}

Example input:
Sentence: Polymer electrodes for long - term ECG measurements were fabricated by loading high content of carbon nanotubes ( CNTs ) in polydimethylsiloxane .

Example answer:
{"entities": [{"text": "Polymer", "type": "Chemical"}, {"text": "carbon nanotubes", "type": "Chemical"}, {"text": "CNTs", "type": "Chemical"}, {"text": "polydimethylsiloxane", "type": "Chemical"}]}

Example input:
Sentence: The 60 - mm electrode spacing was the most successful bipolar configuration .

Example answer:
{"entities": [{"text": "electrode", "type": "MedicalDevice"}, {"text": "bipolar", "type": "SpatialConcept"}, {"text": "configuration", "type": "SpatialConcept"}]}

Example input:
Sentence: Monolayer GO sheets were assembled onto interdigitated electrodes , followed by reduction through linear sweep voltammetry and then modification with a single - stranded DNA aptamer .

Example answer:
{"entities": [{"text": "GO", "type": "Chemical"}, {"text": "electrodes", "type": "MedicalDevice"}, {"text": "single - stranded DNA", "type": "Chemical"}, {"text": "aptamer", "type": "Chemical"}]}

Example input:
Sentence: High Performance Reduction of H2O2 with an Electron Transport Decaheme Cytochrome on a Porous ITO Electrode The decaheme cytochrome MtrC from Shewanella oneidensis MR - 1 immobilized on an ITO electrode displays unprecedented H2O2 reduction activity .

Example answer:
{"entities": [{"text": "H2O2", "type": "Chemical"}, {"text": "Electron Transport", "type": "BiologicFunction"}, {"text": "Decaheme Cytochrome", "type": "Chemical"}, {"text": "ITO", "type": "Chemical"}, {"text": "decaheme cytochrome MtrC", "type": "Chemical"}, {"text": "Shewanella oneidensis MR - 1", "type": "Bacterium"}, {"text": "immobilized", "type": "Chemical"}]}

Input:
Sentence: A hierarchical ITO electrode enabled optimal immobilization of MtrC and a high current density of 1 mA cm ( - 2 ) at 0 .

## Item MedMentions:test:3634
Example input:
Sentence: Unfortunately , the provision of individualized , timely feedback can be particularly challenging in first - year courses as they tend to be large and diverse cohort classes that pose challenges of time and logistics .

Example answer:
{"entities": [{"text": "feedback", "type": "BiologicFunction"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "classes", "type": "IntellectualProduct"}]}

Example input:
Sentence: Some medical student cohorts undertook brief empathy training , whereas others had no exposure .

Example answer:
{"entities": [{"text": "medical student", "type": "ProfessionalOrOccupationalGroup"}, {"text": "cohorts", "type": "PopulationGroup"}]}

Example input:
Sentence: Higher - achieving students , and students whose exam grades improved in the first half of the semester , reported using specific cognitive and metacognitive strategies significantly more frequently than their lower - achieving peers .

Example answer:
{"entities": [{"text": "students", "type": "PopulationGroup"}, {"text": "grades", "type": "IntellectualProduct"}, {"text": "improved", "type": "Finding"}, {"text": "cognitive", "type": "BiologicFunction"}, {"text": "metacognitive strategies", "type": "BiologicFunction"}, {"text": "peers", "type": "PopulationGroup"}]}

Example input:
Sentence: Our results showed that younger patients managed to achieve a higher level of functioning in educational level , marital status , and social contacts .

Example answer:
{"entities": [{"text": "educational level", "type": "Finding"}, {"text": "social contacts", "type": "Finding"}]}

Example input:
Sentence: Students ' familiarity with LGBT terminology and demographics increased significantly after the session .

Example answer:
{"entities": [{"text": "Students", "type": "PopulationGroup"}, {"text": "familiarity", "type": "BiologicFunction"}, {"text": "LGBT", "type": "PopulationGroup"}, {"text": "terminology", "type": "IntellectualProduct"}]}

Example input:
Sentence: The present study revealed a higher level of satisfaction among professionals with graduate studies ( human resources policy and activities developed ) and civil servants ( wage policy and work schedule ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "satisfaction", "type": "BiologicFunction"}, {"text": "human resources policy", "type": "IntellectualProduct"}, {"text": "civil servants", "type": "ProfessionalOrOccupationalGroup"}, {"text": "policy", "type": "IntellectualProduct"}]}

Example input:
Sentence: Professionals with graduate studies were more satisfied with the human resources policy and the activities developed , whereas health civil servants showed more satisfaction with the wage policy and the work schedule .

Example answer:
{"entities": [{"text": "Professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "satisfied", "type": "IntellectualProduct"}, {"text": "human resources policy", "type": "IntellectualProduct"}, {"text": "health", "type": "HealthCareActivity"}, {"text": "civil servants", "type": "ProfessionalOrOccupationalGroup"}, {"text": "satisfaction", "type": "BiologicFunction"}, {"text": "policy", "type": "IntellectualProduct"}]}

Example input:
Sentence: The study also showed that if a training on the given subject was organized , 60 % of respondents would be willing to participate in it .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "respondents", "type": "PopulationGroup"}, {"text": "willing", "type": "Finding"}]}

Example input:
Sentence: Participants ' self - reported level of knowledge , skill and capacity in identifying priorities , engaging men and influencing practice beyond their own organisation increased immediately following training ( P < 0 . 001 ) and , with the exception of improving capacity to engage men and influencing practice beyond their organisation , these improvements were sustained at 5 - month post training ( P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "Participants '", "type": "PopulationGroup"}, {"text": "self - reported level of knowledge", "type": "Finding"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: Postgraduate training was characterised by work - life imbalance .

Example answer:
{"entities": []}

Input:
Sentence: In addition , recent graduates were more likely to report having had training on this topic than older graduates .

## Item MedMentions:test:3467
Example input:
Sentence: Furthermore , the nano - UCPs were superior to a traditional two - camera method for NIR and visible light path alignment in an in vivo Infrared - Laser - Evoked Gene Operator ( IR - LEGO ) optogenetics assay in the budding yeast Saccharomyces cerevisiae .

Example answer:
{"entities": [{"text": "UCPs", "type": "Chemical"}, {"text": "camera", "type": "MedicalDevice"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "Infrared - Laser - Evoked Gene Operator ( IR - LEGO ) optogenetics assay", "type": "ResearchActivity"}, {"text": "Saccharomyces cerevisiae", "type": "Eukaryote"}]}

Example input:
Sentence: Transcutaneous electrical stimulation was applied for 2 min to the right postero - lateral surface of the neck during scan # 1 ( control condition , sternocleidomastoid stimulation : " SCM " ) and to the right antero - lateral surface of the neck during scan # 2 ( experimental condition , non - invasive vagus nerve stimulation : " nVNS " ) .

Example answer:
{"entities": [{"text": "Transcutaneous electrical stimulation", "type": "HealthCareActivity"}, {"text": "right postero - lateral surface of the neck", "type": "SpatialConcept"}, {"text": "scan", "type": "HealthCareActivity"}, {"text": "sternocleidomastoid", "type": "AnatomicalStructure"}, {"text": "stimulation", "type": "Finding"}, {"text": "SCM", "type": "Finding"}, {"text": "right antero - lateral surface of the neck", "type": "SpatialConcept"}, {"text": "vagus nerve stimulation", "type": "HealthCareActivity"}, {"text": "nVNS", "type": "HealthCareActivity"}]}

Example input:
Sentence: To evaluate the effectiveness of a vein visualization display system using near - infrared light ( " Vein Display " ) for the safe and proper selection of venipuncture sites for indwelling needle placement in the forearm .

Example answer:
{"entities": [{"text": "vein visualization display system", "type": "MedicalDevice"}, {"text": "Vein Display", "type": "MedicalDevice"}, {"text": "venipuncture", "type": "HealthCareActivity"}, {"text": "sites", "type": "SpatialConcept"}, {"text": "needle", "type": "MedicalDevice"}, {"text": "forearm", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Cortical - ventral striatum ( VS ) circuitry is a common target of psychobehavioral interventions in drug addiction , and cortical - VS dysfunction has been reported in IGD ; hence , the primary aim of the study was to investigate how the VS circuitry responds to psychobehavioral interventions in IGD .

Example answer:
{"entities": [{"text": "Cortical", "type": "SpatialConcept"}, {"text": "ventral striatum", "type": "AnatomicalStructure"}, {"text": "VS", "type": "AnatomicalStructure"}, {"text": "psychobehavioral interventions", "type": "HealthCareActivity"}, {"text": "drug addiction", "type": "BiologicFunction"}, {"text": "cortical", "type": "SpatialConcept"}, {"text": "IGD", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: This study highlights the practicality and versatility of albumin -mediated biomimetic mineralization of a nanotheranostic agent and also suggests that bioinspired Gd : CuS @ BSA NPs possess promising imaging guidance and effective tumor ablation properties , with high spatial resolution and deep tissue penetration .

Example answer:
{"entities": [{"text": "albumin", "type": "Chemical"}, {"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "BSA", "type": "Chemical"}, {"text": "imaging guidance", "type": "HealthCareActivity"}, {"text": "tumor ablation properties", "type": "HealthCareActivity"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Access to Vagal Projections via Cutaneous Electrical Stimulation of the Neck : fMRI Evidence in Healthy Humans Stimulation of the vagus nerve via implanted electrodes is currently used to treat refractory epilepsy and depression .

Example answer:
{"entities": [{"text": "Access", "type": "SpatialConcept"}, {"text": "Vagal Projections", "type": "SpatialConcept"}, {"text": "Cutaneous Electrical Stimulation", "type": "HealthCareActivity"}, {"text": "Neck", "type": "SpatialConcept"}, {"text": "fMRI", "type": "HealthCareActivity"}, {"text": "Humans", "type": "Eukaryote"}, {"text": "Stimulation of the vagus nerve", "type": "HealthCareActivity"}, {"text": "treat", "type": "HealthCareActivity"}, {"text": "refractory epilepsy", "type": "BiologicFunction"}, {"text": "depression", "type": "BiologicFunction"}]}

Example input:
Sentence: Two analyses were conducted using FSL ( whole - brain and brainstem ; corrected , p < 0 . 01 ) to determine whether nVNS activated vagal projections in the brainstem and forebrain , compared to baseline and SCM stimulation .

Example answer:
{"entities": [{"text": "FSL", "type": "IntellectualProduct"}, {"text": "whole - brain", "type": "AnatomicalStructure"}, {"text": "brainstem", "type": "AnatomicalStructure"}, {"text": "nVNS", "type": "HealthCareActivity"}, {"text": "vagal", "type": "AnatomicalStructure"}, {"text": "projections", "type": "SpatialConcept"}, {"text": "forebrain", "type": "AnatomicalStructure"}, {"text": "SCM stimulation", "type": "Finding"}]}

Example input:
Sentence: Compared to baseline and control ( SCM ) stimulation , nVNS significantly activated primary vagal projections including : nucleus of the solitary tract ( primary central relay of vagal afferents ) , parabrachial area , primary sensory cortex , and insula .

Example answer:
{"entities": [{"text": "( SCM ) stimulation", "type": "Finding"}, {"text": "nVNS", "type": "HealthCareActivity"}, {"text": "primary vagal", "type": "AnatomicalStructure"}, {"text": "projections", "type": "SpatialConcept"}, {"text": "nucleus of the solitary tract", "type": "AnatomicalStructure"}, {"text": "vagal afferents", "type": "AnatomicalStructure"}, {"text": "parabrachial area", "type": "AnatomicalStructure"}, {"text": "primary sensory cortex", "type": "AnatomicalStructure"}, {"text": "insula", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Simulated volume of tissue activated ( VTA ) , using clinical electrode placements , are recorded along with patient outcomes in the Unified Parkinson 's disease rating scale ( UPDRS ) .

Example answer:
{"entities": [{"text": "Simulated", "type": "ResearchActivity"}, {"text": "clinical electrode placements", "type": "HealthCareActivity"}, {"text": "Unified Parkinson 's disease rating scale", "type": "IntellectualProduct"}, {"text": "UPDRS", "type": "IntellectualProduct"}]}

Example input:
Sentence: Visualization for Understanding Uncertainty in Activation Volumes for Deep Brain Stimulation We have created the Neurostimulation Uncertainty Viewer ( nuView or νView ) tool for exploring data arising from deep brain stimulation ( DBS ) .

Example answer:
{"entities": [{"text": "Uncertainty", "type": "Finding"}, {"text": "Deep Brain Stimulation", "type": "HealthCareActivity"}, {"text": "Neurostimulation Uncertainty Viewer ( nuView or νView ) tool", "type": "IntellectualProduct"}, {"text": "deep brain stimulation", "type": "HealthCareActivity"}, {"text": "DBS", "type": "HealthCareActivity"}]}

Input:
Sentence: νView provides a collection of visual methods to explore the activated tissue to enhance understanding of electrode usage for improved therapy with DBS .

## Item MedMentions:test:3368
Example input:
Sentence: The activation of cPLA2α is mediated by ERK activity .

Example answer:
{"entities": [{"text": "cPLA2α", "type": "Chemical"}, {"text": "ERK activity", "type": "BiologicFunction"}]}

Example input:
Sentence: The early activation of STAT1α ( detected by phospho - serine727 and phoshpo - tyrosine701 ) by IFNγ and the late activation of STAT1α by LPS were not affected in the presence of cPLA2α inhibitors , indicating that STAT1α is not under cPLA2α regulation .

Example answer:
{"entities": [{"text": "STAT1α", "type": "Chemical"}, {"text": "phospho - serine727", "type": "Chemical"}, {"text": "phoshpo - tyrosine701", "type": "Chemical"}, {"text": "IFNγ", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "cPLA2α", "type": "Chemical"}, {"text": "inhibitors", "type": "Chemical"}, {"text": "regulation", "type": "BiologicFunction"}]}

Example input:
Sentence: The results of Western blot analysis , confocal microscopy , and a DNA binding activity assay revealed that the classical NF - κB pathway was activated by ApxI , as evidenced by the decreased levels of IκB and subsequent NF - κB translocation and activation in ApxI -stimulated PAMs .

Example answer:
{"entities": [{"text": "Western blot analysis", "type": "HealthCareActivity"}, {"text": "confocal microscopy", "type": "HealthCareActivity"}, {"text": "DNA binding", "type": "BiologicFunction"}, {"text": "activity assay", "type": "HealthCareActivity"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "ApxI", "type": "Chemical"}, {"text": "IκB", "type": "Chemical"}, {"text": "translocation", "type": "BiologicFunction"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "PAMs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Notably , the attenuation of JNK activation by a specific inhibitor ( SP600125 ) reduced ApxI -induced NF - κB activation , whereas a p38 blocker ( SB203580 ) had no effect on the NF - κB pathway .

Example answer:
{"entities": [{"text": "JNK", "type": "Chemical"}, {"text": "SP600125", "type": "Chemical"}, {"text": "ApxI", "type": "Chemical"}, {"text": "NF - κB activation", "type": "BiologicFunction"}, {"text": "p38 blocker", "type": "Chemical"}, {"text": "SB203580", "type": "Chemical"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , in the presence of si - cPLA2 or PYR , MGO no longer decreased NF - κB phosphorylation .

Example answer:
{"entities": [{"text": "si - cPLA2", "type": "Chemical"}, {"text": "PYR", "type": "Chemical"}, {"text": "MGO", "type": "Chemical"}, {"text": "no longer decreased", "type": "Finding"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}]}

Example input:
Sentence: The activation of cPLA2 by LPS was mediated by both adaptor proteins downstream to LPS receptor ; TRIF and MyD88 , while the activation of cPLA2α by IFNγ was mediated by the secreted TNF - α at 4 h .

Example answer:
{"entities": [{"text": "cPLA2", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "adaptor proteins", "type": "Chemical"}, {"text": "downstream", "type": "SpatialConcept"}, {"text": "LPS receptor", "type": "Chemical"}, {"text": "TRIF", "type": "BiologicFunction"}, {"text": "MyD88", "type": "BiologicFunction"}, {"text": "cPLA2α", "type": "Chemical"}, {"text": "IFNγ", "type": "Chemical"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "TNF - α", "type": "Chemical"}]}

Example input:
Sentence: Cumulatively , our results indicate that cPLA2α may serve as a pivotal amplifier of the inflammatory response in the CNS .

Example answer:
{"entities": [{"text": "cPLA2α", "type": "Chemical"}, {"text": "inflammatory response", "type": "BiologicFunction"}, {"text": "CNS", "type": "BodySystem"}]}

Example input:
Sentence: Our previous study demonstrated that the reduction of cytosolic phospholipase A2 alpha ( cPLA2α ) protein overexpression and activation in the spinal cord of a mouse model of ALS , hmSOD1 G93A , inhibited CD40 upregulation in microglia .

Example answer:
{"entities": [{"text": "cytosolic phospholipase A2 alpha", "type": "Chemical"}, {"text": "cPLA2α", "type": "Chemical"}, {"text": "protein overexpression", "type": "BiologicFunction"}, {"text": "spinal cord", "type": "AnatomicalStructure"}, {"text": "mouse model", "type": "BiologicFunction"}, {"text": "ALS", "type": "BiologicFunction"}, {"text": "hmSOD1 G93A", "type": "Chemical"}, {"text": "inhibited", "type": "BiologicFunction"}, {"text": "CD40", "type": "Chemical"}, {"text": "upregulation", "type": "BiologicFunction"}, {"text": "microglia", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Suppression of cPLA2α activity inhibited superoxide production by NOX2 - NADPH oxidase and activation of NF - κB detected by the phosphorylation of p65 on serine 536 at 15 min by LPS and at 4 h by IFNγ .

Example answer:
{"entities": [{"text": "cPLA2α", "type": "Chemical"}, {"text": "superoxide production by NOX2 - NADPH oxidase", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "serine 536", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "IFNγ", "type": "Chemical"}]}

Example input:
Sentence: Our results show for the first time that cPLA2 upregulates CD40 protein expression induced by either LPS or IFNγ , and this regulatory effect is mediated via the activation of NOX2 - NADPH oxidase and NF - κB .

Example answer:
{"entities": [{"text": "cPLA2", "type": "Chemical"}, {"text": "upregulates", "type": "BiologicFunction"}, {"text": "CD40", "type": "Chemical"}, {"text": "protein expression", "type": "BiologicFunction"}, {"text": "LPS", "type": "Chemical"}, {"text": "IFNγ", "type": "Chemical"}, {"text": "regulatory", "type": "BiologicFunction"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "NOX2 - NADPH oxidase", "type": "Chemical"}, {"text": "NF - κB", "type": "Chemical"}]}

Input:
Sentence: Inhibition of NOX2 prevented NF - κB activation and CD40 induction but did not affect cPLA2α activation , suggesting cPLA2α is located upstream to NOX2 and NF - κB .

## Item MedMentions:test:3526
Example input:
Sentence: Of them , 69 . 2 % reported benefits from PDE5i usage , mainly in the form of enhancement of erection ( 36 . 7 % ) and increasing erection duration ( 31 . 2 % ) .

Example answer:
{"entities": [{"text": "reported", "type": "HealthCareActivity"}, {"text": "PDE5i", "type": "Chemical"}, {"text": "erection", "type": "BiologicFunction"}, {"text": "erection duration", "type": "Finding"}]}

Example input:
Sentence: Over 4 years ( between Jan 2011 and Jan 2015 ) , all cases of severe hypospadias were included in this study ; except those with prior attempts at repair , circumcised cases , and cases with severe hypogonadism - because of partial androgen insensitivity - not responding to hormonal manipulations .

Example answer:
{"entities": [{"text": "hypospadias", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "attempts at repair", "type": "HealthCareActivity"}, {"text": "circumcised", "type": "Finding"}, {"text": "hypogonadism", "type": "BiologicFunction"}, {"text": "partial androgen insensitivity", "type": "BiologicFunction"}, {"text": "hormonal manipulations", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients who received EBRT were significantly more likely to experience a decrease in more than one functional domain ( urinary , sexual , bowel , or hormonal ) at 1 year when compared with those on AS ( 60 % vs . 28 % , P = 0 .

Example answer:
{"entities": [{"text": "EBRT", "type": "HealthCareActivity"}, {"text": "sexual", "type": "BiologicFunction"}, {"text": "bowel", "type": "AnatomicalStructure"}, {"text": "AS", "type": "HealthCareActivity"}]}

Example input:
Sentence: 2 % and 0 % ( p = 0 . 50 ) Conclusion : Partial ablation results in better post - treatment sexual function compared to whole - gland ablation in men with intermediate - risk prostate cancer .

Example answer:
{"entities": [{"text": "ablation", "type": "HealthCareActivity"}, {"text": "sexual function", "type": "BiologicFunction"}, {"text": "gland", "type": "AnatomicalStructure"}, {"text": "men", "type": "PopulationGroup"}, {"text": "intermediate - risk", "type": "Finding"}, {"text": "prostate cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Vessel - sparing radiotherapy appears to more effectively preserve erectile function when compared to historical series and model -predicted outcomes following nerve - sparing RP or conventional radiotherapy , with maintenance of tumor control .

Example answer:
{"entities": [{"text": "Vessel - sparing radiotherapy", "type": "HealthCareActivity"}, {"text": "erectile function", "type": "BiologicFunction"}, {"text": "model", "type": "IntellectualProduct"}, {"text": "nerve - sparing RP", "type": "HealthCareActivity"}, {"text": "conventional radiotherapy", "type": "HealthCareActivity"}, {"text": "tumor control", "type": "Finding"}]}

Example input:
Sentence: At 5 yr , 88 % of patients were sexually active with or without the use of sexual aids .

Example answer:
{"entities": [{"text": "sexually active", "type": "Finding"}]}

Example input:
Sentence: Functional patency at 2 years was 69 % for those aged > 75 years compared to 78 % - 81 % for younger patients .

Example answer:
{"entities": [{"text": "patency", "type": "BiologicFunction"}]}

Example input:
Sentence: Of 139 pairs , the 12 - month rate of successful intercourse was 29 . 5 % for whole - gland and 46 . 8 % for partial ablation ( OR 2 .

Example answer:
{"entities": [{"text": "intercourse", "type": "BiologicFunction"}, {"text": "gland", "type": "AnatomicalStructure"}, {"text": "ablation", "type": "HealthCareActivity"}]}

Example input:
Sentence: The percentage of patients who shifted from SD at baseline to normal sexual functioning at EOT was higher in males ( placebo , 40 . 6 % ; vilazodone , 35 . 7 % ) than in females ( placebo , 24 . 9 % ; vilazodone , 34 . 9 % ) ; no statistical testing was performed .

Example answer:
{"entities": [{"text": "SD", "type": "BiologicFunction"}, {"text": "sexual functioning", "type": "BiologicFunction"}, {"text": "males", "type": "PopulationGroup"}, {"text": "placebo", "type": "Chemical"}, {"text": "vilazodone", "type": "Chemical"}, {"text": "females", "type": "PopulationGroup"}]}

Example input:
Sentence: Both physician - and patient -reported inventories were used to capture erectile function at baseline and at 2 and 5 yr after treatment .

Example answer:
{"entities": [{"text": "physician", "type": "ProfessionalOrOccupationalGroup"}, {"text": "erectile function", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Input:
Sentence: At 2 yr after treatment , 87 % of baseline - potent men retained erections suitable for intercourse .

## Item MedMentions:test:3753
Example input:
Sentence: 37 to 11 . 58 ) ; p < 0 . 0001 ) than those persistent .

Example answer:
{"entities": []}

Example input:
Sentence: 95 - 0 . 99 ) and OS ( HR = 0 . 94 ; 95 % CI 0 . 91 - 0 . 97 ) as well as from the first to the third chemotherapy cycle for OS ( HR = 0 .

Example answer:
{"entities": [{"text": "chemotherapy cycle", "type": "HealthCareActivity"}]}

Example input:
Sentence: The advent of the direct - acting oral anticoagulants such as rivaroxaban has made it easier than ever to manage patients outside of the hospital .

Example answer:
{"entities": [{"text": "direct - acting oral anticoagulants", "type": "Chemical"}, {"text": "rivaroxaban", "type": "Chemical"}, {"text": "manage patients", "type": "HealthCareActivity"}, {"text": "hospital", "type": "Organization"}]}

Example input:
Sentence: Baseline - adjusted completion rates for all HRQoL questionnaires across treatment arms were 65 % and 70 % for dacarbazine and nivolumab , respectively , and remained similar throughout treatment .

Example answer:
{"entities": [{"text": "questionnaires", "type": "IntellectualProduct"}, {"text": "treatment arms", "type": "HealthCareActivity"}, {"text": "dacarbazine", "type": "Chemical"}, {"text": "nivolumab", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Of the patients with 1 or no dose - reduction criteria assigned to receive the 5 mg twice daily dose of apixaban or warfarin , 3966 had 1 dose - reduction criterion ; these patients had higher rates of stroke or systemic embolism ( HR , 1 . 47 ; 95 % CI , 1 . 20 - 1 . 81 ) and major bleeding ( HR , 1 . 89 ; 95 % CI , 1 . 62 - 2 . 20 ) compared with those with no dose - reduction criteria ( n = 13 356 ) .

Example answer:
{"entities": [{"text": "apixaban", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "bleeding", "type": "BiologicFunction"}]}

Example input:
Sentence: Non - persistence was defined as a gap in dabigatran or rivaroxaban prescriptions ≥14 days .

Example answer:
{"entities": [{"text": "Non - persistence", "type": "Finding"}, {"text": "dabigatran", "type": "Chemical"}, {"text": "rivaroxaban", "type": "Chemical"}, {"text": "prescriptions", "type": "IntellectualProduct"}]}

Example input:
Sentence: NOAC non - persistence rates are high in clinical practice , with approximately one in three patients becoming non - persistent to dabigatran or rivaroxaban within 6 months after drug initiation .

Example answer:
{"entities": [{"text": "NOAC", "type": "Chemical"}, {"text": "non - persistence", "type": "Finding"}, {"text": "clinical practice", "type": "IntellectualProduct"}, {"text": "non - persistent", "type": "Finding"}, {"text": "dabigatran", "type": "Chemical"}, {"text": "rivaroxaban", "type": "Chemical"}, {"text": "drug", "type": "Chemical"}]}

Example input:
Sentence: 7 year ) and 10 119 rivaroxaban users ( age 77 . 0±7 . 1 year ) with women comprising 52 % of each medication group .

Example answer:
{"entities": [{"text": "rivaroxaban", "type": "Chemical"}, {"text": "women", "type": "PopulationGroup"}, {"text": "medication group", "type": "PopulationGroup"}]}

Example input:
Sentence: 9 % of patients were non - persistent to rivaroxaban .

Example answer:
{"entities": [{"text": "non - persistent", "type": "Finding"}, {"text": "rivaroxaban", "type": "Chemical"}]}

Example input:
Sentence: 59 to 5 . 43 ) ; p < 0 . 0001 ) and rivaroxaban ( HR 6 . 25 ( 95 % CI 3 .

Example answer:
{"entities": [{"text": "rivaroxaban", "type": "Chemical"}]}

Input:
Sentence: 60 to 1 . 94 ) ; p < 0 . 0001 ) or rivaroxaban ( HR 1 . 89 ( 95 % CI 1 . 64 to 2 . 19 ) ; p < 0 . 0001 ) compared with those who were persistent .

## Item MedMentions:test:3581
Example input:
Sentence: A quasi - experimental study of a reminiscence program focused on autobiographical memory in institutionalized older adults with cognitive impairment Working with past memories through reminiscence interventions has been practiced for several decades with successful outcomes on mental health in older adults .

Example answer:
{"entities": [{"text": "quasi - experimental study", "type": "ResearchActivity"}, {"text": "reminiscence program", "type": "HealthCareActivity"}, {"text": "autobiographical memory", "type": "BiologicFunction"}, {"text": "older adults", "type": "PopulationGroup"}, {"text": "cognitive impairment", "type": "BiologicFunction"}, {"text": "past memories", "type": "BiologicFunction"}, {"text": "reminiscence interventions", "type": "HealthCareActivity"}, {"text": "mental health", "type": "BiologicFunction"}]}

Example input:
Sentence: The use of simulation in graduate medical education has gained significant traction as a way to provide trainees with exposure to various techniques and procedures before use on the general patient population .

Example answer:
{"entities": [{"text": "simulation", "type": "ResearchActivity"}, {"text": "trainees", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Efficient patient modeling for visuo - haptic VR simulation using a generic patient atlas This work presents a new time - saving virtual patient modeling system by way of example for an existing visuo - haptic training and planning virtual reality ( VR ) system for percutaneous transhepatic cholangio - drainage ( PTCD ) .

Example answer:
{"entities": [{"text": "modeling", "type": "ResearchActivity"}, {"text": "atlas", "type": "IntellectualProduct"}, {"text": "modeling system", "type": "ResearchActivity"}, {"text": "percutaneous transhepatic cholangio - drainage", "type": "HealthCareActivity"}, {"text": "PTCD", "type": "HealthCareActivity"}]}

Example input:
Sentence: Based on a cohort of 17 PD patients and 20 healthy controls , we assessed how naïve raters judge the emotion and emotional intensity displayed in dynamic facial expressions as adults with and without PD watched emotionally evocative films ( Experiment 1 ) , and how age -matched peers naïve to patients ' disease status judge their social desirability along various dimensions from audiovisual stimuli ( interview excerpts ) recorded after certain films ( Experiment 2 ) .

Example answer:
{"entities": [{"text": "cohort", "type": "PopulationGroup"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "emotion", "type": "BiologicFunction"}, {"text": "emotional", "type": "Finding"}, {"text": "facial expressions", "type": "Finding"}, {"text": "emotionally", "type": "BiologicFunction"}, {"text": "films", "type": "IntellectualProduct"}, {"text": "Experiment", "type": "ResearchActivity"}, {"text": "peers", "type": "PopulationGroup"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "audiovisual", "type": "IntellectualProduct"}, {"text": "interview excerpts", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Participants attending reminiscence sessions exhibited better outcomes compared to the control group in cognition , anxiety and depression ( p < 0 . 001 ) , and presented a higher number of retrieved autobiographical events , specificity of evoked memories and positive valence of events ( p < 0 . 001 ) , and also presented lower latency time for recalling events , and lower negative recalled events ( p < 0 .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "cognition", "type": "BiologicFunction"}, {"text": "anxiety", "type": "BiologicFunction"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "retrieved", "type": "BiologicFunction"}, {"text": "memories", "type": "BiologicFunction"}, {"text": "recalling", "type": "BiologicFunction"}, {"text": "recalled", "type": "BiologicFunction"}]}

Example input:
Sentence: We demonstrate that our approach has the potential to aid in the development of automated functional brain mapping using continuous video and neural recordings of patients in clinical settings .

Example answer:
{"entities": [{"text": "automated functional brain mapping", "type": "HealthCareActivity"}, {"text": "video and neural recordings", "type": "IntellectualProduct"}]}

Example input:
Sentence: Twenty - two groups with 120 fifth - year students were each assigned paper - based problem - based learning and video -based problem - based learning using patient -simulated videos .

Example answer:
{"entities": [{"text": "students", "type": "PopulationGroup"}, {"text": "video", "type": "IntellectualProduct"}, {"text": "patient -simulated videos", "type": "IntellectualProduct"}]}

Example input:
Sentence: A practical , customized video intervention may help improve patient self - efficacy , reduce problems with medication use , and improve medication adherence in diabetes patients .

Example answer:
{"entities": [{"text": "practical", "type": "IntellectualProduct"}, {"text": "video", "type": "IntellectualProduct"}, {"text": "improve", "type": "Finding"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "medication", "type": "HealthCareActivity"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: The clinical patient -simulated video method is more practical and clinical problem - based tutorials can be implemented if we create patient -simulated videos for each symptom as teaching materials .

Example answer:
{"entities": [{"text": "patient -simulated video", "type": "IntellectualProduct"}, {"text": "problem - based tutorials", "type": "IntellectualProduct"}, {"text": "patient -simulated videos", "type": "IntellectualProduct"}, {"text": "symptom", "type": "Finding"}]}

Example input:
Sentence: Video -based problem - based learning displayed significantly higher achievement rates for imagining authentic patients ( p = 0 . 001 ) , incorporating a comprehensive approach including psychosocial aspects ( p < 0 . 001 ) , and satisfaction with sessions ( p = 0 . 001 ) .

Example answer:
{"entities": [{"text": "Video", "type": "IntellectualProduct"}, {"text": "achievement rates", "type": "Finding"}]}

Input:
Sentence: Patient -simulated videos showing daily life facilitate imagining true patients and support a comprehensive approach that fosters better memory .

## Item MedMentions:test:3598
Example input:
Sentence: The United States had the highest rate of poor primary care coordination among the 11 high - income countries evaluated .

Example answer:
{"entities": [{"text": "United States", "type": "SpatialConcept"}, {"text": "high - income", "type": "PopulationGroup"}, {"text": "countries", "type": "SpatialConcept"}]}

Example input:
Sentence: Narrow networks were more prevalent among pediatric than adult specialists , because of both the sparseness of pediatric specialists and their exclusion from networks .

Example answer:
{"entities": [{"text": "pediatric", "type": "ProfessionalOrOccupationalGroup"}, {"text": "specialists", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Prevalence were calculated with confidence intervals of 95 % for each management area , stratified by sex and age groups , and differences between them were evaluated .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}]}

Example input:
Sentence: Additionally , commentary centered on diagnosis - related quality of care as affected by two emergent categories : ( 1 ) US health care providers ( n = 79 ; 63 commenters ) and ( 2 ) US health care reform - related policies , most commonly the Affordable Care Act ( ACA ) and insurance / reimbursement issues ( n = 62 ; 47 commenters ) .

Example answer:
{"entities": [{"text": "commentary", "type": "IntellectualProduct"}, {"text": "quality of care", "type": "HealthCareActivity"}, {"text": "categories", "type": "IntellectualProduct"}, {"text": "US", "type": "SpatialConcept"}, {"text": "health care providers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "commenters", "type": "ProfessionalOrOccupationalGroup"}, {"text": "health care reform - related policies", "type": "IntellectualProduct"}, {"text": "Affordable Care Act", "type": "IntellectualProduct"}, {"text": "ACA", "type": "IntellectualProduct"}]}

Example input:
Sentence: Proportions of narrow networks between pediatric and adult specialty providers were compared .

Example answer:
{"entities": [{"text": "pediatric", "type": "ProfessionalOrOccupationalGroup"}, {"text": "specialty providers", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Among the 1836 unique silver plan networks , the proportions of narrow networks were greater for pediatric ( 65 . 9 % ) than adult specialty ( 34 . 9 % ) networks ( P < .001 for all specialties ) .

Example answer:
{"entities": [{"text": "pediatric", "type": "ProfessionalOrOccupationalGroup"}, {"text": "specialty", "type": "ProfessionalOrOccupationalGroup"}, {"text": "specialties", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: A larger proportion of pediatric networks ( 43 . 8 % ) had no available specialists in the underlying area when compared with adult networks ( 10 . 4 % ) ( P < .001 for all specialties ) .

Example answer:
{"entities": [{"text": "pediatric", "type": "ProfessionalOrOccupationalGroup"}, {"text": "specialists", "type": "ProfessionalOrOccupationalGroup"}, {"text": "underlying area", "type": "SpatialConcept"}, {"text": "specialties", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: A sensor network was then developed to automatically capture these states using only three sensors , a local wireless network , and a data capture computer .

Example answer:
{"entities": [{"text": "local", "type": "SpatialConcept"}, {"text": "data capture", "type": "ResearchActivity"}]}

Example input:
Sentence: Understanding narrow networks and marketplace network adequacy standards is a necessary beginning to monitor access to care for children and families .

Example answer:
{"entities": [{"text": "care", "type": "HealthCareActivity"}]}

Example input:
Sentence: Narrow networks included none available networks ( ie , no providers available in the underlying area ) and limited networks ( ie , included < 10 % of the available providers in the underlying area ) .

Example answer:
{"entities": [{"text": "providers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "underlying area", "type": "SpatialConcept"}]}

Input:
Sentence: Networks were quantified as the fraction of providers in the underlying rating area within a state that participated in the network .

## Item MedMentions:test:3662
Example input:
Sentence: We developed a 12 - lead smartphone -based electrocardiogram ( ECG ) acquisition and monitoring system ( called " cvrPhone " ) , and an application to assess underlying ischemia , and estimate the respiration rate ( RR ) and tidal volume ( TV ) from analysis of electrocardiographic ( ECG ) signals only .

Example answer:
{"entities": [{"text": "electrocardiogram", "type": "Finding"}, {"text": "ECG", "type": "Finding"}, {"text": "ischemia", "type": "BiologicFunction"}, {"text": "respiration rate", "type": "ClinicalAttribute"}, {"text": "RR", "type": "ClinicalAttribute"}, {"text": "tidal volume", "type": "Finding"}, {"text": "TV", "type": "Finding"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "electrocardiographic ( ECG ) signals", "type": "Finding"}]}

Example input:
Sentence: A multidisciplinary approach , particularly close involvement of the advanced heart failure , mechanical heart and pancreas surgery teams was key to the success of this case .

Example answer:
{"entities": [{"text": "heart failure", "type": "BiologicFunction"}, {"text": "mechanical heart", "type": "MedicalDevice"}, {"text": "pancreas surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Heart beat characterization from ballistocardiogram signals using extended functions of multiple instances A multiple instance learning ( MIL ) method , extended Function of Multiple Instances ( eFUMI ) , is applied to ballistocardiogram ( BCG ) signals produced by a hydraulic bed sensor .

Example answer:
{"entities": [{"text": "Heart beat", "type": "BiologicFunction"}, {"text": "ballistocardiogram signals", "type": "HealthCareActivity"}, {"text": "extended functions of multiple instances", "type": "IntellectualProduct"}, {"text": "multiple instance learning ( MIL ) method ,", "type": "IntellectualProduct"}, {"text": "extended Function of Multiple Instances", "type": "IntellectualProduct"}, {"text": "eFUMI", "type": "IntellectualProduct"}, {"text": "ballistocardiogram", "type": "HealthCareActivity"}, {"text": "BCG", "type": "HealthCareActivity"}]}

Example input:
Sentence: To pursue these goals , a group of 23 schizophrenia patients and a group of 23 healthy controls performed a heartbeat perception task .

Example answer:
{"entities": [{"text": "group", "type": "PopulationGroup"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "heartbeat", "type": "BiologicFunction"}, {"text": "perception", "type": "BiologicFunction"}]}

Example input:
Sentence: This study was designed to evaluate the feasibility of MyHEART , a telephone - based health coach self - management intervention for young adults .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "MyHEART", "type": "IntellectualProduct"}, {"text": "telephone - based health coach self - management intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: Experimental results show that the estimated heartbeat concept found by eFUMI is more representative and a more discriminative prototype of the heartbeat signals than those found by comparison MIL methods in the literature .

Example answer:
{"entities": [{"text": "Experimental results", "type": "Finding"}, {"text": "heartbeat", "type": "BiologicFunction"}, {"text": "eFUMI", "type": "IntellectualProduct"}, {"text": "prototype", "type": "IntellectualProduct"}, {"text": "MIL methods", "type": "IntellectualProduct"}]}

Example input:
Sentence: The eFUMI method models the problem of learning a heartbeat concept from a BCG signal as a MIL problem .

Example answer:
{"entities": [{"text": "eFUMI method", "type": "IntellectualProduct"}, {"text": "models", "type": "IntellectualProduct"}, {"text": "problem", "type": "Finding"}, {"text": "heartbeat", "type": "BiologicFunction"}, {"text": "BCG signal", "type": "HealthCareActivity"}, {"text": "MIL", "type": "IntellectualProduct"}]}

Example input:
Sentence: After learning the heartbeat concept , heartbeat detection and heart rate estimation can be applied to test data .

Example answer:
{"entities": [{"text": "heartbeat", "type": "BiologicFunction"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "heart rate", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Then , using these bags , eFUMI learns a personalized concept of heartbeat for a subject as well as several non - heartbeat background concepts .

Example answer:
{"entities": [{"text": "eFUMI", "type": "IntellectualProduct"}, {"text": "heartbeat", "type": "BiologicFunction"}]}

Example input:
Sentence: This heartbeat concept is a prototype ( or " signature " ) that characterizes the heartbeat pattern for an individual in ballistocardiogram data .

Example answer:
{"entities": [{"text": "heartbeat", "type": "BiologicFunction"}, {"text": "prototype", "type": "IntellectualProduct"}, {"text": "individual", "type": "PopulationGroup"}, {"text": "ballistocardiogram", "type": "HealthCareActivity"}]}

Input:
Sentence: The goal of this approach is to learn a personalized heartbeat " concept " for an individual .

## Item MedMentions:test:3457
Example input:
Sentence: Finally , the best resulting protein models were applied prospectively in a large virtual screening campaign , in which two new active compounds were identified that were chemically distinct from those described in the literature .

Example answer:
{"entities": [{"text": "compounds", "type": "Chemical"}, {"text": "literature", "type": "IntellectualProduct"}]}

Example input:
Sentence: We used simulated body fluid to evaluate their bioactivity and human osteoblasts ( bone - forming cells ) to evaluate cytocompatibility .

Example answer:
{"entities": [{"text": "simulated", "type": "ResearchActivity"}, {"text": "body fluid", "type": "BodySubstance"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "osteoblasts", "type": "AnatomicalStructure"}, {"text": "bone - forming cells", "type": "AnatomicalStructure"}, {"text": "cytocompatibility", "type": "Finding"}]}

Example input:
Sentence: The study showed that modelled NH3 concentrations provide more accurate estimations of true exposure than distances - based surrogates , and that distance - based surrogates ( especially those based on distance to the closest point source ) are imprecise methods to identify exposed populations , although they may be useful for initial studies .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "NH3", "type": "Chemical"}, {"text": "exposure", "type": "InjuryOrPoisoning"}, {"text": "source", "type": "Finding"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: We first use the model to explore the uptake and release kinetics of the small molecule inhibitor by cartilage tissue .

Example answer:
{"entities": [{"text": "small molecule", "type": "Chemical"}, {"text": "inhibitor", "type": "Chemical"}, {"text": "cartilage tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In addition , toxicity studies in vitro and in vivo verify that Gd : CuS @ BSA NPs qualify as biocompatible agents .

Example answer:
{"entities": [{"text": "toxicity studies", "type": "HealthCareActivity"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "BSA", "type": "Chemical"}]}

Example input:
Sentence: Based on the QSPR model reported herein , we concluded that the lowest energy PXDD @ C60 complexes are those that the World Health Organization ( WHO ) considers to be less dangerous with respect to the aryl hydrocarbon receptor ( AhR ) toxicity mechanism .

Example answer:
{"entities": [{"text": "model", "type": "IntellectualProduct"}, {"text": "reported", "type": "IntellectualProduct"}, {"text": "PXDD", "type": "Chemical"}, {"text": "C60", "type": "Chemical"}, {"text": "complexes", "type": "Chemical"}, {"text": "World Health Organization", "type": "Organization"}, {"text": "WHO", "type": "Organization"}, {"text": "aryl hydrocarbon receptor", "type": "Chemical"}, {"text": "AhR", "type": "Chemical"}]}

Example input:
Sentence: Speciation modeling that includes formation constants for U ternary complexes reveals that the aqueous concentration of dicarbonato U species ( UO2 ( CO3 ) 2 ( - 2 ) ) best predicts U bioavailability to L .

Example answer:
{"entities": [{"text": "Speciation modeling", "type": "ResearchActivity"}, {"text": "U", "type": "Chemical"}, {"text": "dicarbonato U", "type": "Chemical"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "L .", "type": "Eukaryote"}]}

Example input:
Sentence: In this study , we performed molecular modeling on these compounds to determine their stereo - electronic properties required for optimal antiviral activity .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "molecular modeling", "type": "ResearchActivity"}, {"text": "compounds", "type": "Chemical"}, {"text": "antiviral activity", "type": "Finding"}]}

Example input:
Sentence: CNM did not pass all parameters of Lipinski 's rule of five , with a predicted low oral bioavailability and high plasma protein binding , but with good predicted blood brain barrier penetration .

Example answer:
{"entities": [{"text": "CNM", "type": "Chemical"}, {"text": "parameters", "type": "IntellectualProduct"}, {"text": "Lipinski 's rule of five", "type": "IntellectualProduct"}, {"text": "oral", "type": "SpatialConcept"}, {"text": "plasma protein binding", "type": "BiologicFunction"}]}

Example input:
Sentence: Our model will be useful to understand ligand - binding regulation of biological processes , such as the metabolism of nucleic acid .

Example answer:
{"entities": [{"text": "model", "type": "IntellectualProduct"}, {"text": "ligand - binding regulation", "type": "BiologicFunction"}, {"text": "biological processes", "type": "BiologicFunction"}, {"text": "metabolism", "type": "BiologicFunction"}, {"text": "nucleic acid", "type": "Chemical"}]}

Input:
Sentence: Molecular modeling assays predicted low toxicity risk and good oral bioavailability of the substances in humans .

## Item MedMentions:test:3833
Example input:
Sentence: 05 for both groups .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: 05 vs .

Example answer:
{"entities": []}

Example input:
Sentence: 05 vs .

Example answer:
{"entities": []}

Example input:
Sentence: 05 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 ( .

Example answer:
{"entities": []}

Input:
Sentence: 05 ) .

## Item MedMentions:test:3651
Example input:
Sentence: Frequent severe adverse events ( > 4 % difference from placebo ) were diarrhoea ( eight [ 11 % ] of 70 in the masitinib group vs one [ 2 % ] of 63 in the placebo group ) , rash ( four [ 6 % ] vs none ) , and asthenia ( four [ 6 % ] vs one [ 2 % ] ) .

Example answer:
{"entities": [{"text": "severe adverse events", "type": "Finding"}, {"text": "placebo", "type": "Chemical"}, {"text": "diarrhoea", "type": "Finding"}, {"text": "masitinib", "type": "Chemical"}, {"text": "asthenia", "type": "Finding"}]}

Example input:
Sentence: Randomized Crossover Trial of Amoxapine Versus Vitamin B12 for Retrograde Ejaculation To compare the efficacy and safety of amoxapine and vitamin B12 for treating retrograde ejaculation ( RE ) .

Example answer:
{"entities": [{"text": "Randomized", "type": "ResearchActivity"}, {"text": "Crossover Trial", "type": "ResearchActivity"}, {"text": "Amoxapine", "type": "Chemical"}, {"text": "Vitamin B12", "type": "Chemical"}, {"text": "Retrograde Ejaculation", "type": "BiologicFunction"}, {"text": "amoxapine", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}, {"text": "treating", "type": "HealthCareActivity"}, {"text": "retrograde ejaculation", "type": "BiologicFunction"}, {"text": "RE", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients were centrally randomised ( 1 : 1 ) to receive either oral masitinib ( 6 mg / kg per day over 24 weeks with possible extension ) or matched placebo with minimisation according to severe symptoms .

Example answer:
{"entities": [{"text": "randomised", "type": "ResearchActivity"}, {"text": "masitinib", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}, {"text": "severe symptoms", "type": "Finding"}]}

Example input:
Sentence: Narcolepsy Following Yellow Fever Vaccination : A Case Report Narcolepsy with cataplexy is a rare , but important differential diagnosis for daytime sleepiness and atonic paroxysms in an adolescent .

Example answer:
{"entities": [{"text": "Narcolepsy", "type": "BiologicFunction"}, {"text": "Yellow Fever Vaccination", "type": "HealthCareActivity"}, {"text": "Case Report", "type": "IntellectualProduct"}, {"text": "cataplexy", "type": "BiologicFunction"}, {"text": "differential diagnosis", "type": "HealthCareActivity"}, {"text": "daytime sleepiness", "type": "Finding"}, {"text": "atonic", "type": "Finding"}]}

Example input:
Sentence: Thirty - day all - cause readmission occurred in 17 % and 19 % of matched patients receiving and not receiving spironolactone , respectively ( hazard ratio [ HR ] , 0 .

Example answer:
{"entities": [{"text": "readmission", "type": "HealthCareActivity"}, {"text": "spironolactone", "type": "Chemical"}]}

Example input:
Sentence: Success rate was higher for amoxapine than for vitamin B12 ( 80 % , 20 / 25 vs 16 % , 4 / 25 ; P < 0 . 0001 ) .

Example answer:
{"entities": [{"text": "amoxapine", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}]}

Example input:
Sentence: Sixteen patients ( 20 % ) had low PSAP and 65 ( 80 % ) showed high PSAP .

Example answer:
{"entities": [{"text": "PSAP", "type": "HealthCareActivity"}]}

Example input:
Sentence: The percentage of patients who shifted from SD at baseline to normal sexual functioning at EOT was higher in males ( placebo , 40 . 6 % ; vilazodone , 35 . 7 % ) than in females ( placebo , 24 . 9 % ; vilazodone , 34 . 9 % ) ; no statistical testing was performed .

Example answer:
{"entities": [{"text": "SD", "type": "BiologicFunction"}, {"text": "sexual functioning", "type": "BiologicFunction"}, {"text": "males", "type": "PopulationGroup"}, {"text": "placebo", "type": "Chemical"}, {"text": "vilazodone", "type": "Chemical"}, {"text": "females", "type": "PopulationGroup"}]}

Example input:
Sentence: 18 patients were responsive to amoxapine but not to vitamin B12 , 2 patients were responsive to vitamin B12 but not amoxapine , 2 patients were responsive to both drugs , and 3 patients had no response to either drug .

Example answer:
{"entities": [{"text": "amoxapine", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}, {"text": "drugs", "type": "HealthCareActivity"}, {"text": "no response", "type": "Finding"}, {"text": "drug", "type": "HealthCareActivity"}]}

Example input:
Sentence: One patient ( B12 - amoxapine group ) withdrew for personal reasons ( breakdown of marital relations ) ; all other patients completed the study .

Example answer:
{"entities": [{"text": "B12", "type": "Chemical"}, {"text": "amoxapine", "type": "Chemical"}]}

Input:
Sentence: One patient ( 4 % ) reported sleepiness and 2 ( 8 % ) reported constipation while receiving amoxapine .

## Item MedMentions:test:3478
Example input:
Sentence: Lateral cephalometric radiographs from 78 patients with impacted canines , 68 with dental agenesis and 17 with hyperdontia were collected .

Example answer:
{"entities": [{"text": "Lateral", "type": "SpatialConcept"}, {"text": "cephalometric", "type": "HealthCareActivity"}, {"text": "radiographs", "type": "HealthCareActivity"}, {"text": "impacted", "type": "AnatomicalStructure"}, {"text": "canines", "type": "Finding"}, {"text": "dental agenesis", "type": "AnatomicalStructure"}, {"text": "hyperdontia", "type": "Finding"}]}

Example input:
Sentence: All dogs were treated with parathyroidectomy ( n = 37 ) or percutaneous ultrasound - guided heat ablation ( n = 17 ) .

Example answer:
{"entities": [{"text": "dogs", "type": "Eukaryote"}, {"text": "parathyroidectomy", "type": "HealthCareActivity"}, {"text": "percutaneous", "type": "SpatialConcept"}, {"text": "ultrasound - guided heat ablation", "type": "HealthCareActivity"}]}

Example input:
Sentence: A 17 - year - old girl with Class I skeletal malocclusion ( end - to - end molar relationships , deviated midline and space deficiency for left maxillary canine ) was referred for orthodontic treatment .

Example answer:
{"entities": [{"text": "old girl", "type": "PopulationGroup"}, {"text": "skeletal malocclusion", "type": "AnatomicalStructure"}, {"text": "midline", "type": "SpatialConcept"}, {"text": "left maxillary canine", "type": "AnatomicalStructure"}, {"text": "orthodontic treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of the study was to find any association between canine impaction , hyperdontia or hypodontia and sellar dimensions or bridging .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "canine", "type": "Finding"}, {"text": "impaction", "type": "AnatomicalStructure"}, {"text": "hyperdontia", "type": "Finding"}, {"text": "hypodontia", "type": "AnatomicalStructure"}, {"text": "sellar", "type": "AnatomicalStructure"}, {"text": "bridging", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A total of 1 , 989 children aged 0 . 19 to 17 years were identified with dog bite s .

Example answer:
{"entities": [{"text": "dog bite s", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Eyelid injuries occurred in 227 ( 99 % ) of children , 47 ( 20 % ) sustained canalicular system injuries , 3 ( 1 . 3 % ) suffered corneal abrasions , and 2 patients sustained facial nerve injury resulting in lagophthalmos .

Example answer:
{"entities": [{"text": "Eyelid injuries", "type": "InjuryOrPoisoning"}, {"text": "canalicular system", "type": "BodySystem"}, {"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "suffered", "type": "BiologicFunction"}, {"text": "corneal abrasions", "type": "InjuryOrPoisoning"}, {"text": "facial", "type": "SpatialConcept"}, {"text": "nerve injury", "type": "InjuryOrPoisoning"}, {"text": "lagophthalmos", "type": "BiologicFunction"}]}

Example input:
Sentence: Dog bite s to the face occurred in most patients ( n = 1 , 414 [ 71 % ] ) .

Example answer:
{"entities": [{"text": "Dog bite s", "type": "InjuryOrPoisoning"}, {"text": "face", "type": "SpatialConcept"}]}

Example input:
Sentence: These injuries occur in about 1 in 6 dog bite s to the face and primarily involve the ocular adnexa .

Example answer:
{"entities": [{"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "dog bite s", "type": "InjuryOrPoisoning"}, {"text": "face", "type": "SpatialConcept"}, {"text": "ocular adnexa", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A retrospective review of all children younger than 18 years who sought medical attention after a dog bite to the face between January 1 , 2003 and May 22 , 2014 was performed at a large tertiary pediatric hospital .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "attention", "type": "BiologicFunction"}, {"text": "dog bite", "type": "InjuryOrPoisoning"}, {"text": "face", "type": "SpatialConcept"}, {"text": "pediatric hospital", "type": "Organization"}]}

Example input:
Sentence: Ophthalmic Manifestations of Facial Dog Bites in Children To characterize ophthalmic manifestations and periocular injuries of pediatric facial dog bites .

Example answer:
{"entities": [{"text": "Ophthalmic Manifestations", "type": "Finding"}, {"text": "Facial", "type": "SpatialConcept"}, {"text": "Dog Bites", "type": "InjuryOrPoisoning"}, {"text": "ophthalmic manifestations", "type": "Finding"}, {"text": "periocular injuries", "type": "InjuryOrPoisoning"}, {"text": "facial", "type": "SpatialConcept"}, {"text": "dog bites", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: The authors report the clinical features and management on the largest series of ophthalmic and periocular injuries associated with pediatric facial dog bite s .

## Item MedMentions:test:3711
Example input:
Sentence: Although we focus here on the detection of positive selection from multiple population data , the local score approach is general and can be applied to other genome scans for selection or other genomewide analyses such as GWAS .

Example answer:
{"entities": [{"text": "detection", "type": "Finding"}, {"text": "positive", "type": "Finding"}, {"text": "selection", "type": "BiologicFunction"}, {"text": "multiple population data", "type": "IntellectualProduct"}, {"text": "local score approach", "type": "ResearchActivity"}, {"text": "genomewide analyses", "type": "ResearchActivity"}, {"text": "GWAS", "type": "ResearchActivity"}]}

Example input:
Sentence: gypseum complex , while molecular procedures based on sequencing of certain DNA regions are the most reliable and applicable strategies for this purpose .

Example answer:
{"entities": [{"text": "gypseum complex", "type": "Eukaryote"}, {"text": "sequencing", "type": "HealthCareActivity"}, {"text": "DNA regions", "type": "SpatialConcept"}]}

Example input:
Sentence: In this paper , we present a new statistical algorithm , MACHETE ( Mismatched Alignment CHimEra Tracking Engine ) , which achieves highly sensitive and specific detection of gene fusions from RNA - Seq data , including the highest Positive Predictive Value ( PPV ) compared to the current state - of - the - art , as assessed in simulated data .

Example answer:
{"entities": [{"text": "statistical algorithm", "type": "IntellectualProduct"}, {"text": "MACHETE", "type": "IntellectualProduct"}, {"text": "Mismatched Alignment CHimEra Tracking Engine )", "type": "IntellectualProduct"}, {"text": "detection", "type": "Finding"}, {"text": "gene fusions", "type": "ResearchActivity"}, {"text": "RNA - Seq data", "type": "IntellectualProduct"}]}

Example input:
Sentence: In recent years , with the development of machine learning , computational methods have been broadly used to predict PPIs , and can achieve good prediction rate .

Example answer:
{"entities": [{"text": "computational methods", "type": "ResearchActivity"}, {"text": "PPIs", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , the new algorithm can speed up approximately 79 % of the implementation process as compared with the standard cross - correlation method on the same computing platform .

Example answer:
{"entities": [{"text": "algorithm", "type": "IntellectualProduct"}, {"text": "standard cross - correlation method", "type": "ResearchActivity"}]}

Example input:
Sentence: One way ANOVA and Tukey 's multiple post hoc procedures were used . Pearson 's correlation coefficient was used for correlation .

Example answer:
{"entities": []}

Example input:
Sentence: Our method derives partial correlation based on the precision matrix estimated via Constrained L1 - minimization Approach ( CLIME ) , which is a recently developed statistical method that is more efficient and demonstrates better performance than the existing methods .

Example answer:
{"entities": [{"text": "method", "type": "IntellectualProduct"}, {"text": "Constrained L1 - minimization Approach", "type": "ResearchActivity"}, {"text": "CLIME", "type": "ResearchActivity"}, {"text": "statistical method", "type": "ResearchActivity"}, {"text": "methods", "type": "IntellectualProduct"}]}

Example input:
Sentence: We have developed novel computational and statistical methodology to permit comparative and confirmatory analyses across multiple and disparate data sources .

Example answer:
{"entities": [{"text": "computational", "type": "IntellectualProduct"}, {"text": "statistical methodology", "type": "IntellectualProduct"}]}

Example input:
Sentence: Sanger sequencing was previously the classic approach for quasispecies analysis , but this method was also time - consuming and laborious .

Example answer:
{"entities": [{"text": "Sanger sequencing", "type": "ResearchActivity"}, {"text": "quasispecies", "type": "Virus"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "method", "type": "IntellectualProduct"}]}

Example input:
Sentence: We show in theory and numerical studies that the proposed method is more efficient compared with existing approaches , especially when covariates are time varying .

Example answer:
{"entities": [{"text": "numerical studies", "type": "ResearchActivity"}]}

Input:
Sentence: The proposed approach is computationally efficient and requires only summary - level statistics .

## Item MedMentions:test:3528
Example input:
Sentence: The result is a rather rich dataset of frequencies at which responses can be found .

Example answer:
{"entities": [{"text": "result", "type": "Finding"}, {"text": "dataset", "type": "IntellectualProduct"}]}

Example input:
Sentence: To make the functionality accessible to biologists , and to facilitate reproducible analysis , we have also developed a web - based interface providing an expertly guided and customizable way of utilizing the methodology .

Example answer:
{"entities": [{"text": "biologists", "type": "ProfessionalOrOccupationalGroup"}, {"text": "reproducible analysis", "type": "ResearchActivity"}, {"text": "web - based interface", "type": "IntellectualProduct"}, {"text": "expertly guided", "type": "ProfessionalOrOccupationalGroup"}, {"text": "methodology", "type": "IntellectualProduct"}]}

Example input:
Sentence: The complexity of the human brain , including normal functioning and potential for dysfunctions , has developed over evolutionary time and has been shaped by natural selection .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "dysfunctions", "type": "BiologicFunction"}]}

Example input:
Sentence: BEST returns , as a result , a list of 10 different types of biomedical entities including genes , diseases , drugs , targets , transcription factors , miRNAs , and mutations that are relevant to a user 's query .

Example answer:
{"entities": [{"text": "BEST", "type": "IntellectualProduct"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "drugs", "type": "Chemical"}, {"text": "targets", "type": "MedicalDevice"}, {"text": "transcription factors", "type": "Chemical"}, {"text": "miRNAs", "type": "Chemical"}, {"text": "mutations", "type": "BiologicFunction"}, {"text": "query", "type": "IntellectualProduct"}]}

Example input:
Sentence: As proof of principle that MACHETE discovers novel gene fusions with high accuracy in vivo , we mined public data to discover and subsequently PCR validate novel gene fusions missed by other algorithms in the ovarian cancer cell line OVCAR3 .

Example answer:
{"entities": [{"text": "MACHETE", "type": "IntellectualProduct"}, {"text": "gene fusions", "type": "ResearchActivity"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "public", "type": "Organization"}, {"text": "PCR", "type": "ResearchActivity"}, {"text": "validate", "type": "ResearchActivity"}, {"text": "algorithms", "type": "IntellectualProduct"}, {"text": "ovarian cancer", "type": "BiologicFunction"}, {"text": "cell line", "type": "AnatomicalStructure"}, {"text": "OVCAR3", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Our results also indicate a potential neuroprosthetic approach to communicate with the brain at a very high resolution and provide a potential novel solution for evaluating the degree or state of neurological disease in animal models .

Example answer:
{"entities": [{"text": "neuroprosthetic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "communicate", "type": "BiologicFunction"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "evaluating", "type": "HealthCareActivity"}, {"text": "neurological disease", "type": "BiologicFunction"}, {"text": "animal models", "type": "Eukaryote"}]}

Example input:
Sentence: Our optimized techniques provide specimens for genetic , epigenetic and gene expression studies from a single small sample which can be used to develop diagnostics and treatments using a systems biology approach in the prenatal period .

Example answer:
{"entities": [{"text": "genetic", "type": "ResearchActivity"}, {"text": "epigenetic", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "diagnostics", "type": "HealthCareActivity"}, {"text": "treatments", "type": "HealthCareActivity"}, {"text": "systems biology", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: These results provide synthesis of existing data to support the potential translation of findings from mouse to primate species .

Example answer:
{"entities": [{"text": "translation", "type": "ResearchActivity"}, {"text": "findings", "type": "Finding"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "primate species", "type": "Eukaryote"}]}

Example input:
Sentence: Expectations for the methodology and translation of animal research : a survey of the general public , medical students and animal researchers in North America To determine what are considered acceptable standards for animal research ( AR ) methodology and translation rate to humans , a validated survey was sent to : a ) a sample of the general public , via Sampling Survey International ( SSI ; Canada ) , Amazon Mechanical Turk ( AMT ; USA ) , a Canadian city festival ( CF ) and a Canadian children 's hospital ( CH ) ; b ) a sample of medical students ( two first - year classes ) ; and c ) a sample of scientists ( corresponding authors and academic paediatricians ) .

Example answer:
{"entities": [{"text": "translation", "type": "ResearchActivity"}, {"text": "animal research", "type": "ResearchActivity"}, {"text": "survey", "type": "IntellectualProduct"}, {"text": "general public", "type": "PopulationGroup"}, {"text": "medical students", "type": "ProfessionalOrOccupationalGroup"}, {"text": "animal", "type": "Eukaryote"}, {"text": "researchers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "North America", "type": "SpatialConcept"}, {"text": "standards", "type": "IntellectualProduct"}, {"text": "AR", "type": "ResearchActivity"}, {"text": "humans", "type": "Eukaryote"}, {"text": "Sampling Survey International", "type": "IntellectualProduct"}, {"text": "SSI", "type": "IntellectualProduct"}, {"text": "Canada", "type": "SpatialConcept"}, {"text": "Amazon Mechanical Turk", "type": "IntellectualProduct"}, {"text": "AMT", "type": "IntellectualProduct"}, {"text": "USA", "type": "SpatialConcept"}, {"text": "Canadian city", "type": "SpatialConcept"}, {"text": "Canadian", "type": "SpatialConcept"}, {"text": "children 's hospital", "type": "Organization"}, {"text": "CH", "type": "Organization"}, {"text": "scientists", "type": "ProfessionalOrOccupationalGroup"}, {"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "academic", "type": "Organization"}, {"text": "paediatricians", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: The collected data were described and the sequenced glycoprotein ( G ) and nucleoprotein ( N ) genes were implemented to estimate the evolutionary rates and phylogeographic patterns using BEAST v .

Example answer:
{"entities": [{"text": "collected data", "type": "Finding"}, {"text": "sequenced glycoprotein", "type": "AnatomicalStructure"}, {"text": "G", "type": "AnatomicalStructure"}, {"text": "nucleoprotein", "type": "AnatomicalStructure"}, {"text": "( N ) genes", "type": "AnatomicalStructure"}, {"text": "patterns", "type": "SpatialConcept"}]}

Input:
Sentence: Our results provide a resource for studying animal evolution , morphological complexity , breeding , and biomedical research .

## Item MedMentions:test:3508
Example input:
Sentence: Of the patients with 1 or no dose - reduction criteria assigned to receive the 5 mg twice daily dose of apixaban or warfarin , 3966 had 1 dose - reduction criterion ; these patients had higher rates of stroke or systemic embolism ( HR , 1 . 47 ; 95 % CI , 1 . 20 - 1 . 81 ) and major bleeding ( HR , 1 . 89 ; 95 % CI , 1 . 62 - 2 . 20 ) compared with those with no dose - reduction criteria ( n = 13 356 ) .

Example answer:
{"entities": [{"text": "apixaban", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "bleeding", "type": "BiologicFunction"}]}

Example input:
Sentence: Multicenter Trial of Rivaroxaban for Early Discharge of Pulmonary Embolism From the Emergency Department ( MERCURY PE ) : Rationale and Design Traditionally , patients with pulmonary embolism ( PE ) are admitted from the emergency department and treated with low - molecular - weight heparin followed by warfarin .

Example answer:
{"entities": [{"text": "Multicenter Trial", "type": "ResearchActivity"}, {"text": "Rivaroxaban", "type": "Chemical"}, {"text": "Pulmonary Embolism", "type": "BiologicFunction"}, {"text": "Emergency Department", "type": "Organization"}, {"text": "MERCURY PE", "type": "Organization"}, {"text": "pulmonary embolism", "type": "BiologicFunction"}, {"text": "PE", "type": "BiologicFunction"}, {"text": "emergency department", "type": "Organization"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "low - molecular - weight heparin", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}]}

Example input:
Sentence: Patients with atrial fibrillation and isolated advanced age , low body weight , or renal dysfunction have a higher risk of stroke or systemic embolism and major bleeding but show consistent benefits with the 5 mg twice daily dose of apixaban vs warfarin compared with patients without these characteristics .

Example answer:
{"entities": [{"text": "atrial fibrillation", "type": "BiologicFunction"}, {"text": "renal dysfunction", "type": "Finding"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "bleeding", "type": "BiologicFunction"}, {"text": "apixaban", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}]}

Example input:
Sentence: Within 48 h of initiation of warfarin therapy , the tetraparesis and hyperesthesia were markedly improved .

Example answer:
{"entities": [{"text": "warfarin therapy", "type": "HealthCareActivity"}, {"text": "tetraparesis", "type": "Finding"}, {"text": "hyperesthesia", "type": "Finding"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: Warfarin treatment was associated with higher risk of bleeding in all eGFR groups and lower risk of stroke in patients with eGFR ≥15 mL / min per 1 .

Example answer:
{"entities": [{"text": "bleeding", "type": "BiologicFunction"}, {"text": "eGFR", "type": "HealthCareActivity"}, {"text": "stroke", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study , we report regarding the preoperative preparation and severe , persistent hypertension attack management with a combination of α - adrenergic blockade , β - adrenergic blockade , sodium nitroprusside and remifentanil in a patient who underwent laparoscopic surgery for phaeochromocytoma .

Example answer:
{"entities": [{"text": "preoperative preparation", "type": "HealthCareActivity"}, {"text": "α - adrenergic blockade", "type": "Chemical"}, {"text": "β - adrenergic blockade", "type": "Chemical"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "remifentanil", "type": "Chemical"}, {"text": "laparoscopic surgery", "type": "HealthCareActivity"}, {"text": "phaeochromocytoma", "type": "BiologicFunction"}]}

Example input:
Sentence: Atorvastatin -induced dermatomyositis A 49 - year - old man with no previous history of musculoskeletal or cutaneous problems who had a myocardial infarction ( MI ) was treated with atorvastatin , prasugrel , enoxaparine , and diltiazem following percutaneous coronary intervention .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "Chemical"}, {"text": "dermatomyositis", "type": "BiologicFunction"}, {"text": "musculoskeletal", "type": "Finding"}, {"text": "cutaneous problems", "type": "Finding"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "MI", "type": "BiologicFunction"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "atorvastatin", "type": "Chemical"}, {"text": "prasugrel", "type": "Chemical"}, {"text": "enoxaparine", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "percutaneous coronary intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: A total of 7 trials ( 958 patients ) explored the use of increased dosing of enoxaparin for VTE prophylaxis in trauma patients .

Example answer:
{"entities": [{"text": "trials", "type": "ResearchActivity"}, {"text": "enoxaparin", "type": "Chemical"}, {"text": "VTE prophylaxis", "type": "HealthCareActivity"}, {"text": "trauma", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Various treatment options such as low - intensity warfarin and aspirin plus clopidogrel have been suggested but are inferior to dose - adjusted warfarin .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "inferior", "type": "SpatialConcept"}]}

Example input:
Sentence: Additionally , warfarin in combination with clopidogrel and enoxaparin appeared to be a safe and effective treatment for the suspected thrombi reported in this case .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "clopidogrel", "type": "Chemical"}, {"text": "enoxaparin", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "thrombi", "type": "BiologicFunction"}, {"text": "reported", "type": "HealthCareActivity"}]}

Input:
Sentence: The patient was treated with a combination of warfarin , clopidogrel , and enoxaparin as well as analgesics .

## Item MedMentions:test:3713
Example input:
Sentence: The level of significance was set at 0 . 001 .

Example answer:
{"entities": [{"text": "level of significance", "type": "ResearchActivity"}]}

Example input:
Sentence: Univariate and multivariate analysis was performed with a priori significance at p ≤ 0 .

Example answer:
{"entities": []}

Example input:
Sentence: Experts measure hyperemia using levels in a grading scale , a procedure that is subjective , non - repeatable and time consuming , thus creating a need for its automatisation .

Example answer:
{"entities": [{"text": "hyperemia", "type": "BiologicFunction"}, {"text": "grading scale", "type": "IntellectualProduct"}]}

Example input:
Sentence: The data were grouped into PHI themes , which were then prioritized on the basis of degree of interdependency .

Example answer:
{"entities": [{"text": "PHI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Thresholds were the most effective outcome measure to both track progression and to distinguish between MAV and Ménière 's patients .

Example answer:
{"entities": [{"text": "MAV", "type": "Finding"}, {"text": "Ménière 's", "type": "BiologicFunction"}]}

Example input:
Sentence: Following three rounds of ranking and prioritizing , five priorities were agreed at Divisional level , and from these , the five top organizational priorities were selected .

Example answer:
{"entities": [{"text": "ranking", "type": "IntellectualProduct"}, {"text": "priorities", "type": "ResearchActivity"}, {"text": "Divisional level", "type": "Organization"}, {"text": "organizational priorities", "type": "ResearchActivity"}]}

Example input:
Sentence: In Round 2 , nurses from the clinical areas ranked topics of importance resulting in a set of four to five priorities .

Example answer:
{"entities": [{"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "ranked", "type": "IntellectualProduct"}, {"text": "priorities", "type": "ResearchActivity"}]}

Example input:
Sentence: Items rated very or extremely important by 80 % or more of the experts were reviewed in the final group round to build the final set .

Example answer:
{"entities": [{"text": "experts", "type": "ProfessionalOrOccupationalGroup"}, {"text": "set", "type": "IntellectualProduct"}]}

Example input:
Sentence: In considering value , it is necessary to assess the quality of the evidence as well as to define levels of value .

Example answer:
{"entities": []}

Example input:
Sentence: The level of significance was set at p = 0 .

Example answer:
{"entities": []}

Input:
Sentence: An importance scale was used to determine a priority multi - level indicator set .

## Item MedMentions:test:3456
Example input:
Sentence: In this context , mental health care professionals ( MHPs ) are increasingly required to work on interdisciplinary teams in a variety of settings .

Example answer:
{"entities": [{"text": "mental health care professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "MHPs", "type": "ProfessionalOrOccupationalGroup"}, {"text": "interdisciplinary teams", "type": "HealthCareActivity"}]}

Example input:
Sentence: Reporting of poor facility hygiene , difficulty getting an appointment , poor physician behaviour and high costs of health care all declined ( P < 0 . 001 ) in PHC settings , but remained higher among urban , low - income and working - age populations .

Example answer:
{"entities": [{"text": "Reporting", "type": "HealthCareActivity"}, {"text": "physician", "type": "ProfessionalOrOccupationalGroup"}, {"text": "PHC", "type": "HealthCareActivity"}, {"text": "settings", "type": "SpatialConcept"}, {"text": "low - income", "type": "Finding"}, {"text": "populations", "type": "PopulationGroup"}]}

Example input:
Sentence: A collaborative research team from three Canadian nursing programs completed a mixed method survey to describe how nursing students used mobile nursing information support and the extent of this support for learning .

Example answer:
{"entities": [{"text": "nursing programs", "type": "ResearchActivity"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "survey", "type": "IntellectualProduct"}, {"text": "nursing students", "type": "ProfessionalOrOccupationalGroup"}, {"text": "nursing information support", "type": "IntellectualProduct"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "learning", "type": "BiologicFunction"}]}

Example input:
Sentence: Little is known , however , about the profiles of MHPs in relation to their perceived work role performance .

Example answer:
{"entities": [{"text": "MHPs", "type": "ProfessionalOrOccupationalGroup"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "work role performance", "type": "Finding"}]}

Example input:
Sentence: Data from the 9306 participants were categorized by 5 regions : Asia ( n = 552 ) ; Europe ( n = 4909 ) ; Latin America ( n = 1406 ) ; North America ( n = 2146 ) ; and Australia , New Zealand , and South Africa ( n = 293 ) .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "regions", "type": "SpatialConcept"}, {"text": "Asia", "type": "SpatialConcept"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "Latin America", "type": "SpatialConcept"}, {"text": "North America", "type": "SpatialConcept"}, {"text": "Australia", "type": "SpatialConcept"}, {"text": "New Zealand", "type": "SpatialConcept"}, {"text": "South Africa", "type": "SpatialConcept"}]}

Example input:
Sentence: In the context of a five - wave longitudinal research design , participants included 928 mother - child dyads in Belfast ( 453 boys , 475 girls ) drawn from socially deprived , ethnically homogenous areas that had experienced political violence .

Example answer:
{"entities": [{"text": "five - wave longitudinal research design", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "Belfast", "type": "SpatialConcept"}, {"text": "ethnically", "type": "Finding"}, {"text": "homogenous", "type": "SpatialConcept"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "violence", "type": "BiologicFunction"}]}

Example input:
Sentence: Employing a hermeneutic -phenomenological approach , eight service users were interviewed about their expectations for treatment and their goals and hopes for recovery at the start of their contact with health professionals at a CMHC .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "goals", "type": "IntellectualProduct"}, {"text": "hopes", "type": "BiologicFunction"}, {"text": "recovery", "type": "BiologicFunction"}, {"text": "health professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "CMHC", "type": "Organization"}]}

Example input:
Sentence: We carried out a cross - sectional study among a convenience sample of caregivers employed at 11 LTCF in Japan using a vignette - based questionnaire .

Example answer:
{"entities": [{"text": "cross - sectional study", "type": "ResearchActivity"}, {"text": "convenience sample", "type": "ResearchActivity"}, {"text": "caregivers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "employed", "type": "Finding"}, {"text": "LTCF", "type": "Organization"}, {"text": "Japan", "type": "SpatialConcept"}, {"text": "vignette - based questionnaire", "type": "IntellectualProduct"}]}

Example input:
Sentence: Two other profiles were identified , positioned between the aforementioned groups in terms of the perceived performance of MHPs : the junior primary care MHPs and the diversified specialized care MHPs .

Example answer:
{"entities": [{"text": "perceived", "type": "BiologicFunction"}, {"text": "MHPs", "type": "ProfessionalOrOccupationalGroup"}, {"text": "junior primary care", "type": "HealthCareActivity"}, {"text": "diversified specialized care", "type": "HealthCareActivity"}]}

Example input:
Sentence: Questionnaires relating to drugs , orthotic devices , mobility aids , rehabilitation and medical input were sent to 435 members of a unique regional French network dedicated to adults with cerebral palsy .

Example answer:
{"entities": [{"text": "Questionnaires", "type": "IntellectualProduct"}, {"text": "drugs", "type": "Chemical"}, {"text": "orthotic devices", "type": "MedicalDevice"}, {"text": "mobility aids", "type": "MedicalDevice"}, {"text": "medical input", "type": "Finding"}, {"text": "members", "type": "PopulationGroup"}, {"text": "regional French", "type": "SpatialConcept"}, {"text": "cerebral palsy", "type": "BiologicFunction"}]}

Input:
Sentence: MHPs in Quebec ( N = 315 ) from four local service networks completed a self - administered questionnaire eliciting information on individual and team characteristics , as well as team processes and states .

## Item MedMentions:test:3650
Example input:
Sentence: Of the patients with 1 or no dose - reduction criteria assigned to receive the 5 mg twice daily dose of apixaban or warfarin , 3966 had 1 dose - reduction criterion ; these patients had higher rates of stroke or systemic embolism ( HR , 1 . 47 ; 95 % CI , 1 . 20 - 1 . 81 ) and major bleeding ( HR , 1 . 89 ; 95 % CI , 1 . 62 - 2 . 20 ) compared with those with no dose - reduction criteria ( n = 13 356 ) .

Example answer:
{"entities": [{"text": "apixaban", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "bleeding", "type": "BiologicFunction"}]}

Example input:
Sentence: De - escalation therapy was considered when the initial antibiotic therapy was narrowed to penicillin , amoxicillin or amoxicillin / clavulanate within the first 72 h after admission .

Example answer:
{"entities": [{"text": "De - escalation therapy", "type": "HealthCareActivity"}, {"text": "antibiotic therapy", "type": "HealthCareActivity"}, {"text": "penicillin", "type": "Chemical"}, {"text": "amoxicillin", "type": "Chemical"}, {"text": "amoxicillin / clavulanate", "type": "Chemical"}, {"text": "admission", "type": "HealthCareActivity"}]}

Example input:
Sentence: Disease progression was rapid under oxaliplatin , capecitabine , irinotecan , and bevacizumab .

Example answer:
{"entities": [{"text": "Disease progression", "type": "BiologicFunction"}, {"text": "oxaliplatin", "type": "Chemical"}, {"text": "capecitabine", "type": "Chemical"}, {"text": "irinotecan", "type": "Chemical"}, {"text": "bevacizumab", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , we found that an AMPA receptor antagonist , NBQX ( 10 mg / kg ) , completely reversed the antidepressant - like activity of a mixture of scopolamine and LY341495 in the TST .

Example answer:
{"entities": [{"text": "AMPA receptor", "type": "Chemical"}, {"text": "antagonist", "type": "Chemical"}, {"text": "NBQX", "type": "Chemical"}, {"text": "antidepressant - like activity", "type": "Finding"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "LY341495", "type": "Chemical"}, {"text": "TST", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , DBP and MBP showed significant increases in patients when prophylactic atropine was administrated .

Example answer:
{"entities": [{"text": "DBP", "type": "ClinicalAttribute"}, {"text": "MBP", "type": "Finding"}, {"text": "patients", "type": "Chemical"}, {"text": "prophylactic", "type": "HealthCareActivity"}, {"text": "atropine", "type": "Chemical"}, {"text": "administrated", "type": "HealthCareActivity"}]}

Example input:
Sentence: Chemotherapy regimens included gemcitabine alone or in association with other agents ( 44 % ) , oxaliplatin , irinotecan , fluorouracil and leucovorin ( FOLFIRINOX 8 % ) , and cisplatin , gemcitabine plus capecitabine and epirubicin ( PEXG ) or capecitabine and docetaxel ( PDXG ) or epirubicin and fluorouracil ( PEFG ) ( 48 % ) .

Example answer:
{"entities": [{"text": "Chemotherapy regimens", "type": "HealthCareActivity"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "agents", "type": "Chemical"}, {"text": "oxaliplatin", "type": "Chemical"}, {"text": "irinotecan", "type": "Chemical"}, {"text": "fluorouracil", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "capecitabine", "type": "Chemical"}, {"text": "epirubicin", "type": "Chemical"}, {"text": "PEXG", "type": "HealthCareActivity"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "PDXG", "type": "HealthCareActivity"}, {"text": "PEFG", "type": "HealthCareActivity"}]}

Example input:
Sentence: Randomized Crossover Trial of Amoxapine Versus Vitamin B12 for Retrograde Ejaculation To compare the efficacy and safety of amoxapine and vitamin B12 for treating retrograde ejaculation ( RE ) .

Example answer:
{"entities": [{"text": "Randomized", "type": "ResearchActivity"}, {"text": "Crossover Trial", "type": "ResearchActivity"}, {"text": "Amoxapine", "type": "Chemical"}, {"text": "Vitamin B12", "type": "Chemical"}, {"text": "Retrograde Ejaculation", "type": "BiologicFunction"}, {"text": "amoxapine", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}, {"text": "treating", "type": "HealthCareActivity"}, {"text": "retrograde ejaculation", "type": "BiologicFunction"}, {"text": "RE", "type": "BiologicFunction"}]}

Example input:
Sentence: Success rate was higher for amoxapine than for vitamin B12 ( 80 % , 20 / 25 vs 16 % , 4 / 25 ; P < 0 . 0001 ) .

Example answer:
{"entities": [{"text": "amoxapine", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}]}

Example input:
Sentence: One patient ( B12 - amoxapine group ) withdrew for personal reasons ( breakdown of marital relations ) ; all other patients completed the study .

Example answer:
{"entities": [{"text": "B12", "type": "Chemical"}, {"text": "amoxapine", "type": "Chemical"}]}

Example input:
Sentence: 18 patients were responsive to amoxapine but not to vitamin B12 , 2 patients were responsive to vitamin B12 but not amoxapine , 2 patients were responsive to both drugs , and 3 patients had no response to either drug .

Example answer:
{"entities": [{"text": "amoxapine", "type": "Chemical"}, {"text": "vitamin B12", "type": "Chemical"}, {"text": "drugs", "type": "HealthCareActivity"}, {"text": "no response", "type": "Finding"}, {"text": "drug", "type": "HealthCareActivity"}]}

Input:
Sentence: The B12 - amoxapine group received the opposite regimen .

## Item MedMentions:test:3782
Example input:
Sentence: We show in theory and numerical studies that the proposed method is more efficient compared with existing approaches , especially when covariates are time varying .

Example answer:
{"entities": [{"text": "numerical studies", "type": "ResearchActivity"}]}

Example input:
Sentence: The SFCR algorithm is composed of two consecutive steps corresponding to complementary reconstruction models , each with a structural feature based l1 norm constraint and a voxel fidelity based l2 norm constraint , which allows both the structure edges and tiny features to be recovered , whereas the noise and artifacts could be reduced .

Example answer:
{"entities": [{"text": "algorithm", "type": "IntellectualProduct"}, {"text": "reconstruction models", "type": "IntellectualProduct"}, {"text": "structural feature", "type": "SpatialConcept"}, {"text": "structure", "type": "SpatialConcept"}]}

Example input:
Sentence: We demonstrate that the scoring functions generated by our approach are similar to or even outperform state - of - the - art scoring functions for predicting near - native solutions .

Example answer:
{"entities": [{"text": "scoring functions", "type": "ResearchActivity"}]}

Example input:
Sentence: Of additional importance , we find that potentials specifically trained to identify the native bound complex perform rather poorly on identifying acceptable or medium quality ( near - native ) solutions .

Example answer:
{"entities": []}

Example input:
Sentence: Generalized additive models and state - space models showed that modelling based on data fusion from EC , pH , and NIR sensors produced better results than modelling without sensor data or data from just a single sensor .

Example answer:
{"entities": [{"text": "models", "type": "IntellectualProduct"}, {"text": "state - space models", "type": "IntellectualProduct"}, {"text": "modelling", "type": "ResearchActivity"}, {"text": "NIR", "type": "HealthCareActivity"}]}

Example input:
Sentence: Furthermore , the new algorithm can speed up approximately 79 % of the implementation process as compared with the standard cross - correlation method on the same computing platform .

Example answer:
{"entities": [{"text": "algorithm", "type": "IntellectualProduct"}, {"text": "standard cross - correlation method", "type": "ResearchActivity"}]}

Example input:
Sentence: The machine - learning methods investigated herein performed well in both the qualitative classification ( ∼70 % accuracy ) and quantitative IC50 predictions ( RMSE ∼ 1 log ) .

Example answer:
{"entities": [{"text": "methods", "type": "IntellectualProduct"}, {"text": "classification", "type": "IntellectualProduct"}]}

Example input:
Sentence: The SVC model ( C = 8 . 1728 and γ = 0 . 2333 ) optimized by the particle swarm optimization ( PSO ) algorithm possesses an accuracy of 88 . 15 % for the training set .

Example answer:
{"entities": [{"text": "particle swarm optimization ( PSO ) algorithm", "type": "IntellectualProduct"}]}

Example input:
Sentence: Optical simulations ( in terms of through - focus Strehl ratio from Hartmann - Shack aberrometry ) accurately predicted the pattern producing the highest perceived quality in 4 out of 5 patients , both for far and near vision .

Example answer:
{"entities": [{"text": "Optical simulations", "type": "Finding"}, {"text": "pattern", "type": "SpatialConcept"}, {"text": "vision", "type": "BiologicFunction"}]}

Example input:
Sentence: Simulation studies show that the Dens - based method demonstrates comparable or better performance with respect to the existing methods in network estimation .

Example answer:
{"entities": [{"text": "Simulation studies", "type": "ResearchActivity"}, {"text": "Dens - based method", "type": "ResearchActivity"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "network", "type": "BiologicFunction"}]}

Input:
Sentence: Experiments on simulated data sets show that our approximation algorithm is very competitive both in efficiency and in quality of the solutions .

## Item MedMentions:test:3246
Example input:
Sentence: Therefore the aim of the present study was to evaluate the tooth discoloration potential of a nano zinc oxide - eugenol ( NZOE ) sealer .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "tooth discoloration", "type": "Finding"}, {"text": "zinc oxide - eugenol", "type": "Chemical"}, {"text": "NZOE", "type": "Chemical"}, {"text": "sealer", "type": "Chemical"}]}

Example input:
Sentence: Skin texture , clarity , and mottled and discrete pigmentation were the most improved parameters by the end of the study ( 40 % to 52 % improvement from baseline ) , with 100 % of subjects showing improvement in skin clarity and texture .

Example answer:
{"entities": [{"text": "Skin texture", "type": "Finding"}, {"text": "clarity", "type": "Finding"}, {"text": "mottled", "type": "Finding"}, {"text": "parameters", "type": "Finding"}, {"text": "study", "type": "ResearchActivity"}, {"text": "subjects", "type": "PopulationGroup"}, {"text": "skin clarity", "type": "Finding"}, {"text": "texture", "type": "Finding"}]}

Example input:
Sentence: Influence of dentin thickness on intrapulpal temperature under simulated pulpal pressure during Nd : YAG laser irradiation The aim of this study was to evaluate the effects of dentin thickness and pulpal pressure simulation ( PPS ) on the variation of intrapulpal temperature ( ∆T ) when submitted to an adhesive technique using laser irradiation .

Example answer:
{"entities": [{"text": "dentin", "type": "BodySubstance"}, {"text": "intrapulpal", "type": "AnatomicalStructure"}, {"text": "study", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}]}

Example input:
Sentence: Tooth Discoloration Resulting from a Nano Zinc Oxide - Eugenol Sealer A desirable quality of any endodontic sealer is its ability to be tooth color friendly .

Example answer:
{"entities": [{"text": "Tooth Discoloration", "type": "Finding"}, {"text": "Zinc Oxide - Eugenol", "type": "Chemical"}, {"text": "Sealer", "type": "Chemical"}, {"text": "endodontic sealer", "type": "Chemical"}, {"text": "tooth color", "type": "Finding"}]}

Example input:
Sentence: 15 , 16 , and 17 were developmentally delayed and were displaying the characteristic " ghost appearance . " Comprehensive dental care was done under local anaesthesia and it included extraction of the primary molars affected by ROD , stainless steel crown on 64 , and caries prevention program .

Example answer:
{"entities": [{"text": "Comprehensive dental care", "type": "HealthCareActivity"}, {"text": "local anaesthesia", "type": "HealthCareActivity"}, {"text": "extraction", "type": "HealthCareActivity"}, {"text": "primary molars", "type": "Finding"}, {"text": "ROD", "type": "AnatomicalStructure"}, {"text": "stainless steel crown", "type": "MedicalDevice"}, {"text": "caries", "type": "BiologicFunction"}]}

Example input:
Sentence: Surface roughness of the samples was measured using the Surface Roughness Tester system ( TR 200 Time Group , Germany ) before and after bleaching .

Example answer:
{"entities": [{"text": "Surface roughness", "type": "Finding"}, {"text": "Surface Roughness Tester system", "type": "MedicalDevice"}, {"text": "TR 200 Time Group", "type": "Organization"}, {"text": "Germany", "type": "SpatialConcept"}, {"text": "bleaching", "type": "HealthCareActivity"}]}

Example input:
Sentence: Diode lasers increased the ARI scores and thus decreased the risk of enamel fracture .

Example answer:
{"entities": [{"text": "Diode lasers", "type": "MedicalDevice"}, {"text": "ARI scores", "type": "Finding"}, {"text": "enamel fracture", "type": "Finding"}]}

Example input:
Sentence: The highest surface roughness was seen in the conventional bleaching group and the lowest surface roughness was reported in group 3 ( laser white gel + diode laser ) , in which the average surface roughness increased by only 0 .

Example answer:
{"entities": [{"text": "surface roughness", "type": "Finding"}, {"text": "bleaching", "type": "HealthCareActivity"}, {"text": "laser white gel", "type": "Chemical"}, {"text": "diode laser", "type": "MedicalDevice"}]}

Example input:
Sentence: Results : The results showed that the mean surface roughness of the teeth before and after bleaching had a significant difference in all the study groups .

Example answer:
{"entities": [{"text": "surface roughness", "type": "Finding"}, {"text": "teeth", "type": "AnatomicalStructure"}, {"text": "bleaching", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of this study was to compare surface roughness of enamel in teeth bleached using Diode and Neodymium - Doped Yttrium Aluminium Garnet ( Nd : YAG ) lasers with those bleached using conventional method .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "surface roughness", "type": "Finding"}, {"text": "enamel", "type": "BodySubstance"}, {"text": "teeth bleached", "type": "HealthCareActivity"}, {"text": "Diode", "type": "MedicalDevice"}, {"text": "Neodymium - Doped Yttrium Aluminium Garnet ( Nd : YAG ) lasers", "type": "MedicalDevice"}, {"text": "bleached", "type": "HealthCareActivity"}]}

Input:
Sentence: A Comparative Study of Enamel Surface Roughness After Bleaching With Diode Laser and Nd : YAG Laser Introduction : Bleaching process can affect surface roughness of enamel , which is a vital factor in esthetic and resistance of tooth .

## Item MedMentions:test:3829
Example input:
Sentence: The final pathway resulting in supernumerary teeth seems to involve Wnt , a morphogen active during many stages of development .

Example answer:
{"entities": [{"text": "supernumerary teeth", "type": "Finding"}, {"text": "Wnt", "type": "Chemical"}, {"text": "morphogen", "type": "Chemical"}]}

Example input:
Sentence: A total of 20 teeth were debonded without lasing ( group 1 ) , 20 immediately after lasing ( group 2 ) , and 20 1 hour after lasing ( group 3 ) .

Example answer:
{"entities": [{"text": "teeth", "type": "AnatomicalStructure"}, {"text": "debonded", "type": "HealthCareActivity"}]}

Example input:
Sentence: The crown of 55 was broken down with only the root remaining below the gingival level .

Example answer:
{"entities": [{"text": "crown", "type": "AnatomicalStructure"}, {"text": "root", "type": "AnatomicalStructure"}, {"text": "gingival", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The teeth in the remaining five groups were prepared with MOD cavities and endodontically treated .

Example answer:
{"entities": [{"text": "teeth", "type": "AnatomicalStructure"}, {"text": "MOD cavities", "type": "BiologicFunction"}, {"text": "endodontically treated", "type": "HealthCareActivity"}]}

Example input:
Sentence: Difference between groups was statistically significant for age , number of teeth and frequency of dental checkups ( p < 0 .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}, {"text": "teeth", "type": "AnatomicalStructure"}, {"text": "dental checkups", "type": "HealthCareActivity"}]}

Example input:
Sentence: Group 3 specimens were subjected to pH cycling and artificial caries were created on the buccal , lingual and gingival walls .

Example answer:
{"entities": [{"text": "pH cycling", "type": "HealthCareActivity"}, {"text": "caries", "type": "BiologicFunction"}, {"text": "buccal", "type": "SpatialConcept"}, {"text": "lingual", "type": "SpatialConcept"}, {"text": "gingival walls", "type": "SpatialConcept"}]}

Example input:
Sentence: The teeth were sectioned , and the roots received endodontic treatment .

Example answer:
{"entities": [{"text": "teeth", "type": "AnatomicalStructure"}, {"text": "sectioned", "type": "HealthCareActivity"}, {"text": "roots", "type": "AnatomicalStructure"}, {"text": "endodontic treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: They were randomly divided into the I / S group ( Intact upper molar teeth / Solid diet feeding ) , the E / S group ( Extracted upper molar teeth / Solid diet feeding ) , the I / P group ( Intact upper molar teeth / Powder diet feeding ) , and the E / P group ( Extracted upper molar teeth / Powder diet feeding ) .

Example answer:
{"entities": [{"text": "randomly", "type": "ResearchActivity"}, {"text": "upper molar teeth", "type": "AnatomicalStructure"}, {"text": "Solid diet", "type": "Food"}, {"text": "Extracted", "type": "HealthCareActivity"}, {"text": "Powder diet", "type": "HealthCareActivity"}]}

Example input:
Sentence: Seventy - two sound maxillary premolar teeth were randomly divided into six groups ( n = 12 ) .

Example answer:
{"entities": [{"text": "maxillary", "type": "AnatomicalStructure"}, {"text": "premolar teeth", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The teeth in the first group were left intact and tested as unprepared negative control ( group I ) specimens .

Example answer:
{"entities": [{"text": "teeth", "type": "AnatomicalStructure"}]}

Input:
Sentence: The teeth were divided into 3 groups .

## Item MedMentions:test:3617
Example input:
Sentence: Genotypes in all the analyzed polymorphisms preserved the Hardy - Weinberg equilibrium in pregnant women , both infected and uninfected with HCMV ( P > 0 . 050 ) .

Example answer:
{"entities": [{"text": "analyzed polymorphisms", "type": "BiologicFunction"}, {"text": "pregnant women", "type": "PopulationGroup"}, {"text": "infected", "type": "Finding"}, {"text": "HCMV", "type": "Virus"}]}

Example input:
Sentence: We found substantial individual variation in resistance and tolerance to the fungal pathogen Metarhizium anisopliae Ma549 using the Drosophila melanogaster Genetic Reference Panel ( DGRP ) .

Example answer:
{"entities": [{"text": "individual", "type": "PopulationGroup"}, {"text": "resistance", "type": "BiologicFunction"}, {"text": "fungal pathogen Metarhizium anisopliae Ma549", "type": "Eukaryote"}, {"text": "Drosophila melanogaster Genetic Reference Panel", "type": "Eukaryote"}, {"text": "DGRP", "type": "Eukaryote"}]}

Example input:
Sentence: The genetic basis for variation in resistance to infection in the Drosophila melanogaster genetic reference panel Individuals vary extensively in the way they respond to disease but the genetic basis of this variation is not fully understood .

Example answer:
{"entities": [{"text": "resistance", "type": "BiologicFunction"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "Drosophila melanogaster genetic reference panel", "type": "Eukaryote"}, {"text": "Individuals", "type": "PopulationGroup"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: smegmatis strains resistant to the lead compounds led to the identification of a number of single nucleotide polymorphisms indicating multiple targets .

Example answer:
{"entities": [{"text": "smegmatis", "type": "Bacterium"}, {"text": "lead compounds", "type": "Chemical"}, {"text": "single nucleotide polymorphisms", "type": "SpatialConcept"}]}

Example input:
Sentence: Many candidate genes have homologs identified in studies of human disease , suggesting that genes affecting variation in susceptibility are conserved across species .

Example answer:
{"entities": [{"text": "candidate genes", "type": "AnatomicalStructure"}, {"text": "homologs", "type": "SpatialConcept"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: The size polymorphism in the mt genomes of these closely related Chrysoporthe species was attributed to the varying number and length of introns , coding sequences and to a lesser extent , intergenic sequences .

Example answer:
{"entities": [{"text": "size", "type": "SpatialConcept"}, {"text": "polymorphism", "type": "BiologicFunction"}, {"text": "mt genomes", "type": "AnatomicalStructure"}, {"text": "Chrysoporthe species", "type": "Eukaryote"}, {"text": "introns", "type": "Chemical"}, {"text": "coding sequences", "type": "AnatomicalStructure"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "intergenic sequences", "type": "Chemical"}]}

Example input:
Sentence: Our studies reveal a new paradigm of host - pathogen interactions , in which pathogens exploit conserved host post - translational modifications , thereby achieving highly specific receptor binding while also tolerating genetic changes across multiple isoforms of receptors .

Example answer:
{"entities": [{"text": "host - pathogen interactions", "type": "BiologicFunction"}, {"text": "post - translational modifications", "type": "BiologicFunction"}, {"text": "receptor binding", "type": "BiologicFunction"}, {"text": "genetic changes", "type": "BiologicFunction"}, {"text": "isoforms", "type": "Chemical"}, {"text": "receptors", "type": "Chemical"}]}

Example input:
Sentence: Human mobility networks and persistence of rapidly mutating pathogens Rapidly mutating pathogens may be able to persist in the population and reach an endemic equilibrium by escaping hosts ' acquired immunity .

Example answer:
{"entities": [{"text": "Human", "type": "Eukaryote"}, {"text": "mutating", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}, {"text": "acquired immunity", "type": "BiologicFunction"}]}

Example input:
Sentence: The mean survival time was significantly prolonged in patients carrying 1 or 2 C alleles ( C / C or C / T genotype ) compared with patients lacking the C allele ( T / T genotype ) [ T / T vs .

Example answer:
{"entities": [{"text": "C", "type": "Chemical"}, {"text": "alleles", "type": "AnatomicalStructure"}, {"text": "T", "type": "Chemical"}, {"text": "allele", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The majority of polymorphisms increasing resistance to Ma549 were sex biased , located in non - coding regions , had moderately large effect and were rare , suggesting that there is a general cost to defense .

Example answer:
{"entities": [{"text": "polymorphisms", "type": "BiologicFunction"}, {"text": "resistance", "type": "BiologicFunction"}, {"text": "Ma549", "type": "Eukaryote"}, {"text": "non - coding regions", "type": "Chemical"}]}

Input:
Sentence: We identified polymorphisms associated with differences between lines in both their mean survival times and microenvironmental plasticity , suggesting that lines differ in their ability to adapt to variable pathogen exposures .

## Item MedMentions:test:3622
Example input:
Sentence: Fluorescently tagged TMCs localize to the tips of stereocilia , the site of the transduction channels .

Example answer:
{"entities": [{"text": "Fluorescently tagged", "type": "HealthCareActivity"}, {"text": "TMCs", "type": "Chemical"}, {"text": "localize", "type": "SpatialConcept"}, {"text": "stereocilia", "type": "AnatomicalStructure"}, {"text": "transduction", "type": "BiologicFunction"}, {"text": "channels", "type": "Chemical"}]}

Example input:
Sentence: The expression of OsAld - Y - GFP fusion protein in tobacco epidermal cells showed that OsAld - Y was localized to the peroxisome .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "OsAld - Y", "type": "Chemical"}, {"text": "GFP", "type": "Chemical"}, {"text": "fusion protein", "type": "Chemical"}, {"text": "tobacco", "type": "Eukaryote"}, {"text": "epidermal cells", "type": "AnatomicalStructure"}, {"text": "peroxisome", "type": "AnatomicalStructure"}]}

Example input:
Sentence: GFP -tagged Tsps co - localized with the proton pump on the contractile vacuole network .

Example answer:
{"entities": [{"text": "GFP", "type": "Chemical"}, {"text": "Tsps", "type": "Chemical"}, {"text": "proton pump", "type": "Chemical"}, {"text": "contractile vacuole network", "type": "BiologicFunction"}]}

Example input:
Sentence: By contrast , repression of SlTDT in tomato reduced malate content of and increased citrate content .

Example answer:
{"entities": [{"text": "SlTDT", "type": "AnatomicalStructure"}, {"text": "tomato", "type": "Eukaryote"}, {"text": "malate", "type": "Chemical"}, {"text": "citrate", "type": "Chemical"}]}

Example input:
Sentence: Here , we report an unexpected finding of non - overlapping localization of these two proteins in mouse NMJs revealed using dual - color stimulated emission depletion ( STED ) super resolution microscopy .

Example answer:
{"entities": [{"text": "non - overlapping localization", "type": "BiologicFunction"}, {"text": "proteins", "type": "Chemical"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "NMJs", "type": "AnatomicalStructure"}, {"text": "super resolution microscopy", "type": "HealthCareActivity"}]}

Example input:
Sentence: The expression patterns of SlTDT in tomato were analyzed by RT - qPCR .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "SlTDT", "type": "AnatomicalStructure"}, {"text": "tomato", "type": "Eukaryote"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: Optimized blue - light illumination triggered the co - localization of TALE constructs with DNMT3A - CD or TET1 - CD fusion proteins at the targeted site of the Ascl1 promoter .

Example answer:
{"entities": [{"text": "illumination", "type": "HealthCareActivity"}, {"text": "TALE constructs", "type": "Chemical"}, {"text": "DNMT3A", "type": "Chemical"}, {"text": "CD", "type": "SpatialConcept"}, {"text": "TET1", "type": "Chemical"}, {"text": "fusion proteins", "type": "Chemical"}, {"text": "Ascl1", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}]}

Example input:
Sentence: Gas chromatography - mass spectrometer ( GC - MS ) analysis showed that overexpression of SlTDT significantly increased malate content , and reduced citrate content in tomato fruit .

Example answer:
{"entities": [{"text": "Gas chromatography - mass spectrometer", "type": "HealthCareActivity"}, {"text": "GC - MS ) analysis", "type": "HealthCareActivity"}, {"text": "overexpression", "type": "BiologicFunction"}, {"text": "SlTDT", "type": "AnatomicalStructure"}, {"text": "malate", "type": "Chemical"}, {"text": "citrate", "type": "Chemical"}, {"text": "tomato", "type": "Eukaryote"}, {"text": "fruit", "type": "Food"}]}

Example input:
Sentence: These results indicated that SlTDT played an important role in remobilization of malate and citrate in fruit vacuoles .

Example answer:
{"entities": [{"text": "SlTDT", "type": "AnatomicalStructure"}, {"text": "malate", "type": "Chemical"}, {"text": "citrate", "type": "Chemical"}, {"text": "fruit", "type": "Food"}, {"text": "vacuoles", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The results indicated that SlTDT expressed in leaves , roots , flowers and fruits at different ripening stages , suggesting SlTDT may be associated with the development of different tissues .

Example answer:
{"entities": [{"text": "indicated", "type": "Finding"}, {"text": "SlTDT", "type": "AnatomicalStructure"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "leaves", "type": "Eukaryote"}, {"text": "roots", "type": "Eukaryote"}, {"text": "flowers", "type": "Eukaryote"}, {"text": "fruits", "type": "Food"}, {"text": "ripening", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Input:
Sentence: Confocal microscopic study using green fluorescent fusion proteins revealed that SlTDT was localized on tonoplast .
