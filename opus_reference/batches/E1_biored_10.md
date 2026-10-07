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

## Item biored:test:407
Example input:
Sentence: VEGF-stimulated hRMVEC proliferation was measured following transfection with NOX4 siRNA or STAT3 siRNA , or respective controls .

Example answer:
{"entities": [{"text": "VEGF-stimulated", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: HIV-1 Tat activates indoleamine 2,3 dioxygenase in murine organotypic hippocampal slice cultures in a p38 mitogen-activated protein kinase-dependent manner .

Example answer:
{"entities": [{"text": "HIV-1", "type": "OrganismTaxon"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "indoleamine 2,3 dioxygenase", "type": "GeneOrGeneProduct"}, {"text": "murine", "type": "OrganismTaxon"}, {"text": "p38 mitogen-activated protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Angiotensin II subtype 1a receptor signaling in resident hepatic macrophages induces liver metastasis formation .

Example answer:
{"entities": [{"text": "Angiotensin II subtype 1a receptor", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As a species comparison with our previous results , we used LbetaT2 cells to investigate the effects of BMP-4 on gonadotrophin mRNA and secretion modulated by activin and GnRH .

Example answer:
{"entities": [{"text": "LbetaT2", "type": "CellLine"}, {"text": "BMP-4", "type": "GeneOrGeneProduct"}, {"text": "gonadotrophin", "type": "GeneOrGeneProduct"}, {"text": "activin", "type": "GeneOrGeneProduct"}, {"text": "GnRH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Because human immunodeficiency virus type 1 ( HIV-1 ) Tat protein causes depressive-like behavior in mice , we investigated its ability to activate IDO in organotypic hippocampal slice cultures ( OHSCs ) derived from neonatal C57BL/6 mice .

Example answer:
{"entities": [{"text": "human immunodeficiency virus type 1", "type": "OrganismTaxon"}, {"text": "HIV-1", "type": "OrganismTaxon"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "depressive-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Methadone , an agonist of OPRM1 , enhances the sensitivity of parental leukemic cells , but not OPRM1-depleted cells , to L-asparaginase treatment , indicating that OPRM1 is required for the synergistic action of L-asparaginase and methadone , and that OPRM1 loss promotes leukemic cell survival likely through downregulation of the OPRM1-mediated apoptotic pathway .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "methadone", "type": "ChemicalEntity"}, {"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Markers of fibrinolysis , thrombin-activatable fibrinolysis inhibitor ( TAFI ) , tissue-type plasminogen activator ( tPA ) , and plasminogen activator inhibitor-1 ( PAI-1 ) levels were studied for the evaluation of short-term effects of raloxifene administration in postmenopausal women .

Example answer:
{"entities": [{"text": "thrombin-activatable fibrinolysis inhibitor", "type": "GeneOrGeneProduct"}, {"text": "TAFI", "type": "GeneOrGeneProduct"}, {"text": "tissue-type plasminogen activator", "type": "GeneOrGeneProduct"}, {"text": "tPA", "type": "GeneOrGeneProduct"}, {"text": "plasminogen activator inhibitor-1", "type": "GeneOrGeneProduct"}, {"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "raloxifene", "type": "ChemicalEntity"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Input:
Sentence: In the present study , we have investigated the molecular mechanisms by which female hormones influence cholesterol metabolism in macrophages in response to the HIV protease inhibitor ritonavir .

## Item biored:test:456
Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The patient 's observations were within normal limits , he was administered oxygen via a face mask and glyceryl trinitrate ( GTN ) .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "oxygen", "type": "ChemicalEntity"}, {"text": "glyceryl trinitrate", "type": "ChemicalEntity"}, {"text": "GTN", "type": "ChemicalEntity"}]}

Example input:
Sentence: However , there was no significant difference in the lidocaine concentrations measured when the systolic blood pressure became 70 mmHg .

Example answer:
{"entities": [{"text": "lidocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: All patients were observed for 6 hours after each challenge , and controlled again after 24 hours to exclude delayed reactions .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The extent of hypotension and changes in brain tissue oxygenation ( PbtO ( 2 ) ) and in cerebral blood flow were studied in a separate group of animals .

Example answer:
{"entities": [{"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice subjected to hypotensive episodes showed a significant decrease in latency time ( 178 +/- 156 s ) compared with those injected with saline , NTG + NIMO , or delayed NTG ( 580 +/- 81 s , 557 +/- 67 s , and 493 +/- 146 s , respectively ) .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: Three time domain indexes of hemodynamic variability were employed : the standard deviation of mean arterial pressure as a measure of blood pressure variability and the standard deviation of beat-to-beat intervals ( SDRR ) and the root mean square of successive differences in R-wave-to-R-wave intervals as measures of heart rate variability .

Example answer:
{"entities": []}

Example input:
Sentence: Hemodynamic parameters and lead II electrocardiograph were monitored and recorded continuously .

Example answer:
{"entities": []}

Example input:
Sentence: Systolic blood pressures ( SBP ) and bodyweights were recorded each alternate day .

Example answer:
{"entities": []}

Example input:
Sentence: Several minutes after the GTN the patient experienced a sudden drop in blood pressure and heart rate , this was rectified by atropine sulphate and a fluid challenge .

Example answer:
{"entities": [{"text": "GTN", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "drop in blood pressure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "atropine sulphate", "type": "ChemicalEntity"}]}

Input:
Sentence: Blood pressure , heart rate , respiratory rate and oxygen saturation were monitored over 1 hour .

## Item biored:test:295
Example input:
Sentence: Mutations of the steroid 5alpha-reductase type 2 ( SRD5A2 ) gene in 46 , XY subjects cause masculinization defects of varying degrees , due to reduced or impaired enzymatic activity .

Example answer:
{"entities": [{"text": "steroid 5alpha-reductase type 2", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We describe a novel germline mutation of BMPR1A in a family with juvenile polyposis and colon cancer .

Example answer:
{"entities": [{"text": "BMPR1A", "type": "GeneOrGeneProduct"}, {"text": "juvenile polyposis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : In this family , a heterozygous cytosine insertion in exon 10 ( c.1546_1547insC ) inducing a frame shift mutation of MEN1 was found in the proband and the other two suffering members of his family .

Example answer:
{"entities": [{"text": "cytosine insertion", "type": "SequenceVariant"}, {"text": "c.1546_1547insC", "type": "SequenceVariant"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This study aimed to identify mutations in a Chinese pedigree with MEN1 .

Example answer:
{"entities": [{"text": "MEN1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Pituitary adenoma predisposition ( PAP ) has been recently associated with germline mutations in the aryl hydrocarbon receptor interacting protein ( AIP ) gene .

Example answer:
{"entities": [{"text": "Pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aryl hydrocarbon receptor interacting protein", "type": "GeneOrGeneProduct"}, {"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutation analysis in a Chinese family with multiple endocrine neoplasia type 1 .

Example answer:
{"entities": [{"text": "multiple endocrine neoplasia type 1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The mutation in exon 10 of MEN1 gene might induce development of parathyroid hyperplasia and pituitary adenoma and cosegregate with MEN1 syndrome .

Example answer:
{"entities": [{"text": "MEN1", "type": "GeneOrGeneProduct"}, {"text": "parathyroid hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1 syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Multiple endocrine neoplasia type 1 ( MEN1 ) is an autosomal dominant cancer syndrome which is caused by germline mutations of the tumor suppressor gene MEN1 .

Example answer:
{"entities": [{"text": "Multiple endocrine neoplasia type 1", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal dominant cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Multiple endocrine neoplasia type 1 ( MEN1 ) is characterized by parathyroid , enteropancreatic endocrine and pituitary adenomas as well as germline mutation of the MEN1 gene .

## Item biored:test:428
Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A relatively high frequency of germ-line genomic rearrangements in MLH1 and MSH2 has been reported among Lynch Syndrome ( HNPCC ) patients from different ethnic populations .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We found the frequency of the three different genotypes of GSTP1 Ile105Val in our ethnic Kashmir population , i.e. , Ile/Ile , Ile/Val and Val/Val , to be 52.4 , 33.3 and 14.3 % among prostate cancer cases , 48.5 , 37.5 and 14 % among benign prostate hyperplasia cases and 73.8 , 21.3 and 5 % in the control population , respectively .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Whereas we confirmed lack of direct correlation between the clinical phenotype and the genotype , we also found that the so-called 'common mutation ' ( p.R50X ) accounted for about 43 % of alleles in our cohort and that no population-related mutations are clearly identified in Italian patients .

Example answer:
{"entities": [{"text": "p.R50X", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : The symptoms of infertility observed in the DMC1 homozygote mutation carrier and in both patients with a heterozygous substitution in exon 2 of the MSH5 gene provide indirect evidence of the role of genes involved in meiotic recombination in the regulation of ovarian function .

Example answer:
{"entities": [{"text": "infertility", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: A patient of Chinese origin with ambiguous genitalia at 14 months , a 46 , XY karyotype , and normal T secretion under human chorionic gonadotropin ( hCG ) stimulation underwent a gonadectomy at 20 months .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "T", "type": "ChemicalEntity"}, {"text": "human chorionic gonadotropin", "type": "ChemicalEntity"}, {"text": "hCG", "type": "ChemicalEntity"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Haplotype analysis suggests a germline mosaicism of the 2-bp deletion in the maternal grandmother of both affected individuals .

Example answer:
{"entities": []}

Input:
Sentence: Gonadal mosaicism may be responsible for a proportion of multiplex or simplex RP families , in which more than 50 % of all cases of RP are found .

## Item biored:test:460
Example input:
Sentence: The superoxide scavenger tempol ( 30 , 100 , and 300 micromol kg ( -1 ) , IV ) did not change arterial pressure in control rats but caused a dose-dependent decrease in LNNA rats ( -18 +/- 8 , -26 +/- 15 , and -54 +/- 11 mm Hg ) .

Example answer:
{"entities": [{"text": "superoxide", "type": "ChemicalEntity"}, {"text": "tempol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "LNNA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Both polymorphisms were in strong linkage disequilibrium ( D ' = 0.71 , P < .001 ) , and the 3R/-6 base pair ( bp ) haplotype showed a significant overall survival benefit compared with the most prevalent haplotype 2R/+6bp ( HR = 0.42 ; 95 % CI , 0.20 to 0.85 ; P = .017 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Five of the forty genes -- ENT3 , IDP3 , JEM1 , ARG2 and HSP82 -- ranked highest in their ability to block alpha-syn-induced reactive oxygen species accumulation , and these five genes were characterized in more detail .

Example answer:
{"entities": [{"text": "ENT3", "type": "GeneOrGeneProduct"}, {"text": "IDP3", "type": "GeneOrGeneProduct"}, {"text": "JEM1", "type": "GeneOrGeneProduct"}, {"text": "ARG2", "type": "GeneOrGeneProduct"}, {"text": "HSP82", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn-induced", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : LAT and HAT groups were matched in age , obesity , insulin , and glucose , and had similar expression of insulin-related genes ( InsR , IRS-1 ) .

Example answer:
{"entities": [{"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "insulin-related", "type": "GeneOrGeneProduct"}, {"text": "InsR", "type": "GeneOrGeneProduct"}, {"text": "IRS-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hypoxia is widely accepted as a fundamental biological phenomenon , which is strongly associated with tissue damage and cell viability under stress conditions .

Example answer:
{"entities": [{"text": "Hypoxia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "mitochondrial respiratory dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADP/O", "type": "ChemicalEntity"}, {"text": "isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: By contrast , oxidation related genes were decreased ( AMPK , UCP1 , CPT1 , FABP7 ) .

Example answer:
{"entities": [{"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "UCP1", "type": "GeneOrGeneProduct"}, {"text": "CPT1", "type": "GeneOrGeneProduct"}, {"text": "FABP7", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The patient 's observations were within normal limits , he was administered oxygen via a face mask and glyceryl trinitrate ( GTN ) .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "oxygen", "type": "ChemicalEntity"}, {"text": "glyceryl trinitrate", "type": "ChemicalEntity"}, {"text": "GTN", "type": "ChemicalEntity"}]}

Example input:
Sentence: The extent of hypotension and changes in brain tissue oxygenation ( PbtO ( 2 ) ) and in cerebral blood flow were studied in a separate group of animals .

Example answer:
{"entities": [{"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , a longitudinal follow-up study on survival in the same sample indicated that 192RR homozygotes have a poorer survival compared to QQ homozygotes ( hazard rate : 1.38 , P = 0.04 ) .

Example answer:
{"entities": [{"text": "192RR", "type": "SequenceVariant"}]}

Input:
Sentence: The mean respiratory rate and oxygen saturations in the two groups were similar .

## Item biored:test:415
Example input:
Sentence: Intact cells loaded with fura-2 had an elevated intracellular free Ca ( 2+ ) concentration ( ( i ) ) , which decreased to the same level such as in non-transfected cells if external Ca ( 2+ ) was chelated by EGTA .

Example answer:
{"entities": [{"text": "fura-2", "type": "ChemicalEntity"}, {"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "EGTA", "type": "ChemicalEntity"}]}

Example input:
Sentence: In a second series , cytosolic Ca2+ activity ( Fluo3 fluorescence ) , cell volume ( forward scatter ) , and PS-exposure ( annexin V binding ) were determined by FACS analysis in erythrocytes from healthy volunteers .

Example answer:
{"entities": [{"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "Fluo3", "type": "ChemicalEntity"}, {"text": "PS-exposure", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Consistent with these in vitro data , expression levels of the ER stress markers 78-kDa glucose-regulated protein and CCAAT/enhancer-binding protein homologous protein , as well as that of the RA marker glial fibrillary acidic protein were increased in APP/PS1 AD mouse model .

Example answer:
{"entities": [{"text": "78-kDa glucose-regulated protein", "type": "GeneOrGeneProduct"}, {"text": "CCAAT/enhancer-binding protein homologous protein", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: While IL-2 suppresses early Tfh-cell differentiation , Tfh-cell recognition of antigen-presenting B cells and signaling through the T-cell receptor likely triggers expression of the high-affinity IL-2 receptor and responses to IL-2 including downregulation of Bcl6 .

Example answer:
{"entities": [{"text": "IL-2", "type": "GeneOrGeneProduct"}, {"text": "T-cell receptor", "type": "GeneOrGeneProduct"}, {"text": "IL-2 receptor", "type": "GeneOrGeneProduct"}, {"text": "Bcl6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In response to IL-2 , these CD25 ( + ) Tfh cells increased expression of costimulatory molecules ICOS or OX40 , upregulated transcription factor cMaf , produced cytokines IL-21 , IL-17 , and IL-10 , and raised the levels of antiapoptotic protein Bcl2 .

Example answer:
{"entities": [{"text": "IL-2", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "ICOS", "type": "GeneOrGeneProduct"}, {"text": "OX40", "type": "GeneOrGeneProduct"}, {"text": "cMaf", "type": "GeneOrGeneProduct"}, {"text": "IL-21", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "Bcl2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results indicated that the presence of CD72- * 2 allele decreases risk for human SLE conferred by FCGR2B-232Thr , possibly by increasing the AS isoform of CD72 .

Example answer:
{"entities": [{"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B-232Thr", "type": "GeneOrGeneProduct"}, {"text": "CD72", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TIPE2 inhibited the phosphorylation of Akt , while promoting the phosphorylation of P38 , but had no effect on IkBa and ERK pathway .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "P38", "type": "GeneOrGeneProduct"}, {"text": "IkBa", "type": "GeneOrGeneProduct"}, {"text": "ERK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , the abundance and proliferative index of lymph node , thymus and CNS CD4 ( + ) CD25 ( + ) FoxP3 ( + ) Tregs were strikingly reduced in VPAC2-deficient mice with EAE .

Example answer:
{"entities": [{"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "FoxP3", "type": "GeneOrGeneProduct"}, {"text": "VPAC2-deficient", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: E2 did , however , significantly suppress CD36 protein levels as measured by fluorescent immunocytochemistry .

## Item biored:test:356
Example input:
Sentence: CONCLUSIONS : Dexamethasone treatment is effective in controlling the premature pubarche , hypoglycemia , hypertension , and hypokalemia in this child case , wherein arginine 714 plays a key role in the proper formation of the ligand-binding pocket and the AF-2 surface of the GR alpha LBD .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVES : Hypertension often persists after adrenalectomy for primary aldosteronism .

Example answer:
{"entities": [{"text": "Hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This report describes a patient with mild language delay and mental retardation , who was found to have nonketotic hyperglycinemia following her presentation with acute encephalopathy and chorea shortly after initiation of valproate therapy .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "language delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nonketotic hyperglycinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chorea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "valproate", "type": "ChemicalEntity"}]}

Example input:
Sentence: At re-warming , patient had resolution of her cerebral edema and intracranial hypertension .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracranial hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: NPHP can be associated with retinal degeneration ( Senior-Loken syndrome ) , brainstem and cerebellar anomalies ( Joubert syndrome ) , or liver fibrosis .

Example answer:
{"entities": [{"text": "NPHP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "retinal degeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Senior-Loken syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebellar anomalies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Joubert syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Multivariate logistic regression revealed the common haplotypes H1 ( AGACT ) , H2 ( AGAWT ) , and H3 ( AGAWC ) were associated with the persistent postoperative hypertension ( P = .01 , 0.03 , 0.005 after Bonferroni correction ) .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Most of the reported cases are adults , demonstrating symptoms associated with mineralocorticoid and/or adrenal androgen excess caused by compensatively increased secretion of the adrenocorticotropic hormone .

Example answer:
{"entities": [{"text": "mineralocorticoid", "type": "ChemicalEntity"}, {"text": "androgen", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , one of these patients had preclinical hypopituitarism , which is an unusual feature of WFS .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "hypopituitarism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "WFS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Notably , the same mutation is associated with the Hamel cerebropalatocardiac syndrome , another form of S-XLMR .

Example answer:
{"entities": [{"text": "Hamel cerebropalatocardiac syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: She also had hypertension and premature pubarche , whereas dexamethasone effectively suppressed these clinical manifestations .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Input:
Sentence: Three similar associations of Bartter syndrome/GS with pseudotumor cerebri were found in the literature , suggesting that electrolyte abnormalities and secondary aldosteronism may have a role in idiopathic intracranial hypertension .

## Item biored:test:364
Example input:
Sentence: METHODS : One hundred PC patients and an age matched cohort of 79 benign prostate hyperplasia and 67 population controls were entered in this study .

Example answer:
{"entities": [{"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: 480 subjects were studied : 240 patients with premature CAD , 240 age and sex matched blood donors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : A case-control study was carried out in Chinese Han population , including 368 cases of migraine and 517 controls .

Example answer:
{"entities": [{"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Included were 5,128 CL/P cases , 1,745 CPO cases , and 3,712 controls ( like-sexed , non-malformed liveborn infant , born immediately after a malformed one , in the same hospital ) , over 4,199,630 consecutive births .

Example answer:
{"entities": [{"text": "CL/P", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CPO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: One-hundred and fifty HCM ( 90 sporadic hypertrophic cardiomyopathy [ SHCM ] and 60 familial hypertrophic cardiomyopathy [ FHCM ] ) patients and 165 age- and sex-matched normal healthy controls without known hypertension and left ventricular hypertrophy were included in the study .

Example answer:
{"entities": [{"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sporadic hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "familial hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular hypertrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A retrospective study was carried out on paraffin-embedded sections from 113 patients diagnosed of advanced CRC .

Example answer:
{"entities": [{"text": "paraffin-embedded", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : One hundred and fifty-eight patients with wet AMD , 80 patients with soft drusen , and 220 matched control subjects were recruited among Han Chinese in mainland China .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: METHODS : Two hundred eighty SSc cases containing 29/280 having PAH diagnosed by catheterism were compared with 140 patients with osteoarthritis .

## Item biored:test:403
Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mutations associated with lamivudine-resistance in therapy-na ve hepatitis B virus ( HBV ) infected patients with and without HIV co-infection : implications for antiretroviral therapy in HBV and HIV co-infected South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistance", "type": "ChemicalEntity"}, {"text": "hepatitis B virus ( HBV ) infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HIV co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV and HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This was an exploratory study to investigate lamivudine-resistant hepatitis B virus ( HBV ) strains in selected lamivudine-na ve HBV carriers with and without human immunodeficiency virus ( HIV ) co-infection in South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus", "type": "OrganismTaxon"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-na", "type": "ChemicalEntity"}, {"text": "human immunodeficiency virus ( HIV ) co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: One month after starting the antiviral therapy , the patient was admitted to the hospital because he developed rhabdomyolysis .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Capecitabine has a well-established safety profile and can be given safely to patients with advanced age , hepatic and renal dysfunctions .

Example answer:
{"entities": [{"text": "Capecitabine", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hepatic and renal dysfunctions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Acute renal failure in patients with AIDS on tenofovir while receiving prolonged vancomycin course for osteomyelitis .

Example answer:
{"entities": [{"text": "Acute renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "AIDS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tenofovir", "type": "ChemicalEntity"}, {"text": "vancomycin", "type": "ChemicalEntity"}, {"text": "osteomyelitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Example input:
Sentence: It remains to be seen whether such pre-existing antiviral mutations could result in widespread emergence of HBV resistant strains when lamivudine-containing highly active antiretroviral ( ARV ) treatment ( HAART ) regimens become widely applied in South Africa , as this is likely to have potential implications in the management of HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-containing", "type": "ChemicalEntity"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: To determine the incidence of clinically significant adverse events after long-term , fixed-dose , generic highly active antiretroviral therapy ( HAART ) use among HIV-infected individuals in South India , we examined the experiences of 3154 HIV-infected individuals who received a minimum of 3 months of generic HAART between February 1996 and December 2006 at a tertiary HIV care referral center in South India .

Example answer:
{"entities": [{"text": "HIV-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Individuals with HIV can now live long lives with drug therapy that often includes protease inhibitors such as ritonavir .

## Item biored:test:405
Example input:
Sentence: Tumors implanted in LKB1 ( endo-/- ) mice but not macrophage-specific LKB1-knockout mice grew faster and showed enhanced vascular permeability and increased angiogenesis as compared with those implanted in wild-type mice .

Example answer:
{"entities": [{"text": "Tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "LKB1-knockout", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Controlling for relevant covariates , we also found treatment with selective serotonin reuptake inhibitors ( SSRIs ) to be associated with lower trabecular BMD at the radius ( P = .03 ) and BMD z score at the lumbar spine ( P < .05 ) .

Example answer:
{"entities": [{"text": "selective serotonin reuptake inhibitors", "type": "ChemicalEntity"}, {"text": "SSRIs", "type": "ChemicalEntity"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Improved cardiac function and less scar formation were observed in TIEG1 KO mice , and we also observed the altered expression of phosphatase and tensin homolog ( Pten ) , Akt and Bcl-2/Bax , as well as vascular endothelial growth factor ( VEGF ) .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "Pten", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2/Bax", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : This is the first study to link risperidone-induced hyperprolactinemia and SSRI treatment to lower BMD in children and adolescents .

Example answer:
{"entities": [{"text": "risperidone-induced", "type": "ChemicalEntity"}, {"text": "hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SSRI", "type": "ChemicalEntity"}]}

Example input:
Sentence: Atherosclerosis could produce gastric hemorrhagic ulcer via aggravation of gastric acid back-diffusion , LPO generation , histamine release and microvascular permeability that could be ameliorated by verapamil in rats .

Example answer:
{"entities": [{"text": "Atherosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric hemorrhagic ulcer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LPO", "type": "ChemicalEntity"}, {"text": "histamine", "type": "ChemicalEntity"}, {"text": "verapamil", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The effects of METH in CX3CR1 knockout mice were not gender-dependent and did not extend beyond the striatum .

Example answer:
{"entities": [{"text": "METH", "type": "ChemicalEntity"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Male Wistar rats were challenged intragastrically once daily for 9 days with 1.0 ml/kg of corn oil containing vitamin D2 and cholesterol to induce atherosclerosis .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "corn oil", "type": "ChemicalEntity"}, {"text": "vitamin D2", "type": "ChemicalEntity"}, {"text": "cholesterol", "type": "ChemicalEntity"}, {"text": "atherosclerosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Male CD-1 mice were treated with warfarin ( 2 mg/kg over 24 h ) , resulting in a mean ( +/-s.d . )

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Input:
Sentence: We have previously demonstrated that ritonavir treatment increases atherosclerotic lesion formation in male mice to a greater extent than in female mice .

## Item biored:test:380
Example input:
Sentence: His condition was further complicated by septicaemia and meningitis caused by infection with extended-spectrum beta-lactamase-producing Klebsiella pneumoniae .

Example answer:
{"entities": [{"text": "septicaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "meningitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Klebsiella pneumoniae", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Viruses were evaluated for replication in SCID mice transplanted with human hepatoma cells ( SCID-HuH-7 mice ) , in mosquitoes , and in rhesus monkeys .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "hepatoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCID-HuH-7", "type": "CellLine"}, {"text": "rhesus monkeys", "type": "OrganismTaxon"}]}

Example input:
Sentence: One patient with a severe cellular and clinical phenotype was a compound heterozygote with POLG1 mutations in the polymerase and exonuclease domain intrans .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Interestingly , DCs that were co-treated with cisplatin and lipopolysaccharide ( LPS ) exhibited a decreased immunostimulatory capacity for inducing the proliferation of Th1- and Th17-type T cells ; instead , these DCs contributed to Th2-type T cell immunity .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "lipopolysaccharide", "type": "ChemicalEntity"}, {"text": "LPS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Because human immunodeficiency virus type 1 ( HIV-1 ) Tat protein causes depressive-like behavior in mice , we investigated its ability to activate IDO in organotypic hippocampal slice cultures ( OHSCs ) derived from neonatal C57BL/6 mice .

Example answer:
{"entities": [{"text": "human immunodeficiency virus type 1", "type": "OrganismTaxon"}, {"text": "HIV-1", "type": "OrganismTaxon"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "depressive-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Twenty-one had Alpers syndrome , the commonest severe POLG1 autosomal recessive phenotype , comprising hepatoencephalopathy and often mtDNA depletion .

Example answer:
{"entities": [{"text": "Alpers syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}, {"text": "hepatoencephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One month after starting the antiviral therapy , the patient was admitted to the hospital because he developed rhabdomyolysis .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Input:
Sentence: An extremely rare case of delusional parasitosis in a chronic hepatitis C patient during pegylated interferon alpha-2b and ribavirin treatment .

## Item biored:test:385
Example input:
Sentence: Because human immunodeficiency virus type 1 ( HIV-1 ) Tat protein causes depressive-like behavior in mice , we investigated its ability to activate IDO in organotypic hippocampal slice cultures ( OHSCs ) derived from neonatal C57BL/6 mice .

Example answer:
{"entities": [{"text": "human immunodeficiency virus type 1", "type": "OrganismTaxon"}, {"text": "HIV-1", "type": "OrganismTaxon"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "depressive-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperlipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fatigue", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "fulminant hepatic failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One month after starting the antiviral therapy , the patient was admitted to the hospital because he developed rhabdomyolysis .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Input:
Sentence: We present a 49-year-old woman who developed a delusional parasitosis during treatment with pegylated interferon alpha-2b weekly and ribavirin .

## Item biored:test:442
Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , our study suggests that p.R246Q mutation is common amongst patients with SRD5A2 gene defect from the Northern states of India .

Example answer:
{"entities": [{"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We progressively screened DNA samples from 613 individuals with ID initially for the most frequent ARX mutations ( c.304ins ( GCG ) ( 7 ) 'expansion ' of pA1 and c.429_452dup 'dup24bp ' of pA2 ) .

Example answer:
{"entities": [{"text": "ID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARX", "type": "GeneOrGeneProduct"}, {"text": "c.304ins ( GCG ) ( 7 )", "type": "SequenceVariant"}, {"text": "c.429_452dup", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : The authors obtained a significant maximum parametric LOD ( logarithm of odds ) score of Z ( max ) = 3.72 on chromosome 8q22 and identified a homozygous missense mutation in the gene MKS3/TMEM67 .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel variant ( K294E ) was identified in a single heterozygous individual with prostate cancer .

Example answer:
{"entities": [{"text": "K294E", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Whereas no mutations were detected in the PDE6H gene , mutations in KCNV2 were identified in all patients , in either the homozygous or compound heterozygous state .

Example answer:
{"entities": [{"text": "PDE6H", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: We did not find this PKD2 variant in a screen of 280 chromosomes of healthy subjects , supporting its pathogenicity .

## Item biored:test:444
Example input:
Sentence: NEK2 , as the most obviously different DEG in cells and tissues from the RNA-seq data , was listed as an HCC candidate biomarker for further verification .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: qRT-PCR detected similar patterns of changes in AQP2 mRNA in the medulla but not in the cortex .

Example answer:
{"entities": [{"text": "AQP2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : PBMCs with the heterozygous and homozygous SLURP-1 G86R mutation had defective T-cell activation .

Example answer:
{"entities": [{"text": "SLURP-1", "type": "GeneOrGeneProduct"}, {"text": "G86R", "type": "SequenceVariant"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA from peripheral nuclear blood cells was genotyped for 5-HTTLPR using standard polymerase chain reaction methods.A significant group effect was observed only on memory function tasks ( p = 0.04 ) but not on reaction times ( p = 0.61 ) or attention/executive functioning ( p = 0.59 ) .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Gene expression was analyzed by quantitative real-time PCR using RNA from peripheral blood mononuclear cells ( PBMC ) .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Real-time PCR of the PKD2 transcript from a skin biopsy revealed 20-fold higher expression in the patient than in a healthy subject and was higher in the patient 's peripheral blood mononuclear cells ( PBMCs ) than in those of her heterozygote daughter and a healthy subject .

## Item biored:test:411
Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Knockdown of either NOX4 or STAT3 inhibited VEGF-induced EC proliferation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , the abundance and proliferative index of lymph node , thymus and CNS CD4 ( + ) CD25 ( + ) FoxP3 ( + ) Tregs were strikingly reduced in VPAC2-deficient mice with EAE .

Example answer:
{"entities": [{"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "FoxP3", "type": "GeneOrGeneProduct"}, {"text": "VPAC2-deficient", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Exposure to azathioprine ( > or =2 microg/mL ) for 48 hours increased cytosolic Ca2+ activity and annexin V binding and decreased forward scatter .

Example answer:
{"entities": [{"text": "azathioprine", "type": "ChemicalEntity"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PGA2 enhanced the EC barrier and protected against barrier dysfunction caused by vasoactive peptide thrombin and proinflammatory bacterial wall lipopolysaccharide ( LPS ) .

Example answer:
{"entities": [{"text": "PGA2", "type": "ChemicalEntity"}, {"text": "thrombin", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipopolysaccharide", "type": "ChemicalEntity"}, {"text": "LPS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Angiotensin II subtype 1a receptor signaling in resident hepatic macrophages induces liver metastasis formation .

Example answer:
{"entities": [{"text": "Angiotensin II subtype 1a receptor", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In LPA2-reconstituted MEF cells lacking LPA1 ' 3 the levels of gamma-H2AX decreased rapidly , whereas in Vector MEF were high and remained sustained .

Example answer:
{"entities": [{"text": "LPA2-reconstituted", "type": "GeneOrGeneProduct"}, {"text": "MEF", "type": "CellLine"}, {"text": "LPA1 ' 3", "type": "GeneOrGeneProduct"}, {"text": "gamma-H2AX", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: E2 decreased the accumulation of cholesteryl esters in macrophages following ritonavir treatment .

## Item biored:test:427
Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Genetic analysis identified a novel V876E mutation in all HypoPP patients in the family , but not in normal family members or 160 control people .

Example answer:
{"entities": [{"text": "V876E", "type": "SequenceVariant"}, {"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: We identified and characterized a PABPN1 mutation in a Taiwanese family with OPMD .

Example answer:
{"entities": [{"text": "PABPN1", "type": "GeneOrGeneProduct"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The mother and daughter were each heterozygous for PPARG nonsense mutation Y355X , whose protein product in vitro was transcriptionally inactive with no dominant-negative activity against the wild-type receptor .

Example answer:
{"entities": [{"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "Y355X", "type": "SequenceVariant"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We describe a novel germline mutation of BMPR1A in a family with juvenile polyposis and colon cancer .

Example answer:
{"entities": [{"text": "BMPR1A", "type": "GeneOrGeneProduct"}, {"text": "juvenile polyposis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report here a new family with X-linked mental retardation due to mutation in OPHN1 and present unpublished data about two families previously reported , concerning the facial and psychological phenotype of affected males and carrier females .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPHN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: In conclusion , we reported on a family in which an asymptomatic woman with somatic-gonadal mosaicism for a RPGR gene mutation transmitted the mutation to an asymptomatic daughter and to a son with XLRP .

## Item biored:test:471
Example input:
Sentence: Although the underlying mechanism ( s ) are not well understood , these effects may involve an increase in acetylcholine ( ACh ) levels .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "ChemicalEntity"}, {"text": "ACh", "type": "ChemicalEntity"}]}

Example input:
Sentence: Further validation by population-based case-control studies and rigorous mechanistic studies is warranted .

Example answer:
{"entities": []}

Example input:
Sentence: Little is known regarding the mechanisms underlying this invasive behavior .

Example answer:
{"entities": []}

Example input:
Sentence: This molecular study reveals a naturally occurring mechanism where the effect of either modifier genes or epigenetic factors could be suspected .

Example answer:
{"entities": []}

Example input:
Sentence: This mechanism can be considered as a target to protect infarcted myocardium .

Example answer:
{"entities": [{"text": "infarcted myocardium", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Future research should evaluate the longitudinal course of this adverse event to determine its temporal stability and whether a higher fracture rate ensues .

Example answer:
{"entities": [{"text": "fracture", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , the regulatory mechanisms for CIN remain to be fully elucidated .

Example answer:
{"entities": [{"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our results may help to analyze novel data obtained using similar experimental models and the simple analysis method described here can be used in similar studies to investigate the basic neuronal mechanism of this or other types of experimental epilepsies .

Example answer:
{"entities": [{"text": "epilepsies", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The mechanism may be related to the improvement of Ca ( 2+ ) handling .

Example answer:
{"entities": [{"text": "Ca ( 2+ )", "type": "ChemicalEntity"}]}

Example input:
Sentence: We suggest that such misregulation is the predominant mechanism of the association we report here .

Example answer:
{"entities": []}

Input:
Sentence: Some other mechanism than those being reported herein should be further investigated .

## Item biored:test:369
Example input:
Sentence: Patients who develop ESRD have a higher preoperative and 1-year serum creatinine and are more likely to have hepatorenal syndrome .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: There was also an excess of MB in warfarin users vs nonusers with ICH ( OR , 2.7 ; 95 % CI , 1.6-4.4 ; P < 0.001 ) but none in warfarin users with IS/TIA ( OR , 1.3 ; 95 % CI , 0.9-1.7 ; P=0.33 ; P difference=0.01 ) .

Example answer:
{"entities": [{"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The area of histochemical injury ( as a percent of the cross-sectional area of the hemisphere ) was less in the hypertensive group ( 33 +/- 3 % vs 21 +/- 2 % , P less than 0.05 ) .

Example answer:
{"entities": [{"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report a case of prolonged neuromuscular block after administration of suxamethonium leading to the discovery of a novel BCHE variant ( c.695T > A , p.Val204Asp ) .

Example answer:
{"entities": [{"text": "neuromuscular block", "type": "DiseaseOrPhenotypicFeature"}, {"text": "suxamethonium", "type": "ChemicalEntity"}, {"text": "BCHE", "type": "GeneOrGeneProduct"}, {"text": "c.695T > A", "type": "SequenceVariant"}, {"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Example input:
Sentence: In pooled follow-up data for 768 antithrombotic users , presence of MB at baseline was associated with a substantially increased risk of subsequent ICH ( OR , 12.1 ; 95 % CI , 3.4-42.5 ; P < 0.001 ) .

Example answer:
{"entities": [{"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We concluded that the CASP8 -652 6N del variant allele may contribute to the risk of developing SCCHN in non-Hispanic white populations .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : In a pooled analysis of 1460 ICH and 3817 IS/TIA , MB were more frequent in ICH vs IS/TIA in all treatment groups , but the excess increased from 2.8 ( odds ratio ; range , 2.3-3.5 ) in nonantithrombotic users to 5.7 ( range , 3.4-9.7 ) in antiplatelet users and 8.0 ( range , 3.5-17.8 ) in warfarin users ( P difference=0.01 ) .

Example answer:
{"entities": [{"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: In these trials , Hp typing of 69 DM individuals and treating those with the Hp 2-2 with vitamin E prevented one myocardial infarct , stroke or cardiovascular death .

Example answer:
{"entities": [{"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "myocardial infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiovascular death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the periphery of the ischemic territory , SG in the cortex was greater ( less edema accumulation ) in the hypertensive group ( 1.041 +/- 0.001 vs 1.039 +/- 0.001 , P less than 0.05 ) .

Example answer:
{"entities": [{"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSIONS : Thus the frequency of 6bINS differs between SSc patients with or without PAH , suggesting the implication of ENG in this devastating vascular complication of SSc .

## Item biored:test:402
Example input:
Sentence: Estrogen replacement ( 17beta-estradiol subcutaneous pellet , 14.2 microg/day , 12 wk ) of Ovx rats restored the hemodynamic and locomotor effects of alpha-methyldopa to sham-operated levels .

Example answer:
{"entities": [{"text": "17beta-estradiol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}]}

Example input:
Sentence: Angiotensin II subtype 1a receptor signaling in resident hepatic macrophages induces liver metastasis formation .

Example answer:
{"entities": [{"text": "Angiotensin II subtype 1a receptor", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , Sal administration significantly suppresses epithelial-mesenchymal transition ( EMT ) , as evidenced by a decreased expression of alpha-SMA , vimentin , TGF-beta1 , snail , slug , and a largely restored expression of E-cadherin .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "alpha-SMA", "type": "GeneOrGeneProduct"}, {"text": "vimentin", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "snail", "type": "GeneOrGeneProduct"}, {"text": "slug", "type": "GeneOrGeneProduct"}, {"text": "E-cadherin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: One month of oral galactose treatment initiated immediately after the STZ-icv administration , successfully prevented development of the STZ-icv-induced cognitive deficits .

Example answer:
{"entities": [{"text": "galactose", "type": "ChemicalEntity"}, {"text": "STZ-icv", "type": "ChemicalEntity"}, {"text": "STZ-icv-induced", "type": "ChemicalEntity"}, {"text": "cognitive deficits", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Knockdown of either NOX4 or STAT3 inhibited VEGF-induced EC proliferation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Testosterone ( 1 mg.kg ( -1 ) .d ( -1 ) , sc ) , the androgen receptor antagonist flutamide ( 10 mg.kg ( -1 ) .d ( -1 ) , ip ) , the estrogen receptor antagonist tamoxifen ( 1 mg.kg ( -1 ) .d ( -1 ) , ip ) or the aromatase inhibitor letrozole ( 4 mg.kg ( -1 ) .d ( -1 ) , ip ) were administered for 6 d after the first injection of STZ .

Example answer:
{"entities": [{"text": "Testosterone", "type": "ChemicalEntity"}, {"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "flutamide", "type": "ChemicalEntity"}, {"text": "estrogen receptor", "type": "GeneOrGeneProduct"}, {"text": "tamoxifen", "type": "ChemicalEntity"}, {"text": "aromatase", "type": "GeneOrGeneProduct"}, {"text": "letrozole", "type": "ChemicalEntity"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Methadone , an agonist of OPRM1 , enhances the sensitivity of parental leukemic cells , but not OPRM1-depleted cells , to L-asparaginase treatment , indicating that OPRM1 is required for the synergistic action of L-asparaginase and methadone , and that OPRM1 loss promotes leukemic cell survival likely through downregulation of the OPRM1-mediated apoptotic pathway .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "methadone", "type": "ChemicalEntity"}, {"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Estrogen prevents cholesteryl ester accumulation in macrophages induced by the HIV protease inhibitor ritonavir .

## Item biored:test:443
Example input:
Sentence: We then examined them on genomic DNA in six MODY probands without mutations in the MODY1 , MODY3 and MODY4 genes and in 54 patients with late-onset Type II diabetes by combined single strand conformational polymorphism-heteroduplex analysis followed by direct sequencing of identified variants .

Example answer:
{"entities": [{"text": ",", "type": "GeneOrGeneProduct"}, {"text": "II diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Peroxisomal proliferator activated receptor-gamma deficiency in a Canadian kindred with familial partial lipodystrophy type 3 ( FPLD3 ) .

Example answer:
{"entities": [{"text": "Peroxisomal proliferator activated receptor-gamma", "type": "GeneOrGeneProduct"}, {"text": "familial partial lipodystrophy type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The antibody reacted with the 80 kDa band protein in control fibroblasts , while no bands were detected in the fibroblasts from a patient with ALD ( # 163 ) , in which mRNA of the ALD gene was undetectable based on Northern blot analysis .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "ALD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel mutation in the connexin 26 gene ( GJB2 ) in a child with clinical and histological features of keratitis-ichthyosis-deafness ( KID ) syndrome .

Example answer:
{"entities": [{"text": "connexin 26", "type": "GeneOrGeneProduct"}, {"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "keratitis-ichthyosis-deafness ( KID ) syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We identified and characterized a PABPN1 mutation in a Taiwanese family with OPMD .

Example answer:
{"entities": [{"text": "PABPN1", "type": "GeneOrGeneProduct"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The exon 4 sequence of TGFBI of the proband exhibits the heterozygous single-nucleotide mutation , C417T , leading to amino acid substitution ( R124C ) in the encoded TGF-induced protein .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "C417T", "type": "SequenceVariant"}, {"text": "R124C", "type": "SequenceVariant"}, {"text": "TGF-induced protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: Probands had at least one developmentally missing tooth , excluding third molars .

Example answer:
{"entities": []}

Input:
Sentence: The proband 's parents did not have the PKD1 mutation .

## Item biored:test:452
Example input:
Sentence: Prehospital care providers who are managing any patient with a syncopal episode that fails to recover within a reasonable time frame should consider the Bezold-Jarisch reflex as the cause and manage the patient accordingly .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "syncopal episode", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The most relevant adverse event was peripheral neuropathy , which occurred in 78 % of the patients ( grade II , 38 % ; grade III , 21 % ) and led to treatment discontinuation in 6 % .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: MATERIAL AND METHODS : Case-control study of 50 obese patients undergoing bariatric surgery and 71 non-obese subjects matched by age and sex .

Example answer:
{"entities": [{"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: MATERIAL AND METHODS : This study was performed based on anesthesia records .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Six affected family members were examined clinically including visual acuity , color cornea photography , applanation tonography , and fundoscopy .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : An in-depth chart review was undertaken in all 24 patients who developed perioperative seizures .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CLINICAL FEATURES : A 50-year-old woman with low back and right leg pain was scheduled for epidural steroid injection .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "low back and right leg pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steroid", "type": "ChemicalEntity"}]}

Example input:
Sentence: A prospective , randomized , double-blind pilot study to compare the results of stereotactic unilateral pallidotomy and subthalamotomy in advanced idiopathic Parkinson 's disease ( PD ) refractory to medical treatment was designed .

Example answer:
{"entities": [{"text": "idiopathic Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Ninety-three patients with APA were assessed for postoperative resolution of hypertension .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Clinical evaluation included the use of the Unified Parkinson 's Disease Rating Scale ( UPDRS ) , Hoehn_Yahr score and Schwab England activities of daily living ( ADL ) score in 'on'- and 'off'-drug conditions before surgery and 6 months after surgery .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: METHODS : With ethical approval , we studied 74 American Society of Anesthesiologists ( ASA ) , physical status class 1 and 2 patients scheduled for elective unilateral lower limb surgery .

## Item biored:test:453
Example input:
Sentence: Ten consecutive patients ( mean age , 58.4 +/- 6.8 years ; 7 men , 3 women ) with similar characteristics at the duration of disease ( mean disease time , 8.4 +/- 3.5 years ) , disabling motor fluctuations ( Hoehn _ Yahr stage 3-5 in off-drug phases ) and levodopa-induced dyskinesias were selected .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesias", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "allopurinol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Patients were divided into three groups and each group had 20 patients .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Anesthesia was continued uneventfully with propofol infusion while all facilities were available to detect and treat malignant hyperthermia .

Example answer:
{"entities": [{"text": "propofol", "type": "ChemicalEntity"}, {"text": "malignant hyperthermia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A prospective , randomized , double-blind pilot study to compare the results of stereotactic unilateral pallidotomy and subthalamotomy in advanced idiopathic Parkinson 's disease ( PD ) refractory to medical treatment was designed .

Example answer:
{"entities": [{"text": "idiopathic Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: After verifying the epidural space , bupivacaine and triamcinolone diacetate were injected .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "triamcinolone diacetate", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Six patients in the conventional group had a positive culture , compared with none in the extended-interval group ( P = 0.002 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Six patients were operated on in the globus pallidus interna ( GPi ) and four in the subthalamic nucleus ( STN ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Patients were randomly allocated to either receive or not receive 1 1 fentanyl , while a third group received dexamethasone in addition to fentanyl .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "fentanyl", "type": "ChemicalEntity"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Input:
Sentence: Patients were randomly allocated into one of two groups : lateral and conventional spinal anaesthesia groups .

## Item biored:test:425
Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Eleven subjects presented SRD5A2 homozygous single-base mutations ( two first cousins and four unrelated patients with G183S , two with R246W , one with del642T , one with G196S , and one with 217_218insC plus the A49T variant in heterozygosis ) , whereas four were compound heterozygotes ( one with Q126R/IVS3+1G > A , one with Q126R/del418T , and two brothers with Q126R/G158R ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "G183S", "type": "SequenceVariant"}, {"text": "R246W", "type": "SequenceVariant"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}, {"text": "A49T", "type": "SequenceVariant"}, {"text": "Q126R/IVS3+1G > A", "type": "SequenceVariant"}, {"text": "Q126R/del418T", "type": "SequenceVariant"}, {"text": "Q126R/G158R", "type": "SequenceVariant"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Identification and molecular characterization of six novel mutations in the UDP-N-acetylglucosamine-1-phosphotransferase gamma subunit ( GNPTG ) gene in patients with mucolipidosis III gamma .

Example answer:
{"entities": [{"text": "UDP-N-acetylglucosamine-1-phosphotransferase gamma subunit", "type": "GeneOrGeneProduct"}, {"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "mucolipidosis III gamma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Example input:
Sentence: Of them , two patients carrying E359K mutation were from two generations in one family with ventricular septal defect ( VSD ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A single heterozygous missense mutation , substitution of a cytosine residue with thymidine in exon 2 of MSH5 , was found in two Caucasian women in whom POF developed at 18 and 36 years of age .

Example answer:
{"entities": [{"text": "cytosine residue with thymidine", "type": "SequenceVariant"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a study of 10 patients from seven families with a clinical phenotype and enzymatic diagnosis of MLIII , six novel GNPTG gene mutations were identified .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "MLIII", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GNPTG", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: L1503R is a member of group I mutation and has dominant-negative effect on secretion of full-length VWF multimers : an analysis of two patients with type 2A von Willebrand disease .

Example answer:
{"entities": [{"text": "L1503R", "type": "SequenceVariant"}, {"text": "VWF", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "type 2A von Willebrand disease", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: A g.ORF15 + 652-653delAG mutation was identified in second- and third-generation patients/carriers .

## Item biored:test:455
Example input:
Sentence: After verifying the epidural space , bupivacaine and triamcinolone diacetate were injected .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "triamcinolone diacetate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here , we describe a case of severe masseter muscle rigidity ( jaw of steel ) after succinylcholine ( Sch ) administration during general anesthetic management for rigid bronchoscopic removal of a tracheal foreign body .

Example answer:
{"entities": [{"text": "masseter muscle rigidity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "jaw of steel", "type": "DiseaseOrPhenotypicFeature"}, {"text": "succinylcholine", "type": "ChemicalEntity"}, {"text": "Sch", "type": "ChemicalEntity"}]}

Example input:
Sentence: After the injection , there was a reduction in radicular symptoms .

Example answer:
{"entities": []}

Example input:
Sentence: After a short period of basal activity recording , epileptic focus was induced by injecting 400IU/2 microl penicillin-G potassium into the left lateral ventricle while the cortical activity was continuously recorded .

Example answer:
{"entities": [{"text": "epileptic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "penicillin-G potassium", "type": "ChemicalEntity"}]}

Example input:
Sentence: CLINICAL FEATURES : A 50-year-old woman with low back and right leg pain was scheduled for epidural steroid injection .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "low back and right leg pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steroid", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A prospective , randomized , double-blind pilot study to compare the results of stereotactic unilateral pallidotomy and subthalamotomy in advanced idiopathic Parkinson 's disease ( PD ) refractory to medical treatment was designed .

Example answer:
{"entities": [{"text": "idiopathic Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: There was statistically significant improvement in all contralateral major parkinsonian motor signs in all patients followed for 6 months .

Example answer:
{"entities": [{"text": "parkinsonian", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: However , intraspinal injection of 5,7-DHT to produce a more selective lesion of only descending serotonin projections in the spinal cord did not affect this hypotension .

Example answer:
{"entities": [{"text": "5,7-DHT", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Complications were observed in two patients : one had a left homonymous hemianopsia after pallidotomy and another one developed left hemiballistic movements 3 days after subthalamotomy which partly improved within 1 month with Valproate 1000 mg/day .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "homonymous hemianopsia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Valproate", "type": "ChemicalEntity"}]}

Input:
Sentence: Patients in the unilateral group were maintained in the lateral position for 15 minutes following spinal injection while those in the conventional group were turned supine immediately after injection .

## Item biored:test:381
Example input:
Sentence: CONCLUSIONS : High serum levels of inflammatory chemokines such as CCL4 and CCL5 in the serum of cirrhotic patients indicate the presence of HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Irinotecan is an anti-neoplastic agent that is widely used for treating colorectal and lung cancers , but often causes toxicities such as severe myelosuppression and diarrhea .

Example answer:
{"entities": [{"text": "Irinotecan", "type": "ChemicalEntity"}, {"text": "colorectal and lung cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "toxicities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diarrhea", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Most hepatocellular carcinomas ( HCC ) develop as a result of chronic liver inflammation .

Example answer:
{"entities": [{"text": "hepatocellular carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chronic liver inflammation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interestingly , DCs that were co-treated with cisplatin and lipopolysaccharide ( LPS ) exhibited a decreased immunostimulatory capacity for inducing the proliferation of Th1- and Th17-type T cells ; instead , these DCs contributed to Th2-type T cell immunity .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "lipopolysaccharide", "type": "ChemicalEntity"}, {"text": "LPS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Upon stimulation with various TLR agonists , cisplatin-treated DCs showed markedly increased IL-10 production through activation of the p38 MAPK and NF-kappaB signaling pathways without altering the levels of TNF-alpha and IL-12p70 , indicating the cisplatin-mediated induction of tolerogenic DCs .

Example answer:
{"entities": [{"text": "TLR", "type": "GeneOrGeneProduct"}, {"text": "cisplatin-treated", "type": "ChemicalEntity"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "p38 MAPK", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-12p70", "type": "GeneOrGeneProduct"}, {"text": "cisplatin-mediated", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Input:
Sentence: During treatment of chronic hepatitis C patients with interferon and ribavirin , a lot of side effects are described .

## Item biored:test:410
Example input:
Sentence: An experimental group of rats was treated with puromycin aminonucleoside ( PAN ; 180 mg/kg iv ) , whereas the control group received only vehicle .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "puromycin aminonucleoside", "type": "ChemicalEntity"}, {"text": "PAN", "type": "ChemicalEntity"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: H9c2 cells were treated with Dox ( 1 uM ) and/or BDNF ( 400 ng/ml ) for 24 hrs .

Example answer:
{"entities": []}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In all clones with combined immune escape and LAM resistance mutations , the nucleotide analogues adefovir and tenofovir remained effective in suppressing viral replication in vitro .

Example answer:
{"entities": [{"text": "LAM", "type": "ChemicalEntity"}, {"text": "adefovir", "type": "ChemicalEntity"}, {"text": "tenofovir", "type": "ChemicalEntity"}]}

Example input:
Sentence: We performed RNA-seq of the HCC cell line SMMC-7721 and the normal liver cell line HL-7702 using the Ion Proton System .

Example answer:
{"entities": [{"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SMMC-7721", "type": "CellLine"}, {"text": "HL-7702", "type": "CellLine"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Input:
Sentence: Cells were then treated with 30 ng/ml ritonavir or vehicle in the presence of aggregated LDL for 24 h. Cell extracts were harvested , and lipid or total RNA was isolated .

## Item biored:test:459
Example input:
Sentence: Mice subjected to hypotensive episodes showed a significant decrease in latency time ( 178 +/- 156 s ) compared with those injected with saline , NTG + NIMO , or delayed NTG ( 580 +/- 81 s , 557 +/- 67 s , and 493 +/- 146 s , respectively ) .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: Additional predictors of persistent postoperative hypertension included duration of hypertension ( P < .0005 ) , family history of hypertension ( P = .001 ) , and elevated systolic blood pressure ( P = .015 ) .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , there was no significant difference in the lidocaine concentrations measured when the systolic blood pressure became 70 mmHg .

Example answer:
{"entities": [{"text": "lidocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: None of the subjects treated with buprenorphine had QTc interval > 0.440 s ( ( 1/2 ) ) .

Example answer:
{"entities": [{"text": "buprenorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Systolic blood pressure ( SBP ) was measured on alternate days using the tail-cuff method .

Example answer:
{"entities": []}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Six patients in the conventional group had a positive culture , compared with none in the extended-interval group ( P = 0.002 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mean changes in MSDBP and mean sitting systolic BP ( MSSBP ) were analyzed at the 8-week core study end point .

Example answer:
{"entities": []}

Example input:
Sentence: In a separate group of mice not subjected to behavioral studies , the same dose of NTG ( n = 3 ) and NTG + NIMO ( n = 3 ) caused mean arterial blood pressure to decrease from 85.9 +/- 3.8 mm Hg sem to 31.6 +/- 0.8 mm Hg sem and from 86.2 +/- 3.7 mm Hg sem to 32.6 +/- 0.2 mm Hg sem , respectively .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: Patients with essential hypertension ( mean sitting diastolic BP [ MSDBP ] , > or =95 mm Hg and < 110 mm Hg ) were randomized to 1 of 8 treatment groups : VAL 160 or 320 mg ; HCTZ 12.5 or 25 mg ; VAL/HCTZ 160/12.5 , 320/12.5 , or 320/25 mg ; or placebo .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "essential hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Input:
Sentence: Patients in the conventional group had statistically significant greater fall in the systolic blood pressures at 15 , 30 and 45 minutes when compared to the baseline ( P= 0.003 , 0.001 and 0.004 ) .

## Item biored:test:360
Example input:
Sentence: FLSs were separated from synovial tissues ( STs ) from patients with RA and osteoarthritis ( OA ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "osteoarthritis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations in phospholipase C epsilon 1 are not sufficient to cause diffuse mesangial sclerosis .

Example answer:
{"entities": [{"text": "phospholipase C epsilon 1", "type": "GeneOrGeneProduct"}, {"text": "diffuse mesangial sclerosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the periphery of the ischemic territory , SG in the cortex was greater ( less edema accumulation ) in the hypertensive group ( 1.041 +/- 0.001 vs 1.039 +/- 0.001 , P less than 0.05 ) .

Example answer:
{"entities": [{"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Taken together , our results demonstrated that Sag is a Kras ( G12D ) -cooperating oncogene required for Kras ( G12D ) -induced immortalization and transformation , and targeting SAG-SCF E3 ligase may , therefore , have therapeutic value for senescence-based cancer treatment .

Example answer:
{"entities": [{"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}, {"text": "SAG-SCF", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: GADD45A-expressing HSCs failed to long-term reconstitute the blood of recipients by inducing multilineage differentiation in vivo .

Example answer:
{"entities": [{"text": "GADD45A-expressing", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: More than 100 different heterozygous mutations in copper/zinc superoxide dismutase ( SOD1 ) have been found in patients with amyotrophic lateral sclerosis ( ALS ) , a fatal neurodegenerative disease .

Example answer:
{"entities": [{"text": "copper/zinc superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegenerative disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: D90A-SOD1 mediated amyotrophic lateral sclerosis : a single founder for all cases with evidence for a Cis-acting disease modifier in the recessive haplotype .

Example answer:
{"entities": [{"text": "D90A-SOD1", "type": "SequenceVariant"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Late-onset scleroderma renal crisis induced by tacrolimus and prednisolone : a case report .

Example answer:
{"entities": [{"text": "scleroderma renal crisis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tacrolimus", "type": "ChemicalEntity"}, {"text": "prednisolone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , there have been reports of thrombotic microangiopathy precipitated by cyclosporine in patients with SSc .

Example answer:
{"entities": [{"text": "thrombotic microangiopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cyclosporine", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SSc", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Scleroderma renal crisis ( SRC ) is a rare complication of systemic sclerosis ( SSc ) but can be severe enough to require temporary or permanent renal replacement therapy .

Example answer:
{"entities": [{"text": "Scleroderma renal crisis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SRC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "systemic sclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SSc", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Systemic sclerosis ( SSc ) is a connective tissue disorder characterized by early generalized microangiopathy with disturbed angiogenesis .

## Item biored:test:450
Example input:
Sentence: Here , we report a case of prolonged neuromuscular block after administration of suxamethonium leading to the discovery of a novel BCHE variant ( c.695T > A , p.Val204Asp ) .

Example answer:
{"entities": [{"text": "neuromuscular block", "type": "DiseaseOrPhenotypicFeature"}, {"text": "suxamethonium", "type": "ChemicalEntity"}, {"text": "BCHE", "type": "GeneOrGeneProduct"}, {"text": "c.695T > A", "type": "SequenceVariant"}, {"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Example input:
Sentence: Previous experiments in this laboratory have shown that microinjection of methyldopa onto the ventrolateral cells of the B3 serotonin neurons in the medulla elicits a hypotensive response mediated by a projection descending into the spinal cord .

Example answer:
{"entities": [{"text": "methyldopa", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we describe a case of severe masseter muscle rigidity ( jaw of steel ) after succinylcholine ( Sch ) administration during general anesthetic management for rigid bronchoscopic removal of a tracheal foreign body .

Example answer:
{"entities": [{"text": "masseter muscle rigidity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "jaw of steel", "type": "DiseaseOrPhenotypicFeature"}, {"text": "succinylcholine", "type": "ChemicalEntity"}, {"text": "Sch", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND AND OBJECTIVE : Despite advantages of induction and maintenance of anaesthesia with sevoflurane , postoperative nausea and vomiting occurs frequently .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "postoperative nausea and vomiting", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : This double-blind study examined the incidence and severity of postoperative nausea and vomiting and pain in the first 24 h after sevoflurane anaesthesia in 216 adult day surgery patients .

Example answer:
{"entities": [{"text": "postoperative nausea and vomiting and pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The observed effect of NIMO may have been attributable to the preservation of calcium homeostasis during hypotension , because there were no differences in the PbtO ( 2 ) indices among groups .

Example answer:
{"entities": [{"text": "NIMO", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , intraspinal injection of 5,7-DHT to produce a more selective lesion of only descending serotonin projections in the spinal cord did not affect this hypotension .

Example answer:
{"entities": [{"text": "5,7-DHT", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: BACKGROUND : Spinal anaesthesia is widely employed in clinical practice but has the main drawback of post-spinal block hypotension .

## Item biored:test:436
Example input:
Sentence: The finding of Mallory body-like inclusions in two cases of genetically documented SEPN-RM led us to suspect a relationship between MB-DRM and SEPN1 .

Example answer:
{"entities": [{"text": "SEPN-RM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SEPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the original MB-DRM German family , we demonstrated a linkage of the disease to the SEPN1 locus ( 1p36 ) , and subsequently a homozygous SEPN1 deletion ( del 92 nucleotide -19/+73 ) in the affected patients .

Example answer:
{"entities": [{"text": "SEPN1", "type": "GeneOrGeneProduct"}, {"text": "del 92 nucleotide -19/+73", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Novel CACNA1S mutation causes autosomal dominant hypokalemic periodic paralysis in a South American family .

Example answer:
{"entities": [{"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "hypokalemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report here a new family with X-linked mental retardation due to mutation in OPHN1 and present unpublished data about two families previously reported , concerning the facial and psychological phenotype of affected males and carrier females .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPHN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: With the advent of next-generation sequencing technologies , the homozygous mutations T71N and A190T in the neuronal calcium sensor ( NCS ) hippocalcin were identified as the genetic cause of primary isolated dystonia ( DYT2 dystonia ) .

Example answer:
{"entities": [{"text": "T71N", "type": "SequenceVariant"}, {"text": "A190T", "type": "SequenceVariant"}, {"text": "neuronal calcium sensor", "type": "GeneOrGeneProduct"}, {"text": "NCS", "type": "GeneOrGeneProduct"}, {"text": "hippocalcin", "type": "GeneOrGeneProduct"}, {"text": "primary isolated dystonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DYT2", "type": "GeneOrGeneProduct"}, {"text": "dystonia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations of MKS3/TMEM67 , found recently in Meckel-Gruber syndrome ( MKS ) type 3 and Joubert syndrome ( JBTS ) type 6 , are predominantly truncating mutations .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "Meckel-Gruber syndrome ( MKS ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Joubert syndrome ( JBTS ) type 6", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Previously , RAPSN mutations have been reported in congenital myasthenia .

## Item biored:test:363
Example input:
Sentence: She also had hypertension and premature pubarche , whereas dexamethasone effectively suppressed these clinical manifestations .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the periphery of the ischemic territory , SG in the cortex was greater ( less edema accumulation ) in the hypertensive group ( 1.041 +/- 0.001 vs 1.039 +/- 0.001 , P less than 0.05 ) .

Example answer:
{"entities": [{"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA polymorphisms at CYP11B2/B1 locus may confer susceptibility to postoperative hypertension of patients with APA .

Example answer:
{"entities": [{"text": "CYP11B2/B1", "type": "GeneOrGeneProduct"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : AA genotype of A 1166C polymorphism was associated with lower minimal systolic blood pressure ( SBP ) and diastolic blood pressure ( DBP ) during HUT compared with other genotypes ( minimal SBP : AA 59.6+/-21,8 , AC 79.9+/-22.7 , CC 65.4+/-22.7 mmHg , P=0.007 ) , ( minimal DBP : AA 36.4+/-22.7 , AC 52.3+/-22.9 , CC 45.4+/-19.5 mmHg , P=0.007 ) .AA genotype was also associated with higher SDNN compared to other genotypes in the early phase of HUT ( SDNN in 5 minutes of tilt : AA 59.7+/-24.6 , AC 50.6+/-20.6 , CC 46.0+/-13.2 , P=0.01 ) and at syncope occurrence ( SDNN : AA 71.0+/-20.9 , AC 58.2+/-17.9 , CC 58+/-10 , P=0.04 ) CONCLUSION : AA genotype of A 1166C polymorphism in the ATR1 gene may be associated with hypotension and decline in sympathetic tone during HUT .

Example answer:
{"entities": [{"text": "A 1166C", "type": "SequenceVariant"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conducted an association study assessing how PD risk in Italy was influenced by the serotonin transporter gene ( SLC6A4 ) polymorphic region 5-HTTLPR , consisting of an insertion/deletion ( long allele-L/short allele-S ) of 43 bp in the SLC6A4 promoter region .

Example answer:
{"entities": [{"text": "PD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "SLC6A4", "type": "GeneOrGeneProduct"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "insertion/deletion ( long allele-L/short allele-S ) of 43 bp", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : The rs4539 ( AA ) , H1 , H2 , and H3 are genetic predictors for postoperative persistence of hypertension for Chinese patients treated by adrenalectomy with APA .

Example answer:
{"entities": [{"text": "rs4539", "type": "SequenceVariant"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Multivariate logistic regression revealed the common haplotypes H1 ( AGACT ) , H2 ( AGAWT ) , and H3 ( AGAWC ) were associated with the persistent postoperative hypertension ( P = .01 , 0.03 , 0.005 after Bonferroni correction ) .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : CYP11B2-CYP11B1 haplotype was associated with persistent postoperative hypertension in Chinese patients undergoing adrenalectomy with APA ( P = .006 ) .

Example answer:
{"entities": [{"text": "CYP11B2-CYP11B1", "type": "GeneOrGeneProduct"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A potential regulatory single nucleotide polymorphism in the promoter of the Klotho gene may be associated with essential hypertension in the Chinese Han population .

Example answer:
{"entities": [{"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "essential hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: OBJECTIVES : Our objective was to investigate the relationship between 6bINS and the vascular complication pulmonary arterial hypertension ( PAH ) in SSc in a French Caucasian population .

## Item biored:test:400
Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Atorvastatin protects against contrast-induced nephropathy via anti-apoptosis by the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Finally , the IKr blockers , Terfenadine and Citalopram , which are reported to cause Torsade de Pointes ( TdP ) in clinical practice , produced early afterdepolarization ( EAD ) .

Example answer:
{"entities": [{"text": "Terfenadine", "type": "ChemicalEntity"}, {"text": "Citalopram", "type": "ChemicalEntity"}, {"text": "Torsade de Pointes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: AIMS : This study sought to assess the risk of developing coronary artery disease ( CAD ) associated with initial treatment of type 2 diabetes with different sulphonylureas .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sulphonylureas", "type": "ChemicalEntity"}]}

Example input:
Sentence: MATERIALS AND METHODS : Our study included patients who were administered 30-60 mL of iodinated contrast agent for percutaneous coronary angiography ( PCAG ) , all with creatinine values between 1.1 and 3.1 mg/dL .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "contrast", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Comparison of effects of isotonic sodium chloride with diltiazem in prevention of contrast-induced nephropathy .

Example answer:
{"entities": [{"text": "sodium chloride", "type": "ChemicalEntity"}, {"text": "diltiazem", "type": "ChemicalEntity"}, {"text": "contrast-induced", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among a total of 60 patients included in the study , 16 patients developed acute renal failure ( ARF ) on the second day after contrast material was injected ( 26.6 % ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "contrast", "type": "ChemicalEntity"}]}

Example input:
Sentence: Contrast-induced nephropathy ( CIN ) is an iatrogenic acute renal failure occurring following the intravascular injection of iodinated radiographic contrast medium .

Example answer:
{"entities": [{"text": "Contrast-induced nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: INTRODUCTION AND OBJECTIVE : Contrast-induced nephropathy ( CIN ) significantly increases the morbidity and mortality of patients .

Example answer:
{"entities": [{"text": "Contrast-induced", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: CONCLUSIONS : The rate of contrast-induced nephropathy , defined by multiple end points , is not statistically different after the intraarterial administration of iopamidol or iodixanol to high-risk patients , with or without diabetes mellitus .

## Item biored:test:416
Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Angiotensin II subtype 1a receptor signaling in resident hepatic macrophages induces liver metastasis formation .

Example answer:
{"entities": [{"text": "Angiotensin II subtype 1a receptor", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Interestingly , DCs that were co-treated with cisplatin and lipopolysaccharide ( LPS ) exhibited a decreased immunostimulatory capacity for inducing the proliferation of Th1- and Th17-type T cells ; instead , these DCs contributed to Th2-type T cell immunity .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "lipopolysaccharide", "type": "ChemicalEntity"}, {"text": "LPS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cisplatin-treated DCs down-regulated the expression of cell surface molecules ( CD80 , CD86 , MHC class I and II ) and up-regulated endocytic capacity in a dose-dependent manner .

Example answer:
{"entities": [{"text": "Cisplatin-treated", "type": "ChemicalEntity"}, {"text": "CD80", "type": "GeneOrGeneProduct"}, {"text": "CD86", "type": "GeneOrGeneProduct"}, {"text": "MHC class I and II", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , the abundance and proliferative index of lymph node , thymus and CNS CD4 ( + ) CD25 ( + ) FoxP3 ( + ) Tregs were strikingly reduced in VPAC2-deficient mice with EAE .

Example answer:
{"entities": [{"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "FoxP3", "type": "GeneOrGeneProduct"}, {"text": "VPAC2-deficient", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , AT2R gene and protein expressions in fetal kidneys were inhibited by PCE , associated with the repression of the gene expression of glial-cell-line-derived neurotrophic factor ( GDNF ) /tyrosine kinase receptor ( c-Ret ) signaling pathway .

Example answer:
{"entities": [{"text": "AT2R", "type": "GeneOrGeneProduct"}, {"text": "glial-cell-line-derived neurotrophic factor", "type": "GeneOrGeneProduct"}, {"text": "GDNF", "type": "GeneOrGeneProduct"}, {"text": "kinase receptor", "type": "GeneOrGeneProduct"}, {"text": "c-Ret", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: This data suggests that E2 modifies the expression of CD36 at the level of protein expression in monocyte-derived macrophages resulting in reduced cholesteryl ester accumulation following ritonavir treatment .

## Item biored:test:461
Example input:
Sentence: After verifying the epidural space , bupivacaine and triamcinolone diacetate were injected .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "triamcinolone diacetate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Post hoc analyses indicated that efficacy was similar with asenapine and haloperidol ; greater contrasts were seen in AEs , especially extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "extrapyramidal symptoms", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rise in blood pressure became less marked when higher concentrations of sevoflurane or enflurane were administered and the blood pressure at convulsions decreased significantly in 1.6 % sevoflurane , and in 0.8 % and 1.6 % enflurane .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "enflurane", "type": "ChemicalEntity"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The findings of this study suggest that lesions of the unilateral STN and GPi are equally effective treatment for patients with advanced PD refractory to medical treatment .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Under isoflurane anesthesia , the MCA of 14 spontaneously hypertensive rats was occluded .

Example answer:
{"entities": [{"text": "isoflurane", "type": "ChemicalEntity"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cauda equina syndrome is a rare complication of epidural anesthesia .

Example answer:
{"entities": [{"text": "Cauda equina syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It is suggested that sevoflurane reduces the convulsive effect of lidocaine toxicity but carries some risk due to circulatory depression .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSION : Compared to conventional spinal anaesthesia , unilateral spinal anaesthesia was associated with fewer cardiovascular perturbations .

## Item biored:test:489
Example input:
Sentence: Rates of response and BP control were significantly higher in the groups that received combination treatment compared with those that received monotherapy .

Example answer:
{"entities": []}

Example input:
Sentence: In this study , we performed a two-stage case-control association study for irinotecan-induced severe myelosuppression ( grades 3 and 4 ) .

Example answer:
{"entities": [{"text": "irinotecan-induced", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : A case-control study was carried out in Chinese Han population , including 368 cases of migraine and 517 controls .

Example answer:
{"entities": [{"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Limited prospective data corroborate these findings , but larger prospective studies are urgently required .

Example answer:
{"entities": []}

Example input:
Sentence: ( CCTTT ) 14 , which has been reported to have a higher activity in a reporter-construct , was significantly more abundant in POAG patients , while ( CCTTT ) 10 and ( CCTTT ) 13 were less common .

Example answer:
{"entities": [{"text": "( CCTTT ) 14", "type": "SequenceVariant"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "( CCTTT ) 10", "type": "SequenceVariant"}, {"text": "( CCTTT ) 13", "type": "SequenceVariant"}]}

Example input:
Sentence: In addition , we studied 89 cases and 50 controls from Ohio to replicate any positive findings .

Example answer:
{"entities": []}

Example input:
Sentence: We therefore conducted a case-control study with 515 incident lung cancer cases and 1030 age- and sex-matched controls without cancer , and further conducted a meta-analysis .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A case-control study was conducted on incident gastric adenocarcinoma patients ( n=271 ) and age-gender frequency-matched control subjects ( n=271 ) .

Example answer:
{"entities": [{"text": "gastric adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Further validation by population-based case-control studies and rigorous mechanistic studies is warranted .

Example answer:
{"entities": []}

Input:
Sentence: Larger confirmatory case-control studies are warranted .

## Item biored:test:329
Example input:
Sentence: PURPOSE : Aniridia ( AN ) is a rare congenital panocular disorder caused by the mutations of the paired box homeotic gene 6 ( PAX6 ) gene .

Example answer:
{"entities": [{"text": "Aniridia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "congenital panocular disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paired box homeotic gene 6", "type": "GeneOrGeneProduct"}, {"text": "PAX6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: We report here a new family with X-linked mental retardation due to mutation in OPHN1 and present unpublished data about two families previously reported , concerning the facial and psychological phenotype of affected males and carrier females .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPHN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: NPHP can be associated with retinal degeneration ( Senior-Loken syndrome ) , brainstem and cerebellar anomalies ( Joubert syndrome ) , or liver fibrosis .

Example answer:
{"entities": [{"text": "NPHP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "retinal degeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Senior-Loken syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebellar anomalies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Joubert syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Our data suggest that in a model representative of human retinopathy of prematurity , NOX4 was increased at a time point when IVNV developed .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "retinopathy of prematurity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Endothelial NADPH oxidase 4 mediates vascular endothelial growth factor receptor 2-induced intravitreal neovascularization in a rat model of retinopathy of prematurity .

Example answer:
{"entities": [{"text": "NADPH oxidase 4", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor receptor", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "retinopathy of prematurity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Identification of this new de novo nonsense mutation confirms the diagnosis of FDH in this child and highlights the clinical importance of PORCN and Wnt signalling pathways in embryogenesis .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PORCN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cone dystrophy with supernormal rod response is strictly associated with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "Cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : The phenotype of cone dystrophy with supernormal rod response is tightly linked with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: BACKGROUND : To examine the contribution of mutations within the Norrie disease ( NDP ) gene to the clinically similar retinal diseases Norrie disease , X-linked familial exudative vitreoretinopathy ( FEVR ) , Coat 's disease and retinopathy of prematurity ( ROP ) .

## Item biored:test:333
Example input:
Sentence: CONCLUSION : Identification of this new de novo nonsense mutation confirms the diagnosis of FDH in this child and highlights the clinical importance of PORCN and Wnt signalling pathways in embryogenesis .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PORCN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Eleven subjects presented SRD5A2 homozygous single-base mutations ( two first cousins and four unrelated patients with G183S , two with R246W , one with del642T , one with G196S , and one with 217_218insC plus the A49T variant in heterozygosis ) , whereas four were compound heterozygotes ( one with Q126R/IVS3+1G > A , one with Q126R/del418T , and two brothers with Q126R/G158R ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "G183S", "type": "SequenceVariant"}, {"text": "R246W", "type": "SequenceVariant"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}, {"text": "A49T", "type": "SequenceVariant"}, {"text": "Q126R/IVS3+1G > A", "type": "SequenceVariant"}, {"text": "Q126R/del418T", "type": "SequenceVariant"}, {"text": "Q126R/G158R", "type": "SequenceVariant"}]}

Example input:
Sentence: In LCD , three novel heterozygous mutations found were glycine-594-valine ( Gly594Val ) in 2 of 18 patients , valine-539-aspartic acid ( Val539Asp ) in 1 patient , and deletion of valine 624 , valine 625 ( Val624-Val625del ) in 1 patient .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glycine-594-valine", "type": "SequenceVariant"}, {"text": "Gly594Val", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "valine-539-aspartic acid", "type": "SequenceVariant"}, {"text": "Val539Asp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion of valine 624 , valine 625", "type": "SequenceVariant"}, {"text": "Val624-Val625del", "type": "SequenceVariant"}]}

Example input:
Sentence: Seven novel single-nucleotide polymorphisms ( SNPs ) were also found , of which a change of leucine 269 to phenylalanine ( Leu269Phe ) was found in 12 of 18 patients with the Arg555Trp mutation .

Example answer:
{"entities": [{"text": "leucine 269 to phenylalanine", "type": "SequenceVariant"}, {"text": "Leu269Phe", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Arg555Trp", "type": "SequenceVariant"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In GCD , 18 patients with GCD type I had a mutation of arginine 555-to-tryptophan ( Arg555Trp ) and 1 patient with GCD type III ( Reis-Bucklers dystrophy ) , had the Arg124Leu mutation .

Example answer:
{"entities": [{"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "GCD type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 555-to-tryptophan", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "GCD type III", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Reis-Bucklers dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Arg124Leu", "type": "SequenceVariant"}]}

Example input:
Sentence: RT-PCR analysis , performed on a patient homozygous for the intronic deletion ( c.609+28_610-16del ) , failed to detect any GNPTG RNA transcripts .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "GNPTG", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We next sequenced PTPN11 in DNA samples from 54 patients with the multiple enchondromatosis disorders Ollier disease or Maffucci syndrome , but found no coding sequence PTPN11 mutations .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "enchondromatosis disorders Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a study of 10 patients from seven families with a clinical phenotype and enzymatic diagnosis of MLIII , six novel GNPTG gene mutations were identified .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "MLIII", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GNPTG", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Input:
Sentence: RESULTS : Evidence for two novel mutations in the NDP gene was presented : Leu103Val in one FEVR patient and His43Arg in monozygotic twin Norrie disease patients .

## Item biored:test:412
Example input:
Sentence: CONCLUSIONS : Our data suggest that in a model representative of human retinopathy of prematurity , NOX4 was increased at a time point when IVNV developed .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "retinopathy of prematurity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Earlier studies revealed the major role of Extracellular signal-regulated kinase ( ERK ) pathways in low-density lipoprotein receptor ( LDLr ) expression .

Example answer:
{"entities": [{"text": "Extracellular signal-regulated kinase", "type": "GeneOrGeneProduct"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "LDLr", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The selective 5-HT6 receptor antagonist Ro4368554 restores memory performance in cholinergic and serotonergic models of memory deficiency in the rat .

Example answer:
{"entities": [{"text": "5-HT6 receptor", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "serotonergic", "type": "ChemicalEntity"}, {"text": "memory deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: We therefore systematically analyzed the functional impact of the most prevalent immune escape variants , the sG145R and sP120T mutants , on the viral replication efficacy and antiviral drug susceptibility of common treatment-associated mutants with resistance to lamivudine ( LAM ) and/or HBeAg negativity .

Example answer:
{"entities": [{"text": "lamivudine", "type": "ChemicalEntity"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg", "type": "ChemicalEntity"}]}

Example input:
Sentence: The loss of Lifr results in both the failure for STAT3 to translocate to the LE nuclei and a reduction in the expression of the LIF regulated gene Msx1 that regulates uterine receptivity .

Example answer:
{"entities": [{"text": "Lifr", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "Msx1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A common missense variant in the gene encoding a component of the sulfonylurea receptor ( ABCC8 p.A1369S ) promotes closure of the target channel of sulfonylurea therapy and is associated with increased insulin secretion , thus mimicking the effects of sulfonylurea therapy .

Example answer:
{"entities": [{"text": "sulfonylurea receptor", "type": "GeneOrGeneProduct"}, {"text": "ABCC8", "type": "GeneOrGeneProduct"}, {"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "sulfonylurea", "type": "ChemicalEntity"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Rab6c was found to be under-expressed in MCF7/AdrR and MES-SA/Dx5 ( a human MDR uterine sarcoma cell line ) compared with their non-MDR parental cell lines .

Example answer:
{"entities": [{"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "MES-SA/Dx5", "type": "CellLine"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "uterine sarcoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Targeting IDO itself or the p38 MAPK signaling pathway could provide a novel therapy for comorbid depressive disorders in HIV-1-infected patients .

Example answer:
{"entities": [{"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "p38 MAPK", "type": "GeneOrGeneProduct"}, {"text": "depressive disorders", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HIV-1-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Input:
Sentence: Ritonavir increased the expression of the scavenger receptor , CD36 mRNA , responsible for the uptake of LDL .

## Item biored:test:372
Example input:
Sentence: Initial brain magnetic resonance imaging ( MRI ) were obtained after the hospitalization , including DWI ( 8/8 ) , apparent diffusion coefficient ( ADC ) map ( 4/8 ) , FLAIR ( 7/8 ) , and T2-weighted image ( 8/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Three time domain indexes of hemodynamic variability were employed : the standard deviation of mean arterial pressure as a measure of blood pressure variability and the standard deviation of beat-to-beat intervals ( SDRR ) and the root mean square of successive differences in R-wave-to-R-wave intervals as measures of heart rate variability .

Example answer:
{"entities": []}

Example input:
Sentence: Histological analyses of apoptosis , proliferation , angiogenesis and infarct zone assessments were performed using terminal deoxynucleotidyltransferase-mediated dUTP nick-end labelling ( TUNEL ) staining , BrdU immunostaining , a-smooth muscle actin ( a-SMA ) /CD31 immunostaining and Masson 's trichrome staining , respectively .

Example answer:
{"entities": [{"text": "infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "terminal", "type": "GeneOrGeneProduct"}, {"text": "dUTP", "type": "ChemicalEntity"}, {"text": "a-smooth muscle actin", "type": "GeneOrGeneProduct"}, {"text": "a-SMA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The clinical application of doxorubicin ( Dox ) is limited by its adverse effect of cardiotoxicity .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "Dox", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The protective role of mangiferin was analyzed by triphenyl tetrazolium chloride ( TTC ) test used for macroscopic enzyme mapping assay of the ischemic myocardium .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "triphenyl tetrazolium chloride", "type": "ChemicalEntity"}, {"text": "TTC", "type": "ChemicalEntity"}, {"text": "ischemic myocardium", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Hemodynamic parameters and lead II electrocardiograph were monitored and recorded continuously .

Example answer:
{"entities": []}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Field potential duration ( FPD ) in human-induced pluripotent stem cell-derived cardiomyocytes ( hiPS-CMs ) , which can express QT interval in an electrocardiogram , is reported to be a useful tool to predict K ( + ) channel and Ca ( 2+ ) channel blocker effects on QT interval .

Example answer:
{"entities": [{"text": "human-induced", "type": "OrganismTaxon"}, {"text": "K ( + ) channel and Ca ( 2+ ) channel blocker", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol alone decreased left ventricular systolic pressure and myocardial contractility indexed as LVdp/dtmax and LVdp/dtmin .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

## Item biored:test:447
Example input:
Sentence: A common missense variant in the gene encoding a component of the sulfonylurea receptor ( ABCC8 p.A1369S ) promotes closure of the target channel of sulfonylurea therapy and is associated with increased insulin secretion , thus mimicking the effects of sulfonylurea therapy .

Example answer:
{"entities": [{"text": "sulfonylurea receptor", "type": "GeneOrGeneProduct"}, {"text": "ABCC8", "type": "GeneOrGeneProduct"}, {"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "sulfonylurea", "type": "ChemicalEntity"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Several studies have reported that , compared with wild-type individuals , CYP2C19 variant allele carriers exhibit a significantly lower capacity to metabolize clopidogrel into its active metabolite and inhibit platelet activation , and are therefore at significantly higher risk of adverse cardiovascular events .

Example answer:
{"entities": [{"text": "CYP2C19", "type": "GeneOrGeneProduct"}, {"text": "clopidogrel", "type": "ChemicalEntity"}]}

Example input:
Sentence: Single nucleotide polymorphism in ABCG2 is associated with irinotecan-induced severe myelosuppression .

Example answer:
{"entities": [{"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "irinotecan-induced", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although only limited subjects were investigated , our results suggested that a genetic polymorphism in ABCG2 might alter the transport activity for the drug and elevate the systemic circulation level of irinotecan , leading to severe myelosuppression .

Example answer:
{"entities": [{"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "irinotecan", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Microfluorimetry and patch-clamp experiments were performed on TRPV6-expressing HEK cells to determine whether this Ca ( 2+ ) -sensing Ca ( 2+ ) channel is constitutively active .

Example answer:
{"entities": [{"text": "TRPV6-expressing", "type": "GeneOrGeneProduct"}, {"text": "HEK", "type": "CellLine"}, {"text": "Ca ( 2+ )", "type": "ChemicalEntity"}]}

Example input:
Sentence: In summary , no constitutive open TRPV6 channels were detected in patch-clamp experiments from transfected HEK cells .

Example answer:
{"entities": [{"text": "TRPV6", "type": "GeneOrGeneProduct"}, {"text": "HEK", "type": "CellLine"}]}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PBMCs from homozygotes and wild-type controls were stimulated with anti-CD3/anti-CD28 antibodies and the level of T-cell activation was determined by the stimulation index .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : PBMCs with the heterozygous and homozygous SLURP-1 G86R mutation had defective T-cell activation .

Example answer:
{"entities": [{"text": "SLURP-1", "type": "GeneOrGeneProduct"}, {"text": "G86R", "type": "SequenceVariant"}]}

Input:
Sentence: Patch-clamping of PBMCs from the p.F482C homozygous and heterozygous subjects revealed lower polycystin-2 channel function than in controls .
