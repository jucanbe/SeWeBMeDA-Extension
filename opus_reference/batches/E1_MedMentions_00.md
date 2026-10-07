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

## Item MedMentions:test:21
Example input:
Sentence: 46 . 5 years , P < 0 . 001 )

Example answer:
{"entities": []}

Example input:
Sentence: 6 ( P ≤ 0 . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 6 months , P = 0 . 502 ; OS : 7 . 0 vs 7 . 8 months , P = 0 . 452 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 21 . 3 months , p = -0 . 01 )

Example answer:
{"entities": []}

Example input:
Sentence: 68 days .

Example answer:
{"entities": []}

Example input:
Sentence: 1 vs 7 . 6 months , P = 0 . 316 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 8 months , P = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 61±1 . 0 days .

Example answer:
{"entities": []}

Example input:
Sentence: 94 days ) ( P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 9 days ; P = .009 ) .

Example answer:
{"entities": []}

Input:
Sentence: 6 days ; P = .

## Item MedMentions:test:105
Example input:
Sentence: 24 . 6 % , P = 0 . 056 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 38ng / mL , P = 0 . 008 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 27 ( 6 . 7 % ) ( P = 0 . 086 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 27 . 7 0 . 8 % , respectively , p < 0 . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 27 . 3 % ; p = 0 . 5988 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % versus 7 . 0 % ( P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 1 mm ( 2 ) ( p < 0 . 05 ) at final follow - up as assessed by CT , and from 154 . 1 ± 93 .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}]}

Example input:
Sentence: 39±3 . 81 % , p < 0 . 001 ; respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: I . 95 % : 7 . 2 - 38 . 6 vs 60 . 0 % , C . I . 95 % : 21 . 6 - 84 . 3 , p = 0 . 01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 26 . 0 mm / mm ( 2 ) ; P ≤ 0 . 001 ) .

Example answer:
{"entities": []}

Input:
Sentence: 383 mm ( 3 ) ; p < 0 . 001 ) and more often progressive ( 68 % vs .

## Item MedMentions:test:292
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

## Item MedMentions:test:1
Example input:
Sentence: 4 months of follow - up , 31 . 7 % ( 126 / 398 ) of the patients showed clinical recurrence .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: A total of 224 ( 93 % ) patients who completed 6 months ' adherence assessment were included in the model .

Example answer:
{"entities": []}

Example input:
Sentence: Subjects had a median of 6 ED visits , and 2 inpatient admissions in the past 12 months at this hospital .

Example answer:
{"entities": [{"text": "Subjects", "type": "PopulationGroup"}, {"text": "ED visits", "type": "HealthCareActivity"}, {"text": "hospital", "type": "Organization"}]}

Example input:
Sentence: A total of 65 , 359 patients were included : 63 , 597 ( 97 . 3 % ) PA patients and 1 , 762 SA patients ( 2 . 7 % ) .

Example answer:
{"entities": [{"text": "PA", "type": "BiologicFunction"}, {"text": "SA", "type": "Finding"}]}

Example input:
Sentence: Twenty - eight patients were eligible for three - month follow - up .

Example answer:
{"entities": [{"text": "patients were eligible for three - month follow - up", "type": "Finding"}]}

Example input:
Sentence: Follow - up data were available for 104 patients ( 42 % ) , of whom 64 had NPSLE ( 61 . 5 % ) .

Example answer:
{"entities": [{"text": "Follow - up", "type": "HealthCareActivity"}, {"text": "NPSLE", "type": "BiologicFunction"}]}

Example input:
Sentence: 4322 patients ( 17 . 1 % ) met the primary outcome .

Example answer:
{"entities": []}

Example input:
Sentence: Until December 2015 , we have registered 2880 patients that were treated in 3959 surgeries and 8528 consultations .

Example answer:
{"entities": [{"text": "surgeries", "type": "HealthCareActivity"}, {"text": "consultations", "type": "HealthCareActivity"}]}

Example input:
Sentence: Over a 2 - year period , 141 patients were followed .

Example answer:
{"entities": []}

Example input:
Sentence: In total , 519 patients completed 1 year of follow - up , among which 69 ( 13 .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Input:
Sentence: From 1 July 2013 to 31 September 2014 , 686 patients were referred , 338 ( 49 . 3 % ) attended a first appointment and 172 ( 25 . 1 % ) completed follow - up .

## Item MedMentions:test:131
Example input:
Sentence: Fifteen articles were considered for this review .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}]}

Example input:
Sentence: In total , we identified 791 references , retrieved 20 full text articles , and included nine studies in our review .

Example answer:
{"entities": [{"text": "references", "type": "IntellectualProduct"}, {"text": "full text articles", "type": "IntellectualProduct"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: After a further evaluation , 22 articles were analyzed .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: Thirteen publications , including 11 studies , met all inclusion and exclusion criteria .

Example answer:
{"entities": [{"text": "publications", "type": "IntellectualProduct"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: The initial search retrieved 1240 articles . Twenty - two articles were selected and used in the review .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}, {"text": "review", "type": "IntellectualProduct"}]}

Example input:
Sentence: Four articles meeting the inclusion criteria were included in the review .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}]}

Example input:
Sentence: Sixty - seven relevant articles were identified .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}]}

Example input:
Sentence: 21 , 614 articles were identified , 542 were assessed with respect to their eligibility for inclusion and 14 systematic reviews included .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}, {"text": "systematic reviews", "type": "IntellectualProduct"}]}

Example input:
Sentence: Seven hundred thirty - one articles met the search criteria and 51 studies were initially selected .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}, {"text": "studies", "type": "HealthCareActivity"}]}

Example input:
Sentence: Overall , 1 , 554 , 325 articles were analyzed .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Input:
Sentence: A total of 8 articles were included in the final dataset .

## Item MedMentions:test:243
Example input:
Sentence: A larger proportion of pediatric networks ( 43 . 8 % ) had no available specialists in the underlying area when compared with adult networks ( 10 . 4 % ) ( P < .001 for all specialties ) .

Example answer:
{"entities": [{"text": "pediatric", "type": "ProfessionalOrOccupationalGroup"}, {"text": "specialists", "type": "ProfessionalOrOccupationalGroup"}, {"text": "underlying area", "type": "SpatialConcept"}, {"text": "specialties", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: An established relationship with a primary care physician was significantly associated with better care coordination , whereas being chronically ill or younger was associated with poorer care coordination .

Example answer:
{"entities": [{"text": "primary care physician", "type": "ProfessionalOrOccupationalGroup"}, {"text": "chronically ill", "type": "BiologicFunction"}]}

Example input:
Sentence: Overall , paediatricians and paediatric residents view the positive impact on paediatric patients as the most important aspect of hospital clown visits , rather than the clinical efficacy of hospital clowning .

Example answer:
{"entities": [{"text": "paediatricians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "view", "type": "BiologicFunction"}, {"text": "positive", "type": "Finding"}, {"text": "hospital clown", "type": "ProfessionalOrOccupationalGroup"}, {"text": "visits", "type": "HealthCareActivity"}, {"text": "hospital clowning", "type": "Organization"}]}

Example input:
Sentence: • In general , paediatricians have positive ideas about hospital clowns , aside from personal prejudices .

Example answer:
{"entities": [{"text": "paediatricians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "positive", "type": "Finding"}, {"text": "hospital clowns", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: In addition , there has been no progress in the development of an empathetic , respectful or person - centered clinical practice ; instead , economic , social and educational differences perpetuate a paternalistic clinical practice .

Example answer:
{"entities": []}

Example input:
Sentence: This report reviews new studies of the epidemiology of father involvement , including nonresidential as well as residential fathers .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "epidemiology", "type": "ResearchActivity"}, {"text": "nonresidential", "type": "Finding"}]}

Example input:
Sentence: CONCLUSIONS : This study provides promising support for the PAT as a psychosocial screener for families of infants and older children across illness conditions .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "PAT", "type": "IntellectualProduct"}, {"text": "screener", "type": "HealthCareActivity"}, {"text": "illness", "type": "Finding"}]}

Example input:
Sentence: The effects of father involvement on child outcomes are discussed within each phase of a child 's development .

Example answer:
{"entities": [{"text": "child outcomes", "type": "BiologicFunction"}, {"text": "child 's development", "type": "BiologicFunction"}]}

Example input:
Sentence: Narrow networks were more prevalent among pediatric than adult specialists , because of both the sparseness of pediatric specialists and their exclusion from networks .

Example answer:
{"entities": [{"text": "pediatric", "type": "ProfessionalOrOccupationalGroup"}, {"text": "specialists", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Implications and advice for all child health providers to encourage and support father involvement are outlined .

Example answer:
{"entities": [{"text": "advice", "type": "HealthCareActivity"}, {"text": "health providers", "type": "ProfessionalOrOccupationalGroup"}]}

Input:
Sentence: The role of pediatricians in working with fathers has correspondingly increased in importance .

## Item MedMentions:test:294
Example input:
Sentence: Therefore , the increased activity during less favorable weather conditions and the fast recruitment of nestmates following the discovery of a food source , as observed for P . orizabaensis , may be adaptations that evolved to coexist even with more aggressive and dominant species of stingless bees , with which P .

Example answer:
{"entities": [{"text": "nestmates", "type": "PopulationGroup"}, {"text": "food", "type": "Food"}, {"text": "source", "type": "Finding"}, {"text": "P . orizabaensis", "type": "Eukaryote"}, {"text": "adaptations", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "stingless bees", "type": "Eukaryote"}, {"text": "P .", "type": "Eukaryote"}]}

Example input:
Sentence: Altered natal dispersal at the range periphery : The role of behavior , resources , and maternal condition Natal dispersal outcomes are an interplay between environmental conditions and individual phenotypes .

Example answer:
{"entities": [{"text": "natal", "type": "SpatialConcept"}, {"text": "periphery", "type": "SpatialConcept"}, {"text": "maternal", "type": "Finding"}, {"text": "Natal", "type": "SpatialConcept"}, {"text": "environmental", "type": "SpatialConcept"}]}

Example input:
Sentence: An Inhibitory Septum to Lateral Hypothalamus Circuit That Suppresses Feeding Feeding behavior is orchestrated by neural circuits primarily residing in the hypothalamus and hindbrain .

Example answer:
{"entities": [{"text": "Lateral Hypothalamus", "type": "SpatialConcept"}, {"text": "hypothalamus", "type": "AnatomicalStructure"}, {"text": "hindbrain", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We combined studies of prey abundance , feeding behavior , and stable isotope analyses of diet in both seagrass and coral rubble to determine if N . bredini 's diet was consistent across different habitat types .

Example answer:
{"entities": [{"text": "stable isotope analyses", "type": "ResearchActivity"}, {"text": "diet", "type": "Food"}, {"text": "seagrass", "type": "Eukaryote"}, {"text": "coral rubble", "type": "Eukaryote"}, {"text": "N . bredini 's", "type": "Eukaryote"}, {"text": "habitat types", "type": "SpatialConcept"}]}

Example input:
Sentence: Our findings are consistent with the idea that diffuse co - evolution drives the evolution of extremely long proboscises and flower tubes , and highlight the importance of morphological traits , beyond the forbidden links hypothesis , in structuring interactions between mutualistic partners , revealing that the role of niche - based processes can be much more complex than previously known .

Example answer:
{"entities": [{"text": "co - evolution", "type": "BiologicFunction"}, {"text": "evolution", "type": "BiologicFunction"}, {"text": "long proboscises", "type": "Eukaryote"}, {"text": "flower tubes", "type": "Eukaryote"}, {"text": "morphological", "type": "SpatialConcept"}]}

Example input:
Sentence: We found convergence in morphological traits across the five communities and that the distribution of morphological differences between hawkmoths and plants is consistent with expectations under the morphological match hypothesis in three of the five communities .

Example answer:
{"entities": [{"text": "morphological", "type": "SpatialConcept"}, {"text": "hawkmoths", "type": "Eukaryote"}, {"text": "plants", "type": "Eukaryote"}]}

Example input:
Sentence: In combination with the phylogenetically informed morphometric analyses , our results suggest that the morphological changes of non - human anthropoid hands did not coevolve with the brain to facilitate the manipulative ability during the evolutionary process , although the manipulative ability is a survival skill .

Example answer:
{"entities": [{"text": "phylogenetically informed morphometric analyses", "type": "HealthCareActivity"}, {"text": "morphological", "type": "SpatialConcept"}, {"text": "non - human anthropoid hands", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "evolutionary process", "type": "BiologicFunction"}]}

Example input:
Sentence: Biphasic character was also demonstrated at the functional level via differing affinities on either side of the BJPNF for cell attachment .

Example answer:
{"entities": [{"text": "BJPNF", "type": "Chemical"}, {"text": "cell attachment", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Recently , optimal foraging models have predicted that there might be a close association between mouthparts ' length and the corolla depth of the visited flowers , thus favouring trait convergence and specialization at community level .

Example answer:
{"entities": [{"text": "corolla", "type": "Eukaryote"}, {"text": "depth", "type": "SpatialConcept"}, {"text": "flowers", "type": "Eukaryote"}]}

Example input:
Sentence: Using multiple lines of study to describe the natural diets of other presumed specialists may demonstrate that specialized morphology often broadens rather than narrows diet breadth .

Example answer:
{"entities": [{"text": "diets", "type": "Food"}]}

Input:
Sentence: Thus , contrary to expectation , the specialized feeding morphology of N .

## Item MedMentions:test:403
Example input:
Sentence: 8U·g ( - 1 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The college offers PhD programs in these five disciplines : Cancer Biology , Medicinal Chemistry , Pharmaceutics , Pharmacognosy , and Pharmacology . One of the Pharmacognosy dissertations focused on plant - derived natural products with potential anti - inflammatory and cancer chemopreventive activities .

Example answer:
{"entities": [{"text": "college", "type": "Organization"}, {"text": "PhD", "type": "IntellectualProduct"}, {"text": "Cancer Biology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Medicinal Chemistry", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Pharmaceutics", "type": "ResearchActivity"}, {"text": "Pharmacognosy", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Pharmacology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "dissertations", "type": "IntellectualProduct"}, {"text": "plant - derived", "type": "Eukaryote"}, {"text": "natural products", "type": "Chemical"}, {"text": "cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Applicants to the University College of Teacher Education Styria ( N = 243 ) completed personality scales as part of their college admission process .

Example answer:
{"entities": [{"text": "Applicants", "type": "PopulationGroup"}, {"text": "University College of Teacher Education", "type": "Organization"}, {"text": "Styria", "type": "SpatialConcept"}, {"text": "personality scales", "type": "IntellectualProduct"}, {"text": "college admission process", "type": "IntellectualProduct"}]}

Example input:
Sentence: He studied medicine at the University of Michigan , graduated in 1973 , and after a rotating internship , he completed a master 's degree in maternal and child health ( 1976 ) and a PhD in epidemiology ( 1979 ) at the University of North Carolina in Chapel Hill . After graduation , he went to work at the National Institute of Environmental Health Sciences ( NIEHS , one of the US National Institutes of Health ) in Durham , NC , where he has spent his career .

Example answer:
{"entities": [{"text": "medicine", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "University of Michigan", "type": "Organization"}, {"text": "PhD", "type": "IntellectualProduct"}, {"text": "epidemiology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "University of North Carolina", "type": "Organization"}, {"text": "Chapel Hill", "type": "SpatialConcept"}, {"text": "National Institute of Environmental Health Sciences", "type": "Organization"}, {"text": "NIEHS", "type": "Organization"}, {"text": "US National Institutes of Health", "type": "Organization"}, {"text": "Durham , NC", "type": "SpatialConcept"}]}

Example input:
Sentence: ubc .

Example answer:
{"entities": [{"text": "ubc .", "type": "IntellectualProduct"}]}

Example input:
Sentence: ubc .

Example answer:
{"entities": [{"text": "ubc .", "type": "IntellectualProduct"}]}

Example input:
Sentence: S . and a U .

Example answer:
{"entities": [{"text": "S .", "type": "SpatialConcept"}, {"text": "U .", "type": "SpatialConcept"}]}

Example input:
Sentence: The U .

Example answer:
{"entities": [{"text": "U .", "type": "SpatialConcept"}]}

Example input:
Sentence: U .

Example answer:
{"entities": [{"text": "U .", "type": "SpatialConcept"}]}

Example input:
Sentence: U .

Example answer:
{"entities": []}

Input:
Sentence: degree and U .

## Item MedMentions:test:236
Example input:
Sentence: Evaluation of Drug Sorption to PVC - and Non - PVC -based Tubes in Administration Sets Using a Pump Administration sets are delivery tools for the direct application of drugs into the body and are composed of a spike , a drip chamber , tubes , Luer adapters ( connectors ) , a needle cover for protection , and other accessories .

Example answer:
{"entities": [{"text": "Evaluation", "type": "HealthCareActivity"}, {"text": "PVC", "type": "Chemical"}, {"text": "Tubes", "type": "MedicalDevice"}, {"text": "Administration Sets", "type": "MedicalDevice"}, {"text": "Pump", "type": "MedicalDevice"}, {"text": "Administration sets", "type": "MedicalDevice"}, {"text": "delivery tools", "type": "Chemical"}, {"text": "drugs", "type": "Chemical"}, {"text": "body", "type": "Eukaryote"}, {"text": "spike", "type": "MedicalDevice"}, {"text": "drip chamber", "type": "MedicalDevice"}, {"text": "tubes", "type": "MedicalDevice"}, {"text": "Luer adapters", "type": "MedicalDevice"}, {"text": "needle cover", "type": "MedicalDevice"}]}

Example input:
Sentence: Thus , the VPA treated P - MSCs can serve as an alternative source for deriving neural cells for use in both research and in clinics .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "P", "type": "AnatomicalStructure"}, {"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "neural cells", "type": "AnatomicalStructure"}, {"text": "research", "type": "ResearchActivity"}, {"text": "clinics", "type": "Organization"}]}

Example input:
Sentence: Confluent bBMVEC monolayers were treated with METH , MDMA and MDPV ( 0 . 5mM - 2 . 5mM ) for 24h .

Example answer:
{"entities": [{"text": "bBMVEC", "type": "AnatomicalStructure"}, {"text": "monolayers", "type": "AnatomicalStructure"}, {"text": "METH", "type": "Chemical"}, {"text": "MDMA", "type": "Chemical"}, {"text": "MDPV", "type": "Chemical"}]}

Example input:
Sentence: Our preliminary experience suggests that placement of IVC filters for treatment of venous thrombotic events in an office - based facility is safe and efficacious with basic endovascular equipment .

Example answer:
{"entities": [{"text": "experience", "type": "BiologicFunction"}, {"text": "placement", "type": "HealthCareActivity"}, {"text": "IVC filters", "type": "MedicalDevice"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "venous thrombotic events", "type": "BiologicFunction"}, {"text": "office - based facility", "type": "Organization"}, {"text": "endovascular equipment", "type": "MedicalDevice"}]}

Example input:
Sentence: All women were treated with PBI consisting of PDMS - U , a bulking agent that polymerizes in situ .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "PBI", "type": "HealthCareActivity"}, {"text": "PDMS - U", "type": "Chemical"}, {"text": "bulking agent", "type": "Chemical"}, {"text": "in situ", "type": "SpatialConcept"}]}

Example input:
Sentence: ESC were treated with the progestins , medroxyprogesterone acetate ( MPA ) , norethisterone acetate ( NETA ) , or dienogest ( DNG ) and cytokine mRNA production , protein secretion , and cell viability measured .

Example answer:
{"entities": [{"text": "ESC", "type": "AnatomicalStructure"}, {"text": "progestins", "type": "Chemical"}, {"text": "medroxyprogesterone acetate", "type": "Chemical"}, {"text": "MPA", "type": "Chemical"}, {"text": "norethisterone acetate", "type": "Chemical"}, {"text": "NETA", "type": "Chemical"}, {"text": "dienogest", "type": "Chemical"}, {"text": "DNG", "type": "Chemical"}, {"text": "cytokine", "type": "Chemical"}, {"text": "mRNA production", "type": "BiologicFunction"}, {"text": "protein secretion", "type": "BiologicFunction"}, {"text": "cell viability measured", "type": "ResearchActivity"}]}

Example input:
Sentence: When volume reached > 250mm ( 3 , ) interventions included : implantation of drug - free silk foam ( Control -F ) , doxorubicin 400μg foam ( Dox400 -F ) , vincristine 50μg foam ( Vin50 -F ) , drug - free silk gel ( Control -G ) , vincristine 50μg gel ( Vin50 -G ) , or single dose intravenous vincristine 50μg ( Vin50 -IV ) .

Example answer:
{"entities": [{"text": "interventions", "type": "HealthCareActivity"}, {"text": "implantation", "type": "HealthCareActivity"}, {"text": "silk", "type": "Chemical"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "( Dox400", "type": "Chemical"}, {"text": "vincristine", "type": "Chemical"}, {"text": "Vin50", "type": "Chemical"}, {"text": "intravenous", "type": "SpatialConcept"}]}

Example input:
Sentence: The technique can be used in combination with PV isolation to treat persistent AF with good acute success rates , short procedure times , and acceptable safety concerns .

Example answer:
{"entities": [{"text": "PV isolation", "type": "HealthCareActivity"}, {"text": "persistent AF", "type": "BiologicFunction"}]}

Example input:
Sentence: vancomycin - treated patients .

Example answer:
{"entities": [{"text": "vancomycin", "type": "Chemical"}, {"text": "treated", "type": "HealthCareActivity"}]}

Example input:
Sentence: The effectiveness of this fungal species on the degradation of commercial low molecular weight polyvinyl chloride ( PVC ) was studied under laboratory conditions .

Example answer:
{"entities": [{"text": "fungal", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "low molecular weight polyvinyl chloride", "type": "Chemical"}, {"text": "PVC", "type": "Chemical"}]}

Input:
Sentence: treated PVC .

## Item MedMentions:test:361
Example input:
Sentence: 0 μg / kg in the starter period and 22 . 5 μg / kg in the finisher period .

Example answer:
{"entities": []}

Example input:
Sentence: 98 µg / mL .

Example answer:
{"entities": []}

Example input:
Sentence: 91 , 1 . 83 , 3 . 66 and 7 . 33μg / ml respectively , for 24h .

Example answer:
{"entities": []}

Example input:
Sentence: 8 μg / kg , while the registered amount s in the other samples were < 1 μg / kg .

Example answer:
{"entities": [{"text": "registered", "type": "HealthCareActivity"}]}

Example input:
Sentence: 3 to 52 . 5 μg / m ( 3 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 98 µg / mL and higher .

Example answer:
{"entities": []}

Example input:
Sentence: 90±6 . 86 µg / ml at 24 and 48 h , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: For example , a 10 μg / m³ increase of 7 - day ( lag 06 ) average concentrations of PM10 ( particulate matter no greater than 10 microns ) , SO₂ , NO₂ was associated with 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 1 μg / m³ ( range 4 . 1 - 42 . 3 ) , and that of O₃ was 75 . 0 μg / m³ ( range : 51 . 3 - 106 . 3 ) .

Example answer:
{"entities": [{"text": "O₃", "type": "Chemical"}]}

Example input:
Sentence: That of NO₂ was 17 . 0 μg / m³ ( range : 4 . 7 - 31 . 3 ) , NOx was 82 .

Example answer:
{"entities": [{"text": "NO₂", "type": "Chemical"}, {"text": "NOx", "type": "Chemical"}]}

Input:
Sentence: 1 μg / m³ ( range : 13 . 3 - 165 . 3 ) , and NO was 65 μg / m³ ( range : 8 . 7 - 138 . 4 ) during the study period .

## Item MedMentions:test:30
Example input:
Sentence: The signal of human settlement on modern forests is broad , spatially varying and acts to homogenize modern forests relative to their historic counterparts , with significant implications for future management .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "broad", "type": "SpatialConcept"}]}

Example input:
Sentence: Indigenous forest patches within the plantation mosaic contained a highly characteristic acoustic species assemblage , emphasizing their complementary contribution to local biodiversity .

Example answer:
{"entities": [{"text": "acoustic species", "type": "IntellectualProduct"}, {"text": "local", "type": "SpatialConcept"}]}

Example input:
Sentence: Identifying those at highest risk would allow hearing conservation activities to be focused on those individuals .

Example answer:
{"entities": [{"text": "Identifying", "type": "HealthCareActivity"}, {"text": "hearing", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: Areas covered in nonnative timber or grass species were devoid of acoustic species .

Example answer:
{"entities": [{"text": "Areas", "type": "SpatialConcept"}, {"text": "nonnative timber", "type": "Eukaryote"}, {"text": "grass", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "acoustic species", "type": "IntellectualProduct"}]}

Example input:
Sentence: Natural vegetation patches inside the plantation mosaic supported high mean acoustic diversity ( indigenous forests 7 . 6 , grasslands 8 . 0 , wetlands 9 . 1 ) , which increased as plant heterogeneity and patch size increased .

Example answer:
{"entities": [{"text": "grasslands", "type": "SpatialConcept"}, {"text": "plant", "type": "Eukaryote"}, {"text": "patch size", "type": "SpatialConcept"}]}

Example input:
Sentence: These tools allow audiologists to focus hearing conservation efforts on those individuals who are most in need of those services .

Example answer:
{"entities": [{"text": "tools", "type": "IntellectualProduct"}, {"text": "audiologists", "type": "ProfessionalOrOccupationalGroup"}, {"text": "hearing", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: For that purpose , real - time auditory feedback of physiological and physical information based on sound signals , often termed " sonification , " has been proven particularly useful .

Example answer:
{"entities": []}

Example input:
Sentence: Large , natural , protected grassland sites in the PA had the highest mean acoustic diversity ( 14 . 1 species / site ) .

Example answer:
{"entities": [{"text": "grassland sites", "type": "SpatialConcept"}, {"text": "PA", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "site", "type": "SpatialConcept"}]}

Example input:
Sentence: The spatial signals of novelty and ecological change also point to potential challenges in using modern spatial distributions of species and communities and their relationship to underlying geophysical and climatic attributes in understanding potential responses to changing climate .

Example answer:
{"entities": [{"text": "spatial distributions", "type": "SpatialConcept"}, {"text": "species", "type": "Eukaryote"}]}

Example input:
Sentence: Use of ecoacoustics to determine biodiversity patterns across ecological gradients The variety of local animal sounds characterizes a landscape .

Example answer:
{"entities": [{"text": "patterns", "type": "SpatialConcept"}, {"text": "ecological", "type": "SpatialConcept"}, {"text": "local", "type": "SpatialConcept"}, {"text": "animal", "type": "Eukaryote"}, {"text": "landscape", "type": "SpatialConcept"}]}

Input:
Sentence: Overall , acoustic signals determined spatial biodiversity patterns and can be a useful tool for guiding conservation .

## Item MedMentions:test:134
Example input:
Sentence: Here , we describe genetic mutational analysis of CHH genes in Indonesian 46 , XY disorder of sex development patients with under - virilisation .

Example answer:
{"entities": [{"text": "genetic mutational", "type": "BiologicFunction"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "CHH", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "Indonesian", "type": "PopulationGroup"}, {"text": "46 , XY disorder of sex development", "type": "BiologicFunction"}, {"text": "under - virilisation", "type": "BiologicFunction"}]}

Example input:
Sentence: Haemoglobinopathies and β - Thalassaemia among the Tribals Working in the Tea Gardens of Assam , India Prevalence of haemoglobinopathies and β - thalassaemia are very high in India but information about its status among the tribals working in the tea gardens of Assam is very less .

Example answer:
{"entities": [{"text": "Haemoglobinopathies", "type": "BiologicFunction"}, {"text": "β - Thalassaemia", "type": "BiologicFunction"}, {"text": "Tribals", "type": "PopulationGroup"}, {"text": "Tea", "type": "Food"}, {"text": "India", "type": "SpatialConcept"}, {"text": "haemoglobinopathies", "type": "BiologicFunction"}, {"text": "β - thalassaemia", "type": "BiologicFunction"}, {"text": "tribals", "type": "PopulationGroup"}, {"text": "tea", "type": "Food"}]}

Example input:
Sentence: A total 1204 samples from the tribals working in tea gardens of Assam were analysed for both Complete Blood Count ( CBC ) and High Pressure Liquid Chromatography ( HPLC ) for detection of haemoglobinopathies and β - thalassaemia .

Example answer:
{"entities": [{"text": "tribals", "type": "PopulationGroup"}, {"text": "tea", "type": "Food"}, {"text": "analysed", "type": "ResearchActivity"}, {"text": "Complete Blood Count", "type": "HealthCareActivity"}, {"text": "CBC", "type": "HealthCareActivity"}, {"text": "High Pressure Liquid Chromatography", "type": "HealthCareActivity"}, {"text": "HPLC", "type": "HealthCareActivity"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "haemoglobinopathies", "type": "BiologicFunction"}, {"text": "β - thalassaemia", "type": "BiologicFunction"}]}

Example input:
Sentence: Association of CDKAL1 , CDKN2A / B & HHEX gene polymorphisms with type 2 diabetes mellitus in the population of Hyderabad , India The genome - wide association studies ( GWAS ) have shown an association of type 2 diabetes mellitus ( T2DM ) with several novel genes .

Example answer:
{"entities": [{"text": "CDKAL1", "type": "AnatomicalStructure"}, {"text": "CDKN2A", "type": "AnatomicalStructure"}, {"text": "B", "type": "AnatomicalStructure"}, {"text": "HHEX", "type": "AnatomicalStructure"}, {"text": "type 2 diabetes mellitus", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}, {"text": "India", "type": "SpatialConcept"}, {"text": "genome - wide association studies", "type": "ResearchActivity"}, {"text": "GWAS", "type": "ResearchActivity"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We postulate that variants in CHH genes , in particular PROKR2 , PROK2 , WDR11 and FGFR1 with CHD7 , may contribute to under - virilisation phenotypes including hypospadias in Indonesia .

Example answer:
{"entities": [{"text": "CHH", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "PROKR2", "type": "AnatomicalStructure"}, {"text": "PROK2", "type": "AnatomicalStructure"}, {"text": "WDR11", "type": "AnatomicalStructure"}, {"text": "FGFR1", "type": "AnatomicalStructure"}, {"text": "CHD7", "type": "AnatomicalStructure"}, {"text": "under - virilisation", "type": "BiologicFunction"}, {"text": "hypospadias", "type": "BiologicFunction"}, {"text": "Indonesia", "type": "SpatialConcept"}]}

Example input:
Sentence: Here , we report , for the first time in India , the complete genome sequence of BGE14 / ABT1 / MVC / India , a reassortment strain with segments A and B derived from a very virulent IBDV strain and an attenuated IBDV , respectively .

Example answer:
{"entities": [{"text": "India", "type": "SpatialConcept"}, {"text": "genome sequence", "type": "AnatomicalStructure"}, {"text": "BGE14 / ABT1 / MVC / India", "type": "Virus"}, {"text": "segments A and B", "type": "AnatomicalStructure"}, {"text": "IBDV", "type": "Virus"}]}

Example input:
Sentence: Our results indicated a higher prevalence of β - thalassaemia ( 3 . 07 % ) among the Munda ethnic group and higher prevalence of sickle cell anaemia ( 4 . 73 % ) among the Lohar ethnic group .

Example answer:
{"entities": [{"text": "indicated", "type": "Finding"}, {"text": "β - thalassaemia", "type": "BiologicFunction"}, {"text": "Munda ethnic group", "type": "PopulationGroup"}, {"text": "sickle cell anaemia", "type": "BiologicFunction"}, {"text": "Lohar ethnic group", "type": "PopulationGroup"}]}

Example input:
Sentence: This was the first study to report the presence of HbE among the tribals working in the tea gardens of Assam .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "presence", "type": "Finding"}, {"text": "HbE", "type": "Chemical"}, {"text": "tribals", "type": "PopulationGroup"}, {"text": "tea", "type": "Food"}]}

Example input:
Sentence: We report here the findings on the pattern of genetic association of three genes ( CDKAL1 , CDKN2A / B and HHEX ) with T2DM in the population of Hyderabad , south India .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "CDKAL1", "type": "AnatomicalStructure"}, {"text": "CDKN2A", "type": "AnatomicalStructure"}, {"text": "B", "type": "AnatomicalStructure"}, {"text": "HHEX", "type": "AnatomicalStructure"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}, {"text": "India", "type": "SpatialConcept"}]}

Example input:
Sentence: Serogroup H was found along with serogroup B in 12 ( 55 . 26 % ) samples and with serogroup I in 8 ( 22 . 2 % ) samples .

Example answer:
{"entities": [{"text": "Serogroup H", "type": "IntellectualProduct"}, {"text": "serogroup B", "type": "IntellectualProduct"}, {"text": "serogroup I", "type": "IntellectualProduct"}]}

Input:
Sentence: The serogroup H was identified for the first time from the Indian subcontinent .

## Item MedMentions:test:141
Example input:
Sentence: pylori by the persistence of DNA breaks but not by enhanced mutagenesis .

Example answer:
{"entities": [{"text": "pylori", "type": "Bacterium"}, {"text": "DNA breaks", "type": "BiologicFunction"}, {"text": "mutagenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: melanogaster are much higher than the short - term ones , indicating a continuing decline in selection intensity , to such an extent that the short - term estimates suggest that selection is only active in the most GC -rich parts of the genome .

Example answer:
{"entities": [{"text": "melanogaster", "type": "Eukaryote"}, {"text": "selection", "type": "BiologicFunction"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "genome", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Genotypes 1 and 4 demonstrated remarkable similarity in terms of genome sequences and proteins , but surprisingly , in terms of the preferred codons for gene expression , they showed the greatest difference .

Example answer:
{"entities": [{"text": "proteins", "type": "Chemical"}, {"text": "codons", "type": "SpatialConcept"}, {"text": "gene expression", "type": "BiologicFunction"}]}

Example input:
Sentence: Human mobility networks and persistence of rapidly mutating pathogens Rapidly mutating pathogens may be able to persist in the population and reach an endemic equilibrium by escaping hosts ' acquired immunity .

Example answer:
{"entities": [{"text": "Human", "type": "Eukaryote"}, {"text": "mutating", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}, {"text": "acquired immunity", "type": "BiologicFunction"}]}

Example input:
Sentence: The results showed a higher persistence in the host by B .

Example answer:
{"entities": [{"text": "persistence", "type": "BiologicFunction"}, {"text": "B .", "type": "Bacterium"}]}

Example input:
Sentence: Purging was negligible , but allele frequencies were strongly affected by drift in small populations , while selection for inbreeding avoidance was weak in larger populations because inbreeding risk decreased .

Example answer:
{"entities": [{"text": "drift", "type": "BiologicFunction"}, {"text": "inbreeding", "type": "BiologicFunction"}]}

Example input:
Sentence: This suggests that the dependence of inactivation on genome type disappeared in favor of protein -mediated inactivation mechanisms common to all viruses .

Example answer:
{"entities": [{"text": "genome type", "type": "AnatomicalStructure"}, {"text": "protein", "type": "Chemical"}, {"text": "viruses", "type": "Virus"}]}

Example input:
Sentence: The mechanism of duplication matters , with whole - genome duplicates exhibiting different preservation trends compared to small - scale duplicates .

Example answer:
{"entities": [{"text": "genome", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The possession of a highly mobile genome has contributed to the genetic diversity and ongoing evolution of C .

Example answer:
{"entities": [{"text": "mobile genome", "type": "AnatomicalStructure"}, {"text": "evolution", "type": "BiologicFunction"}, {"text": "C .", "type": "Bacterium"}]}

Example input:
Sentence: In contrast , the other genome types are more stable ; therefore , inactivation is slower and mainly driven by the degradation of viral proteins .

Example answer:
{"entities": [{"text": "genome types", "type": "AnatomicalStructure"}, {"text": "viral proteins", "type": "Chemical"}]}

Input:
Sentence: Genome type appeared to be the major determinant for persistence .

## Item MedMentions:test:270
Example input:
Sentence: A critical feature in working with this client group is to recognize their ambiguity and the fragility and temporality of their decisions about their destiny .

Example answer:
{"entities": [{"text": "fragility", "type": "Finding"}, {"text": "temporality", "type": "BiologicFunction"}, {"text": "decisions", "type": "BiologicFunction"}]}

Example input:
Sentence: Mining Health App Data to Find More and Less Successful Weight Loss Subgroups More than half of all smartphone app downloads involve weight , diet , and exercise .

Example answer:
{"entities": [{"text": "Health App", "type": "IntellectualProduct"}, {"text": "Weight Loss", "type": "Finding"}, {"text": "smartphone app", "type": "IntellectualProduct"}, {"text": "diet ,", "type": "Food"}]}

Example input:
Sentence: Wide methodological variability was seen , particularly related to key factors in the cognitive data capture and image analysis techniques .

Example answer:
{"entities": [{"text": "image analysis techniques", "type": "HealthCareActivity"}]}

Example input:
Sentence: The most important behavioral factors identified are physical activity , nutrition / food intake and substance consumption : coffee , alcohol , cigarettes .

Example answer:
{"entities": [{"text": "nutrition", "type": "BiologicFunction"}, {"text": "food intake", "type": "BiologicFunction"}, {"text": "consumption", "type": "BiologicFunction"}, {"text": "coffee", "type": "Food"}, {"text": "alcohol", "type": "Food"}]}

Example input:
Sentence: For potential consumers , the findings showed that behavioral determinants , behavioral intentions , and mavenism predicted intentions to persuade others .

Example answer:
{"entities": [{"text": "consumers", "type": "PopulationGroup"}, {"text": "findings", "type": "Finding"}, {"text": "intentions", "type": "BiologicFunction"}]}

Example input:
Sentence: Knowledge changes were more affected by participant characteristics in the application group .

Example answer:
{"entities": [{"text": "Knowledge", "type": "IntellectualProduct"}, {"text": "participant", "type": "PopulationGroup"}, {"text": "application group", "type": "PopulationGroup"}]}

Example input:
Sentence: Of these variables , stop - signal reaction times and Barratt attentional impulsiveness were the strongest predictors of group classification .

Example answer:
{"entities": [{"text": "Barratt attentional impulsiveness", "type": "IntellectualProduct"}, {"text": "classification", "type": "IntellectualProduct"}]}

Example input:
Sentence: Furthermore , while both groups showed higher information needs satisfaction after the intervention , the application group was significantly more satisfied .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "application group", "type": "PopulationGroup"}]}

Example input:
Sentence: This study demonstrates that distinct subgroups can be identified in " messy " commercial app data and the identified subgroups can be replicated in independent samples .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "subgroups", "type": "IntellectualProduct"}, {"text": "commercial app", "type": "IntellectualProduct"}]}

Example input:
Sentence: Behavioral factors delineated the subgroups , though app -related behavioral characteristics further distinguished them .

Example answer:
{"entities": [{"text": "subgroups", "type": "IntellectualProduct"}, {"text": "app", "type": "IntellectualProduct"}]}

Input:
Sentence: Behavioral factors and use of custom app features characterized the subgroups .

## Item MedMentions:test:272
Example input:
Sentence: Boosting a Drug 's Market Share Can Cross a Dangerous Line Hub programs have emerged as a profitable new line of business in the sales and distribution side of the pharmaceutical industry that has got more than its fair share of wheeling and dealing . But they spell trouble if they spark collusion , threaten patients , or waste federal dollars .

Example answer:
{"entities": [{"text": "Drug 's", "type": "Chemical"}, {"text": "pharmaceutical industry", "type": "Organization"}, {"text": "federal", "type": "Organization"}]}

Example input:
Sentence: Injuries are largely preventable ; as such , targeted efforts are needed to decrease the burden of injury - related disability and death among PLHIV .

Example answer:
{"entities": [{"text": "Injuries", "type": "InjuryOrPoisoning"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "disability", "type": "Finding"}, {"text": "death", "type": "Finding"}, {"text": "PLHIV", "type": "BiologicFunction"}]}

Example input:
Sentence: Recognising and responding to ' cutting corners ' when providing nursing care : a qualitative study The aim of this study is to report on a key finding of a larger study investigating the ' gaps ' in patient care that registered nurses encounter during the course of their practice .

Example answer:
{"entities": [{"text": "Recognising", "type": "BiologicFunction"}, {"text": "responding", "type": "BiologicFunction"}, {"text": "nursing care", "type": "HealthCareActivity"}, {"text": "qualitative study", "type": "ResearchActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "finding", "type": "Finding"}, {"text": "larger study", "type": "ResearchActivity"}, {"text": "gaps", "type": "SpatialConcept"}, {"text": "patient care", "type": "HealthCareActivity"}, {"text": "registered nurses", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Corners were cut in patient assessment , essential nursing care , the care of central venous catheters and medication administration .

Example answer:
{"entities": [{"text": "assessment", "type": "HealthCareActivity"}, {"text": "nursing care", "type": "HealthCareActivity"}, {"text": "care of central venous catheters", "type": "HealthCareActivity"}, {"text": "medication administration", "type": "HealthCareActivity"}]}

Example input:
Sentence: Further research and inquiry are needed to deepen understanding of cutting corners and its impact on patient safety .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "patient safety", "type": "HealthCareActivity"}]}

Example input:
Sentence: Identifying the nature and implications of cutting corners when providing nursing care is an important contributing factor to improving patient safety and quality care .

Example answer:
{"entities": [{"text": "implications", "type": "Finding"}, {"text": "nursing care", "type": "HealthCareActivity"}, {"text": "patient safety", "type": "HealthCareActivity"}, {"text": "quality care", "type": "HealthCareActivity"}]}

Example input:
Sentence: A key finding of this larger study was that ' cutting corners ' was a gap discerned by nurses . ' Cutting corners ' has been characterised as a ' violation ' and threat to patient safety , although there is a paucity of research on this issue .

Example answer:
{"entities": [{"text": "finding", "type": "Finding"}, {"text": "larger study", "type": "ResearchActivity"}, {"text": "gap", "type": "SpatialConcept"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "patient safety", "type": "HealthCareActivity"}, {"text": "research", "type": "ResearchActivity"}]}

Example input:
Sentence: The findings of the study raise the possibility that cutting corners is a salient but underinvestigated characteristic of nursing practice .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "study", "type": "ResearchActivity"}, {"text": "nursing practice", "type": "HealthCareActivity"}]}

Example input:
Sentence: Cutting corners was a common practice that encompassed ( 1 ) the partial or complete omission of patient care , ( 2 ) delays in providing care and ( 3 ) the failure to do things correctly .

Example answer:
{"entities": [{"text": "patient care", "type": "HealthCareActivity"}, {"text": "providing care", "type": "HealthCareActivity"}]}

Example input:
Sentence: The study found that cutting corners created gaps that contributed to unfinished nursing care and preventable adverse events .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "gaps", "type": "SpatialConcept"}, {"text": "nursing care", "type": "HealthCareActivity"}, {"text": "preventable", "type": "Finding"}, {"text": "adverse events", "type": "BiologicFunction"}]}

Input:
Sentence: The practice of cutting corners was perceived as contributing to preventable adverse events .

## Item MedMentions:test:222
Example input:
Sentence: Observational cross sectional study of one hundred and fifty five patients with end stage kidney disease recruited from a regional Australian renal unit .

Example answer:
{"entities": [{"text": "Observational", "type": "ResearchActivity"}, {"text": "cross sectional study", "type": "ResearchActivity"}, {"text": "end stage kidney disease", "type": "BiologicFunction"}]}

Example input:
Sentence: We retrospectively analyzed the data of 623 patients who underwent radical nephrouretectomy for UTUC .

Example answer:
{"entities": [{"text": "retrospectively analyzed", "type": "ResearchActivity"}, {"text": "radical nephrouretectomy", "type": "HealthCareActivity"}, {"text": "UTUC", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , we report a case of a 41 - year - old female patient who had a late diagnosis of 2 , 8 - dihydroxyadenine nephropathy -induced end - stage renal disease , made on the native nephrectomy that accompanied the renal transplant , and who had a timely intervention that prevented recurrence in the graft .

Example answer:
{"entities": [{"text": "2 , 8 - dihydroxyadenine", "type": "Chemical"}, {"text": "nephropathy", "type": "BiologicFunction"}, {"text": "end - stage renal disease", "type": "BiologicFunction"}, {"text": "nephrectomy", "type": "HealthCareActivity"}, {"text": "renal transplant", "type": "HealthCareActivity"}, {"text": "recurrence", "type": "BiologicFunction"}, {"text": "graft", "type": "HealthCareActivity"}]}

Example input:
Sentence: Kidney transplant recipients after nonrenal solid organ transplantation show low alloreactivity but an increased risk of infection The number of kidney transplant recipients ( KTRs ) after nonrenal solid organ transplantation ( SOT ) has increased to almost 5 % .

Example answer:
{"entities": [{"text": "Kidney transplant recipients", "type": "Finding"}, {"text": "nonrenal solid organ transplantation", "type": "HealthCareActivity"}, {"text": "alloreactivity", "type": "BiologicFunction"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "kidney transplant recipients", "type": "Finding"}, {"text": "KTRs", "type": "Finding"}, {"text": "SOT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Of 413 patients enrolled , 266 ( 64 . 4 % ) , 101 ( 24 . 5 % ) , 40 ( 9 . 6 % ) , and 6 ( 1 . 5 % ) had chronic kidney disease ( CKD ) stages 1 , 2 , 3 , and 4 , respectively .

Example answer:
{"entities": [{"text": "chronic kidney disease ( CKD ) stages 1", "type": "BiologicFunction"}, {"text": "2", "type": "BiologicFunction"}, {"text": "3", "type": "BiologicFunction"}, {"text": "4", "type": "BiologicFunction"}]}

Example input:
Sentence: Cohort comprised CT - DXA pairs within a 6 - month period performed for any indication on 326 consecutive adults , aged 62 . 4 ± 12 .

Example answer:
{"entities": [{"text": "Cohort", "type": "PopulationGroup"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "DXA", "type": "HealthCareActivity"}]}

Example input:
Sentence: Among 8 , 675 patients who started dialysis in 2007 and who survived until January 1 , 2010 , listed in the Renal Data Registry of the Japanese Society for Dialysis Therapy , 5 , 365 VDRA users were matched to 3 , 203 non - users based on clinically relevant variables at the end of 2009 using the coarsened exact matching procedure .

Example answer:
{"entities": [{"text": "dialysis", "type": "HealthCareActivity"}, {"text": "Renal Data Registry", "type": "ResearchActivity"}, {"text": "Japanese Society", "type": "Organization"}, {"text": "Dialysis Therapy", "type": "HealthCareActivity"}, {"text": "VDRA", "type": "Chemical"}, {"text": "coarsened exact matching procedure", "type": "IntellectualProduct"}]}

Example input:
Sentence: During the first 48 months of the change journey ( 2012 through 2015 ) , 498 organ donors ( +44 . 8 % ) provided 1 , 536 organs transplanted ( +52 . 5 % ) .

Example answer:
{"entities": [{"text": "organ donors", "type": "PopulationGroup"}, {"text": "organs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We studied 30 , 598 adult recipients of lung transplants performed between 1999 and 2011 .

Example answer:
{"entities": [{"text": "studied", "type": "ResearchActivity"}, {"text": "recipients", "type": "PopulationGroup"}, {"text": "lung transplants", "type": "HealthCareActivity"}]}

Example input:
Sentence: We retrospectively studied kidney injury in 186 lung - transplantation patients at the UMC Utrecht between 2001 and 2011 .

Example answer:
{"entities": [{"text": "retrospectively studied", "type": "ResearchActivity"}, {"text": "kidney injury", "type": "InjuryOrPoisoning"}, {"text": "lung - transplantation", "type": "HealthCareActivity"}, {"text": "UMC Utrecht", "type": "Organization"}]}

Input:
Sentence: The retrospective cohort included 163 636 adults listed for kidney transplant before December 31 , 2011 .

## Item MedMentions:test:405
Example input:
Sentence: Aortic transprosthetic mean pressure gradient increased more notably in woman and was associated with late TR ( odds ratio 1 .

Example answer:
{"entities": [{"text": "Aortic", "type": "AnatomicalStructure"}, {"text": "transprosthetic mean pressure gradient", "type": "Finding"}, {"text": "woman", "type": "PopulationGroup"}, {"text": "TR", "type": "BiologicFunction"}]}

Example input:
Sentence: E - WIN Project 2016 : Evaluating the current gender situation in neurosurgery across Europe .

Example answer:
{"entities": [{"text": "neurosurgery", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Europe", "type": "SpatialConcept"}]}

Example input:
Sentence: An interactive , multiple - level Survey The proportion of females among neurosurgeons appears to be growing worldwide with time .

Example answer:
{"entities": [{"text": "multiple - level Survey", "type": "ResearchActivity"}, {"text": "females", "type": "PopulationGroup"}, {"text": "neurosurgeons", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: In the Western trial ( SYNTAX ) , female sex favored coronary artery bypass graft compared with percutaneous coronary intervention ( hazard ratio ( percutaneous coronary intervention ) 2 . 213 ; 95 % confidence interval , 1 . 242 - 3 . 943 ; P = 0 . 007 ) , whereas in the Asian women ( PRECOMBAT and BEST ) , the treatment effect was neutral between both strategies .

Example answer:
{"entities": [{"text": "Western", "type": "PopulationGroup"}, {"text": "trial", "type": "ResearchActivity"}, {"text": "SYNTAX", "type": "HealthCareActivity"}, {"text": "female", "type": "PopulationGroup"}, {"text": "sex", "type": "BiologicFunction"}, {"text": "coronary artery bypass graft", "type": "HealthCareActivity"}, {"text": "percutaneous coronary intervention", "type": "HealthCareActivity"}, {"text": "Asian", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "PRECOMBAT", "type": "HealthCareActivity"}, {"text": "BEST", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "strategies", "type": "HealthCareActivity"}]}

Example input:
Sentence: As academic aspirations and advancement depend largely on research productivity , the authors assessed the number of articles authored by women published in the journal Plastic and Reconstructive Surgery .

Example answer:
{"entities": [{"text": "academic", "type": "Organization"}, {"text": "aspirations", "type": "BiologicFunction"}, {"text": "research", "type": "ResearchActivity"}, {"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "articles", "type": "IntellectualProduct"}, {"text": "women", "type": "PopulationGroup"}, {"text": "journal Plastic and Reconstructive Surgery", "type": "IntellectualProduct"}]}

Example input:
Sentence: As a field , plastic surgery had fewer female authors than other medical specialties including pediatrics , obstetrics and gynecology , general surgery , internal medicine , and radiation oncology ( p < 0 .

Example answer:
{"entities": [{"text": "plastic surgery", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "medical specialties", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "pediatrics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "obstetrics and gynecology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "general surgery", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "internal medicine", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "radiation oncology", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Over the same time period , the percentage of female plastic surgery residents increased from 2 . 6 percent to 32 . 5 percent .

Example answer:
{"entities": [{"text": "plastic surgery", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: The increase in representation of female authors in plastic surgery is encouraging but lags behind advances in other specialties .

Example answer:
{"entities": [{"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "plastic surgery", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "specialties", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Findings were placed in the context of gender trends among plastic surgery residents in the United States .

Example answer:
{"entities": [{"text": "plastic surgery", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "United States", "type": "SpatialConcept"}]}

Example input:
Sentence: Gender Authorship Trends of Plastic Surgery Research in the United States An increasing number of women are entering the medical profession , but plastic surgery remains a male - dominated profession , especially within academia .

Example answer:
{"entities": [{"text": "Plastic Surgery", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Research", "type": "ResearchActivity"}, {"text": "United States", "type": "SpatialConcept"}, {"text": "women", "type": "PopulationGroup"}, {"text": "plastic surgery", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "academia", "type": "Organization"}]}

Input:
Sentence: Understanding reasons for these trends may help improve gender equity in academic plastic surgery .

## Item MedMentions:test:343
Example input:
Sentence: There was a positive trend of increased toxicity followed by reduced life history traits such as fecundity , brood size and time to first brood and intrinsic rate of population increase and body growth ( length and area ) of C .

Example answer:
{"entities": [{"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "fecundity", "type": "BiologicFunction"}, {"text": "size", "type": "SpatialConcept"}, {"text": "population", "type": "PopulationGroup"}, {"text": "body growth", "type": "BiologicFunction"}, {"text": "area", "type": "SpatialConcept"}, {"text": "C .", "type": "Eukaryote"}]}

Example input:
Sentence: This study also points out the complexity of using yield as a measure of O3 impact across different environments with the snap bean system , whereas visible foliar injury is more consistently related to O3 effects .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "O3", "type": "Chemical"}, {"text": "environments", "type": "SpatialConcept"}, {"text": "snap bean", "type": "Eukaryote"}, {"text": "foliar injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: We found that both a deficiency and a strong excess of UPF3 expression are detrimental to plant resistance to salt stress .

Example answer:
{"entities": [{"text": "UPF3 expression", "type": "BiologicFunction"}, {"text": "plant resistance", "type": "BiologicFunction"}, {"text": "salt stress", "type": "BiologicFunction"}]}

Example input:
Sentence: We confirmed that the photosynthetic capacity and chlorophyll content was reduced by an ethylene treatment and that several abiotic stress conditions could stimulate cell elongation in an ethylene -dependent manner .

Example answer:
{"entities": [{"text": "chlorophyll", "type": "Chemical"}, {"text": "ethylene", "type": "Chemical"}, {"text": "abiotic stress conditions", "type": "BiologicFunction"}, {"text": "stimulate", "type": "HealthCareActivity"}, {"text": "cell elongation", "type": "BiologicFunction"}]}

Example input:
Sentence: By testing the role of ambient air temperature in outdoor plant environment chambers ( OPECs ) , it was found that increased temperature limits mature pod formation and complicates interpretation of O3 impacts in terms of S156 / R123 yields ratios .

Example answer:
{"entities": [{"text": "pod", "type": "Eukaryote"}, {"text": "O3", "type": "Chemical"}]}

Example input:
Sentence: This study assessed how sequential stressors affect the sensory and quality characteristics of catfish ( Ictalurus punctatus ) fillets .

Example answer:
{"entities": [{"text": "catfish", "type": "Eukaryote"}, {"text": "Ictalurus punctatus", "type": "Eukaryote"}, {"text": "fillets", "type": "Food"}]}

Example input:
Sentence: Fillets from the severe stress treatment ( 33 ° C , approximately 2 . 5 mg / L ) received the highest acceptability scores ( P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "Fillets", "type": "Food"}, {"text": "stress treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: As fish progressed through the harvest event , cook loss decreased , tenderness increased , and pH increased , indicating that stress induced textural changes .

Example answer:
{"entities": []}

Example input:
Sentence: The Effects of Sequential Environmental and Harvest Stressors on the Sensory Characteristics of Cultured Channel Catfish ( Ictalurus Punctatus ) Fillets Stress during fish culture alters physiological homeostasis and affects fillet quality .

Example answer:
{"entities": [{"text": "Cultured Channel Catfish", "type": "Eukaryote"}, {"text": "Ictalurus Punctatus", "type": "Eukaryote"}, {"text": "Fillets", "type": "Food"}, {"text": "Stress", "type": "Finding"}, {"text": "fish culture", "type": "Organization"}, {"text": "physiological homeostasis", "type": "BiologicFunction"}, {"text": "fillet", "type": "Food"}]}

Example input:
Sentence: After each stage of harvest ( environmental stress , socking , and transport ) , fillet yield , consumer acceptability , descriptive evaluation , cook loss , tenderness , and pH were evaluated .

Example answer:
{"entities": [{"text": "fillet", "type": "Food"}, {"text": "consumer", "type": "PopulationGroup"}]}

Input:
Sentence: Fillet yield decreased with increasing severity of environmental stress .

## Item MedMentions:test:253
Example input:
Sentence: Generally , lesions are present in the descending part of the duodenum in an annular pancreas , and the pancreatic and bile ducts join in the papillary region .

Example answer:
{"entities": [{"text": "lesions", "type": "Finding"}, {"text": "descending part of the duodenum", "type": "AnatomicalStructure"}, {"text": "annular pancreas", "type": "AnatomicalStructure"}, {"text": "pancreatic", "type": "AnatomicalStructure"}, {"text": "bile ducts", "type": "AnatomicalStructure"}, {"text": "papillary region", "type": "SpatialConcept"}]}

Example input:
Sentence: It was considered that the pancreatic and bile ducts separately opened into the pyloric ring .

Example answer:
{"entities": [{"text": "pancreatic", "type": "AnatomicalStructure"}, {"text": "bile ducts", "type": "AnatomicalStructure"}, {"text": "opened", "type": "SpatialConcept"}, {"text": "pyloric ring", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In 2012 the patient underwent percutaneous transhepatic biliary drainage for bile duct stricture , complicated with acute pancreatitis .

Example answer:
{"entities": [{"text": "percutaneous transhepatic biliary drainage", "type": "HealthCareActivity"}, {"text": "bile duct stricture", "type": "BiologicFunction"}, {"text": "acute pancreatitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Intraductal papillary neoplasm of the bile duct : a case report Intraductal papillary neoplasm of the bile duct ( IPNB ) is a rare variant of bile duct tumors , characterized by papillary growth within the bile duct lumen and is regarded as a biliary counterpart of intraductal papillary mucinous neoplasm ( IPMN ) of the pancreas .

Example answer:
{"entities": [{"text": "Intraductal papillary neoplasm", "type": "BiologicFunction"}, {"text": "bile duct", "type": "AnatomicalStructure"}, {"text": "case report", "type": "IntellectualProduct"}, {"text": "IPNB", "type": "BiologicFunction"}, {"text": "bile duct tumors", "type": "BiologicFunction"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "bile duct lumen", "type": "SpatialConcept"}, {"text": "intraductal papillary mucinous neoplasm", "type": "BiologicFunction"}, {"text": "IPMN", "type": "BiologicFunction"}, {"text": "pancreas", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The branching pattern of the right hepatic duct ( RHD ) was typical in 55 .

Example answer:
{"entities": [{"text": "branching pattern", "type": "SpatialConcept"}, {"text": "right hepatic duct", "type": "SpatialConcept"}, {"text": "RHD", "type": "SpatialConcept"}]}

Example input:
Sentence: Interlobar and intralobar histological variability is present in chronic BRHP .

Example answer:
{"entities": [{"text": "Interlobar", "type": "SpatialConcept"}, {"text": "BRHP", "type": "BiologicFunction"}]}

Example input:
Sentence: The purpose of our study was to demonstrate the imaging features of various anatomical variants of IHD using magnetic resonance cholangio - pancreatography ( MRCP ) and their prevalence in our population .

Example answer:
{"entities": [{"text": "anatomical variants", "type": "AnatomicalStructure"}, {"text": "IHD", "type": "AnatomicalStructure"}, {"text": "magnetic resonance cholangio - pancreatography", "type": "HealthCareActivity"}, {"text": "MRCP", "type": "HealthCareActivity"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: The most common variant was right posterior sectoral duct ( RPSD ) draining into the left hepatic duct ( LHD ) in 27 . 6 % of subjects .

Example answer:
{"entities": [{"text": "variant", "type": "AnatomicalStructure"}, {"text": "right posterior sectoral duct", "type": "AnatomicalStructure"}, {"text": "RPSD", "type": "AnatomicalStructure"}, {"text": "left hepatic duct", "type": "AnatomicalStructure"}, {"text": "LHD", "type": "AnatomicalStructure"}, {"text": "subjects", "type": "PopulationGroup"}]}

Example input:
Sentence: She was admitted for a diagnosis of acute cholecystitis , and severe intra - and extrahepatic bile duct dilatation with inner air density was noted .

Example answer:
{"entities": [{"text": "admitted", "type": "HealthCareActivity"}, {"text": "diagnosis", "type": "Finding"}, {"text": "acute cholecystitis", "type": "BiologicFunction"}, {"text": "intra", "type": "AnatomicalStructure"}, {"text": "extrahepatic bile duct", "type": "AnatomicalStructure"}, {"text": "dilatation", "type": "BiologicFunction"}, {"text": "inner", "type": "SpatialConcept"}]}

Example input:
Sentence: Common and Uncommon Anatomical Variants of Intrahepatic Bile Ducts in Magnetic Resonance Cholangiopancreatography and its Clinical Implication Preoperative knowledge of intrahepatic bile duct ( IHD ) anatomy is critical for planning liver resections , liver transplantations and complex biliary reconstructive surgery .

Example answer:
{"entities": [{"text": "Anatomical Variants", "type": "AnatomicalStructure"}, {"text": "Intrahepatic Bile Ducts", "type": "AnatomicalStructure"}, {"text": "Magnetic Resonance Cholangiopancreatography", "type": "HealthCareActivity"}, {"text": "Clinical Implication", "type": "Finding"}, {"text": "intrahepatic bile duct", "type": "AnatomicalStructure"}, {"text": "IHD", "type": "AnatomicalStructure"}, {"text": "anatomy", "type": "AnatomicalStructure"}, {"text": "liver resections", "type": "HealthCareActivity"}, {"text": "liver transplantations", "type": "HealthCareActivity"}, {"text": "complex biliary reconstructive surgery", "type": "HealthCareActivity"}]}

Input:
Sentence: Intrahepatic bile duct anatomy is complex with many common and uncommon variations .

## Item MedMentions:test:496
Example input:
Sentence: The highest yields of DCAN and DCAcAm appeared when the Cl2 / Asp molar ratio was about 20 , the yield of TCNM increased with increasing the Cl2 / Asp molar ratio from 5 to 30 and TCNM was not produced when the ratio was less than 5 .

Example answer:
{"entities": [{"text": "DCAN", "type": "Chemical"}, {"text": "DCAcAm", "type": "Chemical"}, {"text": "Cl2", "type": "Chemical"}, {"text": "Asp", "type": "Chemical"}, {"text": "TCNM", "type": "Chemical"}]}

Example input:
Sentence: In this cohort , a diagnostic yield of 73 .

Example answer:
{"entities": [{"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: The extraction was promoted by agitation at 900 rpm and was carried out for 120min .

Example answer:
{"entities": [{"text": "extraction", "type": "HealthCareActivity"}]}

Example input:
Sentence: Recoveries ranged from 53 to 78 % ( THC ) , 57 to 66 % ( 11 - OH - THC ) and 62 to 65 % ( THC - COOH ) , allowing the limits of detection and quantification to be set at 0 .

Example answer:
{"entities": [{"text": "THC", "type": "Chemical"}, {"text": "11 - OH - THC", "type": "Chemical"}, {"text": "THC - COOH", "type": "Chemical"}, {"text": "detection", "type": "HealthCareActivity"}]}

Example input:
Sentence: The yield of WBP was 7 .

Example answer:
{"entities": [{"text": "WBP", "type": "Chemical"}]}

Example input:
Sentence: The spot - number order obtained via 2DE mapping was as follows : phenol extraction ( 655 ) > TCA / acetone extraction ( 589 ) > TCA / acetone / phenol extraction ( 545 ) .

Example answer:
{"entities": [{"text": "2DE mapping", "type": "HealthCareActivity"}, {"text": "phenol", "type": "Chemical"}, {"text": "extraction", "type": "HealthCareActivity"}, {"text": "TCA", "type": "Chemical"}, {"text": "acetone", "type": "Chemical"}]}

Example input:
Sentence: The overall diagnostic yield of SBB was 88 % .

Example answer:
{"entities": [{"text": "diagnostic yield", "type": "Finding"}, {"text": "SBB", "type": "HealthCareActivity"}]}

Example input:
Sentence: Crude extract was obtained by enzymatic digestion and isolated by ion exchange chromatography on DEAE - cellulose .

Example answer:
{"entities": [{"text": "enzymatic digestion", "type": "HealthCareActivity"}, {"text": "ion exchange chromatography", "type": "HealthCareActivity"}, {"text": "DEAE - cellulose", "type": "Chemical"}]}

Example input:
Sentence: However , phenol extraction produced a better 2DE map with greater resolution between spots , and TCA / acetone extraction produced higher protein yields .

Example answer:
{"entities": [{"text": "phenol", "type": "Chemical"}, {"text": "extraction", "type": "HealthCareActivity"}, {"text": "2DE map", "type": "HealthCareActivity"}, {"text": "TCA", "type": "Chemical"}, {"text": "acetone", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}]}

Example input:
Sentence: Then , the percent yield of essential oil from the leaves and shoots was 2 . 45 % ( w / w ) , which includes 50 compounds .

Example answer:
{"entities": [{"text": "essential oil", "type": "Chemical"}, {"text": "leaves", "type": "Eukaryote"}, {"text": "shoots", "type": "Eukaryote"}]}

Input:
Sentence: Extract yield was found to be 4 . 59 % - 7 .

## Item MedMentions:test:62
Example input:
Sentence: coli strains and concentrations , dissolving agents , salinity and pH effects , quality of substrates of various suppliers of 4 - methylumbelliferyl glucuronide ( MUG ) , and environmental water samples were included in the QA / QC plan and used in the assay optimization and documentation .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "dissolving agents", "type": "Chemical"}, {"text": "salinity", "type": "Finding"}, {"text": "suppliers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "4 - methylumbelliferyl glucuronide", "type": "Chemical"}, {"text": "MUG", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "documentation", "type": "IntellectualProduct"}]}

Example input:
Sentence: Succinic acid production by immobilized cultures using spent sulphite liquor as fermentation medium Spent sulphite liquor ( SSL ) was used as carbon source for the production of succinic acid using immobilized cultures of Actinobacillus succinogenes and Basfia succiniciproducens on two different supports , delignified cellulosic material ( DCM ) and alginate beads .

Example answer:
{"entities": [{"text": "Succinic acid", "type": "Chemical"}, {"text": "immobilized", "type": "AnatomicalStructure"}, {"text": "cultures", "type": "HealthCareActivity"}, {"text": "fermentation", "type": "BiologicFunction"}, {"text": "Spent sulphite liquor", "type": "Chemical"}, {"text": "SSL", "type": "Chemical"}, {"text": "carbon", "type": "Chemical"}, {"text": "source", "type": "Finding"}, {"text": "succinic acid", "type": "Chemical"}, {"text": "Actinobacillus succinogenes", "type": "Bacterium"}, {"text": "Basfia succiniciproducens", "type": "Bacterium"}, {"text": "alginate", "type": "Chemical"}]}

Example input:
Sentence: Tracking the relative concentration between Bacteroidales DNA markers and culturable Escherichia coli in fecally polluted subtropical seawater : potential use in differentiating fresh and aged pollution Routine water quality monitoring practices based on the enumeration of culturable Escherichia coli provides no information about the source or age of fecal pollution .

Example answer:
{"entities": [{"text": "Tracking", "type": "SpatialConcept"}, {"text": "Bacteroidales", "type": "Bacterium"}, {"text": "DNA markers", "type": "SpatialConcept"}, {"text": "culturable", "type": "HealthCareActivity"}, {"text": "Escherichia coli", "type": "Bacterium"}, {"text": "fecally", "type": "BodySubstance"}, {"text": "no information", "type": "Finding"}, {"text": "source", "type": "Finding"}, {"text": "fecal", "type": "BodySubstance"}]}

Example input:
Sentence: coli expressing recombinant SGEH .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "recombinant SGEH", "type": "Chemical"}]}

Example input:
Sentence: coli ATCC 25922 and S .

Example answer:
{"entities": [{"text": "coli ATCC 25922", "type": "Bacterium"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: coli , Pseudomonas aeruginosa , Proteus mirabilis , Streptococcus agalactiae , Staphylococcus saprophyticus and Enterococcus faecalis were undertaken using viable bacterial count and optical density measurements over a 48h culture period .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "Pseudomonas aeruginosa", "type": "Bacterium"}, {"text": "Proteus mirabilis", "type": "Bacterium"}, {"text": "Streptococcus agalactiae", "type": "Bacterium"}, {"text": "Staphylococcus saprophyticus", "type": "Bacterium"}, {"text": "Enterococcus faecalis", "type": "Bacterium"}, {"text": "bacterial count", "type": "HealthCareActivity"}, {"text": "optical density measurements", "type": "HealthCareActivity"}, {"text": "culture", "type": "HealthCareActivity"}]}

Example input:
Sentence: coli K - 12 , a classical non - environmental strain , constitutes a model of phenotypic plasticity for adaptation to a redox - cycling herbicide through redundancy of different isoforms of SOD and CAT enzymes .

Example answer:
{"entities": [{"text": "coli K - 12", "type": "Bacterium"}, {"text": "strain", "type": "Bacterium"}, {"text": "adaptation", "type": "BiologicFunction"}, {"text": "redox - cycling", "type": "BiologicFunction"}, {"text": "herbicide", "type": "Chemical"}, {"text": "isoforms", "type": "Chemical"}, {"text": "SOD", "type": "Chemical"}, {"text": "CAT enzymes", "type": "Chemical"}]}

Example input:
Sentence: Finally , contamination free cultures were obtained when streptocycline ( 100 μg / ml ) and gentamicin sulphate ( 75 μg / ml ) were added into the medium .

Example answer:
{"entities": [{"text": "cultures", "type": "HealthCareActivity"}, {"text": "streptocycline", "type": "Chemical"}, {"text": "gentamicin sulphate", "type": "Chemical"}]}

Example input:
Sentence: coli can grow in human urine as a means to maintain colonization during infections .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "human", "type": "Eukaryote"}, {"text": "urine", "type": "BodySubstance"}, {"text": "colonization", "type": "Finding"}, {"text": "infections", "type": "BiologicFunction"}]}

Example input:
Sentence: coli altered the antibiotic production pattern and undecylprodigiosin production was enhanced by 3 . 5 - fold compared to the pure cultures of S .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "antibiotic", "type": "Chemical"}, {"text": "undecylprodigiosin", "type": "Chemical"}, {"text": "pure cultures", "type": "HealthCareActivity"}, {"text": "S .", "type": "Bacterium"}]}

Input:
Sentence: coli culture to S .

## Item MedMentions:test:138
Example input:
Sentence: Long - term viral suppression with nucleoside analogues leads to HBsAg loss in a substantial proportion of patients , particularly if HBeAg - negative .

Example answer:
{"entities": [{"text": "viral", "type": "Virus"}, {"text": "suppression", "type": "HealthCareActivity"}, {"text": "nucleoside analogues", "type": "Chemical"}, {"text": "HBsAg", "type": "Chemical"}, {"text": "HBeAg - negative", "type": "Finding"}]}

Example input:
Sentence: DNA and dsRNA viruses were considerably more resistant than ssRNA viruses , resulting in up to 1 , 000 - fold - longer treatment times to reach a 4 - log inactivation .

Example answer:
{"entities": [{"text": "DNA", "type": "Chemical"}, {"text": "dsRNA", "type": "Chemical"}, {"text": "viruses", "type": "Virus"}, {"text": "ssRNA viruses", "type": "Virus"}]}

Example input:
Sentence: Pushing the system toward harsher pH ( > 9 ) and temperature ( > 35°C ) conditions , such as those encountered in thermophilic digestion and alkaline treatments , led to more consistent inactivation kinetics among ssRNA and other viruses .

Example answer:
{"entities": [{"text": "digestion", "type": "BiologicFunction"}, {"text": "ssRNA", "type": "Chemical"}, {"text": "viruses", "type": "Virus"}]}

Example input:
Sentence: Overall , this study allows us to better understand the behavior of viruses in HEAM .

Example answer:
{"entities": [{"text": "viruses", "type": "Virus"}, {"text": "HEAM", "type": "BodySubstance"}]}

Example input:
Sentence: The goals were to characterize the influence of HEAM solution conditions on inactivation and to determine the potential mechanisms involved .

Example answer:
{"entities": [{"text": "HEAM", "type": "BodySubstance"}]}

Example input:
Sentence: In contrast , the other genome types are more stable ; therefore , inactivation is slower and mainly driven by the degradation of viral proteins .

Example answer:
{"entities": [{"text": "genome types", "type": "AnatomicalStructure"}, {"text": "viral proteins", "type": "Chemical"}]}

Example input:
Sentence: This suggests that the dependence of inactivation on genome type disappeared in favor of protein -mediated inactivation mechanisms common to all viruses .

Example answer:
{"entities": [{"text": "genome type", "type": "AnatomicalStructure"}, {"text": "protein", "type": "Chemical"}, {"text": "viruses", "type": "Virus"}]}

Example input:
Sentence: Ammonia as an In Situ Sanitizer : Influence of Virus Genome Type on Inactivation Treatment of human excreta and animal manure ( HEAM ) is key in controlling the spread of persistent enteric pathogens , such as viruses .

Example answer:
{"entities": [{"text": "Ammonia", "type": "Chemical"}, {"text": "In Situ", "type": "SpatialConcept"}, {"text": "Virus", "type": "Virus"}, {"text": "Genome Type", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "excreta", "type": "BodySubstance"}, {"text": "animal", "type": "Eukaryote"}, {"text": "HEAM", "type": "BodySubstance"}, {"text": "enteric", "type": "SpatialConcept"}, {"text": "viruses", "type": "Virus"}]}

Example input:
Sentence: The apparently slower inactivation of DNA viruses was rationalized by the higher stability of DNA than that of ssRNA in HEAM .

Example answer:
{"entities": [{"text": "DNA viruses", "type": "Virus"}, {"text": "stability", "type": "HealthCareActivity"}, {"text": "DNA", "type": "Chemical"}, {"text": "ssRNA", "type": "Chemical"}, {"text": "HEAM", "type": "BodySubstance"}]}

Example input:
Sentence: Here , we investigated the inactivation of viruses of different genome types under conditions representative of HEAM storage or mesophilic digestion .

Example answer:
{"entities": [{"text": "viruses", "type": "Virus"}, {"text": "genome types", "type": "AnatomicalStructure"}, {"text": "HEAM", "type": "BodySubstance"}, {"text": "digestion", "type": "BiologicFunction"}]}

Input:
Sentence: The extent of virus inactivation during HEAM storage and treatment appears to vary with virus genome type , although the reasons for this variability are not clear .

## Item MedMentions:test:196
Example input:
Sentence: Within a larger global phylogenomic framework , Bayesian modelling suggested that this NZ clade emerged in the late 2000s , with a probable origin in swine from Western Europe .

Example answer:
{"entities": [{"text": "NZ", "type": "SpatialConcept"}, {"text": "clade", "type": "Bacterium"}, {"text": "swine", "type": "Eukaryote"}, {"text": "Western Europe", "type": "SpatialConcept"}]}

Example input:
Sentence: Three CRF35 _ AD sequences from Afghan refugees living in Pakistan nested among Afghan and Iranian CRF35 _ AD branches .

Example answer:
{"entities": [{"text": "sequences", "type": "SpatialConcept"}, {"text": "Afghan", "type": "SpatialConcept"}, {"text": "refugees", "type": "PopulationGroup"}, {"text": "living in", "type": "SpatialConcept"}, {"text": "Pakistan", "type": "SpatialConcept"}, {"text": "Iranian", "type": "SpatialConcept"}]}

Example input:
Sentence: On the post - glacial spread of human commensal Arabidopsis thaliana Recent work has shown that Arabidopsis thaliana contains genetic groups originating from different ice age refugia , with one particular group comprising over 95 % of the current worldwide population .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "Arabidopsis thaliana", "type": "Eukaryote"}]}

Example input:
Sentence: However , these studies have largely ignored three enigmatic genera because of scarce DNA source material and limited overlapping phylogenetic data : blood pheasants ( Ithaginis ) , snow partridges ( Lerwa ) , and long - billed partridges ( Rhizothera ) .

Example answer:
{"entities": [{"text": "DNA", "type": "Chemical"}, {"text": "source material", "type": "Finding"}, {"text": "phylogenetic data", "type": "IntellectualProduct"}, {"text": "blood pheasants", "type": "Eukaryote"}, {"text": "Ithaginis", "type": "Eukaryote"}, {"text": "snow partridges", "type": "Eukaryote"}, {"text": "Lerwa", "type": "Eukaryote"}, {"text": "long - billed partridges", "type": "Eukaryote"}, {"text": "Rhizothera", "type": "Eukaryote"}]}

Example input:
Sentence: Potential factors contributing to viral exchange between Afghanistan and Iran could be injection drug networks and mass migration of Afghan refugees and labours to Iran , which calls for extensive preventive efforts .

Example answer:
{"entities": [{"text": "viral", "type": "Virus"}, {"text": "Afghanistan", "type": "SpatialConcept"}, {"text": "Iran", "type": "SpatialConcept"}, {"text": "Afghan", "type": "SpatialConcept"}, {"text": "refugees", "type": "PopulationGroup"}]}

Example input:
Sentence: Spatio - Temporal History of HIV - 1 CRF35 _ AD in Afghanistan and Iran HIV - 1 Circulating Recombinant Form 35 _ AD ( CRF35 _ AD ) has an important position in the epidemiological profile of Afghanistan and Iran .

Example answer:
{"entities": [{"text": "Spatio - Temporal History", "type": "ResearchActivity"}, {"text": "Afghanistan", "type": "SpatialConcept"}, {"text": "Iran", "type": "SpatialConcept"}, {"text": "HIV - 1 Circulating Recombinant Form 35 _ AD", "type": "Virus"}, {"text": "epidemiological", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Within this cluster , a bidirectional dispersion of the virus was observed across Afghanistan and Iran .

Example answer:
{"entities": [{"text": "virus", "type": "Virus"}, {"text": "Afghanistan", "type": "SpatialConcept"}, {"text": "Iran", "type": "SpatialConcept"}]}

Example input:
Sentence: In this study , we performed a Bayesian phylogeographic analysis to reconstruct the spatio - temporal dispersion pattern of this clade using eligible CRF35 _ AD gag and pol sequences available in the Los Alamos HIV database ( 432 sequences available from Iran , 16 sequences available from Afghanistan , and a single CRF35 _ AD -like pol sequence available from USA ) .

Example answer:
{"entities": [{"text": "gag and pol sequences", "type": "SpatialConcept"}, {"text": "Los Alamos", "type": "SpatialConcept"}, {"text": "HIV database", "type": "IntellectualProduct"}, {"text": "sequences", "type": "SpatialConcept"}, {"text": "Iran", "type": "SpatialConcept"}, {"text": "Afghanistan", "type": "SpatialConcept"}, {"text": "pol sequence", "type": "SpatialConcept"}, {"text": "USA", "type": "SpatialConcept"}]}

Example input:
Sentence: Our results also showed that across all phylogenies , Afghan and Iranian CRF35 _ AD sequences formed a monophyletic cluster ( posterior clade credibility > 0 . 7 ) .

Example answer:
{"entities": [{"text": "Afghan", "type": "SpatialConcept"}, {"text": "Iranian", "type": "SpatialConcept"}, {"text": "sequences", "type": "SpatialConcept"}]}

Example input:
Sentence: We could not clearly identify if Afghanistan or Iran first established or received this epidemic , as the root location of this cluster could not be robustly estimated .

Example answer:
{"entities": [{"text": "Afghanistan", "type": "SpatialConcept"}, {"text": "Iran", "type": "SpatialConcept"}, {"text": "epidemic", "type": "BiologicFunction"}]}

Input:
Sentence: Despite the presence of this clade in Afghanistan and Iran for over a decade , our understanding of its origin and dissemination patterns is limited .

## Item MedMentions:test:92
Example input:
Sentence: how nutrient enrichment ( i . e . , nitrogen availability ) affected the growth of Fucus vesiculosus , a foundational macroalgal species in the North Atlantic rocky intertidal zone , and found that nutrient -enriched algal blades showed a significant increase in tissue growth compared to individuals grown under ambient conditions .

Example answer:
{"entities": [{"text": "nutrient", "type": "Food"}, {"text": "nitrogen", "type": "Chemical"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "Fucus vesiculosus", "type": "Eukaryote"}, {"text": "macroalgal", "type": "Eukaryote"}, {"text": "species", "type": "Eukaryote"}, {"text": "North Atlantic rocky intertidal zone", "type": "SpatialConcept"}, {"text": "algal blades", "type": "IntellectualProduct"}, {"text": "tissue growth", "type": "BiologicFunction"}]}

Example input:
Sentence: On the post - glacial spread of human commensal Arabidopsis thaliana Recent work has shown that Arabidopsis thaliana contains genetic groups originating from different ice age refugia , with one particular group comprising over 95 % of the current worldwide population .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "Arabidopsis thaliana", "type": "Eukaryote"}]}

Example input:
Sentence: Paulownia witches ' broom is one of the most destructive diseases threatening Paulownia production .

Example answer:
{"entities": [{"text": "Paulownia", "type": "Eukaryote"}, {"text": "witches ' broom", "type": "BiologicFunction"}, {"text": "diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Determining putative vectors of the Bogia Coconut Syndrome phytoplasma using loop - mediated isothermal amplification of single - insect feeding media Phytoplasmas are insect vectored mollicutes responsible for disease in many economically important crops .

Example answer:
{"entities": [{"text": "putative vectors", "type": "Eukaryote"}, {"text": "Bogia Coconut Syndrome", "type": "BiologicFunction"}, {"text": "phytoplasma", "type": "Bacterium"}, {"text": "loop - mediated isothermal amplification", "type": "HealthCareActivity"}, {"text": "single - insect feeding media", "type": "Food"}, {"text": "Phytoplasmas", "type": "Bacterium"}, {"text": "insect vectored mollicutes", "type": "Bacterium"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "crops", "type": "Eukaryote"}]}

Example input:
Sentence: While there was a minimal effect of foliar water uptake on live fuel moisture , several species had lower xylem tension and greater photosynthetic rates after overnight fog treatments , especially Salvia leucophylla .

Example answer:
{"entities": [{"text": "foliar", "type": "Eukaryote"}, {"text": "water uptake", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "xylem", "type": "Eukaryote"}, {"text": "Salvia leucophylla", "type": "Eukaryote"}]}

Example input:
Sentence: Eimeria appeared to be more important than fishmeal in predisposing birds to NE , thus the application of Eimeria in NE challenge provides more consistent success in inducing the disease .

Example answer:
{"entities": [{"text": "Eimeria", "type": "Eukaryote"}, {"text": "birds", "type": "Eukaryote"}, {"text": "NE", "type": "BiologicFunction"}, {"text": "challenge", "type": "HealthCareActivity"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Recognizing that the preferred habitats for the species are in the valleys , systematic planting of keystone plant species such as fig trees ( Ficus ) creates the best microhabitats .

Example answer:
{"entities": [{"text": "habitats", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "valleys", "type": "SpatialConcept"}, {"text": "keystone plant", "type": "Eukaryote"}, {"text": "fig trees", "type": "Eukaryote"}, {"text": "Ficus", "type": "Eukaryote"}, {"text": "microhabitats", "type": "SpatialConcept"}]}

Example input:
Sentence: From this study , it appears that drought -deciduous species ( Artemisia californica and Salvia leucophylla ) benefit more from overnight fog events than evergreen species ( Adenostoma fasciculatum , Baccharis pilularis and Ceanothus megacarpus ) .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "Artemisia californica", "type": "Eukaryote"}, {"text": "Salvia leucophylla", "type": "Eukaryote"}, {"text": "Adenostoma fasciculatum", "type": "Eukaryote"}, {"text": "Baccharis pilularis", "type": "Eukaryote"}, {"text": "Ceanothus megacarpus", "type": "Eukaryote"}]}

Example input:
Sentence: Our findings reveal a rice plant strategy for modifying the genetic information to gain the upper hand in the struggle against insect herbivores .

Example answer:
{"entities": [{"text": "rice", "type": "Eukaryote"}, {"text": "plant", "type": "Eukaryote"}, {"text": "insect", "type": "Eukaryote"}, {"text": "herbivores", "type": "Eukaryote"}]}

Example input:
Sentence: The most widely used wild staple foods are Potetilla anserina roots , an important ceremonial food served on such occasions as New Year or at funerals .

Example answer:
{"entities": [{"text": "wild staple foods", "type": "Food"}, {"text": "Potetilla anserina", "type": "Eukaryote"}, {"text": "roots", "type": "Eukaryote"}, {"text": "ceremonial food", "type": "Food"}]}

Input:
Sentence: The most important famine plants remembered by people are the aerial bulbils of Persicaria vivipara .

## Item MedMentions:test:219
Example input:
Sentence: More severe DR was significantly associated with lower PI after adjusting for logarithm of the minimum angle of resolution best - corrected visual acuity , hyperlipidaemia , diabetes type and ETDRS ring in a multivariate mixed linear model .

Example answer:
{"entities": [{"text": "DR", "type": "BiologicFunction"}, {"text": "minimum angle of resolution", "type": "ClinicalAttribute"}, {"text": "best - corrected visual acuity", "type": "Finding"}, {"text": "hyperlipidaemia", "type": "BiologicFunction"}, {"text": "diabetes type", "type": "Finding"}, {"text": "ETDRS", "type": "IntellectualProduct"}]}

Example input:
Sentence: Improve d self - efficacy was associated with a decrease in concerns about medications ( r = - 0 . 64 ) .

Example answer:
{"entities": [{"text": "Improve", "type": "Finding"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "medications", "type": "HealthCareActivity"}]}

Example input:
Sentence: 12 - 1 . 58 ; number needed to harm [ NNH ] , 100 ) and COX - 2 inhibitors ( OR , 1 . 31 ; 95 % CI , 1 . 04 - 1 . 66 ; NNH , 333 ) was associated with increased odds of revision surgery .

Example answer:
{"entities": [{"text": "COX - 2 inhibitors", "type": "Chemical"}, {"text": "revision surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Notably , SL4 treatment resulted in an obvious increase in p21 mRNA and protein levels through activation of MAPK signaling pathways , but not the TGF - β pathway .

Example answer:
{"entities": [{"text": "SL4", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "p21", "type": "AnatomicalStructure"}, {"text": "mRNA", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "MAPK signaling pathways", "type": "BiologicFunction"}, {"text": "TGF - β pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: Thus , D5D inhibition increases DGLA ( precursor to anti - inflammatory eicosanoids ) while decreasing AA ( precursor to pro - inflammatory eicosanoids ) , and could result in synergistic improvement in the low - grade inflammatory state .

Example answer:
{"entities": [{"text": "D5D", "type": "Chemical"}, {"text": "inhibition", "type": "BiologicFunction"}, {"text": "DGLA", "type": "Chemical"}, {"text": "eicosanoids", "type": "Chemical"}, {"text": "AA", "type": "Chemical"}]}

Example input:
Sentence: Disease progression despite PRRT was associated with shorter survival ( median OS 15 vs 53 mo , P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "Disease progression", "type": "BiologicFunction"}, {"text": "PRRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Disease progression was rapid under oxaliplatin , capecitabine , irinotecan , and bevacizumab .

Example answer:
{"entities": [{"text": "Disease progression", "type": "BiologicFunction"}, {"text": "oxaliplatin", "type": "Chemical"}, {"text": "capecitabine", "type": "Chemical"}, {"text": "irinotecan", "type": "Chemical"}, {"text": "bevacizumab", "type": "Chemical"}]}

Example input:
Sentence: Seven of 28 patients treated with DPP4 inhibitors and 26 of 54 treated with other hypoglycemic agents showed progression of retinopathy , defined as one or more steps on the Early Treatment Diabetic Retinopathy Study scale ( P = 0 . 043 ) .

Example answer:
{"entities": [{"text": "DPP4 inhibitors", "type": "Chemical"}, {"text": "hypoglycemic agents", "type": "Chemical"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "retinopathy", "type": "BiologicFunction"}]}

Example input:
Sentence: Treatment with DPP4 inhibitors was the independent protective factor against the progression of DR , aside from improving glycemic control .

Example answer:
{"entities": [{"text": "DPP4 inhibitors", "type": "Chemical"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "DR", "type": "BiologicFunction"}, {"text": "improving glycemic control", "type": "Finding"}]}

Example input:
Sentence: This is the first study to show the benefits of DPP4 inhibitors in reducing DR progression , and provides encouraging preliminary data for further evaluation of DPP4 inhibitors in the progression of DR in a randomized , double - blind , placebo - controlled trial .

Example answer:
{"entities": [{"text": "DPP4 inhibitors", "type": "Chemical"}, {"text": "DR", "type": "BiologicFunction"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "evaluation", "type": "HealthCareActivity"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "double - blind", "type": "ResearchActivity"}]}

Input:
Sentence: Treatment with DPP4 inhibitors was associated with a lower risk of DR progression ( P = 0 . 011 ) .

## Item MedMentions:test:401
Example input:
Sentence: This journal requires that authors assign a level of evidence to each article .

Example answer:
{"entities": [{"text": "journal", "type": "IntellectualProduct"}, {"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "level of evidence", "type": "Finding"}, {"text": "article", "type": "IntellectualProduct"}]}

Example input:
Sentence: Of the 416 citations obtained , 87 met inclusion criteria , totaling 34 , 255 subjects .

Example answer:
{"entities": [{"text": "citations", "type": "IntellectualProduct"}, {"text": "subjects", "type": "PopulationGroup"}]}

Example input:
Sentence: First and senior authors with an M .

Example answer:
{"entities": [{"text": "senior", "type": "PopulationGroup"}, {"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "M .", "type": "IntellectualProduct"}]}

Example input:
Sentence: The manuscript was written by Chastek and Dalal and revised by Albers and Yancy , assisted by the other authors .

Example answer:
{"entities": [{"text": "manuscript", "type": "IntellectualProduct"}, {"text": "authors", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: When the European , AECG and ACR Sjogren 's criteria were applied , 666 patients ( 79 . 9 % ) satisfied at least one of them .

Example answer:
{"entities": [{"text": "European", "type": "IntellectualProduct"}, {"text": "AECG", "type": "IntellectualProduct"}, {"text": "ACR Sjogren 's criteria", "type": "IntellectualProduct"}]}

Example input:
Sentence: All authors have approved the manuscript and agree with submission to Journal of Proteomics .

Example answer:
{"entities": [{"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "manuscript", "type": "IntellectualProduct"}, {"text": "agree", "type": "Finding"}, {"text": "Journal of Proteomics", "type": "IntellectualProduct"}]}

Example input:
Sentence: The European criteria , American - European Consensus Group ( AECG ) and American College of Rheumatology ( ACR ) Sjogren 's criteria were applied .

Example answer:
{"entities": [{"text": "European criteria", "type": "IntellectualProduct"}, {"text": "American - European Consensus Group", "type": "IntellectualProduct"}, {"text": "AECG", "type": "IntellectualProduct"}, {"text": "American College of Rheumatology ( ACR ) Sjogren 's criteria", "type": "IntellectualProduct"}]}

Example input:
Sentence: Inclusion and exclusion criteria concentrated on patient -specific surgical applications , yielding 141 full - text articles , of which 33 craniomaxillofacial articles were analyzed .

Example answer:
{"entities": [{"text": "surgical", "type": "HealthCareActivity"}, {"text": "articles", "type": "IntellectualProduct"}, {"text": "craniomaxillofacial articles", "type": "IntellectualProduct"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: The authors have no conflicts of interest to declare .

Example answer:
{"entities": [{"text": "authors", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Review of randomised clinical trials that used a non - inferiority design published between January 2010 and May 2015 in medical journals that had an impact factor > 10 ( JAMA Internal Medicine , Archives Internal Medicine , PLOS Medicine , Annals of Internal Medicine , BMJ , JAMA , Lancet and New England Journal of Medicine ) .

Example answer:
{"entities": [{"text": "randomised", "type": "ResearchActivity"}, {"text": "clinical trials", "type": "ResearchActivity"}, {"text": "non - inferiority", "type": "Finding"}, {"text": "medical journals", "type": "IntellectualProduct"}, {"text": "JAMA Internal Medicine", "type": "IntellectualProduct"}, {"text": "Archives Internal Medicine", "type": "IntellectualProduct"}, {"text": "PLOS Medicine", "type": "IntellectualProduct"}, {"text": "Annals of Internal Medicine", "type": "IntellectualProduct"}, {"text": "BMJ", "type": "IntellectualProduct"}, {"text": "JAMA", "type": "IntellectualProduct"}, {"text": "Lancet and New England Journal of Medicine", "type": "IntellectualProduct"}]}

Input:
Sentence: All listed authors meet the criteria for authorship set forth by the International Committee for Medical Journal Editors .

## Item MedMentions:test:313
Example input:
Sentence: Acute kidney injury ( AKI ) is a common side effect in the context of various medical procedures , and RIC has been suggested as a means of reducing its incidence .

Example answer:
{"entities": [{"text": "Acute kidney injury", "type": "InjuryOrPoisoning"}, {"text": "AKI", "type": "InjuryOrPoisoning"}, {"text": "medical procedures", "type": "HealthCareActivity"}, {"text": "RIC", "type": "HealthCareActivity"}]}

Example input:
Sentence: Hypoalbuminemia was associated with a significantly higher 30 - day mortality in major procedures such as cystectomy , and in smaller procedures such as TURBT ( P < .01 ) .

Example answer:
{"entities": [{"text": "Hypoalbuminemia", "type": "BiologicFunction"}, {"text": "procedures", "type": "HealthCareActivity"}, {"text": "cystectomy", "type": "HealthCareActivity"}, {"text": "TURBT", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the exploratory analysis , patients with DOR ≥12 months ( n = 287 ) or ≥24 months ( n = 133 ) were more likely to experience grade 3 / 4 AEs than the overall population .

Example answer:
{"entities": [{"text": "exploratory analysis", "type": "ResearchActivity"}, {"text": "AEs", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: Systemic inflammatory response syndrome ( SIRS ) , septic shock , and nephrotoxic medications were evaluated as covariates for AKI .

Example answer:
{"entities": [{"text": "Systemic inflammatory response syndrome", "type": "BiologicFunction"}, {"text": "SIRS", "type": "BiologicFunction"}, {"text": "septic shock", "type": "BiologicFunction"}, {"text": "medications", "type": "IntellectualProduct"}, {"text": "AKI", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Our findings suggest that efforts to reduce AKI in the perioperative period may have a significant long - term impact on patients and payers in reducing mortality and health care utilization .

Example answer:
{"entities": [{"text": "AKI", "type": "InjuryOrPoisoning"}, {"text": "health care utilization", "type": "HealthCareActivity"}]}

Example input:
Sentence: After lung transplantation , AKI is common and often evolves into severe CKD , which is a known cause of morbidity and mortality .

Example answer:
{"entities": [{"text": "lung transplantation", "type": "HealthCareActivity"}, {"text": "AKI", "type": "InjuryOrPoisoning"}, {"text": "CKD", "type": "BiologicFunction"}]}

Example input:
Sentence: Acute Kidney Injury Severity and Long - Term Readmission and Mortality After Cardiac Surgery Acute kidney injury ( AKI ) is a common complication after cardiac surgery .

Example answer:
{"entities": [{"text": "Acute Kidney Injury", "type": "InjuryOrPoisoning"}, {"text": "Readmission", "type": "HealthCareActivity"}, {"text": "Cardiac Surgery", "type": "HealthCareActivity"}, {"text": "Acute kidney injury", "type": "InjuryOrPoisoning"}, {"text": "AKI", "type": "InjuryOrPoisoning"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "cardiac surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Recovery rate of AKI was lower than expected ( 19 % ) , and the cumulative incidence of severe CKD at 1 year was 15 % .

Example answer:
{"entities": [{"text": "AKI", "type": "InjuryOrPoisoning"}, {"text": "CKD", "type": "BiologicFunction"}]}

Example input:
Sentence: Relative to patients without AKI , stage 1 patients had a 56 % increased risk of mortality ( 95 % CI : 1 . 14 to 2 . 13 ) , whereas stage 2 or 3 patients had

Example answer:
{"entities": [{"text": "AKI", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Within 5 years , 513 patients ( 33 . 8 % ) had AKI with AKIN stage 1 ( 29 . 9 % ) and stage 2 to 3 ( 3 . 9 % ) .

Example answer:
{"entities": [{"text": "AKI", "type": "InjuryOrPoisoning"}, {"text": "AKIN", "type": "IntellectualProduct"}]}

Input:
Sentence: Severity of AKI using the AKIN stage criteria is associated with a significantly increased risk of 5 - year readmission and mortality .

## Item MedMentions:test:375
Example input:
Sentence: Hierarchical clustering revealed three response patterns : ( i ) TIL ( high ) tumors showed increases in multiple immune markers after chemotherapy ; ( ii ) TIL ( low ) tumors underwent similar increases , achieving patterns indistinguishable from the first group ; and ( iii ) TIL ( negative ) cases generally remained negative .

Example answer:
{"entities": [{"text": "Hierarchical clustering", "type": "ResearchActivity"}, {"text": "TIL", "type": "AnatomicalStructure"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "negative", "type": "Finding"}]}

Example input:
Sentence: Adjuvant chemotherapy was administrated in patients with Ki - 67 > 10 % ; every patients were treated with radiotherapy and with hormonal therapy too .

Example answer:
{"entities": [{"text": "Adjuvant chemotherapy", "type": "HealthCareActivity"}, {"text": "administrated", "type": "HealthCareActivity"}, {"text": "Ki - 67", "type": "Chemical"}, {"text": "radiotherapy", "type": "HealthCareActivity"}, {"text": "hormonal therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: We considered the typical acidic extracellular pH ( pHe ) of sarcomas , and found that doxorubicin ( DXR ) cytotoxicity is reduced in P - gp negative OS cells cultured at pHe 6 .

Example answer:
{"entities": [{"text": "sarcomas", "type": "BiologicFunction"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DXR", "type": "Chemical"}, {"text": "cytotoxicity", "type": "BiologicFunction"}, {"text": "P - gp", "type": "AnatomicalStructure"}, {"text": "OS", "type": "BiologicFunction"}, {"text": "cells cultured", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Patients ≥70 years were more often treated with less toxic chemotherapy , yet experienced higher rates of hospitalization during treatment and increased rates of acute mortality following CRT .

Example answer:
{"entities": [{"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "hospitalization", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "CRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Tumors that expressed four or five conditions ( biomarkers of chemoresistance with a determinated cutoff ) were associated with a 9 - fold increase in the chances of these patients of having a poor response to NCT .

Example answer:
{"entities": [{"text": "Tumors", "type": "BiologicFunction"}, {"text": "biomarkers", "type": "Chemical"}, {"text": "poor response", "type": "Finding"}]}

Example input:
Sentence: Among all included patients ( n = 443 ) , advanced neoplasia was found in 13 of 310 patients ( 4 . 2 % ) of the 1 - to 5 - mm group versus 13 of 133 patients ( 9 . 8 % ) of the 6 - to 9 - mm group ( hazard ratio [ HR ] , 3 . 49 ; 95 % confidence interval [ CI ] , 1 . 6 - 7 . 6 ) .

Example answer:
{"entities": [{"text": "neoplasia", "type": "BiologicFunction"}, {"text": "found", "type": "Finding"}]}

Example input:
Sentence: Furthermore , the most important factor for growing of tumorspheres is obtaining chemotherapy .

Example answer:
{"entities": [{"text": "tumorspheres", "type": "AnatomicalStructure"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients treated with prior radiotherapy , surgery , or chemotherapy were excluded to reduce heterogeneity .

Example answer:
{"entities": [{"text": "treated with", "type": "Finding"}, {"text": "radiotherapy", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "reduce", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients with HER2 positive primary tumor had higher number of tumorspheres .

Example answer:
{"entities": [{"text": "HER2 positive primary tumor", "type": "BiologicFunction"}, {"text": "tumorspheres", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In our study ( 4 / 2015 to 3 / 2016 ) , chemotherapy was withdrawn because of side effects during treatment for solid carcinomas in 8 % ( 4 / 51 ) of the patients .

Example answer:
{"entities": [{"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "withdrawn", "type": "Finding"}, {"text": "side effects", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "solid carcinomas", "type": "BiologicFunction"}]}

Input:
Sentence: Patients with chemotherapy treatment had lower numbers of tumorspheres compared to patients without chemotherapy .

## Item MedMentions:test:386
Example input:
Sentence: Unpartitioned and codon - based analyses placed Rhizothera sister to a tragopan clade , whereas a partitioned DNA model of the mitogenome was congruent with UCE results .

Example answer:
{"entities": [{"text": "codon - based analyses", "type": "HealthCareActivity"}, {"text": "Rhizothera", "type": "Eukaryote"}, {"text": "tragopan clade", "type": "Eukaryote"}, {"text": "DNA model", "type": "IntellectualProduct"}, {"text": "mitogenome", "type": "AnatomicalStructure"}, {"text": "UCE results", "type": "Finding"}]}

Example input:
Sentence: We did not find mitochondrial DNA of one species in individuals with the plumage of the other species , except in F1 hybrids , which agrees with Haldane´s Rule .

Example answer:
{"entities": [{"text": "mitochondrial DNA", "type": "Chemical"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "plumage", "type": "AnatomicalStructure"}, {"text": "Haldane´s Rule", "type": "IntellectualProduct"}]}

Example input:
Sentence: Activity of G - 6 - PDH was largely restricted to cytosolic fraction while MDH was found in both cytosolic and mitochondrial fraction in Gastrothylax indicus .

Example answer:
{"entities": [{"text": "Activity", "type": "BiologicFunction"}, {"text": "G - 6 - PDH", "type": "Chemical"}, {"text": "cytosolic fraction", "type": "AnatomicalStructure"}, {"text": "MDH", "type": "Chemical"}, {"text": "cytosolic", "type": "AnatomicalStructure"}, {"text": "mitochondrial fraction", "type": "AnatomicalStructure"}, {"text": "Gastrothylax indicus", "type": "Eukaryote"}]}

Example input:
Sentence: Intron Derived Size Polymorphism in the Mitochondrial Genomes of Closely Related Chrysoporthe Species In this study , the complete mitochondrial ( mt ) genomes of Chrysoporthe austroafricana ( 190 , 834 bp ) , C .

Example answer:
{"entities": [{"text": "Intron", "type": "Chemical"}, {"text": "Size", "type": "SpatialConcept"}, {"text": "Polymorphism", "type": "BiologicFunction"}, {"text": "Mitochondrial Genomes", "type": "AnatomicalStructure"}, {"text": "Chrysoporthe Species", "type": "Eukaryote"}, {"text": "mitochondrial ( mt ) genomes", "type": "AnatomicalStructure"}, {"text": "Chrysoporthe austroafricana", "type": "Eukaryote"}, {"text": "C .", "type": "Eukaryote"}]}

Example input:
Sentence: In all mitogenome analyses , Pucrasia was sister to a clade including Perdix and the typical pheasants with high support , in contrast to UCEs and published nuclear intron data .

Example answer:
{"entities": [{"text": "mitogenome analyses", "type": "HealthCareActivity"}, {"text": "Pucrasia", "type": "Eukaryote"}, {"text": "clade", "type": "Eukaryote"}, {"text": "Perdix", "type": "Eukaryote"}, {"text": "pheasants", "type": "Eukaryote"}, {"text": "published nuclear intron data", "type": "IntellectualProduct"}]}

Example input:
Sentence: DNA variation in one mitochondrial marker and nine nuclear microsatellite loci revealed a strong phylogeographic pattern across 28 populations of G .

Example answer:
{"entities": [{"text": "DNA", "type": "Chemical"}, {"text": "mitochondrial", "type": "AnatomicalStructure"}, {"text": "marker", "type": "SpatialConcept"}, {"text": "nuclear", "type": "AnatomicalStructure"}, {"text": "microsatellite loci", "type": "AnatomicalStructure"}, {"text": "phylogeographic pattern", "type": "Finding"}, {"text": "G .", "type": "Eukaryote"}]}

Example input:
Sentence: In cidaroid sea urchins , the anciently diverged sister clade to euechinoid sea urchins , a homologous SM cell type ingresses later in development , after gastrulation has commenced , and consequently at a distinct developmental address .

Example answer:
{"entities": [{"text": "cidaroid", "type": "Eukaryote"}, {"text": "sea urchins", "type": "Eukaryote"}, {"text": "sister clade", "type": "Eukaryote"}, {"text": "euechinoid", "type": "Eukaryote"}, {"text": "SM", "type": "AnatomicalStructure"}, {"text": "cell type", "type": "AnatomicalStructure"}, {"text": "ingresses", "type": "BiologicFunction"}, {"text": "development", "type": "BiologicFunction"}, {"text": "gastrulation", "type": "BiologicFunction"}, {"text": "developmental", "type": "BiologicFunction"}, {"text": "address", "type": "SpatialConcept"}]}

Example input:
Sentence: Additionally , the mitochondrial genome of another member of the Cryphonectriaceae , namely Cryphonectria parasitica ( 158 , 902 bp ) , was retrieved and annotated for comparative purposes .

Example answer:
{"entities": [{"text": "mitochondrial genome", "type": "AnatomicalStructure"}, {"text": "Cryphonectriaceae", "type": "Eukaryote"}, {"text": "Cryphonectria parasitica", "type": "Eukaryote"}]}

Example input:
Sentence: A phylogenetic tree obtained by Bayesian Inference based on DNA sequences of the mitochondrial cytochrome b ( 1 , 023 bp ) grouped them within the Northern clade of the species but failed to separate them from the subspecies V .

Example answer:
{"entities": [{"text": "DNA sequences", "type": "SpatialConcept"}, {"text": "mitochondrial cytochrome b", "type": "Chemical"}, {"text": "grouped", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "subspecies", "type": "IntellectualProduct"}, {"text": "V .", "type": "Eukaryote"}]}

Example input:
Sentence: All three formed a distinct clade in earlier mitochondrial phylogenies .

Example answer:
{"entities": [{"text": "clade", "type": "Eukaryote"}, {"text": "mitochondrial", "type": "AnatomicalStructure"}]}

Input:
Sentence: The two major mitochondrial clades of G .

## Item MedMentions:test:17
Example input:
Sentence: GPs participating in the pdf article intervention demonstrated a decline in self - assessed communication , both at the level of global scoring ( Wald χ ( 2 ) = 34 . 5 , P < . 001 ) and at the level of 20 of 26 specific behaviors ( all P < .

Example answer:
{"entities": [{"text": "GPs", "type": "ProfessionalOrOccupationalGroup"}, {"text": "pdf article", "type": "IntellectualProduct"}, {"text": "intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: Latent class growth analysis ( LCGA ) was applied to 3507 MS patients using an electronic health records ( EHR ) data base to identify subgroups of MS patients based on self - reported depression screening ( PHQ - 9 ) .

Example answer:
{"entities": [{"text": "MS", "type": "BiologicFunction"}, {"text": "electronic health records ( EHR ) data base", "type": "IntellectualProduct"}, {"text": "subgroups", "type": "PopulationGroup"}, {"text": "depression screening", "type": "HealthCareActivity"}]}

Example input:
Sentence: PGA was usually higher than PhGA .

Example answer:
{"entities": [{"text": "PGA", "type": "IntellectualProduct"}]}

Example input:
Sentence: A systematic literature review of all articles published up to January 2015 in Medline or Embase , reporting discordance in RA , was conducted by 2 investigators .

Example answer:
{"entities": [{"text": "literature review", "type": "IntellectualProduct"}, {"text": "articles", "type": "IntellectualProduct"}, {"text": "Medline", "type": "IntellectualProduct"}, {"text": "Embase", "type": "IntellectualProduct"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "investigators", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: The drivers of PGA were pain and functional incapacity , whereas drivers of PhGA were joint counts and acute - phase reactants .

Example answer:
{"entities": [{"text": "PGA", "type": "IntellectualProduct"}, {"text": "pain", "type": "Finding"}, {"text": "joint counts", "type": "IntellectualProduct"}, {"text": "acute - phase reactants", "type": "Chemical"}]}

Example input:
Sentence: We evaluated the discordance rate ( DR ) and inter - rater agreement between local and central histopathological report and the clinical implication on treatment decision .

Example answer:
{"entities": [{"text": "local", "type": "SpatialConcept"}, {"text": "central", "type": "SpatialConcept"}, {"text": "histopathological report", "type": "IntellectualProduct"}]}

Example input:
Sentence: The pooled percentage of patients with discordance was 43 % ( 95 % confidence interval 36 % - 51 % ; range 25 % - 76 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Patient - Physician Discordance in Global Assessment in Rheumatoid Arthritis : A Systematic Literature Review With Meta - Analysis The integration of the patient in therapeutic decision - making is important in the management of rheumatoid arthritis ( RA ) , but the patient opinion regarding disease status may differ from the physician 's opinion .

Example answer:
{"entities": [{"text": "Physician", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Rheumatoid Arthritis", "type": "BiologicFunction"}, {"text": "Literature Review", "type": "IntellectualProduct"}, {"text": "Meta - Analysis", "type": "ResearchActivity"}, {"text": "decision - making", "type": "BiologicFunction"}, {"text": "management", "type": "HealthCareActivity"}, {"text": "rheumatoid arthritis", "type": "BiologicFunction"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "physician 's", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: The value of the difference | PGA - PhGA | defining discordance varied between ≥0 . 5 cm ( n = 2 studies ) to ≥3 cm ( n = 5 studies ) ; the weighted mean value was 2 . 7 cm .

Example answer:
{"entities": [{"text": "PGA", "type": "IntellectualProduct"}]}

Example input:
Sentence: Discordance in global assessment was most frequently defined as a difference of 3 points or more ; even with such a stringent definition , up to half the patients were found to be discordant .

Example answer:
{"entities": []}

Input:
Sentence: Discordance was defined based on the absolute difference of patient global ( PGA ) and physician global assessments ( PhGA ) on 0 - 10 - cm scales .

## Item MedMentions:test:103
Example input:
Sentence: Based on personalized malignancy risk , 54 % of nodules > 4 and ≤6 mm were reclassified to longer - term follow - up than recommended by Fleischner .

Example answer:
{"entities": [{"text": "nodules", "type": "AnatomicalStructure"}, {"text": "Fleischner", "type": "Organization"}]}

Example input:
Sentence: On biopsy , the skin nodule showed an infiltrating lymphoid tumor composed of immunoblastic cells with brisk mitosis and apoptosis .

Example answer:
{"entities": [{"text": "biopsy", "type": "HealthCareActivity"}, {"text": "skin nodule", "type": "AnatomicalStructure"}, {"text": "infiltrating", "type": "BiologicFunction"}, {"text": "lymphoid tumor", "type": "BiologicFunction"}, {"text": "immunoblastic cells", "type": "AnatomicalStructure"}, {"text": "mitosis", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Hard and fixed nodules were observed on digital rectal examination in 14 cases .

Example answer:
{"entities": [{"text": "nodules", "type": "AnatomicalStructure"}, {"text": "digital rectal examination", "type": "HealthCareActivity"}]}

Example input:
Sentence: Logistic regression analysis did not identify additional nodule parameters of future progression , apart from part - solid nature .

Example answer:
{"entities": [{"text": "nodule", "type": "AnatomicalStructure"}, {"text": "parameters", "type": "Finding"}]}

Example input:
Sentence: Morphological investigations revealed a homogeneous monolithic structure composed of uniform nodules ( ∼0 .

Example answer:
{"entities": [{"text": "Morphological", "type": "SpatialConcept"}, {"text": "investigations", "type": "HealthCareActivity"}, {"text": "homogeneous monolithic structure", "type": "SpatialConcept"}, {"text": "nodules", "type": "SpatialConcept"}]}

Example input:
Sentence: Twenty - seven percent of nodules ≤4 mm were reclassified to shorter - term follow - up .

Example answer:
{"entities": [{"text": "nodules", "type": "AnatomicalStructure"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: We divided the nodules into two subgroups according to the histopathology as benign and malignant , and compared the preoperative ultrasonographical , clinical , and biochemical findings .

Example answer:
{"entities": [{"text": "nodules", "type": "BiologicFunction"}, {"text": "subgroups", "type": "PopulationGroup"}, {"text": "histopathology", "type": "HealthCareActivity"}, {"text": "ultrasonographical", "type": "ClinicalAttribute"}, {"text": "clinical", "type": "ClinicalAttribute"}, {"text": "biochemical findings", "type": "Finding"}]}

Example input:
Sentence: Risk of malignancy for nodules was calculated based on size criteria according to the Fleischner Society recommendations from 2005 , along with the additional discriminators of pack - years smoking history , sex , and nodule location .

Example answer:
{"entities": [{"text": "Risk of malignancy", "type": "Finding"}, {"text": "nodules", "type": "Finding"}, {"text": "Fleischner Society", "type": "Organization"}, {"text": "additional discriminators", "type": "IntellectualProduct"}, {"text": "nodule", "type": "AnatomicalStructure"}, {"text": "location", "type": "SpatialConcept"}]}

Example input:
Sentence: An algorithm was used to categorize nodules found in the first screening year of the National Lung Screening Trial as malignant or nonmalignant .

Example answer:
{"entities": [{"text": "algorithm", "type": "IntellectualProduct"}, {"text": "nodules", "type": "Finding"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "malignant", "type": "BiologicFunction"}, {"text": "nonmalignant", "type": "BiologicFunction"}]}

Example input:
Sentence: Subsolid pulmonary nodule morphology and associated patient characteristics in a routine clinical population To determine the presence and morphology of subsolid pulmonary nodules ( SSNs ) in a non - screening setting and relate them to clinical and patient characteristics .

Example answer:
{"entities": [{"text": "Subsolid pulmonary nodule", "type": "Finding"}, {"text": "population", "type": "PopulationGroup"}, {"text": "subsolid pulmonary nodules", "type": "Finding"}, {"text": "SSNs", "type": "Finding"}]}

Input:
Sentence: Nodule morphology , location , and patient characteristics were evaluated .

## Item MedMentions:test:112
Example input:
Sentence: The high - risk group showed decreased fractional anisotropy ( FA ) , a measure of water diffusion directionality , and increased radial diffusivity in the anterior region of corpus callosum compared to the low - risk group .

Example answer:
{"entities": [{"text": "high - risk group", "type": "PopulationGroup"}, {"text": "fractional anisotropy", "type": "HealthCareActivity"}, {"text": "FA", "type": "HealthCareActivity"}, {"text": "water", "type": "Chemical"}, {"text": "anterior region of corpus callosum", "type": "AnatomicalStructure"}, {"text": "low - risk group", "type": "PopulationGroup"}]}

Example input:
Sentence: Perfusion with netarsudil - M1 significantly increased C when compared to baseline ( 51 % , P < 0 .

Example answer:
{"entities": [{"text": "Perfusion", "type": "HealthCareActivity"}, {"text": "netarsudil - M1", "type": "Chemical"}, {"text": "C", "type": "HealthCareActivity"}]}

Example input:
Sentence: 0 minutes versus 82 . 5 min , p = 0 . 027 ) , rate of allogeneic blood transfusion ( 2 % versus 24 % , p = 0 . 001 ) , and cup alignment in the safe zone ( 100 % versus 88 % , p = 0 . 027 ) were significantly improved in the second group compared to the first group .

Example answer:
{"entities": [{"text": "allogeneic blood transfusion", "type": "HealthCareActivity"}]}

Example input:
Sentence: Association between OCT -based microangiography perfusion indices and diabetic retinopathy severity To evaluate the association between retinal capillary non - perfusion and diabetic retinopathy ( DR ) severity using optical coherence tomography - based microangiography ( OMAG ) .

Example answer:
{"entities": [{"text": "OCT", "type": "HealthCareActivity"}, {"text": "diabetic retinopathy", "type": "BiologicFunction"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "retinal capillary non - perfusion", "type": "BiologicFunction"}, {"text": "DR", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients with GCA had increased risks for all types of incident vascular disease compared with non - vasculitis patients : adjusted hazard ratios were 1 . 57 ( 95 % CI : 1 . 36 , 1 . 82 ) for myocardial infarction , 1 . 41 ( 95 % CI : 1 . 29 , 1 . 55 ) for stroke , 1 . 75 ( 95 % CI : 1 . 49 , 2 . 06 ) for peripheral vascular disease , 1 . 98 ( 95 % CI : 1 . 50 , 2 . 62 ) for aortic aneurysm and 2 . 03 ( 95 % CI : 1 . 77 , 2 . 33 ) for venous thromboembolism .

Example answer:
{"entities": [{"text": "GCA", "type": "BiologicFunction"}, {"text": "risks for all types of incident", "type": "Finding"}, {"text": "vascular disease", "type": "BiologicFunction"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "peripheral vascular disease", "type": "BiologicFunction"}, {"text": "aortic aneurysm", "type": "BiologicFunction"}, {"text": "venous thromboembolism", "type": "BiologicFunction"}]}

Example input:
Sentence: To analyze perfusion parameters derived from dynamic computed tomography perfusion imaging ( CTPI ) in patients with suspected coronary artery disease ( CAD ) , and relationship with risk factors .

Example answer:
{"entities": [{"text": "parameters", "type": "Finding"}, {"text": "dynamic computed tomography perfusion imaging", "type": "HealthCareActivity"}, {"text": "CTPI", "type": "HealthCareActivity"}, {"text": "coronary artery disease", "type": "BiologicFunction"}, {"text": "CAD", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}]}

Example input:
Sentence: FA of this region is feasible and may improve diagnosis compared to traditional noninvasive myocardial perfusion analysis .

Example answer:
{"entities": [{"text": "FA", "type": "ResearchActivity"}, {"text": "region", "type": "SpatialConcept"}, {"text": "improve", "type": "Finding"}, {"text": "diagnosis", "type": "Finding"}, {"text": "noninvasive", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: We found that CAD severity by SYNTAX score as well as number of vessels involved was significantly different among quartiles ( p - values < 0 . 001 and < 0 .

Example answer:
{"entities": [{"text": "CAD", "type": "BiologicFunction"}, {"text": "vessels", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Perfusion Angiography in Acute Ischemic Stroke Visualization and quantification of blood flow are essential for the diagnosis and treatment evaluation of cerebrovascular diseases .

Example answer:
{"entities": [{"text": "Perfusion", "type": "HealthCareActivity"}, {"text": "Angiography", "type": "HealthCareActivity"}, {"text": "Ischemic Stroke", "type": "BiologicFunction"}, {"text": "blood flow", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "treatment evaluation", "type": "HealthCareActivity"}, {"text": "cerebrovascular diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients with visual perfusion defects on CTPI , previous coronary intervention , or missing risk factor details were excluded .

Example answer:
{"entities": [{"text": "CTPI", "type": "HealthCareActivity"}, {"text": "coronary intervention", "type": "HealthCareActivity"}, {"text": "risk factor", "type": "Finding"}]}

Input:
Sentence: With further standardization , absolute perfusion measures may improve CAD risk stratification in patients without visual perfusion defects .

## Item MedMentions:test:115
Example input:
Sentence: Inhibition of STEP61 ameliorates deficits in mouse and hiPSC -based schizophrenia models The brain - specific tyrosine phosphatase , STEP ( STriatal - Enriched protein tyrosine Phosphatase ) is an important regulator of synaptic function .

Example answer:
{"entities": [{"text": "Inhibition", "type": "BiologicFunction"}, {"text": "STEP61", "type": "Chemical"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "hiPSC", "type": "AnatomicalStructure"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "models", "type": "BiologicFunction"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "tyrosine phosphatase", "type": "Chemical"}, {"text": "STEP", "type": "Chemical"}, {"text": "STriatal - Enriched protein tyrosine Phosphatase", "type": "Chemical"}, {"text": "synaptic function", "type": "BiologicFunction"}]}

Example input:
Sentence: These findings suggest that sulforaphane might be a promising therapeutic agent for cognitive enhancement in Alzheimer 's disease .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "sulforaphane", "type": "Chemical"}, {"text": "therapeutic agent", "type": "Chemical"}, {"text": "cognitive", "type": "BiologicFunction"}, {"text": "Alzheimer 's disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Simvastatin enhances the hippocampal klotho in a rat model of streptozotocin - induced cognitive decline Brain oxidative status is a crucial factor in the development of sporadic Alzheimer 's disease ( AD ) .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "klotho", "type": "Chemical"}, {"text": "rat", "type": "Eukaryote"}, {"text": "model", "type": "BiologicFunction"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "cognitive decline", "type": "BiologicFunction"}, {"text": "Brain", "type": "AnatomicalStructure"}, {"text": "Alzheimer 's disease", "type": "BiologicFunction"}, {"text": "AD", "type": "BiologicFunction"}]}

Example input:
Sentence: This study was undertaken to examine the effect of sulforaphane on cognitive impairment in zebra fish model using a novel method of fear conditioning .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "sulforaphane", "type": "Chemical"}, {"text": "cognitive impairment", "type": "BiologicFunction"}, {"text": "zebra fish", "type": "Eukaryote"}, {"text": "model", "type": "BiologicFunction"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "fear conditioning", "type": "BiologicFunction"}]}

Example input:
Sentence: We examined the effect of simvastatin ( 5mg / kg , daily for 3 weeks ) on hippocampal klotho and MnSOD expression in the cognitive declined animal model induced by intracerebroventricular ( ICV ) - streptozotocin ( STZ ) administration .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "klotho", "type": "Chemical"}, {"text": "MnSOD", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "cognitive declined", "type": "BiologicFunction"}, {"text": "animal model", "type": "BiologicFunction"}, {"text": "intracerebroventricular", "type": "SpatialConcept"}, {"text": "ICV", "type": "SpatialConcept"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "STZ", "type": "Chemical"}, {"text": "administration", "type": "HealthCareActivity"}]}

Example input:
Sentence: Cognition Enhancing Activity of Sulforaphane Against Scopolamine Induced Cognitive Impairment in Zebra Fish ( Danio rerio ) Several epidemiological studies have shown that consumption of large quantities of vegetables especially cruciferous vegetables ( Broccoli and Brussels sprouts ) can protect against chronic diseases .

Example answer:
{"entities": [{"text": "Cognition", "type": "BiologicFunction"}, {"text": "Sulforaphane", "type": "Chemical"}, {"text": "Scopolamine", "type": "Chemical"}, {"text": "Cognitive Impairment", "type": "BiologicFunction"}, {"text": "Zebra Fish", "type": "Eukaryote"}, {"text": "Danio rerio", "type": "Eukaryote"}, {"text": "epidemiological studies", "type": "ResearchActivity"}, {"text": "vegetables", "type": "Food"}, {"text": "cruciferous vegetables", "type": "Food"}, {"text": "Broccoli", "type": "Food"}, {"text": "Brussels sprouts", "type": "Food"}, {"text": "chronic diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Sulforaphane exposure prior to scopolamine significantly retained the memory of learned task .

Example answer:
{"entities": [{"text": "Sulforaphane", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "memory", "type": "BiologicFunction"}, {"text": "learned", "type": "BiologicFunction"}]}

Example input:
Sentence: Group V served as scopolamine ( 400 µM / L ) induced memory impairment fishes .

Example answer:
{"entities": [{"text": "scopolamine", "type": "Chemical"}, {"text": "memory impairment", "type": "BiologicFunction"}, {"text": "fishes", "type": "Eukaryote"}]}

Example input:
Sentence: There was no significant difference in cognition of group III and IV fishes exposed to sulforaphane and piracetam alone respectively .

Example answer:
{"entities": [{"text": "no significant", "type": "Finding"}, {"text": "cognition", "type": "BiologicFunction"}, {"text": "fishes", "type": "Eukaryote"}, {"text": "sulforaphane", "type": "Chemical"}, {"text": "piracetam", "type": "Chemical"}]}

Example input:
Sentence: Group I served as normal , group II served as fear conditioned control , group III and group IV were sulforaphane ( 25 µM / L ) and piracetam ( 200 mg / L ) treated respectively .

Example answer:
{"entities": [{"text": "fear conditioned control", "type": "BiologicFunction"}, {"text": "sulforaphane", "type": "Chemical"}, {"text": "piracetam", "type": "Chemical"}]}

Input:
Sentence: Group VI and VII were sulforaphane ( 25 µM / L ) and piracetam ( 200 mg / L ) treated scopolamine induced memory impairment groups respectively .

## Item MedMentions:test:184
Example input:
Sentence: 9 ; 95 % confidence interval [ CI ] : -8 . 8 to -0 . 9 ) as well as a decreased Cl / F ( MD : -4 . 0 ; 95 % CI : -8 . 9 to -0 . 03 ) Ob / ob compared with WT mice had a large increase in morphine exposure with a greater AUC150 ( MD : 980 . 4 ; 95 % CI : 630 . 1 - 1330 . 6 ) , CMAX ( MD : 6 . 8 ; 95 % CI : 2 . 7 - 10 . 9 ) , and longer T1 / 2 ( MD : 23 . 1 ; 95 % CI : 10 . 5 - 35 . 6 ) , as well as a decreased Cl / F ( MD : -7 . 0 ; 95 % CI : -11 . 6 to -2 . 7 ) .

Example answer:
{"entities": [{"text": "Cl / F", "type": "ClinicalAttribute"}, {"text": "Ob / ob", "type": "Eukaryote"}, {"text": "WT mice", "type": "Eukaryote"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Compared with the OBD ( - ) s group , the OBD ( + ) s group had significantly more inhibited temperament traits , less flexibility , more negative mood , and less regular rhythm in their daily routines .

Example answer:
{"entities": [{"text": "OBD ( + ) s", "type": "BiologicFunction"}, {"text": "temperament", "type": "BiologicFunction"}, {"text": "negative", "type": "Finding"}, {"text": "mood", "type": "BiologicFunction"}, {"text": "rhythm", "type": "Finding"}]}

Example input:
Sentence: Bias varied across quintiles with overestimation of UNa at lower quintiles ( by 29 - 105 % ) and underestimation at higher quintile ( by 7 - 37 % ) regardless of formula .

Example answer:
{"entities": [{"text": "formula", "type": "IntellectualProduct"}]}

Example input:
Sentence: Within the OBD ( + ) s group , a more inhibited temperament was associated with smaller right hippocampal volumes .

Example answer:
{"entities": [{"text": "OBD ( + ) s", "type": "BiologicFunction"}, {"text": "temperament", "type": "BiologicFunction"}, {"text": "right", "type": "SpatialConcept"}, {"text": "hippocampal", "type": "AnatomicalStructure"}]}

Example input:
Sentence: All regression coefficients were negative , implying that the more the surrogate overestimated quality of life compared to the older adult , the more he or she overestimated the older adult ' s desire to be treated .

Example answer:
{"entities": [{"text": "negative", "type": "Finding"}, {"text": "older adult", "type": "PopulationGroup"}]}

Example input:
Sentence: There was a significant difference in N / L and P / L between idiopathic AAU and control groups ( P = 0 . 006 , P = 0 . 022 ) .

Example answer:
{"entities": [{"text": "N", "type": "AnatomicalStructure"}, {"text": "L", "type": "AnatomicalStructure"}, {"text": "P", "type": "AnatomicalStructure"}, {"text": "AAU", "type": "BiologicFunction"}]}

Example input:
Sentence: We also found that allele ' C ' of rs11030096 was associated with an increased risk of addiction in the dominant model and additive model ( p < 0 .

Example answer:
{"entities": [{"text": "allele ' C", "type": "AnatomicalStructure"}, {"text": "rs11030096", "type": "AnatomicalStructure"}, {"text": "addiction", "type": "BiologicFunction"}, {"text": "dominant model", "type": "IntellectualProduct"}, {"text": "additive model", "type": "IntellectualProduct"}]}

Example input:
Sentence: However , some of the abnormalities in regions also implicated in addiction tend to persist following discontinuation of the overused medication , suggesting that they are a brain trait that predisposes certain individuals to medication overuse and MOH .

Example answer:
{"entities": [{"text": "abnormalities", "type": "Finding"}, {"text": "addiction", "type": "BiologicFunction"}, {"text": "discontinuation", "type": "HealthCareActivity"}, {"text": "medication", "type": "HealthCareActivity"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "MOH", "type": "BiologicFunction"}]}

Example input:
Sentence: 30 drug addicts were selected , and 30 non - addict individuals were selected as the control group .

Example answer:
{"entities": [{"text": "drug addicts", "type": "Finding"}, {"text": "non - addict individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: There was a significant difference between the addicts group and the control group regarding the error of time reproduction and time estimation .

Example answer:
{"entities": [{"text": "reproduction", "type": "BiologicFunction"}]}

Input:
Sentence: The addict group in comparison to the control group had a lower under - reproduction and a higher over - reproduction error , and also a lower under - estimation and higher over - estimation error .

## Item MedMentions:test:448
Example input:
Sentence: Within group comparison : The percentage of CD4 + in the two groups was significantly reduced at 24 hours post - operation ( T2 ) compared with the percentage before surgery , whereas the percentage of CD8 + was higher at T2 .

Example answer:
{"entities": [{"text": "percentage of CD4 +", "type": "HealthCareActivity"}, {"text": "percentage", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "percentage of CD8 + was higher", "type": "Finding"}]}

Example input:
Sentence: Patient - controlled analgesia IV morphine consumption 0 to 24 hours postoperatively was significantly reduced in the ketamine group compared with the placebo group : 79 ( 47 ) vs 121 ( 53 ) mg IV , mean difference 42 mg ( 95 % confidence interval -59 to -25 ) , P < 0 . 001 .

Example answer:
{"entities": [{"text": "Patient - controlled analgesia", "type": "HealthCareActivity"}, {"text": "morphine", "type": "Chemical"}, {"text": "ketamine", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: On univariate analysis more relapsers had significantly higher NSAIDs use within 15 days of relapse , respiratory tract infection within 4 weeks , use of steroids more than once in past , higher consumption of calcium , riboflavin , vitamin A and lower consumption of sugars .

Example answer:
{"entities": [{"text": "NSAIDs", "type": "Chemical"}, {"text": "respiratory tract infection", "type": "BiologicFunction"}, {"text": "steroids", "type": "Chemical"}, {"text": "consumption", "type": "BiologicFunction"}, {"text": "calcium", "type": "Chemical"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "vitamin A", "type": "Chemical"}, {"text": "sugars", "type": "Chemical"}]}

Example input:
Sentence: Perioperative medication use of nonsteroidal anti - inflammatory drugs ( NSAIDs ) ( OR , 1 . 33 ; 95 % CI , 1 .

Example answer:
{"entities": [{"text": "nonsteroidal anti - inflammatory drugs", "type": "Chemical"}, {"text": "NSAIDs", "type": "Chemical"}]}

Example input:
Sentence: In group I , T - SH , NGAL and urea levels were found to be significantly increased postoperatively compared to preoperative measurements ( p < 0 .

Example answer:
{"entities": [{"text": "T - SH", "type": "Chemical"}, {"text": "NGAL", "type": "Chemical"}, {"text": "urea levels", "type": "Finding"}]}

Example input:
Sentence: Patients in the control group needed longer post - operative ventilation time compared to the RIPC group ( 35 . 02 ± 6 .

Example answer:
{"entities": [{"text": "ventilation time", "type": "Finding"}, {"text": "RIPC", "type": "HealthCareActivity"}]}

Example input:
Sentence: Sedation was significantly reduced in the ketamine group 6 and 24 hours postoperatively .

Example answer:
{"entities": [{"text": "Sedation", "type": "Finding"}, {"text": "ketamine", "type": "Chemical"}]}

Example input:
Sentence: Pain , discomfort , and sedation scores , cumulative tramadol consumption , supplemental meperidine requirement , and side effects were recorded .

Example answer:
{"entities": [{"text": "Pain", "type": "Finding"}, {"text": "discomfort", "type": "Finding"}, {"text": "sedation", "type": "Finding"}, {"text": "tramadol", "type": "Chemical"}, {"text": "meperidine", "type": "Chemical"}, {"text": "side effects", "type": "BiologicFunction"}]}

Example input:
Sentence: Also , postoperatively , NGAL , creatinine , aspartate aminotransferase and AOPP levels were higher in group I than group II ( p < 0 .

Example answer:
{"entities": [{"text": "NGAL", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "aspartate aminotransferase", "type": "Chemical"}, {"text": "AOPP", "type": "Chemical"}]}

Example input:
Sentence: Increased odds of revision surgery among active - duty personnel were associated with the perioperative use of NSAIDs and COX - 2 inhibitors .

Example answer:
{"entities": [{"text": "revision surgery", "type": "HealthCareActivity"}, {"text": "active - duty", "type": "ProfessionalOrOccupationalGroup"}, {"text": "personnel", "type": "PopulationGroup"}, {"text": "NSAIDs", "type": "Chemical"}, {"text": "COX - 2 inhibitors", "type": "Chemical"}]}

Input:
Sentence: Supplemental meperidine requirement was significantly higher in group S at each study period after postoperative 30 min than in NSAID - treated groups ( p < 0 .

## Item MedMentions:test:536
Example input:
Sentence: Median PFS and DCR of CG group were 22 weeks and 56 . 6 % , and these were 12 weeks and 44 . 4 % for CF group , and 9 weeks and 41 .

Example answer:
{"entities": [{"text": "CG", "type": "Chemical"}, {"text": "group", "type": "PopulationGroup"}, {"text": "CF", "type": "Chemical"}]}

Example input:
Sentence: monocytogenes L12 strain ( 4 - log CFU / mL ) during storage at 4°C for one week .

Example answer:
{"entities": [{"text": "monocytogenes L12 strain", "type": "Bacterium"}]}

Example input:
Sentence: 0 × 10 ( 5 ) CFU ml ( - 1 ) 22 - 54 % quicker than commercially available resorufin glycosides .

Example answer:
{"entities": [{"text": "resorufin", "type": "Chemical"}, {"text": "glycosides", "type": "Chemical"}]}

Example input:
Sentence: The achievement of primary composite outcome ( four out of seven fasting plasma glucose [ FPG ] within 5 - 7 . 2 mmol / L + mean for three consecutive FPG within 5 - 7 . 2 mmol / L + no severe hypoglycemia ) was 15 % in LTHome versus 41 % in EUT ( noninferiority not met , P - value = 0 . 92 ) .

Example answer:
{"entities": [{"text": "fasting plasma glucose [ FPG ]", "type": "Finding"}, {"text": "FPG", "type": "Finding"}, {"text": "no", "type": "Finding"}, {"text": "hypoglycemia", "type": "BiologicFunction"}, {"text": "LTHome", "type": "IntellectualProduct"}, {"text": "EUT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Median OS of CG , CF , and FOLFIRINOX groups was 28 , 21 , and 23 . 5 weeks , respectively ( p = 0 . 497 ) .

Example answer:
{"entities": [{"text": "CG", "type": "Chemical"}, {"text": "CF", "type": "Chemical"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: 3μg / mL versus 42 . 1μg / mL ; the ratio of FDP to fibrinogen , 3 . 39 versus 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 25log CFU / g , while in the peel led to a κ value of 4 . 6±0 .

Example answer:
{"entities": [{"text": "peel", "type": "Food"}]}

Example input:
Sentence: 23log CFU / g ( p < 0 . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 25log CFU / g and 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 06log CFU / g and 2 . 9±0 .

Example answer:
{"entities": []}

Input:
Sentence: 05log CFU / g , respectively .

## Item MedMentions:test:142
Example input:
Sentence: Complete viral genome sequences were obtained from HAV samples of varying purities and with an input as low as 2ng total RNA containing 1 .

Example answer:
{"entities": [{"text": "viral genome", "type": "AnatomicalStructure"}, {"text": "sequences", "type": "SpatialConcept"}, {"text": "HAV", "type": "Virus"}, {"text": "RNA", "type": "Chemical"}]}

Example input:
Sentence: Unlike other organisms , viruses can have four different genome types ( double - or single - stranded RNA or DNA ) , and the viruses studied herein represent all four types .

Example answer:
{"entities": [{"text": "viruses", "type": "Virus"}, {"text": "genome types", "type": "AnatomicalStructure"}, {"text": "single - stranded RNA", "type": "Chemical"}, {"text": "DNA", "type": "Chemical"}]}

Example input:
Sentence: Overall , this study allows us to better understand the behavior of viruses in HEAM .

Example answer:
{"entities": [{"text": "viruses", "type": "Virus"}, {"text": "HEAM", "type": "BodySubstance"}]}

Example input:
Sentence: DNA and dsRNA viruses were considerably more resistant than ssRNA viruses , resulting in up to 1 , 000 - fold - longer treatment times to reach a 4 - log inactivation .

Example answer:
{"entities": [{"text": "DNA", "type": "Chemical"}, {"text": "dsRNA", "type": "Chemical"}, {"text": "viruses", "type": "Virus"}, {"text": "ssRNA viruses", "type": "Virus"}]}

Example input:
Sentence: In contrast , the other genome types are more stable ; therefore , inactivation is slower and mainly driven by the degradation of viral proteins .

Example answer:
{"entities": [{"text": "genome types", "type": "AnatomicalStructure"}, {"text": "viral proteins", "type": "Chemical"}]}

Example input:
Sentence: Ammonia as an In Situ Sanitizer : Influence of Virus Genome Type on Inactivation Treatment of human excreta and animal manure ( HEAM ) is key in controlling the spread of persistent enteric pathogens , such as viruses .

Example answer:
{"entities": [{"text": "Ammonia", "type": "Chemical"}, {"text": "In Situ", "type": "SpatialConcept"}, {"text": "Virus", "type": "Virus"}, {"text": "Genome Type", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "excreta", "type": "BodySubstance"}, {"text": "animal", "type": "Eukaryote"}, {"text": "HEAM", "type": "BodySubstance"}, {"text": "enteric", "type": "SpatialConcept"}, {"text": "viruses", "type": "Virus"}]}

Example input:
Sentence: Using an Illumina MiSeq platform and two hepatitis A virus ( HAV ) cell - culture adapted strains as a representative enteric virus species , this study examined the limits of single - stranded RNA ( ssRNA ) viral detection following next - generation sequencing without pre - amplification of the viral genome .

Example answer:
{"entities": [{"text": "Illumina MiSeq platform", "type": "IntellectualProduct"}, {"text": "hepatitis A virus", "type": "Virus"}, {"text": "HAV", "type": "Virus"}, {"text": "cell - culture", "type": "HealthCareActivity"}, {"text": "virus", "type": "Virus"}, {"text": "study", "type": "ResearchActivity"}, {"text": "single - stranded RNA", "type": "Chemical"}, {"text": "ssRNA", "type": "Chemical"}, {"text": "viral detection", "type": "HealthCareActivity"}, {"text": "next - generation sequencing", "type": "ResearchActivity"}, {"text": "pre - amplification", "type": "BiologicFunction"}, {"text": "viral genome", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Specifically , eight viruses representing the four viral genome types ( single - stranded RNA [ ssRNA ] , double - stranded RNA [ dsRNA ] , single - stranded DNA [ ssDNA ] , and double - stranded DNA [ dsDNA ] ) were exposed to synthetic solutions with well - controlled temperature ( 20 to 35°C ) , pH ( 8 to 9 ) , and ammonia ( NH3 ) concentrations ( 0 to 40 mmol liter ( - 1 ) ) .

Example answer:
{"entities": [{"text": "viruses", "type": "Virus"}, {"text": "viral genome types", "type": "AnatomicalStructure"}, {"text": "single - stranded RNA", "type": "Chemical"}, {"text": "ssRNA", "type": "Chemical"}, {"text": "double - stranded RNA", "type": "Chemical"}, {"text": "dsRNA", "type": "Chemical"}, {"text": "single - stranded DNA", "type": "Chemical"}, {"text": "ssDNA", "type": "Chemical"}, {"text": "double - stranded DNA", "type": "Chemical"}, {"text": "dsDNA", "type": "Chemical"}, {"text": "ammonia", "type": "Chemical"}, {"text": "NH3", "type": "Chemical"}]}

Example input:
Sentence: The apparently slower inactivation of DNA viruses was rationalized by the higher stability of DNA than that of ssRNA in HEAM .

Example answer:
{"entities": [{"text": "DNA viruses", "type": "Virus"}, {"text": "stability", "type": "HealthCareActivity"}, {"text": "DNA", "type": "Chemical"}, {"text": "ssRNA", "type": "Chemical"}, {"text": "HEAM", "type": "BodySubstance"}]}

Example input:
Sentence: Here , we investigated the inactivation of viruses of different genome types under conditions representative of HEAM storage or mesophilic digestion .

Example answer:
{"entities": [{"text": "viruses", "type": "Virus"}, {"text": "genome types", "type": "AnatomicalStructure"}, {"text": "HEAM", "type": "BodySubstance"}, {"text": "digestion", "type": "BiologicFunction"}]}

Input:
Sentence: Single - stranded RNA viruses are the most labile , because this genome type is susceptible to degradation in HEAM .

## Item MedMentions:test:145
Example input:
Sentence: Proliferation -Related Activity in Endothelial Cells Is Enhanced by Micropower Plasma Nonthermal plasma has received a lot of attention as a medical treatment technique in recent years .

Example answer:
{"entities": [{"text": "Proliferation", "type": "BiologicFunction"}, {"text": "Endothelial Cells", "type": "AnatomicalStructure"}, {"text": "Plasma", "type": "Chemical"}, {"text": "Nonthermal plasma", "type": "HealthCareActivity"}]}

Example input:
Sentence: Molecular targeted therapies in adrenal , pituitary and parathyroid malignancies Tumourigenesis is a relatively common event in endocrine tissues .

Example answer:
{"entities": [{"text": "Molecular targeted therapies", "type": "HealthCareActivity"}, {"text": "adrenal", "type": "BiologicFunction"}, {"text": "pituitary", "type": "BiologicFunction"}, {"text": "parathyroid malignancies", "type": "BiologicFunction"}, {"text": "Tumourigenesis", "type": "BiologicFunction"}, {"text": "endocrine tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We propose that HsaD is a novel therapeutic target , which should be fully exploited in order to design and discover new anti - tubercular drugs .

Example answer:
{"entities": [{"text": "HsaD", "type": "Chemical"}, {"text": "anti - tubercular drugs", "type": "Chemical"}]}

Example input:
Sentence: Fenretinide targets the side population in myeloma cell line NCI - H929 and potentiates the efficacy of antimyeloma with bortezomib and dexamethasone regimen Side population ( SP ) cells , a subset of enriched tumor initiating cells , have been demonstrated to have stem cell -like properties in multiple myeloma ( MM ) by us as well as other previous studies .

Example answer:
{"entities": [{"text": "Fenretinide", "type": "Chemical"}, {"text": "side population", "type": "AnatomicalStructure"}, {"text": "myeloma cell line NCI - H929", "type": "AnatomicalStructure"}, {"text": "antimyeloma", "type": "Finding"}, {"text": "bortezomib and dexamethasone regimen", "type": "HealthCareActivity"}, {"text": "Side population ( SP ) cells", "type": "AnatomicalStructure"}, {"text": "tumor initiating cells", "type": "AnatomicalStructure"}, {"text": "stem cell", "type": "AnatomicalStructure"}, {"text": "multiple myeloma", "type": "BiologicFunction"}, {"text": "MM", "type": "BiologicFunction"}]}

Example input:
Sentence: Biomimetic biodegradable artificial antigen presenting cells synergize with PD - 1 blockade to treat melanoma Biomimetic materials that target the immune system and generate an anti - tumor responses hold promise in augmenting cancer immunotherapy .

Example answer:
{"entities": [{"text": "antigen presenting cells", "type": "AnatomicalStructure"}, {"text": "PD - 1 blockade", "type": "Chemical"}, {"text": "melanoma", "type": "BiologicFunction"}, {"text": "immune system", "type": "BodySystem"}, {"text": "anti - tumor responses", "type": "BiologicFunction"}, {"text": "cancer immunotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: We previously described a novel treatment using a suboptimal dose of anti - CD40 ligand ( anti - CD40L ) and liposomal formulation of a ligand for invariant natural killer T cells administered to sub - lethally irradiated recipient mice after donor bone marrow cell ( BMC ) transfer .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "anti - CD40 ligand", "type": "Chemical"}, {"text": "anti - CD40L", "type": "Chemical"}, {"text": "liposomal", "type": "Chemical"}, {"text": "formulation", "type": "Chemical"}, {"text": "invariant natural killer T cells", "type": "AnatomicalStructure"}, {"text": "sub - lethally", "type": "Finding"}, {"text": "recipient mice", "type": "Eukaryote"}, {"text": "donor", "type": "PopulationGroup"}, {"text": "bone marrow cell", "type": "AnatomicalStructure"}, {"text": "BMC", "type": "AnatomicalStructure"}, {"text": "transfer", "type": "HealthCareActivity"}]}

Example input:
Sentence: Currently , application of IGF - IR -targeting monoclonal antibodies ( mAbs ) , alone or in combination with other drugs , is a promising strategy for breast cancer therapy .

Example answer:
{"entities": [{"text": "IGF - IR", "type": "Chemical"}, {"text": "monoclonal antibodies", "type": "Chemical"}, {"text": "mAbs", "type": "Chemical"}, {"text": "drugs", "type": "Chemical"}, {"text": "promising strategy", "type": "ResearchActivity"}, {"text": "breast cancer therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Overall our data reveal the LR axis as novel therapeutic target for checkpoint inhibition to treat MM .Leukemia accepted article preview online , 11 May 2017 .

Example answer:
{"entities": [{"text": "LR", "type": "Chemical"}, {"text": "checkpoint inhibition", "type": "BiologicFunction"}, {"text": "MM", "type": "BiologicFunction"}]}

Example input:
Sentence: Plasma cells remain a difficult therapeutic target , but inhibition of germinal centre responses via costimulatory blockade or IL21 neutralization , induction of plasma cell apoptosis using proteasome inhibitors or disruption of the plasma cell niche are potential avenues being explored .

Example answer:
{"entities": [{"text": "Plasma cells", "type": "AnatomicalStructure"}, {"text": "therapeutic", "type": "HealthCareActivity"}, {"text": "germinal centre", "type": "AnatomicalStructure"}, {"text": "IL21", "type": "Chemical"}, {"text": "plasma cell", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "proteasome inhibitors", "type": "Chemical"}]}

Example input:
Sentence: Novel immunotherapeutic strategies to target alloantibody -producing B and plasma cells in transplantation There is an unmet need for immunotherapeutic agents that target humoral alloimmunity in solid organ transplantation .

Example answer:
{"entities": [{"text": "immunotherapeutic strategies", "type": "HealthCareActivity"}, {"text": "alloantibody", "type": "Chemical"}, {"text": "B", "type": "AnatomicalStructure"}, {"text": "plasma cells", "type": "AnatomicalStructure"}, {"text": "transplantation", "type": "HealthCareActivity"}, {"text": "immunotherapeutic agents", "type": "Chemical"}, {"text": "solid organ transplantation", "type": "HealthCareActivity"}]}

Input:
Sentence: In this review , we discuss recent progress in the generation of B - cell and plasma cell -targeted therapeutics , with an emphasis on novel agents .

## Item MedMentions:test:153
Example input:
Sentence: Through impoverishment expenditure assessment , the proportions of impoverishment payment are low among both urban and rural residents , but the 7 rare diseases could lead nearly 4 . 6 million people into poverty on a national scale .

Example answer:
{"entities": [{"text": "urban", "type": "PopulationGroup"}, {"text": "rural residents", "type": "PopulationGroup"}, {"text": "rare diseases", "type": "BiologicFunction"}, {"text": "people", "type": "PopulationGroup"}]}

Example input:
Sentence: In the pediatric population , SS is an extremely rare head & neck malignancy .

Example answer:
{"entities": [{"text": "population", "type": "PopulationGroup"}, {"text": "SS", "type": "BiologicFunction"}, {"text": "head & neck malignancy", "type": "BiologicFunction"}]}

Example input:
Sentence: RSTS is a rare , neurodevelopmental genetic disease where most patients with disabilities survive into adulthood .

Example answer:
{"entities": [{"text": "RSTS", "type": "BiologicFunction"}, {"text": "neurodevelopmental", "type": "BiologicFunction"}, {"text": "genetic disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Aside from generating billions of additional needed revenues from the private sector , it could ( 1 ) help eliminate long waits for non - emergent physicians ' care by appointing newly minted specialists to their medical staffs ; ( 2 ) offer prompt admissions for elective cases to " private " wings of hospitals ; ( 3 ) increase available funding for what is currently an undercapitalized system ; ( 4 ) enhance the system 's sluggish operations ; and ( 5 ) encourage more competition among various providers .

Example answer:
{"entities": [{"text": "private sector", "type": "PopulationGroup"}, {"text": "specialists", "type": "ProfessionalOrOccupationalGroup"}, {"text": "medical staffs", "type": "ProfessionalOrOccupationalGroup"}, {"text": "admissions", "type": "HealthCareActivity"}, {"text": "elective cases", "type": "Finding"}, {"text": "private", "type": "Organization"}, {"text": "wings of hospitals", "type": "Organization"}, {"text": "undercapitalized", "type": "Finding"}, {"text": "sluggish", "type": "Finding"}]}

Example input:
Sentence: Investments in children 's health and the Kenyan cash transfer for orphans and vulnerable children : evidence from an unconditional cash transfer scheme Child mortality is one of the most pressing global health and policy issues in the developing world .

Example answer:
{"entities": [{"text": "orphans", "type": "PopulationGroup"}, {"text": "global health", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "policy", "type": "IntellectualProduct"}, {"text": "issues", "type": "IntellectualProduct"}]}

Example input:
Sentence: Causal and maintaining mechanisms for SA in ASD are underexplored , but it is feasible that there is an ASD specificity to the clinical presentation , with implications for the development of targeted treatments .

Example answer:
{"entities": [{"text": "SA", "type": "BiologicFunction"}, {"text": "ASD", "type": "BiologicFunction"}, {"text": "underexplored", "type": "Finding"}, {"text": "treatments", "type": "HealthCareActivity"}]}

Example input:
Sentence: Residents of different income levels all have difficulties to afford the treatment for rare diseases , so poverty caused by rare diseases is quite widespread .

Example answer:
{"entities": [{"text": "Residents", "type": "PopulationGroup"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "rare diseases", "type": "BiologicFunction"}, {"text": "widespread", "type": "SpatialConcept"}]}

Example input:
Sentence: Despite advances in the regulation and incorporation of technologies by the SUS , given the lack of market interest and neglect of diseases of poverty , the government has a vital role to play in ensuring access to the best available therapies in order to reduce health inequalities .

Example answer:
{"entities": [{"text": "technologies", "type": "HealthCareActivity"}, {"text": "SUS", "type": "Organization"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "government", "type": "Organization"}, {"text": "therapies", "type": "HealthCareActivity"}]}

Example input:
Sentence: Affordability of treatment for the 7 rare diseases was assessed through annual per capital income , catastrophic expenditure and impoverishment expenditure among urban and rural residents in China .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "rare diseases", "type": "BiologicFunction"}, {"text": "urban", "type": "PopulationGroup"}, {"text": "rural residents", "type": "PopulationGroup"}, {"text": "China", "type": "SpatialConcept"}]}

Example input:
Sentence: This study aims to provide policy recommendations for the establishment of social security mechanism for rare diseases in China , so as to address the problem of poverty caused by these diseases .

Example answer:
{"entities": [{"text": "policy", "type": "IntellectualProduct"}, {"text": "social security mechanism", "type": "IntellectualProduct"}, {"text": "rare diseases", "type": "BiologicFunction"}, {"text": "China", "type": "SpatialConcept"}, {"text": "diseases", "type": "BiologicFunction"}]}

Input:
Sentence: Therefore , social security mechanism for rare disease patients should be established and specific payment pattern for orphan drugs should be set up .

## Item MedMentions:test:168
Example input:
Sentence: The primary outcome was proportion of subjects without treatment failure ( regimen switch or VL > 200 copies / mL twice consecutively ) at 48 weeks .

Example answer:
{"entities": [{"text": "subjects", "type": "PopulationGroup"}, {"text": "treatment failure", "type": "Finding"}, {"text": "regimen", "type": "HealthCareActivity"}]}

Example input:
Sentence: Outcomes included mean change from baseline to end of treatment ( EOT ) in CSFQ total score and percentage of patients shifting from SD at baseline ( CSFQ total score ≤47 for males , ≤41 for females ) to normal functioning at EOT .

Example answer:
{"entities": [{"text": "Outcomes", "type": "ResearchActivity"}, {"text": "CSFQ total score", "type": "Finding"}, {"text": "SD", "type": "BiologicFunction"}, {"text": "males", "type": "PopulationGroup"}, {"text": "females", "type": "PopulationGroup"}]}

Example input:
Sentence: Changes in clinical measures ( near point of convergence , positive fusional vergence at near , Convergence Insufficiency Symptom Survey [ CISS ] score ) were evaluated .

Example answer:
{"entities": [{"text": "clinical measures", "type": "Finding"}, {"text": "near point of convergence", "type": "BiologicFunction"}, {"text": "positive", "type": "Finding"}, {"text": "fusional vergence at near", "type": "BiologicFunction"}, {"text": "Convergence Insufficiency Symptom Survey", "type": "IntellectualProduct"}, {"text": "CISS", "type": "IntellectualProduct"}, {"text": "evaluated", "type": "HealthCareActivity"}]}

Example input:
Sentence: The ADAS - cog , MMSE and WHO - UCLA AVLT score in the rTMS group was significantly improved compared with baselines at 6 weeks after treatment ( all p < 0 . 05 ) .

Example answer:
{"entities": [{"text": "ADAS", "type": "IntellectualProduct"}, {"text": "cog", "type": "IntellectualProduct"}, {"text": "MMSE", "type": "HealthCareActivity"}, {"text": "WHO - UCLA AVLT", "type": "IntellectualProduct"}, {"text": "rTMS", "type": "HealthCareActivity"}, {"text": "group", "type": "PopulationGroup"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The primary outcome was the alleviation of depressive symptoms , as measured by change in the total GRID - HDRS₁₇ score from baseline to 16 weeks ; primary analysis was done on an intention - to - treat basis .

Example answer:
{"entities": [{"text": "depressive symptoms", "type": "Finding"}, {"text": "GRID - HDRS₁₇", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: The primary efficacy endpoint was met ; the difference in least squares mean change from baseline to day 42 in PANSS total score between asenapine 5 mg bid and placebo was -5 .

Example answer:
{"entities": [{"text": "PANSS total score", "type": "IntellectualProduct"}, {"text": "placebo", "type": "HealthCareActivity"}]}

Example input:
Sentence: The primary end point was the 2 - year progression - free survival ( PFS ) after the protocol treatment .

Example answer:
{"entities": [{"text": "protocol treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The primary endpoint was cumulative response ( ≥75 % improvement from baseline within weeks 8 - 24 ) in at least one severe baseline symptom from the following : pruritus score of 9 or more , eight or more flushes per week , Hamilton Rating Scale for Depression of 19 or more , or Fatigue Impact Scale of 75 or more .

Example answer:
{"entities": [{"text": "primary endpoint", "type": "Chemical"}, {"text": "response", "type": "ClinicalAttribute"}, {"text": "severe baseline symptom", "type": "Finding"}, {"text": "pruritus", "type": "Finding"}, {"text": "Hamilton Rating Scale for Depression", "type": "IntellectualProduct"}, {"text": "Fatigue Impact Scale", "type": "IntellectualProduct"}]}

Example input:
Sentence: Patients ' symptomatology was assessed by means of the Positive and Negative Syndrome Scale ( PANSS ) .

Example answer:
{"entities": [{"text": "symptomatology", "type": "Finding"}, {"text": "Positive and Negative Syndrome Scale", "type": "IntellectualProduct"}, {"text": "PANSS", "type": "IntellectualProduct"}]}

Example input:
Sentence: The results of secondary endpoints including PANSS negative subscale scores and PANSS responders at the end of treatment supported the results of the primary endpoint .

Example answer:
{"entities": [{"text": "PANSS", "type": "IntellectualProduct"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "primary endpoint", "type": "Chemical"}]}

Input:
Sentence: The primary endpoint was the mean change in the positive and negative syndrome scale ( PANSS ) total score from baseline to day 42 / treatment end .
