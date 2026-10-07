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

## Item MedMentions:test:1298
Example input:
Sentence: The occurrence of immune - related adverse events and having a higher percentage of peripheral lymphocytes were predictive biomarkers of a beneficial clinical response during cancer immunotherapy for NSCLC .

Example answer:
{"entities": [{"text": "immune - related adverse events", "type": "BiologicFunction"}, {"text": "peripheral lymphocytes", "type": "HealthCareActivity"}, {"text": "predictive biomarkers", "type": "ClinicalAttribute"}, {"text": "clinical response", "type": "Finding"}, {"text": "cancer immunotherapy", "type": "HealthCareActivity"}, {"text": "NSCLC", "type": "BiologicFunction"}]}

Example input:
Sentence: Conclusion THL can enhance the antitumor immune responses in mice vaccinated with killed tumor cells .

Example answer:
{"entities": [{"text": "THL", "type": "Chemical"}, {"text": "immune responses", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "vaccinated", "type": "Finding"}, {"text": "tumor cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The hypothesis for this study was that preoperative neoadjuvant chemotherapy would shrink the tumor margins and allow an increase in R0 resection , and hence , better survival .

Example answer:
{"entities": [{"text": "tumor margins", "type": "ClinicalAttribute"}, {"text": "R0 resection", "type": "HealthCareActivity"}]}

Example input:
Sentence: Hierarchical clustering revealed three response patterns : ( i ) TIL ( high ) tumors showed increases in multiple immune markers after chemotherapy ; ( ii ) TIL ( low ) tumors underwent similar increases , achieving patterns indistinguishable from the first group ; and ( iii ) TIL ( negative ) cases generally remained negative .

Example answer:
{"entities": [{"text": "Hierarchical clustering", "type": "ResearchActivity"}, {"text": "TIL", "type": "AnatomicalStructure"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "negative", "type": "Finding"}]}

Example input:
Sentence: Results : Neoadjuvant chemotherapy was associated with increased densities of CD3 ( + ) , CD8 ( + ) , CD8 ( + ) TIA - 1 ( + ) , PD - 1 ( + ) and CD20 ( + ) TIL .

Example answer:
{"entities": [{"text": "CD3", "type": "Chemical"}, {"text": "CD8", "type": "Chemical"}, {"text": "TIA - 1", "type": "Chemical"}, {"text": "PD - 1", "type": "Chemical"}, {"text": "CD20", "type": "Chemical"}, {"text": "TIL", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In addition , our results support combination of cytokine -preactivated NK cells with CD4 ( + ) T cell activation upon lymphopenic conditioning to achieve long - term NK cell effector function for cancer immunotherapy .

Example answer:
{"entities": [{"text": "cytokine", "type": "Chemical"}, {"text": "NK cells", "type": "AnatomicalStructure"}, {"text": "CD4 ( + ) T cell", "type": "AnatomicalStructure"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "lymphopenic", "type": "BiologicFunction"}, {"text": "NK cell", "type": "AnatomicalStructure"}, {"text": "cancer immunotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Our previous studies have shown that THL can modulate immune response and inhibit tumor growth .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "THL", "type": "Chemical"}, {"text": "modulate", "type": "SpatialConcept"}, {"text": "immune response", "type": "BiologicFunction"}]}

Example input:
Sentence: A lower chemotherapeutic load and a small number of allogeneic BMTs did not affect total positive treatment results in adult patients with ALL , by complying with the principle achieving the continuity of cytostatic effects and by preserving the total cytostatic loading dose .

Example answer:
{"entities": [{"text": "chemotherapeutic", "type": "Chemical"}, {"text": "allogeneic BMTs", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "results", "type": "Finding"}, {"text": "ALL", "type": "BiologicFunction"}, {"text": "cytostatic", "type": "Chemical"}]}

Example input:
Sentence: The prognostic significance of post - chemotherapy TIL patterns was assessed in an expanded cohort ( n = 90 ) .

Example answer:
{"entities": [{"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "TIL", "type": "AnatomicalStructure"}, {"text": "cohort", "type": "PopulationGroup"}]}

Example input:
Sentence: Despite the dramatic increases seen in the first two patterns , post - chemotherapy TIL showed limited prognostic significance .

Example answer:
{"entities": [{"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "TIL", "type": "AnatomicalStructure"}]}

Input:
Sentence: Conclusions : Chemotherapy augments pre - existing TIL responses but fails to relieve major immune - suppressive mechanisms or confer significant prognostic benefit .

## Item MedMentions:test:1038
Example input:
Sentence: Recipient mice treated with this regimen showed expansion of a Foxp3 -positive regulatory T ( Treg ) cell phenotype , and formation of mixed chimera .

Example answer:
{"entities": [{"text": "Recipient mice", "type": "Eukaryote"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "regimen", "type": "HealthCareActivity"}, {"text": "expansion", "type": "BiologicFunction"}, {"text": "Foxp3", "type": "Chemical"}, {"text": "regulatory T ( Treg ) cell", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Furthermore , the nano - UCPs were superior to a traditional two - camera method for NIR and visible light path alignment in an in vivo Infrared - Laser - Evoked Gene Operator ( IR - LEGO ) optogenetics assay in the budding yeast Saccharomyces cerevisiae .

Example answer:
{"entities": [{"text": "UCPs", "type": "Chemical"}, {"text": "camera", "type": "MedicalDevice"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "Infrared - Laser - Evoked Gene Operator ( IR - LEGO ) optogenetics assay", "type": "ResearchActivity"}, {"text": "Saccharomyces cerevisiae", "type": "Eukaryote"}]}

Example input:
Sentence: Further , we suggest that the method described here , combining a cAMP - dependent luciferase reporter assay with chimeric opsins possessing the third intracellular loop of jellyfish opsin , is a versatile approach for estimating absorption spectra of opsins with unknown signaling cascades or for which absorption spectra are difficult to obtain .

Example answer:
{"entities": [{"text": "cAMP", "type": "Chemical"}, {"text": "luciferase", "type": "Chemical"}, {"text": "reporter", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "opsins", "type": "Chemical"}, {"text": "third intracellular", "type": "SpatialConcept"}, {"text": "loop", "type": "SpatialConcept"}, {"text": "jellyfish", "type": "Eukaryote"}, {"text": "opsin", "type": "Chemical"}, {"text": "absorption spectra", "type": "HealthCareActivity"}, {"text": "signaling cascades", "type": "BiologicFunction"}]}

Example input:
Sentence: These findings suggest that vertebrate Opn3s may form blue - sensitive G protein - coupled pigments .

Example answer:
{"entities": [{"text": "vertebrate", "type": "Eukaryote"}, {"text": "Opn3s", "type": "Chemical"}, {"text": "blue - sensitive G protein - coupled pigments", "type": "Chemical"}]}

Example input:
Sentence: The results suggest that Opn3 is capable of activating G protein ( s ) in a light - dependent manner .

Example answer:
{"entities": [{"text": "Opn3", "type": "Chemical"}, {"text": "G protein ( s )", "type": "Chemical"}]}

Example input:
Sentence: We then used a cAMP - dependent luciferase reporter assay to investigate light - dependent cAMP responses in cultured cells expressing zebrafish , pufferfish , anole and chicken Opn3 .

Example answer:
{"entities": [{"text": "cAMP", "type": "Chemical"}, {"text": "luciferase", "type": "Chemical"}, {"text": "reporter", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "responses", "type": "BiologicFunction"}, {"text": "cultured cells", "type": "AnatomicalStructure"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "zebrafish", "type": "Eukaryote"}, {"text": "pufferfish", "type": "Eukaryote"}, {"text": "anole", "type": "Eukaryote"}, {"text": "chicken", "type": "Eukaryote"}, {"text": "Opn3", "type": "Chemical"}]}

Example input:
Sentence: When incubated with 11 - cis retinal , zebrafish Opn3 formed a blue - sensitive photopigment with an absorption maximum around 465 nm .

Example answer:
{"entities": [{"text": "incubated", "type": "HealthCareActivity"}, {"text": "11 - cis retinal", "type": "Chemical"}, {"text": "zebrafish", "type": "Eukaryote"}, {"text": "Opn3", "type": "Chemical"}, {"text": "blue - sensitive photopigment", "type": "Chemical"}, {"text": "absorption", "type": "BiologicFunction"}]}

Example input:
Sentence: We successfully expressed zebrafish Opn3 in mammalian cultured cells and measured its absorption spectrum spectroscopically .

Example answer:
{"entities": [{"text": "expressed", "type": "BiologicFunction"}, {"text": "zebrafish", "type": "Eukaryote"}, {"text": "Opn3", "type": "Chemical"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "cultured cells", "type": "AnatomicalStructure"}, {"text": "absorption spectrum spectroscopically", "type": "HealthCareActivity"}]}

Example input:
Sentence: The inferred spectral sensitivity curve of zebrafish Opn3 accurately matched the measured absorption spectrum .

Example answer:
{"entities": [{"text": "curve", "type": "SpatialConcept"}, {"text": "zebrafish", "type": "Eukaryote"}, {"text": "Opn3", "type": "Chemical"}, {"text": "absorption spectrum", "type": "HealthCareActivity"}]}

Example input:
Sentence: We were unable to estimate the spectral sensitivity curve of mouse or anole Opn3 , but , like zebrafish Opn3 , the chicken and pufferfish Opn3 - JiL3 chimeras also formed blue - sensitive pigments .

Example answer:
{"entities": [{"text": "curve", "type": "SpatialConcept"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "anole", "type": "Eukaryote"}, {"text": "Opn3", "type": "Chemical"}, {"text": "zebrafish", "type": "Eukaryote"}, {"text": "chicken", "type": "Eukaryote"}, {"text": "pufferfish", "type": "Eukaryote"}, {"text": "Opn3 - JiL3", "type": "Chemical"}, {"text": "blue - sensitive pigments", "type": "Chemical"}]}

Input:
Sentence: Finally , we used this assay to measure the relative wavelength - dependent response of cells expressing Opn3 chimeras to multiple quantally - matched stimuli .

## Item MedMentions:test:1196
Example input:
Sentence: Assessment of CTCs may be useful in the management of high - risk EC patients .

Example answer:
{"entities": [{"text": "Assessment", "type": "HealthCareActivity"}, {"text": "CTCs", "type": "AnatomicalStructure"}, {"text": "management", "type": "HealthCareActivity"}, {"text": "high - risk", "type": "Finding"}, {"text": "EC", "type": "BiologicFunction"}]}

Example input:
Sentence: It is in the low - risk groups that one is likely to find the highest and most inappropriate indications for cesarean sections .

Example answer:
{"entities": [{"text": "cesarean sections", "type": "HealthCareActivity"}]}

Example input:
Sentence: Potentially preventable amputations associated with high - risk diseases are increasing among patients who require inpatient hospital admission , present to the ED , or require outpatient interventional treatment .

Example answer:
{"entities": [{"text": "amputations", "type": "HealthCareActivity"}, {"text": "risk", "type": "HealthCareActivity"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "hospital admission", "type": "HealthCareActivity"}, {"text": "ED", "type": "Organization"}]}

Example input:
Sentence: Although , it helps in alleviating patients ' morbidity very effectively and reliably , there are many technical glitches , which needs to be kept into account and patient should be properly counseled before the procedure to prevent and manage post procedure complications and medico legal aspects .

Example answer:
{"entities": [{"text": "counseled", "type": "HealthCareActivity"}, {"text": "procedure", "type": "HealthCareActivity"}, {"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: In addition , the authors review a screening tool , which can assist surgeons when encountering high - risk patients .

Example answer:
{"entities": [{"text": "screening", "type": "HealthCareActivity"}, {"text": "surgeons", "type": "ProfessionalOrOccupationalGroup"}, {"text": "high - risk", "type": "Finding"}]}

Example input:
Sentence: The obstetrician - gynecologist should discuss the options with patients and make clear recommendations on which route of hysterectomy will maximize benefits and minimize risks given the specific clinical situation .

Example answer:
{"entities": [{"text": "obstetrician", "type": "ProfessionalOrOccupationalGroup"}, {"text": "gynecologist", "type": "ProfessionalOrOccupationalGroup"}, {"text": "route", "type": "SpatialConcept"}, {"text": "hysterectomy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Over one third of high - risk patients ' requests were unfulfilled , indicating that significant barriers may remain .

Example answer:
{"entities": [{"text": "high - risk", "type": "Finding"}]}

Example input:
Sentence: Because of extended appointment lead - time , women with high - risk pregnancy could develop severe complications in their health status and put their babies at risk .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "high - risk pregnancy", "type": "BiologicFunction"}, {"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: Though women with high - risk pregnancies were more likely to request PPTL , they were not more likely to complete the procedure .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "high - risk pregnancies", "type": "BiologicFunction"}, {"text": "PPTL", "type": "HealthCareActivity"}, {"text": "procedure", "type": "HealthCareActivity"}]}

Example input:
Sentence: Though women with high - risk pregnancies were more likely to request PPTL , they were not more likely to complete the procedure .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "high - risk pregnancies", "type": "BiologicFunction"}, {"text": "PPTL", "type": "HealthCareActivity"}, {"text": "procedure", "type": "HealthCareActivity"}]}

Input:
Sentence: Providers should consider these procedures urgent , especially in high - risk women , and advocate for their patients ' access to this procedure .

## Item MedMentions:test:1350
Example input:
Sentence: Half a century later , in 2015 , research on hepatitis and upper GI diseases had not changed significantly ; however , studies on pancreatitis had dropped to 10 . 7 % , while work on the lower GI disorders had risen to 23 .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "hepatitis", "type": "BiologicFunction"}, {"text": "upper", "type": "SpatialConcept"}, {"text": "GI diseases", "type": "BiologicFunction"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "pancreatitis", "type": "BiologicFunction"}, {"text": "work", "type": "ResearchActivity"}, {"text": "lower", "type": "SpatialConcept"}, {"text": "GI disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: Also , the probability of toxicity for organs and tissues was classified as moderate and high for liver and kidney , and moderate and low for skin and eye irritation , respectively .

Example answer:
{"entities": [{"text": "organs", "type": "AnatomicalStructure"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "kidney", "type": "AnatomicalStructure"}, {"text": "skin", "type": "Finding"}, {"text": "eye irritation", "type": "Finding"}]}

Example input:
Sentence: Histologic changes were limited to interstitial hematopoietic areas of the kidney and consisted of small foci of necrosis accompanied by fibrin deposition , minimal inflammatory response , and small numbers of bacterial cocci compatible with streptococci .

Example answer:
{"entities": [{"text": "interstitial", "type": "SpatialConcept"}, {"text": "hematopoietic areas", "type": "AnatomicalStructure"}, {"text": "kidney", "type": "AnatomicalStructure"}, {"text": "foci", "type": "SpatialConcept"}, {"text": "necrosis", "type": "BiologicFunction"}, {"text": "fibrin deposition", "type": "BiologicFunction"}, {"text": "inflammatory response", "type": "BiologicFunction"}, {"text": "bacterial cocci", "type": "Bacterium"}, {"text": "streptococci", "type": "Bacterium"}]}

Example input:
Sentence: Such an increase was however never found in their blood , kidneys or brain .

Example answer:
{"entities": [{"text": "blood", "type": "BodySubstance"}, {"text": "kidneys", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Urine samples from 199 patients ( 90 patients without organ failure [ Group 1 ] , 58 patients with organ failure excluding renal failure [ Group 2 ] , and 51 patients with organ failure including renal failure [ Group 3 ] ) from the CANONIC study were analyzed for urine AQP2 and urine osmolality .

Example answer:
{"entities": [{"text": "Urine samples", "type": "BodySubstance"}, {"text": "organ failure", "type": "Finding"}, {"text": "renal failure", "type": "BiologicFunction"}, {"text": "CANONIC study", "type": "ResearchActivity"}, {"text": "urine", "type": "BodySubstance"}, {"text": "AQP2", "type": "Chemical"}, {"text": "urine osmolality", "type": "ClinicalAttribute"}]}

Example input:
Sentence: This resolved hyponatraemia , and there was no further increase in renal size .

Example answer:
{"entities": [{"text": "hyponatraemia", "type": "BiologicFunction"}, {"text": "renal size", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The aim of the study was to evaluate AQP2 as a predictor of renal insufficiency and death in patients with cirrhosis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "AQP2", "type": "Chemical"}, {"text": "predictor", "type": "IntellectualProduct"}, {"text": "renal insufficiency", "type": "BiologicFunction"}, {"text": "death", "type": "BiologicFunction"}, {"text": "cirrhosis", "type": "BiologicFunction"}]}

Example input:
Sentence: The results revealed that VCD increased markers of liver and kidney functions , oxidative damage and inflammation , and disrupted the antioxidant homeostasis of the rats ( p < 0 .

Example answer:
{"entities": [{"text": "VCD", "type": "Chemical"}, {"text": "markers", "type": "ClinicalAttribute"}, {"text": "liver", "type": "BiologicFunction"}, {"text": "kidney functions", "type": "BiologicFunction"}, {"text": "oxidative damage", "type": "InjuryOrPoisoning"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "antioxidant homeostasis", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: Hepatic function did not appear to be significantly modified makes no evidence of necrosis and suggesting other cell death pathway , the autophagic .

Example answer:
{"entities": [{"text": "Hepatic function", "type": "BiologicFunction"}, {"text": "necrosis", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "autophagic", "type": "BiologicFunction"}]}

Example input:
Sentence: Liver and renal function tests were normal .

Example answer:
{"entities": [{"text": "Liver", "type": "HealthCareActivity"}, {"text": "renal function tests", "type": "HealthCareActivity"}]}

Input:
Sentence: There was no worsening of renal or hepatic function in any group .

## Item MedMentions:test:1436
Example input:
Sentence: Frail patients were more likely to have post - operative complications ( 47 % vs .

Example answer:
{"entities": [{"text": "Frail", "type": "Finding"}, {"text": "post - operative complications", "type": "BiologicFunction"}]}

Example input:
Sentence: Sixteen patients ( 31 % ) had complete pathological response .

Example answer:
{"entities": [{"text": "complete pathological response", "type": "Finding"}]}

Example input:
Sentence: Only 2 % of those treated were transferred to hospital through EMS .

Example answer:
{"entities": [{"text": "hospital", "type": "Organization"}, {"text": "EMS", "type": "HealthCareActivity"}]}

Example input:
Sentence: 56 patients ( 44 % ) had a complete ( 7 % ) or partial response ( 37 % ) .

Example answer:
{"entities": [{"text": "response", "type": "Finding"}]}

Example input:
Sentence: The majority of patients had full recovery or recovery with residual effects .

Example answer:
{"entities": [{"text": "recovery", "type": "BiologicFunction"}]}

Example input:
Sentence: Twelve ( 11 . 7 % ) patients had complications in recovery , principally nausea and vomiting .

Example answer:
{"entities": [{"text": "nausea", "type": "Finding"}, {"text": "vomiting", "type": "Finding"}]}

Example input:
Sentence: Two patients ( 7 . 7 % ) needed re - operation due to nonunion .

Example answer:
{"entities": [{"text": "re - operation", "type": "HealthCareActivity"}, {"text": "nonunion", "type": "Finding"}]}

Example input:
Sentence: Thirty - four percent ( 1632 / 4799 ) reported recovery .

Example answer:
{"entities": [{"text": "recovery", "type": "BiologicFunction"}]}

Example input:
Sentence: 9 - 82 . 9 % ) who did not use rescue medication during the OP .

Example answer:
{"entities": [{"text": "rescue medication", "type": "HealthCareActivity"}]}

Example input:
Sentence: 36 . 8 % patients arrived to the hospital without any first aid .

Example answer:
{"entities": [{"text": "patients arrived", "type": "Finding"}, {"text": "hospital", "type": "Organization"}, {"text": "first aid", "type": "HealthCareActivity"}]}

Input:
Sentence: Eighty - nine per cent returned to the event with no need for further medical care .

## Item MedMentions:test:1495
Example input:
Sentence: The OS of group B ( HR , 0 . 450 ; 95 % confidence interval , 0 . 118 - 1 . 717 ; P = .243 ) was not statistically different from that of group C .

Example answer:
{"entities": []}

Example input:
Sentence: The median OS of group A ( not reached ) was better than that of group B ( 34 . 4 months ) and group C ( 15 . 2 months ) ( P = .009 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 88 % lower than in Group B ( 25 . 60±6 .

Example answer:
{"entities": []}

Example input:
Sentence: Group C received GLA and no irradiation .

Example answer:
{"entities": [{"text": "GLA", "type": "Chemical"}, {"text": "irradiation", "type": "HealthCareActivity"}]}

Example input:
Sentence: 4 was significantly greater than that of the BCG and control group ( p < 0 .

Example answer:
{"entities": [{"text": "4", "type": "Chemical"}, {"text": "BCG", "type": "Chemical"}]}

Example input:
Sentence: The Ten - group classification helped to identify the main groups of subjects who contribute most to the overall CSR .

Example answer:
{"entities": [{"text": "Ten - group classification", "type": "IntellectualProduct"}]}

Example input:
Sentence: Between group comparison : The CD4 + percentage of group E was higher than that of group P ( P < 0 .

Example answer:
{"entities": [{"text": "CD4 + percentage", "type": "HealthCareActivity"}]}

Example input:
Sentence: 40 % higher than in Group B ( 354 .

Example answer:
{"entities": []}

Example input:
Sentence: The largest contributions to the total CSR are group 1 ( 37 . 62 % ) and group 5 ( 17 . 06 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Group 3 which was the second largest group contributed 15 % to the overall CSR .

Example answer:
{"entities": []}

Input:
Sentence: Group 2 and group 4 had high group CSRs of 47 .

## Item MedMentions:test:1187
Example input:
Sentence: Low - Pathogenic Influenza A Viruses in North American Diving Ducks Contribute to the Emergence of a Novel Highly Pathogenic Influenza A ( H7N8 ) Virus Introductions of low - pathogenic avian influenza ( LPAI ) viruses of subtypes H5 and H7 into poultry from wild birds have the potential to mutate to highly pathogenic avian influenza ( HPAI ) viruses , but such viruses ' origins are often unclear .

Example answer:
{"entities": [{"text": "Low - Pathogenic Influenza A Viruses", "type": "Virus"}, {"text": "North American", "type": "Finding"}, {"text": "Diving Ducks", "type": "Eukaryote"}, {"text": "Highly Pathogenic Influenza A ( H7N8 ) Virus", "type": "Virus"}, {"text": "low - pathogenic avian influenza ( LPAI ) viruses", "type": "Virus"}, {"text": "H5", "type": "Virus"}, {"text": "H7", "type": "Virus"}, {"text": "poultry", "type": "Eukaryote"}, {"text": "wild birds", "type": "Eukaryote"}, {"text": "mutate", "type": "BiologicFunction"}, {"text": "highly pathogenic avian influenza ( HPAI ) viruses", "type": "Virus"}, {"text": "viruses", "type": "Virus"}]}

Example input:
Sentence: Highly sensitive detection of influenza virus by boron - doped diamond electrode terminated with sialic acid - mimic peptide The progression of influenza varies according to age and the presence of an underlying disease ; appropriate treatment is therefore required to prevent severe disease .

Example answer:
{"entities": [{"text": "Highly sensitive detection of influenza virus", "type": "HealthCareActivity"}, {"text": "boron - doped diamond electrode", "type": "MedicalDevice"}, {"text": "sialic acid - mimic peptide", "type": "Chemical"}, {"text": "progression of influenza", "type": "BiologicFunction"}, {"text": "underlying disease", "type": "BiologicFunction"}, {"text": "appropriate treatment", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Factors and conditions of virus and host populations affecting the replacement were identified .

Example answer:
{"entities": [{"text": "virus", "type": "Virus"}]}

Example input:
Sentence: Influenza A ( H1N1 ) pdm09 outbreak detected in inter - seasonal months during the surveillance of influenza - like illness in Pune , India , 2012 - 2015 An outbreak of influenza A ( H1N1 ) pdm09 was detected during the ongoing community - based surveillance of influenza - like illness ( ILI ) .

Example answer:
{"entities": [{"text": "Influenza A ( H1N1 ) pdm09", "type": "Virus"}, {"text": "detected", "type": "Finding"}, {"text": "influenza - like illness", "type": "BiologicFunction"}, {"text": "India", "type": "SpatialConcept"}, {"text": "influenza A ( H1N1 ) pdm09", "type": "Virus"}, {"text": "community - based surveillance", "type": "HealthCareActivity"}, {"text": "ILI", "type": "BiologicFunction"}]}

Example input:
Sentence: Influenza A ( H1N1 ) pdm09 outbreak was confirmed in inter - seasonal months during the surveillance of ILI in Pune , India , 2012 - 2015 .

Example answer:
{"entities": [{"text": "Influenza A ( H1N1 ) pdm09", "type": "Virus"}, {"text": "ILI", "type": "BiologicFunction"}, {"text": "India", "type": "SpatialConcept"}]}

Example input:
Sentence: transmissibility , infectious period and duration of immunity ) , seasonality , interaction with other circulating strains and hosts ' mixing and spatial fragmentation .

Example answer:
{"entities": [{"text": "transmissibility", "type": "BiologicFunction"}, {"text": "infectious", "type": "BiologicFunction"}, {"text": "immunity", "type": "BiologicFunction"}]}

Example input:
Sentence: The use of monoclonal antibodies is a rapidly developing strategy for controlling influenza virus infection .

Example answer:
{"entities": [{"text": "monoclonal antibodies", "type": "Chemical"}, {"text": "influenza virus", "type": "Virus"}, {"text": "infection", "type": "BiologicFunction"}]}

Example input:
Sentence: It is probable that the frequency of replacement by a pandemic virus is higher than a seasonal virus because of the high initial susceptibility and high basic reproductive number of the pandemic virus .

Example answer:
{"entities": [{"text": "pandemic virus", "type": "Virus"}, {"text": "seasonal virus", "type": "Virus"}, {"text": "reproductive", "type": "BiologicFunction"}]}

Example input:
Sentence: The findings of this study on replacement mechanisms could lead to a better understanding of virus transmission dynamics and may possibly be helpful in establishing an effective strategy to mitigate the impact of seasonal and pandemic influenza .

Example answer:
{"entities": [{"text": "virus transmission", "type": "BiologicFunction"}, {"text": "seasonal", "type": "BiologicFunction"}, {"text": "pandemic influenza", "type": "BiologicFunction"}]}

Example input:
Sentence: Although new antigenic variants of the influenza A virus replace formerly circulating seasonal and pandemic viruses , replacement mechanisms remain poorly understood .

Example answer:
{"entities": [{"text": "antigenic variants", "type": "BiologicFunction"}, {"text": "influenza A virus", "type": "Virus"}, {"text": "seasonal", "type": "Virus"}, {"text": "pandemic viruses", "type": "Virus"}]}

Input:
Sentence: Mechanisms of replacement of circulating viruses by seasonal and pandemic influenza A viruses Seasonal influenza causes annual epidemics by the accumulation of antigenic changes .

## Item MedMentions:test:1122
Example input:
Sentence: Low literate patients experienced greater improvement in self - efficacy than more literate patients ( t = 2 . 54 , p = 0 .

Example answer:
{"entities": [{"text": "literate", "type": "Finding"}, {"text": "experienced", "type": "BiologicFunction"}, {"text": "improvement", "type": "Finding"}, {"text": "self - efficacy", "type": "BiologicFunction"}]}

Example input:
Sentence: Stroke risk increased with lower education ( OR = 1 . 35 , 95 % CI = 1 .

Example answer:
{"entities": [{"text": "Stroke risk", "type": "IntellectualProduct"}]}

Example input:
Sentence: Structured Instruction With Modified Storybooks to Teach Morphosyntax and Vocabulary to Preschoolers Who are Deaf / Hard of Hearing Children who are deaf / hard of hearing ( D / HH ) are at risk for diminished morphosyntactical and vocabulary development .

Example answer:
{"entities": [{"text": "Structured", "type": "SpatialConcept"}, {"text": "Instruction", "type": "IntellectualProduct"}, {"text": "Vocabulary", "type": "IntellectualProduct"}, {"text": "vocabulary", "type": "IntellectualProduct"}]}

Example input:
Sentence: In contrast , activation in the right precentral gyrus showed a significantly stronger correlation with HLE in FHD + compared to FHD - children , suggesting emerging compensatory networks in genetically at - risk children .

Example answer:
{"entities": [{"text": "right precentral gyrus", "type": "AnatomicalStructure"}, {"text": "HLE", "type": "SpatialConcept"}, {"text": "FHD +", "type": "Finding"}, {"text": "FHD -", "type": "Finding"}]}

Example input:
Sentence: Understanding environmental contributions is important given that we do not understand why some genetically at - risk children do not develop dyslexia .

Example answer:
{"entities": [{"text": "Understanding", "type": "BiologicFunction"}, {"text": "environmental", "type": "SpatialConcept"}, {"text": "understand", "type": "BiologicFunction"}, {"text": "dyslexia", "type": "BiologicFunction"}]}

Example input:
Sentence: Group differences revealed stronger correlation of HLE with brain activation in the left inferior / middle frontal and right fusiform gyri in FHD - compared to FHD + children , suggesting greater impact of HLE on manipulation of phonological codes and recruitment of orthographic representations in typically developing children .

Example answer:
{"entities": [{"text": "HLE", "type": "SpatialConcept"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "left inferior", "type": "AnatomicalStructure"}, {"text": "middle frontal", "type": "AnatomicalStructure"}, {"text": "right fusiform gyri", "type": "AnatomicalStructure"}, {"text": "FHD -", "type": "Finding"}, {"text": "FHD +", "type": "Finding"}, {"text": "phonological codes", "type": "IntellectualProduct"}, {"text": "orthographic representations", "type": "IntellectualProduct"}]}

Example input:
Sentence: While an understanding of genetic contributions is emerging , the ways the environment affects brain functioning in children with developmental dyslexia are poorly understood .

Example answer:
{"entities": [{"text": "understanding", "type": "BiologicFunction"}, {"text": "environment", "type": "SpatialConcept"}, {"text": "affects", "type": "BiologicFunction"}, {"text": "developmental dyslexia", "type": "BiologicFunction"}, {"text": "understood", "type": "BiologicFunction"}]}

Example input:
Sentence: Examining the relationship between home literacy environment and neural correlates of phonological processing in beginning readers with and without a familial risk for dyslexia : an fMRI study Developmental dyslexia is a language - based learning disability characterized by persistent difficulty in learning to read .

Example answer:
{"entities": [{"text": "between", "type": "SpatialConcept"}, {"text": "environment", "type": "SpatialConcept"}, {"text": "dyslexia", "type": "BiologicFunction"}, {"text": "fMRI study", "type": "HealthCareActivity"}, {"text": "Developmental dyslexia", "type": "BiologicFunction"}, {"text": "learning disability", "type": "BiologicFunction"}]}

Example input:
Sentence: We further controlled for socioeconomic status to isolate the neurobiological mechanism by which HLE affects reading development .

Example answer:
{"entities": [{"text": "HLE", "type": "SpatialConcept"}, {"text": "affects", "type": "BiologicFunction"}]}

Example input:
Sentence: A relationship between the home literacy environment ( HLE ) and neural correlates of reading has been identified in typically developing children , yet it remains unclear whether similar effects are observable in children with a genetic predisposition for dyslexia .

Example answer:
{"entities": [{"text": "between", "type": "SpatialConcept"}, {"text": "home literacy environment", "type": "SpatialConcept"}, {"text": "HLE", "type": "SpatialConcept"}, {"text": "dyslexia", "type": "BiologicFunction"}]}

Input:
Sentence: Overall , our results suggest that genetic predisposition for dyslexia alters contributions of HLE to early reading skills before formal reading instruction , which has important implications for educational practice and intervention models .

## Item MedMentions:test:1287
Example input:
Sentence: The structural confirmation of all the synthesized compounds was obtained by EI - MS , IR and 1H - NMR spectral data .

Example answer:
{"entities": [{"text": "structural", "type": "SpatialConcept"}, {"text": "confirmation", "type": "Finding"}, {"text": "EI - MS", "type": "HealthCareActivity"}, {"text": "IR", "type": "HealthCareActivity"}, {"text": "1H - NMR", "type": "HealthCareActivity"}]}

Example input:
Sentence: The deduced peptides revealed that they contain the putative signal peptides and encode for mature peptides , which contain sequence architecture similar to a 6 . 5 - kDa proline - rich AMP of the shore crab , Carcinus maenas which showed similarity with the bactenecin7 .

Example answer:
{"entities": [{"text": "peptides", "type": "Chemical"}, {"text": "signal peptides", "type": "SpatialConcept"}, {"text": "proline - rich", "type": "Chemical"}, {"text": "AMP", "type": "Chemical"}, {"text": "shore crab", "type": "Eukaryote"}, {"text": "Carcinus maenas", "type": "Eukaryote"}, {"text": "bactenecin7", "type": "Chemical"}]}

Example input:
Sentence: Here we describe two strategies to prepare combinatorial libraries suitable for MS analysis to accelerate the discovery of cyclic peptide structures .

Example answer:
{"entities": [{"text": "combinatorial libraries", "type": "Chemical"}, {"text": "MS analysis", "type": "HealthCareActivity"}, {"text": "discovery", "type": "ResearchActivity"}, {"text": "cyclic peptide", "type": "Chemical"}, {"text": "structures", "type": "SpatialConcept"}]}

Example input:
Sentence: The results of ELISA indicated specific reactions of the isolated scFvs against the IGF - IR peptide , and analyses of PCR product and sequencing confirmed the presence of full length VH and Vκ inserts .

Example answer:
{"entities": [{"text": "ELISA", "type": "HealthCareActivity"}, {"text": "scFvs", "type": "Chemical"}, {"text": "IGF - IR peptide", "type": "Chemical"}, {"text": "analyses of PCR product", "type": "HealthCareActivity"}, {"text": "presence", "type": "Finding"}, {"text": "VH and Vκ inserts", "type": "Chemical"}]}

Example input:
Sentence: The FT - IR results imply that Ag - NPs were successfully synthesized and capped with bio - compounds present in P .

Example answer:
{"entities": [{"text": "FT - IR", "type": "ResearchActivity"}, {"text": "results", "type": "Finding"}, {"text": "P .", "type": "Chemical"}]}

Example input:
Sentence: The iTRAQ - labeled peptides were fractionated by high - accuracy liquid chromatography - mass spectrometry ( LC - MS ) .

Example answer:
{"entities": [{"text": "iTRAQ - labeled peptides", "type": "Chemical"}, {"text": "high - accuracy liquid chromatography - mass spectrometry", "type": "HealthCareActivity"}, {"text": "LC - MS", "type": "HealthCareActivity"}]}

Example input:
Sentence: Peptides modified with a 22 kDa PEG ( PEG22 ) remained intact in blood plasma and on incubation with liver homogenates for more than 96 h .

Example answer:
{"entities": [{"text": "Peptides", "type": "Chemical"}, {"text": "22 kDa PEG", "type": "Chemical"}, {"text": "PEG22", "type": "Chemical"}, {"text": "blood plasma", "type": "Chemical"}, {"text": "incubation", "type": "HealthCareActivity"}, {"text": "liver homogenates", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The current study demonstrates the feasibility of the multigram - scale synthesis of a highly pure complex glycopeptide , and it opens new avenues for the use of synthetic glycopeptides as drugs in humans .

Example answer:
{"entities": [{"text": "complex", "type": "Chemical"}, {"text": "glycopeptide", "type": "Chemical"}, {"text": "glycopeptides", "type": "Chemical"}, {"text": "drugs", "type": "Chemical"}, {"text": "humans", "type": "Eukaryote"}]}

Example input:
Sentence: MS data were used to generate spectral libraries of non - modified peptides and an open modification search was performed to identify potential adduct mass shifts and possible modification sites .

Example answer:
{"entities": [{"text": "MS", "type": "HealthCareActivity"}, {"text": "libraries", "type": "Chemical"}, {"text": "peptides", "type": "Chemical"}]}

Example input:
Sentence: A series of mutations was synthetically engineered into β - hairpin peptides to establish structure - activity relationships .

Example answer:
{"entities": [{"text": "mutations", "type": "BiologicFunction"}, {"text": "engineered", "type": "ResearchActivity"}, {"text": "β - hairpin", "type": "Chemical"}, {"text": "peptides", "type": "Chemical"}]}

Input:
Sentence: These findings were confirmed by subsequent database searches and experiments with synthetic peptides .

## Item MedMentions:test:1079
Example input:
Sentence: Notably , the environmental isolate , CD105HS27 , does not share a consensus motif for ( m4 ) C methylation , but has one additional spacer when compared to the clinical isolate M120 .

Example answer:
{"entities": [{"text": "environmental", "type": "SpatialConcept"}, {"text": "isolate", "type": "Chemical"}, {"text": "CD105HS27", "type": "AnatomicalStructure"}, {"text": "( m4 ) C methylation", "type": "BiologicFunction"}, {"text": "M120", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Here , we proposed the use of folate - conjugated DNA - loaded cationic MBs ( FCMBs ) .

Example answer:
{"entities": [{"text": "folate", "type": "Chemical"}, {"text": "cationic MBs", "type": "MedicalDevice"}, {"text": "FCMBs", "type": "MedicalDevice"}]}

Example input:
Sentence: It showed a greater ability to open Caco - 2 tight junctions and to enhance the permeability of Caco - 2 substrates with respect to micelles based on higher palmitoyl substitution , conceivably due to the lower modification of the chitosan chains .

Example answer:
{"entities": [{"text": "Caco - 2", "type": "AnatomicalStructure"}, {"text": "tight junctions", "type": "SpatialConcept"}, {"text": "micelles", "type": "Chemical"}, {"text": "palmitoyl", "type": "Chemical"}, {"text": "chitosan chains", "type": "Chemical"}]}

Example input:
Sentence: Interestingly , when the temperature is turned back to 25 ° C , the compacted DNA molecules can fully recover to the stretched conformation .

Example answer:
{"entities": [{"text": "compacted", "type": "Finding"}, {"text": "DNA", "type": "Chemical"}]}

Example input:
Sentence: Docetaxel ( DTX ) could be entrapped in MPEG - PCLA micelles with high loading capacity and encapsulation efficiency . And all lyophilized DTX -loaded MPEG - PCLA micelles except MPEG - PCL micelles were readily re - dissolved in normal saline at 25 ° C .

Example answer:
{"entities": [{"text": "Docetaxel", "type": "Chemical"}, {"text": "DTX", "type": "Chemical"}, {"text": "MPEG - PCLA", "type": "Chemical"}, {"text": "micelles", "type": "Chemical"}, {"text": "MPEG - PCL", "type": "Chemical"}, {"text": "normal saline", "type": "Chemical"}]}

Example input:
Sentence: This indicates a stronger binding of the protonated C14DMAOH ( + ) to DNA .

Example answer:
{"entities": [{"text": "binding", "type": "BiologicFunction"}, {"text": "C14DMAOH ( + )", "type": "Chemical"}, {"text": "DNA", "type": "Chemical"}]}

Example input:
Sentence: The micelle system of CS - P68 and CS - P127 formed at drug to polymer ratios of 1 : 4 and 1 : 2 , respectively , was found to be the most suitable monodispersed system with a nanosize - range diameter .

Example answer:
{"entities": [{"text": "micelle system", "type": "Chemical"}, {"text": "CS - P68", "type": "Chemical"}, {"text": "CS - P127", "type": "Chemical"}, {"text": "drug", "type": "Chemical"}, {"text": "polymer", "type": "Chemical"}]}

Example input:
Sentence: DNA was compacted and then insoluble DNA / CnDMAOH ( + ) complexes were formed .

Example answer:
{"entities": [{"text": "DNA", "type": "Chemical"}, {"text": "compacted", "type": "Finding"}, {"text": "CnDMAOH ( + )", "type": "Chemical"}, {"text": "complexes", "type": "Chemical"}]}

Example input:
Sentence: The negative charges of DNA molecules can easily be neutralized by positive charges of cationic CnDMAOH ( + ) ( n = 12 and 14 ) micelles .

Example answer:
{"entities": [{"text": "DNA", "type": "Chemical"}, {"text": "cationic CnDMAOH ( + )", "type": "Chemical"}, {"text": "micelles", "type": "Chemical"}]}

Example input:
Sentence: For the DNA / C10DMAO system , however , no DNA compaction was observed even in Tris - HCl buffer solution with a much lower pH and a much higher C10DMAO concentration .

Example answer:
{"entities": [{"text": "DNA", "type": "Chemical"}, {"text": "C10DMAO", "type": "Chemical"}, {"text": "compaction", "type": "Finding"}]}

Input:
Sentence: Because of the much higher critical micelle concentration ( cmc ) of the shorter chain length C10DMAOH ( + ) , cationic C10DMAOH ( + ) micelles cannot form under the studied condition to compact DNA .

## Item MedMentions:test:1365
Example input:
Sentence: The high - risk group showed decreased fractional anisotropy ( FA ) , a measure of water diffusion directionality , and increased radial diffusivity in the anterior region of corpus callosum compared to the low - risk group .

Example answer:
{"entities": [{"text": "high - risk group", "type": "PopulationGroup"}, {"text": "fractional anisotropy", "type": "HealthCareActivity"}, {"text": "FA", "type": "HealthCareActivity"}, {"text": "water", "type": "Chemical"}, {"text": "anterior region of corpus callosum", "type": "AnatomicalStructure"}, {"text": "low - risk group", "type": "PopulationGroup"}]}

Example input:
Sentence: LMCA with T - shaped distal BA was found to have significantly longer LMCA , larger LAD ostial area , larger LCX ostial area and higher DSR of distal BA compared to patients with Y - shaped distal BA .

Example answer:
{"entities": [{"text": "LMCA", "type": "AnatomicalStructure"}, {"text": "T - shaped distal", "type": "SpatialConcept"}, {"text": "LAD ostial", "type": "AnatomicalStructure"}, {"text": "area", "type": "SpatialConcept"}, {"text": "LCX", "type": "AnatomicalStructure"}, {"text": "ostial", "type": "SpatialConcept"}, {"text": "distal", "type": "SpatialConcept"}, {"text": "Y - shaped distal", "type": "SpatialConcept"}]}

Example input:
Sentence: There was also a significant increase in arch width and greater and lesser segments length .

Example answer:
{"entities": [{"text": "arch", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Patients with overlapping lobar ICH had larger ICH volumes than isolated lobar ICH ( overlapping , 48 . 9 mL [ 22 . 6 - 78 . 5 mL ] versus 15 .

Example answer:
{"entities": [{"text": "ICH", "type": "Finding"}]}

Example input:
Sentence: Bucco - lingual or bucco - palatal expansion were the most common presentation ( six [ 46 .

Example answer:
{"entities": [{"text": "Bucco - lingual", "type": "AnatomicalStructure"}, {"text": "bucco - palatal", "type": "AnatomicalStructure"}, {"text": "expansion", "type": "SpatialConcept"}]}

Example input:
Sentence: There was a statistically significant difference in the total augmented volume between the groups in the radiographic analysis ( 158 . 22 ± 39 . 31 mm ( 3 ) and 107 . 09 ± 39 . 69 mm ( 3 ) , respectively , p = 0 . 040 ) .

Example answer:
{"entities": [{"text": "volume", "type": "SpatialConcept"}, {"text": "radiographic analysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: EAT volume was signiﬁcantly increased in patients with ISR compared with those without ISR ( 154 . 5 ± 74 .

Example answer:
{"entities": [{"text": "EAT", "type": "AnatomicalStructure"}, {"text": "ISR", "type": "BiologicFunction"}]}

Example input:
Sentence: The study has quantitatively shown that the modified NAM therapy improved nasal asymmetry by columellar lengthening and effectively molded the maxillary alveolar arch .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "modified NAM therapy", "type": "HealthCareActivity"}, {"text": "improved", "type": "Finding"}, {"text": "nasal asymmetry", "type": "Finding"}, {"text": "columellar", "type": "SpatialConcept"}, {"text": "lengthening", "type": "HealthCareActivity"}, {"text": "maxillary alveolar arch", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Direct extra and intra oral anthropometric measurements were done using a digital vernier caliper before and after NAM therapy .

Example answer:
{"entities": [{"text": "digital vernier caliper", "type": "MedicalDevice"}, {"text": "NAM therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: The intraoral measurements demonstrated a statistically significant reduction in anterior alveolar cleft width .

Example answer:
{"entities": [{"text": "anterior alveolar cleft", "type": "SpatialConcept"}]}

Input:
Sentence: The extra oral measurements revealed a statistically significant increase in bi - alar width , columellar length and width .

## Item MedMentions:test:1283
Example input:
Sentence: To address this issue , the pathophysiology of chronic lung inflammation induced by Pseudomonas aeruginosa in CCSP - deficient mice was determined .

Example answer:
{"entities": [{"text": "chronic lung inflammation", "type": "BiologicFunction"}, {"text": "Pseudomonas aeruginosa", "type": "Bacterium"}, {"text": "CCSP", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Chronic Pseudomonas aeruginosa infection - induced chronic bronchitis and emphysematous changes in CCSP - deficient mice The club cell secretory protein ( CCSP ) is a regulator of lung inflammation following acute respiratory infection or lung injury .

Example answer:
{"entities": [{"text": "Chronic Pseudomonas aeruginosa infection", "type": "BiologicFunction"}, {"text": "chronic bronchitis", "type": "BiologicFunction"}, {"text": "CCSP", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "club cell secretory protein", "type": "Chemical"}, {"text": "lung inflammation", "type": "BiologicFunction"}, {"text": "acute respiratory infection", "type": "BiologicFunction"}, {"text": "lung injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Mice were subcutaneously injected with nPbHsp60 or rPbHsp60 emulsified in complete 's Freund Adjuvant ( CFA ) at three weeks after intravenous injection of P .

Example answer:
{"entities": [{"text": "Mice", "type": "Eukaryote"}, {"text": "nPbHsp60", "type": "Chemical"}, {"text": "rPbHsp60", "type": "Chemical"}, {"text": "emulsified", "type": "BiologicFunction"}, {"text": "complete 's Freund Adjuvant", "type": "Chemical"}, {"text": "CFA", "type": "Chemical"}, {"text": "P .", "type": "Eukaryote"}]}

Example input:
Sentence: aeruginosa inflammation resulted in chronic bronchitis and emphysematous changes in the CCSP - deficient mice .

Example answer:
{"entities": [{"text": "aeruginosa", "type": "Bacterium"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "chronic bronchitis", "type": "BiologicFunction"}, {"text": "CCSP", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: gingivalis heat - shock protein 60 ( HSP60 ) induced the dysfunction of human umbilical vein endothelial cells ( HUVECs ) in vitro .

Example answer:
{"entities": [{"text": "gingivalis", "type": "Bacterium"}, {"text": "heat - shock protein 60", "type": "Chemical"}, {"text": "HSP60", "type": "Chemical"}, {"text": "human umbilical vein endothelial cells", "type": "AnatomicalStructure"}, {"text": "HUVECs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: brasiliensis ( nPbHsp60 ) or its recombinant counterpart ( rPbHsp60 ) affected the course of experimental PCM .

Example answer:
{"entities": [{"text": "brasiliensis", "type": "Eukaryote"}, {"text": "nPbHsp60", "type": "Chemical"}, {"text": "recombinant counterpart", "type": "Chemical"}, {"text": "rPbHsp60", "type": "Chemical"}, {"text": "PCM", "type": "BiologicFunction"}]}

Example input:
Sentence: Heat - shock protein 60 of Porphyromonas gingivalis may induce dysfunction of human umbilical endothelial cells via regulation of endothelial - nitric oxide synthase and vascular endothelial - cadherin Accumulating evidence has established that periodontitis was an independent risk factor for coronary heart disease ( CAD ) .

Example answer:
{"entities": [{"text": "Heat - shock protein 60", "type": "Chemical"}, {"text": "Porphyromonas gingivalis", "type": "Bacterium"}, {"text": "human umbilical endothelial cells", "type": "AnatomicalStructure"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "endothelial - nitric oxide synthase", "type": "Chemical"}, {"text": "vascular endothelial - cadherin", "type": "Chemical"}, {"text": "periodontitis", "type": "BiologicFunction"}, {"text": "risk factor", "type": "Finding"}, {"text": "coronary heart disease", "type": "BiologicFunction"}, {"text": "CAD", "type": "BiologicFunction"}]}

Example input:
Sentence: Further , rPbHsp60 treatment ( i ) decreased the known protective effect of CFA against PCM and ( ii ) increased the concentrations of IL - 17 , TNF - α , IL - 12 , IFN - γ , IL - 4 , IL - 10 , and TGF - β in the lungs .

Example answer:
{"entities": [{"text": "rPbHsp60", "type": "Chemical"}, {"text": "CFA", "type": "Chemical"}, {"text": "PCM", "type": "BiologicFunction"}, {"text": "IL - 17", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "IL - 12", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "IL - 4", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "TGF - β", "type": "Chemical"}, {"text": "lungs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Therefore , we propose that PbHsp60 contributes to the fungal pathogenesis .

Example answer:
{"entities": [{"text": "PbHsp60", "type": "Chemical"}, {"text": "pathogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Thirty days after the nPbHsp60 or rPbHsp60 administration , mice showed remarkably increased fungal load , tissue inflammation , and granulomas in the lungs , liver , and spleen compared with control mice .

Example answer:
{"entities": [{"text": "nPbHsp60", "type": "Chemical"}, {"text": "rPbHsp60", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "granulomas in the lungs", "type": "Finding"}, {"text": "liver", "type": "BiologicFunction"}, {"text": "spleen", "type": "BiologicFunction"}]}

Input:
Sentence: Together , our results indicated that PbHsp60 induced a harmful immune response , exacerbated inflammation , and promoted fungal dissemination .

## Item MedMentions:test:1300
Example input:
Sentence: The role of miR - 4638 - 5p in prostate cancer androgen - independent growth has been demonstrated both in vitro and in vivo .

Example answer:
{"entities": [{"text": "miR - 4638 - 5p", "type": "AnatomicalStructure"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "androgen - independent growth", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: MiR - 424 - 5p participates in esophageal squamous cell carcinoma invasion and metastasis via SMAD7 pathway mediated EMT ESCC is a life - threatening disease due to invasion and metastasis in the early stage .

Example answer:
{"entities": [{"text": "MiR - 424 - 5p", "type": "AnatomicalStructure"}, {"text": "esophageal squamous cell carcinoma", "type": "BiologicFunction"}, {"text": "invasion", "type": "BiologicFunction"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "SMAD7", "type": "AnatomicalStructure"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "EMT", "type": "BiologicFunction"}, {"text": "ESCC", "type": "BiologicFunction"}, {"text": "life - threatening", "type": "Finding"}, {"text": "disease", "type": "BiologicFunction"}]}

Example input:
Sentence: CSCs were then isolated from the tumors and their microRNA ( miRNA ) expression was analyzed by semi - quantitative polymerase chain reaction .

Example answer:
{"entities": [{"text": "CSCs", "type": "AnatomicalStructure"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "microRNA", "type": "Chemical"}, {"text": "miRNA", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "semi - quantitative polymerase chain reaction", "type": "HealthCareActivity"}]}

Example input:
Sentence: The comparison with published findings in adults demonstrated a unique miRNA signature in young patients with aggressive disease .

Example answer:
{"entities": [{"text": "published", "type": "IntellectualProduct"}, {"text": "findings", "type": "Finding"}, {"text": "miRNA", "type": "Chemical"}]}

Example input:
Sentence: MicroRNA - 18a - 5p functions as an oncogene by directly targeting IRF2 in lung cancer Lung cancer is the major form of cancer resulting in cancer - related mortality around the world .

Example answer:
{"entities": [{"text": "MicroRNA - 18a - 5p", "type": "Chemical"}, {"text": "oncogene", "type": "AnatomicalStructure"}, {"text": "targeting", "type": "BiologicFunction"}, {"text": "IRF2", "type": "Chemical"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "Lung cancer", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "cancer - related", "type": "Finding"}, {"text": "world", "type": "PopulationGroup"}]}

Example input:
Sentence: Twenty - two microRNAs were significantly differently expressed in patients with pancreatic cancer when compared to healthy controls and chronic pancreatitis patients ; 17 miRNAs were upregulated ( miR - 21 - 5p , - 23a - 3p , - 31 - 5p , - 34c - 5p , - 93 - 3p , - 135b - 3p , - 155 - 5p , - 186 - 5p , - 196b - 5p , - 203 , - 205 - 5p , - 210 , - 222 - 3p , - 451 , - 492 , - 614 , and miR - 622 ) and 5 were downregulated ( miR - 122 - 5p , - 130b - 3p , - 216b , - 217 , and miR - 375 ) .

Example answer:
{"entities": [{"text": "microRNAs", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "pancreatic cancer", "type": "BiologicFunction"}, {"text": "chronic pancreatitis", "type": "BiologicFunction"}, {"text": "miRNAs", "type": "Chemical"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "miR - 21 - 5p", "type": "AnatomicalStructure"}, {"text": "23a - 3p", "type": "AnatomicalStructure"}, {"text": "31 - 5p", "type": "AnatomicalStructure"}, {"text": "34c - 5p", "type": "AnatomicalStructure"}, {"text": "93 - 3p", "type": "AnatomicalStructure"}, {"text": "135b - 3p", "type": "AnatomicalStructure"}, {"text": "155 - 5p", "type": "AnatomicalStructure"}, {"text": "186 - 5p", "type": "AnatomicalStructure"}, {"text": "196b - 5p ,", "type": "AnatomicalStructure"}, {"text": "203", "type": "AnatomicalStructure"}, {"text": "205 - 5p", "type": "Chemical"}, {"text": "210", "type": "AnatomicalStructure"}, {"text": "222 - 3p", "type": "AnatomicalStructure"}, {"text": "451", "type": "AnatomicalStructure"}, {"text": "492", "type": "AnatomicalStructure"}, {"text": "614", "type": "AnatomicalStructure"}, {"text": "miR - 622", "type": "AnatomicalStructure"}, {"text": "downregulated", "type": "BiologicFunction"}, {"text": "miR - 122 - 5p", "type": "AnatomicalStructure"}, {"text": "130b - 3p", "type": "AnatomicalStructure"}, {"text": "216b", "type": "AnatomicalStructure"}, {"text": "217", "type": "AnatomicalStructure"}, {"text": "miR - 375", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In this study , miR - 18a - 5p significantly upregulated in non - small cell lung cancer ( NSCLC ) tissues and NSCLC cell lines , suggesting an oncogenic function in lung cancer .

Example answer:
{"entities": [{"text": "miR - 18a - 5p", "type": "Chemical"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "non - small cell lung cancer", "type": "BiologicFunction"}, {"text": "NSCLC", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "oncogenic", "type": "AnatomicalStructure"}, {"text": "function", "type": "BiologicFunction"}, {"text": "lung cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Additionally , miR - 18a - 5p can promote carcinogenesis by directly targeting interferon regulatory factor 2 ( IRF2 ) .

Example answer:
{"entities": [{"text": "miR - 18a - 5p", "type": "Chemical"}, {"text": "carcinogenesis", "type": "BiologicFunction"}, {"text": "targeting", "type": "BiologicFunction"}, {"text": "interferon regulatory factor 2", "type": "Chemical"}, {"text": "IRF2", "type": "Chemical"}]}

Example input:
Sentence: MiR - 4638 - 5p inhibits castration resistance of prostate cancer through repressing Kidins220 expression and PI3K / AKT pathway activity MicroRNAs ( miRNAs ) are short , conserved segments of non - coding RNA which play a significant role in prostate cancer development and progression .

Example answer:
{"entities": [{"text": "MiR - 4638 - 5p", "type": "AnatomicalStructure"}, {"text": "castration resistance of prostate cancer", "type": "BiologicFunction"}, {"text": "Kidins220", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "MicroRNAs", "type": "Chemical"}, {"text": "miRNAs", "type": "Chemical"}, {"text": "conserved segments", "type": "SpatialConcept"}, {"text": "non - coding RNA", "type": "Chemical"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "progression", "type": "BiologicFunction"}]}

Example input:
Sentence: miRNA expression profiles were evaluated in formalin - fixed , paraffin - embedded samples of tumor and normal mucosa from 12 patients aged < 30 years old with squamous cell carcinoma of the tongue .

Example answer:
{"entities": [{"text": "miRNA", "type": "Chemical"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "formalin - fixed , paraffin - embedded samples", "type": "AnatomicalStructure"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "mucosa", "type": "AnatomicalStructure"}, {"text": "squamous cell carcinoma of the tongue", "type": "BiologicFunction"}]}

Input:
Sentence: The present study investigated miRNA expression in carcinoma of the oral tongue in young patients .

## Item MedMentions:test:1492
Example input:
Sentence: Appropriate lesion preparation , high - pressure postdilatation , and the use of intravascular imaging are recommended to obtain the best possible final result .

Example answer:
{"entities": [{"text": "lesion", "type": "Finding"}, {"text": "postdilatation", "type": "HealthCareActivity"}, {"text": "intravascular imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: All MGD cases were diagnosed using a preoperative localization study .

Example answer:
{"entities": [{"text": "MGD", "type": "BiologicFunction"}, {"text": "diagnosed", "type": "Finding"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Knowledge of hereditary PHPT and improved preoperative localization studies , such as high - resolution ultrasonography , contributed to the decision to perform FP rather than CP in all cases of unilateral results of the localizing study .

Example answer:
{"entities": [{"text": "PHPT", "type": "BiologicFunction"}, {"text": "improved", "type": "Finding"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "high - resolution ultrasonography", "type": "HealthCareActivity"}, {"text": "FP", "type": "HealthCareActivity"}, {"text": "CP", "type": "HealthCareActivity"}, {"text": "unilateral", "type": "SpatialConcept"}, {"text": "localizing study", "type": "ResearchActivity"}]}

Example input:
Sentence: A diffuse reticular localisation was detected for the complex in the nuclear / perinuclear region of cells , by either optical or X - ray fluorescence imaging techniques .

Example answer:
{"entities": [{"text": "complex", "type": "Chemical"}, {"text": "nuclear", "type": "AnatomicalStructure"}, {"text": "perinuclear region", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "optical", "type": "HealthCareActivity"}, {"text": "X - ray fluorescence imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: This predictive localization may depend on eye movement control in the frontal eye fields ( FEF ) and the intraparietal sulcus ( IPS ) and on motion analysis in the medial temporal area ( MT ) .

Example answer:
{"entities": [{"text": "eye movement", "type": "BiologicFunction"}, {"text": "frontal eye fields", "type": "AnatomicalStructure"}, {"text": "FEF", "type": "AnatomicalStructure"}, {"text": "intraparietal sulcus", "type": "SpatialConcept"}, {"text": "IPS", "type": "SpatialConcept"}, {"text": "medial temporal area", "type": "AnatomicalStructure"}, {"text": "MT", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Their treatment ranges from resection of malignant lesions , to resection and / or surveillance in the case of premalignant lesions , to simple observation in the case of benign or indolent lesions .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "resection", "type": "HealthCareActivity"}, {"text": "lesions", "type": "Finding"}, {"text": "surveillance", "type": "HealthCareActivity"}, {"text": "premalignant lesions", "type": "BiologicFunction"}, {"text": "observation", "type": "ResearchActivity"}]}

Example input:
Sentence: Larger areas of block were used to simulate ablation lesions .

Example answer:
{"entities": [{"text": "areas", "type": "SpatialConcept"}, {"text": "block", "type": "BiologicFunction"}, {"text": "ablation lesions", "type": "Finding"}]}

Example input:
Sentence: On the one hand , this technique allows a better and direct visualization of vascular and solid organ lesions .

Example answer:
{"entities": [{"text": "vascular", "type": "BiologicFunction"}, {"text": "solid organ", "type": "AnatomicalStructure"}, {"text": "lesions", "type": "Finding"}]}

Example input:
Sentence: When localisation was defined as the sum of late gadolinium enhancement in the left ventricular basal anterior and basal anteroseptal area s , or the right ventricular area , it was associated with ventricular tachyarrhythmias ( p < 0 . 001 ) .

Example answer:
{"entities": [{"text": "late gadolinium enhancement", "type": "Chemical"}, {"text": "left ventricular basal anterior", "type": "AnatomicalStructure"}, {"text": "basal anteroseptal area", "type": "AnatomicalStructure"}, {"text": "right ventricular area", "type": "AnatomicalStructure"}, {"text": "ventricular tachyarrhythmias", "type": "BiologicFunction"}]}

Example input:
Sentence: The main reason is the increased awareness of these lesions and the extensive use of cross - sectional imaging , an always improving technique ( 1 ) .

Example answer:
{"entities": [{"text": "awareness", "type": "BiologicFunction"}, {"text": "lesions", "type": "Finding"}]}

Input:
Sentence: Localizing these lesions requires specific techniques .

## Item MedMentions:test:841
Example input:
Sentence: New international networks and far more academic R & D activities should be established in order to find the first therapy specifically for acute pancreatitis .

Example answer:
{"entities": [{"text": "academic", "type": "Organization"}, {"text": "R & D activities", "type": "ResearchActivity"}, {"text": "acute pancreatitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Monascus - fermented MS and AK can perform blood lipid regulation via the suppression of LDL - C assembly and stimulation of apo A1 expression in liver .

Example answer:
{"entities": [{"text": "Monascus", "type": "Eukaryote"}, {"text": "fermented", "type": "BiologicFunction"}, {"text": "MS", "type": "Chemical"}, {"text": "AK", "type": "Chemical"}, {"text": "blood lipid regulation", "type": "BiologicFunction"}, {"text": "suppression", "type": "BiologicFunction"}, {"text": "LDL - C", "type": "Chemical"}, {"text": "stimulation", "type": "HealthCareActivity"}, {"text": "apo A1", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "liver", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Ankaflavin and Monascin Induce Apoptosis in Activated Hepatic Stellate Cells through Suppression of the Akt / NF - κB / p38 Signaling Pathway The increased proliferation of activated hepatic stellate cells ( HSCs ) is associated with hepatic fibrosis and excessive extracellular matrix ( ECM ) - protein production .

Example answer:
{"entities": [{"text": "Ankaflavin", "type": "Chemical"}, {"text": "Monascin", "type": "Chemical"}, {"text": "Apoptosis", "type": "BiologicFunction"}, {"text": "Hepatic Stellate Cells", "type": "AnatomicalStructure"}, {"text": "Akt", "type": "Chemical"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "p38", "type": "Chemical"}, {"text": "Signaling Pathway", "type": "BiologicFunction"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "hepatic stellate cells", "type": "AnatomicalStructure"}, {"text": "HSCs", "type": "AnatomicalStructure"}, {"text": "hepatic fibrosis", "type": "BiologicFunction"}, {"text": "extracellular matrix", "type": "AnatomicalStructure"}, {"text": "ECM", "type": "AnatomicalStructure"}, {"text": "protein", "type": "Chemical"}]}

Example input:
Sentence: Plasma from Brown Norway rats given intravenous injection of saline , compound 48 / 80 ( 2 . 5 mL / kg ) or ovalbumin ( 20 mL / kg ) in 20 s for the first time was used to study the effect mechanism of anaphylactoid reactions through metabolomics ( UPLC - qTOF - MS / MS ) .

Example answer:
{"entities": [{"text": "Plasma", "type": "BodySubstance"}, {"text": "Brown Norway rats", "type": "Eukaryote"}, {"text": "compound 48 / 80", "type": "Chemical"}, {"text": "ovalbumin", "type": "Chemical"}, {"text": "study", "type": "ResearchActivity"}, {"text": "anaphylactoid reactions", "type": "BiologicFunction"}, {"text": "metabolomics", "type": "Chemical"}, {"text": "UPLC - qTOF - MS / MS", "type": "ResearchActivity"}]}

Example input:
Sentence: HMGB1 inhibition by ethyl pyruvate or blockade by neutralizing antibodies significantly decreased the phosphorylation of STAT3 , p38 and IκBα , the production of IL - 1β and TNF - α , and the islet injury in wild - type islets after exposure to H / R and significantly improved early islet graft failure .

Example answer:
{"entities": [{"text": "HMGB1", "type": "Chemical"}, {"text": "ethyl pyruvate", "type": "Chemical"}, {"text": "antibodies", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "STAT3", "type": "Chemical"}, {"text": "p38", "type": "Chemical"}, {"text": "IκBα", "type": "Chemical"}, {"text": "production", "type": "BiologicFunction"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "islet", "type": "AnatomicalStructure"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "islets", "type": "AnatomicalStructure"}, {"text": "H", "type": "BiologicFunction"}, {"text": "R", "type": "HealthCareActivity"}, {"text": "graft failure", "type": "BiologicFunction"}]}

Example input:
Sentence: Neutrophil gelatinase - associated lipocalin in a triphasic rat model of adenine - induced kidney injury The aim of this study is to investigate whether NGAL , given its advantages over traditional biomarkers , can be used to describe the dynamic characteristics of the renal tubulointerstitial insult caused by adenine .

Example answer:
{"entities": [{"text": "Neutrophil gelatinase - associated lipocalin", "type": "Chemical"}, {"text": "rat model", "type": "Eukaryote"}, {"text": "adenine", "type": "Chemical"}, {"text": "kidney injury", "type": "InjuryOrPoisoning"}, {"text": "NGAL", "type": "Chemical"}, {"text": "biomarkers", "type": "ClinicalAttribute"}, {"text": "renal tubulointerstitial insult", "type": "BiologicFunction"}]}

Example input:
Sentence: Panchakarma promoted statistically significant changes in plasma levels of phosphatidylcholines , sphingomyelins and others in just 6 days .

Example answer:
{"entities": [{"text": "Panchakarma", "type": "HealthCareActivity"}, {"text": "plasma", "type": "BodySubstance"}, {"text": "phosphatidylcholines", "type": "Chemical"}, {"text": "sphingomyelins", "type": "Chemical"}]}

Example input:
Sentence: We examined the inhibitory effects of the Monascus purpureus -fermented metabolites , ankaflavin and monascin ( 15 and 30 μM ) , on the Akt / nuclear factor ( NF ) - κB and p38 mitogen - activated protein kinase ( MAPK ) signaling pathways in HSC - T6 ( activated hepatic stellate cell line ) .

Example answer:
{"entities": [{"text": "Monascus purpureus", "type": "Eukaryote"}, {"text": "metabolites", "type": "Chemical"}, {"text": "ankaflavin", "type": "Chemical"}, {"text": "monascin", "type": "Chemical"}, {"text": "Akt", "type": "Chemical"}, {"text": "nuclear factor ( NF ) - κB", "type": "Chemical"}, {"text": "p38 mitogen - activated protein kinase", "type": "Chemical"}, {"text": "MAPK", "type": "Chemical"}, {"text": "signaling pathways", "type": "BiologicFunction"}, {"text": "HSC - T6", "type": "AnatomicalStructure"}, {"text": "activated hepatic stellate cell line", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The discovery of potent and selective kynurenine 3 - monooxygenase inhibitors for the treatment of acute pancreatitis A series of potent , competitive and highly selective kynurenine monooxygenase inhibitors have been discovered via a substrate -based approach for the treatment of acute pancreatitis .

Example answer:
{"entities": [{"text": "kynurenine 3 - monooxygenase", "type": "Chemical"}, {"text": "inhibitors", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "acute pancreatitis", "type": "BiologicFunction"}, {"text": "kynurenine monooxygenase", "type": "Chemical"}, {"text": "approach", "type": "SpatialConcept"}]}

Example input:
Sentence: CONCLUSIONS Leukotriene receptor antagonists used in the late phases of pancreatitis might not result in any benefit ; however , when they are given in the early phases or prophylactically , they may decrease pancreatic damage .

Example answer:
{"entities": [{"text": "Leukotriene receptor antagonists", "type": "Chemical"}, {"text": "pancreatitis", "type": "BiologicFunction"}, {"text": "pancreatic", "type": "AnatomicalStructure"}]}

Input:
Sentence: Effects of Montelukast in an Experimental Model of Acute Pancreatitis BACKGROUND We evaluated the hematological , biochemical , and histopathological effects of Montelukast on pancreatic damage in an experimental acute pancreatitis model created by cerulein in rats before and after the induction of pancreatitis .

## Item MedMentions:test:1076
Example input:
Sentence: Squamous metaplasia was detected in each group , but the difference was not significant .

Example answer:
{"entities": [{"text": "Squamous metaplasia", "type": "BiologicFunction"}, {"text": "detected", "type": "Finding"}, {"text": "not significant", "type": "Finding"}]}

Example input:
Sentence: Analysis of skin biopsies before treatment showed a significant increase in Ki - 67 - positive cells in the suprabasal layer and a dysregulated expression of various skin barrier genes , such as claudin 1 , loricrin , filaggrin and cytokeratin 10 , which were normalized after treatment .

Example answer:
{"entities": [{"text": "Analysis", "type": "ResearchActivity"}, {"text": "skin biopsies", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "Ki - 67", "type": "AnatomicalStructure"}, {"text": "positive", "type": "Finding"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "suprabasal layer", "type": "AnatomicalStructure"}, {"text": "dysregulated expression", "type": "BiologicFunction"}, {"text": "skin barrier", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "claudin 1", "type": "AnatomicalStructure"}, {"text": "loricrin", "type": "AnatomicalStructure"}, {"text": "filaggrin", "type": "AnatomicalStructure"}, {"text": "cytokeratin 10", "type": "AnatomicalStructure"}, {"text": "normalized", "type": "ResearchActivity"}]}

Example input:
Sentence: Analyses of our next generation sequencing results and data from five independent published studies consisting of 191 normal , 10 low - grade squamous intraepithelial lesions , 21 high - grade squamous intraepithelial lesions , and 335 malignant tissues identified a panel of nine genes ( ARHGAP6 , DAPK1 , HAND2 , NKX2 - 2 , NNAT , PCDH10 , PROX1 , PITX2 , and RAB6C ) which could effectively discriminate among the various groups with sensitivity and specificity of 80 % - 100 % ( p < 0 .

Example answer:
{"entities": [{"text": "Analyses", "type": "ResearchActivity"}, {"text": "next generation sequencing", "type": "ResearchActivity"}, {"text": "published studies", "type": "IntellectualProduct"}, {"text": "normal", "type": "Finding"}, {"text": "low - grade squamous intraepithelial lesions", "type": "BiologicFunction"}, {"text": "high - grade squamous intraepithelial lesions", "type": "BiologicFunction"}, {"text": "malignant", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "ARHGAP6", "type": "AnatomicalStructure"}, {"text": "DAPK1", "type": "AnatomicalStructure"}, {"text": "HAND2", "type": "AnatomicalStructure"}, {"text": "NKX2 - 2", "type": "AnatomicalStructure"}, {"text": "NNAT", "type": "AnatomicalStructure"}, {"text": "PCDH10", "type": "AnatomicalStructure"}, {"text": "PROX1", "type": "AnatomicalStructure"}, {"text": "PITX2", "type": "AnatomicalStructure"}, {"text": "RAB6C", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Also , the probability of toxicity for organs and tissues was classified as moderate and high for liver and kidney , and moderate and low for skin and eye irritation , respectively .

Example answer:
{"entities": [{"text": "organs", "type": "AnatomicalStructure"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "kidney", "type": "AnatomicalStructure"}, {"text": "skin", "type": "Finding"}, {"text": "eye irritation", "type": "Finding"}]}

Example input:
Sentence: The tissue histology showed a chronic inflammatory cell infiltrate associated with the MTA .

Example answer:
{"entities": [{"text": "tissue", "type": "AnatomicalStructure"}, {"text": "histology", "type": "HealthCareActivity"}, {"text": "inflammatory cell infiltrate", "type": "BodySubstance"}, {"text": "MTA", "type": "Chemical"}]}

Example input:
Sentence: These effects were verified by histological evaluation of the levels of infiltration of inflammatory cells and collagen , destructions of alveoli and bronchioles , and hyperplasia of goblet cells in lung tissues .

Example answer:
{"entities": [{"text": "evaluation", "type": "HealthCareActivity"}, {"text": "infiltration", "type": "BiologicFunction"}, {"text": "inflammatory cells", "type": "AnatomicalStructure"}, {"text": "collagen", "type": "Chemical"}, {"text": "destructions", "type": "HealthCareActivity"}, {"text": "alveoli", "type": "AnatomicalStructure"}, {"text": "bronchioles", "type": "AnatomicalStructure"}, {"text": "hyperplasia", "type": "BiologicFunction"}, {"text": "goblet cells", "type": "AnatomicalStructure"}, {"text": "lung tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The method requires a pathologist to differentiate healthy tissue from tumor tissue , and basic tissue culture skills .

Example answer:
{"entities": [{"text": "method", "type": "HealthCareActivity"}, {"text": "pathologist", "type": "ProfessionalOrOccupationalGroup"}, {"text": "healthy tissue", "type": "AnatomicalStructure"}, {"text": "tumor tissue", "type": "AnatomicalStructure"}, {"text": "basic tissue culture", "type": "HealthCareActivity"}]}

Example input:
Sentence: The lungs were dissected and blind histopathological evaluation was performed .

Example answer:
{"entities": [{"text": "lungs", "type": "AnatomicalStructure"}, {"text": "evaluation", "type": "HealthCareActivity"}]}

Example input:
Sentence: In conclusion , this study in the hamster demonstrated high homogeneity of infection in liver and spleen and advocates the use of molecular detection methods for assessment of low ( post - treatment ) tissue burdens .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "hamster", "type": "Eukaryote"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "spleen", "type": "AnatomicalStructure"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "methods", "type": "IntellectualProduct"}, {"text": "assessment", "type": "HealthCareActivity"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Tumor tissue showed moderate inhibition of PI3 K and mitogen - activated protein kinase ( MAPK ) pathways .

Example answer:
{"entities": [{"text": "Tumor tissue", "type": "AnatomicalStructure"}, {"text": "inhibition", "type": "BiologicFunction"}, {"text": "mitogen - activated protein kinase ( MAPK ) pathways", "type": "BiologicFunction"}]}

Input:
Sentence: An expert pathologist blinded to the experimental group evaluated the tissues for the following : epithelial distribution , inflammation , hyperplasia , and metaplasia .

## Item MedMentions:test:1270
Example input:
Sentence: The complication rate possibly related to the traction table was 5 % ( 5 patients ) : three anterior dislocations , one periprosthetic femoral fracture , and one intraoperative perforation caused by femoral rasping .

Example answer:
{"entities": [{"text": "complication", "type": "BiologicFunction"}, {"text": "traction table", "type": "MedicalDevice"}, {"text": "anterior dislocations", "type": "InjuryOrPoisoning"}, {"text": "periprosthetic", "type": "InjuryOrPoisoning"}, {"text": "femoral fracture", "type": "InjuryOrPoisoning"}, {"text": "intraoperative perforation", "type": "HealthCareActivity"}, {"text": "femoral rasping", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The first experience of consecutive surgeries by a single surgeon using the direct anterior approach with a traction table is described with a two - year follow - up period .

Example answer:
{"entities": [{"text": "consecutive surgeries", "type": "HealthCareActivity"}, {"text": "single surgeon", "type": "ProfessionalOrOccupationalGroup"}, {"text": "direct anterior approach", "type": "SpatialConcept"}, {"text": "traction table", "type": "MedicalDevice"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: The method of ICC was performed to assess the reproducibility of the two angles , and the absolute value of difference in pre - operative and post - operative radiographs was used to evaluate the uniformity of the two angles .

Example answer:
{"entities": [{"text": "angles", "type": "SpatialConcept"}, {"text": "radiographs", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , there was a great difference between the Pauwels angle in pre - operative and post - operative radiographs ( P = 0 . 037 ) , the absolute difference was 10 . 66±6 .

Example answer:
{"entities": [{"text": "radiographs", "type": "HealthCareActivity"}]}

Example input:
Sentence: Direct anterior approach for total hip arthroplasty with a novel mobile traction table -a prospective cohort study The purpose of this prospective cohort study was to clarify the safety and efficacy of total hip arthroplasty via the direct anterior approach in the supine position with a novel mobile traction table .

Example answer:
{"entities": [{"text": "Direct anterior approach", "type": "SpatialConcept"}, {"text": "total hip arthroplasty", "type": "HealthCareActivity"}, {"text": "mobile traction table", "type": "MedicalDevice"}, {"text": "prospective cohort study", "type": "ResearchActivity"}, {"text": "direct anterior approach", "type": "SpatialConcept"}, {"text": "supine position", "type": "SpatialConcept"}]}

Example input:
Sentence: The deformity is needed to balance both tractional and rotational forces and useful technique to evaluate curve flexibility before the operation .

Example answer:
{"entities": [{"text": "deformity", "type": "AnatomicalStructure"}, {"text": "tractional", "type": "HealthCareActivity"}, {"text": "operation", "type": "HealthCareActivity"}]}

Example input:
Sentence: The direct anterior approach with a novel mobile traction table showed a positive learning curve for surgical time , rate of allogeneic blood transfusion , and cup alignment in the safe zone .

Example answer:
{"entities": [{"text": "direct anterior approach", "type": "SpatialConcept"}, {"text": "mobile traction table", "type": "MedicalDevice"}, {"text": "positive learning curve", "type": "Finding"}, {"text": "allogeneic blood transfusion", "type": "HealthCareActivity"}]}

Example input:
Sentence: Longitudinal traction and lateral pushing angles were more correlated with correction ratios .

Example answer:
{"entities": [{"text": "Longitudinal", "type": "SpatialConcept"}, {"text": "traction", "type": "HealthCareActivity"}, {"text": "lateral pushing angles", "type": "Finding"}]}

Example input:
Sentence: The Cobb angle of the lumbar curve was reduced to 20 . 3 ° after surgery .

Example answer:
{"entities": [{"text": "Cobb angle", "type": "Finding"}, {"text": "lumbar curve", "type": "SpatialConcept"}, {"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: There was a significant difference between longitudinal traction minor Cobb angle , longitudinal traction lateral pushing minor Cobb angle and postoperative minor Cobb angles .

Example answer:
{"entities": [{"text": "longitudinal", "type": "SpatialConcept"}, {"text": "traction", "type": "HealthCareActivity"}, {"text": "Cobb angle", "type": "Finding"}, {"text": "lateral pushing minor Cobb angle", "type": "Finding"}, {"text": "postoperative minor Cobb angles", "type": "Finding"}]}

Input:
Sentence: The significant prescriptive angle of major Cobb angles between postoperative angles were longitudinal traction and lateral pushing Cobb angles .

## Item MedMentions:test:1435
Example input:
Sentence: A total of 216 patients with musculoskeletal disorders were recruited in this study .

Example answer:
{"entities": [{"text": "musculoskeletal disorders", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Snowmobile and dirtbike accidents were associated with a higher rate of fractures ( 63 % , 64 % ) than the ATV group ( 50 % ) ( P = 0 . 0008 ) .

Example answer:
{"entities": [{"text": "fractures", "type": "InjuryOrPoisoning"}, {"text": "ATV group", "type": "PopulationGroup"}]}

Example input:
Sentence: Muscle imbalance is one of the main causes of sport injuries .

Example answer:
{"entities": [{"text": "injuries", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Rushing was identified as the cause of nearly 50 % of injuries , and repetitive work as the cause of an additional 20 % of injuries .

Example answer:
{"entities": [{"text": "injuries", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: In five patients nature of injury was known in other two patients exact nature of injury was not known .

Example answer:
{"entities": [{"text": "nature of injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Two - thirds of the children had experienced at least 1 unintentional injury in the previous 12 months .

Example answer:
{"entities": [{"text": "unintentional injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Snowmobile injuries had the highest rate of spinal ( 23 % ) and lower extremity fractures ( 53 % ) ( P = 0 . 0004 ) .

Example answer:
{"entities": [{"text": "spinal", "type": "InjuryOrPoisoning"}, {"text": "lower extremity fractures", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: The majority of injuries were soft tissue injuries , but others included fractures , tympanic membrane perforation , burns and neck contusions .

Example answer:
{"entities": [{"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "soft tissue injuries", "type": "InjuryOrPoisoning"}, {"text": "fractures", "type": "InjuryOrPoisoning"}, {"text": "tympanic membrane perforation", "type": "InjuryOrPoisoning"}, {"text": "burns", "type": "InjuryOrPoisoning"}, {"text": "neck contusions", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Body regions commonly injured were lower extremity ( 35 . 1 % ) , upper extremity ( 33 . 4 % ) , and head ( 26 .

Example answer:
{"entities": [{"text": "Body regions", "type": "SpatialConcept"}, {"text": "lower extremity", "type": "AnatomicalStructure"}, {"text": "upper extremity", "type": "AnatomicalStructure"}, {"text": "head", "type": "SpatialConcept"}]}

Example input:
Sentence: The most common mechanisms of injury were road traffic injuries ( 36 . 8 % ) , falls ( 26 . 4 % ) , and being struck / hit by a person or object ( 20 .

Example answer:
{"entities": [{"text": "traffic injuries", "type": "InjuryOrPoisoning"}, {"text": "falls", "type": "InjuryOrPoisoning"}, {"text": "person", "type": "PopulationGroup"}]}

Input:
Sentence: Three quarters of injuries were musculoskeletal in nature .

## Item MedMentions:test:1333
Example input:
Sentence: Nanocurcumin -mediated antiapoptotic effects might have benefited residents and sojourners at high altitude in preventing hypoxic cardiac damage .

Example answer:
{"entities": [{"text": "Nanocurcumin", "type": "Chemical"}, {"text": "antiapoptotic effects", "type": "Finding"}, {"text": "hypoxic", "type": "BiologicFunction"}, {"text": "cardiac", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Combination treatment of curcumin and IFN - β / RA had a stronger effect than that of the IFN - β / RA group .

Example answer:
{"entities": [{"text": "Combination treatment", "type": "HealthCareActivity"}, {"text": "curcumin", "type": "Chemical"}, {"text": "IFN - β", "type": "Chemical"}, {"text": "RA", "type": "Chemical"}]}

Example input:
Sentence: The geminally dimethylated and catechol -type curcumin analog ( compound 3 ) was identified as a promising lead molecule in terms of its increased stability and cytoprotective activity against the tert - butyl hydroperoxide ( t - BHP ) - induced death of HepG2 cells .

Example answer:
{"entities": [{"text": "catechol", "type": "Chemical"}, {"text": "curcumin", "type": "Chemical"}, {"text": "analog", "type": "Chemical"}, {"text": "compound 3", "type": "Chemical"}, {"text": "lead molecule", "type": "Chemical"}, {"text": "stability", "type": "BiologicFunction"}, {"text": "cytoprotective", "type": "BiologicFunction"}, {"text": "tert - butyl hydroperoxide", "type": "Chemical"}, {"text": "t - BHP", "type": "Chemical"}, {"text": "death", "type": "BiologicFunction"}, {"text": "HepG2 cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Curcumin synergistically increases the effects of IFN - β / RA on breast cancer cells .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}, {"text": "IFN - β", "type": "Chemical"}, {"text": "RA", "type": "Chemical"}, {"text": "breast cancer cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 0 % inhibition , while the antifungal activity of the compound was the highest against Candida glabrata with 80 .

Example answer:
{"entities": [{"text": "inhibition", "type": "BiologicFunction"}, {"text": "antifungal activity", "type": "Finding"}, {"text": "compound", "type": "Chemical"}, {"text": "Candida glabrata", "type": "Eukaryote"}]}

Example input:
Sentence: Curcumin is a natural antioxidant and antihypertrophic agent , but it has poor biostability .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}, {"text": "antioxidant", "type": "Chemical"}, {"text": "antihypertrophic agent", "type": "Chemical"}]}

Example input:
Sentence: Development of a Curcumin Bioadhesive Monolithic Tablet for Treatment of Vaginal Candidiasis The present investigation was designed to formulate a natural tablet for the treatment of vaginal candidiasis in order to eliminate side effects that are caused by existing antifungal drugs .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}, {"text": "Bioadhesive Monolithic Tablet", "type": "Chemical"}, {"text": "Treatment", "type": "HealthCareActivity"}, {"text": "Vaginal Candidiasis", "type": "BiologicFunction"}, {"text": "investigation", "type": "HealthCareActivity"}, {"text": "formulate", "type": "Chemical"}, {"text": "natural tablet", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "vaginal candidiasis", "type": "BiologicFunction"}, {"text": "side effects", "type": "BiologicFunction"}, {"text": "antifungal drugs", "type": "Chemical"}]}

Example input:
Sentence: Curcumin tablets were characterized by studies of friability , hardness , hydration , DSC , mucoadhesion , In - vitro release and antifungal activity .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}, {"text": "tablets", "type": "Chemical"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "hydration", "type": "Finding"}, {"text": "DSC", "type": "HealthCareActivity"}, {"text": "antifungal", "type": "Chemical"}]}

Example input:
Sentence: Hence , the study indicates the possible and effective use of curcumin bioadhesive monolithic vaginal tablet for vaginal candidiasis as a promising natural antifungal treatment .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "possible", "type": "Finding"}, {"text": "curcumin", "type": "Chemical"}, {"text": "bioadhesive monolithic vaginal tablet", "type": "Chemical"}, {"text": "vaginal candidiasis", "type": "BiologicFunction"}, {"text": "antifungal treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Curcumin has promising antifungal activity in comparison with the existing azole antifungal drugs .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}, {"text": "antifungal", "type": "Chemical"}, {"text": "azole antifungal drugs", "type": "Chemical"}]}

Input:
Sentence: The antifungal activity of the Curcumin tablet has demonstrated a significant effect against Candida albicans .

## Item MedMentions:test:1120
Example input:
Sentence: Here , the authors show that in layer 2 / 3 ( L2 / 3 ) of the somatosensory cortex ( S1 ) , acute RA induces increases in spontaneous but not action - potential evoked transmission , and that this requires retinoic acid receptor ( RARα ) both in presynaptic PV -positive interneurons and postsynaptic pyramidal ( PN ) neurons .

Example answer:
{"entities": [{"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "layer 2 / 3", "type": "AnatomicalStructure"}, {"text": "L2 / 3", "type": "AnatomicalStructure"}, {"text": "somatosensory cortex", "type": "AnatomicalStructure"}, {"text": "S1", "type": "AnatomicalStructure"}, {"text": "RA", "type": "Chemical"}, {"text": "action - potential", "type": "BiologicFunction"}, {"text": "transmission", "type": "BiologicFunction"}, {"text": "retinoic acid receptor", "type": "Chemical"}, {"text": "RARα", "type": "Chemical"}, {"text": "presynaptic", "type": "AnatomicalStructure"}, {"text": "PV", "type": "Chemical"}, {"text": "interneurons", "type": "AnatomicalStructure"}, {"text": "pyramidal ( PN ) neurons", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We show that RA190 reduces the expression of Stat3 and the levels of key immunosuppressive enzymes and cytokines arginase , iNOS , and IL - 10 in MDSCs , while boosting expression of the immunostimulatory cytokine IL - 12 .

Example answer:
{"entities": [{"text": "RA190", "type": "Chemical"}, {"text": "Stat3", "type": "Chemical"}, {"text": "immunosuppressive", "type": "BiologicFunction"}, {"text": "enzymes", "type": "Chemical"}, {"text": "cytokines", "type": "Chemical"}, {"text": "arginase", "type": "Chemical"}, {"text": "iNOS", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "MDSCs", "type": "AnatomicalStructure"}, {"text": "immunostimulatory", "type": "HealthCareActivity"}, {"text": "cytokine", "type": "Chemical"}, {"text": "IL - 12", "type": "Chemical"}]}

Example input:
Sentence: Chromatin immunoprecipitation ( ChIP ) showed approximately 3 - fold enrichment of RANKL - specific DNA in anti - SOX5 immunoprecipitate in IL - 6 treated MH7A cells as compared to untreated cells .

Example answer:
{"entities": [{"text": "Chromatin immunoprecipitation", "type": "HealthCareActivity"}, {"text": "ChIP", "type": "HealthCareActivity"}, {"text": "RANKL - specific DNA", "type": "Chemical"}, {"text": "anti - SOX5 immunoprecipitate", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "MH7A cells", "type": "AnatomicalStructure"}, {"text": "untreated cells", "type": "Finding"}]}

Example input:
Sentence: Differential regulation of spontaneous and evoked inhibitory synaptic transmission in somatosensory cortex by retinoic acid Retinoic acid ( RA ) , a developmental morphogen , has emerged in recent studies as a novel synaptic signaling molecule that acts in mature hippocampal neurons to modulate excitatory and inhibitory synaptic transmission in the context of homeostatic synaptic plasticity .

Example answer:
{"entities": [{"text": "Differential regulation", "type": "BiologicFunction"}, {"text": "inhibitory synaptic transmission", "type": "BiologicFunction"}, {"text": "somatosensory cortex", "type": "AnatomicalStructure"}, {"text": "retinoic acid", "type": "Chemical"}, {"text": "Retinoic acid", "type": "Chemical"}, {"text": "RA", "type": "Chemical"}, {"text": "morphogen", "type": "Chemical"}, {"text": "synaptic", "type": "BiologicFunction"}, {"text": "signaling molecule", "type": "Chemical"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "excitatory", "type": "BiologicFunction"}, {"text": "homeostatic", "type": "BiologicFunction"}, {"text": "synaptic plasticity", "type": "BiologicFunction"}]}

Example input:
Sentence: The increased insulin resistance seen in RA is closely linked to the systemic inflammation induced by certain proinflammatory cytokines such as tumor necrosis factor α ( TNFα ) and interleukin - 6 .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "proinflammatory cytokines", "type": "Chemical"}, {"text": "tumor necrosis factor α", "type": "Chemical"}, {"text": "TNFα", "type": "Chemical"}, {"text": "interleukin - 6", "type": "Chemical"}]}

Example input:
Sentence: We previously reported association between younger age at onset of RA and a RANKL promoter SNP that conferred an elevated promoter activity via binding to a transcription factor SOX5 .

Example answer:
{"entities": [{"text": "RA", "type": "BiologicFunction"}, {"text": "RANKL", "type": "Chemical"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "transcription factor SOX5", "type": "Chemical"}]}

Example input:
Sentence: Our data indicated SOX5 levels were higher in synovium and synovial fluid from RA compared to osteoarthritis patients .

Example answer:
{"entities": [{"text": "data", "type": "IntellectualProduct"}, {"text": "indicated", "type": "Finding"}, {"text": "SOX5", "type": "Chemical"}, {"text": "synovium", "type": "AnatomicalStructure"}, {"text": "synovial fluid", "type": "BodySubstance"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "osteoarthritis", "type": "BiologicFunction"}]}

Example input:
Sentence: Modulation of IL - 6 induced RANKL expression in arthritic synovium by a transcription factor SOX5 Receptor activator of nuclear factor κB ligand ( RANKL ) is critically involved in bone erosion of rheumatoid arthritis ( RA ) .

Example answer:
{"entities": [{"text": "Modulation", "type": "SpatialConcept"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "RANKL", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "arthritic", "type": "BiologicFunction"}, {"text": "synovium", "type": "AnatomicalStructure"}, {"text": "transcription factor SOX5", "type": "Chemical"}, {"text": "Receptor activator of nuclear factor κB ligand", "type": "Chemical"}, {"text": "bone erosion", "type": "BiologicFunction"}, {"text": "rheumatoid arthritis", "type": "BiologicFunction"}, {"text": "RA", "type": "BiologicFunction"}]}

Example input:
Sentence: Here we study the regulation of SOX5 levels in relation to RANKL expression in RA synovial fibroblasts ( SF ) and the development of bone erosion in the collagen - induced arthritis ( CIA ) mouse .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "SOX5", "type": "Chemical"}, {"text": "RANKL", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "synovial", "type": "AnatomicalStructure"}, {"text": "fibroblasts", "type": "AnatomicalStructure"}, {"text": "SF", "type": "AnatomicalStructure"}, {"text": "bone erosion", "type": "BiologicFunction"}, {"text": "collagen - induced arthritis", "type": "BiologicFunction"}, {"text": "CIA", "type": "BiologicFunction"}, {"text": "mouse", "type": "Eukaryote"}]}

Example input:
Sentence: Pro - inflammatory cytokines upregulated SOX5 and RANKL expression in both primary RA SF and the rheumatoid synovial fibroblast cell line , MH7A .

Example answer:
{"entities": [{"text": "cytokines", "type": "Chemical"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "SOX5", "type": "Chemical"}, {"text": "RANKL", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "SF", "type": "AnatomicalStructure"}, {"text": "MH7A", "type": "AnatomicalStructure"}]}

Input:
Sentence: These findings suggest SOX5 is an important regulator of IL - 6 - induced RANKL expression in RA SF .

## Item MedMentions:test:1360
Example input:
Sentence: Patients were followed up for six months with scheduled monthly remote monitoring transmissions in addition to routine in - office checks .

Example answer:
{"entities": [{"text": "followed up", "type": "HealthCareActivity"}, {"text": "remote", "type": "SpatialConcept"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "in - office checks", "type": "HealthCareActivity"}]}

Example input:
Sentence: A follow - up substudy was performed in 40 patients ( mean follow - up interval , 144 days ± 35 [ standard deviation ] ) ; of these 40 patients , 18 underwent anti - inflammatory treatment for systemic symptoms .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "substudy", "type": "ResearchActivity"}, {"text": "anti - inflammatory treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: All participants were followed through the initial study protocol of 24 months and were approached to enter an extension phase , with continuing follow - up visits to 60 months .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "study protocol", "type": "IntellectualProduct"}, {"text": "follow - up visits", "type": "HealthCareActivity"}]}

Example input:
Sentence: Forty - one patients had a minimum of 6 - month of follow - up ( mean , 24 months ; range , 6 - 68 months ) .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients were then followed for three years .

Example answer:
{"entities": []}

Example input:
Sentence: Adherence to controller therapy was assessed over 365 days by using the proportion of days covered ( PDC ) , starting with the first claim for controller therapy in 2012 .

Example answer:
{"entities": []}

Example input:
Sentence: The treatment process consisted of 10 weeks of full intervention and 4 weeks of follow - up meetings that marked the end of intervention .

Example answer:
{"entities": [{"text": "treatment process", "type": "HealthCareActivity"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: A total of 224 ( 93 % ) patients who completed 6 months ' adherence assessment were included in the model .

Example answer:
{"entities": []}

Example input:
Sentence: Patients were followed up for 13 months to assess outcomes .

Example answer:
{"entities": []}

Example input:
Sentence: Patients were followed for 24 months .

Example answer:
{"entities": []}

Input:
Sentence: All patients received a full course of medications and completed research visits at 14 - days ( adherence ) , 30 days and 90 days with by an outreach worker .

## Item MedMentions:test:963
Example input:
Sentence: Knockdown of Nrf2 by small interfering RNA ( siRNA ) abrogated all the effects of EGCG , confirming that the EGCG protection against oxalate -induced EMT was mediated via Nrf2 .

Example answer:
{"entities": [{"text": "Knockdown", "type": "ResearchActivity"}, {"text": "Nrf2", "type": "AnatomicalStructure"}, {"text": "small interfering RNA", "type": "Chemical"}, {"text": "siRNA", "type": "Chemical"}, {"text": "EGCG", "type": "Chemical"}, {"text": "oxalate", "type": "Chemical"}, {"text": "EMT", "type": "BiologicFunction"}, {"text": "Nrf2", "type": "Chemical"}]}

Example input:
Sentence: Taken together , our data indicate that oxalate turned on EMT of renal tubular cells that could be prevented by EGCG via Nrf2 pathway .

Example answer:
{"entities": [{"text": "oxalate", "type": "Chemical"}, {"text": "EMT", "type": "BiologicFunction"}, {"text": "renal", "type": "AnatomicalStructure"}, {"text": "EGCG", "type": "Chemical"}, {"text": "Nrf2", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}]}

Example input:
Sentence: The local / paracrine renin - angiotensin system ( RAS ) plays a major role in inflammatory processes in peripheral tissues and brain .

Example answer:
{"entities": [{"text": "renin - angiotensin system", "type": "BodySystem"}, {"text": "RAS", "type": "BodySystem"}, {"text": "inflammatory processes", "type": "BiologicFunction"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Compared to CONV - R mice , angiotensin II ( AngII ; 1 mg / kg per day for 7 days ) infused GF mice showed reduced reactive oxygen species formation in the vasculature , attenuated vascular mRNA expression of monocyte chemoattractant protein 1 ( MCP - 1 ) , inducible nitric oxide synthase ( iNOS ) and NADPH oxidase subunit Nox2 , as well as a reduced upregulation of retinoic - acid receptor - related orphan receptor gamma t ( Rorγt ) , the signature transcription factor for interleukin ( IL ) - 17 synthesis .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}, {"text": "angiotensin II", "type": "Chemical"}, {"text": "AngII", "type": "Chemical"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "vasculature", "type": "AnatomicalStructure"}, {"text": "vascular", "type": "AnatomicalStructure"}, {"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "monocyte chemoattractant protein 1", "type": "AnatomicalStructure"}, {"text": "MCP - 1", "type": "Chemical"}, {"text": "inducible nitric oxide synthase", "type": "AnatomicalStructure"}, {"text": "iNOS", "type": "AnatomicalStructure"}, {"text": "NADPH oxidase subunit Nox2", "type": "AnatomicalStructure"}, {"text": "upregulation", "type": "BiologicFunction"}, {"text": "retinoic - acid receptor - related orphan receptor gamma t", "type": "Chemical"}, {"text": "Rorγt", "type": "Chemical"}, {"text": "transcription factor", "type": "Chemical"}, {"text": "interleukin ( IL ) - 17", "type": "Chemical"}]}

Example input:
Sentence: The ratios of oxi - AGT and red - AGT were ∼4 : 1 ( rat ) and 16 : 1 ( mouse ) .

Example answer:
{"entities": [{"text": "oxi - AGT", "type": "Chemical"}, {"text": "red - AGT", "type": "Chemical"}, {"text": "rat", "type": "Eukaryote"}, {"text": "mouse", "type": "Eukaryote"}]}

Example input:
Sentence: iAGT levels were 53 % of tAGT in rat plasma but only 22 % in mouse plasma , probably reflecting the greater plasma renin activity in mice .

Example answer:
{"entities": [{"text": "iAGT", "type": "Chemical"}, {"text": "tAGT", "type": "Chemical"}, {"text": "rat", "type": "Eukaryote"}, {"text": "plasma", "type": "BodySubstance"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "renin", "type": "Chemical"}, {"text": "activity", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Furthermore , ruscogenin decreased reactive oxygen species ( ROS ) generation and inhibited the mitogen - activated protein kinase ( MAPK ) pathway in OGD / R -induced bEnd .

Example answer:
{"entities": [{"text": "ruscogenin", "type": "Chemical"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "ROS", "type": "Chemical"}, {"text": "mitogen - activated protein kinase ( MAPK ) pathway", "type": "BiologicFunction"}, {"text": "OGD", "type": "BiologicFunction"}, {"text": "bEnd .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Thus , quantification of the intact AGT ( iAGT ) concentrations is important to evaluate the actual renin substrate available .

Example answer:
{"entities": [{"text": "AGT", "type": "Chemical"}, {"text": "iAGT", "type": "Chemical"}, {"text": "renin substrate", "type": "Chemical"}]}

Example input:
Sentence: Accordingly , we determined iAGT , oxi - AGT , and red - AGT levels in plasma from rats and mice .

Example answer:
{"entities": [{"text": "iAGT", "type": "Chemical"}, {"text": "oxi - AGT", "type": "Chemical"}, {"text": "red - AGT", "type": "Chemical"}, {"text": "plasma", "type": "BodySubstance"}, {"text": "rats", "type": "Eukaryote"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Quantification of intact plasma AGT consisting of oxidized and reduced conformations using a modified ELISA The pleiotropic actions of the renin - angiotensin system ( RAS ) depend on the availability of angiotensinogen ( AGT ) which generates angiotensin I ( ANG I ) when cleaved by renin .

Example answer:
{"entities": [{"text": "plasma", "type": "BodySubstance"}, {"text": "AGT", "type": "Chemical"}, {"text": "reduced conformations", "type": "SpatialConcept"}, {"text": "ELISA", "type": "HealthCareActivity"}, {"text": "renin - angiotensin system", "type": "BodySystem"}, {"text": "RAS", "type": "BodySystem"}, {"text": "angiotensinogen", "type": "Chemical"}, {"text": "angiotensin I", "type": "Chemical"}, {"text": "ANG I", "type": "Chemical"}, {"text": "cleaved", "type": "SpatialConcept"}, {"text": "renin", "type": "Chemical"}]}

Input:
Sentence: The iAGT conformation exists as oxidized AGT ( oxi - AGT ) and reduced AGT ( red - AGT ) in a disulfide bond , and oxi - AGT has a higher affinity for renin , which may exacerbate RAS - associated diseases .

## Item MedMentions:test:1259
Example input:
Sentence: Furthermore , we found that miR - 4638 - 5p , through regulating Kidins220 and the downstream activity of VEGF and PI3K / AKT pathway , influences prostate cancer progression via angiogenesis .

Example answer:
{"entities": [{"text": "miR - 4638 - 5p", "type": "AnatomicalStructure"}, {"text": "Kidins220", "type": "AnatomicalStructure"}, {"text": "downstream", "type": "SpatialConcept"}, {"text": "VEGF", "type": "Chemical"}, {"text": "prostate cancer progression", "type": "BiologicFunction"}, {"text": "angiogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: elegans oocyte , we provide novel evidence that the kinesin - 13 KLP - 7 promotes destabilization of the whole cellular microtubule network .

Example answer:
{"entities": [{"text": "elegans", "type": "Eukaryote"}, {"text": "oocyte", "type": "AnatomicalStructure"}, {"text": "kinesin - 13 KLP - 7", "type": "Chemical"}, {"text": "destabilization", "type": "BiologicFunction"}, {"text": "cellular", "type": "AnatomicalStructure"}, {"text": "microtubule network", "type": "AnatomicalStructure"}]}

Example input:
Sentence: MicroRNA - 18a - 5p functions as an oncogene by directly targeting IRF2 in lung cancer Lung cancer is the major form of cancer resulting in cancer - related mortality around the world .

Example answer:
{"entities": [{"text": "MicroRNA - 18a - 5p", "type": "Chemical"}, {"text": "oncogene", "type": "AnatomicalStructure"}, {"text": "targeting", "type": "BiologicFunction"}, {"text": "IRF2", "type": "Chemical"}, {"text": "lung cancer", "type": "BiologicFunction"}, {"text": "Lung cancer", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "cancer - related", "type": "Finding"}, {"text": "world", "type": "PopulationGroup"}]}

Example input:
Sentence: The metastasis suppressor CD82 / KAI1 inhibits fibronectin adhesion - induced epithelial - to - mesenchymal transition in prostate cancer cells by repressing the associated integrin signaling The transmembrane protein CD82 / KAI1 suppresses the metastatic potential of various cancer cell types .

Example answer:
{"entities": [{"text": "metastasis suppressor", "type": "AnatomicalStructure"}, {"text": "CD82 / KAI1", "type": "Chemical"}, {"text": "fibronectin", "type": "Chemical"}, {"text": "adhesion", "type": "BiologicFunction"}, {"text": "epithelial - to - mesenchymal transition", "type": "BiologicFunction"}, {"text": "prostate", "type": "AnatomicalStructure"}, {"text": "cancer cells", "type": "AnatomicalStructure"}, {"text": "integrin signaling", "type": "BiologicFunction"}, {"text": "transmembrane protein", "type": "Chemical"}, {"text": "cancer cell", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Here we report that AMS and MS188 target the CYP703A2 gene , which is involved in sporopollenin biosynthesis .

Example answer:
{"entities": [{"text": "AMS", "type": "Chemical"}, {"text": "MS188", "type": "Chemical"}, {"text": "CYP703A2 gene", "type": "AnatomicalStructure"}, {"text": "sporopollenin biosynthesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Keratin 13 Is Enriched in Prostate Tubule - Initiating Cells and May Identify Primary Prostate Tumors that Metastasize to the Bone Benign human prostate tubule - initiating cells ( TIC ) and aggressive prostate cancer display common traits , including tolerance of low androgen levels , resistance to apoptosis , and microenvironment interactions that drive epithelial budding and outgrowth .

Example answer:
{"entities": [{"text": "Keratin 13", "type": "Chemical"}, {"text": "Prostate", "type": "AnatomicalStructure"}, {"text": "Tubule - Initiating Cells", "type": "AnatomicalStructure"}, {"text": "Primary Prostate Tumors", "type": "BiologicFunction"}, {"text": "Metastasize", "type": "BiologicFunction"}, {"text": "Bone", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "prostate", "type": "AnatomicalStructure"}, {"text": "tubule - initiating cells", "type": "AnatomicalStructure"}, {"text": "TIC", "type": "AnatomicalStructure"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "low androgen levels", "type": "Finding"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "microenvironment interactions", "type": "BiologicFunction"}, {"text": "epithelial budding", "type": "BiologicFunction"}, {"text": "outgrowth", "type": "BiologicFunction"}]}

Example input:
Sentence: Kinesins are microtubule -based motor proteins that mediate diverse functions within the cell , including the transport of vesicles , organelles , chromosomes and protein complexes , as well as the movement of microtubules .

Example answer:
{"entities": [{"text": "Kinesins", "type": "Chemical"}, {"text": "microtubule", "type": "Chemical"}, {"text": "motor proteins", "type": "Chemical"}, {"text": "cell", "type": "AnatomicalStructure"}, {"text": "transport", "type": "BiologicFunction"}, {"text": "vesicles", "type": "AnatomicalStructure"}, {"text": "organelles", "type": "AnatomicalStructure"}, {"text": "chromosomes", "type": "AnatomicalStructure"}, {"text": "protein complexes", "type": "Chemical"}, {"text": "movement of microtubules", "type": "BiologicFunction"}]}

Example input:
Sentence: The kinesin motor protein Kif7 is required for T - cell development and normal MHC expression on thymic epithelial cells ( TEC ) in the thymus Kif7 is a ciliary kinesin motor protein that regulates mammalian Hedgehog pathway activation through influencing structure of the primary cilium .

Example answer:
{"entities": [{"text": "kinesin motor protein Kif7", "type": "Chemical"}, {"text": "T - cell development", "type": "BiologicFunction"}, {"text": "MHC", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "thymic epithelial cells", "type": "AnatomicalStructure"}, {"text": "TEC", "type": "AnatomicalStructure"}, {"text": "thymus", "type": "AnatomicalStructure"}, {"text": "Kif7", "type": "Chemical"}, {"text": "ciliary", "type": "AnatomicalStructure"}, {"text": "kinesin motor protein", "type": "Chemical"}, {"text": "regulates", "type": "BiologicFunction"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "Hedgehog pathway", "type": "BiologicFunction"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "primary cilium", "type": "AnatomicalStructure"}]}

Example input:
Sentence: KIF18A may be a useful predictive marker for lymph node metastasis in breast cancer , which could facilitate curative adjuvant treatment .

Example answer:
{"entities": [{"text": "KIF18A", "type": "Chemical"}, {"text": "predictive", "type": "IntellectualProduct"}, {"text": "marker", "type": "ClinicalAttribute"}, {"text": "lymph node metastasis", "type": "BiologicFunction"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the current study , the expression of kinesin family member 18A ( KIF18A ) , a member of kinesin superfamily , was investigated in breast cancer using immunohistochemistry , and its effect on breast cancer prognosis was examined .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "kinesin family member 18A", "type": "Chemical"}, {"text": "KIF18A", "type": "Chemical"}, {"text": "member of kinesin superfamily", "type": "Chemical"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "immunohistochemistry", "type": "HealthCareActivity"}]}

Input:
Sentence: Clinicopathological relevance of kinesin family member 18A expression in invasive breast cancer Recently , kinesin motor proteins have been focused on as targets for cancer therapy .

## Item MedMentions:test:1153
Example input:
Sentence: The median age of the patients was 16 years ( range 3 - 60 ) , 28 % of subjects had atopy , and 57 % carried ≥1 respiratory virus in nasopharynx .

Example answer:
{"entities": [{"text": "atopy", "type": "BiologicFunction"}, {"text": "respiratory virus", "type": "Virus"}, {"text": "nasopharynx", "type": "AnatomicalStructure"}]}

Example input:
Sentence: PMcoarse was associated with an increase in FENO , indicating sub - clinical airway inflammation in healthy children .

Example answer:
{"entities": [{"text": "airway", "type": "AnatomicalStructure"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "healthy children", "type": "Finding"}]}

Example input:
Sentence: Children of polygamous mothers had half the odds of receiving malaria medication for fever within 72 hours of symptom onset , while children with increased household wealth status had increased odds of childhood vaccination and receiving treatment for malaria .

Example answer:
{"entities": [{"text": "polygamous mothers", "type": "Finding"}, {"text": "malaria", "type": "BiologicFunction"}, {"text": "medication", "type": "Chemical"}, {"text": "childhood vaccination", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Thus , our finding of increased parvalbumin neuron density at early developmental times might suggest a mechanism by which an acute prenatal insult like LPS exposure could produce long - term changes in prefrontal cortical or subicular function .

Example answer:
{"entities": [{"text": "parvalbumin", "type": "Chemical"}, {"text": "neuron", "type": "AnatomicalStructure"}, {"text": "acute prenatal insult", "type": "InjuryOrPoisoning"}, {"text": "LPS", "type": "Chemical"}]}

Example input:
Sentence: For the December 2012 - February 2013 period , the Plasmodium vivax infection rate for An . darlingi was 7 . 8 % , and the entomological inoculation rate was 35 . 7 infective bites per person per three - month span .

Example answer:
{"entities": [{"text": "Plasmodium vivax infection", "type": "BiologicFunction"}, {"text": "An . darlingi", "type": "Eukaryote"}, {"text": "infective bites", "type": "InjuryOrPoisoning"}, {"text": "person", "type": "PopulationGroup"}]}

Example input:
Sentence: Haemophilus influenzae type b meningitis in a vaccinated and immunocompetent child Invasive Haemophilus influenzae type b ( Hib ) disease decreased dramatically after the introduction of conjugate vaccine in routine immunization schedules .

Example answer:
{"entities": [{"text": "Haemophilus influenzae type b meningitis", "type": "BiologicFunction"}, {"text": "vaccinated", "type": "HealthCareActivity"}, {"text": "immunocompetent", "type": "ClinicalAttribute"}, {"text": "Invasive Haemophilus influenzae type b ( Hib ) disease", "type": "BiologicFunction"}, {"text": "conjugate vaccine", "type": "Chemical"}, {"text": "immunization schedules", "type": "HealthCareActivity"}]}

Example input:
Sentence: Severe respiratory depression and bradycardia before induction of anesthesia and onset of Takotsubo cardiomyopathy after cardiopulmonary resuscitation A 69 - year -old woman undergoing treatment for hypertension and epilepsy was scheduled to undergo cataract surgery .

Example answer:
{"entities": [{"text": "respiratory depression", "type": "BiologicFunction"}, {"text": "bradycardia", "type": "BiologicFunction"}, {"text": "anesthesia", "type": "HealthCareActivity"}, {"text": "Takotsubo cardiomyopathy", "type": "BiologicFunction"}, {"text": "cardiopulmonary resuscitation", "type": "HealthCareActivity"}, {"text": "woman", "type": "PopulationGroup"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "hypertension", "type": "BiologicFunction"}, {"text": "epilepsy", "type": "BiologicFunction"}, {"text": "cataract surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: These findings raise the question whether the yellow fever vaccine strain may , through a potential molecular mimicry mechanism , be another infectious trigger for this neuro - immunological disorder .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "question", "type": "IntellectualProduct"}, {"text": "yellow fever vaccine strain", "type": "Chemical"}, {"text": "molecular mimicry", "type": "BiologicFunction"}, {"text": "infectious trigger", "type": "ClinicalAttribute"}, {"text": "neuro - immunological", "type": "BiologicFunction"}, {"text": "disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: The discovery of hypocretins , also known as orexins , and their link to narcolepsy has undoubtedly allowed us to advance our knowledge on key mechanisms controlling the boundaries and transitions between sleep and wakefulness .

Example answer:
{"entities": [{"text": "hypocretins", "type": "Chemical"}, {"text": "orexins", "type": "Chemical"}, {"text": "narcolepsy", "type": "BiologicFunction"}, {"text": "knowledge", "type": "IntellectualProduct"}, {"text": "sleep", "type": "BiologicFunction"}, {"text": "wakefulness", "type": "BiologicFunction"}]}

Example input:
Sentence: Narcolepsy Following Yellow Fever Vaccination : A Case Report Narcolepsy with cataplexy is a rare , but important differential diagnosis for daytime sleepiness and atonic paroxysms in an adolescent .

Example answer:
{"entities": [{"text": "Narcolepsy", "type": "BiologicFunction"}, {"text": "Yellow Fever Vaccination", "type": "HealthCareActivity"}, {"text": "Case Report", "type": "IntellectualProduct"}, {"text": "cataplexy", "type": "BiologicFunction"}, {"text": "differential diagnosis", "type": "HealthCareActivity"}, {"text": "daytime sleepiness", "type": "Finding"}, {"text": "atonic", "type": "Finding"}]}

Input:
Sentence: A recent increase in incidence in the pediatric age group probably linked to the use of the Pandemrix influenza vaccine in 2009 , has increased awareness that different environmental factors can " trigger " narcolepsy with cataplexy in a genetically susceptible population .

## Item MedMentions:test:813
Example input:
Sentence: KEGG pathway analysis showed that DHA may induce the apoptosis of cancer cells preferentially through mediating P53 , MAPK , TNF , PI3K / AKT , and NF - κB signaling pathways .

Example answer:
{"entities": [{"text": "DHA", "type": "Chemical"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "cancer cells", "type": "AnatomicalStructure"}, {"text": "P53", "type": "BiologicFunction"}, {"text": "MAPK", "type": "BiologicFunction"}, {"text": "TNF", "type": "BiologicFunction"}, {"text": "NF - κB signaling pathways", "type": "BiologicFunction"}]}

Example input:
Sentence: Improved hematopoietic differentiation of human pluripotent stem cells via estrogen receptor signaling pathway Aside from its importance in reproduction , estrogen ( E2 ) is known to regulate the proliferation and differentiation of hematopoietic stem cells in rodents .

Example answer:
{"entities": [{"text": "Improved", "type": "Finding"}, {"text": "hematopoietic differentiation", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "pluripotent stem cells", "type": "AnatomicalStructure"}, {"text": "estrogen receptor signaling pathway", "type": "BiologicFunction"}, {"text": "reproduction", "type": "BiologicFunction"}, {"text": "estrogen", "type": "Chemical"}, {"text": "E2", "type": "Chemical"}, {"text": "differentiation of hematopoietic stem cells", "type": "BiologicFunction"}, {"text": "rodents", "type": "Eukaryote"}]}

Example input:
Sentence: However , exogenous adenosine added to breast cancer cells or the A3 receptor agonist IB - MECA dose - dependently arrested cell motility by simultaneous stimulation of multiple leading edges , doubling cell surface areas and significantly reducing migration velocity by up to 75 % .

Example answer:
{"entities": [{"text": "adenosine", "type": "Chemical"}, {"text": "breast cancer cells", "type": "AnatomicalStructure"}, {"text": "A3 receptor", "type": "Chemical"}, {"text": "agonist", "type": "Chemical"}, {"text": "IB - MECA", "type": "Chemical"}, {"text": "cell motility", "type": "BiologicFunction"}, {"text": "leading edges", "type": "AnatomicalStructure"}, {"text": "cell surface", "type": "AnatomicalStructure"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "migration", "type": "BiologicFunction"}]}

Example input:
Sentence: Interestingly , knockdown of STAT3 significantly attenuated HDACIs - induced P - gp up - regulation in colorectal cancer cells , suggesting that STAT3 plays a crucial role in HDACIs - up - regulated P - gp .

Example answer:
{"entities": [{"text": "knockdown", "type": "ResearchActivity"}, {"text": "STAT3", "type": "Chemical"}, {"text": "HDACIs", "type": "Chemical"}, {"text": "P - gp", "type": "Chemical"}, {"text": "up - regulation", "type": "BiologicFunction"}, {"text": "colorectal cancer cells", "type": "AnatomicalStructure"}, {"text": "up - regulated", "type": "BiologicFunction"}]}

Example input:
Sentence: However , the mechanism for events after dimerization in breast cancer models is not clear .

Example answer:
{"entities": [{"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Upregulating and activating DOR promoted the proliferation of human breast cancer cells in a concentration‑dependent manner within a specific concentration range , whereas downregulating or inhibiting DOR activation significantly suppressed cell proliferation .

Example answer:
{"entities": [{"text": "Upregulating", "type": "BiologicFunction"}, {"text": "activating", "type": "BiologicFunction"}, {"text": "DOR", "type": "Chemical"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "downregulating", "type": "BiologicFunction"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "cell proliferation", "type": "BiologicFunction"}]}

Example input:
Sentence: Regarding the signaling pathway , targeting epidermal growth factor ( EGF ) receptor ( EGFR ) , ErbB2 ( HER2 ) or inhibition of tumor necrosis factor - α - converting enzyme , one of the enzymes which generates soluble EGF - like ligands , resulted in partial recovery of MHC - I surface expression .

Example answer:
{"entities": [{"text": "signaling pathway", "type": "BiologicFunction"}, {"text": "targeting", "type": "BiologicFunction"}, {"text": "epidermal growth factor", "type": "Chemical"}, {"text": "EGF", "type": "Chemical"}, {"text": "receptor", "type": "Chemical"}, {"text": "EGFR", "type": "Chemical"}, {"text": "ErbB2", "type": "Chemical"}, {"text": "HER2", "type": "Chemical"}, {"text": "tumor necrosis factor", "type": "Chemical"}, {"text": "α - converting enzyme", "type": "Chemical"}, {"text": "enzymes", "type": "Chemical"}, {"text": "EGF - like ligands", "type": "Chemical"}, {"text": "MHC - I", "type": "Chemical"}, {"text": "surface", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}]}

Example input:
Sentence: Levels of ACTA2 , STAT1 , and HER2 were increased and relapse free survival was decreased in high - risk breast cancer patients .

Example answer:
{"entities": [{"text": "ACTA2", "type": "Chemical"}, {"text": "STAT1", "type": "Chemical"}, {"text": "HER2", "type": "Chemical"}, {"text": "high - risk", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: We also investigated the effect of ACTA2 on cell motility , which was suppressed by ACTA2 shRNA overexpression in MDA - MB231 HER2 and 4T1 mammary carcinoma cells .

Example answer:
{"entities": [{"text": "ACTA2", "type": "Chemical"}, {"text": "cell motility", "type": "BiologicFunction"}, {"text": "ACTA2 shRNA", "type": "Chemical"}, {"text": "overexpression", "type": "BiologicFunction"}, {"text": "MDA - MB231", "type": "AnatomicalStructure"}, {"text": "HER2", "type": "Chemical"}, {"text": "4T1 mammary carcinoma cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Taken together , these results demonstrated that induction of ACTA2 by EGFR and HER2 dimerization was regulated through a JAK2 / STAT1 signaling pathway , and aberrant ACTA2 expression accelerated the invasiveness and metastasis of breast cancer cells .

Example answer:
{"entities": [{"text": "ACTA2", "type": "Chemical"}, {"text": "EGFR", "type": "Chemical"}, {"text": "HER2", "type": "Chemical"}, {"text": "JAK2", "type": "Chemical"}, {"text": "STAT1", "type": "Chemical"}, {"text": "signaling pathway", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "invasiveness", "type": "BiologicFunction"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Input:
Sentence: Dimerization of EGFR and HER2 induces breast cancer cell motility through STAT1 -dependent ACTA2 induction The dimerization of EGFR and HER2 is associated with poor prognosis such as induction of tumor growth and cell invasion compared to when EGFR remains as a homodimer .

## Item MedMentions:test:1378
Example input:
Sentence: To characterize the effect of MDO on key components of sleep architecture in infants with PRS .

Example answer:
{"entities": [{"text": "MDO", "type": "HealthCareActivity"}, {"text": "sleep", "type": "BiologicFunction"}, {"text": "PRS", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Ten of these infants developed WM abnormalities associated with prematurity .

Example answer:
{"entities": [{"text": "WM abnormalities", "type": "BiologicFunction"}, {"text": "prematurity", "type": "Finding"}]}

Example input:
Sentence: Charts from 32 infants with PRS that were addressed with MDO at our tertiary - care children 's hospital were retrospectively reviewed .

Example answer:
{"entities": [{"text": "PRS", "type": "AnatomicalStructure"}, {"text": "MDO", "type": "HealthCareActivity"}, {"text": "tertiary - care children 's hospital", "type": "Organization"}]}

Example input:
Sentence: 22 % of infants diagnosed with BPD and 34 % of preterm infants without BPD had no clinical signs of late respiratory disease during early childhood .

Example answer:
{"entities": [{"text": "diagnosed", "type": "Finding"}, {"text": "BPD", "type": "BiologicFunction"}, {"text": "clinical signs", "type": "Finding"}, {"text": "late respiratory disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Thirty - two out of 72 ELBW infants underwent conventional MR imaging and DTI at term - equivalent age .

Example answer:
{"entities": [{"text": "ELBW infants", "type": "Finding"}, {"text": "MR imaging", "type": "HealthCareActivity"}, {"text": "DTI", "type": "HealthCareActivity"}]}

Example input:
Sentence: A retrospective cohort analysis from a single institution across the duration of the study comparing the clinical and financial outcomes of infants ( aged < 32 weeks ) treated under the 2009 AAP guidelines ( PRE ) and infants ( aged > 29 weeks ) managed after the 2014 AAP guidelines ( POST ) took effect .

Example answer:
{"entities": [{"text": "cohort analysis", "type": "ResearchActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "treated", "type": "Finding"}, {"text": "AAP", "type": "Organization"}, {"text": "guidelines", "type": "IntellectualProduct"}, {"text": "AAP guidelines", "type": "IntellectualProduct"}]}

Example input:
Sentence: We aimed to assess rotational mechanics in infants with hypoxic ischemic encephalopathy ( HIE ) and premature infants ( < 32 weeks ) at 36 weeks postmenstrual age ( PMA ) ( preterm group ) and compare them with healthy term controls ( term controls ) .

Example answer:
{"entities": [{"text": "rotational", "type": "SpatialConcept"}, {"text": "hypoxic ischemic encephalopathy", "type": "BiologicFunction"}, {"text": "HIE", "type": "BiologicFunction"}, {"text": "preterm group", "type": "PopulationGroup"}]}

Example input:
Sentence: Of these , 26 infants ( 57 . 7 % male ; mean age = 4 . 1 weeks , SD = 5 . 0 ) had pre - and post - operative polysomnograms ( PSG ) .

Example answer:
{"entities": [{"text": "polysomnograms", "type": "HealthCareActivity"}, {"text": "PSG", "type": "HealthCareActivity"}]}

Example input:
Sentence: MDO improve s several sleep architecture parameters in this sample of infants with PRS .

Example answer:
{"entities": [{"text": "MDO", "type": "HealthCareActivity"}, {"text": "improve", "type": "Finding"}, {"text": "sleep", "type": "BiologicFunction"}, {"text": "PRS", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Although MDO has been shown to improve the apnea - hypopnea index ( AHI ) in children with PRS , the consequences of MDO on other aspects of infant sleep , including hypercapnea , hypoxia , the REM to Non - REM ratio , as well as its effect on central and mixed apneas has not been investigated with an adequate sample size .

Example answer:
{"entities": [{"text": "MDO", "type": "HealthCareActivity"}, {"text": "improve", "type": "Finding"}, {"text": "apnea - hypopnea index", "type": "IntellectualProduct"}, {"text": "AHI", "type": "IntellectualProduct"}, {"text": "PRS", "type": "AnatomicalStructure"}, {"text": "sleep", "type": "BiologicFunction"}, {"text": "hypercapnea", "type": "Finding"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "REM", "type": "BiologicFunction"}, {"text": "Non - REM", "type": "BiologicFunction"}, {"text": "central", "type": "BiologicFunction"}, {"text": "mixed apneas", "type": "BiologicFunction"}]}

Input:
Sentence: Among the 26 infants , 73 . 1 % demonstrated severe pre - MDO sleep apnea ( AHI > 10 ) .

## Item MedMentions:test:1421
Example input:
Sentence: A one - chamber pacemaker was implanted in each of the 28 pigs .

Example answer:
{"entities": [{"text": "one - chamber pacemaker", "type": "MedicalDevice"}, {"text": "pigs", "type": "Eukaryote"}]}

Example input:
Sentence: However , relatively aggressive protocols of stimulation were required in order to induce arrhythmia in the studied pigs .

Example answer:
{"entities": [{"text": "protocols", "type": "IntellectualProduct"}, {"text": "stimulation", "type": "HealthCareActivity"}, {"text": "arrhythmia", "type": "BiologicFunction"}, {"text": "pigs", "type": "Eukaryote"}]}

Example input:
Sentence: Downregulation of repolarizing TREK - 1 channels was associated with prolongation of atrial effective refractory periods versus baseline conditions , consistent with prior observations in humans with HF .

Example answer:
{"entities": [{"text": "Downregulation", "type": "BiologicFunction"}, {"text": "repolarizing", "type": "BiologicFunction"}, {"text": "TREK - 1 channels", "type": "Chemical"}, {"text": "atrial effective refractory periods", "type": "Finding"}, {"text": "observations", "type": "ResearchActivity"}, {"text": "humans", "type": "Eukaryote"}, {"text": "HF", "type": "BiologicFunction"}]}

Example input:
Sentence: Both RT - PCR and western blotting showed a marked increase in the expression of the adult pigs compared with prenatal pigs .

Example answer:
{"entities": [{"text": "RT - PCR", "type": "ResearchActivity"}, {"text": "western blotting", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "pigs", "type": "Eukaryote"}]}

Example input:
Sentence: Vaccination of piglets at 2 and 3 weeks of age with Ingelvac PRRSFLEX ® EU provides protection against heterologous field challenge in the face of homologous maternally derived antibodies Due to difficulties in eradicating porcine reproductive and respiratory syndrome ( PRRS ) linked to biosecurity challenges , transmission of the virus and the lack of efficient DIVA vaccines , successful control of PRRS requires a combination of strict management measures and vaccination of both sows and piglets .

Example answer:
{"entities": [{"text": "Vaccination", "type": "HealthCareActivity"}, {"text": "piglets", "type": "Eukaryote"}, {"text": "Ingelvac PRRSFLEX ® EU", "type": "Chemical"}, {"text": "maternally derived antibodies", "type": "Chemical"}, {"text": "eradicating", "type": "HealthCareActivity"}, {"text": "porcine reproductive and respiratory syndrome", "type": "BiologicFunction"}, {"text": "PRRS", "type": "BiologicFunction"}, {"text": "transmission of the virus", "type": "BiologicFunction"}, {"text": "DIVA vaccines", "type": "Chemical"}, {"text": "management measures", "type": "HealthCareActivity"}, {"text": "vaccination", "type": "HealthCareActivity"}]}

Example input:
Sentence: Males and females did not differ significantly in terms of VERP duration determined throughout the whole study period .

Example answer:
{"entities": [{"text": "VERP", "type": "Finding"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Ventricular Effective Refraction Period and Ventricular Repolarization Analysis in Experimental Tachycardiomyopathy in Swine Swine are recognized animal models of human cardiovascular diseases .

Example answer:
{"entities": [{"text": "Ventricular Effective Refraction Period", "type": "Finding"}, {"text": "Ventricular Repolarization", "type": "BiologicFunction"}, {"text": "Analysis", "type": "ResearchActivity"}, {"text": "Tachycardiomyopathy", "type": "BiologicFunction"}, {"text": "Swine", "type": "Eukaryote"}, {"text": "animal models", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "cardiovascular diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: The duration of the QTc interval of female pigs was shown to be significantly longer than that of the males throughout the whole study period .

Example answer:
{"entities": [{"text": "pigs", "type": "Eukaryote"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Ventricular pacing , stimulation with 2 and 3 premature impulses at progressively shorter coupling intervals and an imposed rhythm of 130 bpm or 150 bpm induced transient ventricular tachycardia in one female pig and four male pigs .

Example answer:
{"entities": [{"text": "Ventricular pacing", "type": "HealthCareActivity"}, {"text": "stimulation", "type": "HealthCareActivity"}, {"text": "rhythm", "type": "Finding"}, {"text": "ventricular tachycardia", "type": "BiologicFunction"}, {"text": "pig", "type": "Eukaryote"}, {"text": "pigs", "type": "Eukaryote"}]}

Example input:
Sentence: The aim of this study was to analyze changes in the durations of ventricular effective refraction period ( VERP ) , QT and QTc intervals of pigs with chronic tachycardia - induced tachycardiomyopathy ( TIC ) .

Example answer:
{"entities": [{"text": "ventricular effective refraction period", "type": "Finding"}, {"text": "VERP", "type": "Finding"}, {"text": "QT", "type": "ClinicalAttribute"}, {"text": "pigs", "type": "Eukaryote"}, {"text": "tachycardia", "type": "BiologicFunction"}, {"text": "tachycardiomyopathy", "type": "BiologicFunction"}, {"text": "TIC", "type": "BiologicFunction"}]}

Input:
Sentence: Beginning from the 12th week of rapid ventricular pacing , a significant increase in duration of VERP was observed in both male and female pigs .

## Item MedMentions:test:1469
Example input:
Sentence: Interestingly , their absorption profiles were totally different ; prompt absorption was observed for the complex prepared in acetate buffer , whereas sustained absorption was observed for the complex prepared in citrate buffer .

Example answer:
{"entities": [{"text": "absorption", "type": "BiologicFunction"}, {"text": "complex", "type": "Chemical"}]}

Example input:
Sentence: The five peaks of components were successfully isolated , and peaks of J2 , J3 , J5 , and J7 were assigned to be Jatropha factors C1 , C2 , C3 , and C4 / 5 , but J6 was a mixture of Jatropha factor C6 and its isomer based on the data of UV and LC - MS / MS , and J2 was identified using ( 1 ) H NMR analysis .

Example answer:
{"entities": [{"text": "Jatropha", "type": "Eukaryote"}, {"text": "MS", "type": "HealthCareActivity"}, {"text": "( 1 ) H NMR analysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: Phenol red diffusion studies and UV - Vis spectra of phenol red - silk tyrosine hydrogels at different pHs showed altered absorption bands , confirming entrapment of dye within the hydrogel network .

Example answer:
{"entities": [{"text": "Phenol red", "type": "Chemical"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "UV - Vis spectra", "type": "HealthCareActivity"}, {"text": "phenol red", "type": "Chemical"}, {"text": "silk tyrosine", "type": "Chemical"}, {"text": "hydrogels", "type": "Chemical"}, {"text": "confirming", "type": "Finding"}, {"text": "entrapment", "type": "Finding"}, {"text": "dye", "type": "Chemical"}, {"text": "hydrogel network", "type": "Chemical"}]}

Example input:
Sentence: The 633 and 654 nm bands in the 77 K fluorescence emission spectra indicated the presence of Pchlide and Pchl pigments .

Example answer:
{"entities": [{"text": "fluorescence emission spectra", "type": "HealthCareActivity"}, {"text": "Pchlide", "type": "Chemical"}, {"text": "Pchl pigments", "type": "Chemical"}]}

Example input:
Sentence: By choosing characteristic absorption peaks , removing baseline and using the least square method , we can identify the components and proportions of each mixture , where the goodness of fit to practical situation is up to 94 % .

Example answer:
{"entities": []}

Example input:
Sentence: The results show that the all THz transmission and absorption spectra of chlorophyll a and β - carotene changed upon light treatment , with the maximum changes at 15 min of illumination indicating the greatest changes of the collective vibrational mode of chlorophyll a and β - carotene .

Example answer:
{"entities": [{"text": "THz transmission", "type": "HealthCareActivity"}, {"text": "absorption spectra", "type": "HealthCareActivity"}, {"text": "chlorophyll a", "type": "Chemical"}, {"text": "β - carotene", "type": "Chemical"}, {"text": "illumination", "type": "HealthCareActivity"}]}

Example input:
Sentence: Due to the spectral overlap between phenol red absorbance at 415 nm and di - tyrosine fluorescence at 417 nm , phenol red - silk hydrogels provide both absorbance and fluorescence -based pH sensing .

Example answer:
{"entities": [{"text": "spectral overlap", "type": "Finding"}, {"text": "phenol red", "type": "Chemical"}, {"text": "di - tyrosine", "type": "Chemical"}, {"text": "silk", "type": "Chemical"}, {"text": "hydrogels", "type": "Chemical"}]}

Example input:
Sentence: UV - visible and Resonance Raman spectroelectrochemical studies suggest the formation of a high valent iron - oxo species as the catalytic intermediate .

Example answer:
{"entities": [{"text": "Resonance Raman spectroelectrochemical studies", "type": "HealthCareActivity"}]}

Example input:
Sentence: Ultraviolet absorption spectroscopy ( UV - vis ) analysis confirmed the formation and allowed the quantification of both native ( AM - RIF ) and acetylated ( AMA - RIF ) amylose inclusion complexes .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "AM", "type": "Chemical"}, {"text": "RIF", "type": "Chemical"}, {"text": "AMA", "type": "Chemical"}, {"text": "amylose", "type": "Chemical"}]}

Example input:
Sentence: Temperature - and solvent -dependent absorption changes showed that DANP and pyrene chromophores stacked at room temperature in an aqueous buffer solution and quenched fluorescence .

Example answer:
{"entities": [{"text": "solvent", "type": "Chemical"}, {"text": "DANP", "type": "Chemical"}, {"text": "stacked", "type": "SpatialConcept"}, {"text": "room temperature", "type": "Finding"}, {"text": "quenched fluorescence", "type": "HealthCareActivity"}]}

Input:
Sentence: UV - Vis spectrum of reaction mixture showed strong absorption peak with centering at 400 nm .

## Item MedMentions:test:1521
Example input:
Sentence: Patient age ranged from 12 to 68 years , with a median age of 20 and 51 years among those with ovarian and uterine PNETs , respectively .

Example answer:
{"entities": [{"text": "ovarian", "type": "AnatomicalStructure"}, {"text": "uterine", "type": "AnatomicalStructure"}, {"text": "PNETs", "type": "BiologicFunction"}]}

Example input:
Sentence: Results The mean age of patients was 11 . 2 ± 5 . 4 years ( range , 1 - 27 years ) , and approximately one - half were female .

Example answer:
{"entities": [{"text": "female", "type": "PopulationGroup"}]}

Example input:
Sentence: Patients with VWD were younger , 49 . 67 versus 57 . 30 years , Caucasian , 82 .

Example answer:
{"entities": [{"text": "VWD", "type": "BiologicFunction"}, {"text": "Caucasian", "type": "PopulationGroup"}]}

Example input:
Sentence: Seventy - one patients ( 43 males , 28 females ; aged 70 . 9±10 .

Example answer:
{"entities": [{"text": "aged", "type": "PopulationGroup"}]}

Example input:
Sentence: The risk of HTN is reduced in patients with VWD , but not after adjustment for HTN risk factors plus demographics , as patients with VWD not having HTN are also typically young , Caucasian , and female .

Example answer:
{"entities": [{"text": "HTN", "type": "BiologicFunction"}, {"text": "VWD", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "Caucasian", "type": "PopulationGroup"}]}

Example input:
Sentence: Patients were predominantly male ( 76 . 1 % ) and young ( mean age 28 years ) .

Example answer:
{"entities": []}

Example input:
Sentence: The mean age of patient was 44 . 53±8 . 69 years , 89 . 5 % of them were males .

Example answer:
{"entities": []}

Example input:
Sentence: Patient DR , aged 51 , and patient KH , aged 78 .

Example answer:
{"entities": []}

Example input:
Sentence: Of 60 patients , 42 ( 70 % ) were male , all were white , with a median ( interquartile range ) age of 71 ( 64 to 82 ) years .

Example answer:
{"entities": [{"text": "white", "type": "PopulationGroup"}]}

Example input:
Sentence: There were 27 male and 17 female patients with a mean age of 41 ± 12 . 7 years ( range , 15 to 67 ) .

Example answer:
{"entities": []}

Input:
Sentence: Patients with HTN were older , 67 . 55 versus 47 . 29 years , male , 45 .

## Item MedMentions:test:1413
Example input:
Sentence: miR - 495 was upregulated in clinical cancer tissues compared with adjacent non - cancerous tissues , and radiation significantly reduced the expression level of miR - 495 in carcinoma cell lines .

Example answer:
{"entities": [{"text": "miR - 495", "type": "AnatomicalStructure"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "adjacent", "type": "SpatialConcept"}, {"text": "non - cancerous tissues", "type": "AnatomicalStructure"}, {"text": "carcinoma cell lines", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Since 2005 , when miRNA deregulation was first reported in breast cancer , more than 1000 reports have been published about miRNAs .

Example answer:
{"entities": [{"text": "miRNA", "type": "Chemical"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "reports", "type": "IntellectualProduct"}, {"text": "miRNAs", "type": "Chemical"}]}

Example input:
Sentence: MiR - 4638 - 5p inhibits castration resistance of prostate cancer through repressing Kidins220 expression and PI3K / AKT pathway activity MicroRNAs ( miRNAs ) are short , conserved segments of non - coding RNA which play a significant role in prostate cancer development and progression .

Example answer:
{"entities": [{"text": "MiR - 4638 - 5p", "type": "AnatomicalStructure"}, {"text": "castration resistance of prostate cancer", "type": "BiologicFunction"}, {"text": "Kidins220", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "MicroRNAs", "type": "Chemical"}, {"text": "miRNAs", "type": "Chemical"}, {"text": "conserved segments", "type": "SpatialConcept"}, {"text": "non - coding RNA", "type": "Chemical"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "progression", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , we found that miR - 4638 - 5p , through regulating Kidins220 and the downstream activity of VEGF and PI3K / AKT pathway , influences prostate cancer progression via angiogenesis .

Example answer:
{"entities": [{"text": "miR - 4638 - 5p", "type": "AnatomicalStructure"}, {"text": "Kidins220", "type": "AnatomicalStructure"}, {"text": "downstream", "type": "SpatialConcept"}, {"text": "VEGF", "type": "Chemical"}, {"text": "prostate cancer progression", "type": "BiologicFunction"}, {"text": "angiogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Restoration of miR - 424 - 5p in EC - 1 cells by using miR - 424 - 5p mimics could decrease the invasion , metastasis and proliferation of EC - 1 cells , indicating its role in inhibition on the invasion and metastasis ability of ESCC cells and tissues .

Example answer:
{"entities": [{"text": "miR - 424 - 5p", "type": "AnatomicalStructure"}, {"text": "EC - 1 cells", "type": "AnatomicalStructure"}, {"text": "invasion", "type": "BiologicFunction"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "ESCC", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: MiR - 376c was significantly downregulated in cervical cancer cell lines and clinical tissues .

Example answer:
{"entities": [{"text": "MiR - 376c", "type": "AnatomicalStructure"}, {"text": "downregulated", "type": "BiologicFunction"}, {"text": "cervical cancer", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The role of miR - 4638 - 5p in prostate cancer androgen - independent growth has been demonstrated both in vitro and in vivo .

Example answer:
{"entities": [{"text": "miR - 4638 - 5p", "type": "AnatomicalStructure"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "androgen - independent growth", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: Our results described that miR - 424 - 5p - SMAD7 pathway contributed to ESCC invasion and metastasis and up - regulation of miR - 424 - 5p perhaps provided a strategy for preventing tumor invasion , metastasis .

Example answer:
{"entities": [{"text": "miR - 424 - 5p", "type": "AnatomicalStructure"}, {"text": "SMAD7", "type": "AnatomicalStructure"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "ESCC", "type": "BiologicFunction"}, {"text": "invasion", "type": "BiologicFunction"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "up - regulation", "type": "BiologicFunction"}, {"text": "tumor invasion", "type": "Finding"}]}

Example input:
Sentence: We showed that the expression levels of miR - 424 - 5p were decreased both in ESCC tissues and cell lines .

Example answer:
{"entities": [{"text": "miR - 424 - 5p", "type": "AnatomicalStructure"}, {"text": "ESCC", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "cell lines", "type": "AnatomicalStructure"}]}

Example input:
Sentence: MiR - 424 - 5p participates in esophageal squamous cell carcinoma invasion and metastasis via SMAD7 pathway mediated EMT ESCC is a life - threatening disease due to invasion and metastasis in the early stage .

Example answer:
{"entities": [{"text": "MiR - 424 - 5p", "type": "AnatomicalStructure"}, {"text": "esophageal squamous cell carcinoma", "type": "BiologicFunction"}, {"text": "invasion", "type": "BiologicFunction"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "SMAD7", "type": "AnatomicalStructure"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "EMT", "type": "BiologicFunction"}, {"text": "ESCC", "type": "BiologicFunction"}, {"text": "life - threatening", "type": "Finding"}, {"text": "disease", "type": "BiologicFunction"}]}

Input:
Sentence: Recent evidence had suggested that deregulation of miR - 424 - 5p took an important role in cancers .

## Item MedMentions:test:1149
Example input:
Sentence: American cutaneous leishmaniasis : In situ immune response of patients with recent and late lesions TNF - α , IFN - γ , IL - 10 , IL - 17 , CD68 and CD57 were evaluated in biopsies of patients with American cutaneous leishmaniasis living in Sorocaba , Brazil .

Example answer:
{"entities": [{"text": "American cutaneous leishmaniasis", "type": "BiologicFunction"}, {"text": "immune response", "type": "BiologicFunction"}, {"text": "recent", "type": "InjuryOrPoisoning"}, {"text": "lesions", "type": "Finding"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "IL - 17", "type": "Chemical"}, {"text": "CD68", "type": "Chemical"}, {"text": "CD57", "type": "Chemical"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "biopsies", "type": "HealthCareActivity"}, {"text": "Sorocaba", "type": "SpatialConcept"}, {"text": "Brazil", "type": "SpatialConcept"}]}

Example input:
Sentence: chagasi infection and for controlling human visceral leishmaniasis ( VL ) .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "visceral leishmaniasis", "type": "BiologicFunction"}, {"text": "VL", "type": "BiologicFunction"}]}

Example input:
Sentence: Our data provide the first evidence that KSHV gpK8 . 1 , gB , and gH / gL glycoproteins can be incorporated onto the surface of VLPs and used as prophylactic vaccine candidates , with potential to prevent KSHV infection .

Example answer:
{"entities": [{"text": "KSHV", "type": "Virus"}, {"text": "gpK8 . 1", "type": "Chemical"}, {"text": "gB", "type": "Chemical"}, {"text": "gH", "type": "Chemical"}, {"text": "gL glycoproteins", "type": "Chemical"}, {"text": "VLPs", "type": "AnatomicalStructure"}, {"text": "prophylactic vaccine", "type": "Chemical"}, {"text": "infection", "type": "BiologicFunction"}]}

Example input:
Sentence: Mucosal IgM Antibody with d - Mannose Affinity in Fugu Takifugu rubripes Is Utilized by a Monogenean Parasite Heterobothrium okamotoi for Host Recognition How parasites recognize their definitive hosts is a mystery ; however , parasitism is reportedly initiated by recognition of certain molecules on host surfaces .

Example answer:
{"entities": [{"text": "Mucosal", "type": "AnatomicalStructure"}, {"text": "IgM Antibody", "type": "Chemical"}, {"text": "d - Mannose", "type": "Chemical"}, {"text": "Fugu Takifugu rubripes", "type": "Eukaryote"}, {"text": "Monogenean", "type": "Eukaryote"}, {"text": "Parasite", "type": "Eukaryote"}, {"text": "Heterobothrium okamotoi", "type": "Eukaryote"}, {"text": "Host Recognition", "type": "BiologicFunction"}, {"text": "parasites", "type": "Eukaryote"}, {"text": "recognize", "type": "BiologicFunction"}, {"text": "recognition", "type": "BiologicFunction"}, {"text": "host surfaces", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Trisaccharide containing α2 , 3 - linked sialic acid is a receptor for mumps virus Mumps virus ( MuV ) remains an important pathogen worldwide , causing epidemic parotitis , orchitis , meningitis , and encephalitis .

Example answer:
{"entities": [{"text": "Trisaccharide", "type": "Chemical"}, {"text": "α2 , 3 - linked sialic acid", "type": "Chemical"}, {"text": "receptor", "type": "Chemical"}, {"text": "mumps virus", "type": "Virus"}, {"text": "Mumps virus", "type": "Virus"}, {"text": "MuV", "type": "Virus"}, {"text": "epidemic parotitis", "type": "BiologicFunction"}, {"text": "orchitis", "type": "BiologicFunction"}, {"text": "meningitis", "type": "BiologicFunction"}, {"text": "encephalitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Neutralizing antibody assay revealed that sera from mice immunized with the VLPs inhibited KSHV infection of HEK - 293 cells in a dose - dependent manner .

Example answer:
{"entities": [{"text": "Neutralizing antibody", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "immunized", "type": "HealthCareActivity"}, {"text": "VLPs", "type": "AnatomicalStructure"}, {"text": "KSHV", "type": "Virus"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "HEK - 293 cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The possible role of Sergentomyia in the circulation of mammalian leishmaniases in the Old World has been considered as Leishmania DNA and / or parasites have been identified in several species .

Example answer:
{"entities": [{"text": "possible", "type": "Finding"}, {"text": "Sergentomyia", "type": "Eukaryote"}, {"text": "circulation", "type": "Finding"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "leishmaniases", "type": "BiologicFunction"}, {"text": "Old World", "type": "SpatialConcept"}, {"text": "Leishmania DNA", "type": "Chemical"}, {"text": "parasites", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: Can Sergentomyia ( Diptera , Psychodidae ) play a role in the transmission of mammal - infecting Leishmania ?

Example answer:
{"entities": [{"text": "Sergentomyia", "type": "Eukaryote"}, {"text": "Diptera", "type": "Eukaryote"}, {"text": "Psychodidae", "type": "Eukaryote"}, {"text": "mammal", "type": "Eukaryote"}, {"text": "infecting", "type": "BiologicFunction"}, {"text": "Leishmania", "type": "Eukaryote"}]}

Example input:
Sentence: 1 , gB , and gH / gL glycoproteins , implicated in the virus entry into host cells , are attractive vaccine targets for eliciting potent neutralizing antibodies ( nAbs ) against virus infection .

Example answer:
{"entities": [{"text": "1", "type": "Chemical"}, {"text": "gB", "type": "Chemical"}, {"text": "gH", "type": "Chemical"}, {"text": "gL glycoproteins", "type": "Chemical"}, {"text": "virus", "type": "Virus"}, {"text": "host cells", "type": "AnatomicalStructure"}, {"text": "vaccine", "type": "Chemical"}, {"text": "neutralizing antibodies", "type": "Chemical"}, {"text": "nAbs", "type": "Chemical"}, {"text": "virus infection", "type": "BiologicFunction"}]}

Example input:
Sentence: However , several criteria must be fulfilled to incriminate an arthropod as a biological vector of leishmaniasis , namely : it must be attracted to and willing to feed on humans and any reservoir host , and be present in the same environment ; several unambiguously identified wild female flies not containing blood meals have to be found infected ( through isolation and / or typing of parasites ) with the same strain of Leishmania as occurs in humans or any reservoir host ; the presence of infective forms of Leishmania on naturally infected females and / or on colonized sand flies infected experimentally should be observed ; and finally , the vector has to be able to transmit parasites as a result of blood - feeding on a susceptible mammal .

Example answer:
{"entities": [{"text": "arthropod", "type": "Eukaryote"}, {"text": "biological vector", "type": "Eukaryote"}, {"text": "leishmaniasis", "type": "BiologicFunction"}, {"text": "willing", "type": "Finding"}, {"text": "humans", "type": "Eukaryote"}, {"text": "present", "type": "Finding"}, {"text": "environment", "type": "SpatialConcept"}, {"text": "wild", "type": "Eukaryote"}, {"text": "flies", "type": "Eukaryote"}, {"text": "blood", "type": "BodySubstance"}, {"text": "infected", "type": "Finding"}, {"text": "isolation", "type": "HealthCareActivity"}, {"text": "typing", "type": "HealthCareActivity"}, {"text": "parasites", "type": "Eukaryote"}, {"text": "Leishmania", "type": "Eukaryote"}, {"text": "presence", "type": "Finding"}, {"text": "infective", "type": "BiologicFunction"}, {"text": "sand flies", "type": "Eukaryote"}, {"text": "vector", "type": "Eukaryote"}, {"text": "mammal", "type": "Eukaryote"}]}

Input:
Sentence: Because the sand fly salivary proteins are potent immunogens obligatorily co - deposited during transmission of Leishmania parasites , their inclusion in an anti - Leishmania vaccine has been investigated in past decades .

## Item MedMentions:test:1612
Example input:
Sentence: 68 μg CE / g DW , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 7mmHg , and 13 . 5±3 .

Example answer:
{"entities": []}

Example input:
Sentence: 37 μM ( MQ ) , and 5 . 06 ± 0 . 86 μM ( GSK369796 ) .

Example answer:
{"entities": [{"text": "MQ", "type": "Chemical"}, {"text": "GSK369796", "type": "Chemical"}]}

Example input:
Sentence: 774 μM , PC3 : 7 .

Example answer:
{"entities": [{"text": "PC3", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 7μm .

Example answer:
{"entities": []}

Example input:
Sentence: 6 μm at baseline to 270 . 8 ± 27 .

Example answer:
{"entities": []}

Example input:
Sentence: 4±2 . 28μg .

Example answer:
{"entities": []}

Example input:
Sentence: 6 μm ( 2 ) and 27 . 5 - 48 . 9 μm , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 3 to 52 . 5 μg / m ( 3 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 9 μg / 10 μl ) .

Example answer:
{"entities": []}

Input:
Sentence: 7 μg .

## Item MedMentions:test:1395
Example input:
Sentence: Convergent validity was tested with a Pearson r correlation coefficient between the WARPS / STAID and ISS scores .

Example answer:
{"entities": [{"text": "ISS scores", "type": "IntellectualProduct"}]}

Example input:
Sentence: Very large significant correlation was obtained between the RPEres and score ( r = 0 . 83 ; ± 0 . 22 CL , p < 0 .

Example answer:
{"entities": [{"text": "RPEres", "type": "IntellectualProduct"}]}

Example input:
Sentence: Rigid 32R computed by the framework was more accurate than that obtained manually , with the respective target registration error below 0 .

Example answer:
{"entities": [{"text": "computed", "type": "HealthCareActivity"}]}

Example input:
Sentence: There is a positive correlation ( r = 0 . 80 ) and moderate agreement ( κ = 0 . 509 ) of grading with PC - MRI and 3D - CISS sequences .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "grading", "type": "IntellectualProduct"}, {"text": "PC - MRI", "type": "HealthCareActivity"}]}

Example input:
Sentence: The difference was clinically negligible and independent of renal length ( p = 0 . 698 ) , volume ( p = 0 . 297 ) , and patient age ( p = 0 . 768 ) but was associated with SRF ( p = 0 . 018 ) .

Example answer:
{"entities": [{"text": "renal", "type": "AnatomicalStructure"}, {"text": "SRF", "type": "Finding"}]}

Example input:
Sentence: Estimation of Split Renal Function With ( 99m ) Tc - DMSA SPECT : Comparison Between 3D Volumetric Assessment and 2D Coronal Projection Imaging Split renal function ( SRF ) can be estimated with ( 99m ) Tc - labeled dimercaptosuccinic acid ( DMSA ) SPECT cortical renal scintigraphy on either 2D projected images or 3D images .

Example answer:
{"entities": [{"text": "Estimation", "type": "HealthCareActivity"}, {"text": "Split Renal Function", "type": "Finding"}, {"text": "( 99m ) Tc - DMSA", "type": "Chemical"}, {"text": "SPECT", "type": "HealthCareActivity"}, {"text": "3D", "type": "SpatialConcept"}, {"text": "Volumetric Assessment", "type": "HealthCareActivity"}, {"text": "2D", "type": "SpatialConcept"}, {"text": "Coronal Projection Imaging", "type": "HealthCareActivity"}, {"text": "Split renal function", "type": "Finding"}, {"text": "SRF", "type": "Finding"}, {"text": "( 99m ) Tc - labeled dimercaptosuccinic acid ( DMSA )", "type": "Chemical"}, {"text": "cortical renal", "type": "AnatomicalStructure"}, {"text": "scintigraphy", "type": "HealthCareActivity"}, {"text": "2D projected images", "type": "IntellectualProduct"}, {"text": "3D images", "type": "IntellectualProduct"}]}

Example input:
Sentence: The relationship between the WARPS / STAID and the ISS scores , measured using a Pearson r correlation coefficient , demonstrated a strong relationship : r = -0 .

Example answer:
{"entities": [{"text": "ISS scores", "type": "IntellectualProduct"}]}

Example input:
Sentence: 003 ) in SRFs obtained with the two methods .

Example answer:
{"entities": [{"text": "methods", "type": "HealthCareActivity"}]}

Example input:
Sentence: The purpose of this study was to determine whether there is a significant difference between SRF values calculated with the 2D method and those calculated with the 3D method .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "SRF", "type": "Finding"}, {"text": "2D", "type": "SpatialConcept"}, {"text": "method", "type": "HealthCareActivity"}, {"text": "3D", "type": "SpatialConcept"}]}

Example input:
Sentence: An automated computational method was developed to estimate SRF using both 2D projection images and direct 3D images .

Example answer:
{"entities": [{"text": "automated computational method", "type": "HealthCareActivity"}, {"text": "SRF", "type": "Finding"}, {"text": "2D projection images", "type": "IntellectualProduct"}, {"text": "3D images", "type": "IntellectualProduct"}]}

Input:
Sentence: There was strong correlation between SRFs estimated with the 2D and 3D methods ( r = 0 .

## Item MedMentions:test:1027
Example input:
Sentence: There was no survival benefit with the addition of CADI - 05 to the combination of cisplatin - paclitaxel in patients with advanced NSCLC ; however , the squamous cell subset did demonstrate a survival advantage .

Example answer:
{"entities": [{"text": "CADI - 05", "type": "Chemical"}, {"text": "cisplatin - paclitaxel", "type": "HealthCareActivity"}, {"text": "NSCLC", "type": "BiologicFunction"}, {"text": "squamous cell subset", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Delicaflavone may represent a potential therapeutic agent for lung cancer .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "lung cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Delicaflavone may represent a potential therapeutic agent for lung cancer .

Example answer:
{"entities": [{"text": "Delicaflavone", "type": "Chemical"}, {"text": "lung cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: The antitumour activity on these models of doxorubicin , dacarbazine ( DTIC ) , ifosfamide ( monotherapy or combination ) , trabectedin and eribulin was tested .

Example answer:
{"entities": [{"text": "antitumour activity", "type": "Finding"}, {"text": "models", "type": "IntellectualProduct"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "dacarbazine", "type": "Chemical"}, {"text": "DTIC", "type": "Chemical"}, {"text": "ifosfamide", "type": "Chemical"}, {"text": "combination", "type": "HealthCareActivity"}, {"text": "trabectedin", "type": "Chemical"}, {"text": "eribulin", "type": "Chemical"}]}

Example input:
Sentence: Results showed that these compounds were highly cytotoxic , in particular on Human Promyelocytic Leukemia cells ( HL60 ) and Chronic Myelogenous Leukemia cells ( K562 ) when compared with conventional antineoplastic drugs such as etoposide and cisplatin .

Example answer:
{"entities": [{"text": "compounds", "type": "Chemical"}, {"text": "Human Promyelocytic Leukemia cells", "type": "AnatomicalStructure"}, {"text": "HL60", "type": "AnatomicalStructure"}, {"text": "Chronic Myelogenous Leukemia cells", "type": "AnatomicalStructure"}, {"text": "K562", "type": "AnatomicalStructure"}, {"text": "antineoplastic drugs", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Chemotherapy regimens included gemcitabine alone or in association with other agents ( 44 % ) , oxaliplatin , irinotecan , fluorouracil and leucovorin ( FOLFIRINOX 8 % ) , and cisplatin , gemcitabine plus capecitabine and epirubicin ( PEXG ) or capecitabine and docetaxel ( PDXG ) or epirubicin and fluorouracil ( PEFG ) ( 48 % ) .

Example answer:
{"entities": [{"text": "Chemotherapy regimens", "type": "HealthCareActivity"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "agents", "type": "Chemical"}, {"text": "oxaliplatin", "type": "Chemical"}, {"text": "irinotecan", "type": "Chemical"}, {"text": "fluorouracil", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "capecitabine", "type": "Chemical"}, {"text": "epirubicin", "type": "Chemical"}, {"text": "PEXG", "type": "HealthCareActivity"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "PDXG", "type": "HealthCareActivity"}, {"text": "PEFG", "type": "HealthCareActivity"}]}

Example input:
Sentence: From chemotherapy to target therapies associated with radiation in the treatment of NSCLC : a durable marriage ? The integration between radiotherapy and drugs , from chemotherapy to recently available target therapies , continues to have a relevant role in the treatment of locally advanced and metastatic Non - small cell lung cancer ( NSCLC ) .

Example answer:
{"entities": [{"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "therapies", "type": "HealthCareActivity"}, {"text": "NSCLC", "type": "BiologicFunction"}, {"text": "radiotherapy", "type": "IntellectualProduct"}, {"text": "drugs", "type": "HealthCareActivity"}, {"text": "Non - small cell lung cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: All lung cancer patients receiving one or more cytotoxic agents during the period 21 June 2010 till 2 December 2014 at OLVG were included .

Example answer:
{"entities": [{"text": "lung cancer", "type": "BiologicFunction"}, {"text": "cytotoxic agents", "type": "Chemical"}, {"text": "OLVG", "type": "SpatialConcept"}]}

Example input:
Sentence: The primary objective of this study is to determine the incidence and the clinical relevance of the drug - drug interactions between antineoplastic agents and regular medication used by lung cancer patients .

Example answer:
{"entities": [{"text": "drug - drug interactions", "type": "BiologicFunction"}, {"text": "antineoplastic agents", "type": "Chemical"}, {"text": "regular medication", "type": "Chemical"}, {"text": "lung cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: The most frequent interaction was between cytostatics and coumarins while the most relevant one was between cisplatin and furosemide .

Example answer:
{"entities": [{"text": "interaction", "type": "BiologicFunction"}, {"text": "cytostatics", "type": "Chemical"}, {"text": "coumarins", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "furosemide", "type": "Chemical"}]}

Input:
Sentence: Drug - drug interactions of cytostatics with regular medicines in lung cancer patients Lung cancer patients have a high risk for drug - drug interactions , as they use numerous types of concomitant medicines including antineoplastic agents , cancer treatment co - medication , and medicines aimed at several types of comorbidities .

## Item MedMentions:test:1446
Example input:
Sentence: The presence of three biominerals in the trichomes of the basally branching Eucnide urens indicates either an early evolution and subsequent loss or several independent origins of multiple biomineralization .

Example answer:
{"entities": [{"text": "presence", "type": "Finding"}, {"text": "biominerals", "type": "Chemical"}, {"text": "trichomes", "type": "AnatomicalStructure"}, {"text": "basally", "type": "SpatialConcept"}, {"text": "branching", "type": "SpatialConcept"}, {"text": "Eucnide urens", "type": "Eukaryote"}, {"text": "biomineralization", "type": "BiologicFunction"}]}

Example input:
Sentence: The most abundant OPE was tris - ( 2 - chloroethyl ) phosphate ( TCEP ) , with concentrations ranging from 30 to 227 pg / m3 , followed by three major OPEs , such as tris - ( 1 - chloro - 2 - propyl ) phosphate ( TCPP , 0 . 8 to 82 pg / m3 ) , tri - n - butyl phosphate ( TnBP , 2 to 19 pg / m3 ) and tri - iso - butyl phosphate ( TiBP , 0 . 3 to 14 pg / m3 ) .

Example answer:
{"entities": [{"text": "OPE", "type": "Chemical"}, {"text": "tris - ( 2 - chloroethyl ) phosphate", "type": "Chemical"}, {"text": "TCEP", "type": "Chemical"}, {"text": "OPEs", "type": "Chemical"}, {"text": "tris - ( 1 - chloro - 2 - propyl ) phosphate", "type": "Chemical"}, {"text": "TCPP", "type": "Chemical"}, {"text": "tri - n - butyl phosphate", "type": "Chemical"}, {"text": "TnBP", "type": "Chemical"}, {"text": "tri - iso - butyl phosphate", "type": "Chemical"}, {"text": "TiBP", "type": "Chemical"}]}

Example input:
Sentence: 8 in detecting taper corrosion -related pseudotumors on MARS - MRI was 88 % and 32 % and 70 % and 50 % , respectively .

Example answer:
{"entities": [{"text": "taper", "type": "MedicalDevice"}, {"text": "pseudotumors", "type": "AnatomicalStructure"}, {"text": "MARS - MRI", "type": "HealthCareActivity"}]}

Example input:
Sentence: The vast majority of the 31 species investigated had at least two different biominerals in their trichomes , and 22 had three different biominerals in their trichomes .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "biominerals", "type": "Chemical"}, {"text": "trichomes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We used standard microbiological cultures , as well as ATP bioluminescence technique to quantify bioburden as relative light units ( RLU ) .

Example answer:
{"entities": [{"text": "microbiological cultures", "type": "HealthCareActivity"}, {"text": "ATP", "type": "Chemical"}, {"text": "bioluminescence technique", "type": "HealthCareActivity"}]}

Example input:
Sentence: We found that use of extractant fluid enhanced detection of bioburden .

Example answer:
{"entities": [{"text": "detection", "type": "Finding"}]}

Example input:
Sentence: There is significant bioburden in reprocessed EUS needles ; standard microbiological cultures have low sensitivity for detection of needle contamination .

Example answer:
{"entities": [{"text": "microbiological cultures", "type": "HealthCareActivity"}, {"text": "sensitivity", "type": "HealthCareActivity"}, {"text": "detection", "type": "Finding"}]}

Example input:
Sentence: Larger ( 19 G ) needles had higher surface contamination ( P = 0 . 016 ) , but there was no relation of luminal contamination with needle diameter ( P = 0 . 138 ) .

Example answer:
{"entities": [{"text": "needles", "type": "MedicalDevice"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "no relation", "type": "Finding"}, {"text": "luminal", "type": "SpatialConcept"}, {"text": "needle", "type": "MedicalDevice"}]}

Example input:
Sentence: There was significant correlation between the surface and intraluminal bioburden ( P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "surface", "type": "SpatialConcept"}, {"text": "intraluminal", "type": "SpatialConcept"}]}

Example input:
Sentence: We found culture positivity in 3 / 34 ( 8 . 8 % ) , and detectable bioburden on the exposed surface of 33 / 35 ( 94 .

Example answer:
{"entities": [{"text": "culture positivity", "type": "Finding"}, {"text": "detectable", "type": "ClinicalAttribute"}, {"text": "surface", "type": "SpatialConcept"}]}

Input:
Sentence: Significant bioburden was found in three ( 8 . 6 % ) and two ( 5 . 7 % ) needles on the surface and lumen , respectively .

## Item MedMentions:test:1440
Example input:
Sentence: A structured search of bibliographic databases ( eg , MEDLINE , EMBASE , PubMed , CINAHL , Cochrane CENTRAL ) has been undertaken to retrieve randomised controlled trials and cohort studies that describe the use of TxA in paediatric trauma patients .

Example answer:
{"entities": [{"text": "bibliographic databases", "type": "IntellectualProduct"}, {"text": "MEDLINE", "type": "IntellectualProduct"}, {"text": "EMBASE", "type": "IntellectualProduct"}, {"text": "PubMed", "type": "IntellectualProduct"}, {"text": "CINAHL", "type": "IntellectualProduct"}, {"text": "Cochrane CENTRAL", "type": "IntellectualProduct"}, {"text": "randomised controlled trials", "type": "ResearchActivity"}, {"text": "TxA", "type": "Chemical"}, {"text": "paediatric trauma", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Studies reporting reintervention after endovascular repair were identified by searching PubMed and Embase in accordance with preferred reporting items for systematic reviews and meta - analyses guidelines , and by reviewing the reference lists of retrieved articles .

Example answer:
{"entities": [{"text": "reintervention", "type": "HealthCareActivity"}, {"text": "PubMed", "type": "IntellectualProduct"}, {"text": "Embase", "type": "IntellectualProduct"}, {"text": "systematic reviews", "type": "IntellectualProduct"}, {"text": "meta - analyses", "type": "ResearchActivity"}, {"text": "guidelines", "type": "IntellectualProduct"}, {"text": "retrieved articles", "type": "IntellectualProduct"}]}

Example input:
Sentence: This is a retrospective analysis of transfemoral TAVI patients included in a prospective institutional database .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "TAVI", "type": "HealthCareActivity"}, {"text": "prospective institutional database", "type": "IntellectualProduct"}]}

Example input:
Sentence: Only 1 subgroup , transapical TAVI , was not significantly associated with stroke - related mortality ( OR 1 . 97 , 95 % confidence interval , 0 . 43 to 7 . 43 , p = 0 .

Example answer:
{"entities": [{"text": "subgroup", "type": "IntellectualProduct"}, {"text": "transapical TAVI", "type": "HealthCareActivity"}, {"text": "stroke", "type": "BiologicFunction"}]}

Example input:
Sentence: Transapical TAVI is not associated with increased stroke - related mortality in patients who suffer from perioperative stroke .

Example answer:
{"entities": [{"text": "Transapical TAVI", "type": "HealthCareActivity"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "suffer", "type": "BiologicFunction"}]}

Example input:
Sentence: Meta - Analysis of Perioperative Stroke and Mortality in Transcatheter Aortic Valve Implantation Transcatheter aortic valve implantation ( TAVI ) is a rapidly evolving safe method with decreasing incidence of perioperative stroke .

Example answer:
{"entities": [{"text": "Meta - Analysis", "type": "ResearchActivity"}, {"text": "Stroke", "type": "BiologicFunction"}, {"text": "Transcatheter Aortic Valve Implantation", "type": "HealthCareActivity"}, {"text": "Transcatheter aortic valve implantation", "type": "HealthCareActivity"}, {"text": "TAVI", "type": "HealthCareActivity"}, {"text": "decreasing", "type": "Finding"}, {"text": "stroke", "type": "BiologicFunction"}]}

Example input:
Sentence: The primary aim of this meta - analysis was to determine whether perioperative stroke increases risk of stroke - related mortality after TAVI .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "TAVI", "type": "HealthCareActivity"}]}

Example input:
Sentence: In conclusion , perioperative strokes after TAVI are associated with > 6 times greater risk of 30 - day stroke - related mortality .

Example answer:
{"entities": [{"text": "strokes", "type": "BiologicFunction"}, {"text": "TAVI", "type": "HealthCareActivity"}, {"text": "risk", "type": "Finding"}, {"text": "stroke", "type": "BiologicFunction"}]}

Example input:
Sentence: Summary OR of stroke - related mortality after TAVI was estimated to be 6 . 45 ( 95 % confidence interval 3 . 90 to 10 . 66 , p < 0 .

Example answer:
{"entities": [{"text": "Summary", "type": "IntellectualProduct"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "TAVI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Data were extracted from the finalized studies and analyzed to generate a summary odds ratio ( OR ) of stroke - related mortality after TAVI .

Example answer:
{"entities": [{"text": "extracted", "type": "ResearchActivity"}, {"text": "summary", "type": "IntellectualProduct"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "TAVI", "type": "HealthCareActivity"}]}

Input:
Sentence: Online databases , using relevant keywords , and additional related records were searched to retrieve articles involving TAVI and stroke after TAVI .

## Item MedMentions:test:1438
Example input:
Sentence: Levels of copeptin and plasma N - terminal probrain natriuretic peptide ( NT - proBNP ) were evaluated prospectively in 24 obstructive HCM patients , 36 nonobstructive HCM patients , and 36 age - and sex - matched control subjects .

Example answer:
{"entities": [{"text": "copeptin", "type": "Chemical"}, {"text": "HCM", "type": "BiologicFunction"}]}

Example input:
Sentence: Copeptin and NT - proBNP levels were significantly higher in patients with obstructive HCM , and higher levels were associated with worse outcome .

Example answer:
{"entities": [{"text": "Copeptin", "type": "Chemical"}, {"text": "HCM", "type": "BiologicFunction"}]}

Example input:
Sentence: Copeptin and NT - proBNP levels were higher in the obstructive HCM subgroup compared with the nonobstructive HCM subgroup ( 18 . 3 vs 13 .

Example answer:
{"entities": [{"text": "Copeptin", "type": "Chemical"}, {"text": "HCM", "type": "BiologicFunction"}, {"text": "subgroup", "type": "IntellectualProduct"}]}

Example input:
Sentence: Short - Term Influence of Radiofrequency Ablation on NT - proBNP , MR - proANP , Copeptin , and MR - proADM in Patients With Atrial Fibrillation : Data From the Observational SMURF Study There is limited knowledge on the short - term influence of radiofrequency ablation ( RFA ) of atrial fibrillation ( AF ) on 2 cardiac biomarkers ; the N - terminal pro - B - type natriuretic peptide ( NT - proBNP ) and the midregional fragment of the N - terminal of pro - ANP ( MR - proANP ) and 2 extracardiac biomarkers ; the c - terminal provasopressin ( copeptin ) and the midregional portion of proadrenomedullin ( MR - proADM ) .

Example answer:
{"entities": [{"text": "Radiofrequency Ablation", "type": "HealthCareActivity"}, {"text": "NT - proBNP", "type": "Chemical"}, {"text": "MR - proANP", "type": "Chemical"}, {"text": "Copeptin", "type": "Chemical"}, {"text": "MR - proADM", "type": "Chemical"}, {"text": "Atrial Fibrillation", "type": "BiologicFunction"}, {"text": "Observational SMURF Study", "type": "ResearchActivity"}, {"text": "radiofrequency ablation", "type": "HealthCareActivity"}, {"text": "RFA", "type": "HealthCareActivity"}, {"text": "atrial fibrillation", "type": "BiologicFunction"}, {"text": "AF", "type": "BiologicFunction"}, {"text": "cardiac biomarkers", "type": "ClinicalAttribute"}, {"text": "N - terminal pro - B - type natriuretic peptide", "type": "Chemical"}, {"text": "midregional fragment of the N - terminal of pro - ANP", "type": "Chemical"}, {"text": "extracardiac biomarkers", "type": "ClinicalAttribute"}, {"text": "c - terminal provasopressin", "type": "Chemical"}, {"text": "copeptin", "type": "Chemical"}, {"text": "midregional portion of proadrenomedullin", "type": "Chemical"}]}

Example input:
Sentence: Copeptin and NT - proBNP levels were higher in the HCM group compared with controls ( 14 . 1 vs 8 . 4 pmol / L , P < 0 . 01 ; and 383 vs 44 pg / mL , P < 0 . 01 , respectively ) .

Example answer:
{"entities": [{"text": "Copeptin", "type": "Chemical"}, {"text": "HCM", "type": "BiologicFunction"}]}

Example input:
Sentence: The level of NT - proBNP decreased the day after RFA in participants in AF at the time of RFA , compared to the participants in sinus rhythm who showed a slight increase ( P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "NT - proBNP", "type": "Chemical"}, {"text": "RFA", "type": "HealthCareActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "AF", "type": "BiologicFunction"}, {"text": "sinus rhythm", "type": "Finding"}]}

Example input:
Sentence: Furthermore , regardless of the actual rhythm , the level of MR - proANP showed an increase immediately after RFA ( P < 0 .

Example answer:
{"entities": [{"text": "actual rhythm", "type": "BiologicFunction"}, {"text": "MR - proANP", "type": "Chemical"}, {"text": "RFA", "type": "HealthCareActivity"}]}

Example input:
Sentence: We found no sign of a cardiac release of MR - proADM or copeptin .

Example answer:
{"entities": [{"text": "no sign", "type": "Finding"}, {"text": "cardiac", "type": "AnatomicalStructure"}, {"text": "MR - proADM", "type": "Chemical"}, {"text": "copeptin", "type": "Chemical"}]}

Example input:
Sentence: Levels of copeptin and MR - proADM were not higher in the CS compared to peripheral blood .

Example answer:
{"entities": [{"text": "copeptin", "type": "Chemical"}, {"text": "MR - proADM", "type": "Chemical"}, {"text": "CS", "type": "AnatomicalStructure"}, {"text": "peripheral blood", "type": "BodySubstance"}]}

Example input:
Sentence: NT - proBNP , MR - proANP , copeptin , and MR - proADM levels were measured in peripheral blood , the coronary sinus ( CS ) , and the left atrium before ablation , and in peripheral blood immediately and the day after RFA .

Example answer:
{"entities": [{"text": "NT - proBNP", "type": "Chemical"}, {"text": "MR - proANP", "type": "Chemical"}, {"text": "copeptin", "type": "Chemical"}, {"text": "MR - proADM", "type": "Chemical"}, {"text": "peripheral blood", "type": "BodySubstance"}, {"text": "coronary sinus", "type": "AnatomicalStructure"}, {"text": "CS", "type": "AnatomicalStructure"}, {"text": "left atrium", "type": "AnatomicalStructure"}, {"text": "ablation", "type": "HealthCareActivity"}, {"text": "RFA", "type": "HealthCareActivity"}]}

Input:
Sentence: Copeptin level showed a 6 - fold increase immediately after RFA compared to baseline ( P < 0 . 001 ) , whereas MR - proADM level increased the day after RFA ( P < 0 .

## Item MedMentions:test:1510
Example input:
Sentence: Over the same time period , the percentage of female plastic surgery residents increased from 2 . 6 percent to 32 . 5 percent .

Example answer:
{"entities": [{"text": "plastic surgery", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: A total of 50 donor / recipient evaluations were conducted ; half of them had at least one C1q + Ab ( n = 26 , 52 % ) .

Example answer:
{"entities": [{"text": "donor", "type": "PopulationGroup"}, {"text": "recipient", "type": "PopulationGroup"}, {"text": "evaluations", "type": "HealthCareActivity"}, {"text": "C1q + Ab", "type": "Chemical"}]}

Example input:
Sentence: There was one surgical conversion ( 4 % ; 1 / 25 ) due to bleeding from a femoral anastomosis .

Example answer:
{"entities": [{"text": "surgical conversion", "type": "HealthCareActivity"}, {"text": "bleeding", "type": "BiologicFunction"}]}

Example input:
Sentence: From 2008 through 2011 , the four years prior to the organization beginning its change journey , LifeShare recovered 344 organ donors from which 1 , 007 organs were transplanted in 48 months .

Example answer:
{"entities": [{"text": "organization", "type": "Organization"}, {"text": "LifeShare", "type": "HealthCareActivity"}, {"text": "organ donors", "type": "PopulationGroup"}, {"text": "organs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Complete healing was significant in patients treated with major surgery ( 80 % ) compared to the non - operative group ( 20 % ; p < 0 . 035 ) .

Example answer:
{"entities": [{"text": "healing", "type": "BiologicFunction"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "non - operative", "type": "HealthCareActivity"}]}

Example input:
Sentence: surgical resection was carried out in 11 patients ( 8 . 5 % ) .

Example answer:
{"entities": [{"text": "surgical resection", "type": "HealthCareActivity"}]}

Example input:
Sentence: The rate of conversion to open surgery was 35 % ; if minilaparotomies are excluded , the conversion rate was only 16 % .

Example answer:
{"entities": [{"text": "open surgery", "type": "HealthCareActivity"}, {"text": "minilaparotomies", "type": "HealthCareActivity"}]}

Example input:
Sentence: Therefore , we concluded that the divided and sliding STA flap could at least partially solve the donor - site problem .

Example answer:
{"entities": [{"text": "STA", "type": "AnatomicalStructure"}, {"text": "flap", "type": "AnatomicalStructure"}, {"text": "donor - site", "type": "SpatialConcept"}, {"text": "problem", "type": "Finding"}]}

Example input:
Sentence: During the first 48 months of the change journey ( 2012 through 2015 ) , 498 organ donors ( +44 . 8 % ) provided 1 , 536 organs transplanted ( +52 . 5 % ) .

Example answer:
{"entities": [{"text": "organ donors", "type": "PopulationGroup"}, {"text": "organs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: No living donor mortality was reported ; 29 patients ( 29 % ) experienced at least one complication .

Example answer:
{"entities": [{"text": "No", "type": "Finding"}, {"text": "living donor", "type": "PopulationGroup"}, {"text": "complication", "type": "BiologicFunction"}]}

Input:
Sentence: 3 % of potential living donors underwent surgery .

## Item MedMentions:test:1396
Example input:
Sentence: ZrO2 nanotubular arrays with diameters of 70 - 120 nm were obtained .

Example answer:
{"entities": [{"text": "ZrO2", "type": "Chemical"}, {"text": "arrays", "type": "SpatialConcept"}]}

Example input:
Sentence: Silver nanoparticles were prepared from the reduction of silver nitrate and NaBH4 was used as reducing agent .

Example answer:
{"entities": [{"text": "Silver", "type": "Chemical"}, {"text": "silver nitrate", "type": "Chemical"}, {"text": "NaBH4", "type": "Chemical"}, {"text": "reducing agent", "type": "Chemical"}]}

Example input:
Sentence: Here , we developed a novel method to fabricate GelMA / nanohydroxylapatite ( nHA ) microgel arrays using a photocrosslinkable strategy .

Example answer:
{"entities": [{"text": "GelMA", "type": "Chemical"}, {"text": "nanohydroxylapatite", "type": "Chemical"}, {"text": "nHA", "type": "Chemical"}, {"text": "microgel", "type": "Chemical"}, {"text": "arrays", "type": "SpatialConcept"}]}

Example input:
Sentence: Titanium dioxide and Zinc Oxide nanoparticle were synthesized by wet chemical process .

Example answer:
{"entities": [{"text": "Titanium dioxide", "type": "Chemical"}, {"text": "Zinc Oxide", "type": "Chemical"}]}

Example input:
Sentence: Atomic force microscopy was employed to determine the zirconia surface morphology and the adhesion forces between the S .

Example answer:
{"entities": [{"text": "Atomic force microscopy", "type": "HealthCareActivity"}, {"text": "zirconia", "type": "Chemical"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: Ultrathin Au nanowires assisted magnetic graphene - silica ZIC - HILIC composites for highly specific enrichment of N - linked glycopeptides Protein glycosylation has been proven to participate in a variety of complex biological processes ; however , the low abundance of glycopeptides in natural samples makes it essential to develop methods to isolate and enrich glycopeptides .

Example answer:
{"entities": [{"text": "Au", "type": "Chemical"}, {"text": "magnetic graphene", "type": "Chemical"}, {"text": "silica", "type": "Chemical"}, {"text": "N - linked glycopeptides", "type": "Chemical"}, {"text": "Protein glycosylation", "type": "BiologicFunction"}, {"text": "complex biological processes", "type": "BiologicFunction"}, {"text": "glycopeptides", "type": "Chemical"}]}

Example input:
Sentence: Second , an anodic oxidation was applied to fabricate zirconia nanotubular arrays .

Example answer:
{"entities": [{"text": "anodic oxidation", "type": "BiologicFunction"}, {"text": "zirconia", "type": "Chemical"}, {"text": "arrays", "type": "SpatialConcept"}]}

Example input:
Sentence: Finally , heat treatment was used at different annealing temperatures in order to change the structure and morphology from nanotubes to nanowires and subsequently to nanoneedles in the presence of argon gas .

Example answer:
{"entities": [{"text": "structure", "type": "SpatialConcept"}, {"text": "argon", "type": "Chemical"}, {"text": "gas", "type": "Chemical"}]}

Example input:
Sentence: First , a physical vapor deposition magnetron sputtering technique was used to deposit pure zirconium nanograins on top of a substrate .

Example answer:
{"entities": [{"text": "physical vapor deposition", "type": "IntellectualProduct"}, {"text": "zirconium", "type": "Chemical"}]}

Example input:
Sentence: The size of the pure zirconium nanograins was estimated to be approximately 200 - 300 nm .

Example answer:
{"entities": [{"text": "size", "type": "SpatialConcept"}, {"text": "zirconium", "type": "Chemical"}]}

Input:
Sentence: From Zirconium Nanograins to Zirconia Nanoneedles Combinations of three simple techniques were utilized to gradually form zirconia nanoneedles from zirconium nanograins .

## Item MedMentions:test:1632
Example input:
Sentence: 93±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 93±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 95±1 .

Example answer:
{"entities": []}

Example input:
Sentence: 52±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 55 and 1 .

Example answer:
{"entities": []}

Example input:
Sentence: 19 , 1 . 97±0 . 25 , and 1 . 67±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 40 ; REC 0 . 99±0 . 54 ; CAL 3 . 00±0 . 58 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 38±0 . 02 and 1 . 95±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 98 , 1 . 45 - 54 . 19 and 2 . 00 - 50 .

Example answer:
{"entities": []}

Example input:
Sentence: 97 to 1 . 8±1 .

Example answer:
{"entities": []}

Input:
Sentence: 53 ; REC 1 . 95±0 .
