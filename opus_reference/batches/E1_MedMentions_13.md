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

## Item MedMentions:test:2577
Example input:
Sentence: However , fucoxanthin failed to provide neuroprotection and activated autophagy following TBI in Nrf2 ( - / - ) mice .

Example answer:
{"entities": [{"text": "fucoxanthin", "type": "Chemical"}, {"text": "neuroprotection", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "TBI", "type": "InjuryOrPoisoning"}, {"text": "Nrf2", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: In conclusion , our studies indicated that fucoxanthin provided neuroprotective effects in models of TBI , potentially via regulation of the Nrf2 - ARE and Nrf2 - autophagy pathways .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "fucoxanthin", "type": "Chemical"}, {"text": "TBI", "type": "InjuryOrPoisoning"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "Nrf2", "type": "Chemical"}, {"text": "ARE", "type": "Chemical"}, {"text": "autophagy pathways", "type": "BiologicFunction"}]}

Example input:
Sentence: We found that fucoxanthin alleviated TBI -induced secondary brain injury , including neurological deficits , cerebral edema , brain lesion and neuronal apoptosis .

Example answer:
{"entities": [{"text": "fucoxanthin", "type": "Chemical"}, {"text": "TBI", "type": "InjuryOrPoisoning"}, {"text": "brain injury", "type": "InjuryOrPoisoning"}, {"text": "neurological deficits", "type": "Finding"}, {"text": "cerebral edema", "type": "BiologicFunction"}, {"text": "brain lesion", "type": "BiologicFunction"}, {"text": "apoptosis", "type": "BiologicFunction"}]}

Example input:
Sentence: These results suggest that the reduction of oxidative stress and neuroinflammation are not the key components of the secondary injury that contribute to cognitive deficits following TBI .

Example answer:
{"entities": [{"text": "results", "type": "Finding"}, {"text": "reduction", "type": "HealthCareActivity"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "secondary injury", "type": "InjuryOrPoisoning"}, {"text": "TBI", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Spatial cognitive deficits and chronic brain tissue loss , as well as endogenous brain repair processes such as neurogenesis , angiogenesis , and oligodendrogenesis , were evaluated up to 35 days after TBI .

Example answer:
{"entities": [{"text": "brain tissue", "type": "AnatomicalStructure"}, {"text": "brain repair processes", "type": "HealthCareActivity"}, {"text": "neurogenesis", "type": "BiologicFunction"}, {"text": "angiogenesis", "type": "BiologicFunction"}, {"text": "oligodendrogenesis", "type": "BiologicFunction"}, {"text": "TBI", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Cognitive assessment of pycnogenol therapy following traumatic brain injury We have previously shown that pycnogenol ( PYC ) increases antioxidants , decreases oxidative stress , suppresses neuroinflammation and enhances synaptic plasticity following traumatic brain injury ( TBI ) .

Example answer:
{"entities": [{"text": "Cognitive assessment", "type": "HealthCareActivity"}, {"text": "pycnogenol", "type": "Chemical"}, {"text": "therapy", "type": "HealthCareActivity"}, {"text": "traumatic brain injury", "type": "InjuryOrPoisoning"}, {"text": "PYC", "type": "Chemical"}, {"text": "antioxidants", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "enhances synaptic plasticity", "type": "BiologicFunction"}, {"text": "TBI", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Mechanistically , the combined treatment promoted post - TBI restorative processes in the brain , including generation of immature neurons , microvessels , and oligodendrocytes , each of which was significantly correlated with the improved cognitive recovery .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}, {"text": "post - TBI", "type": "InjuryOrPoisoning"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "immature neurons", "type": "AnatomicalStructure"}, {"text": "microvessels", "type": "AnatomicalStructure"}, {"text": "oligodendrocytes", "type": "AnatomicalStructure"}, {"text": "improved", "type": "Finding"}]}

Example input:
Sentence: Repetitive and Prolonged Omega - 3 Fatty Acid Treatment After Traumatic Brain Injury Enhances Long - Term Tissue Restoration and Cognitive Recovery Traumatic brain injury ( TBI ) is one of the most disabling clinical conditions that could lead to neurocognitive disorders in survivors .

Example answer:
{"entities": [{"text": "Omega - 3 Fatty Acid", "type": "Chemical"}, {"text": "Treatment", "type": "HealthCareActivity"}, {"text": "Traumatic Brain Injury", "type": "InjuryOrPoisoning"}, {"text": "Tissue", "type": "AnatomicalStructure"}, {"text": "Restoration", "type": "HealthCareActivity"}, {"text": "Cognitive Recovery", "type": "HealthCareActivity"}, {"text": "Traumatic brain injury", "type": "InjuryOrPoisoning"}, {"text": "TBI", "type": "InjuryOrPoisoning"}, {"text": "neurocognitive disorders", "type": "BiologicFunction"}]}

Example input:
Sentence: In the present study , we employed the decline of spatial cognitive function as a main outcome after TBI to investigate the therapeutic efficacy of post - TBI n - 3 PUFA treatment and the underlying mechanisms .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "cognitive function", "type": "BiologicFunction"}, {"text": "TBI", "type": "InjuryOrPoisoning"}, {"text": "n - 3 PUFA", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: These results indicated that repetitive and prolonged n - 3 PUFA treatments after TBI are capable of enhancing brain remodeling and could be developed as a potential therapy to treat TBI victims in the clinic .

Example answer:
{"entities": [{"text": "indicated", "type": "Finding"}, {"text": "n - 3 PUFA", "type": "Chemical"}, {"text": "treatments", "type": "HealthCareActivity"}, {"text": "TBI", "type": "InjuryOrPoisoning"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "therapy", "type": "HealthCareActivity"}, {"text": "clinic", "type": "Organization"}]}

Input:
Sentence: However , it remains unclear whether a clinically relevant therapeutic regimen with n - 3 PUFAs administered after TBI would still offer significant improvement of long - term cognitive recovery .

## Item MedMentions:test:2666
Example input:
Sentence: Cell apoptosis and differentially expressed proteins was detected by flow cytometry ( FCM ) , quantitative real - time polymerase chain reaction ( qRT - PCR ) , and western blotting , respectively .

Example answer:
{"entities": [{"text": "Cell apoptosis", "type": "BiologicFunction"}, {"text": "differentially expressed proteins", "type": "Chemical"}, {"text": "detected", "type": "Finding"}, {"text": "flow cytometry", "type": "HealthCareActivity"}, {"text": "FCM", "type": "HealthCareActivity"}, {"text": "quantitative real - time polymerase chain reaction", "type": "ResearchActivity"}, {"text": "qRT - PCR", "type": "ResearchActivity"}, {"text": "western blotting", "type": "HealthCareActivity"}]}

Example input:
Sentence: In recent years , various forms of cell therapy , including the use of mesenchymal stromal cells , have been put forward as an alternative strategy for more defined therapy .

Example answer:
{"entities": [{"text": "cell therapy", "type": "HealthCareActivity"}, {"text": "mesenchymal stromal cells", "type": "AnatomicalStructure"}, {"text": "therapy", "type": "HealthCareActivity"}]}

Example input:
Sentence: A total of three primary histological varieties have been identified : conventional , chondroid , and dedifferentiated .

Example answer:
{"entities": [{"text": "histological varieties", "type": "BiologicFunction"}, {"text": "conventional", "type": "BiologicFunction"}, {"text": "chondroid", "type": "BiologicFunction"}, {"text": "dedifferentiated", "type": "BiologicFunction"}]}

Example input:
Sentence: However , existing methods suffered from not only unavoidability of cell damaging conditions and / or sophisticated equipment , but also unavailability of proper materials to satisfy both mechanical and biological expectations .

Example answer:
{"entities": []}

Example input:
Sentence: This study primarily established the doubling method of haploids called " bud seedling method " in China which was very practicably in maize doubled haploid breeding .

Example answer:
{"entities": [{"text": "doubling method", "type": "ResearchActivity"}, {"text": "haploids", "type": "AnatomicalStructure"}, {"text": "bud seedling method", "type": "ResearchActivity"}, {"text": "China", "type": "SpatialConcept"}, {"text": "maize", "type": "Eukaryote"}, {"text": "haploid", "type": "AnatomicalStructure"}, {"text": "breeding", "type": "BiologicFunction"}]}

Example input:
Sentence: Also , haploids were obtained from two kinds of maternal genotypes involved in the experiment , including high - oil type and common type .

Example answer:
{"entities": [{"text": "haploids", "type": "AnatomicalStructure"}, {"text": "maternal", "type": "BiologicFunction"}, {"text": "experiment", "type": "ResearchActivity"}]}

Example input:
Sentence: So far , alternatives to conventional secretion were primarily observed and studied in yeast and animal cells .

Example answer:
{"entities": [{"text": "secretion", "type": "BiologicFunction"}, {"text": "studied", "type": "ResearchActivity"}, {"text": "yeast", "type": "Eukaryote"}, {"text": "animal cells", "type": "AnatomicalStructure"}]}

Example input:
Sentence: T - cell and ILC phenotype was analysed by multicolour flow cytometry .

Example answer:
{"entities": [{"text": "T - cell", "type": "AnatomicalStructure"}, {"text": "ILC", "type": "AnatomicalStructure"}, {"text": "analysed", "type": "ResearchActivity"}, {"text": "multicolour flow cytometry", "type": "HealthCareActivity"}]}

Example input:
Sentence: Here , it was demonstrated that this assay could be implemented to quantitatively analyze the cell proliferation of different types of cell lines , and to concurrently analyze the proliferation of two types of cell lines in coculture by utilizing cell tracking dyes with different spectral characteristics .

Example answer:
{"entities": [{"text": "assay", "type": "HealthCareActivity"}, {"text": "cell proliferation", "type": "BiologicFunction"}, {"text": "cell lines", "type": "AnatomicalStructure"}, {"text": "analyze", "type": "ResearchActivity"}, {"text": "coculture", "type": "HealthCareActivity"}, {"text": "cell tracking", "type": "ResearchActivity"}, {"text": "dyes", "type": "Chemical"}]}

Example input:
Sentence: This in vitro differentiation method for generating human trophoblasts starting from hPSCs overcomes the ethical and legal restrictions of working with early human embryos , and this system can be used for a variety of applications , including drug discovery and stem cell research .

Example answer:
{"entities": [{"text": "differentiation method", "type": "BiologicFunction"}, {"text": "human", "type": "Eukaryote"}, {"text": "trophoblasts", "type": "AnatomicalStructure"}, {"text": "hPSCs", "type": "AnatomicalStructure"}, {"text": "embryos", "type": "AnatomicalStructure"}, {"text": "drug discovery", "type": "ResearchActivity"}, {"text": "stem cell research", "type": "ResearchActivity"}]}

Input:
Sentence: However , respective methods have been described mainly in non - differentiated or haploid cell types .

## Item MedMentions:test:2408
Example input:
Sentence: Analyses of our next generation sequencing results and data from five independent published studies consisting of 191 normal , 10 low - grade squamous intraepithelial lesions , 21 high - grade squamous intraepithelial lesions , and 335 malignant tissues identified a panel of nine genes ( ARHGAP6 , DAPK1 , HAND2 , NKX2 - 2 , NNAT , PCDH10 , PROX1 , PITX2 , and RAB6C ) which could effectively discriminate among the various groups with sensitivity and specificity of 80 % - 100 % ( p < 0 .

Example answer:
{"entities": [{"text": "Analyses", "type": "ResearchActivity"}, {"text": "next generation sequencing", "type": "ResearchActivity"}, {"text": "published studies", "type": "IntellectualProduct"}, {"text": "normal", "type": "Finding"}, {"text": "low - grade squamous intraepithelial lesions", "type": "BiologicFunction"}, {"text": "high - grade squamous intraepithelial lesions", "type": "BiologicFunction"}, {"text": "malignant", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "ARHGAP6", "type": "AnatomicalStructure"}, {"text": "DAPK1", "type": "AnatomicalStructure"}, {"text": "HAND2", "type": "AnatomicalStructure"}, {"text": "NKX2 - 2", "type": "AnatomicalStructure"}, {"text": "NNAT", "type": "AnatomicalStructure"}, {"text": "PCDH10", "type": "AnatomicalStructure"}, {"text": "PROX1", "type": "AnatomicalStructure"}, {"text": "PITX2", "type": "AnatomicalStructure"}, {"text": "RAB6C", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Additionally , the genetic background of the unique biphasic pathological characteristics of such mixed neuronal - glial tumors remains unclear .

Example answer:
{"entities": [{"text": "biphasic pathological characteristics", "type": "BiologicFunction"}, {"text": "mixed neuronal - glial tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: Targeted - NGS on genes commonly mutated in IPMN and PDAC was performed on tumors from ( 1 ) 13 patients who developed disease progression in the remnant pancreas following resection of IPMN ; and ( 2 ) 10 patients who underwent a resection for PDAC and had a concomitant IPMN .

Example answer:
{"entities": [{"text": "Targeted - NGS", "type": "ResearchActivity"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "mutated", "type": "BiologicFunction"}, {"text": "IPMN", "type": "BiologicFunction"}, {"text": "PDAC", "type": "BiologicFunction"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "disease progression", "type": "BiologicFunction"}, {"text": "remnant", "type": "AnatomicalStructure"}, {"text": "pancreas", "type": "AnatomicalStructure"}, {"text": "resection", "type": "HealthCareActivity"}]}

Example input:
Sentence: Morphologic features of central nervous system ( CNS ) tumors were seen in 15 PNETs , including 9 medulloblastomas , 3 ependymomas , 2 medulloepitheliomas , and 1 glioblastoma , consistent with central PNET .

Example answer:
{"entities": [{"text": "central nervous system", "type": "BodySystem"}, {"text": "CNS", "type": "BodySystem"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "PNETs", "type": "BiologicFunction"}, {"text": "medulloblastomas", "type": "BiologicFunction"}, {"text": "ependymomas", "type": "BiologicFunction"}, {"text": "medulloepitheliomas", "type": "BiologicFunction"}, {"text": "glioblastoma", "type": "BiologicFunction"}, {"text": "central PNET", "type": "BiologicFunction"}]}

Example input:
Sentence: Genetic screening showed no mutations for both the RET proto - oncogene for HD and the p53 tumor suppressor gene for osteosarcoma .

Example answer:
{"entities": [{"text": "Genetic screening", "type": "HealthCareActivity"}, {"text": "mutations", "type": "BiologicFunction"}, {"text": "RET proto - oncogene", "type": "AnatomicalStructure"}, {"text": "HD", "type": "AnatomicalStructure"}, {"text": "p53 tumor suppressor gene", "type": "AnatomicalStructure"}, {"text": "osteosarcoma", "type": "BiologicFunction"}]}

Example input:
Sentence: Central PNETs show a spectrum of morphologic features that overlaps with CNS tumors but lack EWSR1 rearrangement s .

Example answer:
{"entities": [{"text": "Central PNETs", "type": "BiologicFunction"}, {"text": "CNS", "type": "BodySystem"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "EWSR1", "type": "AnatomicalStructure"}, {"text": "rearrangement", "type": "BiologicFunction"}]}

Example input:
Sentence: Phenotypic and genetic heterogeneity of tumor tissue and circulating tumor cells in patients with metastatic castration - resistant prostate cancer : A report from the PETRUS prospective study Molecular characterization of cancer samples is hampered by tumor tissue availability in metastatic castration - resistant prostate cancer ( mCRPC ) patients .

Example answer:
{"entities": [{"text": "Phenotypic", "type": "Finding"}, {"text": "tumor tissue", "type": "AnatomicalStructure"}, {"text": "circulating tumor cells", "type": "AnatomicalStructure"}, {"text": "metastatic castration - resistant prostate cancer", "type": "BiologicFunction"}, {"text": "report", "type": "IntellectualProduct"}, {"text": "PETRUS prospective study", "type": "ResearchActivity"}, {"text": "Molecular characterization of cancer samples", "type": "IntellectualProduct"}, {"text": "mCRPC", "type": "BiologicFunction"}]}

Example input:
Sentence: Ewing sarcoma / peripheral PNETs lack morphologic features of CNS tumors .

Example answer:
{"entities": [{"text": "Ewing sarcoma / peripheral PNETs", "type": "BiologicFunction"}, {"text": "CNS", "type": "BodySystem"}, {"text": "tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: Comprehensive genetic characterization of rosette - forming glioneuronal tumors : independent component analysis by tissue microdissection A rosette - forming glioneuronal tumor ( RGNT ) is a rare mixed neuronal - glial tumor characterized by biphasic architecture of glial and neurocytic components .

Example answer:
{"entities": [{"text": "genetic", "type": "AnatomicalStructure"}, {"text": "rosette - forming glioneuronal tumors", "type": "BiologicFunction"}, {"text": "component", "type": "AnatomicalStructure"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "microdissection", "type": "HealthCareActivity"}, {"text": "rosette - forming glioneuronal tumor", "type": "BiologicFunction"}, {"text": "RGNT", "type": "BiologicFunction"}, {"text": "mixed neuronal - glial tumor", "type": "BiologicFunction"}, {"text": "biphasic architecture", "type": "Finding"}, {"text": "glial", "type": "AnatomicalStructure"}, {"text": "neurocytic", "type": "AnatomicalStructure"}, {"text": "components", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Their results suggested that RGNTs , which are tumors harboring two divergent differentiations that arose from a single clone , have a diverse genetic background .

Example answer:
{"entities": [{"text": "RGNTs", "type": "BiologicFunction"}, {"text": "tumors", "type": "BiologicFunction"}, {"text": "divergent differentiations", "type": "Finding"}, {"text": "clone", "type": "AnatomicalStructure"}]}

Input:
Sentence: Although previous studies have suggested that RGNTs and pilocytic astrocytomas ( PAs ) represent the same tumor entity , their results confirm that the genetic background of RGNTs is not identical to that of PA .

## Item MedMentions:test:2511
Example input:
Sentence: Our results reveal a large disparity of manipulative potentials among anthropoid hands .

Example answer:
{"entities": [{"text": "anthropoid hands", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In combination with the phylogenetically informed morphometric analyses , our results suggest that the morphological changes of non - human anthropoid hands did not coevolve with the brain to facilitate the manipulative ability during the evolutionary process , although the manipulative ability is a survival skill .

Example answer:
{"entities": [{"text": "phylogenetically informed morphometric analyses", "type": "HealthCareActivity"}, {"text": "morphological", "type": "SpatialConcept"}, {"text": "non - human anthropoid hands", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "evolutionary process", "type": "BiologicFunction"}]}

Example input:
Sentence: We used functional MRI - guided proton magnetic resonance spectroscopy to test the hypothesis that unilateral deafferentation is associated with lower levels of N - acetylaspartate ( NAA , a putative marker of neuronal integrity ) in the sensorimotor hand territory located contralateral to the missing hand in chronic amputees ( n = 19 ) compared with the analogous hand territory of age - and sex - matched healthy controls ( n = 28 ) .

Example answer:
{"entities": [{"text": "MRI - guided proton magnetic resonance spectroscopy", "type": "HealthCareActivity"}, {"text": "unilateral deafferentation", "type": "HealthCareActivity"}, {"text": "lower levels of N - acetylaspartate", "type": "Finding"}, {"text": "NAA", "type": "Chemical"}, {"text": "putative marker", "type": "ClinicalAttribute"}, {"text": "neuronal", "type": "AnatomicalStructure"}, {"text": "contralateral", "type": "SpatialConcept"}, {"text": "missing hand", "type": "Finding"}, {"text": "hand territory", "type": "Finding"}, {"text": "age - and sex - matched", "type": "Finding"}]}

Example input:
Sentence: In the present study , after mapping the preferred hand representation in two healthy male monkeys with intracortical micro - stimulation , ET - 1 was microinjected into the contralateral motor cortex ( M1 ) to its preferred hand .

Example answer:
{"entities": [{"text": "hand", "type": "AnatomicalStructure"}, {"text": "monkeys", "type": "Eukaryote"}, {"text": "ET - 1", "type": "Chemical"}, {"text": "microinjected", "type": "HealthCareActivity"}, {"text": "contralateral", "type": "SpatialConcept"}, {"text": "motor cortex", "type": "SpatialConcept"}, {"text": "M1", "type": "SpatialConcept"}]}

Example input:
Sentence: Consistent with previous results , in both cases there were clear biases to overestimate distances oriented along the medio - lateral axis of the hand compared to the proximo - distal axis .

Example answer:
{"entities": [{"text": "oriented", "type": "SpatialConcept"}, {"text": "medio - lateral axis", "type": "BiologicFunction"}, {"text": "hand", "type": "AnatomicalStructure"}, {"text": "proximo - distal axis", "type": "BiologicFunction"}]}

Example input:
Sentence: Here , we investigated whether individual differences in the magnitude of these distortions are shared between tactile distance perception and position sense , as would be predicted by the hypothesis that a single distorted body model underlies both tasks .

Example answer:
{"entities": [{"text": "distortions", "type": "AnatomicalStructure"}, {"text": "distance perception", "type": "BiologicFunction"}, {"text": "position sense", "type": "BiologicFunction"}]}

Example input:
Sentence: From the aspect of hand proportions , the human hand has the best manipulative potential among anthropoids .

Example answer:
{"entities": [{"text": "hand proportions", "type": "ClinicalAttribute"}, {"text": "human", "type": "Eukaryote"}, {"text": "hand", "type": "AnatomicalStructure"}, {"text": "anthropoids", "type": "Eukaryote"}]}

Example input:
Sentence: Rubber Hand and Virtual Hand Illusions showed that body ownership can be manipulated by applying suitable visual and tactile stimulation .

Example answer:
{"entities": [{"text": "Rubber Hand", "type": "MedicalDevice"}, {"text": "Virtual Hand Illusions", "type": "BiologicFunction"}, {"text": "visual", "type": "HealthCareActivity"}, {"text": "tactile stimulation", "type": "HealthCareActivity"}]}

Example input:
Sentence: Assessing the manipulative potentials of monkeys , apes and humans from hand proportions : implications for hand evolution The hand structure possesses a greater potential for performing manipulative skills than is typically observed , whether in humans or non - human anthropoids .

Example answer:
{"entities": [{"text": "monkeys", "type": "Eukaryote"}, {"text": "apes", "type": "Eukaryote"}, {"text": "humans", "type": "Eukaryote"}, {"text": "hand proportions", "type": "ClinicalAttribute"}, {"text": "hand", "type": "AnatomicalStructure"}, {"text": "evolution", "type": "BiologicFunction"}, {"text": "hand structure", "type": "AnatomicalStructure"}, {"text": "non - human anthropoids", "type": "Eukaryote"}]}

Example input:
Sentence: We used established tasks to measure distortions of the represented shape of the hand dorsum .

Example answer:
{"entities": [{"text": "distortions", "type": "AnatomicalStructure"}, {"text": "shape", "type": "SpatialConcept"}, {"text": "hand dorsum", "type": "SpatialConcept"}]}

Input:
Sentence: For both of these abilities , recent studies have reported that the stored body representations involved are highly distorted , at least in the case of the hand , with the hand dorsum represented as wider and squatter than it actually is .

## Item MedMentions:test:2815
Example input:
Sentence: Comprehensive statistical model selection and validation procedures were used to develop and test separate calibration models designed to predict objectively - measured SB and moderate to vigorous PA ( MVPA from self - reported PAR data .

Example answer:
{"entities": [{"text": "statistical model", "type": "IntellectualProduct"}, {"text": "models", "type": "IntellectualProduct"}, {"text": "self - reported", "type": "ResearchActivity"}]}

Example input:
Sentence: Partial correlation analyses were performed between exercise and cognitive parameters .

Example answer:
{"entities": [{"text": "Partial correlation analyses", "type": "ResearchActivity"}, {"text": "cognitive", "type": "BiologicFunction"}, {"text": "parameters", "type": "Finding"}]}

Example input:
Sentence: Several model parameters necessary for computer simulation were determined by reviewing and analyzing available published experimental data .

Example answer:
{"entities": [{"text": "model", "type": "IntellectualProduct"}, {"text": "analyzing", "type": "ResearchActivity"}, {"text": "published", "type": "IntellectualProduct"}]}

Example input:
Sentence: Furthermore , the composites were applied for the analysis of real biological samples .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Psychometric tests ( confirmatory factor analysis , Cronbach 's alpha , composite reliability ) and association ( linear regression , ANOVA ) with sociodemographic variables were undertaken .

Example answer:
{"entities": [{"text": "Psychometric", "type": "HealthCareActivity"}, {"text": "tests", "type": "IntellectualProduct"}, {"text": "Cronbach 's alpha", "type": "IntellectualProduct"}, {"text": "composite reliability", "type": "IntellectualProduct"}]}

Example input:
Sentence: Intra - and inter - observer reproducibility and scan - rescan reproducibility were evaluated using intra - class correlation coefficients ( ICCs ) and coefficient of variation ( CoV ) .

Example answer:
{"entities": []}

Example input:
Sentence: The composite memory score exhibited significant positive associations with the average GCIPL thickness and the GCIPL thickness in the superotemporal , inferonasal , and inferotemporal sectors .

Example answer:
{"entities": [{"text": "positive", "type": "Finding"}, {"text": "average GCIPL", "type": "AnatomicalStructure"}, {"text": "GCIPL", "type": "AnatomicalStructure"}, {"text": "superotemporal", "type": "SpatialConcept"}, {"text": "inferonasal", "type": "SpatialConcept"}, {"text": "inferotemporal sectors", "type": "SpatialConcept"}]}

Example input:
Sentence: The composite endpoint of procedure failure or acute complication was less common in the STSF group ( 2 vs . 8 , P = 0 . 05 ) .

Example answer:
{"entities": [{"text": "complication", "type": "BiologicFunction"}]}

Example input:
Sentence: The ICC3 , 1 values of 0 . 78 - 0 . 89 , Pearson correlation coefficient of 0 . 78 - 0 . 90 , and Bland - Altman plots showed almost perfect agreements between the US and CT method for all parameters , except the area under the transverse arch ( AUTA ) .

Example answer:
{"entities": [{"text": "Bland - Altman plots", "type": "IntellectualProduct"}, {"text": "agreements", "type": "IntellectualProduct"}, {"text": "US", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "method", "type": "IntellectualProduct"}, {"text": "area under the transverse arch ( AUTA )", "type": "SpatialConcept"}]}

Example input:
Sentence: The relative energies were refined through composite focal - point analyses employing basis sets as large as aug - cc - pV5Z and correlation treatments through CCSD ( T ) .

Example answer:
{"entities": [{"text": "composite focal - point analyses", "type": "ResearchActivity"}, {"text": "aug - cc - pV5Z", "type": "IntellectualProduct"}, {"text": "correlation treatments", "type": "ResearchActivity"}, {"text": "CCSD ( T )", "type": "IntellectualProduct"}]}

Input:
Sentence: The composite parameter was recorded and analyzed .

## Item MedMentions:test:2368
Example input:
Sentence: The TC + TT genotypes and T allele of rs2243250 were strongly associated with elevated AS risk [ CC vs TC + TT : odds ratio ( OR ) = 2 . 378 , 95 % confidence interval ( CI ) = 1 . 746 - 3 . 239 , P < 0 . 001 ; C vs T : OR = 2 . 588 , 95 % CI = 2 .

Example answer:
{"entities": [{"text": "T allele", "type": "AnatomicalStructure"}, {"text": "rs2243250", "type": "AnatomicalStructure"}, {"text": "AS", "type": "BiologicFunction"}]}

Example input:
Sentence: Different clinical pictures ( 0 - 50 % of diarrhea positivity ) , viral titer levels ( mean 5 . 3 - 7 . 2 log10 genome copies /mL ) , and antibody conditions ( 30 - 80 % of positivity ) were registered among sows on the four farms .

Example answer:
{"entities": [{"text": "clinical pictures", "type": "Finding"}, {"text": "diarrhea", "type": "Finding"}, {"text": "genome copies", "type": "AnatomicalStructure"}, {"text": "antibody conditions", "type": "Chemical"}, {"text": "farms", "type": "SpatialConcept"}]}

Example input:
Sentence: Compared with those with the TT genotype , those with the CC genotype had a lower mean ± SE total dairy intake ( 2 . 15 ± 0 . 09 compared with 2 . 67 ± 0 . 12 servings / d , P = 0 . 003 ) , a lower skim - milk intake ( 0 . 20 ± 0 . 03 compared with 0 . 46 ± 0 . 06 servings / d , P = 0 .

Example answer:
{"entities": [{"text": "total dairy intake", "type": "Finding"}, {"text": "lower skim - milk intake", "type": "Finding"}]}

Example input:
Sentence: For 300 SNPs , EBFST had the highest precision in all cases , but the bias was negative and greater than those for GST _ NC and θWC _ F in all cases .

Example answer:
{"entities": [{"text": "EBFST", "type": "IntellectualProduct"}, {"text": "negative", "type": "Finding"}]}

Example input:
Sentence: As the number of loci increased up to 10 000 , the precision of GST _ NC and θWC _ F became slightly better than for EBFST for cases with FST ≥0 .

Example answer:
{"entities": [{"text": "loci", "type": "SpatialConcept"}, {"text": "EBFST", "type": "IntellectualProduct"}, {"text": "FST", "type": "IntellectualProduct"}]}

Example input:
Sentence: Animal permanent environment also affected PBTTC ( 0 . 14±0 . 07 ) .

Example answer:
{"entities": [{"text": "Animal permanent environment", "type": "SpatialConcept"}, {"text": "PBTTC", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Genetic parameters for tick count and udder health in commercial and indigenous ewes in South Africa The genetics of tick infestation in sheep need study , as host resistance often forms part of integrated pest control programs .

Example answer:
{"entities": [{"text": "parameters", "type": "Finding"}, {"text": "udder", "type": "AnatomicalStructure"}, {"text": "commercial", "type": "IntellectualProduct"}, {"text": "South Africa", "type": "SpatialConcept"}, {"text": "tick infestation", "type": "BiologicFunction"}, {"text": "sheep", "type": "Eukaryote"}]}

Example input:
Sentence: Repeated udder health scores , site - specific tick count , mating weight and reproduction records ( N = 879 - 1204 ) were recorded annually from 2010 to 2015 on ewes of the indigenous Namaqua Afrikaner (  ) fat - tailed breed , as well as the commercial Dorper and SA Mutton Merino ( SAMM ) breeds .

Example answer:
{"entities": [{"text": "udder", "type": "AnatomicalStructure"}, {"text": "site - specific", "type": "SpatialConcept"}, {"text": "mating", "type": "BiologicFunction"}, {"text": "reproduction", "type": "BiologicFunction"}, {"text": "records", "type": "IntellectualProduct"}, {"text": "Namaqua Afrikaner", "type": "Eukaryote"}, {"text": "", "type": "Eukaryote"}, {"text": "fat - tailed breed", "type": "IntellectualProduct"}, {"text": "commercial", "type": "IntellectualProduct"}, {"text": "Dorper", "type": "Eukaryote"}, {"text": "SA Mutton Merino ( SAMM ) breeds", "type": "Eukaryote"}]}

Example input:
Sentence: Udder health scores of  ewes were lower than those of Dorpers , which in turn had lower scores than SAMM ewes .

Example answer:
{"entities": [{"text": "Udder", "type": "AnatomicalStructure"}, {"text": "", "type": "Eukaryote"}, {"text": "Dorpers", "type": "Eukaryote"}, {"text": "SAMM", "type": "Eukaryote"}]}

Example input:
Sentence: Heavier ewes had higher UPLTC

Example answer:
{"entities": [{"text": "UPLTC", "type": "AnatomicalStructure"}]}

Input:
Sentence:  ewes had lower values for HTLTC , UPLTC and TTC than the commercial breeds , but higher values for PBTTC than Dorpers .

## Item MedMentions:test:2608
Example input:
Sentence: The antibody titers of lgG , lgG1 and lgG2a , proportion of CD4 ( + ) and CD8 ( + ) T cells , and concentrations of IFN - γ were found to be significantly higher in multiple - gene rBCGs than that in single - gene rBCGs ( P < 0 .

Example answer:
{"entities": [{"text": "antibody", "type": "Chemical"}, {"text": "lgG", "type": "AnatomicalStructure"}, {"text": "lgG1", "type": "AnatomicalStructure"}, {"text": "lgG2a", "type": "AnatomicalStructure"}, {"text": "CD4 ( + )", "type": "AnatomicalStructure"}, {"text": "CD8 ( + ) T cells", "type": "AnatomicalStructure"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "gene", "type": "AnatomicalStructure"}, {"text": "rBCGs", "type": "Bacterium"}, {"text": "single - gene", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In infants with bronchopulmonary dysplasia and / or pulmonary hypertension ( n = 119 [ 51 % ] ) , RV free wall longitudinal strain and IVS GLS were significantly lower ( P < .01 ) , LV GLS and GLSRs were similar ( P = .56 ) , and IVS segmental longitudinal strain persisted as an RV - dominant base - to - apex gradient from 32 weeks postmenstrual age to 1 year CA .

Example answer:
{"entities": [{"text": "bronchopulmonary dysplasia", "type": "BiologicFunction"}, {"text": "pulmonary hypertension", "type": "BiologicFunction"}, {"text": "RV free wall", "type": "AnatomicalStructure"}, {"text": "IVS", "type": "AnatomicalStructure"}, {"text": "LV", "type": "AnatomicalStructure"}, {"text": "segmental", "type": "SpatialConcept"}, {"text": "RV", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We aimed to evaluate systemic and intestinal T - cell and innate lymphoid cell ( ILC ) responses , previously associated to IBD , in patients with PSC - UC compared to patients with UC and healthy controls .

Example answer:
{"entities": [{"text": "evaluate", "type": "HealthCareActivity"}, {"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "T - cell", "type": "AnatomicalStructure"}, {"text": "innate lymphoid cell", "type": "AnatomicalStructure"}, {"text": "ILC", "type": "AnatomicalStructure"}, {"text": "responses", "type": "BiologicFunction"}, {"text": "IBD", "type": "BiologicFunction"}, {"text": "PSC", "type": "BiologicFunction"}, {"text": "UC", "type": "BiologicFunction"}]}

Example input:
Sentence: Administration of RGD peptide , TGFβ , and αvβ6 - neutralizing antibodies attenuated IVD degeneration .

Example answer:
{"entities": [{"text": "Administration", "type": "HealthCareActivity"}, {"text": "RGD peptide", "type": "Chemical"}, {"text": "TGFβ", "type": "Chemical"}, {"text": "αvβ6", "type": "Chemical"}, {"text": "neutralizing antibodies", "type": "Chemical"}, {"text": "IVD degeneration", "type": "BiologicFunction"}]}

Example input:
Sentence: RNA sequencing revealed that differential gene expression between CD177 ( + ) and CD177 ( - ) neutrophils from patients with IBD was associated with response to bacterial defence , hydrogen peroxide and reactive oxygen species ( ROS ) .

Example answer:
{"entities": [{"text": "RNA sequencing", "type": "HealthCareActivity"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "CD177 ( + )", "type": "AnatomicalStructure"}, {"text": "CD177 ( - )", "type": "AnatomicalStructure"}, {"text": "neutrophils", "type": "AnatomicalStructure"}, {"text": "IBD", "type": "BiologicFunction"}, {"text": "bacterial defence", "type": "BiologicFunction"}, {"text": "hydrogen peroxide", "type": "Chemical"}, {"text": "reactive oxygen species", "type": "Chemical"}, {"text": "ROS", "type": "Chemical"}]}

Example input:
Sentence: In a challenge assay , rHVT / IBD ( UL3 - 4 ) protected chickens from challenge with virulent Marek 's disease virus serotype 1 and IBDV .

Example answer:
{"entities": [{"text": "assay", "type": "HealthCareActivity"}, {"text": "rHVT / IBD", "type": "Chemical"}, {"text": "UL3 - 4", "type": "SpatialConcept"}, {"text": "chickens", "type": "Eukaryote"}, {"text": "Marek 's disease virus serotype 1", "type": "Virus"}, {"text": "IBDV", "type": "Virus"}]}

Example input:
Sentence: rHVT / IBD ( US10 ) showed good growth activity in vitro , with growth comparable to that of the parent HVT .

Example answer:
{"entities": [{"text": "rHVT / IBD", "type": "Chemical"}, {"text": "US10", "type": "SpatialConcept"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "in vitro", "type": "ResearchActivity"}, {"text": "HVT", "type": "Virus"}]}

Example input:
Sentence: On the other hand , rHVT / IBD ( UL3 - 4 ) , rHVT / IBD ( UL22 - 23 ) , and rHVT / IBD ( UL45 - 46 ) exhibited decreased growth activity in chicken embryo fibroblast ( CEF ) cells compared to the parent HVT .

Example answer:
{"entities": [{"text": "rHVT / IBD", "type": "Chemical"}, {"text": "UL3 - 4", "type": "SpatialConcept"}, {"text": "UL22 - 23", "type": "SpatialConcept"}, {"text": "UL45 - 46", "type": "SpatialConcept"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "chicken embryo", "type": "AnatomicalStructure"}, {"text": "fibroblast ( CEF ) cells", "type": "AnatomicalStructure"}, {"text": "HVT", "type": "Virus"}]}

Example input:
Sentence: Based on the results of in vitro and in vivo assays , rHVT / IBD ( UL3 - 4 ) was selected for further testing .

Example answer:
{"entities": [{"text": "in vitro", "type": "ResearchActivity"}, {"text": "rHVT / IBD", "type": "Chemical"}, {"text": "UL3 - 4", "type": "SpatialConcept"}]}

Example input:
Sentence: However , the rHVT / IBD ( US10 ) elicited lower levels of virus - neutralizing ( VN ) antibodies compared to the other constructs .

Example answer:
{"entities": [{"text": "rHVT / IBD", "type": "Chemical"}, {"text": "US10", "type": "SpatialConcept"}, {"text": "virus - neutralizing ( VN ) antibodies", "type": "Chemical"}]}

Input:
Sentence: rHVT / IBD ( UL3 - 4 ) and rHVT / IBD ( UL45 - 46 ) appeared to be similar in their ability to elicit VN antibodies .

## Item MedMentions:test:2693
Example input:
Sentence: Results show that using glycerol as co - substrate led to higher volumetric productivities , and lower specific and volumetric methanol consumption rates .

Example answer:
{"entities": [{"text": "glycerol", "type": "Chemical"}, {"text": "volumetric", "type": "SpatialConcept"}, {"text": "methanol", "type": "Chemical"}]}

Example input:
Sentence: We used the relative potency factor ( RPF ) method to normalise the various pesticides to the index compound ( IC ) of methamidophos and chlorpyrifos separately .

Example answer:
{"entities": [{"text": "relative potency factor ( RPF ) method", "type": "IntellectualProduct"}, {"text": "pesticides", "type": "Chemical"}, {"text": "index compound", "type": "Chemical"}, {"text": "IC", "type": "Chemical"}, {"text": "methamidophos", "type": "Chemical"}, {"text": "chlorpyrifos", "type": "Chemical"}]}

Example input:
Sentence: The minimum inhibitory concentration ( MIC ) value against NSCs was 3 , 10 , and 300 mg / L , in each staining process , acridine orange / ethidium bromide ( AO / EB ) staining , 3 - ( 4 , 5 - dimethylthiazol - 2 - yl ) 2 , 5 - diphenyl tetrazolium bromide ( MTT ) assay , and Hoechst staining , for CH3HgCl , CP , and CH3COOPb , respectively .

Example answer:
{"entities": [{"text": "minimum inhibitory concentration ( MIC ) value", "type": "Finding"}, {"text": "NSCs", "type": "AnatomicalStructure"}, {"text": "staining process", "type": "HealthCareActivity"}, {"text": "acridine orange", "type": "Chemical"}, {"text": "ethidium bromide", "type": "Chemical"}, {"text": "AO", "type": "Chemical"}, {"text": "EB", "type": "Chemical"}, {"text": "staining", "type": "HealthCareActivity"}, {"text": "3 - ( 4 , 5 - dimethylthiazol - 2 - yl ) 2 , 5 - diphenyl tetrazolium bromide", "type": "Chemical"}, {"text": "MTT", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}, {"text": "CH3HgCl", "type": "Chemical"}, {"text": "CP", "type": "Chemical"}, {"text": "CH3COOPb", "type": "Chemical"}]}

Example input:
Sentence: e . cell / substrate ratio of 20 : 1 ( w / w ) at pH 7 . 5 and 20 ° C in 10 % ( v / v ) dimethylformamide ( DMF ) in a 10 h reaction . 99 % enantiopure ( R ) - PGE was obtained when the reaction time was prolonged to 12 h with a yield of 34 % .

Example answer:
{"entities": [{"text": "cell", "type": "AnatomicalStructure"}, {"text": "dimethylformamide", "type": "Chemical"}, {"text": "DMF", "type": "Chemical"}, {"text": "enantiopure ( R ) - PGE", "type": "Chemical"}]}

Example input:
Sentence: Enhanced performance of proteins separation was achieved on the MCN - C4 - monolith in comparison with the butyl - silica hybrid monolithic column without MCN ( C4 - monolith ) .

Example answer:
{"entities": [{"text": "proteins", "type": "Chemical"}, {"text": "MCN", "type": "Chemical"}]}

Example input:
Sentence: Stationary - phase cells were more tolerant to imipenem ( Carbapenem ) than exponential cells , leaving a small fraction of persisters at high imipenem concentration in both populations .

Example answer:
{"entities": [{"text": "Stationary - phase cells", "type": "Bacterium"}, {"text": "tolerant", "type": "Finding"}, {"text": "imipenem", "type": "Chemical"}, {"text": "Carbapenem", "type": "Chemical"}, {"text": "exponential cells", "type": "Bacterium"}, {"text": "persisters", "type": "Bacterium"}, {"text": "populations", "type": "PopulationGroup"}]}

Example input:
Sentence: 1 % formic acid in water ) ; sample load ( 26 cycles of 250μL ) ; wash ( 100μL of 3 % acetic acid in water followed by 100μL 5 % methanol in water ) ; and elution ( 6 cycles of 100μL of 10 % ammonium hydroxide in methanol ) .

Example answer:
{"entities": [{"text": "formic acid", "type": "Chemical"}, {"text": "water", "type": "Chemical"}, {"text": "acetic acid", "type": "Chemical"}, {"text": "methanol", "type": "Chemical"}, {"text": "ammonium hydroxide", "type": "Chemical"}]}

Example input:
Sentence: Preparation of organic - silica hybrid monolithic columns via crosslinking of functionalized mesoporous carbon nanoparticles for capillary liquid chromatography An organic - silica hybrid monolithic capillary column was fabricated by crosslinking ( 3 - aminopropyl ) trimethoxysilane ( APTMS ) modified mesoporous carbon nanoparticles ( AP - MCNs ) with tetramethoxysilane ( TMOS ) and n - butyltrimethoxysilane ( C4 - TriMOS ) .

Example answer:
{"entities": [{"text": "mesoporous carbon", "type": "Chemical"}, {"text": "capillary liquid chromatography", "type": "HealthCareActivity"}, {"text": "( 3 - aminopropyl ) trimethoxysilane", "type": "Chemical"}, {"text": "APTMS", "type": "Chemical"}, {"text": "AP - MCNs", "type": "Chemical"}, {"text": "tetramethoxysilane", "type": "Chemical"}, {"text": "TMOS", "type": "Chemical"}, {"text": "n - butyltrimethoxysilane", "type": "Chemical"}, {"text": "C4 - TriMOS", "type": "Chemical"}]}

Example input:
Sentence: A small plasma volume ( 0 . 25mL ) pre - diluted ( 1 : 20 ) , was extracted with MEPS M1 sorbent as follows : conditioning ( 4 cycles of 250μL methanol and 4 cycles of 250μL 0 .

Example answer:
{"entities": [{"text": "small plasma volume", "type": "ClinicalAttribute"}, {"text": "MEPS", "type": "HealthCareActivity"}, {"text": "methanol", "type": "Chemical"}]}

Example input:
Sentence: Simultaneous separation of all four drugs was accomplished with a Chromolith Reversed - Phase column and mobile phases consisting of water , methanol , ammonium acetate and formic acid with subsequent mass spectrometric quantification .

Example answer:
{"entities": [{"text": "drugs", "type": "Chemical"}, {"text": "mobile phases", "type": "Chemical"}, {"text": "water", "type": "Chemical"}, {"text": "methanol", "type": "Chemical"}, {"text": "ammonium acetate", "type": "Chemical"}, {"text": "formic acid", "type": "Chemical"}]}

Input:
Sentence: An InertSustain RP - C18 column was used with the mobile phase consisting of methanol and 0 .

## Item MedMentions:test:2626
Example input:
Sentence: The modified McLaughlin technique with added iliac crest bone graft to fill the defect and prevent humeral head deformity is a successful technique for the treatment of patients with chronic locked posterior shoulder dislocation . [ Orthopedics . 201x ; xx ( x ) : xx - xx . ] .

Example answer:
{"entities": [{"text": "McLaughlin technique", "type": "HealthCareActivity"}, {"text": "iliac crest", "type": "AnatomicalStructure"}, {"text": "bone graft", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "chronic locked posterior shoulder dislocation", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Flaps A , B , and C are each folded in 90 degrees ; flap D is dislocated to the proximal plane of the reconstructed digit , followed by skin suturing .

Example answer:
{"entities": [{"text": "Flaps", "type": "AnatomicalStructure"}, {"text": "flap D", "type": "AnatomicalStructure"}, {"text": "digit", "type": "AnatomicalStructure"}, {"text": "skin suturing", "type": "HealthCareActivity"}]}

Example input:
Sentence: Flap D is freed to a degree minimally needed for dislocation , while leaving a thick subcutaneous pedicle .

Example answer:
{"entities": [{"text": "Flap D", "type": "AnatomicalStructure"}, {"text": "dislocation", "type": "InjuryOrPoisoning"}, {"text": "subcutaneous pedicle", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In the largest percentage of reconstructions , costal cartilage and a postauricular flap were used to correct the deformity .

Example answer:
{"entities": [{"text": "reconstructions", "type": "HealthCareActivity"}, {"text": "costal cartilage", "type": "AnatomicalStructure"}, {"text": "postauricular flap", "type": "AnatomicalStructure"}, {"text": "deformity", "type": "AnatomicalStructure"}]}

Example input:
Sentence: All clinical cases and cadaveric specimens underwent surgical closure prior to MR imaging including placement of titanium mesh over the craniotomy defect with a dural graft of porcine small intestinal submucosa ( SIS ) sealed with Tisseel ( fibrin sealant ) .

Example answer:
{"entities": [{"text": "cadaveric", "type": "AnatomicalStructure"}, {"text": "surgical closure", "type": "HealthCareActivity"}, {"text": "MR imaging", "type": "HealthCareActivity"}, {"text": "titanium", "type": "Chemical"}, {"text": "mesh", "type": "MedicalDevice"}, {"text": "craniotomy", "type": "HealthCareActivity"}, {"text": "porcine", "type": "Eukaryote"}, {"text": "small intestinal submucosa", "type": "AnatomicalStructure"}, {"text": "SIS", "type": "AnatomicalStructure"}, {"text": "Tisseel", "type": "Chemical"}, {"text": "fibrin sealant", "type": "Chemical"}]}

Example input:
Sentence: However , primary closure of the donor site is not easy when the size of the necessary skin island is relatively large .

Example answer:
{"entities": [{"text": "primary closure", "type": "HealthCareActivity"}, {"text": "donor site", "type": "SpatialConcept"}, {"text": "size", "type": "SpatialConcept"}, {"text": "skin island", "type": "BodySystem"}]}

Example input:
Sentence: On the inducing graft ( IG ) side , the tendon canal and semitendinosus tibial attachment site were connected by the fascia lata , which was harvested at the same width as the semitendinosus tendon .

Example answer:
{"entities": [{"text": "side", "type": "SpatialConcept"}, {"text": "tendon canal", "type": "AnatomicalStructure"}, {"text": "semitendinosus", "type": "AnatomicalStructure"}, {"text": "tibial", "type": "AnatomicalStructure"}, {"text": "attachment site", "type": "SpatialConcept"}, {"text": "fascia lata", "type": "AnatomicalStructure"}, {"text": "harvested", "type": "HealthCareActivity"}, {"text": "semitendinosus tendon", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We applied this technique to the hair - bearing STA flap , where primary donor - site closure is extremely beneficial for preventing baldness consequent to skin grafting .

Example answer:
{"entities": [{"text": "hair - bearing STA", "type": "AnatomicalStructure"}, {"text": "flap", "type": "AnatomicalStructure"}, {"text": "primary donor - site closure", "type": "HealthCareActivity"}, {"text": "baldness", "type": "BiologicFunction"}, {"text": "skin grafting", "type": "HealthCareActivity"}]}

Example input:
Sentence: Divided and Sliding Superficial Temporal Artery Flap for Primary Donor - site Closure Superficial temporal artery ( STA ) flaps are often used for reconstruction of hair - bearing areas .

Example answer:
{"entities": [{"text": "Superficial Temporal Artery", "type": "AnatomicalStructure"}, {"text": "Flap", "type": "AnatomicalStructure"}, {"text": "Donor - site", "type": "SpatialConcept"}, {"text": "Closure", "type": "HealthCareActivity"}, {"text": "Superficial temporal artery", "type": "AnatomicalStructure"}, {"text": "STA", "type": "AnatomicalStructure"}, {"text": "flaps", "type": "AnatomicalStructure"}, {"text": "reconstruction", "type": "HealthCareActivity"}, {"text": "hair - bearing areas", "type": "SpatialConcept"}]}

Example input:
Sentence: Therefore , we concluded that the divided and sliding STA flap could at least partially solve the donor - site problem .

Example answer:
{"entities": [{"text": "STA", "type": "AnatomicalStructure"}, {"text": "flap", "type": "AnatomicalStructure"}, {"text": "donor - site", "type": "SpatialConcept"}, {"text": "problem", "type": "Finding"}]}

Input:
Sentence: We have solved this issue by applying the divided and sliding flap technique , which was first reported for primary donor - site closure of a latissimus dorsi musculocutaneous flap .

## Item MedMentions:test:2658
Example input:
Sentence: Predictions were the poorest for aquifers where the salt water wedge was expected to extend further inland under predevelopment conditions and was therefore more dispersive prior to pumping .

Example answer:
{"entities": [{"text": "salt water", "type": "Chemical"}, {"text": "wedge", "type": "SpatialConcept"}, {"text": "inland", "type": "SpatialConcept"}]}

Example input:
Sentence: Earthworm species with soil -specific habitat preferences were spatially predicted with higher accuracy by PSS than more ubiquitous species .

Example answer:
{"entities": [{"text": "Earthworm", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "habitat", "type": "SpatialConcept"}, {"text": "PSS", "type": "HealthCareActivity"}]}

Example input:
Sentence: Based on these data , a methodology was formed to estimate a statistical predictive model of the spatial - seasonal variations in the presence of Anopheles in the Cayenne region .

Example answer:
{"entities": [{"text": "statistical predictive model", "type": "IntellectualProduct"}, {"text": "presence", "type": "Finding"}, {"text": "Anopheles", "type": "Eukaryote"}, {"text": "Cayenne region", "type": "SpatialConcept"}]}

Example input:
Sentence: Here we present new gridded ( 8x8 km ) reconstructions of pre - settlement ( 1800s ) forest composition and structure from the upper Midwestern US ( Minnesota , Wisconsin , and most of Michigan ) , using 19th Century Public Land Survey System ( PLSS ) , with estimates of relative composition , above - ground biomass , stem density , and basal area for 28 tree types .

Example answer:
{"entities": [{"text": "upper Midwestern US", "type": "SpatialConcept"}, {"text": "Minnesota", "type": "SpatialConcept"}, {"text": "Wisconsin", "type": "SpatialConcept"}, {"text": "Century Public Land Survey System", "type": "IntellectualProduct"}, {"text": "PLSS", "type": "IntellectualProduct"}, {"text": "above - ground", "type": "SpatialConcept"}, {"text": "stem", "type": "Eukaryote"}, {"text": "basal area", "type": "SpatialConcept"}, {"text": "tree", "type": "Eukaryote"}]}

Example input:
Sentence: This study investigates whether PSS data contribute to the spatial prediction of earthworm abundances in species distribution models of agricultural soils .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "PSS", "type": "HealthCareActivity"}, {"text": "earthworm", "type": "Eukaryote"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "models", "type": "IntellectualProduct"}, {"text": "agricultural", "type": "SpatialConcept"}]}

Example input:
Sentence: how nutrient enrichment ( i . e . , nitrogen availability ) affected the growth of Fucus vesiculosus , a foundational macroalgal species in the North Atlantic rocky intertidal zone , and found that nutrient -enriched algal blades showed a significant increase in tissue growth compared to individuals grown under ambient conditions .

Example answer:
{"entities": [{"text": "nutrient", "type": "Food"}, {"text": "nitrogen", "type": "Chemical"}, {"text": "growth", "type": "BiologicFunction"}, {"text": "Fucus vesiculosus", "type": "Eukaryote"}, {"text": "macroalgal", "type": "Eukaryote"}, {"text": "species", "type": "Eukaryote"}, {"text": "North Atlantic rocky intertidal zone", "type": "SpatialConcept"}, {"text": "algal blades", "type": "IntellectualProduct"}, {"text": "tissue growth", "type": "BiologicFunction"}]}

Example input:
Sentence: aquasalis near town and rural sites , and An . darlingi only found in inland sites .

Example answer:
{"entities": [{"text": "aquasalis", "type": "Eukaryote"}, {"text": "An . darlingi", "type": "Eukaryote"}, {"text": "inland sites", "type": "SpatialConcept"}]}

Example input:
Sentence: To carry out the ecohydrological modeling , the following information was used : bathymetry , physical and hydraulic features , and the Habitat Suitability Index for species of the Hypostomus auroguttatus .

Example answer:
{"entities": [{"text": "ecohydrological modeling", "type": "ResearchActivity"}, {"text": "Habitat", "type": "SpatialConcept"}, {"text": "species", "type": "IntellectualProduct"}, {"text": "Hypostomus auroguttatus", "type": "Eukaryote"}]}

Example input:
Sentence: auroguttatus Adult , the highest value of Weighted Usable Area was associated with the percentage of 100 % of the average long - term streamflow in September .

Example answer:
{"entities": [{"text": "auroguttatus", "type": "Eukaryote"}, {"text": "Area", "type": "SpatialConcept"}]}

Example input:
Sentence: auroguttatus Juvenile , higher values of Weighted Usable Area were associated with the percentage of 60 % and 70 % of the average long - term streamflows in October and September , respectively .

Example answer:
{"entities": [{"text": "auroguttatus", "type": "Eukaryote"}, {"text": "Area", "type": "SpatialConcept"}]}

Input:
Sentence: aquasalis presence that integrated marsh and forest surface area was extrapolated to generate predictive maps .

## Item MedMentions:test:2791
Example input:
Sentence: Compound 1 exhibited significant inhibition on NO production with an IC50 value of 9 .

Example answer:
{"entities": [{"text": "Compound 1", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}]}

Example input:
Sentence: The change of CDR - SB from baseline to 2 years exhibited significant negative associations with the average ( β = -0 . 150 , p = 0 . 006 ) and minimum GCIPL thicknesses as well as GCIPL thickness in the superotemporal , superior , superonasal , and inferonasal sectors at baseline .

Example answer:
{"entities": [{"text": "CDR - SB", "type": "IntellectualProduct"}, {"text": "negative", "type": "Finding"}, {"text": "minimum GCIPL", "type": "AnatomicalStructure"}, {"text": "GCIPL", "type": "AnatomicalStructure"}, {"text": "superotemporal", "type": "SpatialConcept"}, {"text": "superior", "type": "SpatialConcept"}, {"text": "superonasal", "type": "SpatialConcept"}, {"text": "inferonasal sectors", "type": "SpatialConcept"}]}

Example input:
Sentence: A comparison of γH2AX and 53BP1 quantifications in double - staine d biopsies showed similar HRS dose - response relationships .

Example answer:
{"entities": [{"text": "γH2AX", "type": "AnatomicalStructure"}, {"text": "53BP1", "type": "AnatomicalStructure"}, {"text": "biopsies", "type": "HealthCareActivity"}]}

Example input:
Sentence: 99mg / mL ) and DPPH assay ( 88 . 65 % , EC50 = 212 . 33μg / ml ) .

Example answer:
{"entities": [{"text": "DPPH", "type": "Chemical"}, {"text": "assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: To determine optimal concentration , B - CSM was firstly added at varying amounts ( 5 , 10 , 20 , 40 , and 60 % ) relative to culture medium .

Example answer:
{"entities": [{"text": "B - CSM", "type": "Chemical"}, {"text": "culture medium", "type": "Chemical"}]}

Example input:
Sentence: Median creatinine and eGFR were 67 μmol / L and 112 mL / min / 1 . 73 m2 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "eGFR", "type": "HealthCareActivity"}]}

Example input:
Sentence: There was no significant effect on PAM - 13 ( estimated mean difference ( emd ) -0 . 41 , 95 % CI ( CI ) : - 7 . 49 - 6 . 67 ) , nor on the RAS ( emd 0 . 02 , CI : - 0 . 27 - 0 . 31 ) or BASIS - 32 ( 0 . 09 , CI : - 0 . 28 - 0 . 45 ) .

Example answer:
{"entities": [{"text": "PAM - 13", "type": "IntellectualProduct"}, {"text": "RAS", "type": "IntellectualProduct"}, {"text": "BASIS - 32", "type": "IntellectualProduct"}]}

Example input:
Sentence: In DEXCHNP , the IC50 was 20 . 12 μg / ml for HEK and 7 . 37 μg / ml for RAW264 .

Example answer:
{"entities": [{"text": "HEK", "type": "AnatomicalStructure"}, {"text": "RAW264 .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Preliminary pharmacokinetic studies with EC508 used intravenous and oral administration in male rats .

Example answer:
{"entities": [{"text": "pharmacokinetic studies", "type": "ResearchActivity"}, {"text": "EC508", "type": "Chemical"}, {"text": "intravenous", "type": "SpatialConcept"}, {"text": "oral administration", "type": "HealthCareActivity"}, {"text": "rats", "type": "Eukaryote"}]}

Example input:
Sentence: Lastly , the authors constructed a nonlinear dose - response numerical model for these synoptic sediment PCB concentrations and biological effects : Y = 100 / 1 + 10 ( ( [ logEC50 - logX ] × [ Hill slope ] ) ) ( EC50 = median effective concentration ) .

Example answer:
{"entities": [{"text": "dose - response numerical model", "type": "IntellectualProduct"}, {"text": "PCB", "type": "Chemical"}]}

Input:
Sentence: Median effect concentrations ( EC50s ) for B .

## Item MedMentions:test:2732
Example input:
Sentence: The functional and aesthetic assessments were performed at least 6 months after surgery , and the results were compared statistically with a control group .

Example answer:
{"entities": [{"text": "assessments", "type": "HealthCareActivity"}, {"text": "surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: 2 years ) , 29 . 0 % ( 20 / 69 ) of patients had recurrence and 18 . 8 % ( 13 / 69 ) required reoperation at median time of 4 . 8 years ( 3 . 1 - 9 . 1 years ) after the initial repair .

Example answer:
{"entities": [{"text": "recurrence", "type": "BiologicFunction"}, {"text": "reoperation", "type": "HealthCareActivity"}, {"text": "initial repair", "type": "HealthCareActivity"}]}

Example input:
Sentence: Clinical evaluations showed that all photoaging parameters improved significantly from baseline as early as Week 12 and the amelioration continued until Week 52 .

Example answer:
{"entities": [{"text": "Clinical evaluations", "type": "HealthCareActivity"}, {"text": "photoaging", "type": "InjuryOrPoisoning"}, {"text": "parameters", "type": "Finding"}]}

Example input:
Sentence: Both patients fully recovered and both showed a complete relief of symptoms at 3 months following the procedure .

Example answer:
{"entities": [{"text": "relief", "type": "Finding"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: 4 ; 95 % CI , -8 . 1 to -2 . 6 ; P < .001 ) , and the treatment effect was maintained for at least 12 months ( -15 . 4 vs -11 .

Example answer:
{"entities": [{"text": "treatment", "type": "HealthCareActivity"}]}

Example input:
Sentence: The median OS for the patients treated in the TKI era was 22 months ( 95 % confidence interval [ CI ] , 17 - 25 months ) compared with 14 months ( 95 % CI , 10 - 19 months ; P < .01 ) for the historical controls .

Example answer:
{"entities": [{"text": "treated", "type": "HealthCareActivity"}, {"text": "TKI", "type": "Chemical"}, {"text": "historical controls", "type": "PopulationGroup"}]}

Example input:
Sentence: Further improvements were detected at 24 months ( AOFAS , from 57 . 1 ± 14 . 9 before surgery to 86 . 6 ± 10 .

Example answer:
{"entities": [{"text": "AOFAS", "type": "IntellectualProduct"}]}

Example input:
Sentence: During the median 21 . 5 months follow - up ( range , 3 - 119 months ) , 36 ( 76 . 6 % ) patients showed good outcomes ( improved to below BNI class IIIa ) .

Example answer:
{"entities": [{"text": "median", "type": "SpatialConcept"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "class IIIa", "type": "IntellectualProduct"}]}

Example input:
Sentence: At the 36 - month follow - up examination , there was continual evidence of satisfactory reduction and fusion .

Example answer:
{"entities": [{"text": "follow - up", "type": "HealthCareActivity"}, {"text": "examination", "type": "HealthCareActivity"}, {"text": "satisfactory", "type": "Finding"}, {"text": "reduction", "type": "HealthCareActivity"}, {"text": "fusion", "type": "HealthCareActivity"}]}

Example input:
Sentence: Successful Restoration of Severely Mutilated Primary Incisors Using a Novel Method to Retain Zirconia Crowns - Two Year Results This manuscript describes a simple reliable technique for restoring severely mutilated primary anterior teeth .

Example answer:
{"entities": [{"text": "Successful Restoration", "type": "HealthCareActivity"}, {"text": "Primary Incisors", "type": "AnatomicalStructure"}, {"text": "Crowns", "type": "MedicalDevice"}, {"text": "manuscript", "type": "IntellectualProduct"}, {"text": "restoring", "type": "HealthCareActivity"}, {"text": "primary anterior teeth", "type": "AnatomicalStructure"}]}

Input:
Sentence: Restorations were evaluated at baseline and at 6 , 12 , 18 , and 24 months by two blinded independent examiners using modified FDI criteria .

## Item MedMentions:test:2697
Example input:
Sentence: Using data obtained by the Surveillance , Epidemiology , and End Results ( SEER ) program from 2010 - 2012 , a retrospective , population - based cohort study was conducted to investigate tumor subtype - specific differences in various characteristics , overall survival ( OS ) and breast cancer - specific mortality ( BCSM ) between males and females .

Example answer:
{"entities": [{"text": "Surveillance , Epidemiology , and End Results ( SEER ) program", "type": "Organization"}, {"text": "population - based cohort study", "type": "ResearchActivity"}, {"text": "tumor subtype", "type": "IntellectualProduct"}]}

Example input:
Sentence: The breast cancer mortality reduction in the invited population due to screening and the percentage of females diagnosed with symptomatic breast cancer , who die from breast cancer , were collated from the literature .

Example answer:
{"entities": [{"text": "breast cancer", "type": "BiologicFunction"}, {"text": "invited population", "type": "PopulationGroup"}, {"text": "screening", "type": "HealthCareActivity"}, {"text": "diagnosed", "type": "Finding"}, {"text": "literature", "type": "IntellectualProduct"}]}

Example input:
Sentence: Given the higher prevalence and earlier onset of type 2 diabetes in Black women , it is likely that diabetes contributes to racial disparities in breast cancer mortality .

Example answer:
{"entities": [{"text": "earlier onset", "type": "Finding"}, {"text": "type 2 diabetes", "type": "BiologicFunction"}, {"text": "Black women", "type": "PopulationGroup"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "racial", "type": "PopulationGroup"}, {"text": "disparities", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Among 228 , 511 women identified , the percentage of blacks with stage IIIC / IV disease at diagnosis was nearly twice that of non - Hispanic whites ( 17 . 8 % vs 9 . 8 % ; P < 0 . 001 ) .

Example answer:
{"entities": [{"text": "women", "type": "PopulationGroup"}, {"text": "blacks", "type": "PopulationGroup"}, {"text": "stage IIIC / IV disease at diagnosis", "type": "IntellectualProduct"}, {"text": "non - Hispanic whites", "type": "PopulationGroup"}]}

Example input:
Sentence: Overall , breast cancer was detected in 543 women , with a detection rate of 10 . 3 per 1 , 000 persons .

Example answer:
{"entities": [{"text": "breast cancer", "type": "BiologicFunction"}, {"text": "detected", "type": "Finding"}, {"text": "women", "type": "PopulationGroup"}, {"text": "persons", "type": "PopulationGroup"}]}

Example input:
Sentence: Women with resectable breast cancer from 1990 to 2007 in the Surveillance , Epidemiology , and End Results database ( n = 199 , 963 ) were analyzed .

Example answer:
{"entities": [{"text": "Women", "type": "PopulationGroup"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "Surveillance , Epidemiology , and End Results database", "type": "Organization"}, {"text": "analyzed", "type": "ResearchActivity"}]}

Example input:
Sentence: We examined factors associated with negative psychological consequences of a breast cancer diagnosis , in a diverse sample of 910 recently diagnosed patients ( 378 African - American , 372 White , and 160 Latina ) .

Example answer:
{"entities": [{"text": "examined", "type": "Finding"}, {"text": "negative", "type": "Finding"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "diagnosed", "type": "Finding"}, {"text": "African - American", "type": "PopulationGroup"}, {"text": "White", "type": "PopulationGroup"}, {"text": "Latina", "type": "PopulationGroup"}]}

Example input:
Sentence: There were 368 deaths during follow - up , of which 273 were due to breast cancer .

Example answer:
{"entities": [{"text": "deaths", "type": "Finding"}, {"text": "follow - up", "type": "HealthCareActivity"}, {"text": "breast cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Diabetes and breast cancer mortality in Black women Breast cancer mortality is higher in Black women than in White women .

Example answer:
{"entities": [{"text": "Diabetes", "type": "BiologicFunction"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "Black women", "type": "PopulationGroup"}, {"text": "Breast cancer", "type": "BiologicFunction"}, {"text": "White women", "type": "PopulationGroup"}]}

Example input:
Sentence: African - American and Latina women reported greater psychological consequences related to their breast cancer diagnosis ; this disparity was mediated by differences in unmet social support .

Example answer:
{"entities": [{"text": "African - American", "type": "PopulationGroup"}, {"text": "Latina", "type": "SpatialConcept"}, {"text": "women", "type": "PopulationGroup"}, {"text": "breast cancer", "type": "BiologicFunction"}, {"text": "diagnosis", "type": "Finding"}, {"text": "disparity", "type": "Finding"}]}

Input:
Sentence: 1 , 621 Black women with invasive breast cancer diagnosed in 1995 - 2013 were followed by mailed questionnaires and searches of the National Death Index .

## Item MedMentions:test:2630
Example input:
Sentence: LAMP - 2 mediates oxidative stress -dependent cell death in Zn ( 2 + ) - treated lung epithelium cells Zinc is an essential element for the biological system .

Example answer:
{"entities": [{"text": "LAMP - 2", "type": "Chemical"}, {"text": "oxidative stress", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "Zn ( 2 + )", "type": "Chemical"}, {"text": "treated", "type": "HealthCareActivity"}, {"text": "lung", "type": "AnatomicalStructure"}, {"text": "epithelium cells", "type": "AnatomicalStructure"}, {"text": "Zinc", "type": "Chemical"}, {"text": "element", "type": "Chemical"}, {"text": "biological system", "type": "BodySystem"}]}

Example input:
Sentence: To investigate thiamine 's role in symbiosis , we focused on THI1 , a thiamine - biosynthesis gene expressed in roots , nodules , and seeds .

Example answer:
{"entities": [{"text": "thiamine 's", "type": "Chemical"}, {"text": "THI1", "type": "AnatomicalStructure"}, {"text": "thiamine - biosynthesis gene", "type": "AnatomicalStructure"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "roots", "type": "Eukaryote"}, {"text": "nodules", "type": "Eukaryote"}, {"text": "seeds", "type": "Eukaryote"}]}

Example input:
Sentence: Despite robust activation of the intestinal innate immune response , mice lacking acinar Orai1 exhibited intestinal bacterial outgrowth and dysbiosis , ultimately causing systemic translocation , inflammation , and death .

Example answer:
{"entities": [{"text": "activation of the intestinal innate immune response", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "acinar", "type": "SpatialConcept"}, {"text": "Orai1", "type": "AnatomicalStructure"}, {"text": "intestinal", "type": "AnatomicalStructure"}, {"text": "outgrowth", "type": "BiologicFunction"}, {"text": "translocation", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "death", "type": "BiologicFunction"}]}

Example input:
Sentence: irregularis stored more thiamine than the source ( host plants ) , despite lacking thiamine biosynthesis genes .

Example answer:
{"entities": [{"text": "irregularis", "type": "Eukaryote"}, {"text": "thiamine", "type": "Chemical"}, {"text": "thiamine biosynthesis genes", "type": "AnatomicalStructure"}]}

Example input:
Sentence: In particular , C9orf72 depletion leads to reduced activity of MTOR , a negative regulator of macroautophagy / autophagy , and concomitantly increased TFEB levels and nuclear translocation .

Example answer:
{"entities": [{"text": "C9orf72", "type": "AnatomicalStructure"}, {"text": "MTOR", "type": "Chemical"}, {"text": "macroautophagy", "type": "BiologicFunction"}, {"text": "autophagy", "type": "BiologicFunction"}, {"text": "TFEB", "type": "Chemical"}, {"text": "nuclear translocation", "type": "BiologicFunction"}]}

Example input:
Sentence: Argininosuccinic Acid Lyase Deficiency Missed by Newborn Screen Argininosuccinic acid lyase ( ASL ) deficiency , caused by mutations in the ASL gene ( OMIM : 608310 ) is a urea cycle disorder that has pleiotropic presentations .

Example answer:
{"entities": [{"text": "Argininosuccinic Acid Lyase Deficiency", "type": "BiologicFunction"}, {"text": "Newborn Screen", "type": "HealthCareActivity"}, {"text": "Argininosuccinic acid lyase ( ASL ) deficiency", "type": "BiologicFunction"}, {"text": "mutations", "type": "BiologicFunction"}, {"text": "ASL gene", "type": "AnatomicalStructure"}, {"text": "OMIM : 608310", "type": "IntellectualProduct"}, {"text": "urea cycle", "type": "BiologicFunction"}, {"text": "disorder", "type": "BiologicFunction"}, {"text": "pleiotropic presentations", "type": "BiologicFunction"}]}

Example input:
Sentence: Cyclic nucleotide signaling is impaired in HD models , and PDE10 loss may represent a homeostatic adaptation to maintain signaling .

Example answer:
{"entities": [{"text": "Cyclic nucleotide signaling", "type": "BiologicFunction"}, {"text": "HD", "type": "BiologicFunction"}, {"text": "models", "type": "BiologicFunction"}, {"text": "PDE10", "type": "Chemical"}, {"text": "homeostatic", "type": "BiologicFunction"}, {"text": "adaptation", "type": "BiologicFunction"}, {"text": "signaling", "type": "BiologicFunction"}]}

Example input:
Sentence: These phenotypes were rescued by THI1 complementation and by exogenous thiamine .

Example answer:
{"entities": [{"text": "THI1", "type": "AnatomicalStructure"}, {"text": "thiamine", "type": "Chemical"}]}

Example input:
Sentence: Therefore , disturbance of the thiamine supply would affect progeny phenotypes such as spore formation and hyphal growth .

Example answer:
{"entities": [{"text": "thiamine", "type": "Chemical"}, {"text": "spore formation", "type": "BiologicFunction"}, {"text": "hyphal growth", "type": "BiologicFunction"}]}

Example input:
Sentence: Binding of Pollutants to Biomolecules : A Simulation Study A number of cases around the world have been reported where animals were found dead or dying with symptoms resembling a thiamine ( vitamin B ) deficiency , and for some of these , a link to pollutants has been suggested .

Example answer:
{"entities": [{"text": "Pollutants", "type": "Chemical"}, {"text": "Biomolecules", "type": "Chemical"}, {"text": "Simulation Study", "type": "ResearchActivity"}, {"text": "world", "type": "PopulationGroup"}, {"text": "animals", "type": "Eukaryote"}, {"text": "found dead", "type": "Finding"}, {"text": "dying", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}, {"text": "thiamine", "type": "BiologicFunction"}, {"text": "( vitamin B ) deficiency", "type": "BiologicFunction"}, {"text": "pollutants", "type": "Chemical"}]}

Input:
Sentence: Loss of function produces chlorosis , a typical thiamine -deficiency phenotype , and mortality .

## Item MedMentions:test:2628
Example input:
Sentence: EphB1 receptor may be a potential target for relieving the established diabetic pain .

Example answer:
{"entities": [{"text": "EphB1 receptor", "type": "Chemical"}, {"text": "relieving", "type": "HealthCareActivity"}, {"text": "diabetic", "type": "Finding"}, {"text": "pain", "type": "Finding"}]}

Example input:
Sentence: Further , rPbHsp60 treatment ( i ) decreased the known protective effect of CFA against PCM and ( ii ) increased the concentrations of IL - 17 , TNF - α , IL - 12 , IFN - γ , IL - 4 , IL - 10 , and TGF - β in the lungs .

Example answer:
{"entities": [{"text": "rPbHsp60", "type": "Chemical"}, {"text": "CFA", "type": "Chemical"}, {"text": "PCM", "type": "BiologicFunction"}, {"text": "IL - 17", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "IL - 12", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "IL - 4", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "TGF - β", "type": "Chemical"}, {"text": "lungs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Finally , we demonstrate that CBG upregulates gene expression of the antimicrobial peptides ( AMPs ) hBD - 2 and hBD - 3 in DCs , and induces secretion of HNP1 - 3 and hCAP - 18 / LL - 37 from neutrophils , potentiating neutrophil antibacterial activity .

Example answer:
{"entities": [{"text": "CBG", "type": "Chemical"}, {"text": "upregulates", "type": "BiologicFunction"}, {"text": "gene expression", "type": "BiologicFunction"}, {"text": "antimicrobial peptides", "type": "Chemical"}, {"text": "AMPs", "type": "Chemical"}, {"text": "hBD - 2", "type": "Chemical"}, {"text": "hBD - 3", "type": "Chemical"}, {"text": "DCs", "type": "AnatomicalStructure"}, {"text": "secretion", "type": "BiologicFunction"}, {"text": "HNP1", "type": "Chemical"}, {"text": "3", "type": "Chemical"}, {"text": "hCAP - 18 / LL - 37", "type": "Chemical"}, {"text": "neutrophils", "type": "AnatomicalStructure"}, {"text": "neutrophil", "type": "AnatomicalStructure"}, {"text": "antibacterial activity", "type": "BiologicFunction"}]}

Example input:
Sentence: Peptide -based vaccination against OPN integrin binding sites does not improve cardio - metabolic disease in mice Obesity causes insulin resistance via a chronic low - grade inflammation .

Example answer:
{"entities": [{"text": "Peptide", "type": "Chemical"}, {"text": "vaccination", "type": "HealthCareActivity"}, {"text": "OPN", "type": "Chemical"}, {"text": "integrin", "type": "Chemical"}, {"text": "binding sites", "type": "Chemical"}, {"text": "cardio - metabolic disease", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "Obesity", "type": "BiologicFunction"}, {"text": "insulin resistance", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}]}

Example input:
Sentence: In particular , we discuss the possible contribution to the incretin cardiovascular effects of a direct cardiac action of GLP - 1 metabolites through GLP - 1 receptor -independent pathways , and of DPP4 substrates other than GLP - 1 .

Example answer:
{"entities": [{"text": "incretin", "type": "Chemical"}, {"text": "cardiovascular", "type": "BodySystem"}, {"text": "cardiac", "type": "AnatomicalStructure"}, {"text": "GLP - 1", "type": "Chemical"}, {"text": "metabolites", "type": "Chemical"}, {"text": "GLP - 1 receptor", "type": "Chemical"}, {"text": "pathways", "type": "BiologicFunction"}, {"text": "DPP4", "type": "Chemical"}]}

Example input:
Sentence: All patients who presented with lower urinary tract symptoms due to BPH and who met the inclusion criteria were studied .

Example answer:
{"entities": [{"text": "lower urinary tract symptoms", "type": "Finding"}, {"text": "BPH", "type": "BiologicFunction"}, {"text": "studied", "type": "ResearchActivity"}]}

Example input:
Sentence: BaPWV was positively correlated with age , systolic blood pressure ( SBP ) , diastolic blood pressure ( DBP ) , 2 - hour ( OGTT ) insulin , RBP4 , and VFA , and negatively correlated with GIR in FH2D + group .

Example answer:
{"entities": [{"text": "systolic blood pressure", "type": "ClinicalAttribute"}, {"text": "SBP", "type": "ClinicalAttribute"}, {"text": "diastolic blood pressure", "type": "ClinicalAttribute"}, {"text": "DBP", "type": "ClinicalAttribute"}, {"text": "RBP4", "type": "Chemical"}, {"text": "FH2D +", "type": "Finding"}, {"text": "group", "type": "PopulationGroup"}]}

Example input:
Sentence: Pharmacological Actions of Glucagon - Like Peptide - 1 , Gastric Inhibitory Polypeptide , and Glucagon Glucagon family of peptide hormones is a group of structurally related brain - gut peptides that exert their pleiotropic actions through interactions with unique members of class B1 G protein - coupled receptors ( GPCRs ) .

Example answer:
{"entities": [{"text": "Pharmacological Actions", "type": "BiologicFunction"}, {"text": "Glucagon - Like Peptide - 1", "type": "Chemical"}, {"text": "Gastric Inhibitory Polypeptide", "type": "Chemical"}, {"text": "Glucagon", "type": "Chemical"}, {"text": "Glucagon family", "type": "Chemical"}, {"text": "peptide hormones", "type": "Chemical"}, {"text": "brain - gut peptides", "type": "Chemical"}, {"text": "pleiotropic actions", "type": "BiologicFunction"}, {"text": "unique members of class B1", "type": "IntellectualProduct"}, {"text": "G protein - coupled receptors", "type": "Chemical"}, {"text": "GPCRs", "type": "Chemical"}]}

Example input:
Sentence: GLP - 1r blockade prevented hypoglycaemia in 100 % of individuals , normalised beta cell function and reversed neuroglycopenic symptoms , supporting the conclusion that GLP - 1 plays a primary role in mediating hyperinsulinaemic hypoglycaemia in PBH .

Example answer:
{"entities": [{"text": "GLP - 1r", "type": "Chemical"}, {"text": "hypoglycaemia", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "beta cell function", "type": "BiologicFunction"}, {"text": "reversed neuroglycopenic symptoms", "type": "Finding"}, {"text": "GLP - 1", "type": "Chemical"}, {"text": "hyperinsulinaemic hypoglycaemia", "type": "BiologicFunction"}, {"text": "PBH", "type": "BiologicFunction"}]}

Example input:
Sentence: We conducted a double - blinded crossover study wherein eight participants with confirmed PBH were assigned in random order to intravenous infusion of the GLP - 1 receptor ( GLP - 1r ) antagonist .

Example answer:
{"entities": [{"text": "double - blinded", "type": "ResearchActivity"}, {"text": "crossover study", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "PBH", "type": "BiologicFunction"}, {"text": "intravenous infusion", "type": "HealthCareActivity"}, {"text": "GLP - 1 receptor", "type": "Chemical"}, {"text": "GLP - 1r", "type": "Chemical"}, {"text": "antagonist", "type": "Chemical"}]}

Input:
Sentence: This study was designed to test the hypothesis that PBH and associated symptoms are primarily mediated by glucagon - like peptide - 1 ( GLP - 1 ) .

## Item MedMentions:test:2740
Example input:
Sentence: We hypothesized that it would also be favorable as a laparoscopic application due to unique features .

Example answer:
{"entities": [{"text": "laparoscopic application", "type": "SpatialConcept"}]}

Example input:
Sentence: Further studies will help to refine and determine the benefits of standardized protocols such as that developed in this study for the management of life - threatening laparoscopic complications .

Example answer:
{"entities": [{"text": "standardized protocols", "type": "IntellectualProduct"}, {"text": "management", "type": "HealthCareActivity"}, {"text": "life - threatening", "type": "Finding"}, {"text": "laparoscopic", "type": "HealthCareActivity"}, {"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: The Effectiveness of a Systematic Algorithm for the Management of Vascular Injuries during the Laparoscopic Surgery Currently , there is no standardized training protocol to teach surgeons how to deal with vascular injuries during laparoscopic procedures .

Example answer:
{"entities": [{"text": "Systematic Algorithm", "type": "IntellectualProduct"}, {"text": "Management", "type": "HealthCareActivity"}, {"text": "Vascular Injuries", "type": "InjuryOrPoisoning"}, {"text": "Laparoscopic Surgery", "type": "HealthCareActivity"}, {"text": "training protocol", "type": "IntellectualProduct"}, {"text": "surgeons", "type": "ProfessionalOrOccupationalGroup"}, {"text": "vascular injuries", "type": "InjuryOrPoisoning"}, {"text": "laparoscopic procedures", "type": "HealthCareActivity"}]}

Example input:
Sentence: Future studies should focus on longer - term durability and comparisons with laparoscopic techniques .

Example answer:
{"entities": [{"text": "longer - term durability", "type": "Finding"}, {"text": "laparoscopic techniques", "type": "HealthCareActivity"}]}

Example input:
Sentence: Introducing enhanced haptic feedback in laparoscopic instruments might well improve surgical safety and efficiency .

Example answer:
{"entities": [{"text": "laparoscopic instruments", "type": "MedicalDevice"}, {"text": "improve", "type": "Finding"}]}

Example input:
Sentence: Therefore , haptic feedback is considered an unmet need in laparoscopy .

Example answer:
{"entities": [{"text": "laparoscopy", "type": "HealthCareActivity"}]}

Example input:
Sentence: The questionnaire was distributed to a group of laparoscopic surgeons based in Europe .

Example answer:
{"entities": [{"text": "questionnaire", "type": "IntellectualProduct"}, {"text": "laparoscopic surgeons", "type": "ProfessionalOrOccupationalGroup"}, {"text": "Europe", "type": "SpatialConcept"}]}

Example input:
Sentence: A questionnaire was designed to determine surgeons ' use and preferences for laparoscopic instruments and expectations about enhanced haptic feedback .

Example answer:
{"entities": [{"text": "questionnaire", "type": "IntellectualProduct"}, {"text": "surgeons '", "type": "ProfessionalOrOccupationalGroup"}, {"text": "laparoscopic instruments", "type": "MedicalDevice"}]}

Example input:
Sentence: Surgeons were also asked whether they experience physical complaints related to laparoscopic instruments .

Example answer:
{"entities": [{"text": "Surgeons", "type": "ProfessionalOrOccupationalGroup"}, {"text": "laparoscopic instruments", "type": "MedicalDevice"}]}

Example input:
Sentence: Of all respondents , 77 % reported physical complaints directly attributable to the use of laparoscopic instruments .

Example answer:
{"entities": [{"text": "respondents", "type": "PopulationGroup"}, {"text": "laparoscopic instruments", "type": "MedicalDevice"}]}

Input:
Sentence: This study stresses that the high prevalence of physical complaints directly related to laparoscopic instruments among laparoscopic surgeons is still relevant .

## Item MedMentions:test:2872
Example input:
Sentence: Data from a multiple baseline design indicated that all children acquired the targeted skills and demonstrated high levels of generalization of these skills to untrained context .

Example answer:
{"entities": [{"text": "baseline design", "type": "ResearchActivity"}, {"text": "generalization", "type": "BiologicFunction"}, {"text": "untrained", "type": "Finding"}]}

Example input:
Sentence: Although a positive perception of their educational environment was found , minor corrective measures need to be implemented .

Example answer:
{"entities": [{"text": "perception", "type": "BiologicFunction"}]}

Example input:
Sentence: Other highly prevalent strategies in the school context include Search for Information , Emotion , and Social Support .

Example answer:
{"entities": [{"text": "Emotion", "type": "BiologicFunction"}]}

Example input:
Sentence: The vast majority of service providers ( 93 . 4 % ) reported that ENGAGE had impacted their work practice up to 5 - month post training .

Example answer:
{"entities": [{"text": "reported", "type": "HealthCareActivity"}, {"text": "ENGAGE", "type": "Organization"}]}

Example input:
Sentence: Multivariable regression analyses examined student , family , and school factors affecting engagement .

Example answer:
{"entities": [{"text": "Multivariable regression analyses", "type": "IntellectualProduct"}, {"text": "student", "type": "PopulationGroup"}]}

Example input:
Sentence: They were more likely to prefer a personal engagement strategy , valued scientific evidence , preferred a more active approach to safety education , and advocated disclosure of errors .

Example answer:
{"entities": [{"text": "engagement", "type": "HealthCareActivity"}, {"text": "approach", "type": "SpatialConcept"}]}

Example input:
Sentence: Hence , it is imperative that education interventions are needed to bring or sustain positive change .

Example answer:
{"entities": [{"text": "education interventions", "type": "HealthCareActivity"}, {"text": "positive", "type": "Finding"}]}

Example input:
Sentence: Cross - sectional study assessing school engagement .

Example answer:
{"entities": [{"text": "Cross - sectional study", "type": "ResearchActivity"}]}

Example input:
Sentence: To investigate school engagement for students with ADHD during the crucial high school transition period and to identify factors associated with low school engagement .

Example answer:
{"entities": [{"text": "students", "type": "PopulationGroup"}, {"text": "ADHD", "type": "BiologicFunction"}, {"text": "low school engagement", "type": "Finding"}]}

Example input:
Sentence: School engagement is measured as student attitudes to school ( cognitive and emotional ) and suspension rates ( behavioural ) .

Example answer:
{"entities": [{"text": "school", "type": "Organization"}, {"text": "cognitive", "type": "BiologicFunction"}, {"text": "emotional", "type": "BiologicFunction"}]}

Input:
Sentence: School engagement is potentially modifiable , and targeting engagement may be a means to improve education outcomes .

## Item MedMentions:test:2567
Example input:
Sentence: Prevalence of HPV positivity was 43 . 9 % with an average age of 35 .

Example answer:
{"entities": [{"text": "HPV positivity", "type": "Finding"}]}

Example input:
Sentence: Women older than 50 years were a high - risk group for HR - HPV infection and cervical cancer .

Example answer:
{"entities": [{"text": "HR - HPV infection", "type": "BiologicFunction"}, {"text": "cervical cancer", "type": "BiologicFunction"}]}

Example input:
Sentence: Statistically significant correlations were found only in MB between parameters HPV - p53 , p53 - pRb and p53 - p16 .

Example answer:
{"entities": [{"text": "parameters", "type": "Finding"}, {"text": "HPV", "type": "Virus"}, {"text": "p53", "type": "Chemical"}, {"text": "pRb", "type": "Chemical"}, {"text": "p16", "type": "Chemical"}]}

Example input:
Sentence: HPV DNA was amplified using polymerase chain reaction ( PCR ) and HPV genotypes were identified by reverse hybridization .

Example answer:
{"entities": [{"text": "HPV DNA", "type": "Chemical"}, {"text": "amplified", "type": "BiologicFunction"}, {"text": "polymerase chain reaction", "type": "ResearchActivity"}, {"text": "PCR", "type": "ResearchActivity"}, {"text": "HPV", "type": "Virus"}, {"text": "reverse hybridization", "type": "ResearchActivity"}]}

Example input:
Sentence: It is concluded that in Cuban HCV - infected patients , the responder homogeneous variant rs8099917TT is the most frequent genotype .

Example answer:
{"entities": [{"text": "Cuban", "type": "PopulationGroup"}, {"text": "HCV", "type": "Virus"}, {"text": "infected", "type": "Finding"}, {"text": "responder", "type": "Finding"}, {"text": "variant", "type": "AnatomicalStructure"}, {"text": "rs8099917TT", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Tumors positive for any other high - risk HPV genotype were classified as non - HPV16 - positive .

Example answer:
{"entities": [{"text": "Tumors", "type": "BiologicFunction"}, {"text": "positive for", "type": "Finding"}, {"text": "high - risk", "type": "Finding"}, {"text": "HPV genotype", "type": "Chemical"}, {"text": "classified", "type": "IntellectualProduct"}, {"text": "non - HPV16 - positive", "type": "Finding"}]}

Example input:
Sentence: The prevalence of HR - HPV among women older than 50 years was significantly higher than the other groups ( P < 0 .

Example answer:
{"entities": [{"text": "HR - HPV", "type": "Virus"}]}

Example input:
Sentence: As opposed to other studies , HPV 52 was the third most commonly encountered strain after HPV 16 and HPV 18 .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "HPV 52", "type": "Virus"}, {"text": "encountered", "type": "HealthCareActivity"}, {"text": "HPV 16", "type": "Virus"}, {"text": "HPV 18", "type": "Virus"}]}

Example input:
Sentence: The main carcinogenic genotypes were HPV - 16 , HPV - 18 , HPV - 58 , HPV - 52 , and HPV - 31 . HPV - 16 and HPV - 18 combined caused 80 .

Example answer:
{"entities": [{"text": "carcinogenic", "type": "Chemical"}, {"text": "HPV - 16", "type": "Virus"}, {"text": "HPV - 18", "type": "Virus"}, {"text": "HPV - 58", "type": "Virus"}, {"text": "HPV - 52", "type": "Virus"}, {"text": "HPV - 31", "type": "Virus"}]}

Example input:
Sentence: HPV 16 was the commonest strain ( N = 57 , 73 . 08 % ) followed by HPV 18 ( N = 28 , 35 . 90 % ) .

Example answer:
{"entities": [{"text": "HPV 16", "type": "Virus"}, {"text": "HPV 18", "type": "Virus"}]}

Input:
Sentence: The most common HR - HPV genotypes were HPV - 16 , HPV - 58 , HPV - 52 , HPV - 18 , and HPV - 31 .

## Item MedMentions:test:2546
Example input:
Sentence: Lentiviral vector containing small interfering RNA targeting Siglec - 1 ( Lv - shSiglec - 1 ) or control vector ( Lv - shNC ) were injected intravenously into 6 - week old Apoe ( - / - ) mice .

Example answer:
{"entities": [{"text": "Lentiviral vector", "type": "Chemical"}, {"text": "small interfering RNA", "type": "Chemical"}, {"text": "Siglec - 1", "type": "AnatomicalStructure"}, {"text": "Lv - shSiglec - 1", "type": "Chemical"}, {"text": "control vector", "type": "Chemical"}, {"text": "Lv - shNC", "type": "Chemical"}, {"text": "intravenously", "type": "SpatialConcept"}, {"text": "Apoe ( - / - )", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Importantly , even though the immune system of newborns may be characterized as developmentally immature , with a propensity to develop Th2 immunity , significant CD8 + T - cell responses may still be elicited in the context of optimal priming .

Example answer:
{"entities": [{"text": "immune system", "type": "BodySystem"}, {"text": "developmentally", "type": "BiologicFunction"}, {"text": "Th2", "type": "AnatomicalStructure"}, {"text": "immunity", "type": "BiologicFunction"}, {"text": "CD8 + T - cell", "type": "AnatomicalStructure"}, {"text": "responses", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study , we used adeno - associated virus ( AAV ) serotype 9 ( AAV9 ) to deliver a functional NPC1 gene systemically into NPC1 ( - / - ) mice at postnatal day 4 .

Example answer:
{"entities": [{"text": "adeno - associated virus", "type": "Virus"}, {"text": "AAV", "type": "Virus"}, {"text": "serotype 9", "type": "IntellectualProduct"}, {"text": "AAV9", "type": "Virus"}, {"text": "NPC1 gene", "type": "AnatomicalStructure"}, {"text": "NPC1 ( - / - )", "type": "AnatomicalStructure"}, {"text": "mice", "type": "Eukaryote"}, {"text": "postnatal day 4", "type": "HealthCareActivity"}]}

Example input:
Sentence: Female BALB / c mice were vaccinated with 100 μg of purified recombinant vector intramuscularly 3 times at two - week intervals and the levels of five cytokines including IFN - γ , IL - 12 , IL - 4 , IL - 10 and TGF - β were measured .

Example answer:
{"entities": [{"text": "BALB / c mice", "type": "Eukaryote"}, {"text": "vaccinated", "type": "HealthCareActivity"}, {"text": "recombinant", "type": "Chemical"}, {"text": "vector", "type": "Chemical"}, {"text": "intramuscularly", "type": "SpatialConcept"}, {"text": "cytokines", "type": "Chemical"}, {"text": "IFN - γ", "type": "Chemical"}, {"text": "IL - 12", "type": "Chemical"}, {"text": "IL - 4", "type": "Chemical"}, {"text": "IL - 10", "type": "Chemical"}, {"text": "TGF - β", "type": "Chemical"}]}

Example input:
Sentence: We aimed to improve the efficacy and safety of adoptive T - cell transfer by using adenoviral vectors for direct delivery of immunomodulatory murine cytokines into B16 .

Example answer:
{"entities": [{"text": "adoptive T - cell transfer", "type": "HealthCareActivity"}, {"text": "adenoviral vectors", "type": "Chemical"}, {"text": "immunomodulatory", "type": "HealthCareActivity"}, {"text": "murine", "type": "Eukaryote"}, {"text": "cytokines", "type": "Chemical"}, {"text": "B16 .", "type": "AnatomicalStructure"}]}

Example input:
Sentence: We further tested the impact of maternal immunity against our replication - deficient adenoviral vector during early life vaccination .

Example answer:
{"entities": [{"text": "maternal", "type": "Finding"}, {"text": "immunity", "type": "BiologicFunction"}, {"text": "replication - deficient", "type": "BiologicFunction"}, {"text": "adenoviral vector", "type": "Chemical"}, {"text": "vaccination", "type": "HealthCareActivity"}]}

Example input:
Sentence: The aim of the present study was therefore to assess whether replication - deficient adenovectors could overcome the risk of overwhelming antigen stimulation during the first period of life and provide a pertinent alternative in infant vaccinology .

Example answer:
{"entities": [{"text": "replication - deficient", "type": "BiologicFunction"}, {"text": "adenovectors", "type": "Chemical"}, {"text": "antigen stimulation", "type": "BiologicFunction"}, {"text": "vaccinology", "type": "HealthCareActivity"}]}

Example input:
Sentence: Replication deficient adenoviral vectors have been demonstrated to induce potent CD8 + T - cell response in mice , primates and humans .

Example answer:
{"entities": [{"text": "Replication deficient", "type": "BiologicFunction"}, {"text": "adenoviral vectors", "type": "Chemical"}, {"text": "CD8 + T - cell", "type": "AnatomicalStructure"}, {"text": "response", "type": "BiologicFunction"}, {"text": "mice", "type": "Eukaryote"}, {"text": "primates", "type": "Eukaryote"}, {"text": "humans", "type": "Eukaryote"}]}

Example input:
Sentence: Overall , our results indicate that memory CD8 + T cells induced by adenoviral vectors in infant mice are of good quality and match those elicited in the adult host .

Example answer:
{"entities": [{"text": "memory", "type": "AnatomicalStructure"}, {"text": "CD8 + T cells", "type": "AnatomicalStructure"}, {"text": "adenoviral vectors", "type": "Chemical"}, {"text": "infant", "type": "Eukaryote"}, {"text": "mice", "type": "Eukaryote"}]}

Example input:
Sentence: Early life vaccination : Generation of adult - quality memory CD8 + T cells in infant mice using non - replicating adenoviral vectors Intracellular pathogens represent a serious threat during early life .

Example answer:
{"entities": [{"text": "vaccination", "type": "HealthCareActivity"}, {"text": "memory", "type": "AnatomicalStructure"}, {"text": "CD8 + T cells", "type": "AnatomicalStructure"}, {"text": "infant", "type": "Eukaryote"}, {"text": "mice", "type": "Eukaryote"}, {"text": "non - replicating", "type": "BiologicFunction"}, {"text": "adenoviral vectors", "type": "Chemical"}, {"text": "Intracellular", "type": "SpatialConcept"}]}

Input:
Sentence: To address this , infant mice were vaccinated with three different adenoviral vectors and the CD8 + T - cell response after early life vaccination was explored .

## Item MedMentions:test:2829
Example input:
Sentence: Rapid intervention necessitates the capacity to generate , grow , and genetically manipulate infectious CoVs in order to rapidly evaluate pathogenic mechanisms , host and tissue permissibility , and candidate antiviral therapeutic efficacy .

Example answer:
{"entities": [{"text": "Rapid intervention", "type": "HealthCareActivity"}, {"text": "genetically manipulate", "type": "ResearchActivity"}, {"text": "infectious CoVs", "type": "BiologicFunction"}, {"text": "pathogenic", "type": "Finding"}, {"text": "host and tissue permissibility", "type": "BiologicFunction"}, {"text": "antiviral therapeutic efficacy", "type": "HealthCareActivity"}]}

Example input:
Sentence: In particular , CRISPR - Cas9 shows highly efficient gene editing activity for therapeutic purposes in systems ranging from patient stem cells to animal models .

Example answer:
{"entities": [{"text": "CRISPR - Cas9", "type": "BiologicFunction"}, {"text": "gene editing", "type": "ResearchActivity"}, {"text": "stem cells", "type": "AnatomicalStructure"}, {"text": "animal models", "type": "Eukaryote"}]}

Example input:
Sentence: The central concepts of genomic instability fit nicely with the mutator phenotype hypothesis proposed by Lawrence Loeb , both of which represent functionally similar frameworks for describing how genomic stability can be compromised .

Example answer:
{"entities": [{"text": "genomic instability", "type": "BiologicFunction"}, {"text": "Lawrence Loeb", "type": "ProfessionalOrOccupationalGroup"}, {"text": "genomic stability", "type": "BiologicFunction"}]}

Example input:
Sentence: The results from this study indicate that the molecular signature of AD treatment may include a much broader range of genomic markers than previously hypothesized , suggesting that response to medication may be as complex as the pathology .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "AD", "type": "BiologicFunction"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "genomic markers", "type": "BiologicFunction"}, {"text": "response", "type": "ClinicalAttribute"}, {"text": "medication", "type": "Chemical"}]}

Example input:
Sentence: It was found that the short - term therapeutic efficacy ( CR rate ) was higher in the group of patients carrying the homozygous mutation of XRCC1 - 399 ( A / A genotype ) than in the group of patients without the XRCC1 - 399 mutation ( G / G genotype ) .

Example answer:
{"entities": [{"text": "CR", "type": "Finding"}, {"text": "homozygous mutation", "type": "BiologicFunction"}, {"text": "XRCC1 - 399", "type": "AnatomicalStructure"}, {"text": "A", "type": "Chemical"}, {"text": "mutation", "type": "BiologicFunction"}, {"text": "G", "type": "Chemical"}]}

Example input:
Sentence: The aim of this research is to propose a practical implementation of the notion of actionability , a common criteria justifying the disclosure of secondary findings but whose interpretation varies greatly among professionals .

Example answer:
{"entities": [{"text": "research", "type": "ResearchActivity"}, {"text": "findings", "type": "Finding"}, {"text": "interpretation", "type": "IntellectualProduct"}, {"text": "professionals", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: We distinguish three types of actionability corresponding to ( 1 ) well - established medical actions , ( 2 ) patient -initiated health - related actions and ( 3 ) life - plan decisions .

Example answer:
{"entities": [{"text": "life - plan decisions", "type": "BiologicFunction"}]}

Example input:
Sentence: The mutation burden in the involved tissues likely accounts for the variable manifestations .

Example answer:
{"entities": [{"text": "mutation", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "variable manifestations", "type": "Finding"}]}

Example input:
Sentence: A clinically actionable pathogenic or likely pathogenic variant was identified in 40 of 302 cases ( 13 % ) .

Example answer:
{"entities": [{"text": "pathogenic", "type": "Finding"}]}

Example input:
Sentence: Regarding variants of uncertain clinical significance in actionable genes , we found that different understandings of autonomy lead to different conclusions and that , for some of them , it may be legitimate to refrain from returning uncertain information .

Example answer:
{"entities": [{"text": "variants", "type": "AnatomicalStructure"}, {"text": "clinical significance", "type": "Finding"}, {"text": "genes", "type": "AnatomicalStructure"}]}

Input:
Sentence: We argue that actionability depends on the characteristics of the mutation or gene and on the values of patients .

## Item MedMentions:test:2855
Example input:
Sentence: With a 5 - year survival rate of just 8 % , pancreatic cancer ( PC ) is projected to be the second leading cause of cancer deaths by 2030 .

Example answer:
{"entities": [{"text": "pancreatic cancer", "type": "BiologicFunction"}, {"text": "PC", "type": "BiologicFunction"}]}

Example input:
Sentence: Preterm infants at 36 weeks PMA have comparable measurements of twist to term infants .

Example answer:
{"entities": [{"text": "twist", "type": "SpatialConcept"}]}

Example input:
Sentence: We conducted a prospective analysis of risk factors and length of survival among pancreatic cancer patients living in Oklahoma between 1997 and 2012 ( n = 6 , 291 ) .

Example answer:
{"entities": [{"text": "prospective analysis", "type": "ResearchActivity"}, {"text": "risk factors", "type": "Finding"}, {"text": "Oklahoma", "type": "SpatialConcept"}]}

Example input:
Sentence: The ventral pancreas encompassed almost the entire circumference of the pyloric ring , suggesting a subtype of annular pancreas .

Example answer:
{"entities": [{"text": "ventral pancreas", "type": "AnatomicalStructure"}, {"text": "encompassed", "type": "SpatialConcept"}, {"text": "pyloric ring", "type": "AnatomicalStructure"}, {"text": "subtype", "type": "IntellectualProduct"}, {"text": "annular pancreas", "type": "AnatomicalStructure"}]}

Example input:
Sentence: 6 % ID / g at 15min ) , with corresponding high tumor -to - blood ( T / B ) , tumor -to - muscle ( T / M ) , and tumor -to - pancreas ( T / P ) ratios ( T / B = 2 . 55 , T / M = 22 .

Example answer:
{"entities": [{"text": "tumor -to - blood", "type": "Finding"}, {"text": "T / B", "type": "Finding"}, {"text": "tumor -to - muscle", "type": "Finding"}, {"text": "T / M", "type": "Finding"}, {"text": "tumor -to - pancreas ( T / P ) ratios", "type": "Finding"}]}

Example input:
Sentence: 4 weeks and their infants had a mean birthweight of 3138 ± 677 g .

Example answer:
{"entities": []}

Example input:
Sentence: Incomplete Annular Pancreas with Ectopic Opening of the Pancreatic and Bile Ducts into the Pyloric Ring : First Report of a Rare Anomaly The patient was a 56 - year - old woman who had experienced epigastralgia and dorsal pain several times over the last 20 years .

Example answer:
{"entities": [{"text": "Annular Pancreas", "type": "AnatomicalStructure"}, {"text": "Ectopic", "type": "SpatialConcept"}, {"text": "Opening", "type": "SpatialConcept"}, {"text": "Pancreatic", "type": "AnatomicalStructure"}, {"text": "Bile Ducts", "type": "AnatomicalStructure"}, {"text": "Pyloric Ring", "type": "AnatomicalStructure"}, {"text": "Report", "type": "IntellectualProduct"}, {"text": "Anomaly", "type": "Finding"}, {"text": "epigastralgia", "type": "Finding"}, {"text": "dorsal pain", "type": "Finding"}]}

Example input:
Sentence: This study was undertaken to study the morphometry of human pancreas at different gestational age groups of normal , still born fetuses .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "morphometry", "type": "HealthCareActivity"}, {"text": "human", "type": "Eukaryote"}, {"text": "pancreas", "type": "AnatomicalStructure"}, {"text": "fetuses", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The length and weight of the pancreas as well as height of its head were noted .

Example answer:
{"entities": [{"text": "pancreas", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The average length of pancreas was 1 . 80 cm in 12 ( th ) week and 4 . 70 cm in 40 ( th ) week of gestation .

Example answer:
{"entities": [{"text": "pancreas", "type": "AnatomicalStructure"}, {"text": "week", "type": "Finding"}, {"text": "week of gestation", "type": "Finding"}]}

Input:
Sentence: The average height of pancreas head was 0 . 80 cm in the 12 ( th ) and 2 . 70 cm in 40 ( th ) week of gestation .

## Item MedMentions:test:2635
Example input:
Sentence: In this study , we determined the cumulative acute exposure to OPs and CPs of Shanghai residents from vegetables and fruits ( VFs ) .

Example answer:
{"entities": [{"text": "OPs", "type": "Chemical"}, {"text": "CPs", "type": "Chemical"}, {"text": "residents", "type": "PopulationGroup"}, {"text": "vegetables", "type": "Food"}, {"text": "fruits", "type": "Food"}, {"text": "VFs", "type": "Food"}]}

Example input:
Sentence: Referenced to Dietary Reference Intakes , survivors consumed inadequate amounts of vitamin D , vitamin E , potassium , fiber , magnesium , and calcium ( 27 % , 54 % , 58 % , 59 % , 84 % , and 90 % of the recommended intakes ) but excessive amounts of sodium and saturated fat ( 155 % and 115 % of the recommended intakes ) from foods .

Example answer:
{"entities": [{"text": "Dietary Reference Intakes", "type": "IntellectualProduct"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "potassium", "type": "Food"}, {"text": "fiber", "type": "Food"}, {"text": "magnesium", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "recommended intakes", "type": "IntellectualProduct"}, {"text": "sodium", "type": "Food"}, {"text": "saturated fat", "type": "Food"}]}

Example input:
Sentence: In conclusion , substitution of saturated fat with omega - 3 fat in a high - caloric diet induced hyperlipidaemia with an FA profile yielding similar rates and quality of blastocysts compared with normolipidaemic controls .

Example answer:
{"entities": [{"text": "saturated fat", "type": "Food"}, {"text": "omega - 3 fat", "type": "Chemical"}, {"text": "high - caloric diet", "type": "HealthCareActivity"}, {"text": "hyperlipidaemia", "type": "BiologicFunction"}, {"text": "FA profile", "type": "HealthCareActivity"}, {"text": "blastocysts", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Corn oil intake favorably impacts lipoprotein cholesterol , apolipoprotein and lipoprotein particle levels compared with extra - virgin olive oil Corn oil ( CO ) and extra - virgin olive oil ( EVOO ) are rich sources of unsaturated fatty acids ( UFA ) , but UFA profiles differ among oils , which may affect lipoprotein levels .

Example answer:
{"entities": [{"text": "Corn oil intake", "type": "Chemical"}, {"text": "lipoprotein cholesterol", "type": "Chemical"}, {"text": "apolipoprotein", "type": "HealthCareActivity"}, {"text": "lipoprotein", "type": "HealthCareActivity"}, {"text": "extra - virgin olive oil", "type": "Chemical"}, {"text": "Corn oil", "type": "Chemical"}, {"text": "CO", "type": "Chemical"}, {"text": "EVOO", "type": "Chemical"}, {"text": "sources of", "type": "Finding"}, {"text": "unsaturated fatty acids", "type": "Chemical"}, {"text": "UFA", "type": "Chemical"}, {"text": "oils", "type": "Chemical"}, {"text": "lipoprotein levels", "type": "HealthCareActivity"}]}

Example input:
Sentence: After 21 d of feeding , supplementation of oxidized fish oil increased the levels of malondialdehyde ( MDA ) , oxidized glutathione ( GSSG ) , interleukin - 1β ( IL - 1β ) , tumor necrosis factor - α ( TNF - α ) , interleukin - 2 ( IL - 2 ) , nuclear factor κ B ( NF - κB ) , inducible nitric oxide synthase ( iNOS ) , NO , and Caspase - 3 in jejunal mucosa , and decreased the villous height in duodenum and the levels of secretory immunoglobulin A ( sIgA ) and IL - 4 in the jejunal mucosa compared with supplementation with fresh oil .

Example answer:
{"entities": [{"text": "supplementation", "type": "HealthCareActivity"}, {"text": "oxidized", "type": "BiologicFunction"}, {"text": "fish oil", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "MDA", "type": "Chemical"}, {"text": "oxidized glutathione", "type": "Chemical"}, {"text": "GSSG", "type": "Chemical"}, {"text": "interleukin - 1β", "type": "Chemical"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "tumor necrosis factor - α", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "interleukin - 2", "type": "Chemical"}, {"text": "IL - 2", "type": "Chemical"}, {"text": "nuclear factor κ B", "type": "Chemical"}, {"text": "( NF - κB", "type": "Chemical"}, {"text": "inducible nitric oxide synthase", "type": "Chemical"}, {"text": "iNOS", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "Caspase - 3", "type": "Chemical"}, {"text": "jejunal mucosa", "type": "AnatomicalStructure"}, {"text": "villous", "type": "AnatomicalStructure"}, {"text": "duodenum", "type": "AnatomicalStructure"}, {"text": "secretory immunoglobulin A", "type": "Chemical"}, {"text": "( sIgA", "type": "Chemical"}, {"text": "IL - 4", "type": "Chemical"}, {"text": "oil", "type": "Chemical"}]}

Example input:
Sentence: Higher fish consumption ( at least 3 portions ) was associated with lower omega - 6 fatty acid levels ( p = 0 . 026 ) and higher omega - 3 fatty acid levels ( p = 0 . 037 ) , both results being statistically significant .

Example answer:
{"entities": [{"text": "fish consumption", "type": "BiologicFunction"}, {"text": "omega - 6 fatty acid", "type": "Chemical"}, {"text": "omega - 3 fatty acid", "type": "Chemical"}, {"text": "results", "type": "Finding"}]}

Example input:
Sentence: The ApoE polymorphism showed different influences on serum lipid parameters with increasing age and body mass index ( BMI ) in our Shandong Han population .

Example answer:
{"entities": [{"text": "ApoE", "type": "AnatomicalStructure"}, {"text": "serum lipid parameters", "type": "HealthCareActivity"}, {"text": "body mass index", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Serum apolipoprotein E concentration and polymorphism influence serum lipid levels in Chinese Shandong Han population Apolipoprotein E ( ApoE ) , which has been shown to influence serum lipid parameters , can bind to multiple types of lipids and plays an important role in the metabolism and homeostasis of lipids and lipoproteins .

Example answer:
{"entities": [{"text": "serum lipid levels", "type": "HealthCareActivity"}, {"text": "Apolipoprotein E", "type": "Chemical"}, {"text": "ApoE", "type": "Chemical"}, {"text": "serum lipid parameters", "type": "HealthCareActivity"}, {"text": "lipids", "type": "Chemical"}, {"text": "metabolism", "type": "BiologicFunction"}, {"text": "homeostasis", "type": "BiologicFunction"}, {"text": "lipoproteins", "type": "Chemical"}]}

Example input:
Sentence: Shandong province of China .

Example answer:
{"entities": [{"text": "Shandong province of China", "type": "SpatialConcept"}]}

Example input:
Sentence: Therefore , studying the effect of ApoE polymorphism on ApoE concentration and serum lipid levels in Shandong province is very important .A total of 815 subjects including 285 men and 530 women were randomly selected and studied from Jinan , Shandong province .

Example answer:
{"entities": [{"text": "ApoE", "type": "AnatomicalStructure"}, {"text": "ApoE", "type": "Chemical"}, {"text": "serum lipid levels", "type": "HealthCareActivity"}, {"text": "Shandong province", "type": "SpatialConcept"}, {"text": "men", "type": "PopulationGroup"}, {"text": "women", "type": "PopulationGroup"}]}

Input:
Sentence: The serum lipid levels were also closely correlated with dietary habits , and Shandong cuisine is famous for its high salt and oil contents , which widely differ among the different areas in China .

## Item MedMentions:test:2798
Example input:
Sentence: All cases showed markers positivity to Neuron - specific enolase , Chromogranin , Synaptophysin and Estrogen and Progesterone receptors were found .

Example answer:
{"entities": [{"text": "Neuron - specific enolase", "type": "Chemical"}, {"text": "Chromogranin", "type": "Chemical"}, {"text": "Synaptophysin", "type": "Chemical"}]}

Example input:
Sentence: There were decreased numbers of GFAP immunopositive astrocytes per unit area , although those that remained had increased arbor length and complexity .

Example answer:
{"entities": [{"text": "decreased numbers", "type": "Finding"}, {"text": "immunopositive astrocytes", "type": "AnatomicalStructure"}, {"text": "complexity", "type": "Finding"}]}

Example input:
Sentence: C - Reactive Protein ( CRP ) is a good inflammatory marker .

Example answer:
{"entities": [{"text": "C - Reactive Protein", "type": "Chemical"}, {"text": "CRP", "type": "Chemical"}, {"text": "marker", "type": "ClinicalAttribute"}]}

Example input:
Sentence: CGRP expression , as determined by IHC , cannot be observed in other groups , indicating that the hippocampus may be the specific component of the brain that responds to " big stress " .

Example answer:
{"entities": [{"text": "CGRP", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "IHC", "type": "HealthCareActivity"}, {"text": "hippocampus", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "big stress", "type": "BiologicFunction"}]}

Example input:
Sentence: ELISA analysis indicated a great density of CGRP in TBI - fracture group at different time points .

Example answer:
{"entities": [{"text": "ELISA analysis", "type": "HealthCareActivity"}, {"text": "CGRP", "type": "Chemical"}, {"text": "TBI", "type": "InjuryOrPoisoning"}, {"text": "fracture", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: 3 % of the patched Grpr - Cre neurons , where the majority of the cells displayed a tonic firing property .

Example answer:
{"entities": [{"text": "Grpr - Cre", "type": "AnatomicalStructure"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "tonic firing", "type": "BiologicFunction"}]}

Example input:
Sentence: Our results suggest that CGRP - expressing nerve growth factor -dependent neurons are primarily responsible for hip joint pain and may represent therapeutic targets .

Example answer:
{"entities": [{"text": "CGRP", "type": "Chemical"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "nerve growth factor", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "hip joint pain", "type": "Finding"}]}

Example input:
Sentence: FG -labeled neurons in the control group were distributed throughout the left DRG from T13 to L5 , primarily in L2 to L4 , and CGRP -positive neurons were significantly more frequent than IB4 - binding neurons .

Example answer:
{"entities": [{"text": "FG", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "left DRG", "type": "AnatomicalStructure"}, {"text": "T13", "type": "AnatomicalStructure"}, {"text": "L5", "type": "AnatomicalStructure"}, {"text": "L2", "type": "AnatomicalStructure"}, {"text": "L4", "type": "AnatomicalStructure"}, {"text": "CGRP", "type": "Chemical"}, {"text": "IB4", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , hip joint inflammation caused an increase in CGRP -positive neurons , but not in IB4 - binding neurons .

Example answer:
{"entities": [{"text": "hip joint", "type": "SpatialConcept"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "CGRP", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "IB4", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}]}

Example input:
Sentence: In the inflammatory group , FG -labeled neurons were similarly distributed , primarily at L3 and L4 , and CGRP -positive neurons were significantly more frequent than IB4 - binding neurons .

Example answer:
{"entities": [{"text": "FG", "type": "Chemical"}, {"text": "neurons", "type": "AnatomicalStructure"}, {"text": "L3", "type": "AnatomicalStructure"}, {"text": "L4", "type": "AnatomicalStructure"}, {"text": "CGRP", "type": "Chemical"}, {"text": "IB4", "type": "Chemical"}, {"text": "binding", "type": "BiologicFunction"}]}

Input:
Sentence: The percentage of CGRP -positive neurons was significantly greater in the inflammatory group ( P < 0 . 05 ) .

## Item MedMentions:test:2586
Example input:
Sentence: MSCs derived from bone marrow , adipose and umbilical cord that were infected with NDV delivered the virus to co - cultured glioma cells and GSCs .

Example answer:
{"entities": [{"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "bone marrow", "type": "AnatomicalStructure"}, {"text": "adipose", "type": "AnatomicalStructure"}, {"text": "umbilical cord", "type": "AnatomicalStructure"}, {"text": "infected", "type": "Finding"}, {"text": "NDV", "type": "Virus"}, {"text": "virus", "type": "Virus"}, {"text": "co - cultured", "type": "HealthCareActivity"}, {"text": "glioma", "type": "BiologicFunction"}, {"text": "cells", "type": "AnatomicalStructure"}, {"text": "GSCs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: MSC - EV increased hepatic mRNA expression of NACHT , LRR and PYD domains - containing protein 12 ( Nlrp12 ) , and the chemokine ( C - X - C motif ) ligand 1 ( CXCL1 ) , and reduced mRNA expression of several inflammatory cytokines such as IL - 6 during IRI .

Example answer:
{"entities": [{"text": "MSC", "type": "AnatomicalStructure"}, {"text": "EV", "type": "AnatomicalStructure"}, {"text": "hepatic", "type": "SpatialConcept"}, {"text": "mRNA expression", "type": "BiologicFunction"}, {"text": "NACHT , LRR and PYD domains - containing protein 12", "type": "AnatomicalStructure"}, {"text": "Nlrp12", "type": "AnatomicalStructure"}, {"text": "chemokine ( C - X - C motif ) ligand 1", "type": "AnatomicalStructure"}, {"text": "CXCL1", "type": "AnatomicalStructure"}, {"text": "cytokines", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "IRI", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: CCR2 Positive Exosome Released by Mesenchymal Stem Cells Suppresses Macrophage Functions and Alleviates Ischemia / Reperfusion - Induced Renal Injury Mesenchymal stem cells ( MSCs ) derived exosomes have been shown to have protective effects on the kidney in ischemia / reperfusion - induced renal injury .

Example answer:
{"entities": [{"text": "CCR2", "type": "Chemical"}, {"text": "Exosome", "type": "AnatomicalStructure"}, {"text": "Mesenchymal Stem Cells", "type": "AnatomicalStructure"}, {"text": "Macrophage", "type": "AnatomicalStructure"}, {"text": "Ischemia", "type": "BiologicFunction"}, {"text": "Reperfusion", "type": "BiologicFunction"}, {"text": "Induced Renal Injury", "type": "InjuryOrPoisoning"}, {"text": "Mesenchymal stem cells", "type": "AnatomicalStructure"}, {"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "exosomes", "type": "AnatomicalStructure"}, {"text": "kidney", "type": "AnatomicalStructure"}, {"text": "ischemia", "type": "BiologicFunction"}, {"text": "reperfusion", "type": "BiologicFunction"}, {"text": "induced renal injury", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: In particular , platelet lysate ( PL ) - MSCs produce higher levels of chemerin compared with fetal bovine serum ( FBS ) - MSCs .

Example answer:
{"entities": [{"text": "platelet lysate", "type": "AnatomicalStructure"}, {"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "chemerin", "type": "Chemical"}, {"text": "fetal bovine serum", "type": "Chemical"}, {"text": "FBS", "type": "Chemical"}]}

Example input:
Sentence: The results indicate that CCR2 expressed on MSC - exo may play a key role in inflammation regulation and renal injury repair by acting as a decoy to suppress CCL2 activity .

Example answer:
{"entities": [{"text": "indicate", "type": "Finding"}, {"text": "CCR2", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "MSC", "type": "AnatomicalStructure"}, {"text": "exo", "type": "AnatomicalStructure"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "regulation", "type": "BiologicFunction"}, {"text": "renal injury repair", "type": "BiologicFunction"}]}

Example input:
Sentence: After purification , MSC - secreted chemerin was identified using mass spectrometry analysis and the biological activity of secreted isoforms was evaluated using migration assay .

Example answer:
{"entities": [{"text": "MSC", "type": "AnatomicalStructure"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "chemerin", "type": "Chemical"}, {"text": "mass spectrometry", "type": "HealthCareActivity"}, {"text": "analysis", "type": "ResearchActivity"}, {"text": "isoforms", "type": "Chemical"}, {"text": "migration assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: We also proved that CCR2 high - expressed MSC - exo could reduce the concentration of free CCL2 and suppress its functions to recruit or activate macrophage .

Example answer:
{"entities": [{"text": "CCR2", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "MSC", "type": "AnatomicalStructure"}, {"text": "exo", "type": "AnatomicalStructure"}, {"text": "CCL2", "type": "Chemical"}, {"text": "activate macrophage", "type": "BiologicFunction"}]}

Example input:
Sentence: In our current study , we focused on the abundant proteins in exosomes derived from MSCs ( MSC - exo ) and found that the C - C motif chemokine receptor - 2 ( CCR2 ) was expressed on MSC - exo with a high ability to bind to its ligand CCL2 .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "proteins", "type": "Chemical"}, {"text": "exosomes", "type": "AnatomicalStructure"}, {"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "MSC", "type": "AnatomicalStructure"}, {"text": "exo", "type": "AnatomicalStructure"}, {"text": "C - C motif chemokine receptor - 2", "type": "Chemical"}, {"text": "CCR2", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "bind to its ligand CCL2", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , chemerin is secreted by MSCs as an inactive precursor , which can be converted into its active form by exogenous chemerin - activating serine and cysteine proteases .

Example answer:
{"entities": [{"text": "chemerin", "type": "Chemical"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "serine", "type": "Chemical"}, {"text": "cysteine proteases", "type": "Chemical"}]}

Example input:
Sentence: Our data indicate that , in response to various inflammatory stimuli , MSCs secrete high amounts of inactive chemerin , which can then be activated by inflammation - induced tissue proteases .

Example answer:
{"entities": [{"text": "MSCs", "type": "AnatomicalStructure"}, {"text": "secrete", "type": "BiologicFunction"}, {"text": "chemerin", "type": "Chemical"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "tissue", "type": "AnatomicalStructure"}, {"text": "proteases", "type": "Chemical"}]}

Input:
Sentence: Bone marrow - derived MSCs secrete chemerin and express its receptors ChemR23 and CCRL2 .

## Item MedMentions:test:2734
Example input:
Sentence: A patient with an abnormally high level of the tumor markers , carbohydrate antigen - 724 ( CA724 ) , CA19 - 9 and carcinoembryonic antigen ( CEA ) , although without any detectable tumor , was treated with an immunomodulatory therapy featuring an infusion of cytokine - induced autologous killer cells ( CIKs ) at the request of the patient .

Example answer:
{"entities": [{"text": "tumor markers", "type": "Chemical"}, {"text": "carbohydrate antigen - 724", "type": "Chemical"}, {"text": "CA724", "type": "Chemical"}, {"text": "CA19 - 9", "type": "Chemical"}, {"text": "carcinoembryonic antigen", "type": "Chemical"}, {"text": "CEA", "type": "Chemical"}, {"text": "detectable", "type": "ClinicalAttribute"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "treated with", "type": "HealthCareActivity"}, {"text": "immunomodulatory therapy", "type": "HealthCareActivity"}, {"text": "infusion", "type": "HealthCareActivity"}, {"text": "cytokine - induced autologous killer cells", "type": "AnatomicalStructure"}, {"text": "CIKs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Finally , we discuss the potential role of PSCs in pituitary tumorigenesis in the context of current models of carcinogenesis and present evidence showing that in contrast to pituitary adenoma , which follows a classical cancer stem cell paradigm , a novel mechanism has been revealed for paracrine , non - cell autonomous tumor initiation in adamantinomatous craniopharyngioma , a benign but clinically aggressive pediatric tumor .

Example answer:
{"entities": [{"text": "PSCs", "type": "AnatomicalStructure"}, {"text": "pituitary", "type": "AnatomicalStructure"}, {"text": "tumorigenesis", "type": "BiologicFunction"}, {"text": "carcinogenesis", "type": "BiologicFunction"}, {"text": "present", "type": "Finding"}, {"text": "pituitary adenoma", "type": "BiologicFunction"}, {"text": "cancer stem cell", "type": "AnatomicalStructure"}, {"text": "non - cell", "type": "AnatomicalStructure"}, {"text": "tumor", "type": "BiologicFunction"}, {"text": "adamantinomatous craniopharyngioma", "type": "BiologicFunction"}, {"text": "pediatric tumor", "type": "BiologicFunction"}]}

Example input:
Sentence: Carcinoid tumor , as the glomus tumor , can show an organoid pattern , increased vascularity , and uniform , round cells with eosinophilic cytoplasm , but usually are positive for cytokeratin and always stained with chromogranin and synaptophysin showing negative for smooth muscle markers which is presented in our case .

Example answer:
{"entities": [{"text": "Carcinoid tumor", "type": "BiologicFunction"}, {"text": "glomus tumor", "type": "BiologicFunction"}, {"text": "organoid pattern", "type": "Finding"}, {"text": "eosinophilic cytoplasm", "type": "AnatomicalStructure"}, {"text": "positive for cytokeratin", "type": "Finding"}, {"text": "chromogranin", "type": "Chemical"}, {"text": "synaptophysin", "type": "Chemical"}, {"text": "negative", "type": "Finding"}, {"text": "smooth muscle", "type": "AnatomicalStructure"}, {"text": "markers", "type": "Chemical"}]}

Example input:
Sentence: Coronal histological examination of the lateral wall of the CS showed invagination of the dura propria and periosteal dura into the SOF .

Example answer:
{"entities": [{"text": "Coronal histological examination", "type": "HealthCareActivity"}, {"text": "lateral wall", "type": "SpatialConcept"}, {"text": "CS", "type": "SpatialConcept"}, {"text": "invagination", "type": "AnatomicalStructure"}, {"text": "dura propria", "type": "AnatomicalStructure"}, {"text": "periosteal dura", "type": "AnatomicalStructure"}, {"text": "SOF", "type": "SpatialConcept"}]}

Example input:
Sentence: We describe the first reported case of a pituitary macroadenoma associated with RSTS .

Example answer:
{"entities": [{"text": "pituitary macroadenoma", "type": "BiologicFunction"}, {"text": "RSTS", "type": "BiologicFunction"}]}

Example input:
Sentence: Incomplete Annular Pancreas with Ectopic Opening of the Pancreatic and Bile Ducts into the Pyloric Ring : First Report of a Rare Anomaly The patient was a 56 - year - old woman who had experienced epigastralgia and dorsal pain several times over the last 20 years .

Example answer:
{"entities": [{"text": "Annular Pancreas", "type": "AnatomicalStructure"}, {"text": "Ectopic", "type": "SpatialConcept"}, {"text": "Opening", "type": "SpatialConcept"}, {"text": "Pancreatic", "type": "AnatomicalStructure"}, {"text": "Bile Ducts", "type": "AnatomicalStructure"}, {"text": "Pyloric Ring", "type": "AnatomicalStructure"}, {"text": "Report", "type": "IntellectualProduct"}, {"text": "Anomaly", "type": "Finding"}, {"text": "epigastralgia", "type": "Finding"}, {"text": "dorsal pain", "type": "Finding"}]}

Example input:
Sentence: EES is the ideal approach for complete resection of ectopic intracavernous adenomas allowing for a wide exploration of the CS with no surgical complications .

Example answer:
{"entities": [{"text": "EES", "type": "HealthCareActivity"}, {"text": "resection", "type": "HealthCareActivity"}, {"text": "ectopic", "type": "SpatialConcept"}, {"text": "adenomas", "type": "BiologicFunction"}, {"text": "exploration", "type": "HealthCareActivity"}, {"text": "CS", "type": "SpatialConcept"}, {"text": "no", "type": "Finding"}, {"text": "surgical", "type": "HealthCareActivity"}, {"text": "complications", "type": "BiologicFunction"}]}

Example input:
Sentence: Pathology confirmed the diagnosis of an ACTH - secreting adenoma .

Example answer:
{"entities": [{"text": "Pathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "diagnosis", "type": "Finding"}, {"text": "ACTH - secreting adenoma", "type": "BiologicFunction"}]}

Example input:
Sentence: Increased ACTH , serum cortisol and free urine cortisol levels were identified , however the pituitary MRI failed to reveal a pituitary tumor ; instead , a parasellar lesion in the left cavernous sinus ( CS ) was noticed .

Example answer:
{"entities": [{"text": "ACTH", "type": "Chemical"}, {"text": "serum cortisol", "type": "Chemical"}, {"text": "pituitary MRI", "type": "HealthCareActivity"}, {"text": "pituitary tumor", "type": "BiologicFunction"}, {"text": "parasellar lesion", "type": "Finding"}, {"text": "cavernous sinus", "type": "SpatialConcept"}, {"text": "CS", "type": "SpatialConcept"}]}

Example input:
Sentence: Only 12 cases of ectopic intracavernous ACTH - secreting adenomas have been reported to date and all were microadenomas .

Example answer:
{"entities": [{"text": "ectopic", "type": "SpatialConcept"}, {"text": "ACTH - secreting adenomas", "type": "BiologicFunction"}, {"text": "microadenomas", "type": "BiologicFunction"}]}

Input:
Sentence: The presence of an ectopic ACTH - secreting macroadenoma in the CS represents a surgical challenge .

## Item MedMentions:test:2770
Example input:
Sentence: Intravascular ultrasound ( n = 34 ) or optical coherence tomography ( n = 31 ) was performed in all cases .

Example answer:
{"entities": [{"text": "Intravascular ultrasound", "type": "HealthCareActivity"}, {"text": "optical coherence tomography", "type": "HealthCareActivity"}]}

Example input:
Sentence: The present method of optimized HR - FSE imaging with a 3 T system improved visualization of intimal flaps and should thus be considered for assessing patients with suspected ICAD that cannot be definitively diagnosed by conventional imaging modalities .

Example answer:
{"entities": [{"text": "HR - FSE imaging", "type": "HealthCareActivity"}, {"text": "improved", "type": "Finding"}, {"text": "visualization", "type": "HealthCareActivity"}, {"text": "intimal flaps", "type": "AnatomicalStructure"}, {"text": "ICAD", "type": "AnatomicalStructure"}, {"text": "diagnosed", "type": "Finding"}]}

Example input:
Sentence: A combined optical coherence tomography and intravascular ultrasound study Some plaques grow slowly in a linear manner , whereas others undergo a rapid phasic progression .

Example answer:
{"entities": [{"text": "optical coherence tomography", "type": "HealthCareActivity"}, {"text": "intravascular ultrasound", "type": "HealthCareActivity"}, {"text": "study", "type": "ResearchActivity"}, {"text": "plaques", "type": "Finding"}, {"text": "grow slowly", "type": "Finding"}]}

Example input:
Sentence: The aim of the current study was to compare the performance of MRI and ultrasound in detecting carotid artery plaques and measuring extent of atherosclerosis .

Example answer:
{"entities": [{"text": "study", "type": "ResearchActivity"}, {"text": "MRI", "type": "HealthCareActivity"}, {"text": "ultrasound", "type": "HealthCareActivity"}, {"text": "detecting", "type": "Finding"}, {"text": "carotid artery plaques", "type": "AnatomicalStructure"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "atherosclerosis", "type": "BiologicFunction"}]}

Example input:
Sentence: On the one hand , this technique allows a better and direct visualization of vascular and solid organ lesions .

Example answer:
{"entities": [{"text": "vascular", "type": "BiologicFunction"}, {"text": "solid organ", "type": "AnatomicalStructure"}, {"text": "lesions", "type": "Finding"}]}

Example input:
Sentence: For rapid imaging of the cerebrovasculature , digital subtraction angiography ( DSA ) remains the gold standard as it offers high spatial resolution .

Example answer:
{"entities": [{"text": "imaging", "type": "HealthCareActivity"}, {"text": "cerebrovasculature", "type": "BodySystem"}, {"text": "digital subtraction angiography", "type": "HealthCareActivity"}, {"text": "DSA", "type": "HealthCareActivity"}]}

Example input:
Sentence: Before the introduction of this technique , vascular puncture was acquired based on an integration of angiographic data , the bony iliofemoral landmarks and a radiopaque object .

Example answer:
{"entities": [{"text": "vascular", "type": "AnatomicalStructure"}, {"text": "puncture", "type": "HealthCareActivity"}, {"text": "angiographic", "type": "HealthCareActivity"}, {"text": "iliofemoral", "type": "AnatomicalStructure"}, {"text": "landmarks", "type": "SpatialConcept"}]}

Example input:
Sentence: The results provide further evidence that retinal vascular features are clinically informative about underlying stroke risk factors and demonstrate the utility of handheld retinal photography in the stroke ward .

Example answer:
{"entities": [{"text": "retinal", "type": "AnatomicalStructure"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "retinal photography", "type": "HealthCareActivity"}, {"text": "ward", "type": "Organization"}]}

Example input:
Sentence: Vessels abnormalities were assessed with brain computed tomography ( CT ) angiography , magnetic resonance angiography ( MRA ) and / or digital subtraction angiography ( DSA ) .

Example answer:
{"entities": [{"text": "Vessels abnormalities", "type": "Finding"}, {"text": "brain", "type": "AnatomicalStructure"}, {"text": "computed tomography", "type": "HealthCareActivity"}, {"text": "CT", "type": "HealthCareActivity"}, {"text": "angiography", "type": "HealthCareActivity"}, {"text": "magnetic resonance angiography", "type": "HealthCareActivity"}, {"text": "MRA", "type": "HealthCareActivity"}, {"text": "digital subtraction angiography", "type": "HealthCareActivity"}, {"text": "DSA", "type": "HealthCareActivity"}]}

Example input:
Sentence: The quality of the imaging procedure was compared according to four items : global vascular opacification , cerebral venous opacification , and lower limbs opacification ( arterial and venous ) .

Example answer:
{"entities": [{"text": "imaging procedure", "type": "HealthCareActivity"}, {"text": "global vascular", "type": "AnatomicalStructure"}, {"text": "lower limbs", "type": "AnatomicalStructure"}, {"text": "arterial", "type": "SpatialConcept"}, {"text": "venous", "type": "SpatialConcept"}]}

Input:
Sentence: Modern imaging equipment can facilitate precise measurement and monitoring of vascular features .

## Item MedMentions:test:2638
Example input:
Sentence: AKT / GSK3β Signaling in Glioblastoma Glioblastoma ( GBM ) is the most aggressive of primary brain tumors .

Example answer:
{"entities": [{"text": "AKT", "type": "Chemical"}, {"text": "GSK3β", "type": "Chemical"}, {"text": "Signaling", "type": "BiologicFunction"}, {"text": "Glioblastoma", "type": "BiologicFunction"}, {"text": "GBM", "type": "BiologicFunction"}, {"text": "brain tumors", "type": "BiologicFunction"}]}

Example input:
Sentence: PI3 K and its downstream Akt are widely expressed in the spinal cord , particularly in the laminae I - IV of the dorsal horn , where nociceptive C and Aδ fibers of primary afferents principally terminate .

Example answer:
{"entities": [{"text": "PI3 K", "type": "Chemical"}, {"text": "downstream", "type": "SpatialConcept"}, {"text": "Akt", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "spinal cord", "type": "AnatomicalStructure"}, {"text": "laminae I - IV", "type": "AnatomicalStructure"}, {"text": "dorsal horn", "type": "AnatomicalStructure"}, {"text": "nociceptive C", "type": "AnatomicalStructure"}, {"text": "Aδ fibers", "type": "AnatomicalStructure"}, {"text": "afferents", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Much less attention has been paid to the role of glycogen synthase kinase 3 β ( GSK3β ) , a target of AKT .

Example answer:
{"entities": [{"text": "glycogen synthase kinase 3 β", "type": "Chemical"}, {"text": "GSK3β", "type": "Chemical"}, {"text": "AKT", "type": "Chemical"}]}

Example input:
Sentence: Exposure of CreaT and GSK3ß expressing oocytes for 24 hours to Lithium was followed by a significant increase of the creatine induced current .

Example answer:
{"entities": [{"text": "CreaT", "type": "Chemical"}, {"text": "GSK3ß", "type": "Chemical"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "oocytes", "type": "AnatomicalStructure"}, {"text": "Lithium", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "current", "type": "BiologicFunction"}]}

Example input:
Sentence: Down - Regulation of the Na + , Cl - Coupled Creatine Transporter CreaT ( SLC6A8 ) by Glycogen Synthase Kinase GSK3ß The Na + , Cl - coupled creatine transporter CreaT ( SLC6A8 ) is expressed in a variety of tissues including the brain .

Example answer:
{"entities": [{"text": "Down - Regulation", "type": "BiologicFunction"}, {"text": "Na + , Cl -", "type": "Chemical"}, {"text": "Creatine Transporter", "type": "Chemical"}, {"text": "CreaT", "type": "Chemical"}, {"text": "SLC6A8", "type": "Chemical"}, {"text": "Glycogen Synthase Kinase", "type": "Chemical"}, {"text": "GSK3ß", "type": "Chemical"}, {"text": "creatine transporter", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "tissues", "type": "AnatomicalStructure"}, {"text": "brain", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Kinetic analysis revealed that GSK3ß significantly decreased the maximal creatine transport rate .

Example answer:
{"entities": [{"text": "analysis", "type": "ResearchActivity"}, {"text": "GSK3ß", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "transport", "type": "BiologicFunction"}]}

Example input:
Sentence: GSK3ß is phosphorylated and thus inhibited by PKB / Akt .

Example answer:
{"entities": [{"text": "GSK3ß", "type": "Chemical"}, {"text": "phosphorylated", "type": "BiologicFunction"}, {"text": "PKB / Akt", "type": "Chemical"}]}

Example input:
Sentence: In CreaT expressing oocytes , co - expression of GSK3ß but not of K85RGSK3ß , resulted in a significant decrease of creatine induced current .

Example answer:
{"entities": [{"text": "CreaT", "type": "Chemical"}, {"text": "expressing", "type": "BiologicFunction"}, {"text": "oocytes", "type": "AnatomicalStructure"}, {"text": "co - expression", "type": "BiologicFunction"}, {"text": "GSK3ß", "type": "Chemical"}, {"text": "K85RGSK3ß", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "current", "type": "BiologicFunction"}]}

Example input:
Sentence: GSK3ß down - regulates the creatine transporter CreaT , an effect reversed by treatment with the antidepressant Lithium and by co - expression of PKB / Akt .

Example answer:
{"entities": [{"text": "GSK3ß", "type": "Chemical"}, {"text": "down - regulates", "type": "BiologicFunction"}, {"text": "creatine transporter", "type": "Chemical"}, {"text": "CreaT", "type": "Chemical"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "Lithium", "type": "Chemical"}, {"text": "co - expression", "type": "BiologicFunction"}, {"text": "PKB / Akt", "type": "Chemical"}]}

Example input:
Sentence: CreaT was expressed in Xenopus laevis oocytes with or without wild - type GSK3ß or inactive K85RGSK3ß .

Example answer:
{"entities": [{"text": "CreaT", "type": "Chemical"}, {"text": "expressed", "type": "BiologicFunction"}, {"text": "Xenopus laevis", "type": "Eukaryote"}, {"text": "oocytes", "type": "AnatomicalStructure"}, {"text": "wild - type", "type": "AnatomicalStructure"}, {"text": "GSK3ß", "type": "Chemical"}, {"text": "inactive K85RGSK3ß", "type": "Chemical"}]}

Input:
Sentence: CreaT and GSK3ß were further expressed without and with additional expression of wild type PKB / Akt .

## Item MedMentions:test:2469
Example input:
Sentence: The micelle system of CS - P68 and CS - P127 formed at drug to polymer ratios of 1 : 4 and 1 : 2 , respectively , was found to be the most suitable monodispersed system with a nanosize - range diameter .

Example answer:
{"entities": [{"text": "micelle system", "type": "Chemical"}, {"text": "CS - P68", "type": "Chemical"}, {"text": "CS - P127", "type": "Chemical"}, {"text": "drug", "type": "Chemical"}, {"text": "polymer", "type": "Chemical"}]}

Example input:
Sentence: After the GO - Fe3O4 / SiO2 / AuNWs / L - Cys composites were applied to glycopeptide enrichment , 26 glycopeptides from a human IgG digest could be identified , with a detection limit as low as 10 fmol .

Example answer:
{"entities": [{"text": "GO", "type": "Chemical"}, {"text": "Fe3O4", "type": "Chemical"}, {"text": "SiO2", "type": "Chemical"}, {"text": "L - Cys", "type": "Chemical"}, {"text": "glycopeptide", "type": "Chemical"}, {"text": "glycopeptides", "type": "Chemical"}, {"text": "human IgG", "type": "Chemical"}]}

Example input:
Sentence: Liquid trimyristin nanoparticles loaded with fenofibrate , orlistat , tocopherol acetate and ubidecarenone were studied in three different release media with increasing complexity and comparability to physiological conditions : a rapeseed oil nanoemulsion , porcine serum and porcine blood .

Example answer:
{"entities": [{"text": "trimyristin", "type": "Chemical"}, {"text": "fenofibrate", "type": "Chemical"}, {"text": "orlistat", "type": "Chemical"}, {"text": "tocopherol acetate", "type": "Chemical"}, {"text": "ubidecarenone", "type": "Chemical"}, {"text": "media", "type": "Chemical"}, {"text": "porcine", "type": "Eukaryote"}, {"text": "serum", "type": "BodySubstance"}, {"text": "blood", "type": "BodySubstance"}]}

Example input:
Sentence: In RCE and in pig cornea , the micelles improved the penetration of both rhodamine andr cyclosporine .

Example answer:
{"entities": [{"text": "RCE", "type": "AnatomicalStructure"}, {"text": "pig", "type": "Eukaryote"}, {"text": "cornea", "type": "AnatomicalStructure"}, {"text": "micelles", "type": "Chemical"}, {"text": "improved", "type": "Finding"}, {"text": "rhodamine", "type": "Chemical"}, {"text": "cyclosporine", "type": "Chemical"}]}

Example input:
Sentence: A model chitosan - tripolyphosphate ( TPP ) hydrogel nanoparticles ( CS - HNP ) , with a broad spectrum of possible applications was produced and sterilized in the absence and in the presence of protective sugars ( glucose and mannitol ) .

Example answer:
{"entities": [{"text": "chitosan", "type": "Chemical"}, {"text": "tripolyphosphate", "type": "Chemical"}, {"text": "TPP", "type": "Chemical"}, {"text": "CS", "type": "Chemical"}, {"text": "possible", "type": "Finding"}, {"text": "sterilized", "type": "HealthCareActivity"}, {"text": "protective sugars", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "mannitol", "type": "Chemical"}]}

Example input:
Sentence: PEG - DSPE coating may be related to better absorption , based on the stability and a pharmacokinetic improvement in the blood circulation time .

Example answer:
{"entities": [{"text": "PEG - DSPE", "type": "Chemical"}, {"text": "blood circulation time", "type": "HealthCareActivity"}]}

Example input:
Sentence: CS - PEG -blended PLGA nano - delivery system of quercetin , ellagic acid and gallic acid can potentiate apoptosis - mediated cell death in HepG2 cell line .

Example answer:
{"entities": [{"text": "CS", "type": "Chemical"}, {"text": "PEG", "type": "Chemical"}, {"text": "PLGA", "type": "Chemical"}, {"text": "quercetin", "type": "Chemical"}, {"text": "ellagic acid", "type": "Chemical"}, {"text": "gallic acid", "type": "Chemical"}, {"text": "apoptosis - mediated", "type": "BiologicFunction"}, {"text": "cell death", "type": "BiologicFunction"}, {"text": "HepG2 cell line", "type": "AnatomicalStructure"}]}

Example input:
Sentence: The immobilization approach includes the loading of DSPE - PEG ( 2000 ) - biotin containing sterically stabilized micelles ( SSMs ) which are restructured in a buffer change step , resulting in an accessible substrate for liposome immobilization .

Example answer:
{"entities": [{"text": "immobilization", "type": "HealthCareActivity"}, {"text": "DSPE - PEG ( 2000 )", "type": "Chemical"}, {"text": "biotin", "type": "Chemical"}, {"text": "micelles", "type": "Chemical"}, {"text": "SSMs", "type": "Chemical"}, {"text": "liposome", "type": "Chemical"}]}

Example input:
Sentence: On application of physiologically acceptable external magnetic field , FITC conjugated artemisinin magnetic nanoparticles showed an enhanced accumulation of nanoparticles in the 4T1 breast tumour tissues of BALB / c mice model .

Example answer:
{"entities": [{"text": "external", "type": "SpatialConcept"}, {"text": "FITC", "type": "Chemical"}, {"text": "artemisinin", "type": "Chemical"}, {"text": "4T1 breast tumour tissues", "type": "AnatomicalStructure"}, {"text": "BALB / c mice", "type": "Eukaryote"}, {"text": "model", "type": "BiologicFunction"}]}

Example input:
Sentence: CS - PEG decorated PLGA nano - prototype for delivery of bioactive compounds : A novel approach for induction of apoptosis in HepG2 cell line Polymer - based nanoparticles are used as vectors for cancer drug delivery .

Example answer:
{"entities": [{"text": "CS", "type": "Chemical"}, {"text": "PEG", "type": "Chemical"}, {"text": "PLGA nano - prototype", "type": "Chemical"}, {"text": "bioactive compounds", "type": "Chemical"}, {"text": "approach", "type": "SpatialConcept"}, {"text": "apoptosis", "type": "BiologicFunction"}, {"text": "HepG2 cell line", "type": "AnatomicalStructure"}, {"text": "Polymer", "type": "Chemical"}, {"text": "vectors", "type": "SpatialConcept"}, {"text": "cancer", "type": "BiologicFunction"}]}

Input:
Sentence: Reaction of Lymphoid Organs to Injection of Iron - Carbon Nanoparticles The distribution of iron - carbon nanoparticles in FeC - DSPE - PEG - 2000 modification ( micellar particles with structure ( Fe ) core - carbon shell ; PEG -based coating ) is studied .

## Item MedMentions:test:1992
Example input:
Sentence: RRMS patients had higher levels of NFL , CXCL13 , CHI3L1 , and CHIT1 than controls ( p < 0 .

Example answer:
{"entities": [{"text": "RRMS", "type": "BiologicFunction"}, {"text": "NFL", "type": "Chemical"}, {"text": "CXCL13", "type": "Chemical"}, {"text": "CHI3L1", "type": "Chemical"}, {"text": "CHIT1", "type": "Chemical"}]}

Example input:
Sentence: Cell wall polymers in culms were quantified by means of the monoclonal antibodies LM6 , LM11 , JIM13 and BS - 400 - 3 and the carbohydrate - binding module CBM3a using the high - throughput CoMPP technique .

Example answer:
{"entities": [{"text": "Cell wall", "type": "AnatomicalStructure"}, {"text": "culms", "type": "Eukaryote"}, {"text": "monoclonal antibodies", "type": "Chemical"}, {"text": "LM6", "type": "Chemical"}, {"text": "LM11", "type": "Chemical"}, {"text": "JIM13", "type": "Chemical"}, {"text": "BS - 400 - 3", "type": "Chemical"}, {"text": "carbohydrate - binding module CBM3a", "type": "Chemical"}, {"text": "CoMPP technique", "type": "HealthCareActivity"}]}

Example input:
Sentence: In contrast , SHED - CM specifically depleted of a set of anti - inflammatory M2 macrophage inducers , monocyte chemoattractant protein - 1 ( MCP - 1 ) and the secreted ectodomain of sialic acid - binding Ig - like lectin - 9 ( sSiglec - 9 ) lost the ability to restore neurological function in this model .

Example answer:
{"entities": [{"text": "SHED - CM", "type": "AnatomicalStructure"}, {"text": "M2 macrophage", "type": "AnatomicalStructure"}, {"text": "monocyte chemoattractant protein - 1", "type": "Chemical"}, {"text": "MCP - 1", "type": "Chemical"}, {"text": "secreted", "type": "BiologicFunction"}, {"text": "ectodomain", "type": "SpatialConcept"}, {"text": "sialic acid - binding Ig - like lectin - 9", "type": "Chemical"}, {"text": "sSiglec - 9", "type": "Chemical"}, {"text": "restore", "type": "HealthCareActivity"}, {"text": "neurological function", "type": "BiologicFunction"}]}

Example input:
Sentence: After the GO - Fe3O4 / SiO2 / AuNWs / L - Cys composites were applied to glycopeptide enrichment , 26 glycopeptides from a human IgG digest could be identified , with a detection limit as low as 10 fmol .

Example answer:
{"entities": [{"text": "GO", "type": "Chemical"}, {"text": "Fe3O4", "type": "Chemical"}, {"text": "SiO2", "type": "Chemical"}, {"text": "L - Cys", "type": "Chemical"}, {"text": "glycopeptide", "type": "Chemical"}, {"text": "glycopeptides", "type": "Chemical"}, {"text": "human IgG", "type": "Chemical"}]}

Example input:
Sentence: Serum biomarkers of cartilage function and inflammation [ collagen type II C - telopeptide ( CTXII ) , cartilage oligomeric matrix protein ( COMP ) , and alpha - 2 - macroglobulin ( A2 M ) ] were measured by ELISA .

Example answer:
{"entities": [{"text": "Serum", "type": "BodySubstance"}, {"text": "biomarkers", "type": "ClinicalAttribute"}, {"text": "cartilage function", "type": "BiologicFunction"}, {"text": "inflammation", "type": "BiologicFunction"}, {"text": "collagen type II C - telopeptide", "type": "HealthCareActivity"}, {"text": "CTXII", "type": "HealthCareActivity"}, {"text": "cartilage oligomeric matrix protein", "type": "HealthCareActivity"}, {"text": "COMP", "type": "HealthCareActivity"}, {"text": "alpha - 2 - macroglobulin", "type": "HealthCareActivity"}, {"text": "A2 M", "type": "HealthCareActivity"}, {"text": "ELISA", "type": "HealthCareActivity"}]}

Example input:
Sentence: In the CSX group , a significant correlation was found between TCC and FCN3 - TCC level ( r = 0 . 507 , P = 0 . 032 ) and between ficolin - 3 / MASP - 2 complex level and FCN3 - TCC deposition ( r = 0 . 651 , P = 0 . 003 ) .

Example answer:
{"entities": [{"text": "CSX", "type": "BiologicFunction"}, {"text": "TCC", "type": "Chemical"}, {"text": "FCN3", "type": "Chemical"}, {"text": "ficolin - 3", "type": "Chemical"}, {"text": "MASP - 2", "type": "Chemical"}, {"text": "complex", "type": "Chemical"}]}

Example input:
Sentence: Serum levels of ficolin - 2 and ficolin - 3 , ficolin - 3 / MASP - 2 complex and ficolin - 3 -mediated TCC deposition ( FCN3 - TCC ) were determined .

Example answer:
{"entities": [{"text": "Serum", "type": "BodySubstance"}, {"text": "ficolin - 2", "type": "Chemical"}, {"text": "ficolin - 3", "type": "Chemical"}, {"text": "MASP - 2", "type": "Chemical"}, {"text": "complex", "type": "Chemical"}, {"text": "TCC", "type": "Chemical"}, {"text": "FCN3", "type": "Chemical"}]}

Example input:
Sentence: Levels of interleukin - 6 ( IL - 6 ) , interferon - γ inducible protein - 10 ( CXCL10 ) , and monocyte chemoattractant protein - 1 ( CCL2 ) were determined by enzyme - linked immunosorbant assay ( ELISA ) .

Example answer:
{"entities": [{"text": "interleukin - 6", "type": "Chemical"}, {"text": "IL - 6", "type": "Chemical"}, {"text": "interferon - γ inducible protein - 10", "type": "Chemical"}, {"text": "CXCL10", "type": "Chemical"}, {"text": "monocyte chemoattractant protein - 1", "type": "Chemical"}, {"text": "CCL2", "type": "Chemical"}, {"text": "enzyme - linked immunosorbant assay", "type": "HealthCareActivity"}, {"text": "ELISA", "type": "HealthCareActivity"}]}

Example input:
Sentence: NFL and CHIT1 levels correlated with relapse status , and NFL and CXCL13 levels correlated with the formation of new magnetic resonance imaging lesions .

Example answer:
{"entities": [{"text": "NFL", "type": "Chemical"}, {"text": "CHIT1", "type": "Chemical"}, {"text": "relapse status", "type": "BiologicFunction"}, {"text": "CXCL13", "type": "Chemical"}, {"text": "magnetic resonance imaging", "type": "HealthCareActivity"}, {"text": "lesions", "type": "Finding"}]}

Example input:
Sentence: The results indicate that CSF levels of NFL , CXCL13 , CHI3L1 , and CHIT1 correlate with the clinical and / or radiological disease activity , providing additional dimensions in the assessment of treatment efficacy .

Example answer:
{"entities": [{"text": "CSF", "type": "BodySubstance"}, {"text": "NFL", "type": "Chemical"}, {"text": "CXCL13", "type": "Chemical"}, {"text": "CHI3L1", "type": "Chemical"}, {"text": "CHIT1", "type": "Chemical"}, {"text": "assessment", "type": "HealthCareActivity"}]}

Input:
Sentence: The concentrations of C - X - C motif chemokine 13 ( CXCL13 ) , C - C motif chemokine ligand 2 ( CCL2 ) , chitinase - 3 - like protein 1 ( CHI3L1 ) , glial fibrillary acidic protein , neurofilament light protein ( NFL ) , and neurogranin were determined by ELISA , and chitotriosidase ( CHIT1 ) was analyzed by spectrofluorometry .

## Item MedMentions:test:2902
Example input:
Sentence: Meta - analysis for poor prognostic factors as determined by hazard ratio ( HR ) and 95 % confidential interval ( 95 % CI ) .

Example answer:
{"entities": [{"text": "Meta - analysis", "type": "ResearchActivity"}, {"text": "prognostic factors", "type": "ClinicalAttribute"}]}

Example input:
Sentence: We performed a meta - analysis using weighted mean differences ( WMD ) and 95 % confidence intervals in a random - effects model .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: The present meta - analysis aims to determine whether the resuscitative phase really takes advantages by being performed with EGDT .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}, {"text": "resuscitative", "type": "HealthCareActivity"}, {"text": "EGDT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Meta - analytic methods will be employed wherever appropriate .

Example answer:
{"entities": [{"text": "Meta - analytic methods", "type": "ResearchActivity"}]}

Example input:
Sentence: Meta - analyses of 21 interventions fully or partially recommended their use , with recommendations being positively correlated with the effect sizes of the pooled intervention .

Example answer:
{"entities": [{"text": "Meta - analyses", "type": "ResearchActivity"}, {"text": "positively", "type": "Finding"}]}

Example input:
Sentence: Our results are consistent with the meta - analysis .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: A random effects meta - analysis was then used to estimate pooled effects .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: Meta - analysis was performed using HR and 95 % CI as the primary outcomes of interest .

Example answer:
{"entities": [{"text": "Meta - analysis", "type": "ResearchActivity"}]}

Example input:
Sentence: The outcomes subject to meta - analysis were pulmonary function , hospitalization , and further treatment .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "IntellectualProduct"}, {"text": "pulmonary function", "type": "BiologicFunction"}, {"text": "hospitalization", "type": "HealthCareActivity"}, {"text": "further treatment", "type": "Finding"}]}

Example input:
Sentence: Due to the variations in setting , design and outcome it was not feasible to pool results using a meta - analysis .

Example answer:
{"entities": [{"text": "meta - analysis", "type": "ResearchActivity"}]}

Input:
Sentence: Meta - analysis was used to pool results for these outcomes .

## Item MedMentions:test:2627
Example input:
Sentence: Gut microbiota after Roux - en - Y gastric bypass and sleeve gastrectomy in a diabetic rat model : Increased diversity and associations of discriminant genera with metabolic changes Recent work with gut microbiota after bariatric surgery is limited , and the results have not been in agreement .

Example answer:
{"entities": [{"text": "Roux - en - Y gastric bypass", "type": "HealthCareActivity"}, {"text": "sleeve gastrectomy", "type": "HealthCareActivity"}, {"text": "diabetic", "type": "BiologicFunction"}, {"text": "rat", "type": "Eukaryote"}, {"text": "model", "type": "BiologicFunction"}, {"text": "genera", "type": "IntellectualProduct"}, {"text": "metabolic", "type": "BiologicFunction"}, {"text": "bariatric surgery", "type": "HealthCareActivity"}]}

Example input:
Sentence: However , in our study , surgery did not achieve the expected outcome in patients with specific metabolic , anthropometric and surgical characteristics ( BMI > 50 Kg / m2 , presence of metabolic syndrome , presence of T2DM with high preoperative HbA1c % level and gastric pouch volume greater than 60 ml ) .

Example answer:
{"entities": [{"text": "surgery", "type": "HealthCareActivity"}, {"text": "expected", "type": "IntellectualProduct"}, {"text": "surgical", "type": "HealthCareActivity"}, {"text": "BMI", "type": "ClinicalAttribute"}, {"text": "metabolic syndrome", "type": "BiologicFunction"}, {"text": "T2DM", "type": "BiologicFunction"}, {"text": "HbA1c", "type": "Chemical"}, {"text": "gastric pouch", "type": "AnatomicalStructure"}]}

Example input:
Sentence: HMGB1 inhibition by ethyl pyruvate or blockade by neutralizing antibodies significantly decreased the phosphorylation of STAT3 , p38 and IκBα , the production of IL - 1β and TNF - α , and the islet injury in wild - type islets after exposure to H / R and significantly improved early islet graft failure .

Example answer:
{"entities": [{"text": "HMGB1", "type": "Chemical"}, {"text": "ethyl pyruvate", "type": "Chemical"}, {"text": "antibodies", "type": "Chemical"}, {"text": "phosphorylation", "type": "BiologicFunction"}, {"text": "STAT3", "type": "Chemical"}, {"text": "p38", "type": "Chemical"}, {"text": "IκBα", "type": "Chemical"}, {"text": "production", "type": "BiologicFunction"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "islet", "type": "AnatomicalStructure"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "islets", "type": "AnatomicalStructure"}, {"text": "H", "type": "BiologicFunction"}, {"text": "R", "type": "HealthCareActivity"}, {"text": "graft failure", "type": "BiologicFunction"}]}

Example input:
Sentence: Thus , our results suggest that HMGB1 released from H / R induced islets works in an autocrine manner to up - regulate STAT or p38 and augment IL - 1β production via TLR2 , and up - regulate NF - κB and augment TNF - α production via TLR4 in intra - islet , which are associated with H / R -induced islet injury and early graft failure .

Example answer:
{"entities": [{"text": "HMGB1", "type": "Chemical"}, {"text": "H", "type": "BiologicFunction"}, {"text": "R", "type": "HealthCareActivity"}, {"text": "islets", "type": "AnatomicalStructure"}, {"text": "up - regulate", "type": "BiologicFunction"}, {"text": "STAT", "type": "Chemical"}, {"text": "p38", "type": "Chemical"}, {"text": "IL - 1β", "type": "Chemical"}, {"text": "production", "type": "BiologicFunction"}, {"text": "TLR2", "type": "Chemical"}, {"text": "NF - κB", "type": "Chemical"}, {"text": "TNF - α", "type": "Chemical"}, {"text": "TLR4", "type": "Chemical"}, {"text": "intra - islet", "type": "AnatomicalStructure"}, {"text": "islet", "type": "AnatomicalStructure"}, {"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "graft failure", "type": "BiologicFunction"}]}

Example input:
Sentence: However , patients in the POST implementation group were more likely to exhibit hypoglycaemia .

Example answer:
{"entities": [{"text": "hypoglycaemia", "type": "BiologicFunction"}]}

Example input:
Sentence: Targeting postprandial blood sugar over fasting blood sugar : A clinic based comparative study Recent studies indicate that modulation of post prandial blood sugar ( PPBS ) plays an important role in the long term glycemic control .

Example answer:
{"entities": [{"text": "postprandial blood sugar", "type": "HealthCareActivity"}, {"text": "fasting blood sugar", "type": "HealthCareActivity"}, {"text": "clinic based comparative study", "type": "ResearchActivity"}, {"text": "post prandial blood sugar", "type": "BiologicFunction"}, {"text": "PPBS", "type": "BiologicFunction"}, {"text": "glycemic control", "type": "HealthCareActivity"}]}

Example input:
Sentence: We conducted a double - blinded crossover study wherein eight participants with confirmed PBH were assigned in random order to intravenous infusion of the GLP - 1 receptor ( GLP - 1r ) antagonist .

Example answer:
{"entities": [{"text": "double - blinded", "type": "ResearchActivity"}, {"text": "crossover study", "type": "ResearchActivity"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "PBH", "type": "BiologicFunction"}, {"text": "intravenous infusion", "type": "HealthCareActivity"}, {"text": "GLP - 1 receptor", "type": "Chemical"}, {"text": "GLP - 1r", "type": "Chemical"}, {"text": "antagonist", "type": "Chemical"}]}

Example input:
Sentence: The level of postoperative HbA1c % was related to BMI loss after surgery .

Example answer:
{"entities": [{"text": "HbA1c", "type": "Chemical"}, {"text": "BMI", "type": "IntellectualProduct"}]}

Example input:
Sentence: Infusion of Ex - 9 decreased the time to peak glucose and rate of glucose decline during OGTT , and raised the postprandial nadir by over 70 % , normalising it relative to NSCs and preventing hypoglycaemia in all PBH participants .

Example answer:
{"entities": [{"text": "Infusion", "type": "HealthCareActivity"}, {"text": "Ex - 9", "type": "Chemical"}, {"text": "glucose", "type": "Chemical"}, {"text": "OGTT", "type": "HealthCareActivity"}, {"text": "hypoglycaemia", "type": "BiologicFunction"}, {"text": "PBH", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}]}

Example input:
Sentence: GLP - 1r blockade prevented hypoglycaemia in 100 % of individuals , normalised beta cell function and reversed neuroglycopenic symptoms , supporting the conclusion that GLP - 1 plays a primary role in mediating hyperinsulinaemic hypoglycaemia in PBH .

Example answer:
{"entities": [{"text": "GLP - 1r", "type": "Chemical"}, {"text": "hypoglycaemia", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "beta cell function", "type": "BiologicFunction"}, {"text": "reversed neuroglycopenic symptoms", "type": "Finding"}, {"text": "GLP - 1", "type": "Chemical"}, {"text": "hyperinsulinaemic hypoglycaemia", "type": "BiologicFunction"}, {"text": "PBH", "type": "BiologicFunction"}]}

Input:
Sentence: Critical role for GLP - 1 in symptomatic post - bariatric hypoglycaemia Post - bariatric hypoglycaemia ( PBH ) is a rare , but severe , metabolic disorder arising months to years after bariatric surgery .

## Item MedMentions:test:2776
Example input:
Sentence: We found a possible association between inflammatory markers and exclusive breastfeeding duration in adolescents , regardless of their BMI .

Example answer:
{"entities": [{"text": "found", "type": "Finding"}, {"text": "possible", "type": "Finding"}, {"text": "markers", "type": "ClinicalAttribute"}, {"text": "BMI", "type": "ClinicalAttribute"}]}

Example input:
Sentence: On the other hand , in elderly patients , lesions were characterized by a single , large , well - demarcated amorphous calcified deposit surrounded by fibrous tissue , without chronic inflammation or foreign body reaction .

Example answer:
{"entities": [{"text": "elderly", "type": "PopulationGroup"}, {"text": "lesions", "type": "Finding"}, {"text": "well - demarcated amorphous calcified deposit", "type": "BiologicFunction"}, {"text": "surrounded", "type": "SpatialConcept"}, {"text": "fibrous tissue", "type": "AnatomicalStructure"}, {"text": "chronic inflammation", "type": "BiologicFunction"}, {"text": "foreign body reaction", "type": "BiologicFunction"}]}

Example input:
Sentence: Hypertension was the most frequent comorbidity ( 40 . 0 % ) , followed by diabetes mellitus ( 17 . 8 % ) and Alzheimer 's disease ( 14 . 8 % ) .

Example answer:
{"entities": [{"text": "Hypertension", "type": "BiologicFunction"}, {"text": "diabetes mellitus", "type": "BiologicFunction"}, {"text": "Alzheimer 's disease", "type": "BiologicFunction"}]}

Example input:
Sentence: In this study , youth with chronic pain associated with juvenile fibromyalgia ( JFM ) , juvenile idiopathic arthritis ( JIA ) , or sickle cell disease ( SCD ) ( ages 8 to 18 years ) from three pediatric centers completed all 47 candidate items for development of the pain behavior item bank along with established measures of pain interference , depressive symptoms , fatigue , average pain intensity , and pain catastrophizing .

Example answer:
{"entities": [{"text": "chronic pain", "type": "Finding"}, {"text": "juvenile fibromyalgia", "type": "BiologicFunction"}, {"text": "JFM", "type": "BiologicFunction"}, {"text": "juvenile idiopathic arthritis", "type": "BiologicFunction"}, {"text": "JIA", "type": "BiologicFunction"}, {"text": "sickle cell disease", "type": "BiologicFunction"}, {"text": "SCD", "type": "BiologicFunction"}, {"text": "pediatric centers", "type": "Organization"}, {"text": "items", "type": "IntellectualProduct"}, {"text": "item bank", "type": "IntellectualProduct"}, {"text": "pain interference", "type": "IntellectualProduct"}, {"text": "depressive symptoms", "type": "Finding"}, {"text": "fatigue", "type": "Finding"}, {"text": "average pain intensity", "type": "IntellectualProduct"}, {"text": "pain catastrophizing", "type": "BiologicFunction"}]}

Example input:
Sentence: 48 ; 95 % CI 1 . 31 - 4 . 70 ) , and cystic fibrosis ( OR 2 . 17 ; 95 % CI 1 . 16 - 4 . 06 ) .

Example answer:
{"entities": [{"text": "cystic fibrosis", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , we found an association between inflammatory and degenerative biomarkers .

Example answer:
{"entities": [{"text": "biomarkers", "type": "ClinicalAttribute"}]}

Example input:
Sentence: Histological signs of chronic inflammation affecting ventricular myocardium are strongly associated with AF and demonstrate significant correlation with fibrosis extent that cannot be explained by cardiovascular comorbidities otherwise .

Example answer:
{"entities": [{"text": "signs", "type": "Finding"}, {"text": "chronic inflammation", "type": "BiologicFunction"}, {"text": "ventricular myocardium", "type": "AnatomicalStructure"}, {"text": "AF", "type": "BiologicFunction"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "cardiovascular", "type": "SpatialConcept"}]}

Example input:
Sentence: Histological evidence of inflammatory reaction associated with fibrosis in the atrial and ventricular walls in a case - control study of patients with history of atrial fibrillation Chronic inflammation in the atrial myocardium was shown to play an important role in the development of atrial fibrosis in patients with atrial fibrillation ( AF ) .

Example answer:
{"entities": [{"text": "inflammatory reaction", "type": "BiologicFunction"}, {"text": "fibrosis", "type": "BiologicFunction"}, {"text": "atrial", "type": "AnatomicalStructure"}, {"text": "ventricular walls", "type": "AnatomicalStructure"}, {"text": "case - control study", "type": "ResearchActivity"}, {"text": "history", "type": "Finding"}, {"text": "atrial fibrillation", "type": "BiologicFunction"}, {"text": "Chronic inflammation", "type": "BiologicFunction"}, {"text": "atrial myocardium", "type": "AnatomicalStructure"}, {"text": "role", "type": "IntellectualProduct"}, {"text": "development", "type": "BiologicFunction"}, {"text": "AF", "type": "BiologicFunction"}]}

Example input:
Sentence: Histopathological studies showed higher inflammatory cell infiltrates , cardiac fibrosis , and collagen deposition in LPS group , which were reduced by the administration of NS .

Example answer:
{"entities": [{"text": "studies", "type": "ResearchActivity"}, {"text": "inflammatory cell infiltrates", "type": "BodySubstance"}, {"text": "cardiac fibrosis", "type": "BiologicFunction"}, {"text": "collagen", "type": "Chemical"}, {"text": "LPS", "type": "Chemical"}, {"text": "administration", "type": "HealthCareActivity"}, {"text": "NS", "type": "Eukaryote"}]}

Example input:
Sentence: Fibrosis extent demonstrated correlation with both CD3 + and CD45 + cell counts in the right ( r = 0 . 781 , P < 0 . 001 for CD45 + and r = 0 .

Example answer:
{"entities": [{"text": "Fibrosis", "type": "BiologicFunction"}, {"text": "extent", "type": "SpatialConcept"}, {"text": "CD3 +", "type": "Chemical"}, {"text": "CD45 +", "type": "Chemical"}, {"text": "cell counts", "type": "HealthCareActivity"}]}

Input:
Sentence: Neither fibrosis nor inflammatory cell count showed association with either age or comorbidities .

## Item MedMentions:test:2737
Example input:
Sentence: We have previously clarified that exposure to cigarette smoke extract ( CSE ) of a mouse melanoma cell culture medium causes rapid reduction of intracellular GSH levels , and that the GSH - MVK adduct can be detected by LC / MS analysis while the GSH - CA adduct is hardly detected .

Example answer:
{"entities": [{"text": "cigarette smoke extract", "type": "Chemical"}, {"text": "CSE", "type": "Chemical"}, {"text": "mouse", "type": "Eukaryote"}, {"text": "melanoma cell", "type": "AnatomicalStructure"}, {"text": "culture medium", "type": "Chemical"}, {"text": "intracellular", "type": "SpatialConcept"}, {"text": "GSH", "type": "Chemical"}, {"text": "MVK", "type": "Chemical"}, {"text": "detected", "type": "Finding"}, {"text": "LC / MS analysis", "type": "HealthCareActivity"}, {"text": "CA", "type": "Chemical"}]}

Example input:
Sentence: On the contrary , heavy smoking decreased the risk for men , HR 0 .

Example answer:
{"entities": [{"text": "men", "type": "PopulationGroup"}]}

Example input:
Sentence: Comparing current smokers and nonsmokers , some significant associations from adjusted analyses included the following : having a Mental Component Summary score ( a measure of overall mental health ) above the mean of the US population relative to below the mean ( adjusted odds ratio [ aOR ] = 0 . 81 , 95 % CI : 0 . 73 - 0 . 90 ) ; having physician - diagnosed depression

Example answer:
{"entities": [{"text": "current smokers", "type": "Finding"}, {"text": "nonsmokers", "type": "Finding"}, {"text": "adjusted analyses", "type": "ResearchActivity"}, {"text": "mental health", "type": "BiologicFunction"}, {"text": "US", "type": "SpatialConcept"}, {"text": "population", "type": "PopulationGroup"}, {"text": "physician", "type": "ProfessionalOrOccupationalGroup"}, {"text": "diagnosed", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}]}

Example input:
Sentence: Furthermore , PHAs have high rates of depression ( 40 - 60 % ) , a risk factor for smoking cessation relapse .

Example answer:
{"entities": [{"text": "depression", "type": "BiologicFunction"}, {"text": "risk factor", "type": "Finding"}]}

Example input:
Sentence: Rates of cigarette smoking , a leading contributor to CVD among PHAs , are 40 - 70 % ( 2 - 3 times higher than the general population ) .

Example answer:
{"entities": [{"text": "CVD", "type": "BiologicFunction"}, {"text": "general population", "type": "PopulationGroup"}]}

Example input:
Sentence: A significant proportion of smokers with emphysema according to low - dose chest CT scanning but without airway limitation had alterations in their quality of life , number of exacerbations , Dlco values , and oxygen saturation during the 6MWT test .

Example answer:
{"entities": [{"text": "smokers", "type": "Finding"}, {"text": "emphysema", "type": "BiologicFunction"}, {"text": "chest CT scanning", "type": "HealthCareActivity"}, {"text": "airway", "type": "AnatomicalStructure"}, {"text": "exacerbations", "type": "Finding"}, {"text": "Dlco", "type": "HealthCareActivity"}, {"text": "oxygen saturation", "type": "BiologicFunction"}, {"text": "6MWT test", "type": "HealthCareActivity"}]}

Example input:
Sentence: Compared to the control group , a higher proportion of patients with mesenteric embolization were current smokers ( 89 % vs .

Example answer:
{"entities": [{"text": "mesenteric embolization", "type": "BiologicFunction"}, {"text": "smokers", "type": "Finding"}]}

Example input:
Sentence: To better understand the risk - benefit ratio of ECs , more information is needed about net nicotine consumption and toxicant exposure of cigarette smokers switching to ECs .

Example answer:
{"entities": [{"text": "ECs", "type": "MedicalDevice"}, {"text": "nicotine", "type": "Chemical"}, {"text": "smokers", "type": "Finding"}]}

Example input:
Sentence: Those who switched exclusively to ECs for at least half of the study period significantly reduced two additional VOCs .

Example answer:
{"entities": [{"text": "ECs", "type": "MedicalDevice"}, {"text": "study", "type": "ResearchActivity"}, {"text": "VOCs", "type": "Chemical"}]}

Example input:
Sentence: Smokers using ECs over 4 - weeks maintained cotinine levels and experienced significant reductions in carbon monoxide , NNAL , and two out of eight measured VOC metabolites .

Example answer:
{"entities": [{"text": "Smokers", "type": "Finding"}, {"text": "ECs", "type": "MedicalDevice"}, {"text": "cotinine levels", "type": "HealthCareActivity"}, {"text": "carbon monoxide", "type": "Chemical"}, {"text": "NNAL", "type": "Chemical"}, {"text": "VOC", "type": "Chemical"}, {"text": "metabolites", "type": "Chemical"}]}

Input:
Sentence: Smokers switching exclusively to ECs for at least half of the study period demonstrated significant reductions in HEMA ( p > = 0 . 03 ) and AAMA ( p < 0 . 01 ) .

## Item MedMentions:test:2809
Example input:
Sentence: It is judged that below an absorbed dose of 100 mGy , no clinically relevant tissue damage occurs , forming the basis for the current radiation protection system concerning non - cancer effects .

Example answer:
{"entities": [{"text": "tissue damage", "type": "InjuryOrPoisoning"}, {"text": "radiation protection system", "type": "HealthCareActivity"}]}

Example input:
Sentence: The radiation dose imparted to members of public due to the levels observed is well within station technical specification limit for 3H .

Example answer:
{"entities": [{"text": "members of public", "type": "Organization"}, {"text": "3H", "type": "Chemical"}]}

Example input:
Sentence: Establishment of a mouse model of 70 % lethal dose by total - body irradiation Whereas increasing concerns about radiation exposure to nuclear disasters or side effects of anticancer radiotherapy , relatively little research for radiation damages or remedy has been done .

Example answer:
{"entities": [{"text": "mouse model", "type": "BiologicFunction"}, {"text": "total - body irradiation", "type": "HealthCareActivity"}, {"text": "radiation exposure", "type": "InjuryOrPoisoning"}, {"text": "side effects", "type": "BiologicFunction"}, {"text": "anticancer", "type": "HealthCareActivity"}, {"text": "radiotherapy", "type": "HealthCareActivity"}, {"text": "research", "type": "ResearchActivity"}, {"text": "radiation damages", "type": "BiologicFunction"}]}

Example input:
Sentence: Recent epidemiological findings point , however , to an excess risk of non - cancer diseases following exposure to lower doses of ionizing radiation than was previously thought .

Example answer:
{"entities": [{"text": "non - cancer", "type": "Finding"}, {"text": "diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Radiation therapy was delivered on a Cobalt - 60 unit using a single fraction of 16 Gy .

Example answer:
{"entities": [{"text": "Radiation therapy", "type": "HealthCareActivity"}, {"text": "Cobalt - 60", "type": "Chemical"}]}

Example input:
Sentence: We examine radiosensitivity at the dose of 2 Gy , a routinely administered dose during fractionated radiotherapy , and we determined that a wide range of DSBs were induced by the given dose among healthy individuals , with highly radiosensitive individuals harboring more IR - induced breaks in the genome than radioresistant individuals following exposure to the same dose .

Example answer:
{"entities": [{"text": "fractionated radiotherapy", "type": "HealthCareActivity"}, {"text": "DSBs", "type": "BiologicFunction"}, {"text": "individuals", "type": "PopulationGroup"}, {"text": "genome", "type": "AnatomicalStructure"}, {"text": "exposure to", "type": "InjuryOrPoisoning"}]}

Example input:
Sentence: Biological basis of radiation protection needs rejuvenation Human beings encounter radiation in many different situations - from proximity to radioactive waste sites to participation in medical procedures using X - rays etc .

Example answer:
{"entities": [{"text": "basis", "type": "Chemical"}, {"text": "radiation protection", "type": "HealthCareActivity"}, {"text": "rejuvenation", "type": "HealthCareActivity"}, {"text": "Human beings", "type": "Eukaryote"}, {"text": "proximity", "type": "SpatialConcept"}, {"text": "radioactive waste", "type": "Chemical"}, {"text": "sites", "type": "SpatialConcept"}, {"text": "medical procedures", "type": "HealthCareActivity"}]}

Example input:
Sentence: The potential for radiation from wireless technology to cause serious biological effects has important implications and necessitates a reevaluation of its near - ubiquitous presence , especially in hospitals and medical facilities .

Example answer:
{"entities": [{"text": "hospitals", "type": "Organization"}, {"text": "medical facilities", "type": "Organization"}]}

Example input:
Sentence: Ironically , the same health physics community that has been successful in demonstrating that exposures to radiation and to radioactive materials can be effectively managed is shrinking at an increasingly rapid rate .

Example answer:
{"entities": [{"text": "health physics", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "exposures to radiation", "type": "InjuryOrPoisoning"}, {"text": "radioactive materials", "type": "Chemical"}, {"text": "effectively managed", "type": "HealthCareActivity"}]}

Example input:
Sentence: The use of radioactive materials and radiation - generating devices is prevalent today .

Example answer:
{"entities": [{"text": "prevalent today", "type": "SpatialConcept"}]}

Input:
Sentence: Radiation doses occur continuously including during airline flights , in our homes , during medical procedures , and in energy production .

## Item MedMentions:test:2599
Example input:
Sentence: Here , we identified putative target genes of PHY signaling in the moss Physcomitrella patens and found light - regulated genes that are putative orthologs of PIF - controlled genes in Arabidopsis .

Example answer:
{"entities": [{"text": "genes", "type": "AnatomicalStructure"}, {"text": "PHY", "type": "Chemical"}, {"text": "signaling", "type": "BiologicFunction"}, {"text": "moss", "type": "Eukaryote"}, {"text": "Physcomitrella patens", "type": "Eukaryote"}, {"text": "light - regulated genes", "type": "AnatomicalStructure"}, {"text": "orthologs", "type": "AnatomicalStructure"}, {"text": "PIF - controlled genes", "type": "AnatomicalStructure"}, {"text": "Arabidopsis", "type": "Eukaryote"}]}

Example input:
Sentence: Our studies reveal a new paradigm of host - pathogen interactions , in which pathogens exploit conserved host post - translational modifications , thereby achieving highly specific receptor binding while also tolerating genetic changes across multiple isoforms of receptors .

Example answer:
{"entities": [{"text": "host - pathogen interactions", "type": "BiologicFunction"}, {"text": "post - translational modifications", "type": "BiologicFunction"}, {"text": "receptor binding", "type": "BiologicFunction"}, {"text": "genetic changes", "type": "BiologicFunction"}, {"text": "isoforms", "type": "Chemical"}, {"text": "receptors", "type": "Chemical"}]}

Example input:
Sentence: Although plant hormone synthesis and signal transduction were both significantly affected by DADS , the expression trends of the genes in these two pathways were conflicting .

Example answer:
{"entities": [{"text": "plant", "type": "Eukaryote"}, {"text": "hormone synthesis", "type": "BiologicFunction"}, {"text": "signal transduction", "type": "BiologicFunction"}, {"text": "DADS", "type": "Chemical"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "genes", "type": "AnatomicalStructure"}, {"text": "pathways", "type": "BiologicFunction"}]}

Example input:
Sentence: Silencing PLA2 influenced the expression of immune - related genes , including MyD88 and defensin in the Toll pathway and relish and diptericin in the Imd pathway .

Example answer:
{"entities": [{"text": "Silencing", "type": "BiologicFunction"}, {"text": "PLA2", "type": "AnatomicalStructure"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "immune - related genes", "type": "AnatomicalStructure"}, {"text": "MyD88", "type": "AnatomicalStructure"}, {"text": "defensin", "type": "Chemical"}, {"text": "Toll pathway", "type": "BiologicFunction"}, {"text": "relish", "type": "Chemical"}, {"text": "diptericin", "type": "Chemical"}]}

Example input:
Sentence: TRPM2 -mediated Ca ( 2 + ) signaling has been implicated in the aggravation of inflammatory diseases .

Example answer:
{"entities": [{"text": "TRPM2", "type": "Chemical"}, {"text": "Ca ( 2 + ) signaling", "type": "BiologicFunction"}, {"text": "aggravation", "type": "Finding"}, {"text": "inflammatory diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Interplant Aboveground Signaling Prompts Upregulation of Auxin Promoter and Malate Transporter as Part of Defensive Response in the Neighboring Plants When disrupted by stimuli such as herbivory , pathogenic infection , or mechanical wounding , plants secrete signals such as root exudates and volatile organic compounds ( VOCs ) .

Example answer:
{"entities": [{"text": "Upregulation", "type": "BiologicFunction"}, {"text": "Auxin", "type": "Chemical"}, {"text": "Promoter", "type": "Chemical"}, {"text": "Malate", "type": "Chemical"}, {"text": "Transporter", "type": "BiologicFunction"}, {"text": "Defensive Response", "type": "BiologicFunction"}, {"text": "Neighboring", "type": "SpatialConcept"}, {"text": "Plants", "type": "Eukaryote"}, {"text": "herbivory", "type": "Eukaryote"}, {"text": "pathogenic infection", "type": "BiologicFunction"}, {"text": "mechanical wounding", "type": "InjuryOrPoisoning"}, {"text": "plants", "type": "Eukaryote"}, {"text": "secrete", "type": "BiologicFunction"}, {"text": "root", "type": "Eukaryote"}, {"text": "volatile organic compounds", "type": "Chemical"}, {"text": "VOCs", "type": "Chemical"}]}

Example input:
Sentence: Pairwise statistical testing of differential expression followed by co - expression network analysis revealed that physically clustered genes coding for putative virulence functions were induced depending on substrate or stage of plant infection .

Example answer:
{"entities": [{"text": "Pairwise statistical testing", "type": "IntellectualProduct"}, {"text": "expression", "type": "BiologicFunction"}, {"text": "co - expression network analysis", "type": "ResearchActivity"}, {"text": "clustered genes", "type": "AnatomicalStructure"}, {"text": "coding", "type": "SpatialConcept"}, {"text": "virulence", "type": "BiologicFunction"}, {"text": "plant", "type": "Eukaryote"}, {"text": "infection", "type": "BiologicFunction"}]}

Example input:
Sentence: Brassinosteroid / Abscisic Acid Antagonism in Balancing Growth and Stress In this issue of Developmental Cell , Gui et al . ( 2016 ) show that an abscisic acid - inducible remorin protein in rice directly interacts with critical brassinosteroid signaling components to attenuate the brassinosteroid response , thus illuminating one aspect of the brassinosteroid / abscisic acid antagonism .

Example answer:
{"entities": [{"text": "Brassinosteroid", "type": "Chemical"}, {"text": "Abscisic Acid", "type": "Chemical"}, {"text": "Growth", "type": "BiologicFunction"}, {"text": "Stress", "type": "Finding"}, {"text": "issue", "type": "IntellectualProduct"}, {"text": "Developmental Cell", "type": "BiologicFunction"}, {"text": "abscisic acid", "type": "Chemical"}, {"text": "remorin protein", "type": "Chemical"}, {"text": "rice", "type": "Eukaryote"}, {"text": "brassinosteroid", "type": "Chemical"}, {"text": "signaling components", "type": "Chemical"}]}

Example input:
Sentence: Silencing of the genes RDR1 , NPR1 and DCL2 / DCL4 , associated with these defence pathways , enhanced virus spread and accumulation in SO plants in comparison with non - silenced controls , whereas silencing of the genes NPR3 / NPR4 , associated with the hypersensitive response , produced a slight decrease in CTV accumulation and reduced stunting of SO grafted on CTV - infected rough lemon plants .

Example answer:
{"entities": [{"text": "Silencing of the genes", "type": "BiologicFunction"}, {"text": "RDR1", "type": "AnatomicalStructure"}, {"text": "NPR1", "type": "AnatomicalStructure"}, {"text": "DCL2", "type": "AnatomicalStructure"}, {"text": "DCL4", "type": "AnatomicalStructure"}, {"text": "defence pathways", "type": "BiologicFunction"}, {"text": "virus spread", "type": "BiologicFunction"}, {"text": "accumulation", "type": "Finding"}, {"text": "SO plants", "type": "Eukaryote"}, {"text": "silencing of the genes", "type": "BiologicFunction"}, {"text": "NPR3", "type": "AnatomicalStructure"}, {"text": "NPR4", "type": "AnatomicalStructure"}, {"text": "hypersensitive response", "type": "BiologicFunction"}, {"text": "CTV", "type": "Virus"}, {"text": "stunting", "type": "BiologicFunction"}, {"text": "SO", "type": "Eukaryote"}, {"text": "infected", "type": "Finding"}, {"text": "lemon plants", "type": "Eukaryote"}]}

Example input:
Sentence: We speculate that plant -derived signal - induced upregulation of root -specific ALMT1 in the undamaged neighboring plants sharing the environment with stressed plants may associate more with the benign microbes belowground .

Example answer:
{"entities": [{"text": "plant", "type": "Eukaryote"}, {"text": "upregulation", "type": "BiologicFunction"}, {"text": "root -specific ALMT1", "type": "Chemical"}, {"text": "neighboring", "type": "SpatialConcept"}, {"text": "plants", "type": "Eukaryote"}, {"text": "environment", "type": "SpatialConcept"}, {"text": "stressed", "type": "Finding"}]}

Input:
Sentence: In plant - pathogen interactions , DEGs related to calcium signaling were primarily inhibited , while those encoding pathogenesis - related proteins were primarily up - regulated .

## Item MedMentions:test:2891
Example input:
Sentence: Multinomial logistic regressions ( crude and adjusted for sex and country ) tested associations between recent pain and alcohol use in the pooled multicountry sample .

Example answer:
{"entities": [{"text": "logistic regressions", "type": "ResearchActivity"}, {"text": "crude", "type": "Chemical"}, {"text": "country", "type": "SpatialConcept"}, {"text": "pain", "type": "Finding"}, {"text": "multicountry", "type": "SpatialConcept"}]}

Example input:
Sentence: Multivariate logistic regression analyses ( adjusted for age , gender , education level , physical activity , alcohol use , smoking status , depression , arrhythmia , myocardial infarction , heart failure , stroke ) showed that participants with better feelings of affection , behavioral confirmation and stable good social support had a lower risk of incident SMC .

Example answer:
{"entities": [{"text": "education level", "type": "Finding"}, {"text": "smoking status", "type": "ClinicalAttribute"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "arrhythmia", "type": "Finding"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "heart failure", "type": "BiologicFunction"}, {"text": "stroke", "type": "BiologicFunction"}, {"text": "participants", "type": "PopulationGroup"}, {"text": "feelings", "type": "BiologicFunction"}, {"text": "affection", "type": "BiologicFunction"}, {"text": "confirmation", "type": "Finding"}, {"text": "SMC", "type": "BiologicFunction"}]}

Example input:
Sentence: The Copenhagen Psychosocial Questionnaire II was used to measure violence and nurse job outcomes .

Example answer:
{"entities": [{"text": "Copenhagen Psychosocial Questionnaire II", "type": "IntellectualProduct"}, {"text": "violence", "type": "BiologicFunction"}, {"text": "nurse", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Multiple logistic regression was used to estimate the adjusted association of background characteristics , depressed mood , and perceived heroin refusal self - efficacy with preference for MAT .

Example answer:
{"entities": [{"text": "Multiple logistic regression", "type": "ResearchActivity"}, {"text": "depressed mood", "type": "Finding"}, {"text": "perceived", "type": "BiologicFunction"}, {"text": "heroin", "type": "Chemical"}, {"text": "self - efficacy", "type": "BiologicFunction"}, {"text": "MAT", "type": "HealthCareActivity"}]}

Example input:
Sentence: Correlation coefficients indicated that all four executive functioning measures and the two punishment measures were significantly correlated with aggression .

Example answer:
{"entities": [{"text": "executive functioning", "type": "BiologicFunction"}]}

Example input:
Sentence: Multiple linear regressions were conducted to identify predictive factors for elevated specific PTSD symptoms and elevated nonspecific PTSD symptoms .

Example answer:
{"entities": [{"text": "predictive factors", "type": "IntellectualProduct"}, {"text": "PTSD", "type": "BiologicFunction"}, {"text": "symptoms", "type": "Finding"}]}

Example input:
Sentence: Predicting violence and recidivism in a large sample of males on probation or parole This study evaluated the utility of items and scales from the Iowa Violence and Victimization Instrument in a sample of 1961 males from the state of Iowa who were on probation or released from prison to parole supervision .

Example answer:
{"entities": [{"text": "violence", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}, {"text": "Iowa", "type": "SpatialConcept"}, {"text": "Violence", "type": "BiologicFunction"}, {"text": "Instrument", "type": "IntellectualProduct"}, {"text": "released from prison", "type": "Finding"}]}

Example input:
Sentence: Workplace Violence and Job Outcomes of Newly Licensed Nurses The purpose of this study was to examine the prevalence of workplace violence toward newly licensed nurses and the relationship between workplace violence and job outcomes .

Example answer:
{"entities": [{"text": "Licensed Nurses", "type": "ProfessionalOrOccupationalGroup"}, {"text": "examine", "type": "Finding"}, {"text": "licensed nurses", "type": "ProfessionalOrOccupationalGroup"}]}

Example input:
Sentence: Multivariate logistic regression models were used to estimate the association between job strain and T2DM .

Example answer:
{"entities": [{"text": "Multivariate logistic regression models", "type": "IntellectualProduct"}, {"text": "job strain", "type": "Finding"}, {"text": "T2DM", "type": "BiologicFunction"}]}

Example input:
Sentence: Violence perpetrated by nurse colleagues had a significant relationship with all four job outcomes , while violence by physicians had a significant inverse relationship with job satisfaction .

Example answer:
{"entities": [{"text": "Violence", "type": "BiologicFunction"}, {"text": "nurse", "type": "ProfessionalOrOccupationalGroup"}, {"text": "violence", "type": "BiologicFunction"}, {"text": "physicians", "type": "ProfessionalOrOccupationalGroup"}, {"text": "job satisfaction", "type": "BiologicFunction"}]}

Input:
Sentence: Multiple linear and logistic regression analyses were conducted to examine the relationship between violence and job outcomes .

## Item MedMentions:test:2725
Example input:
Sentence: Rates and predictors of injury in a population - based cohort of people living with HIV Injuries are responsible for 10 % of the global burden of disease ; however , the epidemiology of injury among people living with HIV ( PLHIV ) has not been well elucidated .

Example answer:
{"entities": [{"text": "injury", "type": "InjuryOrPoisoning"}, {"text": "cohort", "type": "PopulationGroup"}, {"text": "people", "type": "PopulationGroup"}, {"text": "HIV", "type": "BiologicFunction"}, {"text": "Injuries", "type": "InjuryOrPoisoning"}, {"text": "disease", "type": "BiologicFunction"}, {"text": "people living with HIV", "type": "BiologicFunction"}, {"text": "PLHIV", "type": "BiologicFunction"}]}

Example input:
Sentence: Population -based community study ( Canberra and Queanbeyan , Australia ) .

Example answer:
{"entities": [{"text": "Population", "type": "PopulationGroup"}, {"text": "study", "type": "ResearchActivity"}, {"text": "Canberra", "type": "SpatialConcept"}, {"text": "Australia", "type": "SpatialConcept"}]}

Example input:
Sentence: Spatio - Temporal History of HIV - 1 CRF35 _ AD in Afghanistan and Iran HIV - 1 Circulating Recombinant Form 35 _ AD ( CRF35 _ AD ) has an important position in the epidemiological profile of Afghanistan and Iran .

Example answer:
{"entities": [{"text": "Spatio - Temporal History", "type": "ResearchActivity"}, {"text": "Afghanistan", "type": "SpatialConcept"}, {"text": "Iran", "type": "SpatialConcept"}, {"text": "HIV - 1 Circulating Recombinant Form 35 _ AD", "type": "Virus"}, {"text": "epidemiological", "type": "BiomedicalOccupationOrDiscipline"}]}

Example input:
Sentence: In all , 181 , 814 BC patients ( 1 , 516 male and 180 , 298 female ) were eligible for this study .

Example answer:
{"entities": [{"text": "BC", "type": "BiologicFunction"}, {"text": "study", "type": "ResearchActivity"}]}

Example input:
Sentence: Genotype data were also available from 5154 healthy UK controls from the Wellcome Trust ( WTCCC2 ) for comparison .

Example answer:
{"entities": [{"text": "Wellcome Trust ( WTCCC2 )", "type": "ResearchActivity"}]}

Example input:
Sentence: Cost - Effectiveness of the ' One4All ' HIV Linkage Intervention in Guangxi Zhuang Autonomous Region , China In Guangxi Zhuang Autonomous Region , China , an estimated 80 % of newly - identified antiretroviral therapy ( ART ) - eligible patients are not engaged in ART .

Example answer:
{"entities": [{"text": "One4All", "type": "HealthCareActivity"}, {"text": "HIV", "type": "BiologicFunction"}, {"text": "Intervention", "type": "HealthCareActivity"}, {"text": "Guangxi Zhuang Autonomous Region", "type": "SpatialConcept"}, {"text": "China", "type": "SpatialConcept"}, {"text": "antiretroviral therapy", "type": "HealthCareActivity"}, {"text": "ART", "type": "HealthCareActivity"}]}

Example input:
Sentence: Birth records with covariates were obtained from the BC Perinatal Database Registry ( N = 232 , 291 ) .

Example answer:
{"entities": [{"text": "BC Perinatal Database Registry", "type": "IntellectualProduct"}]}

Example input:
Sentence: Using Canadian census data , published literature and expert opinions , two population - based , top - down mathematical models were developed to estimate the supply and demand for donor sperm and the feasibility of an ASD program .

Example answer:
{"entities": [{"text": "published literature", "type": "IntellectualProduct"}, {"text": "two population - based , top - down mathematical models", "type": "IntellectualProduct"}, {"text": "donor", "type": "PopulationGroup"}, {"text": "sperm", "type": "AnatomicalStructure"}, {"text": "feasibility", "type": "ResearchActivity"}]}

Example input:
Sentence: The dataset was provided by the Child Outcomes Research Consortium , which collects outcome measures from child services across the UK .

Example answer:
{"entities": [{"text": "dataset", "type": "IntellectualProduct"}, {"text": "Child Outcomes Research Consortium", "type": "ProfessionalOrOccupationalGroup"}, {"text": "child services", "type": "HealthCareActivity"}, {"text": "UK", "type": "SpatialConcept"}]}

Example input:
Sentence: We populated the model with data from the One4All trial ( CTN - 0056 ) , China CDC HIV registry and published reports .

Example answer:
{"entities": [{"text": "One4All trial", "type": "HealthCareActivity"}, {"text": "CTN - 0056", "type": "HealthCareActivity"}, {"text": "China", "type": "SpatialConcept"}, {"text": "CDC", "type": "Organization"}, {"text": "HIV", "type": "BiologicFunction"}, {"text": "published reports", "type": "IntellectualProduct"}]}

Input:
Sentence: A population - based dataset was created via linkage between the BC Centre for Excellence in HIV / AIDS and PopulationDataBC .

## Item MedMentions:test:2773
Example input:
Sentence: A positive correlation between physical activity level and neurocognitive function has been reported in healthy individuals , but it is unclear whether such a correlation exists in patients with schizophrenia and whether the relationship is different according to inpatients or outpatients .

Example answer:
{"entities": [{"text": "neurocognitive function", "type": "BiologicFunction"}, {"text": "healthy individuals", "type": "PopulationGroup"}, {"text": "schizophrenia", "type": "BiologicFunction"}]}

Example input:
Sentence: Physical Activity and Abnormal Blood Glucose Among Healthy Weight Adults Physical activity has been linked to prevention and treatment of prediabetes and diabetes in overweight and obese adults .

Example answer:
{"entities": [{"text": "Abnormal Blood Glucose", "type": "Finding"}, {"text": "treatment", "type": "HealthCareActivity"}, {"text": "prediabetes", "type": "BiologicFunction"}, {"text": "diabetes", "type": "BiologicFunction"}, {"text": "overweight and obese", "type": "BiologicFunction"}]}

Example input:
Sentence: 001 ) and high activity groups ( OR , 0 . 663 ; 95 % CI , 0 . 589 - 0 . 748 ; p = 0 . 001 ) than in the low activity group , even after adjusting for age , sex , smoking , underlying disease , and general or abdominal obesity and muscle mass .

Example answer:
{"entities": [{"text": "underlying disease", "type": "BiologicFunction"}, {"text": "general", "type": "BiologicFunction"}, {"text": "abdominal obesity", "type": "Finding"}, {"text": "muscle mass", "type": "Finding"}]}

Example input:
Sentence: Higher physical activity was associated with a lower likelihood of abnormal blood glucose in an adjusted Poisson regression .

Example answer:
{"entities": [{"text": "abnormal blood glucose", "type": "Finding"}, {"text": "Poisson regression", "type": "IntellectualProduct"}]}

Example input:
Sentence: Among healthy weight adults , low physical activity levels are significantly associated with abnormal blood glucose ( prediabetes and undiagnosed diabetes ) .

Example answer:
{"entities": [{"text": "abnormal blood glucose", "type": "Finding"}, {"text": "prediabetes", "type": "BiologicFunction"}, {"text": "undiagnosed", "type": "Finding"}, {"text": "diabetes", "type": "BiologicFunction"}]}

Example input:
Sentence: Association of physical activity on body composition , cardiometabolic risk factors , and prevalence of cardiovascular disease in the Korean population ( from the fifth Korea national health and nutrition examination survey , 2008 - 2011 ) Data regarding associations among physical activity ( PA ) level , body composition , and prevalence of cardiovascular diseases in Asian populations are rare .

Example answer:
{"entities": [{"text": "cardiometabolic risk factors", "type": "Finding"}, {"text": "cardiovascular disease", "type": "BiologicFunction"}, {"text": "Korean population", "type": "PopulationGroup"}, {"text": "Korea", "type": "SpatialConcept"}, {"text": "national health and nutrition examination survey", "type": "ResearchActivity"}, {"text": "cardiovascular diseases", "type": "BiologicFunction"}]}

Example input:
Sentence: Although higher physical activity was associated with better neurocognitive functions of outpatients , in inpatients with non - remitted schizophrenia , higher physical activity was associated with worsening of several cognitive domains .

Example answer:
{"entities": [{"text": "neurocognitive functions", "type": "BiologicFunction"}, {"text": "schizophrenia", "type": "BiologicFunction"}, {"text": "cognitive domains", "type": "BiologicFunction"}]}

Example input:
Sentence: In the outpatient group , higher physical activity was associated with faster Motor and Psychomotor Speeds in outpatients .

Example answer:
{"entities": [{"text": "Psychomotor", "type": "BiologicFunction"}]}

Example input:
Sentence: Degree of physical activity was positively correlated with eating disorder psychopathology in the sample with AN , and a trend towards a positive association between physical activity and levels of depression and anxiety was also found in this sample .

Example answer:
{"entities": [{"text": "positively correlated", "type": "Finding"}, {"text": "eating disorder", "type": "BiologicFunction"}, {"text": "psychopathology", "type": "BiomedicalOccupationOrDiscipline"}, {"text": "AN", "type": "BiologicFunction"}, {"text": "positive association", "type": "Finding"}, {"text": "depression", "type": "BiologicFunction"}, {"text": "anxiety", "type": "Finding"}]}

Example input:
Sentence: Regular physical activity was associated with a low prevalence of cardiovascular diseases ( stroke , myocardial infarction , stable angina , and chronic renal disease ) , which was independent of body composition and conventional risk factors in the Korean population , with a positive dose - response relationship .

Example answer:
{"entities": [{"text": "cardiovascular diseases", "type": "BiologicFunction"}, {"text": "stroke", "type": "InjuryOrPoisoning"}, {"text": "myocardial infarction", "type": "BiologicFunction"}, {"text": "stable angina", "type": "BiologicFunction"}, {"text": "chronic renal disease", "type": "BiologicFunction"}, {"text": "risk factors", "type": "Finding"}, {"text": "Korean population", "type": "PopulationGroup"}, {"text": "positive", "type": "Finding"}]}

Input:
Sentence: Among individuals with AN , physical activity was not significantly correlated with BMI , duration of illness , or number of days since hospital admission .

## Item MedMentions:test:2993
Example input:
Sentence: 4 . 86 ( 95 % CI , 1 . 9 - 11 .

Example answer:
{"entities": []}

Example input:
Sentence: 1 % ( 95 % CI : 24 . 3 - 27 . 9 ) , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 1 % ( 95 % CI : 54 . 6 , 82 . 3 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 50 % ( 95 % CI , 48 . 70 % to 88 . 30 % ) , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: 1 % ( 95 % CI 27 . 1 - 51 . 0 % ) in 2015 .

Example answer:
{"entities": []}

Example input:
Sentence: 81 ( 95 % CI 0 . 65 , 1 . 01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 9 % ( 95 % CI : 79 . 6 , 97 . 7 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 37 % ( 95 % CI : 11 . 35 - 11 . 40 ) .

Example answer:
{"entities": []}

Example input:
Sentence: 4 , 95 % CI = -15 .

Example answer:
{"entities": []}

Example input:
Sentence: 15 ( 95 % CI : 5 . 37 - 9 . 51 ) ] .

Example answer:
{"entities": []}

Input:
Sentence: 81 % ( 95 % CI 20 . 21 % - 30 . 07 % ) and 15 .

## Item MedMentions:test:2842
Example input:
Sentence: suzukii larvae and the fact that fruits used in bioassays often start to rot and dissolve before larvae have reached the adult stage .

Example answer:
{"entities": [{"text": "suzukii", "type": "Eukaryote"}, {"text": "larvae", "type": "Eukaryote"}, {"text": "fruits", "type": "Food"}, {"text": "bioassays", "type": "HealthCareActivity"}]}

Example input:
Sentence: Effects of deltamethrin were initially tested using a colonised strain of Culicoides nubeculosus Meigen and a modified World Health Organisation exposure assay .

Example answer:
{"entities": [{"text": "deltamethrin", "type": "Chemical"}, {"text": "Culicoides nubeculosus Meigen", "type": "Eukaryote"}, {"text": "World Health Organisation", "type": "Organization"}, {"text": "exposure assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: cholerae : these methods include swarm assay , temporal stimulation assay , capillary assay , and receptor methylation assay .

Example answer:
{"entities": [{"text": "cholerae", "type": "Bacterium"}, {"text": "swarm assay", "type": "HealthCareActivity"}, {"text": "temporal stimulation assay", "type": "HealthCareActivity"}, {"text": "capillary assay", "type": "HealthCareActivity"}, {"text": "receptor methylation assay", "type": "HealthCareActivity"}]}

Example input:
Sentence: Using a fragment based approach , over 1000 compounds were screened by a combination of differential scanning fluorimetry , NMR spectroscopy and enzymatic assay with pure recombinant HsaD to identify potential inhibitors .

Example answer:
{"entities": [{"text": "approach", "type": "SpatialConcept"}, {"text": "compounds", "type": "Chemical"}, {"text": "screened", "type": "HealthCareActivity"}, {"text": "differential scanning fluorimetry", "type": "HealthCareActivity"}, {"text": "NMR spectroscopy", "type": "HealthCareActivity"}, {"text": "enzymatic assay", "type": "HealthCareActivity"}, {"text": "HsaD", "type": "Chemical"}, {"text": "inhibitors", "type": "Chemical"}]}

Example input:
Sentence: Use of grape berries in bioassays made it possible to assess effects of an insecticide present on a fruit 's surface on oviposition and larval hatch from eggs .

Example answer:
{"entities": [{"text": "grape berries", "type": "Food"}, {"text": "bioassays", "type": "HealthCareActivity"}, {"text": "insecticide", "type": "Chemical"}, {"text": "fruit 's", "type": "Food"}, {"text": "surface", "type": "SpatialConcept"}, {"text": "oviposition", "type": "BiologicFunction"}, {"text": "larval", "type": "Eukaryote"}, {"text": "hatch", "type": "BiologicFunction"}, {"text": "eggs", "type": "AnatomicalStructure"}]}

Example input:
Sentence: Insecticidal effects of deltamethrin in laboratory and field populations of Culicoides species : how effective are host - contact reduction methods in India ? Bluetongue virus ( BTV ) is transmitted by Culicoides biting midges and causes bluetongue ( BT ) , a clinical disease observed primarily in sheep .

Example answer:
{"entities": [{"text": "deltamethrin", "type": "Chemical"}, {"text": "laboratory", "type": "Organization"}, {"text": "Culicoides species", "type": "Eukaryote"}, {"text": "methods", "type": "ResearchActivity"}, {"text": "India", "type": "SpatialConcept"}, {"text": "Bluetongue virus", "type": "Virus"}, {"text": "BTV", "type": "Virus"}, {"text": "transmitted", "type": "BiologicFunction"}, {"text": "Culicoides", "type": "Eukaryote"}, {"text": "biting midges", "type": "Eukaryote"}, {"text": "bluetongue", "type": "BiologicFunction"}, {"text": "BT", "type": "BiologicFunction"}, {"text": "clinical disease", "type": "BiologicFunction"}, {"text": "sheep", "type": "Eukaryote"}]}

Example input:
Sentence: The results demonstrate mainly the biotechnological potential of D .

Example answer:
{"entities": [{"text": "D .", "type": "Bacterium"}]}

Example input:
Sentence: Number of adult flies was significantly reduced if the bioassay medium was treated with an azadirachtin A containing insecticide both before or after egg deposition .

Example answer:
{"entities": [{"text": "flies", "type": "Eukaryote"}, {"text": "bioassay", "type": "HealthCareActivity"}, {"text": "azadirachtin A", "type": "Chemical"}, {"text": "insecticide", "type": "Chemical"}]}

Example input:
Sentence: Suitability of our bioassays was validated in an assessment of the efficacy of four bioinsecticides and one synthetic insecticide against various developmental stages of D .

Example answer:
{"entities": [{"text": "bioassays", "type": "HealthCareActivity"}, {"text": "validated", "type": "ResearchActivity"}, {"text": "bioinsecticides", "type": "Chemical"}, {"text": "insecticide", "type": "Chemical"}, {"text": "developmental", "type": "BiologicFunction"}, {"text": "D .", "type": "Eukaryote"}]}

Example input:
Sentence: Insecticides tested in these three different bioassays with acetamiprid , spinosad or natural pyrethrins as active ingredients achieved a significant D .

Example answer:
{"entities": [{"text": "Insecticides", "type": "Chemical"}, {"text": "bioassays", "type": "HealthCareActivity"}, {"text": "acetamiprid", "type": "Chemical"}, {"text": "spinosad", "type": "Chemical"}, {"text": "pyrethrins", "type": "Chemical"}, {"text": "achieved", "type": "Finding"}, {"text": "D .", "type": "Eukaryote"}]}

Input:
Sentence: Efficacy of insecticides is usually assessed first in laboratory bioassays , which are compounded by the cryptic nature of D .
