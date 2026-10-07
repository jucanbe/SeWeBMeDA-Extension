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

## Item biored:test:1087
Example input:
Sentence: Proinflammatory cytokine gene polymorphisms have been demonstrated to associate with gastric cancer risk , of which IL1B-31T/C and -511C/T changes have been well investigated due to the possibility that they may alter the IL1B transcription .

Example answer:
{"entities": [{"text": "Proinflammatory cytokine", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IL1B-31T/C", "type": "GeneOrGeneProduct"}, {"text": "-511C/T", "type": "SequenceVariant"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: STUDY DESIGN : Wild-type ( WT ) and superoxide dismutase 1 ( SOD1 ) -overexpressing day 8.75 embryos from nondiabetic WT control with SOD1 transgenic male and diabetic WT female with SOD1 transgenic male were analyzed for ER stress markers : C/EBP-homologous protein ( CHOP ) , calnexin , eukaryotic initiation factor 2a ( eIF2a ) , protein kinase ribonucleic acid ( RNA ) -like ER kinase ( PERK ) , binding immunoglobulin protein , protein disulfide isomerase family A member 3 , kinases inositol-requiring protein-1a ( IRE1a ) , and the X-box binding protein ( XBP1 ) messenger RNA ( mRNA ) splicing .

Example answer:
{"entities": [{"text": "superoxide dismutase 1", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "C/EBP-homologous protein", "type": "GeneOrGeneProduct"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "eukaryotic initiation factor 2a", "type": "GeneOrGeneProduct"}, {"text": "eIF2a", "type": "GeneOrGeneProduct"}, {"text": "protein kinase ribonucleic acid ( RNA ) -like ER kinase", "type": "GeneOrGeneProduct"}, {"text": "PERK", "type": "GeneOrGeneProduct"}, {"text": "binding immunoglobulin protein", "type": "GeneOrGeneProduct"}, {"text": "protein disulfide isomerase family A member 3", "type": "GeneOrGeneProduct"}, {"text": "kinases inositol-requiring protein-1a", "type": "GeneOrGeneProduct"}, {"text": "IRE1a", "type": "GeneOrGeneProduct"}, {"text": "X-box binding protein", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using individual-level data from 120,286 participants in the UK Biobank and summary association results from four large-scale genome-wide association studies , we examined the impact of this variant on cardiometabolic traits , type 2 diabetes , and coronary heart disease .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: These results suggest that TNMD polymorphisms are associated with adiposity and also with glucose metabolism and conversion from IGT to T2D in men .

Example answer:
{"entities": [{"text": "TNMD", "type": "GeneOrGeneProduct"}, {"text": "adiposity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: Measured genotype analysis tested associations between SNPs and obesity and diabetes-related traits .

Example answer:
{"entities": [{"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes-related", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Maternal diabetes significantly increased the levels of CHOP , calnexin , phosphorylated ( p ) -eIF2a , p-PERK , and p-IRE1a ; triggered XBP1 mRNA splicing ; and enhanced ER chaperone gene expression in WT embryos .

Example answer:
{"entities": [{"text": "Maternal diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The aim of this study was to investigate the associations of IL-65-72C/G and TNF-alpha -857C/T SNPs , and inflammation and metabolic biomarkers in women with GDM pregnancies .

## Item biored:test:1092
Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: AIMS : Individuals with both diabetes mellitus ( DM ) and the Haptoglobin ( Hp ) 2-2 genotype are at increased risk of cardiovascular disease .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Haptoglobin", "type": "GeneOrGeneProduct"}, {"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "cardiovascular disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our results thus indicates that PON1 192RR homozygosity is associated with increased mortality in women in the second half of life and that this increased mortality is possibly related to CHD severity and survival after CHD rather than susceptibility to development of CHD .

Example answer:
{"entities": [{"text": "PON1", "type": "GeneOrGeneProduct"}, {"text": "192RR", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The fetal measures for women who quit after learning of their pregnancies were compared with measures for women who continued some drinking throughout the course of their pregnancies .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Furthermore the GG distribution within cases was even greater in younger men ( < 65 years ; 42 % ; P = 0.012 ) .

Example answer:
{"entities": [{"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: She had profound insulin resistance , diabetes , severe hypertriglyceridemia and relapsing pancreatitis , while her pre-pubescent daughter had normal fat distribution but elevated plasma triglycerides and C-peptide and depressed high-density lipoprotein cholesterol .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertriglyceridemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pancreatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "triglycerides", "type": "ChemicalEntity"}, {"text": "C-peptide", "type": "ChemicalEntity"}, {"text": "high-density lipoprotein cholesterol", "type": "ChemicalEntity"}]}

Example input:
Sentence: When women reportedly quit drinking early in their pregnancies , fetal growth measures were not significantly different from a non-alcohol-exposed group , regardless of prior drinking patterns .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Advanced maternal age , a recognized risk factor for CPO , was also associated with the only identified geographic cluster for CPO .

Example answer:
{"entities": [{"text": "CPO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Women with both a DHFR deletion allele and low folate intake ( < 400 microg/d from diet plus supplements ) had a significantly greater risk of preterm delivery ( AOR : 5.5 ; 95 % CI : 1.5 , 20.4 ; P = 0.01 ) and a significantly greater risk of having an infant with a low birth weight ( AOR : 8.3 ; 95 % CI : 1.8 , 38.6 ; P = 0.01 ) than did women without a deletion allele and with a folate intake > /=400 microg/d .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "DHFR", "type": "GeneOrGeneProduct"}, {"text": "folate", "type": "ChemicalEntity"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Women with a deletion allele had a significantly greater risk of preterm delivery [ adjusted odds ratio ( AOR ) : 3.0 ; 95 % CI : 1.0 , 8.8 ; P < 0.05 ] than did those without a deletion allele .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Women with GDM were of older maternal age , had higher BMI , were more nulliparous , and had T2DM and GDM history , compared to women with healthy pregnancies ( p < 0.05 ) .

## Item biored:test:998
Example input:
Sentence: When examining a worldwide cohort of 62 independent patients with NPHP and associated liver fibrosis we identified altogether four novel mutations ( p.W290L , p.C615R , p.G821S , and p.G821R ) in five of them .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NPHP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.W290L", "type": "SequenceVariant"}, {"text": "p.C615R", "type": "SequenceVariant"}, {"text": "p.G821S", "type": "SequenceVariant"}, {"text": "p.G821R", "type": "SequenceVariant"}]}

Example input:
Sentence: No association was found between PAI-1 serum levels or 4G/5G genotype with liver fibrosis in obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : Hypomorphic MKS3/TMEM67 mutations cause NPHP with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "NPHP with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Plasminogen activator inhibitor type 1 serum levels and 4G/5G gene polymorphism in morbidly obese Hispanic patients with non-alcoholic fatty liver disease .

Example answer:
{"entities": [{"text": "Plasminogen activator inhibitor type 1", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Nonketotic hyperglycinemia is a disorder of amino acid metabolism in which a defect in the glycine cleavage system leads to an accumulation of glycine in the brain and other body compartments .

Example answer:
{"entities": [{"text": "Nonketotic hyperglycinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "disorder of amino acid metabolism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glycine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Among NASH patients , body mass index was significantly lower ( p < 0.05 ) , and non-obese patients were significantly more frequent ( p < 0.001 ) in carriers of Val175Met variant than in homozygotes of wild type PEMT .

Example answer:
{"entities": [{"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Val175Met", "type": "SequenceVariant"}, {"text": "PEMT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PAI-1 4G/5G promoter genotypes frequencies were similar in patients with or without liver fibrosis associated to NASH ( p = 0.6 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: His liver was cirrhotic with parenchymal iron deposits and the result of a glucose tolerance test was compatible with diabetes mellitus .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "iron", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: BACKGROUND/AIMS : The genetic predisposition on the development of nonalcoholic steatohepatitis ( NASH ) has been poorly understood .

Example answer:
{"entities": [{"text": "nonalcoholic steatohepatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Nonalcoholic fatty liver disease ( NAFLD ) defines a spectrum of conditions from simple steatosis to nonalcoholic steatohepatitis ( NASH ) and cirrhosis and is regarded as the hepatic manifestation of the metabolic syndrome .

## Item biored:test:1089
Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Molecular dynamic simulations of structural changes induced by L1503R indicated that the mean value of all-atom root-mean-squared-deviation was shifted from those with wild type or another mutation L1503Q that has been reported to be a group II mutation , which is susceptible to ADAMTS13 proteolysis .

Example answer:
{"entities": [{"text": "L1503R", "type": "SequenceVariant"}, {"text": "L1503Q", "type": "SequenceVariant"}, {"text": "ADAMTS13", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Histological analyses of apoptosis , proliferation , angiogenesis and infarct zone assessments were performed using terminal deoxynucleotidyltransferase-mediated dUTP nick-end labelling ( TUNEL ) staining , BrdU immunostaining , a-smooth muscle actin ( a-SMA ) /CD31 immunostaining and Masson 's trichrome staining , respectively .

Example answer:
{"entities": [{"text": "infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "terminal", "type": "GeneOrGeneProduct"}, {"text": "dUTP", "type": "ChemicalEntity"}, {"text": "a-smooth muscle actin", "type": "GeneOrGeneProduct"}, {"text": "a-SMA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To determine whether c.609+28_610-16del allele-derived transcripts were subject to nonsense-mediated mRNA decay ( NMD ) , patient fibroblasts were incubated with the protein synthesis inhibitor anisomycin .

Example answer:
{"entities": [{"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "anisomycin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Inhibition of PRMT5 by EPZ015666 and siRNA-mediated knockdown reduced IL-6 and IL-8 production , and proliferation of RA FLSs .

Example answer:
{"entities": [{"text": "PRMT5", "type": "GeneOrGeneProduct"}, {"text": "EPZ015666", "type": "ChemicalEntity"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We also found an interaction between the presence of DBH -1021T and the -889TT genotype ( rs1800587 ) of IL1A : synergy factor = 1.9 ( 1.2-3.1 , 0.005 ) .

Example answer:
{"entities": [{"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "-1021T", "type": "SequenceVariant"}, {"text": "-889TT", "type": "SequenceVariant"}, {"text": "rs1800587", "type": "SequenceVariant"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: STUDY DESIGN : Wild-type ( WT ) and superoxide dismutase 1 ( SOD1 ) -overexpressing day 8.75 embryos from nondiabetic WT control with SOD1 transgenic male and diabetic WT female with SOD1 transgenic male were analyzed for ER stress markers : C/EBP-homologous protein ( CHOP ) , calnexin , eukaryotic initiation factor 2a ( eIF2a ) , protein kinase ribonucleic acid ( RNA ) -like ER kinase ( PERK ) , binding immunoglobulin protein , protein disulfide isomerase family A member 3 , kinases inositol-requiring protein-1a ( IRE1a ) , and the X-box binding protein ( XBP1 ) messenger RNA ( mRNA ) splicing .

Example answer:
{"entities": [{"text": "superoxide dismutase 1", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "C/EBP-homologous protein", "type": "GeneOrGeneProduct"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "eukaryotic initiation factor 2a", "type": "GeneOrGeneProduct"}, {"text": "eIF2a", "type": "GeneOrGeneProduct"}, {"text": "protein kinase ribonucleic acid ( RNA ) -like ER kinase", "type": "GeneOrGeneProduct"}, {"text": "PERK", "type": "GeneOrGeneProduct"}, {"text": "binding immunoglobulin protein", "type": "GeneOrGeneProduct"}, {"text": "protein disulfide isomerase family A member 3", "type": "GeneOrGeneProduct"}, {"text": "kinases inositol-requiring protein-1a", "type": "GeneOrGeneProduct"}, {"text": "IRE1a", "type": "GeneOrGeneProduct"}, {"text": "X-box binding protein", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: For this purpose we developed a high-throughput methodology to genotype both normal and deleted alleles using a chip-based matrix-assisted laser desorption-time-of-flight ( MALDI-TOF ) mass spectrometer and Multiplex PCR .

Example answer:
{"entities": []}

Input:
Sentence: Matrix-assisted laser desorption ionization time of flight mass spectrometry ( MALDI-TOF-MS ) and MassARRAY-IPLEX were performed to analyze IL-65-72C/G and TNF-alpha -857C/T SNPs .

## Item biored:test:1020
Example input:
Sentence: The ability of oral Leu to increase protein synthesis and mTOR kinase after 1 h was largely prevented in sepsis .

Example answer:
{"entities": [{"text": "Leu", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Also , BCNU administration increased serum tumor necrosis factor-alpha ( TNFalpha ) , hippocampal MT and malondialdehyde ( MDA ) contents as well as caspase-3 activity in addition to histological alterations .

Example answer:
{"entities": [{"text": "BCNU", "type": "ChemicalEntity"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Chronic inflammation enhances gankyrin expression in the human liver .

Example answer:
{"entities": [{"text": "Chronic inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gankyrin", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Given VIP 's role as an anti-inflammatory mediator , we hypothesized that VIP ( -/- ) mice would exhibit enhanced inflammatory mediator expression after cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: The data suggest that in VIP ( -/- ) mice with bladder inflammation , inflammatory mediators are increased above that observed in WT with CYP .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Flow cytometry analysis found TIPE2 overexpression promoted apoptosis of H446 .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "H446", "type": "CellLine"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Inhibition of caspases , RIP1 , or RIP3 blocks radiation/TNFa-induced cell death , whereas inhibition of RIP1 blocks TNFa-induced caspase activation , suggesting that caspases and RIP1 act sequentially to mediate the non-compensatory cell death pathways .

Example answer:
{"entities": [{"text": "caspases", "type": "GeneOrGeneProduct"}, {"text": "RIP1", "type": "GeneOrGeneProduct"}, {"text": "RIP3", "type": "GeneOrGeneProduct"}, {"text": "TNFa-induced", "type": "GeneOrGeneProduct"}, {"text": "caspase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Although alcohol increased TNF-alpha , IL-6 , and IL-1beta mRNA , no change in key components of the NLRP3 inflammasome ( NLRP3 , ACS , and cleaved caspase-1 ) was detected suggesting alcohol did not increase pyroptosis .

## Item biored:test:1086
Example input:
Sentence: Using individual-level data from 120,286 participants in the UK Biobank and summary association results from four large-scale genome-wide association studies , we examined the impact of this variant on cardiometabolic traits , type 2 diabetes , and coronary heart disease .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: There are differential effects of age , gender and smoking status on the association of the G-395A polymorphism with EH ; the G-395A polymorphism is significantly associated with EH in subjects over 60years old , in females and in nonsmokers .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In agreement with the expectation that this mutation alters the LYAR binding activity , we found that the Ag ( +25 G- > A ) and Gg-globin-XmnI polymorphisms are associated with high HbF in erythroid precursor cells isolated from b ( 0 ) 39/b ( 0 ) 39 thalassemia patients .

Example answer:
{"entities": [{"text": "LYAR", "type": "GeneOrGeneProduct"}, {"text": "Ag", "type": "GeneOrGeneProduct"}, {"text": "+25 G- > A", "type": "SequenceVariant"}, {"text": "Gg-globin-XmnI", "type": "GeneOrGeneProduct"}, {"text": "HbF", "type": "GeneOrGeneProduct"}, {"text": "b ( 0 ) 39/b ( 0 ) 39 thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Our results showed substantial evidence of association between -1607 promoter polymorphism of MMP1 and DDD in the Southern Chinese subjects .

Example answer:
{"entities": [{"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , the meta-analysis of Taiwanese Han Chinese , Brazilian , and Polish populations showed that the Gln/Gln or Gln/Arg genotype and Gln allele were associated with SLE incidence .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results suggest that TNMD polymorphisms are associated with adiposity and also with glucose metabolism and conversion from IGT to T2D in men .

Example answer:
{"entities": [{"text": "TNMD", "type": "GeneOrGeneProduct"}, {"text": "adiposity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Input:
Sentence: However , few studies have focused on the association of IL-65-72C/G and TNF-alpha -857C/T single nucleotide polymorphisms ( SNPs ) , inflammatory biomarkers , and metabolic indexes in women with GDM , especially in the Inner Mongolia population .

## Item biored:test:1091
Example input:
Sentence: A significant correlation was found between baseline TAFI antigen concentrations and the duration of amenorrhea ( P < 0.05 ; r = 0.33 ) .

Example answer:
{"entities": [{"text": "TAFI", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : In a pooled analysis of 1460 ICH and 3817 IS/TIA , MB were more frequent in ICH vs IS/TIA in all treatment groups , but the excess increased from 2.8 ( odds ratio ; range , 2.3-3.5 ) in nonantithrombotic users to 5.7 ( range , 3.4-9.7 ) in antiplatelet users and 8.0 ( range , 3.5-17.8 ) in warfarin users ( P difference=0.01 ) .

Example answer:
{"entities": [{"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Significantly lower frequency of the A-C-C-G with higher frequency of A-C-A-G haplotypes was also noticed in subjects with DS ( P value =0.02089 and 0.00588 respectively ) .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , the main outcome measure was the sequencing of genomic DNA from peripheral blood samples of 41 women with POF and 36 fertile women ( controls ) .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: ( CCTTT ) 14 , which has been reported to have a higher activity in a reporter-construct , was significantly more abundant in POAG patients , while ( CCTTT ) 10 and ( CCTTT ) 13 were less common .

Example answer:
{"entities": [{"text": "( CCTTT ) 14", "type": "SequenceVariant"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "( CCTTT ) 10", "type": "SequenceVariant"}, {"text": "( CCTTT ) 13", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Significant differences were detected in genotypic distribution ( p = 0.04 ) as well as the allelic frequency ( p = 0.003 ) between the SHCM patients and controls .

Example answer:
{"entities": [{"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Though FAS-670 polymorphisms did not show any significant difference , the proportion of subjects with IL1B-31TT ( or IL1B-511CC ) increased according to stage ( trend P=0.019 ) .

Example answer:
{"entities": [{"text": "FAS-670", "type": "GeneOrGeneProduct"}, {"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Women with both a DHFR deletion allele and low folate intake ( < 400 microg/d from diet plus supplements ) had a significantly greater risk of preterm delivery ( AOR : 5.5 ; 95 % CI : 1.5 , 20.4 ; P = 0.01 ) and a significantly greater risk of having an infant with a low birth weight ( AOR : 8.3 ; 95 % CI : 1.8 , 38.6 ; P = 0.01 ) than did women without a deletion allele and with a folate intake > /=400 microg/d .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "DHFR", "type": "GeneOrGeneProduct"}, {"text": "folate", "type": "ChemicalEntity"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Women with a deletion allele had a significantly greater risk of preterm delivery [ adjusted odds ratio ( AOR ) : 3.0 ; 95 % CI : 1.0 , 8.8 ; P < 0.05 ] than did those without a deletion allele .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: RESULTS Distribution frequency of TNF-alpha -857CT ( OR=3.316 , 95 % CI=1.092-8.304 , p=0.025 ) in women with GDM pregnancies were obviously higher than that in women with healthy pregnancies .

## Item biored:test:1070
Example input:
Sentence: Here we investigated the role of Sag/Rbx2 E3 ligase in cellular senescence and immortalization of mouse embryonic fibroblasts ( MEFs ) and report that Sag is required for proper cell proliferation and Kras ( G12D ) -induced immortalization .

Example answer:
{"entities": [{"text": "Sag/Rbx2", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The growth of breast cancer xenografts in NOD/SCID mice was also inhibited by the doxycycline-induced Star-PAP overexpression .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "doxycycline-induced", "type": "ChemicalEntity"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Tumors implanted in LKB1 ( endo-/- ) mice but not macrophage-specific LKB1-knockout mice grew faster and showed enhanced vascular permeability and increased angiogenesis as compared with those implanted in wild-type mice .

Example answer:
{"entities": [{"text": "Tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "LKB1-knockout", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The expression of MLPH in primary prostate tumors was significantly lower in those with the G compared with the T allele and correlated significantly with AR protein .

Example answer:
{"entities": [{"text": "MLPH", "type": "GeneOrGeneProduct"}, {"text": "prostate tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Interestingly , the differential expression of miRNA in mice also corroborated with the miRNA expression in human PC cell lines and tissue samples ; ectopic expression of Let-7b in CD18/HPAF and Capan1 cells resulted in the downregulation of KRAS and MSST1 expression .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Let-7b", "type": "GeneOrGeneProduct"}, {"text": "CD18/HPAF", "type": "CellLine"}, {"text": "Capan1", "type": "CellLine"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "MSST1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Curcumin also decreased bladder tumor growth in athymic nude mice bearing KU7 cells as xenografts and this was accompanied by decreased Sp1 , Sp3 , and Sp4 protein levels in tumors .

Example answer:
{"entities": [{"text": "Curcumin", "type": "ChemicalEntity"}, {"text": "bladder tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "KU7", "type": "CellLine"}, {"text": "Sp1", "type": "GeneOrGeneProduct"}, {"text": "Sp3", "type": "GeneOrGeneProduct"}, {"text": "Sp4", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Forced expression of MCM8 in RWPE1 cells , the immortalized but non-transformed prostate epithelial cell line , exhibited fast cell growth and transformation , while knock down of MCM8 in PC3 , DU145 and LNCaP cells induced cell growth arrest , and decreased tumour volumes and mortality of severe combined immunodeficiency mice xenografted with PC3 and DU145 cells .

## Item biored:test:1058
Example input:
Sentence: Sequencing of the PAX6 gene , three intragenic mutations including a novel heterozygous splicing-site mutations c.357-3C > G ( p.Ser119fsX ) were identified in the patients of the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "c.357-3C > G", "type": "SequenceVariant"}, {"text": "p.Ser119fsX", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We progressively screened DNA samples from 613 individuals with ID initially for the most frequent ARX mutations ( c.304ins ( GCG ) ( 7 ) 'expansion ' of pA1 and c.429_452dup 'dup24bp ' of pA2 ) .

Example answer:
{"entities": [{"text": "ID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARX", "type": "GeneOrGeneProduct"}, {"text": "c.304ins ( GCG ) ( 7 )", "type": "SequenceVariant"}, {"text": "c.429_452dup", "type": "SequenceVariant"}]}

Example input:
Sentence: We detected 24 p53 mutations in 15/25 ( 60 % ) NMSCs , 1 deletion and 23 base substitutions , the majority ( 78 % ) being UV-specific C to T transitions at bipyrimidine sites .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "NMSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "C to T", "type": "SequenceVariant"}]}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutation screening of all exons of the PAX6 gene was performed by direct sequencing of PCR-amplified DNA fragments .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: METHODS : We examined five hotspot mutations in the PIK3CA gene ( E542K , E545K , E546K , H1047R , and H1047L ) in formalin-fixed and paraffin-embedded tissue sections of paired endoscopic biopsy and surgically resected specimens from 181 patients undergoing curative resection for ESCC between 2000 and 2011 using a Luminex technology-based multiplex gene mutation detection kit .

## Item biored:test:1083
Example input:
Sentence: Interactions have been reported between the low-activity -1021T allele ( rs1611115 ) of DBH and polymorphisms of the pro-inflammatory cytokine genes , IL1A and IL6 , contributing to the risk of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "rs1611115", "type": "SequenceVariant"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Its +1858C > T ( R620W ) polymorphism has been shown to associate with a risk for multiple autoimmune diseases , including type 1 diabetes ( T1D ) and juvenile idiopathic arthritis ( JIA ) .

Example answer:
{"entities": [{"text": "+1858C > T", "type": "SequenceVariant"}, {"text": "R620W", "type": "SequenceVariant"}, {"text": "autoimmune diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "juvenile idiopathic arthritis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations in the coding region of the HNF-6 gene are not associated with Type II diabetes or with changes in insulin responses to glucose among the Caucasians examined .

Example answer:
{"entities": [{"text": "gene", "type": "GeneOrGeneProduct"}, {"text": "diabetes or", "type": "DiseaseOrPhenotypicFeature"}, {"text": "among", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Maternal diabetes significantly increased the levels of CHOP , calnexin , phosphorylated ( p ) -eIF2a , p-PERK , and p-IRE1a ; triggered XBP1 mRNA splicing ; and enhanced ER chaperone gene expression in WT embryos .

Example answer:
{"entities": [{"text": "Maternal diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: The transcription factor hepatocyte nuclear factor ( HNF ) -6 is an upstream regulator of several genes involved in the pathogenesis of maturity-onset diabetes of the young .

Example answer:
{"entities": [{"text": "hepatocyte nuclear factor ( HNF ) -6", "type": "GeneOrGeneProduct"}, {"text": "maturity-onset diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We therefore tested the hypothesis that variability in the HNF-6 gene is associated with subsets of Type II ( non-insulin-dependent ) diabetes mellitus and estimates of insulin secretion in glucose tolerant subjects .

Example answer:
{"entities": [{"text": "HNF-6", "type": "GeneOrGeneProduct"}, {"text": "Type II ( non-insulin-dependent ) diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Hepatocyte nuclear factor-6 : associations between genetic variability and type II diabetes and between genetic variability and estimates of insulin secretion .

Example answer:
{"entities": [{"text": "Hepatocyte nuclear factor-6", "type": "GeneOrGeneProduct"}, {"text": "type II diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Interleukin 6 ( IL-6 ) and Tumor Necrosis Factor alpha ( TNF-alpha ) Single Nucleotide Polymorphisms ( SNPs ) , Inflammation and Metabolism in Gestational Diabetes Mellitus in Inner Mongolia .

## Item biored:test:979
Example input:
Sentence: The melanocortin agonist NDP-MSH dose-dependently inhibited JNK activity in HEK293 cells stably expressing the human MC4R ; effects were reversed by melanocortin receptor antagonist .

Example answer:
{"entities": [{"text": "melanocortin", "type": "GeneOrGeneProduct"}, {"text": "NDP-MSH", "type": "ChemicalEntity"}, {"text": "JNK", "type": "GeneOrGeneProduct"}, {"text": "HEK293", "type": "CellLine"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "MC4R", "type": "GeneOrGeneProduct"}, {"text": "melanocortin receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We used rat pancreatic acini to explore the ability of GI-hormones/neurotransmitters/growth-factors to activate Group-I-PAKs and the signaling cascades involved .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "Group-I-PAKs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The current study shows that the melanocortinergic system interacts with insulin signaling via novel effects on JNK activity .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "JNK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Importantly , this is the first experimental evidence that removal of CB from amyloid precursor protein/presenilin transgenic mice aggravates AD pathogenesis , suggesting that CB has a critical role in AD pathogenesis .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "amyloid precursor", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The melanocortin agonist melanotan II increased insulin-stimulated AKT phosphorylation in the rat hypothalamus in vivo .

Example answer:
{"entities": [{"text": "melanocortin", "type": "GeneOrGeneProduct"}, {"text": "melanotan II", "type": "ChemicalEntity"}, {"text": "insulin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: The aldosterone-sensitive serum- and glucocorticoid-inducible kinase SGK1 has been shown to participate in the stimulation of ENaC and to mediate renal fibrosis following mineralocorticoid and salt excess .

Example answer:
{"entities": [{"text": "aldosterone-sensitive", "type": "ChemicalEntity"}, {"text": "serum- and glucocorticoid-inducible kinase", "type": "GeneOrGeneProduct"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "renal fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mineralocorticoid", "type": "ChemicalEntity"}, {"text": "salt", "type": "ChemicalEntity"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: ADAM12 knockdown also diminished ALDEFLUOR ( + ) and CD44 ( hi ) /CD24 ( -/lo ) CSC-enriched populations in vitro and reduced tumorigenesis in mice in vivo .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: Serum amyloid A potently activated IkappaB kinase , c-Jun N-terminal kinase ( JNK ) , Erk and Akt and enhanced NF-kappaB-dependent luciferase activity in primary human and rat HSCs .

## Item biored:test:1093
Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "ChemicalEntity"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: Both GcgR knockout ( Gcgr ( -/- ) ) mice and db/db mice that were administered GcgR monoclonal antibody displayed lower blood glucose levels accompanied by elevated plasma ghrelin levels .

Example answer:
{"entities": [{"text": "GcgR", "type": "GeneOrGeneProduct"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "blood glucose", "type": "ChemicalEntity"}, {"text": "ghrelin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The prognostic value of serum tumour markers alpha-fetoprotein ( AFP ) and des-gamma-carboxy prothrombin ( DCP ) is limited .

Example answer:
{"entities": [{"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fetoprotein", "type": "GeneOrGeneProduct"}, {"text": "AFP", "type": "GeneOrGeneProduct"}, {"text": "des-gamma-carboxy prothrombin", "type": "GeneOrGeneProduct"}, {"text": "DCP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Serum levels of IL-1beta , CCL11 , IL-2Ralpha , CXCL9 , TRAIL , PDGF-BB , and CCL4 were associated with symptoms accompanying the infection , while IL-6 , IL-9 , IL-10 , IL-13 , IL-15 , IL-17 , G-CSF , and VEGF were associated with predisposition and recurrence of erysipelas .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "CCL11", "type": "GeneOrGeneProduct"}, {"text": "IL-2Ralpha", "type": "GeneOrGeneProduct"}, {"text": "CXCL9", "type": "GeneOrGeneProduct"}, {"text": "TRAIL", "type": "GeneOrGeneProduct"}, {"text": "PDGF-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IL-9", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "IL-15", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "G-CSF", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "erysipelas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Women with both a DHFR deletion allele and low folate intake ( < 400 microg/d from diet plus supplements ) had a significantly greater risk of preterm delivery ( AOR : 5.5 ; 95 % CI : 1.5 , 20.4 ; P = 0.01 ) and a significantly greater risk of having an infant with a low birth weight ( AOR : 8.3 ; 95 % CI : 1.8 , 38.6 ; P = 0.01 ) than did women without a deletion allele and with a folate intake > /=400 microg/d .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "DHFR", "type": "GeneOrGeneProduct"}, {"text": "folate", "type": "ChemicalEntity"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Women with a deletion allele had a significantly greater risk of preterm delivery [ adjusted odds ratio ( AOR ) : 3.0 ; 95 % CI : 1.0 , 8.8 ; P < 0.05 ] than did those without a deletion allele .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Maternal diabetes significantly increased the levels of CHOP , calnexin , phosphorylated ( p ) -eIF2a , p-PERK , and p-IRE1a ; triggered XBP1 mRNA splicing ; and enhanced ER chaperone gene expression in WT embryos .

Example answer:
{"entities": [{"text": "Maternal diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Serum concentrations of CRP , neopterin and IL-6 as markers of inflammation and thrombopoietin ( TPO ) , GCSF , FGF basic and VEGF , HMGB1 , CK-18 ( M65 ) and CK18 fragment ( M30 ) and a panel of proinflammatory chemokines ( CCL2 , CCL3 , CCL4 , CCL5 , CXCL5 and IL-8 ) were measured .

Example answer:
{"entities": [{"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "neopterin", "type": "ChemicalEntity"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thrombopoietin", "type": "GeneOrGeneProduct"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "GCSF", "type": "GeneOrGeneProduct"}, {"text": "FGF basic", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "HMGB1", "type": "GeneOrGeneProduct"}, {"text": "CK-18", "type": "GeneOrGeneProduct"}, {"text": "CK18", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCL3", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Inflammatory biomarkers in serum ( hs-CRP , IL-6 , IL-8 , IL-6/IL-10 ratio ) and placental ( NF-kappaB , IL-6 , IL-8 , IL-6/IL-10 ratio , IL-1b , TNF-alpha ) were significantly different ( p < 0.05 ) between women with GDM and women with healthy pregnancies .

## Item biored:test:1080
Example input:
Sentence: Our aim was to study the associations of individual single nucleotide polymorphisms and haplotypes with adiposity , glucose metabolism , and the risk of type 2 diabetes ( T2D ) .

Example answer:
{"entities": [{"text": "adiposity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , rs6232 , encoding the amino acid exchange N221D , influences insulin sensitivity and glucose homeostasis .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "N221D", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: With the exception of SLC2A2 , other genes were not associated with the risk of type 2 diabetes .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The risk for type 2 diabetes in the AA genotype carriers was increased in the control group ( 5.56 [ 1.78-17.39 ] , P = 0.003 ) but not in the intervention group .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The risk of developing T2D was approximately 2-fold in individuals with genotypes associated with higher 2-hour plasma glucose levels ; the hazard ratios were 2.192 ( p = 0.025 ) for rs2073162-A , 2.191 ( p = 0.027 ) for rs2073163-C , and 1.998 ( p = 0.054 ) for rs1155974-T .

Example answer:
{"entities": [{"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "rs2073162-A", "type": "SequenceVariant"}, {"text": "rs2073163-C", "type": "SequenceVariant"}, {"text": "rs1155974-T", "type": "SequenceVariant"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The p.A1369S variant was associated with a significantly lower risk of type 2 diabetes ( odds ratio [ OR ] 0.93 ; 95 % CI 0.91 , 0.95 ; P = 1.2 x 10 ( -11 ) ) .

Example answer:
{"entities": [{"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The type 2 diabetes risk rs11708067-A allele showed fewer H3K27ac ChIP-seq reads in human islets , lower transcriptional activity in reporter assays in rodent b-cells ( rat 832/13 and mouse MIN6 ) , and increased nuclear protein binding compared with the rs11708067-G allele .

## Item biored:test:1042
Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The androgen receptor ( AR ) gene has polymorphic regions containing variable length glutamine and glycine repeats and these are believed to be associated with PC risk .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results unravel a hidden link between AR and a functional putative PCa risk SNP , whose allele alteration affects androgen regulation of its host gene MLPH .

Example answer:
{"entities": [{"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "ChemicalEntity"}, {"text": "MLPH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The six-nucleotide deletion/insertion variant in the CASP8 promoter region is inversely associated with risk of squamous cell carcinoma of the head and neck .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Taken together , our results demonstrated that Sag is a Kras ( G12D ) -cooperating oncogene required for Kras ( G12D ) -induced immortalization and transformation , and targeting SAG-SCF E3 ligase may , therefore , have therapeutic value for senescence-based cancer treatment .

Example answer:
{"entities": [{"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}, {"text": "SAG-SCF", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: HAT subjects had increased anti-inflammatory genes TGFB1 , TIMP1 , TIMP3 , and TIMP4 while proinflammatory PIG7 and MMP2 were also significantly increased ; all genes , p < 0.025 .

Example answer:
{"entities": [{"text": "TGFB1", "type": "GeneOrGeneProduct"}, {"text": "TIMP1", "type": "GeneOrGeneProduct"}, {"text": "TIMP3", "type": "GeneOrGeneProduct"}, {"text": "TIMP4", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PIG7", "type": "GeneOrGeneProduct"}, {"text": "MMP2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genome-wide association studies have identified genomic loci , whose single-nucleotide polymorphisms ( SNPs ) predispose to prostate cancer ( PCa ) .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Long-term exposure upregulated expression of some malignancy related genes ( STEAP4 , SERPINA3 , SAMD9 , GDF15 , KRT15 , ITGB6 , TP63 , and PGR , as well as the CEACAM , interferon related , and HLA gene families ) .

## Item biored:test:1095
Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Gankyrin deficiency in non-parenchymal cells , but not in parenchymal cells , reduced STAT3 activity , interleukin ( IL ) -6 production , and cancer stem cell marker ( Bmi1 and epithelial cell adhesion molecule [ EpCAM ] ) expression , leading to attenuated tumorigenic potential .

Example answer:
{"entities": [{"text": "Gankyrin", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "interleukin ( IL ) -6", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bmi1", "type": "GeneOrGeneProduct"}, {"text": "epithelial cell adhesion molecule", "type": "GeneOrGeneProduct"}, {"text": "EpCAM", "type": "GeneOrGeneProduct"}, {"text": "tumorigenic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum concentrations of CRP , neopterin and IL-6 as markers of inflammation and thrombopoietin ( TPO ) , GCSF , FGF basic and VEGF , HMGB1 , CK-18 ( M65 ) and CK18 fragment ( M30 ) and a panel of proinflammatory chemokines ( CCL2 , CCL3 , CCL4 , CCL5 , CXCL5 and IL-8 ) were measured .

Example answer:
{"entities": [{"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "neopterin", "type": "ChemicalEntity"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thrombopoietin", "type": "GeneOrGeneProduct"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "GCSF", "type": "GeneOrGeneProduct"}, {"text": "FGF basic", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "HMGB1", "type": "GeneOrGeneProduct"}, {"text": "CK-18", "type": "GeneOrGeneProduct"}, {"text": "CK18", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCL3", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Maternal diabetes significantly increased the levels of CHOP , calnexin , phosphorylated ( p ) -eIF2a , p-PERK , and p-IRE1a ; triggered XBP1 mRNA splicing ; and enhanced ER chaperone gene expression in WT embryos .

Example answer:
{"entities": [{"text": "Maternal diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , the meta-analysis of Taiwanese Han Chinese , Brazilian , and Polish populations showed that the Gln/Gln or Gln/Arg genotype and Gln allele were associated with SLE incidence .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although treatment with the pancreatic b-cell toxin streptozotocin induced hyperglycemia and raised plasma ghrelin levels in wild-type mice , hyperglycemia was averted in similarly treated Gcgr ( -/- ) mice and the plasma ghrelin level was further increased .

Example answer:
{"entities": [{"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "hyperglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ghrelin", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: She had profound insulin resistance , diabetes , severe hypertriglyceridemia and relapsing pancreatitis , while her pre-pubescent daughter had normal fat distribution but elevated plasma triglycerides and C-peptide and depressed high-density lipoprotein cholesterol .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertriglyceridemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pancreatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "triglycerides", "type": "ChemicalEntity"}, {"text": "C-peptide", "type": "ChemicalEntity"}, {"text": "high-density lipoprotein cholesterol", "type": "ChemicalEntity"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Input:
Sentence: CONCLUSIONS TNF-alpha -857C/T SNP , hs-CRP , IL-6 , IL-8 , and IL-6/IL-10 were associated with GDM in women from Inner Mongolia , as was serious inflammation and disordered lipid and glucose metabolisms .

## Item biored:test:1094
Example input:
Sentence: In tissue samples with normal fibroblasts ( NFs ) serving as control samples , expression of TGF-beta1 and -beta2 was decreased when compared to keloid fibroblasts ( KFs ) , while expression of TGF-beta3 and of TGF-betaRII was significantly higher in NFs .

Example answer:
{"entities": [{"text": "TGF-beta1 and -beta2", "type": "GeneOrGeneProduct"}, {"text": "keloid", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-beta3", "type": "GeneOrGeneProduct"}, {"text": "TGF-betaRII", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Rare but not common IRS2 variants may play a role in the regulation of body weight but not an essential role in fasting glucose homeostasis in Hispanic children .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Maternal diabetes significantly increased the levels of CHOP , calnexin , phosphorylated ( p ) -eIF2a , p-PERK , and p-IRE1a ; triggered XBP1 mRNA splicing ; and enhanced ER chaperone gene expression in WT embryos .

Example answer:
{"entities": [{"text": "Maternal diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Serum concentrations of CRP , neopterin and IL-6 as markers of inflammation and thrombopoietin ( TPO ) , GCSF , FGF basic and VEGF , HMGB1 , CK-18 ( M65 ) and CK18 fragment ( M30 ) and a panel of proinflammatory chemokines ( CCL2 , CCL3 , CCL4 , CCL5 , CXCL5 and IL-8 ) were measured .

Example answer:
{"entities": [{"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "neopterin", "type": "ChemicalEntity"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thrombopoietin", "type": "GeneOrGeneProduct"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "GCSF", "type": "GeneOrGeneProduct"}, {"text": "FGF basic", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "HMGB1", "type": "GeneOrGeneProduct"}, {"text": "CK-18", "type": "GeneOrGeneProduct"}, {"text": "CK18", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCL3", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Women with both a DHFR deletion allele and low folate intake ( < 400 microg/d from diet plus supplements ) had a significantly greater risk of preterm delivery ( AOR : 5.5 ; 95 % CI : 1.5 , 20.4 ; P = 0.01 ) and a significantly greater risk of having an infant with a low birth weight ( AOR : 8.3 ; 95 % CI : 1.8 , 38.6 ; P = 0.01 ) than did women without a deletion allele and with a folate intake > /=400 microg/d .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "DHFR", "type": "GeneOrGeneProduct"}, {"text": "folate", "type": "ChemicalEntity"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : LAT and HAT groups were matched in age , obesity , insulin , and glucose , and had similar expression of insulin-related genes ( InsR , IRS-1 ) .

Example answer:
{"entities": [{"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "insulin-related", "type": "GeneOrGeneProduct"}, {"text": "InsR", "type": "GeneOrGeneProduct"}, {"text": "IRS-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Resequencing of IRS2 reveals rare variants for obesity but not fasting glucose homeostasis in Hispanic children .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Differences were found for serum FBG , FINS , HOMA-IR , and HOMA-beta , and placental IRS-1 , IRS-2 , leptin , adiponectin , visfatin , RBP-4 , chemerin , nesfatin-1 , FATP-4 , EL , LPL , FABP-1 , FABP-3 , FABP-4 , and FABP-5 .
