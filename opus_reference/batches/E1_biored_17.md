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

## Item biored:test:686
Example input:
Sentence: A 3-year-old Chinese boy presented with prominent clinical features of malonic aciduria , including developmental delay , short stature , brain abnormalities and massive excretion of malonic acid and methylmalonic acid .

Example answer:
{"entities": [{"text": "malonic aciduria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "short stature", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "malonic acid", "type": "ChemicalEntity"}, {"text": "methylmalonic acid", "type": "ChemicalEntity"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : This study has identified a new heterozygous de novo mutation in the Cx26 gene ( c.263C > T ; p.Ala88Val ) leading to KID syndrome .

Example answer:
{"entities": [{"text": "Cx26", "type": "GeneOrGeneProduct"}, {"text": "c.263C > T", "type": "SequenceVariant"}, {"text": "p.Ala88Val", "type": "SequenceVariant"}, {"text": "KID syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In LCD , three novel heterozygous mutations found were glycine-594-valine ( Gly594Val ) in 2 of 18 patients , valine-539-aspartic acid ( Val539Asp ) in 1 patient , and deletion of valine 624 , valine 625 ( Val624-Val625del ) in 1 patient .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glycine-594-valine", "type": "SequenceVariant"}, {"text": "Gly594Val", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "valine-539-aspartic acid", "type": "SequenceVariant"}, {"text": "Val539Asp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion of valine 624 , valine 625", "type": "SequenceVariant"}, {"text": "Val624-Val625del", "type": "SequenceVariant"}]}

Example input:
Sentence: Atypical clinical features for LCD were noted in patients with the Gly594Val and Val624-Val625del mutations .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Gly594Val", "type": "SequenceVariant"}, {"text": "Val624-Val625del", "type": "SequenceVariant"}]}

Example input:
Sentence: A novel mutation in the connexin 26 gene ( GJB2 ) in a child with clinical and histological features of keratitis-ichthyosis-deafness ( KID ) syndrome .

Example answer:
{"entities": [{"text": "connexin 26", "type": "GeneOrGeneProduct"}, {"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "keratitis-ichthyosis-deafness ( KID ) syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Novel compound heterozygous mutation of MLYCD in a Chinese patient with malonic aciduria .

Example answer:
{"entities": [{"text": "MLYCD", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "malonic aciduria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: A Taiwanese boy with congenital generalized lipodystrophy caused by homozygous Ile262fs mutation in the BSCL2 gene .

## Item biored:test:702
Example input:
Sentence: We progressively screened DNA samples from 613 individuals with ID initially for the most frequent ARX mutations ( c.304ins ( GCG ) ( 7 ) 'expansion ' of pA1 and c.429_452dup 'dup24bp ' of pA2 ) .

Example answer:
{"entities": [{"text": "ID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARX", "type": "GeneOrGeneProduct"}, {"text": "c.304ins ( GCG ) ( 7 )", "type": "SequenceVariant"}, {"text": "c.429_452dup", "type": "SequenceVariant"}]}

Example input:
Sentence: 480 subjects were studied : 240 patients with premature CAD , 240 age and sex matched blood donors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interestingly , a nucleotide insertion of c.1146+25insA in exon 6 was detected in five VSD patients , but not in 486 normal healthy controls .

Example answer:
{"entities": [{"text": "c.1146+25insA", "type": "SequenceVariant"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Cheek swab samples were obtained for DNA analysis from 116 case/parent trios .

Example answer:
{"entities": []}

Example input:
Sentence: DNA was extracted from the blood drawn from 399 prostate cancer patients , 150 BPH patients and 294 healthy community controls .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : This study included 133 patients with AVSD and 200 healthy controls .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AVSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : DNA was collected from 191 patients ( mean age 44+/-18 years , 61 men , 130 women ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Genomic DNA was isolated from the venous blood leukocytes of 322 unrelated patients with schizophrenia , 156 patients with depression , 300 patients with heroin addiction , and 300 healthy unrelated individuals .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : DNA samples of 126 SIDS cases and 261 controls were investigated .

Example answer:
{"entities": [{"text": "SIDS", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We used 15 DNA samples ( 8 validation samples and 7 samples of clinically suspected vEDS patients ) in this study .

## Item biored:test:694
Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These included missense ( p.T286M ) and nonsense ( p.W111X ) mutations and a transition in the obligate AG-dinucleotide of the intron 8 acceptor splice site ( c.610-2A > G ) .

Example answer:
{"entities": [{"text": "p.T286M", "type": "SequenceVariant"}, {"text": "p.W111X", "type": "SequenceVariant"}, {"text": "AG-dinucleotide", "type": "SequenceVariant"}, {"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: Sequencing of the GJB2 gene showed that the child was heterozygous for a novel nucleotide change , c.263C > T , in exon 2 , leading to a substitution of alanine for valine at position 88 ( p.Ala88Val ) .

Example answer:
{"entities": [{"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "c.263C > T", "type": "SequenceVariant"}, {"text": "alanine for valine at position 88", "type": "SequenceVariant"}, {"text": "p.Ala88Val", "type": "SequenceVariant"}]}

Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Example input:
Sentence: In 10 of these families , all the homozygotes have a 137-bp insertion in their cDNA caused by a point mutation in a sequence resembling a splice-donor site .

Example answer:
{"entities": [{"text": "137-bp insertion", "type": "SequenceVariant"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : In this family , a heterozygous cytosine insertion in exon 10 ( c.1546_1547insC ) inducing a frame shift mutation of MEN1 was found in the proband and the other two suffering members of his family .

Example answer:
{"entities": [{"text": "cytosine insertion", "type": "SequenceVariant"}, {"text": "c.1546_1547insC", "type": "SequenceVariant"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Interestingly , a nucleotide insertion of c.1146+25insA in exon 6 was detected in five VSD patients , but not in 486 normal healthy controls .

Example answer:
{"entities": [{"text": "c.1146+25insA", "type": "SequenceVariant"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In addition , each affected child was heterozygous for the G1681A mutation in exon 7 that led to an Ala467Thr substitution in POLG , within the linker region of the protein .

Example answer:
{"entities": [{"text": "G1681A", "type": "SequenceVariant"}, {"text": "Ala467Thr", "type": "SequenceVariant"}, {"text": "POLG", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: He had a homozygous insertion of a nucleotide , 783insG ( Ile262fs mutation ) , in exon 7 of the BSCL2 gene .

## Item biored:test:655
Example input:
Sentence: We evaluated the frequency of the XRCC1 Arg399Gln substitution in patients with SLE ( n=265 ) and controls ( n=360 ) in a sample of the Polish population .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A known variation , 714C- > ( I238M ) , was also found in the patient with L490R .

Example answer:
{"entities": [{"text": "714C-", "type": "SequenceVariant"}, {"text": "I238M", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "L490R", "type": "SequenceVariant"}]}

Example input:
Sentence: The patient showed an R227Q mutation that has been described in an Asian population and MPH patients , along with a novel frameshift mutation , Tdel219 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "R227Q", "type": "SequenceVariant"}, {"text": "MPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Tdel219", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In LCD , three novel heterozygous mutations found were glycine-594-valine ( Gly594Val ) in 2 of 18 patients , valine-539-aspartic acid ( Val539Asp ) in 1 patient , and deletion of valine 624 , valine 625 ( Val624-Val625del ) in 1 patient .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glycine-594-valine", "type": "SequenceVariant"}, {"text": "Gly594Val", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "valine-539-aspartic acid", "type": "SequenceVariant"}, {"text": "Val539Asp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion of valine 624 , valine 625", "type": "SequenceVariant"}, {"text": "Val624-Val625del", "type": "SequenceVariant"}]}

Example input:
Sentence: Although the sP120T substitution also impaired HBsAg secretion , it did not enhance the replication of LAM-resistant clones .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}]}

Example input:
Sentence: Three patients were heterozygous for A207D , G196S , and R266W substitutions .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "A207D", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "R266W", "type": "SequenceVariant"}]}

Example input:
Sentence: We therefore systematically analyzed the functional impact of the most prevalent immune escape variants , the sG145R and sP120T mutants , on the viral replication efficacy and antiviral drug susceptibility of common treatment-associated mutants with resistance to lamivudine ( LAM ) and/or HBeAg negativity .

Example answer:
{"entities": [{"text": "lamivudine", "type": "ChemicalEntity"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg", "type": "ChemicalEntity"}]}

Example input:
Sentence: In all clones with combined immune escape and LAM resistance mutations , the nucleotide analogues adefovir and tenofovir remained effective in suppressing viral replication in vitro .

Example answer:
{"entities": [{"text": "LAM", "type": "ChemicalEntity"}, {"text": "adefovir", "type": "ChemicalEntity"}, {"text": "tenofovir", "type": "ChemicalEntity"}]}

Example input:
Sentence: Replication-competent HBV strains with sG145R or sP120T and LAM resistance ( rtM204I or rtL180M/rtM204V ) were generated on an HBeAg-positive and an HBeAg-negative background with precore ( PC ) and basal core promoter ( BCP ) mutants .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg-positive", "type": "ChemicalEntity"}, {"text": "HBeAg-negative", "type": "ChemicalEntity"}, {"text": "precore", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: LAM resistance substitutions ( rtL180M + rtM204V ) were detected in 10 ( 50 % ) of the 20 patients with viremia .

## Item biored:test:662
Example input:
Sentence: A Cys 23-Ser 23 substitution in the 5-HT ( 2C ) receptor gene influences body weight regulation in females with seasonal affective disorder : an Austrian-Canadian collaborative study .

Example answer:
{"entities": [{"text": "Cys 23-Ser 23", "type": "SequenceVariant"}, {"text": "5-HT ( 2C ) receptor", "type": "GeneOrGeneProduct"}, {"text": "seasonal affective disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The selective 5-HT6 receptor antagonist Ro4368554 restores memory performance in cholinergic and serotonergic models of memory deficiency in the rat .

Example answer:
{"entities": [{"text": "5-HT6 receptor", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "serotonergic", "type": "ChemicalEntity"}, {"text": "memory deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: Because 5-HT transporters play a key element in the regulation of synaptic 5-HT transmission it may be important to control for the potential covariance effect of a polymorphism in the 5-HT transporter promoter gene region ( 5-HTTLPR ) when studying the effects of MDMA as well as cognitive functioning .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "5-HT transporter promoter gene region", "type": "GeneOrGeneProduct"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Serotonin transporter gene polymorphic element 5-HTTLPR increases the risk of sporadic Parkinson 's disease in Italy .

Example answer:
{"entities": [{"text": "Serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The phosphatidylethanolamine N-methyltransferase gene V175M single nucleotide polymorphism confers the susceptibility to NASH in Japanese population .

Example answer:
{"entities": [{"text": "phosphatidylethanolamine N-methyltransferase", "type": "GeneOrGeneProduct"}, {"text": "V175M", "type": "SequenceVariant"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although 3,4-methylenedioxymethamphetamine ( MDMA or ecstasy ) has been shown to damage brain serotonin ( 5-HT ) neurons in animals and possibly humans , little is known about the long-term consequences of MDMA-induced 5-HT neurotoxic lesions on functions in which 5-HT is involved , such as cognitive function .

Example answer:
{"entities": [{"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "MDMA-induced", "type": "ChemicalEntity"}, {"text": "neurotoxic lesions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Memory function and serotonin transporter promoter gene polymorphism in ecstasy ( MDMA ) users .

Example answer:
{"entities": [{"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: This study investigated the possible association between three functional polymorphisms in the promoter region of the dopamine D4 receptor ( DRD4 ) gene and schizophrenia , depression , and heroin addiction .

Example answer:
{"entities": [{"text": "dopamine D4 receptor", "type": "GeneOrGeneProduct"}, {"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Antagonists at serotonin type 6 ( 5-HT ( 6 ) ) receptors show activity in models of learning and memory .

Example answer:
{"entities": [{"text": "serotonin type 6 ( 5-HT ( 6 ) ) receptors", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conducted an association study assessing how PD risk in Italy was influenced by the serotonin transporter gene ( SLC6A4 ) polymorphic region 5-HTTLPR , consisting of an insertion/deletion ( long allele-L/short allele-S ) of 43 bp in the SLC6A4 promoter region .

Example answer:
{"entities": [{"text": "PD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "SLC6A4", "type": "GeneOrGeneProduct"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "insertion/deletion ( long allele-L/short allele-S ) of 43 bp", "type": "SequenceVariant"}]}

Input:
Sentence: Serotonin 6 receptor gene is associated with methamphetamine-induced psychosis in a Japanese population .

## Item biored:test:665
Example input:
Sentence: Effects of the antidepressant trazodone , a 5-HT 2A/2C receptor antagonist , on dopamine-dependent behaviors in rats .

Example answer:
{"entities": [{"text": "trazodone", "type": "ChemicalEntity"}, {"text": "5-HT 2A/2C receptor", "type": "GeneOrGeneProduct"}, {"text": "dopamine-dependent", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Compound 1 is a potent A ( 2A ) /A ( 1 ) receptor antagonist in vitro ( A ( 2A ) K ( i ) = 4.1 nM ; A ( 1 ) K ( i ) = 17.0 nM ) that has excellent activity , after oral administration , across a number of animal models of Parkinson 's disease including mouse and rat models of haloperidol-induced catalepsy , mouse model of reserpine-induced akinesia , rat 6-hydroxydopamine ( 6-OHDA ) lesion model of drug-induced rotation , and MPTP-treated non-human primate model .

Example answer:
{"entities": [{"text": "A ( 2A ) /A ( 1 ) receptor antagonist", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "reserpine-induced", "type": "ChemicalEntity"}, {"text": "akinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "6-hydroxydopamine", "type": "ChemicalEntity"}, {"text": "6-OHDA", "type": "ChemicalEntity"}, {"text": "MPTP-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: In experiments using specific adrenergic antagonists , we found that pretreatment with the beta-adrenergic receptor antagonist propranolol blocked cocaine-induced anxiety-like behavior in Dbh +/- and wild-type C57BL6/J mice , while the alpha ( 1 ) antagonist prazosin and the alpha ( 2 ) antagonist yohimbine had no effect .

Example answer:
{"entities": [{"text": "adrenergic antagonists", "type": "ChemicalEntity"}, {"text": "beta-adrenergic receptor", "type": "GeneOrGeneProduct"}, {"text": "propranolol", "type": "ChemicalEntity"}, {"text": "cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "alpha ( 1 )", "type": "GeneOrGeneProduct"}, {"text": "prazosin", "type": "ChemicalEntity"}, {"text": "alpha ( 2 )", "type": "GeneOrGeneProduct"}, {"text": "yohimbine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In conclusion , although Ro4368554 did not improve a time-related retention deficit , it reversed a cholinergic and a serotonergic memory deficit , suggesting that both mechanisms may be involved in the facilitation of object memory by Ro4368554 and , possibly , other 5-HT ( 6 ) receptor antagonists .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-HT ( 6 ) receptor", "type": "ChemicalEntity"}]}

Example input:
Sentence: We suggest that trazodone ( 5 , 10 and 20 mg/kg ) , by blocking the 5-HT 2C receptors , releases the nigrostriatal DAergic neurons from tonic inhibition caused by 5-HT , and thereby potentiates dexamphetamine stereotypy and antagonizes haloperidol catalepsy .

Example answer:
{"entities": [{"text": "5-HT 2C", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Antagonists at serotonin type 6 ( 5-HT ( 6 ) ) receptors show activity in models of learning and memory .

Example answer:
{"entities": [{"text": "serotonin type 6 ( 5-HT ( 6 ) ) receptors", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT ( 6 )", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "serotonergic-", "type": "ChemicalEntity"}, {"text": "tryptophan", "type": "ChemicalEntity"}, {"text": "TRP", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: The selective 5-HT6 receptor antagonist Ro4368554 restores memory performance in cholinergic and serotonergic models of memory deficiency in the rat .

Example answer:
{"entities": [{"text": "5-HT6 receptor", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "serotonergic", "type": "ChemicalEntity"}, {"text": "memory deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Input:
Sentence: In addition , the disrupted prepulse inhibition induced by d-amphetamine or phencyclidine was restored by 5-HT6 receptor antagonist in an animal study using rats .

## Item biored:test:712
Example input:
Sentence: RESULTS : By clinical examination , the patients and the pedigrees were divided into the following three groups : AN , coloboma of iris and choroids , and the anterior segment malformations including peters anomaly .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coloboma of iris and choroids", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anterior segment malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "peters anomaly", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Thirty-seven unrelated patients were studied , 18 with LCD and 19 with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Three generations of family members were positively diagnosed with lattice corneal dystrophy .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Analysis of a nuclear family with three affected offspring identified an autosomal-recessive form of spondyloepimetaphyseal dysplasia characterized by severe short stature and a unique constellation of radiographic findings .

Example answer:
{"entities": [{"text": "spondyloepimetaphyseal dysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "short stature", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A combined clinical and genetic study was conducted in a cohort of patients with CDSRR , to substantiate these prior RESULTS : Seventeen patients from 13 families underwent a detailed ophthalmic examination including color vision testing , Goldmann visual fields , fundus photography , Ganzfeld and multifocal ERGs , and optical coherence tomography .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : Cone dystrophy with supernormal rod response ( CDSRR ) is a retinal disorder characterized by reduced visual acuity , color vision defects , and specific alterations of ERG responses that feature elevated scotopic b-wave amplitudes at high luminance intensities .

Example answer:
{"entities": [{"text": "Cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "retinal disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "color vision defects", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : To identify the underlying genetic defect in a four-generation family of Chinese origin with autosomal dominant congenital cataract-microcornea syndrome ( CCMC ) .

Example answer:
{"entities": [{"text": "genetic defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCMC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cone dystrophy with supernormal rod response is strictly associated with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "Cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : The phenotype of cone dystrophy with supernormal rod response is tightly linked with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Material and Methods : Twenty-four unrelated patients diagnosed with cone dystrophy or cone rod dystrophy according to standard diagnostic criteria and a family history consistent with an autosomal dominant mode of inheritance were included in the study .

## Item biored:test:687
Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Congenital disorder of glycosylation Ic due to a de novo deletion and an hALG-6 mutation .

Example answer:
{"entities": [{"text": "Congenital disorder of glycosylation Ic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hALG-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Deficiency of the muscle isozyme of glycogen phosphorylase is causative of McArdle disease or Glycogen storage disease type V ( GSD-V ) , the most common autosomal recessive disorder of glycogen metabolism .

Example answer:
{"entities": [{"text": "Deficiency of the muscle isozyme of glycogen phosphorylase", "type": "DiseaseOrPhenotypicFeature"}, {"text": "McArdle disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Glycogen storage disease type V", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GSD-V", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal recessive disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glycogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: We describe a new cause of congenital disorder of glycosylation-Ic ( CDG-Ic ) in a young girl with a rather mild CDG phenotype .

Example answer:
{"entities": [{"text": "congenital disorder of glycosylation-Ic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDG-Ic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDG", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Recently , mutations in phospholipase C epsilon 1 ( PLCE1 ) were found to cause a nonsyndromic , autosomal recessive form of this disease .

Example answer:
{"entities": [{"text": "phospholipase C epsilon 1", "type": "GeneOrGeneProduct"}, {"text": "PLCE1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These findings identify an autosomal-recessive skeletal dysplasia and a significant role for the aggrecan C-type lectin domain in regulating endochondral ossification and , thereby , height .

Example answer:
{"entities": [{"text": "autosomal-recessive skeletal dysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aggrecan", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the TGFBI gene in Indian patients with lattice corneal dystrophy ( LCD ) or granular corneal dystrophy ( GCD ) and to look for genotype-phenotype correlations .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "granular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Peroxisomal proliferator activated receptor-gamma deficiency in a Canadian kindred with familial partial lipodystrophy type 3 ( FPLD3 ) .

Example answer:
{"entities": [{"text": "Peroxisomal proliferator activated receptor-gamma", "type": "GeneOrGeneProduct"}, {"text": "familial partial lipodystrophy type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Classic galactosemia is an autosomal recessive disorder of galactose metabolism manifesting in the first weeks of life following exposure to a milk-based diet .

Example answer:
{"entities": [{"text": "Classic galactosemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal recessive disorder of galactose metabolism", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Congenital generalized lipodystrophy ( CGL ) is a rare autosomal recessive disease that is characterized by a near-complete absence of adipose tissue from birth or early infancy .

## Item biored:test:706
Example input:
Sentence: VEGF-stimulated hRMVEC proliferation was measured following transfection with NOX4 siRNA or STAT3 siRNA , or respective controls .

Example answer:
{"entities": [{"text": "VEGF-stimulated", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Genomic DNA was screened for GLDC , AMT , and GCSH gene mutations .

Example answer:
{"entities": [{"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "AMT", "type": "GeneOrGeneProduct"}, {"text": "GCSH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We did not observe any correlation between the Ser1245Cys polymorphism of the hOGG1 gene and gastric cancer , including subjects with impaired DNA repair and/or high levels of endogenous oxidative DNA lesions .

Example answer:
{"entities": [{"text": "Ser1245Cys", "type": "SequenceVariant"}, {"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Taken together , our results demonstrated that Sag is a Kras ( G12D ) -cooperating oncogene required for Kras ( G12D ) -induced immortalization and transformation , and targeting SAG-SCF E3 ligase may , therefore , have therapeutic value for senescence-based cancer treatment .

Example answer:
{"entities": [{"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}, {"text": "SAG-SCF", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The metrics from DNA damage and repair study were correlated with the genotypes of common polymorphisms of the hOGG1 and RAD51 genes : a G -- > C transversion at 1245 position of the hOGG1 gene producing a Ser -- > Cys substitution at the codon 326 ( the Ser326Cys polymorphism ) and a G -- > C substitution at position 135 ( 5'-untranslated region ) of the RAD51 gene ( the G135C polymorphism ) .

Example answer:
{"entities": [{"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "RAD51", "type": "GeneOrGeneProduct"}, {"text": "G -- > C transversion at 1245 position", "type": "SequenceVariant"}, {"text": "Ser -- > Cys substitution at the codon 326", "type": "SequenceVariant"}, {"text": "Ser326Cys", "type": "SequenceVariant"}, {"text": "G -- > C substitution at position 135", "type": "SequenceVariant"}, {"text": "G135C", "type": "SequenceVariant"}]}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Input:
Sentence: The use of hrMCA in combination with SAG from genomic DNA enables rapid detection of COL3A1 mutations with high efficiency and specificity .

## Item biored:test:720
Example input:
Sentence: Mutations of TP53 and dysfunction of the Brca1 and/or Brca2 tumor-suppressor proteins have been implicated in the molecular pathogenesis of a large fraction of OSCs , but frequent somatic mutations in other well-established tumor-suppressor genes have not been identified .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "Brca1", "type": "GeneOrGeneProduct"}, {"text": "Brca2", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Seven hundred fifty three subjects , corresponding to 251 full trios of childhood-onset SLE families , were genotyped and analyzed using transmission disequilibrium testing ( TDT ) and multitest corrections .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Four patients harbor yet non-described SRD5A2 gene mutations : a single nucleotide deletion ( del642T ) , a G158R amino acid substitution , a splice junction mutation ( IVS3+1G > A ) , and the insertion of a cytosine ( 217_218insC ) occurring at a CCCC motif .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G158R", "type": "SequenceVariant"}, {"text": "IVS3+1G > A", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}]}

Example input:
Sentence: The OR for the 399 Gln allele in patients with SLE was 1.406 ( 95 % CI=1.111-1.779 , p=0.0045 ) .

Example answer:
{"entities": [{"text": "399 Gln", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Similarly , NF1 alterations including homozygous deletions and splicing mutations were identified in 9 ( 22 % ) of 41 primary OSCs .

Example answer:
{"entities": [{"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: More than 100 different heterozygous mutations in copper/zinc superoxide dismutase ( SOD1 ) have been found in patients with amyotrophic lateral sclerosis ( ALS ) , a fatal neurodegenerative disease .

Example answer:
{"entities": [{"text": "copper/zinc superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegenerative disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Nine distinct mutations including one small deletion mutation ( 46delS ) , two small insertion mutations ( 118-119insA and 125-126insAA ) , and six non-synonymous mutations ( A6V , P163S , E359K , P407Q , S429T and A442V ) were identified in 12 of the 486 patients ( nine with ventricular septal defect , two with Tetralogy of Fallot , and one with endocardial cushion defect ) .

Example answer:
{"entities": [{"text": "46delS", "type": "SequenceVariant"}, {"text": "118-119insA", "type": "SequenceVariant"}, {"text": "125-126insAA", "type": "SequenceVariant"}, {"text": "A6V", "type": "SequenceVariant"}, {"text": "P163S", "type": "SequenceVariant"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "P407Q", "type": "SequenceVariant"}, {"text": "S429T", "type": "SequenceVariant"}, {"text": "A442V", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Tetralogy of Fallot", "type": "DiseaseOrPhenotypicFeature"}, {"text": "endocardial cushion defect", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Input:
Sentence: More than 70 mutations have been identified in SLS patients , including small deletions or insertions , missense mutations , splicing defects and complex nucleotide changes .

## Item biored:test:726
Example input:
Sentence: Seven hundred fifty three subjects , corresponding to 251 full trios of childhood-onset SLE families , were genotyped and analyzed using transmission disequilibrium testing ( TDT ) and multitest corrections .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , the meta-analysis of Taiwanese Han Chinese , Brazilian , and Polish populations showed that the Gln/Gln or Gln/Arg genotype and Gln allele were associated with SLE incidence .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations of TP53 and dysfunction of the Brca1 and/or Brca2 tumor-suppressor proteins have been implicated in the molecular pathogenesis of a large fraction of OSCs , but frequent somatic mutations in other well-established tumor-suppressor genes have not been identified .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "Brca1", "type": "GeneOrGeneProduct"}, {"text": "Brca2", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: In addition , two SNPs found in a GWAS of European ancestry women were confirmed in our study , indicating that African Americans share some genetic risk factors for SLE with European and Chinese subjects .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The OR for the 399 Gln allele in patients with SLE was 1.406 ( 95 % CI=1.111-1.779 , p=0.0045 ) .

Example answer:
{"entities": [{"text": "399 Gln", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The most strongly associated SNP with SLE was the rs9271366 ( odds ratio , OR = 1.70 , p = 5.6 10 ( -5 ) ) near the HLA-DRB1 gene .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}, {"text": "HLA-DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Input:
Sentence: These studies suggest that large gene deletions may account for up to 5 % of the mutant alleles in SLS .

## Item biored:test:710
Example input:
Sentence: Using direct sequencing a point mutation ( 144 G > A ) resulting in a Q48H substitution in exon 1 of the MYOC gene was observed in five of the eight glaucoma patients , but not in unaffected family members and 100 unrelated controls .

Example answer:
{"entities": [{"text": "144 G > A", "type": "SequenceVariant"}, {"text": "Q48H", "type": "SequenceVariant"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Genomic DNA was extracted from peripheral leukocytes from six affected and three unaffected members of a family with lattice corneal dystrophy type I. Exon 4 of the transforming growth factor-induced gene ( TGFBI ) was screened for the most frequent mutation , R124C , in the proband by sequencing .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor-induced gene", "type": "GeneOrGeneProduct"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "R124C", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: The relationship between microcoria , glaucoma , and the MYOC Q48H mutation in this family is discussed .

Example answer:
{"entities": [{"text": "microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "Q48H", "type": "SequenceVariant"}]}

Example input:
Sentence: A G1103R mutation in CRB1 is co-inherited with high hyperopia and Leber congenital amaurosis .

Example answer:
{"entities": [{"text": "G1103R", "type": "SequenceVariant"}, {"text": "CRB1", "type": "GeneOrGeneProduct"}, {"text": "hyperopia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Leber congenital amaurosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , eight individuals who had both microcoria and glaucoma were screened for glaucoma genes : myocilin ( MYOC ) , optineurin ( OPTN ) and CYP1B1 .

Example answer:
{"entities": [{"text": "microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocilin", "type": "GeneOrGeneProduct"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "optineurin", "type": "GeneOrGeneProduct"}, {"text": "OPTN", "type": "GeneOrGeneProduct"}, {"text": "CYP1B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the TGFBI gene in Indian patients with lattice corneal dystrophy ( LCD ) or granular corneal dystrophy ( GCD ) and to look for genotype-phenotype correlations .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "granular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Data presented here supports the hypothesis that congenital microcoria is a potential risk factor for glaucoma , although this observation is complicated by the partial segregation of MYOC Q48H ( 1q24.3-q25.2 ) , a mutation known to be associated with glaucoma in India .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "Q48H", "type": "SequenceVariant"}]}

Example input:
Sentence: The result expands the mutation spectrum of GJA8 in associated with congenital cataract and microcornea , and implies that this gene has direct involvement with the development of the lens as well as the other anterior segment of the eye .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcornea", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: However , the role of GUCA1B gene mutations in inherited retinal disease has been controversial .

## Item biored:test:691
Example input:
Sentence: Hypomorphic mutations in meckelin ( MKS3/TMEM67 ) cause nephronophthisis with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "meckelin", "type": "GeneOrGeneProduct"}, {"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "nephronophthisis with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Twenty-one had Alpers syndrome , the commonest severe POLG1 autosomal recessive phenotype , comprising hepatoencephalopathy and often mtDNA depletion .

Example answer:
{"entities": [{"text": "Alpers syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}, {"text": "hepatoencephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients who develop ESRD have a higher preoperative and 1-year serum creatinine and are more likely to have hepatorenal syndrome .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "ChemicalEntity"}, {"text": "escitalopram", "type": "ChemicalEntity"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Recently , a lethal phenotype characterized by sudden infant death with dysgenesis of the testes syndrome ( SIDDT ) was identified to be caused by loss of function mutations in the TSPYL1 gene .

Example answer:
{"entities": [{"text": "sudden infant death with dysgenesis of the testes syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SIDDT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSPYL1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , accumulated F4/80 ( + ) cells in the liver metastasis were not BM-derived F4/80 ( + ) cells , but mainly resident hepatic F4/80 ( + ) cells , and these resident hepatic F4/80 ( + ) cells were positive for TGF-b1 .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Clinically significant anemia ( hemoglobin < 7 g/dL ) was observed in 5.4 % of patients ( CD4 , 165 cells/microL ) and hepatitis ( clinical jaundice with alanine aminotransferase > 5 times upper limits of normal ) in 3.5 % of patients ( CD4 , 260 cells/microL ) .

Example answer:
{"entities": [{"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hemoglobin", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "hepatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "jaundice", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alanine aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Serum alpha-GST levels were significantly elevated by day 4 , which corresponded to hepatotoxicity as shown by the increasing incidence of inflammation of the liver capsule , necrosis , and steatosis throughout the study .

Example answer:
{"entities": [{"text": "alpha-GST", "type": "GeneOrGeneProduct"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation of the liver capsule", "type": "DiseaseOrPhenotypicFeature"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Hypomorphic MKS3/TMEM67 mutations cause NPHP with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "NPHP with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: His liver was cirrhotic with parenchymal iron deposits and the result of a glucose tolerance test was compatible with diabetes mellitus .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "iron", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Hepatomegaly was noticed , and histological examination of a liver biopsy specimen suggested severe hepatic steatosis and periportal necrosis .

## Item biored:test:752
Example input:
Sentence: Mutation analysis in a Chinese family with multiple endocrine neoplasia type 1 .

Example answer:
{"entities": [{"text": "multiple endocrine neoplasia type 1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The patient showed an R227Q mutation that has been described in an Asian population and MPH patients , along with a novel frameshift mutation , Tdel219 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "R227Q", "type": "SequenceVariant"}, {"text": "MPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Tdel219", "type": "SequenceVariant"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: This mutation was responsible for the familial disorder through the substitution of a highly conserved arginine to tryptophan at codon 198 ( p.R198W ) .

Example answer:
{"entities": [{"text": "arginine to tryptophan at codon 198", "type": "SequenceVariant"}, {"text": "p.R198W", "type": "SequenceVariant"}]}

Example input:
Sentence: We identified and characterized a PABPN1 mutation in a Taiwanese family with OPMD .

Example answer:
{"entities": [{"text": "PABPN1", "type": "GeneOrGeneProduct"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: The exon 4 sequence of TGFBI of the proband exhibits the heterozygous single-nucleotide mutation , C417T , leading to amino acid substitution ( R124C ) in the encoded TGF-induced protein .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "C417T", "type": "SequenceVariant"}, {"text": "R124C", "type": "SequenceVariant"}, {"text": "TGF-induced protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In our present study , a third Chinese family with this mutation was identified , suggesting that this mutation is a prevalent CYP17 mutation in the Chinese population .

Example answer:
{"entities": [{"text": "CYP17", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The mutation identified in the proband was screened in the other family members and the 170 healthy Chinese individuals by direct sequencing .

## Item biored:test:684
Example input:
Sentence: CONCLUSIONS : In contrast to a single GCG expansion in most of OPMD patients in the literature , an insertion of ( GCG ) 4GCA in the PABPN1 gene was found in the Taiwanese OPMD subjects .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "insertion of ( GCG ) 4GCA", "type": "SequenceVariant"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The single nucleotide polymorphism Gly ( 388 ) Arg in FGFR4 is not associated with increased risk of prostate cancer in Scottish men .

Example answer:
{"entities": [{"text": "Gly ( 388 ) Arg", "type": "SequenceVariant"}, {"text": "FGFR4", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: A Stratified analysis of the genotypes with age of onset and tumor grade showed the w1/m1 genotype to be significantly associated with an early age of onset ; however the tumor grades did not have significant association with the variant genotypes .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Its +1858C > T ( R620W ) polymorphism has been shown to associate with a risk for multiple autoimmune diseases , including type 1 diabetes ( T1D ) and juvenile idiopathic arthritis ( JIA ) .

Example answer:
{"entities": [{"text": "+1858C > T", "type": "SequenceVariant"}, {"text": "R620W", "type": "SequenceVariant"}, {"text": "autoimmune diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "juvenile idiopathic arthritis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The normal ( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG due to an insertion of ( GCG ) 4GCA into the normal allele in the Taiwanese OPMD subjects .

Example answer:
{"entities": [{"text": "( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG", "type": "SequenceVariant"}, {"text": "insertion of ( GCG ) 4GCA", "type": "SequenceVariant"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: ( CCTTT ) 14 , which has been reported to have a higher activity in a reporter-construct , was significantly more abundant in POAG patients , while ( CCTTT ) 10 and ( CCTTT ) 13 were less common .

Example answer:
{"entities": [{"text": "( CCTTT ) 14", "type": "SequenceVariant"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "( CCTTT ) 10", "type": "SequenceVariant"}, {"text": "( CCTTT ) 13", "type": "SequenceVariant"}]}

Example input:
Sentence: There was a significant association between the GSTP1 Ile/Val genotype and the advanced age group among the cases .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}]}

Example input:
Sentence: Also it appears that preferential premolar agenesis is associated with FGFR1 ( P = 0.014 ) and IRF6 ( P = 0.002 ) markers .

Example answer:
{"entities": [{"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "IRF6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Though FAS-670 polymorphisms did not show any significant difference , the proportion of subjects with IL1B-31TT ( or IL1B-511CC ) increased according to stage ( trend P=0.019 ) .

Example answer:
{"entities": [{"text": "FAS-670", "type": "GeneOrGeneProduct"}, {"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The FGG 10034C > T polymorphism was furthermore not associated with age at onset of PAD .

## Item biored:test:753
Example input:
Sentence: In contrast , the protein abundances of Na ( + ) /H ( + ) exchanger type 3 ( NHE3 ) , Na ( + ) -K ( + ) -2Cl ( - ) cotransporter ( BSC-1 ) , and thiazide-sensitive Na ( + ) -Cl ( - ) cotransporter ( TSC ) were decreased .

Example answer:
{"entities": [{"text": "Na ( + ) /H ( + ) exchanger type 3", "type": "GeneOrGeneProduct"}, {"text": "NHE3", "type": "GeneOrGeneProduct"}, {"text": "Na ( + ) -K ( + ) -2Cl ( - ) cotransporter", "type": "GeneOrGeneProduct"}, {"text": "BSC-1", "type": "GeneOrGeneProduct"}, {"text": "thiazide-sensitive Na ( + ) -Cl ( - ) cotransporter", "type": "GeneOrGeneProduct"}, {"text": "TSC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: A haplotype containing these four SNPs ( CATA ) significantly increased protection of wet AMD with a P value of 0.0005 and an odds ratio of 0.29 ( 95 % confidence interval : 0.15-0.60 ) .

Example answer:
{"entities": [{"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Western blot analysis and reverse transcription-polymerase chain reaction were used to detect target gene and protein expression .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : We performed comprehensive genomic profiling ( CGP ) for coding regions in more than 300 cancer-related genes of 186 GISTs to assess for their somatic alterations .

Example answer:
{"entities": [{"text": "cancer-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GISTs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genotype and allele were analyzed using SPSS 11.5 software .

Example answer:
{"entities": []}

Example input:
Sentence: A combination of fluorescence in situ hybridization ( FISH ) and Southern blot analysis demonstrated disruption of a synaptotagmin gene ( SYT14 ) at the 1q32 breakpoint .

Example answer:
{"entities": [{"text": "synaptotagmin", "type": "GeneOrGeneProduct"}, {"text": "SYT14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Utilizing bioinformatic tools , a platform of 9,412 single-nucleotide polymorphisms ( SNPs ) from 1,204 genes was designed and validated .

Example answer:
{"entities": []}

Example input:
Sentence: For this purpose we developed a high-throughput methodology to genotype both normal and deleted alleles using a chip-based matrix-assisted laser desorption-time-of-flight ( MALDI-TOF ) mass spectrometer and Multiplex PCR .

Example answer:
{"entities": []}

Example input:
Sentence: Bioinformatics gene ontology ( GO ) analysis of these 306 genes revealed significant enrichment in `` signal peptides '' , `` extracellular matrix '' and `` secreted proteins '' GO Terms .

Example answer:
{"entities": []}

Input:
Sentence: Protein conservation analysis was performed in six species using an online ClustalW tool .

## Item biored:test:754
Example input:
Sentence: Expression of mutated caveolin-1 in caveolin-1-null mouse fibroblasts failed to induce formation of caveolae due to retention of the mutated protein in the endoplasmic reticulum .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "caveolin-1-null", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: The frameshift caused by the c.1052delA deletion removes the last 81 amino acids of the protein , including the third zinc-finger motif .

Example answer:
{"entities": [{"text": "c.1052delA", "type": "SequenceVariant"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: The NDUFS2 contains a highly conserved protein kinase C phosphorylation site and the NDUFS3 subunit contains a highly conserved casein kinase II phosphorylation site which make them strong candidates for future mutation detection studies in enzymatic complex I-deficient patients .

Example answer:
{"entities": [{"text": "NDUFS2", "type": "GeneOrGeneProduct"}, {"text": "protein kinase C", "type": "GeneOrGeneProduct"}, {"text": "NDUFS3", "type": "GeneOrGeneProduct"}, {"text": "casein kinase II", "type": "GeneOrGeneProduct"}, {"text": "enzymatic complex I-deficient", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Expression of the normal and mutant G3 domains in mammalian cells showed that the mutation created a functional N-glycosylation site but did not adversely affect protein trafficking and secretion .

Example answer:
{"entities": []}

Example input:
Sentence: Molecular dynamic simulations of structural changes induced by L1503R indicated that the mean value of all-atom root-mean-squared-deviation was shifted from those with wild type or another mutation L1503Q that has been reported to be a group II mutation , which is susceptible to ADAMTS13 proteolysis .

Example answer:
{"entities": [{"text": "L1503R", "type": "SequenceVariant"}, {"text": "L1503Q", "type": "SequenceVariant"}, {"text": "ADAMTS13", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Molecular dynamic ( MD ) simulations showed that the overall effect of the mutation p.Val204Asp is disruption of hydrogen bonding between Gln223 and Glu441 , leading Ser198 and His438 to move away from each other with subsequent disruption of the catalytic triad functionality regardless of the type of substrate .

Example answer:
{"entities": [{"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Example input:
Sentence: Moreover , the only R to G mutation at position 76 was found to strongly impact on protein folding and oligomerization by altering the hydrogen bond network .

Example answer:
{"entities": [{"text": "R to G mutation at position 76", "type": "SequenceVariant"}]}

Example input:
Sentence: This frameshift mutation leads to a caveolin-1 protein that contains all known functional domains but has a change in only the final 20 amino acids of the C-terminus .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We demonstrated that the disease-causing mutations did not affect the structure of the protein , however both mutants showed a defect in oligomerisation .

Example answer:
{"entities": []}

Input:
Sentence: Protein structure was modeled based on the Protein data bank and mutated in DeepView v4.0.1 to predict the functional consequences of the mutation .

## Item biored:test:346
Example input:
Sentence: Seven novel single-nucleotide polymorphisms ( SNPs ) were also found , of which a change of leucine 269 to phenylalanine ( Leu269Phe ) was found in 12 of 18 patients with the Arg555Trp mutation .

Example answer:
{"entities": [{"text": "leucine 269 to phenylalanine", "type": "SequenceVariant"}, {"text": "Leu269Phe", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Arg555Trp", "type": "SequenceVariant"}]}

Example input:
Sentence: Nine distinct mutations including one small deletion mutation ( 46delS ) , two small insertion mutations ( 118-119insA and 125-126insAA ) , and six non-synonymous mutations ( A6V , P163S , E359K , P407Q , S429T and A442V ) were identified in 12 of the 486 patients ( nine with ventricular septal defect , two with Tetralogy of Fallot , and one with endocardial cushion defect ) .

Example answer:
{"entities": [{"text": "46delS", "type": "SequenceVariant"}, {"text": "118-119insA", "type": "SequenceVariant"}, {"text": "125-126insAA", "type": "SequenceVariant"}, {"text": "A6V", "type": "SequenceVariant"}, {"text": "P163S", "type": "SequenceVariant"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "P407Q", "type": "SequenceVariant"}, {"text": "S429T", "type": "SequenceVariant"}, {"text": "A442V", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Tetralogy of Fallot", "type": "DiseaseOrPhenotypicFeature"}, {"text": "endocardial cushion defect", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CD72 polymorphisms associated with alternative splicing modify susceptibility to human systemic lupus erythematosus through epistatic interaction with FCGR2B .

Example answer:
{"entities": [{"text": "CD72", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: HAT subjects had increased anti-inflammatory genes TGFB1 , TIMP1 , TIMP3 , and TIMP4 while proinflammatory PIG7 and MMP2 were also significantly increased ; all genes , p < 0.025 .

Example answer:
{"entities": [{"text": "TGFB1", "type": "GeneOrGeneProduct"}, {"text": "TIMP1", "type": "GeneOrGeneProduct"}, {"text": "TIMP3", "type": "GeneOrGeneProduct"}, {"text": "TIMP4", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PIG7", "type": "GeneOrGeneProduct"}, {"text": "MMP2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , patients with the IL-17F 7488TT genotype showed a severe thrombocytopenic state ( platelet count < 10 10 ( 9 ) /L ) at diagnosis than those with the IL-17F 7488TC genotype ( 20.9 % vs. 0 % , P=0.04 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "IL-17F", "type": "GeneOrGeneProduct"}, {"text": "7488TT", "type": "SequenceVariant"}, {"text": "thrombocytopenic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "7488TC", "type": "SequenceVariant"}]}

Example input:
Sentence: BACKGROUND : The plasminogen activator inhibitor type-1 ( PAI-1 ) has been implicated in the regulation of fibrinolysis and extracellular matrix components .

Example answer:
{"entities": [{"text": "plasminogen activator inhibitor type-1", "type": "GeneOrGeneProduct"}, {"text": "PAI-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: Plasminogen activator inhibitor type 1 serum levels and 4G/5G gene polymorphism in morbidly obese Hispanic patients with non-alcoholic fatty liver disease .

Example answer:
{"entities": [{"text": "Plasminogen activator inhibitor type 1", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Variants of coagulation factors [ factor V 1691G > A ( factor V Leiden ) , factor V 4070A > G ( factor V HR2 haplotype ) , factor VII Arg353Gln , factor XIII Val34Leu , beta-fibrinogen -455G > A , prothrombin 20210G > A ] , coagulation inhibitors [ tissue factor pathway inhibitor 536C > T , thrombomodulin 127G > A ] , fibrinolytic factors [ angiotensin converting enzyme intron 16 insertion/deletion , factor VII-activating protease 1601G > A ( FSAP Marburg I ) , plasminogen activator inhibitor 1-675 insertion/deletion ( 5G/4G ) , tissue plasminogen activator intron h deletion/insertion ] , and other factors implicated in influencing susceptibility to thromboembolic diseases [ apolipoprotein E2/E3/E4 , glycoprotein Ia 807C > T , methylenetetrahydrofolate reductase 677C > T ] were included .

## Item biored:test:704
Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Three BRCA1 abnormalities - 5382insC , C61G , and 4153delA - accounted for 51 % , 20 % , and 11 % of the identified mutations , respectively ..

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5382insC", "type": "SequenceVariant"}, {"text": "C61G", "type": "SequenceVariant"}, {"text": "4153delA", "type": "SequenceVariant"}]}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: A deletion of 84,682 base pairs covering the CFHR1 and CFHR3 genes was detected by direct polymerase chain reaction and gel electrophoresis .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: Four patients harbor yet non-described SRD5A2 gene mutations : a single nucleotide deletion ( del642T ) , a G158R amino acid substitution , a splice junction mutation ( IVS3+1G > A ) , and the insertion of a cytosine ( 217_218insC ) occurring at a CCCC motif .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G158R", "type": "SequenceVariant"}, {"text": "IVS3+1G > A", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Nine distinct mutations including one small deletion mutation ( 46delS ) , two small insertion mutations ( 118-119insA and 125-126insAA ) , and six non-synonymous mutations ( A6V , P163S , E359K , P407Q , S429T and A442V ) were identified in 12 of the 486 patients ( nine with ventricular septal defect , two with Tetralogy of Fallot , and one with endocardial cushion defect ) .

Example answer:
{"entities": [{"text": "46delS", "type": "SequenceVariant"}, {"text": "118-119insA", "type": "SequenceVariant"}, {"text": "125-126insAA", "type": "SequenceVariant"}, {"text": "A6V", "type": "SequenceVariant"}, {"text": "P163S", "type": "SequenceVariant"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "P407Q", "type": "SequenceVariant"}, {"text": "S429T", "type": "SequenceVariant"}, {"text": "A442V", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Tetralogy of Fallot", "type": "DiseaseOrPhenotypicFeature"}, {"text": "endocardial cushion defect", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The novel mutations include : eight missense mutations ( c.475G > A , p.G159R ; c.689C > G , p.P230R ; c.1094C > T , p.A365E ; c.1151C > A , p.A384D ; c.1182C > T , p.R428C ; c.1471C > T , p.R491C ; c.2444A > C , p.D815A ; c.2477G > C , p.W826S ) , two nonsense mutations ( c.1475G > A , p.W492X ; c.1627A > T , p.K543X ) , five splice site mutations ( c.855 +1G > C ; c.1092 +1G > A ; c. 1093-1G > T ; c.1239 +1G > A ; c.2380 +1G > A ) , and four deletions ( c.715_717delGTC , p.V239del ; c.304delA , p.N102DfsX4 ; c.1970_2177del , p.V657_G726 ; c.2113_2114delGG , p.G705RfsX16 ) .

Example answer:
{"entities": [{"text": "c.475G > A", "type": "SequenceVariant"}, {"text": "p.G159R", "type": "SequenceVariant"}, {"text": "c.689C > G", "type": "SequenceVariant"}, {"text": "p.P230R", "type": "SequenceVariant"}, {"text": "c.1094C > T", "type": "SequenceVariant"}, {"text": "p.A365E", "type": "SequenceVariant"}, {"text": "c.1151C > A", "type": "SequenceVariant"}, {"text": "p.A384D", "type": "SequenceVariant"}, {"text": "c.1182C > T ,", "type": "SequenceVariant"}, {"text": "p.R428C", "type": "SequenceVariant"}, {"text": "c.1471C > T", "type": "SequenceVariant"}, {"text": "p.R491C", "type": "SequenceVariant"}, {"text": "c.2444A > C", "type": "SequenceVariant"}, {"text": "p.D815A", "type": "SequenceVariant"}, {"text": "c.2477G > C", "type": "SequenceVariant"}, {"text": "p.W826S", "type": "SequenceVariant"}, {"text": "c.1475G > A", "type": "SequenceVariant"}, {"text": "p.W492X", "type": "SequenceVariant"}, {"text": "c.1627A > T", "type": "SequenceVariant"}, {"text": "p.K543X", "type": "SequenceVariant"}, {"text": "c.855 +1G > C", "type": "SequenceVariant"}, {"text": "c.1092 +1G > A", "type": "SequenceVariant"}, {"text": "c. 1093-1G > T", "type": "SequenceVariant"}, {"text": "c.1239 +1G > A", "type": "SequenceVariant"}, {"text": "c.2380 +1G > A", "type": "SequenceVariant"}, {"text": "c.715_717delGTC", "type": "SequenceVariant"}, {"text": "p.V239del", "type": "SequenceVariant"}, {"text": "c.304delA", "type": "SequenceVariant"}, {"text": "p.N102DfsX4", "type": "SequenceVariant"}, {"text": "c.1970_2177del", "type": "SequenceVariant"}, {"text": "p.V657_G726", "type": "SequenceVariant"}, {"text": "c.2113_2114delGG", "type": "SequenceVariant"}, {"text": "p.G705RfsX16", "type": "SequenceVariant"}]}

Input:
Sentence: In addition , we identified five novel COL3A1 mutations , including one deletion ( c.2187delA ) and one nonsense mutation ( c.2992C > T ) that could not be determined by the conventional total RNA method .

## Item biored:test:667
Example input:
Sentence: Dopamine is not essential for the development of methamphetamine-induced neurotoxicity .

Example answer:
{"entities": [{"text": "Dopamine", "type": "ChemicalEntity"}, {"text": "methamphetamine-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , we demonstrate that mice genetically engineered to have unilateral brain DA deficits develop METH-induced dopaminergic deficits that are of comparable magnitude on both sides of the brain .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "dopaminergic deficits", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although 3,4-methylenedioxymethamphetamine ( MDMA or ecstasy ) has been shown to damage brain serotonin ( 5-HT ) neurons in animals and possibly humans , little is known about the long-term consequences of MDMA-induced 5-HT neurotoxic lesions on functions in which 5-HT is involved , such as cognitive function .

Example answer:
{"entities": [{"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "MDMA-induced", "type": "ChemicalEntity"}, {"text": "neurotoxic lesions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here we show that the recently reported ability of L-dihydroxyphenylalanine to reverse the protective effect of alpha-methyl-para-tyrosine on METH-induced DA neurotoxicity is also confounded by drug effects on body temperature .

Example answer:
{"entities": [{"text": "L-dihydroxyphenylalanine", "type": "ChemicalEntity"}, {"text": "alpha-methyl-para-tyrosine", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Taken together , these findings demonstrate that DA is not essential for the development of METH-induced dopaminergic neurotoxicity and suggest that mechanisms independent of DA warrant more intense investigation .

Example answer:
{"entities": [{"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: This patient presented with symptoms of neuroleptic malignant syndrome ( NMS ) , thus demonstrating that NMS-like symptoms can occur after combined paroxetine and alprazolam treatment .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "neuroleptic malignant syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NMS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NMS-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Example input:
Sentence: Methamphetamine-induced neurotoxicity and microglial activation are not mediated by fractalkine receptor signaling .

Example answer:
{"entities": [{"text": "Methamphetamine-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fractalkine receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Methamphetamine ( METH ) damages dopamine ( DA ) nerve endings by a process that has been linked to microglial activation but the signaling pathways that mediate this response have not yet been delineated .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}]}

Example input:
Sentence: It is widely believed that dopamine ( DA ) mediates methamphetamine ( METH ) -induced toxicity to brain dopaminergic neurons , because drugs that interfere with DA neurotransmission decrease toxicity , whereas drugs that increase DA neurotransmission enhance toxicity .

Example answer:
{"entities": [{"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The symptoms of methamphetamine ( METH ) -induced psychosis are similar to those of paranoid type schizophrenia .

## Item biored:test:685
Example input:
Sentence: We conducted an association study assessing how PD risk in Italy was influenced by the serotonin transporter gene ( SLC6A4 ) polymorphic region 5-HTTLPR , consisting of an insertion/deletion ( long allele-L/short allele-S ) of 43 bp in the SLC6A4 promoter region .

Example answer:
{"entities": [{"text": "PD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "SLC6A4", "type": "GeneOrGeneProduct"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "insertion/deletion ( long allele-L/short allele-S ) of 43 bp", "type": "SequenceVariant"}]}

Example input:
Sentence: Thus , the -1021T allele with presumed low activity may be associated with misregulation of inflammation , which could contribute to the onset of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genetic polymorphism of the glutathione-S-transferase P1 gene ( GSTP1 ) and susceptibility to prostate cancer in the Kashmiri population .

Example answer:
{"entities": [{"text": "glutathione-S-transferase P1", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found the frequency of the three different genotypes of GSTP1 Ile105Val in our ethnic Kashmir population , i.e. , Ile/Ile , Ile/Val and Val/Val , to be 52.4 , 33.3 and 14.3 % among prostate cancer cases , 48.5 , 37.5 and 14 % among benign prostate hyperplasia cases and 73.8 , 21.3 and 5 % in the control population , respectively .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The p.A1369S variant was associated with a significantly lower risk of type 2 diabetes ( odds ratio [ OR ] 0.93 ; 95 % CI 0.91 , 0.95 ; P = 1.2 x 10 ( -11 ) ) .

Example answer:
{"entities": [{"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results strongly suggest that the E333D TRbeta mutation is responsible for the RTH phenotype in the proposita 's family .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our data indicate that the 5-HTTLPR polymorphic element within the SLC6A4 promoter may govern the genetic risk of PD in Italians .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "SLC6A4", "type": "GeneOrGeneProduct"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs25531 and the haplotype 5-HTTLPR/rs25531 did not associate with risk of PD .

Example answer:
{"entities": [{"text": "rs25531", "type": "SequenceVariant"}, {"text": "5-HTTLPR/rs25531", "type": "GeneOrGeneProduct"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We conclude that the thrombophilic FGG 10034 T gene variant does not contribute to the genetic susceptibility to PAD .

## Item biored:test:756
Example input:
Sentence: GATA4 mutations in 486 Chinese patients with congenital heart disease .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "congenital heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We identified and characterized a PABPN1 mutation in a Taiwanese family with OPMD .

Example answer:
{"entities": [{"text": "PABPN1", "type": "GeneOrGeneProduct"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The D487_S488_F489 deletion had been identified in two previously genotyped Chinese families .

Example answer:
{"entities": [{"text": "D487_S488_F489 deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation was responsible for the familial disorder through the substitution of a highly conserved arginine to tryptophan at codon 198 ( p.R198W ) .

Example answer:
{"entities": [{"text": "arginine to tryptophan at codon 198", "type": "SequenceVariant"}, {"text": "p.R198W", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutation analysis in a Chinese family with multiple endocrine neoplasia type 1 .

Example answer:
{"entities": [{"text": "multiple endocrine neoplasia type 1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The six unaffected family individuals carried alternative heterozygous mutations .

Example answer:
{"entities": []}

Example input:
Sentence: Using PCR-RFLP , we confirmed the heterozygous mutation in six affected family members and excluded it in three healthy members .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: First degree relatives carrying the mutation were clinically unaffected .

Example answer:
{"entities": []}

Example input:
Sentence: In our present study , a third Chinese family with this mutation was identified , suggesting that this mutation is a prevalent CYP17 mutation in the Chinese population .

Example answer:
{"entities": [{"text": "CYP17", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: This mutation was also present in two family members but absent in the other , unaffected family members and the 170 healthy Chinese individuals .

## Item biored:test:501
Example input:
Sentence: Genome-wide association studies have identified genomic loci , whose single-nucleotide polymorphisms ( SNPs ) predispose to prostate cancer ( PCa ) .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Four variants in two genes exceeded the multiple testing threshold for associations with prostate cancer mortality in fixed-effect meta-analyses .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: By histology-based analysis , the Cys/Cys genotype showed a significantly positive association with small-cell carcinoma ( OR=2.40 , 95 % CI=1.32-4.49 ) and marginally significant association with adenocarcinoma ( OR=1.32 , 95 % CI=0.98-1.77 ) .

Example answer:
{"entities": [{"text": "small-cell carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We performed comprehensive genomic profiling ( CGP ) for coding regions in more than 300 cancer-related genes of 186 GISTs to assess for their somatic alterations .

Example answer:
{"entities": [{"text": "cancer-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GISTs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The correlation between survival and NEK2 expression was analyzed in 359 patients with HCC using RNASeqV2 data available from The Cancer Genome Atlas ( TCGA ) website ( https : //tcga-data.nci.nih.gov/tcga/ ) .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Common germline genetic variation in antioxidant defense genes and survival after diagnosis of breast cancer .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: METHODS : We examined associations between common germline genetic variation in 13 genes involved in cell cycle control ( CCND1 , CCND2 , CCND3 , CCNE1 , CDK2 [ p33 ] , CDK4 , CDK6 , CDKN1A [ p21 , Cip1 ] , CDKN1B [ p27 , Kip1 ] , CDKN2A [ p16 ] , CDKN2B [ p15 ] , CDKN2C [ p18 ] , and CDKN2D [ p19 ] ) and survival among women diagnosed with invasive breast cancer participating in the SEARCH ( Studies of Epidemiology and Risk factors in Cancer Heredity ) breast cancer study .

## Item biored:test:673
Example input:
Sentence: This study investigated the possible association between three functional polymorphisms in the promoter region of the dopamine D4 receptor ( DRD4 ) gene and schizophrenia , depression , and heroin addiction .

Example answer:
{"entities": [{"text": "dopamine D4 receptor", "type": "GeneOrGeneProduct"}, {"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our data do not provide support for rs2230912 or the other polymorphisms studied within the P2RX7 locus , being involved in susceptibility to mood disorders .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "mood disorders", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Neither rs2230912 nor any of 8 other SNPs genotyped across P2RX7 was found to be associated with mood disorder in general , nor specifically with bipolar or unipolar disorder .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "mood disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bipolar or unipolar disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs25531 and the haplotype 5-HTTLPR/rs25531 did not associate with risk of PD .

Example answer:
{"entities": [{"text": "rs25531", "type": "SequenceVariant"}, {"text": "5-HTTLPR/rs25531", "type": "GeneOrGeneProduct"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , these three SNP markers were genotyped in 218 schizophrenia pedigrees of Taiwan ( 864 individuals ) for association analysis .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These observations strongly suggest that the -120-bp duplication polymorphism of DRD4 is associated with schizophrenia and that the -521 C/T polymorphism is associated with heroin addiction .

Example answer:
{"entities": [{"text": "-120-bp duplication", "type": "SequenceVariant"}, {"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-521 C/T", "type": "SequenceVariant"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Results of this analysis indicated that there is a strong finding of -120 bp duplication allele frequencies with schizophrenia ( p=0.008 ) and weak finding with -1240 L/S and for paranoid schizophrenia ( p=0.022 ) .

Example answer:
{"entities": [{"text": "-120 bp duplication", "type": "SequenceVariant"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-1240 L/S", "type": "SequenceVariant"}, {"text": "paranoid schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among these three SNPs , neither SNP4 , SNP7 , SNP18 has shown significant association with schizophrenia in single locus association analysis , nor any compositions of the three SNP haplotypes has shown significantly associations with the DSM-IV diagnosed schizophrenia .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although none of the observed linkages remained significant after multiple test correction through simulation , further analysis of NDE1 revealed an association between a tag-haplotype and schizophrenia ( P = 0.00046 ) specific to females , which proved to be significant ( P = 0.011 ) after multiple test correction .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In the haplotype-wise analysis , we detected an association between two markers ( rs6693503 and rs1805054 ) and three markers ( rs6693503 , rs1805054 and rs4912138 ) in HTR6 and METH-induced psychosis patients , respectively .

## Item biored:test:721
Example input:
Sentence: Distinct patterns of germ-line deletions in MLH1 and MSH2 : the implication of Alu repetitive element in the genetic etiology of Lynch syndrome ( HNPCC ) .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: The major histocompatibility complex ( MHC ) on chromosome 6p21 is a key contributor to the genetic basis of systemic lupus erythematosus ( SLE ) .

Example answer:
{"entities": [{"text": "major histocompatibility complex", "type": "GeneOrGeneProduct"}, {"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: More than 100 different heterozygous mutations in copper/zinc superoxide dismutase ( SOD1 ) have been found in patients with amyotrophic lateral sclerosis ( ALS ) , a fatal neurodegenerative disease .

Example answer:
{"entities": [{"text": "copper/zinc superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegenerative disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In two unrelated pedigrees of Alpers ' syndrome , each affected child was found to carry a homozygous mutation in exon 17 of the POLG locus that led to a Glu873Stop mutation just upstream of the polymerase domain of the protein .

Example answer:
{"entities": [{"text": "Alpers ' syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POLG", "type": "GeneOrGeneProduct"}, {"text": "Glu873Stop", "type": "SequenceVariant"}]}

Example input:
Sentence: These results indicated that the presence of CD72- * 2 allele decreases risk for human SLE conferred by FCGR2B-232Thr , possibly by increasing the AS isoform of CD72 .

Example answer:
{"entities": [{"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B-232Thr", "type": "GeneOrGeneProduct"}, {"text": "CD72", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report on a new allele at the arylsulfatase A ( ARSA ) locus causing late-onset metachromatic leukodystrophy ( MLD ) .

Example answer:
{"entities": [{"text": "arylsulfatase A", "type": "GeneOrGeneProduct"}, {"text": "ARSA", "type": "GeneOrGeneProduct"}, {"text": "metachromatic leukodystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We now describe 2 SLS patients whose disease is caused by large contiguous gene deletions of the ALDH3A2 locus on 17p11.2 .

## Item biored:test:714
Example input:
Sentence: The compound heterozygous mutations , c.892C > T and c.1072T > C , were identified in exon 3 of CHST6 in three patients .

Example answer:
{"entities": [{"text": "c.892C > T", "type": "SequenceVariant"}, {"text": "c.1072T > C", "type": "SequenceVariant"}, {"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Computer prediction indicated that the C111G polymorphism , which occurs 12 bases upstream from the translation start codon , might alter the secondary structure of the transcript .

Example answer:
{"entities": [{"text": "C111G", "type": "SequenceVariant"}]}

Example input:
Sentence: In our present study , a third Chinese family with this mutation was identified , suggesting that this mutation is a prevalent CYP17 mutation in the Chinese population .

Example answer:
{"entities": [{"text": "CYP17", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A 28 bp variable number of tandem repeats ( VNTR ) , a G/C single nucleotide polymorphism ( SNP ) , and a deletion of 6 bp at position 1494 were studied .

Example answer:
{"entities": [{"text": "28 bp variable number of tandem repeats", "type": "SequenceVariant"}, {"text": "G/C", "type": "SequenceVariant"}, {"text": "deletion of 6 bp at position 1494", "type": "SequenceVariant"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: Seven novel single-nucleotide polymorphisms ( SNPs ) were also found , of which a change of leucine 269 to phenylalanine ( Leu269Phe ) was found in 12 of 18 patients with the Arg555Trp mutation .

Example answer:
{"entities": [{"text": "leucine 269 to phenylalanine", "type": "SequenceVariant"}, {"text": "Leu269Phe", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Arg555Trp", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: With the exception of g.3318-34C > T and g.3352delG , all variants occurred heterozygously .

Example answer:
{"entities": [{"text": "g.3318-34C > T", "type": "SequenceVariant"}, {"text": "g.3352delG", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Three CYP17 gene mutations were identified from these patients .

Example answer:
{"entities": [{"text": "CYP17", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: Results : Three different sequence variants , c.-17T > C , c.171T > C , c.465G > T were identified .

## Item biored:test:682
Example input:
Sentence: The normal ( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG due to an insertion of ( GCG ) 4GCA into the normal allele in the Taiwanese OPMD subjects .

Example answer:
{"entities": [{"text": "( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG", "type": "SequenceVariant"}, {"text": "insertion of ( GCG ) 4GCA", "type": "SequenceVariant"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Compared with the control group , patients with chronic ITP had a significantly lower frequency of the IL-17F 7488CC genotype ( 0 % vs. 4.8 % , P < 0.05 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "chronic ITP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IL-17F", "type": "GeneOrGeneProduct"}, {"text": "7488CC", "type": "SequenceVariant"}]}

Example input:
Sentence: ( CCTTT ) 14 , which has been reported to have a higher activity in a reporter-construct , was significantly more abundant in POAG patients , while ( CCTTT ) 10 and ( CCTTT ) 13 were less common .

Example answer:
{"entities": [{"text": "( CCTTT ) 14", "type": "SequenceVariant"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "( CCTTT ) 10", "type": "SequenceVariant"}, {"text": "( CCTTT ) 13", "type": "SequenceVariant"}]}

Example input:
Sentence: The allele frequencies of polymorphisms at codon 787 CAG/CAA ( Gln/Gln ) in glioblastomas in Japan were G/G ( 82.4 % ) , G/A ( 10.8 % ) , A/A ( 6.8 % ) , corresponding to G 0.878 versus A 0.122 , significantly different from those in glioblastomas in Switzerland : G/G ( 27.2 % ) , G/A ( 28.4 % ) , A/A ( 44.4 % ) , corresponding to G 0.414 versus A 0.586 ( p < 0.0001 ) .

Example answer:
{"entities": [{"text": "codon 787 CAG/CAA", "type": "SequenceVariant"}, {"text": "Gln/Gln", "type": "SequenceVariant"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Significantly lower frequency of the A-C-C-G with higher frequency of A-C-A-G haplotypes was also noticed in subjects with DS ( P value =0.02089 and 0.00588 respectively ) .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Our results indicate that the PSA/ARE GG genotype confers an increased risk of PC especially among younger men .

Example answer:
{"entities": [{"text": "PSA/ARE", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: We found the frequency of the three different genotypes of GSTP1 Ile105Val in our ethnic Kashmir population , i.e. , Ile/Ile , Ile/Val and Val/Val , to be 52.4 , 33.3 and 14.3 % among prostate cancer cases , 48.5 , 37.5 and 14 % among benign prostate hyperplasia cases and 73.8 , 21.3 and 5 % in the control population , respectively .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Additionally , when PSA genotype was cross classified with CAG repeat , significantly more cases than both BPH and population controls were observed to have a short ( < 22 ) CAG/GG genotype ( P = 0.006 ) .

Example answer:
{"entities": [{"text": "PSA", "type": "GeneOrGeneProduct"}, {"text": "CAG repeat", "type": "SequenceVariant"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: FGG genotype frequencies were not significantly different between PAD patients ( CC : 57.3 % , CT : 36.7 % , TT : 5.8 % ) and control subjects ( CC : 60.9 % , CT : 33.5 % , TT 5.6 % ; p=0.35 ) .

## Item biored:test:729
Example input:
Sentence: Of particular interest are genes involved in defense against reactive oxygen species ( ROS ) because ROS are thought to cause DNA damage and contribute to the pathogenesis of cancer .

Example answer:
{"entities": [{"text": "reactive oxygen species", "type": "ChemicalEntity"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Loss of heterozygosity ( LOH ) analysis of tumour DNA revealed the loss of the wild-type allele .

Example answer:
{"entities": [{"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Tumor TS 1494del6 allele ( frequency of allelic loss , 36 % ) was protective ( for each allele with the deletion , based on an additive model , HR = 0.42 ; 95 % CI , 0.22 to 0.82 ; P = .0034 ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "1494del6", "type": "SequenceVariant"}]}

Example input:
Sentence: The first was to estimate the frequency of loss of heterozygosity ( LOH ) of the RB1 gene as a mechanism in disease causation in tumors of patients from India .

Example answer:
{"entities": [{"text": "RB1", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: BACKGROUND : Mammalian Ras genes regulate diverse cellular processes including proliferation and differentiation and are frequently mutated in human cancers .

Example answer:
{"entities": [{"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The identification of FH as a tumor suppressor was an unexpected finding and following the identification of subunits of succinate dehydrogenase in 2000 and 2001 , was only the second description of the involvement of an enzyme of intermediary metabolism in tumorigenesis .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Deregulation of these gene products may interfere with the signalling pathways that are involved in MCL tumour development and maintenance .

Example answer:
{"entities": [{"text": "MCL tumour", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It was first identified in Peutz-Jeghers syndrome as a tumor suppressor gene .

Example answer:
{"entities": [{"text": "Peutz-Jeghers syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations of TP53 and dysfunction of the Brca1 and/or Brca2 tumor-suppressor proteins have been implicated in the molecular pathogenesis of a large fraction of OSCs , but frequent somatic mutations in other well-established tumor-suppressor genes have not been identified .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "Brca1", "type": "GeneOrGeneProduct"}, {"text": "Brca2", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Loss or reduction in function of tumor suppressor genes contributes to tumorigenesis .

## Item biored:test:708
Example input:
Sentence: Novel CACNA1S mutation causes autosomal dominant hypokalemic periodic paralysis in a South American family .

Example answer:
{"entities": [{"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "hypokalemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In GCD , 18 patients with GCD type I had a mutation of arginine 555-to-tryptophan ( Arg555Trp ) and 1 patient with GCD type III ( Reis-Bucklers dystrophy ) , had the Arg124Leu mutation .

Example answer:
{"entities": [{"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "GCD type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 555-to-tryptophan", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "GCD type III", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Reis-Bucklers dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Arg124Leu", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : Cone dystrophy with supernormal rod response ( CDSRR ) is a retinal disorder characterized by reduced visual acuity , color vision defects , and specific alterations of ERG responses that feature elevated scotopic b-wave amplitudes at high luminance intensities .

Example answer:
{"entities": [{"text": "Cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "retinal disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "color vision defects", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the TGFBI gene in Indian patients with lattice corneal dystrophy ( LCD ) or granular corneal dystrophy ( GCD ) and to look for genotype-phenotype correlations .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "granular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further analyses of C. elegans RAB-28 , recently associated with autosomal-recessive cone-rod dystrophy , reveal that this small GTPase is exclusively expressed in ciliated neurons where it dynamically associates with IFT trains .

Example answer:
{"entities": [{"text": "C. elegans", "type": "OrganismTaxon"}, {"text": "RAB-28", "type": "GeneOrGeneProduct"}, {"text": "cone-rod dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GTPase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : The phenotype of cone dystrophy with supernormal rod response is tightly linked with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cone dystrophy with supernormal rod response is strictly associated with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "Cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Mutation screening of the GUCA1B gene in patients with autosomal dominant cone and cone rod dystrophy .

## Item biored:test:730
Example input:
Sentence: As previously observed for glioblastomas in Europe , there was a positive association between EGFR amplification and p16 deletion ( p=0.009 ) , whereas there was an inverse association between TP53 mutations and p16 deletion ( p=0.049 ) in glioblastomas in Japan .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results suggest that primary glioblastomas in Japan show genetic alterations similar to those in Switzerland , suggesting a similar molecular basis in caucasians and Asians , despite different genetic backgrounds , including different status of a polymorphism in the EGFR gene .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: Quantitative microsatellite analysis revealed LOH 10q in 41 of 59 ( 69 % ) glioblastomas .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PTCH1 gene mutations in exon 17 and loss of heterozygosity on D9S180 microsatellite in sporadic and inherited human basal cell carcinomas .

Example answer:
{"entities": [{"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "basal cell carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a genome-wide screen of DNA copy number alterations in 36 primary OSCs , we identified two tumors with apparent homozygous deletions of the NF1 gene .

Example answer:
{"entities": [{"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A homozygous deletion of the DOCK8 ( dedicator of cytokinesis 8 ) locus at chromosome 9p24 was found in a lung cancer cell line by array-CGH analysis .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "dedicator of cytokinesis 8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The allele frequencies of polymorphisms at codon 787 CAG/CAA ( Gln/Gln ) in glioblastomas in Japan were G/G ( 82.4 % ) , G/A ( 10.8 % ) , A/A ( 6.8 % ) , corresponding to G 0.878 versus A 0.122 , significantly different from those in glioblastomas in Switzerland : G/G ( 27.2 % ) , G/A ( 28.4 % ) , A/A ( 44.4 % ) , corresponding to G 0.414 versus A 0.586 ( p < 0.0001 ) .

Example answer:
{"entities": [{"text": "codon 787 CAG/CAA", "type": "SequenceVariant"}, {"text": "Gln/Gln", "type": "SequenceVariant"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Here , by allelic DNA copy number analysis using single-nucleotide polymorphism genotyping array and mass spectrometry , we report homozygous deletion in glioblastoma multiformes at chromosome 13q21 , where DACH1 gene is located .

## Item biored:test:749
Example input:
Sentence: MEASUREMENTS : Information regarding major bleeding episodes , strokes , and warfarin use was obtained from patients , relatives , primary physicians , and medical records .

Example answer:
{"entities": [{"text": "bleeding", "type": "DiseaseOrPhenotypicFeature"}, {"text": "strokes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : Ninety-three patients with APA were assessed for postoperative resolution of hypertension .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A combined clinical and genetic study was conducted in a cohort of patients with CDSRR , to substantiate these prior RESULTS : Seventeen patients from 13 families underwent a detailed ophthalmic examination including color vision testing , Goldmann visual fields , fundus photography , Ganzfeld and multifocal ERGs , and optical coherence tomography .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Twenty-four members of the family were clinically examined and genomic DNA was extracted .

Example answer:
{"entities": []}

Example input:
Sentence: PATIENTS AND METHODS : Six unrelated families and 10 sporadic patients were examined clinically .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: All but one patient were managed using cardiopulmonary bypass .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : All individuals in the study underwent a full clinical examination and the details of history were collected .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Blood sampling , karyotype , hormonal dosage , ultrasound , and ovarian biopsy were carried out on most patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : Six affected family members were examined clinically including visual acuity , color cornea photography , applanation tonography , and fundoscopy .

Example answer:
{"entities": []}

Example input:
Sentence: MATERIALS AND METHODS : The patients were examined using standard ophthalmic techniques .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: METHODS : Patients and family members were given complete physical , ophthalmic , and cardiovascular examinations .

## Item biored:test:728
Example input:
Sentence: A g-secretase inhibitor , DAPT , selectively depleted CD133 ( + ) cells , suppressed N1ICD and SKP2 , induced p27Kip1 , inhibited ACC growthin vivo , and sensitized CD133 ( + ) cells to radiation .

Example answer:
{"entities": [{"text": "g-secretase", "type": "GeneOrGeneProduct"}, {"text": "DAPT", "type": "ChemicalEntity"}, {"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "N1ICD", "type": "GeneOrGeneProduct"}, {"text": "SKP2", "type": "GeneOrGeneProduct"}, {"text": "p27Kip1", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A homozygous deletion of the DOCK8 ( dedicator of cytokinesis 8 ) locus at chromosome 9p24 was found in a lung cancer cell line by array-CGH analysis .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "dedicator of cytokinesis 8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Aberrant expression of UCHL1 in pediatric high-grade gliomas may promote cell invasion , transformation , and self-renewal properties , at least in part , by modulating Wnt/Beta catenin activity .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "gliomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Wnt/Beta catenin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As previously observed for glioblastomas in Europe , there was a positive association between EGFR amplification and p16 deletion ( p=0.009 ) , whereas there was an inverse association between TP53 mutations and p16 deletion ( p=0.049 ) in glioblastomas in Japan .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: UCHL1 might act as an oncogene in glioma within the gene network that imparts stem-like characteristics to these cancer cells .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PTCH1 gene mutations in exon 17 and loss of heterozygosity on D9S180 microsatellite in sporadic and inherited human basal cell carcinomas .

Example answer:
{"entities": [{"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "basal cell carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ubiquitin carboxyl-terminal esterase L1 ( UCHL1 ) is associated with stem-like cancer cell functions in pediatric high-grade glioma .

Example answer:
{"entities": [{"text": "Ubiquitin carboxyl-terminal esterase L1", "type": "GeneOrGeneProduct"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work we used SF188 and SJ-GBM2 cell lines to study the function of the ubiquitin carboxyl-terminal esterase L1 ( UCHL1 ) , a deubiquitinase de-regulated in several cancers , in pediatric high-grade gliomas .

Example answer:
{"entities": [{"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "ubiquitin carboxyl-terminal esterase L1", "type": "GeneOrGeneProduct"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gliomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: UCHL1 depletion in SF188 and SJ-GBM2 glioma cells was associated with decreased cell proliferation and invasion , along with a reduced ability to grow in soft agar and to form spheres ( i.e .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agar", "type": "ChemicalEntity"}]}

Input:
Sentence: Homozygously deleted gene DACH1 regulates tumor-initiating activity of glioma cells .

## Item biored:test:731
Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Sag inactivation by genetic deletion remarkably suppresses cell proliferation by inducing senescence , which is associated with accumulation of p16 , but not p53 .

Example answer:
{"entities": [{"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: As previously observed for glioblastomas in Europe , there was a positive association between EGFR amplification and p16 deletion ( p=0.009 ) , whereas there was an inverse association between TP53 mutations and p16 deletion ( p=0.049 ) in glioblastomas in Japan .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Quantitative microsatellite analysis revealed LOH 10q in 41 of 59 ( 69 % ) glioblastomas .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using Western blot analysis and RT-PCR , we have demonstrated that TD induces HIF-1a expression and activity in primary mouse astrocytes .

Example answer:
{"entities": [{"text": "TD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: UCHL1 might act as an oncogene in glioma within the gene network that imparts stem-like characteristics to these cancer cells .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A g-secretase inhibitor , DAPT , selectively depleted CD133 ( + ) cells , suppressed N1ICD and SKP2 , induced p27Kip1 , inhibited ACC growthin vivo , and sensitized CD133 ( + ) cells to radiation .

Example answer:
{"entities": [{"text": "g-secretase", "type": "GeneOrGeneProduct"}, {"text": "DAPT", "type": "ChemicalEntity"}, {"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "N1ICD", "type": "GeneOrGeneProduct"}, {"text": "SKP2", "type": "GeneOrGeneProduct"}, {"text": "p27Kip1", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work we used SF188 and SJ-GBM2 cell lines to study the function of the ubiquitin carboxyl-terminal esterase L1 ( UCHL1 ) , a deubiquitinase de-regulated in several cancers , in pediatric high-grade gliomas .

Example answer:
{"entities": [{"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "ubiquitin carboxyl-terminal esterase L1", "type": "GeneOrGeneProduct"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gliomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Aberrant expression of UCHL1 in pediatric high-grade gliomas may promote cell invasion , transformation , and self-renewal properties , at least in part , by modulating Wnt/Beta catenin activity .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "gliomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Wnt/Beta catenin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: UCHL1 depletion in SF188 and SJ-GBM2 glioma cells was associated with decreased cell proliferation and invasion , along with a reduced ability to grow in soft agar and to form spheres ( i.e .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agar", "type": "ChemicalEntity"}]}

Input:
Sentence: We found decreased cell proliferation of a series of glioma cell lines by forced expression of DACH1 .

## Item biored:test:751
Example input:
Sentence: Forty-two of the 70 coding SNPs result in nonsynonymous amino acid substitutions relative to the consensus sequence ; 28 SNPs were detected in the promoter , 12 in introns , 28 in the 3'-UTR , and 2 in the 5'-UTR .

Example answer:
{"entities": []}

Example input:
Sentence: An 18 kb genomic clone hybridizing with the h mu OR1 cDNA contains 63 and 489 bp exonic sequences flanked by splice donor/acceptor sequences .

Example answer:
{"entities": [{"text": "h mu OR1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Sanger sequence analysis of PTPN11 coding regions in a total of 17 MC families identified mutations in 10 of them ( 5 frameshift , 2 nonsense , and 3 splice-site mutations ) .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Exonic and intronic segments , 5 ' and 3 ' flanking regions of IRS2 ( 14.5 kb ) , were bidirectionally sequenced for single nucleotide polymorphism ( SNP ) discovery in 934 Hispanic children using 3730XL DNA Sequencers .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A total of 10 novel variants was recognized , among them four variants in the adjacent 5'-region of the GJB2 coding exon 2 ( g.3318-6T > A , g.3318-15C > T , g.3318-34C > T , g.3318-35T > G ) , a 6 base-pair deletion ( g.3455_3460del [ p.Asp46_Gln48delinsGlu ] ) , a variant leading to a stop codon ( g.3512C > A [ p.Tyr65X ] ) , synonymous variants ( g.3395C > T [ p.Thr26 ] , g.3503C > T [ p.Asn62 ] , g.3627A > C [ p.Arg104 ] ) , and one non-synonymous variant ( g.3816C > A [ p.Val167Met ] ) .

Example answer:
{"entities": [{"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "g.3318-6T > A", "type": "SequenceVariant"}, {"text": "g.3318-15C > T", "type": "SequenceVariant"}, {"text": "g.3318-34C > T", "type": "SequenceVariant"}, {"text": "g.3318-35T > G", "type": "SequenceVariant"}, {"text": "g.3455_3460del", "type": "SequenceVariant"}, {"text": "p.Asp46_Gln48delinsGlu", "type": "SequenceVariant"}, {"text": "g.3512C > A", "type": "SequenceVariant"}, {"text": "p.Tyr65X", "type": "SequenceVariant"}, {"text": "g.3395C > T", "type": "SequenceVariant"}, {"text": "p.Thr26", "type": "SequenceVariant"}, {"text": "g.3503C > T", "type": "SequenceVariant"}, {"text": "p.Asn62", "type": "SequenceVariant"}, {"text": "g.3627A > C", "type": "SequenceVariant"}, {"text": "p.Arg104", "type": "SequenceVariant"}, {"text": "g.3816C > A", "type": "SequenceVariant"}, {"text": "p.Val167Met", "type": "SequenceVariant"}]}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Specific PRC primers were designed to amplify all 14 exons of the HGD gene with the flanking intronic sequences including the splice site sequences .

Example answer:
{"entities": [{"text": "HGD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: Exons and flanking intron sequences of the TGFBI gene were amplified by PCR with specific primers .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: All of the 65 coding exons and their flanking intronic boundaries of FBN1 were amplified in the proband by polymerase chain reaction and followed by direct sequencing .

## Item biored:test:689
Example input:
Sentence: RESULTS : The child had a height of -4 SD , elevated serum GH concentrations , abnormally low serum IGF-I and IGFBP-3 concentrations and normal GHBP concentrations .

Example answer:
{"entities": [{"text": "GH", "type": "GeneOrGeneProduct"}, {"text": "IGF-I", "type": "GeneOrGeneProduct"}, {"text": "IGFBP-3", "type": "GeneOrGeneProduct"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: His apoE phenotype was apoE3/2 and he had mild dyslipidemia with a mid-band on polyacrylamide gel electrophoresis .

Example answer:
{"entities": [{"text": "apoE", "type": "GeneOrGeneProduct"}, {"text": "apoE3/2", "type": "GeneOrGeneProduct"}, {"text": "dyslipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "polyacrylamide", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The affected 6-year-old boy had red skin at birth and subsequently developed skin fragility , progressive plantar keratoderma , nail dystrophy , and alopecia .

Example answer:
{"entities": [{"text": "skin fragility", "type": "DiseaseOrPhenotypicFeature"}, {"text": "plantar keratoderma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nail dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alopecia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Tak1 ( col2 ) mice displayed severe chondrodysplasia with runting , impaired formation of secondary centres of ossification , and joint abnormalities including elbow dislocation and tarsal fusion .

Example answer:
{"entities": [{"text": "Tak1", "type": "GeneOrGeneProduct"}, {"text": "col2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "chondrodysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "joint abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "elbow dislocation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tarsal fusion", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We present a Canadian FPLD3 kindred with an affected mother who had loss of fat on arms and legs , but no increase in facial , neck , suprascapular or abdominal fat .

Example answer:
{"entities": [{"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: She had profound insulin resistance , diabetes , severe hypertriglyceridemia and relapsing pancreatitis , while her pre-pubescent daughter had normal fat distribution but elevated plasma triglycerides and C-peptide and depressed high-density lipoprotein cholesterol .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertriglyceridemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pancreatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "triglycerides", "type": "ChemicalEntity"}, {"text": "C-peptide", "type": "ChemicalEntity"}, {"text": "high-density lipoprotein cholesterol", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 3-year-old Chinese boy presented with prominent clinical features of malonic aciduria , including developmental delay , short stature , brain abnormalities and massive excretion of malonic acid and methylmalonic acid .

Example answer:
{"entities": [{"text": "malonic aciduria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "short stature", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "malonic acid", "type": "ChemicalEntity"}, {"text": "methylmalonic acid", "type": "ChemicalEntity"}]}

Input:
Sentence: We report a 3-month-old Taiwanese boy with initial presentation of a lack of subcutaneous fat , prominent musculature , generalized eruptive xanthomas , and extreme hypertriglyceridemia .

## Item biored:test:657
Example input:
Sentence: Recent data highlight the presence , in HIV-1-seropositive patients with lymphoma , of p17 variants ( vp17s ) endowed with B-cell clonogenicity , suggesting a role of vp17s in lymphomagenesis .

Example answer:
{"entities": [{"text": "HIV-1-seropositive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "lymphomagenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Importantly , 35 % ( 6/17 ) are tandem mutations , including 4 UV signature CC to TT transitions possibly linked to modulated DNA repair caused by the immunosuppressive drug cyclosporin A ( CsA ) .

Example answer:
{"entities": [{"text": "CC to TT", "type": "SequenceVariant"}, {"text": "cyclosporin A", "type": "ChemicalEntity"}, {"text": "CsA", "type": "ChemicalEntity"}]}

Example input:
Sentence: A common single nucleotide polymorphism ( SNP ) , G472A , codes for a Val158Met substitution and results in a fourfold down regulation of enzyme activity .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "Val158Met", "type": "SequenceVariant"}]}

Example input:
Sentence: Phosphatidylinositol 3-kinase p85alpha regulatory subunit gene Met326Ile polymorphism in women with polycystic ovary syndrome .

Example answer:
{"entities": [{"text": "Phosphatidylinositol 3-kinase", "type": "GeneOrGeneProduct"}, {"text": "p85alpha", "type": "GeneOrGeneProduct"}, {"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "polycystic ovary syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We investigated the mechanisms responsible for the functional disparity on B cells between a wild-type p17 ( refp17 ) and a vp17 named S75X .

Example answer:
{"entities": [{"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One patient with a severe cellular and clinical phenotype was a compound heterozygote with POLG1 mutations in the polymerase and exonuclease domain intrans .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In a prospective study involving 74 MFA patients and 170 control subjects , we identified four patients harboring a heterozygous single nucleotide polymorphism in exon 6 of the PrlR gene , encoding Ile ( 146 ) -- > Leu substitution in its extracellular domain .

Example answer:
{"entities": [{"text": "MFA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "PrlR", "type": "GeneOrGeneProduct"}, {"text": "Ile ( 146 ) -- > Leu", "type": "SequenceVariant"}]}

Example input:
Sentence: These results strongly suggest that the E333D TRbeta mutation is responsible for the RTH phenotype in the proposita 's family .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Three patients were heterozygous for A207D , G196S , and R266W substitutions .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "A207D", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "R266W", "type": "SequenceVariant"}]}

Input:
Sentence: Three patients with the triple polymerase substitution pattern ( rtV173L + rtL180M + rtM204V ) had associated changes in the envelope gene ( sE164D + sI195M ) .

## Item biored:test:750
Example input:
Sentence: EXPERIMENTAL DESIGN : Genomic DNA was purified from peripheral blood mononuclear cells or tissue specimens .

Example answer:
{"entities": []}

Example input:
Sentence: After informed consent was obtained , genomic DNA was extracted from the venous blood of all participants .

Example answer:
{"entities": []}

Example input:
Sentence: GENETIC ANALYSIS : Genomic DNA was extracted from peripheral blood leukocytes and mutation analysis of the entire coding sequence of the TSHR gene was performed in both children and their parents by direct DNA sequencing .

Example answer:
{"entities": [{"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genomic DNA was isolated from the leukocytes and genotyping was performed using the Sequenom platform .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA was extracted from peripheral blood of 11 family members , and the coding region of CHST6 was amplified by the polymerase chain reaction ( PCR ) method .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genomic DNA was extracted from the women 's leukocytes and genotyped .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Peripheral blood samples were collected and genomic DNA was extracted from the leukocytes .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA was isolated from the white blood cells of all family members of the affected case following standard established protocols .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA was prepared from the peripheral blood leukocytes of at least one affected woman from each family .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}]}

Example input:
Sentence: Genomic DNA was isolated from the venous blood leukocytes of 322 unrelated patients with schizophrenia , 156 patients with depression , 300 patients with heroin addiction , and 300 healthy unrelated individuals .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Genomic DNA was extracted from leukocytes of venous blood of six individuals in the family and 170 healthy Chinese individuals .

## Item biored:test:652
Example input:
Sentence: b ( + ) IVSI-110 ) and that this genetic combination has been selected within the population of b ( 0 ) -thalassemia patients , due to functional association with high HbF .

Example answer:
{"entities": [{"text": "b ( 0 ) -thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HbF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Significantly lower frequency of the A-C-C-G with higher frequency of A-C-A-G haplotypes was also noticed in subjects with DS ( P value =0.02089 and 0.00588 respectively ) .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients were genotyped for rs4704559 , rs10942891 and rs4704560 by allelic discrimination with Taqman assays .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "rs4704559", "type": "SequenceVariant"}, {"text": "rs10942891", "type": "SequenceVariant"}, {"text": "rs4704560", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Significant differences were detected in genotypic distribution ( p = 0.04 ) as well as the allelic frequency ( p = 0.003 ) between the SHCM patients and controls .

Example answer:
{"entities": [{"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In particular , subjects with stage IV had a two times higher probability of having either IL1B-31TT ( or IL1B-511CC ) genotype compared with stage I subjects .

Example answer:
{"entities": [{"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: HBV lamivudine-resistant strains were detected in 3 of 15 mono-infected chronic hepatitis B patients and 10 of 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Twenty-four of 113 ( 21 % ) gastric cancer patients had the II , 57 ( 51 % ) the ID , and 32 ( 28 % ) the DD genotype .

Example answer:
{"entities": [{"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Example input:
Sentence: The latter group was further sub-divided into 13 occult HBV ( HBsAg-negative ) and 7 overt HBV ( HBsAg- positive ) patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "HBsAg-negative", "type": "ChemicalEntity"}, {"text": "HBsAg-", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The HBV viral loads for mono-infected and co-infected patients ranged from 3.32 x 10 ( 2 ) to 3.82 x 10 ( 7 ) and < 200 to 4.40 x 10 ( 3 ) copies/ml , respectively .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: The distribution of HBV genotypes among these patients was A ( n = 9 ; 50 % ) , D ( n = 4 ; 22.2 % ) , G ( n = 3 ; 16.7 % ) , and F ( n = 2 ; 11.1 % ) .

## Item biored:test:678
Example input:
Sentence: This single nucleotide polymorphism ( SNP ) seemed to be functional as it was associated with decreased lung cancer risk .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Common single nucleotide polymorphisms ( SNPs ) within this gene , rs6232 and rs6235 , are associated with obesity .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Four SNPs , including rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , in CFH showed a significant association with wet AMD in the cohort of this study .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This mutation was linked to a novel single nucleotide polymorphism ( SNP ) in intron 3 ( IVS3 + 18C > T ) .

Example answer:
{"entities": [{"text": "IVS3 + 18C > T", "type": "SequenceVariant"}]}

Example input:
Sentence: A single nucleotide polymorphism at position 388 of the FGFR4 amino-acid sequence results in the substitution of glycine ( Gly ) with arginine ( Arg ) and higher frequency of the ArgArg genotype was previously found in prostate cancer patients .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}, {"text": "glycine ( Gly ) with arginine ( Arg )", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The non-synonymous SNP rs2230912 ( resulting in amino-acid polymorphism Q460R ) showed the strongest association and has been postulated to be pathogenically relevant .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "Q460R", "type": "SequenceVariant"}]}

Example input:
Sentence: TS enhancer region , 3R G > C single nucleotide polymorphism ( SNP ) , and TS 1494del6 polymorphisms were assessed in both fresh-frozen normal mucosa and tumor .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "G > C", "type": "SequenceVariant"}, {"text": "1494del6", "type": "SequenceVariant"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A common single nucleotide polymorphism ( SNP ) , G472A , codes for a Val158Met substitution and results in a fourfold down regulation of enzyme activity .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "Val158Met", "type": "SequenceVariant"}]}

Example input:
Sentence: DiGeorge and Velocardiofacial syndromes ( DGS/VCFS ) are endowed by a similar complex phenotype including cardiovascular , craniofacial , and thymic malformations , and are associated with heterozygous deletions of 22q11 chromosomal band .

Example answer:
{"entities": [{"text": "DiGeorge and Velocardiofacial syndromes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiovascular , craniofacial , and thymic malformations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In more than 98 % of cases , the disease is associated with a G to A or G to C substitution at nucleotide position 1138 ( p.G380R ) of the fibroblast growth factor receptor 3 ( FGFR3 ) gene .

Example answer:
{"entities": [{"text": "G to A or G to C substitution at nucleotide position 1138", "type": "SequenceVariant"}, {"text": "p.G380R", "type": "SequenceVariant"}, {"text": "fibroblast growth factor receptor 3", "type": "GeneOrGeneProduct"}, {"text": "FGFR3", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: A functional single nucleotide polymorphism ( SNP ) in the 3 ' untranslated region of the FGG gene ( FGG 10034C > T , rs2066865 ) has been associated with deep venous thrombosis and myocardial infarction .

## Item biored:test:697
Example input:
Sentence: Deletion 22q11.2 syndrome is the most frequent known microdeletion syndrome and is associated with a highly variable phenotype , including DiGeorge and Shprintzen ( velocardiofacial ) syndromes .

Example answer:
{"entities": [{"text": "Deletion 22q11.2 syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DiGeorge and Shprintzen ( velocardiofacial ) syndromes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Mal de Meleda ( MDM ) is palmoplantar erythrokeratoderma with an autosomal recessive inheritance and is caused by a mutation in the gene encoding SLURP-1 ( lymphocyte antigen 6/urokinase-type plasminogen activator receptor related protein-1 ) .

Example answer:
{"entities": [{"text": "Mal de Meleda", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "palmoplantar erythrokeratoderma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}, {"text": "lymphocyte antigen", "type": "GeneOrGeneProduct"}, {"text": "plasminogen activator receptor related protein-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: T and C alleles of SOD2 T2734C individually were linked to patients with bullous and erythematous erysipelas , respectively .

Example answer:
{"entities": [{"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "erythematous erysipelas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Of them , two patients carrying E359K mutation were from two generations in one family with ventricular septal defect ( VSD ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations of MKS3/TMEM67 , found recently in Meckel-Gruber syndrome ( MKS ) type 3 and Joubert syndrome ( JBTS ) type 6 , are predominantly truncating mutations .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "Meckel-Gruber syndrome ( MKS ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Joubert syndrome ( JBTS ) type 6", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Identification of novel type VII collagen gene mutations resulting in severe recessive dystrophic epidermolysis bullosa .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mucolipidosis type III ( MLIII ) is an autosomal recessive disorder affecting lysosomal hydrolase trafficking .

Example answer:
{"entities": [{"text": "Mucolipidosis type III", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLIII", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal recessive disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DiGeorge and Velocardiofacial syndromes ( DGS/VCFS ) are endowed by a similar complex phenotype including cardiovascular , craniofacial , and thymic malformations , and are associated with heterozygous deletions of 22q11 chromosomal band .

Example answer:
{"entities": [{"text": "DiGeorge and Velocardiofacial syndromes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiovascular , craniofacial , and thymic malformations", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Ehlers-Danlos syndrome , vascular type ( vEDS ) ( MIM # 130050 ) is an autosomal dominant disorder caused by type III procollagen gene ( COL3A1 ) mutations .
