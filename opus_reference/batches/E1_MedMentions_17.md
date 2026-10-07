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

## Item MedMentions:test:3308
Example input:
Sentence: A venous ( adults ) or capillary ( children ) sample was taken for immediate HbA1c analysis .

Example answer:
{"entities": [{"text": "venous", "type": "BodySubstance"}, {"text": "capillary ( children ) sample", "type": "BodySubstance"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: These specimens were obtained from 18 participants with no evidence of breast disease ( ND ) , 92 participants diagnosed with Benign Breast Disease ( BBD ) and 100 participants diagnosed with BC , including DCIS .

Example answer:
{"entities": [{"text": "participants", "type": "PopulationGroup"}, {"text": "no evidence of breast disease", "type": "Finding"}, {"text": "ND", "type": "Finding"}, {"text": "diagnosed", "type": "Finding"}, {"text": "Benign Breast Disease", "type": "BiologicFunction"}, {"text": "BBD", "type": "BiologicFunction"}, {"text": "BC", "type": "BiologicFunction"}, {"text": "DCIS", "type": "BiologicFunction"}]}

Example input:
Sentence: All serum samples ( n = 210 ) were collected prior to biopsy .

Example answer:
{"entities": [{"text": "serum samples", "type": "BodySubstance"}, {"text": "biopsy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Blood samples are also collected in the ED using PAXgene DNA and PAXgene RNA tubes .

Example answer:
{"entities": [{"text": "Blood samples", "type": "BodySubstance"}, {"text": "ED", "type": "Organization"}]}

Example input:
Sentence: 28 ( 52 % ) patients were analyzed for both tissue samples and CTCs .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "tissue samples", "type": "AnatomicalStructure"}, {"text": "CTCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The analysis was carried out by real - time quantitative PCR on 104 patients and 110 healthy volunteers .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "real - time quantitative PCR", "type": "ResearchActivity"}, {"text": "healthy volunteers", "type": "PopulationGroup"}]}

Example input:
Sentence: These men underwent a health examination including blood sampling in 2010 and a subset of 324 also had a quantitative PCR - based measurement of TL .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}, {"text": "health examination", "type": "HealthCareActivity"}, {"text": "blood sampling", "type": "HealthCareActivity"}, {"text": "quantitative PCR - based measurement", "type": "HealthCareActivity"}, {"text": "TL", "type": "BiologicFunction"}]}

Example input:
Sentence: Blood samples were taken from 1025 women at presentation for thyroid stimulating hormone ( TSH ) , anti - thyroglobulin antibodies ( TGAb ) , and thyroid peroxidase antibodies ( TPOAb ) .

Example answer:
{"entities": [{"text": "Blood samples", "type": "BodySubstance"}, {"text": "women", "type": "PopulationGroup"}, {"text": "thyroid stimulating hormone", "type": "Chemical"}, {"text": "TSH", "type": "Chemical"}, {"text": "anti - thyroglobulin antibodies", "type": "Chemical"}, {"text": "TGAb", "type": "Chemical"}, {"text": "thyroid peroxidase antibodies", "type": "Chemical"}, {"text": "TPOAb", "type": "Chemical"}]}

Example input:
Sentence: PBMCs were isolated from whole blood of 40 AS patients and 40 healthy individuals .

Example answer:
{"entities": [{"text": "PBMCs", "type": "AnatomicalStructure"}, {"text": "whole blood", "type": "BodySubstance"}, {"text": "AS", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: Blood samples and colorectal biopsies were collected from patients with PSC - UC , patients with UC and healthy controls .

Example answer:
{"entities": [{"text": "Blood samples", "type": "BodySubstance"}, {"text": "colorectal", "type": "SpatialConcept"}, {"text": "biopsies", "type": "HealthCareActivity"}, {"text": "PSC", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}]}

Input:
Sentence: Blood samples were collected from 10 healthy individuals and 22 patients with different types of cancer .

## Item MedMentions:test:3012
Example input:
Sentence: These results strongly suggest that excessive activation of the NLRP3 inflammasome and downstream PGE2 signaling contribute to the pathogenesis of TMEV - induced demyelinating disease .

Example answer:
{"entities": [{"text": "activation", "type": "BiologicFunction"}, {"text": "NLRP3 inflammasome", "type": "AnatomicalStructure"}, {"text": "downstream", "type": "SpatialConcept"}, {"text": "PGE2", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "TMEV", "type": "Virus"}, {"text": "demyelinating disease", "type": "BiologicFunction"}]}

Example input:
Sentence: Inhibition of virus - induced PGE2 signaling using AH23848 resulted in decreased pathogenesis of demyelinating disease and viral loads in the central nervous system ( CNS ) .

Example answer:
{"entities": [{"text": "virus", "type": "Virus"}, {"text": "PGE2", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "AH23848", "type": "Chemical"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "demyelinating disease", "type": "BiologicFunction"}, {"text": "viral loads", "type": "Finding"}, {"text": "central nervous system", "type": "BodySystem"}, {"text": "CNS", "type": "BodySystem"}]}

Example input:
Sentence: We also propose a novel antiviral immunomodulatory pathway controlled by interferon - β ( IFN - β ) and mediated by immune - responsive gene 1 ( IRG1 ) and itaconic acid , its product .

Example answer:
{"entities": [{"text": "antiviral", "type": "BiologicFunction"}, {"text": "immunomodulatory", "type": "Chemical"}, {"text": "interferon - β", "type": "Chemical"}, {"text": "IFN - β", "type": "Chemical"}, {"text": "immune - responsive gene 1", "type": "Chemical"}, {"text": "IRG1", "type": "Chemical"}, {"text": "itaconic acid", "type": "Chemical"}]}

Example input:
Sentence: We demonstrate here that TMEV infection activates the NLRP3 inflammasome and PGE2 signaling much more vigorously in dendritic cells ( DCs ) and CD11b + cells from susceptible SJL mice than in cells from resistant B6 mice .

Example answer:
{"entities": [{"text": "TMEV", "type": "Virus"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "activates", "type": "BiologicFunction"}, {"text": "NLRP3 inflammasome", "type": "AnatomicalStructure"}, {"text": "PGE2", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "dendritic cells", "type": "AnatomicalStructure"}, {"text": "DCs", "type": "AnatomicalStructure"}, {"text": "CD11b + cells", "type": "AnatomicalStructure"}, {"text": "SJL mice", "type": "Eukaryote"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "B6 mice", "type": "Eukaryote"}]}

Example input:
Sentence: The meta cleavage product hydrolase , HsaD , has been demonstrated to be critical for the survival of Mycobacterium tuberculosis in macrophages and is encoded in an operon involved in cholesterol catabolism , which is identical in M .

Example answer:
{"entities": [{"text": "meta cleavage product hydrolase", "type": "Chemical"}, {"text": "HsaD", "type": "Chemical"}, {"text": "Mycobacterium tuberculosis", "type": "Bacterium"}, {"text": "macrophages", "type": "AnatomicalStructure"}, {"text": "operon", "type": "AnatomicalStructure"}, {"text": "cholesterol catabolism", "type": "BiologicFunction"}, {"text": "M .", "type": "Bacterium"}]}

Example input:
Sentence: It could be concluded that the effect mechanism is mainly composed of histidine metabolism , arachidonic acid metabolism , energy metabolism , purine metabolism and other small molecules through 30 metabolites .

Example answer:
{"entities": [{"text": "histidine metabolism", "type": "BiologicFunction"}, {"text": "arachidonic acid metabolism", "type": "BiologicFunction"}, {"text": "energy metabolism", "type": "BiologicFunction"}, {"text": "metabolites", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated the levels of intermediate molecules leading to PGE2 signaling and the effects of blocking PGE2 signaling on the immune response to TMEV infection , viral persistence and the development of demyelinating disease .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "intermediate", "type": "SpatialConcept"}, {"text": "PGE2", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "immune response", "type": "BiologicFunction"}, {"text": "TMEV", "type": "Virus"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "viral", "type": "Virus"}, {"text": "persistence", "type": "Finding"}, {"text": "demyelinating disease", "type": "BiologicFunction"}]}

Example input:
Sentence: MITA overexpression stimulated IRF3 - IFN pathway ; while MRP overexpression activated NF - κB pathway , suggesting these two isoform s may inhibit HBV replication through different ways .

Example answer:
{"entities": [{"text": "MITA", "type": "Chemical"}, {"text": "overexpression", "type": "BiologicFunction"}, {"text": "IRF3", "type": "Chemical"}, {"text": "IFN", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "MRP", "type": "Chemical"}, {"text": "NF - κB pathway", "type": "BiologicFunction"}, {"text": "isoform", "type": "Chemical"}, {"text": "HBV", "type": "Virus"}, {"text": "replication", "type": "BiologicFunction"}]}

Example input:
Sentence: The study of APMV and human cells interaction revealed that the virus is able to evade the IFN system by inhibiting the regulation of interferon -stimulated genes , suggesting that the virus and humans have had host - pathogen interactions .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "APMV", "type": "Virus"}, {"text": "human", "type": "Eukaryote"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "interaction", "type": "BiologicFunction"}, {"text": "virus", "type": "Virus"}, {"text": "evade", "type": "BiologicFunction"}, {"text": "IFN", "type": "Chemical"}, {"text": "system", "type": "BodySystem"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "interferon", "type": "Chemical"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "humans", "type": "Eukaryote"}, {"text": "host - pathogen interactions", "type": "BiologicFunction"}]}

Example input:
Sentence: Thus , lipid metabolism modulators are good candidates to regulate virus assembly and HCV replication .

Example answer:
{"entities": [{"text": "lipid metabolism", "type": "BiologicFunction"}, {"text": "modulators", "type": "Chemical"}, {"text": "virus assembly", "type": "BiologicFunction"}, {"text": "HCV", "type": "Virus"}, {"text": "replication", "type": "BiologicFunction"}]}

Input:
Sentence: This metabolite links metabolism to antiviral activity by inactivating the virus , in a novel immunomodulatory pathway relevant for APMV infections and probably to other infectious diseases as well .

## Item MedMentions:test:3054
Example input:
Sentence: CF induced HepG2 cell death in a time - and dose - dependent manner with half maximal inhibitory concentration values of 219 .

Example answer:
{"entities": [{"text": "CF", "type": "Eukaryote"}, {"text": "HepG2", "type": "AnatomicalStructure"}, {"text": "cell death", "type": "BiologicFunction"}]}

Example input:
Sentence: In particular , C9orf72 depletion leads to reduced activity of MTOR , a negative regulator of macroautophagy / autophagy , and concomitantly increased TFEB levels and nuclear translocation .

Example answer:
{"entities": [{"text": "C9orf72", "type": "AnatomicalStructure"}, {"text": "MTOR", "type": "Chemical"}, {"text": "macroautophagy", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "TFEB", "type": "Chemical"}, {"text": "nuclear translocation", "type": "BiologicFunction"}]}

Example input:
Sentence: The results showed that the production of reactive oxygen species increased in a concentration -dependent manner after exposure to PFOS for 96 h .

Example answer:
{"entities": [{"text": "reactive oxygen species", "type": "Chemical"}, {"text": "PFOS", "type": "Chemical"}]}

Example input:
Sentence: Accordingly , the apparent fenretinide -induced - apoptosis was linked to the rapid generation of reactive oxygen species ( ROS ) .

Example answer:
{"entities": [{"text": "fenretinide", "type": "Chemical"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: All major genotoxic responses to FA , including replication inhibition and activation of the transcription factor p53 and the apical ATM and ATR kinases , were unaffected by immunoproteasome inactivity .

Example answer:
{"entities": [{"text": "FA", "type": "Chemical"}, {"text": "replication inhibition", "type": "BiologicFunction"}, {"text": "transcription factor p53", "type": "Chemical"}, {"text": "apical", "type": "SpatialConcept"}, {"text": "ATM", "type": "Chemical"}, {"text": "ATR kinases", "type": "Chemical"}, {"text": "immunoproteasome", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , the present study demonstrated that CF induced ROS formation , increased caspase 3 activities , decreased the ΔΨm , and caused HepG2 apoptosis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "CF", "type": "Eukaryote"}, {"text": "ROS formation", "type": "BiologicFunction"}, {"text": "caspase 3 activities", "type": "BiologicFunction"}, {"text": "ΔΨm", "type": "BiologicFunction"}, {"text": "HepG2", "type": "AnatomicalStructure"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Hematopoiesis - specific Fh1 deletion ( resulting in endogenous fumarate accumulation and a genetic TCA cycle block reflected by decreased maximal mitochondrial respiration ) caused lethal fetal liver hematopoietic defects and hematopoietic stem cell ( HSC ) failure .

Example answer:
{"entities": [{"text": "Hematopoiesis", "type": "BiologicFunction"}, {"text": "Fh1", "type": "AnatomicalStructure"}, {"text": "deletion", "type": "BiologicFunction"}, {"text": "fumarate", "type": "Chemical"}, {"text": "TCA cycle", "type": "BiologicFunction"}, {"text": "mitochondrial", "type": "AnatomicalStructure"}, {"text": "respiration", "type": "BiologicFunction"}, {"text": "lethal fetal liver", "type": "AnatomicalStructure"}, {"text": "hematopoietic defects", "type": "AnatomicalStructure"}, {"text": "hematopoietic stem cell", "type": "AnatomicalStructure"}, {"text": "HSC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Micronucleus test was applied to investigate genotoxic potential of fluoride .

Example answer:
{"entities": [{"text": "Micronucleus test", "type": "HealthCareActivity"}, {"text": "fluoride", "type": "Chemical"}]}

Example input:
Sentence: Our results revealed the genotoxic potential of fluoride but did not confirm mitochondrial swelling nor an increase of positive TUNEL labelling induced by fluoride , indicating absence of apoptosis .

Example answer:
{"entities": [{"text": "fluoride", "type": "Chemical"}, {"text": "mitochondrial swelling", "type": "BiologicFunction"}, {"text": "positive", "type": "Finding"}, {"text": "TUNEL labelling", "type": "ResearchActivity"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Currently , studies have reported a probable link to oxidative stress , DNA damage and apoptosis induced by fluoride in rat hepatocytes .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "reported", "type": "IntellectualProduct"}, {"text": "probable link", "type": "Finding"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "DNA damage", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "fluoride", "type": "Chemical"}, {"text": "rat", "type": "Eukaryote"}, {"text": "hepatocytes", "type": "AnatomicalStructure"}]}

Input:
Sentence: Genotoxic effect and rat hepatocyte death occurred after oxidative stress induction and antioxidant gene downregulation caused by long term fluoride exposure Studies focusing on possible genotoxic effects of excess fluoride are contradictory and inconclusive .

## Item MedMentions:test:3370
Example input:
Sentence: Established measures of SNR gain are derived from areas of uniform uptake , which is not applicable to the heterogeneous uptake in cardiac PET images using fluoro - deoxyglucose ( FDG ) .

Example answer:
{"entities": [{"text": "cardiac", "type": "AnatomicalStructure"}, {"text": "PET", "type": "HealthCareActivity"}, {"text": "images", "type": "IntellectualProduct"}, {"text": "fluoro - deoxyglucose", "type": "Chemical"}, {"text": "FDG", "type": "Chemical"}]}

Example input:
Sentence: After reclassifying NIFTP , the positive predictive value of GEC decreased from 42 % ( 95 % confidence interval [ 95 % CI ] , 39 % - 45 % ) to 24 % ( 95 % CI , 22 % - 26 % ) in the AUS group and from 23 % ( 95 % CI , 19 % - 27 % ) to 13 % ( 95 % CI , 9 % - 18 % ) in the SFN group .

Example answer:
{"entities": [{"text": "reclassifying", "type": "IntellectualProduct"}, {"text": "NIFTP", "type": "BiologicFunction"}, {"text": "GEC", "type": "ResearchActivity"}, {"text": "AUS", "type": "Finding"}, {"text": "SFN", "type": "BiologicFunction"}]}

Example input:
Sentence: Further , a study is carried out to count nuclei manually and automatically from the proposed algorithm with an average error rate of 6 . 84 % which is significant .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "nuclei", "type": "AnatomicalStructure"}, {"text": "manually", "type": "HealthCareActivity"}, {"text": "automatically", "type": "HealthCareActivity"}, {"text": "algorithm", "type": "IntellectualProduct"}]}

Example input:
Sentence: Lowering the diagnostic threshold to any follicular cells yielded a sensitivity of 92 % , a specificity of 60 % , a positive predictive value of 59 % , a negative predictive value of 92 % , and a false - negative rate of 7 . 7 % , whereas the values for the initially diagnostic cases were 93 % , 58 % , 59 % , 93 % , and 7 . 7 % , respectively .

Example answer:
{"entities": [{"text": "follicular", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "false - negative", "type": "Finding"}]}

Example input:
Sentence: The blue channel of the first stage output is given as input to k - means algorithm , which provides separate cluster for Ki - 67 positive and negative cells .

Example answer:
{"entities": [{"text": "first stage", "type": "IntellectualProduct"}, {"text": "k - means algorithm", "type": "ResearchActivity"}, {"text": "Ki - 67", "type": "Chemical"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: F - measure and performance analysis on the enolase search results and comparison to GEMMA and SCI - PHY demonstrate that TuLIP avoids the over - division problem of these methods .

Example answer:
{"entities": [{"text": "performance analysis", "type": "ResearchActivity"}, {"text": "enolase", "type": "Chemical"}, {"text": "GEMMA", "type": "IntellectualProduct"}, {"text": "SCI - PHY", "type": "IntellectualProduct"}, {"text": "TuLIP", "type": "IntellectualProduct"}]}

Example input:
Sentence: Characteristic nuclei were circumscribed , and parameters discriminating groups included nuclear circumference ( μm ) , area ( μm ( 2 ) ) , and 15 positive pixel count ( PPC ) algorithm IA measurements .

Example answer:
{"entities": [{"text": "nuclear", "type": "SpatialConcept"}, {"text": "area", "type": "SpatialConcept"}, {"text": "positive pixel count ( PPC ) algorithm IA", "type": "HealthCareActivity"}]}

Example input:
Sentence: The F - measure for L * a * b * colour space ( 0 . 8847 ) provides the best statistical result as compared to grey , HSI , YCbCr , YIQ and XYZ colour space .

Example answer:
{"entities": [{"text": "colour space", "type": "IntellectualProduct"}]}

Example input:
Sentence: The study provides an automated count of positive and negative nuclei using L * a * b * colour space and hybrid segmentation technique .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "nuclei", "type": "AnatomicalStructure"}, {"text": "colour space", "type": "IntellectualProduct"}]}

Example input:
Sentence: The positive and negative nuclei detection results for all colour space s are compared with the ground truth for validation and F - measure is calculated .

Example answer:
{"entities": [{"text": "nuclei", "type": "AnatomicalStructure"}, {"text": "detection", "type": "Finding"}, {"text": "colour space", "type": "IntellectualProduct"}, {"text": "calculated", "type": "HealthCareActivity"}]}

Input:
Sentence: The count of positive and negative nuclei is used to calculate the F - measure for each colour space .

## Item MedMentions:test:3194
Example input:
Sentence: Safety and immunogenecity of a live attenuated Rift Valley fever vaccine ( CL13 T ) in camels Rift Valley fever is an emerging zoonotic viral disease , enzootic and endemic in Africa and the Arabian Peninsula , which poses a significant threat to both human and animal health .

Example answer:
{"entities": [{"text": "immunogenecity", "type": "ResearchActivity"}, {"text": "attenuated", "type": "Chemical"}, {"text": "Rift Valley fever vaccine", "type": "Chemical"}, {"text": "CL13 T", "type": "Chemical"}, {"text": "camels", "type": "Eukaryote"}, {"text": "Rift Valley fever", "type": "BiologicFunction"}, {"text": "viral disease", "type": "BiologicFunction"}, {"text": "enzootic", "type": "BiologicFunction"}, {"text": "endemic", "type": "BiologicFunction"}, {"text": "Africa", "type": "SpatialConcept"}, {"text": "Arabian Peninsula", "type": "SpatialConcept"}, {"text": "human", "type": "Eukaryote"}, {"text": "animal", "type": "Eukaryote"}]}

Example input:
Sentence: 4 % , 15 % , and 0 . 8 % of wild boars , sika deer , and raccoons , respectively .

Example answer:
{"entities": [{"text": "wild boars", "type": "Eukaryote"}, {"text": "sika deer", "type": "Eukaryote"}, {"text": "raccoons", "type": "Eukaryote"}]}

Example input:
Sentence: The adder ( Vipera berus ) in Southern Altay Mountains : population characteristics , distribution , morphology and phylogenetic position As the most widely distributed snake in Eurasia , the adder ( Vipera berus ) has been extensively investigated in Europe but poorly understood in Asia .

Example answer:
{"entities": [{"text": "adder", "type": "Eukaryote"}, {"text": "Vipera berus", "type": "Eukaryote"}, {"text": "Southern Altay Mountains", "type": "SpatialConcept"}, {"text": "distribution", "type": "SpatialConcept"}, {"text": "distributed", "type": "SpatialConcept"}, {"text": "snake", "type": "Eukaryote"}, {"text": "Eurasia", "type": "SpatialConcept"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "Asia", "type": "SpatialConcept"}]}

Example input:
Sentence: Bird richness , diversity , and abundance were measured within a 25 - m radius of each of the 120 sampling points in various stages of succession and urban areas from May to April ( 2014 ) in the Ziarat catchment .

Example answer:
{"entities": [{"text": "Bird", "type": "Eukaryote"}, {"text": "within", "type": "SpatialConcept"}, {"text": "Ziarat", "type": "SpatialConcept"}, {"text": "catchment", "type": "SpatialConcept"}]}

Example input:
Sentence: Here we applied 3D dental surface texture analysis to a sample of field voles ( Microtus agrestis ) trapped from Finnish Lapland at different seasons and localities to test for inter - population variations .

Example answer:
{"entities": [{"text": "3D", "type": "SpatialConcept"}, {"text": "dental", "type": "AnatomicalStructure"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "field voles", "type": "Eukaryote"}, {"text": "Microtus agrestis", "type": "Eukaryote"}, {"text": "Finnish Lapland", "type": "SpatialConcept"}, {"text": "localities", "type": "SpatialConcept"}, {"text": "inter - population", "type": "PopulationGroup"}]}

Example input:
Sentence: Wild food plants and fungi used in the mycophilous Tibetan community of Zhagana ( Tewo County , Gansu , China ) The aim of the study was to investigate knowledge and use of wild food plants and fungi in a highland valley in the Gannan Tibetan Autonomous Region on the north - eastern edges of the Tibetan Plateau .

Example answer:
{"entities": [{"text": "Wild food plants", "type": "Food"}, {"text": "fungi", "type": "Eukaryote"}, {"text": "mycophilous", "type": "Food"}, {"text": "Tibetan", "type": "SpatialConcept"}, {"text": "Zhagana", "type": "SpatialConcept"}, {"text": "Tewo County", "type": "SpatialConcept"}, {"text": "Gansu", "type": "SpatialConcept"}, {"text": "China", "type": "SpatialConcept"}, {"text": "study", "type": "ResearchActivity"}, {"text": "knowledge", "type": "IntellectualProduct"}, {"text": "wild food plants", "type": "Food"}, {"text": "valley", "type": "SpatialConcept"}, {"text": "Gannan Tibetan Autonomous Region", "type": "SpatialConcept"}, {"text": "Tibetan Plateau", "type": "SpatialConcept"}]}

Example input:
Sentence: Four species of rodents including Mus musculus ( 52 . 75 % ) , Rattus norvegicus ( 38 . 46 % ) , Rhombomys opimus ( 4 . 40 % ) and Meriones libycus ( 4 . 40 % ) were captured .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "rodents", "type": "Eukaryote"}, {"text": "Mus musculus", "type": "Eukaryote"}, {"text": "Rattus norvegicus", "type": "Eukaryote"}, {"text": "Rhombomys opimus", "type": "Eukaryote"}, {"text": "Meriones libycus", "type": "Eukaryote"}]}

Example input:
Sentence: In addition , we examined whole blood samples from 190 wild boars and 276 sika deer , as well as sera from 120 wild raccoons .

Example answer:
{"entities": [{"text": "blood samples", "type": "BodySubstance"}, {"text": "wild boars", "type": "Eukaryote"}, {"text": "sika deer", "type": "Eukaryote"}, {"text": "sera", "type": "BodySubstance"}, {"text": "wild raccoons", "type": "Eukaryote"}]}

Example input:
Sentence: A total of 6 female -1 - year -old healthy Kazakh sheep were used for the experiments .

Example answer:
{"entities": [{"text": "Kazakh sheep", "type": "Eukaryote"}, {"text": "experiments", "type": "ResearchActivity"}]}

Example input:
Sentence: Zoonotic and Non - zoonotic Parasites of Wild Rodents in Turkman Sahra , Northeastern Iran This study was conducted to collect informative data on the parasitic infection of wild rodents , emphasizing on finding parasites , which have medical importance to human .

Example answer:
{"entities": [{"text": "Non - zoonotic", "type": "Finding"}, {"text": "Parasites", "type": "Eukaryote"}, {"text": "Wild", "type": "IntellectualProduct"}, {"text": "Rodents", "type": "Eukaryote"}, {"text": "Turkman Sahra , Northeastern Iran", "type": "SpatialConcept"}, {"text": "study", "type": "ResearchActivity"}, {"text": "collect informative data", "type": "ResearchActivity"}, {"text": "parasitic infection", "type": "BiologicFunction"}, {"text": "wild", "type": "IntellectualProduct"}, {"text": "rodents", "type": "Eukaryote"}, {"text": "finding", "type": "Finding"}, {"text": "parasites", "type": "Eukaryote"}, {"text": "human", "type": "Eukaryote"}]}

Input:
Sentence: During 2012 - 2014 , a total number of 91 wild rodents were captured from rural areas of Turkmen Sahra , Golestan Province , using handmade traps .

## Item MedMentions:test:3132
Example input:
Sentence: T1 and T2 Mapping in Recognition of Early Cardiac Involvement in Systemic Sarcoidosis Purpose To determine whether quantitative tissue characterization with T1 and T2 mapping supports recognition of myocardial involvement in patients with systemic sarcoidosis .

Example answer:
{"entities": [{"text": "Recognition", "type": "Finding"}, {"text": "Early Cardiac Involvement", "type": "Finding"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "recognition", "type": "Finding"}, {"text": "myocardial", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Thirty - two individuals , who were referred for positron emission tomography / computed tomography , were evaluated for known or suspected cardiac sarcoidosis applying ( 18 ) F - fluorodeoxyglucose to determine inflammation and ( 13 ) N - ammonia to assess for perfusion deficits following a high - fat / low - carbohydrate diet and fasting state > 12 h to suppress myocardial glucose uptake .

Example answer:
{"entities": [{"text": "individuals", "type": "PopulationGroup"}, {"text": "positron emission tomography", "type": "HealthCareActivity"}, {"text": "computed tomography", "type": "HealthCareActivity"}, {"text": "cardiac sarcoidosis", "type": "BiologicFunction"}, {"text": "( 18 ) F - fluorodeoxyglucose", "type": "Chemical"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "( 13 ) N - ammonia", "type": "Chemical"}, {"text": "perfusion deficits", "type": "Finding"}, {"text": "high - fat", "type": "HealthCareActivity"}, {"text": "low - carbohydrate diet", "type": "HealthCareActivity"}, {"text": "fasting state", "type": "Finding"}, {"text": "suppress", "type": "BiologicFunction"}, {"text": "myocardial", "type": "AnatomicalStructure"}, {"text": "glucose uptake", "type": "BiologicFunction"}]}

Example input:
Sentence: Risk stratification for major adverse cardiac events and ventricular tachyarrhythmias by cardiac MRI in patients with cardiac sarcoidosis The presence of myocardial fibrosis by cardiac MRI has prognostic value in cardiac sarcoidosis , and localisation may be equally relevant to clinical outcomes .

Example answer:
{"entities": [{"text": "stratification", "type": "ResearchActivity"}, {"text": "adverse cardiac events", "type": "Finding"}, {"text": "ventricular tachyarrhythmias", "type": "BiologicFunction"}, {"text": "cardiac MRI", "type": "HealthCareActivity"}, {"text": "cardiac sarcoidosis", "type": "BiologicFunction"}, {"text": "myocardial fibrosis", "type": "BiologicFunction"}, {"text": "prognostic value", "type": "ClinicalAttribute"}, {"text": "clinical outcomes", "type": "Finding"}]}

Example input:
Sentence: In patients with cardiac sarcoidosis , both fibrosis mass and its localisation to the basal anterior / anteroseptal left ventricle , or right ventricle was associated with the development of major adverse cardiac events or ventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "cardiac sarcoidosis", "type": "BiologicFunction"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "mass", "type": "Finding"}, {"text": "basal anterior", "type": "AnatomicalStructure"}, {"text": "anteroseptal left ventricle", "type": "AnatomicalStructure"}, {"text": "right ventricle", "type": "AnatomicalStructure"}, {"text": "adverse cardiac events", "type": "Finding"}, {"text": "ventricular tachyarrhythmias", "type": "BiologicFunction"}]}

Example input:
Sentence: Importantly , cardiac inflammation , fibrosis and systolic dysfunction were attenuated in GF mice , indicating systemic protection from cardiovascular inflammatory stress induced by AngII .

Example answer:
{"entities": [{"text": "fibrosis", "type": "BiologicFunction"}, {"text": "systolic dysfunction", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "cardiovascular inflammatory stress", "type": "Finding"}, {"text": "AngII", "type": "Chemical"}]}

Example input:
Sentence: Immune - suppression -mediated decrease in inflammation was associated with preserved myocardial flow reserve ( MFR ) at follow - up , whereas MFR significantly worsened in regions without changes or even increases in inflammation ( median Δ MFR : 0 . 07 [ IQR : -0 . 29 to 0 . 45 ] vs .

Example answer:
{"entities": [{"text": "Immune - suppression", "type": "HealthCareActivity"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "myocardial flow reserve", "type": "ClinicalAttribute"}, {"text": "MFR", "type": "ClinicalAttribute"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "worsened", "type": "Finding"}]}

Example input:
Sentence: Conclusion Quantitative myocardial tissue characterization with T1 and T2 mapping may enable noninvasive recognition of cardiac involvement and activity of myocardial inflammation in patients with systemic sarcoidosis .

Example answer:
{"entities": [{"text": "myocardial tissue", "type": "AnatomicalStructure"}, {"text": "noninvasive recognition", "type": "HealthCareActivity"}, {"text": "cardiac involvement", "type": "Finding"}, {"text": "myocardial inflammation", "type": "BiologicFunction"}]}

Example input:
Sentence: Although positron emission tomography assessment of myocardial inflammation is increasingly applied to identify active cardiac sarcoidosis , its effect on coronary flow and immune - suppressive treatment remains to be characterized .

Example answer:
{"entities": [{"text": "positron emission tomography", "type": "HealthCareActivity"}, {"text": "myocardial inflammation", "type": "BiologicFunction"}, {"text": "active cardiac sarcoidosis", "type": "BiologicFunction"}, {"text": "coronary flow", "type": "BiologicFunction"}, {"text": "immune - suppressive treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Sarcoid -mediated myocardial inflammation is associated with a regional impairment of coronary circulatory function .

Example answer:
{"entities": [{"text": "Sarcoid", "type": "BiologicFunction"}, {"text": "myocardial inflammation", "type": "BiologicFunction"}, {"text": "coronary circulatory", "type": "BiologicFunction"}]}

Example input:
Sentence: Myocardial Blood Flow and Inflammatory Cardiac Sarcoidosis This study sought to evaluate the effects of inflammatory sarcoid disease on coronary circulatory function and the response to immune - suppressive treatment .

Example answer:
{"entities": [{"text": "Myocardial Blood Flow", "type": "BiologicFunction"}, {"text": "Inflammatory", "type": "BiologicFunction"}, {"text": "Cardiac Sarcoidosis", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "inflammatory", "type": "BiologicFunction"}, {"text": "sarcoid disease", "type": "BiologicFunction"}, {"text": "coronary circulatory", "type": "BiologicFunction"}, {"text": "immune - suppressive treatment", "type": "HealthCareActivity"}]}

Input:
Sentence: The association between immune - suppressive treatment -related alterations in myocardial inflammation and changes in coronary vasodilator capacity suggests direct adverse effect of inflammation on coronary circulatory function in cardiac sarcoidosis .

## Item MedMentions:test:3326
Example input:
Sentence: Implications for assessment and subsequent treatment for pretend ability among children with varying degrees of ASD symptoms , as well as for future research , are discussed .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "ASD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: Ratings of adaptive and behavioral functioning approximately 2 years postdiagnosis were within the average range , although the percentage of children exceeding clinical cutoffs for impairment in adaptive skills exceeded expectation , particularly practical skills .

Example answer:
{"entities": [{"text": "postdiagnosis", "type": "Finding"}]}

Example input:
Sentence: After accounting for adjustment near diagnosis , no variables predicted declines in behavioral adjustment .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}]}

Example input:
Sentence: Suicidal thinking and behavior was associated with older child age and with higher rates of concurrent depression , oppositional defiant disorder , and posttraumatic stress disorder in univariate analyses , with age and depression remaining as significant predictors in a multivariate logistic regression model .

Example answer:
{"entities": [{"text": "Suicidal thinking", "type": "Finding"}, {"text": "behavior", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "posttraumatic stress disorder", "type": "BiologicFunction"}]}

Example input:
Sentence: The assessment included the Motor Severity Stereotypy Scale ( MSSS ) , the Repetitive Behavior Scale - Revised ( RBS - R ) , the Raven 's Colored Progressive Matrices , the Child Behavior CheckList for ages 1½ - 5 or 4 - 18 ( CBCL ) , the Social Responsiveness Scale ( SRS ) , and the Autism Diagnostic Observation Schedule - second edition ( ADOS 2 ) .

Example answer:
{"entities": [{"text": "assessment", "type": "HealthCareActivity"}, {"text": "Motor Severity Stereotypy Scale", "type": "IntellectualProduct"}, {"text": "MSSS", "type": "IntellectualProduct"}, {"text": "Repetitive Behavior Scale - Revised", "type": "IntellectualProduct"}, {"text": "RBS - R", "type": "IntellectualProduct"}, {"text": "Raven 's Colored Progressive Matrices", "type": "Finding"}, {"text": "Social Responsiveness Scale", "type": "IntellectualProduct"}, {"text": "( SRS )", "type": "IntellectualProduct"}, {"text": "Autism Diagnostic Observation Schedule - second edition", "type": "IntellectualProduct"}, {"text": "ADOS 2", "type": "IntellectualProduct"}]}

Example input:
Sentence: This study explored whether familial / demographic , developmental , diagnostic , or treatment -related variables best predict posttreatment behavioral and adaptive functioning .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The diagnosis of disruptive behaviour disorder ( DBD ) was assessed by a structured interview - the diagnostic interview schedule for children version IV ( DISC - IV ) .

Example answer:
{"entities": [{"text": "diagnosis", "type": "HealthCareActivity"}, {"text": "disruptive behaviour disorder", "type": "BiologicFunction"}, {"text": "DBD", "type": "BiologicFunction"}, {"text": "the diagnostic interview schedule for children version IV", "type": "IntellectualProduct"}, {"text": "DISC - IV", "type": "IntellectualProduct"}]}

Example input:
Sentence: Parents rated children ' s behavioral adjustment and adaptive functioning and provided demographic and developmental histories .

Example answer:
{"entities": [{"text": "histories", "type": "Finding"}]}

Example input:
Sentence: Increased recognition of neurodevelopmental processes in the origin of affective disorders may allow for earlier and more effective intervention and prevention .

Example answer:
{"entities": [{"text": "recognition", "type": "BiologicFunction"}, {"text": "affective disorders", "type": "BiologicFunction"}, {"text": "intervention", "type": "HealthCareActivity"}, {"text": "prevention", "type": "HealthCareActivity"}]}

Example input:
Sentence: After accounting for adaptive functioning near diagnosis , premorbid behavior problems predicted declines in adaptive functioning 2 years postdiagnosis .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "postdiagnosis", "type": "Finding"}]}

Input:
Sentence: Assessing prediagnosis functioning and diagnostic and treatment -related variables may improve our ability to predict those at greatest risk , although those factors may be less helpful in identifying children likely to develop behavioral difficulties .

## Item MedMentions:test:3274
Example input:
Sentence: After the MB probe was unfolded by the target DNA sequence , the labels of oligonucleotide encapsulated Ag NCs would be brought in close proximity to the CdS QDs electrode surface , and efficient photocurrent quenching of QDs could be resulted from an energy transfer process that originated from NCs .

Example answer:
{"entities": [{"text": "probe", "type": "MedicalDevice"}, {"text": "DNA sequence", "type": "SpatialConcept"}, {"text": "oligonucleotide", "type": "Chemical"}, {"text": "Ag", "type": "Chemical"}, {"text": "proximity", "type": "SpatialConcept"}, {"text": "CdS", "type": "Chemical"}, {"text": "energy transfer", "type": "BiologicFunction"}]}

Example input:
Sentence: The minimum inhibitory concentration ( MIC ) value against NSCs was 3 , 10 , and 300 mg / L , in each staining process , acridine orange / ethidium bromide ( AO / EB ) staining , 3 - ( 4 , 5 - dimethylthiazol - 2 - yl ) 2 , 5 - diphenyl tetrazolium bromide ( MTT ) assay , and Hoechst staining , for CH3HgCl , CP , and CH3COOPb , respectively .

Example answer:
{"entities": [{"text": "minimum inhibitory concentration ( MIC ) value", "type": "Finding"}, {"text": "NSCs", "type": "AnatomicalStructure"}, {"text": "staining process", "type": "HealthCareActivity"}, {"text": "acridine orange", "type": "Chemical"}, {"text": "ethidium bromide", "type": "Chemical"}, {"text": "AO", "type": "Chemical"}, {"text": "EB", "type": "Chemical"}, {"text": "staining", "type": "HealthCareActivity"}, {"text": "3 - ( 4 , 5 - dimethylthiazol - 2 - yl ) 2 , 5 - diphenyl tetrazolium bromide", "type": "Chemical"}, {"text": "MTT", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "CH3HgCl", "type": "Chemical"}, {"text": "CP", "type": "Chemical"}, {"text": "CH3COOPb", "type": "Chemical"}]}

Example input:
Sentence: The CT and CC genotypes were associated with a 50 % and a 2 - fold increased risk , respectively , of a suboptimal plasma 25 ( OH ) D concentration ( < 75 nmol / L ) .

Example answer:
{"entities": [{"text": "plasma", "type": "BodySubstance"}, {"text": "25 ( OH ) D", "type": "Chemical"}]}

Example input:
Sentence: Spectrum - based and color - selective electrochemiluminescence immunoassay for determining human prostate specific antigen in near - infrared region The conventional electrochemiluminescence ( ECL ) analyses were performed via detecting the time ( or potential ) dependent ECL intensity with the proceeding of ECL reaction .

Example answer:
{"entities": [{"text": "Spectrum - based and color - selective electrochemiluminescence immunoassay", "type": "HealthCareActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "prostate specific antigen", "type": "Chemical"}, {"text": "near - infrared region", "type": "SpatialConcept"}, {"text": "electrochemiluminescence", "type": "HealthCareActivity"}, {"text": "ECL", "type": "HealthCareActivity"}, {"text": "analyses", "type": "ResearchActivity"}]}

Example input:
Sentence: However , the high efficiency micro ( 540 ) - UCPs were suboptimal for NIR and visible light coalignment , due to their larger size and spatial broadening from particle -to - particle energy transfer consistent with a long - lived excited state and saturated power dependence .

Example answer:
{"entities": [{"text": "UCPs", "type": "Chemical"}, {"text": "size", "type": "SpatialConcept"}, {"text": "spatial broadening", "type": "SpatialConcept"}, {"text": "particle", "type": "Chemical"}, {"text": "energy transfer", "type": "BiologicFunction"}, {"text": "excited state", "type": "Finding"}]}

Example input:
Sentence: The bi - directiona l movement of the DNA walker on the track led to continuous distance - based energy transfer from CdS : Mn NCs film by AuNPs , which resulted in significant ECL signal variation of CdS : Mn NCs for multiple detection of miRNA - 21 and miRNA - 155 down to 1 . 51 fM and 1 . 67 fM , respectively .

Example answer:
{"entities": [{"text": "movement", "type": "BiologicFunction"}, {"text": "DNA walker", "type": "Chemical"}, {"text": "energy transfer", "type": "BiologicFunction"}, {"text": "CdS", "type": "Chemical"}, {"text": "Mn", "type": "Chemical"}, {"text": "ECL", "type": "HealthCareActivity"}, {"text": "miRNA - 21", "type": "Chemical"}, {"text": "miRNA - 155", "type": "Chemical"}]}

Example input:
Sentence: More than 5 - fold enhance in ECL intensity was observed after modified with rGO - CuS composite .

Example answer:
{"entities": [{"text": "ECL", "type": "HealthCareActivity"}, {"text": "rGO", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}]}

Example input:
Sentence: By using miRNA - 21 as the driving force , the DNA walker could move forth along the track and generated quenching of ECL response due to the proximity between Au nanoparticles ( AuNPs ) and Mn ( 2 + ) doped CdS nanocrystals ( CdS : Mn NCs ) film as the ECL emitters , realizing ultrasensitive determination of miRNA - 21 .

Example answer:
{"entities": [{"text": "miRNA - 21", "type": "Chemical"}, {"text": "DNA walker", "type": "Chemical"}, {"text": "quenching", "type": "BiologicFunction"}, {"text": "ECL", "type": "HealthCareActivity"}, {"text": "proximity", "type": "SpatialConcept"}, {"text": "Au", "type": "Chemical"}, {"text": "Mn ( 2 + )", "type": "Chemical"}, {"text": "CdS", "type": "Chemical"}, {"text": "Mn", "type": "Chemical"}, {"text": "determination", "type": "HealthCareActivity"}]}

Example input:
Sentence: 0fg / mL to 100 . 0pg / mL , indicating a sensitive and color - selective ECL immunoassay in NIR region with improved anti - interference performance to biological autofluorescence and tissue absorption .

Example answer:
{"entities": [{"text": "color - selective ECL immunoassay", "type": "HealthCareActivity"}, {"text": "NIR region", "type": "SpatialConcept"}, {"text": "autofluorescence", "type": "HealthCareActivity"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Herein , by spectrally recording all the photons generated in ECL process , a spectral ECL immunoassay was developed in near - infrared ( NIR ) region with human prostate specific antigen ( PSA ) as target and dual - stabilizers - capped CdTe nanocrystals ( NCs ) as tags .

Example answer:
{"entities": [{"text": "ECL", "type": "HealthCareActivity"}, {"text": "spectral ECL immunoassay", "type": "HealthCareActivity"}, {"text": "near - infrared ( NIR ) region", "type": "SpatialConcept"}, {"text": "human", "type": "Eukaryote"}, {"text": "prostate specific antigen", "type": "Chemical"}, {"text": "PSA", "type": "Chemical"}, {"text": "dual - stabilizers - capped CdTe", "type": "Chemical"}, {"text": "tags", "type": "MedicalDevice"}]}

Input:
Sentence: The CdTe NCs displayed efficient ECL around 780 nm with the full width at half - maximum around 70 nm in the immune - complexes , the maximum intensity on ECL spectrum profiles increased linearly with the logarithmic increased concentration of PSA from 20 .

## Item MedMentions:test:3324
Example input:
Sentence: The biofilm formation is one of the most ubiquitous adaptive response observed in prokaryotes to various stresses , such as those induced in the presence of toxic compounds .

Example answer:
{"entities": [{"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "toxic", "type": "InjuryOrPoisoning"}, {"text": "compounds", "type": "Chemical"}]}

Example input:
Sentence: Biofilm formation was significantly promoted ( p < 0 . 05 ) by 5 and 10 µM C6 - HSL , inhibited ( p < 0 . 05 ) by C4 - HSL ( 5 and 10 µM ) and 5 µM 3 - oxo - C8 - HSL , suggesting that QS may have a regulatory role in the biofilm formation of H .

Example answer:
{"entities": [{"text": "Biofilm formation", "type": "BiologicFunction"}, {"text": "C6 - HSL", "type": "Chemical"}, {"text": "C4 - HSL", "type": "Chemical"}, {"text": "3 - oxo - C8 - HSL", "type": "Chemical"}, {"text": "QS", "type": "BiologicFunction"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "H .", "type": "Bacterium"}]}

Example input:
Sentence: This study focused on the process of biofilm formation in three Thiomonas strains ( CB1 , CB2 and CB3 ) isolated from the same AMD .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "Thiomonas strains", "type": "Bacterium"}, {"text": "CB1", "type": "Bacterium"}, {"text": "CB2", "type": "Bacterium"}, {"text": "CB3", "type": "Bacterium"}]}

Example input:
Sentence: aureus strains of the same capsular phenotype with different biofilm forming strengths were used to non - invasively infect mammary glands of lactating mice .

Example answer:
{"entities": [{"text": "aureus", "type": "Bacterium"}, {"text": "capsular", "type": "SpatialConcept"}, {"text": "biofilm forming", "type": "BiologicFunction"}, {"text": "mammary glands", "type": "AnatomicalStructure"}, {"text": "lactating", "type": "Finding"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Together , the data demonstrate that coaggregation networks within an individual 's oral microflora are extensive and that Rothia and Haemophilus can be important initiators of cell - cell interactions in the early biofilm .IMPORTANCE Extensive involvement of specific interbacterial adhesion in dental plaque biofilm formation has been postulated based on in vitro coaggregation between oral bacteria from culture collections that are not subject specific .

Example answer:
{"entities": [{"text": "Rothia", "type": "Bacterium"}, {"text": "Haemophilus", "type": "Bacterium"}, {"text": "cell - cell interactions", "type": "BiologicFunction"}, {"text": "biofilm", "type": "Bacterium"}, {"text": "adhesion", "type": "BiologicFunction"}, {"text": "dental plaque", "type": "BiologicFunction"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "oral bacteria", "type": "Bacterium"}, {"text": "subject", "type": "PopulationGroup"}]}

Example input:
Sentence: The object of this study was to explore the effect of surface properties including surface roughness and hydrophobicity on the adhesion and biofilm formation of Streptococcus mutans ( S . mutans ) to zirconia .

Example answer:
{"entities": [{"text": "surface roughness", "type": "Finding"}, {"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "Streptococcus mutans", "type": "Bacterium"}, {"text": "S . mutans", "type": "Bacterium"}, {"text": "zirconia", "type": "Chemical"}]}

Example input:
Sentence: aureus than the weak biofilm forming strain .

Example answer:
{"entities": [{"text": "aureus", "type": "Bacterium"}, {"text": "biofilm forming", "type": "BiologicFunction"}]}

Example input:
Sentence: The findings obtained here shed interesting light on how the formation of biofilms , and the motility processes contribute to the adaptation of Thiomonas strains to extreme environments .

Example answer:
{"entities": [{"text": "formation of biofilms", "type": "BiologicFunction"}, {"text": "motility processes", "type": "BiologicFunction"}, {"text": "adaptation", "type": "BiologicFunction"}, {"text": "Thiomonas strains", "type": "Bacterium"}, {"text": "environments", "type": "SpatialConcept"}]}

Example input:
Sentence: strains revealed divergent response to arsenite Bacteria of the genus Thiomonas are found ubiquitously in arsenic contaminated waters such as acid mine drainage ( AMD ) , where they contribute to the precipitation and the natural bioremediation of arsenic .

Example answer:
{"entities": [{"text": "strains", "type": "Bacterium"}, {"text": "arsenite", "type": "Chemical"}, {"text": "Bacteria", "type": "Bacterium"}, {"text": "genus", "type": "IntellectualProduct"}, {"text": "Thiomonas", "type": "Bacterium"}, {"text": "found ubiquitously", "type": "Finding"}, {"text": "arsenic", "type": "Chemical"}]}

Example input:
Sentence: Comparison of biofilm formation and motility processes in arsenic - resistant Thiomonas spp .

Example answer:
{"entities": [{"text": "biofilm formation", "type": "BiologicFunction"}, {"text": "motility processes", "type": "BiologicFunction"}, {"text": "arsenic", "type": "Chemical"}, {"text": "Thiomonas spp .", "type": "Bacterium"}]}

Input:
Sentence: Indeed , two strains favoured biofilm formation , whereas one favoured motility in the presence of arsenite .

## Item MedMentions:test:3296
Example input:
Sentence: Rupture of GORE - TEX neochordae 10 years after mitral valve repair The current non - resectional paradigm in mitral valve ( MV ) repair emphasizes the use of polytetrafluoroethylene ( PTFE ) for artificial chordal replacement .

Example answer:
{"entities": [{"text": "GORE - TEX neochordae", "type": "Chemical"}, {"text": "resectional", "type": "HealthCareActivity"}, {"text": "polytetrafluoroethylene", "type": "Chemical"}, {"text": "PTFE", "type": "Chemical"}, {"text": "artificial chordal replacement", "type": "HealthCareActivity"}]}

Example input:
Sentence: A Double - Blind Randomized Controlled Trial of Maternal Postpartum Deworming to Improve Infant Weight Gain in the Peruvian Amazon Nutritional interventions targeting the critical growth and development period before two years of age can have the greatest impact on health trajectories over the life course .

Example answer:
{"entities": [{"text": "Double - Blind", "type": "ResearchActivity"}, {"text": "Randomized Controlled Trial", "type": "ResearchActivity"}, {"text": "Maternal Postpartum", "type": "BiologicFunction"}, {"text": "Deworming", "type": "HealthCareActivity"}, {"text": "Weight Gain", "type": "Finding"}, {"text": "Nutritional interventions", "type": "HealthCareActivity"}]}

Example input:
Sentence: While excellent long - term durability of repair using PTFE neochordae has been established , there have been rare reports of neochordal rupture at various times after surgery .

Example answer:
{"entities": [{"text": "PTFE neochordae", "type": "Chemical"}, {"text": "reports", "type": "HealthCareActivity"}, {"text": "neochordal rupture", "type": "BiologicFunction"}, {"text": "surgery", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: We postulate that variants in CHH genes , in particular PROKR2 , PROK2 , WDR11 and FGFR1 with CHD7 , may contribute to under - virilisation phenotypes including hypospadias in Indonesia .

Example answer:
{"entities": [{"text": "CHH", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "PROKR2", "type": "AnatomicalStructure"}, {"text": "PROK2", "type": "AnatomicalStructure"}, {"text": "WDR11", "type": "AnatomicalStructure"}, {"text": "FGFR1", "type": "AnatomicalStructure"}, {"text": "CHD7", "type": "AnatomicalStructure"}, {"text": "under - virilisation", "type": "BiologicFunction"}, {"text": "hypospadias", "type": "BiologicFunction"}, {"text": "Indonesia", "type": "SpatialConcept"}]}

Example input:
Sentence: Over 4 years ( between Jan 2011 and Jan 2015 ) , all cases of severe hypospadias were included in this study ; except those with prior attempts at repair , circumcised cases , and cases with severe hypogonadism - because of partial androgen insensitivity - not responding to hormonal manipulations .

Example answer:
{"entities": [{"text": "hypospadias", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "attempts at repair", "type": "HealthCareActivity"}, {"text": "circumcised", "type": "Finding"}, {"text": "hypogonadism", "type": "BiologicFunction"}, {"text": "partial androgen insensitivity", "type": "BiologicFunction"}, {"text": "hormonal manipulations", "type": "HealthCareActivity"}]}

Example input:
Sentence: Koyanagi repair ( parameatal - based and fully extended circumferential foreskin flap urethroplasty ) has enabled correction of severe hypospadias in one stage .

Example answer:
{"entities": [{"text": "Koyanagi repair", "type": "HealthCareActivity"}, {"text": "parameatal - based", "type": "SpatialConcept"}, {"text": "extended", "type": "SpatialConcept"}, {"text": "circumferential", "type": "SpatialConcept"}, {"text": "foreskin", "type": "AnatomicalStructure"}, {"text": "flap urethroplasty", "type": "HealthCareActivity"}]}

Example input:
Sentence: Single - staged repair of severe hypospadias using parameatal foreskin - based urethroplasty has passed through different modifications , all aimed at optimizing the outcome ( Table ) .

Example answer:
{"entities": [{"text": "parameatal foreskin", "type": "AnatomicalStructure"}, {"text": "urethroplasty", "type": "HealthCareActivity"}]}

Example input:
Sentence: To retrospectively analyze the outcome of a proposed modification of the originally described yoke repair , for patients with severe hypospadias .

Example answer:
{"entities": [{"text": "analyze", "type": "ResearchActivity"}, {"text": "yoke repair", "type": "HealthCareActivity"}, {"text": "hypospadias", "type": "BiologicFunction"}]}

Example input:
Sentence: 48 months had repair of severe hypospadias using the neo - yoke technique .

Example answer:
{"entities": [{"text": "repair of severe hypospadias", "type": "HealthCareActivity"}, {"text": "neo - yoke technique", "type": "HealthCareActivity"}]}

Example input:
Sentence: Neo - yoke repair for severe hypospadias : A simple modification for better outcome Although staged repair for reconstructing severe hypospadias is more popular , various one - stage repairs have been attempted .

Example answer:
{"entities": [{"text": "Neo - yoke repair", "type": "HealthCareActivity"}, {"text": "hypospadias", "type": "BiologicFunction"}, {"text": "staged repair", "type": "HealthCareActivity"}, {"text": "one - stage repairs", "type": "HealthCareActivity"}]}

Input:
Sentence: Neo - yoke repair for severe hypospadias is a natural development of established one - stage techniques , which resulted in better mid - term outcomes .

## Item MedMentions:test:3348
Example input:
Sentence: The total sample included 29 , 010 females and 70 , 995 males .

Example answer:
{"entities": []}

Example input:
Sentence: The cumulative 5 - year incidence of all - cause death was significantly higher in men than in women ( 47 % vs .

Example answer:
{"entities": [{"text": "death", "type": "BiologicFunction"}, {"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: The CHE incidence of empty - nest singles ( 59 . 3 % , p = 0 . 000 , OR = 3 . 19 ) and empty - nest couples ( 52 . 9 % , p = 0 . 000 , OR = 2 . 45 ) are both statistically higher than that of non - empty - nest elderly households ( 31 . 4 % ) .

Example answer:
{"entities": [{"text": "singles", "type": "Finding"}, {"text": "elderly", "type": "PopulationGroup"}]}

Example input:
Sentence: We performed a large epidemiologic study on hospital admissions for portal vein thrombosis ( PVT ) and the Budd - Chiari syndrome ( BCS ) between 2002 and 2012 in Northwestern Italy .

Example answer:
{"entities": [{"text": "epidemiologic study", "type": "ResearchActivity"}, {"text": "hospital admissions", "type": "HealthCareActivity"}, {"text": "portal vein thrombosis", "type": "BiologicFunction"}, {"text": "PVT", "type": "BiologicFunction"}, {"text": "Budd - Chiari syndrome", "type": "BiologicFunction"}, {"text": "BCS", "type": "BiologicFunction"}, {"text": "Northwestern Italy", "type": "SpatialConcept"}]}

Example input:
Sentence: Age , non - abdominal solid cancer , and CCI were independently associated with in - hospital mortality in both PVT and BCS after stepwise regression analysis , male gender and haematologic cancer were associated with mortality in BCS patients only .

Example answer:
{"entities": [{"text": "non - abdominal solid cancer", "type": "BiologicFunction"}, {"text": "PVT", "type": "BiologicFunction"}, {"text": "BCS", "type": "BiologicFunction"}, {"text": "regression analysis", "type": "IntellectualProduct"}, {"text": "haematologic cancer", "type": "BiologicFunction"}, {"text": "mortality", "type": "Finding"}]}

Example input:
Sentence: A total of 3535 patients with PVT and 287 with BCS were hospitalized .

Example answer:
{"entities": [{"text": "PVT", "type": "BiologicFunction"}, {"text": "BCS", "type": "BiologicFunction"}, {"text": "hospitalized", "type": "Finding"}]}

Example input:
Sentence: The STI incidence rates ( per 100 person - years ) for women and men , respectively , were as follows : chlamydia ( 3 . 5 and 0 . 7 ) , gonorrhea ( 1 . 1 and 0 . 4 ) , HIV ( 0 . 04 and 0 . 07 ) and syphilis ( 0 . 14 and 0 . 15 ) .

Example answer:
{"entities": [{"text": "STI", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}, {"text": "chlamydia", "type": "BiologicFunction"}, {"text": "gonorrhea", "type": "BiologicFunction"}, {"text": "HIV", "type": "BiologicFunction"}, {"text": "syphilis", "type": "BiologicFunction"}]}

Example input:
Sentence: In all , 181 , 814 BC patients ( 1 , 516 male and 180 , 298 female ) were eligible for this study .

Example answer:
{"entities": [{"text": "BC", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: 3 % in patients with PVT and 4 . 9 % in patients with BCS .

Example answer:
{"entities": [{"text": "PVT", "type": "BiologicFunction"}, {"text": "BCS", "type": "BiologicFunction"}]}

Example input:
Sentence: In this large study we confirmed the low incidence of BCS and we found an incidence of PVT higher than previously reported .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "BCS", "type": "BiologicFunction"}, {"text": "PVT", "type": "BiologicFunction"}]}

Input:
Sentence: The overall gender - specific incidence rates for PVT were 3 . 78 per 100 , 000 inhabitants in males and 1 . 73 per 100 , 000 inhabitants in females ; for BCS 2 .

## Item MedMentions:test:3273
Example input:
Sentence: Facial numbness was least likely to occur with MVD ( 16 % ) compared to RF and SRS ( 50 % and 36 % respectively ) .

Example answer:
{"entities": [{"text": "Facial numbness", "type": "Finding"}, {"text": "MVD", "type": "HealthCareActivity"}, {"text": "RF", "type": "HealthCareActivity"}, {"text": "SRS", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the aortic banding model , the sensitivity of systolic Ca ( 2 + ) to LCC density and diastolic Ca ( 2 + ) to SERCA density decreased by 16 - fold and increased by 23 % , respectively , relative to the SHAM model .

Example answer:
{"entities": [{"text": "aortic", "type": "AnatomicalStructure"}, {"text": "banding", "type": "HealthCareActivity"}, {"text": "model", "type": "IntellectualProduct"}, {"text": "Ca ( 2 + )", "type": "Chemical"}, {"text": "LCC", "type": "Chemical"}, {"text": "diastolic", "type": "ClinicalAttribute"}, {"text": "SERCA", "type": "Chemical"}, {"text": "SHAM model", "type": "Eukaryote"}]}

Example input:
Sentence: Debonding leads to a short - term increase in tooth sensitivity .

Example answer:
{"entities": [{"text": "Debonding", "type": "HealthCareActivity"}, {"text": "tooth sensitivity", "type": "BiologicFunction"}]}

Example input:
Sentence: Myopes showed worse blur sensitivity than emmetropes monocularly ( p < 0 .

Example answer:
{"entities": [{"text": "Myopes", "type": "BiologicFunction"}, {"text": "worse", "type": "Finding"}, {"text": "emmetropes", "type": "Finding"}, {"text": "monocularly", "type": "BiologicFunction"}]}

Example input:
Sentence: Oxytocin Reduces Face Processing Time but Leaves Recognition Accuracy and Eye - Gaze Unaffected Previous studies have found that oxytocin ( OXT ) can improve the recognition of emotional facial expressions ; it has been proposed that this effect is mediated by an increase in attention to the eye - region of faces .

Example answer:
{"entities": [{"text": "Oxytocin", "type": "Chemical"}, {"text": "Face", "type": "SpatialConcept"}, {"text": "Recognition", "type": "BiologicFunction"}, {"text": "Eye", "type": "AnatomicalStructure"}, {"text": "Gaze", "type": "Finding"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "oxytocin", "type": "Chemical"}, {"text": "OXT", "type": "Chemical"}, {"text": "improve", "type": "Finding"}, {"text": "recognition", "type": "BiologicFunction"}, {"text": "emotional", "type": "Finding"}, {"text": "facial expressions", "type": "Finding"}, {"text": "attention", "type": "BiologicFunction"}, {"text": "eye - region", "type": "SpatialConcept"}, {"text": "faces", "type": "SpatialConcept"}]}

Example input:
Sentence: Scars in the axilla and IMF can achieve comparable cosmetic effects and patient satisfaction in Chinese women .

Example answer:
{"entities": [{"text": "Scars", "type": "AnatomicalStructure"}, {"text": "axilla", "type": "HealthCareActivity"}, {"text": "IMF", "type": "SpatialConcept"}, {"text": "Chinese", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: However , the patients with visible EMCs showed higher visual analog scale values at each time interval .

Example answer:
{"entities": [{"text": "EMCs", "type": "InjuryOrPoisoning"}, {"text": "visual analog scale", "type": "HealthCareActivity"}]}

Example input:
Sentence: For the patients without visible EMCs , discomfort peaked immediately after debonding and started to decrease on day 1 ; at 1 week after debonding , the visual analog scale scores were lower than just before debonding and immediately after debonding .

Example answer:
{"entities": [{"text": "EMCs", "type": "InjuryOrPoisoning"}, {"text": "discomfort", "type": "Finding"}, {"text": "debonding", "type": "HealthCareActivity"}, {"text": "visual analog scale", "type": "HealthCareActivity"}]}

Example input:
Sentence: After debonding , 15 patients possessing teeth with visible EMCs and 15 subjects whose teeth were free of EMCs were enrolled in the study .

Example answer:
{"entities": [{"text": "debonding", "type": "HealthCareActivity"}, {"text": "teeth", "type": "AnatomicalStructure"}, {"text": "EMCs", "type": "InjuryOrPoisoning"}, {"text": "subjects", "type": "PopulationGroup"}, {"text": "enrolled", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Comparison of teeth with and without visible enamel microcracks Our aim was to assess the possible changes in sensitivity of teeth with and without visible enamel microcracks ( EMCs ) up to 1 week after the removal of metal brackets .

Example answer:
{"entities": [{"text": "teeth", "type": "AnatomicalStructure"}, {"text": "enamel", "type": "BodySubstance"}, {"text": "microcracks", "type": "InjuryOrPoisoning"}, {"text": "sensitivity of teeth", "type": "BiologicFunction"}, {"text": "enamel microcracks", "type": "InjuryOrPoisoning"}, {"text": "( EMCs )", "type": "InjuryOrPoisoning"}, {"text": "metal brackets", "type": "MedicalDevice"}]}

Input:
Sentence: EMCs , a form of enamel damage , do not predispose to greater sensitivity perception in relation to bracket removal .

## Item MedMentions:test:3356
Example input:
Sentence: In the last decades , in addition to surgery , self - expanding metallic stents ( SEMSs ) are available both as a bridge to surgery ( BTS ) or palliation .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "self - expanding metallic stents", "type": "MedicalDevice"}, {"text": "( SEMSs )", "type": "MedicalDevice"}, {"text": "palliation", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: Endovascular treatment was performed by means of a vascular reconstruction technique that used at different surgical times : overlapping ; a telescoped self - expandable stent , LEO + ; and a flow - diverter device , SILK .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "vascular", "type": "AnatomicalStructure"}, {"text": "reconstruction technique", "type": "HealthCareActivity"}, {"text": "overlapping ; a telescoped self - expandable stent", "type": "HealthCareActivity"}, {"text": "LEO +", "type": "MedicalDevice"}, {"text": "flow - diverter device", "type": "MedicalDevice"}, {"text": "SILK", "type": "MedicalDevice"}]}

Example input:
Sentence: To address these problems , we have developed a biomechanical modeling guided CBCT estimation technique ( Bio - CBCT - est ) by combining 2D - 3D deformation with finite element analysis ( FEA ) - based biomechanical modeling of anatomical structures .

Example answer:
{"entities": [{"text": "modeling", "type": "ResearchActivity"}, {"text": "CBCT", "type": "HealthCareActivity"}, {"text": "estimation technique", "type": "IntellectualProduct"}, {"text": "Bio - CBCT - est", "type": "IntellectualProduct"}, {"text": "2D", "type": "SpatialConcept"}, {"text": "3D", "type": "SpatialConcept"}, {"text": "finite element analysis", "type": "IntellectualProduct"}, {"text": "FEA", "type": "IntellectualProduct"}, {"text": "anatomical structures", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Three hyperelastic plaque types as well as five elastoplastic stents were simulated .

Example answer:
{"entities": [{"text": "plaque", "type": "Finding"}, {"text": "elastoplastic stents", "type": "MedicalDevice"}]}

Example input:
Sentence: µCT - based FE models of cartilage - bone enabled us to quantify the distribution of the applied compression which was transferred through the articular cartilage to its underlying SCB , and to investigate the mechanism and the mode of SCB tissue failure .

Example answer:
{"entities": [{"text": "µCT - based", "type": "HealthCareActivity"}, {"text": "FE models", "type": "IntellectualProduct"}, {"text": "cartilage - bone", "type": "AnatomicalStructure"}, {"text": "articular cartilage", "type": "AnatomicalStructure"}, {"text": "SCB", "type": "AnatomicalStructure"}, {"text": "SCB tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The FE models were analysed under axial compressions of approximately 30MPa applied to the cartilage surface while the bone edges were constrained .

Example answer:
{"entities": [{"text": "FE models", "type": "IntellectualProduct"}, {"text": "analysed", "type": "ResearchActivity"}, {"text": "axial", "type": "SpatialConcept"}, {"text": "cartilage surface", "type": "SpatialConcept"}, {"text": "bone", "type": "AnatomicalStructure"}, {"text": "edges", "type": "SpatialConcept"}]}

Example input:
Sentence: In this study , we used high - resolution micro - computed tomography ( µCT ) - based finite element ( FE ) modelling of cartilage - bone to evaluate the failure mechanism and the locations of SCB tissue at high - risk of initial failure under compression .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "high - resolution micro - computed tomography", "type": "HealthCareActivity"}, {"text": "µCT", "type": "HealthCareActivity"}, {"text": "finite element ( FE ) modelling", "type": "IntellectualProduct"}, {"text": "cartilage - bone", "type": "AnatomicalStructure"}, {"text": "locations", "type": "SpatialConcept"}, {"text": "SCB tissue", "type": "AnatomicalStructure"}, {"text": "high - risk of", "type": "Finding"}]}

Example input:
Sentence: Steel stent showed the lowest foreshortening and fully expansion pressure but the difference was much lower than that the one for dogboning .

Example answer:
{"entities": [{"text": "Steel", "type": "Chemical"}, {"text": "stent", "type": "MedicalDevice"}, {"text": "foreshortening", "type": "Finding"}]}

Example input:
Sentence: A numerical study on the application of the functionally graded materials in the stent design Undesirable deformation of the stent can induce a significant amount of injure not only to the blood vessel but also to the plaque .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "stent", "type": "MedicalDevice"}, {"text": "significant", "type": "InjuryOrPoisoning"}, {"text": "injure", "type": "InjuryOrPoisoning"}, {"text": "blood vessel", "type": "AnatomicalStructure"}, {"text": "plaque", "type": "Finding"}]}

Example input:
Sentence: Dogboning , foreshortening , maximum stress in the plaque , and the pressure which is needed to fully expand the stent for different stent materials , were acquired .

Example answer:
{"entities": [{"text": "foreshortening", "type": "Finding"}, {"text": "stress", "type": "Finding"}, {"text": "plaque", "type": "Finding"}, {"text": "expand", "type": "SpatialConcept"}, {"text": "stent", "type": "MedicalDevice"}]}

Input:
Sentence: To do this , Finite Element ( FE ) method was employed to simulate the expansion of a stent and the corresponding displacement of the stenosis plaque .

## Item MedMentions:test:3560
Example input:
Sentence: 0007 ; 3 . 02 vs .

Example answer:
{"entities": []}

Example input:
Sentence: 0397 )

Example answer:
{"entities": []}

Example input:
Sentence: 039 )

Example answer:
{"entities": []}

Example input:
Sentence: 012 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 012 and 0 . 041 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: 035 , P = .260 .

Example answer:
{"entities": []}

Example input:
Sentence: 012 )

Example answer:
{"entities": []}

Example input:
Sentence: 034 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 038 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 035 ) .

Example answer:
{"entities": []}

Input:
Sentence: 032 )

## Item MedMentions:test:3199
Example input:
Sentence: Natural competence for transformation While most molecular biologists are familiar with the artificial transformation of bacteria in the context of laboratory cloning experiments , natural competence for transformation refers to a specific physiological state in which prokaryotes are able to take up genetic material from their surroundings .

Example answer:
{"entities": [{"text": "transformation", "type": "BiologicFunction"}, {"text": "transformation of bacteria", "type": "BiologicFunction"}, {"text": "laboratory", "type": "Organization"}, {"text": "cloning", "type": "ResearchActivity"}, {"text": "experiments", "type": "ResearchActivity"}, {"text": "genetic material", "type": "AnatomicalStructure"}, {"text": "surroundings", "type": "SpatialConcept"}]}

Example input:
Sentence: Escherichia coli HGT : Engineered for high glucose throughput even under slowly growing or resting conditions Aerobic production - scale processes are constrained by the technical limitations of maximum oxygen transfer and heat removal .

Example answer:
{"entities": [{"text": "Escherichia coli HGT", "type": "Bacterium"}, {"text": "Engineered", "type": "ResearchActivity"}, {"text": "high glucose", "type": "Finding"}, {"text": "throughput", "type": "BiologicFunction"}, {"text": "slowly growing", "type": "Finding"}, {"text": "resting conditions", "type": "Finding"}, {"text": "oxygen transfer", "type": "Finding"}]}

Example input:
Sentence: The possession of a highly mobile genome has contributed to the genetic diversity and ongoing evolution of C .

Example answer:
{"entities": [{"text": "mobile genome", "type": "AnatomicalStructure"}, {"text": "evolution", "type": "BiologicFunction"}, {"text": "C .", "type": "Bacterium"}]}

Example input:
Sentence: The gene content of these two transposons differ considerably which could impact upon horizontal gene transfer ; differences include CDSs encoding methylases and a conjugative prophage only in Tn6164 .

Example answer:
{"entities": [{"text": "gene content", "type": "AnatomicalStructure"}, {"text": "transposons", "type": "Chemical"}, {"text": "horizontal gene transfer", "type": "BiologicFunction"}, {"text": "CDSs", "type": "SpatialConcept"}, {"text": "methylases", "type": "Chemical"}, {"text": "conjugative prophage", "type": "Virus"}, {"text": "Tn6164", "type": "Chemical"}]}

Example input:
Sentence: HGT plays a major role in bacterial evolution , and past research has demonstrated that HGT , including natural competence for transformation , contributes to the emergence of pathogens and the spread of virulence factors .

Example answer:
{"entities": [{"text": "HGT", "type": "BiologicFunction"}, {"text": "evolution", "type": "BiologicFunction"}, {"text": "research", "type": "ResearchActivity"}, {"text": "transformation", "type": "BiologicFunction"}, {"text": "virulence factors", "type": "Chemical"}]}

Example input:
Sentence: Overall , heritability ( H2 ) was calculated for GYLD , LM6 and JIM and resulted to be 0 . 42 , 0 . 32 and 0 . 20 , respectively .

Example answer:
{"entities": [{"text": "LM6", "type": "Chemical"}, {"text": "JIM", "type": "Chemical"}]}

Example input:
Sentence: The homologous recombination efficiencies of the double mutant ∆l sku70∆lslig4 and the triple mutant ∆lsku70∆lsku80∆lslig4 were also markedly enhanced .

Example answer:
{"entities": [{"text": "homologous recombination", "type": "BiologicFunction"}, {"text": "mutant", "type": "AnatomicalStructure"}, {"text": "∆l sku70∆lslig4", "type": "AnatomicalStructure"}, {"text": "∆lsku70∆lsku80∆lslig4", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The carriage of horizontally transferred genes appear to have genome wide effects based on two different methylation patterns .

Example answer:
{"entities": [{"text": "horizontally transferred genes", "type": "AnatomicalStructure"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "methylation", "type": "BiologicFunction"}, {"text": "patterns", "type": "SpatialConcept"}]}

Example input:
Sentence: Data suggests that both mechanisms are functional and impact upon horizontal gene transfer and genome evolution within C .

Example answer:
{"entities": [{"text": "horizontal gene transfer", "type": "BiologicFunction"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "C .", "type": "Bacterium"}]}

Example input:
Sentence: As a consequence , natural competence for transformation is considered a primary mode of horizontal gene transfer ( HGT ) in prokaryotes , together with conjugation ( direct cell to cell transfer of DNA via a specialized conjugal pilus ) and phage transduction ( DNA transfer mediated by viruses ) .

Example answer:
{"entities": [{"text": "transformation", "type": "BiologicFunction"}, {"text": "horizontal gene transfer", "type": "BiologicFunction"}, {"text": "HGT", "type": "BiologicFunction"}, {"text": "conjugation", "type": "BiologicFunction"}, {"text": "cell", "type": "AnatomicalStructure"}, {"text": "DNA", "type": "Chemical"}, {"text": "conjugal pilus", "type": "AnatomicalStructure"}, {"text": "phage", "type": "Virus"}, {"text": "transduction", "type": "BiologicFunction"}, {"text": "viruses", "type": "Virus"}]}

Input:
Sentence: Together with high mutation rates and an efficient DNA recombination system , horizontal gene transfer through natural competence makes of H .

## Item MedMentions:test:3431
Example input:
Sentence: This review is aimed at collecting and summarizing available evidence from experimental and mechanistic studies on the action of GLP1 - RA and DPP4i on the cardiovascular system , both deriving from clinical and pre - clinical sources .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "experimental", "type": "ResearchActivity"}, {"text": "mechanistic studies", "type": "ResearchActivity"}, {"text": "GLP1 - RA", "type": "Chemical"}, {"text": "DPP4i", "type": "Chemical"}, {"text": "cardiovascular system", "type": "BodySystem"}]}

Example input:
Sentence: Rheumatoid arthritis , insulin resistance , and diabetes Recent progress in the management of rheumatoid arthritis ( RA ) is turning attention toward comorbidities , such as diabetes .

Example answer:
{"entities": [{"text": "Rheumatoid arthritis", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "management", "type": "HealthCareActivity"}, {"text": "rheumatoid arthritis", "type": "BiologicFunction"}, {"text": "RA", "type": "BiologicFunction"}]}

Example input:
Sentence: The increased insulin resistance seen in RA is closely linked to the systemic inflammation induced by certain proinflammatory cytokines such as tumor necrosis factor α ( TNFα ) and interleukin - 6 .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "proinflammatory cytokines", "type": "Chemical"}, {"text": "tumor necrosis factor α", "type": "Chemical"}, {"text": "TNFα", "type": "Chemical"}, {"text": "interleukin - 6", "type": "Chemical"}]}

Example input:
Sentence: The objectives of this review are to clarify the links between RA and diabetes and to assess potential effects of disease - modifying antirheumatic drugs ( DMARDs ) on diabetes .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "disease - modifying antirheumatic drugs", "type": "Chemical"}, {"text": "DMARDs", "type": "Chemical"}]}

Example input:
Sentence: Studies are underway to address these knowledge gaps and may be expected to inform cardiovascular risk management in RA and the general population .

Example answer:
{"entities": [{"text": "Studies", "type": "ResearchActivity"}, {"text": "knowledge", "type": "IntellectualProduct"}, {"text": "management", "type": "HealthCareActivity"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "general population", "type": "PopulationGroup"}]}

Example input:
Sentence: Growing evidence suggests lower lipid levels are present in patients with active RA vs .

Example answer:
{"entities": [{"text": "lipid levels", "type": "Finding"}, {"text": "present", "type": "Finding"}, {"text": "RA", "type": "BiologicFunction"}]}

Example input:
Sentence: Increase in lipid levels in patients with RA on synthetic and biological disease - modifying antirheumatic drugs may be accompanied by antiatherogenic changes in lipid composition and function .

Example answer:
{"entities": [{"text": "lipid levels", "type": "Finding"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "synthetic", "type": "Chemical"}, {"text": "disease - modifying antirheumatic drugs", "type": "Chemical"}, {"text": "lipid", "type": "Chemical"}, {"text": "composition", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Knowledge about quantitative and qualitative lipid changes in RA is expanding .

Example answer:
{"entities": [{"text": "Knowledge", "type": "IntellectualProduct"}, {"text": "lipid", "type": "Chemical"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "expanding", "type": "SpatialConcept"}]}

Example input:
Sentence: The relative role of lipids in cardiovascular risk in the context of systemic inflammation and antirheumatic therapy remains uncertain , delaying development of effective strategies for cardiovascular risk management in RA .

Example answer:
{"entities": [{"text": "lipids", "type": "Chemical"}, {"text": "antirheumatic therapy", "type": "HealthCareActivity"}, {"text": "management", "type": "HealthCareActivity"}, {"text": "RA", "type": "BiologicFunction"}]}

Example input:
Sentence: The role of lipids in cardiovascular risk in RA may be overpowered by the benefits of inflammation suppression with antirheumatic medication use .

Example answer:
{"entities": [{"text": "lipids", "type": "Chemical"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "suppression", "type": "BiologicFunction"}, {"text": "antirheumatic medication", "type": "Chemical"}]}

Input:
Sentence: The impact of lipid changes on cardiovascular outcomes in RA is a subject of active research .

## Item MedMentions:test:3570
Example input:
Sentence: Review of randomised clinical trials that used a non - inferiority design published between January 2010 and May 2015 in medical journals that had an impact factor > 10 ( JAMA Internal Medicine , Archives Internal Medicine , PLOS Medicine , Annals of Internal Medicine , BMJ , JAMA , Lancet and New England Journal of Medicine ) .

Example answer:
{"entities": [{"text": "randomised", "type": "ResearchActivity"}, {"text": "clinical trials", "type": "ResearchActivity"}, {"text": "non - inferiority", "type": "Finding"}, {"text": "medical journals", "type": "IntellectualProduct"}, {"text": "JAMA Internal Medicine", "type": "IntellectualProduct"}, {"text": "Archives Internal Medicine", "type": "IntellectualProduct"}, {"text": "PLOS Medicine", "type": "IntellectualProduct"}, {"text": "Annals of Internal Medicine", "type": "IntellectualProduct"}, {"text": "BMJ", "type": "IntellectualProduct"}, {"text": "JAMA", "type": "IntellectualProduct"}, {"text": "Lancet and New England Journal of Medicine", "type": "IntellectualProduct"}]}

Example input:
Sentence:  of the authors has a financial or proprietary interest in any material or method mentioned .

Example answer:
{"entities": [{"text": "authors", "type": "ProfessionalOrOccupationalGroup"}, {"text": "financial or proprietary interest", "type": "BiologicFunction"}, {"text": "method", "type": "IntellectualProduct"}]}

Example input:
Sentence: The paper contributes with a new open ontology describing both low - level and high - level context information , as well as their relationships .

Example answer:
{"entities": []}

Example input:
Sentence: A chemical free nano - delivery system using SC - CO2 has been revealed for storage and controlled release of bioactive ingredients .

Example answer:
{"entities": [{"text": "CO2", "type": "Chemical"}]}

Example input:
Sentence: 0 open source license and is available at the project website : https : / / www . assembla .

Example answer:
{"entities": []}

Example input:
Sentence: The work cannot be changed in any way or used commercially without permission from the journal .

Example answer:
{"entities": []}

Example input:
Sentence: For the first time , a pericardiocentesis approach with a medial - to - lateral needle trajectory and real - time , in - plane , needle visualization was performed in a tamponade patient population .This is an open - access article distributed under the terms of the Creative Commons Attribution - Non Commercial - No Derivatives License 4 . 0 ( CCBY - NC - ND ) , where it is permissible to download and share the work provided it is properly cited .

Example answer:
{"entities": [{"text": "pericardiocentesis", "type": "HealthCareActivity"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "medial - to - lateral", "type": "SpatialConcept"}, {"text": "needle", "type": "MedicalDevice"}, {"text": "tamponade", "type": "BiologicFunction"}]}

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
Sentence: This is an open access article distributed under the terms of the Creative Commons Non - Commercial , No Derivatives ( CC BY - NC - ND ) license .

## Item MedMentions:test:3395
Example input:
Sentence: Here , the miR - CATCH technique was applied to the mesothelin ( MSLN ) gene and coupled with next generation sequencing ( NGS ) , to identify miRNAs that regulate MSLN mRNA and that may be responsible for its increased protein levels found in malignant pleural mesothelioma ( MPM ) .

Example answer:
{"entities": [{"text": "mesothelin ( MSLN ) gene", "type": "AnatomicalStructure"}, {"text": "next generation sequencing", "type": "ResearchActivity"}, {"text": "NGS", "type": "ResearchActivity"}, {"text": "miRNAs", "type": "Chemical"}, {"text": "regulate", "type": "BiologicFunction"}, {"text": "MSLN mRNA", "type": "AnatomicalStructure"}, {"text": "protein levels", "type": "Finding"}, {"text": "malignant pleural mesothelioma", "type": "BiologicFunction"}, {"text": "MPM", "type": "BiologicFunction"}]}

Example input:
Sentence: Finally , we investigated the evolutionary patterns and location of positive selection sites ( PSSs ) in the MyD88 gene from Arthropoda , Mollusca and Insecta using PAML software with the maximum likelihood method .

Example answer:
{"entities": [{"text": "evolutionary patterns", "type": "BiologicFunction"}, {"text": "positive selection sites", "type": "AnatomicalStructure"}, {"text": "PSSs", "type": "AnatomicalStructure"}, {"text": "MyD88 gene", "type": "AnatomicalStructure"}, {"text": "Arthropoda", "type": "Eukaryote"}, {"text": "Mollusca", "type": "Eukaryote"}, {"text": "Insecta", "type": "Eukaryote"}, {"text": "PAML software", "type": "IntellectualProduct"}, {"text": "maximum likelihood method", "type": "IntellectualProduct"}]}

Example input:
Sentence: Notable nucleotide differences exist between genomes in the right half , including the presence of mycobacteriophage mobile element 1 ( MPME1 ) in Jane .

Example answer:
{"entities": [{"text": "nucleotide", "type": "Chemical"}, {"text": "genomes", "type": "AnatomicalStructure"}, {"text": "mycobacteriophage", "type": "Virus"}, {"text": "mobile element 1", "type": "Chemical"}]}

Example input:
Sentence: All exons and exon - intron boundaries of PRIM1 gene were sequenced in 192 Han Chinese women with non - syndromic POI .

Example answer:
{"entities": [{"text": "exons", "type": "Chemical"}, {"text": "exon - intron boundaries", "type": "Chemical"}, {"text": "PRIM1 gene", "type": "AnatomicalStructure"}, {"text": "sequenced", "type": "HealthCareActivity"}, {"text": "women", "type": "PopulationGroup"}, {"text": "POI", "type": "BiologicFunction"}]}

Example input:
Sentence: The following single nucleotide polymorphisms ( SNPs ) were genotyped ; C1236 T , C3435 T , G2677 T / A in MDR1 gene and A6986 G in CYP3A5 gene , using PCR - RFLP method and validated by direct gene sequencing .

Example answer:
{"entities": [{"text": "single nucleotide polymorphisms", "type": "SpatialConcept"}, {"text": "SNPs", "type": "SpatialConcept"}, {"text": "genotyped", "type": "HealthCareActivity"}, {"text": "C1236 T", "type": "SpatialConcept"}, {"text": "C3435 T", "type": "SpatialConcept"}, {"text": "G2677 T", "type": "SpatialConcept"}, {"text": "A", "type": "SpatialConcept"}, {"text": "MDR1 gene", "type": "AnatomicalStructure"}, {"text": "A6986 G", "type": "SpatialConcept"}, {"text": "CYP3A5 gene", "type": "AnatomicalStructure"}, {"text": "PCR - RFLP method", "type": "HealthCareActivity"}, {"text": "gene sequencing", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here we report that AMS and MS188 target the CYP703A2 gene , which is involved in sporopollenin biosynthesis .

Example answer:
{"entities": [{"text": "AMS", "type": "Chemical"}, {"text": "MS188", "type": "Chemical"}, {"text": "CYP703A2 gene", "type": "AnatomicalStructure"}, {"text": "sporopollenin biosynthesis", "type": "BiologicFunction"}]}

Example input:
Sentence: Matrix metalloproteinase - 9 Gene - 1562C > T Gene Polymorphism and Coronary Artery Disease in the Chinese Han Population : A Meta - Analysis of 5468 Subjects Multiple studies indicate that the matrix metalloproteinase - 9 ( MMP - 9 ) - 1562C > T gene polymorphism may be associated with an increased risk of coronary artery disease ( CAD ) in the Chinese Han population .

Example answer:
{"entities": [{"text": "Matrix metalloproteinase - 9 Gene - 1562C > T Gene", "type": "AnatomicalStructure"}, {"text": "Coronary Artery Disease", "type": "BiologicFunction"}, {"text": "Meta - Analysis", "type": "ResearchActivity"}, {"text": "Subjects", "type": "PopulationGroup"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "matrix metalloproteinase - 9 ( MMP - 9 ) - 1562C > T gene", "type": "AnatomicalStructure"}, {"text": "increased risk", "type": "Finding"}, {"text": "coronary artery disease", "type": "BiologicFunction"}, {"text": "CAD", "type": "BiologicFunction"}]}

Example input:
Sentence: Several critical hub genes were disclosed , such as RPS2 , MMP1 , MMP11 and FAM83H .

Example answer:
{"entities": [{"text": "hub genes", "type": "AnatomicalStructure"}, {"text": "RPS2", "type": "AnatomicalStructure"}, {"text": "MMP1", "type": "AnatomicalStructure"}, {"text": "MMP11", "type": "AnatomicalStructure"}, {"text": "FAM83H", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Molecular phenotyping identified loss of mismatch - repair protein immunostaining for PMS2 , microsatellite instability , a lack of MLH1 promoter methylation , and lack of BRAF mutation suggestive of Lynch syndrome .

Example answer:
{"entities": [{"text": "Molecular phenotyping", "type": "HealthCareActivity"}, {"text": "mismatch - repair protein", "type": "Chemical"}, {"text": "immunostaining", "type": "HealthCareActivity"}, {"text": "PMS2", "type": "Chemical"}, {"text": "microsatellite instability", "type": "BiologicFunction"}, {"text": "BRAF mutation", "type": "BiologicFunction"}, {"text": "Lynch syndrome", "type": "BiologicFunction"}]}

Example input:
Sentence: The MLH1 - PMS1 gene combination isolated from the homozygous clinical isolate conferred a mutator phenotype when expressed in the S288c laboratory background .

Example answer:
{"entities": [{"text": "MLH1", "type": "AnatomicalStructure"}, {"text": "PMS1 gene", "type": "AnatomicalStructure"}, {"text": "isolate", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "laboratory", "type": "Organization"}]}

Input:
Sentence: Here we analyzed the MLH1 and PMS1 genes across 1010 S .

## Item MedMentions:test:3465
Example input:
Sentence: 4 % had moderate burden and 37 % had favorable burden .

Example answer:
{"entities": []}

Example input:
Sentence: A health education intervention study was conducted from November 2012 to January 2014 in a rural area of Kuppam , Andhra Pradesh , South India among the people aged 15 years and above .

Example answer:
{"entities": [{"text": "intervention study", "type": "IntellectualProduct"}, {"text": "South India", "type": "SpatialConcept"}, {"text": "people", "type": "PopulationGroup"}]}

Example input:
Sentence: The influx of injuries and illnesses in rural areas where OCRs are often held can impose a large burden on emergency medical services ( EMS ) and local EDs .

Example answer:
{"entities": [{"text": "injuries", "type": "InjuryOrPoisoning"}, {"text": "illnesses", "type": "Finding"}, {"text": "emergency medical services", "type": "HealthCareActivity"}, {"text": "EMS", "type": "HealthCareActivity"}]}

Example input:
Sentence: This study was conducted to assess the burden of cervical cancer in India and review the performance characteristics of available cervical cancer screening tools , so as to provide evidence -based recommendations for application of most practically suited screening test to be used in resource -poor field settings .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "cervical cancer", "type": "BiologicFunction"}, {"text": "India", "type": "SpatialConcept"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "screening test", "type": "HealthCareActivity"}]}

Example input:
Sentence: Burden of cervical cancer and role of screening in India Cervical cancer is a major cause of cancer mortality in women and more than a quarter of its global burden is contributed by developing countries .

Example answer:
{"entities": [{"text": "cervical cancer", "type": "BiologicFunction"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "India", "type": "SpatialConcept"}, {"text": "Cervical cancer", "type": "BiologicFunction"}, {"text": "women", "type": "PopulationGroup"}]}

Example input:
Sentence: The burden of mental disorders in EMR increased from 1726 DALYs /100 , 000 in 1990 to 1912 DALYs /100 , 000 in 2013 ( 10 . 8 % increase ) .

Example answer:
{"entities": [{"text": "mental disorders", "type": "BiologicFunction"}, {"text": "EMR", "type": "SpatialConcept"}]}

Example input:
Sentence: Long - term follow - up of this cohort for the incident cardiovascular disease will shed light on the true cardiovascular risk in a typical South Indian rural farming population .

Example answer:
{"entities": [{"text": "Long - term follow - up", "type": "HealthCareActivity"}, {"text": "cardiovascular disease", "type": "BiologicFunction"}, {"text": "South Indian", "type": "SpatialConcept"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: The greatest burden appears for the most part in infants ( < 1 year ) in Bulgaria , Hungary , Latvia , Romania , and Serbia , but not in the other participating countries where the burden may have shifted to older children , though surveillance of adults may be inappropriate .

Example answer:
{"entities": [{"text": "Bulgaria", "type": "SpatialConcept"}, {"text": "Hungary", "type": "SpatialConcept"}, {"text": "Latvia", "type": "SpatialConcept"}, {"text": "Romania", "type": "SpatialConcept"}, {"text": "Serbia", "type": "SpatialConcept"}, {"text": "countries", "type": "SpatialConcept"}]}

Example input:
Sentence: Rural patients had significantly higher transfer rates ( OR : 2 . 73 , p < 0 . 05 ) .

Example answer:
{"entities": [{"text": "Rural", "type": "Finding"}, {"text": "transfer", "type": "HealthCareActivity"}]}

Example input:
Sentence: The Nallampatti noncommunicable disease study To assess the prevalence of noncommunicable diseases in a true rural farming population in South India and compare the data with the landmark contemporary Indian Council of Medical Research - India Diabetes ( ICMR - INDIAB ) study .

Example answer:
{"entities": [{"text": "Nallampatti", "type": "SpatialConcept"}, {"text": "noncommunicable disease", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "noncommunicable diseases", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}, {"text": "South India", "type": "SpatialConcept"}, {"text": "landmark contemporary Indian Council of Medical Research - India Diabetes ( ICMR - INDIAB ) study", "type": "IntellectualProduct"}]}

Input:
Sentence: The burden was higher than the comparable ICMR - INDIAB study in rural Tamil Nadu .

## Item MedMentions:test:3177
Example input:
Sentence: 34 healthy volunteers ( HV ) , 30 IBS with diarrhea ( IBS - D ) , 16 IBS with constipation ( IBS - C ) , and 11 IBS with mixed bowel habit ( IBS - M ) underwent whole - gut transit and small and large bowel volumes assessment with MRI scans from t = 0 to t = 360 min .

Example answer:
{"entities": [{"text": "healthy volunteers", "type": "PopulationGroup"}, {"text": "HV", "type": "PopulationGroup"}, {"text": "IBS with diarrhea", "type": "BiologicFunction"}, {"text": "IBS - D", "type": "BiologicFunction"}, {"text": "IBS with constipation", "type": "BiologicFunction"}, {"text": "IBS - C", "type": "BiologicFunction"}, {"text": "IBS with mixed bowel habit", "type": "BiologicFunction"}, {"text": "IBS - M", "type": "BiologicFunction"}, {"text": "whole - gut", "type": "AnatomicalStructure"}, {"text": "small", "type": "AnatomicalStructure"}, {"text": "large bowel", "type": "AnatomicalStructure"}, {"text": "assessment", "type": "HealthCareActivity"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "scans", "type": "HealthCareActivity"}]}

Example input:
Sentence: The distribution - adding mid - high dose range was also important for stool frequency and urgency / tenesmus .

Example answer:
{"entities": [{"text": "distribution - adding", "type": "IntellectualProduct"}, {"text": "mid", "type": "SpatialConcept"}, {"text": "stool frequency", "type": "Finding"}, {"text": "urgency", "type": "BiologicFunction"}, {"text": "tenesmus", "type": "Finding"}]}

Example input:
Sentence: ATV trough levels at week 9 were higher in controls ( median 438 ng / mL ) than in the switch arm ( median 124 ng / mL ) ( p = 0 . 003 ) , as was total bilirubin at week 48 ( median 38 μmol / L and 28 μmol / L , respectively ; p = 0 .

Example answer:
{"entities": [{"text": "ATV", "type": "Chemical"}, {"text": "median", "type": "SpatialConcept"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Lubiprostone significantly softened the stool and increased the frequency of BM from median of 2 to 4 times per week .

Example answer:
{"entities": [{"text": "Lubiprostone", "type": "Chemical"}, {"text": "stool", "type": "BodySubstance"}, {"text": "frequency of BM", "type": "Finding"}]}

Example input:
Sentence: Parameter - adding also indicated the low - mid dose region was significantly correlated with stool frequency and proctitis .

Example answer:
{"entities": [{"text": "Parameter - adding", "type": "IntellectualProduct"}, {"text": "mid", "type": "SpatialConcept"}, {"text": "region", "type": "SpatialConcept"}, {"text": "stool frequency", "type": "Finding"}, {"text": "proctitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Median ( interquartile range ) : fasting small bowel water content in IBS - nonC was 21 ( 10 - 42 ) , significantly less than HV at 44 ml ( 15 - 70 ) , P < 0 .

Example answer:
{"entities": [{"text": "fasting", "type": "Finding"}, {"text": "small bowel", "type": "AnatomicalStructure"}, {"text": "water", "type": "BodySubstance"}, {"text": "IBS - nonC", "type": "BiologicFunction"}, {"text": "HV", "type": "PopulationGroup"}]}

Example input:
Sentence: Moreover , the ability for mucin secretion and the expression of membrane water channel ( aquaporine 8 , AQP8 ) were increased significantly in the Lop + Urd treated group compared with Lop + Vehicle treated group .

Example answer:
{"entities": [{"text": "mucin", "type": "Chemical"}, {"text": "secretion", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "membrane water channel", "type": "Chemical"}, {"text": "aquaporine 8", "type": "Chemical"}, {"text": "AQP8", "type": "Chemical"}, {"text": "Lop", "type": "Chemical"}, {"text": "Urd", "type": "Chemical"}, {"text": "treated", "type": "Finding"}, {"text": "Vehicle", "type": "Chemical"}]}

Example input:
Sentence: The constipation phenotypes and their related mechanisms were investigated in the transverse colons of SD rats with loperamide ( Lop ) - induced constipation after treatment with 100 mg / kg of Urd .

Example answer:
{"entities": [{"text": "constipation", "type": "Finding"}, {"text": "transverse colons", "type": "AnatomicalStructure"}, {"text": "SD rats", "type": "Eukaryote"}, {"text": "loperamide", "type": "Chemical"}, {"text": "Lop", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "Urd", "type": "Chemical"}]}

Example input:
Sentence: The thickness of the mucosa layer , muscle and flat luminal surface , as well as the number of goblet cells , paneth cells and lipid droplets were enhanced in the Lop + Urd treated group .

Example answer:
{"entities": [{"text": "mucosa layer", "type": "AnatomicalStructure"}, {"text": "muscle", "type": "AnatomicalStructure"}, {"text": "flat luminal surface", "type": "SpatialConcept"}, {"text": "goblet cells", "type": "AnatomicalStructure"}, {"text": "paneth cells", "type": "AnatomicalStructure"}, {"text": "lipid droplets", "type": "AnatomicalStructure"}, {"text": "Lop", "type": "Chemical"}, {"text": "Urd", "type": "Chemical"}, {"text": "treated", "type": "Finding"}]}

Example input:
Sentence: The results of the present study provide the first strong evidence that Urd can be considered an important candidate for improving chronic constipation induced by Lop treatment in animal models .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "Urd", "type": "Chemical"}, {"text": "constipation", "type": "Finding"}, {"text": "Lop", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "animal models", "type": "Eukaryote"}]}

Input:
Sentence: The number , weight and water contents of stools were significantly higher in the Lop + Urd treated group than the Lop + Vehicle treated group , while food intake and water consumption of the same group were maintained at a constant level .

## Item MedMentions:test:3413
Example input:
Sentence: In addition , the CR rate was significantly increased in patients carrying one or two ERCC1 - 118 C alleles ( C / C or C / T genotype ) compared with patients lacking the C allele ( T / T genotype ) .

Example answer:
{"entities": [{"text": "CR", "type": "Finding"}, {"text": "ERCC1 - 118", "type": "AnatomicalStructure"}, {"text": "alleles", "type": "AnatomicalStructure"}, {"text": "C", "type": "Chemical"}, {"text": "T", "type": "Chemical"}, {"text": "allele", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 95 - 0 . 99 ) and OS ( HR = 0 . 94 ; 95 % CI 0 . 91 - 0 . 97 ) as well as from the first to the third chemotherapy cycle for OS ( HR = 0 .

Example answer:
{"entities": [{"text": "chemotherapy cycle", "type": "HealthCareActivity"}]}

Example input:
Sentence: We retrospectively compared the outcomes of allo - SCT for patients with CNS involvement and for patients without CNS involvement ( CNS - ) using a database in Japan .

Example answer:
{"entities": [{"text": "allo - SCT", "type": "HealthCareActivity"}, {"text": "CNS involvement", "type": "Finding"}, {"text": "CNS -", "type": "Finding"}, {"text": "database", "type": "IntellectualProduct"}, {"text": "Japan", "type": "SpatialConcept"}]}

Example input:
Sentence: It was found that the short - term therapeutic efficacy ( CR rate ) was higher in the group of patients carrying the homozygous mutation of XRCC1 - 399 ( A / A genotype ) than in the group of patients without the XRCC1 - 399 mutation ( G / G genotype ) .

Example answer:
{"entities": [{"text": "CR", "type": "Finding"}, {"text": "homozygous mutation", "type": "BiologicFunction"}, {"text": "XRCC1 - 399", "type": "AnatomicalStructure"}, {"text": "A", "type": "Chemical"}, {"text": "mutation", "type": "BiologicFunction"}, {"text": "G", "type": "Chemical"}]}

Example input:
Sentence: Composite Cortical State ( CCS ) and Composite Cortical State distance ( CCSd ) , two new modifications of CS , along with CS and CI were evaluated on electroencephalographic ( EEG ) data of healthy control individuals undergoing N2O inhalation up to equilibrated peak gas concentrations of 20 , 40 or 60 % N2O / O2 .

Example answer:
{"entities": [{"text": "Composite Cortical State", "type": "IntellectualProduct"}, {"text": "CCS", "type": "IntellectualProduct"}, {"text": "Composite Cortical State distance", "type": "IntellectualProduct"}, {"text": "CCSd", "type": "IntellectualProduct"}, {"text": "modifications", "type": "Finding"}, {"text": "CS", "type": "IntellectualProduct"}, {"text": "CI", "type": "IntellectualProduct"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "electroencephalographic", "type": "HealthCareActivity"}, {"text": "EEG", "type": "HealthCareActivity"}, {"text": "N2O", "type": "Chemical"}, {"text": "inhalation", "type": "BiologicFunction"}, {"text": "O2", "type": "Chemical"}]}

Example input:
Sentence: The median overall survival ( OS ) for CY + patients was 12 months .

Example answer:
{"entities": []}

Example input:
Sentence: In CD and UC patients , V was 49 % and 52 % higher than in AS , respectively , and CL was 47 % and 60 % higher than in AS , respectively .

Example answer:
{"entities": [{"text": "CD", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}, {"text": "AS", "type": "BiologicFunction"}]}

Example input:
Sentence: The OS rates at 1 and 3 years were significantly higher for CY - patients ( 75 . 1 % and 35 .

Example answer:
{"entities": [{"text": "CY -", "type": "Finding"}]}

Example input:
Sentence: Compared to cognitively preserved ( CP ) , CI patients had higher T2 WM lesion volume ( LV ) , lower NBV and GMV , and more severe diffusivity abnormalities in WM lesions , cortex , and NAWM .

Example answer:
{"entities": [{"text": "CI", "type": "BiologicFunction"}, {"text": "abnormalities", "type": "AnatomicalStructure"}, {"text": "WM lesions", "type": "Finding"}, {"text": "cortex", "type": "AnatomicalStructure"}, {"text": "NAWM", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Patients who achieved cCR had significantly longer OS in comparison with patients achieving clinical partial response ( cPR ) and clinical stable disease ( cSD ) .

Example answer:
{"entities": [{"text": "achieved", "type": "Finding"}, {"text": "cCR", "type": "Finding"}, {"text": "clinical partial response", "type": "Finding"}, {"text": "cPR", "type": "Finding"}, {"text": "clinical stable disease", "type": "Finding"}, {"text": "cSD", "type": "Finding"}]}

Input:
Sentence: CNS + patients who achieved CR showed OS comparable to that of CNS - patients .

## Item MedMentions:test:3593
Example input:
Sentence: 97 to 1 . 8±1 .

Example answer:
{"entities": []}

Example input:
Sentence: 95±1 .

Example answer:
{"entities": []}

Example input:
Sentence: 05 , 99 . 0 / 0 . 8 / 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 95 , P = 0 . 001 and 89 vs .

Example answer:
{"entities": []}

Example input:
Sentence: 93 , 0 . 82 , 0 . 74 , 0 . 51 and 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 0 and 97 .

Example answer:
{"entities": []}

Example input:
Sentence: 98 , 1 . 45 - 54 . 19 and 2 . 00 - 50 .

Example answer:
{"entities": []}

Example input:
Sentence: 98 - 1 . 02 ; P = .96 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 97 , p = 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 94 - 0 . 99 and OR = 0 .

Example answer:
{"entities": []}

Input:
Sentence: 95 - 0 . 98 and OR = 0 .

## Item MedMentions:test:3317
Example input:
Sentence: A retrospective study involving 7 centers over a 5 - year period beginning in 2011 was performed .

Example answer:
{"entities": [{"text": "retrospective study", "type": "ResearchActivity"}]}

Example input:
Sentence: The analysis included 21 patients ( 12 women , 9 men ; mean age 36 years ) .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "women", "type": "PopulationGroup"}, {"text": "men", "type": "PopulationGroup"}, {"text": "mean age 36 years", "type": "Finding"}]}

Example input:
Sentence: Thus , we aim to determine the potential of the recently introduced third - generation dual - source CT ( DSCT ) for CTA in a ' real - life ' clinical setting .

Example answer:
{"entities": [{"text": "third - generation dual - source CT", "type": "HealthCareActivity"}, {"text": "DSCT", "type": "HealthCareActivity"}, {"text": "CTA", "type": "HealthCareActivity"}]}

Example input:
Sentence: Ninety four patients who underwent triphasic abdominal CT ( liver mass protocol , n = 47 ; pancreas mass protocol , n = 47 ) between August 2014 and May 2015 were retrospectively reviewed .

Example answer:
{"entities": [{"text": "triphasic abdominal CT", "type": "HealthCareActivity"}, {"text": "retrospectively reviewed", "type": "IntellectualProduct"}]}

Example input:
Sentence: Ten retrospective patients ' computed tomography datasets were considered .

Example answer:
{"entities": [{"text": "computed tomography", "type": "HealthCareActivity"}, {"text": "datasets", "type": "IntellectualProduct"}]}

Example input:
Sentence: The CTTs of the STC patients were significantly longer than the healthy controls .

Example answer:
{"entities": [{"text": "CTTs", "type": "HealthCareActivity"}, {"text": "STC", "type": "Finding"}]}

Example input:
Sentence: In this prospective study , 40 patients with a BMI < 28 . 0 kg / m ( 2 ) underwent CTA examination for breast reconstruction and were randomly assigned into two groups ( n = 20 for each group ) as follows : Group A was submitted to dual - energy spectral CT and iodixanol ( 270 mg I / mL ) and Group B was submitted to conventional high iodine contrast agent iohexol ( 350 mg I / mL ) .

Example answer:
{"entities": [{"text": "prospective study", "type": "ResearchActivity"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "CTA", "type": "HealthCareActivity"}, {"text": "breast reconstruction", "type": "Finding"}, {"text": "dual - energy spectral CT", "type": "HealthCareActivity"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "iodine contrast agent", "type": "Chemical"}, {"text": "iohexol", "type": "Chemical"}]}

Example input:
Sentence: From March 2003 to February 2012 , a total of 2024 CTO patients treated with either medical therapy alone or revascularization were enrolled in the study .

Example answer:
{"entities": [{"text": "CTO", "type": "BiologicFunction"}, {"text": "medical therapy", "type": "HealthCareActivity"}, {"text": "revascularization", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Cohort comprised CT - DXA pairs within a 6 - month period performed for any indication on 326 consecutive adults , aged 62 . 4 ± 12 .

Example answer:
{"entities": [{"text": "Cohort", "type": "PopulationGroup"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "DXA", "type": "HealthCareActivity"}]}

Example input:
Sentence: This retrospective study was performed with ( 99m ) Tc - DMSA SPECT images of 316 patients ( age range , 1 - 26 years ) .

Example answer:
{"entities": [{"text": "retrospective study", "type": "ResearchActivity"}, {"text": "( 99m ) Tc - DMSA", "type": "Chemical"}, {"text": "SPECT", "type": "HealthCareActivity"}, {"text": "images", "type": "IntellectualProduct"}]}

Input:
Sentence: Two hundred and sixty - eight consecutive patients ( age : 67 ± 10 years ; BMI : 27 ± 5 kg / m² ; 61 % male ) undergoing clinically indicated CTA with DSCT were included in the retrospective single - center analysis .

## Item MedMentions:test:3322
Example input:
Sentence: Clinical - microbiological research of action ozone therapy and light - emetting diode radiation of red range ( 630 nanometers ) on microflora of the hole extracted toothatalveolitis and limited osteomyelitis of jaws As a result of cliniko - microbiological research the data testifying to substantial improvement of efficiency of antimicrobictherape at inclusion in a complex of medical actions at alveolitis and the limited osteomyelitis of a jow ozone therapy in a combination with a light - emettinf diode irradiation of the hole extracted teeth red ( 630 nanometers ) are obtained by light .

Example answer:
{"entities": [{"text": "Clinical - microbiological research", "type": "ResearchActivity"}, {"text": "action ozone therapy", "type": "HealthCareActivity"}, {"text": "hole extracted", "type": "HealthCareActivity"}, {"text": "toothatalveolitis", "type": "BiologicFunction"}, {"text": "limited osteomyelitis", "type": "BiologicFunction"}, {"text": "jaws", "type": "AnatomicalStructure"}, {"text": "cliniko - microbiological research", "type": "ResearchActivity"}, {"text": "antimicrobictherape", "type": "HealthCareActivity"}]}

Example input:
Sentence: As for purified PPO , superior to thermal treatment , less heat was needed to inactivate the PPO with ultrasonic treatment .

Example answer:
{"entities": [{"text": "PPO", "type": "Chemical"}, {"text": "thermal treatment", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Administration of AO restored both the cytosolic and mitochondrial oxidative stress by normalizing nicotinamide adenine dinucleotide phosphate ( NADPH ) generating enzymes .

Example answer:
{"entities": [{"text": "Administration", "type": "HealthCareActivity"}, {"text": "AO", "type": "Chemical"}, {"text": "cytosolic", "type": "AnatomicalStructure"}, {"text": "mitochondrial", "type": "AnatomicalStructure"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "normalizing", "type": "ResearchActivity"}, {"text": "nicotinamide adenine dinucleotide phosphate", "type": "Chemical"}, {"text": "NADPH", "type": "Chemical"}, {"text": "enzymes", "type": "Chemical"}]}

Example input:
Sentence: After MWCNT production and functionalization to produce MWCNT - GO , ultrasonic irradiation was employed to precipitate nHAp onto the MWCNT - GO scaffolds ( at 1 - 3 wt % ) .

Example answer:
{"entities": [{"text": "MWCNT", "type": "Chemical"}, {"text": "GO", "type": "Chemical"}, {"text": "employed", "type": "Finding"}, {"text": "nHAp", "type": "Chemical"}]}

Example input:
Sentence: To improve the poor outcomes , ozonation had been applied with or without ultrasound .

Example answer:
{"entities": [{"text": "poor outcomes", "type": "Finding"}]}

Example input:
Sentence: UV - visible and Resonance Raman spectroelectrochemical studies suggest the formation of a high valent iron - oxo species as the catalytic intermediate .

Example answer:
{"entities": [{"text": "Resonance Raman spectroelectrochemical studies", "type": "HealthCareActivity"}]}

Example input:
Sentence: Effective degradation of methylisothiazolone biocide using ozone : Kinetics , mechanisms , and decreases in toxicity Methylisothiazolone ( MIT ) is a common biocide that is widely used in water - desalination reverse - osmosis processes .

Example answer:
{"entities": [{"text": "methylisothiazolone", "type": "Chemical"}, {"text": "biocide", "type": "Chemical"}, {"text": "ozone", "type": "Chemical"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "Methylisothiazolone", "type": "Chemical"}, {"text": "MIT", "type": "Chemical"}]}

Example input:
Sentence: The kinetics and mechanisms involved in the degradation of MIT during ozonation were investigated in this study .

Example answer:
{"entities": [{"text": "MIT", "type": "Chemical"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Ultrasonic irradiation process was carried out in a batch reactor for aqueous amoxicillin solutions at three different frequencies ( 575 , 861 and 1141kHz ) .

Example answer:
{"entities": [{"text": "amoxicillin", "type": "Chemical"}]}

Example input:
Sentence: Medium - high frequency ultrasound and ozone based advanced oxidation for amoxicillin removal in water In this study , treatment of an antibiotic compound amoxicillin by medium - high frequency ultrasonic irradiation and / or ozonation has been studied .

Example answer:
{"entities": [{"text": "ozone", "type": "Chemical"}, {"text": "oxidation", "type": "BiologicFunction"}, {"text": "amoxicillin", "type": "Chemical"}, {"text": "water", "type": "Chemical"}, {"text": "antibiotic", "type": "Chemical"}]}

Input:
Sentence: Furthermore , the intermediate compounds , after the incomplete oxidation mechanisms , has been analyzed to reveal the possible degradation pathways of amoxicillin through ultrasonic irradiation and ozonation applications .

## Item MedMentions:test:2896
Example input:
Sentence: Our previous work demonstrates that oncogenic KIAA0101 transcript variant ( tv ) 1 promotes HCC development and might be a HCC therapeutic target .

Example answer:
{"entities": [{"text": "oncogenic", "type": "AnatomicalStructure"}, {"text": "KIAA0101", "type": "AnatomicalStructure"}, {"text": "transcript variant", "type": "AnatomicalStructure"}, {"text": "( tv ) 1", "type": "AnatomicalStructure"}, {"text": "HCC", "type": "BiologicFunction"}]}

Example input:
Sentence: The results also showed that HCV has a GC ( guanine - cytosine ) abundant genome structure and prefers codons with GC for translation .

Example answer:
{"entities": [{"text": "HCV", "type": "Virus"}, {"text": "GC", "type": "Chemical"}, {"text": "guanine - cytosine", "type": "Chemical"}, {"text": "genome structure", "type": "AnatomicalStructure"}, {"text": "codons", "type": "SpatialConcept"}]}

Example input:
Sentence: To this end , we analyzed stool samples from six stage 4 - HCV patients and eight healthy individuals by high - throughput 16S rRNA gene sequencing using Illumina MiSeq .

Example answer:
{"entities": [{"text": "stool samples", "type": "BodySubstance"}, {"text": "HCV", "type": "Virus"}, {"text": "healthy individuals", "type": "PopulationGroup"}, {"text": "16S rRNA gene sequencing", "type": "HealthCareActivity"}, {"text": "Illumina MiSeq", "type": "MedicalDevice"}]}

Example input:
Sentence: The genotype distribution of IL - 28B rs12979860CC , - CT , and - TT was 29 , 41 , and 30 % , respectively , and the distribution for rs8099917TT , - TG , and - GG was 63 , 31 , and 5 % , respectively .

Example answer:
{"entities": [{"text": "IL - 28B rs12979860CC", "type": "AnatomicalStructure"}, {"text": "CT", "type": "AnatomicalStructure"}, {"text": "TT", "type": "AnatomicalStructure"}, {"text": "rs8099917TT", "type": "AnatomicalStructure"}, {"text": "TG", "type": "AnatomicalStructure"}, {"text": "GG", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The study cohort included 73 chronic HCV patients treated with concomitant administration of CIGB - 230 and nonpegylated IFN - α plus ribavirin ( non - pegIFN - α / R ) antiviral therapy .

Example answer:
{"entities": [{"text": "HCV", "type": "Virus"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "CIGB - 230", "type": "Chemical"}, {"text": "nonpegylated IFN - α", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "non - pegIFN - α", "type": "Chemical"}, {"text": "R", "type": "Chemical"}, {"text": "antiviral therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the present study , chronically infected HCV patients with known viremia were subjected to HCV genotyping .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "chronically infected", "type": "BiologicFunction"}, {"text": "HCV", "type": "Virus"}, {"text": "viremia", "type": "BiologicFunction"}]}

Example input:
Sentence: G G homozygotic and G A heterozygotic status in TLR9 2848 G > A SNP decreased significantly the occurrence of HCMV infection ( OR 0 .

Example answer:
{"entities": [{"text": "G", "type": "Chemical"}, {"text": "A", "type": "Chemical"}, {"text": "TLR9", "type": "AnatomicalStructure"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "HCMV infection", "type": "BiologicFunction"}]}

Example input:
Sentence: It is concluded that in Cuban HCV - infected patients , the responder homogeneous variant rs8099917TT is the most frequent genotype .

Example answer:
{"entities": [{"text": "Cuban", "type": "PopulationGroup"}, {"text": "HCV", "type": "Virus"}, {"text": "infected", "type": "Finding"}, {"text": "responder", "type": "Finding"}, {"text": "variant", "type": "AnatomicalStructure"}, {"text": "rs8099917TT", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The simultaneous genotyping of 2 IL - 28B SNPs could improve the prediction of SVR contributing to better therapeutic decisions and treatment management .

Example answer:
{"entities": [{"text": "genotyping", "type": "HealthCareActivity"}, {"text": "IL - 28B", "type": "AnatomicalStructure"}, {"text": "SNPs", "type": "SpatialConcept"}, {"text": "improve", "type": "Finding"}, {"text": "SVR", "type": "Finding"}, {"text": "decisions", "type": "BiologicFunction"}, {"text": "treatment management", "type": "HealthCareActivity"}]}

Example input:
Sentence: Assessment of IL - 28 : rs12979860 and rs8099917 Polymorphisms in a Cohort of Cuban Chronic HCV Genotype 1b Patients Hepatitis C virus ( HCV ) is a significant global public health problem with > 185 million infections worldwide .

Example answer:
{"entities": [{"text": "Assessment", "type": "HealthCareActivity"}, {"text": "IL - 28", "type": "AnatomicalStructure"}, {"text": "rs8099917", "type": "AnatomicalStructure"}, {"text": "Polymorphisms", "type": "BiologicFunction"}, {"text": "Cohort", "type": "PopulationGroup"}, {"text": "Cuban", "type": "PopulationGroup"}, {"text": "Chronic HCV Genotype 1b", "type": "BiologicFunction"}, {"text": "Hepatitis C virus", "type": "Virus"}, {"text": "HCV", "type": "Virus"}, {"text": "infections", "type": "BiologicFunction"}, {"text": "worldwide", "type": "PopulationGroup"}]}

Input:
Sentence: A series of genome - wide association studies ( GWAS ) has identified IL - 28B polymorphisms as a predictor of sustained virologic response ( SVR ) , as well as spontaneous clearance in chronic HCV genotype 1 patients .

## Item MedMentions:test:3447
Example input:
Sentence: However , increases in C - telopeptide of type II collagen ( CTX - II ) , associated with collagen type II breakdown , were significantly greater in the placebo group ( 1 . 32 ± 1 . 10 ng / mL ) than in either of the groups that received the corticosteroid injection within the first several days after injury ( group 1 : 0 .

Example answer:
{"entities": [{"text": "C - telopeptide of type II collagen", "type": "Chemical"}, {"text": "CTX - II", "type": "Chemical"}, {"text": "collagen type II", "type": "Chemical"}, {"text": "breakdown", "type": "BiologicFunction"}, {"text": "placebo", "type": "Chemical"}, {"text": "corticosteroid", "type": "Chemical"}, {"text": "injection", "type": "HealthCareActivity"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "group 1", "type": "IntellectualProduct"}]}

Example input:
Sentence: Within group comparison : The percentage of CD4 + in the two groups was significantly reduced at 24 hours post - operation ( T2 ) compared with the percentage before surgery , whereas the percentage of CD8 + was higher at T2 .

Example answer:
{"entities": [{"text": "percentage of CD4 +", "type": "HealthCareActivity"}, {"text": "percentage", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}, {"text": "percentage of CD8 + was higher", "type": "Finding"}]}

Example input:
Sentence: Furthermore , in the ninth month , graft fixation groups had the lowest chondrocyte densities , the highest degree of inflammation , the highest degree of foreign body reaction , and the highest butyl cyanoacrylate density .

Example answer:
{"entities": [{"text": "graft", "type": "HealthCareActivity"}, {"text": "fixation", "type": "HealthCareActivity"}, {"text": "chondrocyte", "type": "AnatomicalStructure"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "foreign body reaction", "type": "BiologicFunction"}, {"text": "butyl cyanoacrylate", "type": "Chemical"}]}

Example input:
Sentence: Estimated glomerular filtration rate ( eGFR ) decreased in the control arm ( p = 0 . 007 ) , but did not change in the switch arm .

Example answer:
{"entities": [{"text": "Estimated glomerular filtration rate", "type": "HealthCareActivity"}, {"text": "eGFR", "type": "HealthCareActivity"}, {"text": "not change", "type": "Finding"}]}

Example input:
Sentence: A total of 73 patients from the GDFR group were compared with 72 patients from the control group .

Example answer:
{"entities": [{"text": "GDFR", "type": "HealthCareActivity"}]}

Example input:
Sentence: Postoperative estimated glomerular filtration rate ( eGFR ) at 3 to 36 months were obtained from 90 . 2 % of patients , and of those , 34 .

Example answer:
{"entities": [{"text": "estimated glomerular filtration rate", "type": "HealthCareActivity"}, {"text": "eGFR", "type": "HealthCareActivity"}]}

Example input:
Sentence: High - risk patients undergoing brain surgery were randomly assigned to a usual care group ( control group ) or a GDFR group .

Example answer:
{"entities": [{"text": "brain surgery", "type": "HealthCareActivity"}, {"text": "GDFR", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of our study was to evaluate the effect of an intraoperative goal - directed fluid restriction ( GDFR ) strategy on the postoperative outcome of high - risk patients undergoing brain surgery .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "goal - directed fluid restriction", "type": "HealthCareActivity"}, {"text": "GDFR", "type": "HealthCareActivity"}, {"text": "brain surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: In high - risk patients undergoing brain surgery , intraoperative GDFR was associated with a reduction in ICU length of stay and costs , and a decrease in postoperative morbidity .

Example answer:
{"entities": [{"text": "brain surgery", "type": "HealthCareActivity"}, {"text": "GDFR", "type": "HealthCareActivity"}, {"text": "ICU", "type": "Organization"}]}

Example input:
Sentence: In the GDFR group , ( 1 ) fluid maintenance was restricted to 3 ml / kg / h of a crystalloid solution and ( 2 ) colloid boluses were allowed only in case of hypotension associated with a low cardiac index and a high stroke volume variation .

Example answer:
{"entities": [{"text": "GDFR", "type": "HealthCareActivity"}, {"text": "fluid", "type": "BodySubstance"}, {"text": "crystalloid solution", "type": "Chemical"}, {"text": "colloid boluses", "type": "Chemical"}, {"text": "hypotension", "type": "Finding"}, {"text": "cardiac index", "type": "Finding"}, {"text": "high stroke volume", "type": "Finding"}]}

Input:
Sentence: During surgery , the GDFR group received less colloid ( 1 . 9 ± 1 .

## Item MedMentions:test:3409
Example input:
Sentence: Results showed that E . coli strains segregated mainly in phylogenetic group B1 , 52 . 8 % in diarrheic herds and 52 . 9 % in healthy herds .

Example answer:
{"entities": [{"text": "E . coli", "type": "Bacterium"}, {"text": "diarrheic", "type": "Finding"}]}

Example input:
Sentence: Diversity of Microbial Carbohydrate - Active enZYmes ( CAZYmes ) Associated with Freshwater and Soil Samples from Caatinga Biome Semi - arid and arid areas occupy about 33 % of terrestrial ecosystems .

Example answer:
{"entities": [{"text": "Carbohydrate - Active enZYmes", "type": "Chemical"}, {"text": "CAZYmes", "type": "Chemical"}]}

Example input:
Sentence: Our data support the pivotal role of the most characterized fibrolytic bacteria ( Prevotella , Ruminocccus and Fibrobacter ) , and highlight a substantial , although most probably underestimated , contribution of fungi and ciliate protozoa to polysaccharide degradation .

Example answer:
{"entities": [{"text": "fibrolytic bacteria", "type": "Bacterium"}, {"text": "Prevotella", "type": "Bacterium"}, {"text": "Ruminocccus", "type": "Bacterium"}, {"text": "Fibrobacter", "type": "Bacterium"}, {"text": "fungi", "type": "Eukaryote"}, {"text": "ciliate protozoa", "type": "Eukaryote"}, {"text": "polysaccharide", "type": "Chemical"}]}

Example input:
Sentence: According to amplicon sequencing of bacterial 16S rRNA genes and mcrA genes , the microbial communities of both microbiomes were similar though Methanoculleus was more and Methanobacterium was less abundant in the coumarin - adapted than in the non - adapted microbiome .

Example answer:
{"entities": [{"text": "16S rRNA genes", "type": "AnatomicalStructure"}, {"text": "mcrA genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The present study used RNA - sequencing to reveal both the expression of genes encoding carbohydrate - active enzymes ( CAZymes ) by the rumen microbiota of a lactating dairy cow and the microorganisms forming the fiber -degrading community .

Example answer:
{"entities": [{"text": "RNA - sequencing", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "carbohydrate - active enzymes", "type": "Chemical"}, {"text": "CAZymes", "type": "Chemical"}, {"text": "rumen", "type": "AnatomicalStructure"}, {"text": "microbiota", "type": "Eukaryote"}, {"text": "fiber", "type": "Eukaryote"}]}

Example input:
Sentence: Glycoside hydrolases and glycosyltransferases were the most abundant CAZYme families , with glycoside hydrolases more dominant in soil ( ∼44 % ) and glycosyltransferases more abundant in freshwater ( ∼50 % ) .

Example answer:
{"entities": [{"text": "Glycoside hydrolases", "type": "Chemical"}, {"text": "glycosyltransferases", "type": "Chemical"}, {"text": "CAZYme", "type": "Chemical"}, {"text": "glycoside hydrolases", "type": "Chemical"}]}

Example input:
Sentence: Functional analysis identified 12 , 237 CAZymes , accounting for 1 % of the transcripts .

Example answer:
{"entities": [{"text": "Functional analysis", "type": "ResearchActivity"}, {"text": "CAZymes", "type": "Chemical"}, {"text": "transcripts", "type": "Chemical"}]}

Example input:
Sentence: The CAZyme profile was dominated by families GH94 ( cellobiose - phosphorylase ) , GH13 ( amylase ) , GH43 and GH10 ( hemicellulases ) , GH9 and GH48 ( cellulases ) , PL11 ( pectinase ) as well as GH2 and GH3 ( oligosaccharidases ) .

Example answer:
{"entities": [{"text": "CAZyme", "type": "Chemical"}, {"text": "GH94", "type": "Chemical"}, {"text": "cellobiose - phosphorylase", "type": "Chemical"}, {"text": "GH13", "type": "Chemical"}, {"text": "amylase", "type": "Chemical"}, {"text": "GH43", "type": "Chemical"}, {"text": "GH10", "type": "Chemical"}, {"text": "hemicellulases", "type": "Chemical"}, {"text": "GH9", "type": "Chemical"}, {"text": "GH48", "type": "Chemical"}, {"text": "cellulases", "type": "Chemical"}, {"text": "PL11", "type": "Chemical"}, {"text": "pectinase", "type": "Chemical"}, {"text": "GH2", "type": "Chemical"}, {"text": "GH3", "type": "Chemical"}, {"text": "oligosaccharidases", "type": "Chemical"}]}

Example input:
Sentence: Here , using fluorescence microscopy and chromosome conformation capture in conjunction with deep sequencing ( Hi - C ) , we show that in Caulobacter crescentus , both transcription rate and transcript length , independent of concurrent translation , drive the formation of domain boundaries .

Example answer:
{"entities": [{"text": "fluorescence microscopy", "type": "HealthCareActivity"}, {"text": "deep sequencing", "type": "ResearchActivity"}, {"text": "Caulobacter crescentus", "type": "Bacterium"}, {"text": "transcription", "type": "BiologicFunction"}, {"text": "transcript", "type": "Chemical"}, {"text": "translation", "type": "BiologicFunction"}, {"text": "domain boundaries", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The main taxa associated with the CAZYme sequences were Planctomycetia ( relative abundance in soil , 29 % ) and Alphaproteobacteria ( relative abundance in freshwater , 27 % ) .

Example answer:
{"entities": [{"text": "CAZYme sequences", "type": "SpatialConcept"}, {"text": "Planctomycetia", "type": "Bacterium"}, {"text": "Alphaproteobacteria", "type": "Bacterium"}]}

Input:
Sentence: Moreover , an important part of the fibrolytic bacterial community remains to be characterized since one third of the CAZyme transcripts originated from distantly related strains .

## Item MedMentions:test:3182
Example input:
Sentence: They became anuric and presented with progressive dyspnea , tachypnea , and tachycardia , requiring hemodialysis for a period of 1 month in one case .

Example answer:
{"entities": [{"text": "anuric", "type": "BiologicFunction"}, {"text": "progressive dyspnea", "type": "Finding"}, {"text": "tachypnea", "type": "Finding"}, {"text": "tachycardia", "type": "BiologicFunction"}, {"text": "hemodialysis", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here , we report a case of a 41 - year - old female patient who had a late diagnosis of 2 , 8 - dihydroxyadenine nephropathy -induced end - stage renal disease , made on the native nephrectomy that accompanied the renal transplant , and who had a timely intervention that prevented recurrence in the graft .

Example answer:
{"entities": [{"text": "2 , 8 - dihydroxyadenine", "type": "Chemical"}, {"text": "nephropathy", "type": "BiologicFunction"}, {"text": "end - stage renal disease", "type": "BiologicFunction"}, {"text": "nephrectomy", "type": "HealthCareActivity"}, {"text": "renal transplant", "type": "HealthCareActivity"}, {"text": "recurrence", "type": "BiologicFunction"}, {"text": "graft", "type": "HealthCareActivity"}]}

Example input:
Sentence: We present a 79 - year -old male who was admitted due to acute renal failure with a history of radical radiotherapy for prostate adenocarcinoma 13 years ago .

Example answer:
{"entities": [{"text": "admitted", "type": "HealthCareActivity"}, {"text": "acute renal failure", "type": "BiologicFunction"}, {"text": "history", "type": "Finding"}, {"text": "radical radiotherapy", "type": "HealthCareActivity"}, {"text": "prostate adenocarcinoma", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , a 48 year old man presented with a large intra - abdominal mass preoperatively diagnosed as a case of right renal cell carcinoma and radical nephrectomy was performed .

Example answer:
{"entities": [{"text": "man", "type": "PopulationGroup"}, {"text": "intra - abdominal mass", "type": "Finding"}, {"text": "preoperatively diagnosed", "type": "Finding"}, {"text": "radical nephrectomy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Urinary stones were present in 5 patients , pelvi - ureteric junction obstruction in 3 , horseshoe kidny in 3 , ectopic kidney in 2 and upper urinary tract carcinoma in one case .

Example answer:
{"entities": [{"text": "Urinary stones", "type": "BodySubstance"}, {"text": "pelvi - ureteric junction obstruction", "type": "BiologicFunction"}, {"text": "horseshoe kidny", "type": "AnatomicalStructure"}, {"text": "ectopic kidney", "type": "AnatomicalStructure"}]}

Example input:
Sentence: A 23 years old male patient admitted with h / o dysuria , pyuria and loss of appetite since 3 months .

Example answer:
{"entities": [{"text": "h / o dysuria", "type": "Finding"}, {"text": "pyuria", "type": "Finding"}, {"text": "loss of appetite", "type": "BiologicFunction"}]}

Example input:
Sentence: A 36 - year -old Sri Lankan woman presented with generalized body swelling and foamy urine of 2 weeks ' duration .

Example answer:
{"entities": [{"text": "Sri Lankan", "type": "PopulationGroup"}, {"text": "woman", "type": "PopulationGroup"}, {"text": "body swelling", "type": "Finding"}]}

Example input:
Sentence: Following surgical resection , the two patients were diagnosed with urachal adenocarcinoma ( mixed type ) and urachal mucinous adenocarcinoma , respectively , based on the histopathological examination .

Example answer:
{"entities": [{"text": "surgical resection", "type": "HealthCareActivity"}, {"text": "diagnosed", "type": "Finding"}, {"text": "urachal adenocarcinoma", "type": "BiologicFunction"}, {"text": "urachal mucinous adenocarcinoma", "type": "BiologicFunction"}, {"text": "examination", "type": "HealthCareActivity"}]}

Example input:
Sentence: Namely , a 69 years - old man with a warthy lesions of the foreskin and the glans misunderstood for a condylomata that at histological and immunohistochemical analysis showed a bladder urothelial carcinoma ; and a 71 years - old man with reddish skin lesion of the glans , a previous history of bladder and urethral carcinoma and histological pagetoid spread of urothelial cancer to the glans .

Example answer:
{"entities": [{"text": "lesions", "type": "Finding"}, {"text": "condylomata", "type": "BiologicFunction"}, {"text": "histological", "type": "HealthCareActivity"}, {"text": "bladder urothelial carcinoma", "type": "BiologicFunction"}, {"text": "history of bladder", "type": "Finding"}, {"text": "urethral carcinoma", "type": "BiologicFunction"}, {"text": "histological pagetoid spread", "type": "Finding"}, {"text": "urothelial cancer", "type": "BiologicFunction"}, {"text": "to the glans", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Urachal carcinoma : Report of two cases and review of the literature Urachal carcinoma is a rare tumor that most commonly occurs in ovaries and less often in the adnexal region and urinary system .

Example answer:
{"entities": [{"text": "Urachal carcinoma", "type": "BiologicFunction"}, {"text": "Report", "type": "IntellectualProduct"}, {"text": "literature", "type": "IntellectualProduct"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "ovaries", "type": "AnatomicalStructure"}, {"text": "adnexal", "type": "AnatomicalStructure"}, {"text": "region", "type": "SpatialConcept"}, {"text": "urinary system", "type": "BodySystem"}]}

Input:
Sentence: We herein present two cases of urachal carcinoma : One case was a 32 - year - old male patient who presented with painless hematuria with blood clots for 1 month , whereas the other case was a 50 - year - old woman who presented with gross hematuria with mild dysuria , urgency and frequent urination for 1 year .

## Item MedMentions:test:3149
Example input:
Sentence: In patients with 0 < BI < 3 , ( 36 RR , 36 reaction - free ) , higher antibody levels to PGL - I ( p = 0 . 014 ) and to LID - 1 ( p = 0 . 035 ) were seen in RR while difference in anti - ND - O - LID positivity was borderline ( p = 0 . 052 ) .

Example answer:
{"entities": [{"text": "RR", "type": "BiologicFunction"}, {"text": "reaction - free", "type": "Finding"}, {"text": "antibody", "type": "Chemical"}, {"text": "PGL - I", "type": "Chemical"}, {"text": "LID - 1", "type": "Chemical"}, {"text": "anti - ND - O - LID", "type": "Finding"}, {"text": "positivity", "type": "Finding"}]}

Example input:
Sentence: D2 receptors were particularly responsible for microglial RAS inhibition in basal culture conditions .

Example answer:
{"entities": [{"text": "D2 receptors", "type": "Chemical"}, {"text": "microglial", "type": "AnatomicalStructure"}, {"text": "RAS", "type": "BodySystem"}, {"text": "basal", "type": "SpatialConcept"}, {"text": "culture", "type": "HealthCareActivity"}]}

Example input:
Sentence: Systematic variation of the benzenesulfonamide part of the GluN2A selective NMDA receptor antagonist TCN - 201 GluN2A subunit containing N - methyl - d - aspartate receptors ( NMDARs ) are highly involved in various physiological processes in the central nervous system , but also in some diseases , such as anxiety , depression and schizophrenia .

Example answer:
{"entities": [{"text": "benzenesulfonamide", "type": "Chemical"}, {"text": "GluN2A selective NMDA receptor", "type": "Chemical"}, {"text": "antagonist", "type": "Chemical"}, {"text": "TCN - 201", "type": "Chemical"}, {"text": "GluN2A subunit", "type": "Chemical"}, {"text": "N - methyl - d - aspartate receptors", "type": "Chemical"}, {"text": "NMDARs", "type": "Chemical"}, {"text": "physiological processes", "type": "BiologicFunction"}, {"text": "central nervous system", "type": "BodySystem"}, {"text": "diseases", "type": "BiologicFunction"}, {"text": "anxiety", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "schizophrenia", "type": "BiologicFunction"}]}

Example input:
Sentence: At baseline higher anti - PGL - I , anti - LID - 1 and anti - ND - O - LID seropositivity rates were seen in patients who developed ENL and RR compared to reaction - free patients ( p < 0 . 0001 ) .

Example answer:
{"entities": [{"text": "anti - PGL - I", "type": "Finding"}, {"text": "anti - LID - 1", "type": "Finding"}, {"text": "anti - ND - O - LID", "type": "Finding"}, {"text": "ENL", "type": "BiologicFunction"}, {"text": "RR", "type": "BiologicFunction"}, {"text": "reaction - free", "type": "Finding"}]}

Example input:
Sentence: The partial agonistic effect of aripiprazole on D2 receptors may have augmented the mesolimbic dopaminergic pathway , which was suppressed by risperidone , causing spontaneous ejaculations in this patient .

Example answer:
{"entities": [{"text": "agonistic", "type": "Chemical"}, {"text": "aripiprazole", "type": "Chemical"}, {"text": "D2 receptors", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "risperidone", "type": "Chemical"}, {"text": "ejaculations", "type": "BiologicFunction"}]}

Example input:
Sentence: Ocular hypotensive effect of the novel EP3 / FP agonist ONO - 9054 versus Xalatan : results of a 28 - day , double - masked , randomised study ONO - 9054 is being developed for the reduction of intraocular pressure ( IOP ) in patients with ocular hypertension ( OHT ) and open - angle glaucoma ( OAG ) .

Example answer:
{"entities": [{"text": "Ocular hypotensive", "type": "BiologicFunction"}, {"text": "EP3", "type": "Chemical"}, {"text": "FP", "type": "Chemical"}, {"text": "agonist", "type": "Chemical"}, {"text": "ONO - 9054", "type": "Chemical"}, {"text": "Xalatan", "type": "Chemical"}, {"text": "double - masked", "type": "ResearchActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "intraocular pressure", "type": "BiologicFunction"}, {"text": "IOP", "type": "BiologicFunction"}, {"text": "ocular hypertension", "type": "BiologicFunction"}, {"text": "OHT", "type": "BiologicFunction"}, {"text": "open - angle glaucoma", "type": "BiologicFunction"}, {"text": "OAG", "type": "BiologicFunction"}]}

Example input:
Sentence: Infusion of a small amount of a D1 or D2 antagonist led to early saccades in the self - timed , but not the triggered MS tasks , while infusion of DA agonists produced no consistent effect .

Example answer:
{"entities": [{"text": "Infusion", "type": "HealthCareActivity"}, {"text": "D1", "type": "Chemical"}, {"text": "D2", "type": "Chemical"}, {"text": "antagonist", "type": "Chemical"}, {"text": "saccades", "type": "BiologicFunction"}, {"text": "MS tasks", "type": "HealthCareActivity"}, {"text": "infusion", "type": "HealthCareActivity"}, {"text": "DA agonists", "type": "Chemical"}]}

Example input:
Sentence: Using the activatory Gq - coupled human M3 muscarinic receptor ( hM3Dq ) , we found that chemogenetic stimulation of dSPNs mimicked , while stimulation of iSPNs abolished the therapeutic action of L - DOPA in PD mice .

Example answer:
{"entities": [{"text": "activatory Gq - coupled human M3 muscarinic receptor", "type": "Chemical"}, {"text": "hM3Dq", "type": "Chemical"}, {"text": "chemogenetic stimulation", "type": "BiologicFunction"}, {"text": "dSPNs", "type": "AnatomicalStructure"}, {"text": "stimulation", "type": "BiologicFunction"}, {"text": "iSPNs", "type": "AnatomicalStructure"}, {"text": "therapeutic action", "type": "BiologicFunction"}, {"text": "L - DOPA", "type": "Chemical"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: In the absence of L - DOPA , only chemogenetic stimulation of dSPNs mediated through the Gs - coupled modified rat muscarinic M3 receptor ( rM3Ds ) induced appreciable dyskinesia in PD mice .

Example answer:
{"entities": [{"text": "L - DOPA", "type": "Chemical"}, {"text": "chemogenetic stimulation", "type": "BiologicFunction"}, {"text": "dSPNs", "type": "AnatomicalStructure"}, {"text": "Gs - coupled modified rat muscarinic M3 receptor", "type": "Chemical"}, {"text": "rM3Ds", "type": "Chemical"}, {"text": "dyskinesia", "type": "BiologicFunction"}, {"text": "PD", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: In LID mice , hM3Dq stimulation of dSPNs exacerbated dyskinetic responses to L - DOPA , while stimulation of iSPNs inhibited these responses .

Example answer:
{"entities": [{"text": "LID", "type": "Finding"}, {"text": "mice", "type": "Eukaryote"}, {"text": "hM3Dq", "type": "Chemical"}, {"text": "stimulation", "type": "BiologicFunction"}, {"text": "dSPNs", "type": "AnatomicalStructure"}, {"text": "L - DOPA", "type": "Chemical"}, {"text": "iSPNs", "type": "AnatomicalStructure"}]}

Input:
Sentence: Combining D2 receptor agonist treatment with rM3Ds - dSPN stimulation reproduced all symptoms of LID .

## Item MedMentions:test:3313
Example input:
Sentence: We found 19 patients who already diagnosed and treated for TB infection .

Example answer:
{"entities": [{"text": "diagnosed", "type": "Finding"}, {"text": "TB infection", "type": "BiologicFunction"}]}

Example input:
Sentence: The diagnosis of TB was supported by microbiological evidence of alcohol acid - fast Bacilli present in sputum smear ( 21 % ) , histological diagnosis ( 31 . 6 % ) , polymerase chain reaction ( 21 % ) , and imaging in ( 26 . 3 % ) .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "microbiological", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "alcohol acid - fast Bacilli present in sputum smear", "type": "Finding"}, {"text": "polymerase chain reaction", "type": "ResearchActivity"}, {"text": "imaging in", "type": "HealthCareActivity"}]}

Example input:
Sentence: Currently , only 62 % of incident tuberculosis ( TB ) cases are reported to the national programme in Pakistan .

Example answer:
{"entities": [{"text": "tuberculosis", "type": "BiologicFunction"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "reported", "type": "HealthCareActivity"}, {"text": "national programme", "type": "HealthCareActivity"}, {"text": "Pakistan", "type": "SpatialConcept"}]}

Example input:
Sentence: All patients were HIV - infected and diagnosed with TB , either bacteriologically or clinically , and followed until a determination of TB treatment outcome .

Example answer:
{"entities": [{"text": "HIV - infected", "type": "BiologicFunction"}, {"text": "diagnosed", "type": "Finding"}, {"text": "TB", "type": "BiologicFunction"}]}

Example input:
Sentence: The overall yield of all forms TB patients among investigated was 22 .

Example answer:
{"entities": [{"text": "TB", "type": "BiologicFunction"}]}

Example input:
Sentence: Among children ( N = 455 ) evaluated for presumptive TB , 70 . 3 % ( 320 / 455 ) had Xpert and 62 .

Example answer:
{"entities": [{"text": "Xpert", "type": "HealthCareActivity"}]}

Example input:
Sentence: A total of 783043 contacts were screened for tuberculosis : 23741 ( 3 . 0 % ) presumptive TB patients were identified of whom , 4710 ( 19 . 8 % ) all forms and 4084 ( 17 . 2 % ) bacteriologically confirmed TB patients were detected .

Example answer:
{"entities": [{"text": "screened", "type": "HealthCareActivity"}, {"text": "tuberculosis", "type": "BiologicFunction"}, {"text": "TB", "type": "BiologicFunction"}, {"text": "bacteriologically", "type": "Finding"}, {"text": "detected", "type": "HealthCareActivity"}]}

Example input:
Sentence: Extrapulmonary TB was the major presentation ( 57 . 9 % ) mainly tuberculous lymphadenitis ( 26 . 3 % ) .

Example answer:
{"entities": [{"text": "Extrapulmonary TB", "type": "BiologicFunction"}, {"text": "tuberculous lymphadenitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Overall , most patients ( 76 % ) received at least one TB test ; 45 % were positive .

Example answer:
{"entities": [{"text": "TB test", "type": "HealthCareActivity"}, {"text": "positive", "type": "Finding"}]}

Example input:
Sentence: 8 % and all forms TB patients by 7 .

Example answer:
{"entities": [{"text": "TB", "type": "BiologicFunction"}]}

Input:
Sentence: 34 . 5 % ( 157 / 455 ) were diagnosed with TB : 80 . 3 % ( 126 / 157 ) pulmonary TB , 13 . 4 % ( 21 / 157 ) bacteriologically confirmed , 53 . 5 % ( 84 / 157 ) HIV positive , and 48 . 4 % ( 76 / 157 ) inpatients .

## Item MedMentions:test:3366
Example input:
Sentence: The early activation of STAT1α ( detected by phospho - serine727 and phoshpo - tyrosine701 ) by IFNγ and the late activation of STAT1α by LPS were not affected in the presence of cPLA2α inhibitors , indicating that STAT1α is not under cPLA2α regulation .

Example answer:
{"entities": [{"text": "STAT1α", "type": "Chemical"}, {"text": "phospho - serine727", "type": "Chemical"}, {"text": "phoshpo - tyrosine701", "type": "Chemical"}, {"text": "IFNγ", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "cPLA2α", "type": "Chemical"}, {"text": "inhibitors", "type": "Chemical"}, {"text": "regulation", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , we describe the validation of the silencing of CD40 expression with a specific siRNA in ApoE ( - / - ) mouse aortas , and its systemic effects on splenic lymphocytic subpopulations as well as on the infiltration of aortic intima by F4 / 80 ( + ) , galectin - 3 ( + ) macrophages or by NF - κB ( + ) cells .

Example answer:
{"entities": [{"text": "validation", "type": "ResearchActivity"}, {"text": "silencing", "type": "BiologicFunction"}, {"text": "CD40", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "siRNA", "type": "Chemical"}, {"text": "ApoE ( - / - )", "type": "AnatomicalStructure"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "aortas", "type": "AnatomicalStructure"}, {"text": "splenic", "type": "AnatomicalStructure"}, {"text": "lymphocytic subpopulations", "type": "IntellectualProduct"}, {"text": "infiltration", "type": "BiologicFunction"}, {"text": "aortic intima", "type": "AnatomicalStructure"}, {"text": "F4 / 80 ( + )", "type": "AnatomicalStructure"}, {"text": "galectin - 3 ( + ) macrophages", "type": "AnatomicalStructure"}, {"text": "NF - κB ( + ) cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The activation of cPLA2α is mediated by ERK activity .

Example answer:
{"entities": [{"text": "cPLA2α", "type": "Chemical"}, {"text": "ERK activity", "type": "BiologicFunction"}]}

Example input:
Sentence: The activation of cPLA2 by LPS was mediated by both adaptor proteins downstream to LPS receptor ; TRIF and MyD88 , while the activation of cPLA2α by IFNγ was mediated by the secreted TNF - α at 4 h .

Example answer:
{"entities": [{"text": "cPLA2", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "adaptor proteins", "type": "Chemical"}, {"text": "downstream", "type": "SpatialConcept"}, {"text": "LPS receptor", "type": "Chemical"}, {"text": "TRIF", "type": "BiologicFunction"}, {"text": "MyD88", "type": "BiologicFunction"}, {"text": "cPLA2α", "type": "Chemical"}, {"text": "IFNγ", "type": "Chemical"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "TNF - α", "type": "Chemical"}]}

Example input:
Sentence: Addition of LPS to microglia caused an immediate activation of cPLA2α detected by its phosphorylated form , while addition of IFNγ induced cPLA2α activation at a later time scale ( 4 h ) .

Example answer:
{"entities": [{"text": "LPS", "type": "Chemical"}, {"text": "microglia", "type": "AnatomicalStructure"}, {"text": "cPLA2α", "type": "Chemical"}, {"text": "phosphorylated", "type": "BiologicFunction"}, {"text": "IFNγ", "type": "Chemical"}]}

Example input:
Sentence: Cumulatively , our results indicate that cPLA2α may serve as a pivotal amplifier of the inflammatory response in the CNS .

Example answer:
{"entities": [{"text": "cPLA2α", "type": "Chemical"}, {"text": "inflammatory response", "type": "BiologicFunction"}, {"text": "CNS", "type": "BodySystem"}]}

Example input:
Sentence: Regulatory role of cytosolic phospholipase A2 alpha in the induction of CD40 in microglia The aberrant expression of CD40 , a co - stimulatory receptor found on the antigen - presenting cells , is involved in the pathogenesis of various degenerative diseases .

Example answer:
{"entities": [{"text": "Regulatory role", "type": "BiologicFunction"}, {"text": "cytosolic phospholipase A2 alpha", "type": "Chemical"}, {"text": "CD40", "type": "Chemical"}, {"text": "microglia", "type": "AnatomicalStructure"}, {"text": "receptor", "type": "Chemical"}, {"text": "antigen - presenting cells", "type": "AnatomicalStructure"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "degenerative diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Our previous study demonstrated that the reduction of cytosolic phospholipase A2 alpha ( cPLA2α ) protein overexpression and activation in the spinal cord of a mouse model of ALS , hmSOD1 G93A , inhibited CD40 upregulation in microglia .

Example answer:
{"entities": [{"text": "cytosolic phospholipase A2 alpha", "type": "Chemical"}, {"text": "cPLA2α", "type": "Chemical"}, {"text": "protein overexpression", "type": "BiologicFunction"}, {"text": "spinal cord", "type": "AnatomicalStructure"}, {"text": "mouse model", "type": "BiologicFunction"}, {"text": "ALS", "type": "BiologicFunction"}, {"text": "hmSOD1 G93A", "type": "Chemical"}, {"text": "inhibited", "type": "BiologicFunction"}, {"text": "CD40", "type": "Chemical"}, {"text": "upregulation", "type": "BiologicFunction"}, {"text": "microglia", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Cultures of primary mouse microglia or BV - 2 microglia cell line exposed to lipopolysaccharide ( LPS ) or interferon gamma ( IFNγ ) for different periods of time , in order to study the role of cPLA2α in the events leading to CD40 protein induction .

Example answer:
{"entities": [{"text": "Cultures", "type": "HealthCareActivity"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "microglia", "type": "AnatomicalStructure"}, {"text": "BV - 2 microglia cell line", "type": "AnatomicalStructure"}, {"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "interferon gamma", "type": "Chemical"}, {"text": "IFNγ", "type": "Chemical"}, {"text": "cPLA2α", "type": "Chemical"}, {"text": "CD40", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}]}

Example input:
Sentence: Our results show for the first time that cPLA2 upregulates CD40 protein expression induced by either LPS or IFNγ , and this regulatory effect is mediated via the activation of NOX2 - NADPH oxidase and NF - κB .

Example answer:
{"entities": [{"text": "cPLA2", "type": "Chemical"}, {"text": "upregulates", "type": "BiologicFunction"}, {"text": "CD40", "type": "Chemical"}, {"text": "protein expression", "type": "BiologicFunction"}, {"text": "LPS", "type": "Chemical"}, {"text": "IFNγ", "type": "Chemical"}, {"text": "regulatory", "type": "BiologicFunction"}, {"text": "activation", "type": "BiologicFunction"}, {"text": "NOX2 - NADPH oxidase", "type": "Chemical"}, {"text": "NF - κB", "type": "Chemical"}]}

Input:
Sentence: The present study was designed to determine whether cPLA2α has a direct , participatory role in the molecular events leading to CD40 induction .

## Item MedMentions:test:3172
Example input:
Sentence: Total phenols , flavonoids , tannins and antioxidant activity were evaluated using the Folin ciocalteux , Aluminum trichloride , vanillin and scavenging activity on 22 - diphenyl - 1 - picrylhydrazyl ( DPPH ) radical methods , respectively .

Example answer:
{"entities": [{"text": "phenols", "type": "Chemical"}, {"text": "flavonoids", "type": "Chemical"}, {"text": "tannins", "type": "Chemical"}, {"text": "antioxidant activity", "type": "BiologicFunction"}, {"text": "Folin ciocalteux", "type": "Chemical"}, {"text": "Aluminum trichloride", "type": "Chemical"}, {"text": "vanillin", "type": "Chemical"}, {"text": "scavenging activity", "type": "BiologicFunction"}, {"text": "22 - diphenyl - 1 - picrylhydrazyl", "type": "Chemical"}, {"text": "DPPH", "type": "Chemical"}, {"text": "radical", "type": "Chemical"}]}

Example input:
Sentence: To overcome this problem , we developed a new structure - based computational method , Cross - React , to predict cross - reactivity between allergenic proteins available in the Structural Database of Allergens ( SDAP ) .

Example answer:
{"entities": [{"text": "structure - based computational method", "type": "IntellectualProduct"}, {"text": "Cross - React", "type": "IntellectualProduct"}, {"text": "cross - reactivity", "type": "BiologicFunction"}, {"text": "proteins", "type": "Chemical"}, {"text": "Structural Database of Allergens", "type": "IntellectualProduct"}, {"text": "SDAP", "type": "IntellectualProduct"}]}

Example input:
Sentence: Cross - reactivity features of deoxynivalenol ( DON ) - targeted immunoaffinity columns aiming to achieve simultaneous analysis of DON and major conjugates in cereal samples Immunoafﬁnity columns ( IACs ) are a well - established tool in the determination of regulated mycotoxins in food and feed commodities .

Example answer:
{"entities": [{"text": "Cross - reactivity", "type": "BiologicFunction"}, {"text": "deoxynivalenol", "type": "Chemical"}, {"text": "DON", "type": "Chemical"}, {"text": "immunoaffinity", "type": "HealthCareActivity"}, {"text": "analysis", "type": "HealthCareActivity"}, {"text": "conjugates", "type": "Chemical"}, {"text": "cereal", "type": "Food"}, {"text": "Immunoafﬁnity", "type": "HealthCareActivity"}, {"text": "mycotoxins", "type": "Chemical"}, {"text": "food", "type": "Food"}, {"text": "feed commodities", "type": "Food"}]}

Example input:
Sentence: Cross - reactivity was evidenced by identification of a common * 0401 - restricted epitope for RV - A16 and RV - A39 by tetramer - guided epitope mapping and the ability for RV - A16 -specific Th1 cells to proliferate in response to their RV - A39 peptide counterpart .

Example answer:
{"entities": [{"text": "restricted epitope", "type": "Chemical"}, {"text": "RV - A16", "type": "Virus"}, {"text": "RV - A39", "type": "Virus"}, {"text": "tetramer - guided epitope mapping", "type": "HealthCareActivity"}, {"text": "Th1 cells", "type": "AnatomicalStructure"}, {"text": "peptide", "type": "Chemical"}]}

Example input:
Sentence: Based on these findings , we suggest that Cross - React can be used as a predictive tool to assess protein allergenicity and cross - reactivity . : Cross - React is available at : http : / / curie .

Example answer:
{"entities": [{"text": "Cross - React", "type": "IntellectualProduct"}, {"text": "predictive tool", "type": "IntellectualProduct"}, {"text": "cross - reactivity", "type": "BiologicFunction"}]}

Example input:
Sentence: Taking into consideration the levels of DON conjugates existing in real samples , the cross - reactivity of one DON - IAC allows a quantitative analysis of all of these analytes .

Example answer:
{"entities": [{"text": "DON", "type": "Chemical"}, {"text": "conjugates", "type": "Chemical"}, {"text": "cross - reactivity", "type": "BiologicFunction"}, {"text": "analytes", "type": "Chemical"}]}

Example input:
Sentence: The results showed that adenosine , histamine , N - acetylhistamine , N ( α ) - γ - glutamylhistamine , malate and xanthine are important indices for anaphylactoid reactions .

Example answer:
{"entities": [{"text": "adenosine", "type": "Chemical"}, {"text": "histamine", "type": "Chemical"}, {"text": "N - acetylhistamine", "type": "Chemical"}, {"text": "N ( α ) - γ - glutamylhistamine", "type": "Chemical"}, {"text": "malate", "type": "Chemical"}, {"text": "xanthine", "type": "Chemical"}, {"text": "anaphylactoid reactions", "type": "BiologicFunction"}]}

Example input:
Sentence: We have carried out a detailed characterisation of the cross - reactivity of the four main IACs brands against DON and its conjugates as well as an assessment of the competition among the analytes .

Example answer:
{"entities": [{"text": "cross - reactivity", "type": "BiologicFunction"}, {"text": "DON", "type": "Chemical"}, {"text": "conjugates", "type": "Chemical"}, {"text": "analytes", "type": "Chemical"}]}

Example input:
Sentence: This study compared the novel dual EP3 / FP agonist ONO - 9054 with the FP agonist Xalatan .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "EP3", "type": "Chemical"}, {"text": "FP", "type": "Chemical"}, {"text": "agonist", "type": "Chemical"}, {"text": "ONO - 9054", "type": "Chemical"}, {"text": "Xalatan", "type": "Chemical"}]}

Example input:
Sentence: We applied the Cross - React method to a diverse set of seven allergens , and successfully identified several cross - reactive allergens with high to moderate sequence identity which have also been experimentally shown to cross - react .

Example answer:
{"entities": [{"text": "Cross - React", "type": "IntellectualProduct"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "allergens", "type": "Chemical"}, {"text": "cross - reactive", "type": "BiologicFunction"}, {"text": "sequence", "type": "SpatialConcept"}]}

Input:
Sentence: Cross - reactivity was evaluated for norfentanyl , acetyl fentanyl , 4 - anilino - N - phenethylpiperidine , beta - hydroxythiofentanyl , butyryl fentanyl and furanyl fentanyl .

## Item MedMentions:test:3389
Example input:
Sentence: To achieve this aim , we assessed the rotifer total protein content , the rotifers fatty acid profile , zebrafish larval growth performance , the expression of key growth , and endocrine appetite regulation genes .

Example answer:
{"entities": [{"text": "rotifer", "type": "Eukaryote"}, {"text": "total protein content", "type": "HealthCareActivity"}, {"text": "rotifers", "type": "Eukaryote"}, {"text": "fatty acid profile", "type": "HealthCareActivity"}, {"text": "zebrafish", "type": "Eukaryote"}, {"text": "larval", "type": "Eukaryote"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "endocrine", "type": "BodySystem"}, {"text": "appetite regulation", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Pre - treating wildtype larvae with the liver - sparing Lxr agonist hyodeoxycholic acid also delayed the rate of intestinal lipid transport in larvae .

Example answer:
{"entities": [{"text": "wildtype", "type": "AnatomicalStructure"}, {"text": "larvae", "type": "Eukaryote"}, {"text": "Lxr", "type": "Chemical"}, {"text": "agonist", "type": "Chemical"}, {"text": "hyodeoxycholic acid", "type": "Chemical"}, {"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "lipid", "type": "Chemical"}, {"text": "transport", "type": "BiologicFunction"}]}

Example input:
Sentence: dusmeti larvae is selective in enabling ingestion of bacteria only above 2 .

Example answer:
{"entities": [{"text": "dusmeti", "type": "Eukaryote"}, {"text": "larvae", "type": "Eukaryote"}, {"text": "ingestion", "type": "BiologicFunction"}, {"text": "bacteria", "type": "Bacterium"}]}

Example input:
Sentence: This anatomical location brings additional functional challenges ( swallowing , phonation , respiration ) , especially in the pediatric population .

Example answer:
{"entities": [{"text": "anatomical location", "type": "SpatialConcept"}, {"text": "challenges", "type": "HealthCareActivity"}, {"text": "swallowing", "type": "BiologicFunction"}, {"text": "phonation", "type": "BiologicFunction"}, {"text": "respiration", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: After five days of feeding , weight of larvae and their survival rate was found to decrease with increasing JA concentrations in both broccoli cultivars .

Example answer:
{"entities": [{"text": "larvae", "type": "Eukaryote"}, {"text": "JA", "type": "Chemical"}, {"text": "broccoli cultivars", "type": "Eukaryote"}]}

Example input:
Sentence: Over - expression of Lxrα in the intestine delays the transport of ingested lipids in larvae , while deletion of Lxrα increases the rate of lipid transport .

Example answer:
{"entities": [{"text": "Over - expression", "type": "BiologicFunction"}, {"text": "Lxrα", "type": "AnatomicalStructure"}, {"text": "intestine", "type": "AnatomicalStructure"}, {"text": "transport", "type": "BiologicFunction"}, {"text": "lipids", "type": "Chemical"}, {"text": "larvae", "type": "Eukaryote"}, {"text": "deletion", "type": "BiologicFunction"}, {"text": "Lxrα", "type": "Chemical"}, {"text": "lipid", "type": "Chemical"}]}

Example input:
Sentence: The larval burden in infected animals was 0 .

Example answer:
{"entities": [{"text": "larval", "type": "Eukaryote"}]}

Example input:
Sentence: Mouthing or ingesting a pest - control product and consuming an item / insect after treatment were common mechanisms for children under the age of two .

Example answer:
{"entities": [{"text": "Mouthing", "type": "BiologicFunction"}, {"text": "ingesting", "type": "BiologicFunction"}, {"text": "pest - control product", "type": "Chemical"}]}

Example input:
Sentence: The energy - deficient red palm weevil larvae through their intrinsic abilities showed enhanced response to their digestibility resulting 27 .

Example answer:
{"entities": [{"text": "red palm weevil", "type": "Eukaryote"}, {"text": "larvae", "type": "Eukaryote"}]}

Example input:
Sentence: 78 % increase in approximate digestibility ( AD ) compared to control larvae .

Example answer:
{"entities": [{"text": "larvae", "type": "Eukaryote"}]}

Input:
Sentence: Larval feeding has important challenges associated with such factors as small mouth gape ( ≈100 μm ) , the low activity of digestive enzymes , and the intake of live food .

## Item MedMentions:test:3179
Example input:
Sentence: 33 with and without comorbidities ) or the discharge destination ( AUC = 0 . 72 without comorbidities ; 0 . 73 - 0 . 74 with comorbidities ) beyond that accounted for by demographic and clinical information .

Example answer:
{"entities": [{"text": "discharge", "type": "HealthCareActivity"}, {"text": "destination", "type": "SpatialConcept"}, {"text": "clinical information", "type": "IntellectualProduct"}]}

Example input:
Sentence: Age - sex adjusted hazard ratios were highest in the 45 - 64 years group : for major CVD s , HR ( no qualifications vs university degree ) = 1 . 62 ( 95 % CI : 1 . 49 - 1 . 77 ) for primary events , and HR = 1 . 49

Example answer:
{"entities": [{"text": "CVD", "type": "BiologicFunction"}, {"text": "university degree", "type": "IntellectualProduct"}, {"text": "primary", "type": "BiologicFunction"}]}

Example input:
Sentence: Comparing current smokers and nonsmokers , some significant associations from adjusted analyses included the following : having a Mental Component Summary score ( a measure of overall mental health ) above the mean of the US population relative to below the mean ( adjusted odds ratio [ aOR ] = 0 . 81 , 95 % CI : 0 . 73 - 0 . 90 ) ; having physician - diagnosed depression

Example answer:
{"entities": [{"text": "current smokers", "type": "Finding"}, {"text": "nonsmokers", "type": "Finding"}, {"text": "adjusted analyses", "type": "ResearchActivity"}, {"text": "mental health", "type": "BiologicFunction"}, {"text": "US", "type": "SpatialConcept"}, {"text": "population", "type": "PopulationGroup"}, {"text": "physician", "type": "ProfessionalOrOccupationalGroup"}, {"text": "diagnosed", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}]}

Example input:
Sentence: 91 ; 95 % confidence interval ( CI ) , 0 . 68 - 1 . 2 ] , 3 . 0 times more likely to be discharged to home or self - care ( 95 % CI , 2 .

Example answer:
{"entities": [{"text": "discharged to home", "type": "HealthCareActivity"}, {"text": "self - care", "type": "Organization"}]}

Example input:
Sentence: 08 - 1 . 20 ) greater risk of death and a 26 % ( HR = 1 . 26 , 95 % CI = 1 . 20 - 1 . 32 ) greater risk of hospitalization , and an increase of one mental condition was associated with a 31 % ( HR = 1 . 31 , 95 % CI = 1 .

Example answer:
{"entities": [{"text": "death", "type": "BiologicFunction"}, {"text": "HR", "type": "ClinicalAttribute"}, {"text": "hospitalization", "type": "HealthCareActivity"}]}

Example input:
Sentence: 6 to 2 . 9 ) and nearby sources of safe abortion care ( AOR = 1 . 7 ; 95 % CI 1 .

Example answer:
{"entities": [{"text": "safe abortion care", "type": "HealthCareActivity"}]}

Example input:
Sentence: 64 ; 95 % CI 0 . 45 - 0 . 90 , respectively ) , and those who achieved hemodynamic response ( adjusted HR 0 . 75 ; 95 % CI = 0 . 57 - 1 . 0 ) had lower risk .

Example answer:
{"entities": [{"text": "hemodynamic response", "type": "BiologicFunction"}]}

Example input:
Sentence: 07 ; model 2 : aOR : 1 . 9 , 95 % CI : 1 . 1 to 3 .

Example answer:
{"entities": []}

Example input:
Sentence: In the exploratory analysis , patients with DOR ≥12 months ( n = 287 ) or ≥24 months ( n = 133 ) were more likely to experience grade 3 / 4 AEs than the overall population .

Example answer:
{"entities": [{"text": "exploratory analysis", "type": "ResearchActivity"}, {"text": "AEs", "type": "BiologicFunction"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: 6 , 95 % CI : 1 . 1 - 6 . 2 , and respiratory related arousal index : ≥7 . 6 / h OR = 2 . 3 , 95 % CI : 1 . 1 - 4 . 7 , but not measures of hypoxemia after adjustment for age , hypertension , diabetes , smoking , obesity , and NSAID use .

Example answer:
{"entities": [{"text": "arousal", "type": "BiologicFunction"}, {"text": "index", "type": "IntellectualProduct"}, {"text": "hypoxemia", "type": "Finding"}, {"text": "hypertension", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "obesity", "type": "BiologicFunction"}, {"text": "NSAID", "type": "Chemical"}]}

Input:
Sentence: ( aOR = 1 . 52 , 95 % CI : 1 . 33 - 1 . 74 ) , respiratory conditions ( aOR = 1 . 16 , 95 % CI : 1 . 04 - 1 . 30 ) , or repeated seizures / blackouts / convulsions ( aOR = 1 . 80 , 95 % CI : 1 . 22 - 2 . 67 ) ; heavy alcohol use vs never use ( aOR = 5 . 49 , 95 % CI : 4 . 57 - 6 . 59 ) ; a poor vs excellent perception of overall health ( aOR = 3 . 79 , 95 % CI : 2 . 60 - 5 . 52 ) ; and being deployed vs nondeployed ( aOR = 0 . 87 , 95 % CI : 0 . 78 - 0 . 96 ) .

## Item MedMentions:test:3601
Example input:
Sentence: Thus , the aim of the present study was to determine the epidemiological pattern of the disease in an endemic herd reared under extensive conditions ( Spanish Pyrenees ) by identifying main factors associated with infection and clinical disease dynamics .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "pattern", "type": "SpatialConcept"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "Spanish", "type": "SpatialConcept"}, {"text": "Pyrenees", "type": "SpatialConcept"}, {"text": "infection", "type": "BiologicFunction"}, {"text": "clinical disease", "type": "BiologicFunction"}]}

Example input:
Sentence: For such diseases , multiple biological , environmental and population - level mechanisms determine the dynamics of the outbreak , including pathogen 's epidemiological traits ( e . g .

Example answer:
{"entities": [{"text": "diseases", "type": "BiologicFunction"}, {"text": "environmental", "type": "SpatialConcept"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: Infection rates were minimal to completely absent in all Cx .

Example answer:
{"entities": [{"text": "Infection rates", "type": "Finding"}, {"text": "Cx .", "type": "Eukaryote"}]}

Example input:
Sentence: Simulating the potential role of media coverage and infected bats in the 2014 Ebola outbreak Multiple epidemiological models have been developed to model the transmission dynamics of Ebola virus ( EBOV ) disease in West Africa in 2014 because the severity of the epidemic is commonly overestimated .

Example answer:
{"entities": [{"text": "Simulating", "type": "ResearchActivity"}, {"text": "infected", "type": "Finding"}, {"text": "bats", "type": "Eukaryote"}, {"text": "Ebola", "type": "BiologicFunction"}, {"text": "Ebola virus ( EBOV ) disease", "type": "BiologicFunction"}, {"text": "West Africa", "type": "SpatialConcept"}]}

Example input:
Sentence: Our layered - surveillance approach was effective in localizing a cluster of influenza A outbreak .

Example answer:
{"entities": [{"text": "approach", "type": "SpatialConcept"}, {"text": "localizing", "type": "SpatialConcept"}]}

Example input:
Sentence: Two clinical isolates ( D7630 and D7632 ) and one environmental isolate ( D7631 ) were recovered from this outbreak .

Example answer:
{"entities": [{"text": "isolates", "type": "Chemical"}, {"text": "D7630", "type": "Bacterium"}, {"text": "D7632", "type": "Bacterium"}, {"text": "environmental", "type": "SpatialConcept"}, {"text": "isolate", "type": "Chemical"}, {"text": "D7631", "type": "Bacterium"}]}

Example input:
Sentence: Outbreak in later part of winter , high case fatality and younger population is more affected .

Example answer:
{"entities": [{"text": "younger population", "type": "PopulationGroup"}]}

Example input:
Sentence: The ensuing report summarizes a recent outbreak in these infections that have been reported both in Europe and the United States , along with efforts to reduce the risk for patient infection .

Example answer:
{"entities": [{"text": "infections", "type": "BiologicFunction"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "United States", "type": "SpatialConcept"}, {"text": "infection", "type": "BiologicFunction"}]}

Example input:
Sentence: Using the method developed here , the analysis of 268 samples from 73 suspected outbreaks showed 100 % specificity and 95 .

Example answer:
{"entities": [{"text": "method", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: The study site was dominated by a few multi - locus microsatellite genotypes , and their identities and large - scale locations persist across both study years , suggesting that local epizootics ( outbreaks ) are initiated each wet season by residual propagules from the previous wet season , and not by long - distance transport of propagules from other sites .

Example answer:
{"entities": [{"text": "study site", "type": "SpatialConcept"}, {"text": "locations", "type": "SpatialConcept"}, {"text": "study", "type": "ResearchActivity"}, {"text": "local", "type": "SpatialConcept"}, {"text": "sites", "type": "SpatialConcept"}]}

Input:
Sentence: The epidemiology of the outbreak is largely unstudied , with the list of X .

## Item MedMentions:test:3603
Example input:
Sentence: Pooled odds ratio ( ORs ) for the association and the corresponding 95 % confidence intervals ( CIs ) were evaluated by a random or fixed - effect model .

Example answer:
{"entities": []}

Example input:
Sentence: Using correlation analysis , the main findings indicated that agreement varied as a result of the child 's difficulties for reports of conduct problems , and this seemed to be related to the presence or absence of externalising difficulties in the child 's presentation .

Example answer:
{"entities": [{"text": "correlation analysis", "type": "ResearchActivity"}, {"text": "indicated", "type": "Finding"}, {"text": "reports", "type": "IntellectualProduct"}, {"text": "conduct problems", "type": "Finding"}, {"text": "presence", "type": "Finding"}, {"text": "externalising difficulties", "type": "Finding"}]}

Example input:
Sentence: Data were analyzed by robust regression analysis and presented as β coefficients with 95 % confidence intervals ( CI ) .

Example answer:
{"entities": [{"text": "analyzed", "type": "ResearchActivity"}, {"text": "regression analysis", "type": "IntellectualProduct"}]}

Example input:
Sentence: The inter - rater agreement ( k ) between local and central pathology was calculated for Ki - 67 , grading , hormone receptors ( ER / PgR ) and HER2 / neu .

Example answer:
{"entities": [{"text": "central pathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "Ki - 67", "type": "Chemical"}, {"text": "grading", "type": "IntellectualProduct"}, {"text": "hormone receptors", "type": "Chemical"}, {"text": "ER", "type": "Chemical"}, {"text": "PgR", "type": "Chemical"}, {"text": "HER2 / neu", "type": "ClinicalAttribute"}]}

Example input:
Sentence: The scores of the two radiologists were consistent ( kappa = 0 . 634 ) .

Example answer:
{"entities": [{"text": "radiologists", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Agreement was assessed by intraclass correlation coefficients ( ICCs ) and Bland - Altman plots .

Example answer:
{"entities": []}

Example input:
Sentence: Substantial agreement was observed for ER ( k0 . 612 ; 95 % CI , 0538 - 0 . 686 ) , PgR ( k0 . 659 ; 95 % CI , 0580 - 0 . 737 ) , Ki - 67 ( k0 .

Example answer:
{"entities": [{"text": "ER", "type": "Chemical"}, {"text": "PgR", "type": "Chemical"}, {"text": "Ki - 67", "type": "Chemical"}]}

Example input:
Sentence: Kappa statistics were calculated to assess agreement between Xpert and smear to culture .

Example answer:
{"entities": [{"text": "Kappa statistics", "type": "IntellectualProduct"}, {"text": "Xpert", "type": "HealthCareActivity"}, {"text": "smear", "type": "HealthCareActivity"}, {"text": "culture", "type": "HealthCareActivity"}]}

Example input:
Sentence: Odds ratios ( ORs ) and 95 % confidence intervals ( CIs ) were used to estimate the strength of associations .

Example answer:
{"entities": []}

Example input:
Sentence: Intraclass correlation coefficients ( ICC ) , estimated kappa ( κ ) , weighted kappa ( κω ) , and Bland - Altman plots were used to determine interobserver and intraobserver levels of agreement .

Example answer:
{"entities": []}

Input:
Sentence: The traditional overall proportion of agreement does not provide an adequate picture of reliability - weighted kappa coefficients should be used instead .

## Item MedMentions:test:3093
Example input:
Sentence: Group III / IV muscle afferents limit the intramuscular metabolic perturbation during whole body exercise in humans The purpose of this study was to determine the role of group III / IV muscle afferents in limiting the endurance exercise - induced metabolic perturbation assayed in muscle biopsy samples taken from locomotor muscle .

Example answer:
{"entities": [{"text": "Group III / IV muscle", "type": "AnatomicalStructure"}, {"text": "afferents", "type": "AnatomicalStructure"}, {"text": "intramuscular", "type": "SpatialConcept"}, {"text": "whole body", "type": "AnatomicalStructure"}, {"text": "humans", "type": "Eukaryote"}, {"text": "study", "type": "ResearchActivity"}, {"text": "determine", "type": "HealthCareActivity"}, {"text": "group III / IV muscle", "type": "AnatomicalStructure"}, {"text": "endurance", "type": "Finding"}, {"text": "assayed", "type": "HealthCareActivity"}, {"text": "muscle", "type": "AnatomicalStructure"}, {"text": "biopsy samples", "type": "AnatomicalStructure"}, {"text": "locomotor", "type": "BiologicFunction"}]}

Example input:
Sentence: Reduced Chest and Abdominal Wall Mobility and Their Relationship to Lung Function , Respiratory Muscle Strength , and Exercise Tolerance in Subjects With COPD Advanced air - flow limitation in patients with COPD leads to a reduction in vital capacity , respiratory muscle strength , and exercise capacity .

Example answer:
{"entities": [{"text": "Reduced Chest", "type": "Finding"}, {"text": "Abdominal Wall", "type": "AnatomicalStructure"}, {"text": "Lung Function", "type": "BiologicFunction"}, {"text": "Muscle Strength", "type": "BiologicFunction"}, {"text": "Exercise Tolerance", "type": "ClinicalAttribute"}, {"text": "COPD", "type": "BiologicFunction"}, {"text": "air - flow", "type": "BiologicFunction"}, {"text": "vital capacity", "type": "ClinicalAttribute"}, {"text": "muscle strength", "type": "BiologicFunction"}, {"text": "exercise capacity", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Superoxide dismutase and catalase activity was elevated after exposure to the lower concentrations and then decreased with higher concentrations .

Example answer:
{"entities": [{"text": "Superoxide dismutase", "type": "Chemical"}, {"text": "catalase", "type": "Chemical"}, {"text": "activity", "type": "BiologicFunction"}]}

Example input:
Sentence: Neither heating rate nor thermal stress affected plasma sodium and chloride levels , nor the expression of transcripts that included catalase , glucocorticoid receptor , heat shock protein70 ( hsp70 ) , heat shock protein 90α ( hsp90α ) and cytochrome P450 1a ( cyp1a ) .

Example answer:
{"entities": [{"text": "thermal stress", "type": "BiologicFunction"}, {"text": "plasma sodium", "type": "HealthCareActivity"}, {"text": "chloride levels", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "transcripts", "type": "Chemical"}, {"text": "catalase", "type": "Chemical"}, {"text": "glucocorticoid receptor", "type": "Chemical"}, {"text": "heat shock protein70", "type": "Chemical"}, {"text": "hsp70", "type": "Chemical"}, {"text": "heat shock protein 90α", "type": "Chemical"}, {"text": "hsp90α", "type": "Chemical"}, {"text": "cytochrome P450 1a", "type": "Chemical"}, {"text": "cyp1a", "type": "Chemical"}]}

Example input:
Sentence: We investigated whether elevating muscle carnitine , and thereby the acetyl - group buffering capacity , altered the metabolic and physiological adaptations to 24 weeks of high - intensity interval training ( HIIT ) at 100 % maximal exercise capacity ( Wattmax ) .

Example answer:
{"entities": [{"text": "muscle", "type": "AnatomicalStructure"}, {"text": "carnitine", "type": "Chemical"}, {"text": "acetyl - group buffering capacity", "type": "Finding"}, {"text": "metabolic", "type": "BiologicFunction"}, {"text": "physiological adaptations", "type": "BiologicFunction"}]}

Example input:
Sentence: To investigate the role of metabo - and mechanosensitive group III / IV muscle afferents in limiting the intramuscular metabolic perturbation during whole body endurance exercise , eight subjects performed 5 km cycling time trials under control conditions ( CTRL ) and with lumbar intrathecal fentanyl impairing lower limb muscle afferent feedback ( FENT ) .

Example answer:
{"entities": [{"text": "metabo", "type": "BiologicFunction"}, {"text": "group III / IV muscle", "type": "AnatomicalStructure"}, {"text": "afferents", "type": "AnatomicalStructure"}, {"text": "intramuscular", "type": "SpatialConcept"}, {"text": "whole body", "type": "AnatomicalStructure"}, {"text": "endurance", "type": "Finding"}, {"text": "trials", "type": "ResearchActivity"}, {"text": "under control conditions", "type": "Finding"}, {"text": "CTRL", "type": "Finding"}, {"text": "lumbar", "type": "SpatialConcept"}, {"text": "intrathecal", "type": "SpatialConcept"}, {"text": "fentanyl", "type": "Chemical"}, {"text": "lower limb", "type": "AnatomicalStructure"}, {"text": "muscle", "type": "AnatomicalStructure"}, {"text": "afferent", "type": "AnatomicalStructure"}, {"text": "feedback", "type": "BiologicFunction"}, {"text": "FENT", "type": "BiologicFunction"}]}

Example input:
Sentence: Burned adults had a significant decrease in stability index and balance including the dynamic limits of stability ( P < .05 ) .

Example answer:
{"entities": [{"text": "Burned", "type": "InjuryOrPoisoning"}, {"text": "balance", "type": "BiologicFunction"}]}

Example input:
Sentence: Severely burned adults exhibited significantly lower peak torque and total work in their quadriceps ( 27 . 50 and 22 . 58 % , P < .05 ) and knee flexors ( 23 . 72 , and 21 . 65 % , P < .05 ) relative to the nonburned adults .

Example answer:
{"entities": [{"text": "burned", "type": "InjuryOrPoisoning"}, {"text": "quadriceps", "type": "AnatomicalStructure"}, {"text": "knee flexors", "type": "AnatomicalStructure"}, {"text": "nonburned adults", "type": "Finding"}]}

Example input:
Sentence: Patients who had severe burns ( burned TBSA ≥ 40 % ) showed muscular weakness , limited balance , and mobility levels between 16 and 24 weeks after discharge from the hospital compared with matched nonburned control subjects .

Example answer:
{"entities": [{"text": "severe burns", "type": "InjuryOrPoisoning"}, {"text": "burned TBSA", "type": "InjuryOrPoisoning"}, {"text": "muscular weakness", "type": "Finding"}, {"text": "balance", "type": "BiologicFunction"}, {"text": "discharge", "type": "HealthCareActivity"}, {"text": "hospital", "type": "Organization"}]}

Example input:
Sentence: Therefore , the aim of this study is to determine the impact of severe burn injuries on lower - limb muscular strength , balance , and mobility level in adults .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "severe burn injuries", "type": "InjuryOrPoisoning"}, {"text": "lower - limb", "type": "AnatomicalStructure"}, {"text": "muscular strength", "type": "BiologicFunction"}, {"text": "balance", "type": "BiologicFunction"}]}

Input:
Sentence: Lower - Limb Muscular Strength , Balance , and Mobility Levels in Adults Following Severe Thermal Burn Injuries Severe burn injuries are associated with hypermetabolic response and increased catabolism .

## Item MedMentions:test:3542
Example input:
Sentence: In contrast , 25 % ( n = 26 ) of class II were over - treated due to use of unnecessarily broad - spectrum antibiotics .

Example answer:
{"entities": [{"text": "over - treated", "type": "HealthCareActivity"}, {"text": "broad - spectrum antibiotics", "type": "Chemical"}]}

Example input:
Sentence: Prior to the introduction of the Yellow Card Scheme , 24 % of the participating herds had an antimicrobial consumption for one or more age groups which exceeded the Yellow Card Scheme threshold values on antimicrobial consumption , while 50 % of the herds had an antimicrobial consumption below the national average .

Example answer:
{"entities": [{"text": "Yellow Card Scheme", "type": "IntellectualProduct"}, {"text": "antimicrobial", "type": "Chemical"}, {"text": "consumption", "type": "BiologicFunction"}]}

Example input:
Sentence: A significant reduction ( p < 0 , 001 - 0 , 02 ) in susceptibility for the strains after 2009 was noted towards piperacillin ( 100 % vs 50 % ) , ceftazidime ( 100 % / 77 . 3 % ) , cefepime ( 97 . 9 % / 68 . 2 % ) , amikacin ( 100 % / 63 .

Example answer:
{"entities": [{"text": "piperacillin", "type": "Chemical"}, {"text": "ceftazidime", "type": "Chemical"}, {"text": "cefepime", "type": "Chemical"}, {"text": "amikacin", "type": "Chemical"}]}

Example input:
Sentence: Almost three - quarters took orally administered drugs , of which antispastic and antiepileptic drugs were among the most frequent .

Example answer:
{"entities": [{"text": "orally administered drugs", "type": "Chemical"}, {"text": "antiepileptic drugs", "type": "Chemical"}]}

Example input:
Sentence: The most common indications for antimicrobial use were antimicrobial prophylaxis ( 28 .

Example answer:
{"entities": [{"text": "antimicrobial", "type": "Chemical"}, {"text": "prophylaxis", "type": "HealthCareActivity"}]}

Example input:
Sentence: Overall , 161 antimicrobials were prescribed ( 1 . 9 antimicrobials per patient ) : 55 . 3 % ( 89 / 161 ) were empiric , 16 .

Example answer:
{"entities": [{"text": "antimicrobials", "type": "Chemical"}]}

Example input:
Sentence: Sixty - three percent of class I ( n = 43 ) were over - treated due to both the use of intravenous antibiotic s when oral therapy was sufficient and use of unnecessarily broad - spectrum antibiotics .

Example answer:
{"entities": [{"text": "over - treated", "type": "HealthCareActivity"}, {"text": "antibiotic", "type": "Chemical"}, {"text": "oral therapy", "type": "HealthCareActivity"}, {"text": "broad - spectrum antibiotics", "type": "Chemical"}]}

Example input:
Sentence: Amoxicillin / clavulanate ( 8 . 2 % , 14 / 171 ) and sulfamethoxazole / trimethoprim ( 8 . 2 % , 14 / 171 ) were the most prescribed antimicrobials .

Example answer:
{"entities": [{"text": "Amoxicillin / clavulanate", "type": "Chemical"}, {"text": "sulfamethoxazole / trimethoprim", "type": "Chemical"}, {"text": "antimicrobials", "type": "Chemical"}]}

Example input:
Sentence: Among the farmers , 13 % also stated that change in choice of product had contributed to reducing their antimicrobial consumption .

Example answer:
{"entities": [{"text": "farmers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "antimicrobial", "type": "Chemical"}, {"text": "consumption", "type": "BiologicFunction"}]}

Example input:
Sentence: The measures most frequently stated as having contributed to the antimicrobial reduction were increased use of vaccines ( 52 % of farmers ; 35 % of the veterinarians ) , less use of group medication ( 44 % of the farmers ; 58 % of the veterinarians ) and staff education ( 22 % of the farmers ; 26 % of the veterinarians ) .

Example answer:
{"entities": [{"text": "antimicrobial", "type": "Chemical"}, {"text": "vaccines", "type": "Chemical"}, {"text": "farmers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "veterinarians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "group medication", "type": "Chemical"}]}

Input:
Sentence: Reduced usage of antimicrobials for oral use accounted for 89 % of the total reduction in antimicrobial use .

## Item MedMentions:test:3670
Example input:
Sentence: Correlations with anatomic aspects provided evidence of a rostrocaudal gradient with increasing gray / white - matter ratio and decreasing hematoma -volume and rate of hematoma enlargement from frontal to occipital ICH location .

Example answer:
{"entities": [{"text": "rostrocaudal", "type": "SpatialConcept"}, {"text": "gray", "type": "AnatomicalStructure"}, {"text": "white - matter", "type": "AnatomicalStructure"}, {"text": "hematoma", "type": "BiologicFunction"}, {"text": "enlargement", "type": "AnatomicalStructure"}, {"text": "frontal", "type": "AnatomicalStructure"}, {"text": "occipital", "type": "AnatomicalStructure"}, {"text": "ICH", "type": "Finding"}, {"text": "location", "type": "SpatialConcept"}]}

Example input:
Sentence: Sample entropy data show the level of signal complexity in different phases of the ictal ECT .

Example answer:
{"entities": [{"text": "ECT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Analysis of aortic valves indicated that the transprosthetic mean pressure gradient increased with time ( 13 . 4 ± 5 . 2 vs 15 .

Example answer:
{"entities": [{"text": "Analysis", "type": "ResearchActivity"}, {"text": "aortic valves", "type": "AnatomicalStructure"}, {"text": "indicated", "type": "Finding"}, {"text": "transprosthetic mean pressure gradient", "type": "Finding"}]}

Example input:
Sentence: 47 ( range : 1 . 72 - 38 . 48 ) , while no statistical difference for the VN angle ( P = 0 . 084 ) and the absolute difference was 2 . 20±1 . 63 ( range : 0 . 05 - 7 . 56 ) .

Example answer:
{"entities": []}

Example input:
Sentence: GRV ≥ 25 mL or higher than expected GRV adjusted by weight ( 0 . 4 mL / kg ) were also not different among the study groups ( P = .90 and P = .87 , respectively ) .

Example answer:
{"entities": [{"text": "GRV", "type": "ClinicalAttribute"}, {"text": "expected", "type": "IntellectualProduct"}]}

Example input:
Sentence: The ESG group demonstrated an improvement in the maximum vertical opening ( MVO = 5 . 1 ±3 . 4 mm ; P = . 012 ) and anteroposterior mandibular movement ( MAM ) during maximum opening ( 7 . 4 ±9 . 5 ; P = . 019 ) , significantly higher than that of the EG ( MVO = 1 . 8 ±3 . 5 mm ; MAM = 0 .

Example answer:
{"entities": [{"text": "maximum vertical opening", "type": "BiologicFunction"}, {"text": "MVO", "type": "BiologicFunction"}, {"text": "anteroposterior mandibular movement", "type": "BiologicFunction"}, {"text": "MAM", "type": "BiologicFunction"}, {"text": "opening", "type": "BiologicFunction"}]}

Example input:
Sentence: Significant increasing in mCBFV , LF / HF ratio , SD2 / SD1 , Shannon Entropy and inversely decreasing SampEn during breath holding maneuver compared with baseline were found in both groups ( p < 0 .

Example answer:
{"entities": [{"text": "mCBFV", "type": "Finding"}, {"text": "decreasing", "type": "Finding"}, {"text": "breath holding", "type": "Finding"}]}

Example input:
Sentence: In addition , the data of ground reaction force ( GRF ) and ground reaction moment ( GRM ) was record when they performed walking at comfortable state .

Example answer:
{"entities": []}

Example input:
Sentence: The high - risk group showed decreased fractional anisotropy ( FA ) , a measure of water diffusion directionality , and increased radial diffusivity in the anterior region of corpus callosum compared to the low - risk group .

Example answer:
{"entities": [{"text": "high - risk group", "type": "PopulationGroup"}, {"text": "fractional anisotropy", "type": "HealthCareActivity"}, {"text": "FA", "type": "HealthCareActivity"}, {"text": "water", "type": "Chemical"}, {"text": "anterior region of corpus callosum", "type": "AnatomicalStructure"}, {"text": "low - risk group", "type": "PopulationGroup"}]}

Example input:
Sentence: The demographic variables , sample entropy of GRF and GRM , and impulse difference of bilateral foot were considered as potential explanatory variables of risk assessment model .

Example answer:
{"entities": [{"text": "explanatory", "type": "IntellectualProduct"}, {"text": "risk assessment", "type": "HealthCareActivity"}, {"text": "model", "type": "IntellectualProduct"}]}

Input:
Sentence: 28e - 05 ) ; impulse difference ( p = 0 . 02036 ) ; sample entropy of GRF in vertical direction ( p = 0 . 0144 ) ; sample entropy of GRM in anterior - posterior direction ( p = 0 . 0387 ) .

## Item MedMentions:test:3062
Example input:
Sentence: In experiment 1 , SVC were grown in DMEM containing 10 % FBS ( Control ) and treated with 300 µM oleic acid ( OLA ) + FBS , linoleic acid ( LNA ) + FBS , palmitic acid ( PAM ) + FBS , or stearic acid ( STA ) + FBS for 48 h .

Example answer:
{"entities": [{"text": "SVC", "type": "AnatomicalStructure"}, {"text": "DMEM", "type": "Chemical"}, {"text": "FBS", "type": "Chemical"}, {"text": "oleic acid", "type": "Chemical"}, {"text": "OLA", "type": "Chemical"}, {"text": "linoleic acid", "type": "Chemical"}, {"text": "LNA", "type": "Chemical"}, {"text": "palmitic acid", "type": "Chemical"}, {"text": "PAM", "type": "Chemical"}, {"text": "stearic acid", "type": "Chemical"}, {"text": "STA", "type": "Chemical"}]}

Example input:
Sentence: strain CCA53 exhibiting ligninolytic potential Microbial degradation of lignin releases fermentable sugars , effective utilization of which could support biofuel production from lignocellulosic biomass .

Example answer:
{"entities": [{"text": "strain CCA53", "type": "Bacterium"}, {"text": "ligninolytic", "type": "BiologicFunction"}, {"text": "degradation", "type": "BiologicFunction"}, {"text": "lignin", "type": "Chemical"}, {"text": "fermentable sugars", "type": "Chemical"}, {"text": "biofuel", "type": "Chemical"}, {"text": "lignocellulosic", "type": "Chemical"}]}

Example input:
Sentence: Carboxymethyl cellulase production optimization from newly isolated thermophilic Bacillus subtilis K - 18 for saccharification using response surface methodology In this study , a novel thermophilic strain was isolated from soil and used for cellulase production in submerged fermentation using potato peel as sole carbon source .

Example answer:
{"entities": [{"text": "Carboxymethyl cellulase", "type": "Chemical"}, {"text": "Bacillus subtilis K - 18", "type": "Bacterium"}, {"text": "response surface methodology", "type": "ResearchActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "cellulase", "type": "Chemical"}, {"text": "submerged fermentation", "type": "BiologicFunction"}, {"text": "potato peel", "type": "Food"}, {"text": "carbon", "type": "Chemical"}, {"text": "source", "type": "Finding"}]}

Example input:
Sentence: Succinic acid production by immobilized cultures using spent sulphite liquor as fermentation medium Spent sulphite liquor ( SSL ) was used as carbon source for the production of succinic acid using immobilized cultures of Actinobacillus succinogenes and Basfia succiniciproducens on two different supports , delignified cellulosic material ( DCM ) and alginate beads .

Example answer:
{"entities": [{"text": "Succinic acid", "type": "Chemical"}, {"text": "immobilized", "type": "AnatomicalStructure"}, {"text": "cultures", "type": "HealthCareActivity"}, {"text": "fermentation", "type": "BiologicFunction"}, {"text": "Spent sulphite liquor", "type": "Chemical"}, {"text": "SSL", "type": "Chemical"}, {"text": "carbon", "type": "Chemical"}, {"text": "source", "type": "Finding"}, {"text": "succinic acid", "type": "Chemical"}, {"text": "Actinobacillus succinogenes", "type": "Bacterium"}, {"text": "Basfia succiniciproducens", "type": "Bacterium"}, {"text": "alginate", "type": "Chemical"}]}

Example input:
Sentence: In vitro antifungal , probiotic , and antioxidant functional properties of a novel Lactobacillus paraplantarum isolated from fermented dates in Saudi Arabia Fermented foods produced using dates are used in Gulf countries as beneficial and healthful foods .

Example answer:
{"entities": [{"text": "probiotic", "type": "Chemical"}, {"text": "antioxidant", "type": "Chemical"}, {"text": "Lactobacillus paraplantarum", "type": "Bacterium"}, {"text": "fermented", "type": "Food"}, {"text": "dates", "type": "Food"}, {"text": "Saudi Arabia", "type": "SpatialConcept"}, {"text": "Fermented foods", "type": "Food"}, {"text": "Gulf countries", "type": "SpatialConcept"}, {"text": "healthful foods", "type": "Food"}]}

Example input:
Sentence: Reduction of Aflatoxin B1 Toxicity by Lactobacillus plantarum C88 : A Potential Probiotic Strain Isolated from Chinese Traditional Fermented Food " Tofu " In this study , we investigated the potential of Lactobacillus plantarum isolated from Chinese traditional fermented foods to reduce the toxicity of aflatoxin B1 ( AFB1 ) , and its subsequent detoxification mechanism .

Example answer:
{"entities": [{"text": "Reduction", "type": "HealthCareActivity"}, {"text": "Aflatoxin B1", "type": "Chemical"}, {"text": "Toxicity", "type": "InjuryOrPoisoning"}, {"text": "Lactobacillus plantarum C88", "type": "Bacterium"}, {"text": "Probiotic Strain", "type": "Bacterium"}, {"text": "Chinese", "type": "PopulationGroup"}, {"text": "Fermented Food", "type": "Food"}, {"text": "Tofu", "type": "Food"}, {"text": "study", "type": "ResearchActivity"}, {"text": "Lactobacillus plantarum", "type": "Bacterium"}, {"text": "fermented foods", "type": "Food"}, {"text": "toxicity", "type": "InjuryOrPoisoning"}, {"text": "aflatoxin B1", "type": "Chemical"}, {"text": "AFB1", "type": "Chemical"}, {"text": "detoxification", "type": "HealthCareActivity"}]}

Example input:
Sentence: Novel Acinetobacter parvus HANDI 309 microbial biomass for the production of N - acetyl - β - d - glucosamine ( GlcNAc ) using swollen chitin substrate in submerged fermentation N - acetyl - β - d - glucosamine ( GlcNAc ) 6 is extensively used as an important bio - agent and a functional food additive .

Example answer:
{"entities": [{"text": "Acinetobacter parvus HANDI 309", "type": "Bacterium"}, {"text": "N - acetyl - β - d - glucosamine", "type": "Chemical"}, {"text": "GlcNAc", "type": "Chemical"}, {"text": "chitin", "type": "Chemical"}, {"text": "submerged fermentation", "type": "BiologicFunction"}, {"text": "( GlcNAc ) 6", "type": "Chemical"}, {"text": "bio - agent", "type": "Chemical"}, {"text": "food additive", "type": "Food"}]}

Example input:
Sentence: First , the nutrients were recovered from wheat bran by acid protease hydrolysis .

Example answer:
{"entities": [{"text": "nutrients", "type": "Food"}, {"text": "wheat bran", "type": "Food"}, {"text": "acid", "type": "Chemical"}, {"text": "protease", "type": "Chemical"}]}

Example input:
Sentence: inulinus YB1 - 5 resulted in d - Lactate levels of 99 . 5g / L , with an average production efficiency of 1 . 94g / L / h and a yield of 0 . 89g / g glucose .

Example answer:
{"entities": [{"text": "inulinus YB1 - 5", "type": "Bacterium"}, {"text": "d - Lactate", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}]}

Example input:
Sentence: This study provided a feasible procedure that can help produce cellulosic d - Lactate using agricultural waste without external nutrient supplementation .

Example answer:
{"entities": [{"text": "cellulosic", "type": "Chemical"}, {"text": "d - Lactate", "type": "Chemical"}, {"text": "external", "type": "SpatialConcept"}, {"text": "nutrient supplementation", "type": "Food"}]}

Input:
Sentence: Combined utilization of nutrients and sugar derived from wheat bran for d - Lactate fermentation by Sporolactobacillus inulinus YBS1 - 5 To decrease d - Lactate production cost , wheat bran , a low - cost waste of milling industry , was selected as the sole feedstock .
