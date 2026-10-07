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

## Item biored:test:1048
Example input:
Sentence: Previously , we showed that following etoposide ( ETO ) treatment embryonal carcinoma PA-1 cells undergo a p53-dependent upregulation of OCT4A and p21Cip1 ( governing self-renewal and regulating cell cycle inhibition and senescence , respectively ) .

Example answer:
{"entities": [{"text": "etoposide", "type": "ChemicalEntity"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "embryonal carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p53-dependent", "type": "GeneOrGeneProduct"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: b-Catenin is a critical component of canonical Wnt signaling and is essential for the regulation of cell differentiation and morphogenesis during embryogenesis .

Example answer:
{"entities": [{"text": "b-Catenin", "type": "GeneOrGeneProduct"}, {"text": "Wnt", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : The symptoms of infertility observed in the DMC1 homozygote mutation carrier and in both patients with a heterozygous substitution in exon 2 of the MSH5 gene provide indirect evidence of the role of genes involved in meiotic recombination in the regulation of ovarian function .

Example answer:
{"entities": [{"text": "infertility", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: There was a marked increase in the number of TUNEL positive cells and nestin positive cells in BCNU-exposed group , but a decreased immunoreactivity to glial fibrillary acidic protein , synaptophysin and transforming growth factor beta1 was observed , indicating a delayed maturation , and melatonin significantly reversed these changes .

Example answer:
{"entities": [{"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}, {"text": "transforming growth factor beta1", "type": "GeneOrGeneProduct"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : These results indicate that ADAM12 actively supports the CSC phenotype in claudin-low breast cancer cells via modulation of the EGFR pathway .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "claudin-low", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CCK and other GI-hormones/neurotransmitters/growth-factors activate PAK2 via small GTPases ( CDC42/Rac1 ) , PKC and SFK but not cytosolic calcium or PI3K .

Example answer:
{"entities": [{"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "small GTPases", "type": "GeneOrGeneProduct"}, {"text": "CDC42/Rac1", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "SFK", "type": "GeneOrGeneProduct"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Drosophila ovarian germline stem cells ( GSCs ) are maintained by Dpp signaling and the Pumilio ( Pum ) and Nanos ( Nos ) translational repressors .

Example answer:
{"entities": [{"text": "Drosophila", "type": "OrganismTaxon"}, {"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Pumilio", "type": "GeneOrGeneProduct"}, {"text": "Pum", "type": "GeneOrGeneProduct"}, {"text": "Nanos", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We hypothesized that activin and/or GnRH pathways may be modulated by BMP-4 , but neither the activin-stimulated phosphorylation of Smad2/3 nor the GnRH-induced ERK1/2 or cAMP response element-binding phosphorylation were modified .

Example answer:
{"entities": [{"text": "activin", "type": "GeneOrGeneProduct"}, {"text": "GnRH", "type": "GeneOrGeneProduct"}, {"text": "BMP-4", "type": "GeneOrGeneProduct"}, {"text": "activin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "Smad2/3", "type": "GeneOrGeneProduct"}, {"text": "GnRH-induced", "type": "GeneOrGeneProduct"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Upon division , Dpp signaling is extinguished , and Nos is downregulated in one daughter cell , causing it to switch to a differentiating cystoblast ( CB ) .

Example answer:
{"entities": [{"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: CenpH regulates meiotic G2/M transition by modulating the APC/CCdh1-cyclin B1 pathway in oocytes .

## Item biored:test:995
Example input:
Sentence: Here , we show that simultaneous overexpression of the mitotic checkpoint protein Mad2 with Kras ( G12D ) or Her2 in mammary glands of adult mice results in mitotic checkpoint overactivation and a delay in tumor onset .

Example answer:
{"entities": [{"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "GeneOrGeneProduct"}, {"text": "Her2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further , expression of miRNA biosynthetic machinery including Dicer , Exportin-5 , TRKRA , and TARBP2 were downregulated , while DGCR8 and Ago2 were upregulated in KC mice .

Example answer:
{"entities": [{"text": "Dicer", "type": "GeneOrGeneProduct"}, {"text": "Exportin-5", "type": "GeneOrGeneProduct"}, {"text": "TRKRA", "type": "GeneOrGeneProduct"}, {"text": "TARBP2", "type": "GeneOrGeneProduct"}, {"text": "DGCR8", "type": "GeneOrGeneProduct"}, {"text": "Ago2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The expression of the Msx2 gene and phosphorylated-Smad1/5/8 , possible readouts of Bmp signaling , was also increased in the mutants .

Example answer:
{"entities": [{"text": "Msx2", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Aberrant caveolin-1-mediated Smad signaling and proliferation identified by analysis of adenine 474 deletion mutation ( c.474delA ) in patient fibroblasts : a new perspective on the mechanism of pulmonary hypertension .

Example answer:
{"entities": [{"text": "caveolin-1-mediated", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "adenine 474 deletion", "type": "SequenceVariant"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pulmonary hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Collectively , these results extend the pattern of TMPRSS6 mutations associated with IRIDA and functionally demonstrate that mutations affecting protease regions other than the catalytic domain may have a profound impact in the regulatory role of matriptase-2 during iron deficiency .

Example answer:
{"entities": [{"text": "TMPRSS6", "type": "GeneOrGeneProduct"}, {"text": "IRIDA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "matriptase-2", "type": "GeneOrGeneProduct"}, {"text": "iron deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: We also demonstrate that the A118D SEA domain mutation causes an intra-molecular structural imbalance that impairs matriptase-2 activation .

Example answer:
{"entities": [{"text": "A118D", "type": "SequenceVariant"}, {"text": "matriptase-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recent reports have demonstrated that mutations in the OPHN1 gene were responsible for a syndromic rather than non-specific mental retardation .

Example answer:
{"entities": [{"text": "OPHN1", "type": "GeneOrGeneProduct"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Five of the forty genes -- ENT3 , IDP3 , JEM1 , ARG2 and HSP82 -- ranked highest in their ability to block alpha-syn-induced reactive oxygen species accumulation , and these five genes were characterized in more detail .

Example answer:
{"entities": [{"text": "ENT3", "type": "GeneOrGeneProduct"}, {"text": "IDP3", "type": "GeneOrGeneProduct"}, {"text": "JEM1", "type": "GeneOrGeneProduct"}, {"text": "ARG2", "type": "GeneOrGeneProduct"}, {"text": "HSP82", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn-induced", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}]}

Input:
Sentence: By identifying genes mis-expressed in mol1 mutants , we demonstrate that MOL1 represses genes associated with stress-related ethylene and jasmonic acid hormone signaling pathways which have known roles in coordinating lateral growth of the Arabidopsis stem .

## Item biored:test:1079
Example input:
Sentence: Here we describe the characterization of the rs368698783 ( +25 G- > A ) polymorphism of the Ag-globin gene associated in b ( 0 ) 39 thalassemia patients with high HbF in erythroid precursor cells .

Example answer:
{"entities": [{"text": "rs368698783", "type": "SequenceVariant"}, {"text": "+25 G- > A", "type": "SequenceVariant"}, {"text": "Ag-globin", "type": "GeneOrGeneProduct"}, {"text": "b ( 0 ) 39 thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HbF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A common missense variant in the gene encoding a component of the sulfonylurea receptor ( ABCC8 p.A1369S ) promotes closure of the target channel of sulfonylurea therapy and is associated with increased insulin secretion , thus mimicking the effects of sulfonylurea therapy .

Example answer:
{"entities": [{"text": "sulfonylurea receptor", "type": "GeneOrGeneProduct"}, {"text": "ABCC8", "type": "GeneOrGeneProduct"}, {"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "sulfonylurea", "type": "ChemicalEntity"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The results show that the rs368698783 polymorphism is present in b-thalassemia patients in the 5'UTR sequence ( +25 ) of the Ag-globin gene , known to affect the LYAR ( human homologue of mouse Ly-1 antibody reactive clone ) binding site 5'-GGTTAT-3 ' .

Example answer:
{"entities": [{"text": "rs368698783", "type": "SequenceVariant"}, {"text": "b-thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Ag-globin", "type": "GeneOrGeneProduct"}, {"text": "LYAR", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "Ly-1 antibody reactive clone", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Common single nucleotide polymorphisms ( SNPs ) within this gene , rs6232 and rs6235 , are associated with obesity .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RNA sequencing identified a significant overlap between ADAM12- and Epidermal Growth Factor Receptor ( EGFR ) -regulated genes .

Example answer:
{"entities": [{"text": "ADAM12-", "type": "GeneOrGeneProduct"}, {"text": "Epidermal Growth Factor Receptor", "type": "GeneOrGeneProduct"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TS enhancer region , 3R G > C single nucleotide polymorphism ( SNP ) , and TS 1494del6 polymorphisms were assessed in both fresh-frozen normal mucosa and tumor .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "G > C", "type": "SequenceVariant"}, {"text": "1494del6", "type": "SequenceVariant"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SNP 10510452_139 in the promoter region was shown to have a high posterior probability ( P = 0.77-0.86 ) of influencing BMI , fat mass , and waist circumference in Hispanic children .

Example answer:
{"entities": [{"text": "SNP 10510452_139", "type": "SequenceVariant"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , rs6232 , encoding the amino acid exchange N221D , influences insulin sensitivity and glucose homeostasis .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "N221D", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Input:
Sentence: rs11708067 overlaps a predicted enhancer region in pancreatic islets .

## Item biored:test:1031
Example input:
Sentence: METHODS : We performed comprehensive genomic profiling ( CGP ) for coding regions in more than 300 cancer-related genes of 186 GISTs to assess for their somatic alterations .

Example answer:
{"entities": [{"text": "cancer-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GISTs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Differential expression of microRNAs ( miRNAs ) has been demonstrated in various cancers , including pancreatic cancer ( PC ) .

Example answer:
{"entities": [{"text": "cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pancreatic cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As previously observed for glioblastomas in Europe , there was a positive association between EGFR amplification and p16 deletion ( p=0.009 ) , whereas there was an inverse association between TP53 mutations and p16 deletion ( p=0.049 ) in glioblastomas in Japan .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genome-wide association studies have identified genomic loci , whose single-nucleotide polymorphisms ( SNPs ) predispose to prostate cancer ( PCa ) .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The correlation between survival and NEK2 expression was analyzed in 359 patients with HCC using RNASeqV2 data available from The Cancer Genome Atlas ( TCGA ) website ( https : //tcga-data.nci.nih.gov/tcga/ ) .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Mining oncogenomic databases revealed that loss of the PI4K2B allele and underexpression of PI4KIIb mRNA are associated with human cancers .

## Item biored:test:1034
Example input:
Sentence: The effects of alcohol consumption on prostate cancer incidence and survival remain unclear , potentially due to methodological limitations of observational studies .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Faced with the selective pressure of oncogene withdrawal , Mad2-positive tumors have a higher frequency of developing persistent subclones that avoid remission and continue to grow .

Example answer:
{"entities": [{"text": "Mad2-positive", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: IMPORTANCE OF THE FIELD : Fluoropyrimidines , in particular 5-fluorouracil ( 5-FU ) , have been the mainstay of treatment for several solid tumors , including colorectal , breast and head and neck cancers , for > 40 years .

Example answer:
{"entities": [{"text": "Fluoropyrimidines", "type": "ChemicalEntity"}, {"text": "5-fluorouracil", "type": "ChemicalEntity"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "colorectal , breast and head and neck cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results suggest that alcohol consumption is unlikely to affect prostate cancer incidence , but it may influence disease progression .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , we investigated the associations of genetic variants in alcohol-metabolising genes with prostate cancer incidence and survival .

Example answer:
{"entities": [{"text": "alcohol-metabolising", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A key hallmark of cancer cells is their altered metabolism , known as Warburg effect .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Study-specific associations of 68 single nucleotide polymorphisms ( SNPs ) in 8 alcohol-metabolising genes ( Alcohol Dehydrogenases ( ADHs ) and Aldehyde Dehydrogenases ( ALDHs ) ) with prostate cancer diagnosis and prostate cancer-specific mortality , by grade , were assessed using logistic and Cox regression models , respectively .

Example answer:
{"entities": [{"text": "alcohol-metabolising", "type": "ChemicalEntity"}, {"text": "Alcohol Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ADHs", "type": "GeneOrGeneProduct"}, {"text": "Aldehyde Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ALDHs", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prostate", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alcohol consumption and prostate cancer incidence and progression : A Mendelian randomisation study .

Example answer:
{"entities": [{"text": "Alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: We found little evidence that variants in alcohol metabolising genes were associated with prostate cancer diagnosis .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Long-term exposure of MCF-7 breast cancer cells to ethanol stimulates oncogenic features .

## Item biored:test:1064
Example input:
Sentence: Certain concepts concerning EPO/EPOR action modes have been challenged by in vivo studies : Bcl-x levels are elevated in maturing erythroblasts , but not in their progenitors ; truncated EPOR alleles that lack a major p85/PI3K recruitment site nonetheless promote polycythemia ; and Erk1 disruption unexpectedly bolsters erythropoiesis .

Example answer:
{"entities": [{"text": "EPO/EPOR", "type": "GeneOrGeneProduct"}, {"text": "Bcl-x", "type": "GeneOrGeneProduct"}, {"text": "EPOR", "type": "GeneOrGeneProduct"}, {"text": "p85/PI3K", "type": "GeneOrGeneProduct"}, {"text": "polycythemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Erk1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : When compared with Crohn 's disease patients without CARD15 mutations , the presence of at least one CARD15 variant in Crohn 's disease patients more frequently led to gASCA positivity ( 66.1 % versus 51.5 % , p < 0.0001 ) and ALCA positivity ( 43.3 % versus 34.9 % , p = 0.018 ) and higher gASCA titers ( 85.7 versus 51.8 ELISA units , p < 0.0001 ) , independent of ileal involvement .

Example answer:
{"entities": [{"text": "Crohn 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CARD15", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: CONCLUSIONS : The PIK3CA mutation status was highly concordant between endoscopic biopsy and surgically resected specimens from the same patient , suggesting that endoscopic biopsy specimens can be clinically used to detect PIK3CA mutations in patients with ESCC .

## Item biored:test:1044
Example input:
Sentence: PA-1 cells treated with ETO display highly heterogeneous increases in OCT4A and p21Cip1 indicative of dis-adaptation catastrophe .

Example answer:
{"entities": [{"text": "PA-1", "type": "CellLine"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Silencing OCT4A suppresses p21Cip1 , changes cell cycle regulation and subsequently suppresses terminal senescence ; p21Cip1-silencing did not affect OCT4A expression or cellular phenotype .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1-silencing", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Instead , ETO-induced OCT4A was concomitant with activation of AMPK , a key component of metabolic stress and autophagy regulation .

Example answer:
{"entities": [{"text": "ETO-induced", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Changes in microRNA ( miRNA ) expression during pancreatic cancer development and progression in a genetically engineered KrasG12D ; Pdx1-Cre mouse ( KC ) model .

Example answer:
{"entities": [{"text": "pancreatic cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KrasG12D", "type": "GeneOrGeneProduct"}, {"text": "Pdx1-Cre", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Interestingly , the differential expression of miRNA in mice also corroborated with the miRNA expression in human PC cell lines and tissue samples ; ectopic expression of Let-7b in CD18/HPAF and Capan1 cells resulted in the downregulation of KRAS and MSST1 expression .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Let-7b", "type": "GeneOrGeneProduct"}, {"text": "CD18/HPAF", "type": "CellLine"}, {"text": "Capan1", "type": "CellLine"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "MSST1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SOX2 and NANOG expression did not change following ETO treatment suggesting a dissociation of OCT4A from its pluripotency function .

Example answer:
{"entities": [{"text": "SOX2", "type": "GeneOrGeneProduct"}, {"text": "NANOG", "type": "GeneOrGeneProduct"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Differential expression of microRNAs ( miRNAs ) has been demonstrated in various cancers , including pancreatic cancer ( PC ) .

Example answer:
{"entities": [{"text": "cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pancreatic cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Previously , we showed that following etoposide ( ETO ) treatment embryonal carcinoma PA-1 cells undergo a p53-dependent upregulation of OCT4A and p21Cip1 ( governing self-renewal and regulating cell cycle inhibition and senescence , respectively ) .

Example answer:
{"entities": [{"text": "etoposide", "type": "ChemicalEntity"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "embryonal carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p53-dependent", "type": "GeneOrGeneProduct"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Role of stress-activated OCT4A in the cell fate decisions of embryonal carcinoma cells treated with etoposide .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "embryonal carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoposide", "type": "ChemicalEntity"}]}

Input:
Sentence: A similar treatment also modulated numerous microRNAs ( miRs ) including one regulator of Oct4 as well as miRs involved in oncogenesis and/or malignancy , with only a few estrogen-induced miRs .

## Item biored:test:1045
Example input:
Sentence: Amphetamine abuse was predictive of larger cranial to body growth ratios .

Example answer:
{"entities": [{"text": "Amphetamine", "type": "ChemicalEntity"}]}

Example input:
Sentence: The effects of alcohol consumption on prostate cancer incidence and survival remain unclear , potentially due to methodological limitations of observational studies .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A key hallmark of cancer cells is their altered metabolism , known as Warburg effect .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because intensity of alcohol consumption is associated with poorer fetal outcomes , separate analyses were conducted for the heavy ( average of > or=5 drinks per drinking day ) alcohol consumers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND : More than 3 decades after Jones and Smith ( 1973 ) reported on the devastation caused by alcohol exposure on fetal development , the rates of heavy drinking during pregnancy remain relatively unchanged .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results suggest that alcohol consumption is unlikely to affect prostate cancer incidence , but it may influence disease progression .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Impact of alcohol exposure after pregnancy recognition on ultrasonographic fetal growth measures .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Alcohol consumption and prostate cancer incidence and progression : A Mendelian randomisation study .

Example answer:
{"entities": [{"text": "Alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found little evidence that variants in alcohol metabolising genes were associated with prostate cancer diagnosis .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Any alcohol consumption postpregnancy recognition among the heavy drinkers resulted in reduced cerebellar growth as well as decreased cranial to body growth in comparison with women who either quit drinking or who were nondrinkers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "reduced cerebellar growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "decreased cranial to body growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Input:
Sentence: Long-term 25 mM ethanol also induced a 5.6-fold upregulation of anchorage-independent growth , an indicator of malignant-like features .

## Item biored:test:997
Example input:
Sentence: To determine the pathogenic importance of CB depletions in AD models , we crossed 5 familial AD mutations ( 5XFAD ; Tg ) mice with CB knock-out ( CBKO ) mice and generated a novel line CBKO.5XFAD ( CBKOTg ) mice .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CBKO", "type": "GeneOrGeneProduct"}, {"text": "CBKO.5XFAD", "type": "GeneOrGeneProduct"}, {"text": "CBKOTg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both GcgR knockout ( Gcgr ( -/- ) ) mice and db/db mice that were administered GcgR monoclonal antibody displayed lower blood glucose levels accompanied by elevated plasma ghrelin levels .

Example answer:
{"entities": [{"text": "GcgR", "type": "GeneOrGeneProduct"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "blood glucose", "type": "ChemicalEntity"}, {"text": "ghrelin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Although treatment with the pancreatic b-cell toxin streptozotocin induced hyperglycemia and raised plasma ghrelin levels in wild-type mice , hyperglycemia was averted in similarly treated Gcgr ( -/- ) mice and the plasma ghrelin level was further increased .

Example answer:
{"entities": [{"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "hyperglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ghrelin", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: Overload-induced [ ( 3 ) H ] -2-deoxy-d-glucose uptake was not inhibited by d-fructose , demonstrating that the fructose-transporting GLUT2 , GLUT5 , GLUT8 , and GLUT12 do not mediate this effect .

Example answer:
{"entities": [{"text": "[ ( 3 ) H ] -2-deoxy-d-glucose", "type": "ChemicalEntity"}, {"text": "d-fructose", "type": "ChemicalEntity"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GLUT5", "type": "GeneOrGeneProduct"}, {"text": "GLUT8", "type": "GeneOrGeneProduct"}, {"text": "GLUT12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , gene-targeted mice lacking SGK1 showed blunted volume retention , yet were not protected against renal fibrosis during experimental nephrotic syndrome .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "volume retention", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the current study , we investigated whether a physiological intervention by feeding 40 % high fat diet ( HFD ) , which induces obesity in male Sprague-Dawley rats ( 250-275 g ) , sensitizes to doxorubicin-induced cardiotoxicity .

Example answer:
{"entities": [{"text": "fat", "type": "ChemicalEntity"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Superoxide dismutase 1 overexpression in mice abolishes maternal diabetes-induced endoplasmic reticulum stress in diabetic embryopathy .

Example answer:
{"entities": [{"text": "Superoxide dismutase 1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "maternal", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "embryopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Male CD-1 mice were treated with warfarin ( 2 mg/kg over 24 h ) , resulting in a mean ( +/-s.d . )

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Overload-induced muscle glucose uptake and hypertrophic growth were not impaired in muscle-specific GLUT4 knockout mice , demonstrating that GLUT4 is not necessary for these processes .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "GLUT4", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: Male 11b-HSD1 Knockout Mice Fed Trans-Fats and Fructose Are Not Protected From Metabolic Syndrome or Nonalcoholic Fatty Liver Disease .

## Item biored:test:1068
Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Patients with MDM with the homozygous SLURP-1 G86R mutation may have an impaired T-cell activation .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}, {"text": "G86R", "type": "SequenceVariant"}]}

Example input:
Sentence: DOCK8 expression was reduced in 62/71 ( 87 % ) primary lung cancers compared with normal lung tissue , and the reduction occurred irrespective of the histological type of lung cancer .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "lung cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Deregulation of these gene products may interfere with the signalling pathways that are involved in MCL tumour development and maintenance .

Example answer:
{"entities": [{"text": "MCL tumour", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thus , the present results suggest that genetic and epigenetic inactivation of DOCK8 is involved in the development and/or progression of lung and other cancers by disturbing such regulations .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "lung and other cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The six-nucleotide deletion/insertion variant in the CASP8 promoter region is inversely associated with risk of squamous cell carcinoma of the head and neck .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The gain of MCM8 is associated with aggressive clinical features of several human cancers .

## Item biored:test:1090
Example input:
Sentence: Our objective was to resequence insulin receptor substrate 2 ( IRS2 ) to identify variants associated with obesity- and diabetes-related traits in Hispanic children .

Example answer:
{"entities": [{"text": "insulin receptor substrate 2", "type": "GeneOrGeneProduct"}, {"text": "IRS2", "type": "GeneOrGeneProduct"}, {"text": "obesity-", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes-related", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PBMCs from homozygotes and wild-type controls were stimulated with anti-CD3/anti-CD28 antibodies and the level of T-cell activation was determined by the stimulation index .

Example answer:
{"entities": []}

Example input:
Sentence: Plasma TAFI , tPA , and PAI-1 antigen levels were measured at baseline and after 3 months of treatment by commercially available ELISA kits .

Example answer:
{"entities": [{"text": "TAFI", "type": "GeneOrGeneProduct"}, {"text": "tPA", "type": "GeneOrGeneProduct"}, {"text": "PAI-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In an effort to identify tumor associated antigens that may be useful for immunotherapy , we utilized serological analysis of recombinant cDNA expression libraries ( SEREX ) technique to identify breast cancer-associated antigens .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Semiquantitative assessment of the density of NOX4 colabeling with lectin-stained retinal ECs was determined by immunolabeling of retinal cryosections from P18 pups in OIR or in RA .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "lectin-stained", "type": "GeneOrGeneProduct"}, {"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum concentrations of CRP , neopterin and IL-6 as markers of inflammation and thrombopoietin ( TPO ) , GCSF , FGF basic and VEGF , HMGB1 , CK-18 ( M65 ) and CK18 fragment ( M30 ) and a panel of proinflammatory chemokines ( CCL2 , CCL3 , CCL4 , CCL5 , CXCL5 and IL-8 ) were measured .

Example answer:
{"entities": [{"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "neopterin", "type": "ChemicalEntity"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thrombopoietin", "type": "GeneOrGeneProduct"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "GCSF", "type": "GeneOrGeneProduct"}, {"text": "FGF basic", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "HMGB1", "type": "GeneOrGeneProduct"}, {"text": "CK-18", "type": "GeneOrGeneProduct"}, {"text": "CK18", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCL3", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Several regulated genes were validated using enzyme-linked immunoassays including IL-1beta and CXCL1 .

Example answer:
{"entities": []}

Example input:
Sentence: Expression of cytokines and IDO mRNA in OHSCs was measured by real-time RT-PCR and cytokine protein was measured by enzyme-linked immunosorbent assays ( ELISAs ) .

Example answer:
{"entities": [{"text": "IDO", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The excretion and genetic expression of inflammatory factors were , respectively , estimated by enzyme-linked immunosorbent assay ( ELISA ) and real-time polymerase chain reaction ( PCR ) .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Enzyme linked immunosorbent assay ( ELISA ) was performed to analyze inflammatory biomarkers and adipokines .

## Item biored:test:1037
Example input:
Sentence: A new Rab6 homolog cDNA , Rab6c , was discovered by a hypermethylated DNA fragment probe that was isolated from a human multidrug resistant ( MDR ) breast cancer cell line , MCF7/AdrR , by the methylation sensitive-representational difference analysis ( MS-RDA ) technique .

Example answer:
{"entities": [{"text": "Rab6", "type": "GeneOrGeneProduct"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCF7/AdrR", "type": "CellLine"}]}

Example input:
Sentence: CONCLUSIONS : These results indicate that ADAM12 actively supports the CSC phenotype in claudin-low breast cancer cells via modulation of the EGFR pathway .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "claudin-low", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The AT1aKO bone marrow ( BM ) ( AT1aKO-BM ) > WT showed suppressed formation of liver metastasis compared with WT-BM > WT .

Example answer:
{"entities": [{"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "AT1aKO-BM", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : ADAM12 is upregulated in human breast cancers and is a predictor of chemoresistance in estrogen receptor-negative tumors .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "breast cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "estrogen", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found little evidence that variants in alcohol metabolising genes were associated with prostate cancer diagnosis .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Metalloprotease-disintegrin ADAM12 actively promotes the stem cell-like phenotype in claudin-low breast cancer .

Example answer:
{"entities": [{"text": "Metalloprotease-disintegrin", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "claudin-low", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We modulated the b-catenin gene conditionally in endodermal epithelia by utilizing tamoxifen-inducible Cre driver line ( Shh ( CreERT2 ) ) .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "tamoxifen-inducible", "type": "ChemicalEntity"}, {"text": "Shh", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , Sal administration significantly suppresses epithelial-mesenchymal transition ( EMT ) , as evidenced by a decreased expression of alpha-SMA , vimentin , TGF-beta1 , snail , slug , and a largely restored expression of E-cadherin .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "alpha-SMA", "type": "GeneOrGeneProduct"}, {"text": "vimentin", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "snail", "type": "GeneOrGeneProduct"}, {"text": "slug", "type": "GeneOrGeneProduct"}, {"text": "E-cadherin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: ADAM12 is induced during epithelial-to-mesenchymal transition , a feature associated with claudin-low breast tumors , which are enriched in cancer stem cell ( CSC ) markers .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "claudin-low", "type": "GeneOrGeneProduct"}, {"text": "breast tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In mammary epithelial cells , Star-PAP knockdown partially transformed these cells and induced them to undergo epithelial-mesenchymal transition ( EMT ) .

Example answer:
{"entities": [{"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We previously showed that long-term exposure to 2.5 mM ethanol ( blood alcohol ~0.012 % ) of MCF-12A , a human normal epithelial breast cell line , induced epithelial mesenchymal transition ( EMT ) and oncogenic transformation .

## Item biored:test:1085
Example input:
Sentence: In contrast to alleles that cause early-onset MLD , the arginine84 to glutamine substitution is associated with some residual ARSA activity .

Example answer:
{"entities": [{"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine84 to glutamine", "type": "SequenceVariant"}, {"text": "ARSA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Arg124Cys and Arg555Trp appear to be the predominant mutations causing LCD and GCD , respectively , in the population studied .

Example answer:
{"entities": [{"text": "Arg124Cys", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: AIMS : Individuals with both diabetes mellitus ( DM ) and the Haptoglobin ( Hp ) 2-2 genotype are at increased risk of cardiovascular disease .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Haptoglobin", "type": "GeneOrGeneProduct"}, {"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "cardiovascular disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This phenotype resembled that of bone morphogenetic protein receptor ( BMPR ) 1 and Gdf5-deficient mice .

Example answer:
{"entities": [{"text": "bone morphogenetic protein receptor ( BMPR ) 1", "type": "GeneOrGeneProduct"}, {"text": "Gdf5-deficient", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Women were significantly more likely to experience lactic acidosis , while men were significantly more likely to experience immune reconstitution syndrome ( p < 0.05 ) .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "lactic acidosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "immune reconstitution syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: She had profound insulin resistance , diabetes , severe hypertriglyceridemia and relapsing pancreatitis , while her pre-pubescent daughter had normal fat distribution but elevated plasma triglycerides and C-peptide and depressed high-density lipoprotein cholesterol .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertriglyceridemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pancreatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "triglycerides", "type": "ChemicalEntity"}, {"text": "C-peptide", "type": "ChemicalEntity"}, {"text": "high-density lipoprotein cholesterol", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Maternal diabetes significantly increased the levels of CHOP , calnexin , phosphorylated ( p ) -eIF2a , p-PERK , and p-IRE1a ; triggered XBP1 mRNA splicing ; and enhanced ER chaperone gene expression in WT embryos .

Example answer:
{"entities": [{"text": "Maternal diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Superoxide dismutase 1 overexpression in mice abolishes maternal diabetes-induced endoplasmic reticulum stress in diabetic embryopathy .

Example answer:
{"entities": [{"text": "Superoxide dismutase 1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "maternal", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "embryopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although treatment with the pancreatic b-cell toxin streptozotocin induced hyperglycemia and raised plasma ghrelin levels in wild-type mice , hyperglycemia was averted in similarly treated Gcgr ( -/- ) mice and the plasma ghrelin level was further increased .

Example answer:
{"entities": [{"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "hyperglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ghrelin", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both GcgR knockout ( Gcgr ( -/- ) ) mice and db/db mice that were administered GcgR monoclonal antibody displayed lower blood glucose levels accompanied by elevated plasma ghrelin levels .

Example answer:
{"entities": [{"text": "GcgR", "type": "GeneOrGeneProduct"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "blood glucose", "type": "ChemicalEntity"}, {"text": "ghrelin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: GDM women are with inflammatory and metabolisms abnormalities .

## Item biored:test:1029
Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Molecular dynamic ( MD ) simulations showed that the overall effect of the mutation p.Val204Asp is disruption of hydrogen bonding between Gln223 and Glu441 , leading Ser198 and His438 to move away from each other with subsequent disruption of the catalytic triad functionality regardless of the type of substrate .

Example answer:
{"entities": [{"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Example input:
Sentence: Furthermore , PI3K/Akt pathway signaling was also increased in Eu-myc B cells , and this increase was partially suppressed with ibrutinib .

Example answer:
{"entities": [{"text": "PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "ibrutinib", "type": "ChemicalEntity"}]}

Example input:
Sentence: Collectively , our findings present a new approach for identifying ciliary proteins , and unveil RAB28 , a GTPase most closely related to the BBS protein RABL4/IFT27 , as an IFT-associated cargo with BBSome-dependent cell autonomous and non-autonomous functions at the ciliary base .

Example answer:
{"entities": [{"text": "RAB28", "type": "GeneOrGeneProduct"}, {"text": "GTPase", "type": "GeneOrGeneProduct"}, {"text": "BBS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RABL4/IFT27", "type": "GeneOrGeneProduct"}, {"text": "BBSome-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our interpretation is that Ent3p mediates the transport of alpha-syn to the vacuole for proteolytic degradation .

Example answer:
{"entities": [{"text": "Ent3p", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To investigate this question , we have developed in vitro motility assays with purified DDB and BICD2 's membrane vesicle partner , the GTPase Rab6a .

Example answer:
{"entities": [{"text": "DDB", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "GTPase Rab6a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Whole-Organism Developmental Expression Profiling Identifies RAB-28 as a Novel Ciliary GTPase Associated with the BBSome and Intraflagellar Transport .

Example answer:
{"entities": [{"text": "RAB-28", "type": "GeneOrGeneProduct"}, {"text": "GTPase", "type": "GeneOrGeneProduct"}, {"text": "BBSome", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Whereas inactive GDP-bound RAB-28 displays no IFT movement and diffuse localisation , GTP-bound ( activated ) RAB-28 concentrates at the periciliary membrane in a BBSome-dependent manner and undergoes bidirectional IFT .

Example answer:
{"entities": [{"text": "GDP-bound", "type": "ChemicalEntity"}, {"text": "RAB-28", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}, {"text": "BBSome-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Rab6a-GTP , either in solution or bound to artificial liposomes , released BICD2 from an autoinhibited state and promoted robust dynein-dynactin transport .

Example answer:
{"entities": [{"text": "Rab6a-GTP", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "dynein-dynactin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: PI4KIIb depletion caused increased MT1-MMP trafficking to invasive structures at the plasma membrane and was accompanied by reduced colocalization of MT1-MMP with membranes containing the endosomal markers Rab5 and Rab7 but increased localization with the exocytic Rab8 .

## Item biored:test:1065
Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The authors obtained a significant maximum parametric LOD ( logarithm of odds ) score of Z ( max ) = 3.72 on chromosome 8q22 and identified a homozygous missense mutation in the gene MKS3/TMEM67 .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: As previously observed for glioblastomas in Europe , there was a positive association between EGFR amplification and p16 deletion ( p=0.009 ) , whereas there was an inverse association between TP53 mutations and p16 deletion ( p=0.049 ) in glioblastomas in Japan .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Therefore , epigenetic mechanisms , including DNA methylation and histone deacetylation , were indicated to be involved in DOCK8 down-regulation in lung cancer cells .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Negative Selection and Chromosome Instability Induced by Mad2 Overexpression Delay Breast Cancer but Facilitate Oncogene-Independent Outgrowth .

Example answer:
{"entities": [{"text": "Chromosome Instability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Breast Cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thus , the present results suggest that genetic and epigenetic inactivation of DOCK8 is involved in the development and/or progression of lung and other cancers by disturbing such regulations .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "lung and other cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Input:
Sentence: Oncogenic activity of amplified miniature chromosome maintenance 8 in human malignancies .

## Item biored:test:1007
Example input:
Sentence: Object of the present study was to study the influence of SLCO1B1 * 5 , * 15 and * 15+C1007G , a novel haplotype found in a patient with pravastatin-induced myopathy , on the functional properties of OATP1B1 by transient expression systems of HEK293 and HeLa cells using endogenous conjugates and statins as substrates .

Example answer:
{"entities": [{"text": "SLCO1B1", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pravastatin-induced", "type": "ChemicalEntity"}, {"text": "myopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OATP1B1", "type": "GeneOrGeneProduct"}, {"text": "HEK293", "type": "CellLine"}, {"text": "HeLa", "type": "CellLine"}]}

Example input:
Sentence: To determine the pathogenic importance of CB depletions in AD models , we crossed 5 familial AD mutations ( 5XFAD ; Tg ) mice with CB knock-out ( CBKO ) mice and generated a novel line CBKO.5XFAD ( CBKOTg ) mice .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CBKO", "type": "GeneOrGeneProduct"}, {"text": "CBKO.5XFAD", "type": "GeneOrGeneProduct"}, {"text": "CBKOTg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , HFD-induced obese rats are highly sensitized to doxorubicin-induced cardiotoxicity by substantially downregulating cardiac mitochondrial ATP generation , increasing oxidative stress and downregulating the JAK/STAT3 pathway .

Example answer:
{"entities": [{"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "JAK/STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: BACKGROUND/AIMS : The genetic predisposition on the development of nonalcoholic steatohepatitis ( NASH ) has been poorly understood .

Example answer:
{"entities": [{"text": "nonalcoholic steatohepatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Urinary sodium excretion reached signficantly lower values in sgk1 ( +/+ ) mice ( 15 +/- 5 mumol/mg crea ) than in sgk1 ( -/- ) mice ( 35 +/- 5 mumol/mg crea ) and was associated with a significantly higher body weight gain in sgk1 ( +/+ ) compared with sgk1 ( -/- ) mice ( +6.6 +/- 0.7 vs. +4.1 +/- 0.8 g ) .

Example answer:
{"entities": [{"text": "sodium", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "weight gain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , gene-targeted mice lacking SGK1 showed blunted volume retention , yet were not protected against renal fibrosis during experimental nephrotic syndrome .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "volume retention", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the current study , we investigated whether a physiological intervention by feeding 40 % high fat diet ( HFD ) , which induces obesity in male Sprague-Dawley rats ( 250-275 g ) , sensitizes to doxorubicin-induced cardiotoxicity .

Example answer:
{"entities": [{"text": "fat", "type": "ChemicalEntity"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: These data indicate that 11b-HSD1-deficient mice are not protected from metabolic disease or hepatosteatosis in the face of a NAFLD-inducing diet .

## Item biored:test:1066
Example input:
Sentence: Here we investigated the role of Sag/Rbx2 E3 ligase in cellular senescence and immortalization of mouse embryonic fibroblasts ( MEFs ) and report that Sag is required for proper cell proliferation and Kras ( G12D ) -induced immortalization .

Example answer:
{"entities": [{"text": "Sag/Rbx2", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}]}

Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The major histocompatibility complex ( MHC ) on chromosome 6p21 is a key contributor to the genetic basis of systemic lupus erythematosus ( SLE ) .

Example answer:
{"entities": [{"text": "major histocompatibility complex", "type": "GeneOrGeneProduct"}, {"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our study suggests that Alu is a promoting factor for the genomic recombinations in both MLH1 and MSH2 , and the local Alu density may be involved in shaping the deletion pattern .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Previous studies have implicated replication stalling as a mechanism for mtDNA depletion .

Example answer:
{"entities": []}

Example input:
Sentence: However , the chromosomal intervals still contain many genes potentially involved in MCL pathogeny .

Example answer:
{"entities": [{"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The genes that showed consistent correlation between DNA copy number and RNA expression levels are likely to be important in MCL pathology .

Example answer:
{"entities": [{"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we show that simultaneous overexpression of the mitotic checkpoint protein Mad2 with Kras ( G12D ) or Her2 in mammary glands of adult mice results in mitotic checkpoint overactivation and a delay in tumor onset .

Example answer:
{"entities": [{"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "GeneOrGeneProduct"}, {"text": "Her2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: Loss of MLH1 , a major component of DNA MMR , results in tolerance to the cytotoxic effects of methylating agents and persistence of mutagenised cells at high risk of malignant transformation .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cytotoxic", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Miniature chromosome maintenance ( MCM ) proteins play critical roles in DNA replication licensing , initiation and elongation .

## Item biored:test:1074
Example input:
Sentence: Hepatocyte nuclear factor-6 : associations between genetic variability and type II diabetes and between genetic variability and estimates of insulin secretion .

Example answer:
{"entities": [{"text": "Hepatocyte nuclear factor-6", "type": "GeneOrGeneProduct"}, {"text": "type II diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymorphisms in the SLC2A2 ( GLUT2 ) gene are associated with the conversion from impaired glucose tolerance to type 2 diabetes : the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genetic Variation at the Sulfonylurea Receptor , Type 2 Diabetes , and Coronary Heart Disease .

Example answer:
{"entities": [{"text": "Sulfonylurea Receptor", "type": "GeneOrGeneProduct"}, {"text": "Type 2 Diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Coronary Heart Disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our objective was to resequence insulin receptor substrate 2 ( IRS2 ) to identify variants associated with obesity- and diabetes-related traits in Hispanic children .

Example answer:
{"entities": [{"text": "insulin receptor substrate 2", "type": "GeneOrGeneProduct"}, {"text": "IRS2", "type": "GeneOrGeneProduct"}, {"text": "obesity-", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes-related", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results support the conclusion that the 1858C/T allele is the major risk variant for type 1 diabetes in the PTPN22 locus , but they suggest that additional infrequent coding variants at PTPN22 may also contribute to type 1 diabetes risk .

Example answer:
{"entities": [{"text": "1858C/T", "type": "SequenceVariant"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: We then examined them on genomic DNA in six MODY probands without mutations in the MODY1 , MODY3 and MODY4 genes and in 54 patients with late-onset Type II diabetes by combined single strand conformational polymorphism-heteroduplex analysis followed by direct sequencing of identified variants .

Example answer:
{"entities": [{"text": ",", "type": "GeneOrGeneProduct"}, {"text": "II diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The p.A1369S variant was associated with a significantly lower risk of type 2 diabetes ( odds ratio [ OR ] 0.93 ; 95 % CI 0.91 , 0.95 ; P = 1.2 x 10 ( -11 ) ) .

Example answer:
{"entities": [{"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: A Type 2 Diabetes-Associated Functional Regulatory Variant in a Pancreatic Islet Enhancer at the ADCY5 Locus .

## Item biored:test:1056
Example input:
Sentence: Thus , targeting PKCalpha may provide novel therapeutic options in endometrial tumors .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "endometrial tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We sought to define a functional role for the protein kinase C ( PKC ) isoform , PKCalpha , in an established cell model of endometrial adenocarcinoma .

Example answer:
{"entities": [{"text": "protein kinase C", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "endometrial adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A potential downstream signaling pathway involving phosphatidylinositol 3-kinase ( PI3K ) /threonine protein kinase B ( Akt ) /mammalian target of rapamycin ( mTOR ) was identifiedby western blot analysis .

Example answer:
{"entities": [{"text": "phosphatidylinositol 3-kinase", "type": "GeneOrGeneProduct"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "target of rapamycin", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: H3 histamine receptor-mediated activation of protein kinase Calpha inhibits the growth of cholangiocarcinoma in vitro and in vivo .

Example answer:
{"entities": [{"text": "H3 histamine", "type": "GeneOrGeneProduct"}, {"text": "protein kinase Calpha", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : About 10-15 % of adult , and most pediatric , gastrointestinal stromal tumors ( GIST ) lack mutations in KIT , PDGFRA , SDHx , or RAS pathway components ( KRAS , BRAF , NF1 ) .

Example answer:
{"entities": [{"text": "gastrointestinal stromal tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KIT", "type": "GeneOrGeneProduct"}, {"text": "PDGFRA", "type": "GeneOrGeneProduct"}, {"text": "SDHx", "type": "GeneOrGeneProduct"}, {"text": "RAS", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The d-myo-inositol 1,4,5-trisphosphate ( IP ( 3 ) ) /Ca ( 2+ ) /protein kinase C ( PKC ) /mitogen-activated protein kinase pathway regulates cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "d-myo-inositol 1,4,5-trisphosphate", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "( 2+ )", "type": "ChemicalEntity"}, {"text": "kinase C", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "protein kinase", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: BACKGROUND : PIK3CA mutations are expected to be potential therapeutic targets for esophageal squamous cell carcinoma ( ESCC ) .

## Item biored:test:1073
Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Deregulation of these gene products may interfere with the signalling pathways that are involved in MCL tumour development and maintenance .

Example answer:
{"entities": [{"text": "MCL tumour", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The six-nucleotide deletion/insertion variant in the CASP8 promoter region is inversely associated with risk of squamous cell carcinoma of the head and neck .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thus , the present results suggest that genetic and epigenetic inactivation of DOCK8 is involved in the development and/or progression of lung and other cancers by disturbing such regulations .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "lung and other cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Therefore , epigenetic mechanisms , including DNA methylation and histone deacetylation , were indicated to be involved in DOCK8 down-regulation in lung cancer cells .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The genes that showed consistent correlation between DNA copy number and RNA expression levels are likely to be important in MCL pathology .

Example answer:
{"entities": [{"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: As a result , our study showed that copy number increase and overexpression of MCM8 may play critical roles in human cancer development .

## Item biored:test:1088
Example input:
Sentence: METHODS : DNA was collected from 191 patients ( mean age 44+/-18 years , 61 men , 130 women ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Fetal measures from the heavy-exposed fetuses were also compared with measures from a nondrinking group that was representative of normal , uncomplicated pregnancies from our clinics .

Example answer:
{"entities": []}

Example input:
Sentence: DNA was extracted from the blood drawn from 399 prostate cancer patients , 150 BPH patients and 294 healthy community controls .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Serum samples were collected from cirrhotic potential liver transplant patients ( LTx ) with ( n=61 ) and without HCC ( n=78 ) as well as from healthy controls ( HCs ; n=39 ) .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Continuous tracking of individual HSCs and their progeny via time-lapse microscopy elucidated that once GADD45A was expressed , HSCs differentiate into committed progenitors within 29 hours .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Thirty-seven unrelated patients were studied , 18 with LCD and 19 with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: 480 subjects were studied : 240 patients with premature CAD , 240 age and sex matched blood donors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , the main outcome measure was the sequencing of genomic DNA from peripheral blood samples of 41 women with POF and 36 fertile women ( controls ) .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Blood sampling , karyotype , hormonal dosage , ultrasound , and ovarian biopsy were carried out on most patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: MATERIAL AND METHODS Blood samples and placentas from 140 women with GDM and 140 women with healthy pregnancies were collected .

## Item biored:test:1054
Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: There was a marked increase in the number of TUNEL positive cells and nestin positive cells in BCNU-exposed group , but a decreased immunoreactivity to glial fibrillary acidic protein , synaptophysin and transforming growth factor beta1 was observed , indicating a delayed maturation , and melatonin significantly reversed these changes .

Example answer:
{"entities": [{"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}, {"text": "transforming growth factor beta1", "type": "GeneOrGeneProduct"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : The symptoms of infertility observed in the DMC1 homozygote mutation carrier and in both patients with a heterozygous substitution in exon 2 of the MSH5 gene provide indirect evidence of the role of genes involved in meiotic recombination in the regulation of ovarian function .

Example answer:
{"entities": [{"text": "infertility", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These results indicate that ADAM12 actively supports the CSC phenotype in claudin-low breast cancer cells via modulation of the EGFR pathway .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "claudin-low", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that simultaneous overexpression of the mitotic checkpoint protein Mad2 with Kras ( G12D ) or Her2 in mammary glands of adult mice results in mitotic checkpoint overactivation and a delay in tumor onset .

Example answer:
{"entities": [{"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "GeneOrGeneProduct"}, {"text": "Her2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CCK and other GI-hormones/neurotransmitters/growth-factors activate PAK2 via small GTPases ( CDC42/Rac1 ) , PKC and SFK but not cytosolic calcium or PI3K .

Example answer:
{"entities": [{"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "small GTPases", "type": "GeneOrGeneProduct"}, {"text": "CDC42/Rac1", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "SFK", "type": "GeneOrGeneProduct"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We hypothesized that activin and/or GnRH pathways may be modulated by BMP-4 , but neither the activin-stimulated phosphorylation of Smad2/3 nor the GnRH-induced ERK1/2 or cAMP response element-binding phosphorylation were modified .

Example answer:
{"entities": [{"text": "activin", "type": "GeneOrGeneProduct"}, {"text": "GnRH", "type": "GeneOrGeneProduct"}, {"text": "BMP-4", "type": "GeneOrGeneProduct"}, {"text": "activin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "Smad2/3", "type": "GeneOrGeneProduct"}, {"text": "GnRH-induced", "type": "GeneOrGeneProduct"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Upon division , Dpp signaling is extinguished , and Nos is downregulated in one daughter cell , causing it to switch to a differentiating cystoblast ( CB ) .

Example answer:
{"entities": [{"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Our findings reveal a novel role of CenpH in regulating meiotic G2/M transition by acting via the APC/C ( Cdh1 ) -cyclin B1 pathway .

## Item biored:test:1038
Example input:
Sentence: A key hallmark of cancer cells is their altered metabolism , known as Warburg effect .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : More than 3 decades after Jones and Smith ( 1973 ) reported on the devastation caused by alcohol exposure on fetal development , the rates of heavy drinking during pregnancy remain relatively unchanged .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Because intensity of alcohol consumption is associated with poorer fetal outcomes , separate analyses were conducted for the heavy ( average of > or=5 drinks per drinking day ) alcohol consumers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Study-specific associations of 68 single nucleotide polymorphisms ( SNPs ) in 8 alcohol-metabolising genes ( Alcohol Dehydrogenases ( ADHs ) and Aldehyde Dehydrogenases ( ALDHs ) ) with prostate cancer diagnosis and prostate cancer-specific mortality , by grade , were assessed using logistic and Cox regression models , respectively .

Example answer:
{"entities": [{"text": "alcohol-metabolising", "type": "ChemicalEntity"}, {"text": "Alcohol Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ADHs", "type": "GeneOrGeneProduct"}, {"text": "Aldehyde Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ALDHs", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prostate", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Any alcohol consumption postpregnancy recognition among the heavy drinkers resulted in reduced cerebellar growth as well as decreased cranial to body growth in comparison with women who either quit drinking or who were nondrinkers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "reduced cerebellar growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "decreased cranial to body growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: In this study , we investigated the associations of genetic variants in alcohol-metabolising genes with prostate cancer incidence and survival .

Example answer:
{"entities": [{"text": "alcohol-metabolising", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The effects of alcohol consumption on prostate cancer incidence and survival remain unclear , potentially due to methodological limitations of observational studies .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results suggest that alcohol consumption is unlikely to affect prostate cancer incidence , but it may influence disease progression .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found little evidence that variants in alcohol metabolising genes were associated with prostate cancer diagnosis .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alcohol consumption and prostate cancer incidence and progression : A Mendelian randomisation study .

Example answer:
{"entities": [{"text": "Alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In this study , we investigated in the human breast cancer cell line MCF-7 , whether a similar exposure to ethanol at concentrations ranging up to peak blood levels in heavy drinkers would increase malignant progression .

## Item biored:test:1040
Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Prolonged CsA exposure aggravated renal damage , without clear changes on the traditional markers , but with changes in serums TGF- b and IL-7 , TBARs clearance , and kidney TGF-b and mTOR .

Example answer:
{"entities": [{"text": "CsA", "type": "ChemicalEntity"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF- b", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "TBARs", "type": "ChemicalEntity"}, {"text": "TGF-b", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: There was a marked increase in the number of TUNEL positive cells and nestin positive cells in BCNU-exposed group , but a decreased immunoreactivity to glial fibrillary acidic protein , synaptophysin and transforming growth factor beta1 was observed , indicating a delayed maturation , and melatonin significantly reversed these changes .

Example answer:
{"entities": [{"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}, {"text": "transforming growth factor beta1", "type": "GeneOrGeneProduct"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Instead , ETO-induced OCT4A was concomitant with activation of AMPK , a key component of metabolic stress and autophagy regulation .

Example answer:
{"entities": [{"text": "ETO-induced", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Any alcohol consumption postpregnancy recognition among the heavy drinkers resulted in reduced cerebellar growth as well as decreased cranial to body growth in comparison with women who either quit drinking or who were nondrinkers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "reduced cerebellar growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "decreased cranial to body growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Study-specific associations of 68 single nucleotide polymorphisms ( SNPs ) in 8 alcohol-metabolising genes ( Alcohol Dehydrogenases ( ADHs ) and Aldehyde Dehydrogenases ( ALDHs ) ) with prostate cancer diagnosis and prostate cancer-specific mortality , by grade , were assessed using logistic and Cox regression models , respectively .

Example answer:
{"entities": [{"text": "alcohol-metabolising", "type": "ChemicalEntity"}, {"text": "Alcohol Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ADHs", "type": "GeneOrGeneProduct"}, {"text": "Aldehyde Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ALDHs", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prostate", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SOX2 and NANOG expression did not change following ETO treatment suggesting a dissociation of OCT4A from its pluripotency function .

Example answer:
{"entities": [{"text": "SOX2", "type": "GeneOrGeneProduct"}, {"text": "NANOG", "type": "GeneOrGeneProduct"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Together , these findings imply that OCT4A induction following DNA damage in PA-1 cells , performs a cell stress , rather than self-renewal , function by moderating the expression of p21Cip1 , which alongside AMPK helps to then regulate autophagy .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We found little evidence that variants in alcohol metabolising genes were associated with prostate cancer diagnosis .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Long-term ( 4-week ) exposure to 25 mM ethanol upregulated the Oct4 and Nanog proteins , as well as the malignancy marker Ceacam6 .

## Item biored:test:1078
Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results support the conclusion that the 1858C/T allele is the major risk variant for type 1 diabetes in the PTPN22 locus , but they suggest that additional infrequent coding variants at PTPN22 may also contribute to type 1 diabetes risk .

Example answer:
{"entities": [{"text": "1858C/T", "type": "SequenceVariant"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our aim was to study the associations of individual single nucleotide polymorphisms and haplotypes with adiposity , glucose metabolism , and the risk of type 2 diabetes ( T2D ) .

Example answer:
{"entities": [{"text": "adiposity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: AIMS : Individuals with both diabetes mellitus ( DM ) and the Haptoglobin ( Hp ) 2-2 genotype are at increased risk of cardiovascular disease .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Haptoglobin", "type": "GeneOrGeneProduct"}, {"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "cardiovascular disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With the exception of SLC2A2 , other genes were not associated with the risk of type 2 diabetes .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymorphisms in the SLC2A2 ( GLUT2 ) gene are associated with the conversion from impaired glucose tolerance to type 2 diabetes : the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The risk for type 2 diabetes in the AA genotype carriers was increased in the control group ( 5.56 [ 1.78-17.39 ] , P = 0.003 ) but not in the intervention group .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The p.A1369S variant was associated with a significantly lower risk of type 2 diabetes ( odds ratio [ OR ] 0.93 ; 95 % CI 0.91 , 0.95 ; P = 1.2 x 10 ( -11 ) ) .

Example answer:
{"entities": [{"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We demonstrated that type 2 diabetes risk alleles are associated with decreased ADCY5 expression in human islets and examined candidate variants for regulatory function .

## Item biored:test:1067
Example input:
Sentence: A homozygous deletion of the DOCK8 ( dedicator of cytokinesis 8 ) locus at chromosome 9p24 was found in a lung cancer cell line by array-CGH analysis .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "dedicator of cytokinesis 8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Mal de Meleda ( MDM ) is palmoplantar erythrokeratoderma with an autosomal recessive inheritance and is caused by a mutation in the gene encoding SLURP-1 ( lymphocyte antigen 6/urokinase-type plasminogen activator receptor related protein-1 ) .

Example answer:
{"entities": [{"text": "Mal de Meleda", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "palmoplantar erythrokeratoderma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}, {"text": "lymphocyte antigen", "type": "GeneOrGeneProduct"}, {"text": "plasminogen activator receptor related protein-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Loss of MLH1 , a major component of DNA MMR , results in tolerance to the cytotoxic effects of methylating agents and persistence of mutagenised cells at high risk of malignant transformation .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cytotoxic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The authors obtained a significant maximum parametric LOD ( logarithm of odds ) score of Z ( max ) = 3.72 on chromosome 8q22 and identified a homozygous missense mutation in the gene MKS3/TMEM67 .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The six-nucleotide deletion/insertion variant in the CASP8 promoter region is inversely associated with risk of squamous cell carcinoma of the head and neck .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Therefore , epigenetic mechanisms , including DNA methylation and histone deacetylation , were indicated to be involved in DOCK8 down-regulation in lung cancer cells .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The genes that showed consistent correlation between DNA copy number and RNA expression levels are likely to be important in MCL pathology .

Example answer:
{"entities": [{"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: MCM8 , one of the MCM proteins playing a critical role in DNA repairing and recombination , was found to have overexpression and increased DNA copy number in a variety of human malignancies .

## Item biored:test:1051
Example input:
Sentence: ZnSO ( 4 ) pretreatment counteracted BCNU-induced inhibition of GR and depletion of GSH and resulted in significant reduction in the levels of MDA and TNFalpha as well as the activity of caspase-3 .

Example answer:
{"entities": [{"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our results demonstrate that both cisplatin and paclitaxel cause early mitochondrial impairment with loss of membrane potential and induction of autophagic vacuoles in neurons .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "mitochondrial impairment", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , MT induction halts BCNU-induced hippocampal toxicity as it prevented GR inhibition and GSH depletion and counteracted the increased levels of TNFalpha , MDA and caspase-3 activity with subsequent preservation of cognition .

Example answer:
{"entities": [{"text": "MT", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These data suggest that exposure of animals to BCNU during pregnancy leads to delayed maturation of offspring cerebellum and melatonin protects the cerebellum against the effects of BCNU .

Example answer:
{"entities": [{"text": "BCNU", "type": "ChemicalEntity"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study was designed to evaluate the alterations in offspring rat cerebellum induced by maternal exposure to carmustine- [ 1,3-bis ( 2-chloroethyl ) -1-nitrosoure ] ( BCNU ) and to investigate the effects of exogenous melatonin upon cerebellar BCNU-induced cortical dysplasia , using histological and biochemical analyses .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "carmustine-", "type": "ChemicalEntity"}, {"text": "1,3-bis ( 2-chloroethyl ) -1-nitrosoure", "type": "ChemicalEntity"}, {"text": "BCNU", "type": "ChemicalEntity"}, {"text": "melatonin", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "cortical dysplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Upon division , Dpp signaling is extinguished , and Nos is downregulated in one daughter cell , causing it to switch to a differentiating cystoblast ( CB ) .

Example answer:
{"entities": [{"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: There was a marked increase in the number of TUNEL positive cells and nestin positive cells in BCNU-exposed group , but a decreased immunoreactivity to glial fibrillary acidic protein , synaptophysin and transforming growth factor beta1 was observed , indicating a delayed maturation , and melatonin significantly reversed these changes .

Example answer:
{"entities": [{"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}, {"text": "transforming growth factor beta1", "type": "GeneOrGeneProduct"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Input:
Sentence: Depletion of CenpH by morpholino injection decreased cyclin B1 levels , resulting in attenuation of maturation-promoting factor ( MPF ) activation , and severely compromised meiotic resumption .

## Item biored:test:1084
Example input:
Sentence: Associated corticosteroid therapy and twin gestations appear to be predisposing factors .

Example answer:
{"entities": [{"text": "corticosteroid", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND : Focal dermal hypoplasia ( FDH ) ( OMIM 305600 ) is an X-linked dominant disorder of ecto-mesodermal development .

Example answer:
{"entities": [{"text": "Focal dermal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 305600", "type": "DiseaseOrPhenotypicFeature"}, {"text": "X-linked dominant disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : In type 2 diabetic patients , cases who developed CAD were compared retrospectively with controls that did not .

Example answer:
{"entities": [{"text": "type 2 diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: AIMS : Individuals with both diabetes mellitus ( DM ) and the Haptoglobin ( Hp ) 2-2 genotype are at increased risk of cardiovascular disease .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Haptoglobin", "type": "GeneOrGeneProduct"}, {"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "cardiovascular disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Maternal diabetes significantly increased the levels of CHOP , calnexin , phosphorylated ( p ) -eIF2a , p-PERK , and p-IRE1a ; triggered XBP1 mRNA splicing ; and enhanced ER chaperone gene expression in WT embryos .

Example answer:
{"entities": [{"text": "Maternal diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: They were ascertained between 1967 and 2004 , in 190 maternity hospitals of the ECLAMC ( Estudio Colaborativo Latinoamericano de Malformaciones Congenitas ) network , in 102 cities of all 10 South American countries .

Example answer:
{"entities": []}

Example input:
Sentence: BACKGROUND : Sudden infant death syndrome ( SIDS ) constitutes the most frequent cause of death in the postperinatal period in Germany .

Example answer:
{"entities": [{"text": "Sudden infant death syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SIDS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Arg124Cys and Arg555Trp appear to be the predominant mutations causing LCD and GCD , respectively , in the population studied .

Example answer:
{"entities": [{"text": "Arg124Cys", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Thirty-seven unrelated patients were studied , 18 with LCD and 19 with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The diagnosis of LCD or GCD was made on the basis of clinical and/or histopathological evaluation .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: BACKGROUND Gestational diabetes mellitus ( GDM ) is common all over the world .

## Item biored:test:1052
Example input:
Sentence: Moreover , using RNA interference with small inhibitory RNAs for Sp1 , Sp3 , and Sp4 , we observed that curcumin-dependent inhibition of nuclear factor kappaB ( NF-kappaB ) -dependent genes , such as bcl-2 , survivin , and cyclin D1 , was also due , in part , to loss of Sp proteins .

Example answer:
{"entities": [{"text": "Sp1", "type": "GeneOrGeneProduct"}, {"text": "Sp3", "type": "GeneOrGeneProduct"}, {"text": "Sp4", "type": "GeneOrGeneProduct"}, {"text": "curcumin-dependent", "type": "ChemicalEntity"}, {"text": "nuclear factor kappaB", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "survivin", "type": "GeneOrGeneProduct"}, {"text": "cyclin D1", "type": "GeneOrGeneProduct"}, {"text": "Sp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CCK and other GI-hormones/neurotransmitters/growth-factors activate PAK2 via small GTPases ( CDC42/Rac1 ) , PKC and SFK but not cytosolic calcium or PI3K .

Example answer:
{"entities": [{"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "small GTPases", "type": "GeneOrGeneProduct"}, {"text": "CDC42/Rac1", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "SFK", "type": "GeneOrGeneProduct"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Coenzyme Q10 significantly compensated deficits in the antioxidant defense mechanisms ( reduced glutathione level and superoxide dismutase activity ) , suppressed lipid peroxidation , decreased the elevations of tumor necrosis factor-alpha , nitric oxide and platinum ion concentration , and attenuated the reductions of selenium and zinc ions in renal tissue resulted from cisplatin administration .

Example answer:
{"entities": [{"text": "Coenzyme Q10", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "nitric oxide", "type": "ChemicalEntity"}, {"text": "platinum", "type": "ChemicalEntity"}, {"text": "selenium", "type": "ChemicalEntity"}, {"text": "zinc", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Upon division , Dpp signaling is extinguished , and Nos is downregulated in one daughter cell , causing it to switch to a differentiating cystoblast ( CB ) .

Example answer:
{"entities": [{"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Importantly , this is the first experimental evidence that removal of CB from amyloid precursor protein/presenilin transgenic mice aggravates AD pathogenesis , suggesting that CB has a critical role in AD pathogenesis .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "amyloid precursor", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Calbindin-D28k ( CB ) , one of the major calcium-binding and buffering proteins , has a critical role in preventing a neuronal death as well as maintaining calcium homeostasis .

Example answer:
{"entities": [{"text": "Calbindin-D28k", "type": "GeneOrGeneProduct"}, {"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "neuronal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "calcium", "type": "ChemicalEntity"}]}

Input:
Sentence: CenpH protects cyclin B1 from destruction by competing with the action of APC/C ( Cdh1 ) Impaired G2/M transition after CenpH depletion could be rescued by expression of exogenous cyclin B1 .

## Item biored:test:884
Example input:
Sentence: In response to IL-2 , these CD25 ( + ) Tfh cells increased expression of costimulatory molecules ICOS or OX40 , upregulated transcription factor cMaf , produced cytokines IL-21 , IL-17 , and IL-10 , and raised the levels of antiapoptotic protein Bcl2 .

Example answer:
{"entities": [{"text": "IL-2", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "ICOS", "type": "GeneOrGeneProduct"}, {"text": "OX40", "type": "GeneOrGeneProduct"}, {"text": "cMaf", "type": "GeneOrGeneProduct"}, {"text": "IL-21", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "Bcl2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Given VIP 's role as an anti-inflammatory mediator , we hypothesized that VIP ( -/- ) mice would exhibit enhanced inflammatory mediator expression after cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: TSPO was up-regulated in Iba1 ( + ) cells from brains of patients with ICH and in CD11b ( + ) CD45 ( int ) cells from mice subjected to collagenase-induced ICH .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "Iba1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD11b", "type": "GeneOrGeneProduct"}, {"text": "CD45", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "collagenase-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: The data suggest that in VIP ( -/- ) mice with bladder inflammation , inflammatory mediators are increased above that observed in WT with CYP .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Exaggerated expression of inflammatory mediators in vasoactive intestinal polypeptide knockout ( VIP-/- ) mice with cyclophosphamide ( CYP ) -induced cystitis .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vasoactive intestinal polypeptide", "type": "GeneOrGeneProduct"}, {"text": "VIP-/-", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CYP", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A mouse inflammatory cytokine and receptor RT2 profiler array was used to determine regulated transcripts in the urinary bladder of wild type ( WT ) and VIP ( -/- ) mice with or without CYP-induced cystitis ( 150 mg/kg ; i.p .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CYP-induced", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A mouse model of BLM-induced PF was established , and Bach1 siRNA ( 1x109 pfu ) was administered to the mice via the tail vein .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "BLM-induced", "type": "ChemicalEntity"}, {"text": "PF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: This effect was dependent on the production of IL-10 from DCs , as neither DCs isolated from IL-10-/- mice nor IL-10-neutralized DCs generated tolerogenic DCs .

Example answer:
{"entities": [{"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "IL-10-/-", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "IL-10-neutralized", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: In vivo induction of airway IL-1b , IL-4 , IL-5 , IL-6 , IL-12 ( p40 ) , IFN-g , CCL2 , CCL5 , CCL3 , CXCL1 , IP-10/CXCL10 , IL-22 , MIG/CXCL9 and MIF were dependent on Mavs expression in mice .

## Item biored:test:1072
Example input:
Sentence: EPO/EPOR-modulated cell cycle mediators included Cdc25a , Btg3 , Cyclin-d2 , p27-kip1 , Cyclin-g2 and CyclinB1-IP-1 .

Example answer:
{"entities": [{"text": "EPO/EPOR-modulated", "type": "GeneOrGeneProduct"}, {"text": "Cdc25a", "type": "GeneOrGeneProduct"}, {"text": "Btg3", "type": "GeneOrGeneProduct"}, {"text": "Cyclin-d2", "type": "GeneOrGeneProduct"}, {"text": "p27-kip1", "type": "GeneOrGeneProduct"}, {"text": "Cyclin-g2", "type": "GeneOrGeneProduct"}, {"text": "CyclinB1-IP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We recently reported that phosphoinositide 3-kinase ( PI3K ) /protein kinase B ( Akt ) mediates transcriptional regulation and activation of bone morphogenetic protein ( BMP ) -2 signaling by nuclear factor ( NF ) -kappaB in bone metastatic prostate cancer cells .

Example answer:
{"entities": [{"text": "phosphoinositide 3-kinase ( PI3K ) /protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "bone morphogenetic protein ( BMP ) -2", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor ( NF ) -kappaB", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Caspase 8 ( CASP8 ) is an apoptosis-related cysteine peptidase involved in the death receptor pathway and likely in the mitochondrial pathway .

Example answer:
{"entities": [{"text": "Caspase 8", "type": "GeneOrGeneProduct"}, {"text": "CASP8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Therefore , epigenetic mechanisms , including DNA methylation and histone deacetylation , were indicated to be involved in DOCK8 down-regulation in lung cancer cells .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The d-myo-inositol 1,4,5-trisphosphate ( IP ( 3 ) ) /Ca ( 2+ ) /protein kinase C ( PKC ) /mitogen-activated protein kinase pathway regulates cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "d-myo-inositol 1,4,5-trisphosphate", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "( 2+ )", "type": "ChemicalEntity"}, {"text": "kinase C", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "protein kinase", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We utilized intracellular phospho-flow cytometry to investigate the relationship between Myc and BCR signaling in pre-malignant B cells .

Example answer:
{"entities": [{"text": "Myc", "type": "GeneOrGeneProduct"}, {"text": "BCR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that simultaneous overexpression of the mitotic checkpoint protein Mad2 with Kras ( G12D ) or Her2 in mammary glands of adult mice results in mitotic checkpoint overactivation and a delay in tumor onset .

Example answer:
{"entities": [{"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "GeneOrGeneProduct"}, {"text": "Her2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In Mz-ChA-1 cells stimulated with ( R ) - ( alpha ) - ( - ) -methylhistamine dihydrobromide ( RAMH ) , we measured ( a ) cell growth , ( b ) IP ( 3 ) and cyclic AMP levels , and ( c ) phosphorylation of PKC and mitogen-activated protein kinase isoforms .

Example answer:
{"entities": [{"text": "Mz-ChA-1", "type": "CellLine"}, {"text": "( R ) - ( alpha ) - ( - ) -methylhistamine dihydrobromide", "type": "ChemicalEntity"}, {"text": "RAMH", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The cyclin D1/MCM8 interaction is required for Rb phosphorylation and S-phase entry in cancer cells .

## Item biored:test:1071
Example input:
Sentence: Melanocortin-4 receptor activation inhibits c-Jun N-terminal kinase activity and promotes insulin signaling .

Example answer:
{"entities": [{"text": "Melanocortin-4 receptor", "type": "GeneOrGeneProduct"}, {"text": "c-Jun N-terminal kinase", "type": "GeneOrGeneProduct"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Following knockdown of PKCalpha , Mz-ChA-1 cells were stimulated with RAMH before evaluating cell growth and extracellular signal-regulated kinase ( ERK ) -1/2 phosphorylation .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Mz-ChA-1", "type": "CellLine"}, {"text": "RAMH", "type": "ChemicalEntity"}, {"text": "extracellular signal-regulated kinase ( ERK ) -1/2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: NDP-MSH augmented insulin-stimulated AKT phosphorylation in vitro .

Example answer:
{"entities": [{"text": "NDP-MSH", "type": "ChemicalEntity"}, {"text": "insulin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Investigations of the underlying mechanisms revealed that BDNF activated Akt and preserved phosphorylation of mammalian target of rapamycin and Bad without affecting p38 mitogen-activated protein kinase and extracellular regulated protein kinase pathways .

Example answer:
{"entities": [{"text": "mammalian target of", "type": "GeneOrGeneProduct"}, {"text": "p38 mitogen-activated protein", "type": "GeneOrGeneProduct"}, {"text": "extracellular regulated protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , CBKOTg mice reduced levels of phosphorylated mitogen-activated protein kinase ( extracellular signal-regulated kinase ) 1/2 and cAMP response element-binding protein at Ser-133 and synaptic molecules such as N-methyl-D-aspartate receptor 1 ( NMDA receptor 1 ) , NMDA receptor 2A , PSD-95 and synaptophysin in the subiculum compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}, {"text": "extracellular signal-regulated kinase ) 1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding protein", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-D-aspartate receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 2A", "type": "GeneOrGeneProduct"}, {"text": "PSD-95", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The melanocortin agonist NDP-MSH dose-dependently inhibited JNK activity in HEK293 cells stably expressing the human MC4R ; effects were reversed by melanocortin receptor antagonist .

Example answer:
{"entities": [{"text": "melanocortin", "type": "GeneOrGeneProduct"}, {"text": "NDP-MSH", "type": "ChemicalEntity"}, {"text": "JNK", "type": "GeneOrGeneProduct"}, {"text": "HEK293", "type": "CellLine"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "MC4R", "type": "GeneOrGeneProduct"}, {"text": "melanocortin receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We hypothesized that activin and/or GnRH pathways may be modulated by BMP-4 , but neither the activin-stimulated phosphorylation of Smad2/3 nor the GnRH-induced ERK1/2 or cAMP response element-binding phosphorylation were modified .

Example answer:
{"entities": [{"text": "activin", "type": "GeneOrGeneProduct"}, {"text": "GnRH", "type": "GeneOrGeneProduct"}, {"text": "BMP-4", "type": "GeneOrGeneProduct"}, {"text": "activin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "Smad2/3", "type": "GeneOrGeneProduct"}, {"text": "GnRH-induced", "type": "GeneOrGeneProduct"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Smad1/5 phosphorylation induced by BMP-4 , indicating activation of BMP signalling , was the same whether BMP-4 was used alone or combined with activin+/-GnRH .

Example answer:
{"entities": [{"text": "Smad1/5", "type": "GeneOrGeneProduct"}, {"text": "BMP-4", "type": "GeneOrGeneProduct"}, {"text": "BMP", "type": "GeneOrGeneProduct"}, {"text": "activin+/-GnRH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In Mz-ChA-1 cells stimulated with ( R ) - ( alpha ) - ( - ) -methylhistamine dihydrobromide ( RAMH ) , we measured ( a ) cell growth , ( b ) IP ( 3 ) and cyclic AMP levels , and ( c ) phosphorylation of PKC and mitogen-activated protein kinase isoforms .

Example answer:
{"entities": [{"text": "Mz-ChA-1", "type": "CellLine"}, {"text": "( R ) - ( alpha ) - ( - ) -methylhistamine dihydrobromide", "type": "ChemicalEntity"}, {"text": "RAMH", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The melanocortin receptor type 4 ( MC4R ) modulates insulin signaling via effects on c-Jun N-terminal kinase ( JNK ) .

Example answer:
{"entities": [{"text": "melanocortin receptor type 4", "type": "GeneOrGeneProduct"}, {"text": "MC4R", "type": "GeneOrGeneProduct"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "c-Jun N-terminal kinase", "type": "GeneOrGeneProduct"}, {"text": "JNK", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: MCM8 bound cyclin D1 and activated Rb protein phosphorylation by cyclin-dependent kinase 4 in vitro and in vivo .

## Item biored:test:1069
Example input:
Sentence: We also examined the inhibitor of RNASEL ( ABCE1 ) for variation associated with prostate cancer risk .

Example answer:
{"entities": [{"text": "RNASEL", "type": "GeneOrGeneProduct"}, {"text": "ABCE1", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The six-nucleotide deletion/insertion variant in the CASP8 promoter region is inversely associated with risk of squamous cell carcinoma of the head and neck .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , a 38 % remission rate has been recently reported in refractory MCL treated with temsirolimus , a mTOR inhibitor.Here we had the opportunity to study a case of refractory MCL who had tumor regression two months after temsirolimus treatment , and a progression-free survival of 10 months .

Example answer:
{"entities": [{"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "temsirolimus", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : To evaluate the association of variation in genes involved in immune response , including IL10 , production and detoxification of reactive oxygen species , and repair of oxidative DNA damage with risk of recurrence after surgery for localized prostate cancer .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: IMPACT : This study supports that genetic variation in immune response and oxidation influence prostate cancer recurrence risk and suggests genetic variation in these pathways may inform prognosis .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The molecular mechanisms involved in prostate cancer ( PC ) metastasis and bone remodeling are poorly understood .

Example answer:
{"entities": [{"text": "prostate cancer ( PC ) metastasis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The expression of MLPH in primary prostate tumors was significantly lower in those with the G compared with the T allele and correlated significantly with AR protein .

Example answer:
{"entities": [{"text": "MLPH", "type": "GeneOrGeneProduct"}, {"text": "prostate tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Variation in IL10 , CRP , GSTP1 , IL1B , and NOS2 was associated with prostate cancer recurrence independent of pathologic prognostic factors .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Increased expression of MCM8 in prostate cancer is associated with cancer recurrence .

## Item biored:test:1024
Example input:
Sentence: Gankyrin binds to Src homology 2 domain-containing protein tyrosine phosphatase-1 ( SHP-1 ) , mainly expressed in liver non-parenchymal cells , resulting in phosphorylation and activation of signal transducer and activator of transcription 3 ( STAT3 ) .

Example answer:
{"entities": [{"text": "Gankyrin", "type": "GeneOrGeneProduct"}, {"text": "Src homology 2 domain-containing protein tyrosine phosphatase-1", "type": "GeneOrGeneProduct"}, {"text": "SHP-1", "type": "GeneOrGeneProduct"}, {"text": "signal transducer and activator of transcription 3", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A similar clathrin adaptor protein , epsinR , exists in humans .

Example answer:
{"entities": [{"text": "clathrin", "type": "ChemicalEntity"}, {"text": "epsinR", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: To investigate this question , we have developed in vitro motility assays with purified DDB and BICD2 's membrane vesicle partner , the GTPase Rab6a .

Example answer:
{"entities": [{"text": "DDB", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "GTPase Rab6a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PAK2 was activated by some pancreatic growth-factors [ EGF , PDGF , bFGF ] , by secretagogues activating phospholipase-C ( PLC ) [ CCK , carbachol , bombesin ] and by post-receptor stimulants activating PKC [ TPA ] , but not agents only mobilizing cellular calcium or increasing cyclic AMP .

Example answer:
{"entities": [{"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "pancreatic growth-factors", "type": "GeneOrGeneProduct"}, {"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "PDGF", "type": "GeneOrGeneProduct"}, {"text": "bFGF", "type": "GeneOrGeneProduct"}, {"text": "phospholipase-C", "type": "GeneOrGeneProduct"}, {"text": "PLC", "type": "GeneOrGeneProduct"}, {"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "carbachol", "type": "ChemicalEntity"}, {"text": "bombesin", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "TPA", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: We used rat pancreatic acini to explore the ability of GI-hormones/neurotransmitters/growth-factors to activate Group-I-PAKs and the signaling cascades involved .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "Group-I-PAKs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The endosomal sorting complex required for transport ( ESCRT ) -III mediates membrane fission in fundamental cellular processes , including cytokinesis .

Example answer:
{"entities": [{"text": "endosomal sorting complex required for transport ( ESCRT ) -III", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Top canonical pathways identified by Ingenuity Pathway Analysis ( IPA ) included `` Clathrin-mediated Endocytosis Signaling '' ( p = 5.14x10-4 ) , `` Virus Entry via Endocytic Pathways '' ( p = 6.15x 10-4 ) , and `` High Mobility Group-Box 1 ( HMGB1 ) Signaling '' ( p = 6.15x10-4 ) .

Example answer:
{"entities": [{"text": "Clathrin-mediated", "type": "GeneOrGeneProduct"}, {"text": "High Mobility Group-Box 1", "type": "GeneOrGeneProduct"}, {"text": "HMGB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CCK and other GI-hormones/neurotransmitters/growth-factors activate PAK2 via small GTPases ( CDC42/Rac1 ) , PKC and SFK but not cytosolic calcium or PI3K .

Example answer:
{"entities": [{"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "small GTPases", "type": "GeneOrGeneProduct"}, {"text": "CDC42/Rac1", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "SFK", "type": "GeneOrGeneProduct"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Phosphatidylinositol ( PI ) 3-kinase is an important enzyme in the early insulin signaling cascade and plays a key role in insulin-mediated glucose transport .

Example answer:
{"entities": [{"text": "Phosphatidylinositol ( PI ) 3-kinase", "type": "GeneOrGeneProduct"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "insulin-mediated", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: Lastly , overexpression of Ent3p , which is a clathrin adapter protein involved in protein transport between the Golgi and the vacuole , causes alpha-syn to redistribute from the plasma membrane into cytoplasmic vesicular structures .

Example answer:
{"entities": [{"text": "Ent3p", "type": "GeneOrGeneProduct"}, {"text": "clathrin", "type": "ChemicalEntity"}, {"text": "alpha-syn", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The type II phosphatidylinositol 4-kinase ( PI4KII ) enzymes synthesize the lipid phosphatidylinositol 4-phosphate ( PI ( 4 ) P ) , which has been detected at the Golgi complex and endosomal compartments and recruits clathrin adaptors .

## Item biored:test:1077
Example input:
Sentence: Rab6a-GTP , either in solution or bound to artificial liposomes , released BICD2 from an autoinhibited state and promoted robust dynein-dynactin transport .

Example answer:
{"entities": [{"text": "Rab6a-GTP", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "dynein-dynactin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Besides several 'anonymous genes ' , we also identified various fully annotated genes , whose gene products are involved in cyclic adenosine monophosphate-regulated pathways ( PRKACB ) , DNA damage repair , maintenance of chromosome stability and prevention of rereplication ( ATM , ERCC5 , FBXO5 ) , energy metabolism ( such as genes that are involved in the synthesis of proteins encoded by the mitochondrial genome ) and signal transduction ( ARHGAP29 ) .

Example answer:
{"entities": [{"text": "cyclic adenosine", "type": "ChemicalEntity"}, {"text": "PRKACB", "type": "GeneOrGeneProduct"}, {"text": "ATM", "type": "GeneOrGeneProduct"}, {"text": "ERCC5", "type": "GeneOrGeneProduct"}, {"text": "FBXO5", "type": "GeneOrGeneProduct"}, {"text": "ARHGAP29", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Aberrant caveolin-1-mediated Smad signaling and proliferation identified by analysis of adenine 474 deletion mutation ( c.474delA ) in patient fibroblasts : a new perspective on the mechanism of pulmonary hypertension .

Example answer:
{"entities": [{"text": "caveolin-1-mediated", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "adenine 474 deletion", "type": "SequenceVariant"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pulmonary hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , CBKOTg mice reduced levels of phosphorylated mitogen-activated protein kinase ( extracellular signal-regulated kinase ) 1/2 and cAMP response element-binding protein at Ser-133 and synaptic molecules such as N-methyl-D-aspartate receptor 1 ( NMDA receptor 1 ) , NMDA receptor 2A , PSD-95 and synaptophysin in the subiculum compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}, {"text": "extracellular signal-regulated kinase ) 1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding protein", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-D-aspartate receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 2A", "type": "GeneOrGeneProduct"}, {"text": "PSD-95", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The d-myo-inositol 1,4,5-trisphosphate ( IP ( 3 ) ) /Ca ( 2+ ) /protein kinase C ( PKC ) /mitogen-activated protein kinase pathway regulates cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "d-myo-inositol 1,4,5-trisphosphate", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "( 2+ )", "type": "ChemicalEntity"}, {"text": "kinase C", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "protein kinase", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The melanocortin receptor type 4 ( MC4R ) modulates insulin signaling via effects on c-Jun N-terminal kinase ( JNK ) .

Example answer:
{"entities": [{"text": "melanocortin receptor type 4", "type": "GeneOrGeneProduct"}, {"text": "MC4R", "type": "GeneOrGeneProduct"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "c-Jun N-terminal kinase", "type": "GeneOrGeneProduct"}, {"text": "JNK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We used rat pancreatic acini to explore the ability of GI-hormones/neurotransmitters/growth-factors to activate Group-I-PAKs and the signaling cascades involved .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "Group-I-PAKs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Gastrointestinal hormones/neurotransmitters and growth factors can activate P21 activated kinase 2 in pancreatic acinar cells by novel mechanisms .

Example answer:
{"entities": [{"text": "Gastrointestinal", "type": "ChemicalEntity"}, {"text": "P21 activated kinase 2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A common missense variant in the gene encoding a component of the sulfonylurea receptor ( ABCC8 p.A1369S ) promotes closure of the target channel of sulfonylurea therapy and is associated with increased insulin secretion , thus mimicking the effects of sulfonylurea therapy .

Example answer:
{"entities": [{"text": "sulfonylurea receptor", "type": "GeneOrGeneProduct"}, {"text": "ABCC8", "type": "GeneOrGeneProduct"}, {"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "sulfonylurea", "type": "ChemicalEntity"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PAK2 was activated by some pancreatic growth-factors [ EGF , PDGF , bFGF ] , by secretagogues activating phospholipase-C ( PLC ) [ CCK , carbachol , bombesin ] and by post-receptor stimulants activating PKC [ TPA ] , but not agents only mobilizing cellular calcium or increasing cyclic AMP .

Example answer:
{"entities": [{"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "pancreatic growth-factors", "type": "GeneOrGeneProduct"}, {"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "PDGF", "type": "GeneOrGeneProduct"}, {"text": "bFGF", "type": "GeneOrGeneProduct"}, {"text": "phospholipase-C", "type": "GeneOrGeneProduct"}, {"text": "PLC", "type": "GeneOrGeneProduct"}, {"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "carbachol", "type": "ChemicalEntity"}, {"text": "bombesin", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "TPA", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}]}

Input:
Sentence: Adenylate cyclase 5 catalyzes the production of cyclic AMP , which is a second messenger molecule involved in cell signaling and pancreatic b-cell insulin secretion .

## Item biored:test:885
Example input:
Sentence: TSPO was up-regulated in Iba1 ( + ) cells from brains of patients with ICH and in CD11b ( + ) CD45 ( int ) cells from mice subjected to collagenase-induced ICH .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "Iba1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD11b", "type": "GeneOrGeneProduct"}, {"text": "CD45", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "collagenase-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: The transforming growth factor ( TGF ) -b-inducible early gene-1 ( TIEG1 ) plays a crucial role in modulating cell apoptosis and proliferation in a number of diseases , including pancreatic cancer , leukaemia and osteoporosis .

Example answer:
{"entities": [{"text": "transforming growth factor ( TGF ) -b-inducible early gene-1", "type": "GeneOrGeneProduct"}, {"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "pancreatic cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "osteoporosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : We examined the genetic association of the promoter insertion/deletion ( indel ) in IRF5 gene with systemic lupus erythematosus ( SLE ) in distinct populations and assessed its role in gene expression .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interestingly , the differential expression of miRNA in mice also corroborated with the miRNA expression in human PC cell lines and tissue samples ; ectopic expression of Let-7b in CD18/HPAF and Capan1 cells resulted in the downregulation of KRAS and MSST1 expression .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Let-7b", "type": "GeneOrGeneProduct"}, {"text": "CD18/HPAF", "type": "CellLine"}, {"text": "Capan1", "type": "CellLine"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "MSST1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Improved cardiac function and less scar formation were observed in TIEG1 KO mice , and we also observed the altered expression of phosphatase and tensin homolog ( Pten ) , Akt and Bcl-2/Bax , as well as vascular endothelial growth factor ( VEGF ) .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "Pten", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2/Bax", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further , expression of miRNA biosynthetic machinery including Dicer , Exportin-5 , TRKRA , and TARBP2 were downregulated , while DGCR8 and Ago2 were upregulated in KC mice .

Example answer:
{"entities": [{"text": "Dicer", "type": "GeneOrGeneProduct"}, {"text": "Exportin-5", "type": "GeneOrGeneProduct"}, {"text": "TRKRA", "type": "GeneOrGeneProduct"}, {"text": "TARBP2", "type": "GeneOrGeneProduct"}, {"text": "DGCR8", "type": "GeneOrGeneProduct"}, {"text": "Ago2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Gene expression analysis revealed that rs10954213 exerted the greatest influence on IRF5 transcript levels .

Example answer:
{"entities": [{"text": "rs10954213", "type": "SequenceVariant"}, {"text": "IRF5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Promoter insertion/deletion in the IRF5 gene is highly associated with susceptibility to systemic lupus erythematosus in distinct populations , but exerts a modest effect on gene expression in peripheral blood mononuclear cells .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , we determined in a syngeneic sarcoma mouse model that radiation up-regulates IRF3 , IFNb , and the T cell chemokines CCL2 and CCL5 in the tumor microenvironment , which are associated with activation and increased infiltration of Th1/Tc1 T cells in the tumor microenvironment .

Example answer:
{"entities": [{"text": "sarcoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "IRF3", "type": "GeneOrGeneProduct"}, {"text": "IFNb", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Loss of Trif expression in mice altered the RSV induction of IL-1b , IL-5 , CXCL12 , MIF , LIF , CXCL12 and IFN-g. Silencing of retinoic acid-inducible gene-1 ( RIG-I ) expression in A549 cells had a greater impact on RSV-inducible cytokines than melanoma differentiation-associated protein 5 ( MDA5 ) and laboratory of genetics and physiology 2 ( LGP2 ) , and Trif expression .

## Item biored:test:1081
Example input:
Sentence: CONCLUSION : The novel finding of this study is the association of the mutant allele ( A1359 ) with a decrease of resistin , leptin and interleukin-6 secondary to weight loss .

Example answer:
{"entities": [{"text": "A1359", "type": "SequenceVariant"}, {"text": "resistin", "type": "GeneOrGeneProduct"}, {"text": "leptin", "type": "GeneOrGeneProduct"}, {"text": "interleukin-6", "type": "GeneOrGeneProduct"}, {"text": "weight loss", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , rs6232 , encoding the amino acid exchange N221D , influences insulin sensitivity and glucose homeostasis .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "N221D", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We recently showed that long-term weight reduction changes the gene expression profile of adipose tissue in overweight individuals with impaired glucose tolerance ( IGT ) .

Example answer:
{"entities": [{"text": "overweight", "type": "DiseaseOrPhenotypicFeature"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A common missense variant in the gene encoding a component of the sulfonylurea receptor ( ABCC8 p.A1369S ) promotes closure of the target channel of sulfonylurea therapy and is associated with increased insulin secretion , thus mimicking the effects of sulfonylurea therapy .

Example answer:
{"entities": [{"text": "sulfonylurea receptor", "type": "GeneOrGeneProduct"}, {"text": "ABCC8", "type": "GeneOrGeneProduct"}, {"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "sulfonylurea", "type": "ChemicalEntity"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Focused transcriptomics revealed that myocyte-specific enhancer factor 2C ( MEF2C ) and myogenic factor 5 ( MYF5 ) expression was inhibited by high glucose levels , and endoribonuclease-prepared small interfering RNA-mediated combined inhibition of those transcription factors phenocopied the glycolytic shift that was observed in high glucose conditions .

Example answer:
{"entities": [{"text": "myocyte-specific enhancer factor 2C", "type": "GeneOrGeneProduct"}, {"text": "MEF2C", "type": "GeneOrGeneProduct"}, {"text": "myogenic factor 5", "type": "GeneOrGeneProduct"}, {"text": "MYF5", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : A heterozygous in-frame deletion Y248del ( c.742_744delTAC ) was identified in one GH-secreting adenoma patient .

Example answer:
{"entities": [{"text": "Y248del", "type": "SequenceVariant"}, {"text": "c.742_744delTAC", "type": "SequenceVariant"}, {"text": "GH-secreting adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Input:
Sentence: Homozygous deletion of the orthologous enhancer region in 832/13 cells resulted in a 64 % reduction in expression level of Adcy5 , but not adjacent gene Sec22a , and a 39 % reduction in insulin secretion .

## Item biored:test:1076
Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: Focused transcriptomics revealed that myocyte-specific enhancer factor 2C ( MEF2C ) and myogenic factor 5 ( MYF5 ) expression was inhibited by high glucose levels , and endoribonuclease-prepared small interfering RNA-mediated combined inhibition of those transcription factors phenocopied the glycolytic shift that was observed in high glucose conditions .

Example answer:
{"entities": [{"text": "myocyte-specific enhancer factor 2C", "type": "GeneOrGeneProduct"}, {"text": "MEF2C", "type": "GeneOrGeneProduct"}, {"text": "myogenic factor 5", "type": "GeneOrGeneProduct"}, {"text": "MYF5", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: None of the SNPs or indels were associated with diabetes-related traits or accounted for a previously identified quantitative trait locus on chromosome 13 for fasting serum glucose .

Example answer:
{"entities": [{"text": "diabetes-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: The p.A1369S variant was associated with a significantly lower risk of type 2 diabetes ( odds ratio [ OR ] 0.93 ; 95 % CI 0.91 , 0.95 ; P = 1.2 x 10 ( -11 ) ) .

Example answer:
{"entities": [{"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We then examined them on genomic DNA in six MODY probands without mutations in the MODY1 , MODY3 and MODY4 genes and in 54 patients with late-onset Type II diabetes by combined single strand conformational polymorphism-heteroduplex analysis followed by direct sequencing of identified variants .

Example answer:
{"entities": [{"text": ",", "type": "GeneOrGeneProduct"}, {"text": "II diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymorphisms in the SLC2A2 ( GLUT2 ) gene are associated with the conversion from impaired glucose tolerance to type 2 diabetes : the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Variants associated with type 2 diabetes and fasting glucose levels reside in introns of ADCY5 , a gene that encodes adenylate cyclase 5 .

## Item biored:test:1018
Example input:
Sentence: Study-specific associations of 68 single nucleotide polymorphisms ( SNPs ) in 8 alcohol-metabolising genes ( Alcohol Dehydrogenases ( ADHs ) and Aldehyde Dehydrogenases ( ALDHs ) ) with prostate cancer diagnosis and prostate cancer-specific mortality , by grade , were assessed using logistic and Cox regression models , respectively .

Example answer:
{"entities": [{"text": "alcohol-metabolising", "type": "ChemicalEntity"}, {"text": "Alcohol Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ADHs", "type": "GeneOrGeneProduct"}, {"text": "Aldehyde Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ALDHs", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prostate", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: p16ink4a , the inducer of terminal senescence , underwent autophagic sequestration in the cytoplasm of ETO-treated cells , allowing alternative cell fates .

Example answer:
{"entities": [{"text": "p16ink4a", "type": "GeneOrGeneProduct"}, {"text": "ETO-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: We found little evidence that variants in alcohol metabolising genes were associated with prostate cancer diagnosis .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Instead , ETO-induced OCT4A was concomitant with activation of AMPK , a key component of metabolic stress and autophagy regulation .

Example answer:
{"entities": [{"text": "ETO-induced", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: Together , these findings imply that OCT4A induction following DNA damage in PA-1 cells , performs a cell stress , rather than self-renewal , function by moderating the expression of p21Cip1 , which alongside AMPK helps to then regulate autophagy .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The autophagy inhibitor 3-methyladenine was used to assess the effect of autophagy on ROS production and apoptosis under hypoxic conditions .

Example answer:
{"entities": [{"text": "3-methyladenine", "type": "ChemicalEntity"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "hypoxic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Accordingly , failure of autophagy was accompanied by an accumulation of p16ink4a , nuclear disintegration , and loss of cell recovery .

Example answer:
{"entities": [{"text": "p16ink4a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , inhibition of autophagy led to increased ROS production and a higher percentage of apoptotic cells in the two cell types .

Example answer:
{"entities": [{"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results demonstrated that hypoxia induced apoptosis , increased ROS production , and promoted autophagy in a time-dependent manner relative to that observed under normoxia .

Example answer:
{"entities": [{"text": "hypoxia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Input:
Sentence: Alcohol increased Atg12-5 , LC3B-I and -II , and ULK1 S555 phosphorylation , suggesting increased autophagy , while markers of apoptosis ( cleaved caspase-3 and -9 , and PARP ) were unchanged .

## Item biored:test:1082
Example input:
Sentence: Polymorphisms in the SLC2A2 ( GLUT2 ) gene are associated with the conversion from impaired glucose tolerance to type 2 diabetes : the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A recent addition to the list of widely confirmed type 1 diabetes risk loci is the PTPN22 gene encoding a lymphoid-specific phosphatase ( Lyp ) .

Example answer:
{"entities": [{"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "lymphoid-specific phosphatase", "type": "GeneOrGeneProduct"}, {"text": "Lyp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results support the conclusion that the 1858C/T allele is the major risk variant for type 1 diabetes in the PTPN22 locus , but they suggest that additional infrequent coding variants at PTPN22 may also contribute to type 1 diabetes risk .

Example answer:
{"entities": [{"text": "1858C/T", "type": "SequenceVariant"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The risk for type 2 diabetes in the AA genotype carriers was increased in the control group ( 5.56 [ 1.78-17.39 ] , P = 0.003 ) but not in the intervention group .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , rs6232 , encoding the amino acid exchange N221D , influences insulin sensitivity and glucose homeostasis .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "N221D", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The p.A1369S variant was associated with a significantly lower risk of type 2 diabetes ( odds ratio [ OR ] 0.93 ; 95 % CI 0.91 , 0.95 ; P = 1.2 x 10 ( -11 ) ) .

Example answer:
{"entities": [{"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Together , these data suggest that rs11708067-A risk allele contributes to type 2 diabetes by disrupting an islet enhancer , which results in reduced ADCY5 expression and impaired insulin secretion .
