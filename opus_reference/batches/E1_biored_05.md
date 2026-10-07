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

## Item biored:test:236
Example input:
Sentence: Exonic and intronic segments , 5 ' and 3 ' flanking regions of IRS2 ( 14.5 kb ) , were bidirectionally sequenced for single nucleotide polymorphism ( SNP ) discovery in 934 Hispanic children using 3730XL DNA Sequencers .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : This study showed that SNPs rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , but not rs7535263 , rs1410996 , or rs2274700 , in CFH were significantly associated with wet AMD in a mainland Han Chinese population .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "rs7535263", "type": "SequenceVariant"}, {"text": "rs1410996", "type": "SequenceVariant"}, {"text": "rs2274700", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: DNA samples of 760 anonymous AJ subjects were submitted for analysis , subsequently detecting six individuals heterozygous for the GALT deletion mutation , giving a carrier frequency of 1 in 127 ( 0.79 % ) .

Example answer:
{"entities": [{"text": "GALT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In Southern blot analysis , from the signal densities of the hybridized bands and their similarities to those of exons 2 and 3 in our previous quantitative study , we found that exon 1beta was homozygously deleted in four cases , hemizygously deleted in five cases and not deleted in one case .

Example answer:
{"entities": []}

Example input:
Sentence: V311fs is an 8-bp nucleotide ( TTAAATGG ) deletion in exon 5 .

Example answer:
{"entities": [{"text": "V311fs", "type": "SequenceVariant"}, {"text": "8-bp nucleotide ( TTAAATGG ) deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Recently , an unusual mutation was characterized causing a 5.5 kb deletion , with a relatively high carrier rate in subjects of Ashkenazi Jewish ( AJ ) descent .

Example answer:
{"entities": [{"text": "5.5 kb deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: A 28 bp variable number of tandem repeats ( VNTR ) , a G/C single nucleotide polymorphism ( SNP ) , and a deletion of 6 bp at position 1494 were studied .

Example answer:
{"entities": [{"text": "28 bp variable number of tandem repeats", "type": "SequenceVariant"}, {"text": "G/C", "type": "SequenceVariant"}, {"text": "deletion of 6 bp at position 1494", "type": "SequenceVariant"}]}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Input:
Sentence: A high carrier frequency for the 15-bp deletion in exon 7 may exist in the Singapore population .

## Item biored:test:124
Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Three BRCA1 abnormalities - 5382insC , C61G , and 4153delA - accounted for 51 % , 20 % , and 11 % of the identified mutations , respectively ..

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5382insC", "type": "SequenceVariant"}, {"text": "C61G", "type": "SequenceVariant"}, {"text": "4153delA", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutations of TP53 and dysfunction of the Brca1 and/or Brca2 tumor-suppressor proteins have been implicated in the molecular pathogenesis of a large fraction of OSCs , but frequent somatic mutations in other well-established tumor-suppressor genes have not been identified .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "Brca1", "type": "GeneOrGeneProduct"}, {"text": "Brca2", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Founder mutations in the BRCA1 gene in Polish families with breast-ovarian cancer .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The single family with a BRCA2 mutation had the breast-ovarian cancer syndrome .

Example answer:
{"entities": [{"text": "BRCA2", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: As these studies concerned sporadic cancer cases , we investigated whether N372H and another common variant located in the 5'-untranslated region ( 203G > A ) of the BRCA2 gene modify breast or ovarian cancer risk in BRCA1 mutation carriers .

## Item biored:test:166
Example input:
Sentence: Sequencing of the GJB2 gene showed that the child was heterozygous for a novel nucleotide change , c.263C > T , in exon 2 , leading to a substitution of alanine for valine at position 88 ( p.Ala88Val ) .

Example answer:
{"entities": [{"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "c.263C > T", "type": "SequenceVariant"}, {"text": "alanine for valine at position 88", "type": "SequenceVariant"}, {"text": "p.Ala88Val", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : A heterozygous germline T to C transition in exon 10 of the TSHR gene ( c.1358T -- > C ) resulting in the substitution of methionine ( ATG ) by threonine ( ACG ) at codon 453 ( p.M453T ) was identified in the father and his two children .

Example answer:
{"entities": [{"text": "T to C", "type": "SequenceVariant"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}, {"text": "c.1358T -- > C", "type": "SequenceVariant"}, {"text": "methionine ( ATG ) by threonine ( ACG ) at codon 453", "type": "SequenceVariant"}, {"text": "p.M453T", "type": "SequenceVariant"}]}

Example input:
Sentence: Seven novel single-nucleotide polymorphisms ( SNPs ) were also found , of which a change of leucine 269 to phenylalanine ( Leu269Phe ) was found in 12 of 18 patients with the Arg555Trp mutation .

Example answer:
{"entities": [{"text": "leucine 269 to phenylalanine", "type": "SequenceVariant"}, {"text": "Leu269Phe", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Arg555Trp", "type": "SequenceVariant"}]}

Example input:
Sentence: A common single nucleotide polymorphism ( SNP ) , G472A , codes for a Val158Met substitution and results in a fourfold down regulation of enzyme activity .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "Val158Met", "type": "SequenceVariant"}]}

Example input:
Sentence: The two transversions resulted in the substitution of a stop codon for glutamine at codon 298 ( p.Q298X ) and a missense mutation at codon 358 , tyrosine to histidine ( p.Y358H ) .

Example answer:
{"entities": [{"text": "stop codon for glutamine at codon 298", "type": "SequenceVariant"}, {"text": "p.Q298X", "type": "SequenceVariant"}, {"text": "codon 358 , tyrosine to histidine", "type": "SequenceVariant"}, {"text": "p.Y358H", "type": "SequenceVariant"}]}

Example input:
Sentence: The heterozygous c.973G > A transition in exon 9 resulted in a substitution of lysine for glutamic acid at amino acid 325 ( E325K ) in the second calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "c.973G > A", "type": "SequenceVariant"}, {"text": "lysine for glutamic acid at amino acid 325", "type": "SequenceVariant"}, {"text": "E325K", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The patient 's GR gene had a heterozygotic mutation ( G -- > A ) at nucleotide position 2141 ( exon 8 ) , which resulted in substitution of arginine by glutamine at amino acid position 714 in the ligand-binding domain ( LBD ) of the GR alpha .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "( G -- > A ) at nucleotide position 2141", "type": "SequenceVariant"}, {"text": "arginine by glutamine at amino acid position 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Gene polymorphism resulting in the substitution of glutamine with lysine at residue 223 in the carbohydrate recognition domain of SP-A2 increases susceptibility to meningococcal disease , as well as the risk of death .

Example answer:
{"entities": [{"text": "glutamine with lysine at residue 223", "type": "SequenceVariant"}, {"text": "carbohydrate", "type": "ChemicalEntity"}, {"text": "SP-A2", "type": "GeneOrGeneProduct"}, {"text": "meningococcal disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The genetic polymorphism rs1052133 , which leads to substitution of the amino acid at codon 326 from Ser to Cys , shows functional differences , namely a decrease in enzyme activity in hOGG1-Cys326 .

Example answer:
{"entities": [{"text": "rs1052133", "type": "SequenceVariant"}, {"text": "326 from Ser to Cys", "type": "SequenceVariant"}, {"text": "hOGG1-Cys326", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this report the distribution of the exonic G/A single nucleotide polymorphism ( SNP ) in purine nucleoside phosphorylase ( PNP ) gene , resulting in the amino acid substitution serine to glycine at position 51 ( G51S ) , was investigated in a large population of AD patients ( n=321 ) and non-demented control ( n=208 ) .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "purine nucleoside phosphorylase", "type": "GeneOrGeneProduct"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "serine to glycine at position 51", "type": "SequenceVariant"}, {"text": "G51S", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: There are two known polymorphisms in exon 11 of the DBP gene resulting in amino acid variants : GAT -- > GAG substitution replaces aspartic acid by glutamic acid in codon 416 ; and ACG -- > AAG substitution in codon 420 leads to an exchange of threonine for lysine .

## Item biored:test:225
Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study aimed to identify mutations in a Chinese pedigree with MEN1 .

Example answer:
{"entities": [{"text": "MEN1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The goal of this study was to define the identities , origins and frequencies of TMC1 mutations in an expanded cohort of 557 large Pakistani families segregating recessive deafness .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "recessive deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A missense mutation in BCOR was described in a family with Lenz microphthalmia syndrome , a phenotype showing substantial overlapping features with that described in the two cousins .

Example answer:
{"entities": [{"text": "BCOR", "type": "GeneOrGeneProduct"}, {"text": "Lenz microphthalmia syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , our study suggests that p.R246Q mutation is common amongst patients with SRD5A2 gene defect from the Northern states of India .

Example answer:
{"entities": [{"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In our present study , a third Chinese family with this mutation was identified , suggesting that this mutation is a prevalent CYP17 mutation in the Chinese population .

Example answer:
{"entities": [{"text": "CYP17", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We identified and characterized a PABPN1 mutation in a Taiwanese family with OPMD .

Example answer:
{"entities": [{"text": "PABPN1", "type": "GeneOrGeneProduct"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Mutations found in the PTCH1 gene and neighboring repetitive sequences may have contributed to the development of the studied BCCs .

Example answer:
{"entities": [{"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The aim of this study was to investigate the spectrum of mutations in this gene in BCD patients from Singapore , and to characterize their phenotype .

## Item biored:test:239
Example input:
Sentence: A key hallmark of cancer cells is their altered metabolism , known as Warburg effect .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Together , these findings imply that OCT4A induction following DNA damage in PA-1 cells , performs a cell stress , rather than self-renewal , function by moderating the expression of p21Cip1 , which alongside AMPK helps to then regulate autophagy .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA damage and repair were evaluated by alkaline single cell gel electrophoresis ( comet assay ) assisted by DNA repair enzymes : endonuclease III ( Nth ) and formamidopyrimidine-DNA glycosylase ( Fpg ) , preferentially recognizing oxidized DNA bases .

Example answer:
{"entities": [{"text": "endonuclease III", "type": "GeneOrGeneProduct"}, {"text": "Nth", "type": "GeneOrGeneProduct"}, {"text": "formamidopyrimidine-DNA glycosylase", "type": "GeneOrGeneProduct"}, {"text": "Fpg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both the mutagens ' sensitivity and the efficacy of DNA repair may be affected by variation in several genes , including DNA repair genes .

Example answer:
{"entities": []}

Example input:
Sentence: BACKGROUND : To evaluate the association of variation in genes involved in immune response , including IL10 , production and detoxification of reactive oxygen species , and repair of oxidative DNA damage with risk of recurrence after surgery for localized prostate cancer .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both can be involved in the repair of oxidative DNA lesions , which can contribute to stomach cancer .

Example answer:
{"entities": [{"text": "stomach cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Of particular interest are genes involved in defense against reactive oxygen species ( ROS ) because ROS are thought to cause DNA damage and contribute to the pathogenesis of cancer .

Example answer:
{"entities": [{"text": "reactive oxygen species", "type": "ChemicalEntity"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA-damage response gene GADD45A induces differentiation in hematopoietic stem cells without inhibiting cell cycle or survival .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In general , GADD45A provides cellular stability by either arresting the cell cycle progression until DNA damage is repaired or , in cases of fatal damage , by inducing apoptosis .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The cell 's susceptibility to mutagens and its ability to repair DNA lesions are important for cancer induction , promotion and progression .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The response of the cell to DNA damage and its ability to maintain genomic stability by DNA repair are crucial in preventing cancer initiation and progression .

## Item biored:test:240
Example input:
Sentence: A meta-analysis of previous and our present study revealed that this polymorphism is positively associated with adenocarcinoma , although suggestive associations were also found for squamous- and small-cell lung cancers .

Example answer:
{"entities": [{"text": "adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "squamous- and small-cell lung cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The metrics from DNA damage and repair study were correlated with the genotypes of common polymorphisms of the hOGG1 and RAD51 genes : a G -- > C transversion at 1245 position of the hOGG1 gene producing a Ser -- > Cys substitution at the codon 326 ( the Ser326Cys polymorphism ) and a G -- > C substitution at position 135 ( 5'-untranslated region ) of the RAD51 gene ( the G135C polymorphism ) .

Example answer:
{"entities": [{"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "RAD51", "type": "GeneOrGeneProduct"}, {"text": "G -- > C transversion at 1245 position", "type": "SequenceVariant"}, {"text": "Ser -- > Cys substitution at the codon 326", "type": "SequenceVariant"}, {"text": "Ser326Cys", "type": "SequenceVariant"}, {"text": "G -- > C substitution at position 135", "type": "SequenceVariant"}, {"text": "G135C", "type": "SequenceVariant"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the present study we explored the effect of three polymorphisms of the TS gene on overall and progression- free survival of colorectal cancer ( CRC ) patients subjected to 5FU chemotherapy .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "5FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: We did not observe any correlation between the Ser1245Cys polymorphism of the hOGG1 gene and gastric cancer , including subjects with impaired DNA repair and/or high levels of endogenous oxidative DNA lesions .

Example answer:
{"entities": [{"text": "Ser1245Cys", "type": "SequenceVariant"}, {"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both the mutagens ' sensitivity and the efficacy of DNA repair may be affected by variation in several genes , including DNA repair genes .

Example answer:
{"entities": []}

Example input:
Sentence: We observed a strong association between gastric cancer occurrence , impaired DNA repair in human lymphocytes and the G/C genotype of the G135C polymorphism of the RAD51 gene .

Example answer:
{"entities": [{"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "G/C", "type": "SequenceVariant"}, {"text": "G135C", "type": "SequenceVariant"}, {"text": "RAD51", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: It has been shown that DNA repair is reduced in patients with systemic lupus erythematosus ( SLE ) and that the X-ray repair cross-complementing ( XRCC1 ) Arg399Gln ( rs25487 ) polymorphism may contribute to DNA repair .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "X-ray repair cross-complementing", "type": "GeneOrGeneProduct"}, {"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "rs25487", "type": "SequenceVariant"}]}

Example input:
Sentence: The p53 mutation spectrum , presenting a high level of CC to TT mutations , shows that the UV component of sunlight is the major risk factor and modulated DNA repair by immunosuppressive drug treatment may be significant in the skin carcinogenesis of RTRs .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "CC to TT", "type": "SequenceVariant"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA damage and repair in gastric cancer -- a correlation with the hOGG1 and RAD51 genes polymorphisms .

Example answer:
{"entities": [{"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "RAD51", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Therefore , polymorphism of DNA repair genes may affect the process of carcinogenesis .

## Item biored:test:204
Example input:
Sentence: We also demonstrate that the A118D SEA domain mutation causes an intra-molecular structural imbalance that impairs matriptase-2 activation .

Example answer:
{"entities": [{"text": "A118D", "type": "SequenceVariant"}, {"text": "matriptase-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: We also tested whether a G/A substitution at the G-395A site affected the transcription level in vitro through the dual-luciferase reporter assay .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "G-395A", "type": "SequenceVariant"}]}

Example input:
Sentence: The two transversions resulted in the substitution of a stop codon for glutamine at codon 298 ( p.Q298X ) and a missense mutation at codon 358 , tyrosine to histidine ( p.Y358H ) .

Example answer:
{"entities": [{"text": "stop codon for glutamine at codon 298", "type": "SequenceVariant"}, {"text": "p.Q298X", "type": "SequenceVariant"}, {"text": "codon 358 , tyrosine to histidine", "type": "SequenceVariant"}, {"text": "p.Y358H", "type": "SequenceVariant"}]}

Example input:
Sentence: However , in transient transfection assays , the E333D TRbeta mutant exhibited impaired transcriptional regulation on two distinct positively regulated thyroid response elements ( F2- and DR4-TREs ) as well as on the negatively regulated human TSHalpha promoter .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "TSHalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: RNA sequencing was performed to identify global gene expression changes after ADAM12 knockdown .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Analysis of PTPN22 transcripts from a subject heterozygous for this variant indicated that it interfered with normal mRNA splicing , resulting in a premature termination codon after exon 17 .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: To determine whether c.609+28_610-16del allele-derived transcripts were subject to nonsense-mediated mRNA decay ( NMD ) , patient fibroblasts were incubated with the protein synthesis inhibitor anisomycin .

Example answer:
{"entities": [{"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "anisomycin", "type": "ChemicalEntity"}]}

Input:
Sentence: After transfection and inhibition of transcription with actinomycin D , analysis of mRNA turnover failed to reveal differences in mRNA stability between A118 and G118 alleles , indicating a defect in transcription or mRNA maturation .

## Item biored:test:244
Example input:
Sentence: The result of PCR associated with restriction fragment length polymorphism analysis also suggested that this mutation is heterozygous .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: TS genotyping methods were polymerase chain reaction ( PCR ) for VNTR and PCR , followed by restriction length fragment polymorphism ( PCR-RFLP ) for SNP and ins/del 6 bp .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "ins/del 6 bp", "type": "SequenceVariant"}]}

Example input:
Sentence: Genomic DNA was isolated from the venous blood leukocytes of 322 unrelated patients with schizophrenia , 156 patients with depression , 300 patients with heroin addiction , and 300 healthy unrelated individuals .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The genotypes of the polymorphism were determined by restriction fragment length polymorphism PCR .

Example answer:
{"entities": []}

Example input:
Sentence: DNA from peripheral nuclear blood cells was genotyped for 5-HTTLPR using standard polymerase chain reaction methods.A significant group effect was observed only on memory function tasks ( p = 0.04 ) but not on reaction times ( p = 0.61 ) or attention/executive functioning ( p = 0.59 ) .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genotyping was determined by the polymerase chain reaction-restriction fragment length polymorphism ( PCR-RFLP ) technique .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Genotypes were determined in DNA from peripheral blood lymphocytes of 150 breast cancer patients and 150 age-matched women ( controls ) by restriction fragment length polymorphism and allele-specific PCR .

## Item biored:test:194
Example input:
Sentence: There was also an excess of MB in warfarin users vs nonusers with ICH ( OR , 2.7 ; 95 % CI , 1.6-4.4 ; P < 0.001 ) but none in warfarin users with IS/TIA ( OR , 1.3 ; 95 % CI , 0.9-1.7 ; P=0.33 ; P difference=0.01 ) .

Example answer:
{"entities": [{"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Semiquantitative assessment of the density of NOX4 colabeling with lectin-stained retinal ECs was determined by immunolabeling of retinal cryosections from P18 pups in OIR or in RA .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "lectin-stained", "type": "GeneOrGeneProduct"}, {"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Studies of additional cases yielded a second set of data that , in combination with the first set , confirmed a weak association of UP III SNP7 in VUR ( P= 0.036 adjusted for both subsets of cases vs. controls ) .

Example answer:
{"entities": [{"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cox regression analysis of IHC scores found that only phospho AKT ( pAKT ) was a significant independent predictor of worse PFS .

Example answer:
{"entities": [{"text": "AKT", "type": "GeneOrGeneProduct"}, {"text": "pAKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : In a pooled analysis of 1460 ICH and 3817 IS/TIA , MB were more frequent in ICH vs IS/TIA in all treatment groups , but the excess increased from 2.8 ( odds ratio ; range , 2.3-3.5 ) in nonantithrombotic users to 5.7 ( range , 3.4-9.7 ) in antiplatelet users and 8.0 ( range , 3.5-17.8 ) in warfarin users ( P difference=0.01 ) .

Example answer:
{"entities": [{"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: ( CCTTT ) 14 , which has been reported to have a higher activity in a reporter-construct , was significantly more abundant in POAG patients , while ( CCTTT ) 10 and ( CCTTT ) 13 were less common .

Example answer:
{"entities": [{"text": "( CCTTT ) 14", "type": "SequenceVariant"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "( CCTTT ) 10", "type": "SequenceVariant"}, {"text": "( CCTTT ) 13", "type": "SequenceVariant"}]}

Example input:
Sentence: PbtO ( 2 ) decreased from 51.7 +/- 4.5 mm Hg sem to 33.8 +/- 5.2 mm Hg sem in the NTG group and from 38.6 +/- 6.1 mm Hg sem to 25.4 +/- 2.0 mm Hg sem in the NTG + NIMO groups , respectively .

Example answer:
{"entities": [{"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Input:
Sentence: RESULTS : Densitometry showed no significant difference regarding GAP43-ir in the IML between Pilo , CHX+Pilo , and control groups .

## Item biored:test:217
Example input:
Sentence: Atorvastatin protects against contrast-induced nephropathy via anti-apoptosis by the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Histological examination showed that losartan could prevent tubular atrophy , interstitial infiltration and fibrosis in ADR nephropathy .

Example answer:
{"entities": [{"text": "losartan", "type": "ChemicalEntity"}, {"text": "atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADR", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , Hsp90beta inhibition-mediated renal improvements also accompanied the reduction of renal oxidative stress .

Example answer:
{"entities": [{"text": "Hsp90beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Also , histopathological renal tissue damage mediated by cisplatin was ameliorated by coenzyme Q10 treatment .

Example answer:
{"entities": [{"text": "renal tissue damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "coenzyme Q10", "type": "ChemicalEntity"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , we establish the unilateral ureteric obstruction ( UUO ) or folic acid ( FA ) -induced mice renal interstitial fibrosis in vivo and the transforming growth factor ( TGF ) -beta1-stimulated human proximal tubular epithelial cell ( HK-2 ) model in vitro .

Example answer:
{"entities": [{"text": "unilateral ureteric obstruction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "UUO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "folic acid", "type": "ChemicalEntity"}, {"text": "FA", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "renal interstitial fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor ( TGF )", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK-2", "type": "CellLine"}]}

Example input:
Sentence: Histopathological examination revealed severe renal damage such as proteinaceous casts in tubuli and tubular expansion in the kidney of control rats , while an improvement of the damage was seen in antithrombin-treated rats .

Example answer:
{"entities": [{"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "antithrombin-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results of the present study suggested that atorvastatin protected against contrast-induced renal tubular cell apoptosis through the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced renal tubular cell apoptosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our results show that treatment with Sal can ameliorate tubular injury and deposition of the extracellular matrix ( ECM ) components ( including collagen SH and collagen I ) .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "tubular injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "collagen SH", "type": "GeneOrGeneProduct"}, {"text": "collagen I", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Erdosteine caused a marked reduction in the extent of tubular damage .

## Item biored:test:198
Example input:
Sentence: Specific knockdown of OPRM1 confers L-asparaginase resistance , validating our genome-wide retroviral shRNA library screening data .

Example answer:
{"entities": [{"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : The mother and daughter were each heterozygous for PPARG nonsense mutation Y355X , whose protein product in vitro was transcriptionally inactive with no dominant-negative activity against the wild-type receptor .

Example answer:
{"entities": [{"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "Y355X", "type": "SequenceVariant"}]}

Example input:
Sentence: OPMD is caused by a short trinucleotide repeat expansion encoding an expanded polyalanine tract in the polyadenylate binding-protein nuclear 1 ( PABPN1 ) gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "polyalanine", "type": "ChemicalEntity"}, {"text": "polyadenylate binding-protein nuclear 1", "type": "GeneOrGeneProduct"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Catechol-O-methyltransferase ( COMT ) gene variants : possible association of the Val158Met variant with opiate addiction in Hispanic women .

Example answer:
{"entities": [{"text": "Catechol-O-methyltransferase", "type": "GeneOrGeneProduct"}, {"text": "COMT", "type": "GeneOrGeneProduct"}, {"text": "Val158Met", "type": "SequenceVariant"}, {"text": "opiate addiction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The human mu opiate receptor ( h mu OR1 ) shares 95 % amino acid identity with the rat sequence .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "mu opiate receptor", "type": "GeneOrGeneProduct"}, {"text": "h mu OR1", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: Thus , our study demonstrates for the first time , a novel OPRM1-mediated mechanism for L-asparaginase resistance in ALL , and identifies OPRM1 as a functional biomarker for defining high-risk subpopulations and for the detection of evolving resistant clones .

Example answer:
{"entities": [{"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also demonstrate that the A118D SEA domain mutation causes an intra-molecular structural imbalance that impairs matriptase-2 activation .

Example answer:
{"entities": [{"text": "A118D", "type": "SequenceVariant"}, {"text": "matriptase-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genome-wide loss-of-function genetic screening identifies opioid receptor u1 as a key regulator of L-asparaginase resistance in pediatric acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "opioid receptor u1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "acute lymphoblastic leukemia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Allelic expression imbalance of human mu opioid receptor ( OPRM1 ) caused by variant A118G .

## Item biored:test:215
Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Recent studies indicate that genetic ablation of mouse uroplakin ( UP ) III gene , which encodes a 47 kD urothelial-specific integral membrane protein forming urothelial plaques , causes VUR and hydronephrosis .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "uroplakin ( UP ) III", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Given VIP 's role as an anti-inflammatory mediator , we hypothesized that VIP ( -/- ) mice would exhibit enhanced inflammatory mediator expression after cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Coenzyme Q10 treatment ameliorates acute cisplatin nephrotoxicity in mice .

Example answer:
{"entities": [{"text": "Coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "nephrotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: In vitro , the Vps2/Vps24 subunits of ESCRT-III formed side-by-side filaments with Snf7 and inhibited further polymerization , but the growth inhibition was alleviated by the addition of Vps4 and ATP .

Example answer:
{"entities": [{"text": "Vps2/Vps24", "type": "GeneOrGeneProduct"}, {"text": "ESCRT-III", "type": "GeneOrGeneProduct"}, {"text": "Snf7", "type": "GeneOrGeneProduct"}, {"text": "Vps4", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Also , histopathological renal tissue damage mediated by cisplatin was ameliorated by coenzyme Q10 treatment .

Example answer:
{"entities": [{"text": "renal tissue damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "coenzyme Q10", "type": "ChemicalEntity"}]}

Example input:
Sentence: It was concluded that coenzyme Q10 represents a potential therapeutic option to protect against acute cisplatin nephrotoxicity commonly encountered in clinical practice .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "nephrotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The results of the present study suggested that atorvastatin protected against contrast-induced renal tubular cell apoptosis through the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced renal tubular cell apoptosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Atorvastatin protects against contrast-induced nephropathy via anti-apoptosis by the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Erdosteine showed histopathological protection against VCM-induced nephrotoxicity .

## Item biored:test:209
Example input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Rats were exposed to BCNU on embryonic day 15 and melatonin was given until delivery .

Example answer:
{"entities": [{"text": "Rats", "type": "OrganismTaxon"}, {"text": "BCNU", "type": "ChemicalEntity"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : 24 Rats were divided into 4 groups and received following treatments for 4 weeks ; Corn oil ( control ) , diazinon ( 15mg/kg per day , orally ) and crocin ( 12.5 and 25mg/kg per day , intraperitoneally ) in combination with diazinon ( 15 mg/kg ) .

Example answer:
{"entities": [{"text": "Rats", "type": "OrganismTaxon"}, {"text": "Corn oil", "type": "ChemicalEntity"}, {"text": "diazinon", "type": "ChemicalEntity"}, {"text": "crocin", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : Male adult Wistar rats ( n = 90 and 260-290 g ) were divided into 1 , control ; 2 and 3 , crocins ( 15 and 30 mg/kg ) ; 4 , STZ ; 5 and 6 , STZ + crocins ( 15 and 30 mg/kg ) groups .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "crocins", "type": "ChemicalEntity"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here we successfully constructed the desminopathy rat model , evaluated with conventional stains , containing hematoxylin and eosin ( HE ) , Gomori Trichrome ( MGT ) , ( PAS ) , red oil ( ORO ) , NADH-TR , SDH staining and immunohistochemistry .

Example answer:
{"entities": [{"text": "desminopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: Pregnant Wistar rats were assigned to five groups : intact-control , saline-control , melatonin-treated , BCNU-exposed and BCNU-exposed plus melatonin .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "melatonin-treated", "type": "ChemicalEntity"}, {"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A total of 60 male Wistar albino rats were randomly divided into four groups ( 15/group ) : The control group injected with single doses of normal saline ( i.c.v ) followed 24 h later by BCNU solvent ( i.v ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "BCNU", "type": "ChemicalEntity"}]}

Example input:
Sentence: Rats were divided into eight groups and bilaterally cannulated into CA1 region of the hippocampus .

Example answer:
{"entities": [{"text": "Rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "allopurinol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The rats were assigned into four groups ( n=10 per group ) , as follows : Control rats ; rats+atorvastatin ; rats + iopamidol ; rats+iopamidol+atorvastatin .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rats+atorvastatin", "type": "OrganismTaxon"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "rats+iopamidol+atorvastatin", "type": "OrganismTaxon"}]}

Input:
Sentence: Rats were divided into three groups : sham , VCM and VCM plus erdosteine .

## Item biored:test:183
Example input:
Sentence: METHODS : We resequenced the positional candidate gene RNASEL in 48 prostate cancer cases and genotyped the previously reported R462Q and D541E polymorphisms in 230 prostate cancer cases and 458 controls .

Example answer:
{"entities": [{"text": "RNASEL", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "R462Q", "type": "SequenceVariant"}, {"text": "D541E", "type": "SequenceVariant"}]}

Example input:
Sentence: We also observed a 20 bp insertion/deletion polymorphism 1,109 bp upstream of the initiation codon , but this variant was not associated with prostate cancer .

Example answer:
{"entities": [{"text": "20 bp insertion/deletion polymorphism 1,109 bp upstream of the initiation codon", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Another POF patient of African origin showed a homozygous nucleotide change in the tenth of DMC1 gene that led to an alteration of the amino acid composition of the protein ( M200V ) .

Example answer:
{"entities": [{"text": "POF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "M200V", "type": "SequenceVariant"}]}

Example input:
Sentence: OBJECTIVE : We examined the genetic association of the promoter insertion/deletion ( indel ) in IRF5 gene with systemic lupus erythematosus ( SLE ) in distinct populations and assessed its role in gene expression .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The six-nucleotide deletion/insertion variant in the CASP8 promoter region is inversely associated with risk of squamous cell carcinoma of the head and neck .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A SNP for guanine insertion/deletion ( G/D ) , the -1607 promoter polymorphism , of the MMP1 gene was found significantly affecting promoter activity and corresponding transcription level .

Example answer:
{"entities": [{"text": "guanine insertion/deletion ( G/D ) , the -1607 promoter polymorphism", "type": "SequenceVariant"}, {"text": "MMP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : We corroborated the association of the promoter indel with SLE in 5 different populations and revealed that rs10954213 is the main single-nucleotide polymorphism responsible for altered IRF5 expression in PBMC .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs10954213", "type": "SequenceVariant"}, {"text": "IRF5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : In this family , a heterozygous cytosine insertion in exon 10 ( c.1546_1547insC ) inducing a frame shift mutation of MEN1 was found in the proband and the other two suffering members of his family .

Example answer:
{"entities": [{"text": "cytosine insertion", "type": "SequenceVariant"}, {"text": "c.1546_1547insC", "type": "SequenceVariant"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Of these , rs11891426 : T > G in an intron of the melanophilin gene ( MLPH ) was within a novel putative auxiliary AR-binding motif , which is enriched in the neighborhood of canonical androgen-responsive elements .

Example answer:
{"entities": [{"text": "rs11891426", "type": "SequenceVariant"}, {"text": "T > G", "type": "SequenceVariant"}, {"text": "melanophilin", "type": "GeneOrGeneProduct"}, {"text": "MLPH", "type": "GeneOrGeneProduct"}, {"text": "AR-binding", "type": "GeneOrGeneProduct"}, {"text": "androgen-responsive", "type": "ChemicalEntity"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We identified a promoter insertion/deletion in linkage disequilibrium with the previously described BRAF polymorphism in intron 11 ( rs1639679 ) reported to be associated with melanoma susceptibility in males .

## Item biored:test:220
Example input:
Sentence: These findings suggest that glutamate-mediated mechanisms in the neural circuits at the IC level influence haloperidol-induced catalepsy and participate in the regulation of motor activity .

Example answer:
{"entities": [{"text": "glutamate-mediated", "type": "ChemicalEntity"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Levodopa is the most effective symptomatic therapy for Parkinson 's disease , but its chronic use could lead to chronic adverse outcomes , such as motor fluctuations , dyskinesia and visual hallucinations .

Example answer:
{"entities": [{"text": "Levodopa", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We studied the prevalence and predictors of levodopa-induced dyskinesia among multiethnic Malaysian patients with PD .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Risk factors and predictors of levodopa-induced dyskinesia among multiethnic Malaysians with Parkinson 's disease .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Dyskinesia was present in 44 % ( n = 42 ) with median levodopa therapy of 3 years .

Example answer:
{"entities": [{"text": "Dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "levodopa", "type": "ChemicalEntity"}]}

Example input:
Sentence: The three significant predictors of dyskinesia were duration of levodopa therapy , onset age , and total daily levodopa dose .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "levodopa", "type": "ChemicalEntity"}]}

Example input:
Sentence: Patients with dyskinesia had lower onset age ( p < 0.001 ) , longer duration of levodopa therapy ( p < 0.001 ) , longer disease duration ( p < 0.001 ) , higher total daily levodopa dose ( p < 0.001 ) , and higher total UPDRS scores ( p = 0.005 ) than patients without dyskinesia .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "levodopa", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In addition , there is convincing clinical evidence that monotherapy with continuous subcutaneous apomorphine infusions is associated with marked reductions of preexisting levodopa-induced dyskinesias .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesias", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Chronic pulsatile levodopa therapy for Parkinson 's disease ( PD ) leads to the development of motor fluctuations and dyskinesia .

Example answer:
{"entities": [{"text": "levodopa", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The prevalence of levodopa-induced dyskinesia in our patients was 44 % .

Example answer:
{"entities": [{"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: The neural mechanisms and circuitry involved in levodopa-induced dyskinesia are unclear .

## Item biored:test:251
Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A relatively high frequency of germ-line genomic rearrangements in MLH1 and MSH2 has been reported among Lynch Syndrome ( HNPCC ) patients from different ethnic populations .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Using a genome-wide screen of DNA copy number alterations in 36 primary OSCs , we identified two tumors with apparent homozygous deletions of the NF1 gene .

Example answer:
{"entities": [{"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ten primary central nervous system lymphomas ( PCNSL , brain lymphomas ) were examined for p14 gene exon 1beta deletion , mutation and methylation by Southern blot analysis , nucleotide analysis of polymerase chain reaction clones and Southern blot-based methylation assay .

Example answer:
{"entities": [{"text": "primary central nervous system lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our observation of frequent p14 gene abnormalities ( 90 % ) and inactivation ( 40-60 % ) was in striking contrast to the same pathological subtype of systemic lymphoma in which p14 gene abnormalities and inactivation were infrequent , suggesting a difference in carcinogenesis between PCNSL and systemic lymphoma .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}, {"text": "systemic lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: RESULTS : The most recurrent alterations in PCFCL were high-level DNA amplifications at 2p16.1 ( 63 % ) and deletion of chromosome 14q32.33 ( 68 % ) .

## Item biored:test:242
Example input:
Sentence: The major histocompatibility complex ( MHC ) on chromosome 6p21 is a key contributor to the genetic basis of systemic lupus erythematosus ( SLE ) .

Example answer:
{"entities": [{"text": "major histocompatibility complex", "type": "GeneOrGeneProduct"}, {"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our study suggests that Alu is a promoting factor for the genomic recombinations in both MLH1 and MSH2 , and the local Alu density may be involved in shaping the deletion pattern .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The expression of NEK2 , phospho-AKT and MMP-2 was evaluated by immunohistochemistry in 63 cases of HCC and matched adjacent non-tumorous liver tissues .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "MMP-2", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Collectively , these results extend the pattern of TMPRSS6 mutations associated with IRIDA and functionally demonstrate that mutations affecting protease regions other than the catalytic domain may have a profound impact in the regulatory role of matriptase-2 during iron deficiency .

Example answer:
{"entities": [{"text": "TMPRSS6", "type": "GeneOrGeneProduct"}, {"text": "IRIDA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "matriptase-2", "type": "GeneOrGeneProduct"}, {"text": "iron deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we show that simultaneous overexpression of the mitotic checkpoint protein Mad2 with Kras ( G12D ) or Her2 in mammary glands of adult mice results in mitotic checkpoint overactivation and a delay in tumor onset .

Example answer:
{"entities": [{"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "GeneOrGeneProduct"}, {"text": "Her2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In Mz-ChA-1 cells stimulated with ( R ) - ( alpha ) - ( - ) -methylhistamine dihydrobromide ( RAMH ) , we measured ( a ) cell growth , ( b ) IP ( 3 ) and cyclic AMP levels , and ( c ) phosphorylation of PKC and mitogen-activated protein kinase isoforms .

Example answer:
{"entities": [{"text": "Mz-ChA-1", "type": "CellLine"}, {"text": "( R ) - ( alpha ) - ( - ) -methylhistamine dihydrobromide", "type": "ChemicalEntity"}, {"text": "RAMH", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The five cases of MSH2 deletions result exclusively from intragenic unequal recombination mediated by repetitive Alu sequences .

Example answer:
{"entities": [{"text": "MSH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Loss of MLH1 , a major component of DNA MMR , results in tolerance to the cytotoxic effects of methylating agents and persistence of mutagenised cells at high risk of malignant transformation .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cytotoxic", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: hMSH2 is one of the crucial proteins of MMR .

## Item biored:test:226
Example input:
Sentence: A combined clinical and genetic study was conducted in a cohort of patients with CDSRR , to substantiate these prior RESULTS : Seventeen patients from 13 families underwent a detailed ophthalmic examination including color vision testing , Goldmann visual fields , fundus photography , Ganzfeld and multifocal ERGs , and optical coherence tomography .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DESIGN AND METHODS : Nine patients clinically diagnosed with hemochromatosis were included in the study .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "hemochromatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Seven hundred fifty three subjects , corresponding to 251 full trios of childhood-onset SLE families , were genotyped and analyzed using transmission disequilibrium testing ( TDT ) and multitest corrections .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : One hundred and fifty-eight patients with wet AMD , 80 patients with soft drusen , and 220 matched control subjects were recruited among Han Chinese in mainland China .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS : Three affected individuals from the same family ( a father and his two children ) were studied .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : Twenty-four members of the family were clinically examined and genomic DNA was extracted .

Example answer:
{"entities": []}

Example input:
Sentence: 480 subjects were studied : 240 patients with premature CAD , 240 age and sex matched blood donors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Thirty-seven unrelated patients were studied , 18 with LCD and 19 with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A total of 1346 patients were randomized into the 8-week core study ( 734 men , 612 women ; 924 white , 291 black , 23 Asian , 108 other ; mean age , 52.7 years ; mean weight , 92.6 kg ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: PATIENTS AND METHODS : Six unrelated families and 10 sporadic patients were examined clinically .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: METHODS : Nine patients with BCD from six families were recruited into the study .

## Item biored:test:227
Example input:
Sentence: Exonic and intronic segments , 5 ' and 3 ' flanking regions of IRS2 ( 14.5 kb ) , were bidirectionally sequenced for single nucleotide polymorphism ( SNP ) discovery in 934 Hispanic children using 3730XL DNA Sequencers .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The patient was a compound heterozygote for SRD5A2 mutations , carrying 2 mutations in exon 4 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We sequenced exon IV of COMT gene in search for novel polymorphisms and then genotyped four out of five identified by direct sequencing , using TaqMan assay on 266 opioid-dependent and 173 control subjects .

Example answer:
{"entities": [{"text": "COMT", "type": "GeneOrGeneProduct"}, {"text": "opioid-dependent", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : To begin to determine whether mutations in UP genes might play a role in human VUR , we genotyped all four UP genes in 76 patients with radiologically proven primary VUR by polymerase chain reaction ( PCR ) amplification and sequencing of all their exons plus 50 to 150 bp of flanking intronic sequences .

Example answer:
{"entities": [{"text": "UP", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Genomic DNA extracted from peripheral blood was amplified by polymerase chain reaction ( PCR ) method and the exons of all candidate genes were sequenced .

Example answer:
{"entities": []}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Exons 1-8 of the AR gene and exons 1-5 of the SRD5A2 gene were sequenced from peripheral blood DNA .

Example answer:
{"entities": [{"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : DNA obtained from leukocytes and tumor cells was amplified by polymerase chain reaction regarding five exons of PTCH1 and PTCH2 and neighboring microsatellites .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "PTCH2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The 11 exons of the CYP4V2 gene were amplified from genomic DNA of patients by polymerase chain reaction and then sequenced .

## Item biored:test:230
Example input:
Sentence: In 10 of these families , all the homozygotes have a 137-bp insertion in their cDNA caused by a point mutation in a sequence resembling a splice-donor site .

Example answer:
{"entities": [{"text": "137-bp insertion", "type": "SequenceVariant"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found a single nucleotide deletion c.342delA , located in exon 3 , which resulted in a frameshift at amino acid position 58 ( p.Arg58fs or p.R58fs ) .

Example answer:
{"entities": [{"text": "c.342delA", "type": "SequenceVariant"}, {"text": "p.Arg58fs", "type": "SequenceVariant"}, {"text": "p.R58fs", "type": "SequenceVariant"}]}

Example input:
Sentence: In Southern blot analysis , from the signal densities of the hybridized bands and their similarities to those of exons 2 and 3 in our previous quantitative study , we found that exon 1beta was homozygously deleted in four cases , hemizygously deleted in five cases and not deleted in one case .

Example answer:
{"entities": []}

Example input:
Sentence: In addition , although exon 1beta mutation is rare in various tumors , we detected a missense mutation ( L50R ) in one case with a hemizygous deletion .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "L50R", "type": "SequenceVariant"}]}

Example input:
Sentence: Thus , the same deletion patterns covered the entire p14 gene for all cases except for one case , which suggested the hemizygous deletion of exons 1beta and 2 and homozygous deletion of exon 3 .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: The compound heterozygous mutations , c.892C > T and c.1072T > C , were identified in exon 3 of CHST6 in three patients .

Example answer:
{"entities": [{"text": "c.892C > T", "type": "SequenceVariant"}, {"text": "c.1072T > C", "type": "SequenceVariant"}, {"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Input:
Sentence: The third mutation , a previously identified 15-bp deletion that included the 3 ' splice site for exon 7 , was found in all nine patients , with six patients carrying the deletion in the homozygous state .

## Item biored:test:248
Example input:
Sentence: CONCLUSION : Tumor TS 1494del6 genotype may be a prognostic factor in FU-based adjuvant treatment of colorectal cancer patients .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "1494del6", "type": "SequenceVariant"}, {"text": "FU-based", "type": "ChemicalEntity"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Quantitative microsatellite analysis revealed LOH 10q in 41 of 59 ( 69 % ) glioblastomas .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Ag-globin gene sequencing was performed on genomic DNA isolated from a total of 75 b-thalassemia patients , including 31 b ( 0 ) 39/b ( 0 ) 39 , 33 b ( 0 ) 39/b ( + ) IVSI-110 , 9 b ( + ) IVSI-110/b ( + ) IVSI-110 , one b ( 0 ) IVSI-1/b ( + ) IVSI-6 and one b ( 0 ) 39/b ( + ) IVSI-6 .

Example answer:
{"entities": [{"text": "Ag-globin", "type": "GeneOrGeneProduct"}, {"text": "b-thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a genome-wide screen of DNA copy number alterations in 36 primary OSCs , we identified two tumors with apparent homozygous deletions of the NF1 gene .

Example answer:
{"entities": [{"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We have analyzed skin lesions from RTRs with aggressive tumors for p53 gene modifications , the presence of Human Papillomas Virus ( HPV ) DNA in relation to the p53 codon 72 genotype and polymorphisms of the XPD repair gene .

Example answer:
{"entities": [{"text": "skin lesions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "Human Papillomas Virus", "type": "OrganismTaxon"}, {"text": "HPV", "type": "OrganismTaxon"}, {"text": "XPD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ten primary central nervous system lymphomas ( PCNSL , brain lymphomas ) were examined for p14 gene exon 1beta deletion , mutation and methylation by Southern blot analysis , nucleotide analysis of polymerase chain reaction clones and Southern blot-based methylation assay .

Example answer:
{"entities": [{"text": "primary central nervous system lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Array-based comparative genomic hybridization analysis reveals recurrent chromosomal alterations and prognostic parameters in primary cutaneous large B-cell lymphoma .

## Item biored:test:219
Example input:
Sentence: Dyskinesia was present in 44 % ( n = 42 ) with median levodopa therapy of 3 years .

Example answer:
{"entities": [{"text": "Dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "levodopa", "type": "ChemicalEntity"}]}

Example input:
Sentence: Patients with dyskinesia had lower onset age ( p < 0.001 ) , longer duration of levodopa therapy ( p < 0.001 ) , longer disease duration ( p < 0.001 ) , higher total daily levodopa dose ( p < 0.001 ) , and higher total UPDRS scores ( p = 0.005 ) than patients without dyskinesia .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "levodopa", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Parkinson 's disease ( PD ) is a neurodegenerative disorder causing muscular rigidity , resting tremor and bradykinesia .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegenerative disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscular rigidity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "resting tremor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradykinesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A number of small scale clinical trials have unequivocally shown that intermittent subcutaneous apomorphine injections produce antiparkinsonian benefit close if not identical to that seen with levodopa and that apomorphine rescue injections can reliably revert off-periods even in patients with complex on-off motor swings .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "levodopa", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: While powerful antiparkinsonian effects had been observed as early as 1951 , the potential of treating fluctuating Parkinson 's disease by subcutaneous administration of apomorphine has only recently become the subject of systematic study .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "apomorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Apomorphine : an underutilized therapy for Parkinson 's disease .

Example answer:
{"entities": [{"text": "Apomorphine", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Levodopa is the most effective symptomatic therapy for Parkinson 's disease , but its chronic use could lead to chronic adverse outcomes , such as motor fluctuations , dyskinesia and visual hallucinations .

Example answer:
{"entities": [{"text": "Levodopa", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: There is now evidence to suggest a central role for the dopaminergic system in restless legs syndrome ( RLS ) .

Example answer:
{"entities": [{"text": "restless legs syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RLS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , there is convincing clinical evidence that monotherapy with continuous subcutaneous apomorphine infusions is associated with marked reductions of preexisting levodopa-induced dyskinesias .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesias", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Chronic pulsatile levodopa therapy for Parkinson 's disease ( PD ) leads to the development of motor fluctuations and dyskinesia .

Example answer:
{"entities": [{"text": "levodopa", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: rTMS of supplementary motor area modulates therapy-induced dyskinesias in Parkinson disease .

## Item biored:test:197
Example input:
Sentence: Immunoelectron microscopy further revealed an increased labeling of alpha-ENaC in the apical plasma membrane of cortical collecting duct principal cells of PAN-treated rats , indicating enhanced apical targeting of alpha-ENaC subunits .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "PAN-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PA-1 cells treated with ETO display highly heterogeneous increases in OCT4A and p21Cip1 indicative of dis-adaptation catastrophe .

Example answer:
{"entities": [{"text": "PA-1", "type": "CellLine"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: UCHL1 depletion in SF188 and SJ-GBM2 glioma cells was associated with decreased cell proliferation and invasion , along with a reduced ability to grow in soft agar and to form spheres ( i.e .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agar", "type": "ChemicalEntity"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Functional analyses reveal that whilst cilium structure , sensory function and IFT are seemingly normal in a rab-28 null allele , overexpression of predicted GDP or GTP locked variants of RAB-28 perturbs cilium and sensory pore morphogenesis and function .

Example answer:
{"entities": [{"text": "rab-28", "type": "GeneOrGeneProduct"}, {"text": "GDP", "type": "ChemicalEntity"}, {"text": "GTP", "type": "ChemicalEntity"}, {"text": "RAB-28", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: The change in GAP43-ir present in Pilo-treated animals was a thinning of the band to a very narrow layer just above the granule cell layer that is likely to be associated with the loss of hilar cell projections that express GAP-43 .

## Item biored:test:200
Example input:
Sentence: Association study of polymorphisms in the promoter region of DRD4 with schizophrenia , depression , and heroin addiction .

Example answer:
{"entities": [{"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We sequenced exon IV of COMT gene in search for novel polymorphisms and then genotyped four out of five identified by direct sequencing , using TaqMan assay on 266 opioid-dependent and 173 control subjects .

Example answer:
{"entities": [{"text": "COMT", "type": "GeneOrGeneProduct"}, {"text": "opioid-dependent", "type": "ChemicalEntity"}]}

Example input:
Sentence: These observations strongly suggest that the -120-bp duplication polymorphism of DRD4 is associated with schizophrenia and that the -521 C/T polymorphism is associated with heroin addiction .

Example answer:
{"entities": [{"text": "-120-bp duplication", "type": "SequenceVariant"}, {"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-521 C/T", "type": "SequenceVariant"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study investigated the possible association between three functional polymorphisms in the promoter region of the dopamine D4 receptor ( DRD4 ) gene and schizophrenia , depression , and heroin addiction .

Example answer:
{"entities": [{"text": "dopamine D4 receptor", "type": "GeneOrGeneProduct"}, {"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OPMD is caused by a short trinucleotide repeat expansion encoding an expanded polyalanine tract in the polyadenylate binding-protein nuclear 1 ( PABPN1 ) gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "polyalanine", "type": "ChemicalEntity"}, {"text": "polyadenylate binding-protein nuclear 1", "type": "GeneOrGeneProduct"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further analysis of G472A genotypes in Hispanic subjects with data stratified by gender identified a point-wise significant ( P = 0.049 ) association of G/A and A/A genotypes with opiate addiction in women , but not men .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "opiate addiction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Thus , our study demonstrates for the first time , a novel OPRM1-mediated mechanism for L-asparaginase resistance in ALL , and identifies OPRM1 as a functional biomarker for defining high-risk subpopulations and for the detection of evolving resistant clones .

Example answer:
{"entities": [{"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using a genotype test , we found a trend to point-wise association ( P = 0.053 ) of the G472A SNP in Hispanic subjects with opiate addiction .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "opiate addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Catechol-O-methyltransferase ( COMT ) gene variants : possible association of the Val158Met variant with opiate addiction in Hispanic women .

Example answer:
{"entities": [{"text": "Catechol-O-methyltransferase", "type": "GeneOrGeneProduct"}, {"text": "COMT", "type": "GeneOrGeneProduct"}, {"text": "Val158Met", "type": "SequenceVariant"}, {"text": "opiate addiction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Input:
Sentence: Genetic variants of OPRM1 have been implicated in predisposition to drug addiction , in particular the single nucleotide polymorphism A118G , leading to an N40D substitution , with an allele frequency of 10-32 % , and uncertain functions .

## Item biored:test:221
Example input:
Sentence: CONCLUSION : In a PA retention paradigm , the injection of NTG immediately after learning produced a significant impairment of long-term associative memory in mice , whereas delayed induced hypotension had no effect .

Example answer:
{"entities": [{"text": "NTG", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Levodopa is the most effective symptomatic therapy for Parkinson 's disease , but its chronic use could lead to chronic adverse outcomes , such as motor fluctuations , dyskinesia and visual hallucinations .

Example answer:
{"entities": [{"text": "Levodopa", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Apomorphine was the first dopaminergic drug ever used to treat symptoms of Parkinson 's disease .

Example answer:
{"entities": [{"text": "Apomorphine", "type": "ChemicalEntity"}, {"text": "dopaminergic drug", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Continuous subcutaneous apomorphine infusions can reduce daily off-time by more than 50 % in this group of patients , which appears to be a stronger effect than that generally seen with add-on therapy with oral dopamine agonists or COMT inhibitors .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "dopamine agonists", "type": "ChemicalEntity"}, {"text": "COMT inhibitors", "type": "ChemicalEntity"}]}

Example input:
Sentence: While powerful antiparkinsonian effects had been observed as early as 1951 , the potential of treating fluctuating Parkinson 's disease by subcutaneous administration of apomorphine has only recently become the subject of systematic study .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "apomorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Apomorphine : an underutilized therapy for Parkinson 's disease .

Example answer:
{"entities": [{"text": "Apomorphine", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A number of small scale clinical trials have unequivocally shown that intermittent subcutaneous apomorphine injections produce antiparkinsonian benefit close if not identical to that seen with levodopa and that apomorphine rescue injections can reliably revert off-periods even in patients with complex on-off motor swings .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "levodopa", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Given the marked degree of efficacy of subcutaneous apomorphine treatment in fluctuating Parkinson 's disease , this approach seems to deserve more widespread clinical use .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Chronic pulsatile levodopa therapy for Parkinson 's disease ( PD ) leads to the development of motor fluctuations and dyskinesia .

Example answer:
{"entities": [{"text": "levodopa", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , there is convincing clinical evidence that monotherapy with continuous subcutaneous apomorphine infusions is associated with marked reductions of preexisting levodopa-induced dyskinesias .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesias", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Using repetitive transcranial magnetic stimulation ( rTMS ) over the supplementary motor area ( SMA ) in a group of patients with advanced Parkinson disease , the authors investigated whether modulation of SMA excitability may result in a modification of a dyskinetic state induced by continuous apomorphine infusion .

## Item biored:test:201
Example input:
Sentence: RESULTS : We found that sorted SUM159PT cell populations with high ADAM12 levels had elevated expression of CSC markers and an increased ability to form mammospheres .

Example answer:
{"entities": [{"text": "SUM159PT", "type": "CellLine"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : In contrast to a single GCG expansion in most of OPMD patients in the literature , an insertion of ( GCG ) 4GCA in the PABPN1 gene was found in the Taiwanese OPMD subjects .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "insertion of ( GCG ) 4GCA", "type": "SequenceVariant"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Oprm1 may also be utilized for effective treatment of L-asparaginase-resistant ALL.Oncogene advance online publication , 26 June 2017 ; doi:10.1038/onc.2017.211 .

Example answer:
{"entities": [{"text": "Oprm1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase-resistant", "type": "ChemicalEntity"}, {"text": "ALL.Oncogene", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Consistent with this premise , patient leukemic cells with relatively high levels of OPRM1 are more sensitive to L-asparaginase treatment compared to OPRM1-depleted leukemic cells , further indicating that OPRM1 loss has a crucial role in L-asparaginase resistance in leukemic patients .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Specific knockdown of OPRM1 confers L-asparaginase resistance , validating our genome-wide retroviral shRNA library screening data .

Example answer:
{"entities": [{"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Thus , our study demonstrates for the first time , a novel OPRM1-mediated mechanism for L-asparaginase resistance in ALL , and identifies OPRM1 as a functional biomarker for defining high-risk subpopulations and for the detection of evolving resistant clones .

Example answer:
{"entities": [{"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also found that OPRM1 is expressed in all leukemic cells tested .

Example answer:
{"entities": [{"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We have measured allele-specific mRNA expression of OPRM1 in human autopsy brain tissues , using A118G as a marker .

## Item biored:test:246
Example input:
Sentence: Common germline genetic variation in antioxidant defense genes and survival after diagnosis of breast cancer .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the haplotype analysis , 1 haplotype carrying the variant allele from both +3100 T/G and +8365 C/T , with a population frequency of 3 % , was also significantly associated with decreased risk of prostate cancer ( p=0.036 , global simulated p-value=0.046 ) .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A common A/G transition -1,071 bp from the transcriptional start site was genotyped and showed no evidence of association with prostate cancer .

Example answer:
{"entities": [{"text": "A/G transition -1,071 bp", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : We found no evidence of association between R462Q and D541E polymorphisms and prostate cancer risk in our case/control analysis .

Example answer:
{"entities": [{"text": "R462Q", "type": "SequenceVariant"}, {"text": "D541E", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: By histology-based analysis , the Cys/Cys genotype showed a significantly positive association with small-cell carcinoma ( OR=2.40 , 95 % CI=1.32-4.49 ) and marginally significant association with adenocarcinoma ( OR=1.32 , 95 % CI=0.98-1.77 ) .

Example answer:
{"entities": [{"text": "small-cell carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A meta-analysis of previous and our present study revealed that this polymorphism is positively associated with adenocarcinoma , although suggestive associations were also found for squamous- and small-cell lung cancers .

Example answer:
{"entities": [{"text": "adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "squamous- and small-cell lung cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A single nucleotide polymorphism at position 388 of the FGFR4 amino-acid sequence results in the substitution of glycine ( Gly ) with arginine ( Arg ) and higher frequency of the ArgArg genotype was previously found in prostate cancer patients .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}, {"text": "glycine ( Gly ) with arginine ( Arg )", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Genome-wide association studies have identified genomic loci , whose single-nucleotide polymorphisms ( SNPs ) predispose to prostate cancer ( PCa ) .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In overall analysis , the homozygous Cys/Cys genotype showed a significant association with lung cancer compared to Ser allele carrier status ( odds ratio ( OR ) =1.31 , 95 % confidence interval ( CI ) =1.02-1.69 ) .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The single nucleotide polymorphism Gly ( 388 ) Arg in FGFR4 is not associated with increased risk of prostate cancer in Scottish men .

Example answer:
{"entities": [{"text": "Gly ( 388 ) Arg", "type": "SequenceVariant"}, {"text": "FGFR4", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "men", "type": "OrganismTaxon"}]}

Input:
Sentence: A strong association between breast cancer occurrence and the Gly/Gly phenotype of the Gly322Asp polymorphism ( odds ratio 8.39 ; 95 % confidence interval 1.44-48.8 ) was found .

## Item biored:test:238
Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Odds ratios and 95 % confidence intervals for cancer risk by MLH1 -93 polymorphism status , and stratified by previous exposure to methylating chemotherapy , were calculated using unconditional logistic regression .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We did not observe any correlation between the Ser1245Cys polymorphism of the hOGG1 gene and gastric cancer , including subjects with impaired DNA repair and/or high levels of endogenous oxidative DNA lesions .

Example answer:
{"entities": [{"text": "Ser1245Cys", "type": "SequenceVariant"}, {"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The five cases of MSH2 deletions result exclusively from intragenic unequal recombination mediated by repetitive Alu sequences .

Example answer:
{"entities": [{"text": "MSH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A relatively high frequency of germ-line genomic rearrangements in MLH1 and MSH2 has been reported among Lynch Syndrome ( HNPCC ) patients from different ethnic populations .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : A single heterozygous missense mutation , substitution of a cytosine residue with thymidine in exon 2 of MSH5 , was found in two Caucasian women in whom POF developed at 18 and 36 years of age .

Example answer:
{"entities": [{"text": "cytosine residue with thymidine", "type": "SequenceVariant"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymorphic MLH1 and risk of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Polymorphisms of the DNA mismatch repair gene HMSH2 in breast cancer occurence and progression .

## Item biored:test:241
Example input:
Sentence: Given the essential role of this hormonal system in breast physiology , we reasoned that genetic anomalies of Prl/PrlR genes may be related to the occurrence of breast diseases with high proliferative potential .

Example answer:
{"entities": [{"text": "Prl/PrlR", "type": "GeneOrGeneProduct"}, {"text": "breast diseases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the present study we explored the effect of three polymorphisms of the TS gene on overall and progression- free survival of colorectal cancer ( CRC ) patients subjected to 5FU chemotherapy .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "5FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Common germline genetic variation in antioxidant defense genes and survival after diagnosis of breast cancer .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : The prognosis of breast cancer varies considerably among individuals , and inherited genetic factors may help explain this variability .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Odds ratios and 95 % confidence intervals for cancer risk by MLH1 -93 polymorphism status , and stratified by previous exposure to methylating chemotherapy , were calculated using unconditional logistic regression .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Loss of MLH1 , a major component of DNA MMR , results in tolerance to the cytotoxic effects of methylating agents and persistence of mutagenised cells at high risk of malignant transformation .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cytotoxic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The importance of genetic variability of the components of mismatch repair ( MMR ) genes is well documented in colorectal cancer , but little is known about its role in breast cancer .

## Item biored:test:229
Example input:
Sentence: In the TfR2 gene , 2 novel mutations , 1469T- > G ( L490R ) and 1665delC ( V561X ) , were found in 2 patients .

Example answer:
{"entities": [{"text": "TfR2", "type": "GeneOrGeneProduct"}, {"text": "1469T- > G", "type": "SequenceVariant"}, {"text": "L490R", "type": "SequenceVariant"}, {"text": "1665delC", "type": "SequenceVariant"}, {"text": "V561X", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The I280S mutation was recently reported in a heterozygous patient .

Example answer:
{"entities": [{"text": "I280S", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mutations of MKS3/TMEM67 , found recently in Meckel-Gruber syndrome ( MKS ) type 3 and Joubert syndrome ( JBTS ) type 6 , are predominantly truncating mutations .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "Meckel-Gruber syndrome ( MKS ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Joubert syndrome ( JBTS ) type 6", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , mutation of arginine 124-to-cysteine ( Arg124Cys ) was found in 8 of 18 patients and histidine 626-to-arginine ( His626Arg ) in 2 of 18 patients .

Example answer:
{"entities": [{"text": "arginine 124-to-cysteine", "type": "SequenceVariant"}, {"text": "Arg124Cys", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "histidine 626-to-arginine", "type": "SequenceVariant"}, {"text": "His626Arg", "type": "SequenceVariant"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Input:
Sentence: RESULTS : Three pathogenic mutations were identified ; two mutations , S482X and K386T , were novel and found in three patients .

## Item biored:test:207
Example input:
Sentence: Oxidative stress may be involved in the development of stone formation in the renal system .

Example answer:
{"entities": [{"text": "stone formation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These findings suggest that thrombin plays an important role in the pathogenesis of puromycin aminonucleoside-induced nephrotic syndrome .

Example answer:
{"entities": [{"text": "thrombin", "type": "GeneOrGeneProduct"}, {"text": "puromycin", "type": "ChemicalEntity"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Renal failure developed after a prolonged course of vancomycin therapy in 2 patients who were receiving tenofovir disoproxil fumarate as part of an antiretroviral regimen .

Example answer:
{"entities": [{"text": "Renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vancomycin", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "tenofovir disoproxil fumarate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hsp90beta inhibition caused the destabilization of upstream mediators in various pathogenic signalling events , thereby effectively ameliorating this nephropathy owing to renal hypoxia and oxidative stress .

Example answer:
{"entities": [{"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoxia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The results of the present study suggested that atorvastatin protected against contrast-induced renal tubular cell apoptosis through the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced renal tubular cell apoptosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Atorvastatin protects against contrast-induced nephropathy via anti-apoptosis by the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Vancomycin nephrotoxicity is infrequent but may result from coadministration with a nephrotoxic agent .

Example answer:
{"entities": [{"text": "Vancomycin", "type": "ChemicalEntity"}, {"text": "nephrotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nephrotoxic", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In vivo evidences suggesting the role of oxidative stress in pathogenesis of vancomycin-induced nephrotoxicity : protection by erdosteine .

## Item biored:test:231
Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSION : The novel finding of this study is the association of the mutant allele ( A1359 ) with a decrease of resistin , leptin and interleukin-6 secondary to weight loss .

Example answer:
{"entities": [{"text": "A1359", "type": "SequenceVariant"}, {"text": "resistin", "type": "GeneOrGeneProduct"}, {"text": "leptin", "type": "GeneOrGeneProduct"}, {"text": "interleukin-6", "type": "GeneOrGeneProduct"}, {"text": "weight loss", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This mutation was responsible for the familial disorder through the substitution of a highly conserved arginine to tryptophan at codon 198 ( p.R198W ) .

Example answer:
{"entities": [{"text": "arginine to tryptophan at codon 198", "type": "SequenceVariant"}, {"text": "p.R198W", "type": "SequenceVariant"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: Genetic analysis identified a novel V876E mutation in all HypoPP patients in the family , but not in normal family members or 160 control people .

Example answer:
{"entities": [{"text": "V876E", "type": "SequenceVariant"}, {"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In addition , each affected child was heterozygous for the G1681A mutation in exon 7 that led to an Ala467Thr substitution in POLG , within the linker region of the protein .

Example answer:
{"entities": [{"text": "G1681A", "type": "SequenceVariant"}, {"text": "Ala467Thr", "type": "SequenceVariant"}, {"text": "POLG", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , although exon 1beta mutation is rare in various tumors , we detected a missense mutation ( L50R ) in one case with a hemizygous deletion .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "L50R", "type": "SequenceVariant"}]}

Input:
Sentence: Haplotype analysis in patients and controls indicated a founder effect for this deletion mutation in exon 7 .

## Item biored:test:249
Example input:
Sentence: Genome-wide association studies have identified genomic loci , whose single-nucleotide polymorphisms ( SNPs ) predispose to prostate cancer ( PCa ) .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Primary malignant lymphoma of the brain : frequent abnormalities and inactivation of p14 tumor suppressor gene .

Example answer:
{"entities": [{"text": "Primary malignant lymphoma of the brain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p14", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the TGFBI gene in Indian patients with lattice corneal dystrophy ( LCD ) or granular corneal dystrophy ( GCD ) and to look for genotype-phenotype correlations .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "granular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our observation of frequent p14 gene abnormalities ( 90 % ) and inactivation ( 40-60 % ) was in striking contrast to the same pathological subtype of systemic lymphoma in which p14 gene abnormalities and inactivation were infrequent , suggesting a difference in carcinogenesis between PCNSL and systemic lymphoma .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}, {"text": "systemic lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Integrated genomic and expression profiling in mantle cell lymphoma : identification of gene-dosage regulated candidate genes .

Example answer:
{"entities": [{"text": "mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ten primary central nervous system lymphomas ( PCNSL , brain lymphomas ) were examined for p14 gene exon 1beta deletion , mutation and methylation by Southern blot analysis , nucleotide analysis of polymerase chain reaction clones and Southern blot-based methylation assay .

Example answer:
{"entities": [{"text": "primary central nervous system lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p14", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: PURPOSE : To evaluate the clinical relevance of genomic aberrations in primary cutaneous large B-cell lymphoma ( PCLBCL ) .

## Item biored:test:196
Example input:
Sentence: Loss-of-function experiments demonstrate that Chl serves as a BMP antagonist with functions that overlap and are redundant with those of Chd in forming the dorsoventral axis .

Example answer:
{"entities": [{"text": "Chl", "type": "GeneOrGeneProduct"}, {"text": "BMP", "type": "GeneOrGeneProduct"}, {"text": "Chd", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: A common missense variant in the gene encoding a component of the sulfonylurea receptor ( ABCC8 p.A1369S ) promotes closure of the target channel of sulfonylurea therapy and is associated with increased insulin secretion , thus mimicking the effects of sulfonylurea therapy .

Example answer:
{"entities": [{"text": "sulfonylurea receptor", "type": "GeneOrGeneProduct"}, {"text": "ABCC8", "type": "GeneOrGeneProduct"}, {"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "sulfonylurea", "type": "ChemicalEntity"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A 70 % reduction in Wnt signaling was also observed in the SF188 and SJ-GBM2 UCHL1 knockdowns ( KDs ) using a TCF-dependent TOPflash reporter assay .

Example answer:
{"entities": [{"text": "Wnt", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "TCF-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We propose that the alteration in the replication/nuclear location pattern of the non-deleted TDR22 indicates an altered gene regulation hence an altered transcritpion in DGS/VCFS .

Example answer:
{"entities": [{"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Five of the forty genes -- ENT3 , IDP3 , JEM1 , ARG2 and HSP82 -- ranked highest in their ability to block alpha-syn-induced reactive oxygen species accumulation , and these five genes were characterized in more detail .

Example answer:
{"entities": [{"text": "ENT3", "type": "GeneOrGeneProduct"}, {"text": "IDP3", "type": "GeneOrGeneProduct"}, {"text": "JEM1", "type": "GeneOrGeneProduct"}, {"text": "ARG2", "type": "GeneOrGeneProduct"}, {"text": "HSP82", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn-induced", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}]}

Example input:
Sentence: Functional analyses reveal that whilst cilium structure , sensory function and IFT are seemingly normal in a rab-28 null allele , overexpression of predicted GDP or GTP locked variants of RAB-28 perturbs cilium and sensory pore morphogenesis and function .

Example answer:
{"entities": [{"text": "rab-28", "type": "GeneOrGeneProduct"}, {"text": "GDP", "type": "ChemicalEntity"}, {"text": "GTP", "type": "ChemicalEntity"}, {"text": "RAB-28", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: CONCLUSIONS : Our current finding that animals in the CHX+Pilo group have a GAP43-ir band in the IML , similar to that of controls , reinforces prior data on the blockade of MFS in these animals .

## Item biored:test:273
Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Etifoxine improved blood-brain barrier integrity and diminished cell death .

Example answer:
{"entities": [{"text": "Etifoxine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Intracerebral hemorrhage ( ICH ) is a devastating disease without effective treatment .

Example answer:
{"entities": [{"text": "Intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: INTRODUCTION AND OBJECTIVE : Contrast-induced nephropathy ( CIN ) significantly increases the morbidity and mortality of patients .

Example answer:
{"entities": [{"text": "Contrast-induced", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : The rate of major hemorrhage was high in this old , frail group , but excluding fatalities , resulted in no long-term sequelae , and the stroke rate on warfarin was low , demonstrating how effective warfarin treatment is .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Clinically significant anemia ( hemoglobin < 7 g/dL ) was observed in 5.4 % of patients ( CD4 , 165 cells/microL ) and hepatitis ( clinical jaundice with alanine aminotransferase > 5 times upper limits of normal ) in 3.5 % of patients ( CD4 , 260 cells/microL ) .

Example answer:
{"entities": [{"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hemoglobin", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "hepatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "jaundice", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alanine aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND : Hypotension and a resultant decrease in cerebral blood flow have been implicated in the development of cognitive dysfunction .

Example answer:
{"entities": [{"text": "Hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cognitive dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The side effects of azathioprine include anemia , which has been attributed to bone marrow suppression .

Example answer:
{"entities": [{"text": "azathioprine", "type": "ChemicalEntity"}, {"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bone marrow suppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND AND PURPOSE : Cerebral microbleeds ( MB ) are potential risk factors for intracerebral hemorrhage ( ICH ) , but it is unclear if they are a contraindication to using antithrombotic drugs .

Example answer:
{"entities": [{"text": "Cerebral microbleeds", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antithrombotic drugs", "type": "ChemicalEntity"}]}

Example input:
Sentence: Alternatively , anemia could result from accelerated suicidal erythrocyte death or eryptosis , which is characterized by exposure of phosphatidylserine ( PS ) at the erythrocyte surface and by cell shrinkage .

Example answer:
{"entities": [{"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "phosphatidylserine", "type": "ChemicalEntity"}, {"text": "PS", "type": "ChemicalEntity"}]}

Input:
Sentence: In general , anemia can increase the risk of morbidity and mortality , and may have negative effects on cerebral function and quality of life .

## Item biored:test:271
Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results suggest that , despite a known association with increased weight , long-term sulfonylurea therapy may reduce the risk of coronary heart disease .

Example answer:
{"entities": [{"text": "sulfonylurea", "type": "ChemicalEntity"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : In this study population , combination therapies with VAL/HCTZ were associated with significantly greater BP reductions compared with either monotherapy , were well tolerated , and were associated with less hypokalemia than HCTZ alone .

Example answer:
{"entities": [{"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: The incidence of hypokalemia was lower with VAL/HCTZ combinations ( 1.8 % -6.1 % ) than with HCTZ monotherapies ( 7.1 % -13.3 % ) .

Example answer:
{"entities": [{"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Strategies of extended-interval and conventional dosing have been utilized extensively in the general medical population ; however , data are lacking to support a dosing strategy in the hematology/oncology population .

Example answer:
{"entities": []}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using a mouse model , we tested whether the rapid reversal of anticoagulation using human prothrombin complex concentrate ( PCC ) can reduce hemorrhagic blood volume .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "prothrombin complex concentrate", "type": "ChemicalEntity"}, {"text": "PCC", "type": "ChemicalEntity"}]}

Example input:
Sentence: Clinically significant anemia ( hemoglobin < 7 g/dL ) was observed in 5.4 % of patients ( CD4 , 165 cells/microL ) and hepatitis ( clinical jaundice with alanine aminotransferase > 5 times upper limits of normal ) in 3.5 % of patients ( CD4 , 260 cells/microL ) .

Example answer:
{"entities": [{"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hemoglobin", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "hepatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "jaundice", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alanine aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: The most common regimens were 3TC + d4T + nevirapine ( NVP ) ( 54.8 % ) , zidovudine ( AZT ) + 3TC + NVP ( 14.5 % ) , 3TC + d4T + efavirenz ( EFV ) ( 20.1 % ) , and AZT + 3TC + EFV ( 5.4 % ) .

Example answer:
{"entities": [{"text": "3TC", "type": "ChemicalEntity"}, {"text": "d4T", "type": "ChemicalEntity"}, {"text": "nevirapine", "type": "ChemicalEntity"}, {"text": "NVP", "type": "ChemicalEntity"}, {"text": "zidovudine", "type": "ChemicalEntity"}, {"text": "AZT", "type": "ChemicalEntity"}, {"text": "efavirenz", "type": "ChemicalEntity"}, {"text": "EFV", "type": "ChemicalEntity"}]}

Example input:
Sentence: It remains to be seen whether such pre-existing antiviral mutations could result in widespread emergence of HBV resistant strains when lamivudine-containing highly active antiretroviral ( ARV ) treatment ( HAART ) regimens become widely applied in South Africa , as this is likely to have potential implications in the management of HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-containing", "type": "ChemicalEntity"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: Although this regimen produces sustained virologic responses ( SVRs ) in approximately 50 % of patients , it can be associated with a potentially dose-limiting hemolytic anemia .

## Item biored:test:189
Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Hippocampus mice treated with GFC75 plus P400 showed an increase in AChE activity ( 63.30 % ) when compared with seized mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: GFC produced an increased latency to first seizure , at doses 25mg/kg ( 20.12 + 2.20 min ) , 50mg/kg ( 20.95 + 2.21 min ) or 75 mg/kg ( 23.43 + 1.99 min ) when compared with seized mice .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "fractalkine receptor", "type": "GeneOrGeneProduct"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "MPTP-induced", "type": "ChemicalEntity"}, {"text": "neurodegeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DA", "type": "ChemicalEntity"}]}

Example input:
Sentence: In an independent sample set , we identified 5 GIST cases lacking alterations in the KIT/PDGFRA/SDHx/RAS pathways , including two additional cases with FGFR1-TACC1 and ETV6-NTRK3 fusions .

Example answer:
{"entities": [{"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KIT/PDGFRA/SDHx/RAS", "type": "GeneOrGeneProduct"}, {"text": "FGFR1-TACC1", "type": "GeneOrGeneProduct"}, {"text": "ETV6-NTRK3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , GABA content of mice hippocampus treated with GFC75 plus P400 showed an increase of 46.90 % when compared with seized mice .

Example answer:
{"entities": [{"text": "GABA", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion , our data suggest that GFC may influence in epileptogenesis and promote anticonvulsant actions in pilocarpine model by modulating the GABA and glutamate contents and of AChE activity in seized mice hippocampus .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Striatal microglia expressing eGFP constitutively show morphological changes after METH that are characteristic of activation .

Example answer:
{"entities": [{"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}]}

Input:
Sentence: PURPOSE : GAP43 has been thought to be linked with mossy fiber sprouting ( MFS ) in various experimental models of epilepsy .

## Item biored:test:199
Example input:
Sentence: Thus , our study demonstrates for the first time , a novel OPRM1-mediated mechanism for L-asparaginase resistance in ALL , and identifies OPRM1 as a functional biomarker for defining high-risk subpopulations and for the detection of evolving resistant clones .

Example answer:
{"entities": [{"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The present results demonstrate that CCK-8 attenuates the effect of morphine on hippocampal LTP through CCK2 receptors and suggest an ameliorative function of CCK-8 on morphine-induced memory impairment .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}, {"text": "CCK2 receptors", "type": "GeneOrGeneProduct"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Genome-wide loss-of-function genetic screening identifies opioid receptor u1 as a key regulator of L-asparaginase resistance in pediatric acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "opioid receptor u1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "acute lymphoblastic leukemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Methadone , an agonist of OPRM1 , enhances the sensitivity of parental leukemic cells , but not OPRM1-depleted cells , to L-asparaginase treatment , indicating that OPRM1 is required for the synergistic action of L-asparaginase and methadone , and that OPRM1 loss promotes leukemic cell survival likely through downregulation of the OPRM1-mediated apoptotic pathway .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "methadone", "type": "ChemicalEntity"}, {"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Human mu opiate receptor .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "mu opiate receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A human mu opiate receptor cDNA has been identified from a cerebral cortical cDNA library using sequences from the rat mu opiate receptor cDNA .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "mu opiate receptor", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: The human mu opiate receptor ( h mu OR1 ) shares 95 % amino acid identity with the rat sequence .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "mu opiate receptor", "type": "GeneOrGeneProduct"}, {"text": "h mu OR1", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The expressed mu OR1 recognized tested opiate drugs and opioid peptides in a sodium- and GTP-sensitive fashion with affinities virtually identical to those displayed by the rat mu opiate receptor .

Example answer:
{"entities": [{"text": "mu OR1", "type": "GeneOrGeneProduct"}, {"text": "opiate", "type": "ChemicalEntity"}, {"text": "opioid peptides", "type": "ChemicalEntity"}, {"text": "sodium-", "type": "ChemicalEntity"}, {"text": "GTP-sensitive", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "mu opiate receptor", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: As a primary target for opioid drugs and peptides , the mu opioid receptor ( OPRM1 ) plays a key role in pain perception and addiction .

## Item biored:test:235
Example input:
Sentence: A missense mutation in BCOR was described in a family with Lenz microphthalmia syndrome , a phenotype showing substantial overlapping features with that described in the two cousins .

Example answer:
{"entities": [{"text": "BCOR", "type": "GeneOrGeneProduct"}, {"text": "Lenz microphthalmia syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine the pathogenic importance of CB depletions in AD models , we crossed 5 familial AD mutations ( 5XFAD ; Tg ) mice with CB knock-out ( CBKO ) mice and generated a novel line CBKO.5XFAD ( CBKOTg ) mice .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CBKO", "type": "GeneOrGeneProduct"}, {"text": "CBKO.5XFAD", "type": "GeneOrGeneProduct"}, {"text": "CBKOTg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : Arg124Cys and Arg555Trp appear to be the predominant mutations causing LCD and GCD , respectively , in the population studied .

Example answer:
{"entities": [{"text": "Arg124Cys", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Whereas no mutations were detected in the PDE6H gene , mutations in KCNV2 were identified in all patients , in either the homozygous or compound heterozygous state .

Example answer:
{"entities": [{"text": "PDE6H", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Both sporadic and inherited BCCs are associated with mutations in the tumor suppressor gene PTCH1 , but there is still uncertainty on the role of its homolog PTCH2 .

Example answer:
{"entities": [{"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "PTCH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Example input:
Sentence: Importantly , 35 % ( 6/17 ) are tandem mutations , including 4 UV signature CC to TT transitions possibly linked to modulated DNA repair caused by the immunosuppressive drug cyclosporin A ( CsA ) .

Example answer:
{"entities": [{"text": "CC to TT", "type": "SequenceVariant"}, {"text": "cyclosporin A", "type": "ChemicalEntity"}, {"text": "CsA", "type": "ChemicalEntity"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : Mutations found in the PTCH1 gene and neighboring repetitive sequences may have contributed to the development of the studied BCCs .

Example answer:
{"entities": [{"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSIONS : This study identified novel mutations in the CYP4V2 gene as a cause of BCD .

## Item biored:test:160
Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To determine the pathogenic importance of CB depletions in AD models , we crossed 5 familial AD mutations ( 5XFAD ; Tg ) mice with CB knock-out ( CBKO ) mice and generated a novel line CBKO.5XFAD ( CBKOTg ) mice .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CBKO", "type": "GeneOrGeneProduct"}, {"text": "CBKO.5XFAD", "type": "GeneOrGeneProduct"}, {"text": "CBKOTg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Mutations found in the PTCH1 gene and neighboring repetitive sequences may have contributed to the development of the studied BCCs .

Example answer:
{"entities": [{"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : A heterozygous germline T to C transition in exon 10 of the TSHR gene ( c.1358T -- > C ) resulting in the substitution of methionine ( ATG ) by threonine ( ACG ) at codon 453 ( p.M453T ) was identified in the father and his two children .

Example answer:
{"entities": [{"text": "T to C", "type": "SequenceVariant"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}, {"text": "c.1358T -- > C", "type": "SequenceVariant"}, {"text": "methionine ( ATG ) by threonine ( ACG ) at codon 453", "type": "SequenceVariant"}, {"text": "p.M453T", "type": "SequenceVariant"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Anticipation in familial lattice corneal dystrophy type I with R124C mutation in the TGFBI ( BIGH3 ) gene .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "R124C", "type": "SequenceVariant"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "BIGH3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Input:
Sentence: This -4-bp transition , as well as 2 mutations previously linked with familial and sporadic chondrocalcinosis ( +14 bp C-to-T and C-terminal GAG deletion , respectively ) , but not the French familial chondrocalcinosis kindred 143-bp T-to-C mutation , increased reticulocyte ANKH transcription/ANKH translation in vitro .
