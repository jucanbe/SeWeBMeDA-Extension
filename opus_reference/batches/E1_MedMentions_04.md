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

## Item MedMentions:test:1055
Example input:
Sentence: 3 % , 10 . 8 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 1 % ) were positive for dermatophyte growth whose pH varied from 7 .

Example answer:
{"entities": [{"text": "dermatophyte", "type": "Eukaryote"}, {"text": "growth", "type": "BiologicFunction"}]}

Example input:
Sentence: 3 % versus 7 . 0 % ( P < 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 5 , which was significantly higher than that in those with pH < 5 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % ; p = 0 . 014 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 04min ( - 1 ) at pH 10 but the mineralization achieved was around 10 % .

Example answer:
{"entities": []}

Example input:
Sentence: 02 % was found in 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 % , p = 0 . 018 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 6 . 3 % , p = 0 . 002 ) were more often observed in the low PA group .

Example answer:
{"entities": []}

Example input:
Sentence: 4 % ) was obtained at pH 7 .

Example answer:
{"entities": []}

Input:
Sentence: 1 % ) was observed at pH 3 .

## Item MedMentions:test:611
Example input:
Sentence: The Promoting Active Aging ( PRACTA ) study consisted of a baseline questionnaire , implementation of an intervention , and a follow - up questionnaire that was administered 1 month after the intervention .

Example answer:
{"entities": [{"text": "Aging", "type": "BiologicFunction"}, {"text": "PRACTA", "type": "HealthCareActivity"}, {"text": "baseline questionnaire", "type": "IntellectualProduct"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "follow - up questionnaire", "type": "IntellectualProduct"}]}

Example input:
Sentence: We assessed treatment effect using repeated measures methodology for rare diseases via the generalised estimating equation model in a modified intention - to - treat population , including all participants assigned to treatment minus those who withdrew due to a non - treatment - related cause .

Example answer:
{"entities": [{"text": "methodology", "type": "ResearchActivity"}, {"text": "rare diseases", "type": "BiologicFunction"}, {"text": "generalised estimating equation model", "type": "IntellectualProduct"}, {"text": "intention - to - treat", "type": "ResearchActivity"}, {"text": "population", "type": "PopulationGroup"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "non - treatment - related cause", "type": "Finding"}]}

Example input:
Sentence: The results encourage exploring these techniques ' capability to improve mood in randomized controlled studies and patients .

Example answer:
{"entities": [{"text": "mood", "type": "BiologicFunction"}, {"text": "controlled studies", "type": "ResearchActivity"}]}

Example input:
Sentence: Offering a monetary incentive when a reminder is required could be cost - effective depending on the sample size of the study and the resources available to administer the reminder letters .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "letters", "type": "IntellectualProduct"}]}

Example input:
Sentence: Further studies are required in a larger sample with longer follow - up durations to confirm the outcome of the present work for the benefit of patients .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: This study aimed to evaluate the effect of promising a monetary incentive at first mailout versus a promise on reminder letters only .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "letters", "type": "IntellectualProduct"}]}

Example input:
Sentence: Recent improvements in the widespread availability of individual participant data from randomised controlled trials makes it feasible to conduct extensive individual participant data meta - analyses which were previously impossible , thereby reducing the effect of publication or reporting bias on the understanding of the infant immune response .

Example answer:
{"entities": [{"text": "widespread", "type": "SpatialConcept"}, {"text": "individual", "type": "PopulationGroup"}, {"text": "participant", "type": "PopulationGroup"}, {"text": "randomised controlled trials", "type": "ResearchActivity"}, {"text": "meta - analyses", "type": "ResearchActivity"}, {"text": "impossible", "type": "Finding"}, {"text": "publication", "type": "IntellectualProduct"}, {"text": "reporting", "type": "HealthCareActivity"}, {"text": "understanding", "type": "BiologicFunction"}, {"text": "immune response", "type": "BiologicFunction"}]}

Example input:
Sentence: On the other hand , a range of meta - analyses ( each including thousands of participants ) have reported mixed results , with the most recent among them showing benefit from RIC , pinpointing at the same time a number of shortcomings in published studies , adversely affecting the quality of available data .

Example answer:
{"entities": [{"text": "meta - analyses", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "RIC", "type": "HealthCareActivity"}, {"text": "published", "type": "IntellectualProduct"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "available data", "type": "IntellectualProduct"}]}

Example input:
Sentence: The incentive was posted out on receipt of a completed questionnaire .

Example answer:
{"entities": [{"text": "questionnaire", "type": "IntellectualProduct"}]}

Example input:
Sentence: There is heterogeneity across studies and until recently , most studies had only short to medium term follow - up periods , thus limiting the evidence available on longer term benefit .

Example answer:
{"entities": [{"text": "follow - up periods", "type": "HealthCareActivity"}]}

Input:
Sentence: Evaluation of the effects of an offer of a monetary incentive on the rate of questionnaire return during follow - up of a clinical trial : a randomised study within a trial A systematic review on the use of incentives to promote questionnaire return in clinical trials suggest they are effective , but not all studies have sufficient funds to use them .

## Item MedMentions:test:767
Example input:
Sentence: Mechanical hyperalgesia was evaluated by electronic von Frey test .

Example answer:
{"entities": [{"text": "Mechanical hyperalgesia", "type": "Finding"}, {"text": "electronic von Frey test", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , spinal treatment of EphB1 - Fc in the early phase after STZ injection did not prevent the induction of DNP .

Example answer:
{"entities": [{"text": "spinal", "type": "SpatialConcept"}, {"text": "EphB1", "type": "Chemical"}, {"text": "Fc", "type": "Chemical"}, {"text": "STZ", "type": "Chemical"}, {"text": "injection", "type": "HealthCareActivity"}, {"text": "DNP", "type": "Finding"}]}

Example input:
Sentence: Diabetes induced mechanical allodynia and hyperalgesia , cold allodynia , heat hypoalgesia , and depression - like behaviour .

Example answer:
{"entities": [{"text": "Diabetes", "type": "BiologicFunction"}, {"text": "mechanical allodynia", "type": "Finding"}, {"text": "hyperalgesia", "type": "Finding"}, {"text": "cold allodynia", "type": "Finding"}, {"text": "heat hypoalgesia", "type": "Finding"}, {"text": "depression - like behaviour", "type": "BiologicFunction"}]}

Example input:
Sentence: SA - 57 dose -dependently reversed mechanical allodynia in the constriction injury ( CCI ) of the sciatic nerve model of neuropathic pain and carrageenan inflammatory pain model .

Example answer:
{"entities": [{"text": "SA - 57", "type": "Chemical"}, {"text": "mechanical allodynia", "type": "Finding"}, {"text": "constriction injury", "type": "InjuryOrPoisoning"}, {"text": "CCI", "type": "InjuryOrPoisoning"}, {"text": "sciatic nerve", "type": "AnatomicalStructure"}, {"text": "neuropathic pain", "type": "Finding"}, {"text": "carrageenan", "type": "Chemical"}, {"text": "inflammatory pain", "type": "Finding"}]}

Example input:
Sentence: Minocycline reduces mechanical allodynia and depressive - like behaviour in type - 1 diabetes mellitus in the rat A common and devastating complication of diabetes mellitus is painful diabetic neuropathy ( PDN ) that can be accompanied by emotional disorders such as depression .

Example answer:
{"entities": [{"text": "Minocycline", "type": "Chemical"}, {"text": "mechanical allodynia", "type": "Finding"}, {"text": "depressive - like behaviour", "type": "BiologicFunction"}, {"text": "type - 1 diabetes mellitus", "type": "BiologicFunction"}, {"text": "rat", "type": "Eukaryote"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "painful diabetic neuropathy", "type": "BiologicFunction"}, {"text": "PDN", "type": "BiologicFunction"}, {"text": "emotional disorders", "type": "BiologicFunction"}, {"text": "depression", "type": "BiologicFunction"}]}

Example input:
Sentence: Motor - evoked potentials ( MEPs ) were recorded from the abductor pollicis brevis and flexor digitorum superficialis muscles .

Example answer:
{"entities": [{"text": "Motor - evoked potentials", "type": "BiologicFunction"}, {"text": "MEPs", "type": "BiologicFunction"}, {"text": "abductor pollicis brevis", "type": "AnatomicalStructure"}, {"text": "flexor digitorum superficialis muscles", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Activation of ephrinB - EphB receptor signalling in rat spinal cord contributes to maintenance of diabetic neuropathic pain Diabetic neuropathic pain ( DNP ) is severe and intractable in clinic .

Example answer:
{"entities": [{"text": "rat spinal cord", "type": "AnatomicalStructure"}, {"text": "diabetic", "type": "Finding"}, {"text": "neuropathic pain", "type": "Finding"}, {"text": "Diabetic", "type": "Finding"}, {"text": "DNP", "type": "Finding"}, {"text": "clinic", "type": "Organization"}]}

Example input:
Sentence: Electromechanical delays during a fatiguing exercise and recovery in patients with myotonic dystrophy type 1 The partitioning of the electromechanical delay by an electromyographic ( EMG ) , mechanomyographic ( MMG ) and force combined approach can provide further insight into the electrochemical and mechanical processes involved with skeletal muscle contraction and relaxation .

Example answer:
{"entities": [{"text": "fatiguing", "type": "Finding"}, {"text": "recovery", "type": "BiologicFunction"}, {"text": "myotonic dystrophy type 1", "type": "BiologicFunction"}, {"text": "mechanomyographic", "type": "HealthCareActivity"}, {"text": "MMG", "type": "HealthCareActivity"}, {"text": "skeletal muscle contraction", "type": "BiologicFunction"}, {"text": "relaxation", "type": "BiologicFunction"}]}

Example input:
Sentence: The aim of the study was to monitor by this combined approach the changes in delays ' electrochemical and mechanical components throughout a fatiguing task and during recovery in patients with myotonic dystrophy type 1 ( DM1 ) , who present at the skeletal muscle level fibres rearrangement , muscle weakness and myotonia , especially in the distal muscles .

Example answer:
{"entities": [{"text": "fatiguing", "type": "Finding"}, {"text": "recovery", "type": "BiologicFunction"}, {"text": "myotonic dystrophy type 1", "type": "BiologicFunction"}, {"text": "DM1", "type": "BiologicFunction"}, {"text": "skeletal muscle level fibres rearrangement", "type": "BiologicFunction"}, {"text": "muscle weakness", "type": "Finding"}, {"text": "myotonia", "type": "Finding"}, {"text": "distal muscles", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Allodynia was measured using Von Frey filaments to calculate the mechanical pain threshold .

Example answer:
{"entities": [{"text": "Allodynia", "type": "Finding"}, {"text": "Von Frey filaments", "type": "MedicalDevice"}, {"text": "mechanical pain threshold", "type": "Finding"}]}

Input:
Sentence: DNP manifested as mechanical allodynia , which was determined by measuring incidence of foot withdrawal in response to mechanical indentation of the hind paw by an electro von Frey filament .

## Item MedMentions:test:906
Example input:
Sentence: Long - term viral suppression with nucleoside analogues leads to HBsAg loss in a substantial proportion of patients , particularly if HBeAg - negative .

Example answer:
{"entities": [{"text": "viral", "type": "Virus"}, {"text": "suppression", "type": "HealthCareActivity"}, {"text": "nucleoside analogues", "type": "Chemical"}, {"text": "HBsAg", "type": "Chemical"}, {"text": "HBeAg - negative", "type": "Finding"}]}

Example input:
Sentence: Thus awareness is important as additional treatment with ribavirin or pegylated interferon may be required , as in this case , in order to help achieve eradication .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "eradication", "type": "HealthCareActivity"}]}

Example input:
Sentence: Use of nonsteroidal anti - inflammatory drugs ( NSAIDs ) , such as aspirin , has been reported to be beneficial in inflammation - associated diseases like cancer , diabetes and cardiovascular disorders .

Example answer:
{"entities": [{"text": "nonsteroidal anti - inflammatory drugs", "type": "Chemical"}, {"text": "NSAIDs", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "associated diseases", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "cardiovascular disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: Empty Capsids and Macrophage Inhibition / Depletion Increase rAAV Transgene Expression in Joints of Both Healthy and Arthritic Mice Gene therapy has potential to treat rheumatic diseases ; however , the presence of macrophages in the joint might hamper adeno - associated viral vector -mediated gene delivery .

Example answer:
{"entities": [{"text": "Capsids", "type": "AnatomicalStructure"}, {"text": "Macrophage", "type": "AnatomicalStructure"}, {"text": "rAAV", "type": "Chemical"}, {"text": "Transgene", "type": "AnatomicalStructure"}, {"text": "Expression", "type": "BiologicFunction"}, {"text": "Joints", "type": "SpatialConcept"}, {"text": "Arthritic", "type": "BiologicFunction"}, {"text": "Mice", "type": "Eukaryote"}, {"text": "Gene therapy", "type": "HealthCareActivity"}, {"text": "treat", "type": "HealthCareActivity"}, {"text": "rheumatic diseases", "type": "BiologicFunction"}, {"text": "presence", "type": "Finding"}, {"text": "macrophages", "type": "AnatomicalStructure"}, {"text": "joint", "type": "SpatialConcept"}, {"text": "adeno - associated viral", "type": "Virus"}, {"text": "vector", "type": "Chemical"}]}

Example input:
Sentence: Anti - influenza therapy , such as with neuraminidase inhibitors , is effective , but diagnosis at an early phase of infection before viral propagation is critical .

Example answer:
{"entities": [{"text": "neuraminidase inhibitors", "type": "Chemical"}, {"text": "diagnosis", "type": "Finding"}, {"text": "viral propagation", "type": "BiologicFunction"}]}

Example input:
Sentence: Modified nucleoside analogues act as antiviral drugs by targeting Flaviviridae polymerases and integrating into the synthesized product causing premature termination .

Example answer:
{"entities": [{"text": "nucleoside analogues", "type": "Chemical"}, {"text": "antiviral drugs", "type": "Chemical"}, {"text": "Flaviviridae", "type": "Virus"}, {"text": "polymerases", "type": "Chemical"}, {"text": "premature termination", "type": "BiologicFunction"}]}

Example input:
Sentence: Here we demonstrate that in arthritic , but also in healthy , mice administration of agents that influence macrophage activity / number and / or addition of empty decoy capsids substantially improve the efficacy of recombinant adeno - associated viral vector 5 transgene expression in the joint .

Example answer:
{"entities": [{"text": "arthritic", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "administration of agents", "type": "HealthCareActivity"}, {"text": "macrophage", "type": "AnatomicalStructure"}, {"text": "decoy capsids", "type": "AnatomicalStructure"}, {"text": "improve", "type": "Finding"}, {"text": "adeno - associated viral", "type": "Virus"}, {"text": "vector", "type": "Chemical"}, {"text": "transgene", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "joint", "type": "SpatialConcept"}]}

Example input:
Sentence: Manipulation of niche factors influencing the distribution and maintenance of these critical antibody - secreting cells may serve as potential therapeutic targets to enhance antiviral responses postvaccination and postinfection .

Example answer:
{"entities": [{"text": "antibody - secreting cells", "type": "AnatomicalStructure"}, {"text": "antiviral responses", "type": "BiologicFunction"}]}

Example input:
Sentence: One of the strategies considered to suppress the emergence of the drug - resistant viruses is to use drugs inhibiting the host factor , which contributes to HCV proliferation , in combination with direct anti - viral agents .

Example answer:
{"entities": [{"text": "drug - resistant", "type": "BiologicFunction"}, {"text": "viruses", "type": "Virus"}, {"text": "drugs", "type": "Chemical"}, {"text": "HCV", "type": "Virus"}, {"text": "anti - viral agents", "type": "Chemical"}]}

Example input:
Sentence: Considering current HCV treatments , to avoid the emergence of direct anti - viral agents - resistant viruses , combination therapy with direct anti - viral agents and host - targeted agents would be optimal .

Example answer:
{"entities": [{"text": "HCV", "type": "Virus"}, {"text": "treatments", "type": "HealthCareActivity"}, {"text": "anti - viral agents", "type": "Chemical"}, {"text": "viruses", "type": "Virus"}, {"text": "combination therapy", "type": "HealthCareActivity"}, {"text": "agents", "type": "Chemical"}]}

Input:
Sentence: Ideally , new treatment alternatives should suppress unwanted inflammation , but spare beneficial antiviral immunity .

## Item MedMentions:test:660
Example input:
Sentence: Vasopressin regulates the growth of the biliary epithelium in polycystic liver disease The neurohypophysial hormone arginine vasopressin ( AVP ) acts by three distinct receptor subtypes : V1a , V1b , and V2 .

Example answer:
{"entities": [{"text": "Vasopressin", "type": "Chemical"}, {"text": "regulates the growth", "type": "BiologicFunction"}, {"text": "polycystic liver disease", "type": "AnatomicalStructure"}, {"text": "neurohypophysial hormone", "type": "Chemical"}, {"text": "arginine vasopressin", "type": "Chemical"}, {"text": "AVP", "type": "Chemical"}, {"text": "receptor", "type": "Chemical"}, {"text": "V1a", "type": "Chemical"}, {"text": "V1b", "type": "Chemical"}, {"text": "V2", "type": "Chemical"}]}

Example input:
Sentence: In vitro , small and large mouse cholangiocytes , H69 ( non - malignant human cholangiocytes ) and LCDE ( human cholangiocytes from the cystic epithelium ) were stimulated with vasopressin in the absence / presence of AVP antagonists such as OPC - 31260 and Tolvaptan , before assessing cellular growth by MTT assay and cAMP levels .

Example answer:
{"entities": [{"text": "mouse", "type": "Eukaryote"}, {"text": "H69", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "LCDE", "type": "AnatomicalStructure"}, {"text": "cystic epithelium", "type": "AnatomicalStructure"}, {"text": "stimulated", "type": "BiologicFunction"}, {"text": "vasopressin", "type": "Chemical"}, {"text": "presence", "type": "Finding"}, {"text": "AVP antagonists", "type": "Chemical"}, {"text": "OPC - 31260", "type": "Chemical"}, {"text": "Tolvaptan", "type": "Chemical"}, {"text": "cellular growth", "type": "BiologicFunction"}, {"text": "MTT assay", "type": "HealthCareActivity"}, {"text": "cAMP", "type": "Chemical"}]}

Example input:
Sentence: Previously , we had shown that diperoxovanadate , a physiologically stable peroxovanadium compound , can substitute H2O2 effectively in peroxidation reactions .

Example answer:
{"entities": [{"text": "diperoxovanadate", "type": "Chemical"}, {"text": "peroxovanadium compound", "type": "Chemical"}, {"text": "H2O2", "type": "Chemical"}]}

Example input:
Sentence: The objective of the study was to test the potential ovarian cancer chemopreventive effect of the p53 stabilizing compound CP - 31398 on hens that spontaneously present the ovarian cancer phenotype .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "BiologicFunction"}, {"text": "p53", "type": "Chemical"}, {"text": "stabilizing compound", "type": "Chemical"}, {"text": "CP - 31398", "type": "Chemical"}, {"text": "hens", "type": "Eukaryote"}]}

Example input:
Sentence: In addition , an increased expression of N - methyl - d - aspartic acid ( NMDA ) receptors and a decreased expression of γ - aminobutyric acid ( GABA ) receptors in this cancer pain were prevented by PTD - Cu / Zn SOD administration or peroxiredoxin 4 overexpression .

Example answer:
{"entities": [{"text": "N - methyl - d - aspartic acid ( NMDA ) receptors", "type": "Chemical"}, {"text": "γ - aminobutyric acid ( GABA ) receptors", "type": "Chemical"}, {"text": "cancer pain", "type": "Finding"}, {"text": "PTD", "type": "SpatialConcept"}, {"text": "Cu / Zn SOD", "type": "Chemical"}, {"text": "peroxiredoxin 4", "type": "Chemical"}, {"text": "overexpression", "type": "BiologicFunction"}]}

Example input:
Sentence: Combretastatin A - 4 ( CA - 4 ) is a well - known vasculature - disrupting agent , which has been shown to effectively kill a variety of cancers through inhibition of tubulin polymerization .

Example answer:
{"entities": [{"text": "Combretastatin A - 4", "type": "Chemical"}, {"text": "CA - 4", "type": "Chemical"}, {"text": "vasculature", "type": "AnatomicalStructure"}, {"text": "cancers", "type": "BiologicFunction"}, {"text": "tubulin", "type": "Chemical"}]}

Example input:
Sentence: Similar results were obtained with the administration of miconazole , which inhibits the biosynthesis of epoxyeicosatrienoic acids ( EETs ) , endogenous agonists for TRPV4 , from arachidonic acid ( AA ) .

Example answer:
{"entities": [{"text": "administration", "type": "HealthCareActivity"}, {"text": "miconazole", "type": "Chemical"}, {"text": "epoxyeicosatrienoic acids", "type": "Chemical"}, {"text": "EETs", "type": "Chemical"}, {"text": "agonists", "type": "Chemical"}, {"text": "TRPV4", "type": "Chemical"}, {"text": "arachidonic acid", "type": "Chemical"}, {"text": "AA", "type": "Chemical"}]}

Example input:
Sentence: The PAPV -mediated growth arrest was significantly abrogated in cells pre - treated with the N - acetylcysteine , Rac1 knocked down by siRNA and DPI an inhibitor of NADPH oxidase .

Example answer:
{"entities": [{"text": "PAPV", "type": "Chemical"}, {"text": "growth arrest", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "N - acetylcysteine", "type": "Chemical"}, {"text": "Rac1", "type": "Chemical"}, {"text": "knocked down", "type": "ResearchActivity"}, {"text": "siRNA", "type": "Chemical"}, {"text": "DPI", "type": "Chemical"}, {"text": "NADPH oxidase", "type": "Chemical"}]}

Example input:
Sentence: Growth arrest of lung carcinoma cells ( A549 ) by polyacrylate - anchored peroxovanadate by activating Rac1 - NADPH oxidase signalling axis Hydrogen peroxide is often required in sublethal , millimolar concentrations to show its oxidant effects on cells in culture as it is easily destroyed by cellular catalase .

Example answer:
{"entities": [{"text": "Growth arrest", "type": "BiologicFunction"}, {"text": "lung carcinoma", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "( A549 )", "type": "AnatomicalStructure"}, {"text": "polyacrylate", "type": "Chemical"}, {"text": "anchored", "type": "HealthCareActivity"}, {"text": "peroxovanadate", "type": "Chemical"}, {"text": "Rac1", "type": "Chemical"}, {"text": "NADPH oxidase", "type": "Chemical"}, {"text": "signalling", "type": "BiologicFunction"}, {"text": "axis", "type": "SpatialConcept"}, {"text": "Hydrogen peroxide", "type": "Chemical"}, {"text": "sublethal", "type": "Finding"}, {"text": "oxidant effects", "type": "Chemical"}, {"text": "cellular", "type": "AnatomicalStructure"}, {"text": "catalase", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , our results show that polyacrylate derivative of peroxovanadate efficiently arrests growth of A549 cancerous cells by activating the axis of Rac1 - NADPH oxidase leading to oxidative stress and DNA damage .

Example answer:
{"entities": [{"text": "polyacrylate", "type": "Chemical"}, {"text": "peroxovanadate", "type": "Chemical"}, {"text": "arrests growth", "type": "BiologicFunction"}, {"text": "A549", "type": "AnatomicalStructure"}, {"text": "cancerous cells", "type": "AnatomicalStructure"}, {"text": "axis", "type": "SpatialConcept"}, {"text": "Rac1", "type": "Chemical"}, {"text": "NADPH oxidase", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "DNA damage", "type": "BiologicFunction"}]}

Input:
Sentence: We report here that peroxovanadate when anchored to polyacrylic acid ( PAPV ) becomes a highly potent inhibitor of growth of lung carcinoma cells ( A549 ) .

## Item MedMentions:test:761
Example input:
Sentence: Furthermore , sdeA and gcsA mutants displayed growth defects and raft mislocalization , which were accompanied by reduced neutral lipids levels and attenuated G .

Example answer:
{"entities": [{"text": "sdeA", "type": "AnatomicalStructure"}, {"text": "gcsA", "type": "AnatomicalStructure"}, {"text": "mutants", "type": "BiologicFunction"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "raft", "type": "AnatomicalStructure"}, {"text": "reduced neutral lipids levels", "type": "Finding"}, {"text": "G .", "type": "Eukaryote"}]}

Example input:
Sentence: The transformed plants showed 91 - 102 % increase in total phenolic contents and 53 - 65 % increase in total flavonoid contents compared to untransformed plants .

Example answer:
{"entities": [{"text": "transformed plants", "type": "Eukaryote"}, {"text": "phenolic", "type": "Chemical"}, {"text": "flavonoid", "type": "Chemical"}, {"text": "untransformed plants", "type": "Eukaryote"}]}

Example input:
Sentence: Subcellular reprogramming of metabolism during cold acclimation in Arabidopsis thaliana Metabolite changes in plant leaves during exposure to low temperatures involve re - allocation of a large number of metabolites between sub - cellular compartments .

Example answer:
{"entities": [{"text": "Subcellular reprogramming", "type": "BiologicFunction"}, {"text": "metabolism", "type": "BiologicFunction"}, {"text": "cold acclimation", "type": "BiologicFunction"}, {"text": "Arabidopsis thaliana", "type": "Eukaryote"}, {"text": "Metabolite", "type": "Chemical"}, {"text": "plant leaves", "type": "Eukaryote"}, {"text": "metabolites", "type": "Chemical"}, {"text": "sub - cellular compartments", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Although increased levels of unmethylated GlcCer were observed in smtA and smtB mutants , ΔsmtA and wild - type cells showed a similar 9 , Me - GlcCer content , reduced by 50 % in the smtB disruptant .

Example answer:
{"entities": [{"text": "unmethylated GlcCer", "type": "Chemical"}, {"text": "smtA", "type": "AnatomicalStructure"}, {"text": "smtB", "type": "AnatomicalStructure"}, {"text": "mutants", "type": "BiologicFunction"}, {"text": "ΔsmtA", "type": "BiologicFunction"}, {"text": "wild - type", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "9 , Me - GlcCer", "type": "Chemical"}, {"text": "disruptant", "type": "BiologicFunction"}]}

Example input:
Sentence: Glycogen metabolism and respiration were higher in Synechocystis and Anabaena than in S .

Example answer:
{"entities": [{"text": "Glycogen metabolism", "type": "BiologicFunction"}, {"text": "respiration", "type": "BiologicFunction"}, {"text": "Synechocystis", "type": "Bacterium"}, {"text": "Anabaena", "type": "Bacterium"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: While attempts have been made to study cellulose metabolism through the use of knock - out mutants , there have been no systematic effort to characterize natural variation for cellulose metabolism in ecotypes adapted to different habitats .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "cellulose metabolism", "type": "BiologicFunction"}, {"text": "knock - out", "type": "BiologicFunction"}, {"text": "mutants", "type": "BiologicFunction"}, {"text": "habitats", "type": "SpatialConcept"}]}

Example input:
Sentence: In this study , we identified a rice Chl -deficient mutant , ygdl - 1 ( yellow green and droopy leaf - 1 ) , which showed yellow - green leaves throughout plant development with decreased content of Chls and carotene and an increased Chl a / b ratio .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "rice", "type": "Food"}, {"text": "Chl", "type": "Chemical"}, {"text": "mutant", "type": "BiologicFunction"}, {"text": "ygdl - 1", "type": "BiologicFunction"}, {"text": "yellow green and droopy leaf - 1", "type": "BiologicFunction"}, {"text": "yellow - green leaves", "type": "Eukaryote"}, {"text": "plant development", "type": "BiologicFunction"}, {"text": "Chls", "type": "Chemical"}, {"text": "carotene", "type": "Chemical"}]}

Example input:
Sentence: Only the double mutant lacking cls and cls2 showed a reduction of the CL content , 83 % lower than the amount produced by the wild - type .

Example answer:
{"entities": [{"text": "double mutant lacking cls", "type": "AnatomicalStructure"}, {"text": "cls2", "type": "AnatomicalStructure"}, {"text": "CL", "type": "Chemical"}, {"text": "wild - type", "type": "AnatomicalStructure"}]}

Example input:
Sentence: While for both , the starchless mutant of plastidial phospho - gluco mutase ( pgm ) and a mutant defective in sucrose - phosphate synthase A1 , metabolic constraints , especially at low temperature , could be uncovered based on subcellularly resolved metabolite profiles , only pgm had lowered freezing tolerance .

Example answer:
{"entities": [{"text": "starchless mutant", "type": "BiologicFunction"}, {"text": "plastidial", "type": "AnatomicalStructure"}, {"text": "phospho - gluco mutase", "type": "Chemical"}, {"text": "pgm", "type": "Chemical"}, {"text": "mutant", "type": "BiologicFunction"}, {"text": "sucrose - phosphate synthase A1", "type": "Chemical"}, {"text": "subcellularly", "type": "AnatomicalStructure"}, {"text": "resolved", "type": "Finding"}, {"text": "metabolite profiles", "type": "BiologicFunction"}, {"text": "freezing tolerance", "type": "BiologicFunction"}]}

Example input:
Sentence: Two mutants of Arabidopsis thaliana representing antipodes in the diversion of carbohydrate metabolism between sucrose and starch were compared to Col - 0 wildtype before and after cold acclimation to investigate interactions of cold acclimation with subcellular re - programming of metabolism .

Example answer:
{"entities": [{"text": "mutants", "type": "BiologicFunction"}, {"text": "Arabidopsis thaliana", "type": "Eukaryote"}, {"text": "antipodes", "type": "AnatomicalStructure"}, {"text": "carbohydrate metabolism", "type": "BiologicFunction"}, {"text": "sucrose", "type": "Chemical"}, {"text": "starch", "type": "Chemical"}, {"text": "Col - 0 wildtype", "type": "Eukaryote"}, {"text": "cold acclimation", "type": "BiologicFunction"}, {"text": "subcellular re - programming", "type": "BiologicFunction"}, {"text": "metabolism", "type": "BiologicFunction"}]}

Input:
Sentence: In addition , the analysis of primary carbon metabolites revealed the significantly reduced levels of sucrose and fructose in the mutant leaves , while the glucose content was similar to wild - type plants .

## Item MedMentions:test:873
Example input:
Sentence: This method is called MS under non - denaturing conditions or native MS and allows the unambiguous determination of protein - ligand interactions .

Example answer:
{"entities": [{"text": "method", "type": "IntellectualProduct"}, {"text": "MS", "type": "HealthCareActivity"}, {"text": "protein", "type": "Chemical"}, {"text": "ligand", "type": "Chemical"}, {"text": "interactions", "type": "BiologicFunction"}]}

Example input:
Sentence: The immobilization approach includes the loading of DSPE - PEG ( 2000 ) - biotin containing sterically stabilized micelles ( SSMs ) which are restructured in a buffer change step , resulting in an accessible substrate for liposome immobilization .

Example answer:
{"entities": [{"text": "immobilization", "type": "HealthCareActivity"}, {"text": "DSPE - PEG ( 2000 )", "type": "Chemical"}, {"text": "biotin", "type": "Chemical"}, {"text": "micelles", "type": "Chemical"}, {"text": "SSMs", "type": "Chemical"}, {"text": "liposome", "type": "Chemical"}]}

Example input:
Sentence: Heteroprotein Complex Formation of Bovine Lactoferrin and Pea Protein Isolate : A Multiscale Structural Analysis Associative electrostatic interactions between two oppositely charged globular proteins , lactoferrin ( LF ) and pea protein isolate ( PPI ) , the latter being a mixture of vicilin , legumin , and convicilin , was studied with a specific PPI / LF molar ratio at room temperature .

Example answer:
{"entities": [{"text": "Heteroprotein", "type": "Chemical"}, {"text": "Complex", "type": "Chemical"}, {"text": "Bovine Lactoferrin", "type": "Chemical"}, {"text": "Isolate", "type": "Chemical"}, {"text": "lactoferrin", "type": "Chemical"}, {"text": "LF", "type": "Chemical"}, {"text": "isolate", "type": "Chemical"}, {"text": "vicilin", "type": "Chemical"}, {"text": "legumin", "type": "Chemical"}, {"text": "convicilin", "type": "Chemical"}, {"text": "studied", "type": "ResearchActivity"}, {"text": "room temperature", "type": "Finding"}]}

Example input:
Sentence: In this paper we examined the protein structure refinement by means of potential energy minimization using immune computing as a method of sampling conformations .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "protein structure", "type": "Chemical"}, {"text": "immune computing", "type": "IntellectualProduct"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "conformations", "type": "SpatialConcept"}]}

Example input:
Sentence: Furthermore , through structural analysis of the protein , we propose the binding sites of substrate and product molecules that were characterized as two hydrophobic superficial pockets located at opposite ends of the enolase connected through a channel where the catalysis of dehydration and isomerization might occur .

Example answer:
{"entities": [{"text": "structural analysis", "type": "HealthCareActivity"}, {"text": "protein", "type": "Chemical"}, {"text": "binding sites", "type": "Chemical"}, {"text": "enolase", "type": "Chemical"}, {"text": "channel", "type": "Chemical"}]}

Example input:
Sentence: Using this approach , we demonstrate how self - conjugation of a secreted industrial enzyme , XynA , dramatically increases its resilience to boiling , and we show that cellular consortia can be engineered to self - assemble functional protein - protein conjugates with tunable composition .

Example answer:
{"entities": [{"text": "self - conjugation", "type": "BiologicFunction"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "enzyme", "type": "Chemical"}, {"text": "XynA", "type": "Chemical"}, {"text": "cellular consortia", "type": "AnatomicalStructure"}, {"text": "engineered", "type": "ResearchActivity"}, {"text": "protein - protein conjugates", "type": "Chemical"}]}

Example input:
Sentence: Membrane Protein Solubilization and Composition of Protein Detergent Complexes Membrane proteins are typically expressed in heterologous systems with a view to in vitro characterization .

Example answer:
{"entities": [{"text": "Membrane Protein Solubilization", "type": "BiologicFunction"}, {"text": "Protein", "type": "Chemical"}, {"text": "Detergent", "type": "Chemical"}, {"text": "Complexes", "type": "Chemical"}, {"text": "Membrane proteins", "type": "Chemical"}, {"text": "typically expressed", "type": "BiologicFunction"}]}

Example input:
Sentence: In the second part of the chapter we illustrate how to analyze the composition of protein detergent complexes ; this analysis is important as it has been found that compositional variation often causes irreproducible results .

Example answer:
{"entities": [{"text": "analyze", "type": "ResearchActivity"}, {"text": "protein", "type": "Chemical"}, {"text": "detergent", "type": "Chemical"}, {"text": "complexes", "type": "Chemical"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: A critical step in the preparation of membrane proteins after expression in any system is the solubilization of the protein in aqueous solution , typically using detergents and lipids , to obtain the protein in a form suitable for purification , structural or functional analysis .

Example answer:
{"entities": [{"text": "membrane proteins", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "solubilization of the protein", "type": "BiologicFunction"}, {"text": "detergents", "type": "Chemical"}, {"text": "lipids", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}, {"text": "structural", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: In this chapter we give a general protocol for preparing protein detergent complexes that is aimed at guiding the reader through the different critical steps .

Example answer:
{"entities": [{"text": "general protocol", "type": "IntellectualProduct"}, {"text": "protein", "type": "Chemical"}, {"text": "detergent", "type": "Chemical"}, {"text": "complexes", "type": "Chemical"}]}

Input:
Sentence: This process is particularly difficult as the objective is to prepare the protein in an unnatural environment , a protein detergent complex , separating it from its natural lipid partners while causing the minimum destabilization or modification of the structure .

## Item MedMentions:test:829
Example input:
Sentence: The study was terminated early for administrative reasons ; 123 patients from Korea , Taiwan , and India were randomized to receive vernakalant ( n = 55 ) or placebo ( n = 56 ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "administrative", "type": "Finding"}, {"text": "Korea", "type": "SpatialConcept"}, {"text": "Taiwan", "type": "SpatialConcept"}, {"text": "India", "type": "SpatialConcept"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "vernakalant", "type": "Chemical"}, {"text": "placebo", "type": "Chemical"}]}

Example input:
Sentence: This prospective , randomized , double - blind , placebo - controlled trial investigates the effect of rTMS on 30 cases of Alzheimer 's disease ( AD ) participants , who were classified into mild and moderate groups .

Example answer:
{"entities": [{"text": "prospective", "type": "ResearchActivity"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "double - blind", "type": "ResearchActivity"}, {"text": "placebo - controlled trial", "type": "ResearchActivity"}, {"text": "rTMS", "type": "HealthCareActivity"}, {"text": "Alzheimer 's disease", "type": "BiologicFunction"}, {"text": "AD", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: A 16 - week assessor - masked randomized controlled trial with a 12 - month follow - up was conducted in 1 university hospital and 1 psychiatric hospital from September 2008 to December 2014 .

Example answer:
{"entities": [{"text": "randomized controlled trial", "type": "ResearchActivity"}, {"text": "university hospital", "type": "Organization"}, {"text": "psychiatric hospital", "type": "Organization"}]}

Example input:
Sentence: Aim : This randomized controlled trial ( RCT ) was conducted to evaluate the short - term efficacy of a multi - component psychosocial intervention program for informal caregivers of persons with neurocognitive disorders in Alexandria , Egypt .

Example answer:
{"entities": [{"text": "randomized controlled trial", "type": "ResearchActivity"}, {"text": "RCT", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "multi - component psychosocial intervention", "type": "HealthCareActivity"}, {"text": "caregivers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "persons", "type": "PopulationGroup"}, {"text": "neurocognitive disorders", "type": "BiologicFunction"}, {"text": "Alexandria", "type": "SpatialConcept"}, {"text": "Egypt", "type": "SpatialConcept"}]}

Example input:
Sentence: In a randomized , double - blind , placebo - controlled , between - subjects design , 40 healthy young adults completed a stimulus - response learning task on either levodopa or placebo .

Example answer:
{"entities": [{"text": "randomized", "type": "ResearchActivity"}, {"text": "double - blind", "type": "ResearchActivity"}, {"text": "stimulus - response learning", "type": "BiologicFunction"}, {"text": "levodopa", "type": "Chemical"}, {"text": "placebo", "type": "ResearchActivity"}]}

Example input:
Sentence: The ACT - ONE trial is a randomized , double - blind , parallel group , placebo - controlled , phase II multicentre trial in patients ( 25 - 80 years ) with stages III or IV colorectal cancer or non - small cell lung cancer -related cachexia that tested two doses of espindolol ( a novel non - selective β blocker with central 5 - HT1a and partial β2 receptor agonist effects ) .

Example answer:
{"entities": [{"text": "ACT - ONE trial", "type": "ResearchActivity"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "double - blind", "type": "ResearchActivity"}, {"text": "parallel group", "type": "ResearchActivity"}, {"text": "phase II multicentre trial", "type": "ResearchActivity"}, {"text": "stages III or IV colorectal cancer", "type": "BiologicFunction"}, {"text": "non - small cell lung cancer", "type": "BiologicFunction"}, {"text": "cachexia", "type": "Finding"}, {"text": "espindolol", "type": "Chemical"}, {"text": "non - selective β blocker", "type": "Chemical"}, {"text": "central 5 - HT1a", "type": "Chemical"}, {"text": "β2 receptor agonist", "type": "Chemical"}]}

Example input:
Sentence: Methods : A pair - matched , placebo - controlled study design included 20 resistance - trained participants assigned to IHRT ( FIO2 0 . 143 ) or placebo ( FIO2 0 . 20 ) , ( n = 10 per group ) .

Example answer:
{"entities": [{"text": "resistance - trained", "type": "HealthCareActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "IHRT", "type": "HealthCareActivity"}, {"text": "FIO2", "type": "HealthCareActivity"}]}

Example input:
Sentence: Randomized , double - blind , placebo - controlled study .

Example answer:
{"entities": [{"text": "Randomized", "type": "ResearchActivity"}, {"text": "double - blind", "type": "ResearchActivity"}]}

Example input:
Sentence: This parallel , placebo - controlled , phase 2 , randomized trial was conducted at three US academic medical centers .

Example answer:
{"entities": [{"text": "parallel", "type": "ResearchActivity"}, {"text": "placebo - controlled", "type": "ResearchActivity"}, {"text": "phase 2", "type": "ResearchActivity"}, {"text": "randomized trial", "type": "ResearchActivity"}, {"text": "US", "type": "SpatialConcept"}, {"text": "academic medical centers", "type": "Organization"}]}

Example input:
Sentence: This is a double - blind , randomised , placebo - controlled , parallel - group superiority trial with two parallel arms .

Example answer:
{"entities": [{"text": "double - blind", "type": "ResearchActivity"}, {"text": "randomised", "type": "ResearchActivity"}]}

Input:
Sentence: A parallel , double - blind , randomized , placebo - controlled clinical trial was carried out .

## Item MedMentions:test:869
Example input:
Sentence: The implant survival rate was 99 % at the two - year follow - up .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Main Outcomes and Measures : Body composition ( Dual Energy X - ray Absorptiometry ) and metabolic parameters were compared in PWS adults ( mean age , 25 . 5 ± 8 . 9 y ) with deletion ( n = 47 ) or uniparental disomy ( UPD ) ( n = 26 ) , taking into account GH treatment in childhood and / or adolescence .

Example answer:
{"entities": [{"text": "Dual Energy X - ray Absorptiometry", "type": "HealthCareActivity"}, {"text": "metabolic parameters", "type": "Finding"}, {"text": "PWS", "type": "AnatomicalStructure"}, {"text": "deletion", "type": "BiologicFunction"}, {"text": "uniparental disomy", "type": "BiologicFunction"}, {"text": "UPD", "type": "BiologicFunction"}]}

Example input:
Sentence: There was no significant difference ( P > 0 . 05 ) in baseline age ( t = 0 . 64 ) , body mass index value ( t = 0 . 51 ) , prostate volume ( t = 0 . 87 ) , prostate - specific antigen levels ( t = 0 . 43 ) , maximal ( t = 0 . 84 ) and average flow rate ( t = 0 . 59 ) , and post - void residual urine volume ( t = 0 . 71 ) .

Example answer:
{"entities": [{"text": "body mass index value", "type": "ClinicalAttribute"}, {"text": "prostate - specific antigen levels", "type": "HealthCareActivity"}, {"text": "maximal", "type": "Finding"}, {"text": "average flow rate", "type": "Finding"}, {"text": "residual urine volume", "type": "Finding"}]}

Example input:
Sentence: Subjects were divided into sex - specific tertiles based on the difference in their BMI ( DBMI ) over a 6 - year period ( 6 - 12 years of age ) .

Example answer:
{"entities": [{"text": "Subjects", "type": "PopulationGroup"}, {"text": "sex - specific tertiles", "type": "IntellectualProduct"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "DBMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: No group differences were found for intraoperative blood loss , hospitalization times , positive surgical margins , biochemical recurrence , sexual dysfunction or need for adjuvant therapy .

Example answer:
{"entities": [{"text": "blood loss", "type": "Finding"}, {"text": "hospitalization", "type": "HealthCareActivity"}, {"text": "positive surgical margins", "type": "Finding"}, {"text": "sexual dysfunction", "type": "BiologicFunction"}, {"text": "adjuvant therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Difference between groups was statistically significant for age , number of teeth and frequency of dental checkups ( p < 0 .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}, {"text": "teeth", "type": "AnatomicalStructure"}, {"text": "dental checkups", "type": "HealthCareActivity"}]}

Example input:
Sentence: All of the implants were clinically stable during a mean follow - up period of 39 . 2 months .

Example answer:
{"entities": [{"text": "implants", "type": "MedicalDevice"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Five - year OS was significantly longer in the high BMI group ( 82 . 2 % ) when compared to that of the low BMI group ( 66 . 2 % ) ( HR 0 . 597 ; 95 % CI 0 . 370 - 0 . 963 ; p = 0 .

Example answer:
{"entities": [{"text": "high BMI", "type": "Finding"}, {"text": "group", "type": "PopulationGroup"}, {"text": "low BMI", "type": "Finding"}]}

Example input:
Sentence: When the population was stratified into three groups in function of the normalized peak filling rate , significant differences were observed among groups for age ( p = 0 . 002 ) , mean wall thickness ( p = 0 . 036 ) , and myocardial mass ( p = 0 . 046 ) and atrial dimensions , whereas no significant differences with respect to late enhancement were seen .

Example answer:
{"entities": [{"text": "population", "type": "PopulationGroup"}, {"text": "late enhancement", "type": "HealthCareActivity"}]}

Example input:
Sentence: At baseline , the groups matched in anthropometrics and body composition , and only differed by 4 . 2 years in age ( mean [ 95 % confidence limits ] 49 . 2 [ 48 . 5 - 49 . 9 ] vs 53 .

Example answer:
{"entities": [{"text": "groups", "type": "PopulationGroup"}, {"text": "anthropometrics", "type": "ClinicalAttribute"}]}

Input:
Sentence: There were no significant differences in age , follow - up time , body mass index , implant volume , or implant projection between groups .

## Item MedMentions:test:868
Example input:
Sentence: Pressure treatment resulted in lower VSS scores compared with sham - treated scars .

Example answer:
{"entities": [{"text": "Pressure treatment", "type": "HealthCareActivity"}, {"text": "VSS", "type": "IntellectualProduct"}, {"text": "sham - treated", "type": "HealthCareActivity"}, {"text": "scars", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Independent t - tests were used to compare girls with and without DBD , while path analyses tested for the mediating role of post - trauma symptoms in the relation between stress regulating systems and externalizing behaviour . Females with DBD ( n = 37 ) reported significantly higher rates of post - trauma symptoms and externalizing behaviour problems than girls without DBD ( n = 39 ) .

Example answer:
{"entities": [{"text": "t - tests", "type": "IntellectualProduct"}, {"text": "DBD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "stress regulating systems", "type": "BodySystem"}, {"text": "externalizing behaviour", "type": "Finding"}, {"text": "externalizing behaviour problems", "type": "BiologicFunction"}]}

Example input:
Sentence: The relationship between changes in Vancouver Scar Scale ( VSS ) scores of pressure - treated scars and differential regulation of elastin was assessed .

Example answer:
{"entities": [{"text": "Vancouver Scar Scale", "type": "IntellectualProduct"}, {"text": "VSS", "type": "IntellectualProduct"}, {"text": "pressure - treated", "type": "HealthCareActivity"}, {"text": "scars", "type": "AnatomicalStructure"}, {"text": "elastin", "type": "Chemical"}]}

Example input:
Sentence: Differences between the PA and SA cohorts were analyzed by t - test for continuous variables and chi - square test for categorical variables .

Example answer:
{"entities": [{"text": "PA", "type": "BiologicFunction"}, {"text": "SA", "type": "Finding"}, {"text": "cohorts", "type": "PopulationGroup"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "t - test", "type": "IntellectualProduct"}, {"text": "chi - square test", "type": "IntellectualProduct"}]}

Example input:
Sentence: Students completed questionnaires assessing trauma exposure characteristics , PTSD , dissociation , and burnout .

Example answer:
{"entities": [{"text": "Students", "type": "PopulationGroup"}, {"text": "questionnaires", "type": "IntellectualProduct"}, {"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "PTSD", "type": "BiologicFunction"}, {"text": "dissociation", "type": "BiologicFunction"}]}

Example input:
Sentence: Baseline characteristics were compared by TB disease status and , for patients diagnosed with TB , by TB confirmation status using Wilcoxon rank sum test for continuous variables and the Chi - square test for categorical variables .

Example answer:
{"entities": [{"text": "TB disease", "type": "BiologicFunction"}, {"text": "diagnosed", "type": "HealthCareActivity"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "Chi - square test", "type": "IntellectualProduct"}]}

Example input:
Sentence: The unpaired t test , Mann - Whitney test , and multiple regression analysis were performed .

Example answer:
{"entities": [{"text": "unpaired t test", "type": "IntellectualProduct"}, {"text": "Mann - Whitney test", "type": "IntellectualProduct"}]}

Example input:
Sentence: We compared target achievement rates in questionnaires using the Wilcoxon signed - rank test and discussion contents diversity using the Mann - Whitney U test .

Example answer:
{"entities": [{"text": "achievement rates", "type": "Finding"}, {"text": "questionnaires", "type": "IntellectualProduct"}, {"text": "Wilcoxon signed - rank test", "type": "IntellectualProduct"}]}

Example input:
Sentence: Logistic regressions and Mann - Whitney U - tests were used to correlate parameters with late peak toxicity ( dichotomised at grade 1 or 2 ) .

Example answer:
{"entities": [{"text": "Logistic regressions", "type": "ResearchActivity"}, {"text": "parameters", "type": "Finding"}, {"text": "grade", "type": "IntellectualProduct"}]}

Example input:
Sentence: For known - groups validity , the Mann - Whitney U test and Kruskal - Wallis test were used to examine the associations between SF - 6D and EQ - 5D - 5L and patient characteristics .

Example answer:
{"entities": [{"text": "Kruskal - Wallis test", "type": "IntellectualProduct"}, {"text": "SF - 6D", "type": "IntellectualProduct"}, {"text": "EQ - 5D - 5L", "type": "IntellectualProduct"}]}

Input:
Sentence: The baseline characteristics and scar scores were tested using the Mann - Whitney U - test and Student 's t test between the two groups .

## Item MedMentions:test:802
Example input:
Sentence: nov . , isolated from water of an estuary environment A Gram - stain - negative , aerobic , non - motile and ovoid or rod - shaped bacterial strain , designated KEM - 4 T , was isolated from water of an estuary environment on the Yellow Sea , South Korea , and subjected to a polyphasic taxonomic study .

Example answer:
{"entities": [{"text": "nov .", "type": "Bacterium"}, {"text": "Gram - stain - negative", "type": "Finding"}, {"text": "non - motile", "type": "Bacterium"}, {"text": "ovoid", "type": "SpatialConcept"}, {"text": "rod - shaped", "type": "SpatialConcept"}, {"text": "Yellow Sea", "type": "SpatialConcept"}, {"text": "South Korea", "type": "SpatialConcept"}, {"text": "polyphasic taxonomic study", "type": "ResearchActivity"}]}

Example input:
Sentence: Non - specific transient mutualism between the plant parasitic nematode , Bursaphelenchus xylophilus , and the opportunistic bacterium Serratia quinivorans BXF1 , a plant - growth promoting pine endophyte with antagonistic effects The aim of this study is to understand the biological role of Serratia quinivorans BXF1 , a bacterium commonly found associated with Bursaphelenchus xylophilus , the plant parasitic nematode responsible for pine wilt disease .

Example answer:
{"entities": [{"text": "plant parasitic nematode", "type": "Eukaryote"}, {"text": "Bursaphelenchus xylophilus", "type": "Eukaryote"}, {"text": "bacterium", "type": "Bacterium"}, {"text": "Serratia quinivorans BXF1", "type": "Bacterium"}, {"text": "plant - growth", "type": "BiologicFunction"}, {"text": "pine", "type": "Eukaryote"}, {"text": "endophyte", "type": "Eukaryote"}, {"text": "antagonistic", "type": "Chemical"}, {"text": "study", "type": "ResearchActivity"}, {"text": "wilt disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Phylogenetic analyses based on 16S rRNA gene sequences indicated that strain SYP - A7299 T belongs to the genus Arthrobacter and is most closely related to Arthrobacter halodurans JSM 078085 T ( 97 . 4 % 16S rRNA gene sequence similarity ) .

Example answer:
{"entities": [{"text": "Phylogenetic analyses", "type": "ResearchActivity"}, {"text": "16S rRNA gene sequences", "type": "AnatomicalStructure"}, {"text": "strain SYP - A7299 T", "type": "Bacterium"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Arthrobacter", "type": "Bacterium"}, {"text": "Arthrobacter halodurans JSM 078085 T", "type": "Bacterium"}, {"text": "16S rRNA gene sequence", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Cells of strain STM - 7 T were Gram - staining - negative , aerobic , poly -  - hydroxybutyrate -accumulating , motile by a single polar flagellum , rod - shaped that were surrounded by a thick capsule and forming milky white colored colonies .

Example answer:
{"entities": [{"text": "Cells", "type": "AnatomicalStructure"}, {"text": "strain STM - 7 T", "type": "Bacterium"}, {"text": "Gram - staining - negative , aerobic", "type": "Bacterium"}, {"text": "poly -  - hydroxybutyrate", "type": "Chemical"}, {"text": "single polar flagellum", "type": "AnatomicalStructure"}, {"text": "rod - shaped", "type": "SpatialConcept"}, {"text": "capsule", "type": "AnatomicalStructure"}, {"text": "colonies", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Differential phenotypic properties , together with the phylogenetic distinctiveness , revealed that strain KEM - 4 T is separated from recognized Altererythrobacter species .

Example answer:
{"entities": [{"text": "phenotypic properties", "type": "Finding"}, {"text": "Altererythrobacter species", "type": "Bacterium"}]}

Example input:
Sentence: Based on the morphological , physiological , biochemical and chemotaxonomic characters presented in this study , strain SYP - A7299 T represents a novel species of the genus Arthrobacter , for which the name Arthrobacter ginkgonis sp .

Example answer:
{"entities": [{"text": "morphological", "type": "SpatialConcept"}, {"text": "strain SYP - A7299 T", "type": "Bacterium"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Arthrobacter", "type": "Bacterium"}, {"text": "Arthrobacter ginkgonis sp .", "type": "Bacterium"}]}

Example input:
Sentence: On the basis of the data presented , strain KEM - 4 T is considered to represent a novel species of the genus Altererythrobacter , for which the name Altererythrobacter confluentis sp .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Altererythrobacter", "type": "Bacterium"}, {"text": "Altererythrobacter confluentis sp .", "type": "Bacterium"}]}

Example input:
Sentence: nov . , isolated from a spring A bacterial strain , designated STM - 7 T , was isolated from a spring in Taiwan and characterized using a polyphasic taxonomy approach .

Example answer:
{"entities": [{"text": "nov .", "type": "Bacterium"}, {"text": "Taiwan", "type": "SpatialConcept"}]}

Example input:
Sentence: The DNA - DNA hybridization value for strain STM - 7 T with Chitinibacter tainanensis S1 T was less than 47 % .

Example answer:
{"entities": [{"text": "DNA - DNA hybridization", "type": "ResearchActivity"}, {"text": "Chitinibacter tainanensis S1 T", "type": "Bacterium"}]}

Example input:
Sentence: Chitinibacter fontanus sp .

Example answer:
{"entities": [{"text": "Chitinibacter fontanus sp .", "type": "Bacterium"}]}

Input:
Sentence: On the basis of the phylogenetic inference and phenotypic data , strain STM - 7 T should be classified as a novel species , for which the name Chitinibacter fontanus sp .

## Item MedMentions:test:781
Example input:
Sentence: Therefore , we sought to develop a Glucagon - CreER ( T2 ) mouse line that would maintain normal glucagon expression and would be less susceptible to transgene silencing .

Example answer:
{"entities": [{"text": "Glucagon - CreER ( T2 ) mouse line", "type": "AnatomicalStructure"}, {"text": "glucagon", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "transgene", "type": "AnatomicalStructure"}, {"text": "silencing", "type": "BiologicFunction"}]}

Example input:
Sentence: EGCG pretreatment could prevent all these changes and molecular mechanisms underlying the prevention by EGCG were most likely due to reduced production of intracellular ROS through activation of Nrf2 signaling and increased catalase anti - oxidant enzyme .

Example answer:
{"entities": [{"text": "EGCG", "type": "Chemical"}, {"text": "molecular mechanisms", "type": "BiologicFunction"}, {"text": "production", "type": "BiologicFunction"}, {"text": "intracellular ROS", "type": "Chemical"}, {"text": "Nrf2", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "catalase anti - oxidant enzyme", "type": "Chemical"}]}

Example input:
Sentence: Transactivation Domain of Human c - Myc Is Essential to Alleviate Poly ( Q ) -Mediated Neurotoxicity in Drosophila Disease Models Polyglutamine ( poly ( Q ) ) disorders , such as Huntington 's disease ( HD ) and spinocerebellar ataxias , represent a group of neurological disorders which arise due to an atypically expanded poly ( Q ) tract in the coding region of the affected gene .

Example answer:
{"entities": [{"text": "Transactivation", "type": "BiologicFunction"}, {"text": "Domain", "type": "SpatialConcept"}, {"text": "Human c - Myc", "type": "Chemical"}, {"text": "Poly ( Q )", "type": "Chemical"}, {"text": "Neurotoxicity", "type": "InjuryOrPoisoning"}, {"text": "Drosophila", "type": "Eukaryote"}, {"text": "Disease Models", "type": "BiologicFunction"}, {"text": "Polyglutamine", "type": "Chemical"}, {"text": "poly ( Q )", "type": "Chemical"}, {"text": "disorders", "type": "BiologicFunction"}, {"text": "Huntington 's disease", "type": "BiologicFunction"}, {"text": "HD", "type": "BiologicFunction"}, {"text": "spinocerebellar ataxias", "type": "BiologicFunction"}, {"text": "neurological disorders", "type": "BiologicFunction"}, {"text": "expanded", "type": "SpatialConcept"}, {"text": "coding region", "type": "AnatomicalStructure"}, {"text": "gene", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Gcn5 is recruited onto the il - 2 promoter by interacting with the NFAT in T cells upon TCR stimulation .

Example answer:
{"entities": [{"text": "Gcn5", "type": "Chemical"}, {"text": "il - 2", "type": "AnatomicalStructure"}, {"text": "promoter", "type": "Chemical"}, {"text": "NFAT", "type": "Chemical"}, {"text": "T cells", "type": "AnatomicalStructure"}, {"text": "TCR stimulation", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study , we conditionally deleted Gcn5 ( encoded by the Kat2a gene ) specifically in T lymphocytes by crossing floxed Gcn5 and Lck - Cre mice , and demonstrated that Gcn5 plays important roles in multiple stages of T cell functions including development , clonal expansion , and differentiation .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "deleted", "type": "BiologicFunction"}, {"text": "Gcn5", "type": "Chemical"}, {"text": "Kat2a gene", "type": "AnatomicalStructure"}, {"text": "T lymphocytes", "type": "AnatomicalStructure"}, {"text": "crossing", "type": "BiologicFunction"}, {"text": "floxed Gcn5", "type": "AnatomicalStructure"}, {"text": "Lck - Cre", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "T cell functions", "type": "BiologicFunction"}, {"text": "development", "type": "BiologicFunction"}, {"text": "clonal expansion", "type": "BiologicFunction"}, {"text": "differentiation", "type": "BiologicFunction"}]}

Example input:
Sentence: Several signaling pathways are involved in the pathogenesis of DN including elevation in level of angiotensin II , formation of advanced glycation end products ( AGE ) , activation of protein kinase c ( PKC ) , and lipid accumulation .

Example answer:
{"entities": [{"text": "signaling pathways", "type": "BiologicFunction"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "DN", "type": "BiologicFunction"}, {"text": "elevation", "type": "SpatialConcept"}, {"text": "angiotensin II", "type": "Chemical"}, {"text": "advanced glycation end products", "type": "Chemical"}, {"text": "AGE", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "protein kinase c", "type": "Chemical"}, {"text": "PKC", "type": "Chemical"}, {"text": "lipid accumulation", "type": "Finding"}]}

Example input:
Sentence: Co - treatment of GEnC with tryptophanol restored the above high - glucose - induced alterations .

Example answer:
{"entities": [{"text": "GEnC", "type": "AnatomicalStructure"}, {"text": "tryptophanol", "type": "Chemical"}, {"text": "high - glucose", "type": "Finding"}]}

Example input:
Sentence: By inhibiting concurrently many pathways involved in DN pathogenesis , GCN2 kinase may serve as a pharmaceutical target for the treatment of DN .

Example answer:
{"entities": [{"text": "pathways", "type": "BiologicFunction"}, {"text": "DN", "type": "BiologicFunction"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "GCN2 kinase", "type": "Chemical"}, {"text": "pharmaceutical", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Activation of general control nonderepressible 2 kinase protects human glomerular endothelial cells from harmful high - glucose - induced molecular pathways Considering the referred beneficial effects of protein restriction on diabetic nephropathy ( DN ) and the role of renal endothelium in its pathogenesis , we evaluated the effect of general control nonderepressible 2 ( GCN2 ) kinase activation , a sensor of amino acid deprivation , on known detrimental molecular pathways in primary human glomerular endothelial cells ( GEnC ) .

Example answer:
{"entities": [{"text": "Activation", "type": "BiologicFunction"}, {"text": "general control nonderepressible 2 kinase", "type": "Chemical"}, {"text": "human", "type": "Eukaryote"}, {"text": "glomerular endothelial cells", "type": "AnatomicalStructure"}, {"text": "high - glucose", "type": "Finding"}, {"text": "molecular pathways", "type": "BiologicFunction"}, {"text": "protein", "type": "Chemical"}, {"text": "diabetic nephropathy", "type": "BiologicFunction"}, {"text": "DN", "type": "BiologicFunction"}, {"text": "renal", "type": "AnatomicalStructure"}, {"text": "endothelium", "type": "AnatomicalStructure"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "general control nonderepressible 2 ( GCN2 ) kinase", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "amino acid", "type": "Chemical"}, {"text": "GEnC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: GEnC were cultured under normal or high -glucose conditions in the presence or not of the GCN2 kinase activator , tryptophanol .

Example answer:
{"entities": [{"text": "GEnC", "type": "AnatomicalStructure"}, {"text": "cultured", "type": "HealthCareActivity"}, {"text": "high -glucose conditions", "type": "BiologicFunction"}, {"text": "GCN2 kinase", "type": "Chemical"}, {"text": "activator", "type": "BiologicFunction"}, {"text": "tryptophanol", "type": "Chemical"}]}

Input:
Sentence: Activation of GCN2 kinase protects GEnC from high - glucose - induced harmful molecular pathways .

## Item MedMentions:test:941
Example input:
Sentence: Twenty - seven percent of nodules ≤4 mm were reclassified to shorter - term follow - up .

Example answer:
{"entities": [{"text": "nodules", "type": "AnatomicalStructure"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using data from a prospectively maintained database , 1884 lymph node - negative breast cancer patients who underwent partial mastectomy with SLN mapping by a dual - tracer using patent blue dye ( PBD ) and radioisotope were retrospectively studied between January 2000 and July 2013 .

Example answer:
{"entities": [{"text": "database", "type": "IntellectualProduct"}, {"text": "lymph node - negative", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "partial mastectomy", "type": "HealthCareActivity"}, {"text": "SLN mapping", "type": "HealthCareActivity"}, {"text": "patent blue dye", "type": "Chemical"}, {"text": "PBD", "type": "Chemical"}, {"text": "radioisotope", "type": "Chemical"}, {"text": "retrospectively studied", "type": "ResearchActivity"}]}

Example input:
Sentence: Therefore , the contribution of PBD to metastatic nodes identification was relevant for only 2 / 274 patients ( 0 . 8 % ) .

Example answer:
{"entities": [{"text": "PBD", "type": "Chemical"}, {"text": "metastatic nodes", "type": "BiologicFunction"}, {"text": "identification", "type": "HealthCareActivity"}]}

Example input:
Sentence: All patients received four - dimensional CT simulation scan and had respiratory gating if tumor movement exceeded 5 mm .

Example answer:
{"entities": [{"text": "four - dimensional CT simulation scan", "type": "HealthCareActivity"}, {"text": "respiratory gating", "type": "MedicalDevice"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "movement", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients diagnosed with a single lesion of clinical stage T1N0M0 gastric adenocarcinoma , with a diameter of 3 cm or less are eligible for the present study .

Example answer:
{"entities": [{"text": "single lesion", "type": "Finding"}, {"text": "gastric adenocarcinoma", "type": "BiologicFunction"}]}

Example input:
Sentence: There was concordance of tumor location and laterality of positive LN in 82 % [ 95 % confidence interval ( CI ) , 76 - 89 ] .

Example answer:
{"entities": [{"text": "tumor", "type": "BiologicFunction"}, {"text": "location", "type": "SpatialConcept"}, {"text": "positive LN", "type": "Finding"}]}

Example input:
Sentence: Based on personalized malignancy risk , 54 % of nodules > 4 and ≤6 mm were reclassified to longer - term follow - up than recommended by Fleischner .

Example answer:
{"entities": [{"text": "nodules", "type": "AnatomicalStructure"}, {"text": "Fleischner", "type": "Organization"}]}

Example input:
Sentence: Among all included patients ( n = 443 ) , advanced neoplasia was found in 13 of 310 patients ( 4 . 2 % ) of the 1 - to 5 - mm group versus 13 of 133 patients ( 9 . 8 % ) of the 6 - to 9 - mm group ( hazard ratio [ HR ] , 3 . 49 ; 95 % confidence interval [ CI ] , 1 . 6 - 7 . 6 ) .

Example answer:
{"entities": [{"text": "neoplasia", "type": "BiologicFunction"}, {"text": "found", "type": "Finding"}]}

Example input:
Sentence: 34 , 95 % CI : 1 . 12 - 9 . 94 , P = 0 . 031 ) , tumor size ( n = 5 , OR = 3 . 36 , 95 % CI : 2 . 04 - 5 . 51 , P < 0 . 001 ) , lymph node metastasis ( n = 5 , OR = 3 . 15 , 95 % CI : 1 . 89 - 5 . 25 , P < 0 . 001 ) , tobacco use ( n = 3 , OR = 2 . 18 , 95 % CI : 1 . 18 - 4 . 01 , P = 0 . 013 ) , and distant metastasis ( n = 2 , OR = 3 . 06 , 95 % CI : 1 . 19 - 7 . 9 , P = 0 . 02 ) .

Example answer:
{"entities": [{"text": "tumor size", "type": "SpatialConcept"}, {"text": "lymph node metastasis", "type": "Finding"}, {"text": "distant metastasis", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The clinical data of 157 patients with EGC , diagnosed as clinical T1N0M0 with tumors ≤ 40 mm , undergoing SNNS between March 2004 and April 2016 were retrospectively reviewed .

Example answer:
{"entities": [{"text": "clinical data", "type": "IntellectualProduct"}, {"text": "EGC", "type": "BiologicFunction"}, {"text": "diagnosed", "type": "Finding"}, {"text": "T1N0M0 with tumors", "type": "BiologicFunction"}, {"text": "SNNS", "type": "HealthCareActivity"}]}

Input:
Sentence: Patients with tumors < 3 cm and with > 1 node detected by one of the two techniques ( N = 1024 ) were included in this real - life cross - sectional study .

## Item MedMentions:test:710
Example input:
Sentence: Anti LID - 1 serology at baseline showed the best performance to predict ENL ( AUC 0 . 85 ) .

Example answer:
{"entities": [{"text": "Anti LID - 1", "type": "Finding"}, {"text": "serology", "type": "HealthCareActivity"}, {"text": "ENL", "type": "BiologicFunction"}]}

Example input:
Sentence: In the exploratory analysis , patients with DOR ≥12 months ( n = 287 ) or ≥24 months ( n = 133 ) were more likely to experience grade 3 / 4 AEs than the overall population .

Example answer:
{"entities": [{"text": "exploratory analysis", "type": "ResearchActivity"}, {"text": "AEs", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: After reclassifying NIFTP , the positive predictive value of GEC decreased from 42 % ( 95 % confidence interval [ 95 % CI ] , 39 % - 45 % ) to 24 % ( 95 % CI , 22 % - 26 % ) in the AUS group and from 23 % ( 95 % CI , 19 % - 27 % ) to 13 % ( 95 % CI , 9 % - 18 % ) in the SFN group .

Example answer:
{"entities": [{"text": "reclassifying", "type": "IntellectualProduct"}, {"text": "NIFTP", "type": "BiologicFunction"}, {"text": "GEC", "type": "ResearchActivity"}, {"text": "AUS", "type": "Finding"}, {"text": "SFN", "type": "BiologicFunction"}]}

Example input:
Sentence: HRQoL was evaluated at baseline and every 6 weeks while on treatment using the European Organisation for Research and Treatment of Care ( EORTC ) Core Quality of Life Questionnaire ( QLQ - C30 ) and the EuroQoL Five Dimensions Questionnaire ( EQ - 5D ) .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "European Organisation for Research and Treatment of Care ( EORTC ) Core Quality of Life Questionnaire ( QLQ - C30 )", "type": "IntellectualProduct"}, {"text": "EuroQoL Five Dimensions Questionnaire", "type": "IntellectualProduct"}, {"text": "EQ - 5D", "type": "IntellectualProduct"}]}

Example input:
Sentence: The EORTC QLQ - C30 , - C29 and the Wexner score were used to determine functional outcome and quality of life .

Example answer:
{"entities": [{"text": "EORTC QLQ - C30", "type": "IntellectualProduct"}, {"text": "C29", "type": "IntellectualProduct"}]}

Example input:
Sentence: Although OXT had no effect on emotion recognition accuracy , recognition performance was improved because face processing was faster across emotions under the influence of OXT .

Example answer:
{"entities": [{"text": "OXT", "type": "Chemical"}, {"text": "emotion", "type": "BiologicFunction"}, {"text": "recognition", "type": "BiologicFunction"}, {"text": "improved", "type": "Finding"}, {"text": "face", "type": "SpatialConcept"}, {"text": "emotions", "type": "BiologicFunction"}]}

Example input:
Sentence: In this short - term , single - center study , an overnight switch from twice - daily OXC to once - daily ESL in patients with drug - resistant focal epilepsies resulted in improvements in side effects , quality of life , and alertness .

Example answer:
{"entities": [{"text": "single - center study", "type": "ResearchActivity"}, {"text": "switch", "type": "HealthCareActivity"}, {"text": "OXC", "type": "Chemical"}, {"text": "ESL", "type": "Chemical"}, {"text": "drug - resistant", "type": "BiologicFunction"}, {"text": "focal epilepsies", "type": "BiologicFunction"}, {"text": "resulted", "type": "Finding"}, {"text": "side effects", "type": "BiologicFunction"}, {"text": "alertness", "type": "BiologicFunction"}]}

Example input:
Sentence: We investigated the effects of transitioning patients overnight from OXC to ESL .

Example answer:
{"entities": [{"text": "OXC", "type": "Chemical"}, {"text": "ESL", "type": "Chemical"}]}

Example input:
Sentence: Adverse Events Profile total scores improved for 21 / 21 ( 100 . 0 % ) patients , QOLIE - 10 total scores improved for 17 / 21 ( 81 . 0 % ) patients , and alertness scores improved for 16 / 21 ( 76 . 2 % ) patients .

Example answer:
{"entities": [{"text": "Adverse Events Profile", "type": "IntellectualProduct"}, {"text": "improved", "type": "Finding"}, {"text": "QOLIE - 10", "type": "IntellectualProduct"}, {"text": "alertness", "type": "BiologicFunction"}]}

Example input:
Sentence: 3 . Assessments were performed immediately prior to and 5 days after switching from OXC to ESL ( days 0 and 5 , respectively ) .

Example answer:
{"entities": [{"text": "3", "type": "IntellectualProduct"}, {"text": "Assessments", "type": "HealthCareActivity"}, {"text": "switching", "type": "HealthCareActivity"}, {"text": "OXC", "type": "Chemical"}, {"text": "ESL", "type": "Chemical"}]}

Input:
Sentence: After switching from OXC to ESL , there were significant improvements in mean scores for AEP ( P < . 001 ) , QOLIE - 10 ( P = . 001 ) , and alertness ( P < . 05 ) .

## Item MedMentions:test:946
Example input:
Sentence: Although the study had several limitations , no comparison with a control population was the most important one .

Example answer:
{"entities": [{"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: Studies were limited by variable definitions , treatment selection bias , concomitant infections and small sample size .

Example answer:
{"entities": [{"text": "Studies", "type": "ResearchActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "infections", "type": "BiologicFunction"}]}

Example input:
Sentence: Three subgroups were found characterized by high ( 10 . 0 % [ of participants ] ) , wavering above and below moderate ( 26 . 2 % ) and low and variable ( 63 . 8 % ) depression level trajectories .

Example answer:
{"entities": [{"text": "subgroups", "type": "PopulationGroup"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "depression level", "type": "Finding"}]}

Example input:
Sentence: These sufferers participated in a cross - sectional , single - site , study that used a specially designed computer assessment task .

Example answer:
{"entities": [{"text": "cross - sectional , single - site , study", "type": "ResearchActivity"}]}

Example input:
Sentence: A cross - sectional analysis was performed using data from the Dallas Heart Study , a multiethnic population - based study .

Example answer:
{"entities": [{"text": "cross - sectional analysis", "type": "ResearchActivity"}, {"text": "Dallas Heart Study", "type": "ResearchActivity"}, {"text": "multiethnic population - based study", "type": "ResearchActivity"}]}

Example input:
Sentence: Confounders were adjusted with fixed effects for age , gender , BMI , diabetes , CIRS musculoskeletal disorders and duration of symptoms .

Example answer:
{"entities": [{"text": "BMI", "type": "ClinicalAttribute"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "musculoskeletal disorders", "type": "BiologicFunction"}, {"text": "duration", "type": "Chemical"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: Exclusion of complicated cases didn ' t seem to influence overall prevalence of depression , although reduction in severity was apparent .

Example answer:
{"entities": [{"text": "depression", "type": "BiologicFunction"}]}

Example input:
Sentence: After adjustment for potential confounders , women who experienced child death had higher odds for all types of PLEs ( when unadjusted for depression ) ( OR 1 . 20 - 1 . 71 ; p < 0 . 05 ) and depression ( OR = 1 .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "child death", "type": "Finding"}, {"text": "PLEs", "type": "BiologicFunction"}, {"text": "depression", "type": "BiologicFunction"}]}

Example input:
Sentence: Of 3054 included studies , 70 . 7 % ( n = 2160 ) used a cross - sectional design .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "cross - sectional", "type": "ResearchActivity"}]}

Example input:
Sentence: A cross - sectional association in the absence of the longitudinal association can mostly be attributed to reverse causality or residual confounding .

Example answer:
{"entities": [{"text": "longitudinal", "type": "SpatialConcept"}]}

Input:
Sentence: Limitations to the study included the cross sectional design and that the presence of confounders like depression were not recorded .

## Item MedMentions:test:956
Example input:
Sentence: At the end of the study period , the number of different antihypertensive agents was still similar between patients who started with a fixed combination ( 2 . 41 ) and patients who started with a free combination ( 2 . 28 ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "antihypertensive agents", "type": "Chemical"}, {"text": "combination", "type": "Chemical"}]}

Example input:
Sentence: Almost three - quarters took orally administered drugs , of which antispastic and antiepileptic drugs were among the most frequent .

Example answer:
{"entities": [{"text": "orally administered drugs", "type": "Chemical"}, {"text": "antiepileptic drugs", "type": "Chemical"}]}

Example input:
Sentence: The pharmacodynamic effect was detected after the first cycle of adjuvant therapy .

Example answer:
{"entities": [{"text": "pharmacodynamic effect", "type": "BiologicFunction"}, {"text": "detected", "type": "HealthCareActivity"}, {"text": "adjuvant therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Nevertheless , measurement of drug levels should be performed during maintenance , and with loss of response , with persistent high levels of C - reactive protein , and when mucosal lesions are still present .

Example answer:
{"entities": [{"text": "measurement of drug levels", "type": "HealthCareActivity"}, {"text": "C - reactive protein", "type": "Chemical"}, {"text": "mucosal", "type": "AnatomicalStructure"}, {"text": "lesions", "type": "Finding"}, {"text": "present", "type": "Finding"}]}

Example input:
Sentence: With respect to antidrug antibody levels , it will be necessary to define a gold standard method or to establish different cutoff levels for different methodologies .

Example answer:
{"entities": [{"text": "antidrug antibody", "type": "Chemical"}, {"text": "method", "type": "IntellectualProduct"}]}

Example input:
Sentence: In multivariable analysis , agreement with the belief that it is safe to prematurely stop an antibiotic course ( OR : 2 . 8 , CI : 1 . 3 - 5 . 8 ) and concerns about antibiotic side effects ( OR : 2 . 1 , CI : 1 . 1 - 4 . 4 ) were significantly associated with increased odds of reported antibiotic sharing .

Example answer:
{"entities": [{"text": "antibiotic", "type": "Chemical"}]}

Example input:
Sentence: A positive RT dose - survival correlation was observed for the entire study cohort , for those who received systemic therapy , and for those with stage IVA / IVB and IVC disease .

Example answer:
{"entities": [{"text": "systemic therapy", "type": "HealthCareActivity"}, {"text": "stage IVA", "type": "IntellectualProduct"}, {"text": "IVB", "type": "IntellectualProduct"}, {"text": "IVC", "type": "IntellectualProduct"}]}

Example input:
Sentence: Nine ( 60 . 0 % ) events of progression or death occurred by the end of study , and three patients continued to receive the study drug .

Example answer:
{"entities": [{"text": "progression", "type": "BiologicFunction"}, {"text": "death", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "drug", "type": "Chemical"}]}

Example input:
Sentence: After adjustment , antibiotic de - escalation was not associated with a higher risk of mortality ( OR = 0 . 83 , 95 % CI = 0 .

Example answer:
{"entities": [{"text": "antibiotic", "type": "Chemical"}, {"text": "de - escalation", "type": "HealthCareActivity"}]}

Example input:
Sentence: According to statistical analysis , gender as well as the number of drugs prescribed were significant predictors for drug - drug interactions .

Example answer:
{"entities": [{"text": "drugs prescribed", "type": "Chemical"}, {"text": "drug - drug interactions", "type": "BiologicFunction"}]}

Input:
Sentence: In these scenarios , drug and antidrug levels were correlated with clinical outcomes .

## Item MedMentions:test:790
Example input:
Sentence: Prevalence of Physical Activity and Sitting Time Among South Korean Adolescents : Results From the Korean National Health and Nutrition Examination Survey , 2013 This study aimed to describe physical activity ( PA ) and sitting time , and to examine associations between sociodemographic factors , weight status , PA , and sitting time among South Korean adolescents ( 12 - 18 years ) .

Example answer:
{"entities": [{"text": "Sitting", "type": "BiologicFunction"}, {"text": "South Korean", "type": "PopulationGroup"}, {"text": "Korean", "type": "PopulationGroup"}, {"text": "National Health and Nutrition Examination Survey", "type": "ResearchActivity"}, {"text": "sitting", "type": "BiologicFunction"}]}

Example input:
Sentence: However , in 12 countries , the association between overweight perceptions and psychosomatic complaints increased among girls , with particularly strong changes seen in Scotland and Norway .

Example answer:
{"entities": [{"text": "countries", "type": "SpatialConcept"}, {"text": "overweight", "type": "Finding"}, {"text": "perceptions", "type": "BiologicFunction"}, {"text": "girls", "type": "PopulationGroup"}, {"text": "Scotland", "type": "SpatialConcept"}, {"text": "Norway", "type": "SpatialConcept"}]}

Example input:
Sentence: We investigated the association between increased body mass index ( BMI ) during childhood and adult SUA levels in Japan .MethodsWe included 298 children with health examination data between 1981 and 2002 who had also undergone physical examinations after reaching early adulthood ( approximately 27 years old ) .

Example answer:
{"entities": [{"text": "increased body mass index", "type": "Finding"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "SUA levels", "type": "HealthCareActivity"}, {"text": "Japan", "type": "SpatialConcept"}, {"text": "health examination data", "type": "IntellectualProduct"}, {"text": "physical examinations", "type": "HealthCareActivity"}]}

Example input:
Sentence: Trends in Adolescent Overweight Perception and Its Association With Psychosomatic Health 2002 - 2014 : Evidence From 33 Countries Perceiving oneself as overweight is common and strongly associated with adolescents ' subjective well - being .

Example answer:
{"entities": [{"text": "Overweight", "type": "Finding"}, {"text": "Perception", "type": "BiologicFunction"}, {"text": "Countries", "type": "SpatialConcept"}, {"text": "Perceiving", "type": "BiologicFunction"}, {"text": "overweight", "type": "Finding"}]}

Example input:
Sentence: Elevated BP was strongly associated with obesity in all countries .

Example answer:
{"entities": [{"text": "Elevated BP", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "countries", "type": "SpatialConcept"}]}

Example input:
Sentence: Eating habits , physical activity , nutrition knowledge , and self - efficacy by obesity status in upper - grade elementary school students Childhood obesity has increased in recent decades in Korea .

Example answer:
{"entities": [{"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "obesity status", "type": "Finding"}, {"text": "Childhood obesity", "type": "BiologicFunction"}, {"text": "Korea", "type": "SpatialConcept"}]}

Example input:
Sentence: Between 1997 - 2000 and 2011 - 2012 , the prevalence of elevated BP decreased in Korea and did not change substantially in China and in the United States of America .

Example answer:
{"entities": [{"text": "elevated BP", "type": "BiologicFunction"}, {"text": "Korea", "type": "SpatialConcept"}, {"text": "China", "type": "SpatialConcept"}, {"text": "United States of America", "type": "SpatialConcept"}]}

Example input:
Sentence: Data in adolescents aged 10 - 19 years came from China ( 1997 - 2011 , n = 8025 ) , Korea ( 1998 - 2012 , n = 10 119 ) , Seychelles ( 1998 - 2012 , n = 27 569 ) and the United States of America ( 1999 - 2012 , n = 14 580 ) .

Example answer:
{"entities": [{"text": "China", "type": "SpatialConcept"}, {"text": "Korea", "type": "SpatialConcept"}, {"text": "Seychelles", "type": "SpatialConcept"}, {"text": "United States of America", "type": "SpatialConcept"}]}

Example input:
Sentence: Although the prevalence of obesity increased markedly in the four countries , secular BP trends in adolescents differed in countries of different regions .

Example answer:
{"entities": [{"text": "obesity", "type": "BiologicFunction"}, {"text": "countries", "type": "SpatialConcept"}, {"text": "regions", "type": "SpatialConcept"}]}

Example input:
Sentence: Recent blood pressure trends in adolescents from China , Korea , Seychelles and the United States of America , 1997 - 2012 Although the prevalence of obesity is increasing worldwide , secular trends in elevated blood pressure ( BP ) differ across populations .

Example answer:
{"entities": [{"text": "blood pressure", "type": "BiologicFunction"}, {"text": "China", "type": "SpatialConcept"}, {"text": "Korea", "type": "SpatialConcept"}, {"text": "Seychelles", "type": "SpatialConcept"}, {"text": "United States of America", "type": "SpatialConcept"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "worldwide", "type": "SpatialConcept"}, {"text": "elevated blood pressure", "type": "BiologicFunction"}, {"text": "BP", "type": "BiologicFunction"}, {"text": "populations", "type": "PopulationGroup"}]}

Input:
Sentence: We aimed to compare recent BP and obesity trends in adolescents aged 10 - 19 years in China , Korea , Seychelles and the United States of America .

## Item MedMentions:test:1008
Example input:
Sentence: Overall satisfaction did not change statistically between the iterations but the qualitative analysis revealed greater trust in the second prototype .

Example answer:
{"entities": [{"text": "satisfaction", "type": "BiologicFunction"}, {"text": "iterations", "type": "Finding"}, {"text": "qualitative analysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: In conclusion , a male preponderance was observed , with frequent re - presentations , often in high - risk circumstances .

Example answer:
{"entities": [{"text": "male preponderance", "type": "Finding"}, {"text": "high - risk", "type": "Finding"}]}

Example input:
Sentence: Five themes characterized discussion and underpinned their choices : shock and vulnerability , burden of isolation , fear of infection , respect for privacy and confidentiality , and confusion over procedural inconsistencies .

Example answer:
{"entities": [{"text": "shock", "type": "BiologicFunction"}, {"text": "burden of isolation", "type": "Finding"}, {"text": "fear of infection", "type": "BiologicFunction"}, {"text": "confusion over procedural inconsistencies", "type": "BiologicFunction"}]}

Example input:
Sentence: This paper is different in that it assumes that neither country will undertake a significant philosophic or structural change in their healthcare system , but there are lessons to be learned that are inherent in one that could be a major breakthrough for the other .

Example answer:
{"entities": [{"text": "paper", "type": "IntellectualProduct"}, {"text": "country", "type": "SpatialConcept"}, {"text": "structural", "type": "SpatialConcept"}, {"text": "healthcare system", "type": "Organization"}, {"text": "learned", "type": "BiologicFunction"}]}

Example input:
Sentence: Similar associations were identified for hospitals with a higher percentage of patients , who claimed they would recommend these institutions to others .

Example answer:
{"entities": [{"text": "hospitals", "type": "Organization"}]}

Example input:
Sentence: Institutions greatly contrasted in the case numbers and temporal factors used to define experience .

Example answer:
{"entities": [{"text": "Institutions", "type": "Organization"}]}

Example input:
Sentence: Overarching barriers to implementation included : inherent differences between specialist vs generalist settings ; poor communication between healthcare settings ; generic barriers to implementation ; and poor governance structures and leadership .

Example answer:
{"entities": [{"text": "poor communication", "type": "Finding"}, {"text": "healthcare settings", "type": "HealthCareActivity"}, {"text": "governance", "type": "Organization"}]}

Example input:
Sentence: We argue that the profession 's institutional connections , defining tasks , epistemological underpinnings , and social position have changed in major ways during these 2 decades .

Example answer:
{"entities": [{"text": "epistemological", "type": "IntellectualProduct"}]}

Example input:
Sentence: The United States had the highest rate of poor primary care coordination among the 11 high - income countries evaluated .

Example answer:
{"entities": [{"text": "United States", "type": "SpatialConcept"}, {"text": "high - income", "type": "PopulationGroup"}, {"text": "countries", "type": "SpatialConcept"}]}

Example input:
Sentence: Core Privileging and Credentialing : Hospitals ' Approach to Gynecologic Surgery Privileging and credentialing requirements are determined by medical staff leadership at the hospital level to ensure clinicians provide safe healthcare services .

Example answer:
{"entities": [{"text": "Core", "type": "SpatialConcept"}, {"text": "Hospitals '", "type": "Organization"}, {"text": "Approach", "type": "SpatialConcept"}, {"text": "Gynecologic Surgery", "type": "HealthCareActivity"}, {"text": "medical staff", "type": "ProfessionalOrOccupationalGroup"}, {"text": "hospital", "type": "Organization"}, {"text": "clinicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "healthcare services", "type": "Organization"}]}

Input:
Sentence: Major inconsistencies in privileging were found alacross the 5 institutions .

## Item MedMentions:test:1193
Example input:
Sentence: 34 + 11 .

Example answer:
{"entities": []}

Example input:
Sentence: 34 ( t18 = 1 . 50 , p = 0 . 15 , d = 0 . 34 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 1 × 22 .

Example answer:
{"entities": []}

Example input:
Sentence: 735 x 10 ( - 18 ) )

Example answer:
{"entities": []}

Example input:
Sentence: 7 vs 33 .

Example answer:
{"entities": []}

Example input:
Sentence: 28 and 34 .

Example answer:
{"entities": []}

Example input:
Sentence: 33 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 33±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 33 to 1 .

Example answer:
{"entities": []}

Example input:
Sentence: 33×0 .

Example answer:
{"entities": []}

Input:
Sentence: 33×1 .

## Item MedMentions:test:1114
Example input:
Sentence: The mean logMAR BCVA at baseline was 0 . 49 ± 0 . 1 , which remained stable ( 0 . 45 ± 0 . 1 ) 3 months after treatment ( p = 0 . 060 ) .

Example answer:
{"entities": [{"text": "BCVA", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Visuospatial function ( P = . 002 ) , inhibition ( P = . 002 ) , reasoning ( P = . 003 ) , binocular acuity ( P = . 04 ) , and stereopsis ( P = . 005 ) best determined the tactical cluster ( unadjusted R ( 2 ) = . 41 ) .

Example answer:
{"entities": [{"text": "inhibition", "type": "BiologicFunction"}, {"text": "reasoning", "type": "BiologicFunction"}, {"text": "binocular acuity", "type": "Finding"}, {"text": "stereopsis", "type": "BiologicFunction"}, {"text": "tactical cluster", "type": "ResearchActivity"}]}

Example input:
Sentence: Main outcome measures were task - specific performance , distance and near visual acuity ( DVA and NVA ) , intensity and extent of ( foveal ) crowding at 5 m and 40 cm , and stereopsis .

Example answer:
{"entities": [{"text": "distance", "type": "ClinicalAttribute"}, {"text": "DVA", "type": "ClinicalAttribute"}, {"text": "crowding", "type": "Finding"}, {"text": "stereopsis", "type": "BiologicFunction"}]}

Example input:
Sentence: Further improvements were detected at 24 months ( AOFAS , from 57 . 1 ± 14 . 9 before surgery to 86 . 6 ± 10 .

Example answer:
{"entities": [{"text": "AOFAS", "type": "IntellectualProduct"}]}

Example input:
Sentence: At 60 months , median corrected distance VA ) in the fresh group had improved to 20 / 150 from a baseline of counting fingers , whereas the frozen group improved to 20 / 400 from a baseline of hand motions .

Example answer:
{"entities": [{"text": "VA", "type": "ClinicalAttribute"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: The visuo - integrative mode l ( unadjusted R ( 2 ) = . 12 ) comprised binocular acuity ( P = . 007 ) and stereopsis ( P = . 045 ) .

Example answer:
{"entities": [{"text": "visuo - integrative mode", "type": "IntellectualProduct"}, {"text": "binocular acuity", "type": "Finding"}, {"text": "stereopsis", "type": "BiologicFunction"}]}

Example input:
Sentence: The improvements of monocular and binocular acuity in treatment group were better than controls at 3 - and 6 - months ( p < 0 . 05 ) .

Example answer:
{"entities": [{"text": "monocular", "type": "BiologicFunction"}, {"text": "binocular", "type": "BiologicFunction"}, {"text": "acuity", "type": "ClinicalAttribute"}, {"text": "treatment group", "type": "PopulationGroup"}]}

Example input:
Sentence: Attentional shift ( P = . 0004 ) , stereopsis ( P = . 007 ) , glare recovery ( P = . 047 ) , and use of assistive devices ( P = . 03 ) best predicted the operational cluster ( unadjusted R ( 2 ) = . 28 ) .

Example answer:
{"entities": [{"text": "Attentional shift", "type": "Finding"}, {"text": "stereopsis", "type": "BiologicFunction"}, {"text": "glare recovery", "type": "HealthCareActivity"}, {"text": "assistive devices", "type": "MedicalDevice"}, {"text": "operational cluster", "type": "ResearchActivity"}]}

Example input:
Sentence: The average preoperative visual acuity of 20 / 125 ( logMAR 0 . 81 , standard deviation [ SD ] = 0 . 36 ) improved by nearly 4 lines to an average final visual acuity of 20 / 57 ( logMAR 0 . 45 , SD = 0 . 37 ) ( P = .0072 ) .

Example answer:
{"entities": [{"text": "visual acuity", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Near and distance stereopsis in treatment group were better than controls at 3 - and 6 - months ( p < 0 . 05 ) .

Example answer:
{"entities": [{"text": "stereopsis", "type": "BiologicFunction"}, {"text": "treatment group", "type": "PopulationGroup"}]}

Input:
Sentence: 02 logMAR ) and improved stereopsis ( 670 ± 249″ ) .

## Item MedMentions:test:1211
Example input:
Sentence: The objective of this study was to investigate the use of different approaches for assessing exposure to air pollution from biodegradable wastes by analyzing ( 1 ) the misclassification of exposure that is committed by using these surrogates , ( 2 ) the existence of differentia l misclassification ( 3 ) the effects that misclassification may have on health effect estimates and the interpretation of epidemiological results , and ( 4 ) the ability of the exposure measures to predict health outcomes using 10 - fold cross validation .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "exposure", "type": "InjuryOrPoisoning"}, {"text": "analyzing", "type": "ResearchActivity"}, {"text": "misclassification", "type": "IntellectualProduct"}, {"text": "epidemiological", "type": "ResearchActivity"}, {"text": "cross validation", "type": "ResearchActivity"}]}

Example input:
Sentence: It can easily create various reactive chemical species ( ROS ) and is harmless to living body .

Example answer:
{"entities": [{"text": "reactive chemical species", "type": "Chemical"}, {"text": "ROS", "type": "Chemical"}, {"text": "living body", "type": "Eukaryote"}]}

Example input:
Sentence: Results show that dissolved U is bioavailable under all the geochemical conditions tested .

Example answer:
{"entities": [{"text": "Results", "type": "Finding"}, {"text": "dissolved U", "type": "Chemical"}]}

Example input:
Sentence: In this study , we have assessed the ecotoxicity of four engineered Fe nanomaterials , specifically , Nano - Goethite , Trap - Ox Fe - zeolites , Carbo - Iron ( ® ) and FerMEG12 , developed within the European FP7 project NanoRem for sub - surface remediation towards a test battery consisting of eight ecotoxicity tests on bacteria ( V .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "ecotoxicity", "type": "InjuryOrPoisoning"}, {"text": "Fe", "type": "Chemical"}, {"text": "Nano - Goethite", "type": "Chemical"}, {"text": "Trap - Ox Fe - zeolites", "type": "Chemical"}, {"text": "Carbo - Iron", "type": "Chemical"}, {"text": "FerMEG12", "type": "Chemical"}, {"text": "test battery", "type": "HealthCareActivity"}, {"text": "tests", "type": "HealthCareActivity"}, {"text": "bacteria", "type": "Bacterium"}, {"text": "V .", "type": "Bacterium"}]}

Example input:
Sentence: Considering that in vitro assays may have limited metabolic capacity , inactive chemicals that are biotransformed into metabolites with endocrine bioactivity may be missed for further screening and testing .

Example answer:
{"entities": [{"text": "in vitro assays", "type": "HealthCareActivity"}, {"text": "inactive chemicals", "type": "Chemical"}, {"text": "biotransformed", "type": "BiologicFunction"}, {"text": "metabolites", "type": "Chemical"}, {"text": "endocrine", "type": "BodySystem"}]}

Example input:
Sentence: Bioavailability of dissolved U ( VI ) was characterized in controlled laboratory experiments over a range of water hardness , pH , and in the presence of complexing ligands in the form of dissolved natural organic matter ( DOM ) .

Example answer:
{"entities": [{"text": "dissolved U ( VI )", "type": "Chemical"}, {"text": "laboratory", "type": "Organization"}, {"text": "experiments", "type": "ResearchActivity"}, {"text": "water", "type": "Chemical"}, {"text": "presence", "type": "Finding"}, {"text": "complexing ligands", "type": "Chemical"}]}

Example input:
Sentence: The biocompatibility of the materials were established through toxicity studies on cell lines .

Example answer:
{"entities": [{"text": "cell lines", "type": "AnatomicalStructure"}]}

Example input:
Sentence: To assess the environmental fate and effects of thiophenones capable of quorum sensing inhibition , candidate substances were first identified that have potentially high biodegradability and low ecotoxicity using quantitative structure activity relationships .

Example answer:
{"entities": [{"text": "environmental", "type": "SpatialConcept"}, {"text": "quorum sensing", "type": "BiologicFunction"}]}

Example input:
Sentence: Little or no data are available on the authenticity of lifestyle products and actual toxicity associated with their use and misuse .

Example answer:
{"entities": [{"text": "misuse", "type": "Finding"}]}

Example input:
Sentence: Subsequent confirmatory hazard assessment of these substances , using a marine alga and a marine crustacean , indicated that these estimates were significantly under predicted with acute toxicity values more than three orders of magnitude lower than anticipated combined with limited biodegradability .

Example answer:
{"entities": [{"text": "confirmatory", "type": "Finding"}, {"text": "marine alga", "type": "Eukaryote"}, {"text": "crustacean", "type": "Eukaryote"}, {"text": "indicated", "type": "Finding"}, {"text": "acute toxicity", "type": "HealthCareActivity"}]}

Input:
Sentence: However , there are currently limited data regarding the biodegradability or ecotoxicity of these substances .

## Item MedMentions:test:859
Example input:
Sentence: In a sample of 99 healthy volunteers ( 28 water pipe smokers , 30 secondhand tobacco smoke exposed persons , and 41 controls ) , we systematically compared CYP1A2 and CYP2A6 enzyme activities in vivo using caffeine urine test .

Example answer:
{"entities": [{"text": "healthy volunteers", "type": "PopulationGroup"}, {"text": "secondhand tobacco smoke", "type": "InjuryOrPoisoning"}, {"text": "persons", "type": "PopulationGroup"}, {"text": "CYP1A2", "type": "Chemical"}, {"text": "CYP2A6", "type": "Chemical"}, {"text": "enzyme activities", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "caffeine urine test", "type": "HealthCareActivity"}]}

Example input:
Sentence: A model system composed of ( 3 - caffeoylquinic acid lactone ( 3 - CQAL ) , 4 - caffeoyl quinic acid lactone ( 4 - CQAL ) , and 4 - feruloylquinic acid lactone ( 4 - FQAL ) ) was used for the screening of enzymes before treatment of the coffee extracts .

Example answer:
{"entities": [{"text": "model system", "type": "IntellectualProduct"}, {"text": "3 - caffeoylquinic acid lactone", "type": "Chemical"}, {"text": "3 - CQAL", "type": "Chemical"}, {"text": "4 - caffeoyl quinic acid lactone", "type": "Chemical"}, {"text": "4 - CQAL", "type": "Chemical"}, {"text": "4 - feruloylquinic acid lactone", "type": "Chemical"}, {"text": "4 - FQAL", "type": "Chemical"}, {"text": "screening", "type": "ResearchActivity"}, {"text": "enzymes", "type": "Chemical"}, {"text": "coffee extracts", "type": "Chemical"}]}

Example input:
Sentence: We hypothesized that this would offset the antihypertensive effect of the dihydropyridine calcium channel blocker felodipine .

Example answer:
{"entities": [{"text": "antihypertensive", "type": "Chemical"}, {"text": "dihydropyridine calcium channel blocker", "type": "Chemical"}, {"text": "felodipine", "type": "Chemical"}]}

Example input:
Sentence: The total phenol content ( TPC ) , total flavonoid content ( TFC ) , flavonol content ( FC ) and antioxidant activity ( DPPH , ABTS ) in the coffee extracts was determined .

Example answer:
{"entities": [{"text": "phenol", "type": "Chemical"}, {"text": "TPC", "type": "Chemical"}, {"text": "flavonoid", "type": "Chemical"}, {"text": "TFC", "type": "Chemical"}, {"text": "flavonol", "type": "Chemical"}, {"text": "FC", "type": "Chemical"}, {"text": "antioxidant activity", "type": "BiologicFunction"}, {"text": "DPPH", "type": "Chemical"}, {"text": "ABTS", "type": "Chemical"}, {"text": "coffee extracts", "type": "Chemical"}]}

Example input:
Sentence: Pretreatment plasma caffeine concentrations were unquantifiable .

Example answer:
{"entities": [{"text": "plasma", "type": "BodySubstance"}, {"text": "caffeine concentrations", "type": "HealthCareActivity"}]}

Example input:
Sentence: Coffee containing caffeine ( 127 mg ) caused maximum pressor effect .

Example answer:
{"entities": [{"text": "Coffee", "type": "Food"}, {"text": "caffeine", "type": "Chemical"}, {"text": "pressor", "type": "Chemical"}]}

Example input:
Sentence: 05 ) compared to felodipine alone .

Example answer:
{"entities": [{"text": "felodipine", "type": "Chemical"}]}

Example input:
Sentence: Consistently brewed black coffee ( 2×300ml ) , felodipine maximum recommended dose ( 10 mg ) , and coffee plus felodipine were tested in middle - aged normotensive subjects .

Example answer:
{"entities": [{"text": "black coffee", "type": "Food"}, {"text": "felodipine", "type": "Chemical"}, {"text": "coffee", "type": "Food"}, {"text": "normotensive", "type": "Finding"}, {"text": "subjects", "type": "PopulationGroup"}]}

Example input:
Sentence: The pressor effects of coffee and its modulation by felodipine were variable among individuals .

Example answer:
{"entities": [{"text": "pressor", "type": "Chemical"}, {"text": "coffee", "type": "Food"}, {"text": "modulation", "type": "SpatialConcept"}, {"text": "felodipine", "type": "Chemical"}, {"text": "individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: Coffee - Antihypertensive Drug Interaction : A Hemodynamic and Pharmacokinetic Study With Felodipine A period of abstinence from coffee to permit caffeine elimination appears to enable increased blood pressure on subsequent exposure .

Example answer:
{"entities": [{"text": "Coffee", "type": "Food"}, {"text": "Antihypertensive Drug", "type": "Chemical"}, {"text": "Hemodynamic", "type": "BiologicFunction"}, {"text": "Pharmacokinetic Study", "type": "ResearchActivity"}, {"text": "Felodipine", "type": "Chemical"}, {"text": "coffee", "type": "Food"}, {"text": "permit", "type": "IntellectualProduct"}, {"text": "caffeine", "type": "Chemical"}, {"text": "elimination", "type": "BiologicFunction"}, {"text": "blood pressure", "type": "BiologicFunction"}]}

Input:
Sentence: Caffeine and felodipine pharmacokinetics were similar for coffee and felodipine given alone or in combination indicating an interaction having a pharmacodynamic basis .

## Item MedMentions:test:1026
Example input:
Sentence: Despite highlighting good intra - and inter - operator reproducibility , we found that a scale bias between instruments might interfere with thorough CCT monitoring .

Example answer:
{"entities": [{"text": "scale", "type": "IntellectualProduct"}, {"text": "instruments", "type": "MedicalDevice"}, {"text": "CCT", "type": "ClinicalAttribute"}, {"text": "monitoring", "type": "HealthCareActivity"}]}

Example input:
Sentence: Consequently , the prediction accuracy of these predictors in large dataset becomes unknown and needs to be re - tested .

Example answer:
{"entities": [{"text": "predictors", "type": "IntellectualProduct"}, {"text": "dataset", "type": "IntellectualProduct"}]}

Example input:
Sentence: Instrument -to - instrument reproducibility was determined by ANOVA for repeated measurements .

Example answer:
{"entities": [{"text": "Instrument", "type": "MedicalDevice"}, {"text": "instrument", "type": "MedicalDevice"}]}

Example input:
Sentence: The performances of the two methods were compared in terms of bias in the estimates , standard errors , and coverage probability .

Example answer:
{"entities": [{"text": "methods", "type": "IntellectualProduct"}]}

Example input:
Sentence: Despite reasonable inference times being obtained for a relevant set of users and instances , additional work is required to scale to long - term scenarios with a large number of users .

Example answer:
{"entities": [{"text": "inference", "type": "BiologicFunction"}, {"text": "set", "type": "BiologicFunction"}, {"text": "users", "type": "PopulationGroup"}]}

Example input:
Sentence: Future studies should replicate data mining analyses to increase methodology rigor .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "analyses", "type": "ResearchActivity"}]}

Example input:
Sentence: The machine - learning methods investigated herein performed well in both the qualitative classification ( ∼70 % accuracy ) and quantitative IC50 predictions ( RMSE ∼ 1 log ) .

Example answer:
{"entities": [{"text": "methods", "type": "IntellectualProduct"}, {"text": "classification", "type": "IntellectualProduct"}]}

Example input:
Sentence: The performance of a 32R method can be estimated by comparing it to an accurate reference or gold standard method ( usually based on fiducial markers ) on the same set of images ( gold standard dataset ) .

Example answer:
{"entities": [{"text": "gold standard method", "type": "HealthCareActivity"}, {"text": "fiducial markers", "type": "MedicalDevice"}, {"text": "images", "type": "IntellectualProduct"}, {"text": "gold", "type": "Chemical"}, {"text": "dataset", "type": "IntellectualProduct"}]}

Example input:
Sentence: This indicate that dealing with object repetitiveness of datasets is a key issue in protein - protein interactions prediction using SVMs since real world data contain certain degrees of repeat proteins .

Example answer:
{"entities": [{"text": "datasets", "type": "IntellectualProduct"}, {"text": "protein - protein interactions", "type": "BiologicFunction"}, {"text": "proteins", "type": "Chemical"}]}

Example input:
Sentence: To study the effect of object repetitiveness of datasets on predicting results .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "datasets", "type": "IntellectualProduct"}]}

Input:
Sentence: In fact , performance of currently reported methods are significantly over - estimated and affected by the object repetitiveness in the datasets used .

## Item MedMentions:test:897
Example input:
Sentence: The cells were divided into four groups : G1 - osteoblast differentiation medium only ( as the hypoxic condition ) , G2 - treatment with 50 μM melatonin only , G3 - laser irradiation ( 808 nm , 80 mW , GaAlAs diode ) only , and G4 - treatment with 50 μM melatonin and laser irradiation ( 808 nm , 80 mW , GaAlAs diode ) .

Example answer:
{"entities": [{"text": "cells", "type": "AnatomicalStructure"}, {"text": "osteoblast differentiation", "type": "BiologicFunction"}, {"text": "medium", "type": "Chemical"}, {"text": "hypoxic condition", "type": "BiologicFunction"}, {"text": "melatonin", "type": "Chemical"}]}

Example input:
Sentence: Comparative evaluation of iodine - 131 metaiodobenzylguanidine and 18 - fluorodeoxyglucose positron emission tomography in assessing neural crest tumors : Will they play a complementary role ? 18 - Fluorodeoxyglucose positron emission tomography ( FDG - PET ) has established a role in the evaluation of several malignancies .

Example answer:
{"entities": [{"text": "Comparative evaluation", "type": "HealthCareActivity"}, {"text": "iodine - 131 metaiodobenzylguanidine", "type": "Chemical"}, {"text": "18 - fluorodeoxyglucose", "type": "Chemical"}, {"text": "positron emission tomography", "type": "HealthCareActivity"}, {"text": "neural crest tumors", "type": "BiologicFunction"}, {"text": "18 - Fluorodeoxyglucose", "type": "Chemical"}, {"text": "FDG - PET", "type": "HealthCareActivity"}, {"text": "malignancies", "type": "BiologicFunction"}]}

Example input:
Sentence: FDG - PET detected more metastatic foci than ( 131 ) I - MIBG ( 18 vs .

Example answer:
{"entities": [{"text": "FDG - PET", "type": "HealthCareActivity"}, {"text": "metastatic foci", "type": "SpatialConcept"}, {"text": "( 131 ) I - MIBG", "type": "Chemical"}]}

Example input:
Sentence: Focal WM and cortical lesions were identified , and volumetric measures from WM , cortical GM , the hippocampus , and deep GM nuclei were obtained .

Example answer:
{"entities": [{"text": "WM", "type": "AnatomicalStructure"}, {"text": "cortical", "type": "AnatomicalStructure"}, {"text": "lesions", "type": "Finding"}, {"text": "volumetric", "type": "SpatialConcept"}, {"text": "GM", "type": "AnatomicalStructure"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "deep GM", "type": "AnatomicalStructure"}, {"text": "nuclei", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In the inflammatory group , FG -labeled neurons were similarly distributed , primarily at L3 and L4 , and CGRP -positive neurons were significantly more frequent than IB4 - binding neurons .

Example answer:
{"entities": [{"text": "FG", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "L3", "type": "AnatomicalStructure"}, {"text": "L4", "type": "AnatomicalStructure"}, {"text": "CGRP", "type": "Chemical"}, {"text": "IB4", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients with a primary IPMN with HGD or with positive family history are at an increased risk to develop subsequent high - risk neoplasms in the remnant pancreas .

Example answer:
{"entities": [{"text": "IPMN", "type": "BiologicFunction"}, {"text": "HGD", "type": "BiologicFunction"}, {"text": "positive", "type": "Finding"}, {"text": "family history", "type": "Finding"}, {"text": "high - risk", "type": "Finding"}, {"text": "neoplasms", "type": "BiologicFunction"}, {"text": "remnant", "type": "AnatomicalStructure"}, {"text": "pancreas", "type": "AnatomicalStructure"}]}

Example input:
Sentence: With doped Gd species and strong tunable NIR absorbance , Gd : CuS @ BSA NPs demonstrate prominent tumor - contrasted imaging performance both on the photoacoustic and magnetic resonance imaging modalities .

Example answer:
{"entities": [{"text": "doped Gd species", "type": "Chemical"}, {"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "BSA", "type": "Chemical"}, {"text": "tumor - contrasted imaging", "type": "HealthCareActivity"}, {"text": "photoacoustic", "type": "HealthCareActivity"}, {"text": "magnetic resonance imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: Nuclear enlargement , pallor , grooves , and the presence of histiocytoid cells in initially ND FNA correlated with malignancy .

Example answer:
{"entities": [{"text": "Nuclear enlargement", "type": "BiologicFunction"}, {"text": "pallor", "type": "Finding"}, {"text": "grooves", "type": "SpatialConcept"}, {"text": "presence", "type": "Finding"}, {"text": "histiocytoid cells", "type": "AnatomicalStructure"}, {"text": "ND", "type": "Finding"}, {"text": "FNA", "type": "HealthCareActivity"}, {"text": "malignancy", "type": "BiologicFunction"}]}

Example input:
Sentence: Whole slide images were obtained for colonic normal mucosa ( NCM ) , hyperplastic polyps ( HP ) , conventional tubular adenomas ( TA ) , and adenomas with high - grade dysplasia ( HGD ) , and esophageal intestinal metaplasia negative for dysplasia ( IM ) , indefinite for dysplasia ( IFD ) , low - grade dysplasia ( LGD ) , and HGD .

Example answer:
{"entities": [{"text": "slide images", "type": "IntellectualProduct"}, {"text": "hyperplastic polyps", "type": "BiologicFunction"}, {"text": "HP", "type": "BiologicFunction"}, {"text": "tubular adenomas", "type": "BiologicFunction"}, {"text": "TA", "type": "BiologicFunction"}, {"text": "adenomas", "type": "BiologicFunction"}, {"text": "high - grade dysplasia", "type": "BiologicFunction"}, {"text": "HGD", "type": "BiologicFunction"}, {"text": "esophageal intestinal metaplasia", "type": "BiologicFunction"}, {"text": "negative", "type": "Finding"}, {"text": "dysplasia", "type": "BiologicFunction"}, {"text": "IM", "type": "BiologicFunction"}, {"text": "indefinite for dysplasia", "type": "Finding"}, {"text": "IFD", "type": "Finding"}, {"text": "low - grade dysplasia", "type": "BiologicFunction"}, {"text": "LGD", "type": "BiologicFunction"}]}

Example input:
Sentence: Pixel intensity ( brightness ) separated lesions within both groups with statistical significance except for colonic TAs versus HPs and esophageal LGD versus IM .

Example answer:
{"entities": [{"text": "lesions", "type": "Finding"}, {"text": "colonic TAs", "type": "BiologicFunction"}, {"text": "HPs", "type": "BiologicFunction"}, {"text": "esophageal LGD", "type": "BiologicFunction"}]}

Input:
Sentence: HGD nuclei in both groups demonstrated more pixel staining heterogeneity than other lesions .

## Item MedMentions:test:1232
Example input:
Sentence: 04 , < 0 . 01 , 0 . 04 and < 0 . 01 respectively ) than the others .

Example answer:
{"entities": []}

Example input:
Sentence: 026 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 005 .

Example answer:
{"entities": []}

Example input:
Sentence: 004 ; OS : 7 . 9 vs 11 .

Example answer:
{"entities": []}

Example input:
Sentence: 010 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 007 , and p = 0 . 04 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 004 , OR = 8 . 89 , CI = 1 .

Example answer:
{"entities": []}

Example input:
Sentence: 006 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 004 )

Example answer:
{"entities": []}

Example input:
Sentence: 004 ) .

Example answer:
{"entities": []}

Input:
Sentence: 004 , respectively ) .

## Item MedMentions:test:1031
Example input:
Sentence: The bacterial lipopolysaccharide ( LPS ) was injected intravenously ( iv ) on TGFβ reporter mice ( Smad - binding element ( SBE ) / Tk - Luc ) to study in their brains the real - time activation profile of the TGFβ pathway in a non - invasive way .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "injected intravenously", "type": "HealthCareActivity"}, {"text": "TGFβ", "type": "Chemical"}, {"text": "reporter mice", "type": "Eukaryote"}, {"text": "Smad - binding element", "type": "Chemical"}, {"text": "SBE", "type": "Chemical"}, {"text": "study", "type": "ResearchActivity"}, {"text": "brains", "type": "AnatomicalStructure"}, {"text": "real - time activation profile", "type": "HealthCareActivity"}, {"text": "TGFβ pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: The early activation of STAT1α ( detected by phospho - serine727 and phoshpo - tyrosine701 ) by IFNγ and the late activation of STAT1α by LPS were not affected in the presence of cPLA2α inhibitors , indicating that STAT1α is not under cPLA2α regulation .

Example answer:
{"entities": [{"text": "STAT1α", "type": "Chemical"}, {"text": "phospho - serine727", "type": "Chemical"}, {"text": "phoshpo - tyrosine701", "type": "Chemical"}, {"text": "IFNγ", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "cPLA2α", "type": "Chemical"}, {"text": "inhibitors", "type": "Chemical"}, {"text": "regulation", "type": "BiologicFunction"}]}

Example input:
Sentence: Anti - PGL - I serology had a limited predictive value for RR according to receiver operating curve / ROC analyses ( area - under - the - curve / AUC = 0 . 7 ) .

Example answer:
{"entities": [{"text": "Anti - PGL - I", "type": "Finding"}, {"text": "serology", "type": "HealthCareActivity"}, {"text": "RR", "type": "BiologicFunction"}]}

Example input:
Sentence: High levels of Lp ( a ) may be particularly important in the pathogenesis of CAD in AAs .

Example answer:
{"entities": [{"text": "Lp ( a )", "type": "Chemical"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "CAD", "type": "BiologicFunction"}, {"text": "AAs", "type": "PopulationGroup"}]}

Example input:
Sentence: IL - 8 was measured using a radioimmunoassay , surfactant protein D ( SP - D ) was measured by ELISA , and matrix metalloproteinase ( MMP ) 2 and MMP8 expression was assessed by PCR .

Example answer:
{"entities": [{"text": "IL - 8", "type": "Chemical"}, {"text": "radioimmunoassay", "type": "HealthCareActivity"}, {"text": "surfactant protein D", "type": "Chemical"}, {"text": "SP - D", "type": "Chemical"}, {"text": "ELISA", "type": "HealthCareActivity"}, {"text": "matrix metalloproteinase ( MMP ) 2", "type": "Chemical"}, {"text": "MMP8", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "PCR", "type": "ResearchActivity"}]}

Example input:
Sentence: Enzyme - linked immunosorbent assay measured prolactin secretion .

Example answer:
{"entities": [{"text": "Enzyme - linked immunosorbent assay", "type": "HealthCareActivity"}, {"text": "prolactin secretion", "type": "BiologicFunction"}]}

Example input:
Sentence: The relation of Lp ( a ) with the extent and severity of subclinical coronary plaque has not been described in AAs .

Example answer:
{"entities": [{"text": "Lp ( a )", "type": "Chemical"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "coronary", "type": "AnatomicalStructure"}, {"text": "plaque", "type": "Finding"}, {"text": "AAs", "type": "PopulationGroup"}]}

Example input:
Sentence: ELISA was applied to assay serum concentration of IL - 2 and IL - 10 .

Example answer:
{"entities": [{"text": "ELISA", "type": "HealthCareActivity"}, {"text": "IL - 2", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}]}

Example input:
Sentence: IgM and IgG antibody responses to PGL - I , LID - 1 , ND - O - LID were evaluated by ELISA in 452 reaction - free leprosy patients at diagnosis , enrolled and monitored for the development of leprosy reactions during a total person - time of 780 , 930 person - days , i .

Example answer:
{"entities": [{"text": "IgM", "type": "Chemical"}, {"text": "IgG", "type": "Chemical"}, {"text": "antibody responses", "type": "BiologicFunction"}, {"text": "PGL - I", "type": "Chemical"}, {"text": "LID - 1", "type": "Chemical"}, {"text": "ND - O - LID", "type": "Chemical"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "ELISA", "type": "HealthCareActivity"}, {"text": "reaction - free", "type": "Finding"}, {"text": "leprosy", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "monitored", "type": "HealthCareActivity"}, {"text": "leprosy reactions", "type": "BiologicFunction"}, {"text": "person", "type": "PopulationGroup"}]}

Example input:
Sentence: RANKL and OPG levels were measured by ELISA .

Example answer:
{"entities": [{"text": "RANKL", "type": "Chemical"}, {"text": "OPG", "type": "Chemical"}, {"text": "ELISA", "type": "HealthCareActivity"}]}

Input:
Sentence: Lp ( a ) was measured by ELISA .

## Item MedMentions:test:954
Example input:
Sentence: Using the SimAlba model , it is possible to simulate the distributions of previously unknown variables at the small area level such as smoking , alcohol consumption , mental well - being , and obesity .

Example answer:
{"entities": [{"text": "simulate", "type": "ResearchActivity"}, {"text": "small area level", "type": "ResearchActivity"}, {"text": "mental well - being", "type": "Finding"}, {"text": "obesity", "type": "BiologicFunction"}]}

Example input:
Sentence: We characterized the genome - wide binding profile of BarR using chromatin immunoprecipation combined with high - throughput sequencing ( ChIP - seq ) .

Example answer:
{"entities": [{"text": "genome - wide binding profile", "type": "HealthCareActivity"}, {"text": "BarR", "type": "Chemical"}, {"text": "chromatin immunoprecipation", "type": "HealthCareActivity"}, {"text": "high - throughput sequencing", "type": "ResearchActivity"}, {"text": "ChIP - seq", "type": "ResearchActivity"}]}

Example input:
Sentence: LBBB was significantly associated with the presence of SF and AR ; within the LBBB group , 79 % had SF and 65 % had AR .

Example answer:
{"entities": [{"text": "LBBB", "type": "BiologicFunction"}, {"text": "SF", "type": "Finding"}]}

Example input:
Sentence: Levels of DSBs were estimated from the scoring of CAs visualized with telomere / centromere - fluorescence in situ hybridization ( TC - FISH ) .

Example answer:
{"entities": [{"text": "DSBs", "type": "BiologicFunction"}, {"text": "CAs", "type": "BiologicFunction"}, {"text": "telomere", "type": "AnatomicalStructure"}, {"text": "centromere", "type": "AnatomicalStructure"}, {"text": "fluorescence in situ hybridization", "type": "ResearchActivity"}, {"text": "TC - FISH", "type": "ResearchActivity"}]}

Example input:
Sentence: Research studies have shown that breast tumors are associated with systemic changes in levels of both serum protein biomarkers ( SPB ) and tumor associated autoantibodies ( TAAb ) .

Example answer:
{"entities": [{"text": "Research studies", "type": "ResearchActivity"}, {"text": "breast tumors", "type": "BiologicFunction"}, {"text": "serum protein biomarkers", "type": "ClinicalAttribute"}, {"text": "SPB", "type": "ClinicalAttribute"}, {"text": "tumor associated autoantibodies", "type": "Chemical"}, {"text": "TAAb", "type": "Chemical"}]}

Example input:
Sentence: When TAAb data was independently used , clinical sensitivity and specificity for detection of BC were 72 .

Example answer:
{"entities": [{"text": "TAAb", "type": "Chemical"}, {"text": "clinical sensitivity", "type": "ResearchActivity"}, {"text": "detection", "type": "Finding"}, {"text": "BC", "type": "BiologicFunction"}]}

Example input:
Sentence: When SPB data was independently used for modeling , clinical sensitivity and specificity for detection of BC were 74 . 7 % and 77 . 0 % , respectively .

Example answer:
{"entities": [{"text": "SPB", "type": "ClinicalAttribute"}, {"text": "modeling", "type": "ResearchActivity"}, {"text": "clinical sensitivity", "type": "ResearchActivity"}, {"text": "BC", "type": "BiologicFunction"}]}

Example input:
Sentence: This study evaluates these contributions using a retrospective cohort of pre - biopsy serum samples with known clinical outcomes collected from a single site , thus minimizing potential site - to - site variation and enabling direct assessment of SPB and TAAb contributions to identify BC .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "evaluates", "type": "HealthCareActivity"}, {"text": "retrospective cohort", "type": "ResearchActivity"}, {"text": "biopsy", "type": "HealthCareActivity"}, {"text": "serum samples", "type": "BodySubstance"}, {"text": "clinical outcomes", "type": "Finding"}, {"text": "site", "type": "SpatialConcept"}, {"text": "variation", "type": "Finding"}, {"text": "SPB", "type": "ClinicalAttribute"}, {"text": "TAAb", "type": "Chemical"}, {"text": "BC", "type": "BiologicFunction"}]}

Example input:
Sentence: from non - BC ( i . e . , BBD and ND ) using expression data from SPB alone , TAAb alone , and a combination of SPB and TAAb .

Example answer:
{"entities": [{"text": "BBD", "type": "BiologicFunction"}, {"text": "ND", "type": "Finding"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "SPB", "type": "ClinicalAttribute"}, {"text": "TAAb", "type": "Chemical"}]}

Example input:
Sentence: These data demonstrate the benefit of the integration of SPB and TAAb data and strongly support the further development of combinatorial proteomic approaches for detecting BC .

Example answer:
{"entities": [{"text": "SPB", "type": "ClinicalAttribute"}, {"text": "TAAb", "type": "Chemical"}, {"text": "BC", "type": "BiologicFunction"}]}

Input:
Sentence: However , the independent contribution of SPB and TAAb expression data for identifying BC relative to a combinatorial SPB and TAAb approach has not been fully investigated .

## Item MedMentions:test:800
Example input:
Sentence: Analyzing the morphological , physiological , and biochemical characteristics of this strain demonstrated that it was similar to Lactobacillus species , and molecular level amplification of the 16S rRNA gene showed that it belonged to Lactobacillus paraplantarum .

Example answer:
{"entities": [{"text": "morphological", "type": "SpatialConcept"}, {"text": "strain", "type": "Bacterium"}, {"text": "Lactobacillus species", "type": "Bacterium"}, {"text": "molecular level amplification", "type": "BiologicFunction"}, {"text": "16S rRNA", "type": "Chemical"}, {"text": "gene", "type": "AnatomicalStructure"}, {"text": "Lactobacillus paraplantarum", "type": "Bacterium"}]}

Example input:
Sentence: Differential phenotypic properties , together with the phylogenetic distinctiveness , revealed that strain KEM - 4 T is separated from recognized Altererythrobacter species .

Example answer:
{"entities": [{"text": "phenotypic properties", "type": "Finding"}, {"text": "Altererythrobacter species", "type": "Bacterium"}]}

Example input:
Sentence: Based on the morphological , physiological , biochemical and chemotaxonomic characters presented in this study , strain SYP - A7299 T represents a novel species of the genus Arthrobacter , for which the name Arthrobacter ginkgonis sp .

Example answer:
{"entities": [{"text": "morphological", "type": "SpatialConcept"}, {"text": "strain SYP - A7299 T", "type": "Bacterium"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Arthrobacter", "type": "Bacterium"}, {"text": "Arthrobacter ginkgonis sp .", "type": "Bacterium"}]}

Example input:
Sentence: On the basis of the data presented , strain KEM - 4 T is considered to represent a novel species of the genus Altererythrobacter , for which the name Altererythrobacter confluentis sp .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Altererythrobacter", "type": "Bacterium"}, {"text": "Altererythrobacter confluentis sp .", "type": "Bacterium"}]}

Example input:
Sentence: Phylogenetic tree based on 16S rRNA gene sequences indicated that strain EGI 6500337 T formed a distinct lineage in the cluster that comprised the genera Aurantimonas and Aureimonas in the family Aurantimonadaceae .

Example answer:
{"entities": [{"text": "16S rRNA", "type": "Chemical"}, {"text": "gene sequences", "type": "SpatialConcept"}, {"text": "strain EGI 6500337 T", "type": "Bacterium"}, {"text": "genera Aurantimonas", "type": "Bacterium"}, {"text": "Aureimonas", "type": "Bacterium"}, {"text": "family Aurantimonadaceae", "type": "Bacterium"}]}

Example input:
Sentence: Phylogenetic analysis based on 16S rRNA gene sequences showed that strain FA102 T formed a distinct evolutionary lineage within the family Marinifilaceae and its closest relative was Marinifilum fragile JCM 15579 T ( 93 .

Example answer:
{"entities": [{"text": "Phylogenetic analysis", "type": "ResearchActivity"}, {"text": "16S rRNA gene sequences", "type": "Chemical"}, {"text": "FA102 T", "type": "Bacterium"}, {"text": "evolutionary", "type": "BiologicFunction"}, {"text": "Marinifilaceae", "type": "Bacterium"}, {"text": "closest relative", "type": "Finding"}, {"text": "Marinifilum fragile JCM 15579 T", "type": "Bacterium"}]}

Example input:
Sentence: nov . , isolated from a spring A bacterial strain , designated STM - 7 T , was isolated from a spring in Taiwan and characterized using a polyphasic taxonomy approach .

Example answer:
{"entities": [{"text": "nov .", "type": "Bacterium"}, {"text": "Taiwan", "type": "SpatialConcept"}]}

Example input:
Sentence: The 16S rRNA gene sequence of strain EGI 6500337 T shared the highest similarities to those of Aurantimonas coralicida DSM 14790 T ( 97 . 15 % ) and Aurantimonas manganoxydans DSM 21871 T ( 97 . 15 % ) .

Example answer:
{"entities": [{"text": "16S rRNA", "type": "Chemical"}, {"text": "gene sequence", "type": "SpatialConcept"}, {"text": "strain EGI 6500337 T", "type": "Bacterium"}, {"text": "Aurantimonas coralicida DSM 14790 T", "type": "Bacterium"}, {"text": "Aurantimonas manganoxydans DSM 21871 T", "type": "Bacterium"}]}

Example input:
Sentence: Phylogenetic analyses based on 16S rRNA gene sequences indicated that strain SYP - A7299 T belongs to the genus Arthrobacter and is most closely related to Arthrobacter halodurans JSM 078085 T ( 97 . 4 % 16S rRNA gene sequence similarity ) .

Example answer:
{"entities": [{"text": "Phylogenetic analyses", "type": "ResearchActivity"}, {"text": "16S rRNA gene sequences", "type": "AnatomicalStructure"}, {"text": "strain SYP - A7299 T", "type": "Bacterium"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Arthrobacter", "type": "Bacterium"}, {"text": "Arthrobacter halodurans JSM 078085 T", "type": "Bacterium"}, {"text": "16S rRNA gene sequence", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The DNA - DNA hybridization value for strain STM - 7 T with Chitinibacter tainanensis S1 T was less than 47 % .

Example answer:
{"entities": [{"text": "DNA - DNA hybridization", "type": "ResearchActivity"}, {"text": "Chitinibacter tainanensis S1 T", "type": "Bacterium"}]}

Input:
Sentence: Phylogenetic analyses based on 16S rRNA gene sequences showed that strain STM - 7 T belonged to the genus Chitinibacter and was most closely related to Chitinibacter tainanensis S1 T with sequence similarity of 97 .

## Item MedMentions:test:1170
Example input:
Sentence: Using a short hairpin RNA strategy , we demonstrate here that the 2 mammalian RBPs , PUMILIO ( PUM ) 1 and PUM2 , members of the PUF family of posttranscriptional regulators , are essential for hematopoietic stem / progenitor cell ( HSPC ) proliferation and survival in vitro and in vivo upon reconstitution assays .

Example answer:
{"entities": [{"text": "short hairpin RNA", "type": "Chemical"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "RBPs", "type": "Chemical"}, {"text": "PUMILIO", "type": "Chemical"}, {"text": "PUM ) 1", "type": "Chemical"}, {"text": "PUM2", "type": "Chemical"}, {"text": "PUF family", "type": "Chemical"}, {"text": "posttranscriptional regulators", "type": "BiologicFunction"}, {"text": "hematopoietic stem / progenitor cell ( HSPC ) proliferation", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "reconstitution assays", "type": "HealthCareActivity"}]}

Example input:
Sentence: All patients were examined initially with POCUS by EPs and then with radiology - performed US ( RADUS ) by radiologists .

Example answer:
{"entities": [{"text": "POCUS", "type": "HealthCareActivity"}, {"text": "EPs", "type": "ProfessionalOrOccupationalGroup"}, {"text": "radiology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "US", "type": "HealthCareActivity"}, {"text": "RADUS", "type": "HealthCareActivity"}, {"text": "radiologists", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: A PPMV - 1 isolate , abbreviated as PPMV - 1 / QL - 01 / CH / 15 , was isolated from a great spotted woodpecker in the northwest region of China in 2015 .

Example answer:
{"entities": [{"text": "PPMV - 1", "type": "Virus"}, {"text": "isolate", "type": "Chemical"}, {"text": "PPMV - 1 / QL - 01 / CH / 15", "type": "Virus"}, {"text": "woodpecker", "type": "Eukaryote"}, {"text": "northwest region of China", "type": "SpatialConcept"}]}

Example input:
Sentence: Bacteriuria is a common finding in patients with symptomatic BPH in our setting .

Example answer:
{"entities": [{"text": "Bacteriuria", "type": "BiologicFunction"}, {"text": "finding", "type": "Finding"}, {"text": "BPH", "type": "BiologicFunction"}]}

Example input:
Sentence: pasteurianus isolates from dead ducklings collected in several natural outbreaks in China during 2010 - 2013 .

Example answer:
{"entities": [{"text": "pasteurianus", "type": "Bacterium"}, {"text": "dead", "type": "Finding"}, {"text": "ducklings", "type": "Eukaryote"}, {"text": "China", "type": "SpatialConcept"}]}

Example input:
Sentence: Given that purpura and subsequent possible postinflammatory hyperpigmentation ( PIH ) are occasionally unbearable in some patients , and several studies using the low nonpurpuragenic fluence were reported .

Example answer:
{"entities": [{"text": "purpura", "type": "BiologicFunction"}, {"text": "postinflammatory hyperpigmentation", "type": "BiologicFunction"}, {"text": "PIH", "type": "BiologicFunction"}, {"text": "nonpurpuragenic", "type": "Finding"}]}

Example input:
Sentence: pasteurianus is an under - recognized pathogen and zoonotic agent causing opportunistic infections in humans .

Example answer:
{"entities": [{"text": "pasteurianus", "type": "Bacterium"}, {"text": "zoonotic agent", "type": "Bacterium"}, {"text": "opportunistic infections", "type": "BiologicFunction"}, {"text": "humans", "type": "Eukaryote"}]}

Example input:
Sentence: Palmoplantar pustulosis - a cross - sectional analysis in Germany Palmoplantar pustulosis ( PPP ) is a recalcitrant chronic inflammatory skin disease .

Example answer:
{"entities": [{"text": "Palmoplantar pustulosis", "type": "BiologicFunction"}, {"text": "cross - sectional analysis", "type": "ResearchActivity"}, {"text": "Germany", "type": "SpatialConcept"}, {"text": "PPP", "type": "BiologicFunction"}, {"text": "inflammatory skin disease", "type": "BiologicFunction"}]}

Example input:
Sentence: purpureus MEIDOU 2012 from well - watered and water - stress treatments that were subjected to drought stress for 10 days .

Example answer:
{"entities": [{"text": "purpureus", "type": "Eukaryote"}, {"text": "stress", "type": "Finding"}]}

Example input:
Sentence: Purpura and PIH were not reported in all patients .

Example answer:
{"entities": [{"text": "Purpura", "type": "BiologicFunction"}, {"text": "PIH", "type": "BiologicFunction"}]}

Input:
Sentence: purpureus has been identified .

## Item MedMentions:test:967
Example input:
Sentence: PFTs averaged over all patients and parameters demonstrated small absolute declines , 5 . 7 % averaged PFT decline , at approximately 1 year of follow - up , but only the diffusing capacity of lung for carbon monoxide ( DLCO ) demonstrated a statistically significant decline ( 10 . 29 vs .

Example answer:
{"entities": [{"text": "PFTs", "type": "HealthCareActivity"}, {"text": "PFT", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: We investigated factors that can affect the MPV values of asthma patients , including infection , atopy , immunotherapy treatment , and severity of asthma exacerbation .

Example answer:
{"entities": [{"text": "MPV", "type": "HealthCareActivity"}, {"text": "asthma", "type": "BiologicFunction"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "atopy", "type": "BiologicFunction"}, {"text": "immunotherapy treatment", "type": "HealthCareActivity"}, {"text": "asthma exacerbation", "type": "BiologicFunction"}]}

Example input:
Sentence: On univariate analysis , variables associated with worse survival included : clinical stage IIIB ( p = 0 . 037 ) , planning target volume ( PTV ) over 450 cc ( p < 0 . 001 ) , heart V30 over 40 % ( p = -0 . 048 ) , and esophageal mean dose over 20 % ( p = 0 . 024 ) , V5 ( p = -0 . 015 ) , and V60 ( p = -0 . 011 ) .

Example answer:
{"entities": [{"text": "worse", "type": "Finding"}, {"text": "stage IIIB", "type": "BiologicFunction"}, {"text": "heart", "type": "AnatomicalStructure"}, {"text": "esophageal", "type": "SpatialConcept"}]}

Example input:
Sentence: On average , a 1μg / m ( 3 ) increase in PM10 was associated with cumulative increases of 0 . 26893 , 0 . 30437 , and 0 . 21924 YLL for non - accidental , respiratory , and cardiovascular mortality , respectively , referring to 20μg / m ( 3 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Despite the latter finding , both major vascular complications and major bleeding at 30 days were significantly lower in the RM group compared to the control group ( 4 . 3 % vs .

Example answer:
{"entities": [{"text": "bleeding", "type": "BiologicFunction"}]}

Example input:
Sentence: During a median follow - up of 46 months , patients in the upper tertile of changes in peak V̇O2 ( ≥13 . 0 % ) , compared with those in the lower tertile ( < 1 . 0 % ) , had lower rates of the composite of all - cause death or HF hospitalization ( 37 . 9 % vs .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "peak V̇O2", "type": "Finding"}, {"text": "death", "type": "BiologicFunction"}, {"text": "HF", "type": "BiologicFunction"}, {"text": "hospitalization", "type": "HealthCareActivity"}]}

Example input:
Sentence: Therefore , we developed the following recommendations for the pediatric PMV definition : ≥ 21 consecutive days ( after 37 weeks postmenstrual age ) of ventilation for ≥ 6 h / d considering invasive ventilation and NIV and including short interruptions ( < 48 h ) of ventilation during the weaning process as the same episode of ventilation .

Example answer:
{"entities": [{"text": "PMV", "type": "HealthCareActivity"}, {"text": "definition", "type": "IntellectualProduct"}, {"text": "ventilation", "type": "BiologicFunction"}, {"text": "invasive", "type": "HealthCareActivity"}, {"text": "NIV", "type": "HealthCareActivity"}, {"text": "weaning", "type": "Finding"}]}

Example input:
Sentence: They also experienced significantly more exacerbations in the previous year ( 0 . 19 vs 0 .

Example answer:
{"entities": [{"text": "exacerbations", "type": "Finding"}]}

Example input:
Sentence: Compared with those without polycythemia , the polycythemia group had significantly lower forced expiratory volume in one second ( FEV1 ) level ( 0 . 9±0 .

Example answer:
{"entities": [{"text": "polycythemia", "type": "BiologicFunction"}, {"text": "forced expiratory volume in one second ( FEV1 ) level", "type": "HealthCareActivity"}]}

Example input:
Sentence: We evaluated the mean platelet volume ( MPV ) , used as a marker of platelet activation , in asthmatic patients during asymptomatic periods and exacerbations compared to healthy controls to determine whether MPV can be used as an indicator of inflammation .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "mean platelet volume", "type": "HealthCareActivity"}, {"text": "MPV", "type": "HealthCareActivity"}, {"text": "marker", "type": "ClinicalAttribute"}, {"text": "platelet activation", "type": "BiologicFunction"}, {"text": "asthmatic", "type": "BiologicFunction"}, {"text": "asymptomatic", "type": "Finding"}, {"text": "exacerbations", "type": "Finding"}, {"text": "indicator", "type": "Chemical"}, {"text": "inflammation", "type": "BiologicFunction"}]}

Input:
Sentence: Mean MPV values in the exacerbation period , the healthy period , and in the control group were 8 . 1 ±0 . 8 fl , 8 . 1 ±1 . 06 fl , and 8 .

## Item MedMentions:test:788
Example input:
Sentence: The newly identified miR - 376c / BMI1 pathway provides an insight into cervical cancer progression and may represent a novel therapeutic target .

Example answer:
{"entities": [{"text": "miR - 376c", "type": "Chemical"}, {"text": "BMI1", "type": "AnatomicalStructure"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "cervical cancer", "type": "BiologicFunction"}, {"text": "progression", "type": "BiologicFunction"}]}

Example input:
Sentence: Our results described that miR - 424 - 5p - SMAD7 pathway contributed to ESCC invasion and metastasis and up - regulation of miR - 424 - 5p perhaps provided a strategy for preventing tumor invasion , metastasis .

Example answer:
{"entities": [{"text": "miR - 424 - 5p", "type": "AnatomicalStructure"}, {"text": "SMAD7", "type": "AnatomicalStructure"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "ESCC", "type": "BiologicFunction"}, {"text": "invasion", "type": "BiologicFunction"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "up - regulation", "type": "BiologicFunction"}, {"text": "tumor invasion", "type": "Finding"}]}

Example input:
Sentence: We generated a human embryonic stem cell ( hESC ) line carrying a naturally occurring mutation of MYPBC3 ( c . 2905 +1 G > A ) to study HCM pathogenesis during cardiac differentiation .

Example answer:
{"entities": [{"text": "mutation", "type": "BiologicFunction"}, {"text": "MYPBC3", "type": "AnatomicalStructure"}, {"text": "c . 2905 +1 G > A", "type": "BiologicFunction"}, {"text": "HCM", "type": "BiologicFunction"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "cardiac differentiation", "type": "BiologicFunction"}]}

Example input:
Sentence: Several critical hub genes were disclosed , such as RPS2 , MMP1 , MMP11 and FAM83H .

Example answer:
{"entities": [{"text": "hub genes", "type": "AnatomicalStructure"}, {"text": "RPS2", "type": "AnatomicalStructure"}, {"text": "MMP1", "type": "AnatomicalStructure"}, {"text": "MMP11", "type": "AnatomicalStructure"}, {"text": "FAM83H", "type": "AnatomicalStructure"}]}

Example input:
Sentence: MiR - 132 was effective in both impeding cell growth and boosting apoptosis in HCC cell lines .

Example answer:
{"entities": [{"text": "MiR - 132", "type": "Chemical"}, {"text": "cell growth", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}]}

Example input:
Sentence: An Encapsulation of Gene Signatures for Hepatocellular Carcinoma , MicroRNA - 132 Predicted Target Genes and the Corresponding Overlaps Previous studies have demonstrated that microRNA - 132 plays a vital part in and is actively associated with several cancers , with its tumor - suppressive role in hepatocellular carcinoma confirmed .

Example answer:
{"entities": [{"text": "Hepatocellular Carcinoma", "type": "BiologicFunction"}, {"text": "MicroRNA - 132", "type": "Chemical"}, {"text": "Target Genes", "type": "AnatomicalStructure"}, {"text": "Corresponding Overlaps", "type": "SpatialConcept"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "microRNA - 132", "type": "Chemical"}, {"text": "cancers", "type": "BiologicFunction"}, {"text": "tumor - suppressive role", "type": "BiologicFunction"}, {"text": "hepatocellular carcinoma", "type": "BiologicFunction"}]}

Example input:
Sentence: A total of fifty - nine genes were obtained from the analytical integration , which were considered to be both HCC - and miR - 132 - related .

Example answer:
{"entities": [{"text": "genes", "type": "AnatomicalStructure"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "miR - 132", "type": "Chemical"}]}

Example input:
Sentence: The tumor - suppressive role of miR - 132 in HCC has been further confirmed by in vitro experiments .

Example answer:
{"entities": [{"text": "tumor - suppressive role", "type": "BiologicFunction"}, {"text": "miR - 132", "type": "Chemical"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "experiments", "type": "ResearchActivity"}]}

Example input:
Sentence: Gene signatures in the study identified the potential molecular mechanisms of HCC , miR - 132 and their established associations , which might be effective for diagnosis , individualized treatments and prognosis of HCC patients .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "miR - 132", "type": "Chemical"}, {"text": "diagnosis", "type": "ResearchActivity"}, {"text": "treatments", "type": "HealthCareActivity"}, {"text": "prognosis", "type": "HealthCareActivity"}]}

Example input:
Sentence: Various assays were performed to explore the role and cellular functions of miR - 132 in HCC and a successive panel of tasks was completed , including NLP analysis , miR - 132 target genes prediction , comprehensive analyses ( gene ontology analysis , pathway analysis , network analysis and connectivity analysis ) , and analytical integration .

Example answer:
{"entities": [{"text": "assays", "type": "HealthCareActivity"}, {"text": "cellular functions", "type": "BiologicFunction"}, {"text": "miR - 132", "type": "Chemical"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "successive panel", "type": "ResearchActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "target genes", "type": "AnatomicalStructure"}, {"text": "analyses", "type": "ResearchActivity"}, {"text": "gene ontology analysis", "type": "IntellectualProduct"}, {"text": "pathway analysis", "type": "IntellectualProduct"}, {"text": "network analysis", "type": "IntellectualProduct"}]}

Input:
Sentence: Later , HCC - related and miR - 132 - related potential targets , pathways , networks and highlighted hub genes were revealed as well as those of the overlapped section .

## Item MedMentions:test:939
Example input:
Sentence: Survival improved with the evolution of the technique , although this was not statistically significant due to the overall low rate of further revision .

Example answer:
{"entities": [{"text": "revision", "type": "HealthCareActivity"}]}

Example input:
Sentence: , the study examined whether the use of heterogeneous cluster grouping in reflective writing for medical humanities literature acquisition could have positive effects on medical university students in terms of empathy , critical thinking , and reflective writing .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "examined", "type": "Finding"}, {"text": "medical university", "type": "Organization"}, {"text": "students", "type": "PopulationGroup"}, {"text": "critical thinking", "type": "BiologicFunction"}]}

Example input:
Sentence: The key benefit of the pdf article intervention was raising doctors ' reflection on limitations in their communication skills , whereas e - learning was more effective in changing their perception of older patients ' proactive attitude , especially among GPs working in privately owned facilities and having a greater number of assigned patients .

Example answer:
{"entities": [{"text": "pdf article", "type": "IntellectualProduct"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "doctors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "older", "type": "PopulationGroup"}, {"text": "GPs", "type": "ProfessionalOrOccupationalGroup"}, {"text": "privately owned facilities", "type": "Organization"}]}

Example input:
Sentence: There is great variance in the propensity to generalize as well as the speed of extinction learning when these novel movements are not followed by pain .

Example answer:
{"entities": [{"text": "generalize", "type": "BiologicFunction"}, {"text": "extinction learning", "type": "BiologicFunction"}, {"text": "movements", "type": "BiologicFunction"}, {"text": "pain", "type": "Finding"}]}

Example input:
Sentence: Effective feedback can become part of the learning cycle that is not only a learning opportunity for the student but can also be used to inform the teacher and ongoing curriculum development .

Example answer:
{"entities": [{"text": "feedback", "type": "BiologicFunction"}, {"text": "part of", "type": "SpatialConcept"}, {"text": "learning", "type": "BiologicFunction"}, {"text": "student", "type": "PopulationGroup"}, {"text": "teacher", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Based on student evaluations presented in this study , this method provided feedback in a manner that engaged students , uncovered underlying misconceptions , facilitated peer discussion , and provided opportunity for new instruction while allowing the lecturer to recognize common gaps in knowledge and inform ongoing curriculum development .

Example answer:
{"entities": [{"text": "student", "type": "PopulationGroup"}, {"text": "evaluations", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "feedback", "type": "BiologicFunction"}, {"text": "students", "type": "PopulationGroup"}, {"text": "underlying misconceptions", "type": "Finding"}, {"text": "peer", "type": "PopulationGroup"}, {"text": "recognize", "type": "BiologicFunction"}, {"text": "gaps", "type": "SpatialConcept"}, {"text": "knowledge", "type": "IntellectualProduct"}]}

Example input:
Sentence: The present study describes a method that was used to provide formative task - related feedback to a large cohort of first - year physiology and anatomy students .

Example answer:
{"entities": [{"text": "present", "type": "Finding"}, {"text": "study", "type": "ResearchActivity"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "physiology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "anatomy", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "students", "type": "PopulationGroup"}]}

Example input:
Sentence: Feedback is considered particularly important during the first year of university and can even be viewed as a retention strategy that can help attenuate student performance anxieties and solidify perceptions of academic support .

Example answer:
{"entities": [{"text": "Feedback", "type": "BiologicFunction"}, {"text": "university", "type": "Organization"}, {"text": "student", "type": "PopulationGroup"}, {"text": "performance anxieties", "type": "BiologicFunction"}, {"text": "perceptions", "type": "BiologicFunction"}]}

Example input:
Sentence: A method of providing engaging formative feedback to large cohort first - year physiology and anatomy students A growing body of evidence demonstrates a critical role for effective , meaningful feedback to enhance student learning .

Example answer:
{"entities": [{"text": "cohort", "type": "PopulationGroup"}, {"text": "physiology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "anatomy", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "students", "type": "PopulationGroup"}, {"text": "feedback", "type": "BiologicFunction"}, {"text": "student", "type": "PopulationGroup"}, {"text": "learning", "type": "BiologicFunction"}]}

Example input:
Sentence: Unfortunately , the provision of individualized , timely feedback can be particularly challenging in first - year courses as they tend to be large and diverse cohort classes that pose challenges of time and logistics .

Example answer:
{"entities": [{"text": "feedback", "type": "BiologicFunction"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "classes", "type": "IntellectualProduct"}]}

Input:
Sentence: Various forms of generic feedback can provide rapid and cost - effect feedback to large cohorts but may be of limited benefit to students other than signaling weaknesses in knowledge .

## Item MedMentions:test:1274
Example input:
Sentence: 02 ( mean ± SE ) and root - mean - squared - error of 7 . 6 ± 0 . 5 mmHg after a best - case calibration .

Example answer:
{"entities": []}

Example input:
Sentence: There was a mean ( ± standard deviation ) change in weight of -1 .

Example answer:
{"entities": []}

Example input:
Sentence: The mean duration of follow - up ( ± SD ) was 24 .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: 0 ± 0 .

Example answer:
{"entities": []}

Example input:
Sentence: The mean ( ±SD ) PWV was 2 .

Example answer:
{"entities": []}

Example input:
Sentence: 1 ( SD = 12 . 8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Significantly higher mean ± s .

Example answer:
{"entities": []}

Example input:
Sentence: 08 ( mean ± standard deviation ) ,

Example answer:
{"entities": []}

Example input:
Sentence: Mean ± SD GRV was 18 .

Example answer:
{"entities": [{"text": "GRV", "type": "ClinicalAttribute"}]}

Example input:
Sentence: 7 ( mean ± SD ) .

Example answer:
{"entities": []}

Input:
Sentence: The data are presented as means ± SD .

## Item MedMentions:test:853
Example input:
Sentence: The present work comprehensively investigates the efficacy of these ions for assigning the C - 5 stereochemistry of the reducing end uronic acid in 33 HS tetrasaccharides .

Example answer:
{"entities": [{"text": "ions", "type": "Chemical"}, {"text": "C - 5 stereochemistry", "type": "SpatialConcept"}, {"text": "uronic acid", "type": "Chemical"}, {"text": "HS tetrasaccharides", "type": "Chemical"}]}

Example input:
Sentence: Implementation of infrared and Raman modalities for glycosaminoglycan characterization in complex systems Glycosaminoglycans ( GAGs ) are natural , linear and negatively charged heteropolysaccharides which are incident in every mammalian tissue .

Example answer:
{"entities": [{"text": "infrared", "type": "HealthCareActivity"}, {"text": "Raman", "type": "HealthCareActivity"}, {"text": "glycosaminoglycan", "type": "Chemical"}, {"text": "characterization", "type": "IntellectualProduct"}, {"text": "Glycosaminoglycans", "type": "Chemical"}, {"text": "GAGs", "type": "Chemical"}, {"text": "linear", "type": "SpatialConcept"}, {"text": "negatively charged", "type": "Chemical"}, {"text": "heteropolysaccharides", "type": "Chemical"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The strain 's growth patterns under various concentrations of H2 O2 and its scavenging properties towards hydroxyl radical ( 64 . 85 % ) and DPPH ( 84 . 97 % ) were also interesting properties .

Example answer:
{"entities": [{"text": "strain 's", "type": "Bacterium"}, {"text": "growth patterns", "type": "Finding"}, {"text": "H2 O2", "type": "Chemical"}, {"text": "scavenging properties", "type": "BiologicFunction"}, {"text": "hydroxyl radical", "type": "Chemical"}, {"text": "DPPH", "type": "Chemical"}]}

Example input:
Sentence: FTIR confirmed the involvement of phosphoric group of sTPP with amine groups of chitosan and also role of hydrogen bonding involved in the preparation of MTXCHNP and DEXCHNP .

Example answer:
{"entities": [{"text": "FTIR", "type": "ResearchActivity"}, {"text": "sTPP", "type": "Chemical"}, {"text": "amine groups", "type": "Chemical"}, {"text": "chitosan", "type": "Chemical"}]}

Example input:
Sentence: A recent study using electron detachment dissociation and principal component analysis revealed a series of ions that correlate with GlcA versus IdoA for a set of 2 - O - sulfo HS tetrasaccharide standards .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "electron detachment dissociation", "type": "ResearchActivity"}, {"text": "ions", "type": "Chemical"}, {"text": "GlcA", "type": "Chemical"}, {"text": "IdoA", "type": "Chemical"}, {"text": "2 - O - sulfo HS tetrasaccharide", "type": "Chemical"}]}

Example input:
Sentence: Complete structural elucidation of glycosaminoglycans necessitates the unambiguous assignments of sulfo modifications and the C - 5 uronic acid stereochemistry .

Example answer:
{"entities": [{"text": "glycosaminoglycans", "type": "Chemical"}, {"text": "sulfo", "type": "Chemical"}, {"text": "C - 5 uronic acid", "type": "Chemical"}, {"text": "stereochemistry", "type": "SpatialConcept"}]}

Example input:
Sentence: The existence of α - and β - glycosidic linkages between the sugar units was confirmed by FTIR and NMR spectra .

Example answer:
{"entities": [{"text": "sugar", "type": "Chemical"}, {"text": "FTIR", "type": "ResearchActivity"}, {"text": "NMR spectra", "type": "HealthCareActivity"}]}

Example input:
Sentence: By characterization using LC - MS / MS analysis , all components of a series of PEs were elucidated to be the 12 - deoxy - 16 - hydroxyphorbol esters composed of isomeric form of dicarboxylic groups with same m / z value of 380 .

Example answer:
{"entities": [{"text": "PEs", "type": "Chemical"}]}

Example input:
Sentence: The previously observed diagnostic ions are generally not observed with 2 - O - sulfo uronic acids or for more highly sulfated heparan sulfate tetrasaccharides .

Example answer:
{"entities": [{"text": "ions", "type": "Chemical"}, {"text": "2 - O - sulfo uronic acids", "type": "Chemical"}, {"text": "sulfated heparan sulfate tetrasaccharides", "type": "Chemical"}]}

Example input:
Sentence: Single Stage Tandem Mass Spectrometry Assignment of the C - 5 Uronic Acid Stereochemistry in Heparan Sulfate Tetrasaccharides using Electron Detachment Dissociation The analysis of heparan sulfate ( HS ) glycosaminoglycans presents many challenges , due to the high degree of structural heterogeneity arising from their non - template biosynthesis .

Example answer:
{"entities": [{"text": "Single Stage Tandem Mass Spectrometry", "type": "ResearchActivity"}, {"text": "C - 5 Uronic Acid", "type": "Chemical"}, {"text": "Stereochemistry", "type": "SpatialConcept"}, {"text": "Heparan Sulfate Tetrasaccharides", "type": "Chemical"}, {"text": "Electron Detachment Dissociation", "type": "ResearchActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "heparan sulfate ( HS ) glycosaminoglycans", "type": "Chemical"}, {"text": "structural", "type": "SpatialConcept"}]}

Input:
Sentence: The results of infrared characterization indicated the presence of hydroxyl groups , sulfate , uronic acid and glycosidic linkages in all SP fractions spectrums .

## Item MedMentions:test:765
Example input:
Sentence: We performed RNA - seq analysis by using two pipelines , one with and one without a reference sequence , to obtain transcriptome data .

Example answer:
{"entities": [{"text": "RNA - seq analysis", "type": "HealthCareActivity"}, {"text": "transcriptome", "type": "SpatialConcept"}]}

Example input:
Sentence: Testing set and two validation sets comprising paired tumor and adjacent mucosa tissue samples from 151 patients were used for transcript profiling of 15 5 - FU pathway genes by quantitative real - time PCR and DNA methylation profiling by high resolution melting analysis .

Example answer:
{"entities": [{"text": "Testing set", "type": "IntellectualProduct"}, {"text": "validation sets", "type": "IntellectualProduct"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "adjacent", "type": "SpatialConcept"}, {"text": "mucosa tissue", "type": "AnatomicalStructure"}, {"text": "transcript", "type": "Chemical"}, {"text": "profiling", "type": "ResearchActivity"}, {"text": "5 - FU", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "quantitative real - time PCR", "type": "ResearchActivity"}, {"text": "DNA methylation profiling", "type": "ResearchActivity"}]}

Example input:
Sentence: High - throughput sequencing of two populations of extracellular vesicles provides an mRNA signature that can be detected in the circulation of breast cancer patients Extracellular vesicles ( EVs ) contain a wide range of RNA types with a reported prevalence of non - coding RNA .

Example answer:
{"entities": [{"text": "High - throughput sequencing", "type": "ResearchActivity"}, {"text": "extracellular vesicles", "type": "AnatomicalStructure"}, {"text": "mRNA", "type": "Chemical"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "Extracellular vesicles", "type": "AnatomicalStructure"}, {"text": "EVs", "type": "AnatomicalStructure"}, {"text": "RNA", "type": "Chemical"}, {"text": "non - coding RNA", "type": "Chemical"}]}

Example input:
Sentence: RNA - seq analysis showed that hundreds of genes were upregulated in M2c macrophages compared to the M0 control , with thousands of alternative splicing events .

Example answer:
{"entities": [{"text": "RNA - seq analysis", "type": "HealthCareActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "macrophages", "type": "AnatomicalStructure"}, {"text": "alternative splicing", "type": "BiologicFunction"}]}

Example input:
Sentence: CSCs were then isolated from the tumors and their microRNA ( miRNA ) expression was analyzed by semi - quantitative polymerase chain reaction .

Example answer:
{"entities": [{"text": "CSCs", "type": "AnatomicalStructure"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "microRNA", "type": "Chemical"}, {"text": "miRNA", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "semi - quantitative polymerase chain reaction", "type": "HealthCareActivity"}]}

Example input:
Sentence: Inferred copy number variations from the single - cell RNA - seq data separate carcinoma cells from non - cancer cells .

Example answer:
{"entities": [{"text": "Inferred copy number variations", "type": "SpatialConcept"}, {"text": "single - cell RNA - seq", "type": "SpatialConcept"}, {"text": "carcinoma cells", "type": "AnatomicalStructure"}, {"text": "non - cancer cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Transcriptome profiling by RNA - sequencing determined the genome -wide patterns of expression of virulence factors both in vitro ( potato dextrose agar or medium amended with grape wood as substrate ) and in planta .

Example answer:
{"entities": [{"text": "Transcriptome profiling", "type": "HealthCareActivity"}, {"text": "RNA - sequencing", "type": "HealthCareActivity"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "virulence factors", "type": "Chemical"}, {"text": "potato", "type": "Food"}, {"text": "dextrose agar", "type": "Chemical"}, {"text": "medium", "type": "Chemical"}, {"text": "grape", "type": "Food"}, {"text": "planta", "type": "Eukaryote"}]}

Example input:
Sentence: We characterized the genome - wide binding profile of BarR using chromatin immunoprecipation combined with high - throughput sequencing ( ChIP - seq ) .

Example answer:
{"entities": [{"text": "genome - wide binding profile", "type": "HealthCareActivity"}, {"text": "BarR", "type": "Chemical"}, {"text": "chromatin immunoprecipation", "type": "HealthCareActivity"}, {"text": "high - throughput sequencing", "type": "ResearchActivity"}, {"text": "ChIP - seq", "type": "ResearchActivity"}]}

Example input:
Sentence: Single - cell RNA - seq enables comprehensive tumour and immune cell profiling in primary breast cancer Single - cell transcriptome profiling of tumour tissue isolates allows the characterization of heterogeneous tumour cells along with neighbouring stromal and immune cells .

Example answer:
{"entities": [{"text": "Single - cell RNA - seq", "type": "SpatialConcept"}, {"text": "tumour", "type": "BiologicFunction"}, {"text": "immune cell profiling", "type": "HealthCareActivity"}, {"text": "primary breast cancer", "type": "BiologicFunction"}, {"text": "Single - cell transcriptome profiling", "type": "HealthCareActivity"}, {"text": "tumour tissue isolates", "type": "AnatomicalStructure"}, {"text": "tumour cells", "type": "AnatomicalStructure"}, {"text": "stromal", "type": "AnatomicalStructure"}, {"text": "immune cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: RNA - seq data of READ were downloaded from The Cancer Genome Atlas ( TCGA ) database .

Example answer:
{"entities": [{"text": "RNA - seq", "type": "SpatialConcept"}, {"text": "READ", "type": "BiologicFunction"}, {"text": "The Cancer Genome Atlas", "type": "ResearchActivity"}, {"text": "TCGA", "type": "ResearchActivity"}, {"text": "database", "type": "IntellectualProduct"}]}

Input:
Sentence: Bioinformatic analysis of RNA - seq data unveiled critical genes in rectal adenocarcinoma RNA - seq data of rectal adenocarcinoma ( READ ) were analyzed with bioinformatics tools to unveil potential biomarkers in the disease .

## Item MedMentions:test:1024
Example input:
Sentence: Statistically significant correlations were found only in MB between parameters HPV - p53 , p53 - pRb and p53 - p16 .

Example answer:
{"entities": [{"text": "parameters", "type": "Finding"}, {"text": "HPV", "type": "Virus"}, {"text": "p53", "type": "Chemical"}, {"text": "pRb", "type": "Chemical"}, {"text": "p16", "type": "Chemical"}]}

Example input:
Sentence: The molecular mechanisms associated with this disease have been investigated by transcriptome sequencing , but changes in protein abundance have not been investigated with isobaric tags for relative and absolute quantitation .

Example answer:
{"entities": [{"text": "molecular mechanisms", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "transcriptome sequencing", "type": "HealthCareActivity"}, {"text": "protein", "type": "Chemical"}, {"text": "isobaric tags for relative and absolute quantitation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Quantitative real - time PCR analysis demonstrated that 5 of the 13 chloroplast proteins ATPF , PSAA , PSAB , PSBB and RBL in TP were higher abundance compared with those in DP .

Example answer:
{"entities": [{"text": "Quantitative real - time PCR analysis", "type": "ResearchActivity"}, {"text": "chloroplast proteins", "type": "Chemical"}, {"text": "ATPF", "type": "Chemical"}, {"text": "PSAA", "type": "Chemical"}, {"text": "PSAB", "type": "Chemical"}, {"text": "PSBB", "type": "Chemical"}, {"text": "RBL", "type": "Chemical"}, {"text": "TP", "type": "BiologicFunction"}]}

Example input:
Sentence: A total of 76 proteins were successfully identified using matrix - assisted laser desorption / ionization time - of - flight mass spectrometry / mass spectrometry ( MALDI - TOF / MS / MS ) .

Example answer:
{"entities": [{"text": "proteins", "type": "Chemical"}, {"text": "matrix - assisted laser desorption / ionization time - of - flight mass spectrometry", "type": "ResearchActivity"}, {"text": "mass spectrometry", "type": "HealthCareActivity"}, {"text": "MALDI - TOF / MS", "type": "ResearchActivity"}, {"text": "MS", "type": "HealthCareActivity"}]}

Example input:
Sentence: Also , correlation analysis revealed a significant correlation between C - reactive protein ( CRP ) and N / L ( P = 0 . 002 ; r = 0 . 461 ) .

Example answer:
{"entities": [{"text": "correlation analysis", "type": "ResearchActivity"}, {"text": "C - reactive protein", "type": "Chemical"}, {"text": "CRP", "type": "Chemical"}, {"text": "N", "type": "AnatomicalStructure"}, {"text": "L", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Proteins displaying greater than threefold changes ( > log2 1 . 59 ) at 1 - hour CPB relative to the initiation of CPB ( 26 down - regulated and 22 up - regulated ) were selected for further analysis .

Example answer:
{"entities": [{"text": "Proteins", "type": "Chemical"}, {"text": "CPB", "type": "HealthCareActivity"}, {"text": "down - regulated", "type": "BiologicFunction"}, {"text": "up - regulated", "type": "BiologicFunction"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: The 2D - LC - MS / MS analysis identified 1324 proteins in the two pools , of which 744 were quantifiable .

Example answer:
{"entities": [{"text": "2D - LC - MS", "type": "HealthCareActivity"}, {"text": "MS", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "pools", "type": "ClinicalAttribute"}]}

Example input:
Sentence: We provided a new high confidence protein complex prediction method supported by functional studies and literature mining .

Example answer:
{"entities": [{"text": "protein complex", "type": "Chemical"}, {"text": "literature", "type": "IntellectualProduct"}]}

Example input:
Sentence: A total of 2 , 051 proteins were obtained , 879 of which were found to be differentially abundant in pairwise comparisons between the sample groups .

Example answer:
{"entities": [{"text": "proteins", "type": "Chemical"}]}

Example input:
Sentence: The SWATH approach provided quantitation for 730 proteins , 552 of which overlapped with the common population from the 2D - IDA results .

Example answer:
{"entities": [{"text": "SWATH approach", "type": "HealthCareActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "2D - IDA", "type": "IntellectualProduct"}]}

Input:
Sentence: Intensity correlation filtering between the two methods gave 475 proteins for biological interpretation .

## Item MedMentions:test:796
Example input:
Sentence: By contrast , in neurons co - expressing MagR and channelrhodopin , optical but not MS increased calcium influx in hippocampal neurons .

Example answer:
{"entities": [{"text": "neurons", "type": "AnatomicalStructure"}, {"text": "co - expressing", "type": "BiologicFunction"}, {"text": "MagR", "type": "Chemical"}, {"text": "channelrhodopin", "type": "Chemical"}, {"text": "optical", "type": "HealthCareActivity"}, {"text": "MS", "type": "HealthCareActivity"}, {"text": "calcium influx", "type": "BiologicFunction"}, {"text": "hippocampal", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Among these targets , calcium signaling mechanisms are critically dependent on the developmental stage and their full expression is a hallmark of the mature , functional neuron .

Example answer:
{"entities": [{"text": "calcium signaling", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "neuron", "type": "AnatomicalStructure"}]}

Example input:
Sentence: This was shown by real - time monitoring of intracellular Ca ( 2 + ) signaling in neurotypic cells growing on the impregnated polymer surface .

Example answer:
{"entities": [{"text": "real - time monitoring", "type": "ResearchActivity"}, {"text": "intracellular Ca ( 2 + ) signaling", "type": "BiologicFunction"}, {"text": "neurotypic cells", "type": "AnatomicalStructure"}, {"text": "polymer", "type": "Chemical"}, {"text": "surface", "type": "SpatialConcept"}]}

Example input:
Sentence: REST levels affect the functional expression of voltage dependent calcium channels and the migratory activity in immortalized GnRH neurons The repressor element - 1 silencing transcription factor ( REST ) has emerged as a key controller of neuronal differentiation and has been shown to play a critical role in the expression of the neuronal phenotype ; however , much has still to be learned about its role at specific developmental stages and about the functional targets affected .

Example answer:
{"entities": [{"text": "REST", "type": "AnatomicalStructure"}, {"text": "affect", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "voltage dependent calcium channels", "type": "Chemical"}, {"text": "immortalized", "type": "ResearchActivity"}, {"text": "GnRH", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "repressor element - 1 silencing transcription factor", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Secreted Ectodomain of Sialic Acid - Binding Ig - Like Lectin - 9 and Monocyte Chemoattractant Protein - 1 Synergistically Regenerate Transected Rat Peripheral Nerves by Altering Macrophage Polarity Peripheral nerves ( PNs ) exhibit remarkable self - repairing reparative activity after a simple crush or cut injury .

Example answer:
{"entities": [{"text": "Secreted", "type": "BiologicFunction"}, {"text": "Ectodomain", "type": "SpatialConcept"}, {"text": "Sialic Acid - Binding Ig - Like Lectin - 9", "type": "Chemical"}, {"text": "Monocyte Chemoattractant Protein - 1", "type": "Chemical"}, {"text": "Rat", "type": "Eukaryote"}, {"text": "Peripheral Nerves", "type": "AnatomicalStructure"}, {"text": "Macrophage", "type": "AnatomicalStructure"}, {"text": "Polarity", "type": "SpatialConcept"}, {"text": "Peripheral nerves", "type": "AnatomicalStructure"}, {"text": "PNs", "type": "AnatomicalStructure"}, {"text": "repairing", "type": "BiologicFunction"}, {"text": "reparative activity", "type": "BiologicFunction"}, {"text": "crush", "type": "HealthCareActivity"}, {"text": "cut injury", "type": "HealthCareActivity"}]}

Example input:
Sentence: The re - establishment of Ca ( 2 + ) distribution and intensity were correlated with the functional recovery of muscle in ESN rats .

Example answer:
{"entities": [{"text": "Ca ( 2 + )", "type": "Chemical"}, {"text": "distribution", "type": "BiologicFunction"}, {"text": "functional recovery", "type": "Finding"}, {"text": "muscle", "type": "AnatomicalStructure"}, {"text": "ESN", "type": "HealthCareActivity"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: 1 channels after ESN at the nerve terminals corresponded with changes in the Ca ( 2 + ) distribution .

Example answer:
{"entities": [{"text": "1 channels", "type": "Chemical"}, {"text": "ESN", "type": "HealthCareActivity"}, {"text": "nerve terminals", "type": "AnatomicalStructure"}, {"text": "Ca ( 2 + )", "type": "Chemical"}, {"text": "distribution", "type": "BiologicFunction"}]}

Example input:
Sentence: We show for the first time that functional voltage - dependent calcium channels are expressed in wild type GN11 cells ; down - regulation of REST by a silencing approach shifts these cells towards a more differentiated phenotype , increasing the functional expression of P / Q - type channels and reducing their migratory potential .

Example answer:
{"entities": [{"text": "voltage - dependent calcium channels", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "wild type", "type": "AnatomicalStructure"}, {"text": "GN11 cells", "type": "AnatomicalStructure"}, {"text": "down - regulation", "type": "BiologicFunction"}, {"text": "REST", "type": "AnatomicalStructure"}, {"text": "silencing", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "P", "type": "Chemical"}, {"text": "Q - type channels", "type": "Chemical"}]}

Example input:
Sentence: 1 channels and calcium ions in nerve terminals following end - to - side neurorrhaphy : ionic imaging analysis by TOF - SIMS The P / Q - type voltage - dependent calcium channel ( Cav2 . 1 ) in the presynaptic membranes of motor nerve terminals plays an important role in regulating Ca ( 2 + ) transport , resulting in transmitter release within the nervous system .

Example answer:
{"entities": [{"text": "1 channels", "type": "Chemical"}, {"text": "calcium ions", "type": "Chemical"}, {"text": "nerve terminals", "type": "AnatomicalStructure"}, {"text": "end - to - side neurorrhaphy", "type": "HealthCareActivity"}, {"text": "ionic imaging analysis", "type": "HealthCareActivity"}, {"text": "P / Q - type voltage - dependent calcium channel", "type": "Chemical"}, {"text": "Cav2 . 1", "type": "Chemical"}, {"text": "presynaptic membranes", "type": "AnatomicalStructure"}, {"text": "motor nerve", "type": "AnatomicalStructure"}, {"text": "terminals", "type": "AnatomicalStructure"}, {"text": "regulating Ca ( 2 + ) transport", "type": "BiologicFunction"}, {"text": "transmitter", "type": "Chemical"}, {"text": "nervous system", "type": "BodySystem"}]}

Example input:
Sentence: The distribution of Ca ( 2 + ) at regenerating MEPs following ESN was first detected by time - of - flight secondary ion mass spectrometry , and the specific localization and expression of Cav2 .

Example answer:
{"entities": [{"text": "distribution", "type": "BiologicFunction"}, {"text": "Ca ( 2 + )", "type": "Chemical"}, {"text": "MEPs", "type": "AnatomicalStructure"}, {"text": "ESN", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Cav2 .", "type": "Chemical"}]}

Input:
Sentence: Although the functional significance of calcium channels and the levels of Ca ( 2 + ) signalling in nerve regeneration are well documented , little is known about calcium channel expression and its relation with the dynamic Ca ( 2 + ) ion distribution at regenerating MEPs .

## Item MedMentions:test:1003
Example input:
Sentence: Myeloid - derived suppressor cells , which were a copious cell subset in BMCs , enhanced the Ki67 expression of Treg cells .

Example answer:
{"entities": [{"text": "Myeloid - derived suppressor cells", "type": "AnatomicalStructure"}, {"text": "copious cell subset", "type": "AnatomicalStructure"}, {"text": "BMCs", "type": "AnatomicalStructure"}, {"text": "Ki67", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Treg cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Surgery alone did not induce an inflammatory cell response , as evidenced by the lack of leukocyte infiltration in the sham groups .

Example answer:
{"entities": [{"text": "Surgery", "type": "HealthCareActivity"}, {"text": "inflammatory cell response", "type": "BiologicFunction"}, {"text": "leukocyte infiltration", "type": "Finding"}, {"text": "sham", "type": "HealthCareActivity"}]}

Example input:
Sentence: Except for CD68 and IL - 17 , the distribution of in situ for CD57 , IL - 10 , TNF - α and IFN - γ showed that patients with recent lesions expressed higher levels than those with late lesions .

Example answer:
{"entities": [{"text": "CD68", "type": "Chemical"}, {"text": "IL - 17", "type": "Chemical"}, {"text": "CD57", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "recent lesions", "type": "InjuryOrPoisoning"}, {"text": "lesions", "type": "Finding"}]}

Example input:
Sentence: The plaque area and serum pro - inflammatory cytokine ( IL - 1β , IL - 6 , TNF - α and IL - 17A ) levels in Lv - shSiglec - 1 mice were significantly lower than Lv - shNC mice , whereas IL - 10 was higher .

Example answer:
{"entities": [{"text": "plaque", "type": "Finding"}, {"text": "area", "type": "SpatialConcept"}, {"text": "serum", "type": "BodySubstance"}, {"text": "pro - inflammatory cytokine", "type": "Chemical"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "IL - 17A", "type": "Chemical"}, {"text": "Lv - shSiglec - 1", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "Lv - shNC", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}]}

Example input:
Sentence: The scars were significantly longer in the axilla group compared with the IMF group ( P < 0 .

Example answer:
{"entities": [{"text": "scars", "type": "AnatomicalStructure"}, {"text": "axilla", "type": "HealthCareActivity"}, {"text": "group", "type": "PopulationGroup"}, {"text": "IMF", "type": "SpatialConcept"}]}

Example input:
Sentence: Immune - suppression -mediated decrease in inflammation was associated with preserved myocardial flow reserve ( MFR ) at follow - up , whereas MFR significantly worsened in regions without changes or even increases in inflammation ( median Δ MFR : 0 . 07 [ IQR : -0 . 29 to 0 . 45 ] vs .

Example answer:
{"entities": [{"text": "Immune - suppression", "type": "HealthCareActivity"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "myocardial flow reserve", "type": "ClinicalAttribute"}, {"text": "MFR", "type": "ClinicalAttribute"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "worsened", "type": "Finding"}]}

Example input:
Sentence: This protective effect was associated with decreased muscle inflammation , but no changes in adipose tissue inflammation in aging M ( IL10 ) mice .

Example answer:
{"entities": [{"text": "muscle inflammation", "type": "BiologicFunction"}, {"text": "no", "type": "Finding"}, {"text": "adipose tissue", "type": "AnatomicalStructure"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "aging", "type": "BiologicFunction"}, {"text": "M ( IL10 )", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: In conclusion , these data suggested that ( i ) patients from Group I had recent lesions ( in the beginning of chronic phase ) compared to those from Group II and ( ii ) the modulation of inflammatory response in patients with recent American cutaneous leishmaniasis was correlated with IL - 10 expression in skin lesions preventing the development of mucosal forms .

Example answer:
{"entities": [{"text": "Group I", "type": "PopulationGroup"}, {"text": "recent lesions", "type": "InjuryOrPoisoning"}, {"text": "Group II", "type": "PopulationGroup"}, {"text": "inflammatory response", "type": "BiologicFunction"}, {"text": "American cutaneous leishmaniasis", "type": "BiologicFunction"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "skin lesions", "type": "BiologicFunction"}, {"text": "development", "type": "BiologicFunction"}, {"text": "mucosal forms", "type": "Finding"}]}

Example input:
Sentence: Additionally , adh7Δ cells were more sensitive to the combined stress than wild - type and bdh2Δ cells .

Example answer:
{"entities": [{"text": "combined stress", "type": "Finding"}, {"text": "wild - type", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Compared with D0 no surgery controls , the D1 and D7 sham groups exhibited no surgical mortality and similar necropsy and echocardiographic variables .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "sham", "type": "HealthCareActivity"}, {"text": "surgical", "type": "HealthCareActivity"}, {"text": "necropsy", "type": "HealthCareActivity"}, {"text": "echocardiographic", "type": "HealthCareActivity"}]}

Input:
Sentence: In contrast , the D1 and D7 MI groups showed the expected robust inflammatory and scar formation responses .

## Item MedMentions:test:1230
Example input:
Sentence: One - sample test for proportions and T - tests examined equality of proportions ( anchors ) and means scores ( non - anchors ) with the fixed intervals ( 0 . 0 , 2 . 5 , 5 . 0 , 7 . 5 , and 10 . 0 ) .

Example answer:
{"entities": [{"text": "One - sample test", "type": "IntellectualProduct"}, {"text": "T - tests", "type": "IntellectualProduct"}, {"text": "anchors", "type": "PopulationGroup"}, {"text": "non - anchors", "type": "PopulationGroup"}]}

Example input:
Sentence: Chi - squared test and t - test for independent samples were performed to compare sociodemographic and clinical variables between the two groups .

Example answer:
{"entities": [{"text": "Chi - squared test", "type": "IntellectualProduct"}, {"text": "t - test", "type": "IntellectualProduct"}]}

Example input:
Sentence: One - way analysis of variance , Student 's t - test and Chi - square tests were used as appropriate with statistical significance attributed to P < 0 .

Example answer:
{"entities": [{"text": "Chi - square tests", "type": "IntellectualProduct"}]}

Example input:
Sentence: Paired t - tests assessed within - participant improvement in targeted barriers each month , and nested regression models assessed if changes in a participant 's barrier scores were associated with improvements in adherence and HbA1c .

Example answer:
{"entities": [{"text": "t - tests", "type": "IntellectualProduct"}, {"text": "within - participant", "type": "PopulationGroup"}, {"text": "regression models", "type": "IntellectualProduct"}, {"text": "participant 's", "type": "PopulationGroup"}, {"text": "HbA1c", "type": "Chemical"}]}

Example input:
Sentence: Independent t - tests were used to evaluate potential sex and grade level differences for age , BMI , VO2 , EE , and METs .

Example answer:
{"entities": [{"text": "Independent t - tests", "type": "IntellectualProduct"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "VO2", "type": "HealthCareActivity"}, {"text": "EE", "type": "BiologicFunction"}, {"text": "METs", "type": "HealthCareActivity"}]}

Example input:
Sentence: Data were ‎analyzed using the independent t - test , analysis of covariance , and Pearson Correlation analysis .‎ Results : The two groups did not show any differences in comprehending the stories ; however , the BD ‎ group 's mentalizing scores were significantly weaker than the TD group ( p < 0 . 05 ) .

Example answer:
{"entities": [{"text": "t - test", "type": "IntellectualProduct"}, {"text": "Pearson Correlation analysis", "type": "ResearchActivity"}, {"text": "BD", "type": "BiologicFunction"}]}

Example input:
Sentence: Unpaired Student 's t - test was used to evaluate statistical differences between groups .

Example answer:
{"entities": [{"text": "Unpaired Student 's t - test", "type": "IntellectualProduct"}, {"text": "evaluate", "type": "HealthCareActivity"}]}

Example input:
Sentence: The differences between measurements were statistically analyzed using paired t tests .

Example answer:
{"entities": [{"text": "paired t tests", "type": "IntellectualProduct"}]}

Example input:
Sentence: Data was analyzed with t - test and paired t - test by using SPSS 21 software .

Example answer:
{"entities": [{"text": "t - test", "type": "IntellectualProduct"}, {"text": "paired t - test", "type": "IntellectualProduct"}, {"text": "SPSS 21 software", "type": "IntellectualProduct"}]}

Example input:
Sentence: 01 ) in all patients using a paired t - test analysis .

Example answer:
{"entities": [{"text": "t - test analysis", "type": "IntellectualProduct"}]}

Input:
Sentence: Exam results for both groups were analyzed with a paired Student 's t - test .

## Item MedMentions:test:1023
Example input:
Sentence: One strategy involves the synthesis of a one - bead - two - peptides library in which each bead contains both the cyclic peptide and its linear counterpart to facilitate MS analysis .

Example answer:
{"entities": [{"text": "one - bead - two - peptides library", "type": "Chemical"}, {"text": "cyclic peptide", "type": "Chemical"}, {"text": "MS analysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: This LC - MS / MS method displayed good selectivity , sensitivity ( lower limit of quantification = 2 .

Example answer:
{"entities": [{"text": "LC - MS / MS method", "type": "HealthCareActivity"}]}

Example input:
Sentence: MS data were used to generate spectral libraries of non - modified peptides and an open modification search was performed to identify potential adduct mass shifts and possible modification sites .

Example answer:
{"entities": [{"text": "MS", "type": "HealthCareActivity"}, {"text": "libraries", "type": "Chemical"}, {"text": "peptides", "type": "Chemical"}]}

Example input:
Sentence: Combinatorial Library Screening Coupled to Mass Spectrometry to Identify Valuable Cyclic Peptides Combinatorial library screening coupled to mass spectrometry ( MS ) analysis is a practical approach to identify useful peptides .

Example answer:
{"entities": [{"text": "Combinatorial Library", "type": "Chemical"}, {"text": "Mass Spectrometry", "type": "HealthCareActivity"}, {"text": "Cyclic Peptides", "type": "Chemical"}, {"text": "Combinatorial library", "type": "Chemical"}, {"text": "mass spectrometry ( MS ) analysis", "type": "HealthCareActivity"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "peptides", "type": "Chemical"}]}

Example input:
Sentence: Metabolite mapping by consecutive nanostructure and silver - assisted mass spectrometry imaging on tissue sections Nanostructure - based mass spectrometry imaging ( MSI ) is a promising technology for molecular imaging of small molecules , without the complex chemical background typically encountered in matrix - assisted molecular imaging approaches .

Example answer:
{"entities": [{"text": "Metabolite", "type": "Chemical"}, {"text": "silver - assisted mass spectrometry imaging", "type": "HealthCareActivity"}, {"text": "tissue sections", "type": "AnatomicalStructure"}, {"text": "Nanostructure - based mass spectrometry imaging", "type": "HealthCareActivity"}, {"text": "MSI", "type": "HealthCareActivity"}, {"text": "molecular imaging", "type": "HealthCareActivity"}, {"text": "small molecules", "type": "Chemical"}, {"text": "matrix - assisted molecular imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: By optimizing MS / MS parameters , we established a quantification method that allowed the simultaneous analysis of 18 d - amino acids with high sensitivity and reproducibility .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "d - amino acids", "type": "Chemical"}]}

Example input:
Sentence: Mass spectrometry based proteomics provides a suitable platform to investigate protease activity , providing information about substrate specificity and mapping cleavage sites .

Example answer:
{"entities": [{"text": "Mass spectrometry", "type": "HealthCareActivity"}, {"text": "proteomics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "protease activity", "type": "BiologicFunction"}, {"text": "mapping", "type": "HealthCareActivity"}, {"text": "cleavage sites", "type": "SpatialConcept"}]}

Example input:
Sentence: The ability to place metabolite and lipid classes in a tissue - specific context makes this novel method suited to MSI analyses where the collection of additional information from the same sample maximises resource use , and also maximises the number of annotated small molecules , in particular for metabolites that are typically undetectable with traditional platforms .

Example answer:
{"entities": [{"text": "metabolite", "type": "Chemical"}, {"text": "lipid", "type": "Chemical"}, {"text": "MSI analyses", "type": "HealthCareActivity"}, {"text": "small molecules", "type": "Chemical"}, {"text": "metabolites", "type": "Chemical"}, {"text": "undetectable", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Recent advancements in MS enable us to determine the molecular masses of protein - ligand complexes without disrupting the non - covalent interactions through the gentle desolvation of the complexes by increasing the vacuum pressure of a chamber in a mass spectrometer .

Example answer:
{"entities": [{"text": "MS", "type": "HealthCareActivity"}, {"text": "protein", "type": "Chemical"}, {"text": "ligand", "type": "Chemical"}, {"text": "complexes", "type": "Chemical"}, {"text": "desolvation", "type": "BiologicFunction"}, {"text": "chamber", "type": "MedicalDevice"}, {"text": "mass spectrometer", "type": "MedicalDevice"}]}

Example input:
Sentence: Mass spectrometry ( MS ) has been used to determine the precise molecular masses of molecules .

Example answer:
{"entities": [{"text": "Mass spectrometry", "type": "HealthCareActivity"}, {"text": "MS", "type": "HealthCareActivity"}]}

Input:
Sentence: While mass spectrometry ( MS ) analysis offers the potential for in - depth compositional analysis it is often limited in coverage and relative quantitation capacity .
