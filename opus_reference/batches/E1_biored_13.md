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

## Item biored:test:349
Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Keratitis-ichthyosis-deafness ( KID ) syndrome is a rare congenital ectodermal disorder , caused by heterozygous missense mutation in GJB2 , encoding the gap junction protein connexin 26 .

Example answer:
{"entities": [{"text": "Keratitis-ichthyosis-deafness ( KID ) syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "congenital ectodermal disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "connexin 26", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel mutation in the connexin 26 gene ( GJB2 ) in a child with clinical and histological features of keratitis-ichthyosis-deafness ( KID ) syndrome .

Example answer:
{"entities": [{"text": "connexin 26", "type": "GeneOrGeneProduct"}, {"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "keratitis-ichthyosis-deafness ( KID ) syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The patient ( TJ ) presented with a generalized seizure associated with hypoglycemia and hypokalemia .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A patient of Chinese origin with ambiguous genitalia at 14 months , a 46 , XY karyotype , and normal T secretion under human chorionic gonadotropin ( hCG ) stimulation underwent a gonadectomy at 20 months .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "T", "type": "ChemicalEntity"}, {"text": "human chorionic gonadotropin", "type": "ChemicalEntity"}, {"text": "hCG", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 3-year-old Chinese boy presented with prominent clinical features of malonic aciduria , including developmental delay , short stature , brain abnormalities and massive excretion of malonic acid and methylmalonic acid .

Example answer:
{"entities": [{"text": "malonic aciduria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "short stature", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "malonic acid", "type": "ChemicalEntity"}, {"text": "methylmalonic acid", "type": "ChemicalEntity"}]}

Example input:
Sentence: This report describes a patient with mild language delay and mental retardation , who was found to have nonketotic hyperglycinemia following her presentation with acute encephalopathy and chorea shortly after initiation of valproate therapy .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "language delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nonketotic hyperglycinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chorea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "valproate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We report a case of Gitelman syndrome ( GS ) in a dizygotic twin who presented at 12 years of age with growth delay , metabolic alkalosis , hypomagnesemia and hypokalemia with inappropriate kaliuresis , and idiopathic intracranial hypertension with bilateral papilledema ( pseudotumor cerebri ) .

## Item biored:test:477
Example input:
Sentence: The -930A > G polymorphism of the CYBA gene is associated with premature coronary artery disease .

Example answer:
{"entities": [{"text": "-930A > G", "type": "SequenceVariant"}, {"text": "CYBA", "type": "GeneOrGeneProduct"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study showed that CFH was more likely to be AMD susceptibility gene at Chr.1q31 based on the finding that the CFHR1 and CFHR3 deletion was not polymorphic in the cohort of this study , and none of the SNPs that were significantly associated with AMD in a white population in C2 , CFB , and C3 genes showed a significant association with AMD .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Single nucleotide polymorphism in ABCG2 is associated with irinotecan-induced severe myelosuppression .

Example answer:
{"entities": [{"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "irinotecan-induced", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A heterozygous germline T to C transition in exon 10 of the TSHR gene ( c.1358T -- > C ) resulting in the substitution of methionine ( ATG ) by threonine ( ACG ) at codon 453 ( p.M453T ) was identified in the father and his two children .

Example answer:
{"entities": [{"text": "T to C", "type": "SequenceVariant"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}, {"text": "c.1358T -- > C", "type": "SequenceVariant"}, {"text": "methionine ( ATG ) by threonine ( ACG ) at codon 453", "type": "SequenceVariant"}, {"text": "p.M453T", "type": "SequenceVariant"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Combination of polymorphisms within 5 ' and 3 ' untranslated regions of thymidylate synthase gene modulates survival in 5 fluorouracil-treated colorectal cancer patients .

Example answer:
{"entities": [{"text": "thymidylate synthase", "type": "GeneOrGeneProduct"}, {"text": "5", "type": "ChemicalEntity"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Roles of G1359A polymorphism of the cannabinoid receptor gene ( CNR1 ) on weight loss and adipocytokines after a hypocaloric diet .

Example answer:
{"entities": [{"text": "G1359A", "type": "SequenceVariant"}, {"text": "cannabinoid receptor", "type": "GeneOrGeneProduct"}, {"text": "CNR1", "type": "GeneOrGeneProduct"}, {"text": "weight loss", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We analyzed the nucleotidic sequence of the CYP2F1 gene in DNA samples from 90 French Caucasians consisting in 44 patients with lung cancer and 46 control individuals , using single-strand conformation polymorphism analysis of PCR products ( PCR-SSCP ) .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The CFHR1 and CFHR3 deletion was not polymorphic in the Chinese population and was not associated with wet AMD or drusen .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Genetic polymorphisms in the carbonyl reductase 3 gene CBR3 and the NAD ( P ) H : quinone oxidoreductase 1 gene NQO1 in patients who developed anthracycline-related congestive heart failure after childhood cancer .

## Item biored:test:523
Example input:
Sentence: A single nucleotide polymorphism at position 388 of the FGFR4 amino-acid sequence results in the substitution of glycine ( Gly ) with arginine ( Arg ) and higher frequency of the ArgArg genotype was previously found in prostate cancer patients .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}, {"text": "glycine ( Gly ) with arginine ( Arg )", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The aim of this study was to investigate the association of DNA polymorphisms within steroid synthesis genes ( CYP11B2 , CYP11B1 ) and the postoperative resolution of hypertension in Chinese patients undergoing adrenalectomy for aldosterone-producing adenomas ( APA ) .

Example answer:
{"entities": [{"text": "steroid synthesis genes", "type": "GeneOrGeneProduct"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "aldosterone-producing adenomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a genotype test , we found a trend to point-wise association ( P = 0.053 ) of the G472A SNP in Hispanic subjects with opiate addiction .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "opiate addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: Genotype frequencies of the G472A SNP varied significantly ( P = 0.029 ) among the three main ethnic/cultural groups ( Caucasians , Hispanics , and African Americans ) .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}]}

Example input:
Sentence: Our findings suggest that the G51S PNP polymorphism is associated with a faster rate of cognitive decline in AD patients , highlighting the important role of purine metabolism in the progression of this neurodegenerative disorder .

Example answer:
{"entities": [{"text": "G51S", "type": "SequenceVariant"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "cognitive decline", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "neurodegenerative disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this report the distribution of the exonic G/A single nucleotide polymorphism ( SNP ) in purine nucleoside phosphorylase ( PNP ) gene , resulting in the amino acid substitution serine to glycine at position 51 ( G51S ) , was investigated in a large population of AD patients ( n=321 ) and non-demented control ( n=208 ) .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "purine nucleoside phosphorylase", "type": "GeneOrGeneProduct"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "serine to glycine at position 51", "type": "SequenceVariant"}, {"text": "G51S", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : We investigate whether the G-395A polymorphism of Klotho is associated with EH in a population consisting of 215 patients with EH and 220 non-hypertensive subjects .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : We genotyped 1498 German subjects for SNPs rs6232 and rs6235 within PCSK1 .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "PCSK1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: MATERIALS & METHODS : A total of nine tagging SNPs , five additionally selected SNPs and a cytosine-adenine repeat polymorphism were determined in 133 German adult patients ( 66 men , 67 women ; mean age 45.4 years +/- 13.1 standard deviation ; majority Caucasian ) with GH-deficiency ( GHD ) of different origin , derived from the prospective Pfizer International Metabolic Study ( KIMS ) Pharmacogenetics Study .

## Item biored:test:566
Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Haplotype reconstruction via the expectation-maximization algorithm showed in both populations that only the haplotype containing the minor ( W ) allele at codon 620 was associated with T1D ( OR=2.26 , 95 % CI 1.68-3.02 in Czechs , OR=14.8 , 95 % CI 2.0-651 in Azeri ) or JIA ( OR=2.43 , 95 % CI 1.66-3.56 in Czechs ) .

Example answer:
{"entities": [{"text": "( W ) allele at codon 620", "type": "SequenceVariant"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: By multipoint linkage analysis with markers spanning the entire X-chromosome we mapped the disease locus to a 28-Mb interval between Xp11.4 and Xq12 , including the BCOR gene .

Example answer:
{"entities": [{"text": "BCOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Only D9S180 , of six microsatellites , showed loss of heterozygosity in three BCCs ( two sporadic and one inherited ) .

Example answer:
{"entities": [{"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Linkage disequilibrium analysis indicates that D90A homozygotes and heterozygotes share a rare haplotype and are all descended from a single ancient founder ( alpha 0.974 ) c.895 generations ago .

Example answer:
{"entities": [{"text": "D90A", "type": "SequenceVariant"}]}

Example input:
Sentence: However , haplotype analysis showed that the patient does not carry any paternal DNA markers extending 33kb in the telomeric direction from the ALG6 region , and microsatellite analysis extended the abnormal region to at least 2.5Mb .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "ALG6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The phenotype co-segregates with short-tandem repeat markers flanking the TMC1 gene at the DFNA36 locus on chromosome 9q31-q21 .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "DFNA36", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Homozygosity for a haplotype that was identical by descent between two of the affected individuals identified a locus for the disease gene within a 17.4 Mb interval on chromosome 15 , a region containing 296 genes .

Example answer:
{"entities": []}

Input:
Sentence: In addition , a common haplotype that segregated with the disease in both families was detected by haplotype reconstruction with 10 markers ( microsatellites and SNPs ) , which span 4.6 Mb of DNA covering the DGUOK locus .

## Item biored:test:470
Example input:
Sentence: The current data showed that pilocarpine significantly delayed onset of arrhythmias , decreased the time course of ventricular tachycardia and fibrillation , reduced arrhythmia score , and increased the survival time of arrhythmic rats and guinea pigs .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmias", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ventricular tachycardia and fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "guinea pigs", "type": "OrganismTaxon"}]}

Example input:
Sentence: Chemokine CCL2 and its receptor CCR2 are increased in the hippocampus following pilocarpine-induced status epilepticus .

Example answer:
{"entities": [{"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Behavioral and neurochemical studies in mice pretreated with garcinielliptone FC in pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "garcinielliptone FC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In aspartate , glutamine and glutamate levels detected a decrease of 5.21 % , 13.55 % and 21.80 % , respectively in mice hippocampus treated with GFC75 plus P400 when compared with seized mice .

Example answer:
{"entities": [{"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: Anticonvulsant effect of eslicarbazepine acetate ( BIA 2-093 ) on seizures induced by microperfusion of picrotoxin in the hippocampus of freely moving rats .

Example answer:
{"entities": [{"text": "eslicarbazepine acetate", "type": "ChemicalEntity"}, {"text": "BIA 2-093", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "picrotoxin", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The present study aimed to evaluate the GFC effects at doses of 25 , 50 or 75 mg/kg on seizure parameters to determine their anticonvulsant activity and its effects on amino acid ( r-aminobutyric acid ( GABA ) , glutamine , aspartate and glutathione ) levels as well as on acetylcholinesterase ( AChE ) activity in mice hippocampus after seizures .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "r-aminobutyric acid", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In conclusion , our data suggest that GFC may influence in epileptogenesis and promote anticonvulsant actions in pilocarpine model by modulating the GABA and glutamate contents and of AChE activity in seized mice hippocampus .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A single dose of valproic acid ( VPA ) , which is a widely used antiepileptic drug , is associated with oxidative stress in rats , as recently demonstrated by elevated levels of 15-F ( 2t ) -isoprostane ( 15-F ( 2t ) -IsoP ) .

Example answer:
{"entities": [{"text": "valproic acid", "type": "ChemicalEntity"}, {"text": "VPA", "type": "ChemicalEntity"}, {"text": "antiepileptic drug", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "15-F ( 2t ) -isoprostane", "type": "ChemicalEntity"}, {"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}]}

Input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

## Item biored:test:562
Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "fractalkine receptor", "type": "GeneOrGeneProduct"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "MPTP-induced", "type": "ChemicalEntity"}, {"text": "neurodegeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DA", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our findings suggest that the G51S PNP polymorphism is associated with a faster rate of cognitive decline in AD patients , highlighting the important role of purine metabolism in the progression of this neurodegenerative disorder .

Example answer:
{"entities": [{"text": "G51S", "type": "SequenceVariant"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "cognitive decline", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "neurodegenerative disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This is the first known constitutional rearrangement of SYT14 , and further systematic genetic analysis and clinical studies of DGAP128 may offer unique insights into the role of SYT14 in neurodevelopment .

Example answer:
{"entities": [{"text": "SYT14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metronidazole-induced", "type": "ChemicalEntity"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Myotonic dystrophy ( DM ) , the most prevalent muscular disorder in adults , is caused by ( CTG ) n-repeat expansion in a gene encoding a protein kinase ( DM protein kinase ; DMPK ) and involves changes in cytoarchitecture and ion homeostasis .

Example answer:
{"entities": [{"text": "Myotonic dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscular disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM protein kinase", "type": "GeneOrGeneProduct"}, {"text": "DMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Initial MRIs showed abnormal high signal intensities on DWI and FLAIR ( or T2-weighted image ) at the dentate nucleus ( 8/8 ) , inferior colliculus ( 6/8 ) , corpus callosum ( 2/8 ) , pons ( 2/8 ) , medulla ( 1/8 ) , and bilateral cerebral white matter ( 1/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Initial brain magnetic resonance imaging ( MRI ) were obtained after the hospitalization , including DWI ( 8/8 ) , apparent diffusion coefficient ( ADC ) map ( 4/8 ) , FLAIR ( 7/8 ) , and T2-weighted image ( 8/8 ) .

Example answer:
{"entities": []}

Input:
Sentence: Brain MRIs are normal in DGUOK patients in the literature .

## Item biored:test:527
Example input:
Sentence: In agreement with the expectation that this mutation alters the LYAR binding activity , we found that the Ag ( +25 G- > A ) and Gg-globin-XmnI polymorphisms are associated with high HbF in erythroid precursor cells isolated from b ( 0 ) 39/b ( 0 ) 39 thalassemia patients .

Example answer:
{"entities": [{"text": "LYAR", "type": "GeneOrGeneProduct"}, {"text": "Ag", "type": "GeneOrGeneProduct"}, {"text": "+25 G- > A", "type": "SequenceVariant"}, {"text": "Gg-globin-XmnI", "type": "GeneOrGeneProduct"}, {"text": "HbF", "type": "GeneOrGeneProduct"}, {"text": "b ( 0 ) 39/b ( 0 ) 39 thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : The G-395A polymorphism of the human Klotho gene is associated with EH and may be a potential regulatory site .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that the G-395A polymorphism in the promoter region of the human Klotho gene may contribute to the prevalence of Essential Hypertension ( EH ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "Essential Hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

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
Sentence: Atypical GH insensitivity syndrome and severe insulin-like growth factor-I deficiency resulting from compound heterozygous mutations of the GH receptor , including a novel frameshift mutation affecting the intracellular domain .

Example answer:
{"entities": [{"text": "GH insensitivity syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin-like growth factor-I deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONTEXT : Interindividual variations in glucocorticoid sensitivity have been associated with manifestations of cortisol excess or deficiency and may be partly explained by polymorphisms in the human glucocorticoid receptor ( hGR ) gene .

Example answer:
{"entities": [{"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "cortisol", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "glucocorticoid receptor", "type": "GeneOrGeneProduct"}, {"text": "hGR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Mutations affecting the intracellular domain of the GHR can result in GH insensitivity and IGF deficiency , despite normal serum concentrations of GHBP .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND/AIMS : GH insensitivity and IGF deficiency may result from aberrations of the GH receptor ( GHR ) .

Example answer:
{"entities": [{"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}, {"text": "GHR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: CONCLUSION : IGF-1 gene polymorphisms were not associated with the responsiveness to exogenous GH in GHD .

## Item biored:test:554
Example input:
Sentence: Seven novel single-nucleotide polymorphisms ( SNPs ) were also found , of which a change of leucine 269 to phenylalanine ( Leu269Phe ) was found in 12 of 18 patients with the Arg555Trp mutation .

Example answer:
{"entities": [{"text": "leucine 269 to phenylalanine", "type": "SequenceVariant"}, {"text": "Leu269Phe", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Arg555Trp", "type": "SequenceVariant"}]}

Example input:
Sentence: A common single nucleotide polymorphism ( SNP ) , G472A , codes for a Val158Met substitution and results in a fourfold down regulation of enzyme activity .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "Val158Met", "type": "SequenceVariant"}]}

Example input:
Sentence: Plotting the distribution of known DNA breakpoints among the introns of the two genes showed that , the highest breakpoint density is co-localized with the highest Alu density .

Example answer:
{"entities": []}

Example input:
Sentence: We progressively screened DNA samples from 613 individuals with ID initially for the most frequent ARX mutations ( c.304ins ( GCG ) ( 7 ) 'expansion ' of pA1 and c.429_452dup 'dup24bp ' of pA2 ) .

Example answer:
{"entities": [{"text": "ID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARX", "type": "GeneOrGeneProduct"}, {"text": "c.304ins ( GCG ) ( 7 )", "type": "SequenceVariant"}, {"text": "c.429_452dup", "type": "SequenceVariant"}]}

Example input:
Sentence: In this report the distribution of the exonic G/A single nucleotide polymorphism ( SNP ) in purine nucleoside phosphorylase ( PNP ) gene , resulting in the amino acid substitution serine to glycine at position 51 ( G51S ) , was investigated in a large population of AD patients ( n=321 ) and non-demented control ( n=208 ) .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "purine nucleoside phosphorylase", "type": "GeneOrGeneProduct"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "serine to glycine at position 51", "type": "SequenceVariant"}, {"text": "G51S", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The following gene polymorphisms were determined in genomic DNA : angiotensin-converting enzyme insertion/deletion polymorphism ( I/D ACE ) , angiotensinogen gene polymorphism ( M 235 ) , angiotensin II receptor type 1 ( ATR1 ) polymorphism ( A 11666C ) , and polymorphism of serotonin transporter gene ( 5HTTLPR ) .Heart rate variability during HUT was assessed in 5-minute intervals by low frequency , high frequency , standard deviation of the normal-to-normal ( SDNN ) , and root mean square successive difference parameters .

Example answer:
{"entities": [{"text": "angiotensin-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "M 235", "type": "SequenceVariant"}, {"text": "angiotensin II receptor type 1", "type": "GeneOrGeneProduct"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "A 11666C", "type": "SequenceVariant"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "5HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: A 28 bp variable number of tandem repeats ( VNTR ) , a G/C single nucleotide polymorphism ( SNP ) , and a deletion of 6 bp at position 1494 were studied .

Example answer:
{"entities": [{"text": "28 bp variable number of tandem repeats", "type": "SequenceVariant"}, {"text": "G/C", "type": "SequenceVariant"}, {"text": "deletion of 6 bp at position 1494", "type": "SequenceVariant"}]}

Example input:
Sentence: METHODS : The single nucleotide polymorphisms ( SNP ) at positions -1123 ( rs2488457 ) , +1858 ( rs2476601 , the R620W substitution ) , and +2740 ( rs1217412 ) were genotyped using TaqMan assays in 372 subjects with childhood-onset T1D , 130 subjects with JIA , and 400 control subjects of Czech origin , and in 160 subjects with T1D and 271 healthy controls of Azeri origin .

Example answer:
{"entities": [{"text": "rs2488457", "type": "SequenceVariant"}, {"text": "rs2476601", "type": "SequenceVariant"}, {"text": "R620W", "type": "SequenceVariant"}, {"text": "rs1217412", "type": "SequenceVariant"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Exonic and intronic segments , 5 ' and 3 ' flanking regions of IRS2 ( 14.5 kb ) , were bidirectionally sequenced for single nucleotide polymorphism ( SNP ) discovery in 934 Hispanic children using 3730XL DNA Sequencers .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Genotyping of STRs and single nucleotide polymorphisms defined the AUNA1 breakpoint as 35 kb 5 ' to PCDH9 , with a 2.4 Mb area of overlap with the IT .

## Item biored:test:555
Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: Molecular characterization by DNA sequencing analysis and multiplex ligation-dependent probe amplification of the MLYCD gene revealed a heterozygous mutation ( c.920T > G , p.Leu307Arg ) in the patient and his father and a heterozygous deletion comprising exon 1 in the patient and his mother .

Example answer:
{"entities": [{"text": "MLYCD", "type": "GeneOrGeneProduct"}, {"text": "c.920T > G", "type": "SequenceVariant"}, {"text": "p.Leu307Arg", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: Sanger sequence analysis of PTPN11 coding regions in a total of 17 MC families identified mutations in 10 of them ( 5 frameshift , 2 nonsense , and 3 splice-site mutations ) .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We next sequenced PTPN11 in DNA samples from 54 patients with the multiple enchondromatosis disorders Ollier disease or Maffucci syndrome , but found no coding sequence PTPN11 mutations .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "enchondromatosis disorders Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Direct sequencing of the encoding regions of the candidate genes revealed a heterozygous mutation c.592C -- > T in exon 2 of the gap junction protein , alpha 8 ( GJA8 ) gene .

Example answer:
{"entities": [{"text": "c.592C -- > T", "type": "SequenceVariant"}, {"text": "gap junction protein , alpha 8", "type": "GeneOrGeneProduct"}, {"text": "GJA8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA capture and parallel sequencing identified heterozygous putative loss-of-function mutations in PTPN11 in 4 of the 11 families .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: However , haplotype analysis showed that the patient does not carry any paternal DNA markers extending 33kb in the telomeric direction from the ALG6 region , and microsatellite analysis extended the abnormal region to at least 2.5Mb .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "ALG6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Input:
Sentence: DNA sequencing of coding regions in the AUNA1 family and in the retained homologue chromosome in the monosomic patient revealed no mutations .

## Item biored:test:549
Example input:
Sentence: Recently , a lethal phenotype characterized by sudden infant death with dysgenesis of the testes syndrome ( SIDDT ) was identified to be caused by loss of function mutations in the TSPYL1 gene .

Example answer:
{"entities": [{"text": "sudden infant death with dysgenesis of the testes syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SIDDT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSPYL1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Homozygosity for c.2607C > A was also identified in an unrelated but haplotypically identical patient with an unusually favorable outcome despite severe neonatal-onset GE .

Example answer:
{"entities": [{"text": "c.2607C > A", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "GE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The -930G allele carrier state was a risk factor for CAD ( OR 2.03 , 95 % CI 1.21-3.44 , P=0.007 ) .

Example answer:
{"entities": [{"text": "-930G", "type": "SequenceVariant"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A haplotype containing these four SNPs ( CATA ) significantly increased protection of wet AMD with a P value of 0.0005 and an odds ratio of 0.29 ( 95 % confidence interval : 0.15-0.60 ) .

Example answer:
{"entities": [{"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These findings extend the body of evidence for compound heterozygous mutations leading to HS-RDEB and provide the basis for prenatal diagnosis in this family .

Example answer:
{"entities": [{"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The symptoms of infertility observed in the DMC1 homozygote mutation carrier and in both patients with a heterozygous substitution in exon 2 of the MSH5 gene provide indirect evidence of the role of genes involved in meiotic recombination in the regulation of ovarian function .

Example answer:
{"entities": [{"text": "infertility", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Approximately 30 % of alleles causing genetic disorders generate premature termination codons ( PTCs ) , which are usually associated with severe phenotypes .

Example answer:
{"entities": []}

Example input:
Sentence: Mutational analyses of TS and allelic imbalances were studied in all primary tumors and in 18 additional metachronic metastases .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Most carrier females have mild mental retardation and subtle facial changes .

Example answer:
{"entities": [{"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Offspring of IT balanced carriers are at high risk to have either pure partial trisomy or monosomy for the inserted segment as manifested by `` pure '' phenotypes .

## Item biored:test:569
Example input:
Sentence: The development of antibodies reflects a loss of tolerance to intestinal bacteria that underlies Crohn 's disease , resulting in an exaggerated adaptive immune response to these bacteria .

Example answer:
{"entities": [{"text": "bacteria", "type": "OrganismTaxon"}, {"text": "Crohn 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Oxidative stress plays an essential role in inflammation and fibrosis .

Example answer:
{"entities": [{"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CBMCs were stimulated with innate ( Lipid A , LpA ; Peptidoglycan , Ppg ) , adaptive stimuli ( house dust mite Dermatophagoides pteronyssinus 1 , Derp1 ) or mitogen ( phytohemagglutinin , PHA ) .

Example answer:
{"entities": [{"text": "Lipid A", "type": "ChemicalEntity"}, {"text": "LpA", "type": "ChemicalEntity"}, {"text": "Peptidoglycan", "type": "ChemicalEntity"}, {"text": "Ppg", "type": "ChemicalEntity"}, {"text": "Dermatophagoides pteronyssinus 1", "type": "GeneOrGeneProduct"}, {"text": "Derp1", "type": "GeneOrGeneProduct"}, {"text": "phytohemagglutinin", "type": "ChemicalEntity"}, {"text": "PHA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Atopic diseases during the first 3 years of life were assessed by questionnaire answered by the parents .

Example answer:
{"entities": []}

Example input:
Sentence: The excretion and genetic expression of inflammatory factors were , respectively , estimated by enzyme-linked immunosorbent assay ( ELISA ) and real-time polymerase chain reaction ( PCR ) .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further follow-up of the cohort is required to study the polymorphisms ' relevance for immune-mediated diseases such as childhood asthma .

Example answer:
{"entities": [{"text": "immune-mediated diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: IL-3 is an allergic cytokine with the multilineage potential , while CSF-1 is produced in the steady state with restricted lineage coverage .

Example answer:
{"entities": [{"text": "IL-3", "type": "GeneOrGeneProduct"}, {"text": "CSF-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This study investigated the influence of TBX21 and HLX1 single nucleotide polymorphisms ( SNPs ) , which have previously been shown to be associated with asthma , on T ( H ) 1/T ( H ) 2 lineage cytokines at birth .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Finally , the inflammatory infiltration of alveolar and interstitial cells and the destruction of lung structure were significantly attenuated in the mide administered Bach1 siRNA compared with those in the BLM group .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "BLM", "type": "ChemicalEntity"}]}

Example input:
Sentence: Airway stem cells slowly self-renew and produce differentiated progeny to maintain homeostasis throughout the lifespan of an individual .

Example answer:
{"entities": []}

Input:
Sentence: Asthma is a chronic inflammatory disease of the airways .

## Item biored:test:480
Example input:
Sentence: The p53 mutation spectrum , presenting a high level of CC to TT mutations , shows that the UV component of sunlight is the major risk factor and modulated DNA repair by immunosuppressive drug treatment may be significant in the skin carcinogenesis of RTRs .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "CC to TT", "type": "SequenceVariant"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: With few genetic studies investigating biosynthetic and metabolic enzymes governing the rate of 5-HT activity and their relationship to migraine , it was the objective of this study to assess genetic variants within the human tryptophan hydroxylase ( TPH ) , amino acid decarboxylase ( AADC ) and monoamine oxidase A ( MAOA ) genes in migraine susceptibility .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tryptophan hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "amino acid decarboxylase", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "monoamine oxidase A", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Two coding polymorphisms , 55M/L and 192Q/R , and a promoter variant , -107C/T , has been extensively studied with respect to susceptibility to CHD .

Example answer:
{"entities": [{"text": "55M/L", "type": "SequenceVariant"}, {"text": "192Q/R", "type": "SequenceVariant"}, {"text": "-107C/T", "type": "SequenceVariant"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Mutations found in the PTCH1 gene and neighboring repetitive sequences may have contributed to the development of the studied BCCs .

Example answer:
{"entities": [{"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Model selection suggests an association between nucleotide substitution rate and disease progression , but a role for CCR5 genotype remains elusive .

Example answer:
{"entities": [{"text": "CCR5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The androgen receptor ( AR ) gene has polymorphic regions containing variable length glutamine and glycine repeats and these are believed to be associated with PC risk .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Several studies have reported that , compared with wild-type individuals , CYP2C19 variant allele carriers exhibit a significantly lower capacity to metabolize clopidogrel into its active metabolite and inhibit platelet activation , and are therefore at significantly higher risk of adverse cardiovascular events .

Example answer:
{"entities": [{"text": "CYP2C19", "type": "GeneOrGeneProduct"}, {"text": "clopidogrel", "type": "ChemicalEntity"}]}

Example input:
Sentence: We analyzed the nucleotidic sequence of the CYP2F1 gene in DNA samples from 90 French Caucasians consisting in 44 patients with lung cancer and 46 control individuals , using single-strand conformation polymorphism analysis of PCR products ( PCR-SSCP ) .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study showed that CFH was more likely to be AMD susceptibility gene at Chr.1q31 based on the finding that the CFHR1 and CFHR3 deletion was not polymorphic in the cohort of this study , and none of the SNPs that were significantly associated with AMD in a white population in C2 , CFB , and C3 genes showed a significant association with AMD .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Thus , in this study , the authors examined whether common polymorphisms in candidate genes involved in the pharmacodynamics of anthracyclines ( in particular , the nicotinamide adenine dinucleotide phosphate : quinone oxidoreductase 1 gene NQO1 and the carbonyl reductase 3 gene CBR3 ) had an impact on the risk of anthracycline-related CHF .

## Item biored:test:525
Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Multivariate logistic regression revealed the common haplotypes H1 ( AGACT ) , H2 ( AGAWT ) , and H3 ( AGAWC ) were associated with the persistent postoperative hypertension ( P = .01 , 0.03 , 0.005 after Bonferroni correction ) .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Significantly lower frequency of the A-C-C-G with higher frequency of A-C-A-G haplotypes was also noticed in subjects with DS ( P value =0.02089 and 0.00588 respectively ) .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Example input:
Sentence: Subgroup analysis shows a higher incidence of the heterozygous ArgGly genotype in cancer cases than in the combined group of BPH and controls ( P < 0.05 ) ; this difference is statistically significant between cancer and BPH patients but not between cancer cases and community controls .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Treatment with recombinant DNA-derived IGF-I resulted in growth acceleration .

Example answer:
{"entities": [{"text": "IGF-I", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Mutations affecting the intracellular domain of the GHR can result in GH insensitivity and IGF deficiency , despite normal serum concentrations of GHBP .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In Austrians , genotype distribution differed between patients and controls ( p=0.044 ) and Cys 23 Ser was associated with weight ( p=0.039 ) , body mass index ( BMI ; p=0.038 ) , and seasonal appetite change ( p=0.031 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "Cys 23 Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: BACKGROUND/AIMS : GH insensitivity and IGF deficiency may result from aberrations of the GH receptor ( GHR ) .

Example answer:
{"entities": [{"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}, {"text": "GHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The child had a height of -4 SD , elevated serum GH concentrations , abnormally low serum IGF-I and IGFBP-3 concentrations and normal GHBP concentrations .

Example answer:
{"entities": [{"text": "GH", "type": "GeneOrGeneProduct"}, {"text": "IGF-I", "type": "GeneOrGeneProduct"}, {"text": "IGFBP-3", "type": "GeneOrGeneProduct"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: GH-dose after 1 year of treatment , IGF-1 concentrations , IGF-1-standard deviation score ( SDS ) , the IGF-1 : GH ratio and anthropometric data were analyzed by genotype .

## Item biored:test:534
Example input:
Sentence: Tak1 ( col2 ) mice displayed severe chondrodysplasia with runting , impaired formation of secondary centres of ossification , and joint abnormalities including elbow dislocation and tarsal fusion .

Example answer:
{"entities": [{"text": "Tak1", "type": "GeneOrGeneProduct"}, {"text": "col2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "chondrodysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "joint abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "elbow dislocation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tarsal fusion", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Point mutations in the BICD2 gene have been identified in patients with a dominant form of spinal muscular atrophy , but how these mutations cause disease is unknown .

Example answer:
{"entities": [{"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "spinal muscular atrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutation of the a-tubulin isotype TUBA1A is associated with cortical malformations in humans .

Example answer:
{"entities": [{"text": "a-tubulin", "type": "GeneOrGeneProduct"}, {"text": "TUBA1A", "type": "GeneOrGeneProduct"}, {"text": "cortical malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: In mice carrying a Tuba1a missense mutation ( S140G ) , neurons accumulate , and glial cells are dispersed along the rostral migratory stream in postnatal and adult brains .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "Tuba1a", "type": "GeneOrGeneProduct"}, {"text": "S140G", "type": "SequenceVariant"}]}

Example input:
Sentence: We studied the PAX6 gene mutations in a cohort of affected individuals with different clinical phenotype including AN , coloboma of iris and choroid , or anterior segment malformations .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coloboma of iris and choroid", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anterior segment malformations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Neither intragenic mutation nor large deletion was identified in the group with coloboma of iris and choroid .

Example answer:
{"entities": [{"text": "coloboma of iris and choroid", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Identification of novel type VII collagen gene mutations resulting in severe recessive dystrophic epidermolysis bullosa .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: These observations suggest that mutations in this region of the collagen type I alpha 2 chain carry a high risk of abnormal limb development and intracranial bleeding .

## Item biored:test:464
Example input:
Sentence: Nitric oxide ( NO ) , gaseous neurotransmitter , has contradictor role in epileptogenesis due to opposite effects of L-arginine , precursor of NO syntheses ( NOS ) , and L-NAME ( NOS inhibitor ) observed in different epilepsy models .

Example answer:
{"entities": [{"text": "Nitric oxide", "type": "ChemicalEntity"}, {"text": "NO", "type": "ChemicalEntity"}, {"text": "L-arginine", "type": "ChemicalEntity"}, {"text": "NO syntheses", "type": "GeneOrGeneProduct"}, {"text": "NOS", "type": "GeneOrGeneProduct"}, {"text": "L-NAME", "type": "ChemicalEntity"}, {"text": "epilepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: When tested in a multivariate regression analysis , tranexamic acid was a strong independent predictor of seizures ( OR 14.3 , 95 % CI 5.5-36.7 ; p < 0.001 ) .

Example answer:
{"entities": [{"text": "tranexamic acid", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine whether there was a temporal relationship between VPA-associated oxidative stress and hepatotoxicity , adult male Sprague-Dawley rats were treated ip with VPA ( 500 mg/kg ) or 0.9 % saline ( vehicle ) once daily for 2 , 4 , 7 , 10 , or 14 days .

Example answer:
{"entities": [{"text": "VPA-associated", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Apamin ( 10 ng ) had a tendency to decrease the convulsive threshold ( 21.6 +/- 2.2 to 19.9 +/- 2.5 mg. l ( -1 ) ) but this was not statistically significant .

Example answer:
{"entities": [{"text": "Apamin", "type": "ChemicalEntity"}, {"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In aspartate , glutamine and glutamate levels detected a decrease of 5.21 % , 13.55 % and 21.80 % , respectively in mice hippocampus treated with GFC75 plus P400 when compared with seized mice .

Example answer:
{"entities": [{"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: Anticonvulsant effect of eslicarbazepine acetate ( BIA 2-093 ) on seizures induced by microperfusion of picrotoxin in the hippocampus of freely moving rats .

Example answer:
{"entities": [{"text": "eslicarbazepine acetate", "type": "ChemicalEntity"}, {"text": "BIA 2-093", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "picrotoxin", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In conclusion , our data suggest that GFC may influence in epileptogenesis and promote anticonvulsant actions in pilocarpine model by modulating the GABA and glutamate contents and of AChE activity in seized mice hippocampus .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The present study aimed to evaluate the GFC effects at doses of 25 , 50 or 75 mg/kg on seizure parameters to determine their anticonvulsant activity and its effects on amino acid ( r-aminobutyric acid ( GABA ) , glutamine , aspartate and glutathione ) levels as well as on acetylcholinesterase ( AChE ) activity in mice hippocampus after seizures .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "r-aminobutyric acid", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A single dose of valproic acid ( VPA ) , which is a widely used antiepileptic drug , is associated with oxidative stress in rats , as recently demonstrated by elevated levels of 15-F ( 2t ) -isoprostane ( 15-F ( 2t ) -IsoP ) .

Example answer:
{"entities": [{"text": "valproic acid", "type": "ChemicalEntity"}, {"text": "VPA", "type": "ChemicalEntity"}, {"text": "antiepileptic drug", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "15-F ( 2t ) -isoprostane", "type": "ChemicalEntity"}, {"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}]}

Input:
Sentence: The present study aimed to investigate the anticonvulsant activity as well as the effects on the level of hippocampal amino acid neurotransmitters ( glutamate , aspartate , glycine and GABA ) of N- ( 2-propylpentanoyl ) urea ( VPU ) in comparison to its parent compound , valproic acid ( VPA ) .

## Item biored:test:558
Example input:
Sentence: Linkage disequilibrium analysis indicates that D90A homozygotes and heterozygotes share a rare haplotype and are all descended from a single ancient founder ( alpha 0.974 ) c.895 generations ago .

Example answer:
{"entities": [{"text": "D90A", "type": "SequenceVariant"}]}

Example input:
Sentence: We investigated clinical and cellular phenotypes of 24 children with mutations in the catalytic ( alpha ) subunit of the mitochondrial DNA ( mtDNA ) gamma polymerase ( POLG1 ) .

Example answer:
{"entities": [{"text": "mitochondrial DNA ( mtDNA ) gamma polymerase", "type": "GeneOrGeneProduct"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: With the advent of next-generation sequencing technologies , the homozygous mutations T71N and A190T in the neuronal calcium sensor ( NCS ) hippocalcin were identified as the genetic cause of primary isolated dystonia ( DYT2 dystonia ) .

Example answer:
{"entities": [{"text": "T71N", "type": "SequenceVariant"}, {"text": "A190T", "type": "SequenceVariant"}, {"text": "neuronal calcium sensor", "type": "GeneOrGeneProduct"}, {"text": "NCS", "type": "GeneOrGeneProduct"}, {"text": "hippocalcin", "type": "GeneOrGeneProduct"}, {"text": "primary isolated dystonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DYT2", "type": "GeneOrGeneProduct"}, {"text": "dystonia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: POLG mutations associated with Alpers ' syndrome and mitochondrial DNA depletion .

Example answer:
{"entities": [{"text": "POLG", "type": "GeneOrGeneProduct"}, {"text": "Alpers ' syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial DNA depletion", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Myotonic dystrophy ( DM ) , the most prevalent muscular disorder in adults , is caused by ( CTG ) n-repeat expansion in a gene encoding a protein kinase ( DM protein kinase ; DMPK ) and involves changes in cytoarchitecture and ion homeostasis .

Example answer:
{"entities": [{"text": "Myotonic dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscular disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM protein kinase", "type": "GeneOrGeneProduct"}, {"text": "DMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Depletion of mitochondrial DNA in fibroblast cultures from patients with POLG1 mutations is a consequence of catalytic mutations .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It is an autosomal recessive , developmental mitochondrial DNA depletion disorder characterized by deficiency in mitochondrial DNA polymerase gamma ( POLG ) catalytic activity , refractory seizures , neurodegeneration , and liver disease .

Example answer:
{"entities": [{"text": "mitochondrial DNA depletion", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DNA polymerase gamma", "type": "GeneOrGeneProduct"}, {"text": "POLG", "type": "GeneOrGeneProduct"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver disease", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The first founder DGUOK mutation associated with hepatocerebral mitochondrial DNA depletion syndrome .

## Item biored:test:530
Example input:
Sentence: Taken together , the results suggest that mutual interactions between these factors may be pivotal not only in enhancing the osteomimicry and metastatic potential of PC cells , but also in bone remodeling and in shifting the balance from osteoclastogenesis towards osteoblastogenesis .

Example answer:
{"entities": [{"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The expression of bone morphogenetic protein ( Bmp ) genes , such as Bmp4 and Bmp7 , was also ectopically induced in the epithelia of the URS in the b-catenin GOF mutants .

Example answer:
{"entities": [{"text": "bone morphogenetic protein", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}, {"text": "Bmp4", "type": "GeneOrGeneProduct"}, {"text": "Bmp7", "type": "GeneOrGeneProduct"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OSX encodes a transcription factor containing three Cys2-His2 zinc-finger DNA-binding domains at its C terminus , which , in mice , has been shown to be essential for bone formation .

Example answer:
{"entities": [{"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: BACKGROUND : Oculopharyngeal muscular dystrophy ( OPMD ) is a late onset autosomal dominant muscle disorder .

Example answer:
{"entities": [{"text": "Oculopharyngeal muscular dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal dominant muscle disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Identification of a frameshift mutation in Osterix in a patient with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "Osterix", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This finding adds another locus to the spectrum of genes associated with osteogenesis imperfecta and reveals that SP7/OSX also plays a key role in human bone development .

Example answer:
{"entities": [{"text": "osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SP7/OSX", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Osteogenesis imperfecta , or `` brittle bone disease , '' is a type I collagen-related condition associated with osteoporosis and increased risk of bone fractures .

Example answer:
{"entities": [{"text": "Osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brittle bone disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "is a", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type I", "type": "GeneOrGeneProduct"}, {"text": "osteoporosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bone fractures", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Osteogenesis imperfecta ( OI ) is a heritable bone disorder characterized by fractures with minimal trauma .

## Item biored:test:560
Example input:
Sentence: Sequencing of the PAX6 gene , three intragenic mutations including a novel heterozygous splicing-site mutations c.357-3C > G ( p.Ser119fsX ) were identified in the patients of the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "c.357-3C > G", "type": "SequenceVariant"}, {"text": "p.Ser119fsX", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: R58fs mutation in the HGD gene in a family with alkaptonuria in the UAE .

Example answer:
{"entities": [{"text": "R58fs", "type": "SequenceVariant"}, {"text": "HGD", "type": "GeneOrGeneProduct"}, {"text": "alkaptonuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These included missense ( p.T286M ) and nonsense ( p.W111X ) mutations and a transition in the obligate AG-dinucleotide of the intron 8 acceptor splice site ( c.610-2A > G ) .

Example answer:
{"entities": [{"text": "p.T286M", "type": "SequenceVariant"}, {"text": "p.W111X", "type": "SequenceVariant"}, {"text": "AG-dinucleotide", "type": "SequenceVariant"}, {"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we report on two hemizygous mutations in OGT in individuals with X-linked intellectual disability ( XLID ) and dysmorphic features : one missense mutation ( p.Arg284Pro ) and one mutation leading to a splicing defect ( c.463-6T > G ) .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "c.463-6T > G", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : The patient 's GR gene had a heterozygotic mutation ( G -- > A ) at nucleotide position 2141 ( exon 8 ) , which resulted in substitution of arginine by glutamine at amino acid position 714 in the ligand-binding domain ( LBD ) of the GR alpha .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "( G -- > A ) at nucleotide position 2141", "type": "SequenceVariant"}, {"text": "arginine by glutamine at amino acid position 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: In this study , we describe a new splice site mutation in the DGUOK gene and the clinical , radiologic , and genetic features of these DGUOK patients .

## Item biored:test:487
Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: A known variation , 714C- > ( I238M ) , was also found in the patient with L490R .

Example answer:
{"entities": [{"text": "714C-", "type": "SequenceVariant"}, {"text": "I238M", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "L490R", "type": "SequenceVariant"}]}

Example input:
Sentence: The dual-luciferase reporter assay revealed that the -395A carrier of a 498-bp DNA fragment ( containing the G-395A site ) upstream of the Klotho gene has higher relative luciferase activity than the -395G carrier .

Example answer:
{"entities": [{"text": "-395A", "type": "SequenceVariant"}, {"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "-395G", "type": "SequenceVariant"}]}

Example input:
Sentence: C_6+/6+ and G_6+/6+ combined genotypes were respectively associated to the best and worst PFS ( P=0.03 when compared with each other ) , while combinations carrying the allele 6- determined an intermediate evolution that might be indicative of a variable response to chemotherapy .

Example answer:
{"entities": []}

Example input:
Sentence: BACKGROUND : A intragenic biallelic polymorphism ( 1359 G/A ) of the CB1 gene resulting in the substitution of the G to A at nucleotide position 1359 in codon 435 ( Thr ) , was reported as a common polymorphism in Caucasian populations .

Example answer:
{"entities": [{"text": "1359 G/A", "type": "SequenceVariant"}, {"text": "CB1", "type": "GeneOrGeneProduct"}, {"text": "G to A at nucleotide position 1359", "type": "SequenceVariant"}, {"text": "codon 435 ( Thr )", "type": "SequenceVariant"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: Several studies have reported that , compared with wild-type individuals , CYP2C19 variant allele carriers exhibit a significantly lower capacity to metabolize clopidogrel into its active metabolite and inhibit platelet activation , and are therefore at significantly higher risk of adverse cardiovascular events .

Example answer:
{"entities": [{"text": "CYP2C19", "type": "GeneOrGeneProduct"}, {"text": "clopidogrel", "type": "ChemicalEntity"}]}

Input:
Sentence: In line , recombinant CBR3 V244 ( G allele ) synthesized 2.6-fold more cardiotoxic doxorubicinol per unit of time than CBR3 M244 ( A allele ; CBR3 V244 [ 8.26+/-3.57 nmol/hour.mg ] vs CBR3 M244 [ 3.22+/-0.67 nmol/hour.mg ] ; P=.01 ) .

## Item biored:test:483
Example input:
Sentence: Several studies have reported that , compared with wild-type individuals , CYP2C19 variant allele carriers exhibit a significantly lower capacity to metabolize clopidogrel into its active metabolite and inhibit platelet activation , and are therefore at significantly higher risk of adverse cardiovascular events .

Example answer:
{"entities": [{"text": "CYP2C19", "type": "GeneOrGeneProduct"}, {"text": "clopidogrel", "type": "ChemicalEntity"}]}

Example input:
Sentence: Serum samples were PCR amplified with HBV reverse transcriptase ( RT ) primers , followed by direct sequencing across the tyrosine-methionine-aspartate-aspartate ( YMDD ) motif of the major catalytic region in the C domain of the HBV RT enzyme .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: Polymerase chain reaction was carried out and single nucleotide polymorphisms of FGFR4 were identified by restriction enzyme digestion .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: A common single nucleotide polymorphism ( SNP ) , G472A , codes for a Val158Met substitution and results in a fourfold down regulation of enzyme activity .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "Val158Met", "type": "SequenceVariant"}]}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: Low activity of patient plasma butyrylcholinesterase with butyrylthiocholine ( BTC ) and benzoylcholine , and values of dibucaine and fluoride numbers fit with heterozygous atypical silent genotype .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "butyrylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "butyrylthiocholine", "type": "ChemicalEntity"}, {"text": "BTC", "type": "ChemicalEntity"}, {"text": "benzoylcholine", "type": "ChemicalEntity"}, {"text": "dibucaine", "type": "ChemicalEntity"}, {"text": "fluoride", "type": "ChemicalEntity"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Enzyme activity assays with recombinant CBR3 isoforms ( CBR3 V244 and CBR3 M244 ) and the anthracycline substrate doxorubicin were used to investigate the functional impact of the CBR3 V244M polymorphism .

## Item biored:test:587
Example input:
Sentence: The creatine kinase peaked at 62,246 IU/L and the patient was treated with intravenous normal saline .

Example answer:
{"entities": [{"text": "creatine kinase", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: Nine days later the patient 's creatine kinase had dropped to 1695 U/L and creatinine was 3.3 mg/dL .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "creatine kinase", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Example input:
Sentence: The convulsive threshold ( mean +/- SD ) was 41.4 +/- 6.5 mg. l ( -1 ) with lidocaine infusion ( 6 mg.kg ( -1 ) .min ( -1 ) ) , increasing significantly to 66.6 +/- 10.9 mg. l ( -1 ) when the end-tidal concentration of sevoflurane was 0.8 % .

Example answer:
{"entities": [{"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "sevoflurane", "type": "ChemicalEntity"}]}

Example input:
Sentence: At pH 9 , a higher rate of etodolac release from ED was observed as compared to aqueous buffer of pH 7.4 and 80 % human plasma ( pH 7.4 ) , following first-order kinetics .

Example answer:
{"entities": [{"text": "etodolac", "type": "ChemicalEntity"}, {"text": "ED", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: After admission , the patient received a continuous intravenous infusion of 5-FU ( 1000 mg/day ) , during which precordial pain with right bundle branch block occurred concomitantly with a high serum FBAL concentration of 1955 ng/ml .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "right bundle branch block", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: All of the patients ' plasma blood urea nitrogen ( BUN ) and creatinine levels were measured on the second and seventh day after the administration of intravenous contrast material .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "blood urea nitrogen", "type": "ChemicalEntity"}, {"text": "BUN", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "contrast", "type": "ChemicalEntity"}]}

Example input:
Sentence: Laboratory evaluation revealed 66,680 U/L creatine kinase , 93 mg/dL blood urea nitrogen , 4.6 mg/dL creatinine , 1579 U/L aspartate aminotransferase , and 738 U/L alanine aminotransferase .

Example answer:
{"entities": [{"text": "creatine kinase", "type": "ChemicalEntity"}, {"text": "blood urea nitrogen", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "aspartate aminotransferase", "type": "ChemicalEntity"}, {"text": "alanine aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: However , the threshold ( 61.6 +/- 8.7 mg. l ( -1 ) ) during 1.6 % sevoflurane was not significant from that during 0.8 % sevoflurane , indicating a celling effect .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}]}

Example input:
Sentence: Laboratory tests showed an elevation of creatine phosphokinase ( 2218 IU/L ) , aspartate aminotransferase ( 134 IU/L ) , alanine aminotransferase ( 78 IU/L ) , and BUN ( 27.9 mg/ml ) levels .

Example answer:
{"entities": [{"text": "creatine phosphokinase", "type": "ChemicalEntity"}, {"text": "aspartate aminotransferase", "type": "ChemicalEntity"}, {"text": "alanine aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: The serum FBAL concentration subsequently decreased to 352 ng/ml , the same as the value measured on the first day of S-1 administration .

Example answer:
{"entities": [{"text": "FBAL", "type": "ChemicalEntity"}, {"text": "S-1", "type": "ChemicalEntity"}]}

Input:
Sentence: Laboratory test findings on admission were notable only for a flecainide plasma concentration of 1360 microg/L ( reference range 200-1000 ) .

## Item biored:test:533
Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genome-wide loss-of-function genetic screening identifies opioid receptor u1 as a key regulator of L-asparaginase resistance in pediatric acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "opioid receptor u1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "acute lymphoblastic leukemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : The mutation in this kindred led to missplicing and reduced GLDC ( glycine decarboxylase ) expression .

Example answer:
{"entities": [{"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "glycine decarboxylase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations of TP53 and dysfunction of the Brca1 and/or Brca2 tumor-suppressor proteins have been implicated in the molecular pathogenesis of a large fraction of OSCs , but frequent somatic mutations in other well-established tumor-suppressor genes have not been identified .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "Brca1", "type": "GeneOrGeneProduct"}, {"text": "Brca2", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mild glycine encephalopathy ( NKH ) in a large kindred due to a silent exonic GLDC splice mutation .

Example answer:
{"entities": [{"text": "glycine encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NKH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we report on two hemizygous mutations in OGT in individuals with X-linked intellectual disability ( XLID ) and dysmorphic features : one missense mutation ( p.Arg284Pro ) and one mutation leading to a splicing defect ( c.463-6T > G ) .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "c.463-6T > G", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutations in N-acetylglucosamine ( O-GlcNAc ) transferase in patients with X-linked intellectual disability .

Example answer:
{"entities": [{"text": "N-acetylglucosamine ( O-GlcNAc ) transferase", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that defects in O-GlcNAc homeostasis and host cell factor 1 proteolysis may play roles in mediation of XLID in individuals with OGT mutations .

Example answer:
{"entities": [{"text": "O-GlcNAc", "type": "GeneOrGeneProduct"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OGT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In all of these patients , OI was caused by glycine mutations affecting exon 49 of the COL1A2 gene , which codes for the most carboxy-terminal part of the triple-helical domain of the collagen type I alpha 2 chain .

## Item biored:test:521
Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Subgroup analysis shows a higher incidence of the heterozygous ArgGly genotype in cancer cases than in the combined group of BPH and controls ( P < 0.05 ) ; this difference is statistically significant between cancer and BPH patients but not between cancer cases and community controls .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Although only limited subjects were investigated , our results suggested that a genetic polymorphism in ABCG2 might alter the transport activity for the drug and elevate the systemic circulation level of irinotecan , leading to severe myelosuppression .

Example answer:
{"entities": [{"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "irinotecan", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The child had a height of -4 SD , elevated serum GH concentrations , abnormally low serum IGF-I and IGFBP-3 concentrations and normal GHBP concentrations .

Example answer:
{"entities": [{"text": "GH", "type": "GeneOrGeneProduct"}, {"text": "IGF-I", "type": "GeneOrGeneProduct"}, {"text": "IGFBP-3", "type": "GeneOrGeneProduct"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONTEXT : Interindividual variations in glucocorticoid sensitivity have been associated with manifestations of cortisol excess or deficiency and may be partly explained by polymorphisms in the human glucocorticoid receptor ( hGR ) gene .

Example answer:
{"entities": [{"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "cortisol", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "glucocorticoid receptor", "type": "GeneOrGeneProduct"}, {"text": "hGR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Atypical GH insensitivity syndrome and severe insulin-like growth factor-I deficiency resulting from compound heterozygous mutations of the GH receptor , including a novel frameshift mutation affecting the intracellular domain .

Example answer:
{"entities": [{"text": "GH insensitivity syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin-like growth factor-I deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Mutations affecting the intracellular domain of the GHR can result in GH insensitivity and IGF deficiency , despite normal serum concentrations of GHBP .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND/AIMS : GH insensitivity and IGF deficiency may result from aberrations of the GH receptor ( GHR ) .

Example answer:
{"entities": [{"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}, {"text": "GHR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Variance in IGF-1 concentrations due to genetic variations may affect different response to growth hormone ( GH ) treatment , resulting in different individually required GH-doses in GH-deficient patients .

## Item biored:test:482
Example input:
Sentence: Model selection suggests an association between nucleotide substitution rate and disease progression , but a role for CCR5 genotype remains elusive .

Example answer:
{"entities": [{"text": "CCR5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: A 5-HT ( 2C ) Cys 23 Ser substitution , coded for by a single nucleotide polymorphism ( Cys 23 Ser ) within the 5-HT ( 2C ) gene , has been shown to influence 5-HT ( 2C ) function .

Example answer:
{"entities": [{"text": "5-HT ( 2C )", "type": "GeneOrGeneProduct"}, {"text": "Cys 23 Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: BACKGROUND : A intragenic biallelic polymorphism ( 1359 G/A ) of the CB1 gene resulting in the substitution of the G to A at nucleotide position 1359 in codon 435 ( Thr ) , was reported as a common polymorphism in Caucasian populations .

Example answer:
{"entities": [{"text": "1359 G/A", "type": "SequenceVariant"}, {"text": "CB1", "type": "GeneOrGeneProduct"}, {"text": "G to A at nucleotide position 1359", "type": "SequenceVariant"}, {"text": "codon 435 ( Thr )", "type": "SequenceVariant"}]}

Example input:
Sentence: This study showed that CFH was more likely to be AMD susceptibility gene at Chr.1q31 based on the finding that the CFHR1 and CFHR3 deletion was not polymorphic in the cohort of this study , and none of the SNPs that were significantly associated with AMD in a white population in C2 , CFB , and C3 genes showed a significant association with AMD .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Seven SNPs in CFH and two SNPs in C2 , CFB ' , and C3 were genotyped using the ABI SNaPshot method .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Two coding polymorphisms , 55M/L and 192Q/R , and a promoter variant , -107C/T , has been extensively studied with respect to susceptibility to CHD .

Example answer:
{"entities": [{"text": "55M/L", "type": "SequenceVariant"}, {"text": "192Q/R", "type": "SequenceVariant"}, {"text": "-107C/T", "type": "SequenceVariant"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In more than 98 % of cases , the disease is associated with a G to A or G to C substitution at nucleotide position 1138 ( p.G380R ) of the fibroblast growth factor receptor 3 ( FGFR3 ) gene .

Example answer:
{"entities": [{"text": "G to A or G to C substitution at nucleotide position 1138", "type": "SequenceVariant"}, {"text": "p.G380R", "type": "SequenceVariant"}, {"text": "fibroblast growth factor receptor 3", "type": "GeneOrGeneProduct"}, {"text": "FGFR3", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Thirty patients with CHF ( cases ) and 115 matched controls were genotyped for polymorphisms in NQO1 ( NQO1 * 2 ) and CBR3 ( the CBR3 valine [ V ] to methionine [ M ] substitution at position 244 [ V244M ] ) .

## Item biored:test:538
Example input:
Sentence: In this study , we establish the unilateral ureteric obstruction ( UUO ) or folic acid ( FA ) -induced mice renal interstitial fibrosis in vivo and the transforming growth factor ( TGF ) -beta1-stimulated human proximal tubular epithelial cell ( HK-2 ) model in vitro .

Example answer:
{"entities": [{"text": "unilateral ureteric obstruction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "UUO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "folic acid", "type": "ChemicalEntity"}, {"text": "FA", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "renal interstitial fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor ( TGF )", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK-2", "type": "CellLine"}]}

Example input:
Sentence: Moreover , AT2R gene and protein expressions in fetal kidneys were inhibited by PCE , associated with the repression of the gene expression of glial-cell-line-derived neurotrophic factor ( GDNF ) /tyrosine kinase receptor ( c-Ret ) signaling pathway .

Example answer:
{"entities": [{"text": "AT2R", "type": "GeneOrGeneProduct"}, {"text": "glial-cell-line-derived neurotrophic factor", "type": "GeneOrGeneProduct"}, {"text": "GDNF", "type": "GeneOrGeneProduct"}, {"text": "kinase receptor", "type": "GeneOrGeneProduct"}, {"text": "c-Ret", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A mouse model of BLM-induced PF was established , and Bach1 siRNA ( 1x109 pfu ) was administered to the mice via the tail vein .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "BLM-induced", "type": "ChemicalEntity"}, {"text": "PF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: This phenotype resembled that of bone morphogenetic protein receptor ( BMPR ) 1 and Gdf5-deficient mice .

Example answer:
{"entities": [{"text": "bone morphogenetic protein receptor ( BMPR ) 1", "type": "GeneOrGeneProduct"}, {"text": "Gdf5-deficient", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Moreover , the abundance and proliferative index of lymph node , thymus and CNS CD4 ( + ) CD25 ( + ) FoxP3 ( + ) Tregs were strikingly reduced in VPAC2-deficient mice with EAE .

Example answer:
{"entities": [{"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "FoxP3", "type": "GeneOrGeneProduct"}, {"text": "VPAC2-deficient", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The NDUFS2 contains a highly conserved protein kinase C phosphorylation site and the NDUFS3 subunit contains a highly conserved casein kinase II phosphorylation site which make them strong candidates for future mutation detection studies in enzymatic complex I-deficient patients .

Example answer:
{"entities": [{"text": "NDUFS2", "type": "GeneOrGeneProduct"}, {"text": "protein kinase C", "type": "GeneOrGeneProduct"}, {"text": "NDUFS3", "type": "GeneOrGeneProduct"}, {"text": "casein kinase II", "type": "GeneOrGeneProduct"}, {"text": "enzymatic complex I-deficient", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Tak1 ( col2 ) mice displayed severe chondrodysplasia with runting , impaired formation of secondary centres of ossification , and joint abnormalities including elbow dislocation and tarsal fusion .

Example answer:
{"entities": [{"text": "Tak1", "type": "GeneOrGeneProduct"}, {"text": "col2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "chondrodysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "joint abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "elbow dislocation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tarsal fusion", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both b-catenin loss- and gain-of-function ( LOF and GOF ) mutants displayed abnormal clefts in the perineal region and hypoplastic elongation of the URS .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "hypoplastic", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Moreover , Foxf2 knockout mice present with cleft palate in combination with hypoplasia of the genital tubercle .

## Item biored:test:529
Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A G1103R mutation in CRB1 is co-inherited with high hyperopia and Leber congenital amaurosis .

Example answer:
{"entities": [{"text": "G1103R", "type": "SequenceVariant"}, {"text": "CRB1", "type": "GeneOrGeneProduct"}, {"text": "hyperopia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Leber congenital amaurosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Osteogenesis imperfecta , or `` brittle bone disease , '' is a type I collagen-related condition associated with osteoporosis and increased risk of bone fractures .

Example answer:
{"entities": [{"text": "Osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brittle bone disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "is a", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type I", "type": "GeneOrGeneProduct"}, {"text": "osteoporosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bone fractures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This finding adds another locus to the spectrum of genes associated with osteogenesis imperfecta and reveals that SP7/OSX also plays a key role in human bone development .

Example answer:
{"entities": [{"text": "osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SP7/OSX", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Compound heterozygosity for a novel nine-nucleotide deletion and the Asn45Ser missense mutation in the glycoprotein IX gene in a patient with Bernard-Soulier syndrome .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}, {"text": "glycoprotein IX", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Identification of a frameshift mutation in Osterix in a patient with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "Osterix", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , although exon 1beta mutation is rare in various tumors , we detected a missense mutation ( L50R ) in one case with a hemizygous deletion .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "L50R", "type": "SequenceVariant"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Osteogenesis imperfecta type III with intracranial hemorrhage and brachydactyly associated with mutations in exon 49 of COL1A2 .

## Item biored:test:505
Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A common single nucleotide polymorphism ( SNP ) , G472A , codes for a Val158Met substitution and results in a fourfold down regulation of enzyme activity .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "Val158Met", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Four SNPs , including rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , in CFH showed a significant association with wet AMD in the cohort of this study .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These findings suggest that 521T > C , existing commonly in SLCO1B1 * 5 , * 15 and * 15+C1007G , is the key single nucleotide polymorphism ( SNP ) that determines the functional properties of SLCO1B1 * 5 , * 15 and * 15+C1007G allelic proteins and that decreased activities of these variant proteins are mainly caused by a sorting error produced by this SNP .

Example answer:
{"entities": [{"text": "521T > C", "type": "SequenceVariant"}, {"text": "SLCO1B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also observed associations for candidate SNPs in CRP , GSTP1 , and IL1B .

Example answer:
{"entities": [{"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this report the distribution of the exonic G/A single nucleotide polymorphism ( SNP ) in purine nucleoside phosphorylase ( PNP ) gene , resulting in the amino acid substitution serine to glycine at position 51 ( G51S ) , was investigated in a large population of AD patients ( n=321 ) and non-demented control ( n=208 ) .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "purine nucleoside phosphorylase", "type": "GeneOrGeneProduct"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "serine to glycine at position 51", "type": "SequenceVariant"}, {"text": "G51S", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We observed strong linkage disequilibrium between the T allele at -511 and the C allele at -31 and between the C allele at -511 and the T allele at -31 in IL1B in both the cases and controls ( R ( 2 ) =0.94 ) .

Example answer:
{"entities": [{"text": "T allele at -511", "type": "SequenceVariant"}, {"text": "C allele at -31", "type": "SequenceVariant"}, {"text": "C allele at -511", "type": "SequenceVariant"}, {"text": "T allele at -31", "type": "SequenceVariant"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : In the Czechs , all three SNPs were in a tight linkage disequlibrium , while in the Azeri , the linkage disequlibrium was limited to between the promoter and 3'-UTR polymorphism , D ' ( -1123 , +2740 ) =0.99 , r ( 2 ) =0.72 .

Example answer:
{"entities": []}

Example input:
Sentence: We genotyped candidate single-nucleotide polymorphisms ( SNP ) in IL10 , CRP , GPX1 , GSR , GSTP1 , hOGG1 , IL1B , IL1RN , IL6 , IL8 , MPO , NOS2 , NOS3 , SOD1 , SOD2 , SOD3 , TLR4 , and TNF and tagging SNPs in IL10 , CRP , GSR , IL1RN , IL6 , NOS2 , and NOS3 .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "IL1RN", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "IL8", "type": "GeneOrGeneProduct"}, {"text": "MPO", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "NOS3", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "SOD3", "type": "GeneOrGeneProduct"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "TNF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These SNPs were in linkage disequilibrium with each other .

Example answer:
{"entities": []}

Input:
Sentence: This SNP is part of a large linkage disequilibrium block , which contains CCND3 , BYSL , TRFP , USP49 , C6ofr49 , FRS3 , and PGC .

## Item biored:test:573
Example input:
Sentence: The challenge was considered positive if one or more of the following appeared : erythema , rush or urticaria-angioedema .

Example answer:
{"entities": [{"text": "erythema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "urticaria-angioedema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Groups were compared regarding adverse events and changes from baseline to week 16 in electrocardiograms and vital signs .

Example answer:
{"entities": []}

Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We hereafter used an independent sample of 541 Danish individuals from the oldest cohort and confirmed the initial findings ( hazard rate : 1.38 , P = 0.09 ) .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : A case-control study was carried out in Chinese Han population , including 368 cases of migraine and 517 controls .

Example answer:
{"entities": [{"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Treatment-related adverse events ( AEs ) occurred in 44 % and 52 % , 57 % , and 41 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: This study investigated the influence of TBX21 and HLX1 single nucleotide polymorphisms ( SNPs ) , which have previously been shown to be associated with asthma , on T ( H ) 1/T ( H ) 2 lineage cytokines at birth .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: TBX21 SNP rs11079788 carriers developed less symptoms of atopic dermatitis at 3 years of age ( p = 0.03 ) .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "rs11079788", "type": "SequenceVariant"}, {"text": "atopic dermatitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further follow-up of the cohort is required to study the polymorphisms ' relevance for immune-mediated diseases such as childhood asthma .

Example answer:
{"entities": [{"text": "immune-mediated diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Atopic diseases during the first 3 years of life were assessed by questionnaire answered by the parents .

Example answer:
{"entities": []}

Input:
Sentence: At baseline , all participants completed a questionnaire on demographics , symptoms , triggering factors , severity of asthma , and the presence of atopism .

## Item biored:test:590
Example input:
Sentence: At re-warming , patient had resolution of her cerebral edema and intracranial hypertension .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracranial hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The patient achieved a partial response 6 months after the initiation of the S-1 treatment .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "S-1", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fourteen days after hospitalization , creatine kinase level had returned to 230 IU/L and the patient was discharged .

Example answer:
{"entities": [{"text": "creatine kinase", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: She had a gradual return of motor function and ability of feeling Foley catheter .

Example answer:
{"entities": []}

Example input:
Sentence: Three hours later , she complained of perineal numbness and lower extremity weakness .

Example answer:
{"entities": [{"text": "numbness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lower extremity weakness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Her aminotransferase levels returned to normal by postoperative day 23 , and her 2-year follow-up showed no adverse events .

Example answer:
{"entities": [{"text": "aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: The patient had depressed of mental status lasting at least 24 h prior to admission .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All of the symptoms were completely resolved over the next 8 hours .

Example answer:
{"entities": []}

Example input:
Sentence: At discharge , she had complete recovery of neurological and hepatic functions .

Example answer:
{"entities": []}

Example input:
Sentence: Drowsiness was common on clonidine , but generally resolved by 6 to 8 weeks .

Example answer:
{"entities": [{"text": "Drowsiness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}]}

Input:
Sentence: Her delirium resolved 3 days later .

## Item biored:test:488
Example input:
Sentence: In the present study we explored the effect of three polymorphisms of the TS gene on overall and progression- free survival of colorectal cancer ( CRC ) patients subjected to 5FU chemotherapy .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "5FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Model selection suggests an association between nucleotide substitution rate and disease progression , but a role for CCR5 genotype remains elusive .

Example answer:
{"entities": [{"text": "CCR5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The p53 mutation spectrum , presenting a high level of CC to TT mutations , shows that the UV component of sunlight is the major risk factor and modulated DNA repair by immunosuppressive drug treatment may be significant in the skin carcinogenesis of RTRs .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "CC to TT", "type": "SequenceVariant"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : We decided to investigate the role of the polymorphism ( G1359A ) of CB1 receptor gene on adipocytokines response and weight loss secondary to a lifestyle modification ( Mediterranean hypocaloric diet and exercise ) in obese patients .

Example answer:
{"entities": [{"text": "G1359A", "type": "SequenceVariant"}, {"text": "CB1 receptor", "type": "GeneOrGeneProduct"}, {"text": "weight loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Roles of G1359A polymorphism of the cannabinoid receptor gene ( CNR1 ) on weight loss and adipocytokines after a hypocaloric diet .

Example answer:
{"entities": [{"text": "G1359A", "type": "SequenceVariant"}, {"text": "cannabinoid receptor", "type": "GeneOrGeneProduct"}, {"text": "CNR1", "type": "GeneOrGeneProduct"}, {"text": "weight loss", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These results indicate that ADAM12 actively supports the CSC phenotype in claudin-low breast cancer cells via modulation of the EGFR pathway .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "claudin-low", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Several studies have reported that , compared with wild-type individuals , CYP2C19 variant allele carriers exhibit a significantly lower capacity to metabolize clopidogrel into its active metabolite and inhibit platelet activation , and are therefore at significantly higher risk of adverse cardiovascular events .

Example answer:
{"entities": [{"text": "CYP2C19", "type": "GeneOrGeneProduct"}, {"text": "clopidogrel", "type": "ChemicalEntity"}]}

Input:
Sentence: CONCLUSIONS : The functional CBR3 V244M polymorphism may have an impact on the risk of anthracycline-related CHF among childhood cancer survivors by modulating the intracardiac formation of cardiotoxic anthracycline alcohol metabolites .

## Item biored:test:543
Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: Seven novel single-nucleotide polymorphisms ( SNPs ) were also found , of which a change of leucine 269 to phenylalanine ( Leu269Phe ) was found in 12 of 18 patients with the Arg555Trp mutation .

Example answer:
{"entities": [{"text": "leucine 269 to phenylalanine", "type": "SequenceVariant"}, {"text": "Leu269Phe", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Arg555Trp", "type": "SequenceVariant"}]}

Example input:
Sentence: The normal ( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG due to an insertion of ( GCG ) 4GCA into the normal allele in the Taiwanese OPMD subjects .

Example answer:
{"entities": [{"text": "( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG", "type": "SequenceVariant"}, {"text": "insertion of ( GCG ) 4GCA", "type": "SequenceVariant"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We evaluated the frequency of the XRCC1 Arg399Gln substitution in patients with SLE ( n=265 ) and controls ( n=360 ) in a sample of the Polish population .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , mutation of arginine 124-to-cysteine ( Arg124Cys ) was found in 8 of 18 patients and histidine 626-to-arginine ( His626Arg ) in 2 of 18 patients .

Example answer:
{"entities": [{"text": "arginine 124-to-cysteine", "type": "SequenceVariant"}, {"text": "Arg124Cys", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "histidine 626-to-arginine", "type": "SequenceVariant"}, {"text": "His626Arg", "type": "SequenceVariant"}]}

Example input:
Sentence: Three patients were heterozygous for A207D , G196S , and R266W substitutions .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "A207D", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "R266W", "type": "SequenceVariant"}]}

Example input:
Sentence: The patient showed an R227Q mutation that has been described in an Asian population and MPH patients , along with a novel frameshift mutation , Tdel219 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "R227Q", "type": "SequenceVariant"}, {"text": "MPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Tdel219", "type": "SequenceVariant"}]}

Example input:
Sentence: A known variation , 714C- > ( I238M ) , was also found in the patient with L490R .

Example answer:
{"entities": [{"text": "714C-", "type": "SequenceVariant"}, {"text": "I238M", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "L490R", "type": "SequenceVariant"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Two patients carried a c.262G > A sequence variation predicting for an Ala88Thr exchange which was also detected in 2 normal controls .

## Item biored:test:517
Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results indicated that the presence of CD72- * 2 allele decreases risk for human SLE conferred by FCGR2B-232Thr , possibly by increasing the AS isoform of CD72 .

Example answer:
{"entities": [{"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B-232Thr", "type": "GeneOrGeneProduct"}, {"text": "CD72", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: We conclude that the SNPs of SLC2A2 predict the conversion to diabetes in obese subjects with IGT .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The most strongly associated SNP with SLE was the rs9271366 ( odds ratio , OR = 1.70 , p = 5.6 10 ( -5 ) ) near the HLA-DRB1 gene .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}, {"text": "HLA-DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using the two Asian cohorts , significant association of FCGR2B-232Thr/Thr with SLE was observed only in the presence of CD72- * 1/ * 1 genotype ( OR 4.63 , 95 % CI 1.47-14.6 , P=0.009 versus FCGR2B-232Ile/Ile plus CD72- * 2/ * 2 ) .

Example answer:
{"entities": [{"text": "FCGR2B-232Thr/Thr", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "FCGR2B-232Ile/Ile", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Rs13266634 ( OR = 1.19 , 95 % CI = 1.00-1.42 , p = 0.045 ) in SLC30A8 showed a nominal association with the risk of T2DM , whereas SNPs in IGF2BP2 , FTO and WFS1 were not associated .

## Item biored:test:580
Example input:
Sentence: Mutations of MKS3/TMEM67 , found recently in Meckel-Gruber syndrome ( MKS ) type 3 and Joubert syndrome ( JBTS ) type 6 , are predominantly truncating mutations .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "Meckel-Gruber syndrome ( MKS ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Joubert syndrome ( JBTS ) type 6", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One possibility might be that individuals who are compound heterozygotes for ATM mutations are more common than we realize ..

Example answer:
{"entities": [{"text": "ATM", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Importantly , 35 % ( 6/17 ) are tandem mutations , including 4 UV signature CC to TT transitions possibly linked to modulated DNA repair caused by the immunosuppressive drug cyclosporin A ( CsA ) .

Example answer:
{"entities": [{"text": "CC to TT", "type": "SequenceVariant"}, {"text": "cyclosporin A", "type": "ChemicalEntity"}, {"text": "CsA", "type": "ChemicalEntity"}]}

Example input:
Sentence: The demonstration of mutations giving rise to a slightly milder phenotype in A-T raises the interesting question of what range of phenotypes might occur in individuals in whom both mutations are milder .

Example answer:
{"entities": [{"text": "A-T", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A relatively high frequency of germ-line genomic rearrangements in MLH1 and MSH2 has been reported among Lynch Syndrome ( HNPCC ) patients from different ethnic populations .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We identified such a mechanism as the origin of the mild to asymptomatic phenotype observed in cystic fibrosis patients homozygous for the E831X mutation ( 2623G > T ) in the CFTR gene .

Example answer:
{"entities": [{"text": "cystic fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "E831X", "type": "SequenceVariant"}, {"text": "2623G > T", "type": "SequenceVariant"}, {"text": "CFTR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: This study investigated the influence of TBX21 and HLX1 single nucleotide polymorphisms ( SNPs ) , which have previously been shown to be associated with asthma , on T ( H ) 1/T ( H ) 2 lineage cytokines at birth .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Patients with mild or moderate-severe asthma had similar frequencies of these mutations .

## Item biored:test:565
Example input:
Sentence: RESULTS : In a patient , a C-to-G transition was identified at nucleotide 857 in exon 8 that resulted in a substitution of alanine for proline at amino acid 286 in the first calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "C-to-G transition was identified at nucleotide 857", "type": "SequenceVariant"}, {"text": "alanine for proline at amino acid 286", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The single base pair guanine insertion/deletion polymorphism ( 4G/5G ) within the promoter region of the PAI-1 gene influences PAI-1 synthesis and may modulate hepatic fibrogenesis .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "hepatic fibrogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Computer-based structural analysis revealed that replacement of arginine by glutamine at position 714 transmitted a conformational change to the LBD and the AF-2 transactivation surface , resulting in a decreased binding affinity to ligand and to the LXXLL coactivator motif .

Example answer:
{"entities": [{"text": "arginine by glutamine at position 714", "type": "SequenceVariant"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: In addition to contributing to proteome plasticity , alternative splicing at a NAGNAG tandem site can thus remove a disease-causing UAG stop codon .

Example answer:
{"entities": []}

Example input:
Sentence: The present study highlights the importance of the 5 ' untranslated region ( UTR ) in identification of genes of human disease , suggests that a single-nucleotide substitution in the 5 ' UTR could be associated with protein aggregation , and indicates that the GEF protein is associated with cerebellar degeneration in humans .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "GEF", "type": "GeneOrGeneProduct"}, {"text": "cerebellar degeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Moreover , the only R to G mutation at position 76 was found to strongly impact on protein folding and oligomerization by altering the hydrogen bond network .

Example answer:
{"entities": [{"text": "R to G mutation at position 76", "type": "SequenceVariant"}]}

Example input:
Sentence: The D2267 residue is predicted to coordinate binding of a calcium ion , which influences the conformational binding loops of the C-type lectin domain that mediate interactions with tenascins and other extracellular-matrix proteins .

Example answer:
{"entities": [{"text": "D2267", "type": "SequenceVariant"}, {"text": "calcium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Molecular dynamic ( MD ) simulations showed that the overall effect of the mutation p.Val204Asp is disruption of hydrogen bonding between Gln223 and Glu441 , leading Ser198 and His438 to move away from each other with subsequent disruption of the catalytic triad functionality regardless of the type of substrate .

Example answer:
{"entities": [{"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Input:
Sentence: In silico analysis of the putative impact of the insertion shows serious clashes in protein conformation : this insertion disrupts the alpha5 helix of the dGK kinase domain , rendering the protein unable to bind purine deoxyribonucleosides .

## Item biored:test:571
Example input:
Sentence: The objective of the present study was to examine the association of the T704C polymorphism of exon 2 of the angiotensinogen ( AGT ) gene with HCM in a South Indian population from Andhra Pradesh .

Example answer:
{"entities": [{"text": "T704C", "type": "SequenceVariant"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "AGT", "type": "GeneOrGeneProduct"}, {"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further follow-up of the cohort is required to study the polymorphisms ' relevance for immune-mediated diseases such as childhood asthma .

Example answer:
{"entities": [{"text": "immune-mediated diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , the ACE genotypes correlated with the number of lymph node metastases and the Unio Internationale Contra Cancrum ( UICC ) tumor stage .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "lymph node metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Lack of association between ADRA2B-4825 gene insertion/deletion polymorphism and migraine in Chinese Han population .

Example answer:
{"entities": [{"text": "ADRA2B-4825", "type": "GeneOrGeneProduct"}, {"text": "gene insertion/deletion", "type": "SequenceVariant"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : The present study aimed to estimate the association between susceptibility to migraine and the 12-nucleotide insertion/deletion ( indel ) polymorphism in promoter region of alpha ( 2B ) -adrenergic receptor gene ( ADRA2B ) .

Example answer:
{"entities": [{"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}, {"text": "12-nucleotide insertion/deletion ( indel )", "type": "SequenceVariant"}, {"text": "alpha ( 2B ) -adrenergic receptor", "type": "GeneOrGeneProduct"}, {"text": "ADRA2B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The distribution of the ACE genotypes did not differ significantly from the control group of 189 patients without gastric cancer .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : In the present study , we aimed to substantiate the putative significance of angiotensin I-converting enzyme ( ACE ) on gastric cancer biology by investigating the influence of its gene polymorphism on gastric cancer progression .

Example answer:
{"entities": [{"text": "angiotensin I-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Our study shows that ACE is expressed locally in gastric cancer and that the gene polymorphism influences metastatic behavior .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The following gene polymorphisms were determined in genomic DNA : angiotensin-converting enzyme insertion/deletion polymorphism ( I/D ACE ) , angiotensinogen gene polymorphism ( M 235 ) , angiotensin II receptor type 1 ( ATR1 ) polymorphism ( A 11666C ) , and polymorphism of serotonin transporter gene ( 5HTTLPR ) .Heart rate variability during HUT was assessed in 5-minute intervals by low frequency , high frequency , standard deviation of the normal-to-normal ( SDNN ) , and root mean square successive difference parameters .

Example answer:
{"entities": [{"text": "angiotensin-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "M 235", "type": "SequenceVariant"}, {"text": "angiotensin II receptor type 1", "type": "GeneOrGeneProduct"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "A 11666C", "type": "SequenceVariant"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "5HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This study investigated the influence of TBX21 and HLX1 single nucleotide polymorphisms ( SNPs ) , which have previously been shown to be associated with asthma , on T ( H ) 1/T ( H ) 2 lineage cytokines at birth .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We aimed to investigate the frequency of an ACE gene polymorphism in Turkish asthmatic patients and to determine its impact on clinical parameters and disease severity .

## Item biored:test:439
Example input:
Sentence: One patient with a severe cellular and clinical phenotype was a compound heterozygote with POLG1 mutations in the polymerase and exonuclease domain intrans .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Novel CACNA1S mutation causes autosomal dominant hypokalemic periodic paralysis in a South American family .

Example answer:
{"entities": [{"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "hypokalemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , our study suggests that p.R246Q mutation is common amongst patients with SRD5A2 gene defect from the Northern states of India .

Example answer:
{"entities": [{"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our findings support the notion that mutations in the PCSK9 gene cause autosomal dominant hypercholesterolemia .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "autosomal dominant hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : In two different Caucasian populations , the Czechs and the Azeri , no independent contribution can be detected either of the -1123 promoter SNP or the +2740 3'-UTR SNP , and only the minor allele at PTPN22 codon 620 contributes to the risk of autoimmunity .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The results revealed that the adult offspring kidneys in the PCE group exhibited glomerulosclerosis as well as interstitial fibrosis , accompanied by elevated levels of serum creatinine and urine protein .

Example answer:
{"entities": [{"text": "glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "interstitial fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Twenty-one had Alpers syndrome , the commonest severe POLG1 autosomal recessive phenotype , comprising hepatoencephalopathy and often mtDNA depletion .

Example answer:
{"entities": [{"text": "Alpers syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}, {"text": "hepatoencephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations in the PCSK9 gene in Norwegian subjects with autosomal dominant hypercholesterolemia .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "autosomal dominant hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results demonstrated that PCE could induce dysplasia of fetal kidneys as well as glomerulosclerosis of adult offspring , and the low functional programming of renal AT2R might mediate the developmental origin of adult glomerulosclerosis .

Example answer:
{"entities": [{"text": "dysplasia of fetal kidneys", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AT2R", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Nephronophthisis ( NPHP ) , a rare recessive cystic kidney disease , is the most frequent genetic cause of chronic renal failure in children and young adults .

Example answer:
{"entities": [{"text": "Nephronophthisis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cystic kidney disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chronic renal failure", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: BACKGROUND : Autosomal dominant polycystic kidney disease ( ADPKD ) , which is caused by mutations in polycystins 1 ( PC1 ) and 2 ( PC2 ) , is one of the most commonly inherited renal diseases , affecting ~1 : 1000 Caucasians .

## Item biored:test:563
Example input:
Sentence: In addition to hyperthyroidism , ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers were consistently found in all affected individuals .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Six patients were operated on in the globus pallidus interna ( GPi ) and four in the subthalamic nucleus ( STN ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : Reversible inferior colliculus lesions could be considered as the characteristic for metronidazole-induced encephalopathy , next to the dentate nucleus involvement .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metronidazole-induced", "type": "ChemicalEntity"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude this nonpenetrance may be due to compensatory mutations at a second locus and that mutation within PLCE1 is not always sufficient to cause diffuse mesangial sclerosis .

Example answer:
{"entities": [{"text": "PLCE1", "type": "GeneOrGeneProduct"}, {"text": "diffuse mesangial sclerosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metronidazole-induced", "type": "ChemicalEntity"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Initial MRIs showed abnormal high signal intensities on DWI and FLAIR ( or T2-weighted image ) at the dentate nucleus ( 8/8 ) , inferior colliculus ( 6/8 ) , corpus callosum ( 2/8 ) , pons ( 2/8 ) , medulla ( 1/8 ) , and bilateral cerebral white matter ( 1/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Comparison of unilateral pallidotomy and subthalamotomy findings in advanced idiopathic Parkinson 's disease .

Example answer:
{"entities": [{"text": "idiopathic Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Complications were observed in two patients : one had a left homonymous hemianopsia after pallidotomy and another one developed left hemiballistic movements 3 days after subthalamotomy which partly improved within 1 month with Valproate 1000 mg/day .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "homonymous hemianopsia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Valproate", "type": "ChemicalEntity"}]}

Example input:
Sentence: A prospective , randomized , double-blind pilot study to compare the results of stereotactic unilateral pallidotomy and subthalamotomy in advanced idiopathic Parkinson 's disease ( PD ) refractory to medical treatment was designed .

Example answer:
{"entities": [{"text": "idiopathic Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Interestingly , we found subtentorial abnormal myelination and moderate hyperintensity in the bilateral pallidi in our patients .

## Item biored:test:532
Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The patient homozygous for both L490R and I238M presented with a mild manifestation of hemochromatosis at the age of 41 years .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "L490R", "type": "SequenceVariant"}, {"text": "I238M", "type": "SequenceVariant"}, {"text": "hemochromatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Keratitis-ichthyosis-deafness ( KID ) syndrome is a rare congenital ectodermal disorder , caused by heterozygous missense mutation in GJB2 , encoding the gap junction protein connexin 26 .

Example answer:
{"entities": [{"text": "Keratitis-ichthyosis-deafness ( KID ) syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "congenital ectodermal disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "connexin 26", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Focal dermal hypoplasia ( FDH ) ( OMIM 305600 ) is an X-linked dominant disorder of ecto-mesodermal development .

Example answer:
{"entities": [{"text": "Focal dermal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 305600", "type": "DiseaseOrPhenotypicFeature"}, {"text": "X-linked dominant disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : By clinical examination , the patients and the pedigrees were divided into the following three groups : AN , coloboma of iris and choroids , and the anterior segment malformations including peters anomaly .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coloboma of iris and choroids", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anterior segment malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "peters anomaly", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A patient of Chinese origin with ambiguous genitalia at 14 months , a 46 , XY karyotype , and normal T secretion under human chorionic gonadotropin ( hCG ) stimulation underwent a gonadectomy at 20 months .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "T", "type": "ChemicalEntity"}, {"text": "human chorionic gonadotropin", "type": "ChemicalEntity"}, {"text": "hCG", "type": "ChemicalEntity"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The affected 6-year-old boy had red skin at birth and subsequently developed skin fragility , progressive plantar keratoderma , nail dystrophy , and alopecia .

Example answer:
{"entities": [{"text": "skin fragility", "type": "DiseaseOrPhenotypicFeature"}, {"text": "plantar keratoderma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nail dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alopecia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Here we describe three patients , a boy ( aged 15 years ) and two girls ( aged 17 and 7 years ) with OI type III who suffered intracranial hemorrhage and in addition had brachydactyly and nail hypoplasia .

## Item biored:test:567
Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genomic DNA was extracted from peripheral leukocytes from six affected and three unaffected members of a family with lattice corneal dystrophy type I. Exon 4 of the transforming growth factor-induced gene ( TGFBI ) was screened for the most frequent mutation , R124C , in the proband by sequencing .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor-induced gene", "type": "GeneOrGeneProduct"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "R124C", "type": "SequenceVariant"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: Another POF patient of African origin showed a homozygous nucleotide change in the tenth of DMC1 gene that led to an alteration of the amino acid composition of the protein ( M200V ) .

Example answer:
{"entities": [{"text": "POF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "M200V", "type": "SequenceVariant"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: R58fs mutation in the HGD gene in a family with alkaptonuria in the UAE .

Example answer:
{"entities": [{"text": "R58fs", "type": "SequenceVariant"}, {"text": "HGD", "type": "GeneOrGeneProduct"}, {"text": "alkaptonuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The patient 's GR gene had a heterozygotic mutation ( G -- > A ) at nucleotide position 2141 ( exon 8 ) , which resulted in substitution of arginine by glutamine at amino acid position 714 in the ligand-binding domain ( LBD ) of the GR alpha .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "( G -- > A ) at nucleotide position 2141", "type": "SequenceVariant"}, {"text": "arginine by glutamine at amino acid position 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In conclusion , we report a new DGUOK splice site mutation that provide insight into a critical protein domain ( dGK kinase domain ) and the first founder mutation in a North-African population .

## Item biored:test:542
Example input:
Sentence: The two transversions resulted in the substitution of a stop codon for glutamine at codon 298 ( p.Q298X ) and a missense mutation at codon 358 , tyrosine to histidine ( p.Y358H ) .

Example answer:
{"entities": [{"text": "stop codon for glutamine at codon 298", "type": "SequenceVariant"}, {"text": "p.Q298X", "type": "SequenceVariant"}, {"text": "codon 358 , tyrosine to histidine", "type": "SequenceVariant"}, {"text": "p.Y358H", "type": "SequenceVariant"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: Sequence analysis of aggrecan complementary DNA from an affected individual revealed homozygosity for a missense mutation ( c.6799G -- > A ) that predicts a p.D2267N amino acid substitution in the C-type lectin domain within the G3 domain of aggrecan .

Example answer:
{"entities": [{"text": "aggrecan", "type": "GeneOrGeneProduct"}, {"text": "c.6799G -- > A", "type": "SequenceVariant"}, {"text": "p.D2267N", "type": "SequenceVariant"}]}

Example input:
Sentence: The normal ( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG due to an insertion of ( GCG ) 4GCA into the normal allele in the Taiwanese OPMD subjects .

Example answer:
{"entities": [{"text": "( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG", "type": "SequenceVariant"}, {"text": "insertion of ( GCG ) 4GCA", "type": "SequenceVariant"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The heterozygous c.973G > A transition in exon 9 resulted in a substitution of lysine for glutamic acid at amino acid 325 ( E325K ) in the second calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "c.973G > A", "type": "SequenceVariant"}, {"text": "lysine for glutamic acid at amino acid 325", "type": "SequenceVariant"}, {"text": "E325K", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Sequencing of the GJB2 gene showed that the child was heterozygous for a novel nucleotide change , c.263C > T , in exon 2 , leading to a substitution of alanine for valine at position 88 ( p.Ala88Val ) .

Example answer:
{"entities": [{"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "c.263C > T", "type": "SequenceVariant"}, {"text": "alanine for valine at position 88", "type": "SequenceVariant"}, {"text": "p.Ala88Val", "type": "SequenceVariant"}]}

Example input:
Sentence: DNA sequencing analysis showed the patient to be a compound heterozygote for two mutations in the GPIX gene , a novel nine-nucleotide deletion starting at position 1952 of the gene that changes asparagine 86 for alanine and eliminates amino acids 87 , 88 , and 89 ( arginine , threonine , and proline ) and a previously reported point mutation that changes the codon asparagine ( AAC ) for serine ( AGC ) at residue 45 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GPIX", "type": "GeneOrGeneProduct"}, {"text": "nine-nucleotide deletion starting at position 1952", "type": "SequenceVariant"}, {"text": "changes asparagine 86 for alanine and eliminates amino acids 87 , 88 , and 89 ( arginine , threonine , and proline )", "type": "SequenceVariant"}, {"text": "asparagine ( AAC ) for serine ( AGC ) at residue 45", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Input:
Sentence: Two heterozygous DNA sequence variations were solely present in one single patient each but in none of the 20 normal controls : a duplication of GCC ( c.97GCC [ 9 ] + [ 10 ] ) resulting in an extra alanine within exon 1 and a 25 * G > A substitution in the 3'-untranslated region .
