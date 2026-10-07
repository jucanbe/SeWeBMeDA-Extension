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

## Item MedMentions:test:2830
Example input:
Sentence: This was linked to persistent IFN - γ secretion upon repeated iNKT cell stimulation and a restoration of the dynamic antigen - induced motility arrest as observed by intravital microscopy , thereby showing alleviation of iNKT cell anergy .

Example answer:
{"entities": [{"text": "IFN - γ secretion", "type": "BiologicFunction"}, {"text": "iNKT", "type": "AnatomicalStructure"}, {"text": "cell stimulation", "type": "BiologicFunction"}, {"text": "antigen", "type": "Chemical"}, {"text": "motility arrest", "type": "BiologicFunction"}, {"text": "intravital microscopy", "type": "HealthCareActivity"}, {"text": "alleviation of iNKT cell anergy", "type": "BiologicFunction"}]}

Example input:
Sentence: The drug binding and induction of cytotoxic degranulation was CD133 + specific and the anti - cancer activity was improved by integrating the interleukin ( IL ) - 15 cross linker .

Example answer:
{"entities": [{"text": "drug binding", "type": "BiologicFunction"}, {"text": "degranulation", "type": "BiologicFunction"}, {"text": "CD133 +", "type": "Chemical"}, {"text": "anti - cancer activity", "type": "Finding"}, {"text": "interleukin ( IL ) - 15", "type": "Chemical"}]}

Example input:
Sentence: Additionally , our analysis showed that the Grpr - Cre population expresses Vglut2 mRNA , and mice ablated of Vglut2 in Grpr - Cre cells ( Vglut2 - lox ; Grpr - Cre mice ) displayed less spontaneous itch and attenuated responses to both histaminergic and nonhistaminergic agents .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "Grpr - Cre", "type": "AnatomicalStructure"}, {"text": "expresses", "type": "BiologicFunction"}, {"text": "Vglut2", "type": "Chemical"}, {"text": "mRNA", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "Grpr - Cre cells", "type": "AnatomicalStructure"}, {"text": "lox", "type": "Chemical"}, {"text": "Grpr - Cre mice", "type": "AnatomicalStructure"}, {"text": "itch", "type": "Finding"}, {"text": "histaminergic", "type": "Chemical"}, {"text": "nonhistaminergic agents", "type": "Chemical"}]}

Example input:
Sentence: Mathematical modeling provided estimates of receptor aggregation kinetics based on FcεRI occupancy with IgE and allergen dose .

Example answer:
{"entities": [{"text": "Mathematical modeling", "type": "IntellectualProduct"}, {"text": "receptor aggregation", "type": "BiologicFunction"}, {"text": "FcεRI", "type": "Chemical"}, {"text": "IgE", "type": "Chemical"}, {"text": "allergen", "type": "Chemical"}]}

Example input:
Sentence: Moreover , only three times of μEPIT over two weeks could sufficiently inhibit allergen - specific IgE responses in mice suffering OVA -induced airway hyperresponsivness ( AHR ) , which was unattainable by eight times of SCIT over three weeks .

Example answer:
{"entities": [{"text": "μEPIT", "type": "HealthCareActivity"}, {"text": "allergen - specific IgE", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "OVA", "type": "Chemical"}, {"text": "airway hyperresponsivness", "type": "BiologicFunction"}, {"text": "AHR", "type": "BiologicFunction"}, {"text": "SCIT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Pen a 1 - specific IgE was affinity purified from shrimp - positive plasma .

Example answer:
{"entities": [{"text": "Pen a 1", "type": "Chemical"}, {"text": "specific IgE", "type": "Chemical"}, {"text": "shrimp", "type": "Eukaryote"}, {"text": "positive", "type": "Finding"}, {"text": "plasma", "type": "BodySubstance"}]}

Example input:
Sentence: These fragments have reduced dimerization capacity , compete with intact Pen a 1 for binding to IgE - FcεRI complexes , and represent a starting point for the design of promising hypoallergens for immunotherapy .

Example answer:
{"entities": [{"text": "dimerization", "type": "BiologicFunction"}, {"text": "Pen a 1", "type": "Chemical"}, {"text": "IgE", "type": "Chemical"}, {"text": "FcεRI", "type": "Chemical"}, {"text": "complexes", "type": "Chemical"}, {"text": "hypoallergens", "type": "Chemical"}, {"text": "immunotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Cells primed with a range of Pen a 1 - specific IgE and challenged with Pen a 1 showed a bell - shaped dose response for secretion , with optimal Pen a 1 doses of 0 . 1 - 10 ng / ml .

Example answer:
{"entities": [{"text": "Pen a 1", "type": "Chemical"}, {"text": "specific IgE", "type": "Chemical"}, {"text": "response for secretion", "type": "BiologicFunction"}]}

Example input:
Sentence: Allergen Valency , Dose , and FcεRI Occupancy Set Thresholds for Secretory Responses to Pen a 1 and Motivate Design of Hypoallergens Ag -mediated crosslinking of IgE - FcεRI complexes activates mast cells and basophils , initiating the allergic response .

Example answer:
{"entities": [{"text": "Allergen", "type": "Chemical"}, {"text": "FcεRI", "type": "Chemical"}, {"text": "Secretory Responses", "type": "BiologicFunction"}, {"text": "Pen a 1", "type": "Chemical"}, {"text": "Hypoallergens", "type": "Chemical"}, {"text": "Ag", "type": "Chemical"}, {"text": "IgE", "type": "Chemical"}, {"text": "complexes", "type": "Chemical"}, {"text": "mast cells", "type": "AnatomicalStructure"}, {"text": "basophils", "type": "AnatomicalStructure"}, {"text": "allergic response", "type": "BiologicFunction"}]}

Example input:
Sentence: Maximal degranulation was elicited when ∼2700 I gE - FcεRI complexes were occupied with specific IgE and challenged with Pen a 1 ( IgE epitope valency of ≥8 ) , although measurable responses were achieved when only a few hundred FcεRI were occupied .

Example answer:
{"entities": [{"text": "gE", "type": "Chemical"}, {"text": "FcεRI", "type": "Chemical"}, {"text": "complexes", "type": "Chemical"}, {"text": "specific IgE", "type": "Chemical"}, {"text": "Pen a 1", "type": "Chemical"}, {"text": "IgE", "type": "Chemical"}, {"text": "epitope", "type": "Chemical"}]}

Input:
Sentence: We report that degranulation is linked to the number of FcεRI occupied with allergen - specific IgE , as well as the dose and valency of Pen a 1 .

## Item MedMentions:test:2637
Example input:
Sentence: Across curvature s , legibility decreased by 2 % - 8 % , whereas perceived visual fatigue increased by 22 % during the second task set .

Example answer:
{"entities": [{"text": "curvature", "type": "SpatialConcept"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "visual fatigue", "type": "BiologicFunction"}]}

Example input:
Sentence: These results suggest that whereas gaze - cued orienting of attention can be driven by both global and local visual information , global visual information determines the speed of behavioral responses towards other entities appearing in the surrounding of gaze cue stimuli .

Example answer:
{"entities": [{"text": "gaze", "type": "Finding"}, {"text": "attention", "type": "BiologicFunction"}, {"text": "global", "type": "SpatialConcept"}, {"text": "local", "type": "SpatialConcept"}, {"text": "surrounding", "type": "SpatialConcept"}]}

Example input:
Sentence: We tracked eye gaze and behavioral performance in two task conditions : one with and one without local interference from background noise elements .

Example answer:
{"entities": [{"text": "eye gaze", "type": "Finding"}, {"text": "local interference", "type": "BiologicFunction"}]}

Example input:
Sentence: The two task sets induced an increase of 102 % in the eye complaint score and a decrease of 0 .

Example answer:
{"entities": []}

Example input:
Sentence: We found that a model which included attentional load and task experience as predictors had the best model fit while adding performance as a predictor to this model reduced the overall model fit .

Example answer:
{"entities": [{"text": "model", "type": "IntellectualProduct"}, {"text": "attentional load", "type": "IntellectualProduct"}, {"text": "experience", "type": "BiologicFunction"}, {"text": "performance", "type": "HealthCareActivity"}]}

Example input:
Sentence: To manipulate attentional load , participants covertly tracked between zero and five objects among several randomly moving objects on a computer screen .

Example answer:
{"entities": [{"text": "attentional load", "type": "IntellectualProduct"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "tracked", "type": "SpatialConcept"}]}

Example input:
Sentence: Overall , results suggest that pupillometry provides a viable metric for precisely assessing attentional load and task experience in visuospatial tasks .

Example answer:
{"entities": [{"text": "pupillometry", "type": "HealthCareActivity"}, {"text": "attentional load", "type": "IntellectualProduct"}, {"text": "experience", "type": "BiologicFunction"}]}

Example input:
Sentence: We found that pupil sizes increased with each increment in attentional load .

Example answer:
{"entities": [{"text": "pupil sizes", "type": "ClinicalAttribute"}, {"text": "attentional load", "type": "IntellectualProduct"}]}

Example input:
Sentence: We compared the model fit for predicting pupil size modulations using attentional load , task experience , and task performance as predictors .

Example answer:
{"entities": [{"text": "pupil size", "type": "ClinicalAttribute"}, {"text": "modulations", "type": "SpatialConcept"}, {"text": "attentional load", "type": "IntellectualProduct"}, {"text": "experience", "type": "BiologicFunction"}, {"text": "task performance", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , studies relating changes in attentional load and task experience on a finer scale to pupil size modulations are scarce .

Example answer:
{"entities": [{"text": "attentional load", "type": "IntellectualProduct"}, {"text": "experience", "type": "BiologicFunction"}, {"text": "scale", "type": "IntellectualProduct"}, {"text": "pupil size", "type": "ClinicalAttribute"}, {"text": "modulations", "type": "SpatialConcept"}]}

Input:
Sentence: Pupil Sizes Scale with Attentional Load and Task Experience in a Multiple Object Tracking Task Previous studies have related changes in attentional load to pupil size modulations .

## Item MedMentions:test:2710
Example input:
Sentence: Intrinsic rifamycin resistance of Mycobacterium abscessus is mediated by ADP - ribosyltransferase MAB _ 0591 Rifampicin , a potent first - line TB drug of the rifamycin group , shows only little activity against the emerging pathogen Mycobacterium abscessus .

Example answer:
{"entities": [{"text": "Intrinsic", "type": "SpatialConcept"}, {"text": "rifamycin", "type": "Chemical"}, {"text": "Mycobacterium abscessus", "type": "Bacterium"}, {"text": "ADP - ribosyltransferase", "type": "Chemical"}, {"text": "MAB _ 0591", "type": "AnatomicalStructure"}, {"text": "Rifampicin", "type": "Chemical"}, {"text": "TB drug", "type": "Chemical"}, {"text": "rifamycin group", "type": "Chemical"}]}

Example input:
Sentence: The aim of this study was to investigate the role of the MAB _ 0591 ( arrMab ) - encoded rifampicin ADP - ribosyltransferase ( Arr _ Mab ) in innate high - level rifampicin resistance in M .

Example answer:
{"entities": [{"text": "MAB _ 0591", "type": "AnatomicalStructure"}, {"text": "arrMab", "type": "AnatomicalStructure"}, {"text": "rifampicin", "type": "Chemical"}, {"text": "ADP - ribosyltransferase", "type": "Chemical"}, {"text": "Arr _ Mab", "type": "Chemical"}, {"text": "M .", "type": "Bacterium"}]}

Example input:
Sentence: Simultaneous quantification of isoniazid , rifampicin , ethambutol and pyrazinamide by liquid chromatography / tandem mass spectrometry A remediable cause of poor treatment response in drug - susceptible tuberculosis ( TB ) patients may be low plasma levels of one or more of the first - line anti - TB drugs .

Example answer:
{"entities": [{"text": "isoniazid", "type": "Chemical"}, {"text": "rifampicin", "type": "Chemical"}, {"text": "ethambutol", "type": "Chemical"}, {"text": "pyrazinamide", "type": "Chemical"}, {"text": "liquid chromatography", "type": "HealthCareActivity"}, {"text": "remediable", "type": "HealthCareActivity"}, {"text": "poor treatment response", "type": "Finding"}, {"text": "drug", "type": "Chemical"}, {"text": "tuberculosis", "type": "BiologicFunction"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "plasma", "type": "BodySubstance"}, {"text": "anti - TB drugs", "type": "Chemical"}]}

Example input:
Sentence: Rifampicin - resistance of the strains from the 30 culture - positive cases of extra - pulmonary tuberculosis ( 20 . 0 % , 6 / 30 ) exhibited agreement with GeneXpert MTB / RIF test .

Example answer:
{"entities": [{"text": "Rifampicin - resistance", "type": "BiologicFunction"}, {"text": "culture - positive cases", "type": "Finding"}, {"text": "extra - pulmonary tuberculosis", "type": "BiologicFunction"}, {"text": "GeneXpert MTB / RIF test", "type": "HealthCareActivity"}]}

Example input:
Sentence: Following adaptation to DDAC , a threefold increase in the minimum inhibitory concentration ( MIC ) values for this biocide was observed in 48 % of the Escherichia coli and Listeria monocytogenes strains , and 3 % of the Salmonella strains .

Example answer:
{"entities": [{"text": "adaptation", "type": "BiologicFunction"}, {"text": "DDAC", "type": "Chemical"}, {"text": "minimum inhibitory concentration", "type": "HealthCareActivity"}, {"text": "MIC", "type": "HealthCareActivity"}, {"text": "biocide", "type": "Chemical"}, {"text": "Escherichia coli", "type": "Bacterium"}, {"text": "Listeria monocytogenes strains", "type": "Bacterium"}, {"text": "Salmonella strains", "type": "Bacterium"}]}

Example input:
Sentence: A significant reduction ( p < 0 , 001 - 0 , 02 ) in susceptibility for the strains after 2009 was noted towards piperacillin ( 100 % vs 50 % ) , ceftazidime ( 100 % / 77 . 3 % ) , cefepime ( 97 . 9 % / 68 . 2 % ) , amikacin ( 100 % / 63 .

Example answer:
{"entities": [{"text": "piperacillin", "type": "Chemical"}, {"text": "ceftazidime", "type": "Chemical"}, {"text": "cefepime", "type": "Chemical"}, {"text": "amikacin", "type": "Chemical"}]}

Example input:
Sentence: All patients had MIC < 2 μg / mL , the vancomycin susceptibility threshold .

Example answer:
{"entities": [{"text": "MIC", "type": "HealthCareActivity"}, {"text": "vancomycin", "type": "Chemical"}]}

Example input:
Sentence: The rifamycin WT phenotype was restored after complementation of the M .

Example answer:
{"entities": [{"text": "rifamycin", "type": "Chemical"}, {"text": "WT", "type": "AnatomicalStructure"}, {"text": "M .", "type": "Bacterium"}]}

Example input:
Sentence: abscessus ΔarrMab mutant with arrMab Further MIC data demonstrated that a C25 modification increases rifamycin activity in WT M .

Example answer:
{"entities": [{"text": "abscessus", "type": "Bacterium"}, {"text": "ΔarrMab mutant", "type": "AnatomicalStructure"}, {"text": "arrMab", "type": "Chemical"}, {"text": "MIC data", "type": "Finding"}, {"text": "C25", "type": "Chemical"}, {"text": "modification", "type": "Finding"}, {"text": "rifamycin", "type": "Chemical"}, {"text": "WT", "type": "AnatomicalStructure"}, {"text": "M .", "type": "Bacterium"}]}

Example input:
Sentence: tuberculosis Rifamycin MIC values were consistently lower for the M .

Example answer:
{"entities": [{"text": "tuberculosis", "type": "Bacterium"}, {"text": "Rifamycin", "type": "Chemical"}, {"text": "MIC values", "type": "Finding"}, {"text": "M .", "type": "Bacterium"}]}

Input:
Sentence: MIC assays were used to study susceptibility to rifampicin and C25 carbamate -modified rifamycin derivatives .

## Item MedMentions:test:2668
Example input:
Sentence: Moreover , the tumor - targeting ability of the nanocomplexes was demonstrated , both in vitro by confocal microscopy and in vivo by fluorescence imaging , to be driven by an inherent property of the residual PBA .

Example answer:
{"entities": [{"text": "tumor", "type": "BiologicFunction"}, {"text": "nanocomplexes", "type": "Chemical"}, {"text": "confocal microscopy", "type": "HealthCareActivity"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "fluorescence imaging", "type": "HealthCareActivity"}, {"text": "PBA", "type": "Chemical"}]}

Example input:
Sentence: Subsequently , the photodynamic therapy efficiency of various controlled mixtures was assessed using multicellular spheroids when a photosensitizer , pheophorbide a , was encapsulated in the polymer self - assemblies .

Example answer:
{"entities": [{"text": "photodynamic therapy", "type": "HealthCareActivity"}, {"text": "spheroids", "type": "Finding"}, {"text": "photosensitizer", "type": "Chemical"}, {"text": "pheophorbide a", "type": "Chemical"}, {"text": "polymer", "type": "Chemical"}]}

Example input:
Sentence: Fluorescently labeled pep5 , monitored by real time confocal microscopy , entered the MDA - MB - 231 cells 3min after application and localized to the nucleus and cytoplasm .

Example answer:
{"entities": [{"text": "Fluorescently labeled", "type": "HealthCareActivity"}, {"text": "pep5", "type": "Chemical"}, {"text": "real time confocal microscopy", "type": "HealthCareActivity"}, {"text": "MDA - MB - 231", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "localized", "type": "SpatialConcept"}, {"text": "nucleus", "type": "AnatomicalStructure"}, {"text": "cytoplasm", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We showed that the formulation Pc9 - T1107 was efficient to reduce cell viability after photodynamic treatment both in 2D cultures ( IC50 10±2nM ) as well as in CT26 spheroids ( IC50 370±11nM ) .

Example answer:
{"entities": [{"text": "Pc9", "type": "Chemical"}, {"text": "T1107", "type": "Chemical"}, {"text": "cell viability", "type": "BiologicFunction"}, {"text": "photodynamic treatment", "type": "HealthCareActivity"}, {"text": "2D", "type": "SpatialConcept"}, {"text": "cultures", "type": "HealthCareActivity"}, {"text": "CT26 spheroids", "type": "AnatomicalStructure"}]}

Example input:
Sentence: By using confocal microscopy , we observed that SET can strongly block the formation of T‑P complex i n vitro .

Example answer:
{"entities": [{"text": "confocal microscopy", "type": "HealthCareActivity"}, {"text": "SET", "type": "Chemical"}, {"text": "T‑P complex", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In this scenario , we applied the multifunctional Pluronic P123 / F127 mixed micelles for Verteporfin -mediated photodynamic therapy in PC3 and MCF - 7 cancer cells .

Example answer:
{"entities": [{"text": "multifunctional Pluronic P123", "type": "Chemical"}, {"text": "F127", "type": "Chemical"}, {"text": "micelles", "type": "Chemical"}, {"text": "Verteporfin", "type": "Chemical"}, {"text": "photodynamic therapy", "type": "HealthCareActivity"}, {"text": "PC3", "type": "AnatomicalStructure"}, {"text": "MCF - 7 cancer cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Multifunctional theranostic Pluronic mixed micelles improve targeted photoactivity of Verteporfin in cancer cells Nanotechnology development provides new strategies to treat cancer by integration of different treatment modalities in a single multifunctional nanoparticle .

Example answer:
{"entities": [{"text": "Multifunctional theranostic Pluronic", "type": "Chemical"}, {"text": "micelles", "type": "Chemical"}, {"text": "improve", "type": "Finding"}, {"text": "Verteporfin", "type": "Chemical"}, {"text": "cancer cells", "type": "AnatomicalStructure"}, {"text": "cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: These results point Verteporfin -loaded multifunctional micelles as a promising tool to further developments in photodynamic therapy of cancer .

Example answer:
{"entities": [{"text": "Verteporfin", "type": "Chemical"}, {"text": "multifunctional micelles", "type": "Chemical"}, {"text": "photodynamic therapy", "type": "HealthCareActivity"}, {"text": "cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Formulations were not toxic in the dark condition , but showed high Verteporfin -induced phototoxicity against both cancer cell lines at low drug and light doses .

Example answer:
{"entities": [{"text": "Formulations", "type": "Chemical"}, {"text": "Verteporfin", "type": "Chemical"}, {"text": "phototoxicity", "type": "BiologicFunction"}, {"text": "cancer cell lines", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Multifunctional Pluronics formed spherical nanoparticulated micelles that efficiently encapsulated the photosensitizer Verteporfin maintaining its favorable photophysical properties .

Example answer:
{"entities": [{"text": "Multifunctional Pluronics", "type": "Chemical"}, {"text": "spherical", "type": "SpatialConcept"}, {"text": "nanoparticulated micelles", "type": "Chemical"}, {"text": "photosensitizer", "type": "Chemical"}, {"text": "Verteporfin", "type": "Chemical"}]}

Input:
Sentence: Confocal microscopy studies demonstrated a larger intracellular distribution of the formulation and photosensitizer , which could drive Verteporfin to act on multiple cell sites .

## Item MedMentions:test:2936
Example input:
Sentence: 27 . 7±4 . 8 % ; 23 . 0±1 . 7 vs . 46 . 5±3 . 4 % ; and 17 . 6±1 .

Example answer:
{"entities": []}

Example input:
Sentence: The average preoperative UCLA score in the nerve - release group was 7 . 91 , and final follow - up average was 27 . 86 ; average 3 . 05 grades of strength were recovered .

Example answer:
{"entities": [{"text": "nerve - release group", "type": "PopulationGroup"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: 6 % patients in the β - blocker group and 13 . 6 % patients in the no - β - blocker group ( hazard ratio [ HR ] : 0 . 81 , 95 % confidence interval [ CI ] : 0 . 61 - 1 . 08 ; P = 0 . 15 ) .

Example answer:
{"entities": [{"text": "β - blocker", "type": "Chemical"}]}

Example input:
Sentence: 3 % for heating block , 81 .

Example answer:
{"entities": []}

Example input:
Sentence: All presented with symmetric weakness , 17 ( 56 . 7 % ) patients having predominantly proximal weakness , neck or truncal weakness in 6 ( 20 % ) , hyporeflexia in 12 ( 40 % ) , with mean Medical Research Council ( MRC ) sum score of 46 . 67 ± 6 .

Example answer:
{"entities": [{"text": "symmetric weakness", "type": "Finding"}, {"text": "proximal weakness", "type": "Finding"}, {"text": "neck", "type": "SpatialConcept"}, {"text": "truncal weakness", "type": "Finding"}, {"text": "hyporeflexia", "type": "Finding"}]}

Example input:
Sentence: 9 % ( 99 / 148 ) , with 7 ( 4 . 7 % ) , 92 ( 62 . 2 % ) , 36 ( 24 . 3 % ) , and 13 ( 8 . 8 % ) cases showing complete response , partial response , no change , and progressive disease , respectively .

Example answer:
{"entities": [{"text": "response", "type": "ClinicalAttribute"}, {"text": "no change", "type": "Finding"}, {"text": "progressive disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Twenty - eight ( 62 . 2 % ) and 18 ( 40 .

Example answer:
{"entities": []}

Example input:
Sentence: Twenty - four ( 54 . 5 % ) patients had normal activity , 3 ( 6 . 8 % ) had occasional discomfort , 2 ( 4 . 5 % ) had pain impairing function , 7 ( 15 .

Example answer:
{"entities": [{"text": "occasional discomfort", "type": "Finding"}, {"text": "pain impairing function", "type": "BiologicFunction"}]}

Example input:
Sentence: Of the 98 patients , 45 received general anesthesia , and 53 received regional anesthesia with a single - shot peripheral nerve block .

Example answer:
{"entities": [{"text": "general anesthesia", "type": "HealthCareActivity"}, {"text": "peripheral nerve block", "type": "HealthCareActivity"}]}

Example input:
Sentence: Sixty - five percent also received regional or local anesthesia consisting of caudal block in 79 .

Example answer:
{"entities": [{"text": "regional", "type": "HealthCareActivity"}, {"text": "local anesthesia", "type": "HealthCareActivity"}, {"text": "caudal block", "type": "HealthCareActivity"}]}

Input:
Sentence: 23 % or nerve block in 20 .

## Item MedMentions:test:2758
Example input:
Sentence: Colonic anastomosis leakage had the highest fractional complication burden in both groups .

Example answer:
{"entities": [{"text": "Colonic anastomosis", "type": "HealthCareActivity"}, {"text": "leakage", "type": "BiologicFunction"}, {"text": "groups", "type": "PopulationGroup"}]}

Example input:
Sentence: We sought to investigate metastases in the gastrocolic ligament in colon cancer close to the hepatic flexure .

Example answer:
{"entities": [{"text": "metastases", "type": "BiologicFunction"}, {"text": "gastrocolic ligament", "type": "AnatomicalStructure"}, {"text": "colon cancer", "type": "BiologicFunction"}, {"text": "hepatic flexure", "type": "SpatialConcept"}]}

Example input:
Sentence: Gastroepiploic , infrapyloric , and superficial pancreatic head lymph node metastases in the gastrocolic ligament have been reported for colon cancer close to the hepatic flexure .

Example answer:
{"entities": [{"text": "Gastroepiploic", "type": "AnatomicalStructure"}, {"text": "infrapyloric", "type": "AnatomicalStructure"}, {"text": "superficial pancreatic head lymph node", "type": "AnatomicalStructure"}, {"text": "metastases", "type": "BiologicFunction"}, {"text": "gastrocolic ligament", "type": "AnatomicalStructure"}, {"text": "colon cancer", "type": "BiologicFunction"}, {"text": "hepatic flexure", "type": "SpatialConcept"}]}

Example input:
Sentence: The combined use at different surgical times of the self - expandable stent and flow - diverter device was technically successful in both patients .

Example answer:
{"entities": [{"text": "self - expandable stent", "type": "MedicalDevice"}, {"text": "flow - diverter device", "type": "MedicalDevice"}]}

Example input:
Sentence: Metastases in the gastrocolic ligament occurred in 9 % of patients with T2 or deeper invasive colon cancer close to the hepatic flexure .

Example answer:
{"entities": [{"text": "Metastases", "type": "BiologicFunction"}, {"text": "gastrocolic ligament", "type": "AnatomicalStructure"}, {"text": "T2", "type": "Finding"}, {"text": "colon cancer", "type": "BiologicFunction"}, {"text": "hepatic flexure", "type": "SpatialConcept"}]}

Example input:
Sentence: Out of 100 patients , indications for stenting were locally advanced disease not amenable to surgery ( 52 % ) , metastatic disease ( 35 % ) , CVA ( 1 % ) , cardiac and respiratory problem ( 8 % ) , un - willing for surgery in 5 % of patients .

Example answer:
{"entities": [{"text": "stenting", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "metastatic disease", "type": "BiologicFunction"}, {"text": "CVA", "type": "BiologicFunction"}, {"text": "respiratory problem", "type": "Finding"}]}

Example input:
Sentence: The aim of our study was to demonstrate the safety and efficacy of the use of SEMSs as BTS in selected patients with acute colonic malignant obstructions .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "safety", "type": "HealthCareActivity"}, {"text": "SEMSs", "type": "MedicalDevice"}, {"text": "acute colonic malignant obstructions", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Our experience shows that SEMS insertion is a safe and effective technique in selected patients with colonic malignant obstruction ; the reduction in hospital stay and short - term complications in BG is an important cost - saving aim .

Example answer:
{"entities": [{"text": "experience", "type": "BiologicFunction"}, {"text": "SEMS insertion", "type": "HealthCareActivity"}, {"text": "colonic malignant obstruction", "type": "AnatomicalStructure"}, {"text": "complications", "type": "BiologicFunction"}, {"text": "BG", "type": "PopulationGroup"}]}

Example input:
Sentence: In the last decades , in addition to surgery , self - expanding metallic stents ( SEMSs ) are available both as a bridge to surgery ( BTS ) or palliation .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "self - expanding metallic stents", "type": "MedicalDevice"}, {"text": "( SEMSs )", "type": "MedicalDevice"}, {"text": "palliation", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: In total , 125 patients with malignant colonic obstruction who underwent emergency surgery or stent insertion were retrospectively enrolled in our study ; 62 patients underwent surgery initially , whereas 62 were subjected to stenting as BTS .

Example answer:
{"entities": [{"text": "malignant colonic obstruction", "type": "AnatomicalStructure"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "stent insertion", "type": "HealthCareActivity"}, {"text": "enrolled", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "stenting", "type": "HealthCareActivity"}]}

Input:
Sentence: Colonic acute malignant obstructions : effectiveness of self - expanding metallic stent as bridge to surgery Bowel obstruction is a frequent event in patients with adenocarcinoma , affecting , in some series , almost one - third of the patients .

## Item MedMentions:test:2703
Example input:
Sentence: It is widely known that disruption of the BBB occurs in various neurodegenerative diseases , including Alzheimer 's disease ( AD ) .

Example answer:
{"entities": [{"text": "disruption of the BBB", "type": "HealthCareActivity"}, {"text": "neurodegenerative diseases", "type": "BiologicFunction"}, {"text": "Alzheimer 's disease", "type": "BiologicFunction"}, {"text": "AD", "type": "BiologicFunction"}]}

Example input:
Sentence: Intravascular Inflammation Triggers Intracerebral Activated Microglia and Contributes to Secondary Brain Injury After Experimental Subarachnoid Hemorrhage ( eSAH ) Activation of innate immunity contributes to secondary brain injury after experimental subarachnoid hemorrhage ( eSAH ) .

Example answer:
{"entities": [{"text": "Intravascular", "type": "SpatialConcept"}, {"text": "Inflammation", "type": "BiologicFunction"}, {"text": "Intracerebral", "type": "SpatialConcept"}, {"text": "Microglia", "type": "AnatomicalStructure"}, {"text": "Secondary Brain Injury", "type": "InjuryOrPoisoning"}, {"text": "Subarachnoid Hemorrhage", "type": "BiologicFunction"}, {"text": "eSAH", "type": "BiologicFunction"}, {"text": "secondary brain injury", "type": "InjuryOrPoisoning"}, {"text": "subarachnoid hemorrhage", "type": "BiologicFunction"}]}

Example input:
Sentence: Investigations showed bicytopenia , nephrotic range proteinuria with hypoalbuminemia , hypogammaglobulinemia , and features of hyaline - vascular type Castleman disease in a lymph node biopsy .

Example answer:
{"entities": [{"text": "Investigations", "type": "HealthCareActivity"}, {"text": "bicytopenia", "type": "Finding"}, {"text": "nephrotic range proteinuria", "type": "Finding"}, {"text": "hypoalbuminemia", "type": "BiologicFunction"}, {"text": "hypogammaglobulinemia", "type": "BiologicFunction"}, {"text": "hyaline", "type": "BodySubstance"}, {"text": "vascular", "type": "AnatomicalStructure"}, {"text": "Castleman disease", "type": "BiologicFunction"}, {"text": "lymph node biopsy", "type": "HealthCareActivity"}]}

Example input:
Sentence: The classic triad of oral and genital ulcerations in conjunction with uveitis was originally described by the Turkish dermatologist Hulusi Behcet in 1937 , but associated symptoms of the cardiovascular , central nervous , pulmonary , and gastrointestinal systems were later identified .

Example answer:
{"entities": [{"text": "oral", "type": "BiologicFunction"}, {"text": "genital ulcerations", "type": "BiologicFunction"}, {"text": "uveitis", "type": "BiologicFunction"}, {"text": "Turkish", "type": "PopulationGroup"}, {"text": "dermatologist", "type": "ProfessionalOrOccupationalGroup"}, {"text": "associated symptoms", "type": "Finding"}, {"text": "cardiovascular", "type": "BodySystem"}, {"text": "central nervous", "type": "BodySystem"}, {"text": "gastrointestinal systems", "type": "BodySystem"}]}

Example input:
Sentence: Mild encephalitis / encephalopathy with reversible splenial lesion ( MERS ) associated with Streptococcus pneumoniae Bacteraemia Mild encephalopathy with a reversible splenial lesion ( MERS ) is a clinico - radiological syndrome that can be related to infectious and non - infectious conditions .

Example answer:
{"entities": [{"text": "Mild encephalitis / encephalopathy with reversible splenial lesion", "type": "BiologicFunction"}, {"text": "MERS", "type": "BiologicFunction"}, {"text": "Streptococcus pneumoniae", "type": "Bacterium"}, {"text": "Bacteraemia", "type": "BiologicFunction"}, {"text": "Mild encephalopathy with a reversible splenial lesion", "type": "BiologicFunction"}, {"text": "clinico - radiological syndrome", "type": "BiologicFunction"}]}

Example input:
Sentence: Disruption of the BBB has been described in several neurological diseases .

Example answer:
{"entities": [{"text": "BBB", "type": "BiologicFunction"}, {"text": "neurological diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Magnetic resonance images revealed target - like hemorrhagic lesions in the right hemisphere of the cerebellum .

Example answer:
{"entities": [{"text": "Magnetic resonance images", "type": "IntellectualProduct"}, {"text": "hemorrhagic", "type": "BiologicFunction"}, {"text": "lesions", "type": "Finding"}, {"text": "right hemisphere of the cerebellum", "type": "AnatomicalStructure"}]}

Example input:
Sentence: She was subsequently diagnosed with an intracranial hemorrhage in the distribution of the right basal ganglia .

Example answer:
{"entities": [{"text": "diagnosed", "type": "Finding"}, {"text": "intracranial hemorrhage", "type": "BiologicFunction"}, {"text": "right basal ganglia", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In fact , Behcet 's disease with neurological involvement ( neuro - Behcet 's disease ) is not uncommon .

Example answer:
{"entities": [{"text": "Behcet 's disease", "type": "BiologicFunction"}, {"text": "neurological involvement", "type": "BiologicFunction"}, {"text": "neuro - Behcet 's disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Herein , we report an unusual case of neuro - Behcet 's disease in a patient who presented with a solitary cerebellar hemorrhage .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "neuro - Behcet 's disease", "type": "BiologicFunction"}, {"text": "cerebellar hemorrhage", "type": "BiologicFunction"}]}

Input:
Sentence: Neuro - Behcet disease presenting as a solitary cerebellar hemorrhagic lesion : a case report and review of the literature Behcet 's disease is a heterogeneous , multisystem , inflammatory disorder of unknown etiology .

## Item MedMentions:test:2720
Example input:
Sentence: Coexistence of light - driven Na ( + ) and H ( + ) transport in a microbial rhodopsin from Nonlabens dokdonensis Ion pumping microbial rhodopsins are photochemically active membrane proteins , converting light energy into ion - motive - force for ATP synthesis .

Example answer:
{"entities": [{"text": "light - driven", "type": "BiologicFunction"}, {"text": "Na ( + )", "type": "BiologicFunction"}, {"text": "H ( + ) transport", "type": "BiologicFunction"}, {"text": "microbial rhodopsin", "type": "Chemical"}, {"text": "Nonlabens dokdonensis", "type": "Bacterium"}, {"text": "Ion pumping", "type": "Chemical"}, {"text": "microbial rhodopsins", "type": "Chemical"}, {"text": "active membrane proteins", "type": "Chemical"}, {"text": "ion - motive - force", "type": "BiologicFunction"}, {"text": "ATP synthesis", "type": "BiologicFunction"}]}

Example input:
Sentence: The biochemical methane potential ( BMP ) of five different algae ( Chlorella vulgaris ) / manure ( cattle ) mixtures showed that the mixture of 80 / 20 ( on VS basis ) resulted in the highest BMP value ( 431mL CH4 gVS ( - 1 ) ) , while the BMP of microalgae alone ( 100 / 0 ) was 415mL CH4 gVS ( - 1 ) .

Example answer:
{"entities": [{"text": "methane", "type": "Chemical"}, {"text": "algae", "type": "Eukaryote"}, {"text": "Chlorella vulgaris", "type": "Eukaryote"}, {"text": "cattle", "type": "Eukaryote"}, {"text": "CH4", "type": "Chemical"}, {"text": "microalgae", "type": "Eukaryote"}]}

Example input:
Sentence: However , strain QH - 12 could not utilize the major intermediate product phthalate ( phthalic acid ; PA ) as the sole carbon and energy source , and only a little amount of PA was detected .

Example answer:
{"entities": [{"text": "strain QH - 12", "type": "Bacterium"}, {"text": "phthalate", "type": "Chemical"}, {"text": "phthalic acid", "type": "Chemical"}, {"text": "PA", "type": "Chemical"}, {"text": "carbon", "type": "Chemical"}, {"text": "energy source", "type": "Finding"}, {"text": "detected", "type": "Finding"}]}

Example input:
Sentence: Escherichia coli HGT : Engineered for high glucose throughput even under slowly growing or resting conditions Aerobic production - scale processes are constrained by the technical limitations of maximum oxygen transfer and heat removal .

Example answer:
{"entities": [{"text": "Escherichia coli HGT", "type": "Bacterium"}, {"text": "Engineered", "type": "ResearchActivity"}, {"text": "high glucose", "type": "Finding"}, {"text": "throughput", "type": "BiologicFunction"}, {"text": "slowly growing", "type": "Finding"}, {"text": "resting conditions", "type": "Finding"}, {"text": "oxygen transfer", "type": "Finding"}]}

Example input:
Sentence: CAT - NP containing biocompatible Fe3O4 were developed to catalyze H2O2 to generate free - radicals in situ that simultaneously degrade the biofilm matrix and rapidly kill the embedded bacteria with exceptional efficacy ( > 5 - log reduction of cell - viability ) .

Example answer:
{"entities": [{"text": "biocompatible", "type": "Chemical"}, {"text": "Fe3O4", "type": "Chemical"}, {"text": "H2O2", "type": "Chemical"}, {"text": "free - radicals", "type": "Chemical"}, {"text": "in situ", "type": "SpatialConcept"}, {"text": "biofilm matrix", "type": "AnatomicalStructure"}, {"text": "embedded bacteria", "type": "Bacterium"}, {"text": "cell - viability", "type": "BiologicFunction"}]}

Example input:
Sentence: Carboxymethyl cellulase production optimization from newly isolated thermophilic Bacillus subtilis K - 18 for saccharification using response surface methodology In this study , a novel thermophilic strain was isolated from soil and used for cellulase production in submerged fermentation using potato peel as sole carbon source .

Example answer:
{"entities": [{"text": "Carboxymethyl cellulase", "type": "Chemical"}, {"text": "Bacillus subtilis K - 18", "type": "Bacterium"}, {"text": "response surface methodology", "type": "ResearchActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "cellulase", "type": "Chemical"}, {"text": "submerged fermentation", "type": "BiologicFunction"}, {"text": "potato peel", "type": "Food"}, {"text": "carbon", "type": "Chemical"}, {"text": "source", "type": "Finding"}]}

Example input:
Sentence: Succinic acid production by immobilized cultures using spent sulphite liquor as fermentation medium Spent sulphite liquor ( SSL ) was used as carbon source for the production of succinic acid using immobilized cultures of Actinobacillus succinogenes and Basfia succiniciproducens on two different supports , delignified cellulosic material ( DCM ) and alginate beads .

Example answer:
{"entities": [{"text": "Succinic acid", "type": "Chemical"}, {"text": "immobilized", "type": "AnatomicalStructure"}, {"text": "cultures", "type": "HealthCareActivity"}, {"text": "fermentation", "type": "BiologicFunction"}, {"text": "Spent sulphite liquor", "type": "Chemical"}, {"text": "SSL", "type": "Chemical"}, {"text": "carbon", "type": "Chemical"}, {"text": "source", "type": "Finding"}, {"text": "succinic acid", "type": "Chemical"}, {"text": "Actinobacillus succinogenes", "type": "Bacterium"}, {"text": "Basfia succiniciproducens", "type": "Bacterium"}, {"text": "alginate", "type": "Chemical"}]}

Example input:
Sentence: The strain 's growth patterns under various concentrations of H2 O2 and its scavenging properties towards hydroxyl radical ( 64 . 85 % ) and DPPH ( 84 . 97 % ) were also interesting properties .

Example answer:
{"entities": [{"text": "strain 's", "type": "Bacterium"}, {"text": "growth patterns", "type": "Finding"}, {"text": "H2 O2", "type": "Chemical"}, {"text": "scavenging properties", "type": "BiologicFunction"}, {"text": "hydroxyl radical", "type": "Chemical"}, {"text": "DPPH", "type": "Chemical"}]}

Example input:
Sentence: The immobilized cultures improved the efficiency of succinic acid production as compared to free cell cultures .

Example answer:
{"entities": [{"text": "immobilized", "type": "AnatomicalStructure"}, {"text": "cultures", "type": "HealthCareActivity"}, {"text": "succinic acid", "type": "Chemical"}, {"text": "free cell cultures", "type": "HealthCareActivity"}]}

Example input:
Sentence: Agar concentration 4 % ( w / v ) and 4 mM glutamate were selected for bacterial immobilization in terms of rate and longevity of hydrogen production .

Example answer:
{"entities": [{"text": "Agar", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "bacterial immobilization", "type": "AnatomicalStructure"}, {"text": "hydrogen production", "type": "BiologicFunction"}]}

Input:
Sentence: Hydrogen production by immobilized photosynthetic bacteria is a convenient technology for hydrogen production as it enables to produce hydrogen with high organic acid concentrations comparing to suspended cultures .

## Item MedMentions:test:2894
Example input:
Sentence: This study aimed to identify current practices and processes used in the RTW of injured nurses , and determine if these are consistent with the seven principles for successful RTW as described by the Canadian Institute for Work & Health .

Example answer:
{"entities": [{"text": "RTW", "type": "Finding"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Job stressors , and particularly interpersonal relationships and management issues , significantly predict nurses ' job burnout .

Example answer:
{"entities": [{"text": "issues", "type": "Finding"}, {"text": "nurses '", "type": "ProfessionalOrOccupationalGroup"}, {"text": "job burnout", "type": "BiologicFunction"}]}

Example input:
Sentence: Recently , efforts have been made to understand the role of resilience in determining the psychological adjustment of employed nurses .

Example answer:
{"entities": [{"text": "employed", "type": "Finding"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Method As part of a larger cross - sectional study , survey data were collected from New South Wales nurses who had sustained a major workplace injury or illness .

Example answer:
{"entities": [{"text": "cross - sectional study", "type": "ResearchActivity"}, {"text": "survey data", "type": "IntellectualProduct"}, {"text": "New South Wales", "type": "SpatialConcept"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "workplace", "type": "SpatialConcept"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "illness", "type": "Finding"}]}

Example input:
Sentence: As nursing students are the future of the nursing workforce it is important to advance our understanding of the determinants of resilience in this population .

Example answer:
{"entities": [{"text": "nursing students", "type": "ProfessionalOrOccupationalGroup"}, {"text": "nursing", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "workforce", "type": "ProfessionalOrOccupationalGroup"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: Conclusions These findings suggest the practices and processes involved in the RTW of injured nurses are inconsistent with best practice principles for RTW , highlighting the need for interventions such as targeted employer education and training for improved industry RTW outcomes .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "RTW", "type": "Finding"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "employer", "type": "ProfessionalOrOccupationalGroup"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: Purpose Workplace injury and illness rates are high within the nursing profession , and in conjunction with current nursing shortages , low retention rates , and the high cost of workplace injury , the need for effective return to work ( RTW ) for injured nurses is highlighted .

Example answer:
{"entities": [{"text": "Workplace", "type": "SpatialConcept"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "illness", "type": "Finding"}, {"text": "nursing profession", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "nursing", "type": "ProfessionalOrOccupationalGroup"}, {"text": "workplace", "type": "SpatialConcept"}, {"text": "return to work", "type": "Finding"}, {"text": "RTW", "type": "Finding"}, {"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Approximately three quarters of the nurses had experienced at least one type of violence .

Example answer:
{"entities": [{"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "experienced", "type": "BiologicFunction"}, {"text": "violence", "type": "BiologicFunction"}]}

Example input:
Sentence: Violence perpetrated by nurse colleagues had a significant relationship with all four job outcomes , while violence by physicians had a significant inverse relationship with job satisfaction .

Example answer:
{"entities": [{"text": "Violence", "type": "BiologicFunction"}, {"text": "nurse", "type": "ProfessionalOrOccupationalGroup"}, {"text": "violence", "type": "BiologicFunction"}, {"text": "physicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "job satisfaction", "type": "BiologicFunction"}]}

Example input:
Sentence: Workplace Violence and Job Outcomes of Newly Licensed Nurses The purpose of this study was to examine the prevalence of workplace violence toward newly licensed nurses and the relationship between workplace violence and job outcomes .

Example answer:
{"entities": [{"text": "Licensed Nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "examine", "type": "Finding"}, {"text": "licensed nurses", "type": "ProfessionalOrOccupationalGroup"}]}

Input:
Sentence: Workplace violence is experienced by a high percentage of newly licensed nurses , and is associated with their job outcomes .

## Item MedMentions:test:2969
Example input:
Sentence: In high temperature days , a 10μg / m ( 3 ) increment in PM10 concentration corresponded to pooled estimates of 0 . 78 % ( 95 % CI : 0 . 44 % , 1 .

Example answer:
{"entities": []}

Example input:
Sentence: For example , a 10 μg / m³ increase of 7 - day ( lag 06 ) average concentrations of PM10 ( particulate matter no greater than 10 microns ) , SO₂ , NO₂ was associated with 0 .

Example answer:
{"entities": []}

Example input:
Sentence: Both down - and up - conversion measurements allow the quantification of concentrations from 0 to 300 μmol / L with a detection limit of 0 . 6 μmol / L , and this dual - mode detection increases the reliability of the measurement .

Example answer:
{"entities": [{"text": "dual - mode detection", "type": "HealthCareActivity"}]}

Example input:
Sentence: On average , a 1μg / m ( 3 ) increase in PM10 was associated with cumulative increases of 0 . 26893 , 0 . 30437 , and 0 . 21924 YLL for non - accidental , respiratory , and cardiovascular mortality , respectively , referring to 20μg / m ( 3 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 48 % ( 0 . 28 % , 0 . 69 % ) and 0 . 47 % ( 0 . 32 % , 0 . 63 % ) respectively , for 10μg / m ( 3 ) increase in exposure , both significantly higher than the increase of 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 6 . 8 [ 5 . 8 - 8 . 0 ] mL min ( - 1 ) kg ( - 1 ) , P < 0 . 001 ) and increases in respiratory quotient ( 0 . 96 [ 0 . 91 - 1 . 06 ] vs .

Example answer:
{"entities": [{"text": "respiratory quotient", "type": "ClinicalAttribute"}]}

Example input:
Sentence: In addition , the optimized FUS parameters for FCMBs - enhanced gene delivery were confirmed by cell experiments ( center frequency = 1 MHz ; acoustic pressure = 700 kPa ; pulse repetition frequency = 5 Hz ; cycle number = 10000 ; exposure time = 1 min ; FCMBs concentration = 4 × 10 ( 7 ) MB / mL ) .

Example answer:
{"entities": [{"text": "FUS", "type": "HealthCareActivity"}, {"text": "FCMBs", "type": "MedicalDevice"}, {"text": "gene delivery", "type": "BiologicFunction"}, {"text": "cell", "type": "AnatomicalStructure"}, {"text": "experiments", "type": "ResearchActivity"}]}

Example input:
Sentence: Moreover , due to the synergistic effect , coupling of ozone and ultrasound gave rise to rate constant of 2 . 5min ( - 1 ) ( 625 times higher than ultrasound ) .

Example answer:
{"entities": [{"text": "ozone", "type": "Chemical"}]}

Example input:
Sentence: As Pi concentration ( [ Pi ] ) was increased from 0 to 30 mmol·L ( - 1 ) , twitch duration decreased , with progressive reductions in sensitivity to Pi as [ Pi ] was increased .

Example answer:
{"entities": [{"text": "Pi", "type": "Chemical"}, {"text": "twitch", "type": "Finding"}, {"text": "reductions", "type": "HealthCareActivity"}]}

Example input:
Sentence: Commercially available IONPs were acoustically analysed to quantify their effect on the speed of sound ( SOS ) and acoustic attenuation as a function of concentration .

Example answer:
{"entities": [{"text": "analysed", "type": "ResearchActivity"}]}

Input:
Sentence: The results have shown a consistent concentration dependent speed of sound increase ( 1 . 86 [ Formula : see text ] rise per 100 µg · ml ( - 1 ) IONPs ) .

## Item MedMentions:test:2581
Example input:
Sentence: A role for the locus coeruleus in the analgesic efficacy of N - acetylaspartylglutamate peptidase ( GCPII ) inhibitors ZJ43 and 2 - PMPA N - acetylaspartylglutamate ( NAAG ) is the third most prevalent and widely distributed neurotransmitter in the mammalian nervous system .

Example answer:
{"entities": [{"text": "locus coeruleus", "type": "AnatomicalStructure"}, {"text": "analgesic efficacy", "type": "Finding"}, {"text": "N - acetylaspartylglutamate peptidase", "type": "Chemical"}, {"text": "GCPII", "type": "Chemical"}, {"text": "inhibitors", "type": "Chemical"}, {"text": "ZJ43", "type": "Chemical"}, {"text": "2 - PMPA", "type": "Chemical"}, {"text": "N - acetylaspartylglutamate", "type": "Chemical"}, {"text": "NAAG", "type": "Chemical"}, {"text": "neurotransmitter", "type": "Chemical"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "nervous system", "type": "BodySystem"}]}

Example input:
Sentence: These results indicate that vagal nerve plays an important role in mediating the anti - inflammatory effect in viral myocarditis , and that cholinergic stimulation with nicotine also plays its peripheral anti - inflammatory role relying on α7nAChR , without requirement for the integrity of vagal nerve in the model .

Example answer:
{"entities": [{"text": "vagal nerve", "type": "AnatomicalStructure"}, {"text": "anti - inflammatory", "type": "Chemical"}, {"text": "viral myocarditis", "type": "BiologicFunction"}, {"text": "stimulation", "type": "HealthCareActivity"}, {"text": "nicotine", "type": "Chemical"}, {"text": "peripheral", "type": "SpatialConcept"}, {"text": "α7nAChR", "type": "Chemical"}, {"text": "model", "type": "BiologicFunction"}]}

Example input:
Sentence: Moreover , pre - treatment with naloxone , an opioid receptor antagonist , only partially inhibited the effects of tebanicline in formalin and tail - pressure tests .

Example answer:
{"entities": [{"text": "naloxone", "type": "Chemical"}, {"text": "opioid receptor antagonist", "type": "Chemical"}, {"text": "tebanicline", "type": "Chemical"}, {"text": "formalin", "type": "Chemical"}, {"text": "tail - pressure tests", "type": "HealthCareActivity"}]}

Example input:
Sentence: Anti - nociceptive roles of the glia -specific metabolic inhibitor fluorocitrate in paclitaxel - evoked neuropathic pain Paclitaxel ( Taxol ) is a powerful chemotherapy drug used in breast cancers , but it often causes neuropathic pain , leading to the early cessation of therapy and poor treatment outcomes .

Example answer:
{"entities": [{"text": "Anti - nociceptive roles", "type": "Finding"}, {"text": "glia", "type": "AnatomicalStructure"}, {"text": "metabolic inhibitor", "type": "BiologicFunction"}, {"text": "fluorocitrate", "type": "Chemical"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "neuropathic pain", "type": "Finding"}, {"text": "Paclitaxel", "type": "Chemical"}, {"text": "Taxol", "type": "Chemical"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "drug", "type": "Chemical"}, {"text": "breast cancers", "type": "BiologicFunction"}, {"text": "therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Although high doses of SA - 57 alone were required to produce antinociception , low doses of this compound , which elevated AEA and did not affect 2 - AG brain levels , augmented the antinociceptive effects of morphine , but lacked cannabimimetic side effects .

Example answer:
{"entities": [{"text": "SA - 57", "type": "Chemical"}, {"text": "antinociception", "type": "Finding"}, {"text": "compound", "type": "Chemical"}, {"text": "AEA", "type": "Chemical"}, {"text": "2 - AG", "type": "Chemical"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "antinociceptive", "type": "Finding"}, {"text": "morphine", "type": "Chemical"}, {"text": "side effects", "type": "BiologicFunction"}]}

Example input:
Sentence: The endocannabinoid hydrolysis inhibitor SA - 57 : Intrinsic antinociceptive effects , augmented morphine -induced antinociception , and attenuated heroin seeking behavior in mice Although opioids are highly efficacious analgesics , their abuse potential and other untoward side effects diminish their therapeutic utility .

Example answer:
{"entities": [{"text": "endocannabinoid", "type": "Chemical"}, {"text": "SA - 57", "type": "Chemical"}, {"text": "antinociceptive", "type": "Finding"}, {"text": "morphine", "type": "Chemical"}, {"text": "antinociception", "type": "Finding"}, {"text": "heroin", "type": "Chemical"}, {"text": "seeking behavior", "type": "Finding"}, {"text": "mice", "type": "Eukaryote"}, {"text": "opioids", "type": "Chemical"}, {"text": "analgesics", "type": "Chemical"}, {"text": "abuse potential", "type": "BiologicFunction"}, {"text": "untoward side effects", "type": "BiologicFunction"}]}

Example input:
Sentence: Tebanicline had dose - dependent analgesic effects in formalin , hot - plate and tail - pressure tests .

Example answer:
{"entities": [{"text": "Tebanicline", "type": "Chemical"}, {"text": "analgesic effects", "type": "Finding"}, {"text": "formalin", "type": "Chemical"}, {"text": "hot - plate and tail - pressure tests", "type": "HealthCareActivity"}]}

Example input:
Sentence: By contrast , the antinociceptive effect of tebanicline was not demonstrated in the tail - flick assay .

Example answer:
{"entities": [{"text": "tebanicline", "type": "Chemical"}, {"text": "tail - flick assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: We assessed whether tebanicline exerts an effect on various noxious stimuli and mediates the nicotine receptor or opioid receptor through stimulation .

Example answer:
{"entities": [{"text": "tebanicline", "type": "Chemical"}, {"text": "nicotine receptor", "type": "Chemical"}, {"text": "opioid receptor", "type": "Chemical"}, {"text": "stimulation", "type": "BiologicFunction"}]}

Example input:
Sentence: The antinociceptive effects of tebanicline were determined by noxious chemical , thermal and mechanical stimuli -induced behaviours in mice .

Example answer:
{"entities": [{"text": "tebanicline", "type": "Chemical"}, {"text": "thermal", "type": "BiologicFunction"}, {"text": "mechanical stimuli", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Input:
Sentence: Antinociceptive effect of tebanicline for various noxious stimuli -induced behaviours in mice Tebanicline ( ABT - 594 ) , an analogue of epibatidine , exhibits potent antinociceptive effects and high affinity for the nicotinic acetylcholine receptor in the central nervous system .

## Item MedMentions:test:2751
Example input:
Sentence: The results of this study suggested that MAP suppressed microbiological growth and retarded lipid and protein oxidation in chicken thigh meats , with a 9 - day shelf - life extention with insignificant effects of OS .

Example answer:
{"entities": [{"text": "lipid", "type": "BiologicFunction"}, {"text": "protein oxidation", "type": "BiologicFunction"}, {"text": "chicken thigh meats", "type": "Food"}]}

Example input:
Sentence: At P14 , relative to controls , LPS and hyperoxia pups had reduced body weight , increased density of apoptotic cells ( TUNEL ) in the cortex , striatum and white matter , astrocytes ( GFAP ) in the white matter and activated microglia ( CD68 ) in the cortex and striatum , but no change in total microglia density ( Iba1 ) .

Example answer:
{"entities": [{"text": "LPS", "type": "Chemical"}, {"text": "hyperoxia", "type": "Finding"}, {"text": "pups", "type": "Eukaryote"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "TUNEL", "type": "ResearchActivity"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "striatum", "type": "AnatomicalStructure"}, {"text": "white matter", "type": "AnatomicalStructure"}, {"text": "astrocytes", "type": "AnatomicalStructure"}, {"text": "GFAP", "type": "Chemical"}, {"text": "microglia", "type": "AnatomicalStructure"}, {"text": "CD68", "type": "Chemical"}, {"text": "Iba1", "type": "Chemical"}]}

Example input:
Sentence: Compared to CONV - R mice , angiotensin II ( AngII ; 1 mg / kg per day for 7 days ) infused GF mice showed reduced reactive oxygen species formation in the vasculature , attenuated vascular mRNA expression of monocyte chemoattractant protein 1 ( MCP - 1 ) , inducible nitric oxide synthase ( iNOS ) and NADPH oxidase subunit Nox2 , as well as a reduced upregulation of retinoic - acid receptor - related orphan receptor gamma t ( Rorγt ) , the signature transcription factor for interleukin ( IL ) - 17 synthesis .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}, {"text": "angiotensin II", "type": "Chemical"}, {"text": "AngII", "type": "Chemical"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "vasculature", "type": "AnatomicalStructure"}, {"text": "vascular", "type": "AnatomicalStructure"}, {"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "monocyte chemoattractant protein 1", "type": "AnatomicalStructure"}, {"text": "MCP - 1", "type": "Chemical"}, {"text": "inducible nitric oxide synthase", "type": "AnatomicalStructure"}, {"text": "iNOS", "type": "AnatomicalStructure"}, {"text": "NADPH oxidase subunit Nox2", "type": "AnatomicalStructure"}, {"text": "upregulation", "type": "BiologicFunction"}, {"text": "retinoic - acid receptor - related orphan receptor gamma t", "type": "Chemical"}, {"text": "Rorγt", "type": "Chemical"}, {"text": "transcription factor", "type": "Chemical"}, {"text": "interleukin ( IL ) - 17", "type": "Chemical"}]}

Example input:
Sentence: SBS rats also demonstrated a significant three - to fourfold decrease in SMO , GIL , and PTCH mRNA , and protein levels ( determined by Real - Time PCR and Western blot ) compared to control animals .

Example answer:
{"entities": [{"text": "SBS", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}, {"text": "SMO", "type": "Chemical"}, {"text": "GIL", "type": "Chemical"}, {"text": "PTCH", "type": "Chemical"}, {"text": "mRNA", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}, {"text": "Real - Time PCR", "type": "ResearchActivity"}, {"text": "Western blot", "type": "HealthCareActivity"}, {"text": "control animals", "type": "Eukaryote"}]}

Example input:
Sentence: Downregulation of repolarizing TREK - 1 channels was associated with prolongation of atrial effective refractory periods versus baseline conditions , consistent with prior observations in humans with HF .

Example answer:
{"entities": [{"text": "Downregulation", "type": "BiologicFunction"}, {"text": "repolarizing", "type": "BiologicFunction"}, {"text": "TREK - 1 channels", "type": "Chemical"}, {"text": "atrial effective refractory periods", "type": "Finding"}, {"text": "observations", "type": "ResearchActivity"}, {"text": "humans", "type": "Eukaryote"}, {"text": "HF", "type": "BiologicFunction"}]}

Example input:
Sentence: TREK - 1 ( K2P2 . 1 ) K ( + ) channels are suppressed in patients with atrial fibrillation and heart failure and provide therapeutic targets for rhythm control Atrial fibrillation ( AF ) is the most common cardiac arrhythmia .

Example answer:
{"entities": [{"text": "TREK - 1 ( K2P2 . 1 ) K ( + ) channels", "type": "Chemical"}, {"text": "atrial fibrillation", "type": "BiologicFunction"}, {"text": "heart failure", "type": "BiologicFunction"}, {"text": "Atrial fibrillation", "type": "BiologicFunction"}, {"text": "AF", "type": "BiologicFunction"}, {"text": "cardiac arrhythmia", "type": "Finding"}]}

Example input:
Sentence: Functional correction of ionic remodeling through TREK - 1 gene therapy represents a novel paradigm to optimize and specify AF management .

Example answer:
{"entities": [{"text": "TREK - 1 gene therapy", "type": "HealthCareActivity"}, {"text": "AF", "type": "BiologicFunction"}]}

Example input:
Sentence: In conclusion , TREK - 1 downregulation and rhythm control by Ad - TREK - 1 transfer suggest mechanistic and potential therapeutic significance of TREK - 1 channels in a subgroup of AF patients with HF and prolonged atrial effective refractory periods .

Example answer:
{"entities": [{"text": "TREK - 1", "type": "Chemical"}, {"text": "downregulation", "type": "BiologicFunction"}, {"text": "Ad - TREK - 1 transfer", "type": "ResearchActivity"}, {"text": "mechanistic and potential therapeutic", "type": "HealthCareActivity"}, {"text": "TREK - 1 channels", "type": "Chemical"}, {"text": "subgroup", "type": "IntellectualProduct"}, {"text": "AF", "type": "BiologicFunction"}, {"text": "HF", "type": "BiologicFunction"}, {"text": "atrial effective refractory periods", "type": "Finding"}]}

Example input:
Sentence: In patients with chronic AF and HF , atrial TREK - 1 mRNA levels were reduced by 82 % ( left atrium ) and 81 % ( right atrium ) compared with sinus rhythm ( SR ) subjects .

Example answer:
{"entities": [{"text": "chronic AF", "type": "BiologicFunction"}, {"text": "HF", "type": "BiologicFunction"}, {"text": "atrial TREK - 1", "type": "Chemical"}, {"text": "mRNA", "type": "Chemical"}, {"text": "left atrium", "type": "AnatomicalStructure"}, {"text": "right atrium", "type": "AnatomicalStructure"}, {"text": "sinus rhythm", "type": "Finding"}, {"text": "SR", "type": "Finding"}, {"text": "subjects", "type": "PopulationGroup"}]}

Example input:
Sentence: Ad - TREK - 1 increased the SR prevalence to 62 % during follow - up in AF animals , compared to 35 % in the untreated AF group .

Example answer:
{"entities": [{"text": "Ad - TREK - 1", "type": "Chemical"}, {"text": "SR", "type": "Finding"}, {"text": "AF", "type": "BiologicFunction"}, {"text": "animals", "type": "Eukaryote"}]}

Input:
Sentence: TREK - 1 mRNA ( -66 % ) and protein ( -61 % ) was suppressed in AF animals at 14 - day follow - up compared with SR controls .

## Item MedMentions:test:3039
Example input:
Sentence: The measures of disease outcome were overall survival ( OS ) and disease - free survival ( DFS ) which estimated using the Kaplan - Meier method .

Example answer:
{"entities": [{"text": "disease outcome", "type": "Finding"}, {"text": "Kaplan - Meier method", "type": "ResearchActivity"}]}

Example input:
Sentence: Their Kaplan - Meier survival curves were digitized and pooled for generation of median overall ( OS ) and progression free ( PFS ) survivals and log - rank hazard ratios ( HRs ) .

Example answer:
{"entities": [{"text": "log - rank", "type": "IntellectualProduct"}]}

Example input:
Sentence: Univariate and multivariate survival analyses were conducted using the Cox proportional hazards regression methodology .

Example answer:
{"entities": [{"text": "multivariate survival analyses", "type": "ResearchActivity"}, {"text": "Cox proportional hazards regression methodology", "type": "IntellectualProduct"}]}

Example input:
Sentence: However , on landmark analysis this difference disappeared once limiting the survival analysis to men who survived ≥18 months [ HR = 0 .

Example answer:
{"entities": [{"text": "landmark analysis", "type": "ResearchActivity"}, {"text": "survival analysis", "type": "ResearchActivity"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: The combined results of univariate and multivariate Cox regression analysis showed that the SNP in ERCC1 - 118 was closely associated with survival time .

Example answer:
{"entities": [{"text": "multivariate Cox regression analysis", "type": "IntellectualProduct"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "ERCC1 - 118", "type": "AnatomicalStructure"}, {"text": "survival time", "type": "ClinicalAttribute"}]}

Example input:
Sentence: In a univariate analysis , AQP2 was a significant predictor of 14 and 28 - day survival , but this was not confirmed in multivariate analysis .

Example answer:
{"entities": [{"text": "AQP2", "type": "Chemical"}, {"text": "predictor", "type": "IntellectualProduct"}]}

Example input:
Sentence: We used univariate and multivariate analyses to identify independent predictors of overall survival .

Example answer:
{"entities": []}

Example input:
Sentence: Five - year survival outcomes were evaluated using Kaplan - Meier and Cox models .

Example answer:
{"entities": [{"text": "Kaplan - Meier", "type": "ResearchActivity"}, {"text": "Cox models", "type": "IntellectualProduct"}]}

Example input:
Sentence: The baseline characteristics were analyzed , and overall survival ( OS ) was estimated using the Kaplan - Meier method .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "Kaplan - Meier method", "type": "IntellectualProduct"}]}

Example input:
Sentence: As per intention - to - treat analysis , no survival benefit was observed between two groups [ 208 versus 196 days ; hazard ratio , 0 . 86 ; 95 % confidence interval ( CI ) 0 . 63 - 1 . 19 ; P = 0 . 3804 ] .

Example answer:
{"entities": [{"text": "intention - to - treat analysis", "type": "ResearchActivity"}]}

Input:
Sentence: Moreover , we investigated survival outcomes accounting for this parameter .

## Item MedMentions:test:2672
Example input:
Sentence: This genome -wide phylogeny provides an improved foundation for resolving phylogenetic relationships in Acropora and , combined with PaxC , provides a fascinating platform for future research into regions of the genome that influence reproductive isolation and speciation in corals .

Example answer:
{"entities": [{"text": "genome", "type": "AnatomicalStructure"}, {"text": "resolving", "type": "Finding"}, {"text": "Acropora", "type": "Eukaryote"}, {"text": "PaxC", "type": "SpatialConcept"}, {"text": "research", "type": "ResearchActivity"}, {"text": "regions of the genome", "type": "AnatomicalStructure"}, {"text": "corals", "type": "Eukaryote"}]}

Example input:
Sentence: Chasing ghosts : allopolyploid origin of Oxyria sinensis ( Polygonaceae ) from its only diploid congener and an unknown ancestor Reconstructing the origin of a polyploid species is particularly challenging when an ancestor has become extinct . Under such circumstances , the extinct donor of a genome found in the polyploid may be treated as a ' ghost ' species in that its prior existence is recognized through the presence of its genome in the polyploid .

Example answer:
{"entities": [{"text": "Oxyria sinensis", "type": "Eukaryote"}, {"text": "Polygonaceae", "type": "Eukaryote"}, {"text": "polyploid", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "genome", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Previous work has shown that conspecific colonies of Acropora that spawn in different seasons ( spring and autumn ) are associated with highly diverged lineages of the phylogenetic marker PaxC Here , we used 10 034 single - nucleotide polymorphisms to generate a genome -wide phylogeny and compared it with gene genealogies from the PaxC intron and the mtDNA Control Region in 20 species of Acropora , including three species with spring - and autumn - spawning cohorts .

Example answer:
{"entities": [{"text": "conspecific colonies", "type": "AnatomicalStructure"}, {"text": "Acropora", "type": "Eukaryote"}, {"text": "diverged", "type": "Finding"}, {"text": "phylogenetic marker", "type": "SpatialConcept"}, {"text": "PaxC", "type": "SpatialConcept"}, {"text": "single - nucleotide polymorphisms", "type": "SpatialConcept"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "gene", "type": "AnatomicalStructure"}, {"text": "genealogies", "type": "IntellectualProduct"}, {"text": "intron", "type": "Chemical"}, {"text": "mtDNA Control Region", "type": "AnatomicalStructure"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "cohorts", "type": "PopulationGroup"}]}

Example input:
Sentence: underwoodii including eight subspecies ( polystictus , discifer , underwoodii , incommodus , melanantherus , peruanus , annae , addae ) , although up to three species have been recognized by some authors .

Example answer:
{"entities": [{"text": "underwoodii", "type": "Eukaryote"}, {"text": "subspecies", "type": "IntellectualProduct"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "authors", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: One of the most specious and best - defined genera is Euplotes , which constitutes more than 70 morphospecies , many of which have never been molecularly tested .

Example answer:
{"entities": [{"text": "genera", "type": "IntellectualProduct"}, {"text": "Euplotes", "type": "Eukaryote"}, {"text": "morphospecies", "type": "IntellectualProduct"}]}

Example input:
Sentence: Biogeography and taxonomy of racket - tail hummingbirds ( Aves : Trochilidae : < i > Ocreatus < /i > ) : evidence for species delimitation from morphology and display behavior We analyzed geographic variation , biogeography , and intrageneric relationships of racket - tail hummingbirds Ocreatus ( Aves , Trochilidae ) .

Example answer:
{"entities": [{"text": "racket - tail hummingbirds", "type": "Eukaryote"}, {"text": "Aves", "type": "Eukaryote"}, {"text": "Trochilidae", "type": "Eukaryote"}, {"text": "Ocreatus", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "analyzed", "type": "ResearchActivity"}, {"text": "geographic", "type": "SpatialConcept"}]}

Example input:
Sentence: In this taxonomic treatment , O . annae becomes an endemic species to Peru and O .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "Peru", "type": "SpatialConcept"}]}

Example input:
Sentence: In order to evaluate the current taxonomy we studied geographic variation in coloration , mensural characters , and behavioral data of all Ocreatus taxa .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "studied", "type": "ResearchActivity"}, {"text": "geographic", "type": "SpatialConcept"}, {"text": "Ocreatus", "type": "Eukaryote"}, {"text": "taxa", "type": "IntellectualProduct"}]}

Example input:
Sentence: We recommend additional sampling of distributional , ethological , and molecular data for an improved resolution of the evolutionary history of Ocreatus .

Example answer:
{"entities": [{"text": "sampling", "type": "HealthCareActivity"}, {"text": "improved", "type": "Finding"}, {"text": "evolutionary", "type": "BiologicFunction"}, {"text": "Ocreatus", "type": "Eukaryote"}]}

Example input:
Sentence: Presently , the genus is usually considered monospecific , with O .

Example answer:
{"entities": [{"text": "genus", "type": "IntellectualProduct"}, {"text": "O .", "type": "Eukaryote"}]}

Input:
Sentence: Our results indicate that the genus should be considered a superspecies with four species , the monotypic Ocreatus addae , O . annae , and O . peruanus , and the polytypic O .

## Item MedMentions:test:2847
Example input:
Sentence: Different clinical pictures ( 0 - 50 % of diarrhea positivity ) , viral titer levels ( mean 5 . 3 - 7 . 2 log10 genome copies /mL ) , and antibody conditions ( 30 - 80 % of positivity ) were registered among sows on the four farms .

Example answer:
{"entities": [{"text": "clinical pictures", "type": "Finding"}, {"text": "diarrhea", "type": "Finding"}, {"text": "genome copies", "type": "AnatomicalStructure"}, {"text": "antibody conditions", "type": "Chemical"}, {"text": "farms", "type": "SpatialConcept"}]}

Example input:
Sentence: The frequencies of IFN - γ +874 T / A and T / T genotypes , as well as T allele , were significantly higher in the HLH group compared with those in the control group .

Example answer:
{"entities": [{"text": "IFN - γ", "type": "AnatomicalStructure"}, {"text": "T allele", "type": "AnatomicalStructure"}, {"text": "HLH", "type": "BiologicFunction"}]}

Example input:
Sentence: Blood samples were taken from 1025 women at presentation for thyroid stimulating hormone ( TSH ) , anti - thyroglobulin antibodies ( TGAb ) , and thyroid peroxidase antibodies ( TPOAb ) .

Example answer:
{"entities": [{"text": "Blood samples", "type": "BodySubstance"}, {"text": "women", "type": "PopulationGroup"}, {"text": "thyroid stimulating hormone", "type": "Chemical"}, {"text": "TSH", "type": "Chemical"}, {"text": "anti - thyroglobulin antibodies", "type": "Chemical"}, {"text": "TGAb", "type": "Chemical"}, {"text": "thyroid peroxidase antibodies", "type": "Chemical"}, {"text": "TPOAb", "type": "Chemical"}]}

Example input:
Sentence: The levels of IFN - γ and IL - 12 for the mice following immunization with Ag85A - Tb10 .

Example answer:
{"entities": [{"text": "IFN - γ", "type": "Chemical"}, {"text": "IL - 12", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "immunization", "type": "HealthCareActivity"}, {"text": "Ag85A", "type": "Chemical"}, {"text": "Tb10 .", "type": "Chemical"}]}

Example input:
Sentence: IFN - γ and IL - 12 Th1 cytokines increased significantly in mice vaccinated with Ag85a - TB10 .

Example answer:
{"entities": [{"text": "IFN - γ", "type": "Chemical"}, {"text": "IL - 12", "type": "Chemical"}, {"text": "Th1", "type": "Chemical"}, {"text": "cytokines", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "vaccinated", "type": "HealthCareActivity"}, {"text": "Ag85a", "type": "Chemical"}, {"text": "TB10 .", "type": "Chemical"}]}

Example input:
Sentence: THL increased the production of IFN - γ , IL - 2 , and TNF - α in mice vaccinated with γ - irradiated CT - 26 - high cells .

Example answer:
{"entities": [{"text": "THL", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "IL - 2", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "vaccinated", "type": "Finding"}, {"text": "γ - irradiated", "type": "HealthCareActivity"}, {"text": "CT - 26 - high cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The animals were selected randomly from 700 cattle on dairy farms , aged 3 - 5 years and suspected of having TB .

Example answer:
{"entities": [{"text": "animals", "type": "Eukaryote"}, {"text": "cattle", "type": "Eukaryote"}, {"text": "TB", "type": "BiologicFunction"}]}

Example input:
Sentence: All nine positive samples in the IFN - γ assay were positive in culture too .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "culture", "type": "HealthCareActivity"}]}

Example input:
Sentence: It is suggested that all positive samples in TST are also positive by IFN - γ too .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "TST", "type": "HealthCareActivity"}, {"text": "IFN - γ", "type": "Chemical"}]}

Example input:
Sentence: Interferon - γ assay , a high - sensitivity , specific and appropriate method for detection of bovine tuberculosis in cattle Bovine tuberculosis ( TB ) is an important zoonotic disease that is caused by Mycobacterium bovis .

Example answer:
{"entities": [{"text": "Interferon - γ", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "method", "type": "HealthCareActivity"}, {"text": "detection", "type": "HealthCareActivity"}, {"text": "bovine tuberculosis", "type": "BiologicFunction"}, {"text": "cattle", "type": "Eukaryote"}, {"text": "Bovine tuberculosis", "type": "BiologicFunction"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "zoonotic disease", "type": "BiologicFunction"}, {"text": "Mycobacterium bovis", "type": "Bacterium"}]}

Input:
Sentence: Ten cattle were positive using the TST and nine were positive by IFN - γ assay .

## Item MedMentions:test:2913
Example input:
Sentence: To reach an unbiased synchronization of the IADF position within tree rings and seasonal fluctuations in environmental conditions , it is necessary to know the timing of cambial activity and wood formation , which are species - and site - specific processes .

Example answer:
{"entities": [{"text": "unbiased", "type": "ResearchActivity"}, {"text": "position", "type": "SpatialConcept"}, {"text": "tree", "type": "Eukaryote"}, {"text": "rings", "type": "SpatialConcept"}, {"text": "fluctuations", "type": "Finding"}, {"text": "environmental", "type": "SpatialConcept"}, {"text": "cambial activity", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , the abundance of sponges in the Hirnantian sequence of South China may have aided post - extinction ecosystem recovery by stabilizing the sediment surface , allowing sessile suspension feeders such as brachiopods , corals , and bryozoans to recover rapidly .

Example answer:
{"entities": [{"text": "sponges", "type": "Eukaryote"}, {"text": "South China", "type": "SpatialConcept"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "brachiopods", "type": "Eukaryote"}, {"text": "corals", "type": "Eukaryote"}, {"text": "bryozoans", "type": "Eukaryote"}]}

Example input:
Sentence: In this study , it was recommended that any future habitat restoration initiative should include strong chain - link fencing to protect the seedlings from livestock activity .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "habitat", "type": "SpatialConcept"}, {"text": "initiative", "type": "BiologicFunction"}, {"text": "seedlings", "type": "Eukaryote"}, {"text": "livestock", "type": "Eukaryote"}]}

Example input:
Sentence: Local communities ' access to low value FPA resources improved during the post - colonial period but access to high value resources like commercial timber as well as sharing income benefits derived from FPA commercial activities remained a pipe dream .

Example answer:
{"entities": [{"text": "Local", "type": "SpatialConcept"}, {"text": "FPA", "type": "SpatialConcept"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: The productivity of such plantations often exceeds that of less - intensively - managed forests , and land managers have the option of choosing specific planting stock to produce specific types of wood for industrial use .

Example answer:
{"entities": [{"text": "land managers", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Synchronisms between bud and cambium phenology in black spruce : early - flushing provenances exhibit early xylem formation Bud and cambial phenology represent the adaptation of species to the local environment that allows the growing season to be maximized while minimizing the risk of frost for the developing tissues .

Example answer:
{"entities": [{"text": "bud", "type": "Eukaryote"}, {"text": "cambium", "type": "AnatomicalStructure"}, {"text": "black spruce", "type": "Eukaryote"}, {"text": "xylem", "type": "Eukaryote"}, {"text": "Bud", "type": "Eukaryote"}, {"text": "cambial", "type": "AnatomicalStructure"}, {"text": "adaptation", "type": "BiologicFunction"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "local", "type": "SpatialConcept"}, {"text": "environment", "type": "SpatialConcept"}, {"text": "frost", "type": "Chemical"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Long - term Cu stabilization and biomass yields of Giant reed and poplar after adding a biochar , alone or with iron grit , into a contaminated soil from a wood preservation site A 2 - year pot experiment was carried out to examine the aging effect of biochar ( B ) , alone or combined with iron grit ( Z ) , on Cu stabilization and plant growth in a contaminated soil ( 964 mg Cu kg ( - 1 ) ) from a wood preservation site .

Example answer:
{"entities": [{"text": "Cu", "type": "Chemical"}, {"text": "stabilization", "type": "HealthCareActivity"}, {"text": "Giant reed", "type": "Eukaryote"}, {"text": "poplar", "type": "Eukaryote"}, {"text": "biochar", "type": "Chemical"}, {"text": "iron grit", "type": "Chemical"}, {"text": "contaminated soil", "type": "InjuryOrPoisoning"}, {"text": "wood preservation", "type": "Chemical"}, {"text": "pot experiment", "type": "ResearchActivity"}, {"text": "aging effect", "type": "BiologicFunction"}, {"text": "B", "type": "Chemical"}, {"text": "Z", "type": "Chemical"}, {"text": "plant growth", "type": "BiologicFunction"}]}

Example input:
Sentence: Elimination and molecular identification of endophytic bacterial contaminants during in vitro propagation of Bambusa balcooa Bambusa balcooa is an economically important , multipurpose bamboo species , decidedly used in construction industry .

Example answer:
{"entities": [{"text": "Elimination", "type": "HealthCareActivity"}, {"text": "molecular identification", "type": "HealthCareActivity"}, {"text": "bacterial", "type": "Bacterium"}, {"text": "propagation", "type": "HealthCareActivity"}, {"text": "Bambusa balcooa", "type": "Eukaryote"}, {"text": "bamboo", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}]}

Example input:
Sentence: Micropropagation , being the potent alternative for season independent rapid regeneration , is restricted in bamboo because of endophytic contamination .

Example answer:
{"entities": [{"text": "Micropropagation", "type": "HealthCareActivity"}, {"text": "bamboo", "type": "Eukaryote"}]}

Example input:
Sentence: Availability of natural bamboo is depleting very rapidly due to accelerated deforestation and its unrestrained use .

Example answer:
{"entities": [{"text": "bamboo", "type": "Eukaryote"}]}

Input:
Sentence: The large number and timely supply of saplings are the need of the hour for the restoration of bamboo stands .

## Item MedMentions:test:2845
Example input:
Sentence: A total of 240 patients with type 2 diabetes ( T2DM ) attending an out - patient medical clinic were randomized to either PPBS or FBS monitoring .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "out - patient medical clinic", "type": "Organization"}, {"text": "randomized", "type": "Finding"}, {"text": "PPBS", "type": "HealthCareActivity"}, {"text": "FBS", "type": "HealthCareActivity"}, {"text": "monitoring", "type": "HealthCareActivity"}]}

Example input:
Sentence: Indomethacin ( 10μM ) and NS398 ( 1μM ) decreased the contractile response in diabetic rats and atorvastatin reversed these effects , without changing COX - 2 expression .

Example answer:
{"entities": [{"text": "Indomethacin", "type": "Chemical"}, {"text": "NS398", "type": "Chemical"}, {"text": "contractile", "type": "AnatomicalStructure"}, {"text": "diabetic", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}, {"text": "atorvastatin", "type": "Chemical"}, {"text": "COX - 2", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}]}

Example input:
Sentence: We adapted an existing clinical - economic model to include environmental outcomes ( carbon dioxide [ CO2 ] emissions ) to predict the consequences of adding insulin to an oral antidiabetic ( OAD ) regimen for patients with type 2 diabetes mellitus ( T2DM ) over 30 years , from the United Kingdom payer perspective .

Example answer:
{"entities": [{"text": "economic model", "type": "IntellectualProduct"}, {"text": "environmental", "type": "SpatialConcept"}, {"text": "carbon dioxide", "type": "Chemical"}, {"text": "CO2", "type": "Chemical"}, {"text": "insulin", "type": "Chemical"}, {"text": "oral", "type": "SpatialConcept"}, {"text": "antidiabetic", "type": "Chemical"}, {"text": "OAD", "type": "Chemical"}, {"text": "regimen", "type": "HealthCareActivity"}, {"text": "type 2 diabetes mellitus", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "United Kingdom", "type": "SpatialConcept"}, {"text": "payer", "type": "Organization"}]}

Example input:
Sentence: When taking into account household chores load , a more pronounced risk of T2DM was associated with high job strain in combination with heavy household chores load in women aged 60 years at baseline ( OR = 9 . 45 , 95 % CI : 1 . 17 - 76 . 53 ) .

Example answer:
{"entities": [{"text": "T2DM", "type": "BiologicFunction"}, {"text": "job strain", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Individuals with T2DM may be at higher risk of developing periodontal disease .

Example answer:
{"entities": [{"text": "Individuals", "type": "PopulationGroup"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "periodontal disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Serum free triiodothyronine ( FT3 ) , free thyroxine ( FT4 ) , and thyroid - stimulating hormone ( TSH ) levels were measured by chemiluminescence immunoassay , and T2DM was defined according to the American Diabetes Association criteria .

Example answer:
{"entities": [{"text": "Serum", "type": "BodySubstance"}, {"text": "free triiodothyronine", "type": "Chemical"}, {"text": "FT3", "type": "Chemical"}, {"text": "free thyroxine", "type": "Chemical"}, {"text": "FT4", "type": "Chemical"}, {"text": "thyroid - stimulating hormone ( TSH ) levels", "type": "Finding"}, {"text": "T2DM", "type": "BiologicFunction"}]}

Example input:
Sentence: The ratios of plasma concentrations of nifedipine in the umbilical vein , intervillous space and amniotic fluid to those in the maternal vein for CG and T2DM were 0 . 53 and 0 . 44 , 0 . 78 and 0 . 87 , respectively , with an amniotic fluid / maternal plasma ratio of 0 .

Example answer:
{"entities": [{"text": "nifedipine", "type": "Chemical"}, {"text": "umbilical vein", "type": "AnatomicalStructure"}, {"text": "intervillous space", "type": "SpatialConcept"}, {"text": "amniotic fluid", "type": "BodySubstance"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "plasma", "type": "BodySubstance"}]}

Example input:
Sentence: The study was conducted in 12 hypertensive pregnant women [ control group ( CG ) ] and 10 hypertensive pregnant women with T2DM taking slow - release nifedipine ( 20 mg , 12 / 12 h ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "hypertensive", "type": "BiologicFunction"}, {"text": "pregnant women", "type": "PopulationGroup"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: Effect of type 2 diabetes mellitus on the pharmacokinetics and transplacental transfer of nifedipine in hypertensive pregnant women Diabetes mellitus can inhibit cytochrome P450 3A4 , an enzyme responsible for the metabolism of nifedipine , used for the treatment of hypertension in pregnant women .

Example answer:
{"entities": [{"text": "type 2 diabetes mellitus", "type": "BiologicFunction"}, {"text": "nifedipine", "type": "Chemical"}, {"text": "hypertensive", "type": "BiologicFunction"}, {"text": "pregnant women", "type": "PopulationGroup"}, {"text": "Diabetes mellitus", "type": "BiologicFunction"}, {"text": "cytochrome P450 3A4", "type": "Chemical"}, {"text": "enzyme", "type": "Chemical"}, {"text": "metabolism", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "hypertension", "type": "BiologicFunction"}]}

Example input:
Sentence: We aimed to assess the effect of type 2 diabetes mellitus ( T2DM ) on the pharmacokinetics , placental transfer and distribution of nifedipine in amniotic fluid in hypertensive pregnant women .

Example answer:
{"entities": [{"text": "type 2 diabetes mellitus", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "nifedipine", "type": "Chemical"}, {"text": "amniotic fluid", "type": "BodySubstance"}, {"text": "hypertensive", "type": "BiologicFunction"}, {"text": "pregnant women", "type": "PopulationGroup"}]}

Input:
Sentence: There was no influence of T2DM on the pharmacokinetics or placental transfer of nifedipine in hypertensive women with controlled diabetes .

## Item MedMentions:test:2692
Example input:
Sentence: Interview respondents were found to engage in the Senior Games and related physical activity to the extent that they associated various intangible advantages with the games and valued psychological satisfaction .

Example answer:
{"entities": [{"text": "respondents", "type": "PopulationGroup"}, {"text": "Senior", "type": "PopulationGroup"}, {"text": "satisfaction", "type": "BiologicFunction"}]}

Example input:
Sentence: For that purpose , real - time auditory feedback of physiological and physical information based on sound signals , often termed " sonification , " has been proven particularly useful .

Example answer:
{"entities": []}

Example input:
Sentence: Although higher physical activity was associated with better neurocognitive functions of outpatients , in inpatients with non - remitted schizophrenia , higher physical activity was associated with worsening of several cognitive domains .

Example answer:
{"entities": [{"text": "neurocognitive functions", "type": "BiologicFunction"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "cognitive domains", "type": "BiologicFunction"}]}

Example input:
Sentence: No significant improvements are observed in the reduction of muscle tone or daily living activities .

Example answer:
{"entities": [{"text": "muscle tone", "type": "BiologicFunction"}]}

Example input:
Sentence: Focusing on light physical activities might be a potential strategy to make patients less sedentary , but for this to be achieved prior ( or at least parallel ) improvements in functional capacity seem to be necessary .

Example answer:
{"entities": [{"text": "functional capacity", "type": "Finding"}]}

Example input:
Sentence: The model brings together concepts and theories related to human sensorimotor interaction with music , and specifies the underlying psychological and physiological principles .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "music", "type": "IntellectualProduct"}]}

Example input:
Sentence: This review draws from leading research on pain neuroscience and control of posture and movement to help inform rehabilitation approaches and when it may or may not be prudent to " dance through " pain .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "research", "type": "ResearchActivity"}, {"text": "pain", "type": "Finding"}, {"text": "neuroscience", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "control of posture", "type": "Finding"}, {"text": "movement", "type": "BiologicFunction"}]}

Example input:
Sentence: This 3Mo model is intended to provide a conceptual framework that guides future research on musical biofeedback systems in the domain of sports and motor rehabilitation .

Example answer:
{"entities": [{"text": "guides", "type": "IntellectualProduct"}, {"text": "research", "type": "ResearchActivity"}, {"text": "musical", "type": "IntellectualProduct"}, {"text": "biofeedback", "type": "HealthCareActivity"}, {"text": "motor", "type": "BiologicFunction"}]}

Example input:
Sentence: Training control of posture and movement can improve motor skills and tissue integrity and also normalize perception of sensory stimuli from the peripheral nervous system in the brain .

Example answer:
{"entities": [{"text": "control of posture", "type": "Finding"}, {"text": "movement", "type": "BiologicFunction"}, {"text": "motor skills", "type": "BiologicFunction"}, {"text": "normalize", "type": "ResearchActivity"}, {"text": "perception", "type": "BiologicFunction"}, {"text": "peripheral nervous system", "type": "BodySystem"}, {"text": "brain", "type": "AnatomicalStructure"}]}

Example input:
Sentence: These functions relate the power of music to Motivate , and to Monitor and Modify physiological and physical processes .

Example answer:
{"entities": [{"text": "music", "type": "IntellectualProduct"}, {"text": "Motivate", "type": "BiologicFunction"}, {"text": "Monitor", "type": "HealthCareActivity"}]}

Input:
Sentence: In the current article , we assert that the use of music , and musical principles , can have a major added value , on top of mere sound signals , to the benefit of psychological and physical optimization of sports and motor rehabilitation tasks .

## Item MedMentions:test:2774
Example input:
Sentence: Fibrosis extent demonstrated correlation with both CD3 + and CD45 + cell counts in the right ( r = 0 . 781 , P < 0 . 001 for CD45 + and r = 0 .

Example answer:
{"entities": [{"text": "Fibrosis", "type": "BiologicFunction"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "CD3 +", "type": "Chemical"}, {"text": "CD45 +", "type": "Chemical"}, {"text": "cell counts", "type": "HealthCareActivity"}]}

Example input:
Sentence: Importantly , cardiac inflammation , fibrosis and systolic dysfunction were attenuated in GF mice , indicating systemic protection from cardiovascular inflammatory stress induced by AngII .

Example answer:
{"entities": [{"text": "fibrosis", "type": "BiologicFunction"}, {"text": "systolic dysfunction", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "cardiovascular inflammatory stress", "type": "Finding"}, {"text": "AngII", "type": "Chemical"}]}

Example input:
Sentence: Histopathological studies showed higher inflammatory cell infiltrates , cardiac fibrosis , and collagen deposition in LPS group , which were reduced by the administration of NS .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "inflammatory cell infiltrates", "type": "BodySubstance"}, {"text": "cardiac fibrosis", "type": "BiologicFunction"}, {"text": "collagen", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "NS", "type": "Eukaryote"}]}

Example input:
Sentence: Plasma norepinephrine was the unique predictor of myocardial fibrosis at univariate analysis ( P < 0 .

Example answer:
{"entities": [{"text": "Plasma", "type": "BodySubstance"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "myocardial fibrosis", "type": "BiologicFunction"}]}

Example input:
Sentence: In patients with cardiac sarcoidosis , both fibrosis mass and its localisation to the basal anterior / anteroseptal left ventricle , or right ventricle was associated with the development of major adverse cardiac events or ventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "cardiac sarcoidosis", "type": "BiologicFunction"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "mass", "type": "Finding"}, {"text": "basal anterior", "type": "AnatomicalStructure"}, {"text": "anteroseptal left ventricle", "type": "AnatomicalStructure"}, {"text": "right ventricle", "type": "AnatomicalStructure"}, {"text": "adverse cardiac events", "type": "Finding"}, {"text": "ventricular tachyarrhythmias", "type": "BiologicFunction"}]}

Example input:
Sentence: Increased left ventricular fibrosis mass was associated with increased prevalence of ventricular tachyarrhythmias ( p < 0 .

Example answer:
{"entities": [{"text": "left ventricular", "type": "AnatomicalStructure"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "mass", "type": "Finding"}, {"text": "ventricular tachyarrhythmias", "type": "BiologicFunction"}]}

Example input:
Sentence: ISO caused ventricular leukocyte infiltration , myocyte fibrosis , and necrosis with increased concentrations of the natriuretic peptides , cardiac troponins , and Myl3 .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "ventricular", "type": "SpatialConcept"}, {"text": "leukocyte infiltration", "type": "Finding"}, {"text": "myocyte fibrosis", "type": "BiologicFunction"}, {"text": "necrosis", "type": "BiologicFunction"}, {"text": "natriuretic peptides", "type": "Chemical"}, {"text": "cardiac", "type": "AnatomicalStructure"}, {"text": "troponins", "type": "Chemical"}, {"text": "Myl3", "type": "Chemical"}]}

Example input:
Sentence: However , it is not clear to what extent atrial inflammatory reaction associated with AF extends on the ventricular myocardium .

Example answer:
{"entities": [{"text": "extent", "type": "SpatialConcept"}, {"text": "atrial", "type": "AnatomicalStructure"}, {"text": "inflammatory reaction", "type": "BiologicFunction"}, {"text": "AF", "type": "BiologicFunction"}, {"text": "extends", "type": "SpatialConcept"}, {"text": "ventricular myocardium", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Histological evidence of inflammatory reaction associated with fibrosis in the atrial and ventricular walls in a case - control study of patients with history of atrial fibrillation Chronic inflammation in the atrial myocardium was shown to play an important role in the development of atrial fibrosis in patients with atrial fibrillation ( AF ) .

Example answer:
{"entities": [{"text": "inflammatory reaction", "type": "BiologicFunction"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "atrial", "type": "AnatomicalStructure"}, {"text": "ventricular walls", "type": "AnatomicalStructure"}, {"text": "case - control study", "type": "ResearchActivity"}, {"text": "history", "type": "Finding"}, {"text": "atrial fibrillation", "type": "BiologicFunction"}, {"text": "Chronic inflammation", "type": "BiologicFunction"}, {"text": "atrial myocardium", "type": "AnatomicalStructure"}, {"text": "role", "type": "IntellectualProduct"}, {"text": "development", "type": "BiologicFunction"}, {"text": "AF", "type": "BiologicFunction"}]}

Example input:
Sentence: Histological signs of chronic inflammation affecting ventricular myocardium are strongly associated with AF and demonstrate significant correlation with fibrosis extent that cannot be explained by cardiovascular comorbidities otherwise .

Example answer:
{"entities": [{"text": "signs", "type": "Finding"}, {"text": "chronic inflammation", "type": "BiologicFunction"}, {"text": "ventricular myocardium", "type": "AnatomicalStructure"}, {"text": "AF", "type": "BiologicFunction"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "cardiovascular", "type": "SpatialConcept"}]}

Input:
Sentence: Our aim was to assess the extent of fibrosis and lymphomononuclear infiltration in human ventricular myocardium and explore its association with AF .

## Item MedMentions:test:2946
Example input:
Sentence: These include pain after stenting ( 38 % ) , stent obstruction ( 23 % ) and stent migration ( 6 % ) .

Example answer:
{"entities": [{"text": "pain", "type": "Finding"}, {"text": "stenting", "type": "HealthCareActivity"}, {"text": "stent obstruction", "type": "BiologicFunction"}, {"text": "stent migration", "type": "BiologicFunction"}]}

Example input:
Sentence: Rates of survival free from homograft stenosis and reintervention at 1 , 5 and 10 years were 96 % , 82 % and 75 % and 99 % , 94 % and 91 % , respectively .

Example answer:
{"entities": [{"text": "homograft", "type": "Chemical"}, {"text": "stenosis", "type": "BiologicFunction"}, {"text": "reintervention", "type": "HealthCareActivity"}]}

Example input:
Sentence: This multicenter retrospective study included 194 patients who underwent stent placement between July and October 2015 .

Example answer:
{"entities": [{"text": "multicenter retrospective study", "type": "ResearchActivity"}, {"text": "stent placement", "type": "HealthCareActivity"}]}

Example input:
Sentence: Reasons for stent placement include 122 cases post ureteroscopy ( 63 % ) , 8 cases post percutaneous nephrolithotomy ( PCNL ) ( 4 % ) , 14 cases post extracorporeal shock wave lithotripsy ( SWL ) ( 7 % ) , 18 cases of cancer - related ureteral obstruction ( 9 % ) , 21 cases of hydronephrosis ( 11 % ) , and 11 for other reasons ( 6 % ) .

Example answer:
{"entities": [{"text": "stent placement", "type": "HealthCareActivity"}, {"text": "ureteroscopy", "type": "HealthCareActivity"}, {"text": "percutaneous nephrolithotomy", "type": "HealthCareActivity"}, {"text": "PCNL", "type": "HealthCareActivity"}, {"text": "extracorporeal shock wave lithotripsy", "type": "HealthCareActivity"}, {"text": "SWL", "type": "HealthCareActivity"}, {"text": "cancer - related", "type": "Finding"}, {"text": "ureteral obstruction", "type": "AnatomicalStructure"}, {"text": "hydronephrosis", "type": "BiologicFunction"}]}

Example input:
Sentence: The outcome indicated that there was no mobilization , displacement , or subsidence in all patients with the exception of one case with prosthesis migration .

Example answer:
{"entities": []}

Example input:
Sentence: The combined use at different surgical times of the self - expandable stent and flow - diverter device was technically successful in both patients .

Example answer:
{"entities": [{"text": "self - expandable stent", "type": "MedicalDevice"}, {"text": "flow - diverter device", "type": "MedicalDevice"}]}

Example input:
Sentence: The primary outcome was proportion of subjects without treatment failure ( regimen switch or VL > 200 copies / mL twice consecutively ) at 48 weeks .

Example answer:
{"entities": [{"text": "subjects", "type": "PopulationGroup"}, {"text": "treatment failure", "type": "Finding"}, {"text": "regimen", "type": "HealthCareActivity"}]}

Example input:
Sentence: All surgeries were successful .

Example answer:
{"entities": [{"text": "surgeries", "type": "HealthCareActivity"}]}

Example input:
Sentence: We observed a marked increase ( P = 0 . 01 ) in stenting after publication of the SAPPHIRE trial ( Stenting and Angioplasty With Protection in Patients at High Risk for Endarterectomy ) in 2004 , whereas stenting remained relatively unchanged after subsequent randomized trials published in 2006 ( P = 0 . 11 ) and 2010 ( P = 0 . 34 ) .

Example answer:
{"entities": [{"text": "stenting", "type": "HealthCareActivity"}, {"text": "publication", "type": "IntellectualProduct"}, {"text": "SAPPHIRE trial", "type": "ResearchActivity"}, {"text": "Stenting and Angioplasty With Protection in Patients at High Risk for Endarterectomy", "type": "ResearchActivity"}, {"text": "unchanged", "type": "Finding"}, {"text": "randomized trials", "type": "ResearchActivity"}]}

Example input:
Sentence: The probabilities of homograft stenosis and reintervention 10 years after the Ross procedure were 29 % and 10 % , respectively ; only one patient had a reintervention -related death .

Example answer:
{"entities": [{"text": "homograft", "type": "Chemical"}, {"text": "stenosis", "type": "BiologicFunction"}, {"text": "reintervention", "type": "HealthCareActivity"}, {"text": "Ross procedure", "type": "HealthCareActivity"}, {"text": "death", "type": "BiologicFunction"}]}

Input:
Sentence: Results In all cases , stent - graft deployment was successful .

## Item MedMentions:test:2953
Example input:
Sentence: Appropriate lesion preparation , high - pressure postdilatation , and the use of intravascular imaging are recommended to obtain the best possible final result .

Example answer:
{"entities": [{"text": "lesion", "type": "Finding"}, {"text": "postdilatation", "type": "HealthCareActivity"}, {"text": "intravascular imaging", "type": "HealthCareActivity"}]}

Example input:
Sentence: The particle size analysis revealed that the Z - average diameter of the AgNPs was 50 . 86 nm with polydispersity index ( PDI ) 0 . 136 .

Example answer:
{"entities": [{"text": "AgNPs", "type": "Chemical"}]}

Example input:
Sentence: Among patients nonadherent to stimulants pre - augmentation ( n = 165 ) , unadjusted mean ( SD ) pre - and post - stimulant mMPRs were 0 .

Example answer:
{"entities": [{"text": "stimulants", "type": "Chemical"}, {"text": "augmentation", "type": "HealthCareActivity"}, {"text": "stimulant", "type": "Chemical"}]}

Example input:
Sentence: Risk of advanced lesions at the first follow - up colonoscopy after polypectomy of diminutive versus small adenomatous polyps of low - grade dysplasia The current guidelines for surveillance after polypectomy do not distinguish between diminutive ( 1 - 5 mm ) and small ( 6 - 9 mm ) polyps with low - grade dysplasia ( LGD ) .

Example answer:
{"entities": [{"text": "lesions", "type": "Finding"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "colonoscopy", "type": "HealthCareActivity"}, {"text": "polypectomy", "type": "HealthCareActivity"}, {"text": "adenomatous polyps", "type": "BiologicFunction"}, {"text": "dysplasia", "type": "BiologicFunction"}, {"text": "guidelines", "type": "IntellectualProduct"}, {"text": "surveillance", "type": "HealthCareActivity"}, {"text": "polyps", "type": "AnatomicalStructure"}, {"text": "LGD", "type": "BiologicFunction"}]}

Example input:
Sentence: The main PV diameter on preoperative computed tomography was 8 .

Example answer:
{"entities": [{"text": "PV", "type": "AnatomicalStructure"}, {"text": "computed tomography", "type": "HealthCareActivity"}]}

Example input:
Sentence: Responders also had significant changes in volumetric apparent diffusion coefficient ( P = .01 and P = .03 ) and contrast enhancement ( P < .0001 and P < .0001 ) at 1 month for both readers , respectively .

Example answer:
{"entities": [{"text": "Responders", "type": "Finding"}, {"text": "volumetric", "type": "SpatialConcept"}]}

Example input:
Sentence: Then , the balloon was inflated somewhat when the distal tip of the balloon was slightly advanced from the tip of the reperfusion catheter , and together the coaxial system was advanced to an embolus over a 0 . 014 - in guidewire , even around the corner .

Example answer:
{"entities": [{"text": "balloon", "type": "MedicalDevice"}, {"text": "distal", "type": "SpatialConcept"}, {"text": "reperfusion", "type": "BiologicFunction"}, {"text": "catheter", "type": "MedicalDevice"}, {"text": "embolus", "type": "Finding"}]}

Example input:
Sentence: Air speed had no significant effect on the spray plume volume median diameter ( Dv ( 0 . 5 ) ) at the speeds tested with Fyfanon ( ® ) .

Example answer:
{"entities": []}

Example input:
Sentence: On logistic regression analysis , smaller size ( < 3 mm ) without complete occlusion related to recanalization ( OR , 8 . 0 , 95 % CI , 1 . 3 - 50 . 0 , P = 0 . 026 ) .

Example answer:
{"entities": [{"text": "size", "type": "SpatialConcept"}, {"text": "recanalization", "type": "HealthCareActivity"}]}

Example input:
Sentence: What 's more , smaller size ( < 3 mm ) without complete occlusion may relate to recanalization .

Example answer:
{"entities": [{"text": "recanalization", "type": "HealthCareActivity"}]}

Input:
Sentence: Postdilatation with noncompliant balloons ( mean diameter 3 .

## Item MedMentions:test:2992
Example input:
Sentence: A total of 291 participants ( 97 cases and 194 controls ) were included in our study .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: In total , 1288 patients were analyzed .

Example answer:
{"entities": []}

Example input:
Sentence: Twenty - seven men participated on at least 11 days and were thus included in the analyses .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "analyses", "type": "ResearchActivity"}]}

Example input:
Sentence: A total of 4 , 267 patients were included in the analysis .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: The analysis included 21 patients ( 12 women , 9 men ; mean age 36 years ) .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}, {"text": "mean age 36 years", "type": "Finding"}]}

Example input:
Sentence: 50 patients were taken to analysis .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: A total of 1 , 373 patients were included in the analyses .

Example answer:
{"entities": [{"text": "analyses", "type": "ResearchActivity"}]}

Example input:
Sentence: The analysis included 289 109 patients from 13 observational studies .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "observational studies", "type": "ResearchActivity"}]}

Example input:
Sentence: Analyses were based on 13 , 958 respondents .

Example answer:
{"entities": [{"text": "Analyses", "type": "ResearchActivity"}, {"text": "respondents", "type": "PopulationGroup"}]}

Example input:
Sentence: Two hundred seventy - nine participants ( n = 279 ) were included in the final analysis .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "analysis", "type": "ResearchActivity"}]}

Input:
Sentence: The analysis was conducted on a sample of 4629 participants of whom 72 .

## Item MedMentions:test:2796
Example input:
Sentence: Does genistein lower plasma lipids and homocysteine levels in postmenopausal women ?

Example answer:
{"entities": [{"text": "genistein", "type": "Chemical"}, {"text": "plasma lipids", "type": "HealthCareActivity"}, {"text": "homocysteine levels", "type": "HealthCareActivity"}, {"text": "postmenopausal", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Furthermore , indications of reduced cardiometabolic adaptations to exercise in postmenopausal women add to the adverse health profile .

Example answer:
{"entities": [{"text": "adaptations", "type": "BiologicFunction"}, {"text": "postmenopausal", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "adverse", "type": "BiologicFunction"}]}

Example input:
Sentence: On the decrease in bone mineral density and osteoporosis in postmenopausal women influence many risk factors whose identification has the aim to develop more effective prevention of this disease in the elderly .

Example answer:
{"entities": [{"text": "bone mineral density", "type": "ClinicalAttribute"}, {"text": "osteoporosis", "type": "BiologicFunction"}, {"text": "postmenopausal", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "risk factors", "type": "Finding"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "elderly", "type": "PopulationGroup"}]}

Example input:
Sentence: A 3 - month high - intensity aerobic training intervention , involving healthy , nonobese , late premenopausal ( n = 40 ) and early postmenopausal ( n = 39 ) women was conducted and anthropometrics , body composition , blood pressure , lipid profile , glucose tolerance , and maximal oxygen consumption were determined at baseline and after the intervention .

Example answer:
{"entities": [{"text": "intervention", "type": "HealthCareActivity"}, {"text": "nonobese", "type": "Finding"}, {"text": "premenopausal", "type": "Finding"}, {"text": "postmenopausal", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "anthropometrics", "type": "ClinicalAttribute"}, {"text": "blood pressure", "type": "BiologicFunction"}, {"text": "maximal oxygen consumption", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Our meta - analysis demonstrates that genistein significantly reduces homocysteine levels and increases HDL cholesterol levels in postmenopausal women .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}, {"text": "genistein", "type": "Chemical"}, {"text": "homocysteine levels", "type": "HealthCareActivity"}, {"text": "HDL cholesterol levels", "type": "HealthCareActivity"}, {"text": "postmenopausal", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Genistein also significantly decreases LDL cholesterol , total cholesterol and triglyceride levels in postmenopausal women with metabolic syndrome .

Example answer:
{"entities": [{"text": "Genistein", "type": "Chemical"}, {"text": "LDL cholesterol", "type": "HealthCareActivity"}, {"text": "total cholesterol", "type": "HealthCareActivity"}, {"text": "triglyceride levels", "type": "HealthCareActivity"}, {"text": "postmenopausal", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "metabolic syndrome", "type": "BiologicFunction"}]}

Example input:
Sentence: Analysis of the data of our research shows that by the univariate logistic regression the values of lipid parameters total cholesterol ( p = 0 . 000 ) , LDL ( p = 0 . 005 ) and TG ( p = 0 . 033 ) were significantly associated with osteoporosis , while in multivariate logistic model only total cholesterol ( p = 0 . 018 ) was found as an independent risk factor for osteoporosis in postmenopausal women .

Example answer:
{"entities": [{"text": "Analysis", "type": "ResearchActivity"}, {"text": "research", "type": "ResearchActivity"}, {"text": "univariate logistic regression", "type": "ResearchActivity"}, {"text": "lipid", "type": "Chemical"}, {"text": "parameters", "type": "Finding"}, {"text": "total cholesterol", "type": "Chemical"}, {"text": "LDL", "type": "Chemical"}, {"text": "TG", "type": "Chemical"}, {"text": "osteoporosis", "type": "BiologicFunction"}, {"text": "multivariate logistic model", "type": "IntellectualProduct"}, {"text": "risk factor", "type": "Finding"}, {"text": "postmenopausal", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: In fully adjusted models , women had higher levels of high - density lipoprotein cholesterol and high - density lipoprotein particle concentration , leptin , d - dimer , homoarginine , and N - terminal pro B - type natriuretic peptide , and lower levels of low - density lipoprotein cholesterol , adiponectin , lipoprotein - associated phospholipase A2 mass and activity , monocyte chemoattractant protein - 1 , soluble endothelial cell adhesion molecule , symmetrical dimethylarginine , asymmetrical dimethylarginine , high - sensitivity troponin T , and cystatin C .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "high - density lipoprotein cholesterol", "type": "Chemical"}, {"text": "high - density lipoprotein particle", "type": "Chemical"}, {"text": "leptin", "type": "Chemical"}, {"text": "d - dimer", "type": "Chemical"}, {"text": "homoarginine", "type": "Chemical"}, {"text": "N - terminal pro B - type natriuretic peptide", "type": "Chemical"}, {"text": "low - density lipoprotein cholesterol", "type": "Chemical"}, {"text": "adiponectin", "type": "Chemical"}, {"text": "lipoprotein", "type": "Chemical"}, {"text": "phospholipase A2", "type": "Chemical"}, {"text": "activity", "type": "BiologicFunction"}, {"text": "monocyte chemoattractant protein - 1", "type": "Chemical"}, {"text": "endothelial cell adhesion molecule", "type": "Chemical"}, {"text": "symmetrical", "type": "Finding"}, {"text": "dimethylarginine", "type": "Chemical"}, {"text": "asymmetrical", "type": "SpatialConcept"}, {"text": "troponin T", "type": "Chemical"}, {"text": "cystatin C", "type": "Chemical"}]}

Example input:
Sentence: We sought to evaluate risk factors for type 2 diabetes and cardiovascular disease in late premenopausal and early postmenopausal women , matched by age and body composition , and investigate the effect of high - intensity training .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "risk factors", "type": "Finding"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "cardiovascular disease", "type": "BiologicFunction"}, {"text": "premenopausal", "type": "Finding"}, {"text": "postmenopausal", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: Cardiovascular risk factors are similar in late premenopausal and early postmenopausal women , matched by age and body composition , with the exception that postmenopausal women have higher high - and low - density lipoprotein - cholesterol levels .

Example answer:
{"entities": [{"text": "premenopausal", "type": "Finding"}, {"text": "postmenopausal", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "high -", "type": "HealthCareActivity"}, {"text": "low - density lipoprotein - cholesterol levels", "type": "HealthCareActivity"}]}

Input:
Sentence: At baseline the postmenopausal women had higher total cholesterol ( P < .001 ) , low - density lipoprotein - cholesterol ( P < .05 ) , and high - density lipoprotein - cholesterol ( P < .001 ) than the premenopausal women .

## Item MedMentions:test:2877
Example input:
Sentence: Anesthesia resulted in long - term neurobehavioral changes in the fear conditioning task carried out 65 days after exposure to anesthesia in 3xTg - AD mice .

Example answer:
{"entities": [{"text": "Anesthesia", "type": "HealthCareActivity"}, {"text": "3xTg - AD mice", "type": "Eukaryote"}]}

Example input:
Sentence: Here we traced the dynamics of distinct abstract and effector - selective decision signals in the form of the broad - band centro - parietal positivity ( CPP ) and limb - selective β - band ( 8 - 16 and 18 - 30 Hz ) EEG activity , respectively , during delayed - reported motion direction decisions with and without foreknowledge of direction - response mapping .

Example answer:
{"entities": [{"text": "traced", "type": "Finding"}, {"text": "abstract", "type": "BiologicFunction"}, {"text": "centro - parietal positivity", "type": "Finding"}, {"text": "CPP", "type": "Finding"}, {"text": "limb - selective β - band", "type": "Finding"}, {"text": "EEG", "type": "HealthCareActivity"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "motion direction", "type": "SpatialConcept"}, {"text": "decisions", "type": "BiologicFunction"}, {"text": "direction", "type": "SpatialConcept"}]}

Example input:
Sentence: Across two experiments we examined whether repetitive transcranial magnetic stimulation ( rTMS ) over right FEF , right IPS , righ t MT , and a control site , peripheral V1 / V2 , diminished participants ' perception of two cases of predictive position perception : trans - saccadic fusion , and the flash grab illusion , both presented in the contralateral visual field .

Example answer:
{"entities": [{"text": "repetitive transcranial magnetic stimulation", "type": "HealthCareActivity"}, {"text": "rTMS", "type": "HealthCareActivity"}, {"text": "right", "type": "SpatialConcept"}, {"text": "FEF", "type": "AnatomicalStructure"}, {"text": "right IPS", "type": "SpatialConcept"}, {"text": "righ", "type": "SpatialConcept"}, {"text": "MT", "type": "AnatomicalStructure"}, {"text": "site", "type": "SpatialConcept"}, {"text": "peripheral V1", "type": "AnatomicalStructure"}, {"text": "V2", "type": "AnatomicalStructure"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "perception", "type": "BiologicFunction"}, {"text": "position", "type": "SpatialConcept"}, {"text": "trans - saccadic", "type": "BiologicFunction"}, {"text": "fusion", "type": "BiologicFunction"}, {"text": "flash grab illusion", "type": "BiologicFunction"}, {"text": "visual field", "type": "SpatialConcept"}]}

Example input:
Sentence: This study examined whether executive function capacity contributes to generalization and extinction of generalization as well as peak - shift of conditioned fear of movement - related pain and expectancy .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "executive function capacity", "type": "BiologicFunction"}, {"text": "generalization", "type": "BiologicFunction"}, {"text": "extinction", "type": "BiologicFunction"}]}

Example input:
Sentence: Evidence was found in favor of an area - shift , rather than a peak - shift effect , which implies that the peak conditioned fear response extended to , but did not shift to a novel stimulus .

Example answer:
{"entities": [{"text": "conditioned fear response", "type": "BiologicFunction"}]}

Example input:
Sentence: Demonstration and validation of a new pressure -based MRI -safe pain tolerance device One of the barriers to studying the behavioral and emotional effects of pain using functional Magnetic Resonance Imaging ( fMRI ) is the absence of a commercially available , MRI - compatible , pressure -based algometer to elicit pain .

Example answer:
{"entities": [{"text": "validation", "type": "ResearchActivity"}, {"text": "MRI", "type": "MedicalDevice"}, {"text": "pain tolerance", "type": "Finding"}, {"text": "device", "type": "MedicalDevice"}, {"text": "emotional", "type": "BiologicFunction"}, {"text": "pain", "type": "Finding"}, {"text": "functional Magnetic Resonance Imaging", "type": "HealthCareActivity"}, {"text": "fMRI", "type": "HealthCareActivity"}, {"text": "algometer", "type": "MedicalDevice"}]}

Example input:
Sentence: Participants completed study measures , which included the pain intensity , the Pain Catastrophizing Scale ( PCS ) , and the Tampa Scale of Kinesiophobia ( TSK ) .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "study", "type": "ResearchActivity"}, {"text": "pain intensity", "type": "ClinicalAttribute"}, {"text": "Pain Catastrophizing Scale", "type": "IntellectualProduct"}, {"text": "PCS", "type": "IntellectualProduct"}, {"text": "Tampa Scale of Kinesiophobia", "type": "IntellectualProduct"}, {"text": "TSK", "type": "IntellectualProduct"}]}

Example input:
Sentence: The mice exhibited significant freezing , even when the fear memory was no longer triggered by external CS , indicating that the artificial reactivation of a specific neuronal ensemble was sufficient to evoke the extinguished fear response .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}, {"text": "fear", "type": "BiologicFunction"}, {"text": "memory", "type": "BiologicFunction"}, {"text": "CS", "type": "BiologicFunction"}, {"text": "neuronal ensemble", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Low inhibitory capacity was associated with slower extinction of generalized fear of movement - related pain and pain expectancy .

Example answer:
{"entities": [{"text": "Low inhibitory capacity", "type": "BiologicFunction"}, {"text": "extinction", "type": "BiologicFunction"}, {"text": "generalized fear", "type": "BiologicFunction"}, {"text": "pain", "type": "Finding"}]}

Example input:
Sentence: The peak - shift effect describes a phenomenon whereby particular novel movements elicit even greater fear responses than the original pain - provoking movement ( CS + ) , because they represent a more extreme version of the CS + .

Example answer:
{"entities": [{"text": "movements", "type": "BiologicFunction"}, {"text": "fear responses", "type": "BiologicFunction"}, {"text": "pain - provoking", "type": "Finding"}, {"text": "movement", "type": "BiologicFunction"}, {"text": "CS +", "type": "BiologicFunction"}]}

Input:
Sentence: Fear elicited by a novel safe movement , situated outside the CS + / - continuum on the CS + side , can be as strong as to the original stimulus predicting the pain - onset .

## Item MedMentions:test:2695
Example input:
Sentence: Despite similar fat mass and energy balance , M ( IL10 ) mice were protected from aging - associated insulin resistance with significant increases in glucose infusion rates , whole - body glucose turnover , and skeletal muscle glucose uptake ( ∼60 % ; P < 0 . 05 ) , as compared to age -matched WT mice .

Example answer:
{"entities": [{"text": "energy balance", "type": "BiologicFunction"}, {"text": "M ( IL10 )", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "aging", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "glucose", "type": "Chemical"}, {"text": "whole - body", "type": "AnatomicalStructure"}, {"text": "skeletal muscle", "type": "AnatomicalStructure"}, {"text": "glucose uptake", "type": "BiologicFunction"}, {"text": "WT mice", "type": "Eukaryote"}]}

Example input:
Sentence: In DIO mice , chronic treatment with compound - 326 lowered insulin resistance and caused body weight loss without significant impact on cumulative calorie intake .

Example answer:
{"entities": [{"text": "DIO mice", "type": "Eukaryote"}, {"text": "compound - 326", "type": "Chemical"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "body weight loss", "type": "Finding"}]}

Example input:
Sentence: To investigate , we examined glucose metabolism in 18 - mo - old transgenic mice with muscle - specific overexpression of IL - 10 ( M ( IL10 ) ) and in wild - type mice during hyperinsulinemic - euglycemic clamping .

Example answer:
{"entities": [{"text": "glucose metabolism", "type": "BiologicFunction"}, {"text": "transgenic mice", "type": "Eukaryote"}, {"text": "muscle", "type": "AnatomicalStructure"}, {"text": "overexpression", "type": "BiologicFunction"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "M ( IL10 )", "type": "Chemical"}, {"text": "wild - type mice", "type": "Eukaryote"}, {"text": "hyperinsulinemic - euglycemic clamping", "type": "HealthCareActivity"}]}

Example input:
Sentence: High - fidelity Glucagon - CreER mouse line generated by CRISPR - Cas9 assisted gene targeting α - cells are the second most prominent cell type in pancreatic islets and are responsible for producing glucagon to increase plasma glucose levels in times of fasting .

Example answer:
{"entities": [{"text": "Glucagon - CreER mouse line", "type": "AnatomicalStructure"}, {"text": "gene targeting", "type": "ResearchActivity"}, {"text": "α - cells", "type": "AnatomicalStructure"}, {"text": "cell type", "type": "IntellectualProduct"}, {"text": "pancreatic islets", "type": "AnatomicalStructure"}, {"text": "glucagon", "type": "Chemical"}, {"text": "plasma glucose levels", "type": "Finding"}, {"text": "fasting", "type": "Finding"}]}

Example input:
Sentence: Our results demonstrates that mice challenged with Ts19 Frag - II presented biochemical alterations , increasing serum levels of urea , ALT and β - globulin , besides decreasing γ - globulins .

Example answer:
{"entities": [{"text": "mice", "type": "Eukaryote"}, {"text": "Ts19 Frag - II", "type": "Chemical"}, {"text": "biochemical", "type": "BiologicFunction"}, {"text": "serum levels of urea", "type": "Finding"}, {"text": "ALT", "type": "Chemical"}, {"text": "β - globulin", "type": "Chemical"}, {"text": "γ - globulins", "type": "Chemical"}]}

Example input:
Sentence: Finally , hPP2 - 36 , [ K ( 22 ) ( PEG22 ) ] hPP2 - 36 and [ K ( 22 ) ( PEG22 ) , Q ( 34 ) ] hPP significantly reduced cumulative food intake in mice over 16 h after s .

Example answer:
{"entities": [{"text": "hPP2 - 36", "type": "Chemical"}, {"text": "hPP", "type": "Chemical"}, {"text": "food intake", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Infusion of Ex - 9 decreased the time to peak glucose and rate of glucose decline during OGTT , and raised the postprandial nadir by over 70 % , normalising it relative to NSCs and preventing hypoglycaemia in all PBH participants .

Example answer:
{"entities": [{"text": "Infusion", "type": "HealthCareActivity"}, {"text": "Ex - 9", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "OGTT", "type": "HealthCareActivity"}, {"text": "hypoglycaemia", "type": "BiologicFunction"}, {"text": "PBH", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: Discovery and Optimization of a Novel Triazole Series of GPR142 Agonists for the Treatment of Type 2 Diabetes GPR142 has been identified as a potential glucose - stimulated insulin secretion ( GSIS ) target for the treatment of type 2 diabetes mellitus ( T2DM ) .

Example answer:
{"entities": [{"text": "Triazole Series", "type": "Chemical"}, {"text": "GPR142", "type": "Chemical"}, {"text": "Agonists", "type": "Chemical"}, {"text": "Type 2 Diabetes", "type": "BiologicFunction"}, {"text": "glucose - stimulated insulin secretion", "type": "BiologicFunction"}, {"text": "GSIS", "type": "BiologicFunction"}, {"text": "type 2 diabetes mellitus", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}]}

Example input:
Sentence: Compared with FH2D - group , FH2D + group had a significantly higher oral glucose tolerance test ( OGTT ) 2 - hour insulin , RBP4 and baPWV levels , a lower adiponectin and glucose infusing rate ( GIR ) ( P < 0 . 05 ) .

Example answer:
{"entities": [{"text": "FH2D -", "type": "Finding"}, {"text": "group", "type": "PopulationGroup"}, {"text": "FH2D +", "type": "Finding"}, {"text": "RBP4", "type": "Chemical"}, {"text": "adiponectin", "type": "HealthCareActivity"}]}

Example input:
Sentence: These studies provide strong evidence that reduction of glucose excursion through treatment with 20e is GPR142 -mediated , and GPR142 agonists could be used as a potential treatment for type 2 diabetes .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "glucose excursion", "type": "Finding"}, {"text": "20e", "type": "Chemical"}, {"text": "GPR142", "type": "Chemical"}, {"text": "agonists", "type": "Chemical"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}]}

Input:
Sentence: This optimization led to compound 20e , which showed significant reduction of glucose excursion in wild - type but not in GPR142 deficient mice in an oral glucose tolerance test ( oGTT ) study .

## Item MedMentions:test:2978
Example input:
Sentence: In fact , Behcet 's disease with neurological involvement ( neuro - Behcet 's disease ) is not uncommon .

Example answer:
{"entities": [{"text": "Behcet 's disease", "type": "BiologicFunction"}, {"text": "neurological involvement", "type": "BiologicFunction"}, {"text": "neuro - Behcet 's disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Central nervous system tumours profile at a referral center in the Brazilian Amazon region , 1997 - 2014 Tumours of the Central Nervous System ( CNS ) are an important cause of mortality from cancer .

Example answer:
{"entities": [{"text": "Central nervous system tumours", "type": "BiologicFunction"}, {"text": "profile", "type": "HealthCareActivity"}, {"text": "Amazon region", "type": "SpatialConcept"}, {"text": "Tumours of the Central Nervous System", "type": "BiologicFunction"}, {"text": "CNS", "type": "BodySystem"}, {"text": "cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Cases with concurrent flat carcinoma in - situ , angiolymphatic invasion , absent muscularis propria , or clinically advanced disease were excluded .

Example answer:
{"entities": [{"text": "flat carcinoma in - situ", "type": "Finding"}, {"text": "angiolymphatic invasion", "type": "Finding"}, {"text": "muscularis propria", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The disorder is associated with an increased predisposition for development of nervous system tumors , including pituitary adenomas .

Example answer:
{"entities": [{"text": "disorder", "type": "BiologicFunction"}, {"text": "nervous system tumors", "type": "BiologicFunction"}, {"text": "pituitary adenomas", "type": "BiologicFunction"}]}

Example input:
Sentence: Finally , we discuss the potential role of PSCs in pituitary tumorigenesis in the context of current models of carcinogenesis and present evidence showing that in contrast to pituitary adenoma , which follows a classical cancer stem cell paradigm , a novel mechanism has been revealed for paracrine , non - cell autonomous tumor initiation in adamantinomatous craniopharyngioma , a benign but clinically aggressive pediatric tumor .

Example answer:
{"entities": [{"text": "PSCs", "type": "AnatomicalStructure"}, {"text": "pituitary", "type": "AnatomicalStructure"}, {"text": "tumorigenesis", "type": "BiologicFunction"}, {"text": "carcinogenesis", "type": "BiologicFunction"}, {"text": "present", "type": "Finding"}, {"text": "pituitary adenoma", "type": "BiologicFunction"}, {"text": "cancer stem cell", "type": "AnatomicalStructure"}, {"text": "non - cell", "type": "AnatomicalStructure"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "adamantinomatous craniopharyngioma", "type": "BiologicFunction"}, {"text": "pediatric tumor", "type": "BiologicFunction"}]}

Example input:
Sentence: Abnormalities in NPC proliferation , differentiation , survival , or integration have been linked to various neurological diseases including Fragile X syndrome .

Example answer:
{"entities": [{"text": "Abnormalities", "type": "Finding"}, {"text": "NPC proliferation", "type": "BiologicFunction"}, {"text": "differentiation", "type": "BiologicFunction"}, {"text": "survival", "type": "BiologicFunction"}, {"text": "integration", "type": "BiologicFunction"}, {"text": "Fragile X syndrome", "type": "BiologicFunction"}]}

Example input:
Sentence: The results of the present study suggest that a neurological etiology could be added to the previously described structural etiology explaining the speech difficulties found in 22q11DS .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "speech difficulties", "type": "Finding"}, {"text": "22q11DS", "type": "BiologicFunction"}]}

Example input:
Sentence: Clinical manifestations may be complicated by the coexistence of both the original and subsequent neurological disorders .

Example answer:
{"entities": [{"text": "neurological disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: In addition , we found rare , functional mutations in known causal genes for neuropsychiatric disorders including holoprosencephaly and epilepsy .

Example answer:
{"entities": [{"text": "functional mutations", "type": "Finding"}, {"text": "causal genes", "type": "AnatomicalStructure"}, {"text": "neuropsychiatric disorders", "type": "BiologicFunction"}, {"text": "holoprosencephaly", "type": "AnatomicalStructure"}, {"text": "epilepsy", "type": "BiologicFunction"}]}

Example input:
Sentence: Individually each condition can be a classic paraneoplastic neurological syndrome .

Example answer:
{"entities": [{"text": "paraneoplastic neurological syndrome", "type": "BiologicFunction"}]}

Input:
Sentence: Whilst it could be argued that this could simply be a coincidence , the rarity of these conditions and the absence of an alternative aetiology for the neurological dysfunction argue in favour of a paraneoplastic phenomenon .

## Item MedMentions:test:2839
Example input:
Sentence: Quantitative real - time PCR analysis demonstrated that 5 of the 13 chloroplast proteins ATPF , PSAA , PSAB , PSBB and RBL in TP were higher abundance compared with those in DP .

Example answer:
{"entities": [{"text": "Quantitative real - time PCR analysis", "type": "ResearchActivity"}, {"text": "chloroplast proteins", "type": "Chemical"}, {"text": "ATPF", "type": "Chemical"}, {"text": "PSAA", "type": "Chemical"}, {"text": "PSAB", "type": "Chemical"}, {"text": "PSBB", "type": "Chemical"}, {"text": "RBL", "type": "Chemical"}, {"text": "TP", "type": "BiologicFunction"}]}

Example input:
Sentence: We cocultured MU N2 and MU 1615 which expresses red fluorescent protein ( RFP ) and Acanthamoeba polyphaga ( AP ) , and confirmed infected AP by Ziehl - Neelsen ( ZN ) staining .

Example answer:
{"entities": [{"text": "cocultured", "type": "HealthCareActivity"}, {"text": "MU N2", "type": "Bacterium"}, {"text": "MU 1615", "type": "Bacterium"}, {"text": "expresses red fluorescent protein", "type": "Chemical"}, {"text": "RFP", "type": "Chemical"}, {"text": "Acanthamoeba polyphaga", "type": "Eukaryote"}, {"text": "AP", "type": "Eukaryote"}, {"text": "infected", "type": "Finding"}, {"text": "Ziehl - Neelsen ( ZN ) staining", "type": "HealthCareActivity"}]}

Example input:
Sentence: Above a concentration threshold , these constructs undergo light - activated phase separation , forming spatiotemporally definable liquid optoDroplets .

Example answer:
{"entities": [{"text": "spatiotemporally", "type": "ResearchActivity"}, {"text": "optoDroplets", "type": "ResearchActivity"}]}

Example input:
Sentence: The RA of NASP , EEF1A1 , DNMT1 , ODC1 and RPS27A was increased ( P < 0 .

Example answer:
{"entities": [{"text": "NASP", "type": "AnatomicalStructure"}, {"text": "EEF1A1", "type": "AnatomicalStructure"}, {"text": "DNMT1", "type": "AnatomicalStructure"}, {"text": "ODC1", "type": "AnatomicalStructure"}, {"text": "RPS27A", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Furthermore , the nano - UCPs were superior to a traditional two - camera method for NIR and visible light path alignment in an in vivo Infrared - Laser - Evoked Gene Operator ( IR - LEGO ) optogenetics assay in the budding yeast Saccharomyces cerevisiae .

Example answer:
{"entities": [{"text": "UCPs", "type": "Chemical"}, {"text": "camera", "type": "MedicalDevice"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "Infrared - Laser - Evoked Gene Operator ( IR - LEGO ) optogenetics assay", "type": "ResearchActivity"}, {"text": "Saccharomyces cerevisiae", "type": "Eukaryote"}]}

Example input:
Sentence: Nonlabens dokdonensis rhodopsin 2 ( NdR2 ) , was recently identified as a light - driven Na ( + ) pump .

Example answer:
{"entities": [{"text": "Nonlabens dokdonensis", "type": "Bacterium"}, {"text": "rhodopsin 2", "type": "Chemical"}, {"text": "NdR2", "type": "Chemical"}, {"text": "light - driven", "type": "BiologicFunction"}, {"text": "Na ( + ) pump", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , we introduce an optogenetic platform that uses light to activate IDR -mediated phase transitions in living cells .

Example answer:
{"entities": [{"text": "optogenetic", "type": "ResearchActivity"}, {"text": "IDR", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Manipulation of an existing crystal form unexpectedly results in interwoven packing networks with pseudo - translational symmetry Nonribosomal peptide synthetases ( NRPSs ) are multimodular enzymes that synthesize a myriad of diverse molecules .

Example answer:
{"entities": [{"text": "crystal form", "type": "Chemical"}, {"text": "unexpectedly results", "type": "Finding"}, {"text": "interwoven packing networks", "type": "Chemical"}, {"text": "Nonribosomal peptide synthetases", "type": "Chemical"}, {"text": "NRPSs", "type": "Chemical"}, {"text": "multimodular enzymes", "type": "Chemical"}]}

Example input:
Sentence: The acute phase proteins haptoglobin , apolipoprotein A - I and α1 - antichymotrypsin 3 , and the antioxidant enzyme peroxiredoxin 2 were found differentially expressed by 2D - DIGE .

Example answer:
{"entities": [{"text": "acute phase proteins", "type": "Chemical"}, {"text": "haptoglobin", "type": "Chemical"}, {"text": "apolipoprotein A - I", "type": "Chemical"}, {"text": "antioxidant", "type": "Chemical"}, {"text": "peroxiredoxin 2", "type": "Chemical"}, {"text": "2D - DIGE", "type": "HealthCareActivity"}]}

Example input:
Sentence: Spatiotemporal Control of Intracellular Phase Transitions Using Light - Activated optoDroplets Phase transitions driven by intrinsically disordered protein regions ( IDRs ) have emerged as a ubiquitous mechanism for assembling liquid - like RNA / protein ( RNP ) bodies and other membrane - less organelles .

Example answer:
{"entities": [{"text": "Spatiotemporal", "type": "ResearchActivity"}, {"text": "Intracellular", "type": "SpatialConcept"}, {"text": "Light - Activated optoDroplets", "type": "ResearchActivity"}, {"text": "intrinsically disordered protein regions", "type": "Chemical"}, {"text": "IDRs", "type": "Chemical"}, {"text": "RNA / protein", "type": "Chemical"}, {"text": "RNP", "type": "Chemical"}, {"text": "bodies", "type": "AnatomicalStructure"}, {"text": "membrane - less organelles", "type": "AnatomicalStructure"}]}

Input:
Sentence: We use this " optoDroplet " system to study condensed phases driven by the IDRs of various RNP body proteins , including FUS , DDX4 , and HNRNPA1 .

## Item MedMentions:test:2700
Example input:
Sentence: Selective activation of intestinal Lxrα holds therapeutic promise .

Example answer:
{"entities": [{"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "Lxrα", "type": "Chemical"}]}

Example input:
Sentence: The UPR has long been known to regulate phospholipid metabolism , and Lpl1 ' s relationship with Hac1 appears to reflect Hac1 ' s role in stimulating phospholipid synthesis under stress .

Example answer:
{"entities": [{"text": "UPR", "type": "BiologicFunction"}, {"text": "regulate phospholipid metabolism", "type": "BiologicFunction"}, {"text": "Lpl1", "type": "Chemical"}, {"text": "Hac1", "type": "Chemical"}, {"text": "phospholipid synthesis", "type": "BiologicFunction"}]}

Example input:
Sentence: The platelet - activating receptor C - type lectin receptor - 2 plays an essential role in liver regeneration after partial hepatectomy in mice Essentials Regeneration role of C - type lectin receptor - 2 ( CLEC - 2 ) after 70 % hepatectomy ( HPx ) was investigated .

Example answer:
{"entities": [{"text": "platelet - activating receptor", "type": "Chemical"}, {"text": "C - type lectin receptor - 2", "type": "Chemical"}, {"text": "liver regeneration", "type": "BiologicFunction"}, {"text": "partial hepatectomy", "type": "HealthCareActivity"}, {"text": "mice", "type": "Eukaryote"}, {"text": "Regeneration", "type": "BiologicFunction"}, {"text": "CLEC - 2", "type": "Chemical"}, {"text": "70 % hepatectomy", "type": "HealthCareActivity"}, {"text": "HPx", "type": "HealthCareActivity"}]}

Example input:
Sentence: Liver expression of canalicular phospholipid ( ABCB4 ) , bile acid ( ABCB11 ) , and sterol ( ABCG5 / 8 ) transporters , their upstream regulators LXR and FXR as well as pro - inflammatory cytokines interleukin - 6 ( IL6 ) and tumor necrosis factor ( TNF ) were investigated among patients with IF [ age median 3 .

Example answer:
{"entities": [{"text": "Liver", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "canalicular", "type": "AnatomicalStructure"}, {"text": "phospholipid", "type": "Chemical"}, {"text": "ABCB4", "type": "Chemical"}, {"text": "bile acid", "type": "Chemical"}, {"text": "ABCB11", "type": "Chemical"}, {"text": "sterol", "type": "Chemical"}, {"text": "ABCG5 / 8", "type": "Chemical"}, {"text": "transporters", "type": "Chemical"}, {"text": "upstream regulators", "type": "Chemical"}, {"text": "LXR", "type": "Chemical"}, {"text": "FXR", "type": "Chemical"}, {"text": "pro - inflammatory cytokines", "type": "Chemical"}, {"text": "interleukin - 6", "type": "Chemical"}, {"text": "IL6", "type": "Chemical"}, {"text": "tumor necrosis factor", "type": "Chemical"}, {"text": "TNF", "type": "Chemical"}, {"text": "IF", "type": "BiologicFunction"}]}

Example input:
Sentence: However , the roles of apoliprotein ( Apo ) E ( Apoe ) and low - density lipoprotein ( Ldl ) receptor ( Ldlr ) in colorectal carcinogenesis have not yet been investigated .

Example answer:
{"entities": [{"text": "apoliprotein ( Apo ) E", "type": "Chemical"}, {"text": "Apoe", "type": "Chemical"}, {"text": "low - density lipoprotein ( Ldl ) receptor", "type": "Chemical"}, {"text": "Ldlr", "type": "Chemical"}, {"text": "colorectal carcinogenesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Role of Intestinal LXRα in Regulating Post - prandial Lipid Excursion and Diet - Induced Hypercholesterolemia and Hepatic Lipid Accumulation Post - prandial hyperlipidemia has emerged as a cardiovascular risk factor with limited therapeutic options .

Example answer:
{"entities": [{"text": "Intestinal", "type": "AnatomicalStructure"}, {"text": "LXRα", "type": "Chemical"}, {"text": "Regulating", "type": "BiologicFunction"}, {"text": "Lipid", "type": "Chemical"}, {"text": "Diet", "type": "Food"}, {"text": "Hypercholesterolemia", "type": "BiologicFunction"}, {"text": "Hepatic", "type": "SpatialConcept"}, {"text": "Lipid Accumulation", "type": "Finding"}, {"text": "hyperlipidemia", "type": "BiologicFunction"}, {"text": "cardiovascular", "type": "SpatialConcept"}, {"text": "risk factor", "type": "Finding"}, {"text": "therapeutic options", "type": "HealthCareActivity"}]}

Example input:
Sentence: These results showed that AVP and its receptors may be important in the modulation of the proliferation rate of the biliary epithelium .

Example answer:
{"entities": [{"text": "AVP", "type": "Chemical"}, {"text": "receptors", "type": "Chemical"}, {"text": "proliferation rate", "type": "Finding"}]}

Example input:
Sentence: Here we hypothesize that biliary phospholipid flow could directly contribute to the proliferative power of normal and dysplastic enterocytes .

Example answer:
{"entities": [{"text": "biliary", "type": "AnatomicalStructure"}, {"text": "phospholipid", "type": "Chemical"}, {"text": "normal", "type": "AnatomicalStructure"}, {"text": "dysplastic enterocytes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In turn , phospholipids cannot re - establish intestinal tumorigenesis in Abcb4 ( - / - ) mice crossed with mice with intestinal specific ablation of Lrh1 , a nuclear hormone receptor that is activates by phospholipids .

Example answer:
{"entities": [{"text": "phospholipids", "type": "Chemical"}, {"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "tumorigenesis", "type": "BiologicFunction"}, {"text": "Abcb4", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "ablation", "type": "HealthCareActivity"}, {"text": "Lrh1", "type": "Chemical"}, {"text": "nuclear hormone receptor", "type": "Chemical"}]}

Example input:
Sentence: Biliary Phospholipids Sustain Enterocyte Proliferation and Intestinal Tumor Progression via Nuclear Receptor Lrh1 in mice The proliferative - crypt compartment of the intestinal epithelium is enriched in phospholipids and accumulation of phospholipids has been described in colorectal tumors .

Example answer:
{"entities": [{"text": "Biliary", "type": "AnatomicalStructure"}, {"text": "Phospholipids", "type": "Chemical"}, {"text": "Enterocyte", "type": "AnatomicalStructure"}, {"text": "Proliferation", "type": "BiologicFunction"}, {"text": "Intestinal Tumor", "type": "BiologicFunction"}, {"text": "Progression", "type": "BiologicFunction"}, {"text": "Nuclear Receptor", "type": "Chemical"}, {"text": "Lrh1", "type": "Chemical"}, {"text": "mice", "type": "Eukaryote"}, {"text": "intestinal epithelium", "type": "AnatomicalStructure"}, {"text": "phospholipids", "type": "Chemical"}, {"text": "accumulation", "type": "Finding"}, {"text": "colorectal tumors", "type": "BiologicFunction"}]}

Input:
Sentence: Our data identify the key role of biliary phospholipids in sustaining intestinal mucosa proliferation and tumor progression through the activation of nuclear receptor Lrh1 .

## Item MedMentions:test:2834
Example input:
Sentence: The multivariate analysis revealed that TN MBC patients had poorer OS and BCSM ( p < 0 .

Example answer:
{"entities": [{"text": "TN", "type": "Finding"}, {"text": "MBC", "type": "BiologicFunction"}]}

Example input:
Sentence: We also found that allele ' C ' of rs11030096 was associated with an increased risk of addiction in the dominant model and additive model ( p < 0 .

Example answer:
{"entities": [{"text": "allele ' C", "type": "AnatomicalStructure"}, {"text": "rs11030096", "type": "AnatomicalStructure"}, {"text": "addiction", "type": "BiologicFunction"}, {"text": "dominant model", "type": "IntellectualProduct"}, {"text": "additive model", "type": "IntellectualProduct"}]}

Example input:
Sentence: These convergent findings from mouse and hiPSC SZ models provide evidence for STEP61 dysfunction in SZ .Molecular Psychiatry advance online publication , 18 October 2016 ; doi : 10 . 1038 / mp . 2016 .

Example answer:
{"entities": [{"text": "findings", "type": "Finding"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "hiPSC", "type": "AnatomicalStructure"}, {"text": "SZ", "type": "BiologicFunction"}, {"text": "models", "type": "BiologicFunction"}, {"text": "STEP61", "type": "Chemical"}]}

Example input:
Sentence: Multivariate Imaging Genetics Study of MRI Gray Matter Volume and SNPs Reveals Biological Pathways Correlated with Brain Structural Differences in Attention Deficit Hyperactivity Disorder Attention deficit hyperactivity disorder ( ADHD ) is a prevalent neurodevelopmental disorder affecting children , adolescents , and adults .

Example answer:
{"entities": [{"text": "Imaging", "type": "HealthCareActivity"}, {"text": "Genetics Study", "type": "ResearchActivity"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "Gray Matter", "type": "AnatomicalStructure"}, {"text": "SNPs", "type": "SpatialConcept"}, {"text": "Brain", "type": "AnatomicalStructure"}, {"text": "Structural", "type": "SpatialConcept"}, {"text": "Attention Deficit Hyperactivity Disorder", "type": "BiologicFunction"}, {"text": "Attention deficit hyperactivity disorder", "type": "BiologicFunction"}, {"text": "ADHD", "type": "BiologicFunction"}, {"text": "neurodevelopmental disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: In this sample of Egyptian females , ACE I / D polymorphism was not significantly associated with obesity nor with any of its related disorders studied .

Example answer:
{"entities": [{"text": "Egyptian", "type": "PopulationGroup"}, {"text": "ACE I / D polymorphism", "type": "Finding"}, {"text": "not significantly", "type": "Finding"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: Our objective was to study the association of ACE I / D polymorphism with obesity and certain related disorders , namely hypertension , insulin resistance and metabolic syndrome , in Egyptian females .

Example answer:
{"entities": [{"text": "objective", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "ACE I / D polymorphism", "type": "Finding"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "disorders", "type": "BiologicFunction"}, {"text": "hypertension", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "metabolic syndrome", "type": "BiologicFunction"}, {"text": "Egyptian", "type": "PopulationGroup"}]}

Example input:
Sentence: Array comparative genomic hybridization and metaphase fluorescence in situ hybridization analyses were performed on the peripheral blood to determine the origin and mosaicism of the sSMC , and quantitative fluorescent polymerase chain reaction was used to exclude uniparental disomy .

Example answer:
{"entities": [{"text": "Array comparative genomic hybridization", "type": "ResearchActivity"}, {"text": "metaphase fluorescence in situ hybridization analyses", "type": "ResearchActivity"}, {"text": "peripheral blood", "type": "BodySubstance"}, {"text": "sSMC", "type": "AnatomicalStructure"}, {"text": "quantitative fluorescent polymerase chain reaction", "type": "HealthCareActivity"}, {"text": "uniparental disomy", "type": "BiologicFunction"}]}

Example input:
Sentence: The sSMC ( 8 ) was r ( 8 ) ( : : p11 .

Example answer:
{"entities": [{"text": "sSMC ( 8 )", "type": "AnatomicalStructure"}, {"text": "r ( 8 ) ( : : p11 .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Molecular cytogenetic characterization of mosaicism for a small supernumerary marker chromosome derived from chromosome 8 or r ( 8 ) ( : : p11 .

Example answer:
{"entities": [{"text": "small supernumerary marker chromosome", "type": "AnatomicalStructure"}, {"text": "chromosome 8", "type": "AnatomicalStructure"}, {"text": "r ( 8 ) ( : : p11 .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 22→q11 . 21 : : ) in an 18 - year - old female with short stature , obesity , attention deficit hyperactivity disorder , and intellectual disability We present molecular cytogenetic characterization of mosaicism for a small supernumerary marker chromosome ( sSMC ) derived from chromosome 8 .

Example answer:
{"entities": [{"text": "22→q11 . 21 : : )", "type": "AnatomicalStructure"}, {"text": "female", "type": "PopulationGroup"}, {"text": "short stature", "type": "Finding"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "attention deficit hyperactivity disorder", "type": "BiologicFunction"}, {"text": "intellectual disability", "type": "BiologicFunction"}, {"text": "small supernumerary marker chromosome", "type": "AnatomicalStructure"}, {"text": "sSMC", "type": "AnatomicalStructure"}, {"text": "chromosome 8", "type": "AnatomicalStructure"}]}

Input:
Sentence: Mosaic sSMC ( 8 ) derived from r ( 8 ) ( : : p11 . 22→q11 . 21 : : ) can be associated with obesity , intellectual disability , and attention deficit hyperactivity disorder .

## Item MedMentions:test:3114
Example input:
Sentence: 9 ± 1 . 0 , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 9 ± 1 .

Example answer:
{"entities": []}

Example input:
Sentence: 15±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 15±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 9 to 277 . 1 ± 16 .

Example answer:
{"entities": []}

Example input:
Sentence: 9 vs 5 . 1 ± 10 .

Example answer:
{"entities": []}

Example input:
Sentence: 9 vs . 45 . 9±1 .

Example answer:
{"entities": []}

Example input:
Sentence: 09±13 .

Example answer:
{"entities": []}

Example input:
Sentence: 89±3 .

Example answer:
{"entities": []}

Example input:
Sentence: 9±2 .

Example answer:
{"entities": []}

Input:
Sentence: 9±15 .

## Item MedMentions:test:3123
Example input:
Sentence: 3 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 4 and 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 , 42 . 4 , and 66 .

Example answer:
{"entities": []}

Example input:
Sentence: 3±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 3±0 .

Example answer:
{"entities": []}

Example input:
Sentence: 3±0 .

Example answer:
{"entities": []}

Example input:
Sentence: All 3 A .

Example answer:
{"entities": [{"text": "A .", "type": "Eukaryote"}]}

Example input:
Sentence: 3 - 28 .

Example answer:
{"entities": []}

Example input:
Sentence: a 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 3 at . % .

Example answer:
{"entities": []}

Input:
Sentence: 3 at .

## Item MedMentions:test:3129
Example input:
Sentence: 4 to 0 . 8 .

Example answer:
{"entities": []}

Example input:
Sentence: 06 to 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 61 , 0 . 67 and 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 7 ± 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 07 - 0 . 46 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 7 at baseline and 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 7 ( range = 0 - 15 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 7 - 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 7 - 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 7 ( range 0 - 8 ) .

Example answer:
{"entities": []}

Input:
Sentence: 0 to 7 .

## Item MedMentions:test:2850
Example input:
Sentence: DR - 70 , a marker used to measure fibrin degradation products , generated by all major cancers , may helps to find high risk lung cancer patients .

Example answer:
{"entities": [{"text": "DR - 70", "type": "Chemical"}, {"text": "marker", "type": "Chemical"}, {"text": "fibrin degradation products", "type": "Chemical"}, {"text": "cancers", "type": "BiologicFunction"}, {"text": "high risk", "type": "Finding"}, {"text": "lung cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: The ratio of FDP to fibrinogen and the ratio of D - dimer to fibrinogen were the most accurate markers .

Example answer:
{"entities": [{"text": "accurate markers", "type": "MedicalDevice"}]}

Example input:
Sentence: Many foot care professionals recommend offloading measures as part of management strategies for modulating excess pressure to prevent development of diabetic foot ulcers ( DFUs ) .

Example answer:
{"entities": [{"text": "foot care", "type": "HealthCareActivity"}, {"text": "professionals", "type": "ProfessionalOrOccupationalGroup"}, {"text": "diabetic foot ulcers", "type": "BiologicFunction"}, {"text": "DFUs", "type": "BiologicFunction"}]}

Example input:
Sentence: Levels of fibrin degradation products ( FDP ) , D - dimer , fibrinogen , the ratio of FDP to fibrinogen , the ratio of D - dimer to fibrinogen , systolic blood pressure , heart rate , the Glasgow Coma Scale , pH , base excess , hemoglobin and lactate levels , the pattern of pelvic injury , and injury severity score were measured at hospital admission , and compared between the two groups .

Example answer:
{"entities": [{"text": "fibrin degradation products", "type": "HealthCareActivity"}, {"text": "FDP", "type": "HealthCareActivity"}, {"text": "D - dimer", "type": "HealthCareActivity"}, {"text": "fibrinogen", "type": "HealthCareActivity"}, {"text": "ratio of FDP to fibrinogen", "type": "HealthCareActivity"}, {"text": "ratio of D - dimer to fibrinogen", "type": "HealthCareActivity"}, {"text": "systolic blood pressure", "type": "ClinicalAttribute"}, {"text": "heart rate", "type": "ClinicalAttribute"}, {"text": "Glasgow Coma Scale", "type": "IntellectualProduct"}, {"text": "base excess", "type": "HealthCareActivity"}, {"text": "hemoglobin", "type": "HealthCareActivity"}, {"text": "lactate", "type": "HealthCareActivity"}, {"text": "pelvic injury", "type": "InjuryOrPoisoning"}, {"text": "injury severity score", "type": "IntellectualProduct"}, {"text": "hospital admission", "type": "HealthCareActivity"}]}

Example input:
Sentence: To identify , critically appraise and synthesize the best available evidence on methods of offloading to prevent the development , and reduce the risk , of primary foot ulceration in adults with diabetes .The question addressed by the review was : what is the effectiveness of methods of offloading in preventing primary DFUs in adults with diabetes ? Adults 18 years and older with diabetes mellitus , regardless of age , gender , ethnicity , duration or type of diabetes , with no history of DFUs and in any clinical setting will be included .

Example answer:
{"entities": [{"text": "methods", "type": "HealthCareActivity"}, {"text": "foot ulceration", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "addressed", "type": "IntellectualProduct"}, {"text": "review", "type": "IntellectualProduct"}, {"text": "DFUs", "type": "BiologicFunction"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "history", "type": "Finding"}]}

Example input:
Sentence: Fibrinogen values were found to be correlated with CRP levels , neutrophil , and WBC count .

Example answer:
{"entities": [{"text": "Fibrinogen values", "type": "Finding"}, {"text": "CRP levels", "type": "Finding"}, {"text": "neutrophil", "type": "HealthCareActivity"}, {"text": "WBC count", "type": "HealthCareActivity"}]}

Example input:
Sentence: Mean fibrinogen values were significantly higher in patients with DFU grade ≧ 3 compared to those with DFU grades 1 - 2 ( 5 . 23 ± 1 .

Example answer:
{"entities": [{"text": "fibrinogen values", "type": "Finding"}, {"text": "DFU", "type": "BiologicFunction"}, {"text": "grade", "type": "IntellectualProduct"}, {"text": "grades", "type": "IntellectualProduct"}]}

Example input:
Sentence: A retrospective study was designed to examine the utility of fibrinogen in estimating disease severity in patients with DFU admitted to our hospital between January 2015 and January 2016 .

Example answer:
{"entities": [{"text": "retrospective study", "type": "ResearchActivity"}, {"text": "fibrinogen", "type": "Chemical"}, {"text": "DFU", "type": "BiologicFunction"}, {"text": "admitted", "type": "HealthCareActivity"}, {"text": "hospital", "type": "Organization"}]}

Example input:
Sentence: Fibrinogen : A Marker in Predicting Diabetic Foot Ulcer Severity Aims .

Example answer:
{"entities": [{"text": "Fibrinogen", "type": "Chemical"}, {"text": "Marker", "type": "ClinicalAttribute"}, {"text": "Diabetic Foot Ulcer", "type": "BiologicFunction"}]}

Example input:
Sentence: Fibrinogen levels might be a valuable tool for assessing the disease severity and monitoring the disease progression in patients with DFU .

Example answer:
{"entities": [{"text": "Fibrinogen levels", "type": "Finding"}, {"text": "assessing", "type": "HealthCareActivity"}, {"text": "monitoring", "type": "HealthCareActivity"}, {"text": "disease progression", "type": "BiologicFunction"}, {"text": "DFU", "type": "BiologicFunction"}]}

Input:
Sentence: To examine whether fibrinogen levels are a valuable biomarker for assessing disease severity and monitoring disease progression in patients with diabetic foot ulcer ( DFU ) .

## Item MedMentions:test:2892
Example input:
Sentence: Violence perpetrated by nurse colleagues had a significant relationship with all four job outcomes , while violence by physicians had a significant inverse relationship with job satisfaction .

Example answer:
{"entities": [{"text": "Violence", "type": "BiologicFunction"}, {"text": "nurse", "type": "ProfessionalOrOccupationalGroup"}, {"text": "violence", "type": "BiologicFunction"}, {"text": "physicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "job satisfaction", "type": "BiologicFunction"}]}

Example input:
Sentence: 41 % , P = 0 . 003 ) , although women were more symptomatic and much older .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "much older", "type": "Finding"}]}

Example input:
Sentence: At the same time , 61 % of students showed high perceived stress levels .

Example answer:
{"entities": [{"text": "students", "type": "ProfessionalOrOccupationalGroup"}, {"text": "perceived", "type": "BiologicFunction"}]}

Example input:
Sentence: For mental health and substance use services , three classes emerged ( stable - low , 69 % and 61 % , respectively ; low - baseline - increase , 10 % and 12 % , respectively ; high - baseline decline , 21 % and 28 % , respectively ) .

Example answer:
{"entities": [{"text": "mental health", "type": "BiologicFunction"}, {"text": "services", "type": "HealthCareActivity"}]}

Example input:
Sentence: Participants included 500 emerging adults ( 49 . 6 % male ) who completed an online battery of questionnaires assessing history of child maltreatment and dimensions of alexithymia .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "questionnaires", "type": "IntellectualProduct"}, {"text": "child maltreatment", "type": "BiologicFunction"}, {"text": "alexithymia", "type": "Finding"}]}

Example input:
Sentence: The most common events were " Hospitalization of a family member " ( 24 % ) , " Getting a bad report card " ( 20 % ) , " Serious arguments between parents " ( 19 % ) , and " Serious illness / injury in a family member " ( 19 % ) .

Example answer:
{"entities": [{"text": "Hospitalization", "type": "HealthCareActivity"}, {"text": "Getting a bad report card", "type": "Finding"}, {"text": "Serious illness", "type": "Finding"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: 15 % , p = 1 . 000 ) , likewise bullying ( p = 0 . 088 ) .

Example answer:
{"entities": [{"text": "bullying", "type": "BiologicFunction"}]}

Example input:
Sentence: At baseline , 14 % reported being cybervictims , 8 % reported being cyberbullies , and 20 % reported being cyberbully - victims in the previous year .

Example answer:
{"entities": [{"text": "reported", "type": "IntellectualProduct"}, {"text": "cyberbullies", "type": "PopulationGroup"}]}

Example input:
Sentence: In this subgroup , the male : female ratio is 4 . 57 : 1 ; 37 . 18 % of presentations were associated with a fracture ( n = 29 ) and 35 . 90 % ( n = 28 ) of patients re - presented following another punch injury , as a victim of violence , or by other psychiatric presentation .

Example answer:
{"entities": [{"text": "subgroup", "type": "IntellectualProduct"}, {"text": "fracture", "type": "InjuryOrPoisoning"}, {"text": "punch", "type": "BiologicFunction"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "victim of violence", "type": "Finding"}]}

Example input:
Sentence: Approximately three quarters of the nurses had experienced at least one type of violence .

Example answer:
{"entities": [{"text": "nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "experienced", "type": "BiologicFunction"}, {"text": "violence", "type": "BiologicFunction"}]}

Input:
Sentence: Verbal abuse was most prevalent ( 59 . 6 % ) , followed by threats of violence ( 36 . 9 % ) , physical violence ( 27 . 6 % ) , bullying ( 25 . 6 % ) , and sexual harassment ( 22 .

## Item MedMentions:test:2858
Example input:
Sentence: Through impoverishment expenditure assessment , the proportions of impoverishment payment are low among both urban and rural residents , but the 7 rare diseases could lead nearly 4 . 6 million people into poverty on a national scale .

Example answer:
{"entities": [{"text": "urban", "type": "PopulationGroup"}, {"text": "rural residents", "type": "PopulationGroup"}, {"text": "rare diseases", "type": "BiologicFunction"}, {"text": "people", "type": "PopulationGroup"}]}

Example input:
Sentence: The incidence of OCS was calculated based on the total number of craniomaxillofacial ( CMF ) emergencies .

Example answer:
{"entities": [{"text": "OCS", "type": "BiologicFunction"}, {"text": "craniomaxillofacial", "type": "SpatialConcept"}, {"text": "CMF", "type": "SpatialConcept"}, {"text": "emergencies", "type": "BiologicFunction"}]}

Example input:
Sentence: Through catastrophic expenditure assessment , proportions of the population experiencing catastrophic expenditure caused by the 7 rare diseases are all under 0 .

Example answer:
{"entities": [{"text": "population", "type": "PopulationGroup"}, {"text": "rare diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: However , once one is ill and taking medications , he will suffer from catastrophic health expenditure .

Example answer:
{"entities": [{"text": "ill", "type": "Finding"}, {"text": "medications", "type": "IntellectualProduct"}]}

Example input:
Sentence: Conducting a cross - sectional survey in Greece in 2013 , we find that the combination of SHI - PHI has a strong negative influence on insured OOP payments for inpatient health care in private hospitals .

Example answer:
{"entities": [{"text": "cross - sectional survey", "type": "ResearchActivity"}, {"text": "Greece", "type": "SpatialConcept"}, {"text": "find", "type": "Finding"}, {"text": "SHI - PHI", "type": "HealthCareActivity"}, {"text": "negative", "type": "Finding"}, {"text": "health care", "type": "HealthCareActivity"}, {"text": "private hospitals", "type": "Organization"}]}

Example input:
Sentence: Drawing evidence from Greece , a country with huge fiscal problems that has suffered the consequences of the economic crisis more than any other , could be a starting point for policymakers to consider the perspective of SHI - PHI co - operation against OOP payments more seriously .

Example answer:
{"entities": [{"text": "Greece", "type": "SpatialConcept"}, {"text": "country", "type": "SpatialConcept"}, {"text": "fiscal problems", "type": "Finding"}, {"text": "suffered", "type": "Finding"}, {"text": "SHI - PHI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Worsening fracture classification and self - payment / Medicaid payment trended toward increasing opioid consumption .

Example answer:
{"entities": [{"text": "fracture classification", "type": "IntellectualProduct"}]}

Example input:
Sentence: Catastrophic health expenditure : a comparative analysis of empty - nest and non - empty - nest households with seniors in Shandong , China The aim of this study was to compare the catastrophic health expenditure ( CHE ) prevalence and its determinants between empty - nest and non - empty - nest elderly households .

Example answer:
{"entities": [{"text": "Catastrophic", "type": "BiologicFunction"}, {"text": "seniors", "type": "PopulationGroup"}, {"text": "Shandong , China", "type": "SpatialConcept"}, {"text": "study", "type": "ResearchActivity"}, {"text": "catastrophic", "type": "BiologicFunction"}, {"text": "elderly", "type": "PopulationGroup"}]}

Example input:
Sentence: Combined social and private health insurance versus catastrophic out of pocket payments for private hospital care in Greece The high level of out of pocket ( OOP ) payments constitutes a major concern for Greece and several other European and OECD countries as a result of the significant down turning of their public health finances due to the 2008 financial crisis .

Example answer:
{"entities": [{"text": "social", "type": "HealthCareActivity"}, {"text": "private health insurance", "type": "HealthCareActivity"}, {"text": "private hospital care", "type": "Organization"}, {"text": "Greece", "type": "SpatialConcept"}, {"text": "European", "type": "SpatialConcept"}, {"text": "OECD", "type": "Organization"}, {"text": "countries", "type": "SpatialConcept"}]}

Example input:
Sentence: Moreover , we find that poor people present a greater tendency to incur catastrophic OOP expenditures for hospital health care in private providers .

Example answer:
{"entities": [{"text": "find", "type": "Finding"}, {"text": "people", "type": "PopulationGroup"}, {"text": "hospital health care", "type": "HealthCareActivity"}, {"text": "private providers", "type": "Organization"}]}

Input:
Sentence: Further , this study examines the catastrophic impact of OOP payments on insured 's welfare using the incidence and intensity methodological approach of measuring catastrophic health care expenditures .

## Item MedMentions:test:3030
Example input:
Sentence: The involvement of spinal astrocytes in the pathogenesis of paclitaxel - induced neuropathy has been reported , but little is known about the role of fluorocitrate ( FC ) , a selective inhibitor of astrocyte activation , during neuropathic pain related to paclitaxel treatment .

Example answer:
{"entities": [{"text": "spinal", "type": "AnatomicalStructure"}, {"text": "astrocytes", "type": "AnatomicalStructure"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "neuropathy", "type": "BiologicFunction"}, {"text": "fluorocitrate", "type": "Chemical"}, {"text": "FC", "type": "Chemical"}, {"text": "astrocyte activation", "type": "BiologicFunction"}, {"text": "neuropathic pain", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: After stereo - tactic radiation therapy in combination with chemotherapy , she is currently in remission from her lymphoma and has normalized IGF - 1 levels without medical therapy , 8 months after her histopathological diagnosis .

Example answer:
{"entities": [{"text": "stereo - tactic radiation therapy", "type": "HealthCareActivity"}, {"text": "chemotherapy", "type": "HealthCareActivity"}, {"text": "remission", "type": "BiologicFunction"}, {"text": "lymphoma", "type": "BiologicFunction"}, {"text": "normalized", "type": "ResearchActivity"}, {"text": "IGF - 1", "type": "Chemical"}, {"text": "medical therapy", "type": "HealthCareActivity"}, {"text": "diagnosis", "type": "Finding"}]}

Example input:
Sentence: Alizarin Red staining showed markedly increased mineralized nodules as compared with only melatonin - treated or laser - irradiated cells at day 7 , which significantly increased by day 14 .

Example answer:
{"entities": [{"text": "Alizarin Red staining", "type": "HealthCareActivity"}, {"text": "mineralized", "type": "BiologicFunction"}, {"text": "nodules", "type": "BiologicFunction"}, {"text": "melatonin", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: However , it also promotes accelerated senescence in healthy tissues and leads to progressive cognitive dysfunction in up to 50 % of tumor patients surviving long term after treatment , due to γ - irradiation -induced cerebromicrovascular injury .

Example answer:
{"entities": [{"text": "senescence", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "cognitive dysfunction", "type": "BiologicFunction"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Predictors of neurologic and nonneurologic death in patients with brain metastasis initially treated with upfront stereotactic radiosurgery without whole - brain radiation therapy In this study we attempted to discern the factors predictive of neurologic death in patients with brain metastasis treated with upfront stereotactic radiosurgery ( SRS ) without whole brain radiation therapy ( WBRT ) while accounting for the competing risk of nonneurologic death .

Example answer:
{"entities": [{"text": "neurologic", "type": "BiologicFunction"}, {"text": "nonneurologic death", "type": "Finding"}, {"text": "brain metastasis", "type": "BiologicFunction"}, {"text": "upfront stereotactic radiosurgery", "type": "HealthCareActivity"}, {"text": "whole - brain radiation therapy", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "neurologic death", "type": "BiologicFunction"}, {"text": "SRS", "type": "HealthCareActivity"}, {"text": "whole brain radiation therapy", "type": "HealthCareActivity"}, {"text": "WBRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: A 39 - year - old Caucasian female with a past medical history of RSTS diagnosed at age two was found to have a gadolinium -enhancing pituitary mass on magnetic resonance imaging ( MRI ) of the brain three years ago during workup for migraine - like headaches .

Example answer:
{"entities": [{"text": "Caucasian", "type": "PopulationGroup"}, {"text": "female", "type": "PopulationGroup"}, {"text": "past medical history", "type": "Finding"}, {"text": "RSTS", "type": "BiologicFunction"}, {"text": "diagnosed", "type": "Finding"}, {"text": "gadolinium", "type": "Chemical"}, {"text": "pituitary mass", "type": "AnatomicalStructure"}, {"text": "magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "migraine - like headaches", "type": "Finding"}]}

Example input:
Sentence: As a result of radiotherapy he developed an osteoradionecrosis of his mandible and a consecutive pathological fracture of his left mandibular angle .

Example answer:
{"entities": [{"text": "radiotherapy", "type": "HealthCareActivity"}, {"text": "osteoradionecrosis of his mandible", "type": "BiologicFunction"}, {"text": "pathological fracture", "type": "BiologicFunction"}]}

Example input:
Sentence: For 14 of these patients vestibular damage was diagnosed post - radiotherapy .

Example answer:
{"entities": [{"text": "vestibular damage", "type": "Finding"}, {"text": "diagnosed", "type": "Finding"}, {"text": "post - radiotherapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Visual outcome , endocrine function and tumor control after fractionated stereotactic radiation therapy of craniopharyngiomas in adults : findings in a prospective cohort The purpose of this study was to examine visual outcome , endocrine function and tumor control in a prospective cohort of craniopharyngioma patients , treated with fractionated stereotactic radiation therapy ( FSRT ) .

Example answer:
{"entities": [{"text": "endocrine function", "type": "BiologicFunction"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "fractionated stereotactic radiation therapy", "type": "HealthCareActivity"}, {"text": "craniopharyngiomas in adults", "type": "BiologicFunction"}, {"text": "prospective cohort", "type": "ResearchActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "examine", "type": "HealthCareActivity"}, {"text": "craniopharyngioma", "type": "BiologicFunction"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "FSRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: FSRT was relatively safe in this prospective cohort of craniopharyngiomas , with only one case of radiation - induced optic neuropathy and no case of new endocrinopathy .

Example answer:
{"entities": [{"text": "FSRT", "type": "HealthCareActivity"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "craniopharyngiomas", "type": "BiologicFunction"}, {"text": "radiation - induced optic neuropathy", "type": "BiologicFunction"}, {"text": "endocrinopathy", "type": "BiologicFunction"}]}

Input:
Sentence: One patient developed radiation - induced optic neuropathy at seven years after FSRT .

## Item MedMentions:test:2915
Example input:
Sentence: Half a year later , they retook the same personality scales in 1 of 3 randomly assigned experimental response conditions : honest , faking - good , or reproduce .

Example answer:
{"entities": [{"text": "personality scales", "type": "IntellectualProduct"}, {"text": "response conditions", "type": "BiologicFunction"}]}

Example input:
Sentence: Out of harm 's way : Secure versus insecure - disorganized attachment predicts less adolescent risk taking related to childhood poverty Although some risk taking in adolescence is normative , evidence suggests that adolescents raised in conditions of socioeconomic disadvantage are disproportionately burdened with risk taking and its negative consequences .

Example answer:
{"entities": [{"text": "Secure", "type": "Finding"}, {"text": "insecure - disorganized attachment", "type": "Finding"}, {"text": "predicts", "type": "Finding"}, {"text": "negative", "type": "Finding"}]}

Example input:
Sentence: Individual classification of strong risk attitudes : An application across lottery types and age groups Empirical evaluations of risk attitudes often rely on a weak definition of risk that concerns preferences towards risky and riskless options ( e . g .

Example answer:
{"entities": [{"text": "Individual", "type": "PopulationGroup"}, {"text": "classification", "type": "IntellectualProduct"}, {"text": "attitudes", "type": "BiologicFunction"}, {"text": "definition", "type": "IntellectualProduct"}]}

Example input:
Sentence: Faking behavior also introduced a uniform bias , implying that the classically observed mean raw score differences may not be readily interpreted .

Example answer:
{"entities": []}

Example input:
Sentence: Transgressive overyielding suggests that positive niche complementarity effects are driving some of the responses to intraspecific richness .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}]}

Example input:
Sentence: The varying latent retest correlations indicated that faking can distort respondents ' rank - order and thus the fairness of subsequent selection decisions , depending on the kind of faking behavior .

Example answer:
{"entities": [{"text": "retest correlations", "type": "ResearchActivity"}, {"text": "indicated", "type": "Finding"}, {"text": "respondents", "type": "PopulationGroup"}, {"text": "selection decisions", "type": "BiologicFunction"}]}

Example input:
Sentence: The present work argues that weak risk attitudes have limited generalizability and proposes the use of a strong definition of risk that is concerned with preferences towards options with the same expected value but different degrees of risk

Example answer:
{"entities": [{"text": "attitudes", "type": "BiologicFunction"}, {"text": "definition", "type": "IntellectualProduct"}]}

Example input:
Sentence: This result is of interest as mindfulness alone explained 23 % of the variance and unproductive Repeated Negative Thinking ( RNT ) and RNT consuming mental capacity predicted 8 % and 2 % respectively .

Example answer:
{"entities": [{"text": "mindfulness", "type": "BiologicFunction"}, {"text": "Repeated Negative Thinking", "type": "BiologicFunction"}, {"text": "RNT", "type": "BiologicFunction"}]}

Example input:
Sentence: Unrealistic comparative optimism : An unsuccessful search for evidence of a genuinely motivational bias One of the most accepted findings across psychology is that people are unrealistically optimistic in their judgments of comparative risk concerning future life events -they judge negative events as less likely to happen to themselves than to the average person . Harris and Hahn ( 2011 ) , however , demonstrated how unbiased ( non - optimistic ) responses can result in data patterns commonly interpreted as indicative of optimism due to statistical artifacts .

Example answer:
{"entities": [{"text": "optimism", "type": "BiologicFunction"}, {"text": "findings", "type": "Finding"}, {"text": "psychology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "people", "type": "PopulationGroup"}, {"text": "unrealistically optimistic", "type": "Finding"}, {"text": "judgments", "type": "BiologicFunction"}, {"text": "judge", "type": "BiologicFunction"}, {"text": "average person", "type": "PopulationGroup"}, {"text": "Harris", "type": "Eukaryote"}, {"text": "Hahn", "type": "Eukaryote"}]}

Example input:
Sentence: A reanalysis of previously - published data and the results from a new study show that only a minority of individuals manifests the reflection effect under a strong definition of risk , and that , when facing certain lottery - pair types , older adults appear to be more risk seeking than younger adults .

Example answer:
{"entities": [{"text": "reanalysis", "type": "ResearchActivity"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "definition", "type": "IntellectualProduct"}, {"text": "older adults", "type": "PopulationGroup"}]}

Input:
Sentence: A large body of work has shown that individuals tend to be weak risk averse in choice contexts involving risky and riskless gains but weak risk seeking in contexts involving losses , a phenomenon known as the reflection effect .

## Item MedMentions:test:2609
Example input:
Sentence: Compounds 3 , 5 , 6 , 8 , 9 , 10 , 14 and 16 showed inhibitory effects on the proliferation of human breast cancer cells MCF - 7 by 24 .

Example answer:
{"entities": [{"text": "Compounds", "type": "Chemical"}, {"text": "3", "type": "Chemical"}, {"text": "5", "type": "Chemical"}, {"text": "6", "type": "Chemical"}, {"text": "8", "type": "Chemical"}, {"text": "9", "type": "Chemical"}, {"text": "10", "type": "Chemical"}, {"text": "14", "type": "Chemical"}, {"text": "16", "type": "Chemical"}, {"text": "inhibitory effects on the proliferation", "type": "BiologicFunction"}, {"text": "human breast cancer cells", "type": "AnatomicalStructure"}, {"text": "MCF - 7", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Stimulation of cell proliferation by glutathione monoethyl ester in aged bone marrow stromal cells is associated with the assistance of TERT gene expression and telomerase activity The proliferation and differentiation potential of aged bone marrow stromal cells ( BMSCs ) are significantly reduced .

Example answer:
{"entities": [{"text": "cell proliferation", "type": "BiologicFunction"}, {"text": "glutathione monoethyl ester", "type": "Chemical"}, {"text": "aged bone marrow stromal cells", "type": "AnatomicalStructure"}, {"text": "TERT", "type": "AnatomicalStructure"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "telomerase activity", "type": "BiologicFunction"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "differentiation", "type": "BiologicFunction"}, {"text": "BMSCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Myeloid - derived suppressor cells , which were a copious cell subset in BMCs , enhanced the Ki67 expression of Treg cells .

Example answer:
{"entities": [{"text": "Myeloid - derived suppressor cells", "type": "AnatomicalStructure"}, {"text": "copious cell subset", "type": "AnatomicalStructure"}, {"text": "BMCs", "type": "AnatomicalStructure"}, {"text": "Ki67", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Treg cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The B1R + tumor - to - blood and B1R + tumor - to - muscle contrast ratios were also higher for ( 68 ) Ga - Z02176 ( 56 . 1 ± 17 .

Example answer:
{"entities": [{"text": "( 68 ) Ga", "type": "Chemical"}, {"text": "Z02176", "type": "Chemical"}]}

Example input:
Sentence: A prospective randomized , controlled , open - label pilot study was conducted on 50 Egyptian patients with BM who were randomly assigned to receive 30 - Gy WBRT ( control group : 25 patients ) or 30 Gy WBRT + simvastatin 80 mg / day for the WBRT period ( simvastatin group : 25 patients ) .

Example answer:
{"entities": [{"text": "prospective", "type": "ResearchActivity"}, {"text": "randomized", "type": "ResearchActivity"}, {"text": "controlled", "type": "ResearchActivity"}, {"text": "open - label pilot study", "type": "ResearchActivity"}, {"text": "Egyptian", "type": "PopulationGroup"}, {"text": "BM", "type": "BiologicFunction"}, {"text": "30 - Gy WBRT", "type": "HealthCareActivity"}, {"text": "30 Gy WBRT", "type": "HealthCareActivity"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "WBRT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Uptake in B1R + tumor was higher by using ( 68 ) Ga - Z02176 ( 28 . 9 ± 6 .

Example answer:
{"entities": [{"text": "Uptake", "type": "BiologicFunction"}, {"text": "B1R +", "type": "Chemical"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "( 68 ) Ga", "type": "Chemical"}, {"text": "Z02176", "type": "Chemical"}]}

Example input:
Sentence: The viability and proliferation of hABMSCs were higher after treating with 5 - 20 % B - CSM to the cells , compared to 40 - 60 % .

Example answer:
{"entities": [{"text": "viability", "type": "BiologicFunction"}, {"text": "proliferation", "type": "BiologicFunction"}, {"text": "hABMSCs", "type": "AnatomicalStructure"}, {"text": "B - CSM", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Compound 7b was found to markedly inhibit BTK activity at concentrations of 0 .

Example answer:
{"entities": [{"text": "Compound 7b", "type": "Chemical"}, {"text": "BTK", "type": "Chemical"}, {"text": "activity", "type": "BiologicFunction"}]}

Example input:
Sentence: Design and synthesis of phosphoryl - substituted diphenylpyrimidines ( Pho - DPPYs ) as potent Bruton 's tyrosine kinase ( BTK ) inhibitors : Targeted treatment of B lymphoblastic leukemia cell lines A family of phosphoryl - substituted diphenylpyrimidine derivatives ( Pho - DPPYs ) were synthesized and biologically evaluated as potent BTK inhibitors in this study .

Example answer:
{"entities": [{"text": "phosphoryl - substituted diphenylpyrimidines", "type": "Chemical"}, {"text": "Pho - DPPYs", "type": "Chemical"}, {"text": "Bruton 's tyrosine kinase ( BTK ) inhibitors", "type": "Chemical"}, {"text": "Targeted treatment", "type": "HealthCareActivity"}, {"text": "B lymphoblastic leukemia", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "phosphoryl - substituted diphenylpyrimidine derivatives ( Pho - DPPYs )", "type": "Chemical"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "BTK inhibitors", "type": "Chemical"}]}

Example input:
Sentence: In a word , compound 7b is a promising BTK inhibitor for the treatment of B - cell lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "compound 7b", "type": "Chemical"}, {"text": "BTK inhibitor", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "B - cell lymphoblastic leukemia", "type": "BiologicFunction"}]}

Input:
Sentence: 82nmol / L , as well as to suppress the proliferations of B - cell leukemia cell lines ( Ramos and Raji ) expressing high levels of BTK at concentrations of 3 . 17μM and 6 .

## Item MedMentions:test:2814
Example input:
Sentence: Phylogenetic analyses based on 16S rRNA gene sequences indicated that strain SYP - A7299 T belongs to the genus Arthrobacter and is most closely related to Arthrobacter halodurans JSM 078085 T ( 97 . 4 % 16S rRNA gene sequence similarity ) .

Example answer:
{"entities": [{"text": "Phylogenetic analyses", "type": "ResearchActivity"}, {"text": "16S rRNA gene sequences", "type": "AnatomicalStructure"}, {"text": "strain SYP - A7299 T", "type": "Bacterium"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Arthrobacter", "type": "Bacterium"}, {"text": "Arthrobacter halodurans JSM 078085 T", "type": "Bacterium"}, {"text": "16S rRNA gene sequence", "type": "AnatomicalStructure"}]}

Example input:
Sentence: coli HGT ( high glucose throughput ) strain was engineered by modulating the stringent response regulation program and decreasing the activity of pyruvate dehydrogenase .

Example answer:
{"entities": [{"text": "coli HGT", "type": "Bacterium"}, {"text": "high glucose", "type": "Finding"}, {"text": "throughput", "type": "BiologicFunction"}, {"text": "engineered", "type": "ResearchActivity"}, {"text": "stringent response", "type": "BiologicFunction"}, {"text": "regulation program", "type": "BiologicFunction"}, {"text": "decreasing", "type": "Finding"}, {"text": "pyruvate dehydrogenase", "type": "Chemical"}]}

Example input:
Sentence: Fluoranthene degradation and binding mechanism study based on the active - site structure of ring - hydroxylating dioxygenase in Microbacterium paraoxydans JPM1 In this study , a gram - positive fluoranthene - degrading bacterial strain was isolated from crude oil in Dagang Oilfield and identified as Microbacterium paraoxydans JPM1 by the analysis of 16S rDNA sequence .

Example answer:
{"entities": [{"text": "Fluoranthene", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "structure", "type": "SpatialConcept"}, {"text": "ring - hydroxylating dioxygenase", "type": "Chemical"}, {"text": "Microbacterium paraoxydans JPM1", "type": "Bacterium"}, {"text": "gram - positive fluoranthene - degrading bacterial", "type": "Bacterium"}, {"text": "crude oil", "type": "Chemical"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "16S rDNA", "type": "Chemical"}, {"text": "sequence", "type": "SpatialConcept"}]}

Example input:
Sentence: On the contrary , the butyrogenic gut pathogen Fusobacterium utilizes different amino acid metabolism pathways like those for Glutamate ( 4 - aminobutyrate and Glutarate ) and Lysine for butyrogenesis which leads to a concomitant release of harmful by - products like ammonia in the process .

Example answer:
{"entities": [{"text": "Fusobacterium", "type": "Bacterium"}, {"text": "amino acid metabolism pathways", "type": "BiologicFunction"}, {"text": "Glutamate", "type": "Chemical"}, {"text": "4 - aminobutyrate", "type": "Chemical"}, {"text": "Glutarate", "type": "Chemical"}, {"text": "Lysine", "type": "Chemical"}, {"text": "butyrogenesis", "type": "BiologicFunction"}, {"text": "ammonia", "type": "Chemical"}]}

Example input:
Sentence: The Crystal Structure of the C - Terminal Domain of the Salmonella enterica PduO Protein : An Old Fold with a New Heme - Binding Mode The two - domain protein PduO , involved in 1 , 2 - propanediol utilization in the pathogenic Gram - negative bacterium Salmonella enterica is an ATP : Cob ( I ) alamin adenosyltransferase , but this is a function of the N - terminal domain alone .

Example answer:
{"entities": [{"text": "Crystal Structure", "type": "Chemical"}, {"text": "C - Terminal Domain", "type": "SpatialConcept"}, {"text": "Salmonella enterica", "type": "Bacterium"}, {"text": "PduO Protein", "type": "Chemical"}, {"text": "Heme - Binding", "type": "BiologicFunction"}, {"text": "two - domain protein PduO", "type": "Chemical"}, {"text": "1 , 2 - propanediol", "type": "Chemical"}, {"text": "Gram - negative bacterium", "type": "Bacterium"}, {"text": "ATP", "type": "Chemical"}, {"text": "Cob ( I ) alamin adenosyltransferase", "type": "Chemical"}, {"text": "function", "type": "BiologicFunction"}, {"text": "N - terminal domain", "type": "SpatialConcept"}]}

Example input:
Sentence: In addition , we present a corrected structure of WbpE , a related sugar aminotransferase from Pseudomonas aeruginosa , solved to 1 .

Example answer:
{"entities": [{"text": "structure", "type": "SpatialConcept"}, {"text": "WbpE", "type": "Chemical"}, {"text": "sugar", "type": "Chemical"}, {"text": "aminotransferase", "type": "Chemical"}, {"text": "Pseudomonas aeruginosa", "type": "Bacterium"}]}

Example input:
Sentence: jejuni , which plays a key role in the production of these unusual sugars by functioning as a pyridoxal 5 ' - phosphate dependent aminotransferase .

Example answer:
{"entities": [{"text": "jejuni", "type": "Bacterium"}, {"text": "sugars", "type": "Chemical"}, {"text": "pyridoxal 5 ' - phosphate", "type": "Chemical"}, {"text": "aminotransferase", "type": "Chemical"}]}

Example input:
Sentence: An Improved Culture Method for Selective Isolation of Campylobacter jejuni from Wastewater Campylobacter jejuni is one of the leading foodborne pathogens worldwide .

Example answer:
{"entities": [{"text": "Culture Method", "type": "HealthCareActivity"}, {"text": "Isolation", "type": "HealthCareActivity"}, {"text": "Campylobacter jejuni", "type": "Bacterium"}]}

Example input:
Sentence: jejuni 81116 ( Penner serotype HS : 6 ) lipoglycan contains two dideoxyhexosamine residues , and enzymological assay data show that this bacterial strain can synthesize both dTDP - 3 - acetamido - 3 , 6 - dideoxy - d - glucose and dTDP - 3 - acetamido - 3 , 6 - dideoxy - d - galactose .

Example answer:
{"entities": [{"text": "jejuni 81116", "type": "IntellectualProduct"}, {"text": "Penner serotype HS : 6", "type": "IntellectualProduct"}, {"text": "lipoglycan", "type": "Chemical"}, {"text": "dideoxyhexosamine", "type": "Chemical"}, {"text": "enzymological assay", "type": "HealthCareActivity"}, {"text": "bacterial strain", "type": "Bacterium"}, {"text": "dTDP - 3 - acetamido - 3 , 6 - dideoxy - d - glucose", "type": "Chemical"}, {"text": "dTDP - 3 - acetamido - 3 , 6 - dideoxy - d - galactose", "type": "Chemical"}]}

Example input:
Sentence: Of particular significance are the external aldimine structures of WlaRG solved in the presence of either dTDP - 3 - amino - 3 , 6 - dideoxy - d - galactose or dTDP - 3 - amino - 3 , 6 - dideoxy - d - glucose .

Example answer:
{"entities": [{"text": "aldimine", "type": "Chemical"}, {"text": "structures", "type": "SpatialConcept"}, {"text": "WlaRG", "type": "Chemical"}, {"text": "dTDP - 3 - amino - 3 , 6 - dideoxy - d - galactose", "type": "Chemical"}, {"text": "dTDP - 3 - amino - 3 , 6 - dideoxy - d - glucose", "type": "Chemical"}]}

Input:
Sentence: Structural investigation on WlaRG from Campylobacter jejuni : A sugar aminotransferase Campylobacter jejuni is a Gram - negative bacterium that represents a leading cause of human gastroenteritis worldwide .

## Item MedMentions:test:3046
Example input:
Sentence: From 2003 - 2013 , 39 ( 0 . 1 % , 39 / 32 , 824 ) NTPn were reported .

Example answer:
{"entities": [{"text": "NTPn", "type": "Bacterium"}]}

Example input:
Sentence: Registered on 27 February 2016 .

Example answer:
{"entities": []}

Example input:
Sentence: DRKS00010231 ( retrospectively registered on 24 March 2016 ; first version ) .

Example answer:
{"entities": []}

Example input:
Sentence: An NLR ≥3 .

Example answer:
{"entities": []}

Example input:
Sentence: ISRCTN12389808 , 18th November 2016 , retrospectively registered .

Example answer:
{"entities": []}

Example input:
Sentence: nl between 2006 - 2015 were analysed .

Example answer:
{"entities": [{"text": "nl", "type": "IntellectualProduct"}, {"text": "analysed", "type": "ResearchActivity"}]}

Example input:
Sentence: ClinicalTrials . gov , registered on March 12 , 2014 , identifier : NCT02087592 . World Health Organization Trial Registration , registered on 3 August 2015 , identifier : NCT02087592 .

Example answer:
{"entities": [{"text": "World Health Organization", "type": "Organization"}]}

Example input:
Sentence: NCT # 01234883 ( Registration Date : November 3 , 2010 ) .

Example answer:
{"entities": []}

Example input:
Sentence: NTR5568 .

Example answer:
{"entities": []}

Example input:
Sentence: This study was registered at the Netherlands Trial Register [ NTR2153 ] on the 5 ( th ) of January 2010 .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "registered", "type": "IntellectualProduct"}, {"text": "Netherlands Trial Register", "type": "IntellectualProduct"}, {"text": "NTR2153", "type": "IntellectualProduct"}]}

Input:
Sentence: nl ( NTR registration number : 5586 ) on 15 January 2016 .
