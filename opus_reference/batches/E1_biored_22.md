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

## Item biored:test:899
Example input:
Sentence: RESULTS : Maternal diabetes significantly increased the levels of CHOP , calnexin , phosphorylated ( p ) -eIF2a , p-PERK , and p-IRE1a ; triggered XBP1 mRNA splicing ; and enhanced ER chaperone gene expression in WT embryos .

Example answer:
{"entities": [{"text": "Maternal diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Silencing of PKCalpha prevented RAMH inhibition of Mz-ChA-1 cell growth and ablated RAMH effects on ERK1/2 phosphorylation .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "RAMH", "type": "ChemicalEntity"}, {"text": "Mz-ChA-1", "type": "CellLine"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Consistent with impaired growth , PKCalpha knockdown increased levels of the cyclin-dependent kinase ( CDK ) inhibitors p21 ( Cip1/WAF1 ) ( p21 ) and p27 ( Kip1 ) ( p27 ) .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "cyclin-dependent kinase", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "Cip1/WAF1", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Kip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Protein level of BDNF was reduced in Dox-treated rat ventricles , whereas BDNF and its receptor tropomyosin-related kinase B ( TrkB ) were markedly up-regulated after BDNF administration .

Example answer:
{"entities": [{"text": "tropomyosin-related kinase", "type": "GeneOrGeneProduct"}, {"text": "(", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed slightly reduced levels of OGT protein and reduced levels of its opposing enzyme O-GlcNAcase in both patient-derived fibroblasts , but global O-GlcNAc levels appeared to be unaffected .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "O-GlcNAcase", "type": "GeneOrGeneProduct"}, {"text": "patient-derived", "type": "OrganismTaxon"}, {"text": "O-GlcNAc", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Western blotting showed that the protein levels of p-IKKBalpha/beta and P65 were upregulated by the OGD/R treatment and such effects were significantly inhibited by NSP administration .

## Item biored:test:901
Example input:
Sentence: Gene deletion or pharmacological blockade of KCa3.1 protected against SOCE-induced Ca2+ overload and ER stress via the protein kinase B ( AKT ) signaling pathway in astrocytes .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Neuroprotective effects of melatonin upon the offspring cerebellar cortex in the rat model of BCNU-induced cortical dysplasia .

Example answer:
{"entities": [{"text": "melatonin", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "cortical dysplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "frataxin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Previous studies have suggested the cardioprotective effect of brain-derived neurotrophic factor ( BDNF ) .

Example answer:
{"entities": [{"text": "brain-derived neurotrophic factor", "type": "GeneOrGeneProduct"}, {"text": "BDNF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The present study aimed to investigate whether atorvastatin protects against CIN via anti-apoptotic effects by the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: On the other hand , induction of metallothionein ( MT ) by ZnSO ( 4 ) and its role in neuroprotection has been documented .

Example answer:
{"entities": [{"text": "metallothionein", "type": "ChemicalEntity"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}]}

Example input:
Sentence: TSPO ligands have shown anti-inflammatory and neuroprotective properties in models of CNS injury .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "CNS injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Our results thus verified the neuroprotective effects of NSP in ischemic astrocytes .

## Item biored:test:924
Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The mother and daughter were each heterozygous for PPARG nonsense mutation Y355X , whose protein product in vitro was transcriptionally inactive with no dominant-negative activity against the wild-type receptor .

Example answer:
{"entities": [{"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "Y355X", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : KCa3.1 expression was markedly associated with endoplasmic reticulum ( ER ) stress and unfolded protein response ( UPR ) in both Abeta-stimulated primary astrocytes and brain lysates of AD patients and APP/PS1 AD mice .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Abeta-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: CCK-activation of PAK2 showed several novel features being dependent on both receptor-activation states , having PLC- and PKC-dependent/independent components and small-GTPase-dependent/independent components .

Example answer:
{"entities": [{"text": "CCK-activation", "type": "GeneOrGeneProduct"}, {"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "PLC-", "type": "GeneOrGeneProduct"}, {"text": "PKC-dependent/independent", "type": "GeneOrGeneProduct"}, {"text": "small-GTPase-dependent/independent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We studied the possible effects of the expansion of ancient Mediterranean civilizations during the five centuries before and after Christ on the European distribution of the mutant allele for the chemokine receptor gene CCR5 which has a 32-bp deletion ( CCR5-Delta32 ) .

Example answer:
{"entities": [{"text": "chemokine receptor", "type": "GeneOrGeneProduct"}, {"text": "CCR5", "type": "GeneOrGeneProduct"}, {"text": "32-bp deletion", "type": "SequenceVariant"}, {"text": "CCR5-Delta32", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Specific knockdown of OPRM1 confers L-asparaginase resistance , validating our genome-wide retroviral shRNA library screening data .

Example answer:
{"entities": [{"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Thus , our study demonstrates for the first time , a novel OPRM1-mediated mechanism for L-asparaginase resistance in ALL , and identifies OPRM1 as a functional biomarker for defining high-risk subpopulations and for the detection of evolving resistant clones .

Example answer:
{"entities": [{"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Five of the forty genes -- ENT3 , IDP3 , JEM1 , ARG2 and HSP82 -- ranked highest in their ability to block alpha-syn-induced reactive oxygen species accumulation , and these five genes were characterized in more detail .

Example answer:
{"entities": [{"text": "ENT3", "type": "GeneOrGeneProduct"}, {"text": "IDP3", "type": "GeneOrGeneProduct"}, {"text": "JEM1", "type": "GeneOrGeneProduct"}, {"text": "ARG2", "type": "GeneOrGeneProduct"}, {"text": "HSP82", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn-induced", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Among the most highly repressed genes upon PPARa activation were several chemokines ( e.g .

## Item biored:test:849
Example input:
Sentence: We used rat pancreatic acini to explore the ability of GI-hormones/neurotransmitters/growth-factors to activate Group-I-PAKs and the signaling cascades involved .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "Group-I-PAKs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Metallothionein induction reduces caspase-3 activity and TNFalpha levels with preservation of cognitive function and intact hippocampal neurons in carmustine-treated rats .

Example answer:
{"entities": [{"text": "Metallothionein", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "carmustine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mechanistic studies revealed that OB rats are sensitized due to : ( 1 ) higher oxyradical stress leading to upregulation of uncoupling proteins 2 and 3 , ( 2 ) downregulation of cardiac peroxisome proliferators activated receptor-alpha , ( 3 ) decreased plasma adiponectin levels , ( 4 ) decreased cardiac fatty-acid oxidation ( 666.9+/-14.0 nmol/min/g heart in ND versus 400.2+/-11.8 nmol/min/g heart in OB ) , ( 5 ) decreased mitochondrial AMP-alpha2 protein kinase , and ( 6 ) 86 % drop in cardiac ATP levels accompanied by decreased ATP/ADP ratio after doxorubicin administration .

Example answer:
{"entities": [{"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "uncoupling proteins 2 and 3", "type": "GeneOrGeneProduct"}, {"text": "peroxisome proliferators activated receptor-alpha", "type": "GeneOrGeneProduct"}, {"text": "adiponectin", "type": "GeneOrGeneProduct"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "AMP-alpha2 protein kinase", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "ATP/ADP", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: We have recently shown that estrogen negatively modulates the hypotensive effect of clonidine ( mixed alpha2-/I1-receptor agonist ) in female rats and implicates the cardiovascular autonomic control in this interaction .

Example answer:
{"entities": [{"text": "estrogen", "type": "ChemicalEntity"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}, {"text": "alpha2-/I1-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: ( Anacardiaceae ) , on isoproterenol ( ISPH ) -induced myocardial infarction ( MI ) in rats through its antioxidative mechanism .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "ISPH", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: These data suggest that pilocarpine produced antiarrhythmic actions on arrhythmic rat and guinea pig models induced by aconitine or ouabain via stimulating the cardiac M ( 3 ) -mAChR .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "M ( 3 ) -mAChR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This study was designed to evaluate the effects of pilocarpine and explore the underlying ionic mechanism , using both aconitine-induced rat and ouabain-induced guinea pig arrhythmia models .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "aconitine-induced", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "ouabain-induced", "type": "ChemicalEntity"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: [ Ca ( 2+ ) ] ( i ) overload induced by aconitine or ouabain was reduced in isolated myocytes pretreated with pilocarpine .

Example answer:
{"entities": [{"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Input:
Sentence: Aconitine-induced Ca2+ overload causes arrhythmia and triggers apoptosis through p38 MAPK signaling pathway in rats .

## Item biored:test:862
Example input:
Sentence: Gastrointestinal hormones/neurotransmitters and growth factors can activate P21 activated kinase 2 in pancreatic acinar cells by novel mechanisms .

Example answer:
{"entities": [{"text": "Gastrointestinal", "type": "ChemicalEntity"}, {"text": "P21 activated kinase 2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CCK and other GI-hormones/neurotransmitters/growth-factors activate PAK2 via small GTPases ( CDC42/Rac1 ) , PKC and SFK but not cytosolic calcium or PI3K .

Example answer:
{"entities": [{"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "small GTPases", "type": "GeneOrGeneProduct"}, {"text": "CDC42/Rac1", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "SFK", "type": "GeneOrGeneProduct"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This cardioprotection is accompanied by decreased cardiac oxidative stress and triglycerides and increased cardiac fatty-acid oxidation , ATP synthesis , and upregulated JAK/STAT3 pathway .

Example answer:
{"entities": [{"text": "triglycerides", "type": "ChemicalEntity"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "JAK/STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Brain-derived neurotrophic factor attenuates doxorubicin-induced cardiac dysfunction through activating Akt signalling in rats .

Example answer:
{"entities": [{"text": "Brain-derived neurotrophic factor", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The current data showed that pilocarpine significantly delayed onset of arrhythmias , decreased the time course of ventricular tachycardia and fibrillation , reduced arrhythmia score , and increased the survival time of arrhythmic rats and guinea pigs .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmias", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ventricular tachycardia and fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "guinea pigs", "type": "OrganismTaxon"}]}

Example input:
Sentence: We have recently shown that estrogen negatively modulates the hypotensive effect of clonidine ( mixed alpha2-/I1-receptor agonist ) in female rats and implicates the cardiovascular autonomic control in this interaction .

Example answer:
{"entities": [{"text": "estrogen", "type": "ChemicalEntity"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}, {"text": "alpha2-/I1-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: These data suggest that pilocarpine produced antiarrhythmic actions on arrhythmic rat and guinea pig models induced by aconitine or ouabain via stimulating the cardiac M ( 3 ) -mAChR .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "M ( 3 ) -mAChR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This study was designed to evaluate the effects of pilocarpine and explore the underlying ionic mechanism , using both aconitine-induced rat and ouabain-induced guinea pig arrhythmia models .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "aconitine-induced", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "ouabain-induced", "type": "ChemicalEntity"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: [ Ca ( 2+ ) ] ( i ) overload induced by aconitine or ouabain was reduced in isolated myocytes pretreated with pilocarpine .

Example answer:
{"entities": [{"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Input:
Sentence: Hence , our results suggest that aconitine significantly aggravates Ca ( 2+ ) overload and causes arrhythmia and finally promotes apoptotic development via phosphorylation of P38 mitogen-activated protein kinase .

## Item biored:test:903
Example input:
Sentence: Consistent with impaired growth , PKCalpha knockdown increased levels of the cyclin-dependent kinase ( CDK ) inhibitors p21 ( Cip1/WAF1 ) ( p21 ) and p27 ( Kip1 ) ( p27 ) .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "cyclin-dependent kinase", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "Cip1/WAF1", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Kip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: NDP-MSH augmented insulin-stimulated AKT phosphorylation in vitro .

Example answer:
{"entities": [{"text": "NDP-MSH", "type": "ChemicalEntity"}, {"text": "insulin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Alteration of NEK2 protein levels may contribute to invasion and metastasis of HCC , which may occur through activation of AKT signaling and promotion of MMP-2 expression .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "metastasis of HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AKT", "type": "GeneOrGeneProduct"}, {"text": "MMP-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Despite the absence of functional phosphatase and tensin homolog ( PTEN ) protein in Ishikawa cells , PKCalpha knockdown reduced Akt phosphorylation at serine 473 and concomitantly inhibited phosphorylation of the Akt target , glycogen synthase kinase-3beta ( GSK-3beta ) .

Example answer:
{"entities": [{"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "glycogen synthase kinase-3beta", "type": "GeneOrGeneProduct"}, {"text": "GSK-3beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , PI3K/Akt pathway signaling was also increased in Eu-myc B cells , and this increase was partially suppressed with ibrutinib .

Example answer:
{"entities": [{"text": "PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "ibrutinib", "type": "ChemicalEntity"}]}

Example input:
Sentence: The expression of NEK2 , phospho-AKT and MMP-2 was evaluated by immunohistochemistry in 63 cases of HCC and matched adjacent non-tumorous liver tissues .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "MMP-2", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Investigations of the underlying mechanisms revealed that BDNF activated Akt and preserved phosphorylation of mammalian target of rapamycin and Bad without affecting p38 mitogen-activated protein kinase and extracellular regulated protein kinase pathways .

Example answer:
{"entities": [{"text": "mammalian target of", "type": "GeneOrGeneProduct"}, {"text": "p38 mitogen-activated protein", "type": "GeneOrGeneProduct"}, {"text": "extracellular regulated protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: NEK2 expression was positively correlated with the expression of phospho-AKT ( r=0.883 , P < 0.01 ) and MMP-2 ( r=0.781 , P < 0.01 ) .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "MMP-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We recently reported that phosphoinositide 3-kinase ( PI3K ) /protein kinase B ( Akt ) mediates transcriptional regulation and activation of bone morphogenetic protein ( BMP ) -2 signaling by nuclear factor ( NF ) -kappaB in bone metastatic prostate cancer cells .

Example answer:
{"entities": [{"text": "phosphoinositide 3-kinase ( PI3K ) /protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "bone morphogenetic protein ( BMP ) -2", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor ( NF ) -kappaB", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Our data also indicated that NSP has little influence on the MAPK and PI3K/Akt pathways .

## Item biored:test:883
Example input:
Sentence: PRMT5 regulated the production of inflammatory factors , cell proliferation , migration and invasion of RA FLS , which was mediated by the NF-kB and AKT pathways .

Example answer:
{"entities": [{"text": "PRMT5", "type": "GeneOrGeneProduct"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kB", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Rab6c was found to be under-expressed in MCF7/AdrR and MES-SA/Dx5 ( a human MDR uterine sarcoma cell line ) compared with their non-MDR parental cell lines .

Example answer:
{"entities": [{"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "MES-SA/Dx5", "type": "CellLine"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "uterine sarcoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Viruses were evaluated for replication in SCID mice transplanted with human hepatoma cells ( SCID-HuH-7 mice ) , in mosquitoes , and in rhesus monkeys .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "hepatoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCID-HuH-7", "type": "CellLine"}, {"text": "rhesus monkeys", "type": "OrganismTaxon"}]}

Example input:
Sentence: In RA FLSs , the level of PRMT5 was up-regulated by stimulation with IL-1b and TNF-a .

Example answer:
{"entities": [{"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PRMT5", "type": "GeneOrGeneProduct"}, {"text": "IL-1b", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TSPO was up-regulated in Iba1 ( + ) cells from brains of patients with ICH and in CD11b ( + ) CD45 ( int ) cells from mice subjected to collagenase-induced ICH .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "Iba1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD11b", "type": "GeneOrGeneProduct"}, {"text": "CD45", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "collagenase-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The binding of mTOR , PRAS40 and RagC to raptor did not differ for control and septic muscle in the basal condition ; however , the Leu-induced decrease in PRAS40 raptor and increase in RagC raptor seen in control muscle was absent in sepsis .

Example answer:
{"entities": [{"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "PRAS40", "type": "GeneOrGeneProduct"}, {"text": "RagC", "type": "GeneOrGeneProduct"}, {"text": "raptor", "type": "GeneOrGeneProduct"}, {"text": "Leu-induced", "type": "ChemicalEntity"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A mouse inflammatory cytokine and receptor RT2 profiler array was used to determine regulated transcripts in the urinary bladder of wild type ( WT ) and VIP ( -/- ) mice with or without CYP-induced cystitis ( 150 mg/kg ; i.p .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CYP-induced", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: To identify the regulation of RSV inducible cytokines , Mavs and Trif deficient animals were infected with RSV .

## Item biored:test:888
Example input:
Sentence: Immunohistochemistry and western blotting are used to determine the mechanisms of Sal against RIF .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "RIF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Promoter insertion/deletion in the IRF5 gene is highly associated with susceptibility to systemic lupus erythematosus in distinct populations , but exerts a modest effect on gene expression in peripheral blood mononuclear cells .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In vivo , PGA2 was protective in two distinct models of acute lung injury ( ALI ) : LPS-induced inflammatory injury and two-hit ALI caused by suboptimal mechanical ventilation and injection of thrombin receptor-activating peptide .

Example answer:
{"entities": [{"text": "PGA2", "type": "ChemicalEntity"}, {"text": "acute lung injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LPS-induced", "type": "ChemicalEntity"}, {"text": "inflammatory injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thrombin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Tissue-Specific Ablation of the LIF Receptor in the Murine Uterine Epithelium Results in Implantation Failure .

Example answer:
{"entities": [{"text": "LIF Receptor", "type": "GeneOrGeneProduct"}, {"text": "Murine", "type": "OrganismTaxon"}]}

Example input:
Sentence: The cytokine leukemia inhibitory factor ( LIF ) is essential for rendering the uterus receptive for blastocyst implantation .

Example answer:
{"entities": [{"text": "leukemia inhibitory factor", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: LIF , secreted from the endometrial glands ( GEs ) , binds to the LIFR , activating the Janus kinase-signal transducer and activation of transcription ( STAT ) 3 ( Jak-Stat3 ) signaling pathway in the LE .

Example answer:
{"entities": [{"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "LIFR", "type": "GeneOrGeneProduct"}, {"text": "Janus", "type": "GeneOrGeneProduct"}, {"text": "transducer and activation of transcription ( STAT ) 3", "type": "GeneOrGeneProduct"}, {"text": "Jak-Stat3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In mice , LIF receptor expression ( LIFR ) is largely restricted to the uterine luminal epithelium ( LE ) .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "LIF receptor", "type": "GeneOrGeneProduct"}, {"text": "LIFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The loss of Lifr results in both the failure for STAT3 to translocate to the LE nuclei and a reduction in the expression of the LIF regulated gene Msx1 that regulates uterine receptivity .

Example answer:
{"entities": [{"text": "Lifr", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "Msx1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Expression of LIF protects the lung from lung injury and enhanced pathology during RSV infection .

## Item biored:test:894
Example input:
Sentence: In the present study , we demonstrate that NF-kappaB , whether activated by recombinant human tumor necrosis factor ( TNF ) -alpha or by ectopic expression of the p65 subunit , is involved in extracellular matrix adhesion and invasion of osteotropic PC-3 and C4-2B , but not LNCaP , cells .

Example answer:
{"entities": [{"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tumor necrosis factor ( TNF ) -alpha", "type": "GeneOrGeneProduct"}, {"text": "p65", "type": "GeneOrGeneProduct"}, {"text": "PC-3", "type": "CellLine"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "LNCaP", "type": "CellLine"}]}

Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cocaine", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}, {"text": "nNOS", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Nuclear factor kappa B ( NFkappaB ) is a sensor of oxidative stress and participates in memory formation that could be involved in drug toxicity and addiction mechanisms .

Example answer:
{"entities": [{"text": "Nuclear factor kappa B", "type": "GeneOrGeneProduct"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Nitric oxide ( NO ) , gaseous neurotransmitter , has contradictor role in epileptogenesis due to opposite effects of L-arginine , precursor of NO syntheses ( NOS ) , and L-NAME ( NOS inhibitor ) observed in different epilepsy models .

Example answer:
{"entities": [{"text": "Nitric oxide", "type": "ChemicalEntity"}, {"text": "NO", "type": "ChemicalEntity"}, {"text": "L-arginine", "type": "ChemicalEntity"}, {"text": "NO syntheses", "type": "GeneOrGeneProduct"}, {"text": "NOS", "type": "GeneOrGeneProduct"}, {"text": "L-NAME", "type": "ChemicalEntity"}, {"text": "epilepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Therefore NFkappaB activity , oxidative stress , neuronal nitric oxide synthase ( nNOS ) activity , spatial learning and memory as well as the effect of topiramate , a previously proposed therapy for cocaine addiction , were evaluated in an experimental model of cocaine administration in rats .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "neuronal nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nNOS", "type": "GeneOrGeneProduct"}, {"text": "topiramate", "type": "ChemicalEntity"}, {"text": "cocaine addiction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cocaine", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: FASN activity was measured by monitoring oxidation of nicotinamide adenine dinucleotide phosphate at a wavelength of 340 nm , and intracellular free fatty acid levels were detected using a Free Fatty Acid Quantification kit .

Example answer:
{"entities": [{"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "nicotinamide adenine dinucleotide phosphate", "type": "ChemicalEntity"}, {"text": "free fatty acid", "type": "ChemicalEntity"}, {"text": "Free Fatty Acid", "type": "ChemicalEntity"}]}

Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Semiquantitative assessment of the density of NOX4 colabeling with lectin-stained retinal ECs was determined by immunolabeling of retinal cryosections from P18 pups in OIR or in RA .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "lectin-stained", "type": "GeneOrGeneProduct"}, {"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Tat also induced the synthesis and release of TNFa and IL-6 protein in the supernatant of the slices and increased expression of the inducible isoform of nitric oxide synthase ( iNOS ) and the serotonin transporter ( SERT ) .

Example answer:
{"entities": [{"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "TNFa", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "inducible isoform of nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "SERT", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: To explore the potential mechanisms of NSP , the release of nitric oxide ( NO ) and TNF-alpha related to NSP administration were measured by enzyme-linked immunosorbent assay .

## Item biored:test:855
Example input:
Sentence: Mechanistic studies revealed that OB rats are sensitized due to : ( 1 ) higher oxyradical stress leading to upregulation of uncoupling proteins 2 and 3 , ( 2 ) downregulation of cardiac peroxisome proliferators activated receptor-alpha , ( 3 ) decreased plasma adiponectin levels , ( 4 ) decreased cardiac fatty-acid oxidation ( 666.9+/-14.0 nmol/min/g heart in ND versus 400.2+/-11.8 nmol/min/g heart in OB ) , ( 5 ) decreased mitochondrial AMP-alpha2 protein kinase , and ( 6 ) 86 % drop in cardiac ATP levels accompanied by decreased ATP/ADP ratio after doxorubicin administration .

Example answer:
{"entities": [{"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "uncoupling proteins 2 and 3", "type": "GeneOrGeneProduct"}, {"text": "peroxisome proliferators activated receptor-alpha", "type": "GeneOrGeneProduct"}, {"text": "adiponectin", "type": "GeneOrGeneProduct"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "AMP-alpha2 protein kinase", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "ATP/ADP", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "aspartate transaminase", "type": "GeneOrGeneProduct"}, {"text": "creatine kinase", "type": "GeneOrGeneProduct"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "catalase", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This study was designed to evaluate the alterations in offspring rat cerebellum induced by maternal exposure to carmustine- [ 1,3-bis ( 2-chloroethyl ) -1-nitrosoure ] ( BCNU ) and to investigate the effects of exogenous melatonin upon cerebellar BCNU-induced cortical dysplasia , using histological and biochemical analyses .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "carmustine-", "type": "ChemicalEntity"}, {"text": "1,3-bis ( 2-chloroethyl ) -1-nitrosoure", "type": "ChemicalEntity"}, {"text": "BCNU", "type": "ChemicalEntity"}, {"text": "melatonin", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "cortical dysplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The heart tissue antioxidant enzymes such as superoxide dismutase , catalase , glutathione peroxidase , glutathione transferase and glutathione reductase activities , non-enzymic antioxidants such as cerruloplasmin , Vitamin C , Vitamin E and glutathione levels were altered in MI rats .

Example answer:
{"entities": [{"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "catalase", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}, {"text": "glutathione transferase", "type": "GeneOrGeneProduct"}, {"text": "glutathione reductase", "type": "GeneOrGeneProduct"}, {"text": "cerruloplasmin", "type": "GeneOrGeneProduct"}, {"text": "Vitamin C", "type": "ChemicalEntity"}, {"text": "Vitamin E", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: These data suggest that pilocarpine produced antiarrhythmic actions on arrhythmic rat and guinea pig models induced by aconitine or ouabain via stimulating the cardiac M ( 3 ) -mAChR .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "M ( 3 ) -mAChR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Subcutaneous injection of ISPH ( 200 mg/kg body weight in 1 ml saline ) to rats for 2 consecutive days caused myocardial damage in rat heart , which was determined by the increased activity of serum lactate dehydrogenase ( LDH ) and creatine phosphokinase isoenzymes ( CK-MB ) , increased uric acid level and reduced plasma iron binding capacity .

Example answer:
{"entities": [{"text": "ISPH", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "LDH", "type": "GeneOrGeneProduct"}, {"text": "creatine phosphokinase isoenzymes", "type": "GeneOrGeneProduct"}, {"text": "CK-MB", "type": "GeneOrGeneProduct"}, {"text": "uric acid", "type": "ChemicalEntity"}, {"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: [ Ca ( 2+ ) ] ( i ) overload induced by aconitine or ouabain was reduced in isolated myocytes pretreated with pilocarpine .

Example answer:
{"entities": [{"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: This study was designed to evaluate the effects of pilocarpine and explore the underlying ionic mechanism , using both aconitine-induced rat and ouabain-induced guinea pig arrhythmia models .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "aconitine-induced", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "ouabain-induced", "type": "ChemicalEntity"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: To investigate effects of aconitine on myocardial injury , we performed cytotoxicity assay in neonatal rat ventricular myocytes ( NRVMs ) , as well as measured lactate dehydrogenase level in the culture medium of NRVMs and activities of serum cardiac enzymes in rats .

## Item biored:test:865
Example input:
Sentence: CYP treatment significantly ( p < or = 0.001 ) increased expression of CXCL1 and IL-1beta in the urinary bladder of WT and VIP ( -/- ) mice , but expression in VIP ( -/- ) mice with CYP treatment was significantly ( p < or = 0.001 ) greater ( 4.2- to 13-fold increase ) than that observed in WT urinary bladder ( 3.6- to 5-fold increase ) .

Example answer:
{"entities": []}

Example input:
Sentence: This shift in balance may contribute to increased bladder dysfunction in VIP ( -/- ) mice with bladder inflammation and altered neurochemical expression in micturition pathways .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice lacking mPGES-1 are resistant to lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 2-wk administration of LiCl ( 4 mmol.kg ( -1 ) .day ( -1 ) ip ) in mPGES-1 +/+ mice led to a marked polyuria with hyposmotic urine .

Example answer:
{"entities": [{"text": "LiCl", "type": "ChemicalEntity"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conclude that mPGES-1-derived PGE ( 2 ) mediates lithium-induced polyuria likely via inhibition of AQP2 and NKCC2 expression .

Example answer:
{"entities": [{"text": "mPGES-1-derived", "type": "GeneOrGeneProduct"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cyclooxygenase-2 activity is required for the development of lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Cyclooxygenase-2", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In contrast , mPGES-1 -/- mice were largely resistant to lithium-induced polyuria and a urine concentrating defect , accompanied by nearly complete blockade of high urine PGE ( 2 ) and cAMP output .

Example answer:
{"entities": [{"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "cAMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: The decreased capacity to concentrate urine is likely due to lithium acutely disrupting the cAMP pathway and chronically reducing urea transporter ( UT-A1 ) and water channel ( AQP2 ) expression in the inner medulla .

## Item biored:test:917
Example input:
Sentence: RESULTS : KCa3.1 expression was markedly associated with endoplasmic reticulum ( ER ) stress and unfolded protein response ( UPR ) in both Abeta-stimulated primary astrocytes and brain lysates of AD patients and APP/PS1 AD mice .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Abeta-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: In addition to contributing to proteome plasticity , alternative splicing at a NAGNAG tandem site can thus remove a disease-causing UAG stop codon .

Example answer:
{"entities": []}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Together , these findings imply that OCT4A induction following DNA damage in PA-1 cells , performs a cell stress , rather than self-renewal , function by moderating the expression of p21Cip1 , which alongside AMPK helps to then regulate autophagy .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: Attenuated expression of LDHA by siRNA or inhibition of LDHA activities by FX11 inhibited cell proliferation , migration , invasion , and promoted cell apoptosis of PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: In IEC-6 crypt cells and jejunum enteroids quantitative RT-PCR showed a time- and dose-dependent upregulation of lpa2 in response to gamma-irradiation that was abolished by mutation of the NF-kappaB site in the lpa2 promoter or by inhibition of ATM/ATR kinases with CGK-733 , suggesting that lpa2 is a DNA damage response gene upregulated by ATM via NF-kappaB .

Example answer:
{"entities": [{"text": "IEC-6", "type": "CellLine"}, {"text": "lpa2", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "ATM/ATR kinases", "type": "GeneOrGeneProduct"}, {"text": "CGK-733", "type": "ChemicalEntity"}, {"text": "ATM", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RNA sequencing was performed to identify global gene expression changes after ADAM12 knockdown .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The single base pair guanine insertion/deletion polymorphism ( 4G/5G ) within the promoter region of the PAI-1 gene influences PAI-1 synthesis and may modulate hepatic fibrogenesis .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "hepatic fibrogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The impact of PPARa activation on whole genome gene expression in human precision cut liver slices .

## Item biored:test:904
Example input:
Sentence: Here , we show that simultaneous overexpression of the mitotic checkpoint protein Mad2 with Kras ( G12D ) or Her2 in mammary glands of adult mice results in mitotic checkpoint overactivation and a delay in tumor onset .

Example answer:
{"entities": [{"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "GeneOrGeneProduct"}, {"text": "Her2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Whole-Organism Developmental Expression Profiling Identifies RAB-28 as a Novel Ciliary GTPase Associated with the BBSome and Intraflagellar Transport .

Example answer:
{"entities": [{"text": "RAB-28", "type": "GeneOrGeneProduct"}, {"text": "GTPase", "type": "GeneOrGeneProduct"}, {"text": "BBSome", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Inability to identify a separate zebrafish gene corresponding to the mammalian CHL1 gene suggests that Chl may serve roles in zebrafish distributed between CHL1 and CHL2 in other species .

Example answer:
{"entities": [{"text": "zebrafish", "type": "OrganismTaxon"}, {"text": "CHL1", "type": "GeneOrGeneProduct"}, {"text": "Chl", "type": "GeneOrGeneProduct"}, {"text": "CHL2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A combination of fluorescence in situ hybridization ( FISH ) and Southern blot analysis demonstrated disruption of a synaptotagmin gene ( SYT14 ) at the 1q32 breakpoint .

Example answer:
{"entities": [{"text": "synaptotagmin", "type": "GeneOrGeneProduct"}, {"text": "SYT14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Zebrafish chordin-like and chordin are functionally redundant in regulating patterning of the dorsoventral axis .

Example answer:
{"entities": [{"text": "Zebrafish", "type": "OrganismTaxon"}, {"text": "chordin-like", "type": "GeneOrGeneProduct"}, {"text": "chordin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The expression of bone morphogenetic protein ( Bmp ) genes , such as Bmp4 and Bmp7 , was also ectopically induced in the epithelia of the URS in the b-catenin GOF mutants .

Example answer:
{"entities": [{"text": "bone morphogenetic protein", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}, {"text": "Bmp4", "type": "GeneOrGeneProduct"}, {"text": "Bmp7", "type": "GeneOrGeneProduct"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recent studies indicate that genetic ablation of mouse uroplakin ( UP ) III gene , which encodes a 47 kD urothelial-specific integral membrane protein forming urothelial plaques , causes VUR and hydronephrosis .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "uroplakin ( UP ) III", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further analyses of C. elegans RAB-28 , recently associated with autosomal-recessive cone-rod dystrophy , reveal that this small GTPase is exclusively expressed in ciliated neurons where it dynamically associates with IFT trains .

Example answer:
{"entities": [{"text": "C. elegans", "type": "OrganismTaxon"}, {"text": "RAB-28", "type": "GeneOrGeneProduct"}, {"text": "cone-rod dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GTPase", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Protein-Trap Insertional Mutagenesis Uncovers New Genes Involved in Zebrafish Skin Development , Including a Neuregulin 2a-Based ErbB Signaling Pathway Required during Median Fin Fold Morphogenesis .

## Item biored:test:907
Example input:
Sentence: Further analyses of C. elegans RAB-28 , recently associated with autosomal-recessive cone-rod dystrophy , reveal that this small GTPase is exclusively expressed in ciliated neurons where it dynamically associates with IFT trains .

Example answer:
{"entities": [{"text": "C. elegans", "type": "OrganismTaxon"}, {"text": "RAB-28", "type": "GeneOrGeneProduct"}, {"text": "cone-rod dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GTPase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Functional analyses reveal that whilst cilium structure , sensory function and IFT are seemingly normal in a rab-28 null allele , overexpression of predicted GDP or GTP locked variants of RAB-28 perturbs cilium and sensory pore morphogenesis and function .

Example answer:
{"entities": [{"text": "rab-28", "type": "GeneOrGeneProduct"}, {"text": "GDP", "type": "ChemicalEntity"}, {"text": "GTP", "type": "ChemicalEntity"}, {"text": "RAB-28", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To identify new cilium-associated genes , we employed the nematode C. elegans , where ciliogenesis occurs within a short timespan during late embryogenesis when most sensory neurons differentiate .

Example answer:
{"entities": [{"text": "C. elegans", "type": "OrganismTaxon"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DOCK8 was expressed in a variety of human organs , including the lungs , and was also expressed in type II alveolar , bronchiolar epithelial and bronchial epithelial cells , which are considered as being progenitors for lung cancer cells .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A combination of fluorescence in situ hybridization ( FISH ) and Southern blot analysis demonstrated disruption of a synaptotagmin gene ( SYT14 ) at the 1q32 breakpoint .

Example answer:
{"entities": [{"text": "synaptotagmin", "type": "GeneOrGeneProduct"}, {"text": "SYT14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Whole-Organism Developmental Expression Profiling Identifies RAB-28 as a Novel Ciliary GTPase Associated with the BBSome and Intraflagellar Transport .

Example answer:
{"entities": [{"text": "RAB-28", "type": "GeneOrGeneProduct"}, {"text": "GTPase", "type": "GeneOrGeneProduct"}, {"text": "BBSome", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Zebrafish chordin-like and chordin are functionally redundant in regulating patterning of the dorsoventral axis .

Example answer:
{"entities": [{"text": "Zebrafish", "type": "OrganismTaxon"}, {"text": "chordin-like", "type": "GeneOrGeneProduct"}, {"text": "chordin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Inability to identify a separate zebrafish gene corresponding to the mammalian CHL1 gene suggests that Chl may serve roles in zebrafish distributed between CHL1 and CHL2 in other species .

Example answer:
{"entities": [{"text": "zebrafish", "type": "OrganismTaxon"}, {"text": "CHL1", "type": "GeneOrGeneProduct"}, {"text": "Chl", "type": "GeneOrGeneProduct"}, {"text": "CHL2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here we identify and characterize zebrafish , Danio rerio , CHL ( Chl ) .

Example answer:
{"entities": [{"text": "zebrafish", "type": "OrganismTaxon"}, {"text": "Danio rerio", "type": "OrganismTaxon"}, {"text": "CHL", "type": "GeneOrGeneProduct"}, {"text": "Chl", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Here we report the Zebrafish Integument Project ( ZIP ) , an expression-driven platform for identifying new skin genes and phenotypes in the vertebrate model Danio rerio ( zebrafish ) .

## Item biored:test:919
Example input:
Sentence: Chronic inflammation enhances gankyrin expression in the human liver .

Example answer:
{"entities": [{"text": "Chronic inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gankyrin", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: No association was found between PAI-1 serum levels or 4G/5G genotype with liver fibrosis in obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: No differences were observed in PAI-1 plasma levels among obese patients with liver fibrosis ( 10.64 4.35 ) compared to patients without liver fibrosis ( 10.61 5.2 ; p = 0.985 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "ChemicalEntity"}, {"text": "escitalopram", "type": "ChemicalEntity"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PCPA significantly and substantially depleted 5-HT and 5-HIAA in all brain regions examined .

Example answer:
{"entities": [{"text": "PCPA", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "5-HIAA", "type": "ChemicalEntity"}]}

Example input:
Sentence: This study was designed to evaluate the role of angiotensin II subtype receptor 1a ( AT1a ) in the formation of liver metastasis in CRC .

Example answer:
{"entities": [{"text": "angiotensin II subtype receptor 1a", "type": "GeneOrGeneProduct"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The liver levels of beta-oxidation metabolites of VPA were decreased by day 14 , while the levels of 4-ene-VPA and ( E ) -2,4-diene-VPA were not elevated throughout the study .

Example answer:
{"entities": [{"text": "VPA", "type": "ChemicalEntity"}, {"text": "4-ene-VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: To determine whether there was a temporal relationship between VPA-associated oxidative stress and hepatotoxicity , adult male Sprague-Dawley rats were treated ip with VPA ( 500 mg/kg ) or 0.9 % saline ( vehicle ) once daily for 2 , 4 , 7 , 10 , or 14 days .

Example answer:
{"entities": [{"text": "VPA-associated", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Input:
Sentence: However , much less is known about the role of PPARa in human liver .

## Item biored:test:872
Example input:
Sentence: also significantly augmented hippocampal LTP in saline-treated ( 1ml/kg , s.c. ) rats .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: We conclude that mPGES-1-derived PGE ( 2 ) mediates lithium-induced polyuria likely via inhibition of AQP2 and NKCC2 expression .

Example answer:
{"entities": [{"text": "mPGES-1-derived", "type": "GeneOrGeneProduct"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cyclooxygenase-2 activity is required for the development of lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Cyclooxygenase-2", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CYP treatment significantly ( p < or = 0.001 ) increased expression of CXCL1 and IL-1beta in the urinary bladder of WT and VIP ( -/- ) mice , but expression in VIP ( -/- ) mice with CYP treatment was significantly ( p < or = 0.001 ) greater ( 4.2- to 13-fold increase ) than that observed in WT urinary bladder ( 3.6- to 5-fold increase ) .

Example answer:
{"entities": []}

Example input:
Sentence: Mice lacking mPGES-1 are resistant to lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 2-wk administration of LiCl ( 4 mmol.kg ( -1 ) .day ( -1 ) ip ) in mPGES-1 +/+ mice led to a marked polyuria with hyposmotic urine .

Example answer:
{"entities": [{"text": "LiCl", "type": "ChemicalEntity"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Example input:
Sentence: In contrast , mPGES-1 -/- mice were largely resistant to lithium-induced polyuria and a urine concentrating defect , accompanied by nearly complete blockade of high urine PGE ( 2 ) and cAMP output .

Example answer:
{"entities": [{"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "cAMP", "type": "ChemicalEntity"}]}

Input:
Sentence: Lithium-treated WT mice had 19-fold increased urine output whereas treated PKCa KO animals had a 4-fold increase in output .

## Item biored:test:895
Example input:
Sentence: STUDY DESIGN : Wild-type ( WT ) and superoxide dismutase 1 ( SOD1 ) -overexpressing day 8.75 embryos from nondiabetic WT control with SOD1 transgenic male and diabetic WT female with SOD1 transgenic male were analyzed for ER stress markers : C/EBP-homologous protein ( CHOP ) , calnexin , eukaryotic initiation factor 2a ( eIF2a ) , protein kinase ribonucleic acid ( RNA ) -like ER kinase ( PERK ) , binding immunoglobulin protein , protein disulfide isomerase family A member 3 , kinases inositol-requiring protein-1a ( IRE1a ) , and the X-box binding protein ( XBP1 ) messenger RNA ( mRNA ) splicing .

Example answer:
{"entities": [{"text": "superoxide dismutase 1", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "C/EBP-homologous protein", "type": "GeneOrGeneProduct"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "eukaryotic initiation factor 2a", "type": "GeneOrGeneProduct"}, {"text": "eIF2a", "type": "GeneOrGeneProduct"}, {"text": "protein kinase ribonucleic acid ( RNA ) -like ER kinase", "type": "GeneOrGeneProduct"}, {"text": "PERK", "type": "GeneOrGeneProduct"}, {"text": "binding immunoglobulin protein", "type": "GeneOrGeneProduct"}, {"text": "protein disulfide isomerase family A member 3", "type": "GeneOrGeneProduct"}, {"text": "kinases inositol-requiring protein-1a", "type": "GeneOrGeneProduct"}, {"text": "IRE1a", "type": "GeneOrGeneProduct"}, {"text": "X-box binding protein", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemistry and western blotting are used to determine the mechanisms of Sal against RIF .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "RIF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A potential downstream signaling pathway involving phosphatidylinositol 3-kinase ( PI3K ) /threonine protein kinase B ( Akt ) /mammalian target of rapamycin ( mTOR ) was identifiedby western blot analysis .

Example answer:
{"entities": [{"text": "phosphatidylinositol 3-kinase", "type": "GeneOrGeneProduct"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "target of rapamycin", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We recently reported that phosphoinositide 3-kinase ( PI3K ) /protein kinase B ( Akt ) mediates transcriptional regulation and activation of bone morphogenetic protein ( BMP ) -2 signaling by nuclear factor ( NF ) -kappaB in bone metastatic prostate cancer cells .

Example answer:
{"entities": [{"text": "phosphoinositide 3-kinase ( PI3K ) /protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "bone morphogenetic protein ( BMP ) -2", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor ( NF ) -kappaB", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The 293T cells transfected with the full-coding cDNA inserted in the expression vector produced a new 80 kDa protein , as detected by Western blot .

Example answer:
{"entities": [{"text": "293T", "type": "CellLine"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover mRNA levels of LDLr and ERK1/2 as well as protein levels of total and activated forms of ERK1/2 in rat liver were evaluated by Western blotting and quantitative real time polymerase chain reaction analysis .

Example answer:
{"entities": [{"text": "LDLr", "type": "GeneOrGeneProduct"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: Western blot analysis and reverse transcription-polymerase chain reaction were used to detect target gene and protein expression .

Example answer:
{"entities": []}

Example input:
Sentence: p38 MAPK phosphorylation was analyzed by western blot .

Example answer:
{"entities": [{"text": "p38 MAPK", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The proteins related to the NF-kappaB , ERK1/2 , and PI3K/Akt pathways were investigated by Western blotting .

## Item biored:test:864
Example input:
Sentence: Nimodipine prevents memory impairment caused by nitroglycerin-induced hypotension in adult mice .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nitroglycerin-induced", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Patients taking clozapine and olanzapine must be examined for insulin resistance and its consequences .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice lacking mPGES-1 are resistant to lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In contrast , mPGES-1 -/- mice were largely resistant to lithium-induced polyuria and a urine concentrating defect , accompanied by nearly complete blockade of high urine PGE ( 2 ) and cAMP output .

Example answer:
{"entities": [{"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "cAMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Example input:
Sentence: We conclude that mPGES-1-derived PGE ( 2 ) mediates lithium-induced polyuria likely via inhibition of AQP2 and NKCC2 expression .

Example answer:
{"entities": [{"text": "mPGES-1-derived", "type": "GeneOrGeneProduct"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : While the incidence of new-onset diabetes mellitus may be increasing in patients with schizophrenia treated with certain atypical antipsychotic agents , it remains unclear whether atypical agents are directly affecting glucose metabolism or simply increasing known risk factors for diabetes .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antipsychotic agents", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Cyclooxygenase-2 activity is required for the development of lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Cyclooxygenase-2", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Lithium , an effective antipsychotic , induces nephrogenic diabetes insipidus ( NDI ) in 40 % of patients .

## Item biored:test:915
Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: EP4 mediated barrier-protective effects of PGA2 by activating Rap1/Rac1 GTPase and protein kinase A targets at cell adhesions and cytoskeleton : VE-cadherin , p120-catenin , ZO-1 , cortactin , and VASP .

Example answer:
{"entities": [{"text": "EP4", "type": "GeneOrGeneProduct"}, {"text": "PGA2", "type": "ChemicalEntity"}, {"text": "Rap1/Rac1 GTPase", "type": "GeneOrGeneProduct"}, {"text": "protein kinase A", "type": "GeneOrGeneProduct"}, {"text": "VE-cadherin", "type": "GeneOrGeneProduct"}, {"text": "p120-catenin", "type": "GeneOrGeneProduct"}, {"text": "ZO-1", "type": "GeneOrGeneProduct"}, {"text": "cortactin", "type": "GeneOrGeneProduct"}, {"text": "VASP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both baseline and NRG-1 beta-induced migration were erbB-dependent and required the action of MEK 1/2 , SAPK/JNK , PI-3 kinase , Src family kinases and ROCK-I/II .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB-dependent", "type": "GeneOrGeneProduct"}, {"text": "MEK 1/2", "type": "GeneOrGeneProduct"}, {"text": "SAPK/JNK", "type": "GeneOrGeneProduct"}, {"text": "PI-3 kinase", "type": "GeneOrGeneProduct"}, {"text": "Src family kinases", "type": "GeneOrGeneProduct"}, {"text": "ROCK-I/II", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hypothesizing that NRG-1 beta and/or NRG-1 alpha promote MPNST invasion , we found that NRG-1 beta promoted MPNST migration in a substrate-specific manner , markedly enhancing migration on laminin but not on collagen type I or fibronectin .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "laminin", "type": "GeneOrGeneProduct"}, {"text": "collagen type I", "type": "GeneOrGeneProduct"}, {"text": "fibronectin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Re-expression of LKB1 or knockdown of VEGF receptor 2 decreased the overproliferation and -migration observed in LKB1 ( endo-/- ) cells .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We have shown that MPNSTs express neuregulin-1 ( NRG-1 ) beta isoforms , which promote Schwann cell migration during development , and NRG-1 alpha isoforms , whose effects on Schwann cells are poorly understood .

Example answer:
{"entities": [{"text": "MPNSTs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuregulin-1 ( NRG-1 ) beta", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PGA2 also suppressed LPS-induced inflammatory signaling by inhibiting the NFkB pathway and expression of EC adhesion molecules ICAM1 and VCAM1 .

Example answer:
{"entities": [{"text": "PGA2", "type": "ChemicalEntity"}, {"text": "LPS-induced", "type": "ChemicalEntity"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkB", "type": "GeneOrGeneProduct"}, {"text": "EC adhesion molecules", "type": "GeneOrGeneProduct"}, {"text": "ICAM1", "type": "GeneOrGeneProduct"}, {"text": "VCAM1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In IEC-6 crypt cells and jejunum enteroids quantitative RT-PCR showed a time- and dose-dependent upregulation of lpa2 in response to gamma-irradiation that was abolished by mutation of the NF-kappaB site in the lpa2 promoter or by inhibition of ATM/ATR kinases with CGK-733 , suggesting that lpa2 is a DNA damage response gene upregulated by ATM via NF-kappaB .

Example answer:
{"entities": [{"text": "IEC-6", "type": "CellLine"}, {"text": "lpa2", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "ATM/ATR kinases", "type": "GeneOrGeneProduct"}, {"text": "CGK-733", "type": "ChemicalEntity"}, {"text": "ATM", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The NRG-1 receptors erbB3 and erbB4 were present in MPNST invadopodia ( processes mediating invasion ) , partially colocalized with focal adhesion kinase and the laminin receptor beta ( 1 ) -integrin and coimmunoprecipitated with beta ( 1 ) -integrin .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB3", "type": "GeneOrGeneProduct"}, {"text": "erbB4", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal adhesion kinase", "type": "GeneOrGeneProduct"}, {"text": "laminin receptor", "type": "GeneOrGeneProduct"}, {"text": "beta ( 1 ) -integrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Identifying Lgl2 as an antagonist of Nrg2a-ErbB signaling revealed a significantly earlier role for Lgl2 during epidermal morphogenesis than has been described to date .

## Item biored:test:840
Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We suggest that trazodone ( 5 , 10 and 20 mg/kg ) , by blocking the 5-HT 2C receptors , releases the nigrostriatal DAergic neurons from tonic inhibition caused by 5-HT , and thereby potentiates dexamphetamine stereotypy and antagonizes haloperidol catalepsy .

Example answer:
{"entities": [{"text": "5-HT 2C", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: induced catalepsy and antagonized apomorphine and dexamphetamine stereotypies .

Example answer:
{"entities": []}

Example input:
Sentence: Haloperidol-induced catalepsy was challenged with prior intracollicular microinjections of glutamate NMDA receptor antagonists , MK-801 ( 15 or 30 mmol/0.5 microl ) and AP7 ( 10 or 20 nmol/0.5 microl ) , or of the NMDA receptor agonist N-methyl-d-aspartate ( NMDA , 20 or 30 nmol/0.5 microl ) .

Example answer:
{"entities": [{"text": "Haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutamate NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-d-aspartate", "type": "ChemicalEntity"}, {"text": "NMDA", "type": "ChemicalEntity"}]}

Example input:
Sentence: These findings suggest that glutamate-mediated mechanisms in the neural circuits at the IC level influence haloperidol-induced catalepsy and participate in the regulation of motor activity .

Example answer:
{"entities": [{"text": "glutamate-mediated", "type": "ChemicalEntity"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Compound 1 is a potent A ( 2A ) /A ( 1 ) receptor antagonist in vitro ( A ( 2A ) K ( i ) = 4.1 nM ; A ( 1 ) K ( i ) = 17.0 nM ) that has excellent activity , after oral administration , across a number of animal models of Parkinson 's disease including mouse and rat models of haloperidol-induced catalepsy , mouse model of reserpine-induced akinesia , rat 6-hydroxydopamine ( 6-OHDA ) lesion model of drug-induced rotation , and MPTP-treated non-human primate model .

Example answer:
{"entities": [{"text": "A ( 2A ) /A ( 1 ) receptor antagonist", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "reserpine-induced", "type": "ChemicalEntity"}, {"text": "akinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "6-hydroxydopamine", "type": "ChemicalEntity"}, {"text": "6-OHDA", "type": "ChemicalEntity"}, {"text": "MPTP-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : The effect of pretreatment with trazodone on dexamphetamine- and apomorphine-induced oral stereotypies , on catalepsy induced by haloperidol and apomorphine ( 0.05 mg/kg , i.p .

Example answer:
{"entities": [{"text": "trazodone", "type": "ChemicalEntity"}, {"text": "dexamphetamine-", "type": "ChemicalEntity"}, {"text": "apomorphine-induced", "type": "ChemicalEntity"}, {"text": "oral stereotypies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "apomorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: did not induce catalepsy , and did not antagonize apomorphine ( 1.5 and 3 mg/kg ) stereotypy and apomorphine ( 0.05 mg/kg ) -induced catalepsy .

Example answer:
{"entities": []}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: Amphetamine ( 3 mg/kg ip ) induced hyper locomotion , apomorphine ( 1.5 mg/kg subcutaneously [ sc ] ) induced climbing , and haloperidol ( 1.5 mg/kg sc ) induced catalepsy tests were used as animal models of schizophrenia .

## Item biored:test:913
Example input:
Sentence: Inhibition of type I TGFb receptors ALK1/2/3/6 responsible for phosphorylation of Smad1/5/8 reduced the hyperproliferation seen in c.474delA fibroblasts .

Example answer:
{"entities": [{"text": "type I TGFb receptors", "type": "GeneOrGeneProduct"}, {"text": "ALK1/2/3/6", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: Gene deletion or pharmacological blockade of KCa3.1 protected against SOCE-induced Ca2+ overload and ER stress via the protein kinase B ( AKT ) signaling pathway in astrocytes .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: NRG-1 beta stimulated human and murine MPNST cell migration and invasion in a concentration-dependent manner in three-dimensional migration assays , acting as a chemotactic factor .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "murine", "type": "OrganismTaxon"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , CBKOTg mice reduced levels of phosphorylated mitogen-activated protein kinase ( extracellular signal-regulated kinase ) 1/2 and cAMP response element-binding protein at Ser-133 and synaptic molecules such as N-methyl-D-aspartate receptor 1 ( NMDA receptor 1 ) , NMDA receptor 2A , PSD-95 and synaptophysin in the subiculum compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}, {"text": "extracellular signal-regulated kinase ) 1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding protein", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-D-aspartate receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 2A", "type": "GeneOrGeneProduct"}, {"text": "PSD-95", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Receptor screening using pharmacological and molecular inhibitory approaches identified EP4 as a novel PGA2 receptor .

Example answer:
{"entities": [{"text": "EP4", "type": "GeneOrGeneProduct"}, {"text": "PGA2 receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report the inhibition of these unusual receptor tyrosine kinases by the multi-targeted cancer drugs imatinib and ponatinib , as well as the selective type II inhibitor DDR1-IN-1 .

Example answer:
{"entities": [{"text": "receptor tyrosine kinases", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "imatinib", "type": "ChemicalEntity"}, {"text": "ponatinib", "type": "ChemicalEntity"}, {"text": "DDR1-IN-1", "type": "ChemicalEntity"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both baseline and NRG-1 beta-induced migration were erbB-dependent and required the action of MEK 1/2 , SAPK/JNK , PI-3 kinase , Src family kinases and ROCK-I/II .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB-dependent", "type": "GeneOrGeneProduct"}, {"text": "MEK 1/2", "type": "GeneOrGeneProduct"}, {"text": "SAPK/JNK", "type": "GeneOrGeneProduct"}, {"text": "PI-3 kinase", "type": "GeneOrGeneProduct"}, {"text": "Src family kinases", "type": "GeneOrGeneProduct"}, {"text": "ROCK-I/II", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The NRG-1 receptors erbB3 and erbB4 were present in MPNST invadopodia ( processes mediating invasion ) , partially colocalized with focal adhesion kinase and the laminin receptor beta ( 1 ) -integrin and coimmunoprecipitated with beta ( 1 ) -integrin .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB3", "type": "GeneOrGeneProduct"}, {"text": "erbB4", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal adhesion kinase", "type": "GeneOrGeneProduct"}, {"text": "laminin receptor", "type": "GeneOrGeneProduct"}, {"text": "beta ( 1 ) -integrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: While NRG-1 beta potently and persistently activated Erk 1/2 , SAPK/JNK , Akt and Src family kinases , NRG-1 alpha did not activate Akt and activated these other kinases with kinetics distinct from those evident in NRG-1 beta-stimulated cells .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "Erk 1/2", "type": "GeneOrGeneProduct"}, {"text": "SAPK/JNK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Src family kinases", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}, {"text": "NRG-1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Pharmacological inhibition verified that Nrg2a signals through the ErbB receptor tyrosine kinase network .

## Item biored:test:873
Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A mouse inflammatory cytokine and receptor RT2 profiler array was used to determine regulated transcripts in the urinary bladder of wild type ( WT ) and VIP ( -/- ) mice with or without CYP-induced cystitis ( 150 mg/kg ; i.p .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CYP-induced", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cyclooxygenase-2 activity is required for the development of lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Cyclooxygenase-2", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice lacking mPGES-1 are resistant to lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In contrast , mPGES-1 -/- mice were largely resistant to lithium-induced polyuria and a urine concentrating defect , accompanied by nearly complete blockade of high urine PGE ( 2 ) and cAMP output .

Example answer:
{"entities": [{"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "cAMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: CYP treatment significantly ( p < or = 0.001 ) increased expression of CXCL1 and IL-1beta in the urinary bladder of WT and VIP ( -/- ) mice , but expression in VIP ( -/- ) mice with CYP treatment was significantly ( p < or = 0.001 ) greater ( 4.2- to 13-fold increase ) than that observed in WT urinary bladder ( 3.6- to 5-fold increase ) .

Example answer:
{"entities": []}

Example input:
Sentence: We conclude that mPGES-1-derived PGE ( 2 ) mediates lithium-induced polyuria likely via inhibition of AQP2 and NKCC2 expression .

Example answer:
{"entities": [{"text": "mPGES-1-derived", "type": "GeneOrGeneProduct"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: AQP2 and UT-A1 expression was lowered in 6 week lithium-treated WT animals whereas in treated PKCa KO mice , AQP2 was only reduced by 2-fold and UT-A1 expression was unaffected .

## Item biored:test:918
Example input:
Sentence: Consistent with these in vitro data , expression levels of the ER stress markers 78-kDa glucose-regulated protein and CCAAT/enhancer-binding protein homologous protein , as well as that of the RA marker glial fibrillary acidic protein were increased in APP/PS1 AD mouse model .

Example answer:
{"entities": [{"text": "78-kDa glucose-regulated protein", "type": "GeneOrGeneProduct"}, {"text": "CCAAT/enhancer-binding protein homologous protein", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: Although treatment with the pancreatic b-cell toxin streptozotocin induced hyperglycemia and raised plasma ghrelin levels in wild-type mice , hyperglycemia was averted in similarly treated Gcgr ( -/- ) mice and the plasma ghrelin level was further increased .

Example answer:
{"entities": [{"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "hyperglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ghrelin", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hsp90beta was previously proven to regulate the upstream mediators in multiple cellular signalling cascades through stabilizing and maintaining their activities .

Example answer:
{"entities": [{"text": "Hsp90beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: CCK and other GI-hormones/neurotransmitters/growth-factors activate PAK2 via small GTPases ( CDC42/Rac1 ) , PKC and SFK but not cytosolic calcium or PI3K .

Example answer:
{"entities": [{"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "small GTPases", "type": "GeneOrGeneProduct"}, {"text": "CDC42/Rac1", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "SFK", "type": "GeneOrGeneProduct"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We used rat pancreatic acini to explore the ability of GI-hormones/neurotransmitters/growth-factors to activate Group-I-PAKs and the signaling cascades involved .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "Group-I-PAKs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Overall , these results suggest that KCa3.1 is involved in the regulation of Ca2+ homeostasis in astrocytes and attenuation of the UPR and ER stress , thus contributing to memory deficits and neuronal loss .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PAK2 was activated by some pancreatic growth-factors [ EGF , PDGF , bFGF ] , by secretagogues activating phospholipase-C ( PLC ) [ CCK , carbachol , bombesin ] and by post-receptor stimulants activating PKC [ TPA ] , but not agents only mobilizing cellular calcium or increasing cyclic AMP .

Example answer:
{"entities": [{"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "pancreatic growth-factors", "type": "GeneOrGeneProduct"}, {"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "PDGF", "type": "GeneOrGeneProduct"}, {"text": "bFGF", "type": "GeneOrGeneProduct"}, {"text": "phospholipase-C", "type": "GeneOrGeneProduct"}, {"text": "PLC", "type": "GeneOrGeneProduct"}, {"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "carbachol", "type": "ChemicalEntity"}, {"text": "bombesin", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "TPA", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Expression of the master regulators of oxidative metabolism transcription factor A mitochondrial , PGC-1a , AMPK , and serine-threonine liver kinase B1 was altered by high glucose , as well as their downstream signaling networks .

Example answer:
{"entities": [{"text": "master regulators of oxidative metabolism transcription factor A mitochondrial", "type": "GeneOrGeneProduct"}, {"text": "PGC-1a", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "serine-threonine liver kinase B1", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : KCa3.1 expression was markedly associated with endoplasmic reticulum ( ER ) stress and unfolded protein response ( UPR ) in both Abeta-stimulated primary astrocytes and brain lysates of AD patients and APP/PS1 AD mice .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Abeta-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: BACKGROUND : Studies in mice have shown that PPARa is an important regulator of lipid metabolism in liver and key transcription factor involved in the adaptive response to fasting .

## Item biored:test:938
Example input:
Sentence: Consistent with these in vitro data , expression levels of the ER stress markers 78-kDa glucose-regulated protein and CCAAT/enhancer-binding protein homologous protein , as well as that of the RA marker glial fibrillary acidic protein were increased in APP/PS1 AD mouse model .

Example answer:
{"entities": [{"text": "78-kDa glucose-regulated protein", "type": "GeneOrGeneProduct"}, {"text": "CCAAT/enhancer-binding protein homologous protein", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: Model selection suggests an association between nucleotide substitution rate and disease progression , but a role for CCR5 genotype remains elusive .

Example answer:
{"entities": [{"text": "CCR5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A total of five SNPs were identified to show the possible association with severe myelosuppression ( P ( Fisher ) < 0.01 ) and were further examined in 7 cases and 20 controls in the second stage of the study .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A unique set of EPO-regulated survival factors included Lyl1 , Gas5 , Pim3 , Pim1 , Bim , Trib3 and Serpina 3g .

Example answer:
{"entities": [{"text": "EPO-regulated", "type": "GeneOrGeneProduct"}, {"text": "Lyl1", "type": "GeneOrGeneProduct"}, {"text": "Gas5", "type": "GeneOrGeneProduct"}, {"text": "Pim3", "type": "GeneOrGeneProduct"}, {"text": "Pim1", "type": "GeneOrGeneProduct"}, {"text": "Bim", "type": "GeneOrGeneProduct"}, {"text": "Trib3", "type": "GeneOrGeneProduct"}, {"text": "Serpina 3g", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Four variants in two genes exceeded the multiple testing threshold for associations with prostate cancer mortality in fixed-effect meta-analyses .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The prognostic value of serum tumour markers alpha-fetoprotein ( AFP ) and des-gamma-carboxy prothrombin ( DCP ) is limited .

Example answer:
{"entities": [{"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fetoprotein", "type": "GeneOrGeneProduct"}, {"text": "AFP", "type": "GeneOrGeneProduct"}, {"text": "des-gamma-carboxy prothrombin", "type": "GeneOrGeneProduct"}, {"text": "DCP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Relationships between protein expression and clinicopathological parameters were assessed , and the correlations between NEK2 with phospho-AKT and MMP-2 expressions were evaluated .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "MMP-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The correlation between survival and NEK2 expression was analyzed in 359 patients with HCC using RNASeqV2 data available from The Cancer Genome Atlas ( TCGA ) website ( https : //tcga-data.nci.nih.gov/tcga/ ) .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Potential associations of CEP55 expression scores with clinical parameters and patient survival were evaluated .

## Item biored:test:937
Example input:
Sentence: SEREX screening of cDNA expression libraries derived from 3 breast cancer patients identified a total of 88 positive clones ( bcg-1 to bcg-88 ) , including 27 hitherto unknown sequences .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: qRT-PCR detected similar patterns of changes in AQP2 mRNA in the medulla but not in the cortex .

Example answer:
{"entities": [{"text": "AQP2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Gene expression was analyzed by quantitative real-time PCR using RNA from peripheral blood mononuclear cells ( PBMC ) .

Example answer:
{"entities": []}

Example input:
Sentence: The standard of protein was measured by Western blot or immunofluorescence .

Example answer:
{"entities": []}

Example input:
Sentence: Expression of cytokines and IDO mRNA in OHSCs was measured by real-time RT-PCR and cytokine protein was measured by enzyme-linked immunosorbent assays ( ELISAs ) .

Example answer:
{"entities": [{"text": "IDO", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The 293T cells transfected with the full-coding cDNA inserted in the expression vector produced a new 80 kDa protein , as detected by Western blot .

Example answer:
{"entities": [{"text": "293T", "type": "CellLine"}]}

Example input:
Sentence: Western blot analysis and reverse transcription-polymerase chain reaction were used to detect target gene and protein expression .

Example answer:
{"entities": []}

Input:
Sentence: CEP55 mRNA and protein expression levels were detected by quantitative real-time PCR ( qRT-PCR ) , Western blotting , and immunohistochemistry ( IHC ) .

## Item biored:test:939
Example input:
Sentence: In this study , we knocked down Bach1 using adenovirus-mediated small interfering RNA ( siRNA ) to determine whether the use of Bach1 siRNA is an effective therapeutic strategy in mice with bleomycin ( BLM ) -induced PF .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "bleomycin", "type": "ChemicalEntity"}, {"text": "BLM", "type": "ChemicalEntity"}, {"text": "PF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunoperoxidase brightfield- and laser-scanning confocal fluorescence microscopy demonstrated increased targeting of alpha-ENaC , beta-ENaC , and gamma-ENaC subunits to the apical plasma membrane in the distal convoluted tubule ( DCT2 ) , connecting tubule , and cortical and medullary collecting duct segments .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "beta-ENaC", "type": "GeneOrGeneProduct"}, {"text": "gamma-ENaC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA from peripheral nuclear blood cells was genotyped for 5-HTTLPR using standard polymerase chain reaction methods.A significant group effect was observed only on memory function tasks ( p = 0.04 ) but not on reaction times ( p = 0.61 ) or attention/executive functioning ( p = 0.59 ) .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The 293T cells transfected with the full-coding cDNA inserted in the expression vector produced a new 80 kDa protein , as detected by Western blot .

Example answer:
{"entities": [{"text": "293T", "type": "CellLine"}]}

Example input:
Sentence: Histological analyses of apoptosis , proliferation , angiogenesis and infarct zone assessments were performed using terminal deoxynucleotidyltransferase-mediated dUTP nick-end labelling ( TUNEL ) staining , BrdU immunostaining , a-smooth muscle actin ( a-SMA ) /CD31 immunostaining and Masson 's trichrome staining , respectively .

Example answer:
{"entities": [{"text": "infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "terminal", "type": "GeneOrGeneProduct"}, {"text": "dUTP", "type": "ChemicalEntity"}, {"text": "a-smooth muscle actin", "type": "GeneOrGeneProduct"}, {"text": "a-SMA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A combination of fluorescence in situ hybridization ( FISH ) and Southern blot analysis demonstrated disruption of a synaptotagmin gene ( SYT14 ) at the 1q32 breakpoint .

Example answer:
{"entities": [{"text": "synaptotagmin", "type": "GeneOrGeneProduct"}, {"text": "SYT14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA damage and repair were evaluated by alkaline single cell gel electrophoresis ( comet assay ) assisted by DNA repair enzymes : endonuclease III ( Nth ) and formamidopyrimidine-DNA glycosylase ( Fpg ) , preferentially recognizing oxidized DNA bases .

Example answer:
{"entities": [{"text": "endonuclease III", "type": "GeneOrGeneProduct"}, {"text": "Nth", "type": "GeneOrGeneProduct"}, {"text": "formamidopyrimidine-DNA glycosylase", "type": "GeneOrGeneProduct"}, {"text": "Fpg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Western blot analysis and reverse transcription-polymerase chain reaction were used to detect target gene and protein expression .

Example answer:
{"entities": []}

Input:
Sentence: CEP55 function was investigated further using RNA interference , wound healing assay , transwell assay , immunofluorescence analysis , qRT-PCR , and Western blotting .

## Item biored:test:763
Example input:
Sentence: Gene deletion or pharmacological blockade of KCa3.1 protected against SOCE-induced Ca2+ overload and ER stress via the protein kinase B ( AKT ) signaling pathway in astrocytes .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Inhibition of type I TGFb receptors ALK1/2/3/6 responsible for phosphorylation of Smad1/5/8 reduced the hyperproliferation seen in c.474delA fibroblasts .

Example answer:
{"entities": [{"text": "type I TGFb receptors", "type": "GeneOrGeneProduct"}, {"text": "ALK1/2/3/6", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We recently reported that phosphoinositide 3-kinase ( PI3K ) /protein kinase B ( Akt ) mediates transcriptional regulation and activation of bone morphogenetic protein ( BMP ) -2 signaling by nuclear factor ( NF ) -kappaB in bone metastatic prostate cancer cells .

Example answer:
{"entities": [{"text": "phosphoinositide 3-kinase ( PI3K ) /protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "bone morphogenetic protein ( BMP ) -2", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor ( NF ) -kappaB", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: While NRG-1 beta potently and persistently activated Erk 1/2 , SAPK/JNK , Akt and Src family kinases , NRG-1 alpha did not activate Akt and activated these other kinases with kinetics distinct from those evident in NRG-1 beta-stimulated cells .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "Erk 1/2", "type": "GeneOrGeneProduct"}, {"text": "SAPK/JNK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Src family kinases", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}, {"text": "NRG-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Example input:
Sentence: Both baseline and NRG-1 beta-induced migration were erbB-dependent and required the action of MEK 1/2 , SAPK/JNK , PI-3 kinase , Src family kinases and ROCK-I/II .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB-dependent", "type": "GeneOrGeneProduct"}, {"text": "MEK 1/2", "type": "GeneOrGeneProduct"}, {"text": "SAPK/JNK", "type": "GeneOrGeneProduct"}, {"text": "PI-3 kinase", "type": "GeneOrGeneProduct"}, {"text": "Src family kinases", "type": "GeneOrGeneProduct"}, {"text": "ROCK-I/II", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: KEY FINDINGS : NNK stimulated expression of oncogenic genes , including MYB and PIK3CA in BEP2D , ETS1 , NRAS and SRC in Het-1A , and AKT1 , KIT and RB1 in both cell types , which could be abolished in the presence of rSLURP-1 .

## Item biored:test:902
Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Besides their role in neurotransmission and neuromodulation , they are involved in trophic factor release , apoptosis , and inflammatory responses .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Gene deletion or pharmacological blockade of KCa3.1 protected against SOCE-induced Ca2+ overload and ER stress via the protein kinase B ( AKT ) signaling pathway in astrocytes .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: NF-kB functions as a molecular link between tumor cells and Th1/Tc1 T cells in the tumor microenvironment to exert radiation-mediated tumor suppression .

Example answer:
{"entities": [{"text": "NF-kB", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Nuclear factor kappa B ( NFkappaB ) is a sensor of oxidative stress and participates in memory formation that could be involved in drug toxicity and addiction mechanisms .

Example answer:
{"entities": [{"text": "Nuclear factor kappa B", "type": "GeneOrGeneProduct"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , BMP-2 mediates TNF-alpha-induced invasion of C4-2B cells in a NF-kappaB-dependent fashion .

Example answer:
{"entities": [{"text": "BMP-2", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha-induced", "type": "GeneOrGeneProduct"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "NF-kappaB-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the present study , we demonstrate that NF-kappaB , whether activated by recombinant human tumor necrosis factor ( TNF ) -alpha or by ectopic expression of the p65 subunit , is involved in extracellular matrix adhesion and invasion of osteotropic PC-3 and C4-2B , but not LNCaP , cells .

Example answer:
{"entities": [{"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tumor necrosis factor ( TNF ) -alpha", "type": "GeneOrGeneProduct"}, {"text": "p65", "type": "GeneOrGeneProduct"}, {"text": "PC-3", "type": "CellLine"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "LNCaP", "type": "CellLine"}]}

Example input:
Sentence: The signal transduction target upon interleukin 1 beta ( IL1beta ) stimulation , the nuclear factor of kappa B ( NFkappaB ) activation , supports cancer development , signal transduction in which is mediated by FS-7 cell-associated cell surface antigen ( FAS ) signaling .

Example answer:
{"entities": [{"text": "interleukin 1 beta", "type": "GeneOrGeneProduct"}, {"text": "IL1beta", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor of kappa B", "type": "GeneOrGeneProduct"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FS-7 cell-associated cell surface antigen", "type": "GeneOrGeneProduct"}, {"text": "FAS", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , Sal treatment significantly decreases the release of inflammatory cytokines and inhibits the TLR4/NF-kappaB and MAPK signaling pathways .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TLR4/NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TNF-alpha or conditioned media ( CM ) of TNF-alpha-stimulated C4-2B cells upregulated BMP-2 and BMP-dependent Smad transcripts and inhibited receptor activator of NF-kappaB ligand transcripts in RAW 264.7 preosteoclast cells , respectively , implying that this factor may contribute to suppression of osteoclastogenesis via direct and paracrine mechanisms .

Example answer:
{"entities": [{"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha-stimulated", "type": "GeneOrGeneProduct"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "BMP-2", "type": "GeneOrGeneProduct"}, {"text": "BMP-dependent", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "receptor activator of NF-kappaB ligand", "type": "GeneOrGeneProduct"}, {"text": "RAW 264.7", "type": "CellLine"}]}

Input:
Sentence: The potential mechanisms include inhibition of the release of NO/TNF-alpha and repression of the NF-kappaB signaling pathways .

## Item biored:test:961
Example input:
Sentence: Four variants in two genes exceeded the multiple testing threshold for associations with prostate cancer mortality in fixed-effect meta-analyses .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The expression of the Msx2 gene and phosphorylated-Smad1/5/8 , possible readouts of Bmp signaling , was also increased in the mutants .

Example answer:
{"entities": [{"text": "Msx2", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Double immunofluorescence analysis showed that the number of accumulated F4/80 ( + ) cells expressing TGF-b1 in metastatic areas was higher in WT than in AT1aKO .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We found that the common allele is preferentially expressed in normal lymphocytes , normal breast , and breast tumors compared with the rare allele , but there were no differences in total levels of GPX4 mRNA across genotypes .

Example answer:
{"entities": [{"text": "breast tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In current study , we observed overexpression of LDHA in the clinical prostate cancer samples compared with benign prostate hyperplasia tissues as demonstrated by immunohistochemistry and real-time qPCR .

Example answer:
{"entities": [{"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our data show that in pre-malignant B cells , Myc overexpression is sufficient to activate BCR and PI3K/Akt signaling pathways and further enhances signaling following BCR ligation .

Example answer:
{"entities": [{"text": "Myc", "type": "GeneOrGeneProduct"}, {"text": "BCR", "type": "GeneOrGeneProduct"}, {"text": "PI3K/Akt", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Accumulating evidence from epidemiologic studies , chemical carcinogen-induced rodent models and clinical trials indicate that COX-2 plays a role in human carcinogenesis and is overexpressed in prostate cancer tissue .

Example answer:
{"entities": [{"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The enhanced metastatic potential was associated with transcriptional upregulation of osteopontin , osteocalcin , and collagen IA1 in osteotropic PC cells , suggesting their role in osteomimicry of PC cells .

Example answer:
{"entities": [{"text": "osteopontin", "type": "GeneOrGeneProduct"}, {"text": "osteocalcin", "type": "GeneOrGeneProduct"}, {"text": "collagen IA1", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Chronic overexpression influences steady-state levels of mRNAs for metastasis-related genes .

## Item biored:test:890
Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Calbindin-D28k ( CB ) , one of the major calcium-binding and buffering proteins , has a critical role in preventing a neuronal death as well as maintaining calcium homeostasis .

Example answer:
{"entities": [{"text": "Calbindin-D28k", "type": "GeneOrGeneProduct"}, {"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "neuronal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "calcium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Studies of synergy between morphine and a novel sodium channel blocker , CNSB002 , in rat models of inflammatory and neuropathic pain .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "sodium channel blocker", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "frataxin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVE : This study determined the antihyperalgesic effect of CNSB002 , a sodium channel blocker with antioxidant properties given alone and in combinations with morphine in rat models of inflammatory and neuropathic pain .

Example answer:
{"entities": [{"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "sodium channel blocker", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Topiramate prevented all the alterations observed , showing novel neuroprotective properties .

Example answer:
{"entities": [{"text": "Topiramate", "type": "ChemicalEntity"}]}

Example input:
Sentence: On the other hand , induction of metallothionein ( MT ) by ZnSO ( 4 ) and its role in neuroprotection has been documented .

Example answer:
{"entities": [{"text": "metallothionein", "type": "ChemicalEntity"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}]}

Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: TSPO ligands have shown anti-inflammatory and neuroprotective properties in models of CNS injury .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "CNS injury", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Neuroserpin ( NSP ) reportedly exerts neuroprotective effects in cerebral ischemic animal models and patients ; however , the mechanism of protection is poorly understood .

## Item biored:test:966
Example input:
Sentence: All of the patients ' plasma blood urea nitrogen ( BUN ) and creatinine levels were measured on the second and seventh day after the administration of intravenous contrast material .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "blood urea nitrogen", "type": "ChemicalEntity"}, {"text": "BUN", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "contrast", "type": "ChemicalEntity"}]}

Example input:
Sentence: INTERVENTION AND OUTCOME : An 18-gauge Touhy needle was inserted until loss of resistance occurred at the L4-5 level .

Example answer:
{"entities": []}

Example input:
Sentence: Antithrombin ( 50 or 500 IU/kg/i.v . )

Example answer:
{"entities": [{"text": "Antithrombin", "type": "ChemicalEntity"}]}

Example input:
Sentence: In pooled follow-up data for 768 antithrombotic users , presence of MB at baseline was associated with a substantially increased risk of subsequent ICH ( OR , 12.1 ; 95 % CI , 3.4-42.5 ; P < 0.001 ) .

Example answer:
{"entities": [{"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Peripheral blood samples were collected and genomic DNA was extracted from the leukocytes .

Example answer:
{"entities": []}

Example input:
Sentence: First , we showed that an intravenous administration of human PCC rapidly reversed anticoagulation in mice .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "PCC", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The mean hemorrhagic blood volume was reduced in PCC-treated animals ( 6.5+/-3.1 microL ) compared with saline controls ( 15.3+/-11.2 microL , P=0.015 ) .

Example answer:
{"entities": [{"text": "PCC-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the propositus , blood smears revealed giant platelets ( 30 x 10 ( 9 ) platelets/L ) , and platelet agglutination to ristocetin was absent .

Example answer:
{"entities": [{"text": "ristocetin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Using a mouse model , we tested whether the rapid reversal of anticoagulation using human prothrombin complex concentrate ( PCC ) can reduce hemorrhagic blood volume .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "prothrombin complex concentrate", "type": "ChemicalEntity"}, {"text": "PCC", "type": "ChemicalEntity"}]}

Input:
Sentence: Two milliliters of peripheral blood were collected in a sterile anticoagulative tube .

## Item biored:test:889
Example input:
Sentence: Brain-derived neurotrophic factor significantly inhibited Dox-induced cardiomyocyte apoptosis , oxidative stress and cardiac dysfunction in rats .

Example answer:
{"entities": [{"text": "cardiac", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Ca2+-dependent endoplasmic reticulum stress correlation with astrogliosis involves upregulation of KCa3.1 and inhibition of AKT/mTOR signaling .

Example answer:
{"entities": [{"text": "Ca2+-dependent", "type": "ChemicalEntity"}, {"text": "astrogliosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "AKT/mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: On the other hand , induction of metallothionein ( MT ) by ZnSO ( 4 ) and its role in neuroprotection has been documented .

Example answer:
{"entities": [{"text": "metallothionein", "type": "ChemicalEntity"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}]}

Example input:
Sentence: Superoxide dismutase 1 overexpression in mice abolishes maternal diabetes-induced endoplasmic reticulum stress in diabetic embryopathy .

Example answer:
{"entities": [{"text": "Superoxide dismutase 1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "maternal", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "embryopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "frataxin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , rats that experienced SE exhibited CCR2-labeling in populations of hypertrophied astrocytes , especially in CA1 and dentate gyrus .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCR2-labeling", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Neuroprotective effects of melatonin upon the offspring cerebellar cortex in the rat model of BCNU-induced cortical dysplasia .

Example answer:
{"entities": [{"text": "melatonin", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "cortical dysplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Neuroprotective effect of neuroserpin in oxygen-glucose deprivation- and reoxygenation-treated rat astrocytes in vitro .

## Item biored:test:950
Example input:
Sentence: Rab6a-GTP , either in solution or bound to artificial liposomes , released BICD2 from an autoinhibited state and promoted robust dynein-dynactin transport .

Example answer:
{"entities": [{"text": "Rab6a-GTP", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "dynein-dynactin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We have shown that MPNSTs express neuregulin-1 ( NRG-1 ) beta isoforms , which promote Schwann cell migration during development , and NRG-1 alpha isoforms , whose effects on Schwann cells are poorly understood .

Example answer:
{"entities": [{"text": "MPNSTs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuregulin-1 ( NRG-1 ) beta", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Surface-plasmon-resonance studies showed that the mutation influenced the binding and kinetics of the interactions between the aggrecan G3 domain and tenascin-C .

Example answer:
{"entities": [{"text": "aggrecan", "type": "GeneOrGeneProduct"}, {"text": "tenascin-C", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , Sal administration significantly suppresses epithelial-mesenchymal transition ( EMT ) , as evidenced by a decreased expression of alpha-SMA , vimentin , TGF-beta1 , snail , slug , and a largely restored expression of E-cadherin .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "alpha-SMA", "type": "GeneOrGeneProduct"}, {"text": "vimentin", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "snail", "type": "GeneOrGeneProduct"}, {"text": "slug", "type": "GeneOrGeneProduct"}, {"text": "E-cadherin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hypothesizing that NRG-1 beta and/or NRG-1 alpha promote MPNST invasion , we found that NRG-1 beta promoted MPNST migration in a substrate-specific manner , markedly enhancing migration on laminin but not on collagen type I or fibronectin .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "laminin", "type": "GeneOrGeneProduct"}, {"text": "collagen type I", "type": "GeneOrGeneProduct"}, {"text": "fibronectin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To investigate this question , we have developed in vitro motility assays with purified DDB and BICD2 's membrane vesicle partner , the GTPase Rab6a .

Example answer:
{"entities": [{"text": "DDB", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "GTPase Rab6a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: One of the responding genes was X-chromosomal tenomodulin ( TNMD ) , a putative angiogenesis inhibitor .

Example answer:
{"entities": [{"text": "tenomodulin", "type": "GeneOrGeneProduct"}, {"text": "TNMD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Remarkably , transfection of Langerin cDNA into fibroblasts created a compact network of membrane structures with typical features of BG .

Example answer:
{"entities": [{"text": "Langerin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: BACKGROUND : Transgelin is an actin-binding protein that promotes motility in normal cells .

## Item biored:test:911
Example input:
Sentence: PAK2 was activated by some pancreatic growth-factors [ EGF , PDGF , bFGF ] , by secretagogues activating phospholipase-C ( PLC ) [ CCK , carbachol , bombesin ] and by post-receptor stimulants activating PKC [ TPA ] , but not agents only mobilizing cellular calcium or increasing cyclic AMP .

Example answer:
{"entities": [{"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "pancreatic growth-factors", "type": "GeneOrGeneProduct"}, {"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "PDGF", "type": "GeneOrGeneProduct"}, {"text": "bFGF", "type": "GeneOrGeneProduct"}, {"text": "phospholipase-C", "type": "GeneOrGeneProduct"}, {"text": "PLC", "type": "GeneOrGeneProduct"}, {"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "carbachol", "type": "ChemicalEntity"}, {"text": "bombesin", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "TPA", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Hypothesizing that NRG-1 beta and/or NRG-1 alpha promote MPNST invasion , we found that NRG-1 beta promoted MPNST migration in a substrate-specific manner , markedly enhancing migration on laminin but not on collagen type I or fibronectin .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "laminin", "type": "GeneOrGeneProduct"}, {"text": "collagen type I", "type": "GeneOrGeneProduct"}, {"text": "fibronectin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: NRG-1 beta stimulated human and murine MPNST cell migration and invasion in a concentration-dependent manner in three-dimensional migration assays , acting as a chemotactic factor .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "murine", "type": "OrganismTaxon"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have shown that MPNSTs express neuregulin-1 ( NRG-1 ) beta isoforms , which promote Schwann cell migration during development , and NRG-1 alpha isoforms , whose effects on Schwann cells are poorly understood .

Example answer:
{"entities": [{"text": "MPNSTs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuregulin-1 ( NRG-1 ) beta", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The mutants also displayed reduced cell proliferation in the URS mesenchyme .

Example answer:
{"entities": []}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Example input:
Sentence: The NRG-1 receptors erbB3 and erbB4 were present in MPNST invadopodia ( processes mediating invasion ) , partially colocalized with focal adhesion kinase and the laminin receptor beta ( 1 ) -integrin and coimmunoprecipitated with beta ( 1 ) -integrin .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB3", "type": "GeneOrGeneProduct"}, {"text": "erbB4", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal adhesion kinase", "type": "GeneOrGeneProduct"}, {"text": "laminin receptor", "type": "GeneOrGeneProduct"}, {"text": "beta ( 1 ) -integrin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: In nrg2a mutant larvae , the basal keratinocytes within the apical MFF , known as ridge cells , displayed reduced pAKT levels as well as reduced apical domains and exaggerated basolateral domains .

## Item biored:test:929
Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Consistent with this premise , patient leukemic cells with relatively high levels of OPRM1 are more sensitive to L-asparaginase treatment compared to OPRM1-depleted leukemic cells , further indicating that OPRM1 loss has a crucial role in L-asparaginase resistance in leukemic patients .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CAA reduced hRPTEC cell number and protein , induced a loss in free intracellular thiols and an increase in necrosis markers .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}, {"text": "hRPTEC", "type": "CellLine"}, {"text": "thiols", "type": "ChemicalEntity"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : KCa3.1 expression was markedly associated with endoplasmic reticulum ( ER ) stress and unfolded protein response ( UPR ) in both Abeta-stimulated primary astrocytes and brain lysates of AD patients and APP/PS1 AD mice .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Abeta-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In IEC-6 crypt cells and jejunum enteroids quantitative RT-PCR showed a time- and dose-dependent upregulation of lpa2 in response to gamma-irradiation that was abolished by mutation of the NF-kappaB site in the lpa2 promoter or by inhibition of ATM/ATR kinases with CGK-733 , suggesting that lpa2 is a DNA damage response gene upregulated by ATM via NF-kappaB .

Example answer:
{"entities": [{"text": "IEC-6", "type": "CellLine"}, {"text": "lpa2", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "ATM/ATR kinases", "type": "GeneOrGeneProduct"}, {"text": "CGK-733", "type": "ChemicalEntity"}, {"text": "ATM", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: In particular , PPARa activation markedly suppressed immunity/inflammation-related genes in human liver slices but not in primary hepatocytes .

## Item biored:test:954
Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Using patient demographics , tumor characteristics , and CGP , we show that GIST lacking alterations in canonical genes occur in younger patients , frequently metastasize to lymph nodes , and most contain deleterious genomic alterations , including gene fusions involving FGFR1 and NTRK3 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "metastasize to lymph nodes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "NTRK3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The aim of this study was to investigate the effect of TGF-beta1 targeting by antisense oligonucleotides on the RNA synthesis and protein expression of TGF-beta isoforms and their receptors in keloid-derived fibroblasts .

Example answer:
{"entities": [{"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "oligonucleotides", "type": "ChemicalEntity"}, {"text": "TGF-beta", "type": "GeneOrGeneProduct"}, {"text": "keloid-derived", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Effect of the abrogation of TGF-beta1 by antisense oligonucleotides on the expression of TGF-beta-isoforms and their receptors I and II in isolated fibroblasts from keloid scars .

Example answer:
{"entities": [{"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "oligonucleotides", "type": "ChemicalEntity"}, {"text": "TGF-beta-isoforms and their receptors I and II", "type": "GeneOrGeneProduct"}, {"text": "keloid scars", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We performed comprehensive genomic profiling ( CGP ) for coding regions in more than 300 cancer-related genes of 186 GISTs to assess for their somatic alterations .

Example answer:
{"entities": [{"text": "cancer-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GISTs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , the MLFs infected with Bach1 siRNA exhibited increased mRNA and protein expression levels of heme oxygenase-1 and glutathione peroxidase 1 , but decreased levels of TGF-b1 and interleukin-6 in the cell supernatants compared with the cells exposed to TGF-b1 alone .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "heme oxygenase-1", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase 1", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "interleukin-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Exons and flanking intron sequences of the TGFBI gene were amplified by PCR with specific primers .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Downstream effects of transgelin overexpression were investigated by gene expression profiling and quantitative PCR .

## Item biored:test:920
Example input:
Sentence: Thus , our study demonstrates for the first time , a novel OPRM1-mediated mechanism for L-asparaginase resistance in ALL , and identifies OPRM1 as a functional biomarker for defining high-risk subpopulations and for the detection of evolving resistant clones .

Example answer:
{"entities": [{"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In IEC-6 crypt cells and jejunum enteroids quantitative RT-PCR showed a time- and dose-dependent upregulation of lpa2 in response to gamma-irradiation that was abolished by mutation of the NF-kappaB site in the lpa2 promoter or by inhibition of ATM/ATR kinases with CGK-733 , suggesting that lpa2 is a DNA damage response gene upregulated by ATM via NF-kappaB .

Example answer:
{"entities": [{"text": "IEC-6", "type": "CellLine"}, {"text": "lpa2", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "ATM/ATR kinases", "type": "GeneOrGeneProduct"}, {"text": "CGK-733", "type": "ChemicalEntity"}, {"text": "ATM", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RNA sequencing identified a significant overlap between ADAM12- and Epidermal Growth Factor Receptor ( EGFR ) -regulated genes .

Example answer:
{"entities": [{"text": "ADAM12-", "type": "GeneOrGeneProduct"}, {"text": "Epidermal Growth Factor Receptor", "type": "GeneOrGeneProduct"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Together , these findings imply that OCT4A induction following DNA damage in PA-1 cells , performs a cell stress , rather than self-renewal , function by moderating the expression of p21Cip1 , which alongside AMPK helps to then regulate autophagy .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The single base pair guanine insertion/deletion polymorphism ( 4G/5G ) within the promoter region of the PAI-1 gene influences PAI-1 synthesis and may modulate hepatic fibrogenesis .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "hepatic fibrogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Genome-wide loss-of-function genetic screening identifies opioid receptor u1 as a key regulator of L-asparaginase resistance in pediatric acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "opioid receptor u1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "acute lymphoblastic leukemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: METHODS : Here we set out to study the function of PPARa in human liver via analysis of whole genome gene regulation in human liver slices treated with the PPARa agonist Wy14643 .

## Item biored:test:893
Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cocaine", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}, {"text": "nNOS", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Histological analyses of apoptosis , proliferation , angiogenesis and infarct zone assessments were performed using terminal deoxynucleotidyltransferase-mediated dUTP nick-end labelling ( TUNEL ) staining , BrdU immunostaining , a-smooth muscle actin ( a-SMA ) /CD31 immunostaining and Masson 's trichrome staining , respectively .

Example answer:
{"entities": [{"text": "infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "terminal", "type": "GeneOrGeneProduct"}, {"text": "dUTP", "type": "ChemicalEntity"}, {"text": "a-smooth muscle actin", "type": "GeneOrGeneProduct"}, {"text": "a-SMA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: On the other hand , induction of metallothionein ( MT ) by ZnSO ( 4 ) and its role in neuroprotection has been documented .

Example answer:
{"entities": [{"text": "metallothionein", "type": "ChemicalEntity"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The study investigates if alpha-lipoic acid is neuroprotective against chemotherapy induced neurotoxicity , if mitochondrial damage plays a critical role in toxic neurodegenerative cascade , and if neuroprotective effects of alpha-lipoic acid depend on mitochondria protection .

Example answer:
{"entities": [{"text": "alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "toxic neurodegenerative cascade", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "frataxin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Input:
Sentence: To confirm the neuroprotective effects of NSP , we measured the cell survival rate , relative lactate dehydrogenase ( LDH ) release ; we also performed morphological methods , namely Hoechst 33342 staining and Annexin V assay .

## Item biored:test:928
Example input:
Sentence: The EPOR therefore engages a sophisticated set of transcriptome response circuits , with Tnfr-sf13c deployed as one novel positive regulator of proerythroblast formation .

Example answer:
{"entities": [{"text": "EPOR", "type": "GeneOrGeneProduct"}, {"text": "Tnfr-sf13c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The 293T cells transfected with the full-coding cDNA inserted in the expression vector produced a new 80 kDa protein , as detected by Western blot .

Example answer:
{"entities": [{"text": "293T", "type": "CellLine"}]}

Example input:
Sentence: RESULTS : KCa3.1 expression was markedly associated with endoplasmic reticulum ( ER ) stress and unfolded protein response ( UPR ) in both Abeta-stimulated primary astrocytes and brain lysates of AD patients and APP/PS1 AD mice .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Abeta-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Interestingly , the differential expression of miRNA in mice also corroborated with the miRNA expression in human PC cell lines and tissue samples ; ectopic expression of Let-7b in CD18/HPAF and Capan1 cells resulted in the downregulation of KRAS and MSST1 expression .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Let-7b", "type": "GeneOrGeneProduct"}, {"text": "CD18/HPAF", "type": "CellLine"}, {"text": "Capan1", "type": "CellLine"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "MSST1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Expression of the master regulators of oxidative metabolism transcription factor A mitochondrial , PGC-1a , AMPK , and serine-threonine liver kinase B1 was altered by high glucose , as well as their downstream signaling networks .

Example answer:
{"entities": [{"text": "master regulators of oxidative metabolism transcription factor A mitochondrial", "type": "GeneOrGeneProduct"}, {"text": "PGC-1a", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "serine-threonine liver kinase B1", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: Expression analysis on a cDNA panel from 17 different normal tissues by reverse transcription-PCR ( RT-PCR ) revealed tissue restricted mRNA expression of 2 of the 27 unknown antigens .

Example answer:
{"entities": []}

Example input:
Sentence: The single base pair guanine insertion/deletion polymorphism ( 4G/5G ) within the promoter region of the PAI-1 gene influences PAI-1 synthesis and may modulate hepatic fibrogenesis .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "hepatic fibrogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Comparative analysis of gene regulation by Wy14643 between human liver slices and primary human hepatocytes showed that down-regulation of gene expression by PPARa is much better captured by liver slices as compared to primary hepatocytes .

## Item biored:test:927
Example input:
Sentence: CD133 ( + ) ACC cells produced activated NOTCH1 ( N1ICD ) and generated CD133 ( - ) cells that expressed JAG1 as well as neural differentiation factors NR2F1 , NR2F2 , and p27Kip1 .

Example answer:
{"entities": [{"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "N1ICD", "type": "GeneOrGeneProduct"}, {"text": "JAG1", "type": "GeneOrGeneProduct"}, {"text": "NR2F1", "type": "GeneOrGeneProduct"}, {"text": "NR2F2", "type": "GeneOrGeneProduct"}, {"text": "p27Kip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: NEK2 , as the most obviously different DEG in cells and tissues from the RNA-seq data , was listed as an HCC candidate biomarker for further verification .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Five of the forty genes -- ENT3 , IDP3 , JEM1 , ARG2 and HSP82 -- ranked highest in their ability to block alpha-syn-induced reactive oxygen species accumulation , and these five genes were characterized in more detail .

Example answer:
{"entities": [{"text": "ENT3", "type": "GeneOrGeneProduct"}, {"text": "IDP3", "type": "GeneOrGeneProduct"}, {"text": "JEM1", "type": "GeneOrGeneProduct"}, {"text": "ARG2", "type": "GeneOrGeneProduct"}, {"text": "HSP82", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn-induced", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}]}

Example input:
Sentence: The aim of this study was therefore to investigate the influence of mutations in these innate immune receptor genes ( nucleotide oligomerisation domain ( NOD ) 2/caspase recruitment domain ( CARD ) 15 , NOD1/CARD4 , TUCAN/CARDINAL/CARD8 , Toll-like receptor ( TLR ) 4 , TLR2 , TLR1 and TLR6 ) on the development of antimicrobial and antiglycan antibodies in inflammatory bowel disease ( IBD ) .

Example answer:
{"entities": [{"text": "innate immune receptor", "type": "GeneOrGeneProduct"}, {"text": "nucleotide oligomerisation domain ( NOD )", "type": "GeneOrGeneProduct"}, {"text": "recruitment domain ( CARD ) 15", "type": "GeneOrGeneProduct"}, {"text": "NOD1/CARD4", "type": "GeneOrGeneProduct"}, {"text": "TUCAN/CARDINAL/CARD8", "type": "GeneOrGeneProduct"}, {"text": "Toll-like receptor ( TLR ) 4", "type": "GeneOrGeneProduct"}, {"text": "TLR2", "type": "GeneOrGeneProduct"}, {"text": "TLR1", "type": "GeneOrGeneProduct"}, {"text": "TLR6", "type": "GeneOrGeneProduct"}, {"text": "inflammatory bowel disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IBD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interestingly , DCs that were co-treated with cisplatin and lipopolysaccharide ( LPS ) exhibited a decreased immunostimulatory capacity for inducing the proliferation of Th1- and Th17-type T cells ; instead , these DCs contributed to Th2-type T cell immunity .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "lipopolysaccharide", "type": "ChemicalEntity"}, {"text": "LPS", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : We identified in ACC CD133-positive CSC that expressed NOTCH1 and SOX10 , formed spheroids , and initiated tumors in nude mice .

Example answer:
{"entities": [{"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD133-positive", "type": "GeneOrGeneProduct"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: We genotyped candidate single-nucleotide polymorphisms ( SNP ) in IL10 , CRP , GPX1 , GSR , GSTP1 , hOGG1 , IL1B , IL1RN , IL6 , IL8 , MPO , NOS2 , NOS3 , SOD1 , SOD2 , SOD3 , TLR4 , and TNF and tagging SNPs in IL10 , CRP , GSR , IL1RN , IL6 , NOS2 , and NOS3 .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "IL1RN", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "IL8", "type": "GeneOrGeneProduct"}, {"text": "MPO", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "NOS3", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "SOD3", "type": "GeneOrGeneProduct"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "TNF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Stage IIIb or IV NSCLC patients , with two or fewer prior chemotherapy regimens , one platinum based ( stratum 1 ) or both chemotherapy and epidermal growth factor receptor tyrosine kinase inhibitors ( stratum 2 ) , received RAD001 10 mg/day until progression or unacceptable toxicity .

Example answer:
{"entities": [{"text": "NSCLC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "platinum", "type": "ChemicalEntity"}, {"text": "epidermal growth factor receptor tyrosine kinase", "type": "GeneOrGeneProduct"}, {"text": "RAD001", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A common IL10 haplotype and 2 common NOS2 haplotypes were associated with recurrence .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: TLR3 , NOS2 , and LCN2 ) .
