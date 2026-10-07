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

## Item MedMentions:test:263
Example input:
Sentence: Consistent with this : ( 1 ) FFA and LO responded more strongly to nonfreckled ( smooth ) faces , compared with otherwise identical freckled ( textured ) faces ; and ( 2 ) strong functional connections were found between LO and FFA .

Example answer:
{"entities": [{"text": "FFA", "type": "BodySystem"}, {"text": "LO", "type": "AnatomicalStructure"}, {"text": "faces", "type": "SpatialConcept"}, {"text": "freckled", "type": "Finding"}, {"text": "connections", "type": "SpatialConcept"}]}

Example input:
Sentence: The steric repulsion generated from the long POEGMA brush layer in the swollen state was long - range and strong so that the protein adsorption is very unlikely .

Example answer:
{"entities": [{"text": "POEGMA brush", "type": "Chemical"}, {"text": "swollen state", "type": "Finding"}, {"text": "protein", "type": "Chemical"}, {"text": "adsorption", "type": "HealthCareActivity"}]}

Example input:
Sentence: One remarkable , yet unresolved , feature of SMA is that not all motor neurons are equally affected , with some populations displaying a robust resistance to the disease .

Example answer:
{"entities": [{"text": "SMA", "type": "BiologicFunction"}, {"text": "motor neurons", "type": "AnatomicalStructure"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "resistance to the disease", "type": "BiologicFunction"}]}

Example input:
Sentence: In addition to slow and fast oscillations arising from excitatory and inhibitory networks , respectively , we show that the interaction between these two networks generates phase - amplitude cross - frequency coupling ( CFC ) , in which multiple different frequency components coexist and the amplitude of the fast oscillation is modulated by the phase of the slow oscillation .

Example answer:
{"entities": [{"text": "oscillations", "type": "BiologicFunction"}, {"text": "excitatory", "type": "BiologicFunction"}, {"text": "inhibitory", "type": "BiologicFunction"}, {"text": "networks", "type": "AnatomicalStructure"}, {"text": "phase - amplitude cross - frequency coupling", "type": "BiologicFunction"}, {"text": "CFC", "type": "BiologicFunction"}, {"text": "amplitude", "type": "SpatialConcept"}, {"text": "oscillation", "type": "BiologicFunction"}, {"text": "modulated", "type": "SpatialConcept"}]}

Example input:
Sentence: Our findings are consistent with the idea that diffuse co - evolution drives the evolution of extremely long proboscises and flower tubes , and highlight the importance of morphological traits , beyond the forbidden links hypothesis , in structuring interactions between mutualistic partners , revealing that the role of niche - based processes can be much more complex than previously known .

Example answer:
{"entities": [{"text": "co - evolution", "type": "BiologicFunction"}, {"text": "evolution", "type": "BiologicFunction"}, {"text": "long proboscises", "type": "Eukaryote"}, {"text": "flower tubes", "type": "Eukaryote"}, {"text": "morphological", "type": "SpatialConcept"}]}

Example input:
Sentence: Cross - validation analyses on an independent sample exhibited high correlations with observed SB ( r = 0 . 72 ) and MVPA ( r = 0 . 75 ) .

Example answer:
{"entities": [{"text": "Cross - validation", "type": "ResearchActivity"}]}

Example input:
Sentence: Bifurcation Analysis on Phase - Amplitude Cross - Frequency Coupling in Neural Networks with Dynamic Synapses We investigate a discrete - time network model composed of excitatory and inhibitory neurons and dynamic synapses with the aim at revealing dynamical properties behind oscillatory phenomena possibly related to brain functions .

Example answer:
{"entities": [{"text": "Bifurcation", "type": "SpatialConcept"}, {"text": "Analysis", "type": "ResearchActivity"}, {"text": "Phase - Amplitude Cross - Frequency Coupling", "type": "BiologicFunction"}, {"text": "Neural Networks", "type": "AnatomicalStructure"}, {"text": "Synapses", "type": "SpatialConcept"}, {"text": "network model", "type": "IntellectualProduct"}, {"text": "excitatory", "type": "BiologicFunction"}, {"text": "inhibitory", "type": "BiologicFunction"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "synapses", "type": "SpatialConcept"}, {"text": "oscillatory phenomena", "type": "BiologicFunction"}]}

Example input:
Sentence: Bispectral pairwise interacting source analysis for identifying systems of cross - frequency interacting brain sources from electroencephalographic or magnetoencephalographic signals Brain cognitive functions arise through the coordinated activity of several brain regions , which actually form complex dynamical systems operating at multiple frequencies .

Example answer:
{"entities": [{"text": "Bispectral pairwise interacting source analysis", "type": "ResearchActivity"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "sources", "type": "Finding"}, {"text": "electroencephalographic", "type": "HealthCareActivity"}, {"text": "magnetoencephalographic", "type": "HealthCareActivity"}, {"text": "Brain", "type": "AnatomicalStructure"}, {"text": "cognitive functions", "type": "BiologicFunction"}, {"text": "coordinated activity", "type": "BiologicFunction"}, {"text": "brain regions", "type": "SpatialConcept"}]}

Example input:
Sentence: Simulations show that the performances of biPISA in estimating the phase difference between the interacting sources are affected by the increasing level of noise rather than by the number of the interacting subsystems .

Example answer:
{"entities": [{"text": "Simulations", "type": "ResearchActivity"}, {"text": "biPISA", "type": "ResearchActivity"}, {"text": "sources", "type": "Finding"}]}

Example input:
Sentence: Specifically , the biPISA makes it possible to identify one or many subsystems of cross - frequency interacting sources by decomposing the antisymmetric components of the cross - bispectra between EEG or MEG signals , based on the assumption that interactions are pairwise .

Example answer:
{"entities": [{"text": "biPISA", "type": "ResearchActivity"}, {"text": "sources", "type": "Finding"}, {"text": "cross - bispectra", "type": "ResearchActivity"}, {"text": "EEG", "type": "HealthCareActivity"}, {"text": "MEG", "type": "HealthCareActivity"}]}

Input:
Sentence: Thanks to the properties of the antisymmetric components of the cross - bispectra , biPISA is also robust to spurious interactions arising from mixing artifacts , i .

## Item MedMentions:test:544
Example input:
Sentence: Al was the most abundant TE with a VWM concentration and wet flux of 33 . 8 μg L ( - 1 ) and 29 . 2 mg m ( - 2 ) yr ( - 1 ) , which were 2 and 3 orders of magnitude higher than those of Co , respectively .

Example answer:
{"entities": [{"text": "Al", "type": "Chemical"}, {"text": "TE", "type": "Chemical"}, {"text": "Co", "type": "Chemical"}]}

Example input:
Sentence: Predictions were the poorest for aquifers where the salt water wedge was expected to extend further inland under predevelopment conditions and was therefore more dispersive prior to pumping .

Example answer:
{"entities": [{"text": "salt water", "type": "Chemical"}, {"text": "wedge", "type": "SpatialConcept"}, {"text": "inland", "type": "SpatialConcept"}]}

Example input:
Sentence: Soils sampled in slope and plane revealed similar characteristics , with the exception of organic matter content and penetrometer resistance , both higher in slope .

Example answer:
{"entities": []}

Example input:
Sentence: Although organic - rich anaerobic sedimentary habitats in the ocean margins harbor large numbers of microbial cells , microbial populations in ultraoligotrophic aerobic sedimentary habitats in the open ocean gyres are several orders of magnitude less abundant .

Example answer:
{"entities": [{"text": "organic - rich anaerobic sedimentary habitats", "type": "SpatialConcept"}, {"text": "ultraoligotrophic aerobic sedimentary habitats", "type": "SpatialConcept"}]}

Example input:
Sentence: The results show that water , suspended particles , and sediments were significant ly contaminated by various TMs ( As , Cd , Cu , Ni , Pb , and Zn ) .

Example answer:
{"entities": [{"text": "water", "type": "Chemical"}, {"text": "particles", "type": "Chemical"}, {"text": "TMs", "type": "Chemical"}, {"text": "As", "type": "Chemical"}, {"text": "Cd", "type": "Chemical"}, {"text": "Cu", "type": "Chemical"}, {"text": "Ni", "type": "Chemical"}, {"text": "Pb", "type": "Chemical"}, {"text": "Zn", "type": "Chemical"}]}

Example input:
Sentence: ( 3 ) The congener profiles , ∑ PCDD / Fs and TEQ between background atmosphere and surrounding atmosphere of landfill did not show statistically significant difference .

Example answer:
{"entities": [{"text": "congener profiles", "type": "HealthCareActivity"}, {"text": "PCDD", "type": "Chemical"}, {"text": "Fs", "type": "Chemical"}, {"text": "landfill", "type": "SpatialConcept"}]}

Example input:
Sentence: Mixed - layer growth rates of Prochlorococcus and Synechococcus were largely balanced by mortality , whereas eukaryotic phytoplankton showed positive net growth ( ∼0 .

Example answer:
{"entities": [{"text": "Mixed - layer", "type": "SpatialConcept"}, {"text": "Prochlorococcus", "type": "Bacterium"}, {"text": "Synechococcus", "type": "Bacterium"}, {"text": "eukaryotic phytoplankton", "type": "Eukaryote"}, {"text": "positive", "type": "Finding"}, {"text": "net growth", "type": "BiologicFunction"}]}

Example input:
Sentence: The authors used an equilibrium partitioning ( EqP ) approach to generate predicted PCB sediment effect concentrations ( largely Aroclor 1254 ) associated with a gradient of toxic effects in benthic organisms from effects observed in aquatic toxicity studies .

Example answer:
{"entities": [{"text": "equilibrium partitioning ( EqP ) approach", "type": "IntellectualProduct"}, {"text": "PCB", "type": "Chemical"}, {"text": "Aroclor 1254", "type": "Chemical"}, {"text": "toxic effects", "type": "InjuryOrPoisoning"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "studies", "type": "ResearchActivity"}]}

Example input:
Sentence: The present study differs from all other EqP collective sediment investigations in that the authors examined a common dose - response gradient of effects for PCBs rather than a single , protective value .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "EqP", "type": "IntellectualProduct"}, {"text": "PCBs", "type": "Chemical"}]}

Example input:
Sentence: In this study , we consistently observed in seawater microcosms of 3 different conditions that culturable E .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "culturable", "type": "HealthCareActivity"}, {"text": "E .", "type": "Bacterium"}]}

Input:
Sentence: Similar results were observed across four estuarine sediment types , despite their different physical - chemical characteristics .

## Item MedMentions:test:491
Example input:
Sentence: All isolates were tested for their inhibitory activities on the mRNA expression of PCSK9 .

Example answer:
{"entities": [{"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "PCSK9", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Compound 1 was screened for its antibacterial , antifungal and antioxidant potential .

Example answer:
{"entities": [{"text": "Compound", "type": "Chemical"}]}

Example input:
Sentence: casei exhibited the antifungal activity against blastoconidia and biofilm of C .

Example answer:
{"entities": [{"text": "casei", "type": "Bacterium"}, {"text": "antifungal activity", "type": "Finding"}, {"text": "blastoconidia", "type": "Eukaryote"}, {"text": "biofilm", "type": "Bacterium"}, {"text": "C .", "type": "Eukaryote"}]}

Example input:
Sentence: Monosubstituted Benzene Derivatives from Fruits of Ficus hirta and Their Antifungal Activity against Phytopathogen Penicillium italicum Ficus hirta , a widely consumed food by Hakka people , has been reported to show potent antifungal activity against phytopathogen Penicillium italicum .

Example answer:
{"entities": [{"text": "Monosubstituted Benzene Derivatives", "type": "Chemical"}, {"text": "Fruits", "type": "Food"}, {"text": "Ficus hirta", "type": "Eukaryote"}, {"text": "Antifungal Activity", "type": "Finding"}, {"text": "Penicillium italicum", "type": "Eukaryote"}, {"text": "food", "type": "Food"}, {"text": "people", "type": "PopulationGroup"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "antifungal activity", "type": "Finding"}]}

Example input:
Sentence: Compounds 2 and 4 - 7 showed mild antibacterial activity against human pathogen Staphylococcus aureus and fish pathogens Streptococcus iniae and Vibrio ichthyoenteri , and compounds 4 and 7 weakly suppressed NO production .

Example answer:
{"entities": [{"text": "Compounds 2 and 4 - 7", "type": "Chemical"}, {"text": "antibacterial activity", "type": "Finding"}, {"text": "human", "type": "Eukaryote"}, {"text": "Staphylococcus aureus", "type": "Bacterium"}, {"text": "fish", "type": "Eukaryote"}, {"text": "Streptococcus iniae", "type": "Bacterium"}, {"text": "Vibrio ichthyoenteri", "type": "Bacterium"}, {"text": "compounds 4 and 7", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}]}

Example input:
Sentence: casei showed the antifungal activity against Candida biofilm , and the biofilm of L .

Example answer:
{"entities": [{"text": "casei", "type": "Bacterium"}, {"text": "antifungal activity", "type": "Finding"}, {"text": "Candida", "type": "Eukaryote"}, {"text": "biofilm", "type": "Bacterium"}, {"text": "L .", "type": "Bacterium"}]}

Example input:
Sentence: The results showed that among aqueous , 70 % ethanols , acetic ether , chloroform , petroleum ether and essential oil extracts from the shoots and leaves , the essential oil showed the best in vitro acaricidal activity against adult P .

Example answer:
{"entities": [{"text": "ethanols", "type": "Chemical"}, {"text": "acetic ether", "type": "Chemical"}, {"text": "chloroform", "type": "Chemical"}, {"text": "petroleum ether", "type": "Chemical"}, {"text": "essential oil", "type": "Chemical"}, {"text": "shoots", "type": "Eukaryote"}, {"text": "leaves", "type": "Eukaryote"}, {"text": "acaricidal", "type": "Chemical"}, {"text": "P .", "type": "Eukaryote"}]}

Example input:
Sentence: Antibacterial and antifungal activities of the compound were tested against different bacterial and fungal strains , employing the agar well diffusion methods .

Example answer:
{"entities": [{"text": "Antibacterial", "type": "Finding"}, {"text": "antifungal activities", "type": "Finding"}, {"text": "compound", "type": "Chemical"}, {"text": "bacterial", "type": "Bacterium"}, {"text": "fungal strains", "type": "Eukaryote"}, {"text": "agar well diffusion methods", "type": "HealthCareActivity"}]}

Example input:
Sentence: 0 % inhibition , while the antifungal activity of the compound was the highest against Candida glabrata with 80 .

Example answer:
{"entities": [{"text": "inhibition", "type": "BiologicFunction"}, {"text": "antifungal activity", "type": "Finding"}, {"text": "compound", "type": "Chemical"}, {"text": "Candida glabrata", "type": "Eukaryote"}]}

Example input:
Sentence: multiplinervium showed no significant antifungal activity ( MIC > 250 µg / mL ) against several yeasts and filamentous fungal strains .

Example answer:
{"entities": [{"text": "multiplinervium", "type": "Eukaryote"}, {"text": "antifungal activity", "type": "BiologicFunction"}, {"text": "yeasts", "type": "Eukaryote"}, {"text": "filamentous fungal strains", "type": "Eukaryote"}]}

Input:
Sentence: All of the isolates were evaluated for antifungal activities against P .

## Item MedMentions:test:220
Example input:
Sentence: Methylchloroisothiazolinone / MI 0 . 02 % aq . ( dose , 6 μg / cm ) diagnoses significantly more contact allergy than 0 . 01 % ( dose , 3 μg / cm ) , without resulting in more adverse reactions .

Example answer:
{"entities": [{"text": "Methylchloroisothiazolinone / MI", "type": "Chemical"}, {"text": "diagnoses", "type": "Finding"}, {"text": "contact allergy", "type": "BiologicFunction"}, {"text": "adverse reactions", "type": "BiologicFunction"}]}

Example input:
Sentence: For the 50 - 60 % peak gas levels , individuals showed statistically significant reductions in responsiveness compared to rest , and across the group CS and CCS increased by 39 and 42 % , respectively , while CCSd was found to decrease by 398 % .

Example answer:
{"entities": [{"text": "individuals", "type": "PopulationGroup"}, {"text": "reductions", "type": "HealthCareActivity"}, {"text": "group", "type": "PopulationGroup"}, {"text": "CS", "type": "IntellectualProduct"}, {"text": "CCS", "type": "IntellectualProduct"}, {"text": "CCSd", "type": "IntellectualProduct"}]}

Example input:
Sentence: Sulforaphane administered for four weeks at doses of 25 μmoles and 150 μmoles to patients with COPD did not stimulate the expression of Nrf2 target genes or have an effect on levels of other anti - oxidants or markers of inflammation .

Example answer:
{"entities": [{"text": "Sulforaphane", "type": "Chemical"}, {"text": "administered", "type": "HealthCareActivity"}, {"text": "COPD", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Nrf2", "type": "Chemical"}, {"text": "target genes", "type": "AnatomicalStructure"}, {"text": "anti - oxidants", "type": "Chemical"}, {"text": "markers", "type": "ClinicalAttribute"}, {"text": "inflammation", "type": "BiologicFunction"}]}

Example input:
Sentence: Mean PDC for all oral and inhaled controller therapy was also higher in the SA cohort compared with the PA cohort ( 0 . 80 vs .

Example answer:
{"entities": [{"text": "oral", "type": "Chemical"}, {"text": "inhaled", "type": "BiologicFunction"}, {"text": "controller therapy", "type": "HealthCareActivity"}, {"text": "SA", "type": "Finding"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "PA", "type": "BiologicFunction"}]}

Example input:
Sentence: Moreover , only three times of μEPIT over two weeks could sufficiently inhibit allergen - specific IgE responses in mice suffering OVA -induced airway hyperresponsivness ( AHR ) , which was unattainable by eight times of SCIT over three weeks .

Example answer:
{"entities": [{"text": "μEPIT", "type": "HealthCareActivity"}, {"text": "allergen - specific IgE", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "OVA", "type": "Chemical"}, {"text": "airway hyperresponsivness", "type": "BiologicFunction"}, {"text": "AHR", "type": "BiologicFunction"}, {"text": "SCIT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients who met GOLD criteria for COPD and were able to tolerate bronchoscopies were randomly assigned ( 1 : 1 : 1 ) to receive placebo , 25 μmoles , or 150 μmoles sulforaphane daily by mouth for four weeks .

Example answer:
{"entities": [{"text": "COPD", "type": "BiologicFunction"}, {"text": "bronchoscopies", "type": "HealthCareActivity"}, {"text": "placebo", "type": "Chemical"}, {"text": "sulforaphane", "type": "Chemical"}, {"text": "mouth", "type": "SpatialConcept"}]}

Example input:
Sentence: Compared with those without polycythemia , the polycythemia group had significantly lower forced expiratory volume in one second ( FEV1 ) level ( 0 . 9±0 .

Example answer:
{"entities": [{"text": "polycythemia", "type": "BiologicFunction"}, {"text": "forced expiratory volume in one second ( FEV1 ) level", "type": "HealthCareActivity"}]}

Example input:
Sentence: PFTs averaged over all patients and parameters demonstrated small absolute declines , 5 . 7 % averaged PFT decline , at approximately 1 year of follow - up , but only the diffusing capacity of lung for carbon monoxide ( DLCO ) demonstrated a statistically significant decline ( 10 . 29 vs .

Example answer:
{"entities": [{"text": "PFTs", "type": "HealthCareActivity"}, {"text": "PFT", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Despite pneumothorax , patients experienced modest but significant improvements in lung function parameters ( forced expiratory volume in 1 second : 55±148 mL , residual volume : -390±964 mL , total lung capacity : -348±876 ; all P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "pneumothorax", "type": "BiologicFunction"}, {"text": "lung function", "type": "BiologicFunction"}, {"text": "forced expiratory volume", "type": "BiologicFunction"}, {"text": "residual volume", "type": "ClinicalAttribute"}, {"text": "total lung capacity", "type": "Finding"}]}

Example input:
Sentence: Our results showed an increase in bronchial hyperresponsiveness stimulated by methacholine ( Mch ) , inflammatory cell influx , especially eosinophils together with an increase of high mobility group box 1 ( HMGB1 ) and altered lipid peroxidation ( LP ) and antioxidant defenses in the OVA group compared to the control group ( p ≤ 0 . 5 ) .

Example answer:
{"entities": [{"text": "bronchial hyperresponsiveness", "type": "BiologicFunction"}, {"text": "methacholine", "type": "Chemical"}, {"text": "Mch", "type": "Chemical"}, {"text": "cell influx", "type": "BiologicFunction"}, {"text": "eosinophils", "type": "AnatomicalStructure"}, {"text": "high mobility group box 1", "type": "Chemical"}, {"text": "HMGB1", "type": "Chemical"}, {"text": "lipid peroxidation", "type": "BiologicFunction"}, {"text": "LP", "type": "BiologicFunction"}, {"text": "antioxidant", "type": "Chemical"}, {"text": "OVA", "type": "Chemical"}]}

Input:
Sentence: All subjects performed a methacholine bronchial challenge with the provocation dose causing 20 % decrease in the forced expiratory volume in 1 s calculated ( PD20met ) .

## Item MedMentions:test:373
Example input:
Sentence: Both primary BC ( 52 cases ; 38 % ) and metastatic site biopsies ( 86 cases ; 62 % ) were found to harbor ERBB2mut , which were distributed across carcinoma not otherwise specified ( NOS ) ( 69 cases ; 50 % ) , invasive ductal carcinoma ( IDC ) ( 40 cases ; 29 % ) , invasive lobular carcinoma ( ILC ) ( 27 cases ; 20 % ) , and mucinous mBC ( 2 cases ; 1 % ) .

Example answer:
{"entities": [{"text": "primary BC", "type": "BiologicFunction"}, {"text": "biopsies", "type": "HealthCareActivity"}, {"text": "ERBB2mut", "type": "AnatomicalStructure"}, {"text": "carcinoma", "type": "BiologicFunction"}, {"text": "invasive ductal carcinoma", "type": "BiologicFunction"}, {"text": "IDC", "type": "BiologicFunction"}, {"text": "invasive lobular carcinoma", "type": "BiologicFunction"}, {"text": "ILC", "type": "BiologicFunction"}, {"text": "mucinous mBC", "type": "BiologicFunction"}]}

Example input:
Sentence: Tumors that expressed four or five conditions ( biomarkers of chemoresistance with a determinated cutoff ) were associated with a 9 - fold increase in the chances of these patients of having a poor response to NCT .

Example answer:
{"entities": [{"text": "Tumors", "type": "BiologicFunction"}, {"text": "biomarkers", "type": "Chemical"}, {"text": "poor response", "type": "Finding"}]}

Example input:
Sentence: In two thirds of breast cancer patients , large ( > 1 cm ) residual tumors are present after neoadjuvant chemotherapy ( NCT ) .

Example answer:
{"entities": [{"text": "breast cancer", "type": "BiologicFunction"}, {"text": "residual tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: Circulating tumor cells ( CTCs ) are also known to be involved in cancer progression .

Example answer:
{"entities": [{"text": "Circulating tumor cells", "type": "AnatomicalStructure"}, {"text": "CTCs", "type": "AnatomicalStructure"}, {"text": "cancer progression", "type": "BiologicFunction"}]}

Example input:
Sentence: Retrospective review was performed of records of 83 patients with HCC who underwent ( 90 ) Y glass microsphere radioembolization with ( 99m ) Tc - MAA single photon emission computed tomography ( SPECT ) and ( 90 ) Y positron emission tomography ( PET ) / CT between January 2013 and December 2014 .

Example answer:
{"entities": [{"text": "Retrospective review", "type": "ResearchActivity"}, {"text": "records", "type": "IntellectualProduct"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "( 90 ) Y", "type": "Chemical"}, {"text": "glass microsphere", "type": "MedicalDevice"}, {"text": "radioembolization", "type": "HealthCareActivity"}, {"text": "( 99m ) Tc - MAA", "type": "Chemical"}, {"text": "single photon emission computed tomography", "type": "HealthCareActivity"}, {"text": "SPECT", "type": "HealthCareActivity"}, {"text": "positron emission tomography", "type": "HealthCareActivity"}, {"text": "( PET ) / CT", "type": "HealthCareActivity"}]}

Example input:
Sentence: A patient with an abnormally high level of the tumor markers , carbohydrate antigen - 724 ( CA724 ) , CA19 - 9 and carcinoembryonic antigen ( CEA ) , although without any detectable tumor , was treated with an immunomodulatory therapy featuring an infusion of cytokine - induced autologous killer cells ( CIKs ) at the request of the patient .

Example answer:
{"entities": [{"text": "tumor markers", "type": "Chemical"}, {"text": "carbohydrate antigen - 724", "type": "Chemical"}, {"text": "CA724", "type": "Chemical"}, {"text": "CA19 - 9", "type": "Chemical"}, {"text": "carcinoembryonic antigen", "type": "Chemical"}, {"text": "CEA", "type": "Chemical"}, {"text": "detectable", "type": "ClinicalAttribute"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "immunomodulatory therapy", "type": "HealthCareActivity"}, {"text": "infusion", "type": "HealthCareActivity"}, {"text": "cytokine - induced autologous killer cells", "type": "AnatomicalStructure"}, {"text": "CIKs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Visualization and targeting of LGR5 ( + ) human colon cancer stem cells The cancer stem cell ( CSC ) theory highlights a self - renewing subpopulation of cancer cells that fuels tumour growth .

Example answer:
{"entities": [{"text": "Visualization", "type": "Finding"}, {"text": "LGR5 ( + )", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "colon", "type": "AnatomicalStructure"}, {"text": "cancer stem cells", "type": "AnatomicalStructure"}, {"text": "cancer stem cell", "type": "AnatomicalStructure"}, {"text": "CSC", "type": "AnatomicalStructure"}, {"text": "self - renewing", "type": "BiologicFunction"}, {"text": "subpopulation", "type": "IntellectualProduct"}, {"text": "cancer cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: This study demonstrates that a small fraction of CETCs has proliferative activity .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "CETCs", "type": "AnatomicalStructure"}, {"text": "proliferative activity", "type": "Finding"}]}

Example input:
Sentence: Identifying the CETC subset with cancer stem cell properties may provide more clinically useful prognostic information .

Example answer:
{"entities": [{"text": "CETC", "type": "AnatomicalStructure"}, {"text": "cancer stem cell", "type": "AnatomicalStructure"}, {"text": "prognostic", "type": "IntellectualProduct"}]}

Example input:
Sentence: We have developed a simple method for identification and characterization of circulating cancer stem cells among circulating epithelial tumor cells ( CETCs ) .

Example answer:
{"entities": [{"text": "cancer stem cells", "type": "AnatomicalStructure"}, {"text": "circulating epithelial tumor cells", "type": "AnatomicalStructure"}, {"text": "CETCs", "type": "AnatomicalStructure"}]}

Input:
Sentence: CETCs were cultured under conditions favoring growth of tumorspheres from 72 patients with breast cancer , including a subpopulation of 23 patients with metastatic disease .

## Item MedMentions:test:98
Example input:
Sentence: No significant difference in the period of xylem formation and total growth was observed between the flushing classes .

Example answer:
{"entities": [{"text": "No significant", "type": "Finding"}, {"text": "xylem", "type": "Eukaryote"}, {"text": "growth", "type": "BiologicFunction"}]}

Example input:
Sentence: The temporal relationship between the apical and radial meristems can help in the understanding of tree growth as a whole process .

Example answer:
{"entities": [{"text": "apical", "type": "SpatialConcept"}, {"text": "meristems", "type": "Eukaryote"}, {"text": "tree", "type": "Eukaryote"}, {"text": "growth", "type": "BiologicFunction"}]}

Example input:
Sentence: Synchronisms between bud and cambium phenology in black spruce : early - flushing provenances exhibit early xylem formation Bud and cambial phenology represent the adaptation of species to the local environment that allows the growing season to be maximized while minimizing the risk of frost for the developing tissues .

Example answer:
{"entities": [{"text": "bud", "type": "Eukaryote"}, {"text": "cambium", "type": "AnatomicalStructure"}, {"text": "black spruce", "type": "Eukaryote"}, {"text": "xylem", "type": "Eukaryote"}, {"text": "Bud", "type": "Eukaryote"}, {"text": "cambial", "type": "AnatomicalStructure"}, {"text": "adaptation", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "local", "type": "SpatialConcept"}, {"text": "environment", "type": "SpatialConcept"}, {"text": "frost", "type": "Chemical"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We additionally analyzed the same phases again in September and in winter to verify the possible formation of IADFs in fall and whether cell production and differentiation was completed by the end of the calendar year .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "possible", "type": "Finding"}, {"text": "cell", "type": "AnatomicalStructure"}, {"text": "production", "type": "BiologicFunction"}, {"text": "differentiation", "type": "BiologicFunction"}]}

Example input:
Sentence: We applied the microcoring technique to analyze xylogenesis in Pinus halepensis and Arbutus unedo .

Example answer:
{"entities": [{"text": "analyze", "type": "ResearchActivity"}, {"text": "xylogenesis", "type": "BiologicFunction"}, {"text": "Pinus halepensis", "type": "Eukaryote"}, {"text": "Arbutus unedo", "type": "Eukaryote"}]}

Example input:
Sentence: Both species formed the same type of IADFs ( earlywood -like cells within latewood ) , due to temporary growth restoration triggered by rain events during the period of summer drought .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "restoration", "type": "Finding"}]}

Example input:
Sentence: Timing of False Ring Formation in Pinus halepensis and Arbutus unedo in Southern Italy : Outlook from an Analysis of Xylogenesis and Tree - Ring Chronologies Mediterranean tree rings are characterized by intra - annual density fluctuations ( IADFs ) due to partly climate - driven cambial activity .

Example answer:
{"entities": [{"text": "Ring Formation", "type": "BiologicFunction"}, {"text": "Pinus halepensis", "type": "Eukaryote"}, {"text": "Arbutus unedo", "type": "Eukaryote"}, {"text": "Southern", "type": "SpatialConcept"}, {"text": "Italy", "type": "SpatialConcept"}, {"text": "Outlook", "type": "ClinicalAttribute"}, {"text": "Analysis", "type": "ResearchActivity"}, {"text": "Xylogenesis", "type": "BiologicFunction"}, {"text": "Tree - Ring", "type": "Eukaryote"}, {"text": "Chronologies", "type": "IntellectualProduct"}, {"text": "Mediterranean", "type": "SpatialConcept"}, {"text": "tree rings", "type": "Eukaryote"}, {"text": "cambial activity", "type": "BiologicFunction"}]}

Example input:
Sentence: To reach an unbiased synchronization of the IADF position within tree rings and seasonal fluctuations in environmental conditions , it is necessary to know the timing of cambial activity and wood formation , which are species - and site - specific processes .

Example answer:
{"entities": [{"text": "unbiased", "type": "ResearchActivity"}, {"text": "position", "type": "SpatialConcept"}, {"text": "tree", "type": "Eukaryote"}, {"text": "rings", "type": "SpatialConcept"}, {"text": "fluctuations", "type": "Finding"}, {"text": "environmental", "type": "SpatialConcept"}, {"text": "cambial activity", "type": "BiologicFunction"}]}

Example input:
Sentence: To the best of our knowledge , this is the first attempt to study xylogenesis in a hardwood species forming frequent IADFs .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "xylogenesis", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: To facilitate tree - ring dating and identification of IADFs , we performed traditional dendroecological analysis .

Example answer:
{"entities": [{"text": "tree - ring dating", "type": "ResearchActivity"}, {"text": "analysis", "type": "ResearchActivity"}]}

Input:
Sentence: The dendro - anatomical approach , combining analysis of tree - ring series and of xylogenesis , helped to detect the period of IADF formation in the two species .

## Item MedMentions:test:427
Example input:
Sentence: In this study , we have tried to create a carbon nanoparticle with aspirin , and we expect that this new carbon nanoparticle will have both anti - inflammatory and fluorescent biomarker functions .

Example answer:
{"entities": [{"text": "carbon", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "fluorescent", "type": "Chemical"}, {"text": "biomarker functions", "type": "Chemical"}]}

Example input:
Sentence: Herein , a biocompatible Gd -integrated CuS nanotheranostic agent ( Gd : CuS @ BSA ) was synthesized via a facile and environmentally friendly biomimetic strategy , using bovine serum albumin ( BSA ) as a biotemplate at physiological temperature .

Example answer:
{"entities": [{"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "BSA", "type": "Chemical"}, {"text": "bovine serum albumin", "type": "Chemical"}]}

Example input:
Sentence: Self - assembled nanocomplex between polymerized phenylboronic acid and doxorubicin for efficient tumor - targeted chemotherapy Since the discovery that nano - scaled particulates can easily be incorporated into tumors via the enhanced permeability and retention ( EPR ) effect , such nanostructures have been exploited as therapeutic small molecule delivery systems .

Example answer:
{"entities": [{"text": "nanocomplex", "type": "Chemical"}, {"text": "phenylboronic acid", "type": "Chemical"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "delivery systems", "type": "MedicalDevice"}]}

Example input:
Sentence: Cytotoxicity and cell adhesion of nanocomposite films evaluated through cell viability ( MMT ) assay and crystal violet staining revealed that PVA -3wt % TiO2 nanocomposite could act as an excellent composite and hence suitable to be used in bone implant applications .

Example answer:
{"entities": [{"text": "Cytotoxicity", "type": "BiologicFunction"}, {"text": "cell adhesion", "type": "BiologicFunction"}, {"text": "cell viability ( MMT ) assay", "type": "ResearchActivity"}, {"text": "crystal violet staining", "type": "HealthCareActivity"}, {"text": "PVA", "type": "Chemical"}, {"text": "TiO2", "type": "Chemical"}, {"text": "bone implant applications", "type": "MedicalDevice"}]}

Example input:
Sentence: A model chitosan - tripolyphosphate ( TPP ) hydrogel nanoparticles ( CS - HNP ) , with a broad spectrum of possible applications was produced and sterilized in the absence and in the presence of protective sugars ( glucose and mannitol ) .

Example answer:
{"entities": [{"text": "chitosan", "type": "Chemical"}, {"text": "tripolyphosphate", "type": "Chemical"}, {"text": "TPP", "type": "Chemical"}, {"text": "CS", "type": "Chemical"}, {"text": "possible", "type": "Finding"}, {"text": "sterilized", "type": "HealthCareActivity"}, {"text": "protective sugars", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "mannitol", "type": "Chemical"}]}

Example input:
Sentence: A Microfluidic Platform to design crosslinked Hyaluronic Acid Nanoparticles ( cHANPs ) for enhanced MRI Recent advancements in imaging diagnostics have focused on the use of nanostructures that entrap Magnetic Resonance Imaging ( MRI ) Contrast Agents ( CAs ) , without the need to chemically modify the clinically approved compounds .

Example answer:
{"entities": [{"text": "enhanced MRI", "type": "HealthCareActivity"}, {"text": "imaging diagnostics", "type": "HealthCareActivity"}, {"text": "Magnetic Resonance Imaging", "type": "HealthCareActivity"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "Contrast Agents", "type": "Chemical"}, {"text": "CAs", "type": "Chemical"}, {"text": "chemically", "type": "Chemical"}, {"text": "compounds", "type": "Chemical"}]}

Example input:
Sentence: This study highlights the practicality and versatility of albumin -mediated biomimetic mineralization of a nanotheranostic agent and also suggests that bioinspired Gd : CuS @ BSA NPs possess promising imaging guidance and effective tumor ablation properties , with high spatial resolution and deep tissue penetration .

Example answer:
{"entities": [{"text": "albumin", "type": "Chemical"}, {"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "BSA", "type": "Chemical"}, {"text": "imaging guidance", "type": "HealthCareActivity"}, {"text": "tumor ablation properties", "type": "HealthCareActivity"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We have developed a method of formulation , in which CaWO4 ( CWO ) nanoparticles ( NPs ) are encapsulated within a biocompatible poly ( ethylene glycol - b - d , l - lactic acid ) ( PEG - PLA ) block copolymer ( BCP ) capsule .

Example answer:
{"entities": [{"text": "CaWO4", "type": "Chemical"}, {"text": "CWO", "type": "Chemical"}, {"text": "poly ( ethylene glycol - b - d , l - lactic acid ) ( PEG - PLA ) block copolymer ( BCP ) capsule", "type": "Chemical"}]}

Example input:
Sentence: Here , we prepared a series of nHAp / MWCNT - GO nanocomposites aimed at producing materials that combine similar bone characteristics ( nHAp ) with high mechanical strength ( MWCNT - GO ) .

Example answer:
{"entities": [{"text": "prepared", "type": "Finding"}, {"text": "nHAp", "type": "Chemical"}, {"text": "MWCNT", "type": "Chemical"}, {"text": "GO", "type": "Chemical"}, {"text": "bone", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Graphene oxide / multi - walled carbon nanotubes as nanofeatured scaffolds for the assisted deposition of nanohydroxyapatite : characterization and biological evaluation Nanohydroxyapatite ( nHAp ) is an emergent bioceramic that shows similar chemical and crystallographic properties as the mineral phase present in bone .

Example answer:
{"entities": [{"text": "Graphene oxide", "type": "Chemical"}, {"text": "multi - walled carbon nanotubes", "type": "Chemical"}, {"text": "nanohydroxyapatite", "type": "Chemical"}, {"text": "Nanohydroxyapatite", "type": "Chemical"}, {"text": "nHAp", "type": "Chemical"}, {"text": "bioceramic", "type": "Chemical"}, {"text": "mineral", "type": "Chemical"}, {"text": "present", "type": "Finding"}, {"text": "bone", "type": "AnatomicalStructure"}]}

Input:
Sentence: All nanocomposites were proved to be bioactive , since carbonated nHAp was found after 21 days in simulated body fluid .

## Item MedMentions:test:464
Example input:
Sentence: All groups improved their performance , obtaining low scores for the closed - eyes condition balance task after the training period in RD , VM , and aids received to keep balance in the novel task , and no differences were found between groups or in interaction effects .

Example answer:
{"entities": []}

Example input:
Sentence: Genetic reduction or pharmacological inhibition of STEP prevents the loss of NMDARs from synaptic membranes and reverses behavioral deficits in Nrg1 ( + / - ) mice .

Example answer:
{"entities": [{"text": "reduction", "type": "HealthCareActivity"}, {"text": "STEP", "type": "Chemical"}, {"text": "NMDARs", "type": "Chemical"}, {"text": "synaptic membranes", "type": "AnatomicalStructure"}, {"text": "behavioral deficits", "type": "BiologicFunction"}, {"text": "Nrg1 ( + / - )", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: The results showed that compounds 7 and 8 have neuroprotective effect .

Example answer:
{"entities": [{"text": "compounds 7", "type": "Chemical"}, {"text": "8", "type": "Chemical"}]}

Example input:
Sentence: ( i . e . , current reduction ) may allow the elimination of the reversible malfunctioning short term effects ( HPNS ) , or even deleterious long term effects induced by increased NMDAR function during HP exposure .

Example answer:
{"entities": [{"text": "HPNS", "type": "BiologicFunction"}, {"text": "NMDAR", "type": "Chemical"}]}

Example input:
Sentence: This lack of direct structural information not only hampers our knowledge regarding the binding modes of many popular ligands ( including the endogenous neurotransmitter - serotonin ) , but also limits the search for more potent compounds .

Example answer:
{"entities": [{"text": "structural", "type": "SpatialConcept"}, {"text": "binding modes", "type": "BiologicFunction"}, {"text": "ligands", "type": "Chemical"}, {"text": "neurotransmitter", "type": "Chemical"}, {"text": "serotonin", "type": "Chemical"}, {"text": "compounds", "type": "Chemical"}]}

Example input:
Sentence: Moreover , bicuculline or D - serine treatments rescue the motor and cognitive deficits in MK - 801 -treated mice and reduce STEP61 in mouse frontal cortex .

Example answer:
{"entities": [{"text": "bicuculline", "type": "Chemical"}, {"text": "D - serine", "type": "Chemical"}, {"text": "treatments", "type": "HealthCareActivity"}, {"text": "motor", "type": "Finding"}, {"text": "cognitive deficits", "type": "BiologicFunction"}, {"text": "MK - 801", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "STEP61", "type": "Chemical"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "frontal cortex", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Using HD mouse models that exhibit reduced PDE10 , we demonstrate the benefit of pharmacologic PDE10 inhibition to acutely correct basal ganglia circuitry deficits .

Example answer:
{"entities": [{"text": "HD", "type": "BiologicFunction"}, {"text": "mouse models", "type": "BiologicFunction"}, {"text": "PDE10", "type": "Chemical"}, {"text": "basal ganglia", "type": "AnatomicalStructure"}]}

Example input:
Sentence: They are key regulators of hormonal homeostasis and are important drug targets for metabolic disorders such as type - 2 diabetes mellitus ( T2DM ) , obesity , and dysregulations of the nervous systems such as migraine , anxiety , depression , neurodegeneration , psychiatric disorders , and cardiovascular diseases .

Example answer:
{"entities": [{"text": "homeostasis", "type": "BiologicFunction"}, {"text": "drug targets", "type": "MedicalDevice"}, {"text": "metabolic disorders", "type": "BiologicFunction"}, {"text": "type - 2 diabetes mellitus", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "dysregulations of the nervous systems", "type": "BiologicFunction"}, {"text": "migraine", "type": "BiologicFunction"}, {"text": "anxiety", "type": "BiologicFunction"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "neurodegeneration", "type": "BiologicFunction"}, {"text": "psychiatric disorders", "type": "BiologicFunction"}, {"text": "cardiovascular diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: The suppression of microglial cells using natural bioactive compounds has become increasingly important for brain therapy owing to the expected beneficial effect of lower toxicity .

Example answer:
{"entities": [{"text": "microglial cells", "type": "AnatomicalStructure"}, {"text": "bioactive compounds", "type": "Chemical"}]}

Example input:
Sentence: Overall , these findings demonstrate that Isx - 9 is a promising synthetic compound for the mitigation of stress - induced deficits in adult hippocampal neurogenesis .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "Isx - 9", "type": "Chemical"}, {"text": "compound", "type": "Chemical"}, {"text": "stress", "type": "Finding"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "neurogenesis", "type": "BiologicFunction"}]}

Input:
Sentence: Thus , the search for compounds that can reverse these deficits with minimal side effects has become a recognized priority .

## Item MedMentions:test:535
Example input:
Sentence: succinogenes immobilized cultures ( 35 . 4g / L and 0 .

Example answer:
{"entities": [{"text": "succinogenes", "type": "Bacterium"}, {"text": "immobilized", "type": "AnatomicalStructure"}, {"text": "cultures", "type": "HealthCareActivity"}]}

Example input:
Sentence: Growth was slowest with Vin50 -G , 28±10 .

Example answer:
{"entities": [{"text": "Growth was slowest", "type": "Finding"}, {"text": "Vin50", "type": "Chemical"}]}

Example input:
Sentence: In experiment 1 , SVC were grown in DMEM containing 10 % FBS ( Control ) and treated with 300 µM oleic acid ( OLA ) + FBS , linoleic acid ( LNA ) + FBS , palmitic acid ( PAM ) + FBS , or stearic acid ( STA ) + FBS for 48 h .

Example answer:
{"entities": [{"text": "SVC", "type": "AnatomicalStructure"}, {"text": "DMEM", "type": "Chemical"}, {"text": "FBS", "type": "Chemical"}, {"text": "oleic acid", "type": "Chemical"}, {"text": "OLA", "type": "Chemical"}, {"text": "linoleic acid", "type": "Chemical"}, {"text": "LNA", "type": "Chemical"}, {"text": "palmitic acid", "type": "Chemical"}, {"text": "PAM", "type": "Chemical"}, {"text": "stearic acid", "type": "Chemical"}, {"text": "STA", "type": "Chemical"}]}

Example input:
Sentence: All samples were cultured for 72 hours and colony - forming unit ( CFU ) was counted .

Example answer:
{"entities": [{"text": "cultured", "type": "HealthCareActivity"}]}

Example input:
Sentence: monocytogenes L12 strain ( 4 - log CFU / mL ) during storage at 4°C for one week .

Example answer:
{"entities": [{"text": "monocytogenes L12 strain", "type": "Bacterium"}]}

Example input:
Sentence: Growth occurred at 5 - 35 ° C ( optimum 30 ° C ) , at pH 6 .

Example answer:
{"entities": [{"text": "Growth", "type": "BiologicFunction"}]}

Example input:
Sentence: 25log CFU / g , while in the peel led to a κ value of 4 . 6±0 .

Example answer:
{"entities": [{"text": "peel", "type": "Food"}]}

Example input:
Sentence: 25log CFU / g and 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 06log CFU / g and 2 . 9±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 23log CFU / g ( p < 0 . 05 ) .

Example answer:
{"entities": []}

Input:
Sentence: 03log CFU / g were obtained from the growth of S .

## Item MedMentions:test:537
Example input:
Sentence: Silver nanoparticles were prepared from the reduction of silver nitrate and NaBH4 was used as reducing agent .

Example answer:
{"entities": [{"text": "Silver", "type": "Chemical"}, {"text": "silver nitrate", "type": "Chemical"}, {"text": "NaBH4", "type": "Chemical"}, {"text": "reducing agent", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , we investigated the newly synthesized nano - formulations against human hepatocellular carcinoma ( HepG2 ) and colorectal cancer ( HCT 116 ) cell lines using cell growth inhibition assays , followed by apoptosis and necrosis assays using flow cytometry to detect the underlying mechanism of HepG2 cell death .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "hepatocellular carcinoma", "type": "BiologicFunction"}, {"text": "HepG2", "type": "AnatomicalStructure"}, {"text": "colorectal cancer", "type": "BiologicFunction"}, {"text": "HCT 116", "type": "AnatomicalStructure"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "cell growth inhibition", "type": "BiologicFunction"}, {"text": "assays", "type": "HealthCareActivity"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "necrosis", "type": "BiologicFunction"}, {"text": "flow cytometry", "type": "HealthCareActivity"}, {"text": "detect", "type": "HealthCareActivity"}, {"text": "cell death", "type": "BiologicFunction"}]}

Example input:
Sentence: The mechanism is systematically investigated and the nanocontainers constructed through this method show excellent chemo - thermo performance in vitro .

Example answer:
{"entities": [{"text": "chemo - thermo performance", "type": "Finding"}]}

Example input:
Sentence: Important advances in polymer science , together with the development of novel techniques for nanocarrier preparation , and the discovery of novel targeting ligands and molecules , allow a fine - tuning of size , shape , chemicophysical properties and surface chemistry of functional particulate systems ; it enables the improvement of the therapeutic performances for several drugs , also toward districts that are difficult to be treated , such as the brain .

Example answer:
{"entities": [{"text": "polymer", "type": "Chemical"}, {"text": "ligands", "type": "Chemical"}, {"text": "size", "type": "SpatialConcept"}, {"text": "shape", "type": "SpatialConcept"}, {"text": "drugs", "type": "Chemical"}, {"text": "brain", "type": "AnatomicalStructure"}]}

Example input:
Sentence: However , the convoluted synthetic process of conventional nanostructures has impeded their feasibility and reproducibility in clinical applications .

Example answer:
{"entities": [{"text": "feasibility", "type": "ResearchActivity"}, {"text": "clinical applications", "type": "HealthCareActivity"}]}

Example input:
Sentence: Prepared nanoparticles were characterized by Visual inspection , Ultraviolet - visible spectroscopy ( UV ) , Fourier transform infrared Spectroscopy ( FT - IR ) , Transmission Electron Microscopy ( TEM ) techniques .

Example answer:
{"entities": [{"text": "Ultraviolet - visible spectroscopy", "type": "HealthCareActivity"}, {"text": "UV", "type": "HealthCareActivity"}, {"text": "Fourier transform infrared Spectroscopy", "type": "ResearchActivity"}, {"text": "FT - IR", "type": "ResearchActivity"}, {"text": "Transmission Electron Microscopy ( TEM ) techniques", "type": "HealthCareActivity"}]}

Example input:
Sentence: In this work , a polymer assembling strategy was used to make nanoparticles with exceptionally high loading of theranostic agent .

Example answer:
{"entities": [{"text": "polymer", "type": "Chemical"}, {"text": "theranostic agent", "type": "Chemical"}]}

Example input:
Sentence: Titanium dioxide and Zinc Oxide nanoparticle were synthesized by wet chemical process .

Example answer:
{"entities": [{"text": "Titanium dioxide", "type": "Chemical"}, {"text": "Zinc Oxide", "type": "Chemical"}]}

Example input:
Sentence: So far , there have been very few nanoparticles with immutable structures that can achieve this goal efficiently .

Example answer:
{"entities": [{"text": "structures", "type": "SpatialConcept"}]}

Example input:
Sentence: The use of plants extracts to synthesize and stabilize noble metal nanoparticles have been considered as safe , cost - effective , eco - benign and green approach nowadays .

Example answer:
{"entities": [{"text": "plants extracts", "type": "Chemical"}, {"text": "stabilize", "type": "Finding"}, {"text": "green approach", "type": "SpatialConcept"}]}

Input:
Sentence: To overcome these concerns , new methodologies including synthesis of nontoxic , human friendly and efficient nanoparticles is required .

## Item MedMentions:test:507
Example input:
Sentence: RFA for large GCHs can cause hemepigment - induced acute kidney injury due to massive intravascular hemolysis .

Example answer:
{"entities": [{"text": "RFA", "type": "HealthCareActivity"}, {"text": "GCHs", "type": "BiologicFunction"}, {"text": "hemepigment", "type": "Chemical"}, {"text": "acute kidney injury", "type": "InjuryOrPoisoning"}, {"text": "intravascular hemolysis", "type": "BiologicFunction"}]}

Example input:
Sentence: In a multivariate analysis , GCS ( Odds ratio [ OR ] = 0 . 726 , 95 % confidence interval [ CI ] = 0 . 661 - 0 . 796 , P < 0 . 001 ) , bleeding volume ( OR = 1 .

Example answer:
{"entities": [{"text": "GCS", "type": "IntellectualProduct"}, {"text": "bleeding", "type": "BiologicFunction"}]}

Example input:
Sentence: In a recent report of bipolar RFA , using two expandable needle electrodes , was uneventfully performed in patients with large GCH ( > 10 cm ) .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "bipolar RFA", "type": "HealthCareActivity"}, {"text": "GCH", "type": "BiologicFunction"}]}

Example input:
Sentence: Although further investigation is necessary to validate the maximum possible flap size , this technique may be applicable to at least small defects that are common after skin cancer ablation or trauma .

Example answer:
{"entities": [{"text": "investigation", "type": "HealthCareActivity"}, {"text": "validate", "type": "ResearchActivity"}, {"text": "possible", "type": "Finding"}, {"text": "flap", "type": "AnatomicalStructure"}, {"text": "size", "type": "SpatialConcept"}, {"text": "skin cancer", "type": "BiologicFunction"}, {"text": "ablation", "type": "HealthCareActivity"}, {"text": "trauma", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Patients with GCA had increased risks for all types of incident vascular disease compared with non - vasculitis patients : adjusted hazard ratios were 1 . 57 ( 95 % CI : 1 . 36 , 1 . 82 ) for myocardial infarction , 1 . 41 ( 95 % CI : 1 . 29 , 1 . 55 ) for stroke , 1 . 75 ( 95 % CI : 1 . 49 , 2 . 06 ) for peripheral vascular disease , 1 . 98 ( 95 % CI : 1 . 50 , 2 . 62 ) for aortic aneurysm and 2 . 03 ( 95 % CI : 1 . 77 , 2 . 33 ) for venous thromboembolism .

Example answer:
{"entities": [{"text": "GCA", "type": "BiologicFunction"}, {"text": "risks for all types of incident", "type": "Finding"}, {"text": "vascular disease", "type": "BiologicFunction"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "peripheral vascular disease", "type": "BiologicFunction"}, {"text": "aortic aneurysm", "type": "BiologicFunction"}, {"text": "venous thromboembolism", "type": "BiologicFunction"}]}

Example input:
Sentence: In 2015 we treated two patients for very large symptomatic GCH ( 15 . 7 and 25 . 0 cm ) with bipolar RFA during open laparotomy .

Example answer:
{"entities": [{"text": "GCH", "type": "BiologicFunction"}, {"text": "bipolar RFA", "type": "HealthCareActivity"}, {"text": "open laparotomy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Univariate analysis showed that PG volumes receiving more than 5 , 10 , 15 , and 20 Gy RBE ( V5 , V10 , V15 and V20 , respectively ) , mean dose , and maximum dose were significantly associated with PG atrophy .

Example answer:
{"entities": [{"text": "PG", "type": "AnatomicalStructure"}, {"text": "PG atrophy", "type": "BiologicFunction"}]}

Example input:
Sentence: RF Ablation of Giant Hemangiomas Inducing Acute Renal Failure : A Report of Two Cases In patients that require treatment for hepatic giant cavernous hemangiomas ( GCH ) , radiofrequency ablation ( RFA ) has been suggested to represent a safe and effective alternative to invasive surgery .

Example answer:
{"entities": [{"text": "RF Ablation", "type": "HealthCareActivity"}, {"text": "Giant Hemangiomas", "type": "BiologicFunction"}, {"text": "Acute Renal Failure", "type": "BiologicFunction"}, {"text": "Report", "type": "IntellectualProduct"}, {"text": "hepatic", "type": "SpatialConcept"}, {"text": "giant cavernous hemangiomas", "type": "BiologicFunction"}, {"text": "GCH", "type": "BiologicFunction"}, {"text": "radiofrequency ablation", "type": "HealthCareActivity"}, {"text": "RFA", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the GDFR group , ( 1 ) fluid maintenance was restricted to 3 ml / kg / h of a crystalloid solution and ( 2 ) colloid boluses were allowed only in case of hypotension associated with a low cardiac index and a high stroke volume variation .

Example answer:
{"entities": [{"text": "GDFR", "type": "HealthCareActivity"}, {"text": "fluid", "type": "BodySubstance"}, {"text": "crystalloid solution", "type": "Chemical"}, {"text": "colloid boluses", "type": "Chemical"}, {"text": "hypotension", "type": "Finding"}, {"text": "cardiac index", "type": "Finding"}, {"text": "high stroke volume", "type": "Finding"}]}

Example input:
Sentence: After receiver operating characteristics analysis , we defined a " high - risk group " for an unfavorable short - term outcome with GCS < 11 and ICH volume > 32 ml supratentorially or 21 ml infratentorially .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "GCS", "type": "IntellectualProduct"}, {"text": "ICH", "type": "Finding"}, {"text": "supratentorially", "type": "SpatialConcept"}, {"text": "infratentorially", "type": "SpatialConcept"}]}

Input:
Sentence: The presented cases suggest that caution is warranted and advocate an upper limit regarding the volume of GCHs that can be safely ablated .

## Item MedMentions:test:522
Example input:
Sentence: In the exploratory analysis , patients with DOR ≥12 months ( n = 287 ) or ≥24 months ( n = 133 ) were more likely to experience grade 3 / 4 AEs than the overall population .

Example answer:
{"entities": [{"text": "exploratory analysis", "type": "ResearchActivity"}, {"text": "AEs", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: 977 , CV = 1 . 5 % ) and inter - session reliability ( ICC = 0 . 978 , CV = 1 .

Example answer:
{"entities": []}

Example input:
Sentence: For the 50 - 60 % peak gas levels , individuals showed statistically significant reductions in responsiveness compared to rest , and across the group CS and CCS increased by 39 and 42 % , respectively , while CCSd was found to decrease by 398 % .

Example answer:
{"entities": [{"text": "individuals", "type": "PopulationGroup"}, {"text": "reductions", "type": "HealthCareActivity"}, {"text": "group", "type": "PopulationGroup"}, {"text": "CS", "type": "IntellectualProduct"}, {"text": "CCS", "type": "IntellectualProduct"}, {"text": "CCSd", "type": "IntellectualProduct"}]}

Example input:
Sentence: 6 , 95 % CI : 1 . 1 - 6 . 2 , and respiratory related arousal index : ≥7 . 6 / h OR = 2 . 3 , 95 % CI : 1 . 1 - 4 . 7 , but not measures of hypoxemia after adjustment for age , hypertension , diabetes , smoking , obesity , and NSAID use .

Example answer:
{"entities": [{"text": "arousal", "type": "BiologicFunction"}, {"text": "index", "type": "IntellectualProduct"}, {"text": "hypoxemia", "type": "Finding"}, {"text": "hypertension", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "NSAID", "type": "Chemical"}]}

Example input:
Sentence: 9 , 95 % confidence interval ( CI ) : 1 . 02 - 3 . 5 , severe OSA ( AHI ≥30 / h ) : OR = 2 .

Example answer:
{"entities": [{"text": "OSA", "type": "BiologicFunction"}]}

Example input:
Sentence: We compared patients with TCI ( baseline MoCA < 26 with ≥ 2 points increase at 1 month ) , PMCI ( MoCA < 26 with < 2 points increase ) , and no cognitive impairment ( NCI ; MoCA ≥ 26 ) .

Example answer:
{"entities": [{"text": "TCI", "type": "BiologicFunction"}, {"text": "MoCA", "type": "IntellectualProduct"}, {"text": "PMCI", "type": "BiologicFunction"}, {"text": "no cognitive impairment", "type": "Finding"}, {"text": "NCI", "type": "Finding"}]}

Example input:
Sentence: PA delivered through ACI can elicit EE at a moderate intensity level .

Example answer:
{"entities": [{"text": "EE", "type": "BiologicFunction"}]}

Example input:
Sentence: 1 % ) had PMCI , 98 ( 30 . 1 % ) TCI , and 182 ( 55 . 8 % ) NCI .

Example answer:
{"entities": [{"text": "PMCI", "type": "BiologicFunction"}, {"text": "TCI", "type": "BiologicFunction"}, {"text": "NCI", "type": "Finding"}]}

Example input:
Sentence: 42 ± 6 . 41 and 1 . 89 ± 8 . 77 cm / s , respectively ) , but these changes did not differ between patients with TCI , PMCI , and NCI .

Example answer:
{"entities": [{"text": "TCI", "type": "BiologicFunction"}, {"text": "PMCI", "type": "BiologicFunction"}, {"text": "NCI", "type": "Finding"}]}

Example input:
Sentence: The average EE for NCI and ACI were 1 . 8 ± 0 .

Example answer:
{"entities": [{"text": "EE", "type": "BiologicFunction"}]}

Input:
Sentence: The average intensity level for NCI and ACI were 1 . 9 ± 0 .

## Item MedMentions:test:347
Example input:
Sentence: Genes commonly coaltered with ERBB2 were tumor protein 53 ( TP53 ) ( 49 % ) ; phosphatidylinositol 3 - kinase catalytic subunit alpha ( PIK3CA ) ( 42 % ) ; cadherin 1 , type 1 ( CDH1 ) ( 37 % ) ; MYC ( 17 % ) ; and cyclin D1 protein ( CCND1 ) ( 16 % ) .

Example answer:
{"entities": [{"text": "Genes", "type": "AnatomicalStructure"}, {"text": "ERBB2", "type": "AnatomicalStructure"}, {"text": "tumor protein 53", "type": "AnatomicalStructure"}, {"text": "TP53", "type": "AnatomicalStructure"}, {"text": "phosphatidylinositol 3 - kinase catalytic subunit alpha", "type": "AnatomicalStructure"}, {"text": "PIK3CA", "type": "AnatomicalStructure"}, {"text": "cadherin 1 , type 1", "type": "AnatomicalStructure"}, {"text": "CDH1", "type": "AnatomicalStructure"}, {"text": "MYC", "type": "AnatomicalStructure"}, {"text": "cyclin D1 protein", "type": "AnatomicalStructure"}, {"text": "CCND1", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 9 % , 36 / 84 ) was the most common capsular serotype among HMKP isolates , followed by K1 ( 23 . 8 % , 20 / 84 ) .

Example answer:
{"entities": [{"text": "capsular", "type": "SpatialConcept"}, {"text": "serotype", "type": "IntellectualProduct"}, {"text": "HMKP", "type": "Bacterium"}, {"text": "isolates", "type": "Chemical"}, {"text": "K1", "type": "IntellectualProduct"}]}

Example input:
Sentence: Eight candidate genes were included : rbcL , rpoC1 , rpoB , matK , trnH - psbA , trnL ( UAA ) , atpF - atpH , and psbK - psbI .

Example answer:
{"entities": [{"text": "candidate genes", "type": "AnatomicalStructure"}, {"text": "rbcL", "type": "AnatomicalStructure"}, {"text": "rpoC1", "type": "AnatomicalStructure"}, {"text": "rpoB", "type": "AnatomicalStructure"}, {"text": "matK", "type": "AnatomicalStructure"}, {"text": "trnH - psbA", "type": "SpatialConcept"}, {"text": "trnL", "type": "AnatomicalStructure"}, {"text": "UAA", "type": "SpatialConcept"}, {"text": "atpF - atpH", "type": "SpatialConcept"}, {"text": "psbK - psbI", "type": "SpatialConcept"}]}

Example input:
Sentence: Analyses of our next generation sequencing results and data from five independent published studies consisting of 191 normal , 10 low - grade squamous intraepithelial lesions , 21 high - grade squamous intraepithelial lesions , and 335 malignant tissues identified a panel of nine genes ( ARHGAP6 , DAPK1 , HAND2 , NKX2 - 2 , NNAT , PCDH10 , PROX1 , PITX2 , and RAB6C ) which could effectively discriminate among the various groups with sensitivity and specificity of 80 % - 100 % ( p < 0 .

Example answer:
{"entities": [{"text": "Analyses", "type": "ResearchActivity"}, {"text": "next generation sequencing", "type": "ResearchActivity"}, {"text": "published studies", "type": "IntellectualProduct"}, {"text": "normal", "type": "Finding"}, {"text": "low - grade squamous intraepithelial lesions", "type": "BiologicFunction"}, {"text": "high - grade squamous intraepithelial lesions", "type": "BiologicFunction"}, {"text": "malignant", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "ARHGAP6", "type": "AnatomicalStructure"}, {"text": "DAPK1", "type": "AnatomicalStructure"}, {"text": "HAND2", "type": "AnatomicalStructure"}, {"text": "NKX2 - 2", "type": "AnatomicalStructure"}, {"text": "NNAT", "type": "AnatomicalStructure"}, {"text": "PCDH10", "type": "AnatomicalStructure"}, {"text": "PROX1", "type": "AnatomicalStructure"}, {"text": "PITX2", "type": "AnatomicalStructure"}, {"text": "RAB6C", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Our study demonstrates that 20 % of C→T and C→G mutations in the TpCpW context - where W denotes A or T , segregating as polymorphisms in human population -or 1 . 4 % of all heritable mutations are attributable to APOBEC3A / B activity .

Example answer:
{"entities": [{"text": "C→T", "type": "BiologicFunction"}, {"text": "C→G mutations", "type": "BiologicFunction"}, {"text": "TpCpW", "type": "SpatialConcept"}, {"text": "A", "type": "Chemical"}, {"text": "T", "type": "Chemical"}, {"text": "human population", "type": "Eukaryote"}, {"text": "mutations", "type": "BiologicFunction"}, {"text": "APOBEC3A / B", "type": "AnatomicalStructure"}, {"text": "activity", "type": "BiologicFunction"}]}

Example input:
Sentence: 1234 C > T mutation in varying amounts in affected skin ( up to 35 % ) and intestinal hamartoma ( 26 % ) .

Example answer:
{"entities": [{"text": "1234 C > T mutation", "type": "BiologicFunction"}, {"text": "skin", "type": "BodySystem"}, {"text": "intestinal hamartoma", "type": "BiologicFunction"}]}

Example input:
Sentence: In the present study , 1 , 997 genes only expressed in B73 and 2 , 024 genes only expressed in Mo17 displayed SPE complementation under control and water deficit conditions .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "water", "type": "Chemical"}]}

Example input:
Sentence: Specifically , five ( 56 % ) ductal adenomas and three ( 50 % ) tubular adenomas harbored mutated genes .

Example answer:
{"entities": [{"text": "ductal adenomas", "type": "BiologicFunction"}, {"text": "tubular adenomas", "type": "BiologicFunction"}, {"text": "mutated genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Similar results were seen when empty decoy capsids were added to full genome containing capsids in a 5 : 1 ratio .

Example answer:
{"entities": [{"text": "decoy capsids", "type": "AnatomicalStructure"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "capsids", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 2 % ) squamous , 89 ( 8 . 3 % ) micropapillary , 23 ( 2 . 2 % ) glandular , 34 ( 3 . 2 % ) mixed variants , and 33 ( 3 .

Example answer:
{"entities": [{"text": "squamous", "type": "BiologicFunction"}, {"text": "micropapillary", "type": "BiologicFunction"}, {"text": "glandular", "type": "BiologicFunction"}]}

Input:
Sentence: Twenty - two ( 56 % ) had partial capsular genes ( Group I ) and 17 ( 44 % ) had complete capsular deletion of which 15 had replacement by other genes ( Group II ) .

## Item MedMentions:test:449
Example input:
Sentence: Data were extracted from selected studies and analyzed using Stata to compare outcomes in trauma patients with early tracheostomy ( ET ) or late tracheostomy ( LT ) / prolonged intubation ( PI ) .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "Stata", "type": "IntellectualProduct"}, {"text": "trauma", "type": "InjuryOrPoisoning"}, {"text": "tracheostomy", "type": "HealthCareActivity"}, {"text": "ET", "type": "HealthCareActivity"}, {"text": "LT", "type": "HealthCareActivity"}, {"text": "intubation", "type": "HealthCareActivity"}, {"text": "PI", "type": "HealthCareActivity"}]}

Example input:
Sentence: 4 . Laryngoscope , 2017 .

Example answer:
{"entities": [{"text": "Laryngoscope", "type": "MedicalDevice"}]}

Example input:
Sentence: This randomized , controlled , cross - over study aimed to analyze the effectiveness of Macintosh , Miller , McCoy and McGrath laryngoscopes during with or without chest compressions in the scope of a simulated cardiopulmonary resuscitation scenario .

Example answer:
{"entities": [{"text": "randomized", "type": "ResearchActivity"}, {"text": "cross - over study", "type": "ResearchActivity"}, {"text": "analyze", "type": "ResearchActivity"}, {"text": "Macintosh", "type": "MedicalDevice"}, {"text": "Miller", "type": "MedicalDevice"}, {"text": "McCoy", "type": "MedicalDevice"}, {"text": "McGrath laryngoscopes", "type": "MedicalDevice"}, {"text": "cardiopulmonary resuscitation", "type": "HealthCareActivity"}]}

Example input:
Sentence: 4 . Laryngoscope , 2016 .

Example answer:
{"entities": []}

Example input:
Sentence: McGrath video laryngoscopes do not appear to have advantages over direct laryngoscopes for securing a smooth and successful tracheal intubation during rhythmic chest compressions .

Example answer:
{"entities": [{"text": "direct laryngoscopes", "type": "HealthCareActivity"}, {"text": "tracheal intubation", "type": "HealthCareActivity"}]}

Example input:
Sentence: The time required for successful tracheal intubation , number of attempts , dental trauma severity and the need for optimization manoeuvres were recorded during cardiopulmonary resuscitation with and without chest compressions .

Example answer:
{"entities": [{"text": "tracheal intubation", "type": "HealthCareActivity"}, {"text": "number of attempts", "type": "ClinicalAttribute"}, {"text": "dental trauma", "type": "InjuryOrPoisoning"}, {"text": "recorded", "type": "Finding"}, {"text": "cardiopulmonary resuscitation", "type": "HealthCareActivity"}]}

Example input:
Sentence: McCoy laryngoscope yielded the shortest time for successful tracheal intubation both in the presence of and without chest compressions .

Example answer:
{"entities": [{"text": "McCoy laryngoscope", "type": "MedicalDevice"}, {"text": "tracheal intubation", "type": "HealthCareActivity"}, {"text": "presence", "type": "Finding"}]}

Example input:
Sentence: We believe that as McCoy laryngoscope provided tracheal intubation in a shorter time and with fewer attempts , this laryngoscope may increase the success rate of resuscitation .

Example answer:
{"entities": [{"text": "McCoy laryngoscope", "type": "MedicalDevice"}, {"text": "tracheal intubation", "type": "HealthCareActivity"}, {"text": "laryngoscope", "type": "MedicalDevice"}, {"text": "resuscitation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Participants who are experienced computer game players using Macintosh , McCoy and McGrath achieved successful tracheal intubation in a significantly shorter time during resuscitation without chest compressions .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "experienced", "type": "BiologicFunction"}, {"text": "players", "type": "PopulationGroup"}, {"text": "Macintosh", "type": "MedicalDevice"}, {"text": "McCoy", "type": "MedicalDevice"}, {"text": "McGrath", "type": "MedicalDevice"}, {"text": "achieved", "type": "Finding"}, {"text": "tracheal intubation", "type": "HealthCareActivity"}, {"text": "resuscitation", "type": "HealthCareActivity"}]}

Example input:
Sentence: During the use of McCoy laryngoscopes , fewer tracheal intubation attempts , lower incidence of dental trauma and lower visual analogue scale scores on the ease of intubation were recorded .

Example answer:
{"entities": [{"text": "McCoy laryngoscopes", "type": "MedicalDevice"}, {"text": "tracheal intubation", "type": "HealthCareActivity"}, {"text": "dental trauma", "type": "InjuryOrPoisoning"}, {"text": "visual analogue scale scores", "type": "ClinicalAttribute"}, {"text": "intubation", "type": "HealthCareActivity"}, {"text": "recorded", "type": "Finding"}]}

Input:
Sentence: Dental trauma incidence and number of tracheal intubation attempts did not show any significant difference between the four laryngoscopes being related to the rate of playing computer games .

## Item MedMentions:test:221
Example input:
Sentence: Vagally - mediated cardiac activity as indexed by heart rate variability ( HRV ) has been associated with SRM and regulatory processes during stress .

Example answer:
{"entities": [{"text": "Vagally - mediated cardiac activity", "type": "Finding"}, {"text": "indexed", "type": "IntellectualProduct"}, {"text": "heart rate variability", "type": "Finding"}, {"text": "HRV", "type": "Finding"}, {"text": "regulatory processes", "type": "BiologicFunction"}, {"text": "stress", "type": "Finding"}]}

Example input:
Sentence: Systolic blood pressure and heart rate showed no significant differences between the 2 groups ( P = . 138 and .464 , respectively ) .

Example answer:
{"entities": [{"text": "Systolic blood pressure", "type": "ClinicalAttribute"}, {"text": "heart rate", "type": "ClinicalAttribute"}]}

Example input:
Sentence: By univariate analysis , blood pressure ( BP ) , heart rate , National Institutes of Health Stroke Scale ( NIHSS ) score , number of diffusion - positive lesion , count of red blood cell , high - density lipoprotein , and degree of stenosis differed significantly between the 2 groups .

Example answer:
{"entities": [{"text": "blood pressure", "type": "BiologicFunction"}, {"text": "BP", "type": "BiologicFunction"}, {"text": "heart rate", "type": "ClinicalAttribute"}, {"text": "National Institutes of Health Stroke Scale ( NIHSS ) score", "type": "Finding"}, {"text": "positive", "type": "Finding"}, {"text": "lesion", "type": "Finding"}, {"text": "count of red blood cell", "type": "HealthCareActivity"}, {"text": "high - density lipoprotein", "type": "Chemical"}]}

Example input:
Sentence: Correlation between Decreased Parasympathetic Activity and Reduced Cerebrovascular Reactivity in Patients with Lacunar Infarct Reduced cerebrovascular reactivity ( CVR ) was found in patients with recent lacunar infarct .

Example answer:
{"entities": [{"text": "Decreased Parasympathetic Activity", "type": "BiologicFunction"}, {"text": "Cerebrovascular Reactivity", "type": "BiologicFunction"}, {"text": "Lacunar Infarct", "type": "BiologicFunction"}, {"text": "cerebrovascular reactivity", "type": "BiologicFunction"}, {"text": "CVR", "type": "BiologicFunction"}, {"text": "lacunar infarct", "type": "BiologicFunction"}]}

Example input:
Sentence: It has been suggested that increased parasympathetic nervous activity is involved in asthma development in endurance athletes .

Example answer:
{"entities": [{"text": "parasympathetic", "type": "AnatomicalStructure"}, {"text": "nervous activity", "type": "BiologicFunction"}, {"text": "asthma", "type": "BiologicFunction"}, {"text": "endurance", "type": "Finding"}, {"text": "athletes", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: The cortisol awakenings response ( CAR ) measured hypothalamic - pituitary - adrenal ( HPA ) axis activity , whereas autonomous nervous system ( ANS ) activity was assessed by heart rate ( HR ) , pre - ejection period ( PEP ) and respiratory sinus arrhythmia ( RSA ) .

Example answer:
{"entities": [{"text": "cortisol awakenings response", "type": "BiologicFunction"}, {"text": "CAR", "type": "BiologicFunction"}, {"text": "hypothalamic - pituitary - adrenal ( HPA ) axis", "type": "BodySystem"}, {"text": "autonomous nervous system", "type": "BodySystem"}, {"text": "ANS", "type": "BodySystem"}, {"text": "heart rate", "type": "ClinicalAttribute"}, {"text": "HR", "type": "ClinicalAttribute"}, {"text": "respiratory sinus arrhythmia", "type": "BiologicFunction"}, {"text": "RSA", "type": "BiologicFunction"}]}

Example input:
Sentence: Parasympathetic Activity and Bronchial Hyperresponsiveness in Athletes A high prevalence of asthma and bronchial hyperresponsiveness ( BHR ) is reported in swimmers and cross - country skiers .

Example answer:
{"entities": [{"text": "Parasympathetic", "type": "AnatomicalStructure"}, {"text": "Activity", "type": "BiologicFunction"}, {"text": "Bronchial Hyperresponsiveness", "type": "BiologicFunction"}, {"text": "Athletes", "type": "ProfessionalOrOccupationalGroup"}, {"text": "asthma", "type": "BiologicFunction"}, {"text": "bronchial hyperresponsiveness", "type": "BiologicFunction"}, {"text": "BHR", "type": "BiologicFunction"}, {"text": "swimmers", "type": "PopulationGroup"}, {"text": "cross - country skiers", "type": "Finding"}]}

Example input:
Sentence: The type of sport influences BHR severity and its relationship to parasympathetic activity .

Example answer:
{"entities": [{"text": "BHR", "type": "BiologicFunction"}, {"text": "parasympathetic", "type": "AnatomicalStructure"}, {"text": "activity", "type": "BiologicFunction"}]}

Example input:
Sentence: Parasympathetic activity was measured by pupillometry and heart rate variability at the onset of exercise with the cardiac vagal index calculated in 28 cross - country skiers ( ♂ 18 / ♀10 ) , 29 swimmers ( ♂ 17 / ♀12 ) , and 30 healthy nonathlete controls ( ♂ 14 / ♀16 ) on two different days .

Example answer:
{"entities": [{"text": "Parasympathetic", "type": "AnatomicalStructure"}, {"text": "activity", "type": "BiologicFunction"}, {"text": "pupillometry", "type": "HealthCareActivity"}, {"text": "heart rate", "type": "ClinicalAttribute"}, {"text": "cross - country skiers", "type": "Finding"}]}

Example input:
Sentence: We aimed to assess the associations of BHR to parasympathetic activity in healthy and asthmatic swimmers and cross - country skiers and healthy non athletes .

Example answer:
{"entities": [{"text": "BHR", "type": "BiologicFunction"}, {"text": "parasympathetic", "type": "AnatomicalStructure"}, {"text": "activity", "type": "BiologicFunction"}, {"text": "asthmatic", "type": "BiologicFunction"}, {"text": "swimmers", "type": "PopulationGroup"}, {"text": "cross - country skiers", "type": "Finding"}, {"text": "athletes", "type": "ProfessionalOrOccupationalGroup"}]}

Input:
Sentence: Parasympathetic activity measured in the heart is more closely related to BHR as compared with parasympathetic activity measured in the pupils .

## Item MedMentions:test:251
Example input:
Sentence: Mutation of 19 potential MRP1 phosphorylation sites revealed that HEK - Tyr920Phe / Ser921Ala - MRP1 transported As ( GS ) 3 like HeLa - WT - MRP1 , whereas individual HEK - Tyr920Phe - and - Ser921Ala - MRP1 mutants were similar to HEK - WT - MRP1 .

Example answer:
{"entities": [{"text": "Mutation", "type": "BiologicFunction"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "sites", "type": "SpatialConcept"}, {"text": "HEK", "type": "AnatomicalStructure"}, {"text": "Tyr920Phe / Ser921Ala - MRP1", "type": "Chemical"}, {"text": "transported", "type": "BiologicFunction"}, {"text": "HeLa - WT", "type": "AnatomicalStructure"}, {"text": "MRP1", "type": "Chemical"}, {"text": "Tyr920Phe -", "type": "Chemical"}, {"text": "Ser921Ala - MRP1", "type": "Chemical"}, {"text": "mutants", "type": "Chemical"}, {"text": "HEK - WT", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A Microfluidic Platform to design crosslinked Hyaluronic Acid Nanoparticles ( cHANPs ) for enhanced MRI Recent advancements in imaging diagnostics have focused on the use of nanostructures that entrap Magnetic Resonance Imaging ( MRI ) Contrast Agents ( CAs ) , without the need to chemically modify the clinically approved compounds .

Example answer:
{"entities": [{"text": "enhanced MRI", "type": "HealthCareActivity"}, {"text": "imaging diagnostics", "type": "HealthCareActivity"}, {"text": "Magnetic Resonance Imaging", "type": "HealthCareActivity"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "Contrast Agents", "type": "Chemical"}, {"text": "CAs", "type": "Chemical"}, {"text": "chemically", "type": "Chemical"}, {"text": "compounds", "type": "Chemical"}]}

Example input:
Sentence: Retrospective review was performed of records of 83 patients with HCC who underwent ( 90 ) Y glass microsphere radioembolization with ( 99m ) Tc - MAA single photon emission computed tomography ( SPECT ) and ( 90 ) Y positron emission tomography ( PET ) / CT between January 2013 and December 2014 .

Example answer:
{"entities": [{"text": "Retrospective review", "type": "ResearchActivity"}, {"text": "records", "type": "IntellectualProduct"}, {"text": "HCC", "type": "BiologicFunction"}, {"text": "( 90 ) Y", "type": "Chemical"}, {"text": "glass microsphere", "type": "MedicalDevice"}, {"text": "radioembolization", "type": "HealthCareActivity"}, {"text": "( 99m ) Tc - MAA", "type": "Chemical"}, {"text": "single photon emission computed tomography", "type": "HealthCareActivity"}, {"text": "SPECT", "type": "HealthCareActivity"}, {"text": "positron emission tomography", "type": "HealthCareActivity"}, {"text": "( PET ) / CT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Our studies showed that MPP + treatment accelerated iron influx in the MES23 .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "MPP +", "type": "Chemical"}, {"text": "iron influx", "type": "BiologicFunction"}, {"text": "MES23 .", "type": "BiologicFunction"}]}

Example input:
Sentence: Simulations and in vivo human experiments at 7 T MRI show that the SFCR method provides high quality susceptibility maps with improved RMSE and MSSIM .

Example answer:
{"entities": [{"text": "Simulations", "type": "ResearchActivity"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "human", "type": "Eukaryote"}, {"text": "experiments", "type": "ResearchActivity"}, {"text": "MRI", "type": "HealthCareActivity"}]}

Example input:
Sentence: We propose that a Cdc45 -mediated loading guarantees a seamless deposition of RPA on newly emerging ssDNA at the nascent replication fork .

Example answer:
{"entities": [{"text": "Cdc45", "type": "Chemical"}, {"text": "RPA", "type": "Chemical"}, {"text": "ssDNA", "type": "Chemical"}, {"text": "replication fork", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We tested for viability of MU inside AP and observed strong RFP signals inside both trophozoites and cysts after 3 and 42 days of coculturing respectively .

Example answer:
{"entities": [{"text": "MU", "type": "Bacterium"}, {"text": "AP", "type": "Eukaryote"}, {"text": "RFP", "type": "Chemical"}, {"text": "signals", "type": "BiologicFunction"}, {"text": "trophozoites", "type": "Eukaryote"}, {"text": "cysts", "type": "AnatomicalStructure"}, {"text": "coculturing", "type": "HealthCareActivity"}]}

Example input:
Sentence: Men with elevated prostate - specific antigen or abnormal digital rectal exam underwent a 3 T multiparametric magnetic resonance imaging ( mpMRI ) with endorectal coil .

Example answer:
{"entities": [{"text": "Men", "type": "PopulationGroup"}, {"text": "prostate - specific antigen", "type": "Chemical"}, {"text": "abnormal digital rectal exam", "type": "HealthCareActivity"}, {"text": "3 T multiparametric magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "mpMRI", "type": "HealthCareActivity"}, {"text": "endorectal coil", "type": "MedicalDevice"}]}

Example input:
Sentence: We conducted a pilot study to evaluate the segmentation on a set of 10 infant hip MRI sequences using a 1 . 5 Tesla MR scanner .

Example answer:
{"entities": [{"text": "pilot study", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "hip", "type": "AnatomicalStructure"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "MR scanner", "type": "MedicalDevice"}]}

Example input:
Sentence: MRCP is a reliable non - invasive imaging method for demonstration of bile duct morpholog y , which is useful to plan complex surgeries and to prevent iatrogenic injuries .

Example answer:
{"entities": [{"text": "MRCP", "type": "HealthCareActivity"}, {"text": "imaging method", "type": "HealthCareActivity"}, {"text": "bile duct", "type": "AnatomicalStructure"}, {"text": "surgeries", "type": "HealthCareActivity"}, {"text": "iatrogenic injuries", "type": "InjuryOrPoisoning"}]}

Input:
Sentence: MRCP was performed in a 1 . 5 - Tesla magnet ( Philips ) with SSH MRCP 3DHR and SSHMRCP rad protocol .

## Item MedMentions:test:575
Example input:
Sentence: Survival analysis in the post - matching cohort was then evaluated using Kaplan - Meier analyses .

Example answer:
{"entities": [{"text": "Survival analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Statistical analyses examined differences in post - acute healthcare utilization , adjusted for pre - stroke utilization , as a function of race ( African - American vs . White ) , gender , age , stroke belt residence , income , Medicaid dual - eligibility , Charlson comorbidity index , and whether the person lived with an available caregiver .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "acute healthcare", "type": "HealthCareActivity"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "race", "type": "PopulationGroup"}, {"text": "African - American", "type": "PopulationGroup"}, {"text": "White", "type": "PopulationGroup"}, {"text": "residence", "type": "SpatialConcept"}, {"text": "Charlson comorbidity index", "type": "IntellectualProduct"}, {"text": "person", "type": "PopulationGroup"}, {"text": "caregiver", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Quantitative data were analysed to determine changes in motivation between intervention and comparison facilities pre - and post - intervention using STATA ™ version 13 .

Example answer:
{"entities": [{"text": "analysed", "type": "ResearchActivity"}, {"text": "motivation", "type": "BiologicFunction"}, {"text": "STATA ™ version 13", "type": "IntellectualProduct"}]}

Example input:
Sentence: Results After adjusting for covariates , women were more likely than men to receive home health care and to use emergency department services during the post - acute care period .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}, {"text": "emergency department services", "type": "HealthCareActivity"}, {"text": "acute care", "type": "HealthCareActivity"}]}

Example input:
Sentence: With this multimodal approach to evaluation and intervention , Kristen steadily improved and she returned to her baseline function .

Example answer:
{"entities": [{"text": "evaluation", "type": "HealthCareActivity"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "Kristen", "type": "PopulationGroup"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: We used hazard ratios ( HR ) and 95 % confidence intervals ( CI ) from the univariate and age - sex adjusted logistic regression model to assess the risk of comorbidities in patients with PsA and PsV .

Example answer:
{"entities": [{"text": "assess the risk", "type": "HealthCareActivity"}, {"text": "PsA", "type": "BiologicFunction"}, {"text": "PsV", "type": "BiologicFunction"}]}

Example input:
Sentence: Multivariable analyses using Cox proportional hazards were performed to measure the association between PBT , patient variables , and 3 primary end points : recurrence - free survival , disease - specific survival , and overall survival .

Example answer:
{"entities": [{"text": "Cox proportional hazards", "type": "IntellectualProduct"}, {"text": "PBT", "type": "HealthCareActivity"}, {"text": "recurrence - free survival", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The data of the 43 patients whose complete measurements were taken again in September 2014 were used for the longitudinal analysis .

Example answer:
{"entities": []}

Example input:
Sentence: The daily average steps of participants at baseline was 5678 ( SD , 2833 ; median , 5718 [ interquartile range , 3675 - 7279 ] ) .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: Routinely collected pre - / post - intervention data ( n = 246 patients at baseline ; sample sizes varied at end line ) were analysed and appropriate descriptive and summary statistics produced .

Example answer:
{"entities": []}

Input:
Sentence: Via a multi - step statistical plan , data were analyzed descriptively , cross - sectionally , and longitudinally , adjusting for baseline covariates , in patients having baseline plus ≥1 post - baseline assessment .

## Item MedMentions:test:532
Example input:
Sentence: rubrum survival was not affected in contact with purified OA , DTX - 1 and PTX - 2 solutions , but decreased significantly when the ciliate was exposed to cell - free or filtered culture medium from both D .

Example answer:
{"entities": [{"text": "rubrum", "type": "Eukaryote"}, {"text": "survival", "type": "BiologicFunction"}, {"text": "OA", "type": "Chemical"}, {"text": "DTX - 1", "type": "Chemical"}, {"text": "PTX - 2", "type": "Chemical"}, {"text": "ciliate", "type": "Eukaryote"}, {"text": "culture medium", "type": "Chemical"}, {"text": "D .", "type": "Eukaryote"}]}

Example input:
Sentence: lucidum .

Example answer:
{"entities": [{"text": "lucidum", "type": "Eukaryote"}]}

Example input:
Sentence: lucidum .

Example answer:
{"entities": [{"text": "lucidum", "type": "Eukaryote"}]}

Example input:
Sentence: Epidemiological study of relapsing fever borreliae detected in Haemaphysalis ticks and wild animals in the western part of Japan The genus Borrelia comprises arthropod - borne bacteria , which are infectious agents in vertebrates .

Example answer:
{"entities": [{"text": "Epidemiological study", "type": "ResearchActivity"}, {"text": "relapsing fever", "type": "BiologicFunction"}, {"text": "borreliae", "type": "Bacterium"}, {"text": "detected", "type": "Finding"}, {"text": "Haemaphysalis", "type": "Eukaryote"}, {"text": "ticks", "type": "Eukaryote"}, {"text": "wild animals", "type": "Eukaryote"}, {"text": "western part of Japan", "type": "SpatialConcept"}, {"text": "genus Borrelia", "type": "Bacterium"}, {"text": "arthropod - borne bacteria", "type": "Bacterium"}, {"text": "vertebrates", "type": "Eukaryote"}]}

Example input:
Sentence: jacquemontianum , and P .

Example answer:
{"entities": [{"text": "jacquemontianum", "type": "Eukaryote"}, {"text": "P .", "type": "Eukaryote"}]}

Example input:
Sentence: italicum .

Example answer:
{"entities": [{"text": "italicum", "type": "Eukaryote"}]}

Example input:
Sentence: incurvatum .

Example answer:
{"entities": [{"text": "incurvatum", "type": "Eukaryote"}]}

Example input:
Sentence: Typhi Vi antibodies and performed culture and quantitative polymerase chain reaction for the subset with bile , gallstone , tissue , and stool samples available .

Example answer:
{"entities": [{"text": "Typhi Vi antibodies", "type": "Chemical"}, {"text": "quantitative polymerase chain reaction", "type": "ResearchActivity"}, {"text": "bile", "type": "BodySubstance"}, {"text": "gallstone", "type": "BodySubstance"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "stool samples", "type": "BodySubstance"}]}

Example input:
Sentence: Typhi and GBC .

Example answer:
{"entities": [{"text": "Typhi", "type": "Bacterium"}, {"text": "GBC", "type": "BiologicFunction"}]}

Example input:
Sentence: typhimurium SL 1344 .

Example answer:
{"entities": [{"text": "typhimurium SL 1344", "type": "Bacterium"}]}

Input:
Sentence: Typhimurium .

## Item MedMentions:test:482
Example input:
Sentence: Multivariate analysis including the well - known RFs demonstrated that the latter for T - ALL were of no independent prognostic value and only the patient 's age was identified for B - ALL ( p = 0 . 013 ) .

Example answer:
{"entities": [{"text": "RFs", "type": "Finding"}, {"text": "T - ALL", "type": "BiologicFunction"}, {"text": "B - ALL", "type": "BiologicFunction"}]}

Example input:
Sentence: On univariate analysis , variables associated with worse survival included : clinical stage IIIB ( p = 0 . 037 ) , planning target volume ( PTV ) over 450 cc ( p < 0 . 001 ) , heart V30 over 40 % ( p = -0 . 048 ) , and esophageal mean dose over 20 % ( p = 0 . 024 ) , V5 ( p = -0 . 015 ) , and V60 ( p = -0 . 011 ) .

Example answer:
{"entities": [{"text": "worse", "type": "Finding"}, {"text": "stage IIIB", "type": "BiologicFunction"}, {"text": "heart", "type": "AnatomicalStructure"}, {"text": "esophageal", "type": "SpatialConcept"}]}

Example input:
Sentence: In Kaplan - Meier analyses , the high AST / ALT group showed worse progression - free survival ( PFS ) , cancer - specific survival ( CSS ) , and overall survival ( all P < .001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Odds ratio ( OR ) and 95 % confidence interval ( CI ) were pooled to evaluate the relationship between GLUT - 1 and clinical features and hazard ratio ( HR ) and 95 % CI were combined to measure the effect of GLUT - 1 on overall survival ( OS ) .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "GLUT - 1", "type": "Chemical"}, {"text": "clinical features", "type": "Finding"}]}

Example input:
Sentence: In multivariate Cox analyses , high AST / ALT was revealed as an independent predictor of PFS ( HR , 2 . 335 ; 95 % CI , 1 . 633 - 3 . 340 ; P < .001 ) , CSS ( HR , 2 . 550 ; 1 . 689 - 3 . 851 ; P < .001 ) , and overall survival ( HR , 2 . 069 ; 95 % CI , 1 . 409 - 3 . 038 ; P < .001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 22 was an independent indicator of a poor prognosis for advanced hypopharyngeal SCC , as per the following parameters : overall survival ( hazard ratio [ HR ] 2 . 53 , 95 % confidence interval [ CI ] 1 . 48 - 4 . 30 , p = 0 . 001 ) , disease - specific survival ( HR 2 . 45 , 95 % CI 1 . 38 - 4 . 34 , p = 0 . 002 ) , and disease - free survival ( HR 2 .

Example answer:
{"entities": [{"text": "independent", "type": "Finding"}, {"text": "poor prognosis", "type": "Finding"}, {"text": "hypopharyngeal", "type": "SpatialConcept"}, {"text": "SCC", "type": "BiologicFunction"}]}

Example input:
Sentence: BMI was also an independent prognostic factor for OS in multivariate analysis ( HR 0 . 541 ; 95 % CI 0 .

Example answer:
{"entities": [{"text": "BMI", "type": "ClinicalAttribute"}, {"text": "prognostic factor", "type": "ClinicalAttribute"}]}

Example input:
Sentence: EGFR ID expression ( hazard ratio [ HR ] 0 . 53 , P = 0 . 022 ) and Eastern Cooperative Oncology Group ( ECOG ) performance status ( PS ) ( HR 0 . 43 , P = 0 . 022 ) were significantly related with progression - free survival following EGFR - TKIs treatment .

Example answer:
{"entities": [{"text": "EGFR", "type": "Chemical"}, {"text": "ID", "type": "SpatialConcept"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Eastern Cooperative Oncology Group ( ECOG ) performance status ( PS )", "type": "ClinicalAttribute"}, {"text": "progression", "type": "BiologicFunction"}, {"text": "EGFR - TKIs treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Meta - analysis for poor prognostic factors as determined by hazard ratio ( HR ) and 95 % confidential interval ( 95 % CI ) .

Example answer:
{"entities": [{"text": "Meta - analysis", "type": "ResearchActivity"}, {"text": "prognostic factors", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Multivariable analysis revealed that female [ hazard ratio ( HR ) = 0 . 78 ] , adenocarcinoma ( HR = 0 . 77 ) , locoregional ( only ) recurrence ( HR = 0 . 59 ) and longer recurrence -free survival ( HR = 0 . 99 ) were favourably associated with PRS .

Example answer:
{"entities": [{"text": "adenocarcinoma", "type": "BiologicFunction"}, {"text": "locoregional ( only ) recurrence", "type": "BiologicFunction"}, {"text": "longer recurrence -free survival", "type": "Finding"}]}

Input:
Sentence: On multivariate analysis , performance status 0 to 1 ( hazard ratio [ HR ] , 0 . 026 ; P < .001 ) , adenocarcinoma ( HR , 0 . 156 ; P = .003 ) , and group A ( HR , 0 . 199 ; P = .033 ) were independent prognostic factors .

## Item MedMentions:test:393
Example input:
Sentence: The technique does not require contrast material , so it can safely be used in patients with renal failure .

Example answer:
{"entities": [{"text": "contrast material", "type": "Chemical"}, {"text": "renal failure", "type": "BiologicFunction"}]}

Example input:
Sentence: 12 ; 95 % CI , 5 . 56 to 22 . 24 ) and overall stone - free rates ( OR , 8 . 70 ; 95 % CI , 3 . 23 to 23 . 45 ) than URL , along with lower possibilities of surgical conversion ( OR , 0 . 11 ; 95 % CI , 0 . 03 to 0 . 49 ) and postoperative shock wave lithotripsy ( OR , 0 .

Example answer:
{"entities": [{"text": "URL", "type": "HealthCareActivity"}, {"text": "surgical conversion", "type": "HealthCareActivity"}, {"text": "shock wave lithotripsy", "type": "HealthCareActivity"}]}

Example input:
Sentence: During the operation , there was no bleeding , ureteral perforation , avulsion , and rupture .

Example answer:
{"entities": [{"text": "operation", "type": "HealthCareActivity"}, {"text": "no", "type": "Finding"}, {"text": "bleeding", "type": "BiologicFunction"}, {"text": "ureteral perforation", "type": "Finding"}, {"text": "avulsion", "type": "HealthCareActivity"}, {"text": "rupture", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Reasons for stent placement include 122 cases post ureteroscopy ( 63 % ) , 8 cases post percutaneous nephrolithotomy ( PCNL ) ( 4 % ) , 14 cases post extracorporeal shock wave lithotripsy ( SWL ) ( 7 % ) , 18 cases of cancer - related ureteral obstruction ( 9 % ) , 21 cases of hydronephrosis ( 11 % ) , and 11 for other reasons ( 6 % ) .

Example answer:
{"entities": [{"text": "stent placement", "type": "HealthCareActivity"}, {"text": "ureteroscopy", "type": "HealthCareActivity"}, {"text": "percutaneous nephrolithotomy", "type": "HealthCareActivity"}, {"text": "PCNL", "type": "HealthCareActivity"}, {"text": "extracorporeal shock wave lithotripsy", "type": "HealthCareActivity"}, {"text": "SWL", "type": "HealthCareActivity"}, {"text": "cancer - related", "type": "Finding"}, {"text": "ureteral obstruction", "type": "AnatomicalStructure"}, {"text": "hydronephrosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Minimally invasive percutaneous nephrolithotomy improves stone - free rates for impacted proximal ureteral stones : A systematic review and meta - analysis Urinary stones are common medical disorders and the treatment of impacted proximal ureteral stones ( IPUS ) is still a challenge for urologists .

Example answer:
{"entities": [{"text": "percutaneous nephrolithotomy", "type": "HealthCareActivity"}, {"text": "proximal", "type": "SpatialConcept"}, {"text": "ureteral stones", "type": "BiologicFunction"}, {"text": "systematic review", "type": "IntellectualProduct"}, {"text": "meta - analysis", "type": "ResearchActivity"}, {"text": "Urinary stones", "type": "BiologicFunction"}, {"text": "disorders", "type": "BiologicFunction"}, {"text": "impacted proximal ureteral stones", "type": "BiologicFunction"}, {"text": "IPUS", "type": "BiologicFunction"}, {"text": "urologists", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: The aim of this study was to compare the efficacy and safety of minimally invasive percutaneous nephrolithotomy ( MI - PCNL ) and ureteroscopic lithotripsy ( URL ) in the treatment of IPUS via a meta - analysis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "compare the efficacy", "type": "ResearchActivity"}, {"text": "safety", "type": "ResearchActivity"}, {"text": "percutaneous nephrolithotomy", "type": "HealthCareActivity"}, {"text": "PCNL", "type": "HealthCareActivity"}, {"text": "ureteroscopic lithotripsy", "type": "HealthCareActivity"}, {"text": "URL", "type": "HealthCareActivity"}, {"text": "IPUS", "type": "BiologicFunction"}, {"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: The results demonstrated that FURS in combination with holmium laser lithotripsy represented a favorable less - invasive alternative with high SFR and acceptable complication rates in the treatment of bilateral upper urinary tract calculi .

Example answer:
{"entities": [{"text": "FURS", "type": "HealthCareActivity"}, {"text": "lithotripsy", "type": "HealthCareActivity"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "bilateral", "type": "SpatialConcept"}, {"text": "upper", "type": "SpatialConcept"}, {"text": "urinary tract calculi", "type": "BodySubstance"}]}

Example input:
Sentence: Safety and Efficacy of Flexible Ureteroscopy in Combination with Holmium Laser Lithotripsy for the Treatment of Bilateral Upper Urinary Tract Calculi To retrospectively evaluate the safety and efficacy of flexible ureteroscopy ( FURS ) in combination with holmium laser lithotripsy for the treatment of bilateral upper urinary calculi .

Example answer:
{"entities": [{"text": "Safety", "type": "ResearchActivity"}, {"text": "Efficacy", "type": "ResearchActivity"}, {"text": "Flexible Ureteroscopy", "type": "HealthCareActivity"}, {"text": "Lithotripsy", "type": "HealthCareActivity"}, {"text": "Treatment", "type": "HealthCareActivity"}, {"text": "Bilateral", "type": "SpatialConcept"}, {"text": "Upper", "type": "SpatialConcept"}, {"text": "Urinary Tract Calculi", "type": "BodySubstance"}, {"text": "safety", "type": "ResearchActivity"}, {"text": "efficacy", "type": "ResearchActivity"}, {"text": "flexible ureteroscopy", "type": "HealthCareActivity"}, {"text": "FURS", "type": "HealthCareActivity"}, {"text": "lithotripsy", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "bilateral", "type": "SpatialConcept"}, {"text": "upper", "type": "SpatialConcept"}, {"text": "urinary calculi", "type": "BodySubstance"}]}

Example input:
Sentence: Retroperitoneal hemorrhage after ureteroscopy without laser lithotripsy : an extreme example of an underreported event ?

Example answer:
{"entities": [{"text": "Retroperitoneal hemorrhage", "type": "BiologicFunction"}, {"text": "ureteroscopy", "type": "HealthCareActivity"}, {"text": "laser lithotripsy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Retroperitoneal hemorrhage and an associated hematoma are uncommon but potentially serious complications following ureteroscopy with laser lithotripsy .

Example answer:
{"entities": [{"text": "Retroperitoneal hemorrhage", "type": "BiologicFunction"}, {"text": "hematoma", "type": "BiologicFunction"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "ureteroscopy", "type": "HealthCareActivity"}, {"text": "laser lithotripsy", "type": "HealthCareActivity"}]}

Input:
Sentence: However , no reports of serious bleeding complications have been published regarding ureteroscopy without laser lithotripsy in the management of stone disease .

## Item MedMentions:test:497
Example input:
Sentence: The control group ( n = 60 ) received conservative therapy without prostaglandins and prostacyclins , and the treatment group ( n = 150 ) received treatment with pl - VEGF165 as two intramuscular injections for a total dose of 2 .

Example answer:
{"entities": [{"text": "conservative therapy", "type": "HealthCareActivity"}, {"text": "prostaglandins", "type": "Chemical"}, {"text": "prostacyclins", "type": "Chemical"}, {"text": "treatment group", "type": "PopulationGroup"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "pl - VEGF165", "type": "Chemical"}]}

Example input:
Sentence: Additionally , CF significantly enhanced p21 levels , reduced cyclin D1 protein levels and triggered cancer cell death .

Example answer:
{"entities": [{"text": "CF", "type": "Eukaryote"}, {"text": "p21", "type": "Chemical"}, {"text": "cyclin D1 protein", "type": "Chemical"}, {"text": "cancer", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}]}

Example input:
Sentence: When intratumorally administered , PEG - PLA - coated CWO NPs showed complete retention in a tumor - bearing mouse model ( measurements were made up to 1 week ) .

Example answer:
{"entities": [{"text": "PEG - PLA", "type": "Chemical"}, {"text": "tumor - bearing mouse model", "type": "BiologicFunction"}]}

Example input:
Sentence: A bleomycin , etoposide , and cisplatin treatment protocol targeting germ cell neoplasia lead to disease remission and prolonged survival of 34 months .

Example answer:
{"entities": [{"text": "bleomycin", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "treatment protocol", "type": "HealthCareActivity"}, {"text": "germ cell neoplasia", "type": "BiologicFunction"}, {"text": "disease remission", "type": "Finding"}]}

Example input:
Sentence: For negative control , the phagocytosis inhibitor cytochalasin D ( CyD ) , was added prior to culture .

Example answer:
{"entities": [{"text": "phagocytosis", "type": "BiologicFunction"}, {"text": "cytochalasin D", "type": "Chemical"}, {"text": "CyD", "type": "Chemical"}, {"text": "culture", "type": "HealthCareActivity"}]}

Example input:
Sentence: A patient with an abnormally high level of the tumor markers , carbohydrate antigen - 724 ( CA724 ) , CA19 - 9 and carcinoembryonic antigen ( CEA ) , although without any detectable tumor , was treated with an immunomodulatory therapy featuring an infusion of cytokine - induced autologous killer cells ( CIKs ) at the request of the patient .

Example answer:
{"entities": [{"text": "tumor markers", "type": "Chemical"}, {"text": "carbohydrate antigen - 724", "type": "Chemical"}, {"text": "CA724", "type": "Chemical"}, {"text": "CA19 - 9", "type": "Chemical"}, {"text": "carcinoembryonic antigen", "type": "Chemical"}, {"text": "CEA", "type": "Chemical"}, {"text": "detectable", "type": "ClinicalAttribute"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "immunomodulatory therapy", "type": "HealthCareActivity"}, {"text": "infusion", "type": "HealthCareActivity"}, {"text": "cytokine - induced autologous killer cells", "type": "AnatomicalStructure"}, {"text": "CIKs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Chemotherapy regimens included gemcitabine alone or in association with other agents ( 44 % ) , oxaliplatin , irinotecan , fluorouracil and leucovorin ( FOLFIRINOX 8 % ) , and cisplatin , gemcitabine plus capecitabine and epirubicin ( PEXG ) or capecitabine and docetaxel ( PDXG ) or epirubicin and fluorouracil ( PEFG ) ( 48 % ) .

Example answer:
{"entities": [{"text": "Chemotherapy regimens", "type": "HealthCareActivity"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "agents", "type": "Chemical"}, {"text": "oxaliplatin", "type": "Chemical"}, {"text": "irinotecan", "type": "Chemical"}, {"text": "fluorouracil", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}, {"text": "FOLFIRINOX", "type": "HealthCareActivity"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "capecitabine", "type": "Chemical"}, {"text": "epirubicin", "type": "Chemical"}, {"text": "PEXG", "type": "HealthCareActivity"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "PDXG", "type": "HealthCareActivity"}, {"text": "PEFG", "type": "HealthCareActivity"}]}

Example input:
Sentence: The four different concentrations of pyridine and cyclophosphamide showed breaks and pulverization of chromosomes in dose dependent manner .

Example answer:
{"entities": [{"text": "pyridine", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "breaks", "type": "BiologicFunction"}, {"text": "pulverization of chromosomes", "type": "BiologicFunction"}]}

Example input:
Sentence: The objective of the study was to test the potential ovarian cancer chemopreventive effect of the p53 stabilizing compound CP - 31398 on hens that spontaneously present the ovarian cancer phenotype .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "BiologicFunction"}, {"text": "p53", "type": "Chemical"}, {"text": "stabilizing compound", "type": "Chemical"}, {"text": "CP - 31398", "type": "Chemical"}, {"text": "hens", "type": "Eukaryote"}]}

Example input:
Sentence: Breast cancer tissues were used as positive control for ERα and PR expression .

Example answer:
{"entities": [{"text": "Breast cancer", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "ERα", "type": "Chemical"}, {"text": "PR", "type": "Chemical"}]}

Input:
Sentence: Cyclophosphamide , a well - known carcinogen was used as positive control .

## Item MedMentions:test:365
Example input:
Sentence: Here , we investigate gastrocnemius muscle - tendon interaction in typically - developing ( TD ) adults and children , and in children with spastic cerebral palsy ( SCP ) .

Example answer:
{"entities": [{"text": "gastrocnemius muscle - tendon", "type": "SpatialConcept"}, {"text": "typically - developing", "type": "BiologicFunction"}, {"text": "TD", "type": "BiologicFunction"}, {"text": "spastic cerebral palsy", "type": "AnatomicalStructure"}, {"text": "SCP", "type": "AnatomicalStructure"}]}

Example input:
Sentence: This study used ultrasonography to assess the flexor pollicis longus tendon and intermediate tissue .

Example answer:
{"entities": [{"text": "ultrasonography", "type": "HealthCareActivity"}, {"text": "flexor pollicis longus tendon", "type": "AnatomicalStructure"}, {"text": "intermediate tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: At post - operative week 8 , the distal end of the regenerated tissue reached the vicinity of the tibial insertion on the control side in two of six specimens .

Example answer:
{"entities": [{"text": "distal end", "type": "SpatialConcept"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "tibial", "type": "AnatomicalStructure"}, {"text": "insertion", "type": "HealthCareActivity"}, {"text": "side", "type": "SpatialConcept"}, {"text": "specimens", "type": "Eukaryote"}]}

Example input:
Sentence: On the IG side , the regenerated tissue maintained continuity with the tibial insertion in all specimens .

Example answer:
{"entities": [{"text": "IG side", "type": "SpatialConcept"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "continuity", "type": "SpatialConcept"}, {"text": "tibial", "type": "AnatomicalStructure"}, {"text": "insertion", "type": "HealthCareActivity"}, {"text": "specimens", "type": "Eukaryote"}]}

Example input:
Sentence: Compression of the flexor pollicis longus tendon was seen in 11 cases ( 39 . 3 % ) , and this finding suggested the presence of thin , membrane - like intermediate tissue .

Example answer:
{"entities": [{"text": "flexor pollicis longus tendon", "type": "AnatomicalStructure"}, {"text": "intermediate tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Bilateral semitendinosus tendons were harvested from rabbits using a tendon stripper .

Example answer:
{"entities": [{"text": "Bilateral", "type": "SpatialConcept"}, {"text": "semitendinosus tendons", "type": "AnatomicalStructure"}, {"text": "harvested", "type": "HealthCareActivity"}, {"text": "rabbits", "type": "Eukaryote"}, {"text": "tendon stripper", "type": "MedicalDevice"}]}

Example input:
Sentence: On the inducing graft ( IG ) side , the tendon canal and semitendinosus tibial attachment site were connected by the fascia lata , which was harvested at the same width as the semitendinosus tendon .

Example answer:
{"entities": [{"text": "side", "type": "SpatialConcept"}, {"text": "tendon canal", "type": "AnatomicalStructure"}, {"text": "semitendinosus", "type": "AnatomicalStructure"}, {"text": "tibial", "type": "AnatomicalStructure"}, {"text": "attachment site", "type": "SpatialConcept"}, {"text": "fascia lata", "type": "AnatomicalStructure"}, {"text": "harvested", "type": "HealthCareActivity"}, {"text": "semitendinosus tendon", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Tendon tissue regenerated with the fascia lata graft was thicker than naturally occurring regenerated tissue .

Example answer:
{"entities": [{"text": "Tendon tissue", "type": "AnatomicalStructure"}, {"text": "fascia lata", "type": "AnatomicalStructure"}, {"text": "graft", "type": "AnatomicalStructure"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Inducement of tissue regeneration of harvested hamstring tendons in a rabbit model The objective of this study was to determine if the use of fascia lata as a tendon regeneration guide ( placed into the tendon canal following harvesting the semitendinosus tendon ) would improve the incidence of tissue regeneration and prevent fatty degeneration of the semitendinosus muscle .

Example answer:
{"entities": [{"text": "tissue regeneration", "type": "BiologicFunction"}, {"text": "harvested", "type": "HealthCareActivity"}, {"text": "hamstring tendons", "type": "AnatomicalStructure"}, {"text": "rabbit", "type": "Eukaryote"}, {"text": "objective", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "fascia lata", "type": "AnatomicalStructure"}, {"text": "tendon", "type": "AnatomicalStructure"}, {"text": "regeneration", "type": "HealthCareActivity"}, {"text": "tendon canal", "type": "AnatomicalStructure"}, {"text": "harvesting", "type": "HealthCareActivity"}, {"text": "semitendinosus tendon", "type": "AnatomicalStructure"}, {"text": "improve", "type": "Finding"}, {"text": "fatty degeneration", "type": "BiologicFunction"}, {"text": "semitendinosus muscle", "type": "AnatomicalStructure"}]}

Example input:
Sentence: However , the proportion of fatty tissue in the semitendinosus muscle was greater than that of normal muscle .Cite

Example answer:
{"entities": [{"text": "fatty tissue", "type": "AnatomicalStructure"}, {"text": "semitendinosus muscle", "type": "AnatomicalStructure"}, {"text": "normal muscle", "type": "AnatomicalStructure"}]}

Input:
Sentence: We evaluated the incidence of tendon tissue regeneration , cross - sectional area of the regenerated tendon tissue and proportion of fatty tissue in the semitendinosus muscle .

## Item MedMentions:test:195
Example input:
Sentence: This study provides a novel approach to exploit the history of physical illnesses extracted from EMR ( ICD - 10 codes without chapter V - mental and behavioral disorders ) to predict suicide risk , and this model outperforms existing clinical assessments of suicide risk .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "history", "type": "Finding"}, {"text": "physical illnesses", "type": "BiologicFunction"}, {"text": "EMR", "type": "IntellectualProduct"}, {"text": "without chapter V - mental and behavioral disorders", "type": "Finding"}, {"text": "suicide risk", "type": "Finding"}, {"text": "assessments", "type": "HealthCareActivity"}]}

Example input:
Sentence: The 2009 World Health Organisation ( WHO ) Global Health Risks Report was used as a framework to determine the prevalence and number of eight key risk factors for cardiovascular disease ( CVD ) in men and women with psychosis .

Example answer:
{"entities": [{"text": "World Health Organisation", "type": "Organization"}, {"text": "WHO", "type": "Organization"}, {"text": "Report", "type": "IntellectualProduct"}, {"text": "framework", "type": "IntellectualProduct"}, {"text": "cardiovascular disease", "type": "BiologicFunction"}, {"text": "CVD", "type": "BiologicFunction"}, {"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}, {"text": "psychosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Linear mixed models in the six months before suicidal behavior were conducted for each of five proposed acute risk factors for suicidal behavior .

Example answer:
{"entities": [{"text": "suicidal behavior", "type": "Finding"}, {"text": "risk factors", "type": "Finding"}]}

Example input:
Sentence: Acute risk factors for suicide attempts and death : prospective findings from the STEP - BD study Suicide is unfortunately common in psychiatric practice , but difficult to predict .

Example answer:
{"entities": [{"text": "risk factors", "type": "Finding"}, {"text": "suicide attempts", "type": "Finding"}, {"text": "death", "type": "Finding"}, {"text": "prospective findings", "type": "ResearchActivity"}, {"text": "BD", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "Suicide", "type": "Finding"}, {"text": "psychiatric", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "practice", "type": "BiologicFunction"}]}

Example input:
Sentence: Results An increase in suicide rates from the first to the second decade was followed by a fall in the third decade .

Example answer:
{"entities": []}

Example input:
Sentence: Mental illness has increased among young people in high - income countries , and suicide is now the leading cause of death for this group .

Example answer:
{"entities": [{"text": "Mental illness", "type": "BiologicFunction"}, {"text": "people", "type": "PopulationGroup"}, {"text": "high - income countries", "type": "SpatialConcept"}, {"text": "suicide", "type": "Finding"}, {"text": "cause of death", "type": "Finding"}, {"text": "group", "type": "PopulationGroup"}]}

Example input:
Sentence: This was associated with an increasing proportion of single men , those living alone , unemployment , consumption of alcohol , use of hanging , previous suicide attempt and history of treatment for mental illness .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "living alone", "type": "Finding"}, {"text": "unemployment", "type": "Finding"}, {"text": "hanging", "type": "InjuryOrPoisoning"}, {"text": "suicide attempt", "type": "Finding"}, {"text": "mental illness", "type": "BiologicFunction"}]}

Example input:
Sentence: Clinical implications This study highlights the need for more interventions and focus to be given to young males in the suicide prevention area and is of high importance in the field of public health .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "interventions", "type": "HealthCareActivity"}, {"text": "focus", "type": "BiologicFunction"}, {"text": "suicide", "type": "Finding"}, {"text": "field of public health", "type": "IntellectualProduct"}]}

Example input:
Sentence: An understanding of the interrelatedness of diverse distal and proximal risk factors on suicidal pathways in the wider environmental context for male farmers is required when developing and implementing rural suicide prevention activities .

Example answer:
{"entities": [{"text": "distal", "type": "SpatialConcept"}, {"text": "proximal", "type": "SpatialConcept"}, {"text": "risk factors", "type": "Finding"}, {"text": "suicidal", "type": "Finding"}, {"text": "farmers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "rural", "type": "Finding"}, {"text": "suicide prevention", "type": "HealthCareActivity"}]}

Example input:
Sentence: Data on suicides and open verdicts in men aged 15 - 34 were obtained from coroner 's records in Newcastle upon Tyne and analysed using SPSS software .

Example answer:
{"entities": [{"text": "suicides", "type": "Finding"}, {"text": "men", "type": "PopulationGroup"}, {"text": "coroner 's records", "type": "IntellectualProduct"}, {"text": "Newcastle upon Tyne", "type": "SpatialConcept"}, {"text": "analysed", "type": "ResearchActivity"}, {"text": "SPSS software", "type": "IntellectualProduct"}]}

Input:
Sentence: Changes in risk factors for young male suicide in Newcastle upon Tyne , 1961 - 2009 Aims and method To ascertain differences in patterns of suicide in young men over three decades ( 1960s , 1990s and 2000s ) and discuss implications for suicide prevention .

## Item MedMentions:test:637
Example input:
Sentence: 0±4 . 5 mm .

Example answer:
{"entities": []}

Example input:
Sentence: 49±0 . 14 mm , respectively , with no significant difference ( P > . 05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 26 . 0 mm / mm ( 2 ) ; P ≤ 0 . 001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 9 mm after follow - up ( p < 0 . 001 ) .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: 9±2 .

Example answer:
{"entities": []}

Example input:
Sentence: 1±1 . 6 mm , 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 9 ±3 . 8 mm ; MAM = 0 . 8 ±4 .

Example answer:
{"entities": [{"text": "MAM", "type": "BiologicFunction"}]}

Example input:
Sentence: 8 mm and 38 . 2 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 85 ± 0 . 27 mm and 0 . 87 ± 0 . 28 mm , was lower than the values obtained by manual and automated probing .

Example answer:
{"entities": [{"text": "probing", "type": "HealthCareActivity"}]}

Example input:
Sentence: 9 ± 4 . 2 mm ( range , 0 . 5 - 25 . 9 mm ) .

Example answer:
{"entities": []}

Input:
Sentence: 09±0 . 30 mm .

## Item MedMentions:test:476
Example input:
Sentence: Psychometric tests ( confirmatory factor analysis , Cronbach 's alpha , composite reliability ) and association ( linear regression , ANOVA ) with sociodemographic variables were undertaken .

Example answer:
{"entities": [{"text": "Psychometric", "type": "HealthCareActivity"}, {"text": "tests", "type": "IntellectualProduct"}, {"text": "Cronbach 's alpha", "type": "IntellectualProduct"}, {"text": "composite reliability", "type": "IntellectualProduct"}]}

Example input:
Sentence: Data analysis involved Pearson 's chi - square test , McNemar 's test , and Poisson regression with robust variance .

Example answer:
{"entities": [{"text": "Pearson 's chi - square test", "type": "IntellectualProduct"}, {"text": "McNemar 's test", "type": "IntellectualProduct"}, {"text": "Poisson regression", "type": "IntellectualProduct"}]}

Example input:
Sentence: Data were analyzed using repeated - measures ANOVA , α = 0 .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: Data were analyzed by three - way ANOVA and Tukey tests ( p < 0 .

Example answer:
{"entities": [{"text": "Tukey tests", "type": "IntellectualProduct"}]}

Example input:
Sentence: The data were analyzed using one - way analysis of variance followed by the post hoc Tukey honestly significantly different test ( p < 0 . 05 ) .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "post hoc Tukey", "type": "HealthCareActivity"}, {"text": "test", "type": "HealthCareActivity"}]}

Example input:
Sentence: Kinesiographic data were statistically analyzed using 1 - way ANOVA , followed by the Bonferroni test for multiple comparisons of means ( α = . 05 ) .

Example answer:
{"entities": [{"text": "Kinesiographic data", "type": "IntellectualProduct"}]}

Example input:
Sentence: The two - way ANOVA analysis shows these differences are not statistically significant .

Example answer:
{"entities": []}

Example input:
Sentence: For statistical analysis One - way ANOVA followed by the Holm - Sìdak post hoc test was used .

Example answer:
{"entities": [{"text": "Holm - Sìdak post hoc test", "type": "IntellectualProduct"}]}

Example input:
Sentence: Finally , a Newcombe - Wilson test was performed to evaluate the relationship between group and cluster codes and a 3×2 ANOVA to investigate the differences in kinematics between groups and cluster codes .

Example answer:
{"entities": [{"text": "Newcombe - Wilson test", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "cluster codes", "type": "IntellectualProduct"}, {"text": "kinematics", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Data collected were analyzed using analysis of variance ( ANOVA ) , Mann - Whitney and t tests .

Example answer:
{"entities": [{"text": "Data collected", "type": "Finding"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "Mann - Whitney", "type": "IntellectualProduct"}, {"text": "t tests", "type": "IntellectualProduct"}]}

Input:
Sentence: The distribution of the results is not normal thus analysis of variance ( ANOVA ) test and clustering analysis were employed for statistical verification of the grouping .

## Item MedMentions:test:470
Example input:
Sentence: CGRP expression , as determined by IHC , cannot be observed in other groups , indicating that the hippocampus may be the specific component of the brain that responds to " big stress " .

Example answer:
{"entities": [{"text": "CGRP", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "IHC", "type": "HealthCareActivity"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "big stress", "type": "BiologicFunction"}]}

Example input:
Sentence: Our results are broadly consistent with findings in rodents that acute alcohol and stress exposure suppress neurogenesis in the adult hippocampus , which in turn impairs performance in high interference memory tasks , while adolescent onset binge drinking causes more extensive brain damage and cognitive deficits .

Example answer:
{"entities": [{"text": "rodents", "type": "Eukaryote"}, {"text": "stress", "type": "BiologicFunction"}, {"text": "neurogenesis", "type": "BiologicFunction"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "memory", "type": "BiologicFunction"}, {"text": "brain damage", "type": "InjuryOrPoisoning"}, {"text": "cognitive deficits", "type": "BiologicFunction"}]}

Example input:
Sentence: We found that hippocampal Arc expression continued to increase well past the minimal time required for plateau - level fear .

Example answer:
{"entities": [{"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "Arc", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "fear", "type": "BiologicFunction"}]}

Example input:
Sentence: The hippocampus is a structure involved in exercise , which can improve synaptic plasticity and long - term potentiation ( LTP ) .

Example answer:
{"entities": [{"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "improve", "type": "Finding"}, {"text": "synaptic plasticity", "type": "BiologicFunction"}, {"text": "long - term potentiation", "type": "BiologicFunction"}, {"text": "LTP", "type": "BiologicFunction"}]}

Example input:
Sentence: Inspired by its higher expression during development and in regions involved in emotional behaviors , we hypothesized its involvement in cerebral changes caused by early - life stress .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "development", "type": "BiologicFunction"}, {"text": "emotional", "type": "Finding"}, {"text": "cerebral", "type": "AnatomicalStructure"}, {"text": "early - life stress", "type": "BiologicFunction"}]}

Example input:
Sentence: Given the proposed role of this form of structural plasticity in the functioning of the hippocampus ( namely learning and memory and affective behaviors ) , it is believed that alterations in hippocampal neurogenesis might underlie some of the behavioral deficits associated with these psychiatric and neurological conditions .

Example answer:
{"entities": [{"text": "functioning", "type": "BiologicFunction"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "learning", "type": "BiologicFunction"}, {"text": "memory", "type": "BiologicFunction"}, {"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "neurogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Behavioral analyses during 10 days of chronic stress pointed to a delayed decline in spatial memory , the full impact of which is evident only after the end of stress .

Example answer:
{"entities": [{"text": "Behavioral analyses", "type": "HealthCareActivity"}, {"text": "spatial memory", "type": "BiologicFunction"}, {"text": "stress", "type": "Finding"}]}

Example input:
Sentence: Notably , animals that were behaviorally the worst affected at the end of chronic stress suffered the most pronounced early loss in hippocampal volume .

Example answer:
{"entities": [{"text": "animals", "type": "Eukaryote"}, {"text": "suffered", "type": "BiologicFunction"}, {"text": "early loss in hippocampal volume", "type": "Finding"}]}

Example input:
Sentence: Together , these findings support the view that not only is smaller hippocampal volume linked to stress - induced memory deficits , but it may also act as an early risk factor for the eventual development of cognitive impairments seen in stress - related psychiatric disorders .

Example answer:
{"entities": [{"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "stress", "type": "Finding"}, {"text": "memory deficits", "type": "BiologicFunction"}, {"text": "risk factor", "type": "Finding"}, {"text": "cognitive impairments", "type": "BiologicFunction"}]}

Example input:
Sentence: Early hippocampal volume loss as a marker of eventual memory deficits caused by repeated stress Exposure to severe and prolonged stress has detrimental effects on the hippocampus .

Example answer:
{"entities": [{"text": "hippocampal", "type": "AnatomicalStructure"}, {"text": "volume loss", "type": "Finding"}, {"text": "marker", "type": "ClinicalAttribute"}, {"text": "memory deficits", "type": "BiologicFunction"}, {"text": "repeated stress", "type": "Finding"}, {"text": "stress", "type": "Finding"}, {"text": "detrimental effects", "type": "Finding"}, {"text": "hippocampus", "type": "AnatomicalStructure"}]}

Input:
Sentence: However , relatively little is known about the gradual changes in hippocampal structure , and its behavioral consequences , over the course of repeated stress .

## Item MedMentions:test:653
Example input:
Sentence: 3 ) ng / mL compared to the NB 8 group ( 339 . 1±32 .

Example answer:
{"entities": [{"text": "NB 8", "type": "Chemical"}]}

Example input:
Sentence: w . , sum of 6 ndl - PCB = 104 . 0 ng / g l .

Example answer:
{"entities": [{"text": "ndl - PCB", "type": "Chemical"}]}

Example input:
Sentence: w . , sum of 6 ndl - PCB = 162 . 8 ng / g l .

Example answer:
{"entities": [{"text": "ndl - PCB", "type": "Chemical"}]}

Example input:
Sentence: 6 % at six different concentrations from 0 . 5 to 7 . 5 ng / mL with 15 replicates at each level .

Example answer:
{"entities": []}

Example input:
Sentence: 5 ng / mL for urine .

Example answer:
{"entities": [{"text": "urine", "type": "BodySubstance"}]}

Example input:
Sentence: 23 ± 0 . 27 ng / mL [ P = .01 ] ; group 3 : 0 . 19 ± 0 . 34 ng / mL [ P = .01 ] ) .

Example answer:
{"entities": [{"text": "group 3", "type": "IntellectualProduct"}]}

Example input:
Sentence: 7 ng / mL urine or 38 .

Example answer:
{"entities": [{"text": "urine", "type": "BodySubstance"}]}

Example input:
Sentence: 2154 . 2 ± 1358 . 3 ng / mL ; p = .041 )

Example answer:
{"entities": []}

Example input:
Sentence: 54±9 . 02 ng / mL , P = 0 . 009 )

Example answer:
{"entities": []}

Example input:
Sentence: 6 ) ng / mL ( P < .001 ) and NB 4 group ( 293 . 6±43 . 3 ) ng / mL ( P < .01 ) .

Example answer:
{"entities": [{"text": "NB 4", "type": "Chemical"}]}

Input:
Sentence: 6 ng / ml .

## Item MedMentions:test:90
Example input:
Sentence: Through time - lapse imaging and quantitative assessment of migratory behaviour of the cardioblasts in loss - of - function mutants , we demonstrate that both Slit and Netrin mediated signals are autonomously and concomitantly required to maximize migration velocity , filopodial and lamellipodial activities .

Example answer:
{"entities": [{"text": "time - lapse imaging", "type": "HealthCareActivity"}, {"text": "cardioblasts", "type": "AnatomicalStructure"}, {"text": "loss - of - function", "type": "Finding"}, {"text": "mutants", "type": "BiologicFunction"}, {"text": "Slit", "type": "Chemical"}, {"text": "Netrin mediated signals", "type": "BiologicFunction"}, {"text": "migration velocity", "type": "BiologicFunction"}, {"text": "filopodial", "type": "AnatomicalStructure"}, {"text": "lamellipodial", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Coexistence of light - driven Na ( + ) and H ( + ) transport in a microbial rhodopsin from Nonlabens dokdonensis Ion pumping microbial rhodopsins are photochemically active membrane proteins , converting light energy into ion - motive - force for ATP synthesis .

Example answer:
{"entities": [{"text": "light - driven", "type": "BiologicFunction"}, {"text": "Na ( + )", "type": "BiologicFunction"}, {"text": "H ( + ) transport", "type": "BiologicFunction"}, {"text": "microbial rhodopsin", "type": "Chemical"}, {"text": "Nonlabens dokdonensis", "type": "Bacterium"}, {"text": "Ion pumping", "type": "Chemical"}, {"text": "microbial rhodopsins", "type": "Chemical"}, {"text": "active membrane proteins", "type": "Chemical"}, {"text": "ion - motive - force", "type": "BiologicFunction"}, {"text": "ATP synthesis", "type": "BiologicFunction"}]}

Example input:
Sentence: They dock and fuse with endocytic carrier vesicles originating from the plasma membrane , sort the internalized material in internal microdomains , and allow the budding of new carrier vesicles from their membrane , destined to fuse with the plasma membrane ( recycling ) or other organelles .

Example answer:
{"entities": [{"text": "dock", "type": "BiologicFunction"}, {"text": "endocytic", "type": "BiologicFunction"}, {"text": "carrier vesicles", "type": "AnatomicalStructure"}, {"text": "plasma membrane", "type": "AnatomicalStructure"}, {"text": "internalized", "type": "Finding"}, {"text": "internal", "type": "SpatialConcept"}, {"text": "microdomains", "type": "AnatomicalStructure"}, {"text": "budding", "type": "BiologicFunction"}, {"text": "membrane", "type": "AnatomicalStructure"}, {"text": "recycling", "type": "AnatomicalStructure"}, {"text": "organelles", "type": "AnatomicalStructure"}]}

Example input:
Sentence: With the establishment of a larger collection of studied plant proteins taking these UPS pathways , a clearer picture of endomembrane trafficking as a whole will emerge .

Example answer:
{"entities": [{"text": "plant proteins", "type": "Chemical"}, {"text": "UPS", "type": "BiologicFunction"}, {"text": "endomembrane", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In this study , marked differences in As ( GS ) 3 transport kinetics were observed between MRP1 -enriched membrane vesicles prepared from human embryonic kidney 293 ( HEK ) ( Km 3 .

Example answer:
{"entities": [{"text": "transport", "type": "BiologicFunction"}, {"text": "MRP1", "type": "Chemical"}, {"text": "membrane", "type": "AnatomicalStructure"}, {"text": "vesicles", "type": "AnatomicalStructure"}, {"text": "human", "type": "Eukaryote"}, {"text": "embryonic", "type": "AnatomicalStructure"}, {"text": "kidney", "type": "AnatomicalStructure"}, {"text": "293 ( HEK )", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A high concentration of glucose and angiotensin II also promoted podocyte movement and migration .

Example answer:
{"entities": [{"text": "glucose", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}, {"text": "podocyte", "type": "AnatomicalStructure"}, {"text": "movement", "type": "BiologicFunction"}, {"text": "migration", "type": "BiologicFunction"}]}

Example input:
Sentence: Analyzing Endosomal Docking , Fusion , Sorting , and Budding Mechanisms in Isolated Organelles Due to their central role in the reception and sorting of newly internalized material , early endosomes undergo extensive membrane remodeling .

Example answer:
{"entities": [{"text": "Analyzing", "type": "ResearchActivity"}, {"text": "Endosomal", "type": "AnatomicalStructure"}, {"text": "Docking", "type": "BiologicFunction"}, {"text": "Fusion", "type": "HealthCareActivity"}, {"text": "Sorting", "type": "BiologicFunction"}, {"text": "Budding", "type": "BiologicFunction"}, {"text": "Organelles", "type": "AnatomicalStructure"}, {"text": "sorting", "type": "BiologicFunction"}, {"text": "internalized", "type": "Finding"}, {"text": "endosomes", "type": "AnatomicalStructure"}, {"text": "membrane", "type": "AnatomicalStructure"}, {"text": "remodeling", "type": "BiologicFunction"}]}

Example input:
Sentence: When early endosome transport is abolished , POs and LDs drift slowly towards the growing cell end .

Example answer:
{"entities": [{"text": "endosome transport", "type": "BiologicFunction"}, {"text": "POs", "type": "AnatomicalStructure"}, {"text": "LDs", "type": "AnatomicalStructure"}, {"text": "growing cell end", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Active diffusion and microtubule - based transport oppose myosin forces to position organelles in cells Even distribution of peroxisomes ( POs ) and lipid droplets ( LDs ) is critical to their role in lipid and reactive oxygen species homeostasis .

Example answer:
{"entities": [{"text": "microtubule - based transport", "type": "BiologicFunction"}, {"text": "myosin", "type": "Chemical"}, {"text": "position", "type": "SpatialConcept"}, {"text": "organelles", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "peroxisomes", "type": "AnatomicalStructure"}, {"text": "POs", "type": "AnatomicalStructure"}, {"text": "lipid droplets", "type": "AnatomicalStructure"}, {"text": "LDs", "type": "AnatomicalStructure"}, {"text": "lipid", "type": "Chemical"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "homeostasis", "type": "BiologicFunction"}]}

Example input:
Sentence: Modelling reveals that microtubule - based directed transport and active diffusion support distribution , mobility and mixing of POs .

Example answer:
{"entities": [{"text": "Modelling", "type": "ResearchActivity"}, {"text": "microtubule - based directed transport", "type": "BiologicFunction"}, {"text": "mobility", "type": "BiologicFunction"}, {"text": "POs", "type": "AnatomicalStructure"}]}

Input:
Sentence: These movements require ATP and involve bidirectional early endosome motility , indicating that microtubule - associated membrane trafficking enhances diffusion of organelles .

## Item MedMentions:test:542
Example input:
Sentence: Moreover , the inhibited growth of doubly siderophore - deficient strain of P . donghuensis under iron - limiting conditions could be partly restored by 7 - hydroxytropolone .

Example answer:
{"entities": [{"text": "inhibited growth", "type": "BiologicFunction"}, {"text": "P . donghuensis", "type": "Bacterium"}, {"text": "partly restored", "type": "HealthCareActivity"}, {"text": "7 - hydroxytropolone", "type": "Chemical"}]}

Example input:
Sentence: Mucosal IgM Antibody with d - Mannose Affinity in Fugu Takifugu rubripes Is Utilized by a Monogenean Parasite Heterobothrium okamotoi for Host Recognition How parasites recognize their definitive hosts is a mystery ; however , parasitism is reportedly initiated by recognition of certain molecules on host surfaces .

Example answer:
{"entities": [{"text": "Mucosal", "type": "AnatomicalStructure"}, {"text": "IgM Antibody", "type": "Chemical"}, {"text": "d - Mannose", "type": "Chemical"}, {"text": "Fugu Takifugu rubripes", "type": "Eukaryote"}, {"text": "Monogenean", "type": "Eukaryote"}, {"text": "Parasite", "type": "Eukaryote"}, {"text": "Heterobothrium okamotoi", "type": "Eukaryote"}, {"text": "Host Recognition", "type": "BiologicFunction"}, {"text": "parasites", "type": "Eukaryote"}, {"text": "recognize", "type": "BiologicFunction"}, {"text": "recognition", "type": "BiologicFunction"}, {"text": "host surfaces", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 7 - Hydroxytropolone produced and utilized as an iron - scavenger by Pseudomonas donghuensis Pseudomonas donghuensis can excrete large quantities of iron chelating substances in iron - restricted environments .

Example answer:
{"entities": [{"text": "7 - Hydroxytropolone", "type": "Chemical"}, {"text": "iron", "type": "Chemical"}, {"text": "Pseudomonas donghuensis", "type": "Bacterium"}, {"text": "excrete", "type": "BiologicFunction"}, {"text": "iron chelating substances", "type": "Chemical"}, {"text": "environments", "type": "SpatialConcept"}]}

Example input:
Sentence: The same chemicals were tested in 48 - h tests with other branchiopods ( the cladocerans Daphnia magna and Ceriodaphnia dubia ) and an amphipod ( Hyalella azteca ) , and in 96 - h tests with snails ( Physa gyrina and Lymnaea stagnalis ) .

Example answer:
{"entities": [{"text": "chemicals", "type": "Chemical"}, {"text": "tests", "type": "HealthCareActivity"}, {"text": "branchiopods", "type": "Eukaryote"}, {"text": "cladocerans", "type": "Eukaryote"}, {"text": "Daphnia magna", "type": "Eukaryote"}, {"text": "Ceriodaphnia dubia", "type": "Eukaryote"}, {"text": "amphipod", "type": "Eukaryote"}, {"text": "Hyalella azteca", "type": "Eukaryote"}, {"text": "snails", "type": "Eukaryote"}, {"text": "Physa gyrina", "type": "Eukaryote"}, {"text": "Lymnaea stagnalis", "type": "Eukaryote"}]}

Example input:
Sentence: Benihoppe , Tochiotome , Sachinoka , and Guimeiren strawberry fruits extracted by head - space solid - phase microextraction ( HS - SPME ) , respectively .

Example answer:
{"entities": [{"text": "Benihoppe", "type": "Food"}, {"text": "Tochiotome", "type": "Food"}, {"text": "Sachinoka", "type": "Food"}, {"text": "Guimeiren strawberry fruits", "type": "Food"}, {"text": "extracted", "type": "HealthCareActivity"}, {"text": "head - space solid - phase microextraction", "type": "HealthCareActivity"}, {"text": "HS - SPME", "type": "HealthCareActivity"}]}

Example input:
Sentence: In this study , we showed that the monogenean parasite Heterobothrium okamotoi utilizes IgM to recognize its host , fugu Takifugu rubripes Oncomiracidia are infective larvae of H . okamotoi that shed their cilia and metamorphose into juveniles when exposed to purified d - mannose - binding fractions from fugu mucus .

Example answer:
{"entities": [{"text": "monogenean", "type": "Eukaryote"}, {"text": "parasite", "type": "Eukaryote"}, {"text": "Heterobothrium okamotoi", "type": "Eukaryote"}, {"text": "IgM", "type": "Chemical"}, {"text": "fugu Takifugu rubripes Oncomiracidia", "type": "Eukaryote"}, {"text": "infective larvae", "type": "Eukaryote"}, {"text": "H . okamotoi", "type": "Eukaryote"}, {"text": "cilia", "type": "AnatomicalStructure"}, {"text": "metamorphose", "type": "BiologicFunction"}, {"text": "d - mannose", "type": "Chemical"}, {"text": "fugu", "type": "Eukaryote"}, {"text": "mucus", "type": "BodySubstance"}]}

Example input:
Sentence: Scoparone ( 6 , 7 - dimethoxycoumarin ) , a major bioactive compound found in various plant parts , including the inner shell of chestnut ( Castanea crenata ) , was evaluated on lipopolysaccharide ( LPS ) - activated BV - 2 microglia cells .

Example answer:
{"entities": [{"text": "Scoparone", "type": "Chemical"}, {"text": "6 , 7 - dimethoxycoumarin", "type": "Chemical"}, {"text": "bioactive compound", "type": "Chemical"}, {"text": "found", "type": "Finding"}, {"text": "plant parts", "type": "IntellectualProduct"}, {"text": "chestnut", "type": "Food"}, {"text": "Castanea crenata", "type": "Eukaryote"}, {"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "BV - 2 microglia cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: n . ( Draconematidae ) differs from other Prochaetosoma species except P .

Example answer:
{"entities": [{"text": "Draconematidae", "type": "Eukaryote"}, {"text": "Prochaetosoma species", "type": "Eukaryote"}, {"text": "P .", "type": "Eukaryote"}]}

Example input:
Sentence: Two known and one new species of Draconematidae and Epsilonematida ( Nematoda , Desmodorida ) from the White Sea , North Russia Morphological descriptions of three " walking nematode " species found for the first time in the White Sea are presented .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "Draconematidae", "type": "Eukaryote"}, {"text": "Epsilonematida", "type": "Eukaryote"}, {"text": "Nematoda", "type": "Eukaryote"}, {"text": "Desmodorida", "type": "Eukaryote"}, {"text": "White Sea", "type": "SpatialConcept"}, {"text": "North Russia", "type": "SpatialConcept"}, {"text": "Morphological", "type": "SpatialConcept"}, {"text": "descriptions", "type": "IntellectualProduct"}, {"text": "walking nematode", "type": "Eukaryote"}]}

Example input:
Sentence: Draconema ophicephalum ( Claparède , 1863 ) ( Draconematidae ) and Epsilonema steineri Chitwood , 1935 ( Epsilonematidae ) , both known from insufficient material and females only , are re - described and problems of their taxonomic identification as well as species compositions of respective genera are discussed .

Example answer:
{"entities": [{"text": "Draconema ophicephalum", "type": "Eukaryote"}, {"text": "Draconematidae", "type": "Eukaryote"}, {"text": "Epsilonema steineri", "type": "Eukaryote"}, {"text": "Epsilonematidae", "type": "Eukaryote"}, {"text": "problems", "type": "Finding"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "compositions", "type": "ClinicalAttribute"}, {"text": "genera", "type": "IntellectualProduct"}]}

Input:
Sentence: Draconema hoonsooi , D .

## Item MedMentions:test:177
Example input:
Sentence: After the scheduled survival period , the pulmonary arteries were sampled .

Example answer:
{"entities": [{"text": "pulmonary arteries", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The first cryoenergy application was performed in close proximity to the position during isolation of the left superior pulmonary vein ( PV ) .

Example answer:
{"entities": [{"text": "proximity", "type": "SpatialConcept"}, {"text": "isolation", "type": "HealthCareActivity"}, {"text": "left superior pulmonary vein", "type": "AnatomicalStructure"}, {"text": "PV", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Patients were monitored post - operatively for 2 h with standard invasive monitoring and with a study device comprising an arterial tonometry sensor ( BPro ( ® ) ) added with a three - dimensional accelerometer to investigate the potential impact of movement .

Example answer:
{"entities": [{"text": "monitored post - operatively", "type": "HealthCareActivity"}, {"text": "invasive monitoring", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "arterial", "type": "AnatomicalStructure"}, {"text": "tonometry sensor", "type": "MedicalDevice"}, {"text": "BPro ( ® )", "type": "MedicalDevice"}, {"text": "movement", "type": "BiologicFunction"}]}

Example input:
Sentence: Before the introduction of this technique , vascular puncture was acquired based on an integration of angiographic data , the bony iliofemoral landmarks and a radiopaque object .

Example answer:
{"entities": [{"text": "vascular", "type": "AnatomicalStructure"}, {"text": "puncture", "type": "HealthCareActivity"}, {"text": "angiographic", "type": "HealthCareActivity"}, {"text": "iliofemoral", "type": "AnatomicalStructure"}, {"text": "landmarks", "type": "SpatialConcept"}]}

Example input:
Sentence: Recently , minimally invasive methods , such as video - assisted thoracoscopic surgery ( VATS ) and , even more recently , non - intubated anesthesia , have emerged .

Example answer:
{"entities": [{"text": "methods", "type": "IntellectualProduct"}, {"text": "video - assisted thoracoscopic surgery", "type": "HealthCareActivity"}, {"text": "( VATS )", "type": "HealthCareActivity"}, {"text": "non - intubated", "type": "HealthCareActivity"}, {"text": "anesthesia", "type": "HealthCareActivity"}]}

Example input:
Sentence: Pressure tolerance at the sealed end was evaluated in 91 pulmonary artery sections .

Example answer:
{"entities": [{"text": "end", "type": "SpatialConcept"}, {"text": "pulmonary artery", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Pulmonary arteries from beagle dogs ( mean body weight 13 . 1 kg , range 10 . 5 - 15 . 4 kg ) were divided into 3 groups according to the in - vivo sealing method used ( Enseal , ligation , and proximal ligation plus distal Enseal ) and extracted to evaluate the pressure tolerance up to 75 mm Hg at the sealed end .

Example answer:
{"entities": [{"text": "Pulmonary arteries", "type": "AnatomicalStructure"}, {"text": "beagle dogs", "type": "Eukaryote"}, {"text": "in - vivo", "type": "SpatialConcept"}, {"text": "sealing method", "type": "IntellectualProduct"}, {"text": "Enseal", "type": "MedicalDevice"}, {"text": "ligation", "type": "HealthCareActivity"}, {"text": "proximal", "type": "SpatialConcept"}, {"text": "distal", "type": "SpatialConcept"}, {"text": "end", "type": "SpatialConcept"}]}

Example input:
Sentence: No sealing failure was found , and pathological findings showed healing and persistent hemostasis at all sealed ends of the pulmonary arteries after 2 and 4 weeks of the survival period .

Example answer:
{"entities": [{"text": "No", "type": "Finding"}, {"text": "sealing", "type": "HealthCareActivity"}, {"text": "findings", "type": "Finding"}, {"text": "healing", "type": "BiologicFunction"}, {"text": "hemostasis", "type": "BiologicFunction"}, {"text": "ends", "type": "SpatialConcept"}, {"text": "pulmonary arteries", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Our objective was to evaluate the feasibility and safety of sealing pulmonary arteries with the Enseal tissue - sealing device .

Example answer:
{"entities": [{"text": "sealing", "type": "HealthCareActivity"}, {"text": "pulmonary arteries", "type": "AnatomicalStructure"}, {"text": "Enseal tissue - sealing device", "type": "MedicalDevice"}]}

Example input:
Sentence: Pulmonary artery sealing with the Enseal device is feasible and safe in thoracic surgery settings .

Example answer:
{"entities": [{"text": "Pulmonary artery", "type": "AnatomicalStructure"}, {"text": "sealing", "type": "HealthCareActivity"}, {"text": "Enseal device", "type": "MedicalDevice"}, {"text": "thoracic surgery", "type": "HealthCareActivity"}]}

Input:
Sentence: Experimental study in pulmonary artery sealing with a vessel - sealing device The development of vessel - sealing devices will facilitate safety in video - assisted thoracoscopic surgery .

## Item MedMentions:test:156
Example input:
Sentence: Cervical fetal fibronectin , alpha fetoprotein , C - reactive protein and interleukin 6 can have an overall good diagnostic accuracy in identifying pregnancies at risk of SPTB .

Example answer:
{"entities": [{"text": "Cervical", "type": "SpatialConcept"}, {"text": "fetal fibronectin", "type": "Chemical"}, {"text": "alpha fetoprotein", "type": "Chemical"}, {"text": "C - reactive protein", "type": "Chemical"}, {"text": "interleukin 6", "type": "Chemical"}, {"text": "pregnancies at risk", "type": "BiologicFunction"}, {"text": "SPTB", "type": "Finding"}]}

Example input:
Sentence: 88 [ 95 % confidence interval 0 . 79 - 0 . 96 ] vs 0 . 77 [ 95 % confidence interval 0 . 62 - 0 . 92 ] , P = .12 in the cervical surgery group ; and 0 . 77 [ 95 % confidence interval 0 . 70 - 0 . 84 ] vs 0 . 74 [ 95 % confidence interval 0 . 67 - 0 . 81 ] , P = .32 in the previous spontaneous preterm birth group ) .

Example answer:
{"entities": [{"text": "spontaneous preterm birth", "type": "Finding"}]}

Example input:
Sentence: Cervical fibronectin was the biomarkers which showed the highest strength of association with the occurrence of SPTB ( delivery within 24 h OR 7 , 95 % CI 3 - 17 ; delivery < 7 days ( OR 12 , 95 % CI 8 - 16 ) .

Example answer:
{"entities": [{"text": "Cervical fibronectin", "type": "Chemical"}, {"text": "biomarkers", "type": "ClinicalAttribute"}, {"text": "SPTB", "type": "Finding"}, {"text": "delivery", "type": "BiologicFunction"}]}

Example input:
Sentence: We conducted a prospective blinded secondary analysis of a larger observational study of cervicovaginal fluid quantitative fetal fibronectin concentration in asymptomatic women measured with a Hologic 10Q system ( Hologic , Marlborough , MA ) .

Example answer:
{"entities": [{"text": "prospective", "type": "ResearchActivity"}, {"text": "blinded", "type": "ResearchActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "observational study", "type": "ResearchActivity"}, {"text": "cervicovaginal fluid", "type": "BodySubstance"}, {"text": "asymptomatic", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "Hologic 10Q system", "type": "IntellectualProduct"}, {"text": "Hologic", "type": "IntellectualProduct"}, {"text": "Marlborough", "type": "SpatialConcept"}, {"text": "MA", "type": "SpatialConcept"}]}

Example input:
Sentence: The rate of spontaneous preterm birth < 34 weeks in the cervical surgery group was 3 % compared with 9 % in previous spontaneous preterm birth group .

Example answer:
{"entities": [{"text": "spontaneous preterm birth", "type": "Finding"}]}

Example input:
Sentence: We sought to compare the predictive accuracy of cervicovaginal fluid quantitative fetal fibronectin and cervical length testing in asymptomatic women with previous cervical surgery to that in women with 1 previous preterm birth .

Example answer:
{"entities": [{"text": "cervicovaginal fluid", "type": "BodySubstance"}, {"text": "cervical length testing", "type": "HealthCareActivity"}, {"text": "asymptomatic", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "preterm birth", "type": "Finding"}]}

Example input:
Sentence: Receiver operating characteristic curves comparing quantitative fetal fibronectin for prediction at all 3 gestational end points were comparable between the cervical surgery and previous spontaneous preterm birth groups ( 34 weeks : area under the curve , 0 . 78 [ 95 % confidence interval 0 .

Example answer:
{"entities": [{"text": "spontaneous preterm birth", "type": "Finding"}]}

Example input:
Sentence: Quantitative fetal fibronectin and cervical length to predict preterm birth in asymptomatic women with previous cervical surgery Quantitative fetal fibronectin testing has demonstrated accuracy for prediction of spontaneous preterm birth in asymptomatic women with a history of preterm birth .

Example answer:
{"entities": [{"text": "cervical length", "type": "HealthCareActivity"}, {"text": "preterm birth", "type": "Finding"}, {"text": "asymptomatic", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "spontaneous preterm birth", "type": "Finding"}, {"text": "history", "type": "Finding"}]}

Example input:
Sentence: Prediction of spontaneous preterm birth using cervical length compared with quantitative fetal fibronectin for prediction of preterm birth < 34 weeks of gestation offered similar prediction ( area under the curve , 0 .

Example answer:
{"entities": [{"text": "spontaneous preterm birth", "type": "Finding"}, {"text": "cervical length", "type": "HealthCareActivity"}, {"text": "preterm birth", "type": "Finding"}, {"text": "gestation", "type": "BiologicFunction"}]}

Example input:
Sentence: Prediction of spontaneous preterm birth using cervicovaginal fluid quantitative fetal fibronectin in asymptomatic women with cervical surgery is valid , and has comparative accuracy to that in women with a history of spontaneous preterm birth .

Example answer:
{"entities": [{"text": "spontaneous preterm birth", "type": "Finding"}, {"text": "cervicovaginal fluid", "type": "BodySubstance"}, {"text": "asymptomatic", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "history", "type": "Finding"}]}

Input:
Sentence: Prediction of spontaneous preterm birth ( < 30 , < 34 , and < 37 weeks ) with cervicovaginal fluid quantitative fetal fibronectin concentration in primiparous women who had undergone at least 1 invasive cervical procedure ( n = 473 ) was compared with prediction in women who had previous spontaneous preterm birth , preterm prelabor rupture of membranes , or late miscarriage ( n = 821 ) .

## Item MedMentions:test:613
Example input:
Sentence: Aggregated over trials , participants spent more money for punishing the defection of likable - looking and smiling partners compared to punishing the defection of unlikable - looking and nonsmiling partners , but only because participants were more likely to cooperate with likable - looking and smiling partners , which provided the participants with more opportunities for moralistic punishment .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "likable", "type": "BiologicFunction"}, {"text": "partners", "type": "PopulationGroup"}, {"text": "unlikable", "type": "BiologicFunction"}, {"text": "opportunities", "type": "Finding"}]}

Example input:
Sentence: There were no statistically significant differences in costs per patient - day between cohorts after correcting for mortality ( € 1000 vs .

Example answer:
{"entities": [{"text": "cohorts", "type": "PopulationGroup"}]}

Example input:
Sentence: This study aimed to evaluate the effect of promising a monetary incentive at first mailout versus a promise on reminder letters only .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "letters", "type": "IntellectualProduct"}]}

Example input:
Sentence: A total of 1 , 029 women were randomised , 508 to the first mailout group and 518 to the reminder group .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "randomised", "type": "ResearchActivity"}]}

Example input:
Sentence: The total costs tended to be higher in patients who developed renal failure ( € 19 , 626±€10 , 840 vs . € 17 , 388±€9 , 369 ; P = . 14 ) .

Example answer:
{"entities": [{"text": "renal failure", "type": "BiologicFunction"}]}

Example input:
Sentence: 0 days ; P = . 26 ) and cost ( € 17 , 219±€8 , 792 vs .

Example answer:
{"entities": []}

Example input:
Sentence: The ICER was , therefore , substantially lower than the € 40 , 000 willingness - to - pay threshold per QALY adopted for the analysis .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: In a follow - up survey comparing video and paper groups to non - experienced groups , the rates were higher for video ( χ ( 2 ) = 24 . 319 , p < 0 . 001 ) and paper ( χ ( 2 ) = 11 . 134 , p = 0 . 001 ) .

Example answer:
{"entities": [{"text": "follow - up", "type": "ResearchActivity"}, {"text": "survey", "type": "IntellectualProduct"}, {"text": "video", "type": "IntellectualProduct"}]}

Example input:
Sentence: The primary outcome was the overall return rate , and secondary outcomes were the return rate without any chasing from the study office , and the total cost of the vouchers .

Example answer:
{"entities": [{"text": "vouchers", "type": "IntellectualProduct"}]}

Example input:
Sentence: There was no evidence to suggest a difference between groups in the overall return rate ( adjusted RR 1 . 03 ( 95 % CI 0 . 96 to 1 . 11 ) , however the proportion returned without chasing was higher in the first mailout group ( adjusted RR 1 . 22 , 95 % CI 1 .

Example answer:
{"entities": []}

Input:
Sentence: The total cost of the vouchers per participant was higher in the first mailout group ( mean difference £ 4 . 56 , 95 % CI £ 4 . 02 to £ 5 . 11 ) .

## Item MedMentions:test:607
Example input:
Sentence: coli and T .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "T .", "type": "Bacterium"}]}

Example input:
Sentence: coli and T .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "T .", "type": "Bacterium"}]}

Example input:
Sentence: coli removal by Napier grass VFS was on the order of log unit , which provided an important level of protection and reduced surface - flow concentrations of E .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "Napier grass", "type": "Eukaryote"}, {"text": "E .", "type": "Bacterium"}]}

Example input:
Sentence: In the CSX group , a significant correlation was found between TCC and FCN3 - TCC level ( r = 0 . 507 , P = 0 . 032 ) and between ficolin - 3 / MASP - 2 complex level and FCN3 - TCC deposition ( r = 0 . 651 , P = 0 . 003 ) .

Example answer:
{"entities": [{"text": "CSX", "type": "BiologicFunction"}, {"text": "TCC", "type": "Chemical"}, {"text": "FCN3", "type": "Chemical"}, {"text": "ficolin - 3", "type": "Chemical"}, {"text": "MASP - 2", "type": "Chemical"}, {"text": "complex", "type": "Chemical"}]}

Example input:
Sentence: coli to below the 200 ( CFU 100 mL ( - 1 ) ) recommended water quality standards , but not for nutrients and SS .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "nutrients", "type": "Food"}]}

Example input:
Sentence: coli C600 , and the cell - free supernatant of E .

Example answer:
{"entities": [{"text": "coli C600", "type": "Bacterium"}, {"text": "cell - free supernatant", "type": "BodySubstance"}, {"text": "E .", "type": "Bacterium"}]}

Example input:
Sentence: coli K - 12 , a classical non - environmental strain , constitutes a model of phenotypic plasticity for adaptation to a redox - cycling herbicide through redundancy of different isoforms of SOD and CAT enzymes .

Example answer:
{"entities": [{"text": "coli K - 12", "type": "Bacterium"}, {"text": "strain", "type": "Bacterium"}, {"text": "adaptation", "type": "BiologicFunction"}, {"text": "redox - cycling", "type": "BiologicFunction"}, {"text": "herbicide", "type": "Chemical"}, {"text": "isoforms", "type": "Chemical"}, {"text": "SOD", "type": "Chemical"}, {"text": "CAT enzymes", "type": "Chemical"}]}

Example input:
Sentence: coli cells were consistently detected by MVT .

Example answer:
{"entities": [{"text": "coli", "type": "Bacterium"}, {"text": "cells", "type": "Bacterium"}, {"text": "detected", "type": "Finding"}]}

Example input:
Sentence: coli 83972 and the uropathogenic strain E .

Example answer:
{"entities": [{"text": "coli 83972", "type": "Bacterium"}, {"text": "uropathogenic strain E .", "type": "Bacterium"}]}

Example input:
Sentence: coli ATCC 25922 and S .

Example answer:
{"entities": [{"text": "coli ATCC 25922", "type": "Bacterium"}, {"text": "S .", "type": "Bacterium"}]}

Input:
Sentence: coli CFT073 .

## Item MedMentions:test:519
Example input:
Sentence: No more CTCs were detected after the first cycle of standard chemotherapy in this study , and no distant metastases or recurrence were found in the CTC - positive patients during the follow - up period .

Example answer:
{"entities": [{"text": "CTCs", "type": "AnatomicalStructure"}, {"text": "detected", "type": "HealthCareActivity"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "distant metastases or recurrence", "type": "Finding"}, {"text": "CTC", "type": "AnatomicalStructure"}, {"text": "positive", "type": "Finding"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Circulating tumor cells ( CTCs ) are also known to be involved in cancer progression .

Example answer:
{"entities": [{"text": "Circulating tumor cells", "type": "AnatomicalStructure"}, {"text": "CTCs", "type": "AnatomicalStructure"}, {"text": "cancer progression", "type": "BiologicFunction"}]}

Example input:
Sentence: 28 ( 52 % ) patients were analyzed for both tissue samples and CTCs .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "tissue samples", "type": "AnatomicalStructure"}, {"text": "CTCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Detection of circulating tumour cells may add value in endometrial cancer management To evaluate the role of circulating tumour cells ( CTCs ) in patients with endometrial cancer ( EC ) .

Example answer:
{"entities": [{"text": "Detection", "type": "HealthCareActivity"}, {"text": "circulating tumour cells", "type": "AnatomicalStructure"}, {"text": "endometrial cancer", "type": "BiologicFunction"}, {"text": "management", "type": "HealthCareActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "CTCs", "type": "AnatomicalStructure"}, {"text": "EC", "type": "BiologicFunction"}]}

Example input:
Sentence: We have developed a simple method for identification and characterization of circulating cancer stem cells among circulating epithelial tumor cells ( CETCs ) .

Example answer:
{"entities": [{"text": "cancer stem cells", "type": "AnatomicalStructure"}, {"text": "circulating epithelial tumor cells", "type": "AnatomicalStructure"}, {"text": "CETCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: TIC can be distinguished from epithelial and stromal cells that comprise prostate tissue via cell sorting based upon Epcam , CD44 , and CD49f antigenic profiles .

Example answer:
{"entities": [{"text": "TIC", "type": "AnatomicalStructure"}, {"text": "epithelial", "type": "AnatomicalStructure"}, {"text": "stromal cells", "type": "AnatomicalStructure"}, {"text": "prostate tissue", "type": "AnatomicalStructure"}, {"text": "cell sorting", "type": "HealthCareActivity"}, {"text": "Epcam", "type": "AnatomicalStructure"}, {"text": "CD44", "type": "AnatomicalStructure"}, {"text": "CD49f", "type": "AnatomicalStructure"}]}

Example input:
Sentence: AR - amplification was detected in CellSearch -captured CTCs , but not in ISET -enriched CTCs which harbor exclusively AR gain of copies .

Example answer:
{"entities": [{"text": "AR", "type": "AnatomicalStructure"}, {"text": "amplification", "type": "ResearchActivity"}, {"text": "detected", "type": "Finding"}, {"text": "CellSearch", "type": "HealthCareActivity"}, {"text": "CTCs", "type": "AnatomicalStructure"}, {"text": "ISET", "type": "HealthCareActivity"}]}

Example input:
Sentence: CTCs were detected using the CellSearch system , and CTC results were correlated with standard clinicopathological characteristics and serum tumour marker CA125 / HE4 status using Chi - squared test , continuity correction or Fisher 's exact test .

Example answer:
{"entities": [{"text": "CTCs", "type": "AnatomicalStructure"}, {"text": "detected", "type": "HealthCareActivity"}, {"text": "CellSearch system", "type": "HealthCareActivity"}, {"text": "CTC", "type": "AnatomicalStructure"}, {"text": "serum tumour marker CA125 / HE4 status", "type": "Finding"}, {"text": "Chi - squared test", "type": "HealthCareActivity"}, {"text": "Fisher 's exact test", "type": "IntellectualProduct"}]}

Example input:
Sentence: Our data indicate that CTCs detected by the CellSearch and the ISET - filtration systems are not only phenotypically but also genetically different .

Example answer:
{"entities": [{"text": "CTCs", "type": "AnatomicalStructure"}, {"text": "detected", "type": "Finding"}, {"text": "CellSearch", "type": "HealthCareActivity"}, {"text": "ISET - filtration systems", "type": "HealthCareActivity"}]}

Example input:
Sentence: By comparing CellSearch and filtration ( ISET ) - enrichment combined to four color immunofluorescent staining , we showed that CellSearch and ISET isolated distinct subpopulations of CTCs : CTCs undergoing epithelial - to - mesenchymal transition , CTC clusters and large CTCs with cytomorphological characteristics but no detectable markers were isolated using ISET .

Example answer:
{"entities": [{"text": "CellSearch", "type": "HealthCareActivity"}, {"text": "filtration ( ISET", "type": "HealthCareActivity"}, {"text": "immunofluorescent staining", "type": "HealthCareActivity"}, {"text": "ISET", "type": "HealthCareActivity"}, {"text": "CTCs", "type": "AnatomicalStructure"}, {"text": "epithelial - to - mesenchymal transition", "type": "BiologicFunction"}, {"text": "CTC clusters", "type": "AnatomicalStructure"}, {"text": "detectable", "type": "ClinicalAttribute"}, {"text": "markers", "type": "ClinicalAttribute"}]}

Input:
Sentence: Epithelial CTCs detected by the CellSearch were mostly lost during the ISET - filtration .

## Item MedMentions:test:29
Example input:
Sentence: In order to illuminate this question , we chose for our study the representative grassland species Hippocrepis comosa ( Horseshoe vetch ) .

Example answer:
{"entities": [{"text": "grassland", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Hippocrepis comosa", "type": "Eukaryote"}, {"text": "Horseshoe vetch", "type": "Eukaryote"}]}

Example input:
Sentence: Indigenous forest patches within the plantation mosaic contained a highly characteristic acoustic species assemblage , emphasizing their complementary contribution to local biodiversity .

Example answer:
{"entities": [{"text": "acoustic species", "type": "IntellectualProduct"}, {"text": "local", "type": "SpatialConcept"}]}

Example input:
Sentence: This diversity is unprecedented for any Hirnantian fossil group , and the fauna provides a unique window into a post - extinction ecosystem .

Example answer:
{"entities": []}

Example input:
Sentence: Pasture type significantly affected most of the instrumental variables considered and , as a consequence , sensory properties were affected as well .

Example answer:
{"entities": [{"text": "Pasture", "type": "SpatialConcept"}]}

Example input:
Sentence: This high productivity was due primarily to high elevation range and high orographic diversity , which favored high habitat quality .

Example answer:
{"entities": [{"text": "elevation", "type": "SpatialConcept"}, {"text": "habitat", "type": "SpatialConcept"}]}

Example input:
Sentence: Using DNA microsatellites , we found that this population is reasonably genetically robust despite historical grazing , with similar effective population sizes and genetic diversity metrics across all sampling locations irrespective of habitat type and degree of degradation .

Example answer:
{"entities": [{"text": "DNA", "type": "Chemical"}, {"text": "microsatellites", "type": "Chemical"}, {"text": "population", "type": "PopulationGroup"}, {"text": "grazing", "type": "BiologicFunction"}, {"text": "locations", "type": "SpatialConcept"}, {"text": "habitat", "type": "SpatialConcept"}]}

Example input:
Sentence: Areas covered in nonnative timber or grass species were devoid of acoustic species .

Example answer:
{"entities": [{"text": "Areas", "type": "SpatialConcept"}, {"text": "nonnative timber", "type": "Eukaryote"}, {"text": "grass", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "acoustic species", "type": "IntellectualProduct"}]}

Example input:
Sentence: Species distribution modeling and molecular markers suggest longitudinal range shifts and cryptic northern refugia of the typical calcareous grassland species Hippocrepis comosa ( horseshoe vetch ) Calcareous grasslands belong to the most diverse , endangered habitats in Europe , but there is still insufficient information about the origin of the plant species related to these grasslands .

Example answer:
{"entities": [{"text": "Species", "type": "IntellectualProduct"}, {"text": "modeling", "type": "ResearchActivity"}, {"text": "molecular markers", "type": "ClinicalAttribute"}, {"text": "calcareous grassland", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Hippocrepis comosa", "type": "Eukaryote"}, {"text": "horseshoe vetch", "type": "Eukaryote"}, {"text": "Calcareous grasslands", "type": "SpatialConcept"}, {"text": "endangered habitats", "type": "SpatialConcept"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "plant", "type": "Eukaryote"}, {"text": "grasslands", "type": "SpatialConcept"}]}

Example input:
Sentence: Natural vegetation patches inside the plantation mosaic supported high mean acoustic diversity ( indigenous forests 7 . 6 , grasslands 8 . 0 , wetlands 9 . 1 ) , which increased as plant heterogeneity and patch size increased .

Example answer:
{"entities": [{"text": "grasslands", "type": "SpatialConcept"}, {"text": "plant", "type": "Eukaryote"}, {"text": "patch size", "type": "SpatialConcept"}]}

Example input:
Sentence: Large , natural , protected grassland sites in the PA had the highest mean acoustic diversity ( 14 . 1 species / site ) .

Example answer:
{"entities": [{"text": "grassland sites", "type": "SpatialConcept"}, {"text": "PA", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "site", "type": "SpatialConcept"}]}

Input:
Sentence: Sites grazed by native and domestic megaherbivores were fairly rich ( 5 . 1 ) in acoustic species but none were unique to this habitat type , where acoustic diversity was greater than in intensively managed grassland sites ( 0 . 04 ) .

## Item MedMentions:test:563
Example input:
Sentence: Intravascular ultrasound ( n = 34 ) or optical coherence tomography ( n = 31 ) was performed in all cases .

Example answer:
{"entities": [{"text": "Intravascular ultrasound", "type": "HealthCareActivity"}, {"text": "optical coherence tomography", "type": "HealthCareActivity"}]}

Example input:
Sentence: No meatal stenosis or urethral sacculation was detected during follow - up of the studied group .

Example answer:
{"entities": [{"text": "No meatal stenosis", "type": "Finding"}, {"text": "urethral sacculation", "type": "Finding"}, {"text": "detected", "type": "Finding"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: A prospectively maintained single - institution neuroendovascular database was accessed to identify consecutive cases of very small ( < 3 mm ) ruptured anterior communicating artery aneurysms treated endovascularly between 2006 and 2013 .

Example answer:
{"entities": [{"text": "neuroendovascular database", "type": "IntellectualProduct"}, {"text": "anterior communicating artery aneurysms", "type": "BiologicFunction"}]}

Example input:
Sentence: The most common diagnosis was single ventricle physiology ( 52 % ) , 9 palliated by Fontan operation and 2 by aortopulmonary shunts : d - transposition of the great arteries after Mustard / Senning ( n = 2 ) , tetralogy of Fallot ( n = 2 ) , aortic valve disease ( n = 2 ) , and other biventricular surgery ( n = 4 ) .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "single ventricle", "type": "AnatomicalStructure"}, {"text": "physiology", "type": "BiologicFunction"}, {"text": "palliated", "type": "HealthCareActivity"}, {"text": "Fontan operation", "type": "HealthCareActivity"}, {"text": "aortopulmonary shunts", "type": "HealthCareActivity"}, {"text": "d - transposition of the great arteries", "type": "AnatomicalStructure"}, {"text": "Mustard", "type": "HealthCareActivity"}, {"text": "Senning", "type": "HealthCareActivity"}, {"text": "tetralogy of Fallot", "type": "AnatomicalStructure"}, {"text": "aortic valve disease", "type": "BiologicFunction"}, {"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Circumferential fusiform aneurysm of the posterior circulation involving arterial branches or perforating vessels to the brain stem may be treated with this arterial reconstruction technique at different surgical times , using the self - expandable stent called LEO + and the flow - diverter device SILK , minimizing the risk of complications and failure of the endovascular technique , with the potential for arterial reconstruction with thrombosis of the aneurysmatic sac , as well as flow maintenance in the eloquent arteries , in this type of cerebral aneurysm .

Example answer:
{"entities": [{"text": "Circumferential", "type": "SpatialConcept"}, {"text": "fusiform aneurysm", "type": "AnatomicalStructure"}, {"text": "circulation", "type": "BiologicFunction"}, {"text": "arterial branches", "type": "AnatomicalStructure"}, {"text": "perforating", "type": "Finding"}, {"text": "vessels", "type": "AnatomicalStructure"}, {"text": "brain stem", "type": "AnatomicalStructure"}, {"text": "arterial", "type": "AnatomicalStructure"}, {"text": "reconstruction technique", "type": "HealthCareActivity"}, {"text": "self - expandable stent", "type": "MedicalDevice"}, {"text": "LEO +", "type": "MedicalDevice"}, {"text": "flow - diverter device", "type": "MedicalDevice"}, {"text": "SILK", "type": "MedicalDevice"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "technique", "type": "HealthCareActivity"}, {"text": "arterial reconstruction", "type": "HealthCareActivity"}, {"text": "thrombosis", "type": "BiologicFunction"}, {"text": "aneurysmatic sac", "type": "BiologicFunction"}, {"text": "eloquent arteries", "type": "AnatomicalStructure"}, {"text": "cerebral aneurysm", "type": "BiologicFunction"}]}

Example input:
Sentence: Out of 100 patients , indications for stenting were locally advanced disease not amenable to surgery ( 52 % ) , metastatic disease ( 35 % ) , CVA ( 1 % ) , cardiac and respiratory problem ( 8 % ) , un - willing for surgery in 5 % of patients .

Example answer:
{"entities": [{"text": "stenting", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "metastatic disease", "type": "BiologicFunction"}, {"text": "CVA", "type": "BiologicFunction"}, {"text": "respiratory problem", "type": "Finding"}]}

Example input:
Sentence: There were no complications during the procedure , nor in the long - term follow - up with full arterial vascular reconstruction , maintenance of cerebral perfusion and complete aneurysm occlusion at the 6 - and 12 - month angiographic follow - up .

Example answer:
{"entities": [{"text": "complications", "type": "BiologicFunction"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "arterial", "type": "AnatomicalStructure"}, {"text": "vascular", "type": "AnatomicalStructure"}, {"text": "reconstruction", "type": "HealthCareActivity"}, {"text": "aneurysm", "type": "BiologicFunction"}, {"text": "angiographic", "type": "HealthCareActivity"}]}

Example input:
Sentence: Two - stage reconstructive overlapping stent LEO + and SILK for treatment of intracranial circumferential fusiform aneurysms in the posterior circulation Intracranial circumferential fusiform aneurysms of the posterior circulation involving arterial branches or perforating vessels are difficult to treat .

Example answer:
{"entities": [{"text": "reconstructive", "type": "HealthCareActivity"}, {"text": "overlapping stent", "type": "MedicalDevice"}, {"text": "LEO +", "type": "MedicalDevice"}, {"text": "SILK", "type": "MedicalDevice"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "intracranial", "type": "SpatialConcept"}, {"text": "circumferential", "type": "SpatialConcept"}, {"text": "fusiform aneurysms", "type": "AnatomicalStructure"}, {"text": "circulation", "type": "BiologicFunction"}, {"text": "Intracranial", "type": "SpatialConcept"}, {"text": "arterial branches", "type": "AnatomicalStructure"}, {"text": "perforating", "type": "Finding"}, {"text": "vessels", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Angiographic follow - up was available for 174 patients ( 65 . 9 % ) , the incidence of recanalization was 5 . 7 % .

Example answer:
{"entities": [{"text": "Angiographic", "type": "HealthCareActivity"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "recanalization", "type": "HealthCareActivity"}]}

Example input:
Sentence: Progressive Occlusion and Recanalization after Endovascular Treatment for 287 Unruptured Small Aneurysms ( < 5 mm ) : A Single - Center 6 - Year Experience We aimed to investigate the effect of coiling for small unruptured intracranial aneurysms ( UIAs ) ﹤5 mm ) on progressive occlusio n and recanalization , and the dubious factors related to progressive occlusion and recanalization among UIAs without complete occlusion .

Example answer:
{"entities": [{"text": "Recanalization", "type": "HealthCareActivity"}, {"text": "Endovascular Treatment", "type": "HealthCareActivity"}, {"text": "Unruptured Small Aneurysms", "type": "BiologicFunction"}, {"text": "Single - Center", "type": "Organization"}, {"text": "Experience", "type": "BiologicFunction"}, {"text": "coiling", "type": "SpatialConcept"}, {"text": "unruptured intracranial aneurysms", "type": "BiologicFunction"}, {"text": "UIAs", "type": "BiologicFunction"}, {"text": "recanalization", "type": "HealthCareActivity"}]}

Input:
Sentence: There was no aneurysm recanalization nor intra - stent stenosis .

## Item MedMentions:test:605
Example input:
Sentence: The correlation ( rs ) between the scores based on the position of the labeling capsule and ROMs in the healthy group and the STC patients was .880 ( P < . 05 ) and .889 ( P < . 05 ) , respectively .

Example answer:
{"entities": [{"text": "ROMs", "type": "MedicalDevice"}, {"text": "STC", "type": "Finding"}]}

Example input:
Sentence: Trifecta and margins ischaemia complications ( MIC ) score achievement rates were used to assess the quality of surgery in both the expert and fellow groups .

Example answer:
{"entities": [{"text": "Trifecta", "type": "BiologicFunction"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "expert", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: It was included in this review only observational studies using either research diagnostic criteria ( RDC ) / TMD or DC / TMD indexes were selected .

Example answer:
{"entities": [{"text": "research diagnostic criteria", "type": "IntellectualProduct"}, {"text": "RDC", "type": "IntellectualProduct"}, {"text": "TMD", "type": "BiologicFunction"}, {"text": "DC", "type": "IntellectualProduct"}, {"text": "indexes", "type": "IntellectualProduct"}]}

Example input:
Sentence: The linkage disequilibrium analysis demonstrated that ITPR3 association with CSCC was independent of HLA - DRB1 alleles .

Example answer:
{"entities": [{"text": "linkage disequilibrium analysis", "type": "ResearchActivity"}, {"text": "ITPR3", "type": "AnatomicalStructure"}, {"text": "association", "type": "ResearchActivity"}, {"text": "CSCC", "type": "BiologicFunction"}, {"text": "HLA - DRB1", "type": "AnatomicalStructure"}, {"text": "alleles", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Interpretation of the expression was done by immunoreactive score of Remmele and Stegner ( IRS ) scoring method .

Example answer:
{"entities": [{"text": "Interpretation", "type": "IntellectualProduct"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "immunoreactive score of Remmele and Stegner ( IRS ) scoring method", "type": "ResearchActivity"}]}

Example input:
Sentence: Expectations scores were not related to age ( P = .36 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The RR correlated negatively with the visual dryness score of skin on the leg but correlated positively with water content of the stratum corneum on the arm .

Example answer:
{"entities": [{"text": "skin", "type": "BodySystem"}, {"text": "leg", "type": "AnatomicalStructure"}, {"text": "stratum corneum", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Very large significant correlation was obtained between the RPEres and score ( r = 0 . 83 ; ± 0 . 22 CL , p < 0 .

Example answer:
{"entities": [{"text": "RPEres", "type": "IntellectualProduct"}]}

Example input:
Sentence: The relationship between the WARPS / STAID and the ISS scores , measured using a Pearson r correlation coefficient , demonstrated a strong relationship : r = -0 .

Example answer:
{"entities": [{"text": "ISS scores", "type": "IntellectualProduct"}]}

Example input:
Sentence: The Dundee Ready Education Environment Measure ( DREEM ) was used to determine educational environment while self - rated perceived stress level was measured by the Depression Anxiety Stress Scale ( DASS ) .

Example answer:
{"entities": [{"text": "Dundee Ready Education Environment Measure", "type": "IntellectualProduct"}, {"text": "DREEM", "type": "IntellectualProduct"}, {"text": "self - rated", "type": "IntellectualProduct"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "stress", "type": "BiologicFunction"}, {"text": "Depression Anxiety Stress Scale", "type": "IntellectualProduct"}, {"text": "DASS", "type": "IntellectualProduct"}]}

Input:
Sentence: However , this was not associated with their DREEM scores .

## Item MedMentions:test:698
Example input:
Sentence: A total of 100 cases ( 38 males , 62 females ; age range - 17 - 76 years ; mean age - 43 . 6 years ) of acute SAH were studied .

Example answer:
{"entities": [{"text": "SAH", "type": "BiologicFunction"}, {"text": "studied", "type": "ResearchActivity"}]}

Example input:
Sentence: Neuroepithelial tumours were more frequent in patients with ages ranging from less than a year to 19 years , whereas metastatic tumours were prevalent in patients over 40 years of age .

Example answer:
{"entities": [{"text": "Neuroepithelial tumours", "type": "BiologicFunction"}, {"text": "metastatic tumours", "type": "BiologicFunction"}]}

Example input:
Sentence: As to age , 32 of 106 patients aged > 35 years and 5 of 33 younger patients ( 28 males and 9 females ) had recurrence .

Example answer:
{"entities": []}

Example input:
Sentence: Five hundred and twenty - five patients with AVF creation were stratified based on age < 65 , 65 - 75 , and > 75 years .

Example answer:
{"entities": [{"text": "AVF", "type": "AnatomicalStructure"}]}

Example input:
Sentence: ATV trough levels at week 9 were higher in controls ( median 438 ng / mL ) than in the switch arm ( median 124 ng / mL ) ( p = 0 . 003 ) , as was total bilirubin at week 48 ( median 38 μmol / L and 28 μmol / L , respectively ; p = 0 .

Example answer:
{"entities": [{"text": "ATV", "type": "Chemical"}, {"text": "median", "type": "SpatialConcept"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: The patients qualifying for MVD were generally healthier and younger , with a mean age ± SD of 57±14 , compared to those undergoing RF ( 75±15 ) or SRS ( 73±13 , p < 0 . 0001 ) .

Example answer:
{"entities": [{"text": "MVD", "type": "HealthCareActivity"}, {"text": "RF", "type": "HealthCareActivity"}, {"text": "SRS", "type": "HealthCareActivity"}]}

Example input:
Sentence: 05 ) , while the patients from CMUT and CMU1 were younger than the others ( p < 0 .

Example answer:
{"entities": [{"text": "CMUT", "type": "Organization"}, {"text": "CMU1", "type": "Organization"}]}

Example input:
Sentence: A total of 758 patients who presented following either snowmobile ( n = 87 ) , ATV - related ( n = 308 ) or dirtbike ( n = 363 ) - related trauma at our institution between 1996 and 2015 were retrospectively reviewed .

Example answer:
{"entities": [{"text": "snowmobile", "type": "InjuryOrPoisoning"}, {"text": "ATV - related", "type": "InjuryOrPoisoning"}, {"text": "dirtbike ( n = 363 ) - related trauma", "type": "InjuryOrPoisoning"}, {"text": "institution", "type": "Organization"}]}

Example input:
Sentence: Snowmobile and ATV patients had higher Injury Severity Score ( 11 . 3 , 9 . 6 ) than dirtbike patients ( 7 . 8 ) ( P = 0 .

Example answer:
{"entities": [{"text": "Injury Severity Score", "type": "IntellectualProduct"}]}

Example input:
Sentence: Patients with VWD were younger , 49 . 67 versus 57 . 30 years , Caucasian , 82 .

Example answer:
{"entities": [{"text": "VWD", "type": "BiologicFunction"}, {"text": "Caucasian", "type": "PopulationGroup"}]}

Input:
Sentence: ATV patients were found to be younger ( 11 .

## Item MedMentions:test:101
Example input:
Sentence: The biochemical methane potential ( BMP ) of five different algae ( Chlorella vulgaris ) / manure ( cattle ) mixtures showed that the mixture of 80 / 20 ( on VS basis ) resulted in the highest BMP value ( 431mL CH4 gVS ( - 1 ) ) , while the BMP of microalgae alone ( 100 / 0 ) was 415mL CH4 gVS ( - 1 ) .

Example answer:
{"entities": [{"text": "methane", "type": "Chemical"}, {"text": "algae", "type": "Eukaryote"}, {"text": "Chlorella vulgaris", "type": "Eukaryote"}, {"text": "cattle", "type": "Eukaryote"}, {"text": "CH4", "type": "Chemical"}, {"text": "microalgae", "type": "Eukaryote"}]}

Example input:
Sentence: Our results demonstrate that the treatment of 5 % HRW significantly decreased the ROS content , maintained biomass and polar growth morphology of mycelium , and decreased secondary metabolism under HAc - induced oxidative stress .

Example answer:
{"entities": [{"text": "HRW", "type": "Chemical"}, {"text": "ROS", "type": "Chemical"}, {"text": "polar growth", "type": "BiologicFunction"}, {"text": "mycelium", "type": "Eukaryote"}, {"text": "secondary metabolism", "type": "BiologicFunction"}, {"text": "HAc", "type": "Chemical"}, {"text": "induced", "type": "BiologicFunction"}, {"text": "oxidative stress", "type": "BiologicFunction"}]}

Example input:
Sentence: The strain 's growth patterns under various concentrations of H2 O2 and its scavenging properties towards hydroxyl radical ( 64 . 85 % ) and DPPH ( 84 . 97 % ) were also interesting properties .

Example answer:
{"entities": [{"text": "strain 's", "type": "Bacterium"}, {"text": "growth patterns", "type": "Finding"}, {"text": "H2 O2", "type": "Chemical"}, {"text": "scavenging properties", "type": "BiologicFunction"}, {"text": "hydroxyl radical", "type": "Chemical"}, {"text": "DPPH", "type": "Chemical"}]}

Example input:
Sentence: how nutrient enrichment ( i . e . , nitrogen availability ) affected the growth of Fucus vesiculosus , a foundational macroalgal species in the North Atlantic rocky intertidal zone , and found that nutrient -enriched algal blades showed a significant increase in tissue growth compared to individuals grown under ambient conditions .

Example answer:
{"entities": [{"text": "nutrient", "type": "Food"}, {"text": "nitrogen", "type": "Chemical"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "Fucus vesiculosus", "type": "Eukaryote"}, {"text": "macroalgal", "type": "Eukaryote"}, {"text": "species", "type": "Eukaryote"}, {"text": "North Atlantic rocky intertidal zone", "type": "SpatialConcept"}, {"text": "algal blades", "type": "IntellectualProduct"}, {"text": "tissue growth", "type": "BiologicFunction"}]}

Example input:
Sentence: MeHg accumulation in the brain causes histopathological alterations , neurobehavioral changes , and impairments to cognitive motor functions in mammalian models .

Example answer:
{"entities": [{"text": "MeHg", "type": "Chemical"}, {"text": "accumulation", "type": "Finding"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "motor functions", "type": "BiologicFunction"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "models", "type": "BiologicFunction"}]}

Example input:
Sentence: While there was a minimal effect of foliar water uptake on live fuel moisture , several species had lower xylem tension and greater photosynthetic rates after overnight fog treatments , especially Salvia leucophylla .

Example answer:
{"entities": [{"text": "foliar", "type": "Eukaryote"}, {"text": "water uptake", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "xylem", "type": "Eukaryote"}, {"text": "Salvia leucophylla", "type": "Eukaryote"}]}

Example input:
Sentence: We confirmed that the photosynthetic capacity and chlorophyll content was reduced by an ethylene treatment and that several abiotic stress conditions could stimulate cell elongation in an ethylene -dependent manner .

Example answer:
{"entities": [{"text": "chlorophyll", "type": "Chemical"}, {"text": "ethylene", "type": "Chemical"}, {"text": "abiotic stress conditions", "type": "BiologicFunction"}, {"text": "stimulate", "type": "HealthCareActivity"}, {"text": "cell elongation", "type": "BiologicFunction"}]}

Example input:
Sentence: Data suggest that the cells were able to cope with subnanomolar MeHg exposure , but this tolerance resulted in a significant cost to the cell energy and reserve metabolism as well as ample changes in the nutrition and motility of C .

Example answer:
{"entities": [{"text": "cells", "type": "AnatomicalStructure"}, {"text": "able to cope", "type": "Finding"}, {"text": "MeHg", "type": "Chemical"}, {"text": "cell energy and reserve metabolism", "type": "BiologicFunction"}, {"text": "nutrition", "type": "BiologicFunction"}, {"text": "motility", "type": "BiologicFunction"}, {"text": "C .", "type": "Eukaryote"}]}

Example input:
Sentence: At the molecular level , MeHg significantly dysregulated the expression of genes involved in motility , energy metabolism , lipid metabolism , metal transport , and antioxidant enzymes .

Example answer:
{"entities": [{"text": "MeHg", "type": "Chemical"}, {"text": "dysregulated", "type": "BiologicFunction"}, {"text": "expression of genes", "type": "BiologicFunction"}, {"text": "motility", "type": "BiologicFunction"}, {"text": "energy metabolism", "type": "BiologicFunction"}, {"text": "lipid metabolism", "type": "BiologicFunction"}, {"text": "metal transport", "type": "BiologicFunction"}, {"text": "antioxidant", "type": "Chemical"}, {"text": "enzymes", "type": "Chemical"}]}

Example input:
Sentence: Transcriptomic and Physiological Responses of the Green Microalga Chlamydomonas reinhardtii during Short - Term Exposure to Subnanomolar Methylmercury Concentrations The effects of short - term exposure to subnanomolar methyl - mercury ( MeHg ) concentrations , representative of contaminated environments , on the microalga Chlamydomonas reinhardtii were assessed using both physiological end points and gene expression analysis .

Example answer:
{"entities": [{"text": "Transcriptomic", "type": "BiologicFunction"}, {"text": "Physiological Responses", "type": "BiologicFunction"}, {"text": "Green Microalga", "type": "Eukaryote"}, {"text": "Chlamydomonas reinhardtii", "type": "Eukaryote"}, {"text": "Methylmercury", "type": "Chemical"}, {"text": "methyl - mercury", "type": "Chemical"}, {"text": "MeHg", "type": "Chemical"}, {"text": "environments", "type": "SpatialConcept"}, {"text": "microalga", "type": "Eukaryote"}, {"text": "physiological end points", "type": "BiologicFunction"}, {"text": "gene expression analysis", "type": "ResearchActivity"}]}

Input:
Sentence: MeHg bioaccumulated and induced significant increase of the photosynthesis efficiency , while the algal growth , oxidative stress , and chlorophyll fluorescence were unaffected .

## Item MedMentions:test:643
Example input:
Sentence: In addition , using this technique will give good aesthetic and functional results .

Example answer:
{"entities": []}

Example input:
Sentence: Respondents then chose among procedures that differed regarding treatment modalities , the potential for treatment -related complications , the likelihood of recurrence , provider case volume , and distance needed to travel for treatment .

Example answer:
{"entities": [{"text": "Respondents", "type": "PopulationGroup"}, {"text": "procedures", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "provider", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Optimal treatment approaches in this sizable patient subgroup should be the subject of future prospective studies .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "subgroup", "type": "IntellectualProduct"}, {"text": "prospective studies", "type": "ResearchActivity"}]}

Example input:
Sentence: Survival improved with the evolution of the technique , although this was not statistically significant due to the overall low rate of further revision .

Example answer:
{"entities": [{"text": "revision", "type": "HealthCareActivity"}]}

Example input:
Sentence: Establishing and validating efficient dysphagia - optimised radiotherapy techniques is , therefore , of paramount importance in an era where health - related quality of life measures are increasingly influential determinants of curative management strategies , particularly as the incidence of good prognosis , human papillomavirus -driven pharyngeal cancer in younger patients continues to rise .

Example answer:
{"entities": [{"text": "dysphagia", "type": "BiologicFunction"}, {"text": "radiotherapy techniques", "type": "HealthCareActivity"}, {"text": "prognosis", "type": "HealthCareActivity"}, {"text": "human papillomavirus", "type": "Virus"}, {"text": "pharyngeal cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: The relative advantages and disadvantages of the approaches to hysterectomy should be discussed in the context of the patient ' s values and preferences , and the patient and health care provider should together determine the best course of action after this discussion .

Example answer:
{"entities": [{"text": "hysterectomy", "type": "HealthCareActivity"}, {"text": "health care provider", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: As proper selection of imaging modality is very important for planning the treatment , various advances in this area are required .

Example answer:
{"entities": [{"text": "planning the treatment", "type": "IntellectualProduct"}]}

Example input:
Sentence: An aggressive diagnostic approach is necessary in these patients , who can benefit most from an accurate diagnosis .

Example answer:
{"entities": [{"text": "diagnostic approach", "type": "HealthCareActivity"}, {"text": "diagnosis", "type": "HealthCareActivity"}]}

Example input:
Sentence: The proposed method relies on post processing of clinical projection images , and does not require patient specific optimisation .

Example answer:
{"entities": [{"text": "method", "type": "IntellectualProduct"}, {"text": "post processing", "type": "IntellectualProduct"}]}

Example input:
Sentence: There is a definite need for evidence - based strategies to optimise results of these types of surgery .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}]}

Input:
Sentence: As regards optimizing the results , patient selection for either technique could prove essential .
