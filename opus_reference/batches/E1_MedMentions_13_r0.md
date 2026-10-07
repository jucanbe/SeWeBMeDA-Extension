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

