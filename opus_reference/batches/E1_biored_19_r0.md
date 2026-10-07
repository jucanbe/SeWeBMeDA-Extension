# Task
You are a biomedical named entity recognition system for the BioRED annotation scheme.
Identify every mention of the following entity types in the sentence:
- CellLine: A specific cell line used in biomedical research (e.g., HeLa, A549).
- ChemicalEntity: A chemical compound, drug, or small molecule (e.g., doxorubicin, ethanol).
- DiseaseOrPhenotypicFeature: A disease or observable trait (e.g., Parkinson's disease, fever).
- GeneOrGeneProduct: A gene or its expressed product (e.g., TP53, insulin).
- OrganismTaxon: A species or strain (e.g., Homo sapiens, E. coli).
- SequenceVariant: A specific variation in a DNA/RNA/protein sequence (e.g., BRCA1 c.68_69delAG).

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

## Item biored:test:761
Example input:
Sentence: Modulation of PKCalpha by histamine receptors may be important in regulating cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "histamine receptors", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Therefore , radiation-induced NF-kB functions as a molecular link between tumor cells and immune cells in the tumor microenvironment for radiation-mediated tumor suppression .

Example answer:
{"entities": [{"text": "NF-kB", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: NRG-1 beta stimulated human and murine MPNST cell migration and invasion in a concentration-dependent manner in three-dimensional migration assays , acting as a chemotactic factor .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "murine", "type": "OrganismTaxon"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study was designed to evaluate the alterations in offspring rat cerebellum induced by maternal exposure to carmustine- [ 1,3-bis ( 2-chloroethyl ) -1-nitrosoure ] ( BCNU ) and to investigate the effects of exogenous melatonin upon cerebellar BCNU-induced cortical dysplasia , using histological and biochemical analyses .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "carmustine-", "type": "ChemicalEntity"}, {"text": "1,3-bis ( 2-chloroethyl ) -1-nitrosoure", "type": "ChemicalEntity"}, {"text": "BCNU", "type": "ChemicalEntity"}, {"text": "melatonin", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "cortical dysplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The melanocortin agonist NDP-MSH dose-dependently inhibited JNK activity in HEK293 cells stably expressing the human MC4R ; effects were reversed by melanocortin receptor antagonist .

Example answer:
{"entities": [{"text": "melanocortin", "type": "GeneOrGeneProduct"}, {"text": "NDP-MSH", "type": "ChemicalEntity"}, {"text": "JNK", "type": "GeneOrGeneProduct"}, {"text": "HEK293", "type": "CellLine"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "MC4R", "type": "GeneOrGeneProduct"}, {"text": "melanocortin receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , CBKOTg mice reduced levels of phosphorylated mitogen-activated protein kinase ( extracellular signal-regulated kinase ) 1/2 and cAMP response element-binding protein at Ser-133 and synaptic molecules such as N-methyl-D-aspartate receptor 1 ( NMDA receptor 1 ) , NMDA receptor 2A , PSD-95 and synaptophysin in the subiculum compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}, {"text": "extracellular signal-regulated kinase ) 1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding protein", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-D-aspartate receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 2A", "type": "GeneOrGeneProduct"}, {"text": "PSD-95", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The signal transduction target upon interleukin 1 beta ( IL1beta ) stimulation , the nuclear factor of kappa B ( NFkappaB ) activation , supports cancer development , signal transduction in which is mediated by FS-7 cell-associated cell surface antigen ( FAS ) signaling .

Example answer:
{"entities": [{"text": "interleukin 1 beta", "type": "GeneOrGeneProduct"}, {"text": "IL1beta", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor of kappa B", "type": "GeneOrGeneProduct"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FS-7 cell-associated cell surface antigen", "type": "GeneOrGeneProduct"}, {"text": "FAS", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: 5-Aza-2'-deoxy-cytidine and/or Trichostatin A treatments induced DOCK8 expression in lung cancer cell lines with reduced DOCK8 expression .

Example answer:
{"entities": [{"text": "5-Aza-2'-deoxy-cytidine", "type": "ChemicalEntity"}, {"text": "Trichostatin A", "type": "ChemicalEntity"}, {"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: AIMS : To elucidate how the nicotinic acetylcholine receptors expressed on bronchial and oral epithelial cells targeted by the tobacco nitrosamine ( 4- ( methylnitrosamino ) -1- ( 3-pyridyl ) -1-butanone ) ( NNK ) facilitate carcinogenic transformation .

