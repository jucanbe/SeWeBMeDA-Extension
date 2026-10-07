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

## Item MedMentions:test:3410
Example input:
Sentence: Two mutants of Arabidopsis thaliana representing antipodes in the diversion of carbohydrate metabolism between sucrose and starch were compared to Col - 0 wildtype before and after cold acclimation to investigate interactions of cold acclimation with subcellular re - programming of metabolism .

Example answer:
{"entities": [{"text": "mutants", "type": "BiologicFunction"}, {"text": "Arabidopsis thaliana", "type": "Eukaryote"}, {"text": "antipodes", "type": "AnatomicalStructure"}, {"text": "carbohydrate metabolism", "type": "BiologicFunction"}, {"text": "sucrose", "type": "Chemical"}, {"text": "starch", "type": "Chemical"}, {"text": "Col - 0 wildtype", "type": "Eukaryote"}, {"text": "cold acclimation", "type": "BiologicFunction"}, {"text": "subcellular re - programming", "type": "BiologicFunction"}, {"text": "metabolism", "type": "BiologicFunction"}]}

Example input:
Sentence: Mining for Candidate Genes in an Introgression Line by Using RNA Sequencing : The Anthocyanin Overaccumulation Phenotype in Brassica Introgression breeding is a widely used method for the genetic improvement of crop plants ; however , the mechanism underlying candidate gene flow patterns during hybridization is poorly understood .

Example answer:
{"entities": [{"text": "Candidate Genes", "type": "BiologicFunction"}, {"text": "Introgression Line", "type": "BiologicFunction"}, {"text": "RNA Sequencing", "type": "HealthCareActivity"}, {"text": "Anthocyanin", "type": "Chemical"}, {"text": "Overaccumulation", "type": "Finding"}, {"text": "Brassica", "type": "Eukaryote"}, {"text": "Introgression", "type": "BiologicFunction"}, {"text": "breeding", "type": "BiologicFunction"}, {"text": "genetic improvement", "type": "HealthCareActivity"}, {"text": "crop plants", "type": "Eukaryote"}, {"text": "candidate gene", "type": "BiologicFunction"}, {"text": "flow", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study , we identified a rice Chl -deficient mutant , ygdl - 1 ( yellow green and droopy leaf - 1 ) , which showed yellow - green leaves throughout plant development with decreased content of Chls and carotene and an increased Chl a / b ratio .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "rice", "type": "Food"}, {"text": "Chl", "type": "Chemical"}, {"text": "mutant", "type": "BiologicFunction"}, {"text": "ygdl - 1", "type": "BiologicFunction"}, {"text": "yellow green and droopy leaf - 1", "type": "BiologicFunction"}, {"text": "yellow - green leaves", "type": "Eukaryote"}, {"text": "plant development", "type": "BiologicFunction"}, {"text": "Chls", "type": "Chemical"}, {"text": "carotene", "type": "Chemical"}]}

Example input:
Sentence: Our finding revealed that ATPF , PSAA , PSAB , PSBB and RBL can induce considerable expression changes in TP and may affect the development and growth of rice through photosynthesis and metabolic pathways .

Example answer:
{"entities": [{"text": "ATPF", "type": "Chemical"}, {"text": "PSAA", "type": "Chemical"}, {"text": "PSAB", "type": "Chemical"}, {"text": "PSBB", "type": "Chemical"}, {"text": "RBL", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "TP", "type": "BiologicFunction"}, {"text": "development", "type": "BiologicFunction"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "rice", "type": "Eukaryote"}]}

Example input:
Sentence: The increase of A is largely due to an increase of RuBP regeneration rate via increased leaf nitrogen content , and partially explained by reduced stomatal limitation via increased stomatal conductance relative to A .

Example answer:
{"entities": [{"text": "leaf", "type": "Eukaryote"}, {"text": "nitrogen", "type": "Chemical"}, {"text": "stomatal", "type": "Eukaryote"}]}

Example input:
Sentence: Identification of a peroxisomal -targeted aldolase involved in chlorophyll biosynthesis and sugar metabolism in rice Chlorophyll plays remarkable and critical roles in photosynthetic light - harvesting , energy transduction and plant development .

Example answer:
{"entities": [{"text": "peroxisomal", "type": "AnatomicalStructure"}, {"text": "aldolase", "type": "Chemical"}, {"text": "chlorophyll", "type": "Chemical"}, {"text": "sugar", "type": "Chemical"}, {"text": "metabolism", "type": "BiologicFunction"}, {"text": "rice", "type": "Food"}, {"text": "Chlorophyll", "type": "Chemical"}, {"text": "photosynthetic light - harvesting ,", "type": "BiologicFunction"}, {"text": "energy transduction", "type": "BiologicFunction"}, {"text": "plant development", "type": "BiologicFunction"}]}

Example input:
Sentence: Our results suggest that the OsAld - Y participates in Chl accumulation , chloroplast development and plant growth by influencing the photosynthetic rate of leaves and the sugar metabolism of rice .

Example answer:
{"entities": [{"text": "OsAld - Y", "type": "Chemical"}, {"text": "Chl", "type": "Chemical"}, {"text": "accumulation", "type": "Finding"}, {"text": "chloroplast", "type": "AnatomicalStructure"}, {"text": "development", "type": "BiologicFunction"}, {"text": "plant growth", "type": "BiologicFunction"}, {"text": "leaves", "type": "Eukaryote"}, {"text": "sugar", "type": "Chemical"}, {"text": "metabolism", "type": "BiologicFunction"}, {"text": "rice", "type": "Food"}]}

Example input:
Sentence: The detailed analysis of molecular functions of CAR8 would help to understand the association between photosynthesis and flowering and demonstrate specific genetic mechanisms that can be exploited to improve photosynthesis in rice and potentially other crops .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "molecular functions", "type": "BiologicFunction"}, {"text": "CAR8", "type": "AnatomicalStructure"}, {"text": "flowering", "type": "BiologicFunction"}, {"text": "improve", "type": "Finding"}, {"text": "rice", "type": "Eukaryote"}]}

Example input:
Sentence: In this study , we determined precise location of Carbon Assimilation Rate 8 ( CAR8 ) by crossing a high - yielding indica cultivar with a Japanese commercial cultivar .

Example answer:
{"entities": [{"text": "location", "type": "SpatialConcept"}, {"text": "Carbon Assimilation Rate 8", "type": "AnatomicalStructure"}, {"text": "CAR8", "type": "AnatomicalStructure"}, {"text": "crossing", "type": "BiologicFunction"}, {"text": "indica cultivar", "type": "Eukaryote"}, {"text": "Japanese", "type": "SpatialConcept"}, {"text": "commercial", "type": "IntellectualProduct"}, {"text": "cultivar", "type": "Eukaryote"}]}

Example input:
Sentence: Exploiting the natural variation in CO2 assimilation rate ( A ) between rice cultivars using quantitative genetics is one promising means to identify genes contributing to higher photosynthesis .

Example answer:
{"entities": [{"text": "rice cultivars", "type": "Eukaryote"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Input:
Sentence: Fine Mapping of Carbon Assimilation Rate 8 , a Quantitative Trait Locus for Flag Leaf Nitrogen Content , Stomatal Conductance and Photosynthesis in Rice Increasing the rate of leaf photosynthesis is one important approach for increasing grain yield in rice ( Oryza sativa ) .

## Item MedMentions:test:3852
Example input:
Sentence: These data further advance the model for Red recombination and the proposition that Redβ and RAD52 SSAPs share ancestral and mechanistic roots .

Example answer:
{"entities": [{"text": "Red recombination", "type": "BiologicFunction"}, {"text": "Redβ", "type": "Chemical"}, {"text": "RAD52", "type": "Chemical"}, {"text": "SSAPs", "type": "Chemical"}]}

Example input:
Sentence: We found that β - Amyloid 1 - 42 ( Aβ42 ) - induced BBB disruption was rescued by human recombinant ANXA1 ( hrANXA1 ) in the murine brain endothelial cell line bEnd .

Example answer:
{"entities": [{"text": "β - Amyloid 1 - 42", "type": "Chemical"}, {"text": "Aβ42", "type": "Chemical"}, {"text": "BBB disruption", "type": "HealthCareActivity"}, {"text": "human recombinant ANXA1", "type": "Chemical"}, {"text": "hrANXA1", "type": "Chemical"}, {"text": "murine", "type": "Chemical"}, {"text": "brain endothelial cell line bEnd .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Several critical hub genes were disclosed , such as RPS2 , MMP1 , MMP11 and FAM83H .

Example answer:
{"entities": [{"text": "hub genes", "type": "AnatomicalStructure"}, {"text": "RPS2", "type": "AnatomicalStructure"}, {"text": "MMP1", "type": "AnatomicalStructure"}, {"text": "MMP11", "type": "AnatomicalStructure"}, {"text": "FAM83H", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Through predominately different molecular targets and mechanisms of action , the two drugs modulate the same Creb1 pathway which plays a key role in neurotrophic responses and in inflammatory processes .

Example answer:
{"entities": [{"text": "molecular targets", "type": "Chemical"}, {"text": "drugs", "type": "Chemical"}, {"text": "modulate", "type": "HealthCareActivity"}, {"text": "Creb1 pathway", "type": "BiologicFunction"}, {"text": "neurotrophic responses", "type": "ClinicalAttribute"}, {"text": "inflammatory processes", "type": "BiologicFunction"}]}

Example input:
Sentence: Eight candidate genes were included : rbcL , rpoC1 , rpoB , matK , trnH - psbA , trnL ( UAA ) , atpF - atpH , and psbK - psbI .

Example answer:
{"entities": [{"text": "candidate genes", "type": "AnatomicalStructure"}, {"text": "rbcL", "type": "AnatomicalStructure"}, {"text": "rpoC1", "type": "AnatomicalStructure"}, {"text": "rpoB", "type": "AnatomicalStructure"}, {"text": "matK", "type": "AnatomicalStructure"}, {"text": "trnH - psbA", "type": "SpatialConcept"}, {"text": "trnL", "type": "AnatomicalStructure"}, {"text": "UAA", "type": "SpatialConcept"}, {"text": "atpF - atpH", "type": "SpatialConcept"}, {"text": "psbK - psbI", "type": "SpatialConcept"}]}

Example input:
Sentence: 1038delG The Kidd blood group on the red blood cell ( RBC ) glycoprotein urea transporter - B has a growing number of weak and  alleles in its gene SLC14A1 that are emerging from more widespread genotyping of blood donors and patients .

Example answer:
{"entities": [{"text": "1038delG", "type": "AnatomicalStructure"}, {"text": "Kidd blood group", "type": "BodySystem"}, {"text": "red blood cell", "type": "AnatomicalStructure"}, {"text": "RBC", "type": "AnatomicalStructure"}, {"text": "glycoprotein", "type": "Chemical"}, {"text": "urea transporter - B", "type": "Chemical"}, {"text": " alleles", "type": "BiologicFunction"}, {"text": "gene SLC14A1", "type": "AnatomicalStructure"}, {"text": "widespread", "type": "SpatialConcept"}, {"text": "genotyping", "type": "HealthCareActivity"}, {"text": "blood donors", "type": "PopulationGroup"}]}

Example input:
Sentence: The RA of NASP , EEF1A1 , DNMT1 , ODC1 and RPS27A was increased ( P < 0 .

Example answer:
{"entities": [{"text": "NASP", "type": "AnatomicalStructure"}, {"text": "EEF1A1", "type": "AnatomicalStructure"}, {"text": "DNMT1", "type": "AnatomicalStructure"}, {"text": "ODC1", "type": "AnatomicalStructure"}, {"text": "RPS27A", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Annexin A1 restores Aβ1 - 42 -induced blood - brain barrier disruption through the inhibition of RhoA - ROCK signaling pathway The blood - brain barrier ( BBB ) is composed of brain capillary endothelial cells and has an important role in maintaining homeostasis of the brain separating the blood from the parenchyma of the central nervous system ( CNS ) .

Example answer:
{"entities": [{"text": "Annexin A1", "type": "Chemical"}, {"text": "Aβ1 - 42", "type": "Chemical"}, {"text": "blood - brain barrier disruption", "type": "HealthCareActivity"}, {"text": "inhibition", "type": "BiologicFunction"}, {"text": "RhoA - ROCK signaling pathway", "type": "BiologicFunction"}, {"text": "blood - brain barrier", "type": "AnatomicalStructure"}, {"text": "BBB", "type": "AnatomicalStructure"}, {"text": "brain capillary", "type": "AnatomicalStructure"}, {"text": "endothelial cells", "type": "AnatomicalStructure"}, {"text": "homeostasis", "type": "BiologicFunction"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "blood", "type": "BodySubstance"}, {"text": "parenchyma", "type": "AnatomicalStructure"}, {"text": "central nervous system", "type": "BodySystem"}, {"text": "CNS", "type": "BodySystem"}]}

Example input:
Sentence: Here , we examined the possible interaction of BRG1 -also known as SMARCA4 , an adenosine triphosphatase -containing chromatin remodeler -and SMAD3 in response to cocaine exposure .

Example answer:
{"entities": [{"text": "interaction", "type": "BiologicFunction"}, {"text": "BRG1", "type": "Chemical"}, {"text": "SMARCA4", "type": "Chemical"}, {"text": "adenosine triphosphatase", "type": "Chemical"}, {"text": "chromatin remodeler", "type": "Chemical"}, {"text": "SMAD3", "type": "Chemical"}, {"text": "cocaine exposure", "type": "Finding"}]}

Example input:
Sentence: Using a short hairpin RNA strategy , we demonstrate here that the 2 mammalian RBPs , PUMILIO ( PUM ) 1 and PUM2 , members of the PUF family of posttranscriptional regulators , are essential for hematopoietic stem / progenitor cell ( HSPC ) proliferation and survival in vitro and in vivo upon reconstitution assays .

Example answer:
{"entities": [{"text": "short hairpin RNA", "type": "Chemical"}, {"text": "mammalian", "type": "Eukaryote"}, {"text": "RBPs", "type": "Chemical"}, {"text": "PUMILIO", "type": "Chemical"}, {"text": "PUM ) 1", "type": "Chemical"}, {"text": "PUM2", "type": "Chemical"}, {"text": "PUF family", "type": "Chemical"}, {"text": "posttranscriptional regulators", "type": "BiologicFunction"}, {"text": "hematopoietic stem / progenitor cell ( HSPC ) proliferation", "type": "BiologicFunction"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "reconstitution assays", "type": "HealthCareActivity"}]}

Input:
Sentence: HDAC2 , RBBP4 , CREB1 , and RB1 .

## Item MedMentions:test:3430
Example input:
Sentence: Treatment for Rheumatoid Arthritis and Risk of Alzheimer 's Disease : A Nested Case - Control Analysis It is increasingly becoming accepted that inflammation may play an important role in the pathogenesis of Alzheimer 's disease ( AD ) , as several immune -related genes have been associated with AD .

Example answer:
{"entities": [{"text": "Treatment", "type": "HealthCareActivity"}, {"text": "Rheumatoid Arthritis", "type": "BiologicFunction"}, {"text": "Risk", "type": "Finding"}, {"text": "Alzheimer 's Disease", "type": "BiologicFunction"}, {"text": "Nested Case - Control Analysis", "type": "ResearchActivity"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "pathogenesis", "type": "BiologicFunction"}, {"text": "Alzheimer 's disease", "type": "BiologicFunction"}, {"text": "AD", "type": "BiologicFunction"}, {"text": "immune", "type": "BodySystem"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: On the other hand , anti - inflammatory and immunosuppressive therapies may impact in body fat storage and in liver lipid dynamics .

Example answer:
{"entities": [{"text": "anti - inflammatory", "type": "HealthCareActivity"}, {"text": "immunosuppressive therapies", "type": "HealthCareActivity"}, {"text": "body", "type": "Eukaryote"}, {"text": "fat", "type": "Chemical"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "lipid", "type": "Chemical"}]}

Example input:
Sentence: We also assessed relative risk of AD following exposure to standard RA therapies , including anti - TNF agents ( infliximab , adalimumab , etanercept ) , methotrexate , prednisone , sulfasalazine , and rituximab .

Example answer:
{"entities": [{"text": "assessed relative risk", "type": "HealthCareActivity"}, {"text": "AD", "type": "BiologicFunction"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "therapies", "type": "HealthCareActivity"}, {"text": "anti - TNF agents", "type": "Chemical"}, {"text": "infliximab", "type": "Chemical"}, {"text": "adalimumab", "type": "Chemical"}, {"text": "etanercept", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "sulfasalazine", "type": "Chemical"}, {"text": "rituximab", "type": "Chemical"}]}

Example input:
Sentence: Growing evidence suggests lower lipid levels are present in patients with active RA vs .

Example answer:
{"entities": [{"text": "lipid levels", "type": "Finding"}, {"text": "present", "type": "Finding"}, {"text": "RA", "type": "BiologicFunction"}]}

Example input:
Sentence: Rheumatoid arthritis , insulin resistance , and diabetes Recent progress in the management of rheumatoid arthritis ( RA ) is turning attention toward comorbidities , such as diabetes .

Example answer:
{"entities": [{"text": "Rheumatoid arthritis", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "management", "type": "HealthCareActivity"}, {"text": "rheumatoid arthritis", "type": "BiologicFunction"}, {"text": "RA", "type": "BiologicFunction"}]}

Example input:
Sentence: The objectives of this review are to clarify the links between RA and diabetes and to assess potential effects of disease - modifying antirheumatic drugs ( DMARDs ) on diabetes .

Example answer:
{"entities": [{"text": "review", "type": "IntellectualProduct"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "disease - modifying antirheumatic drugs", "type": "Chemical"}, {"text": "DMARDs", "type": "Chemical"}]}

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

Example input:
Sentence: Increase in lipid levels in patients with RA on synthetic and biological disease - modifying antirheumatic drugs may be accompanied by antiatherogenic changes in lipid composition and function .

Example answer:
{"entities": [{"text": "lipid levels", "type": "Finding"}, {"text": "RA", "type": "BiologicFunction"}, {"text": "synthetic", "type": "Chemical"}, {"text": "disease - modifying antirheumatic drugs", "type": "Chemical"}, {"text": "lipid", "type": "Chemical"}, {"text": "composition", "type": "ClinicalAttribute"}]}

Input:
Sentence: Lipids and lipid changes with synthetic and biologic disease - modifying antirheumatic drug therapy in rheumatoid arthritis : implications for cardiovascular risk To highlight recently published studies addressing lipid changes with disease - modifying antirheumatic drug use and outline implications on cardiovascular outcomes in rheumatoid arthritis ( RA ) .

## Item MedMentions:test:3637
Example input:
Sentence: Two D - SFT patient - derived xenografts ( PDXs ) that represent the first available preclinical in vivo models of SFT were developed and characterised .

Example answer:
{"entities": [{"text": "D - SFT", "type": "BiologicFunction"}, {"text": "patient - derived xenografts", "type": "BiologicFunction"}, {"text": "PDXs", "type": "BiologicFunction"}, {"text": "in vivo models", "type": "ResearchActivity"}, {"text": "SFT", "type": "BiologicFunction"}]}

Example input:
Sentence: Additionally , 2 , 3 , 5 , 4 ' - tetrahydroxystilbene - 2 - O - β - D - glucoside significantly increased the microvessel density in the brain and upregulated CD31 expression in ischemic penumbra , relative to that in the control .

Example answer:
{"entities": [{"text": "2 , 3 , 5 , 4 ' - tetrahydroxystilbene - 2 - O - β - D - glucoside", "type": "Chemical"}, {"text": "microvessel", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "CD31", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "ischemic", "type": "BiologicFunction"}]}

Example input:
Sentence: SSNS and drug loaded SSNS were characterized by DSC , XRPD , FTIR , SEM , Contact angle study and evaluated for in - vitro , in - vivo studies .

Example answer:
{"entities": [{"text": "SSNS", "type": "Chemical"}, {"text": "drug", "type": "Chemical"}, {"text": "DSC", "type": "HealthCareActivity"}, {"text": "XRPD", "type": "HealthCareActivity"}, {"text": "FTIR", "type": "ResearchActivity"}, {"text": "SEM", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "in - vivo", "type": "SpatialConcept"}]}

Example input:
Sentence: Therefore , these data indicated that 2 , 3 , 5 , 4 ' - tetrahydroxystilbene - 2 - O - β - D - glucoside treatment promoted angiogenesis and recovery from ischemia / reperfusion -induced brain injury in rats .

Example answer:
{"entities": [{"text": "indicated", "type": "Finding"}, {"text": "2 , 3 , 5 , 4 ' - tetrahydroxystilbene - 2 - O - β - D - glucoside", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "angiogenesis", "type": "BiologicFunction"}, {"text": "ischemia / reperfusion", "type": "InjuryOrPoisoning"}, {"text": "brain injury", "type": "InjuryOrPoisoning"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: Optimization of this scaffold in terms of EP1 antagonist potency and ligand - lipophilicity efficiency ( LLE ; pIC50 - clogP ) led to a 1 , 2 , 3 , 6 - tetrahydropyridyl - substituted benzo [ d ] thiazole derivative , 7r ( IC50 1 . 1nM ; LLE 4 . 7 ) , which showed a good pharmacological effect when administered intraduodenally in a 17 - phenyl trinor - PGE2 ( 17 - PTP ) - induced overactive bladder model in rats .

Example answer:
{"entities": [{"text": "EP1", "type": "Chemical"}, {"text": "antagonist", "type": "BiologicFunction"}, {"text": "1 , 2 , 3 , 6 - tetrahydropyridyl - substituted benzo [ d ] thiazole derivative , 7r", "type": "Chemical"}, {"text": "17 - phenyl trinor - PGE2", "type": "Chemical"}, {"text": "17 - PTP", "type": "Chemical"}, {"text": "overactive bladder", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: Herein , a biocompatible Gd -integrated CuS nanotheranostic agent ( Gd : CuS @ BSA ) was synthesized via a facile and environmentally friendly biomimetic strategy , using bovine serum albumin ( BSA ) as a biotemplate at physiological temperature .

Example answer:
{"entities": [{"text": "Gd", "type": "Chemical"}, {"text": "CuS", "type": "Chemical"}, {"text": "BSA", "type": "Chemical"}, {"text": "bovine serum albumin", "type": "Chemical"}]}

Example input:
Sentence: A self - developed particle deposition model was adapted and validated to simulate the deposition of budesonide ( inhaled corticosteroid ; ICS ) and formoterol ( long acting β2 agonist ; LABA ) in the upper airways and lungs of the healthy volunteers .

Example answer:
{"entities": [{"text": "particle", "type": "Chemical"}, {"text": "model", "type": "IntellectualProduct"}, {"text": "simulate", "type": "ResearchActivity"}, {"text": "budesonide", "type": "Chemical"}, {"text": "inhaled corticosteroid", "type": "Chemical"}, {"text": "ICS", "type": "Chemical"}, {"text": "formoterol", "type": "Chemical"}, {"text": "long acting β2 agonist", "type": "Chemical"}, {"text": "LABA", "type": "Chemical"}, {"text": "upper airways", "type": "SpatialConcept"}, {"text": "lungs", "type": "AnatomicalStructure"}, {"text": "healthy volunteers", "type": "PopulationGroup"}]}

Example input:
Sentence: Moreover , the tumor accumulation of the GNS - pHLIP was 3 - fold higher than that of GNS - mPEG after intravenous injection into MCF - 7 breast tumor animal models for 24 h .

Example answer:
{"entities": [{"text": "tumor", "type": "BiologicFunction"}, {"text": "accumulation", "type": "Finding"}, {"text": "GNS", "type": "Chemical"}, {"text": "pHLIP", "type": "Chemical"}, {"text": "mPEG", "type": "Chemical"}, {"text": "MCF - 7", "type": "AnatomicalStructure"}, {"text": "breast tumor", "type": "BiologicFunction"}, {"text": "animal models", "type": "BiologicFunction"}]}

Example input:
Sentence: The influence of different long - circulating materials on the pharmacokinetics of liposomal vincristine sulfate This study was designed to improve the in vivo pharmacokinetics of long - circulating vincristine sulfate ( VS ) - loaded liposomes ; three different long - circulating materials , chitosan , poly ( ethylene glycol ) - 1 , 2 - distearoyl sn - glycero - 3 - phosphatidylethanolamine ( PEG - DSPE ) , and poly ( ethylene glycol ) - poly - lactide - co - glycolide ( PEG - PLGA ) , were evaluated at the same coating molar ratio with the commercial product Marqibo ( ® ) ( vincristine sulfate liposome injection [ VSLI ] ) .

Example answer:
{"entities": [{"text": "long - circulating materials", "type": "Chemical"}, {"text": "pharmacokinetics", "type": "BiologicFunction"}, {"text": "liposomal vincristine sulfate", "type": "Chemical"}, {"text": "in vivo", "type": "SpatialConcept"}, {"text": "long - circulating vincristine sulfate ( VS ) - loaded liposomes", "type": "Chemical"}, {"text": "chitosan", "type": "Chemical"}, {"text": "poly ( ethylene glycol ) - 1 , 2 - distearoyl sn - glycero - 3 - phosphatidylethanolamine", "type": "Chemical"}, {"text": "PEG - DSPE", "type": "Chemical"}, {"text": "poly ( ethylene glycol ) - poly - lactide - co - glycolide", "type": "Chemical"}, {"text": "PEG - PLGA", "type": "Chemical"}, {"text": "Marqibo", "type": "Chemical"}]}

Example input:
Sentence: The present study examined whether structural remodeling of the SNS occurs in the vasculature in a genetically hyperlipidemic animal model of atherosclerosis , the Watanabe heritable hyperlipidemic rabbit ( WHHL ; relative to normolipidemic New Zealand white rabbits [ NZW ] ) , and whether SNS plasticity is driven by the progression of disease and / or by stressful social behavior .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "structural remodeling", "type": "BiologicFunction"}, {"text": "SNS", "type": "BodySystem"}, {"text": "vasculature", "type": "AnatomicalStructure"}, {"text": "hyperlipidemic", "type": "BiologicFunction"}, {"text": "animal model", "type": "Eukaryote"}, {"text": "atherosclerosis", "type": "BiologicFunction"}, {"text": "Watanabe heritable hyperlipidemic rabbit", "type": "Eukaryote"}, {"text": "WHHL", "type": "Eukaryote"}, {"text": "normolipidemic", "type": "Finding"}, {"text": "New Zealand white rabbits", "type": "Eukaryote"}, {"text": "NZW", "type": "Eukaryote"}, {"text": "plasticity", "type": "BiologicFunction"}, {"text": "progression of disease", "type": "BiologicFunction"}]}

Input:
Sentence: In vivo pharmacodynamic study ( hyperlipidaemia model ) showed SNSS based formulation significantly improved the bioavailability of drug .

## Item MedMentions:test:3716
Example input:
Sentence: MBL was detected by modified Hodge and imipenem - ethylenediaminetetraacetic acid double - disc synergy test .

Example answer:
{"entities": [{"text": "MBL", "type": "Chemical"}, {"text": "detected", "type": "Finding"}, {"text": "Hodge and imipenem - ethylenediaminetetraacetic acid double - disc synergy test", "type": "HealthCareActivity"}]}

Example input:
Sentence: Immunohistochemical ( IHC ) , double - IHC , immunofluorescence ( IF ) and double - IF analyses were carried out using a tissue microarray consisting of cores with normal human pancreatic tissue .

Example answer:
{"entities": [{"text": "immunofluorescence", "type": "HealthCareActivity"}, {"text": "IF", "type": "HealthCareActivity"}, {"text": "double - IF analyses", "type": "HealthCareActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "pancreatic tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Serum free triiodothyronine ( FT3 ) , free thyroxine ( FT4 ) , and thyroid - stimulating hormone ( TSH ) levels were measured by chemiluminescence immunoassay , and T2DM was defined according to the American Diabetes Association criteria .

Example answer:
{"entities": [{"text": "Serum", "type": "BodySubstance"}, {"text": "free triiodothyronine", "type": "Chemical"}, {"text": "FT3", "type": "Chemical"}, {"text": "free thyroxine", "type": "Chemical"}, {"text": "FT4", "type": "Chemical"}, {"text": "thyroid - stimulating hormone ( TSH ) levels", "type": "Finding"}, {"text": "T2DM", "type": "BiologicFunction"}]}

Example input:
Sentence: However , they also have the potential to become attractive pre - concentration and clean - up materials for the determination of masked ( also called modified ) mycotoxins , which have been recognised as important contributors to the toxicological hazard deriving from fungal spoilage of goods .

Example answer:
{"entities": [{"text": "mycotoxins", "type": "Chemical"}, {"text": "toxicological", "type": "BiologicFunction"}, {"text": "goods", "type": "Food"}]}

Example input:
Sentence: An orthogonal liquid chromatography - mass spectrometry assay has also been implemented for the confirmation of hits from the antibody - based assays .

Example answer:
{"entities": [{"text": "orthogonal liquid chromatography - mass spectrometry assay", "type": "HealthCareActivity"}, {"text": "implemented", "type": "Finding"}, {"text": "antibody - based assays", "type": "HealthCareActivity"}]}

Example input:
Sentence: In this study , we have evaluated these two antibodies for the analysis of riboflavin and FMN by indirect competitive ELISA ( icELISA ) in selected foods and pharmaceuticals .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "evaluated", "type": "HealthCareActivity"}, {"text": "antibodies", "type": "Chemical"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "FMN", "type": "Chemical"}, {"text": "competitive", "type": "BiologicFunction"}, {"text": "ELISA", "type": "HealthCareActivity"}, {"text": "icELISA", "type": "HealthCareActivity"}, {"text": "foods", "type": "Food"}, {"text": "pharmaceuticals", "type": "Chemical"}]}

Example input:
Sentence: Comparable to IFN - γ SC , total antibodies evaluated by indirect immunofluorescence assay ( IFA ) were cross reactive , however , neutralizing antibody titers could only be detected against the strain used for infection .

Example answer:
{"entities": [{"text": "IFN - γ", "type": "Chemical"}, {"text": "SC", "type": "AnatomicalStructure"}, {"text": "antibodies", "type": "Chemical"}, {"text": "indirect immunofluorescence assay", "type": "HealthCareActivity"}, {"text": "IFA", "type": "HealthCareActivity"}, {"text": "cross reactive", "type": "BiologicFunction"}, {"text": "neutralizing antibody", "type": "Chemical"}, {"text": "detected", "type": "Finding"}, {"text": "infection", "type": "BiologicFunction"}]}

Example input:
Sentence: The immunoassays developed in this study are sensitive and appears feasible for screening a large number of samples in the quantification of riboflavin and FMN in various biological samples , pharmaceuticals and natural / processed foods .

Example answer:
{"entities": [{"text": "immunoassays", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "FMN", "type": "Chemical"}, {"text": "pharmaceuticals", "type": "Chemical"}, {"text": "processed foods", "type": "Food"}]}

Example input:
Sentence: Cross - reactivity features of deoxynivalenol ( DON ) - targeted immunoaffinity columns aiming to achieve simultaneous analysis of DON and major conjugates in cereal samples Immunoafﬁnity columns ( IACs ) are a well - established tool in the determination of regulated mycotoxins in food and feed commodities .

Example answer:
{"entities": [{"text": "Cross - reactivity", "type": "BiologicFunction"}, {"text": "deoxynivalenol", "type": "Chemical"}, {"text": "DON", "type": "Chemical"}, {"text": "immunoaffinity", "type": "HealthCareActivity"}, {"text": "analysis", "type": "HealthCareActivity"}, {"text": "conjugates", "type": "Chemical"}, {"text": "cereal", "type": "Food"}, {"text": "Immunoafﬁnity", "type": "HealthCareActivity"}, {"text": "mycotoxins", "type": "Chemical"}, {"text": "food", "type": "Food"}, {"text": "feed commodities", "type": "Food"}]}

Example input:
Sentence: A rapid lateral flow immunoassay utilizing CPS - specific monoclonal antibody was developed and tested in endemic regions worldwide .

Example answer:
{"entities": [{"text": "immunoassay", "type": "HealthCareActivity"}, {"text": "CPS", "type": "Chemical"}, {"text": "monoclonal antibody", "type": "Chemical"}, {"text": "endemic regions", "type": "SpatialConcept"}, {"text": "worldwide", "type": "SpatialConcept"}]}

Input:
Sentence: Development of Dual Quantitative Lateral Flow Immunoassay for the Detection of Mycotoxins Lateral flow immunoassays have been widely used in recent years for detection of toxins , heavy metals , and biomarkers .

## Item MedMentions:test:3873
Example input:
Sentence: GSCs are therefore a promising target for GBM treatment .

Example answer:
{"entities": [{"text": "GSCs", "type": "AnatomicalStructure"}, {"text": "GBM", "type": "BiologicFunction"}]}

Example input:
Sentence: It is a feasible and effective therapeutic method for HCC patients .

Example answer:
{"entities": [{"text": "therapeutic method", "type": "HealthCareActivity"}, {"text": "HCC", "type": "BiologicFunction"}]}

Example input:
Sentence: Use by MSM and individuals reporting sexual risk suggests GCO may reach populations with a higher risk of STI .

Example answer:
{"entities": [{"text": "MSM", "type": "PopulationGroup"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "reporting", "type": "HealthCareActivity"}, {"text": "GCO", "type": "IntellectualProduct"}, {"text": "populations", "type": "PopulationGroup"}, {"text": "STI", "type": "BiologicFunction"}]}

Example input:
Sentence: Early diagnosis and tracking of GC is a challenge due to a lack of reliable tools .

Example answer:
{"entities": [{"text": "diagnosis", "type": "Finding"}, {"text": "GC", "type": "BiologicFunction"}, {"text": "challenge", "type": "HealthCareActivity"}]}

Example input:
Sentence: We used GCO program data , website metrics , and provincial STI clinic records to describe temporal trends , progression through the service pathway , and demographic , risk , and testing outcomes for individuals creating GCO accounts during the first 15 months of implementation .

Example answer:
{"entities": [{"text": "GCO", "type": "IntellectualProduct"}, {"text": "website", "type": "IntellectualProduct"}, {"text": "provincial", "type": "Organization"}, {"text": "STI", "type": "BiologicFunction"}, {"text": "clinic", "type": "Organization"}, {"text": "records", "type": "IntellectualProduct"}, {"text": "individuals", "type": "PopulationGroup"}]}

Example input:
Sentence: GCO was promoted through email invitations to provincial STI clinic clients , access codes to clients unable to access immediate clinic -based testing ( deferred testers ) , and a campaign to gay , bisexual , and other men who have sex with men ( MSM ) .

Example answer:
{"entities": [{"text": "GCO", "type": "IntellectualProduct"}, {"text": "email invitations", "type": "IntellectualProduct"}, {"text": "provincial", "type": "Organization"}, {"text": "STI", "type": "BiologicFunction"}, {"text": "clinic", "type": "Organization"}, {"text": "access", "type": "SpatialConcept"}, {"text": "campaign", "type": "HealthCareActivity"}, {"text": "gay", "type": "PopulationGroup"}, {"text": "bisexual", "type": "PopulationGroup"}, {"text": "men who have sex with men", "type": "PopulationGroup"}, {"text": "MSM", "type": "PopulationGroup"}]}

Example input:
Sentence: The objective of the study was to report on characteristics of GCO users , use and test outcomes ( overall and by promotional strategy ) during this pilot phase .

Example answer:
{"entities": [{"text": "objective", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "report", "type": "HealthCareActivity"}, {"text": "GCO", "type": "IntellectualProduct"}, {"text": "users", "type": "PopulationGroup"}]}

Example input:
Sentence: A total of 63 ( 12 . 5 % ) GCO clients were testing for the first time .

Example answer:
{"entities": [{"text": "GCO", "type": "IntellectualProduct"}]}

Example input:
Sentence: Use by first - time testers , repeated use , and STI diagnosis of individuals unable to access immediate clinic -based testing suggest GCO may facilitate uptake of STBBI testing and earlier diagnosis .

Example answer:
{"entities": [{"text": "STI", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "access", "type": "SpatialConcept"}, {"text": "clinic", "type": "Organization"}, {"text": "GCO", "type": "IntellectualProduct"}, {"text": "STBBI", "type": "BiologicFunction"}]}

Example input:
Sentence: Motivation to test ( eg , unable to access clinical services immediately ) appears a key factor underlying GCO use .

Example answer:
{"entities": [{"text": "Motivation", "type": "BiologicFunction"}, {"text": "access", "type": "SpatialConcept"}, {"text": "clinical", "type": "Organization"}, {"text": "GCO", "type": "IntellectualProduct"}]}

Input:
Sentence: Our evaluation suggests that GCO is an acceptable and feasible approach to engage individuals in testing .

## Item MedMentions:test:3955
Example input:
Sentence: Fishes exposed to scopolamine showed a significant cognitive impairment .

Example answer:
{"entities": [{"text": "Fishes", "type": "Eukaryote"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "cognitive impairment", "type": "BiologicFunction"}]}

Example input:
Sentence: After exposure to respective treatment fishes in group III to VII were subjected to cognitive evaluation .

Example answer:
{"entities": [{"text": "fishes", "type": "Eukaryote"}, {"text": "cognitive", "type": "BiologicFunction"}, {"text": "evaluation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Higher fish consumption ( at least 3 portions ) was associated with lower omega - 6 fatty acid levels ( p = 0 . 026 ) and higher omega - 3 fatty acid levels ( p = 0 . 037 ) , both results being statistically significant .

Example answer:
{"entities": [{"text": "fish consumption", "type": "BiologicFunction"}, {"text": "omega - 6 fatty acid", "type": "Chemical"}, {"text": "omega - 3 fatty acid", "type": "Chemical"}, {"text": "results", "type": "Finding"}]}

Example input:
Sentence: Developmental Hypoxia Has Negligible Effects on Long - Term Hypoxia Tolerance and Aerobic Metabolism of Atlantic Salmon ( Salmo salar ) Exposure to developmental hypoxia can have long - term impacts on the physiological performance of fish because of irreversible plasticity .

Example answer:
{"entities": [{"text": "Hypoxia", "type": "BiologicFunction"}, {"text": "Aerobic Metabolism", "type": "BiologicFunction"}, {"text": "Atlantic Salmon", "type": "Eukaryote"}, {"text": "Salmo salar", "type": "Eukaryote"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "physiological", "type": "BiologicFunction"}, {"text": "fish", "type": "Eukaryote"}]}

Example input:
Sentence: The short - term effects of farmed fish food consumed by wild fish congregating outside the farms We simulated in the laboratory the possible effects on fatty acids and immune status of wild fish arriving for the first time in the vicinity of a sea - cage fish farm , shifting their natural diet to commercial feed consumption , rich in fatty acids of vegetable origin .

Example answer:
{"entities": [{"text": "farmed fish", "type": "Eukaryote"}, {"text": "food consumed", "type": "Food"}, {"text": "wild fish", "type": "Eukaryote"}, {"text": "farms", "type": "Organization"}, {"text": "laboratory", "type": "Organization"}, {"text": "fatty acids", "type": "Food"}, {"text": "immune status", "type": "ClinicalAttribute"}, {"text": "sea - cage fish farm", "type": "Organization"}, {"text": "natural diet", "type": "Food"}, {"text": "commercial", "type": "IntellectualProduct"}, {"text": "rich in fatty acids", "type": "Finding"}, {"text": "vegetable origin", "type": "Food"}]}

Example input:
Sentence: Their use has been linked to a host of deleterious effects in aquatic ecosystems such as osteoporosis in vertebrates , developmental impairments in molluscs and reduced fecundity and growth in cladocerans .

Example answer:
{"entities": [{"text": "osteoporosis", "type": "BiologicFunction"}, {"text": "vertebrates", "type": "Eukaryote"}, {"text": "developmental", "type": "BiologicFunction"}, {"text": "molluscs", "type": "Eukaryote"}, {"text": "fecundity", "type": "BiologicFunction"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "cladocerans", "type": "Eukaryote"}]}

Example input:
Sentence: significantly reducing ( 60 % ) the number of parasites in the fish .

Example answer:
{"entities": [{"text": "parasites", "type": "Eukaryote"}, {"text": "fish", "type": "Eukaryote"}]}

Example input:
Sentence: After transfer between farms , high mortality was observed in fish , associated with back arching , abnormal swimming , and ulcerative skin lesions .

Example answer:
{"entities": [{"text": "farms", "type": "Organization"}, {"text": "fish", "type": "Eukaryote"}, {"text": "back arching", "type": "Finding"}, {"text": "abnormal", "type": "Finding"}, {"text": "ulcerative", "type": "BiologicFunction"}, {"text": "skin lesions", "type": "BiologicFunction"}]}

Example input:
Sentence: More research is needed in order to elucidate whether the rapid assimilation of the dietary fatty acids could harm the immune status of fish when feeding for longer periods than two months .

Example answer:
{"entities": [{"text": "dietary fatty acids", "type": "Chemical"}, {"text": "could harm", "type": "Finding"}, {"text": "immune status", "type": "ClinicalAttribute"}, {"text": "fish", "type": "Eukaryote"}]}

Example input:
Sentence: As fish progressed through the harvest event , cook loss decreased , tenderness increased , and pH increased , indicating that stress induced textural changes .

Example answer:
{"entities": []}

Input:
Sentence: The extent of these changes cannot be considered large enough to regard them as compromising the health status of fish .

## Item MedMentions:test:3995
Example input:
Sentence: The presence of TPS cytomorphologic criteria for HGUC in each specimen was recorded , as was the proportion of atypical cells meeting all 4 criteria .

Example answer:
{"entities": [{"text": "presence", "type": "Finding"}, {"text": "TPS", "type": "HealthCareActivity"}, {"text": "cytomorphologic", "type": "AnatomicalStructure"}, {"text": "HGUC", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The German Society of Pediatric Oncology and Hematology ( GPOH ) data center registered and followed patients with other diagnoses than Ewing sarcoma who were treated according to the EE99 protocol in an additional non - Ewing database .

Example answer:
{"entities": [{"text": "German Society of Pediatric Oncology and Hematology ( GPOH ) data center", "type": "Organization"}, {"text": "registered", "type": "HealthCareActivity"}, {"text": "diagnoses", "type": "Finding"}, {"text": "Ewing sarcoma", "type": "BiologicFunction"}, {"text": "treated", "type": "Finding"}, {"text": "EE99 protocol", "type": "IntellectualProduct"}, {"text": "non - Ewing database", "type": "IntellectualProduct"}]}

Example input:
Sentence: Finally , a Newcombe - Wilson test was performed to evaluate the relationship between group and cluster codes and a 3×2 ANOVA to investigate the differences in kinematics between groups and cluster codes .

Example answer:
{"entities": [{"text": "Newcombe - Wilson test", "type": "ResearchActivity"}, {"text": "evaluate", "type": "HealthCareActivity"}, {"text": "cluster codes", "type": "IntellectualProduct"}, {"text": "kinematics", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: In conclusion , a male preponderance was observed , with frequent re - presentations , often in high - risk circumstances .

Example answer:
{"entities": [{"text": "male preponderance", "type": "Finding"}, {"text": "high - risk", "type": "Finding"}]}

Example input:
Sentence: Body Cathexis Scale ( BCS ) , Liebowitz Social Anxiety Scale ( LSAS ) , and Premature Ejaculation Diagnostic Tool ( PEDT ) were applied to the study group twice , once before and once three months after circumcision , and only once in the control group .

Example answer:
{"entities": [{"text": "Body Cathexis Scale", "type": "IntellectualProduct"}, {"text": "BCS", "type": "IntellectualProduct"}, {"text": "Liebowitz Social Anxiety Scale", "type": "IntellectualProduct"}, {"text": "LSAS", "type": "IntellectualProduct"}, {"text": "Premature Ejaculation Diagnostic Tool", "type": "IntellectualProduct"}, {"text": "PEDT", "type": "IntellectualProduct"}, {"text": "circumcision", "type": "HealthCareActivity"}]}

Example input:
Sentence: Patients were dichotomized at admission into low - or high - risk categories using a cutoff of MELD ≥ 19 , and they were reclassified at day of implant forming four groups : Group LL ( remained low risk ) , LH ( worsened to high risk ) , HH ( remained high risk ) , and HL ( improved to low risk ) .

Example answer:
{"entities": [{"text": "admission", "type": "HealthCareActivity"}, {"text": "MELD", "type": "IntellectualProduct"}, {"text": "implant", "type": "HealthCareActivity"}, {"text": "groups", "type": "IntellectualProduct"}, {"text": "Group", "type": "IntellectualProduct"}, {"text": "remained", "type": "Finding"}, {"text": "worsened", "type": "IntellectualProduct"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: Individuals were stratified by gender , age , and region , and the RIs were obtained by nonparametric methods .

Example answer:
{"entities": [{"text": "Individuals", "type": "PopulationGroup"}, {"text": "region", "type": "SpatialConcept"}, {"text": "nonparametric methods", "type": "IntellectualProduct"}]}

Example input:
Sentence: ND cases were reclassified into TBS categories by 2 pathologists , and the results were compared with surgical outcomes .

Example answer:
{"entities": [{"text": "ND", "type": "Finding"}, {"text": "TBS", "type": "HealthCareActivity"}, {"text": "categories", "type": "IntellectualProduct"}, {"text": "pathologists", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Cases were distributed in group # 1 ( all cases with both techniques ) , group # 2 ( dissection / clamping ) , and group # 3 ( blind stick ) .

Example answer:
{"entities": [{"text": "dissection", "type": "BiologicFunction"}, {"text": "blind stick", "type": "MedicalDevice"}]}

Example input:
Sentence: The cases were further classified into PsA and PsV .

Example answer:
{"entities": [{"text": "further", "type": "SpatialConcept"}, {"text": "classified", "type": "IntellectualProduct"}, {"text": "PsA", "type": "BiologicFunction"}, {"text": "PsV", "type": "BiologicFunction"}]}

Input:
Sentence: Epstein and Hutchins classification was used to categorize these cases .

## Item MedMentions:test:3814
Example input:
Sentence: Icaritin activated AMP - activated protein kinase ( AMPK ) signaling in CRC cells , functioning as the upstream signaling for autophagy activation .

Example answer:
{"entities": [{"text": "Icaritin", "type": "Chemical"}, {"text": "AMP - activated protein kinase", "type": "Chemical"}, {"text": "AMPK", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "CRC", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "autophagy", "type": "BiologicFunction"}]}

Example input:
Sentence: In line with the in vivo studies , Mnk1 knockdown by Mnk1 siRNA transfection induced exaggerated angiotensin II - induced cardiomyocyte hypertrophy in neonatal rat ventricular myocytes ( NRVMs ) .

Example answer:
{"entities": [{"text": "Mnk1", "type": "AnatomicalStructure"}, {"text": "knockdown", "type": "ResearchActivity"}, {"text": "siRNA", "type": "Chemical"}, {"text": "transfection", "type": "ResearchActivity"}, {"text": "angiotensin II", "type": "Chemical"}, {"text": "cardiomyocyte hypertrophy", "type": "Finding"}, {"text": "rat", "type": "Eukaryote"}, {"text": "ventricular myocytes", "type": "AnatomicalStructure"}, {"text": "NRVMs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We demonstrated that in primary CLL samples and in CLL cell lines USP7 is : i ) over - expressed through a mechanism involving miR - 338 - 3p and miR - 181b deregulation ; ii ) functionally activated by Casein Kinase 2 ( CK2 ) , an upstream interactor known to be deregulated in CLL ; iii ) effectively targeted by the USP7 inhibitor P5091 .

Example answer:
{"entities": [{"text": "CLL", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "USP7", "type": "Chemical"}, {"text": "over - expressed", "type": "BiologicFunction"}, {"text": "miR - 338 - 3p", "type": "Chemical"}, {"text": "miR - 181b", "type": "Chemical"}, {"text": "Casein Kinase 2", "type": "Chemical"}, {"text": "CK2", "type": "Chemical"}, {"text": "upstream", "type": "SpatialConcept"}, {"text": "interactor", "type": "Chemical"}, {"text": "inhibitor", "type": "Chemical"}, {"text": "P5091", "type": "Chemical"}]}

Example input:
Sentence: We found that USP6 directly deubiquitinated Jak1 , leading to its stabilization and activation of STAT3 .

Example answer:
{"entities": [{"text": "USP6", "type": "Chemical"}, {"text": "deubiquitinated", "type": "BiologicFunction"}, {"text": "Jak1", "type": "Chemical"}, {"text": "stabilization", "type": "Finding"}, {"text": "STAT3", "type": "Chemical"}]}

Example input:
Sentence: Taken together , these results demonstrated that induction of ACTA2 by EGFR and HER2 dimerization was regulated through a JAK2 / STAT1 signaling pathway , and aberrant ACTA2 expression accelerated the invasiveness and metastasis of breast cancer cells .

Example answer:
{"entities": [{"text": "ACTA2", "type": "Chemical"}, {"text": "EGFR", "type": "Chemical"}, {"text": "HER2", "type": "Chemical"}, {"text": "JAK2", "type": "Chemical"}, {"text": "STAT1", "type": "Chemical"}, {"text": "signaling pathway", "type": "BiologicFunction"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "invasiveness", "type": "BiologicFunction"}, {"text": "metastasis", "type": "BiologicFunction"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: This overmigration is stimulated by JNK activation ( and the function of its target Mmp1 ) , while proliferative responses are mediated by Dpp / TGF - β signalling activation .

Example answer:
{"entities": [{"text": "overmigration", "type": "BiologicFunction"}, {"text": "JNK activation", "type": "BiologicFunction"}, {"text": "Mmp1", "type": "AnatomicalStructure"}, {"text": "proliferative", "type": "BiologicFunction"}, {"text": "Dpp", "type": "BiologicFunction"}, {"text": "TGF - β signalling", "type": "BiologicFunction"}, {"text": "activation", "type": "BiologicFunction"}]}

Example input:
Sentence: Analysis of primary clinical samples of nodular fasciitis confirmed the activation of a Jak1 - STAT3 gene signature in vivo Together , our studies highlight Jak1 as the first identified substrate for USP6 , and they offer a mechanistic rationale for the clinical investigation of Jak and STAT3 inhibitors as therapeutics for the treatment of bone and soft tissue tumors along with other neoplasms driven by USP6 overexpression .

Example answer:
{"entities": [{"text": "Analysis", "type": "ResearchActivity"}, {"text": "nodular fasciitis", "type": "BiologicFunction"}, {"text": "confirmed", "type": "Finding"}, {"text": "Jak1", "type": "Chemical"}, {"text": "STAT3", "type": "Chemical"}, {"text": "studies", "type": "HealthCareActivity"}, {"text": "USP6", "type": "Chemical"}, {"text": "clinical investigation", "type": "HealthCareActivity"}, {"text": "Jak", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "bone", "type": "BiologicFunction"}, {"text": "soft tissue tumors", "type": "BiologicFunction"}, {"text": "neoplasms", "type": "BiologicFunction"}, {"text": "overexpression", "type": "BiologicFunction"}]}

Example input:
Sentence: Here we report that the Jak1 - STAT3 signaling pathway serves as an essential effector of USP6 in BSTT formation .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "Jak1", "type": "Chemical"}, {"text": "STAT3", "type": "Chemical"}, {"text": "signaling pathway", "type": "BiologicFunction"}, {"text": "USP6", "type": "Chemical"}, {"text": "BSTT", "type": "BiologicFunction"}]}

Example input:
Sentence: The tumorigenic potential of USP6 was attenuated significantly by CRISPR -mediated deletion of Jak1 or STAT3 , or by administration of a Jak family inhibitor .

Example answer:
{"entities": [{"text": "tumorigenic", "type": "BiologicFunction"}, {"text": "USP6", "type": "Chemical"}, {"text": "CRISPR", "type": "Chemical"}, {"text": "deletion", "type": "BiologicFunction"}, {"text": "Jak1", "type": "AnatomicalStructure"}, {"text": "STAT3", "type": "AnatomicalStructure"}, {"text": "Jak family", "type": "Chemical"}]}

Example input:
Sentence: Jak1 - STAT3 Signals Are Essential Effectors of the USP6 / TRE17 Oncogene in Tumorigenesis Bone and soft tissue tumors ( BSTT ) are relatively poorly understood , hampering the development of effective therapies .

Example answer:
{"entities": [{"text": "Jak1", "type": "Chemical"}, {"text": "STAT3", "type": "Chemical"}, {"text": "Signals", "type": "BiologicFunction"}, {"text": "USP6", "type": "Chemical"}, {"text": "TRE17 Oncogene", "type": "Chemical"}, {"text": "Tumorigenesis", "type": "BiologicFunction"}, {"text": "Bone", "type": "BiologicFunction"}, {"text": "soft tissue tumors", "type": "BiologicFunction"}, {"text": "BSTT", "type": "BiologicFunction"}, {"text": "therapies", "type": "HealthCareActivity"}]}

Input:
Sentence: Deregulated JAK2 signaling has emerged as the central phenotypic driver of BCR -ABL1 - negative MPNs and a unifying therapeutic target .

## Item MedMentions:test:3233
Example input:
Sentence: Cephalosporins were the most frequently prescribed class of antibiotic in clinical practice .

Example answer:
{"entities": [{"text": "Cephalosporins", "type": "Chemical"}, {"text": "antibiotic", "type": "Chemical"}, {"text": "clinical practice", "type": "HealthCareActivity"}]}

Example input:
Sentence: De - escalation therapy was considered when the initial antibiotic therapy was narrowed to penicillin , amoxicillin or amoxicillin / clavulanate within the first 72 h after admission .

Example answer:
{"entities": [{"text": "De - escalation therapy", "type": "HealthCareActivity"}, {"text": "antibiotic therapy", "type": "HealthCareActivity"}, {"text": "penicillin", "type": "Chemical"}, {"text": "amoxicillin", "type": "Chemical"}, {"text": "amoxicillin / clavulanate", "type": "Chemical"}, {"text": "admission", "type": "HealthCareActivity"}]}

Example input:
Sentence: Amoxicillin and cephalexin were the most commonly available antibiotics for sale at the stands ( 60 % and 21 % , respectively ) .

Example answer:
{"entities": [{"text": "Amoxicillin", "type": "Chemical"}, {"text": "cephalexin", "type": "Chemical"}, {"text": "antibiotics", "type": "Chemical"}]}

Example input:
Sentence: The most common reasons for inappropriate antibiotic prescribing were too broad ( 41 % ) , wrong dosage ( 22 % ) , and not indicated ( 17 % ) .

Example answer:
{"entities": [{"text": "antibiotic", "type": "Chemical"}, {"text": "prescribing", "type": "HealthCareActivity"}, {"text": "not indicated", "type": "Finding"}]}

Example input:
Sentence: Inappropriately used antibiotic s should be subject to rigorous control and management , and public policy initiatives are required to promote the judicious use of antibiotic s .

Example answer:
{"entities": [{"text": "antibiotic", "type": "Chemical"}]}

Example input:
Sentence: Major causes of inappropriate antibiotic use were prolonged prescriptions ( 21 . 7 % , 35 / 161 ) and use of agents with an excessively broad coverage spectrum ( 21 . 1 % , 34 / 161 ) .

Example answer:
{"entities": [{"text": "antibiotic", "type": "Chemical"}, {"text": "prescriptions", "type": "HealthCareActivity"}, {"text": "agents", "type": "Chemical"}]}

Example input:
Sentence: The use of aseptic compounding to prepare cefuroxime aliquots by hospital pharmacy appeared to be safe and efficacious .

Example answer:
{"entities": [{"text": "aseptic compounding", "type": "HealthCareActivity"}, {"text": "cefuroxime", "type": "Chemical"}]}

Example input:
Sentence: Empiric intravenous antibiotics ( ceftriaxone and vancomycin ) were administered for suspected bacterial meningitis during 10 days .

Example answer:
{"entities": [{"text": "intravenous", "type": "SpatialConcept"}, {"text": "antibiotics", "type": "Chemical"}, {"text": "ceftriaxone", "type": "Chemical"}, {"text": "vancomycin", "type": "Chemical"}, {"text": "bacterial meningitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Results - Cloxacillin was used in 90 % of the cases , clindamycin in 7 % , and cephalosporins in 2 % .

Example answer:
{"entities": [{"text": "Cloxacillin", "type": "Chemical"}, {"text": "clindamycin", "type": "Chemical"}, {"text": "cephalosporins", "type": "Chemical"}]}

Example input:
Sentence: Amoxicillin / clavulanate ( 8 . 2 % , 14 / 171 ) and sulfamethoxazole / trimethoprim ( 8 . 2 % , 14 / 171 ) were the most prescribed antimicrobials .

Example answer:
{"entities": [{"text": "Amoxicillin / clavulanate", "type": "Chemical"}, {"text": "sulfamethoxazole / trimethoprim", "type": "Chemical"}, {"text": "antimicrobials", "type": "Chemical"}]}

Input:
Sentence: The antibiotic s used inappropriately included azithromycin enteric - coated capsules , compound cefaclor tablets and nifuratel nysfungin vaginal soft capsules in primary hospitals , amoxicillin and clavulanate potassium dispersible tablets ( 7 : 1 ) and cefonicid sodium for injection in secondary hospitals , cefminox sodium for injection and amoxicillin sodium and sulbactam sodium for injection in tertiary hospitals .

## Item MedMentions:test:3795
Example input:
Sentence: Diabetes induced mechanical allodynia and hyperalgesia , cold allodynia , heat hypoalgesia , and depression - like behaviour .

Example answer:
{"entities": [{"text": "Diabetes", "type": "BiologicFunction"}, {"text": "mechanical allodynia", "type": "Finding"}, {"text": "hyperalgesia", "type": "Finding"}, {"text": "cold allodynia", "type": "Finding"}, {"text": "heat hypoalgesia", "type": "Finding"}, {"text": "depression - like behaviour", "type": "BiologicFunction"}]}

Example input:
Sentence: The relative contribution of exaggerated incretin hormone signalling to dysregulated insulin secretion and symptomatic hypoglycaemia is a subject of ongoing inquiry .

Example answer:
{"entities": [{"text": "incretin hormone", "type": "Chemical"}, {"text": "signalling", "type": "BiologicFunction"}, {"text": "insulin secretion", "type": "BiologicFunction"}, {"text": "hypoglycaemia", "type": "BiologicFunction"}]}

Example input:
Sentence: The association between antidepressant use and hemoglobin A1C in older adults Depression is known to increase diabetes risk and worsen glycemic control in older adults , who already experience high rates of diabetes .

Example answer:
{"entities": [{"text": "antidepressant", "type": "Chemical"}, {"text": "hemoglobin A1C", "type": "Chemical"}, {"text": "older adults", "type": "PopulationGroup"}, {"text": "Depression", "type": "BiologicFunction"}, {"text": "worsen glycemic control", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Feelings of depressed mood were associated with obesity ( 1 .

Example answer:
{"entities": [{"text": "Feelings", "type": "BiologicFunction"}, {"text": "depressed mood", "type": "Finding"}, {"text": "obesity", "type": "BiologicFunction"}]}

Example input:
Sentence: Minocycline reduces mechanical allodynia and depressive - like behaviour in type - 1 diabetes mellitus in the rat A common and devastating complication of diabetes mellitus is painful diabetic neuropathy ( PDN ) that can be accompanied by emotional disorders such as depression .

Example answer:
{"entities": [{"text": "Minocycline", "type": "Chemical"}, {"text": "mechanical allodynia", "type": "Finding"}, {"text": "depressive - like behaviour", "type": "BiologicFunction"}, {"text": "type - 1 diabetes mellitus", "type": "BiologicFunction"}, {"text": "rat", "type": "Eukaryote"}, {"text": "complication", "type": "BiologicFunction"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "painful diabetic neuropathy", "type": "BiologicFunction"}, {"text": "PDN", "type": "BiologicFunction"}, {"text": "emotional disorders", "type": "BiologicFunction"}, {"text": "depression", "type": "BiologicFunction"}]}

Example input:
Sentence: Higher depressive symptoms were associated with lower future income and earnings .

Example answer:
{"entities": [{"text": "depressive symptoms", "type": "Finding"}]}

Example input:
Sentence: Lipohypertrophy was present in 53 % and was more frequent in insulin pen users ( 63 % ) compared to insulin pump users ( 34 % ) .

Example answer:
{"entities": [{"text": "Lipohypertrophy", "type": "BiologicFunction"}, {"text": "present", "type": "Finding"}, {"text": "insulin pen", "type": "MedicalDevice"}, {"text": "users", "type": "PopulationGroup"}, {"text": "insulin pump", "type": "MedicalDevice"}]}

Example input:
Sentence: Nurses should focus on injection technique education , and should also screen for depressive symptoms and treatment satisfaction as those factors could be associated with development of lipohypertrophy .

Example answer:
{"entities": [{"text": "Nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "screen", "type": "HealthCareActivity"}, {"text": "depressive symptoms", "type": "Finding"}, {"text": "lipohypertrophy", "type": "BiologicFunction"}]}

Example input:
Sentence: Differences in depression , treatment satisfaction and injection behavior in adults with type 1 diabetes and different degrees of lipohypertrophy To assess the prevalence of lipohypertrophy , and to compare differences in external , personal , and regimen factors in adults with type 1 diabetes and different degrees of lipohypertrophy .

Example answer:
{"entities": [{"text": "depression", "type": "Finding"}, {"text": "injection behavior", "type": "Finding"}, {"text": "type 1 diabetes", "type": "BiologicFunction"}, {"text": "lipohypertrophy", "type": "BiologicFunction"}, {"text": "regimen", "type": "HealthCareActivity"}]}

Example input:
Sentence: Participants with two or more lipohypertrophic areas had higher depression scores , lower treatment satisfaction with glycemic control , higher bolus doses , and reported suboptimal injection behavior compared to those with no lipohypertrophic areas .

Example answer:
{"entities": [{"text": "Participants", "type": "PopulationGroup"}, {"text": "lipohypertrophic", "type": "BiologicFunction"}, {"text": "glycemic control", "type": "BiologicFunction"}, {"text": "bolus doses", "type": "HealthCareActivity"}, {"text": "injection behavior", "type": "Finding"}, {"text": "lipohypertrophic areas", "type": "BiologicFunction"}]}

Input:
Sentence: Depressive symptoms and lower treatment satisfaction might affect diabetes self - management and glycemic control , but the association with lipohypertrophy needs further exploration .

## Item MedMentions:test:3875
Example input:
Sentence: Gene expression data generated from Affymetrix Gene Chip human U133 Plus 2 . 0 array of sorted adult and fetal epithelial cells revealed KRT13 to be significantly enriched in FC and TIC compared to basal cells ( BC ) and luminal cells ( LC ) ( p < 0 .

Example answer:
{"entities": [{"text": "Gene expression", "type": "BiologicFunction"}, {"text": "Affymetrix Gene Chip human U133 Plus 2 . 0 array", "type": "ResearchActivity"}, {"text": "epithelial cells", "type": "AnatomicalStructure"}, {"text": "KRT13", "type": "Chemical"}, {"text": "FC", "type": "AnatomicalStructure"}, {"text": "TIC", "type": "AnatomicalStructure"}, {"text": "basal cells", "type": "AnatomicalStructure"}, {"text": "BC", "type": "AnatomicalStructure"}, {"text": "luminal cells", "type": "AnatomicalStructure"}, {"text": "LC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In addition , LVEF under 30 % and left ventricle end diastolic diameter above 60 mm were independent predictors of functional response to CD133 + cell therapy .

Example answer:
{"entities": [{"text": "LVEF", "type": "ClinicalAttribute"}, {"text": "left ventricle end diastolic diameter", "type": "HealthCareActivity"}, {"text": "CD133 + cell", "type": "AnatomicalStructure"}, {"text": "therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: Our results show that Ins2Akita / + mice with under - expressed Lias gene , exhibit higher oxidative stress and more severe DN features ( albuminuria , glomerular basement membrane thickening and mesangial matrix expansion ) .

Example answer:
{"entities": [{"text": "Ins2Akita / + mice", "type": "Eukaryote"}, {"text": "under - expressed", "type": "BiologicFunction"}, {"text": "Lias gene", "type": "AnatomicalStructure"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "DN", "type": "BiologicFunction"}, {"text": "albuminuria", "type": "Finding"}, {"text": "glomerular basement membrane thickening", "type": "Finding"}, {"text": "mesangial matrix expansion", "type": "Finding"}]}

Example input:
Sentence: Real - time PCR and Western blotting experiments further showed that the expression of Hoxd13 was significantly lower when miR - 193 was highly expressed in rat intestinal epithelial cells .

Example answer:
{"entities": [{"text": "Real - time PCR", "type": "ResearchActivity"}, {"text": "Western blotting experiments", "type": "HealthCareActivity"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "Hoxd13", "type": "Chemical"}, {"text": "miR - 193", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "rat", "type": "Eukaryote"}, {"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "epithelial cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Analysed region for three genes , BCR , IL17RA and RBM38 showed an absolute mean DNA methylation of 25 .

Example answer:
{"entities": [{"text": "Analysed", "type": "ResearchActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "BCR", "type": "AnatomicalStructure"}, {"text": "IL17RA", "type": "AnatomicalStructure"}, {"text": "RBM38", "type": "AnatomicalStructure"}, {"text": "DNA methylation", "type": "BiologicFunction"}]}

Example input:
Sentence: Two genes , IL17RA and RBM38 were technically validated using direct capillary sequencing and results were comparable with positive correlation

Example answer:
{"entities": [{"text": "genes", "type": "AnatomicalStructure"}, {"text": "IL17RA", "type": "AnatomicalStructure"}, {"text": "RBM38", "type": "AnatomicalStructure"}, {"text": "technically validated", "type": "ResearchActivity"}, {"text": "direct capillary sequencing", "type": "ResearchActivity"}, {"text": "positive", "type": "Finding"}]}

Example input:
Sentence: To identify genomic loci underlying LBM , we performed a gene -based genome - wide association study of lean mass index ( LMI ) in 1000 unrelated Caucasian subjects , and replicated in 2283 unrelated Caucasians subjects .

Example answer:
{"entities": [{"text": "genomic loci", "type": "AnatomicalStructure"}, {"text": "LBM", "type": "ClinicalAttribute"}, {"text": "gene", "type": "AnatomicalStructure"}, {"text": "genome - wide association study", "type": "ResearchActivity"}, {"text": "unrelated", "type": "Finding"}, {"text": "Caucasian", "type": "PopulationGroup"}, {"text": "subjects", "type": "PopulationGroup"}, {"text": "Caucasians", "type": "PopulationGroup"}]}

Example input:
Sentence: 58I > V ) in the ND6 gene modulated the phenotypic expression of primary LHON -associated m .

Example answer:
{"entities": [{"text": "58I > V", "type": "AnatomicalStructure"}, {"text": "ND6 gene", "type": "AnatomicalStructure"}, {"text": "modulated", "type": "SpatialConcept"}, {"text": "LHON", "type": "BiologicFunction"}, {"text": "m .", "type": "BiologicFunction"}]}

Example input:
Sentence: Gene -based association analyses highlighted the significant associations of three genes UQCR , TCF3 and MBD3 in one single locus 19p13 .

Example answer:
{"entities": [{"text": "Gene", "type": "AnatomicalStructure"}, {"text": "association analyses", "type": "ResearchActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "UQCR", "type": "AnatomicalStructure"}, {"text": "TCF3", "type": "AnatomicalStructure"}, {"text": "MBD3", "type": "AnatomicalStructure"}, {"text": "locus", "type": "AnatomicalStructure"}, {"text": "19p13 .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Gene -based genome - wide association study identified 19p13 .

Example answer:
{"entities": [{"text": "Gene", "type": "AnatomicalStructure"}, {"text": "genome - wide association study", "type": "ResearchActivity"}, {"text": "19p13 .", "type": "AnatomicalStructure"}]}

Input:
Sentence: These results , together with the known functional relevance of the three genes to LMI , suggested that the 19p13 .

## Item MedMentions:test:4085
Example input:
Sentence: lolii ) produces epoxy - janthitrem alkaloids and is the only endophyte known to provide ryegrass with resistance against porina larvae ( Wiseana cervinata ( Walker ) ) , a major pasture pest in cooler areas of New Zealand .

Example answer:
{"entities": [{"text": "lolii", "type": "Eukaryote"}, {"text": "epoxy - janthitrem", "type": "Chemical"}, {"text": "alkaloids", "type": "Chemical"}, {"text": "endophyte", "type": "Eukaryote"}, {"text": "ryegrass", "type": "Eukaryote"}, {"text": "resistance", "type": "BiologicFunction"}, {"text": "porina larvae", "type": "Eukaryote"}, {"text": "Wiseana cervinata ( Walker )", "type": "Eukaryote"}, {"text": "pasture", "type": "Eukaryote"}, {"text": "areas", "type": "SpatialConcept"}, {"text": "New Zealand", "type": "SpatialConcept"}]}

Example input:
Sentence: The mean linear intercept ( MLI ) and mean alveolar number ( MAN ) were used to assess the degree of lung emphysema .

Example answer:
{"entities": [{"text": "lung emphysema", "type": "BiologicFunction"}]}

Example input:
Sentence: laevis .

Example answer:
{"entities": [{"text": "laevis", "type": "Eukaryote"}]}

Example input:
Sentence: laevis .

Example answer:
{"entities": [{"text": "laevis", "type": "Eukaryote"}]}

Example input:
Sentence: albicans .

Example answer:
{"entities": [{"text": "albicans", "type": "Eukaryote"}]}

Example input:
Sentence: albicans .

Example answer:
{"entities": [{"text": "albicans", "type": "Eukaryote"}]}

Example input:
Sentence: albicans .

Example answer:
{"entities": [{"text": "albicans", "type": "Eukaryote"}]}

Example input:
Sentence: alvei H4 was investigated by adding exogenous AHLs ( C4 - HSL , C6 - HSL and 3 - oxo - C8 - HSL ) to H .

Example answer:
{"entities": [{"text": "alvei H4", "type": "Bacterium"}, {"text": "AHLs", "type": "Chemical"}, {"text": "C4 - HSL", "type": "Chemical"}, {"text": "C6 - HSL", "type": "Chemical"}, {"text": "3 - oxo - C8 - HSL", "type": "Chemical"}, {"text": "H .", "type": "Bacterium"}]}

Example input:
Sentence: alvei H4 culture .

Example answer:
{"entities": [{"text": "alvei H4", "type": "Bacterium"}]}

Example input:
Sentence: alvei H4 .

Example answer:
{"entities": [{"text": "alvei H4", "type": "Bacterium"}]}

Input:
Sentence: alvei .

## Item MedMentions:test:3992
Example input:
Sentence: Moderation analysis indicated that all EFs moderated the relationship between physical punishment and aggression , and only inhibition and problem - solving ability , but not cognitive flexibility and nonverbal fluency , moderated the relations between symbolic punishment and aggression .

Example answer:
{"entities": [{"text": "Moderation analysis", "type": "ResearchActivity"}, {"text": "EFs", "type": "BiologicFunction"}, {"text": "problem - solving ability", "type": "Finding"}, {"text": "cognitive flexibility", "type": "BiologicFunction"}, {"text": "nonverbal", "type": "Finding"}]}

Example input:
Sentence: Understanding the types of facilitation activities and their distinguishing characteristics can assist managers in planning and executing implementations of evidence - based interventions .

Example answer:
{"entities": [{"text": "facilitation", "type": "Organization"}, {"text": "managers", "type": "ProfessionalOrOccupationalGroup"}, {"text": "evidence - based interventions", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: We undertook a nation - wide document analysis to address this gap in knowledge .

Example answer:
{"entities": [{"text": "document", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "knowledge", "type": "IntellectualProduct"}]}

Example input:
Sentence: The data outlined here concur with human studies indicating that potential obstacles are internally represented , a finding implying basic cognitive operations allowing for action selection in macaques .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "studies", "type": "ResearchActivity"}, {"text": "internally", "type": "SpatialConcept"}, {"text": "finding", "type": "Finding"}, {"text": "macaques", "type": "Eukaryote"}]}

Example input:
Sentence: These synthesis analyses involving a large sample of youth with varying initial risk levels represent a further step toward strengthening our knowledge of preventive intervention response and improving preventive interventions .

Example answer:
{"entities": [{"text": "response", "type": "ClinicalAttribute"}]}

Example input:
Sentence: While most chose two different analyses ( 91 ; 54 % ) the most common being intention - to - treat ( ITT ) or modified ITT and per - protocol , a large number of articles only chose to conduct and report one analysis ( 65 ; 39 % ) , most commonly the ITT analysis .

Example answer:
{"entities": [{"text": "analyses", "type": "ResearchActivity"}, {"text": "intention - to - treat", "type": "ResearchActivity"}, {"text": "ITT", "type": "ResearchActivity"}, {"text": "articles", "type": "IntellectualProduct"}, {"text": "report", "type": "IntellectualProduct"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "ITT analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: This essay examines several evidence - based practices developed in the USA , the spread of these practices , the barriers to ensuring availability to people who could benefit from these services , and some promising directions for overcoming the barriers .

Example answer:
{"entities": [{"text": "essay", "type": "IntellectualProduct"}, {"text": "USA", "type": "SpatialConcept"}, {"text": "practices", "type": "HealthCareActivity"}, {"text": "people", "type": "PopulationGroup"}, {"text": "services", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using correlation analysis , the main findings indicated that agreement varied as a result of the child 's difficulties for reports of conduct problems , and this seemed to be related to the presence or absence of externalising difficulties in the child 's presentation .

Example answer:
{"entities": [{"text": "correlation analysis", "type": "ResearchActivity"}, {"text": "indicated", "type": "Finding"}, {"text": "reports", "type": "IntellectualProduct"}, {"text": "conduct problems", "type": "Finding"}, {"text": "presence", "type": "Finding"}, {"text": "externalising difficulties", "type": "Finding"}]}

Example input:
Sentence: Discussing the barriers to the implementation of the Classification can improve understanding of it and its use .

Example answer:
{"entities": [{"text": "Classification", "type": "IntellectualProduct"}, {"text": "improve", "type": "Finding"}]}

Example input:
Sentence: The study uncovered a number of barriers relating to both the relative status of each group and their defined areas of responsibility .

Example answer:
{"entities": []}

Input:
Sentence: The analyses also uncovered numerous barriers and facilitators to implementing each statement .

## Item MedMentions:test:3641
Example input:
Sentence: The country 's malaria incidence is highly variable at provincial level , but less is known at village level .

Example answer:
{"entities": [{"text": "country 's", "type": "SpatialConcept"}, {"text": "malaria", "type": "BiologicFunction"}, {"text": "village", "type": "SpatialConcept"}]}

Example input:
Sentence: In this study , we combine multiplex PCR , custom designed dual indexing and Miseq sequencing for high throughput SNP - profiling of 457 malaria infections from Guinea - Bissau , at the cost of 10 USD per sample .

Example answer:
{"entities": [{"text": "multiplex PCR", "type": "HealthCareActivity"}, {"text": "custom designed dual indexing", "type": "ResearchActivity"}, {"text": "Miseq", "type": "IntellectualProduct"}, {"text": "sequencing", "type": "HealthCareActivity"}, {"text": "SNP", "type": "SpatialConcept"}, {"text": "malaria", "type": "BiologicFunction"}, {"text": "infections", "type": "BiologicFunction"}, {"text": "Guinea - Bissau", "type": "SpatialConcept"}]}

Example input:
Sentence: Performance of loop - mediated isothermal amplification ( LAMP ) for the diagnosis of malaria among malaria suspected pregnant women in Northwest Ethiopia Malaria is a major public health problem and an important cause of maternal and infant morbidity in sub - Saharan Africa , including Ethiopia .

Example answer:
{"entities": [{"text": "loop - mediated isothermal amplification", "type": "HealthCareActivity"}, {"text": "LAMP", "type": "HealthCareActivity"}, {"text": "diagnosis", "type": "Finding"}, {"text": "malaria", "type": "BiologicFunction"}, {"text": "pregnant women", "type": "PopulationGroup"}, {"text": "Northwest", "type": "SpatialConcept"}, {"text": "Ethiopia", "type": "SpatialConcept"}, {"text": "Malaria", "type": "BiologicFunction"}, {"text": "public", "type": "PopulationGroup"}, {"text": "problem", "type": "Finding"}, {"text": "sub - Saharan Africa", "type": "SpatialConcept"}]}

Example input:
Sentence: Analysis of spatial clustering of village malaria cases by Plasmodium species was performed by year .

Example answer:
{"entities": [{"text": "village", "type": "SpatialConcept"}, {"text": "malaria", "type": "BiologicFunction"}, {"text": "Plasmodium species", "type": "Eukaryote"}]}

Example input:
Sentence: The 11 - loci barcode successfully identifies recently emerging parasite subpopulations in western Cambodia that are associated with the C580Y dominant allele for artemisinin resistance in k13 gene .

Example answer:
{"entities": [{"text": "11 - loci barcode", "type": "SpatialConcept"}, {"text": "parasite", "type": "Eukaryote"}, {"text": "western Cambodia", "type": "SpatialConcept"}, {"text": "artemisinin", "type": "Chemical"}, {"text": "resistance", "type": "BiologicFunction"}, {"text": "k13 gene", "type": "AnatomicalStructure"}]}

Example input:
Sentence: falciparum population structure and the gene flow among the parasite population in Cambodia are essential .

Example answer:
{"entities": [{"text": "falciparum", "type": "Eukaryote"}, {"text": "gene flow", "type": "BiologicFunction"}, {"text": "parasite", "type": "Eukaryote"}, {"text": "Cambodia", "type": "SpatialConcept"}]}

Example input:
Sentence: The MIS data of Ratanakiri Province 2010 - 2014 were used to calculate annual incidence rates by Plasmodium species at province and commune levels .

Example answer:
{"entities": [{"text": "MIS", "type": "IntellectualProduct"}, {"text": "Plasmodium species", "type": "Eukaryote"}]}

Example input:
Sentence: Plasmodium falciparum parasite population structure and gene flow associated to anti - malarial drugs resistance in Cambodia Western Cambodia is recognized as the epicentre of emergence of Plasmodium falciparum multi - drug resistance .

Example answer:
{"entities": [{"text": "Plasmodium falciparum", "type": "Eukaryote"}, {"text": "parasite", "type": "Eukaryote"}, {"text": "gene flow", "type": "BiologicFunction"}, {"text": "anti - malarial", "type": "Chemical"}, {"text": "drugs resistance", "type": "BiologicFunction"}, {"text": "Cambodia", "type": "SpatialConcept"}, {"text": "Western Cambodia", "type": "SpatialConcept"}, {"text": "emergence", "type": "BiologicFunction"}]}

Example input:
Sentence: The Cambodian Government aims to eliminate all forms of malaria by 2025 .

Example answer:
{"entities": [{"text": "Government", "type": "Organization"}, {"text": "malaria", "type": "BiologicFunction"}]}

Example input:
Sentence: Passive case detection of malaria in Ratanakiri Province ( Cambodia ) to detect villages at higher risk for malaria Cambodia reduced malaria incidence by more than 75 % between 2000 and 2015 , a target of the Millennium Development Goal 6 .

Example answer:
{"entities": [{"text": "Passive case detection", "type": "ResearchActivity"}, {"text": "malaria", "type": "BiologicFunction"}, {"text": "detect", "type": "Finding"}, {"text": "villages", "type": "SpatialConcept"}, {"text": "Millennium Development Goal 6", "type": "IntellectualProduct"}]}

Input:
Sentence: In 2010 , the Cambodian malaria programme created a Malaria Information System ( MIS ) to capture malaria information at village level through PCD by village malaria workers and health facilities .

## Item MedMentions:test:3828
Example input:
Sentence: These findings suggest that right IPS contributes to predictive position perception during saccades and motion processing in the contralateral visual field .

Example answer:
{"entities": [{"text": "IPS", "type": "SpatialConcept"}, {"text": "position", "type": "SpatialConcept"}, {"text": "perception", "type": "BiologicFunction"}, {"text": "saccades", "type": "BiologicFunction"}, {"text": "contralateral", "type": "SpatialConcept"}, {"text": "visual field", "type": "SpatialConcept"}]}

Example input:
Sentence: Across two experiments we examined whether repetitive transcranial magnetic stimulation ( rTMS ) over right FEF , right IPS , righ t MT , and a control site , peripheral V1 / V2 , diminished participants ' perception of two cases of predictive position perception : trans - saccadic fusion , and the flash grab illusion , both presented in the contralateral visual field .

Example answer:
{"entities": [{"text": "repetitive transcranial magnetic stimulation", "type": "HealthCareActivity"}, {"text": "rTMS", "type": "HealthCareActivity"}, {"text": "right", "type": "SpatialConcept"}, {"text": "FEF", "type": "AnatomicalStructure"}, {"text": "right IPS", "type": "SpatialConcept"}, {"text": "righ", "type": "SpatialConcept"}, {"text": "MT", "type": "AnatomicalStructure"}, {"text": "site", "type": "SpatialConcept"}, {"text": "peripheral V1", "type": "AnatomicalStructure"}, {"text": "V2", "type": "AnatomicalStructure"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "perception", "type": "BiologicFunction"}, {"text": "position", "type": "SpatialConcept"}, {"text": "trans - saccadic", "type": "BiologicFunction"}, {"text": "fusion", "type": "BiologicFunction"}, {"text": "flash grab illusion", "type": "BiologicFunction"}, {"text": "visual field", "type": "SpatialConcept"}]}

Example input:
Sentence: Overall lateralization of seizures with unilateral blinking was contralateral in six patients and ipsilateral in four .

Example answer:
{"entities": [{"text": "seizures", "type": "Finding"}, {"text": "unilateral", "type": "SpatialConcept"}, {"text": "blinking", "type": "BiologicFunction"}, {"text": "contralateral", "type": "SpatialConcept"}]}

Example input:
Sentence: Mean deviations found in the mesiodistal direction were 0 . 817 mm at the implant tip and 0 . 528 mm at the implant shoulder .

Example answer:
{"entities": [{"text": "Mean deviations", "type": "ClinicalAttribute"}, {"text": "implant tip", "type": "MedicalDevice"}, {"text": "implant shoulder", "type": "MedicalDevice"}]}

Example input:
Sentence: An increase in cortical thickness at the hemisphere contralateral to the lesion ( CLH ) was detected in motor and language areas , which may reflect compensation for the gray matter loss in the lesion area or retention of ipsilateral pathways .

Example answer:
{"entities": [{"text": "cortical", "type": "AnatomicalStructure"}, {"text": "hemisphere", "type": "AnatomicalStructure"}, {"text": "contralateral", "type": "SpatialConcept"}, {"text": "lesion", "type": "Finding"}, {"text": "CLH", "type": "AnatomicalStructure"}, {"text": "detected", "type": "Finding"}, {"text": "motor", "type": "SpatialConcept"}, {"text": "language areas", "type": "SpatialConcept"}, {"text": "gray matter", "type": "AnatomicalStructure"}, {"text": "area", "type": "SpatialConcept"}, {"text": "ipsilateral", "type": "SpatialConcept"}]}

Example input:
Sentence: When unilateral blinking was early in seizures , overall lateralization was more often contralateral ( 6 / 7 patients , PPV 85 % ) .

Example answer:
{"entities": [{"text": "unilateral", "type": "SpatialConcept"}, {"text": "blinking", "type": "BiologicFunction"}, {"text": "seizures", "type": "Finding"}, {"text": "contralateral", "type": "SpatialConcept"}]}

Example input:
Sentence: Consistent with previous results , in both cases there were clear biases to overestimate distances oriented along the medio - lateral axis of the hand compared to the proximo - distal axis .

Example answer:
{"entities": [{"text": "oriented", "type": "SpatialConcept"}, {"text": "medio - lateral axis", "type": "BiologicFunction"}, {"text": "hand", "type": "AnatomicalStructure"}, {"text": "proximo - distal axis", "type": "BiologicFunction"}]}

Example input:
Sentence: A unilateral decrease in the vertical height of the dentition and the subsequent steeper occlusal plane inclinations correlated with ( 1 ) mandibular rotational displacement and condylar lateral displacement , ( 2 ) mandibular and condylar morphologic changes ( 3 ) changes in temporal bone position .

Example answer:
{"entities": [{"text": "unilateral", "type": "SpatialConcept"}, {"text": "decrease in the vertical height", "type": "Finding"}, {"text": "dentition", "type": "AnatomicalStructure"}, {"text": "occlusal plane inclinations", "type": "Finding"}, {"text": "mandibular rotational displacement", "type": "AnatomicalStructure"}, {"text": "condylar", "type": "AnatomicalStructure"}, {"text": "mandibular", "type": "AnatomicalStructure"}, {"text": "temporal bone", "type": "AnatomicalStructure"}, {"text": "position", "type": "SpatialConcept"}]}

Example input:
Sentence: Sagittal alignment of pelvis , hip , and spine was analyzed on lateral radiographs taken before ( baseline ) and 1 year after ( follow - up ) THA .

Example answer:
{"entities": [{"text": "Sagittal", "type": "SpatialConcept"}, {"text": "pelvis", "type": "AnatomicalStructure"}, {"text": "hip", "type": "AnatomicalStructure"}, {"text": "spine", "type": "AnatomicalStructure"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "THA", "type": "HealthCareActivity"}]}

Example input:
Sentence: Less angular displacement of the proximal tibia was detected in the medial than in the lateral direction , and tibial displacement was lower in the cranial than the caudal direction .

Example answer:
{"entities": [{"text": "angular", "type": "SpatialConcept"}, {"text": "proximal tibia", "type": "AnatomicalStructure"}, {"text": "medial", "type": "SpatialConcept"}, {"text": "lateral", "type": "SpatialConcept"}, {"text": "direction", "type": "SpatialConcept"}, {"text": "tibial", "type": "AnatomicalStructure"}, {"text": "cranial", "type": "SpatialConcept"}, {"text": "caudal", "type": "SpatialConcept"}]}

Input:
Sentence: Temporal bone sagittal inclination showed a more forward and medial inclination on the contralateral side ( p < 0 .

## Item MedMentions:test:3909
Example input:
Sentence: Cell viability decreased and apoptotic cells significantly increased as concentrations of NaF increased over specific periods of time .

Example answer:
{"entities": [{"text": "Cell viability", "type": "BiologicFunction"}, {"text": "apoptotic", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "NaF", "type": "Chemical"}]}

Example input:
Sentence: In experiment 1 , SVC were grown in DMEM containing 10 % FBS ( Control ) and treated with 300 µM oleic acid ( OLA ) + FBS , linoleic acid ( LNA ) + FBS , palmitic acid ( PAM ) + FBS , or stearic acid ( STA ) + FBS for 48 h .

Example answer:
{"entities": [{"text": "SVC", "type": "AnatomicalStructure"}, {"text": "DMEM", "type": "Chemical"}, {"text": "FBS", "type": "Chemical"}, {"text": "oleic acid", "type": "Chemical"}, {"text": "OLA", "type": "Chemical"}, {"text": "linoleic acid", "type": "Chemical"}, {"text": "LNA", "type": "Chemical"}, {"text": "palmitic acid", "type": "Chemical"}, {"text": "PAM", "type": "Chemical"}, {"text": "stearic acid", "type": "Chemical"}, {"text": "STA", "type": "Chemical"}]}

Example input:
Sentence: Despite of defense mechanisms induced by oil , acute toxic effects have been recorded including mortality , delayed hatching , high rates of developmental abnormalities , disrupted locomotor activity and cardiac failures at the highest PAH concentrations ( ∑TPAHs = 257 , 029±47 , 231ng·L ( - 1 ) ) .

Example answer:
{"entities": [{"text": "oil", "type": "Chemical"}, {"text": "toxic effects", "type": "InjuryOrPoisoning"}, {"text": "hatching", "type": "BiologicFunction"}, {"text": "developmental abnormalities", "type": "AnatomicalStructure"}, {"text": "locomotor activity", "type": "BiologicFunction"}, {"text": "cardiac failures", "type": "BiologicFunction"}, {"text": "PAH", "type": "Chemical"}]}

Example input:
Sentence: Mesenchymal stromal cells exposed to carbon monoxide , with docosahexaenoic acid substrate , produced specialized proresolving lipid mediators , particularly D - series resolvins , which promoted survival .

Example answer:
{"entities": [{"text": "Mesenchymal stromal cells", "type": "AnatomicalStructure"}, {"text": "carbon monoxide", "type": "Chemical"}, {"text": "docosahexaenoic acid", "type": "Chemical"}, {"text": "proresolving", "type": "Finding"}, {"text": "resolvins", "type": "Chemical"}]}

Example input:
Sentence: Higher fish consumption ( at least 3 portions ) was associated with lower omega - 6 fatty acid levels ( p = 0 . 026 ) and higher omega - 3 fatty acid levels ( p = 0 . 037 ) , both results being statistically significant .

Example answer:
{"entities": [{"text": "fish consumption", "type": "BiologicFunction"}, {"text": "omega - 6 fatty acid", "type": "Chemical"}, {"text": "omega - 3 fatty acid", "type": "Chemical"}, {"text": "results", "type": "Finding"}]}

Example input:
Sentence: DHA exposure caused typical apoptotic characteristics .

Example answer:
{"entities": [{"text": "DHA", "type": "Chemical"}]}

Example input:
Sentence: After 21 d of feeding , supplementation of oxidized fish oil increased the levels of malondialdehyde ( MDA ) , oxidized glutathione ( GSSG ) , interleukin - 1β ( IL - 1β ) , tumor necrosis factor - α ( TNF - α ) , interleukin - 2 ( IL - 2 ) , nuclear factor κ B ( NF - κB ) , inducible nitric oxide synthase ( iNOS ) , NO , and Caspase - 3 in jejunal mucosa , and decreased the villous height in duodenum and the levels of secretory immunoglobulin A ( sIgA ) and IL - 4 in the jejunal mucosa compared with supplementation with fresh oil .

Example answer:
{"entities": [{"text": "supplementation", "type": "HealthCareActivity"}, {"text": "oxidized", "type": "BiologicFunction"}, {"text": "fish oil", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "MDA", "type": "Chemical"}, {"text": "oxidized glutathione", "type": "Chemical"}, {"text": "GSSG", "type": "Chemical"}, {"text": "interleukin - 1β", "type": "Chemical"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "tumor necrosis factor - α", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "interleukin - 2", "type": "Chemical"}, {"text": "IL - 2", "type": "Chemical"}, {"text": "nuclear factor κ B", "type": "Chemical"}, {"text": "( NF - κB", "type": "Chemical"}, {"text": "inducible nitric oxide synthase", "type": "Chemical"}, {"text": "iNOS", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "Caspase - 3", "type": "Chemical"}, {"text": "jejunal mucosa", "type": "AnatomicalStructure"}, {"text": "villous", "type": "AnatomicalStructure"}, {"text": "duodenum", "type": "AnatomicalStructure"}, {"text": "secretory immunoglobulin A", "type": "Chemical"}, {"text": "( sIgA", "type": "Chemical"}, {"text": "IL - 4", "type": "Chemical"}, {"text": "oil", "type": "Chemical"}]}

Example input:
Sentence: AA exposure showed no obvious effect on viability of DU145 cells .

Example answer:
{"entities": [{"text": "AA", "type": "Chemical"}, {"text": "viability", "type": "BiologicFunction"}, {"text": "DU145 cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Zebrafish embryos ( Danio rerio ) were exposed during 96 h at three WAF concentrations ( 1 , 10 and 100 % for Arabian Light and 10 , 50 and 100 % for Erika ) in order to cover a wide range of polycyclic aromatic hydrocarbon ( PAH ) concentrations , representative of the levels found after environmental oil spills .

Example answer:
{"entities": [{"text": "Zebrafish", "type": "Eukaryote"}, {"text": "embryos", "type": "AnatomicalStructure"}, {"text": "Danio rerio", "type": "Eukaryote"}, {"text": "Arabian Light", "type": "Chemical"}, {"text": "Erika", "type": "Chemical"}, {"text": "polycyclic aromatic hydrocarbon", "type": "Chemical"}, {"text": "PAH", "type": "Chemical"}, {"text": "environmental", "type": "SpatialConcept"}]}

Example input:
Sentence: Human prostate cancer DU145 cells were treated with different concentrations of fish oil , omega - 3 PUFA ( DHA , and Eicosapentaenoic acid , EPA ) , or omega - 6 PUFA ( Arachidonic acid , AA ) .

Example answer:
{"entities": [{"text": "Human", "type": "Eukaryote"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "DU145 cells", "type": "AnatomicalStructure"}, {"text": "fish oil", "type": "Chemical"}, {"text": "omega - 3 PUFA", "type": "Chemical"}, {"text": "DHA", "type": "Chemical"}, {"text": "Eicosapentaenoic acid", "type": "Chemical"}, {"text": "EPA", "type": "Chemical"}, {"text": "omega - 6 PUFA", "type": "Chemical"}, {"text": "Arachidonic acid", "type": "Chemical"}, {"text": "AA", "type": "Chemical"}]}

Input:
Sentence: However , exposure with fish oil , EPA , or DHA for 24 h significantly affected cell viability .

## Item MedMentions:test:3616
Example input:
Sentence: When adjusted for confounders , fusion surgery was not associated with a more favorable outcome in both SSM scores as compared to decompression alone surgery .

Example answer:
{"entities": [{"text": "fusion surgery", "type": "HealthCareActivity"}, {"text": "outcome", "type": "ResearchActivity"}, {"text": "decompression alone surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: Other indications were the treatment of functional impairment resulting from dystonia ( 26 . 25 % ) , sialorrhea ( 18 . 75 % ) , freezing of gait , and camptocormia .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "dystonia", "type": "Finding"}, {"text": "sialorrhea", "type": "BiologicFunction"}, {"text": "freezing of gait", "type": "Finding"}, {"text": "camptocormia", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 7 ESGE / EASL suggest performing endoscopic treatment with concomitant ductal sampling ( brush cytology , endobiliary biopsies ) of suspected significant strictures identified at MRC in PSC patients who present with symptoms likely to improve following endoscopic treatment .

Example answer:
{"entities": [{"text": "ESGE", "type": "Organization"}, {"text": "EASL", "type": "Organization"}, {"text": "endoscopic", "type": "HealthCareActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "ductal", "type": "AnatomicalStructure"}, {"text": "strictures", "type": "AnatomicalStructure"}, {"text": "MRC", "type": "HealthCareActivity"}, {"text": "PSC", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "improve", "type": "Finding"}]}

Example input:
Sentence: Compared with D0 no surgery controls , the D1 and D7 sham groups exhibited no surgical mortality and similar necropsy and echocardiographic variables .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "sham", "type": "HealthCareActivity"}, {"text": "surgical", "type": "HealthCareActivity"}, {"text": "necropsy", "type": "HealthCareActivity"}, {"text": "echocardiographic", "type": "HealthCareActivity"}]}

Example input:
Sentence: The clinical diagnosis was FP in 45 . 5 % , nasolacrimal duct stenosis ( NLDS ) in 26 .

Example answer:
{"entities": [{"text": "clinical diagnosis", "type": "HealthCareActivity"}, {"text": "FP", "type": "Finding"}, {"text": "nasolacrimal duct stenosis", "type": "Finding"}, {"text": "NLDS", "type": "Finding"}]}

Example input:
Sentence: There was no significant difference in DSG results in those with FP or NLDS .

Example answer:
{"entities": [{"text": "DSG", "type": "HealthCareActivity"}, {"text": "FP", "type": "Finding"}, {"text": "NLDS", "type": "Finding"}]}

Example input:
Sentence: The value of lacrimal scintillography in the assessment of patients with epiphora PurposeTo assess the influence of dacryoscintillography ( DSG ) on the treatment decision for patients with epiphora and clinically patent non - functioning lacrimal systems .MethodsA retrospective 3 - year review .

Example answer:
{"entities": [{"text": "lacrimal scintillography", "type": "HealthCareActivity"}, {"text": "epiphora", "type": "BiologicFunction"}, {"text": "dacryoscintillography", "type": "HealthCareActivity"}, {"text": "DSG", "type": "HealthCareActivity"}, {"text": "clinically patent", "type": "Finding"}, {"text": "lacrimal systems", "type": "AnatomicalStructure"}, {"text": "retrospective 3 - year review", "type": "ResearchActivity"}]}

Example input:
Sentence: Inclusion : patients having DSG for epiphora with delayed tear clearance , lacrimal system patency on syringing , and no visible external cause for watering .

Example answer:
{"entities": [{"text": "DSG", "type": "HealthCareActivity"}, {"text": "epiphora", "type": "BiologicFunction"}, {"text": "delayed tear clearance", "type": "Finding"}, {"text": "lacrimal system patency on syringing", "type": "Finding"}, {"text": "watering", "type": "Finding"}]}

Example input:
Sentence: DCR surgery was considered inappropriate in all 46 eyes with normal DSG .

Example answer:
{"entities": [{"text": "DCR surgery", "type": "HealthCareActivity"}, {"text": "eyes", "type": "Finding"}, {"text": "DSG", "type": "HealthCareActivity"}]}

Example input:
Sentence: DSG can at best provide limited guidance on whether to proceed to DCR surgery .Eye advance online publication , 3 March 2017 ; doi : 10 . 1038 / eye . 2017 . 20 .

Example answer:
{"entities": [{"text": "DSG", "type": "HealthCareActivity"}, {"text": "DCR surgery", "type": "HealthCareActivity"}]}

Input:
Sentence: DCR was successful in 76 . 5 % , however , the DSG result did not affect the success of surgery .Conclusion DSG has severe limitations due to lack of correlation with symptoms and clinical examination , inability to separate lacrimal duct narrowing from lacrimal pump function , and inability to predict the results of surgery .

## Item MedMentions:test:4098
Example input:
Sentence: 10 . 9 ± 4 .

Example answer:
{"entities": []}

Example input:
Sentence: 95 ± 21 . 52 vs 144 .

Example answer:
{"entities": []}

Example input:
Sentence: 16 . 5 ± 4 .

Example answer:
{"entities": []}

Example input:
Sentence: 1 , 54 . 2 ± 3 . 7 , and 104 . 9 ± 4 .

Example answer:
{"entities": []}

Example input:
Sentence: 1 ± 15 . 8 , and 13 . 9 ± 2 .

Example answer:
{"entities": []}

Example input:
Sentence: 14 ± 6 .

Example answer:
{"entities": []}

Example input:
Sentence: 5 ± 64 .

Example answer:
{"entities": []}

Example input:
Sentence: 486 . 9 ± 86 .

Example answer:
{"entities": []}

Example input:
Sentence: 4 ± 14 .

Example answer:
{"entities": []}

Example input:
Sentence: 2 ± 15 . 6 , 24 . 0 ± 5 .

Example answer:
{"entities": []}

Input:
Sentence: 5 ± 12 . 5 and 44 . 6 ± 14 .

## Item MedMentions:test:3623
Example input:
Sentence: High throughput selection of antibiotic - resistant transgenic Arabidopsis plants Kanamycin resistance is the most frequently used antibiotic - resistance marker for Arabidopsis transformations , however , this method frequently causes escape of untransformed plants , particularly at the high seedling density during the selection .

Example answer:
{"entities": [{"text": "transgenic", "type": "Eukaryote"}, {"text": "Arabidopsis plants", "type": "Eukaryote"}, {"text": "Kanamycin", "type": "Chemical"}, {"text": "marker", "type": "ClinicalAttribute"}, {"text": "Arabidopsis", "type": "Eukaryote"}, {"text": "transformations", "type": "BiologicFunction"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "untransformed plants", "type": "Eukaryote"}, {"text": "seedling", "type": "Eukaryote"}]}

Example input:
Sentence: Host - induced gene silencing ( HIGS ) strategy was used to generate the transgenic eggplants expressing msp - 18 and msp - 20 , independently .

Example answer:
{"entities": [{"text": "gene silencing", "type": "BiologicFunction"}, {"text": "HIGS", "type": "BiologicFunction"}, {"text": "transgenic eggplants", "type": "Eukaryote"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "msp - 18", "type": "AnatomicalStructure"}, {"text": "msp - 20", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Such plant -derived signals also upregulated the Aluminum - activated malate transporter ( ALMT1 ) responsible for the secretion of malic acid ( MA ) and the DR5 promoter , an auxin responsive promoter concentrated in root apex of the neighboring plants .

Example answer:
{"entities": [{"text": "plant", "type": "Eukaryote"}, {"text": "upregulated", "type": "BiologicFunction"}, {"text": "Aluminum - activated malate transporter", "type": "Chemical"}, {"text": "ALMT1", "type": "Chemical"}, {"text": "secretion", "type": "BiologicFunction"}, {"text": "malic acid", "type": "Chemical"}, {"text": "MA", "type": "Chemical"}, {"text": "DR5 promoter", "type": "Chemical"}, {"text": "auxin responsive promoter", "type": "Chemical"}, {"text": "root", "type": "Eukaryote"}, {"text": "neighboring", "type": "SpatialConcept"}, {"text": "plants", "type": "Eukaryote"}]}

Example input:
Sentence: The present study was conducted to investigate the effects of rol ABC genes on antioxidant and medicinal potential of lettuce by Agrobacterium -mediated transformation .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "rol ABC genes", "type": "AnatomicalStructure"}, {"text": "antioxidant", "type": "BiologicFunction"}, {"text": "lettuce", "type": "Eukaryote"}, {"text": "Agrobacterium", "type": "Bacterium"}, {"text": "transformation", "type": "BiologicFunction"}]}

Example input:
Sentence: In LpMYB1 overexpressed Arabidopsis , the tolerance of transgenic seedlings to drought and salt was improved , and the germination potential of transgenic seeds increase in the presence of NaCl or ABA .

Example answer:
{"entities": [{"text": "LpMYB1", "type": "Chemical"}, {"text": "overexpressed", "type": "BiologicFunction"}, {"text": "Arabidopsis", "type": "Eukaryote"}, {"text": "transgenic", "type": "Eukaryote"}, {"text": "seedlings", "type": "Eukaryote"}, {"text": "improved", "type": "Finding"}, {"text": "germination", "type": "BiologicFunction"}, {"text": "seeds", "type": "Eukaryote"}, {"text": "presence", "type": "Finding"}, {"text": "NaCl", "type": "Chemical"}, {"text": "ABA", "type": "Chemical"}]}

Example input:
Sentence: These results indicated that SlTDT played an important role in remobilization of malate and citrate in fruit vacuoles .

Example answer:
{"entities": [{"text": "SlTDT", "type": "AnatomicalStructure"}, {"text": "malate", "type": "Chemical"}, {"text": "citrate", "type": "Chemical"}, {"text": "fruit", "type": "Food"}, {"text": "vacuoles", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The results indicated that SlTDT expressed in leaves , roots , flowers and fruits at different ripening stages , suggesting SlTDT may be associated with the development of different tissues .

Example answer:
{"entities": [{"text": "indicated", "type": "Finding"}, {"text": "SlTDT", "type": "AnatomicalStructure"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "leaves", "type": "Eukaryote"}, {"text": "roots", "type": "Eukaryote"}, {"text": "flowers", "type": "Eukaryote"}, {"text": "fruits", "type": "Food"}, {"text": "ripening", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Gas chromatography - mass spectrometer ( GC - MS ) analysis showed that overexpression of SlTDT significantly increased malate content , and reduced citrate content in tomato fruit .

Example answer:
{"entities": [{"text": "Gas chromatography - mass spectrometer", "type": "HealthCareActivity"}, {"text": "GC - MS ) analysis", "type": "HealthCareActivity"}, {"text": "overexpression", "type": "BiologicFunction"}, {"text": "SlTDT", "type": "AnatomicalStructure"}, {"text": "malate", "type": "Chemical"}, {"text": "citrate", "type": "Chemical"}, {"text": "tomato", "type": "Eukaryote"}, {"text": "fruit", "type": "Food"}]}

Example input:
Sentence: By contrast , repression of SlTDT in tomato reduced malate content of and increased citrate content .

Example answer:
{"entities": [{"text": "SlTDT", "type": "AnatomicalStructure"}, {"text": "tomato", "type": "Eukaryote"}, {"text": "malate", "type": "Chemical"}, {"text": "citrate", "type": "Chemical"}]}

Example input:
Sentence: The expression patterns of SlTDT in tomato were analyzed by RT - qPCR .

Example answer:
{"entities": [{"text": "expression", "type": "BiologicFunction"}, {"text": "patterns", "type": "SpatialConcept"}, {"text": "SlTDT", "type": "AnatomicalStructure"}, {"text": "tomato", "type": "Eukaryote"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Input:
Sentence: To further explore the function of SlTDT , we constructed both overexpression and RNAi vectors and obtained transgenic tomato plants by agrobacterium -mediated method .

## Item MedMentions:test:3804
Example input:
Sentence: From February 2009 to December 2015 a total of 184 consecutive patients underwent RARP and either standard or extended PLND for localized prostate cancer ( PCa ) .

Example answer:
{"entities": [{"text": "RARP", "type": "HealthCareActivity"}, {"text": "extended", "type": "SpatialConcept"}, {"text": "PLND", "type": "HealthCareActivity"}, {"text": "localized prostate cancer", "type": "BiologicFunction"}, {"text": "PCa", "type": "BiologicFunction"}]}

Example input:
Sentence: Patients and Methods We conducted a multicenter randomized noninferiority trial in intermediate - risk prostate cancer ( T1 to 2a , Gleason score ≤ 6 , and prostate - specific antigen [ PSA ] 10 . 1 to 20 ng / mL ; T2b to 2c , Gleason ≤ 6 , and PSA ≤ 20 ng / mL ; or T1 to 2 , Gleason = 7 , and PSA ≤ 20 ng / mL ) .

Example answer:
{"entities": [{"text": "multicenter randomized noninferiority trial", "type": "ResearchActivity"}, {"text": "intermediate - risk", "type": "Finding"}, {"text": "prostate cancer", "type": "BiologicFunction"}, {"text": "Gleason score", "type": "Finding"}, {"text": "prostate - specific antigen", "type": "Chemical"}, {"text": "PSA", "type": "Chemical"}, {"text": "Gleason", "type": "Finding"}]}

Example input:
Sentence: The primary end point was the 2 - year progression - free survival ( PFS ) after the protocol treatment .

Example answer:
{"entities": [{"text": "protocol treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: In this study , we manipulated RBBP6 expression levels followed by treatment with either camptothecin or γ - aminobutyric acid in cervical cancer cells to induce apoptosis or cell cycle arrest .

Example answer:
{"entities": [{"text": "study", "type": "HealthCareActivity"}, {"text": "manipulated", "type": "HealthCareActivity"}, {"text": "RBBP6", "type": "AnatomicalStructure"}, {"text": "camptothecin", "type": "Chemical"}, {"text": "γ - aminobutyric acid", "type": "Chemical"}, {"text": "induce", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "cell cycle arrest", "type": "BiologicFunction"}]}

Example input:
Sentence: One hundred twelve cases with a confirmed PSA increase > 0 . 5 ng / ml over the nadir value during the follow - up were included in Group A and underwent a new prostate biopsy .

Example answer:
{"entities": [{"text": "PSA", "type": "Chemical"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "prostate biopsy", "type": "HealthCareActivity"}]}

Example input:
Sentence: 9 % , and at 5 yr the biochemical failures were limited to the National Comprehensive Cancer Network high - risk group .

Example answer:
{"entities": [{"text": "National Comprehensive Cancer Network", "type": "Organization"}]}

Example input:
Sentence: The outcome events of breast cancer were classified as breast cancer - specific death ( BCSD ) , non - BCSD , or survival .

Example answer:
{"entities": [{"text": "breast cancer", "type": "BiologicFunction"}, {"text": "non - BCSD", "type": "Finding"}]}

Example input:
Sentence: Outcomes were biochemical progression - free survival ( BPFS ) using ASTRO and Phoenix criteria , 12 - month continence ( strictly pad - free ) and sexual function ( potency sufficient for sexual intercourse ) .

Example answer:
{"entities": [{"text": "biochemical", "type": "IntellectualProduct"}, {"text": "continence", "type": "BiologicFunction"}, {"text": "sexual function", "type": "BiologicFunction"}, {"text": "sexual intercourse", "type": "BiologicFunction"}]}

Example input:
Sentence: Personalized Medicine Approaches in Prostate Cancer Employing Patient Derived 3D Organoids and Humanized Mice Prostate cancer ( PCa ) is the most common malignancy and the second most common cause of cancer death in Western men .

Example answer:
{"entities": [{"text": "Personalized Medicine Approaches", "type": "HealthCareActivity"}, {"text": "Prostate Cancer", "type": "BiologicFunction"}, {"text": "3D", "type": "SpatialConcept"}, {"text": "Organoids", "type": "AnatomicalStructure"}, {"text": "Humanized Mice", "type": "Eukaryote"}, {"text": "Prostate cancer", "type": "BiologicFunction"}, {"text": "PCa", "type": "BiologicFunction"}, {"text": "malignancy", "type": "BiologicFunction"}, {"text": "Western", "type": "SpatialConcept"}, {"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: Biochemical recurrence was defined as two consecutive post - RP prostate - specific antigen ( PSA ) levels of > 0 . 2 ng / mL after post - RP PSA reaching the nadir of < 0 .

Example answer:
{"entities": [{"text": "Biochemical recurrence", "type": "Finding"}, {"text": "RP", "type": "HealthCareActivity"}, {"text": "prostate - specific antigen", "type": "Chemical"}, {"text": "PSA", "type": "Chemical"}]}

Input:
Sentence: The primary outcome was biochemical - clinical failure ( BCF ) defined by any of the following : PSA failure ( nadir + 2 ) , hormonal intervention , clinical local or distant failure , or death as a result of prostate cancer .

## Item MedMentions:test:3890
Example input:
Sentence: A total of 346 patients were included in the study .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: 167 patients were included in the study .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: In total , 1043 patients met inclusion criteria , among whom 43 . 5 % were ENE - positive .

Example answer:
{"entities": [{"text": "ENE", "type": "Finding"}, {"text": "positive", "type": "Finding"}]}

Example input:
Sentence: Three hundred sixty - six patients ( 29 % ) were included in the NR group .

Example answer:
{"entities": []}

Example input:
Sentence: There were 100 ( 35 . 7 % ) patients who had no comorbidity recorded using the CCI , 112 ( 40 .

Example answer:
{"entities": [{"text": "recorded", "type": "IntellectualProduct"}]}

Example input:
Sentence: 20 studies met our inclusion criteria with 3305 patients in ET group and 4446 patients in LT / PI group .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "ET", "type": "HealthCareActivity"}, {"text": "group", "type": "PopulationGroup"}, {"text": "LT", "type": "HealthCareActivity"}, {"text": "PI", "type": "HealthCareActivity"}]}

Example input:
Sentence: Results : 128 patients met the inclusion criteria .

Example answer:
{"entities": []}

Example input:
Sentence: A total of 144 , 098 patients met the study criteria .

Example answer:
{"entities": []}

Example input:
Sentence: Results One hundred sixty - one patients met inclusion criteria and were included in the study .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: NOM may be a feasible option for surgically eligible rectal cancer patients with cCR after nCRT .

Example answer:
{"entities": [{"text": "surgically", "type": "HealthCareActivity"}, {"text": "rectal cancer", "type": "BiologicFunction"}, {"text": "cCR", "type": "Finding"}, {"text": "nCRT", "type": "HealthCareActivity"}]}

Input:
Sentence: In total , 15 studies , including 920 patients , met the inclusion criteria ; 575 ( 62 . 5 % ) of these patients underwent NOM after cCR , with the remaining patients forming a surgical control group .

## Item MedMentions:test:4018
Example input:
Sentence: The concentration of iodine in the thyroid is the most accurate indicator of iodine nutrition .

Example answer:
{"entities": [{"text": "concentration of iodine", "type": "HealthCareActivity"}, {"text": "thyroid", "type": "AnatomicalStructure"}, {"text": "iodine nutrition", "type": "Chemical"}]}

Example input:
Sentence: The ratios of plasma concentrations of nifedipine in the umbilical vein , intervillous space and amniotic fluid to those in the maternal vein for CG and T2DM were 0 . 53 and 0 . 44 , 0 . 78 and 0 . 87 , respectively , with an amniotic fluid / maternal plasma ratio of 0 .

Example answer:
{"entities": [{"text": "nifedipine", "type": "Chemical"}, {"text": "umbilical vein", "type": "AnatomicalStructure"}, {"text": "intervillous space", "type": "SpatialConcept"}, {"text": "amniotic fluid", "type": "BodySubstance"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "plasma", "type": "BodySubstance"}]}

Example input:
Sentence: Iodine Storage and Metabolism of Mild to Moderate Iodine - Deficient Pregnant Rats Severe iodine deficiency during pregnancy results in neurodevelopmental disorders in children , while the consequences of mild to moderate iodine deficiency ( MMID ) are uncertain .

Example answer:
{"entities": [{"text": "Iodine Storage", "type": "Chemical"}, {"text": "Metabolism", "type": "BiologicFunction"}, {"text": "Iodine - Deficient", "type": "BiologicFunction"}, {"text": "Pregnant", "type": "BiologicFunction"}, {"text": "Rats", "type": "Eukaryote"}, {"text": "Severe iodine deficiency", "type": "BiologicFunction"}, {"text": "neurodevelopmental disorders", "type": "BiologicFunction"}, {"text": "mild to moderate iodine deficiency", "type": "BiologicFunction"}, {"text": "MMID", "type": "BiologicFunction"}, {"text": "uncertain", "type": "Finding"}]}

Example input:
Sentence: This study aimed to evaluate whether the iodine stores in the thyroid cover the needs of the mother and the fetus in iodine - sufficient and MMID conditions by inductively coupled plasma - mass spectrometry .

Example answer:
{"entities": [{"text": "iodine stores", "type": "Chemical"}, {"text": "thyroid cover", "type": "AnatomicalStructure"}, {"text": "iodine", "type": "Chemical"}, {"text": "MMID", "type": "BiologicFunction"}, {"text": "inductively coupled plasma - mass spectrometry", "type": "HealthCareActivity"}]}

Example input:
Sentence: One hundred four - week - old female Wistar rats were randomly divided into MMID ( low iodine intake [ L ] ) and normal ( normal iodine intake [ N ] ) groups .

Example answer:
{"entities": [{"text": "female Wistar rats", "type": "Eukaryote"}, {"text": "MMID", "type": "BiologicFunction"}, {"text": "low iodine intake", "type": "Finding"}, {"text": "normal", "type": "Finding"}, {"text": "normal iodine intake", "type": "Finding"}]}

Example input:
Sentence: The rats were fed for the next three months , and after pregnancy they were further divided into two subgroups , respectively : low iodine pregnancy ( LP ) and low iodine pregnancy with iodine supplement ( LP + ) , and normal iodine intake pregnancy ( NP ) and normal iodine intake pregnancy with iodine supplement ( NP + ) .

Example answer:
{"entities": [{"text": "rats", "type": "Eukaryote"}, {"text": "divided into two subgroups", "type": "IntellectualProduct"}, {"text": "low iodine", "type": "Finding"}, {"text": "pregnancy", "type": "BiologicFunction"}, {"text": "LP", "type": "Finding"}, {"text": "iodine supplement", "type": "Food"}, {"text": "LP +", "type": "Food"}, {"text": "normal iodine intake", "type": "Finding"}, {"text": "NP", "type": "BiologicFunction"}, {"text": "NP +", "type": "Food"}]}

Example input:
Sentence: Iodine supplementation can increase the iodine concentration in the thyroid of maternal rats with MMID and their offspring , as well as in the amniotic fluid during pregnancy .

Example answer:
{"entities": [{"text": "Iodine supplementation", "type": "HealthCareActivity"}, {"text": "iodine concentration", "type": "HealthCareActivity"}, {"text": "thyroid", "type": "AnatomicalStructure"}, {"text": "maternal", "type": "Finding"}, {"text": "rats", "type": "Eukaryote"}, {"text": "MMID", "type": "BiologicFunction"}, {"text": "amniotic fluid", "type": "BodySubstance"}]}

Example input:
Sentence: The iodine intake of pregnant rats in the NP + and LP + groups was twice as much as in the NP and LP groups .

Example answer:
{"entities": [{"text": "pregnant", "type": "BiologicFunction"}, {"text": "rats", "type": "Eukaryote"}, {"text": "NP +", "type": "Food"}, {"text": "LP + groups", "type": "Food"}, {"text": "NP", "type": "Finding"}, {"text": "LP groups", "type": "Finding"}]}

Example input:
Sentence: The iodine concentration in the thyroid of the maternal and newborn rats , maternal serum , placenta , and amniotic fluid were determined by inductively coupled plasma - mass spectrometry .

Example answer:
{"entities": [{"text": "iodine concentration", "type": "HealthCareActivity"}, {"text": "thyroid", "type": "AnatomicalStructure"}, {"text": "maternal", "type": "Finding"}, {"text": "newborn", "type": "Finding"}, {"text": "rats", "type": "Eukaryote"}, {"text": "placenta", "type": "AnatomicalStructure"}, {"text": "amniotic fluid", "type": "BodySubstance"}, {"text": "inductively coupled plasma - mass spectrometry", "type": "HealthCareActivity"}]}

Example input:
Sentence: The concentration of iodine in the thyroid of the N group was significantly higher than that in the L group before pregnancy .

Example answer:
{"entities": [{"text": "concentration of iodine", "type": "HealthCareActivity"}, {"text": "thyroid", "type": "AnatomicalStructure"}, {"text": "N group", "type": "Finding"}, {"text": "L group", "type": "Finding"}]}

Input:
Sentence: The concentration of iodine in amniotic fluid was significantly different between the four groups .

## Item MedMentions:test:4036
Example input:
Sentence: The percentage of patients who shifted from SD at baseline to normal sexual functioning at EOT was higher in males ( placebo , 40 . 6 % ; vilazodone , 35 . 7 % ) than in females ( placebo , 24 . 9 % ; vilazodone , 34 . 9 % ) ; no statistical testing was performed .

Example answer:
{"entities": [{"text": "SD", "type": "BiologicFunction"}, {"text": "sexual functioning", "type": "BiologicFunction"}, {"text": "males", "type": "PopulationGroup"}, {"text": "placebo", "type": "Chemical"}, {"text": "vilazodone", "type": "Chemical"}, {"text": "females", "type": "PopulationGroup"}]}

Example input:
Sentence: The patient was treated with aripiprazole , showing improvement after two weeks of treatment .

Example answer:
{"entities": [{"text": "treated with", "type": "HealthCareActivity"}, {"text": "aripiprazole", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: Prolactin levels decreased by 58 % in the aripiprazole group compared with an increase by 22 % in the placebo group .

Example answer:
{"entities": [{"text": "Prolactin levels decreased", "type": "Finding"}, {"text": "aripiprazole", "type": "Chemical"}]}

Example input:
Sentence: This double - blind , placebo - controlled study aimed at examining the effect of adjunctive treatment with 10 mg aripiprazole on prolactin levels and sexual side - effects in patients with schizophrenia symptomatically maintained on risperidone .

Example answer:
{"entities": [{"text": "double - blind", "type": "ResearchActivity"}, {"text": "placebo - controlled study", "type": "ResearchActivity"}, {"text": "prolactin levels", "type": "HealthCareActivity"}, {"text": "side - effects", "type": "BiologicFunction"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "risperidone", "type": "Chemical"}]}

Example input:
Sentence: Aripiprazole improved erectile dysfunction in five out of six patients .

Example answer:
{"entities": [{"text": "Aripiprazole", "type": "Chemical"}, {"text": "improved", "type": "Finding"}, {"text": "erectile dysfunction", "type": "BiologicFunction"}]}

Example input:
Sentence: Spontaneous ejaculations without sexual arousal have been previously described with several typical and atypical antipsychotics .

Example answer:
{"entities": [{"text": "ejaculations", "type": "BiologicFunction"}, {"text": "sexual arousal", "type": "BiologicFunction"}, {"text": "antipsychotics", "type": "Chemical"}]}

Example input:
Sentence: Aripiprazole was administered at a fixed daily dose of 10 mg / day for 8 weeks .

Example answer:
{"entities": [{"text": "Aripiprazole", "type": "Chemical"}, {"text": "administered", "type": "HealthCareActivity"}]}

Example input:
Sentence: The partial agonistic effect of aripiprazole on D2 receptors may have augmented the mesolimbic dopaminergic pathway , which was suppressed by risperidone , causing spontaneous ejaculations in this patient .

Example answer:
{"entities": [{"text": "agonistic", "type": "Chemical"}, {"text": "aripiprazole", "type": "Chemical"}, {"text": "D2 receptors", "type": "Chemical"}, {"text": "pathway", "type": "BiologicFunction"}, {"text": "risperidone", "type": "Chemical"}, {"text": "ejaculations", "type": "BiologicFunction"}]}

Example input:
Sentence: Spontaneous Ejaculations Associated with Aripiprazole Sexual side effects are common with antipsychotic use .

Example answer:
{"entities": [{"text": "Ejaculations", "type": "BiologicFunction"}, {"text": "Aripiprazole", "type": "Chemical"}, {"text": "side effects", "type": "BiologicFunction"}, {"text": "antipsychotic", "type": "Chemical"}]}

Example input:
Sentence: We report the case of a man who had spontaneous ejaculations after stopping risperidone and starting 30 mg / day aripiprazole .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "man", "type": "PopulationGroup"}, {"text": "ejaculations", "type": "BiologicFunction"}, {"text": "risperidone", "type": "Chemical"}, {"text": "aripiprazole", "type": "Chemical"}]}

Input:
Sentence: Spontaneous ejaculations ceased 3 days after decreasing the aripiprazole dose to 15 mg / day .

## Item MedMentions:test:4067
Example input:
Sentence: Results first show that the mechanical moduli of the membranes have to be adjusted as a function of the model used .

Example answer:
{"entities": [{"text": "Results", "type": "Finding"}, {"text": "membranes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We used rheology to measure the strain - stiffening behavior of the clots and determined the fiber properties by modeling the clots as semi - flexible polymer networks .

Example answer:
{"entities": [{"text": "clots", "type": "BiologicFunction"}, {"text": "fiber", "type": "AnatomicalStructure"}, {"text": "modeling", "type": "ResearchActivity"}]}

Example input:
Sentence: We have established a high throughput method of quantifying dynamic changes in the mechanical properties of SC upon drying .

Example answer:
{"entities": [{"text": "SC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: These gels with tunable mechanical properties can be injected into defect sites to form scaffolds for cell growth and tissue repair , and they do not require any separate seeding of cells before injection , thus eliminating the need for cell harvesting and cell maintenance .

Example answer:
{"entities": [{"text": "gels", "type": "Chemical"}, {"text": "scaffolds", "type": "Chemical"}, {"text": "cell growth", "type": "BiologicFunction"}, {"text": "tissue repair", "type": "BiologicFunction"}, {"text": "seeding of cells", "type": "BiologicFunction"}, {"text": "injection", "type": "HealthCareActivity"}, {"text": "cell harvesting", "type": "BiologicFunction"}, {"text": "cell maintenance", "type": "BiologicFunction"}]}

Example input:
Sentence: Data showed that hyposmotic solutions significantly triggered increases in cytosolic calcium concentration ( [ Ca ( 2 + ) ] c ) of synoviocytes .

Example answer:
{"entities": [{"text": "cytosolic", "type": "AnatomicalStructure"}, {"text": "calcium", "type": "Chemical"}, {"text": "synoviocytes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Extracellular matrix architectures provided insights about phallic glans material properties and how they may affect tissue strength and flexibility during inflation and in response to copulatory forces .

Example answer:
{"entities": [{"text": "Extracellular matrix", "type": "AnatomicalStructure"}, {"text": "phallic glans", "type": "AnatomicalStructure"}, {"text": "tissue", "type": "AnatomicalStructure"}]}

Example input:
Sentence: This technique can be employed to quantify changes in the drying behavior and mechanical properties of SC with cosmetic cleanser and moisturizer treatments .

Example answer:
{"entities": [{"text": "SC", "type": "AnatomicalStructure"}, {"text": "cleanser", "type": "Chemical"}, {"text": "moisturizer", "type": "Chemical"}, {"text": "treatments", "type": "HealthCareActivity"}]}

Example input:
Sentence: The soft tissue was modeled as an elastic layer bonded to a rigid base .

Example answer:
{"entities": [{"text": "soft tissue", "type": "AnatomicalStructure"}, {"text": "modeled", "type": "ResearchActivity"}]}

Example input:
Sentence: How do wettability , zeta potential and hydroxylation degree affect the biological response of biomaterials ? It is well known that composition , electric charge , wettability and roughness of implant surfaces have great influence on their interaction with the biological fluids and tissues , but systematic studies of different materials in the same experimental conditions are still lacking in the scientific literature .

Example answer:
{"entities": [{"text": "hydroxylation degree", "type": "Finding"}, {"text": "biological response", "type": "Finding"}, {"text": "biomaterials", "type": "Chemical"}, {"text": "implant", "type": "MedicalDevice"}, {"text": "surfaces", "type": "SpatialConcept"}, {"text": "biological fluids", "type": "BodySubstance"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "systematic studies", "type": "ResearchActivity"}, {"text": "scientific literature", "type": "IntellectualProduct"}]}

Example input:
Sentence: This study revealed the important synergistic roles of cellular contractility and tissue stiffness in the maintenance of fibrotic tissue and suggests a new therapeutic principle for fibrosis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "cellular contractility", "type": "BiologicFunction"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "fibrosis", "type": "BiologicFunction"}]}

Input:
Sentence: The effects of several parameters on the solution behaviors are reported , and a method for applying the solution to determine the mechanical properties of soft tissues is suggested .

## Item MedMentions:test:4081
Example input:
Sentence: With the recent conclusion of Phase 3 of the Social Cognition Psychometric Evaluation ( SCOPE ) Study , the most psychometrically sound measures of social cognition have been identified .

Example answer:
{"entities": [{"text": "Psychometric Evaluation ( SCOPE ) Study", "type": "HealthCareActivity"}, {"text": "psychometrically", "type": "HealthCareActivity"}, {"text": "sound measures", "type": "HealthCareActivity"}]}

Example input:
Sentence: Thresholds were the most effective outcome measure to both track progression and to distinguish between MAV and Ménière 's patients .

Example answer:
{"entities": [{"text": "MAV", "type": "Finding"}, {"text": "Ménière 's", "type": "BiologicFunction"}]}

Example input:
Sentence: All patients were evaluated by anamnesis , physical examination , and self - report quality - of - life questionnaires .

Example answer:
{"entities": [{"text": "evaluated", "type": "HealthCareActivity"}, {"text": "anamnesis", "type": "BiologicFunction"}, {"text": "physical examination", "type": "HealthCareActivity"}, {"text": "self - report", "type": "ResearchActivity"}, {"text": "quality - of - life questionnaires", "type": "IntellectualProduct"}]}

Example input:
Sentence: We used the GRADE approach to assess the quality of evidence .

Example answer:
{"entities": []}

Example input:
Sentence: Recently , it has been suggested that conscious perception might arise from the dynamic interplay of functionally specialized but widely distributed cortical areas .

Example answer:
{"entities": [{"text": "conscious", "type": "BiologicFunction"}, {"text": "perception", "type": "BiologicFunction"}, {"text": "cortical areas", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The approach also proves explanatorily advantageous , as it enables us not only to draw attention to certain new and important differences in respect of subjective measures of awareness and to justify how a given creature may be ranked higher in one dimension of consciousness and lower in terms of another , but also allows for innovative explanations of a variety of well - known phenomena ( amongst these , the interpretations of blindsight and locked - in syndrome will be briefly outlined here ) .

Example answer:
{"entities": [{"text": "approach", "type": "SpatialConcept"}, {"text": "attention", "type": "BiologicFunction"}, {"text": "awareness", "type": "BiologicFunction"}, {"text": "creature", "type": "Eukaryote"}, {"text": "ranked", "type": "IntellectualProduct"}, {"text": "consciousness", "type": "BiologicFunction"}, {"text": "innovative explanations", "type": "IntellectualProduct"}, {"text": "interpretations", "type": "IntellectualProduct"}, {"text": "locked - in syndrome", "type": "BiologicFunction"}]}

Example input:
Sentence: One of the basic disagreements present in the continuing debate about consciousness pertains to its gradational nature .

Example answer:
{"entities": [{"text": "consciousness", "type": "BiologicFunction"}, {"text": "gradational", "type": "IntellectualProduct"}]}

Example input:
Sentence: It is hoped that such a four - dimensional approach will help to clarify and justify claims about the hierarchical nature of consciousness .

Example answer:
{"entities": [{"text": "four - dimensional", "type": "SpatialConcept"}, {"text": "consciousness", "type": "BiologicFunction"}]}

Example input:
Sentence: Four - Dimensional Graded Consciousness Both the multidimensional phenomenon and the polysemous notion of consciousness continue to prove resistant to consistent measurement and unambiguous definition .

Example answer:
{"entities": [{"text": "Four - Dimensional", "type": "SpatialConcept"}, {"text": "Graded", "type": "IntellectualProduct"}, {"text": "Consciousness", "type": "BiologicFunction"}, {"text": "multidimensional", "type": "SpatialConcept"}, {"text": "consciousness", "type": "BiologicFunction"}, {"text": "unambiguous definition", "type": "IntellectualProduct"}]}

Example input:
Sentence: Consequently , consciousness may be said to vary with respect to phenomenal quality , semantic abstraction , physiological complexity , and functional usefulness .

Example answer:
{"entities": [{"text": "consciousness", "type": "BiologicFunction"}, {"text": "complexity", "type": "BiologicFunction"}]}

Input:
Sentence: We therefore focus on the question of what it is , exactly , that is or could be graded in cases of consciousness , and how we can measure it .

## Item MedMentions:test:3900
Example input:
Sentence: The availability of the genome sequence will provide a better understanding of strain MPKL 26 ( T ) and the genus Sinomonas .

Example answer:
{"entities": [{"text": "genome sequence", "type": "SpatialConcept"}, {"text": "genus Sinomonas", "type": "Bacterium"}]}

Example input:
Sentence: Here we report the first demonstration of single contig genome assembly using Oxford Nanopore native barcoding when applied to a multiplexed library of 12 samples and combined with existing Illumina short - read data .

Example answer:
{"entities": [{"text": "report", "type": "IntellectualProduct"}, {"text": "single contig genome assembly", "type": "SpatialConcept"}, {"text": "Oxford Nanopore", "type": "Organization"}, {"text": "barcoding", "type": "ResearchActivity"}, {"text": "multiplexed library", "type": "AnatomicalStructure"}, {"text": "short - read data", "type": "IntellectualProduct"}]}

Example input:
Sentence: Use of single molecule sequencing for comparative genomics of an environmental and a clinical isolate of Clostridium difficile ribotype 078 How the pathogen Clostridium difficile might survive , evolve and be transferred between reservoirs within the natural environment is poorly understood .

Example answer:
{"entities": [{"text": "genomics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "environmental", "type": "SpatialConcept"}, {"text": "isolate", "type": "Chemical"}, {"text": "Clostridium difficile", "type": "Bacterium"}, {"text": "ribotype 078", "type": "Finding"}, {"text": "reservoirs", "type": "SpatialConcept"}, {"text": "natural environment", "type": "SpatialConcept"}]}

Example input:
Sentence: In this work , we have used deep metagenomic sequencing to assemble eight complete genomes of the first tailed phages that infect freshwater Actinobacteria .

Example answer:
{"entities": [{"text": "metagenomic sequencing", "type": "ResearchActivity"}, {"text": "genomes", "type": "AnatomicalStructure"}, {"text": "infect", "type": "Finding"}, {"text": "Actinobacteria", "type": "Bacterium"}]}

Example input:
Sentence: Dramatic improvements in bacterial whole genome sequencing ( WGS ) offer new opportunities for personalising the treatment of S .

Example answer:
{"entities": [{"text": "bacterial", "type": "Bacterium"}, {"text": "whole genome sequencing", "type": "ResearchActivity"}, {"text": "WGS", "type": "ResearchActivity"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "S .", "type": "BiologicFunction"}]}

Example input:
Sentence: To address this , single molecule real time ( SMRT ) sequencing was used in this study as it produces high quality genome sequences , with resolution of repeat regions ( including those found in mobile elements ) and can generate data to determine methylation modifications across the sequence ( the methylome ) .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "genome sequences", "type": "SpatialConcept"}, {"text": "mobile elements", "type": "Chemical"}, {"text": "methylation", "type": "BiologicFunction"}, {"text": "sequence", "type": "SpatialConcept"}]}

Example input:
Sentence: Using a hybrid assembly of existing short read and barcoded long read sequences from multiplexed data , we completed a genome of the S .

Example answer:
{"entities": [{"text": "assembly", "type": "SpatialConcept"}, {"text": "barcoded long read sequences", "type": "SpatialConcept"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: The long - read data represented only ~5 - 10 % of an average MinION ( TM ) run ( ~7x genomic coverage ) , but , using standard tools , this was sufficient to complete the circular chromosome of S .

Example answer:
{"entities": [{"text": "long - read data", "type": "IntellectualProduct"}, {"text": "MinION ( TM )", "type": "MedicalDevice"}, {"text": "genomic", "type": "AnatomicalStructure"}, {"text": "tools", "type": "IntellectualProduct"}, {"text": "circular chromosome", "type": "AnatomicalStructure"}, {"text": "S .", "type": "Bacterium"}]}

Example input:
Sentence: The use of Oxford Nanopore native barcoding for complete genome assembly The Oxford Nanopore Technologies MinION ( TM ) is a mobile DNA sequencer that can produce long read sequences with a short turn - around time .

Example answer:
{"entities": [{"text": "Oxford Nanopore", "type": "Organization"}, {"text": "barcoding", "type": "ResearchActivity"}, {"text": "genome assembly", "type": "SpatialConcept"}, {"text": "Oxford Nanopore Technologies", "type": "Organization"}, {"text": "MinION ( TM )", "type": "MedicalDevice"}, {"text": "long read sequences", "type": "SpatialConcept"}]}

Example input:
Sentence: The ability to complete multiple genomes , for which short - read data is already available , from a single MinION ( TM ) run is set to impact on our understanding of accessory genome content , plasmid diversity and genome rearrangements .

Example answer:
{"entities": [{"text": "genomes", "type": "AnatomicalStructure"}, {"text": "short - read data", "type": "IntellectualProduct"}, {"text": "available", "type": "Finding"}, {"text": "MinION ( TM )", "type": "MedicalDevice"}, {"text": "understanding", "type": "BiologicFunction"}, {"text": "genome content", "type": "AnatomicalStructure"}, {"text": "plasmid", "type": "Chemical"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "rearrangements", "type": "BiologicFunction"}]}

Input:
Sentence: This paves the way for the closure of multiple bacterial genomes from a single MinION ( TM ) sequencing run , given the availability of existing short - read data .

## Item MedMentions:test:3905
Example input:
Sentence: Prolyl - 4 - hydroxylase 2 and 3 coregulate murine erythropoietin in brain pericytes A classic response to systemic hypoxia is the increased production of red blood cells due to hypoxia - inducible factor ( HIF ) - mediated induction of erythropoietin ( EPO ) .

Example answer:
{"entities": [{"text": "Prolyl - 4 - hydroxylase 2", "type": "Chemical"}, {"text": "3", "type": "Chemical"}, {"text": "murine", "type": "Chemical"}, {"text": "erythropoietin", "type": "Chemical"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "pericytes", "type": "AnatomicalStructure"}, {"text": "response", "type": "Finding"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "production of red blood cells", "type": "BiologicFunction"}, {"text": "hypoxia - inducible factor", "type": "Chemical"}, {"text": "HIF", "type": "Chemical"}, {"text": "EPO", "type": "Chemical"}]}

Example input:
Sentence: Investigation of argyrophilic nucleolar organizing region Ischemia / reperfusion ( I / R ) injury is a complex event frequently observed in vascular surgery and can cause functional and structural cell damage .

Example answer:
{"entities": [{"text": "argyrophilic", "type": "AnatomicalStructure"}, {"text": "nucleolar organizing region", "type": "AnatomicalStructure"}, {"text": "Ischemia / reperfusion ( I / R ) injury", "type": "InjuryOrPoisoning"}, {"text": "vascular surgery", "type": "HealthCareActivity"}, {"text": "functional", "type": "BiologicFunction"}, {"text": "structural", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Hif - 1α Overexpression Improves Transplanted Bone Mesenchymal Stem Cells Survival in Rat MCAO Stroke Model Bone mesenchymal stem cells ( BMSCs ) death after transplantation is a serious obstacle impacting on the outcome of cell therapy for cerebral infarction .

Example answer:
{"entities": [{"text": "Hif - 1α", "type": "Chemical"}, {"text": "Overexpression", "type": "BiologicFunction"}, {"text": "Improves", "type": "Finding"}, {"text": "Transplanted Bone Mesenchymal Stem Cells", "type": "HealthCareActivity"}, {"text": "Survival", "type": "BiologicFunction"}, {"text": "Rat MCAO Stroke Model", "type": "BiologicFunction"}, {"text": "Bone mesenchymal stem cells", "type": "AnatomicalStructure"}, {"text": "BMSCs", "type": "AnatomicalStructure"}, {"text": "death", "type": "BiologicFunction"}, {"text": "transplantation", "type": "HealthCareActivity"}, {"text": "cell therapy", "type": "HealthCareActivity"}, {"text": "cerebral infarction", "type": "BiologicFunction"}]}

Example input:
Sentence: Here we aimed to further elucidate HIF - 1α protein expression in serrated and non - serrated colorectal carcinomas ( CRCs ) and their precursor lesions and its association with vascular endothelial growth factor ( VEGF ) and microvascular density ( MVD ) .

Example answer:
{"entities": [{"text": "HIF - 1α", "type": "Chemical"}, {"text": "protein expression", "type": "BiologicFunction"}, {"text": "serrated", "type": "BiologicFunction"}, {"text": "non - serrated colorectal carcinomas", "type": "BiologicFunction"}, {"text": "CRCs", "type": "BiologicFunction"}, {"text": "precursor lesions", "type": "Finding"}, {"text": "vascular endothelial growth factor", "type": "Chemical"}, {"text": "VEGF", "type": "Chemical"}]}

Example input:
Sentence: Our objective was to determine the role of HMGB1 and the degree of activation of TLR -related signal transduction pathways in hypoxia / reoxygenation ( H / R ) - induced proinflammatory cytokine production and intra - islet graft inflammation .

Example answer:
{"entities": [{"text": "HMGB1", "type": "Chemical"}, {"text": "TLR", "type": "Chemical"}, {"text": "signal transduction pathways", "type": "BiologicFunction"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "reoxygenation", "type": "HealthCareActivity"}, {"text": "H", "type": "BiologicFunction"}, {"text": "R", "type": "HealthCareActivity"}, {"text": "proinflammatory cytokine production", "type": "BiologicFunction"}, {"text": "intra - islet", "type": "AnatomicalStructure"}, {"text": "graft", "type": "Chemical"}, {"text": "inflammation", "type": "BiologicFunction"}]}

Example input:
Sentence: During HOV , tissue hypoxia was aggravated in the myocardium , brain , and kidneys , whereas tissue oxygenation of the liver and intestine was not influenced by volume status .

Example answer:
{"entities": [{"text": "HOV", "type": "Finding"}, {"text": "hypoxia", "type": "BiologicFunction"}, {"text": "myocardium", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "kidneys", "type": "AnatomicalStructure"}, {"text": "liver", "type": "AnatomicalStructure"}, {"text": "intestine", "type": "AnatomicalStructure"}, {"text": "volume status", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Right ventricular ( RV ) dysfunction , paradoxical septal motion , and higher RV systolic pressure remained the only variables significantly associated with poor survival .

Example answer:
{"entities": [{"text": "Right ventricular ( RV ) dysfunction", "type": "BiologicFunction"}, {"text": "paradoxical septal motion", "type": "Finding"}, {"text": "higher RV systolic pressure", "type": "Finding"}]}

Example input:
Sentence: Right Ventricular Response During Exercise in Patients with Chronic Obstructive Pulmonary Disease Right ventricular ( RV ) pump function is of essential clinical and prognostic importance in a variety of heart and lung diseases .

Example answer:
{"entities": [{"text": "Right Ventricular", "type": "AnatomicalStructure"}, {"text": "Chronic Obstructive Pulmonary Disease", "type": "BiologicFunction"}, {"text": "Right ventricular", "type": "AnatomicalStructure"}, {"text": "RV", "type": "AnatomicalStructure"}, {"text": "pump function", "type": "BiologicFunction"}, {"text": "prognostic", "type": "IntellectualProduct"}, {"text": "heart", "type": "BiologicFunction"}, {"text": "lung diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: High Alt Med Biol . 17 : 342 - 352 , 2016 . - a sustained work load on the right heart on ascent to high altitudes promotes right ventricular hypertrophy ( RVH ) , which eventually undergoes decompensation and promotes pathological damage .

Example answer:
{"entities": [{"text": "right heart", "type": "SpatialConcept"}, {"text": "right ventricular hypertrophy", "type": "BiologicFunction"}, {"text": "RVH", "type": "BiologicFunction"}, {"text": "decompensation", "type": "Finding"}, {"text": "pathological damage", "type": "BiologicFunction"}]}

Example input:
Sentence: After culture , the cardiac patch was implanted to repair a defect with a diameter of 2 mm created in the right ventricular outflow tract ( RVOT ) wall .

Example answer:
{"entities": [{"text": "cardiac patch", "type": "MedicalDevice"}, {"text": "implanted", "type": "HealthCareActivity"}, {"text": "repair", "type": "HealthCareActivity"}, {"text": "right ventricular outflow tract ( RVOT ) wall", "type": "AnatomicalStructure"}]}

Input:
Sentence: Right ventricle outflow tract ( RVOT ) tissues were collected during the surgery to assess hypoxia - inducible factor ( Hif ) - 1α and other signalling proteins .

## Item MedMentions:test:3460
Example input:
Sentence: We examined the therapeutic and preventive potential of andrographolide , which is a lactone diterpenoid from Andrographis paniculata , and focused on the Kelch - like ECH - associated protein 1 ( Keap1 ) / nuclear factor ( erythroid - derived 2 ) - like 2 ( Nrf2 ) - mediated heme oxygenase ( HO ) - 1 - inducing effects and the inhibitory activity of amyloid beta ( Aβ ) 42 - induced microglial activation related to Nrf2 and nuclear factor κB ( NF - κB ) - mediated inflammatory responses .

Example answer:
{"entities": [{"text": "andrographolide", "type": "Chemical"}, {"text": "lactone diterpenoid", "type": "Chemical"}, {"text": "Andrographis paniculata", "type": "Eukaryote"}, {"text": "Kelch - like ECH - associated protein 1", "type": "Chemical"}, {"text": "Keap1", "type": "Chemical"}, {"text": "nuclear factor ( erythroid - derived 2 ) - like 2", "type": "Chemical"}, {"text": "Nrf2", "type": "Chemical"}, {"text": "heme oxygenase", "type": "Chemical"}, {"text": "( HO ) - 1", "type": "Chemical"}, {"text": "amyloid beta ( Aβ ) 42", "type": "Chemical"}, {"text": "microglial activation", "type": "BiologicFunction"}, {"text": "nuclear factor κB", "type": "Chemical"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "inflammatory responses", "type": "BiologicFunction"}]}

Example input:
Sentence: The major menaquinone were MK - 8 ( H2 ) ( 72 % ) and MK - 9 ( H2 ) ( 28 % ) , and the predominant cellular fatty acids were anteiso - C15 : 0 , iso - C15 : 0 and anteiso - C17 : 0 .

Example answer:
{"entities": [{"text": "menaquinone", "type": "Chemical"}, {"text": "MK - 8 ( H2 )", "type": "Chemical"}, {"text": "MK - 9 ( H2 )", "type": "Chemical"}, {"text": "cellular fatty acids", "type": "Chemical"}, {"text": "anteiso - C15 : 0", "type": "Chemical"}, {"text": "iso - C15 : 0", "type": "Chemical"}, {"text": "anteiso - C17 : 0", "type": "Chemical"}]}

Example input:
Sentence: Purification of benzoic acid extracted from the extracellular fermentation medium was confirmed by nuclear magnetic resonance ( NMR ) , and infrared and mass spectral data revealed minimum inhibitory concentration ( MIC ) values of 10 , 20 , 10 , 5 , and 10 mg mL ( - 1 ) for Aspergillus fumigates , Curvularia lunata , Fusarium oxysporum , Gibberella moniliformis , and Penicillium chrysogenum , respectively .

Example answer:
{"entities": [{"text": "Purification", "type": "HealthCareActivity"}, {"text": "benzoic acid", "type": "Chemical"}, {"text": "extracellular", "type": "AnatomicalStructure"}, {"text": "fermentation", "type": "BiologicFunction"}, {"text": "medium", "type": "Chemical"}, {"text": "nuclear magnetic resonance", "type": "HealthCareActivity"}, {"text": "NMR", "type": "HealthCareActivity"}, {"text": "infrared", "type": "HealthCareActivity"}, {"text": "mass spectral", "type": "HealthCareActivity"}, {"text": "minimum inhibitory concentration", "type": "HealthCareActivity"}, {"text": "MIC", "type": "HealthCareActivity"}, {"text": "Aspergillus fumigates", "type": "Eukaryote"}, {"text": "Curvularia lunata", "type": "Eukaryote"}, {"text": "Fusarium oxysporum", "type": "Eukaryote"}, {"text": "Gibberella moniliformis", "type": "Eukaryote"}, {"text": "Penicillium chrysogenum", "type": "Eukaryote"}]}

Example input:
Sentence: The root cultures likewise produced the known alkaloids dioncophylline A ( 8 ) , 5 ' - O - demethyldioncophylline A ( 9 ) , dioncopeltine A ( 10 ) , habropetaline A ( 11 ) , and 5 ' - O - methyldioncophylline D ( 12a / b ) , the naphthalene glucoside plumbaside A ( 2 ) , and the naphthoquinones plumbagin ( 13 ) , droserone ( 14 ) , and 8 - hydroxydroserone ( 15 ) .

Example answer:
{"entities": [{"text": "root", "type": "Eukaryote"}, {"text": "cultures", "type": "HealthCareActivity"}, {"text": "alkaloids", "type": "Chemical"}, {"text": "dioncophylline A", "type": "Chemical"}, {"text": "5 ' - O - demethyldioncophylline A", "type": "Chemical"}, {"text": "dioncopeltine A", "type": "Chemical"}, {"text": "habropetaline A", "type": "Chemical"}, {"text": "5 ' - O - methyldioncophylline D", "type": "Chemical"}, {"text": "naphthalene glucoside plumbaside A", "type": "Chemical"}, {"text": "naphthoquinones plumbagin", "type": "Chemical"}, {"text": "droserone", "type": "Chemical"}, {"text": "8 - hydroxydroserone", "type": "Chemical"}]}

Example input:
Sentence: Extracts of the endophytic fungus cultured on potato dextrose agar were purified using several chromatographic techniques .

Example answer:
{"entities": [{"text": "endophytic fungus", "type": "Eukaryote"}, {"text": "potato dextrose agar", "type": "Chemical"}]}

Example input:
Sentence: New metabolites from the sponge -derived fungus Aspergillus sydowii J05B - 7F - 4 Two new metabolites , diorcinolic acid ( 1 ) and β - d - glucopyranosyl aspergillusene A ( 8 ) , together with six diphenylethers ( 2 - 7 ) , a diketopiperazine ( 9 ) , a chromone ( 10 ) and a xanthone ( 11 ) were isolated from the fungus Aspergillus sydowii derived from the marine sponge Stelletta sp .

Example answer:
{"entities": [{"text": "metabolites", "type": "Chemical"}, {"text": "sponge", "type": "Eukaryote"}, {"text": "fungus", "type": "Eukaryote"}, {"text": "Aspergillus sydowii J05B - 7F - 4", "type": "Eukaryote"}, {"text": "diorcinolic acid", "type": "Chemical"}, {"text": "β - d - glucopyranosyl aspergillusene A", "type": "Chemical"}, {"text": "diphenylethers", "type": "Chemical"}, {"text": "diketopiperazine", "type": "Chemical"}, {"text": "chromone", "type": "Chemical"}, {"text": "xanthone", "type": "Chemical"}, {"text": "Aspergillus sydowii", "type": "Eukaryote"}, {"text": "marine sponge", "type": "Eukaryote"}, {"text": "Stelletta sp", "type": "Eukaryote"}]}

Example input:
Sentence: Herein , this study reports the isolation and characterization of secondary metabolites from an endophytic fungus Penicillium polonicum ( NFW9 ) associated with Taxus fuana .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "secondary metabolites", "type": "Chemical"}, {"text": "endophytic fungus", "type": "Eukaryote"}, {"text": "Penicillium polonicum", "type": "Eukaryote"}, {"text": "NFW9", "type": "Eukaryote"}, {"text": "Taxus fuana", "type": "Eukaryote"}]}

Example input:
Sentence: The endophytic fungus Penicillium polonicum of Taxus fuana is capable of producing biologically active natural compounds .

Example answer:
{"entities": [{"text": "endophytic fungus", "type": "Eukaryote"}, {"text": "Penicillium polonicum", "type": "Eukaryote"}, {"text": "Taxus fuana", "type": "Eukaryote"}, {"text": "biologically active natural compounds", "type": "Chemical"}]}

Example input:
Sentence: Bioactive Constituents from an Endophytic Fungus , Penicillium polonicum NFW9 , associated with Taxus fauna Endophytic fungi are being recognized as vital and untapped sources of a variety of structurally novel and unique bioactive secondary metabolites in the field of natural products drug discovery .

Example answer:
{"entities": [{"text": "Endophytic Fungus", "type": "Eukaryote"}, {"text": "Penicillium polonicum", "type": "Eukaryote"}, {"text": "NFW9", "type": "Eukaryote"}, {"text": "Taxus fauna", "type": "Eukaryote"}, {"text": "Endophytic fungi", "type": "Eukaryote"}, {"text": "vital and untapped sources", "type": "Finding"}, {"text": "secondary metabolites", "type": "Chemical"}, {"text": "natural products", "type": "Chemical"}, {"text": "drug discovery", "type": "ResearchActivity"}]}

Example input:
Sentence: γ - Butenolide and furanone derivatives from the soil -derived fungus Aspergillus sclerotiorum PSU - RSPG178 Chromatographic separation of the broth extract of the soil -derived fungus Aspergillus sclerotiorum PSU - RSPG178 resulted in isolation of four γ - butenolide - furanone dimers , aspersclerotiorones A - D , a furanone derivative , aspersclerotiorone E , and two γ - butenolide derivatives , aspersclerotiorones F and G , together with six known compounds , penicillic acid , dihydropenicillic acid , 5 , 6 - dihydro - 6 - hydroxypenicillic acid , 6 - methoxy - 5 , 6 - dihydropenicillic acid , coculnol and ( 4R , 5R ) - 4 , 5 - dihydroxy - 3 - methoxy - 5 - methylcyclohex - 2 - en - 1 - one .

Example answer:
{"entities": [{"text": "γ - Butenolide", "type": "Chemical"}, {"text": "furanone derivatives", "type": "Chemical"}, {"text": "fungus", "type": "Eukaryote"}, {"text": "Aspergillus sclerotiorum", "type": "Eukaryote"}, {"text": "PSU - RSPG178", "type": "Eukaryote"}, {"text": "Chromatographic separation", "type": "HealthCareActivity"}, {"text": "broth", "type": "Chemical"}, {"text": "γ - butenolide - furanone dimers", "type": "Chemical"}, {"text": "aspersclerotiorones A - D", "type": "Chemical"}, {"text": "furanone derivative", "type": "Chemical"}, {"text": "aspersclerotiorone E", "type": "Chemical"}, {"text": "γ - butenolide derivatives", "type": "Chemical"}, {"text": "aspersclerotiorones F", "type": "Chemical"}, {"text": "G", "type": "Chemical"}, {"text": "penicillic acid", "type": "Chemical"}, {"text": "dihydropenicillic acid", "type": "Chemical"}, {"text": "5 , 6 - dihydro - 6 - hydroxypenicillic acid", "type": "Chemical"}, {"text": "6 - methoxy - 5 , 6 - dihydropenicillic acid", "type": "Chemical"}, {"text": "coculnol", "type": "Chemical"}, {"text": "( 4R , 5R ) - 4 , 5 - dihydroxy - 3 - methoxy - 5 - methylcyclohex - 2 - en - 1 - one", "type": "Chemical"}]}

Input:
Sentence: Bioactivity - directed fractionation of the ethyl acetate extract of a fermentation culture of an endophytic fungus , Penicillium polonicum led to the isolation of a dimeric anthraquinone , ( R ) - 1 , 1 ' , 3 , 3 ' , 5 , 5 ' - hexahydroxy - 7 , 7 ' - dimethyl [ 2 , 2 ' - bianthracene ] - 9 , 9 ' , 10 , 10 ' - tetraone ( 1 ) , a steroidal furanoid ( - ) - wortmannolone ( 2 ) , along with three other compounds ( 3  4 ) .

## Item MedMentions:test:3994
Example input:
Sentence: This association was strongest for pts , where primary tumour tissue was examined ( PFS : 6 . 7 vs 10 .

Example answer:
{"entities": [{"text": "primary tumour tissue", "type": "AnatomicalStructure"}, {"text": "examined", "type": "Finding"}]}

Example input:
Sentence: The relationship between histological prostatitis and lower urinary tract symptoms and sexual function This prospective analysis assessed the effect of histological prostatitis on lower urinary tract functions and sexual function .

Example answer:
{"entities": [{"text": "prostatitis", "type": "BiologicFunction"}, {"text": "lower urinary tract symptoms", "type": "Finding"}, {"text": "sexual function", "type": "BiologicFunction"}, {"text": "prospective analysis", "type": "ResearchActivity"}, {"text": "lower urinary tract", "type": "BodySystem"}]}

Example input:
Sentence: Histopathological findings of skin biopsy , adrenal and bone marrow aspirates raised suspicion , whereas fungal cultures confirmed Histoplasma infection .

Example answer:
{"entities": [{"text": "Histopathological findings", "type": "Finding"}, {"text": "skin biopsy", "type": "HealthCareActivity"}, {"text": "adrenal", "type": "AnatomicalStructure"}, {"text": "bone marrow aspirates", "type": "BodySubstance"}, {"text": "suspicion", "type": "BiologicFunction"}, {"text": "fungal cultures", "type": "HealthCareActivity"}, {"text": "confirmed", "type": "Finding"}, {"text": "Histoplasma infection", "type": "BiologicFunction"}]}

Example input:
Sentence: Histological prostatitis notably affected sexual function of patients and may serve as a major risk factor for sexual dysfunction while having little effect on lower urinary tract symptoms .

Example answer:
{"entities": [{"text": "prostatitis", "type": "BiologicFunction"}, {"text": "sexual function", "type": "BiologicFunction"}, {"text": "risk factor", "type": "Finding"}, {"text": "sexual dysfunction", "type": "BiologicFunction"}, {"text": "lower urinary tract symptoms", "type": "Finding"}]}

Example input:
Sentence: The patients were separated into two groups as histologically observed prostatitis ( Group A ) and no prostatitis ( Group B ) according to the biopsy outcomes .

Example answer:
{"entities": [{"text": "prostatitis", "type": "BiologicFunction"}, {"text": "no prostatitis", "type": "Finding"}, {"text": "biopsy", "type": "HealthCareActivity"}]}

Example input:
Sentence: A retrospective analysis of histopathological records of 1 , 181 prostatic specimens received in the pathology department was done over a period of 13 years ( January 2003 to January 2016 ) .

Example answer:
{"entities": [{"text": "retrospective analysis", "type": "ResearchActivity"}, {"text": "histopathological records", "type": "IntellectualProduct"}, {"text": "prostatic specimens", "type": "BodySubstance"}, {"text": "pathology department", "type": "Organization"}]}

Example input:
Sentence: Among these , nonspecific granulomatous prostatitis ( n = 10 ) was the most common followed by tubercular prostatitis ( n = 5 ) , posttransurethral resection of the prostate ( n = 3 ) , allergic ( n = 2 ) , and xanthogranulomatous prostatitis ( n = 2 ) .

Example answer:
{"entities": [{"text": "granulomatous prostatitis", "type": "BiologicFunction"}, {"text": "tubercular prostatitis", "type": "BiologicFunction"}, {"text": "posttransurethral resection", "type": "HealthCareActivity"}, {"text": "prostate", "type": "AnatomicalStructure"}, {"text": "xanthogranulomatous prostatitis", "type": "BiologicFunction"}]}

Example input:
Sentence: However , assigning an etiologic cause to the wide spectrum of granulomas in granulomatous prostatitis requires a pathologist 's expertise and proper clinical correlation for appropriate patient management .

Example answer:
{"entities": [{"text": "granulomas", "type": "BiologicFunction"}, {"text": "granulomatous prostatitis", "type": "BiologicFunction"}, {"text": "pathologist 's", "type": "ProfessionalOrOccupationalGroup"}, {"text": "clinical correlation", "type": "ResearchActivity"}, {"text": "patient management", "type": "HealthCareActivity"}]}

Example input:
Sentence: Despite present - day advances in imaging modalities and serological investigations , it is virtually impossible to identify granulomatous prostatitis clinically .

Example answer:
{"entities": [{"text": "serological investigations", "type": "HealthCareActivity"}, {"text": "granulomatous prostatitis", "type": "BiologicFunction"}]}

Example input:
Sentence: Twenty - two cases of granulomatous prostatitis were identified , accounting for an incidence of 1 . 86 % .

Example answer:
{"entities": [{"text": "granulomatous prostatitis", "type": "BiologicFunction"}]}

Input:
Sentence: All histologically proven cases of granulomatous prostatitis were retrieved , and relevant clinical data were collected from patients ' records .

## Item MedMentions:test:3914
Example input:
Sentence: The Eastern Iberian System , where this insect uses both host - plants , harboured the highest level of genetic diversity .

Example answer:
{"entities": [{"text": "insect", "type": "Eukaryote"}]}

Example input:
Sentence: isabellae likely diverged before the Last Glacial Maximum and geographically separated the species into a " southern " ( Central and Southern Iberian clusters ) and a " northern " lineage ( Eastern Iberian , Pyrenean and French Alpine clusters ) .

Example answer:
{"entities": [{"text": "isabellae", "type": "Eukaryote"}, {"text": "geographically", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "southern", "type": "SpatialConcept"}, {"text": "northern", "type": "SpatialConcept"}]}

Example input:
Sentence: On the post - glacial spread of human commensal Arabidopsis thaliana Recent work has shown that Arabidopsis thaliana contains genetic groups originating from different ice age refugia , with one particular group comprising over 95 % of the current worldwide population .

Example answer:
{"entities": [{"text": "human", "type": "Eukaryote"}, {"text": "Arabidopsis thaliana", "type": "Eukaryote"}]}

Example input:
Sentence: However , in confluent high - biomass regions , Rothia occurred in islands whereas Haemophilus was distributed throughout .

Example answer:
{"entities": [{"text": "regions", "type": "SpatialConcept"}, {"text": "Rothia", "type": "Bacterium"}, {"text": "Haemophilus", "type": "Bacterium"}]}

Example input:
Sentence: Both species co - occur at a site in southern Italy characterized by a Mediterranean climate .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "site", "type": "SpatialConcept"}, {"text": "southern", "type": "SpatialConcept"}, {"text": "Italy", "type": "SpatialConcept"}, {"text": "Mediterranean", "type": "SpatialConcept"}]}

Example input:
Sentence: The analysis showed a distinct separation of the southern refugia into a western cluster embracing Iberia and an eastern group including the Balkans and Italy , which determined the postglacial recolonization of Central Europe .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "Iberia", "type": "SpatialConcept"}, {"text": "eastern", "type": "SpatialConcept"}, {"text": "Balkans", "type": "SpatialConcept"}, {"text": "Italy", "type": "SpatialConcept"}]}

Example input:
Sentence: Three populations of the novel species have been found in brackish and marine samples in the Mediterranean and the White Sea .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "brackish", "type": "Chemical"}, {"text": "marine samples", "type": "SpatialConcept"}, {"text": "Mediterranean", "type": "SpatialConcept"}, {"text": "White Sea", "type": "SpatialConcept"}]}

Example input:
Sentence: Based on species distribution modeling and molecular markers , we identified the glacial refugia and the postglacial migration routes of the species to Central Europe .

Example answer:
{"entities": [{"text": "species", "type": "IntellectualProduct"}, {"text": "modeling", "type": "ResearchActivity"}, {"text": "molecular markers", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Species distribution modeling and molecular markers suggest longitudinal range shifts and cryptic northern refugia of the typical calcareous grassland species Hippocrepis comosa ( horseshoe vetch ) Calcareous grasslands belong to the most diverse , endangered habitats in Europe , but there is still insufficient information about the origin of the plant species related to these grasslands .

Example answer:
{"entities": [{"text": "Species", "type": "IntellectualProduct"}, {"text": "modeling", "type": "ResearchActivity"}, {"text": "molecular markers", "type": "ClinicalAttribute"}, {"text": "calcareous grassland", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Hippocrepis comosa", "type": "Eukaryote"}, {"text": "horseshoe vetch", "type": "Eukaryote"}, {"text": "Calcareous grasslands", "type": "SpatialConcept"}, {"text": "endangered habitats", "type": "SpatialConcept"}, {"text": "Europe", "type": "SpatialConcept"}, {"text": "plant", "type": "Eukaryote"}, {"text": "grasslands", "type": "SpatialConcept"}]}

Example input:
Sentence: We clearly demonstrate that H . comosa followed a latitudinal and due to its oceanity also a longitudinal gradient during the last glacial maximum ( LGM ) , restricting the species to southern refugia situated on the Peninsulas of Iberia , the Balkans , and Italy during the last glaciation .

Example answer:
{"entities": [{"text": "H . comosa", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Peninsulas of Iberia", "type": "SpatialConcept"}, {"text": "Balkans", "type": "SpatialConcept"}, {"text": "Italy", "type": "SpatialConcept"}]}

Input:
Sentence: Both species distribution modeling and molecular markers underline that refugia of temperate , oceanic species such as H . comosa must not be exclusively located in southern but also in western of parts of Europe .

## Item MedMentions:test:4047
Example input:
Sentence: OSA was present in two - thirds of patients with type B AoD .

Example answer:
{"entities": [{"text": "OSA", "type": "BiologicFunction"}, {"text": "type B AoD", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 9 , 95 % confidence interval ( CI ) : 1 . 02 - 3 . 5 , severe OSA ( AHI ≥30 / h ) : OR = 2 .

Example answer:
{"entities": [{"text": "OSA", "type": "BiologicFunction"}]}

Example input:
Sentence: The predictors of shorter OS were a higher Memorial Sloan Kettering Cancer Center score ; liver , lung , and brain metastases ; and multiple sites of BMs ( hazard ratio , 1 . 38 ; 95 % CI , 1 . 02 - 1 . 91 ; P = .04 ) .

Example answer:
{"entities": [{"text": "liver", "type": "BiologicFunction"}, {"text": "lung", "type": "BiologicFunction"}, {"text": "brain metastases", "type": "BiologicFunction"}, {"text": "multiple sites", "type": "SpatialConcept"}, {"text": "BMs", "type": "BiologicFunction"}]}

Example input:
Sentence: A comprehensive medical evaluation yielded only a finding of moderate OSA .

Example answer:
{"entities": [{"text": "evaluation", "type": "HealthCareActivity"}, {"text": "finding", "type": "Finding"}, {"text": "OSA", "type": "BiologicFunction"}]}

Example input:
Sentence: OSA may therefore be implicated in both the etiology and prognosis of AoD .

Example answer:
{"entities": [{"text": "OSA", "type": "BiologicFunction"}, {"text": "prognosis", "type": "HealthCareActivity"}, {"text": "AoD", "type": "AnatomicalStructure"}]}

Example input:
Sentence: High hepatic tumor load ( > 50 % ) and high plasma chromogranin A ( > 600 ng / mL ) were negative baseline predictors for PFS and OS on univariate analysis , CgA remained significant on multivariate analysis ( PFS , P = 0 . 011 ; OS , P = 0 . 026 ) .

Example answer:
{"entities": [{"text": "hepatic tumor", "type": "BiologicFunction"}, {"text": "plasma chromogranin A", "type": "Chemical"}, {"text": "CgA", "type": "Chemical"}]}

Example input:
Sentence: Patients with GCA had increased risks for all types of incident vascular disease compared with non - vasculitis patients : adjusted hazard ratios were 1 . 57 ( 95 % CI : 1 . 36 , 1 . 82 ) for myocardial infarction , 1 . 41 ( 95 % CI : 1 . 29 , 1 . 55 ) for stroke , 1 . 75 ( 95 % CI : 1 . 49 , 2 . 06 ) for peripheral vascular disease , 1 . 98 ( 95 % CI : 1 . 50 , 2 . 62 ) for aortic aneurysm and 2 . 03 ( 95 % CI : 1 . 77 , 2 . 33 ) for venous thromboembolism .

Example answer:
{"entities": [{"text": "GCA", "type": "BiologicFunction"}, {"text": "risks for all types of incident", "type": "Finding"}, {"text": "vascular disease", "type": "BiologicFunction"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "peripheral vascular disease", "type": "BiologicFunction"}, {"text": "aortic aneurysm", "type": "BiologicFunction"}, {"text": "venous thromboembolism", "type": "BiologicFunction"}]}

Example input:
Sentence: Correlates of OS were explored using univariate analysis and multivariable analysis ( MVA ) .

Example answer:
{"entities": []}

Example input:
Sentence: CKD [ 10 . 5 % , n = 85 ( Stage 1 - 3 , 9 . 7 % ; Stage 4 - 5 , 0 . 7 % ) ] of predominantly mild severity showed significant association s with OSA ( AHI≥10 ) : odds ratio ( OR ) = 1 .

Example answer:
{"entities": [{"text": "CKD", "type": "BiologicFunction"}, {"text": "mild severity", "type": "Finding"}, {"text": "OSA", "type": "BiologicFunction"}]}

Example input:
Sentence: This study sought to explore whether the severity of OSA is associated with false lumen thrombosis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "OSA", "type": "BiologicFunction"}, {"text": "lumen", "type": "SpatialConcept"}, {"text": "thrombosis", "type": "BiologicFunction"}]}

Input:
Sentence: Multivariable analysis revealed that OSA severity was positively associated with partial thrombosis ( odds ratio , 1 . 784 , 95 % confidence interval : 1 . 182 - 2 . 691 , P = .006 ) after adjusting for other confounding factors .

## Item MedMentions:test:4203
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

## Item MedMentions:test:3775
Example input:
Sentence: L1 retrotransposon expression in circulating tumor cells Long interspersed nuclear element 1 ( LINE - 1 or L1 ) belongs to the non - long terminal repeat ( non - LTR ) retrotransposon family , which has been implicated in carcinogenesis and disease progression .

Example answer:
{"entities": [{"text": "L1 retrotransposon", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "circulating tumor cells", "type": "AnatomicalStructure"}, {"text": "Long interspersed nuclear element 1", "type": "Chemical"}, {"text": "LINE - 1", "type": "Chemical"}, {"text": "L1", "type": "Chemical"}, {"text": "non - long terminal repeat ( non - LTR ) retrotransposon family", "type": "Chemical"}, {"text": "carcinogenesis", "type": "BiologicFunction"}, {"text": "disease progression", "type": "BiologicFunction"}]}

Example input:
Sentence: KCNQ1 variant penetrance was estimated to be only 9 % to 17 % .

Example answer:
{"entities": [{"text": "KCNQ1", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We aimed to explore whether stressful events in early and recent life was associated with leucocyte telomere length ( TL ) , which is assumed to reflect the accumulated burden of inflammation and oxidative stress occurring during the life course .

Example answer:
{"entities": [{"text": "leucocyte telomere length", "type": "BiologicFunction"}, {"text": "TL", "type": "BiologicFunction"}, {"text": "accumulated", "type": "Finding"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "oxidative stress", "type": "BiologicFunction"}]}

Example input:
Sentence: LncRNA MIAT enhances cardiac hypertrophy partly through sponging miR - 150 In this work , we aimed to study whether myocardial infarction associated transcript ( MIAT ) exerts a regulative effect on cardiac hypertrophy via acting as a miR - 150 sponge .

Example answer:
{"entities": [{"text": "LncRNA MIAT", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "BiologicFunction"}, {"text": "miR - 150", "type": "AnatomicalStructure"}, {"text": "myocardial infarction associated transcript", "type": "Chemical"}, {"text": "MIAT", "type": "Chemical"}, {"text": "regulative", "type": "BiologicFunction"}]}

Example input:
Sentence: CKIP - 1 rs2306235 polymorphism may be a risk factor for chronic heart failure in a Chinese Han population .

Example answer:
{"entities": [{"text": "CKIP - 1 rs2306235", "type": "AnatomicalStructure"}, {"text": "polymorphism", "type": "SpatialConcept"}, {"text": "risk factor", "type": "Finding"}, {"text": "chronic heart failure", "type": "BiologicFunction"}]}

Example input:
Sentence: Therefore , we investigated whether CKIP - 1 nonsynonymous polymorphism rs2306235 ( Pro21Ala ) contributes to risk and prognosis of chronic heart failure in a Chinese population .

Example answer:
{"entities": [{"text": "CKIP - 1", "type": "AnatomicalStructure"}, {"text": "nonsynonymous polymorphism rs2306235", "type": "SpatialConcept"}, {"text": "Pro21Ala", "type": "BiologicFunction"}, {"text": "prognosis", "type": "HealthCareActivity"}, {"text": "chronic heart failure", "type": "BiologicFunction"}, {"text": "Chinese population", "type": "PopulationGroup"}]}

Example input:
Sentence: Identifying the importance of large genomic studies , our study demonstrates that 46 % of pathogenic mutations in KCNQ1 had a population frequency of less than 1 : 50 , 000 .

Example answer:
{"entities": [{"text": "genomic studies", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "KCNQ1", "type": "AnatomicalStructure"}, {"text": "population", "type": "PopulationGroup"}]}

Example input:
Sentence: Our data highlighted the predominant role of catecholaminergic polymorphic ventricular tachycardia and long QT syndrome , especially the RYR2 gene , as well as the minimal yield from other genes .

Example answer:
{"entities": [{"text": "catecholaminergic polymorphic ventricular tachycardia", "type": "BiologicFunction"}, {"text": "long QT syndrome", "type": "BiologicFunction"}, {"text": "RYR2 gene", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: KCNQ1 Gene Variants in Large Asymptomatic Populations : Considerations for Genomic Screening of Military Cohorts The advances in genomic technology of large populations make the potential for genomic screening of military cohorts and recruits feasible , affording the potential to identify at - risk individuals before occurrence of potentially life - threatening events .

Example answer:
{"entities": [{"text": "KCNQ1 Gene", "type": "AnatomicalStructure"}, {"text": "Military Cohorts", "type": "ProfessionalOrOccupationalGroup"}, {"text": "military cohorts", "type": "ProfessionalOrOccupationalGroup"}, {"text": "life - threatening events", "type": "Finding"}]}

Example input:
Sentence: This study of KCNQ1 provides a platform for consideration of other genes that cause sudden cardiac death as well as other medically actionable hereditary disorders for which genomic screening is available .

Example answer:
{"entities": [{"text": "KCNQ1", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "sudden cardiac death", "type": "BiologicFunction"}, {"text": "hereditary disorders", "type": "BiologicFunction"}]}

Input:
Sentence: Exploring sudden cardiac death , known to cause significant morbidity and mortality in young military service members , we focused on the most common gene associated with long QT syndrome ( LQTS ) , KCNQ1 .

## Item MedMentions:test:4208
Example input:
Sentence: 6 μm at baseline to 270 . 8 ± 27 .

Example answer:
{"entities": []}

Example input:
Sentence: 9 ± 4 . 2 mm ( range , 0 . 5 - 25 . 9 mm ) .

Example answer:
{"entities": []}

Example input:
Sentence: 94 ± 2 . 52 nm ) > Medium ( 17 . 00 ± 3 . 81 nm ) > Fine ( 11 . 89 ± 1 .

Example answer:
{"entities": []}

Example input:
Sentence: 03×10 ( - 9 ) , 7 . 57×10 ( - 9 ) , 9 . 69×10 ( - 9 ) and 8 . 15×10 ( - 9 ) , respectively , which were much lower than the threshold value of CR ( 10 ( - 6 ) ) ,

Example answer:
{"entities": []}

Example input:
Sentence: 10 . 9 ± 4 .

Example answer:
{"entities": []}

Example input:
Sentence: 0pM to 10nM and the detection limit was experimentally found to be of 0 .

Example answer:
{"entities": [{"text": "detection", "type": "HealthCareActivity"}, {"text": "found", "type": "Finding"}]}

Example input:
Sentence: 48 % ( 0 . 28 % , 0 . 69 % ) and 0 . 47 % ( 0 . 32 % , 0 . 63 % ) respectively , for 10μg / m ( 3 ) increase in exposure , both significantly higher than the increase of 0 .

Example answer:
{"entities": []}

Example input:
Sentence: 31×10 ( - 6 ) ngμL ( - 1 ) with a limit of detection of 1 . 80×10 ( - 14 ) ngμL ( - 1 ) with a high selectivity and sensitivity .

Example answer:
{"entities": []}

Example input:
Sentence: 61 cm for the best conditions , 2 . 4 ± 3 .

Example answer:
{"entities": []}

Example input:
Sentence: 1 cm ( P < .05 ) with 0 - dB noise .

Example answer:
{"entities": []}

Input:
Sentence: 6 cm for 10 - dB noise , 4 . 3 ± 3 .

## Item MedMentions:test:3851
Example input:
Sentence: Here , we demonstrate that CF3DODA - Me induced apoptosis , degraded Sp1 , inhibited the expression of multiple drivers of the blebbishield emergency program such as VEGFR2 , p70S6 K , and N - Myc through activation of caspase - 3 , inhibited reactive oxygen species ; and inhibited K - Ras activation to abolish transformation from blebbishields as well as transformation in soft agar .

Example answer:
{"entities": [{"text": "CF3DODA - Me", "type": "Chemical"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "Sp1", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "blebbishield emergency program", "type": "BiologicFunction"}, {"text": "VEGFR2", "type": "Chemical"}, {"text": "p70S6 K", "type": "Chemical"}, {"text": "N - Myc", "type": "Chemical"}, {"text": "caspase - 3", "type": "Chemical"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "K - Ras", "type": "Chemical"}, {"text": "transformation", "type": "BiologicFunction"}, {"text": "blebbishields", "type": "AnatomicalStructure"}, {"text": "soft agar", "type": "Chemical"}]}

Example input:
Sentence: We report for the first time that similar to dmyc , tissue - specific induced expression of human c - myc also suppresses poly ( Q ) -mediated neurotoxicity by an analogous mechanism .

Example answer:
{"entities": [{"text": "dmyc", "type": "Chemical"}, {"text": "induced expression", "type": "BiologicFunction"}, {"text": "human c - myc", "type": "Chemical"}, {"text": "poly ( Q )", "type": "Chemical"}, {"text": "neurotoxicity", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Myocyte enhancer factor 2 ( MEF2 ) proteins are reported that they have the potential contributions to adult muscle regeneration .

Example answer:
{"entities": [{"text": "Myocyte enhancer factor 2 ( MEF2 ) proteins", "type": "Chemical"}, {"text": "muscle regeneration", "type": "Finding"}]}

Example input:
Sentence: Elevation of both cAMP and cGMP by PDE10 inhibition was required for rescue .

Example answer:
{"entities": [{"text": "Elevation", "type": "HealthCareActivity"}, {"text": "cAMP", "type": "Chemical"}, {"text": "cGMP", "type": "Chemical"}, {"text": "PDE10", "type": "Chemical"}]}

Example input:
Sentence: These phenotypes were rescued by THI1 complementation and by exogenous thiamine .

Example answer:
{"entities": [{"text": "THI1", "type": "AnatomicalStructure"}, {"text": "thiamine", "type": "Chemical"}]}

Example input:
Sentence: The majority of resistant isolates were oxa23 -positive global clone GC2 ; fine - scale phylogenomic analysis revealed five distinct GC2 sublineages within the ICU that had evolved locally via independent chromosomal insertions of oxa23 transposons .

Example answer:
{"entities": [{"text": "resistant", "type": "BiologicFunction"}, {"text": "isolates", "type": "Chemical"}, {"text": "clone", "type": "AnatomicalStructure"}, {"text": "GC2", "type": "Bacterium"}, {"text": "phylogenomic analysis", "type": "ResearchActivity"}, {"text": "ICU", "type": "Organization"}, {"text": "chromosomal insertions", "type": "BiologicFunction"}, {"text": "transposons", "type": "Chemical"}]}

Example input:
Sentence: Gene transfer of full - length MYBPC3 during differentiation prevented hypertrophy , sarcomere disarray and improved calcium impulse propagation in HCM hESC -CMs .

Example answer:
{"entities": [{"text": "Gene transfer", "type": "ResearchActivity"}, {"text": "MYBPC3", "type": "AnatomicalStructure"}, {"text": "differentiation", "type": "BiologicFunction"}, {"text": "hypertrophy", "type": "BiologicFunction"}, {"text": "sarcomere", "type": "AnatomicalStructure"}, {"text": "disarray", "type": "AnatomicalStructure"}, {"text": "improved", "type": "Finding"}, {"text": "calcium impulse propagation", "type": "BiologicFunction"}, {"text": "HCM", "type": "BiologicFunction"}, {"text": "hESC -CMs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In our current study , we focused on the abundant proteins in exosomes derived from MSCs ( MSC - exo ) and found that the C - C motif chemokine receptor - 2 ( CCR2 ) was expressed on MSC - exo with a high ability to bind to its ligand CCL2 .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "exosomes", "type": "AnatomicalStructure"}, {"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "MSC", "type": "AnatomicalStructure"}, {"text": "exo", "type": "AnatomicalStructure"}, {"text": "C - C motif chemokine receptor - 2", "type": "Chemical"}, {"text": "CCR2", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "bind to its ligand CCL2", "type": "BiologicFunction"}]}

Example input:
Sentence: Transactivation Domain of Human c - Myc Is Essential to Alleviate Poly ( Q ) -Mediated Neurotoxicity in Drosophila Disease Models Polyglutamine ( poly ( Q ) ) disorders , such as Huntington 's disease ( HD ) and spinocerebellar ataxias , represent a group of neurological disorders which arise due to an atypically expanded poly ( Q ) tract in the coding region of the affected gene .

Example answer:
{"entities": [{"text": "Transactivation", "type": "BiologicFunction"}, {"text": "Domain", "type": "SpatialConcept"}, {"text": "Human c - Myc", "type": "Chemical"}, {"text": "Poly ( Q )", "type": "Chemical"}, {"text": "Neurotoxicity", "type": "InjuryOrPoisoning"}, {"text": "Drosophila", "type": "Eukaryote"}, {"text": "Disease Models", "type": "BiologicFunction"}, {"text": "Polyglutamine", "type": "Chemical"}, {"text": "poly ( Q )", "type": "Chemical"}, {"text": "disorders", "type": "BiologicFunction"}, {"text": "Huntington 's disease", "type": "BiologicFunction"}, {"text": "HD", "type": "BiologicFunction"}, {"text": "spinocerebellar ataxias", "type": "BiologicFunction"}, {"text": "neurological disorders", "type": "BiologicFunction"}, {"text": "expanded", "type": "SpatialConcept"}, {"text": "coding region", "type": "AnatomicalStructure"}, {"text": "gene", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Our study suggests that strategies focussing on the transactivation domain of c - Myc could be a very useful approach to design novel drug molecules against poly ( Q ) disorders .

Example answer:
{"entities": [{"text": "transactivation", "type": "BiologicFunction"}, {"text": "domain", "type": "SpatialConcept"}, {"text": "c - Myc", "type": "Chemical"}, {"text": "drug molecules", "type": "Chemical"}, {"text": "poly ( Q )", "type": "Chemical"}, {"text": "disorders", "type": "BiologicFunction"}]}

Input:
Sentence: Among the three isoforms of c - Myc , the rescue potential was maximally manifested by the full - length c - Myc2 protein , followed by c - Myc1 , but not by c - MycS which lacks the transactivation domain .

## Item MedMentions:test:3956
Example input:
Sentence: The steric repulsion generated from the long POEGMA brush layer in the swollen state was long - range and strong so that the protein adsorption is very unlikely .

Example answer:
{"entities": [{"text": "POEGMA brush", "type": "Chemical"}, {"text": "swollen state", "type": "Finding"}, {"text": "protein", "type": "Chemical"}, {"text": "adsorption", "type": "HealthCareActivity"}]}

Example input:
Sentence: Controlled release patterns coupled with diffusion of drug were observed in two different buffers ( PBS ) at pH 7 .

Example answer:
{"entities": [{"text": "drug", "type": "Chemical"}, {"text": "buffers", "type": "Chemical"}, {"text": "PBS", "type": "Chemical"}]}

Example input:
Sentence: The coatings were hydrophilic and reached a thickness of up to 180 nm within 30 min of polymerization .

Example answer:
{"entities": []}

Example input:
Sentence: The thickness of the POEGMA brush layers could be well controlled by the polymerization time and density of the immobilized initiators .

Example answer:
{"entities": [{"text": "POEGMA brush", "type": "Chemical"}]}

Example input:
Sentence: Here , we report on a random copolymer brush surface - poly ( CBMAA - ran - HPMAA ) - providing high BRE immobilization capacity while simultaneously exhibiting ultralow - fouling behavior in complex food media .

Example answer:
{"entities": [{"text": "random copolymer brush", "type": "Chemical"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "poly ( CBMAA - ran - HPMAA )", "type": "Chemical"}, {"text": "BRE", "type": "Chemical"}, {"text": "complex food media", "type": "Food"}]}

Example input:
Sentence: However , for longer ( 17 and 30nm - thick ) POEGMA brush layer surfaces , material surface would be sufficiently covered by the dense coating and the first step of protein adsorption on surface was avoided .

Example answer:
{"entities": [{"text": "POEGMA brush", "type": "Chemical"}, {"text": "surfaces", "type": "SpatialConcept"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "protein", "type": "Chemical"}, {"text": "adsorption", "type": "HealthCareActivity"}]}

Example input:
Sentence: TIRM measurements showed that around 95 % of the protein - coated particles could freely move in the serum and no attractive force between two surfaces was detected .

Example answer:
{"entities": [{"text": "TIRM", "type": "HealthCareActivity"}, {"text": "protein", "type": "Chemical"}, {"text": "particles", "type": "Chemical"}, {"text": "serum", "type": "BodySubstance"}, {"text": "no", "type": "Finding"}, {"text": "surfaces", "type": "SpatialConcept"}, {"text": "detected", "type": "Finding"}]}

Example input:
Sentence: It was considered that shorter polymer chains or chains with low grafted density cannot fully cover the surfaces , proteins in serum could directly interact with the material surface and then deposited to form an adsorbed layer .

Example answer:
{"entities": [{"text": "shorter polymer chains", "type": "Chemical"}, {"text": "chains", "type": "Chemical"}, {"text": "surfaces", "type": "SpatialConcept"}, {"text": "proteins", "type": "Chemical"}, {"text": "serum", "type": "BodySubstance"}, {"text": "material", "type": "Chemical"}, {"text": "surface", "type": "SpatialConcept"}]}

Example input:
Sentence: The functionalization of the surface with polymer brushes significantly reduced the protein fouling and eliminated platelet activation and leukocyte adhesion .

Example answer:
{"entities": [{"text": "surface", "type": "SpatialConcept"}, {"text": "polymer brushes", "type": "Chemical"}, {"text": "protein", "type": "Chemical"}, {"text": "platelet activation", "type": "BiologicFunction"}, {"text": "leukocyte adhesion", "type": "BiologicFunction"}]}

Example input:
Sentence: Long - range interactions between protein - coated particles and POEGMA brush layers in a serum environment Hydrophilic poly [ oligo ( ethylene glycol ) methyl methacrylate ] ( POEGMA ) brush layers with different thickness and graft densities were prepared by surface - initiated atom transfer radical polymerization ( SI - ATRP ) to construct a model surface to examine protein - surface interactions in a serum environment .

Example answer:
{"entities": [{"text": "protein", "type": "Chemical"}, {"text": "particles", "type": "Chemical"}, {"text": "POEGMA brush", "type": "Chemical"}, {"text": "serum environment", "type": "BodySubstance"}, {"text": "Hydrophilic poly [ oligo ( ethylene glycol ) methyl methacrylate ] ( POEGMA ) brush", "type": "Chemical"}, {"text": "prepared", "type": "Finding"}, {"text": "model", "type": "IntellectualProduct"}, {"text": "surface", "type": "SpatialConcept"}]}

Input:
Sentence: Some particles were freely diffusing , some experienced intermittent diffusion and more than 50 % of particles were irreversibly deposited to the surfaces covered by short polymer brushes .

## Item MedMentions:test:3943
Example input:
Sentence: MRI tumor size in the longest diameter ( LD ) was measured according to the RECIST ( Response Evaluation Criteria In Solid Tumors ) guidelines .

Example answer:
{"entities": [{"text": "MRI", "type": "HealthCareActivity"}, {"text": "tumor size", "type": "SpatialConcept"}, {"text": "RECIST", "type": "IntellectualProduct"}, {"text": "Response Evaluation Criteria In Solid Tumors", "type": "IntellectualProduct"}, {"text": "guidelines", "type": "IntellectualProduct"}]}

Example input:
Sentence: A total of 32 patients who had undergone ( 131 ) I - MIBG and FDG - PET prospectively were evaluated and clinicopathologically grouped into three categories : neuroblastoma , pheochromocytoma , and medullary carcinoma thyroid .

Example answer:
{"entities": [{"text": "( 131 ) I - MIBG", "type": "Chemical"}, {"text": "FDG - PET", "type": "HealthCareActivity"}, {"text": "neuroblastoma", "type": "BiologicFunction"}, {"text": "pheochromocytoma", "type": "BiologicFunction"}, {"text": "medullary carcinoma thyroid", "type": "BiologicFunction"}]}

Example input:
Sentence: In multiple logistic analysis , we found that higher AP / T ratio and microcalcification were independently associated with malignancy ( p < 0 .

Example answer:
{"entities": [{"text": "multiple logistic analysis", "type": "ResearchActivity"}, {"text": "microcalcification", "type": "BiologicFunction"}, {"text": "malignancy", "type": "BiologicFunction"}]}

Example input:
Sentence: The predictors of shorter OS were a higher Memorial Sloan Kettering Cancer Center score ; liver , lung , and brain metastases ; and multiple sites of BMs ( hazard ratio , 1 . 38 ; 95 % CI , 1 . 02 - 1 . 91 ; P = .04 ) .

Example answer:
{"entities": [{"text": "liver", "type": "BiologicFunction"}, {"text": "lung", "type": "BiologicFunction"}, {"text": "brain metastases", "type": "BiologicFunction"}, {"text": "multiple sites", "type": "SpatialConcept"}, {"text": "BMs", "type": "BiologicFunction"}]}

Example input:
Sentence: Future follow - up studies are needed to assess longitudinal cancer risks of suspicious mpMRI lesions .

Example answer:
{"entities": [{"text": "follow - up studies", "type": "ResearchActivity"}, {"text": "longitudinal cancer", "type": "BiologicFunction"}, {"text": "mpMRI", "type": "HealthCareActivity"}, {"text": "lesions", "type": "Finding"}]}

Example input:
Sentence: Upon univariate analysis , malignancy was significantly associated with age > 60 years , disease -free interval ≥24 months , SPN size > 8 mm , upper lobe localization and SUVmax > 2 .

Example answer:
{"entities": [{"text": "malignancy", "type": "BiologicFunction"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "SPN", "type": "BiologicFunction"}, {"text": "size", "type": "SpatialConcept"}, {"text": "upper lobe", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 1 ) months and median imaging follow - up was 12 ( ±18 .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Risk of malignancy for nodules was calculated based on size criteria according to the Fleischner Society recommendations from 2005 , along with the additional discriminators of pack - years smoking history , sex , and nodule location .

Example answer:
{"entities": [{"text": "Risk of malignancy", "type": "Finding"}, {"text": "nodules", "type": "Finding"}, {"text": "Fleischner Society", "type": "Organization"}, {"text": "additional discriminators", "type": "IntellectualProduct"}, {"text": "nodule", "type": "AnatomicalStructure"}, {"text": "location", "type": "SpatialConcept"}]}

Example input:
Sentence: By incorporating 3 demographic data points , the risk of lung nodule malignancy within the Fleischner categories can be considerably stratified and more personalized follow - up recommendations can be made .

Example answer:
{"entities": [{"text": "risk of lung nodule malignancy", "type": "Finding"}, {"text": "Fleischner", "type": "Organization"}, {"text": "categories", "type": "IntellectualProduct"}, {"text": "follow - up", "type": "HealthCareActivity"}]}

Example input:
Sentence: Based on personalized malignancy risk , 54 % of nodules > 4 and ≤6 mm were reclassified to longer - term follow - up than recommended by Fleischner .

Example answer:
{"entities": [{"text": "nodules", "type": "AnatomicalStructure"}, {"text": "Fleischner", "type": "Organization"}]}

Input:
Sentence: Imaging follow - up recommendations were assigned according to Fleischner size category malignancy risk .

## Item MedMentions:test:4112
Example input:
Sentence: Based on the similarity of calculated stereo - electronic profiles , specifically the electrostatic potential profiles of the compounds , and in silico screening of related compounds from literature , we identified three additional compounds , Quinacrine ( QC ) , Mefloquine ( MQ ) , and GSK369796 .

Example answer:
{"entities": [{"text": "compounds", "type": "Chemical"}, {"text": "literature", "type": "IntellectualProduct"}, {"text": "Quinacrine", "type": "Chemical"}, {"text": "QC", "type": "Chemical"}, {"text": "Mefloquine", "type": "Chemical"}, {"text": "MQ", "type": "Chemical"}, {"text": "GSK369796", "type": "Chemical"}]}

Example input:
Sentence: Construction of Fused Polyheterocycles through Sequential [ 4 + 2 ] and [ 3 + 2 ] Cycloadditions A method for Pd - catalyzed aerobic oxidative reaction of quinazolinones and alkynes has been developed for sequential [ 4 + 2 ] and [ 3 + 2 ] cycloadditions to assemble a novel fused - polycyclic system containing tetrahydropyridine and dihydrofuran rings .

Example answer:
{"entities": [{"text": "Pd", "type": "Chemical"}, {"text": "oxidative reaction", "type": "BiologicFunction"}, {"text": "quinazolinones", "type": "Chemical"}, {"text": "alkynes", "type": "Chemical"}, {"text": "tetrahydropyridine", "type": "Chemical"}, {"text": "dihydrofuran rings", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated a systematic series of 4 - substituted - 2 - pyridylquinazolines in terms of their inhibitory potency as well as selectivity toward ABCG2 .

Example answer:
{"entities": [{"text": "4 - substituted - 2 - pyridylquinazolines", "type": "Chemical"}, {"text": "ABCG2", "type": "Chemical"}]}

Example input:
Sentence: Selective remote esterification of 8 - aminoquinoline amides via copper ( ii ) -catalyzed C ( sp ( 2 ) ) - O cross - coupling reaction The remote C - O coupling of quinoline amides at the C5 position has been established using cheap and readily available copper catalyst under mild conditions .

Example answer:
{"entities": [{"text": "8 - aminoquinoline amides", "type": "Chemical"}, {"text": "copper ( ii )", "type": "Chemical"}, {"text": "quinoline amides", "type": "Chemical"}, {"text": "copper", "type": "Chemical"}]}

Example input:
Sentence: N - ( 1H - Pyrazol - 3 - yl ) quinazolin - 4 - amines as a novel class of casein kinase 1δ / ε inhibitors : Synthesis , biological evaluation and molecular modeling studies Described herein is the design , synthesis and biological evaluation of a series of N - ( 1H - pyrazol - 3 - yl ) quinazolin - 4 - amines against a panel of eight disease relevant protein kinases .

Example answer:
{"entities": [{"text": "N - ( 1H - Pyrazol - 3 - yl ) quinazolin - 4 - amines", "type": "Chemical"}, {"text": "casein kinase 1δ", "type": "Chemical"}, {"text": "ε", "type": "Chemical"}, {"text": "inhibitors", "type": "Chemical"}, {"text": "molecular modeling studies", "type": "ResearchActivity"}, {"text": "N - ( 1H - pyrazol - 3 - yl ) quinazolin - 4 - amines", "type": "Chemical"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "protein kinases", "type": "Chemical"}]}

Example input:
Sentence: The 4 - anilinoquinazolines were evaluated for potential cytotoxicity against three cancer cell lines , namely , human breast adenocarcinoma ( MCF - 7 ) cells , human cervical cancer ( HeLa ) and human lung cancer ( A549 ) cells .

Example answer:
{"entities": [{"text": "4 - anilinoquinazolines", "type": "Chemical"}, {"text": "cytotoxicity", "type": "BiologicFunction"}, {"text": "cancer cell lines", "type": "AnatomicalStructure"}, {"text": "human breast adenocarcinoma ( MCF - 7 ) cells", "type": "AnatomicalStructure"}, {"text": "human cervical cancer", "type": "AnatomicalStructure"}, {"text": "HeLa", "type": "AnatomicalStructure"}, {"text": "human lung cancer ( A549 ) cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In the current study , the synthesis of novel 1 - 4 - ( 7 - chloroquinolin - 4 - yl ) piperazin - 1 - yl ) - 2 - ( N - substituted - amino ) - ethanone derivatives ( 4a - t ) was achieved through the amination of 2 - chloro - 1 - ( 4 - ( 7 - chloroquinolin - 4 - yl ) piperazin - 1 - yl ) ethanone ( 3 ) with different secondary amines .

Example answer:
{"entities": [{"text": "current study", "type": "ResearchActivity"}, {"text": "1 - 4 - ( 7 - chloroquinolin - 4 - yl ) piperazin - 1 - yl ) - 2 - ( N - substituted - amino ) - ethanone", "type": "Chemical"}, {"text": "derivatives", "type": "Chemical"}, {"text": "4a - t", "type": "Chemical"}, {"text": "2 - chloro - 1 - ( 4 - ( 7 - chloroquinolin - 4 - yl ) piperazin - 1 - yl ) ethanone ( 3 )", "type": "Chemical"}, {"text": "secondary amines .", "type": "Chemical"}]}

Example input:
Sentence: We have discovered electrophilic quinazolines that covalently modify a soluble catalytic subunit of V - ATPase with high potency and exquisite proteomic selectivity as revealed by fluorescence imaging and chemical proteomic activity - based profiling .

Example answer:
{"entities": [{"text": "quinazolines", "type": "Chemical"}, {"text": "covalently modify", "type": "BiologicFunction"}, {"text": "catalytic subunit", "type": "SpatialConcept"}, {"text": "V - ATPase", "type": "Chemical"}, {"text": "fluorescence imaging", "type": "HealthCareActivity"}, {"text": "chemical proteomic activity - based profiling", "type": "HealthCareActivity"}]}

Example input:
Sentence: Taken together , the results of this study establish N - ( 1H - pyrazol - 3 - yl ) quinazolin - 4 - amines especially 3c and 3d as valuable lead molecules with great potential for CK1δ / ε inhibitor development targeting neurodegenerative disorders and cancer .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "N - ( 1H - pyrazol - 3 - yl ) quinazolin - 4 - amines", "type": "Chemical"}, {"text": "3c", "type": "Chemical"}, {"text": "3d", "type": "Chemical"}, {"text": "CK1δ", "type": "Chemical"}, {"text": "ε", "type": "Chemical"}, {"text": "inhibitor", "type": "Chemical"}, {"text": "neurodegenerative disorders", "type": "BiologicFunction"}, {"text": "cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: New compounds obtained following the proposed synthesis were fully characterized and , including the thirteen 4 ( 3H ) quinazolinimines synthesized by this method and previously reported by us , were used to study its cytotoxic effect on neoplastic cell lines .

Example answer:
{"entities": [{"text": "compounds", "type": "Chemical"}, {"text": "4 ( 3H ) quinazolinimines", "type": "Chemical"}, {"text": "previously reported", "type": "IntellectualProduct"}, {"text": "study", "type": "ResearchActivity"}, {"text": "cytotoxic effect", "type": "BiologicFunction"}, {"text": "neoplastic cell lines", "type": "AnatomicalStructure"}]}

Input:
Sentence: This method provides novel , direct and flexible access to diverse substituted 4 ( 3H ) quinazolinimines .

## Item MedMentions:test:4040
Example input:
Sentence: Copeptin and NT - proBNP levels were higher in the HCM group compared with controls ( 14 . 1 vs 8 . 4 pmol / L , P < 0 . 01 ; and 383 vs 44 pg / mL , P < 0 . 01 , respectively ) .

Example answer:
{"entities": [{"text": "Copeptin", "type": "Chemical"}, {"text": "HCM", "type": "BiologicFunction"}]}

Example input:
Sentence: Levels of copeptin and plasma N - terminal probrain natriuretic peptide ( NT - proBNP ) were evaluated prospectively in 24 obstructive HCM patients , 36 nonobstructive HCM patients , and 36 age - and sex - matched control subjects .

Example answer:
{"entities": [{"text": "copeptin", "type": "Chemical"}, {"text": "HCM", "type": "BiologicFunction"}]}

Example input:
Sentence: Copeptin and NT - proBNP levels were significantly higher in patients with obstructive HCM , and higher levels were associated with worse outcome .

Example answer:
{"entities": [{"text": "Copeptin", "type": "Chemical"}, {"text": "HCM", "type": "BiologicFunction"}]}

Example input:
Sentence: The current study used the Surveillance , Epidemiology , and End Results ( SEER ) - Consumer Assessment of Healthcare Providers and Systems ( CAHPS ) data set , a new data resource linking patient - reported information from the CAHPS Medicare Survey with clinical information from the National Cancer Institute 's SEER program .

Example answer:
{"entities": [{"text": "Surveillance , Epidemiology , and End Results", "type": "Organization"}, {"text": "SEER", "type": "Organization"}, {"text": "Consumer Assessment of Healthcare Providers and Systems", "type": "Organization"}, {"text": "CAHPS", "type": "Organization"}, {"text": "data set", "type": "IntellectualProduct"}, {"text": "resource linking patient - reported information", "type": "IntellectualProduct"}, {"text": "Medicare Survey", "type": "ResearchActivity"}, {"text": "clinical information", "type": "IntellectualProduct"}, {"text": "National Cancer Institute 's", "type": "Organization"}, {"text": "SEER program", "type": "Organization"}]}

Example input:
Sentence: The literature does not support an association between adjunctive corticosteroids and survival from NH - PCP but data are limited and findings should not be considered conclusive .

Example answer:
{"entities": [{"text": "literature", "type": "IntellectualProduct"}, {"text": "adjunctive corticosteroids", "type": "Chemical"}, {"text": "NH - PCP", "type": "BiologicFunction"}]}

Example input:
Sentence: Outcomes reported here comprised a survey of 400 actual patients seen by the PCPs in the study .

Example answer:
{"entities": [{"text": "survey", "type": "ResearchActivity"}, {"text": "PCPs", "type": "ProfessionalOrOccupationalGroup"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Guidelines for non - HIV PCP ( NH - PCP ) recommend adjunctive corticosteroids based on expert opinion .

Example answer:
{"entities": [{"text": "Guidelines", "type": "IntellectualProduct"}, {"text": "non - HIV PCP", "type": "BiologicFunction"}, {"text": "NH - PCP", "type": "BiologicFunction"}, {"text": "adjunctive corticosteroids", "type": "Chemical"}]}

Example input:
Sentence: There was no association between corticosteroids and survival in NH - PCP ( odds ratio , 0 .

Example answer:
{"entities": [{"text": "corticosteroids", "type": "Chemical"}, {"text": "NH - PCP", "type": "BiologicFunction"}]}

Example input:
Sentence: We conducted a systematic review and meta - analysis characterizing adjunctive corticosteroids for NH - PCP .

Example answer:
{"entities": [{"text": "systematic review", "type": "IntellectualProduct"}, {"text": "meta - analysis", "type": "IntellectualProduct"}, {"text": "adjunctive corticosteroids", "type": "Chemical"}, {"text": "NH - PCP", "type": "BiologicFunction"}]}

Example input:
Sentence: Our search yielded 5044 abstracts , 277 articles were chosen for full review , and 6 articles described outcomes in moderate to severe NH - PCP .

Example answer:
{"entities": [{"text": "abstracts", "type": "IntellectualProduct"}, {"text": "articles", "type": "IntellectualProduct"}, {"text": "NH - PCP", "type": "BiologicFunction"}]}

Input:
Sentence: Data on clinical outcomes from NH - PCP were extracted with a standardized instrument .
