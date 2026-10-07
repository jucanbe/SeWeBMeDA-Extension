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

## Item MedMentions:test:627
Example input:
Sentence: Head / neck and oropharynx pathologies accounted for 24 . 5 % of cases ( hr : 16 / 100 000 and 3 . 9 / 100 000 , in males and females , respectively ) , followed by genital warts ( 17 . 3 % of hospitalizations ; hr : 7 . 5 / 100 000 in males and 8 . 52 / 100 000 in females ) , anal ( 8 .

Example answer:
{"entities": [{"text": "Head", "type": "SpatialConcept"}, {"text": "neck", "type": "SpatialConcept"}, {"text": "oropharynx", "type": "SpatialConcept"}, {"text": "hospitalizations", "type": "HealthCareActivity"}, {"text": "anal", "type": "BiologicFunction"}]}

Example input:
Sentence: 9 % of cases were males .

Example answer:
{"entities": []}

Example input:
Sentence: 4 % ) , and bilateral complete occlusion in 1 ( 1 . 8 % ) .

Example answer:
{"entities": [{"text": "bilateral", "type": "SpatialConcept"}, {"text": "complete occlusion", "type": "BiologicFunction"}]}

Example input:
Sentence: The patient group consisted of 50 ( 52 . 6 % ) boys and 45 ( 47 . 4 % ) girls with a mean age of 125 ±38 months old .

Example answer:
{"entities": []}

Example input:
Sentence: Eyelid injuries occurred in 227 ( 99 % ) of children , 47 ( 20 % ) sustained canalicular system injuries , 3 ( 1 . 3 % ) suffered corneal abrasions , and 2 patients sustained facial nerve injury resulting in lagophthalmos .

Example answer:
{"entities": [{"text": "Eyelid injuries", "type": "InjuryOrPoisoning"}, {"text": "canalicular system", "type": "BodySystem"}, {"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "suffered", "type": "BiologicFunction"}, {"text": "corneal abrasions", "type": "InjuryOrPoisoning"}, {"text": "facial", "type": "SpatialConcept"}, {"text": "nerve injury", "type": "InjuryOrPoisoning"}, {"text": "lagophthalmos", "type": "BiologicFunction"}]}

Example input:
Sentence: The main comorbidities were high myopia in 18 eyes ( 26 . 1 % ) , trauma in 8 eyes ( 11 . 6 % ) , retinal detachment in 6 eyes ( 8 . 7 % ) , congenital cataracts in 8 eyes ( 11 . 6 % ) , and Marfan 's syndrome in 2 eyes ( 2 . 9 % ) .

Example answer:
{"entities": [{"text": "high myopia", "type": "BiologicFunction"}, {"text": "eyes", "type": "AnatomicalStructure"}, {"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "retinal detachment", "type": "BiologicFunction"}, {"text": "congenital cataracts", "type": "AnatomicalStructure"}, {"text": "Marfan 's syndrome", "type": "BiologicFunction"}]}

Example input:
Sentence: Among the patients , 5 % were boys and 46 % girls .

Example answer:
{"entities": []}

Example input:
Sentence: Incidence of environmental and genetic factors causing congenital cataract in Children of Lahore To check the incidence of environmental and genetic factors causing congenital cataract in infants .

Example answer:
{"entities": [{"text": "congenital cataract", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Bilateral congenital cataract was observed in 91 ( 75 . 83 % ) patients and unilateral congenital cataract in 29 ( 24 . 17 % ) .

Example answer:
{"entities": [{"text": "Bilateral congenital cataract", "type": "BiologicFunction"}, {"text": "unilateral congenital cataract", "type": "BiologicFunction"}]}

Example input:
Sentence: 3 % ) patients were diagnosed with congenital cataract .

Example answer:
{"entities": [{"text": "diagnosed", "type": "Finding"}, {"text": "congenital cataract", "type": "AnatomicalStructure"}]}

Input:
Sentence: 93 % ) .. Congenital cataract predominated in boys compared to girls .

## Item MedMentions:test:731
Example input:
Sentence: Although no significant difference was observed in image noise , the signal - to - noise ratio was significantly higher with FIRST ( 18 . 4 vs . 16 .

Example answer:
{"entities": [{"text": "FIRST", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using computer simulations , we demonstrate that this approach detects selection with higher power than several state - of - the - art single - marker , windowing or haplotype -based approaches .

Example answer:
{"entities": [{"text": "detects", "type": "Finding"}, {"text": "selection", "type": "BiologicFunction"}, {"text": "single - marker", "type": "BiologicFunction"}]}

Example input:
Sentence: 1 for both scales . Multi - layer perceptron ( MLP ) obtains the best values , but is less consistent than the random forest ( RF ) method .

Example answer:
{"entities": [{"text": "Multi - layer perceptron", "type": "IntellectualProduct"}, {"text": "MLP", "type": "IntellectualProduct"}, {"text": "random forest ( RF ) method", "type": "IntellectualProduct"}]}

Example input:
Sentence: Our approach , including statistical background removal , could be directly generalised to broader spectral ranges , for example , to resolve tissue reflectance or autofluorescence and in future be tailored to video rate applications requiring snapshot HSI data acquisition .

Example answer:
{"entities": [{"text": "generalised", "type": "SpatialConcept"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "reflectance", "type": "HealthCareActivity"}, {"text": "autofluorescence", "type": "HealthCareActivity"}, {"text": "HSI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here , signal - to - noise ratio ( SNR ) comparisons between EPI and nCPMG SS - FSE acquisitions and reconstruction techniques give similar values .

Example answer:
{"entities": [{"text": "EPI", "type": "HealthCareActivity"}, {"text": "nCPMG", "type": "Finding"}, {"text": "SS - FSE", "type": "HealthCareActivity"}]}

Example input:
Sentence: Evaluations with modified dynamic XCAT phantom and preclinical porcine datasets have demonstrated that the proposed PWLS - ndiSTV approach can achieve promising gains over other existing approaches in terms of noise - induced artifacts mitigation , edge details preservation , and accurate MPHP maps calculation .

Example answer:
{"entities": [{"text": "preclinical porcine datasets", "type": "IntellectualProduct"}, {"text": "PWLS - ndiSTV", "type": "IntellectualProduct"}, {"text": "MPHP maps", "type": "HealthCareActivity"}]}

Example input:
Sentence: Results : Contrast - to - noise ratio was significantly better in BPL reconstructions when compared with OSEM in phantom studies .

Example answer:
{"entities": [{"text": "BPL", "type": "IntellectualProduct"}, {"text": "OSEM", "type": "IntellectualProduct"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: With the measurement of Mean Squared Error and Peak Signal to Noise Ratio obtained from different images , fuzzy methods provided better results , and their implementation - compared with histogram equalization method - led both to the improvement of contrast and visual quality of images and to the improvement of liver segmentation algorithms results in images .

Example answer:
{"entities": [{"text": "images", "type": "IntellectualProduct"}, {"text": "fuzzy", "type": "IntellectualProduct"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "histogram equalization method", "type": "IntellectualProduct"}, {"text": "visual quality", "type": "Finding"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "segmentation algorithms", "type": "IntellectualProduct"}]}

Example input:
Sentence: Imaging based on this property has shown a substantial contrast - to - noise ratio improvement ( up to 5 fold , p < 0 .

Example answer:
{"entities": [{"text": "Imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: In addition , the elastographic signal - to - noise ratio and the contrast - to - noise ratio are also significantly improved with this new method .

Example answer:
{"entities": []}

Input:
Sentence: Moreover , in comparison to other approaches , superior noise - resolution trade - offs can be found with the proposed methods .

## Item MedMentions:test:146
Example input:
Sentence: shRNA lentiviral -mediated targeting of either PI3Kδ or PI3Kγ alone , or both in combination , increased survival of NSG mice xeno - transplanted with MM cells .

Example answer:
{"entities": [{"text": "shRNA", "type": "Chemical"}, {"text": "lentiviral", "type": "Virus"}, {"text": "PI3Kδ", "type": "Chemical"}, {"text": "PI3Kγ", "type": "Chemical"}, {"text": "NSG mice", "type": "Eukaryote"}, {"text": "xeno - transplanted", "type": "Chemical"}, {"text": "MM", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Cell replacement therapy holds great promise as first animal studies using transplantation of neural stem cells to irradiated brain have been successful in restoring memory and cognition deficits .

Example answer:
{"entities": [{"text": "Cell replacement therapy", "type": "HealthCareActivity"}, {"text": "animal", "type": "Eukaryote"}, {"text": "transplantation", "type": "HealthCareActivity"}, {"text": "neural stem cells", "type": "AnatomicalStructure"}, {"text": "irradiated brain", "type": "AnatomicalStructure"}, {"text": "restoring", "type": "HealthCareActivity"}, {"text": "memory", "type": "BiologicFunction"}, {"text": "cognition deficits", "type": "BiologicFunction"}]}

Example input:
Sentence: Manipulation of niche factors influencing the distribution and maintenance of these critical antibody - secreting cells may serve as potential therapeutic targets to enhance antiviral responses postvaccination and postinfection .

Example answer:
{"entities": [{"text": "antibody - secreting cells", "type": "AnatomicalStructure"}, {"text": "antiviral responses", "type": "BiologicFunction"}]}

Example input:
Sentence: Our results demonstrate a novel therapeutic paradigm for residual cancer , in which multiple classes of allotransplant leukocytes can be armed by MYXV ex vivo to enhance the graft - versus - tumor effects .

Example answer:
{"entities": [{"text": "residual cancer", "type": "BiologicFunction"}, {"text": "allotransplant", "type": "HealthCareActivity"}, {"text": "leukocytes", "type": "AnatomicalStructure"}, {"text": "MYXV", "type": "Virus"}, {"text": "graft - versus - tumor effects", "type": "BiologicFunction"}]}

Example input:
Sentence: Anti - CD45RB and donor - specific spleen cells transfusion inhibition allograft skin rejection mediated by memory T cells Donor - reactive memory T ( Tm ) cells mediate accelerated rejection , which is known as a barrier to the survival of transplanted organs .

Example answer:
{"entities": [{"text": "Anti - CD45RB", "type": "Chemical"}, {"text": "allograft skin rejection", "type": "BiologicFunction"}, {"text": "memory T cells", "type": "AnatomicalStructure"}, {"text": "memory T ( Tm ) cells", "type": "AnatomicalStructure"}, {"text": "rejection", "type": "BiologicFunction"}, {"text": "transplanted organs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: As key antibody producers , plasma cells and plasmablasts are critical components of vaccine -induced immunity to human immunodeficiency virus type 1 ( HIV - 1 ) in humans and SIV in the macaque model ; however , few have attempted to examine the role of these cells in viral suppression postinfection .

Example answer:
{"entities": [{"text": "antibody", "type": "Chemical"}, {"text": "plasma cells", "type": "AnatomicalStructure"}, {"text": "plasmablasts", "type": "AnatomicalStructure"}, {"text": "vaccine", "type": "Chemical"}, {"text": "immunity", "type": "BiologicFunction"}, {"text": "human immunodeficiency virus type 1", "type": "Virus"}, {"text": "HIV - 1", "type": "Virus"}, {"text": "humans", "type": "Eukaryote"}, {"text": "SIV", "type": "Virus"}, {"text": "macaque model", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "viral suppression", "type": "Finding"}]}

Example input:
Sentence: Efficient genomic disruption of multiple gene loci to generate universal donor cells , as well as potent effector T cells resistant to multiple inhibitory pathways such as PD - 1 and CTLA4 is an attractive strategy for cell therapy .

Example answer:
{"entities": [{"text": "genomic", "type": "AnatomicalStructure"}, {"text": "gene loci", "type": "AnatomicalStructure"}, {"text": "donor cells", "type": "AnatomicalStructure"}, {"text": "effector T cells", "type": "AnatomicalStructure"}, {"text": "PD - 1", "type": "AnatomicalStructure"}, {"text": "CTLA4", "type": "AnatomicalStructure"}, {"text": "cell therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Current mAbs used in transplant directly target and destroy graft - destructive immune cells , interrupt cytokine and costimulation -dependent T and B cell activation , and prevent down - stream complement activation .

Example answer:
{"entities": [{"text": "mAbs", "type": "Chemical"}, {"text": "transplant", "type": "HealthCareActivity"}, {"text": "graft - destructive immune cells", "type": "AnatomicalStructure"}, {"text": "cytokine", "type": "Chemical"}, {"text": "costimulation", "type": "BiologicFunction"}, {"text": "T", "type": "BiologicFunction"}, {"text": "B cell activation", "type": "BiologicFunction"}, {"text": "down - stream complement activation", "type": "BiologicFunction"}]}

Example input:
Sentence: Plasma cells remain a difficult therapeutic target , but inhibition of germinal centre responses via costimulatory blockade or IL21 neutralization , induction of plasma cell apoptosis using proteasome inhibitors or disruption of the plasma cell niche are potential avenues being explored .

Example answer:
{"entities": [{"text": "Plasma cells", "type": "AnatomicalStructure"}, {"text": "therapeutic", "type": "HealthCareActivity"}, {"text": "germinal centre", "type": "AnatomicalStructure"}, {"text": "IL21", "type": "Chemical"}, {"text": "plasma cell", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "proteasome inhibitors", "type": "Chemical"}]}

Example input:
Sentence: Novel immunotherapeutic strategies to target alloantibody -producing B and plasma cells in transplantation There is an unmet need for immunotherapeutic agents that target humoral alloimmunity in solid organ transplantation .

Example answer:
{"entities": [{"text": "immunotherapeutic strategies", "type": "HealthCareActivity"}, {"text": "alloantibody", "type": "Chemical"}, {"text": "B", "type": "AnatomicalStructure"}, {"text": "plasma cells", "type": "AnatomicalStructure"}, {"text": "transplantation", "type": "HealthCareActivity"}, {"text": "immunotherapeutic agents", "type": "Chemical"}, {"text": "solid organ transplantation", "type": "HealthCareActivity"}]}

Input:
Sentence: The ultimate aim of these animal and human studies is to develop agents that efficiently target humoral effectors , whilst sparing B and plasma cells with a regulatory capacity to promote long - term allograft survival , but we remain some distance away from this goal .

## Item MedMentions:test:509
Example input:
Sentence: Children with better working memory and language abilities were expected to have better speech recognition in noise than peers with poorer skills in these domains .

Example answer:
{"entities": [{"text": "working memory", "type": "BiologicFunction"}, {"text": "peers", "type": "PopulationGroup"}, {"text": "domains", "type": "SpatialConcept"}]}

Example input:
Sentence: Most individuals showed rightward or leftward laterality shift trends between inanimate and animate targets .

Example answer:
{"entities": []}

Example input:
Sentence: When unilateral blinking was early in seizures , overall lateralization was more often contralateral ( 6 / 7 patients , PPV 85 % ) .

Example answer:
{"entities": [{"text": "unilateral", "type": "SpatialConcept"}, {"text": "blinking", "type": "BiologicFunction"}, {"text": "seizures", "type": "Finding"}, {"text": "contralateral", "type": "SpatialConcept"}]}

Example input:
Sentence: To quantify language control processes , we measured the FC of the dACC and Lcaudate with a region specific to each language modality : left superior temporal gyrus ( LSTG ) for speech and left pre / postcentral gyrus ( LPCG ) for sign .

Example answer:
{"entities": [{"text": "dACC", "type": "SpatialConcept"}, {"text": "Lcaudate", "type": "AnatomicalStructure"}, {"text": "region", "type": "SpatialConcept"}, {"text": "left superior temporal gyrus", "type": "AnatomicalStructure"}, {"text": "LSTG", "type": "AnatomicalStructure"}, {"text": "speech", "type": "BiologicFunction"}, {"text": "left pre / postcentral gyrus", "type": "AnatomicalStructure"}, {"text": "LPCG", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Given that this increased lateralization could not be explained by hand movement alone , the contribution of motor movement versus ' linguistic ' processes to the strength of hemispheric lateralization during sign production remains unclear .

Example answer:
{"entities": [{"text": "lateralization", "type": "BiologicFunction"}, {"text": "hand", "type": "AnatomicalStructure"}, {"text": "movement", "type": "BiologicFunction"}, {"text": "processes", "type": "BiologicFunction"}, {"text": "hemispheric", "type": "SpatialConcept"}, {"text": "production", "type": "BiologicFunction"}]}

Example input:
Sentence: This increased left lateralization may be driven by specific properties of sign production such as the increased use of self - monitoring mechanisms or the nature of phonological encoding of signs .

Example answer:
{"entities": [{"text": "left", "type": "SpatialConcept"}, {"text": "lateralization", "type": "BiologicFunction"}, {"text": "production", "type": "BiologicFunction"}, {"text": "phonological encoding", "type": "BiologicFunction"}]}

Example input:
Sentence: Examining the contribution of motor movement and language dominance to increased left lateralization during sign generation in native signers The neural systems supporting speech and sign processing are very similar , although not identical .

Example answer:
{"entities": [{"text": "left", "type": "SpatialConcept"}, {"text": "lateralization", "type": "BiologicFunction"}, {"text": "signers", "type": "PopulationGroup"}, {"text": "neural systems", "type": "BodySystem"}, {"text": "speech", "type": "BiologicFunction"}, {"text": "processing", "type": "BiologicFunction"}]}

Example input:
Sentence: To address the possibility that hearing native signers ' elevated lateralization indices ( LIs ) were due to performing a task in their less dominant language , here we test deaf native signers , whose dominant language is British Sign Language ( BSL ) .

Example answer:
{"entities": [{"text": "hearing", "type": "BiologicFunction"}, {"text": "signers", "type": "PopulationGroup"}]}

Example input:
Sentence: In a previous fTCD study of hearing native signers ( Gutierrez - Sigut , Daws , et al . , 2015 ) we found stronger left lateralization for sign than speech .

Example answer:
{"entities": [{"text": "fTCD study", "type": "ResearchActivity"}, {"text": "hearing", "type": "BiologicFunction"}, {"text": "signers", "type": "PopulationGroup"}, {"text": "left", "type": "SpatialConcept"}, {"text": "lateralization", "type": "BiologicFunction"}, {"text": "speech", "type": "BiologicFunction"}]}

Example input:
Sentence: Here we directly contrast lateralization strength of covert versus overt signing during phonological and semantic fluency tasks .

Example answer:
{"entities": [{"text": "lateralization", "type": "BiologicFunction"}]}

Input:
Sentence: Comparisons with previous data from hearing native English speakers suggest stronger laterality indices for sign than speech in both covert and overt tasks .

## Item MedMentions:test:201
Example input:
Sentence: Model simulations are used to investigate the relation between the peak wall stress , hematoma thickness and permeability in patients of different age .

Example answer:
{"entities": [{"text": "Model simulations", "type": "ResearchActivity"}, {"text": "hematoma", "type": "BiologicFunction"}]}

Example input:
Sentence: Blood flow in the cerebral venous system : modeling and simulation The development of a software platform incorporating all aspects , from medical imaging data , through three - dimensional reconstruction and suitable meshing , up to simulation of blood flow in patient - specific geometries , is a crucial challenge in biomedical engineering .

Example answer:
{"entities": [{"text": "Blood flow", "type": "BiologicFunction"}, {"text": "cerebral", "type": "AnatomicalStructure"}, {"text": "venous system", "type": "BodySystem"}, {"text": "modeling", "type": "ResearchActivity"}, {"text": "simulation", "type": "ResearchActivity"}, {"text": "software", "type": "IntellectualProduct"}, {"text": "medical imaging", "type": "HealthCareActivity"}, {"text": "three - dimensional", "type": "SpatialConcept"}, {"text": "blood flow", "type": "BiologicFunction"}, {"text": "biomedical engineering", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: The accuracy of the proposed segmentation framework is quantitatively assessed using two public databases ( ISBI VESSEL12 challenge and MICCAI LOLA11 challenge ) and our own database with , respectively , 20 , 55 , and 30 CT images of various lung pathologies acquired with different scanners and protocols .

Example answer:
{"entities": [{"text": "segmentation", "type": "HealthCareActivity"}, {"text": "databases", "type": "IntellectualProduct"}, {"text": "ISBI VESSEL12 challenge", "type": "IntellectualProduct"}, {"text": "MICCAI LOLA11 challenge", "type": "IntellectualProduct"}, {"text": "database", "type": "IntellectualProduct"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "images", "type": "IntellectualProduct"}, {"text": "lung", "type": "AnatomicalStructure"}, {"text": "scanners", "type": "MedicalDevice"}, {"text": "protocols", "type": "HealthCareActivity"}]}

Example input:
Sentence: A multivariable Cox proportional hazards model was used to estimate the primary composite outcome of stroke , transient ischaemic attack ( TIA ) and mortality associated with non - persistence .

Example answer:
{"entities": [{"text": "multivariable Cox proportional hazards model", "type": "IntellectualProduct"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "transient ischaemic attack", "type": "BiologicFunction"}, {"text": "TIA", "type": "BiologicFunction"}, {"text": "non - persistence", "type": "Finding"}]}

Example input:
Sentence: Extended Tofts model and population - based arterial input function were used to calculate kinetic parameters of RCC tumors .

Example answer:
{"entities": [{"text": "Tofts model", "type": "IntellectualProduct"}, {"text": "population - based", "type": "ResearchActivity"}, {"text": "arterial", "type": "SpatialConcept"}, {"text": "input function", "type": "IntellectualProduct"}, {"text": "RCC", "type": "BiologicFunction"}, {"text": "tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: Multivariable models were used to determine factors associated with sentinel node biopsy .

Example answer:
{"entities": [{"text": "sentinel node biopsy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Accurate Lungs Segmentation on CT Chest Images by Adaptive Appearance - Guided Shape Modeling To accurately segment pathological and healthy lungs for reliable computer - aided disease diagnostics , a stack of chest CT scans is modeled as a sample of a spatially inhomogeneous joint 3D Markov - Gibbs random field ( MGRF ) of voxel - wise lung and chest CT image signals ( intensities ) .

Example answer:
{"entities": [{"text": "Lungs", "type": "AnatomicalStructure"}, {"text": "Segmentation", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "Chest", "type": "SpatialConcept"}, {"text": "Images", "type": "IntellectualProduct"}, {"text": "Adaptive Appearance - Guided Shape Modeling", "type": "ResearchActivity"}, {"text": "segment", "type": "HealthCareActivity"}, {"text": "lungs", "type": "AnatomicalStructure"}, {"text": "computer - aided disease diagnostics", "type": "HealthCareActivity"}, {"text": "stack", "type": "SpatialConcept"}, {"text": "chest", "type": "SpatialConcept"}, {"text": "scans", "type": "HealthCareActivity"}, {"text": "modeled", "type": "ResearchActivity"}, {"text": "lung", "type": "AnatomicalStructure"}, {"text": "image", "type": "IntellectualProduct"}]}

Example input:
Sentence: Efficient patient modeling for visuo - haptic VR simulation using a generic patient atlas This work presents a new time - saving virtual patient modeling system by way of example for an existing visuo - haptic training and planning virtual reality ( VR ) system for percutaneous transhepatic cholangio - drainage ( PTCD ) .

Example answer:
{"entities": [{"text": "modeling", "type": "ResearchActivity"}, {"text": "atlas", "type": "IntellectualProduct"}, {"text": "modeling system", "type": "ResearchActivity"}, {"text": "percutaneous transhepatic cholangio - drainage", "type": "HealthCareActivity"}, {"text": "PTCD", "type": "HealthCareActivity"}]}

Example input:
Sentence: Multi - component model of intramural hematoma A novel multi - component model is introduced for studying interaction between blood flow and deforming aortic wall with intramural hematoma ( IMH ) .

Example answer:
{"entities": [{"text": "intramural hematoma", "type": "BiologicFunction"}, {"text": "studying", "type": "ResearchActivity"}, {"text": "blood flow", "type": "BiologicFunction"}, {"text": "deforming", "type": "Finding"}, {"text": "aortic wall", "type": "AnatomicalStructure"}, {"text": "IMH", "type": "BiologicFunction"}]}

Example input:
Sentence: Our modeling process is based on a generic patient atlas to start with .

Example answer:
{"entities": [{"text": "modeling process", "type": "ResearchActivity"}, {"text": "atlas", "type": "IntellectualProduct"}]}

Input:
Sentence: The methodology consists of patient - specific , locally - adaptive transfer functions and dedicated modeling methods such as multi - atlas segmentation , vessel filtering and spline - modeling .

## Item MedMentions:test:36
Example input:
Sentence: A linear regression model including age , weight , height , daily calcium intake , physical activity , smoking vitamin D supplementation and parathyroid hormone showed that 25 - hydroxyvitamin D independently predicted cortical porosity ( standardized β = -0 .

Example answer:
{"entities": [{"text": "model", "type": "IntellectualProduct"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "supplementation", "type": "Chemical"}, {"text": "parathyroid hormone", "type": "Chemical"}, {"text": "25 - hydroxyvitamin D", "type": "Chemical"}, {"text": "cortical", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Baseline 25 - hydroxyvitamin D ( 25 ( OH ) D ) serum levels were analyzed continuously and categorically .

Example answer:
{"entities": [{"text": "25 - hydroxyvitamin D ( 25 ( OH ) D ) serum levels", "type": "HealthCareActivity"}, {"text": "analyzed continuously", "type": "ResearchActivity"}]}

Example input:
Sentence: Low level of 25 - hydroxy vitamin D ( 25 - ( OH ) - D ) is highly prevalent in children worldwide and has been linked to various adverse health outcomes including rickets , osteomalacia , osteomalacic myopathy , sarcopenia , and weakness , growth retardation , hypocalcemia , seizure and tetany , autism , cardiovascular diseases , diabetes mellitus , cancers ( prostate , colon , breast ) , infectious diseases ( viral , tuberculosis ) , and autoimmune diseases , such as multiple sclerosis and Hashimoto 's thyroiditis .

Example answer:
{"entities": [{"text": "25 - hydroxy vitamin D", "type": "Chemical"}, {"text": "25 - ( OH ) - D", "type": "Chemical"}, {"text": "adverse", "type": "BiologicFunction"}, {"text": "rickets", "type": "BiologicFunction"}, {"text": "osteomalacia", "type": "BiologicFunction"}, {"text": "osteomalacic myopathy", "type": "BiologicFunction"}, {"text": "sarcopenia", "type": "BiologicFunction"}, {"text": "weakness", "type": "Finding"}, {"text": "growth retardation", "type": "BiologicFunction"}, {"text": "hypocalcemia", "type": "BiologicFunction"}, {"text": "seizure", "type": "Finding"}, {"text": "tetany", "type": "BiologicFunction"}, {"text": "autism", "type": "BiologicFunction"}, {"text": "cardiovascular diseases", "type": "BiologicFunction"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "cancers", "type": "BiologicFunction"}, {"text": "prostate", "type": "BiologicFunction"}, {"text": "colon", "type": "BiologicFunction"}, {"text": "breast", "type": "BiologicFunction"}, {"text": "infectious diseases", "type": "BiologicFunction"}, {"text": "viral", "type": "BiologicFunction"}, {"text": "tuberculosis", "type": "BiologicFunction"}, {"text": "autoimmune diseases ,", "type": "BiologicFunction"}, {"text": "multiple sclerosis", "type": "BiologicFunction"}, {"text": "Hashimoto 's thyroiditis", "type": "BiologicFunction"}]}

Example input:
Sentence: In a cross - sectional survey , relationship between serum levels of 25 - hydroxy vitamin D ( 25 ( OH ) D ) and glycated haemoglobin ( HbA1C ) was examined in 141 type - 2 diabetic patients including 102 males and 39 females ; age range 22 to 70 years , visiting the Aga Khan University Hospital during July 2013 - April 2014 .

Example answer:
{"entities": [{"text": "cross - sectional survey", "type": "ResearchActivity"}, {"text": "serum", "type": "BodySubstance"}, {"text": "levels of 25 - hydroxy vitamin D", "type": "HealthCareActivity"}, {"text": "25 ( OH ) D", "type": "Chemical"}, {"text": "glycated haemoglobin", "type": "HealthCareActivity"}, {"text": "HbA1C", "type": "Chemical"}, {"text": "type - 2 diabetic", "type": "BiologicFunction"}, {"text": "males", "type": "PopulationGroup"}, {"text": "females", "type": "PopulationGroup"}, {"text": "Aga Khan University Hospital", "type": "Organization"}]}

Example input:
Sentence: We examined 1998 community - dwelling ambulatory men aged ≥65 years at baseline in the Fujiwara - kyo Osteoporosis Risk in Men Study for frailty status as represented by activities of daily living ( ADL ) , physical performance tests ( grip strength , one - foot standing balance with eyes open , timed 10 - m walk ) , and laboratory sera tests .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "men", "type": "PopulationGroup"}, {"text": "frailty", "type": "Finding"}, {"text": "physical performance tests", "type": "HealthCareActivity"}, {"text": "timed 10 - m walk", "type": "HealthCareActivity"}, {"text": "laboratory sera tests", "type": "HealthCareActivity"}]}

Example input:
Sentence: In men with vitamin D deficiency ( < 25 nmol L ( - 1 ) ) or insufficiency [ 25 - 49 nmol L ( - 1 ) , in combination with an elevated serum level of parathyroid hormone ( > 6 . 8 pmol L ( - 1 ) ) ] , cortical porosity was 17 . 2 % higher than in vitamin D - sufficient men ( P < 0 .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "vitamin D deficiency", "type": "BiologicFunction"}, {"text": "serum", "type": "BodySubstance"}, {"text": "level of parathyroid hormone", "type": "HealthCareActivity"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "vitamin D", "type": "Chemical"}]}

Example input:
Sentence: 1 % , P < 0 . 05 ) whilst cortical volumetric BMD , area , trabecular bone volume fraction and femoral neck areal BMD were lower in men in the lowest quartile of vitamin D levels compared to the highest .

Example answer:
{"entities": [{"text": "cortical", "type": "AnatomicalStructure"}, {"text": "volumetric BMD", "type": "ClinicalAttribute"}, {"text": "area", "type": "SpatialConcept"}, {"text": "trabecular bone", "type": "AnatomicalStructure"}, {"text": "femoral neck", "type": "AnatomicalStructure"}, {"text": "areal BMD", "type": "ClinicalAttribute"}, {"text": "men", "type": "PopulationGroup"}, {"text": "vitamin D levels", "type": "HealthCareActivity"}]}

Example input:
Sentence: Serum vitamin D is associated with cortical porosity , area and density , indicating that bone fragility as a result of low vitamin D could be due to changes in cortical bone microstructure and geometry .

Example answer:
{"entities": [{"text": "Serum", "type": "BodySubstance"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "area", "type": "SpatialConcept"}, {"text": "density", "type": "ClinicalAttribute"}, {"text": "bone", "type": "AnatomicalStructure"}, {"text": "fragility", "type": "BiologicFunction"}, {"text": "bone microstructure", "type": "AnatomicalStructure"}, {"text": "geometry", "type": "SpatialConcept"}]}

Example input:
Sentence: Bone microstructure was measured by high - resolution peripheral quantitative computed tomography , areal BMD by dual - energy X - ray absorptiometry and serum 25 - hydroxyvitamin D and parathyroid hormone levels by immunoassay .

Example answer:
{"entities": [{"text": "Bone microstructure", "type": "AnatomicalStructure"}, {"text": "high - resolution peripheral quantitative computed tomography", "type": "HealthCareActivity"}, {"text": "areal BMD", "type": "ClinicalAttribute"}, {"text": "dual - energy X - ray absorptiometry", "type": "HealthCareActivity"}, {"text": "serum", "type": "BodySubstance"}, {"text": "25 - hydroxyvitamin D", "type": "HealthCareActivity"}, {"text": "parathyroid hormone levels", "type": "HealthCareActivity"}, {"text": "immunoassay", "type": "HealthCareActivity"}]}

Example input:
Sentence: Low serum vitamin D is associated with higher cortical porosity in elderly men Bone loss at peripheral sites in the elderly is mainly cortical and involves increased cortical porosity .

Example answer:
{"entities": [{"text": "serum", "type": "BodySubstance"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "elderly", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}, {"text": "Bone loss", "type": "BiologicFunction"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "sites", "type": "SpatialConcept"}]}

Input:
Sentence: To investigate the association between serum levels of 25 - hydroxyvitamin D , bone microstructure and areal bone mineral density ( BMD ) in elderly men .

## Item MedMentions:test:669
Example input:
Sentence: 0 % and individual changes were statistically significant ( p < 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 79 to 1 . 45 and there was no consistent pattern among the three groups ; the changes were not statistically significantly different from baseline .

Example answer:
{"entities": [{"text": "pattern", "type": "SpatialConcept"}, {"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: However , the difference was not statistically significant ( P = 0 . 149 ) .

Example answer:
{"entities": []}

Example input:
Sentence: These distributions were significantly different ( p < 0 . 0001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The difference in quality - of - life ratings was a significant predictor of prediction inaccuracy for the three hypothetical health states ( p < 0 . 01 ) and nearly significant for the current health state ( p = 0 . 077 ) .

Example answer:
{"entities": []}

Example input:
Sentence: This difference was also not statistically significant ( p = 0 . 14 , 95 % CI for median difference -7 .

Example answer:
{"entities": []}

Example input:
Sentence: No statistically significant differences were found for hemorrhagic events ( p = 0 . 07 ) , venous thromboembolic events ( p = 0 . 13 ) , or fatal adverse events ( p = 0 . 26 ) .

Example answer:
{"entities": [{"text": "hemorrhagic", "type": "BiologicFunction"}, {"text": "venous thromboembolic", "type": "BiologicFunction"}, {"text": "adverse events", "type": "BiologicFunction"}]}

Example input:
Sentence: The difference was not statistically significant ( p = 0 . 15 , 95 % CI for median difference -0 .

Example answer:
{"entities": []}

Example input:
Sentence: The clinicopathological features , hazard ratio ( HR ) and 95 % confidence intervals ( CI ) were collected from these studies and were analyzed using Stata version 12 .

Example answer:
{"entities": [{"text": "clinicopathological features", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "Stata version 12 .", "type": "IntellectualProduct"}]}

Example input:
Sentence: There were significant differences ( P < 0 . 001 ; < 0 . 001 ; < 0 . 001 ; < 0 . 001 ) .

Example answer:
{"entities": []}

Input:
Sentence: Several clinical features were found to be statistically different ( P < 0 .

## Item MedMentions:test:647
Example input:
Sentence: We found that the risk of a neonate being prescribed an ASD was 46 % less during Period 3 ( cEEG ) than during Period 1 ( brief conventional EEG only ) ( 95 % CI 6 - 69 % , p = 0 .

Example answer:
{"entities": [{"text": "ASD", "type": "Chemical"}, {"text": "cEEG", "type": "HealthCareActivity"}, {"text": "EEG", "type": "HealthCareActivity"}]}

Example input:
Sentence: The feasibility trial included 36 infants ( 27 - 34 weeks of gestation ) , who were randomised into three groups ( T - piece , new system with face mask or new system with prongs ) .

Example answer:
{"entities": [{"text": "feasibility trial", "type": "ResearchActivity"}, {"text": "weeks of gestation", "type": "Finding"}, {"text": "randomised", "type": "ResearchActivity"}, {"text": "T - piece", "type": "MedicalDevice"}, {"text": "system", "type": "MedicalDevice"}, {"text": "face mask", "type": "MedicalDevice"}, {"text": "prongs", "type": "MedicalDevice"}]}

Example input:
Sentence: We reviewed medical records from 167 children ages 0 - 18 years diagnosed with de novo AML over an 18 - year period at Texas Children 's Cancer Center , among whom 129 self - identified as Hispanic or NHW .

Example answer:
{"entities": [{"text": "medical records", "type": "IntellectualProduct"}, {"text": "diagnosed", "type": "Finding"}, {"text": "AML", "type": "BiologicFunction"}, {"text": "Texas", "type": "SpatialConcept"}, {"text": "Children 's Cancer Center", "type": "Organization"}, {"text": "Hispanic", "type": "PopulationGroup"}, {"text": "NHW", "type": "PopulationGroup"}]}

Example input:
Sentence: We prospectively studied extremely low birth weight ( ELBW ; < 1000 g ) preterm infants who were admitted to the Neonatal Intensive Care Unit of Hanyang University Hospital between February 2011 and February 2014 .

Example answer:
{"entities": [{"text": "extremely low birth weight ( ELBW ; < 1000 g ) preterm infants", "type": "Finding"}, {"text": "admitted", "type": "HealthCareActivity"}, {"text": "Neonatal Intensive Care Unit", "type": "Organization"}, {"text": "Hanyang University Hospital", "type": "Organization"}]}

Example input:
Sentence: The results showed that all of the 32 neonates whose PICCs had been successfully placed and correct tip position verified by chest radiography acquired qualified P wave on IC - ECG .

Example answer:
{"entities": [{"text": "results", "type": "Finding"}, {"text": "tip", "type": "MedicalDevice"}, {"text": "position", "type": "SpatialConcept"}, {"text": "chest radiography", "type": "HealthCareActivity"}, {"text": "P wave", "type": "ClinicalAttribute"}, {"text": "IC", "type": "SpatialConcept"}, {"text": "ECG", "type": "Finding"}]}

Example input:
Sentence: This study included 40 patients with a pre - operative diagnosis of high - risk EC between April 2015 and May 2016 .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "high - risk", "type": "Finding"}, {"text": "EC", "type": "BiologicFunction"}]}

Example input:
Sentence: In uncomplicated preterm infants ( n = 103 [ 48 % ] ) , LV GLS and GLSRs remained unchanged from days 5 to 7 to 1 year CA ( P = .60 and P = .59 ) .

Example answer:
{"entities": [{"text": "LV", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Thirty - two out of 72 ELBW infants underwent conventional MR imaging and DTI at term - equivalent age .

Example answer:
{"entities": [{"text": "ELBW infants", "type": "Finding"}, {"text": "MR imaging", "type": "HealthCareActivity"}, {"text": "DTI", "type": "HealthCareActivity"}]}

Example input:
Sentence: The reason for ECLS was E - CPR in two patients , inability to wean from cardiopulmonary bypass ( CPB ) in seven patients , respiratory insufficiency and hypoxia in nine patients , low cardiac output ( LCOS ) in seven patients .

Example answer:
{"entities": [{"text": "ECLS", "type": "HealthCareActivity"}, {"text": "E - CPR", "type": "HealthCareActivity"}, {"text": "inability to wean", "type": "Finding"}, {"text": "cardiopulmonary bypass", "type": "HealthCareActivity"}, {"text": "CPB", "type": "HealthCareActivity"}, {"text": "respiratory insufficiency", "type": "BiologicFunction"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "low cardiac output", "type": "BiologicFunction"}, {"text": "LCOS", "type": "BiologicFunction"}]}

Example input:
Sentence: The use of neonatal extracorporeal life support in pediatric cardiac intensive care unit The aim of the study is to evaluate extracorporeal life support system ( ECLS ) employed in neonates in pediatric cardiac intensive care unit .

Example answer:
{"entities": [{"text": "extracorporeal life support", "type": "HealthCareActivity"}, {"text": "cardiac intensive care unit", "type": "Organization"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "extracorporeal life support system", "type": "HealthCareActivity"}, {"text": "ECLS", "type": "HealthCareActivity"}]}

Input:
Sentence: Twenty - five neonates that required ECLS in between November 2010 and November 2015 were evaluated .

## Item MedMentions:test:429
Example input:
Sentence: Furthermore , number of diffusion - weighted image ( DWI ) - positive lesion ( ≥8 ) , degree of stenosis ( > 80 . 0 % ) , and NIHSS score ( ≥4 ) were also independent factors associated with ND .

Example answer:
{"entities": [{"text": "diffusion - weighted image", "type": "HealthCareActivity"}, {"text": "DWI", "type": "HealthCareActivity"}, {"text": "positive", "type": "Finding"}, {"text": "lesion", "type": "Finding"}, {"text": "NIHSS score", "type": "Finding"}, {"text": "ND", "type": "Finding"}]}

Example input:
Sentence: DWI examination with a b value of 600 s / mm2 was carried out for all patients .

Example answer:
{"entities": [{"text": "DWI", "type": "HealthCareActivity"}, {"text": "examination", "type": "HealthCareActivity"}]}

Example input:
Sentence: The average ADC value of cysts were significantly higher when compared to hemangiomas and normal control group ( p < 0 . 001 ) .

Example answer:
{"entities": [{"text": "cysts", "type": "BiologicFunction"}, {"text": "hemangiomas", "type": "BiologicFunction"}]}

Example input:
Sentence: Conclusion In vivo abdominal DKI calculated using standard b - values is feasible and enables quantitative differentiation between malignant and benign liver lesions .

Example answer:
{"entities": [{"text": "In vivo", "type": "SpatialConcept"}, {"text": "abdominal", "type": "SpatialConcept"}, {"text": "DKI", "type": "HealthCareActivity"}, {"text": "liver lesions", "type": "Finding"}]}

Example input:
Sentence: Assessment of Early Treatment Response With DWI After CT -Guided Radiofrequency Ablation of Functioning Adrenal Adenomas The objective of this study was to establish the suitability of the apparent diffusion coefficient ( ADC ) as a parameter for evaluating early treatment response after percutaneous ablation of functional adrenal adenomas .

Example answer:
{"entities": [{"text": "Assessment", "type": "HealthCareActivity"}, {"text": "Treatment Response", "type": "ClinicalAttribute"}, {"text": "DWI", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "Radiofrequency Ablation", "type": "HealthCareActivity"}, {"text": "Adrenal Adenomas", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "treatment response", "type": "ClinicalAttribute"}, {"text": "percutaneous", "type": "SpatialConcept"}, {"text": "ablation", "type": "HealthCareActivity"}, {"text": "adrenal adenomas", "type": "BiologicFunction"}]}

Example input:
Sentence: To distinguish hemangiomas from malignant liver lesions , the " cut - off " ADC value of 1 . 800×10 ( - 3 ) mm ( 2 ) / s had a sensitivity of 97 .

Example answer:
{"entities": [{"text": "hemangiomas", "type": "BiologicFunction"}, {"text": "liver lesions", "type": "Finding"}]}

Example input:
Sentence: Diagnostic value of diffusion weighted MRI and ADC in differential diagnosis of cavernous hemangioma of the liver To investigate the use of diffusion weighted magnetic resonance imaging ( DWI ) and the apparent diffusion coefficient ( ADC ) values in the diagnosis of hemangioma .

Example answer:
{"entities": [{"text": "diffusion weighted MRI", "type": "HealthCareActivity"}, {"text": "differential diagnosis", "type": "HealthCareActivity"}, {"text": "cavernous hemangioma", "type": "BiologicFunction"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "diffusion weighted magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "DWI", "type": "HealthCareActivity"}, {"text": "diagnosis", "type": "ResearchActivity"}, {"text": "hemangioma", "type": "BiologicFunction"}]}

Example input:
Sentence: When dynamic examination cannot distinguish cases with vascular metastasis and lesions from hemangioma , DWI and ADC values can be useful in the primary diagnosis and differential diagnosis .

Example answer:
{"entities": [{"text": "dynamic examination", "type": "HealthCareActivity"}, {"text": "vascular metastasis", "type": "BiologicFunction"}, {"text": "lesions", "type": "Finding"}, {"text": "hemangioma", "type": "BiologicFunction"}, {"text": "DWI", "type": "HealthCareActivity"}, {"text": "differential diagnosis", "type": "HealthCareActivity"}]}

Example input:
Sentence: Differentiation of malignant and benign lesions was possible based on both DWI ADC as well as DKI D - values ( P values were in the range of 0 .

Example answer:
{"entities": [{"text": "lesions", "type": "Finding"}, {"text": "DWI", "type": "HealthCareActivity"}, {"text": "DKI", "type": "HealthCareActivity"}]}

Example input:
Sentence: DWI and quantitative measurement of ADC values can be used in differential diagnosis of benign and malignant liver lesions and also in the diagnosis and differentiation of hemangiomas .

Example answer:
{"entities": [{"text": "DWI", "type": "HealthCareActivity"}, {"text": "differential diagnosis", "type": "HealthCareActivity"}, {"text": "liver lesions", "type": "Finding"}, {"text": "diagnosis", "type": "ResearchActivity"}, {"text": "hemangiomas", "type": "BiologicFunction"}]}

Input:
Sentence: After DWI examination , an ADC map was created and ADC values were measured for 72 liver masses and normal liver tissue ( control group ) .

## Item MedMentions:test:494
Example input:
Sentence: Mice immunized with the combination of gB and gH / gL VLPs had a better nAb response than those immunized with either gB ( p = 0 . 0268 ) , or gH /gL ( p = 0 .

Example answer:
{"entities": [{"text": "Mice", "type": "Eukaryote"}, {"text": "immunized", "type": "HealthCareActivity"}, {"text": "gB", "type": "Chemical"}, {"text": "gH", "type": "Chemical"}, {"text": "gL", "type": "Chemical"}, {"text": "VLPs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Despite similar fat mass and energy balance , M ( IL10 ) mice were protected from aging - associated insulin resistance with significant increases in glucose infusion rates , whole - body glucose turnover , and skeletal muscle glucose uptake ( ∼60 % ; P < 0 . 05 ) , as compared to age -matched WT mice .

Example answer:
{"entities": [{"text": "energy balance", "type": "BiologicFunction"}, {"text": "M ( IL10 )", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "aging", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "glucose", "type": "Chemical"}, {"text": "whole - body", "type": "AnatomicalStructure"}, {"text": "skeletal muscle", "type": "AnatomicalStructure"}, {"text": "glucose uptake", "type": "BiologicFunction"}, {"text": "WT mice", "type": "Eukaryote"}]}

Example input:
Sentence: Firstly , compared with the normal control group , mice in the model control group gained more body weight with severe liver steatosis and increased serum levels of triglyceride , total cholesterol , free fatty acids , alanine aminotransferase and aspartate aminotransferase .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}, {"text": "liver steatosis", "type": "BiologicFunction"}, {"text": "serum levels of triglyceride", "type": "Finding"}, {"text": "total cholesterol", "type": "Finding"}, {"text": "free fatty acids", "type": "Finding"}, {"text": "alanine aminotransferase", "type": "Finding"}, {"text": "aspartate aminotransferase", "type": "Finding"}]}

Example input:
Sentence: Rapamycin effects were also genotype dependent , however , with stronger survivorship increases in hybrid mice ( 14 . 4 % ; 95 % CI : 12 . 5 - 16 . 3 % ) relative to pure inbred strains ( 8 . 8 % ; 95 % CI : 6 . 2 - 11 . 6 % ) .

Example answer:
{"entities": [{"text": "Rapamycin", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "inbred strains", "type": "Eukaryote"}]}

Example input:
Sentence: Our results indicate that the strain and age of mice , and even purchasing company ( especially outbred ) , should be matched over experimental groups in TBI experiment .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}, {"text": "company", "type": "Organization"}, {"text": "outbred", "type": "Eukaryote"}, {"text": "TBI", "type": "HealthCareActivity"}, {"text": "experiment", "type": "ResearchActivity"}]}

Example input:
Sentence: LR compared with ob / ob mice had significant decreases in AUC150 ( MD : -779 . 9 ; 95 % CI : -1229 . 8 to -330 ) , CMAX ( MD : -6 . 1 ; 95 % CI : -11 .

Example answer:
{"entities": [{"text": "LR", "type": "HealthCareActivity"}, {"text": "ob / ob", "type": "Eukaryote"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Oral supplementation with vitamin C eliminated differences in body weight , bone weight , BMC , and BMD between SMP30 / GNL KO and wild - type mice at each age .

Example answer:
{"entities": [{"text": "Oral", "type": "SpatialConcept"}, {"text": "supplementation", "type": "Chemical"}, {"text": "vitamin C", "type": "Chemical"}, {"text": "bone", "type": "AnatomicalStructure"}, {"text": "BMD", "type": "ClinicalAttribute"}, {"text": "SMP30 / GNL", "type": "AnatomicalStructure"}, {"text": "KO", "type": "Eukaryote"}, {"text": "wild - type mice", "type": "Eukaryote"}]}

Example input:
Sentence: Male C57BL / 6 mice were randomly assigned to one of four groups : a control diet ( CTL ) , high - fat diet ( HF ) , high - fat diet supplemented with voglibose ( VO ) , and high fat diet pair - fed group ( PF ) .

Example answer:
{"entities": [{"text": "C57BL / 6 mice", "type": "Eukaryote"}]}

Example input:
Sentence: Significant difference of survival rate both ICR and C57BL6N mice was not observed in between 5 - week - old and 8 - week - old groups receiving 10 or 12 Gy TBI .

Example answer:
{"entities": [{"text": "ICR", "type": "Eukaryote"}, {"text": "C57BL6N mice", "type": "Eukaryote"}, {"text": "TBI", "type": "HealthCareActivity"}]}

Example input:
Sentence: In ICR mice , however , survival rate and body weight change rate were completely different among the companies .

Example answer:
{"entities": [{"text": "ICR mice", "type": "Eukaryote"}, {"text": "body weight change", "type": "Finding"}, {"text": "companies", "type": "Organization"}]}

Input:
Sentence: Results showed that survival rate and body weight change rate in inbred C57BL / 6N mice were similar between A and B company .

## Item MedMentions:test:295
Example input:
Sentence: Twenty - two male Jcl : ICR mice were divided into control ( n = 8 ) , masseter - hypofunction ( n = 7 ) and temporalis - hypofunction groups ( n = 7 ) .

Example answer:
{"entities": [{"text": "Jcl", "type": "Eukaryote"}, {"text": "ICR mice", "type": "Eukaryote"}, {"text": "temporalis", "type": "AnatomicalStructure"}]}

Example input:
Sentence: LR compared with ob / ob mice had significant decreases in AUC150 ( MD : -779 . 9 ; 95 % CI : -1229 . 8 to -330 ) , CMAX ( MD : -6 . 1 ; 95 % CI : -11 .

Example answer:
{"entities": [{"text": "LR", "type": "HealthCareActivity"}, {"text": "ob / ob", "type": "Eukaryote"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Finally , hPP2 - 36 , [ K ( 22 ) ( PEG22 ) ] hPP2 - 36 and [ K ( 22 ) ( PEG22 ) , Q ( 34 ) ] hPP significantly reduced cumulative food intake in mice over 16 h after s .

Example answer:
{"entities": [{"text": "hPP2 - 36", "type": "Chemical"}, {"text": "hPP", "type": "Chemical"}, {"text": "food intake", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Mineral content ( BMC ) and mineral density ( BMD ) of the mandible and femur of SMP30 / GNL KO and wild - type mice at 2 and 3 months of age with or without vitamin C supplementation were measured by dual - energy X - ray absorptiometry .

Example answer:
{"entities": [{"text": "mineral density", "type": "ClinicalAttribute"}, {"text": "BMD", "type": "ClinicalAttribute"}, {"text": "mandible", "type": "AnatomicalStructure"}, {"text": "femur", "type": "AnatomicalStructure"}, {"text": "SMP30 / GNL", "type": "AnatomicalStructure"}, {"text": "KO", "type": "Eukaryote"}, {"text": "wild - type mice", "type": "Eukaryote"}, {"text": "vitamin C", "type": "Chemical"}, {"text": "supplementation", "type": "Chemical"}, {"text": "dual - energy X - ray absorptiometry", "type": "HealthCareActivity"}]}

Example input:
Sentence: 3 ( - ∕ - ) male mice with a m oderately high - fat diet ( M HF , 31 . 8 % kcal fat ) for 4 months and then examined OB ultrastructure using transmission electron microscopy .

Example answer:
{"entities": [{"text": "3 ( - ∕ - ) male mice", "type": "Eukaryote"}, {"text": "oderately high - fat diet (", "type": "HealthCareActivity"}, {"text": "HF ,", "type": "HealthCareActivity"}, {"text": "OB", "type": "AnatomicalStructure"}, {"text": "transmission electron microscopy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Several PK parameters were significantly greater in ob / ob compared with DIO mice , including AUC150 ( MD : 636 . 4 ; 95 % CI : 207 . 4 - 1065 . 4 ) , CMAX ( MD : 5 . 3 ; 95 % CI : 3 . 2 - 10 . 3 ) , and T1 / 2 ( MD : 18 . 3 ; 95 % CI : 2 . 8 - 33 . 7 ) .

Example answer:
{"entities": [{"text": "PK", "type": "BiologicFunction"}, {"text": "parameters", "type": "Finding"}, {"text": "ob / ob", "type": "Eukaryote"}, {"text": "DIO mice", "type": "Eukaryote"}]}

Example input:
Sentence: MKO mice were protected against obesity and sensitized to insulin , an effect associated with elevated GDF15 secretion after UPR ( mt ) activation .

Example answer:
{"entities": [{"text": "MKO mice", "type": "Eukaryote"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "sensitized", "type": "BiologicFunction"}, {"text": "insulin", "type": "Chemical"}, {"text": "GDF15", "type": "Chemical"}, {"text": "secretion", "type": "BiologicFunction"}, {"text": "UPR ( mt )", "type": "BiologicFunction"}]}

Example input:
Sentence: Genetic inactivation of myostatin increases maximal force and power , but in return it reduces muscle quality , particularly in male mice .

Example answer:
{"entities": [{"text": "Genetic inactivation", "type": "BiologicFunction"}, {"text": "myostatin", "type": "AnatomicalStructure"}, {"text": "maximal force", "type": "BiologicFunction"}, {"text": "muscle", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Similarly , absolute maximal power was increased in 6 - month - old KO ( Lee ) mice .

Example answer:
{"entities": [{"text": "absolute maximal power", "type": "BiologicFunction"}, {"text": "KO ( Lee ) mice", "type": "Eukaryote"}]}

Example input:
Sentence: Absolute maximal isometric force was increased in 6 - month - old KO ( Lee ) and KO ( Grobet ) mice , as compared to wild - type mice .

Example answer:
{"entities": [{"text": "Absolute maximal isometric force", "type": "BiologicFunction"}, {"text": "KO ( Lee )", "type": "Eukaryote"}, {"text": "KO ( Grobet ) mice", "type": "Eukaryote"}, {"text": "wild - type mice", "type": "Eukaryote"}]}

Input:
Sentence: In contrast , specific maximal force ( relative maximal force per unit of muscle mass was decreased in all 6 - month - old male and female KO mice , except in 6 - month -old female KO ( Grobet ) mice , whereas specific maximal power was reduced only in male KO ( Lee ) mice .

## Item MedMentions:test:518
Example input:
Sentence: The cytology was diagnostic in 48 / 50 biopsies ( 96 % ) : out of 41 neoplastic lesions ( 85 % ) , 37 were malignant ( 90 . 2 % ) and 4 were benign ( 9 . 8 % ) ; 7 out of 48 were non - neoplastic ( 14 . 6 % ) .

Example answer:
{"entities": [{"text": "cytology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "biopsies", "type": "HealthCareActivity"}, {"text": "lesions", "type": "Finding"}, {"text": "malignant", "type": "BiologicFunction"}, {"text": "non - neoplastic", "type": "BiologicFunction"}]}

Example input:
Sentence: We prospectively enrolled 312 men with lesions suspicious for cancer ( suspicion score 2 - 5 ) on mpMRI . MRI / ultrasound fusion - guided prostate biopsies were performed .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "lesions", "type": "Finding"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "mpMRI", "type": "HealthCareActivity"}, {"text": "MRI / ultrasound fusion - guided prostate biopsies", "type": "HealthCareActivity"}]}

Example input:
Sentence: Among the patients with ≥3 polyps resected ( n = 130 ) , advanced neoplasia was found in 5 of 79 patients ( 6 . 3 % ) of the 1 - to 5 - mm group versus 5 of 51 patients ( 9 . 8 % ) of the 6 - to 9 - mm group ( HR 2 .

Example answer:
{"entities": [{"text": "polyps", "type": "AnatomicalStructure"}, {"text": "resected", "type": "HealthCareActivity"}, {"text": "neoplasia", "type": "BiologicFunction"}, {"text": "found", "type": "Finding"}]}

Example input:
Sentence: Majority of patients ( 94 % ) had squamous cell carcinoma , while only 6 % had adenocarcinoma .

Example answer:
{"entities": [{"text": "squamous cell carcinoma", "type": "BiologicFunction"}, {"text": "adenocarcinoma", "type": "BiologicFunction"}]}

Example input:
Sentence: Both primary BC ( 52 cases ; 38 % ) and metastatic site biopsies ( 86 cases ; 62 % ) were found to harbor ERBB2mut , which were distributed across carcinoma not otherwise specified ( NOS ) ( 69 cases ; 50 % ) , invasive ductal carcinoma ( IDC ) ( 40 cases ; 29 % ) , invasive lobular carcinoma ( ILC ) ( 27 cases ; 20 % ) , and mucinous mBC ( 2 cases ; 1 % ) .

Example answer:
{"entities": [{"text": "primary BC", "type": "BiologicFunction"}, {"text": "biopsies", "type": "HealthCareActivity"}, {"text": "ERBB2mut", "type": "AnatomicalStructure"}, {"text": "carcinoma", "type": "BiologicFunction"}, {"text": "invasive ductal carcinoma", "type": "BiologicFunction"}, {"text": "IDC", "type": "BiologicFunction"}, {"text": "invasive lobular carcinoma", "type": "BiologicFunction"}, {"text": "ILC", "type": "BiologicFunction"}, {"text": "mucinous mBC", "type": "BiologicFunction"}]}

Example input:
Sentence: Phenotypic and genetic heterogeneity of tumor tissue and circulating tumor cells in patients with metastatic castration - resistant prostate cancer : A report from the PETRUS prospective study Molecular characterization of cancer samples is hampered by tumor tissue availability in metastatic castration - resistant prostate cancer ( mCRPC ) patients .

Example answer:
{"entities": [{"text": "Phenotypic", "type": "Finding"}, {"text": "tumor tissue", "type": "AnatomicalStructure"}, {"text": "circulating tumor cells", "type": "AnatomicalStructure"}, {"text": "metastatic castration - resistant prostate cancer", "type": "BiologicFunction"}, {"text": "report", "type": "IntellectualProduct"}, {"text": "PETRUS prospective study", "type": "ResearchActivity"}, {"text": "Molecular characterization of cancer samples", "type": "IntellectualProduct"}, {"text": "mCRPC", "type": "BiologicFunction"}]}

Example input:
Sentence: The vast majority of malignant specimens in histopathology consisted of papillary thyroid carcinoma ( PTC ) ( n = 91 , 86 .

Example answer:
{"entities": [{"text": "histopathology", "type": "HealthCareActivity"}, {"text": "papillary thyroid carcinoma", "type": "BiologicFunction"}, {"text": "PTC", "type": "BiologicFunction"}]}

Example input:
Sentence: Among them , 53 out of 312 ( 17 . 0 % ) men were diagnosed to have prostate cancer on biopsy .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "diagnosed", "type": "Finding"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "biopsy", "type": "HealthCareActivity"}]}

Example input:
Sentence: We analyzed 67 patients with suspected MCpEF who underwent endomyocardial biopsy ( EMB ) .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "suspected MCpEF", "type": "BiologicFunction"}, {"text": "endomyocardial biopsy", "type": "HealthCareActivity"}, {"text": "EMB", "type": "HealthCareActivity"}]}

Example input:
Sentence: Of 301 MRI - guided biopsies , 65 . 4 % contained cancer while 57 . 2 % of 659 TRUS biopsies contained cancer ( P = 0 . 016 ) .

Example answer:
{"entities": [{"text": "MRI - guided biopsies", "type": "HealthCareActivity"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "TRUS", "type": "HealthCareActivity"}, {"text": "biopsies", "type": "HealthCareActivity"}]}

Input:
Sentence: Among 54 mCRPC patients enrolled , 38 ( 70 % ) had biopsies containing more than 50 % tumour cells .

## Item MedMentions:test:740
Example input:
Sentence: 9 compared with 75 . 8 ± 2 .

Example answer:
{"entities": []}

Example input:
Sentence: If these rates remain constant over time , the average surgeon would perform 1 . 8 ( SD = 1 . 7 ) splenectomies and 0 . 6 ( SD = 1 . 1 ) splenorrhaphies for trauma over a 30 - year surgical career .

Example answer:
{"entities": [{"text": "surgeon", "type": "ProfessionalOrOccupationalGroup"}, {"text": "splenectomies", "type": "HealthCareActivity"}, {"text": "splenorrhaphies", "type": "HealthCareActivity"}, {"text": "trauma", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: 88 [ 95 % confidence interval 0 . 79 - 0 . 96 ] vs 0 . 77 [ 95 % confidence interval 0 . 62 - 0 . 92 ] , P = .12 in the cervical surgery group ; and 0 . 77 [ 95 % confidence interval 0 . 70 - 0 . 84 ] vs 0 . 74 [ 95 % confidence interval 0 . 67 - 0 . 81 ] , P = .32 in the previous spontaneous preterm birth group ) .

Example answer:
{"entities": [{"text": "spontaneous preterm birth", "type": "Finding"}]}

Example input:
Sentence: 85 ± 0 .

Example answer:
{"entities": []}

Example input:
Sentence: The principal indications for surgery were inguinal ( 62 ) and umbilical ( 47 ) hernias .

Example answer:
{"entities": [{"text": "surgery", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "inguinal", "type": "AnatomicalStructure"}, {"text": "umbilical ( 47 ) hernias", "type": "BiologicFunction"}]}

Example input:
Sentence: The rate of conversion to open surgery was 35 % ; if minilaparotomies are excluded , the conversion rate was only 16 % .

Example answer:
{"entities": [{"text": "open surgery", "type": "HealthCareActivity"}, {"text": "minilaparotomies", "type": "HealthCareActivity"}]}

Example input:
Sentence: ( 27 . 1±42 . 6 vs 75 .

Example answer:
{"entities": []}

Example input:
Sentence: During the study period , a total of 1250 patients underwent surgery , of whom 515 were elective cases ; 115 of these met the criteria for ambulatory surgery ; 103 patients , with an average age of 59 . 74 ± 41 . 57 months , actually underwent surgery .

Example answer:
{"entities": [{"text": "met the criteria", "type": "Finding"}, {"text": "ambulatory surgery", "type": "HealthCareActivity"}, {"text": "underwent surgery", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: 72 in the second surgery .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: 6 % ( 63 / 88 ) on the first day after the first surgical procedure ; it then increased to 86 .

Example answer:
{"entities": [{"text": "surgical procedure", "type": "HealthCareActivity"}]}

Input:
Sentence: 75 in the first surgery and 2 . 08 ± 0 .

## Item MedMentions:test:127
Example input:
Sentence: Toxoplasma gondii seroprevalence in the Portuguese population : comparison of three cross - sectional studies spanning three decades Toxoplasma gondii is an obligate intracellular protozoan infecting up to one - third of the world 's population , constituting a life threat if transmitted from mother to child during pregnancy .

Example answer:
{"entities": [{"text": "Toxoplasma gondii", "type": "Eukaryote"}, {"text": "seroprevalence", "type": "ResearchActivity"}, {"text": "Portuguese population", "type": "PopulationGroup"}, {"text": "cross - sectional studies", "type": "ResearchActivity"}, {"text": "intracellular", "type": "SpatialConcept"}, {"text": "protozoan", "type": "Eukaryote"}, {"text": "world 's population", "type": "PopulationGroup"}, {"text": "life threat", "type": "Finding"}, {"text": "pregnancy", "type": "BiologicFunction"}]}

Example input:
Sentence: We performed a large epidemiologic study on hospital admissions for portal vein thrombosis ( PVT ) and the Budd - Chiari syndrome ( BCS ) between 2002 and 2012 in Northwestern Italy .

Example answer:
{"entities": [{"text": "epidemiologic study", "type": "ResearchActivity"}, {"text": "hospital admissions", "type": "HealthCareActivity"}, {"text": "portal vein thrombosis", "type": "BiologicFunction"}, {"text": "PVT", "type": "BiologicFunction"}, {"text": "Budd - Chiari syndrome", "type": "BiologicFunction"}, {"text": "BCS", "type": "BiologicFunction"}, {"text": "Northwestern Italy", "type": "SpatialConcept"}]}

Example input:
Sentence: The Netherlands Chlamydia cohort study ( NECCST ) protocol to assess the risk of late complications following Chlamydia trachomatis infection in women Chlamydia trachomatis ( CT ) , the most common bacterial sexually transmitted infection ( STI ) among young women , can result in serious sequelae .

Example answer:
{"entities": [{"text": "Netherlands Chlamydia cohort study", "type": "ResearchActivity"}, {"text": "NECCST", "type": "ResearchActivity"}, {"text": "protocol", "type": "IntellectualProduct"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "Chlamydia trachomatis infection", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "Chlamydia trachomatis", "type": "Bacterium"}, {"text": "CT", "type": "Bacterium"}, {"text": "bacterial sexually transmitted infection", "type": "BiologicFunction"}, {"text": "STI", "type": "BiologicFunction"}, {"text": "sequelae", "type": "BiologicFunction"}]}

Example input:
Sentence: We studied the seroprevalence trends in the Portuguese general population over the past 3 decades , by assessing chronological spread cross - sectional studies , with special focus on women of childbearing age , by age group , region and gender .

Example answer:
{"entities": [{"text": "seroprevalence", "type": "ResearchActivity"}, {"text": "Portuguese general population", "type": "PopulationGroup"}, {"text": "cross - sectional studies", "type": "ResearchActivity"}, {"text": "women", "type": "PopulationGroup"}, {"text": "childbearing", "type": "BiologicFunction"}, {"text": "region", "type": "SpatialConcept"}]}

Example input:
Sentence: In Portugal , there is a lack of knowledge of the current epidemiological situation , as the unique toxoplasmosis National Serological Survey was performed in 1979 / 1980 .

Example answer:
{"entities": [{"text": "Portugal", "type": "SpatialConcept"}, {"text": "toxoplasmosis", "type": "BiologicFunction"}]}

Example input:
Sentence: There was no consistent pattern associated with the switch from wP to aP vaccines on reported pertussis incidence rates .

Example answer:
{"entities": [{"text": "wP", "type": "Chemical"}, {"text": "aP vaccines", "type": "Chemical"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "pertussis", "type": "BiologicFunction"}]}

Example input:
Sentence: The annual incidence of pertussis in the participating countries was obtained from relevant government institutions and / or national surveillance systems .

Example answer:
{"entities": [{"text": "pertussis", "type": "BiologicFunction"}, {"text": "countries", "type": "SpatialConcept"}, {"text": "government institutions", "type": "Organization"}, {"text": "national surveillance systems", "type": "Organization"}]}

Example input:
Sentence: The heterogeneity in reported data may be related to a number of factors including surveillance system characteristics or capabilities , different case definitions , type of pertussis confirmation tests used , public awareness of the disease , as well as real differences in the magnitude of the disease , or a combination of these factors .

Example answer:
{"entities": [{"text": "reported", "type": "HealthCareActivity"}, {"text": "pertussis", "type": "BiologicFunction"}, {"text": "confirmation tests", "type": "HealthCareActivity"}, {"text": "public", "type": "Organization"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: We reviewed the changes in the pertussis incidence rates in each country to explore differences and / or similarities between countries in relation to pertussis surveillance ; case definitions for detection and confirmation of pertussis ; incidence and number of cases of pertussis by year , overall and by age group ; population by year , overall and by age group ; pertussis immunization schedule and coverage , and switch from whole - cell pertussis vaccines ( wP ) to acellular pertussis vaccines ( aP ) .

Example answer:
{"entities": [{"text": "pertussis", "type": "BiologicFunction"}, {"text": "country", "type": "SpatialConcept"}, {"text": "countries", "type": "SpatialConcept"}, {"text": "detection", "type": "Finding"}, {"text": "population", "type": "PopulationGroup"}, {"text": "immunization schedule", "type": "HealthCareActivity"}, {"text": "whole - cell pertussis vaccines", "type": "Chemical"}, {"text": "wP", "type": "Chemical"}, {"text": "acellular pertussis vaccines", "type": "Chemical"}, {"text": "aP", "type": "Chemical"}]}

Example input:
Sentence: Comparative Epidemiologic Characteristics of Pertussis in 10 Central and Eastern European Countries , 2000 - 2013 We undertook an epidemiological survey of the annual incidence of pertussis reported from 2000 to 2013 in ten Central and Eastern European countries to ascertain whether increased pertussis reports in some countries share common underlying drivers or whether there are specific features in each country .

Example answer:
{"entities": [{"text": "Pertussis", "type": "BiologicFunction"}, {"text": "Central", "type": "SpatialConcept"}, {"text": "Eastern European Countries", "type": "SpatialConcept"}, {"text": "epidemiological survey", "type": "ResearchActivity"}, {"text": "pertussis", "type": "BiologicFunction"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "Eastern European countries", "type": "SpatialConcept"}, {"text": "reports", "type": "IntellectualProduct"}, {"text": "countries", "type": "SpatialConcept"}, {"text": "country", "type": "SpatialConcept"}]}

Input:
Sentence: Our study highlights the need to standardize pertussis detection and confirmation in surveillance programs across Europe , complemented with carefully - designed seroprevalence studies using the same protocols and methodologies .

## Item MedMentions:test:590
Example input:
Sentence: Suicidal thinking and behavior was associated with older child age and with higher rates of concurrent depression , oppositional defiant disorder , and posttraumatic stress disorder in univariate analyses , with age and depression remaining as significant predictors in a multivariate logistic regression model .

Example answer:
{"entities": [{"text": "Suicidal thinking", "type": "Finding"}, {"text": "behavior", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "posttraumatic stress disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , a number of studies have found that postpartum depression affects mother - infant emotion regulation , but there has been only one study on anxiety and emotion regulation and no studies at all on parenting stress and emotion regulation .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "postpartum depression", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "parenting stress", "type": "BiologicFunction"}]}

Example input:
Sentence: The second aim is to examine the relationship between anxiety , postpartum depression , and parenting stress and mother - infant emotion regulation assessed at 3 months .

Example answer:
{"entities": [{"text": "postpartum depression", "type": "BiologicFunction"}, {"text": "parenting stress", "type": "BiologicFunction"}]}

Example input:
Sentence: Parenting stress was not shown to predict such regulation .

Example answer:
{"entities": [{"text": "Parenting stress", "type": "BiologicFunction"}]}

Example input:
Sentence: The Edinburgh Postnatal Depression Scale ( EPDS ) , State - Trait Anxiety Inventory ( STAI ) , and Parenting Stress Index - Short Form ( PSI - SF ) were administered to the mothers to assess depression , anxiety , and parenting stress , respectively .

Example answer:
{"entities": [{"text": "Edinburgh Postnatal Depression Scale", "type": "IntellectualProduct"}, {"text": "EPDS", "type": "IntellectualProduct"}, {"text": "State - Trait Anxiety Inventory", "type": "HealthCareActivity"}, {"text": "STAI", "type": "HealthCareActivity"}, {"text": "Parenting Stress Index - Short Form", "type": "IntellectualProduct"}, {"text": "PSI - SF", "type": "IntellectualProduct"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "parenting stress", "type": "BiologicFunction"}]}

Example input:
Sentence: Parental depressive and posttraumatic stress symptoms were associated with impairments in social emotional adjustment in young children , increased anxiety in early childhood , and adjustment problems in school - age children .

Example answer:
{"entities": [{"text": "depressive", "type": "BiologicFunction"}, {"text": "posttraumatic stress symptoms", "type": "BiologicFunction"}, {"text": "emotional", "type": "Finding"}, {"text": "anxiety", "type": "Finding"}]}

Example input:
Sentence: Mother - Infant Emotion Regulation at Three Months : The Role of Maternal Anxiety , Depression and Parenting Stress While the association between anxiety and postpartum depression is well known , few studies have investigated the relationship between these two states and parenting stress .

Example answer:
{"entities": [{"text": "Depression", "type": "BiologicFunction"}, {"text": "Parenting Stress", "type": "BiologicFunction"}, {"text": "postpartum depression", "type": "BiologicFunction"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "parenting stress", "type": "BiologicFunction"}]}

Example input:
Sentence: In a laboratory observation , depression was correlated with both negative maternal states and negative dyadic matches as well as infant positive / mother negative mismatches ; anxiety was correlated with both negative maternal states and infant negative states as well as mismatches involving one of the partners having a negative state .

Example answer:
{"entities": [{"text": "laboratory observation", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "negative", "type": "Finding"}, {"text": "maternal", "type": "Finding"}, {"text": "positive", "type": "Finding"}]}

Example input:
Sentence: Multiple regression analysis showed that anxiety is a greater predictor than depression of less adequate styles of mother - infant emotion regulation .

Example answer:
{"entities": [{"text": "depression", "type": "BiologicFunction"}]}

Example input:
Sentence: Therefore , the primary aim of our study is to identify , in a community sample of 71 mothers , the relationship between maternal depression , anxiety , and parenting stress .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "maternal depression", "type": "BiologicFunction"}, {"text": "parenting stress", "type": "BiologicFunction"}]}

Input:
Sentence: Analysis revealed correlations between anxiety and depression , showing that parenting stress is associated with both states .

## Item MedMentions:test:601
Example input:
Sentence: 36 more infant deaths occurred among non - Hispanic black women relative to all other women ( 95 % confidence interva l : 2 . 78 , 3 . 93 ) .

Example answer:
{"entities": [{"text": "infant deaths", "type": "Finding"}, {"text": "non - Hispanic black women", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Improving access to and utilisation of appropriate and responsive healthcare may help to address disparities in stillbirth risk for Indigenous women .

Example answer:
{"entities": [{"text": "healthcare", "type": "HealthCareActivity"}, {"text": "stillbirth", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: In all , 181 , 814 BC patients ( 1 , 516 male and 180 , 298 female ) were eligible for this study .

Example answer:
{"entities": [{"text": "BC", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: This cohort study involved 76 women conceiving with donated oocytes , 149 age - matched nulliparous women conceiving spontaneously and 63 women conceiving after non - donor IVF .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "nulliparous women", "type": "Finding"}, {"text": "non - donor IVF", "type": "HealthCareActivity"}]}

Example input:
Sentence: 9±6 . 2 years and 2768 ( 58 . 9 % ) were women .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: We conducted a population -representative household survey of four health clinic catchment areas of 1 , 075 women of reproductive age in 2015 .

Example answer:
{"entities": [{"text": "population", "type": "PopulationGroup"}, {"text": "health clinic catchment areas", "type": "SpatialConcept"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: This study highlights gestational age specific stillbirth risk for Indigenous and non - Indigenous women ; and disparity in risk at term gestations .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "stillbirth", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "term gestations", "type": "BiologicFunction"}]}

Example input:
Sentence: The objective of this study was to examine gestational age specific risk of stillbirth associated with these conditions among Indigenous and non - Indigenous women .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "stillbirth", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Diabetes , hypertension , antepartum haemorrhage and small - for - gestational age ( SGA ) have been identified as important contributors to higher rates among Indigenous women .

Example answer:
{"entities": [{"text": "Diabetes", "type": "BiologicFunction"}, {"text": "hypertension", "type": "BiologicFunction"}, {"text": "antepartum haemorrhage", "type": "BiologicFunction"}, {"text": "small - for - gestational age", "type": "BiologicFunction"}, {"text": "SGA", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Gestational age specific stillbirth risk among Indigenous and non - Indigenous women in Queensland , Australia : a population based study In Australia , significant disparity persists in stillbirth rates between Aboriginal and Torres Strait Islander ( Indigenous Australian ) and non - Indigenous women .

Example answer:
{"entities": [{"text": "stillbirth", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "Queensland", "type": "SpatialConcept"}, {"text": "Australia", "type": "SpatialConcept"}, {"text": "population based study", "type": "ResearchActivity"}, {"text": "Torres Strait Islander", "type": "PopulationGroup"}]}

Input:
Sentence: Of 360987 births analysed , 20273 ( 5 . 6 % ) were to Indigenous women and 340714 ( 94 . 4 % ) were to non - Indigenous women .

## Item MedMentions:test:604
Example input:
Sentence: Irrespective of profession , length of practicum or exposure to specific empathy training , there were no significant differences in the self - reported JSPE scores across the seven different cohorts of students .

Example answer:
{"entities": [{"text": "self - reported", "type": "ResearchActivity"}, {"text": "cohorts", "type": "PopulationGroup"}, {"text": "students", "type": "PopulationGroup"}]}

Example input:
Sentence: Twenty - five ( 50 % ) FXMs were positive .

Example answer:
{"entities": [{"text": "FXMs", "type": "HealthCareActivity"}, {"text": "positive", "type": "Finding"}]}

Example input:
Sentence: Evaluations showed a significant improvement between pre - and post - programme knowledge and confidence in all six stations and overall , and a high degree of satisfaction in all settings .

Example answer:
{"entities": [{"text": "Evaluations", "type": "IntellectualProduct"}, {"text": "knowledge", "type": "IntellectualProduct"}, {"text": "confidence", "type": "BiologicFunction"}, {"text": "satisfaction", "type": "BiologicFunction"}, {"text": "settings", "type": "SpatialConcept"}]}

Example input:
Sentence: Although a positive perception of their educational environment was found , minor corrective measures need to be implemented .

Example answer:
{"entities": [{"text": "perception", "type": "BiologicFunction"}]}

Example input:
Sentence: There was a statistically significant improvement of all domain scores of the UDI - 6 , IIQ - 7 , and PISQ - 12 at 6 months follow up .

Example answer:
{"entities": [{"text": "UDI - 6", "type": "IntellectualProduct"}, {"text": "IIQ - 7", "type": "IntellectualProduct"}, {"text": "PISQ - 12", "type": "IntellectualProduct"}]}

Example input:
Sentence: 20 . The majority of the participants ( 49 . 3 % ) had moderate and relatively favorable spiritual attitude ( a score of 72 - 120 ) , 27 . 8 % had high or favorable spiritual attitude ; 8 . 7 % had mild burden , 54 .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "attitude", "type": "BiologicFunction"}]}

Example input:
Sentence: At the same time , 61 % of students showed high perceived stress levels .

Example answer:
{"entities": [{"text": "students", "type": "ProfessionalOrOccupationalGroup"}, {"text": "perceived", "type": "BiologicFunction"}]}

Example input:
Sentence: Fifteen domains were derived from the qualitative methods , with content saturation achieved , resulting in 115 items .

Example answer:
{"entities": []}

Example input:
Sentence: The highest percentage was observed for " Students perception of learning " ( 64 . 04 % ) while the lowest was for " Students ' social self - perception " ( 60 . 32 % ) .

Example answer:
{"entities": [{"text": "Students", "type": "ProfessionalOrOccupationalGroup"}, {"text": "perception", "type": "BiologicFunction"}, {"text": "learning", "type": "BiologicFunction"}]}

Example input:
Sentence: The Dundee Ready Education Environment Measure ( DREEM ) was used to determine educational environment while self - rated perceived stress level was measured by the Depression Anxiety Stress Scale ( DASS ) .

Example answer:
{"entities": [{"text": "Dundee Ready Education Environment Measure", "type": "IntellectualProduct"}, {"text": "DREEM", "type": "IntellectualProduct"}, {"text": "self - rated", "type": "IntellectualProduct"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "stress", "type": "BiologicFunction"}, {"text": "Depression Anxiety Stress Scale", "type": "IntellectualProduct"}, {"text": "DASS", "type": "IntellectualProduct"}]}

Input:
Sentence: Most students ( 62 . 39 % ) showed positive perceptions for the total and five domains of DREEM .

## Item MedMentions:test:44
Example input:
Sentence: In this study , total of 45 patients , mostly offspring of consanguineous marriages were examined using whole exome sequencing .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "whole exome sequencing", "type": "ResearchActivity"}]}

Example input:
Sentence: We describe the application of a targeted next - generation sequencing ( NGS ) and bioinformatics approach to samples from 17 mesiodens patients .

Example answer:
{"entities": [{"text": "next - generation sequencing", "type": "ResearchActivity"}, {"text": "NGS", "type": "ResearchActivity"}, {"text": "bioinformatics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "mesiodens", "type": "BiologicFunction"}]}

Example input:
Sentence: Our study supports the efficacy of exome sequencing in the presence of both a family history suggestive of an inherited disorder and well - documented ultrasound findings .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "exome sequencing", "type": "ResearchActivity"}, {"text": "family history", "type": "Finding"}, {"text": "inherited disorder", "type": "BiologicFunction"}, {"text": "well - documented", "type": "HealthCareActivity"}, {"text": "ultrasound findings", "type": "Finding"}]}

Example input:
Sentence: Comparative gene expression profiling of motor neurons innervating the extensor digitorum longus ( disease - resistant ) , gastrocnemius ( intermediate vulnerability ) , and tibialis anterior ( vulnerable ) muscles in mice revealed that disease susceptibility correlates strongly with a modified bioenergetic profile .

Example answer:
{"entities": [{"text": "gene expression profiling", "type": "HealthCareActivity"}, {"text": "motor neurons", "type": "AnatomicalStructure"}, {"text": "extensor digitorum longus", "type": "AnatomicalStructure"}, {"text": "disease - resistant", "type": "BiologicFunction"}, {"text": "gastrocnemius", "type": "AnatomicalStructure"}, {"text": "tibialis anterior", "type": "AnatomicalStructure"}, {"text": "muscles", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "disease susceptibility", "type": "ClinicalAttribute"}, {"text": "bioenergetic", "type": "BiologicFunction"}, {"text": "profile", "type": "HealthCareActivity"}]}

Example input:
Sentence: Today , the advantage of whole exome sequencing in clinical diagnostic strategies of heterogeneous disorders is clear .

Example answer:
{"entities": [{"text": "whole exome sequencing", "type": "ResearchActivity"}, {"text": "clinical diagnostic", "type": "HealthCareActivity"}, {"text": "heterogeneous disorders", "type": "Finding"}]}

Example input:
Sentence: Data analysis was performed to identify the most probable pathogenic rare variants in known NMD genes which led to identification of causal variants for 33 out of 45 patients ( 73 . 3 % ) in the following known genes : CAPN3 , Col6A1 , Col6A3 , DMD , DYSF , FHL1 , GJB1 , ISPD , LAMA2 , LMNA , PLEC1 , RYR1 , SGCA , SGCB , SYNE1 , TNNT1 and 22 novel pathogenic variants were detected .

Example answer:
{"entities": [{"text": "pathogenic", "type": "Finding"}, {"text": "rare variants", "type": "AnatomicalStructure"}, {"text": "NMD", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "CAPN3", "type": "AnatomicalStructure"}, {"text": "Col6A1", "type": "AnatomicalStructure"}, {"text": "Col6A3", "type": "AnatomicalStructure"}, {"text": "DMD", "type": "AnatomicalStructure"}, {"text": "DYSF", "type": "AnatomicalStructure"}, {"text": "FHL1", "type": "AnatomicalStructure"}, {"text": "GJB1", "type": "AnatomicalStructure"}, {"text": "ISPD", "type": "AnatomicalStructure"}, {"text": "LAMA2", "type": "AnatomicalStructure"}, {"text": "LMNA", "type": "AnatomicalStructure"}, {"text": "PLEC1", "type": "AnatomicalStructure"}, {"text": "RYR1", "type": "AnatomicalStructure"}, {"text": "SGCA", "type": "AnatomicalStructure"}, {"text": "SGCB", "type": "AnatomicalStructure"}, {"text": "SYNE1", "type": "AnatomicalStructure"}, {"text": "TNNT1", "type": "AnatomicalStructure"}, {"text": "variants", "type": "AnatomicalStructure"}, {"text": "detected", "type": "Finding"}]}

Example input:
Sentence: This could be explained by the consanguineous background of these patients and is another strong advantage of offering clinical exome sequencing in diagnostic laboratories , especially in populations with high rate of consanguinity .

Example answer:
{"entities": [{"text": "exome sequencing", "type": "ResearchActivity"}, {"text": "laboratories", "type": "Organization"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "consanguinity", "type": "Finding"}]}

Example input:
Sentence: Our results demonstrate that exome sequencing in multigenerational families with BD is effective in identifying rare genomic variants of potential clinical relevance and also disease modifiers related to coexisting medical conditions .

Example answer:
{"entities": [{"text": "exome sequencing", "type": "ResearchActivity"}, {"text": "BD", "type": "BiologicFunction"}, {"text": "genomic variants", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: To determine whether rare , damaging mutations shared identity - by - descent in families with BD could be associated with disease , exome sequencing was performed in multigenerational families of the NIMH BD Family Study followed by in silico functional prediction .

Example answer:
{"entities": [{"text": "mutations", "type": "BiologicFunction"}, {"text": "BD", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "exome sequencing", "type": "ResearchActivity"}, {"text": "NIMH", "type": "Organization"}, {"text": "Family Study", "type": "HealthCareActivity"}, {"text": "in silico functional prediction", "type": "ResearchActivity"}]}

Example input:
Sentence: We used targeted next generation sequencing ( NGS ) , covering 24 candidate genes involved in neurodegenerative disorders , to analyze 40 probands with familial PD , and 10 patients with mixed neurodegenerative disorders .

Example answer:
{"entities": [{"text": "next generation sequencing", "type": "ResearchActivity"}, {"text": "NGS", "type": "ResearchActivity"}, {"text": "candidate genes", "type": "AnatomicalStructure"}, {"text": "neurodegenerative disorders", "type": "BiologicFunction"}, {"text": "familial PD", "type": "BiologicFunction"}]}

Input:
Sentence: Improved diagnostic yield of neuromuscular disorders applying clinical exome sequencing in patients arising from a consanguineous population Neuromuscular diseases ( NMDs ) include a broad range of disorders affecting muscles , nerves and neuromuscular junctions .

## Item MedMentions:test:549
Example input:
Sentence: Conventional and digital photo - stimulable phosphor ( PSP ; Optime ) radiographs and two CBCTs images ( NewTom 3 G and Cranex 3D ) were obtained from them .

Example answer:
{"entities": [{"text": "Conventional and digital photo - stimulable phosphor ( PSP ; Optime ) radiographs", "type": "HealthCareActivity"}, {"text": "CBCTs images", "type": "HealthCareActivity"}, {"text": "NewTom 3 G", "type": "MedicalDevice"}, {"text": "Cranex 3D", "type": "MedicalDevice"}]}

Example input:
Sentence: The Beck Depression Inventory - II was conducted and the concentration of serum magnesium was measured .

Example answer:
{"entities": [{"text": "Beck Depression Inventory - II", "type": "HealthCareActivity"}, {"text": "serum magnesium was measured", "type": "HealthCareActivity"}]}

Example input:
Sentence: Our aim was to compare BPs and the urinary excretion of albumin , calcium , and phosphate in preterm and term - born cohorts in early childhood .

Example answer:
{"entities": [{"text": "BPs", "type": "BiologicFunction"}, {"text": "excretion", "type": "BiologicFunction"}, {"text": "albumin", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "phosphate", "type": "Chemical"}, {"text": "term - born", "type": "BiologicFunction"}, {"text": "cohorts", "type": "PopulationGroup"}]}

Example input:
Sentence: Amorphous calcium phosphate ( ACP ) - based ones additionally protect against unwanted demineralization and actively support regeneration of hard tissue minerals .

Example answer:
{"entities": [{"text": "Amorphous calcium phosphate", "type": "Chemical"}, {"text": "ACP", "type": "Chemical"}, {"text": "unwanted", "type": "Finding"}, {"text": "demineralization", "type": "BiologicFunction"}, {"text": "regeneration", "type": "BiologicFunction"}, {"text": "hard tissue", "type": "AnatomicalStructure"}, {"text": "minerals", "type": "Chemical"}]}

Example input:
Sentence: There was a significant reduction in the intake of macro and micronutrients , with a high prevalence of inadequacy , of up to 100 % , for calcium , iron , phosphorus , magnesium , niacin , riboflavin , thiamin , vitamin B6 , vitamin C and zinc .

Example answer:
{"entities": [{"text": "micronutrients", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "iron", "type": "Chemical"}, {"text": "phosphorus", "type": "Chemical"}, {"text": "magnesium", "type": "Chemical"}, {"text": "niacin", "type": "Chemical"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "thiamin", "type": "Chemical"}, {"text": "vitamin B6", "type": "Chemical"}, {"text": "vitamin C", "type": "Chemical"}, {"text": "zinc", "type": "Chemical"}]}

Example input:
Sentence: Reclassification was highest for PTH , VDBP , and phosphorus ( all 7 . 5 % ) .

Example answer:
{"entities": [{"text": "Reclassification", "type": "IntellectualProduct"}, {"text": "PTH", "type": "Chemical"}, {"text": "VDBP", "type": "Chemical"}, {"text": "phosphorus", "type": "Chemical"}]}

Example input:
Sentence: Stone formation was assessed by increase in the levels of calcium and phosphorous in the urine and accumulation of nitrogenous substances like urea , creatinine in renal tissues and blood .

Example answer:
{"entities": [{"text": "Stone", "type": "BodySubstance"}, {"text": "calcium", "type": "Chemical"}, {"text": "phosphorous", "type": "Chemical"}, {"text": "urine", "type": "BodySubstance"}, {"text": "accumulation", "type": "Finding"}, {"text": "nitrogenous substances", "type": "Chemical"}, {"text": "urea", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "renal tissues", "type": "AnatomicalStructure"}, {"text": "blood", "type": "BodySubstance"}]}

Example input:
Sentence: We compared clinicopathological features ; preoperative calcium , parathyroid hormone ( PTH ) , phosphorus , vitamin D , 24 - hour urine calcium , and alkaline phosphatase levels ; postoperative calcium and PTH levels ; pathologic diagnosis ; multiplicity ; and results of a localization study between the 2 groups .

Example answer:
{"entities": [{"text": "clinicopathological", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "calcium", "type": "HealthCareActivity"}, {"text": "parathyroid hormone", "type": "HealthCareActivity"}, {"text": "PTH", "type": "HealthCareActivity"}, {"text": "phosphorus", "type": "HealthCareActivity"}, {"text": "vitamin D", "type": "HealthCareActivity"}, {"text": "24 - hour urine calcium", "type": "HealthCareActivity"}, {"text": "alkaline phosphatase levels", "type": "Finding"}, {"text": "PTH levels", "type": "HealthCareActivity"}, {"text": "localization study", "type": "ResearchActivity"}]}

Example input:
Sentence: Urinary albumin ( mg / L ) , calcium and phosphate levels indexed to creatinine ( mg / dL ) , and BP were measured .

Example answer:
{"entities": [{"text": "Urinary albumin", "type": "Finding"}, {"text": "calcium", "type": "Finding"}, {"text": "phosphate levels", "type": "Finding"}, {"text": "indexed", "type": "IntellectualProduct"}, {"text": "creatinine", "type": "Chemical"}, {"text": "BP", "type": "BiologicFunction"}]}

Example input:
Sentence: Elemental concentrations of barium , calcium , iron , potassium , magnesium , zinc and phosphorus in porcine bone ( as an experimental analog for human bone ) were analyzed by inductively coupled plasma optical emission spectroscopy ( ICP - OES ) .

Example answer:
{"entities": [{"text": "Elemental", "type": "Chemical"}, {"text": "barium", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "iron", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "magnesium", "type": "Chemical"}, {"text": "zinc", "type": "Chemical"}, {"text": "phosphorus", "type": "Chemical"}, {"text": "porcine", "type": "Eukaryote"}, {"text": "bone", "type": "AnatomicalStructure"}, {"text": "analog", "type": "Chemical"}, {"text": "human", "type": "Eukaryote"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Input:
Sentence: Calcium , magnesium , and phosphorus were obtained from medical record .

## Item MedMentions:test:186
Example input:
Sentence: The air - seawater gas exchange fluxes were dominated by net volatilization from seawater to air for TCEP ( mean , 146 ± 239 ng / m2 / day ) , TCPP ( mean , 1670 ± 3031 ng / m2 / day ) , TiBP ( mean , 537 ± 581 ng / m2 / day ) and TnBP ( mean , 230 ± 254 ng / m2 / day ) .

Example answer:
{"entities": [{"text": "TCEP", "type": "Chemical"}, {"text": "TCPP", "type": "Chemical"}, {"text": "TiBP", "type": "Chemical"}, {"text": "TnBP", "type": "Chemical"}]}

Example input:
Sentence: The authors used an equilibrium partitioning ( EqP ) approach to generate predicted PCB sediment effect concentrations ( largely Aroclor 1254 ) associated with a gradient of toxic effects in benthic organisms from effects observed in aquatic toxicity studies .

Example answer:
{"entities": [{"text": "equilibrium partitioning ( EqP ) approach", "type": "IntellectualProduct"}, {"text": "PCB", "type": "Chemical"}, {"text": "Aroclor 1254", "type": "Chemical"}, {"text": "toxic effects", "type": "InjuryOrPoisoning"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: Growth occurred at 5 - 35 ° C ( optimum 30 ° C ) , at pH 6 .

Example answer:
{"entities": [{"text": "Growth", "type": "BiologicFunction"}]}

Example input:
Sentence: Fermentation resulted in the production of hydrolysates that demonstrated excellent solubility ( 90 . 7 % ) , good foaming capacity ( 36 . 7 % ) and emulsification activity ( 94 . 6 m ( 2 ) / g ) .

Example answer:
{"entities": [{"text": "Fermentation", "type": "BiologicFunction"}, {"text": "hydrolysates", "type": "Chemical"}, {"text": "emulsification activity", "type": "HealthCareActivity"}]}

Example input:
Sentence: 67gkg ( - 1 ) ) than aboveground biomass ( 0 . 20gkg ( - 1 ) ) and that the belowground net primary productivity ( BNPP ) was 8 - 15 times the aboveground net primary productivity ( ANPP ) .

Example answer:
{"entities": []}

Example input:
Sentence: how nutrient enrichment ( i . e . , nitrogen availability ) affected the growth of Fucus vesiculosus , a foundational macroalgal species in the North Atlantic rocky intertidal zone , and found that nutrient -enriched algal blades showed a significant increase in tissue growth compared to individuals grown under ambient conditions .

Example answer:
{"entities": [{"text": "nutrient", "type": "Food"}, {"text": "nitrogen", "type": "Chemical"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "Fucus vesiculosus", "type": "Eukaryote"}, {"text": "macroalgal", "type": "Eukaryote"}, {"text": "species", "type": "Eukaryote"}, {"text": "North Atlantic rocky intertidal zone", "type": "SpatialConcept"}, {"text": "algal blades", "type": "IntellectualProduct"}, {"text": "tissue growth", "type": "BiologicFunction"}]}

Example input:
Sentence: 5 - 0 . 6 day ( - 1 ) ) , that is , growth available to support larger ( mesozooplankton ) consumer biomass .

Example answer:
{"entities": [{"text": "growth", "type": "BiologicFunction"}, {"text": "mesozooplankton", "type": "Eukaryote"}]}

Example input:
Sentence: Mixed - layer growth rates of Prochlorococcus and Synechococcus were largely balanced by mortality , whereas eukaryotic phytoplankton showed positive net growth ( ∼0 .

Example answer:
{"entities": [{"text": "Mixed - layer", "type": "SpatialConcept"}, {"text": "Prochlorococcus", "type": "Bacterium"}, {"text": "Synechococcus", "type": "Bacterium"}, {"text": "eukaryotic phytoplankton", "type": "Eukaryote"}, {"text": "positive", "type": "Finding"}, {"text": "net growth", "type": "BiologicFunction"}]}

Example input:
Sentence: Phytoplankton production and taxon - specific growth rates in the Costa Rica Dome During summer 2010 , we investigated phytoplankton production and growth rates at 19 stations in the eastern tropical Pacific , where winds and strong opposing currents generate the Costa Rica Dome ( CRD ) , an open - ocean upwelling feature .

Example answer:
{"entities": [{"text": "Phytoplankton", "type": "Eukaryote"}, {"text": "Costa Rica Dome", "type": "SpatialConcept"}, {"text": "phytoplankton", "type": "Eukaryote"}, {"text": "CRD", "type": "SpatialConcept"}, {"text": "open", "type": "SpatialConcept"}, {"text": "ocean", "type": "SpatialConcept"}]}

Example input:
Sentence: These are the first group - specific phytoplankton rate estimates in this region , and they demonstrate that integrated primary production is high , exceeding 1 g C m ( - 2 ) day ( - 1 ) on average , even during a period of reduced upwelling .

Example answer:
{"entities": [{"text": "phytoplankton", "type": "Eukaryote"}, {"text": "region", "type": "SpatialConcept"}]}

Input:
Sentence: Primary production ( ( 14 ) C - incorporation ) and group - specific growth and net growth rates ( two - treatment seawater dilution method ) were estimated from samples incubated in situ at eight depths .

## Item MedMentions:test:531
Example input:
Sentence: Furthermore , the self - reference effect on functional connectivity between the left inferior frontal cortex and frontopolar cortices was significantly enhanced in TD taking the 3P perspective , whereas such effect was reversed in ASD .

Example answer:
{"entities": [{"text": "left", "type": "SpatialConcept"}, {"text": "inferior frontal cortex", "type": "SpatialConcept"}, {"text": "frontopolar cortices", "type": "SpatialConcept"}, {"text": "ASD", "type": "BiologicFunction"}]}

Example input:
Sentence: The AD brains have significantly higher local connectivity than healthy controls in alpha and beta bands .

Example answer:
{"entities": [{"text": "AD", "type": "BiologicFunction"}, {"text": "brains", "type": "AnatomicalStructure"}, {"text": "alpha", "type": "SpatialConcept"}, {"text": "beta bands", "type": "SpatialConcept"}]}

Example input:
Sentence: The statistical significance was observed in the change in S - wave magnitude in the right precordial leads in both subsets of patients before AVR .

Example answer:
{"entities": [{"text": "S - wave", "type": "Finding"}, {"text": "AVR", "type": "HealthCareActivity"}]}

Example input:
Sentence: Finally , in 12 SD patients in whom PET was available , a strong correlation between FDG uptake and face - to - name and voice - to - name matching data was found in the right but not in the left temporal lobe .

Example answer:
{"entities": [{"text": "SD", "type": "BiologicFunction"}, {"text": "PET", "type": "HealthCareActivity"}, {"text": "FDG uptake", "type": "Chemical"}, {"text": "right", "type": "AnatomicalStructure"}, {"text": "left temporal lobe", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Moreover , patients in the S + EX group displayed greater increases of different HRV indices ( RR , pNN50 , RMSSD , SDHR , SDNN , HF , and LF ) compared with those in the S group .

Example answer:
{"entities": [{"text": "indices", "type": "IntellectualProduct"}]}

Example input:
Sentence: We utilized RS - fMRI to measure the amplitude of low - frequency fluctuation ( ALFF ) and the fractional ALFF ( fALFF ) in 51 patients with PD and 50 age - and sex -matched healthy controls .

Example answer:
{"entities": [{"text": "RS - fMRI", "type": "HealthCareActivity"}, {"text": "amplitude", "type": "SpatialConcept"}, {"text": "fluctuation", "type": "Finding"}, {"text": "ALFF", "type": "Finding"}, {"text": "fALFF", "type": "Finding"}, {"text": "PD", "type": "BiologicFunction"}]}

Example input:
Sentence: However , when considering only tremor -periods significantly more afferent than efferent connections were associated with coherence from 12 to 20Hz across all recording heights .

Example answer:
{"entities": [{"text": "tremor", "type": "Finding"}, {"text": "afferent", "type": "SpatialConcept"}, {"text": "efferent", "type": "SpatialConcept"}, {"text": "connections", "type": "SpatialConcept"}, {"text": "coherence", "type": "BiologicFunction"}]}

Example input:
Sentence: No difference between efferent and afferent connections is seen in the frequency range from 4 to 12Hz for all recording heights .

Example answer:
{"entities": [{"text": "efferent", "type": "SpatialConcept"}, {"text": "afferent", "type": "SpatialConcept"}, {"text": "connections", "type": "SpatialConcept"}]}

Example input:
Sentence: Within the STN 74 % and 63 % of the afferent connections are associated with coherence from 4 - 8Hz and 8 - 12Hz , respectively .

Example answer:
{"entities": [{"text": "STN", "type": "AnatomicalStructure"}, {"text": "afferent", "type": "SpatialConcept"}, {"text": "connections", "type": "SpatialConcept"}, {"text": "coherence", "type": "BiologicFunction"}]}

Example input:
Sentence: Still , for the AR patients dorsal of the STN significantly more afferent than efferent connections were associated with coherence in the frequency range from 12 to 16Hz .

Example answer:
{"entities": [{"text": "AR", "type": "BiologicFunction"}, {"text": "dorsal", "type": "SpatialConcept"}, {"text": "STN", "type": "AnatomicalStructure"}, {"text": "afferent", "type": "SpatialConcept"}, {"text": "efferent", "type": "SpatialConcept"}, {"text": "connections", "type": "SpatialConcept"}, {"text": "coherence", "type": "BiologicFunction"}]}

Input:
Sentence: For the AR patients , no significant difference in afferent and efferent connections within the STN was found for the different frequency bands .

## Item MedMentions:test:545
Example input:
Sentence: Traumatic Brain Injury Induces Alterations in Cortical Glutamate Uptake without a Reduction in Glutamate Transporter - 1 Protein Expression We hypothesize that the primary mechanism for removal of glutamate from the extracellular space is altered after traumatic brain injury ( TBI ) .

Example answer:
{"entities": [{"text": "Traumatic Brain Injury", "type": "InjuryOrPoisoning"}, {"text": "Cortical", "type": "AnatomicalStructure"}, {"text": "Glutamate", "type": "Chemical"}, {"text": "Uptake", "type": "BiologicFunction"}, {"text": "Glutamate Transporter - 1 Protein", "type": "Chemical"}, {"text": "Expression", "type": "BiologicFunction"}, {"text": "glutamate", "type": "Chemical"}, {"text": "extracellular space", "type": "SpatialConcept"}, {"text": "traumatic brain injury", "type": "InjuryOrPoisoning"}, {"text": "TBI", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: CA3 cells also exhibited increased intrinsic excitability .

Example answer:
{"entities": [{"text": "CA3 cells", "type": "AnatomicalStructure"}, {"text": "increased intrinsic excitability", "type": "Finding"}]}

Example input:
Sentence: Taken together , our data suggest diminished activity of glutamate transporters in the prefrontal cortex , with no changes in protein expression of the primary glutamate transporter GLT - 1 , and global alteration s in signaling networks that include serine - threonine kinases that are known modulators of glutamate transport activity .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "prefrontal cortex", "type": "AnatomicalStructure"}, {"text": "no changes", "type": "Finding"}, {"text": "protein expression", "type": "BiologicFunction"}, {"text": "glutamate transporter", "type": "Chemical"}, {"text": "GLT - 1", "type": "Chemical"}, {"text": "signaling networks", "type": "BiologicFunction"}, {"text": "serine - threonine kinases", "type": "Chemical"}, {"text": "modulators", "type": "Chemical"}, {"text": "glutamate transport activity", "type": "BiologicFunction"}]}

Example input:
Sentence: An analysis of the spontaneous glutamatergic and gamma - aminobutyric acid -mediated currents on CA3 cells reveal a dramatic alteration in amplitude and frequency of the nonevoked events .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "glutamatergic", "type": "Chemical"}, {"text": "gamma - aminobutyric acid", "type": "Chemical"}, {"text": "CA3 cells", "type": "AnatomicalStructure"}, {"text": "alteration", "type": "Finding"}]}

Example input:
Sentence: In the ipsilateral cortex and hippocampus , we found no differences in expression of the primary glutamate transporter in the brain ( GLT - 1 ) 24 h after TBI .

Example answer:
{"entities": [{"text": "ipsilateral", "type": "SpatialConcept"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "primary glutamate transporter", "type": "Chemical"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "GLT - 1", "type": "Chemical"}, {"text": "TBI", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The hippocampus is a structure involved in exercise , which can improve synaptic plasticity and long - term potentiation ( LTP ) .

Example answer:
{"entities": [{"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "improve", "type": "Finding"}, {"text": "synaptic plasticity", "type": "BiologicFunction"}, {"text": "long - term potentiation", "type": "BiologicFunction"}, {"text": "LTP", "type": "BiologicFunction"}]}

Example input:
Sentence: Together , these results demonstrate that aging is accompanied by a decrease in the GABAergic inhibition , reduced expression of short - and long - term forms of synaptic plasticity , and increased intrinsic excitability .

Example answer:
{"entities": [{"text": "aging", "type": "BiologicFunction"}, {"text": "GABAergic inhibition", "type": "BiologicFunction"}, {"text": "synaptic plasticity", "type": "BiologicFunction"}, {"text": "increased intrinsic excitability", "type": "Finding"}]}

Example input:
Sentence: Effect of exercise , exercise withdrawal , and continued regular exercise on excitability and long - term potentiation in the dentate gyrus of hippocampus Exercise mediates beneficial effects on the brain function and neural health , particularly in the hippocampus as the main area of memory .

Example answer:
{"entities": [{"text": "excitability", "type": "Finding"}, {"text": "long - term potentiation", "type": "BiologicFunction"}, {"text": "dentate gyrus", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "main area", "type": "SpatialConcept"}, {"text": "memory", "type": "BiologicFunction"}]}

Example input:
Sentence: The present study investigated the effect of exercise , exercise withdrawal , and continued regular exercise on excitability and long - term potentiation in the dentate gyrus ( DG ) of hippocampus .

Example answer:
{"entities": [{"text": "present", "type": "Finding"}, {"text": "study", "type": "ResearchActivity"}, {"text": "excitability", "type": "Finding"}, {"text": "long - term potentiation", "type": "BiologicFunction"}, {"text": "dentate gyrus", "type": "AnatomicalStructure"}, {"text": "DG", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In contrast , we found a decrease in glutamate uptake in the cortex , but not the hippocampus , 24 h after injury .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "uptake", "type": "BiologicFunction"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: Finally , hippocampal glutamate and GABA were evaluated to study excitability changes .

## Item MedMentions:test:801
Example input:
Sentence: 4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: 27 . 7±4 . 8 % ; 34 . 8±2 .

Example answer:
{"entities": []}

Example input:
Sentence: 4 % )

Example answer:
{"entities": []}

Example input:
Sentence: 4 % )

Example answer:
{"entities": []}

Example input:
Sentence: 4 % , 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 4 % and 92 .

Example answer:
{"entities": []}

Example input:
Sentence: 4 % , 96 .

Example answer:
{"entities": []}

Example input:
Sentence: 9 mol % .

Example answer:
{"entities": []}

Example input:
Sentence: 8 mol % .

Example answer:
{"entities": []}

Example input:
Sentence: 5 mol % .

Example answer:
{"entities": []}

Input:
Sentence: 4 mol % .

## Item MedMentions:test:452
Example input:
Sentence: KEGG pathway analysis showed that DHA may induce the apoptosis of cancer cells preferentially through mediating P53 , MAPK , TNF , PI3K / AKT , and NF - κB signaling pathways .

Example answer:
{"entities": [{"text": "DHA", "type": "Chemical"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "cancer cells", "type": "AnatomicalStructure"}, {"text": "P53", "type": "BiologicFunction"}, {"text": "MAPK", "type": "BiologicFunction"}, {"text": "TNF", "type": "BiologicFunction"}, {"text": "NF - κB signaling pathways", "type": "BiologicFunction"}]}

Example input:
Sentence: Compared to HMEC , MDA - MB - 231 cells overexpress the ectonucleotidases ENPP1 and CD73 , which convert extracellular ATP released by the cells to adenosine that stimulates A3 receptors and promotes cell migration with frequent directional changes .

Example answer:
{"entities": [{"text": "HMEC", "type": "AnatomicalStructure"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "overexpress", "type": "BiologicFunction"}, {"text": "ectonucleotidases ENPP1", "type": "Chemical"}, {"text": "CD73", "type": "Chemical"}, {"text": "extracellular", "type": "AnatomicalStructure"}, {"text": "ATP", "type": "Chemical"}, {"text": "adenosine", "type": "Chemical"}, {"text": "A3 receptors", "type": "Chemical"}, {"text": "cell migration", "type": "BiologicFunction"}, {"text": "directional", "type": "BiologicFunction"}]}

Example input:
Sentence: Under these conditions , pep5 is able to interact with different intracellular proteins , primarily cytoskeleton and proteasome components , which can lead to cellular apoptosis .

Example answer:
{"entities": [{"text": "pep5", "type": "Chemical"}, {"text": "intracellular", "type": "SpatialConcept"}, {"text": "proteins", "type": "Chemical"}, {"text": "cytoskeleton", "type": "AnatomicalStructure"}, {"text": "proteasome components", "type": "Chemical"}, {"text": "cellular apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: While neutrophils and benign human mammary epithelial cells ( HMEC ) form a single leading edge , MDA - MB - 231 breast cancer cells possess multiple leading edges enriched with A3 adenosine receptors .

Example answer:
{"entities": [{"text": "neutrophils", "type": "AnatomicalStructure"}, {"text": "human mammary", "type": "AnatomicalStructure"}, {"text": "epithelial cells", "type": "AnatomicalStructure"}, {"text": "HMEC", "type": "AnatomicalStructure"}, {"text": "leading edge", "type": "AnatomicalStructure"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "breast cancer cells", "type": "AnatomicalStructure"}, {"text": "leading edges", "type": "AnatomicalStructure"}, {"text": "A3 adenosine receptors", "type": "Chemical"}]}

Example input:
Sentence: These interactions could explain the long - lasting ERK1 / 2 phosphorylation and the cytoskeleton perturbations in the MDA - MB - 231 cells , in which the stress fibers ' integrity is affected by pep5 treatments .

Example answer:
{"entities": [{"text": "ERK1 / 2", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "cytoskeleton", "type": "AnatomicalStructure"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "stress fibers", "type": "AnatomicalStructure"}, {"text": "pep5", "type": "Chemical"}, {"text": "treatments", "type": "HealthCareActivity"}]}

Example input:
Sentence: Fluorescently labeled pep5 , monitored by real time confocal microscopy , entered the MDA - MB - 231 cells 3min after application and localized to the nucleus and cytoplasm .

Example answer:
{"entities": [{"text": "Fluorescently labeled", "type": "HealthCareActivity"}, {"text": "pep5", "type": "Chemical"}, {"text": "real time confocal microscopy", "type": "HealthCareActivity"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "localized", "type": "SpatialConcept"}, {"text": "nucleus", "type": "AnatomicalStructure"}, {"text": "cytoplasm", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Pep5 , a peptide derived from Cyclin D2 , induces cell death in tumor cell lines and reduces the volume of rat C6 glioblastoma tumors in vivo .

Example answer:
{"entities": [{"text": "Pep5", "type": "Chemical"}, {"text": "peptide", "type": "Chemical"}, {"text": "Cyclin D2", "type": "Chemical"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "tumor cell lines", "type": "AnatomicalStructure"}, {"text": "rat", "type": "Eukaryote"}, {"text": "C6 glioblastoma tumors", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: Pep5 induced permanent extracellular signal - regulated kinase ( ERK1 / 2 ) phosphorylation in MDA - MB - 231 cells synchronized in G1 / S or S phase .

Example answer:
{"entities": [{"text": "Pep5", "type": "Chemical"}, {"text": "extracellular signal - regulated kinase", "type": "Chemical"}, {"text": "ERK1 / 2", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "G1 / S", "type": "BiologicFunction"}]}

Example input:
Sentence: Pep5 , a natural intracellular peptide formed by the degradation of Cyclin D2 through the ubiquitin - proteasome system , induces cell death when reintroduced into MDA - MB - 231 breast cancer cells , which express low levels of Cyclin D2 , specifically in G1 / S arrested cells or in cells that are passing through S phase .

Example answer:
{"entities": [{"text": "Pep5", "type": "Chemical"}, {"text": "intracellular", "type": "SpatialConcept"}, {"text": "peptide", "type": "Chemical"}, {"text": "degradation of Cyclin D2", "type": "BiologicFunction"}, {"text": "ubiquitin - proteasome system", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "breast cancer cells", "type": "AnatomicalStructure"}, {"text": "Cyclin D2", "type": "Chemical"}, {"text": "G1 / S", "type": "BiologicFunction"}, {"text": "arrested cells", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Pep5 - induced cell death was increased when the MDA - MB - 231 cell population was arrested at the G1 / S transition or in S phase compared to asynchronous cells .

Example answer:
{"entities": [{"text": "Pep5", "type": "Chemical"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "cell population", "type": "AnatomicalStructure"}, {"text": "G1 / S transition", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Input:
Sentence: Here , we chose the human MDA - MB - 231 breast cancer cells to evaluate the mechanism of cell death induced by pep5 in different phases of the cell cycle .

## Item MedMentions:test:579
Example input:
Sentence: Cancerous lesions were larger ( median volume : 0 . 40 vs .

Example answer:
{"entities": [{"text": "Cancerous", "type": "BiologicFunction"}, {"text": "lesions", "type": "Finding"}]}

Example input:
Sentence: Compared to cognitively preserved ( CP ) , CI patients had higher T2 WM lesion volume ( LV ) , lower NBV and GMV , and more severe diffusivity abnormalities in WM lesions , cortex , and NAWM .

Example answer:
{"entities": [{"text": "CI", "type": "BiologicFunction"}, {"text": "abnormalities", "type": "AnatomicalStructure"}, {"text": "WM lesions", "type": "Finding"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "NAWM", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Focal WM and cortical lesions were identified , and volumetric measures from WM , cortical GM , the hippocampus , and deep GM nuclei were obtained .

Example answer:
{"entities": [{"text": "WM", "type": "AnatomicalStructure"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "lesions", "type": "Finding"}, {"text": "volumetric", "type": "SpatialConcept"}, {"text": "GM", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "deep GM", "type": "AnatomicalStructure"}, {"text": "nuclei", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Nuclear area , circumference , and PPC algorithm findings distinguished lesions in a statistically significant manner .

Example answer:
{"entities": [{"text": "Nuclear area", "type": "Finding"}, {"text": "PPC algorithm", "type": "IntellectualProduct"}, {"text": "lesions", "type": "Finding"}]}

Example input:
Sentence: Men with elevated prostate - specific antigen or abnormal digital rectal exam underwent a 3 T multiparametric magnetic resonance imaging ( mpMRI ) with endorectal coil .

Example answer:
{"entities": [{"text": "Men", "type": "PopulationGroup"}, {"text": "prostate - specific antigen", "type": "Chemical"}, {"text": "abnormal digital rectal exam", "type": "HealthCareActivity"}, {"text": "3 T multiparametric magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "mpMRI", "type": "HealthCareActivity"}, {"text": "endorectal coil", "type": "MedicalDevice"}]}

Example input:
Sentence: Future follow - up studies are needed to assess longitudinal cancer risks of suspicious mpMRI lesions .

Example answer:
{"entities": [{"text": "follow - up studies", "type": "ResearchActivity"}, {"text": "longitudinal cancer", "type": "BiologicFunction"}, {"text": "mpMRI", "type": "HealthCareActivity"}, {"text": "lesions", "type": "Finding"}]}

Example input:
Sentence: 79 . Larger lesions were associated with higher risk PCa ( Gleason and D ' Amico ) and lower ADC ( all P < 0 . 0001 ) .

Example answer:
{"entities": [{"text": "lesions", "type": "Finding"}, {"text": "higher risk", "type": "Finding"}, {"text": "PCa", "type": "BiologicFunction"}, {"text": "Gleason and D ' Amico", "type": "IntellectualProduct"}, {"text": "lower ADC", "type": "Finding"}]}

Example input:
Sentence: We prospectively enrolled 312 men with lesions suspicious for cancer ( suspicion score 2 - 5 ) on mpMRI . MRI / ultrasound fusion - guided prostate biopsies were performed .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "lesions", "type": "Finding"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "mpMRI", "type": "HealthCareActivity"}, {"text": "MRI / ultrasound fusion - guided prostate biopsies", "type": "HealthCareActivity"}]}

Example input:
Sentence: The median ADC ( ×10 ( - 6 ) mm ( 2 ) /sec ) for lesions negative and positive for PCa were 984 . 5 and 666 .

Example answer:
{"entities": [{"text": "lesions", "type": "Finding"}, {"text": "PCa", "type": "BiologicFunction"}]}

Example input:
Sentence: To evaluate the performance of apparent diffusion coefficient ( ADC ) and lesion volume in potentially risk - stratifying patients with prostate cancer ( PCa ) .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "lesion volume", "type": "Finding"}, {"text": "stratifying", "type": "ResearchActivity"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "PCa", "type": "BiologicFunction"}]}

Input:
Sentence: The mean ADC of suspicious lesions on mpMRI was inversely correlated , while lesion volume had a direct correlation with PCa detection .

## Item MedMentions:test:499
Example input:
Sentence: It can be diagnosed by the complex shape of the RTA , by the membranous tegular extension , the long coiled embolus , the retrolateral incision on the cymbium , the long convoluted copulatory duct extending anteriorly to the copulatory openings and by the presence of paramedian epigynal pockets and of an anterior ridge on the epigynum .

Example answer:
{"entities": [{"text": "diagnosed", "type": "Finding"}, {"text": "shape", "type": "SpatialConcept"}, {"text": "RTA", "type": "AnatomicalStructure"}, {"text": "membranous tegular extension", "type": "AnatomicalStructure"}, {"text": "long coiled embolus", "type": "AnatomicalStructure"}, {"text": "retrolateral incision on the cymbium", "type": "AnatomicalStructure"}, {"text": "long convoluted copulatory duct", "type": "AnatomicalStructure"}, {"text": "anteriorly", "type": "SpatialConcept"}, {"text": "copulatory openings", "type": "AnatomicalStructure"}, {"text": "presence", "type": "Finding"}, {"text": "paramedian epigynal pockets", "type": "AnatomicalStructure"}, {"text": "anterior", "type": "SpatialConcept"}, {"text": "ridge", "type": "SpatialConcept"}, {"text": "epigynum", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Abnormalities confined to the posterior fossa according to USS were found in 81 fetuses ( 67 with parenchymal and 14 with CSF -containing lesions ) .

Example answer:
{"entities": [{"text": "Abnormalities confined to the posterior fossa", "type": "Finding"}, {"text": "USS", "type": "HealthCareActivity"}, {"text": "fetuses", "type": "AnatomicalStructure"}, {"text": "parenchymal", "type": "AnatomicalStructure"}, {"text": "CSF", "type": "BodySubstance"}, {"text": "lesions", "type": "Finding"}]}

Example input:
Sentence: In conclusion , central and Ewing sarcoma / peripheral PNETs may be encountered in the female genital tract with central PNETs being more common .

Example answer:
{"entities": [{"text": "central", "type": "BiologicFunction"}, {"text": "Ewing sarcoma / peripheral PNETs", "type": "BiologicFunction"}, {"text": "female genital tract", "type": "AnatomicalStructure"}, {"text": "central PNETs", "type": "BiologicFunction"}]}

Example input:
Sentence: An abdominopelvic computed tomography ( CT ) scan showed markedly enlarged seminal vesicles causing bilateral ureteral obstruction and a mildly enlarged prostate .

Example answer:
{"entities": [{"text": "abdominopelvic computed tomography ( CT ) scan", "type": "HealthCareActivity"}, {"text": "seminal vesicles", "type": "AnatomicalStructure"}, {"text": "bilateral ureteral", "type": "AnatomicalStructure"}, {"text": "obstruction", "type": "BiologicFunction"}, {"text": "prostate", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Whole slide images were obtained for colonic normal mucosa ( NCM ) , hyperplastic polyps ( HP ) , conventional tubular adenomas ( TA ) , and adenomas with high - grade dysplasia ( HGD ) , and esophageal intestinal metaplasia negative for dysplasia ( IM ) , indefinite for dysplasia ( IFD ) , low - grade dysplasia ( LGD ) , and HGD .

Example answer:
{"entities": [{"text": "slide images", "type": "IntellectualProduct"}, {"text": "hyperplastic polyps", "type": "BiologicFunction"}, {"text": "HP", "type": "BiologicFunction"}, {"text": "tubular adenomas", "type": "BiologicFunction"}, {"text": "TA", "type": "BiologicFunction"}, {"text": "adenomas", "type": "BiologicFunction"}, {"text": "high - grade dysplasia", "type": "BiologicFunction"}, {"text": "HGD", "type": "BiologicFunction"}, {"text": "esophageal intestinal metaplasia", "type": "BiologicFunction"}, {"text": "negative", "type": "Finding"}, {"text": "dysplasia", "type": "BiologicFunction"}, {"text": "IM", "type": "BiologicFunction"}, {"text": "indefinite for dysplasia", "type": "Finding"}, {"text": "IFD", "type": "Finding"}, {"text": "low - grade dysplasia", "type": "BiologicFunction"}, {"text": "LGD", "type": "BiologicFunction"}]}

Example input:
Sentence: 3 % ( 23 / 173 ) of posterior complex fistulas .

Example answer:
{"entities": [{"text": "posterior", "type": "SpatialConcept"}, {"text": "fistulas", "type": "AnatomicalStructure"}]}

Example input:
Sentence: MRI - based characteristics of selected perianal fistulas were independently evaluated by examiners who focused on lesions in these 2 spaces and were blinded to each other 's findings .

Example answer:
{"entities": [{"text": "MRI", "type": "HealthCareActivity"}, {"text": "perianal fistulas", "type": "AnatomicalStructure"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "examiners", "type": "ProfessionalOrOccupationalGroup"}, {"text": "lesions", "type": "Finding"}, {"text": "spaces", "type": "SpatialConcept"}]}

Example input:
Sentence: The deep posterior intersphincteric space is more likely than the deep postanal space to be involved in complex cryptoglandular fistulas and is likely to play a more important role in the management of complex cryptoglandular fistulas .

Example answer:
{"entities": [{"text": "deep posterior", "type": "SpatialConcept"}, {"text": "intersphincteric space", "type": "SpatialConcept"}, {"text": "deep postanal space", "type": "SpatialConcept"}, {"text": "cryptoglandular", "type": "AnatomicalStructure"}, {"text": "fistulas", "type": "AnatomicalStructure"}, {"text": "management", "type": "HealthCareActivity"}]}

Example input:
Sentence: The purpose of this study was to assess the clinical significance of the 2 deep posterior perianal spaces and to describe in detail the courses of posterior complex cryptoglandular fistula extensions .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "clinical significance", "type": "Finding"}, {"text": "deep posterior perianal spaces", "type": "SpatialConcept"}, {"text": "posterior", "type": "SpatialConcept"}, {"text": "cryptoglandular", "type": "AnatomicalStructure"}, {"text": "fistula", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Clinical Significance of 2 Deep Posterior Perianal Spaces to Complex Cryptoglandular Fistulas Confusion exists regarding the clinical significance of the deep posterior intersphincteric space and deep postanal space to complex perianal fistulas .

Example answer:
{"entities": [{"text": "Clinical Significance", "type": "Finding"}, {"text": "Deep Posterior Perianal Spaces", "type": "SpatialConcept"}, {"text": "Cryptoglandular", "type": "AnatomicalStructure"}, {"text": "Fistulas", "type": "AnatomicalStructure"}, {"text": "clinical significance", "type": "Finding"}, {"text": "deep posterior", "type": "SpatialConcept"}, {"text": "intersphincteric space", "type": "SpatialConcept"}, {"text": "deep postanal space", "type": "SpatialConcept"}, {"text": "perianal fistulas", "type": "AnatomicalStructure"}]}

Input:
Sentence: The occurrence rates of these 2 deep perianal space lesions in posterior cryptoglandular fistulas were determined .

## Item MedMentions:test:539
Example input:
Sentence: Seizures manifesting with unilateral blinking were focal motor in four patients , focal motor evolving into epileptic spasms in six , and epileptic spasms with focal features in one .

Example answer:
{"entities": [{"text": "Seizures", "type": "Finding"}, {"text": "unilateral", "type": "SpatialConcept"}, {"text": "blinking", "type": "BiologicFunction"}, {"text": "focal motor", "type": "Finding"}, {"text": "epileptic spasms", "type": "BiologicFunction"}, {"text": "focal features", "type": "Finding"}]}

Example input:
Sentence: To address this issue , we recorded high - density ECoG signals from patients undergoing epilepsy surgery evaluation as they performed elementary upper extremity movements while systematically varying movement speed and duration .

Example answer:
{"entities": [{"text": "issue", "type": "Finding"}, {"text": "ECoG", "type": "HealthCareActivity"}, {"text": "epilepsy", "type": "BiologicFunction"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "evaluation", "type": "HealthCareActivity"}, {"text": "upper extremity", "type": "AnatomicalStructure"}, {"text": "movements", "type": "BiologicFunction"}, {"text": "movement", "type": "BiologicFunction"}]}

Example input:
Sentence: Lateral hypothalamus orexinergic system modulates the stress effect on pentylenetetrazol induced seizures through corticotropin releasing hormone receptor type 1 Stress is a trigger factor for seizure initiation which activates hypothalamic pituitary adrenal ( HPA ) axis as well other brain areas .

Example answer:
{"entities": [{"text": "Lateral hypothalamus orexinergic system", "type": "BodySystem"}, {"text": "modulates", "type": "SpatialConcept"}, {"text": "stress", "type": "BiologicFunction"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "seizures", "type": "Finding"}, {"text": "corticotropin releasing hormone receptor type 1", "type": "Chemical"}, {"text": "Stress", "type": "BiologicFunction"}, {"text": "trigger factor for seizure", "type": "ClinicalAttribute"}, {"text": "hypothalamic pituitary adrenal ( HPA ) axis", "type": "BodySystem"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "areas", "type": "SpatialConcept"}]}

Example input:
Sentence: Eleven ( 12 % ) had seizures with unilateral blinking , of which 10 underwent epilepsy surgery .

Example answer:
{"entities": [{"text": "seizures", "type": "Finding"}, {"text": "unilateral", "type": "SpatialConcept"}, {"text": "blinking", "type": "BiologicFunction"}, {"text": "epilepsy", "type": "BiologicFunction"}, {"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: We aimed to determine its lateralizing utility in patients with tuberous sclerosis complex ( TSC ) .

Example answer:
{"entities": [{"text": "tuberous sclerosis complex", "type": "BiologicFunction"}, {"text": "TSC", "type": "BiologicFunction"}]}

Example input:
Sentence: Unrecognized seizure propagation to contralateral symptomatogenic regions and potentially different mechanisms may account for the variable lateralization .

Example answer:
{"entities": [{"text": "seizure", "type": "Finding"}, {"text": "contralateral", "type": "SpatialConcept"}, {"text": "symptomatogenic regions", "type": "SpatialConcept"}]}

Example input:
Sentence: Ictal unilateral blinking is an unreliable lateralizing sign in tuberous sclerosis complex Ictal unilateral blinking is an uncommon but reportedly reliable lateralizing sign , indicating an ipsilateral seizure focus .

Example answer:
{"entities": [{"text": "Ictal", "type": "Finding"}, {"text": "unilateral", "type": "SpatialConcept"}, {"text": "blinking", "type": "BiologicFunction"}, {"text": "tuberous sclerosis complex", "type": "BiologicFunction"}, {"text": "ipsilateral", "type": "SpatialConcept"}, {"text": "seizure focus", "type": "Finding"}]}

Example input:
Sentence: Ictal unilateral blinking is not infrequent but unreliable in lateralizing seizures in TSC .

Example answer:
{"entities": [{"text": "Ictal", "type": "Finding"}, {"text": "unilateral", "type": "SpatialConcept"}, {"text": "blinking", "type": "BiologicFunction"}, {"text": "seizures", "type": "Finding"}, {"text": "TSC", "type": "BiologicFunction"}]}

Example input:
Sentence: When unilateral blinking was early in seizures , overall lateralization was more often contralateral ( 6 / 7 patients , PPV 85 % ) .

Example answer:
{"entities": [{"text": "unilateral", "type": "SpatialConcept"}, {"text": "blinking", "type": "BiologicFunction"}, {"text": "seizures", "type": "Finding"}, {"text": "contralateral", "type": "SpatialConcept"}]}

Example input:
Sentence: Overall lateralization of seizures with unilateral blinking was contralateral in six patients and ipsilateral in four .

Example answer:
{"entities": [{"text": "seizures", "type": "Finding"}, {"text": "unilateral", "type": "SpatialConcept"}, {"text": "blinking", "type": "BiologicFunction"}, {"text": "contralateral", "type": "SpatialConcept"}]}

Input:
Sentence: Lateralization of seizures was inferred from other semiology , ictal scalp EEG and outcome following tuberectomy .

## Item MedMentions:test:572
Example input:
Sentence: This correlation was stronger for triple negative and HER2 / neu positive subtypes ( r = 0 . 92 and 0 . 62 , respectively ) .

Example answer:
{"entities": [{"text": "triple negative", "type": "BiologicFunction"}, {"text": "HER2 / neu positive", "type": "ClinicalAttribute"}, {"text": "subtypes", "type": "IntellectualProduct"}]}

Example input:
Sentence: The presence of the HLA - B27 antigen was determined in 142 ( 64 . 8 % ) out of 219 patients , of them 87 were diagnosed with an entity of the SpA group .

Example answer:
{"entities": [{"text": "presence", "type": "Finding"}, {"text": "HLA - B27 antigen", "type": "Chemical"}, {"text": "diagnosed", "type": "Finding"}, {"text": "SpA", "type": "BiologicFunction"}]}

Example input:
Sentence: For triple negative or HER2 / neu positive disease the sensitivity and specificity were 88 % ( 95 % CI , 62 - 98 ) and 75 % ( 95 % CI , 43 - 93 ) , respectively .

Example answer:
{"entities": [{"text": "triple negative", "type": "BiologicFunction"}, {"text": "HER2 / neu positive", "type": "ClinicalAttribute"}]}

Example input:
Sentence: 2 % ) patients appeared to be HLA - B27 - negative , but 13 were still diagnosed with an entity of the SpA group .

Example answer:
{"entities": [{"text": "HLA - B27", "type": "Chemical"}, {"text": "negative", "type": "Finding"}, {"text": "diagnosed", "type": "Finding"}, {"text": "SpA", "type": "BiologicFunction"}]}

Example input:
Sentence: Clinical Features and Complications of the HLA - B27 -associated Acute Anterior Uveitis : A Metanalysis In this article , we report a literature - based metanalysis we have conducted to outline the clinical features of the HLA - B27 Acute Anterior Uveitis ( AAU ) .

Example answer:
{"entities": [{"text": "Clinical Features", "type": "Finding"}, {"text": "Complications", "type": "BiologicFunction"}, {"text": "HLA - B27", "type": "Chemical"}, {"text": "Acute Anterior Uveitis", "type": "BiologicFunction"}, {"text": "Metanalysis", "type": "ResearchActivity"}, {"text": "article", "type": "IntellectualProduct"}, {"text": "literature - based", "type": "IntellectualProduct"}, {"text": "metanalysis", "type": "ResearchActivity"}, {"text": "clinical features", "type": "Finding"}, {"text": "AAU", "type": "BiologicFunction"}]}

Example input:
Sentence: Complications of uveitis are more likely to be found in non - SpA HLA - B27 - negative patients ( р < 0 . 0001 ) .

Example answer:
{"entities": [{"text": "Complications", "type": "BiologicFunction"}, {"text": "uveitis", "type": "BiologicFunction"}, {"text": "non - SpA", "type": "Finding"}, {"text": "HLA - B27", "type": "Chemical"}, {"text": "negative", "type": "Finding"}]}

Example input:
Sentence: Clinical presentation of uveitis in the presence of SpA in both HLA - B27 - positive and negative patients resembles that of idiopathic uveitis - an independent HLA - B27 - associated syndrome ( р > 0 . 05 ) .

Example answer:
{"entities": [{"text": "uveitis", "type": "BiologicFunction"}, {"text": "presence", "type": "Finding"}, {"text": "SpA", "type": "BiologicFunction"}, {"text": "negative", "type": "Finding"}, {"text": "idiopathic uveitis", "type": "BiologicFunction"}, {"text": "HLA - B27", "type": "Chemical"}, {"text": "syndrome", "type": "BiologicFunction"}]}

Example input:
Sentence: The results obtained remark some of the peculiar features linked to the HLA B27 Acute Anterior Uveitis , such as strong association with ankylosing spondylitis ( RR = 6 . 80 ) and systemic diseases ( RR = 9 . 9 ) , male prevalence ( RR = 1 . 2 ) , unilateral ( RR = 1 . 1 ) or alternating bilateral ( RR = 2 . 2 ) involvement , hypopion ( RR = 5 . 5 ) , fibrinous reaction and even papillitis ( R = 7 . 7 ) .

Example answer:
{"entities": [{"text": "HLA B27", "type": "Chemical"}, {"text": "Acute Anterior Uveitis", "type": "BiologicFunction"}, {"text": "ankylosing spondylitis", "type": "BiologicFunction"}, {"text": "systemic diseases", "type": "BiologicFunction"}, {"text": "unilateral", "type": "SpatialConcept"}, {"text": "bilateral", "type": "SpatialConcept"}, {"text": "hypopion", "type": "BiologicFunction"}, {"text": "fibrinous", "type": "Chemical"}, {"text": "papillitis", "type": "BiologicFunction"}]}

Example input:
Sentence: We also performed a comparison of HLA - B27 - positive and negative patients with no account to their SpA status and revealed a higher complication rate in those that were « negative » ( p < 0 . 0001 ) , which can be explained by the fact that HLA - B27 - negative patients often have autoimmune or infectious uveitis of different origin notable for long attacks and short remissions .

Example answer:
{"entities": [{"text": "negative", "type": "Finding"}, {"text": "SpA", "type": "BiologicFunction"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "HLA - B27", "type": "Chemical"}, {"text": "autoimmune", "type": "BiologicFunction"}, {"text": "infectious uveitis", "type": "BiologicFunction"}, {"text": "remissions", "type": "Finding"}]}

Example input:
Sentence: When comparing the two groups of HLA - B27 - positive and negative patients having both SpA and uveitis , no statistically significant difference was found as to the age of onset , site , frequency of attacks , and uni - or bilateral involvement ( p > 0 . 05 ) .

Example answer:
{"entities": [{"text": "negative", "type": "Finding"}, {"text": "SpA", "type": "BiologicFunction"}, {"text": "uveitis", "type": "BiologicFunction"}, {"text": "site", "type": "SpatialConcept"}, {"text": "uni", "type": "SpatialConcept"}, {"text": "bilateral", "type": "SpatialConcept"}]}

Input:
Sentence: Simultaneous bilateral ( RR = 0 . 3 ) AAU is more frequent in HLA - B27 negative form .

## Item MedMentions:test:584
Example input:
Sentence: Tobacco use and morbid obesity were the largest risk factors for deep and superficial infections , respectively ( P < .001 ; relative risk of 1 . 90 and 2 . 19 , respectively ) .

Example answer:
{"entities": [{"text": "morbid obesity", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "deep", "type": "BiologicFunction"}, {"text": "superficial infections", "type": "BiologicFunction"}]}

Example input:
Sentence: Animals underwent necropsy with blinded histomorphologic evaluation on days 0 , 3 , and 10 postprocedure to assess for presence of bowel perforation , depth of thermal injury , and extent of inflammatory response .

Example answer:
{"entities": [{"text": "Animals", "type": "Eukaryote"}, {"text": "necropsy", "type": "HealthCareActivity"}, {"text": "blinded", "type": "ResearchActivity"}, {"text": "histomorphologic evaluation", "type": "HealthCareActivity"}, {"text": "postprocedure to assess", "type": "Finding"}, {"text": "bowel perforation", "type": "BiologicFunction"}, {"text": "thermal injury", "type": "InjuryOrPoisoning"}, {"text": "inflammatory response", "type": "BiologicFunction"}]}

Example input:
Sentence: Incisional hernia developed in 16 of 51 patients ( 31 % ) with wound infection .

Example answer:
{"entities": [{"text": "Incisional hernia", "type": "BiologicFunction"}, {"text": "wound infection", "type": "BiologicFunction"}]}

Example input:
Sentence: All patients ≥18 years at the time of ACL reconstruction were identified using the American Medical Association Current Procedural Terminology ( CPT ) for ACL reconstruction ( CPT code 29888 ) over 7 years ( 2005 - 2011 ) .

Example answer:
{"entities": [{"text": "ACL reconstruction", "type": "HealthCareActivity"}, {"text": "American Medical Association", "type": "Organization"}, {"text": "Current Procedural Terminology", "type": "IntellectualProduct"}, {"text": "CPT", "type": "IntellectualProduct"}, {"text": "CPT code 29888", "type": "IntellectualProduct"}]}

Example input:
Sentence: Time to definitive abdominal closure was reduced in the PR group compared with the CR group ( 4 . 1 ± 2 . 2 days vs 5 . 9 ± 3 . 5 days ; p ≤ 0 . 002 ) .

Example answer:
{"entities": [{"text": "abdominal closure", "type": "HealthCareActivity"}, {"text": "PR", "type": "HealthCareActivity"}, {"text": "group", "type": "PopulationGroup"}, {"text": "CR", "type": "HealthCareActivity"}]}

Example input:
Sentence: The Netherlands Chlamydia cohort study ( NECCST ) protocol to assess the risk of late complications following Chlamydia trachomatis infection in women Chlamydia trachomatis ( CT ) , the most common bacterial sexually transmitted infection ( STI ) among young women , can result in serious sequelae .

Example answer:
{"entities": [{"text": "Netherlands Chlamydia cohort study", "type": "ResearchActivity"}, {"text": "NECCST", "type": "ResearchActivity"}, {"text": "protocol", "type": "IntellectualProduct"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "Chlamydia trachomatis infection", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "Chlamydia trachomatis", "type": "Bacterium"}, {"text": "CT", "type": "Bacterium"}, {"text": "bacterial sexually transmitted infection", "type": "BiologicFunction"}, {"text": "STI", "type": "BiologicFunction"}, {"text": "sequelae", "type": "BiologicFunction"}]}

Example input:
Sentence: Deep postoperative infections occurred at a rate of 0 . 22 % .

Example answer:
{"entities": [{"text": "postoperative infections", "type": "BiologicFunction"}]}

Example input:
Sentence: In the traditional drilling and drainage group , 13 patients were with hematoma recurrence within 3 months after the operation and 7 patients were with postoperative intracranial pneumocephalus .

Example answer:
{"entities": [{"text": "traditional drilling", "type": "HealthCareActivity"}, {"text": "drainage", "type": "HealthCareActivity"}, {"text": "hematoma", "type": "BiologicFunction"}, {"text": "recurrence", "type": "BiologicFunction"}, {"text": "operation", "type": "HealthCareActivity"}, {"text": "intracranial pneumocephalus", "type": "BiologicFunction"}]}

Example input:
Sentence: Superficial infections were identified by International Classification of Diseases , Ninth Revision infection codes without any record of incision and drainage .

Example answer:
{"entities": [{"text": "Superficial infections", "type": "BiologicFunction"}, {"text": "International Classification of Diseases , Ninth Revision infection codes", "type": "IntellectualProduct"}, {"text": "record", "type": "IntellectualProduct"}, {"text": "incision", "type": "HealthCareActivity"}, {"text": "drainage", "type": "HealthCareActivity"}]}

Example input:
Sentence: Each CPT code was designated as a high - or low - complexity procedure , with the former typically requiring accessory incisions or increased operative time .

Example answer:
{"entities": [{"text": "CPT code", "type": "IntellectualProduct"}, {"text": "high -", "type": "HealthCareActivity"}, {"text": "low - complexity procedure", "type": "HealthCareActivity"}, {"text": "incisions", "type": "HealthCareActivity"}]}

Input:
Sentence: Deep infections were identified by a CPT code for incision and drainage within 90 days of surgery .

## Item MedMentions:test:415
Example input:
Sentence: The Electrophoretic mobility shift assays ( EMSA ) and chromatin immunoprecipitation ( ChIP ) assays determined the MyoD binding site in Mef2c promoter .

Example answer:
{"entities": [{"text": "Electrophoretic mobility shift assays", "type": "HealthCareActivity"}, {"text": "EMSA", "type": "HealthCareActivity"}, {"text": "chromatin immunoprecipitation ( ChIP ) assays", "type": "HealthCareActivity"}, {"text": "MyoD", "type": "Chemical"}, {"text": "binding site", "type": "SpatialConcept"}, {"text": "Mef2c", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}]}

Example input:
Sentence: Our " chemical - compound -based " strategy successfully directs hiPSCs into expandable myoblasts , which exhibit a myogenic transcriptional program , forming striated contractile myofibers and participating in muscle regeneration in vivo .

Example answer:
{"entities": [{"text": "chemical - compound", "type": "Chemical"}, {"text": "strategy", "type": "ResearchActivity"}, {"text": "hiPSCs", "type": "AnatomicalStructure"}, {"text": "myoblasts", "type": "AnatomicalStructure"}, {"text": "myogenic transcriptional", "type": "BiologicFunction"}, {"text": "contractile", "type": "AnatomicalStructure"}, {"text": "myofibers", "type": "AnatomicalStructure"}, {"text": "muscle regeneration", "type": "Finding"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: Quantitative real - time PCR ( qRT - PCR ) revealed the expression pattern of Mef2c gene in muscle of eight tissues .

Example answer:
{"entities": [{"text": "Quantitative real - time PCR", "type": "ResearchActivity"}, {"text": "qRT - PCR", "type": "ResearchActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Mef2c gene", "type": "AnatomicalStructure"}, {"text": "muscle", "type": "AnatomicalStructure"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: These results advanced our knowledge of the promoter of the pig Mef2c gene .

Example answer:
{"entities": [{"text": "promoter", "type": "Chemical"}, {"text": "pig", "type": "Eukaryote"}, {"text": "Mef2c gene", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In order to further understand Mef2c gene , the promoter of pig Mef2c gene was analyzed in this paper .

Example answer:
{"entities": [{"text": "Mef2c gene", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "pig", "type": "Eukaryote"}]}

Example input:
Sentence: Myocyte enhancer factor 2 ( MEF2 ) proteins are reported that they have the potential contributions to adult muscle regeneration .

Example answer:
{"entities": [{"text": "Myocyte enhancer factor 2 ( MEF2 ) proteins", "type": "Chemical"}, {"text": "muscle regeneration", "type": "Finding"}]}

Example input:
Sentence: MEF2C could up - regulate the transcriptional activities of Mef2c promoter constructs which contained a 3 ' - end nucleotide sequence with p300 binding site .

Example answer:
{"entities": [{"text": "MEF2C", "type": "AnatomicalStructure"}, {"text": "up - regulate the transcriptional activities", "type": "BiologicFunction"}, {"text": "Mef2c", "type": "AnatomicalStructure"}, {"text": "promoter constructs", "type": "Chemical"}, {"text": "3 ' - end nucleotide sequence", "type": "SpatialConcept"}, {"text": "p300", "type": "Chemical"}, {"text": "binding site", "type": "SpatialConcept"}]}

Example input:
Sentence: Function deletion and mutation analyses showed that MyoD and MEF2 binding sites within the Mef2c promoter were responsible for the regulation of Mef2c transcription .

Example answer:
{"entities": [{"text": "deletion", "type": "BiologicFunction"}, {"text": "mutation", "type": "BiologicFunction"}, {"text": "analyses", "type": "ResearchActivity"}, {"text": "MyoD", "type": "Chemical"}, {"text": "MEF2", "type": "Chemical"}, {"text": "binding sites", "type": "SpatialConcept"}, {"text": "Mef2c", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "transcription", "type": "BiologicFunction"}]}

Example input:
Sentence: The Mef2c promoter had the higher transcriptional activity in differentiated C2C12 cells than that in proliferating C2C12 cells , which was accompanied by the up - regulation of mRNA expression of Mef2c gene .

Example answer:
{"entities": [{"text": "Mef2c", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "transcriptional activity", "type": "BiologicFunction"}, {"text": "differentiated", "type": "BiologicFunction"}, {"text": "C2C12 cells", "type": "AnatomicalStructure"}, {"text": "proliferating", "type": "BiologicFunction"}, {"text": "up - regulation", "type": "BiologicFunction"}, {"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "Mef2c gene", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Function analysis of Mef2c promoter in muscle differentiation Regeneration of adult skeletal muscle following injury occurs through the activation of satellite cells , that proliferates , differentiates , and fuses with injured myofibers .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "Mef2c", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "muscle differentiation", "type": "BiologicFunction"}, {"text": "Regeneration of adult skeletal muscle", "type": "BiologicFunction"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "satellite cells", "type": "AnatomicalStructure"}, {"text": "proliferates", "type": "BiologicFunction"}, {"text": "differentiates", "type": "BiologicFunction"}, {"text": "fuses", "type": "BiologicFunction"}, {"text": "myofibers", "type": "AnatomicalStructure"}]}

Input:
Sentence: And the study of Mef2c promoter regulator elements helped to elucidating the regulation mechanisms of Mef2c in muscle differentiation or muscle repair and regeneration .

## Item MedMentions:test:208
Example input:
Sentence: The health - related quality of life ( HRQOL ) was measured using the European Organization for Research and Treatment of Cancer ( EORTC ) QLQ - C30 and its breast module BR - 23 .

Example answer:
{"entities": [{"text": "European Organization for Research and Treatment of Cancer", "type": "Organization"}, {"text": "EORTC", "type": "Organization"}, {"text": "QLQ - C30", "type": "IntellectualProduct"}, {"text": "breast module BR - 23", "type": "IntellectualProduct"}]}

Example input:
Sentence: We evaluated the outcome of elderly patients who benefited from ICOAS for a strictly palliative goal METHODS : We performed a national retrospective cohort study in France of patients aged > 75years old with PJI , and managed with ICOAS planned for life long from 2009 to 2014 , and compared the population with an event versus the population free of event .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "elderly", "type": "PopulationGroup"}, {"text": "ICOAS", "type": "HealthCareActivity"}, {"text": "palliative goal", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "national retrospective cohort study", "type": "ResearchActivity"}, {"text": "France", "type": "SpatialConcept"}, {"text": "PJI", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: As health - related quality - of - life ( HRQoL ) concerns are paramount when selecting among treatment options for low - risk PCa , this study examined HRQoL outcomes in men undergoing EBRT as compared to AS in a prospective , racially diverse cohort .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "PCa", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "examined", "type": "Finding"}, {"text": "EBRT", "type": "HealthCareActivity"}, {"text": "AS", "type": "HealthCareActivity"}, {"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: The median number of days from initial consult to death increased from 52 days ( 2008 ) to 223 days ( 2014 ) .

Example answer:
{"entities": [{"text": "death", "type": "Finding"}]}

Example input:
Sentence: HRQoL was evaluated at baseline and every 6 weeks while on treatment using the European Organisation for Research and Treatment of Care ( EORTC ) Core Quality of Life Questionnaire ( QLQ - C30 ) and the EuroQoL Five Dimensions Questionnaire ( EQ - 5D ) .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "European Organisation for Research and Treatment of Care ( EORTC ) Core Quality of Life Questionnaire ( QLQ - C30 )", "type": "IntellectualProduct"}, {"text": "EuroQoL Five Dimensions Questionnaire", "type": "IntellectualProduct"}, {"text": "EQ - 5D", "type": "IntellectualProduct"}]}

Example input:
Sentence: An online survey was completed by members of the National Hospice and Palliative Care Organization ( NHPCO ) which inquired about personal ritual practices , and included the Professional Quality of Life ( ProQOL ) scale to measure current levels of Compassion Satisfaction , Burnout , and Secondary Traumatic Stress .

Example answer:
{"entities": [{"text": "online survey", "type": "IntellectualProduct"}, {"text": "Hospice", "type": "HealthCareActivity"}, {"text": "Professional Quality of Life ( ProQOL ) scale", "type": "IntellectualProduct"}, {"text": "Satisfaction", "type": "BiologicFunction"}, {"text": "Burnout", "type": "Finding"}, {"text": "Secondary Traumatic Stress", "type": "BiologicFunction"}]}

Example input:
Sentence: We retrospectively reviewed records of patients seen by the QoLS ( n = 615 ) from March 2007 to December 2014 .

Example answer:
{"entities": [{"text": "records of patients", "type": "IntellectualProduct"}, {"text": "QoLS", "type": "HealthCareActivity"}]}

Example input:
Sentence: Improving end - of - life care through quality improvement Although end of life ( EoL ) care has been identified as an area for quality improvement in hospitals , the quality of care Canadian patients receive at the end of life is not well - evidenced .

Example answer:
{"entities": [{"text": "end - of - life care", "type": "HealthCareActivity"}, {"text": "end of life ( EoL ) care", "type": "HealthCareActivity"}, {"text": "hospitals", "type": "Organization"}, {"text": "quality of care", "type": "HealthCareActivity"}, {"text": "end of life", "type": "HealthCareActivity"}]}

Example input:
Sentence: Hospital - wide , patients receiving PC services before death increased from approximately 50 % to nearly 100 % .

Example answer:
{"entities": [{"text": "PC", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "death", "type": "Finding"}]}

Example input:
Sentence: Total QoLS patient encounters increased from 58 ( 2007 ) to 1 , 297 ( 2014 ) , new consults increased from 17 ( 2007 ) to 115 ( 2014 ) , and mean encounters per patient increased from 5 . 06 ( 2007 ) to 16 . 11 ( 2014 ) .

Example answer:
{"entities": [{"text": "QoLS", "type": "HealthCareActivity"}, {"text": "encounters", "type": "HealthCareActivity"}, {"text": "consults", "type": "HealthCareActivity"}]}

Input:
Sentence: Since its inception , the QoLS experienced a dramatic increase in referrals and encounters per patient , increased use by all clinical services , a trend toward earlier consultation and longer term follow - up , increasing outpatient location of death , and near - universal PC involvement at the end - of - life .

## Item MedMentions:test:651
Example input:
Sentence: Mutation analysis was performed in 437 tissue samples from 204 patients , mainly with papillary thyroid carcinomas ( PTC ) ( n = 180 ) , including 196 LNM and 56 distant metastases .

Example answer:
{"entities": [{"text": "Mutation analysis", "type": "HealthCareActivity"}, {"text": "tissue samples", "type": "AnatomicalStructure"}, {"text": "papillary thyroid carcinomas", "type": "BiologicFunction"}, {"text": "PTC", "type": "BiologicFunction"}, {"text": "LNM", "type": "BiologicFunction"}, {"text": "distant metastases", "type": "IntellectualProduct"}]}

Example input:
Sentence: The diagnosis and discrimination of these lesions are very important because of the risk for concurrent or later development of malignancy .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "lesions", "type": "Finding"}, {"text": "malignancy", "type": "BiologicFunction"}]}

Example input:
Sentence: With regard to the malignant disorders ( including liver , gastric , colon , pancreatic and oesophageal cancer ) , no such large - scale changes were observed in the last 50 years .

Example answer:
{"entities": [{"text": "malignant disorders", "type": "BiologicFunction"}, {"text": "liver", "type": "BiologicFunction"}, {"text": "gastric", "type": "BiologicFunction"}, {"text": "colon", "type": "BiologicFunction"}, {"text": "pancreatic", "type": "BiologicFunction"}, {"text": "oesophageal cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Our detailed single - cancer analysis of noncoding alterations identifies regulatory mutations as candidates for diagnostic and prognostic markers , and suggests new mechanisms for tumor evolution .

Example answer:
{"entities": [{"text": "single - cancer analysis", "type": "HealthCareActivity"}, {"text": "noncoding alterations", "type": "BiologicFunction"}, {"text": "regulatory mutations", "type": "BiologicFunction"}, {"text": "diagnostic", "type": "ClinicalAttribute"}, {"text": "tumor evolution", "type": "BiologicFunction"}]}

Example input:
Sentence: There was a significant concordance between the primary tumor genotype and the corresponding LNM for all the genes , in particular BRAF -mutated PTC .

Example answer:
{"entities": [{"text": "primary tumor", "type": "BiologicFunction"}, {"text": "LNM", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "BRAF", "type": "AnatomicalStructure"}, {"text": "PTC", "type": "BiologicFunction"}]}

Example input:
Sentence: In 1978 , Compagno and Oertel were the first to recognize the crucial distinction between the serous and the mucinous cystic neoplasms of the pancreas by explaining the importance of identifying the mucinous neoplasms because of their overt or latent malignant potential ( 4 , 5 ) .

Example answer:
{"entities": [{"text": "serous and the mucinous cystic neoplasms", "type": "BiologicFunction"}, {"text": "pancreas", "type": "AnatomicalStructure"}, {"text": "identifying", "type": "BiologicFunction"}, {"text": "mucinous neoplasms", "type": "BiologicFunction"}]}

Example input:
Sentence: Among all included patients ( n = 443 ) , advanced neoplasia was found in 13 of 310 patients ( 4 . 2 % ) of the 1 - to 5 - mm group versus 13 of 133 patients ( 9 . 8 % ) of the 6 - to 9 - mm group ( hazard ratio [ HR ] , 3 . 49 ; 95 % confidence interval [ CI ] , 1 . 6 - 7 . 6 ) .

Example answer:
{"entities": [{"text": "neoplasia", "type": "BiologicFunction"}, {"text": "found", "type": "Finding"}]}

Example input:
Sentence: The presence of multiple cancers in a patient with a predisposing mutation provides an opportunity to profile synchronous cancers in the same genetic background .

Example answer:
{"entities": [{"text": "multiple cancers", "type": "BiologicFunction"}, {"text": "mutation", "type": "BiologicFunction"}, {"text": "synchronous cancers", "type": "BiologicFunction"}]}

Example input:
Sentence: Of six testicular tumors studied , one , a Leydig tumor , was discovered to carry a detectable degree of heteroplasmy for two separate point mutations : a C → T mutation at bp 64 and a T → C mutation found at bp 152 .

Example answer:
{"entities": [{"text": "testicular tumors", "type": "BiologicFunction"}, {"text": "Leydig tumor", "type": "BiologicFunction"}, {"text": "detectable", "type": "ClinicalAttribute"}, {"text": "point mutations", "type": "BiologicFunction"}, {"text": "C → T mutation", "type": "BiologicFunction"}, {"text": "T → C mutation", "type": "BiologicFunction"}]}

Example input:
Sentence: The same mutations had been found in blood and ovary malignant tumours .

Example answer:
{"entities": [{"text": "mutations", "type": "BiologicFunction"}, {"text": "blood", "type": "BodySubstance"}, {"text": "ovary", "type": "AnatomicalStructure"}, {"text": "malignant tumours", "type": "BiologicFunction"}]}

Input:
Sentence: Mutations in the tumors were compared in order to determine the relationship between neoplasms .

## Item MedMentions:test:804
Example input:
Sentence: Spatial change in the strength and sign of relationships was investigated using geographically weighted regression and significant DPD clusters were identified using the Local Moran 's I .

Example answer:
{"entities": [{"text": "Spatial change", "type": "SpatialConcept"}, {"text": "DPD", "type": "BiologicFunction"}]}

Example input:
Sentence: 31 ± 0 . 22 ; P < .001 ) , and this increase was correlated with the decrease in strain .

Example answer:
{"entities": [{"text": "strain", "type": "HealthCareActivity"}]}

Example input:
Sentence: We found 5 km marked the threshold distance beyond which follow - up attendance significantly dropped .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: 05 for all ) included unmet social support ( β = 0 . 38 ) , and provider trust ( β = 0 . 12 ) , followed by stage at diagnosis ( β = 0 . 10 ) and perceived neighborhood social disorder ( β = 0 .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "neighborhood", "type": "SpatialConcept"}]}

Example input:
Sentence: 32 ± 4 . 11 ( t18 = 1 . 34 , p = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 1 , p < 0 . 01 ) , ' going for the ball only ' ( τ - b = 0 . 27 , moderate , z = 4 . 6 , p < 0 . 001 ) and ' staying on feet ' ( τ - b = 0 . 23 , moderate , z = 3 . 6 , p < 0 .

Example answer:
{"entities": []}

Example input:
Sentence: Distribution by age , sex and residence was found similar ( p > 0 . 05 ) in positive and negative cases .

Example answer:
{"entities": [{"text": "residence", "type": "SpatialConcept"}, {"text": "positive", "type": "Finding"}, {"text": "negative cases", "type": "Finding"}]}

Example input:
Sentence: 01 ; child externalizing problem behaviors , β = - 0 . 43 , p < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Stratified results demonstrated that among those utilizing fixed facilities , greater distance was associated with higher odds of follow - up non - attendance ( OR 5 . 01 - 10 km vs .

Example answer:
{"entities": [{"text": "facilities", "type": "Organization"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: 117±0 . 048 , P < 0 . 001 ) , SAT ( β = - 0 .

Example answer:
{"entities": [{"text": "SAT", "type": "AnatomicalStructure"}]}

Input:
Sentence: This relation was particularly strong for being placed away from home ( β = - 0 . 16 ; P < 0 . 000 ) .

## Item MedMentions:test:850
Example input:
Sentence: 01 , and 14 .

Example answer:
{"entities": []}

Example input:
Sentence: 026 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 02 ( SE = - 0 . 02 ) ; P = 0 . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 012 )

Example answer:
{"entities": []}

Example input:
Sentence: 012 and 0 . 041 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 02 ] .

Example answer:
{"entities": []}

Example input:
Sentence: 012 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 02 , 131 . 19 and 120 .

Example answer:
{"entities": []}

Example input:
Sentence: 02 - 2 . 88 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 02 vs .

Example answer:
{"entities": []}

Input:
Sentence: 02 ) .

## Item MedMentions:test:304
Example input:
Sentence: We evaluated the frequency of APC gene promoter 1A methylation between tumor tissues and autologous controls in NSCLC patients by meta - analysis .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "APC gene", "type": "AnatomicalStructure"}, {"text": "promoter 1A", "type": "AnatomicalStructure"}, {"text": "tumor tissues", "type": "AnatomicalStructure"}, {"text": "autologous controls", "type": "HealthCareActivity"}, {"text": "NSCLC", "type": "BiologicFunction"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Methylation Analysis of BRCA1 and APC in Breast Cancer and It 's Relationship to Clinicopathological Features Promoter methylation of tumor suppressor genes is an important epigenetic alteration that occurs in the primary stages of human tumors , including breast cancer .

Example answer:
{"entities": [{"text": "Methylation Analysis", "type": "ResearchActivity"}, {"text": "BRCA1", "type": "AnatomicalStructure"}, {"text": "APC", "type": "AnatomicalStructure"}, {"text": "Breast Cancer", "type": "BiologicFunction"}, {"text": "Promoter methylation", "type": "BiologicFunction"}, {"text": "tumor suppressor genes", "type": "AnatomicalStructure"}, {"text": "epigenetic alteration", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Analysed region for three genes , BCR , IL17RA and RBM38 showed an absolute mean DNA methylation of 25 .

Example answer:
{"entities": [{"text": "Analysed", "type": "ResearchActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "BCR", "type": "AnatomicalStructure"}, {"text": "IL17RA", "type": "AnatomicalStructure"}, {"text": "RBM38", "type": "AnatomicalStructure"}, {"text": "DNA methylation", "type": "BiologicFunction"}]}

Example input:
Sentence: The prevalence of methylation in the promoter region of this gene in tumor tissues and autologous controls has not been consistent in previous studies .

Example answer:
{"entities": [{"text": "promoter region", "type": "Chemical"}, {"text": "gene", "type": "AnatomicalStructure"}, {"text": "tumor tissues", "type": "AnatomicalStructure"}, {"text": "autologous controls", "type": "HealthCareActivity"}]}

Example input:
Sentence: The APC gene promoter 1A methylation rate in cancer tissues was much higher than in autologous controls , with a pooled OR of 3 .

Example answer:
{"entities": [{"text": "APC gene", "type": "AnatomicalStructure"}, {"text": "promoter 1A", "type": "AnatomicalStructure"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "autologous controls", "type": "HealthCareActivity"}]}

Example input:
Sentence: The expression of the FZD9 gene was absent in various leukemic cell lines , while it was restored following treatment with DNA demethylating agent 5 - aza - 2 ' - deoxycytidine .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "FZD9 gene", "type": "AnatomicalStructure"}, {"text": "leukemic", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "DNA demethylating agent", "type": "Chemical"}, {"text": "5 - aza - 2 ' - deoxycytidine", "type": "Chemical"}]}

Example input:
Sentence: APC promoter methylation was detected in 30 . 67 % breast cancer tissues and BRCA1 was methylated in 9 .

Example answer:
{"entities": [{"text": "APC", "type": "AnatomicalStructure"}, {"text": "promoter methylation", "type": "BiologicFunction"}, {"text": "detected", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "BRCA1", "type": "AnatomicalStructure"}, {"text": "methylated", "type": "BiologicFunction"}]}

Example input:
Sentence: Bisulfite sequencing analysis of the FZD9 promoter region showed that it was partially methylated in cell lines in which FZD9 gene was not expressed .

Example answer:
{"entities": [{"text": "Bisulfite sequencing analysis", "type": "ResearchActivity"}, {"text": "FZD9", "type": "AnatomicalStructure"}, {"text": "promoter region", "type": "Chemical"}, {"text": "methylated", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "FZD9 gene", "type": "AnatomicalStructure"}, {"text": "expressed", "type": "BiologicFunction"}]}

Example input:
Sentence: The present study examined the involvement of FZD9 promoter methylation in the downregulation of FZD9 expression in leukemia cells .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "examined", "type": "Finding"}, {"text": "FZD9", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "methylation", "type": "BiologicFunction"}, {"text": "downregulation", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "leukemia", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In conclusion , the present study indicated that the methylation profile of the FZD9 gene corresponded to that of a candidate tumor - suppressor gene in acute myeloid leukemia .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "methylation", "type": "BiologicFunction"}, {"text": "profile", "type": "HealthCareActivity"}, {"text": "FZD9 gene", "type": "AnatomicalStructure"}, {"text": "tumor - suppressor gene", "type": "AnatomicalStructure"}, {"text": "acute myeloid leukemia", "type": "BiologicFunction"}]}

Input:
Sentence: Methylation -specific polymerase chain reaction analysis revealed that the promoter region of the FZD9 gene was frequently methylated in primary or relapse acute myeloid leukemia ( 52 . 9 % ; excluding acute promyelocytic leukemia ) ; however , methylation was infrequent in B - cell acute lymphocytic leukemia ( 5 . 6 % ) .

## Item MedMentions:test:756
Example input:
Sentence: A potent inhibitor , JQ1 , which effectively disrupts the interaction of BET proteins with acetylated histones , preferentially suppresses transcription of the MYC gene .

Example answer:
{"entities": [{"text": "potent inhibitor", "type": "Chemical"}, {"text": "JQ1", "type": "Chemical"}, {"text": "BET proteins", "type": "Chemical"}, {"text": "acetylated histones", "type": "BiologicFunction"}, {"text": "transcription", "type": "BiologicFunction"}, {"text": "MYC gene", "type": "AnatomicalStructure"}]}

Example input:
Sentence: ChIP assay showed that there was a decreasing trend for histone acetylation at the StAR promoter in fetal adrenal glands , whereas H3 acetyl - K14 at the YY1 promoter presented an increasing trend following nicotine exposure .

Example answer:
{"entities": [{"text": "ChIP", "type": "HealthCareActivity"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "decreasing", "type": "Finding"}, {"text": "histone acetylation", "type": "BiologicFunction"}, {"text": "StAR promoter", "type": "AnatomicalStructure"}, {"text": "fetal adrenal glands", "type": "AnatomicalStructure"}, {"text": "H3 acetyl - K14", "type": "BiologicFunction"}, {"text": "YY1 promoter", "type": "AnatomicalStructure"}, {"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: To address this problem , we used genome - editing strategies to investigate C9orf72 interactions , subcellular localization , and knockout ( KO ) phenotypes .

Example answer:
{"entities": [{"text": "problem", "type": "Finding"}, {"text": "genome - editing", "type": "ResearchActivity"}, {"text": "C9orf72", "type": "Chemical"}, {"text": "interactions", "type": "BiologicFunction"}, {"text": "subcellular localization", "type": "AnatomicalStructure"}, {"text": "knockout", "type": "BiologicFunction"}, {"text": "KO", "type": "BiologicFunction"}]}

Example input:
Sentence: Chromatin immunoprecipitation ( ChIP ) showed that MS188 directly bound to the promoter of CYP703A2 and luciferase - inducible assay showed that MS188 activated the expression of CYP703A2 .

Example answer:
{"entities": [{"text": "Chromatin immunoprecipitation", "type": "HealthCareActivity"}, {"text": "ChIP", "type": "HealthCareActivity"}, {"text": "MS188", "type": "Chemical"}, {"text": "promoter", "type": "Chemical"}, {"text": "CYP703A2", "type": "AnatomicalStructure"}, {"text": "luciferase - inducible", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "CYP703A2", "type": "Chemical"}]}

Example input:
Sentence: Chromatin immunoprecipitation ( ChIP ) showed approximately 3 - fold enrichment of RANKL - specific DNA in anti - SOX5 immunoprecipitate in IL - 6 treated MH7A cells as compared to untreated cells .

Example answer:
{"entities": [{"text": "Chromatin immunoprecipitation", "type": "HealthCareActivity"}, {"text": "ChIP", "type": "HealthCareActivity"}, {"text": "RANKL - specific DNA", "type": "Chemical"}, {"text": "anti - SOX5 immunoprecipitate", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "MH7A cells", "type": "AnatomicalStructure"}, {"text": "untreated cells", "type": "Finding"}]}

Example input:
Sentence: Finally , we apply co - ChIP to measure the distribution of the bivalent H3K4me3 - H3K27me3 domains in two distinct mouse embryonic stem cell ( mESC ) states and in four adult tissues .

Example answer:
{"entities": [{"text": "co - ChIP", "type": "HealthCareActivity"}, {"text": "H3K4me3", "type": "AnatomicalStructure"}, {"text": "H3K27me3", "type": "AnatomicalStructure"}, {"text": "domains", "type": "SpatialConcept"}, {"text": "mouse embryonic stem cell", "type": "AnatomicalStructure"}, {"text": "mESC", "type": "AnatomicalStructure"}, {"text": "adult tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Histone modifications and the interactions between the YY1 and StAR promoter were assessed using chromatin immunoprecipitation ( ChIP ) .

Example answer:
{"entities": [{"text": "Histone modifications", "type": "BiologicFunction"}, {"text": "YY1", "type": "Chemical"}, {"text": "StAR promoter", "type": "AnatomicalStructure"}, {"text": "chromatin immunoprecipitation", "type": "HealthCareActivity"}, {"text": "ChIP", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using co - ChIP , we study the genome - wide co - occurrence of 14 chromatin marks ( 70 pairwise combinations ) , and find previously undescribed co - occurrence patterns , including the co - occurrence of H3K9me1 and H3K27ac in super - enhancers .

Example answer:
{"entities": [{"text": "co - ChIP", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "genome - wide", "type": "AnatomicalStructure"}, {"text": "chromatin marks", "type": "SpatialConcept"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "H3K9me1", "type": "AnatomicalStructure"}, {"text": "H3K27ac", "type": "AnatomicalStructure"}, {"text": "super - enhancers", "type": "SpatialConcept"}]}

Example input:
Sentence: Here we present a genome - wide quantitative method for combinatorial indexed chromatin immunoprecipitation ( co - ChIP ) to characterize co - occurrence of histone modifications on nucleosomes .

Example answer:
{"entities": [{"text": "combinatorial indexed", "type": "IntellectualProduct"}, {"text": "chromatin immunoprecipitation", "type": "HealthCareActivity"}, {"text": "co - ChIP", "type": "HealthCareActivity"}, {"text": "histone modifications", "type": "BiologicFunction"}, {"text": "nucleosomes", "type": "Chemical"}]}

Example input:
Sentence: Co - ChIP enables genome - wide mapping of histone mark co - occurrence at single - molecule resolution Histone modifications play an important role in chromatin organization and transcriptional regulation , but despite the large amount of genome - wide histone modification data collected in different cells and tissues , little is known about co - occurrence of modifications on the same nucleosome .

Example answer:
{"entities": [{"text": "Co - ChIP", "type": "HealthCareActivity"}, {"text": "genome - wide mapping", "type": "ResearchActivity"}, {"text": "histone mark", "type": "SpatialConcept"}, {"text": "Histone modifications", "type": "BiologicFunction"}, {"text": "chromatin organization", "type": "BiologicFunction"}, {"text": "transcriptional regulation", "type": "BiologicFunction"}, {"text": "genome - wide", "type": "AnatomicalStructure"}, {"text": "histone modification", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "modifications", "type": "BiologicFunction"}, {"text": "nucleosome", "type": "Chemical"}]}

Input:
Sentence: These results show that co - ChIP can reveal the complex interactions between histone modifications .

## Item MedMentions:test:620
Example input:
Sentence: Danish women 's experiences of the rebozo technique during labour : A qualitative explorative study The study aimed to explore women 's experiences of the rebozo technique during labour .

Example answer:
{"entities": [{"text": "Danish", "type": "SpatialConcept"}, {"text": "women 's", "type": "PopulationGroup"}, {"text": "experiences", "type": "BiologicFunction"}, {"text": "labour", "type": "BiologicFunction"}, {"text": "qualitative explorative study", "type": "ResearchActivity"}]}

Example input:
Sentence: Improving access to and utilisation of appropriate and responsive healthcare may help to address disparities in stillbirth risk for Indigenous women .

Example answer:
{"entities": [{"text": "healthcare", "type": "HealthCareActivity"}, {"text": "stillbirth", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: An educational programme for health care professionals working in maternal and child health has been designed to address these needs according to the Perinatal Society of Australia and New Zealand Guideline for Perinatal Mortality : IMproving Perinatal mortality Review and Outcomes Via Education ( IMPROVE ) .

Example answer:
{"entities": [{"text": "health care professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "maternal", "type": "Finding"}, {"text": "child health", "type": "HealthCareActivity"}, {"text": "Perinatal Society of Australia and New Zealand Guideline for Perinatal Mortality", "type": "IntellectualProduct"}]}

Example input:
Sentence: Evaluation of an international educational programme for health care professionals on best practice in the management of a perinatal death : IMproving Perinatal mortality Review and Outcomes Via Education ( IMPROVE ) Stillbirths and neonatal deaths are devastating events for both parents and clinicians and are global public health concerns .

Example answer:
{"entities": [{"text": "Evaluation", "type": "IntellectualProduct"}, {"text": "health care professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "death", "type": "BiologicFunction"}, {"text": "Stillbirths", "type": "Finding"}, {"text": "neonatal deaths", "type": "Finding"}, {"text": "global public health", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Emergency departments , birthday parties , fraternities and the workplace serve as settings for interventions ; these are increasingly delivered via digital and mobile technology .

Example answer:
{"entities": [{"text": "Emergency departments", "type": "HealthCareActivity"}, {"text": "fraternities", "type": "Organization"}, {"text": "workplace", "type": "SpatialConcept"}, {"text": "interventions", "type": "HealthCareActivity"}]}

Example input:
Sentence: Development process of an assessment tool for disruptive behavior problems in cross - cultural settings : the Disruptive Behavior International Scale - Nepal version ( DBIS - N ) Systematic processes are needed to develop valid measurement instruments for disruptive behavior disorders ( DBDs ) in cross - cultural settings .

Example answer:
{"entities": [{"text": "assessment", "type": "HealthCareActivity"}, {"text": "disruptive behavior problems", "type": "BiologicFunction"}, {"text": "cross - cultural settings", "type": "ResearchActivity"}, {"text": "Disruptive Behavior International Scale", "type": "IntellectualProduct"}, {"text": "Nepal", "type": "SpatialConcept"}, {"text": "version", "type": "IntellectualProduct"}, {"text": "DBIS - N", "type": "IntellectualProduct"}, {"text": "disruptive behavior disorders", "type": "BiologicFunction"}, {"text": "DBDs", "type": "BiologicFunction"}]}

Example input:
Sentence: In an accompanying article , we describe the process of selecting , implementing , and evaluating a package of interventions designed to prevent and reduce disrespect and abuse in a large urban hospital in Tanzania .

Example answer:
{"entities": [{"text": "evaluating", "type": "HealthCareActivity"}, {"text": "interventions", "type": "HealthCareActivity"}, {"text": "urban hospital", "type": "Organization"}, {"text": "Tanzania", "type": "SpatialConcept"}]}

Example input:
Sentence: For these changes to translate into dignified care during childbirth for all women in a sustainable fashion , institutional commitment to providing the necessary resources and staff will be needed .

Example answer:
{"entities": [{"text": "childbirth", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "institutional", "type": "Organization"}, {"text": "staff", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Based on our experience and findings , we conclude that a visible , sustained , and participatory intervention process ; committed facility leadership ; management support ; and staff engagement throughout the project contributed to a marked change in the culture of the hospital to one that values and promotes respectful maternity care .

Example answer:
{"entities": [{"text": "participatory intervention process", "type": "HealthCareActivity"}, {"text": "facility", "type": "Organization"}, {"text": "hospital", "type": "Organization"}, {"text": "maternity care", "type": "HealthCareActivity"}]}

Example input:
Sentence: Several recent studies have sought to quantify the prevalence of D & A , however little evidence exists about effective interventions to mitigate disrespect and abuse , and promote respectful maternity care .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "interventions", "type": "HealthCareActivity"}, {"text": "maternity care", "type": "HealthCareActivity"}]}

Input:
Sentence: Applying a participatory approach to the promotion of a culture of respect during childbirth Disrespect and abuse ( D & A ) during facility - based childbirth is a topic of growing concern and attention globally .

## Item MedMentions:test:567
Example input:
Sentence: Patients with PE were retrospectively analyzed and divided into 2 groups based on computed tomography : a group with pleural effusion due to PE ( effusion group ) and a group without pleural effusion ( control group ) .

Example answer:
{"entities": [{"text": "PE", "type": "BiologicFunction"}, {"text": "retrospectively analyzed", "type": "ResearchActivity"}, {"text": "computed tomography", "type": "HealthCareActivity"}, {"text": "pleural effusion", "type": "BiologicFunction"}]}

Example input:
Sentence: Evaluation of Choroidal Thickness in Patients with Pseudoexfoliation Syndrome and Pseudoexfoliation Glaucoma Purpose .

Example answer:
{"entities": [{"text": "Evaluation", "type": "HealthCareActivity"}, {"text": "Choroidal", "type": "AnatomicalStructure"}, {"text": "Pseudoexfoliation Syndrome", "type": "BiologicFunction"}, {"text": "Pseudoexfoliation Glaucoma", "type": "BiologicFunction"}]}

Example input:
Sentence: In treated eyes , PEFL was significantly higher in ESVs than in the IW ( P < 0 . 01 ) and was associated with increased cross - sectional area of ESVs ( P < 0 .

Example answer:
{"entities": [{"text": "eyes", "type": "AnatomicalStructure"}, {"text": "ESVs", "type": "AnatomicalStructure"}, {"text": "cross - sectional area", "type": "SpatialConcept"}]}

Example input:
Sentence: Macular thickness as detected by TD - OCT had high discriminating power between controls , glaucoma suspects and glaucoma patients comparable with peripapillary RNFL thickness parameters .

Example answer:
{"entities": [{"text": "Macular", "type": "AnatomicalStructure"}, {"text": "TD - OCT", "type": "HealthCareActivity"}, {"text": "glaucoma suspects", "type": "BiologicFunction"}, {"text": "glaucoma", "type": "BiologicFunction"}, {"text": "peripapillary", "type": "SpatialConcept"}, {"text": "RNFL", "type": "AnatomicalStructure"}, {"text": "parameters", "type": "Finding"}]}

Example input:
Sentence: Macular Ganglion Cell - Inner Plexiform Layer Thickness Is Associated with Clinical Progression in Mild Cognitive Impairment and Alzheimers Disease We investigated the association of the macular ganglion cell - inner plexiform layer ( GCIPL ) and peripapillary retinal nerve fiber layer ( RNFL ) thicknesses with disease progression in mild cognitive impairment ( MCI ) and Alzheimer 's disease ( AD ) .

Example answer:
{"entities": [{"text": "Ganglion Cell", "type": "AnatomicalStructure"}, {"text": "Inner Plexiform Layer", "type": "AnatomicalStructure"}, {"text": "Clinical Progression", "type": "BiologicFunction"}, {"text": "Mild Cognitive Impairment", "type": "BiologicFunction"}, {"text": "Alzheimers Disease", "type": "BiologicFunction"}, {"text": "ganglion cell", "type": "AnatomicalStructure"}, {"text": "inner plexiform layer", "type": "AnatomicalStructure"}, {"text": "GCIPL", "type": "AnatomicalStructure"}, {"text": "peripapillary retinal nerve fiber layer", "type": "AnatomicalStructure"}, {"text": "RNFL", "type": "AnatomicalStructure"}, {"text": "disease progression", "type": "BiologicFunction"}, {"text": "mild cognitive impairment", "type": "BiologicFunction"}, {"text": "MCI", "type": "BiologicFunction"}, {"text": "Alzheimer 's disease", "type": "BiologicFunction"}, {"text": "AD", "type": "BiologicFunction"}]}

Example input:
Sentence: Choroidal thicknesses in the macular and peripapillary areas were measured by using spectral domain optical coherence tomography .

Example answer:
{"entities": [{"text": "Choroidal", "type": "AnatomicalStructure"}, {"text": "peripapillary", "type": "SpatialConcept"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "spectral domain optical coherence tomography", "type": "MedicalDevice"}]}

Example input:
Sentence: The role of choroid in the development of glaucomatous damage in patients with PEX syndrome remains unclear .

Example answer:
{"entities": [{"text": "choroid", "type": "AnatomicalStructure"}, {"text": "glaucomatous", "type": "BiologicFunction"}, {"text": "PEX syndrome", "type": "BiologicFunction"}]}

Example input:
Sentence: To compare the macular and peripapillary choroidal thickness in eyes with pseudoexfoliation ( PEX ) syndrome and PEX glaucoma with the normal eyes of healthy controls .

Example answer:
{"entities": [{"text": "peripapillary", "type": "SpatialConcept"}, {"text": "choroidal", "type": "AnatomicalStructure"}, {"text": "eyes", "type": "AnatomicalStructure"}, {"text": "pseudoexfoliation ( PEX ) syndrome", "type": "BiologicFunction"}, {"text": "PEX glaucoma", "type": "BiologicFunction"}]}

Example input:
Sentence: The mean values of choroidal thickness in the macular and peripapillary areas ( except the superior quadrant ) in the patients with PEX syndrome and PEX glaucoma were lower compared with controls ( all p < 0 .

Example answer:
{"entities": [{"text": "choroidal", "type": "AnatomicalStructure"}, {"text": "peripapillary", "type": "SpatialConcept"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "superior", "type": "SpatialConcept"}, {"text": "quadrant", "type": "SpatialConcept"}, {"text": "PEX syndrome", "type": "BiologicFunction"}, {"text": "PEX glaucoma", "type": "BiologicFunction"}]}

Example input:
Sentence: The mean values of the macular and peripapillary choroidal thickness in the PEX glaucoma group were lower compared with PEX syndrome group ; however this difference was not significant .

Example answer:
{"entities": [{"text": "peripapillary", "type": "SpatialConcept"}, {"text": "choroidal", "type": "AnatomicalStructure"}, {"text": "PEX glaucoma", "type": "BiologicFunction"}, {"text": "PEX syndrome", "type": "BiologicFunction"}, {"text": "not significant", "type": "Finding"}]}

Input:
Sentence: The findings of this study revealed that macular and peripapillary choroidal thicknesses were decreased in PEX syndrome and PEX glaucoma cases .

## Item MedMentions:test:823
Example input:
Sentence: The purpose of our study was to examine home health data using visual analysis techniques to discover clinically salient associations between patient characteristics with problem - oriented health outcomes of older adult home health patients during the home health service period .

Example answer:
{"entities": [{"text": "home health data", "type": "IntellectualProduct"}, {"text": "visual analysis techniques", "type": "HealthCareActivity"}, {"text": "older adult home health patients", "type": "HealthCareActivity"}, {"text": "home health service", "type": "HealthCareActivity"}]}

Example input:
Sentence: What Is the Real Impact of Urinary Incontinence on Female Sexual Dysfunction ? A Case Control Study Urinary incontinence ( UI ) has been associated with negative effects on women 's sexuality . Women 's sexuality and sexual function are a complex issue , and the role of UI is not completely clear .

Example answer:
{"entities": [{"text": "Urinary Incontinence", "type": "BiologicFunction"}, {"text": "Female Sexual Dysfunction", "type": "BiologicFunction"}, {"text": "Case Control Study", "type": "ResearchActivity"}, {"text": "Urinary incontinence", "type": "BiologicFunction"}, {"text": "UI", "type": "BiologicFunction"}, {"text": "negative", "type": "Finding"}, {"text": "women 's", "type": "PopulationGroup"}, {"text": "Women 's", "type": "PopulationGroup"}, {"text": "sexual function", "type": "BiologicFunction"}, {"text": "issue", "type": "Finding"}]}

Example input:
Sentence: Positive tests for NG and CT in patients evaluated for sexual victimization may represent infection from sexual contact , contiguous spread of infection , or the presence of infected assailant secretions .

Example answer:
{"entities": [{"text": "Positive", "type": "Finding"}, {"text": "tests", "type": "HealthCareActivity"}, {"text": "NG", "type": "Bacterium"}, {"text": "CT", "type": "Bacterium"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "infected assailant secretions", "type": "BodySubstance"}]}

Example input:
Sentence: Furthermore , women with UI showed less sexual desire , sexual comfort , and sexual satisfaction than their counterparts despite having a similar frequency of sexual activity .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "UI", "type": "BiologicFunction"}, {"text": "sexual comfort", "type": "BiologicFunction"}, {"text": "sexual satisfaction", "type": "BiologicFunction"}]}

Example input:
Sentence: This study aims to analyze the impact of an individual reminiscence program in a group of older persons with cognitive decline living in nursing homes on the dimensions of cognition , autobiographical memory , mood , behavior and anxiety .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "individual", "type": "PopulationGroup"}, {"text": "reminiscence program", "type": "HealthCareActivity"}, {"text": "cognitive decline", "type": "BiologicFunction"}, {"text": "nursing homes", "type": "Organization"}, {"text": "cognition", "type": "BiologicFunction"}, {"text": "autobiographical memory", "type": "BiologicFunction"}, {"text": "mood", "type": "BiologicFunction"}, {"text": "anxiety", "type": "BiologicFunction"}]}

Example input:
Sentence: In bivariate analysis , a positive test was associated with female sex , age older than 11 years , previous sexual contact , acute or healed genital injury , drug / alcohol intoxication , and examination within 72 hours of sexual contact .

Example answer:
{"entities": [{"text": "genital injury", "type": "InjuryOrPoisoning"}, {"text": "examination", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the present study , we investigated the sexual functioning of BC patients and its association with women 's personal characteristics and cancer treatments .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "sexual functioning", "type": "BiologicFunction"}, {"text": "BC", "type": "BiologicFunction"}, {"text": "association", "type": "BiologicFunction"}, {"text": "women 's", "type": "PopulationGroup"}, {"text": "cancer treatments", "type": "HealthCareActivity"}]}

Example input:
Sentence: Expressing sexuality in nursing homes .

Example answer:
{"entities": [{"text": "nursing homes", "type": "Organization"}]}

Example input:
Sentence: Female residents reported key elements influencing how they manage their sexuality in Nursing Homes .

Example answer:
{"entities": [{"text": "residents", "type": "PopulationGroup"}, {"text": "Nursing Homes", "type": "Organization"}]}

Example input:
Sentence: The experience of older women : A qualitative study In nursing homes , a number of barriers to the expression of sexuality exist , such as the lack of privacy , certain attitudes on behalf of the staff and the family , the lack of a sexual partner , and physical limitations .

Example answer:
{"entities": [{"text": "older women", "type": "PopulationGroup"}, {"text": "qualitative study", "type": "ResearchActivity"}, {"text": "nursing homes", "type": "Organization"}, {"text": "lack of privacy", "type": "Finding"}, {"text": "attitudes", "type": "BiologicFunction"}, {"text": "staff", "type": "ProfessionalOrOccupationalGroup"}, {"text": "sexual partner", "type": "PopulationGroup"}, {"text": "physical limitations", "type": "Finding"}]}

Input:
Sentence: These results serve to improve our understanding regarding the expression of sexuality in older female nursing home residents .

## Item MedMentions:test:562
Example input:
Sentence: Recent advances in endovascular technologies have expanded the use of coil embolization for small aneurysm treatment .

Example answer:
{"entities": [{"text": "endovascular technologies", "type": "HealthCareActivity"}, {"text": "coil embolization", "type": "HealthCareActivity"}, {"text": "aneurysm", "type": "BiologicFunction"}]}

Example input:
Sentence: Predilation technique with balloon angioplasty to facilitate percutaneous groin access of large size sheath through scar tissue Purpose Percutaneous remote access for endovascular aortic repair is an advantageous alternative to open access .

Example answer:
{"entities": [{"text": "Predilation technique", "type": "HealthCareActivity"}, {"text": "balloon angioplasty", "type": "HealthCareActivity"}, {"text": "percutaneous groin", "type": "SpatialConcept"}, {"text": "access", "type": "SpatialConcept"}, {"text": "large size", "type": "Finding"}, {"text": "sheath", "type": "MedicalDevice"}, {"text": "scar tissue", "type": "Finding"}, {"text": "Percutaneous remote access", "type": "SpatialConcept"}, {"text": "endovascular aortic repair", "type": "HealthCareActivity"}]}

Example input:
Sentence: Reintervention after endovascular repair for aortic dissection : A systematic review and meta - analysis Thoracic endovascular aortic repair has been chosen as a less - invasive alternative to open surgery for the treatment of aortic dissections ; however , the advantages have been challenged by the postoperative reintervention during the follow - up period .

Example answer:
{"entities": [{"text": "Reintervention", "type": "HealthCareActivity"}, {"text": "aortic dissection", "type": "BiologicFunction"}, {"text": "systematic review", "type": "IntellectualProduct"}, {"text": "meta - analysis", "type": "ResearchActivity"}, {"text": "open surgery", "type": "HealthCareActivity"}, {"text": "aortic dissections", "type": "BiologicFunction"}, {"text": "reintervention", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of this study was to evaluate an original technique used for enabling percutaneous remote access for thoracic or abdominal endovascular aortic repair in patients with scar tissue and / or a vascular graft in the groin .

Example answer:
{"entities": [{"text": "percutaneous remote access", "type": "SpatialConcept"}, {"text": "thoracic", "type": "HealthCareActivity"}, {"text": "abdominal endovascular aortic repair", "type": "HealthCareActivity"}, {"text": "scar tissue", "type": "Finding"}, {"text": "groin", "type": "SpatialConcept"}]}

Example input:
Sentence: In the last decades , in addition to surgery , self - expanding metallic stents ( SEMSs ) are available both as a bridge to surgery ( BTS ) or palliation .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "self - expanding metallic stents", "type": "MedicalDevice"}, {"text": "( SEMSs )", "type": "MedicalDevice"}, {"text": "palliation", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Conclusions Percutaneous access in redo groins with scar tissue and / or synthetic vascular graft using ultrasound - guided punction , preclosing with ProGlide ® system and predilation with percutaneous transluminal angioplasty balloon to introduce large size sheath as used for endovascular aortic repair showed to be feasible , safe and with few local complications .

Example answer:
{"entities": [{"text": "Percutaneous access", "type": "SpatialConcept"}, {"text": "redo groins", "type": "SpatialConcept"}, {"text": "scar tissue", "type": "Finding"}, {"text": "ultrasound - guided punction", "type": "MedicalDevice"}, {"text": "preclosing", "type": "HealthCareActivity"}, {"text": "ProGlide ® system", "type": "MedicalDevice"}, {"text": "predilation", "type": "HealthCareActivity"}, {"text": "percutaneous transluminal angioplasty balloon", "type": "HealthCareActivity"}, {"text": "large size", "type": "Finding"}, {"text": "sheath", "type": "MedicalDevice"}, {"text": "endovascular aortic repair", "type": "HealthCareActivity"}, {"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: The combined use at different surgical times of the self - expandable stent and flow - diverter device was technically successful in both patients .

Example answer:
{"entities": [{"text": "self - expandable stent", "type": "MedicalDevice"}, {"text": "flow - diverter device", "type": "MedicalDevice"}]}

Example input:
Sentence: Two - stage reconstructive overlapping stent LEO + and SILK for treatment of intracranial circumferential fusiform aneurysms in the posterior circulation Intracranial circumferential fusiform aneurysms of the posterior circulation involving arterial branches or perforating vessels are difficult to treat .

Example answer:
{"entities": [{"text": "reconstructive", "type": "HealthCareActivity"}, {"text": "overlapping stent", "type": "MedicalDevice"}, {"text": "LEO +", "type": "MedicalDevice"}, {"text": "SILK", "type": "MedicalDevice"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "intracranial", "type": "SpatialConcept"}, {"text": "circumferential", "type": "SpatialConcept"}, {"text": "fusiform aneurysms", "type": "AnatomicalStructure"}, {"text": "circulation", "type": "BiologicFunction"}, {"text": "Intracranial", "type": "SpatialConcept"}, {"text": "arterial branches", "type": "AnatomicalStructure"}, {"text": "perforating", "type": "Finding"}, {"text": "vessels", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Circumferential fusiform aneurysm of the posterior circulation involving arterial branches or perforating vessels to the brain stem may be treated with this arterial reconstruction technique at different surgical times , using the self - expandable stent called LEO + and the flow - diverter device SILK , minimizing the risk of complications and failure of the endovascular technique , with the potential for arterial reconstruction with thrombosis of the aneurysmatic sac , as well as flow maintenance in the eloquent arteries , in this type of cerebral aneurysm .

Example answer:
{"entities": [{"text": "Circumferential", "type": "SpatialConcept"}, {"text": "fusiform aneurysm", "type": "AnatomicalStructure"}, {"text": "circulation", "type": "BiologicFunction"}, {"text": "arterial branches", "type": "AnatomicalStructure"}, {"text": "perforating", "type": "Finding"}, {"text": "vessels", "type": "AnatomicalStructure"}, {"text": "brain stem", "type": "AnatomicalStructure"}, {"text": "arterial", "type": "AnatomicalStructure"}, {"text": "reconstruction technique", "type": "HealthCareActivity"}, {"text": "self - expandable stent", "type": "MedicalDevice"}, {"text": "LEO +", "type": "MedicalDevice"}, {"text": "flow - diverter device", "type": "MedicalDevice"}, {"text": "SILK", "type": "MedicalDevice"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "technique", "type": "HealthCareActivity"}, {"text": "arterial reconstruction", "type": "HealthCareActivity"}, {"text": "thrombosis", "type": "BiologicFunction"}, {"text": "aneurysmatic sac", "type": "BiologicFunction"}, {"text": "eloquent arteries", "type": "AnatomicalStructure"}, {"text": "cerebral aneurysm", "type": "BiologicFunction"}]}

Example input:
Sentence: Endovascular treatment was performed by means of a vascular reconstruction technique that used at different surgical times : overlapping ; a telescoped self - expandable stent , LEO + ; and a flow - diverter device , SILK .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "vascular", "type": "AnatomicalStructure"}, {"text": "reconstruction technique", "type": "HealthCareActivity"}, {"text": "overlapping ; a telescoped self - expandable stent", "type": "HealthCareActivity"}, {"text": "LEO +", "type": "MedicalDevice"}, {"text": "flow - diverter device", "type": "MedicalDevice"}, {"text": "SILK", "type": "MedicalDevice"}]}

Input:
Sentence: This article shows an endovascular reconstruction technique not yet described , using a telescoping self - expandable stent ( LEO + ) and flow - diverter device ( SILK ) at different surgical times .
