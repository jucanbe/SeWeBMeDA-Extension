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

## Item biored:test:316
Example input:
Sentence: Mutations leading to abrogation of matriptase-2 proteolytic activity in humans are associated with an iron-refractory iron deficiency anemia ( IRIDA ) due to elevated hepcidin levels .

Example answer:
{"entities": [{"text": "matriptase-2", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "iron-refractory iron deficiency anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IRIDA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepcidin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hypokalaemic periodic paralysis ( HypoPP ) is an autosomal dominant disorder , which is characterized by periodic attacks of muscle weakness associated with a decrease in the serum potassium level .

Example answer:
{"entities": [{"text": "Hypokalaemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal dominant disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscle weakness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "potassium", "type": "ChemicalEntity"}]}

Example input:
Sentence: The FH mutation database : an online database of fumarate hydratase mutations involved in the MCUL ( HLRCC ) tumor syndrome and congenital fumarase deficiency .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "fumarate hydratase", "type": "GeneOrGeneProduct"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HLRCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fumarase deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One-hundred and fifty HCM ( 90 sporadic hypertrophic cardiomyopathy [ SHCM ] and 60 familial hypertrophic cardiomyopathy [ FHCM ] ) patients and 165 age- and sex-matched normal healthy controls without known hypertension and left ventricular hypertrophy were included in the study .

Example answer:
{"entities": [{"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sporadic hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "familial hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular hypertrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Mutations affecting the intracellular domain of the GHR can result in GH insensitivity and IGF deficiency , despite normal serum concentrations of GHBP .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A major disease-causing gene for HypoPP has been identified as CACNA1S , which encodes the skeletal muscle calcium channel alpha-subunit with four transmembrane domains ( I-IV ) , each with six transmembrane segments ( S1-S6 ) .

Example answer:
{"entities": [{"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "skeletal muscle calcium channel alpha-subunit", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONTEXT : 17alpha-Hydroxylase deficiency is a rare form of congenital adrenal hyperplasia caused by CYP17 gene mutations .

Example answer:
{"entities": [{"text": "17alpha-Hydroxylase deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "congenital adrenal hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CYP17", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Nephronophthisis ( NPHP ) , a rare recessive cystic kidney disease , is the most frequent genetic cause of chronic renal failure in children and young adults .

Example answer:
{"entities": [{"text": "Nephronophthisis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cystic kidney disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chronic renal failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: INTRODUCTION : Hypertrophic cardiomyopathy ( HCM ) is a complex disorder and genetically transmitted cardiac disease with a diverse clinical course .

Example answer:
{"entities": [{"text": "Hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONTEXT : Hereditary hypophosphatemic rickets with hypercalciuria ( HHRH ) is a rare metabolic disorder , characterized by hypophosphatemia and rickets/osteomalacia with increased serum 1,25-dihydroxyvitamin D [ 1,25- ( OH ) ( 2 ) D ] resulting in hypercalciuria .

## Item biored:test:485
Example input:
Sentence: METHODS : We investigate whether the G-395A polymorphism of Klotho is associated with EH in a population consisting of 215 patients with EH and 220 non-hypertensive subjects .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The -930A > G polymorphism of the CYBA gene is associated with premature coronary artery disease .

Example answer:
{"entities": [{"text": "-930A > G", "type": "SequenceVariant"}, {"text": "CYBA", "type": "GeneOrGeneProduct"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A meta-analysis of previous and our present study revealed that this polymorphism is positively associated with adenocarcinoma , although suggestive associations were also found for squamous- and small-cell lung cancers .

Example answer:
{"entities": [{"text": "adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "squamous- and small-cell lung cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study showed that CFH was more likely to be AMD susceptibility gene at Chr.1q31 based on the finding that the CFHR1 and CFHR3 deletion was not polymorphic in the cohort of this study , and none of the SNPs that were significantly associated with AMD in a white population in C2 , CFB , and C3 genes showed a significant association with AMD .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We analyzed the nucleotidic sequence of the CYP2F1 gene in DNA samples from 90 French Caucasians consisting in 44 patients with lung cancer and 46 control individuals , using single-strand conformation polymorphism analysis of PCR products ( PCR-SSCP ) .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Two coding polymorphisms , 55M/L and 192Q/R , and a promoter variant , -107C/T , has been extensively studied with respect to susceptibility to CHD .

Example answer:
{"entities": [{"text": "55M/L", "type": "SequenceVariant"}, {"text": "192Q/R", "type": "SequenceVariant"}, {"text": "-107C/T", "type": "SequenceVariant"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , our preliminary results did not show any evidence that the CYP2F1 genetic polymorphism has implications in the pathogenesis of lung cancer .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using self-reported data on ischemic heart disease to evaluate the impact of the PON 192Q/R polymorphism on susceptibility to CHD , we found only a nonsignificant trend of 192RR homozygosity in women being a risk factor .

Example answer:
{"entities": [{"text": "ischemic heart disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PON", "type": "GeneOrGeneProduct"}, {"text": "192Q/R", "type": "SequenceVariant"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "192RR", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: In overall analysis , the homozygous Cys/Cys genotype showed a significant association with lung cancer compared to Ser allele carrier status ( odds ratio ( OR ) =1.31 , 95 % confidence interval ( CI ) =1.02-1.69 ) .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Analyses indicated no association between the NQO1 * 2 polymorphism and the risk of anthracycline-related CHF ( odds ratio [ OR ] , 1.04 ; P=.97 ) .

## Item biored:test:433
Example input:
Sentence: We describe in a BSS patient the first case of homozygous four bases deletion ( TGAG ) in the gpIbalpha gene coding sequence , leading to a premature stop codon .

Example answer:
{"entities": [{"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion ( TGAG )", "type": "SequenceVariant"}, {"text": "gpIbalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Novel CACNA1S mutation causes autosomal dominant hypokalemic periodic paralysis in a South American family .

Example answer:
{"entities": [{"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "hypokalemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We investigated clinical and cellular phenotypes of 24 children with mutations in the catalytic ( alpha ) subunit of the mitochondrial DNA ( mtDNA ) gamma polymerase ( POLG1 ) .

Example answer:
{"entities": [{"text": "mitochondrial DNA ( mtDNA ) gamma polymerase", "type": "GeneOrGeneProduct"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: With the advent of next-generation sequencing technologies , the homozygous mutations T71N and A190T in the neuronal calcium sensor ( NCS ) hippocalcin were identified as the genetic cause of primary isolated dystonia ( DYT2 dystonia ) .

Example answer:
{"entities": [{"text": "T71N", "type": "SequenceVariant"}, {"text": "A190T", "type": "SequenceVariant"}, {"text": "neuronal calcium sensor", "type": "GeneOrGeneProduct"}, {"text": "NCS", "type": "GeneOrGeneProduct"}, {"text": "hippocalcin", "type": "GeneOrGeneProduct"}, {"text": "primary isolated dystonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DYT2", "type": "GeneOrGeneProduct"}, {"text": "dystonia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Hypomorphic MKS3/TMEM67 mutations cause NPHP with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "NPHP with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that heterozygous loss-of-function mutations in PTPN11 are a frequent cause of MC , that lesions in patients with MC appear to arise following a `` second hit , '' that MC may be locus heterogeneous since 1 familial and 5 sporadically occurring cases lacked obvious disease-causing PTPN11 mutations , and that PTPN11 mutations are not a common cause of Ollier disease or Maffucci syndrome .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The mother and daughter were each heterozygous for PPARG nonsense mutation Y355X , whose protein product in vitro was transcriptionally inactive with no dominant-negative activity against the wild-type receptor .

Example answer:
{"entities": [{"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "Y355X", "type": "SequenceVariant"}]}

Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Previously , we and others reported that recessive mutations in the embryonal acetylcholine receptor g subunit ( CHRNG ) can cause both lethal and nonlethal MPS , thus demonstrating that pterygia resulted from fetal akinesia .

## Item biored:test:545
Example input:
Sentence: The polymorphism did not show any association with FHCM .

Example answer:
{"entities": [{"text": "FHCM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Other regions , such as the transactivation domain , seem to be slightly more polymorphic in the human population and the impact on functionality should be further examined .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Seven novel single-nucleotide polymorphisms ( SNPs ) were also found , of which a change of leucine 269 to phenylalanine ( Leu269Phe ) was found in 12 of 18 patients with the Arg555Trp mutation .

Example answer:
{"entities": [{"text": "leucine 269 to phenylalanine", "type": "SequenceVariant"}, {"text": "Leu269Phe", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Arg555Trp", "type": "SequenceVariant"}]}

Example input:
Sentence: The result of PCR associated with restriction fragment length polymorphism analysis also suggested that this mutation is heterozygous .

Example answer:
{"entities": []}

Example input:
Sentence: Whereas we confirmed lack of direct correlation between the clinical phenotype and the genotype , we also found that the so-called 'common mutation ' ( p.R50X ) accounted for about 43 % of alleles in our cohort and that no population-related mutations are clearly identified in Italian patients .

Example answer:
{"entities": [{"text": "p.R50X", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Polymerase chain reaction was carried out and single nucleotide polymorphisms of FGFR4 were identified by restriction enzyme digestion .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Similarly , NF1 alterations including homozygous deletions and splicing mutations were identified in 9 ( 22 % ) of 41 primary OSCs .

Example answer:
{"entities": [{"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: None of the studied polymorphisms alone affected overall or progression-free survival ( PFS ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Eighteen single nucleotide polymorphisms ( SNPs ) were identified , seven of which were missense , with no truncation or frame shift mutations .

Example answer:
{"entities": []}

Input:
Sentence: In conclusion , the majority of the detected sequence alterations were polymorphisms without obvious functional relevance .

## Item biored:test:522
Example input:
Sentence: We hypothesised that the G-395A polymorphism in the promoter region of the human Klotho gene may contribute to the prevalence of Essential Hypertension ( EH ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "Essential Hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONTEXT : Interindividual variations in glucocorticoid sensitivity have been associated with manifestations of cortisol excess or deficiency and may be partly explained by polymorphisms in the human glucocorticoid receptor ( hGR ) gene .

Example answer:
{"entities": [{"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "cortisol", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "glucocorticoid receptor", "type": "GeneOrGeneProduct"}, {"text": "hGR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : The G-395A polymorphism of the human Klotho gene is associated with EH and may be a potential regulatory site .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Atypical GH insensitivity syndrome and severe insulin-like growth factor-I deficiency resulting from compound heterozygous mutations of the GH receptor , including a novel frameshift mutation affecting the intracellular domain .

Example answer:
{"entities": [{"text": "GH insensitivity syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin-like growth factor-I deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: There are differential effects of age , gender and smoking status on the association of the G-395A polymorphism with EH ; the G-395A polymorphism is significantly associated with EH in subjects over 60years old , in females and in nonsmokers .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We investigate whether the G-395A polymorphism of Klotho is associated with EH in a population consisting of 215 patients with EH and 220 non-hypertensive subjects .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Mutations affecting the intracellular domain of the GHR can result in GH insensitivity and IGF deficiency , despite normal serum concentrations of GHBP .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND/AIMS : GH insensitivity and IGF deficiency may result from aberrations of the GH receptor ( GHR ) .

Example answer:
{"entities": [{"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}, {"text": "GHR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The aim of this study was to test if the IGF-1 gene polymorphisms are associated with the GH-dose of GH-deficient adults .

## Item biored:test:548
Example input:
Sentence: ETV6 proteins with mutations outside of amino acids 332-452 localize to the nucleus , whereas proteins with mutations within amino acids 332-452 remain in the cytoplasm .

Example answer:
{"entities": [{"text": "ETV6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This mutation consists of two consecutive substitutions ( 735-6 TG > AT ) that cause two nonsense mutations ( Y245X , G246X ) , inherited in an autosomal dominant fashion , on one parental chromosome .

Example answer:
{"entities": [{"text": "735-6 TG > AT", "type": "SequenceVariant"}, {"text": "Y245X", "type": "SequenceVariant"}, {"text": "G246X", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation caused protein truncation , and represents a novel case of consecutive nonsense mutations in human disease .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Both mutations reside in the tetratricopeptide repeats of OGT that are essential for substrate recognition .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : In this family , a heterozygous cytosine insertion in exon 10 ( c.1546_1547insC ) inducing a frame shift mutation of MEN1 was found in the proband and the other two suffering members of his family .

Example answer:
{"entities": [{"text": "cytosine insertion", "type": "SequenceVariant"}, {"text": "c.1546_1547insC", "type": "SequenceVariant"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Example input:
Sentence: This is the first known constitutional rearrangement of SYT14 , and further systematic genetic analysis and clinical studies of DGAP128 may offer unique insights into the role of SYT14 in neurodevelopment .

Example answer:
{"entities": [{"text": "SYT14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The two transversions resulted in the substitution of a stop codon for glutamine at codon 298 ( p.Q298X ) and a missense mutation at codon 358 , tyrosine to histidine ( p.Y358H ) .

Example answer:
{"entities": [{"text": "stop codon for glutamine at codon 298", "type": "SequenceVariant"}, {"text": "p.Q298X", "type": "SequenceVariant"}, {"text": "codon 358 , tyrosine to histidine", "type": "SequenceVariant"}, {"text": "p.Y358H", "type": "SequenceVariant"}]}

Example input:
Sentence: ETV6 , or Translocation-Ets-Leukemia ( TEL ) , is an ETS family transcriptional repressor that is essential for establishing hematopoiesis in neonatal bone marrow , and is frequently a target of chromosomal translocations in human cancer .

Example answer:
{"entities": [{"text": "ETV6", "type": "GeneOrGeneProduct"}, {"text": "Translocation-Ets-Leukemia", "type": "GeneOrGeneProduct"}, {"text": "TEL", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We propose that the alteration in the replication/nuclear location pattern of the non-deleted TDR22 indicates an altered gene regulation hence an altered transcritpion in DGS/VCFS .

Example answer:
{"entities": [{"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Insertional translocations ( IT ) are rare structural rearrangements .

## Item biored:test:550
Example input:
Sentence: Haplotype analysis suggests a germline mosaicism of the 2-bp deletion in the maternal grandmother of both affected individuals .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The authors obtained a significant maximum parametric LOD ( logarithm of odds ) score of Z ( max ) = 3.72 on chromosome 8q22 and identified a homozygous missense mutation in the gene MKS3/TMEM67 .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Two additional loci displayed an evidence of linkage ( LOD > 3 ) and included a locus on 16p13 , proximal to the gene encoding NDE1 , which has been shown to biologically interact with DISC1 .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "DISC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : We have confirmed the localization of the congenital microcoria locus ( MCOR ) to 13q31-q32 in a large Asian Indian family and conclude that current information suggests this is a single locus disorder and genetically homogeneous .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Multipoint analysis revealed a 4 cM region encompassing D13S1300 to D13S1280 where the LOD remains just over 6.0 Thus we confirm localization of the congenital microcoria locus to chromosomal locus 13q31-q32 .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The mutations concordantly segregate in all available families according a recessive mode of inheritance .

Example answer:
{"entities": []}

Example input:
Sentence: In the current study , a three generation Asian Indian family with 15 congenital microcoria ( pupils with a diameter < 2 mm ) affected members was studied for linkage to candidate microsatellite markers at the 13q31-q32 locus .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A disease co-segregating haplotype was detected in two hereditary autosomal dominant cases .

Example answer:
{"entities": []}

Example input:
Sentence: Linkage to the chromosomal locus 13q31-q32 has previously been reported in a large French family .

Example answer:
{"entities": []}

Input:
Sentence: We describe an IT between chromosomes 3 and 13 segregating in a three-generation pedigree .

## Item biored:test:511
Example input:
Sentence: We conclude that the SNPs of SLC2A2 predict the conversion to diabetes in obese subjects with IGT .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results suggest that TNMD polymorphisms are associated with adiposity and also with glucose metabolism and conversion from IGT to T2D in men .

Example answer:
{"entities": [{"text": "TNMD", "type": "GeneOrGeneProduct"}, {"text": "adiposity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: None of the SNPs or indels were associated with diabetes-related traits or accounted for a previously identified quantitative trait locus on chromosome 13 for fasting serum glucose .

Example answer:
{"entities": [{"text": "diabetes-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: Polymorphisms in the SLC2A2 ( GLUT2 ) gene are associated with the conversion from impaired glucose tolerance to type 2 diabetes : the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Measured genotype analysis tested associations between SNPs and obesity and diabetes-related traits .

Example answer:
{"entities": [{"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes-related", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Common single nucleotide polymorphisms ( SNPs ) within this gene , rs6232 and rs6235 , are associated with obesity .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using individual-level data from 120,286 participants in the UK Biobank and summary association results from four large-scale genome-wide association studies , we examined the impact of this variant on cardiometabolic traits , type 2 diabetes , and coronary heart disease .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our aim was to study the associations of individual single nucleotide polymorphisms and haplotypes with adiposity , glucose metabolism , and the risk of type 2 diabetes ( T2D ) .

Example answer:
{"entities": [{"text": "adiposity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: According to recent genome-wide association studies , a number of single nucleotide polymorphisms ( SNPs ) are reported to be associated with type 2 diabetes mellitus ( T2DM ) .

## Item biored:test:515
Example input:
Sentence: In overall analysis , the homozygous Cys/Cys genotype showed a significant association with lung cancer compared to Ser allele carrier status ( odds ratio ( OR ) =1.31 , 95 % confidence interval ( CI ) =1.02-1.69 ) .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We also observed associations for candidate SNPs in CRP , GSTP1 , and IL1B .

Example answer:
{"entities": [{"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using the two Asian cohorts , significant association of FCGR2B-232Thr/Thr with SLE was observed only in the presence of CD72- * 1/ * 1 genotype ( OR 4.63 , 95 % CI 1.47-14.6 , P=0.009 versus FCGR2B-232Ile/Ile plus CD72- * 2/ * 2 ) .

Example answer:
{"entities": [{"text": "FCGR2B-232Thr/Thr", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "FCGR2B-232Ile/Ile", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A significant association of the rs729302 A allele with RA susceptibility was found in both sets ( odds ratio ( OR ) 1.22 , 95 % CI 1.09 to 1.35 , p < 0.001 in the combined analysis ) .

Example answer:
{"entities": [{"text": "rs729302", "type": "SequenceVariant"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The non-synonymous SNP rs2230912 ( resulting in amino-acid polymorphism Q460R ) showed the strongest association and has been postulated to be pathogenically relevant .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "Q460R", "type": "SequenceVariant"}]}

Example input:
Sentence: The most strongly associated SNP with SLE was the rs9271366 ( odds ratio , OR = 1.70 , p = 5.6 10 ( -5 ) ) near the HLA-DRB1 gene .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}, {"text": "HLA-DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : We found that the presence of the -1021T allele was associated with AD : odds ratio = 1.2 ( 95 % confidence interval : 1.06-1.4 , p = 0.005 ) .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The strongest association was found in a variant of CDKAL1 [ rs7754840 , odds ratio ( OR ) = 1.77 , 95 % CI = 1.50-2.10 , p = 5.0 x 10 ( -11 ) ] .

## Item biored:test:551
Example input:
Sentence: TS genotyping methods were polymerase chain reaction ( PCR ) for VNTR and PCR , followed by restriction length fragment polymorphism ( PCR-RFLP ) for SNP and ins/del 6 bp .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "ins/del 6 bp", "type": "SequenceVariant"}]}

Example input:
Sentence: In order to explain the reduced genetic heterogeneity detected by Alu insertions among Basque subpopulations , values of the Wright 's F ( ST ) statistic were estimated for both Alu markers and a set of short tandem repeats ( STRs ) in terms of two geographical scales : ( 1 ) the Basque Country , ( 2 ) Europe ( including Basques ) .

Example answer:
{"entities": []}

Example input:
Sentence: Microsatellite markers at 13q31-q32 were PCR amplified and run on an ABI Prism 310 genetic analyzer and genotyped with the GeneScan analysis .

Example answer:
{"entities": []}

Example input:
Sentence: By multipoint linkage analysis with markers spanning the entire X-chromosome we mapped the disease locus to a 28-Mb interval between Xp11.4 and Xq12 , including the BCOR gene .

Example answer:
{"entities": [{"text": "BCOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: An 18 kb genomic clone hybridizing with the h mu OR1 cDNA contains 63 and 489 bp exonic sequences flanked by splice donor/acceptor sequences .

Example answer:
{"entities": [{"text": "h mu OR1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Analysis of hybridization to DNA prepared from human rodent hybrid cell lines and chromosomal in situ hybridization studies indicate localization to 6q24-25 .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Exonic and intronic segments , 5 ' and 3 ' flanking regions of IRS2 ( 14.5 kb ) , were bidirectionally sequenced for single nucleotide polymorphism ( SNP ) discovery in 934 Hispanic children using 3730XL DNA Sequencers .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: The phenotype co-segregates with short-tandem repeat markers flanking the TMC1 gene at the DFNA36 locus on chromosome 9q31-q21 .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "DFNA36", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A 28 bp variable number of tandem repeats ( VNTR ) , a G/C single nucleotide polymorphism ( SNP ) , and a deletion of 6 bp at position 1494 were studied .

Example answer:
{"entities": [{"text": "28 bp variable number of tandem repeats", "type": "SequenceVariant"}, {"text": "G/C", "type": "SequenceVariant"}, {"text": "deletion of 6 bp at position 1494", "type": "SequenceVariant"}]}

Input:
Sentence: Short tandem repeat ( STR ) segregation analysis and array-comparative genomic hybridization were used to define the IT as a 25.1 Mb segment spanning 13q21.2-q31.1 .

## Item biored:test:520
Example input:
Sentence: Genome-wide association studies have identified genomic loci , whose single-nucleotide polymorphisms ( SNPs ) predispose to prostate cancer ( PCa ) .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Two microsatellites , 1 insertion/deletion , and 8 single nucleotide polymorphisms ( SNPs ) in the regulatory region of iNOS were genotyped in 200 POAG patients and 200 age-matched controls .

Example answer:
{"entities": [{"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We investigated the association between chronic ITP and the frequency of the single-nucleotide polymorphism rs763780 ( 7488T/C ) , which causes a His-to-Arg substitution at amino acid 161 .

Example answer:
{"entities": [{"text": "chronic ITP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs763780", "type": "SequenceVariant"}, {"text": "7488T/C", "type": "SequenceVariant"}, {"text": "His-to-Arg substitution at amino acid 161", "type": "SequenceVariant"}]}

Example input:
Sentence: We hypothesised that the G-395A polymorphism in the promoter region of the human Klotho gene may contribute to the prevalence of Essential Hypertension ( EH ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "Essential Hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: None of the SNPs or indels were associated with diabetes-related traits or accounted for a previously identified quantitative trait locus on chromosome 13 for fasting serum glucose .

Example answer:
{"entities": [{"text": "diabetes-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: Plasminogen activator inhibitor type 1 serum levels and 4G/5G gene polymorphism in morbidly obese Hispanic patients with non-alcoholic fatty liver disease .

Example answer:
{"entities": [{"text": "Plasminogen activator inhibitor type 1", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A potential regulatory single nucleotide polymorphism in the promoter of the Klotho gene may be associated with essential hypertension in the Chinese Han population .

Example answer:
{"entities": [{"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "essential hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Common single nucleotide polymorphisms ( SNPs ) within this gene , rs6232 and rs6235 , are associated with obesity .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: AIMS : Several SNPs and a microsatellite cytosine-adenine repeat promoter polymorphism of the IGF-1 gene have been reported to be associated with circulating IGF-1 serum concentrations .

