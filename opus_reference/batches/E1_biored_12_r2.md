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

## Item biored:test:528
Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although only limited subjects were investigated , our results suggested that a genetic polymorphism in ABCG2 might alter the transport activity for the drug and elevate the systemic circulation level of irinotecan , leading to severe myelosuppression .

Example answer:
{"entities": [{"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "irinotecan", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genetic Variation at the Sulfonylurea Receptor , Type 2 Diabetes , and Coronary Heart Disease .

Example answer:
{"entities": [{"text": "Sulfonylurea Receptor", "type": "GeneOrGeneProduct"}, {"text": "Type 2 Diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Coronary Heart Disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The mutant receptor hGRalphaD401H enhances the transcriptional activity of glucocorticoid-responsive genes .

Example answer:
{"entities": [{"text": "hGRalphaD401H", "type": "GeneOrGeneProduct"}, {"text": "glucocorticoid-responsive genes", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Treatment with recombinant DNA-derived IGF-I resulted in growth acceleration .

Example answer:
{"entities": [{"text": "IGF-I", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Atypical GH insensitivity syndrome and severe insulin-like growth factor-I deficiency resulting from compound heterozygous mutations of the GH receptor , including a novel frameshift mutation affecting the intracellular domain .

Example answer:
{"entities": [{"text": "GH insensitivity syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin-like growth factor-I deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Mutations affecting the intracellular domain of the GHR can result in GH insensitivity and IGF deficiency , despite normal serum concentrations of GHBP .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONTEXT : Interindividual variations in glucocorticoid sensitivity have been associated with manifestations of cortisol excess or deficiency and may be partly explained by polymorphisms in the human glucocorticoid receptor ( hGR ) gene .

Example answer:
{"entities": [{"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "cortisol", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "glucocorticoid receptor", "type": "GeneOrGeneProduct"}, {"text": "hGR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND/AIMS : GH insensitivity and IGF deficiency may result from aberrations of the GH receptor ( GHR ) .

Example answer:
{"entities": [{"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}, {"text": "GHR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Therefore , genetic variations of the IGF-1 gene seem not to be major influencing factors of the GH-IGF-axis causing variable response to exogenous GH-treatment .

## Item biored:test:441
Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: Four patients harbor yet non-described SRD5A2 gene mutations : a single nucleotide deletion ( del642T ) , a G158R amino acid substitution , a splice junction mutation ( IVS3+1G > A ) , and the insertion of a cytosine ( 217_218insC ) occurring at a CCCC motif .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G158R", "type": "SequenceVariant"}, {"text": "IVS3+1G > A", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}]}

Example input:
Sentence: Sequencing of the GJB2 gene showed that the child was heterozygous for a novel nucleotide change , c.263C > T , in exon 2 , leading to a substitution of alanine for valine at position 88 ( p.Ala88Val ) .

Example answer:
{"entities": [{"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "c.263C > T", "type": "SequenceVariant"}, {"text": "alanine for valine at position 88", "type": "SequenceVariant"}, {"text": "p.Ala88Val", "type": "SequenceVariant"}]}

Example input:
Sentence: Whereas no mutations were detected in the PDE6H gene , mutations in KCNV2 were identified in all patients , in either the homozygous or compound heterozygous state .

Example answer:
{"entities": [{"text": "PDE6H", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We detected a novel , single , heterozygous nucleotide ( G -- > C ) substitution at position 1201 ( exon 2 ) of the hGR gene , which resulted in aspartic acid to histidine substitution at amino acid position 401 in the amino-terminal domain of the hGRalpha .

Example answer:
{"entities": [{"text": "( G -- > C ) substitution at position 1201", "type": "SequenceVariant"}, {"text": "hGR", "type": "GeneOrGeneProduct"}, {"text": "aspartic acid to histidine substitution at amino acid position 401", "type": "SequenceVariant"}, {"text": "hGRalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Another POF patient of African origin showed a homozygous nucleotide change in the tenth of DMC1 gene that led to an alteration of the amino acid composition of the protein ( M200V ) .

Example answer:
{"entities": [{"text": "POF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "M200V", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation resulted in replacement of a non-polar amino acid ( proline ) with a polar amino acid ( serine ) at position 29 ( P29S ) .

Example answer:
{"entities": [{"text": "( proline ) with a polar amino acid ( serine ) at position 29", "type": "SequenceVariant"}, {"text": "P29S", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutation analysis of the plakophilin 1 gene PKP1 revealed a homozygous deletion of C at nucleotide 888 within exon 5 .

Example answer:
{"entities": [{"text": "plakophilin 1", "type": "GeneOrGeneProduct"}, {"text": "PKP1", "type": "GeneOrGeneProduct"}, {"text": "deletion of C at nucleotide 888", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : A single heterozygous missense mutation , substitution of a cytosine residue with thymidine in exon 2 of MSH5 , was found in two Caucasian women in whom POF developed at 18 and 36 years of age .

Example answer:
{"entities": [{"text": "cytosine residue with thymidine", "type": "SequenceVariant"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this report the distribution of the exonic G/A single nucleotide polymorphism ( SNP ) in purine nucleoside phosphorylase ( PNP ) gene , resulting in the amino acid substitution serine to glycine at position 51 ( G51S ) , was investigated in a large population of AD patients ( n=321 ) and non-demented control ( n=208 ) .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "purine nucleoside phosphorylase", "type": "GeneOrGeneProduct"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "serine to glycine at position 51", "type": "SequenceVariant"}, {"text": "G51S", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: RESULTS : We identified a patient homozygous for a nucleotide change c.1445T > G , resulting in a novel homozygous substitution of the non-polar hydrophobic phenylalanine to the polar hydrophilic cysteine in exon 6 at codon 482 ( p.F482C ) of the PKD2 gene and a de-novo PKD1 splice-site variant IVS21-2delAG .

## Item biored:test:536
Example input:
Sentence: Disruption of the temporally regulated cloaca endodermal b-catenin signaling causes anorectal malformations .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "anorectal malformations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Testis morphology showed that , during early infancy , the 5-alpha-reductase enzyme deficiency may not have affected interstitial or tubular development .

Example answer:
{"entities": [{"text": "5-alpha-reductase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Also known as Goltz syndrome , FDH presents with characteristic linear streaks of hypoplastic dermis and variable abnormalities of bone , nails , hair , limbs , teeth and eyes .

Example answer:
{"entities": [{"text": "Goltz syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoplastic dermis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although congenital malformations , such as anorectal malformations ( ARMs ) , are frequently observed during this process , the underlying pathogenic mechanisms remain unclear .

Example answer:
{"entities": [{"text": "congenital malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anorectal malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARMs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A patient of Chinese origin with ambiguous genitalia at 14 months , a 46 , XY karyotype , and normal T secretion under human chorionic gonadotropin ( hCG ) stimulation underwent a gonadectomy at 20 months .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "T", "type": "ChemicalEntity"}, {"text": "human chorionic gonadotropin", "type": "ChemicalEntity"}, {"text": "hCG", "type": "ChemicalEntity"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both b-catenin loss- and gain-of-function ( LOF and GOF ) mutants displayed abnormal clefts in the perineal region and hypoplastic elongation of the URS .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "hypoplastic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations of the steroid 5alpha-reductase type 2 ( SRD5A2 ) gene in 46 , XY subjects cause masculinization defects of varying degrees , due to reduced or impaired enzymatic activity .

Example answer:
{"entities": [{"text": "steroid 5alpha-reductase type 2", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Defect in androgen action on the target tissues or production of active metabolite share common morphological features .

Example answer:
{"entities": []}

Example input:
Sentence: Defects in these organelles cause inherited human disorders ( ciliopathies ) such as retinitis pigmentosa and Bardet-Biedl syndrome ( BBS ) , frequently affecting many physiological and developmental processes across multiple organs .

Example answer:
{"entities": [{"text": "inherited human disorders", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ciliopathies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "retinitis pigmentosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bardet-Biedl syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BBS", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In contrast to disorders of sexual differentiation caused by lack of androgen production or inhibited androgen action , defects affecting development of the bipotent genital anlagen have rarely been investigated in humans .

## Item biored:test:508
Example input:
Sentence: SEREX screening of cDNA expression libraries derived from 3 breast cancer patients identified a total of 88 positive clones ( bcg-1 to bcg-88 ) , including 27 hitherto unknown sequences .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : We identified in ACC CD133-positive CSC that expressed NOTCH1 and SOX10 , formed spheroids , and initiated tumors in nude mice .

Example answer:
{"entities": [{"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD133-positive", "type": "GeneOrGeneProduct"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Tumor TS 1494del6 genotype may be a prognostic factor in FU-based adjuvant treatment of colorectal cancer patients .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "1494del6", "type": "SequenceVariant"}, {"text": "FU-based", "type": "ChemicalEntity"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : These results indicate that ADAM12 actively supports the CSC phenotype in claudin-low breast cancer cells via modulation of the EGFR pathway .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "claudin-low", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : These data provide strong support for the hypothesis that common variation in GPX4 is associated with prognosis after a diagnosis of breast cancer .

Example answer:
{"entities": [{"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSION : It is possible that CCND3 rs2479717 , or another variant it tags , is associated with prognosis after a diagnosis of breast cancer .

## Item biored:test:519
Example input:
Sentence: Treatment with recombinant DNA-derived IGF-I resulted in growth acceleration .

Example answer:
{"entities": [{"text": "IGF-I", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONTEXT : Interindividual variations in glucocorticoid sensitivity have been associated with manifestations of cortisol excess or deficiency and may be partly explained by polymorphisms in the human glucocorticoid receptor ( hGR ) gene .

Example answer:
{"entities": [{"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "cortisol", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "glucocorticoid receptor", "type": "GeneOrGeneProduct"}, {"text": "hGR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We hypothesised that the G-395A polymorphism in the promoter region of the human Klotho gene may contribute to the prevalence of Essential Hypertension ( EH ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "Essential Hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The G-395A polymorphism of the human Klotho gene is associated with EH and may be a potential regulatory site .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: There are differential effects of age , gender and smoking status on the association of the G-395A polymorphism with EH ; the G-395A polymorphism is significantly associated with EH in subjects over 60years old , in females and in nonsmokers .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We investigate whether the G-395A polymorphism of Klotho is associated with EH in a population consisting of 215 patients with EH and 220 non-hypertensive subjects .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : Mutations affecting the intracellular domain of the GHR can result in GH insensitivity and IGF deficiency , despite normal serum concentrations of GHBP .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Atypical GH insensitivity syndrome and severe insulin-like growth factor-I deficiency resulting from compound heterozygous mutations of the GH receptor , including a novel frameshift mutation affecting the intracellular domain .

Example answer:
{"entities": [{"text": "GH insensitivity syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin-like growth factor-I deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND/AIMS : GH insensitivity and IGF deficiency may result from aberrations of the GH receptor ( GHR ) .

Example answer:
{"entities": [{"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}, {"text": "GHR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Growth hormone dose in growth hormone-deficient adults is not associated with IGF-1 gene polymorphisms .

## Item biored:test:431
Example input:
Sentence: In addition to hyperthyroidism , ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers were consistently found in all affected individuals .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Twenty-one had Alpers syndrome , the commonest severe POLG1 autosomal recessive phenotype , comprising hepatoencephalopathy and often mtDNA depletion .

Example answer:
{"entities": [{"text": "Alpers syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}, {"text": "hepatoencephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Myotonic dystrophy ( DM ) , the most prevalent muscular disorder in adults , is caused by ( CTG ) n-repeat expansion in a gene encoding a protein kinase ( DM protein kinase ; DMPK ) and involves changes in cytoarchitecture and ion homeostasis .

Example answer:
{"entities": [{"text": "Myotonic dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscular disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM protein kinase", "type": "GeneOrGeneProduct"}, {"text": "DMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Loss-of-function mutations in PTPN11 cause metachondromatosis , but not Ollier disease or Maffucci syndrome .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "metachondromatosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that heterozygous loss-of-function mutations in PTPN11 are a frequent cause of MC , that lesions in patients with MC appear to arise following a `` second hit , '' that MC may be locus heterogeneous since 1 familial and 5 sporadically occurring cases lacked obvious disease-causing PTPN11 mutations , and that PTPN11 mutations are not a common cause of Ollier disease or Maffucci syndrome .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Oculopharyngeal muscular dystrophy ( OPMD ) is a late onset autosomal dominant muscle disorder .

Example answer:
{"entities": [{"text": "Oculopharyngeal muscular dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal dominant muscle disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Metachondromatosis ( MC ) is a rare , autosomal dominant , incompletely penetrant combined exostosis and enchondromatosis tumor syndrome .

Example answer:
{"entities": [{"text": "Metachondromatosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "exostosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "enchondromatosis tumor syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Analysis of a nuclear family with three affected offspring identified an autosomal-recessive form of spondyloepimetaphyseal dysplasia characterized by severe short stature and a unique constellation of radiographic findings .

Example answer:
{"entities": [{"text": "spondyloepimetaphyseal dysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "short stature", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MC is clinically distinct from other multiple exostosis or multiple enchondromatosis syndromes and is unlinked to EXT1 and EXT2 , the genes responsible for autosomal dominant multiple osteochondromas ( MO ) .

Example answer:
{"entities": [{"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "multiple exostosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "multiple enchondromatosis syndromes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EXT1", "type": "GeneOrGeneProduct"}, {"text": "EXT2", "type": "GeneOrGeneProduct"}, {"text": "multiple osteochondromas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MO", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Multiple pterygium syndromes ( MPS ) comprise a group of multiple congenital anomaly disorders characterized by webbing ( pterygia ) of the neck , elbows , and/or knees and joint contractures ( arthrogryposis ) .

## Item biored:test:574
Example input:
Sentence: Genomic DNA was extracted from blood samples , and DNA fragments containing the site of polymorphism were amplified by PCR .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA extracted from peripheral blood was amplified by polymerase chain reaction ( PCR ) method and the exons of all candidate genes were sequenced .

Example answer:
{"entities": []}

Example input:
Sentence: DNA was extracted from the blood drawn from 399 prostate cancer patients , 150 BPH patients and 294 healthy community controls .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: EXPERIMENTAL DESIGN : Genomic DNA was purified from peripheral blood mononuclear cells or tissue specimens .

Example answer:
{"entities": []}

Example input:
Sentence: After informed consent was obtained , genomic DNA was extracted from the venous blood of all participants .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA was isolated from the leukocytes and genotyping was performed using the Sequenom platform .

Example answer:
{"entities": []}

Example input:
Sentence: DNA was isolated from peripheral blood and genotyping was performed with PCR-based methods .

Example answer:
{"entities": []}

Example input:
Sentence: Peripheral blood samples were collected and genomic DNA was extracted from the leukocytes .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA was isolated from the venous blood leukocytes of 322 unrelated patients with schizophrenia , 156 patients with depression , 300 patients with heroin addiction , and 300 healthy unrelated individuals .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genomic DNA was isolated from the white blood cells of all family members of the affected case following standard established protocols .

Example answer:
{"entities": []}

Input:
Sentence: Blood samples were obtained from all patients and genomic DNA was isolated .

## Item biored:test:434
Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conclude that heterozygous loss-of-function mutations in PTPN11 are a frequent cause of MC , that lesions in patients with MC appear to arise following a `` second hit , '' that MC may be locus heterogeneous since 1 familial and 5 sporadically occurring cases lacked obvious disease-causing PTPN11 mutations , and that PTPN11 mutations are not a common cause of Ollier disease or Maffucci syndrome .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Novel CACNA1S mutation causes autosomal dominant hypokalemic periodic paralysis in a South American family .

Example answer:
{"entities": [{"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "hypokalemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Recent reports have demonstrated that mutations in the OPHN1 gene were responsible for a syndromic rather than non-specific mental retardation .

Example answer:
{"entities": [{"text": "OPHN1", "type": "GeneOrGeneProduct"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report here a new family with X-linked mental retardation due to mutation in OPHN1 and present unpublished data about two families previously reported , concerning the facial and psychological phenotype of affected males and carrier females .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPHN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The mother and daughter were each heterozygous for PPARG nonsense mutation Y355X , whose protein product in vitro was transcriptionally inactive with no dominant-negative activity against the wild-type receptor .

Example answer:
{"entities": [{"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "Y355X", "type": "SequenceVariant"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Input:
Sentence: We hypothesized that mutations in acetylcholine receptor-related genes might also result in a MPS/fetal akinesia phenotype and so we analyzed 15 cases of lethal MPS/fetal akinesia without CHRNG mutations for mutations in the CHRNA1 , CHRNB1 , CHRND , and rapsyn ( RAPSN ) genes .

## Item biored:test:576
Example input:
Sentence: Moderate or severe adverse events were more common in subjects on clonidine ( 79.4 % versus 49.2 % ; p =.0006 ) but not associated with higher rates of early study withdrawal .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Eighty-one percent of patients with dyskinesia had clinical fluctuations .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : In a pooled analysis of 1460 ICH and 3817 IS/TIA , MB were more frequent in ICH vs IS/TIA in all treatment groups , but the excess increased from 2.8 ( odds ratio ; range , 2.3-3.5 ) in nonantithrombotic users to 5.7 ( range , 3.4-9.7 ) in antiplatelet users and 8.0 ( range , 3.5-17.8 ) in warfarin users ( P difference=0.01 ) .

Example answer:
{"entities": [{"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: We therefore examined the associations with AD of the DBH -1021T allele and of the above interactions in the Epistasis Project , with 1757 cases of AD and 6294 elderly controls .

Example answer:
{"entities": [{"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "-1021T", "type": "SequenceVariant"}]}

Example input:
Sentence: A statistically significant difference in allele frequency between cases and controls was observed for 2 of the SNPs ( +3100 T/G and +8365 C/T ) , with an odds ratio of 0.78 ( 95 % CI=0.64-0.96 ) and 0.65 ( 95 % CI=0.45-0.94 ) respectively .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Study results showed that myoclonus incidence was 85 % , 40 % , 70 % , and 25 % in Group NP , Group F , Group M , and Group FM , respectively , and were significantly lower in Group F and Group FM .

Example answer:
{"entities": [{"text": "myoclonus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have investigated this gene in a large UK case-control sample ( bipolar I disorder N = 687 , unipolar recurrent major depression N = 1,036 , controls N = 1,204 ) .

Example answer:
{"entities": [{"text": "bipolar I disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "unipolar recurrent major depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: D allelic was significantly associated with DDD ( p value = 0.027 , odds ratio = 1.41 with 95 % CI = 1.04-1.90 ) while Genotypic association on the presence of D allele was also significantly associated with DDD ( p value = 0.046 , odds ratio = 1.50 with 95 % CI = 1.01-2.24 ) .

Example answer:
{"entities": [{"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Significantly lower frequency of the A-C-C-G with higher frequency of A-C-A-G haplotypes was also noticed in subjects with DS ( P value =0.02089 and 0.00588 respectively ) .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Twenty-four of 113 ( 21 % ) gastric cancer patients had the II , 57 ( 51 % ) the ID , and 32 ( 28 % ) the DD genotype .

Example answer:
{"entities": [{"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: In the control subjects , the frequency of DD was 18.8 % ( n = 18 ) , ID was 50 % ( n = 48 ) and II was 31.3 % ( n = 30 ) .

## Item biored:test:531
Example input:
Sentence: The boy developed intraventricular and intracerebral haemorrhage , leading to hydrocephalus .

Example answer:
{"entities": [{"text": "intraventricular and intracerebral haemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hydrocephalus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prolonged hypothermia as a bridge to recovery for cerebral edema and intracranial hypertension associated with fulminant hepatic failure .

Example answer:
{"entities": [{"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracranial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fulminant hepatic failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Twenty-one of the 24 patients did not have evidence of new cerebral ischemic injury , but seizures were likely due to ischemic brain injury in 3 patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cerebral ischemic injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic brain injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : The rate of major hemorrhage was high in this old , frail group , but excluding fatalities , resulted in no long-term sequelae , and the stroke rate on warfarin was low , demonstrating how effective warfarin treatment is .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND AND PURPOSE : Cerebral microbleeds ( MB ) are potential risk factors for intracerebral hemorrhage ( ICH ) , but it is unclear if they are a contraindication to using antithrombotic drugs .

Example answer:
{"entities": [{"text": "Cerebral microbleeds", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antithrombotic drugs", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Warfarin-associated intracerebral hemorrhage ( W-ICH ) is a severe type of stroke .

Example answer:
{"entities": [{"text": "Warfarin-associated", "type": "ChemicalEntity"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "W-ICH", "type": "ChemicalEntity"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Intracerebral hemorrhage ( ICH ) is a devastating disease without effective treatment .

Example answer:
{"entities": [{"text": "Intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Intracranial hemorrhage has been reported in a small number of OI patients .

## Item biored:test:540
Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Nine distinct mutations including one small deletion mutation ( 46delS ) , two small insertion mutations ( 118-119insA and 125-126insAA ) , and six non-synonymous mutations ( A6V , P163S , E359K , P407Q , S429T and A442V ) were identified in 12 of the 486 patients ( nine with ventricular septal defect , two with Tetralogy of Fallot , and one with endocardial cushion defect ) .

Example answer:
{"entities": [{"text": "46delS", "type": "SequenceVariant"}, {"text": "118-119insA", "type": "SequenceVariant"}, {"text": "125-126insAA", "type": "SequenceVariant"}, {"text": "A6V", "type": "SequenceVariant"}, {"text": "P163S", "type": "SequenceVariant"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "P407Q", "type": "SequenceVariant"}, {"text": "S429T", "type": "SequenceVariant"}, {"text": "A442V", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Tetralogy of Fallot", "type": "DiseaseOrPhenotypicFeature"}, {"text": "endocardial cushion defect", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Included were 5,128 CL/P cases , 1,745 CPO cases , and 3,712 controls ( like-sexed , non-malformed liveborn infant , born immediately after a malformed one , in the same hospital ) , over 4,199,630 consecutive births .

Example answer:
{"entities": [{"text": "CL/P", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CPO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Of them , two patients carrying E359K mutation were from two generations in one family with ventricular septal defect ( VSD ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Seven hundred fifty three subjects , corresponding to 251 full trios of childhood-onset SLE families , were genotyped and analyzed using transmission disequilibrium testing ( TDT ) and multitest corrections .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Non-predefined geographical areas with significantly unusual cleft BPRs were identified with Kulldorf and Nagarwalla 's spatial scan statistic , employing number of cases and births , and exact location of each hospital .

Example answer:
{"entities": []}

Example input:
Sentence: The aim of this work was to search for unequal birth prevalence rates ( BPRs ) of cleft lip +/- cleft palate ( CL/P ) , and cleft palate only ( CPO ) , among different geographic areas in South America , and to analyze phenotypic characteristics and associated risk factors in each identified cluster .

Example answer:
{"entities": [{"text": "cleft lip", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cleft palate", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CL/P", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CPO", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Eighteen children with DSD and cleft palate were identified in the L beck DSD database ( about 1,500 entries ) .

