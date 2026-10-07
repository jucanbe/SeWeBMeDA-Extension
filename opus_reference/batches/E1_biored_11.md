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

## Item biored:test:432
Example input:
Sentence: C_6+/6+ and G_6+/6+ combined genotypes were respectively associated to the best and worst PFS ( P=0.03 when compared with each other ) , while combinations carrying the allele 6- determined an intermediate evolution that might be indicative of a variable response to chemotherapy .

Example answer:
{"entities": []}

Example input:
Sentence: These findings substantiate the molecular heterogeneity of DRM , expand the morphological spectrum of SEPN-RM , and implicate a necessary reassessment of the nosological boundaries in early-onset myopathies .

Example answer:
{"entities": [{"text": "DRM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SEPN-RM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myopathies", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thus NPHP , JBTS , and MKS represent allelic disorders .

Example answer:
{"entities": [{"text": "NPHP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MKS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "allelic disorders", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: X-linked mental retardation has been traditionally divided into syndromic ( S-XLMR ) and non-syndromic forms ( NS-XLMR ) , although the borderlines between these phenotypes begin to vanish and mutations in a single gene , for example PQBP1 , can cause S-XLMR as well as NS-XLMR .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PQBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MC is clinically distinct from other multiple exostosis or multiple enchondromatosis syndromes and is unlinked to EXT1 and EXT2 , the genes responsible for autosomal dominant multiple osteochondromas ( MO ) .

Example answer:
{"entities": [{"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "multiple exostosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "multiple enchondromatosis syndromes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EXT1", "type": "GeneOrGeneProduct"}, {"text": "EXT2", "type": "GeneOrGeneProduct"}, {"text": "multiple osteochondromas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We investigated the mechanisms responsible for the functional disparity on B cells between a wild-type p17 ( refp17 ) and a vp17 named S75X .

Example answer:
{"entities": [{"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}]}

Example input:
Sentence: This phenotype resembled that of bone morphogenetic protein receptor ( BMPR ) 1 and Gdf5-deficient mice .

Example answer:
{"entities": [{"text": "bone morphogenetic protein receptor ( BMPR ) 1", "type": "GeneOrGeneProduct"}, {"text": "Gdf5-deficient", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: We found the frequency of the three different genotypes of GSTP1 Ile105Val in our ethnic Kashmir population , i.e. , Ile/Ile , Ile/Val and Val/Val , to be 52.4 , 33.3 and 14.3 % among prostate cancer cases , 48.5 , 37.5 and 14 % among benign prostate hyperplasia cases and 73.8 , 21.3 and 5 % in the control population , respectively .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The genetic basis of the other forms remain unknown , including the early-onset , recessive form with Mallory body-like inclusions ( MB-DRMs ) , first described in five related German patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: MPS are phenotypically and genetically heterogeneous but are traditionally divided into prenatally lethal and nonlethal ( Escobar ) types .

## Item biored:test:440
Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Genomic DNA was screened for GLDC , AMT , and GCSH gene mutations .

Example answer:
{"entities": [{"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "AMT", "type": "GeneOrGeneProduct"}, {"text": "GCSH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: An antibody against the synthetic C-terminal peptides deduced from the cDNA of the gene responsible for X-linked adrenoleukodystrophy ( ALD ) was produced to characterize the product of the ALD gene .

Example answer:
{"entities": [{"text": "X-linked adrenoleukodystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the TGFBI gene in Indian patients with lattice corneal dystrophy ( LCD ) or granular corneal dystrophy ( GCD ) and to look for genotype-phenotype correlations .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "granular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA damage and repair were evaluated by alkaline single cell gel electrophoresis ( comet assay ) assisted by DNA repair enzymes : endonuclease III ( Nth ) and formamidopyrimidine-DNA glycosylase ( Fpg ) , preferentially recognizing oxidized DNA bases .

Example answer:
{"entities": [{"text": "endonuclease III", "type": "GeneOrGeneProduct"}, {"text": "Nth", "type": "GeneOrGeneProduct"}, {"text": "formamidopyrimidine-DNA glycosylase", "type": "GeneOrGeneProduct"}, {"text": "Fpg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: MATERIALS AND METHODS : We screened Greek ADPKD patients with the denaturing gradient gel electrophoresis ( DGGE ) assay and direct sequencing .

## Item biored:test:500
Example input:
Sentence: One of the responding genes was X-chromosomal tenomodulin ( TNMD ) , a putative angiogenesis inhibitor .

Example answer:
{"entities": [{"text": "tenomodulin", "type": "GeneOrGeneProduct"}, {"text": "TNMD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: EPO/EPOR-modulated cell cycle mediators included Cdc25a , Btg3 , Cyclin-d2 , p27-kip1 , Cyclin-g2 and CyclinB1-IP-1 .

Example answer:
{"entities": [{"text": "EPO/EPOR-modulated", "type": "GeneOrGeneProduct"}, {"text": "Cdc25a", "type": "GeneOrGeneProduct"}, {"text": "Btg3", "type": "GeneOrGeneProduct"}, {"text": "Cyclin-d2", "type": "GeneOrGeneProduct"}, {"text": "p27-kip1", "type": "GeneOrGeneProduct"}, {"text": "Cyclin-g2", "type": "GeneOrGeneProduct"}, {"text": "CyclinB1-IP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further , expression of miRNA biosynthetic machinery including Dicer , Exportin-5 , TRKRA , and TARBP2 were downregulated , while DGCR8 and Ago2 were upregulated in KC mice .

Example answer:
{"entities": [{"text": "Dicer", "type": "GeneOrGeneProduct"}, {"text": "Exportin-5", "type": "GeneOrGeneProduct"}, {"text": "TRKRA", "type": "GeneOrGeneProduct"}, {"text": "TARBP2", "type": "GeneOrGeneProduct"}, {"text": "DGCR8", "type": "GeneOrGeneProduct"}, {"text": "Ago2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: In TIPE2 over-expression cells , caspase-3 , caspase-9 , and Bax were significantly up-regulated while Bcl-2 was down-regulated .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "caspase-9", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Of particular interest are genes involved in defense against reactive oxygen species ( ROS ) because ROS are thought to cause DNA damage and contribute to the pathogenesis of cancer .

Example answer:
{"entities": [{"text": "reactive oxygen species", "type": "ChemicalEntity"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Folate is critical for cell division , a major feature of in utero development .

Example answer:
{"entities": [{"text": "Folate", "type": "ChemicalEntity"}]}

Example input:
Sentence: The melanocortin system is crucial to regulation of energy homeostasis .

Example answer:
{"entities": [{"text": "melanocortin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Besides several 'anonymous genes ' , we also identified various fully annotated genes , whose gene products are involved in cyclic adenosine monophosphate-regulated pathways ( PRKACB ) , DNA damage repair , maintenance of chromosome stability and prevention of rereplication ( ATM , ERCC5 , FBXO5 ) , energy metabolism ( such as genes that are involved in the synthesis of proteins encoded by the mitochondrial genome ) and signal transduction ( ARHGAP29 ) .

Example answer:
{"entities": [{"text": "cyclic adenosine", "type": "ChemicalEntity"}, {"text": "PRKACB", "type": "GeneOrGeneProduct"}, {"text": "ATM", "type": "GeneOrGeneProduct"}, {"text": "ERCC5", "type": "GeneOrGeneProduct"}, {"text": "FBXO5", "type": "GeneOrGeneProduct"}, {"text": "ARHGAP29", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Mammalian Ras genes regulate diverse cellular processes including proliferation and differentiation and are frequently mutated in human cancers .

Example answer:
{"entities": [{"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Of particular interest are genes involved in cell cycle pathways , which regulate cell division .

## Item biored:test:413
Example input:
Sentence: CONCLUSIONS : This is the first study to link risperidone-induced hyperprolactinemia and SSRI treatment to lower BMD in children and adolescents .

Example answer:
{"entities": [{"text": "risperidone-induced", "type": "ChemicalEntity"}, {"text": "hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SSRI", "type": "ChemicalEntity"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cisplatin-treated DCs down-regulated the expression of cell surface molecules ( CD80 , CD86 , MHC class I and II ) and up-regulated endocytic capacity in a dose-dependent manner .

Example answer:
{"entities": [{"text": "Cisplatin-treated", "type": "ChemicalEntity"}, {"text": "CD80", "type": "GeneOrGeneProduct"}, {"text": "CD86", "type": "GeneOrGeneProduct"}, {"text": "MHC class I and II", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , the GnRH-induced activation of p38 MAPK was decreased by BMP-4 .

Example answer:
{"entities": [{"text": "GnRH-induced", "type": "GeneOrGeneProduct"}, {"text": "p38 MAPK", "type": "GeneOrGeneProduct"}, {"text": "BMP-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : The mutant receptor hGRalphaD401H enhances the transcriptional activity of glucocorticoid-responsive genes .

Example answer:
{"entities": [{"text": "hGRalphaD401H", "type": "GeneOrGeneProduct"}, {"text": "glucocorticoid-responsive genes", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , AT2R gene and protein expressions in fetal kidneys were inhibited by PCE , associated with the repression of the gene expression of glial-cell-line-derived neurotrophic factor ( GDNF ) /tyrosine kinase receptor ( c-Ret ) signaling pathway .

Example answer:
{"entities": [{"text": "AT2R", "type": "GeneOrGeneProduct"}, {"text": "glial-cell-line-derived neurotrophic factor", "type": "GeneOrGeneProduct"}, {"text": "GDNF", "type": "GeneOrGeneProduct"}, {"text": "kinase receptor", "type": "GeneOrGeneProduct"}, {"text": "c-Ret", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The mRNA levels of CD31 , transforming growth factor- b1 ( TGF-b1 ) , and F4/80 were suppressed in AT1aKO compared with WT .

Example answer:
{"entities": [{"text": "CD31", "type": "GeneOrGeneProduct"}, {"text": "transforming growth factor- b1", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Input:
Sentence: Additionally , ritonavir treatment selectively increased the relative levels of PPARgamma mRNA , a transcription factor responsible for the regulation of CD36 mRNA expression .

## Item biored:test:454
Example input:
Sentence: The convulsive threshold ( mean +/- SD ) was 41.4 +/- 6.5 mg. l ( -1 ) with lidocaine infusion ( 6 mg.kg ( -1 ) .min ( -1 ) ) , increasing significantly to 66.6 +/- 10.9 mg. l ( -1 ) when the end-tidal concentration of sevoflurane was 0.8 % .

Example answer:
{"entities": [{"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "sevoflurane", "type": "ChemicalEntity"}]}

Example input:
Sentence: After admission , the patient received a continuous intravenous infusion of 5-FU ( 1000 mg/day ) , during which precordial pain with right bundle branch block occurred concomitantly with a high serum FBAL concentration of 1955 ng/ml .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "right bundle branch block", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: CLINICAL FEATURES : A 50-year-old woman with low back and right leg pain was scheduled for epidural steroid injection .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "low back and right leg pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steroid", "type": "ChemicalEntity"}]}

Example input:
Sentence: Patients with essential hypertension ( mean sitting diastolic BP [ MSDBP ] , > or =95 mm Hg and < 110 mm Hg ) were randomized to 1 of 8 treatment groups : VAL 160 or 320 mg ; HCTZ 12.5 or 25 mg ; VAL/HCTZ 160/12.5 , 320/12.5 , or 320/25 mg ; or placebo .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "essential hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here , we describe a case of severe masseter muscle rigidity ( jaw of steel ) after succinylcholine ( Sch ) administration during general anesthetic management for rigid bronchoscopic removal of a tracheal foreign body .

Example answer:
{"entities": [{"text": "masseter muscle rigidity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "jaw of steel", "type": "DiseaseOrPhenotypicFeature"}, {"text": "succinylcholine", "type": "ChemicalEntity"}, {"text": "Sch", "type": "ChemicalEntity"}]}

Example input:
Sentence: The doses calculated to cause 50 % reversal of hyperalgesia ( ED50 ) were 7.54 ( 1.81 ) and 4.83 ( 1.54 ) in the carrageenan model and 44.18 ( 1.37 ) and 9.14 ( 1.24 ) in the STZ-induced neuropathy model for CNSB002 and morphine , respectively ( mg/kg ; mean , SEM ) .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carrageenan", "type": "ChemicalEntity"}, {"text": "STZ-induced", "type": "ChemicalEntity"}, {"text": "neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: None of the subjects treated with buprenorphine had QTc interval > 0.440 s ( ( 1/2 ) ) .

Example answer:
{"entities": [{"text": "buprenorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: INTERVENTION AND OUTCOME : An 18-gauge Touhy needle was inserted until loss of resistance occurred at the L4-5 level .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: After verifying the epidural space , bupivacaine and triamcinolone diacetate were injected .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "triamcinolone diacetate", "type": "ChemicalEntity"}]}

Input:
Sentence: In the lateral position with operative side down , patients recived 10 mg ( 2mls ) of 0.5 % hyperbaric bupivacaine through a 25-gauge spinal needle .

## Item biored:test:352
Example input:
Sentence: We detected a novel , single , heterozygous nucleotide ( G -- > C ) substitution at position 1201 ( exon 2 ) of the hGR gene , which resulted in aspartic acid to histidine substitution at amino acid position 401 in the amino-terminal domain of the hGRalpha .

Example answer:
{"entities": [{"text": "( G -- > C ) substitution at position 1201", "type": "SequenceVariant"}, {"text": "hGR", "type": "GeneOrGeneProduct"}, {"text": "aspartic acid to histidine substitution at amino acid position 401", "type": "SequenceVariant"}, {"text": "hGRalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These included missense ( p.T286M ) and nonsense ( p.W111X ) mutations and a transition in the obligate AG-dinucleotide of the intron 8 acceptor splice site ( c.610-2A > G ) .

Example answer:
{"entities": [{"text": "p.T286M", "type": "SequenceVariant"}, {"text": "p.W111X", "type": "SequenceVariant"}, {"text": "AG-dinucleotide", "type": "SequenceVariant"}, {"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : In a patient , a C-to-G transition was identified at nucleotide 857 in exon 8 that resulted in a substitution of alanine for proline at amino acid 286 in the first calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "C-to-G transition was identified at nucleotide 857", "type": "SequenceVariant"}, {"text": "alanine for proline at amino acid 286", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: DNA sequencing analysis showed the patient to be a compound heterozygote for two mutations in the GPIX gene , a novel nine-nucleotide deletion starting at position 1952 of the gene that changes asparagine 86 for alanine and eliminates amino acids 87 , 88 , and 89 ( arginine , threonine , and proline ) and a previously reported point mutation that changes the codon asparagine ( AAC ) for serine ( AGC ) at residue 45 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GPIX", "type": "GeneOrGeneProduct"}, {"text": "nine-nucleotide deletion starting at position 1952", "type": "SequenceVariant"}, {"text": "changes asparagine 86 for alanine and eliminates amino acids 87 , 88 , and 89 ( arginine , threonine , and proline )", "type": "SequenceVariant"}, {"text": "asparagine ( AAC ) for serine ( AGC ) at residue 45", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : The patient 's GR gene had a heterozygotic mutation ( G -- > A ) at nucleotide position 2141 ( exon 8 ) , which resulted in substitution of arginine by glutamine at amino acid position 714 in the ligand-binding domain ( LBD ) of the GR alpha .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "( G -- > A ) at nucleotide position 2141", "type": "SequenceVariant"}, {"text": "arginine by glutamine at amino acid position 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The exon 4 sequence of TGFBI of the proband exhibits the heterozygous single-nucleotide mutation , C417T , leading to amino acid substitution ( R124C ) in the encoded TGF-induced protein .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "C417T", "type": "SequenceVariant"}, {"text": "R124C", "type": "SequenceVariant"}, {"text": "TGF-induced protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Input:
Sentence: However , mutation analysis showed that the proband is a compound heterozygote for 2 mutations in SLC12A3 : a substitution of serine by leucine at amino acid position 555 ( p.Ser555Leu ) and a novel guanine to cytosine transition at the 5 ' splice site of intron 22 ( c.2633+1G > C ) , providing the molecular diagnosis of GS .

## Item biored:test:503
Example input:
Sentence: C_6+/6+ and G_6+/6+ combined genotypes were respectively associated to the best and worst PFS ( P=0.03 when compared with each other ) , while combinations carrying the allele 6- determined an intermediate evolution that might be indicative of a variable response to chemotherapy .

Example answer:
{"entities": []}

Example input:
Sentence: In the present study we explored the effect of three polymorphisms of the TS gene on overall and progression- free survival of colorectal cancer ( CRC ) patients subjected to 5FU chemotherapy .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "5FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , we have investigated the impact of these three polymorphisms on mortality using a sample of 1932 Danish individuals aged 47-93 years , previously used in gene-longevity studies .

Example answer:
{"entities": []}

Example input:
Sentence: However , a longitudinal follow-up study on survival in the same sample indicated that 192RR homozygotes have a poorer survival compared to QQ homozygotes ( hazard rate : 1.38 , P = 0.04 ) .

Example answer:
{"entities": [{"text": "192RR", "type": "SequenceVariant"}]}

Example input:
Sentence: We evaluated 16 single nucleotide polymorphisms ( SNPs ) spanning the entire COX-2 gene in 94 subjects of the control group .

Example answer:
{"entities": [{"text": "COX-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Two single nucleotide polymorphisms ( SNPs ) in GPX4 ( rs713041 and rs757229 ) were associated with all-cause mortality even after adjusting for multiple hypothesis testing ( adjusted P = .0041 and P = .0035 ) .

Example answer:
{"entities": [{"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "rs713041", "type": "SequenceVariant"}, {"text": "rs757229", "type": "SequenceVariant"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both polymorphisms were in strong linkage disequilibrium ( D ' = 0.71 , P < .001 ) , and the 3R/-6 base pair ( bp ) haplotype showed a significant overall survival benefit compared with the most prevalent haplotype 2R/+6bp ( HR = 0.42 ; 95 % CI , 0.20 to 0.85 ; P = .017 ) .

Example answer:
{"entities": []}

Example input:
Sentence: None of the studied polymorphisms alone affected overall or progression-free survival ( PFS ) .

Example answer:
{"entities": []}

Input:
Sentence: The genotypes of each polymorphism were tested for association with survival using Cox regression analysis .

## Item biored:test:396
Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: MATERIALS AND METHODS : Our study included patients who were administered 30-60 mL of iodinated contrast agent for percutaneous coronary angiography ( PCAG ) , all with creatinine values between 1.1 and 3.1 mg/dL .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "contrast", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the periphery of the ischemic territory , SG in the cortex was greater ( less edema accumulation ) in the hypertensive group ( 1.041 +/- 0.001 vs 1.039 +/- 0.001 , P less than 0.05 ) .

Example answer:
{"entities": [{"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A combined clinical and genetic study was conducted in a cohort of patients with CDSRR , to substantiate these prior RESULTS : Seventeen patients from 13 families underwent a detailed ophthalmic examination including color vision testing , Goldmann visual fields , fundus photography , Ganzfeld and multifocal ERGs , and optical coherence tomography .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among a total of 60 patients included in the study , 16 patients developed acute renal failure ( ARF ) on the second day after contrast material was injected ( 26.6 % ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "contrast", "type": "ChemicalEntity"}]}

Example input:
Sentence: Atorvastatin protects against contrast-induced nephropathy via anti-apoptosis by the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Patients who develop ESRD have a higher preoperative and 1-year serum creatinine and are more likely to have hepatorenal syndrome .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Thirty-seven unrelated patients were studied , 18 with LCD and 19 with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients were divided into three groups : Controls , no CRF or ESRD , n=748 ; CRF , sustained serum creatinine > 2.5 mg/dl , n=41 ; and ESRD , n=45 .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Input:
Sentence: In 414 patients , contrast volume , presence of diabetes mellitus , use of N-acetylcysteine , mean baseline SCr , and estimated glomerular filtration rate were comparable in the 2 groups .

## Item biored:test:457
Example input:
Sentence: However , intraspinal injection of 5,7-DHT to produce a more selective lesion of only descending serotonin projections in the spinal cord did not affect this hypotension .

Example answer:
{"entities": [{"text": "5,7-DHT", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The incidence of discontinuations for hypertension-related and oedema-related AEs were significantly higher with etoricoxib ( 2.5 % and 1.1 % respectively ) compared with diclofenac ( 1.5 % and 0.4 % respectively ; p < 0.001 for hypertension and p < 0.01 for oedema ) .

Example answer:
{"entities": [{"text": "hypertension-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Hyperprolactinemia was present in 49 % of 83 boys ( n = 41 ) treated with risperidone for a mean of 2.9 years .

Example answer:
{"entities": [{"text": "Hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Patients with essential hypertension ( mean sitting diastolic BP [ MSDBP ] , > or =95 mm Hg and < 110 mm Hg ) were randomized to 1 of 8 treatment groups : VAL 160 or 320 mg ; HCTZ 12.5 or 25 mg ; VAL/HCTZ 160/12.5 , 320/12.5 , or 320/25 mg ; or placebo .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "essential hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Study results showed that myoclonus incidence was 85 % , 40 % , 70 % , and 25 % in Group NP , Group F , Group M , and Group FM , respectively , and were significantly lower in Group F and Group FM .

Example answer:
{"entities": [{"text": "myoclonus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Six patients ( 3.6 % ) in the methadone group presented torsades de pointes .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "methadone", "type": "ChemicalEntity"}, {"text": "torsades de pointes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One-hundred and fifty HCM ( 90 sporadic hypertrophic cardiomyopathy [ SHCM ] and 60 familial hypertrophic cardiomyopathy [ FHCM ] ) patients and 165 age- and sex-matched normal healthy controls without known hypertension and left ventricular hypertrophy were included in the study .

Example answer:
{"entities": [{"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sporadic hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "familial hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular hypertrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice subjected to hypotensive episodes showed a significant decrease in latency time ( 178 +/- 156 s ) compared with those injected with saline , NTG + NIMO , or delayed NTG ( 580 +/- 81 s , 557 +/- 67 s , and 493 +/- 146 s , respectively ) .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: Six patients in the conventional group had a positive culture , compared with none in the extended-interval group ( P = 0.002 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The incidence of hypokalemia was lower with VAL/HCTZ combinations ( 1.8 % -6.1 % ) than with HCTZ monotherapies ( 7.1 % -13.3 % ) .

Example answer:
{"entities": [{"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Input:
Sentence: RESULTS : Three patients ( 8.1 % ) in the unilateral group and 5 ( 13.5 % ) in the conventional group developed hypotension , P= 0.71 .

## Item biored:test:446
Example input:
Sentence: In conclusion , gene-targeted mice lacking SGK1 showed blunted volume retention , yet were not protected against renal fibrosis during experimental nephrotic syndrome .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "volume retention", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Expression of mutated caveolin-1 in caveolin-1-null mouse fibroblasts failed to induce formation of caveolae due to retention of the mutated protein in the endoplasmic reticulum .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "caveolin-1-null", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: Consistently , LKB1 ( endo-/- ) mouse tissues including the lung , skin , kidney and liver showed increased vascular permeability .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: In contrast , the dowregulation of renal medullary NKCC2 expression was significantly attenuated in the -/- mice .

Example answer:
{"entities": [{"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Accordingly , a reduced expression of MEF2C , MYF5 , and PGC-1a was found in kidney tissue sections that were obtained from patients with diabetic nephropathy .

Example answer:
{"entities": [{"text": "MEF2C", "type": "GeneOrGeneProduct"}, {"text": "MYF5", "type": "GeneOrGeneProduct"}, {"text": "PGC-1a", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "diabetic nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The NDUFS2 contains a highly conserved protein kinase C phosphorylation site and the NDUFS3 subunit contains a highly conserved casein kinase II phosphorylation site which make them strong candidates for future mutation detection studies in enzymatic complex I-deficient patients .

Example answer:
{"entities": [{"text": "NDUFS2", "type": "GeneOrGeneProduct"}, {"text": "protein kinase C", "type": "GeneOrGeneProduct"}, {"text": "NDUFS3", "type": "GeneOrGeneProduct"}, {"text": "casein kinase II", "type": "GeneOrGeneProduct"}, {"text": "enzymatic complex I-deficient", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Increased retrograde transport by BICD2 mutants also was observed in cells using an inducible organelle transport assay .

Example answer:
{"entities": [{"text": "BICD2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunoelectron microscopy further revealed an increased labeling of alpha-ENaC in the apical plasma membrane of cortical collecting duct principal cells of PAN-treated rats , indicating enhanced apical targeting of alpha-ENaC subunits .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "PAN-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: RAMH induced a shift in the localization of PKCalpha expression from the cytosolic domain into the membrane region of Mz-ChA-1 cells .

Example answer:
{"entities": [{"text": "RAMH", "type": "ChemicalEntity"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Mz-ChA-1", "type": "CellLine"}]}

Example input:
Sentence: Immunoperoxidase brightfield- and laser-scanning confocal fluorescence microscopy demonstrated increased targeting of alpha-ENaC , beta-ENaC , and gamma-ENaC subunits to the apical plasma membrane in the distal convoluted tubule ( DCT2 ) , connecting tubule , and cortical and medullary collecting duct segments .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "beta-ENaC", "type": "GeneOrGeneProduct"}, {"text": "gamma-ENaC", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Inner medullar collecting duct ( IMCD ) cells transfected with the mutant PKD2 mouse gene presented a perinuclear and diffuse cytoplasmic localization compared with the wild type ER localization .

## Item biored:test:509
Example input:
Sentence: Future research should include animal studies that address mechanistic hypotheses and studies of human populations that integrate early-life exposure , molecular alterations , and latent disease outcomes .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Future research should evaluate the longitudinal course of this adverse event to determine its temporal stability and whether a higher fracture rate ensues .

Example answer:
{"entities": [{"text": "fracture", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Studies of additional cases yielded a second set of data that , in combination with the first set , confirmed a weak association of UP III SNP7 in VUR ( P= 0.036 adjusted for both subsets of cases vs. controls ) .

Example answer:
{"entities": [{"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Molecular study may help differentiating these abnormalities with precision .

Example answer:
{"entities": []}

Example input:
Sentence: Future studies are needed to assess the therapeutic potential emerging from our finding for human W-ICH .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "W-ICH", "type": "ChemicalEntity"}]}

Example input:
Sentence: However , replication of this finding in larger studies is suggested .

Example answer:
{"entities": []}

Example input:
Sentence: Further association was identified in individuals over 40 years of age .

Example answer:
{"entities": []}

Example input:
Sentence: Further follow-up of the cohort is required to study the polymorphisms ' relevance for immune-mediated diseases such as childhood asthma .

Example answer:
{"entities": [{"text": "immune-mediated diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Limited prospective data corroborate these findings , but larger prospective studies are urgently required .

Example answer:
{"entities": []}

Example input:
Sentence: Further validation by population-based case-control studies and rigorous mechanistic studies is warranted .

Example answer:
{"entities": []}

Input:
Sentence: Further study is required to validate this finding .

## Item biored:test:438
Example input:
Sentence: Phosphatidylinositol 3-kinase p85alpha regulatory subunit gene Met326Ile polymorphism in women with polycystic ovary syndrome .

Example answer:
{"entities": [{"text": "Phosphatidylinositol 3-kinase", "type": "GeneOrGeneProduct"}, {"text": "p85alpha", "type": "GeneOrGeneProduct"}, {"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "polycystic ovary syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using self-reported data on ischemic heart disease to evaluate the impact of the PON 192Q/R polymorphism on susceptibility to CHD , we found only a nonsignificant trend of 192RR homozygosity in women being a risk factor .

Example answer:
{"entities": [{"text": "ischemic heart disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PON", "type": "GeneOrGeneProduct"}, {"text": "192Q/R", "type": "SequenceVariant"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "192RR", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We identified and characterized a PABPN1 mutation in a Taiwanese family with OPMD .

Example answer:
{"entities": [{"text": "PABPN1", "type": "GeneOrGeneProduct"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our findings support the notion that mutations in the PCSK9 gene cause autosomal dominant hypercholesterolemia .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "autosomal dominant hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One patient with a severe cellular and clinical phenotype was a compound heterozygote with POLG1 mutations in the polymerase and exonuclease domain intrans .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All these patients had mutations in a catalytic domain in both POLG1 alleles , in either the polymerase or exonuclease domain or both .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations in the PCSK9 gene in Norwegian subjects with autosomal dominant hypercholesterolemia .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "autosomal dominant hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Whereas no mutations were detected in the PDE6H gene , mutations in KCNV2 were identified in all patients , in either the homozygous or compound heterozygous state .

Example answer:
{"entities": [{"text": "PDE6H", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Co-inheritance of a PKD1 mutation and homozygous PKD2 variant : a potential modifier in autosomal dominant polycystic kidney disease .

## Item biored:test:437
Example input:
Sentence: CONCLUSION : Identification of this new de novo nonsense mutation confirms the diagnosis of FDH in this child and highlights the clinical importance of PORCN and Wnt signalling pathways in embryogenesis .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PORCN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results indicate that some ARM phenotypes in the b-catenin GOF mutants were caused by abnormal Bmp signaling .

Example answer:
{"entities": [{"text": "ARM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Testis morphology showed that , during early infancy , the 5-alpha-reductase enzyme deficiency may not have affected interstitial or tubular development .

Example answer:
{"entities": [{"text": "5-alpha-reductase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , AT2R gene and protein expressions in fetal kidneys were inhibited by PCE , associated with the repression of the gene expression of glial-cell-line-derived neurotrophic factor ( GDNF ) /tyrosine kinase receptor ( c-Ret ) signaling pathway .

Example answer:
{"entities": [{"text": "AT2R", "type": "GeneOrGeneProduct"}, {"text": "glial-cell-line-derived neurotrophic factor", "type": "GeneOrGeneProduct"}, {"text": "GDNF", "type": "GeneOrGeneProduct"}, {"text": "kinase receptor", "type": "GeneOrGeneProduct"}, {"text": "c-Ret", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recently , a lethal phenotype characterized by sudden infant death with dysgenesis of the testes syndrome ( SIDDT ) was identified to be caused by loss of function mutations in the TSPYL1 gene .

Example answer:
{"entities": [{"text": "sudden infant death with dysgenesis of the testes syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SIDDT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSPYL1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Both b-catenin loss- and gain-of-function ( LOF and GOF ) mutants displayed abnormal clefts in the perineal region and hypoplastic elongation of the URS .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "hypoplastic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Functional studies were consistent with the hypothesis that whereas incomplete loss of rapsyn function may cause congenital myasthenia , more severe loss of function can result in a lethal fetal akinesia phenotype .

## Item biored:test:492
Example input:
Sentence: Further , we show that mice genetically engineered to be deficient in brain DA develop METH neurotoxicity , as long as the thermic effects of METH are preserved .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: On the other hand , induction of metallothionein ( MT ) by ZnSO ( 4 ) and its role in neuroprotection has been documented .

Example answer:
{"entities": [{"text": "metallothionein", "type": "ChemicalEntity"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}]}

Example input:
Sentence: Taken together , these findings demonstrate that DA is not essential for the development of METH-induced dopaminergic neurotoxicity and suggest that mechanisms independent of DA warrant more intense investigation .

Example answer:
{"entities": [{"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Different mechanisms have been suggested for cocaine toxicity including an increase in oxidative stress but the association between oxidative status in the brain and cocaine induced-behaviour is poorly understood .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The most relevant adverse event was peripheral neuropathy , which occurred in 78 % of the patients ( grade II , 38 % ; grade III , 21 % ) and led to treatment discontinuation in 6 % .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Dopamine is not essential for the development of methamphetamine-induced neurotoxicity .

Example answer:
{"entities": [{"text": "Dopamine", "type": "ChemicalEntity"}, {"text": "methamphetamine-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It is widely believed that dopamine ( DA ) mediates methamphetamine ( METH ) -induced toxicity to brain dopaminergic neurons , because drugs that interfere with DA neurotransmission decrease toxicity , whereas drugs that increase DA neurotransmission enhance toxicity .

Example answer:
{"entities": [{"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion mitochondrial toxicity is an early common event both in paclitaxel and cisplatin induced neurotoxicity .

Example answer:
{"entities": [{"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Neurotoxicity is a potentially serious toxic effect .

## Item biored:test:491
Example input:
Sentence: To explore the mechanisms of Tat-induced IDO expression , slices were pretreated with the p38 mitogen-activated protein kinase ( MAPK ) inhibitor SB 202190 for 30 min before Tat treatment .

Example answer:
{"entities": [{"text": "Tat-induced", "type": "GeneOrGeneProduct"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "p38 mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "SB 202190", "type": "ChemicalEntity"}, {"text": "Tat", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Their use in orthotopic liver transplantation ( OLTX ) has dramatically improved success rates .

Example answer:
{"entities": []}

Example input:
Sentence: HIV-1 Tat activates indoleamine 2,3 dioxygenase in murine organotypic hippocampal slice cultures in a p38 mitogen-activated protein kinase-dependent manner .

Example answer:
{"entities": [{"text": "HIV-1", "type": "OrganismTaxon"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "indoleamine 2,3 dioxygenase", "type": "GeneOrGeneProduct"}, {"text": "murine", "type": "OrganismTaxon"}, {"text": "p38 mitogen-activated protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Protocols of conversion from cyclosporin A ( CsA ) to sirolimus ( SRL ) have been widely used in immunotherapy after transplantation to prevent CsA-induced nephropathy , but the molecular mechanisms underlying these protocols remain nuclear .

Example answer:
{"entities": [{"text": "cyclosporin A", "type": "ChemicalEntity"}, {"text": "CsA", "type": "ChemicalEntity"}, {"text": "sirolimus", "type": "ChemicalEntity"}, {"text": "SRL", "type": "ChemicalEntity"}, {"text": "CsA-induced", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "calcineurin inhibitors", "type": "ChemicalEntity"}, {"text": "mammalian target of rapamycin ( mToR ) inhibitors", "type": "ChemicalEntity"}, {"text": "sirolimus", "type": "ChemicalEntity"}, {"text": "chronic allograft nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Salvage therapy with nelarabine , etoposide , and cyclophosphamide in relapsed/refractory paediatric T-cell lymphoblastic leukaemia and lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "T-cell lymphoblastic leukaemia and lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SB 202190 significantly decreased IDO expression induced by Tat , and this effect was accompanied by a reduction of Tat-induced expression of TNFa , IL-6 , iNOS and SERT .

Example answer:
{"entities": [{"text": "SB 202190", "type": "ChemicalEntity"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "Tat-induced", "type": "GeneOrGeneProduct"}, {"text": "TNFa", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "SERT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Tat also induced the synthesis and release of TNFa and IL-6 protein in the supernatant of the slices and increased expression of the inducible isoform of nitric oxide synthase ( iNOS ) and the serotonin transporter ( SERT ) .

Example answer:
{"entities": [{"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "TNFa", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "inducible isoform of nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "SERT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Because human immunodeficiency virus type 1 ( HIV-1 ) Tat protein causes depressive-like behavior in mice , we investigated its ability to activate IDO in organotypic hippocampal slice cultures ( OHSCs ) derived from neonatal C57BL/6 mice .

Example answer:
{"entities": [{"text": "human immunodeficiency virus type 1", "type": "OrganismTaxon"}, {"text": "HIV-1", "type": "OrganismTaxon"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "depressive-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Input:
Sentence: TAC has been shown to be a potent immunosuppressive agent for solid organ transplantation in pediatrics .

## Item biored:test:418
Example input:
Sentence: A novel apolipoprotein E mutation , ApoE Osaka ( Arg158 Pro ) , in a dyslipidemic patient with lipoprotein glomerulopathy .

Example answer:
{"entities": [{"text": "apolipoprotein E", "type": "GeneOrGeneProduct"}, {"text": "ApoE", "type": "GeneOrGeneProduct"}, {"text": "Arg158 Pro", "type": "SequenceVariant"}, {"text": "dyslipidemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "lipoprotein glomerulopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , each affected child was heterozygous for the G1681A mutation in exon 7 that led to an Ala467Thr substitution in POLG , within the linker region of the protein .

Example answer:
{"entities": [{"text": "G1681A", "type": "SequenceVariant"}, {"text": "Ala467Thr", "type": "SequenceVariant"}, {"text": "POLG", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations in N-acetylglucosamine ( O-GlcNAc ) transferase in patients with X-linked intellectual disability .

Example answer:
{"entities": [{"text": "N-acetylglucosamine ( O-GlcNAc ) transferase", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Arg124Cys and Arg555Trp appear to be the predominant mutations causing LCD and GCD , respectively , in the population studied .

Example answer:
{"entities": [{"text": "Arg124Cys", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report on two hemizygous mutations in OGT in individuals with X-linked intellectual disability ( XLID ) and dysmorphic features : one missense mutation ( p.Arg284Pro ) and one mutation leading to a splicing defect ( c.463-6T > G ) .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "c.463-6T > G", "type": "SequenceVariant"}]}

Example input:
Sentence: XRCC1 Arg399Gln gene polymorphism and the risk of systemic lupus erythematosus in the Polish population .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In summary , our findings demonstrate for the first time that mutations in PQBP1 are associated with an S-XLMR phenotype including microphthalmia , thereby further extending the clinical spectrum of phenotypes associated with PQBP1 mutations .

Example answer:
{"entities": [{"text": "PQBP1", "type": "GeneOrGeneProduct"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: X-linked mental retardation has been traditionally divided into syndromic ( S-XLMR ) and non-syndromic forms ( NS-XLMR ) , although the borderlines between these phenotypes begin to vanish and mutations in a single gene , for example PQBP1 , can cause S-XLMR as well as NS-XLMR .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PQBP1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The g.ORF15 + 652-653delAG mutation in the RPGR gene is the most frequent mutation in X-linked retinitis pigmentosa ( XLRP ) .

## Item biored:test:498
Example input:
Sentence: We found that the common allele is preferentially expressed in normal lymphocytes , normal breast , and breast tumors compared with the rare allele , but there were no differences in total levels of GPX4 mRNA across genotypes .

Example answer:
{"entities": [{"text": "breast tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Four variants in two genes exceeded the multiple testing threshold for associations with prostate cancer mortality in fixed-effect meta-analyses .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: IMPACT : This study supports that genetic variation in immune response and oxidation influence prostate cancer recurrence risk and suggests genetic variation in these pathways may inform prognosis .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the haplotype analysis , 1 haplotype carrying the variant allele from both +3100 T/G and +8365 C/T , with a population frequency of 3 % , was also significantly associated with decreased risk of prostate cancer ( p=0.036 , global simulated p-value=0.046 ) .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : These data provide strong support for the hypothesis that common variation in GPX4 is associated with prognosis after a diagnosis of breast cancer .

Example answer:
{"entities": [{"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the present study we explored the effect of three polymorphisms of the TS gene on overall and progression- free survival of colorectal cancer ( CRC ) patients subjected to 5FU chemotherapy .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "5FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: PURPOSE : The prognosis of breast cancer varies considerably among individuals , and inherited genetic factors may help explain this variability .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Common germline genetic variation in antioxidant defense genes and survival after diagnosis of breast cancer .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Effects of common germline genetic variation in cell cycle control genes on breast cancer survival : results from a population-based cohort .

## Item biored:test:473
Example input:
Sentence: CONCLUSIONS : Methadone is associated with QT prolongation and higher reporting of syncope in a population of heroin addicts .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "QT prolongation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addicts", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The left ventricular dysfunction was significantly lower in the groups treated with 25 and 50mg/kg of metformin .

Example answer:
{"entities": [{"text": "left ventricular dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: We conclude that mPGES-1-derived PGE ( 2 ) mediates lithium-induced polyuria likely via inhibition of AQP2 and NKCC2 expression .

Example answer:
{"entities": [{"text": "mPGES-1-derived", "type": "GeneOrGeneProduct"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Similarly , ganglionic blockade with hexamethonium caused a significantly greater fall in LNNA hypertensive rats ( 76 +/- 9 mm Hg ) compared with control rats ( 35 +/- 10 mm Hg ) .

Example answer:
{"entities": [{"text": "hexamethonium", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Severe reversible left ventricular systolic and diastolic dysfunction due to accidental iatrogenic epinephrine overdose .

Example answer:
{"entities": [{"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "epinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cyclooxygenase-2 activity is required for the development of lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Cyclooxygenase-2", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Sinus node dysfunction has been reported most frequently among the adverse cardiovascular effects of lithium .

## Item biored:test:475
Example input:
Sentence: We conclude that mPGES-1-derived PGE ( 2 ) mediates lithium-induced polyuria likely via inhibition of AQP2 and NKCC2 expression .

Example answer:
{"entities": [{"text": "mPGES-1-derived", "type": "GeneOrGeneProduct"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mice lacking mPGES-1 are resistant to lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The left ventricular dysfunction was significantly lower in the groups treated with 25 and 50mg/kg of metformin .

Example answer:
{"entities": [{"text": "left ventricular dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 50 mg higher methadone dose was associated with a 1.2 ( 95 % CI 1.1 to 1.4 ) times higher odds for syncope .

Example answer:
{"entities": [{"text": "methadone", "type": "ChemicalEntity"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The convulsive threshold ( mean +/- SD ) was 41.4 +/- 6.5 mg. l ( -1 ) with lidocaine infusion ( 6 mg.kg ( -1 ) .min ( -1 ) ) , increasing significantly to 66.6 +/- 10.9 mg. l ( -1 ) when the end-tidal concentration of sevoflurane was 0.8 % .

Example answer:
{"entities": [{"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "sevoflurane", "type": "ChemicalEntity"}]}

Example input:
Sentence: Prehospital care providers who are managing any patient with a syncopal episode that fails to recover within a reasonable time frame should consider the Bezold-Jarisch reflex as the cause and manage the patient accordingly .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "syncopal episode", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cyclooxygenase-2 activity is required for the development of lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Cyclooxygenase-2", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Input:
Sentence: Serum lithium levels remained under or within the therapeutic range during the syncopal attacks .

## Item biored:test:499
Example input:
Sentence: Moreover , there was a strong correlation between that genotype and stomach cancer occurrence in subjects with high level of oxidatively damaged DNA .

Example answer:
{"entities": [{"text": "stomach cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , whether RNASEL variation contributes to the increased risk of prostate cancer observed in populations of African ancestry remains unclear .

Example answer:
{"entities": [{"text": "RNASEL", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both sporadic and inherited BCCs are associated with mutations in the tumor suppressor gene PTCH1 , but there is still uncertainty on the role of its homolog PTCH2 .

Example answer:
{"entities": [{"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "PTCH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: None of the studied polymorphisms alone affected overall or progression-free survival ( PFS ) .

Example answer:
{"entities": []}

Example input:
Sentence: This heterozygous phenotype illustrates that subtle changes in receptor tyrosine kinase signalling can have significant effects , perhaps providing an explanation for the numerous changes seen in cancer .

Example answer:
{"entities": [{"text": "receptor tyrosine kinase", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: IMPACT : This study supports that genetic variation in immune response and oxidation influence prostate cancer recurrence risk and suggests genetic variation in these pathways may inform prognosis .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations of TP53 and dysfunction of the Brca1 and/or Brca2 tumor-suppressor proteins have been implicated in the molecular pathogenesis of a large fraction of OSCs , but frequent somatic mutations in other well-established tumor-suppressor genes have not been identified .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "Brca1", "type": "GeneOrGeneProduct"}, {"text": "Brca2", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Common germline genetic variation in antioxidant defense genes and survival after diagnosis of breast cancer .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : The prognosis of breast cancer varies considerably among individuals , and inherited genetic factors may help explain this variability .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: INTRODUCTION : Somatic alterations have been shown to correlate with breast cancer prognosis and survival , but less is known about the effects of common inherited genetic variation .

## Item biored:test:502
Example input:
Sentence: This objective was undertaken using a high-throughput DNA pooling experimental design , which proved to be a very accurate , sensitive and specific method of estimating allele frequencies for single nucleotide polymorphism , insertion deletion and variable number tandem repeat loci .

Example answer:
{"entities": []}

Example input:
Sentence: The following gene polymorphisms were determined in genomic DNA : angiotensin-converting enzyme insertion/deletion polymorphism ( I/D ACE ) , angiotensinogen gene polymorphism ( M 235 ) , angiotensin II receptor type 1 ( ATR1 ) polymorphism ( A 11666C ) , and polymorphism of serotonin transporter gene ( 5HTTLPR ) .Heart rate variability during HUT was assessed in 5-minute intervals by low frequency , high frequency , standard deviation of the normal-to-normal ( SDNN ) , and root mean square successive difference parameters .

Example answer:
{"entities": [{"text": "angiotensin-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "M 235", "type": "SequenceVariant"}, {"text": "angiotensin II receptor type 1", "type": "GeneOrGeneProduct"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "A 11666C", "type": "SequenceVariant"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "5HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Analysis of the Met326Ile polymorphism was carried out on DNA samples from 256 PCOS patients and 283 controls .

Example answer:
{"entities": [{"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "PCOS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Utilizing bioinformatic tools , a platform of 9,412 single-nucleotide polymorphisms ( SNPs ) from 1,204 genes was designed and validated .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA was obtained to assess the presence of 4G/5G polymorphism .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : We genotyped eight single nucleotide polymorphisms ( SNPs ) in the three genes , DBH , IL1A and IL6 .

Example answer:
{"entities": [{"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The minor allele frequencies were 25.8 % for SNP rs6235 and 6.0 % for rs6232 .

Example answer:
{"entities": [{"text": "rs6235", "type": "SequenceVariant"}, {"text": "rs6232", "type": "SequenceVariant"}]}

Example input:
Sentence: Five SNPs had a minor allele frequency of more than 5 % in our study population and these were genotyped in all case patients and control subjects and gene-specific haplotypes were constructed .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: A total of 140 SNPs were identified with minor allele frequencies ( MAF ) ranging from 0.001 to 0.47 .

Example answer:
{"entities": []}

Input:
Sentence: DNA from up to 4,470 women was genotyped for 85 polymorphisms that tag the known common polymorphisms ( minor allele frequency > 0.05 ) in the genes .

## Item biored:test:472
Example input:
Sentence: The left ventricular dysfunction was significantly lower in the groups treated with 25 and 50mg/kg of metformin .

Example answer:
{"entities": [{"text": "left ventricular dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Similarly , ganglionic blockade with hexamethonium caused a significantly greater fall in LNNA hypertensive rats ( 76 +/- 9 mm Hg ) compared with control rats ( 35 +/- 10 mm Hg ) .

Example answer:
{"entities": [{"text": "hexamethonium", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Severe reversible left ventricular systolic and diastolic dysfunction due to accidental iatrogenic epinephrine overdose .

Example answer:
{"entities": [{"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "epinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Atrial fibrillation or other cardiac arrhythmias are unusual complications in patients treated with chemotherapy .

Example answer:
{"entities": [{"text": "Atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac arrhythmias", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cyclooxygenase-2 activity is required for the development of lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Cyclooxygenase-2", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Atrial fibrillation following chemotherapy for stage IIIE diffuse large B-cell gastric lymphoma in a patient with myotonic dystrophy ( Steinert 's disease ) .

Example answer:
{"entities": [{"text": "Atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "myotonic dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Steinert 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: Complete atrioventricular block secondary to lithium therapy .

## Item biored:test:458
Example input:
Sentence: Similarly , ganglionic blockade with hexamethonium caused a significantly greater fall in LNNA hypertensive rats ( 76 +/- 9 mm Hg ) compared with control rats ( 35 +/- 10 mm Hg ) .

Example answer:
{"entities": [{"text": "hexamethonium", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mice subjected to hypotensive episodes showed a significant decrease in latency time ( 178 +/- 156 s ) compared with those injected with saline , NTG + NIMO , or delayed NTG ( 580 +/- 81 s , 557 +/- 67 s , and 493 +/- 146 s , respectively ) .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: Maximum contraction of vena cava to norepinephrine ( 37 % control ) also was reduced but no change in response to ET-1 was observed .

Example answer:
{"entities": [{"text": "norepinephrine", "type": "ChemicalEntity"}, {"text": "ET-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The incidence of hypokalemia was lower with VAL/HCTZ combinations ( 1.8 % -6.1 % ) than with HCTZ monotherapies ( 7.1 % -13.3 % ) .

Example answer:
{"entities": [{"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: The incidence of discontinuations for hypertension-related and oedema-related AEs were significantly higher with etoricoxib ( 2.5 % and 1.1 % respectively ) compared with diclofenac ( 1.5 % and 0.4 % respectively ; p < 0.001 for hypertension and p < 0.01 for oedema ) .

Example answer:
{"entities": [{"text": "hypertension-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : One third of patients treated for hypertension attain adequate blood pressure ( BP ) control , and multidrug regimens are often required .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients with essential hypertension ( mean sitting diastolic BP [ MSDBP ] , > or =95 mm Hg and < 110 mm Hg ) were randomized to 1 of 8 treatment groups : VAL 160 or 320 mg ; HCTZ 12.5 or 25 mg ; VAL/HCTZ 160/12.5 , 320/12.5 , or 320/25 mg ; or placebo .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "essential hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Input:
Sentence: Four ( 10.8 % ) patients in the conventional group and 1 ( 2.7 % ) in the unilateral group , P= 0.17 required epinephrine infusion to treat hypotension .

## Item biored:test:506
Example input:
Sentence: Common germline genetic variation in antioxidant defense genes and survival after diagnosis of breast cancer .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In an effort to identify tumor associated antigens that may be useful for immunotherapy , we utilized serological analysis of recombinant cDNA expression libraries ( SEREX ) technique to identify breast cancer-associated antigens .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Four variants in two genes exceeded the multiple testing threshold for associations with prostate cancer mortality in fixed-effect meta-analyses .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SEREX screening of cDNA expression libraries derived from 3 breast cancer patients identified a total of 88 positive clones ( bcg-1 to bcg-88 ) , including 27 hitherto unknown sequences .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : We used gene expression microarrays , real-time PCR , immunoblot , protein-specific ELISA , and gene reporter constructs encoding the enzyme luciferase to study the response of a panel of cancer cells to sorafenib .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sorafenib", "type": "ChemicalEntity"}]}

Example input:
Sentence: The correlation between survival and NEK2 expression was analyzed in 359 patients with HCC using RNASeqV2 data available from The Cancer Genome Atlas ( TCGA ) website ( https : //tcga-data.nci.nih.gov/tcga/ ) .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We evaluated the association of survival and somatic expression of these genes in breast tumours using expression microarray data from seven published datasets .

## Item biored:test:462
Example input:
Sentence: The patient was treated with hyperosmolar therapy , hyperventilation , sedation , and chemical paralysis .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "hyperventilation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Carotid arteries and vena cava were removed for measurement of isometric contraction .

Example answer:
{"entities": []}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Maximal contraction to norepinephrine was modestly reduced in arteries from LNNA compared with control rats whereas the maximum contraction to ET-1 was significantly reduced ( 54 % control ) .

Example answer:
{"entities": [{"text": "norepinephrine", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "ET-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , intraspinal injection of 5,7-DHT to produce a more selective lesion of only descending serotonin projections in the spinal cord did not affect this hypotension .

Example answer:
{"entities": [{"text": "5,7-DHT", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The observed effect of NIMO may have been attributable to the preservation of calcium homeostasis during hypotension , because there were no differences in the PbtO ( 2 ) indices among groups .

Example answer:
{"entities": [{"text": "NIMO", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The superoxide scavenger tempol ( 30 , 100 , and 300 micromol kg ( -1 ) , IV ) did not change arterial pressure in control rats but caused a dose-dependent decrease in LNNA rats ( -18 +/- 8 , -26 +/- 15 , and -54 +/- 11 mm Hg ) .

Example answer:
{"entities": [{"text": "superoxide", "type": "ChemicalEntity"}, {"text": "tempol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "LNNA", "type": "ChemicalEntity"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Input:
Sentence: Also , the type of spinal block instituted affected neither the respiratory rate nor the arterial oxygen saturation .

## Item biored:test:494
Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "calcineurin inhibitors", "type": "ChemicalEntity"}, {"text": "mammalian target of rapamycin ( mToR ) inhibitors", "type": "ChemicalEntity"}, {"text": "sirolimus", "type": "ChemicalEntity"}, {"text": "chronic allograft nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Example input:
Sentence: A novel mutation in the connexin 26 gene ( GJB2 ) in a child with clinical and histological features of keratitis-ichthyosis-deafness ( KID ) syndrome .

Example answer:
{"entities": [{"text": "connexin 26", "type": "GeneOrGeneProduct"}, {"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "keratitis-ichthyosis-deafness ( KID ) syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Compound heterozygosity for a novel nine-nucleotide deletion and the Asn45Ser missense mutation in the glycoprotein IX gene in a patient with Bernard-Soulier syndrome .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}, {"text": "glycoprotein IX", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Nephronophthisis ( NPHP ) , a rare recessive cystic kidney disease , is the most frequent genetic cause of chronic renal failure in children and young adults .

Example answer:
{"entities": [{"text": "Nephronophthisis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cystic kidney disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chronic renal failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 14-year-old girl is reported with recurrent , azithromycin-induced , acute interstitial nephritis .

Example answer:
{"entities": [{"text": "azithromycin-induced", "type": "ChemicalEntity"}, {"text": "interstitial nephritis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunosuppressed renal transplant recipients ( RTRs ) are predisposed to non-melanoma skin cancers ( NMSCs ) , predominantly squamous cell carcinomas ( SCCs ) .

Example answer:
{"entities": [{"text": "non-melanoma skin cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NMSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "squamous cell carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 61-year-old Japanese man with nephrotic syndrome due to focal segmental glomerulosclerosis was initially responding well to steroid therapy .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal segmental glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steroid", "type": "ChemicalEntity"}]}

Example input:
Sentence: The patient was a 45-year-old man who was hospitalized due to nephrotic syndrome .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "man", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Here , we describe an eight-and-a-half-yr-old male renal transplant recipient with right BN .

## Item biored:test:479
Example input:
Sentence: PURPOSE : The prognosis of breast cancer varies considerably among individuals , and inherited genetic factors may help explain this variability .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results unravel a hidden link between AR and a functional putative PCa risk SNP , whose allele alteration affects androgen regulation of its host gene MLPH .

Example answer:
{"entities": [{"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "ChemicalEntity"}, {"text": "MLPH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In overall analysis , the homozygous Cys/Cys genotype showed a significant association with lung cancer compared to Ser allele carrier status ( odds ratio ( OR ) =1.31 , 95 % confidence interval ( CI ) =1.02-1.69 ) .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study supports the hypothesis that inflammation is involved in prostate carcinogenesis and that sequence variation within the COX-2 gene influence the risk of prostate cancer .

Example answer:
{"entities": [{"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prostate carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The androgen receptor ( AR ) gene has polymorphic regions containing variable length glutamine and glycine repeats and these are believed to be associated with PC risk .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Several studies have reported that , compared with wild-type individuals , CYP2C19 variant allele carriers exhibit a significantly lower capacity to metabolize clopidogrel into its active metabolite and inhibit platelet activation , and are therefore at significantly higher risk of adverse cardiovascular events .

Example answer:
{"entities": [{"text": "CYP2C19", "type": "GeneOrGeneProduct"}, {"text": "clopidogrel", "type": "ChemicalEntity"}]}

Example input:
Sentence: The identification of around 7 % of homozygotes for the frameshift mutation in our Caucasian population suggests the existence of an interindividual variation of the CYP2F1 activity and , consequently , the possibility of interindividual differences in the toxic response to some pneumotoxicants and in the susceptibility to certain chemically induced diseases .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In our study the combination of high TS expression genotypes G_6+/6+ identifies a group of high risk within CRC patients treated with 5FU .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "5FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : These findings indicate that the promoter polymorphism of IRF5 is a genetic factor conferring predisposition to RA , and that it contributes considerably to disease pathogenesis in patients that were SE negative .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: However , our preliminary results did not show any evidence that the CYP2F1 genetic polymorphism has implications in the pathogenesis of lung cancer .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The potential role of genetic risk factors in anthracycline-related CHF remains to be defined .

## Item biored:test:497
Example input:
Sentence: Both the precordial pain and the electrocardiographic changes disappeared spontaneously after the discontinuation of 5-FU .

Example answer:
{"entities": [{"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: Moreover , numerous patchy , well-limited fibrotic areas , compatible with post-necrotic tissue repair , were found after 6-month temsirolimus therapy .

Example answer:
{"entities": [{"text": "temsirolimus", "type": "ChemicalEntity"}]}

Example input:
Sentence: These events were temporally coincident with the initial use of high-dose tranexamic acid ( TXA ) therapy after withdrawal of aprotinin from general clinical usage .

Example answer:
{"entities": [{"text": "tranexamic acid", "type": "ChemicalEntity"}, {"text": "TXA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Forty patients with a diagnosis consistent with a hematologic/oncologic disorder that required treatment with an aminoglycoside were randomized to either conventional or extended-interval amikacin .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "hematologic/oncologic disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aminoglycoside", "type": "ChemicalEntity"}, {"text": "amikacin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Their use in orthotopic liver transplantation ( OLTX ) has dramatically improved success rates .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSION : In a PA retention paradigm , the injection of NTG immediately after learning produced a significant impairment of long-term associative memory in mice , whereas delayed induced hypotension had no effect .

Example answer:
{"entities": [{"text": "NTG", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SB 202190 significantly decreased IDO expression induced by Tat , and this effect was accompanied by a reduction of Tat-induced expression of TNFa , IL-6 , iNOS and SERT .

Example answer:
{"entities": [{"text": "SB 202190", "type": "ChemicalEntity"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "Tat-induced", "type": "GeneOrGeneProduct"}, {"text": "TNFa", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "SERT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , a 38 % remission rate has been recently reported in refractory MCL treated with temsirolimus , a mTOR inhibitor.Here we had the opportunity to study a case of refractory MCL who had tumor regression two months after temsirolimus treatment , and a progression-free survival of 10 months .

Example answer:
{"entities": [{"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "temsirolimus", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this work is to call attention to the risk of tacrolimus use in patients with SSc .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SSc", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Efficacy of everolimus ( RAD001 ) in patients with advanced NSCLC previously treated with chemotherapy alone or with chemotherapy and EGFR inhibitors .

Example answer:
{"entities": [{"text": "everolimus", "type": "ChemicalEntity"}, {"text": "RAD001", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "NSCLC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Improvement and eventually full recovery only occurred after TAC was completely discontinued and successfully replaced by everolimus .

## Item biored:test:495
Example input:
Sentence: Previous experiments in this laboratory have shown that microinjection of methyldopa onto the ventrolateral cells of the B3 serotonin neurons in the medulla elicits a hypotensive response mediated by a projection descending into the spinal cord .

Example answer:
{"entities": [{"text": "methyldopa", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Point mutations in the BICD2 gene have been identified in patients with a dominant form of spinal muscular atrophy , but how these mutations cause disease is unknown .

Example answer:
{"entities": [{"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "spinal muscular atrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Initial brain magnetic resonance imaging ( MRI ) were obtained after the hospitalization , including DWI ( 8/8 ) , apparent diffusion coefficient ( ADC ) map ( 4/8 ) , FLAIR ( 7/8 ) , and T2-weighted image ( 8/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Deep-tendon reflexes were decreased especially in the right leg .

Example answer:
{"entities": []}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition to hyperthyroidism , ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers were consistently found in all affected individuals .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metronidazole-induced", "type": "ChemicalEntity"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Initial MRIs showed abnormal high signal intensities on DWI and FLAIR ( or T2-weighted image ) at the dentate nucleus ( 8/8 ) , inferior colliculus ( 6/8 ) , corpus callosum ( 2/8 ) , pons ( 2/8 ) , medulla ( 1/8 ) , and bilateral cerebral white matter ( 1/8 ) .

Example answer:
{"entities": []}

Input:
Sentence: MRI demonstrated hyperintense T2 signals in the cervical cord and right brachial plexus roots indicative of both myelitis and right brachial plexitis .

## Item biored:test:409
Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Conjugates formed with CD25 ( + ) BCl6 ( low ) Tfh cells included B cells expressing higher levels of activation-induced cytidine deaminase ( AID ) , memory marker CD45RO , surface IgG or IgA , and MHC class II compared to B-cell conjugates including CD25 ( - ) Bcl6 ( hi ) Tfh cells .

Example answer:
{"entities": [{"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "BCl6", "type": "GeneOrGeneProduct"}, {"text": "activation-induced cytidine deaminase", "type": "GeneOrGeneProduct"}, {"text": "AID", "type": "GeneOrGeneProduct"}, {"text": "CD45RO", "type": "GeneOrGeneProduct"}, {"text": "IgG", "type": "GeneOrGeneProduct"}, {"text": "IgA", "type": "GeneOrGeneProduct"}, {"text": "MHC class II", "type": "GeneOrGeneProduct"}, {"text": "Bcl6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We investigated the mechanisms responsible for the functional disparity on B cells between a wild-type p17 ( refp17 ) and a vp17 named S75X .

Example answer:
{"entities": [{"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A cell proliferation assay was performed after 7 days of incubation under normoxic conditions .

Example answer:
{"entities": []}

Example input:
Sentence: Estrogen replacement ( 17beta-estradiol subcutaneous pellet , 14.2 microg/day , 12 wk ) of Ovx rats restored the hemodynamic and locomotor effects of alpha-methyldopa to sham-operated levels .

Example answer:
{"entities": [{"text": "17beta-estradiol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}]}

Example input:
Sentence: In mammary epithelial cells , Star-PAP knockdown partially transformed these cells and induced them to undergo epithelial-mesenchymal transition ( EMT ) .

Example answer:
{"entities": [{"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PA-1 cells treated with ETO display highly heterogeneous increases in OCT4A and p21Cip1 indicative of dis-adaptation catastrophe .

Example answer:
{"entities": [{"text": "PA-1", "type": "CellLine"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: hiPS-CMs were seeded onto MEA and FPD was measured for 2min every 10min for 30min after drug exposure for the vehicle and each drug concentration .

Example answer:
{"entities": []}

Example input:
Sentence: In LPA2-reconstituted MEF cells lacking LPA1 ' 3 the levels of gamma-H2AX decreased rapidly , whereas in Vector MEF were high and remained sustained .

Example answer:
{"entities": [{"text": "LPA2-reconstituted", "type": "GeneOrGeneProduct"}, {"text": "MEF", "type": "CellLine"}, {"text": "LPA1 ' 3", "type": "GeneOrGeneProduct"}, {"text": "gamma-H2AX", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Briefly , cells were differentiated for 72 h with 100 nM PMA to obtain a macrophage-like phenotype in the presence or absence of 1 nM 17beta-estradiol ( E2 ) , 100 nM progesterone or vehicle ( 0.01 % ethanol ) .

## Item biored:test:476
Example input:
Sentence: In contrast , mPGES-1 -/- mice were largely resistant to lithium-induced polyuria and a urine concentrating defect , accompanied by nearly complete blockade of high urine PGE ( 2 ) and cAMP output .

Example answer:
{"entities": [{"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "cAMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: The aim of this study is to investigate and compare the protective effects of isotonic sodium chloride with sodium bicarbonate infusion and isotonic sodium chloride infusion with diltiazem , a calcium channel blocker , in preventing CIN .

Example answer:
{"entities": [{"text": "sodium chloride", "type": "ChemicalEntity"}, {"text": "sodium bicarbonate", "type": "ChemicalEntity"}, {"text": "diltiazem", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It is suggested that sevoflurane reduces the convulsive effect of lidocaine toxicity but carries some risk due to circulatory depression .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Clinicians are exhorted to pay close attention when initiating levofloxacin therapy in patients taking medications with epileptogenic properties that are CYP1A2 substrates .

Example answer:
{"entities": [{"text": "levofloxacin", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CYP1A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conclude that mPGES-1-derived PGE ( 2 ) mediates lithium-induced polyuria likely via inhibition of AQP2 and NKCC2 expression .

Example answer:
{"entities": [{"text": "mPGES-1-derived", "type": "GeneOrGeneProduct"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}]}

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
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: Lithium should be used with extreme caution , especially in patients with mild disturbance of AV conduction .

## Item biored:test:481
Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : DNA was collected from 191 patients ( mean age 44+/-18 years , 61 men , 130 women ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Further validation by population-based case-control studies and rigorous mechanistic studies is warranted .

Example answer:
{"entities": []}

Example input:
Sentence: PURPOSE : The anthracyclines daunorubicin and doxorubicin and the epipodophyllotoxin etoposide are potent DNA cleavage-enhancing drugs that are widely used in clinical oncology ; however , myelosuppression and cardiac toxicity limit their use .

Example answer:
{"entities": [{"text": "anthracyclines", "type": "ChemicalEntity"}, {"text": "daunorubicin", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "epipodophyllotoxin", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA was extracted from the blood drawn from 399 prostate cancer patients , 150 BPH patients and 294 healthy community controls .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We therefore conducted a case-control study with 515 incident lung cancer cases and 1030 age- and sex-matched controls without cancer , and further conducted a meta-analysis .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We conducted a nested case-control study of men who had a radical prostatectomy in 1993 to 2001 .

Example answer:
{"entities": [{"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A case-control study was conducted on incident gastric adenocarcinoma patients ( n=271 ) and age-gender frequency-matched control subjects ( n=271 ) .

Example answer:
{"entities": [{"text": "gastric adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: METHODS : A nested case-control study was conducted within a cohort of 1979 patients enrolled in the Childhood Cancer Survivor Study who received treatment with anthracyclines and had available DNA .

## Item biored:test:474
Example input:
Sentence: Amiodarone represents an effective antiarrhythmic drug for cardioversion of recent-onset atrial fibrillation ( AF ) and maintenance of sinus rhythm .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "ChemicalEntity"}, {"text": "antiarrhythmic drug", "type": "ChemicalEntity"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prehospital care providers who are managing any patient with a syncopal episode that fails to recover within a reasonable time frame should consider the Bezold-Jarisch reflex as the cause and manage the patient accordingly .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "syncopal episode", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Severe reversible left ventricular systolic and diastolic dysfunction due to accidental iatrogenic epinephrine overdose .

Example answer:
{"entities": [{"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "epinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Chronic pulsatile levodopa therapy for Parkinson 's disease ( PD ) leads to the development of motor fluctuations and dyskinesia .

Example answer:
{"entities": [{"text": "levodopa", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We briefly describe two patients suffering from recent-onset atrial fibrillation , who experienced an acute devastating low back pain a few minutes after initiation of intravenous amiodarone loading .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low back pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amiodarone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Both isomers of propranolol were also capable of reversing ventricular tachycardia caused by ouabain in anaesthetized cats and dogs .

Example answer:
{"entities": [{"text": "propranolol", "type": "ChemicalEntity"}, {"text": "ventricular tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "cats", "type": "OrganismTaxon"}, {"text": "dogs", "type": "OrganismTaxon"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Atrial fibrillation following chemotherapy for stage IIIE diffuse large B-cell gastric lymphoma in a patient with myotonic dystrophy ( Steinert 's disease ) .

Example answer:
{"entities": [{"text": "Atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "myotonic dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Steinert 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Atrial fibrillation or other cardiac arrhythmias are unusual complications in patients treated with chemotherapy .

Example answer:
{"entities": [{"text": "Atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac arrhythmias", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In the present case , complete atrioventricular ( AV ) block with syncopal attacks developed secondary to lithium therapy , necessitating permanent pacemaker implantation .

## Item biored:test:448
Example input:
Sentence: Eleven subjects presented SRD5A2 homozygous single-base mutations ( two first cousins and four unrelated patients with G183S , two with R246W , one with del642T , one with G196S , and one with 217_218insC plus the A49T variant in heterozygosis ) , whereas four were compound heterozygotes ( one with Q126R/IVS3+1G > A , one with Q126R/del418T , and two brothers with Q126R/G158R ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "G183S", "type": "SequenceVariant"}, {"text": "R246W", "type": "SequenceVariant"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}, {"text": "A49T", "type": "SequenceVariant"}, {"text": "Q126R/IVS3+1G > A", "type": "SequenceVariant"}, {"text": "Q126R/del418T", "type": "SequenceVariant"}, {"text": "Q126R/G158R", "type": "SequenceVariant"}]}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The patient was a compound heterozygote for SRD5A2 mutations , carrying 2 mutations in exon 4 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Novel compound heterozygous mutation of MLYCD in a Chinese patient with malonic aciduria .

Example answer:
{"entities": [{"text": "MLYCD", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "malonic aciduria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Identification of this new de novo nonsense mutation confirms the diagnosis of FDH in this child and highlights the clinical importance of PORCN and Wnt signalling pathways in embryogenesis .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PORCN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: One patient with a severe cellular and clinical phenotype was a compound heterozygote with POLG1 mutations in the polymerase and exonuclease domain intrans .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : This study has identified a new heterozygous de novo mutation in the Cx26 gene ( c.263C > T ; p.Ala88Val ) leading to KID syndrome .

Example answer:
{"entities": [{"text": "Cx26", "type": "GeneOrGeneProduct"}, {"text": "c.263C > T", "type": "SequenceVariant"}, {"text": "p.Ala88Val", "type": "SequenceVariant"}, {"text": "KID syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Whereas no mutations were detected in the PDE6H gene , mutations in KCNV2 were identified in all patients , in either the homozygous or compound heterozygous state .

Example answer:
{"entities": [{"text": "PDE6H", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: A novel variant ( K294E ) was identified in a single heterozygous individual with prostate cancer .

Example answer:
{"entities": [{"text": "K294E", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSIONS : We report for the first time a patient with ADPKD who is heterozygous for a de novo PKD1 variant and homozygous for a novel PKD2 mutation .

## Item biored:test:468
Example input:
Sentence: It was partially reduced by PKC- or Src-inhibition , but not with PI3K-inhibitors ( wortmannin , LY294002 ) or thapsigargin .

Example answer:
{"entities": [{"text": "PKC-", "type": "GeneOrGeneProduct"}, {"text": "Src-inhibition", "type": "GeneOrGeneProduct"}, {"text": "PI3K-inhibitors", "type": "GeneOrGeneProduct"}, {"text": "wortmannin", "type": "ChemicalEntity"}, {"text": "LY294002", "type": "ChemicalEntity"}, {"text": "thapsigargin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Each combination was associated with significantly greater reductions in MSSBP and MSDBP compared with the monotherapies and placebo ( all , P < 0.001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : The mutation in this kindred led to missplicing and reduced GLDC ( glycine decarboxylase ) expression .

Example answer:
{"entities": [{"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "glycine decarboxylase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CSF-to-plasma glycine ratio was mildly to moderately elevated .

Example answer:
{"entities": []}

Example input:
Sentence: Laboratory tests showed an elevation of creatine phosphokinase ( 2218 IU/L ) , aspartate aminotransferase ( 134 IU/L ) , alanine aminotransferase ( 78 IU/L ) , and BUN ( 27.9 mg/ml ) levels .

Example answer:
{"entities": [{"text": "creatine phosphokinase", "type": "ChemicalEntity"}, {"text": "aspartate aminotransferase", "type": "ChemicalEntity"}, {"text": "alanine aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , GABA content of mice hippocampus treated with GFC75 plus P400 showed an increase of 46.90 % when compared with seized mice .

Example answer:
{"entities": [{"text": "GABA", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: At the end of study period , serum phenobarbitone and carbamazepine , whole brain malondialdehyde and reduced glutathione levels were estimated .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "ChemicalEntity"}, {"text": "carbamazepine", "type": "ChemicalEntity"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study aimed to evaluate the GFC effects at doses of 25 , 50 or 75 mg/kg on seizure parameters to determine their anticonvulsant activity and its effects on amino acid ( r-aminobutyric acid ( GABA ) , glutamine , aspartate and glutathione ) levels as well as on acetylcholinesterase ( AChE ) activity in mice hippocampus after seizures .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "r-aminobutyric acid", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In aspartate , glutamine and glutamate levels detected a decrease of 5.21 % , 13.55 % and 21.80 % , respectively in mice hippocampus treated with GFC75 plus P400 when compared with seized mice .

Example answer:
{"entities": [{"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Input:
Sentence: In addition , a statistically significant reduction was also observed on the level of GABA and glycine but less than a drastic reduction of glutamate and aspartate level .

## Item biored:test:504
Example input:
Sentence: Common single nucleotide polymorphisms ( SNPs ) within this gene , rs6232 and rs6235 , are associated with obesity .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Tumor TS 1494del6 allele ( frequency of allelic loss , 36 % ) was protective ( for each allele with the deletion , based on an additive model , HR = 0.42 ; 95 % CI , 0.22 to 0.82 ; P = .0034 ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "1494del6", "type": "SequenceVariant"}]}

Example input:
Sentence: The non-synonymous SNP rs2230912 ( resulting in amino-acid polymorphism Q460R ) showed the strongest association and has been postulated to be pathogenically relevant .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "Q460R", "type": "SequenceVariant"}]}

Example input:
Sentence: GPX4 rs713041 is located near the selenocysteine insertion sequence element in the GPX4 3 ' untranslated region , and the rare allele of this SNP is associated with an increased risk of death , with a hazard ratio of 1.27 per rare allele carried ( 95 % CI , 1.13 to 11.43 ) .

Example answer:
{"entities": [{"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "rs713041", "type": "SequenceVariant"}, {"text": "selenocysteine", "type": "ChemicalEntity"}, {"text": "death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: When the patients were stratified by the SE , the rs729302 A allele was found to confer increased risk to RA in patients that were SE negative ( OR 1.50 , 95 % CI 1.17 to 1.92 , p = 0.001 ) as compared with patients carrying the SE ( OR 1.11 , 95 % CI 0.93 to 1.33 , p = 0.24 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs729302", "type": "SequenceVariant"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This single nucleotide polymorphism ( SNP ) seemed to be functional as it was associated with decreased lung cancer risk .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Two single nucleotide polymorphisms ( SNPs ) in GPX4 ( rs713041 and rs757229 ) were associated with all-cause mortality even after adjusting for multiple hypothesis testing ( adjusted P = .0041 and P = .0035 ) .

Example answer:
{"entities": [{"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "rs713041", "type": "SequenceVariant"}, {"text": "rs757229", "type": "SequenceVariant"}]}

Example input:
Sentence: In the haplotype analysis , 1 haplotype carrying the variant allele from both +3100 T/G and +8365 C/T , with a population frequency of 3 % , was also significantly associated with decreased risk of prostate cancer ( p=0.036 , global simulated p-value=0.046 ) .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: RESULTS : The rare allele of the tagging single nucleotide polymorphism ( SNP ) rs2479717 is associated with an increased risk of death ( hazard ratio = 1.26 per rare allele carried , 95 % confidence interval : 1.12 to 1.42 ; P = 0.0001 ) , which was not attenuated after adjusting for tumour stage , grade , and treatment .

## Item biored:test:490
Example input:
Sentence: Efficacy of everolimus ( RAD001 ) in patients with advanced NSCLC previously treated with chemotherapy alone or with chemotherapy and EGFR inhibitors .

Example answer:
{"entities": [{"text": "everolimus", "type": "ChemicalEntity"}, {"text": "RAD001", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "NSCLC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Conversion to sirolimus ameliorates cyclosporine-induced nephropathy in the rat : focus on serum , urine , gene , and protein renal expression biomarkers .

Example answer:
{"entities": [{"text": "sirolimus", "type": "ChemicalEntity"}, {"text": "cyclosporine-induced", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: BACKGROUND : The calcineurin inhibitors cyclosporine and tacrolimus are both known to be nephrotoxic .

Example answer:
{"entities": [{"text": "calcineurin", "type": "GeneOrGeneProduct"}, {"text": "cyclosporine", "type": "ChemicalEntity"}, {"text": "tacrolimus", "type": "ChemicalEntity"}, {"text": "nephrotoxic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Late-onset scleroderma renal crisis induced by tacrolimus and prednisolone : a case report .

Example answer:
{"entities": [{"text": "scleroderma renal crisis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tacrolimus", "type": "ChemicalEntity"}, {"text": "prednisolone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Salvage therapy with nelarabine , etoposide , and cyclophosphamide in relapsed/refractory paediatric T-cell lymphoblastic leukaemia and lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "T-cell lymphoblastic leukaemia and lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: End-stage renal disease ( ESRD ) after orthotopic liver transplantation ( OLTX ) using calcineurin-based immunotherapy : risk of development and treatment .

Example answer:
{"entities": [{"text": "End-stage renal disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "calcineurin-based", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Protocols of conversion from cyclosporin A ( CsA ) to sirolimus ( SRL ) have been widely used in immunotherapy after transplantation to prevent CsA-induced nephropathy , but the molecular mechanisms underlying these protocols remain nuclear .

Example answer:
{"entities": [{"text": "cyclosporin A", "type": "ChemicalEntity"}, {"text": "CsA", "type": "ChemicalEntity"}, {"text": "sirolimus", "type": "ChemicalEntity"}, {"text": "SRL", "type": "ChemicalEntity"}, {"text": "CsA-induced", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "calcineurin inhibitors", "type": "ChemicalEntity"}, {"text": "mammalian target of rapamycin ( mToR ) inhibitors", "type": "ChemicalEntity"}, {"text": "sirolimus", "type": "ChemicalEntity"}, {"text": "chronic allograft nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Recovery of tacrolimus-associated brachial neuritis after conversion to everolimus in a pediatric renal transplant recipient -- case report and review of the literature .

## Item biored:test:463
Example input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Chemokine CCL2 and its receptor CCR2 are increased in the hippocampus following pilocarpine-induced status epilepticus .

Example answer:
{"entities": [{"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Behavioral and neurochemical studies in mice pretreated with garcinielliptone FC in pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "garcinielliptone FC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Anticonvulsant effect of eslicarbazepine acetate ( BIA 2-093 ) on seizures induced by microperfusion of picrotoxin in the hippocampus of freely moving rats .

Example answer:
{"entities": [{"text": "eslicarbazepine acetate", "type": "ChemicalEntity"}, {"text": "BIA 2-093", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "picrotoxin", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: A single dose of valproic acid ( VPA ) , which is a widely used antiepileptic drug , is associated with oxidative stress in rats , as recently demonstrated by elevated levels of 15-F ( 2t ) -isoprostane ( 15-F ( 2t ) -IsoP ) .

Example answer:
{"entities": [{"text": "valproic acid", "type": "ChemicalEntity"}, {"text": "VPA", "type": "ChemicalEntity"}, {"text": "antiepileptic drug", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "15-F ( 2t ) -isoprostane", "type": "ChemicalEntity"}, {"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study aimed to evaluate the GFC effects at doses of 25 , 50 or 75 mg/kg on seizure parameters to determine their anticonvulsant activity and its effects on amino acid ( r-aminobutyric acid ( GABA ) , glutamine , aspartate and glutathione ) levels as well as on acetylcholinesterase ( AChE ) activity in mice hippocampus after seizures .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "r-aminobutyric acid", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , our data suggest that GFC may influence in epileptogenesis and promote anticonvulsant actions in pilocarpine model by modulating the GABA and glutamate contents and of AChE activity in seized mice hippocampus .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: Acute effects of N- ( 2-propylpentanoyl ) urea on hippocampal amino acid neurotransmitters in pilocarpine-induced seizure in rats .

## Item biored:test:430
Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We tested 67 Czech patients of different ages with simple microcephaly for the presence of the most common mutation in the NBS1 gene .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NBS1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In GCD , 18 patients with GCD type I had a mutation of arginine 555-to-tryptophan ( Arg555Trp ) and 1 patient with GCD type III ( Reis-Bucklers dystrophy ) , had the Arg124Leu mutation .

Example answer:
{"entities": [{"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "GCD type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 555-to-tryptophan", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "GCD type III", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Reis-Bucklers dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Arg124Leu", "type": "SequenceVariant"}]}

Example input:
Sentence: Loss-of-function mutations in PTPN11 cause metachondromatosis , but not Ollier disease or Maffucci syndrome .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "metachondromatosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that heterozygous loss-of-function mutations in PTPN11 are a frequent cause of MC , that lesions in patients with MC appear to arise following a `` second hit , '' that MC may be locus heterogeneous since 1 familial and 5 sporadically occurring cases lacked obvious disease-causing PTPN11 mutations , and that PTPN11 mutations are not a common cause of Ollier disease or Maffucci syndrome .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Novel CACNA1S mutation causes autosomal dominant hypokalemic periodic paralysis in a South American family .

Example answer:
{"entities": [{"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "hypokalemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We next sequenced PTPN11 in DNA samples from 54 patients with the multiple enchondromatosis disorders Ollier disease or Maffucci syndrome , but found no coding sequence PTPN11 mutations .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "enchondromatosis disorders Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Sanger sequence analysis of PTPN11 coding regions in a total of 17 MC families identified mutations in 10 of them ( 5 frameshift , 2 nonsense , and 3 splice-site mutations ) .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Mutation analysis of CHRNA1 , CHRNB1 , CHRND , and RAPSN genes in multiple pterygium syndrome/fetal akinesia patients .

## Item biored:test:486
Example input:
Sentence: The CASP8 -652 6N del variant genotypes or haplotypes were inversely associated with SCCHN risk ( adjusted OR , 0.70 ; 95 % CI , 0.57-0.85 for the ins/del + del/del genotypes compared with the ins/ins genotype ; adjusted OR , 0.73 ; 95 % CI , 0.55-0.97 for the del-D haplotype compared with the ins-D haplotype ) .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The -930G allele carrier state was a risk factor for CAD ( OR 2.03 , 95 % CI 1.21-3.44 , P=0.007 ) .

Example answer:
{"entities": [{"text": "-930G", "type": "SequenceVariant"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The -930A > G polymorphism of the CYBA gene is associated with premature coronary artery disease .

Example answer:
{"entities": [{"text": "-930A > G", "type": "SequenceVariant"}, {"text": "CYBA", "type": "GeneOrGeneProduct"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both polymorphisms were in strong linkage disequilibrium ( D ' = 0.71 , P < .001 ) , and the 3R/-6 base pair ( bp ) haplotype showed a significant overall survival benefit compared with the most prevalent haplotype 2R/+6bp ( HR = 0.42 ; 95 % CI , 0.20 to 0.85 ; P = .017 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The aim of the present study was to analyze a possible association between the -930A > G polymorphism and CAD and to search for gene-traditional risk factors interactions .

Example answer:
{"entities": [{"text": "-930A > G", "type": "SequenceVariant"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : A intragenic biallelic polymorphism ( 1359 G/A ) of the CB1 gene resulting in the substitution of the G to A at nucleotide position 1359 in codon 435 ( Thr ) , was reported as a common polymorphism in Caucasian populations .

Example answer:
{"entities": [{"text": "1359 G/A", "type": "SequenceVariant"}, {"text": "CB1", "type": "GeneOrGeneProduct"}, {"text": "G to A at nucleotide position 1359", "type": "SequenceVariant"}, {"text": "codon 435 ( Thr )", "type": "SequenceVariant"}]}

Example input:
Sentence: This study showed that CFH was more likely to be AMD susceptibility gene at Chr.1q31 based on the finding that the CFHR1 and CFHR3 deletion was not polymorphic in the cohort of this study , and none of the SNPs that were significantly associated with AMD in a white population in C2 , CFB , and C3 genes showed a significant association with AMD .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using self-reported data on ischemic heart disease to evaluate the impact of the PON 192Q/R polymorphism on susceptibility to CHD , we found only a nonsignificant trend of 192RR homozygosity in women being a risk factor .

Example answer:
{"entities": [{"text": "ischemic heart disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PON", "type": "GeneOrGeneProduct"}, {"text": "192Q/R", "type": "SequenceVariant"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "192RR", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Two coding polymorphisms , 55M/L and 192Q/R , and a promoter variant , -107C/T , has been extensively studied with respect to susceptibility to CHD .

Example answer:
{"entities": [{"text": "55M/L", "type": "SequenceVariant"}, {"text": "192Q/R", "type": "SequenceVariant"}, {"text": "-107C/T", "type": "SequenceVariant"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: There was a trend toward an association between the CBR3 V244M polymorphism and the risk of CHF ( OR , 8.16 ; P=.056 for G/G vs A/A ; OR , 5.44 ; P=.092 for G/A vs A/A ) .
