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

## Item MedMentions:test:1154
Example input:
Sentence: The patient delivered a clinically healthy boy , who was given the first dose of the HBV vaccine and intravenous specific immunoglobulin , followed by the second dose 2 months later , and did not get infected with HBV .

Example answer:
{"entities": [{"text": "delivered", "type": "Finding"}, {"text": "clinically healthy boy", "type": "Finding"}, {"text": "HBV vaccine", "type": "HealthCareActivity"}, {"text": "intravenous specific immunoglobulin", "type": "Chemical"}, {"text": "infected", "type": "Finding"}, {"text": "HBV", "type": "Virus"}]}

Example input:
Sentence: The second case , a 22 - year - old female , referred to hospital with suspected vasculitis , with complaints of " off and on " fever with decreased oral intake , arthralgia , who later developed generalized nodular skin eruptions .

Example answer:
{"entities": [{"text": "hospital", "type": "Organization"}, {"text": "vasculitis", "type": "BiologicFunction"}, {"text": "fever", "type": "Finding"}, {"text": "decreased oral intake", "type": "Finding"}, {"text": "arthralgia", "type": "Finding"}, {"text": "generalized", "type": "SpatialConcept"}, {"text": "nodular skin eruptions", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , we describe MERS in a 10 - year - old boy who presented with fever and consciousness and who completely recovered within a few days .

Example answer:
{"entities": [{"text": "MERS", "type": "BiologicFunction"}, {"text": "fever", "type": "Finding"}, {"text": "consciousness", "type": "Finding"}, {"text": "completely recovered", "type": "Finding"}]}

Example input:
Sentence: The envelope protein E of the yellow fever vaccine strain 17D has significant amino acid sequence overlap with both hypocretin and the hypocretin receptor 2 receptors in protein regions that are predicted to act as epitopes for antibody production .

Example answer:
{"entities": [{"text": "envelope protein E of the yellow fever vaccine strain 17D", "type": "Chemical"}, {"text": "amino acid sequence", "type": "SpatialConcept"}, {"text": "hypocretin", "type": "Chemical"}, {"text": "hypocretin receptor 2 receptors", "type": "Chemical"}, {"text": "protein regions", "type": "SpatialConcept"}, {"text": "epitopes", "type": "Chemical"}, {"text": "antibody production", "type": "BiologicFunction"}]}

Example input:
Sentence: The descriptive study was conducted at Layton Rahmatullah Benevolent Trust , Lahore , Pakistan , from October 2013 to April 2014 , and comprised children under 15 years of age who had rubella syndrome , herpes simplex , birth trauma , trisomy 21 , Nance - Horan syndrome or Lowe 's syndrome .

Example answer:
{"entities": [{"text": "descriptive study", "type": "ResearchActivity"}, {"text": "Layton Rahmatullah Benevolent Trust", "type": "Organization"}, {"text": "Pakistan", "type": "SpatialConcept"}, {"text": "herpes simplex", "type": "BiologicFunction"}, {"text": "birth trauma", "type": "Finding"}, {"text": "trisomy 21", "type": "BiologicFunction"}, {"text": "Nance - Horan syndrome", "type": "BiologicFunction"}, {"text": "Lowe 's syndrome", "type": "BiologicFunction"}]}

Example input:
Sentence: We present a case of sixteen years old boy diagnosed with SS situated of the hypopharynx treated by surgical excision and post operative radio - chemotherapy .

Example answer:
{"entities": [{"text": "diagnosed", "type": "Finding"}, {"text": "SS", "type": "BiologicFunction"}, {"text": "hypopharynx", "type": "SpatialConcept"}, {"text": "treated by", "type": "HealthCareActivity"}, {"text": "surgical excision", "type": "HealthCareActivity"}, {"text": "post operative", "type": "Finding"}, {"text": "radio", "type": "HealthCareActivity"}, {"text": "chemotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: An adolescent boy collapsed unconscious following convulsion for 3 - 5 min with fever and headache for 2 days .

Example answer:
{"entities": [{"text": "collapsed", "type": "Finding"}, {"text": "unconscious", "type": "Finding"}, {"text": "convulsion", "type": "Finding"}, {"text": "fever", "type": "Finding"}, {"text": "headache", "type": "Finding"}]}

Example input:
Sentence: These findings raise the question whether the yellow fever vaccine strain may , through a potential molecular mimicry mechanism , be another infectious trigger for this neuro - immunological disorder .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "question", "type": "IntellectualProduct"}, {"text": "yellow fever vaccine strain", "type": "Chemical"}, {"text": "molecular mimicry", "type": "BiologicFunction"}, {"text": "infectious trigger", "type": "ClinicalAttribute"}, {"text": "neuro - immunological", "type": "BiologicFunction"}, {"text": "disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: We report a case of a fifteen - months - old girl , previously healthy and vaccinated , admitted in the emergency room with fever and vomiting .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "vaccinated", "type": "HealthCareActivity"}, {"text": "admitted", "type": "HealthCareActivity"}, {"text": "emergency room", "type": "Organization"}, {"text": "fever", "type": "Finding"}, {"text": "vomiting", "type": "Finding"}]}

Example input:
Sentence: Narcolepsy Following Yellow Fever Vaccination : A Case Report Narcolepsy with cataplexy is a rare , but important differential diagnosis for daytime sleepiness and atonic paroxysms in an adolescent .

Example answer:
{"entities": [{"text": "Narcolepsy", "type": "BiologicFunction"}, {"text": "Yellow Fever Vaccination", "type": "HealthCareActivity"}, {"text": "Case Report", "type": "IntellectualProduct"}, {"text": "cataplexy", "type": "BiologicFunction"}, {"text": "differential diagnosis", "type": "HealthCareActivity"}, {"text": "daytime sleepiness", "type": "Finding"}, {"text": "atonic", "type": "Finding"}]}

Input:
Sentence: Here , we describe the case of a 13 - year - old boy with narcolepsy following yellow fever vaccination .

## Item MedMentions:test:848
Example input:
Sentence: The meta - analysis revealed that IV magnesium sulfate is an effective treatment in children , with the pulmonary function significantly improved and hospitalization and further treatment decreased .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "IntellectualProduct"}, {"text": "IV", "type": "HealthCareActivity"}, {"text": "magnesium sulfate", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "pulmonary function", "type": "BiologicFunction"}, {"text": "hospitalization", "type": "HealthCareActivity"}, {"text": "further treatment", "type": "Finding"}]}

Example input:
Sentence: In children treated for sepsis in the emergency department , lactate levels greater than 36 mg / dL were associated with mortality but had a low sensitivity .

Example answer:
{"entities": [{"text": "sepsis", "type": "BiologicFunction"}, {"text": "emergency department", "type": "Organization"}, {"text": "lactate levels", "type": "Finding"}]}

Example input:
Sentence: This observational cohort study of a clinical registry of pediatric patients with suspected sepsis in the emergency department of a tertiary children 's hospital from April 1 , 2012 , to December 31 , 2015 , tested the hypothesis that a serum lactate level of greater than 36 mg / dL is associated with increased mortality compared with a serum lactate level of 36 mg / dL or less .

Example answer:
{"entities": [{"text": "clinical registry", "type": "ResearchActivity"}, {"text": "sepsis", "type": "BiologicFunction"}, {"text": "emergency department", "type": "Organization"}, {"text": "tertiary children 's hospital", "type": "Organization"}, {"text": "serum lactate level", "type": "HealthCareActivity"}]}

Example input:
Sentence: The primary outcome measure was serum bicarbonate level at 4 h .

Example answer:
{"entities": [{"text": "serum bicarbonate level", "type": "Finding"}]}

Example input:
Sentence: Methods 100 children ( 1 - 5 years , 10 - 25 kg ) were randomized into four groups : controls ( saline ) and intravenous Dex at 0 .

Example answer:
{"entities": [{"text": "randomized", "type": "ResearchActivity"}, {"text": "intravenous", "type": "SpatialConcept"}, {"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: Icv injection of hypertonic NaCl with AA or 5 , 6 - EET restored water intake by Nax - KO mice to the WT level , but not that by TRPV4 - KO mice .

Example answer:
{"entities": [{"text": "Icv", "type": "SpatialConcept"}, {"text": "injection", "type": "HealthCareActivity"}, {"text": "hypertonic NaCl", "type": "Chemical"}, {"text": "AA", "type": "Chemical"}, {"text": "5 , 6 - EET", "type": "Chemical"}, {"text": "water intake", "type": "BiologicFunction"}, {"text": "Nax", "type": "AnatomicalStructure"}, {"text": "KO mice", "type": "Eukaryote"}, {"text": "WT", "type": "AnatomicalStructure"}, {"text": "TRPV4", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 9 % NaCl in improvement of 4 - h bicarbonate .

Example answer:
{"entities": [{"text": "improvement of 4 - h bicarbonate", "type": "HealthCareActivity"}]}

Example input:
Sentence: The PLA group had less abdominal pain and better dehydration scores at hour 2 ( both P = .03 ) but not at hour 4 ( P = 0 . 15 and 0 . 08 , respectively ) .

Example answer:
{"entities": [{"text": "PLA", "type": "Chemical"}, {"text": "group", "type": "PopulationGroup"}, {"text": "abdominal pain", "type": "Finding"}, {"text": "dehydration", "type": "BiologicFunction"}]}

Example input:
Sentence: A randomized trial of Plasma - Lyte A and 0 . 9 % sodium chloride in acute pediatric gastroenteritis Compare the efficacy and safety of Plasma - Lyte A ( PLA ) versus 0 . 9 % sodium chloride ( NaCl ) intravenous ( IV ) fluid replacement in children with moderate to severe dehydration secondary to acute gastroenteritis ( AGE ) .

Example answer:
{"entities": [{"text": "randomized trial", "type": "ResearchActivity"}, {"text": "Plasma - Lyte A", "type": "Chemical"}, {"text": "acute pediatric gastroenteritis", "type": "BiologicFunction"}, {"text": "PLA", "type": "Chemical"}, {"text": "intravenous ( IV ) fluid replacement", "type": "HealthCareActivity"}, {"text": "severe dehydration", "type": "BiologicFunction"}, {"text": "acute gastroenteritis", "type": "BiologicFunction"}, {"text": "AGE", "type": "BiologicFunction"}]}

Example input:
Sentence: At hour 4 , the PLA group had greater increases in serum bicarbonate from baseline than did the 0 . 9 % NaCl group ( mean ± SD at 4 h : 18 ± 3 .

Example answer:
{"entities": [{"text": "PLA", "type": "Chemical"}, {"text": "group", "type": "PopulationGroup"}, {"text": "increases in serum bicarbonate", "type": "Finding"}]}

Input:
Sentence: 9 % NaCl , PLA for rehydration in children with AGE was well tolerated and led to more rapid improvement in serum bicarbonate and dehydration score .

## Item MedMentions:test:951
Example input:
Sentence: Patients and caregivers emphasized the need for guidelines to address patient education and engagement , and the psychosocial implications of communication and provision of care in the context of infectious microorganisms in hemodialysis units .

Example answer:
{"entities": [{"text": "caregivers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "guidelines", "type": "IntellectualProduct"}, {"text": "engagement", "type": "HealthCareActivity"}, {"text": "provision of care", "type": "HealthCareActivity"}]}

Example input:
Sentence: They offered two reasons for this : ( 1 ) language barriers between care provider and parents hindered the exchange of information ; ( 2 ) cultural barriers between care provider and parents about sharing the diagnosis and palliative perspective hindered communication .

Example answer:
{"entities": [{"text": "language barriers", "type": "Finding"}, {"text": "care provider", "type": "ProfessionalOrOccupationalGroup"}, {"text": "diagnosis", "type": "Finding"}]}

Example input:
Sentence: The respondents were randomly assigned to one of two scenarios describing a mild or severe febrile episode in an LTCF resident at night .

Example answer:
{"entities": [{"text": "respondents", "type": "PopulationGroup"}, {"text": "febrile", "type": "Finding"}, {"text": "LTCF", "type": "Organization"}, {"text": "resident", "type": "PopulationGroup"}]}

Example input:
Sentence: Well educated patients with symptoms of recurrence more often sought medical attendance compared to less educated counterparts .

Example answer:
{"entities": [{"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: Patients received points for the following signs and symptoms within the past 7 days : cough ( 2 points ) , headache ( 1 point ) , subjective fever ( 1 point ) , and documented fever at triage ( temperature > 38°C [ 100 . 4°F ] ) ( 1 point ) .

Example answer:
{"entities": [{"text": "signs and symptoms", "type": "Finding"}, {"text": "cough", "type": "Finding"}, {"text": "headache", "type": "Finding"}, {"text": "documented fever", "type": "Finding"}, {"text": "triage", "type": "HealthCareActivity"}]}

Example input:
Sentence: The present study aimed to examine the factors associated with inadequacy of initial fever evaluations by caregivers at night in LTCF .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "fever", "type": "Finding"}, {"text": "evaluations", "type": "HealthCareActivity"}, {"text": "caregivers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "LTCF", "type": "Organization"}]}

Example input:
Sentence: Respondents ' thinking patterns in fever evaluation were significantly associated with the adequacy of the evaluation .

Example answer:
{"entities": [{"text": "Respondents", "type": "PopulationGroup"}, {"text": "thinking patterns", "type": "BiologicFunction"}, {"text": "fever", "type": "Finding"}, {"text": "evaluation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Adequacy of initial evaluation of fever in long - term care facilities Febrile residents in long - term care facilities ( LTCF ) might be inadequately evaluated by caregivers .

Example answer:
{"entities": [{"text": "evaluation", "type": "HealthCareActivity"}, {"text": "fever", "type": "Finding"}, {"text": "long - term care facilities", "type": "Organization"}, {"text": "Febrile", "type": "Finding"}, {"text": "residents", "type": "PopulationGroup"}, {"text": "LTCF", "type": "Organization"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "caregivers", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Caregivers who placed particular importance on the preferences of residents and families versus other factors including the resident ' s febrile condition , were more likely to make an inadequate evaluation than those who did not .

Example answer:
{"entities": [{"text": "Caregivers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "residents", "type": "PopulationGroup"}, {"text": "resident", "type": "PopulationGroup"}, {"text": "febrile", "type": "Finding"}, {"text": "evaluation", "type": "HealthCareActivity"}]}

Example input:
Sentence: A total of 34 % of fever evaluations among caregivers were considered to be inadequate regarding the necessity for examination by a physician , due in most cases to underestimating the severity of the fever .

Example answer:
{"entities": [{"text": "fever", "type": "Finding"}, {"text": "evaluations", "type": "HealthCareActivity"}, {"text": "caregivers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "examination", "type": "HealthCareActivity"}, {"text": "physician", "type": "ProfessionalOrOccupationalGroup"}]}

Input:
Sentence: Our findings here suggest that eagerness to comply with residents ' preference in fever evaluation could prompt caregivers not to call for an appropriate diagnostic procedure .

## Item MedMentions:test:749
Example input:
Sentence: Draft Genome Sequence of the Soil Isolate Lysinibacillus fusiformis M5 , a Potential Hypoxanthine Producer Lysinibacillus fusiformis strain M5 is a potential hypoxanthine producer that was isolated from clay soil .

Example answer:
{"entities": [{"text": "Draft Genome Sequence", "type": "SpatialConcept"}, {"text": "Isolate", "type": "Chemical"}, {"text": "Lysinibacillus fusiformis M5", "type": "Bacterium"}, {"text": "Hypoxanthine", "type": "Chemical"}, {"text": "Lysinibacillus fusiformis strain M5", "type": "Bacterium"}, {"text": "hypoxanthine", "type": "Chemical"}, {"text": "isolated", "type": "Chemical"}, {"text": "clay", "type": "Chemical"}]}

Example input:
Sentence: The two isolated endophytes , BB1 and BB2 , were identified through 16S rDNA techniques and NCBI - BLAST algorithm with 99 % sequence similarity with those of Janibacter sp . ( KX423734 ) and Serratia marcescens strain ( KX423735 ) .

Example answer:
{"entities": [{"text": "endophytes", "type": "Eukaryote"}, {"text": "BB1", "type": "Eukaryote"}, {"text": "BB2", "type": "Eukaryote"}, {"text": "16S rDNA", "type": "Chemical"}, {"text": "techniques", "type": "HealthCareActivity"}, {"text": "NCBI - BLAST algorithm", "type": "IntellectualProduct"}, {"text": "sequence", "type": "SpatialConcept"}, {"text": "Janibacter sp .", "type": "Bacterium"}, {"text": "KX423734", "type": "Bacterium"}, {"text": "Serratia marcescens", "type": "Bacterium"}, {"text": "KX423735", "type": "Bacterium"}]}

Example input:
Sentence: On the basis of the data presented , strain KEM - 4 T is considered to represent a novel species of the genus Altererythrobacter , for which the name Altererythrobacter confluentis sp .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Altererythrobacter", "type": "Bacterium"}, {"text": "Altererythrobacter confluentis sp .", "type": "Bacterium"}]}

Example input:
Sentence: Phylogenetic analyses based on 16S rRNA gene sequences indicated that strain SYP - A7299 T belongs to the genus Arthrobacter and is most closely related to Arthrobacter halodurans JSM 078085 T ( 97 . 4 % 16S rRNA gene sequence similarity ) .

Example answer:
{"entities": [{"text": "Phylogenetic analyses", "type": "ResearchActivity"}, {"text": "16S rRNA gene sequences", "type": "AnatomicalStructure"}, {"text": "strain SYP - A7299 T", "type": "Bacterium"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Arthrobacter", "type": "Bacterium"}, {"text": "Arthrobacter halodurans JSM 078085 T", "type": "Bacterium"}, {"text": "16S rRNA gene sequence", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Mey . ) Schischk An orange - coloured , aerobic , motile and short - rods bacterial strain , designated EGI 6500337 T , was isolated from the surface - sterilized root of a halophyte Anabasis elatior ( C .

Example answer:
{"entities": [{"text": "Mey . ) Schischk", "type": "Eukaryote"}, {"text": "short - rods bacterial strain", "type": "Bacterium"}, {"text": "EGI 6500337 T", "type": "Bacterium"}, {"text": "root", "type": "Eukaryote"}, {"text": "halophyte", "type": "Eukaryote"}, {"text": "Anabasis elatior ( C .", "type": "Eukaryote"}]}

Example input:
Sentence: The polar lipid profile of strain EGI 6500337 T contained diphosphatidylglycerol , phosphatidylglycerol , phosphatidylcholine , phosphatidylethanolamine as major components , similarly to the members of the genus Aurantimonas .

Example answer:
{"entities": [{"text": "lipid profile", "type": "Chemical"}, {"text": "strain EGI 6500337 T", "type": "Bacterium"}, {"text": "diphosphatidylglycerol", "type": "Chemical"}, {"text": "phosphatidylglycerol", "type": "Chemical"}, {"text": "phosphatidylcholine", "type": "Chemical"}, {"text": "phosphatidylethanolamine", "type": "Chemical"}, {"text": "genus Aurantimonas", "type": "Bacterium"}]}

Example input:
Sentence: Based on the morphological , physiological , biochemical and chemotaxonomic characters presented in this study , strain SYP - A7299 T represents a novel species of the genus Arthrobacter , for which the name Arthrobacter ginkgonis sp .

Example answer:
{"entities": [{"text": "morphological", "type": "SpatialConcept"}, {"text": "strain SYP - A7299 T", "type": "Bacterium"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Arthrobacter", "type": "Bacterium"}, {"text": "Arthrobacter ginkgonis sp .", "type": "Bacterium"}]}

Example input:
Sentence: The 16S rRNA gene sequence of strain EGI 6500337 T shared the highest similarities to those of Aurantimonas coralicida DSM 14790 T ( 97 . 15 % ) and Aurantimonas manganoxydans DSM 21871 T ( 97 . 15 % ) .

Example answer:
{"entities": [{"text": "16S rRNA", "type": "Chemical"}, {"text": "gene sequence", "type": "SpatialConcept"}, {"text": "strain EGI 6500337 T", "type": "Bacterium"}, {"text": "Aurantimonas coralicida DSM 14790 T", "type": "Bacterium"}, {"text": "Aurantimonas manganoxydans DSM 21871 T", "type": "Bacterium"}]}

Example input:
Sentence: Aurantimonas endophytica sp .

Example answer:
{"entities": [{"text": "Aurantimonas endophytica sp .", "type": "Bacterium"}]}

Example input:
Sentence: Phylogenetic tree based on 16S rRNA gene sequences indicated that strain EGI 6500337 T formed a distinct lineage in the cluster that comprised the genera Aurantimonas and Aureimonas in the family Aurantimonadaceae .

Example answer:
{"entities": [{"text": "16S rRNA", "type": "Chemical"}, {"text": "gene sequences", "type": "SpatialConcept"}, {"text": "strain EGI 6500337 T", "type": "Bacterium"}, {"text": "genera Aurantimonas", "type": "Bacterium"}, {"text": "Aureimonas", "type": "Bacterium"}, {"text": "family Aurantimonadaceae", "type": "Bacterium"}]}

Input:
Sentence: On the basis of the phylogenetic analysis , chemotaxonomic data and phenotypic characteristics , strain EGI 6500337 T represents a novel species of the genus Aurantimonas , for which the name Aurantimonas endophytica sp .

## Item MedMentions:test:1198
Example input:
Sentence: Less than one - half of the participants were aware of the parent 's LW or DPAHC .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "aware", "type": "BiologicFunction"}, {"text": "LW", "type": "IntellectualProduct"}, {"text": "DPAHC", "type": "Finding"}]}

Example input:
Sentence: The effects of father involvement on child outcomes are discussed within each phase of a child 's development .

Example answer:
{"entities": [{"text": "child outcomes", "type": "BiologicFunction"}, {"text": "child 's development", "type": "BiologicFunction"}]}

Example input:
Sentence: When children had a negative relationship with their parent , a supportive message of that parent decreased working memory performance , while a supportive message from the teacher increased performance .

Example answer:
{"entities": [{"text": "negative", "type": "Finding"}, {"text": "supportive", "type": "HealthCareActivity"}, {"text": "message", "type": "IntellectualProduct"}, {"text": "working memory", "type": "BiologicFunction"}, {"text": "performance", "type": "BiologicFunction"}, {"text": "teacher", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Implications and advice for all child health providers to encourage and support father involvement are outlined .

Example answer:
{"entities": [{"text": "advice", "type": "HealthCareActivity"}, {"text": "health providers", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: These four beliefs or dimensions of the negative perception colloquially known as " the dark side " are the belief that they lack both managerial and clinical credibility , they have confused identities , they may be in conflict with clinicians , their clinical colleagues lack insight into the complexities of medical leadership and , as a result , doctors are actively discouraged from making the transition from clinical practice to medical leadership roles in the first place .

Example answer:
{"entities": [{"text": "clinicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "doctors", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Findings Medical leaders had four key beliefs about the " dark side " as perceived through the eyes of their own past clinical experience and / or their clinical colleagues .

Example answer:
{"entities": [{"text": "leaders", "type": "ProfessionalOrOccupationalGroup"}, {"text": "eyes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The deductive analysis was based on the caring theory of ' Involvement in the light - Involvement in the dark ' .

Example answer:
{"entities": []}

Example input:
Sentence: The research question is : " What are the beliefs of medical leaders that form the key themes or dimensions of the negative perception of the ' dark side ' ? " . Design / methodology / approach The paper analysed data from two similar qualitative studies examining medical leadership and engagement in Australia by the same author , in collaboration with other researchers , which used in - depth semi - structured interviews with 45 purposively sampled senior medical leaders in leadership roles across Australia in health services , private and public hospitals , professional associations and health departments .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "leaders", "type": "ProfessionalOrOccupationalGroup"}, {"text": "qualitative studies", "type": "ResearchActivity"}, {"text": "Australia", "type": "SpatialConcept"}, {"text": "researchers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "health services", "type": "HealthCareActivity"}, {"text": "private", "type": "Organization"}, {"text": "public hospitals", "type": "Organization"}, {"text": "health departments", "type": "Organization"}]}

Example input:
Sentence: An isolated involvement in mental health care - experiences of parents of young adults To explore parents ' involvement in the informal and professional care of their young adult child with mental illness .

Example answer:
{"entities": [{"text": "mental health care", "type": "HealthCareActivity"}, {"text": "experiences", "type": "BiologicFunction"}, {"text": "informal", "type": "HealthCareActivity"}, {"text": "professional care", "type": "HealthCareActivity"}, {"text": "mental illness", "type": "BiologicFunction"}]}

Example input:
Sentence: A further aim was to examine concepts in the caring theory of ' Involvement in the light - Involvement in the dark ' in the context of mental health care .

Example answer:
{"entities": [{"text": "mental health care", "type": "HealthCareActivity"}]}

Input:
Sentence: The result are to a great extent consistent with the ' Involvement in the dark ' metaphor , which describes an isolated involvement in which the parents were not informed , seen or acknowledged by the health professionals .

## Item MedMentions:test:1017
Example input:
Sentence: Data are limited on incidence of metabolic comorbidities in HIV + individuals initiating ART in low and middle income countries ( LMICs ) , particularly for Hispanics .

Example answer:
{"entities": [{"text": "HIV +", "type": "Finding"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "ART", "type": "HealthCareActivity"}, {"text": "countries", "type": "SpatialConcept"}, {"text": "LMICs", "type": "SpatialConcept"}, {"text": "Hispanics", "type": "PopulationGroup"}]}

Example input:
Sentence: Bivariate and multivariate analyses were done to identify independent predictors of provider -initiated HIV testing and counseling refusal by OPD clients .

Example answer:
{"entities": [{"text": "HIV testing", "type": "HealthCareActivity"}, {"text": "counseling", "type": "HealthCareActivity"}, {"text": "OPD", "type": "Organization"}]}

Example input:
Sentence: Delayed ART uptake ultimately translates into high rates of HIV morbidity , mortality , and transmission .

Example answer:
{"entities": [{"text": "ART", "type": "HealthCareActivity"}, {"text": "HIV", "type": "BiologicFunction"}, {"text": "transmission", "type": "BiologicFunction"}]}

Example input:
Sentence: 7 % ( CI 86 . 1 - 95 . 2 ) reporting HIV - positive status and receiving ART , 66 .

Example answer:
{"entities": [{"text": "ART", "type": "HealthCareActivity"}]}

Example input:
Sentence: 9 - 73 . 4 ) reporting HIV - positive status irrespective of ART use , 21 . 0 % ( CI 13 . 4 - 28 . 6 ) reporting HIV - negative status , and 19 . 3 % ( CI 9 . 0 - 29 . 5 ) reporting no previous HIV test .

Example answer:
{"entities": [{"text": "ART", "type": "HealthCareActivity"}, {"text": "reporting", "type": "HealthCareActivity"}, {"text": "HIV - negative status", "type": "Finding"}, {"text": "no", "type": "Finding"}, {"text": "HIV test", "type": "HealthCareActivity"}]}

Example input:
Sentence: Key individual impediments to ART uptake included inadequate preparation for a positive diagnosis and the dual stigmatisation of homosexuality and HIV and its consequences , leading to fear of disclosure of HIV status .

Example answer:
{"entities": [{"text": "ART", "type": "HealthCareActivity"}, {"text": "positive", "type": "Finding"}, {"text": "diagnosis", "type": "Finding"}, {"text": "HIV", "type": "Virus"}, {"text": "consequences", "type": "ResearchActivity"}, {"text": "fear", "type": "BiologicFunction"}, {"text": "HIV status", "type": "Finding"}]}

Example input:
Sentence: Undisclosed HIV infection and art use in the kenya AIDS indicator survey 2012 : relevance to targets for HIV diagnosis and treatment in kenya To assess the impact of undisclosed HIV infection and antiretroviral ( ARV ) therapy ( ART ) on national estimates of diagnosed HIV and ART coverage in Kenya .

Example answer:
{"entities": [{"text": "HIV infection", "type": "BiologicFunction"}, {"text": "art", "type": "HealthCareActivity"}, {"text": "kenya AIDS indicator survey 2012", "type": "IntellectualProduct"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "kenya", "type": "SpatialConcept"}, {"text": "antiretroviral ( ARV ) therapy", "type": "HealthCareActivity"}, {"text": "ART", "type": "HealthCareActivity"}, {"text": "Kenya", "type": "SpatialConcept"}]}

Example input:
Sentence: Estimates of diagnosed HIV and ART use based on self - report were compared with those corrected for undisclosed HIV infection and ART use based on ARV testing .

Example answer:
{"entities": [{"text": "ART", "type": "HealthCareActivity"}, {"text": "self - report", "type": "ResearchActivity"}, {"text": "HIV infection", "type": "BiologicFunction"}]}

Example input:
Sentence: Undisclosed HIV infection on ART was associated with being aged 25 - 39 years and not visiting a health provider in the past year , while younger age and higher wealth was associated with undisclosed ART use .

Example answer:
{"entities": [{"text": "HIV infection", "type": "BiologicFunction"}, {"text": "ART", "type": "HealthCareActivity"}, {"text": "aged", "type": "PopulationGroup"}, {"text": "health provider", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Substantial levels of undisclosed HIV infection and ART use while on ART were observed , resulting in diagnosed HIV underestimated by 112 , 000 persons and ART coverage by 131 , 000 persons .

Example answer:
{"entities": [{"text": "HIV infection", "type": "BiologicFunction"}, {"text": "ART", "type": "HealthCareActivity"}, {"text": "persons", "type": "PopulationGroup"}]}

Input:
Sentence: Multivariate analysis determined factors associated with undisclosed HIV infection and ART use among persons on ART .

## Item MedMentions:test:1208
Example input:
Sentence: It is known that upregulation of these receptors is not due to a change in mRNA of these genes , however , more precise details on the process are still uncertain , with several plausible hypotheses describing how nAChRs are upregulated .

Example answer:
{"entities": [{"text": "upregulation", "type": "BiologicFunction"}, {"text": "receptors", "type": "Chemical"}, {"text": "mRNA", "type": "Chemical"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "nAChRs", "type": "Chemical"}, {"text": "upregulated", "type": "BiologicFunction"}]}

Example input:
Sentence: The PCR array analysis showed that CNM significantly upregulated about 7 % of all DNA damage - related genes .

Example answer:
{"entities": [{"text": "PCR array", "type": "ResearchActivity"}, {"text": "CNM", "type": "Chemical"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "DNA damage - related", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Genes with higher m6A methylation and lower expression levels at any particular stage were associated with the biological processes required for or unique to that stage .

Example answer:
{"entities": [{"text": "Genes", "type": "AnatomicalStructure"}, {"text": "m6A", "type": "Chemical"}, {"text": "methylation", "type": "BiologicFunction"}, {"text": "biological processes", "type": "BiologicFunction"}]}

Example input:
Sentence: Gene expression and apoptosis -associated protein levels were measured by reverse transcription - quantitative polymerase chain reaction and western blotting .

Example answer:
{"entities": [{"text": "Gene expression", "type": "BiologicFunction"}, {"text": "apoptosis -associated protein", "type": "Chemical"}, {"text": "reverse transcription - quantitative polymerase chain reaction", "type": "ResearchActivity"}, {"text": "western blotting", "type": "HealthCareActivity"}]}

Example input:
Sentence: We detected 1828 , 1296 and 1190 differentially expressed genes ( DEGs ) in the 4 , 24 and 48 h samples , respectively .

Example answer:
{"entities": [{"text": "detected", "type": "Finding"}, {"text": "differentially expressed", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "DEGs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The genes expression levels of follicle - stimulating hormone beta - subunit ( FSHR ) , insulin - like growth factor ( IGF - 1 ) , Activin , luteinizing hormone / choriogonadotropin receptor , bone morphogenetic protein receptor type IA , transforming growth factor beta receptor 1 , growth differentiation factor 9 , BCL2 - associated X protein ( BAX ) , and C - Myc were studied using real - time polymerase chain reaction .

Example answer:
{"entities": [{"text": "genes expression", "type": "BiologicFunction"}, {"text": "follicle - stimulating hormone beta - subunit", "type": "AnatomicalStructure"}, {"text": "FSHR", "type": "AnatomicalStructure"}, {"text": "insulin - like growth factor", "type": "AnatomicalStructure"}, {"text": "IGF - 1", "type": "AnatomicalStructure"}, {"text": "Activin", "type": "AnatomicalStructure"}, {"text": "luteinizing hormone / choriogonadotropin receptor", "type": "AnatomicalStructure"}, {"text": "bone morphogenetic protein receptor type IA", "type": "AnatomicalStructure"}, {"text": "transforming growth factor beta receptor 1", "type": "AnatomicalStructure"}, {"text": "growth differentiation factor 9", "type": "AnatomicalStructure"}, {"text": "BCL2 - associated X protein", "type": "AnatomicalStructure"}, {"text": "BAX", "type": "AnatomicalStructure"}, {"text": "C - Myc", "type": "AnatomicalStructure"}, {"text": "real - time polymerase chain reaction", "type": "ResearchActivity"}]}

Example input:
Sentence: RNA - seq analysis showed that hundreds of genes were upregulated in M2c macrophages compared to the M0 control , with thousands of alternative splicing events .

Example answer:
{"entities": [{"text": "RNA - seq analysis", "type": "HealthCareActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "macrophages", "type": "AnatomicalStructure"}, {"text": "alternative splicing", "type": "BiologicFunction"}]}

Example input:
Sentence: The qRT - PCR and Western blotting results confirmed the up - regulation of these four genes .

Example answer:
{"entities": [{"text": "qRT - PCR", "type": "ResearchActivity"}, {"text": "Western blotting", "type": "HealthCareActivity"}, {"text": "up - regulation", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Pathway analysis showed that upregulated genes were mainly enriched in the " B cell receptor signaling pathway " , " Cell cycle " and " NF - kappa B signaling pathway " , whereas downregulated genes were mainly enriched in the " Ribosome " , " FoxO signaling pathway " and " p53 signaling pathway " .

Example answer:
{"entities": [{"text": "Pathway analysis", "type": "IntellectualProduct"}, {"text": "upregulated genes", "type": "AnatomicalStructure"}, {"text": "B cell receptor signaling pathway", "type": "BiologicFunction"}, {"text": "Cell cycle", "type": "BiologicFunction"}, {"text": "downregulated genes", "type": "AnatomicalStructure"}, {"text": "Ribosome", "type": "AnatomicalStructure"}, {"text": "p53 signaling pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: 71 ) and up - regulated genes were 4503 and 228 , respectively .

Example answer:
{"entities": [{"text": "71", "type": "Eukaryote"}, {"text": "up - regulated", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Input:
Sentence: The genes measured were identified to be upregulated close to normal levels .

## Item MedMentions:test:1141
Example input:
Sentence: The purpose of this study was to assess bedside nurses ' perceived skills and attitudes about updated safety concepts and examine their impact on medication administration errors and adherence to safe medication administration practices .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "bedside nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "attitudes", "type": "BiologicFunction"}, {"text": "medication administration", "type": "HealthCareActivity"}, {"text": "practices", "type": "BiologicFunction"}]}

Example input:
Sentence: Participants made choices between hypothetical safety partnerships composed by experimentally varying 15 four - level partnership design attributes .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}]}

Example input:
Sentence: CONCLUSIONS : This study provides promising support for the PAT as a psychosocial screener for families of infants and older children across illness conditions .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "PAT", "type": "IntellectualProduct"}, {"text": "screener", "type": "HealthCareActivity"}, {"text": "illness", "type": "Finding"}]}

Example input:
Sentence: In this discussion , I consider this case from the perspective of respecting patients ' and families ' preferences around medical treatment and care .

Example answer:
{"entities": [{"text": "respecting patients ' and families ' preferences", "type": "HealthCareActivity"}, {"text": "medical treatment and care", "type": "HealthCareActivity"}]}

Example input:
Sentence: The Partnership for Health IT Patient Safety was formed to gather data , conduct analysis , educate , and disseminate safe practices for safer care using health information technology ( IT ) .

Example answer:
{"entities": [{"text": "Partnership", "type": "Organization"}, {"text": "Patient Safety", "type": "HealthCareActivity"}, {"text": "disseminate", "type": "SpatialConcept"}, {"text": "safe", "type": "SpatialConcept"}, {"text": "practices", "type": "BiologicFunction"}, {"text": "safer", "type": "SpatialConcept"}]}

Example input:
Sentence: 3 % ) comprised outpatients with higher education , who anticipated more benefits to safety partnerships , were more confident in their ability to contribute , and were more intent on participating .

Example answer:
{"entities": []}

Example input:
Sentence: They valued the opportunity to participate in point of service safety partnerships , such as identity and medication double checks , that might afford an immediate risk reduction .

Example answer:
{"entities": []}

Example input:
Sentence: The Partnership 1 ) reviewed 12 reported safety events , 2 ) solicited expert input , and 3 ) performed a systematic literature review ( 2010 to January 2015 ) to identify publications addressing frequency , perceptions / attitudes , patient safety risks , existing guidance , and potential interventions and mitigation practices .

Example answer:
{"entities": [{"text": "Partnership", "type": "Organization"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "systematic literature review", "type": "IntellectualProduct"}, {"text": "publications", "type": "IntellectualProduct"}, {"text": "perceptions", "type": "BiologicFunction"}, {"text": "attitudes", "type": "BiologicFunction"}, {"text": "patient safety", "type": "HealthCareActivity"}, {"text": "guidance", "type": "HealthCareActivity"}, {"text": "practices", "type": "BiologicFunction"}]}

Example input:
Sentence: Participants preferred an approach to safety based on partnerships between patients and staff rather than a model delegating responsibility for safety to hospital staff .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "staff", "type": "ProfessionalOrOccupationalGroup"}, {"text": "hospital staff", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: We used a discrete choice conjoint experiment to model the safety partnership preferences of 1 , 084 patients or those such as parents acting on their behalf .

Example answer:
{"entities": [{"text": "conjoint experiment", "type": "ResearchActivity"}]}

Input:
Sentence: The objective of this study is to understand the safety partnership preferences of patients and their families .

## Item MedMentions:test:996
Example input:
Sentence: With the additional discriminators of smoking history , sex , and nodule location , significant risk stratification was observed .

Example answer:
{"entities": [{"text": "additional discriminators", "type": "IntellectualProduct"}, {"text": "smoking history", "type": "Finding"}, {"text": "nodule", "type": "AnatomicalStructure"}, {"text": "location", "type": "SpatialConcept"}, {"text": "stratification", "type": "ResearchActivity"}]}

Example input:
Sentence: An HIV - tailored quit - smoking counselling pilot intervention targeting depressive symptoms plus Nicotine Replacement Therapy Cardiovascular disease ( CVD ) rates among people living with HIV / AIDS ( PHAs ) are high .

Example answer:
{"entities": [{"text": "HIV", "type": "Virus"}, {"text": "tailored", "type": "HealthCareActivity"}, {"text": "counselling", "type": "HealthCareActivity"}, {"text": "pilot", "type": "ResearchActivity"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "depressive symptoms", "type": "Finding"}, {"text": "Nicotine Replacement Therapy", "type": "HealthCareActivity"}, {"text": "Cardiovascular disease", "type": "BiologicFunction"}, {"text": "CVD", "type": "BiologicFunction"}, {"text": "people", "type": "PopulationGroup"}]}

Example input:
Sentence: The incidence rate of testing was higher among Black MSM than White MSM ( IDRR : 1 . 3 , 95 % confidence interval CI [ 1 . 1 , 1 . 5 ] ) and higher among MSM who reported 3 + condomless anal intercourse partners ( CAI ) than MSM who reported no CAI ( IDRR : 1 . 6 , 95 % CI [ 1 . 3 , 2 . 0 ] ) .

Example answer:
{"entities": [{"text": "Black", "type": "PopulationGroup"}, {"text": "MSM", "type": "PopulationGroup"}, {"text": "White", "type": "PopulationGroup"}, {"text": "condomless anal intercourse partners", "type": "PopulationGroup"}, {"text": "CAI", "type": "PopulationGroup"}, {"text": "no", "type": "Finding"}]}

Example input:
Sentence: This population - based study evaluates the association between groin hernia repair and tobacco use .

Example answer:
{"entities": [{"text": "population - based study", "type": "ResearchActivity"}, {"text": "evaluates", "type": "HealthCareActivity"}, {"text": "groin hernia repair", "type": "HealthCareActivity"}, {"text": "tobacco", "type": "Chemical"}]}

Example input:
Sentence: In addition to the detection of cocaine , these analyses also provided evidence of nicotine and caffeine intake .

Example answer:
{"entities": [{"text": "detection", "type": "Finding"}, {"text": "cocaine", "type": "Chemical"}, {"text": "analyses", "type": "ResearchActivity"}, {"text": "nicotine", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}]}

Example input:
Sentence: Due to a low smoking prevalence in our study population , we had limited power to detect effect modification between dietary NEAC and smoking on a multiplicative or additive scale .

Example answer:
{"entities": [{"text": "dietary", "type": "Food"}, {"text": "NEAC", "type": "HealthCareActivity"}]}

Example input:
Sentence: We evaluated the evidence for association between a manually curated set of genes and nicotine behaviors in European and African Americans .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: In African Surinamese , the associations were positive for current smoking , nicotine , and alcohol dependence ( odds ratios of 1 . 16 ; 95 % confidence interval : 1 . 06 - 1 . 27 , 1 .

Example answer:
{"entities": [{"text": "African", "type": "SpatialConcept"}, {"text": "Surinamese", "type": "PopulationGroup"}, {"text": "positive", "type": "Finding"}, {"text": "nicotine", "type": "BiologicFunction"}, {"text": "alcohol dependence", "type": "BiologicFunction"}]}

Example input:
Sentence: However , no appreciable improvement was observed with regard to smoking status , obesity or HbA1c control .

Example answer:
{"entities": [{"text": "smoking status", "type": "ClinicalAttribute"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "HbA1c", "type": "Chemical"}]}

Example input:
Sentence: Patients were compared based on age , sex , body mass index , tobacco use , presence of diabetes , and Charlson Comorbidity Index .

Example answer:
{"entities": [{"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Input:
Sentence: No significant findings were detected among sex , race , nicotine use , body mass index , or other concomitant procedures of interest .

## Item MedMentions:test:1219
Example input:
Sentence: Diffusion imaging with nCPMG SS - FSE gives similar SNR to an EPI acquisition , though apparent diffusion coefficient values are higher than seen with EPI .

Example answer:
{"entities": [{"text": "Diffusion imaging", "type": "HealthCareActivity"}, {"text": "nCPMG", "type": "Finding"}, {"text": "SS - FSE", "type": "HealthCareActivity"}, {"text": "EPI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Imaging based on this property has shown a substantial contrast - to - noise ratio improvement ( up to 5 fold , p < 0 .

Example answer:
{"entities": [{"text": "Imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: Optical simulations ( in terms of through - focus Strehl ratio from Hartmann - Shack aberrometry ) accurately predicted the pattern producing the highest perceived quality in 4 out of 5 patients , both for far and near vision .

Example answer:
{"entities": [{"text": "Optical simulations", "type": "Finding"}, {"text": "pattern", "type": "SpatialConcept"}, {"text": "vision", "type": "BiologicFunction"}]}

Example input:
Sentence: The F - measure for L * a * b * colour space ( 0 . 8847 ) provides the best statistical result as compared to grey , HSI , YCbCr , YIQ and XYZ colour space .

Example answer:
{"entities": [{"text": "colour space", "type": "IntellectualProduct"}]}

Example input:
Sentence: Here , signal - to - noise ratio ( SNR ) comparisons between EPI and nCPMG SS - FSE acquisitions and reconstruction techniques give similar values .

Example answer:
{"entities": [{"text": "EPI", "type": "HealthCareActivity"}, {"text": "nCPMG", "type": "Finding"}, {"text": "SS - FSE", "type": "HealthCareActivity"}]}

Example input:
Sentence: Binocular UIVA and binocular UNVA are better in Group A ( p = .00 , p = .00 ) .

Example answer:
{"entities": [{"text": "Binocular", "type": "BiologicFunction"}, {"text": "binocular", "type": "BiologicFunction"}]}

Example input:
Sentence: With doped Gd species and strong tunable NIR absorbance , Gd : CuS @ BSA NPs demonstrate prominent tumor - contrasted imaging performance both on the photoacoustic and magnetic resonance imaging modalities .

Example answer:
{"entities": [{"text": "doped Gd species", "type": "Chemical"}, {"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "BSA", "type": "Chemical"}, {"text": "tumor - contrasted imaging", "type": "HealthCareActivity"}, {"text": "photoacoustic", "type": "HealthCareActivity"}, {"text": "magnetic resonance imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: Under photopic and scotopic conditions , contrast sensitivity results were decreased in Group A , especially at high spatial frequencies .

Example answer:
{"entities": [{"text": "photopic", "type": "BiologicFunction"}, {"text": "scotopic conditions", "type": "BiologicFunction"}]}

Example input:
Sentence: The best mono - spectrum energy with the optimal CNR of the perforating artery was 63 keV .

Example answer:
{"entities": [{"text": "perforating artery", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Both mono - spectrum images of Group A and polychromatic images of Group B were used to reconstruct maximum intensity projection ( MIP ) and volume rendering ( VR ) images of the perforating artery , respectively .

Example answer:
{"entities": [{"text": "mono - spectrum images", "type": "IntellectualProduct"}, {"text": "polychromatic images", "type": "IntellectualProduct"}, {"text": "images", "type": "IntellectualProduct"}, {"text": "perforating artery", "type": "AnatomicalStructure"}]}

Input:
Sentence: The best mono - spectrum images of Group A were selected according to the optimal contrast to noise ratio ( CNR ) .

## Item MedMentions:test:1052
Example input:
Sentence: natIn - BnDTPA - exendin ( 9 - 39 ) exhibited a high affinity for GLP - 1R ( IC50 = 2 . 5nM ) , stability in plasma , and a specific activity that improved following reactions with a solvent and solubilizer .

Example answer:
{"entities": [{"text": "natIn - BnDTPA - exendin ( 9 - 39 )", "type": "Chemical"}, {"text": "GLP - 1R", "type": "Chemical"}, {"text": "plasma", "type": "BodySubstance"}, {"text": "solvent", "type": "Chemical"}, {"text": "solubilizer", "type": "Chemical"}]}

Example input:
Sentence: Although HIF2α was classically considered undruggable , structural and chemical work by Rick Bruick and Kevin Gardner at University of Texas Southwestern laid the foundation for the development of small molecule direct HIF2α antagonists ( PT2385 and the related tool compound PT2399 ) by Peloton Therapeutics that block the dimerization of HIF2α with its partner protein ARNT1 .

Example answer:
{"entities": [{"text": "HIF2α", "type": "Chemical"}, {"text": "University of Texas Southwestern", "type": "Organization"}, {"text": "small molecule", "type": "Chemical"}, {"text": "HIF2α antagonists", "type": "Chemical"}, {"text": "PT2385", "type": "Chemical"}, {"text": "PT2399", "type": "Chemical"}, {"text": "Peloton Therapeutics", "type": "Organization"}, {"text": "dimerization", "type": "BiologicFunction"}, {"text": "protein ARNT1", "type": "Chemical"}]}

Example input:
Sentence: MDCK cells were used to examine the transport mechanisms of HDND - 7 in vitro , and a rat in situ intestinal perfusion model was used to characterize the absorption of HDND - 7 .

Example answer:
{"entities": [{"text": "MDCK cells", "type": "AnatomicalStructure"}, {"text": "transport mechanisms", "type": "BiologicFunction"}, {"text": "HDND - 7", "type": "Chemical"}, {"text": "rat", "type": "Eukaryote"}, {"text": "in situ intestinal perfusion", "type": "HealthCareActivity"}]}

Example input:
Sentence: Moreover , HDND - 7 showed pH - dependent and TEER - independent transport in both directions .

Example answer:
{"entities": [{"text": "HDND - 7", "type": "Chemical"}, {"text": "independent", "type": "Finding"}, {"text": "transport", "type": "BiologicFunction"}, {"text": "directions", "type": "SpatialConcept"}]}

Example input:
Sentence: The transport of HDND - 7 was significantly reduced at 4 ° C or in the presence of NaN3 .

Example answer:
{"entities": [{"text": "transport", "type": "BiologicFunction"}, {"text": "HDND - 7", "type": "Chemical"}, {"text": "presence", "type": "Finding"}, {"text": "NaN3", "type": "Chemical"}]}

Example input:
Sentence: The concentration of HDND - 7 was determined by HPLC .

Example answer:
{"entities": [{"text": "HDND - 7", "type": "Chemical"}, {"text": "HPLC", "type": "HealthCareActivity"}]}

Example input:
Sentence: Intestinal transport of HDND - 7 , a novel hesperetin derivative , in in vitro MDCK cell and in situ single - pass intestinal perfusion models 1 .

Example answer:
{"entities": [{"text": "Intestinal", "type": "AnatomicalStructure"}, {"text": "transport", "type": "BiologicFunction"}, {"text": "HDND - 7", "type": "Chemical"}, {"text": "hesperetin", "type": "Chemical"}, {"text": "MDCK cell", "type": "AnatomicalStructure"}, {"text": "in situ single - pass intestinal perfusion", "type": "HealthCareActivity"}, {"text": "models", "type": "IntellectualProduct"}]}

Example input:
Sentence: In MDCK cells , HDND - 7 was effectively absorbed in a concentration - dependent manner in both directions .

Example answer:
{"entities": [{"text": "MDCK cells", "type": "AnatomicalStructure"}, {"text": "HDND - 7", "type": "Chemical"}, {"text": "directions", "type": "SpatialConcept"}]}

Example input:
Sentence: The in situ intestinal perfusion study indicated HDND - 7 was well - absorbed in four intestinal segments .

Example answer:
{"entities": [{"text": "in situ intestinal perfusion", "type": "HealthCareActivity"}, {"text": "HDND - 7", "type": "Chemical"}, {"text": "intestinal", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In summary , all results indicated that HDND - 7 might be absorbed mainly by passive diffusion via transcellular pathway , MRP2 but P - gp may participate in the efflux of HDND - 7 .

Example answer:
{"entities": [{"text": "HDND - 7", "type": "Chemical"}, {"text": "transcellular pathway", "type": "BiologicFunction"}, {"text": "MRP2", "type": "Chemical"}, {"text": "P - gp", "type": "Chemical"}, {"text": "efflux", "type": "BiologicFunction"}]}

Input:
Sentence: HDND - 7 , a derivative of HDND , has better solubility and high bioavailability .

## Item MedMentions:test:1002
Example input:
Sentence: Finally , using bioinformatics tools , pathway analyses of differentially expressed MS - identified proteins find that acute phase , inflammatory and immune responses as well as oxidative stress are likely involved in the response to contamination , suggesting a physiological perturbation , but that does not necessarily lead to a toxic effect .

Example answer:
{"entities": [{"text": "pathway analyses", "type": "IntellectualProduct"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "MS", "type": "HealthCareActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "immune responses", "type": "BiologicFunction"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "toxic effect", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Analysis of the macrophage - conditioned media for secretion of matrix - remodeling proteins showed that M2c macrophages secreted higher levels of MMP7 , MMP8 , and TIMP1 compared to the other phenotypes .

Example answer:
{"entities": [{"text": "macrophage", "type": "AnatomicalStructure"}, {"text": "conditioned media", "type": "Chemical"}, {"text": "secretion", "type": "BiologicFunction"}, {"text": "proteins", "type": "Chemical"}, {"text": "M2c macrophages", "type": "AnatomicalStructure"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "MMP7", "type": "Chemical"}, {"text": "MMP8", "type": "Chemical"}, {"text": "TIMP1", "type": "Chemical"}]}

Example input:
Sentence: Reduction of extracellular matrix components were mediated via TGFβ signaling pathway inhibition due to downregulation of TGFβ1 , COL1A1 , COL3A1 , HAS2 , HAS3 expression levels .

Example answer:
{"entities": [{"text": "extracellular matrix components", "type": "AnatomicalStructure"}, {"text": "downregulation", "type": "BiologicFunction"}, {"text": "TGFβ1", "type": "AnatomicalStructure"}, {"text": "COL1A1", "type": "AnatomicalStructure"}, {"text": "COL3A1", "type": "AnatomicalStructure"}, {"text": "HAS2", "type": "AnatomicalStructure"}, {"text": "HAS3", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}]}

Example input:
Sentence: Pro - inflammatory cytokines upregulated SOX5 and RANKL expression in both primary RA SF and the rheumatoid synovial fibroblast cell line , MH7A .

Example answer:
{"entities": [{"text": "cytokines", "type": "Chemical"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "SOX5", "type": "Chemical"}, {"text": "RANKL", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "SF", "type": "AnatomicalStructure"}, {"text": "MH7A", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Up - regulated proteins were enriched in GO terms related to humoral immune response , predominantly innate immunity ( C4b , lactotransferrin , protein S100 - A8 , cathelicidin , myeloperoxidase ) and extracellular matrix reorganization ( e . g .

Example answer:
{"entities": [{"text": "Up - regulated", "type": "BiologicFunction"}, {"text": "proteins", "type": "Chemical"}, {"text": "GO", "type": "IntellectualProduct"}, {"text": "humoral immune response", "type": "BiologicFunction"}, {"text": "C4b", "type": "Chemical"}, {"text": "lactotransferrin", "type": "Chemical"}, {"text": "protein S100 - A8", "type": "Chemical"}, {"text": "cathelicidin", "type": "Chemical"}, {"text": "myeloperoxidase", "type": "Chemical"}, {"text": "extracellular matrix", "type": "AnatomicalStructure"}, {"text": "reorganization", "type": "BiologicFunction"}]}

Example input:
Sentence: Total RNA and protein were isolated from muscle tissue to determine the mRNA levels of IL - 6 , IL - 1β , TNF - α , vascular cell adhesion molecule ( VCAM ) - 1 , and intercellular adhesion molecule ( ICAM ) - 1 , and the protein level of phosphorylated p38 mitogen - activated protein kinase ( MAPK ) .

Example answer:
{"entities": [{"text": "RNA", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}, {"text": "muscle tissue", "type": "AnatomicalStructure"}, {"text": "mRNA", "type": "Chemical"}, {"text": "levels of IL - 6", "type": "HealthCareActivity"}, {"text": "IL - 1β", "type": "HealthCareActivity"}, {"text": "TNF - α", "type": "HealthCareActivity"}, {"text": "vascular cell adhesion molecule ( VCAM ) - 1", "type": "HealthCareActivity"}, {"text": "intercellular adhesion molecule ( ICAM ) - 1", "type": "HealthCareActivity"}, {"text": "protein level", "type": "Finding"}, {"text": "phosphorylated p38 mitogen - activated protein kinase", "type": "Chemical"}, {"text": "MAPK", "type": "Chemical"}]}

Example input:
Sentence: RNA - seq analysis showed that hundreds of genes were upregulated in M2c macrophages compared to the M0 control , with thousands of alternative splicing events .

Example answer:
{"entities": [{"text": "RNA - seq analysis", "type": "HealthCareActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "macrophages", "type": "AnatomicalStructure"}, {"text": "alternative splicing", "type": "BiologicFunction"}]}

Example input:
Sentence: AC showed higher initial BMP4 , pSmad1 / 5 / 9 and SOX9 protein levels , a faster ( re - ) differentiation but a similar decline of pSmad2 / 3 - and pSmad1 / 5 / 9 - signalling versus MSC - cultures .

Example answer:
{"entities": [{"text": "AC", "type": "AnatomicalStructure"}, {"text": "BMP4", "type": "Chemical"}, {"text": "pSmad1", "type": "Chemical"}, {"text": "5", "type": "Chemical"}, {"text": "9", "type": "Chemical"}, {"text": "SOX9", "type": "Chemical"}, {"text": "protein levels", "type": "Finding"}, {"text": "( re - ) differentiation", "type": "BiologicFunction"}, {"text": "pSmad2", "type": "Chemical"}, {"text": "3", "type": "Chemical"}, {"text": "signalling", "type": "BiologicFunction"}, {"text": "MSC", "type": "AnatomicalStructure"}, {"text": "cultures", "type": "HealthCareActivity"}]}

Example input:
Sentence: In ileum , five genes were down - regulated and six genes were unchanged in SBS vs sham animals .

Example answer:
{"entities": [{"text": "ileum", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "down - regulated", "type": "BiologicFunction"}, {"text": "unchanged", "type": "Finding"}, {"text": "SBS", "type": "BiologicFunction"}, {"text": "sham", "type": "HealthCareActivity"}, {"text": "animals", "type": "Eukaryote"}]}

Example input:
Sentence: Surgery alone did not induce an inflammatory cell response , as evidenced by the lack of leukocyte infiltration in the sham groups .

Example answer:
{"entities": [{"text": "Surgery", "type": "HealthCareActivity"}, {"text": "inflammatory cell response", "type": "BiologicFunction"}, {"text": "leukocyte infiltration", "type": "Finding"}, {"text": "sham", "type": "HealthCareActivity"}]}

Input:
Sentence: Analysis of 165 inflammatory cytokines and extracellular matrix factors in sham revealed that a minor gene response was initiated but not translated to protein levels .

## Item MedMentions:test:884
Example input:
Sentence: Age at the first visit as well as PNES onset was younger in the ID than in the non - ID group ( t = 2 . 651 , p = 0 . 009 ; t = 3 . 528 , p = 0 . 001 , respectively ) .

Example answer:
{"entities": [{"text": "visit", "type": "HealthCareActivity"}, {"text": "PNES", "type": "BiologicFunction"}, {"text": "ID", "type": "BiologicFunction"}, {"text": "non - ID", "type": "Finding"}]}

Example input:
Sentence: When seizure onset occurred in childhood ( 21 patients ) , terrifying hallucinations associated with focal motor seizures , often sleep - related ( 8 patients ) , or dyscognitive seizures ( 13 patients ) , were prominent features , often evolving into epileptic encephalopathy associated with non - convulsive status epilepticus ( 11 patients ) .

Example answer:
{"entities": [{"text": "terrifying", "type": "Finding"}, {"text": "hallucinations", "type": "BiologicFunction"}, {"text": "focal motor seizures", "type": "BiologicFunction"}, {"text": "sleep - related", "type": "BiologicFunction"}, {"text": "dyscognitive seizures", "type": "Finding"}, {"text": "epileptic encephalopathy", "type": "BiologicFunction"}, {"text": "non - convulsive status epilepticus", "type": "BiologicFunction"}]}

Example input:
Sentence: In the long - term , progressive stabilization of drug resistant epilepsy associated with non - convulsive status epilepticus , focal seizures with motor and autonomic features , and eyelid myoclonia were noticed .

Example answer:
{"entities": [{"text": "stabilization", "type": "HealthCareActivity"}, {"text": "drug resistant epilepsy", "type": "BiologicFunction"}, {"text": "non - convulsive status epilepticus", "type": "BiologicFunction"}, {"text": "focal seizures", "type": "Finding"}, {"text": "motor", "type": "ClinicalAttribute"}, {"text": "autonomic features", "type": "Finding"}, {"text": "eyelid myoclonia", "type": "BiologicFunction"}]}

Example input:
Sentence: UTLE patients more frequently displayed maximal epileptogenicity in hippocampal structures , whereas BTLE patients had maximal values in subhippocampal areas ( entorhinal cortex , temporal pole , parahippocampal cortex ) .

Example answer:
{"entities": [{"text": "UTLE", "type": "BiologicFunction"}, {"text": "hippocampal structures", "type": "AnatomicalStructure"}, {"text": "BTLE", "type": "BiologicFunction"}, {"text": "subhippocampal areas", "type": "SpatialConcept"}, {"text": "entorhinal cortex", "type": "AnatomicalStructure"}, {"text": "temporal pole", "type": "AnatomicalStructure"}, {"text": "parahippocampal cortex", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Electroencephalogram ( EEG ) revealed 2 Hz rhythmic sharp - and - waves continuously , which suggested nonconvulsive status epilepticus ( NCSE ) .

Example answer:
{"entities": [{"text": "Electroencephalogram", "type": "Finding"}, {"text": "EEG", "type": "Finding"}, {"text": "rhythmic sharp - and - waves", "type": "Finding"}, {"text": "nonconvulsive status epilepticus", "type": "BiologicFunction"}, {"text": "NCSE", "type": "BiologicFunction"}]}

Example input:
Sentence: Psychogenic non - epileptic seizure in patients with intellectual disability with special focus on choice of therapeutic intervention There have been a number of studies exploring treatments for psychogenic non - epileptic seizure ( PNES ) but largely neglecting the sizable subgroup of patients with intellectual disability ( ID ) .

Example answer:
{"entities": [{"text": "Psychogenic non - epileptic seizure", "type": "BiologicFunction"}, {"text": "intellectual disability", "type": "BiologicFunction"}, {"text": "therapeutic intervention", "type": "HealthCareActivity"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "treatments", "type": "HealthCareActivity"}, {"text": "psychogenic non - epileptic seizure", "type": "BiologicFunction"}, {"text": "PNES", "type": "BiologicFunction"}, {"text": "neglecting", "type": "Finding"}, {"text": "subgroup", "type": "IntellectualProduct"}, {"text": "ID", "type": "BiologicFunction"}]}

Example input:
Sentence: In conclusion , although overlap exists , the features of PNSC generally appear similar to neurally mediated syncope , while the features of PNES generally appear similar to epileptic seizures .

Example answer:
{"entities": [{"text": "PNSC", "type": "BiologicFunction"}, {"text": "neurally mediated syncope", "type": "BiologicFunction"}, {"text": "epileptic seizures", "type": "BiologicFunction"}]}

Example input:
Sentence: Cohorts with psychogenic nonsyncopal collapse ( n = 40 ) and PNES ( n = 40 ) did not differ in age ( 15 . 5±2 .

Example answer:
{"entities": [{"text": "Cohorts", "type": "PopulationGroup"}, {"text": "psychogenic nonsyncopal collapse", "type": "BiologicFunction"}]}

Example input:
Sentence: Psychogenic nonsyncopal collapse events were briefer than PNES events ( median : 45 versus 201 .

Example answer:
{"entities": [{"text": "Psychogenic nonsyncopal collapse", "type": "BiologicFunction"}]}

Example input:
Sentence: Psychogenic nonsyncopal collapse and PNES likely represent similar disorders that differ primarily by clinical semiologies and referral patterns .

Example answer:
{"entities": [{"text": "Psychogenic nonsyncopal collapse", "type": "BiologicFunction"}, {"text": "disorders", "type": "BiologicFunction"}]}

Input:
Sentence: Comparison of semiologies between tilt - induced psychogenic nonsyncopal collapse and psychogenic nonepileptic seizures We sought to characterize the clinical features of tilt - induced psychogenic nonsyncopal collapse ( PNSC ) from a cohort of young patients and to compare the semiologies between PNSC and EEG -confirmed psychogenic nonepileptic seizures ( PNES ) .

## Item MedMentions:test:1151
Example input:
Sentence: Because the influx of extracellular Zn ( 2 + ) , which originates in presynaptic Zn ( 2 + ) release , is involved in LTP at Schaffer collateral - CA1 pyramidal cell synapses , synapse -dependent Zn ( 2 + ) dynamics may be involved in plasticity of postsynaptic CA1 pyramidal cells .

Example answer:
{"entities": [{"text": "influx", "type": "BiologicFunction"}, {"text": "extracellular", "type": "AnatomicalStructure"}, {"text": "Zn ( 2 + )", "type": "Chemical"}, {"text": "presynaptic Zn ( 2 + ) release", "type": "BiologicFunction"}, {"text": "LTP", "type": "BiologicFunction"}, {"text": "Schaffer collateral", "type": "AnatomicalStructure"}, {"text": "CA1 pyramidal cell synapses", "type": "AnatomicalStructure"}, {"text": "synapse", "type": "SpatialConcept"}, {"text": "plasticity", "type": "BiologicFunction"}, {"text": "CA1 pyramidal cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Field postsynaptic potentials ( fPSPs ) were chronically evoked in perforant pathway - hippocampal CA1 ( PP - CA1 ) , CA1 - subiculum ( CA1 - SUB ) , CA1 - medial prefrontal cortex ( CA1 - mPFC ) , mPFC - nucleus accumbens ( mPFC - NAc ) , and mPFC - basolateral amygdala ( mPFC - BLA ) synapses during lever IN and lever OUT situations .

Example answer:
{"entities": [{"text": "Field postsynaptic potentials", "type": "BiologicFunction"}, {"text": "fPSPs", "type": "BiologicFunction"}, {"text": "perforant pathway", "type": "AnatomicalStructure"}, {"text": "hippocampal CA1", "type": "SpatialConcept"}, {"text": "PP - CA1", "type": "SpatialConcept"}, {"text": "CA1", "type": "SpatialConcept"}, {"text": "subiculum", "type": "AnatomicalStructure"}, {"text": "SUB", "type": "AnatomicalStructure"}, {"text": "medial prefrontal cortex", "type": "AnatomicalStructure"}, {"text": "mPFC", "type": "AnatomicalStructure"}, {"text": "nucleus accumbens", "type": "AnatomicalStructure"}, {"text": "NAc", "type": "AnatomicalStructure"}, {"text": "basolateral amygdala", "type": "AnatomicalStructure"}, {"text": "BLA", "type": "AnatomicalStructure"}, {"text": "synapses", "type": "SpatialConcept"}]}

Example input:
Sentence: These findings may explain , in part , observations from in vivo experiments that ventral tegmental area neurons tend to exhibit longer aversive pauses relative to SNc neurons .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "ventral tegmental area", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "aversive pauses", "type": "HealthCareActivity"}, {"text": "SNc", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Even in rat brain slices bathed in CaEDTA in ACSF , intracellular Zn ( 2 + ) level , which was measured with intracellular ZnAF - 2 , was increased in the stratum lacunosum - moleculare where perforant pathway - CA1 pyramidal cell synapses were contained after tetanic stimulation .

Example answer:
{"entities": [{"text": "rat brain slices", "type": "AnatomicalStructure"}, {"text": "CaEDTA", "type": "Chemical"}, {"text": "ACSF", "type": "Chemical"}, {"text": "intracellular", "type": "AnatomicalStructure"}, {"text": "Zn ( 2 + )", "type": "Chemical"}, {"text": "ZnAF - 2", "type": "Chemical"}, {"text": "perforant pathway", "type": "AnatomicalStructure"}, {"text": "CA1 pyramidal cell synapses", "type": "AnatomicalStructure"}, {"text": "tetanic stimulation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Bassoon Controls Presynaptic Autophagy through Atg5 Mechanisms regulating the surveillance and clearance of synaptic proteins are not well understood .

Example answer:
{"entities": [{"text": "Bassoon", "type": "Chemical"}, {"text": "Presynaptic", "type": "AnatomicalStructure"}, {"text": "Autophagy", "type": "BiologicFunction"}, {"text": "Atg5", "type": "Chemical"}, {"text": "clearance of", "type": "ClinicalAttribute"}, {"text": "synaptic proteins", "type": "Chemical"}]}

Example input:
Sentence: Moreover , using a conditional anterograde axonal tract - tracing approach , we found that OB A2AR neurons innervate the piriform cortex and olfactory tubercle .

Example answer:
{"entities": [{"text": "anterograde axonal tract - tracing approach", "type": "ResearchActivity"}, {"text": "OB", "type": "AnatomicalStructure"}, {"text": "A2AR", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "piriform cortex", "type": "AnatomicalStructure"}, {"text": "olfactory tubercle", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Importantly , Atg5 LOF as well as targeting an Atg5 - binding peptide derived from Bassoon inhibited presynaptic autophagy in boutons lacking Piccolo and Bassoon , providing insights into the molecular mechanisms regulating presynaptic autophagy .

Example answer:
{"entities": [{"text": "Atg5", "type": "Chemical"}, {"text": "LOF", "type": "Finding"}, {"text": "binding peptide", "type": "BiologicFunction"}, {"text": "Bassoon", "type": "Chemical"}, {"text": "presynaptic", "type": "AnatomicalStructure"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "boutons", "type": "AnatomicalStructure"}, {"text": "Piccolo", "type": "Chemical"}, {"text": "regulating", "type": "BiologicFunction"}]}

Example input:
Sentence: Surprisingly , gain or loss of function ( LOF ) of Bassoon alone suppressed or enhanced presynaptic autophagy , respectively , implying a fundamental role for Bassoon in the local regulation of presynaptic autophagy .

Example answer:
{"entities": [{"text": "loss of function", "type": "Finding"}, {"text": "LOF", "type": "Finding"}, {"text": "Bassoon", "type": "Chemical"}, {"text": "presynaptic", "type": "AnatomicalStructure"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "local regulation", "type": "BiologicFunction"}]}

Example input:
Sentence: Presynaptic enrichment is consistent with the established importance of protecting presynaptic sites from depletion of DCV cargo .

Example answer:
{"entities": [{"text": "Presynaptic", "type": "AnatomicalStructure"}, {"text": "presynaptic", "type": "AnatomicalStructure"}, {"text": "sites", "type": "SpatialConcept"}, {"text": "DCV", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Here we report that the destruction of SVs in boutons lacking Piccolo and Bassoon was associated with the induction of presynaptic autophagy , a process that depended on poly - ubiquitination , but not the E3 ubiquitin ligase Siah1 .

Example answer:
{"entities": [{"text": "SVs", "type": "AnatomicalStructure"}, {"text": "boutons", "type": "AnatomicalStructure"}, {"text": "Piccolo", "type": "Chemical"}, {"text": "Bassoon", "type": "Chemical"}, {"text": "presynaptic", "type": "AnatomicalStructure"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "ubiquitination", "type": "BiologicFunction"}, {"text": "E3 ubiquitin ligase", "type": "Chemical"}, {"text": "Siah1", "type": "Chemical"}]}

Input:
Sentence: Occupancy in boutons exceeds that at nearby extrasynaptic axonal sites by approximately threefold , revealing significant local presynaptic enrichment .

## Item MedMentions:test:1282
Example input:
Sentence: Mey . ) Schischk An orange - coloured , aerobic , motile and short - rods bacterial strain , designated EGI 6500337 T , was isolated from the surface - sterilized root of a halophyte Anabasis elatior ( C .

Example answer:
{"entities": [{"text": "Mey . ) Schischk", "type": "Eukaryote"}, {"text": "short - rods bacterial strain", "type": "Bacterium"}, {"text": "EGI 6500337 T", "type": "Bacterium"}, {"text": "root", "type": "Eukaryote"}, {"text": "halophyte", "type": "Eukaryote"}, {"text": "Anabasis elatior ( C .", "type": "Eukaryote"}]}

Example input:
Sentence: While the role of Wg and Dpp has been studied in a wide range of arthropods representing all main branches , that is , Pancrustacea ( = Hexapoda + Crustacea ) , Myriapoda and Chelicerata , investigation of the potential role of EGFR - signaling is restricted to insects ( Hexapoda ) .

Example answer:
{"entities": [{"text": "Wg", "type": "Chemical"}, {"text": "Dpp", "type": "Chemical"}, {"text": "studied", "type": "ResearchActivity"}, {"text": "arthropods", "type": "Eukaryote"}, {"text": "Pancrustacea", "type": "Eukaryote"}, {"text": "Hexapoda", "type": "Eukaryote"}, {"text": "Crustacea", "type": "Eukaryote"}, {"text": "Myriapoda", "type": "Eukaryote"}, {"text": "Chelicerata", "type": "Eukaryote"}, {"text": "EGFR - signaling", "type": "BiologicFunction"}, {"text": "insects", "type": "Eukaryote"}]}

Example input:
Sentence: aeruginosa .

Example answer:
{"entities": [{"text": "aeruginosa", "type": "Bacterium"}]}

Example input:
Sentence: aeruginosa .

Example answer:
{"entities": [{"text": "aeruginosa", "type": "Bacterium"}]}

Example input:
Sentence: aeruginosa .

Example answer:
{"entities": [{"text": "aeruginosa", "type": "Bacterium"}]}

Example input:
Sentence: A comprehensive study of the changes in enzymatic activities and precursor pool sizes have been previously reported for the mosquito Aedes aegypti JH biosynthesis pathway .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "enzymatic activities", "type": "BiologicFunction"}, {"text": "mosquito", "type": "Eukaryote"}, {"text": "Aedes aegypti", "type": "Eukaryote"}, {"text": "JH", "type": "Chemical"}, {"text": "biosynthesis", "type": "BiologicFunction"}, {"text": "pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: An abdominal ectopic pregnancy ( AEP ) is a rare form of EP , and there are few reports of an AEP after IVF / ICSI .

Example answer:
{"entities": [{"text": "abdominal", "type": "SpatialConcept"}, {"text": "ectopic pregnancy", "type": "BiologicFunction"}, {"text": "( AEP )", "type": "BiologicFunction"}, {"text": "EP", "type": "BiologicFunction"}, {"text": "reports", "type": "IntellectualProduct"}, {"text": "AEP", "type": "BiologicFunction"}, {"text": "IVF", "type": "HealthCareActivity"}, {"text": "ICSI", "type": "HealthCareActivity"}]}

Example input:
Sentence: aestivum ssp .

Example answer:
{"entities": [{"text": "aestivum ssp .", "type": "Eukaryote"}]}

Example input:
Sentence: Mosquitoes belonging to subgenus Stegomyia of Aedes , particularly Aedes aegypti , are considered the primary vectors of ZIKV .

Example answer:
{"entities": [{"text": "Mosquitoes", "type": "Eukaryote"}, {"text": "Stegomyia of Aedes", "type": "Eukaryote"}, {"text": "Aedes aegypti", "type": "Eukaryote"}, {"text": "primary vectors", "type": "Eukaryote"}, {"text": "ZIKV", "type": "Virus"}]}

Example input:
Sentence: In contrast , Ae . aegypti ensured high viral dissemination and moderate to very high transmission .

Example answer:
{"entities": [{"text": "Ae . aegypti", "type": "Eukaryote"}, {"text": "viral dissemination", "type": "Finding"}, {"text": "transmission", "type": "BiologicFunction"}]}

Input:
Sentence: aegypti .

## Item MedMentions:test:847
Example input:
Sentence: We conducted a population - based case - control study of 5 , 950 , 391 patients using the 2014 Healthcare Cost and Utilization Project ( HCUP ) , Nationwide Inpatient Survey ( NIS ) discharge records of patients 18 years and older .

Example answer:
{"entities": [{"text": "population - based case - control study", "type": "ResearchActivity"}, {"text": "Nationwide Inpatient Survey", "type": "IntellectualProduct"}, {"text": "NIS", "type": "IntellectualProduct"}, {"text": "discharge records", "type": "IntellectualProduct"}]}

Example input:
Sentence: Family Psychosocial Risk Screening in Infants and Older Children in the Acute Pediatric Hospital Setting Using the Psychosocial Assessment Tool To examine the validity of the Psychosocial Assessment Tool ( PAT ) with families of infants ( < 2 years ) and children admitted to hospital with acute life - threatening illnesses .

Example answer:
{"entities": [{"text": "Risk Screening", "type": "HealthCareActivity"}, {"text": "Pediatric Hospital Setting", "type": "Organization"}, {"text": "Assessment Tool", "type": "IntellectualProduct"}, {"text": "PAT", "type": "IntellectualProduct"}, {"text": "admitted to hospital", "type": "HealthCareActivity"}, {"text": "life - threatening", "type": "Finding"}, {"text": "illnesses", "type": "Finding"}]}

Example input:
Sentence: The charts of children aged 0 to 17 years , consecutively evaluated for sexual victimization , in emergency department and outpatient settings were reviewed .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "emergency department", "type": "Organization"}, {"text": "outpatient settings", "type": "Organization"}]}

Example input:
Sentence: NCT01912742 ( the study was registered in clinicaltrial . gov ) .

Example answer:
{"entities": []}

Example input:
Sentence: All patient specimen identification errors that occurred in the outpatient department ( OPD ) , emergency department ( ED ) , and inpatient department ( IPD ) of a 3 , 800 - bed academic medical center in Taiwan were documented and analyzed retrospectively from 2005 to 2014 .

Example answer:
{"entities": [{"text": "patient specimen", "type": "BodySubstance"}, {"text": "outpatient department", "type": "SpatialConcept"}, {"text": "OPD", "type": "SpatialConcept"}, {"text": "emergency department", "type": "Organization"}, {"text": "ED", "type": "Organization"}, {"text": "inpatient department", "type": "SpatialConcept"}, {"text": "IPD", "type": "SpatialConcept"}, {"text": "academic medical center", "type": "Organization"}, {"text": "Taiwan", "type": "SpatialConcept"}, {"text": "documented", "type": "HealthCareActivity"}]}

Example input:
Sentence: 9 EMTALA investigations and 1 . 7 citations per million emergency department ( ED ) visits during the study period .

Example answer:
{"entities": [{"text": "EMTALA", "type": "IntellectualProduct"}, {"text": "investigations", "type": "HealthCareActivity"}, {"text": "emergency department", "type": "Organization"}, {"text": "( ED", "type": "Organization"}]}

Example input:
Sentence: The National Child Development Study ( NCDS ) is a UK cohort of children born in 1958 .

Example answer:
{"entities": [{"text": "National Child Development Study", "type": "IntellectualProduct"}, {"text": "NCDS", "type": "IntellectualProduct"}, {"text": "UK", "type": "SpatialConcept"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "born", "type": "BiologicFunction"}]}

Example input:
Sentence: We did this ongoing double - blind , non - inferiority study in 161 outpatient centres in 19 countries .

Example answer:
{"entities": [{"text": "double - blind", "type": "ResearchActivity"}, {"text": "non - inferiority study", "type": "ResearchActivity"}, {"text": "centres", "type": "Organization"}, {"text": "countries", "type": "SpatialConcept"}]}

Example input:
Sentence: We performed a retrospective study of children aged 6 months to 17 years who presented to the pediatric emergency department ( PED ) with a fracture of the tibia , femur , humerus , scaphoid , or fifth metatarsus and who followed up with the orthopedic service .

Example answer:
{"entities": [{"text": "retrospective study", "type": "ResearchActivity"}, {"text": "fracture", "type": "InjuryOrPoisoning"}, {"text": "tibia", "type": "AnatomicalStructure"}, {"text": "femur", "type": "AnatomicalStructure"}, {"text": "humerus", "type": "AnatomicalStructure"}, {"text": "scaphoid", "type": "AnatomicalStructure"}, {"text": "fifth metatarsus", "type": "AnatomicalStructure"}, {"text": "orthopedic service", "type": "Organization"}]}

Example input:
Sentence: We conducted a retrospective cohort chart review study of ED patients admitted to an ICU with suspected infection from August 1 , 2012 to February 28 , 2015 .

Example answer:
{"entities": [{"text": "retrospective cohort chart review study", "type": "ResearchActivity"}, {"text": "ED", "type": "Organization"}, {"text": "admitted", "type": "HealthCareActivity"}, {"text": "ICU", "type": "Organization"}, {"text": "suspected infection", "type": "BiologicFunction"}]}

Input:
Sentence: Prospective , randomized , double - blind study conducted at eight pediatric emergency departments ( EDs ) in the US and Canada ( NCT # 01234883 ) .

## Item MedMentions:test:1105
Example input:
Sentence: 05 ) at T2 , whereas the CD8 + percentage was lower than that of group P ( P < 0 . 05 ) at T1 .

Example answer:
{"entities": [{"text": "CD8 + percentage was lower", "type": "Finding"}]}

Example input:
Sentence: The lowest values were obtained in the positive control group ( group II ) ; these values were significantly lower than those of the other groups ( p < 0 . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 4 was significantly greater than that of the BCG and control group ( p < 0 .

Example answer:
{"entities": [{"text": "4", "type": "Chemical"}, {"text": "BCG", "type": "Chemical"}]}

Example input:
Sentence: compared to the control group ( API 0 . 69±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 2 m ( p = 0 . 0001 ) , in the treatment group , whereas the mean value was unchanged in the control group ( p = 0 . 218 ) .

Example answer:
{"entities": [{"text": "treatment group", "type": "PopulationGroup"}]}

Example input:
Sentence: Anteroposterior / Transverse ( AP / T ) ratio was significantly higher in malignant group compared to benign group ( p = 0 . 013 ) .

Example answer:
{"entities": [{"text": "malignant group", "type": "PopulationGroup"}, {"text": "benign group", "type": "PopulationGroup"}]}

Example input:
Sentence: Then histopathological injury score , mean AgNOR number and total AgNOR area / nuclear area ( TAA /  ) were detected for each rat .

Example answer:
{"entities": [{"text": "histopathological injury score", "type": "Finding"}, {"text": "mean AgNOR number", "type": "Finding"}, {"text": "total AgNOR area", "type": "Finding"}, {"text": "nuclear area", "type": "Finding"}, {"text": "TAA", "type": "Finding"}, {"text": "", "type": "Finding"}, {"text": "detected", "type": "Finding"}, {"text": "rat", "type": "Eukaryote"}]}

Example input:
Sentence: 12 . 5 % , p - value 1 . 00 ) between the treatment group and control group , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 2 % in the RM and control group , respectively ( p = 0 . 01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: There was a significant difference in N / L and P / L between idiopathic AAU and control groups ( P = 0 . 006 , P = 0 . 022 ) .

Example answer:
{"entities": [{"text": "N", "type": "AnatomicalStructure"}, {"text": "L", "type": "AnatomicalStructure"}, {"text": "P", "type": "AnatomicalStructure"}, {"text": "AAU", "type": "BiologicFunction"}]}

Input:
Sentence: Also the differences between control group and I / R group were significant for mean AgNOR number ( p = 0 . 000 ) and TAA /  ratio ( p = 0 . 000 ) .

## Item MedMentions:test:1034
Example input:
Sentence: Results Thirty - six percent of nurses had experience with providing palliative care to psychiatric patients with physical co - morbidity in the past 2 years .

Example answer:
{"entities": [{"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "experience", "type": "BiologicFunction"}, {"text": "palliative care", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Introduction Recent empirical research on palliative care for psychiatric patients is lacking .

Example answer:
{"entities": [{"text": "empirical research", "type": "ResearchActivity"}, {"text": "palliative care", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Implications for practice Educating psychiatric nurses about palliative care and close collaboration between physical and mental health care are crucial to address the palliative care needs of psychiatric patients .

Example answer:
{"entities": [{"text": "psychiatric nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "palliative care", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "mental health care", "type": "HealthCareActivity"}]}

Example input:
Sentence: To date , there is a lack of recent empirical research on the experiences of psychiatric nurses in providing palliative care to psychiatric patients who suffer from life - threatening physical co - morbidity .

Example answer:
{"entities": [{"text": "empirical research", "type": "ResearchActivity"}, {"text": "experiences", "type": "BiologicFunction"}, {"text": "psychiatric nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "palliative care", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "life - threatening", "type": "Finding"}]}

Example input:
Sentence: Discussion In palliative care for psychiatric patients , there is more attention for psychosocial and spiritual care compared to palliative care for patients without psychiatric disorders .

Example answer:
{"entities": [{"text": "palliative care", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "attention", "type": "BiologicFunction"}, {"text": "psychosocial", "type": "HealthCareActivity"}, {"text": "spiritual care", "type": "HealthCareActivity"}, {"text": "psychiatric disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: Palliative care in mental health facilities from the perspective of nurses : a mixed - methods study WHAT IS KNOWN ON THE SUBJECT ? : Nurses play an important role in monitoring and supporting patients and their relatives at the end of life .

Example answer:
{"entities": [{"text": "Palliative care", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "mental health facilities", "type": "Organization"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "mixed - methods study", "type": "ResearchActivity"}, {"text": "Nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "end of life", "type": "BiologicFunction"}]}

Example input:
Sentence: Moreover , in palliative care for psychiatric patients there is more attention for psychosocial and spiritual care compared to palliative care for patients without psychiatric disorders .

Example answer:
{"entities": [{"text": "palliative care", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "attention", "type": "BiologicFunction"}, {"text": "psychosocial", "type": "HealthCareActivity"}, {"text": "spiritual care", "type": "HealthCareActivity"}, {"text": "psychiatric disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: The limited literature available indicates that palliative care for psychiatric patients needs to be improved .

Example answer:
{"entities": [{"text": "literature", "type": "IntellectualProduct"}, {"text": "palliative care", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: Patient characteristics and little attention for palliative care within mental health facilities were found to hamper timely and adequate palliative care provision by nurses .

Example answer:
{"entities": [{"text": "attention", "type": "BiologicFunction"}, {"text": "palliative care", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "mental health facilities", "type": "Organization"}, {"text": "provision", "type": "HealthCareActivity"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Since mental health care is increasingly provided ambulatory , the development of palliative care for psychiatric patients outside mental health facilities should be closely monitored .

Example answer:
{"entities": [{"text": "mental health care", "type": "HealthCareActivity"}, {"text": "palliative care", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "mental health facilities", "type": "Organization"}, {"text": "closely", "type": "Finding"}, {"text": "monitored", "type": "HealthCareActivity"}]}

Input:
Sentence: Since mental health care is increasingly provided ambulatory , palliative care for psychiatric patients outside mental health facilities should be closely monitored .

## Item MedMentions:test:1110
Example input:
Sentence: Fractal analysis of the ischemic transition region in chronic ischemic heart disease using magnetic resonance imaging To introduce a novel hypothesis and method to characterise pathomechanisms underlying myocardial ischemia in chronic ischemic heart disease by local fractal analysis ( FA ) of the ischemic myocardial transition region in perfusion imaging .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "chronic ischemic heart disease", "type": "BiologicFunction"}, {"text": "magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "pathomechanisms", "type": "BiologicFunction"}, {"text": "myocardial ischemia", "type": "BiologicFunction"}, {"text": "FA", "type": "ResearchActivity"}, {"text": "myocardial", "type": "SpatialConcept"}, {"text": "perfusion imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: In conclusion , LV mass accounts for approximately half of the predicted variance in biomarker measures of infarct size .

Example answer:
{"entities": [{"text": "LV mass", "type": "Finding"}, {"text": "biomarker", "type": "ClinicalAttribute"}, {"text": "infarct size", "type": "BiologicFunction"}]}

Example input:
Sentence: The area under the receiver operating characteristic curve of LSM and other non - invasive markers of liver fibrosis were compared to determine the most accurate method of predicting liver fibrosis .

Example answer:
{"entities": [{"text": "area", "type": "SpatialConcept"}, {"text": "markers", "type": "MedicalDevice"}, {"text": "liver fibrosis", "type": "BiologicFunction"}, {"text": "method", "type": "HealthCareActivity"}]}

Example input:
Sentence: Relation of Left Ventricular Mass and Infarct Size in Anterior Wall ST - Segment Elevation Acute Myocardial Infarction ( from the EMBRACE STEMI Clinical Trial ) Biomarker measures of infarct size and myocardial salvage index ( MSI ) are important surrogate measures of clinical outcomes after a myocardial infarction .

Example answer:
{"entities": [{"text": "Left Ventricular Mass", "type": "Finding"}, {"text": "Infarct Size", "type": "BiologicFunction"}, {"text": "Anterior Wall ST - Segment Elevation Acute Myocardial Infarction", "type": "BiologicFunction"}, {"text": "STEMI", "type": "BiologicFunction"}, {"text": "Clinical Trial", "type": "ResearchActivity"}, {"text": "Biomarker", "type": "ClinicalAttribute"}, {"text": "infarct size", "type": "BiologicFunction"}, {"text": "myocardial infarction", "type": "BiologicFunction"}]}

Example input:
Sentence: MSI , end - diastolic LV mass on day 4 cardiac magnetic resonance , and CK - MB and troponin I concentrations were evaluated by a core laboratory .

Example answer:
{"entities": [{"text": "end - diastolic", "type": "ClinicalAttribute"}, {"text": "LV mass", "type": "Finding"}, {"text": "cardiac magnetic resonance", "type": "HealthCareActivity"}, {"text": "CK - MB", "type": "HealthCareActivity"}, {"text": "troponin I", "type": "Chemical"}, {"text": "core laboratory", "type": "Organization"}]}

Example input:
Sentence: Simultaneous assessments were made of left ventricular ( LV ) mass index and hypertrophy and measures of LV systolic and diastolic dysfunction .

Example answer:
{"entities": [{"text": "assessments", "type": "HealthCareActivity"}, {"text": "hypertrophy", "type": "BiologicFunction"}, {"text": "LV systolic", "type": "BiologicFunction"}, {"text": "diastolic dysfunction", "type": "BiologicFunction"}]}

Example input:
Sentence: In multivariate models that included age , gender , body surface area , lesion location , smoking , and ischemia time , LV mass remained independently associated with biomarker measures of infarct size ( CK - MB AUC p = 0 .

Example answer:
{"entities": [{"text": "ischemia", "type": "BiologicFunction"}, {"text": "LV mass", "type": "Finding"}, {"text": "biomarker", "type": "ClinicalAttribute"}, {"text": "infarct size", "type": "BiologicFunction"}, {"text": "CK - MB", "type": "HealthCareActivity"}]}

Example input:
Sentence: In patients with cardiac sarcoidosis , both fibrosis mass and its localisation to the basal anterior / anteroseptal left ventricle , or right ventricle was associated with the development of major adverse cardiac events or ventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "cardiac sarcoidosis", "type": "BiologicFunction"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "mass", "type": "Finding"}, {"text": "basal anterior", "type": "AnatomicalStructure"}, {"text": "anteroseptal left ventricle", "type": "AnatomicalStructure"}, {"text": "right ventricle", "type": "AnatomicalStructure"}, {"text": "adverse cardiac events", "type": "Finding"}, {"text": "ventricular tachyarrhythmias", "type": "BiologicFunction"}]}

Example input:
Sentence: Increased left ventricular fibrosis mass was associated with increased prevalence of ventricular tachyarrhythmias ( p < 0 .

Example answer:
{"entities": [{"text": "left ventricular", "type": "AnatomicalStructure"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "mass", "type": "Finding"}, {"text": "ventricular tachyarrhythmias", "type": "BiologicFunction"}]}

Example input:
Sentence: When localisation was defined as the sum of late gadolinium enhancement in the left ventricular basal anterior and basal anteroseptal area s , or the right ventricular area , it was associated with ventricular tachyarrhythmias ( p < 0 . 001 ) .

Example answer:
{"entities": [{"text": "late gadolinium enhancement", "type": "Chemical"}, {"text": "left ventricular basal anterior", "type": "AnatomicalStructure"}, {"text": "basal anteroseptal area", "type": "AnatomicalStructure"}, {"text": "right ventricular area", "type": "AnatomicalStructure"}, {"text": "ventricular tachyarrhythmias", "type": "BiologicFunction"}]}

Input:
Sentence: Left ventricular mass and fibrosis mass were calculated , and localisation was analysed using a 17 - segment model .

## Item MedMentions:test:1005
Example input:
Sentence: In Portugal , there is a lack of knowledge of the current epidemiological situation , as the unique toxoplasmosis National Serological Survey was performed in 1979 / 1980 .

Example answer:
{"entities": [{"text": "Portugal", "type": "SpatialConcept"}, {"text": "toxoplasmosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Overall , 170 ( 62 % ) patients had blood transfusion .

Example answer:
{"entities": [{"text": "blood transfusion", "type": "HealthCareActivity"}]}

Example input:
Sentence: This retrospective , hospital - based study was conducted in patients of ALL , admitted to the Clinical Haematology Department of a tertiary care hospital of Odisha from August 2014 to July 2015 .

Example answer:
{"entities": [{"text": "retrospective , hospital - based study", "type": "ResearchActivity"}, {"text": "ALL", "type": "BiologicFunction"}, {"text": "admitted to the Clinical Haematology Department", "type": "HealthCareActivity"}, {"text": "tertiary care hospital", "type": "Organization"}, {"text": "Odisha", "type": "SpatialConcept"}]}

Example input:
Sentence: When available , the subject grids were analyzed to verify whether a description of content regarding transfusion medicine was given within other disciplines .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "description of content", "type": "IntellectualProduct"}, {"text": "transfusion medicine", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: 1 % ) did not have disciplines of transfusion medicine or hematology and only seven ( 3 .

Example answer:
{"entities": [{"text": "disciplines of transfusion medicine", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "hematology", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: 9 % ) had a discipline of transfusion medicine in the curricular grid .

Example answer:
{"entities": [{"text": "discipline of transfusion medicine", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Education on transfusion medicine is of fundamental importance for safe and efficient transfusion practices .

Example answer:
{"entities": [{"text": "transfusion medicine", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "safe and efficient transfusion practices", "type": "HealthCareActivity"}]}

Example input:
Sentence: Thus , as education in transfusion medicine is vital to medical care , it should aim to promote a responsible practice with the rational use of blood by doctors .

Example answer:
{"entities": [{"text": "transfusion medicine", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "medical care", "type": "Finding"}, {"text": "blood", "type": "BodySubstance"}, {"text": "doctors", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: The websites of the 249 Brazilian medical schools in operation in June 2015 were visited and the curricula of the medical courses were investigated in respect to the presence or absence of a transfusion medicine discipline .

Example answer:
{"entities": [{"text": "websites", "type": "IntellectualProduct"}, {"text": "Brazilian", "type": "PopulationGroup"}, {"text": "medical schools", "type": "Organization"}, {"text": "curricula", "type": "IntellectualProduct"}, {"text": "transfusion medicine discipline", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Thus , additional prospective studies to assess the knowledge and practice of transfusion medicine in Brazilian medical schools are warranted , which could prompt a discussion on the importance of offering training in transfusion medicine to medical students .

Example answer:
{"entities": [{"text": "prospective studies", "type": "ResearchActivity"}, {"text": "knowledge", "type": "IntellectualProduct"}, {"text": "transfusion medicine", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Brazilian", "type": "PopulationGroup"}, {"text": "medical schools", "type": "Organization"}, {"text": "medical students", "type": "ProfessionalOrOccupationalGroup"}]}

Input:
Sentence: This study aims to investigate the situation of the teaching of transfusion medicine in medical schools in Brazil .

## Item MedMentions:test:1139
Example input:
Sentence: Among these , nonspecific granulomatous prostatitis ( n = 10 ) was the most common followed by tubercular prostatitis ( n = 5 ) , posttransurethral resection of the prostate ( n = 3 ) , allergic ( n = 2 ) , and xanthogranulomatous prostatitis ( n = 2 ) .

Example answer:
{"entities": [{"text": "granulomatous prostatitis", "type": "BiologicFunction"}, {"text": "tubercular prostatitis", "type": "BiologicFunction"}, {"text": "posttransurethral resection", "type": "HealthCareActivity"}, {"text": "prostate", "type": "AnatomicalStructure"}, {"text": "xanthogranulomatous prostatitis", "type": "BiologicFunction"}]}

Example input:
Sentence: A questionnaire about urinary incontinence ( International Continence Society scoring ) , anal incontinence , constipation , and obstructed defecation ( Rome criteria and constipation severity score ) , along with an extensive obstetric history , was administered preoperatively and postoperatively annually for 4 years .

Example answer:
{"entities": [{"text": "questionnaire", "type": "IntellectualProduct"}, {"text": "urinary incontinence", "type": "BiologicFunction"}, {"text": "International Continence Society scoring", "type": "IntellectualProduct"}, {"text": "anal", "type": "AnatomicalStructure"}, {"text": "incontinence", "type": "BiologicFunction"}, {"text": "constipation", "type": "Finding"}, {"text": "Rome criteria and constipation severity score", "type": "IntellectualProduct"}, {"text": "obstetric history", "type": "Finding"}]}

Example input:
Sentence: No meatal stenosis or urethral sacculation was detected during follow - up of the studied group .

Example answer:
{"entities": [{"text": "No meatal stenosis", "type": "Finding"}, {"text": "urethral sacculation", "type": "Finding"}, {"text": "detected", "type": "Finding"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: This study collected the data on the clinical phenotype from a family , and the proband , a boy aged 11 years with full - term vaginal delivery , had dry and rough skin and black - brown scaly patches , mainly in the abdomen and extensor aspect of extremities .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "full - term vaginal delivery", "type": "Finding"}, {"text": "dry and rough skin", "type": "Finding"}, {"text": "black - brown scaly patches", "type": "Finding"}, {"text": "abdomen", "type": "SpatialConcept"}, {"text": "extensor", "type": "SpatialConcept"}, {"text": "extremities", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Multiple strictures were noticed in 30 ( 35 .

Example answer:
{"entities": [{"text": "strictures", "type": "BiologicFunction"}]}

Example input:
Sentence: Over 4 years ( between Jan 2011 and Jan 2015 ) , all cases of severe hypospadias were included in this study ; except those with prior attempts at repair , circumcised cases , and cases with severe hypogonadism - because of partial androgen insensitivity - not responding to hormonal manipulations .

Example answer:
{"entities": [{"text": "hypospadias", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "attempts at repair", "type": "HealthCareActivity"}, {"text": "circumcised", "type": "Finding"}, {"text": "hypogonadism", "type": "BiologicFunction"}, {"text": "partial androgen insensitivity", "type": "BiologicFunction"}, {"text": "hormonal manipulations", "type": "HealthCareActivity"}]}

Example input:
Sentence: Hard and fixed nodules were observed on digital rectal examination in 14 cases .

Example answer:
{"entities": [{"text": "nodules", "type": "AnatomicalStructure"}, {"text": "digital rectal examination", "type": "HealthCareActivity"}]}

Example input:
Sentence: No association between flexible sacrum positions and sutured perineal injuries was found ( OR 1 . 02 ; 95 % CI 0 . 86 - 1 . 21 ) or SPT ( OR 0 . 68 ; CI 95 % 0 . 26 - 1 . 79 ) .

Example answer:
{"entities": [{"text": "sacrum", "type": "SpatialConcept"}, {"text": "positions", "type": "SpatialConcept"}, {"text": "perineal injuries", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Between August 2014 and May 2015 , 77 patients with clinical features of anterior urethral stricture disease were included in the study and evaluated by RUG followed by SUG and SE for stricture location , length , depth of spongiofibrosis and periurethral pathologies .

Example answer:
{"entities": [{"text": "anterior urethral stricture disease", "type": "AnatomicalStructure"}, {"text": "SUG", "type": "HealthCareActivity"}, {"text": "SE", "type": "HealthCareActivity"}, {"text": "location", "type": "SpatialConcept"}, {"text": "depth", "type": "ClinicalAttribute"}, {"text": "spongiofibrosis", "type": "BiologicFunction"}, {"text": "periurethral", "type": "SpatialConcept"}, {"text": "pathologies", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Rigid proctoscopy was performed in patients with rectal cancer located in the upper ( Ra ) or lower ( Rb ) division using double - contrast barium enema .

Example answer:
{"entities": [{"text": "Rigid proctoscopy", "type": "HealthCareActivity"}, {"text": "rectal cancer", "type": "BiologicFunction"}, {"text": "located in", "type": "SpatialConcept"}, {"text": "upper", "type": "SpatialConcept"}, {"text": "Ra", "type": "SpatialConcept"}, {"text": "lower", "type": "SpatialConcept"}, {"text": "Rb", "type": "SpatialConcept"}, {"text": "division", "type": "HealthCareActivity"}, {"text": "double - contrast barium enema", "type": "HealthCareActivity"}]}

Input:
Sentence: Anal stricture , rectal prolapse , retained vaginal septum , and a strictured vaginal introitus were also common .

## Item MedMentions:test:857
Example input:
Sentence: Young people , mental health practitioners and researchers co - produce a Transition Preparation Programme to improve outcomes and experience for young people leaving Child and Adolescent Mental Health Services ( CAMHS ) In the UK young people attending child and adolescent mental health services ( CAMHS ) are required to move on , either through discharge or referral to an adult service , at age 17 / 18 , a period of increased risk for onset of mental health problems and other complex psychosocial and physical changes .

Example answer:
{"entities": [{"text": "people", "type": "PopulationGroup"}, {"text": "mental health", "type": "BiologicFunction"}, {"text": "practitioners", "type": "ProfessionalOrOccupationalGroup"}, {"text": "researchers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Transition Preparation Programme", "type": "IntellectualProduct"}, {"text": "experience", "type": "BiologicFunction"}, {"text": "Child and Adolescent Mental Health Services", "type": "HealthCareActivity"}, {"text": "CAMHS", "type": "HealthCareActivity"}, {"text": "UK", "type": "SpatialConcept"}, {"text": "child and adolescent mental health services", "type": "HealthCareActivity"}, {"text": "referral to", "type": "HealthCareActivity"}, {"text": "adult service", "type": "HealthCareActivity"}, {"text": "mental health problems", "type": "Finding"}]}

Example input:
Sentence: The subcutaneous implantable cardioverter - defibrillator ( ICD ) has emerged as a novel tool for prevention of sudden cardiac death , but clinical performance data for adults with congenital heart disease are limited .

Example answer:
{"entities": [{"text": "subcutaneous", "type": "SpatialConcept"}, {"text": "implantable cardioverter - defibrillator", "type": "MedicalDevice"}, {"text": "ICD", "type": "MedicalDevice"}, {"text": "sudden cardiac death", "type": "BiologicFunction"}, {"text": "clinical performance", "type": "Finding"}, {"text": "congenital heart disease", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Feasibility of a transition intervention aimed at adolescents with chronic illness International guidelines recommend planned and structured transition programmes for adolescents with chronic illness because inadequate transition may lead to poor disease control and risk of lacking outpatient follow - up .

Example answer:
{"entities": [{"text": "Feasibility", "type": "ResearchActivity"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "chronic illness", "type": "BiologicFunction"}, {"text": "guidelines", "type": "IntellectualProduct"}, {"text": "programmes", "type": "HealthCareActivity"}, {"text": "poor disease control", "type": "Finding"}, {"text": "outpatient follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Hospitalist co - management of pediatric orthopaedic surgical patients in a community hospital allows for better medical comorbidity and medication management .

Example answer:
{"entities": [{"text": "Hospitalist", "type": "ProfessionalOrOccupationalGroup"}, {"text": "orthopaedic", "type": "HealthCareActivity"}, {"text": "community hospital", "type": "Organization"}, {"text": "medication management", "type": "HealthCareActivity"}]}

Example input:
Sentence: Successful Fetal Tele - Echo at a Small Regional Hospital Prenatal diagnosis of complex congenital heart disease ( CHD ) has been shown to improve newborn outcomes .

Example answer:
{"entities": [{"text": "Fetal Tele - Echo", "type": "HealthCareActivity"}, {"text": "Small Regional Hospital", "type": "Organization"}, {"text": "Prenatal diagnosis", "type": "HealthCareActivity"}, {"text": "congenital heart disease", "type": "AnatomicalStructure"}, {"text": "CHD", "type": "AnatomicalStructure"}, {"text": "improve", "type": "Finding"}, {"text": "newborn", "type": "Finding"}]}

Example input:
Sentence: Clinical Experience With the Subcutaneous Implantable Cardioverter - Defibrillator in Adults With Congenital Heart Disease Sudden cardiac death is a major contributor to mortality for adults with congenital heart disease .

Example answer:
{"entities": [{"text": "Congenital Heart Disease", "type": "AnatomicalStructure"}, {"text": "Sudden cardiac death", "type": "BiologicFunction"}, {"text": "congenital heart disease", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Nurses , the comprehensive medical teams , and patients ' families can all effectively influence the process of preparing these patients for transition to adult care .

Example answer:
{"entities": [{"text": "Nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "comprehensive medical teams", "type": "HealthCareActivity"}, {"text": "adult care", "type": "HealthCareActivity"}]}

Example input:
Sentence: Subcutaneous ICD implantation is feasible for adults with congenital heart disease patients .

Example answer:
{"entities": [{"text": "Subcutaneous", "type": "SpatialConcept"}, {"text": "ICD", "type": "MedicalDevice"}, {"text": "implantation", "type": "HealthCareActivity"}, {"text": "congenital heart disease", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Although these patients are admitted on a pediatric unit , nurses can aid in promoting their independence and help prepare them to transition into the adult medical system .

Example answer:
{"entities": [{"text": "admitted", "type": "HealthCareActivity"}, {"text": "pediatric unit", "type": "Organization"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Caring for adult patients is often a challenge for pediatric nurses , because the nurses have less experience and comfort with adult care , medications , comorbid conditions , and rehabilitation techniques .

Example answer:
{"entities": [{"text": "Caring", "type": "HealthCareActivity"}, {"text": "pediatric nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "adult care", "type": "HealthCareActivity"}, {"text": "medications", "type": "HealthCareActivity"}, {"text": "comorbid conditions", "type": "Finding"}]}

Input:
Sentence: Challenges Caring for Adults With Congenital Heart Disease in Pediatric Settings : How Nurses Can Aid in the Transition As surgery for complex congenital heart disease is becoming more advanced , an increasing number of patients are surviving into adulthood , yet many of these adult patients remain in the pediatric hospital system .

## Item MedMentions:test:1126
Example input:
Sentence: In addition , the current study demonstrated that the downregulation of ZEB2‑AS1 was associated with decreased tumor growth and metastasis in HCC by the regulation of the expression levels of epithelial mesenchymal transition - induced markers .

Example answer:
{"entities": [{"text": "downregulation", "type": "BiologicFunction"}, {"text": "ZEB2‑AS1", "type": "AnatomicalStructure"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "epithelial mesenchymal transition", "type": "BiologicFunction"}, {"text": "markers", "type": "ClinicalAttribute"}]}

Example input:
Sentence: alvei H4 was investigated by adding exogenous AHLs ( C4 - HSL , C6 - HSL and 3 - oxo - C8 - HSL ) to H .

Example answer:
{"entities": [{"text": "alvei H4", "type": "Bacterium"}, {"text": "AHLs", "type": "Chemical"}, {"text": "C4 - HSL", "type": "Chemical"}, {"text": "C6 - HSL", "type": "Chemical"}, {"text": "3 - oxo - C8 - HSL", "type": "Chemical"}, {"text": "H .", "type": "Bacterium"}]}

Example input:
Sentence: Various assays were performed to explore the role and cellular functions of miR - 132 in HCC and a successive panel of tasks was completed , including NLP analysis , miR - 132 target genes prediction , comprehensive analyses ( gene ontology analysis , pathway analysis , network analysis and connectivity analysis ) , and analytical integration .

Example answer:
{"entities": [{"text": "assays", "type": "HealthCareActivity"}, {"text": "cellular functions", "type": "BiologicFunction"}, {"text": "miR - 132", "type": "Chemical"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "successive panel", "type": "ResearchActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "target genes", "type": "AnatomicalStructure"}, {"text": "analyses", "type": "ResearchActivity"}, {"text": "gene ontology analysis", "type": "IntellectualProduct"}, {"text": "pathway analysis", "type": "IntellectualProduct"}, {"text": "network analysis", "type": "IntellectualProduct"}]}

Example input:
Sentence: Hog liver esterase ( HLE ) hydrolyzed chlorogenic acid lactones ( CQALs , FQALs ) selectively , while chlorogenate esterase hydrolyzed all chlorogenic acids ( CQAs , FQAs ) and their corresponding lactones ( CQALs , FQALs ) in a non - selective way .

Example answer:
{"entities": [{"text": "Hog liver esterase", "type": "Chemical"}, {"text": "HLE", "type": "Chemical"}, {"text": "chlorogenic acid lactones", "type": "Chemical"}, {"text": "CQALs", "type": "Chemical"}, {"text": "FQALs", "type": "Chemical"}, {"text": "chlorogenate esterase", "type": "Chemical"}, {"text": "chlorogenic acids", "type": "Chemical"}, {"text": "CQAs", "type": "Chemical"}, {"text": "FQAs", "type": "Chemical"}, {"text": "lactones", "type": "Chemical"}, {"text": "non - selective", "type": "Finding"}]}

Example input:
Sentence: Mep1A is overexpressed in most HCC and induces HCC cell migration and invasion .

Example answer:
{"entities": [{"text": "Mep1A", "type": "Chemical"}, {"text": "overexpressed", "type": "BiologicFunction"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "cell migration", "type": "BiologicFunction"}, {"text": "invasion", "type": "Finding"}]}

Example input:
Sentence: Mep1A , but not meprin β , was overexpressed in a series of 242 human HCC ( 2 . 04 fold , p < 0 . 0001 ) , and a high expression correlated with a poor prognosis .

Example answer:
{"entities": [{"text": "Mep1A", "type": "Chemical"}, {"text": "meprin β", "type": "Chemical"}, {"text": "overexpressed", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "poor prognosis", "type": "Finding"}]}

Example input:
Sentence: Variant 2 of KIAA0101 , antagonizing its oncogenic variant 1 , might be a potential therapeutic strategy in hepatocellular carcinoma Hepatocellular carcinoma ( HCC ) is one of the most lethal malignant tumors worldwide and effective therapies , including molecular therapy , remain elusive .

Example answer:
{"entities": [{"text": "Variant 2", "type": "AnatomicalStructure"}, {"text": "KIAA0101", "type": "AnatomicalStructure"}, {"text": "oncogenic", "type": "AnatomicalStructure"}, {"text": "variant 1", "type": "AnatomicalStructure"}, {"text": "therapeutic strategy", "type": "HealthCareActivity"}, {"text": "hepatocellular carcinoma", "type": "BiologicFunction"}, {"text": "Hepatocellular carcinoma", "type": "BiologicFunction"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "lethal", "type": "Finding"}, {"text": "malignant tumors", "type": "BiologicFunction"}, {"text": "worldwide", "type": "PopulationGroup"}, {"text": "therapies", "type": "HealthCareActivity"}, {"text": "molecular therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: The most active compounds , 2b , 2c , 3c , 4a , 4c and 5a , were found to be more selective against the MCF - 7 and HeLa cell lines than the human lung carcinoma ( A549 ) cells .

Example answer:
{"entities": [{"text": "active compounds", "type": "Chemical"}, {"text": "2b", "type": "Chemical"}, {"text": "2c", "type": "Chemical"}, {"text": "3c", "type": "Chemical"}, {"text": "4a", "type": "Chemical"}, {"text": "4c", "type": "Chemical"}, {"text": "5a", "type": "Chemical"}, {"text": "MCF - 7", "type": "AnatomicalStructure"}, {"text": "HeLa", "type": "AnatomicalStructure"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "human lung carcinoma ( A549 ) cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Overall , we suggest that Mep1A may be a useful target in HCC .

Example answer:
{"entities": [{"text": "Mep1A", "type": "Chemical"}, {"text": "HCC", "type": "BiologicFunction"}]}

Example input:
Sentence: We found that Mep1A was a target of Reptin , a protein that is oncogenic in HCC .

Example answer:
{"entities": [{"text": "Mep1A", "type": "Chemical"}, {"text": "Reptin", "type": "Chemical"}, {"text": "protein that is oncogenic", "type": "Chemical"}, {"text": "HCC", "type": "BiologicFunction"}]}

Input:
Sentence: HCl ( targeting 2C protein ) and oxoglaucine ( attacking 3A coding region ) .

## Item MedMentions:test:709
Example input:
Sentence: PROs assessed included Patient Global Assessment of disease ( PtGA ) , pain , Health Assessment Questionnaire - Disability Index ( HAQ - DI ) , Functional Assessment of Chronic Illness Therapy - Fatigue ( FACIT - F ) and health - related quality of life ( Short Form - 36 [ SF - 36 ] ) .

Example answer:
{"entities": [{"text": "PROs", "type": "IntellectualProduct"}, {"text": "Patient Global Assessment of disease", "type": "IntellectualProduct"}, {"text": "PtGA", "type": "IntellectualProduct"}, {"text": "pain", "type": "Finding"}, {"text": "Health Assessment Questionnaire - Disability Index", "type": "IntellectualProduct"}, {"text": "HAQ - DI", "type": "IntellectualProduct"}, {"text": "Functional Assessment of Chronic Illness Therapy - Fatigue", "type": "IntellectualProduct"}, {"text": "FACIT - F", "type": "IntellectualProduct"}, {"text": "Short Form - 36", "type": "IntellectualProduct"}, {"text": "SF - 36", "type": "IntellectualProduct"}]}

Example input:
Sentence: Questionnaires and functional tests showed an increase in the perception of safety .

Example answer:
{"entities": [{"text": "Questionnaires", "type": "IntellectualProduct"}, {"text": "functional tests", "type": "IntellectualProduct"}]}

Example input:
Sentence: , the choice and number of antiseizure drugs [ ASDs ] ) in therapeutic hypothermia - treated neonates with HI from 2007 to 2015 in the Johns Hopkins Hospital Neonatal Intensive Care Unit . During this period , 3 different EEG monitoring protocols were utilized : Period 1 ( 2007 - 2009 ) , single , brief conventional EEG ( 1 h duration ) at a variable time during therapeutic hypothermia treatment , i .

Example answer:
{"entities": [{"text": "antiseizure drugs", "type": "Chemical"}, {"text": "ASDs", "type": "Chemical"}, {"text": "hypothermia - treated", "type": "HealthCareActivity"}, {"text": "HI", "type": "BiologicFunction"}, {"text": "Johns Hopkins Hospital Neonatal Intensive Care Unit", "type": "Organization"}, {"text": "EEG", "type": "Finding"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "protocols", "type": "HealthCareActivity"}, {"text": "EEG", "type": "HealthCareActivity"}, {"text": "hypothermia treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: To ‎evaluate the severity of attention deficit hyperactivity disorder ( ADHD ) and mania , Conner 's ‎Parent Rating Scale - Revised version ( CPRS - R ) , and Young Mania Rating Scale ( YMRS ) were ‎used , respectively .

Example answer:
{"entities": [{"text": "‎evaluate", "type": "HealthCareActivity"}, {"text": "attention deficit hyperactivity disorder", "type": "BiologicFunction"}, {"text": "ADHD", "type": "BiologicFunction"}, {"text": "mania", "type": "BiologicFunction"}, {"text": "Young Mania Rating Scale", "type": "IntellectualProduct"}, {"text": "YMRS", "type": "IntellectualProduct"}]}

Example input:
Sentence: Health - Related Quality of Life in Patients With α1 Antitrypsin Deficency : A Cross Sectional Study Measures of health related quality of life ( HRQoL ) in patients with α1 - antitrypsin deficiency ( AATD ) can help to determine the impact of the disease and provide an important insight into the intervention outcomes .

Example answer:
{"entities": [{"text": "α1 Antitrypsin Deficency", "type": "BiologicFunction"}, {"text": "Cross Sectional Study", "type": "ResearchActivity"}, {"text": "α1 - antitrypsin deficiency", "type": "BiologicFunction"}, {"text": "AATD", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "intervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: The relationships between symptoms and quality of life over the course of cognitive - behavioral therapy for panic disorder in Japan This study examined the relationships between changes in symptoms and changes in quality of life ( QOL ) during cognitive - behavioral therapy ( CBT ) for panic disorder ( PD ) .

Example answer:
{"entities": [{"text": "symptoms", "type": "Finding"}, {"text": "cognitive - behavioral therapy", "type": "HealthCareActivity"}, {"text": "panic disorder", "type": "BiologicFunction"}, {"text": "Japan", "type": "SpatialConcept"}, {"text": "study", "type": "ResearchActivity"}, {"text": "examined", "type": "Finding"}, {"text": "CBT", "type": "HealthCareActivity"}, {"text": "PD", "type": "BiologicFunction"}]}

Example input:
Sentence: While analyses revealed lower accuracy and longer reaction time in ASD in the condition with local interference only , eye tracking robustly captured ASD -related global atypicalities across both conditions .

Example answer:
{"entities": [{"text": "analyses", "type": "ResearchActivity"}, {"text": "ASD", "type": "BiologicFunction"}, {"text": "local interference", "type": "BiologicFunction"}, {"text": "atypicalities", "type": "Finding"}]}

Example input:
Sentence: Poor performance in the blast - exposed subjects was associated with weaker evoked response potentials ( ERPs ) in frontal EEG channels , as well as a failure of attention to enhance the neural responses evoked by a sequence when it was the target compared to when it was a distractor .

Example answer:
{"entities": [{"text": "blast - exposed subjects", "type": "PopulationGroup"}, {"text": "frontal EEG channels", "type": "HealthCareActivity"}, {"text": "attention", "type": "BiologicFunction"}]}

Example input:
Sentence: HRQoL was evaluated at baseline and every 6 weeks while on treatment using the European Organisation for Research and Treatment of Care ( EORTC ) Core Quality of Life Questionnaire ( QLQ - C30 ) and the EuroQoL Five Dimensions Questionnaire ( EQ - 5D ) .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "European Organisation for Research and Treatment of Care ( EORTC ) Core Quality of Life Questionnaire ( QLQ - C30 )", "type": "IntellectualProduct"}, {"text": "EuroQoL Five Dimensions Questionnaire", "type": "IntellectualProduct"}, {"text": "EQ - 5D", "type": "IntellectualProduct"}]}

Example input:
Sentence: Adverse Events Profile total scores improved for 21 / 21 ( 100 . 0 % ) patients , QOLIE - 10 total scores improved for 17 / 21 ( 81 . 0 % ) patients , and alertness scores improved for 16 / 21 ( 76 . 2 % ) patients .

Example answer:
{"entities": [{"text": "Adverse Events Profile", "type": "IntellectualProduct"}, {"text": "improved", "type": "Finding"}, {"text": "QOLIE - 10", "type": "IntellectualProduct"}, {"text": "alertness", "type": "BiologicFunction"}]}

Input:
Sentence: Tolerability was assessed using the Adverse Events Profile ( AEP ) , quality of life was assessed using the Quality of Life in Epilepsy Inventory 10 ( QOLIE - 10 ) , and alertness was assessed as reaction time using a subtest of the Test Battery for Attention Performance version 2 .

## Item MedMentions:test:1140
Example input:
Sentence: Here we show that NADPH oxidase activation is closely related to heavy ion radiation - induced cell death via excessive ROS generation .

Example answer:
{"entities": [{"text": "NADPH oxidase", "type": "Chemical"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "ROS generation", "type": "BiologicFunction"}]}

Example input:
Sentence: Metabolomics analysis of anaphylactoid reaction reveals its mechanism in a rat model Anaphylactoid reactions , accounting for more than 77 % of all immune - mediated immediate hypersensitivity reactions , have become a serious threat to public health , but their effect mechanism is not clear and diagnostic tests are limited .

Example answer:
{"entities": [{"text": "Metabolomics", "type": "Chemical"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "anaphylactoid reaction", "type": "BiologicFunction"}, {"text": "rat", "type": "Eukaryote"}, {"text": "model", "type": "Eukaryote"}, {"text": "Anaphylactoid reactions", "type": "BiologicFunction"}, {"text": "immune - mediated immediate hypersensitivity reactions", "type": "BiologicFunction"}, {"text": "public health", "type": "HealthCareActivity"}, {"text": "diagnostic tests", "type": "HealthCareActivity"}]}

Example input:
Sentence: Finally , using bioinformatics tools , pathway analyses of differentially expressed MS - identified proteins find that acute phase , inflammatory and immune responses as well as oxidative stress are likely involved in the response to contamination , suggesting a physiological perturbation , but that does not necessarily lead to a toxic effect .

Example answer:
{"entities": [{"text": "pathway analyses", "type": "IntellectualProduct"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "MS", "type": "HealthCareActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "immune responses", "type": "BiologicFunction"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "toxic effect", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The resulting temporal control over melanopsin activation allowed us to compare the activation kinetics of different components of the electrophysiological response .

Example answer:
{"entities": [{"text": "melanopsin", "type": "Chemical"}, {"text": "electrophysiological", "type": "BiologicFunction"}]}

Example input:
Sentence: Several endpoints were recorded at different levels of biological organization , including lethal endpoints , morphological abnormalities , photomotor behavioral responses , cardiac activity , DNA damage and exposure level measurements ( EROD activity , cyp1a and PAH metabolites ) .

Example answer:
{"entities": [{"text": "biological organization", "type": "BiologicFunction"}, {"text": "lethal", "type": "Finding"}, {"text": "morphological abnormalities", "type": "AnatomicalStructure"}, {"text": "cardiac activity", "type": "Finding"}, {"text": "DNA damage", "type": "BiologicFunction"}, {"text": "EROD", "type": "Chemical"}, {"text": "cyp1a", "type": "Chemical"}, {"text": "PAH", "type": "Chemical"}, {"text": "metabolites", "type": "Chemical"}]}

Example input:
Sentence: Pathway analysis showed activation of interferon ( IFN ) and metabolic networks .

Example answer:
{"entities": [{"text": "Pathway analysis", "type": "IntellectualProduct"}, {"text": "interferon", "type": "Chemical"}, {"text": "IFN", "type": "Chemical"}, {"text": "metabolic networks", "type": "BiologicFunction"}]}

Example input:
Sentence: In recent years , there have been significant advances centered on in vitro test systems and bioanalytical strategies , yet a frontier challenge concerns linking observed network perturbations to phenotypes , which will require understanding pathways and networks that give rise to adverse responses .

Example answer:
{"entities": [{"text": "bioanalytical strategies", "type": "HealthCareActivity"}]}

Example input:
Sentence: A Bayesian Network - Based Approach to Selection of Intervention Points in the Mitogen - Activated Protein Kinase Plant Defense Response Pathway An important problem in computational biology is the identification of potential points of intervention that can lead to modified network behavior in a genetic regulatory network .

Example answer:
{"entities": [{"text": "Mitogen - Activated Protein Kinase", "type": "Chemical"}, {"text": "Plant", "type": "Eukaryote"}, {"text": "Defense Response", "type": "BiologicFunction"}, {"text": "Pathway", "type": "BiologicFunction"}, {"text": "problem", "type": "Finding"}, {"text": "computational biology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "network", "type": "BiologicFunction"}, {"text": "genetic regulatory network", "type": "BiologicFunction"}]}

Example input:
Sentence: The Latin American Biological Dosimetry Network ( LBDNet ) was formally founded in 2007 to provide early biological dosimetry assistance in case of radiation emergencies in the Latin American Region .

Example answer:
{"entities": [{"text": "Latin American Biological Dosimetry Network", "type": "Organization"}, {"text": "LBDNet", "type": "Organization"}, {"text": "dosimetry", "type": "HealthCareActivity"}, {"text": "Latin American Region", "type": "SpatialConcept"}]}

Example input:
Sentence: The Latin American Biological Dosimetry Network ( LBDNet ) Biological Dosimetry is a necessary support for national radiation protection programmes and emergency response schemes .

Example answer:
{"entities": [{"text": "Latin American Biological Dosimetry Network", "type": "Organization"}, {"text": "LBDNet", "type": "Organization"}, {"text": "Dosimetry", "type": "HealthCareActivity"}, {"text": "national radiation protection programmes", "type": "IntellectualProduct"}, {"text": "emergency response schemes", "type": "IntellectualProduct"}]}

Input:
Sentence: The process for network activation and the role of the coordinating laboratory during biological dosimetry emergency response is also presented .

## Item MedMentions:test:1234
Example input:
Sentence: This decrease was similar when the items were presented as pictures ( Experiment 1 ) or as words ( Experiment 2 ) , thus excluding a purely visual effect .

Example answer:
{"entities": [{"text": "Experiment", "type": "ResearchActivity"}, {"text": "words", "type": "IntellectualProduct"}]}

Example input:
Sentence: In a follow - up survey comparing video and paper groups to non - experienced groups , the rates were higher for video ( χ ( 2 ) = 24 . 319 , p < 0 . 001 ) and paper ( χ ( 2 ) = 11 . 134 , p = 0 . 001 ) .

Example answer:
{"entities": [{"text": "follow - up", "type": "ResearchActivity"}, {"text": "survey", "type": "IntellectualProduct"}, {"text": "video", "type": "IntellectualProduct"}]}

Example input:
Sentence: A questionnaire was designed to assess attitude ( importance ) and behaviours ( frequency and quantity ) among junior ( under 19 ) players on a 5 - point Likert Scale .

Example answer:
{"entities": [{"text": "questionnaire", "type": "IntellectualProduct"}, {"text": "attitude", "type": "BiologicFunction"}, {"text": "players", "type": "PopulationGroup"}, {"text": "5 - point Likert Scale", "type": "IntellectualProduct"}]}

Example input:
Sentence: After formal teaching about digital professionalism , we administered a survey to medical students that described 35 technology - related behaviors and queried students about professionalism of the behavior ( on a 5 - point Likert scale ) , observation of others engaging in the behavior ( yes or no ) , as well as personal participation in the behavior ( yes or no ) .

Example answer:
{"entities": [{"text": "survey", "type": "IntellectualProduct"}, {"text": "medical students", "type": "ProfessionalOrOccupationalGroup"}, {"text": "students", "type": "PopulationGroup"}, {"text": "5 - point Likert scale", "type": "IntellectualProduct"}, {"text": "yes or no", "type": "IntellectualProduct"}]}

Example input:
Sentence: Assessing the learning potential of an interactive digital game versus an interactive - style didactic lecture : the continued importance of didactic teaching in medical student education Games with educational intent offer a possible advantage of being more interactive and increasing learner satisfaction .

Example answer:
{"entities": [{"text": "learning", "type": "BiologicFunction"}, {"text": "lecture", "type": "IntellectualProduct"}, {"text": "medical student", "type": "ProfessionalOrOccupationalGroup"}, {"text": "possible", "type": "Finding"}, {"text": "learner", "type": "PopulationGroup"}, {"text": "satisfaction", "type": "BiologicFunction"}]}

Example input:
Sentence: An online survey was completed by a convenience sample that engages in Internet gaming ( N = 404 ) .

Example answer:
{"entities": [{"text": "online survey", "type": "IntellectualProduct"}, {"text": "convenience sample", "type": "ResearchActivity"}]}

Example input:
Sentence: Students in the lecture group had higher test scores compared to students in the game group ( 4 . 0 / 5 versus 3 .

Example answer:
{"entities": [{"text": "Students", "type": "PopulationGroup"}, {"text": "lecture", "type": "IntellectualProduct"}, {"text": "students", "type": "PopulationGroup"}]}

Example input:
Sentence: Students in the lecture group perceived the lecture to be more enjoyable and a better use of their time compared to those in the game group ( P = 0 .

Example answer:
{"entities": [{"text": "Students", "type": "PopulationGroup"}, {"text": "lecture", "type": "IntellectualProduct"}, {"text": "perceived", "type": "BiologicFunction"}]}

Example input:
Sentence: Students in the lecture group reported greater understanding and recall of the material than students in the game group ( P < 0 .

Example answer:
{"entities": [{"text": "Students", "type": "PopulationGroup"}, {"text": "lecture", "type": "IntellectualProduct"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "understanding", "type": "BiologicFunction"}, {"text": "recall", "type": "BiologicFunction"}, {"text": "students", "type": "PopulationGroup"}]}

Example input:
Sentence: There was no statistically significant difference between the lecture and game group in ability to maintain interest ( P = 0 . 187 ) .

Example answer:
{"entities": [{"text": "lecture", "type": "IntellectualProduct"}]}

Input:
Sentence: In comparison to pre - survey results , there was a statistically significant decrease in interest for further digital interactive materials reported by students in the game group ( P = 0 . 146 ) .

## Item MedMentions:test:1317
Example input:
Sentence: Diagnoses of problem and pathological gambling and other psychiatric disorders were based on the DSM - IV - TR criteria with the following additional criteria for gamblers : more than 10 lifetime gambling episodes and a single year loss of at least 365 USD from gambling .

Example answer:
{"entities": [{"text": "Diagnoses", "type": "Finding"}, {"text": "pathological gambling", "type": "BiologicFunction"}, {"text": "psychiatric disorders", "type": "BiologicFunction"}, {"text": "DSM - IV - TR criteria", "type": "IntellectualProduct"}]}

Example input:
Sentence: The number of trials has increased over the years , and 35 % of the studies were industry - financed .

Example answer:
{"entities": [{"text": "trials", "type": "ResearchActivity"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: Pathological gambling was highly prevalent among those who ever experienced major depressive episodes ( 5 . 5 % ) , any drug dependence ( 5 . 1 % ) , and intermittent explosive disorder ( 4 . 8 % ) .

Example answer:
{"entities": [{"text": "Pathological gambling", "type": "BiologicFunction"}, {"text": "major depressive episodes", "type": "BiologicFunction"}, {"text": "drug dependence", "type": "BiologicFunction"}, {"text": "intermittent explosive disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: As expected , disordered gamblers were found to spend significantly more money on electronic games and casino table games ( p < 0 .

Example answer:
{"entities": [{"text": "table games", "type": "IntellectualProduct"}]}

Example input:
Sentence: The association between pathological gambling was strongest with a history of major depressive episode [ adjusted odds ratio ( AOR ) = 10 .

Example answer:
{"entities": [{"text": "pathological gambling", "type": "BiologicFunction"}, {"text": "major depressive episode", "type": "BiologicFunction"}]}

Example input:
Sentence: A total of 423 young adults , who gambled ≥5 times in the preceding year , were recruited using media advertisements and undertook detailed assessment including structured psychiatric interview , questionnaires , and neurocognitive tests .

Example answer:
{"entities": [{"text": "media advertisements", "type": "IntellectualProduct"}, {"text": "assessment", "type": "HealthCareActivity"}, {"text": "psychiatric interview", "type": "HealthCareActivity"}, {"text": "questionnaires", "type": "IntellectualProduct"}]}

Example input:
Sentence: Next , we examined and categorized the empirical articles by inclusion of an experimental manipulation and treatment to alleviate at least some aspect of pathological gambling , participant population used , type of gambling task employed in the research , whether the participants in the study actually gambled , and the behavioral phenomena of interest .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "articles", "type": "IntellectualProduct"}, {"text": "manipulation", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "alleviate", "type": "HealthCareActivity"}, {"text": "participant population", "type": "PopulationGroup"}, {"text": "employed", "type": "Finding"}, {"text": "research", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "study", "type": "ResearchActivity"}, {"text": "interest", "type": "BiologicFunction"}]}

Example input:
Sentence: Of the empirical articles , examinations of treatment techniques or methods are scarce ; slot machine play is the most represented form of gambling , and slightly greater than half of the research included compensation based on gambling outcomes within experiments .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}, {"text": "examinations", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "research", "type": "ResearchActivity"}, {"text": "experiments", "type": "ResearchActivity"}]}

Example input:
Sentence: Results The estimated lifetime prevalence rates of pathological and problem gambling were 0 . 90 % [ 95 % confidence interval ( CI ) : 0 . 51 - 1 . 29 ] and 1 .

Example answer:
{"entities": [{"text": "pathological", "type": "BiologicFunction"}]}

Example input:
Sentence: The most popular type of gambling was playing lotteries [ 69 . 5 % , standard error ( SE ) = 1 . 9 ] , the prevalence of which was significantly higher among females and older age groups .

Example answer:
{"entities": [{"text": "older age groups", "type": "PopulationGroup"}]}

Input:
Sentence: The results show that the rate of publication of gambling research has increased in the last 6 years , and a vast majority of articles are empirical .

## Item MedMentions:test:1258
Example input:
Sentence: Secondary measures were change in best - corrected visual acuity ( BCVA ) and central retinal thickness ( CRT ) by spectral - domain optical coherence tomography at 3 months after treatment .

Example answer:
{"entities": [{"text": "best - corrected visual acuity", "type": "Finding"}, {"text": "BCVA", "type": "Finding"}, {"text": "central retinal thickness", "type": "Finding"}, {"text": "CRT", "type": "Finding"}, {"text": "spectral - domain optical coherence tomography", "type": "MedicalDevice"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The higher frequency of BM after treatment was significantly correlated with the acceleration of CTT , SLBTT and whole gut transit time .

Example answer:
{"entities": [{"text": "frequency of BM", "type": "Finding"}, {"text": "SLBTT", "type": "BiologicFunction"}, {"text": "gut", "type": "AnatomicalStructure"}]}

Example input:
Sentence: De - escalation therapy was considered when the initial antibiotic therapy was narrowed to penicillin , amoxicillin or amoxicillin / clavulanate within the first 72 h after admission .

Example answer:
{"entities": [{"text": "De - escalation therapy", "type": "HealthCareActivity"}, {"text": "antibiotic therapy", "type": "HealthCareActivity"}, {"text": "penicillin", "type": "Chemical"}, {"text": "amoxicillin", "type": "Chemical"}, {"text": "amoxicillin / clavulanate", "type": "Chemical"}, {"text": "admission", "type": "HealthCareActivity"}]}

Example input:
Sentence: Consecutive treatment using ETV followed by LdT showed virological rebound in 16 .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "ETV", "type": "Chemical"}, {"text": "LdT", "type": "Chemical"}, {"text": "rebound", "type": "Finding"}]}

Example input:
Sentence: Patients ≥70 years were more often treated with less toxic chemotherapy , yet experienced higher rates of hospitalization during treatment and increased rates of acute mortality following CRT .

Example answer:
{"entities": [{"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "hospitalization", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "CRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Three months after treatment , > 30 % improvement was seen in 10 / 33 ( 30 % ) of VRET participants and 12 / 33 ( 36 % ) in CET .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "VRET", "type": "HealthCareActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "CET", "type": "HealthCareActivity"}]}

Example input:
Sentence: Within 48 h of initiation of warfarin therapy , the tetraparesis and hyperesthesia were markedly improved .

Example answer:
{"entities": [{"text": "warfarin therapy", "type": "HealthCareActivity"}, {"text": "tetraparesis", "type": "Finding"}, {"text": "hyperesthesia", "type": "Finding"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: HBOT maybe an effective therapeutic strategy for this condition .

Example answer:
{"entities": [{"text": "HBOT", "type": "HealthCareActivity"}]}

Example input:
Sentence: The patient was discharged with 20 sessions of HBOT and recovered completely after 1 year .

Example answer:
{"entities": [{"text": "patient was discharged", "type": "HealthCareActivity"}, {"text": "HBOT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Recent clinical trials have favored hyperbaric oxygen therapy ( HBOT ) as a promising therapeutic strategy for adult patients with severe head injuries .

Example answer:
{"entities": [{"text": "clinical trials", "type": "ResearchActivity"}, {"text": "hyperbaric oxygen therapy", "type": "HealthCareActivity"}, {"text": "HBOT", "type": "HealthCareActivity"}, {"text": "head injuries", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: HBOT was administered at 72 h post admission and the condition was clearly improved following the initial therapy .

## Item MedMentions:test:1434
Example input:
Sentence: 854 , P = 0 . 013 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 1 . 6 ; t = 1 . 99 , p = 0 . 058 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 16 . 5 ± 4 .

Example answer:
{"entities": []}

Example input:
Sentence: 62 . 75 ± 4 . 82 , P < 0 . 01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 32 ± 4 . 11 ( t18 = 1 . 34 , p = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 16±0 . 17 s ) .

Example answer:
{"entities": []}

Example input:
Sentence: 0 - 17 . 1 ; p = 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 51 ± 0 . 870 ; p = 0 . 034 .

Example answer:
{"entities": []}

Example input:
Sentence: 0 . 72 [ 0 . 69 - 0 . 77 ] , P < 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 0 ± 16 . 0 , p < 0 .

Example answer:
{"entities": []}

Input:
Sentence: 16±0 . 76 ) ( p < 0 . 01 ) .

## Item MedMentions:test:1384
Example input:
Sentence: The 2D - LC - MS / MS analysis identified 1324 proteins in the two pools , of which 744 were quantifiable .

Example answer:
{"entities": [{"text": "2D - LC - MS", "type": "HealthCareActivity"}, {"text": "MS", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "pools", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The identity of the enolase was confirmed through mass spectrometric analysis that showed the characteristic 442 amino acid sequence with a molecular mass of 48 . 03 kDa .

Example answer:
{"entities": [{"text": "enolase", "type": "Chemical"}, {"text": "mass spectrometric analysis", "type": "HealthCareActivity"}, {"text": "amino acid sequence", "type": "SpatialConcept"}]}

Example input:
Sentence: Proteins displaying greater than threefold changes ( > log2 1 . 59 ) at 1 - hour CPB relative to the initiation of CPB ( 26 down - regulated and 22 up - regulated ) were selected for further analysis .

Example answer:
{"entities": [{"text": "Proteins", "type": "Chemical"}, {"text": "CPB", "type": "HealthCareActivity"}, {"text": "down - regulated", "type": "BiologicFunction"}, {"text": "up - regulated", "type": "BiologicFunction"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: MALDI - ToF mass spectrometry was used to characterize the low - molecular - weight ( 1000 - 14 , 000Da ) serum fraction .

Example answer:
{"entities": [{"text": "MALDI - ToF mass spectrometry", "type": "ResearchActivity"}, {"text": "serum", "type": "BodySubstance"}]}

Example input:
Sentence: The SWATH approach provided quantitation for 730 proteins , 552 of which overlapped with the common population from the 2D - IDA results .

Example answer:
{"entities": [{"text": "SWATH approach", "type": "HealthCareActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "2D - IDA", "type": "IntellectualProduct"}]}

Example input:
Sentence: Two fractions , i . e . , WBP - 1 and WBP - 2 with molecular weight of 83 . 50kDa and 80 .

Example answer:
{"entities": [{"text": "WBP - 1", "type": "Chemical"}, {"text": "WBP - 2", "type": "Chemical"}]}

Example input:
Sentence: Recombinant fragments ( 60 - 79 aa ) , which together span the entire length of tropomyosin , were weak secretagogues .

Example answer:
{"entities": [{"text": "tropomyosin", "type": "Chemical"}]}

Example input:
Sentence: Our study showed that the recombinant protein rIBPv exhibited a thermal hysteresis of 2 ° C at concentrations of > 50 μM , effectively inhibited ice recrystallization , and enhanced bacterial viability during freeze - thaw cycling .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "recombinant protein", "type": "Chemical"}, {"text": "rIBPv", "type": "Chemical"}, {"text": "hysteresis", "type": "Finding"}, {"text": "ice", "type": "Chemical"}]}

Example input:
Sentence: It encodes a protein of 726 amino acids with a calculated molecular mass of 82 , 610 .

Example answer:
{"entities": [{"text": "protein", "type": "Chemical"}, {"text": "amino acids", "type": "Chemical"}]}

Example input:
Sentence: The recombinant protein was expressed at high yields in Pichia pastoris ( 30 mg / L culture ) .

Example answer:
{"entities": [{"text": "recombinant protein", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "Pichia pastoris", "type": "Eukaryote"}, {"text": "culture", "type": "Chemical"}]}

Input:
Sentence: The recombinant protein corresponded to the expected molecular mass of 25 .

## Item MedMentions:test:1306
Example input:
Sentence: Re - analysing raw sequence and metadata from several studies uniformly , we sought to identify a composite and generalisable microbial marker for CRC .

Example answer:
{"entities": [{"text": "Re - analysing", "type": "ResearchActivity"}, {"text": "sequence", "type": "SpatialConcept"}, {"text": "metadata", "type": "IntellectualProduct"}, {"text": "studies", "type": "HealthCareActivity"}, {"text": "microbial marker", "type": "ClinicalAttribute"}, {"text": "CRC", "type": "BiologicFunction"}]}

Example input:
Sentence: The bioinformatic analysis based on the graphical representation of the matrix of Euclidean distances , the principal components analysis , unweighted pair group method with arithmetic mean , and principal coordinate analysis ( PCoA ) revealed three major clusters which were not correlated with the geographic origin .

Example answer:
{"entities": [{"text": "bioinformatic", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "matrix of Euclidean distances", "type": "ResearchActivity"}, {"text": "unweighted pair group method", "type": "ResearchActivity"}, {"text": "principal coordinate analysis", "type": "ResearchActivity"}, {"text": "PCoA", "type": "ResearchActivity"}, {"text": "geographic", "type": "SpatialConcept"}, {"text": "origin", "type": "Finding"}]}

Example input:
Sentence: Meta - analysis approaches for haplotype analysis have not been extensively developed and used , and have not been compared with other ways of jointly analysing multiple genetic variants .

Example answer:
{"entities": [{"text": "Meta - analysis", "type": "ResearchActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "analysing multiple genetic variants", "type": "HealthCareActivity"}]}

Example input:
Sentence: This has implications for the application of dental microwear analysis to fossils : only homologous facets can be compared , even when the molar row seems to constitute a functional unit .

Example answer:
{"entities": [{"text": "dental microwear", "type": "InjuryOrPoisoning"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "facets", "type": "SpatialConcept"}, {"text": "molar", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The use of informativity in the development of robust viromics -based examinations Metagenomics -based studies have provided insight into many of the complex microbial communities responsible for maintaining life on this planet .

Example answer:
{"entities": [{"text": "robust viromics", "type": "AnatomicalStructure"}, {"text": "examinations", "type": "ResearchActivity"}, {"text": "maintaining life on this planet", "type": "HealthCareActivity"}]}

Example input:
Sentence: Metabolomics integrated with proteomics data were used to analyze the anaphylactoid pathways by MetaboAnalyst followed by integrated pathway analysis .

Example answer:
{"entities": [{"text": "Metabolomics", "type": "Chemical"}, {"text": "proteomics data", "type": "IntellectualProduct"}, {"text": "analyze", "type": "ResearchActivity"}, {"text": "pathways", "type": "BiologicFunction"}, {"text": "MetaboAnalyst", "type": "IntellectualProduct"}, {"text": "pathway analysis", "type": "IntellectualProduct"}]}

Example input:
Sentence: Discrepancies were likely due to biased PCR amplification in metabarcoding , low discriminating power of current marker genes for monocots , and biases in microhistologic analysis .

Example answer:
{"entities": [{"text": "Discrepancies", "type": "Finding"}, {"text": "PCR", "type": "ResearchActivity"}, {"text": "amplification", "type": "BiologicFunction"}, {"text": "metabarcoding", "type": "ResearchActivity"}, {"text": "marker genes", "type": "AnatomicalStructure"}, {"text": "monocots", "type": "Eukaryote"}, {"text": "microhistologic analysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using the same samples , microhistology provided consistent food composition with metabarcoding results for greater white - fronted goose , while 13 % of Poaceae was recovered for bean goose .

Example answer:
{"entities": [{"text": "microhistology", "type": "HealthCareActivity"}, {"text": "food composition", "type": "Food"}, {"text": "metabarcoding", "type": "ResearchActivity"}, {"text": "greater white - fronted goose", "type": "Eukaryote"}, {"text": "Poaceae", "type": "Eukaryote"}, {"text": "bean goose", "type": "Eukaryote"}]}

Example input:
Sentence: We concluded that DNA metabarcoding provides new perspectives for studies of herbivorous waterbird diets and inter - specific interactions , as well as new possibilities to investigate interactions between herbivores and plants .

Example answer:
{"entities": [{"text": "DNA metabarcoding", "type": "ResearchActivity"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "herbivorous", "type": "Eukaryote"}, {"text": "waterbird", "type": "Eukaryote"}, {"text": "diets", "type": "Food"}, {"text": "herbivores", "type": "Eukaryote"}, {"text": "plants", "type": "Eukaryote"}]}

Example input:
Sentence: Although most of the identified taxa matched relatively well between the two methods , DNA metabarcoding gave taxonomically more detailed information .

Example answer:
{"entities": [{"text": "DNA metabarcoding", "type": "ResearchActivity"}]}

Input:
Sentence: In addition , microhistologic analysis should be used together with metabarcoding methods to integrate this information .

## Item MedMentions:test:334
Example input:
Sentence: A high prevalence of periradicular radiolucencies was observed with root canal filled teeth , along with high numbers of unmet treatment needs .

Example answer:
{"entities": [{"text": "periradicular radiolucencies", "type": "Finding"}, {"text": "root canal filled teeth", "type": "AnatomicalStructure"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Influence of dentin thickness on intrapulpal temperature under simulated pulpal pressure during Nd : YAG laser irradiation The aim of this study was to evaluate the effects of dentin thickness and pulpal pressure simulation ( PPS ) on the variation of intrapulpal temperature ( ∆T ) when submitted to an adhesive technique using laser irradiation .

Example answer:
{"entities": [{"text": "dentin", "type": "BodySubstance"}, {"text": "intrapulpal", "type": "AnatomicalStructure"}, {"text": "study", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}]}

Example input:
Sentence: The SBS of APC brackets decreased by 33 . 3 % on application of diode laser without increasing the internal pulp chamber wall temperature significantly .

Example answer:
{"entities": [{"text": "APC", "type": "Chemical"}, {"text": "brackets", "type": "MedicalDevice"}, {"text": "diode laser", "type": "MedicalDevice"}, {"text": "internal", "type": "SpatialConcept"}, {"text": "pulp chamber wall", "type": "SpatialConcept"}]}

Example input:
Sentence: Low - intensity pulsed ultrasound reduces periodontal atrophy in occlusal hypofunctional teeth To clarify whether low - intensity pulsed ultrasound ( LIPUS ) exposure has recovery effects on the hypofunctional periodontal ligament ( PDL ) and interradicular alveolar bone ( IRAB ) .

Example answer:
{"entities": [{"text": "periodontal atrophy", "type": "BiologicFunction"}, {"text": "occlusal", "type": "BiologicFunction"}, {"text": "teeth", "type": "AnatomicalStructure"}, {"text": "periodontal ligament", "type": "AnatomicalStructure"}, {"text": "PDL", "type": "AnatomicalStructure"}, {"text": "interradicular alveolar bone", "type": "AnatomicalStructure"}, {"text": "IRAB", "type": "AnatomicalStructure"}]}

Example input:
Sentence: For each tooth , the presence of periradicular pathosis and / or endodontic treatment was recorded , as was the quality of ( post - ) endodontic treatment ( homogeneity and length of root canal fillings ; preparation failures ; posts / screws ; apicoectomies ; coronal restorations ) .

Example answer:
{"entities": [{"text": "tooth", "type": "AnatomicalStructure"}, {"text": "presence", "type": "Finding"}, {"text": "periradicular pathosis", "type": "BiologicFunction"}, {"text": "endodontic treatment", "type": "HealthCareActivity"}, {"text": "root canal fillings", "type": "HealthCareActivity"}, {"text": "preparation failures", "type": "Finding"}, {"text": "posts", "type": "MedicalDevice"}, {"text": "screws", "type": "MedicalDevice"}, {"text": "apicoectomies", "type": "HealthCareActivity"}, {"text": "coronal restorations", "type": "HealthCareActivity"}]}

Example input:
Sentence: We showed that the formulation Pc9 - T1107 was efficient to reduce cell viability after photodynamic treatment both in 2D cultures ( IC50 10±2nM ) as well as in CT26 spheroids ( IC50 370±11nM ) .

Example answer:
{"entities": [{"text": "Pc9", "type": "Chemical"}, {"text": "T1107", "type": "Chemical"}, {"text": "cell viability", "type": "BiologicFunction"}, {"text": "photodynamic treatment", "type": "HealthCareActivity"}, {"text": "2D", "type": "SpatialConcept"}, {"text": "cultures", "type": "HealthCareActivity"}, {"text": "CT26 spheroids", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In the first group , PDT with methylene blue ( MB ) and diode laser ( 810 nm , 0 . 2 W , 40 seconds ) was performed and in the second group diode laser ( 810 nm , 1 . 2 W , 30 seconds ) was irradiated .

Example answer:
{"entities": [{"text": "methylene blue", "type": "Chemical"}, {"text": "MB", "type": "Chemical"}, {"text": "diode laser", "type": "MedicalDevice"}]}

Example input:
Sentence: Clinical - microbiological research of action ozone therapy and light - emetting diode radiation of red range ( 630 nanometers ) on microflora of the hole extracted toothatalveolitis and limited osteomyelitis of jaws As a result of cliniko - microbiological research the data testifying to substantial improvement of efficiency of antimicrobictherape at inclusion in a complex of medical actions at alveolitis and the limited osteomyelitis of a jow ozone therapy in a combination with a light - emettinf diode irradiation of the hole extracted teeth red ( 630 nanometers ) are obtained by light .

Example answer:
{"entities": [{"text": "Clinical - microbiological research", "type": "ResearchActivity"}, {"text": "action ozone therapy", "type": "HealthCareActivity"}, {"text": "hole extracted", "type": "HealthCareActivity"}, {"text": "toothatalveolitis", "type": "BiologicFunction"}, {"text": "limited osteomyelitis", "type": "BiologicFunction"}, {"text": "jaws", "type": "AnatomicalStructure"}, {"text": "cliniko - microbiological research", "type": "ResearchActivity"}, {"text": "antimicrobictherape", "type": "HealthCareActivity"}]}

Example input:
Sentence: The Antibacterial Effect of Additional Photodynamic Therapy in Failed Endodontically Treated Teeth : A Pilot Study Introduction : Root canal therapy as a routine dental procedure has resulted in retention of millions of teeth that would otherwise be lost .

Example answer:
{"entities": [{"text": "Antibacterial Effect", "type": "BiologicFunction"}, {"text": "Photodynamic Therapy", "type": "HealthCareActivity"}, {"text": "Endodontically Treated Teeth", "type": "BiologicFunction"}, {"text": "Pilot Study", "type": "ResearchActivity"}, {"text": "Root canal therapy", "type": "HealthCareActivity"}, {"text": "dental procedure", "type": "HealthCareActivity"}, {"text": "teeth", "type": "AnatomicalStructure"}]}

Example input:
Sentence: PDT and diode laser 810 nm irradiation are effective methods for root canal disinfection .

Example answer:
{"entities": [{"text": "diode laser", "type": "MedicalDevice"}, {"text": "root canal", "type": "SpatialConcept"}, {"text": "disinfection", "type": "HealthCareActivity"}]}

Input:
Sentence: Comparison of the Antibacterial Effect of 810 nm Diode Laser and Photodynamic Therapy in Reducing the Microbial Flora of Root Canal in Endodontic Retreatment in Patients With Periradicular Lesions The aim of this study was to compare the antibacterial efficacy of diode laser 810 nm and photodynamic therapy ( PDT ) in reducing bacterial microflora in endodontic retreatment of teeth with periradicular lesion .

## Item MedMentions:test:1385
Example input:
Sentence: parvus HANDI 309 is a novel bacterial strain that has the ability to produce an enormous amount of exo - chitinase - producing bio - agents in a short time on an industrial scale without any pretreatment , as well as being potentially valuable in the food and pharmaceutical industries .

Example answer:
{"entities": [{"text": "parvus HANDI 309", "type": "Bacterium"}, {"text": "bacterial", "type": "Bacterium"}, {"text": "exo - chitinase", "type": "Chemical"}, {"text": "bio - agents", "type": "Chemical"}, {"text": "pharmaceutical industries", "type": "Organization"}]}

Example input:
Sentence: rubrum survival was not affected in contact with purified OA , DTX - 1 and PTX - 2 solutions , but decreased significantly when the ciliate was exposed to cell - free or filtered culture medium from both D .

Example answer:
{"entities": [{"text": "rubrum", "type": "Eukaryote"}, {"text": "survival", "type": "BiologicFunction"}, {"text": "OA", "type": "Chemical"}, {"text": "DTX - 1", "type": "Chemical"}, {"text": "PTX - 2", "type": "Chemical"}, {"text": "ciliate", "type": "Eukaryote"}, {"text": "culture medium", "type": "Chemical"}, {"text": "D .", "type": "Eukaryote"}]}

Example input:
Sentence: The recombinant protein was expressed at high yields in Pichia pastoris ( 30 mg / L culture ) .

Example answer:
{"entities": [{"text": "recombinant protein", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "Pichia pastoris", "type": "Eukaryote"}, {"text": "culture", "type": "Chemical"}]}

Example input:
Sentence: In vitro antifungal , probiotic , and antioxidant functional properties of a novel Lactobacillus paraplantarum isolated from fermented dates in Saudi Arabia Fermented foods produced using dates are used in Gulf countries as beneficial and healthful foods .

Example answer:
{"entities": [{"text": "probiotic", "type": "Chemical"}, {"text": "antioxidant", "type": "Chemical"}, {"text": "Lactobacillus paraplantarum", "type": "Bacterium"}, {"text": "fermented", "type": "Food"}, {"text": "dates", "type": "Food"}, {"text": "Saudi Arabia", "type": "SpatialConcept"}, {"text": "Fermented foods", "type": "Food"}, {"text": "Gulf countries", "type": "SpatialConcept"}, {"text": "healthful foods", "type": "Food"}]}

Example input:
Sentence: The QH - 12 genome analysis revealed the presence of putative hydrolase / esterase genes involved in PAEs - degradation but no phthalic acid catabolic gene cluster was found , suggesting that a novel degradation pathway of PAEs was present in Gordonia sp .

Example answer:
{"entities": [{"text": "QH - 12", "type": "Bacterium"}, {"text": "genome analysis", "type": "HealthCareActivity"}, {"text": "putative hydrolase", "type": "AnatomicalStructure"}, {"text": "esterase genes", "type": "AnatomicalStructure"}, {"text": "PAEs", "type": "Chemical"}, {"text": "degradation", "type": "BiologicFunction"}, {"text": "phthalic acid", "type": "Chemical"}, {"text": "gene cluster", "type": "AnatomicalStructure"}, {"text": "Gordonia sp .", "type": "Bacterium"}]}

Example input:
Sentence: The S . aureus lipase ( SAL ) was purified to homogeneity .

Example answer:
{"entities": [{"text": "S . aureus", "type": "Bacterium"}, {"text": "lipase", "type": "Chemical"}, {"text": "SAL", "type": "Chemical"}]}

Example input:
Sentence: After partitioning , purification was conducted using a Florisil ( ® ) cartridge .

Example answer:
{"entities": []}

Example input:
Sentence: pastoris was compared in continuous cultures growing at the same µ at either 22 or 30 ° C .

Example answer:
{"entities": [{"text": "pastoris", "type": "Eukaryote"}, {"text": "cultures", "type": "HealthCareActivity"}]}

Example input:
Sentence: ( P . pastoris ) GS115 .

Example answer:
{"entities": [{"text": "( P . pastoris ) GS115", "type": "Eukaryote"}]}

Example input:
Sentence: pastoris as an expression system is the production and secretion of recombinant proteins in the supernatant , ruling out the difficulties encountered when scFv are produced in the cytoplasm of bacteria ( low yield , low solubility and reduced affinity ) .

Example answer:
{"entities": [{"text": "pastoris", "type": "Eukaryote"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "secretion", "type": "BiologicFunction"}, {"text": "recombinant proteins", "type": "Chemical"}, {"text": "supernatant", "type": "BodySubstance"}, {"text": "scFv", "type": "Chemical"}, {"text": "cytoplasm", "type": "AnatomicalStructure"}, {"text": "bacteria", "type": "Bacterium"}, {"text": "affinity", "type": "BiologicFunction"}]}

Input:
Sentence: pastoris , and it could be purified .

## Item MedMentions:test:1188
Example input:
Sentence: Evolution of H5 highly pathogenic avian influenza : sequence data indicate stepwise changes in the cleavage site The genetic composition of an H5 subtype hemagglutinin gene quasispecies , obtained from ostrich tissues that had been infected with H5 subtype influenza virus was analysed using a next generation sequencing approach .

Example answer:
{"entities": [{"text": "Evolution", "type": "BiologicFunction"}, {"text": "H5 highly pathogenic avian influenza", "type": "Virus"}, {"text": "sequence", "type": "SpatialConcept"}, {"text": "cleavage site", "type": "SpatialConcept"}, {"text": "H5 subtype hemagglutinin gene", "type": "AnatomicalStructure"}, {"text": "quasispecies", "type": "Virus"}, {"text": "ostrich", "type": "Eukaryote"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "infected", "type": "BiologicFunction"}, {"text": "H5 subtype influenza virus", "type": "Virus"}, {"text": "next generation sequencing approach", "type": "ResearchActivity"}]}

Example input:
Sentence: Influenza A ( H1N1 ) pdm09 outbreak was confirmed in inter - seasonal months during the surveillance of ILI in Pune , India , 2012 - 2015 .

Example answer:
{"entities": [{"text": "Influenza A ( H1N1 ) pdm09", "type": "Virus"}, {"text": "ILI", "type": "BiologicFunction"}, {"text": "India", "type": "SpatialConcept"}]}

Example input:
Sentence: The influenza A virus exhibited a clear cluster pattern within this patient population .

Example answer:
{"entities": [{"text": "influenza A virus", "type": "Virus"}, {"text": "pattern", "type": "SpatialConcept"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: cholerae O1 strains serving as a source for recurrent cholera epidemics and pandemic disease .

Example answer:
{"entities": [{"text": "cholerae O1", "type": "Bacterium"}, {"text": "source", "type": "Finding"}, {"text": "cholera epidemics", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: These findings raise the question whether the yellow fever vaccine strain may , through a potential molecular mimicry mechanism , be another infectious trigger for this neuro - immunological disorder .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "question", "type": "IntellectualProduct"}, {"text": "yellow fever vaccine strain", "type": "Chemical"}, {"text": "molecular mimicry", "type": "BiologicFunction"}, {"text": "infectious trigger", "type": "ClinicalAttribute"}, {"text": "neuro - immunological", "type": "BiologicFunction"}, {"text": "disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: Influenza A ( H1N1 ) pdm09 outbreak detected in inter - seasonal months during the surveillance of influenza - like illness in Pune , India , 2012 - 2015 An outbreak of influenza A ( H1N1 ) pdm09 was detected during the ongoing community - based surveillance of influenza - like illness ( ILI ) .

Example answer:
{"entities": [{"text": "Influenza A ( H1N1 ) pdm09", "type": "Virus"}, {"text": "detected", "type": "Finding"}, {"text": "influenza - like illness", "type": "BiologicFunction"}, {"text": "India", "type": "SpatialConcept"}, {"text": "influenza A ( H1N1 ) pdm09", "type": "Virus"}, {"text": "community - based surveillance", "type": "HealthCareActivity"}, {"text": "ILI", "type": "BiologicFunction"}]}

Example input:
Sentence: The findings of this study on replacement mechanisms could lead to a better understanding of virus transmission dynamics and may possibly be helpful in establishing an effective strategy to mitigate the impact of seasonal and pandemic influenza .

Example answer:
{"entities": [{"text": "virus transmission", "type": "BiologicFunction"}, {"text": "seasonal", "type": "BiologicFunction"}, {"text": "pandemic influenza", "type": "BiologicFunction"}]}

Example input:
Sentence: Low - Pathogenic Influenza A Viruses in North American Diving Ducks Contribute to the Emergence of a Novel Highly Pathogenic Influenza A ( H7N8 ) Virus Introductions of low - pathogenic avian influenza ( LPAI ) viruses of subtypes H5 and H7 into poultry from wild birds have the potential to mutate to highly pathogenic avian influenza ( HPAI ) viruses , but such viruses ' origins are often unclear .

Example answer:
{"entities": [{"text": "Low - Pathogenic Influenza A Viruses", "type": "Virus"}, {"text": "North American", "type": "Finding"}, {"text": "Diving Ducks", "type": "Eukaryote"}, {"text": "Highly Pathogenic Influenza A ( H7N8 ) Virus", "type": "Virus"}, {"text": "low - pathogenic avian influenza ( LPAI ) viruses", "type": "Virus"}, {"text": "H5", "type": "Virus"}, {"text": "H7", "type": "Virus"}, {"text": "poultry", "type": "Eukaryote"}, {"text": "wild birds", "type": "Eukaryote"}, {"text": "mutate", "type": "BiologicFunction"}, {"text": "highly pathogenic avian influenza ( HPAI ) viruses", "type": "Virus"}, {"text": "viruses", "type": "Virus"}]}

Example input:
Sentence: It is probable that the frequency of replacement by a pandemic virus is higher than a seasonal virus because of the high initial susceptibility and high basic reproductive number of the pandemic virus .

Example answer:
{"entities": [{"text": "pandemic virus", "type": "Virus"}, {"text": "seasonal virus", "type": "Virus"}, {"text": "reproductive", "type": "BiologicFunction"}]}

Example input:
Sentence: Although new antigenic variants of the influenza A virus replace formerly circulating seasonal and pandemic viruses , replacement mechanisms remain poorly understood .

Example answer:
{"entities": [{"text": "antigenic variants", "type": "BiologicFunction"}, {"text": "influenza A virus", "type": "Virus"}, {"text": "seasonal", "type": "Virus"}, {"text": "pandemic viruses", "type": "Virus"}]}

Input:
Sentence: Pandemic influenza occurs through a major antigenic change of the influenza A virus , which can originate from other hosts .

## Item MedMentions:test:1455
Example input:
Sentence: Independent reviewers extracted the data and assessed the quality of the methods of the included meta - analyses using A Measurement Tool to Assess Systematic Reviews ( AMSTAR ) , adding 6 new items to rate their quality .

Example answer:
{"entities": [{"text": "reviewers", "type": "PopulationGroup"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "meta - analyses", "type": "ResearchActivity"}, {"text": "Measurement Tool to Assess Systematic Reviews", "type": "IntellectualProduct"}, {"text": "AMSTAR", "type": "IntellectualProduct"}]}

Example input:
Sentence: Four articles meeting the inclusion criteria were included in the review .

Example answer:
{"entities": [{"text": "articles", "type": "IntellectualProduct"}]}

Example input:
Sentence: Thirteen publications , including 11 studies , met all inclusion and exclusion criteria .

Example answer:
{"entities": [{"text": "publications", "type": "IntellectualProduct"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: However , four - item short form of PCS had two misfit items .

Example answer:
{"entities": [{"text": "PCS", "type": "IntellectualProduct"}]}

Example input:
Sentence: All features were investigated for redundancy .

Example answer:
{"entities": []}

Example input:
Sentence: Three studies which examined the effectiveness of four different offloading interventions met the inclusion criteria .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "interventions", "type": "HealthCareActivity"}]}

Example input:
Sentence: Fifteen domains were derived from the qualitative methods , with content saturation achieved , resulting in 115 items .

Example answer:
{"entities": []}

Example input:
Sentence: After dropping items for low ratings of relevance and severity and for poor item - test correlation , low frequency , and / or poor acceptability in pilot testing , 16 items remained for the Disruptive Behavior International Scale - Nepali version ( DBIS - N ) .

Example answer:
{"entities": [{"text": "Disruptive Behavior International Scale - Nepali version", "type": "IntellectualProduct"}, {"text": "DBIS - N", "type": "IntellectualProduct"}]}

Example input:
Sentence: On the basis of test purpose , in 51 MPs imprecision only was used to estimate MU ; in the remaining MPs , the bias component was not estimable for 22 MPs because EQAs results did not provide reliable statistics .

Example answer:
{"entities": [{"text": "test", "type": "IntellectualProduct"}, {"text": "not", "type": "Finding"}, {"text": "EQAs", "type": "IntellectualProduct"}, {"text": "statistics", "type": "IntellectualProduct"}]}

Example input:
Sentence: Three items did not fit the partial credit model , but the generalized partial credit model could be fitted to the full item set .

Example answer:
{"entities": [{"text": "partial credit model", "type": "IntellectualProduct"}, {"text": "generalized partial credit model", "type": "IntellectualProduct"}]}

Input:
Sentence: Seven items were removed because they : ( 1 ) violated the assumption of independence ; ( 2 ) were mis - fitting ; and / or ( 3 ) were deemed not relevant .

## Item MedMentions:test:1397
Example input:
Sentence: First , a physical vapor deposition magnetron sputtering technique was used to deposit pure zirconium nanograins on top of a substrate .

Example answer:
{"entities": [{"text": "physical vapor deposition", "type": "IntellectualProduct"}, {"text": "zirconium", "type": "Chemical"}]}

Example input:
Sentence: Three oxides ( ZrO2 , Al2O3 , SiO2 ) , three metals ( 316LSS steel , Ti , Nb ) and two polymers ( corona treated polystyrene for cell culture and untreated polystyrene for bacteria culture ) , widely used for biomedical applications , were considered .

Example answer:
{"entities": [{"text": "oxides", "type": "Chemical"}, {"text": "ZrO2", "type": "Chemical"}, {"text": "Al2O3", "type": "Chemical"}, {"text": "SiO2", "type": "Chemical"}, {"text": "metals", "type": "Chemical"}, {"text": "316LSS steel", "type": "Chemical"}, {"text": "Ti", "type": "Chemical"}, {"text": "Nb", "type": "Chemical"}, {"text": "polymers", "type": "Chemical"}, {"text": "corona treated polystyrene", "type": "Chemical"}, {"text": "untreated polystyrene", "type": "Chemical"}, {"text": "bacteria culture", "type": "HealthCareActivity"}]}

Example input:
Sentence: Silk fibroin films prepared by water annealing at 25°C were the least crystalline and had Silk I structure .

Example answer:
{"entities": [{"text": "Silk fibroin", "type": "Chemical"}, {"text": "water", "type": "Chemical"}, {"text": "annealing", "type": "HealthCareActivity"}, {"text": "crystalline", "type": "Chemical"}, {"text": "Silk I", "type": "Chemical"}, {"text": "structure", "type": "Chemical"}]}

Example input:
Sentence: Intermediate crystalline fraction and mixed Silk I / Silk II structure s were found in films prepared by water annealing at 37°C .

Example answer:
{"entities": [{"text": "Intermediate", "type": "SpatialConcept"}, {"text": "crystalline", "type": "Chemical"}, {"text": "Silk I", "type": "Chemical"}, {"text": "Silk II", "type": "Chemical"}, {"text": "structure", "type": "Chemical"}, {"text": "water", "type": "Chemical"}, {"text": "annealing", "type": "HealthCareActivity"}]}

Example input:
Sentence: Monolithic zirconia restorations seem to be less susceptible to damage when endodontic access cavities have to be prepared as compared to veneered zirconia reconstructions .

Example answer:
{"entities": [{"text": "zirconia", "type": "Chemical"}, {"text": "restorations", "type": "HealthCareActivity"}, {"text": "endodontic access cavities", "type": "HealthCareActivity"}, {"text": "veneered", "type": "Chemical"}, {"text": "reconstructions", "type": "HealthCareActivity"}]}

Example input:
Sentence: Titanium dioxide and Zinc Oxide nanoparticle were synthesized by wet chemical process .

Example answer:
{"entities": [{"text": "Titanium dioxide", "type": "Chemical"}, {"text": "Zinc Oxide", "type": "Chemical"}]}

Example input:
Sentence: For TiZr alloy substrates , there is no evidence of discrete phases of oxidized Zr .

Example answer:
{"entities": [{"text": "TiZr", "type": "Chemical"}, {"text": "alloy", "type": "Chemical"}, {"text": "oxidized", "type": "BiologicFunction"}, {"text": "Zr", "type": "Chemical"}]}

Example input:
Sentence: ZrO2 nanotubular arrays with diameters of 70 - 120 nm were obtained .

Example answer:
{"entities": [{"text": "ZrO2", "type": "Chemical"}, {"text": "arrays", "type": "SpatialConcept"}]}

Example input:
Sentence: In assessing the biocompatibility of the ZrO2 surface , the human cell line MDA - MB - 231 was found to attach and proliferate well on surfaces annealed at 850 ° C and 450 ° C ; however , the amorphous ZrO2 surface , which was not heat treated , did not permit extensive cell growth , presumably due to remaining fluoride .

Example answer:
{"entities": [{"text": "ZrO2", "type": "Chemical"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "human cell line", "type": "AnatomicalStructure"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "surfaces", "type": "SpatialConcept"}, {"text": "not heat treated", "type": "Finding"}, {"text": "cell growth", "type": "BiologicFunction"}, {"text": "fluoride", "type": "Chemical"}]}

Example input:
Sentence: Only a few tetragonal peaks appeared at 850 ° C , while monoclinic ZrO2 was obtained at 900 ° C and 950 ° C .

Example answer:
{"entities": [{"text": "ZrO2", "type": "Chemical"}]}

Input:
Sentence: Both tetragonal and monoclinic ZrO2 were observed after annealing at 450 ° C and 650 ° C .

## Item MedMentions:test:686
Example input:
Sentence: 5 - Hydroxyectoine is synthesized from ectoine through a region - and stereo - specific hydroxylation reaction mediated by the EctD enzyme , a member of the non - heme - containing iron ( II ) and 2 - oxoglutarate -dependent dioxygenases .

Example answer:
{"entities": [{"text": "5 - Hydroxyectoine", "type": "Chemical"}, {"text": "ectoine", "type": "Chemical"}, {"text": "EctD enzyme", "type": "Chemical"}, {"text": "non - heme - containing iron ( II )", "type": "Chemical"}, {"text": "2 - oxoglutarate", "type": "Chemical"}, {"text": "dioxygenases", "type": "Chemical"}]}

Example input:
Sentence: Enteric neural cells expressing the light - sensitive ion channel , channelrhodopsin , were isolated from the fetal or postnatal mouse bowel and transplanted into the distal colon of 3 - to 4 - week -old wild - type recipient mice .

Example answer:
{"entities": [{"text": "Enteric", "type": "SpatialConcept"}, {"text": "neural cells", "type": "AnatomicalStructure"}, {"text": "light - sensitive ion channel", "type": "Chemical"}, {"text": "channelrhodopsin", "type": "Chemical"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "bowel", "type": "AnatomicalStructure"}, {"text": "distal colon", "type": "AnatomicalStructure"}, {"text": "wild - type", "type": "AnatomicalStructure"}, {"text": "recipient mice", "type": "Eukaryote"}]}

Example input:
Sentence: Different mutants ( ΔphoP , ΔphoQ , ΔphoPQ , ΔpmrA , ΔpmrB , ΔpmrAB , ΔarnE , ΔarnF and ΔarnBCADTEF ) were constructed and tested for their colistin hetero - resistance phenotype .

Example answer:
{"entities": [{"text": "mutants", "type": "BiologicFunction"}, {"text": "ΔphoP", "type": "AnatomicalStructure"}, {"text": "ΔphoQ", "type": "AnatomicalStructure"}, {"text": "ΔphoPQ", "type": "AnatomicalStructure"}, {"text": "ΔpmrA", "type": "AnatomicalStructure"}, {"text": "ΔpmrB", "type": "AnatomicalStructure"}, {"text": "ΔpmrAB", "type": "AnatomicalStructure"}, {"text": "ΔarnE", "type": "AnatomicalStructure"}, {"text": "ΔarnF", "type": "AnatomicalStructure"}, {"text": "ΔarnBCADTEF", "type": "AnatomicalStructure"}, {"text": "colistin", "type": "Chemical"}]}

Example input:
Sentence: Yet , tspC - cells showed a defect in coping with hypo - osmotic stress , due to accumulation of contractile vacuoles , but heterologous expression of TspC rescued their phenotype .

Example answer:
{"entities": [{"text": "contractile vacuoles", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "TspC", "type": "Chemical"}]}

Example input:
Sentence: Microorganisms producing 5 - hydroxyectoine typically contain a mixture of both ectoines .

Example answer:
{"entities": [{"text": "5 - hydroxyectoine", "type": "Chemical"}, {"text": "ectoines", "type": "Chemical"}]}

Example input:
Sentence: Ectoine was imported into the cells via the osmotically inducible ProP and ProU transport systems , intracellularly converted to 5 - hydroxyectoine , which was then almost quantitatively secreted into the growth medium .

Example answer:
{"entities": [{"text": "Ectoine", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "ProP", "type": "Chemical"}, {"text": "ProU", "type": "Chemical"}, {"text": "transport systems", "type": "BiologicFunction"}, {"text": "intracellularly", "type": "SpatialConcept"}, {"text": "5 - hydroxyectoine", "type": "Chemical"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "growth medium", "type": "Chemical"}]}

Example input:
Sentence: coli K - 12 , a classical non - environmental strain , constitutes a model of phenotypic plasticity for adaptation to a redox - cycling herbicide through redundancy of different isoforms of SOD and CAT enzymes .

Example answer:
{"entities": [{"text": "coli K - 12", "type": "Bacterium"}, {"text": "strain", "type": "Bacterium"}, {"text": "adaptation", "type": "BiologicFunction"}, {"text": "redox - cycling", "type": "BiologicFunction"}, {"text": "herbicide", "type": "Chemical"}, {"text": "isoforms", "type": "Chemical"}, {"text": "SOD", "type": "Chemical"}, {"text": "CAT enzymes", "type": "Chemical"}]}

Example input:
Sentence: We used an Escherichia coli strain ( FF4169 ) defective in the synthesis of the osmostress protectant trehalose as the chassis for our recombinant cell factory .

Example answer:
{"entities": [{"text": "Escherichia coli", "type": "Bacterium"}, {"text": "osmostress", "type": "Finding"}, {"text": "trehalose", "type": "Chemical"}, {"text": "cell factory", "type": "AnatomicalStructure"}]}

Example input:
Sentence: EctD -mediated biotransformation of the chemical chaperone ectoine into hydroxyectoine and its mechanosensitive channel -independent excretion Ectoine and its derivative 5 - hydroxyectoine are cytoprotectants widely synthesized by microorganisms as a defense against the detrimental effects of high osmolarity on cellular physiology and growth .

Example answer:
{"entities": [{"text": "EctD", "type": "Chemical"}, {"text": "chemical", "type": "Chemical"}, {"text": "chaperone", "type": "Chemical"}, {"text": "ectoine", "type": "Chemical"}, {"text": "hydroxyectoine", "type": "Chemical"}, {"text": "channel", "type": "SpatialConcept"}, {"text": "excretion", "type": "BiologicFunction"}, {"text": "Ectoine", "type": "Chemical"}, {"text": "derivative", "type": "Chemical"}, {"text": "5 - hydroxyectoine", "type": "Chemical"}, {"text": "cytoprotectants", "type": "Chemical"}, {"text": "osmolarity", "type": "ClinicalAttribute"}, {"text": "cellular physiology", "type": "BiologicFunction"}, {"text": "growth", "type": "BiologicFunction"}]}

Example input:
Sentence: We aimed to establish a recombinant microbial cell factory where 5 - hydroxyectoine is ( i ) produced in highly purified form , and ( ii ) secreted into the growth medium .

Example answer:
{"entities": [{"text": "cell factory", "type": "AnatomicalStructure"}, {"text": "5 - hydroxyectoine", "type": "Chemical"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "growth medium", "type": "Chemical"}]}

Input:
Sentence: coli mutant lacking all currently known mechanosensitive channels ( MscL , MscS , MscK , MscM ) revealed that the release of 5 - hydroxyectoine under osmotic steady - state conditions occurred independently of these microbial safety valves .

## Item MedMentions:test:816
Example input:
Sentence: Intracranial lesions are of particular significance with respect to the timing of organizing hemorrhage given the acute , and often life - threatening nature of the hemorrhages , and the medicolegal investigation into potential crimes .

Example answer:
{"entities": [{"text": "Intracranial lesions", "type": "Finding"}, {"text": "hemorrhage", "type": "BiologicFunction"}, {"text": "life - threatening", "type": "Finding"}, {"text": "hemorrhages", "type": "BiologicFunction"}, {"text": "medicolegal investigation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Future experiments aim to evaluate additional HP - related hormones and endocrine circuit pathology following diffuse TBI .

Example answer:
{"entities": [{"text": "experiments", "type": "ResearchActivity"}, {"text": "HP - related hormones", "type": "Chemical"}, {"text": "endocrine", "type": "BodySystem"}, {"text": "diffuse TBI", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Spatial cognitive deficits and chronic brain tissue loss , as well as endogenous brain repair processes such as neurogenesis , angiogenesis , and oligodendrogenesis , were evaluated up to 35 days after TBI .

Example answer:
{"entities": [{"text": "brain tissue", "type": "AnatomicalStructure"}, {"text": "brain repair processes", "type": "HealthCareActivity"}, {"text": "neurogenesis", "type": "BiologicFunction"}, {"text": "angiogenesis", "type": "BiologicFunction"}, {"text": "oligodendrogenesis", "type": "BiologicFunction"}, {"text": "TBI", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Predictors of 30 - day mortality in patients with spontaneous primary intracerebral hemorrhage Intracerebral hemorrhage ( ICH ) is a life threatening entity , and an early outcome assessment is mandatory for optimizing therapeutic efforts .

Example answer:
{"entities": [{"text": "intracerebral hemorrhage", "type": "Finding"}, {"text": "Intracerebral hemorrhage", "type": "Finding"}, {"text": "ICH", "type": "Finding"}, {"text": "life threatening", "type": "Finding"}, {"text": "early outcome assessment", "type": "HealthCareActivity"}, {"text": "therapeutic efforts", "type": "HealthCareActivity"}]}

Example input:
Sentence: Based on these factors , the HPC Score was derived ( SAH = 2 points , SDH = 1 point , and skull fracture = 1 point ) .

Example answer:
{"entities": [{"text": "HPC", "type": "InjuryOrPoisoning"}, {"text": "SAH", "type": "BiologicFunction"}, {"text": "SDH", "type": "BiologicFunction"}, {"text": "skull fracture", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: On univariate analyses , HPC was associated with older age , higher initial blood pressure , antiplatelet medications , anticoagulants , subarachnoid hemorrhage ( SAH ) subdural hematoma ( SDH ) , skull fracture , frontal contusion , larger contusion volume , and shorter interval from injury to initial CT .

Example answer:
{"entities": [{"text": "HPC", "type": "InjuryOrPoisoning"}, {"text": "higher initial blood pressure", "type": "Finding"}, {"text": "antiplatelet medications", "type": "Chemical"}, {"text": "anticoagulants", "type": "Chemical"}, {"text": "subarachnoid hemorrhage", "type": "BiologicFunction"}, {"text": "SAH", "type": "BiologicFunction"}, {"text": "subdural hematoma", "type": "BiologicFunction"}, {"text": "SDH", "type": "BiologicFunction"}, {"text": "skull fracture", "type": "InjuryOrPoisoning"}, {"text": "frontal", "type": "AnatomicalStructure"}, {"text": "contusion", "type": "InjuryOrPoisoning"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "initial CT", "type": "HealthCareActivity"}]}

Example input:
Sentence: 33 , 95 % CI , 1 . 80 - 22 . 23 ) , SDH ( OR 3 . 46 , 95 % CI , 1 . 39 - 8 . 63 ) , and skull fracture ( OR 2 . 67 , 95 % CI , 1 . 28 - 5 . 58 ) were associated with HPC .

Example answer:
{"entities": [{"text": "SDH", "type": "BiologicFunction"}, {"text": "skull fracture", "type": "InjuryOrPoisoning"}, {"text": "HPC", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The primary outcome was HPC , defined by both a relative increase in contusion volume by ≥30 % and an absolute increase by ≥10 mL on serial imaging .

Example answer:
{"entities": [{"text": "HPC", "type": "InjuryOrPoisoning"}, {"text": "contusion", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: GCS score on admission together with the baseline volume and localization of the hemorrhage are strong predictors for 30 - day mortality in patients with spontaneous primary intracerebral hemorrhage , and by relying on them it is possible to identify high - risk patients with poor short - term outcome .

Example answer:
{"entities": [{"text": "GCS", "type": "IntellectualProduct"}, {"text": "admission", "type": "HealthCareActivity"}, {"text": "hemorrhage", "type": "BiologicFunction"}, {"text": "intracerebral hemorrhage", "type": "Finding"}, {"text": "high - risk", "type": "Finding"}]}

Example input:
Sentence: A simple HPC Score was developed for early risk stratification of HPC in patients with moderate or severe TBI .

Example answer:
{"entities": [{"text": "HPC", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: Derivation of a Predictive Score for Hemorrhagic Progression of Cerebral Contusions in Moderate and Severe Traumatic Brain Injury After traumatic brain injury ( TBI ) , hemorrhagic progression of contusions ( HPCs ) occurs frequently .

## Item MedMentions:test:1030
Example input:
Sentence: On the other hand , anti - inflammatory and immunosuppressive therapies may impact in body fat storage and in liver lipid dynamics .

Example answer:
{"entities": [{"text": "anti - inflammatory", "type": "HealthCareActivity"}, {"text": "immunosuppressive therapies", "type": "HealthCareActivity"}, {"text": "body", "type": "Eukaryote"}, {"text": "fat", "type": "Chemical"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "lipid", "type": "Chemical"}]}

Example input:
Sentence: The aim of this study was to evaluate the efficacy and safety of simvastatin in addition to whole - brain radiation therapy ( WBRT ) in patients with brain metastases ( BM ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "whole - brain radiation therapy", "type": "HealthCareActivity"}, {"text": "WBRT", "type": "HealthCareActivity"}, {"text": "brain metastases", "type": "BiologicFunction"}, {"text": "BM", "type": "BiologicFunction"}]}

Example input:
Sentence: However , the association of RT dose with OS highlights the importance of identifying patients with unresected ATC who may still yet benefit from multimodal locoregional treatment that incorporates higher dose RT .

Example answer:
{"entities": [{"text": "identifying patients", "type": "HealthCareActivity"}, {"text": "unresected", "type": "IntellectualProduct"}, {"text": "ATC", "type": "BiologicFunction"}, {"text": "multimodal locoregional treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The combination of thixotropy and cytocompatibility of the gels could enable a wide range of biomedical applications such as cell delivery and orthopedic repair .

Example answer:
{"entities": [{"text": "gels", "type": "Chemical"}, {"text": "cell delivery", "type": "BiologicFunction"}, {"text": "orthopedic repair", "type": "BiologicFunction"}]}

Example input:
Sentence: On the contrary , in the setting of oligometastatic and oligoprogressive disease , new molecules demonstrated to be safe and effective , opening to a promising and emerging application of the best interaction between new drugs and new modalities of radiotherapy .

Example answer:
{"entities": [{"text": "oligometastatic", "type": "BiologicFunction"}, {"text": "oligoprogressive disease", "type": "BiologicFunction"}, {"text": "drugs", "type": "HealthCareActivity"}, {"text": "radiotherapy", "type": "IntellectualProduct"}]}

Example input:
Sentence: By searching multiple databases from 1990 to March 2016 , all randomized controlled trials ( RCTs ) which compared the effect of trastuzumab - combined chemotherapy ( TC ) versus chemotherapy alone ( CT ) in gastric cancer would be included .

Example answer:
{"entities": [{"text": "databases", "type": "IntellectualProduct"}, {"text": "randomized controlled trials", "type": "ResearchActivity"}, {"text": "RCTs", "type": "ResearchActivity"}, {"text": "trastuzumab", "type": "Chemical"}, {"text": "combined chemotherapy", "type": "HealthCareActivity"}, {"text": "TC", "type": "HealthCareActivity"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "gastric cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: The primary objective of this study is to determine the incidence and the clinical relevance of the drug - drug interactions between antineoplastic agents and regular medication used by lung cancer patients .

Example answer:
{"entities": [{"text": "drug - drug interactions", "type": "BiologicFunction"}, {"text": "antineoplastic agents", "type": "Chemical"}, {"text": "regular medication", "type": "Chemical"}, {"text": "lung cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: This novel gene therapy system could act alone , or in synergy with current therapies that modulate intracellular cholesterol , such as statins , greatly enhancing its therapeutic application for FH .

Example answer:
{"entities": [{"text": "gene therapy", "type": "HealthCareActivity"}, {"text": "modulate", "type": "SpatialConcept"}, {"text": "intracellular", "type": "SpatialConcept"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "statins", "type": "Chemical"}, {"text": "therapeutic application", "type": "HealthCareActivity"}, {"text": "FH", "type": "BiologicFunction"}]}

Example input:
Sentence: A lower chemotherapeutic load and a small number of allogeneic BMTs did not affect total positive treatment results in adult patients with ALL , by complying with the principle achieving the continuity of cytostatic effects and by preserving the total cytostatic loading dose .

Example answer:
{"entities": [{"text": "chemotherapeutic", "type": "Chemical"}, {"text": "allogeneic BMTs", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "results", "type": "Finding"}, {"text": "ALL", "type": "BiologicFunction"}, {"text": "cytostatic", "type": "Chemical"}]}

Example input:
Sentence: The most frequent interaction was between cytostatics and coumarins while the most relevant one was between cisplatin and furosemide .

Example answer:
{"entities": [{"text": "interaction", "type": "BiologicFunction"}, {"text": "cytostatics", "type": "Chemical"}, {"text": "coumarins", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "furosemide", "type": "Chemical"}]}

Input:
Sentence: Further research should focus on the clinical outcome of the interactions as well as on interactions between cytostatics and alternative medicines and / or over - the - counter medicines .

## Item MedMentions:test:1296
Example input:
Sentence: A retrospective case study was conducted of the clinical and management course of 2 patients with progressive , treatment - refractory metastatic cancer who were treated with a single dose each ( concomitantly ) of the immune checkpoint inhibitors nivolumab , 1 mg / kg , and ipilimumab , 3 mg / kg .

Example answer:
{"entities": [{"text": "retrospective case study", "type": "ResearchActivity"}, {"text": "clinical and management", "type": "HealthCareActivity"}, {"text": "refractory metastatic cancer", "type": "BiologicFunction"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "immune checkpoint inhibitors", "type": "Chemical"}, {"text": "nivolumab", "type": "Chemical"}, {"text": "ipilimumab", "type": "Chemical"}]}

Example input:
Sentence: Conclusion THL can enhance the antitumor immune responses in mice vaccinated with killed tumor cells .

Example answer:
{"entities": [{"text": "THL", "type": "Chemical"}, {"text": "immune responses", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "vaccinated", "type": "Finding"}, {"text": "tumor cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Association of Autoimmune Encephalitis With Combined Immune Checkpoint Inhibitor Treatment for Metastatic Cancer Paraneoplastic encephalitides usually precede a diagnosis of cancer and are often refractory to immunosuppressive therapy .

Example answer:
{"entities": [{"text": "Autoimmune Encephalitis", "type": "BiologicFunction"}, {"text": "Immune Checkpoint Inhibitor", "type": "Chemical"}, {"text": "Metastatic Cancer", "type": "BiologicFunction"}, {"text": "Paraneoplastic encephalitides", "type": "BiologicFunction"}, {"text": "diagnosis of cancer", "type": "HealthCareActivity"}, {"text": "immunosuppressive therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Early recognition and treatment of autoimmune encephalitis in patients receiving immune checkpoint blockade therapy will likely be essential for maximizing clinical recovery and minimizing the effect of drug - related toxic effects .

Example answer:
{"entities": [{"text": "autoimmune encephalitis", "type": "BiologicFunction"}, {"text": "immune checkpoint blockade therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: In vivo blockade of LR signalling combined with iNKT stimulation resulted in superior anti - tumor protection .

Example answer:
{"entities": [{"text": "In vivo", "type": "SpatialConcept"}, {"text": "LR", "type": "Chemical"}, {"text": "signalling", "type": "BiologicFunction"}, {"text": "iNKT", "type": "AnatomicalStructure"}, {"text": "stimulation", "type": "BiologicFunction"}, {"text": "anti - tumor protection", "type": "BiologicFunction"}]}

Example input:
Sentence: Within such infiltrated tumors , referred as " hot " , immune checkpoint inhibitors rescue anti - tumor T cells activity .

Example answer:
{"entities": [{"text": "infiltrated tumors", "type": "BiologicFunction"}, {"text": "immune", "type": "BodySystem"}, {"text": "checkpoint inhibitors", "type": "Chemical"}, {"text": "T cells activity", "type": "BiologicFunction"}]}

Example input:
Sentence: Immune checkpoint inhibition may favor the development of immune responses against neuronal antigens , leading to autoimmune encephalitis .

Example answer:
{"entities": [{"text": "Immune checkpoint inhibition", "type": "BiologicFunction"}, {"text": "immune responses", "type": "BiologicFunction"}, {"text": "autoimmune encephalitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Fading With Time of PD - L1 Immunoreactivity in Non - Small Cells Lung Cancer Tissues : A Methodological Study Blockade of inhibitory immune checkpoints is currently arising as a potential immunologic option for tumor therapy .

Example answer:
{"entities": [{"text": "Non - Small Cells Lung Cancer", "type": "BiologicFunction"}, {"text": "Tissues", "type": "AnatomicalStructure"}, {"text": "inhibitory immune checkpoints", "type": "BiologicFunction"}, {"text": "tumor therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Radiotherapy : Changing the Game in Immunotherapy Immune checkpoint inhibitors are effective in cancer treatment .

Example answer:
{"entities": [{"text": "Radiotherapy", "type": "HealthCareActivity"}, {"text": "Immunotherapy", "type": "HealthCareActivity"}, {"text": "Immune", "type": "BodySystem"}, {"text": "checkpoint inhibitors", "type": "Chemical"}, {"text": "cancer treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Preclinical data show that radiotherapy sensitizes refractory tumors to immune checkpoint inhibitors by recruiting anti - tumor T cells .

Example answer:
{"entities": [{"text": "Preclinical data", "type": "IntellectualProduct"}, {"text": "radiotherapy", "type": "HealthCareActivity"}, {"text": "refractory tumors", "type": "BiologicFunction"}, {"text": "immune", "type": "BodySystem"}, {"text": "checkpoint inhibitors", "type": "Chemical"}, {"text": "anti - tumor", "type": "Chemical"}, {"text": "T cells", "type": "AnatomicalStructure"}]}

Input:
Sentence: Such effects could potentially sensitize tumors to immunotherapies , including checkpoint blockade .
