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

## Item biored:test:764
Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Inhibition of type I TGFb receptors ALK1/2/3/6 responsible for phosphorylation of Smad1/5/8 reduced the hyperproliferation seen in c.474delA fibroblasts .

Example answer:
{"entities": [{"text": "type I TGFb receptors", "type": "GeneOrGeneProduct"}, {"text": "ALK1/2/3/6", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Variation in IL10 , CRP , GSTP1 , IL1B , and NOS2 was associated with prostate cancer recurrence independent of pathologic prognostic factors .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: FGFR1 and NTRK3 actionable alterations in `` Wild-Type '' gastrointestinal stromal tumors .

Example answer:
{"entities": [{"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "NTRK3", "type": "GeneOrGeneProduct"}, {"text": "gastrointestinal stromal tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Example input:
Sentence: While FGF2 , IL1B , TNF and PDGFB were predicted as top upstream regulators ( p < 2x10-16 ) of the UCHL1 KD-associated transcriptome .

Example answer:
{"entities": [{"text": "FGF2", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "TNF", "type": "GeneOrGeneProduct"}, {"text": "PDGFB", "type": "GeneOrGeneProduct"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Other cancer-related genes whose upregulation by NNK was abolishable by rSLURP-1 were the growth factors EGF in BEP2D cells and HGF in Het-1A cells , and the transcription factors CDKN2A and STAT3 ( Het-1A only ) .

## Item biored:test:808
Example input:
Sentence: The standard of protein was measured by Western blot or immunofluorescence .

Example answer:
{"entities": []}

Example input:
Sentence: Chronic inflammation enhances gankyrin expression in the human liver .

Example answer:
{"entities": [{"text": "Chronic inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gankyrin", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Flow-cytometric analysis of the patient 's platelets showed a markedly reduced surface expression of all three glycoproteins of the GPIb/IX/V complex .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "glycoproteins", "type": "GeneOrGeneProduct"}, {"text": "GPIb/IX/V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemistry and western blotting are used to determine the mechanisms of Sal against RIF .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "RIF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunoperoxidase brightfield- and laser-scanning confocal fluorescence microscopy demonstrated increased targeting of alpha-ENaC , beta-ENaC , and gamma-ENaC subunits to the apical plasma membrane in the distal convoluted tubule ( DCT2 ) , connecting tubule , and cortical and medullary collecting duct segments .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "beta-ENaC", "type": "GeneOrGeneProduct"}, {"text": "gamma-ENaC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Histological analyses of apoptosis , proliferation , angiogenesis and infarct zone assessments were performed using terminal deoxynucleotidyltransferase-mediated dUTP nick-end labelling ( TUNEL ) staining , BrdU immunostaining , a-smooth muscle actin ( a-SMA ) /CD31 immunostaining and Masson 's trichrome staining , respectively .

Example answer:
{"entities": [{"text": "infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "terminal", "type": "GeneOrGeneProduct"}, {"text": "dUTP", "type": "ChemicalEntity"}, {"text": "a-smooth muscle actin", "type": "GeneOrGeneProduct"}, {"text": "a-SMA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Western blot analysis and reverse transcription-polymerase chain reaction were used to detect target gene and protein expression .

Example answer:
{"entities": []}

Example input:
Sentence: Moreover mRNA levels of LDLr and ERK1/2 as well as protein levels of total and activated forms of ERK1/2 in rat liver were evaluated by Western blotting and quantitative real time polymerase chain reaction analysis .

Example answer:
{"entities": [{"text": "LDLr", "type": "GeneOrGeneProduct"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: The 293T cells transfected with the full-coding cDNA inserted in the expression vector produced a new 80 kDa protein , as detected by Western blot .

Example answer:
{"entities": [{"text": "293T", "type": "CellLine"}]}

Input:
Sentence: The protein expressions of intercellular adhesion molecule-1 ( ICAM-1 ) and vascular cell adhesion molecule-1 ( VCAM-1 ) in liver were analyzed with Western blotting .

## Item biored:test:817
Example input:
Sentence: Dexamethasone significantly increased SBP and plasma H2O2 level and decreased thymus and body weights .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "H2O2", "type": "ChemicalEntity"}]}

Example input:
Sentence: Likewise , in vivo , B6D2F1 mice were treated with etoposide , daunorubicin , and doxorubicin , with or without dexrazoxane over a wide range of doses : posttreatment , a full hematologic evaluation was done .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "daunorubicin", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "dexrazoxane", "type": "ChemicalEntity"}]}

Example input:
Sentence: Notably , Myc-overexpressing B cells maintained elevated BCR signaling despite treatment with ibrutinib , a Bruton 's tyrosine kinase inhibitor .

Example answer:
{"entities": [{"text": "Myc-overexpressing", "type": "GeneOrGeneProduct"}, {"text": "BCR", "type": "GeneOrGeneProduct"}, {"text": "ibrutinib", "type": "ChemicalEntity"}, {"text": "Bruton 's tyrosine kinase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Clinical trials in patients with brain metastases combining dexrazoxane and high doses of etoposide is ongoing with the aim of improving efficacy without aggravating hematologic toxicity .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexrazoxane", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "hematologic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prolonged PFS and OS were observed in patients achieving CR and receiving bort-dex a single line of prior therapy .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "bort-dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: This retrospective study investigated the combination of bort ( 1.3 mg/m ( 2 ) on days 1 , 4 , 8 , and 11 every 3 weeks ) and dex ( 20 mg on the day of and the day after bort ) as salvage treatment in 85 patients with R/R MM after prior autologous stem cell transplantation or conventional chemotherapy .

Example answer:
{"entities": [{"text": "bort", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Eighty-seven percent of the patients had received immunomodulatory drugs included in some line of therapy before bort-dex .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "bort-dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Bort-dex was an effective salvage treatment for MM patients , particularly for those in first relapse .

Example answer:
{"entities": [{"text": "Bort-dex", "type": "ChemicalEntity"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Bortezomib and dexamethasone as salvage therapy in patients with relapsed/refractory multiple myeloma : analysis of long-term clinical outcomes .

Example answer:
{"entities": [{"text": "Bortezomib", "type": "ChemicalEntity"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple myeloma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Bortezomib ( bort ) -dexamethasone ( dex ) is an effective therapy for relapsed/refractory ( R/R ) multiple myeloma ( MM ) .

Example answer:
{"entities": [{"text": "Bortezomib", "type": "ChemicalEntity"}, {"text": "bort", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "multiple myeloma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Bortezomib and high-dose dexamethasone-containing regimens are considered to be generally tolerable with few severe bacterial infections in patients with B-cell malignancies .

## Item biored:test:878
Example input:
Sentence: Gene expression analysis revealed that rs10954213 exerted the greatest influence on IRF5 transcript levels .

Example answer:
{"entities": [{"text": "rs10954213", "type": "SequenceVariant"}, {"text": "IRF5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Long-Lived CD4+IFN-g+ T Cells rather than Short-Lived CD4+IFN-g+IL-10+ T Cells Initiate Rapid IL-10 Production To Suppress Anamnestic T Cell Responses during Secondary Malaria Infection .

Example answer:
{"entities": [{"text": "CD4+IFN-g+", "type": "GeneOrGeneProduct"}, {"text": "CD4+IFN-g+IL-10+", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "Malaria Infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SB 202190 significantly decreased IDO expression induced by Tat , and this effect was accompanied by a reduction of Tat-induced expression of TNFa , IL-6 , iNOS and SERT .

Example answer:
{"entities": [{"text": "SB 202190", "type": "ChemicalEntity"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "Tat-induced", "type": "GeneOrGeneProduct"}, {"text": "TNFa", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "SERT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: When the patients were stratified by the SE , the rs729302 A allele was found to confer increased risk to RA in patients that were SE negative ( OR 1.50 , 95 % CI 1.17 to 1.92 , p = 0.001 ) as compared with patients carrying the SE ( OR 1.11 , 95 % CI 0.93 to 1.33 , p = 0.24 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs729302", "type": "SequenceVariant"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In rhesus monkeys , rDEN2Delta30 appeared to be slightly attenuated when compared to the parent virus as measured by duration and peak of viremia and neutralizing antibody induction .

Example answer:
{"entities": [{"text": "rhesus monkeys", "type": "OrganismTaxon"}, {"text": "rDEN2Delta30", "type": "OrganismTaxon"}, {"text": "viremia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The results in this study significantly improve our understanding of the durability of IL-10-producing CD4 ( + ) T cells postinfection and provide information on how IL-10 may contribute to optimized parasite control and prevention of immune-mediated pathology during repeated malaria infections .

Example answer:
{"entities": [{"text": "IL-10-producing", "type": "GeneOrGeneProduct"}, {"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "malaria infections", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The binding of mTOR , PRAS40 and RagC to raptor did not differ for control and septic muscle in the basal condition ; however , the Leu-induced decrease in PRAS40 raptor and increase in RagC raptor seen in control muscle was absent in sepsis .

Example answer:
{"entities": [{"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "PRAS40", "type": "GeneOrGeneProduct"}, {"text": "RagC", "type": "GeneOrGeneProduct"}, {"text": "raptor", "type": "GeneOrGeneProduct"}, {"text": "Leu-induced", "type": "ChemicalEntity"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In RA FLSs , the level of PRMT5 was up-regulated by stimulation with IL-1b and TNF-a .

Example answer:
{"entities": [{"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PRMT5", "type": "GeneOrGeneProduct"}, {"text": "IL-1b", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A mouse inflammatory cytokine and receptor RT2 profiler array was used to determine regulated transcripts in the urinary bladder of wild type ( WT ) and VIP ( -/- ) mice with or without CYP-induced cystitis ( 150 mg/kg ; i.p .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CYP-induced", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Notably , IL-10 exerted quantitatively stronger regulatory effects on innate and CD4 ( + ) T cell responses during primary and secondary infections , respectively .

Example answer:
{"entities": [{"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "CD4", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Characterizing the host cytokine response to RSV infection , the regulation of host cytokines and the impact of neutralizing an RSV-inducible cytokine during infection were undertaken in this study .

## Item biored:test:851
Example input:
Sentence: OBJECTIVE : This study determined the antihyperalgesic effect of CNSB002 , a sodium channel blocker with antioxidant properties given alone and in combinations with morphine in rat models of inflammatory and neuropathic pain .

Example answer:
{"entities": [{"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "sodium channel blocker", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , our findings reveal a potent protective role of BDNF against Dox-induced cardiotoxicity by activating Akt signalling , which may facilitate the safe use of Dox in cancer treatment .

Example answer:
{"entities": []}

Example input:
Sentence: Apamin , a selective blocker of calcium-dependent potassium channels , was administered intracerebroventricularly in rats anesthetized with 0.8 % sevoflurane to investigate the mechanism of the anticonvulsive effects .

Example answer:
{"entities": [{"text": "Apamin", "type": "ChemicalEntity"}, {"text": "calcium-dependent", "type": "ChemicalEntity"}, {"text": "potassium", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "sevoflurane", "type": "ChemicalEntity"}]}

Example input:
Sentence: Relationships between desminopathies and Voltage-dependent anion channel 1 ( VDAC1 ) remain unclear .

Example answer:
{"entities": [{"text": "desminopathies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Voltage-dependent anion channel 1", "type": "GeneOrGeneProduct"}, {"text": "VDAC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We hypothesized that epithelial Na channel ( ENaC ) subunit dysregulation may be responsible for the increased sodium retention .

Example answer:
{"entities": [{"text": "epithelial Na channel ( ENaC ) subunit", "type": "GeneOrGeneProduct"}, {"text": "sodium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Inhibition of Na ( + ) channels by local anesthetics may regulate desipramine-induced down-regulation of NET function .

Example answer:
{"entities": [{"text": "Na ( + )", "type": "ChemicalEntity"}, {"text": "anesthetics", "type": "ChemicalEntity"}, {"text": "desipramine-induced", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Voltage-Dependent Anion Channel 1 ( VDAC1 ) Participates the Apoptosis of the Mitochondrial Dysfunction in Desminopathy .

Example answer:
{"entities": [{"text": "Voltage-Dependent Anion Channel 1", "type": "GeneOrGeneProduct"}, {"text": "VDAC1", "type": "GeneOrGeneProduct"}, {"text": "Mitochondrial Dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Desminopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These data suggest that pilocarpine produced antiarrhythmic actions on arrhythmic rat and guinea pig models induced by aconitine or ouabain via stimulating the cardiac M ( 3 ) -mAChR .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "M ( 3 ) -mAChR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: [ Ca ( 2+ ) ] ( i ) overload induced by aconitine or ouabain was reduced in isolated myocytes pretreated with pilocarpine .

Example answer:
{"entities": [{"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: This study was designed to evaluate the effects of pilocarpine and explore the underlying ionic mechanism , using both aconitine-induced rat and ouabain-induced guinea pig arrhythmia models .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "aconitine-induced", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "ouabain-induced", "type": "ChemicalEntity"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Emerging evidence indicates that voltage-dependent Na ( + ) channels have pivotal roles in the cardiotoxicity of aconitine .

## Item biored:test:837
Example input:
Sentence: Compound 1 is a potent A ( 2A ) /A ( 1 ) receptor antagonist in vitro ( A ( 2A ) K ( i ) = 4.1 nM ; A ( 1 ) K ( i ) = 17.0 nM ) that has excellent activity , after oral administration , across a number of animal models of Parkinson 's disease including mouse and rat models of haloperidol-induced catalepsy , mouse model of reserpine-induced akinesia , rat 6-hydroxydopamine ( 6-OHDA ) lesion model of drug-induced rotation , and MPTP-treated non-human primate model .

Example answer:
{"entities": [{"text": "A ( 2A ) /A ( 1 ) receptor antagonist", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "reserpine-induced", "type": "ChemicalEntity"}, {"text": "akinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "6-hydroxydopamine", "type": "ChemicalEntity"}, {"text": "6-OHDA", "type": "ChemicalEntity"}, {"text": "MPTP-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: The goal of this study was to assess the interactive effects of chronic anabolic androgenic steroid ( AAS ) exposure and brain serotonin ( 5-hydroxytryptamine , 5-HT ) depletion on behavior of pubertal male rats .

Example answer:
{"entities": [{"text": "anabolic androgenic steroid", "type": "ChemicalEntity"}, {"text": "AAS", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "5-hydroxytryptamine", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Methamphetamine ( METH ) damages dopamine ( DA ) nerve endings by a process that has been linked to microglial activation but the signaling pathways that mediate this response have not yet been delineated .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "allopurinol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Notably , this and other converging lines of evidence underline the importance of DISC1-related functional pathways in the etiology of schizophrenia .

Example answer:
{"entities": [{"text": "DISC1-related", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although none of the observed linkages remained significant after multiple test correction through simulation , further analysis of NDE1 revealed an association between a tag-haplotype and schizophrenia ( P = 0.00046 ) specific to females , which proved to be significant ( P = 0.011 ) after multiple test correction .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It is widely believed that dopamine ( DA ) mediates methamphetamine ( METH ) -induced toxicity to brain dopaminergic neurons , because drugs that interfere with DA neurotransmission decrease toxicity , whereas drugs that increase DA neurotransmission enhance toxicity .

Example answer:
{"entities": [{"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : We have established that activation of the tryptophan degrading enzyme indoleamine 2,3 dioxygenase ( IDO ) mediates the switch from cytokine-induced sickness behavior to depressive-like behavior .

Example answer:
{"entities": [{"text": "tryptophan", "type": "ChemicalEntity"}, {"text": "indoleamine 2,3 dioxygenase", "type": "GeneOrGeneProduct"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "depressive-like", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : In this study , we evaluated the performance of dopamine beta-hydroxylase knockout ( Dbh -/- ) mice , which lack norepinephrine ( NE ) , in the elevated plus maze ( EPM ) to examine the contribution of noradrenergic signaling to cocaine-induced anxiety .

Example answer:
{"entities": [{"text": "dopamine beta-hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "norepinephrine", "type": "ChemicalEntity"}, {"text": "NE", "type": "ChemicalEntity"}, {"text": "cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "disulfiram", "type": "ChemicalEntity"}, {"text": "dopamine beta-hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "DBH", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: OBJECTIVE : To examine the effects of dehydroepiandrosterone ( DHEA ) on animal models of schizophrenia .

## Item biored:test:906
Example input:
Sentence: Tumor development in response to Ras activation varies between different tissues and the molecular basis for these variations are poorly understood .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Ras", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We suggest that the use of skin care products supplemented with proven chemopreventive agents in conjunction with the use of sunscreens along with educational efforts may be an effective strategy for reducing UV-induced photodamage and skin cancer in humans .

Example answer:
{"entities": [{"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: We first identified the change of signaling pathways and differentially expressed proteins globally by removing CB in Tg mice using mass spectrometry and antibody microarray .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The p53 mutation spectrum , presenting a high level of CC to TT mutations , shows that the UV component of sunlight is the major risk factor and modulated DNA repair by immunosuppressive drug treatment may be significant in the skin carcinogenesis of RTRs .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "CC to TT", "type": "SequenceVariant"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , all cases show similar clinical features , highlighting the importance of functional plakophilin 1 in maintaining desmosomal adhesion in skin , as well as the role of this protein in aspects of ectodermal development .

Example answer:
{"entities": [{"text": "plakophilin 1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Thus , immunosuppression has increased the risk of infections by HPVs , predominantly epidermodysplasia verruciformis , speculated to play a role in skin cancer development .

Example answer:
{"entities": [{"text": "infections", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HPVs", "type": "OrganismTaxon"}, {"text": "epidermodysplasia verruciformis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Skin biopsy revealed widening of intercellular spaces in the epidermis and a reduced number of small , poorly formed desmosomes .

Example answer:
{"entities": []}

Example input:
Sentence: Photochemoprevention has been appreciated as a viable approach to reduce the occurrence of skin cancer and in recent years , the use of agents , especially botanical antioxidants , present in the common diet and beverages consumed by human population have gained considerable attention as photochemopreventive agents for human use .

Example answer:
{"entities": [{"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: The development of skin cancer is a complex multistage phenomenon involving three distinct stages exemplified by initiation , promotion and progression stages .

Example answer:
{"entities": [{"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All these processes for skin cancer development involve stimulation of DNA synthesis , DNA damage and proliferation , inflammation , immunosuppression , epidermal hyperplasia , cell cycle dysregulation , depletion of antioxidant defenses , impairment of signal transduction pathways , induction of cyclooxygenase , increase in prostaglandin synthesis , and induction of ornithine decarboxylase .

Example answer:
{"entities": [{"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "epidermal hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antioxidant", "type": "ChemicalEntity"}, {"text": "cyclooxygenase", "type": "GeneOrGeneProduct"}, {"text": "prostaglandin", "type": "ChemicalEntity"}, {"text": "ornithine decarboxylase", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: A more comprehensive understanding of skin development mechanisms will drive identification of new treatment targets and modalities .

## Item biored:test:791
Example input:
Sentence: The aim of the study was to investigate the effects of moderate and heavy MDMA use on cognitive function , as well as the effects of long-term abstention from MDMA , in subjects genotyped for 5-HTTLPR .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The current study aimed to assess the impact of MDMA use on three separate central executive processes ( set shifting , inhibition and memory updating ) and also on `` prefrontal '' mediated social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Learning and memory deficits in ecstasy users and their neural correlates during a face-learning task .

Example answer:
{"entities": [{"text": "Learning and memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Although 3,4-methylenedioxymethamphetamine ( MDMA or ecstasy ) has been shown to damage brain serotonin ( 5-HT ) neurons in animals and possibly humans , little is known about the long-term consequences of MDMA-induced 5-HT neurotoxic lesions on functions in which 5-HT is involved , such as cognitive function .

Example answer:
{"entities": [{"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "MDMA-induced", "type": "ChemicalEntity"}, {"text": "neurotoxic lesions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Memory function and serotonin transporter promoter gene polymorphism in ecstasy ( MDMA ) users .

Example answer:
{"entities": [{"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: In recent years working memory deficits have been reported in users of MDMA ( 3,4-methylenedioxymethamphetamine , ecstasy ) .

Example answer:
{"entities": [{"text": "memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Compared with MDMA-free polydrug controls , MDMA polydrug users showed impairments in set shifting and memory updating , and also in social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA-free", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: MDMA polydrug users show process-specific central executive impairments coupled with impaired social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "impaired social and emotional judgement processes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Depression , impulsiveness , sleep , and memory in past and present polydrug users of 3,4-methylenedioxymethamphetamine ( MDMA , ecstasy ) .

## Item biored:test:856
Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: In a separate group of mice not subjected to behavioral studies , the same dose of NTG ( n = 3 ) and NTG + NIMO ( n = 3 ) caused mean arterial blood pressure to decrease from 85.9 +/- 3.8 mm Hg sem to 31.6 +/- 0.8 mm Hg sem and from 86.2 +/- 3.7 mm Hg sem to 32.6 +/- 0.2 mm Hg sem , respectively .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: Subcutaneous injection of ISPH ( 200 mg/kg body weight in 1 ml saline ) to rats for 2 consecutive days caused myocardial damage in rat heart , which was determined by the increased activity of serum lactate dehydrogenase ( LDH ) and creatine phosphokinase isoenzymes ( CK-MB ) , increased uric acid level and reduced plasma iron binding capacity .

Example answer:
{"entities": [{"text": "ISPH", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "LDH", "type": "GeneOrGeneProduct"}, {"text": "creatine phosphokinase isoenzymes", "type": "GeneOrGeneProduct"}, {"text": "CK-MB", "type": "GeneOrGeneProduct"}, {"text": "uric acid", "type": "ChemicalEntity"}, {"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: Moderate or severe adverse events were more common in subjects on clonidine ( 79.4 % versus 49.2 % ; p =.0006 ) but not associated with higher rates of early study withdrawal .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}]}

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
Sentence: The results showed that aconitine resulted in myocardial injury and reduced NRVMs viability dose-dependently .

## Item biored:test:861
Example input:
Sentence: Expression of the master regulators of oxidative metabolism transcription factor A mitochondrial , PGC-1a , AMPK , and serine-threonine liver kinase B1 was altered by high glucose , as well as their downstream signaling networks .

Example answer:
{"entities": [{"text": "master regulators of oxidative metabolism transcription factor A mitochondrial", "type": "GeneOrGeneProduct"}, {"text": "PGC-1a", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "serine-threonine liver kinase B1", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: For in vitro experiments , cardiomyocytes were isolated from both TIEG1 knockout ( KO ) and wile-type ( WT ) mice , and the apoptotic ratios were evaluated after a 48-h ischaemic insult .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: To obtain clues to the normal biological role of DMPK in cellular ion homeostasis , we have compared the resting [ Ca2 + ] i , the amplitude and shape of depolarization-induced Ca2 + transients , and the content of ATP-driven ion pumps in cultured skeletal muscle cells of wild-type and DMPK [ -/- ] knockout mice .

Example answer:
{"entities": [{"text": "DMPK", "type": "GeneOrGeneProduct"}, {"text": "Ca2 +", "type": "ChemicalEntity"}, {"text": "ATP-driven", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Decreased cardiac erythropoietin and increased SOCS3 further downregulated the cardioprotective JAK/STAT3 pathway .

Example answer:
{"entities": [{"text": "erythropoietin", "type": "GeneOrGeneProduct"}, {"text": "SOCS3", "type": "GeneOrGeneProduct"}, {"text": "JAK/STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This cardioprotection is accompanied by decreased cardiac oxidative stress and triglycerides and increased cardiac fatty-acid oxidation , ATP synthesis , and upregulated JAK/STAT3 pathway .

Example answer:
{"entities": [{"text": "triglycerides", "type": "ChemicalEntity"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "JAK/STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Importantly , fibroblasts carrying the mutation showed twofold increase in proliferation rate associated with hyperphosphorylation of Smad1/5/8 .

Example answer:
{"entities": [{"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Improved cardiac function and less scar formation were observed in TIEG1 KO mice , and we also observed the altered expression of phosphatase and tensin homolog ( Pten ) , Akt and Bcl-2/Bax , as well as vascular endothelial growth factor ( VEGF ) .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "Pten", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2/Bax", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , the GnRH-induced activation of p38 MAPK was decreased by BMP-4 .

Example answer:
{"entities": [{"text": "GnRH-induced", "type": "GeneOrGeneProduct"}, {"text": "p38 MAPK", "type": "GeneOrGeneProduct"}, {"text": "BMP-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Phosphorylated AMPKa ( p-AMPK ) in the myocardium was significantly elevated by 25mg/kg of metformin , slightly by 50mg/kg , but not by 100mg/kg .

Example answer:
{"entities": [{"text": "AMPKa", "type": "GeneOrGeneProduct"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: p38 MAPK phosphorylation was analyzed by western blot .

Example answer:
{"entities": [{"text": "p38 MAPK", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Furthermore , increased phosphorylation of MAPK family members , especially the P-P38/P38 ratio was found in cardiac tissues .

## Item biored:test:802
Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interestingly , DCs that were co-treated with cisplatin and lipopolysaccharide ( LPS ) exhibited a decreased immunostimulatory capacity for inducing the proliferation of Th1- and Th17-type T cells ; instead , these DCs contributed to Th2-type T cell immunity .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "lipopolysaccharide", "type": "ChemicalEntity"}, {"text": "LPS", "type": "ChemicalEntity"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Also , histopathological renal tissue damage mediated by cisplatin was ameliorated by coenzyme Q10 treatment .

Example answer:
{"entities": [{"text": "renal tissue damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "coenzyme Q10", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results suggested that resident hepatic macrophages induced liver metastasis formation by induction of TGF-b1 through AT1a signaling .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The protective role of mangiferin was analyzed by triphenyl tetrazolium chloride ( TTC ) test used for macroscopic enzyme mapping assay of the ischemic myocardium .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "triphenyl tetrazolium chloride", "type": "ChemicalEntity"}, {"text": "TTC", "type": "ChemicalEntity"}, {"text": "ischemic myocardium", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: It was concluded that coenzyme Q10 represents a potential therapeutic option to protect against acute cisplatin nephrotoxicity commonly encountered in clinical practice .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "nephrotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Chronic inflammation enhances gankyrin expression in the human liver .

Example answer:
{"entities": [{"text": "Chronic inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gankyrin", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Input:
Sentence: Cultured mycelium Cordyceps sinensis ( CMCS ) was widely used for a variety of diseases including liver injury , the current study aims to investigate the protective effects of CMCS on liver sinusoidal endothelial cells ( LSECs ) in acute injury liver and related action mechanisms .

## Item biored:test:853
Example input:
Sentence: Chloroacetaldehyde ( CAA ) is a metabolite of the alkylating agent ifosfamide ( IFO ) and putatively responsible for renal damage following anti-tumor therapy with IFO .

Example answer:
{"entities": [{"text": "Chloroacetaldehyde", "type": "ChemicalEntity"}, {"text": "CAA", "type": "ChemicalEntity"}, {"text": "alkylating agent", "type": "ChemicalEntity"}, {"text": "ifosfamide", "type": "ChemicalEntity"}, {"text": "IFO", "type": "ChemicalEntity"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our data demonstrate that the dystonia-causing mutations strongly affect hippocalcin cellular functions which suggest a central role for perturbed calcium signalling in DYT2 dystonia .

Example answer:
{"entities": [{"text": "dystonia-causing", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hippocalcin", "type": "GeneOrGeneProduct"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "DYT2", "type": "GeneOrGeneProduct"}, {"text": "dystonia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Gastrointestinal hormones/neurotransmitters and growth factors can activate P21 activated kinase 2 in pancreatic acinar cells by novel mechanisms .

Example answer:
{"entities": [{"text": "Gastrointestinal", "type": "ChemicalEntity"}, {"text": "P21 activated kinase 2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These data suggest that pilocarpine produced antiarrhythmic actions on arrhythmic rat and guinea pig models induced by aconitine or ouabain via stimulating the cardiac M ( 3 ) -mAChR .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "M ( 3 ) -mAChR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Calbindin-D28k ( CB ) , one of the major calcium-binding and buffering proteins , has a critical role in preventing a neuronal death as well as maintaining calcium homeostasis .

Example answer:
{"entities": [{"text": "Calbindin-D28k", "type": "GeneOrGeneProduct"}, {"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "neuronal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "calcium", "type": "ChemicalEntity"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: We used rat pancreatic acini to explore the ability of GI-hormones/neurotransmitters/growth-factors to activate Group-I-PAKs and the signaling cascades involved .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "Group-I-PAKs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Exposure to azathioprine ( > or =2 microg/mL ) for 48 hours increased cytosolic Ca2+ activity and annexin V binding and decreased forward scatter .

Example answer:
{"entities": [{"text": "azathioprine", "type": "ChemicalEntity"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This study was designed to evaluate the effects of pilocarpine and explore the underlying ionic mechanism , using both aconitine-induced rat and ouabain-induced guinea pig arrhythmia models .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "aconitine-induced", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "ouabain-induced", "type": "ChemicalEntity"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: [ Ca ( 2+ ) ] ( i ) overload induced by aconitine or ouabain was reduced in isolated myocytes pretreated with pilocarpine .

Example answer:
{"entities": [{"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Input:
Sentence: In this study , we explored the importance of pathological Ca ( 2+ ) signaling in aconitine poisoning in vitro and in vivo .

## Item biored:test:814
Example input:
Sentence: Consistently , LKB1 ( endo-/- ) mouse tissues including the lung , skin , kidney and liver showed increased vascular permeability .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: The facilitative GLUT inhibitor cytochalasin B , but not the sodium-dependent glucose cotransport inhibitor phloridzin , prevented overload-induced uptake demonstrating that GLUTs mediate this effect .

Example answer:
{"entities": [{"text": "GLUT", "type": "GeneOrGeneProduct"}, {"text": "cytochalasin B", "type": "ChemicalEntity"}, {"text": "sodium-dependent", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "phloridzin", "type": "ChemicalEntity"}, {"text": "GLUTs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: EP4 mediated barrier-protective effects of PGA2 by activating Rap1/Rac1 GTPase and protein kinase A targets at cell adhesions and cytoskeleton : VE-cadherin , p120-catenin , ZO-1 , cortactin , and VASP .

Example answer:
{"entities": [{"text": "EP4", "type": "GeneOrGeneProduct"}, {"text": "PGA2", "type": "ChemicalEntity"}, {"text": "Rap1/Rac1 GTPase", "type": "GeneOrGeneProduct"}, {"text": "protein kinase A", "type": "GeneOrGeneProduct"}, {"text": "VE-cadherin", "type": "GeneOrGeneProduct"}, {"text": "p120-catenin", "type": "GeneOrGeneProduct"}, {"text": "ZO-1", "type": "GeneOrGeneProduct"}, {"text": "cortactin", "type": "GeneOrGeneProduct"}, {"text": "VASP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Taking into account that the sarcolemmal integrity is stabilized by the dystrophin-glycoprotein complex ( DGC ) that connects actin and laminin in contractile machinery and extracellular matrix and by integrins , this study tests the hypothesis that isoproterenol affects sarcolemmal stability through changes in the DGC and integrins .

Example answer:
{"entities": [{"text": "dystrophin-glycoprotein", "type": "GeneOrGeneProduct"}, {"text": "actin", "type": "GeneOrGeneProduct"}, {"text": "laminin", "type": "GeneOrGeneProduct"}, {"text": "isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: PGA2 also suppressed LPS-induced inflammatory signaling by inhibiting the NFkB pathway and expression of EC adhesion molecules ICAM1 and VCAM1 .

Example answer:
{"entities": [{"text": "PGA2", "type": "ChemicalEntity"}, {"text": "LPS-induced", "type": "ChemicalEntity"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkB", "type": "GeneOrGeneProduct"}, {"text": "EC adhesion molecules", "type": "GeneOrGeneProduct"}, {"text": "ICAM1", "type": "GeneOrGeneProduct"}, {"text": "VCAM1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: In vivo , PGA2 was protective in two distinct models of acute lung injury ( ALI ) : LPS-induced inflammatory injury and two-hit ALI caused by suboptimal mechanical ventilation and injection of thrombin receptor-activating peptide .

Example answer:
{"entities": [{"text": "PGA2", "type": "ChemicalEntity"}, {"text": "acute lung injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LPS-induced", "type": "ChemicalEntity"}, {"text": "inflammatory injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thrombin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: PGA2 enhanced the EC barrier and protected against barrier dysfunction caused by vasoactive peptide thrombin and proinflammatory bacterial wall lipopolysaccharide ( LPS ) .

Example answer:
{"entities": [{"text": "PGA2", "type": "ChemicalEntity"}, {"text": "thrombin", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipopolysaccharide", "type": "ChemicalEntity"}, {"text": "LPS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Interestingly , DCs that were co-treated with cisplatin and lipopolysaccharide ( LPS ) exhibited a decreased immunostimulatory capacity for inducing the proliferation of Th1- and Th17-type T cells ; instead , these DCs contributed to Th2-type T cell immunity .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "lipopolysaccharide", "type": "ChemicalEntity"}, {"text": "LPS", "type": "ChemicalEntity"}]}

Input:
Sentence: CMCS could protect LSECs from injury and maintain the microvasculature integration in acute injured liver of mice induced by LPS/D-GalN .

## Item biored:test:852
Example input:
Sentence: This study was designed to evaluate the alterations in offspring rat cerebellum induced by maternal exposure to carmustine- [ 1,3-bis ( 2-chloroethyl ) -1-nitrosoure ] ( BCNU ) and to investigate the effects of exogenous melatonin upon cerebellar BCNU-induced cortical dysplasia , using histological and biochemical analyses .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "carmustine-", "type": "ChemicalEntity"}, {"text": "1,3-bis ( 2-chloroethyl ) -1-nitrosoure", "type": "ChemicalEntity"}, {"text": "BCNU", "type": "ChemicalEntity"}, {"text": "melatonin", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "cortical dysplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Calbindin-D28k ( CB ) , one of the major calcium-binding and buffering proteins , has a critical role in preventing a neuronal death as well as maintaining calcium homeostasis .

Example answer:
{"entities": [{"text": "Calbindin-D28k", "type": "GeneOrGeneProduct"}, {"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "neuronal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "calcium", "type": "ChemicalEntity"}]}

Example input:
Sentence: The effect of azathioprine on both annexin V binding and forward scatter was significantly blunted in the nominal absence of extracellular Ca2+ .

Example answer:
{"entities": [{"text": "azathioprine", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Thus , CAA directly reacts with cellular protein and non-protein thiols , mediating its toxicity on hRPTEC .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}, {"text": "thiols", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hRPTEC", "type": "CellLine"}]}

Example input:
Sentence: RESULTS : Exposure to azathioprine ( > or =2 microg/mL ) for 48 hours increased cytosolic Ca2+ activity and annexin V binding and decreased forward scatter .

Example answer:
{"entities": [{"text": "azathioprine", "type": "ChemicalEntity"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These data suggest that pilocarpine produced antiarrhythmic actions on arrhythmic rat and guinea pig models induced by aconitine or ouabain via stimulating the cardiac M ( 3 ) -mAChR .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "M ( 3 ) -mAChR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Chloroacetaldehyde ( CAA ) is a metabolite of the alkylating agent ifosfamide ( IFO ) and putatively responsible for renal damage following anti-tumor therapy with IFO .

Example answer:
{"entities": [{"text": "Chloroacetaldehyde", "type": "ChemicalEntity"}, {"text": "CAA", "type": "ChemicalEntity"}, {"text": "alkylating agent", "type": "ChemicalEntity"}, {"text": "ifosfamide", "type": "ChemicalEntity"}, {"text": "IFO", "type": "ChemicalEntity"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study was designed to evaluate the effects of pilocarpine and explore the underlying ionic mechanism , using both aconitine-induced rat and ouabain-induced guinea pig arrhythmia models .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "aconitine-induced", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "ouabain-induced", "type": "ChemicalEntity"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: [ Ca ( 2+ ) ] ( i ) overload induced by aconitine or ouabain was reduced in isolated myocytes pretreated with pilocarpine .

Example answer:
{"entities": [{"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Input:
Sentence: However , no reports are available on the role of Ca ( 2+ ) in aconitine poisoning .

## Item biored:test:836
Example input:
Sentence: We suggest that trazodone ( 5 , 10 and 20 mg/kg ) , by blocking the 5-HT 2C receptors , releases the nigrostriatal DAergic neurons from tonic inhibition caused by 5-HT , and thereby potentiates dexamphetamine stereotypy and antagonizes haloperidol catalepsy .

Example answer:
{"entities": [{"text": "5-HT 2C", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : We found that cocaine dose-dependently increased anxiety-like behavior in control ( Dbh +/- ) mice , as measured by a decrease in open arm exploration .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "anxiety-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Methamphetamine ( METH ) damages dopamine ( DA ) nerve endings by a process that has been linked to microglial activation but the signaling pathways that mediate this response have not yet been delineated .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}]}

Example input:
Sentence: It is widely believed that dopamine ( DA ) mediates methamphetamine ( METH ) -induced toxicity to brain dopaminergic neurons , because drugs that interfere with DA neurotransmission decrease toxicity , whereas drugs that increase DA neurotransmission enhance toxicity .

Example answer:
{"entities": [{"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In experiments using specific adrenergic antagonists , we found that pretreatment with the beta-adrenergic receptor antagonist propranolol blocked cocaine-induced anxiety-like behavior in Dbh +/- and wild-type C57BL6/J mice , while the alpha ( 1 ) antagonist prazosin and the alpha ( 2 ) antagonist yohimbine had no effect .

Example answer:
{"entities": [{"text": "adrenergic antagonists", "type": "ChemicalEntity"}, {"text": "beta-adrenergic receptor", "type": "GeneOrGeneProduct"}, {"text": "propranolol", "type": "ChemicalEntity"}, {"text": "cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "alpha ( 1 )", "type": "GeneOrGeneProduct"}, {"text": "prazosin", "type": "ChemicalEntity"}, {"text": "alpha ( 2 )", "type": "GeneOrGeneProduct"}, {"text": "yohimbine", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , we demonstrate that mice genetically engineered to have unilateral brain DA deficits develop METH-induced dopaminergic deficits that are of comparable magnitude on both sides of the brain .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "dopaminergic deficits", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The Dbh -/- mice had normal baseline performance in the EPM but were completely resistant to the anxiogenic effects of cocaine .

Example answer:
{"entities": [{"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : In this study , we evaluated the performance of dopamine beta-hydroxylase knockout ( Dbh -/- ) mice , which lack norepinephrine ( NE ) , in the elevated plus maze ( EPM ) to examine the contribution of noradrenergic signaling to cocaine-induced anxiety .

Example answer:
{"entities": [{"text": "dopamine beta-hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "norepinephrine", "type": "ChemicalEntity"}, {"text": "NE", "type": "ChemicalEntity"}, {"text": "cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "disulfiram", "type": "ChemicalEntity"}, {"text": "dopamine beta-hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "DBH", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Effects of dehydroepiandrosterone in amphetamine-induced schizophrenia models in mice .

## Item biored:test:912
Example input:
Sentence: The Shh ( CreERT2/+ ) ; b-catenin ( flox ( ex3 ) /+ ) ; BmprIA ( flox/- ) mutants displayed partial restoration of URS elongation compared with the b-catenin GOF mutants .

Example answer:
{"entities": [{"text": "Shh", "type": "GeneOrGeneProduct"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "BmprIA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Skin biopsy revealed widening of intercellular spaces in the epidermis and a reduced number of small , poorly formed desmosomes .

Example answer:
{"entities": []}

Example input:
Sentence: Striatal microglia expressing eGFP constitutively show morphological changes after METH that are characteristic of activation .

Example answer:
{"entities": [{"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}]}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Transmission electron microscopy showed that fibroblasts carrying the c.474delA mutation form typical caveolae .

Example answer:
{"entities": [{"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: Transmission electron microscopy revealed the enlargement of smooth endoplasmic reticulum and the presence of intracytoplasmic vacuoles .

Example answer:
{"entities": []}

Example input:
Sentence: It could be proved by the observation of a positive stain reaction and the enlarged collagen fibers as well as hyperplastic fibroblasts under microscopes .

Example answer:
{"entities": [{"text": "collagen", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The fetal kidneys in the PCE group displayed an enlarged Bowman 's space and a shrunken glomerular tuft , accompanied by a reduced cortex width and an increase in the nephrogenic zone/cortical zone ratio .

Example answer:
{"entities": []}

Example input:
Sentence: Both b-catenin loss- and gain-of-function ( LOF and GOF ) mutants displayed abnormal clefts in the perineal region and hypoplastic elongation of the URS .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "hypoplastic", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Those defects compromised proper ridge cell elongation into a flattened epithelial morphology , resulting in thickened MFF edges .

## Item biored:test:863
Example input:
Sentence: Diabetes can be induced in LEW.1WR1 weanling rats challenged with virus or with the viral mimetic polyinosinic : polycytidylic acid ( poly I : C ) .

Example answer:
{"entities": [{"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "polyinosinic : polycytidylic acid", "type": "ChemicalEntity"}, {"text": "poly I : C", "type": "ChemicalEntity"}]}

Example input:
Sentence: IFNAR1 deficiency significantly delayed the onset and frequency of diabetes and greatly reduced the intensity of insulitis after poly I : C treatment .

Example answer:
{"entities": [{"text": "IFNAR1", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "poly I : C", "type": "ChemicalEntity"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In contrast , mPGES-1 -/- mice were largely resistant to lithium-induced polyuria and a urine concentrating defect , accompanied by nearly complete blockade of high urine PGE ( 2 ) and cAMP output .

Example answer:
{"entities": [{"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "cAMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mice lacking mPGES-1 are resistant to lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cyclooxygenase-2 activity is required for the development of lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Cyclooxygenase-2", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that mPGES-1-derived PGE ( 2 ) mediates lithium-induced polyuria likely via inhibition of AQP2 and NKCC2 expression .

Example answer:
{"entities": [{"text": "mPGES-1-derived", "type": "GeneOrGeneProduct"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Absence of PKC-alpha attenuates lithium-induced nephrogenic diabetes insipidus .

## Item biored:test:916
Example input:
Sentence: Continuous ESCRT-III remodelling by subunit turnover might facilitate shape adaptions to variable membrane geometries , with broad implications for diverse cellular processes .

Example answer:
{"entities": [{"text": "ESCRT-III", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We modulated the b-catenin gene conditionally in endodermal epithelia by utilizing tamoxifen-inducible Cre driver line ( Shh ( CreERT2 ) ) .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "tamoxifen-inducible", "type": "ChemicalEntity"}, {"text": "Shh", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Conditionally deleting one copy of FGF receptor 2 ( FGFR2 ) in adult mouse airway basal cells results in self-renewal and differentiation phenotypes .

Example answer:
{"entities": [{"text": "FGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "FGFR2", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: Activation of the fibroblast growth factor ( FGF ) signaling pathway induces the corneal epithelial cells to proliferate and the lens epithelial cells to exit the cell cycle .

Example answer:
{"entities": [{"text": "fibroblast growth factor", "type": "GeneOrGeneProduct"}, {"text": "FGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TNF-alpha or conditioned media ( CM ) of TNF-alpha-stimulated C4-2B cells upregulated BMP-2 and BMP-dependent Smad transcripts and inhibited receptor activator of NF-kappaB ligand transcripts in RAW 264.7 preosteoclast cells , respectively , implying that this factor may contribute to suppression of osteoclastogenesis via direct and paracrine mechanisms .

Example answer:
{"entities": [{"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha-stimulated", "type": "GeneOrGeneProduct"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "BMP-2", "type": "GeneOrGeneProduct"}, {"text": "BMP-dependent", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "receptor activator of NF-kappaB ligand", "type": "GeneOrGeneProduct"}, {"text": "RAW 264.7", "type": "CellLine"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Striatal microglia expressing eGFP constitutively show morphological changes after METH that are characteristic of activation .

Example answer:
{"entities": [{"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}]}

Example input:
Sentence: This was preceded by altered nephrin expression , supporting its pivotal role in podocyte morphology .

Example answer:
{"entities": [{"text": "nephrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In mammary epithelial cells , Star-PAP knockdown partially transformed these cells and induced them to undergo epithelial-mesenchymal transition ( EMT ) .

Example answer:
{"entities": [{"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In contrast , CM of TNF-alpha-stimulate or BMP2-stimulated C4-2B cells induced in vitro mineralization of MC3T3-E1 osteoblast cells in a BMP-2-dependent and NF-kappaB-dependent manner , respectively .

Example answer:
{"entities": [{"text": "TNF-alpha-stimulate", "type": "GeneOrGeneProduct"}, {"text": "BMP2-stimulated", "type": "GeneOrGeneProduct"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "MC3T3-E1", "type": "CellLine"}, {"text": "BMP-2-dependent", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB-dependent", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Furthermore , our findings demonstrated that successive , coordinated ridge cell shape changes drive apical MFF development , making MFF ridge cells a valuable model for investigating how the coordinated regulation of cell polarity and cell shape changes serves as a crucial mechanism of epithelial morphogenesis .

## Item biored:test:876
Example input:
Sentence: LF prevented body weight loss and significantly reduced the elevated plasma H2O2 and increased FRAP values .

Example answer:
{"entities": [{"text": "LF", "type": "GeneOrGeneProduct"}, {"text": "weight loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "H2O2", "type": "ChemicalEntity"}]}

Example input:
Sentence: Spirulina lipopolysaccharides inhibit tumor growth in a Toll-like receptor 4-dependent manner by altering the cytokine milieu from interleukin-17/interleukin-23 to interferon-g. Th17 cells and the cytokine they produce , interleukin ( IL ) -17 , play an important role in tumor progression in humans and in mice .

Example answer:
{"entities": [{"text": "Spirulina", "type": "OrganismTaxon"}, {"text": "lipopolysaccharides", "type": "ChemicalEntity"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Toll-like receptor", "type": "GeneOrGeneProduct"}, {"text": "interleukin-17/interleukin-23", "type": "GeneOrGeneProduct"}, {"text": "interferon-g.", "type": "GeneOrGeneProduct"}, {"text": "interleukin ( IL ) -17", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: TIPE2 Inhibits Lung Cancer Growth Attributing to Promotion of Apoptosis by Regulating Some Apoptotic Molecules Expression .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "Lung Cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Consistent with this premise , patient leukemic cells with relatively high levels of OPRM1 are more sensitive to L-asparaginase treatment compared to OPRM1-depleted leukemic cells , further indicating that OPRM1 loss has a crucial role in L-asparaginase resistance in leukemic patients .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Finally , the inflammatory infiltration of alveolar and interstitial cells and the destruction of lung structure were significantly attenuated in the mide administered Bach1 siRNA compared with those in the BLM group .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "BLM", "type": "ChemicalEntity"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In vivo , PGA2 was protective in two distinct models of acute lung injury ( ALI ) : LPS-induced inflammatory injury and two-hit ALI caused by suboptimal mechanical ventilation and injection of thrombin receptor-activating peptide .

Example answer:
{"entities": [{"text": "PGA2", "type": "ChemicalEntity"}, {"text": "acute lung injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LPS-induced", "type": "ChemicalEntity"}, {"text": "inflammatory injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thrombin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The ability of oral Leu to increase protein synthesis and mTOR kinase after 1 h was largely prevented in sepsis .

Example answer:
{"entities": [{"text": "Leu", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The cytokine leukemia inhibitory factor ( LIF ) is essential for rendering the uterus receptive for blastocyst implantation .

Example answer:
{"entities": [{"text": "leukemia inhibitory factor", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Leukemia inhibitory factor protects the lung during respiratory syncytial viral infection .

## Item biored:test:834
Example input:
Sentence: CONCLUSION : In patients with FHF and cerebral edema from acetaminophen overdose , prolonged therapeutic hypothermia could potentially be used as a life saving therapy and a bridge to hepatic and neurological recovery .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: At dose levels of ( + ) -propranolol which attenuated the responses to isoprenaline , there was a significant prolongation of the PR interval of the electrocardiogram.3 .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol alone decreased left ventricular systolic pressure and myocardial contractility indexed as LVdp/dtmax and LVdp/dtmin .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The incidence of discontinuations for hypertension-related and oedema-related AEs were significantly higher with etoricoxib ( 2.5 % and 1.1 % respectively ) compared with diclofenac ( 1.5 % and 0.4 % respectively ; p < 0.001 for hypertension and p < 0.01 for oedema ) .

Example answer:
{"entities": [{"text": "hypertension-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both isomers of propranolol were also capable of reversing ventricular tachycardia caused by ouabain in anaesthetized cats and dogs .

Example answer:
{"entities": [{"text": "propranolol", "type": "ChemicalEntity"}, {"text": "ventricular tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "cats", "type": "OrganismTaxon"}, {"text": "dogs", "type": "OrganismTaxon"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : There were more incidents of bradycardia in subjects treated with clonidine compared with those not treated with clonidine ( 17.5 % versus 3.4 % ; p =.02 ) , but no other significant group differences regarding electrocardiogram and other cardiovascular outcomes .

Example answer:
{"entities": [{"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Physicians prescribing clonidine should monitor for bradycardia and advise patients about the high likelihood of initial drowsiness .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "drowsiness", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSIONS : Severe hypotension and bradycardia occur at similar prevalence in neurocritical care patients who receive dexmedetomidine or propofol .

## Item biored:test:854
Example input:
Sentence: Overload was induced in mouse plantaris muscle by unilateral synergist ablation .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: These rats also showed declines in left ventricular systolic pressure , maximum and minimum rate of developed left ventricular pressure , and elevation of left ventricular end-diastolic pressure and ST-segment .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Field potential duration ( FPD ) in human-induced pluripotent stem cell-derived cardiomyocytes ( hiPS-CMs ) , which can express QT interval in an electrocardiogram , is reported to be a useful tool to predict K ( + ) channel and Ca ( 2+ ) channel blocker effects on QT interval .

Example answer:
{"entities": [{"text": "human-induced", "type": "OrganismTaxon"}, {"text": "K ( + ) channel and Ca ( 2+ ) channel blocker", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion , HFD-induced obese rats are highly sensitized to doxorubicin-induced cardiotoxicity by substantially downregulating cardiac mitochondrial ATP generation , increasing oxidative stress and downregulating the JAK/STAT3 pathway .

Example answer:
{"entities": [{"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "JAK/STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mechanistic studies revealed that OB rats are sensitized due to : ( 1 ) higher oxyradical stress leading to upregulation of uncoupling proteins 2 and 3 , ( 2 ) downregulation of cardiac peroxisome proliferators activated receptor-alpha , ( 3 ) decreased plasma adiponectin levels , ( 4 ) decreased cardiac fatty-acid oxidation ( 666.9+/-14.0 nmol/min/g heart in ND versus 400.2+/-11.8 nmol/min/g heart in OB ) , ( 5 ) decreased mitochondrial AMP-alpha2 protein kinase , and ( 6 ) 86 % drop in cardiac ATP levels accompanied by decreased ATP/ADP ratio after doxorubicin administration .

Example answer:
{"entities": [{"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "uncoupling proteins 2 and 3", "type": "GeneOrGeneProduct"}, {"text": "peroxisome proliferators activated receptor-alpha", "type": "GeneOrGeneProduct"}, {"text": "adiponectin", "type": "GeneOrGeneProduct"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "AMP-alpha2 protein kinase", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "ATP/ADP", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The cardiac toxicity intrinsically associated with the aggressive chemotherapy employed could function as a triggering factor for the arrhythmia in the predisposed myocardium of this patient .

Example answer:
{"entities": [{"text": "cardiac toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: Subcutaneous injection of ISPH ( 200 mg/kg body weight in 1 ml saline ) to rats for 2 consecutive days caused myocardial damage in rat heart , which was determined by the increased activity of serum lactate dehydrogenase ( LDH ) and creatine phosphokinase isoenzymes ( CK-MB ) , increased uric acid level and reduced plasma iron binding capacity .

Example answer:
{"entities": [{"text": "ISPH", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "LDH", "type": "GeneOrGeneProduct"}, {"text": "creatine phosphokinase isoenzymes", "type": "GeneOrGeneProduct"}, {"text": "CK-MB", "type": "GeneOrGeneProduct"}, {"text": "uric acid", "type": "ChemicalEntity"}, {"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: [ Ca ( 2+ ) ] ( i ) overload induced by aconitine or ouabain was reduced in isolated myocytes pretreated with pilocarpine .

Example answer:
{"entities": [{"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Input:
Sentence: We found that Ca ( 2+ ) overload lead to accelerated beating rhythm in adult rat ventricular myocytes and caused arrhythmia in conscious freely moving rats .

## Item biored:test:905
Example input:
Sentence: Thus , immunosuppression has increased the risk of infections by HPVs , predominantly epidermodysplasia verruciformis , speculated to play a role in skin cancer development .

Example answer:
{"entities": [{"text": "infections", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HPVs", "type": "OrganismTaxon"}, {"text": "epidermodysplasia verruciformis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The development of skin cancer is a complex multistage phenomenon involving three distinct stages exemplified by initiation , promotion and progression stages .

Example answer:
{"entities": [{"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Skin biopsy revealed widening of intercellular spaces in the epidermis and a reduced number of small , poorly formed desmosomes .

Example answer:
{"entities": []}

Example input:
Sentence: In addition , affected males display facial similarities that can help the diagnosis .

Example answer:
{"entities": []}

Example input:
Sentence: Over the years , changes in lifestyle has led to a significant increase in the amount of UV radiation that people receive , and this consequently has led to a surge in the incidence of skin cancer .

Example answer:
{"entities": [{"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The diagnosis of P and N-induced skin reactions was based in vivo challenge .

Example answer:
{"entities": [{"text": "P", "type": "ChemicalEntity"}, {"text": "N-induced", "type": "ChemicalEntity"}, {"text": "skin reactions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It is widely used in folk medicine to treat skin diseases in both humans and animals as well as the seed decoction has been used to treat diarrheas and inflammatory diseases .

Example answer:
{"entities": [{"text": "skin diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "diarrheas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory diseases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We suggest that the use of skin care products supplemented with proven chemopreventive agents in conjunction with the use of sunscreens along with educational efforts may be an effective strategy for reducing UV-induced photodamage and skin cancer in humans .

Example answer:
{"entities": [{"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Many such agents have also found a place in skin care products .

Example answer:
{"entities": []}

Example input:
Sentence: Photochemoprevention has been appreciated as a viable approach to reduce the occurrence of skin cancer and in recent years , the use of agents , especially botanical antioxidants , present in the common diet and beverages consumed by human population have gained considerable attention as photochemopreventive agents for human use .

Example answer:
{"entities": [{"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}]}

Input:
Sentence: Skin disorders are widespread , but available treatments are limited .

## Item biored:test:866
Example input:
Sentence: Diabetes can be induced in LEW.1WR1 weanling rats challenged with virus or with the viral mimetic polyinosinic : polycytidylic acid ( poly I : C ) .

Example answer:
{"entities": [{"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "polyinosinic : polycytidylic acid", "type": "ChemicalEntity"}, {"text": "poly I : C", "type": "ChemicalEntity"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: A 2-wk administration of LiCl ( 4 mmol.kg ( -1 ) .day ( -1 ) ip ) in mPGES-1 +/+ mice led to a marked polyuria with hyposmotic urine .

Example answer:
{"entities": [{"text": "LiCl", "type": "ChemicalEntity"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In contrast , mPGES-1 -/- mice were largely resistant to lithium-induced polyuria and a urine concentrating defect , accompanied by nearly complete blockade of high urine PGE ( 2 ) and cAMP output .

Example answer:
{"entities": [{"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "cAMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mice lacking mPGES-1 are resistant to lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cyclooxygenase-2 activity is required for the development of lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Cyclooxygenase-2", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that mPGES-1-derived PGE ( 2 ) mediates lithium-induced polyuria likely via inhibition of AQP2 and NKCC2 expression .

Example answer:
{"entities": [{"text": "mPGES-1-derived", "type": "GeneOrGeneProduct"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Targeting an alternative signaling pathway , such as PKC-mediated signaling , may be an effective method of treating lithium-induced polyuria .

## Item biored:test:847
Example input:
Sentence: We also investigated whether trazodone induces catalepsy in rats .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Nontoxic doses of dexrazoxane reduced myelosuppression and weight loss from daunorubicin and etoposide in mice and antagonized their antiproliferative effects in the colony assay ; however , dexrazoxane neither reduced myelosuppression , weight loss , nor the in vitro cytotoxicity from doxorubicin .

Example answer:
{"entities": [{"text": "dexrazoxane", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "weight loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "daunorubicin", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cytotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: did not induce catalepsy , and did not antagonize apomorphine ( 1.5 and 3 mg/kg ) stereotypy and apomorphine ( 0.05 mg/kg ) -induced catalepsy .

Example answer:
{"entities": []}

Example input:
Sentence: Chronic exposure to PCPA alone significantly decreased locomotor activity and increased irritability but had no effect on sexual behavior , partner preference , or aggression .

Example answer:
{"entities": [{"text": "PCPA", "type": "ChemicalEntity"}, {"text": "irritability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aggression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We suggest that trazodone ( 5 , 10 and 20 mg/kg ) , by blocking the 5-HT 2C receptors , releases the nigrostriatal DAergic neurons from tonic inhibition caused by 5-HT , and thereby potentiates dexamphetamine stereotypy and antagonizes haloperidol catalepsy .

Example answer:
{"entities": [{"text": "5-HT 2C", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : The effect of pretreatment with trazodone on dexamphetamine- and apomorphine-induced oral stereotypies , on catalepsy induced by haloperidol and apomorphine ( 0.05 mg/kg , i.p .

Example answer:
{"entities": [{"text": "trazodone", "type": "ChemicalEntity"}, {"text": "dexamphetamine-", "type": "ChemicalEntity"}, {"text": "apomorphine-induced", "type": "ChemicalEntity"}, {"text": "oral stereotypies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "apomorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : We found that cocaine dose-dependently increased anxiety-like behavior in control ( Dbh +/- ) mice , as measured by a decrease in open arm exploration .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "anxiety-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: These findings suggest that glutamate-mediated mechanisms in the neural circuits at the IC level influence haloperidol-induced catalepsy and participate in the regulation of motor activity .

Example answer:
{"entities": [{"text": "glutamate-mediated", "type": "ChemicalEntity"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSION : We observed that DHEA reduced locomotor activity and increased catalepsy at both doses , while it had no effect on climbing behavior .

## Item biored:test:882
Example input:
Sentence: In collagenase-induced ICH mice , the protection of etifoxine was associated with reduced leukocyte infiltration into the brain and microglial production of IL-6 and TNF-a .

Example answer:
{"entities": [{"text": "collagenase-induced", "type": "ChemicalEntity"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "etifoxine", "type": "ChemicalEntity"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The data suggest that in VIP ( -/- ) mice with bladder inflammation , inflammatory mediators are increased above that observed in WT with CYP .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This effect was dependent on the production of IL-10 from DCs , as neither DCs isolated from IL-10-/- mice nor IL-10-neutralized DCs generated tolerogenic DCs .

Example answer:
{"entities": [{"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "IL-10-/-", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "IL-10-neutralized", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Exaggerated expression of inflammatory mediators in vasoactive intestinal polypeptide knockout ( VIP-/- ) mice with cyclophosphamide ( CYP ) -induced cystitis .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vasoactive intestinal polypeptide", "type": "GeneOrGeneProduct"}, {"text": "VIP-/-", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CYP", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Given VIP 's role as an anti-inflammatory mediator , we hypothesized that VIP ( -/- ) mice would exhibit enhanced inflammatory mediator expression after cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A mouse model of BLM-induced PF was established , and Bach1 siRNA ( 1x109 pfu ) was administered to the mice via the tail vein .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "BLM-induced", "type": "ChemicalEntity"}, {"text": "PF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Viruses were evaluated for replication in SCID mice transplanted with human hepatoma cells ( SCID-HuH-7 mice ) , in mosquitoes , and in rhesus monkeys .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "hepatoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCID-HuH-7", "type": "CellLine"}, {"text": "rhesus monkeys", "type": "OrganismTaxon"}]}

Example input:
Sentence: A mouse inflammatory cytokine and receptor RT2 profiler array was used to determine regulated transcripts in the urinary bladder of wild type ( WT ) and VIP ( -/- ) mice with or without CYP-induced cystitis ( 150 mg/kg ; i.p .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CYP-induced", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: These RSV-inducible cytokines were also observed in the airways of mice during an infection .

## Item biored:test:908
Example input:
Sentence: RESULTS : The patient 's GR gene had a heterozygotic mutation ( G -- > A ) at nucleotide position 2141 ( exon 8 ) , which resulted in substitution of arginine by glutamine at amino acid position 714 in the ligand-binding domain ( LBD ) of the GR alpha .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "( G -- > A ) at nucleotide position 2141", "type": "SequenceVariant"}, {"text": "arginine by glutamine at amino acid position 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We modulated the b-catenin gene conditionally in endodermal epithelia by utilizing tamoxifen-inducible Cre driver line ( Shh ( CreERT2 ) ) .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "tamoxifen-inducible", "type": "ChemicalEntity"}, {"text": "Shh", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genomic DNA was extracted from peripheral leukocytes from six affected and three unaffected members of a family with lattice corneal dystrophy type I. Exon 4 of the transforming growth factor-induced gene ( TGFBI ) was screened for the most frequent mutation , R124C , in the proband by sequencing .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor-induced gene", "type": "GeneOrGeneProduct"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "R124C", "type": "SequenceVariant"}]}

Example input:
Sentence: TS enhancer region , 3R G > C single nucleotide polymorphism ( SNP ) , and TS 1494del6 polymorphisms were assessed in both fresh-frozen normal mucosa and tumor .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "G > C", "type": "SequenceVariant"}, {"text": "1494del6", "type": "SequenceVariant"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results indicate that some ARM phenotypes in the b-catenin GOF mutants were caused by abnormal Bmp signaling .

Example answer:
{"entities": [{"text": "ARM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These 24 GIST were more commonly mutated at 7 genes : ARID1B , ATR , FGFR1 , LTK , SUFU , PARK2 and ZNF217 .

Example answer:
{"entities": [{"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARID1B", "type": "GeneOrGeneProduct"}, {"text": "ATR", "type": "GeneOrGeneProduct"}, {"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "LTK", "type": "GeneOrGeneProduct"}, {"text": "SUFU", "type": "GeneOrGeneProduct"}, {"text": "PARK2", "type": "GeneOrGeneProduct"}, {"text": "ZNF217", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In vivo selection for skin-specific expression of gene-break transposon ( GBT ) mutant lines identified eleven new , revertible GBT alleles of genes involved in skin development .

## Item biored:test:887
Example input:
Sentence: PRMT5 regulated the production of inflammatory factors , cell proliferation , migration and invasion of RA FLS , which was mediated by the NF-kB and AKT pathways .

Example answer:
{"entities": [{"text": "PRMT5", "type": "GeneOrGeneProduct"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kB", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In vitro , the Vps2/Vps24 subunits of ESCRT-III formed side-by-side filaments with Snf7 and inhibited further polymerization , but the growth inhibition was alleviated by the addition of Vps4 and ATP .

Example answer:
{"entities": [{"text": "Vps2/Vps24", "type": "GeneOrGeneProduct"}, {"text": "ESCRT-III", "type": "GeneOrGeneProduct"}, {"text": "Snf7", "type": "GeneOrGeneProduct"}, {"text": "Vps4", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}]}

Example input:
Sentence: The binding of mTOR , PRAS40 and RagC to raptor did not differ for control and septic muscle in the basal condition ; however , the Leu-induced decrease in PRAS40 raptor and increase in RagC raptor seen in control muscle was absent in sepsis .

Example answer:
{"entities": [{"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "PRAS40", "type": "GeneOrGeneProduct"}, {"text": "RagC", "type": "GeneOrGeneProduct"}, {"text": "raptor", "type": "GeneOrGeneProduct"}, {"text": "Leu-induced", "type": "ChemicalEntity"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Gene expression analysis revealed that rs10954213 exerted the greatest influence on IRF5 transcript levels .

Example answer:
{"entities": [{"text": "rs10954213", "type": "SequenceVariant"}, {"text": "IRF5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In rhesus monkeys , rDEN2Delta30 appeared to be slightly attenuated when compared to the parent virus as measured by duration and peak of viremia and neutralizing antibody induction .

Example answer:
{"entities": [{"text": "rhesus monkeys", "type": "OrganismTaxon"}, {"text": "rDEN2Delta30", "type": "OrganismTaxon"}, {"text": "viremia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thus , immunosuppression has increased the risk of infections by HPVs , predominantly epidermodysplasia verruciformis , speculated to play a role in skin cancer development .

Example answer:
{"entities": [{"text": "infections", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HPVs", "type": "OrganismTaxon"}, {"text": "epidermodysplasia verruciformis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: When the patients were stratified by the SE , the rs729302 A allele was found to confer increased risk to RA in patients that were SE negative ( OR 1.50 , 95 % CI 1.17 to 1.92 , p = 0.001 ) as compared with patients carrying the SE ( OR 1.11 , 95 % CI 0.93 to 1.33 , p = 0.24 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs729302", "type": "SequenceVariant"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These findings indicate that the promoter polymorphism of IRF5 is a genetic factor conferring predisposition to RA , and that it contributes considerably to disease pathogenesis in patients that were SE negative .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Immunohistochemistry and western blotting are used to determine the mechanisms of Sal against RIF .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "RIF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Input:
Sentence: CONCLUSIONS : RSV infection in the epithelium induces a network of immune factors to counter infection , primarily in a RIG-I dependent manner .

## Item biored:test:868
Example input:
Sentence: Urinary sodium excretion reached signficantly lower values in sgk1 ( +/+ ) mice ( 15 +/- 5 mumol/mg crea ) than in sgk1 ( -/- ) mice ( 35 +/- 5 mumol/mg crea ) and was associated with a significantly higher body weight gain in sgk1 ( +/+ ) compared with sgk1 ( -/- ) mice ( +6.6 +/- 0.7 vs. +4.1 +/- 0.8 g ) .

Example answer:
{"entities": [{"text": "sodium", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "weight gain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This shift in balance may contribute to increased bladder dysfunction in VIP ( -/- ) mice with bladder inflammation and altered neurochemical expression in micturition pathways .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: During the course of nephrotic syndrome , serum urea concentrations increased significantly faster in sgk1 ( -/- ) mice than in sgk1 ( +/+ ) mice leading to uremia and a reduced median survival in sgk1 ( -/- ) mice ( 29 vs. 40 days in sgk1 ( +/+ ) mice ) .

Example answer:
{"entities": [{"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "urea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "uremia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 2-wk administration of LiCl ( 4 mmol.kg ( -1 ) .day ( -1 ) ip ) in mPGES-1 +/+ mice led to a marked polyuria with hyposmotic urine .

Example answer:
{"entities": [{"text": "LiCl", "type": "ChemicalEntity"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Compared with WT mice , the liver weight and liver metastatic rate were significantly lower in AT1aKO .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "liver metastatic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A mouse inflammatory cytokine and receptor RT2 profiler array was used to determine regulated transcripts in the urinary bladder of wild type ( WT ) and VIP ( -/- ) mice with or without CYP-induced cystitis ( 150 mg/kg ; i.p .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CYP-induced", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: VIP ( -/- ) mice exhibit altered bladder function and neurochemical properties in micturition pathways after cyclophosphamide ( CYP ) -induced cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CYP", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The data suggest that in VIP ( -/- ) mice with bladder inflammation , inflammatory mediators are increased above that observed in WT with CYP .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CYP treatment significantly ( p < or = 0.001 ) increased expression of CXCL1 and IL-1beta in the urinary bladder of WT and VIP ( -/- ) mice , but expression in VIP ( -/- ) mice with CYP treatment was significantly ( p < or = 0.001 ) greater ( 4.2- to 13-fold increase ) than that observed in WT urinary bladder ( 3.6- to 5-fold increase ) .

Example answer:
{"entities": []}

Input:
Sentence: WT mice had increased urine output and lowered urine osmolality after 3 and 5 days of treatment whereas PKCa KO mice had no change in urine output or concentration .

## Item biored:test:892
Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results indicated that IGF-1R may increase cell viability under hypoxic conditions by promoting autophagy and scavenging ROS production , which is closed with PI3K/Akt/mTOR signaling pathway .

Example answer:
{"entities": [{"text": "IGF-1R", "type": "GeneOrGeneProduct"}, {"text": "hypoxic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "PI3K/Akt/mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A rat model of IUGR was established by PCE , male fetuses and adult offspring at the age of postnatal week 24 were euthanized .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "IUGR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Endothelial NADPH oxidase 4 mediates vascular endothelial growth factor receptor 2-induced intravitreal neovascularization in a rat model of retinopathy of prematurity .

Example answer:
{"entities": [{"text": "NADPH oxidase 4", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor receptor", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "retinopathy of prematurity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mechanistic studies revealed that OB rats are sensitized due to : ( 1 ) higher oxyradical stress leading to upregulation of uncoupling proteins 2 and 3 , ( 2 ) downregulation of cardiac peroxisome proliferators activated receptor-alpha , ( 3 ) decreased plasma adiponectin levels , ( 4 ) decreased cardiac fatty-acid oxidation ( 666.9+/-14.0 nmol/min/g heart in ND versus 400.2+/-11.8 nmol/min/g heart in OB ) , ( 5 ) decreased mitochondrial AMP-alpha2 protein kinase , and ( 6 ) 86 % drop in cardiac ATP levels accompanied by decreased ATP/ADP ratio after doxorubicin administration .

Example answer:
{"entities": [{"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "uncoupling proteins 2 and 3", "type": "GeneOrGeneProduct"}, {"text": "peroxisome proliferators activated receptor-alpha", "type": "GeneOrGeneProduct"}, {"text": "adiponectin", "type": "GeneOrGeneProduct"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "AMP-alpha2 protein kinase", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "ATP/ADP", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Newborn rat pups and dams were placed into an OIR model that cycled oxygen concentration between 50 % and 10 % every 24 h for 14 days , and then were placed in room air ( RA ) for an additional 4 days ( rat OIR model ) .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oxygen", "type": "ChemicalEntity"}]}

Example input:
Sentence: Superoxide dismutase 1 overexpression in mice abolishes maternal diabetes-induced endoplasmic reticulum stress in diabetic embryopathy .

Example answer:
{"entities": [{"text": "Superoxide dismutase 1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "maternal", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "embryopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , rats that experienced SE exhibited CCR2-labeling in populations of hypertrophied astrocytes , especially in CA1 and dentate gyrus .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCR2-labeling", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mouse embryonic fibroblasts exhibiting disruption or overexpression of IGF-1R ( R- cells and R+ cells ) were used to examine the level of apoptosis , autophagy , and production of reactive oxygen species ( ROS ) .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "IGF-1R", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Input:
Sentence: Astrocytes from neonatal rats were treated with oxygen-glucose deprivation ( OGD ) followed by reoxygenation ( OGD/R ) .

## Item biored:test:898
Example input:
Sentence: Knockdown of either NOX4 or STAT3 inhibited VEGF-induced EC proliferation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , Sal treatment significantly decreases the release of inflammatory cytokines and inhibits the TLR4/NF-kappaB and MAPK signaling pathways .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TLR4/NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SB 202190 significantly decreased IDO expression induced by Tat , and this effect was accompanied by a reduction of Tat-induced expression of TNFa , IL-6 , iNOS and SERT .

Example answer:
{"entities": [{"text": "SB 202190", "type": "ChemicalEntity"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "Tat-induced", "type": "GeneOrGeneProduct"}, {"text": "TNFa", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "SERT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: ADAM12 knockdown also diminished ALDEFLUOR ( + ) and CD44 ( hi ) /CD24 ( -/lo ) CSC-enriched populations in vitro and reduced tumorigenesis in mice in vivo .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: It was partially reduced by PKC- or Src-inhibition , but not with PI3K-inhibitors ( wortmannin , LY294002 ) or thapsigargin .

Example answer:
{"entities": [{"text": "PKC-", "type": "GeneOrGeneProduct"}, {"text": "Src-inhibition", "type": "GeneOrGeneProduct"}, {"text": "PI3K-inhibitors", "type": "GeneOrGeneProduct"}, {"text": "wortmannin", "type": "ChemicalEntity"}, {"text": "LY294002", "type": "ChemicalEntity"}, {"text": "thapsigargin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , Sal administration significantly suppresses epithelial-mesenchymal transition ( EMT ) , as evidenced by a decreased expression of alpha-SMA , vimentin , TGF-beta1 , snail , slug , and a largely restored expression of E-cadherin .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "alpha-SMA", "type": "GeneOrGeneProduct"}, {"text": "vimentin", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "snail", "type": "GeneOrGeneProduct"}, {"text": "slug", "type": "GeneOrGeneProduct"}, {"text": "E-cadherin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Tat also induced the synthesis and release of TNFa and IL-6 protein in the supernatant of the slices and increased expression of the inducible isoform of nitric oxide synthase ( iNOS ) and the serotonin transporter ( SERT ) .

Example answer:
{"entities": [{"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "TNFa", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "inducible isoform of nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "SERT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Additionally , Sal also reduces the levels of serum biochemical markers ( serum creatinine , Scr ; blood urea nitrogen , BUN ; and uric acid , UA ) and decreases the release of inflammatory cytokines ( IL-1beta , IL-6 , TNF-alpha ) .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "urea", "type": "ChemicalEntity"}, {"text": "nitrogen", "type": "ChemicalEntity"}, {"text": "uric acid", "type": "ChemicalEntity"}, {"text": "UA", "type": "ChemicalEntity"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Protein level of BDNF was reduced in Dox-treated rat ventricles , whereas BDNF and its receptor tropomyosin-related kinase B ( TrkB ) were markedly up-regulated after BDNF administration .

Example answer:
{"entities": [{"text": "tropomyosin-related kinase", "type": "GeneOrGeneProduct"}, {"text": "(", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TNF-alpha or conditioned media ( CM ) of TNF-alpha-stimulated C4-2B cells upregulated BMP-2 and BMP-dependent Smad transcripts and inhibited receptor activator of NF-kappaB ligand transcripts in RAW 264.7 preosteoclast cells , respectively , implying that this factor may contribute to suppression of osteoclastogenesis via direct and paracrine mechanisms .

Example answer:
{"entities": [{"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha-stimulated", "type": "GeneOrGeneProduct"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "BMP-2", "type": "GeneOrGeneProduct"}, {"text": "BMP-dependent", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "receptor activator of NF-kappaB ligand", "type": "GeneOrGeneProduct"}, {"text": "RAW 264.7", "type": "CellLine"}]}

Input:
Sentence: It also reduced NO/TNF-alpha release .

## Item biored:test:891
Example input:
Sentence: The study investigates if alpha-lipoic acid is neuroprotective against chemotherapy induced neurotoxicity , if mitochondrial damage plays a critical role in toxic neurodegenerative cascade , and if neuroprotective effects of alpha-lipoic acid depend on mitochondria protection .

Example answer:
{"entities": [{"text": "alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "toxic neurodegenerative cascade", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Gene deletion or pharmacological blockade of KCa3.1 protected against SOCE-induced Ca2+ overload and ER stress via the protein kinase B ( AKT ) signaling pathway in astrocytes .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "frataxin", "type": "GeneOrGeneProduct"}]}

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
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: TSPO ligands have shown anti-inflammatory and neuroprotective properties in models of CNS injury .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "CNS injury", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We thus attempted to confirm neuroprotective effects of NSP on astrocytes in the ischemic state and then explored the relative mechanisms .

## Item biored:test:869
Example input:
Sentence: Moreover , CBKOTg mice reduced levels of phosphorylated mitogen-activated protein kinase ( extracellular signal-regulated kinase ) 1/2 and cAMP response element-binding protein at Ser-133 and synaptic molecules such as N-methyl-D-aspartate receptor 1 ( NMDA receptor 1 ) , NMDA receptor 2A , PSD-95 and synaptophysin in the subiculum compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}, {"text": "extracellular signal-regulated kinase ) 1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding protein", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-D-aspartate receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 2A", "type": "GeneOrGeneProduct"}, {"text": "PSD-95", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Compared with WT mice , the liver weight and liver metastatic rate were significantly lower in AT1aKO .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "liver metastatic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that simultaneous overexpression of the mitotic checkpoint protein Mad2 with Kras ( G12D ) or Her2 in mammary glands of adult mice results in mitotic checkpoint overactivation and a delay in tumor onset .

Example answer:
{"entities": [{"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "GeneOrGeneProduct"}, {"text": "Her2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Despite the absence of functional phosphatase and tensin homolog ( PTEN ) protein in Ishikawa cells , PKCalpha knockdown reduced Akt phosphorylation at serine 473 and concomitantly inhibited phosphorylation of the Akt target , glycogen synthase kinase-3beta ( GSK-3beta ) .

Example answer:
{"entities": [{"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "glycogen synthase kinase-3beta", "type": "GeneOrGeneProduct"}, {"text": "GSK-3beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In contrast , the dowregulation of renal medullary NKCC2 expression was significantly attenuated in the -/- mice .

Example answer:
{"entities": [{"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: qRT-PCR detected similar patterns of changes in AQP2 mRNA in the medulla but not in the cortex .

Example answer:
{"entities": [{"text": "AQP2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: Western blot analysis revealed that AQP2 expression in medullary tissues was lowered after 3 and 5 days in WT mice ; however , AQP2 was unchanged in PKCa KO .

## Item biored:test:922
Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: Expression analysis on a cDNA panel from 17 different normal tissues by reverse transcription-PCR ( RT-PCR ) revealed tissue restricted mRNA expression of 2 of the 27 unknown antigens .

Example answer:
{"entities": []}

Example input:
Sentence: RNA sequencing was performed to identify global gene expression changes after ADAM12 knockdown .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RNA sequencing identified a significant overlap between ADAM12- and Epidermal Growth Factor Receptor ( EGFR ) -regulated genes .

Example answer:
{"entities": [{"text": "ADAM12-", "type": "GeneOrGeneProduct"}, {"text": "Epidermal Growth Factor Receptor", "type": "GeneOrGeneProduct"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Gene expression analysis revealed that rs10954213 exerted the greatest influence on IRF5 transcript levels .

Example answer:
{"entities": [{"text": "rs10954213", "type": "SequenceVariant"}, {"text": "IRF5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Five of the forty genes -- ENT3 , IDP3 , JEM1 , ARG2 and HSP82 -- ranked highest in their ability to block alpha-syn-induced reactive oxygen species accumulation , and these five genes were characterized in more detail .

Example answer:
{"entities": [{"text": "ENT3", "type": "GeneOrGeneProduct"}, {"text": "IDP3", "type": "GeneOrGeneProduct"}, {"text": "JEM1", "type": "GeneOrGeneProduct"}, {"text": "ARG2", "type": "GeneOrGeneProduct"}, {"text": "HSP82", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn-induced", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A total of 610 differentially expressed genes ( DEGs ) were revealed in the transcriptome comparison , 297 of which were upregulated and 313 were downregulated in HCC .

Example answer:
{"entities": [{"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Transcriptomics analysis indicated that 617 genes were upregulated and 665 genes were downregulated by PPARa activation ( q value < 0.05 ) .

## Item biored:test:819
Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "fulminant hepatic failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: We herein report the case of a 70-year-old man with 5-FU-induced cardiotoxicity , in whom a high serum level of alpha-fluoro-beta-alanine ( FBAL ) was observed .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "5-FU-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fluoro-beta-alanine", "type": "ChemicalEntity"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prolonged PFS and OS were observed in patients achieving CR and receiving bort-dex a single line of prior therapy .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "bort-dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: This retrospective study investigated the combination of bort ( 1.3 mg/m ( 2 ) on days 1 , 4 , 8 , and 11 every 3 weeks ) and dex ( 20 mg on the day of and the day after bort ) as salvage treatment in 85 patients with R/R MM after prior autologous stem cell transplantation or conventional chemotherapy .

Example answer:
{"entities": [{"text": "bort", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 61-year-old Japanese man with nephrotic syndrome due to focal segmental glomerulosclerosis was initially responding well to steroid therapy .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal segmental glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steroid", "type": "ChemicalEntity"}]}

Example input:
Sentence: Bort-dex was an effective salvage treatment for MM patients , particularly for those in first relapse .

Example answer:
{"entities": [{"text": "Bort-dex", "type": "ChemicalEntity"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Bortezomib and dexamethasone as salvage therapy in patients with relapsed/refractory multiple myeloma : analysis of long-term clinical outcomes .

Example answer:
{"entities": [{"text": "Bortezomib", "type": "ChemicalEntity"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple myeloma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Bortezomib ( bort ) -dexamethasone ( dex ) is an effective therapy for relapsed/refractory ( R/R ) multiple myeloma ( MM ) .

Example answer:
{"entities": [{"text": "Bortezomib", "type": "ChemicalEntity"}, {"text": "bort", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "multiple myeloma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We report a case of a 76-year-old man with Waldenstrom macroglobulinaemia who suffered necrotising fasciitis without neutropenia after the combination treatment with bortezomib , high-dose dexamethasone and rituximab .

## Item biored:test:896
Example input:
Sentence: The growth of breast cancer xenografts in NOD/SCID mice was also inhibited by the doxycycline-induced Star-PAP overexpression .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "doxycycline-induced", "type": "ChemicalEntity"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Knockdowns of NOTCH1 , SOX10 , and their common effector FABP7 had negative effects on each other , inhibited spheroidogenesis , and induced cell death pointing at their essential roles in CSC maintenance .

Example answer:
{"entities": [{"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "FABP7", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The antinociception after morphine ( 3.2 mg/kg ) was increased by co-administration with CNSB002 from 28.0 and 31.7 % to 114.6 and 56.9 % reversal of hyperalgesia in the inflammatory and neuropathic models , respectively ( P < 0.01 ; one-way analysis of variance-significantly greater than either drug given alone ) .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: On the other hand , induction of metallothionein ( MT ) by ZnSO ( 4 ) and its role in neuroprotection has been documented .

Example answer:
{"entities": [{"text": "metallothionein", "type": "ChemicalEntity"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}]}

Example input:
Sentence: Moreover , using RNA interference with small inhibitory RNAs for Sp1 , Sp3 , and Sp4 , we observed that curcumin-dependent inhibition of nuclear factor kappaB ( NF-kappaB ) -dependent genes , such as bcl-2 , survivin , and cyclin D1 , was also due , in part , to loss of Sp proteins .

Example answer:
{"entities": [{"text": "Sp1", "type": "GeneOrGeneProduct"}, {"text": "Sp3", "type": "GeneOrGeneProduct"}, {"text": "Sp4", "type": "GeneOrGeneProduct"}, {"text": "curcumin-dependent", "type": "ChemicalEntity"}, {"text": "nuclear factor kappaB", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "survivin", "type": "GeneOrGeneProduct"}, {"text": "cyclin D1", "type": "GeneOrGeneProduct"}, {"text": "Sp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the present study , we demonstrate that NF-kappaB , whether activated by recombinant human tumor necrosis factor ( TNF ) -alpha or by ectopic expression of the p65 subunit , is involved in extracellular matrix adhesion and invasion of osteotropic PC-3 and C4-2B , but not LNCaP , cells .

Example answer:
{"entities": [{"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tumor necrosis factor ( TNF ) -alpha", "type": "GeneOrGeneProduct"}, {"text": "p65", "type": "GeneOrGeneProduct"}, {"text": "PC-3", "type": "CellLine"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "LNCaP", "type": "CellLine"}]}

Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cocaine", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}, {"text": "nNOS", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVE : This study determined the antihyperalgesic effect of CNSB002 , a sodium channel blocker with antioxidant properties given alone and in combinations with morphine in rat models of inflammatory and neuropathic pain .

Example answer:
{"entities": [{"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "sodium channel blocker", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Nuclear factor kappa B ( NFkappaB ) is a sensor of oxidative stress and participates in memory formation that could be involved in drug toxicity and addiction mechanisms .

Example answer:
{"entities": [{"text": "Nuclear factor kappa B", "type": "GeneOrGeneProduct"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: To verify the cause-and-effect relationship between neuroprotection and the NF-kappaB pathway , a NF-kappaB pathway inhibitor sc3060 was employed to observe the effects of NSP-induced neuroprotection .

## Item biored:test:867
Example input:
Sentence: In a prevention study , rats received 4 days of LF treatment followed by Dex and continued during the test period .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "LF", "type": "GeneOrGeneProduct"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Male Wistar rats were treated by Dex ( 30 u g/kg/day subcutaneously ) or saline for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Hippocampus mice treated with GFC75 plus P400 showed an increase in AChE activity ( 63.30 % ) when compared with seized mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A 2-wk administration of LiCl ( 4 mmol.kg ( -1 ) .day ( -1 ) ip ) in mPGES-1 +/+ mice led to a marked polyuria with hyposmotic urine .

Example answer:
{"entities": [{"text": "LiCl", "type": "ChemicalEntity"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mice lacking mPGES-1 are resistant to lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In contrast , mPGES-1 -/- mice were largely resistant to lithium-induced polyuria and a urine concentrating defect , accompanied by nearly complete blockade of high urine PGE ( 2 ) and cAMP output .

Example answer:
{"entities": [{"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "cAMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Input:
Sentence: PKC-alpha null mice ( PKCa KO ) and strain-matched wild type ( WT ) controls were treated with lithium for 0 , 3 or 5 days .

## Item biored:test:877
Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSION : SELP and IRAK1 were identified as novel SLE-associated genes with a high degree of significance , suggesting new directions in understanding the pathogenesis of SLE .

Example answer:
{"entities": [{"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}, {"text": "SLE-associated", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Surfactant protein ( SP ) -A and SP-D are pattern-recognition molecules of the respiratory tract that activate inflammatory and phagocytic defences after binding to microbial sugars .

Example answer:
{"entities": [{"text": "Surfactant protein ( SP ) -A", "type": "GeneOrGeneProduct"}, {"text": "SP-D", "type": "GeneOrGeneProduct"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sugars", "type": "ChemicalEntity"}]}

Example input:
Sentence: Although several studies have investigated the association between rs1052133 and lung cancer susceptibility , the effect of this locus on lung cancer according to histology remains unclear .

Example answer:
{"entities": [{"text": "rs1052133", "type": "SequenceVariant"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Sepsis increased CAT1 , LAT2 and SNAT2 mRNA content two- to fourfold , but only the protein content for CAT1 ( 20 % decrease ) differed significantly .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CAT1", "type": "GeneOrGeneProduct"}, {"text": "LAT2", "type": "GeneOrGeneProduct"}, {"text": "SNAT2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results indicate that rs1052133 contributes to the risk of adenocarcinoma of lung .

Example answer:
{"entities": [{"text": "rs1052133", "type": "SequenceVariant"}, {"text": "adenocarcinoma of lung", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In vivo , PGA2 was protective in two distinct models of acute lung injury ( ALI ) : LPS-induced inflammatory injury and two-hit ALI caused by suboptimal mechanical ventilation and injection of thrombin receptor-activating peptide .

Example answer:
{"entities": [{"text": "PGA2", "type": "ChemicalEntity"}, {"text": "acute lung injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LPS-induced", "type": "ChemicalEntity"}, {"text": "inflammatory injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thrombin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Finally , the inflammatory infiltration of alveolar and interstitial cells and the destruction of lung structure were significantly attenuated in the mide administered Bach1 siRNA compared with those in the BLM group .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "BLM", "type": "ChemicalEntity"}]}

Input:
Sentence: BACKGROUND : Respiratory syncytial virus ( RSV ) infects the lung epithelium where it stimulates the production of numerous host cytokines that are associated with disease burden and acute lung injury .

## Item biored:test:897
Example input:
Sentence: Gene deletion or pharmacological blockade of KCa3.1 protected against SOCE-induced Ca2+ overload and ER stress via the protein kinase B ( AKT ) signaling pathway in astrocytes .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Brain-derived neurotrophic factor significantly inhibited Dox-induced cardiomyocyte apoptosis , oxidative stress and cardiac dysfunction in rats .

Example answer:
{"entities": [{"text": "cardiac", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: NDP-MSH time- and dose-dependently inhibited IRS-1 ( ser307 ) phosphorylation , effects also reversed by a specific melanocortin receptor antagonist .

Example answer:
{"entities": [{"text": "NDP-MSH", "type": "ChemicalEntity"}, {"text": "IRS-1", "type": "GeneOrGeneProduct"}, {"text": "melanocortin receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , rats that experienced SE exhibited CCR2-labeling in populations of hypertrophied astrocytes , especially in CA1 and dentate gyrus .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCR2-labeling", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we investigated the effects of CCK-8 on long-term potentiation ( LTP ) in the lateral perforant path ( LPP ) -granule cell synapse of rat dentate gyrus ( DG ) in acute saline or morphine-treated rats .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "morphine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: There was a marked increase in the number of TUNEL positive cells and nestin positive cells in BCNU-exposed group , but a decreased immunoreactivity to glial fibrillary acidic protein , synaptophysin and transforming growth factor beta1 was observed , indicating a delayed maturation , and melatonin significantly reversed these changes .

Example answer:
{"entities": [{"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}, {"text": "transforming growth factor beta1", "type": "GeneOrGeneProduct"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: NDP-MSH increased insulin-stimulated glucose uptake in hypothalamic GT1-1 cells .

Example answer:
{"entities": [{"text": "NDP-MSH", "type": "ChemicalEntity"}, {"text": "insulin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "GT1-1", "type": "CellLine"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The growth of breast cancer xenografts in NOD/SCID mice was also inhibited by the doxycycline-induced Star-PAP overexpression .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "doxycycline-induced", "type": "ChemicalEntity"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We found that NSP significantly increased the cell survival rate and reduced LDH release in OGD/R-treated astrocytes .

## Item biored:test:914
Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: Here , we show that simultaneous overexpression of the mitotic checkpoint protein Mad2 with Kras ( G12D ) or Her2 in mammary glands of adult mice results in mitotic checkpoint overactivation and a delay in tumor onset .

Example answer:
{"entities": [{"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "GeneOrGeneProduct"}, {"text": "Her2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Hypothesizing that NRG-1 beta and/or NRG-1 alpha promote MPNST invasion , we found that NRG-1 beta promoted MPNST migration in a substrate-specific manner , markedly enhancing migration on laminin but not on collagen type I or fibronectin .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "laminin", "type": "GeneOrGeneProduct"}, {"text": "collagen type I", "type": "GeneOrGeneProduct"}, {"text": "fibronectin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results indicated that the presence of CD72- * 2 allele decreases risk for human SLE conferred by FCGR2B-232Thr , possibly by increasing the AS isoform of CD72 .

Example answer:
{"entities": [{"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B-232Thr", "type": "GeneOrGeneProduct"}, {"text": "CD72", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Negative Selection and Chromosome Instability Induced by Mad2 Overexpression Delay Breast Cancer but Facilitate Oncogene-Independent Outgrowth .

Example answer:
{"entities": [{"text": "Chromosome Instability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Breast Cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: EP4 mediated barrier-protective effects of PGA2 by activating Rap1/Rac1 GTPase and protein kinase A targets at cell adhesions and cytoskeleton : VE-cadherin , p120-catenin , ZO-1 , cortactin , and VASP .

Example answer:
{"entities": [{"text": "EP4", "type": "GeneOrGeneProduct"}, {"text": "PGA2", "type": "ChemicalEntity"}, {"text": "Rap1/Rac1 GTPase", "type": "GeneOrGeneProduct"}, {"text": "protein kinase A", "type": "GeneOrGeneProduct"}, {"text": "VE-cadherin", "type": "GeneOrGeneProduct"}, {"text": "p120-catenin", "type": "GeneOrGeneProduct"}, {"text": "ZO-1", "type": "GeneOrGeneProduct"}, {"text": "cortactin", "type": "GeneOrGeneProduct"}, {"text": "VASP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PGA2 also suppressed LPS-induced inflammatory signaling by inhibiting the NFkB pathway and expression of EC adhesion molecules ICAM1 and VCAM1 .

Example answer:
{"entities": [{"text": "PGA2", "type": "ChemicalEntity"}, {"text": "LPS-induced", "type": "ChemicalEntity"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkB", "type": "GeneOrGeneProduct"}, {"text": "EC adhesion molecules", "type": "GeneOrGeneProduct"}, {"text": "ICAM1", "type": "GeneOrGeneProduct"}, {"text": "VCAM1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In IEC-6 crypt cells and jejunum enteroids quantitative RT-PCR showed a time- and dose-dependent upregulation of lpa2 in response to gamma-irradiation that was abolished by mutation of the NF-kappaB site in the lpa2 promoter or by inhibition of ATM/ATR kinases with CGK-733 , suggesting that lpa2 is a DNA damage response gene upregulated by ATM via NF-kappaB .

Example answer:
{"entities": [{"text": "IEC-6", "type": "CellLine"}, {"text": "lpa2", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "ATM/ATR kinases", "type": "GeneOrGeneProduct"}, {"text": "CGK-733", "type": "ChemicalEntity"}, {"text": "ATM", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Moreover , knockdown of the epithelial polarity regulator and tumor suppressor lgl2 ameliorated the nrg2a mutant phenotype .

## Item biored:test:880
Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Because polymorphism of CD72 , another inhibitory receptor of B cells , was associated with murine SLE , we identified human CD72 polymorphisms , tested their association with SLE and examined genetic interaction with FCGR2B in the Japanese ( 160 SLE , 277 controls ) , Thais ( 87 SLE , 187 controls ) and Caucasians ( 94 families containing SLE members ) .

Example answer:
{"entities": [{"text": "CD72", "type": "GeneOrGeneProduct"}, {"text": "murine", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "FCGR2B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Neutralizing antibody induction and protective efficacy were also assessed in rhesus monkeys .

Example answer:
{"entities": [{"text": "rhesus monkeys", "type": "OrganismTaxon"}]}

Example input:
Sentence: In mice , LIF receptor expression ( LIFR ) is largely restricted to the uterine luminal epithelium ( LE ) .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "LIF receptor", "type": "GeneOrGeneProduct"}, {"text": "LIFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In rhesus monkeys , rDEN2Delta30 appeared to be slightly attenuated when compared to the parent virus as measured by duration and peak of viremia and neutralizing antibody induction .

Example answer:
{"entities": [{"text": "rhesus monkeys", "type": "OrganismTaxon"}, {"text": "rDEN2Delta30", "type": "OrganismTaxon"}, {"text": "viremia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Four animal groups ( n = 6 ) were tested during 9 weeks : control , CsA , SRL , and conversion ( CsA for 3 weeks followed by SRL for 6 weeks ) .

Example answer:
{"entities": [{"text": "CsA", "type": "ChemicalEntity"}, {"text": "SRL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Crossing Ltf-Cre mice with Lifr flx/flx mice generated Lifr flx/D : Ltf Cre/+ females that were overtly normal but infertile .

Example answer:
{"entities": [{"text": "Ltf-Cre", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "Lifr", "type": "GeneOrGeneProduct"}, {"text": "Ltf", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemistry and western blotting are used to determine the mechanisms of Sal against RIF .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "RIF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To specifically delete the LIFR in the LE , we derived a line of mice in which Cre recombinase was inserted into the endogenous lactoferrin gene ( Ltf-Cre ) .

Example answer:
{"entities": [{"text": "LIFR", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lactoferrin", "type": "GeneOrGeneProduct"}, {"text": "Ltf-Cre", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The cytokine leukemia inhibitory factor ( LIF ) is essential for rendering the uterus receptive for blastocyst implantation .

Example answer:
{"entities": [{"text": "leukemia inhibitory factor", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Neutralizing anti-leukemia inhibitory factor ( LIF ) IgG or control IgG was administered to a group of wild-type animals prior to RSV infection .
